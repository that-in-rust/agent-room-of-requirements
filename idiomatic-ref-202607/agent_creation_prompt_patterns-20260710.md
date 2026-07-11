# Agent Creation Prompt Patterns

Use this reference to decide whether a recurring task should become a specialized agent and, when it should, to turn that decision into a bounded and testable agent prompt. The intended reader is an agent-system designer or reviewer who must define five coupled contracts: who the agent serves, when it activates, what authority it receives, how it performs the work, and what evidence proves completion. A persuasive persona is optional; those contracts are not.

The recommended default is proportional rigor: write a small agent charter before writing frontmatter or system-prompt prose, load the minimum relevant local sources, distinguish sourced facts from design inference, define both activation and nonactivation examples, grant only the tools required by the process, and specify verification and escalation before enabling repeated use. Low-risk read-only agents can use a compact charter. Agents that write files, invoke shells, touch external systems, or act proactively need stronger negative triggers, approval boundaries, recovery paths, and behavioral tests.

An agent is usually appropriate when a reusable specialist can own a coherent multi-step outcome, such as reviewing a migration, investigating a failure, or generating a constrained artifact. Prefer a command for one explicit deterministic action, a skill for a reusable method loaded into the current agent, project instructions for broad repository rules, or direct human approval for consequential decisions that should not be delegated. A wrapper around one command is justified only when it adds stable routing, interpretation, or lifecycle behavior; forwarding arguments alone does not create a meaningful agent responsibility.

Evaluate routing and execution separately. An agent may perform its task well yet still be a poor design because it activates too broadly, overlaps another agent, receives unnecessary tools, retries without a bound, or cannot explain when it is done. Completion therefore means more than valid Markdown: the artifact must pass schema checks, positive and negative routing scenarios, permission-boundary review, a representative task run, output-contract inspection, and at least one failure or escalation scenario. Public links in this file are retained evidence pointers; this no-browse evolution pass does not establish their current contents.

## Source Evidence Mapping Table

This inventory is a retrieval map, not a vote count. It contains six local artifact lineages in archived and live locations plus three public ecosystem pointers. Archive/live counterparts preserve provenance and operational context, but identical copies are not independent corroboration. A row establishes that a source was mapped for a role; it does not by itself establish freshness, authority for every claim, or effectiveness of the resulting agent.

| source_location_path_key | source_category_artifact_type | source_authority_confidence_level | source_usage_synthesis_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/agent-development/SKILL.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/agent-development/examples/agent-creation-prompt.md | local_corpus_source_material | local_corpus_sourced_fact | example or template demonstrating expected artifact shape |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/agent-development/examples/complete-agent-examples.md | local_corpus_source_material | local_corpus_sourced_fact | example or template demonstrating expected artifact shape |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/agent-development/references/agent-creation-system-prompt.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/agent-development/references/system-prompt-design.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/agent-development/references/triggering-examples.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| claude-skills/plugins/plugin-dev/agent-development/SKILL.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt |
| claude-skills/plugins/plugin-dev/agent-development/examples/agent-creation-prompt.md | local_corpus_source_material | local_corpus_sourced_fact | example or template demonstrating expected artifact shape |
| claude-skills/plugins/plugin-dev/agent-development/examples/complete-agent-examples.md | local_corpus_source_material | local_corpus_sourced_fact | example or template demonstrating expected artifact shape |
| claude-skills/plugins/plugin-dev/agent-development/references/agent-creation-system-prompt.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| claude-skills/plugins/plugin-dev/agent-development/references/system-prompt-design.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| claude-skills/plugins/plugin-dev/agent-development/references/triggering-examples.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| https://developers.openai.com/codex/guides/agents-md | external_research_source_material | external_research_sourced_fact | primary guidance for project instruction files and agent context loading |
| https://agents.md/ | external_research_source_material | external_research_sourced_fact | community format for predictable agent instructions |
| https://github.com/openai/codex | external_research_source_material | external_research_sourced_fact | GitHub implementation and project-level agent guidance |

For current repository work, start with the live `claude-skills/plugins/plugin-dev/agent-development/SKILL.md` entrypoint. Load a focused reference only for the active uncertainty: `triggering-examples.md` for routing, `system-prompt-design.md` for process and output design, and `agent-creation-system-prompt.md` for assisted generation behavior. Use a complete example to check integrated artifact shape, not as a source of task requirements. Consult the archived counterpart when reconstructing provenance or checking drift. Historical work reverses that order.

Use public documentation to challenge or refresh host-level assumptions, implementation repositories to investigate behavior not resolved by supported documentation, and community formats to evaluate portability. Do not transfer product-specific fields across hosts merely because the underlying design principle is similar. When a public source has not been refreshed, preserve it as a search target and bound any operational recommendation to inspected local evidence plus explicit inference.

For each consequential recommendation, record four things in working notes: the question being answered, the selected source and relevant span, whether the statement is fact or inference, and the scenario or review gate that could disconfirm it. Stop loading more context when schema, the disputed behavior, and a verification method are covered. Record intentionally skipped sources and why; this makes omission auditable without turning exhaustive reading into a proxy for rigor.

## Pattern Scoreboard Ranking Table

The scores below are inherited corpus-prioritization metadata. They preserve deterministic ranking inside this reference set; they are not probabilities, measured effect sizes, or evidence that a 95-point pattern is seven units more effective than an 88-point pattern. Consequence, source quality, and task context override arithmetic when patterns compete.

| pattern_identifier_stable_key | pattern_score_numeric_value | pattern_tier_adoption_level | pattern_failure_prevention_target |
| --- | ---: | --- | --- |
| `agent_creation_prompt_patterns` | 95 | default_adoption_pattern_tier | Source Map First: Load local agent creation material before synthesizing prompt patterns recommendations. |
| `agent_creation_prompt_patterns` | 91 | default_adoption_pattern_tier | Evidence Boundary Split: Separate local facts, external facts, and inference before giving agent instructions. |
| `agent_creation_prompt_patterns` | 88 | default_adoption_pattern_tier | Verification Gate Coupling: Attach each recommendation to at least one command, checklist, or review gate. |

Apply the three defaults as a feedback loop:

1. **Source Map First:** produce a ranked, deduplicated retrieval list tied to the active question. This prevents generic prompt advice from outranking repository conventions.
2. **Evidence Boundary Split:** turn selected material into claim-level facts, bounded inferences, and explicit uncertainty. The label must change confidence or action; decorative prefixes do not count.
3. **Verification Gate Coupling:** attach high-consequence clauses to structural checks, routing fixtures, permission checks, task scenarios, or reviewer criteria. A check that can fail without blocking or narrowing release is monitoring, not a gate.
4. **Loop on failure:** a failed scenario may expose stale evidence, a mistaken inference, or an incomplete prompt contract. Return to the affected source and clause rather than fitting the test to one convenient output.

Each pattern should leave a reviewable artifact: a source selection record, a claim and uncertainty ledger, and a gate matrix. A small read-only agent may satisfy the trio with one canonical source, one material inference, and one focused check. A proactive agent with write or execution authority needs broader counterexamples and recovery evidence. The patterns are therefore coverage requirements, not a demand for equal ceremony on every task.

## Idiomatic Thesis Synthesis Statement

`local_corpus_sourced_fact`: The local row for `agent_creation_prompt_patterns` contains 12 source paths: six artifact types represented in archived and live locations. They are the first retrieval surface for current repository work because they expose the local file format, assisted-generation pattern, complete examples, system-prompt structure, and triggering guidance. The count describes inventory breadth, not twelve independent confirmations.

`external_research_sourced_fact`: The external source map retains public documentation, a community format, and a repository analogue. Those pointers can check project-instruction loading, ecosystem conventions, or implementation behavior when refreshed. Because this pass does not browse, their present content and version alignment remain unverified and they do not support new current-state claims here.

`combined_evidence_inference_note`: The idiomatic default is local compatibility first, external challenge second, and observable agent behavior last. Adopt a local rule when it is relevant and consistent with the target host. Adapt it when the principle transfers but syntax, authority, or routing differs. Avoid or defer it when evidence conflicts on a consequential behavior that cannot be tested. If uncertainty remains, reduce authority, switch to advisory output, or retain human approval instead of hiding uncertainty behind confident prompt prose.

The causal chain matters. Sources constrain what may be claimed; evidence labels constrain how confidently it may be prescribed; the agent charter converts those claims into trigger, authority, process, output, and escalation clauses; and verification determines whether that composition behaves as intended. Accurate quotations can still produce an unsafe agent if they are combined into an overbroad trigger or excessive tool grant. Verify the combined decision, not merely the fidelity of its ingredients.

A maintainable implementation records `source -> claim -> prompt clause -> scenario or gate -> owner`. High confidence in a source does not imply high confidence in runtime behavior until the actual host exercises the clause. When a source changes, inspect the linked claims and rerun the linked scenarios. Retire the agent when its evidence and tests have no owner, its trigger space has been absorbed elsewhere, or its observed value no longer justifies the routing and maintenance cost.

## Local Corpus Source Map

The local corpus is a connected family rather than twelve independent authorities. The live skill is the integrated operational entrypoint; focused references answer narrower questions; examples demonstrate artifact shape; archived copies preserve the historical snapshot. For contract conflicts, explicit current validation rules outrank illustrative examples unless the repository declares an example canonical.

| local_source_filepath_value | local_source_title_text | local_source_heading_signals | local_source_usage_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/agent-development/SKILL.md | agent-development | Agent Development for Claude Code Plugins; Overview; Agent File Structure; Complete Format; Frontmatter Fields; name (required) | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/agent-development/examples/agent-creation-prompt.md | AI-Assisted Agent Generation Template | AI-Assisted Agent Generation Template; Usage Pattern; Step 1: Describe Your Agent Need; Step 2: Use the Generation Prompt; Step 3: Claude Returns JSON; Step 4: Convert to Agent File | example or template demonstrating expected artifact shape |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/agent-development/examples/complete-agent-examples.md | Complete Agent Examples | Complete Agent Examples; Example 1: Code Review Agent; Code Review Summary; Critical Issues (Must Fix); Major Issues (Should Fix); Minor Issues (Consider Fixing) | example or template demonstrating expected artifact shape |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/agent-development/references/agent-creation-system-prompt.md | Agent Creation System Prompt | Agent Creation System Prompt; The Prompt; Usage Pattern; Converting to Agent File; Customization Tips; Adapt the System Prompt | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/agent-development/references/system-prompt-design.md | System Prompt Design Patterns | System Prompt Design Patterns; Core Structure; Pattern 1: Analysis Agents; Summary; Critical Issues; Major Issues | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/agent-development/references/triggering-examples.md | Agent Triggering Examples: Best Practices | Agent Triggering Examples: Best Practices; Example Block Format; Anatomy of a Good Example; Context; User Message; Assistant Response (Before Triggering) | reference detail file for deeper pattern evidence |
| claude-skills/plugins/plugin-dev/agent-development/SKILL.md | agent-development | Agent Development for Claude Code Plugins; Overview; Agent File Structure; Complete Format; Frontmatter Fields; name (required) | skill entrypoint or reusable agent prompt |
| claude-skills/plugins/plugin-dev/agent-development/examples/agent-creation-prompt.md | AI-Assisted Agent Generation Template | AI-Assisted Agent Generation Template; Usage Pattern; Step 1: Describe Your Agent Need; Step 2: Use the Generation Prompt; Step 3: Claude Returns JSON; Step 4: Convert to Agent File | example or template demonstrating expected artifact shape |
| claude-skills/plugins/plugin-dev/agent-development/examples/complete-agent-examples.md | Complete Agent Examples | Complete Agent Examples; Example 1: Code Review Agent; Code Review Summary; Critical Issues (Must Fix); Major Issues (Should Fix); Minor Issues (Consider Fixing) | example or template demonstrating expected artifact shape |
| claude-skills/plugins/plugin-dev/agent-development/references/agent-creation-system-prompt.md | Agent Creation System Prompt | Agent Creation System Prompt; The Prompt; Usage Pattern; Converting to Agent File; Customization Tips; Adapt the System Prompt | reference detail file for deeper pattern evidence |
| claude-skills/plugins/plugin-dev/agent-development/references/system-prompt-design.md | System Prompt Design Patterns | System Prompt Design Patterns; Core Structure; Pattern 1: Analysis Agents; Summary; Critical Issues; Major Issues | reference detail file for deeper pattern evidence |
| claude-skills/plugins/plugin-dev/agent-development/references/triggering-examples.md | Agent Triggering Examples: Best Practices | Agent Triggering Examples: Best Practices; Example Block Format; Anatomy of a Good Example; Context; User Message; Assistant Response (Before Triggering) | reference detail file for deeper pattern evidence |

Use this question-driven routing protocol:

| active_design_question | first_local_source_to_inspect | corroborating_artifact | misuse_to_avoid |
| --- | --- | --- | --- |
| What fields and basic constraints define the agent file? | live `agent-development/SKILL.md` | current validator or minimal agent artifact | inferring the contract from one example |
| How should assisted generation translate a request? | `references/agent-creation-system-prompt.md` | `examples/agent-creation-prompt.md` | accepting generated JSON without task-specific review |
| How should responsibilities, process, quality, output, and edge cases be expressed? | `references/system-prompt-design.md` | one relevant complete example | copying persona, length, or tool choices as requirements |
| What should and should not activate the agent? | `references/triggering-examples.md` | positive, implicit, proactive, negative, and overlap scenarios | treating keyword similarity as sufficient routing evidence |
| How do the pieces compose in a complete file? | `examples/complete-agent-examples.md` | live skill contract | declaring an illustrative template production-ready unchanged |
| How did local guidance change? | archived artifact, then live counterpart | relevant diff and linked regression scenario | counting duplicate versions as independent support |

For operational work, read the live entrypoint, one focused reference matching the unresolved question, and one integrated example only if composition remains unclear. For historical work, begin with the archived entrypoint and compare forward. If archive and live content are byte-identical, one semantic read plus an identity check is sufficient; if they differ, record which changed clause affects schema, routing, authority, process, or verification.

The corpus is strongest on agent creation and triggering. It is less explicit about deployed-agent telemetry, ownership transfer, and retirement, so lifecycle guidance in this evolved reference is labeled synthesis rather than attributed to a single local file. Do not inherit unsupported precision, universal length targets, or claims of production readiness simply because they appear in local examples. Validate concrete format rules against the current repository and behavioral rules against representative runs.

## External Research Source Map

These public sources are comparative dependencies, not direct substitutes for the Claude Code plugin material above. Their authority depends on the claim: supported documentation can establish a documented contract, a repository can clarify implementation behavior, and a community format can reveal portability conventions. None should be stretched beyond its demonstrated product surface.

| external_source_url_value | external_source_name_text | external_source_usage_role | evidence_boundary_label_value |
| --- | --- | --- | --- |
| https://developers.openai.com/codex/guides/agents-md | OpenAI Codex AGENTS.md guide | primary guidance for project instruction files and agent context loading | external_research_sourced_fact |
| https://agents.md/ | AGENTS.md open format | community format for predictable agent instructions | external_research_sourced_fact |
| https://github.com/openai/codex | OpenAI Codex repository | GitHub implementation and project-level agent guidance | external_research_sourced_fact |

No browsing was performed during this evolution pass. The table therefore preserves source identity and intended role, while current content, redirects, versions, and applicability remain to be refreshed before they support a new present-tense external claim. A future evidence record should include access date, relevant product or installed version, a concise supporting passage or implementation location, the local prompt clause derived from it, and the scenario that will fail if the assumed behavior is absent.

Prefer official documentation for supported semantics, then inspect implementation only when documentation leaves a material ambiguity. Use community guidance for interoperability questions, not for vendor-specific frontmatter. Release notes, installed-runtime help, schemas, and controlled experiments are valid alternatives when they answer the uncertainty more directly. The installed runtime can be more operationally relevant than the newest public documentation when a repository is intentionally pinned.

Stop external research when additional information no longer changes trigger boundaries, tool authority, process, output, escalation, or release status. If freshness cannot be established, keep the URL as a future query target, label the proposed rule as inference, and reduce authority or require manual invocation until target-host behavior is observed.

## Anti Pattern Registry Table

Use this registry during release review, not as a vocabulary exercise. A hit blocks reusable release when it affects routing, authority, completion, or recovery and no external enforcing control is named. During exploration, the same defect may remain as a documented question only if the prototype is isolated from automatic triggering and consequential tools.

| anti_pattern_failure_name | failure_cause_risk_reason | safer_default_replacement_pattern | detection_signal_review_method |
| --- | --- | --- | --- |
| context_free_summary_output | agent skips local corpus and produces generic advice | source_map_first_synthesis | verify every listed local path appears in the generated file |
| unsourced_recommendation_claims | guidance appears authoritative without source boundary | evidence_boundary_split_pattern | check for local, external, and inference labels |
| unverified_agent_instruction | recommendation cannot be checked by command or review gate | verification_gate_coupling | require concrete gate in generated reference |
| trigger_boundary_overlap | positive examples match another agent or omit meaningful nonactivation cases | explicit_trigger_exclusion_contract | run overlap and negative-routing scenarios against neighboring agents |
| excessive_tool_authority | tools are copied from a template rather than derived from process steps | least_privilege_tool_mapping | map every granted tool to one required step and deny an unnecessary tool in a fixture |
| ambiguous_completion_state | output prose sounds useful but no observable finish or handoff condition exists | output_and_stop_contract | require a pass, findings, escalation, or blocked result with named evidence |
| retry_or_delegation_loop | prompt permits repeated retries or reciprocal delegation without a budget | bounded_recovery_and_ownership | inject a persistent failure and verify one owner stops or escalates |

The original detection rules are necessary but not sufficient. Path presence does not prove that the relevant source was read; labels do not prove that a claim is correctly scoped; and a command does not prove behavioral coverage. For high-consequence clauses, trace the instruction to a relevant source or explicit inference, identify a disconfirming observation, and exercise a counterexample or denied-capability path. Delete generic prose that does not change behavior instead of manufacturing evidence to preserve it.

Use progressive authority when remediation is incomplete: first verify routing and read-only analysis, then add write or execution tools only after stronger recovery and permission gates pass. Review shared templates for blast radius because a subtle broad trigger or unverifiable completion rule can propagate across many agents. Keep registry entries that continue to catch real defects, revise those whose enforcing environment changed, and retire obsolete warnings before checklist noise teaches reviewers to ignore them.

## Verification Gate Command Set

`verification_gate_command_set`: Run the repository verifier after editing this file, but report its scope precisely. A final-stage generation pass is evidence about the checks implemented by that verifier; it is not automatically evidence that an agent routes correctly, obeys tool boundaries, completes a representative task, or recovers from failure.

```bash
python3 agents-used-monthly-archive/idiomatic-references-202606/tools/verify_reference_generation.py --stage final
```

Use a fail-fast verification stack:

| gate_layer | evidence_to_collect | release_consequence |
| --- | --- | --- |
| Artifact structure | parse frontmatter, validate required fields and identifiers, check placeholders and file location | block on any deterministic contract failure |
| Repository integration | run the named final-stage verifier from the repository root and retain exit status plus a concise result summary | block relevant failures; classify unrelated corpus failures separately |
| Routing behavior | exercise explicit, implicit, proactive, negative, and neighboring-agent overlap scenarios | narrow description or disable automatic activation on misses or false activations |
| Authority boundary | map each tool to a process step and test denial or absence of at least one unnecessary capability | remove unexplained authority before release |
| Task behavior | run a representative normal task and inspect required evidence and output shape | revise process or output contract when invariant outcomes are missing |
| Recovery behavior | inject missing context, tool failure, ambiguity, or a persistent failed check | require bounded retry, blocked status, or escalation rather than silent success |
| Final review | reread the complete prompt, charter, test evidence, and residual uncertainty | release only at the verified authority level |

Preflight the command path and available help when the tool version is uncertain. Prefer focused checks first, then broad integration checks, so an unrelated repository failure does not obscure whether the changed artifact is valid. Verification commands should be read-only unless mutation is an explicit and reviewed part of their contract. Capture command, scope, exit status, decisive checks, and unresolved coverage; avoid raw output dumps that bury the result.

Behavioral scenarios may vary by model or host. Assert stable route categories, denied actions, required evidence, and stop outcomes rather than exact prose. If host execution is unavailable, label the result **structurally verified, behaviorally unverified** and constrain use to manual or read-only operation. A partial pass should narrow deployment, not become a full-confidence claim.

## Agent Usage Decision Guide

`agent_usage_decision_guide`: Use this reference when a task asks to create or revise a reusable agent, cites one of the mapped local paths, or exposes the same routing, authority, and verification problems. Do not trigger on the word “agent” alone. First establish that a persistent autonomous role is more suitable than direct execution, an ephemeral subtask, a skill, a command, a hook, or project-level instructions.

Follow this operating sequence:

1. **Classify the mechanism.** Name the stable outcome the proposed agent uniquely owns. If it only forwards one deterministic command, prefer the command unless proactive routing or interpretation is the actual feature.
2. **Draft the charter.** Record owner, target user, user goal, activation and nonactivation boundaries, inputs, permitted state changes, tool budget, output contract, escalation, refresh trigger, and retirement rule.
3. **Rank local evidence.** Start with the live local entrypoint, load only the focused reference needed for the unresolved design question, and use examples as integration checks rather than requirements.
4. **Separate evidence.** Preserve `local_corpus_sourced_fact`, `external_research_sourced_fact`, and `combined_evidence_inference_note` boundaries wherever provenance changes confidence or action. Treat unrefreshed public sources as future checks.
5. **Design routing.** Include explicit, implicit, and proactive examples only when intended. Add negative examples and neighboring-agent overlap cases. Resolve overlap by narrowing or merging before adding another permanent route.
6. **Derive authority from process.** Grant a tool only when a named step needs it. Keep approvals for irreversible or ownership-sensitive actions outside the agent unless delegation is explicit and tested.
7. **Specify execution and handoff.** Define context inputs, ordered process, quality criteria, outputs, evidence, stop conditions, bounded recovery, and what the parent or user decides next.
8. **Verify in layers.** Run structural and repository checks, then routing, permission, representative-task, and failure-path scenarios. Record false activations separately from missed activations.
9. **Release proportionally.** When behavior is unverified, use manual invocation, advisory output, or read-only tools. Increase authority only as evidence improves.
10. **Maintain or retire.** Assign an owner and refresh triggers. Retire the agent when its source contract, routing value, or test ownership disappears.

Stop and clarify when user intent, ownership, tool availability, or success criteria remain ambiguous. Use an isolated read-only prototype to discover requirements when useful, but do not present it as production-ready. A useful screening question is: **what must this agent never infer or decide on its own?** The answer often reveals the correct negative triggers, approval boundary, and escalation path more clearly than another paragraph of positive responsibilities.

## User Journey Scenario

**Role and starting state:** An agent-system designer is asked to create a reusable `migration-risk-reviewer`. The parent agent can identify a proposed schema or API migration, but repeated reviews consume context and produce inconsistent findings. The user has local agent-development sources, a representative changeset, and an owner who can decide whether findings block the migration. They do not yet know whether a persistent agent, temporary delegation, checklist, or validator command is the right mechanism.

**Decision being made:** The designer must decide whether the reviewer can own a coherent outcome without taking product or remediation authority. The candidate outcome is narrow: inspect a bounded diff and relevant migration files, classify compatibility and rollout risks, cite evidence, and return findings or a clean result. The parent retains the decision to edit code, approve risk, or deploy. If the reviewer would need continuous negotiation over the same state, unbounded production context, or authority from several owners, this split is rejected or routed to an orchestration design.

**Journey from request to artifact:**

1. The designer classifies the workload. Repeated, evidence-based review with stable inputs supports a persistent specialist. A one-time review uses temporary delegation; a deterministic schema check stays a command; product acceptance stays with the user or named owner.
2. The designer drafts the charter before the prompt: user goal, explicit and implicit triggers, nonactivation cases, repository-scoped inputs, read-only tools, prohibited decisions, findings schema, one bounded recovery attempt, escalation owner, refresh signal, and retirement rule.
3. The designer reads the live local skill entrypoint, then the triggering guide because routing is the main uncertainty, and one complete reviewer example to inspect integrated shape. Archived copies are consulted only for provenance or drift. External pointers are not treated as current evidence in this no-browse pass.
4. The designer writes positive scenarios such as “review this migration for rollout risk,” an implicit case where a migration plan requests compatibility analysis, and negative cases such as ordinary code review, direct implementation, or deployment approval. A neighboring code-review agent is included in overlap tests.
5. The process grants read and search capabilities only because the example agent returns findings. A write-enabled fixer is deferred until read-only runs show reliable routing, evidence, and escalation. This preserves reviewer independence and lowers the cost of an incorrect interpretation.
6. The handoff gives the specialist the scoped diff, relevant project instructions, migration contract, and known constraints. It does not dump unrelated conversation history or secrets. The return includes checked scope, findings with file or artifact evidence, uncertainty, unavailable context, and the next decision owned by the parent.
7. Verification covers a risky migration, a safe migration, an unrelated review that must not route, a missing-context case that must escalate, and a denied write attempt. A clean result must state what was checked instead of inventing concerns to satisfy the reviewer persona.
8. After release, the owner records false and missed activations, unsupported findings, reviewer rework, escalation frequency, and agent version. Authority expands only when evidence supports it. The agent is narrowed, merged, or retired when another mechanism owns the same trigger space more clearly.

**Good outcome:** the user receives a reviewable charter, an agent file derived from it, routing and behavior fixtures, and a named maintenance owner. **Bad outcome:** a generic “migration expert” receives broad tools and declares completion with uncited advice. **Borderline outcome:** a wrapper around one schema validator remains a command unless it adds stable proactive timing, interpretation, and escalation that repeated manual runs show are worth permanent routing.

The transferable lesson is the sequence of decisions, not the migration domain. For a generation, validation, security, or documentation agent, substitute the domain inputs and evidence while retaining the same tests for unique ownership, trigger boundaries, least authority, observable output, failure handling, and lifecycle accountability.

## Decision Tradeoff Guide

Apply the decision at the smallest consequential contract dimension, then reconcile the complete agent. One draft may **adopt** validated identifier syntax, **adapt** its trigger examples, and **avoid** a copied shell grant. Whole-agent labels hide this useful precision. Agreement between sources is necessary evidence for some choices, but it does not establish task fit, host behavior, or acceptable authority by itself.

| decision_option_name | when_to_choose_condition | resulting_action_and_tradeoff | verification_question_prompt |
| --- | --- | --- | --- |
| Adopt when | the local contract, target host, task boundary, and representative checks all support the same clause without task-specific change | reuse the clause and its regression evidence; this preserves consistency, but copied assumptions remain a risk if source or host versions drift | Is this exact choice relevant to the target task, accepted by the active host, and covered by a current check? |
| Adapt when | the underlying pattern is sound but trigger scope, authority, context, output, host syntax, or failure handling differs | preserve the proven principle, record the inference and reason, and add a regression scenario; this improves fit but creates local maintenance responsibility | Which source-backed part is retained, which part changed, what observation justified it, and which test now protects the difference? |
| Avoid when | evidence is thin or contradictory, the task does not need a persistent agent, the capability is unavailable, the authority violates policy, or the outcome cannot be verified | remove the clause, choose a simpler mechanism, reduce authority, defer, or require human approval; this limits autonomy but avoids false confidence and costly recovery | Is avoidance caused by policy, capability, evidence, or task fit, and what condition, if any, permits reconsideration? |
| Cost of being wrong | a false route, excessive tool grant, unsupported finding, hidden loop, or wrong abstraction would consume attention, mutate state, expose data, or obscure ownership | increase negative scenarios, approval controls, rollback clarity, and independent review in proportion to consequence and irreversibility | Can a reviewer name the affected state, who can restore it, what evidence exposes the error, and which permission remains outside the agent? |

Bounded actions refine the primary choices without adding a competing vocabulary:

- **Prototype under Adapt:** test an uncertain route or behavior with manual invocation, advisory output, and read-only tools. A prototype supplies evidence; it does not inherit production status from a successful demonstration.
- **Split under Adapt or Avoid:** separate responsibilities when they have materially different triggers, authority, owners, outputs, or lifecycle needs. Do not split merely because the prompt is long.
- **Defer under Avoid:** name the missing source, capability, owner, or fixture and keep the next observation actionable. Anonymous uncertainty tends to become permanent ambiguity.
- **Retire under Avoid:** remove an existing agent when another maintained mechanism owns its trigger space or when no owner maintains its evidence and tests.

The default is bounded adaptation, not habitual customization. Adopt stable current conventions unchanged when they demonstrably fit. Adapt only with a reason and a linked check. Avoiding a capability can be temporary when evidence or host support is missing, or durable when policy reserves the decision for a human. Record that reason so later maintainers do not mistake a safety boundary for unfinished work or use a reversible experiment to bypass policy.

Use cost of error as an input to design rather than an after-the-fact warning. Read-only, manually invoked, reversible agents may tolerate a smaller scenario set. Proactive agents with write, shell, network, or external-system authority require stronger overlap tests, permission denial, bounded recovery, and rollback ownership. If a reviewer cannot say what to undo and who owns recovery, the proposed authority is not bounded enough to release.

Reclassify a decision only after a material source, host, policy, behavior, or ownership change. Update the charter, prompt clause, and linked checks together. Stable syntax may be adopted while routing remains experimental; localizing uncertainty prevents one disputed capability from forcing blind acceptance or rejection of the whole agent.

## Local Corpus Hierarchy

Classification vocabulary includes canonical, supporting, legacy, duplicate, and conflicting source roles.

The hierarchy answers two different questions that must not be collapsed. For provenance in this frozen corpus, the archived `SKILL.md` is the recorded canonical primary source. For current repository operation, the live entrypoint is the first candidate convention after its contents and validator behavior are checked. “Canonical” therefore does not mean “newest,” and “live” does not mean “correct by recency.” Authority remains claim-specific: a file may govern accepted frontmatter while offering only advisory judgment about prompt length or quality.

| local_source_filepath_value | corpus_hierarchy_role | heading_signal_to_convert | reviewer_question_to_answer |
| --- | --- | --- | --- |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/agent-development/SKILL.md | canonical primary source | Agent Development for Claude Code Plugins; Overview; Agent File Structure | What guidance, warning, or example should this source contribute to Agent Creation Prompt Patterns? |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/agent-development/examples/agent-creation-prompt.md | legacy historical source | AI-Assisted Agent Generation Template; Usage Pattern; Step 1: Describe Your Agent Need | What guidance, warning, or example should this source contribute to Agent Creation Prompt Patterns? |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/agent-development/examples/complete-agent-examples.md | legacy historical source | Complete Agent Examples; Example 1: Code Review Agent; Code Review Summary | What guidance, warning, or example should this source contribute to Agent Creation Prompt Patterns? |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/agent-development/references/agent-creation-system-prompt.md | supporting detail source | Agent Creation System Prompt; The Prompt; Usage Pattern | What guidance, warning, or example should this source contribute to Agent Creation Prompt Patterns? |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/agent-development/references/system-prompt-design.md | supporting detail source | System Prompt Design Patterns; Core Structure; Pattern 1: Analysis Agents | What guidance, warning, or example should this source contribute to Agent Creation Prompt Patterns? |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/agent-development/references/triggering-examples.md | supporting detail source | Agent Triggering Examples: Best Practices; Example Block Format; Anatomy of a Good Example | What guidance, warning, or example should this source contribute to Agent Creation Prompt Patterns? |
| claude-skills/plugins/plugin-dev/agent-development/SKILL.md | supporting context source | Agent Development for Claude Code Plugins; Overview; Agent File Structure | What guidance, warning, or example should this source contribute to Agent Creation Prompt Patterns? |
| claude-skills/plugins/plugin-dev/agent-development/examples/agent-creation-prompt.md | supporting example source | AI-Assisted Agent Generation Template; Usage Pattern; Step 1: Describe Your Agent Need | What guidance, warning, or example should this source contribute to Agent Creation Prompt Patterns? |
| claude-skills/plugins/plugin-dev/agent-development/examples/complete-agent-examples.md | supporting example source | Complete Agent Examples; Example 1: Code Review Agent; Code Review Summary | What guidance, warning, or example should this source contribute to Agent Creation Prompt Patterns? |
| claude-skills/plugins/plugin-dev/agent-development/references/agent-creation-system-prompt.md | supporting detail source | Agent Creation System Prompt; The Prompt; Usage Pattern | What guidance, warning, or example should this source contribute to Agent Creation Prompt Patterns? |
| claude-skills/plugins/plugin-dev/agent-development/references/system-prompt-design.md | supporting detail source | System Prompt Design Patterns; Core Structure; Pattern 1: Analysis Agents | What guidance, warning, or example should this source contribute to Agent Creation Prompt Patterns? |
| claude-skills/plugins/plugin-dev/agent-development/references/triggering-examples.md | supporting detail source | Agent Triggering Examples: Best Practices; Example Block Format; Anatomy of a Good Example | What guidance, warning, or example should this source contribute to Agent Creation Prompt Patterns? |

Interpret the roles with bounded authority:

| corpus_hierarchy_role | may_decide_by_default | must_not_decide_alone |
| --- | --- | --- |
| canonical primary source | frozen provenance, the original integrated contract, and the baseline against which this corpus was generated | current runtime behavior after the active repository or host has diverged |
| supporting context source | current local integration context and candidate operational convention | historical intent or universal effectiveness merely because it is newer |
| supporting detail source | the focused question named by its scope, such as triggering or system-prompt design | unrelated frontmatter, host policy, or lifecycle decisions absent from the source |
| supporting example source | how several rules can compose into one artifact and which edge cases a template exposes | the target agent's user, tools, authority, scope, or production readiness |
| legacy historical source | earlier workflow shape, rationale clues, and regression fixtures | current policy or syntax without comparison and validation |

When sources conflict, use this resolution ladder:

1. Name the exact decision dimension: schema, routing, authority, execution, output, verification, or lifecycle. Avoid arguing about an entire file when only one clause differs.
2. Determine whether the question is normative, operational, historical, or illustrative. The best source can differ for each.
3. Compare the relevant spans and record archive/live lineage so copied text is not counted as independent support.
4. Check explicit current repository policy and validator behavior for structural contracts. Validator acceptance proves parseability, not semantic support.
5. Create the smallest agent fixture that exercises the disputed behavior, including a negative or denied path when authority or routing is involved.
6. Adopt, adapt, or avoid the clause; record the selected and rejected evidence, uncertainty, owner, and linked regression check.
7. Mark the decision blocked when a high-consequence discrepancy remains unresolved. Reduce authority or keep manual approval instead of silently choosing the more permissive source.

A good resolution might use the current validator to establish accepted identifier syntax, the archived skill to explain historical intent, and a routing fixture to confirm a newer live example. A bad resolution copies a legacy example because it looks complete. A borderline resolution adopts a newer live behavior in compatibility mode while preserving the old fixture until migration evidence supports replacement.

Use a lightweight propagation record for material clauses: `source -> decision -> agent artifact -> verification gate`. Update the record when a source changes and rerun only the linked checks first, then broaden if behavior diverges. Repeated exceptions are evidence about the hierarchy itself; if maintainers continually override the same role, revise source ownership or classification instead of accumulating unexplained local adaptations.

## Theme Specific Artifact

Theme specific artifact: an agent charter that makes the design reviewable before frontmatter and system-prompt prose make it look finished. The charter is not a second prompt. It is the source of decisions from which trigger examples, tool grants, process clauses, output requirements, and tests are derived. A field may point to an enforced host policy, but vague inherited language such as “use appropriate tools” is not a completed decision.

| artifact_field_name | artifact_completion_rule | evidence_or_enforcement_hint |
| --- | --- | --- |
| charter_owner | name the person or team responsible for source refresh, prompt changes, incident review, and retirement | repository ownership plus maintenance workflow |
| target_user_and_goal | state who invokes or benefits from the agent and the observable outcome they need | user journey plus representative requests |
| unique_owned_outcome | identify what state or decision the agent owns that a command, skill, parent agent, or neighboring specialist does not | mechanism classification and adjacent routing |
| activation_boundary | define explicit, implicit, and proactive triggers that should route | triggering guidance plus positive fixtures |
| nonactivation_boundary | define nearby requests, ownership decisions, and prohibited assumptions that must not route | negative and neighboring-agent fixtures |
| input_and_context_contract | list required inputs, scope limits, source precedence, sensitive data exclusions, and missing-context behavior | local corpus hierarchy plus handoff tests |
| authority_and_tool_budget | map each granted tool or state mutation to a required process step; list actions reserved for the parent or user | least-privilege review plus denied-capability fixtures |
| execution_process | provide ordered, domain-specific steps, checkpoints, and bounded delegation without restating generic helpfulness | system-prompt design source plus task walkthrough |
| output_and_evidence_contract | define result statuses, required evidence, uncertainty, checked scope, and the next owner decision | worked examples plus output schema checks |
| recovery_and_escalation | classify missing context, unavailable tools, failed verification, and contradiction; bound retries and name the escalation owner | failure injection plus retry guidance |
| verification_gate_rule | name structural, routing, permission, representative-task, failure-path, and reviewer checks that establish the approved release level | verification gate command set |
| telemetry_and_feedback | record the minimal events needed to distinguish false route, missed route, unsupported result, rework, and recovery outcome | metrics and observability sections |
| refresh_and_retirement | define material source, host, policy, behavior, or ownership changes that trigger review, and criteria for merge or removal | source dependencies plus portfolio review |

A compact filled charter for the running example looks like this:

| charter_decision | migration-risk-reviewer example |
| --- | --- |
| owner and user | platform-maintenance team owns the prompt; migration authors and reviewers consume findings |
| goal and owned outcome | inspect a scoped migration change and return evidence-bearing compatibility and rollout findings or a clean checked result |
| trigger | requests to assess a concrete migration, including an explicit diff or bounded file set |
| must not trigger | ordinary style review, implementation requests, deployment approval, or risk acceptance without a scoped migration artifact |
| context | scoped diff, migration files, relevant project instructions, and declared compatibility constraints; unrelated conversation and secrets are excluded |
| authority | read and search repository material; do not edit, commit, deploy, approve, or infer product tolerance |
| output | checked scope, prioritized findings with evidence, uncertainty or unavailable context, clean result when justified, and the next decision owned by the parent |
| recovery | retry one transient read failure; otherwise return blocked with the missing input or tool and escalate to the parent |
| verification | validate artifact structure; test risky, safe, unrelated, missing-context, overlap, and denied-write scenarios; reread the complete prompt |
| lifecycle | review after material source or host change, a severe miss, or a meaningful sample; expand authority only with evidence; retire on overlap or owner loss |

**Bad charter:** “Help users with migrations using whatever tools are needed and provide a useful report.” It leaves routing, authority, evidence, and completion open to incompatible interpretations. **Borderline charter:** “Run the schema validator whenever migrations change.” This remains a command or hook unless the proposed agent adds stable routing, interpretation, escalation, and lifecycle ownership that repeated use shows are valuable.

The charter passes review only when two independent implementers would derive materially similar authority and completion behavior, every granted tool maps to a process step, every process step maps to an output or checkpoint, and each material field has an enforcing mechanism or observable violation. Material charter changes must update the generated prompt and linked fixtures in the same review so the design contract and runtime artifact cannot drift independently.

## Worked Example Set

These mini-cases demonstrate decision quality across the complete agent contract. They are worked designs, not measured production results and not templates to copy unchanged. Replace domain inputs, owners, tools, and fixtures with current repository facts.

**Good example: bounded migration-risk reviewer.**

- **Fit:** repeated reviews share a stable diff-and-migration input, compatibility criteria, and an owner who decides remediation. A persistent read-only specialist provides useful context isolation without taking product or deployment authority.
- **Sources:** the designer reads the live skill entrypoint, the triggering reference for routing uncertainty, and one complete reviewer example for composition. Archive/live duplication is recorded once; unrefreshed public pointers do not become current claims.
- **Routing:** explicit migration-risk requests, a bounded implicit compatibility-review case, and intended proactive timing are paired with nonactivation cases for ordinary code review, implementation, and deployment approval. A neighboring code reviewer is included in overlap fixtures.
- **Authority and context:** every read/search tool maps to inspection. The handoff includes only the scoped diff, migration contract, relevant instructions, and known constraints. Write, commit, deploy, and risk-acceptance authority remain outside the specialist.
- **Output and recovery:** the agent returns checked scope, findings with file or artifact evidence, uncertainty, unavailable context, and the next parent decision. A safe migration may return no findings with a checked-scope statement. One transient read retry is allowed; persistent failure returns a blocked result.
- **Evidence:** structural validation, risky and safe task fixtures, unrelated and overlap routes, missing-context escalation, and denied write behavior pass before automatic use. Host-level behavior not exercised remains explicitly unverified.

This example is good because every source and prompt clause changes an observable decision. It can still fail if the repository requires external production context or if findings require product judgment not present in the handoff; those cases escalate rather than invite inference.

**Bad example: universal engineering helper.**

The request “create an expert agent that helps with code, uses all available tools, acts proactively, and ensures quality” is converted directly into a confident persona. Its trigger matches implementation, review, debugging, testing, and documentation tasks already owned elsewhere. It copies a full-access tool list from an example, accepts the entire conversation as context, retries until success, and returns a polished summary without checked scope or evidence.

This design fails source relevance, unique ownership, negative routing, least privilege, bounded recovery, and output verification. A parser might accept the file, but unrelated requests will route, state may change unexpectedly, and reviewers cannot identify what to undo. The correct response is to reject the persistent specialist, classify the actual user outcome, and route it to an existing agent, a focused skill, a command, direct parent execution, or a newly bounded charter.

**Borderline example: schema-validator wrapper.**

The proposed agent invokes one deterministic validator when migration files change and summarizes failures. Three outcomes are plausible:

| observed_need | preferred_mechanism | evidence_needed |
| --- | --- | --- |
| user explicitly supplies arguments and wants raw pass/fail | command | deterministic input, exit status, and error contract |
| parent needs a reusable method for selecting files and interpreting diagnostics in the same context | skill | stable procedure and current project conventions |
| workflow benefits from proactive timing, bounded source discovery, interpretation across several signals, and escalation ownership | agent | repeated manual handoffs, positive and negative route fixtures, unique output contract, and owner commitment |

Begin with the command or manually invoked read-only prototype when invocation frequency and handoff stability are unknown. Promote it only if repeated evidence shows that routing, interpretation, and recovery provide value beyond command relay. If promoted, preserve the command as the deterministic core and test the agent's distinct coordination behavior around it.

Across all three cases, use the same categories of fixtures so differences are attributable to design rather than a changing task. Include a clean input, a real failure, missing context, an unrelated request, a neighboring route, an unavailable tool, and an escalation. Static review can reject obvious defects without deploying them; uncertain routing should be explored in manual or shadow mode before authority grows.

## Outcome Metrics and Feedback Loops

The seed's leading indicator remains useful: a well-bounded prompt should reduce avoidable clarification and unverifiable claims on comparable tasks. It is not sufficient alone. An agent can ask fewer questions by guessing, or produce shorter reviews that omit evidence. Measure routing, task quality, authority, recovery, effort, and user outcome together, and distinguish proposed targets from observed results.

Use a minimal event record for each sampled run:

| metric_dimension | event_or_denominator | interpretation_and_action |
| --- | --- | --- |
| route opportunity | expected agent, actual route, agent version, and task class | record false activation and missed activation separately; narrow or broaden examples based on inspected cases |
| clarification quality | necessary and avoidable clarification counts on comparable inputs | fewer avoidable questions is positive only when unsupported assumptions and failure rates do not rise |
| evidence completeness | required output fields, checked scope, supported findings, and reviewer-confirmed unsupported claims | revise context, process, or output clauses according to the missing category |
| authority compliance | tools used, state changed, approvals requested, and denied-capability outcome | any unexplained or prohibited authority use triggers immediate review regardless of sample size |
| recovery outcome | transient retry, blocked return, escalation owner, and silent or false success | replace repeated retries and ambiguous success with classified, bounded recovery |
| reviewer rework | corrections, reruns, manual reconstruction, and time spent reaching an actionable decision | investigate whether routing, evidence, or output compression caused the burden |
| user outcome | accepted result, bypass, manual redo, abandonment, or mechanism substitution | bypass and redo can reveal low trust even when formal checks pass |
| efficiency context | source count, tool calls, wall time, and input size where meaningful | compare only similar task classes and never trade correctness or control for lower counts alone |

Establish a baseline from the pre-agent workflow or the first bounded release. Record agent and host version so outcomes can be attributed to a specific contract. Segment observations when repository, risk, or task class changes expectations. Low-volume agents may never justify stable percentages; use consequence-weighted case review rather than pretending a tiny denominator supports precise rates.

**Illustrative record shape, not a universal threshold:** “Among 40 reviewer-labeled routing opportunities for version 3, three unrelated code reviews activated the migration agent and one migration review was missed. Two false activations cited no migration artifact. Decision: require a scoped migration input, add both unrelated fixtures to the negative set, and rerun the held-out routing cases.” A bad record says only “usage increased.” A borderline record claims faster runs while the new sample contains smaller changesets.

Use this feedback loop:

1. Validate that event records are complete and that reviewers agree on a shared fixture set.
2. Classify the defect as routing, context, authority, process, output, recovery, source drift, or ownership.
3. Change the smallest contract dimension that explains the evidence and update its charter field and linked fixtures.
4. Re-run the targeted cases, a held-out scenario set, and whole-agent reconciliation so a local fix does not introduce contradiction.
5. Review after a meaningful local sample, a material source or host change, a severe miss, or an authority incident. Do not churn the prompt after every noisy observation.
6. Expand authority only when safety and task evidence improve together. Narrow, merge, or retire when another mechanism provides the outcome with lower routing and maintenance cost.

The original failure signal also remains: a reference that prescribes action without context budget, escalation, or observable completion is not operational. Additional failure signals include rising false routes, unsupported findings, user bypass, reviewer disagreement, repeated blocked runs, or tools that cannot be mapped to required steps. Invocation count, prompt length, output length, and raw speed are diagnostic context, not standalone success measures.

Run the repository verifier after every generated-reference edit and refresh external dependencies when relevant public contracts, installed tooling, or host behavior materially change. Verification protects structure and known fixtures; outcome review tests whether the agent boundary still creates value. A successful feedback loop may end by retiring the agent rather than continually enlarging its prompt.

## Completeness Checklist

Use this checklist as a release gate and evidence index, not as proof by box count. An item is complete only when the decision is relevant, internally consistent, and linked to an artifact, enforcing mechanism, scenario, command, or named reviewer criterion. “Not applicable” requires a reason and a boundary that enforces the omission. After item checks pass, reread and exercise the complete agent because individually plausible clauses can still conflict.

**Purpose and mechanism**

- [ ] The role scenario names the target user, starting state, concrete outcome, current owner, and decision that the agent may make.
- [ ] The design explains why a persistent agent is preferable to direct parent execution, temporary delegation, a skill, command, hook, or project instruction.
- [ ] The unique owned outcome is stable enough to reuse and does not continuously share one decision or mutable state with another agent.
- [ ] The decision guide applies Adopt when, Adapt when, Avoid when, and Cost of being wrong at the relevant clause level, with reasons and re-entry conditions.

**Evidence and source hierarchy**

- [ ] The local corpus hierarchy identifies canonical, live supporting, detail, example, and legacy roles, or gives a specific confidence warning.
- [ ] Archive/live counterparts are treated as one lineage rather than independent corroboration.
- [ ] Every high-consequence factual claim resolves to an inspected source; every material synthesis is labeled and bounded.
- [ ] Public pointers include freshness or version status. Unrefreshed sources are not presented as current behavioral evidence.
- [ ] Source conflicts record selected and rejected evidence, the decision dimension, uncertainty, owner, and linked check.

**Charter, routing, and authority**

- [ ] The theme-specific charter is concrete enough to review without reading every mapped source and names owner, user goal, trigger, tools, output, escalation, refresh, and retirement.
- [ ] Positive scenarios cover intended explicit, implicit, and proactive routing only where each is required.
- [ ] Negative scenarios cover nearby requests, prohibited assumptions, and neighboring-agent overlap.
- [ ] Required inputs, source precedence, scope limits, sensitive-data exclusions, and missing-context behavior are explicit.
- [ ] Every granted tool and state mutation maps to an approved process step; prohibited decisions and actions are named.
- [ ] Irreversible, policy-sensitive, or ownership-sensitive actions remain with the user or parent unless delegation and rollback are explicit and tested.

**Execution, output, and recovery**

- [ ] The prompt defines ordered domain steps, checkpoints, quality criteria, and a stop condition rather than generic helpfulness.
- [ ] The output contract names statuses, checked scope, required evidence, uncertainty, unavailable context, and the next owner decision.
- [ ] A clean result is permitted and must state what was checked; the persona does not reward invented findings.
- [ ] Retry classes and budgets are bounded, persistent failure returns a blocked or escalation result, and delegation cannot loop between agents.
- [ ] The parent-to-specialist handoff and specialist-to-parent return preserve enough provenance to review the outcome without copying unrelated context.

**Examples, gates, and evidence**

- [ ] Worked examples cover good, bad, and borderline usage and explain the deciding condition rather than offering slogans.
- [ ] Structural validation checks file location, accepted metadata, required fields, identifier rules, and forbidden placeholder language.
- [ ] Routing tests include intended routes, nonroutes, and overlap cases; false activation and missed activation are reported separately.
- [ ] Permission tests include at least one denied or absent unnecessary capability.
- [ ] Representative task tests include normal, clean, missing-context, tool-failure, and escalation outcomes where relevant.
- [ ] The repository verifier command, scope, exit status, and decisive results are recorded. Unrelated broad-suite failures are classified rather than hidden.
- [ ] Behavior not exercised in the active host is reported as unverified and causes a narrower release level.

**Metrics, ownership, and routing away**

- [ ] The metrics section names a leading indicator, failure signal, denominator or qualitative review method, agent version, and resulting action.
- [ ] Efficiency metrics are paired with correctness, evidence, authority, and user-control signals.
- [ ] The adjacent routing section points to a better mechanism or reference when this one is not the right fit and explains the handoff evidence.
- [ ] A named owner maintains sources, fixtures, incidents, prompt changes, and retirement decisions.
- [ ] Material source, host, policy, behavior, or ownership changes trigger affected checks plus complete reconciliation.
- [ ] Retirement or merge criteria prevent stale and overlapping agents from remaining in the routing portfolio indefinitely.

**Completion interpretation:** A full pass means the charter, agent file, source ledger, fixtures, command evidence, owner record, and complete reread agree. A structural pass without host behavior supports only **structurally verified, behaviorally unverified** status and should disable proactive routing or consequential authority. A failed item blocks release at the affected authority level; marking the box because relevant prose exists is not sufficient.

Sample traceability in both directions. Each consequential charter decision should reach a prompt clause and gate, and every capability in the prompt should resolve back to an approved charter need. If one reviewer cannot explain the path from user request through route, action, evidence, return, and recovery without hidden conversation, the handoff remains incomplete.

## Adjacent Reference Routing

This reference owns the integrated decision to create or materially revise a persistent agent. Route away when the remaining uncertainty is narrower than that decision or when a different mechanism owns the user outcome. Do not route by the mere presence of words such as “agent,” “creation,” or “prompt.” Route by the next consequential decision, the evidence required to make it, and the owner who will integrate the result.

| unresolved_decision | preferred_route | expected_return_to_this_reference |
| --- | --- | --- |
| Is a persistent agent the right mechanism? | mechanism comparison covering direct parent work, temporary subagent, skill, command, hook, project instruction, and persistent agent | selected mechanism, unique owned outcome, rejected alternatives, and consequence analysis |
| Which requests should activate or not activate the agent? | local triggering examples or routing-focused reference | positive, implicit, proactive, negative, and neighboring-agent fixtures with observed or expected route labels |
| How should responsibilities, process, quality, output, and edge cases be written? | local system-prompt design reference | prompt clauses mapped to charter decisions, with generic filler removed |
| How should a request be converted into an initial configuration? | assisted agent-generation prompt or creation workflow | candidate identifier, use description, and system prompt that remain untrusted until charter and tests reconcile them |
| Should one specialist receive a delegated subtask? | subagent or delegation reference | handoff input, context exclusions, output schema, ownership, merge point, and stop condition |
| What context should be loaded, summarized, or excluded? | context-engineering or dependency-narrowing reference | ranked context set, token or file budget, provenance, excluded material, and refresh rule |
| Which architecture or authority option is preferable under real disagreement? | evidence-based debate or decision-analysis workflow | options, constraints, strongest counterarguments, convergence or unresolved dispute, and named adjudicator |
| What proves the artifact or behavior is acceptable? | verification, testing, or review-gate reference | commands, fixtures, reviewer criteria, results, untested claims, and approved authority level |
| How should a deployed agent retry, checkpoint, report, or stop? | reliability, backpressure, or progress-journal reference | failure classes, budgets, persisted state, escalation, and recovery evidence |
| Has the agent become stale, overlapping, or ownerless? | lifecycle or portfolio review | keep, narrow, merge, replace, or retire decision with migration and ownership plan |

Use a route-and-return loop:

1. State why this reference cannot decide the remaining question from its current evidence.
2. Transfer one bounded decision, the relevant charter fields, inspected sources, constraints, and current uncertainty.
3. Exclude unrelated conversation, broad source dumps, and authority the specialist does not need.
4. Require a concrete return artifact and a condition for success, blocked status, or escalation.
5. Integrate the result through one owner who reconciles trigger, tools, process, output, and tests across the full agent.
6. Stop if the same unresolved condition returns unchanged. Track visited routes so circular reference or agent delegation is visible.

**Good route:** “The migration reviewer overlaps the general code reviewer. Inspect the local triggering guide and return five labeled route fixtures, including two nonactivation and one overlap case; do not redesign tools or output.” The result updates the charter and routing tests. **Bad route:** “Use the prompt reference to improve this agent.” It transfers no decision, evidence, owner, or return condition. **Borderline route:** an architecture debate is delegated without an adjudicator; it becomes useful only after options, constraints, authority consequences, and the person or policy selecting the outcome are named.

Keep coupled decisions together. Trigger scope, context requirements, authority, and output can depend on one another; splitting them among specialists without an integration owner creates locally sound but globally contradictory clauses. Independent review is useful for high-risk choices when it is intentional and converges through named criteria. Repeated routing around one task is a design signal: the proposed agent may be too broad, its ownership unclear, or a simpler mechanism more appropriate.

If a stable adjacent path is unavailable, search by the decision category and require the same return contract rather than inventing a filename. A successful handoff reduces the unresolved decision surface. Consulting more references or agents without changing the charter, evidence, or release status is activity, not resolution.

## Workload Model

`combined_evidence_inference_note`: Treat Agent Creation Prompt Patterns as an agent-workflow operating reference, not as a prose summary. Its workload model protects decision coherence, context attention, tool authority, and review capacity. File and subtask counts are only rough pressure indicators; semantic coupling and consequence determine whether one owner can safely finish the work.

| workload_dimension_name | workload_boundary_value | verification_pressure_point |
| --- | --- | --- |
| primary_usage_surface | agent planning, tool use, context loading, delegation, or skill/plugin execution where bad guidance compounds across long-running sessions | verify that the reference changes the next charter, implementation, test, authority, or review decision |
| bounded_capacity_model | one primary task, up to 10 source files, up to 3 delegated subtasks, and a written completion audit for every run | treat these seed values as conservative starting guardrails; split, stage, or document a justified exception when exceeded |
| source_pressure_model | local heading signals include Agent Development for Claude Code Plugins; Overview; Agent File Structure; Complete Format; Frontmatter Fields; name (required); AI-Assisted Agent Generation | rank sources by the active question, compare against current local contracts, and stop loading when more material no longer changes the agent design |
| coupling_pressure_model | one owner integrates trigger, context, authority, process, output, recovery, and tests; delegated work must have disjoint evidence questions or explicit merge coordination | reject parallel fanout when results depend sequentially, agents edit shared state, or no adjudicator resolves contradiction |
| authority_pressure_model | the agent receives only capabilities mapped to approved process steps; broader tools require stronger tests, approval, and rollback ownership | narrow or stage authority when a failure could mutate shared state, expose sensitive data, or cross ownership boundaries |
| artifact_pressure_model | required artifact is an agent charter with owner, user, trigger, tool budget, output, escalation, refresh, and retirement, plus linked verification evidence | require the artifact and evidence index before claiming the reference is operationally usable |
| completion_pressure_model | unresolved decisions, source conflicts, retries, merge corrections, and reviewer burden remain small enough for one skeptical whole-artifact reread | checkpoint, narrow, or redesign when activity grows but unresolved decisions do not converge |

The values “up to 10 source files” and “up to 3 delegated subtasks” are retained from the seed as planning guardrails, not measured universal capacity claims. Ten large or overlapping files may be too much; more than ten small, precisely indexed sources may remain manageable. Three independent read-only investigations can be safer than one specialist sharing a mutable file with the owner. Exceed a guardrail only with a reason, a revised context or merge plan, and a check for contradiction or lost provenance.

Operate the workload in bounded stages:

1. **Name one owned outcome.** Count unresolved decisions across routing, authority, process, output, and lifecycle. If several require different owners or approvals, split by outcome before loading more sources.
2. **Rank evidence.** Select the smallest source spans that answer the next consequential question. Record why each source is loaded and what was intentionally excluded.
3. **Automate deterministic extraction.** Use parsers, validators, or dependency tools for inventory and structure before delegating judgment, leaving agent attention for comparison and synthesis.
4. **Delegate only independent work.** Give each subtask immutable or disjoint inputs, one question, an output contract, context exclusions, and a return condition. Serial execution is preferable when one answer determines the next question.
5. **Checkpoint after each batch.** Record decisions resolved, new uncertainties, sources loaded, tool use, retry class, and next owner. A rising unresolved-decision count is a stop signal even when nominal budgets remain unused.
6. **Reconcile through one owner.** Compare returned evidence, resolve conflicts, update the charter and prompt, and run linked gates. Parallel completion is not completion until merge corrections and whole-artifact review pass.
7. **Audit the exception.** When boundaries are exceeded, record source size, delegated work, conflicts, discarded results, wall time, reviewer effort, and whether the extra capacity changed the final decision.

**Good example:** one owner reads the skill entrypoint, a triggering reference, and a relevant complete example, then delegates two independent read-only checks for route overlap and validator coverage. Both return fixtures and no shared edits. **Bad example:** three agents receive the same ten files and are asked to “improve the prompt,” producing overlapping rewrites with no adjudicator. **Borderline example:** twelve small schemas exceed the file guardrail but are selected by exact references, summarized deterministically, and reviewed through one owner; the exception is justified by low coupling and retained provenance.

Escalate capacity in this order: narrow the question, select smaller source spans, stage serial batches, summarize with provenance, use a temporary specialist, introduce deterministic tooling, then adopt coordinated multi-agent execution with explicit ownership and merge gates. Each step adds capability and cost. Choose the least complex option that preserves the evidence needed for the next irreversible decision.

Measure local workload behavior rather than manufacturing universal limits. Useful observations include source count and size, decisions resolved, delegated tasks, conflicts, retries, discarded work, merge correction, wall time, and reviewer decision time on comparable tasks. Repeated source overload suggests better indexing; repeated merge conflict suggests a bad ownership split; repeated retry fanout suggests weak failure classification. Redesign the charter or architecture only after recurring pressure, not one exceptional run.

## Reliability Target

The values below are release-policy targets retained from the seed. They are not observed performance results, probabilities, or universal thresholds for every agent host. Report each target as **met**, **unmet**, or **insufficient evidence**, with agent and host version, denominator, failure severity, and approved authority level. Do not translate an unmeasured target into a present-tense reliability claim.

| reliability_target_name | measurable_threshold_value | evidence_collection_method | capability_consequence |
| --- | --- | --- | --- |
| source_boundary_preservation | 100 percent of recommendations keep local, external, and inference boundaries visible where provenance changes confidence or action | trace every consequential recommendation to an inspected source or explicit inference; review mixed claims for scope laundering | block reuse of untraceable high-consequence clauses; source labels without relevant support do not pass |
| decision_accuracy_sample | at least 18 of 20 sampled uses route to the correct adopt, adapt, avoid, or adjacent-reference decision | use reviewer-labeled, nonduplicated, versioned cases that include intended, negative, overlap, and borderline decisions | keep manual or shadow routing when the qualified sample is unmet or unavailable; any severe false route receives separate review |
| unsupported_claim_rate | zero unsupported production, security, latency, or reliability claims in final guidance | reject claims without a source row, explicit bounded inference, or a verification method and status | block consequential authority or external reuse until the claim is removed, sourced, or reframed as uncertainty |
| recovery_path_clarity | every avoid or failure case names rollback, blocked state, escalation, or next-reference route, plus the owner of the next decision | inject missing context, unavailable tools, failed checks, contradiction, and persistent failure; inspect retry and routing sections together | disable autonomous retry or state mutation when recovery cannot terminate with an owned outcome |

Add dimension-specific reliability checks for any deployed agent:

- **Routing:** track false activations and missed activations separately. An aggregate pass cannot excuse one high-consequence route into a destructive or privacy-sensitive workflow.
- **Authority:** every used capability must map to the charter and every prohibited capability must remain unavailable or be refused. One unexplained prohibited action blocks authority expansion regardless of average task success.
- **Evidence quality:** findings identify checked scope, supporting artifacts, uncertainty, and unavailable context. A clean result is accepted when its checked scope is explicit.
- **Task outcome:** representative outputs help the named user make the next decision and do not require hidden reconstruction by the parent.
- **Recovery:** transient and persistent failures follow classified budgets, return blocked or escalation status, and never create reciprocal delegation loops.

Qualify the 18-of-20 sample before interpreting it. Cases should be comparable enough for a reviewer to label the expected decision, should not duplicate one template phrasing, and should record the tested prompt and host version. If reviewers disagree on expected routes, clarify the charter or output contract before collecting more cases. A low-volume agent may remain at **insufficient evidence** and use qualitative case review; it must not claim the sample threshold by extrapolation.

**Interpretation examples:** A good report says, “Version 3 met source and unsupported-claim targets; 19 of 20 qualified routing cases matched; the one miss was a low-consequence manual route; recovery fixtures passed; read-only proactive use approved.” A bad report says, “The agent is 90 percent reliable.” A borderline report records 18 of 20 correct routes but one prohibited shell attempt; the aggregate target passes while the authority hard stop fails, so write or execution authority remains disabled.

Stage capability according to relevant evidence: structural validation before any use, manual read-only invocation before proactive routing, reversible test-environment writes before shared-state mutation, and explicit approval plus rollback before external actions. If a later source change, severe incident, version change, or ownership loss invalidates evidence, downgrade the affected capability and rerun the linked checks. Reliability debt is the gap between granted authority and verified behavior; keep that gap visible instead of allowing capability to grow faster than evidence.

## Failure Mode Table

Classify an observed failure before retrying. Preserve the smallest evidence needed to reproduce the decision class: agent and host version, scoped input, expected and actual route or status, capabilities used, decisive output evidence, and current owner. Do not retain raw sensitive context when redacted fixtures or hashes can establish the same boundary.

| failure_mode_name | likely_trigger_and_detection_signal | immediate_containment | recovery_and_prevention |
| --- | --- | --- | --- |
| source drift hides truth | external or local guidance changes after the reference was written; prompt clause no longer matches inspected source or installed behavior | mark affected claims stale and disable authority that depends on them | refresh the relevant evidence, update the claim-to-clause record, and replay linked routing or behavior fixtures before reuse |
| generic advice escapes review | agent copies plausible best practices without theme-specific evidence; reviewer cannot name what changes if the clause is removed | block reusable completion and delete nonoperative prose | require a relevant source or bounded inference plus a command, scenario, or reviewer criterion that can fail |
| context window loses plan | long-running session forgets constraints, expands scope, or overwrites user intent; checkpoints and current actions disagree | stop new or destructive actions and preserve current state | write and reread a concise plan checkpoint, restore owner and next decision, then resume only the first verified step |
| tool fanout outruns budget | parallel actions conflict, duplicate work, or create unbounded external calls; unresolved decisions and merge corrections grow | halt new fanout and prevent shared-state writes | cap concurrency, assign disjoint ownership, classify completed results, and require merge plus audit checkpoints |
| trigger boundary overfires | unrelated or neighboring requests activate the agent | disable proactive routing or require manual invocation | add negative and overlap fixtures, narrow description language, and inspect portfolio ownership |
| trigger boundary underfires | representative intended requests remain with the parent or route elsewhere | retain direct parent fallback rather than forcing dispatch | add missing intent variants only after confirming the task belongs to this agent and does not broaden overlap |
| authority exceeds charter | an unexplained tool is invoked, prohibited state is changed, or approval is inferred | stop the action, revoke or narrow the capability, and preserve rollback evidence | map tools to steps, test denied capabilities, restore affected state through the named owner, and independently review before expansion |
| evidence is fabricated or untraceable | findings lack checked scope or cited artifacts, or a persona invents issues on a clean input | reject the result and prevent consequential action based on it | require evidence-bearing outputs, include clean fixtures, and permit explicit uncertainty or no-finding status |
| completion is ambiguous | agent returns polished prose without pass, findings, blocked, escalation, or next-owner state | treat the run as incomplete | define output statuses and required fields; test that the parent can act without reconstructing hidden context |
| retry or delegation loops | the same failed check repeats, tools are broadened after failure, or agents hand the same condition back and forth | open the circuit after the configured budget and stop state mutation | classify transient versus persistent failure, retain one owner, track visited handoffs, and return blocked or escalation |
| output exceeds review capacity | result volume hides decisive findings or requires the parent to reread all inputs | stop additional generation and preserve raw evidence separately | prioritize by consequence, return a bounded summary with pointers, and split only by independently reviewable outcome |
| ownership or lifecycle disappears | source, fixtures, escalation, or retirement no longer has a maintainer | disable automatic or consequential use | transfer ownership with explicit acceptance, merge into a maintained mechanism, or retire the agent and migrate routes |

Use a common response protocol: **detect -> contain -> classify -> preserve evidence -> recover through a named owner -> verify -> restore only the proven authority**. Containment comes first when continued execution can mutate state, expose data, or create more fanout. A successful retry does not prove the original cause is fixed; replay the failure fixture and a neighboring regression case before restoring the prior release level.

The agent and the parent have different recovery responsibilities. The agent may retry a declared transient read, return a blocked status, or request a named input. The parent or human owner performs policy decisions, state rollback, credential repair, source refresh requiring broader access, and authority restoration. If no actor can perform the named mitigation, the charter is incomplete and the capability stays disabled.

**Good response:** a prohibited write attempt immediately stops the run, preserves the attempted path, returns blocked, and causes write authority to remain disabled until mapping and denial fixtures pass. **Bad response:** the agent broadens tools and retries because the task “must succeed.” **Borderline response:** a refreshed source makes the next run pass, but the original route cannot be reproduced; keep manual or read-only use until cause and regression evidence are understood.

Review recurring categories across versions. Repeated source overload suggests indexing work, repeated overlap suggests a bad portfolio boundary, repeated context loss suggests smaller checkpoints, and repeated retry fanout suggests weak error classification. Redesign only with causal evidence, but do not keep patching prompt wording when failures consistently point to ownership or architecture. A downgrade path can preserve advisory value while deeper repair proceeds.

## Retry Backpressure Guidance

Retry only after the failed signal is classified and the agent can name what changed that makes another attempt plausibly succeed. Before retrying, determine whether the previous action had side effects, whether repeating it is idempotent or safely compensated, whether the same dependency is already being retried by a delegate, and whether the shared budget remains. Optimism is not a changed condition.

| failure_class | retry_or_backpressure_decision | required_terminal_evidence |
| --- | --- | --- |
| transient side-effect-free read | permit one immediate bounded retry, optionally with locally configured delay, when the dependency reports a clearly retryable condition | original failure, retry count, changed timing or connection condition, and final result |
| stale external evidence | refresh once within the seed's one-retry policy, then escalate to a human or narrower source-specific reference if freshness or compatibility remains unresolved | prior and refreshed source status, affected claim, and whether the prompt clause or release level changed |
| missing context | do not repeat the same action; request the named input or return blocked when the owner cannot provide it | missing field or artifact, requesting owner, and resume point |
| true contradiction | do not retry generation in hope of a different answer; preserve competing evidence and route to the named adjudicator | disputed decision dimension, sources, consequence, and adopted, adapted, avoided, or unresolved outcome |
| failed deterministic verification | fix the identified artifact or contract once, then rerun the focused gate before broad checks | failing assertion, changed file or clause, focused result, and regression status |
| ambiguous write or external action | stop; do not repeat until authoritative state reconciliation establishes whether the first action succeeded | remote or shared-state observation, idempotency key or compensation plan, and rollback owner |
| unavailable capability | return blocked or use an approved fallback that preserves the contract; never broaden tools as a retry tactic | unavailable capability, fallback's evidence-quality difference, and resulting authority or confidence level |
| persistent dependency failure | open a scoped circuit breaker after budget exhaustion and stop dependent work while allowing disjoint safe evidence collection | affected dependency, last safe checkpoint, blocked tasks, owner, and next review condition |

Retry budgets are shared across the parent, nested tools, and delegated agents for the same failing condition. Delegation must not reset the count. A fallback that changes source authority, output quality, or task semantics is an adaptation and must narrow confidence or release status; it is not a transparent retry. Timing and jitter for truly transient dependencies are local policy and should be tuned from observed behavior rather than invented as universal constants.

Apply backpressure by stopping new dependent generation or implementation when source coverage, critique coverage, permission boundaries, or verification gates are red. Scope the stop to the affected artifact, capability, or dependency so unrelated read-only work may continue when it cannot compound the failure. Contain first when further execution can mutate state, expose data, or create fanout.

For long-running workflows, checkpoint after each batch and before any broad rewrite, commit, push, external action, or destructive operation. A checkpoint records current owner, completed evidence, changed state, exact failing signal, retry budget consumed, unresolved decisions, and the first next action. On resume, reread the current specification and verify external state before continuing; do not trust stale in-memory assumptions.

For distributed execution, assign one owner per generated file or theme batch. Give delegated work disjoint inputs or read-only evidence questions, track visited handoffs, and require merge-time verification of exact path, heading, evidence boundaries, authority, and output invariants. Reciprocal delegation of the same unresolved condition terminates as blocked or escalated rather than looping.

**Good recovery:** a repository read times out once, succeeds on the single retry, and records both events. **Bad recovery:** a timed-out external write is issued again with broader tools because no response was seen. **Borderline recovery:** a stale source refresh succeeds, but the refreshed source contradicts local policy; the refresh retry is complete, while the decision remains blocked for adjudication.

Use failure injection to verify call counts, shared budgets, checkpoint persistence, state reconciliation, circuit breaking, and resume behavior. Repeated failures by class and dependency inform source-pipeline, tool-interface, or ownership redesign. Occasional transient failure does not require architecture change, but retry fanout, ambiguous effects, or recurrent contradiction indicate that prompt wording alone is not the root problem.

## Observability Checklist

Collect observability for a named operational decision: route correction, authority review, source refresh, recovery diagnosis, performance comparison, maintenance, or retirement. More events are not inherently better. Prefer a small structured record that lets the owner reproduce the decision class without retaining the user's entire conversation, repository content, secrets, or raw tool payloads.

For each sampled run, capture this minimum evidence when the host permits it:

| event_group | fields_to_record | decision_enabled |
| --- | --- | --- |
| identity and scope | run identifier, parent or delegated correlation identifier, agent and host version, task class, scoped artifact or fixture identifier | compare like runs and trace a specialist result back to its parent handoff |
| routing | expected route when labeled, actual route, explicit or implicit activation category, neighboring agent considered | separate false activation, missed activation, and portfolio overlap |
| context selection | local sources loaded, relevant spans or hashes, intentionally skipped sources and reason, external freshness status, context budget | detect source drift, indiscriminate loading, and missing required evidence without duplicating source contents |
| authority | tool categories granted and used, state changes attempted, approvals requested, denied or unavailable capability | confirm least privilege and identify unexplained authority or policy boundaries |
| execution and recovery | delegated tasks, retry class and count, shared budget, checkpoint, fallback, circuit-breaker, and escalation owner | distinguish safe recovery, fanout, blocked work, and silent failure |
| verification | exact command or fixture set, scope, exit status, reviewer question, rendered artifact where relevant, and decisive result | identify what a pass actually established and which claims remain untested |
| result | pass, findings, clean, partial, blocked, escalated, or failed status; checked scope; evidence completeness; unresolved risk | let the parent act without reconstructing hidden context |
| feedback | reviewer correction, manual redo, accepted result, leading indicator, failure signal, and resulting keep, revise, narrow, expand, merge, or retire decision | connect telemetry to maintenance rather than passive reporting |

Record p50, p95, and p99 latency only when enough comparable repeated runs make those summaries meaningful and include the denominator, task class, input size, and version. For small samples, report individual observations, median where defensible, or a range without implying tail precision. Reviewer decision time may be more relevant for documentation and analysis agents; interactive routing may care about runtime latency. Neither efficiency measure can substitute for correctness, authority, or user control.

Use risk-based sampling. Retain complete structured records for authority events, severe misses, changed versions, failure and recovery cases, and representative release fixtures. Sample routine low-risk successes when volume is high. Synthetic probes are useful for negative routing, denied capabilities, and status logging because they avoid retaining real user data. Periodic sampled review can complement probes under appropriate access controls.

Apply data minimization throughout the lifecycle:

- Store source identities, selected spans, hashes, or categories when full contents are unnecessary.
- Redact user data, credentials, secrets, and unrelated repository content before persistence.
- Keep status and decision metadata even when payload content cannot be retained.
- Set access, retention, and deletion rules appropriate to consequence; verify that expiration and deletion actually occur.
- Avoid high-cardinality labels that copy user prompts into metric systems.
- Report telemetry gaps explicitly. Missing observability narrows confidence and authority; it does not justify inferring success from fluent output.

**Good record:** “Agent v3, host v8, migration-risk fixture 12; expected and actual route matched; three scoped local sources loaded, two skipped with reasons; read/search only; one transient read retry; six output fields present; clean result with checked scope; reviewer accepted; no unresolved risk.” **Bad record:** a complete raw transcript retained indefinitely with `success=true`. **Borderline record:** “p99 improved” based on six heterogeneous runs; preserve the raw observations and defer the percentile claim.

Test the observability contract by injecting known positive, nonroute, denied-tool, retry, blocked, and escalation outcomes. Confirm records correlate parent and specialist, preserve the expected status and count, redact sensitive payloads, and lead to the intended maintenance action. Confidence in agent behavior and confidence in telemetry completeness are separate statements.

At portfolio level, use aggregated signals to find overlapping routes, recurring blocked conditions, reliability debt, unused agents, and ownerless evidence. Do not optimize for invocation count or shorter output alone. An agent with few justified routes may be appropriately specialized; an agent with no owner and no current value is a retirement candidate even when its historical logs contain no failures.

## Performance Verification Method

Performance verification asks whether the agent improves the user's complete decision journey without weakening routing, evidence, authority, recovery, or control. It is a method, not a claim that this reference or any generated agent has achieved a speedup. Some agents intentionally spend more time to reduce risk or supply independent review; evaluate them against that outcome and the best realistic alternative mechanism.

Require tool-call budgets, timeout budgets, and a resumable journal when the workflow exceeds one focused session. Budgets detect runaway context, fanout, and retries; they are not optimization scores. An agent that uses fewer calls by skipping relevant evidence fails even when it is faster. The journal records current owner, completed work, changed state, failing signal, remaining budget, unresolved decisions, and first next action so interruption cost is part of the measured workflow rather than hidden.

Define a benchmark packet before making a comparative claim:

| measurement_dimension | required_context | quality_guardrail |
| --- | --- | --- |
| workload | task class, fixture or sampled-case identifier, input size, source count and size, relevant risk, expected route | compare equivalent tasks or segment materially different workloads |
| environment | agent and host version, model where recorded, installed tools, caching or cold-start condition, concurrency, and network dependency | bind conclusions to the observed environment rather than claiming universal behavior |
| execution | context loaded, delegated tasks, tool-call count, retry count and class, timeout budget, wall-clock boundaries, blocked and failed runs | include recovery and failed-run cost; do not report only successful fast paths |
| latency summary | raw per-run observations plus p50, p95, or p99 only when enough comparable runs support those summaries | publish denominator and retain raw results so summaries can be recomputed |
| human effort | clarification count and quality, reviewer decision time, corrections, manual reconstruction, and reruns | fewer questions or shorter review is positive only when assumptions and error do not rise |
| result quality | expected and actual route, checked scope, evidence completeness, unsupported claims, authority compliance, recovery, and next-action clarity | a performance pass is invalid when the approved quality or authority level changes silently |
| comparison | direct parent, command, skill, earlier agent version, or other realistic baseline | compare end-to-end user outcome, not model execution in isolation |

The seed's leading indicator remains: on comparable tasks, the next run should need fewer avoidable clarifications and produce fewer unverifiable claims. Its failure signal also remains: the reference tells agents what to do without defining context budget, escalation, or an observable stop. Add reviewer rework, false routes, permission violations, repeated blocked states, and user bypass as quality counterweights.

Use a proportional protocol:

1. Freeze or classify representative fixtures and define the start and stop boundaries of wall time and reviewer time.
2. Capture a baseline with the alternative workflow and the same verification requirements.
3. Run the candidate with versioned configuration; include clean, failure, and recovery cases rather than only successful tasks.
4. Validate raw record completeness and fixture equivalence before computing summaries.
5. Compare the user's time to a correct next decision, evidence quality, and recovery burden. Report speed, quality, and authority confidence separately.
6. Repeat stable synthetic fixtures for regression detection and sample real tasks for transfer, with privacy controls.
7. Diagnose the dominant cost before optimizing: source loading, model execution, tool latency, retries, handoff, merge correction, or reviewer reconstruction.

For small or heterogeneous samples, report observations, ranges, and bounded qualitative judgment rather than unsupported tail percentiles. For repeated comparable runtime work, p50, p95, and p99 may be useful when denominator and conditions are explicit. Documentation and analysis workflows often care more about reviewer decision time and correction burden. Context offloading may lower active tokens while increasing retrieval time; measure the net effect on evidence and decision speed.

**Pass condition:** the reference lets a reviewer identify the correct next action, verification gate, approved authority, residual uncertainty, and stop condition without reading unrelated files, and the measured workflow meets the locally declared performance goal without regressing quality. **Fail condition:** implementation begins before workload, reliability target, and failure modes are explicit, or an efficiency claim excludes failures, changes fixtures, mixes versions, or weakens evidence.

Performance overhead can diagnose design. Repeated context reload suggests a poor handoff, merge correction suggests conflicting ownership, and retry time suggests weak failure classification. Some overhead is justified by independent review or safer authority; state that tradeoff instead of optimizing it away. Optimize the bottleneck that controls the user's next decision, not the easiest counter to reduce.

## Scale Boundary Statement

Agent Creation Prompt Patterns stops being sufficient as the sole operating guide when a workflow crosses independent systems, multiple decision owners, unbounded source discovery, shared mutable state, or production traffic without explicit reliability and recovery contracts. The reference remains useful for each specialist charter, but the composed system also needs architecture, message contracts, policy enforcement, observability, failure isolation, and end-to-end verification.

Do not use raw counts as the boundary. Two read-only systems under one owner may remain a bounded advisory agent; two mutating systems with independent owners may already require coordination and compensation. Diagnose scale through these questions:

| boundary_signal | prompt_only_response_is_insufficient_when | required_next_control |
| --- | --- | --- |
| system coupling | output from one system controls mutation in another or partial success creates inconsistent state | typed handoff, idempotency or compensation, correlation, and partial-failure tests |
| ownership | several teams or policies can approve, rollback, or reinterpret the same outcome | explicit decision rights, escalation, integration owner, and change review |
| shared artifacts | multiple agents can rewrite the same file, plan, ticket, or external record | single writer or merge queue, version checks, conflict policy, and post-merge verification |
| source discovery | context cannot be ranked or bounded and agents repeatedly rediscover the same corpus | dependency or source graph, indexed retrieval, provenance-preserving summaries, and stop criteria |
| authority composition | individually narrow agents can sequence actions into broader effective capability | composed authority review, cross-agent policy, approvals, and denied-sequence tests |
| runtime demand | user traffic creates latency, availability, throughput, concurrency, or queue expectations | local SLOs, load and recovery evidence, backpressure, monitoring, and capacity ownership |
| workflow duration | context drift, external-state change, interruption, and stale checkpoints become routine | persisted state, resumable journals, reconciliation on resume, and lifecycle cleanup |

The conservative distributed pattern is one integration owner or coordinator for user intent and end-to-end outcome, plus specialists with bounded inputs, distinct authority, independent failure domains, and typed or structured returns. Component owners verify their local contracts; the integration owner verifies cross-boundary behavior. Disjoint read-only work may run concurrently. Sequentially dependent decisions or shared writes remain serial until a stable interface and merge mechanism exist.

Under distributed execution, split by owned outcome or evidence question rather than arbitrary line or file count. Preserve one writer or verification owner per artifact or theme batch. Do not let parallel agents rewrite the same reference without a merge checkpoint, exact heading and evidence-boundary checks, and complete reread. If specialists disagree, a named adjudicator applies declared criteria; reciprocal delegation is not resolution.

Under long-running workflows, treat context drift as a reliability failure. Checkpoint owner, completed state, external effects, open risks, retry budgets, blocked conditions, and first next action. On resume, verify external state and current specifications before broad rewrite, commit, push, or destructive work. A stale summary is an input to revalidation, not proof that the environment remained unchanged.

Under large-codebase scale, require dependency or source-graph narrowing before applying this reference. A source list without ranked canonical guidance, relevant spans, provenance, and an exclusion rationale is not enough. Move deterministic inventory, schema validation, and stable coordination into code or workflow infrastructure rather than expanding a prompt to rediscover them on every run.

**Good scaled case:** several read-only specialists inspect disjoint migration evidence and return structured findings to one release-risk owner; no specialist shares writes, and partial failures are visible. **Bad scaled case:** several agents edit the same reference and external tracker while each has its own retry loop and no merge owner. **Borderline case:** one advisory agent reads two external services without measured SLOs; keep manual bounded-batch use, disclose freshness and availability uncertainty, and defer automatic production routing.

Verify component schemas and prompts, then test the composed authority and state transitions: correlation, policy consistency, partial failure, retry budgets, idempotency, compensation, stale messages, merge conflict, load, and claimed SLO behavior. Where production assumptions remain untested, narrow the release to advisory, read-only, manual, or bounded-batch operation. If no owner can explain recovery from a partial cross-system action, do not grant that action.

Scale pressure is diagnostic. Repeated source overload points to indexing, repeated merge correction points to ownership, repeated handoff ambiguity points to weak interfaces, and repeated prompt-based coordination points to missing deterministic infrastructure. Evolve only from recurring evidence or a known production requirement; do not build a distributed control plane for hypothetical scale.

## Future Refresh Search Queries

The phrases below are retained discovery templates, not current evidence. This evolution pass does not browse, so no present external behavior, version, or search result is asserted from them. A later refresh begins with the local claim that may have drifted, the installed host or tool version, and the decision that new evidence could change.

| search_query_label_name | search_query_text_value | intended_question | acceptance_boundary |
| --- | --- | --- | --- |
| `official_docs_query_phrase` | agent creation prompt patterns official documentation best practices | what supported public contract governs project instructions, agent configuration, routing, tools, or context for the named product and version? | prefer official primary documentation; inspect the relevant passage and do not extrapolate across product surfaces |
| `github_repository_query_phrase` | agent creation prompt patterns GitHub repository examples | does a public implementation, schema, or maintained example clarify behavior left ambiguous by supported documentation? | label implementation evidence, distinguish released contract from incidental or unreleased behavior, and reproduce locally where consequential |
| `release_notes_query_phrase` | agent creation prompt patterns changelog release notes migration | did a release deprecate, add, or change syntax, precedence, tools, invocation, or lifecycle behavior that affects a prompt clause? | record product and version range, migration guidance, affected local clause, and regression scenario |

Refine a template with the exact product, feature, installed or target version, and decision term. Search for disconfirming language such as `deprecated`, `breaking change`, `limitation`, `not supported`, or `migration`, not only `best practices`. Begin precise; broaden terminology deliberately if concepts were renamed. Search ranking is a discovery aid, not an authority signal.

Refresh on material events:

- a mapped local or public contract changes;
- the installed host or validator version changes;
- observed behavior contradicts a prompt clause;
- a severe route, authority, or recovery incident exposes an assumption;
- a portability or compatibility decision cannot be resolved locally;
- a scheduled owner review covers a high-risk dependency with no stronger event signal.

Use the most direct evidence source for the question. Local repository search, schema or validator diffs, installed-runtime help, release feeds, commit history, issue trackers, and controlled experiments may answer a versioned operational question better than broad web search. Official documentation is normative when it states a supported contract. Repositories and issues can diagnose behavior but may expose incidental, unreleased, or unresolved states. Secondary material is useful for terminology and counterexamples; verify high-consequence claims through primary evidence or controlled target-host behavior.

For every material refresh, record query or local lookup, date, product and version, selected source, concise supporting passage or implementation location, rejected candidates and why, affected evidence label, prompt clause, owner, and linked fixture. If archive/live local sources are involved, verify their integrity separately so external refresh does not erase provenance. Keep concise decision records rather than raw result dumps.

**Good refresh:** search the official host documentation for a named tool-permission change in the installed version, update only the affected authority clause, and rerun denied-capability fixtures. **Bad refresh:** search “best agent prompts,” copy a secondary example, and present it as current local policy. **Borderline refresh:** a repository example shows undocumented behavior; retain it as bounded implementation evidence, reproduce it safely, and avoid broader authority until supported behavior is established.

Stop when additional results no longer change trigger, context, authority, process, output, recovery, or release status. Record a scoped “no material change” result so later maintainers do not repeat the same discovery without cause. If no relevant authoritative support exists, narrow or remove the claim rather than continuing until a convenient confirmation appears.

## Evidence Boundary Notes

- `local_corpus_sourced_fact`: a statement tied directly to an inspected local source path and relevant span above. The label establishes local provenance, not currentness, independence, universal authority, or behavioral effectiveness. Archive/live copies in one lineage do not become independent support by being counted twice.
- `external_research_sourced_fact`: a statement tied directly to an inspected public source, with product, version or date context, and bounded claim scope. The public URLs retained in this no-browse pass are source identities and future refresh pointers; they do not establish new present-tense external facts here.
- `combined_evidence_inference_note`: synthesis that combines inspected evidence with coding and systems judgment to produce agent guidance. It must state assumptions, boundaries, alternatives, uncertainty, and a verification or review method proportionate to consequence.

These labels identify support type, not truth value. A local fact can be stale. An external fact can describe another product surface. An inference can become operationally well tested without becoming an externally sourced fact. Report source confidence and target-host behavioral confidence separately.

Use atomic claim records for consequential routing, authority, state mutation, performance, security, reliability, and lifecycle decisions:

| claim_record_field | completion_rule |
| --- | --- |
| claim | state one decision-bearing proposition rather than combining fact and inference in one sentence |
| evidence_type | select local fact, external fact, or combined inference for the narrow claim scope |
| source_and_state | record path or URL, relevant span or location, archive/live lineage, inspected date or version, and freshness status |
| support_and_limit | explain what the source establishes and what it does not establish |
| prompt_consequence | identify the trigger, context, tool, process, output, recovery, or lifecycle clause affected |
| uncertainty_action | name the owner, next observation, and authority or release limit while uncertainty remains |
| disconfirming_gate | name the scenario, command, reviewer criterion, or runtime observation that would narrow or reject the claim |
| propagation | link affected charter fields, prompt artifact, fixtures, owner, and retirement or migration path |

Split mixed statements when clauses have different evidence. For example:

- **Good boundary:** `local_corpus_sourced_fact` says the inspected local triggering guide uses contextual examples and commentary. `combined_evidence_inference_note` adds a negative neighboring-agent case because this agent's portfolio has overlap risk. A nonactivation fixture verifies the local design decision.
- **Bad boundary:** “External and local best practices prove this agent should use all available tools.” The sources, scope, authority inference, and disconfirming evidence are absent.
- **Borderline boundary:** a public repository implementation accepts a field not documented for the installed release. Record it as versioned implementation evidence, test it reversibly in the target host, and do not generalize it into a supported portability claim.

Labels fail when they are decorative. If removing or changing the source would not alter the claim, confidence, prompt clause, or gate, the reference may be ornamental. If one label covers a sentence containing both observed format and inferred behavior, split the sentence. If uncertainty does not name an owner, next observation, or capability consequence, it is a passive disclaimer rather than a control.

Audit evidence in both directions. Sample high-consequence guidance and trace it to relevant, fresh-enough support plus a disconfirming gate. Then start from every granted capability and route backward to an approved charter need and evidence record. Verify archive/live identity claims structurally, inspect semantic support directly, and exercise target-host behavior where consequences require it. A parser pass cannot establish claim relevance, and one successful run cannot establish universal reliability.

When sources conflict, preserve both, classify the disputed dimension, select an owner and decision criterion, and adopt, adapt, avoid, or remain blocked. Reduce authority or keep manual invocation while consequential uncertainty persists. Do not search indefinitely for confirmation or silently choose the more permissive source.

Treat `source -> claim -> charter decision -> prompt clause -> gate -> owner` as the maintenance graph for long-lived or high-authority agents. A material source change triggers review of linked claims and checks. A failed gate narrows the clause and release level. An ownerless evidence chain is a retirement signal. This traceability also makes deletion safe: maintainers can remove stale sources or agents while identifying which tests, routes, and responsibilities must migrate.
