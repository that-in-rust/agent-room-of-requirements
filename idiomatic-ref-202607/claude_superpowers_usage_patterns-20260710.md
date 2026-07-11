# Claude Superpowers Usage Patterns

The seed title names the theme but does not define the pre-response decision, platform boundary, recursion stop, or evidence that a skill invocation helped. This section helps decide how an agent should discover and invoke applicable skills before responding or acting without turning the rule into recursive ceremony.

**Recommended default.** Before any response or action, scan available skill descriptions, invoke every requested or plausibly applicable skill through the platform mechanism, follow process skills before implementation skills, and materialize any required checklist. The local using-superpowers rule is explicitly front-loaded because skills change how context is gathered, decisions are framed, and implementation proceeds.

**Operating conditions.** This default works when the skill index is current, invocation tooling exists, trigger descriptions are discriminating, and the skill can run before side effects.

**Failure boundary and recovery.** It becomes blocked when the platform lacks a skill mechanism, instructions conflict with higher-priority constraints, recursive invocation has no terminal condition, or required artifacts are unavailable. The bounded recovery is: Use the platform's documented loading method, ask for a missing required input, or state a concrete tooling blocker; bypass only when no skill has even plausible relevance. Do not force a skill workflow through a blocked boundary.

**Gotchas and counterexample.** Common failures are rationalizing a skip, reading skill files through the wrong mechanism, invoking after action, loading every skill indiscriminately, and confusing invocation with successful application. Good: invoke debugging before investigating a reported failure, then follow its evidence loop. Bad: inspect files first and invoke later. Borderline: invoke a broadly matching skill, inspect its scope, and decline it explicitly when the match is false.

**Verification and confidence.** Verify timestamped order of request, skill scan, invocation, checklist creation, action, and outcome; sample whether the chosen skill changed behavior. The before-response invocation rule, one-percent trigger language, process-skill priority, and checklist requirement are direct local facts. False-positive rate, optimal description granularity, and cross-platform invocation semantics require local measurement.

**Assumptions and second-order consequence.** Assume local instructions are active, higher-priority user and safety constraints still govern, and no skill can authorize prohibited action. Skill compliance is a control-flow property: correct timing and behavioral effect matter more than mentioning a skill.

**Revision outcome.** Add an opening execution contract, platform branches, recursion stop, conflict precedence, and outcome verification.

## Source Evidence Mapping Table

The seed maps two local skill paths and three public URLs but does not reveal that the local files are byte-identical or that public contents were not retrieved. This section helps decide which sources establish binding local skill behavior, platform integration constraints, and optional ecosystem analogues.

**Recommended default.** Treat the canonical and working local paths as one duplicated evidence lineage, use their exact text for local rules, and keep public URLs as unfetched discovery pointers. Duplicate snapshots improve provenance but not independent confidence, while a URL alone cannot support a current behavior claim.

**Retained seed evidence.** The frozen source rows remain for provenance and receive explicit duplicate and retrieval interpretation.

| source_location_path_key | source_category_artifact_type | source_authority_confidence_level | source_usage_synthesis_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/claude-skills-202603/superpowers/using-superpowers/SKILL.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt |
| claude-skills/superpowers/using-superpowers/SKILL.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt |
| https://github.com/davepoon/buildwithclaude | external_research_source_material | external_research_sourced_fact | GitHub collection of Claude skills, agents, commands, hooks, and plugins |
| https://github.com/Cranot/claude-code-guide | external_research_source_material | external_research_sourced_fact | community-maintained guide for Claude Code skills, hooks, plugins, and MCP |
| https://www.claudedirectory.org/blog/claude-code-skills-vs-subagents-vs-mcp | external_research_source_material | external_research_sourced_fact | current public taxonomy for Claude Code extension surfaces |

**Operating conditions.** This source model works when file hashes, headings, versions, retrieval status, and claim scope are recorded.

**Failure boundary and recovery.** It fails when duplicate files are counted twice, community taxonomies override local rules, or link presence is mistaken for reading. The bounded recovery is: Diff local snapshots, inspect platform documentation when authorized, run a controlled invocation trace, or report unresolved platform behavior. Do not force a skill workflow through a blocked boundary.

**Gotchas and counterexample.** Authority inflation, stale working copies, external link drift, and source-category spillover can all produce confident but wrong guidance. Good: use the identical local text for invocation order and one public source only after retrieval for taxonomy. Bad: claim three external confirmations from URLs. Borderline: compare a current platform guide only to test integration.

**Verification and confidence.** Check both file hashes, heading locators, retrieval dates, revision identifiers, source-to-claim relevance, and effect of removing each source. Both local files have SHA-256 07d73726944e38fac59b9c90d876e0f714e395308b357973ae77b1321fc75067 and 95 lines. The mapped public contents and current ecosystem taxonomy were not refreshed.

**Assumptions and second-order consequence.** No public claim becomes current without authorized retrieval, and local duplicate status must remain visible. Source duplication should lower retrieval cost through deduplication, not raise epistemic confidence.

**Revision outcome.** Preserve all five rows while adding deduplication, claim scope, freshness, and authority limits.

## Pattern Scoreboard Ranking Table

The seed assigns 95, 91, and 88 without a scoring rubric and treats three evidence controls as independent ranked patterns. This section helps decide which controls must precede superpowers usage and how the inherited numbers may be used.

**Recommended default.** Apply Source Map First, Evidence Boundary Split, and Verification Gate Coupling as a dependency chain; retain the numbers only as uncalibrated editorial metadata. A skill invocation cannot be verified meaningfully until the governing source and factual boundary are known.

**Retained seed evidence.** The scoreboard rows remain exactly visible and are bounded by an explicit non-empirical interpretation.

| pattern_identifier_stable_key | pattern_score_numeric_value | pattern_tier_adoption_level | pattern_failure_prevention_target |
| --- | ---: | --- | --- |
| `claude_superpowers_usage_patterns` | 95 | default_adoption_pattern_tier | Source Map First: Load local claude superpowers material before synthesizing usage patterns recommendations. |
| `claude_superpowers_usage_patterns` | 91 | default_adoption_pattern_tier | Evidence Boundary Split: Separate local facts, external facts, and inference before giving agent instructions. |
| `claude_superpowers_usage_patterns` | 88 | default_adoption_pattern_tier | Verification Gate Coupling: Attach each recommendation to at least one command, checklist, or review gate. |

**Operating conditions.** The chain works when reviewers need a compact sequence and understand that every control may be required.

**Failure boundary and recovery.** It fails when numeric gaps imply empirical effectiveness, scores compare unrelated references, or high ranking excuses poor trigger fit. The bounded recovery is: Use an unscored prerequisite graph or risk-weighted matrix for trigger, timing, platform, and side-effect controls. Do not force a skill workflow through a blocked boundary.

**Gotchas and counterexample.** False precision, independent adoption of dependent controls, and score-based conformity can hide invocation errors. Good: preserve 95 as source metadata and test ordering behavior. Bad: call it a 95 percent success probability. Borderline: compare scores only after one reproducible rubric exists.

**Verification and confidence.** Publish score derivation, dimensions, evidence, sensitivity, and the exact decision each value changes. The three values and names are frozen seed facts; their prerequisite relationship is a strong inference. No denominator, benchmark, or calibration is supplied.

**Assumptions and second-order consequence.** Treat all inherited numbers as provenance rather than performance. The cost of a missed process skill and the cost of a false positive should determine control strength, not static score distance.

**Revision outcome.** Retain the table, mark scores uncalibrated, and add a trigger-timing dependency model.

## Idiomatic Thesis Synthesis Statement

The seed says local first, public second, and verification-backed decisions but does not explain duplicate local sources, platform branches, or how invocation changes action. This section helps decide how to synthesize binding local skill rules with optional ecosystem evidence into an executable workflow.

**Recommended default.** Deduplicate local copies, obey the local pre-action rule, load the selected skill through the correct platform mechanism, follow its process, and verify behavioral effect before broader action. The local source governs timing and priority, while external material can only clarify current integration after retrieval.

**Retained seed evidence.** The three evidence labels remain, but local duplication and behavioral verification are made explicit.

`local_corpus_sourced_fact`: The local row for `claude_superpowers_usage_patterns` contains 2 source path(s), which should be treated as the first retrieval surface for this theme.
`external_research_sourced_fact`: The external source map provides public documentation, repository, or ecosystem analogues where available.
`combined_evidence_inference_note`: Reliable use of Claude Superpowers Usage Patterns comes from loading the local corpus first, checking public ecosystem guidance second, and converting both into verification-backed agent decisions.

**Operating conditions.** This works when a skill's trigger can be matched to the request, the platform can invoke it, and completion evidence is observable.

**Failure boundary and recovery.** It fails when synthesis averages conflicting authority, a public taxonomy substitutes for local workflow, or invocation is recorded without application. The bounded recovery is: Stop for platform clarification, use a bounded manual equivalent outside Claude Code, or explicitly decline a false-positive skill after reading its scope. Do not force a skill workflow through a blocked boundary.

**Gotchas and counterexample.** Local-first can become duplicate-reading ceremony, invocation can become performative, and external freshness can distract from task evidence. Good: invoke brainstorming before creative implementation and transition according to its gate. Bad: list the skill after coding. Borderline: invoke a one-percent match and reject it with a scoped reason.

**Verification and confidence.** Use an execution ledger linking request signal, selected skill, loaded instructions, required artifact, action order, and outcome. The local rule and priority order are explicit in identical source text. How different platforms expose skill invocation is platform-specific.

**Assumptions and second-order consequence.** Higher-priority safety, user scope, and tool availability remain binding. The thesis is not 'more skills'; it is 'the right process enters control flow before irreversible work.'

**Revision outcome.** Expand the thesis into Discover-Invoke-Apply-Verify with conflict and abstention branches.

## Local Corpus Source Map

The seed lists canonical archive and supporting working paths with the same headings but does not disclose that their bytes are identical. This section helps decide which local copy to load, how to avoid duplicate context, and what authority each path carries.

**Recommended default.** Use the canonical archive for stable provenance or the working copy for active access, verify equality, and load the content once through the platform-prescribed skill mechanism unless a diff appears. Identical files represent one rule set and should not consume context twice or count as corroboration.

**Retained seed evidence.** Both original rows remain so one lineage can be traced across archive and working paths.

| local_source_filepath_value | local_source_title_text | local_source_heading_signals | local_source_usage_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/claude-skills-202603/superpowers/using-superpowers/SKILL.md | using-superpowers | How to Access Skills; Using Skills; The Rule; Red Flags; Skill Priority; Skill Types | skill entrypoint or reusable agent prompt |
| claude-skills/superpowers/using-superpowers/SKILL.md | using-superpowers | How to Access Skills; Using Skills; The Rule; Red Flags; Skill Priority; Skill Types | skill entrypoint or reusable agent prompt |

**Operating conditions.** This works while hashes match, headings remain aligned, and no higher-priority local revision supersedes the archive.

**Failure boundary and recovery.** It fails when copies drift, the working file changes silently, or a path label is mistaken for separate authority. The bounded recovery is: Compare hashes, inspect a semantic diff, select one copy with a recorded reason, or preserve both when conflict is real. Do not force a skill workflow through a blocked boundary.

**Gotchas and counterexample.** Duplicate context can overweight wording, archive recency can be misunderstood, and direct file reads can violate the skill's Claude Code access rule. Good: hash both, invoke one through the Skill tool, and note duplicate provenance. Bad: load both as two votes. Borderline: read directly only in a non-Claude environment whose platform instructions require it.

**Verification and confidence.** Record hashes, headings, selected copy, platform access method, and any semantic diff. The two mapped local files are exactly byte-identical in this workspace. Future working-copy divergence and intended release precedence are not established.

**Assumptions and second-order consequence.** In Claude Code, follow the source's Skill-tool access rule; other environments follow their platform documentation. Deduplication is both a context optimization and an evidence-integrity control.

**Revision outcome.** Add hash-based deduplication, platform access branches, and conflict handling.

## External Research Source Map

The seed lists two GitHub collections and one public comparison article but provides no retrieval dates, revisions, or direct connection to the local mandatory rule. This section helps decide when public material should influence skill taxonomy, packaging, or current integration.

**Recommended default.** Consult public sources only after the local invocation rule is satisfied and only for a named current ecosystem question. Community collections can broaden discovery but cannot override local timing, priority, or access instructions.

**Retained seed evidence.** The public rows remain discovery surfaces rather than newly verified evidence.

| external_source_url_value | external_source_name_text | external_source_usage_role | evidence_boundary_label_value |
| --- | --- | --- | --- |
| https://github.com/davepoon/buildwithclaude | Build with Claude collection | GitHub collection of Claude skills, agents, commands, hooks, and plugins | external_research_sourced_fact |
| https://github.com/Cranot/claude-code-guide | Claude Code guide collection | community-maintained guide for Claude Code skills, hooks, plugins, and MCP | external_research_sourced_fact |
| https://www.claudedirectory.org/blog/claude-code-skills-vs-subagents-vs-mcp | Claude concept comparison | current public taxonomy for Claude Code extension surfaces | external_research_sourced_fact |

**Operating conditions.** This works when browsing is authorized, exact revisions or dates are captured, and findings are tested locally.

**Failure boundary and recovery.** It fails when popularity becomes authority, public taxonomy dictates local workflow, or stale examples are copied. The bounded recovery is: Use local skill manifests, platform docs, controlled tool behavior, or maintainers. Do not force a skill workflow through a blocked boundary.

**Gotchas and counterexample.** Repository branches move, blog taxonomies age, collections mix quality levels, and URLs do not prove content was read. Good: retrieve a current taxonomy to distinguish skill versus subagent after local skill invocation. Bad: replace the local process with a blog. Borderline: use examples as hypotheses for local verification.

**Verification and confidence.** Capture URL, date, revision, passage, supported claim, conflicting local rule, and local test. The URL identities and frozen usage roles are seed facts. No current external content was fetched in this pass.

**Assumptions and second-order consequence.** No unfetched public source supports a current factual claim. External sources are valuable for vocabulary and feasibility; local instructions decide behavior.

**Revision outcome.** Preserve the map with freshness, authority, and non-override rules.

## Anti Pattern Registry Table

The seed lists generic context-free, unsourced, and unverified guidance but omits the local skill's own red flags and misuse modes. This section helps decide which failures should block a response or action in a superpowers workflow.

**Recommended default.** Detect skipped scans, late invocation, wrong access method, process-priority inversion, checklist omission, recursive loops, and performative invocation before action continues. These failures disconnect the mandatory local control from the behavior it is intended to shape.

**Retained seed evidence.** The three seed rows remain and are extended with source-specific anti-patterns.

| anti_pattern_failure_name | failure_cause_risk_reason | safer_default_replacement_pattern | detection_signal_review_method |
| --- | --- | --- | --- |
| context_free_summary_output | agent skips local corpus and produces generic advice | source_map_first_synthesis | verify every listed local path appears in the generated file |
| unsourced_recommendation_claims | guidance appears authoritative without source boundary | evidence_boundary_split_pattern | check for local, external, and inference labels |
| unverified_agent_instruction | recommendation cannot be checked by command or review gate | verification_gate_coupling | require concrete gate in generated reference |

**Operating conditions.** The registry works when each anti-pattern has a timestamped signal, containment, correction, and recheck.

**Failure boundary and recovery.** It fails as word matching when agents mention a skill but do not load or follow it, or when every weak match triggers unbounded work. The bounded recovery is: Use execution-order assertions, checklist audits, negative trigger cases, and bounded false-positive review. Do not force a skill workflow through a blocked boundary.

**Gotchas and counterexample.** Rationalization language, silent tool substitution, recursive 'use skills' invocation, and checklist theater are principal risks. Good: block file exploration until the applicable process skill is invoked. Bad: say 'using debugging' after diagnosis. Borderline: invoke, inspect scope, then decline a false match.

**Verification and confidence.** Test skip, late invocation, wrong tool, process inversion, missing checklist, recursion, and no-behavior-change cases. The source explicitly enumerates rationalization red flags and process priority. Relative prevalence and false-positive cost are not measured.

**Assumptions and second-order consequence.** Controls cannot authorize prohibited actions or supersede higher-priority instructions. The most dangerous violation is often timing: correct content loaded after action cannot govern that action.

**Revision outcome.** Expand the registry with local red flags, timing, platform, recursion, and behavioral-effect detectors.

## Verification Gate Command Set

The seed supplies one archive verifier command but no gate for whether a skill was invoked before action or changed behavior. This section helps decide what evidence proves the reference is valid and a superpowers workflow complied substantively.

**Recommended default.** Layer focused artifact validation, source identity checks, execution-order audit, skill-specific artifact checks, and outcome verification. Reference structure and pre-action process compliance are different claims.

**Retained seed evidence.** The original verifier remains one mechanical layer within a broader compliance argument.

`verification_gate_command_set`: Run the repository verifier after editing this file.

```bash
python3 agents-used-monthly-archive/idiomatic-references-202606/tools/verify_reference_generation.py --stage final
```

**Operating conditions.** This works when timestamps or ordered events are available and each selected skill has explicit outputs or gates.

**Failure boundary and recovery.** It fails when a broad PASS substitutes for invocation evidence, events are reconstructed after the fact, or the skill had no behavioral effect. The bounded recovery is: Use deterministic logs, checklist state, stop-hook assertions, or manual reviewer replay. Do not force a skill workflow through a blocked boundary.

**Gotchas and counterexample.** Wrong working directory, shared-corpus failures, retrospective narration, and unrelated success metrics can create false confidence. Good: prove skill invocation preceded file reads and its checklist drove actions. Bad: run the archive verifier only. Borderline: use equivalent ordered evidence when platform logs are unavailable.

**Verification and confidence.** Capture command, exit, counts, request time, invocation time, first action, required artifacts, deviations, and outcome. The focused validator proves accepted file and packet structure. No generic command can prove every skill-specific behavior.

**Assumptions and second-order consequence.** Shared corpus failures remain separate; private hidden reasoning is not required. Verification must connect ordering evidence to skill-required artifacts and task results.

**Revision outcome.** Retain the seed command and add ordering, application, and outcome gates.

## Agent Usage Decision Guide

The seed triggers on theme or path and repeats generic source-first bullets instead of the local one-percent skill scan and priority workflow. This section helps decide when and how an agent should invoke using-superpowers and then select other skills.

**Recommended default.** At conversation start, scan all available skill descriptions, invoke requested or plausibly relevant process skills first, announce purpose, materialize checklists, then invoke implementation skills as directed. The entry skill exists to change behavior before any response, clarification, exploration, or implementation.

**Retained seed evidence.** The seed usage cues remain as context, then the source-specific workflow governs.

`agent_usage_decision_guide`: Use this reference when a task mentions this theme, one of the listed local source paths, or a nearby technology/workflow surface.

- Start with the local corpus source map.
- Prefer patterns with explicit verification gates.
- Treat external sources as freshness and ecosystem checks, not replacements for local repo conventions.
- Preserve the evidence boundary labels when reusing recommendations.

**Operating conditions.** This works when descriptions are visible, the platform invocation tool is available, and nested skill transitions have explicit terminals.

**Failure boundary and recovery.** It fails when no invocation mechanism exists, the skill requires missing user input, or instructions conflict with higher-priority constraints. The bounded recovery is: Use platform documentation, report the blocker, or explicitly decline an invoked false positive after reading scope. Do not force a skill workflow through a blocked boundary.

**Gotchas and counterexample.** Agents often call simple tasks exempt, explore first, rely on memory, or treat user urgency as permission to skip process. Good: invoke a requested TDD skill before writing tests. Bad: inspect the repo first. Borderline: invoke a weak match and stop it once scope clearly excludes the task.

**Verification and confidence.** Check scan, selected skills, priority order, announcements, checklist tasks, transitions, actions, and final evidence. The trigger and red flags are explicit local rules. Description quality and one-percent judgments vary among agents.

**Assumptions and second-order consequence.** Higher-priority instructions and tool availability remain controlling. The guide optimizes for early process correction, accepting bounded false-positive invocation cost.

**Revision outcome.** Replace generic bullets with a pre-action state machine and bypass criteria.

## User Journey Scenario

The seed describes a generic agent-system designer but omits the message-to-skill-to-artifact-to-action journey. This section helps decide how a user request moves through skill discovery, invocation, process execution, implementation, and verification.

**Recommended default.** Use states for request receipt, skill scan, process invocation, checklist creation, context gathering, implementation-skill transition, action, verification, and recovery. Visible state transitions prevent early actions from outrunning the governing skill.

**Retained seed evidence.** The seed user and trigger remain, but the evolved journey begins at message receipt.

Role based opening scenario: The agent-system designer is starting from a task that needs context selection, tool use, delegation, and verification and needs a reference that turns source evidence into an executable next step.
Primary user starting state: The user has a `claude_superpowers_usage_patterns` task, one or more local source paths, and uncertainty about which pattern should drive implementation.
Decision being made: choosing what context to load, what to offload, when to delegate, and how to prove completion.
Reference opening trigger: Open this file when the task mentions claude superpowers usage patterns, any mapped local source path, or an adjacent workflow with the same failure mode.

**Operating conditions.** The journey works when each state emits an observable artifact and can stop on missing input, conflict, or failed verification.

**Failure boundary and recovery.** It fails when clarification is sent before invocation, context is gathered without process guidance, or handoff loses checklist state. The bounded recovery is: Use a direct platform-blocker journey or a minimal false-positive-decline path. Do not force a skill workflow through a blocked boundary.

**Gotchas and counterexample.** Users may not name the needed skill, multiple skills can overlap, and process skills can demand approval before implementation. Good: request enters brainstorming, gains approved design, then writing-plans and implementation. Bad: code first, explain skill later. Borderline: invoke then ask one required clarification.

**Verification and confidence.** An uninvolved reviewer should reconstruct every transition, selected skill, artifact, owner, and stop condition. The local source explicitly places skill invocation before clarification or action. Specific transitions depend on the invoked skill and platform.

**Assumptions and second-order consequence.** Assume planned work; urgent safety containment may require a separately governed emergency path. A safe journey includes explicit abstention when required skill inputs or tools are missing.

**Revision outcome.** Expand the scenario into ordered states with artifacts, failures, and recovery.

## Decision Tradeoff Guide

The seed offers Adopt, Adapt, Avoid, and Cost of being wrong without addressing the local mandatory rule, false positives, platform differences, or multiple applicable skills. This section helps decide whether to invoke, apply, adapt for platform, decline after inspection, or escalate a skill workflow.

**Recommended default.** Invoke on plausible relevance, apply when scope matches, adapt only the access mechanism for non-Claude platforms, decline explicitly after inspection when false, and escalate conflicts. The local rule intentionally favors early invocation because missed process guidance can invalidate all later work.

**Retained seed evidence.** The generic tradeoff rows remain for continuity and are refined by the mandatory local rule.

| decision_option_name | when_to_choose_condition | tradeoff_cost_description | verification_question_prompt |
| --- | --- | --- | --- |
| Adopt when | local corpus and external evidence agree on the claude superpowers usage patterns pattern | fastest path, but can copy stale local assumptions | Does the selected pattern appear in the canonical source and current external evidence? |
| Adapt when | local sources are strong but public ecosystem guidance has changed | preserves repo fit, but requires explicit inference notes | Did the reference label the local fact, external fact, and combined inference separately? |
| Avoid when | source evidence is thin, conflicting, or unrelated to the user journey | prevents false confidence, but may require deeper research | Is there a confidence warning or adjacent reference route? |
| Cost of being wrong | wrong claude superpowers usage patterns guidance can send an agent to the wrong files, tests, or abstraction | wasted implementation loop and weaker verification | Would a reviewer know what to undo and what to inspect next? |

**Operating conditions.** This model works when invocation is cheap, side effects are delayed, and false positives can terminate cleanly.

**Failure boundary and recovery.** It fails when adaptation weakens mandatory behavior, invocation itself has irreversible side effects, or multiple skills conflict without priority. The bounded recovery is: Actions include Invoke-and-Apply, Invoke-and-Decline, Platform-Adapt, Sequence, Escalate, and Block. Do not force a skill workflow through a blocked boundary.

**Gotchas and counterexample.** Avoid can become rationalization, Adapt can bypass the Skill tool, and invoking every skill can exhaust context. Good: sequence debugging before domain implementation. Bad: avoid because the task seems simple. Borderline: platform-adapt access while preserving before-action timing.

**Verification and confidence.** Record chosen mode, candidate skills, trigger evidence, priority, rejected modes, platform rule, and change-of-mind condition. Early invocation and process priority are binding local guidance. False-positive cost and multi-skill conflict frequency need measurement.

**Assumptions and second-order consequence.** Invocation never overrides safety, user scope, or unavailable-tool reality. The intended asymmetry is explicit: a cheap false positive is preferred to a costly missed process skill, but application still requires scope fit.

**Revision outcome.** Replace generic modes with skill-specific invocation and sequencing choices.

## Local Corpus Hierarchy

The seed calls the archive canonical and the working copy supporting even though both files are byte-identical. This section helps decide which copy governs, how duplicate status affects confidence, and what to do if they diverge.

**Recommended default.** Treat the archive as stable canonical provenance and the working copy as an access mirror; load one copy while hashes match and diff before resolving divergence. Authority can remain canonical while evidence independence remains one lineage.

**Retained seed evidence.** Both hierarchy rows remain, with their authority and duplicate lineage separated.

Classification vocabulary includes canonical, supporting, legacy, duplicate, and conflicting source roles.

| local_source_filepath_value | corpus_hierarchy_role | heading_signal_to_convert | reviewer_question_to_answer |
| --- | --- | --- | --- |
| agents-used-monthly-archive/claude-skills-202603/superpowers/using-superpowers/SKILL.md | canonical primary source | How to Access Skills; Using Skills; The Rule | What guidance, warning, or example should this source contribute to Claude Superpowers Usage Patterns? |
| claude-skills/superpowers/using-superpowers/SKILL.md | supporting context source | How to Access Skills; Using Skills; The Rule | What guidance, warning, or example should this source contribute to Claude Superpowers Usage Patterns? |

**Operating conditions.** This works when hashes and headings match and no newer approved policy source exists.

**Failure boundary and recovery.** It fails when working changes are silently ignored, both copies are counted as votes, or archive status is equated with universal platform authority. The bounded recovery is: Promote an approved working revision, preserve a conflict record, or ask the skill owner to resolve precedence. Do not force a skill workflow through a blocked boundary.

**Gotchas and counterexample.** Recency, path labels, duplicate context, and access-method rules can be conflated. Good: record equality and invoke the working skill once. Bad: cite both as corroboration. Borderline: prefer a newer working revision only after owner approval.

**Verification and confidence.** Check hashes, semantic diff, owner, approval history, selected copy, and platform access mechanism. Current byte identity is directly verified. Future divergence and release policy are not defined by the seed.

**Assumptions and second-order consequence.** No copied file can override higher-priority runtime instructions. Hierarchy answers governance, while deduplication answers evidence weight and context cost.

**Revision outcome.** Add duplicate role, divergence protocol, approval, and one-copy loading guidance.

## Theme Specific Artifact

The seed calls for a worked example with goal, decision, failure, and gate but provides only three generic fields. This section helps decide what artifact proves that a skill was discovered, invoked, applied, and verified at the right time.

**Recommended default.** Create a skill-use execution record containing request signal, candidate skills, selection rationale, invocation event, loaded requirements, checklist, transitions, actions, deviations, gates, and outcome. The record makes timing and behavioral effect inspectable without exposing private hidden reasoning.

**Retained seed evidence.** The seed artifact idea remains and becomes a concrete skill-use trace.

Theme specific artifact: worked claude superpowers usage patterns example with user goal, decision point, failure mode, and verification gate.

| artifact_field_name | artifact_completion_rule | evidence_source_hint |
| --- | --- | --- |
| user_goal_statement | state the user's concrete goal before applying Claude Superpowers Usage Patterns | local corpus hierarchy plus critique findings |
| decision_boundary_rule | define the point where this reference should be used or avoided | decision tradeoff guide |
| verification_gate_rule | define the command, checklist, or review question that proves the artifact worked | verification gate command set |

**Operating conditions.** It works when events are concise, source locators are present, and each required artifact links to the invoked skill.

**Failure boundary and recovery.** It fails when written retrospectively, filled with slogans, or disconnected from actual commands and state. The bounded recovery is: Use a lightweight invocation receipt for simple tasks or a full execution journal for multi-skill workflows. Do not force a skill workflow through a blocked boundary.

**Gotchas and counterexample.** The artifact can become transcript dumping, checklist theater, or post-hoc rationalization. Good: record debugging invocation before reproduction and link the regression test. Bad: note only 'used skill.' Borderline: short record for an invoked-and-declined false positive.

**Verification and confidence.** Audit event order, loaded skill identity, checklist completeness, transition authority, actions, and final gate. Timing, invocation, checklist, and application are directly implied by the local workflow. Artifact detail should scale with risk and duration.

**Assumptions and second-order consequence.** Exclude secrets and hidden reasoning while preserving explicit decision rationale. The artifact is a control-flow trace, not a narrative of internal thought.

**Revision outcome.** Expand three fields into a complete, risk-scaled execution record.

## Worked Example Set

The seed examples are circular and do not show the timing, priority, false-positive, or verification differences. This section helps decide how readers recognize correct, incorrect, and borderline superpowers usage.

**Recommended default.** Use one debugging request across all variants so invocation timing and behavioral effect are directly comparable. Controlled contrast exposes the exact step where process guidance enters or fails to enter control flow.

**Retained seed evidence.** The three example labels remain and gain a shared operational scenario.

Good example: Use Claude Superpowers Usage Patterns after loading the canonical source, confirming the external evidence boundary, and writing a verification gate before implementation.
Bad example: Use Claude Superpowers Usage Patterns as a generic tutorial while ignoring the mapped local paths, source hierarchy, and cost of being wrong.
Borderline case: Use Claude Superpowers Usage Patterns only after adding a confidence warning when local evidence is thin or conflicts with current ecosystem guidance.

**Operating conditions.** Examples work when they include request, candidate scan, chosen skill, invocation time, checklist, action, gate, and outcome.

**Failure boundary and recovery.** They fail when good means merely naming the skill or when borderline has no condition that changes the route. The bounded recovery is: Use a creative-task sequence, code-review sequence, or platform-blocker counterfactual. Do not force a skill workflow through a blocked boundary.

**Gotchas and counterexample.** Examples can overfit one harness, hide tool absence, or imply that invocation guarantees correctness. Good: invoke debugging, reproduce, hypothesize, fix, and regression-test. Bad: patch first and mention debugging later. Borderline: invoke a possible skill, find scope mismatch, and decline before action.

**Verification and confidence.** Ask reviewers to identify first action, governing skill, missing requirement, and condition that flips the borderline case. Good, bad, and borderline contrast is useful. One workflow cannot define every platform transition.

**Assumptions and second-order consequence.** Examples illustrate ordering, not measured defect reduction. Borderline quality depends on whether early invocation cheaply resolves uncertainty before side effects.

**Revision outcome.** Replace circular lines with one trace and two counterfactuals.

## Outcome Metrics and Feedback Loops

The seed measures clarifications and unverifiable claims but not missed skills, false positives, late invocation, checklist adherence, or behavior change. This section helps decide whether superpowers usage improves process compliance and task outcomes at acceptable overhead.

**Recommended default.** Track applicable-skill recall, false-positive invocation, pre-action timing, process-priority adherence, checklist completion, deviations caught, rework, and reviewer effort. Metrics must pair compliance with behavioral and outcome evidence so invocation volume does not become the goal.

**Retained seed evidence.** The seed leading and failure signals remain as secondary diagnostics.

Leading indicator: the next run needs fewer clarifications and produces fewer unverifiable claims.
Failure signal: the reference tells agents what to do without defining context budget or escalation rules.
Review cadence: Re-run the verifier after every generated-reference edit and refresh external sources when public APIs, docs, or tooling releases change.

**Operating conditions.** They work on comparable task classes with labeled applicability, stable event definitions, baselines, and adjudication.

**Failure boundary and recovery.** They fail when agents optimize invocation count, hide false positives, or reduce clarification by skipping needed questions. The bounded recovery is: Use sampled execution audits, qualitative after-action review, or before-and-after rework ledgers. Do not force a skill workflow through a blocked boundary.

**Gotchas and counterexample.** High recall can come from invoking everything, low overhead can come from skipping, and completion rate can hide checklist theater. Good: pair missed-skill rate with rework and false positives. Bad: count invocations alone. Borderline: use reviewer labels while a trigger dataset is built.

**Verification and confidence.** Define sample frame, applicability label, event timing, denominator, adjudicator, baseline, uncertainty, and corrective action. Ordering, recall, false-positive, and outcome measures are logically relevant. No local effect size or ideal threshold is established.

**Assumptions and second-order consequence.** Metrics support review and do not prove causality alone. The optimization target is appropriate process intervention, not maximal skill usage.

**Revision outcome.** Replace generic indicators with a trigger-to-outcome metric chain and counter-signals.

## Completeness Checklist

The seed checks scenario, tradeoffs, hierarchy, artifact, examples, metrics, and routing but omits scan, invocation, priority, checklist, transition, platform, and recursion evidence. This section helps decide whether a skill-use analysis is complete enough to authorize or report action.

**Recommended default.** Require evidence of request signal, candidate scan, selected skills, invocation mechanism, source identity, priority order, checklist, transitions, actions, gates, deviations, and recovery. A complete document cannot compensate for a skill invoked after the behavior it should govern.

**Retained seed evidence.** The original seven coverage items remain and are expanded into evidence-bearing checks.

- The role scenario names the user, starting state, decision, and trigger for Claude Superpowers Usage Patterns.
- The decision guide includes Adopt when, Adapt when, Avoid when, and Cost of being wrong.
- The local corpus hierarchy identifies canonical and supporting sources or gives a confidence warning.
- The theme specific artifact is concrete enough to review without reading every mapped source.
- The examples cover good, bad, and borderline usage.
- The metrics section names one leading indicator and one failure signal.
- The adjacent routing section points to a better reference when this one is not the right fit.

**Operating conditions.** The checklist works when critical omissions block action and waivers name authority, rationale, and compensating control.

**Failure boundary and recovery.** It fails as a memory list, when checked items lack evidence, or when all items have equal severity. The bounded recovery is: Use a schema validator, ordered event assertions, or risk-tiered review. Do not force a skill workflow through a blocked boundary.

**Gotchas and counterexample.** Automation bias, retrospective filling, false-positive concealment, and missing recursion stops create false compliance. Good: link invocation event to checklist and first action. Bad: mark skill complete because its name appears. Borderline: waive a detailed trace for a trivial false-positive decline.

**Verification and confidence.** Delete one critical event and confirm the audit blocks; sample evidence pointers and transition ownership. Scan, timing, priority, application, and verification are core local requirements. Hard-gate detail depends on risk and platform.

**Assumptions and second-order consequence.** Complete means ready for the next bounded action. Checklist order should mirror control flow from request through recovery.

**Revision outcome.** Add skill-specific, temporal, platform, and recursion gates.

## Adjacent Reference Routing

The seed routes generically to claude, superpowers, or usage references without exact questions, destinations, or return conditions. This section helps decide when to route from entry-skill guidance to brainstorming, debugging, planning, TDD, implementation, or platform documentation.

**Recommended default.** Route according to the selected process skill and its explicit transition, keep one workflow owner, and return with the required artifact. Using-superpowers is an entry controller, not a substitute for every domain process.

**Retained seed evidence.** The three broad adjacency cues remain categories rather than actionable destinations.

Adjacent reference guidance: Use debate, subagent, context, or verification references when the task narrows to a specific agent behavior.
Adjacent reference 1: consider the claude adjacent reference when the current task pivots away from claude superpowers usage patterns.
Adjacent reference 2: consider the superpowers adjacent reference when the current task pivots away from claude superpowers usage patterns.
Adjacent reference 3: consider the usage adjacent reference when the current task pivots away from claude superpowers usage patterns.

**Operating conditions.** Routing works when the pivot question, destination skill, precedence, expected artifact, and return condition are explicit.

**Failure boundary and recovery.** It fails when routes are keyword-based, circular, or load every skill into context. The bounded recovery is: Invoke one directly requested skill, inspect one plausible match, or stop for platform documentation. Do not force a skill workflow through a blocked boundary.

**Gotchas and counterexample.** Recursive skill routing, process-skill conflicts, lost checklist state, and generic adjacency loops are principal hazards. Good: route a creative feature to brainstorming, then writing-plans after approval. Bad: route 'Claude' to an overview. Borderline: sequence debugging and TDD under one owner.

**Verification and confidence.** Record pivot, destination, invocation, required artifact, completion signal, return owner, and loop stop. Process-before-implementation priority supports explicit routing. Exact available skills and transitions vary by environment.

**Assumptions and second-order consequence.** Higher-priority instructions and the invoked skill's own terminal state govern. The entry skill should reduce context by selecting the next process, not accumulate all possible processes.

**Revision outcome.** Replace generic adjacency with a process transition matrix and recursion stop.

## Workload Model

The seed inherits one task, ten sources, three subtasks, and a completion audit without calibration and truncates repeated heading signals. This section helps decide how many candidate skills, sources, and delegated actions can be managed without losing priority and checklist state.

**Recommended default.** Bound by trigger ambiguity, skill interaction, context cost, side-effect risk, and one owner's ability to reconcile transitions; treat seed counts as heuristics. A few conflicting process skills can be harder than many independent reference lookups.

**Retained seed evidence.** The workload rows remain inherited heuristics and receive stronger semantic boundaries.

`combined_evidence_inference_note`: Treat Claude Superpowers Usage Patterns as a agent workflow operating reference, not as a prose summary.

| workload_dimension_name | workload_boundary_value | verification_pressure_point |
| --- | --- | --- |
| primary_usage_surface | agent planning, tool use, context loading, delegation, or skill/plugin execution where bad guidance compounds across long-running sessions | verify that the reference changes the next implementation or review action |
| bounded_capacity_model | one primary task, up to 10 source files, up to 3 delegated subtasks, and a written completion audit for every run | split the task or create a narrower reference when this boundary is exceeded |
| source_pressure_model | local heading signals include How to Access Skills; Using Skills; The Rule; Red Flags; Skill Priority; Skill Types; How to Access Skills; Using Skills; The Rule; Red Flags; Skill P | compare guidance against canonical local sources before following external examples |
| artifact_pressure_model | required artifact is worked claude superpowers usage patterns example with user goal, decision point, failure mode, and verification gate | require the artifact before claiming the reference is operationally usable |

**Operating conditions.** The model works for one primary task, a small candidate set, explicit ordering, disjoint delegations, and one completion audit.

**Failure boundary and recovery.** It fails with recursive routing, overlapping process ownership, unbounded discovery, or parallel actions before a governing skill is selected. The bounded recovery is: Use sequential invocation, one process owner with delegated evidence, or split independent tasks after boundaries are explicit. Do not force a skill workflow through a blocked boundary.

**Gotchas and counterexample.** Raw counts hide semantic conflict, duplicate local sources inflate context, and fanout can outrun the entry decision. Good: evaluate two plausible skills, invoke one process owner, and delegate read-only checks. Bad: launch three implementations before selection. Borderline: split only disjoint tasks.

**Verification and confidence.** Record candidate count, source deduplication, dependency order, active writers, context budget, merge owner, and stop. Interaction and reconciliation are meaningful workload boundaries. Ten sources and three subtasks are unvalidated.

**Assumptions and second-order consequence.** One primary task retains one accountable workflow owner. The scarce resource is coherent process ownership, not invocation throughput.

**Revision outcome.** Qualify seed counts, deduplicate signals, and add interaction and recursion limits.

## Reliability Target

The seed mixes universal evidence boundaries, an eighteen-of-twenty routing sample, zero unsupported high-impact claims, and recovery coverage without skill-specific calibration. This section helps decide which superpowers properties are hard invariants, empirical targets, or diagnostics.

**Recommended default.** Make pre-action invocation for applicable skills, correct access, process priority, and recovery hard controls; calibrate applicability and false-positive rates on labeled samples. Normative workflow rules and measured trigger quality require different evidence.

**Retained seed evidence.** The four seed rows remain and gain target classes and calibration limits.

| reliability_target_name | measurable_threshold_value | evidence_collection_method |
| --- | --- | --- |
| source_boundary_preservation | 100 percent of recommendations keep local, external, and inference boundaries visible | review generated text for the three evidence labels before reuse |
| decision_accuracy_sample | at least 18 of 20 sampled uses route to the correct adopt, adapt, avoid, or adjacent-reference decision | sample downstream tasks and record reviewer verdicts |
| unsupported_claim_rate | zero unsupported production, security, latency, or reliability claims in final guidance | reject claims without source row, explicit inference note, or verification method |
| recovery_path_clarity | every avoid or failure case names the rollback, escalation, or next-reference route | inspect failure-mode and adjacent-routing sections together |

**Operating conditions.** Reliability review works when applicability labels, task classes, event order, adjudication, and corrective actions are explicit.

**Failure boundary and recovery.** It fails on tiny samples, superficial skill mentions, or one-hundred-percent language without materiality. The bounded recovery is: Use confidence-banded trigger evaluation, severity-weighted audits, or qualitative process review. Do not force a skill workflow through a blocked boundary.

**Gotchas and counterexample.** Eighteen of twenty implies false precision, high recall can invoke everything, and zero unsupported claims can reward labels. Good: hard-block late required-skill invocation and trend false positives separately. Bad: claim ninety-percent reliability. Borderline: exhaustive tracing only for action-controlling events.

**Verification and confidence.** Retain raw applicability labels, timing events, task class, adjudicator, denominator, uncertainty, and correction. Timing, access, and process priority are explicit local controls. Numeric thresholds lack local baseline.

**Assumptions and second-order consequence.** Targets apply to action-controlling skill decisions. Recovery clarity limits the cost of a missed or misapplied skill even when trigger accuracy is unchanged.

**Revision outcome.** Classify inherited targets and add timing, applicability, priority, and recursion reliability.

## Failure Mode Table

The seed lists source drift, generic advice, context loss, and fanout but omits missed applicability, late invocation, wrong access, priority inversion, recursion, and performative compliance. This section helps decide how to diagnose a failed superpowers workflow and choose a causal mitigation.

**Recommended default.** Classify discovery, applicability, access, timing, priority, application, context, coordination, and verification failures before retrying. Different failures require different corrections; more skill invocations cannot fix wrong ordering, and more prose cannot fix a missing tool.

**Retained seed evidence.** The seed modes remain within a broader causal taxonomy.

| failure_mode_name | likely_trigger_condition | required_mitigation_action |
| --- | --- | --- |
| source drift hides truth | external or local guidance changes after the reference was written | refresh public evidence, rerun local corpus gate, and mark stale claims before reuse |
| generic advice escapes review | agent copies plausible best practices without theme-specific verification | block completion until the verification gate names concrete command, reviewer question, or metric |
| context window loses plan | long-running session forgets early constraints or overwrites user intent | write checkpoint summaries and re-read plan before each destructive step |
| tool fanout outruns budget | parallel actions create conflicts, duplicate work, or unbounded external calls | cap fanout, assign ownership, and require merge/audit checkpoints |

**Operating conditions.** The table works when each mode has an observable event, containment, owner, changed condition, and recheck.

**Failure boundary and recovery.** It fails when all violations are called noncompliance or when platform limitations are treated as agent intent. The bounded recovery is: Stop action, invoke correctly, restore checklist state, choose a different skill, ask for input, or report a platform blocker. Do not force a skill workflow through a blocked boundary.

**Gotchas and counterexample.** Late invocation can look compliant, recursive skill selection can loop, and copied announcements can hide absent application. Good: detect file reads before required debugging invocation and restart from evidence. Bad: add more skills. Borderline: platform-adapt after confirming no Skill tool.

**Verification and confidence.** Reproduce the ordering or artifact failure, apply one causal mitigation, and rerun the exact signal. The source's red flags directly support several failure modes. Frequency and impact need local event data.

**Assumptions and second-order consequence.** Contain urgent safety risk first under higher-priority rules. Timing failures can invalidate otherwise correct downstream work because the process never governed it.

**Revision outcome.** Expand the table with skill-specific, platform, temporal, and recursion failures.

## Retry Backpressure Guidance

The seed allows bounded retries for stale evidence and stops on red gates but does not define retry semantics for skill discovery or invocation. This section helps decide when to rescan, reinvoke, change platform path, stop, or escalate.

**Recommended default.** Retry only after classifying the failure and changing one relevant condition; never repeat the same scan or invocation merely to create apparent compliance. A changed-condition retry adds information, while identical retries consume context and can recurse.

**Retained seed evidence.** The original backpressure bullets remain and gain skill-specific stop conditions.

- Retry only after the failed verification signal is classified as transient, stale evidence, missing context, or true contradiction.
- Use one bounded retry for stale external evidence refresh, then escalate to a human or a narrower source-specific reference.
- Apply backpressure by stopping new generation or implementation work when source coverage, critique coverage, or verification gates are red.
- For long-running agent workflows, checkpoint after each batch and re-read the current spec before any broad rewrite, commit, push, or destructive operation.
- For distributed execution, assign one owner per generated file or theme batch and require merge-time verification of exact path, heading, and evidence-boundary invariants.

**Operating conditions.** This works for transient tool failure, corrected skill index, missing input supplied, or an invocation artifact repaired before side effects.

**Failure boundary and recovery.** It is wrong for higher-priority conflict, unavailable required tool, repeated recursion, or irreversible action already taken. The bounded recovery is: Rollback, restore pre-action state, ask the user, use platform documentation, or report blocked. Do not force a skill workflow through a blocked boundary.

**Gotchas and counterexample.** Parallel retries, repeated announcements, stale skill memory, and post-action reinvocation can amplify confusion. Good: refresh an unavailable skill index once. Bad: invoke using-superpowers recursively. Borderline: one idempotent tool retry before action.

**Verification and confidence.** Record failure class, changed condition, attempt count, state restoration, new evidence, gate result, and stop. Bounded changed-condition retries are sound. Retry count depends on tool semantics and side effects.

**Assumptions and second-order consequence.** One workflow owner can halt retries and identify side effects. Backpressure is the recursion brake that keeps a mandatory entry rule from consuming the task.

**Revision outcome.** Add retry classes for scan, access, invocation, missing input, conflict, and recursion.

## Observability Checklist

The seed records sources, commands, timing percentiles, tool calls, delegation, retries, and compact evidence but omits candidate-skill scan, invocation order, checklist, and transitions. This section helps decide what audit data lets a reviewer reconstruct whether the right skill governed the work.

**Recommended default.** Record request event, candidate skills, trigger evidence, selected skill, access method, invocation, loaded version, checklist, transitions, actions, gates, deviations, retries, and outcome. These events prove control-flow timing without retaining a raw transcript.

**Retained seed evidence.** The original operational telemetry remains and receives control-flow evidence.

- Record which local sources were loaded and which were intentionally skipped.
- Record the exact verification command, reviewer question, or rendered artifact used as proof.
- Record p50/p95/p99 latency or reviewer-time measurements when the reference affects runtime or workflow speed.
- Capture tool-call count, context files loaded, delegated tasks, retry count, and completion-audit outcome.
- Record leading indicator and failure signal from this file in the coverage manifest or journal when the reference drives real work.
- Keep audit evidence small enough to review: command output summary, changed-file list, and unresolved-risk notes are preferred over raw transcript dumps.

**Operating conditions.** It works when event names are stable, clocks or order are reliable, sensitive content is minimized, and evidence is linked.

**Failure boundary and recovery.** It fails when logs contain only announcements, tool counts replace purpose, or failed and declined skills disappear. The bounded recovery is: Use sampled execution audits, compact invocation receipts, or risk-tiered journals. Do not force a skill workflow through a blocked boundary.

**Gotchas and counterexample.** Survivorship bias, secret leakage, retrospective events, and meaningless percentiles are principal risks. Good: record an invoked-and-declined skill with reason. Bad: log only final success. Borderline: omit detailed timing for trivial work but retain order.

**Verification and confidence.** Give the audit to an uninvolved reviewer and ask them to reconstruct scan, invocation, application, deviation, and recovery. Ordered compact evidence is directly relevant. Retention and privacy policies vary.

**Assumptions and second-order consequence.** Exclude secrets, hidden reasoning, and unrelated conversation. Observability should support a counterfactual: what would have happened if the skill had been missed.

**Revision outcome.** Convert the list into a skill-lifecycle event schema and reconstruction test.

## Performance Verification Method

The seed measures budgets, wall time, percentiles, and reviewer time but not avoided process errors, false positives, or rework. This section helps decide whether early skill invocation produces enough process value for its discovery and execution cost.

**Recommended default.** Measure scan and invocation overhead alongside missed-skill incidents, false positives, pre-action corrections, checklist defects caught, rework, and reviewer effort. A slower start can perform better when it prevents an invalid implementation path.

**Retained seed evidence.** The seed measurement packet remains but is paired with process-quality outcomes.

Performance method: require tool-call budgets, timeout budgets, and a resumable journal when the workflow exceeds one focused session.
Leading indicator to measure: the next run needs fewer clarifications and produces fewer unverifiable claims.
Failure signal to watch: the reference tells agents what to do without defining context budget or escalation rules.
Required measurement packet: capture input size, source count, tool-call count, wall-clock time, p50/p95/p99 latency where runtime applies, and reviewer decision time where documentation applies.
Pass condition: the reference must let a reviewer identify the correct next action, verification gate, and stop condition without reading unrelated files.
Fail condition: the reference encourages implementation before the workload, reliability target, and failure-mode table are explicit.

**Operating conditions.** The method works on comparable task classes with labeled applicability, stable events, baselines, and enough samples.

**Failure boundary and recovery.** It fails on one-off percentiles, invocation-count vanity, hidden reviewer effort, or speed gained by skipping process. The bounded recovery is: Use timeboxed audits, qualitative value-of-information review, or before-and-after rework. Do not force a skill workflow through a blocked boundary.

**Gotchas and counterexample.** High recall can be expensive, cheap false positives can accumulate, and outcome differences can reflect task mix. Good: compare early debugging invocation against missed-reproduction rework. Bad: report one wall time. Borderline: use direct timing while building a sample.

**Verification and confidence.** Define task class, applicability, sample, baseline, events, units, exclusions, quality guardrails, and decision. Paired overhead and avoided-error measurement is sound. No universal latency or recall target exists.

**Assumptions and second-order consequence.** Evaluate workflow value rather than production service latency unless directly relevant. Performance means earlier correction of process, not fastest first action.

**Revision outcome.** Separate one-run audit, repeated statistics, and value-of-information interpretation.

## Scale Boundary Statement

The seed warns about multiple systems, owners, discovery, production traffic, context drift, and graph narrowing but not multi-skill orchestration. This section helps decide when one using-superpowers workflow must split and how process authority remains coherent.

**Recommended default.** Split independent tasks only after a governing process skill and ownership boundaries are explicit; centralize shared checklists, safety rules, and final verification. Parallel work can scale evidence collection, but conflicting process skills and shared state need one integrator.

**Retained seed evidence.** The seed scale warnings remain and are translated into process-orchestration rules.

Claude Superpowers Usage Patterns stops being sufficient when the task spans multiple independent systems, more than one ownership boundary, unbounded source discovery, or production traffic without an explicit SLO.
Under distributed execution, split work by theme file and preserve one verification owner per split; do not let parallel agents rewrite the same reference without a merge checkpoint.
Under long-running agent workflows, treat context drift as a reliability failure: checkpoint state, summarize open risks, and verify against the spec before continuing.
Under large-codebase scale, require dependency or source-graph narrowing before applying this reference; a source list without ranked canonical guidance is not enough.

**Operating conditions.** It works when tasks are independent, writes are disjoint, transitions are explicit, and every subtask carries required skill context.

**Failure boundary and recovery.** It fails when skills conflict, tasks share one invariant, delegated agents skip invocation, or source discovery is unbounded. The bounded recovery is: Use centralized process execution, hierarchical coordination, sequential dependencies, or read-only delegation. Do not force a skill workflow through a blocked boundary.

**Gotchas and counterexample.** Subagents can lose parent checklist state, duplicate skill context, or race shared artifacts. Good: one debugging owner delegates independent log reads. Bad: each subagent chooses a different process and edits the same file. Borderline: centralize safety while splitting evidence.

**Verification and confidence.** Produce process dependency graph, ownership matrix, inherited skill context, disjoint-write proof, merge order, and integration gates. One integrator and disjoint writes are strong controls. No universal agent, skill, or source count defines scale.

**Assumptions and second-order consequence.** Parallel work requires explicit process inheritance and exclusive writes. The scale limit is reached when process reconciliation costs more than independent evidence adds.

**Revision outcome.** Add multi-skill orchestration, no-split conditions, delegated compliance, and merge verification.

## Future Refresh Search Queries

The seed gives generic official-docs, GitHub, and release-note searches that are too broad to test a specific superpowers claim. This section helps decide how future authorized research should update platform access or skill taxonomy evidence.

**Recommended default.** Search claim-first for exact platform behavior, skill loading, precedence, hooks, or migration changes after the local rule is identified. Specific queries make public evidence falsifiable and prevent generic ecosystem advice from overriding local instructions.

**Retained seed evidence.** The seed query rows remain discovery labels with stricter use.

| search_query_label_name | search_query_text_value |
| --- | --- |
| `official_docs_query_phrase` | claude superpowers usage patterns official documentation best practices |
| `github_repository_query_phrase` | claude superpowers usage patterns GitHub repository examples |
| `release_notes_query_phrase` | claude superpowers usage patterns changelog release notes migration |

**Operating conditions.** It works when browsing is authorized, the disputed claim is named, and findings include date and revision.

**Failure boundary and recovery.** It fails with broad best-practice queries, snippets, result-count authority, or confirmation bias. The bounded recovery is: Diff local skill copies, inspect platform help, run a controlled invocation, or ask maintainers. Do not force a skill workflow through a blocked boundary.

**Gotchas and counterexample.** Official docs may change, GitHub examples may use different harnesses, and community taxonomies can lag. Good: query current Skill tool invocation semantics. Bad: search 'Claude superpowers best practices.' Borderline: use examples only to form a local test.

**Verification and confidence.** Record query, date, authority, revision, locator, supported claim, conflict, and workflow impact. The source categories are useful discovery surfaces. No queries were executed and future results may differ.

**Assumptions and second-order consequence.** Future browsing requires authorization and local priority remains in force unless legitimately overridden. Research should target platform uncertainty, not relitigate a clear local rule without evidence.

**Revision outcome.** Keep categories but replace generic phrases with claim-oriented templates and capture rules.

## Evidence Boundary Notes

The seed defines local fact, external fact, and combined inference but does not distinguish duplicate sources, platform facts, trigger judgment, invocation events, or outcome inference. This section helps decide how skill-usage claims expose provenance, relevance, confidence, and invalidation.

**Recommended default.** Label local rule, duplicate lineage, retrieved platform fact, observed event, applicability judgment, and outcome inference separately. Claim-level lineage prevents identical files, public taxonomies, or retrospective narratives from laundering compliance.

**Retained seed evidence.** The original three labels remain and are refined for skill-control evidence.

- `local_corpus_sourced_fact`: statements tied directly to the local source paths above.
- `external_research_sourced_fact`: statements tied to the public URLs above.
- `combined_evidence_inference_note`: synthesis that combines local and public evidence into agent guidance.

**Operating conditions.** It works when claims are atomic, locators and event times are present, and labels propagate to journals.

**Failure boundary and recovery.** It fails when a section label covers mixed claims, local provenance implies universal platform behavior, or invocation implies success. The bounded recovery is: Use footnotes, provenance columns, event ledgers, inline keys, or a separate evidence appendix. Do not force a skill workflow through a blocked boundary.

**Gotchas and counterexample.** Duplicate-source inflation, missing timestamps, silent conflict resolution, and downstream label loss are principal risks. Good: label the one-percent rule local fact, skill applicability judgment, and reduced rework inference separately. Bad: label success local fact. Borderline: section labels only for uniform source and scope.

**Verification and confidence.** Sample recommendations and reconstruct source, version, event, relevance, confidence, conflict, gate, and invalidation. The three seed labels are a useful base. Correct labeling cannot prove trigger quality or causation.

**Assumptions and second-order consequence.** Expose explicit rationale, not private hidden reasoning or proof beyond evidence. Evidence boundaries make skill-policy updates and postmortems cheaper by localizing invalidated claims.

**Revision outcome.** Extend boundary syntax to duplicate, platform, event, applicability, and outcome evidence.
