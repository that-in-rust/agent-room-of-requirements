# Planning Execution Workflow Patterns

**Decision supported.** This section helps decide which process weight a piece of work deserves and how its plan should be written and executed. The seed title names the theme without its two governing rules, classify work before loading process, and write plans so a zero-context engineer can execute them in reviewed batches.

**Recommended default and causal basis.** Classify incoming work through the decision tree, run the matched flow, and for plan-driven work write bite-sized tasks and execute them three at a time with review between batches. A01 opens with not all work deserves the same process, and writing-plans demands plans assuming the engineer has zero context for the codebase and questionable taste.

**Operating conditions and assumptions.** Work arrives classifiable and plan-driven work has a human partner available at checkpoints. This reference operationalizes A01's four-flow classifier and the writing-plans and executing-plans skill pair, not project-management methodology at large.

**Failure boundary and alternatives.** The doctrine splits across two layers that can be misapplied, A01 governs which process to run while the skill pair governs how a chosen plan is written and executed. Bounded alternatives and recoveries: single uniform process for all work, or plan-free direct execution for work below the multi-step threshold.

**Counterexample, gotchas, and operational comparison.** The tempting failure is loading Feature process onto a Bug, A01 warns over-process wastes time and under-process builds the wrong thing. Good: a broken test routed to Bug flow with a regression test in hours. Bad: a bug fix opened with a PRD cycle. Borderline: an enhancement that keeps discovering new rails, A01's rule of thumb escalates it to Feature flow.

**Verification, evidence, and uncertainty.** Confirm sessions under this reference recorded a classification before process was loaded and plans carried bite-sized steps. A01's classifier and both skill overviews state every element promoted here. How the four time budgets transfer to this repository's documentation-heavy work is unmeasured.

**Second-order consequence.** The two layers share one premise, process is a cost to be justified, A01 buys the lightest safe flow while the skills buy reviewer checkpoints only at batch boundaries instead of every step.

**Revision decision.** Open with the classify-first rule, the four flows with their time scales, and the plan-then-batch-execute contract the skills add beneath Feature and Product work.

**Retained seed evidence.** The exact theme title and its workflow-patterns framing remain unchanged. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

## Source Evidence Mapping Table

**Decision supported.** This section helps decide which recorded source may back which claim about planning and execution workflow. The seed map lists six local rows without their real structure, one classifier document with a mermaid rewrite draft, and one skill pair whose archive and live copies are byte-identical.

**Recommended default and causal basis.** Cite A01 for classification claims, the skill pair for plan-writing and execution claims, and the draft only for the expanded Feature-flow stages it uniquely retains. Claims trace to three distinct texts, not six, A01 plus two skills, and the draft differs from A01 mainly by rendering flows as mermaid diagrams instead of ASCII.

**Operating conditions and assumptions.** The live copies stay identical to their archive snapshots, divergence would make the live copies authoritative. The table records provenance for this document's claims and does not rank workflow literature outside the archive.

**Failure boundary and alternatives.** The rewrite draft is a dated backup from 20260514, citing it as an independent source would double-count the classifier doctrine. Bounded alternatives and recoveries: collapse the map to three evidence units with alias notes, or diff the copies each cycle to catch divergence.

**Counterexample, gotchas, and operational comparison.** Citing archive and live skill copies together for one claim reads like corroboration while adding nothing. Good: citing writing-plans for the bite-sized step rule. Bad: citing the rewrite draft as independent confirmation of the classifier. Borderline: citing the draft's PRDv3 staging, real detail but from a dated backup.

**Verification, evidence, and uncertainty.** Confirm every claim traces to one of the three evidence units and the skill-copy identity checks are recorded. All six mapped files were read in full and the two skill pairs compared byte-identical during this evolution. Why the mermaid draft was reverted to ASCII in live A01 is unrecorded.

**Second-order consequence.** The draft's Feature flow is actually richer than A01's, it shows PRDv1 through v3 and ARCHv1 through v3 with an anti-pattern filter step, so the backup preserves detail the live document compressed.

**Revision decision.** Mark all six paths read in full, group them into three evidence units, and note the draft's mermaid rendering as the only substantive divergence from A01.

**Retained seed evidence.** All source rows with their category, confidence, and synthesis-role columns remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| source_location_path_key | source_category_artifact_type | source_authority_confidence_level | source_usage_synthesis_role |
| --- | --- | --- | --- |
| A01-LLM-Workflow01.md | local_corpus_source_material | local_corpus_sourced_fact | local agent-usable source material |
| agents-used-monthly-archive/claude-skills-202603/superpowers/executing-plans/SKILL.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/claude-skills-202603/superpowers/writing-plans/SKILL.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/rewrite-backups-20260514/A01-LLM-Workflow01.rewrite-draft.md | local_corpus_source_material | local_corpus_sourced_fact | local agent-usable source material |
| claude-skills/superpowers/executing-plans/SKILL.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt |
| claude-skills/superpowers/writing-plans/SKILL.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt |
| https://docs.github.com/actions | external_research_source_material | external_research_sourced_fact | primary automation and CI/CD workflow documentation |
| https://docs.github.com/en/actions/concepts/workflows-and-actions/reusing-workflow-configurations | external_research_source_material | external_research_sourced_fact | primary guidance for reusable workflow composition |
| https://github.com/openai/codex/blob/-/AGENTS.md | external_research_source_material | external_research_sourced_fact | agent project instructions and testing guidance in a real repository |

## Pattern Scoreboard Ranking Table

**Decision supported.** This section helps decide which workflow rules deserve default adoption when planning and executing multi-step work. The seed scoreboard scores corpus hygiene while the corpus's load-bearing rules go unranked, classify before loading process, exact paths and complete code in plans, batch execution with review checkpoints, and stop-and-ask over guessing.

**Recommended default and causal basis.** Apply all four rules on every multi-step task, with classification always first. Each rule guards a distinct failure, misclassification wastes process, vague plans stall executors, unreviewed execution compounds errors, and forced-through blockers corrupt work.

**Operating conditions and assumptions.** Each promoted rule keeps its falsifiable phrasing so a reviewer can point at the violation. The scoreboard ranks workflow-discipline rules for adoption priority and does not rank the four flows against each other.

**Failure boundary and alternatives.** The seed's numeric scores were never measured and neither layer offers an internal ranking beyond its own ordering. Bounded alternatives and recoveries: order the rules by observed violation frequency once measured, or rank by blast radius with misclassification widest.

**Counterexample, gotchas, and operational comparison.** The stop-and-ask rule is the one agents shave under momentum, executing-plans lists four stop triggers and orders clarification over guessing at each. Good: a session record showing classification, a pathed plan, batch reports, and one clean stop. Bad: an unclassified task run under an improvised plan. Borderline: batch size stretched to five for trivial tasks, against the default but not the letter.

**Verification, evidence, and uncertainty.** Trace each promoted rule to its stated section in A01 or the skill pair. A01's classifier, writing-plans' remember list, and executing-plans' process and stop sections state each promoted rule. Which rule violations occur most often in real sessions is unmeasured.

**Second-order consequence.** The four rules span the work's whole lifecycle, routing, specification, execution, and exception handling, so they fail independently and a session can score three of four while still corrupting output through the fourth.

**Revision decision.** Promote a top tier of four rules, classify work type first, write plans with exact file paths and complete code, execute in default batches of three with reports between, and stop immediately at blockers rather than guessing.

**Retained seed evidence.** All scored rows with their tier labels and failure-prevention targets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| pattern_identifier_stable_key | pattern_score_numeric_value | pattern_tier_adoption_level | pattern_failure_prevention_target |
| --- | ---: | --- | --- |
| `planning_execution_workflow_patterns` | 95 | default_adoption_pattern_tier | Source Map First: Load local planning execution material before synthesizing workflow patterns recommendations. |
| `planning_execution_workflow_patterns` | 91 | default_adoption_pattern_tier | Evidence Boundary Split: Separate local facts, external facts, and inference before giving agent instructions. |
| `planning_execution_workflow_patterns` | 88 | default_adoption_pattern_tier | Verification Gate Coupling: Attach each recommendation to at least one command, checklist, or review gate. |

## Idiomatic Thesis Synthesis Statement

**Decision supported.** This section helps decide what single orienting claim should govern planning and execution judgments. The seed thesis repeats the load-local-first formula instead of the corpus's claim, that work should be routed to the lightest safe process and plan-driven work executed from zero-context plans in reviewed batches.

**Recommended default and causal basis.** Phrase the thesis as lightest-safe-process routing with zero-context batch execution, with the three evidence labels kept on its clauses. A01 closes on minimum viable process with maximum confidence, and the skill pair operationalizes exactly that confidence for the plan-driven flows.

**Operating conditions and assumptions.** The labels stay attached so classifier-derived clauses remain distinguishable from skill-derived ones. The thesis orients use of this reference and does not compress the per-flow rules it stands on.

**Failure boundary and alternatives.** A thesis built on either layer alone misses the coupling, classification decides whether the plan-execution machinery is even warranted. Bounded alternatives and recoveries: quote A01's closing couplet as the thesis, or phrase it as the four-flow router plus the plan-execute contract.

**Counterexample, gotchas, and operational comparison.** Paraphrases keep lightest process and drop protects quality, inverting the doctrine into corner-cutting. Good: citing the thesis to strip PRD ceremony from a bug fix. Bad: quoting lightest process to skip regression tests. Borderline: compressing to classify then plan then execute for a prompt, losing the review checkpoints.

**Verification, evidence, and uncertainty.** Check the thesis clauses against A01's common-sense test and both skill overviews. A01's opening and closing lines and the skill pair's core principles ground every clause. Whether external workflow literature phrases the trade the same way is unknown without retrieval.

**Second-order consequence.** Both layers replace trust with structure, A01 distrusts intuition about process weight and the skills distrust executor context and taste, so the thesis is really about making quality independent of who executes.

**Revision decision.** Restate the combined inference as classify first, load the lightest process that protects quality, and when plans are warranted write them for zero-context execution and run them batch-by-batch with review.

**Retained seed evidence.** The labeled thesis lines with their local, external, and combined-inference structure remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`local_corpus_sourced_fact`: The local row for `planning_execution_workflow_patterns` contains 6 source path(s), which should be treated as the first retrieval surface for this theme.
`external_research_sourced_fact`: The external source map provides public documentation, repository, or ecosystem analogues where available.
`combined_evidence_inference_note`: Reliable use of Planning Execution Workflow Patterns comes from loading the local corpus first, checking public ecosystem guidance second, and converting both into verification-backed agent decisions.

## Local Corpus Source Map

**Decision supported.** This section helps decide which local path a planning-execution question should open first. The seed map records heading signals without the corpus's navigation story, A01 at repository root as the router, the skill pair in two trees, and the rewrite draft in a dated backup directory.

**Recommended default and causal basis.** Enter through A01 for process choice, descend to writing-plans and executing-plans for plan-driven flows, and diff live against archive copies when reading. Path placement encodes authority, root-level A01 is the live doctrine, claude-skills is the live skill tree, and rewrite-backups-20260514 is frozen history.

**Operating conditions and assumptions.** All six files remain readable at their mapped paths. The map indexes the six mapped paths and does not cover the S, C, and D tier files A01 references.

**Failure boundary and alternatives.** The map's rows do not say which copy to open first, and the backup draft looks equally citable by path alone. Bounded alternatives and recoveries: map the tier files in a future pass, record line anchors per flow, or collapse identical copies to single rows.

**Counterexample, gotchas, and operational comparison.** The tier files A01 loads by work type, S07, C03, and peers, are unread and unmapped here, so claims about their content would be fabrication. Good: opening A01's decision tree for a process-weight question. Bad: citing S07's contents, an unread file A01 merely names. Borderline: quoting the draft's ARCHv3 anti-pattern filter, real but from frozen backup.

**Verification, evidence, and uncertainty.** Open the six files and confirm they match the roles and identities recorded here. All six files were read in full, 314, 334, 116, 84 lines and two identical copies. Whether the tier files A01 references exist in this repository is unchecked.

**Second-order consequence.** A01 is itself a source map, its tier tables route readers to S06 through S08, C01 through C04, and domain files by work type, so this section's real job is routing to the router.

**Revision decision.** Annotate A01 as the routing entry point, prefer live claude-skills copies for the skill pair, and mark the draft as dated backup consulted only for its expanded Feature-flow detail.

**Retained seed evidence.** The local source rows with their titles, heading signals, and usage roles remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| local_source_filepath_value | local_source_title_text | local_source_heading_signals | local_source_usage_role |
| --- | --- | --- | --- |
| A01-LLM-Workflow01.md | LLM Workflow v01: Work Type Differentiation | LLM Workflow v01: Work Type Differentiation; Quick Classifier; Work Type Framework; Flow 1: Bug Flow (Hours); Flow 2: Enhancement Flow (Days); Flow 3: Feature Flow (Weeks) | local agent-usable source material |
| agents-used-monthly-archive/claude-skills-202603/superpowers/executing-plans/SKILL.md | executing-plans | Executing Plans; Overview; The Process; Step 1: Load and Review Plan; Step 2: Execute Batch; Step 3: Report | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/claude-skills-202603/superpowers/writing-plans/SKILL.md | writing-plans | Writing Plans; Overview; Bite-Sized Task Granularity; Plan Document Header; [Feature Name] Implementation Plan; Task Structure | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/rewrite-backups-20260514/A01-LLM-Workflow01.rewrite-draft.md | LLM Workflow v01: Work Type Differentiation | LLM Workflow v01: Work Type Differentiation; Quick Classifier; Work Type Framework; Flow 1: Bug Flow (Hours); Flow 2: Enhancement Flow (Days); Flow 3: Feature Flow (Weeks) | local agent-usable source material |
| claude-skills/superpowers/executing-plans/SKILL.md | executing-plans | Executing Plans; Overview; The Process; Step 1: Load and Review Plan; Step 2: Execute Batch; Step 3: Report | skill entrypoint or reusable agent prompt |
| claude-skills/superpowers/writing-plans/SKILL.md | writing-plans | Writing Plans; Overview; Bite-Sized Task Granularity; Plan Document Header; [Feature Name] Implementation Plan; Task Structure | skill entrypoint or reusable agent prompt |

## External Research Source Map

**Decision supported.** This section helps decide how much weight external rows may carry in planning-execution guidance. The seed map lists external rows although none was retrieved, and the theme's natural external anchors, agile process-tailoring literature and agent-planning platform docs, are absent from the candidates.

**Recommended default and causal basis.** Rest all claims on the three read evidence units and treat external corroboration as absent until a targeted retrieval pass. External rows are meant to corroborate the theme, and unretrieved URLs cannot corroborate the classifier's time budgets or the skills' batch discipline.

**Operating conditions and assumptions.** Each row keeps a note naming what it could and could not confirm. The map catalogs candidate external references and does not certify content, freshness, or relevance.

**Failure boundary and alternatives.** Removing the rows would break seed preservation, so they stay with downgraded labels. Bounded alternatives and recoveries: a retrieval pass against agent-platform planning documentation if authorized, classic process literature as a secondary candidate, or leaving the table annotated as is.

**Counterexample, gotchas, and operational comparison.** Workflow-methodology search results skew toward framework marketing, retrieval passes should grade for operational substance. Good: naming process-tailoring literature as the retrieval target for the classifier. Bad: citing an unretrieved URL for batch-size doctrine. Borderline: using widely known TDD vocabulary without attribution, common knowledge but unanchored.

**Verification, evidence, and uncertainty.** Confirm no claim cites an external row as fact and the downgrade note is present. No external retrieval was performed during this evolution. Whether external literature supports the four-flow taxonomy is unknown.

**Second-order consequence.** The corpus's boldest external-facing claims are the time budgets, two-to-four hours per bug through four-plus weeks per product, numbers no local source derives and no external source has confirmed.

**Revision decision.** Downgrade all external rows to unretrieved candidates and name process-tailoring writeups, TDD workflow guides, and agent-platform planning docs as replacement candidates.

**Retained seed evidence.** All external rows with their names, roles, and boundary labels remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| external_source_url_value | external_source_name_text | external_source_usage_role | evidence_boundary_label_value |
| --- | --- | --- | --- |
| https://docs.github.com/actions | GitHub Actions documentation | primary automation and CI/CD workflow documentation | external_research_sourced_fact |
| https://docs.github.com/en/actions/concepts/workflows-and-actions/reusing-workflow-configurations | Reusable workflow docs | primary guidance for reusable workflow composition | external_research_sourced_fact |
| https://github.com/openai/codex/blob/-/AGENTS.md | OpenAI Codex repository AGENTS | agent project instructions and testing guidance in a real repository | external_research_sourced_fact |

## Anti Pattern Registry Table

**Decision supported.** This section helps decide which recurring workflow failures deserve standing detection rules. The seed registry lists corpus-hygiene failures while the corpus names its own, over-processing light work, under-processing unclear work, plans that say add validation instead of complete code, guessing through blockers, and starting implementation on main without consent.

**Recommended default and causal basis.** Scan plans for exact paths, complete code, and expected outputs, and scan execution logs for classification, batch reports, and stop events. Each is stated with its guard, A01's classifier for process mismatch, writing-plans' complete-code rule for vague plans, and executing-plans' stop list for guessing.

**Operating conditions and assumptions.** Each row pairs its smell with the observable test the source states. The registry names workflow anti-patterns with detectors and does not police code quality inside tasks.

**Failure boundary and alternatives.** The two layers' anti-patterns differ in blast radius, misclassification wastes a session while a forced-through blocker can corrupt the deliverable. Bounded alternatives and recoveries: encode the checks into a pre-execution checklist, fold detection into the completeness section, or keep the registry as smell-to-guard pointers.

**Counterexample, gotchas, and operational comparison.** Under-processing hides best, a Feature misrouted as an Enhancement fails late, when the missing rails are discovered mid-TDD. Good: rejecting a plan step reading add validation. Bad: pushing through a failing verification because the batch is nearly done. Borderline: a light PRD skipped for a one-line enhancement, defensible when the rails are certain.

**Verification, evidence, and uncertainty.** Replay each registry row against A01 and the skill pair and confirm its test is executable on a real plan or log. A01's over- and under-process warning, writing-plans' remember list, and executing-plans' stop and remember sections supply every added row. Relative frequency of each anti-pattern in real sessions is unmeasured.

**Second-order consequence.** The plan-side anti-patterns are all context assumptions, every writing-plans rule exists because the executor is assumed to know nothing, so the detector is asking what the executor would have to already know.

**Revision decision.** Add rows for process-weight mismatch in both directions, incomplete plan steps, blocker guessing, skipped batch reports, and main-branch implementation without consent.

**Retained seed evidence.** All original registry rows with their causes, replacements, and detection methods remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| anti_pattern_failure_name | failure_cause_risk_reason | safer_default_replacement_pattern | detection_signal_review_method |
| --- | --- | --- | --- |
| context_free_summary_output | agent skips local corpus and produces generic advice | source_map_first_synthesis | verify every listed local path appears in the generated file |
| unsourced_recommendation_claims | guidance appears authoritative without source boundary | evidence_boundary_split_pattern | check for local, external, and inference labels |
| unverified_agent_instruction | recommendation cannot be checked by command or review gate | verification_gate_coupling | require concrete gate in generated reference |

## Verification Gate Command Set

**Decision supported.** This section helps decide which gates must pass before a plan-driven session advances or this reference's guidance is trusted. The seed gate names the corpus verifier while the theme's real gates are per-layer, A01's common-sense test before process loads, per-step verification commands inside plans, and batch-boundary review before execution continues.

**Recommended default and causal basis.** Gate every plan-driven session on the three layers in order, recording verification output verbatim in batch reports. Writing-plans requires exact commands with expected output per step, and executing-plans forbids skipping verifications and requires reporting verification output at each batch boundary.

**Operating conditions and assumptions.** Plans carry runnable verification commands and a reviewer is reachable at batch boundaries. The gate set defines what must pass before work advances between steps, batches, and flows, not the repository's own corpus verifier semantics.

**Failure boundary and alternatives.** The gates assume plans were written to the skill's standard, improvised plans carry no runnable verification to gate on. Bounded alternatives and recoveries: continuous review instead of batch boundaries for high-risk work, or self-review against the plan when no partner is available, noted as a deviation.

**Counterexample, gotchas, and operational comparison.** Verification that repeatedly fails is itself a stop trigger, executing-plans routes it to asking for help, not to retry loops. Good: a batch report with three tasks' verification output and an explicit wait. Bad: continuing past a failed verification because the fix seems obvious. Borderline: batching reports for trivial config-only tasks, tolerated with the deviation noted.

**Verification, evidence, and uncertainty.** Run the three gate layers against a sample session and confirm each yields a decidable outcome. Writing-plans' step template and executing-plans' process steps state every gate verbatim. How often batch reviews catch what per-step verification misses is unmeasured.

**Second-order consequence.** The batch report is a gate disguised as courtesy, saying ready for feedback transfers control to the reviewer, making continuation an approval rather than a default.

**Revision decision.** Adopt three gate layers, classification recorded before process loads, each plan step's verification run as specified, and each batch closed with a report and explicit readiness for feedback.

**Retained seed evidence.** The original verification gate line and its repository verifier command block remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`verification_gate_command_set`: Run the repository verifier after editing this file.

```bash
python3 agents-used-monthly-archive/idiomatic-references-202606/tools/verify_reference_generation.py --stage final
```

## Agent Usage Decision Guide

**Decision supported.** This section helps decide when a working agent should open this reference and which section it should enter through. The seed guide keys usage to theme mentions instead of the states that trigger it, work arriving unclassified, a spec needing a plan, or a written plan needing execution.

**Recommended default and causal basis.** Open this reference when holding unclassified work, an unplanned spec, or an unexecuted plan, and enter at the matching layer. The two skills name their triggers exactly, writing-plans fires when you have a spec for a multi-step task before touching code, and executing-plans when you have a written plan for a separate session.

**Operating conditions and assumptions.** The session type matches, executing-plans expects a separate session with review checkpoints. The guide routes readers into this reference and does not classify their work for them.

**Failure boundary and alternatives.** Keying to every mention of planning would drag the doctrine into trivial tasks the classifier routes to lighter flows. Bounded alternatives and recoveries: direct execution for single-step work, or the subagent-driven execution path writing-plans offers as its first handoff option.

**Counterexample, gotchas, and operational comparison.** Agents skip classification when the work arrives pre-labeled, but labels from requesters encode urgency, not work type. Good: entering at the decision tree with an ambiguous improvement request. Bad: opening writing-plans for a one-line fix. Borderline: consulting only the task-structure template to tighten an existing plan, a fragment use that still helps.

**Verification, evidence, and uncertainty.** Walk an unclassified item, a spec, and a plan through the guide and confirm each lands on the intended layer. Both skills' description lines and A01's classifier partition the entry points as described. How often work arrives genuinely unclassifiable is unmeasured.

**Second-order consequence.** The guide's ordering matters because the skills assume the classifier already fired, plan-writing for a Bug is exactly the over-processing A01 warns against, so entry point two and three presuppose entry point one.

**Revision decision.** Trigger on three states, unclassified work enters at A01's decision tree, a spec without a plan enters at writing-plans, and a plan without progress enters at executing-plans.

**Retained seed evidence.** The original usage line and all guidance bullets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`agent_usage_decision_guide`: Use this reference when a task mentions this theme, one of the listed local source paths, or a nearby technology/workflow surface.

- Start with the local corpus source map.
- Prefer patterns with explicit verification gates.
- Treat external sources as freshness and ecosystem checks, not replacements for local repo conventions.
- Preserve the evidence boundary labels when reusing recommendations.

## User Journey Scenario

**Decision supported.** This section helps decide what end-to-end shape a competent plan-driven session should take. The seed scenario shows a builder choosing a pattern and stops before the journey the corpus scripts, classify the work, write a zero-context plan, then execute it batch by batch with reports and stops.

**Recommended default and causal basis.** Narrate a spec-to-completion pass with the session handoff and one clean stop-and-ask event visible. The corpus hands off explicitly, writing-plans ends by offering subagent-driven or parallel-session execution, and executing-plans picks up the saved plan file in a fresh session.

**Operating conditions and assumptions.** The work classified as plan-worthy and a reviewer is available at batch boundaries. The scenario dramatizes one representative plan-driven journey and does not cover the lighter flows.

**Failure boundary and alternatives.** One journey cannot cover all four flows, Bug and Enhancement journeys never touch the plan-execution machinery. Bounded alternatives and recoveries: a Bug-flow journey ending in hours with a regression test, or a subagent-driven journey staying in one session.

**Counterexample, gotchas, and operational comparison.** Journeys that skip the critical plan review in executing-plans step one inherit plan defects silently, the executor is told to raise concerns before starting. Good: a journey pausing at batch three for feedback before continuing. Bad: one executing all tasks then reporting once at the end. Borderline: a journey where the executor patches a small plan gap silently, against the stop rule but common.

**Verification, evidence, and uncertainty.** Check each journey beat against the five executing-plans steps and confirm none is skipped silently. The skill pair's process sections and handoff script exactly this sequence. Typical plan sizes and batch counts in real sessions are unrecorded.

**Second-order consequence.** The journey crosses a session boundary by design, the plan file is the only context that survives the handoff, which is why writing-plans demands the plan contain everything and why vague plans fail exactly there.

**Revision decision.** Extend the journey through a Feature-flow shape, classification at the decision tree, a plan with exact paths and complete code saved to docs/plans, execution in three-task batches, one mid-batch stop at an unclear instruction, and completion through the finishing sub-skill.

**Retained seed evidence.** The role-based opening, starting state, decision, and trigger lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Role based opening scenario: The new contributor or agent is starting from an unfamiliar theme and deciding whether this reference is the right tool and needs a reference that turns source evidence into an executable next step.
Primary user starting state: The user has a `planning_execution_workflow_patterns` task, one or more local source paths, and uncertainty about which pattern should drive implementation.
Decision being made: choosing what to load, what to trust, what to avoid, and what evidence proves success.
Reference opening trigger: Open this file when the task mentions planning execution workflow patterns, any mapped local source path, or an adjacent workflow with the same failure mode.

## Decision Tradeoff Guide

**Decision supported.** This section helps decide how much process a work item should carry and what being wrong costs in each direction. The seed guide keys adopt, adapt, and avoid to generic evidence agreement instead of this theme's variables, work-type certainty, scope clarity, executor context, and the cost of process mismatch in each direction.

**Recommended default and causal basis.** When classification is uncertain between two flows, run the lighter one but watch the time budget as the tripwire. A01 prices the trade explicitly, over-process wastes time and under-process builds the wrong thing, and its time budgets make the stakes concrete per flow.

**Operating conditions and assumptions.** The work item's scope questions from A01's decision tree are answerable at intake. The guide calibrates process weight per work item and cannot waive the verification gates inside a chosen flow.

**Failure boundary and alternatives.** Classification is fallible, A01's own signal is retrospective, budgets blowing past expectations mean the classification was probably wrong. Bounded alternatives and recoveries: a brief scoping spike when classification is genuinely ambiguous, or escalating one flow up when new rails are discovered mid-work as A01's enhancement rule prescribes.

**Counterexample, gotchas, and operational comparison.** The budget tripwire only works if budgets are recorded at intake, retrofitted budgets always confirm whatever happened. Good: an enhancement escalated to Feature flow when no prior Y exists. Bad: a Product-scale unknown run as a quick feature. Borderline: keeping Enhancement weight on work that found one new rail, defensible if the rail is small.

**Verification, evidence, and uncertainty.** Audit past sessions for budget overruns and check whether classifications were revisited when tripwires fired. A01's classifier table, rule of thumb, and time-budget signal state the trade this guide rekeys onto. The base rate of misclassification at intake is unmeasured.

**Second-order consequence.** The trade is asymmetric with scope uncertainty, under-processing unclear work compounds because wrong things get built on wrong things, while over-processing clear work wastes only the ceremony itself.

**Revision decision.** Rekey adopt to full plan-and-batch discipline for Feature and Product work, adapt to light PRD and TDD for Enhancement work, and avoid heavy process for Bugs where the flow is reproduce, test, fix.

**Retained seed evidence.** The Adopt when, Adapt when, Avoid when, and Cost of being wrong rows with their verification prompts remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| decision_option_name | when_to_choose_condition | tradeoff_cost_description | verification_question_prompt |
| --- | --- | --- | --- |
| Adopt when | local corpus and external evidence agree on the planning execution workflow patterns pattern | fastest path, but can copy stale local assumptions | Does the selected pattern appear in the canonical source and current external evidence? |
| Adapt when | local sources are strong but public ecosystem guidance has changed | preserves repo fit, but requires explicit inference notes | Did the reference label the local fact, external fact, and combined inference separately? |
| Avoid when | source evidence is thin, conflicting, or unrelated to the user journey | prevents false confidence, but may require deeper research | Is there a confidence warning or adjacent reference route? |
| Cost of being wrong | wrong planning execution workflow patterns guidance can send an agent to the wrong files, tests, or abstraction | wasted implementation loop and weaker verification | Would a reviewer know what to undo and what to inspect next? |

## Local Corpus Hierarchy

**Decision supported.** This section helps decide which copy outranks which when planning-execution guidance conflicts or copies diverge. The seed hierarchy names sources without ranking them, and this corpus has a real precedence question, A01 versus its richer mermaid draft, and archive versus live skill copies.

**Recommended default and causal basis.** Resolve doctrine from live copies, cite the draft only for its unique staging detail with its date attached, and re-diff skill copies whenever either path is read. Live A01 outranks the dated draft for current doctrine because the draft is a frozen backup, yet the draft uniquely preserves the staged PRDv1-v3 and ARCHv1-v3 Feature detail.

**Operating conditions and assumptions.** All paths remain readable and the diff check stays part of the read ritual. The hierarchy ranks local retrieval priority for this theme and does not rank the unread tier files A01 references.

**Failure boundary and alternatives.** With byte-identical skill copies the archive-versus-live ranking is untestable today, it matters only at first divergence. Bounded alternatives and recoveries: designating one A01 rendering canonical in the mapping table, a scheduled diff in the refresh queries, or merging the draft's staging detail into live A01 as a proposed edit.

**Counterexample, gotchas, and operational comparison.** The draft's mermaid diagrams render richer than A01's ASCII, tempting readers to treat the prettier document as the newer one. Good: preferring live A01's flow steps while citing the draft for ARCHv3's anti-pattern filter. Bad: citing the draft as current process. Borderline: citing either skill copy today, harmless while identical.

**Verification, evidence, and uncertainty.** Confirm all paths exist and the identity and divergence checks are recorded here. The diff performed during this evolution found both skill pairs byte-identical and the draft diverging from A01 mainly in diagram rendering plus Feature staging. Whether live A01 deliberately dropped the staging detail or lost it is unrecorded.

**Second-order consequence.** The draft inverts the usual staleness rule, here the backup is more detailed than the live document, so precedence must be per-claim, live wins on what to do and the draft adds how the Feature flow once staged it.

**Revision decision.** Rank live A01 first for classification doctrine, the live skill copies first for plan and execution doctrine, the draft as supplementary detail with a dated-backup label, and record the identity checks.

**Retained seed evidence.** The classification vocabulary line, the confidence warning, and the hierarchy rows with their reviewer questions remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Classification vocabulary includes canonical, supporting, legacy, duplicate, and conflicting source roles.

| local_source_filepath_value | corpus_hierarchy_role | heading_signal_to_convert | reviewer_question_to_answer |
| --- | --- | --- | --- |
| A01-LLM-Workflow01.md | canonical primary source | LLM Workflow v01: Work Type Differentiation; Quick Classifier; Work Type Framework | What guidance, warning, or example should this source contribute to Planning Execution Workflow Patterns? |
| agents-used-monthly-archive/claude-skills-202603/superpowers/executing-plans/SKILL.md | legacy historical source | Executing Plans; Overview; The Process | What guidance, warning, or example should this source contribute to Planning Execution Workflow Patterns? |
| agents-used-monthly-archive/claude-skills-202603/superpowers/writing-plans/SKILL.md | legacy historical source | Writing Plans; Overview; Bite-Sized Task Granularity | What guidance, warning, or example should this source contribute to Planning Execution Workflow Patterns? |
| agents-used-monthly-archive/rewrite-backups-20260514/A01-LLM-Workflow01.rewrite-draft.md | legacy historical source | LLM Workflow v01: Work Type Differentiation; Quick Classifier; Work Type Framework | What guidance, warning, or example should this source contribute to Planning Execution Workflow Patterns? |
| claude-skills/superpowers/executing-plans/SKILL.md | supporting context source | Executing Plans; Overview; The Process | What guidance, warning, or example should this source contribute to Planning Execution Workflow Patterns? |
| claude-skills/superpowers/writing-plans/SKILL.md | supporting context source | Writing Plans; Overview; Bite-Sized Task Granularity | What guidance, warning, or example should this source contribute to Planning Execution Workflow Patterns? |

## Theme Specific Artifact

**Decision supported.** This section helps decide what concrete evidence object must exist before this reference counts as operational. The seed artifact names a lifecycle diagram while this theme's operational artifact is a plan document written to the skill's template plus its execution record of batch reports.

**Recommended default and causal basis.** Carry one filled plan-plus-execution-record pair from a real Feature-flow session as the reviewable instance. Writing-plans mandates the header block, goal, architecture, tech stack, and bite-sized task structure, and executing-plans emits batch reports with verification output as it runs.

**Operating conditions and assumptions.** The plan captures steps at the two-to-five-minute grain the skill mandates, not paraphrased summaries. The artifact certifies this reference is operational and does not grade the code the plan produced.

**Failure boundary and alternatives.** Plan artifacts for work the classifier routes to Bug or Enhancement flow are the over-processing A01 warns against. Bounded alternatives and recoveries: a classification record for lighter flows, or a subagent-driven session log when execution stayed in one session.

**Counterexample, gotchas, and operational comparison.** Plans reconstructed after execution flatter the session, the plan must predate the code it directed for the artifact to prove anything. Good: a dated plan file with five pathed tasks and three batch reports. Bad: a merged feature with no surviving plan. Borderline: a plan missing expected outputs on two steps, review-worthy but incomplete.

**Verification, evidence, and uncertainty.** Check the artifact carries the mandated header, per-step commands with expected output, and matching batch reports. Writing-plans' header and task templates and executing-plans' report step define exactly the fields the artifact instantiates. Whether plan discipline measurably improves outcomes here is untested.

**Second-order consequence.** The artifact doubles as the session-boundary contract, everything the executor knows arrives in the plan file, so plan-quality review is executable before any code exists by asking whether a zero-context reader could run it.

**Revision decision.** Define the artifact as one plan file in docs/plans form with header, exact paths, complete code, and expected outputs, paired with its batch reports and any stop events.

**Retained seed evidence.** The artifact definition line and the artifact field rows with completion rules remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Theme specific artifact: worked planning execution workflow patterns example with user goal, decision point, failure mode, and verification gate.

| artifact_field_name | artifact_completion_rule | evidence_source_hint |
| --- | --- | --- |
| user_goal_statement | state the user's concrete goal before applying Planning Execution Workflow Patterns | local corpus hierarchy plus critique findings |
| decision_boundary_rule | define the point where this reference should be used or avoided | decision tradeoff guide |
| verification_gate_rule | define the command, checklist, or review question that proves the artifact worked | verification gate command set |

## Worked Example Set

**Decision supported.** This section helps decide which workflow behaviors should be taught as exemplary, negligent, or conditionally acceptable. The seed examples restate corpus verdicts and never grade real workflow conduct against the corpus's own contrasts, complete code versus add validation, batch reports versus silent runs, stop-and-ask versus guessing.

**Recommended default and causal basis.** Grade every example by classification presence, plan completeness against the template, and execution fidelity to the batch-and-stop rules. Writing-plans teaches through its own template, exact paths, runnable commands, expected outputs, so graded examples should reuse those exact contrasts.

**Operating conditions and assumptions.** Each example names the rule it exercises and the test that decides the verdict. The examples grade workflow conduct, not the merits of the features being built.

**Failure boundary and alternatives.** Examples fixed to the skill's pytest template may read as Python-specific, though the pattern covers any toolchain. Bounded alternatives and recoveries: draw examples from this repository's own lane journals, grade the skill's own pytest task template directly, or add a misclassification example.

**Counterexample, gotchas, and operational comparison.** The borderline case degrades silently, unreported batches still produce code, the loss appears only when late review finds early mistakes replicated across batches. Good: a plan step with the command and its expected FAIL output. Bad: a step reading implement the feature. Borderline: a complete plan whose executor batched all tasks into one report.

**Verification, evidence, and uncertainty.** Scan each verdict against its cited rule and confirm the graded behavior is visible in the plan or log itself. Writing-plans' remember list and executing-plans' process steps ground all three verdicts. Which negligent shape dominates real sessions is unmeasured.

**Second-order consequence.** The corpus's bad examples all shift work forward in time, vague plans defer decisions to the executor and skipped reports defer review to the end, where fixes cost most.

**Revision decision.** Recast good as a classified Feature with a template-conforming plan executed in reported batches, bad as an unclassified task run on an improvised plan with a guessed-through blocker, and borderline as a good plan executed without batch reports.

**Retained seed evidence.** The good, bad, and borderline example lines with their original verdict framing remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Good example: Use Planning Execution Workflow Patterns after loading the canonical source, confirming the external evidence boundary, and writing a verification gate before implementation.
Bad example: Use Planning Execution Workflow Patterns as a generic tutorial while ignoring the mapped local paths, source hierarchy, and cost of being wrong.
Borderline case: Use Planning Execution Workflow Patterns only after adding a confidence warning when local evidence is thin or conflicts with current ecosystem guidance.

## Outcome Metrics and Feedback Loops

**Decision supported.** This section helps decide which observable signals should trigger revising workflow practice or this reference. The seed metrics name lead time and generic signals without this theme's observables, classification-versus-budget variance, stop events per session, plan-gap discoveries mid-execution, and batch report cadence.

**Recommended default and causal basis.** Record per session the classification, budgeted versus actual time, stop events, and plan gaps, and route gap patterns back to plan-writing practice. A01 designates budget overrun as the misclassification signal, and executing-plans' stop triggers mark exactly where plans failed their zero-context contract.

**Operating conditions and assumptions.** Classifications and budgets are recorded at intake so variance is computable. The metrics gauge workflow discipline, not the product quality of what was built.

**Failure boundary and alternatives.** Stop events read as failure but are the discipline working, their absence in long sessions is the suspicious signal. Bounded alternatives and recoveries: sampled session audits, per-flow variance dashboards at volume, or tracking only stop events at first.

**Counterexample, gotchas, and operational comparison.** Budget variance flatters sessions that padded their estimates, the classifier's fixed budget table is the honest baseline. Good: tightening plan templates after three missing-dependency stops. Bad: celebrating zero stops in a session that guessed through two blockers. Borderline: skipping metrics in a period of Bug-only work, noted.

**Verification, evidence, and uncertainty.** Reconcile recorded signals against sampled session logs and check failures trace to named rules. A01's budget-signal paragraph and executing-plans' stop list anchor the added counters. Healthy baselines for stop rates and budget variance are unmeasured, so first thresholds are provisional.

**Second-order consequence.** Plan-gap counts are the cheapest plan-quality feedback, every mid-execution stop for a missing dependency or unclear instruction names a specific writing-plans rule the plan violated.

**Revision decision.** Adopt budget variance per flow, stop events with their trigger types, plan gaps found in execution, and batches per report as primary signals.

**Retained seed evidence.** The leading indicator, failure signal, and review cadence lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Leading indicator: the next task uses the reference to make a better decision with less ambiguity.
Failure signal: the reference remains a source map and never becomes an operating guide.
Review cadence: Re-run the verifier after every generated-reference edit and refresh external sources when public APIs, docs, or tooling releases change.

## Completeness Checklist

**Decision supported.** This section helps decide when this reference may be declared ready to hand to an agent. The seed checklist confirms generic sections exist and never checks this document's specific obligations, the four flows with their steps, the decision tree's question order, the plan template's mandatory parts, the batch-of-three default, and the stop triggers.

**Recommended default and causal basis.** Tick structural items with citations, then grep this document for each flow, question, template part, and stop trigger. This document transmits a routing doctrine plus an execution contract, so readiness means the flows, questions, templates, and stops survived transmission intact.

**Operating conditions and assumptions.** Each added item names its target and whether a script or human verifies it. The checklist gates this document's readiness, not the quality of sessions later run under it.

**Failure boundary and alternatives.** A reference that dropped the stop triggers would still describe execution while losing the rule that prevents corrupted work. Bounded alternatives and recoveries: generate coverage items from the sources' section lists, deep-check two random items per review, or pair-review the plan artifact.

**Counterexample, gotchas, and operational comparison.** Rule presence can pass while phrasing drifted, batch of three weakened to a few tasks changes the checkpoint cadence materially. Good: a tick citing the line carrying the verification-fails-repeatedly stop trigger. Bad: all ticks green from a headings glance. Borderline: carrying forward last cycle's phrasing check with a staleness note.

**Verification, evidence, and uncertainty.** Grep this document for the flows, questions, and triggers, then spot-read two against the sources. The seed's structural items map onto real sections here and anchor the added fidelity layer. How much spot-reading each cycle needs depends on edit volume.

**Second-order consequence.** The doctrine's ordering is part of its content, the classifier's questions must be asked in sequence and stop as soon as one answer is clear, so fidelity checks must verify order, not just presence.

**Revision decision.** Append items requiring all four flows present with time scales, the four classifier questions in order, the plan header and task templates, the batch default, and all four stop triggers.

**Retained seed evidence.** All structural checklist items covering scenario, decision guide, hierarchy, artifact, examples, metrics, and routing remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- The role scenario names the user, starting state, decision, and trigger for Planning Execution Workflow Patterns.
- The decision guide includes Adopt when, Adapt when, Avoid when, and Cost of being wrong.
- The local corpus hierarchy identifies canonical and supporting sources or gives a confidence warning.
- The theme specific artifact is concrete enough to review without reading every mapped source.
- The examples cover good, bad, and borderline usage.
- The metrics section names one leading indicator and one failure signal.
- The adjacent routing section points to a better reference when this one is not the right fit.

## Adjacent Reference Routing

**Decision supported.** This section helps decide when a question should leave this reference and which neighbor owns it. The seed routing splits the theme name into keywords aimed at unnamed destinations instead of routing by need, process routing and plan-execution discipline stay here while TDD mechanics, subagent dispatch, and git worktree setup belong elsewhere.

**Recommended default and causal basis.** Ask whether the question concerns choosing process or writing and executing plans, and keep only those here. The corpus itself routes outward, executing-plans requires the worktree and finishing-a-development-branch skills, and writing-plans hands off to subagent-driven development, neighbors this reference should name rather than absorb.

**Operating conditions and assumptions.** Each route names its trigger, a destination resolving to a real file, and what stays here. Routing redirects within this corpus and cannot authorize work in a destination's domain.

**Failure boundary and alternatives.** Keyword routes point at references that exist only as words, stranding the reader who follows them. Bounded alternatives and recoveries: consult the corpus index before adding routes, keep unresolved needs here with a gap note, or escalate genuine overlap to the user.

**Counterexample, gotchas, and operational comparison.** Execution questions blur the seam, batch discipline is owned here while the subagent-per-task execution style belongs to the subagent references, and both arrive worded as how should this plan be run. Good: keeping a process-weight question here. Bad: routing to the workflow adjacent reference, a keyword with no file. Borderline: a plan-handoff question split between the handoff script here and dispatch mechanics elsewhere.

**Verification, evidence, and uncertainty.** Resolve each named destination to an existing corpus file and walk one sample question through each trigger. The skills' integration sections name the required neighbor skills this routing mirrors. Whether future themes will subdivide this doctrine's territory is unknown.

**Second-order consequence.** This doctrine sits upstream of most neighbors, it decides process and produces plans that other skills execute pieces of, so routing out is usually a handoff downstream rather than a topic overlap.

**Revision decision.** Keep classification, plan writing, and batch execution here, route subagent dispatch to the parallel agent dispatch reference and subagent development to its reference, both real in this corpus, and record unowned needs like worktree setup as gaps.

**Retained seed evidence.** The adjacency guidance line and the keyword-derived route stubs remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Adjacent reference guidance: Use the nearest language, workflow, agent, or documentation reference when the theme becomes concrete.
Adjacent reference 1: consider the planning adjacent reference when the current task pivots away from planning execution workflow patterns.
Adjacent reference 2: consider the execution adjacent reference when the current task pivots away from planning execution workflow patterns.
Adjacent reference 3: consider the workflow adjacent reference when the current task pivots away from planning execution workflow patterns.

## Workload Model

**Decision supported.** This section helps decide how much planning and execution work one session may take on before splitting. The seed model bounds endpoints per batch but not this theme's working units, work items classified per session, plan tasks written per plan, and tasks executed per batch.

**Recommended default and causal basis.** Write plans at the mandated step grain and execute three tasks per batch, adjusting batch size only with the reviewer's consent. The corpus sets the numbers itself, batches default to three tasks, plan steps run two to five minutes, and A01 budgets whole flows from hours to months.

**Operating conditions and assumptions.** The session can hold the plan and its current batch in view at once. The model bounds the planner's and executor's work per session and does not bound the flows' calendar budgets, which A01 owns.

**Failure boundary and alternatives.** The skill's batch size is a default, not a law, and no source bounds how many tasks one plan should carry. Bounded alternatives and recoveries: smaller batches for risky mid-plan sections, subagent-per-task execution for parallelizable plans, or splitting long plans across sessions at batch boundaries.

**Counterexample, gotchas, and operational comparison.** Oversized steps hide work, a step reading implement the endpoint can swallow an hour and every decision in it, defeating the review cadence. Good: a twelve-task plan executed across four reported batches. Bad: a forty-step batch run without a report. Borderline: a five-task batch for homogeneous config edits, against the default with consent.

**Verification, evidence, and uncertainty.** Compare session outcomes at different batch sizes and step grains and record where review quality degrades. Writing-plans' step timing and executing-plans' batch default ground the model's numbers. The plan size at which a single session's execution degrades is unmeasured.

**Second-order consequence.** The step grain is the load-bearing bound, two-to-five-minute steps force decisions into the plan and out of execution, which is what makes batches reviewable and stops rare.

**Revision decision.** Rebound the model around one plan per feature, tasks decomposed to the two-to-five-minute step grain, execution in three-task batches, and one flow's work per session.

**Retained seed evidence.** The four workload dimensions with their boundary values and verification pressure points remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`combined_evidence_inference_note`: Treat Planning Execution Workflow Patterns as a general reference operating reference, not as a prose summary.

| workload_dimension_name | workload_boundary_value | verification_pressure_point |
| --- | --- | --- |
| primary_usage_surface | idiomatic reference selection and synthesis work where the reference must prevent generic advice and preserve evidence boundaries | verify that the reference changes the next implementation or review action |
| bounded_capacity_model | one theme, all mapped local sources, current external evidence when available, and one downstream task review | split the task or create a narrower reference when this boundary is exceeded |
| source_pressure_model | local heading signals include LLM Workflow v01: Work Type Differentiation; Quick Classifier; Work Type Framework; Flow 1: Bug Flow (Hours); Flow 2: Enhancement Flow (Days); Flow 3: | compare guidance against canonical local sources before following external examples |
| artifact_pressure_model | required artifact is worked planning execution workflow patterns example with user goal, decision point, failure mode, and verification gate | require the artifact before claiming the reference is operationally usable |

## Reliability Target

**Decision supported.** This section helps decide what measurable reliability this reference must demonstrate before its guidance is trusted. The seed table demands unmeasured percentages while this theme supports binary targets, every session has a recorded classification and every plan-driven session a template-conforming plan with batch reports.

**Recommended default and causal basis.** Keep the four seed dimensions with methods attached and lead with the two per-session scans. The doctrine's tests are per-session and decidable, the classification exists or does not, the plan carries the header and step grain or does not, so targets can be scanned rather than sampled.

**Operating conditions and assumptions.** Each target names its metric, scan method, population, owner, and corrective action. The targets judge this reference and the workflow discipline, not the shipped features' defect rates.

**Failure boundary and alternatives.** Quoting the seed's percentages as achieved performance manufactures rigor this corpus never earned. Bounded alternatives and recoveries: stop-event handling targets instead of per-session scans, sampled plan audits, or postmortems per blown budget instead of rates.

**Counterexample, gotchas, and operational comparison.** Recorded classification does not prove sound classification, the budget-variance signal is the independent second gate. Good: a scan showing every session carries its classification. Bad: reporting the seed's numbers nobody sampled. Borderline: one undocumented emergency bug fix, recorded afterward with the gap noted.

**Verification, evidence, and uncertainty.** Scan one period's sessions for both targets and record hits with resolutions. A01's classifier and the skill templates give the operational definitions the scans check. No baseline exists for either target, so the first scanned period defines achievability.

**Second-order consequence.** The classification target audits the decision everything downstream inherits, and its absence predicts exactly the budget overruns A01 names as the misclassification signal.

**Revision decision.** Add binary targets, recorded classification per session and a conforming plan with batch reports per plan-driven session, each marked unbaselined and owned.

**Retained seed evidence.** All four reliability rows with their threshold values and evidence-collection methods remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| reliability_target_name | measurable_threshold_value | evidence_collection_method |
| --- | --- | --- |
| source_boundary_preservation | 100 percent of recommendations keep local, external, and inference boundaries visible | review generated text for the three evidence labels before reuse |
| decision_accuracy_sample | at least 18 of 20 sampled uses route to the correct adopt, adapt, avoid, or adjacent-reference decision | sample downstream tasks and record reviewer verdicts |
| unsupported_claim_rate | zero unsupported production, security, latency, or reliability claims in final guidance | reject claims without source row, explicit inference note, or verification method |
| recovery_path_clarity | every avoid or failure case names the rollback, escalation, or next-reference route | inspect failure-mode and adjacent-routing sections together |

## Failure Mode Table

**Decision supported.** This section helps decide which workflow failures deserve standing mitigations. The seed table carries hygiene and traffic rows and omits how workflow sessions actually fail, misclassified work discovered late, plans with gaps that strand executors, blockers guessed through, and reviews skipped until errors compound.

**Recommended default and causal basis.** Check any failed session backward through the chain, review cadence, then stop handling, then plan quality, then the original classification. The corpus names each with its guard, A01's budget tripwire for misclassification, the stop triggers for plan gaps and blockers, and the batch cadence for review starvation.

**Operating conditions and assumptions.** Each row names its trigger, earliest observable signal, blast radius, containment, and correction. The table covers workflow-level failures, while documentation-process failures stay with the seed rows.

**Failure boundary and alternatives.** Misclassification surfaces latest and costs most, its first hard signal is a blown budget after real work is sunk. Bounded alternatives and recoveries: pre-execution plan review to pre-empt gaps, intake classification review to pre-empt misrouting, or smaller batches to shorten the compounding window.

**Counterexample, gotchas, and operational comparison.** Plan gaps and executor incompetence present identically at a distance, the stop trigger's wording, instruction unclear versus test fails, is the differential. Good: a blown budget triaged back to an Enhancement that needed Feature rails. Bad: rerunning a stranded plan unchanged. Borderline: an executor patching one missing path silently, contained but against the stop rule.

**Verification, evidence, and uncertainty.** Seed one failure per row in a review drill and confirm the named signal fires and maps to the right repair. A01's budget signal, the stop triggers, and the batch cadence supply every added row. Failure frequencies in real sessions are unmeasured.

**Second-order consequence.** The failures chain, a misclassified Feature gets no plan, planlessness leaves the executor guessing, and guessing without review checkpoints compounds unchecked, so the earliest guard is worth the most.

**Revision decision.** Add misclassification, plan-gap stranding, blocker guessing, and review starvation rows, each with its source-named signal, blast radius, and repair.

**Retained seed evidence.** All four seed failure rows with their triggers and mitigation actions remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| failure_mode_name | likely_trigger_condition | required_mitigation_action |
| --- | --- | --- |
| source drift hides truth | external or local guidance changes after the reference was written | refresh public evidence, rerun local corpus gate, and mark stale claims before reuse |
| generic advice escapes review | agent copies plausible best practices without theme-specific verification | block completion until the verification gate names concrete command, reviewer question, or metric |
| decision path remains implicit | reader cannot tell when to adopt, adapt, or avoid the pattern | add decision table, cost of being wrong, and adjacent-reference route |
| large corpus becomes list | many sources are indexed but not synthesized into ranked guidance | classify canonical, supporting, legacy, duplicate, and conflicting sources |

## Retry Backpressure Guidance

**Decision supported.** This section helps decide when failed workflow work should be rerun, re-planned, reclassified, or escalated. The seed bullets classify verification failures generically and never carry this theme's retry rules, repeated verification failure is a stop trigger, not a retry loop, and blown budgets trigger reclassification, not harder pushing.

**Recommended default and causal basis.** Diagnose which layer failed before any retry, rerun a step verification once, and route persistent failures to the partner with the plan or classification change named. Executing-plans lists verification fails repeatedly among its stop-and-ask conditions, and A01 reads persistent budget overrun as evidence the classification is wrong.

**Operating conditions and assumptions.** The session's plan and classification records exist so the retry can name what changed. This governs retrying workflow-level work and reference-verification runs, kept as two labeled layers.

**Failure boundary and alternatives.** Reclassification mid-work costs the process already loaded, a Feature reclassified to Product restarts discovery on sunk PRD work. Bounded alternatives and recoveries: escalation to the user when two plan revisions fail on the same task, flow escalation when new rails keep appearing, or abandoning the batch to preserve reviewed work.

**Counterexample, gotchas, and operational comparison.** Retrying by adding process feels rigorous but inverts A01, a failing Enhancement needs reclassification or a fixed plan, not a Product-weight ceremony. Good: a failing step rerun once then raised with its output. Bad: a fifth silent retry of the same verification. Borderline: an executor revising an obviously typoed path solo, letter-violating but low risk.

**Verification, evidence, and uncertainty.** Audit retry sequences for changed plans or classifications between attempts and check verification reruns stayed bounded. The stop-trigger list and A01's budget signal identify the structural causes the retries must change. How often plan revision succeeds on the second attempt is unmeasured.

**Second-order consequence.** The corpus's backpressure is social, not mechanical, every hard failure routes to the human partner, ask for clarification rather than guessing, so escalation is the designed relief valve rather than the last resort.

**Revision decision.** Add the workflow-layer rules, one bounded rerun for a failed step verification then stop and ask, plan gaps route back to plan revision rather than executor improvisation, and repeated budget overruns route to reclassification.

**Retained seed evidence.** All five retry and backpressure bullets, including the one-owner-per-file rule, remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- Retry only after the failed verification signal is classified as transient, stale evidence, missing context, or true contradiction.
- Use one bounded retry for stale external evidence refresh, then escalate to a human or a narrower source-specific reference.
- Apply backpressure by stopping new generation or implementation work when source coverage, critique coverage, or verification gates are red.
- For long-running agent workflows, checkpoint after each batch and re-read the current spec before any broad rewrite, commit, push, or destructive operation.
- For distributed execution, assign one owner per generated file or theme batch and require merge-time verification of exact path, heading, and evidence-boundary invariants.

## Observability Checklist

**Decision supported.** This section helps decide what evidence must exist that a workflow session happened as claimed. The seed bullets recycle generic evidence records and never name this theme's evidence stream, the classification record, the plan file, the batch reports with verification output, and the stop events.

**Recommended default and causal basis.** Record per plan-driven session the classification, plan path, batch reports, and stop events, keeping executor transcripts out of the record. The corpus generates these as it runs, writing-plans saves plans to docs/plans, and executing-plans emits reports and stop events at scripted moments.

**Operating conditions and assumptions.** Sessions can persist small text records alongside their deliverables. This covers observing workflow sessions, not the executed code's runtime telemetry.

**Failure boundary and alternatives.** Full records for Bug-flow sessions are ceremony, the lighter flows warrant lighter evidence. Bounded alternatives and recoveries: plan-and-classification-only retention for routine sessions, full retention for failed ones, or sampled retention at volume.

**Counterexample, gotchas, and operational comparison.** Batch reports paraphrased into summaries lose the verification output that makes them auditable, the skill says show verification output. Good: a session folder with classification, plan, three reports, and one stop event. Bad: a shipped feature with no surviving plan or reports. Borderline: a Bug-flow session recording only the regression test and a one-line note.

**Verification, evidence, and uncertainty.** Spot-check session records for classification, plan conformance, and verbatim reports. The seed's small-audit-evidence preference and the skills' save and report rules anchor the record contents. The retention horizon for session records is untuned.

**Second-order consequence.** The plan file is self-observing evidence, its dated presence in docs/plans with the mandated header proves the planning discipline ran, no separate logging is needed for the writing half.

**Revision decision.** Recenter the checklist on session evidence, the classification with its budget, the plan file as saved, each batch report verbatim, and stop events with their triggers and resolutions.

**Retained seed evidence.** All six observability bullets including the small-audit-evidence preference remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- Record which local sources were loaded and which were intentionally skipped.
- Record the exact verification command, reviewer question, or rendered artifact used as proof.
- Record p50/p95/p99 latency or reviewer-time measurements when the reference affects runtime or workflow speed.
- Capture reviewer decision, unresolved uncertainty, and next refresh trigger.
- Record leading indicator and failure signal from this file in the coverage manifest or journal when the reference drives real work.
- Keep audit evidence small enough to review: command output summary, changed-file list, and unresolved-risk notes are preferred over raw transcript dumps.

## Performance Verification Method

**Decision supported.** This section helps decide how to prove the workflow's time budgets describe this repository's reality. The seed method fixes handler latency numbers while this theme's performance question is A01's own table, whether Bug work lands in hours, Enhancements in days, Features in weeks, and Products in months.

**Recommended default and causal basis.** Record budgeted versus actual per session and review variance per flow at each corpus cycle. A01 publishes per-flow budgets down to the phase level, thirty minutes of PRD for an Enhancement, sixteen hours of TDD for a Feature, making the claim directly checkable against session records.

**Operating conditions and assumptions.** Enough sessions accumulate per flow for variance to mean anything. This evaluates the workflow discipline's time claims, not code performance, keeping the seed's latency defaults as the absent-SLO fallback.

**Failure boundary and alternatives.** The budgets' provenance is unstated, they arrived with A01 rather than from measured local sessions, so they are calibration targets, not verified facts. Bounded alternatives and recoveries: tracking only the binary blown-or-not signal, phase-level tracking for Feature work only, or accepting the table unverified with its label.

**Counterexample, gotchas, and operational comparison.** Documentation-heavy repository work may sit systematically outside budgets written for product engineering, variance then indicates table mismatch, not indiscipline. Good: a quarter's Bug sessions averaging inside the two-to-four-hour band. Bad: quoting the table as measured local performance. Borderline: adopting the table unverified for one quarter while records accumulate, noted as assumed.

**Verification, evidence, and uncertainty.** Publish the variance table with session counts per flow. A01's time-budget table and its classification-signal paragraph state the claim this method tests. Effect size and the session count needed per flow for signal are unknown.

**Second-order consequence.** The budget table serves double duty, prospectively it sizes work and retrospectively it detects misclassification, but only the retrospective use has a stated rule, so measurement is what activates the table's tripwire function.

**Revision decision.** Measure actual time per flow phase against A01's table and read persistent variance as either misclassification or a table needing local recalibration.

**Retained seed evidence.** The performance method line, both indicator lines, the measurement packet, and the pass and fail conditions remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Performance method: require source-boundary preservation and p95 under 10 minutes for a reviewer to identify the next verification action.
Leading indicator to measure: the next task uses the reference to make a better decision with less ambiguity.
Failure signal to watch: the reference remains a source map and never becomes an operating guide.
Required measurement packet: capture input size, source count, tool-call count, wall-clock time, p50/p95/p99 latency where runtime applies, and reviewer decision time where documentation applies.
Pass condition: the reference must let a reviewer identify the correct next action, verification gate, and stop condition without reading unrelated files.
Fail condition: the reference encourages implementation before the workload, reliability target, and failure-mode table are explicit.

## Scale Boundary Statement

**Decision supported.** This section helps decide at what scale single-item workflow discipline stops sufficing and what structure replaces it. The seed statement recites multi-system limits and misses this theme's scale walls, plans too large for one executor session, work items spanning multiple flows at once, and portfolios of concurrent items competing for the same reviewer.

**Recommended default and causal basis.** Run one plan per executor session, decompose multi-flow items at intake, and cap concurrent plan-driven work at what the reviewer can actually read. The doctrine assumes one work item, one flow, one plan, one executor, and one reviewing partner, and every assumption breaks separately at scale.

**Operating conditions and assumptions.** Session records make reviewer saturation visible as unread or perfunctory batch feedback. The boundaries bound this reference and its discipline, not team-level project management.

**Failure boundary and alternatives.** Scaling advice beyond the single-item shape is inference here, no source addresses concurrent items or multi-executor plans. Bounded alternatives and recoveries: subagent-driven execution to parallelize within one reviewed session, plan-file updates as the cross-session memory, or sequential scheduling when reviewer time is the constraint.

**Counterexample, gotchas, and operational comparison.** Splitting a plan across sessions leaks context despite the zero-context contract, the second session knows only the plan, not the first session's discoveries, so mid-plan learnings must be written back into the plan file. Good: a large feature split into two plans reviewed independently. Bad: five concurrent plans reporting to one absent reviewer. Borderline: a plan resumed in a third session with learnings folded back in, workable if the write-back is disciplined.

**Verification, evidence, and uncertainty.** Track feedback latency and depth against concurrent plan count to locate the reviewer wall empirically. The skills' single-plan single-partner shape supports the bottleneck inference, marked as extension beyond the sources. The concurrent-plan count at which review quality collapses is unmeasured.

**Second-order consequence.** The reviewer is the scaling bottleneck by design, checkpoints exist to route control through a human, so parallel plan execution multiplies report traffic into a single approval channel and quietly converts checkpoints into rubber stamps.

**Revision decision.** Add scale signals, plans split across sessions at batch boundaries, items needing two flows decomposed into separate items, and reviewer saturation when batch reports queue faster than feedback returns.

**Retained seed evidence.** All four scale boundary statements including the distributed split and context-drift rules remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Planning Execution Workflow Patterns stops being sufficient when the task spans multiple independent systems, more than one ownership boundary, unbounded source discovery, or production traffic without an explicit SLO.
Under distributed execution, split work by theme file and preserve one verification owner per split; do not let parallel agents rewrite the same reference without a merge checkpoint.
Under long-running agent workflows, treat context drift as a reliability failure: checkpoint state, summarize open risks, and verify against the spec before continuing.
Under large-codebase scale, require dependency or source-graph narrowing before applying this reference; a source list without ranked canonical guidance is not enough.

## Future Refresh Search Queries

**Decision supported.** This section helps decide which future searches would genuinely refresh this reference's external evidence. The seed query table drops the internal theme name into three templates whose literal phrasing targets a coinage no external author uses.

**Recommended default and causal basis.** Search agent planning documentation on a fast cadence and process-methodology commentary on a slow one, feeding the evidence map. Useful refresh queries speak the ecosystem's vocabulary, agent planning workflows, implementation plan templates, process tailoring, not this corpus's file-naming scheme.

**Operating conditions and assumptions.** Each query names its target section, source type, and firing trigger. The queries refresh external analogues for this theme, while the local documents change only through repository edits.

**Failure boundary and alternatives.** Empty results from a coinage query logged as freshness confirmed convert search blindness into false confidence. Bounded alternatives and recoveries: watching the superpowers skill tree and A01 itself for revisions, curated engineering-process reading lists, or dated retrieval records as the refresh driver.

**Counterexample, gotchas, and operational comparison.** Workflow search results skew toward methodology marketing that names process without carrying operational templates. Good: a query for agent plan-execution checkpointing feeding the batch-discipline sections. Bad: searching the literal theme title and logging zero hits as freshness. Borderline: adopting a platform's plan template with an inference label pending corroboration.

**Verification, evidence, and uncertainty.** Run each query once, grade the top results for operational substance, and rewrite phrasings that return mostly marketing noise. The seed's three-row structure targeting docs, repositories, and release notes fits this theme's platform-and-methodology refresh needs. Which phrasings surface substantive workflow guidance is unknowable in advance, so the queries need their own review cadence.

**Second-order consequence.** The fastest-moving refresh target is agent planning tooling, plan-file conventions and execution checkpointing are active platform surface, while the classifier's process-weight doctrine drifts on publication timescales.

**Revision decision.** Rephrase toward ecosystem vocabulary, agent-platform planning and task-decomposition docs, process-tailoring and right-sizing writeups, and TDD workflow guides, each tied to the sections it would refresh.

**Retained seed evidence.** All three labeled query rows with their official-docs, repository, and release-notes targets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| search_query_label_name | search_query_text_value |
| --- | --- |
| `official_docs_query_phrase` | planning execution workflow patterns official documentation best practices |
| `github_repository_query_phrase` | planning execution workflow patterns GitHub repository examples |
| `release_notes_query_phrase` | planning execution workflow patterns changelog release notes migration |

## Evidence Boundary Notes

**Decision supported.** This section helps decide how statements in this reference must be labeled so readers know what each claim rests on and how far its evidence reaches. The seed notes define the three labels but ignore this file's specific hazards, unverified time budgets that read like measurements, a backup draft richer than its live successor, and tier files A01 names but this corpus never read.

**Recommended default and causal basis.** Label per claim, mark budget figures as asserted rather than measured, and keep external URLs as unretrieved candidates. Downstream confidence calibrates on these labels, and the budget table quoted without its unstated provenance overstates what the corpus established.

**Operating conditions and assumptions.** Labels stay stable corpus-wide and every combined-inference clause names the inputs it merges. The notes govern labeling in this reference and its reuses, not source ranking, which the hierarchy owns.

**Failure boundary and alternatives.** Labels applied per section rather than per claim let one labeled sentence launder its unlabeled neighbors. Bounded alternatives and recoveries: an explicit asserted-figure tag for the budget table, inline labels parenthetically on quantitative claims, or claim-to-label indexing during verification.

**Counterexample, gotchas, and operational comparison.** Packet and prompt reuse strips labels mechanically, so the budget numbers need their asserted-not-measured context embedded in the same sentence. Good: the batch-of-three default cited as a local fact from executing-plans. Bad: quoting the Feature budget as this repository's measured cost. Borderline: the reviewer-bottleneck scale advice carried as combined inference with its extension note.

**Verification, evidence, and uncertainty.** Sample load-bearing claims, confirm correct labels, and verify quantitative claims carry the asserted-not-measured qualifier. The three seed definitions match the corpus-wide label vocabulary and A01's uncited tables ground the asserted-figure rule. Label durability through packet reuse and prompt quotation is unaudited, so leakage risk remains an assumption.

**Second-order consequence.** This theme's evidence hazard is authority ambiguity, A01 asserts numbers and file tiers with no cited basis, so its claims are local facts about what the doctrine says, never facts about what work actually costs.

**Revision decision.** Add rules marking the time budgets as A01's asserted calibration targets, the draft's staging detail as dated-backup evidence, the tier-file contents as unread, and the scale and portfolio advice as inference beyond the sources.

**Retained seed evidence.** All three label definitions, local fact, external fact, and combined inference, remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- `local_corpus_sourced_fact`: statements tied directly to the local source paths above.
- `external_research_sourced_fact`: statements tied to the public URLs above.
- `combined_evidence_inference_note`: synthesis that combines local and public evidence into agent guidance.
