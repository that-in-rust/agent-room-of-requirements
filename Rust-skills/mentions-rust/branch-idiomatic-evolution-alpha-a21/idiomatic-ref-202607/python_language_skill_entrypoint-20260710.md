# Python Language Skill Entrypoint

**Decision supported.** This section helps decide whether a task should activate python-coder-01 and under which of its eight modes. The seed title frames the theme as a skill entrypoint without stating the entrypoint's actual contract, that python-coder-01 activates only after classifying the Python surface and selecting one or more of its eight named modes before any planning or coding.

**Recommended default and causal basis.** Activate this skill for .py, pyproject.toml, CLI, service, async, or test work where correctness outranks quick scripting, and name surface plus modes before touching code. The mapped SKILL.md is built around that gate, its Mode Selection section lists Core Python, Typing, Boundary, Async, Resource, Packaging, Testing, and Review modes and its Workflow step one demands naming the surface and its dominant risk first.

**Operating conditions and assumptions.** The task is primarily Python and the repository's existing version targets, packaging tool, formatter, linter, type checker, and test runner are discoverable. This reference governs when and how to activate the python-coder-01 skill and route into its reference files, it is not itself a Python tutorial or pattern catalog.

**Failure boundary and alternatives.** The entrypoint framing collapses for framework-specific work, the skill's own research brief states web, data science, and deployment doctrine belong in companion skills, not this baseline. Bounded alternatives and recoveries: for Rust or TypeScript tasks route to the sibling coder skills the research brief names as repo-local sources, for governance questions route to the python quality and routing references in this corpus.

**Counterexample, gotchas, and operational comparison.** The skill explicitly preserves repo tooling, activating it to introduce ruff or pyright into a black-plus-flake8 repo inverts its own no-new-tools guardrail. Good: activating Boundary plus Testing modes for a CLI that parses untrusted CSV. Bad: activating the skill to restyle a Django template, framework doctrine is out of scope. Borderline: a one-off throwaway script, the skill applies only if correctness matters more than speed.

**Verification, evidence, and uncertainty.** Check the produced plan names a Python Work Mode and cites the surface classification before any implementation step. SKILL.md and all four reference files were read in full during this evolution, 392 content lines across five files. How the eight modes should compose when a task genuinely spans four or more of them is left to judgment by the skill.

**Second-order consequence.** Mode selection is really risk selection, each of the eight modes names the failure class it defends against, bad input, hidden Any, leaks, cancellation loss, import side effects, or packaging drift, so choosing modes forces the risk analysis the skill wants.

**Revision decision.** Open with the activation contract, classify the surface, pick modes, then load references progressively, so readers treat the entrypoint as a gate rather than a summary.

**Retained seed evidence.** The exact theme title and its skill-entrypoint framing remain unchanged. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

## Source Evidence Mapping Table

**Decision supported.** This section helps decide which recorded source may back which kind of Python skill claim. The seed map records one local row for SKILL.md with a generic skill-entrypoint role while the skill is actually a five-file bundle whose entrypoint deliberately defers content to a reference map and three reference files.

**Recommended default and causal basis.** Cite SKILL.md for activation and workflow claims, the reliability reference for pattern claims with PY1 identifiers, and the gates file for anti-pattern and command claims. SKILL.md's workflow step three instructs readers to load references progressively, reference-map.md first, then matching sections of the reliability reference, finishing with quality gates and anti-patterns.

**Operating conditions and assumptions.** The archive keeps the skill directory intact so relative reference links keep resolving. The table records provenance for this document's claims, it does not certify the external documentation URLs as current.

**Failure boundary and alternatives.** The four external URL rows, typing docs, pytest, mypy, and Ruff documentation, were never retrieved in this evolution and cannot corroborate any claim here. Bounded alternatives and recoveries: retrieve the four seed URLs in a future refresh cycle and upgrade their rows, or replace them with the research brief's more specific page-level links.

**Counterexample, gotchas, and operational comparison.** The research brief lists sixteen primary URLs that overlap only partially with the seed's four external rows, conflating the two lists would misstate what the skill consulted. Good: citing PY1-07 for cancellation guidance. Bad: asserting current mypy behavior from the unretrieved mypy.readthedocs.io row. Borderline: citing the research brief's PEP links, they name what the authors consulted, not what this evolution verified.

**Verification, evidence, and uncertainty.** Trace every claim in this file to a named file and section of the python-coder-01 bundle. The source map rows plus the full reads of all five bundle files performed during this evolution. Whether the skill's 2026-06-23 research snapshot still matches the four live documentation sites is unknowable from the archive.

**Second-order consequence.** The bundle's file split mirrors its progressive-disclosure teaching, the entrypoint stays 95 lines because depth lives in references, so citing SKILL.md alone under-represents the evidence the skill actually ships.

**Revision decision.** Expand the local row into the five-file bundle with each file's role, entrypoint, router, pattern reference, gate checklist, and research brief, and mark all external rows unretrieved.

**Retained seed evidence.** All source rows with their category, confidence, and synthesis-role columns remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| source_location_path_key | source_category_artifact_type | source_authority_confidence_level | source_usage_synthesis_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202606/python-coder-01/SKILL.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt |
| https://docs.python.org/3/library/typing.html | external_research_source_material | external_research_sourced_fact | primary typing module documentation |
| https://docs.pytest.org/en/stable/ | external_research_source_material | external_research_sourced_fact | primary Python testing framework documentation |
| https://mypy.readthedocs.io/ | external_research_source_material | external_research_sourced_fact | static type checking documentation and constraints |
| https://docs.astral.sh/ruff/ | external_research_source_material | external_research_sourced_fact | linting and formatting tool documentation |

## Pattern Scoreboard Ranking Table

**Decision supported.** This section helps decide which Python reliability patterns deserve default adoption pressure and in what order. The seed scoreboard scores three corpus-hygiene rules at 95, 91, and 88 while the skill ships its own fifteen-row scoreboard, PY1-01 through PY1-15, with parse-at-boundary ranked highest at 97.

**Recommended default and causal basis.** When prioritizing Python reliability work, take PY1-01 boundary parsing and PY1-02 Any containment first, they gate the value of every downstream typed pattern. The reliability reference opens with that scoreboard precisely so readers triage patterns by score before reading sections, its top four are boundary parsing 97, Any containment 95, dataclasses with explicit defaults 94, and cancellation preservation 94.

**Operating conditions and assumptions.** The codebase has a type checker configured so containment and parsing gains become visible. The scoreboard ranks adoption pressure for patterns within this skill's remit, not across other languages or corpora.

**Failure boundary and alternatives.** Neither scoreboard's numbers are measurements, the skill's scores encode its authors' emphasis, treating them as benchmark data would fabricate precision. Bounded alternatives and recoveries: rank by the repo's own incident history once it exists, or by lint-enforceability with ruff-detectable rules first.

**Counterexample, gotchas, and operational comparison.** Score-order adoption tempts teams to skip PY1-15, running formatter, linter, type checker, and tests as one gate, which is what makes the other fourteen enforceable. Good: fixing boundary parsing before adding Protocol seams. Bad: quoting score 97 as measured defect reduction. Borderline: promoting PY1-09 pathlib usage repo-wide, high value but mechanical enough to delegate to a lint rule.

**Verification, evidence, and uncertainty.** Confirm each promoted pattern cites its PY1 identifier and appears in the reliability reference. The fifteen-row Pattern Scoreboard read in full in python-reliability-reference.md. Relative payoff between mid-table patterns like PY1-10 logging and PY1-11 fixtures is authorial judgment the skill does not justify.

**Second-order consequence.** The two scoreboards operate at different altitudes, the seed ranks how to use references, the PY1 table ranks how to write Python, keeping both visible prevents the document layer from crowding out the code layer.

**Revision decision.** Import the PY1 scoreboard's top tier alongside the seed's document-hygiene rows and state that scores order emphasis, not evidence.

**Retained seed evidence.** All scored rows with their tier labels and failure-prevention targets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| pattern_identifier_stable_key | pattern_score_numeric_value | pattern_tier_adoption_level | pattern_failure_prevention_target |
| --- | ---: | --- | --- |
| `python_language_skill_entrypoint` | 95 | default_adoption_pattern_tier | Source Map First: Load local python language material before synthesizing skill entrypoint recommendations. |
| `python_language_skill_entrypoint` | 91 | default_adoption_pattern_tier | Evidence Boundary Split: Separate local facts, external facts, and inference before giving agent instructions. |
| `python_language_skill_entrypoint` | 88 | default_adoption_pattern_tier | Verification Gate Coupling: Attach each recommendation to at least one command, checklist, or review gate. |

## Idiomatic Thesis Synthesis Statement

**Decision supported.** This section helps decide what single claim should orient a builder applying this skill's guidance. The seed thesis repeats the generic load-local-first formula instead of the skill's actual thesis, that reliable Python comes from making dynamic behavior explicit where it matters, typed contracts, parsed boundaries, deterministic cleanup, import-safe modules, and failure-path tests.

**Recommended default and causal basis.** Phrase Python guidance from this reference as which implicit behavior becomes explicit and which gate proves it. The reliability reference states that premise verbatim in its opening section and immediately bounds it, type hints are guardrails but runtime inputs still need validation.

**Operating conditions and assumptions.** The consuming task can run at least one type, lint, or test gate to make explicitness checkable. The thesis orients activation and review of Python work under this skill, it does not compress the reference files' pattern detail.

**Failure boundary and alternatives.** An explicitness thesis over-applied turns quick automation scripts into ceremony, the skill's own When To Use line limits it to work where correctness matters more than quick scripting. Bounded alternatives and recoveries: a tooling-first thesis centered on ruff plus mypy adoption, weaker because the skill subordinates tools to repo preservation.

**Counterexample, gotchas, and operational comparison.** Explicitness claims decay into style policing without the gate coupling, the skill always pairs a rule with a checkable surface. Good: replacing a hidden Any dict with a parsed TypedDict at the CLI boundary. Bad: quoting pythonic as a requirement, the skill bans vague words in requirements. Borderline: enforcing frozen dataclasses everywhere, explicit but sometimes hostile to legitimate mutation.

**Verification, evidence, and uncertainty.** Confirm thesis clauses each carry an evidence label and trace to a named bundle section. The Premise section of the reliability reference and the guardrail list of SKILL.md. How far the explicitness bar should drop for exploratory notebooks is not addressed by the bundle.

**Second-order consequence.** The thesis unifies the guardrails, every do-not in SKILL.md, bare except, mutable defaults, broad Any, import-time IO, swallowed cancellation, is a way dynamic behavior stays implicit, so the guardrail list is the thesis stated negatively.

**Revision decision.** Restate the thesis as explicit-dynamic-behavior with its five named surfaces and keep the three evidence labels on its clauses.

**Retained seed evidence.** The three labeled thesis statements remain preserved beneath the evolved synthesis. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`local_corpus_sourced_fact`: The local row for `python_language_skill_entrypoint` contains 1 source path(s), which should be treated as the first retrieval surface for this theme.
`external_research_sourced_fact`: The external source map provides public documentation, repository, or ecosystem analogues where available.
`combined_evidence_inference_note`: Reliable use of Python Language Skill Entrypoint comes from loading the local corpus first, checking public ecosystem guidance second, and converting both into verification-backed agent decisions.

## Local Corpus Source Map

**Decision supported.** This section helps decide which file of the skill bundle to open first for a given Python question. The seed map lists SKILL.md alone with six heading signals while the skill's own reference-map.md prescribes a reading order across the bundle that this section should surface.

**Recommended default and causal basis.** Start point questions at reference-map.md, jump to the matching numbered section of the reliability reference, and read SKILL.md fully only when deciding activation or workflow. Reference-map.md's Use Order says read the Pattern Scoreboard first, open only sections matching the boundary being touched, and finish with High-Value Anti-Patterns and the Default Reliability Stack.

**Operating conditions and assumptions.** The question names its boundary, typing, parsing, async, resources, packaging, or testing. The map orders retrieval inside the python-coder-01 bundle, it does not rank other Python references in the archive.

**Failure boundary and alternatives.** Heading signals from SKILL.md alone route readers to workflow prose when most point questions, which exception shape, which fixture style, are answered in the reference files it links. Bounded alternatives and recoveries: collapse the bundle into one merged index, faster lookup but it would break the skill's progressive-disclosure design.

**Counterexample, gotchas, and operational comparison.** The gates file and the reliability reference overlap on anti-patterns, citing them interchangeably blurs which file's table, with or without the prefer column, is meant. Good: answering a cancellation question from section 3 of the reliability reference. Bad: reading all five files for a mutable-default question the anti-pattern table answers in one row. Borderline: using the research brief to answer tooling questions, it names sources rather than guidance.

**Verification, evidence, and uncertainty.** Spot-check that cited heading signals still exist in the bundle files at the recorded paths. Line counts and structural roles observed while reading all five bundle files in full. Whether newer sibling skill versions supersede this 202606 snapshot is not determinable from this theme's map.

**Second-order consequence.** The bundle is deliberately telescopic, 26-line router, 95-line entrypoint, 171-line reference, so retrieval cost tracks question depth, honoring that shape keeps point lookups under fifty lines of reading.

**Revision decision.** Add the four reference files as rows with their line counts and roles and record the router-first reading order.

**Retained seed evidence.** The local source row with its title and heading-signal columns remains preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| local_source_filepath_value | local_source_title_text | local_source_heading_signals | local_source_usage_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202606/python-coder-01/SKILL.md | python-coder-01 | Python Reliability; Overview; When To Use; Mode Selection; Workflow; Output Expectations | skill entrypoint or reusable agent prompt |

## External Research Source Map

**Decision supported.** This section helps decide how much trust an external row may carry in this theme's guidance. The seed map lists typing, pytest, mypy, and Ruff documentation with the external_research_sourced_fact label even though none of the four URLs was retrieved during this evolution.

**Recommended default and causal basis.** Treat every external claim in this theme as unverified until the specific page is retrieved and its retrieval recorded with a date. The evolution worked entirely from the local bundle, so the URL rows are candidate leads inherited from the seed generator, not consulted evidence.

**Operating conditions and assumptions.** No retrieval infrastructure or recorded fetch exists for these URLs within this corpus pass. The map inventories candidate external references for future refresh, it confers no authority on them today.

**Failure boundary and alternatives.** Labeling unretrieved links as sourced fact would launder candidates into corroboration and violate the evidence discipline this file teaches. Bounded alternatives and recoveries: substitute the research brief's sixteen primary links as the refresh shopping list, they include PEP 8, PEP 484, asyncio, contextlib, dataclasses, and packaging pages.

**Counterexample, gotchas, and operational comparison.** Docs.python.org/3/library/typing.html tracks the newest CPython, guidance fetched there may not hold for the older supported versions the skill says to preserve. Good: writing needs-retrieval beside a claim about current ruff format defaults. Bad: asserting mypy strictness flags from the unretrieved row. Borderline: using the URL set to infer the skill's tooling emphasis, suggestive and here corroborated by the local bundle.

**Verification, evidence, and uncertainty.** Check that no statement in this file rests solely on one of the four URL rows. The absence of any retrieval record for these URLs in this evolution's working notes. Whether the four URLs resolve today and what they currently say is unknown from the archive.

**Second-order consequence.** Unlike most themes, this seed's URL set is actually well-aimed, all four match the skill's tooling surface, so a future retrieval pass here has unusually high expected value per fetch.

**Revision decision.** Downgrade each row to unretrieved candidate status and note that the skill's own research brief already lists more specific page-level links for the same tools.

**Retained seed evidence.** All external source rows with their usage-role and boundary-label columns remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| external_source_url_value | external_source_name_text | external_source_usage_role | evidence_boundary_label_value |
| --- | --- | --- | --- |
| https://docs.python.org/3/library/typing.html | Python typing docs | primary typing module documentation | external_research_sourced_fact |
| https://docs.pytest.org/en/stable/ | pytest documentation | primary Python testing framework documentation | external_research_sourced_fact |
| https://mypy.readthedocs.io/ | mypy documentation | static type checking documentation and constraints | external_research_sourced_fact |
| https://docs.astral.sh/ruff/ | Ruff documentation | linting and formatting tool documentation | external_research_sourced_fact |

## Anti Pattern Registry Table

**Decision supported.** This section helps decide which failure shapes reviewers should actively hunt in Python changes. The seed registry lists three meta-level documentation failures while the skill ships an eleven-row High-Value Anti-Patterns table, mutable defaults, bare except, swallowed CancelledError, uncontained Any, assert for validation, import-time IO, print in libraries, manual open and close, stringly paths, blocking calls in async, and exception-to-None conversion.

**Recommended default and causal basis.** When reviewing Python changes under this skill, sweep the eleven-row table first and demand the prefer-column replacement for any hit. The gates file pairs every anti-pattern with its failure reason and a prefer column, and SKILL.md's guardrails re-state the five most damaging as hard do-nots.

**Operating conditions and assumptions.** Review time allows checking replacements rather than only flagging violations. The registry covers Python coding anti-patterns evidenced in the mapped bundle, not organizational or process failures.

**Failure boundary and alternatives.** Anti-pattern lists decay into taboo without the paired replacement, the skill's prefer column exists precisely to keep each rejection actionable. Bounded alternatives and recoveries: encode the mechanical rows into repo lint config and reserve the registry for judgment cases like exception-to-None conversions.

**Counterexample, gotchas, and operational comparison.** Assert remains idiomatic inside tests and for internal invariants, the ban targets external-input validation where -O optimization silently removes checks. Good: rejecting def f(items=[]) with a default_factory fix attached. Bad: flagging assert in a pytest test body. Borderline: print in a CLI's main function, the ban covers library behavior, not user-facing command output.

**Verification, evidence, and uncertainty.** For each registry row, locate its entry in the gates file's anti-pattern table. The High-Value Anti-Patterns table and the SKILL.md guardrail list read in full. Which anti-patterns dominate this repository's actual Python history is unmeasured, the registry inherits the skill's emphasis.

**Second-order consequence.** Most of the eleven rows are mechanically detectable, ruff and type checkers catch mutable defaults, bare except, and uncontained Any, so the registry doubles as a lint-configuration specification.

**Revision decision.** Import the eleven code rows beneath the three seed document rows, keeping each row's why-it-fails and prefer columns intact.

**Retained seed evidence.** All three seed registry rows with their causes, replacements, and detection signals remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| anti_pattern_failure_name | failure_cause_risk_reason | safer_default_replacement_pattern | detection_signal_review_method |
| --- | --- | --- | --- |
| context_free_summary_output | agent skips local corpus and produces generic advice | source_map_first_synthesis | verify every listed local path appears in the generated file |
| unsourced_recommendation_claims | guidance appears authoritative without source boundary | evidence_boundary_split_pattern | check for local, external, and inference labels |
| unverified_agent_instruction | recommendation cannot be checked by command or review gate | verification_gate_coupling | require concrete gate in generated reference |

## Verification Gate Command Set

**Decision supported.** This section helps decide which command or check proves a given Python recommendation was followed. The seed section names one repository verifier while the skill prescribes a repo-native gate battery, python -m pytest, python -m unittest, ruff check, ruff format --check, black --check, mypy, pyright, and python -m build.

**Recommended default and causal basis.** Run the repo's existing formatter, linter, type checker, and test commands as a single gate before declaring Python work done, skipping any only with a stated reason. The gates file lists exactly those commands and adds a discovery step, inspect pyproject.toml, setup.cfg, tox.ini, and noxfile.py first so command choice follows repo configuration.

**Operating conditions and assumptions.** The consuming project has the relevant tools configured, gates that never run are decoration. Gates here verify either this document's invariants or the Python work it recommends, each command must say which.

**Failure boundary and alternatives.** The listed repository verifier checks this reference file's structure, it cannot validate any Python code claim, conflating document gates with code gates would fake coverage. Bounded alternatives and recoveries: review-question gates from the skill's compact review pass for judgment claims no command checks, like whether a seam deserves a Protocol.

**Counterexample, gotchas, and operational comparison.** Running both ruff format --check and black --check on one repo double-formats, the battery is a menu keyed to repo config, not a checklist to run wholesale. Good: gating a boundary-parsing change on pytest plus mypy. Bad: citing the document verifier as proof code handles cancellation. Borderline: python -m build as a routine gate, valuable for packaging changes, noise for pure logic edits.

**Verification, evidence, and uncertainty.** Run the document verifier for this file and confirm each recommended code gate names a runnable command. The Quality Gate Commands section and its rg-based config discovery snippets in the gates file. Exact tool versions current projects should pin are outside the archive's knowledge.

**Second-order consequence.** The python -m prefix the skill prefers is itself a reliability pattern, it pins commands to the active interpreter and sidesteps PATH ambiguity, which is why the gates file states that preference explicitly.

**Revision decision.** Add the skill's gate battery with its inspect-config-first rule and keep the document verifier as the file-level gate.

**Retained seed evidence.** The original verifier command block remains preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`verification_gate_command_set`: Run the repository verifier after editing this file.

```bash
python3 agents-used-monthly-archive/idiomatic-references-202606/tools/verify_reference_generation.py --stage final
```

## Agent Usage Decision Guide

**Decision supported.** This section helps decide which protocol an agent should follow when activating this skill. The seed guide gives four generic bullets while the skill defines a precise agent protocol, classify surface, select modes, write REQ-PY requirements when behavior is unclear, load references progressively, and emit results in a fixed eight-part order.

**Recommended default and causal basis.** Have agents declare Python Work Mode and executable requirements first, then design boundaries, then implement, then present the verification matrix. SKILL.md's workflow and Output Expectations sections specify that protocol, including the WHEN THEN SHALL requirement grammar and the req-to-test traceability table shape.

**Operating conditions and assumptions.** The task's behavior is specifiable, pure exploration tasks may skip REQ-PY formalism with a stated reason. The guide steers agents doing Python work under this skill, it does not authorize restructuring the skill bundle itself.

**Failure boundary and alternatives.** An agent following the four seed bullets literally would produce a sourced essay, the skill wants a mode declaration, requirements, and a verification matrix before prose. Bounded alternatives and recoveries: for review-only tasks, run the gates file's compact review pass, Input, Types, Errors, Resources, Async, Imports, Tests, Gates, instead of the full protocol.

**Counterexample, gotchas, and operational comparison.** The skill bans vague requirement words, pythonic, safe, clean, robust, an agent quoting them back as requirements has failed step two. Good: an agent emitting REQ-PY-001.1 WHEN the CSV row lacks an id THEN the importer SHALL reject the row. Bad: an agent starting with implementation and back-filling requirements. Borderline: skipping the traceability table for a two-line fix, acceptable if the mode and gate are still named.

**Verification, evidence, and uncertainty.** Inspect agent output for the eight-part order and requirement identifiers before accepting the work. The Workflow, Output Expectations, and Guardrails sections of SKILL.md read in full. How strictly the eight-part order should bind small conversational tasks is left to judgment.

**Second-order consequence.** The REQ-PY identifier scheme makes agent output auditable the same way section identifiers do elsewhere in this corpus, a reviewer can trace any test back to the numbered requirement it proves.

**Revision decision.** Replace the generic bullets with the skill's protocol steps and the eight-part output order from Python Work Mode through Open Questions.

**Retained seed evidence.** The four seed usage bullets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`agent_usage_decision_guide`: Use this reference when a task mentions this theme, one of the listed local source paths, or a nearby technology/workflow surface.

- Start with the local corpus source map.
- Prefer patterns with explicit verification gates.
- Treat external sources as freshness and ecosystem checks, not replacements for local repo conventions.
- Preserve the evidence boundary labels when reusing recommendations.

## User Journey Scenario

**Decision supported.** This section helps decide whether this reference fits the user's journey before they invest reading time. The seed scenario names a generic Python maintainer while the skill's own When To Use section draws a sharper journey, a developer holding working-but-loose Python, scripts, CLIs, or async workflows, who must harden it without breaking repo conventions.

**Recommended default and causal basis.** Walk the user from surface classification through mode selection to one bounded hardening step proven by an existing repo gate. SKILL.md scopes itself to refactors needing clearer interfaces, fewer implicit globals, safer exceptions, and stronger test seams, and to reviews asking whether code survives bad inputs, partial state, and cancellation.

**Operating conditions and assumptions.** The user can name the surface and the repo's test or lint commands are runnable. The journey covers hardening and reviewing Python within existing repo conventions, not stack selection or framework doctrine.

**Failure boundary and alternatives.** The journey breaks for greenfield framework choices or data-science pipelines, the research brief explicitly defers those to companion skills. Bounded alternatives and recoveries: route governance-level journeys, which gates should this repo mandate, to the quality and routing references this corpus keeps adjacent.

**Counterexample, gotchas, and operational comparison.** Hardening enthusiasm that swaps tools mid-journey violates the skill's preservation rule, the journey upgrades code, not toolchains. Good: a maintainer hardening a subprocess-calling script with typed errors and a context-managed temp dir. Bad: a user seeking FastAPI architecture advice here. Borderline: a data engineer hardening a notebook-derived ETL script, in scope only once it becomes a module with tests.

**Verification, evidence, and uncertainty.** Ask whether the user can name surface, dominant risk, and existing gates, three yes answers confirm fit. The Overview and When To Use sections of SKILL.md. How long loose-to-reliable hardening takes on a real backlog is unmeasured.

**Second-order consequence.** The journey's first deliverable is always a classification, not code, which is why the skill can serve both implementers and reviewers, the same surface-and-risk statement drives either mode.

**Revision decision.** Recast the scenario as loose-to-reliable hardening, the user names the surface, its dominant risk, and the repo's existing gates before choosing patterns.

**Retained seed evidence.** The role, starting state, decision, and trigger lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Role based opening scenario: The Python maintainer is starting from scripts or services that need typing, fixtures, packaging, and lint discipline and needs a reference that turns source evidence into an executable next step.
Primary user starting state: The user has a `python_language_skill_entrypoint` task, one or more local source paths, and uncertainty about which pattern should drive implementation.
Decision being made: choosing how strict to make typing, tests, validation, and dependency hygiene for the current risk level.
Reference opening trigger: Open this file when the task mentions python language skill entrypoint, any mapped local source path, or an adjacent workflow with the same failure mode.

## Decision Tradeoff Guide

**Decision supported.** This section helps decide whether to adopt, adapt, or avoid a skill recommendation given the surrounding repo's conventions. The seed guide frames adopt, adapt, avoid abstractly without the skill's concrete tension, reliability strictness versus repository preservation when the repo's existing conventions are looser than the skill's defaults.

**Recommended default and causal basis.** Adopt the skill's safety rules unconditionally, adapt its style and structure advice to local convention, and avoid its packaging advice when the repo's build system is unfamiliar territory. The skill encodes both poles itself, its patterns demand typed boundaries and managed resources while its guardrails forbid adding new formatters, linters, package managers, or type checkers to a repo that has its own.

**Operating conditions and assumptions.** The repository's existing conventions are discoverable from config files and neighboring code. The guide arbitrates pattern-level choices, repo-wide toolchain migrations need an explicit migration request per the skill.

**Failure boundary and alternatives.** Strictness applied file-by-file inside a loose codebase produces two dialects, and preservation applied absolutely entrenches hazards like bare except that the skill says are never worth keeping. Bounded alternatives and recoveries: declare a bounded migration, one module hardened per cycle behind existing gates, when the local dialect is worth replacing.

**Counterexample, gotchas, and operational comparison.** Typed-return versus exception design is genuinely repo-relative, imposing the skill's preference where the codebase has a settled error idiom creates the two-dialect problem. Good: fixing a mutable default immediately in an otherwise untouched module. Bad: adding pyright to a mypy repo as part of a bug fix. Borderline: introducing frozen dataclasses into a dict-passing codebase, high value but a visible dialect break.

**Verification, evidence, and uncertainty.** Sample three neighboring files before adopting and record which branch was taken and why. The preservation sentences in SKILL.md's Overview and Guardrails read against its pattern demands. Where preservation deference should stop for borderline-harmful conventions is judgment.

**Second-order consequence.** The skill's own hierarchy resolves most conflicts, guardrails outrank patterns, patterns outrank style, so bare except loses to any local convention argument while import order never does.

**Revision decision.** Add the strictness-versus-preservation axis with the rule that safety patterns adopt immediately while tooling and style adapt to the repo until a migration is declared.

**Retained seed evidence.** The adopt, adapt, avoid, and cost-of-being-wrong rows remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| decision_option_name | when_to_choose_condition | tradeoff_cost_description | verification_question_prompt |
| --- | --- | --- | --- |
| Adopt when | local corpus and external evidence agree on the python language skill entrypoint pattern | fastest path, but can copy stale local assumptions | Does the selected pattern appear in the canonical source and current external evidence? |
| Adapt when | local sources are strong but public ecosystem guidance has changed | preserves repo fit, but requires explicit inference notes | Did the reference label the local fact, external fact, and combined inference separately? |
| Avoid when | source evidence is thin, conflicting, or unrelated to the user journey | prevents false confidence, but may require deeper research | Is there a confidence warning or adjacent reference route? |
| Cost of being wrong | wrong python language skill entrypoint guidance can send an agent to the wrong files, tests, or abstraction | wasted implementation loop and weaker verification | Would a reviewer know what to undo and what to inspect next? |

## Local Corpus Hierarchy

**Decision supported.** This section helps decide which file's text wins when the mapped sources overlap on a claim. The seed hierarchy crowns SKILL.md canonical with a thin-evidence warning, correctly, but misses that the canonical unit is the five-file bundle whose reference files carry most of the actionable content.

**Recommended default and causal basis.** Resolve intra-bundle conflicts toward the more specific file, a PY1 section beats an entrypoint summary of it. SKILL.md defers pattern depth to python-reliability-reference.md and gate detail to the anti-patterns file, so treating the entrypoint as the sole canonical text inverts where the guidance actually lives.

**Operating conditions and assumptions.** No true contradictions exist in the bundle, none were observed in full reads, only different levels of detail. The hierarchy governs precedence within this theme's mapped sources, it does not rank other Python material in the archive.

**Failure boundary and alternatives.** Single-source hierarchies hide staleness risk, if the bundle's 2026-06-23 research snapshot ages, every row here ages with it and no second local source flags the drift. Bounded alternatives and recoveries: invite adjacent-source discovery as the seed suggests, the python quality and routing themes in this corpus are the natural second opinions.

**Counterexample, gotchas, and operational comparison.** The sibling rust and typescript coder skills the brief names are structural templates for this bundle, not evidence about Python, citing them as corroboration would be circular. Good: preferring PY1-07's cleanup-then-reraise listing over the one-line guardrail restating it. Bad: dismissing the reference files because only SKILL.md is mapped. Borderline: citing the research brief's synthesis notes as guidance, they explain scope decisions rather than prescribe.

**Verification, evidence, and uncertainty.** For each precedence claim, cite the two overlapping passages and the observed difference. Side-by-side comparison of overlapping passages performed during the full bundle reads. Whether any newer python-coder skill revision exists elsewhere in the archive is unchecked from this theme.

**Second-order consequence.** The seed's confidence warning is the right instinct generalized wrongly, the risk is not too few files but zero independent files, all five share authorship and date, so corroboration must come from outside the bundle.

**Revision decision.** Re-role the rows, SKILL.md canonical for activation and workflow, the reliability reference canonical for patterns, the gates file canonical for anti-patterns and commands, the map and brief supporting.

**Retained seed evidence.** The hierarchy row and its confidence warning remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Classification vocabulary includes canonical, supporting, legacy, duplicate, and conflicting source roles.
Confidence warning: only one local corpus source is mapped, so this reference should invite adjacent-source discovery before becoming canonical policy.

| local_source_filepath_value | corpus_hierarchy_role | heading_signal_to_convert | reviewer_question_to_answer |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202606/python-coder-01/SKILL.md | canonical primary source | Python Reliability; Overview; When To Use | What guidance, warning, or example should this source contribute to Python Language Skill Entrypoint? |

## Theme Specific Artifact

**Decision supported.** This section helps decide what shape a completed run of this skill must leave behind. The seed artifact table asks for an abstract activation contract while the skill already defines the concrete artifact shape, a mode declaration, REQ-PY executable requirements, and a req-to-test traceability table with test_id, test_type, assertion, and target columns.

**Recommended default and causal basis.** Require the mode-requirements-traceability triple before accepting any nontrivial Python change made under this skill. SKILL.md's Output Expectations section mandates exactly that shape whenever requirements exist, making it the theme's native reviewable artifact.

**Operating conditions and assumptions.** Behavior is unclear enough to warrant requirements, trivially mechanical fixes may skip to the gate record. The artifact standardizes what a run of this skill must produce, it does not replace the skill's reference files.

**Failure boundary and alternatives.** An activation contract without the traceability table degrades into intentions, the table is what lets a reviewer confirm each requirement gained a test. Bounded alternatives and recoveries: the compact review-pass checklist as the artifact for review-only engagements where no code changes.

**Counterexample, gotchas, and operational comparison.** Requirements written with the skill's banned vague words pass the shape check while failing its substance, review the SHALL clauses for observability. Good: three REQ-PY rows each mapped to a named pytest test. Bad: a done message with neither mode nor gate named. Borderline: a traceability table whose assertions restate the requirement verbatim, traceable but untested in spirit.

**Verification, evidence, and uncertainty.** Check candidate artifacts for all three parts and confirm each table row names a runnable test. The Output Expectations section and its table schema in SKILL.md. Whether artifact upkeep survives contact with high-volume small fixes is untested in this repository.

**Second-order consequence.** The artifact doubles as a regression contract, because requirements carry revision suffixes like REQ-PY-001.2, later changes can show precisely which behavior clauses they altered.

**Revision decision.** Replace the abstract rows with the concrete triple, declared modes, REQ-PY requirements in WHEN THEN SHALL form, and the five-column traceability table.

**Retained seed evidence.** The artifact field rows with their completion rules and evidence hints remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Theme specific artifact: skill activation contract with progressive disclosure, misuse case, and verification gate.

| artifact_field_name | artifact_completion_rule | evidence_source_hint |
| --- | --- | --- |
| user_goal_statement | state the user's concrete goal before applying Python Language Skill Entrypoint | local corpus hierarchy plus critique findings |
| decision_boundary_rule | define the point where this reference should be used or avoided | decision tradeoff guide |
| verification_gate_rule | define the command, checklist, or review question that proves the artifact worked | verification gate command set |

## Worked Example Set

**Decision supported.** This section helps decide which worked example a reader should replay to learn this reference's method. The seed examples speak generically about loading sources while the bundle contains ready-made worked material, the frozen slots ImportReport dataclass and the cancellation-preserving run_job listing with cleanup-then-reraise.

**Recommended default and causal basis.** Replay the ImportReport and run_job listings in the target repo's style before writing new value types or async jobs under this skill. The reliability reference embeds those two listings as its only full code examples, one for value-data design under PY1-03 and one for cancellation discipline under PY1-07.

**Operating conditions and assumptions.** The reader's task resembles value-data modeling or async job control, other modes need composed examples. Worked examples here illustrate how to consume this reference, they are not tutorials replacing the bundle.

**Failure boundary and alternatives.** Two listings cannot cover the skill's eight modes, boundary parsing, packaging, and testing get rules and tables but no worked code, so examples must be marked thinner there. Bounded alternatives and recoveries: for boundary work, treat the gates file's rg config-discovery snippets as the worked example of the inspect-first habit.

**Counterexample, gotchas, and operational comparison.** Run_job's cleanup call itself can raise, masking the cancellation, production adaptations should shield or scope the cleanup, a nuance the fifteen-line listing omits. Good: porting ImportReport's default_factory shape to a new report type. Bad: copying run_job while dropping the raise after cleanup. Borderline: reusing the frozen slots combination on a class that later needs mutation, the example's guarantees become friction.

**Verification, evidence, and uncertainty.** Rerun the borrowed listing's behavior in a test, including the cancellation path for run_job. The two code listings read in full inside python-reliability-reference.md. How faithfully the listings compile against the newest CPython is unverified from the archive.

**Second-order consequence.** Both embedded listings teach the same meta-lesson, correctness lives in the type signature and control flow, frozen=True and the bare raise are one-token changes that carry the entire guarantee.

**Revision decision.** Anchor the good example on the two embedded listings with their PY1 citations and add a composed boundary example, CLI string to validated dataclass, marked as inference from the rules.

**Retained seed evidence.** The good, bad, and borderline seed lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Good example: Use Python Language Skill Entrypoint after loading the canonical source, confirming the external evidence boundary, and writing a verification gate before implementation.
Bad example: Use Python Language Skill Entrypoint as a generic tutorial while ignoring the mapped local paths, source hierarchy, and cost of being wrong.
Borderline case: Use Python Language Skill Entrypoint only after adding a confidence warning when local evidence is thin or conflicts with current ecosystem guidance.

## Outcome Metrics and Feedback Loops

**Decision supported.** This section helps decide which signals show this reference is earning its maintenance cost. The seed metrics name a coverage-preservation indicator while the skill defines a nine-point Default Reliability Stack that could serve directly as the measurable outcome rubric for every run.

**Recommended default and causal basis.** Record after each skill-driven task the nine-point stack outcome and whether the recommended pattern shipped, was adapted, or was rejected. The gates file's stack enumerates checkable outcomes, boundaries parsed, seams typed, Any contained, mutable defaults absent, resources managed, cancellation preserved, imports side-effect free, failure paths tested, and gates run or skipped with reasons.

**Operating conditions and assumptions.** Tasks actually declare when this reference guided them, otherwise the loop starves. This section tracks whether the reference improves decisions, the code metrics it borrows are evidence sources, not this document's own KPIs.

**Failure boundary and alternatives.** Gate metrics measure code health, not reference health, a repo can pass all nine while this document goes stale, so document-level and code-level loops must stay separate. Bounded alternatives and recoveries: periodic audit sampling of merged Python changes against the anti-pattern table when per-task recording proves too heavy.

**Counterexample, gotchas, and operational comparison.** Stack compliance saturates, once a module passes all nine the metric stops moving and reviewers must sample requirement quality instead. Good: logging that PY1-01 parsing was adopted in two CLI modules this cycle. Bad: claiming reference success from a green CI badge alone. Borderline: counting PY1 citations in review comments, gameable but cheap.

**Verification, evidence, and uncertainty.** Review the journal for stack outcomes and shipped-adapted-rejected records tied to PY1 identifiers. The nine-item Default Reliability Stack read in full in the gates file. The causal share of the reference versus reviewer skill in any improvement is unmeasurable here.

**Second-order consequence.** The ninth stack item is the honesty valve, gates run or skipped with an explicit reason, tracking skip reasons over time reveals which gates the team quietly considers noise.

**Revision decision.** Define two loops, a document loop sampling whether citations of this file led to accepted hardening changes, and a code loop scoring runs against the nine-point stack.

**Retained seed evidence.** The leading indicator, failure signal, and review cadence lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Leading indicator: the next agent can modify the package without weakening type, lint, or fixture coverage.
Failure signal: the reference says quality matters but gives no migration path from loose scripts to strict package code.
Review cadence: Re-run the verifier after every generated-reference edit and refresh external sources when public APIs, docs, or tooling releases change.

## Completeness Checklist

**Decision supported.** This section helps decide whether this reference is complete enough to accept, reuse, or refresh. The seed checklist verifies this reference's own sections exist but never checks the property the skill runs on, that each recommendation names its mode, its PY1 or guardrail source, its boundary condition, and its gate.

**Recommended default and causal basis.** Run the claim-level sweep during every reread pass and refuse acceptance while any recommendation lacks an attribute. The skill binds every rule to those four attributes, modes scope the work, PY1 identifiers cite the pattern, When To Use lines bound applicability, and the gate battery proves compliance.

**Operating conditions and assumptions.** The file remains small enough for a manual claim sweep, roughly its current size. The checklist audits this reference file before reuse or refresh, not the codebases that consume it.

**Failure boundary and alternatives.** A checklist of section presence can pass on a hollow document, completeness here must mean claim-level auditability, not heading-level coverage. Bounded alternatives and recoveries: automate the citation check with a script grepping for PY1 identifiers and mode names near recommendation verbs.

**Counterexample, gotchas, and operational comparison.** Checklists rot fastest at their newest items, the claim-level additions need the same verifier discipline as the structural ones. Good: rejecting acceptance because a retry recommendation lacked a gate. Bad: passing the file because all 26 headings exist. Borderline: a recommendation cited to SKILL.md as a whole, weak but traceable.

**Verification, evidence, and uncertainty.** Sweep the evolved sections and count recommendations missing any of the four attributes, zero is the pass bar. The attribute structure observed uniformly across the bundle during full reads. Whether claim-level auditing stays affordable as the reference grows is untested.

**Second-order consequence.** The four claim attributes mirror the skill's own output order, mode, requirement, design boundary, verification, so auditing this document and auditing a skill run use one rubric.

**Revision decision.** Add claim-level items, every recommendation names its mode, cites a bundle identifier or section, states a use-when condition, and attaches a runnable or reviewable gate.

**Retained seed evidence.** All seven seed checklist bullets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- The role scenario names the user, starting state, decision, and trigger for Python Language Skill Entrypoint.
- The decision guide includes Adopt when, Adapt when, Avoid when, and Cost of being wrong.
- The local corpus hierarchy identifies canonical and supporting sources or gives a confidence warning.
- The theme specific artifact is concrete enough to review without reading every mapped source.
- The examples cover good, bad, and borderline usage.
- The metrics section names one leading indicator and one failure signal.
- The adjacent routing section points to a better reference when this one is not the right fit.

## Adjacent Reference Routing

**Decision supported.** This section helps decide where to send a task this skill-entrypoint reference cannot finish. The seed routing derives three adjacents by splitting the theme name into python, language, and skill tokens instead of routing to the real neighbors, the python quality gates theme, the python routing-sources theme, and the sibling language coder skills.

**Recommended default and causal basis.** Hand off when the question stops being how to write this Python and becomes what should this repo mandate or which sources should this theme trust. The corpus contains python_quality_antipattern_gates and python_reference_routing_sources references for governance questions, and the research brief names rust-coder-02 and the typescript coder skills as this bundle's structural siblings.

**Operating conditions and assumptions.** A destination reference actually exists in the corpus for the concern in question. Routing hands off tasks this reference cannot serve, it does not summarize the destinations.

**Failure boundary and alternatives.** Token-derived adjacents are circular, they route the reader back to this same shelf under a synonym and waste the escape hatch this section exists to provide. Bounded alternatives and recoveries: external documentation with explicit unverified labels when no internal destination exists, notably for framework doctrine the bundle excludes.

**Counterexample, gotchas, and operational comparison.** Routing away too early forfeits this theme's unique value, the activation protocol, check whether mode selection answers the question before leaving. Good: sending which lint rules should CI enforce to the quality gates theme. Bad: routing python to language, the same shelf twice. Borderline: sending asyncio deep-dives outward, the bundle covers cancellation but not event-loop internals.

**Verification, evidence, and uncertainty.** Test each route by confirming the named destination file exists and covers the handed-off concern. The corpus file listing and the research brief's repo-local source list. The actual distribution of outbound task directions is estimated from corpus shape, not measured traffic.

**Second-order consequence.** The seed's own adjacent-guidance line already knows the answer, use reliability, routing, or quality references when the problem is governance rather than syntax, the three named rows just fail to follow it.

**Revision decision.** Route gate-policy questions to the quality theme, source-selection questions to the routing theme, and non-Python language work to the sibling coder skills.

**Retained seed evidence.** The three seed adjacent-reference lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Adjacent reference guidance: Use reliability, routing, or quality references when the problem is governance rather than syntax.
Adjacent reference 1: consider the python adjacent reference when the current task pivots away from python language skill entrypoint.
Adjacent reference 2: consider the language adjacent reference when the current task pivots away from python language skill entrypoint.
Adjacent reference 3: consider the skill adjacent reference when the current task pivots away from python language skill entrypoint.

## Workload Model

**Decision supported.** This section helps decide how much bundle a single task may load before it must be split. The seed model budgets ten source files and three delegated subtasks generically while this theme's real load shape is a 392-line five-file bundle engineered to be read telescopically, router first, sections on demand.

**Recommended default and causal basis.** Budget one mode's section family per question and escalate to the full bundle only when selecting modes or auditing a run. Reference-map.md exists solely to keep per-question reading under one numbered section, and SKILL.md's progressive-loading step makes partial reads the designed norm.

**Operating conditions and assumptions.** The question names its boundary so the router can dispatch it. The model budgets reading and synthesis effort for tasks using this theme, not general repository work.

**Failure boundary and alternatives.** A file-count budget misprices the work, five tiny files are cheaper than one untargeted read of a monolith, cost tracks sections opened, not files touched. Bounded alternatives and recoveries: precomputed mode-to-section digests if repeated tasks show the same lookups recurring.

**Counterexample, gotchas, and operational comparison.** The traceability and requirements ceremony adds fixed overhead per task, batching many tiny fixes under one requirement set amortizes it. Good: loading only section 3 for a cancellation question. Bad: quoting the whole scoreboard into a review of one function. Borderline: reading the research brief during implementation, background rather than load-bearing.

**Verification, evidence, and uncertainty.** Record loaded files and sections per task in the journal and flag tasks exceeding the mode budget. The measured line counts and telescopic structure of the five bundle files. Optimal budget for audit-class tasks that genuinely need breadth remains a judgment call.

**Second-order consequence.** This theme is the corpus's cheapest full read at 392 lines, so the usual anti-full-read pressure inverts, an agent uncertain about scope should just read the whole bundle rather than risk misrouting.

**Revision decision.** Restate the capacity bound in bundle terms, router plus one matching reference section per point question, full-bundle reads reserved for activation decisions and audits.

**Retained seed evidence.** The workload dimension rows with their boundary values and pressure points remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`combined_evidence_inference_note`: Treat Python Language Skill Entrypoint as a agent workflow operating reference, not as a prose summary.

| workload_dimension_name | workload_boundary_value | verification_pressure_point |
| --- | --- | --- |
| primary_usage_surface | agent planning, tool use, context loading, delegation, or skill/plugin execution where bad guidance compounds across long-running sessions | verify that the reference changes the next implementation or review action |
| bounded_capacity_model | one primary task, up to 10 source files, up to 3 delegated subtasks, and a written completion audit for every run | split the task or create a narrower reference when this boundary is exceeded |
| source_pressure_model | local heading signals include Python Reliability; Overview; When To Use; Mode Selection; Workflow; Output Expectations | compare guidance against canonical local sources before following external examples |
| artifact_pressure_model | required artifact is skill activation contract with progressive disclosure, misuse case, and verification gate | require the artifact before claiming the reference is operationally usable |

## Reliability Target

**Decision supported.** This section helps decide what measurable bar this reference's guidance must clear before reuse. The seed targets track label preservation and routing accuracy but omit the reliability bar the skill itself sets, that recommended Python fails safe, resources close on every path, cancellation propagates, and invalid input dies at the boundary.

**Recommended default and causal basis.** Reject any recommendation touching a failure path that omits its cleanup, re-raise, or rejection behavior. The skill's review questions make those the acceptance surface, are resources closed on success, error, and cancellation, does async preserve CancelledError, does untrusted data become typed before domain logic.

**Operating conditions and assumptions.** Reviewers actually read the failure-path clauses rather than pattern names alone. Targets here measure the reference's guidance quality, runtime reliability belongs to the consuming systems.

**Failure boundary and alternatives.** Document-level targets cannot certify runtime behavior, this section can only require that recommendations carry their fail-safe conditions, not that deployments honor them. Bounded alternatives and recoveries: spot audits of merged Python changes against the review-question list when systematic sampling is unstaffed.

**Counterexample, gotchas, and operational comparison.** Sampled-accuracy targets like 18 of 20 need a sampling owner, absent one the target is fiction. Good: a temp-dir recommendation naming cleanup on the exception path. Bad: recommending task cancellation handling without the re-raise. Borderline: citing a context manager without naming what its exit does on error, directionally safe but unspecified.

**Verification, evidence, and uncertainty.** Sweep evolved sections for failure-path claims and check each names its bound. The Python Review Questions list and the cancellation and resource sections of the reliability reference. Whether guidance-level bounds translate into deployed bounds depends on consumers this file cannot observe.

**Second-order consequence.** The skill treats reliability as a property of control-flow shape, with blocks, cleanup-then-reraise, parse-before-use, so guidance completeness genuinely is an upstream reliability control here.

**Revision decision.** Add a target that 100 percent of failure-path recommendations name their bound, the cleanup route, the re-raise, the validation error, verifiable by reading the guidance.

**Retained seed evidence.** All four seed reliability rows with thresholds and collection methods remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| reliability_target_name | measurable_threshold_value | evidence_collection_method |
| --- | --- | --- |
| source_boundary_preservation | 100 percent of recommendations keep local, external, and inference boundaries visible | review generated text for the three evidence labels before reuse |
| decision_accuracy_sample | at least 18 of 20 sampled uses route to the correct adopt, adapt, avoid, or adjacent-reference decision | sample downstream tasks and record reviewer verdicts |
| unsupported_claim_rate | zero unsupported production, security, latency, or reliability claims in final guidance | reject claims without source row, explicit inference note, or verification method |
| recovery_path_clarity | every avoid or failure case names the rollback, escalation, or next-reference route | inspect failure-mode and adjacent-routing sections together |

## Failure Mode Table

**Decision supported.** This section helps decide which failure shapes deserve standing mitigations when this reference drives work. The seed table lists document-drift and context-window failures but not the dominant failure of skill entrypoints, activation mismatch, the skill invoked for out-of-scope work or bypassed for exactly the work it exists to harden.

**Recommended default and causal basis.** When Python work arrives without a mode declaration, treat it as a suspected skipped activation and re-run classification before review. The bundle draws its scope edges explicitly, correctness-over-scripting in When To Use, framework doctrine deferred by the research brief, tool preservation in the guardrails, each edge is a place misactivation happens.

**Operating conditions and assumptions.** Reviewers know the artifact shape well enough to notice its absence. The table catalogs failures of using this reference and skill, not general production incident taxonomy.

**Failure boundary and alternatives.** Activation failures are silent, an agent that skipped the skill leaves no artifact saying so, detection requires noticing the missing mode declaration in the output. Bounded alternatives and recoveries: a CI check grepping diffs for new tool configs catches migration smuggling mechanically.

**Counterexample, gotchas, and operational comparison.** Mitigations that demand full-bundle rereads will be skipped under deadline, mitigations must be artifact-sized to survive. Good: catching a requirements list containing the word robust and bouncing it. Bad: shipping a review that never states which modes were considered. Borderline: activating the skill on a throwaway script, wasteful rather than harmful.

**Verification, evidence, and uncertainty.** Audit a sample of skill-driven changes for the four added failure signatures. The scope and guardrail boundaries observed across SKILL.md and the research brief. The base rate of activation mismatch in this repository's actual Python work is unmeasured.

**Second-order consequence.** All four added failures are detectable from the artifact shape alone, missing modes, missing REQ-PY rows, banned words in requirements, new tools in the diff, so artifact review is the single mitigation family.

**Revision decision.** Add rows for out-of-scope activation, skipped activation on qualifying work, vague-word requirements, and tool-migration smuggling, each with trigger and mitigation.

**Retained seed evidence.** All four seed failure rows with triggers and mitigations remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| failure_mode_name | likely_trigger_condition | required_mitigation_action |
| --- | --- | --- |
| source drift hides truth | external or local guidance changes after the reference was written | refresh public evidence, rerun local corpus gate, and mark stale claims before reuse |
| generic advice escapes review | agent copies plausible best practices without theme-specific verification | block completion until the verification gate names concrete command, reviewer question, or metric |
| context window loses plan | long-running session forgets early constraints or overwrites user intent | write checkpoint summaries and re-read plan before each destructive step |
| tool fanout outruns budget | parallel actions create conflicts, duplicate work, or unbounded external calls | cap fanout, assign ownership, and require merge/audit checkpoints |

## Retry Backpressure Guidance

**Decision supported.** This section helps decide when a failed operation may be retried or awaited longer and when it must escalate instead. The seed guidance covers retrying failed document verification but not the retry-adjacent discipline the skill teaches for code, timeouts and cancellation as first-class control flow with shielding and executor isolation for blocking work.

**Recommended default and causal basis.** Recommend async constructs only alongside their cancellation story, what re-raises, what cleans up, and what timeout bounds the wait. The skill's Async Mode names tasks, task groups, cancellation, timeouts, shielding, and blocking-call isolation as one concern set, and PY1-07 prescribes cleanup-then-reraise as the non-negotiable cancellation shape.

**Operating conditions and assumptions.** The code's supported Python version determines whether TaskGroup or older task idioms apply, the skill says preserve the repo's targets. This section governs both loops explicitly, document-verification retries and the async control-flow discipline this reference recommends, kept in separate paragraphs.

**Failure boundary and alternatives.** Retry guidance for documents and for code must not merge, one bounded retry for stale evidence is a research policy, task cancellation semantics are a runtime policy, conflating them confuses both. Bounded alternatives and recoveries: keeping the function synchronous when async adds no concurrency win, the skill prefers that over executor ceremony.

**Counterexample, gotchas, and operational comparison.** Bare except is the retry killer here, it swallows CancelledError and converts cooperative shutdown into a hang, the anti-pattern table flags exactly this. Good: a timeout-bounded await whose handler cleans up and re-raises. Bad: except Exception around an await swallowing cancellation. Borderline: shielding cleanup from cancellation, correct in shutdown paths, dangerous as a habit.

**Verification, evidence, and uncertainty.** Check every recommended async construct names its cancellation behavior and timeout bound. The Async Mode line, PY1-07 listing, and blocking-work rules read in full. Correct timeout budgets for this repository's actual workloads require measurements the bundle cannot supply.

**Second-order consequence.** Backpressure in this skill's world is the event loop itself, one blocking call stalls every task, which is why blocking-call isolation sits beside cancellation in the same mode rather than in a performance section.

**Revision decision.** Keep the seed's document-loop rules and add the code-loop contract, preserve CancelledError, bound waits with timeouts, isolate blocking calls, and never hide either behind broad except.

**Retained seed evidence.** All five seed retry and backpressure bullets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- Retry only after the failed verification signal is classified as transient, stale evidence, missing context, or true contradiction.
- Use one bounded retry for stale external evidence refresh, then escalate to a human or a narrower source-specific reference.
- Apply backpressure by stopping new generation or implementation work when source coverage, critique coverage, or verification gates are red.
- For long-running agent workflows, checkpoint after each batch and re-read the current spec before any broad rewrite, commit, push, or destructive operation.
- For distributed execution, assign one owner per generated file or theme batch and require merge-time verification of exact path, heading, and evidence-boundary invariants.

## Observability Checklist

**Decision supported.** This section helps decide which observability evidence must exist for reference-driven code and for the reference itself. The seed checklist records document-usage evidence but omits the code-observability contract the skill states, logging at adapters and orchestration boundaries, actionable messages, no secrets, and no print in library behavior.

**Recommended default and causal basis.** Require every adapter or orchestration recommendation from this reference to name where it logs and what a failure message must contain. PY1-10 draws exactly that line, library code must not rely on print for operational behavior, logging belongs at boundaries, and messages must stay diagnosable without leaking secrets.

**Operating conditions and assumptions.** The consuming project has a logging configuration the boundary code can rely on. This section keeps two ledgers, evidence about uses of this reference, and the logging discipline this reference tells builders to install.

**Failure boundary and alternatives.** Observability advice divorced from the layer becomes noise, per-function logging in pure domain code is clutter while a silent adapter is a blind spot, the boundary placement rule is the content. Bounded alternatives and recoveries: returned diagnostics instead of logging for pure library layers, the anti-pattern table lists that as the print replacement too.

**Counterexample, gotchas, and operational comparison.** Logging raw payloads alongside errors leaks secrets and personal data, the skill says actionable and secret-free, log identifiers and counts, not bodies. Good: a subprocess adapter logging command name, exit code, and duration. Bad: print statements inside a reusable parser. Borderline: debug-level payload logging behind a flag, useful in development, risky if it reaches production config.

**Verification, evidence, and uncertainty.** Grep recommended adapter code for logging calls at boundaries and print calls outside CLI output paths. The PY1-10 section and the print row of the anti-pattern table. Appropriate log retention and volume budgets are deployment-specific and outside the bundle.

**Second-order consequence.** The print ban and the logging rule are one rule seen twice, both route diagnostics through a filterable channel, which is also why the skill counts print among its detectable anti-patterns.

**Revision decision.** Retain the document ledger and add the code ledger, boundary-placed logging, actionable messages, secret hygiene, and print confined to CLI user output.

**Retained seed evidence.** All six seed observability bullets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- Record which local sources were loaded and which were intentionally skipped.
- Record the exact verification command, reviewer question, or rendered artifact used as proof.
- Record p50/p95/p99 latency or reviewer-time measurements when the reference affects runtime or workflow speed.
- Capture tool-call count, context files loaded, delegated tasks, retry count, and completion-audit outcome.
- Record leading indicator and failure signal from this file in the coverage manifest or journal when the reference drives real work.
- Keep audit evidence small enough to review: command output summary, changed-file list, and unresolved-risk notes are preferred over raw transcript dumps.

## Performance Verification Method

**Decision supported.** This section helps decide how a performance claim tied to this reference gets proven or rejected. The seed method measures reviewer navigation time but not the performance concern the skill actually flags, event-loop stalls from blocking calls and the memory discipline of slots dataclasses.

**Recommended default and causal basis.** Verify structural idioms by inspection first and demand latency measurements only where a stated budget exists. The blocking-work rule exists because one synchronous call on the loop degrades every concurrent task, and PY1-03 recommends slots=True when appropriate for memory and attribute discipline.

**Operating conditions and assumptions.** The recommendation sits on a concurrency- or memory-sensitive path, cold paths need no ceremony. This section verifies performance claims made by guidance from this reference, actual load testing belongs to the consuming project.

**Failure boundary and alternatives.** Document navigation speed and code latency are different quantities, a ten-minute review target says nothing about a stalled loop, the method must keep the two measurements apart. Bounded alternatives and recoveries: profiling sessions when a budget is missed and no structural idiom is obviously absent.

**Counterexample, gotchas, and operational comparison.** Slots=True breaks dynamic attribute assignment and some serialization libraries, the skill's when-appropriate hedge is load-bearing, not filler. Good: auditing an async handler for synchronous file reads and moving them out. Bad: claiming a service is fast because it uses dataclasses. Borderline: adding slots to every dataclass by default, cheap but occasionally breaking.

**Verification, evidence, and uncertainty.** For each performance recommendation, record the structural idiom present and any measured value against its stated budget. The blocking-work rules and the slots guidance read in full in the reliability reference. Concrete latency budgets for this repository's services are unknown to the bundle and must come from owners.

**Second-order consequence.** The skill's performance idioms are structural rather than tuned, isolate blocking work, choose slots, use pathlib correctly, so verifying their presence is cheaper and more durable than benchmarking constants.

**Revision decision.** Keep the reviewer-time gate for the document and add the code gate, any async recommendation names its blocking-call audit and any hot value type states its slots decision.

**Retained seed evidence.** The method, indicator, measurement packet, and pass and fail condition lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Performance method: require tool-call budgets, timeout budgets, and a resumable journal when the workflow exceeds one focused session.
Leading indicator to measure: the next agent can modify the package without weakening type, lint, or fixture coverage.
Failure signal to watch: the reference says quality matters but gives no migration path from loose scripts to strict package code.
Required measurement packet: capture input size, source count, tool-call count, wall-clock time, p50/p95/p99 latency where runtime applies, and reviewer decision time where documentation applies.
Pass condition: the reference must let a reviewer identify the correct next action, verification gate, and stop condition without reading unrelated files.
Fail condition: the reference encourages implementation before the workload, reliability target, and failure-mode table are explicit.

## Scale Boundary Statement

**Decision supported.** This section helps decide when a scaling question has outgrown this reference and must move elsewhere. The seed statement bounds document scale but not the scale seams the skill marks, single-skill scope that excludes framework doctrine, single-repo tool preservation, and async guidance that stops at process-local task management.

**Recommended default and causal basis.** Apply the skill fully within process-local Python and hand off explicitly at the first cross-process or framework question. The research brief defers web, data science, and deployment doctrine to companion skills, the guardrails pin tooling to the repo, and Async Mode covers tasks and cancellation, not distributed queues or cross-process coordination.

**Operating conditions and assumptions.** The task's concurrency stays within one interpreter's event loop or thread pool. This section states where this reference's guidance stops scaling, both as a document and in the systems it advises.

**Failure boundary and alternatives.** Stretching the skill past those seams produces confident guidance with no source, nothing in the bundle addresses multiprocessing, distributed locks, or service topology. Bounded alternatives and recoveries: vertical hardening within one process, better parsing, tighter types, managed resources, often removes the pressure that looked like a scale problem.

**Counterexample, gotchas, and operational comparison.** Asyncio fluency tempts extrapolation to distributed semantics, cancellation propagating through a TaskGroup says nothing about cancelling work on another machine. Good: hardening a worker's task lifecycle while routing its queue design elsewhere. Bad: deriving multiprocessing guidance from the asyncio sections. Borderline: subprocess orchestration, in scope for lifecycle and cleanup, out of scope for fleet coordination.

**Verification, evidence, and uncertainty.** Check every recommendation stays within process-local, single-repo evidence or carries an explicit handoff. The mode list, guardrails, and research-brief scope notes read across the bundle. The traffic or team size at which this repository would hit these seams is unknown here.

**Second-order consequence.** The skill scales by composition rather than extension, its research brief expects companion skills for each excluded domain, so the right response to a seam is a new skill, not a thicker entrypoint.

**Revision decision.** Add the code-scale clause, this reference covers single-process Python reliability within one repo's toolchain, cross-process, cross-service, and framework-level scale exceed its evidence.

**Retained seed evidence.** All four seed scale-boundary paragraphs remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Python Language Skill Entrypoint stops being sufficient when the task spans multiple independent systems, more than one ownership boundary, unbounded source discovery, or production traffic without an explicit SLO.
Under distributed execution, split work by theme file and preserve one verification owner per split; do not let parallel agents rewrite the same reference without a merge checkpoint.
Under long-running agent workflows, treat context drift as a reliability failure: checkpoint state, summarize open risks, and verify against the spec before continuing.
Under large-codebase scale, require dependency or source-graph narrowing before applying this reference; a source list without ranked canonical guidance is not enough.

## Future Refresh Search Queries

**Decision supported.** This section helps decide which searches will efficiently reveal that this reference has gone stale. The seed queries recycle the theme name verbatim, which retrieves directory listings rather than the stack developments that would age this reference, new CPython typing and asyncio features, packaging changes, and tool evolution across ruff, mypy, and pyright.

**Recommended default and causal basis.** Run the per-surface version probes each refresh cycle and update or caveat any claim whose pinned surface has moved. The bundle's claims are pinned to refreshable surfaces, a 2026-06-23 research date, TaskGroup availability by version, pyproject.toml conventions, and a specific formatter-linter-checker lineup.

**Operating conditions and assumptions.** Refresh time is bounded, probes are ordered by aging speed, tools first, stdlib features second, PEP-level conventions last. Queries here schedule staleness checks for this file's claims, they do not commission new pattern research.

**Failure boundary and alternatives.** A refresh driven by theme-name queries would confirm the reference exists without testing whether any pinned claim has been superseded. Bounded alternatives and recoveries: subscribing to CPython and tool release notes instead of query-based refresh, steadier but higher standing cost.

**Counterexample, gotchas, and operational comparison.** Newer language features do not automatically deprecate catalogued idioms, the probe question is superseded, not merely older. Good: a probe finding ruff absorbed a formerly-black-only behavior and updating the gate battery note. Bad: re-running the theme-name query and logging no change. Borderline: probing pyright versus mypy market share, interesting but not a claim this file makes.

**Verification, evidence, and uncertainty.** Record each probe, its date, and the claim it confirmed or invalidated in the refresh journal. The dated research brief and version-hedged claims observed across the bundle. Release cadences shift, the probe ordering by aging speed is an estimate.

**Second-order consequence.** The research brief is the refresh manifest in disguise, re-fetching its sixteen primary links and diffing against the bundle's claims is a complete, bounded staleness audit.

**Revision decision.** Replace the generic trio with versioned probes, current CPython typing and asyncio changes, current packaging guidance, current ruff-mypy-pyright feature status, and pytest release changes.

**Retained seed evidence.** The three seed query rows remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| search_query_label_name | search_query_text_value |
| --- | --- |
| `official_docs_query_phrase` | python language skill entrypoint official documentation best practices |
| `github_repository_query_phrase` | python language skill entrypoint GitHub repository examples |
| `release_notes_query_phrase` | python language skill entrypoint changelog release notes migration |

## Evidence Boundary Notes

**Decision supported.** This section helps decide which statements in this file may be reused, with what caveats, and which must stay quarantined. The seed notes define the three labels but not this evolution's actual boundary facts, one mapped file plus four sibling bundle files read in full, four external URLs left unretrieved, and all synthesis beyond the bundle marked as inference.

**Recommended default and causal basis.** Before reusing any claim from this file, check its label, local facts travel with their file and section, inferences travel with their reasoning, external candidates do not travel at all. Every evolved claim above traces to the full reads of SKILL.md and its references directory, while no external retrieval occurred, so the local and inference labels carry the entire file.

**Operating conditions and assumptions.** The archive keeps the bundle at its recorded path so local facts stay re-checkable. These notes bound what this document may assert, they are the last gate before any claim is reused elsewhere.

**Failure boundary and alternatives.** The subtlest leak here is bundle-internal, only SKILL.md is the mapped source, so sibling-file citations are local-corpus facts about the bundle, not about the seed's declared source row. Bounded alternatives and recoveries: tightening to per-claim footnotes if label-level discipline proves too coarse for future disputes.

**Counterexample, gotchas, and operational comparison.** The research brief's URL list looks like external evidence but is a local fact about what the skill's authors say they consulted, quoting it as verified external research would double-count. Good: reusing the cancellation rule with its PY1-07 citation. Bad: quoting the mypy row as evidence about current type-checker behavior. Borderline: reusing the explicitness thesis, sound inference but inference nonetheless.

**Verification, evidence, and uncertainty.** Sample ten claims from the evolved sections and confirm each carries the correct label class. The read ledger of this evolution, 95 plus 171 plus 66 plus 26 plus 34 lines read, zero external retrievals. Future readers cannot re-verify the reading effort itself, only the traceability it left behind.

**Second-order consequence.** Boundary notes make refresh cheap, because unretrieved candidates are already marked, a future cycle knows precisely which claims a retrieval pass could upgrade and which are settled local facts.

**Revision decision.** State the read ledger explicitly, five files and 392 lines with full-read status, the unretrieved status of all four URLs, and the rule that bundle citations name their file.

**Retained seed evidence.** The three labeled boundary definitions remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- `local_corpus_sourced_fact`: statements tied directly to the local source paths above.
- `external_research_sourced_fact`: statements tied to the public URLs above.
- `combined_evidence_inference_note`: synthesis that combines local and public evidence into agent guidance.
