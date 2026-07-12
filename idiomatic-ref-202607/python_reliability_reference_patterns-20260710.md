# Python Reliability Reference Patterns

**Decision supported.** This section helps decide which boundary, typing, data-model, error, resource, async, import, filesystem, logging, fixture, packaging, and tooling controls a Python change requires. The seed title does not define how to select and combine Python reliability controls for a script, package, service, CLI, or async worker with different failure and compatibility risks.

**Recommended default and causal basis.** Parse untrusted inputs before domain logic, contain `Any`, model stable values explicitly, depend on protocols, distinguish expected outcomes from exceptional failures, own cleanup, preserve cancellation, avoid import effects, and test failures through the repository's existing gates. Python's dynamic flexibility moves many defects to runtime; explicit boundaries and lifecycle tests localize uncertainty without pretending annotations validate data or that one tool guarantees reliability.

**Operating conditions and assumptions.** The repository's Python targets and toolchain are known, public contracts and runtime edges are identifiable, resource ownership is explicit, and fixtures can exercise success, error, timeout, cancellation, import, and packaging behavior. Use this reference for general Python reliability decisions and route framework, database, security, performance, or deployment specifics to dedicated evidence.

**Failure boundary and alternatives.** Annotations are treated as validation, broad handlers hide faults or cancellation, mutable defaults share state, blocking work stalls async execution, imports perform irreversible work, or a new quality stack ignores existing CI and compatibility. Bounded alternatives and recoveries: use a smaller control set for a disposable local script while retaining input and cleanup basics, preserve synchronous code when concurrency adds no value, use `unittest` instead of pytest where established, or isolate legacy dynamic code behind parsed adapters.

**Counterexample, gotchas, and operational comparison.** `Any` spreading inward, catching `Exception` and returning `None`, `assert` on external input, forgotten encodings, logs leaking secrets, monkeypatching production design, tests that miss cleanup, and adopting APIs unsupported by declared Python versions. Good: parse environment strings into a frozen value object, inject an HTTP protocol, and test malformed input plus cancellation cleanup. Bad: annotate a JSON dict, catch everything, and return `None`. Borderline: a short script can stay lightly typed only when its boundary, exit, files, and failures remain explicit.

**Verification, evidence, and uncertainty.** Inventory runtime inputs and effects, run malformed and missing cases, inspect type escapes, test mutable-default isolation, verify resource release on all exits, cancel async tasks, import modules in isolation, check paths and encodings, build the package, and run established lint, type, and test commands. The fully read local reference directly defines fifteen patterns spanning API design, parsing, exceptions, resources, asyncio, testing, packaging, and one unified tooling gate. The source is an archived checklist and the four external documentation sets were not refreshed, so current syntax, option, and version details require repository and installed-tool confirmation.

**Second-order consequence.** Reliability comes from converting dynamic uncertainty into explicit boundaries and owned lifecycles, not from maximizing annotations or tool count.

**Revision decision.** Add a risk classifier, causal control stack, lightweight alternatives, failure counterexamples, compatibility boundaries, operational examples, and a claim-linked verification packet.

**Retained seed evidence.** The exact title, one local source row, and four external source rows remain preserved as the frozen evidence base. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

## Source Evidence Mapping Table

**Decision supported.** This section helps decide which source can support a Python reliability claim and what corroboration is needed before changing code or tooling. The seed maps one integrated local reliability checklist and four tool documentation links, but it does not distinguish architecture guidance, language semantics, checker behavior, test framework behavior, lint configuration, or repository-local policy.

**Recommended default and causal basis.** Use the local checklist for cross-cutting design priorities, Python documentation for language and typing semantics, pytest for pytest behavior, mypy for checker behavior, Ruff for lint and format behavior, and repository configuration plus tests for local truth. Each source owns a different contract; checker documentation cannot validate runtime input, a test framework cannot define typing semantics, and generic guidance cannot override supported Python versions or CI commands.

**Operating conditions and assumptions.** The claim is classified, cited to the capable source, current repository files are inspected, external freshness is recorded, and inference is labeled separately. Apply the five frozen rows to their claim classes and treat project code, config, CI, and runtime results as additional direct evidence.

**Failure boundary and alternatives.** One local row becomes universal policy, tool docs define application behavior, archive commands are assumed installed, multiple links are counted as general corroboration, or a source title replaces reading its constraint. Bounded alternatives and recoveries: downgrade to a provisional recommendation, preserve existing tooling, create a small runtime fixture, inspect installed version help, or route framework-specific claims to primary docs.

**Counterexample, gotchas, and operational comparison.** Typing versions changing by Python target, pytest plugin behavior, mypy and runtime semantics diverging, Ruff rule-set drift, project wrappers altering command shape, and lock files constraining versions. Good: use the local pattern to contain `Any`, current typing docs for syntax, and repository mypy config plus tests for adoption. Bad: cite pytest docs to prove cancellation semantics. Borderline: recommend Ruff while labeling installation and rule choices repository-dependent.

**Verification, evidence, and uncertainty.** Build a claim ledger with source class, version or date, repository config, installed command, runtime fixture, contradiction, selected authority, and effect on guidance. The local source was fully read and directly integrates fifteen reliability concerns; the seed accurately identifies four relevant primary documentation families. No browsing occurred, so external pages and current tool options remain unverified.

**Second-order consequence.** Reliability evidence is layered: design guidance selects the question, tool documentation defines one mechanism, and repository execution decides whether it fits.

**Revision decision.** Add claim-specific authority, repository-truth precedence, version and freshness handling, counterexamples, conflict routing, and a verification ledger while preserving every row.

**Retained seed evidence.** The local reference path and four exact external URLs remain unchanged. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| source_location_path_key | source_category_artifact_type | source_authority_confidence_level | source_usage_synthesis_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202606/python-coder-01/references/python-reliability-reference.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt |
| https://docs.python.org/3/library/typing.html | external_research_source_material | external_research_sourced_fact | primary typing module documentation |
| https://docs.pytest.org/en/stable/ | external_research_source_material | external_research_sourced_fact | primary Python testing framework documentation |
| https://mypy.readthedocs.io/ | external_research_source_material | external_research_sourced_fact | static type checking documentation and constraints |
| https://docs.astral.sh/ruff/ | external_research_source_material | external_research_sourced_fact | linting and formatting tool documentation |

## Pattern Scoreboard Ranking Table

**Decision supported.** This section helps decide how to prioritize reliability controls without interpreting either score set as probability, severity, or measured defect reduction. The seed assigns 95, 91, and 88 to source mapping, evidence separation, and verification, while the local source separately scores fifteen patterns from 84 to 97 without defining empirical calibration.

**Recommended default and causal basis.** Treat boundary parsing and lifecycle safety as high-risk prerequisites, use the two scoreboards as editorial attention ordering, and select actual gates from the change's runtime inputs, effects, concurrency, packaging, and compatibility. Pattern importance is conditional: cancellation handling dominates an async worker, import safety dominates a library, and explicit encodings dominate file interchange regardless of small score differences.

**Operating conditions and assumptions.** The reviewer converts relevant rows into pass/fail checks, records why lower-scored controls still apply, and preserves all chosen safeguards through implementation. Retain all numbers as editorial metadata, not probabilities, service objectives, or cross-tool quality measures.

**Failure boundary and alternatives.** 97 becomes reliability percentage, an 84 pattern is skipped, scores resolve conflicting evidence, or an aggregate score hides an untested failure path. Bounded alternatives and recoveries: use a risk matrix by boundary and effect, classify hard prerequisites versus contextual controls, order gates by likely failure cost, or treat all applicable patterns as one completion set.

**Counterexample, gotchas, and operational comparison.** False precision, comparing scores across the seed and local table, optimizing annotations while missing cleanup, and treating editorial rank as a benchmark. Good: elevate cancellation and cleanup for an async job even though parsing has the highest local score. Bad: claim 95-percent safe typing. Borderline: use ranking to order review attention while requiring every applicable gate.

**Verification, evidence, and uncertainty.** Sample changes, record applicable patterns, ordering rationale, defects caught, skipped controls and boundaries, final gate outcomes, and whether score order would have changed the decision. Both score tables are frozen source facts, but neither source provides sample design or statistical validation. Relative value depends on application shape, Python target, dependencies, failure costs, and existing controls.

**Second-order consequence.** The scoreboards are most useful as omission prompts; low-ranked applicable controls can still be release blockers.

**Revision decision.** State calibration limits, connect rows to risk classes, add task-specific reordering, require all applicable controls, and prohibit achieved-rate claims.

**Retained seed evidence.** The seed's 95, 91, and 88 rows remain intact alongside the retained local scoreboard. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| pattern_identifier_stable_key | pattern_score_numeric_value | pattern_tier_adoption_level | pattern_failure_prevention_target |
| --- | ---: | --- | --- |
| `python_reliability_reference_patterns` | 95 | default_adoption_pattern_tier | Source Map First: Load local python reliability material before synthesizing reference patterns recommendations. |
| `python_reliability_reference_patterns` | 91 | default_adoption_pattern_tier | Evidence Boundary Split: Separate local facts, external facts, and inference before giving agent instructions. |
| `python_reliability_reference_patterns` | 88 | default_adoption_pattern_tier | Verification Gate Coupling: Attach each recommendation to at least one command, checklist, or review gate. |

## Idiomatic Thesis Synthesis Statement

**Decision supported.** This section helps decide what governing rule should connect Python's dynamic runtime, static analysis, resource ownership, concurrency, packaging, and repository tooling. The seed says to load sources and verify guidance but does not explain that reliable Python requires runtime parsing, contained dynamic escape hatches, explicit lifecycle ownership, and failure-path tests chosen by risk.

**Recommended default and causal basis.** Make uncertainty explicit at system boundaries, convert it into validated domain values, preserve typed contracts in the core, own every resource and task lifecycle, and verify observable failures with the repository's supported toolchain. Type hints improve reasoning but do not inspect runtime data, and happy-path tests cannot prove cleanup, cancellation, import safety, or package compatibility.

**Operating conditions and assumptions.** Inputs and outputs are identified, compatibility targets are known, side effects have owners, expected outcomes are modeled, exceptional failures remain diagnosable, and tests can force adverse paths. Apply the thesis to general Python code and route specialized persistence, web, distributed, security, and performance concerns to domain references.

**Failure boundary and alternatives.** Strictness becomes annotation volume, validation is scattered in domain logic, errors collapse to `None`, resources rely on garbage collection, or tooling migration precedes understanding existing CI. Bounded alternatives and recoveries: wrap legacy dynamic code with typed adapters, keep a synchronous design, use narrower runtime checks, preserve existing unittest or checker workflows, or stage strictness module by module.

**Counterexample, gotchas, and operational comparison.** `Any` crossing adapters, false confidence from a green type checker, exception translation losing cause, cancellation swallowed by broad handlers, import-time clients, mutable defaults, and tests that patch away real boundaries. Good: a CLI parses strings into domain values, uses a protocol-backed service, and tests invalid input plus file cleanup. Bad: annotated dictionaries and broad `except` blocks. Borderline: a small script can remain less formal only when effects and failures stay explicit.

**Verification, evidence, and uncertainty.** Map uncertainty boundaries, inspect core type escapes, exercise parser rejection, assert error context, test cleanup on success and failure, cancel async work, import without environment effects, run package entry points, and execute existing lint, type, build, and test gates. The local premise and fifteen patterns directly support the full boundary-to-tooling chain. Framework behavior, checker options, and Python-version APIs require current project evidence beyond this archived synthesis.

**Second-order consequence.** Reliability is an information-preservation discipline: parsed values, typed errors, exception context, cancellation, logs, and tests keep failure meaning intact across layers.

**Revision decision.** Replace generic synthesis with an uncertainty-to-contract model, lifecycle rules, staged alternatives, counterexamples, compatibility limits, and executable evidence.

**Retained seed evidence.** The local, external, and combined evidence statements remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`local_corpus_sourced_fact`: The local row for `python_reliability_reference_patterns` contains 1 source path(s), which should be treated as the first retrieval surface for this theme.
`external_research_sourced_fact`: The external source map provides public documentation, repository, or ecosystem analogues where available.
`combined_evidence_inference_note`: Reliable use of Python Reliability Reference Patterns comes from loading the local corpus first, checking public ecosystem guidance second, and converting both into verification-backed agent decisions.

## Local Corpus Source Map

**Decision supported.** This section helps decide which part of the single local source should guide the present Python change and where its authority ends. The seed maps one local reliability file as the first retrieval surface but does not route readers among its premise, fifteen-pattern scoreboard, API design, parsing, async, testing, packaging, and review questions.

**Recommended default and causal basis.** Use the premise for orientation, API and data headings for contracts, boundary and exception headings for runtime inputs, async and resources for lifecycle, testing for adverse cases, packaging for repository gates, and review questions for final audit. Heading-level retrieval avoids treating one compact checklist as exhaustive policy and helps the reviewer connect a concrete risk to the relevant causal control.

**Operating conditions and assumptions.** The change is classified, the exact pattern identifier and passage are read, repository context confirms applicability, and adjacent evidence is sought for framework or tool mechanics. Use the source as an integrated checklist and require project or primary evidence for mechanism-specific and time-sensitive claims.

**Failure boundary and alternatives.** The single source becomes universal canon, all fifteen patterns are copied without risk selection, scores replace reasoning, or a one-line rule overrides project compatibility. Bounded alternatives and recoveries: inspect repository code and CI first, consult current primary documentation for one mechanism, use language-specific framework guidance, or retain uncertainty when evidence is insufficient.

**Counterexample, gotchas, and operational comparison.** Pattern IDs confused with requirements, omitted `PY1-01` heading signal in seed map, brief examples mistaken for exhaustive recipes, and packaging commands imposed where the project uses wrappers. Good: route an async worker to cancellation, blocking, and cleanup passages plus local tests. Bad: use dataclass guidance to solve untrusted JSON validation. Borderline: apply protocol seams only when behavior substitution and test value justify them.

**Verification, evidence, and uncertainty.** Record risk class, pattern ID and passage, project files inspected, supported Python versions, local tool commands, conflicting conventions, current-doc need, resulting gate, and stop condition. The complete 171-line source was read and its sections are internally coherent across fifteen patterns. One local source offers no independent local corroboration and may omit frameworks, security, persistence, deployment, or newer language behavior.

**Second-order consequence.** A one-source map should optimize routing and expose gaps, not simulate consensus.

**Revision decision.** Turn the single row into a pattern-and-risk router, add stop conditions, gap warnings, repository handoff, misuse examples, and source-selection audit.

**Retained seed evidence.** The exact local path, title, heading signals, and skill-entrypoint role remain unchanged. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| local_source_filepath_value | local_source_title_text | local_source_heading_signals | local_source_usage_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202606/python-coder-01/references/python-reliability-reference.md | Python Reliability Reference | Python Reliability Reference; Premise; Pattern Scoreboard; 1. API, Typing, And Data Design; 'PY1-02' Keep 'Any' contained and justified; 'PY1-03' Use dataclasses for value data with explicit defaults | skill entrypoint or reusable agent prompt |

## External Research Source Map

**Decision supported.** This section helps decide when each external documentation family may support a reliability recommendation and what evidence is still needed locally. The seed lists Python typing, pytest, mypy, and Ruff documentation but does not define version scoping, repository fit, or the fact that these tools answer different semantic and operational questions.

**Recommended default and causal basis.** Use Python typing docs for language constructs, pytest docs only when pytest is the project stack, mypy docs for mypy configuration and checker semantics, and Ruff docs for selected lint or format behavior; confirm installed versions and CI. Tool documentation is authoritative for its own interface but cannot prove application runtime validation, repository adoption, or compatibility with other configured tools.

**Operating conditions and assumptions.** The exact mechanism and version are named, the repository already uses or deliberately adopts it, config and CI commands are inspected, and runtime behavior is tested where relevant. Use each external source only for its tool and keep application semantics and repository policy in local evidence.

**Failure boundary and alternatives.** Typing docs prove validation, pytest advice overrides unittest projects, mypy behavior is generalized to pyright, Ruff is added merely because it appears in the map, or unrefreshed pages support latest claims. Bounded alternatives and recoveries: preserve current project tools, use standard-library tests, inspect installed help and lock files, run a minimal checker fixture, or route framework-specific behavior to its primary docs.

**Counterexample, gotchas, and operational comparison.** Python-version-specific typing features, pytest plugin interactions, mypy mode differences, Ruff rule and formatter changes, duplicate formatter ownership, and CI wrappers. Good: use current mypy docs to explain one configured strictness option and prove it in CI. Bad: add pytest and Ruff to a stable unittest package by default. Borderline: propose a tool migration only with compatibility, overlap, rollout, and rollback evidence.

**Verification, evidence, and uncertainty.** Record URL, retrieval status, tool and Python versions, lock and config files, existing CI command, minimal fixture, runtime counterpart, conflicts, adoption decision, and migration path. The four URLs target relevant primary documentation families and their intended roles are accurately preserved by the seed. No browsing occurred, so page freshness and current option names are unverified.

**Second-order consequence.** External docs should narrow mechanism uncertainty, not manufacture a tooling standard where the repository has none.

**Revision decision.** Add tool-specific authority, version and adoption gates, runtime limits, migration alternatives, conflicts, and no-browse freshness labels.

**Retained seed evidence.** The four external URLs, names, usage roles, and evidence labels remain exactly preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| external_source_url_value | external_source_name_text | external_source_usage_role | evidence_boundary_label_value |
| --- | --- | --- | --- |
| https://docs.python.org/3/library/typing.html | Python typing docs | primary typing module documentation | external_research_sourced_fact |
| https://docs.pytest.org/en/stable/ | pytest documentation | primary Python testing framework documentation | external_research_sourced_fact |
| https://mypy.readthedocs.io/ | mypy documentation | static type checking documentation and constraints | external_research_sourced_fact |
| https://docs.astral.sh/ruff/ | Ruff documentation | linting and formatting tool documentation | external_research_sourced_fact |

## Anti Pattern Registry Table

**Decision supported.** This section helps decide which defect signature should block a Python change and what safer design or test should replace it. The seed lists generic source failures but omits Python-specific reliability defects including boundary data leakage, uncontained `Any`, mutable defaults, vague exception collapse, resource leaks, swallowed cancellation, blocking async work, import effects, and fixture contamination.

**Recommended default and causal basis.** Reject unparsed runtime data in the core, unjustified `Any`, shared mutable defaults, bare or meaning-erasing catches, unowned resources, cancellation suppression, event-loop blocking, operational imports, secret-bearing prints, and global-state test leakage. These defects erase type information, failure context, or lifecycle ownership and often pass happy-path tests until concurrency, malformed data, or repeated execution appears.

**Operating conditions and assumptions.** Each anti-pattern has a code signal, adverse scenario, consequence, replacement pattern, regression test, and compatibility boundary. Apply the registry to general Python code and use specialized references for framework, database, or security threat models.

**Failure boundary and alternatives.** Warnings stay stylistic, broader annotations replace validation, catches become wider to quiet tests, cleanup relies on interpreter exit, or new tools are added without behavior repair. Bounded alternatives and recoveries: parse into domain values, use `object` or protocols, factories, typed expected outcomes, contextual exceptions, context managers, synchronous execution, executor isolation, import-safe factories, structured logging, and isolated fixtures.

**Counterexample, gotchas, and operational comparison.** Dataclass fields with mutable instances, exception translation losing `__cause__`, cancellation class behavior by version, subprocess blocking, module-level clients, monkeypatch not restored, and filesystem tests using real home paths. Good: reject malformed JSON at an adapter and test the error plus cleanup. Bad: annotate `dict[str, Any]`, catch `Exception`, and return `None`. Borderline: an import cache is acceptable only when lazy, deterministic, resettable, thread-safe, and tested.

**Verification, evidence, and uncertainty.** Use malformed and missing inputs, repeated instances, fault injection, resource counters, cancellation and timeout fixtures, event-loop responsiveness, isolated imports, temp paths, secret-log scans, and test-order randomization where available. The local checklist directly names every major anti-pattern and corresponding safer control. Framework-specific exception and lifecycle semantics require additional project evidence.

**Second-order consequence.** Python reliability failures often propagate by erasing distinctions: unknown becomes `Any`, failure becomes `None`, cancellation becomes success, and shared state becomes hidden coupling.

**Revision decision.** Retain the three generic rows and add code-level signatures, causal consequences, adverse fixtures, safer patterns, compatibility notes, and recovery routes.

**Retained seed evidence.** Context-free output, unsourced claims, and unverified instruction remain preserved as umbrella failures. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| anti_pattern_failure_name | failure_cause_risk_reason | safer_default_replacement_pattern | detection_signal_review_method |
| --- | --- | --- | --- |
| context_free_summary_output | agent skips local corpus and produces generic advice | source_map_first_synthesis | verify every listed local path appears in the generated file |
| unsourced_recommendation_claims | guidance appears authoritative without source boundary | evidence_boundary_split_pattern | check for local, external, and inference labels |
| unverified_agent_instruction | recommendation cannot be checked by command or review gate | verification_gate_coupling | require concrete gate in generated reference |

## Verification Gate Command Set

**Decision supported.** This section helps decide which gates must pass for this evolved reference and for a concrete Python change at its actual risk level. The seed includes only a generated-reference verifier, while Python reliability requires repository discovery, runtime boundary tests, static analysis, lint and format checks, import and package tests, async failure fixtures, and cleanup evidence.

**Recommended default and causal basis.** Run the focused reference validator, inspect repository Python targets and existing commands, write behavior tests for affected boundaries and failures, then run the established formatter, linter, type checker, tests, build, and entry-point checks. Tool passes are complementary: type checking does not parse runtime data, lint does not prove cleanup, and unit success does not prove import, packaging, cancellation, or CLI behavior.

**Operating conditions and assumptions.** Each claim maps to one or more capable gates, commands come from project config or CI, adverse fixtures precede broad tooling, and failures identify behavior, type, style, package, or compatibility layers. Separate QA for this reference from project code gates and external service integration tests.

**Failure boundary and alternatives.** The archive command certifies code, mypy is treated as runtime validation, coverage replaces assertions, all tools are introduced at once, or a green unit suite ignores build and import behavior. Bounded alternatives and recoveries: use `unittest` where established, run a targeted module gate before the full suite, create minimal checker fixtures, stage strictness, preserve a supported older Python target, or withhold untested claims.

**Counterexample, gotchas, and operational comparison.** Wrong virtual environment, editable installs masking package omissions, test plugins changing behavior, cached type results, formatter overlap, platform filesystem differences, and cancellation tests that never reach the await point. Good: test malformed CLI input and cleanup, run existing mypy and Ruff commands, build a wheel, and invoke its entry point. Bad: run only `mypy .`. Borderline: a narrow script may skip package build when scope and remaining gates are explicit.

**Verification, evidence, and uncertainty.** Capture Python and tool versions, configs, exact commands, selected tests, adverse fixtures, exit codes, import isolation, resource and cancellation observations, build artifact, entry-point result, failures, and unresolved risk. The local source lists common gates and explicitly requires testing malformed input, cleanup, cancellation, import safety, entry points, and filesystem behavior. No target repository or tool installation is supplied, so project commands remain procedures rather than observed passes.

**Second-order consequence.** Verification should mirror uncertainty flow: parse boundaries first, preserve core contracts, then prove lifecycle and packaging around them.

**Revision decision.** Add repository-tool discovery, behavior-first adverse tests, static and runtime gate roles, packaging and import checks, compatibility capture, and the focused validator while retaining the seed command.

**Retained seed evidence.** The original final-stage reference-generation command remains preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`verification_gate_command_set`: Run the repository verifier after editing this file.

```bash
python3 agents-used-monthly-archive/idiomatic-references-202606/tools/verify_reference_generation.py --stage final
```

## Agent Usage Decision Guide

**Decision supported.** This section helps decide whether this reference applies and which smallest reliability control set should govern the Python task. The seed activates on theme mentions but does not classify change risk or choose among boundary parsing, typing, data design, exceptions, resources, asyncio, fixtures, packaging, and adjacent specialized guidance.

**Recommended default and causal basis.** Classify runtime inputs, public API, dynamic types, mutable state, expected and exceptional failures, resources, concurrency, import behavior, filesystem effects, package surface, and supported versions before selecting patterns. Risk classification prevents blanket strictness while ensuring that hidden runtime edges and lifecycle obligations are not omitted from seemingly small changes.

**Operating conditions and assumptions.** The task is general Python, repository conventions are inspectable, affected boundaries are known, and each chosen control can be verified. Activate for general Python reliability and route specialized dominant risks instead of stretching this reference.

**Failure boundary and alternatives.** The dominant concern is framework security, database transactions, distributed delivery, numerical correctness, deployment, or performance requiring domain evidence. Bounded alternatives and recoveries: route to web, persistence, security, async framework, packaging, CLI, testing, performance, or deployment references while retaining relevant general Python contracts.

**Counterexample, gotchas, and operational comparison.** Activating for any `.py` edit, applying service-level controls to disposable scripts, treating every function as a public API, adding async without need, and migrating tools before behavior. Good: a CSV importer selects parsing, typed values, explicit encoding, contextual errors, temp-path fixtures, and package gates. Bad: respond to a typo with full toolchain replacement. Borderline: a one-off script uses a reduced set but still owns files, exits, and malformed input.

**Verification, evidence, and uncertainty.** Record task type, risk inventory, selected pattern IDs, skipped controls with boundaries, repository commands, Python versions, adverse tests, adjacent routes, and stop condition. The fifteen local patterns and review questions provide a direct general-Python classifier. Application-specific risks and current tool capabilities may require controls absent from the one-source corpus.

**Second-order consequence.** Strictness should be asymmetric: invest most where untrusted data, irreversible effects, concurrency, and public contracts amplify defects.

**Revision decision.** Replace keyword routing with a risk inventory, pattern selector, reduced-script path, specialized exits, and auditable decision record.

**Retained seed evidence.** The local-first, explicit-gate, external-check, and evidence-label bullets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`agent_usage_decision_guide`: Use this reference when a task mentions this theme, one of the listed local source paths, or a nearby technology/workflow surface.

- Start with the local corpus source map.
- Prefer patterns with explicit verification gates.
- Treat external sources as freshness and ecosystem checks, not replacements for local repo conventions.
- Preserve the evidence boundary labels when reusing recommendations.

## User Journey Scenario

**Decision supported.** This section helps decide how a maintainer should assess, stage, verify, and communicate a Python reliability improvement from first risk inventory through package release. The seed names a Python maintainer needing typing, fixtures, packaging, and lint discipline but does not show a staged path from loose scripts to reliable boundaries without breaking behavior or compatibility.

**Recommended default and causal basis.** Capture current behavior and Python targets, identify runtime boundaries and effects, write adverse tests, introduce parsed values and owned lifecycles, tighten types behind those seams, run existing gates, build artifacts, and migrate incrementally. Behavior-first staging prevents tooling churn from hiding semantic regressions and gives each strictness increase a testable reason and rollback point.

**Operating conditions and assumptions.** The maintainer can run the current suite, inspect package metadata and CI, isolate one boundary, preserve public behavior, and release changes in reviewable steps. Use this scenario for incremental Python reliability work and route broad rewrites or domain migrations to dedicated plans.

**Failure boundary and alternatives.** There is no executable baseline, environment-dependent imports prevent testing, package ownership is unclear, or a big-bang checker and formatter migration overwhelms behavior changes. Bounded alternatives and recoveries: characterize with integration tests, add one boundary adapter, keep legacy core dynamic, introduce protocols before replacements, preserve synchronous flow, or defer package migration while fixing cleanup and errors.

**Counterexample, gotchas, and operational comparison.** Golden tests preserving bugs, editable installs masking metadata, strictness exclusions becoming permanent, fixture state leaking across stages, and supported Python versions changing accidentally. Good: a CSV script gains malformed-row tests, typed records, explicit encoding, contextual errors, temp fixtures, then package and type gates. Bad: enable strict checking globally and silence errors with `Any`. Borderline: leave one legacy adapter dynamic with explicit parsing, monitoring, and migration criteria.

**Verification, evidence, and uncertainty.** Record baseline commands and outputs, Python targets, risk inventory, characterization tests, changed boundary, type and validation delta, resource and cancellation cases, package artifact, compatibility results, rollback point, and remaining debt. The local checklist directly supports every stage from parsing through packaging and unified gates. Actual migration order depends on repository architecture, team ownership, and current tool configuration.

**Second-order consequence.** A successful migration shrinks the region where invalid states and unknown types can exist while preserving observable behavior.

**Revision decision.** Replace the generic role statement with a staged migration, causal checkpoints, alternatives, failure exits, evidence packet, and good, bad, and borderline outcomes.

**Retained seed evidence.** The maintainer role, scripts-or-services starting state, strictness decision, and opening trigger remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Role based opening scenario: The Python maintainer is starting from scripts or services that need typing, fixtures, packaging, and lint discipline and needs a reference that turns source evidence into an executable next step.
Primary user starting state: The user has a `python_reliability_reference_patterns` task, one or more local source paths, and uncertainty about which pattern should drive implementation.
Decision being made: choosing how strict to make typing, tests, validation, and dependency hygiene for the current risk level.
Reference opening trigger: Open this file when the task mentions python reliability reference patterns, any mapped local source path, or an adjacent workflow with the same failure mode.

## Decision Tradeoff Guide

**Decision supported.** This section helps decide which reliability control to adopt now, adapt to repository constraints, defer, or avoid for the current change. The seed bases adopt, adapt, and avoid on source agreement rather than tradeoffs among runtime validation, typing strictness, data models, protocol seams, error design, async, fixtures, packaging, and tool migration.

**Recommended default and causal basis.** Adopt controls that close active runtime and lifecycle risks, adapt strictness to supported versions and existing tooling, defer broad migrations behind stable seams, and avoid complexity whose verification cost exceeds the bounded need. Each control has benefit and cost: validation duplicates poorly when scattered, strict typing exposes debt, protocols add abstraction, async adds cancellation, and tool migrations create repository-wide churn.

**Operating conditions and assumptions.** The decision compares boundary exposure, failure cost, public API, concurrency, compatibility, team ownership, existing gates, migration size, and rollback. Decide per boundary and change, not by declaring an entire repository universally strict or loose.

**Failure boundary and alternatives.** Source agreement triggers wholesale adoption, adaptation means silencing errors, avoidance leaves no containment path, or cost is measured only in implementation time. Bounded alternatives and recoveries: runtime checks without checker migration, typed adapters around dynamic internals, dataclasses or TypedDict by data stability, concrete injection before protocols, synchronous execution, narrow fixtures, or staged CI warnings.

**Counterexample, gotchas, and operational comparison.** Using `Any` as migration escape, overmodeling transient data, protocol seams without consumers, converting expected outcomes into exceptions, and adding multiple overlapping formatters. Good: adopt boundary parsing and cleanup immediately, adapt type strictness module by module, avoid async for a sequential job. Bad: add every listed tool. Borderline: introduce a protocol only when testing or multiple implementations justify the seam.

**Verification, evidence, and uncertainty.** Write a tradeoff record with risk, chosen pattern IDs, expected benefit, complexity and compatibility cost, alternatives, skipped controls, failure consequence, tests, rollout, rollback, and revisit trigger. The local reference directly explains purpose and boundaries for all compared controls. The corpus does not quantify costs or benefits across project sizes and domains.

**Second-order consequence.** Controls should be sequenced by uncertainty reduction: parsing and lifecycle often make later typing and abstraction changes both smaller and more truthful.

**Revision decision.** Reframe the four seed options around risk reduction, migration cost, compatibility, staged alternatives, and reversible adoption.

**Retained seed evidence.** Adopt when, Adapt when, Avoid when, and Cost of being wrong remain exactly retained. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| decision_option_name | when_to_choose_condition | tradeoff_cost_description | verification_question_prompt |
| --- | --- | --- | --- |
| Adopt when | local corpus and external evidence agree on the python reliability reference patterns pattern | fastest path, but can copy stale local assumptions | Does the selected pattern appear in the canonical source and current external evidence? |
| Adapt when | local sources are strong but public ecosystem guidance has changed | preserves repo fit, but requires explicit inference notes | Did the reference label the local fact, external fact, and combined inference separately? |
| Avoid when | source evidence is thin, conflicting, or unrelated to the user journey | prevents false confidence, but may require deeper research | Is there a confidence warning or adjacent reference route? |
| Cost of being wrong | wrong python reliability reference patterns guidance can send an agent to the wrong files, tests, or abstraction | wasted implementation loop and weaker verification | Would a reviewer know what to undo and what to inspect next? |

## Local Corpus Hierarchy

**Decision supported.** This section helps decide which evidence should control when the archived checklist, project conventions, current language or tool documentation, and observed runtime behavior disagree. The seed marks one local source canonical and warns about thin coverage, but it does not explain how that checklist relates to repository behavior, Python language semantics, current tool docs, tests, and framework-specific evidence.

**Recommended default and causal basis.** Use the checklist for integrated risk framing, repository code and tests for existing behavior, package metadata and CI for supported policy, current primary docs for mechanism semantics, and reproducible fixtures for change claims. One concise reference can prioritize concerns but cannot override the application contract, installed versions, framework lifecycle, or direct failure observations.

**Operating conditions and assumptions.** The claim is classified, direct project evidence is preserved, conflicts are logged, current docs are versioned, and recommendations narrow when evidence remains thin. Preserve the checklist as canonical local synthesis while giving direct project and versioned mechanism evidence claim-specific precedence.

**Failure boundary and alternatives.** Canonical means universal policy, existing code is treated as correct solely because it exists, current docs override declared compatibility, or one test result becomes general guidance. Bounded alternatives and recoveries: retain both interpretations, build a minimal fixture, consult adjacent primary sources, stage the change, narrow scope, or decline a mechanism claim.

**Counterexample, gotchas, and operational comparison.** Tests encoding accidental behavior, CI wrappers, optional dependencies, type-checker-only modules, Python-version conditionals, and framework exception handling. Good: local guidance recommends TaskGroup, but package metadata supports an older Python, so preserve compatibility or stage the target change. Bad: archive score overrides runtime evidence. Borderline: current docs permit a feature but repository policy has not adopted it.

**Verification, evidence, and uncertainty.** Maintain a conflict ledger with claim, checklist passage, project files and tests, Python and tool versions, current source, fixture result, selected authority, migration effect, and uncertainty. The seed explicitly provides a single-source warning, and the local checklist clearly identifies itself as a reliability reference rather than a tutorial. Adjacent local sources have not been mapped, so framework and domain coverage remains incomplete.

**Second-order consequence.** Thin local evidence should increase the precision of claim boundaries, not the volume of generic corroboration.

**Revision decision.** Add claim-relative hierarchy, conflict ledger, project and fixture evidence, compatibility handling, thin-source limits, and adjacent discovery triggers.

**Retained seed evidence.** The confidence warning and sole canonical source row remain unchanged. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Classification vocabulary includes canonical, supporting, legacy, duplicate, and conflicting source roles.
Confidence warning: only one local corpus source is mapped, so this reference should invite adjacent-source discovery before becoming canonical policy.

| local_source_filepath_value | corpus_hierarchy_role | heading_signal_to_convert | reviewer_question_to_answer |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202606/python-coder-01/references/python-reliability-reference.md | canonical primary source | Python Reliability Reference; Premise; Pattern Scoreboard | What guidance, warning, or example should this source contribute to Python Reliability Reference Patterns? |

## Theme Specific Artifact

**Decision supported.** This section helps decide what artifact should govern adoption or refresh of a Python reliability recommendation in a real repository. The seed requests a reference freshness workflow with canonical policy and update checklist, but its three generic fields omit claim inventory, versions, repository fit, adverse fixtures, migration, rollback, and evidence reconciliation.

**Recommended default and causal basis.** Create a reliability adoption packet containing goal and risk, local pattern IDs, claim classes, Python and tool versions, repository config, current primary evidence, affected boundaries, behavior fixtures, compatibility matrix, rollout, rollback, and refresh trigger. Freshness matters only relative to a mechanism and project; a newer rule that breaks supported versions or weakens runtime tests is not a reliable update.

**Operating conditions and assumptions.** Every proposed control links to source evidence and a repository observation, adverse tests exist before migration, unsupported combinations are explicit, and rollback preserves behavior. Require the full packet for policy or tool changes and a lighter claim ledger for narrow code-level application.

**Failure boundary and alternatives.** The artifact is a link list, latest docs imply adoption, tool upgrades bundle behavior changes, no baseline exists, or freshness is declared without a reproduced difference. Bounded alternatives and recoveries: retain archived guidance with a warning, narrow adoption to one module, use runtime checks without tool migration, postpone incompatible features, or route a domain claim to specialized evidence.

**Counterexample, gotchas, and operational comparison.** Lock-file constraints, transitive pytest plugins, checker configuration inheritance, changed Ruff defaults, Python-version syntax, editable installs, and fixtures that only pass in developer environments. Good: refresh one mypy option, prove current config behavior, stage modules, and retain runtime validation. Bad: update all tools and call the reference current. Borderline: adopt a newer typing feature only after target-version and build matrices change deliberately.

**Verification, evidence, and uncertainty.** Replay the packet from a clean environment, resolve every cited version and config, run baseline and new adverse fixtures, compare type and lint diagnostics, build artifacts, test rollback, and review unresolved claims. The seed names a freshness artifact and the local checklist supplies stable risk categories and repository-gate requirements. External pages were not refreshed and no target repository was supplied, so this artifact is a procedure rather than an executed update.

**Second-order consequence.** Freshness is a controlled behavior diff, not a timestamp; unchanged reliable guidance may remain preferable to a newer incompatible mechanism.

**Revision decision.** Expand the three rows into claim and version inventory, project-fit evidence, adverse fixtures, compatibility, rollout, rollback, and refresh conditions.

**Retained seed evidence.** The user goal, decision boundary, and verification gate rows remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Theme specific artifact: reference freshness workflow with canonical source policy and update checklist.

| artifact_field_name | artifact_completion_rule | evidence_source_hint |
| --- | --- | --- |
| user_goal_statement | state the user's concrete goal before applying Python Reliability Reference Patterns | local corpus hierarchy plus critique findings |
| decision_boundary_rule | define the point where this reference should be used or avoided | decision tradeoff guide |
| verification_gate_rule | define the command, checklist, or review question that proves the artifact worked | verification gate command set |

## Worked Example Set

**Decision supported.** This section helps decide what concrete behavior distinguishes a reliable Python change, an attractive but unsafe shortcut, and a bounded migration compromise. The seed provides generic source-loading examples but no Python decisions about runtime parsing, `Any`, protocols, exceptions, cleanup, cancellation, fixtures, packaging, or tool migration.

**Recommended default and causal basis.** Judge examples by uncertainty containment, public contract clarity, lifecycle ownership, failure context, compatibility, adverse tests, and alignment with repository gates. Python code can look idiomatic and pass static checks while accepting malformed runtime data, leaking resources, or hiding cancellation and package defects.

**Operating conditions and assumptions.** The good case shows cause and verification, the bad case is plausible and consequential, and the borderline case names the containment and exit criteria that keep only a narrower claim valid. Use examples for general reliability reasoning, not copy-ready framework implementation.

**Failure boundary and alternatives.** Examples differ only in type-annotation density, the bad case is unrealistic, the good case assumes tools, or the compromise becomes permanent untracked debt. Bounded alternatives and recoveries: use boundary parsing, typed adapters, dataclasses, protocols, explicit outcomes, context managers, sync designs, isolated fixtures, or staged checker adoption as the teaching focus.

**Counterexample, gotchas, and operational comparison.** TypedDict used as runtime validation, protocols added without seams, cleanup mocked out, cancellation test not scheduling work, and tool migrations masking behavior changes. Good: parse a JSON payload into a frozen value, inject a protocol, and test malformed input plus client cleanup. Bad: pass `Any` inward and catch all failures as `None`. Borderline: keep one dynamic third-party adapter with explicit parsing, logging, tests, and removal criteria.

**Verification, evidence, and uncertainty.** For each case, identify input boundary, core type, expected and exceptional outcomes, resources, async control flow, imports, filesystem, fixtures, package targets, tool gates, compatibility, and reviewer verdict. All example dimensions are directly anchored in the fifteen local patterns. The examples are schematic and must be adapted to framework and repository semantics.

**Second-order consequence.** The strongest borderline case makes debt observable and one-directional: unknown data may enter an adapter but cannot escape into the core.

**Revision decision.** Replace generic contrasts with parsed-boundary, meaning-erasing, and contained-legacy cases that expose consequences, alternatives, verification, and migration exit.

**Retained seed evidence.** The original good, bad, and borderline evidence-boundary statements remain retained. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Good example: Use Python Reliability Reference Patterns after loading the canonical source, confirming the external evidence boundary, and writing a verification gate before implementation.
Bad example: Use Python Reliability Reference Patterns as a generic tutorial while ignoring the mapped local paths, source hierarchy, and cost of being wrong.
Borderline case: Use Python Reliability Reference Patterns only after adding a confidence warning when local evidence is thin or conflicts with current ecosystem guidance.

## Outcome Metrics and Feedback Loops

**Decision supported.** This section helps decide which signals show Python changes are becoming safer without encouraging annotation counts, coverage percentages, or tool adoption as ends. The seed wants later agents to preserve type, lint, and fixture coverage and flags missing migration guidance, but it does not define behavior-sensitive indicators or feedback actions.

**Recommended default and causal basis.** Track unparsed boundary escapes, unjustified `Any` crossings, adverse-input detection, error-context preservation, cleanup and cancellation failures, import-side effects, fixture leakage, supported-version regressions, package entry failures, and gate bypasses. These signals map to reliability mechanisms and failure outcomes, whereas raw type or test counts can grow while semantics weaken.

**Operating conditions and assumptions.** Each metric defines scope, denominator, baseline, Python and tool versions, expected behavior, adverse threshold, owner, and the code, test, or policy change triggered. Measure reliability of Python change workflows and separate service SLOs or security incidents into domain metrics.

**Failure boundary and alternatives.** `Any` count is gamed with casts, coverage replaces failure assertions, warnings are suppressed, flaky cancellation tests are excluded, or package failures are separated from code quality. Bounded alternatives and recoveries: use qualitative incident and review audits at low volume, sample boundary modules, track gate failures before rates, or maintain a debt ledger with expiry criteria.

**Counterexample, gotchas, and operational comparison.** Generated code, third-party stubs, intentionally dynamic adapters, expected cancellations, platform filesystem differences, and one defect producing multiple downstream signals. Good: track the proportion of external-input paths with parser rejection tests and every cancellation cleanup regression. Bad: advertise 100-percent type coverage. Borderline: report fewer `Any` uses only alongside boundary and behavior evidence.

**Verification, evidence, and uncertainty.** Publish definitions, scoped modules, raw counts, denominators, exclusions, versions, adverse fixtures, failures, uncertainty, owner, and feedback-to-change trace. The seed objective and local review questions directly support these behavior-sensitive indicators. No repository baseline or incident dataset is supplied, so thresholds and causal improvement remain local.

**Second-order consequence.** The most valuable metric is preserved failure meaning: malformed input, cancellation, and package errors should become easier to diagnose, not merely rarer in test output.

**Revision decision.** Operationalize boundary, lifecycle, compatibility, package, and gate signals with denominators, anti-gaming rules, owners, and migration feedback.

**Retained seed evidence.** The type-lint-fixture preservation indicator, migration-path failure signal, and refresh cadence remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Leading indicator: the next agent can modify the package without weakening type, lint, or fixture coverage.
Failure signal: the reference says quality matters but gives no migration path from loose scripts to strict package code.
Review cadence: Re-run the verifier after every generated-reference edit and refresh external sources when public APIs, docs, or tooling releases change.

## Completeness Checklist

**Decision supported.** This section helps decide what evidence must exist before a Python reliability recommendation or change is complete for its claimed risk scope. The seed checks role, decisions, hierarchy, artifact, examples, metrics, and routing but omits boundary inventory, type escapes, error semantics, lifecycle ownership, cancellation, import safety, filesystem behavior, adverse fixtures, compatibility, and package gates.

**Recommended default and causal basis.** Require the seven seed categories plus runtime-input parsing, core type containment, data defaults, behavior seams, expected and exceptional outcomes, resource ownership, async control flow, import safety, path and encoding, diagnosable logs, isolated fixtures, supported versions, and established gates. Omitting one relevant layer can leave a well-typed and well-linted change vulnerable to malformed data, leaked resources, hidden failures, or broken distribution.

**Operating conditions and assumptions.** Every item links to code, config, test, command output, or explicit nonapplicability, and higher-risk boundaries require adverse evidence. Apply full gates to reusable packages and services, documenting justified reductions for local scripts.

**Failure boundary and alternatives.** Checkmarks lack locations, type checker passes replace runtime tests, happy paths cover lifecycle, unsupported versions are implicit, or tool setup is considered implementation completion. Bounded alternatives and recoveries: use a reduced checklist for a disposable script, add cancellation and package cells only when applicable, stage strictness, or route specialized risk to a domain checklist.

**Counterexample, gotchas, and operational comparison.** Dynamic third-party adapters, generated code, optional dependencies, import modes, editable installs, platform paths, and test fixtures that hide real resource ownership. Good: an importer links each boundary and cleanup item to a test and package gate. Bad: complete because Ruff and mypy pass. Borderline: a local script may omit build checks while explicitly limiting distribution.

**Verification, evidence, and uncertainty.** Audit items against boundary map, type diagnostics, adverse fixtures, resource and cancellation observations, isolated import, temp filesystem, log scan, package metadata, Python matrix, build, entry point, and full project gates. The fifteen local patterns and seven review questions directly support the added completion dimensions. Domain and framework checks remain outside the one-source general reference.

**Second-order consequence.** Completeness is the closure of every relevant uncertainty boundary and lifecycle, not the presence of every possible Python tool.

**Revision decision.** Extend seed categories with evidence pointers, risk-based applicability, runtime and lifecycle gates, compatibility, package verification, and reviewer replay.

**Retained seed evidence.** All seven original checklist bullets remain unchanged. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- The role scenario names the user, starting state, decision, and trigger for Python Reliability Reference Patterns.
- The decision guide includes Adopt when, Adapt when, Avoid when, and Cost of being wrong.
- The local corpus hierarchy identifies canonical and supporting sources or gives a confidence warning.
- The theme specific artifact is concrete enough to review without reading every mapped source.
- The examples cover good, bad, and borderline usage.
- The metrics section names one leading indicator and one failure signal.
- The adjacent routing section points to a better reference when this one is not the right fit.

## Adjacent Reference Routing

**Decision supported.** This section helps decide where to route when general Python controls are insufficient for framework, persistence, security, distributed, packaging, CLI, testing, observability, performance, or deployment concerns. The seed points vaguely to Python, reliability, routing, quality, and reference guidance without naming the dominant risk or evidence expected from a handoff.

**Recommended default and causal basis.** Retain general boundary and lifecycle contracts here, then route the dominant mechanism to its primary framework or domain reference with a minimal risk and evidence packet. Specialized systems define transactions, request lifecycles, threat models, delivery semantics, and operational constraints that a general checklist cannot safely infer.

**Operating conditions and assumptions.** The unresolved question is explicit, the destination owns it, Python targets and existing controls travel with the task, and returned guidance is reconciled with general contracts. Route at domain boundaries and keep general Python contract ownership visible.

**Failure boundary and alternatives.** Routing follows keywords, several references load indiscriminately, specialized guidance weakens parsing or cleanup silently, or ownership of verification becomes unclear. Bounded alternatives and recoveries: use repository-local framework docs, current primary documentation, minimal integration fixtures, or narrow the claim when no capable reference exists.

**Counterexample, gotchas, and operational comparison.** Web validation duplicated across layers, database retries outside transactions, async framework cancellation semantics, packaging tools changing import behavior, and performance optimization bypassing diagnostics. Good: route a FastAPI request lifecycle to framework guidance while retaining parsed domain values and cancellation tests. Bad: use general typing rules to design transaction retries. Borderline: packaging guidance may own build mechanics while this reference owns import safety.

**Verification, evidence, and uncertainty.** Record route trigger, destination capability, Python and dependency versions, handoff boundaries, retained controls, returned evidence, conflicts, integration tests, ownership, and return or stop decision. The local source explicitly bounds itself as a checklist and identifies several seams requiring repository or ecosystem context. The available adjacent reference inventory and current frameworks can change.

**Second-order consequence.** A useful route adds a missing operational model while preserving the information and lifecycle guarantees already established.

**Revision decision.** Replace vague pointers with risk triggers, minimal handoff fields, retained invariants, return criteria, and cross-domain examples.

**Retained seed evidence.** The original python, reliability, reference, routing, and quality labels remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Adjacent reference guidance: Use reliability, routing, or quality references when the problem is governance rather than syntax.
Adjacent reference 1: consider the python adjacent reference when the current task pivots away from python reliability reference patterns.
Adjacent reference 2: consider the reliability adjacent reference when the current task pivots away from python reliability reference patterns.
Adjacent reference 3: consider the reference adjacent reference when the current task pivots away from python reliability reference patterns.

## Workload Model

**Decision supported.** This section helps decide how much reliability change one packet and owner should handle before the work must split into staged boundaries or domain-specific efforts. The seed bounds one audience, one decision, twelve sources, and one checklist, but Python reliability workload is driven by independent runtime boundaries, effect lifecycles, concurrency models, compatibility targets, packages, and ownership.

**Recommended default and causal basis.** Scope one packet to one coherent behavior change and compatibility matrix, split independent input adapters, resource owners, async task trees, packages, or domain migrations, and keep one verification owner per split. Combining unrelated strictness, tool, packaging, and behavior changes obscures causality and makes rollback and failure diagnosis unreliable.

**Operating conditions and assumptions.** The packet inventories modules, public contracts, runtime inputs, effects, resources, tasks, dependencies, Python versions, tools, owners, and adverse fixtures. Use this model for reliability-change coherence and assess runtime capacity separately.

**Failure boundary and alternatives.** A repository-wide cleanup bundles checker migration with behavior changes, several agents edit shared configs, one checklist covers independent services, or source count is treated as capacity. Bounded alternatives and recoveries: stage by boundary, package, compatibility target, or tool; add adapters; freeze tool migration; delegate independent modules; or create a narrower domain reference.

**Counterexample, gotchas, and operational comparison.** Shared pyproject configuration, namespace packages, cross-module `Any`, fixture scopes, event-loop ownership, generated code, and one package artifact spanning multiple owners. Good: one phase hardens an HTTP adapter and its tests, then a later phase tightens core types. Bad: migrate formatter, checker, async design, and packaging together. Borderline: repository-wide lint changes require mechanical isolation and behavior gates.

**Verification, evidence, and uncertainty.** Measure affected boundaries, modules, contracts, effects, tasks, Python matrix, config files, owners, test cases, migration steps, rollback points, and split decisions. The local patterns span separable reliability layers, and the seed already emphasizes one decision and bounded review. No universal module, source, or fixture limit is supported.

**Second-order consequence.** The binding workload is the number of causal changes a reviewer can attribute, not lines of Python or source documents.

**Revision decision.** Retain seed capacity metadata but add boundary, lifecycle, concurrency, compatibility, ownership, staging, and rollback dimensions.

**Retained seed evidence.** The four workload rows and one-audience, one-decision, twelve-source boundary remain preserved as provisional metadata. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`combined_evidence_inference_note`: Treat Python Reliability Reference Patterns as a documentation reference operating reference, not as a prose summary.

| workload_dimension_name | workload_boundary_value | verification_pressure_point |
| --- | --- | --- |
| primary_usage_surface | reference selection, writing, roadmap, or explanation work where the output should improve the next human or agent decision | verify that the reference changes the next implementation or review action |
| bounded_capacity_model | one audience, one decision, up to 12 source documents, and one verification checklist per reference use | split the task or create a narrower reference when this boundary is exceeded |
| source_pressure_model | local heading signals include Python Reliability Reference; Premise; Pattern Scoreboard; 1. API, Typing, And Data Design; 'PY1-02' Keep 'Any' contained and justified; 'PY1-03' Use  | compare guidance against canonical local sources before following external examples |
| artifact_pressure_model | required artifact is reference freshness workflow with canonical source policy and update checklist | require the artifact before claiming the reference is operationally usable |

## Reliability Target

**Decision supported.** This section helps decide which Python reliability properties are hard change gates and which adoption outcomes require sampled evidence. The seed proposes full evidence labels, 18-of-20 routing, zero unsupported claims, and universal recovery paths but does not classify them or cover parsed boundaries, contained dynamics, cleanup, cancellation, import safety, and compatibility.

**Recommended default and causal basis.** Enforce hard gates for affected boundary parsing, justified dynamic escapes, deterministic defaults, meaningful errors, owned cleanup, preserved cancellation, import safety, supported targets, and unsupported-claim rejection; sample routing and migration outcomes separately. One code change can deterministically satisfy its contracts, while repository-wide adoption and human decisions need cohorts and cannot be inferred from a checklist.

**Operating conditions and assumptions.** Each target names scope, Python and tool versions, hard-or-sampled class, denominator, fixture, failure consequence, owner, and retest. Treat seed numbers as proposed review or sampling contracts, never achieved language, tool, or agent reliability.

**Failure boundary and alternatives.** 18 of 20 becomes achieved accuracy, complete labels imply runtime safety, zero `Any` becomes a proxy for reliability, or documented cleanup replaces fault and cancellation tests. Bounded alternatives and recoveries: keep strict per-boundary gates, bootstrap migration baselines qualitatively, narrow module scope, sample high-risk paths, or withhold repository-wide policy claims.

**Counterexample, gotchas, and operational comparison.** Generated code, dynamic adapters, framework-owned cancellation, optional dependencies, supported-version exclusions, and a single defect counted through multiple diagnostics. Good: block a swallowed cancellation as a hard gate and separately sample whether agents select async controls correctly. Bad: claim 90-percent Python reliability. Borderline: release one module with all local gates while broader migration outcomes remain unclaimed.

**Verification, evidence, and uncertainty.** Record target definition, code scope, versions, class, denominator, raw results, adverse fixtures, exclusions, failures, uncertainty, remediation, and measurement window. The seed supplies four target categories and the local checklist directly supports hard contract gates. No downstream task sample or repository metrics accompany the source.

**Second-order consequence.** Hard gates protect information and lifecycle integrity per change; sampled outcomes reveal whether the organization applies them effectively.

**Revision decision.** Classify targets, add boundary and lifecycle invariants, define migration cohorts, require denominators, and prohibit unsupported achieved rates.

**Retained seed evidence.** All four original reliability rows and thresholds remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| reliability_target_name | measurable_threshold_value | evidence_collection_method |
| --- | --- | --- |
| source_boundary_preservation | 100 percent of recommendations keep local, external, and inference boundaries visible | review generated text for the three evidence labels before reuse |
| decision_accuracy_sample | at least 18 of 20 sampled uses route to the correct adopt, adapt, avoid, or adjacent-reference decision | sample downstream tasks and record reviewer verdicts |
| unsupported_claim_rate | zero unsupported production, security, latency, or reliability claims in final guidance | reject claims without source row, explicit inference note, or verification method |
| recovery_path_clarity | every avoid or failure case names the rollback, escalation, or next-reference route | inspect failure-mode and adjacent-routing sections together |

## Failure Mode Table

**Decision supported.** This section helps decide which reliability layer failed, what information or effects were lost, and which dependent claims must be withdrawn or repaired. The seed covers source drift, generic advice, implicit decisions, and source lists but omits boundary parsing, type escape, data default, error translation, resource, cancellation, blocking, import, filesystem, logging, fixture, packaging, and tool failures.

**Recommended default and causal basis.** Classify failures by runtime boundary, core contract, state model, expected outcome, exceptional path, resource lifecycle, async control flow, import, filesystem, diagnostics, test isolation, package, or tooling. Layer localization guides recovery: malformed-input acceptance differs from leaked resources, swallowed cancellation, or a wheel missing an entry point.

**Operating conditions and assumptions.** The first signal is reproducible, affected behavior is named, side effects and state are inspected, repair changes evidence, and regression fixtures cover the original path. Use this taxonomy for general Python reliability and route domain effects to specialized incident models.

**Failure boundary and alternatives.** All defects become typing issues, broad catches are added, tests patch away ownership, package failures are blamed on CI, or static diagnostics are suppressed without runtime evidence. Bounded alternatives and recoveries: add boundary adapters, narrow types, use factories, preserve causes, introduce context managers, re-raise cancellation, isolate blocking work, defer imports, use temp paths, restore fixture state, or repair metadata.

**Counterexample, gotchas, and operational comparison.** Secondary exceptions during cleanup, cancellation arriving between state changes, partial files, logging failures, import caches, test order, editable installs, and checker configuration masking modules. Good: classify a timeout cleanup leak as resource plus async lifecycle and add cancellation fixture. Bad: silence mypy after malformed input causes a crash. Borderline: retain a dynamic adapter while withdrawing core type guarantees beyond it.

**Verification, evidence, and uncertainty.** Capture layer, input and state, Python version, stack and cause, resources and tasks, filesystem effects, logs, fixture isolation, package artifact, tool diagnostics, mitigation, replay, and prevention owner. The local source explicitly enumerates all failure layers and review questions. Framework and infrastructure failures may need additional classes.

**Second-order consequence.** Failure analysis should identify which distinction disappeared: valid versus invalid data, expected versus exceptional outcome, running versus cancelled task, or owned versus leaked resource.

**Revision decision.** Retain the four generic rows and add Python-layer taxonomy, information-loss analysis, effect inspection, regression replay, and recurrence feedback.

**Retained seed evidence.** Source drift, generic advice, implicit decision, and corpus-list failures remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| failure_mode_name | likely_trigger_condition | required_mitigation_action |
| --- | --- | --- |
| source drift hides truth | external or local guidance changes after the reference was written | refresh public evidence, rerun local corpus gate, and mark stale claims before reuse |
| generic advice escapes review | agent copies plausible best practices without theme-specific verification | block completion until the verification gate names concrete command, reviewer question, or metric |
| decision path remains implicit | reader cannot tell when to adopt, adapt, or avoid the pattern | add decision table, cost of being wrong, and adjacent-reference route |
| large corpus becomes list | many sources are indexed but not synthesized into ranked guidance | classify canonical, supporting, legacy, duplicate, and conflicting sources |

## Retry Backpressure Guidance

**Decision supported.** This section helps decide when a failed Python operation or verification step may be retried and when work must stop for state inspection, cleanup, rollback, or domain-specific recovery. The seed limits stale-evidence retries and pauses on red gates but does not define safe replay of Python functions, subprocesses, file writes, async tasks, fixtures, package builds, or tool migrations.

**Recommended default and causal basis.** Retry only after classifying the failure, inspecting partial effects and owned resources, preserving cancellation, changing a relevant prerequisite, and proving replay is idempotent or explicitly compensated. Blind retry can duplicate external actions, overwrite partial files, rerun subprocesses, leak clients, revive cancelled workflows, or make flaky tests appear healthy.

**Operating conditions and assumptions.** Operation identity, input, state snapshot, effect ledger, attempt budget, changed prerequisite, cleanup, owner, and semantic success condition are explicit. Apply general replay controls and delegate network, database, queue, or distributed retries to domain-specific policies.

**Failure boundary and alternatives.** Broad retry catches programmer errors, cancellation triggers retry, package tests rerun until green, tool failures are bypassed, or file and database effects are assumed atomic. Bounded alternatives and recoveries: resume from a validated checkpoint, roll back a temp-file or transaction pattern, recreate an isolated fixture, repair environment or dependency state, switch to synchronous or manual recovery, or escalate to domain guidance.

**Counterexample, gotchas, and operational comparison.** At-least-once APIs, subprocess ambiguity, partial rename semantics, async task siblings, random seeds, test-order dependence, stale virtual environments, and caches across checker runs. Good: retry a read-only HTTP fetch once after a classified transient error with client cleanup. Bad: retry `CancelledError` or a partially applied mutation. Borderline: rebuild a wheel after cleaning the environment and changing a verified dependency prerequisite.

**Verification, evidence, and uncertainty.** Record failure fingerprint, attempt, inputs, Python and dependency versions, state and effects before and after, cancellation status, changed prerequisite, exact command, semantic result, cleanup, and stop reason. The source directly emphasizes explicit errors, deterministic cleanup, cancellation, fixture isolation, and package gates that constrain safe replay. Domain operations define idempotency and compensation, so universal retry counts are unsupported.

**Second-order consequence.** Backpressure prevents uncertainty from becoming repeated side effects; a clean failure is often safer than an unclassified apparent recovery.

**Revision decision.** Add operation identity, effect and task inspection, idempotency and compensation gates, cancellation rules, isolated reruns, semantic success, and escalation.

**Retained seed evidence.** The original classification, bounded refresh, red-gate stop, checkpoint, and one-owner bullets remain retained. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- Retry only after the failed verification signal is classified as transient, stale evidence, missing context, or true contradiction.
- Use one bounded retry for stale external evidence refresh, then escalate to a human or a narrower source-specific reference.
- Apply backpressure by stopping new generation or implementation work when source coverage, critique coverage, or verification gates are red.
- For long-running agent workflows, checkpoint after each batch and re-read the current spec before any broad rewrite, commit, push, or destructive operation.
- For distributed execution, assign one owner per generated file or theme batch and require merge-time verification of exact path, heading, and evidence-boundary invariants.

## Observability Checklist

**Decision supported.** This section helps decide which minimal observations let maintainers diagnose a Python reliability failure without leaking secrets, payloads, or raw transcripts. The seed records sources, verification, timing, reviewer decisions, uncertainty, signals, and concise audits but omits Python boundary, exception, resource, task, import, package, and tool-version context.

**Recommended default and causal basis.** Record code and package revision, Python and dependency versions, boundary and operation identifiers, validated shape rather than raw sensitive data, exception type and cause, resource and task lifecycle, cancellation, effect summary, gate results, and unresolved risk. Failure meaning depends on where invalid data entered, which operation owned effects, and whether cleanup or cancellation completed; generic logs cannot distinguish those paths.

**Operating conditions and assumptions.** Records use correlation identifiers, redact values at collection, preserve exception chains, expose task and resource state, link to fixture and package artifacts, and include failures and cancellations. Capture general Python lifecycle context and route service-specific telemetry to operational guidance.

**Failure boundary and alternatives.** Raw payloads or environment values are logged, `print` is the only diagnostic, exception messages lose type and cause, success-only events hide leaks, or tool versions are absent. Bounded alternatives and recoveries: use structured local fixture logs, minimal library logging at adapter boundaries, test-captured events, package build records, or domain telemetry for services.

**Counterexample, gotchas, and operational comparison.** Secrets in repr output, dataclass fields logged wholesale, duplicate handlers at import, async task names absent, cancellation recorded as error, and logs changing test timing. Good: a redacted import record shows parser rejection, correlation ID, exception cause, no file write, and closed client. Bad: log the full JSON and token. Borderline: library code emits structured debug context only through caller-configured logging.

**Verification, evidence, and uncertainty.** Sample records, reconstruct boundary, parsed outcome, exception chain, resources, tasks, effects, package and tool versions, gate result, and recovery; adversarially test redaction. The local source directly requires diagnosable logging without secrets and explicit boundary, error, resource, async, import, and package behavior. Production telemetry architecture, retention, and privacy policies are domain-specific.

**Second-order consequence.** Observability should preserve the distinctions reliability controls create, especially invalid versus valid input and failed versus cancelled work.

**Revision decision.** Add correlation, version identity, validated-shape logging, exception chains, resource and task events, package gates, redaction, and reconstruction tests.

**Retained seed evidence.** All six original observability bullets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- Record which local sources were loaded and which were intentionally skipped.
- Record the exact verification command, reviewer question, or rendered artifact used as proof.
- Record p50/p95/p99 latency or reviewer-time measurements when the reference affects runtime or workflow speed.
- Capture reviewer decision, unresolved uncertainty, and next refresh trigger.
- Record leading indicator and failure signal from this file in the coverage manifest or journal when the reference drives real work.
- Keep audit evidence small enough to review: command output summary, changed-file list, and unresolved-risk notes are preferred over raw transcript dumps.

## Performance Verification Method

**Decision supported.** This section helps decide how to test whether the reference speeds reliable review and migration decisions without rewarding shallow tool selection or weakening behavior gates. The seed requires readers to find a correct next action within ten minutes but provides no task cohort, reviewer definition, correctness rubric, sample size, baseline, or separation from runtime performance.

**Recommended default and causal basis.** Treat ten minutes as a candidate acceptance hypothesis, compare matched Python tasks, measure orientation, risk classification, source routing, test selection, and verified next-action time, and score correctness plus evidence completeness. A fast recommendation to add mypy or pytest is not useful if it misses runtime parsing, cleanup, cancellation, compatibility, or existing repository conventions.

**Operating conditions and assumptions.** The protocol fixes task, code snapshot, Python targets, reviewer experience, available sources, start and stop events, expected decision, rubric, failures, and baseline. Measure reference-review efficiency separately from Python runtime or tool execution performance.

**Failure boundary and alternatives.** One run is reported as p95, easy tasks dominate, reading ends before repository commands are found, wrong actions count as fast, or runtime latency is mixed with reviewer time. Bounded alternatives and recoveries: measure time to first relevant pattern, time to adverse fixture, reviewer effort, source count avoided, or qualitative action clarity until samples support percentiles.

**Counterexample, gotchas, and operational comparison.** Learning between repeated tasks, tool familiarity, codebase size, hidden setup, cached context, parallel review, and excluding uncertain outcomes. Good: compare matched boundary-parsing reviews and require a correct test plan. Bad: report ten-minute compliance from the seed sentence. Borderline: publish median decision time with full raw samples and no tail claim.

**Verification, evidence, and uncertainty.** Publish protocol, cohort, snapshot, reviewer role, raw durations, decisions, correctness rubric, evidence score, failures, exclusions, percentile calculation, baseline, and uncertainty. The seed states the candidate target and next-action goal; the local source supplies a concrete review-question rubric. No observed reviewer sample accompanies the source, so achieved performance cannot be claimed.

**Second-order consequence.** The unit of performance is a verified reduction in decision uncertainty, not document skimming speed.

**Revision decision.** Mark the target unproven, define matched tasks and stages, require correctness and evidence, expose sample rules, and add low-sample alternatives.

**Retained seed evidence.** The ten-minute method, leading indicator, failure signal, measurement packet, and pass-fail criteria remain retained. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Performance method: require the reader to find the correct next action in 10 minutes or less during review sampling.
Leading indicator to measure: the next agent can modify the package without weakening type, lint, or fixture coverage.
Failure signal to watch: the reference says quality matters but gives no migration path from loose scripts to strict package code.
Required measurement packet: capture input size, source count, tool-call count, wall-clock time, p50/p95/p99 latency where runtime applies, and reviewer decision time where documentation applies.
Pass condition: the reference must let a reviewer identify the correct next action, verification gate, and stop condition without reading unrelated files.
Fail condition: the reference encourages implementation before the workload, reliability target, and failure-mode table are explicit.

## Scale Boundary Statement

**Decision supported.** This section helps decide when one general Python reliability reference and one migration packet no longer provide sufficient evidence or ownership. The seed stops at multiple systems, ownership, unbounded discovery, production traffic, context drift, and large codebases but does not define package, service, concurrency, compatibility, or shared-tooling boundaries.

**Recommended default and causal basis.** Split by package, service, runtime boundary, concurrency domain, or owner; preserve typed contracts at interfaces; coordinate shared configuration explicitly; and add domain SLO, security, persistence, and deployment evidence. General patterns remain useful, but cross-system failures involve transactions, messages, deployments, retries, and operational states absent from a local code checklist.

**Operating conditions and assumptions.** Each split has a behavior boundary, owner, Python and dependency matrix, package artifact, test suite, effect model, and integration contract. Use this statement to exit general guidance, not to assert production readiness.

**Failure boundary and alternatives.** One checklist certifies multiple services, shared pyproject changes have no coordinator, async and sync lifecycles mix implicitly, parallel agents rewrite common fixtures, or production reliability is inferred from unit gates. Bounded alternatives and recoveries: create package-specific plans, domain references, contract tests, service catalogs, dependency maps, staged configuration changes, or narrower migration corridors.

**Counterexample, gotchas, and operational comparison.** Namespace packages, shared virtual environments, monorepo config inheritance, cross-service schemas, queue semantics, optional extras, version skew, and generated clients. Good: harden each service adapter separately and test the API contract between them. Bad: call a monorepo reliable after one mypy run. Borderline: a shared type policy needs coordinated package matrices and staged enforcement.

**Verification, evidence, and uncertainty.** Inventory packages, services, owners, public boundaries, data contracts, task trees, effects, Python and dependency versions, shared configs, integration tests, operational evidence, release order, and rollback. The seed already recognizes system and ownership limits, and the local source explicitly scopes itself to a general checklist. The corpus provides no production-scale benchmark or domain SLO model.

**Second-order consequence.** Scale failure begins when one change's type and lifecycle evidence cannot identify the system state it governs.

**Revision decision.** Add package, service, concurrency, compatibility, shared-config, integration, operational, release, and rollback boundaries.

**Retained seed evidence.** The original multiple-system, ownership, distributed execution, context drift, and graph-narrowing limits remain retained. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Python Reliability Reference Patterns stops being sufficient when the task spans multiple independent systems, more than one ownership boundary, unbounded source discovery, or production traffic without an explicit SLO.
Under distributed execution, split work by theme file and preserve one verification owner per split; do not let parallel agents rewrite the same reference without a merge checkpoint.
Under long-running agent workflows, treat context drift as a reliability failure: checkpoint state, summarize open risks, and verify against the spec before continuing.
Under large-codebase scale, require dependency or source-graph narrowing before applying this reference; a source list without ranked canonical guidance is not enough.

## Future Refresh Search Queries

**Decision supported.** This section helps decide when and how maintainers should refresh Python reliability guidance without turning newer documentation into automatic repository policy. The seed provides generic official-docs, GitHub-example, and release-note queries without a Python or tool version, disputed pattern, drift trigger, source ranking, or repository reproduction.

**Recommended default and causal basis.** Search after a documented language, checker, test, lint, packaging, or compatibility drift signal; include the exact mechanism and versions; prefer primary versioned sources; archive evidence; reproduce it in repository or minimal fixtures; and record migration impact. Search finds candidates, while supported Python targets, installed tools, project configuration, and behavior tests decide whether a new mechanism is reliable locally.

**Operating conditions and assumptions.** The trigger names a claim, query is narrow, source ownership and date are recorded, archive and current versions stay separate, and accepted changes update fixtures, config, and rollback guidance. Search mechanism-specific primary material and keep project adoption a separate decision.

**Failure boundary and alternatives.** Snippets become semantics, latest docs override supported versions, a popular repository defines best practice, absent results prove deprecation, or routine browsing is called validation. Bounded alternatives and recoveries: inspect installed help, package metadata, lock files, release artifacts, or a minimal language and tool fixture; retain uncertainty or preserve existing behavior.

**Counterexample, gotchas, and operational comparison.** Python-version branches, typing backports, pytest plugins, mypy daemon caches, Ruff preview rules, renamed options, and tool wrappers in CI. Good: after a checker diagnostic changes, search the exact option and version, reproduce it, then stage config migration. Bad: adopt a latest strict template. Borderline: keep a community workaround provisional until primary evidence and fixture agreement.

**Verification, evidence, and uncertainty.** Record trigger, query, date, source owner, Python and tool versions, archived hash, claim summary, project config, fixture result, conflict, accepted change, migration, reviewer, and next trigger. The seed supplies three search categories and the local checklist identifies concrete language and tooling surfaces that may drift. No browsing occurred, so all query rows remain unexecuted and prove no freshness.

**Second-order consequence.** A reliability refresh is complete only when evidence, behavior, compatibility, and rollback move together.

**Revision decision.** Retain exact queries and add triggers, versions, authority ranking, archiving, repository reproduction, migration, rollback, and rejection examples.

**Retained seed evidence.** The official documentation, GitHub repository, and release-note query labels and texts remain unchanged. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| search_query_label_name | search_query_text_value |
| --- | --- |
| `official_docs_query_phrase` | python reliability reference patterns official documentation best practices |
| `github_repository_query_phrase` | python reliability reference patterns GitHub repository examples |
| `release_notes_query_phrase` | python reliability reference patterns changelog release notes migration |

## Evidence Boundary Notes

**Decision supported.** This section helps decide how each Python reliability claim should reveal what was read, configured, checked, executed, built, observed, inferred, or left uncertain. The seed defines local, external, and combined evidence but not repository policy, current language or tool docs, static diagnostics, runtime tests, package artifacts, operational observations, or provisional design judgments.

**Recommended default and causal basis.** Preserve the three seed labels and add repository-contract, current-primary, static-analysis, runtime-fixture, package-artifact, operational-observation, and provisional-inference classes in use. Annotations, checker results, runtime validation, cleanup tests, package builds, and service observations answer different questions and cannot transfer certainty automatically.

**Operating conditions and assumptions.** Atomic claims cite exact evidence and versions, combined claims list prerequisites, negative evidence names coverage, conflicts remain visible, and uncertainty narrows action. Apply the taxonomy to this reference and downstream Python reliability packets while preserving exact seed labels.

**Failure boundary and alternatives.** Labels decorate prose, a static pass proves runtime safety, one fixture proves production reliability, archive guidance overrides project compatibility, or operational success excuses unsupported design. Bounded alternatives and recoveries: split the statement, downgrade it, add a runtime or package fixture, preserve competing interpretations, narrow support, or decline the recommendation.

**Counterexample, gotchas, and operational comparison.** Configured does not mean executed, checked does not mean validated, tested does not mean packaged, packaged does not mean deployed, and observed once does not mean invariant. Good: archive pattern motivates parsing, current docs define syntax, project config establishes target, runtime fixture rejects malformed input, and package test bounds support. Bad: infer reliability from mypy. Borderline: report one-platform package success with other cells pending.

**Verification, evidence, and uncertainty.** Sample recommendations, trace each clause to class and location, confirm versions and configs, replay fixtures and builds, inspect combined prerequisites, preserve conflicts and negative evidence, and ensure uncertainty changes the decision. The local source explicitly distinguishes typing guardrails from runtime validation and spans all added evidence layers conceptually. Evidence labels cannot eliminate framework variability, operational change, or untested environments.

**Second-order consequence.** Confidence is compositional: reviewers should know which boundary, checker, fixture, package, or operational premise would change the guidance if falsified.

**Revision decision.** Extend the three-label note with repository, current-doc, static, runtime, package, operational, combination, conflict, and compositional-confidence rules.

**Retained seed evidence.** The exact local-corpus, external-research, and combined-evidence definitions remain preserved verbatim. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- `local_corpus_sourced_fact`: statements tied directly to the local source paths above.
- `external_research_sourced_fact`: statements tied to the public URLs above.
- `combined_evidence_inference_note`: synthesis that combines local and public evidence into agent guidance.
