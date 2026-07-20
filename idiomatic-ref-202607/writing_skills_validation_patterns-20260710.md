# Writing Skills Validation Patterns

**Decision supported.** This section helps decide whether a skill document may be deployed and what evidence of agent compliance that deployment requires. The seed title names validation patterns without stating the source discipline they encode, that writing a skill document is test-driven development where pressure-tested subagent behavior is the failing test.

**Recommended default and causal basis.** Validate every discipline-enforcing skill through the red-green-refactor loop, baseline failure without the skill, compliance with it, then loophole closure. Skill documents change agent behavior only if they counter the rationalizations agents actually produce, and only a baseline run without the skill reveals those rationalizations.

**Operating conditions and assumptions.** The skill under test enforces rules with compliance costs, subagent test runs are available, and baseline behavior can be observed before writing. The patterns govern validating skill documents against agent behavior and do not govern the underlying engineering discipline a skill may teach.

**Failure boundary and alternatives.** Full baseline-and-pressure testing is disproportionate for pure reference skills with no rules an agent has any incentive to bypass. Bounded alternatives and recoveries: academic question checks for pattern skills, retrieval-and-application checks for reference skills, or skipping formal testing for skills with no rule to violate.

**Counterexample, gotchas, and operational comparison.** Authors skip the baseline because the skill seems obviously clear, and the source's rationalization table exists precisely because that confidence is unreliable. Good: a TDD skill bulletproofed through six documented iterations. Bad: deploying a batch of skills untested for efficiency. Borderline: a syntax reference checked only by retrieval scenarios.

**Verification, evidence, and uncertainty.** Run the source's pressure scenario against an agent with and without the skill and compare choices and cited sections. The local SKILL.md states writing skills IS TDD applied to process documentation and maps every TDD concept onto skill creation. How well subagent pressure results generalize across model versions is untested here, so revalidation cadence stays judgment.

**Second-order consequence.** A skill document is production code whose runtime is another agent's judgment, so untested skills fail exactly like untested code.

**Revision decision.** Open by stating the source's Iron Law for documentation, no skill without a failing test first, meaning a baseline scenario run before the skill is written.

**Retained seed evidence.** The exact theme title and its framing as writing skills validation patterns remain unchanged. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

## Source Evidence Mapping Table

**Decision supported.** This section helps decide which recorded source may back which claim about skill validation practice. The seed map lists four local rows although they are two files mirrored byte-identically between the 202603 archive and the live claude-skills tree, and its three URLs carry no retrieval record.

**Recommended default and causal basis.** Cite the live claude-skills copies as working sources, note the 202603 archive rows as dated mirrors, and treat all URLs as unrefreshed candidates. Four rows imply four witnesses, but a mirror only adds a second place to find the same 655 and 384 lines, not corroboration.

**Operating conditions and assumptions.** Rows resolve to real paths, mirrors are diff-confirmed, and confidence labels let a reader weigh claims without opening every file. The table records provenance for this document's claims and does not decide whether the archive or live tree is the maintained home.

**Failure boundary and alternatives.** The mapping cannot say which tree receives future edits, so a citation may point at the copy that silently forks. Bounded alternatives and recoveries: merge mirrors into single rows with a locations column, attach content hashes to detect forks, or date external rows at first retrieval.

**Counterexample, gotchas, and operational comparison.** The live tree is the copy most likely to change, which will quietly invalidate the mirror note unless diffs are rerun. Good: citing the pressure-scenario format from testing-skills-with-subagents with the mirror noted. Bad: counting archive and live copies as agreeing sources. Borderline: citing the AGENTS.md URL for instruction-format context while flagging no retrieval.

**Verification, evidence, and uncertainty.** Diff each archive path against its live counterpart and confirm every external citation names its URL row. Diffs run during this evolution confirmed both SKILL.md copies and both testing-guide copies are byte-identical. Whether the three public URLs discuss skill testing at all is unknown because none was fetched.

**Second-order consequence.** A live skills tree snapshotted into monthly archives duplicates by design, so identity notes belong in every mapping over this corpus.

**Revision decision.** Collapse the four local rows into two files each mirrored across the archive and live trees, and mark the external rows as never retrieved.

**Retained seed evidence.** All seven source rows with their category, confidence, and synthesis-role columns remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| source_location_path_key | source_category_artifact_type | source_authority_confidence_level | source_usage_synthesis_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/claude-skills-202603/superpowers/writing-skills/SKILL.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/claude-skills-202603/superpowers/writing-skills/testing-skills-with-subagents.md | local_corpus_source_material | local_corpus_sourced_fact | local agent-usable source material |
| claude-skills/superpowers/writing-skills/SKILL.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt |
| claude-skills/superpowers/writing-skills/testing-skills-with-subagents.md | local_corpus_source_material | local_corpus_sourced_fact | local agent-usable source material |
| https://developers.openai.com/codex/guides/agents-md | external_research_source_material | external_research_sourced_fact | primary agent instruction context model |
| https://docs.github.com/actions | external_research_source_material | external_research_sourced_fact | verification and automation model |
| https://agents.md/ | external_research_source_material | external_research_sourced_fact | general agent instruction format |

## Pattern Scoreboard Ranking Table

**Decision supported.** This section helps decide which validation habits deserve default adoption when a skill is being written or edited. The seed scoreboard scores 95, 91, and 88 for corpus hygiene and never ranks the source's own validated patterns, baseline-before-writing, multi-pressure scenarios, and explicit loophole counters.

**Recommended default and causal basis.** Rank baseline-before-skill first, multi-pressure verification second, and verbatim rationalization capture third. Writers optimize what the scoreboard rewards, and a board silent on baseline testing licenses skills written from author intuition alone.

**Operating conditions and assumptions.** Each row names the concrete deployment failure it prevents, such as a skill that agents rationalize around under deadline pressure. The scoreboard ranks skill-validation practices for this theme and does not rank the skills those practices test.

**Failure boundary and alternatives.** The numeric scores were never measured in this corpus, so quoting them as findings rather than emphasis fabricates rigor. Bounded alternatives and recoveries: order rows by the source's checklist sequence, replace scores with a deploy-blocking flag, or keep a plain tier without numbers.

**Counterexample, gotchas, and operational comparison.** Single-pressure scenarios pass agents that break under combined pressure, which the source flags as a common weak-test mistake. Good: adopting baseline runs after a skill shipped with unaddressed loopholes. Bad: settling a review by quoting the 88. Borderline: keeping the numbers with an editorial-only caveat.

**Verification, evidence, and uncertainty.** Trace each promoted row to the SKILL.md checklist item or testing-guide phase that mandates it. The source's RED-GREEN-REFACTOR checklist and its three-plus-pressures rule are the documented basis for the promoted rows. Which omitted practice causes the most real deployment failures is unmeasured, so ordering encodes expected cost.

**Second-order consequence.** The source ranks its practices implicitly by what its checklists mandate, and baseline testing heads every one of them.

**Revision decision.** Promote run-the-baseline-first, combine-three-plus-pressures, and negate-each-rationalization-explicitly above the hygiene rows, marked editorial.

**Retained seed evidence.** All three scored rows with their tier labels and failure-prevention targets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| pattern_identifier_stable_key | pattern_score_numeric_value | pattern_tier_adoption_level | pattern_failure_prevention_target |
| --- | ---: | --- | --- |
| `writing_skills_validation_patterns` | 95 | default_adoption_pattern_tier | Source Map First: Load local writing skills material before synthesizing validation patterns recommendations. |
| `writing_skills_validation_patterns` | 91 | default_adoption_pattern_tier | Evidence Boundary Split: Separate local facts, external facts, and inference before giving agent instructions. |
| `writing_skills_validation_patterns` | 88 | default_adoption_pattern_tier | Verification Gate Coupling: Attach each recommendation to at least one command, checklist, or review gate. |

## Idiomatic Thesis Synthesis Statement

**Decision supported.** This section helps decide what single orienting claim should govern how skill documents get validated. The seed thesis counts four local paths and repeats the load-local-first formula instead of the theme's central claim, that a skill is only known to work after an agent was watched failing without it.

**Recommended default and causal basis.** Phrase the thesis as validation equals observed behavior change, with the three evidence labels kept on its clauses. The thesis is the sentence that survives quotation, and a retrieval slogan cannot stop an author from shipping an untested skill.

**Operating conditions and assumptions.** The labels stay attached so the local Iron Law remains distinguishable from ecosystem inference when the thesis is reused. The thesis orients how this reference is used and does not restate the testing procedure the artifact and examples carry.

**Failure boundary and alternatives.** The watched-failure demand overshoots for reference skills the source itself exempts from pressure testing. Bounded alternatives and recoveries: quote the source's core principle verbatim, split the thesis per evidence label, or phrase it as a deployment gate condition.

**Counterexample, gotchas, and operational comparison.** Paraphrases drop the observed-failure clause first, leaving a generic test-your-docs platitude. Good: an author citing the thesis to justify a baseline run before editing. Bad: quoting it as public consensus on documentation testing. Borderline: compressing it for a prompt while keeping the observed-failure clause.

**Verification, evidence, and uncertainty.** Check the local clause against the SKILL.md core principle and confirm the combined clause carries the inference label. The SKILL.md overview states the core principle and the required TDD background this thesis condenses. Whether external instruction-format guides endorse behavioral validation is unknown without retrieval.

**Second-order consequence.** The source's core principle already is a thesis, if you did not watch an agent fail without the skill you do not know it teaches the right thing.

**Revision decision.** Restate the combined inference as no skill counts as validated until an agent failed without it and complied with it under pressure.

**Retained seed evidence.** The three labeled thesis lines with their local, external, and combined-inference structure remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`local_corpus_sourced_fact`: The local row for `writing_skills_validation_patterns` contains 4 source path(s), which should be treated as the first retrieval surface for this theme.
`external_research_sourced_fact`: The external source map provides public documentation, repository, or ecosystem analogues where available.
`combined_evidence_inference_note`: Reliable use of Writing Skills Validation Patterns comes from loading the local corpus first, checking public ecosystem guidance second, and converting both into verification-backed agent decisions.

## Local Corpus Source Map

**Decision supported.** This section helps decide which local file a specific skill-writing or skill-testing question should open first. The seed map lists titles and truncated heading signals but not the division of labor, SKILL.md owns authoring rules and structure while the testing guide owns the pressure-scenario methodology.

**Recommended default and causal basis.** Route what-should-a-skill-contain questions to SKILL.md and how-do-i-prove-it-works questions to testing-skills-with-subagents. A reader with a concrete question needs to know which file answers it, and undifferentiated rows force reading both to find either.

**Operating conditions and assumptions.** Both files remain readable at the mapped paths and their headings still match the recorded signals. The map indexes the two mirrored local sources and does not summarize their content, which later sections synthesize.

**Failure boundary and alternatives.** Heading signals go stale the moment the live tree edits either file, and the map records no snapshot date. Bounded alternatives and recoveries: add rows for the referenced supporting files, record per-file line counts as staleness tripwires, or link the worked example the testing guide cites.

**Counterexample, gotchas, and operational comparison.** The SKILL.md cross-references supporting files like persuasion-principles.md that this map does not row, so coverage looks complete when it is not. Good: opening the testing guide for pressure-type vocabulary. Bad: skimming SKILL.md for scenario design it does not contain. Borderline: answering a frontmatter question from memory with the map cited for the path.

**Verification, evidence, and uncertainty.** Open both files at the mapped paths and confirm the recorded heading signals appear in order. Both files were read in full during this evolution, 655 and 384 lines respectively. Whether the cited examples/CLAUDE_MD_TESTING.md worked example exists in this corpus was not confirmed.

**Second-order consequence.** The pair mirrors code and test suite, SKILL.md is the production rulebook and the testing guide is its verification harness.

**Revision decision.** Annotate each row with its role split, authoring rules and CSO in SKILL.md, scenario design and loophole plugging in the testing guide.

**Retained seed evidence.** All four local source rows with their titles, heading signals, and usage roles remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| local_source_filepath_value | local_source_title_text | local_source_heading_signals | local_source_usage_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/claude-skills-202603/superpowers/writing-skills/SKILL.md | writing-skills | Writing Skills; Overview; What is a Skill?; TDD Mapping for Skills; When to Create a Skill; Skill Types | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/claude-skills-202603/superpowers/writing-skills/testing-skills-with-subagents.md | Testing Skills With Subagents | Testing Skills With Subagents; Overview; When to Use; TDD Mapping for Skill Testing; RED Phase: Baseline Testing (Watch It Fail); GREEN Phase: Write Minimal Skill (Make It Pass) | local agent-usable source material |
| claude-skills/superpowers/writing-skills/SKILL.md | writing-skills | Writing Skills; Overview; What is a Skill?; TDD Mapping for Skills; When to Create a Skill; Skill Types | skill entrypoint or reusable agent prompt |
| claude-skills/superpowers/writing-skills/testing-skills-with-subagents.md | Testing Skills With Subagents | Testing Skills With Subagents; Overview; When to Use; TDD Mapping for Skill Testing; RED Phase: Baseline Testing (Watch It Fail); GREEN Phase: Write Minimal Skill (Make It Pass) | local agent-usable source material |

## External Research Source Map

**Decision supported.** This section helps decide how much weight external rows may carry in skill-validation guidance. The seed map presents the Codex AGENTS.md guide, GitHub Actions docs, and agents.md format as external facts although none was retrieved and none is known to discuss skill validation.

**Recommended default and causal basis.** Treat the URLs as leads for a future refresh pass and rest all current claims on the two local files. An external-fact label promises documentary support, and an unretrieved URL can only supply an analogy to instruction files, not evidence about pressure testing.

**Operating conditions and assumptions.** Each row keeps a role note explaining what question a future retrieval should answer. The map catalogs candidate external analogues for this theme and does not certify their content or freshness.

**Failure boundary and alternatives.** Treating instruction-format guides as authorities on subagent testing would import conventions from a different problem entirely. Bounded alternatives and recoveries: retrieve and date the three URLs in a dedicated pass, replace them with sources about prompt evaluation, or drop the table until retrieval happens.

**Counterexample, gotchas, and operational comparison.** Candidate rows quietly harden into citations when text is reused, unless the unretrieved marker sits inside the row itself. Good: citing agents.md only as a naming analogy with the candidate label. Bad: claiming GitHub Actions documents skill testing. Borderline: using the CI analogy as labeled inference.

**Verification, evidence, and uncertainty.** Confirm no claim in this document cites an external row as fact and that each row carries its unretrieved marker. No external retrieval was performed during this evolution, so the candidate labels reflect the actual evidence state. Whether any of the three URLs mentions behavioral testing of agent instructions is entirely unknown.

**Second-order consequence.** The nearest genuine external analogue is CI itself, a skill baseline run is to documentation what a failing pipeline is to code.

**Revision decision.** Downgrade all three rows to unretrieved candidate analogues and name what each might contribute, instruction-file conventions and CI-style verification models.

**Retained seed evidence.** All three external rows with their names, roles, and boundary labels remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| external_source_url_value | external_source_name_text | external_source_usage_role | evidence_boundary_label_value |
| --- | --- | --- | --- |
| https://developers.openai.com/codex/guides/agents-md | OpenAI Codex AGENTS.md guide | primary agent instruction context model | external_research_sourced_fact |
| https://docs.github.com/actions | GitHub Actions documentation | verification and automation model | external_research_sourced_fact |
| https://agents.md/ | AGENTS.md open format | general agent instruction format | external_research_sourced_fact |

## Anti Pattern Registry Table

**Decision supported.** This section helps decide which recurring skill-authoring failures deserve standing detection rules. The seed registry lists three corpus-hygiene failures and omits the anti-patterns the source itself catalogs, skipping the baseline, single-pressure tests, vague counters, and workflow-summarizing descriptions.

**Recommended default and causal basis.** Screen every new or edited skill against the registry before deployment, treating any hit as a deploy blocker. The source spends whole sections on rationalization tables and common mistakes because those are the failures that actually ship broken skills.

**Operating conditions and assumptions.** Each row pairs a failure with an observable signal a reviewer can check, like a description that narrates process steps. The registry names skill-validation failures with detection signals and does not restate the full testing methodology.

**Failure boundary and alternatives.** An exhaustive import of every source mistake would duplicate the testing guide instead of registering the highest-cost patterns. Bounded alternatives and recoveries: fold detection into the completeness checklist, keep a short top-four registry with links into the source, or auto-check descriptions for process verbs.

**Counterexample, gotchas, and operational comparison.** The workflow-summary trap is subtle, the source documents an agent following a description shortcut instead of reading the skill's flowchart. Good: catching an untested batch of skills before deployment. Bad: a description saying dispatches subagent per task with review between. Borderline: a reference skill deployed on retrieval checks alone with the exemption noted.

**Verification, evidence, and uncertainty.** Replay each registry row against the source section that documents it and confirm the detection signal is observable pre-deployment. The SKILL.md common-rationalizations table and CSO section document these failures with verbatim examples. Relative frequency of each anti-pattern in this team's practice is unmeasured, so row order encodes expected cost.

**Second-order consequence.** The deadliest anti-pattern is meta, believing a skill is obviously clear, which the source counters with a table of exactly such excuses.

**Revision decision.** Add skipping-the-baseline, single-pressure-testing, generic-counters, and description-summarizes-workflow rows with the source's own detection cues.

**Retained seed evidence.** All three original registry rows with their causes, replacements, and detection methods remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| anti_pattern_failure_name | failure_cause_risk_reason | safer_default_replacement_pattern | detection_signal_review_method |
| --- | --- | --- | --- |
| context_free_summary_output | agent skips local corpus and produces generic advice | source_map_first_synthesis | verify every listed local path appears in the generated file |
| unsourced_recommendation_claims | guidance appears authoritative without source boundary | evidence_boundary_split_pattern | check for local, external, and inference labels |
| unverified_agent_instruction | recommendation cannot be checked by command or review gate | verification_gate_coupling | require concrete gate in generated reference |

## Verification Gate Command Set

**Decision supported.** This section helps decide which gates must pass before a skill edit or this reference's guidance is relied on. The seed gate names one repository verifier command while the source's real gates are behavioral, baseline runs, pressure re-tests, and word-count checks no single command captures.

**Recommended default and causal basis.** Run the corpus verifier for structure, wc -w for budget, and require documented baseline and pressure-test results for discipline skills. A skill can pass every text lint and still fail its only meaningful test, an agent complying under pressure.

**Operating conditions and assumptions.** Skill files are reachable for word counts and test transcripts can be attached or linked as evidence. The gate set defines what must pass before skill guidance is trusted and does not implement the subagent harness itself.

**Failure boundary and alternatives.** Behavioral gates cannot be scripted into this corpus's verifier, so the section must distinguish automatable from judgment gates. Bounded alternatives and recoveries: a checklist-only gate for reference skills, a standing pressure-scenario suite rerun on every edit, or reviewer sign-off citing transcript evidence.

**Counterexample, gotchas, and operational comparison.** Green mechanical gates create false confidence precisely because the behavioral gate is the one that catches real failures. Good: an edit blocked because no baseline transcript accompanied it. Bad: deploying on a passing linter alone. Borderline: a typo fix shipped with gates waived and the waiver recorded.

**Verification, evidence, and uncertainty.** Execute the listed commands on a sample skill and confirm the behavioral gate demands transcript evidence rather than assertion. The SKILL.md token-efficiency section prescribes the wc -w check and the deployment checklist mandates test-first evidence. How to standardize pressure-test transcripts as reviewable evidence is unresolved in the source.

**Second-order consequence.** The source already ships one mechanical gate, word count against token budgets, proving behavioral discipline and cheap automation coexist.

**Revision decision.** Keep the repository verifier and add the source's checkable gates, wc -w token budgets, frontmatter field limits, and a recorded baseline-then-compliance test pair.

**Retained seed evidence.** The original verification gate line and its repository verifier command block remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`verification_gate_command_set`: Run the repository verifier after editing this file.

```bash
python3 agents-used-monthly-archive/idiomatic-references-202606/tools/verify_reference_generation.py --stage final
```

## Agent Usage Decision Guide

**Decision supported.** This section helps decide when a working agent should open this reference and which validation path it should take. The seed guide says use this reference when the theme is mentioned, but the real trigger is an act, someone is about to create, edit, or deploy a skill document.

**Recommended default and causal basis.** Open this reference before writing any skill content and select the test approach from the discipline, technique, pattern, or reference type. Validation obligations attach at write time, and a guide keyed to topic mentions fires too late or not at all.

**Operating conditions and assumptions.** The reader can identify their skill's type and has subagent capacity for whichever test style it requires. The guide routes readers into this reference and does not decide the testing depth, which the tradeoff guide owns.

**Failure boundary and alternatives.** Keying to every skill edit would gate trivial typo fixes behind full pressure campaigns the source does not demand. Bounded alternatives and recoveries: a pre-deployment-only trigger for teams that batch reviews, a type-based exemption list, or embedding the trigger in a skill template.

**Counterexample, gotchas, and operational comparison.** Editors assume small edits are exempt, and the source explicitly rejects the just-adding-a-section excuse. Good: consulting the guide before a discipline-skill edit and running the baseline. Bad: opening it only after agents misused a deployed skill. Borderline: a typo fix shipped untested with the exemption recorded.

**Verification, evidence, and uncertainty.** Walk a create, an edit, and a deploy event through the guide and confirm each lands on a concrete test style. The SKILL.md testing-all-skill-types section supplies the four-type matrix this routing applies. Where exactly a cosmetic edit ends and a rule edit begins is a judgment the source leaves open.

**Second-order consequence.** The source binds testing to the edit itself, its Iron Law applies to edits exactly as to new skills, which makes the edit event the natural trigger.

**Revision decision.** Trigger on creating a skill, editing a skill's rules, or preparing deployment, with the source's skill-type matrix choosing the test style.

**Retained seed evidence.** The original usage line and all four guidance bullets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`agent_usage_decision_guide`: Use this reference when a task mentions this theme, one of the listed local source paths, or a nearby technology/workflow surface.

- Start with the local corpus source map.
- Prefer patterns with explicit verification gates.
- Treat external sources as freshness and ecosystem checks, not replacements for local repo conventions.
- Preserve the evidence boundary labels when reusing recommendations.

## User Journey Scenario

**Decision supported.** This section helps decide what end-to-end shape a competent skill-validation session should take. The seed scenario shows a cold reader choosing a reading path and stops before the journey the sources script, baseline, write, pressure-test, plug loopholes, deploy.

**Recommended default and causal basis.** Narrate an author baselining a TDD-adjacent skill, capturing verbatim excuses, and iterating counters until the agent cites the skill under pressure. A journey that ends at reading cannot rehearse the decisions that matter, whether to run the baseline and when to stop refactoring.

**Operating conditions and assumptions.** The reader can dispatch subagents and observe their choices, which the journey treats as available tooling. The scenario dramatizes one representative discipline-skill journey and does not enumerate every authoring path.

**Failure boundary and alternatives.** One linear journey cannot cover all four skill types, whose test styles differ materially. Bounded alternatives and recoveries: a second journey for a reference skill validated by retrieval checks, a failure journey where deployment preceded testing, or the source's worked example cited directly.

**Counterexample, gotchas, and operational comparison.** Journeys written without a real baseline read as tidy fiction, and the source's six-iteration example shows real campaigns loop more than once. Good: a journey ending with a meta-test confirming clarity. Bad: one ending at the skill draft. Borderline: a journey compressing REFACTOR to a single iteration with a note that real counts vary.

**Verification, evidence, and uncertainty.** Check each journey beat against the testing guide's checklist and confirm no phase is skipped. The testing guide's TDD-mapping table and its six-iteration bulletproofing example script exactly this journey. Typical iteration counts to bulletproof beyond the source's single reported campaign are unknown.

**Second-order consequence.** The journey's pivotal moment is emotional, the author watching their obviously clear skill get rationalized around by a real agent.

**Revision decision.** Extend the journey through a baseline run that documents rationalizations, a minimal skill draft, a failed pressure test, a loophole counter, and a bulletproof verdict.

**Retained seed evidence.** The role-based opening, starting state, decision, and trigger lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Role based opening scenario: The reader or documentation author is starting cold and deciding whether the reference answers the next practical question and needs a reference that turns source evidence into an executable next step.
Primary user starting state: The user has a `writing_skills_validation_patterns` task, one or more local source paths, and uncertainty about which pattern should drive implementation.
Decision being made: choosing the reading path, example, diagram, or rewrite pattern that makes action obvious.
Reference opening trigger: Open this file when the task mentions writing skills validation patterns, any mapped local source path, or an adjacent workflow with the same failure mode.

## Decision Tradeoff Guide

**Decision supported.** This section helps decide how much validation depth a given skill deserves and what being wrong costs. The seed guide keys adopt, adapt, and avoid to generic evidence agreement instead of the variables the source uses, skill type, rule-violation incentive, and compliance cost.

**Recommended default and causal basis.** Match test style to skill type using the source's matrix and reserve multi-pressure campaigns for discipline enforcement. Testing depth is the real decision, and the source allocates it by whether agents have any incentive to bypass the skill.

**Operating conditions and assumptions.** The skill's type is identifiable and its compliance cost to agents can be estimated before choosing depth. The guide calibrates validation depth per skill and cannot waive the Iron Law once a rule-bearing skill is being written.

**Failure boundary and alternatives.** Full pressure campaigns on skills with nothing to violate burn subagent time the source explicitly says to save. Bounded alternatives and recoveries: default everything to pressure testing when classification is doubtful, pilot with one scenario before a full campaign, or let a reviewer assign type.

**Counterexample, gotchas, and operational comparison.** Authors misclassify discipline skills as references to dodge pressure testing, which the rationalization table anticipates. Good: pressure-testing a verification-before-completion skill. Bad: retrieval-checking a TDD skill because it is documentation. Borderline: an API reference given one application scenario for its gap risk.

**Verification, evidence, and uncertainty.** Audit recent skills for type-to-test-style match and check misclassifications against later deployment failures. The SKILL.md testing-all-skill-types section and the testing guide's when-to-use list define this allocation. Borderline type assignments remain judgment, and the source offers no tiebreak rule.

**Second-order consequence.** The source prices testing by temptation, the more an agent wants to break a rule the more pressure its test must apply.

**Revision decision.** Rekey adopt to discipline skills under pressure testing, adapt to technique and pattern skills under application scenarios, and avoid to pure reference skills with retrieval checks only.

**Retained seed evidence.** The Adopt when, Adapt when, Avoid when, and Cost of being wrong rows with their verification prompts remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| decision_option_name | when_to_choose_condition | tradeoff_cost_description | verification_question_prompt |
| --- | --- | --- | --- |
| Adopt when | local corpus and external evidence agree on the writing skills validation patterns pattern | fastest path, but can copy stale local assumptions | Does the selected pattern appear in the canonical source and current external evidence? |
| Adapt when | local sources are strong but public ecosystem guidance has changed | preserves repo fit, but requires explicit inference notes | Did the reference label the local fact, external fact, and combined inference separately? |
| Avoid when | source evidence is thin, conflicting, or unrelated to the user journey | prevents false confidence, but may require deeper research | Is there a confidence warning or adjacent reference route? |
| Cost of being wrong | wrong writing skills validation patterns guidance can send an agent to the wrong files, tests, or abstraction | wasted implementation loop and weaker verification | Would a reviewer know what to undo and what to inspect next? |

## Local Corpus Hierarchy

**Decision supported.** This section helps decide which copy and which file a skill-validation question should open first. The seed hierarchy labels the archive SKILL.md canonical, its own testing guide legacy, and both live copies supporting, although each pair is byte-identical and the testing guide is required methodology, not history.

**Recommended default and causal basis.** Cite live-tree copies as working sources with archive rows as dated mirrors, and never rank the testing guide below SKILL.md. A legacy label steers readers away from the file that owns the entire pressure-testing procedure the theme depends on.

**Operating conditions and assumptions.** The mirror relation stays diff-verified and both roles, rulebook and harness, remain represented at the top of the hierarchy. The hierarchy ranks retrieval priority within this corpus and does not decide which tree the repository owner maintains.

**Failure boundary and alternatives.** If either tree is edited alone the identity claim breaks, and the hierarchy gives no signal for which copy then wins. Bounded alternatives and recoveries: hash-pin the pairs to detect forks, ask the owner which tree is authoritative, or collapse to two logical sources with location lists.

**Counterexample, gotchas, and operational comparison.** The live tree changes without archive snapshots keeping pace, so canonicity by recency needs periodic re-verification. Good: one citation naming the live testing guide with its archive mirror noted. Bad: skipping pressure methodology because its row said legacy. Borderline: keeping four rows for discoverability with an explicit duplicate flag.

**Verification, evidence, and uncertainty.** Rerun the pairwise diffs and confirm no citation in this document leans on the legacy label. Diffs during this evolution confirmed both pairs byte-identical, contradicting the seed's role split. Which tree the repository owner regards as the maintained home is their call, so the live-tree preference is provisional.

**Second-order consequence.** Demoting a test suite below its rulebook repeats the exact mistake the theme warns against, treating verification as optional supplement.

**Revision decision.** Rank the pair as co-canonical, SKILL.md for authoring rules and the testing guide for validation methodology, each mirrored across archive and live trees.

**Retained seed evidence.** The classification vocabulary line and all four hierarchy rows with reviewer questions remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Classification vocabulary includes canonical, supporting, legacy, duplicate, and conflicting source roles.

| local_source_filepath_value | corpus_hierarchy_role | heading_signal_to_convert | reviewer_question_to_answer |
| --- | --- | --- | --- |
| agents-used-monthly-archive/claude-skills-202603/superpowers/writing-skills/SKILL.md | canonical primary source | Writing Skills; Overview; What is a Skill? | What guidance, warning, or example should this source contribute to Writing Skills Validation Patterns? |
| agents-used-monthly-archive/claude-skills-202603/superpowers/writing-skills/testing-skills-with-subagents.md | legacy historical source | Testing Skills With Subagents; Overview; When to Use | What guidance, warning, or example should this source contribute to Writing Skills Validation Patterns? |
| claude-skills/superpowers/writing-skills/SKILL.md | supporting context source | Writing Skills; Overview; What is a Skill? | What guidance, warning, or example should this source contribute to Writing Skills Validation Patterns? |
| claude-skills/superpowers/writing-skills/testing-skills-with-subagents.md | supporting context source | Testing Skills With Subagents; Overview; When to Use | What guidance, warning, or example should this source contribute to Writing Skills Validation Patterns? |

## Theme Specific Artifact

**Decision supported.** This section helps decide what concrete evidence object must exist before this reference counts as operational. The seed artifact names a reader promise with before-and-after rewrite while the source's operational artifact is a test campaign record, baseline transcript, rationalization table, and compliance verdict.

**Recommended default and causal basis.** Carry the source's own TDD-skill campaign, six iterations from baseline excuses to a cited-principle compliance, as the reviewable instance. A skill's validation is only auditable through the campaign record, since prose polish proves nothing about agent behavior.

**Operating conditions and assumptions.** The record names its scenario pressures and distinguishes verbatim agent quotes from author paraphrase. The artifact certifies this reference is operational and does not require every historical skill to retro-produce campaign records.

**Failure boundary and alternatives.** A campaign record is overkill for reference skills the source exempts from pressure testing. Bounded alternatives and recoveries: point at the testing guide's CLAUDE_MD_TESTING worked example, synthesize a fresh labeled campaign, or accept a single-scenario record for small skills.

**Counterexample, gotchas, and operational comparison.** Reconstructed records written after deployment look identical to real ones, so provenance notes matter. Good: a record pairing each excuse with its counter section. Bad: a rewrite diff with no behavioral evidence. Borderline: a one-iteration record for a low-stakes technique skill.

**Verification, evidence, and uncertainty.** Check the record shows a failing baseline, a specific counter, and a passing re-test in that order. The testing guide's bulletproofing example documents exactly this record shape across its iterations. Whether borrowed campaign records teach as well as locally produced ones is untested.

**Second-order consequence.** The rationalization table is the campaign's fossil record, each row is a real excuse an agent produced under pressure.

**Revision decision.** Define the artifact as one completed campaign record, pressure scenario text, verbatim baseline rationalizations, the counter added, and the re-test outcome.

**Retained seed evidence.** The artifact definition line and the three artifact field rows with completion rules remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Theme specific artifact: reader promise with before/after rewrite and plain-language acceptance test.

| artifact_field_name | artifact_completion_rule | evidence_source_hint |
| --- | --- | --- |
| user_goal_statement | state the user's concrete goal before applying Writing Skills Validation Patterns | local corpus hierarchy plus critique findings |
| decision_boundary_rule | define the point where this reference should be used or avoided | decision tradeoff guide |
| verification_gate_rule | define the command, checklist, or review question that proves the artifact worked | verification gate command set |

## Worked Example Set

**Decision supported.** This section helps decide which validation behaviors should be taught as exemplary, negligent, or conditionally acceptable. The seed examples restate generic load-canon verdicts and never show actual validation conduct judged, a real baseline honored, a skipped test rationalized, or a partial campaign.

**Recommended default and causal basis.** Grade every example by one question, was agent behavior observed before and after the skill existed. Authors calibrate on instances, and the source teaches through verbatim scenarios and excuse tables rather than abstract verdicts.

**Operating conditions and assumptions.** Each example names its skill type, the test style applied or skipped, and the deployment consequence. The examples grade validation conduct, not the quality of the skills being validated.

**Failure boundary and alternatives.** Examples drawn only from the source's TDD campaign may transfer poorly to pattern or reference skills. Bounded alternatives and recoveries: draw examples from this corpus's own skill folders, add a fourth case for an edit shipped without re-testing, or pair each verdict with its registry row.

**Counterexample, gotchas, and operational comparison.** Polish masquerades as validation, and the source's obviously-clear excuse is precisely how untested skills get justified. Good: six documented iterations ending in cited compliance. Bad: five skills written in one batch and deployed. Borderline: a syntax reference deployed on retrieval checks with the exemption noted.

**Verification, evidence, and uncertainty.** Scan each verdict against the source's checklists and confirm the graded behavior is observable in a transcript or record. The SKILL.md batch-deployment prohibition and the testing guide's campaign example anchor the recast verdicts. Which negligent pattern dominates real practice here is unmeasured, so the chosen cases reflect expected shapes.

**Second-order consequence.** The most instructive bad example is diligent-looking, a beautifully formatted skill whose only missing ingredient is any observed agent behavior.

**Revision decision.** Recast good as a full baseline-to-bulletproof campaign, bad as batch-deploying untested skills, and borderline as a reference skill checked by retrieval only.

**Retained seed evidence.** The good, bad, and borderline example lines with their original verdict framing remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Good example: Use Writing Skills Validation Patterns after loading the canonical source, confirming the external evidence boundary, and writing a verification gate before implementation.
Bad example: Use Writing Skills Validation Patterns as a generic tutorial while ignoring the mapped local paths, source hierarchy, and cost of being wrong.
Borderline case: Use Writing Skills Validation Patterns only after adding a confidence warning when local evidence is thin or conflicts with current ecosystem guidance.

## Outcome Metrics and Feedback Loops

**Decision supported.** This section helps decide which observable signals should trigger revising a skill or this reference. The seed metrics watch whether a reader can apply the reference and never measure validation outcomes, baseline coverage, loophole recurrence, or compliance under re-test.

**Recommended default and causal basis.** Track the share of deployed skills with recorded campaigns and treat any post-deployment rationalization as a metric event. This theme improves outcomes through skills that survive pressure, so its instruments must watch test campaigns, not reading comprehension.

**Operating conditions and assumptions.** Campaign records are kept somewhere queryable and deployment events are distinguishable from drafts. The metrics gauge the validation discipline this reference teaches, not the throughput of skill authoring.

**Failure boundary and alternatives.** Compliance metrics need subagent runs to produce data, which makes them costlier than text metrics and tempting to skip. Bounded alternatives and recoveries: sample audits of deployed skills instead of full coverage, reviewer-graded campaign quality scores, or violation postmortems feeding the registry.

**Counterexample, gotchas, and operational comparison.** Counting campaigns rewards ritual, a campaign with weak single-pressure scenarios inflates the metric while proving little. Good: tightening scenarios after a deployed skill got rationalized in production. Bad: celebrating campaign counts while scenarios stay single-pressure. Borderline: skipping audits in a period with no deployments, noted.

**Verification, evidence, and uncertainty.** Audit recent deployments for campaign records and check each post-deployment violation produced a counter or registry row. The seed's review-cadence line ties re-verification to edits, a loop the compliance metrics extend. Healthy baselines for these rates are unmeasured, so first thresholds are provisional.

**Second-order consequence.** A falling new-rationalization count across iterations is the source's own convergence signal, it defines bulletproof as no new excuses.

**Revision decision.** Adopt baseline-before-writing rate, new-rationalization count per re-test, and post-deployment violation reports as the primary signals.

**Retained seed evidence.** The leading indicator, failure signal, and review cadence lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Leading indicator: a new reader can apply the reference without asking the author for hidden context.
Failure signal: the reference is a literature dump instead of a guided explanation.
Review cadence: Re-run the verifier after every generated-reference edit and refresh external sources when public APIs, docs, or tooling releases change.

## Completeness Checklist

**Decision supported.** This section helps decide when this reference may be declared ready to hand to an agent. The seed checklist confirms generic sections exist and never checks the theme's own obligations, that the validation cycle, pressure vocabulary, and skill-type matrix are all represented.

**Recommended default and causal basis.** Tick structural items with citations, then verify cycle, pressure, and type coverage by grepping this document against the source lists. This document teaches a procedure, so its readiness check must confirm the procedure survives intact, not just that prose sections exist.

**Operating conditions and assumptions.** Each added item names its target section and whether a script or human verifies it. The checklist gates this document's readiness, not the quality of campaigns later run under it.

**Failure boundary and alternatives.** A reference that dropped the REFACTOR phase would still pass the current checklist and teach an incomplete cycle. Bounded alternatives and recoveries: generate coverage items mechanically from the source's checklists, deep-check two random items per review, or pair-review the artifact record.

**Counterexample, gotchas, and operational comparison.** Coverage can pass while descriptions contradict the source, so coverage ticks and fidelity ticks stay separate. Good: a coverage tick citing the line naming all seven pressures. Bad: all ticks green from a headings glance. Borderline: carrying forward last review's matrix tick with a staleness note.

**Verification, evidence, and uncertainty.** List the source's phases, pressures, and types, then grep this document for each and record the misses. The seed's seven structural items map onto real sections here and anchor the added coverage layer. How much fidelity checking each item needs per revision depends on edit volume, so depth stays judgment.

**Second-order consequence.** A checklist for a validation-methodology document is itself a validation artifact and inherits the same failure mode, silently missing steps.

**Revision decision.** Append items requiring all three cycle phases documented, all seven pressure types named, and the four-type test matrix represented.

**Retained seed evidence.** All seven structural checklist items covering scenario, decision guide, hierarchy, artifact, examples, metrics, and routing remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- The role scenario names the user, starting state, decision, and trigger for Writing Skills Validation Patterns.
- The decision guide includes Adopt when, Adapt when, Avoid when, and Cost of being wrong.
- The local corpus hierarchy identifies canonical and supporting sources or gives a confidence warning.
- The theme specific artifact is concrete enough to review without reading every mapped source.
- The examples cover good, bad, and borderline usage.
- The metrics section names one leading indicator and one failure signal.
- The adjacent routing section points to a better reference when this one is not the right fit.

## Adjacent Reference Routing

**Decision supported.** This section helps decide when a question should leave this reference and which neighbor owns it. The seed routing splits the theme name into writing, skills, and validation keywords aimed at unnamed destinations instead of routing by question type to real corpus neighbors.

**Recommended default and causal basis.** Keep skill-content and test-design questions here, send campaign-state questions to the journal reference and dispatch mechanics to the subagent reference. Readers leave this reference with distinct needs, checkpointing long campaigns, decomposing multi-skill work, and each need has an evolved neighbor in this corpus.

**Operating conditions and assumptions.** Each route names its trigger, a destination resolving to a real file, and what stays here. Routing redirects within this corpus and cannot authorize work in a destination's domain.

**Failure boundary and alternatives.** Keyword routes point at references that exist only as words, stranding the reader who follows them. Bounded alternatives and recoveries: consult the corpus index before adding routes, keep unresolved needs here with a gap note, or escalate genuine overlap to the user.

**Counterexample, gotchas, and operational comparison.** Test-dispatch questions masquerade as validation questions, and over-eager routing scatters a reader who needed one scenario template. Good: sending a campaign-checkpoint question to the journal schema reference. Bad: routing to the writing adjacent reference, a keyword with no file. Borderline: answering a small dispatch question inline with a route noted for depth.

**Verification, evidence, and uncertainty.** Resolve each named destination to an existing corpus file and walk one sample question through each trigger. Both named neighbors were evolved earlier in this same Alpha lane and are verified resolvable destinations. The best split between answering inline and routing away depends on question depth, so borderline calls stay recorded judgment.

**Second-order consequence.** This theme consumes its neighbors, a long bulletproofing campaign needs the journal schema for checkpoints and the subagent patterns for dispatching test runs.

**Revision decision.** Route journal-and-checkpoint questions to the tdd progress journal schema reference and subagent-orchestration questions to the subagent development execution patterns reference.

**Retained seed evidence.** The adjacency guidance line and the three keyword-derived route stubs remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Adjacent reference guidance: Use visual, ASCII, HTML, or writing references when the output medium is fixed.
Adjacent reference 1: consider the writing adjacent reference when the current task pivots away from writing skills validation patterns.
Adjacent reference 2: consider the skills adjacent reference when the current task pivots away from writing skills validation patterns.
Adjacent reference 3: consider the validation adjacent reference when the current task pivots away from writing skills validation patterns.

## Workload Model

**Decision supported.** This section helps decide how much validation work one skill may consume before escalation or acceptance. The seed model caps work at twelve source documents and one checklist per reference use, while validation workload is really bounded by scenarios per campaign and iterations to bulletproof.

**Recommended default and causal basis.** Plan one focused campaign per skill with a handful of scenarios and expect several refactor iterations before bulletproof. The costly unit here is a subagent test run, and a model blind to run counts cannot budget the thing that actually consumes effort.

**Operating conditions and assumptions.** Subagent runs are cheap enough to iterate and campaign state is checkpointed between sessions. The model bounds validation effort per skill and does not bound the size of the skills being written.

**Failure boundary and alternatives.** Iteration counts vary by skill, the source's own campaign took six cycles, so any fixed cap will sometimes truncate a campaign early. Bounded alternatives and recoveries: time-boxed campaigns with explicit incompleteness notes, shared scenario suites amortized across similar skills, or reviewer-set iteration budgets.

**Counterexample, gotchas, and operational comparison.** The STOP rule forbids batching, moving to the next skill before the current one is verified is the exact overload the source names. Good: a campaign closed after a clean re-test with zero new excuses. Bad: five skills validated in one interleaved batch. Borderline: a campaign paused at iteration three with state journaled for resumption.

**Verification, evidence, and uncertainty.** Count scenarios and iterations in recorded campaigns and test whether truncated campaigns produced more post-deployment violations. The SKILL.md STOP section and the six-iteration example define the per-skill campaign shape this model adopts. Typical iteration distributions across skill types are unmeasured, so the several-iterations expectation is a defensible default.

**Second-order consequence.** The source replaces effort caps with a convergence condition, you are done when the excuses stop, which is a budget expressed as evidence.

**Revision decision.** Rebound the model around one skill per campaign, three-plus pressures per scenario, and iterations continued until a re-test yields no new rationalization.

**Retained seed evidence.** The four workload dimensions with their boundary values and verification pressure points remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`combined_evidence_inference_note`: Treat Writing Skills Validation Patterns as a documentation reference operating reference, not as a prose summary.

| workload_dimension_name | workload_boundary_value | verification_pressure_point |
| --- | --- | --- |
| primary_usage_surface | reference selection, writing, roadmap, or explanation work where the output should improve the next human or agent decision | verify that the reference changes the next implementation or review action |
| bounded_capacity_model | one audience, one decision, up to 12 source documents, and one verification checklist per reference use | split the task or create a narrower reference when this boundary is exceeded |
| source_pressure_model | local heading signals include Writing Skills; Overview; What is a Skill?; TDD Mapping for Skills; When to Create a Skill; Skill Types; Testing Skills With Subagents; Overview; When | compare guidance against canonical local sources before following external examples |
| artifact_pressure_model | required artifact is reader promise with before/after rewrite and plain-language acceptance test | require the artifact before claiming the reference is operationally usable |

## Reliability Target

**Decision supported.** This section helps decide what measurable reliability this reference must demonstrate before its guidance is trusted. The seed table demands perfect boundary preservation and an 18-of-20 decision sample with no sampling procedure, and omits the theme's own reliability notion, compliance under maximum pressure.

**Recommended default and causal basis.** Keep the four dimensions with methods attached and lead with periodic pressure re-tests of deployed skills. The source defines bulletproof operationally, correct choice, cited sections, acknowledged temptation, and that definition is testable where the seed's percentages are not.

**Operating conditions and assumptions.** Each target names its metric, sampling method, population, owner, and the corrective action a miss triggers. The targets judge this reference and the validation discipline, not the reliability of the software the skills govern.

**Failure boundary and alternatives.** Quoting the unmeasured percentages as achieved performance manufactures rigor this corpus never earned. Bounded alternatives and recoveries: binary pass-fail compliance audits, pooled sampling across the corpus's skill themes, or postmortems on every violation instead of rates.

**Counterexample, gotchas, and operational comparison.** Re-tests with the original scenarios measure memorized compliance, so samples need at least one fresh scenario variant. Good: three sampled skills re-passing under fresh pressure, logged. Bad: reporting the 18-of-20 nobody sampled. Borderline: a re-test with recycled scenarios recorded with that caveat.

**Verification, evidence, and uncertainty.** Run one fresh-scenario re-test per review cycle and audit the evidence labels on a text sample. The testing guide's bulletproof criteria give the operational definition the added target measures. No baseline exists for any threshold here, so the first measured cycle defines what is achievable.

**Second-order consequence.** Compliance is cheap to spot-check, one scenario and one subagent per sampled skill, which makes this theme unusually auditable.

**Revision decision.** Add a bulletproof-rate target, sampled deployed skills re-tested under maximum pressure, with every threshold marked unbaselined and owned.

**Retained seed evidence.** All four reliability rows with their threshold values and evidence-collection methods remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| reliability_target_name | measurable_threshold_value | evidence_collection_method |
| --- | --- | --- |
| source_boundary_preservation | 100 percent of recommendations keep local, external, and inference boundaries visible | review generated text for the three evidence labels before reuse |
| decision_accuracy_sample | at least 18 of 20 sampled uses route to the correct adopt, adapt, avoid, or adjacent-reference decision | sample downstream tasks and record reviewer verdicts |
| unsupported_claim_rate | zero unsupported production, security, latency, or reliability claims in final guidance | reject claims without source row, explicit inference note, or verification method |
| recovery_path_clarity | every avoid or failure case names the rollback, escalation, or next-reference route | inspect failure-mode and adjacent-routing sections together |

## Failure Mode Table

**Decision supported.** This section helps decide which failures in the validation fabric deserve standing mitigations. The seed table carries hygiene rows and omits how validation itself fails, baselines skipped, pressure tests gone stale as models change, loopholes reopened by edits, and descriptions hijacking behavior.

**Recommended default and causal basis.** Detect skipped baselines by demanding transcripts at review and reopened loopholes by re-running the campaign's scenarios after every rule edit. Triage during a bad deployment needs rows describing how skill validation decays, ranked by how silently each failure ships.

**Operating conditions and assumptions.** Each row names its trigger, earliest observable signal, blast radius, containment, and correction. The table covers validation-process failures, while failures of the underlying engineering discipline belong to the skills themselves.

**Failure boundary and alternatives.** Rows are worthless if their earliest signal fires only after agents have already misapplied a deployed skill. Bounded alternatives and recoveries: wire scenario re-runs into the edit workflow, audit deployed skills on a sampled cadence, or require registry review in the deployment checklist.

**Counterexample, gotchas, and operational comparison.** The description shortcut is documented in the source, an agent followed a workflow-summarizing description and skipped the skill body entirely. Good: a re-run catching a loophole an edit reopened. Bad: a production violation revealing the baseline never ran. Borderline: a knowingly stale campaign flagged during a model upgrade and re-run after.

**Verification, evidence, and uncertainty.** Seed one failure per row in a drill and confirm the named signal fires before a simulated deployment would ship the bad skill. The SKILL.md CSO section documents the description-shortcut failure with its before-and-after fix. Observed frequency of each failure in this team's history is unmeasured, so ordering encodes expected silence.

**Second-order consequence.** Every one of these failures is silent at deployment time and loud only in production, which is exactly why the source front-loads testing.

**Revision decision.** Add skipped-baseline, stale-pressure-results, edit-reopened-loophole, and description-shortcut rows with pre-deployment detection signals.

**Retained seed evidence.** All four seed failure rows with their triggers and mitigation actions remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| failure_mode_name | likely_trigger_condition | required_mitigation_action |
| --- | --- | --- |
| source drift hides truth | external or local guidance changes after the reference was written | refresh public evidence, rerun local corpus gate, and mark stale claims before reuse |
| generic advice escapes review | agent copies plausible best practices without theme-specific verification | block completion until the verification gate names concrete command, reviewer question, or metric |
| decision path remains implicit | reader cannot tell when to adopt, adapt, or avoid the pattern | add decision table, cost of being wrong, and adjacent-reference route |
| large corpus becomes list | many sources are indexed but not synthesized into ranked guidance | classify canonical, supporting, legacy, duplicate, and conflicting sources |

## Retry Backpressure Guidance

**Decision supported.** This section helps decide when a failing validation cycle should be retried, redirected to meta-testing, or escalated. The seed bullets classify verification failures generically and never define this theme's retry semantics, what to do when an agent keeps finding new rationalizations or a scenario keeps failing to apply pressure.

**Recommended default and causal basis.** Continue refactor cycles while new-excuse counts fall, meta-test on stagnation, and escalate to redesign when meta-testing says the skill was clear but ignored. A bulletproofing loop without a stop rule can iterate forever, and the source's meta-testing move exists exactly for the stuck case.

**Operating conditions and assumptions.** Iteration outcomes are recorded per cycle so stagnation is detectable rather than felt. This governs retries of validation iterations, not retries of the tests and builds inside the skills being validated.

**Failure boundary and alternatives.** Halting too early ships a leaky skill, while unlimited iteration burns subagent budget on a skill that may need redesign. Bounded alternatives and recoveries: escalate to a human reviewer after a fixed cycle budget, split an overloaded skill into narrower ones, or strengthen the foundational principle before another cycle.

**Counterexample, gotchas, and operational comparison.** The tempting failure is softening the scenario until the agent passes, which converts a loud failure into a silent one. Good: meta-testing after the spirit-not-letter excuse survived twice. Bad: weakening pressures until compliance appears. Borderline: one extra cycle past stagnation, labeled, then escalation.

**Verification, evidence, and uncertainty.** Audit stalled campaigns for whether meta-testing preceded escalation and whether scenario pressure was held constant across cycles. The testing guide's meta-testing section defines the stuck-case procedure and its three diagnostic responses. How often campaigns stagnate in practice is unmeasured, and the two-counter stagnation trigger is a defensible default.

**Second-order consequence.** The source treats a persistent violation as diagnostic, meta-testing asks the agent itself how the skill should have been written.

**Revision decision.** Add campaign semantics, iterate while each cycle closes at least one loophole, and switch to meta-testing when the same rationalization survives two counters.

**Retained seed evidence.** All five retry and backpressure bullets, including the one-owner-per-file rule, remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- Retry only after the failed verification signal is classified as transient, stale evidence, missing context, or true contradiction.
- Use one bounded retry for stale external evidence refresh, then escalate to a human or a narrower source-specific reference.
- Apply backpressure by stopping new generation or implementation work when source coverage, critique coverage, or verification gates are red.
- For long-running agent workflows, checkpoint after each batch and re-read the current spec before any broad rewrite, commit, push, or destructive operation.
- For distributed execution, assign one owner per generated file or theme batch and require merge-time verification of exact path, heading, and evidence-boundary invariants.

## Observability Checklist

**Decision supported.** This section helps decide what evidence must exist that a validation campaign actually happened as claimed. The seed bullets recycle source-loading and latency records and never name this theme's evidence stream, campaign transcripts, verbatim rationalization capture, and per-iteration outcomes.

**Recommended default and causal basis.** Record per iteration the scenario, the agent's choice, its verbatim reasoning, and the resulting skill change. In this theme the transcript is the telemetry, since every claim about a skill's strength rests on what agents actually said under pressure.

**Operating conditions and assumptions.** Test runs produce inspectable transcripts and campaign records link each excuse to the counter it produced. This covers observing validation campaigns, while the skills' own runtime behavior is observed by their operational contexts.

**Failure boundary and alternatives.** Full transcript retention for every cycle can outgrow the skills themselves, so retention needs summarization rules. Bounded alternatives and recoveries: retain only excuse tables plus verdicts instead of full transcripts, sample-audit recorded campaigns, or accept commit history as a secondary trace.

**Counterexample, gotchas, and operational comparison.** Paraphrased excuses drift toward what the author expected to hear, corrupting the table that future counters depend on. Good: an excuse table whose rows quote the transcript exactly. Bad: a campaign record saying agent resisted at first, no quotes. Borderline: summarized transcripts kept with pointers to the full runs.

**Verification, evidence, and uncertainty.** Spot-check recorded excuses against their transcripts and confirm each skill counter cites the excuse it answers. The testing guide mandates documenting choices and rationalizations word-for-word during the baseline phase. The retention horizon for full transcripts is untuned, so the summarize-after-close rule is provisional.

**Second-order consequence.** Verbatim capture is load-bearing, the source builds rationalization tables from exact wording because paraphrase loses the loophole.

**Revision decision.** Recenter the checklist on campaign evidence, scenario text and pressures used, verbatim excuses, counters added, and re-test verdicts per iteration.

**Retained seed evidence.** All six observability bullets including the small-audit-evidence preference remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- Record which local sources were loaded and which were intentionally skipped.
- Record the exact verification command, reviewer question, or rendered artifact used as proof.
- Record p50/p95/p99 latency or reviewer-time measurements when the reference affects runtime or workflow speed.
- Capture reviewer decision, unresolved uncertainty, and next refresh trigger.
- Record leading indicator and failure signal from this file in the coverage manifest or journal when the reference drives real work.
- Keep audit evidence small enough to review: command output summary, changed-file list, and unresolved-risk notes are preferred over raw transcript dumps.

## Performance Verification Method

**Decision supported.** This section helps decide how to prove validation effort is buying more than it costs. The seed method demands a ten-minute reader comprehension check and latency packets, while this theme's performance is campaign cost against violation cost avoided, plus the token budget skills must respect.

**Recommended default and causal basis.** Log campaign cost and caught-loophole counts per skill and check each shipped skill against its word-count target. Validation earns its cost by preventing production rationalizations, so verification must compare campaign effort against the failures it catches.

**Operating conditions and assumptions.** Campaign records include effort notes and skill word counts are measured at deployment. This evaluates the validation discipline's cost and benefit, not the runtime performance of systems the skills touch.

**Failure boundary and alternatives.** The comparison needs violation data that only accumulates after deployments, making early ratios unstable. Bounded alternatives and recoveries: compare violation rates between tested and grandfathered untested skills, use reviewer judgment as interim evidence, or track only the mechanical word-count metric at first.

**Counterexample, gotchas, and operational comparison.** Loopholes caught is inflatable by weak baselines that fail on everything, so the count needs scenario quality alongside it. Good: a campaign whose six iterations caught four loopholes before deployment. Bad: quoting reader-minutes for a behavioral discipline. Borderline: an early ratio published with a sample-of-one caveat.

**Verification, evidence, and uncertainty.** Collect cost and catch counts across several campaigns and publish the ratio with its sample size. The SKILL.md token-efficiency section sets the word-count targets and the fifteen-minutes-saves-hours claim frames the cost argument. The source's testing-saves-hours ratio is asserted, not measured here, so it stays labeled as source claim.

**Second-order consequence.** The source's token-efficiency targets are genuine performance limits, a frequently loaded skill pays its word count in every conversation.

**Revision decision.** Measure subagent runs and author hours per campaign, loopholes caught pre-deployment, and wc -w budgets on the resulting skills.

**Retained seed evidence.** The performance method line, both indicator lines, the measurement packet, and the pass and fail conditions remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Performance method: require the reader to find the correct next action in 10 minutes or less during review sampling.
Leading indicator to measure: a new reader can apply the reference without asking the author for hidden context.
Failure signal to watch: the reference is a literature dump instead of a guided explanation.
Required measurement packet: capture input size, source count, tool-call count, wall-clock time, p50/p95/p99 latency where runtime applies, and reviewer decision time where documentation applies.
Pass condition: the reference must let a reviewer identify the correct next action, verification gate, and stop condition without reading unrelated files.
Fail condition: the reference encourages implementation before the workload, reliability target, and failure-mode table are explicit.

## Scale Boundary Statement

**Decision supported.** This section helps decide at what scale per-skill campaigns stop sufficing and what structure replaces them. The seed statement recites multi-system and SLO limits and misses this theme's scale walls, campaigns that outgrow one author, skill libraries too large to re-test on every model change, and shared scenarios drifting apart.

**Recommended default and causal basis.** Re-test fully while the library is small, switch to risk-ranked sampling as it grows, and re-baseline discipline skills after major model changes. Validation scales by re-testing, and re-test cost grows with library size times model churn, a product the seed never mentions.

**Operating conditions and assumptions.** Skills carry type and risk labels so sampling can rank them, and campaign ownership is unambiguous. The boundaries bound the validation discipline, not the number of skills a team may write.

**Failure boundary and alternatives.** Beyond some library size, full re-validation on every change is unaffordable and sampling becomes the only honest option. Bounded alternatives and recoveries: rolling re-validation quotas per review period, shared scenario suites amortized across similar skills, or freezing rarely used skills with staleness banners.

**Counterexample, gotchas, and operational comparison.** Model upgrades silently invalidate old compliance results, a staleness source with no equivalent in code testing. Good: risk-ranked sampling re-testing discipline skills first after an upgrade. Bad: assuming last year's compliance holds for a new model. Borderline: freezing a rarely loaded skill with its staleness noted.

**Verification, evidence, and uncertainty.** Measure re-test coverage against library size over time and confirm sampled skills show no higher violation rates than fully tested ones. The SKILL.md STOP-before-next-skill section supplies the serialization rule this boundary generalizes. The library size where sampling must begin is unmeasured, so the boundary stays a monitored judgment.

**Second-order consequence.** The source's one-skill-at-a-time STOP rule is itself a scale boundary, serializing campaigns so verification debt cannot pile up unseen.

**Revision decision.** Add library-scale signals, sampled re-testing once full coverage is unaffordable, scenario suites versioned and shared, and one owner per campaign.

**Retained seed evidence.** All four scale boundary statements including the distributed split and context-drift rules remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Writing Skills Validation Patterns stops being sufficient when the task spans multiple independent systems, more than one ownership boundary, unbounded source discovery, or production traffic without an explicit SLO.
Under distributed execution, split work by theme file and preserve one verification owner per split; do not let parallel agents rewrite the same reference without a merge checkpoint.
Under long-running agent workflows, treat context drift as a reliability failure: checkpoint state, summarize open risks, and verify against the spec before continuing.
Under large-codebase scale, require dependency or source-graph narrowing before applying this reference; a source list without ranked canonical guidance is not enough.

## Future Refresh Search Queries

**Decision supported.** This section helps decide which future searches would genuinely refresh this reference's external evidence. The seed query table drops the internal theme name into three templates whose literal phrasing targets a coinage no external author uses.

**Recommended default and causal basis.** Search for prompt-evaluation and instruction-compliance testing practice on a periodic trigger, feeding the external map and thesis. Useful refresh queries speak the ecosystem's vocabulary, prompt evaluation, agent instruction testing, LLM behavioral red-teaming, not this corpus's file-naming scheme.

**Operating conditions and assumptions.** Each query names its target section, source type, and firing trigger. The queries refresh external analogues for this theme, while the local methodology changes only through repository edits.

**Failure boundary and alternatives.** Empty results from a coinage query logged as freshness confirmed convert search blindness into false confidence. Bounded alternatives and recoveries: follow the agents.md changelog directly, track evaluation-framework release notes, or drive refresh from dated retrieval records.

**Counterexample, gotchas, and operational comparison.** The evaluation space is noisy with benchmark marketing, so result screening matters more here than in framework themes. Good: a query on pressure-testing agent instructions feeding the external map. Bad: searching the literal theme title and logging zero hits as freshness. Borderline: adopting a well-argued practitioner post with an inference label pending corroboration.

**Verification, evidence, and uncertainty.** Run each query once, grade the top results for on-topic value, and rewrite phrasings that return mostly noise. The seed's three-row structure targeting docs, repositories, and release notes is sound scaffolding for the revised vocabulary. Which phrasings will track this vocabulary is unknowable in advance, so the queries need their own review cadence.

**Second-order consequence.** This theme borders the fast-moving evaluation space, so its external landscape shifts faster than the stable local methodology.

**Revision decision.** Rephrase toward ecosystem vocabulary, agent prompt evaluation frameworks, pressure-testing LLM instructions, and AGENTS.md convention updates, each tied to the section it refreshes.

**Retained seed evidence.** All three labeled query rows with their official-docs, repository, and release-notes targets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| search_query_label_name | search_query_text_value |
| --- | --- |
| `official_docs_query_phrase` | writing skills validation patterns official documentation best practices |
| `github_repository_query_phrase` | writing skills validation patterns GitHub repository examples |
| `release_notes_query_phrase` | writing skills validation patterns changelog release notes migration |

## Evidence Boundary Notes

**Decision supported.** This section helps decide how statements in this reference must be labeled so readers know what each claim rests on. The seed notes define the three labels but ignore this file's specific hazards, doubly mirrored local sources that could quadruple-count and external rows that are unretrieved analogues.

**Recommended default and causal basis.** Label per claim, cite each mirror pair as one source, and mark URL-derived material as inference pending retrieval. Downstream confidence calibrates on these labels, and an analogue labeled external fact claims documentary support no retrieval ever gave.

**Operating conditions and assumptions.** Labels stay stable corpus-wide and every combined-inference clause names the local and external inputs it merges. The notes govern labeling in this reference and its reuses, not the ranking of sources, which the hierarchy owns.

**Failure boundary and alternatives.** Labels applied per section rather than per claim let one labeled sentence launder its unlabeled neighbors. Bounded alternatives and recoveries: introduce an explicit analogue-inspiration tag, inline labels parenthetically on key claims, or index claims to labels during verification.

**Counterexample, gotchas, and operational comparison.** Packet and prompt reuse strips labels mechanically, so load-bearing claims need labels embedded in their own sentences. Good: the Iron Law cited as local fact from SKILL.md with the mirror noted. Bad: pressure-testing presented as AGENTS.md-endorsed practice. Borderline: the CI analogy labeled inference until a retrieval dates it.

**Verification, evidence, and uncertainty.** Sample load-bearing claims, confirm correct labels, and verify no external-fact label exists without a recorded retrieval. The three seed definitions match the corpus-wide label vocabulary and the boundary-preservation target elsewhere in this file. Label durability through packet reuse and prompt quotation is unaudited, so leakage risk remains an assumption.

**Second-order consequence.** One more hazard is internal, the source's own unmeasured claims, like testing saves hours, need a source-asserted tier distinct from corpus-verified fact.

**Revision decision.** Add rules counting each mirrored pair as one local source and requiring analogue-derived external claims to carry an inference downgrade until a dated retrieval.

**Retained seed evidence.** All three label definitions, local fact, external fact, and combined inference, remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- `local_corpus_sourced_fact`: statements tied directly to the local source paths above.
- `external_research_sourced_fact`: statements tied to the public URLs above.
- `combined_evidence_inference_note`: synthesis that combines local and public evidence into agent guidance.
