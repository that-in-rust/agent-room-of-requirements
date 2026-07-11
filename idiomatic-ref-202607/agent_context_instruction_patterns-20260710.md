# Agent Context Instruction Patterns

This reference helps an agent decide whether a task needs an explicit context-and-instruction policy, which material belongs in that policy, how conflicting guidance should be resolved, and what evidence must exist before action is called complete. Context is not merely prompt input. It is an engineering dependency: a mistaken source, omitted constraint, or ambiguous precedence rule can influence every later read, tool call, edit, delegation, and completion claim.

**Recommended default.** Restate the user's concrete outcome, identify the controlling instruction scopes, load the smallest authoritative local evidence set that can support the next reversible action, separate direct facts from inference, and define verification plus a stop or escalation condition before broad implementation. "Local first" in this reference means local evidence is the first thematic retrieval surface. It does not mean a local file outranks platform safety rules, direct task constraints, or a more specific applicable instruction.

**Use this reference when.** The task involves repository instructions, context selection, memory or checkpointing, tool planning, delegation, repeated agent work, or a decision that could be distorted by stale or excessive context. The pattern is especially useful when a wrong early assumption could send work to the wrong files or make a verifier prove the wrong property.

**Use a lighter path when.** A tiny, read-only, reversible lookup has one obvious source and one obvious answer. A short note naming the source and check may be enough. Use a stronger domain process when work crosses independent systems, changes production behavior, handles sensitive data, or requires service ownership, rollout, rollback, security review, or an SLO. This reference does not supply those controls by itself.

**Required output.** The operational artifact is a context budget policy. At minimum it records the goal, controlling constraints, included and excluded sources, claim boundaries, conflict decisions, memory or handoff rules, tool and retry limits, verification evidence, owner, and stop condition. A reviewer should be able to reconstruct the next action and its authorization without reading unrelated files or a raw transcript.

**Confidence boundary.** The mapped local file and inherited reference metadata are directly inspectable. The broader workflow is systems guidance derived from those facts and from the seed's declared source roles. The external URLs were cataloged by the seed but were not refreshed during this no-browsing evolution. Numerical scores and capacity values are retained as inherited policy metadata, not presented as measured success rates.

A useful quick test is: "Could a reviewer name what must be loaded, what must be ignored, which instruction wins, what happens next, how failure is detected, and when work stops?" If any answer is missing, context work is not yet operationally complete.

## Source Evidence Mapping Table

The map separates source presence from claim authority. A source may be authoritative for one narrow question and silent on another. Official ownership, local placement, or repository existence does not by itself prove freshness, applicability, or complete coverage.

| source_location_path_key | source_category_artifact_type | source_authority_confidence_level | source_usage_synthesis_role | authority_scope_and_limit | freshness_or_access_state | conflict_response |
| --- | --- | --- | --- | --- | --- | --- |
| unclassified-yet/CLAUDE.md | local_corpus_source_material | local_corpus_sourced_fact | local agent-usable source material | Direct support for this repository's description and explicit Git rules; no direct support for token budgets, sub-agent counts, or general agent architecture | Read locally during this evolution; placement and ownership metadata remain unresolved | Preserve its explicit Git restrictions within scope; search for more specific or higher-priority instructions before broad synthesis |
| https://developers.openai.com/codex/guides/agents-md | external_research_source_material | external_research_sourced_fact | primary guidance for project instruction files and agent context loading | Cataloged as official product guidance; applicability depends on current content and runtime version | Not refreshed because this pass prohibits browsing | Do not add current-product claims from it in this pass; schedule a focused refresh when product behavior matters |
| https://agents.md/ | external_research_source_material | external_research_sourced_fact | community format for predictable agent instructions | Cataloged as an interoperability and format reference, not repository-specific policy | Not refreshed because this pass prohibits browsing | Use only as a future format comparison; local and runtime-specific constraints remain controlling |
| https://github.com/openai/codex | external_research_source_material | external_research_sourced_fact | GitHub implementation and project-level agent guidance | Cataloged for implementation examples and project guidance; a moving repository branch is not a stable compatibility contract | Not refreshed or version-pinned in this pass | Verify installed behavior and version before treating an example as current product behavior |

**How to use the map.**

1. Start with the user's outcome and identify the claim that needs support. Do not start by loading every listed source.
2. Select rows whose authority scope actually covers that claim. A path match or keyword match is only a discovery signal.
3. Record whether each selected source was read, unavailable, intentionally skipped, or cataloged for a later freshness check.
4. Separate source authority from source relevance. A highly authoritative source about syntax may be irrelevant to a repository-specific Git decision.
5. If sources conflict, stop synthesis at the conflicting claim. Apply the runtime's instruction-precedence rules, specificity, version fit, and source ownership; do not average the statements.
6. Mark unsupported space explicitly. One narrow local source cannot silently support the entire theme.

**Good use.** The local file supports "do not push without explicit permission." The agent derives a pre-push approval gate and labels that gate as inference from the local rule. **Bad use.** The agent treats the same file as evidence for a universal three-agent delegation limit. **Borderline use.** An official URL is listed for a current feature but has not been refreshed; it may guide a future search, but it cannot support a new factual claim now.

**Verification.** Check local path existence and the relevant passage, retain retrieval or access state for public material, and sample recommendations back to source rows. Also trace changed sources forward: if a source is revised, every dependent recommendation should be identifiable. The inherited four locations and roles are known; complete local coverage, external freshness, and version compatibility remain uncertain.

## Pattern Scoreboard Ranking Table

The three seed controls form one ordered pipeline. The numeric values are preserved exactly, but the seed provides no rubric, sample, date, scorer, or calibration evidence. Read them as inherited prioritization metadata, not probabilities, percentages, benchmarks, or proof that one control is statistically stronger than another.

| pattern_identifier_stable_key | inherited_pattern_score_numeric_value | pattern_tier_adoption_level | control_name_and_default_action | failure_prevention_target | operational_gate |
| --- | ---: | --- | --- | --- | --- |
| agent_context_instruction_patterns | 95 | default_adoption_pattern_tier | Source Map First: inventory the minimum applicable sources before synthesis | Prevent context-free advice and wrong-source decisions | Every consequential premise resolves to a mapped source or an explicit evidence gap |
| agent_context_instruction_patterns | 91 | default_adoption_pattern_tier | Evidence Boundary Split: keep local fact, external fact, and inference distinguishable | Prevent supported premises from lending false authority to inferred conclusions | Sample claims preserve boundary, scope, freshness, and conflict state |
| agent_context_instruction_patterns | 88 | default_adoption_pattern_tier | Verification Gate Coupling: attach each consequential recommendation to a command, artifact check, reviewer question, or measured outcome | Prevent plausible instructions from escaping review without falsification | Completion evidence names the claim, gate, result, and failure interpretation |

**Recommended adoption.** Use all three controls in order. Mapping without boundary labels can still create overbroad synthesis. Boundary labels without a gate can still produce accurate-looking but inert prose. A gate without correct mapping can verify the wrong source, file, or behavior. The controls are complementary, so the small score differences should not be used to drop one.

**Alternative representation.** If maintainers cannot recover a scoring rubric, required/recommended/optional tiers would be more honest than repeatedly rescoring unexplained numbers. Retaining the values is useful for traceability to the seed, but future changes should include a rubric, task sample, reviewer, date, and reason. Until then, score movement is not evidence of improved reliability.

**Counterexample.** "Source Map First scored 95, so it succeeds 95 percent of the time" is unsupported. Another failure is adopting only Source Map First and calling a long list of URLs complete evidence. A borderline case uses the scores merely to order review but never checks whether the three controls appear downstream; the ranking then organizes attention but does not prevent failure.

**Verification.** For a sample of recommendations, ask: Was the supporting source selected before synthesis? Is the claim boundary visible? Is there a gate capable of disproving the recommendation? Report missing-control count and severity instead of inferring significance from score deltas. What is known confidently is the seed's three names, scores, tiers, and intended failure targets. Score provenance and comparative calibration are unknown.

The second-order consequence is that operational completeness is conjunctive. A workflow with two strong controls and one absent control can be less trustworthy than its average score suggests.

## Idiomatic Thesis Synthesis Statement

**local_corpus_sourced_fact:** The seed maps one local path for agent context instruction patterns. The file was read in this evolution and directly establishes the repository's purpose plus two Git constraints: do not push without explicit permission, and do not place external issue-number references in commit messages.

**external_research_sourced_fact:** The seed catalogs three public sources for official product guidance, a community format, and implementation examples. Their URLs and declared roles are preserved. Their current content was not checked because browsing is prohibited for this pass.

**combined_evidence_inference_note:** Reliable agent-context guidance comes from two separate orderings that must not be confused:

1. **Instruction authority order.** Follow the runtime's platform and safety constraints, direct task constraints, applicable repository instructions, and more specific scoped guidance according to the runtime's documented precedence model. A locally relevant file does not automatically outrank a direct controlling instruction.
2. **Evidence retrieval order.** For repository-specific decisions, load applicable local material before using public analogues. Public sources can test format, compatibility, or freshness, but they do not replace local facts.
3. **Synthesis order.** Express source premises atomically, state the inference that connects them to the recommendation, identify uncertainty or conflict, and attach a falsification gate.
4. **Action order.** Prefer the smallest reversible probe that tests the source model before expensive, broad, parallel, or irreversible work.
5. **Recovery order.** When a gate exposes a context defect, revise source selection or precedence first; repeating implementation under the same defective context only compounds error.

This thesis works when local constraints are relevant, source scopes are clear, and the public evidence addresses a compatible version. It fails when local material is stale, external material is unavailable, a direct user constraint conflicts, or the chosen verifier checks structure rather than the intended behavior. In those cases, bound the claim, stop consequential action, and route the conflict to the appropriate owner or narrower reference.

**Good synthesis.** "The local repository file forbids push without explicit permission. Therefore this task will not push, and any later push requires a new explicit user instruction." The premise is local fact; the task behavior is a bounded inference and direct application. **Bad synthesis.** "All coding agents must always ask before every Git operation." The local source does not establish that universal claim. **Borderline synthesis.** "Use the current public instruction-file format" is not usable here until the public source and installed runtime are checked.

**Verification.** Each consequential conclusion should reveal its local premise, any external premise, the inference, the controlling instruction scope, and a gate. This traceable claim is the core unit of guidance. Source quotations alone are insufficient, while a well-labeled inference can be useful even when evidence is sparse.

## Local Corpus Source Map

The local map contains one source. That is enough to establish a few concrete repository facts, but it is not enough to prove a complete context policy.

| local_source_filepath_value | local_source_title_text | local_source_heading_signals | local_source_usage_role | directly_supported_content | unsupported_or_silent_area | hierarchy_status |
| --- | --- | --- | --- | --- | --- | --- |
| unclassified-yet/CLAUDE.md | CLAUDE.md | CLAUDE.md; What This Repo Is; Git Rules MANDATORY; NEVER push without explicit permission; NEVER reference external issue numbers in commit messages | local agent-usable source material | The repository is a private research knowledge base containing analysis, thesis, and research notes; push requires explicit permission; commit messages must omit external issue-number references | Context size, memory, delegation, retries, source ranking, performance targets, and full instruction precedence | Canonical for its explicit Git rules within this repository; supporting for repository purpose; silent elsewhere; broader file-level canonicality is provisional |

**Claim-scoped reading.** The source's mandatory wording has strong authority within its stated Git scope. It does not acquire authority over unrelated context decisions simply because it is the only mapped file. The directory name unclassified-yet and absence of ownership metadata also counsel against claiming that placement alone proves global canonical status.

**Default discovery sequence.**

1. Read the mapped file, not merely its heading signals.
2. Inspect applicable ancestor and task-local instruction files according to the agent runtime.
3. Look for tooling or documentation that enforces the same rule; implementation enforcement can reveal an operational constraint or a stale document.
4. Classify each claim as canonical, supporting, legacy, duplicate, conflicting, or silent.
5. If a consequential claim has only silence, mark it as inference and add a verification or escalation condition.

**Operational implications.** A task may read, analyze, and edit within its authorized boundaries without asking for push permission because no push is occurring. It must not run push unless the user explicitly authorizes that action. If a commit is explicitly requested, its message should omit patterns such as organization/repository issue references and bare issue numbers. The source does not itself authorize creating a commit.

**Counterexamples.** It is valid to derive a pre-push approval gate from the explicit rule. It is invalid to derive a ten-file context cap from the same document. It is borderline to call the file the repository's complete canonical instruction source without checking whether more specific instructions exist.

**Verification and uncertainty.** Confirm the path, relevant content, and current task scope. Record adjacent sources searched and areas left unsupported. The 23-line content is known. Its maintainer, intended hierarchy across all agent runtimes, freshness process, and completeness are unknown. Sparse evidence should increase discovery and explicit uncertainty, not hidden inference.

## External Research Source Map

The public source map is a catalog for a future browsing-enabled or already-cached evidence check. It is not evidence that the current pages were read in this evolution.

| external_source_url_value | external_source_name_text | external_source_usage_role | evidence_boundary_label_value | decision_it_may_support | decision_it_cannot_set_alone | refresh_record_required |
| --- | --- | --- | --- | --- | --- | --- |
| https://developers.openai.com/codex/guides/agents-md | OpenAI Codex AGENTS.md guide | primary guidance for project instruction files and agent context loading | external_research_sourced_fact | Documented current Codex instruction-file behavior, discovery, and format when checked against the installed version | Repository-specific Git policy, direct task permission, or behavior of another runtime | Access result, retrieval date, relevant section, documented version, installed-version comparison |
| https://agents.md/ | AGENTS.md open format | community format for predictable agent instructions | external_research_sourced_fact | Cross-tool format conventions and interoperability expectations | Product-specific implementation guarantees or this repository's authority hierarchy | Access result, retrieval date, format revision if available, local compatibility finding |
| https://github.com/openai/codex | OpenAI Codex repository | GitHub implementation and project-level agent guidance | external_research_sourced_fact | Implementation examples, repository instructions, and release-linked behavior when pinned | Stable behavior across all versions or a substitute for official documentation | Commit or release pin, inspected path, retrieval date, local behavior check |

**Recommended use.** Consult official documentation for documented behavior, the open format for interoperability, and repository code for implementation examples. Then test applicability locally. If browsing is unavailable or prohibited, preserve the source as a future lead and mark current claims unrefreshed.

**Failure boundaries.** An official page can be current but incompatible with an older runtime. A repository main branch can change after the installed release. A community format can be intentionally broader than one product. These are role differences, not defects. The defect is collapsing them into one undifferentiated authority.

**Good use.** A future refresh records the relevant product version and verifies local behavior. **Bad use.** An agent copies a GitHub example and calls it a guaranteed API. **Borderline use.** An official URL is cited without version comparison; the source may be strong, but applicability remains open.

**Verification.** Record access state, date, section, version, and the exact claim changed or confirmed. Search snippets and URL presence are discovery evidence only. The known facts in this pass are the URLs and inherited roles. Current public content, compatibility, and freshness remain uncertain.

A useful second-order rule is that freshness belongs to evidence identity. "Official documentation" without a retrieval and version state is not the same evidence item as a checked, version-compatible passage.

## Anti Pattern Registry Table

An anti-pattern is operational only when it has a trigger, an observable signal, a consequence, a replacement, and a recovery route. The registry focuses on failures that change the next action or invalidate completion.

| anti_pattern_failure_name | failure_cause_risk_reason | detection_signal_review_method | safer_default_replacement_pattern | containment_and_recovery |
| --- | --- | --- | --- | --- |
| context_free_summary_output | The agent skips local evidence and emits advice that could fit any repository | No mapped local path or task-specific constraint appears in the decision artifact | source_map_first_synthesis | Stop broad action, load the smallest applicable local source set, and restate the decision |
| unsourced_recommendation_claims | A supported premise and an inferred policy are blended into authoritative prose | A reviewer cannot trace the recommendation to a scoped premise and visible inference | evidence_boundary_split_pattern | Split the claim, downgrade unsupported parts, and identify evidence needed to restore confidence |
| unverified_agent_instruction | The recommendation has no check capable of disproving it | Completion notes contain advice but no command, artifact assertion, reviewer question, or outcome | verification_gate_coupling | Add a claim-specific gate and rerun before completion |
| instruction_precedence_inversion | A relevant local source is treated as higher authority than a controlling task or safety constraint | The decision log names sources but not their instruction scopes or conflict disposition | precedence_before_synthesis_rule | Stop consequential action, restore the controlling constraint, and audit affected edits or delegations |
| maximal_context_loading | Every possibly related file is loaded, diluting constraints and increasing contradiction risk | No exclusion rationale; context volume grows without a new decision being enabled | minimum_sufficient_context_policy | Remove low-value sources, summarize settled evidence, and retest whether the next action remains supported |
| stale_source_reuse | A path or URL is reused after content, version, or ownership changed | Retrieval state, digest, version, or date is absent for a freshness-sensitive claim | freshness_record_refresh_gate | Mark dependent claims stale, refresh or bound them, and rerun forward impact review |
| verification_proxy_mismatch | A passing check validates structure while the claimed behavior remains untested | The gate can pass even when the recommendation is false | claim_indexed_verification_gate | Replace or supplement the proxy with a behavioral or semantic check |
| delegation_context_loss | A subtask receives files but not the goal, constraints, acceptance condition, or return contract | Returned work cannot explain which requirement it satisfies or which constraints controlled it | bounded_handoff_contract_pattern | Quarantine the output, reconstruct the handoff, verify independently, and merge only after reconciliation |
| unsafe_action_sequencing | Irreversible mutation begins before permission, evidence, or rollback is established | The action log shows write, commit, push, deploy, or external side effect before the gate | reversible_probe_first_pattern | Stop new side effects, contain or roll back when possible, obtain explicit authorization, and resume from a checkpoint |
| uncalibrated_numeric_authority | Inherited scores or limits are described as measured outcomes | No rubric, sample, denominator, or date supports the number | policy_value_provenance_label | Relabel as a planning target or remove the value until measurement exists |

**Gotcha.** Structural compliance can coexist with semantic failure. A long source map may still be context-free, a citation may be irrelevant to the claim, and an exit-zero verifier may check the wrong corpus. Automated linting should catch missing labels and shapes; scenario review should challenge authority, applicability, and causality.

**Good review.** A reviewer notices that 18-of-20 is a target without a sampling protocol and requests target labeling plus a rubric. **Bad review.** The reviewer only searches for forbidden placeholders. **Borderline review.** All three evidence labels exist, but a mixed sentence still lets a local fact support an unrelated inference.

**Verification.** Test the registry with adversarial examples and, for high-impact rows, a fault-injection or replay exercise. Confirm that detection occurs before completion and that containment plus recovery can be proven. The seed gives no incident frequency, so severity ordering is reasoned judgment and should be calibrated against real failures.

## Verification Gate Command Set

**verification_gate_command_set:** The inherited repository verifier is:

~~~bash
python3 agents-used-monthly-archive/idiomatic-references-202606/tools/verify_reference_generation.py --stage final
~~~

Run it from the repository root. It validates the archived 202606 generated-reference corpus and associated artifacts. It is useful evidence that inherited reference invariants remain intact, but it is not sufficient proof for a dated 202607 working copy or its section question packet.

A complete gate set has four layers:

| gate_layer | purpose | evidence | important_limit |
| --- | --- | --- | --- |
| source_identity_gate | Prove the frozen seed and semantic spans were the intended inputs | Path, line coverage, and source-span hash results | Cannot prove source authority or freshness |
| structural_output_gate | Prove 26 heading texts and order, packet counts, mandatory fields, section growth, and placeholder absence | Focused parser output with exact counts | Cannot prove the prose is useful or coherent |
| semantic_review_gate | Prove defaults, limits, examples, uncertainty, and packet decisions are reconciled | Whole-section and whole-file reviewer checklist | Human judgment can vary; rationale must be explicit |
| repository_regression_gate | Detect broader corpus or tooling regressions | Supplied verifier and project test suite output | Shared-workspace failures may be outside one worker's write boundary |

**Interpretation rules.**

- Record the exact command, exit code, check count, and first actionable failure. "Ran tests" is not evidence.
- A global failure caused by incomplete work in another lane remains a failure of the global suite; do not edit another owner's file or the shared queue to hide it.
- Use the narrowest gate that can disprove each claim. Heading preservation needs a parser comparison; semantic support needs a reviewer trace; output cleanliness needs a byte or pattern check.
- Re-run all affected gates after any repair. Earlier green output does not prove the current bytes.
- If a command is unavailable, record the missing dependency or path and use a clearly labeled alternative. Do not silently replace the claim.

**Good evidence.** "Focused pilot audit: 26 sections, 260 questions, 1,560 fields, all heading comparisons equal, all section lengths greater than seed, zero placeholders; exit 0." **Bad evidence.** "The document is much longer, so it is complete." **Borderline evidence.** The global suite fails because the shared queue remains pending while all pilot-owned checks pass; report both states and the ownership constraint.

Verification is claim-indexed. A command is not a ceremonial final step; it is a chosen attempt to falsify a specific completion statement.

## Agent Usage Decision Guide

**agent_usage_decision_guide:** Use this reference when the task involves agent context instruction patterns, the mapped local path, or an adjacent workflow where source selection, precedence, delegation, memory, or verification can change the implementation decision.

1. **Restate the outcome.** Name the user's concrete result, current phase, allowed mutations, and actions requiring additional approval. Separate discovery-only work from execution.
2. **Find controlling instructions.** Identify runtime, safety, direct task, repository, and more specific scoped instructions. Record conflicts rather than blending them.
3. **Build the minimum source map.** Load sources that can support the next decision. Record why each was included and why plausible sources were excluded or deferred.
4. **Classify claims.** Preserve local_corpus_sourced_fact, external_research_sourced_fact, and combined_evidence_inference_note boundaries. Split mixed claims.
5. **Choose a branch.** Adopt, adapt, pause, avoid, or route according to authority, applicability, freshness, risk, and reversibility.
6. **Write the context budget policy.** Record source, memory, delegation, tool, retry, verification, owner, and stop rules.
7. **Take the smallest reversible probe.** Read, inspect, or run a focused check before broad edits, parallel fanout, or external side effects.
8. **Verify the intended property.** Pair structural checks with semantic review and distinguish pilot-owned evidence from unrelated global state.
9. **Stop or escalate.** Stop when the artifact and gate satisfy the bounded goal. Escalate unresolved authority conflict, missing permission, production risk, or incoherent ownership.

**Lightweight alternative.** For a tiny read-only task, steps 1, 2, 3, and 8 may fit in a short decision note. **Stronger alternative.** Distributed or production work needs explicit owners, dependency mapping, integration gates, rollback, SLOs, and domain review.

**Failure examples.** Keyword overlap alone is not an entry criterion. "Agent" appearing in ten files does not justify loading all ten. Local-first retrieval is not permission to ignore direct task constraints. A verification command is weak if it cannot fail when the recommendation is wrong.

**Verification question set.** Can a reviewer identify the goal, controlling instruction, selected and excluded sources, conflict disposition, evidence labels, chosen branch, next reversible action, gate, stop condition, and adjacent route? If not, the workflow remains incomplete.

The deeper design principle is reversibility. A narrow probe tests the source model at low cost; if it fails, revise context before implementation creates wider state.

## User Journey Scenario

Role based opening scenario: The agent-system designer is starting a repository task that needs context selection, tool use, delegation, and verification. The designer needs a reference that turns source evidence into an executable next step rather than a generic summary.

Primary user starting state: The user has an agent_context_instruction_patterns task, one or more local source paths, explicit write boundaries, and uncertainty about which pattern should drive implementation. Some public sources may be cataloged but unavailable under a no-browsing constraint.

Decision being made: Choose what context to load and exclude, which instruction controls, whether work should remain local or be delegated, what memory must survive a handoff, what action is safe next, and what evidence proves completion.

Reference opening trigger: Open this file when the task names this theme, the mapped local path, or a nearby workflow with the same failure mode. Do not trigger solely because a file contains the word agent.

**End-to-end journey.**

1. The designer states the desired artifact and actions that are prohibited without new permission.
2. The agent reads the complete current file, its seed, applicable instructions, and frozen task metadata before editing.
3. The agent maps direct local facts, catalogs unrefreshed public evidence, and writes explicit inference boundaries.
4. The agent chooses adopt, adapt, pause, avoid, or adjacent routing. An unresolved authority conflict blocks consequential action.
5. The agent creates a context budget policy and, for delegated work, a handoff with one owner and acceptance condition.
6. The agent performs the smallest reversible action, captures evidence, and checks whether the source model predicted the result.
7. On failure, the agent classifies the signal, contains side effects, restores the last known good state, and revises context before retrying.
8. On success, the agent runs focused and broader gates, rereads the complete artifact, and reports residual uncertainty.

**Concrete good path.** A worker assigned one reference reads the local Git rules, does not push, verifies immutable source hashes, creates all section packets, rewrites only owned files, and reports both focused success and global shared-workspace failures. **Bad path.** The worker produces a broad agent tutorial, edits the shared queue, and cites the existence of a verifier without running it. **Borderline path.** The policy is complete but the source hierarchy is disputed; the safe outcome is a pause and owner question, not silent adoption.

**Success condition.** The user can see the changed artifact, exact evidence counts, test state, blocker state, and next assigned work without reconstructing the process. The journey is intentionally recoverable: confidence comes from predictable transitions and bounded rollback, not from maximum context volume.

This scenario assumes repository tooling and inspectable local files. It does not replace incident management, legal review, security approval, or production change control.

## Decision Tradeoff Guide

Choose among branches using authority, applicability, freshness, consequence, reversibility, and verification quality. Source agreement is meaningful only when sources answer the same question for a compatible version.

| decision_option_name | when_to_choose_condition | tradeoff_cost_description | required_evidence | verification_question_prompt | revisit_trigger |
| --- | --- | --- | --- | --- | --- |
| Adopt when | Controlling local constraints, applicable evidence, and the proposed gate agree; the action is bounded and recoverable | Fastest path, but can preserve stale assumptions if freshness was misclassified | Scoped source premises, visible inference, and a gate capable of failing | Does the selected pattern appear in the controlling source and does the current gate test the intended behavior? | Source, version, task scope, or gate changes |
| Adapt when | The core constraint remains valid but mechanism, tooling, version, or public guidance differs | Preserves repository fit, but creates inference that needs explicit ownership and review | Kept constraint, changed mechanism, rejected alternative, and local proof | Are local fact, external fact, and adaptation inference separated? | Adapted mechanism fails or stronger direct evidence appears |
| Pause for evidence | A material question is answerable but evidence, permission, owner, or freshness is temporarily missing | Delays action but avoids encoding uncertainty as policy | Named missing evidence and a bounded acquisition or escalation step | What exact evidence will move this case to adopt, adapt, or avoid? | Evidence arrives or the decision deadline changes |
| Avoid when | Evidence is unrelated, contradictory without a resolver, or the reference lacks required domain controls | Prevents false confidence, but requires a narrower reference or domain process | Conflict record, consequence analysis, and route | Is there a confidence warning, rollback, or adjacent-reference route? | Domain owner resolves conflict or the task is rescoped |
| Cost of being wrong | The guidance could send an agent to wrong files, violate permission, duplicate side effects, or produce unverifiable completion | Includes implementation rework, recovery time, lost trust, and downstream propagation | Blast radius, reversibility, detection latency, and recovery owner | Would a reviewer know what to stop, undo, inspect, and reverify? | New dependency or irreversible action increases consequence |

**Simpler alternative.** For routine work, first split actions into read-only/reversible and mutating/irreversible. Apply more evidence and approval to the latter. **Stronger alternative.** High-consequence work should use a domain risk matrix and named approvers.

**Gotchas.** Adapt is not permission to invent unsupported policy. Avoid is not a substitute for a resolvable evidence pause. Missing evidence is not agreement. Fast completion is not a valid tradeoff when the cost of error includes permission violations or corrupted shared state.

**Verification.** Record the chosen branch, decisive evidence, rejected options, reversibility, error cost, owner, and revisit trigger. The branch vocabulary is a useful inherited structure; its thresholds are contextual judgment.

## Local Corpus Hierarchy

Classification vocabulary includes canonical, supporting, legacy, duplicate, and conflicting source roles. Add two operational qualifiers: provisional when authority is plausible but not confirmed, and silent when a source does not address the claim.

| local_source_filepath_value | corpus_hierarchy_role | claim_scope | heading_signal_to_convert | reviewer_question_to_answer | conflict_or_gap_action |
| --- | --- | --- | --- | --- | --- |
| unclassified-yet/CLAUDE.md | Canonical for explicit Git restrictions; supporting for repository identity; provisional as a file-wide primary source; silent on general context policy | Repository purpose, push permission, and commit-message issue references | CLAUDE.md; What This Repo Is; Git Rules MANDATORY | What exact guidance, warning, or example does this source support, and what does it not support? | Inspect more specific instruction scopes; never use silence to manufacture a policy |

**Hierarchy dimensions.**

- **Authority:** Who or what can set the rule?
- **Specificity:** Does the source govern this path, tool, or action?
- **Freshness:** Is it maintained and current for the task?
- **Applicability:** Does it address the same runtime and decision?
- **Enforcement:** Does tooling or process implement the rule?
- **Conflict state:** Is another applicable source inconsistent?

These dimensions can point in different directions. A highly specific old file may be stale. A current official page may be irrelevant to local Git policy. A generated check may enforce legacy behavior after prose changed. Record the dimensions instead of compressing them into one confidence word.

**Default conflict procedure.** Preserve the conflicting statements, apply documented instruction precedence, prefer more specific applicable local guidance within the same authority level, check ownership and implementation enforcement, and ask the responsible human when a consequential conflict remains. Do not resolve conflict by majority vote or by whichever source is longest.

**Good classification.** The no-push rule is canonical within its action scope; a context budget derived from it is inference. **Bad classification.** Every sentence in the file becomes universal agent policy. **Borderline classification.** The file is provisionally primary because it is the only mapped source, pending discovery of nested or maintained instructions.

**Verification and uncertainty.** Inspect path, content, history or ownership signals when available, references from tooling, and overlapping instructions. The source content and one-path map are known. Complete hierarchy, ownership, and freshness process are not.

The second-order insight is claim-scoped authority. File-level labels are convenient indexes, but reliable synthesis attaches hierarchy to individual claims.

## Theme Specific Artifact

Theme specific artifact: context budget policy for prompt, file, memory, and sub-agent handoff.

The artifact is an allocation and a shedding policy. A maximum without exclusion, compaction, or stop rules encourages an agent to fill available capacity even when added context reduces clarity.

| artifact_field_name | artifact_completion_rule | evidence_source_hint | failure_if_missing |
| --- | --- | --- | --- |
| user_goal_statement | State one concrete outcome, current phase, and actions outside permission | Direct task plus controlling instructions | Context cannot be judged relevant |
| controlling_constraint_ledger | Record platform, task, repository, and scoped constraints plus conflicts | Applicable instruction sources | A relevant source may be mistaken for controlling authority |
| source_inclusion_register | Name each loaded source, claim supported, scope, freshness, and cost | Local corpus hierarchy and source maps | Source volume grows without decision value |
| source_exclusion_register | Name plausible skipped or deferred sources and why | Decision boundary and workload model | Omitted evidence is indistinguishable from accidental neglect |
| evidence_boundary_register | Separate local facts, external facts, inference, and uncertainty | Evidence Boundary Notes | Supported premises can over-authorize conclusions |
| memory_checkpoint_policy | Define what is summarized, persisted, reread, and invalidated after change | Retry and observability guidance | Long-running work loses goal or repeats stale decisions |
| delegation_handoff_contract | Give each subtask goal, owned files, constraints, acceptance evidence, and return shape | Scale and routing guidance | Parallel outputs conflict or cannot be reconciled |
| tool_action_budget | Bound calls by purpose, side effect, timeout, and fanout rather than count alone | Workload and retry guidance | Cost and side effects grow without learning |
| verification_gate_rule | Name focused checks, expected evidence, semantic review, and rerun condition | Verification Gate Command Set | Completion becomes assertion rather than proof |
| stop_escalation_rule | Define success, hard stop, retry eligibility, owner, and adjacent route | Failure and tradeoff guidance | Work loops indefinitely or acts through unresolved conflict |

**Filled operational example.** Goal: evolve one assigned reference and packet. Controlling constraints: three editable paths, no shared CSV edit, no browse, no commit or push. Included sources: spec, tests, working file, archive seed, local mapped instruction, lane journal, assignment manifest. Excluded sources: public URLs because browsing is prohibited; unrelated lane files because ownership is disjoint. Memory: append Green and Refactor checkpoints through the required orchestrator. Delegation: none, because the file is one semantic ownership unit. Tool budget: local reads, patch edits, focused parsers, project tests. Gate: exact 26/260/1,560 counts, heading equality, section growth, placeholder absence, whole-file reread. Stop: report this pilot only; do not start assignment two.

**Alternatives.** A one-step read-only task may use an inline six-line note. A repeated pipeline may justify a machine-readable manifest. Machine readability improves linting and reuse but adds schema migration and can encourage fields to be filled mechanically.

**Verification.** A reviewer should replay source selection, see why exclusions were safe, identify remaining capacity and conflicts, reconstruct every handoff, run the gate, and know who owns escalation. The ideal schema granularity is judgment; the need for explicit allocation, shedding, verification, and recovery follows from the workflow's failure modes.

## Worked Example Set

The examples use the same core scenario so the decisive differences are visible.

**Good example:** A worker must evolve one owned Markdown reference in a shared workspace.

- **Trigger and goal:** One named file plus its packet must be expanded without touching shared queue state.
- **Evidence:** The worker reads the full spec, tests, seed, working copy, journal, assignment manifest, and mapped local instruction. Public sources remain labeled unrefreshed because browsing is prohibited.
- **Decision:** Adopt the section packet method, adapt verification to focused pilot checks, and preserve immutable heading and ownership constraints.
- **Action:** Create all packets before rewriting, edit only three allowed paths, and avoid commit or push.
- **Gate:** Compare headings to the archive; count 26 sections, 260 questions, and 1,560 fields; prove every section is longer; scan placeholders; run project tests and classify unrelated failures.
- **Recovery:** If a heading changes, restore its exact text without changing other agents' work. If global tests fail on pending shared state, report rather than edit the shared CSV.
- **Why good:** Authority, evidence boundaries, reversible action, ownership, proof, and stop condition are all visible.

**Bad example:** The worker sees "agent context" and writes a generic tutorial.

- It does not read the local Git rules, invents current claims from unvisited URLs, treats 95 as a success percentage, adds new headings, and edits queue rows to make tests pass.
- It reports completion because the file is longer and says the verifier should pass.
- **Why bad:** The output may be verbose, but it violates ownership, misstates evidence, cannot be falsified, and has no safe recovery state.

**Borderline case:** The worker creates a thorough policy but finds two applicable local instruction files that disagree about whether a mutating action is allowed.

- Structural checks pass and the action is reversible, but authority ownership is unresolved.
- **Promotion to good:** A documented precedence rule or responsible owner resolves the conflict, the policy records it, and affected gates rerun.
- **Rejection to bad:** The worker silently picks the convenient source or delegates the action without carrying the conflict.
- **Correct interim branch:** Pause for evidence; do not encode the guess as policy.

**Second scenario: stale public guidance.** A public source was previously read but the installed runtime version changed. Good use marks dependent claims stale and runs a version-compatible check. Bad use copies the old behavior. Borderline use retains the claim only as an explicitly bounded inference for a read-only probe.

**Third scenario: context overflow.** Good use summarizes settled evidence, preserves unresolved constraints, and drops low-value files. Bad use appends more documents until the original exclusion is lost. Borderline use delegates independent discovery but lacks a return contract; it becomes good only after ownership and acceptance evidence are added.

Examples are illustrative, not universal templates. A different runtime may use different discovery and precedence mechanics.

## Outcome Metrics and Feedback Loops

Leading indicator: the next comparable run needs fewer avoidable clarifications and produces fewer unverifiable claims while preserving healthy questions about real ambiguity.

Failure signal: the reference tells agents what to do without defining context budget, authority, exclusions, gate, or escalation; or it makes the run faster while increasing rework and late corrections.

| metric_name | operational_definition | collection_method | interpretation_limit | feedback_action |
| --- | --- | --- | --- | --- |
| clarification_rate | Clarification requests divided by comparable tasks, classified as avoidable or ambiguity-revealing | Task journal and reviewer rubric | Fewer questions can indicate overconfidence | If avoidable questions cluster, improve entry criteria or source map; retain healthy uncertainty checks |
| unsupported_claim_rate | Consequential claims lacking source scope, visible inference, or verification divided by sampled consequential claims | Claim audit | A trivial task can make zero easy to achieve | Strengthen claim splitting and evidence-needed notes |
| wrong_source_rework_rate | Tasks requiring correction because the wrong file, version, or authority was used | Diff and incident review | Requires honest causal classification | Improve discovery, hierarchy, and freshness controls |
| gate_quality_rate | Sampled completion gates that could actually fail when the associated claim is false | Adversarial reviewer test | Reviewers may disagree on semantic sufficiency | Replace proxy checks and document expected failure |
| recovery_completeness_rate | Failure cases with containment, rollback or safe state, owner, and rerun proof | Failure-mode audit | Some external side effects are not reversible | Add approval or stronger prevention before action |
| reviewer_decision_time | Time for a reviewer to identify branch, next action, gate, and unresolved risk | Timestamped review sample | Familiarity and task complexity confound trends | Reduce artifact noise; do not delete decisive evidence |
| reconciliation_rework | Changes needed because delegated or section-level outputs conflict at merge | Handoff and merge record | High-complexity tasks naturally cost more | Tighten ownership, return contracts, or split boundaries |

**Measurement protocol.** Define numerator, denominator, comparable task cohort, baseline window, sample count, and reviewer rubric before interpreting a trend. Include failures and near misses, not only successful runs. Pair speed with quality and recovery; otherwise optimization moves work from generation into review.

**Known and uncertain.** These are defensible measures, not observed improvements in the seed. Model changes, task mix, caching, and reviewer learning can dominate results. A single run can illustrate a defect but cannot establish a trend.

**Closed loop.** Every material signal changes policy. Wrong-source rework triggers better discovery or hierarchy. Proxy-gate failure triggers a claim-specific test. Context drift triggers a checkpoint and shedding-rule revision. If a metric is collected but never changes a decision, stop collecting it.

Review cadence: rerun the verifier and focused audit after every generated-reference edit. Refresh public evidence only when a freshness-sensitive claim or failure signal justifies it.

## Completeness Checklist

Use this as an evidence-linked readiness gate, not a topic-presence checklist. For each non-applicable item, record why it cannot affect the current decision.

- [ ] The role scenario names the user, starting state, decision, trigger, prohibited actions, and success state for Agent Context Instruction Patterns.
- [ ] The user's goal is one concrete outcome, and discovery-only versus execution work is explicit.
- [ ] Applicable instruction scopes and precedence are recorded; material conflicts have an owner or a hard stop.
- [ ] Every included source names the claim it supports, scope, freshness state, and retrieval cost.
- [ ] Plausible excluded or deferred sources have a reason; context volume is not treated as completeness.
- [ ] The decision guide includes Adopt when, Adapt when, Pause for evidence, Avoid when, and Cost of being wrong.
- [ ] The local corpus hierarchy identifies canonical, supporting, provisional, silent, legacy, duplicate, or conflicting roles at claim scope.
- [ ] Public sources are either refreshed with version metadata or labeled cataloged and unrefreshed.
- [ ] Local facts, external facts, inference, uncertainty, and conflict remain distinguishable in reused guidance.
- [ ] The theme specific artifact contains source, exclusion, memory, delegation, tool, retry, verification, owner, and stop rules.
- [ ] The examples cover good, bad, and borderline usage and state what moves the borderline verdict.
- [ ] The metrics section defines at least one leading indicator, one failure signal, denominators, and a corrective feedback action.
- [ ] Every consequential recommendation has a gate capable of disproving it, with fresh result evidence.
- [ ] Failure modes include detection, containment, recovery, owner, and post-recovery verification.
- [ ] Retry eligibility includes classification, changed condition, idempotency, side effects, and budget.
- [ ] Observability captures compact decision events without secrets, unnecessary source bodies, or private hidden reasoning.
- [ ] The adjacent routing section resolves a destination trigger, handoff payload, return contract, and fallback.
- [ ] Workload and scale boundaries use coupling, fan-in, ownership, and reversibility, not raw file count alone.
- [ ] Inherited numeric scores and targets are labeled as measured, policy, or unknown; no value gains authority from formatting.
- [ ] Exact heading order, packet counts, section growth, placeholder absence, and whole-file coherence have fresh verification evidence.
- [ ] The final report distinguishes pilot-owned success from global shared-state failures and names the next assigned file without beginning it.

**Author check versus reviewer gate.** The author completes the evidence links and reruns executable checks. A reviewer samples claims, challenges source fit, verifies the branch, and checks whether the gate could fail. Automation can enforce shape; it cannot certify semantic authority.

**Gotcha.** A larger checklist can conceal the highest-risk item. Any unresolved precedence conflict, missing permission for an irreversible action, or unsupported consequential claim blocks readiness even if every low-risk box is checked.

The checklist is complete only when it makes the next action safe and reviewable. Presence of prose is not enough.

## Adjacent Reference Routing

Adjacent reference guidance: Route only the unresolved subproblem and retain one owner for the primary task. A route is complete when it has an entry trigger, handoff payload, expected artifact, and return condition.

| dominant_unresolved_problem | adjacent_reference_category | route_when | handoff_payload | expected_return | return_or_stop_condition |
| --- | --- | --- | --- | --- | --- |
| Evidence or architecture claims materially conflict | debate adjacent reference | Two plausible options remain after source and precedence review | Goal, options, source ledger, disputed claims, constraints, decision deadline | Evidence-based disagreement log and converged or explicitly unresolved decision | Return when the primary owner can choose a branch; stop consequential work if unresolved |
| Work decomposes into independent owned units | subagent adjacent reference | Subtasks do not share mutable files or sequential state | Goal, exact ownership, allowed files, constraints, acceptance checks, return shape | Independently verified result and residual risk | Return for one-owner reconciliation before merge |
| Long-running work risks context loss | context or checkpoint adjacent reference | Work crosses sessions, files, or phase boundaries | Current phase, tests, files in motion, decisions, blockers, exact next step | Resumable checkpoint with non-empty next action | Return after snapshot confirms current state |
| Completion or bug-fix certainty is disputed | verification adjacent reference | A claim lacks fresh falsification evidence | Claim, intended behavior, narrowest command, expected failure and success | Fresh output plus interpretation and remaining test gap | Return only after evidence matches the claim |
| Instruction discovery or precedence is runtime-specific | instruction adjacent reference | The current reference cannot establish product behavior | Runtime, version, candidate files, conflict, desired decision | Version-compatible discovery and precedence rule | Return when local applicability is checked |
| Tool integration or external service behavior dominates | tool or plugin adjacent reference | Context policy is settled but execution depends on a specialized interface | Authorized operation, credentials boundary, schema, side effects, retry policy | Tool-specific plan or result with safe evidence | Stop if access or permission is absent |

Adjacent reference 1: choose the agent or subagent category when decomposition and ownership are the hard problem, not merely because multiple agents are available.

Adjacent reference 2: choose the context or checkpoint category when memory, compaction, or resume reliability is the hard problem.

Adjacent reference 3: choose the instruction or verification category when source precedence or proof is the hard problem.

**Bad route.** "See context docs" provides no resolvable destination or return value. **Borderline route.** Verification is selected, but the underlying issue is an authority conflict; a test cannot decide who may set policy. **Fallback.** If no exact adjacent file can be resolved, keep the issue in the primary artifact, state the missing capability, and escalate to the owner rather than inventing a destination.

The return contract prevents specialization from fragmenting state. Returned guidance must be reconciled against the original goal and constraints before the primary task can complete.

## Workload Model

**combined_evidence_inference_note:** Treat Agent Context Instruction Patterns as an agent workflow operating reference, not as a prose summary. The inherited counts below are conservative planning guardrails, not empirically measured capacity limits.

| workload_dimension_name | workload_boundary_value | verification_pressure_point | split_or_escalation_signal |
| --- | --- | --- | --- |
| primary_usage_surface | Agent planning, tool use, context loading, delegation, or skill/plugin execution where bad guidance compounds across a long session | Verify that the reference changes the next implementation or review action | The artifact only summarizes information and cannot identify a safe next action |
| bounded_capacity_model | Start with one primary task, up to 10 source files, up to 3 delegated subtasks, and one written completion audit | Record actual source sizes, task coupling, delegation fan-in, and review burden | Exceeding a count is a review trigger, not automatic failure; split when coherent ownership or reconciliation is lost |
| source_pressure_model | Local heading signals include CLAUDE.md; What This Repo Is; Git Rules MANDATORY; NEVER push without explicit permission; NEVER reference external issue numbers in commit messages | Compare guidance against complete applicable local sources before external analogues | Sources are unbounded, too large, version-conflicted, or selected without claim relevance |
| artifact_pressure_model | Required artifact is a context budget policy for prompt, file, memory, and sub-agent handoff | Require a replayable policy before claiming operational usability | The artifact cannot explain exclusions, handoffs, gate, or stop condition |
| semantic_coupling_model | Count dependencies and shared invariants, not only files | Inspect whether one source change invalidates decisions across units | Independent ownership cannot be assigned without duplicating mutable state |
| action_side_effect_model | Classify reads, local writes, commits, pushes, deployments, and external calls by reversibility and permission | Require stronger evidence and approval as reversibility decreases | An action is irreversible, permission-sensitive, or lacks rollback |
| reconciliation_fan_in_model | Bound how many independent outputs one owner must integrate coherently | Record merge points, conflict rate, and unresolved decisions | Outputs arrive faster than they can be reviewed or share hidden assumptions |
| temporal_context_model | Checkpoint when work spans phases, sessions, or a material source change | Snapshot current phase, exact evidence, and next action | The agent cannot reconstruct why the current branch was chosen |

**Why raw counts are insufficient.** Ten one-line independent sources can be easier than two large contradictory specifications. Three delegated lookups can be safer than one delegated rewrite of shared state. Token, file, and agent counts are observable proxies; semantic coupling, fan-in, side effects, and ownership determine practical risk.

**Alternatives.** Byte or token budgets provide hard capacity but not relevance. Dependency-graph narrowing improves semantic selection but needs tooling. Time-boxes bound expense but can expire before evidence is sufficient. Use the cheapest model that still detects the dominant pressure.

**Verification.** Capture source count and size, dependency crossings, tool calls, fanout, fan-in, retries, elapsed time, reviewer time, and merge conflicts. Compare these with the split trigger. The exact seed ceilings remain uncalibrated policy values.

The binding limit is often reconciliation, not context size. More parallel work can increase throughput while making final correctness worse if one owner cannot validate shared assumptions.

## Reliability Target

These values are retained from the seed as policy targets. They are not observed results. Before claiming achievement, define eligible recommendations, task cohort, sample selection, reviewer rubric, severity, and remediation.

| reliability_target_name | measurable_threshold_value | evidence_collection_method | interpretation_and_hard_stop |
| --- | --- | --- | --- |
| source_boundary_preservation | 100 percent of recommendations keep local, external, and inference boundaries visible | Review generated text and downstream handoffs for the three evidence labels and scoped premises | Any authority inversion or lost boundary on a consequential claim blocks completion |
| decision_accuracy_sample | At least 18 of 20 sampled uses route to the correct adopt, adapt, avoid, pause, or adjacent-reference decision | Preselect comparable downstream tasks and record independent reviewer verdicts plus disagreement | Report misses and causes; aggregate pass does not excuse a severe permission or safety error |
| unsupported_claim_rate | Zero unsupported production, security, latency, or reliability claims in final guidance | Reject claims without a source row, explicit inference note, uncertainty boundary, or verification method | Any unsupported consequential claim is a hard stop until removed, bounded, or evidenced |
| recovery_path_clarity | Every avoid or failure case names containment, rollback or safe state, escalation owner, and next-reference route | Inspect failure-mode and adjacent-routing sections together; replay representative failures | A non-recoverable action requires stronger prevention and approval before execution |

**Sampling protocol.**

1. Pre-register twenty comparable uses rather than selecting only successes.
2. Define what counts as a recommendation, correct route, unsupported claim, and complete recovery.
3. Use at least one reviewer who did not author the decision when feasible.
4. Record disagreement instead of forcing consensus into the score.
5. Classify severity. A wrong low-impact route and a permission violation are not interchangeable.
6. Revise policy for each miss and resample after material changes.

**Good evidence.** Eighteen of twenty cases route correctly, two misses are shown with causes and corrections, and no hard-stop boundary fails. **Bad evidence.** "Target met" appears without samples. **Borderline evidence.** Aggregate routing passes, but one case reverses instruction authority; the hard stop overrides the aggregate.

Twenty cases may be too few for rare failures, and reviewer judgment may vary. These limits do not make the target useless; they prevent false precision. Reliability combines learning metrics with incident-style hard stops.

## Failure Mode Table

The table models detection through recovery. A mitigation that assumes clean state is insufficient after tools, edits, or delegated work have already occurred.

| failure_mode_name | likely_trigger_condition | observable_detection_signal | immediate_containment_action | durable_mitigation_action | recovery_proof_and_owner |
| --- | --- | --- | --- | --- | --- |
| source drift hides truth | Local or public guidance changes after the reference was written | Digest, version, content, or owner differs; a dependent claim no longer traces | Mark dependent claims stale and stop consequential reuse | Refresh public evidence when permitted, rerun local corpus gate, and maintain forward dependency links | Owner reruns affected gates and records changed claims |
| generic advice escapes review | Agent copies plausible best practices without theme-specific evidence | Output could be moved to another repository unchanged; no local constraint changes action | Block completion and quarantine the generic recommendation | Require source map, claim boundaries, and task-specific gate | Reviewer traces sampled advice to local decision and gate |
| context window loses plan | A long session compacts or forgets early constraints | Current action conflicts with checkpoint, exclusions disappear, or questions repeat | Stop new mutations and reload last trusted checkpoint | Persist goal, constraints, decisions, files, tests, risks, and next step | Primary owner reconciles current state against the checkpoint |
| tool fanout outruns budget | Parallel actions create conflicts, duplicate work, or unbounded calls | Duplicate ownership, rising retries, unresolved output queue, or conflicting patches | Stop admission of new work and cancel safe redundant tasks | Cap fanout, assign immutable ownership, and define merge checkpoints | Integrator verifies one accepted output per owned unit |
| instruction precedence inverts | A relevant lower-scope source is treated as controlling | Decision log lacks scope; action violates direct task or safety constraint | Stop affected action and preserve evidence | Record precedence and conflict disposition before synthesis | Responsible owner audits and revalidates every affected action |
| verification checks a proxy | Structural command passes while claimed behavior is false | Gate cannot fail under an adversarial false implementation | Withdraw completion claim | Add behavioral or semantic falsification and expected failure | Fresh focused evidence demonstrates the intended property |
| delegation drops constraints | Handoff includes files but not goal, prohibitions, or acceptance evidence | Returned work cannot explain requirement or owner | Do not merge or apply output | Use bounded handoff and return contract | Primary owner independently checks constraints and tests |
| sensitive context leaks | Raw prompts, source bodies, credentials, or private data enter logs or handoffs unnecessarily | Redaction scan or reviewer finds prohibited data | Restrict access, stop propagation, and follow local incident policy | Data minimization, structured events, redaction, retention limits | Authorized owner confirms containment under applicable policy |
| shared workspace ownership collides | Two agents edit the same semantic unit or one edits shared state outside role | Diff shows overlapping paths or unexplained queue mutation | Stop edits on the collided unit; preserve both states | Immutable whole-file ownership and coordinator-only shared updates | Coordinator resolves ownership and reruns integrity checks |
| retry duplicates side effects | A failed or timed-out action is repeated without known idempotency | Duplicate artifact, external call, commit, or mutation appears | Stop retries and identify side effects | Classify idempotency and changed condition before retry | Owner proves one intended outcome and removes or contains duplicates |
| uncalibrated target becomes fact | A seed score or capacity number is repeated as observed performance | Claim lacks sample, rubric, denominator, or date | Correct the claim and dependent decision | Label policy targets and establish measurement protocol | Reviewer confirms no unsupported numeric inference remains |

**Fault exercise.** Replay at least one stale-source case, one proxy-verification case, and one lost-handoff case. The signal should fire before completion, containment should prevent wider action, and the recovery gate should not rely solely on the corrupted context.

**Uncertainty.** The seed establishes plausible modes but no incidence or severity distribution. Runtime telemetry and rollback capability vary. Calibrate the table with actual failures and near misses.

The last-known-good decision state is a core recovery primitive. Without it, the same damaged context that caused failure must also explain how to recover.

## Retry Backpressure Guidance

Retry is a response to a classified failure, not a default reaction to discomfort or red output.

| failure_class | retry_default | required_changed_condition | backpressure_action | escalation_or_stop |
| --- | --- | --- | --- | --- |
| transient_timeout_or_unavailable_tool | One bounded retry may be reasonable if the operation is idempotent | Delay, restored service, narrower input, or increased timeout within policy | Pause dependent fanout and preserve checkpoint | Escalate after budget or deadline; do not spin |
| stale_external_evidence | One bounded refresh retry when browsing is permitted | New retrieval, version pin, or alternate primary source | Stop synthesis that depends on stale claims | Escalate or narrow the claim if freshness remains unavailable |
| missing_local_context | Retry discovery after naming the missing scope | New path, owner answer, or dependency map | Stop implementation that assumes the missing fact | Ask owner or route to source-specific reference |
| deterministic_verification_failure | Do not rerun unchanged work | Code, artifact, expectation, or context model must change | Block new completion claims | Diagnose and repair before any rerun |
| true_source_contradiction | Do not average or repeatedly query the same sources | Authority resolution, owner decision, or narrower scope | Stop consequential action | Human or domain-owner escalation |
| permission_denial | No retry unless permission changes explicitly | New explicit authorization | Stop all related mutations | Report the blocked action and safe state |
| destructive_or_non_idempotent_action | No blind retry | Proven idempotency, containment, rollback, and authorization | Freeze related side effects | Escalate to responsible owner |
| shared_workspace_global_failure | Rerun only when shared state may have changed | Another owner or coordinator completes the relevant dependency | Continue only disjoint pilot-owned checks | Report global failure; never edit outside ownership to force green |

For every retry, record class, original signal, changed condition, idempotency, side effects, attempt and cost budget, result, and next escalation. A repeated command with no changed premise is usually not a new experiment.

Apply backpressure to new generation and fan-in, not only calls. When unresolved outputs accumulate, stop admission even if tools are responsive. Parallel retries can synchronize into a second load spike or create duplicate valid-looking artifacts.

For long-running agent workflows, checkpoint after each meaningful batch and reread the current specification before a broad rewrite, commit, push, or destructive action. For distributed execution, use one owner per generated file or theme batch and one integration gate.

**Good retry.** A read times out; the agent confirms idempotency, narrows the range, retries once, and records success. **Bad retry.** A push times out and is repeated without checking remote state. **Borderline retry.** A global test is rerun after another lane reports completion; this is reasonable because a relevant condition changed.

The one-retry seed rule is conservative guidance, not a universal optimum. Service contracts, deadlines, and side effects determine the actual policy.

## Observability Checklist

Observe decisions and outcomes, not private hidden reasoning. The goal is a compact replayable audit that helps a reviewer answer what was authorized, what evidence controlled it, what happened, and what remains unresolved.

| event_or_artifact | minimum_fields | reason_to_collect | privacy_and_volume_limit |
| --- | --- | --- | --- |
| task_opened | Task identifier, user goal, phase, owner, prohibited actions | Establishes the unit of work and authority | Do not copy unrelated conversation |
| source_selected | Path or URL, scope, freshness, supported claim, inclusion reason | Makes context choice auditable | Prefer metadata and relevant summary over full source body |
| source_excluded | Candidate, exclusion or deferral reason, revisit trigger | Distinguishes intentional shedding from accidental omission | Record only plausible candidates |
| conflict_recorded | Statements, scopes, authority levels, owner, disposition | Prevents silent conflict flattening | Avoid sensitive text beyond what resolution needs |
| action_executed | Tool or command summary, side-effect class, result, elapsed time | Links context decision to behavior | Redact secrets and credentials |
| delegation_sent | Subtask, owned paths, constraints, acceptance, return shape | Preserves intent across isolation | Do not delegate unnecessary private context |
| gate_completed | Claim, command or review, exit/result, evidence location | Supports completion claims | Keep summary and decisive output, not unbounded logs |
| retry_or_backpressure | Failure class, changed condition, idempotency, budget, decision | Explains repeated or stopped work | Aggregate repetitive transient events where safe |
| checkpoint_written | Current phase, tests, files, decisions, blockers, next step | Enables deterministic resume | Keep one trusted current state plus necessary history |
| task_closed | Changed paths, counts, tests, residual risks, next assigned work | Gives the user a reviewable handoff | Exclude raw internal transcript |

**Checklist.**

- Record which local sources were loaded and which were intentionally skipped.
- Preserve local, external, and inference boundaries in summaries and handoffs.
- Record the exact verification command, reviewer question, or rendered artifact used as proof.
- Capture tool-call count, source count and size, delegated tasks, retry count, fanout, fan-in, and completion-audit outcome when they influence the decision.
- Record p50/p95/p99 latency only for a repeated, comparable runtime cohort with sample count; otherwise use individual timings, median, range, and reviewer-time notes.
- Use a correlation identifier so events from one task, subtask, and retry can be joined.
- Apply schema validation, data minimization, redaction, access control, and retention policy.
- Keep evidence small enough to review: command summary, changed-file list, counts, and unresolved risks are preferred over transcript dumps.
- Run a replay exercise: a reviewer should recover the branch, next action, gate, and stop condition from the recorded events.

**Gotchas.** Tool-call count can reward fewer but less useful calls. Latency without stage and cache state is hard to interpret. Full traces improve forensics but increase privacy and cost. Aggregates are cheap but cannot explain one authority failure. Use sampled structured events as the default and increase detail only for a concrete diagnostic need.

The seed does not define retention, privacy classification, or acceptable telemetry overhead. Those must come from local policy. High-level decision rationale is required; hidden chain-of-thought is neither required nor appropriate evidence.

## Performance Verification Method

Performance method: require tool-call budgets, timeout budgets, context shedding, and a resumable journal when the workflow exceeds one focused session. Measure speed only alongside decision quality and recovery.

**Separate three dimensions.**

1. **Operational latency:** wall-clock and per-stage time for reads, tools, verification, retries, and fan-in.
2. **Agent work cost:** source count and bytes, tool calls, delegated tasks, retries, generated and retained context, and reconciliation effort.
3. **Human review burden:** time to identify the branch, inspect evidence, resolve uncertainty, and approve or reject completion.

**Measurement packet.**

| measurement_field | required_detail | interpretation_guardrail |
| --- | --- | --- |
| task_cohort | Comparable goal, risk, repository surface, and cold or warm state | Do not combine unrelated task classes |
| input_shape | Source count, bytes or tokens where available, dependency coupling, and exclusions | Count does not represent semantic complexity alone |
| execution_shape | Tool calls, fanout, fan-in, retries, timeouts, side-effect classes | Parallel speedup may increase merge and conflict cost |
| timing | Wall time and stage timings with instrumentation point | Separate external wait, cache state, and reviewer delay |
| distribution | Sample count plus p50/p95/p99 latency when repeated runtime data justifies it | A high percentile from a tiny sample is unstable |
| quality | Unsupported claims, wrong-source rework, gate quality, unresolved risks | Faster is not better if correction moves downstream |
| review | Reviewer decision time, disagreements, and requested rework | Familiarity and artifact complexity confound comparison |
| recovery | Detection delay, containment time, rollback or safe-state evidence | Irreversible failure needs prevention, not only faster recovery |

Leading indicator to measure: comparable runs require less avoidable clarification and less reviewer reconstruction while maintaining or improving claim support.

Failure signal to watch: the reference recommends implementation before workload, reliability target, failure modes, and stop conditions are explicit; or latency improves while rework and unresolved risk rise.

Pass condition: a reviewer can identify the correct next action, verification gate, and stop condition without reading unrelated files, and the workflow meets locally established time and cost budgets.

Fail condition: performance claims lack a cohort, sample, instrumentation, or paired quality measure; or optimization removes decisive context.

**Alternatives.** Use qualitative time-boxed review for rare one-off work, a benchmark harness for repeated deterministic workflows, and production tracing only when live systems and policy justify its overhead.

No baseline or observed performance result appears in the seed. Thresholds must be calibrated locally. Optimize avoidable context and reconciliation first; faster tools cannot rescue a wrong source model.

## Scale Boundary Statement

Agent Context Instruction Patterns stops being sufficient when one owner can no longer maintain a coherent source, decision, and verification ledger. Warning signals include multiple independent systems, more than one ownership boundary, unbounded source discovery, tightly coupled mutable artifacts, uncontrolled fanout or fan-in, production traffic without an SLO, and actions that cannot be safely rolled back.

**Default scale response.**

1. Map dependencies and shared invariants before partitioning.
2. Split by stable semantic ownership or independent theme, not arbitrary line count.
3. Give every unit exact owned paths, controlling constraints, acceptance evidence, and return shape.
4. Retain one integrator for cross-boundary decisions and final verification.
5. Apply admission control when outputs arrive faster than they can be reconciled.
6. Add production controls - security, SLOs, rollout, rollback, incident ownership, and change approval - before touching live traffic.
7. Recombine only through an integration gate that tests shared invariants.

Under distributed execution, one owner per generated file is safer than multiple agents rewriting sections of the same file. Parallelism is beneficial when work is independent; otherwise it converts hidden coupling into merge-time conflict.

Under long-running agent workflows, context drift is a reliability failure. Persist the current goal, constraints, decisions, evidence, files, tests, risks, and next action. Invalidate summaries when a controlling source changes.

Under large-codebase scale, narrow by dependency or source graph before loading. A flat source list without ranked canonical guidance and claim relevance is not sufficient.

**Alternatives.** Sequential deep work minimizes coordination risk. Graph-based narrowing reduces context but requires a trustworthy index. Hierarchical delegation increases capacity but adds handoff and coordinator bottlenecks. Choose based on coupling and ownership, not agent availability.

**Examples.** Splitting 99 independent reference files among immutable owners with one coordinator is a good scale pattern. Splitting one semantically coherent file across four simultaneous writers is bad. Files that look separate but share one unresolved schema are borderline and should remain coordinated until the invariant is settled.

**Verification.** Track dependency crossings, ownership conflicts, fanout, fan-in, queue depth, merge conflicts, unresolved decisions, integration-gate results, rollback readiness, and SLO evidence where production applies. The seed offers no measured agent-count error curve; scale triggers are operational judgments.

The deeper boundary is coherent ownership and verification, not raw context-window size.

## Future Refresh Search Queries

These queries are future work items, not evidence used in this no-browsing pass. Run them only when a freshness-sensitive claim could change the decision.

| search_query_label_name | search_query_text_value | intended_source_priority | expected_decision_impact | required_refresh_record | stop_condition |
| --- | --- | --- | --- | --- | --- |
| official_docs_query_phrase | agent context instruction patterns official documentation best practices | Current primary official product documentation | Confirm or contradict documented instruction discovery, scope, or precedence behavior | Query, domain, date, product version, selected finding, affected claim | Stop when the consequential product claim is confirmed, contradicted, or explicitly unresolved |
| github_repository_query_phrase | agent context instruction patterns GitHub repository examples | Official repository, tagged release, then maintained primary examples | Compare implementation and real project instruction patterns with documented behavior | Query, repository, commit or tag, inspected path, date, local compatibility result | Stop when implementation evidence answers the named behavior question |
| release_notes_query_phrase | agent context instruction patterns changelog release notes migration | Official changelog or release notes | Detect behavior changes that invalidate a mapped external claim | Query, release range, date, changed feature, migration effect | Stop when all dependent claims are marked current, adapted, or stale |

**Query discipline.**

- Derive a query from an unresolved claim or observed failure, not merely from the theme name.
- Prefer known primary sources and versioned material. Broad discovery is useful only when the source landscape itself is uncertain.
- Record negative and contradictory findings. Do not search repeatedly until confirmation appears.
- Treat snippets as discovery leads, not evidence.
- Compare public guidance with the installed runtime and local repository behavior.
- Preserve the no-browsing boundary when the task prohibits network research.

**Good refresh.** A runtime upgrade makes instruction discovery uncertain; the reviewer checks current official documentation and a tagged implementation, records version fit, and updates only affected claims. **Bad refresh.** Ten generic links are added without changing a decision. **Borderline refresh.** A current official page is found, but the installed version is unknown; the evidence is strong for current documentation and incomplete for local applicability.

Future terminology and URLs may change. The query ledger should evolve from actual gaps and failure signals rather than becoming a static search ritual.

## Evidence Boundary Notes

- **local_corpus_sourced_fact:** A statement tied directly to an inspected local path and limited to the content and scope that path actually establishes. Local does not automatically mean correct, current, or globally controlling.
- **external_research_sourced_fact:** A statement tied to a checked public source with retrieval state, relevant passage or finding, version, and applicability. In this pass the public URLs are cataloged but unrefreshed, so no new current external claim is added.
- **combined_evidence_inference_note:** A synthesis that shows the premises, reasoning-level conclusion, uncertainty, and verification method. Inference is not inherently weak, but it must not borrow authority from a premise outside its scope.

**Atomic claim rule.** Split a sentence when different clauses have different evidence boundaries. "The local file forbids push, therefore all agents must ask before any Git operation" is mixed and overbroad. A sound version is: "The local file forbids push without explicit permission" as local fact. "This task will not push unless the user later authorizes it" is a bounded application and inference.

**Authority is separate from provenance.** These labels explain where knowledge came from. They do not decide which instruction wins. Resolve platform, safety, direct task, repository, and scoped precedence independently.

**Absence and conflict.**

- A source's silence is an evidence gap, not proof that an action is allowed or prohibited.
- Conflicting sources remain separate facts until authority, scope, freshness, or an owner resolves them.
- A stale but once-authoritative source should be labeled stale; confidence wording cannot restore applicability.
- A copied summary must preserve source, scope, freshness, inference, and unresolved conflict or link reliably to a ledger that does.

**Representation alternatives.** Inline labels maximize visibility but can burden prose. A claim ledger or footnote system improves readability but requires durable linking. Structured metadata enables automated impact analysis but adds schema and migration cost. Choose one representation and test that provenance survives summaries and handoffs.

**Bidirectional verification.** Trace sampled prose back to evidence, then trace each source forward to all dependent claims. The first catches unsupported guidance. The second supports change impact: when a source changes, the affected recommendations are known.

**Confidence boundary.** The three labels and mapped source facts are inherited and useful. Confidence calibration, reviewer agreement, and automated provenance are not established. Record what evidence would upgrade confidence rather than hiding uncertainty behind adjectives.

The second-order consequence is maintainability. Evidence boundaries are change boundaries: precise provenance reduces the amount of guidance that must be distrusted and re-reviewed after one source moves.
