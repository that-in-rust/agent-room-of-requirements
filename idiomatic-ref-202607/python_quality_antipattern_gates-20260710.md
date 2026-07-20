# Python Quality Antipattern Gates

**Decision supported.** This section helps decide what checks a finished piece of Python work must clear before it is handed off. The seed title names a gate theme but the seed never states what a gate means in the mapped source, a hard stop where Python work halts until an eleven-row anti-pattern sweep, a nine-item stack check, and the repo's own commands have all been answered.

**Recommended default and causal basis.** Gate every finished Python change through the anti-pattern sweep, the nine-item stack, and the repo's existing command set before handoff. The mapped gates file is organized as exactly that stop sequence, High-Value Anti-Patterns first, then the Default Reliability Stack phrased as before finishing Python work verify, then Quality Gate Commands, then a compact Review Pass for handoff.

**Operating conditions and assumptions.** The change is Python and its repository's configured tools are identifiable from pyproject.toml, setup.cfg, tox.ini, or noxfile.py. This reference governs how to run quality gates on Python changes, it does not cover activation, mode selection, or pattern authoring, which live in the entrypoint and reliability themes.

**Failure boundary and alternatives.** Gates enforced without the Prefer column become pure rejection, the source pairs every banned shape with its replacement so the gate can propose, not just refuse. Bounded alternatives and recoveries: route pattern-selection questions to the reliability reference and skill-activation questions to the entrypoint theme, this file assumes the code already exists.

**Counterexample, gotchas, and operational comparison.** The stack's ninth item permits skipping a gate only with an explicit reason, silent skips are the failure the item exists to prevent. Good: bouncing a diff at the sweep stage because a helper grew a mutable default. Bad: declaring quality because CI is green while no anti-pattern sweep happened. Borderline: gating a docs-only change, the command stage applies but the sweep has nothing to bite.

**Verification, evidence, and uncertainty.** Confirm the handoff record names sweep outcome, stack outcome, and the exact commands run. The four-heading structure of the 66-line gates file read in full this assignment. How much gate ceremony tiny one-line fixes deserve is left to reviewer judgment by the source.

**Second-order consequence.** The source orders its stages from cheapest to most expensive to argue about, table lookups first, judgment questions last, so following its order front-loads the mechanical rejections and reserves reviewer attention for the eight judgment prompts.

**Revision decision.** Open by defining the four-stage stop sequence, sweep, stack, commands, review pass, so readers apply the source as a gating protocol rather than a reading list.

**Retained seed evidence.** The exact theme title and gate framing remain unchanged. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

## Source Evidence Mapping Table

**Decision supported.** This section helps decide which source row is allowed to justify which class of claim in this theme. The seed map assigns the gates file the generic role of skill entrypoint or reusable agent prompt when it is actually the terminal checklist of the python-coder-01 bundle, the file its own router says to finish with.

**Recommended default and causal basis.** Attribute anti-pattern and stack claims to the gates file by heading, and attribute workflow context to SKILL.md by name when it is used. Reference-map.md's use order ends at High-Value Anti-Patterns and the Default Reliability Stack, and SKILL.md's workflow reaches this file only at verification time, so its role is closer to exit gate than entrypoint.

**Operating conditions and assumptions.** The archive path agents-used-monthly-archive/codex-skills-202606/python-coder-01/references remains stable. The table records where this document's claims come from, it does not vouch for the live state of any linked site.

**Failure boundary and alternatives.** The four external URL rows carry the sourced-fact label without any retrieval having occurred in this evolution, so no claim here may lean on them. Bounded alternatives and recoveries: swap the four generic doc-site rows for the specific pages the bundle's research brief names, which include pytest good-practices and Ruff formatter pages.

**Counterexample, gotchas, and operational comparison.** Tool documentation rows age fastest of all source classes, ruff in particular has been absorbing formatter behavior, so even a future retrieval needs a date stamp to stay meaningful. Good: citing the Why-it-fails column for the bare except rejection. Bad: citing the pytest row for a fixture recommendation, that URL was never fetched. Borderline: citing SKILL.md guardrails here, legitimate but it must be named as a sibling, not the mapped source.

**Verification, evidence, and uncertainty.** Audit each claim in this file for a named heading in the gates file or an explicit sibling-file citation. Full reads this session of the gates file and its four sibling bundle files. Whether the doc sites' current content still matches the bundle's 2026-06-23 snapshot cannot be judged from the archive.

**Second-order consequence.** The gates file is the only bundle member whose content is almost entirely tabular and imperative, which is why it can serve as a gate, provenance for it is provenance for a checklist, cheap to re-verify line by line.

**Revision decision.** Correct the local row's role to terminal quality checklist of the bundle and mark the typing, pytest, mypy, and Ruff rows as unretrieved candidates.

**Retained seed evidence.** Every source row with its category, confidence, and role columns remains preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| source_location_path_key | source_category_artifact_type | source_authority_confidence_level | source_usage_synthesis_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202606/python-coder-01/references/python-quality-gates-and-anti-patterns.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt |
| https://docs.python.org/3/library/typing.html | external_research_source_material | external_research_sourced_fact | primary typing module documentation |
| https://docs.pytest.org/en/stable/ | external_research_source_material | external_research_sourced_fact | primary Python testing framework documentation |
| https://mypy.readthedocs.io/ | external_research_source_material | external_research_sourced_fact | static type checking documentation and constraints |
| https://docs.astral.sh/ruff/ | external_research_source_material | external_research_sourced_fact | linting and formatting tool documentation |

## Pattern Scoreboard Ranking Table

**Decision supported.** This section helps decide which gate stage and which checklist items get attention first under time pressure. The seed scoreboard ranks three document-hygiene rules but never ranks the gates themselves, even though the source's own ordering implies a priority, anti-pattern sweep before stack check before commands before review pass.

**Recommended default and causal basis.** When gate time is short, run the doubly-listed items first, boundary validation, mutable defaults, cancellation preservation, and import-time side effects. The gates file presents its material in that fixed order and the stack numbers its nine items starting from boundary validation, giving an implicit ranking the seed leaves unused.

**Operating conditions and assumptions.** The reviewer can map diff hunks to gate items quickly, unfamiliar code raises the cost of every stage. This ranking prioritizes gate stages and stack items for adoption pressure, it does not rank coding patterns, which the reliability reference scores separately.

**Failure boundary and alternatives.** Treating the seed's 95, 91, and 88 scores or the stack's numbering as measured effect sizes would invent data, both encode authorial ordering only. Bounded alternatives and recoveries: reorder by the repo's own lint-rule hit history once enough gated changes have accumulated.

**Counterexample, gotchas, and operational comparison.** Priority order is not severity order, a low-priority stack item like explicit skip reasons can still block handoff outright. Good: sweeping for the four doubly-listed items in a five-minute review window. Bad: reading the review pass prompts aloud while skipping the mechanical sweep. Borderline: elevating stringly path handling on a Windows-facing repo, sensible local override of the default order.

**Verification, evidence, and uncertainty.** Check that prioritized items appear in the gates file and note which list, table, stack, or both, carries each. Cross-listing comparison between the anti-pattern table and stack read in full. True relative payoff among the nine stack items is not established by the source.

**Second-order consequence.** The eleven anti-patterns and nine stack items overlap by design, mutable defaults and cancellation appear in both, and any item appearing in both lists is the source's strongest signal of priority.

**Revision decision.** Add a gate-stage priority row set, sweep first because it is mechanical, stack second because it is enumerable, review pass last because it needs judgment, alongside the seed's document rows.

**Retained seed evidence.** The three scored seed rows with tier labels remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| pattern_identifier_stable_key | pattern_score_numeric_value | pattern_tier_adoption_level | pattern_failure_prevention_target |
| --- | ---: | --- | --- |
| `python_quality_antipattern_gates` | 95 | default_adoption_pattern_tier | Source Map First: Load local python quality material before synthesizing antipattern gates recommendations. |
| `python_quality_antipattern_gates` | 91 | default_adoption_pattern_tier | Evidence Boundary Split: Separate local facts, external facts, and inference before giving agent instructions. |
| `python_quality_antipattern_gates` | 88 | default_adoption_pattern_tier | Verification Gate Coupling: Attach each recommendation to at least one command, checklist, or review gate. |

## Idiomatic Thesis Synthesis Statement

**Decision supported.** This section helps decide in what form quality expectations for Python work should be written down. The seed thesis recites the load-local-first formula while the source's real thesis is narrower and sharper, quality is verified subtractively, work is finished when eleven known-bad shapes are absent and nine known-good properties are confirmed present.

**Recommended default and causal basis.** Express any new quality rule for Python as either a named bad shape with a replacement or a numbered verifiable property, never as unmeasurable virtue language. The gates file contains no aspirational prose at all, only a rejection table, a numbered verification list, commands, and questions, its form is the argument that quality gating should enumerate rather than exhort.

**Operating conditions and assumptions.** The rule's shape is detectable by command, diff inspection, or a single review question. The thesis orients gate design and review behavior, it does not claim the twenty items are exhaustive for all Python.

**Failure boundary and alternatives.** A subtractive thesis caps at its enumeration, code can pass all twenty checks and still be wrong in ways no listed item covers, the gate proves absence of known hazards, not correctness. Bounded alternatives and recoveries: principle-first framing as the reliability reference does for design work, appropriate upstream of the gate, not at it.

**Counterexample, gotchas, and operational comparison.** Enumerated lists invite completeness illusions, the stack's tests item exists precisely because passing shape checks without behavior tests is a known trap. Good: adding a new gate row named exception-to-None conversion with its typed-result replacement. Bad: adding a gate that code should be maintainable. Borderline: gating on docstring presence, enumerable but the source deliberately omits style items.

**Verification, evidence, and uncertainty.** Test each thesis clause against the gates file's form, every clause should map to a table row, stack item, command, or review question. The wholly enumerative structure of the mapped file, zero exhortative sentences in 66 lines. Where enumeration should stop before the gate list itself becomes unreviewable is a judgment the source does not settle.

**Second-order consequence.** Subtractive gating is what makes the source automatable, every table row names a greppable or lintable shape, an exhortative quality doc could never be turned into CI the way this one can.

**Revision decision.** Restate the thesis as enumerate-then-verify, known-bad absent plus known-good present equals releasable, with the explicit cap that enumeration never proves correctness.

**Retained seed evidence.** The three labeled thesis statements remain preserved beneath the evolved claim. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`local_corpus_sourced_fact`: The local row for `python_quality_antipattern_gates` contains 1 source path(s), which should be treated as the first retrieval surface for this theme.
`external_research_sourced_fact`: The external source map provides public documentation, repository, or ecosystem analogues where available.
`combined_evidence_inference_note`: Reliable use of Python Quality Antipattern Gates comes from loading the local corpus first, checking public ecosystem guidance second, and converting both into verification-backed agent decisions.

## Local Corpus Source Map

**Decision supported.** This section helps decide which of the four source sections a given quality question should open. The seed map correctly lists the gates file with five heading signals but gives no guidance on which heading answers which gate-time question, leaving readers to scan all four sections for every lookup.

**Recommended default and causal basis.** Open the section matching the question type directly, banned shapes, required properties, commands, or review prompts, and read nothing else. The source's headings partition cleanly by question type, what is banned goes to High-Value Anti-Patterns, what must be true goes to Default Reliability Stack, what to run goes to Quality Gate Commands, what to ask goes to Review Pass.

**Operating conditions and assumptions.** The question is gate-time, already-written code being checked, rather than design-time. This map routes questions within the mapped gates file, bundle-wide routing belongs to the entrypoint theme.

**Failure boundary and alternatives.** The heading-to-question mapping breaks for design-time questions, why a pattern is preferred is answered in the reliability reference next door, not anywhere in this 66-line file. Bounded alternatives and recoveries: full-file reads are cheap enough at 66 lines when the question type is unclear.

**Counterexample, gotchas, and operational comparison.** The Review Pass looks like a summary of the other three sections but is not, its Errors and Types prompts have no table counterpart, skipping it loses unique coverage. Good: opening only Quality Gate Commands to pick the check battery for a new repo. Bad: scanning the anti-pattern table for advice on Protocol seams, wrong file entirely. Borderline: opening the stack to justify a review comment, works but the Review Pass prompt is usually the closer fit.

**Verification, evidence, and uncertainty.** Spot-check the four heading signals against the live file and confirm the question-type key still matches section content. Section-by-section content audit of the mapped file performed this assignment. Whether future bundle revisions keep the four-section partition is unknowable now.

**Second-order consequence.** Because the file is only 66 lines, the map's real value is inverted, it tells siblings what not to duplicate, any theme needing the anti-pattern table should link here rather than re-list it.

**Revision decision.** Attach the question-type key to each heading signal so a gate-time lookup opens exactly one of the four sections.

**Retained seed evidence.** The local source row with its title, heading signals, and usage role remains preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| local_source_filepath_value | local_source_title_text | local_source_heading_signals | local_source_usage_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202606/python-coder-01/references/python-quality-gates-and-anti-patterns.md | Python Quality Gates And Anti-Patterns | Python Quality Gates And Anti-Patterns; High-Value Anti-Patterns; Default Reliability Stack; Quality Gate Commands; Review Pass | skill entrypoint or reusable agent prompt |

## External Research Source Map

**Decision supported.** This section helps decide what confidence external tool documentation may contribute to this theme's command guidance. The seed map presents the same four tool-doc URLs as the entrypoint theme but this theme's dependence on them is different, three of its four source sections name concrete tools whose behavior those URLs govern.

**Recommended default and causal basis.** Quote the source's command forms verbatim as archive facts and flag any claim about current tool behavior as requiring retrieval. Quality Gate Commands hardcodes ruff, black, mypy, pyright, and pytest invocations, so unlike prose themes, command rows here can be invalidated by a single upstream flag rename.

**Operating conditions and assumptions.** Consuming repos pin tool versions, unpinned environments widen the gap between archive commands and observed behavior. This map queues external verification targets, it grants no current-fact authority until a dated retrieval exists.

**Failure boundary and alternatives.** None of the four URLs was fetched during this evolution, every command claim therefore carries archive-date risk and must not be presented as verified against current tools. Bounded alternatives and recoveries: running tool --help in the target environment beats any documentation fetch for confirming a specific flag still exists.

**Counterexample, gotchas, and operational comparison.** Ruff and black rows overlap in function, a repo migrating between them makes both URL rows simultaneously relevant and mutually contradictory. Good: noting that ruff format --check comes from the archived source pending confirmation. Bad: asserting the current mypy strict-flag set from the unretrieved row. Borderline: inferring pytest is the bundle's preferred runner from URL presence, corroborated locally so acceptable with a local citation.

**Verification, evidence, and uncertainty.** Confirm no command recommendation cites a URL row without a retrieval date beside it. Zero external fetches recorded in this assignment's working notes. Which of the eight archived command forms have drifted since 2026-06-23 is unknown.

**Second-order consequence.** Command-bearing themes invert the usual refresh economics, one fetched changelog page can confirm or break eight command rows at once, so retrieval here pays more per fetch than in any prose theme.

**Revision decision.** Annotate each URL row with the specific command lines it would verify, making the future retrieval pass a targeted diff rather than open-ended reading.

**Retained seed evidence.** All four external rows with their boundary labels remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| external_source_url_value | external_source_name_text | external_source_usage_role | evidence_boundary_label_value |
| --- | --- | --- | --- |
| https://docs.python.org/3/library/typing.html | Python typing docs | primary typing module documentation | external_research_sourced_fact |
| https://docs.pytest.org/en/stable/ | pytest documentation | primary Python testing framework documentation | external_research_sourced_fact |
| https://mypy.readthedocs.io/ | mypy documentation | static type checking documentation and constraints | external_research_sourced_fact |
| https://docs.astral.sh/ruff/ | Ruff documentation | linting and formatting tool documentation | external_research_sourced_fact |

## Anti Pattern Registry Table

**Decision supported.** This section helps decide which concrete code shapes a Python quality gate must reject on sight. The seed registry holds three documentation-process failures while the mapped source's centerpiece is its eleven-row code table, from mutable default arguments through broad exception-to-None conversion, each with a failure mechanism and a preferred replacement.

**Recommended default and causal basis.** Match every reviewed diff against all eleven rows and require the Prefer replacement, not just removal, for each hit. The source dedicates its first and longest section to that table because gate work starts by matching diff shapes against named hazards, the Why-it-fails column supplies the review justification and the Prefer column supplies the fix.

**Operating conditions and assumptions.** Reviewers have the table at hand, an eleven-row card is small enough to memorize or pin. This registry serves gate-time shape matching on Python diffs, process anti-patterns for documentation work stay in the three seed rows.

**Failure boundary and alternatives.** Importing the table without its two companion columns would recreate the taboo-list failure, a reviewer who can name the ban but not the mechanism or replacement writes unactionable comments. Bounded alternatives and recoveries: encode the lint-catchable class directly into repo configuration and shrink the human sweep to the judgment rows.

**Counterexample, gotchas, and operational comparison.** Several rows have legitimate exceptions the table compresses away, print is fine in CLI user output and assert is fine in tests, the ban text targets library behavior and external validation specifically. Good: flagging manual open and close with the with-statement replacement cited. Bad: flagging logging setup in a CLI main as import-time side effects, entry points are the sanctioned home for effects. Borderline: a cached module-level constant computed at import, cheap and pure so usually acceptable, but worth a question.

**Verification, evidence, and uncertainty.** Cross-check every registry row against the source table's three columns for drift. The eleven-row High-Value Anti-Patterns table transcribed from the full read. Hit-rate data for these rows in this repository's history does not exist yet.

**Second-order consequence.** The table's rows sort into three enforcement classes, lint-catchable like mutable defaults and bare except, type-checker-catchable like uncontained Any, and human-only like exception-to-None conversion, and staffing the gate means covering all three classes, not just the automated two.

**Revision decision.** Adopt the full eleven-row table as the operative registry, keeping mechanism and replacement attached to every row.

**Retained seed evidence.** The three seed process rows with their detection signals remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| anti_pattern_failure_name | failure_cause_risk_reason | safer_default_replacement_pattern | detection_signal_review_method |
| --- | --- | --- | --- |
| context_free_summary_output | agent skips local corpus and produces generic advice | source_map_first_synthesis | verify every listed local path appears in the generated file |
| unsourced_recommendation_claims | guidance appears authoritative without source boundary | evidence_boundary_split_pattern | check for local, external, and inference labels |
| unverified_agent_instruction | recommendation cannot be checked by command or review gate | verification_gate_coupling | require concrete gate in generated reference |

## Verification Gate Command Set

**Decision supported.** This section helps decide which commands constitute the gate for a given repository's Python changes. The seed section supplies only the corpus document verifier while the mapped source's third section is literally titled Quality Gate Commands and lists eight runnable checks plus two rg discovery lines for choosing among them.

**Recommended default and causal basis.** Run the discovery scan, select the repo's configured one-of-each battery, run it as a single gate, and record the selection. The source's rule is use the commands the repo already uses, with the eight-command block as the menu and the rg lines, scanning for pyproject.toml, setup.cfg, tox.ini, noxfile.py, and tool names, as the selection procedure.

**Operating conditions and assumptions.** Config files honestly reflect the tools in use, stale configs mislead the discovery step. These commands gate Python code changes, the seed's document verifier gates edits to this reference file, the two must never substitute for each other.

**Failure boundary and alternatives.** Running the whole menu on one repo is wrong by construction, pytest and unittest, ruff format and black, mypy and pyright are competing pairs, the discovery step exists to pick one of each pair. Bounded alternatives and recoveries: tox or nox sessions subsume the individual commands where those files exist, discovery finds them via the same scan.

**Counterexample, gotchas, and operational comparison.** Python -m build belongs in the menu only for packaging-touching changes, including it routinely slows the gate without adding signal. Good: discovery finds ruff and mypy in pyproject.toml, gate is ruff check, ruff format --check, mypy, pytest. Bad: adding pyright to that same repo for extra safety. Borderline: running black --check where no formatter is configured, defensible as a proposal, wrong as a gate.

**Verification, evidence, and uncertainty.** Compare the recorded battery against the repo's config files after each gated change. The Quality Gate Commands section and both rg discovery lines read in full. Flag-level correctness of the archived command forms against current tool releases is unverified.

**Second-order consequence.** The discovery-first rule quietly makes the gate self-configuring, the same two rg lines work in any repo, so an agent can derive the correct battery without asking anyone, which is exactly what a reusable skill needs.

**Revision decision.** Import the eight-command menu with its discovery preamble and state the pairing rule, one test runner, one formatter, one type checker per repo.

**Retained seed evidence.** The seed's document verifier command block remains preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`verification_gate_command_set`: Run the repository verifier after editing this file.

```bash
python3 agents-used-monthly-archive/idiomatic-references-202606/tools/verify_reference_generation.py --stage final
```

## Agent Usage Decision Guide

**Decision supported.** This section helps decide what script an agent follows when asked to quality-gate Python work. The seed guide tells agents to start with the source map but the mapped source already contains the agent's exact operating script, the eight-prompt Review Pass, Input, Types, Errors, Resources, Async, Imports, Tests, Gates, labeled for use before handoff.

**Recommended default and causal basis.** Have agents emit the eight answers with evidence lines as the gate record for every reviewed Python change. The source frames the pass as compact deliberately, eight one-line questions an agent can answer in order against any diff, producing a reviewable record without loading the rest of the bundle.

**Operating conditions and assumptions.** Diffs are small enough that each prompt can be answered against the whole change, huge diffs need splitting first. This guide scripts agent behavior at gate time, implementation-time behavior is scripted by the entrypoint theme's protocol.

**Failure boundary and alternatives.** The pass assumes code exists to review, an agent invoked at design time gets nothing from it and should be routed to the reliability reference instead. Bounded alternatives and recoveries: the full nine-item stack as the script for release-level audits where more rigor than the compact pass is wanted.

**Counterexample, gotchas, and operational comparison.** Answering yes to Gates requires having actually run the commands, an agent inferring probable success from reading code has failed the prompt's intent. Good: eight labeled answers, with Resources citing the specific with-block added. Bad: a paragraph of overall impressions with no per-prompt structure. Borderline: marking Async not-applicable on synchronous code, correct but should state why in the evidence line.

**Verification, evidence, and uncertainty.** Reject any agent gate record missing one of the eight labels or its evidence line. The Review Pass section's eight prompts read in full. Whether eight prompts stay sufficient as repos adopt newer async and typing constructs is untested.

**Second-order consequence.** The pass doubles as an output format, eight labeled answers are simultaneously the review work and the handoff artifact, collapsing the usual gap between doing a review and documenting it.

**Revision decision.** Make the eight-prompt pass the agent's default script, answered in order with a yes, no, or not-applicable plus one line of evidence per prompt.

**Retained seed evidence.** The four seed usage bullets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`agent_usage_decision_guide`: Use this reference when a task mentions this theme, one of the listed local source paths, or a nearby technology/workflow surface.

- Start with the local corpus source map.
- Prefer patterns with explicit verification gates.
- Treat external sources as freshness and ecosystem checks, not replacements for local repo conventions.
- Preserve the evidence boundary labels when reusing recommendations.

## User Journey Scenario

**Decision supported.** This section helps decide whether this reference matches the user's current position in their task. The seed scenario describes a maintainer seeking discipline generally, but the journey this theme actually serves begins at a specific moment, a change is believed done and someone must decide whether it may ship.

**Recommended default and causal basis.** Enter this reference when a Python change is believed complete, run sweep, stack, commands, pass, and exit with ship, bounce with citations, or escalate. The source's framing sentence, before finishing Python work verify, locates its entire content at that pre-handoff moment rather than during design or implementation.

**Operating conditions and assumptions.** The user has authority to bounce the change or a channel to whoever does. The journey covered runs from believed-done to handed-off, everything upstream belongs to other themes.

**Failure boundary and alternatives.** Arriving earlier in the journey misfires, a user still choosing patterns gets rejection tables when they need design rationale, which lives in the sibling reliability reference. Bounded alternatives and recoveries: for users arriving pre-code, route to the entrypoint theme's activation journey instead.

**Counterexample, gotchas, and operational comparison.** The gate moment tempts scope creep, reviewers spotting design flaws mid-gate should file them separately, not bolt design review onto the ship decision. Good: a reviewer gating a teammate's importer fix in ten minutes with three cited items. Bad: a developer opening this file to decide between dataclasses and dicts. Borderline: self-gating one's own change, valid but the pass's Gates prompt is easy to self-excuse.

**Verification, evidence, and uncertainty.** Ask whether a finished diff exists, if not, this is the wrong reference for the moment. The before-finishing framing sentence and handoff wording of the mapped file. Median wall-clock cost of a full gate cycle on real changes is unmeasured here.

**Second-order consequence.** Positioning the theme at believed-done changes its emotional job, the gate protects the reviewer from having to argue taste, every bounce cites a table row or stack item, making rejection impersonal and fast.

**Revision decision.** Recast the scenario around the pre-handoff moment, the user holds a finished diff and needs a defensible ship-or-bounce decision in minutes.

**Retained seed evidence.** The role, starting state, decision, and trigger lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Role based opening scenario: The Python maintainer is starting from scripts or services that need typing, fixtures, packaging, and lint discipline and needs a reference that turns source evidence into an executable next step.
Primary user starting state: The user has a `python_quality_antipattern_gates` task, one or more local source paths, and uncertainty about which pattern should drive implementation.
Decision being made: choosing how strict to make typing, tests, validation, and dependency hygiene for the current risk level.
Reference opening trigger: Open this file when the task mentions python quality antipattern gates, any mapped local source path, or an adjacent workflow with the same failure mode.

## Decision Tradeoff Guide

**Decision supported.** This section helps decide how much gate to apply to which class of Python change. The seed guide offers generic adopt-adapt-avoid rows without this theme's live tension, gate strictness versus gate throughput, every added check catches more but slows every single change behind it.

**Recommended default and causal basis.** Gate routine changes with sweep plus compact pass, escalate to the full stack and command battery for releases, new modules, or async and boundary code. The source manages that tension by tiering itself, an eleven-row sweep for every change, a nine-item stack for finishing, and a compact eight-prompt pass explicitly for handoff speed.

**Operating conditions and assumptions.** Change classes are distinguishable at gate time, a risk label or path convention suffices. This guide tunes gate depth per change class, it does not license dropping the safety-critical rows for any class.

**Failure boundary and alternatives.** Maximal gating applied uniformly teaches contributors to batch changes into huge PRs to amortize gate cost, which makes each gate pass less thorough, strictness beyond a point reduces realized quality. Bounded alternatives and recoveries: move the mechanical rows into CI so the human tiers govern only judgment items, shrinking the tradeoff surface.

**Counterexample, gotchas, and operational comparison.** Fast-tier drift is gradual, teams quietly reclassify risky paths as routine, periodic audits of tier assignment are part of the tradeoff. Good: full stack on a new async boundary module, compact pass on a typo-class fix. Bad: compact pass on a release cut. Borderline: full stack on every change in a two-person repo, affordable there, corrosive at scale.

**Verification, evidence, and uncertainty.** Sample gated changes quarterly and check tier assignment against the change's actual blast radius. The three-tier structure, table, stack, compact pass, of the mapped file. The throughput cost curve per added gate item is not measured in this repository.

**Second-order consequence.** The doubly-listed items, boundary validation, mutable defaults, cancellation, import effects, form a natural never-skip core, tiering everything else around that core keeps the fast tier honest.

**Revision decision.** Add the strictness-throughput axis with tiered defaults, compact pass for routine changes, full stack for release or risk-flagged changes, sweep always.

**Retained seed evidence.** The adopt, adapt, avoid, and cost-of-being-wrong rows remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| decision_option_name | when_to_choose_condition | tradeoff_cost_description | verification_question_prompt |
| --- | --- | --- | --- |
| Adopt when | local corpus and external evidence agree on the python quality antipattern gates pattern | fastest path, but can copy stale local assumptions | Does the selected pattern appear in the canonical source and current external evidence? |
| Adapt when | local sources are strong but public ecosystem guidance has changed | preserves repo fit, but requires explicit inference notes | Did the reference label the local fact, external fact, and combined inference separately? |
| Avoid when | source evidence is thin, conflicting, or unrelated to the user journey | prevents false confidence, but may require deeper research | Is there a confidence warning or adjacent reference route? |
| Cost of being wrong | wrong python quality antipattern gates guidance can send an agent to the wrong files, tests, or abstraction | wasted implementation loop and weaker verification | Would a reviewer know what to undo and what to inspect next? |

## Local Corpus Hierarchy

**Decision supported.** This section helps decide which bundle file's wording governs when overlapping quality rules differ in detail. The seed hierarchy names the gates file canonical with a thin-evidence warning but omits its precedence relations with the two siblings that share its content, SKILL.md restates five of its bans as guardrails and the reliability reference elaborates several rows into full patterns.

**Recommended default and causal basis.** Quote the gates file for gate decisions and cite the reliability reference when the bounced author asks for the deeper fix rationale. The bundle deliberately repeats safety rules at three altitudes, guardrail one-liners, gate table rows, and pattern sections, so a precedence rule is needed whenever their wordings differ in detail.

**Operating conditions and assumptions.** All three files remain at their archived paths with their current section structure. This hierarchy settles precedence for gate-content questions, activation and pattern-design precedence belong to their own themes.

**Failure boundary and alternatives.** Without stated precedence, a reader might treat SKILL.md's terser guardrail wording as overriding the table's mechanism and replacement columns, losing exactly the detail that makes gate feedback actionable. Bounded alternatives and recoveries: treat this corpus's own python themes as the second opinion layer the warning asks for.

**Counterexample, gotchas, and operational comparison.** The seed's single-source confidence warning stays true in spirit, all three altitudes share one authorship and date, agreement among them is consistency, not independent corroboration. Good: using the table's Prefer column over the guardrail's bare prohibition when writing a bounce comment. Bad: escalating a wording difference between altitudes as a contradiction, it is compression. Borderline: citing the reliability reference's cancellation listing at gate time, richer but slower than the table row.

**Verification, evidence, and uncertainty.** Diff the three altitudes' wordings for each shared rule and confirm differences are compression, not conflict. The shared-rule comparison across guardrails, table, and pattern sections done during full reads. Whether future skill revisions will keep the three altitudes synchronized is unknown.

**Second-order consequence.** The three-altitude repetition is a feature for drift detection, if a future bundle edit changes one altitude and not the others, the disagreement itself flags an incomplete revision.

**Revision decision.** Declare the gates file canonical for what blocks handoff, the reliability reference canonical for why and how to fix, and SKILL.md's guardrails a summary layer that never overrides either.

**Retained seed evidence.** The hierarchy row and its confidence warning remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Classification vocabulary includes canonical, supporting, legacy, duplicate, and conflicting source roles.
Confidence warning: only one local corpus source is mapped, so this reference should invite adjacent-source discovery before becoming canonical policy.

| local_source_filepath_value | corpus_hierarchy_role | heading_signal_to_convert | reviewer_question_to_answer |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202606/python-coder-01/references/python-quality-gates-and-anti-patterns.md | canonical primary source | Python Quality Gates And Anti-Patterns; High-Value Anti-Patterns; Default Reliability Stack | What guidance, warning, or example should this source contribute to Python Quality Antipattern Gates? |

## Theme Specific Artifact

**Decision supported.** This section helps decide what concrete object a team maintains to make this theme's gating repeatable. The seed artifact table asks for an abstract quality rubric while the source's four sections compose directly into a concrete one-page gate card, eleven ban rows, nine stack checkboxes, the repo's selected command battery, and eight pass prompts with answer blanks.

**Recommended default and causal basis.** Instantiate one gate card per repo, use it for every gated change, and re-run discovery to refresh it whenever config files change. Every element of such a card is verbatim source content, only the command battery requires per-repo instantiation via the discovery scan, so the card is derivable rather than authored.

**Operating conditions and assumptions.** Someone owns the card per repo, ownerless cards silently rot. The card standardizes gate execution and its record, it does not replace the source file, which stays the reference of record.

**Failure boundary and alternatives.** A gate card without the per-repo command section is incomplete in the one place that varies, two repos share the bans and stack but almost never share the exact battery. Bounded alternatives and recoveries: a CI pipeline definition as the executable form of the card's mechanical sections, with the card retaining only the human prompts.

**Counterexample, gotchas, and operational comparison.** Laminating the eleven bans into the card is safe, laminating tool flags is not, the command section must stay the card's editable region. Good: a dated card whose battery section says ruff check, mypy, python -m pytest per pyproject scan. Bad: a generic quality checklist with no repo battery. Borderline: sharing one card across a monorepo's packages, works only if their tool configs genuinely match.

**Verification, evidence, and uncertainty.** Check the card's battery against a fresh discovery scan and its fixed sections against the source file. The four-section composition of the mapped file supporting direct card assembly. Card upkeep economics across many small repos is untested here.

**Second-order consequence.** The card's date and repo name turn it into a drift sensor, when a discovery re-scan produces a different battery than the card holds, the card's staleness is proven rather than suspected.

**Revision decision.** Define the artifact as the instantiated gate card, three fixed sections copied from source plus one discovered command section, dated and repo-named.

**Retained seed evidence.** The artifact field rows with completion rules and evidence hints remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Theme specific artifact: quality bar rubric with review blockers, lint gates, and release criteria.

| artifact_field_name | artifact_completion_rule | evidence_source_hint |
| --- | --- | --- |
| user_goal_statement | state the user's concrete goal before applying Python Quality Antipattern Gates | local corpus hierarchy plus critique findings |
| decision_boundary_rule | define the point where this reference should be used or avoided | decision tradeoff guide |
| verification_gate_rule | define the command, checklist, or review question that proves the artifact worked | verification gate command set |

## Worked Example Set

**Decision supported.** This section helps decide which exercise most efficiently teaches someone to operate this theme's gate. The seed examples describe reference usage abstractly while the source's own table rows are miniature worked examples, each ban names a recognizable code shape, def f(items=[]) for mutable defaults, bare except colon, manual open and close, awaiting nothing while calling blocking IO.

**Recommended default and causal basis.** Train new gate operators by having them sweep one recent real diff against all eleven rows and write the eight pass answers. The table's three-column form is example-shaped by design, shape, mechanism, fix, a reviewer learns the gate fastest by walking one real diff against all eleven rows once.

**Operating conditions and assumptions.** A representative recent diff is available, toy examples undertrain shape recognition. Worked examples here teach gate execution, pattern-construction examples live in the reliability reference.

**Failure boundary and alternatives.** Single-row examples mislead about interaction effects, real hazards cluster, a bare except wrapping a blocking call inside an async function trips three rows at once and the fix order matters, unblock first, then narrow the except. Bounded alternatives and recoveries: the rg discovery lines as a second worked example, teaching battery selection on a repo the trainee has never seen.

**Counterexample, gotchas, and operational comparison.** Fix order in multi-hit diffs is not arbitrary, replacing the resource handling before narrowing exceptions avoids masking the cleanup path mid-fix. Good: a walkthrough finding mutable default plus stringly paths and applying both Prefer fixes. Bad: memorizing row names without ever sweeping a diff. Borderline: practicing on generated code, shapes appear but idiom frequency is unrealistic.

**Verification, evidence, and uncertainty.** Have the trainee gate a second diff solo and compare their hits against an experienced operator's sweep. The shape-mechanism-fix structure of all eleven table rows read in full. How many practice sweeps produce reliable shape recognition is unmeasured.

**Second-order consequence.** Sweeping a clean diff is as instructive as sweeping a dirty one, eleven explicit no-hits teach the row shapes while building the habit of recording negative results, which the observability items later depend on.

**Revision decision.** Anchor the section on one composite walkthrough, a small importer diff swept against all eleven rows with two hits and their Prefer fixes applied in dependency order.

**Retained seed evidence.** The good, bad, and borderline seed lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Good example: Use Python Quality Antipattern Gates after loading the canonical source, confirming the external evidence boundary, and writing a verification gate before implementation.
Bad example: Use Python Quality Antipattern Gates as a generic tutorial while ignoring the mapped local paths, source hierarchy, and cost of being wrong.
Borderline case: Use Python Quality Antipattern Gates only after adding a confidence warning when local evidence is thin or conflicts with current ecosystem guidance.

## Outcome Metrics and Feedback Loops

**Decision supported.** This section helps decide which measurements justify and refine the ongoing cost of running this gate. The seed metrics name a coverage indicator but no loop connects gate outcomes back to gate content, nothing tracks which rows actually catch problems and which prompts always answer yes.

**Recommended default and causal basis.** Record row-level and item-level outcomes for every gated change and automate the top recurring mechanical hit each quarter. Every gate execution produces classifiable data for free, per-row hit or no-hit, per-item pass or fail, per-prompt answer, the source's fixed structure makes outcomes tallyable without extra instrumentation.

**Operating conditions and assumptions.** Gate records use consistent row and item names so tallies aggregate cleanly. This loop tunes local gate emphasis and training, it does not license deleting source rows, which remain the reference of record.

**Failure boundary and alternatives.** Hit-rate data misleads in both directions, a never-hitting row may mean the hazard is extinct or that reviewers stopped looking, raw tallies need an occasional seeded-defect audit to stay interpretable. Bounded alternatives and recoveries: escaped-defect tracking, hazards found after handoff mapped back to the row that should have caught them, as the sharper but slower loop.

**Counterexample, gotchas, and operational comparison.** Publishing per-person hit counts turns the gate into a scoreboard and invites gaming, aggregate by codebase area instead. Good: quarterly tally shows mutable defaults hitting repeatedly in one package, a ruff rule is enabled there. Bad: declaring the gate useless because hits declined, decline is the goal. Borderline: timing gate duration per change, useful for the throughput tradeoff but easy to over-optimize.

**Verification, evidence, and uncertainty.** Confirm the journal holds per-row outcomes for recent gated changes and that a quarterly review actually consumed them. The tallyable fixed structure of table, stack, and pass in the mapped file. Hit-rate priors for this repository are unknown until the loop has run.

**Second-order consequence.** The highest-value signal is the second offense, any row that hits twice on the same codebase area marks a spot where a lint rule or fixture would pay for itself immediately.

**Revision decision.** Add the tally loop, count hits per table row and failures per stack item across gated changes, review the distribution quarterly to retarget training and CI automation.

**Retained seed evidence.** The leading indicator, failure signal, and review cadence lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Leading indicator: the next agent can modify the package without weakening type, lint, or fixture coverage.
Failure signal: the reference says quality matters but gives no migration path from loose scripts to strict package code.
Review cadence: Re-run the verifier after every generated-reference edit and refresh external sources when public APIs, docs, or tooling releases change.

## Completeness Checklist

**Decision supported.** This section helps decide what must be confirmed before declaring this reference complete and faithful. The seed checklist confirms this document's sections exist but never audits the gate content against its source, no item catches a silently dropped table row or a stack item paraphrased into vagueness.

**Recommended default and causal basis.** Run the fidelity count against the source file at every reread and refresh cycle before accepting the document. This theme's correctness is largely transcription correctness, eleven rows, nine items, eight commands plus two discovery lines, eight prompts, all countable against the 66-line source in one sitting.

**Operating conditions and assumptions.** The source file remains available at its archived path for comparison. This checklist audits this reference file's fidelity and usability, code auditing is what the gate itself does.

**Failure boundary and alternatives.** Count checks miss semantic drift, a row keeping its name while losing its Prefer column still counts as present, so the audit must check columns and clauses, not just row names. Bounded alternatives and recoveries: checksum the source file and re-audit only when the checksum changes, trading vigilance for effort.

**Counterexample, gotchas, and operational comparison.** Fidelity auditing can ossify the document, evolved guidance may legitimately reorganize source content, the audit checks presence and accuracy, not layout. Good: an audit catching that a transcribed stack lost its explicit-skip-reason clause. Bad: passing the audit because all 26 headings exist. Borderline: flagging paraphrased row wording, acceptable if mechanism and fix survive intact.

**Verification, evidence, and uncertainty.** Count rows, items, commands, and prompts in this document against the source and inspect each for dropped clauses. The countable four-section structure of the mapped file. Whether count-plus-clause auditing catches all meaningful drift is not proven.

**Second-order consequence.** Fixed counts make this the corpus's most mechanically auditable theme, a five-line script comparing counted structures against the source could replace most of the manual audit.

**Revision decision.** Add fidelity items, all eleven rows with all three columns, all nine stack items with their verify framing, the full command menu with discovery lines, all eight prompts with labels.

**Retained seed evidence.** All seven seed checklist bullets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- The role scenario names the user, starting state, decision, and trigger for Python Quality Antipattern Gates.
- The decision guide includes Adopt when, Adapt when, Avoid when, and Cost of being wrong.
- The local corpus hierarchy identifies canonical and supporting sources or gives a confidence warning.
- The theme specific artifact is concrete enough to review without reading every mapped source.
- The examples cover good, bad, and borderline usage.
- The metrics section names one leading indicator and one failure signal.
- The adjacent routing section points to a better reference when this one is not the right fit.

## Adjacent Reference Routing

**Decision supported.** This section helps decide where to send a question that arrived at the gate but is not a gate question. The seed routing splits the theme name into python, quality, and antipattern tokens, producing self-referential rows, while the real neighbors are the entrypoint theme for activation, the reliability-patterns theme for design rationale, and the routing-sources theme for source governance.

**Recommended default and causal basis.** When a gate conversation drifts from is-this-acceptable to which-design-is-better, stop gating and hand off with the destination named. The corpus holds python_language_skill_entrypoint and python_reference_routing_sources alongside this file, and the bundle's reliability reference underlies the reliability-patterns theme, giving every out-of-scope question a concrete destination.

**Operating conditions and assumptions.** The named destination themes exist and cover the drifting question. Routing sends away questions this theme cannot close, it does not summarize destination content.

**Failure boundary and alternatives.** The commonest misroute runs inward, design-time questions arriving at this gate theme, the tell is a question containing should I use, which no gate table can answer. Bounded alternatives and recoveries: external tool documentation, explicitly labeled unverified, for tool-flag questions no internal theme answers.

**Counterexample, gotchas, and operational comparison.** Bans look like design advice, do not use mutable defaults reads as guidance, but the why and the deeper alternatives still live in the reliability reference, route follow-ups there. Good: routing a Protocol-versus-ABC question to the reliability-patterns theme mid-review. Bad: routing to the quality adjacent reference, a token synonym for this same file. Borderline: keeping a which-formatter question here, the discovery scan answers it for configured repos, route only greenfield cases.

**Verification, evidence, and uncertainty.** Confirm each named destination file exists in the corpus and matches its assigned question class. The corpus python-theme listing and the bundle's file roles. Actual misroute frequency at this theme is estimated, not measured.

**Second-order consequence.** Gate themes are natural routing hubs because everyone eventually passes the gate, encoding the outbound routes here propagates them to every contributor at the moment they are most attentive, bounce time.

**Revision decision.** Route should-I-use questions to the reliability-patterns theme, when-to-activate questions to the entrypoint theme, and which-source-wins questions to the routing-sources theme.

**Retained seed evidence.** The three seed adjacent-reference lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Adjacent reference guidance: Use reliability, routing, or quality references when the problem is governance rather than syntax.
Adjacent reference 1: consider the python adjacent reference when the current task pivots away from python quality antipattern gates.
Adjacent reference 2: consider the quality adjacent reference when the current task pivots away from python quality antipattern gates.
Adjacent reference 3: consider the antipattern adjacent reference when the current task pivots away from python quality antipattern gates.

## Workload Model

**Decision supported.** This section helps decide how much gating one person or agent can perform without quality decay. The seed model budgets requirement packets and twenty requirement IDs, an authoring workload, while this theme's real unit of work is the gate cycle, one diff swept, checked, commanded, and passed, repeated many times daily.

**Recommended default and causal basis.** Gate one reviewable diff per cycle and refuse oversized diffs at intake, splitting beats skimming. The source is sized for that cycle, 66 lines total with the compact pass explicitly built for handoff speed, its economics assume dozens of cheap executions rather than one expensive read.

**Operating conditions and assumptions.** Contributors can actually split changes, entangled legacy refactors sometimes cannot be, and get the strict tier with extra time instead. This model budgets gate execution effort, authoring and refresh effort for this document is a separate, rarer workload.

**Failure boundary and alternatives.** The cycle's cost scales with diff size, not file size, a thousand-line diff cannot be swept meaningfully in one cycle and must be split before gating, no budget tweak fixes an oversized unit. Bounded alternatives and recoveries: CI-automated mechanical rows shift the human cycle to judgment items only, halving cycle time at the cost of pipeline upkeep.

**Counterexample, gotchas, and operational comparison.** Batching many small diffs into one gate session saves setup time but degrades per-diff attention near the end of the session, cap sessions rather than stretching them. Good: six small diffs gated in a morning with full records. Bad: one twelve-hundred-line diff waved through with a compact pass. Borderline: gating during code authoring continuously, thorough but dissolves the believed-done moment the gate needs.

**Verification, evidence, and uncertainty.** Track cycle counts and per-cycle durations in the journal and watch for end-of-session record thinning. The compact-pass framing and 66-line size of the mapped source. The reviewable-size threshold varies by codebase familiarity and is judgment.

**Second-order consequence.** Because cycle cost is per-change, the gate's total cost is set by change granularity policy, teams that ship small diffs get more gate coverage per hour than the gate's own design can provide to big-batch teams.

**Revision decision.** Restate capacity in cycle terms, one diff of reviewable size per cycle, sweep plus pass in minutes for the fast tier, stack and battery added for the strict tier.

**Retained seed evidence.** The workload dimension rows with boundary values remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`combined_evidence_inference_note`: Treat Python Quality Antipattern Gates as a quality gate operating reference, not as a prose summary.

| workload_dimension_name | workload_boundary_value | verification_pressure_point |
| --- | --- | --- |
| primary_usage_surface | specification, test, review, and verification work where the artifact must turn ambiguous intent into executable evidence | verify that the reference changes the next implementation or review action |
| bounded_capacity_model | one requirement packet, 20 requirement IDs or fewer, one traceability matrix, and one final gate command set | split the task or create a narrower reference when this boundary is exceeded |
| source_pressure_model | local heading signals include Python Quality Gates And Anti-Patterns; High-Value Anti-Patterns; Default Reliability Stack; Quality Gate Commands; Review Pass | compare guidance against canonical local sources before following external examples |
| artifact_pressure_model | required artifact is quality bar rubric with review blockers, lint gates, and release criteria | require the artifact before claiming the reference is operationally usable |

## Reliability Target

**Decision supported.** This section helps decide what reliability the gate itself must demonstrate to keep its authority. The seed targets measure document properties like label preservation while the gate's own reliability question goes unstated, how often does a change that passed all four stages still carry a hazard the source enumerates.

**Recommended default and causal basis.** Triage every post-handoff discovery of an enumerated hazard within a week and record which stage should have caught it. A gate's worth is its false-pass rate on the hazards it claims to cover, the eleven rows and nine items define that coverage claim precisely, making misses attributable to specific stages.

**Operating conditions and assumptions.** Post-handoff defects are actually traced to their introducing change, without blame culture suppressing reports. Targets here cover gate operation reliability, hazards outside the enumerated twenty are explicitly outside the gate's claim and outside these targets.

**Failure boundary and alternatives.** False-pass measurement needs escaped hazards to surface, in low-traffic repos the sample accumulates too slowly for statistics and only qualitative miss reviews are honest. Bounded alternatives and recoveries: sampled re-gating of shipped changes by a second operator as a proactive measure where escape data is sparse.

**Counterexample, gotchas, and operational comparison.** Zero escapes can mean excellent gating or blind consumers, corroborate quiet quarters with an occasional seeded-hazard drill. Good: an escaped bare except triaged as a sweep miss and added to training diffs. Bad: counting a novel hazard class as gate failure, it was never in the claim. Borderline: counting an explicitly skipped gate's escape, the skip reason was recorded, policy decides whether that counts.

**Verification, evidence, and uncertainty.** Review the quarterly escape ledger and confirm each entry names its stage attribution. The enumerated coverage claim formed by the source's table and stack. This repository's baseline escape rate is unknown until tracking begins.

**Second-order consequence.** Attributing each escape to a stage converts failures into upgrades, a sweep miss retrains shape recognition, a battery gap adds a lint rule, the taxonomy is the improvement mechanism.

**Revision decision.** Add the operational target, zero enumerated-hazard escapes per quarter with every escape triaged to its missing stage, sweep miss, stack miss, battery gap, or pass miss.

**Retained seed evidence.** All four seed reliability rows with thresholds remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| reliability_target_name | measurable_threshold_value | evidence_collection_method |
| --- | --- | --- |
| source_boundary_preservation | 100 percent of recommendations keep local, external, and inference boundaries visible | review generated text for the three evidence labels before reuse |
| decision_accuracy_sample | at least 18 of 20 sampled uses route to the correct adopt, adapt, avoid, or adjacent-reference decision | sample downstream tasks and record reviewer verdicts |
| unsupported_claim_rate | zero unsupported production, security, latency, or reliability claims in final guidance | reject claims without source row, explicit inference note, or verification method |
| recovery_path_clarity | every avoid or failure case names the rollback, escalation, or next-reference route | inspect failure-mode and adjacent-routing sections together |

## Failure Mode Table

**Decision supported.** This section helps decide which ways this gate itself can silently fail and how each is caught. The seed table covers drift and traceability failures but not the gate-specific decay modes, rubber-stamping where all eight prompts get reflexive yes answers, and gate theater where records exist but commands never ran.

**Recommended default and causal basis.** Run one seeded-hazard drill per quarter and spot-re-execute the recorded battery on a sampled change. Checklist instruments decay predictably under repetition, the source's own ninth stack item, skipped with an explicit reason, shows its authors anticipated the temptation to shortcut the command stage.

**Operating conditions and assumptions.** Drills are announced as policy but unannounced in timing, known drills get gamed like anything else. This table catalogs failures of gate operation, code failure modes are the gate's subject matter, not its own failure modes.

**Failure boundary and alternatives.** Both decay modes produce perfect-looking records, detection cannot read the records themselves and must probe behind them, re-running commands or seeding a known-bad diff. Bounded alternatives and recoveries: rotating gate duty between operators surfaces decay socially, fresh eyes notice reflexive yes patterns.

**Counterexample, gotchas, and operational comparison.** Probing signals distrust if framed punitively, frame drills as calibrating the gate, not auditing the operators. Good: a drill diff with a planted mutable default caught at sweep, calibration confirmed. Bad: quarterly metrics celebrated while no one has re-run a battery in a year. Borderline: one operator's pass answers growing terse, possibly efficient fluency, possibly early rubber-stamping.

**Verification, evidence, and uncertainty.** Confirm drill results and battery re-executions appear in the journal at the stated cadence. The ninth stack item's explicit-reason clause showing anticipated shortcut pressure. Actual decay onset time for gates in this environment is unmeasured.

**Second-order consequence.** Gate decay is invisible precisely because the gate defines what evidence looks like, which is why every added row's mitigation is an out-of-band probe rather than another record field.

**Revision decision.** Add rows for rubber-stamping, gate theater, tier misassignment, and stale battery, each with a probe-style detection since records alone cannot reveal them.

**Retained seed evidence.** All four seed failure rows with mitigations remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| failure_mode_name | likely_trigger_condition | required_mitigation_action |
| --- | --- | --- |
| source drift hides truth | external or local guidance changes after the reference was written | refresh public evidence, rerun local corpus gate, and mark stale claims before reuse |
| generic advice escapes review | agent copies plausible best practices without theme-specific verification | block completion until the verification gate names concrete command, reviewer question, or metric |
| green check misses requirement | test command passes while a requirement lacks traceability | audit every REQ ID against at least one test or review assertion |
| metric claim has no method | performance or reliability language appears without measurement | replace claim with threshold, fixture, command, and owner |

## Retry Backpressure Guidance

**Decision supported.** This section helps decide how many gate cycles a change gets and what each re-gate must re-check. The seed guidance covers document-verification retries but not gate-outcome retry policy, what happens after a bounce, how many gate cycles a change may consume, and when repeated bounces stop being normal iteration.

**Recommended default and causal basis.** On re-gate, verify each bounced item's fix explicitly, then run one full sweep of the revised diff before issuing the pass. A bounce with cited rows is a complete repair specification, the Prefer column tells the author exactly what to change, so a healthy re-gate should converge in one cycle for mechanical hits.

**Operating conditions and assumptions.** Bounces carry row citations so re-gates know their focus, uncited bounces cannot be scoped. This section governs the gate's own retry loop, code-level retry and cancellation guidance belongs to the reliability-patterns theme.

**Failure boundary and alternatives.** Unbounded re-gating burns reviewer capacity on a change that may be structurally unsound, three cycles without convergence usually means the diff needs redesign, not another sweep. Bounded alternatives and recoveries: pairing the author with the gate operator for the fix session collapses the bounce-retry loop entirely on complex hits.

**Counterexample, gotchas, and operational comparison.** Backpressure applies to the gate queue too, when believed-done changes pile up awaiting gates, the temptation is thinning the gate, the correct response is adding gate capacity or automating mechanical rows. Good: a bounce for manual open and close, fixed and re-gated once with a clean fresh sweep. Bad: a fifth re-gate of the same importer diff with new hits each round. Borderline: skipping the fresh sweep when the fix was a one-token default_factory change, defensible, records should say so.

**Verification, evidence, and uncertainty.** Count gate cycles per change in the journal and confirm escalations fired at the threshold. The repair-specification structure of the table's Prefer column. The right escalation threshold may differ for legacy versus greenfield code.

**Second-order consequence.** Re-gate scope is the subtle choice, checking only the bounced items is fast but misses regressions the fix introduced, the fresh-sweep-plus-focus compromise costs minutes and closes that hole.

**Revision decision.** Add the convergence policy, mechanical hits get one focused re-gate limited to bounced items plus a fresh sweep, three total cycles triggers escalation to design review.

**Retained seed evidence.** All five seed retry and backpressure bullets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- Retry only after the failed verification signal is classified as transient, stale evidence, missing context, or true contradiction.
- Use one bounded retry for stale external evidence refresh, then escalate to a human or a narrower source-specific reference.
- Apply backpressure by stopping new generation or implementation work when source coverage, critique coverage, or verification gates are red.
- For long-running agent workflows, checkpoint after each batch and re-read the current spec before any broad rewrite, commit, push, or destructive operation.
- For distributed execution, assign one owner per generated file or theme batch and require merge-time verification of exact path, heading, and evidence-boundary invariants.

## Observability Checklist

**Decision supported.** This section helps decide what evidence each gate cycle must produce for the surrounding loops to function. The seed checklist logs document-usage evidence but not the gate record schema, what a completed gate cycle must leave behind for later audit, escape triage, and the tally loop to consume.

**Recommended default and causal basis.** Emit the full record for every gate cycle, no-hit entries included, and store it where the quarterly tally can reach it. The metrics, reliability, and failure sections above all consume gate records, so the record schema is the load-bearing observability decision, per-row sweep outcomes, per-item stack results, the exact battery with exit codes, and the eight labeled pass answers.

**Operating conditions and assumptions.** Record emission is cheap, a filled template or structured log line, ceremony-heavy records will be abandoned. This section specifies observability of gate operation, observability requirements for the gated code itself are one of the stack's own concerns.

**Failure boundary and alternatives.** Records missing the no-hit entries cripple every downstream loop, a sweep that only logs hits cannot distinguish clean from unswept, negative results are the majority of the signal. Bounded alternatives and recoveries: deriving records automatically from CI runs for the mechanical stages, leaving humans to author only the pass answers.

**Counterexample, gotchas, and operational comparison.** Records quoting diff content can smuggle secrets into logs, reference changes by identifier and line range, never by copied payload. Good: a structured record showing eleven sweep entries, four passing commands, and eight labeled answers. Bad: a thumbs-up emoji as the gate record. Borderline: recording only deviations from all-clear, compact but it erases the negative-result signal.

**Verification, evidence, and uncertainty.** Sample recent records and check each field of the minimal schema is present and non-generic. The downstream consumption needs established by the tally, escape, and drill loops. The sustainable record weight before operators start abbreviating is unknown.

**Second-order consequence.** With exit codes captured, the record becomes replayable, an auditor can re-run the identical battery and diff outcomes, turning gate theater detection from interrogation into computation.

**Revision decision.** Define the minimal record, change identifier, tier, eleven sweep outcomes including no-hits, stack results where run, battery commands with exit codes, eight pass answers, operator, and date.

**Retained seed evidence.** All six seed observability bullets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- Record which local sources were loaded and which were intentionally skipped.
- Record the exact verification command, reviewer question, or rendered artifact used as proof.
- Record p50/p95/p99 latency or reviewer-time measurements when the reference affects runtime or workflow speed.
- Capture reviewer decision, unresolved uncertainty, and next refresh trigger.
- Record leading indicator and failure signal from this file in the coverage manifest or journal when the reference drives real work.
- Keep audit evidence small enough to review: command output summary, changed-file list, and unresolved-risk notes are preferred over raw transcript dumps.

## Performance Verification Method

**Decision supported.** This section helps decide how to prove the gate is fast enough without proving it by missing things. The seed method demands REQ-to-test mapping, an authoring concern, while the gate's performance question is its own latency, how long a cycle takes per tier and whether the gate is becoming the delivery bottleneck.

**Recommended default and causal basis.** Log timestamps for gate request, start, and completion, review the wait-versus-work split monthly, and fix waits before touching the checklist. The source built the compact pass specifically as the low-latency tier, so cycle time per tier is the design's own success measure, a compact pass that takes an hour has failed its purpose.

**Operating conditions and assumptions.** Timestamps are captured automatically or trivially, manual timing will be skipped under load. This method verifies the gate process's performance, performance verification of gated code belongs to the code's own budgets and profiling.

**Failure boundary and alternatives.** Optimizing cycle time alone invites the thinning failure, faster gates that miss more, latency numbers are only interpretable alongside the escape ledger from the reliability section. Bounded alternatives and recoveries: dedicated gate hours where operators batch cycles, trading immediacy for predictable wait bounds.

**Counterexample, gotchas, and operational comparison.** Averaging hides the tail, one monster diff blocking the queue for a day disappears in a monthly mean, track the p95 wait as the operative number. Good: p95 queue wait cut from a day to two hours by adding a second operator. Bad: celebrating a three-minute average cycle while escapes tripled. Borderline: skipping the strict tier during a release crunch, exactly when it pays most, the trade must be explicit.

**Verification, evidence, and uncertainty.** Inspect the monthly wait-work split and confirm escape figures were read beside the latency figures. The compact-versus-full tiering of the source expressing intended latency classes. Acceptable p95 wait depends on team cadence and is a local policy choice.

**Second-order consequence.** Queue wait usually dominates cycle time in unhealthy gates, changes sitting a day for a ten-minute review, so the highest-leverage performance fix is scheduling and capacity, not checklist trimming.

**Revision decision.** Measure per-tier cycle time and queue wait separately, target minutes for the compact tier, and always read latency jointly with the escape rate.

**Retained seed evidence.** The method, indicator, measurement packet, and pass and fail lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Performance method: require 100 percent REQ-to-test mapping and fail closed when any claim lacks a verification command or review assertion.
Leading indicator to measure: the next agent can modify the package without weakening type, lint, or fixture coverage.
Failure signal to watch: the reference says quality matters but gives no migration path from loose scripts to strict package code.
Required measurement packet: capture input size, source count, tool-call count, wall-clock time, p50/p95/p99 latency where runtime applies, and reviewer decision time where documentation applies.
Pass condition: the reference must let a reviewer identify the correct next action, verification gate, and stop condition without reading unrelated files.
Fail condition: the reference encourages implementation before the workload, reliability target, and failure-mode table are explicit.

## Scale Boundary Statement

**Decision supported.** This section helps decide at what organizational size this gate design must change shape rather than just replicate. The seed statement bounds document scale but not the gate's scaling seams, one operator's shape memory, one repo's battery, and human sweep bandwidth all stop scaling well before large-team or many-repo settings.

**Recommended default and causal basis.** Within one team and few repos apply the gate as written, at larger scale automate the mechanical rows into shared config before adding operators. The source is a single-reviewer instrument, its sweep relies on individual shape recognition and its battery on one repo's config, nothing in its 66 lines addresses fleet consistency or multi-operator calibration.

**Operating conditions and assumptions.** Lint and type-check infrastructure can host the mechanical rows, some environments lack even that. This statement marks where this theme's guidance stops, fleet-level quality governance needs machinery this corpus does not yet contain.

**Failure boundary and alternatives.** Scaling by copying the file to every team scales the text but not the calibration, two operators with the same card can drift far apart in what they bounce, uncalibrated gates are inconsistent gates. Bounded alternatives and recoveries: periodic cross-operator gating of the same sample diff as a calibration ritual where automation is not yet feasible.

**Counterexample, gotchas, and operational comparison.** Shared CI config becomes its own drift surface at scale, the fleet's battery definitions need the same ownership and refresh discipline as any gate card. Good: a platform team publishing shared ruff config encoding six mechanical rows fleet-wide. Bad: forty teams each hand-sweeping all eleven rows with no calibration. Borderline: one operator gating three related repos, workable until their batteries diverge.

**Verification, evidence, and uncertainty.** Check that repos beyond the small-scale seam have the mechanical rows in shared automated config. The single-reviewer, single-repo assumptions visible throughout the mapped file. The exact operator and repo counts where drift outpaces calibration are estimates.

**Second-order consequence.** The scaling path the source implicitly endorses is automation of its own mechanical majority, eight of eleven rows are lint-expressible, pushing them into shared CI config scales perfectly and leaves humans a three-row judgment sweep that calibrates far more easily.

**Revision decision.** Add the seams, per-operator calibration beyond a handful of operators, per-repo batteries beyond a handful of repos, and human sweeps beyond small diffs all require automation or shared-calibration machinery this file does not provide.

**Retained seed evidence.** All four seed scale-boundary paragraphs remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Python Quality Antipattern Gates stops being sufficient when the task spans multiple independent systems, more than one ownership boundary, unbounded source discovery, or production traffic without an explicit SLO.
Under distributed execution, split work by theme file and preserve one verification owner per split; do not let parallel agents rewrite the same reference without a merge checkpoint.
Under long-running agent workflows, treat context drift as a reliability failure: checkpoint state, summarize open risks, and verify against the spec before continuing.
Under large-codebase scale, require dependency or source-graph narrowing before applying this reference; a source list without ranked canonical guidance is not enough.

## Future Refresh Search Queries

**Decision supported.** This section helps decide which searches reveal that this gate theme's enumeration or commands have gone stale. The seed queries recycle the theme name, but this theme's staleness lives in specific claims, tool command syntax, lint-rule coverage of the eleven rows, and whether new Python releases add hazards the table should gain.

**Recommended default and causal basis.** Each refresh cycle, probe tool release notes against the command block and sweep one new-hazards query per major Python release. The gate's authority rests on its enumeration staying current, a new async footgun or a renamed ruff flag ages this theme faster than any wording drift, so probes must target the enumeration and the commands.

**Operating conditions and assumptions.** Refresh effort is bounded, per-row probes are ordered by the row's local hit rate so busy rows refresh first. These queries schedule staleness probes for this file's enumerated claims, broader Python research belongs to the reliability-patterns theme's refresh.

**Failure boundary and alternatives.** Theme-name searches return this corpus's own files and generic listicles, neither can tell whether ruff now auto-fixes mutable defaults or whether a new interpreter release changed exception semantics. Bounded alternatives and recoveries: watching the bundle itself for upstream revisions, if python-coder-01 ships a new gates file, diffing it beats all external probes.

**Counterexample, gotchas, and operational comparison.** A probe finding a new auto-fix does not delete the row, it moves the row's enforcement class from human to lint, the table entry survives the tooling change. Good: a probe finding a ruff rule now covering stringly path handling, updating that row's enforcement class. Bad: logging the theme-name query returned nothing new. Borderline: probing pyright adoption trends, market interest, not a claim this file makes.

**Verification, evidence, and uncertainty.** Record each probe with date and the specific row or command it confirmed or changed. The tool-and-version-pinned nature of the command block and enforcement classes. The cadence at which new table-worthy hazards emerge is irregular and unpredictable.

**Second-order consequence.** The eleven rows double as a probe checklist, asking per row whether detection tooling improved converts refresh from open-ended reading into eleven bounded yes-no investigations.

**Revision decision.** Replace the name-based trio with claim probes, current ruff rule coverage for each mechanical row, current pytest and mypy invocation changes, and new-release Python pitfalls candidate for table addition.

**Retained seed evidence.** The three seed query rows remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| search_query_label_name | search_query_text_value |
| --- | --- |
| `official_docs_query_phrase` | python quality antipattern gates official documentation best practices |
| `github_repository_query_phrase` | python quality antipattern gates GitHub repository examples |
| `release_notes_query_phrase` | python quality antipattern gates changelog release notes migration |

## Evidence Boundary Notes

**Decision supported.** This section helps decide which of this document's statements may travel elsewhere and under what label. The seed notes define the three labels but omit this evolution's concrete ledger, the mapped 66-line gates file read fully, four sibling bundle files read fully and cited by name where used, zero external URLs retrieved, and every operational design above marked as inference.

**Recommended default and causal basis.** When reusing a claim from this file, first ask whether the count audit could verify it, if yes cite the source heading, if no carry the reasoning along. The gate protocol, tiering policy, record schema, and calibration guidance in this document extend the source rather than restate it, honest labeling requires separating transcribed source content from this evolution's constructed machinery.

**Operating conditions and assumptions.** The source file stays at its archived path so fact-class claims remain re-checkable. These notes govern reuse of this document's claims, the transcribed enumeration travels freely with citations, the constructed machinery travels only with its reasoning.

**Failure boundary and alternatives.** The highest-risk mislabel here is presenting the tiering and drill policies as source facts, the source contains neither tiers nor drills, both are inference built on its structure. Bounded alternatives and recoveries: inline per-claim labels if the section-level split proves too coarse for downstream disputes.

**Counterexample, gotchas, and operational comparison.** Sibling-file citations, SKILL.md guardrails or reliability-reference listings, are still local corpus facts but about files this theme does not map, reuse must name the actual file. Good: reusing the eleven-row table with its source heading cited. Bad: citing the quarterly drill cadence as a python-coder-01 requirement. Borderline: reusing the never-skip core list, derived from source cross-listing but the derivation should travel with it.

**Verification, evidence, and uncertainty.** Sample claims from earlier sections and confirm each falls cleanly on one side of the published split. This assignment's read ledger, 66 mapped lines plus 326 sibling lines read, zero retrievals. Readers cannot re-verify the reading itself, only the citations it produced.

**Second-order consequence.** The fact-inference split maps exactly onto the fidelity audit from the completeness section, everything the count audit covers is fact, everything it cannot count is inference, one boundary serves both purposes.

**Revision decision.** Publish the split explicitly, table rows, stack items, commands, and prompts are local corpus facts, tiers, records, drills, calibration, and escalation thresholds are combined-evidence inference.

**Retained seed evidence.** The three labeled boundary definitions remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- `local_corpus_sourced_fact`: statements tied directly to the local source paths above.
- `external_research_sourced_fact`: statements tied to the public URLs above.
- `combined_evidence_inference_note`: synthesis that combines local and public evidence into agent guidance.
