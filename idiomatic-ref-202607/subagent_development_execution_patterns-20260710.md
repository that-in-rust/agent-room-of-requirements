# Subagent Development Execution Patterns

**Decision supported.** This section helps decide when to delegate an implementation slice, what context and authority to give it, and how the controller proves the integrated result without surrendering ownership. The seed title does not define the controller, worker, spec-review, quality-review, integration, user-communication, or final-verification responsibilities that make delegation safe.

**Recommended default and causal basis.** Delegate only a bounded task with explicit inputs, outputs, dependencies, file ownership, permissions, tests, and stop conditions; inspect artifacts through spec review before quality review, then integrate and run final system gates under controller ownership. Fresh context reduces contamination, but a worker without complete constraints or an integration owner can produce locally plausible work that conflicts, overbuilds, or passes the wrong tests.

**Operating conditions and assumptions.** The controller inventories tasks and dependency edges, selects serial or parallel execution, supplies full requirement text and scene setting, answers questions, preserves user restrictions, records evidence, resolves reviews, integrates changes, and reports uncertainty. This reference governs same-workspace execution orchestration and does not authorize commits, branches, extra agents, network actions, or scope beyond the user's request.

**Failure boundary and alternatives.** The template overrides a no-commit instruction, workers share files, reports substitute for code inspection, quality review starts before scope is correct, unresolved findings are carried forward, or no one owns cross-task behavior. Bounded alternatives and recoveries: execute manually for tightly coupled work, use a separate-session plan workflow, dispatch independent research-only agents, perform one combined review for a tiny change, or ask the user when authority is missing.

**Counterexample, gotchas, and operational comparison.** Tasks that look independent can share generated files or schemas, a fresh agent lacks tacit context, commits may be prohibited, review agents can repeat the same blind spot, and context isolation can hide cross-task invariants. Good: split parser and UI changes only after defining their shared contract and separate files, review each against the plan, then run integration tests. Bad: dispatch three agents to edit one module. Borderline: parallelize read-only analysis while serializing implementation and reconciliation.

**Verification, evidence, and uncertainty.** Draw the dependency and ownership map, inspect every prompt and artifact, compare code to requirements line by line, rerun tests independently, review diffs for interference, execute cross-task gates, and confirm all user constraints. The local workflow and templates directly support fresh implementers, clarification, self-review, spec-first review, quality review, re-review, and final integration. The source's speed, natural-TDD, and universal serial-execution claims are not measured and must be adapted to the available agent runtime and workspace.

**Second-order consequence.** Delegation improves quality only when the controller retains epistemic and integration responsibility; offloading work is not offloading accountability.

**Revision decision.** Add explicit controller and worker contracts, dependency-aware dispatch, user-constraint precedence, integration ownership, evidence, and stop rules before preserving seed content.

**Retained seed evidence.** The exact title and focus on subagent-driven development execution remain unchanged. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

## Source Evidence Mapping Table

**Decision supported.** This section helps decide which unique artifact supports workflow selection, implementation dispatch, specification review, quality review, or external instruction context. The seed counts eight local paths as separate evidence even though each archive file is byte-identical to its live-path counterpart, and it assigns all three public links factual status without recording retrieval.

**Recommended default and causal basis.** Count four unique local contents: the orchestration skill, implementer template, spec reviewer template, and quality reviewer template; retain duplicate locations for provenance and treat public URLs as unrefreshed candidates. Duplicate detection prevents false corroboration, while role separation prevents a concise quality template from being mistaken for a complete orchestration contract.

**Operating conditions and assumptions.** Rows record path pair, SHA-256, artifact role, authority scope, required companion, direct claims, limitations, conflicts, retrieval status, and verification needed before adoption. The map establishes evidence provenance and cannot guarantee current tool semantics, agent availability, or task independence.

**Failure boundary and alternatives.** Eight paths become eight votes, the implementer report proves completion, the reviewer template defines user authority, or public agent guidance is called current without a complete read. Bounded alternatives and recoveries: use a claim ledger for conflicts, compare live and archive bytes during refresh, route platform-specific dispatch behavior to current docs, or rely on repository-local agent instructions.

**Counterexample, gotchas, and operational comparison.** Duplicate pairs can drift later, relative template paths assume directory layout, code-quality prompt delegates to another unavailable template, workflow instructions mention commits and worktrees, and external agent capabilities evolve. Good: cite the spec template for independent code inspection and the workflow for ordering, while adapting commit behavior to user constraints. Bad: cite both copies as corroboration. Borderline: use the quality template only after loading its referenced review rubric.

**Verification, evidence, and uncertainty.** Recompute all hashes, compare each pair, open complete unique artifacts, trace cross-file references, inspect local platform capabilities, preserve external no-browse status, and test the chosen dispatch and review flow. All four unique files were completely read and all four archive/live pairs were proven byte-identical at their recorded hashes. The public pages, referenced requesting-code-review template, and platform-specific Task behavior were not refreshed here.

**Second-order consequence.** The corpus is a composed protocol, not a pile of prompts: authority comes from role and ordering, not path count.

**Revision decision.** Add duplicate groups, hashes, role contracts, companion dependencies, platform status, limitations, and promotion gates while retaining all seed rows.

**Retained seed evidence.** All eight local paths and all three OpenAI Codex or AGENTS.md public paths remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| source_location_path_key | source_category_artifact_type | source_authority_confidence_level | source_usage_synthesis_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/claude-skills-202603/superpowers/subagent-driven-development/SKILL.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/claude-skills-202603/superpowers/subagent-driven-development/code-quality-reviewer-prompt.md | local_corpus_source_material | local_corpus_sourced_fact | local agent-usable source material |
| agents-used-monthly-archive/claude-skills-202603/superpowers/subagent-driven-development/implementer-prompt.md | local_corpus_source_material | local_corpus_sourced_fact | local agent-usable source material |
| agents-used-monthly-archive/claude-skills-202603/superpowers/subagent-driven-development/spec-reviewer-prompt.md | local_corpus_source_material | local_corpus_sourced_fact | local agent-usable source material |
| claude-skills/superpowers/subagent-driven-development/SKILL.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt |
| claude-skills/superpowers/subagent-driven-development/code-quality-reviewer-prompt.md | local_corpus_source_material | local_corpus_sourced_fact | local agent-usable source material |
| claude-skills/superpowers/subagent-driven-development/implementer-prompt.md | local_corpus_source_material | local_corpus_sourced_fact | local agent-usable source material |
| claude-skills/superpowers/subagent-driven-development/spec-reviewer-prompt.md | local_corpus_source_material | local_corpus_sourced_fact | local agent-usable source material |
| https://developers.openai.com/codex/guides/agents-md | external_research_source_material | external_research_sourced_fact | primary guidance for project instruction files and agent context loading |
| https://agents.md/ | external_research_source_material | external_research_sourced_fact | community format for predictable agent instructions |
| https://github.com/openai/codex | external_research_source_material | external_research_sourced_fact | GitHub implementation and project-level agent guidance |

## Pattern Scoreboard Ranking Table

**Decision supported.** This section helps decide which orchestration controls prevent the highest-cost delegation errors under limited context and review capacity. The seed gives unsupported scores to generic evidence controls but does not rank dependency mapping, complete task packets, clarification, spec-first review, quality sequencing, re-review, integration, or user-constraint preservation.

**Recommended default and causal basis.** Rank task dependency and ownership mapping first, then complete bounded task packets, clarification before assumptions, artifact-based spec review, quality review after compliance, mandatory re-review, cross-task integration, final fresh verification, and durable checkpoints. These controls intercept wrong-scope work and conflicting writes before polish or parallel speed can amplify them.

**Operating conditions and assumptions.** Each tier states failure prevented, prerequisites, controller cost, worker cost, concurrency effect, evidence, counterexample, bypass rule, and verification without unsupported probability. Rankings guide same-session orchestration and cannot replace domain-specific review or user authorization.

**Failure boundary and alternatives.** Invocation count becomes quality, fresh context is always better, two reviewers guarantee truth, parallelism is ranked by speed, or mandatory ceremony overwhelms a tiny reversible task. Bounded alternatives and recoveries: use qualitative tiers by risk, combine reviews for trivial changes, add specialist security or architecture review, parallelize disjoint read-only work, or execute coupled work centrally.

**Counterexample, gotchas, and operational comparison.** Reviewers can share prompt bias, tasks can have hidden dependencies, full text can still omit repo context, re-review can loop without decision authority, and integration defects appear only after locally green work. Good: prioritize explicit shared-schema ownership above dispatching two implementers. Bad: rank three-agent review as 95 percent reliable. Borderline: one controller review can cover a private typo after fresh tests, with the deviation documented.

**Verification, evidence, and uncertainty.** Define criteria, apply them to representative independent and coupled tasks, inspect missed defects and overhead, compare alternatives, ensure every tier has a stop condition, and recalibrate from actual incidents. The local workflow directly supports most ranked controls; dependency mapping and user-constraint precedence are necessary extensions exposed by its limits. No empirical study establishes defect reduction, speed gain, optimal reviewer count, or universal ordering cost.

**Second-order consequence.** The highest-leverage subagent pattern is preventing an invalid task boundary before any worker receives it.

**Revision decision.** Replace repeated scores with stable qualitative control tiers, causal criteria, overhead, bypass, and task-risk variants.

**Retained seed evidence.** Source Map First, Evidence Boundary Split, and Verification Gate Coupling remain preserved as evidence safeguards. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| pattern_identifier_stable_key | pattern_score_numeric_value | pattern_tier_adoption_level | pattern_failure_prevention_target |
| --- | ---: | --- | --- |
| `subagent_development_execution_patterns` | 95 | default_adoption_pattern_tier | Source Map First: Load local subagent development material before synthesizing execution patterns recommendations. |
| `subagent_development_execution_patterns` | 91 | default_adoption_pattern_tier | Evidence Boundary Split: Separate local facts, external facts, and inference before giving agent instructions. |
| `subagent_development_execution_patterns` | 88 | default_adoption_pattern_tier | Verification Gate Coupling: Attach each recommendation to at least one command, checklist, or review gate. |

## Idiomatic Thesis Synthesis Statement

**Decision supported.** This section helps decide what principle should govern task decomposition, dispatch, review loops, and final integration. The seed's local-first thesis does not explain why fresh workers help, when delegation is unsafe, or why specification review must precede quality review.

**Recommended default and causal basis.** Delegate independent obligation slices to fresh workers with complete context, preserve one controller-owned dependency and evidence model, verify scope before quality, and integrate only after findings are closed. Context isolation reduces contamination but also removes shared understanding, so explicit task contracts and controller reconciliation are the mechanism that converts isolation into reliability.

**Operating conditions and assumptions.** Tasks have stable inputs, outputs, owners, dependencies, constraints, tests, permissions, questions, review evidence, and integration gates. The thesis applies to delegated execution with inspectable artifacts and must yield to user scope, platform limits, and tightly coupled design work.

**Failure boundary and alternatives.** Freshness substitutes for context, independent means merely different files, reviewers trust reports, quality polish legitimizes extra scope, or controller abdicates final verification. Bounded alternatives and recoveries: manual execution for coupled changes, one worker for a coherent vertical slice, parallel research with serial edits, combined review for low risk, or separate-session plan execution.

**Counterexample, gotchas, and operational comparison.** Generated artifacts create hidden coupling, one task can change another's assumptions, reviewer prompts can bias findings, user messages can alter scope mid-run, and uncommitted shared state complicates diffs. Good: delegate two disjoint adapters after fixing their shared trait contract, then integrate. Bad: delegate schema and consumers concurrently. Borderline: parallelize tests and docs only with explicit ownership and one final behavior gate.

**Verification, evidence, and uncertainty.** Inspect the task graph, challenge independence, compare prompts with user constraints, review actual artifacts, close findings with re-review, and run end-to-end tests after integration. The local skill directly establishes fresh workers, full task text, questions, self-review, spec-first review, quality review, and final review. The optimal granularity and review depth depend on code coupling, tool capabilities, and failure cost.

**Second-order consequence.** Subagent reliability comes from explicit contracts at context boundaries, not from agent multiplicity.

**Revision decision.** Replace generic evidence ordering with a dependency-aware fresh-context, ordered-review, controller-integration thesis.

**Retained seed evidence.** Local retrieval, external checking, and verification-backed decisions remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`local_corpus_sourced_fact`: The local row for `subagent_development_execution_patterns` contains 8 source path(s), which should be treated as the first retrieval surface for this theme.
`external_research_sourced_fact`: The external source map provides public documentation, repository, or ecosystem analogues where available.
`combined_evidence_inference_note`: Reliable use of Subagent Development Execution Patterns comes from loading the local corpus first, checking public ecosystem guidance second, and converting both into verification-backed agent decisions.

## Local Corpus Source Map

**Decision supported.** This section helps decide which local artifact to retrieve for workflow choice, implementer dispatch, scope review, or quality review. The seed lists eight paths and headings but does not group duplicates, explain template dependencies, or distinguish orchestration authority from role-specific prompt content.

**Recommended default and causal basis.** Use the workflow skill for routing and sequence, the implementer template for task and self-review contracts, the spec template for line-by-line scope inspection, and the quality template only with its referenced review rubric after spec approval. Progressive role-based retrieval gives each decision the minimum complete context while preserving protocol order.

**Operating conditions and assumptions.** Each entry includes duplicate pair, hash, role, prerequisites, required inputs, output schema, forbidden assumptions, successor step, and failure recovery. The map routes local artifacts and does not grant roles permissions beyond the controller's task packet.

**Failure boundary and alternatives.** All templates are loaded blindly, a role prompt controls orchestration, quality review runs without base and head evidence, or a report replaces source inspection. Bounded alternatives and recoveries: adapt templates to current agent tools, inline a small review rubric, combine roles for trivial work, or use repository-native review workflows.

**Counterexample, gotchas, and operational comparison.** Relative files may be absent, Task and TodoWrite names are platform-specific, commits may be forbidden, reviewer context can omit working-tree changes, and archived/live pairs can later diverge. Good: load implementer text for dispatch and spec text for independent review. Bad: ask the implementer to certify itself. Borderline: one reviewer checks both scope and quality for a tiny patch while reporting the two verdicts separately.

**Verification, evidence, and uncertainty.** Recompute hashes, inspect role inputs and outputs, resolve referenced templates, adapt platform-specific calls, simulate one review loop, and ensure actual files and tests are inspected. All unique local artifacts and their cross-references were completely read. Availability and semantics of external Task, TodoWrite, worktree, and review tools vary by environment.

**Second-order consequence.** Prompt templates are interfaces; missing input fields and sequencing rules are contract defects.

**Revision decision.** Add duplicate groups, role interfaces, prerequisites, dependencies, platform adaptations, and recovery paths while preserving paths and headings.

**Retained seed evidence.** All local paths, titles, heading signals, and role labels remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| local_source_filepath_value | local_source_title_text | local_source_heading_signals | local_source_usage_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/claude-skills-202603/superpowers/subagent-driven-development/SKILL.md | subagent-driven-development | Subagent-Driven Development; When to Use; The Process; Prompt Templates; Example Workflow; Advantages | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/claude-skills-202603/superpowers/subagent-driven-development/code-quality-reviewer-prompt.md | Code Quality Reviewer Prompt Template | Code Quality Reviewer Prompt Template | local agent-usable source material |
| agents-used-monthly-archive/claude-skills-202603/superpowers/subagent-driven-development/implementer-prompt.md | Implementer Subagent Prompt Template | Implementer Subagent Prompt Template; Task Description; Context; Before You Begin; Your Job; Before Reporting Back: Self-Review | local agent-usable source material |
| agents-used-monthly-archive/claude-skills-202603/superpowers/subagent-driven-development/spec-reviewer-prompt.md | Spec Compliance Reviewer Prompt Template | Spec Compliance Reviewer Prompt Template; What Was Requested; What Implementer Claims They Built; CRITICAL: Do Not Trust the Report; Your Job | local agent-usable source material |
| claude-skills/superpowers/subagent-driven-development/SKILL.md | subagent-driven-development | Subagent-Driven Development; When to Use; The Process; Prompt Templates; Example Workflow; Advantages | skill entrypoint or reusable agent prompt |
| claude-skills/superpowers/subagent-driven-development/code-quality-reviewer-prompt.md | Code Quality Reviewer Prompt Template | Code Quality Reviewer Prompt Template | local agent-usable source material |
| claude-skills/superpowers/subagent-driven-development/implementer-prompt.md | Implementer Subagent Prompt Template | Implementer Subagent Prompt Template; Task Description; Context; Before You Begin; Your Job; Before Reporting Back: Self-Review | local agent-usable source material |
| claude-skills/superpowers/subagent-driven-development/spec-reviewer-prompt.md | Spec Compliance Reviewer Prompt Template | Spec Compliance Reviewer Prompt Template; What Was Requested; What Implementer Claims They Built; CRITICAL: Do Not Trust the Report; Your Job | local agent-usable source material |

## External Research Source Map

**Decision supported.** This section helps decide how future external evidence should update project instructions, tool semantics, delegation limits, or review workflow. The seed lists Codex AGENTS.md guidance, the AGENTS.md community format, and the Codex repository as facts without retrieval date or a boundary between instruction loading and subagent orchestration behavior.

**Recommended default and causal basis.** Use official platform documentation for current agent and tool behavior, repository code and releases for implementation details, and AGENTS.md format guidance only for instruction-file structure. Instruction precedence, thread or subagent availability, filesystem isolation, and review tools can change independently.

**Operating conditions and assumptions.** Rows include exact page or commit, retrieval date, feature version, claim supported, project applicability, conflict with local workflow, reproduction, and expiry. Public sources cannot override user instructions, repository policy, or observed workspace state.

**Failure boundary and alternatives.** Community format proves tool behavior, repository main is treated as released, old examples override user constraints, or public guidance is called current without browsing. Bounded alternatives and recoveries: inspect local tool metadata, use platform help, follow repository AGENTS.md, or retain a conservative manual workflow.

**Counterexample, gotchas, and operational comparison.** Codex and Claude terms differ, agent versus thread ownership differs, worktree isolation may be automatic, permissions vary, and external docs can omit local shared-workspace risks. Good: use official tool docs to confirm whether parallel workers share a filesystem. Bad: infer it from agents.md. Borderline: use Codex repository behavior as supporting evidence pinned to a commit.

**Verification, evidence, and uncertainty.** Open complete primary sources during an authorized refresh, pin versions, reproduce dispatch and isolation, compare local instructions, and update only affected rules. The three URLs are plausible sources for context and tool behavior but were not read in this evolution. Current content, feature availability, and terminology are unknown.

**Second-order consequence.** External freshness matters most at the action boundary where a mistaken isolation assumption can corrupt shared work.

**Revision decision.** Add version, feature, authority-domain, applicability, reproduction, conflict, and expiry fields with explicit no-browse status.

**Retained seed evidence.** All three exact public URLs and their intended context roles remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| external_source_url_value | external_source_name_text | external_source_usage_role | evidence_boundary_label_value |
| --- | --- | --- | --- |
| https://developers.openai.com/codex/guides/agents-md | OpenAI Codex AGENTS.md guide | primary guidance for project instruction files and agent context loading | external_research_sourced_fact |
| https://agents.md/ | AGENTS.md open format | community format for predictable agent instructions | external_research_sourced_fact |
| https://github.com/openai/codex | OpenAI Codex repository | GitHub implementation and project-level agent guidance | external_research_sourced_fact |

## Anti Pattern Registry Table

**Decision supported.** This section helps decide which orchestration smells should stop dispatch or integration and what bounded recovery addresses the cause. The seed lists generic evidence failures but omits false independence, incomplete task packets, overlapping writers, report trust, reviewer-order inversion, self-review substitution, open findings, and template-over-user precedence.

**Recommended default and causal basis.** Register hidden dependency, ambiguous ownership, context-starved prompt, assumption without clarification, parallel shared edit, report-only review, spec-quality inversion, reviewer monoculture, unfixed finding, unauthorized commit, and controller abdication. These failures amplify across workers and can make locally correct artifacts mutually incompatible.

**Operating conditions and assumptions.** Rows name trigger, dependency or authority violated, observable evidence, blast radius, containment, corrected task boundary, required re-review, integration test, and owner. The registry governs orchestration and cannot decide domain correctness without specialist evidence.

**Failure boundary and alternatives.** Warnings say communicate better, recovery dispatches more agents, the same reviewer validates itself, or controller edits blindly despite a worker retaining essential context. Bounded alternatives and recoveries: merge coupled tasks, serialize work, re-prompt with complete context, inspect manually, dispatch a specialist reviewer, revert a slice, or ask the user.

**Counterexample, gotchas, and operational comparison.** Different files can share schemas, a report can omit untracked files, quality feedback can expose a spec ambiguity, user changes can invalidate active tasks, and commits can hide unrelated workspace state. Good: stop two workers when both need the same manifest, assign one owner, then rebase the other task contract. Bad: resolve conflicts after parallel edits. Borderline: controller fixes a trivial integration typo only after understanding ownership and rerunning both reviews.

**Verification, evidence, and uncertainty.** Reconstruct the task graph and actual diffs, compare prompts with requirements, inspect tests and untracked state, reproduce the conflict, apply one recovery, and rerun spec, quality, and integration gates. The local workflow directly names most red flags and review ordering; user-precedence and dependency causality are necessary extensions. Agent isolation, commit behavior, and shared state differ by platform.

**Second-order consequence.** Most delegation failures begin as task-model failures before any code is written.

**Revision decision.** Expand three generic rows into a causal dispatch, ownership, review, authority, and integration registry.

**Retained seed evidence.** Source-first synthesis, evidence labels, and concrete verification remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| anti_pattern_failure_name | failure_cause_risk_reason | safer_default_replacement_pattern | detection_signal_review_method |
| --- | --- | --- | --- |
| context_free_summary_output | agent skips local corpus and produces generic advice | source_map_first_synthesis | verify every listed local path appears in the generated file |
| unsourced_recommendation_claims | guidance appears authoritative without source boundary | evidence_boundary_split_pattern | check for local, external, and inference labels |
| unverified_agent_instruction | recommendation cannot be checked by command or review gate | verification_gate_coupling | require concrete gate in generated reference |

## Verification Gate Command Set

**Decision supported.** This section helps decide which evidence must pass before a delegated task and the complete integrated change are marked done. The seed's archive-wide command does not validate task independence, prompt completeness, actual worker diffs, review order, finding closure, integration behavior, or user-constraint compliance.

**Recommended default and causal basis.** Run artifact structure gates, validate task packet and ownership, inspect worker files and tests, perform spec compliance before quality review, re-review every fix, compare cross-task diffs, and run fresh integration plus repository gates under controller control. Each worker and reviewer proves a bounded claim; only final integration evidence covers interactions and current workspace state.

**Operating conditions and assumptions.** Gates name task revision, base and head state, files, test selection, expected red, actual status, reviewer findings, closure evidence, skipped checks, user constraints, and final owner. These gates prove delegated delivery, not release or security readiness unless included explicitly.

**Failure boundary and alternatives.** Reports or commits prove behavior, one reviewer response closes issues, tests run before later edits are reused, archive validation replaces code gates, or no integration command exists. Bounded alternatives and recoveries: manual structured review, combined low-risk review, isolated reproduction, domain specialist gate, or blocked completion when a required check is unavailable.

**Counterexample, gotchas, and operational comparison.** Dirty worktrees blur base SHA, untracked files evade commit diffs, tests can be flaky, reviewers can inspect stale state, and platform tools may not expose separate subagents. Good: inspect the patch, see targeted tests fail then pass, obtain spec approval, resolve quality findings, and rerun the whole suite. Bad: accept '5/5 passing' from a report. Borderline: use no commit SHAs when commits are forbidden, substituting explicit before/after file hashes and diffs.

**Verification, evidence, and uncertainty.** Force representative failures, run fresh gates after the final edit, inspect outputs and skipped cases, confirm reviewer order and closure, and compare integrated behavior with the original plan. The source directly mandates self-review, spec review, quality review, re-review, and final review. Exact commands and evidence identifiers depend on repository and user permissions.

**Second-order consequence.** Review stages are meaningful only when they inspect the same identifiable artifact state.

**Revision decision.** Retain the archive verifier and add task, artifact, review-order, closure, diff, integration, and authority gates.

**Retained seed evidence.** The existing final-stage generator command remains preserved as an archive artifact gate. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`verification_gate_command_set`: Run the repository verifier after editing this file.

```bash
python3 agents-used-monthly-archive/idiomatic-references-202606/tools/verify_reference_generation.py --stage final
```

## Agent Usage Decision Guide

**Decision supported.** This section helps decide whether to use subagent-driven execution, a separate-session plan workflow, parallel analysis, manual implementation, or more planning. The seed routes by keywords and omits the source workflow's actual preconditions: a written plan, mostly independent tasks, and same-session execution.

**Recommended default and causal basis.** Confirm a concrete plan, classify dependency and file ownership, identify user permission and workspace isolation, choose same-session delegation only for bounded inspectable tasks, and define review plus integration before dispatch. Delegation selected too early converts design uncertainty into multiple inconsistent implementations.

**Operating conditions and assumptions.** The decision record includes objective, plan status, task graph, shared interfaces, owners, isolation, context packet, agent capability, review depth, integration gate, budget, and escalation. Do not create agents, branches, commits, or external actions beyond explicit authority.

**Failure boundary and alternatives.** Many tasks imply delegation, different filenames imply independence, same session implies shared understanding, or agent availability becomes permission. Bounded alternatives and recoveries: brainstorm and plan first, execute centrally, use parallel read-only analysis, create separate worktrees when authorized, or hand off a plan to another session.

**Counterexample, gotchas, and operational comparison.** User updates can change scope, one task may generate another's files, external state prevents deterministic parallelism, review cost can exceed implementation, and a single vertical slice may be clearer. Good: delegate three independent adapters after freezing their interface. Bad: dispatch before deciding the interface. Borderline: parallelize source research, then let one implementer reconcile the design.

**Verification, evidence, and uncertainty.** State the chosen path and rejected alternatives, challenge every dependency, inspect ownership and permissions, run a pilot task, and confirm integration evidence before scaling. The workflow's decision graph directly defines plan, independence, and same-session preconditions. Tooling and workspace isolation vary, and independence is a judgment requiring code evidence.

**Second-order consequence.** The routing decision is itself an architectural decision about information and change ownership.

**Revision decision.** Replace keyword triggering with plan, dependency, ownership, isolation, capability, review, budget, and escalation routing.

**Retained seed evidence.** Local-source-first use, gated patterns, freshness checks, evidence labels, and matching-theme triggers remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`agent_usage_decision_guide`: Use this reference when a task mentions this theme, one of the listed local source paths, or a nearby technology/workflow surface.

- Start with the local corpus source map.
- Prefer patterns with explicit verification gates.
- Treat external sources as freshness and ecosystem checks, not replacements for local repo conventions.
- Preserve the evidence boundary labels when reusing recommendations.

## User Journey Scenario

**Decision supported.** This section helps decide how a controller moves from an implementation plan to an integrated verified result across delegated tasks. The seed names an agent-system designer but stops before task decomposition, prompt assembly, questions, implementation, ordered reviews, integration, user updates, and recovery.

**Recommended default and causal basis.** Read and preserve the full plan, build a dependency and ownership graph, create bounded task packets, dispatch one ready worker, resolve questions, inspect self-review, run spec then quality review loops, integrate, checkpoint, and perform final system review. An end-to-end journey reveals handoff losses and cross-task gaps hidden by per-agent success reports.

**Operating conditions and assumptions.** The scenario includes user objective, plan revision, tasks, dependencies, file boundaries, prompts, permissions, red tests, artifacts, findings, fixes, re-reviews, integration, progress updates, final gates, rollback, and remaining risk. Adapt the journey to task size and never hide user decisions inside delegation.

**Failure boundary and alternatives.** Tasks are marked done from reports, the next worker starts with open findings, user changes are not propagated, or final review repeats local tests only. Bounded alternatives and recoveries: manual vertical slice, research-only delegation, one specialist review, paused clarification, or separate-session execution.

**Counterexample, gotchas, and operational comparison.** Fix loops alter downstream assumptions, context packets age, dirty worktrees contain user edits, reviewers may see stale files, and final integration can reveal the plan itself was wrong. A controller freezes an interface, delegates one adapter, answers a permission question, verifies red-green evidence, closes spec and quality findings, then runs consumer integration before dispatching the next adapter.

**Verification, evidence, and uncertainty.** Replay the journey from the same plan revision, inspect each artifact state, confirm finding closure, compare progress journal to files, and execute final cross-task behavior. The source skill and templates directly supply every core journey stage. No concrete plan, repository, or agent platform is supplied.

**Second-order consequence.** Progress is a sequence of verified state transitions, not a count of dispatched or completed agents.

**Revision decision.** Extend the role scenario into the complete plan-to-task-to-review-to-integration lifecycle.

**Retained seed evidence.** Agent-system designer, context selection, delegation, verification, starting uncertainty, and opening trigger remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Role based opening scenario: The agent-system designer is starting from a task that needs context selection, tool use, delegation, and verification and needs a reference that turns source evidence into an executable next step.
Primary user starting state: The user has a `subagent_development_execution_patterns` task, one or more local source paths, and uncertainty about which pattern should drive implementation.
Decision being made: choosing what context to load, what to offload, when to delegate, and how to prove completion.
Reference opening trigger: Open this file when the task mentions subagent development execution patterns, any mapped local source path, or an adjacent workflow with the same failure mode.

## Decision Tradeoff Guide

| decision_option_name | when_to_choose_condition | tradeoff_cost_description | verification_question_prompt |
| --- | --- | --- | --- |
| Adopt when | local corpus and external evidence agree on the subagent development execution patterns pattern | fastest path, but can copy stale local assumptions | Does the selected pattern appear in the canonical source and current external evidence? |
| Adapt when | local sources are strong but public ecosystem guidance has changed | preserves repo fit, but requires explicit inference notes | Did the reference label the local fact, external fact, and combined inference separately? |
| Avoid when | source evidence is thin, conflicting, or unrelated to the user journey | prevents false confidence, but may require deeper research | Is there a confidence warning or adjacent reference route? |
| Cost of being wrong | wrong subagent development execution patterns guidance can send an agent to the wrong files, tests, or abstraction | wasted implementation loop and weaker verification | Would a reviewer know what to undo and what to inspect next? |

## Local Corpus Hierarchy

Classification vocabulary includes canonical, supporting, legacy, duplicate, and conflicting source roles.

| local_source_filepath_value | corpus_hierarchy_role | heading_signal_to_convert | reviewer_question_to_answer |
| --- | --- | --- | --- |
| agents-used-monthly-archive/claude-skills-202603/superpowers/subagent-driven-development/SKILL.md | canonical primary source | Subagent-Driven Development; When to Use; The Process | What guidance, warning, or example should this source contribute to Subagent Development Execution Patterns? |
| agents-used-monthly-archive/claude-skills-202603/superpowers/subagent-driven-development/code-quality-reviewer-prompt.md | legacy historical source | Code Quality Reviewer Prompt Template | What guidance, warning, or example should this source contribute to Subagent Development Execution Patterns? |
| agents-used-monthly-archive/claude-skills-202603/superpowers/subagent-driven-development/implementer-prompt.md | legacy historical source | Implementer Subagent Prompt Template; Task Description; Context | What guidance, warning, or example should this source contribute to Subagent Development Execution Patterns? |
| agents-used-monthly-archive/claude-skills-202603/superpowers/subagent-driven-development/spec-reviewer-prompt.md | legacy historical source | Spec Compliance Reviewer Prompt Template; What Was Requested; What Implementer Claims They Built | What guidance, warning, or example should this source contribute to Subagent Development Execution Patterns? |
| claude-skills/superpowers/subagent-driven-development/SKILL.md | supporting context source | Subagent-Driven Development; When to Use; The Process | What guidance, warning, or example should this source contribute to Subagent Development Execution Patterns? |
| claude-skills/superpowers/subagent-driven-development/code-quality-reviewer-prompt.md | supporting context source | Code Quality Reviewer Prompt Template | What guidance, warning, or example should this source contribute to Subagent Development Execution Patterns? |
| claude-skills/superpowers/subagent-driven-development/implementer-prompt.md | supporting context source | Implementer Subagent Prompt Template; Task Description; Context | What guidance, warning, or example should this source contribute to Subagent Development Execution Patterns? |
| claude-skills/superpowers/subagent-driven-development/spec-reviewer-prompt.md | supporting context source | Spec Compliance Reviewer Prompt Template; What Was Requested; What Implementer Claims They Built | What guidance, warning, or example should this source contribute to Subagent Development Execution Patterns? |

## Theme Specific Artifact

Theme specific artifact: worked subagent development execution patterns example with user goal, decision point, failure mode, and verification gate.

| artifact_field_name | artifact_completion_rule | evidence_source_hint |
| --- | --- | --- |
| user_goal_statement | state the user's concrete goal before applying Subagent Development Execution Patterns | local corpus hierarchy plus critique findings |
| decision_boundary_rule | define the point where this reference should be used or avoided | decision tradeoff guide |
| verification_gate_rule | define the command, checklist, or review question that proves the artifact worked | verification gate command set |

## Worked Example Set

Good example: Use Subagent Development Execution Patterns after loading the canonical source, confirming the external evidence boundary, and writing a verification gate before implementation.
Bad example: Use Subagent Development Execution Patterns as a generic tutorial while ignoring the mapped local paths, source hierarchy, and cost of being wrong.
Borderline case: Use Subagent Development Execution Patterns only after adding a confidence warning when local evidence is thin or conflicts with current ecosystem guidance.

## Outcome Metrics and Feedback Loops

Leading indicator: the next run needs fewer clarifications and produces fewer unverifiable claims.
Failure signal: the reference tells agents what to do without defining context budget or escalation rules.
Review cadence: Re-run the verifier after every generated-reference edit and refresh external sources when public APIs, docs, or tooling releases change.

## Completeness Checklist

- The role scenario names the user, starting state, decision, and trigger for Subagent Development Execution Patterns.
- The decision guide includes Adopt when, Adapt when, Avoid when, and Cost of being wrong.
- The local corpus hierarchy identifies canonical and supporting sources or gives a confidence warning.
- The theme specific artifact is concrete enough to review without reading every mapped source.
- The examples cover good, bad, and borderline usage.
- The metrics section names one leading indicator and one failure signal.
- The adjacent routing section points to a better reference when this one is not the right fit.

## Adjacent Reference Routing

Adjacent reference guidance: Use debate, subagent, context, or verification references when the task narrows to a specific agent behavior.
Adjacent reference 1: consider the subagent adjacent reference when the current task pivots away from subagent development execution patterns.
Adjacent reference 2: consider the development adjacent reference when the current task pivots away from subagent development execution patterns.
Adjacent reference 3: consider the execution adjacent reference when the current task pivots away from subagent development execution patterns.

## Workload Model

`combined_evidence_inference_note`: Treat Subagent Development Execution Patterns as a agent workflow operating reference, not as a prose summary.

| workload_dimension_name | workload_boundary_value | verification_pressure_point |
| --- | --- | --- |
| primary_usage_surface | agent planning, tool use, context loading, delegation, or skill/plugin execution where bad guidance compounds across long-running sessions | verify that the reference changes the next implementation or review action |
| bounded_capacity_model | one primary task, up to 10 source files, up to 3 delegated subtasks, and a written completion audit for every run | split the task or create a narrower reference when this boundary is exceeded |
| source_pressure_model | local heading signals include Subagent-Driven Development; When to Use; The Process; Prompt Templates; Example Workflow; Advantages; Code Quality Reviewer Prompt Template; Implemen | compare guidance against canonical local sources before following external examples |
| artifact_pressure_model | required artifact is worked subagent development execution patterns example with user goal, decision point, failure mode, and verification gate | require the artifact before claiming the reference is operationally usable |

## Reliability Target

| reliability_target_name | measurable_threshold_value | evidence_collection_method |
| --- | --- | --- |
| source_boundary_preservation | 100 percent of recommendations keep local, external, and inference boundaries visible | review generated text for the three evidence labels before reuse |
| decision_accuracy_sample | at least 18 of 20 sampled uses route to the correct adopt, adapt, avoid, or adjacent-reference decision | sample downstream tasks and record reviewer verdicts |
| unsupported_claim_rate | zero unsupported production, security, latency, or reliability claims in final guidance | reject claims without source row, explicit inference note, or verification method |
| recovery_path_clarity | every avoid or failure case names the rollback, escalation, or next-reference route | inspect failure-mode and adjacent-routing sections together |

## Failure Mode Table

| failure_mode_name | likely_trigger_condition | required_mitigation_action |
| --- | --- | --- |
| source drift hides truth | external or local guidance changes after the reference was written | refresh public evidence, rerun local corpus gate, and mark stale claims before reuse |
| generic advice escapes review | agent copies plausible best practices without theme-specific verification | block completion until the verification gate names concrete command, reviewer question, or metric |
| context window loses plan | long-running session forgets early constraints or overwrites user intent | write checkpoint summaries and re-read plan before each destructive step |
| tool fanout outruns budget | parallel actions create conflicts, duplicate work, or unbounded external calls | cap fanout, assign ownership, and require merge/audit checkpoints |

## Retry Backpressure Guidance

- Retry only after the failed verification signal is classified as transient, stale evidence, missing context, or true contradiction.
- Use one bounded retry for stale external evidence refresh, then escalate to a human or a narrower source-specific reference.
- Apply backpressure by stopping new generation or implementation work when source coverage, critique coverage, or verification gates are red.
- For long-running agent workflows, checkpoint after each batch and re-read the current spec before any broad rewrite, commit, push, or destructive operation.
- For distributed execution, assign one owner per generated file or theme batch and require merge-time verification of exact path, heading, and evidence-boundary invariants.

## Observability Checklist

- Record which local sources were loaded and which were intentionally skipped.
- Record the exact verification command, reviewer question, or rendered artifact used as proof.
- Record p50/p95/p99 latency or reviewer-time measurements when the reference affects runtime or workflow speed.
- Capture tool-call count, context files loaded, delegated tasks, retry count, and completion-audit outcome.
- Record leading indicator and failure signal from this file in the coverage manifest or journal when the reference drives real work.
- Keep audit evidence small enough to review: command output summary, changed-file list, and unresolved-risk notes are preferred over raw transcript dumps.

## Performance Verification Method

Performance method: require tool-call budgets, timeout budgets, and a resumable journal when the workflow exceeds one focused session.
Leading indicator to measure: the next run needs fewer clarifications and produces fewer unverifiable claims.
Failure signal to watch: the reference tells agents what to do without defining context budget or escalation rules.
Required measurement packet: capture input size, source count, tool-call count, wall-clock time, p50/p95/p99 latency where runtime applies, and reviewer decision time where documentation applies.
Pass condition: the reference must let a reviewer identify the correct next action, verification gate, and stop condition without reading unrelated files.
Fail condition: the reference encourages implementation before the workload, reliability target, and failure-mode table are explicit.

## Scale Boundary Statement

Subagent Development Execution Patterns stops being sufficient when the task spans multiple independent systems, more than one ownership boundary, unbounded source discovery, or production traffic without an explicit SLO.
Under distributed execution, split work by theme file and preserve one verification owner per split; do not let parallel agents rewrite the same reference without a merge checkpoint.
Under long-running agent workflows, treat context drift as a reliability failure: checkpoint state, summarize open risks, and verify against the spec before continuing.
Under large-codebase scale, require dependency or source-graph narrowing before applying this reference; a source list without ranked canonical guidance is not enough.

## Future Refresh Search Queries

| search_query_label_name | search_query_text_value |
| --- | --- |
| `official_docs_query_phrase` | subagent development execution patterns official documentation best practices |
| `github_repository_query_phrase` | subagent development execution patterns GitHub repository examples |
| `release_notes_query_phrase` | subagent development execution patterns changelog release notes migration |

## Evidence Boundary Notes

- `local_corpus_sourced_fact`: statements tied directly to the local source paths above.
- `external_research_sourced_fact`: statements tied to the public URLs above.
- `combined_evidence_inference_note`: synthesis that combines local and public evidence into agent guidance.
