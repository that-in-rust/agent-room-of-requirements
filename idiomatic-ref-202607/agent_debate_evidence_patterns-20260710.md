# Agent Debate Evidence Patterns

This reference helps an agent decide whether a consequential engineering choice warrants structured debate and, when it does, how evidence should govern the result. Its default is deliberately narrow: use debate when at least two plausible options remain, a wrong choice has meaningful cost, and independent inspection can expose different failure modes. Use direct implementation with tests, one focused reviewer, or a reversible experiment when the change is routine, cheaply reversible, or already governed by one binding project rule.

The output is not a conversation transcript. It is an auditable decision record that names the question, options, evidence, dissent, convergence rule, accountable owner, implementation gate, and recovery path. Debate is successful when it changes or justifies a bounded next action and makes the conditions for reversing that action visible. More participants, more prose, or unanimous language are not success signals by themselves.

This file distinguishes three evidence boundaries throughout: frozen local-corpus facts, facts retrieved from public sources, and synthesis that combines evidence with engineering judgment. The public URLs below are mapped sources, but their current contents were not retrieved during this no-browse evolution pass. Numeric scores and capacity values inherited from the seed are preserved for provenance and explicitly marked when their calibration is unknown.

## Source Evidence Mapping Table

The evidence map is a claim-routing table, not a bibliography. A source earns authority only for claims within its scope, and repeated monthly snapshots do not become independent corroboration merely because they occupy different paths. Start with the local entrypoint designated by the corpus hierarchy, load detail files for the mechanics they own, and use public material only for current ecosystem or instruction-format questions after a permitted freshness check.

| source_location_path_key | source_category_artifact_type | source_authority_confidence_level | source_usage_synthesis_role | claim_scope_and_limit |
| --- | --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202602/agent-debate-01/SKILL.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt | Governs the locally designated debate invocation and workflow surface; read its actual headings before deriving a rule. |
| agents-used-monthly-archive/codex-skills-202602/agent-debate-01/references/debate-template-and-tag-rules.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence | Supports artifact shape and tag semantics; it does not independently prove that debate improves outcomes. |
| agents-used-monthly-archive/codex-skills-202602/agent-debate-01/references/evidence-and-convergence-guardrails.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence | Supports evidence standards, simplicity constraints, behavior, and convergence rules within the local workflow. |
| agents-used-monthly-archive/codex-skills-202602/agent-debate-01/references/repo-workflow-notes.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence | Supports repository workflow and operational limitations; distinguish implementation notes from normative policy. |
| agents-used-monthly-archive/codex-skills-202603/agent-debate-01/SKILL.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt | Historical entrypoint for version comparison; the later month does not automatically override the hierarchy below. |
| agents-used-monthly-archive/codex-skills-202603/agent-debate-01/references/debate-template-and-tag-rules.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence | Historical or supporting template detail; diff against the paired February file before treating repetition as new evidence. |
| agents-used-monthly-archive/codex-skills-202603/agent-debate-01/references/evidence-and-convergence-guardrails.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence | Historical or supporting guardrails; record any semantic conflict instead of silently blending versions. |
| agents-used-monthly-archive/codex-skills-202603/agent-debate-01/references/repo-workflow-notes.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence | Historical or supporting workflow detail; use for change history and bounded comparison. |
| https://developers.openai.com/codex/guides/agents-md | external_research_source_material | external_research_sourced_fact | primary guidance for project instruction files and agent context loading | Candidate source for current Codex instruction-file behavior after retrieval; not direct evidence for debate efficacy. |
| https://agents.md/ | external_research_source_material | external_research_sourced_fact | community format for predictable agent instructions | Candidate ecosystem-format source after retrieval; community convention does not override repository policy. |
| https://github.com/openai/codex | external_research_source_material | external_research_sourced_fact | GitHub implementation and project-level agent guidance | Candidate implementation source after selecting a revision and locator; a repository URL alone supports no behavioral claim. |

**Retrieval sequence**

1. State the exact decision and list the claims that require evidence.
2. Select the smallest local source set whose headings plausibly govern those claims.
3. Verify each path and record file, heading, and version. Compare paired February and March files where the claim could have changed.
4. Add a public source only when freshness or external implementation behavior is material and browsing is permitted.
5. Label every synthesis claim, including its premises and any contradictory source.
6. Stop and escalate when authority remains ambiguous; do not resolve a hierarchy conflict by counting files.

**Counterexample:** citing the AGENTS.md format page to support a convergence threshold is an evidence-category error even if the page is authoritative for instruction files. Conversely, a local archive file can be the governing workflow source while still containing a stale technical example. Locality establishes provenance, not correctness.

**Verification:** paths and exact locators should be inspectable; public retrieval should record date and revision; every actionable recommendation should trace to a row or be marked as bounded inference. A reviewer should be able to remove one source and identify exactly which claims require reconsideration.

## Pattern Scoreboard Ranking Table

The scoreboard preserves the seed's numeric values as internal prioritization metadata. The seed provides no rubric, denominator, benchmark, or derivation, so the values must not be interpreted as percentages, measured effectiveness, or statistically meaningful distances. Operationally, the three patterns form a prerequisite chain.

| pattern_identifier_stable_key | pattern_score_numeric_value | pattern_tier_adoption_level | pattern_failure_prevention_target | dependency_and_interpretation |
| --- | ---: | --- | --- | --- |
| agent_debate_evidence_patterns | 95 | default_adoption_pattern_tier | Source Map First: Load local agent debate material before synthesizing evidence patterns recommendations. | First prerequisite. The value 95 is preserved but uncalibrated; use it as an editorial priority signal only. |
| agent_debate_evidence_patterns | 91 | default_adoption_pattern_tier | Evidence Boundary Split: Separate local facts, external facts, and inference before giving agent instructions. | Second prerequisite. It makes claims from the selected sources distinguishable and updateable. |
| agent_debate_evidence_patterns | 88 | default_adoption_pattern_tier | Verification Gate Coupling: Attach each recommendation to at least one command, checklist, or review gate. | Third prerequisite. A gate is meaningful only after the recommendation and its provenance are clear. |

**Recommended order:** establish the source map, split claim boundaries, then define the falsifying gate. Applying only the last item produces verifiable artifact shape without trustworthy semantics. Applying only the first produces a well-sourced summary that may never control action.

**When to adapt the order:** a task with one binding local policy may begin at boundary labeling because source selection is already settled. A production-risk decision may strengthen verification before consulting public analogues. A source conflict may pause the chain entirely and route to an owner or experiment.

**Alternative:** use an unscored dependency graph or a risk-weighted matrix when numeric labels create false precision. Rank controls by the cost of an untraceable mistake, the reversibility of the pending action, and the independence of available evidence.

**Verification:** sample real decisions and check whether omission of each prerequisite causes a detectable failure. Record the scoring method before comparing this table with another scoreboard. Until such calibration exists, confidence is high in the dependency logic and low in quantitative comparisons among 95, 91, and 88.

## Idiomatic Thesis Synthesis Statement

**local_corpus_sourced_fact:** The frozen local row for agent_debate_evidence_patterns maps eight local source paths. This is an inventory fact, not proof that all eight are independent, current, or equally authoritative.

**external_research_sourced_fact:** The frozen source map identifies three public URLs as possible documentation, format, or implementation analogues. Their current contents were not fetched in this pass, so the map supports future retrieval, not fresh claims about those pages.

**combined_evidence_inference_note:** Reliable use of Agent Debate Evidence Patterns follows a bounded sequence: identify the governing local source, inspect the smallest relevant detail set, compare external evidence only where freshness matters, expose disagreement, make synthesis explicit, and attach a gate that can falsify the pending action.

The operating method is:

1. **Frame:** write one decision question, owner, options, consequence, and reversibility boundary.
2. **Retrieve:** load source material by claim, not by theme breadth.
3. **Classify:** mark local fact, externally retrieved fact, and inference at claim level.
4. **Challenge:** seek contradictory or independent evidence; duplicated wording is not independent support.
5. **Decide:** adopt, adapt, avoid, experiment, or escalate. Unresolved contradiction is a valid result.
6. **Gate:** connect the decision to a command, test, artifact review, rollback condition, or named authority.
7. **Observe:** retain enough evidence to reconstruct why the choice was made and what would invalidate it.

When local and public evidence disagree, do not average them. First determine whether they answer the same claim and whether one has governing authority. If both remain relevant, preserve the contradiction and choose a reversible action or escalation. A source-count majority is not convergence.

This thesis works best for repository-scoped engineering decisions with inspectable evidence and one accountable owner. It is the wrong abstraction for trivial edits, emergency containment that cannot wait, or policy conflicts that only a human authority can resolve. The deeper consequence is that evidence boundaries reduce future maintenance cost: a changed source invalidates identifiable claims rather than forcing a complete reinterpretation of the document.

## Local Corpus Source Map

This map inventories the complete frozen local retrieval surface. It deliberately separates **where to look** from **which source wins**. Heading signals are navigation hints, not substitutes for reading the governed text.

| local_source_filepath_value | local_source_title_text | local_source_heading_signals | local_source_usage_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202602/agent-debate-01/SKILL.md | agent-debate-01 | Agent Debate 01; When To Debate; Workflow; Script Usage; Output Contract; Guardrails | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/codex-skills-202602/agent-debate-01/references/debate-template-and-tag-rules.md | Debate Template and Tag Rules | Debate Template and Tag Rules; Required Sections; Debate: {TOPIC}; Context; Evidence; Relevant Files | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/codex-skills-202602/agent-debate-01/references/evidence-and-convergence-guardrails.md | Evidence and Convergence Guardrails | Evidence and Convergence Guardrails; Evidence Standard; Simplicity Rules; Behavioral Rules; Convergence Rules | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/codex-skills-202602/agent-debate-01/references/repo-workflow-notes.md | Repo Workflow Notes | Repo Workflow Notes; Core Model; Typical Debate Prompts; Upstream CLI Notes; Practical Limitation | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/codex-skills-202603/agent-debate-01/SKILL.md | agent-debate-01 | Agent Debate 01; When To Debate; Workflow; Script Usage; Output Contract; Guardrails | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/codex-skills-202603/agent-debate-01/references/debate-template-and-tag-rules.md | Debate Template and Tag Rules | Debate Template and Tag Rules; Required Sections; Debate: {TOPIC}; Context; Evidence; Relevant Files | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/codex-skills-202603/agent-debate-01/references/evidence-and-convergence-guardrails.md | Evidence and Convergence Guardrails | Evidence and Convergence Guardrails; Evidence Standard; Simplicity Rules; Behavioral Rules; Convergence Rules | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/codex-skills-202603/agent-debate-01/references/repo-workflow-notes.md | Repo Workflow Notes | Repo Workflow Notes; Core Model; Typical Debate Prompts; Upstream CLI Notes; Practical Limitation | reference detail file for deeper pattern evidence |

**Default reading path:** open the locally designated canonical entrypoint; read When To Debate and Workflow; load the template file when constructing the artifact; load convergence guardrails before accepting agreement; and load repository notes before running tools or coordinating writes. Read a paired March file only to inspect change, conflict, or legacy rationale unless the hierarchy is deliberately updated.

**Version protocol:** verify all eight paths, pair like-named February and March files, and compare hashes or semantic changes. Identical content is one evidence lineage with two snapshots. Changed content requires a conflict note stating which claim changed, which role governs, and why. The later month is not automatically normative; the older canonical designation is also not self-justifying.

**Good use:** cite a specific convergence rule from the guardrails file and carry it into the debate artifact. **Bad use:** count eight paths as eight endorsements. **Borderline use:** prefer a March correction only after repository evidence shows the declared hierarchy is stale or claim-specific authority differs.

Confidence is high in the inventory and low in any unstated explanation for the counter-chronological hierarchy. When the rationale cannot be recovered, preserve both readings, avoid irreversible action, and ask the repository owner to decide precedence.

## External Research Source Map

These are mapped future retrieval surfaces. They are adjacent to agent instructions and Codex behavior; they are not direct proof that a debate protocol converges, improves quality, or should use a particular threshold.

| external_source_url_value | external_source_name_text | external_source_usage_role | evidence_boundary_label_value | permitted_claim_scope |
| --- | --- | --- | --- | --- |
| https://developers.openai.com/codex/guides/agents-md | OpenAI Codex AGENTS.md guide | primary guidance for project instruction files and agent context loading | external_research_sourced_fact | Current instruction-file behavior after authorized retrieval and locator capture. |
| https://agents.md/ | AGENTS.md open format | community format for predictable agent instructions | external_research_sourced_fact | Ecosystem format conventions after authorized retrieval; not repository policy. |
| https://github.com/openai/codex | OpenAI Codex repository | GitHub implementation and project-level agent guidance | external_research_sourced_fact | Implementation evidence tied to a selected revision, path, or issue; not a timeless behavioral guarantee. |

**Default:** consult these sources only when the decision turns on current instruction discovery, format, or Codex implementation. Use the local debate corpus for debate invocation, evidence standards, and convergence. If browsing is prohibited or unnecessary, leave public contents explicitly unverified.

**Future freshness protocol:** record query or direct URL, retrieval date, exact revision or page locator, claim supported, conflict with local guidance, and resulting decision change. Search snippets, repository landing pages, and source names are discovery evidence only.

**Failure boundary:** do not use the official status of one source to support a claim outside its topic. Do not infer defect reduction, ideal agent count, or convergence efficacy from an AGENTS.md page. If a public implementation contradicts local workflow guidance, determine whether the conflict concerns capability or policy; capability evidence may require adaptation, while policy remains an owner decision.

The useful second-order role of an external source is falsification. It should challenge a material integration assumption, not merely add another authoritative-looking row.

## Anti Pattern Registry Table

The registry identifies failures that should block or narrow action. Detection must test semantics, not only the presence of labels, paths, or commands.

| anti_pattern_failure_name | failure_cause_risk_reason | safer_default_replacement_pattern | detection_signal_review_method |
| --- | --- | --- | --- |
| context_free_summary_output | agent skips local corpus and produces generic advice | source_map_first_synthesis | Sample actionable claims and require a relevant local locator or explicit reason no local source governs. |
| unsourced_recommendation_claims | guidance appears authoritative without source boundary | evidence_boundary_split_pattern | Check claim-level local, external, or inference labels plus premises and confidence. |
| unverified_agent_instruction | recommendation cannot be checked by command or review gate | verification_gate_coupling | Require a gate that can falsify the recommendation and state what failure changes. |
| irrelevant_source_laundering | a real source is cited for a claim outside its scope | claim_scope_relevance_review | Ask a reviewer to explain the source-to-claim entailment without relying on its title or authority. |
| duplicate_perspective_consensus | agents repeat one source or one underlying argument | independent_evidence_challenge | Compare evidence origins and failure models; repeated wording does not count as independent support. |
| false_convergence_pressure | disagreement is removed to satisfy a completion goal | dissent_disposition_gate | Preserve unresolved dissent and show whether it changed a test, rollback, escalation, or decision. |
| gate_without_semantics | a command passes but does not test the claimed behavior | falsifiable_gate_alignment | State the exact claim invalidated by a nonzero result or failed review criterion. |
| premature_shared_state_change | implementation starts before evidence and convergence gates | evidence_before_mutation_rule | Inspect timestamps or workflow state and stop writes until the decision owner authorizes the bounded action. |

Apply controls at the earliest inexpensive point: source selection for context-free or irrelevant evidence, claim formation for boundary errors, convergence review for duplicated perspectives, and implementation gating for unsafe mutation. A final search for labels is not equivalent to this staged review.

**Negative verification set:** introduce an irrelevant citation, an inference without premises, two agents using the same source, unanimous text with unresolved risk, and a command unrelated to the claim. Each case should fail for the intended reason. If it passes, strengthen the detector before relying on the registry.

Low-risk work may use lighter evidence, but it should not mislabel judgment as fact. The severity of a control can scale; provenance honesty cannot.

## Verification Gate Command Set

The seed-prescribed repository verifier remains part of the evidence set:

~~~bash
python3 agents-used-monthly-archive/idiomatic-references-202606/tools/verify_reference_generation.py --stage final
~~~

For this evolved file and its mandatory packet, the focused acceptance command is:

~~~bash
python3 tests/verify_idiomatic_reference_file.py \
  --path idiomatic-ref-202607/agent_debate_evidence_patterns-20260710.md
~~~

| gate_layer | evidence_required | proves | does_not_prove |
| --- | --- | --- | --- |
| command availability | script path, interpreter, dependencies, and working directory are valid | the intended verifier can execute | that its assertions cover the current editorial contract |
| focused structure | 26 headings remain ordered, every section is longer, packet counts are exact, and forbidden markers are absent | deterministic artifact completeness for this file | that recommendations are relevant or correct |
| corpus integration | shared tests and final repository verifier pass when all owners finish | corpus inventory, ownership, queue, and cross-file invariants | that every inference is well judged |
| editorial audit | sampled source traces, dissent disposition, bounded precision, alternatives, and recovery are reviewed | decision fitness and evidence relevance | universal future correctness |
| operational gate | the selected command, test, experiment, or owner decision changes the pending action | the guidance is executable and falsifiable | that no new evidence will later require reversal |

Capture the exact command, working directory, exit code, count summary, and unresolved failures. A shared test may remain red because other lanes are incomplete; that is not permission to ignore it or to misreport the target file. Record both the focused result and corpus-wide state.

A passing structural verifier is necessary but not sufficient. Conversely, editorial confidence cannot substitute for deterministic heading, length, and packet checks. Completion requires both, followed by a complete reread that checks cross-section consistency.

## Agent Usage Decision Guide

Use this reference only when the unresolved question is consequential, genuinely contested, and evidence-bearing. A theme keyword or one mapped path is a discovery trigger, not automatic permission to launch multiple agents.

**Precondition test**

- State one decision question and one accountable owner.
- Name at least two plausible options or one recommendation with a material challenge.
- Identify what a wrong choice costs and whether the action is reversible.
- Confirm that participants can inspect independent evidence before editing shared state.
- Define what evidence ends the debate, triggers an experiment, or forces escalation.

**Default workflow**

1. Load the smallest authoritative local source set.
2. Write the decision brief and evidence boundaries.
3. Assign independent questions, evidence surfaces, and exclusive write ownership.
4. Require each position to expose assumptions, contrary evidence, and a falsifying condition.
5. Reconcile claims rather than voting on prose.
6. Preserve unresolved dissent and convert it into a gate, rollback, or owner decision.
7. Authorize only the next bounded action; rerun relevant evidence before broader execution.

**Bypass this reference** for a spelling correction, a one-rule compliance edit, a tiny reversible change with adequate tests, open-ended ideation without a pending decision, or emergency containment that must happen immediately. Prefer direct execution, one specialist review, or a disposable experiment.

**Good use:** debate database migration order using schema dependencies, rehearsal results, and rollback critiques. **Bad use:** ask several agents whether a local rename should follow an already binding convention. **Borderline:** for a reversible dependency choice, use one dissenting reviewer unless compatibility evidence genuinely conflicts and a quick integration experiment cannot resolve it.

The success test is compact: the output names the mode selected, evidence used, dissent status, next action, owner, gate, and stop or rollback condition. The aim is the smallest deliberation mechanism capable of exposing the costly unknown.

## User Journey Scenario

The primary user is an agent-system designer or engineering owner who has a concrete workflow decision, mapped local sources, and uncertainty about context loading, tool use, delegation, or verification. The journey begins with ambiguity and ends with either a bounded action or an explicit reason not to act.

| journey_state | user_question | required_artifact | exit_condition |
| --- | --- | --- | --- |
| entry | What decision is actually pending, and who owns it? | one-sentence decision, owner, deadline, and consequence | the question is specific enough that evidence could change an action |
| boundary | What is reversible, forbidden, or governed by policy? | scope, write boundary, rollback boundary, and authority list | irreversible work is blocked until its evidence gate exists |
| options | Which plausible choices or critiques deserve independent treatment? | option set with assumptions and expected failure modes | options differ materially rather than only in wording |
| evidence | Which local and external claims are relevant and current? | ranked source map and claim ledger | each material claim has provenance or is labeled judgment |
| debate | What survives adversarial challenge? | positions, counterarguments, evidence disputes, and dissent | disagreement is resolved, converted into a gate, or escalated |
| convergence | What action is justified now? | decision, rejected options, confidence, owner, and stop rule | owner accepts a bounded action or explicit abstention |
| execution | Did reality support the decision? | fresh command, test, experiment, or review result | gate passes or execution stops and rolls back |
| recovery | What changes after failure or new evidence? | failure class, restored state, changed condition, and next route | the system is safe and the decision record is updated |

A journey that ends after collecting links is incomplete. A journey that reaches implementation without a decision owner is unsafe. A journey that stops at unresolved contradiction can be correct when it preserves state and clearly names the authority or experiment needed next.

Incident response is a boundary case: contain harm first when delay is unsafe, record the temporary decision, then run the evidence workflow before permanent remediation. This reference is optimized for planned engineering work, not for delaying necessary containment.

Verification asks whether an uninvolved reviewer can follow each state transition, reconstruct why the next action was allowed, identify unresolved dissent, and execute the recovery path without reading an entire transcript.

## Decision Tradeoff Guide

Choose among adoption, adaptation, avoidance, and additional evidence by considering authority, task fit, consequence, reversibility, evidence independence, and verification strength.

| decision_option_name | when_to_choose_condition | tradeoff_cost_description | verification_question_prompt |
| --- | --- | --- | --- |
| Adopt when | local authority, task conditions, evidence boundaries, and a falsifiable gate all align | fastest operational path, but can preserve stale assumptions if source versions were not checked | Which governing source, task precondition, and fresh gate justify unchanged use? |
| Adapt when | the core safety properties remain valid but a bounded workflow, version, or scale mismatch is understood | preserves repository fit, but adaptation can hide an invariant or cost more than an experiment | What changed, what was preserved, and what evidence would show the adaptation is wrong? |
| Avoid when | evidence is thin, irrelevant, contradictory without authority, or the task is routine enough that debate adds no information | prevents false confidence, but may delay a decision or require a different reference | What exact failure boundary is active, and which smaller route replaces this reference? |
| Gather evidence when | one cheap, reversible experiment or source check can discriminate between options | spends time before commitment, but may be cheaper than adapting a weak recommendation | What result selects an option, and will the experiment complete before irreversible work? |
| Cost of being wrong | wrong guidance can send an agent to the wrong files, tests, abstraction, owner, or mutation order | includes implementation rework, recovery, lost evidence, coordination delay, and opportunity cost | Can a reviewer identify what to undo, what state to restore, and which assumption failed? |

Do not treat Adapt as the prudent midpoint. If adaptation weakens traceability, dissent, or rollback, Avoid or Gather evidence is safer. Do not treat source agreement as independence when monthly copies share one lineage.

For each decision, record the chosen mode, decisive criteria, rejected modes, current uncertainty, and a change-of-mind trigger. A high-blast-radius choice with weak evidence should shrink the next action even when deadlines favor speed. A tiny reversible action may proceed with a stronger observation gate and less deliberation.

Confidence lies in the structure of the tradeoff, not in a universal numeric threshold. Reversibility and policy can outweigh apparent evidence volume.

## Local Corpus Hierarchy

Classification vocabulary includes canonical, supporting, legacy, duplicate, and conflicting source roles. The frozen hierarchy designates the February skill as canonical and the March skill as legacy despite the chronological order. Preserve that designation, but verify paired changes rather than inventing a rationale.

| local_source_filepath_value | corpus_hierarchy_role | heading_signal_to_convert | reviewer_question_to_answer |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202602/agent-debate-01/SKILL.md | canonical primary source | Agent Debate 01; When To Debate; Workflow | Which invocation or workflow claim does this heading directly govern? |
| agents-used-monthly-archive/codex-skills-202602/agent-debate-01/references/debate-template-and-tag-rules.md | supporting detail source | Debate Template and Tag Rules; Required Sections; Debate: {TOPIC} | Which artifact or tag requirement does this detail add without overriding entrypoint scope? |
| agents-used-monthly-archive/codex-skills-202602/agent-debate-01/references/evidence-and-convergence-guardrails.md | supporting detail source | Evidence and Convergence Guardrails; Evidence Standard; Simplicity Rules | Which evidence, behavior, or convergence rule is needed for the current claim? |
| agents-used-monthly-archive/codex-skills-202602/agent-debate-01/references/repo-workflow-notes.md | supporting detail source | Repo Workflow Notes; Core Model; Typical Debate Prompts | Which repository operation or practical limitation does this source constrain? |
| agents-used-monthly-archive/codex-skills-202603/agent-debate-01/SKILL.md | legacy historical source | Agent Debate 01; When To Debate; Workflow | What changed from the canonical entrypoint, and is the change historical, corrective, or conflicting? |
| agents-used-monthly-archive/codex-skills-202603/agent-debate-01/references/debate-template-and-tag-rules.md | supporting detail source | Debate Template and Tag Rules; Required Sections; Debate: {TOPIC} | Does the paired detail duplicate, extend, or contradict the canonical lineage? |
| agents-used-monthly-archive/codex-skills-202603/agent-debate-01/references/evidence-and-convergence-guardrails.md | supporting detail source | Evidence and Convergence Guardrails; Evidence Standard; Simplicity Rules | Does later guardrail text change a claim that controls action? |
| agents-used-monthly-archive/codex-skills-202603/agent-debate-01/references/repo-workflow-notes.md | supporting detail source | Repo Workflow Notes; Core Model; Typical Debate Prompts | Does later workflow detail expose a limitation absent from the canonical snapshot? |

**Claim-level precedence**

1. Use the canonical entrypoint for invocation and top-level workflow unless higher-priority instructions override it.
2. Use a supporting file for the narrow mechanic it documents.
3. Use legacy material for rationale, version history, and contradiction detection, not automatic policy replacement.
4. Mark identical paired content duplicate rather than corroborating.
5. Mark semantic disagreement conflicting and preserve both claims until authority, experiment, or owner resolves it.

Authority is claim-specific. A supporting guardrail can be the best source for a convergence detail while the canonical entrypoint remains authoritative for when the skill triggers. Likewise, legacy material may contain the best explanation without governing current behavior.

Verification requires path checks, paired diffs, heading locators, and a conflict log. If the older-canonical ordering appears wrong, ask for repository evidence or an owner decision; neither recency nor a label should be rationalized into correctness.

## Theme Specific Artifact

The required artifact is a decision brief with a debate rubric. It is rationale and control state, not a raw transcript.

| artifact_field_name | artifact_completion_rule | evidence_source_hint |
| --- | --- | --- |
| user_goal_statement | state the concrete outcome and why a decision is needed now | user request and local task context |
| decision_question | phrase one choice that evidence can change | user goal plus competing options |
| decision_owner | name who accepts the result and may stop execution | ownership rules and repository authority |
| scope_and_write_boundary | list in-scope systems, exclusive files, prohibited actions, and reversibility | user constraints and repo workflow notes |
| option_and_assumption_set | list plausible options and assumptions without straw alternatives | independent positions and local architecture evidence |
| claim_evidence_ledger | attach boundary label, locator, freshness, and confidence to material claims | local corpus hierarchy plus authorized external retrieval |
| counterargument_record | preserve the strongest objection and evidence against each option | convergence guardrails and adversarial review |
| dissent_disposition | resolve, gate, defer, or escalate every material dissent | evidence and convergence guardrails |
| convergence_rule | state what evidence permits a decision and what prevents one | local convergence rules plus task risk |
| selected_action | authorize only the next bounded implementation or review action | decision tradeoff guide |
| verification_gate_rule | define command, test, experiment, or reviewer criterion and failure response | verification gate command set |
| recovery_and_refresh_rule | name rollback state, escalation owner, and evidence that reopens the decision | failure, retry, and evidence-boundary sections |

**Completion rule:** every material recommendation must be traceable to the claim ledger or marked judgment; every material dissent must affect the choice, a gate, a rollback, or an explicit owner decision. Empty agreement language does not satisfy a field.

**Good artifact:** two migration orders are compared against schema dependencies and rehearsal output; one dissent about rollback becomes an integration gate; the owner authorizes only the rehearsal-backed sequence. **Bad artifact:** all agents agree, no source locators exist, and implementation starts. **Borderline artifact:** a reversible choice uses a shorter brief but retains the decision, evidence, challenge, gate, and rollback.

The artifact externalizes the stopping rule. That makes premature consensus visible and gives future maintainers a precise change-of-mind trigger when evidence or source authority shifts.

## Worked Example Set

Use one scenario to expose the difference among good, bad, and borderline practice: a team must choose whether a database migration should deploy schema compatibility changes before or together with application code.

**Good example**

The owner frames two options and blocks production mutation. One investigator reads local migration and deployment rules; another inspects schema dependencies and backward-compatibility tests; a third challenges rollback assumptions. Each claim has a locator. Evidence shows old application instances may coexist during rollout, so the together option can break readers. A dissent notes that the compatibility phase increases temporary complexity; the group converts that dissent into a cleanup checkpoint rather than erasing it. The owner chooses schema-first compatibility, requires a rehearsal and rollback test, and authorizes only that bounded step. A failed rehearsal reopens the decision.

Why it is good: independent evidence changes the option, disagreement affects gates, convergence is not a vote, and recovery is explicit.

**Bad example**

Four agents receive the prompt "debate the best migration." They all summarize generic zero-downtime practices, cite the same secondary text, and vote for schema-first. No one reads the repository migration code, current deployment topology, or rollback tooling. The majority is called convergence, and production work begins before a rehearsal.

Why it is bad: the decision question is vague, perspectives are duplicated, sources are irrelevant to local behavior, and the gate cannot falsify the choice.

**Borderline example**

The migration affects an isolated disposable environment and can be recreated in minutes. Two plausible sequences remain, but a complete rehearsal will directly reveal compatibility behavior faster than coordinating a full debate. The owner writes a short decision brief, runs both sequences, preserves results, and uses one reviewer to challenge interpretation. Full debate becomes warranted only if results conflict, production topology differs materially, or rollback cannot be demonstrated.

Why it is borderline: the same conceptual uncertainty exists, but a cheap reversible experiment has greater information value than additional discussion.

**Verification exercise:** give the three traces to a reviewer and ask them to identify the decisive evidence, missing control, unresolved risk, and condition that changes the borderline route. If classification depends only on labels such as "good," the examples are not doing useful work.

## Outcome Metrics and Feedback Loops

Metrics should answer whether the reference improves decisions at acceptable cost. They should not reward document length, agent count, apparent unanimity, or fewer questions without checking whether ambiguity was missed.

| metric_or_signal | operational_definition | desired_interpretation | counter-signal_or_limit |
| --- | --- | --- | --- |
| framing_correction_count | material changes to decision, scope, owner, or option set before debate | early corrections can prevent irrelevant evidence gathering | repeated corrections may show poor intake rather than healthy debate |
| unsupported_claims_caught | actionable claims rejected or relabeled before implementation | evidence controls are intercepting risk | fewer claims may reflect shallow analysis |
| pre_action_reversal_count | decisions changed by challenge, source conflict, or experiment before shared-state mutation | debate produced information before rework became expensive | a high rate can indicate weak initial framing |
| gate_failure_rate | bounded actions stopped by their declared verification gate | gates are capable of falsification | too many failures may reveal low-quality decisions |
| downstream_rework_cost | reviewer time and implementation work spent undoing debate-driven choices | should trend down within comparable task classes | task mix and project maturity confound comparison |
| decision_lead_time | elapsed time from framed question to bounded owner decision | measures workflow cost | speed is harmful if dissent or evidence is suppressed |
| unresolved_risk_age | time a material dissent remains without gate, owner, or escalation | exposes forgotten risk | urgent and low-risk items need separate classes |
| clarification_quality | clarifications that changed scope, evidence, or action, not raw question count | fewer redundant and more decisive questions is useful | fewer total questions alone is ambiguous |

Before collection, define task class, numerator, denominator, baseline, owner, review window, and action on adverse movement. For one-off decisions, prefer a qualitative after-action review over decorative percentages.

The feedback loop is: capture the metric packet, review false positives and missed risks, change one workflow control, and sample later comparable decisions. Re-run structural verification after every generated-reference edit. Refresh public evidence only when it is relevant, authorized, and potentially stale.

Confidence is high that unsupported-claim interception and recovery cost matter. No effect size or ideal cadence is established here. A cheap pre-implementation reversal is a positive signal only when it reflects better evidence rather than indecision.

## Completeness Checklist

Each checked item must point to evidence. A statement that the item was considered is not enough.

- The user, concrete goal, pending decision, accountable owner, and urgency are named.
- Scope, exclusive write ownership, prohibited actions, and reversible boundary are explicit.
- At least two plausible options exist, or one recommendation faces a material challenge; routine work is routed elsewhere.
- The smallest relevant local source set was loaded, with file and heading locators.
- Paired monthly sources were deduplicated or compared; conflicts were not silently merged.
- External source contents are either freshly retrieved with date and revision or explicitly unverified.
- Every actionable claim is labeled local fact, retrieved external fact, or bounded inference.
- Inference premises, confidence, and change-of-mind evidence are visible.
- Alternatives include direct execution, targeted review, experiment, deferral, and escalation where relevant.
- Material counterarguments and failure modes are represented without straw treatment.
- Every dissent is resolved, converted into a gate, deferred with owner, or escalated.
- The convergence rule permits abstention and does not rely on vote count alone.
- The selected action is bounded and names owner, command or test, expected evidence, and stop condition.
- Rollback, state restoration, and adjacent routing are actionable.
- Good, bad, and borderline examples expose the condition that changes the decision.
- Metrics pair workflow cost with quality or recovery and state their measurement limits.
- Mechanical packet and heading checks pass, followed by a complete editorial reread.
- Any waiver names item, rationale, risk owner, expiry condition, and compensating control.

Critical omissions in authority, claim traceability, dissent, action gate, or recovery block completion. Low-risk work may use a shorter artifact, but it may not pretend that absent evidence exists.

Sample checked items by following their links or locators. A checklist is reliable only if a deliberately missing critical item causes the reviewer to stop the next action.

## Adjacent Reference Routing

Route to the narrowest source that answers the dominant unresolved question, then return here for integration. Do not load every adjacent reference preemptively.

| dominant_unresolved_question | preferred_destination | expected_output | return_condition |
| --- | --- | --- | --- |
| When should debate trigger and what is its workflow? | agents-used-monthly-archive/codex-skills-202602/agent-debate-01/SKILL.md | invocation and top-level workflow rule | the decision is framed and the correct workflow mode is selected |
| What exact sections and tags belong in the debate artifact? | agents-used-monthly-archive/codex-skills-202602/agent-debate-01/references/debate-template-and-tag-rules.md | inspectable debate record shape | artifact fields can be audited |
| What evidence and convergence behavior is acceptable? | agents-used-monthly-archive/codex-skills-202602/agent-debate-01/references/evidence-and-convergence-guardrails.md | evidence threshold, dissent disposition, and stopping rule | material disagreement is resolved, gated, or escalated |
| How should the workflow operate inside the repository? | agents-used-monthly-archive/codex-skills-202602/agent-debate-01/references/repo-workflow-notes.md | tool, file, ownership, and practical constraints | execution boundaries are known |
| Is an archive version different or stale? | paired 202602 and 202603 local files | semantic diff and conflict record | authority or bounded dual interpretation is documented |
| How does current Codex instruction loading behave? | mapped public documentation or implementation source, only with authorized retrieval | date- and revision-bound external fact | the integration claim is current enough to use |
| Is the main problem context budget, delegation, or verification rather than debate? | the repository's narrower context, subagent, or verification reference after locating its exact path | one specialized control and artifact | this file can integrate the result without broadening scope |

**Loop prevention:** record the pivot question before routing. If the destination does not resolve it, stop after one route and narrow or escalate; do not circulate among generic references. When two topics are tightly coupled, select one integrator and state precedence rather than merging every document.

**Good route:** send convergence mechanics to the guardrails file and bring the resulting stopping rule back into the decision brief. **Bad route:** route the word "agent" to another overview. **Borderline route:** combine context and verification guidance only when the pending decision materially depends on both.

Routing is a context-budget control. It should occur before broad loading, while the current reference remains responsible for final synthesis and ownership.

## Workload Model

**combined_evidence_inference_note:** Treat Agent Debate Evidence Patterns as an agent-workflow operating reference, not as a prose summary. The seed counts below are preserved as planning heuristics, not measured capacity guarantees.

| workload_dimension_name | workload_boundary_value | verification_pressure_point |
| --- | --- | --- |
| primary_usage_surface | agent planning, tool use, context loading, delegation, or skill/plugin execution where bad guidance compounds across long-running sessions | verify that the reference changes the next implementation or review action |
| bounded_capacity_model | one primary task, up to 10 source files, up to 3 delegated subtasks, and a written completion audit for every run; values are uncalibrated heuristics | split or narrow when evidence cannot be ranked, writes collide, or one owner cannot reconcile every result |
| source_pressure_model | local heading signals include Agent Debate 01; When To Debate; Workflow; Script Usage; Output Contract; Guardrails; Debate Template and Tag Rules; Required Sections; Debate: {TOPIC} | compare guidance against canonical local sources before following external examples |
| artifact_pressure_model | required artifact is a debate rubric with convergence criteria, dissent handling, evidence thresholds, owner, gate, and recovery | require the artifact before claiming operational usability |
| coupling_pressure_model | subtasks must have independent evidence surfaces or disjoint write ownership | serialize tightly coupled work and preserve one integration owner |
| side_effect_pressure_model | shared-state or irreversible actions remain blocked until convergence and verification | record mutation order, rollback state, and authorization |

Raw counts are weaker predictors than coupling, evidence-review burden, ownership collision, and rollback complexity. Eleven tiny sources may be easier than four conflicting systems; two agents editing one file are riskier than several agents inspecting disjoint read-only surfaces.

**Split when:** decisions have independent owners or side effects, source discovery is unbounded, the integrator cannot review all evidence, or merge conflicts obscure dissent. **Do not split when:** one safety invariant crosses all options, migration order is tightly coupled, or parallel outputs cannot be reconciled without recreating the full problem.

Record source rank, dependency edges, active writers, tool-call and time budgets, merge owner, unresolved conflicts, and checkpoint state. The practical bottleneck is often reconciliation attention rather than nominal fanout.

## Reliability Target

The seed mixes invariants, provisional targets, and diagnostics. Keep those classes separate so uncalibrated numbers do not acquire the force of policy.

| reliability_target_name | measurable_threshold_value | evidence_collection_method | target_class_and_limit |
| --- | --- | --- | --- |
| source_boundary_preservation | 100 percent of actionable recommendations keep local, external, and inference boundaries visible | sample every actionable recommendation and trace its label and locator before reuse | hard invariant for actionable claims; descriptive low-risk prose may use shared context where unambiguous |
| decision_accuracy_sample | at least 18 of 20 sampled uses route to the correct adopt, adapt, avoid, gather-evidence, or adjacent-reference decision | use labeled downstream tasks and record independent reviewer verdicts | provisional calibration sample, not proof of 90 percent population accuracy |
| unsupported_claim_rate | zero unsupported production, security, latency, or reliability claims in final guidance | reject claims without source row, explicit inference premises, or aligned verification | hard invariant for high-impact claims |
| recovery_path_clarity | every avoid or failure case names rollback, escalation, or next-reference route | inspect failure modes, retries, and adjacent routing together | hard completion property when side effects are possible |
| dissent_disposition_coverage | every material dissent is resolved, gated, deferred with owner, or escalated | audit debate artifact and selected action | hard process invariant; materiality requires reviewer judgment |
| routing_confusion_signal | record cases where reviewers disagree on the proper route | adjudicate disagreements and revise criteria | diagnostic, not a pass threshold |

For empirical targets, define sample frame, task class, adjudicator, denominator, review window, and correction action. Retain raw verdicts so later calibration can change the threshold. Twenty observations are useful for a pilot review but insufficient for broad precision claims.

One hundred percent language can encourage superficial labels, so review relevance as well as presence. Zero unsupported high-impact claims is a normative gate, not a claim that human review will never miss one.

Recovery clarity is a reliability property in its own right. Even if first-choice accuracy does not improve, a precise rollback and escalation path reduces the duration and cost of a wrong decision.

## Failure Mode Table

Classify a failure before retrying. Several modes can cascade, so containment should stop downstream mutation as soon as an upstream evidence or convergence gate fails.

| failure_mode_name | likely_trigger_condition | observable_signal | required_mitigation_action |
| --- | --- | --- | --- |
| source drift hides truth | external or local guidance changes after the reference was written | locator missing, version diff changes a governing claim, or behavior contradicts the map | pause affected action, refresh only when authorized, rerun local hierarchy check, and mark impacted claims stale |
| generic advice escapes review | agent copies plausible practices without theme-specific evidence | recommendations survive after mapped sources are removed | block completion until each material claim has relevant provenance or bounded judgment |
| irrelevant source laundering | authoritative source addresses a different topic | reviewer cannot explain source-to-claim entailment | remove the claim, find a relevant source, or convert it to explicit uncertainty |
| duplicate perspective consensus | agents share one source or failure model | different prose has identical premises and citations | seek independent evidence or reduce the debate to one analysis plus targeted challenge |
| false convergence pressure | completion incentives erase disagreement | dissent disappears without changed evidence, gate, or owner decision | restore dissent, reopen convergence, and prohibit mutation until disposition is explicit |
| context window loses plan | long session forgets scope or user intent | write boundary, owner, or stop condition changes without decision | checkpoint state, reread current spec and user constraints, then resume only the next bounded action |
| tool fanout outruns budget | parallel calls create conflicts, duplicate work, or unbounded external access | overlapping writes, repeated retrieval, rising unresolved merge work | stop new fanout, preserve results, assign one owner per surface, and reconcile before retry |
| ownership ambiguity | multiple actors can authorize or edit the same artifact | conflicting decisions or edits with no accountable resolver | restore exclusive ownership and name one decision integrator |
| gate without semantics | verification passes but does not test the recommendation | reviewer cannot name which claim a failure would falsify | replace or supplement the gate with claim-aligned evidence |
| premature execution | implementation begins before evidence and convergence are complete | shared-state diff predates authorization or unresolved dissent | stop work, restore safe state, audit side effects, and rerun the decision gate |
| evidence access blocked | required source, tool, or authority is unavailable | critical claim remains unsupported after bounded retrieval | narrow to a reversible action, escalate, or abstain rather than invent confidence |
| policy conflict mislabeled technical | agents attempt to solve an authority choice with implementation evidence | both options satisfy technical tests but violate different owner constraints | ask the policy owner; do not continue technical debate as if it can create authority |

After mitigation, reproduce the original signal and rerun only the relevant gate. A cleared symptom is insufficient if the causal failure remains. If modes cascade, contain side effects first, then resolve source and ownership issues before rerunning reasoning.

This taxonomy is high-confidence systems guidance, but its frequency and severity are not measured here. Incident containment may precede full classification when delay is unsafe.

## Retry Backpressure Guidance

Retry is justified only when the next attempt can produce new information. Classify the failure, change one relevant condition, bound the attempt, and preserve side-effect state.

| failure_class | default_retry_policy | changed_condition_required | stop_or_escalate_condition |
| --- | --- | --- | --- |
| transient local tool failure | one bounded retry after confirming the operation is idempotent or read-only | tool availability, timeout, or invocation corrected | second failure or uncertain side effects |
| missing local context | one retry after loading the exact governing source | specific missing locator or dependency added | source remains unavailable or authority conflicts |
| stale external evidence | at most one authorized refresh | retrieval date, revision, or source authority changes | browsing prohibited, result still conflicts, or freshness cannot be established |
| true contradiction | do not repeat the same debate | discriminating experiment, higher authority, or narrowed reversible action | no safe discriminator or owner available |
| ownership or write collision | no parallel retry | exclusive owner and clean merge point restored | overlapping writes cannot be reconciled safely |
| failed verification gate | retry implementation only after diagnosis | code, assumption, or gate alignment changes | repeated failure, rollback incomplete, or new risk appears |
| duplicated perspectives | do not add more copies of the same prompt | independent source, role, or failure model introduced | independence cannot be obtained |
| irreversible or security-sensitive side effect | default to zero automatic retries | explicit human authorization and restored safe state | authorization absent or restoration unverified |

A retry record contains failure class, hypothesis, changed condition, attempt budget, side effects, new evidence, gate outcome, and next stop decision. Checkpoint after each batch and reread current user constraints before broad rewrites, commits, pushes, or destructive operations.

**Bad retry:** run the same prompts again and treat repeated consensus as support. **Good retry:** repair one missing source locator, rerun once, and compare the changed claim ledger. **Borderline:** retry a timeout only before any mutation and only when the operation is known to be safe.

Backpressure protects epistemic quality as well as compute. Repeated low-information outputs can look like convergence while reducing the chance that a contradictory signal receives attention.

## Observability Checklist

Collect enough structured evidence to reconstruct and challenge the decision without storing a raw transcript or sensitive content.

| event_or_field | minimum_record | review_value |
| --- | --- | --- |
| decision_identity | stable decision name, owner, task class, start and stop events | separates comparable runs and preserves accountability |
| scope_state | in-scope systems, exclusive files, prohibited actions, reversibility | reveals boundary drift |
| source_load | local path and heading, external date and revision, intentional skips | supports provenance and freshness review |
| claim_event | atomic claim, boundary label, locator, confidence, conflict status | supports source-to-decision traceability |
| position_event | option, assumptions, strongest counterargument, falsifier | distinguishes independent reasoning from paraphrase |
| dissent_event | unresolved risk, owner, disposition, gate, expiry | prevents silent consensus |
| tool_event | command or tool, purpose, result summary, side effects | reveals fanout, retries, and unsafe mutation |
| verification_event | exact gate, expected result, actual result, interpretation | connects evidence to action |
| retry_event | failure class, changed condition, attempt number, outcome | detects low-information repetition |
| action_event | authorized bounded action, writer, changed paths, rollback state | supports collision and recovery audits |
| completion_event | selected mode, unresolved risks, next action, stop condition | enables handoff without rereading the full run |

Optional performance fields include input size, ranked source count, tool-call count, reviewer time, and repeated-workflow latency. Use p50, p95, or p99 only when enough comparable samples and stable event definitions exist; percentile labels on one run are meaningless.

Minimize evidence: command output summaries, changed-file lists, source locators, and unresolved-risk notes are preferred over raw transcripts. Exclude secrets, private hidden reasoning, and unrelated conversation. Apply repository retention and privacy rules when known.

**Reconstruction test:** give the packet to an uninvolved reviewer. They should be able to identify why the decision was made, what dissent remains, which action was authorized, how to reproduce the gate, and what state to restore on failure. If they cannot, observability is incomplete even when many metrics were collected.

## Performance Verification Method

Performance here means decision-workflow value at acceptable cost, not production service latency unless the debated choice directly concerns such a system.

**One-run audit**

- Record decision start and stop, input size, ranked source count, tool calls, delegated investigations, retries, reviewer time, and side-effect checkpoints.
- Record quality outcomes: unsupported claims caught, material dissent, pre-action reversals, gate failures, and unresolved risk.
- State the baseline or explain why none exists.
- Judge whether the run produced a clearer next action, stronger stop condition, or cheaper recovery than a simpler method.

**Repeated-workflow evaluation**

1. Define comparable task classes and stable start and stop events.
2. Select a baseline such as direct implementation, targeted review, or experiment-first work.
3. Collect enough cases before reporting percentiles; retain sample count and distribution.
4. Pair lead time and reviewer effort with gate failures, downstream rework, and recovery cost.
5. Investigate adverse cases rather than optimizing one aggregate.
6. Change one workflow control and observe later comparable runs.

**Pass condition:** a reviewer can identify the correct next bounded action, evidence gate, owner, and stop condition without unrelated files, and quality guardrails do not worsen merely to improve speed.

**Fail condition:** implementation begins before workload, reliability, and failure boundaries are explicit; speed improves by suppressing dissent; or measured activity cannot be connected to a decision.

Tool-call and timeout budgets are controls, not targets. A slower debate can perform better when it causes a cheap reversal before expensive implementation. For one-off documentation, use wall time and reviewer decision time directly; do not decorate them with percentiles.

No universal performance threshold is asserted. The method is confident about measurement structure and uncertain about values until a local baseline exists.

## Scale Boundary Statement

Agent Debate Evidence Patterns stops being sufficient as one flat workflow when the task spans independent systems, multiple authority owners, unbounded discovery, production mutation without an explicit service objective, or more evidence than one integrator can review.

**Default decomposition:** split by independent decision and ownership boundary, assign one writer per artifact, and preserve one integration owner for shared invariants. Parallel evidence gathering is safe only when write surfaces are disjoint and the merge order is defined.

**Do not split** a tightly coupled migration order, one security invariant, or a policy decision whose alternatives share the same side effects. Delegating pieces can create locally coherent answers that violate the global constraint. In those cases, centralize synthesis while parallelizing read-only evidence collection.

**Required scale artifacts**

- decision dependency graph showing shared assumptions and ordering;
- ownership matrix for evidence, artifacts, authorization, and integration;
- ranked source budget and stop rule for discovery;
- shared-invariant list that every split must preserve;
- merge order and conflict-resolution owner;
- integration tests or review gates across boundaries;
- checkpoint and recovery state for long-running work.

**Example:** API and storage compatibility can be investigated independently, but one migration integrator owns deployment ordering and rollback. Letting both investigators rewrite the same decision record violates the boundary even if their technical work is sound.

Under large-codebase scale, narrow context with dependency or source graphs before debate. A long unranked source list is not context. Under long-running work, treat forgotten ownership, altered scope, or lost dissent as reliability failures and resume from a checkpoint.

There is no universal file or agent count at which scale changes. The practical limit is reached when reconciliation attention and merge contention grow faster than the value of independent evidence.

## Future Refresh Search Queries

No query below was executed during this pass. Future browsing requires authorization, and every result must be captured with retrieval date, authority, exact locator or revision, supported claim, conflicting evidence, and decision impact.

| search_query_label_name | search_query_text_value | claim_the_query_should_test |
| --- | --- | --- |
| official_docs_query_phrase | agent debate evidence patterns official documentation best practices | Discovery query only; narrow it to a named product and behavior before using results. |
| github_repository_query_phrase | agent debate evidence patterns GitHub repository examples | Find candidate implementations, then select a revision and verify behavior locally. |
| release_notes_query_phrase | agent debate evidence patterns changelog release notes migration | Discover changed behavior, then tie the release entry to a mapped claim. |
| instruction_precedence_query_template | site:developers.openai.com Codex AGENTS.md instruction precedence | Test a current instruction-loading assumption using an official domain. |
| implementation_behavior_query_template | repo:openai/codex AGENTS.md discovery precedence | Locate implementation or tests for one behavior and bind evidence to a revision. |
| convergence_counterevidence_query_template | multi-agent debate false convergence evidence software engineering | Seek disconfirming evidence; treat non-primary results as hypotheses, not policy. |
| local_version_refresh_query | compare 202602 and 202603 agent-debate-01 archive files | Establish whether monthly paths duplicate, extend, or conflict without network use. |

A good refresh begins with the most consequential disputed inference, not with the theme name. A bad refresh copies a search summary or counts results. GitHub examples are useful for hypotheses only until code, tests, revision, and local applicability are inspected.

If no authoritative public debate guidance exists, say so. Do not convert the existence of adjacent AGENTS.md or Codex sources into direct debate evidence. Local diffs, controlled experiments, and maintainer authority remain valid alternatives.

## Evidence Boundary Notes

Use evidence labels at claim level and preserve them when content moves into a debate brief, prompt, implementation plan, or review.

- **local_corpus_sourced_fact:** a statement tied to an exact local path, version, and preferably heading or line locator. Local means provenance and possible repository authority; it does not mean infallible or current.
- **external_research_sourced_fact:** a statement tied to a retrieved public URL, date, revision where applicable, and exact locator. A mapped but unfetched URL is not a current external fact.
- **combined_evidence_inference_note:** a recommendation derived from stated premises. List the local and external facts used, conflicting evidence, assumptions, confidence, and a falsifying condition.

**Claim record syntax**

| field | required content |
| --- | --- |
| claim | one material factual or actionable statement |
| boundary | local fact, retrieved external fact, or combined inference |
| locator | file and heading, or URL and revision/date |
| relevance | why the source supports this exact claim |
| confidence | high, medium, or low with a concrete reason |
| conflict | contrary source or explicit none found within the searched scope |
| verification | command, test, experiment, review criterion, or authority decision |
| invalidation | evidence that reopens or reverses the recommendation |

**Good boundary use:** a local convergence rule is cited to its guardrail heading; applying that rule to a migration is separately labeled inference and gated by rehearsal. **Bad boundary use:** an entire multi-source paragraph is labeled local fact. **Borderline:** a section-level label is acceptable only when every sentence shares one source, scope, and confidence.

Principal failure modes are label laundering, missing locators, duplicated sources treated as corroboration, silent conflict resolution, and loss of labels in downstream summaries. Audit by sampling actionable recommendations and requiring an uninvolved reviewer to find source, freshness, premises, conflict status, confidence, verification, and invalidation.

Evidence boundaries function as data lineage for decisions. They make updates and rollback cheaper because a changed source invalidates identifiable claims rather than forcing reviewers to distrust the whole reference.
