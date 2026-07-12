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

**Decision supported.** This section helps decide whether to adopt, adapt, or avoid delegated subagent execution for a specific task and what evidence retires the cost of choosing wrongly. The seed table keys Adopt, Adapt, and Avoid to generic local-versus-external evidence agreement instead of task independence, file ownership, review capacity, and user permission.

**Recommended default and causal basis.** Adopt delegation when the plan is written and tasks are provably independent, adapt it when coupling or missing permissions require serialization or manual slices, and avoid it when design uncertainty or authority gaps dominate. Adoption criteria tied to observable task properties can be checked before dispatch, while agreement between two document sets says nothing about whether this task can be safely delegated.

**Operating conditions and assumptions.** Each tradeoff row names its triggering condition, the cost it accepts, the recovery it implies, and one verification question a reviewer can answer from artifacts. The tradeoff guide ranks same-workspace delegation choices and cannot authorize commits, new agents, or scope the user has not granted.

**Failure boundary and alternatives.** Adopt is chosen because sources agree, adapt hides an unresolved coupling, avoid becomes a reflex that blocks safe parallel research, or the cost row never names what to undo. Bounded alternatives and recoveries: run a single pilot task before committing to a route, downgrade to research-only delegation, split the decision per subtask instead of per project, or ask the user when the cost of being wrong is irreversible.

**Counterexample, gotchas, and operational comparison.** Agreement can be stale on both sides, a cheap-looking adaptation can double review load, avoidance can silently convert to unplanned manual scope, and cost estimates ignore integration debt. Good: adopt delegation for two adapters only after freezing their interface and naming rollback. Bad: adopt because the local skill and a public page both praise subagents. Borderline: adapt by serializing one coupled task while keeping the rest parallel, documenting why.

**Verification, evidence, and uncertainty.** Answer each row's verification question from actual artifacts, trace one adopt and one avoid decision to its observed outcome, and confirm the cost row identifies concrete undo and inspection steps. The seed's four-row adopt-adapt-avoid-cost skeleton and its verification-question column are directly reusable decision scaffolding. The true cost of a wrong route depends on unmeasured coupling and review capacity, so the guide's cost wording remains judgment rather than measurement.

**Second-order consequence.** A tradeoff guide earns its place only when a wrong route leaves a visible trail a reviewer can reverse; routes without undo instructions are gambles, not decisions.

**Revision decision.** Rekey each tradeoff row from generic evidence agreement to task independence, ownership clarity, permission state, and review budget.

**Retained seed evidence.** The Adopt when, Adapt when, Avoid when, and Cost of being wrong rows with their verification prompts remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| decision_option_name | when_to_choose_condition | tradeoff_cost_description | verification_question_prompt |
| --- | --- | --- | --- |
| Adopt when | local corpus and external evidence agree on the subagent development execution patterns pattern | fastest path, but can copy stale local assumptions | Does the selected pattern appear in the canonical source and current external evidence? |
| Adapt when | local sources are strong but public ecosystem guidance has changed | preserves repo fit, but requires explicit inference notes | Did the reference label the local fact, external fact, and combined inference separately? |
| Avoid when | source evidence is thin, conflicting, or unrelated to the user journey | prevents false confidence, but may require deeper research | Is there a confidence warning or adjacent reference route? |
| Cost of being wrong | wrong subagent development execution patterns guidance can send an agent to the wrong files, tests, or abstraction | wasted implementation loop and weaker verification | Would a reviewer know what to undo and what to inspect next? |

## Local Corpus Hierarchy

**Decision supported.** This section helps decide which local artifact class to trust first when the workflow skill, role templates, and their archived duplicates disagree or overlap. The seed hierarchy labels the archived skill canonical and its byte-identical live copy merely supporting, labels role templates legacy while they remain the active prompts, and repeats one generic reviewer question for all eight rows.

**Recommended default and causal basis.** Treat the live workflow skill plus its three role templates as one canonical protocol set, treat archive copies as provenance snapshots, and assign each row a role-specific reviewer question. Byte-identical duplicates cannot carry different authority, and a hierarchy that contradicts observed file equality trains readers to ignore its labels.

**Operating conditions and assumptions.** Each hierarchy row states duplicate group, role in the protocol, activation order, the companion file it requires, and the reviewer question that its class must answer. The hierarchy classifies retrieval priority inside this corpus and does not grade external documentation or grant any template orchestration authority.

**Failure boundary and alternatives.** Canonical status is read as permission to skip the other templates, legacy labels justify deleting active prompts, duplicate pairs drift after one side is edited, or the repeated question lets every row pass review identically. Bounded alternatives and recoveries: collapse duplicates into one row with two locations, rank by protocol stage instead of source tree, add hash checks to detect drift, or fall back to reading all four unique artifacts when classification is disputed.

**Counterexample, gotchas, and operational comparison.** Archive and live trees can diverge silently after the hierarchy is written, role labels imply an execution order the table never states, and a single canonical pick hides that the protocol needs all four artifacts together. Good: route workflow questions to the skill and dispatch text to the implementer template while recording their duplicate locations. Bad: cite the archived and live skill as two independent canonical votes. Borderline: keep legacy labels for archive copies only after adding a drift check.

**Verification, evidence, and uncertainty.** Recompute duplicate-pair hashes, confirm every unique artifact appears in exactly one duplicate group, and check that each row's reviewer question can only be answered by reading that artifact class. All eight seed paths, their heading signals, and the canonical-supporting-legacy vocabulary were checked against the byte-identical duplicate finding recorded in the evidence map. Whether future edits will land in the archive or live tree first is unknown, so which copy stays authoritative over time remains a maintenance judgment.

**Second-order consequence.** Hierarchy is only meaningful relative to a change process; without a rule for where edits land first, canonical labels decay into historical accidents.

**Revision decision.** Regroup rows by duplicate pair and protocol role, align class labels with observed byte equality, and replace the repeated reviewer question with role-specific questions.

**Retained seed evidence.** All eight path rows, the classification vocabulary line, and the heading-signal column remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

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

**Decision supported.** This section helps decide what concrete worked artifact must exist before this reference counts as operational for a real delegation task. The seed artifact table names goal, boundary, and gate fields but never instantiates them, so nothing proves the reference can drive one actual delegated task end to end.

**Recommended default and causal basis.** Complete the artifact for one real task by writing the user goal, the delegation boundary decision, the failure mode expected, and the gate that proved the outcome, then keep it beside the reference. An instantiated example forces every abstract rule to survive contact with a specific task, which is the cheapest way to expose missing fields before another agent relies on the template.

**Operating conditions and assumptions.** The artifact records task identity, dependency graph excerpt, chosen dispatch route, review evidence, integration result, and the residual risk accepted at completion. The artifact documents one delegation episode for review and cannot serve as blanket approval for repeating the same route on different tasks.

**Failure boundary and alternatives.** Fields are filled with restated definitions instead of task facts, the artifact is written after the fact to justify a decision already made, or one stale example is reused as proof for every future run. Bounded alternatives and recoveries: link to a real progress journal entry instead of a synthetic example, require one artifact per lane rather than per file, or accept a reviewed dry-run walkthrough when no live task is available.

**Counterexample, gotchas, and operational comparison.** A polished artifact can hide that the task was never delegated, goal statements drift from what the user actually asked, and completion rules quietly weaken when the gate command changes. Good: an artifact citing a real two-adapter delegation with its red-green evidence and integration diff. Bad: a table whose user goal is apply subagent patterns. Borderline: a simulated task walkthrough labeled as unexecuted but structurally complete.

**Verification, evidence, and uncertainty.** Check each artifact field against the actual task record, rerun or inspect the named verification gate, and confirm the decision boundary matches what the dependency graph showed at dispatch time. The seed's three completion rules and their evidence-source hints map cleanly onto the goal, boundary, and gate stages of the local workflow. How often the artifact must be refreshed as tooling changes is unmeasured, so its shelf life is a maintenance judgment rather than a rule.

**Second-order consequence.** Templates rot silently; only artifacts that were actually exercised by a task can certify that a reference still works.

**Revision decision.** Extend the three-field skeleton into a full episode record with task identity, dispatch route, review evidence, integration result, and residual risk.

**Retained seed evidence.** The worked-example definition line and the three artifact field rows with completion rules and evidence hints remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Theme specific artifact: worked subagent development execution patterns example with user goal, decision point, failure mode, and verification gate.

| artifact_field_name | artifact_completion_rule | evidence_source_hint |
| --- | --- | --- |
| user_goal_statement | state the user's concrete goal before applying Subagent Development Execution Patterns | local corpus hierarchy plus critique findings |
| decision_boundary_rule | define the point where this reference should be used or avoided | decision tradeoff guide |
| verification_gate_rule | define the command, checklist, or review question that proves the artifact worked | verification gate command set |

## Worked Example Set

**Decision supported.** This section helps decide which usage of this reference counts as exemplary, negligent, or conditionally acceptable when coaching an agent through delegation. The seed example set restates the corpus-loading ritual as good, ignoring paths as bad, and thin evidence as borderline without showing any delegation decision, worker artifact, or review consequence.

**Recommended default and causal basis.** Anchor each example in one observable delegation event: what was dispatched, what evidence came back, which review caught what, and how integration ended. Examples teach by consequence, and a reader can only transfer a lesson when the example shows the action, the signal that judged it, and the cost or benefit that followed.

**Operating conditions and assumptions.** Each example names the task shape, the dispatch or refusal decision, the review evidence observed, and the outcome that makes the verdict checkable. The examples illustrate delegation judgment inside this workspace protocol and do not certify tool behavior or generalize to platforms with different isolation guarantees.

**Failure boundary and alternatives.** Good examples celebrate ritual compliance rather than outcomes, bad examples are strawmen no agent would attempt, or the borderline case gives no rule for when its exception is allowed. Bounded alternatives and recoveries: replace synthetic verdicts with excerpts from real progress journals, add a second borderline case covering permission ambiguity, or express examples as before-and-after task contracts.

**Counterexample, gotchas, and operational comparison.** An example can pass structurally while the underlying decision was wrong, verdicts can encode taste rather than consequence, and copied examples lose the context that made them borderline. Good: dispatching one adapter after freezing its interface and confirming red tests. Bad: dispatching three workers into one module and merging by hope. Borderline: combining spec and quality review for a one-line fix while logging both verdicts separately.

**Verification, evidence, and uncertainty.** Trace each example to a reproducible scenario, confirm the good case's gate actually fires on the bad case, and test that the borderline rule tells a reader when the exception expires. The seed's three-verdict structure survives directly and its bad case already names the real failure of ignoring mapped local paths. Which borderline conditions occur most often in practice is unknown here, so the chosen third case reflects judgment about likely ambiguity rather than frequency data.

**Second-order consequence.** A bad example is only useful if the reference's own gates would catch it; otherwise the example set is advertising, not instrumentation.

**Revision decision.** Rewrite each verdict around an observable delegation event with its dispatch decision, review signal, and outcome.

**Retained seed evidence.** The good, bad, and borderline example lines with their original verdict framing remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Good example: Use Subagent Development Execution Patterns after loading the canonical source, confirming the external evidence boundary, and writing a verification gate before implementation.
Bad example: Use Subagent Development Execution Patterns as a generic tutorial while ignoring the mapped local paths, source hierarchy, and cost of being wrong.
Borderline case: Use Subagent Development Execution Patterns only after adding a confidence warning when local evidence is thin or conflicts with current ecosystem guidance.

## Outcome Metrics and Feedback Loops

**Decision supported.** This section helps decide which observable signals should trigger revising this reference or the delegation workflow it encodes. The seed metrics section names one leading indicator, one failure signal, and a verifier-rerun cadence but never defines who measures them, on what runs, or what change each signal forces.

**Recommended default and causal basis.** Instrument every delegation run to count clarification round-trips, reopened findings, and integration surprises, and route each threshold breach to a named revision action on this file. Signals only create a feedback loop when a specific measurement on a specific run population is bound to a specific corrective action; unattached indicators are slogans.

**Operating conditions and assumptions.** Each metric states its unit, collection point in the journey, healthy range, breach action, and the owner who applies the correction. These metrics evaluate the reference and orchestration protocol, not worker model quality or repository health, which need their own instruments.

**Failure boundary and alternatives.** Indicators are averaged across unlike tasks, the failure signal fires only after integration damage, cadence becomes calendar ritual detached from change events, or breaches accumulate with no revision ever applied. Bounded alternatives and recoveries: sample post-task retrospectives instead of continuous counters, review metrics at each lane checkpoint rather than on a clock, or tie refresh to source-change events like tool releases.

**Counterexample, gotchas, and operational comparison.** Fewer clarifications can mean better prompts or workers guessing silently, metric gaming rises once thresholds are known, and rerunning the verifier checks structure while saying nothing about advice quality. Good: reopening the routing section after two runs where workers guessed instead of asking. Bad: declaring success because the verifier stayed green all month. Borderline: skipping a scheduled review after a week with no delegation runs, recording the skip.

**Verification, evidence, and uncertainty.** Inspect journals for recorded metric values, confirm each breach maps to a committed revision, and cross-check that the leading indicator moved after the correction shipped. The seed's clarification-count indicator and its missing-context-budget failure signal both match failure modes the local workflow already warns about. Healthy thresholds for clarification and reopen counts are unmeasured for this corpus, so initial ranges are provisional and must be recalibrated from real runs.

**Second-order consequence.** A reference without a feedback loop can only degrade, because every change in tools or tasks silently invalidates advice that nothing is measuring.

**Revision decision.** Bind each signal to a measurement unit, run population, breach threshold, revision action, and owner.

**Retained seed evidence.** The leading indicator, failure signal, and verifier-driven review cadence lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Leading indicator: the next run needs fewer clarifications and produces fewer unverifiable claims.
Failure signal: the reference tells agents what to do without defining context budget or escalation rules.
Review cadence: Re-run the verifier after every generated-reference edit and refresh external sources when public APIs, docs, or tooling releases change.

## Completeness Checklist

**Decision supported.** This section helps decide when this reference may be declared complete enough to hand to an agent and what evidence backs each checklist tick. The seed checklist verifies that sections exist and name things but never asks whether their guidance is correct, consistent across sections, or executable by an agent under real constraints.

**Recommended default and causal basis.** Keep the structural items and add cross-section consistency, executable-gate, authority-boundary, and evidence-label checks that each require citing the line that satisfies them. Existence checks catch missing prose while the expensive failures are contradictions between sections and gates that cannot actually run, which only content-level checks intercept.

**Operating conditions and assumptions.** Each checklist item names its satisfying evidence, the section it inspects, and whether a human or script can evaluate it. The checklist gates this document's readiness for agent use and does not certify the delegation outcomes of tasks that later use it.

**Failure boundary and alternatives.** Items are ticked from memory without citations, structural passes are read as content endorsement, or the checklist freezes while sections evolve and silently stops covering new obligations. Bounded alternatives and recoveries: generate structural items from the verifier instead of maintaining them by hand, replace some ticks with paired-reviewer sign-off, or sample two random sections per review for deep reading instead of shallow full passes.

**Counterexample, gotchas, and operational comparison.** Checklists reward completion theater, an item spanning several sections gets ticked when only one satisfies it, and reviewers stop reading carefully once early items pass. Good: ticking the routing item only after quoting the adjacent-reference lines it requires. Bad: ticking all seven items in one glance because headings exist. Borderline: ticking a consistency item from last week's read, noting the staleness.

**Verification, evidence, and uncertainty.** Demand a line citation per tick, rerun the structural verifier, and spot-check one claimed-consistent pair of sections for actual agreement on defaults and boundaries. The seed's seven items map one-to-one onto sections this file genuinely contains, so the structural layer is already sound scaffolding. How much deep review each item deserves per revision is a judgment that depends on how heavily the reference is edited, not a fixed rule.

**Second-order consequence.** A checklist that can be completed without reading the document measures the checklist, not the document.

**Revision decision.** Append consistency, executability, authority, and evidence-label items and require cited evidence for every tick.

**Retained seed evidence.** All seven structural checklist items covering scenario, decision guide, hierarchy, artifact, examples, metrics, and routing remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- The role scenario names the user, starting state, decision, and trigger for Subagent Development Execution Patterns.
- The decision guide includes Adopt when, Adapt when, Avoid when, and Cost of being wrong.
- The local corpus hierarchy identifies canonical and supporting sources or gives a confidence warning.
- The theme specific artifact is concrete enough to review without reading every mapped source.
- The examples cover good, bad, and borderline usage.
- The metrics section names one leading indicator and one failure signal.
- The adjacent routing section points to a better reference when this one is not the right fit.

## Adjacent Reference Routing

**Decision supported.** This section helps decide when to leave this reference and which neighboring reference should own the task instead. The seed routing splits the theme name into subagent, development, and execution keywords and points at unnamed adjacent references, giving an agent no real destination or handoff condition.

**Recommended default and causal basis.** Route by failure surface: dispatch-prompt design to the agent-creation and context-instruction references, review-loop depth to the code-review and debate references, and progress persistence to the TDD checkpoint and journal references. An agent needs routing exactly when this file stops answering, and only condition-plus-destination pairs convert that moment into a next action instead of a dead end.

**Operating conditions and assumptions.** Each route names its trigger condition, the concrete destination reference, what context to carry across, and what this file retains ownership of after the handoff. Routing redirects within this corpus's reference set and cannot substitute for the user's own prioritization or authorize work in the destination's domain.

**Failure boundary and alternatives.** Keyword overlap routes to a file that merely shares a word, two references both claim the task and neither owns integration, or the router sends context-free handoffs that force rediscovery. Bounded alternatives and recoveries: consult the corpus index for exact titles before routing, keep the task here with an explicit gap note when no destination fits, or escalate to the user when two references genuinely conflict over ownership.

**Counterexample, gotchas, and operational comparison.** Adjacent files evolve independently so routes silently dangle, circular routes can bounce an agent between two references, and a plausible route can hide that the corpus simply lacks the needed reference. Good: routing a prompt-template redesign to the agent-creation reference while keeping integration gates here. Bad: routing to the execution adjacent reference, which does not exist by that name. Borderline: routing a review-cadence question to the TDD checkpoint reference while duplicating one shared rule locally with a sync note.

**Verification, evidence, and uncertainty.** Resolve every named destination to an actual corpus file, walk one sample task through each trigger condition, and confirm no pair of routes forms a cycle without an owner. The corpus visibly contains agent-creation, context-instruction, code-review, debate, and TDD checkpoint references that cover this file's adjacent failure surfaces. The best destination for mixed tasks that span dispatch and review depends on task emphasis, so some routings remain judgment calls the agent must record.

**Second-order consequence.** Routing quality is a property of the corpus, not the file; every unresolved route is evidence of a missing or misnamed reference that the corpus owner should fix.

**Revision decision.** Replace keyword stubs with trigger-condition routes to named corpus files plus carried-context and retained-ownership notes.

**Retained seed evidence.** The adjacency guidance line and the three keyword-derived route stubs remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Adjacent reference guidance: Use debate, subagent, context, or verification references when the task narrows to a specific agent behavior.
Adjacent reference 1: consider the subagent adjacent reference when the current task pivots away from subagent development execution patterns.
Adjacent reference 2: consider the development adjacent reference when the current task pivots away from subagent development execution patterns.
Adjacent reference 3: consider the execution adjacent reference when the current task pivots away from subagent development execution patterns.

## Workload Model

**Decision supported.** This section helps decide how much delegation load one controller session can carry before quality collapses and where that load limit binds first. The seed workload table asserts a one-task, ten-file, three-subtask boundary and truncates its own heading-signal cell mid-word, without deriving any limit from controller attention, review cost, or task coupling.

**Recommended default and causal basis.** Size workload by review capacity, dispatching only as many concurrent workers as the controller can spec-review and integrate within the session, which in practice keeps active delegation at one to three bounded tasks. The binding constraint is controller verification bandwidth, because every dispatched worker returns artifacts that demand line-level review, finding closure, and integration testing that cannot be delegated away.

**Operating conditions and assumptions.** The model tracks active workers, files under exclusive ownership, open review findings, integration debt, and the context budget spent on task packets. The workload model bounds one controller session inside one workspace and says nothing about fleet-level scheduling or multi-session pipelines.

**Failure boundary and alternatives.** Worker count is raised because dispatch is cheap, file limits are read as quality guarantees, source-pressure rows are truncated into noise, or workload accounting ignores the re-review loops that dominate real cost. Bounded alternatives and recoveries: measure per-run review minutes and set caps empirically, use a work-in-progress limit on open findings instead of worker count, or split oversized efforts into sequential sessions with journal handoffs.

**Counterexample, gotchas, and operational comparison.** Three trivially independent subtasks cost less than one hidden-coupled pair, review debt compounds invisibly until integration, and static numeric caps invite gaming instead of judgment. Good: pausing new dispatch because two spec reviews are still open. Bad: running five workers because each touches different files. Borderline: temporarily exceeding the subtask cap for read-only research while implementation stays serialized.

**Verification, evidence, and uncertainty.** Count open findings and review turnaround per journal, compare integration failures against concurrent-worker counts, and test whether the stated caps predict where quality actually degraded. The seed's bounded-capacity instinct and its artifact-pressure requirement match the local workflow's insistence on per-task review and audit. The numeric caps are unmeasured heuristics, and the true limit varies with task coupling and reviewer diligence, so all stated numbers are provisional planning aids.

**Second-order consequence.** Delegation shifts cost from writing code to verifying it, so any workload model that counts tasks instead of verification effort will overestimate safe capacity.

**Revision decision.** Rederive each boundary from controller review bandwidth and open-finding limits, and repair the truncated heading-signal cell.

**Retained seed evidence.** The four workload dimensions with their boundary values and verification pressure points remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`combined_evidence_inference_note`: Treat Subagent Development Execution Patterns as a agent workflow operating reference, not as a prose summary.

| workload_dimension_name | workload_boundary_value | verification_pressure_point |
| --- | --- | --- |
| primary_usage_surface | agent planning, tool use, context loading, delegation, or skill/plugin execution where bad guidance compounds across long-running sessions | verify that the reference changes the next implementation or review action |
| bounded_capacity_model | one primary task, up to 10 source files, up to 3 delegated subtasks, and a written completion audit for every run | split the task or create a narrower reference when this boundary is exceeded |
| source_pressure_model | local heading signals include Subagent-Driven Development; When to Use; The Process; Prompt Templates; Example Workflow; Advantages; Code Quality Reviewer Prompt Template; Implemen | compare guidance against canonical local sources before following external examples |
| artifact_pressure_model | required artifact is worked subagent development execution patterns example with user goal, decision point, failure mode, and verification gate | require the artifact before claiming the reference is operationally usable |

## Reliability Target

**Decision supported.** This section helps decide what measurable reliability this reference must exhibit before its guidance is trusted to steer real delegation. The seed reliability table promises a 100 percent boundary rate and an 18-of-20 sampled accuracy without any sampling procedure, sample source, or measurement owner ever existing.

**Recommended default and causal basis.** Keep the four target dimensions but ground each in a feasible measurement: evidence labels checked by the verifier, routing accuracy sampled from journaled runs, unsupported claims caught at review, and recovery paths walked during audits. Targets create reliability only when someone can actually run the measurement; unmeasurable precision teaches readers to treat all numbers in the file as decoration.

**Operating conditions and assumptions.** Each target names its metric, measurement method, sample population, evaluation owner, and the corrective action a miss triggers. The targets judge this document's guidance quality, not the reliability of agent platforms, repositories, or tasks that use it.

**Failure boundary and alternatives.** Percentages are quoted as achievements rather than aspirations, samples are drawn only from successful runs, misses trigger no correction, or the zero-unsupported-claim rule quietly exempts the reliability table itself. Bounded alternatives and recoveries: start with binary pass-fail audits instead of ratio targets, pool samples across the reference family to reach measurable volume, or replace numeric accuracy with defect-review of every miss.

**Counterexample, gotchas, and operational comparison.** A 20-use sample may take months to accumulate for a niche reference, reviewers disagree on what counts as a routing miss, and perfect label preservation can coexist with substantively wrong advice. Good: auditing five journaled uses and reopening the guide after two routing misses. Bad: reporting 18-of-20 accuracy no one measured. Borderline: provisionally claiming label preservation from verifier output while flagging that semantic drift is unchecked.

**Verification, evidence, and uncertainty.** Run the verifier for label structure, pull journaled uses for routing outcomes, demand a source row or inference note for every claim, and walk each failure row's recovery path once. The four seed dimensions align with real failure classes this corpus has already hit: label loss, misrouting, unsupported claims, and dead-end failure guidance. No baseline measurement exists yet for any target, so current compliance is unknown and the first audit will define achievable thresholds.

**Second-order consequence.** An unmeasured target is a liability beyond uselessness, because it manufactures false confidence exactly where the document claims to be most rigorous.

**Revision decision.** Attach a sampling procedure, population, owner, and miss-triggered action to each target and mark all thresholds as unbaselined aspirations.

**Retained seed evidence.** All four reliability rows with their threshold values and evidence-collection methods remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| reliability_target_name | measurable_threshold_value | evidence_collection_method |
| --- | --- | --- |
| source_boundary_preservation | 100 percent of recommendations keep local, external, and inference boundaries visible | review generated text for the three evidence labels before reuse |
| decision_accuracy_sample | at least 18 of 20 sampled uses route to the correct adopt, adapt, avoid, or adjacent-reference decision | sample downstream tasks and record reviewer verdicts |
| unsupported_claim_rate | zero unsupported production, security, latency, or reliability claims in final guidance | reject claims without source row, explicit inference note, or verification method |
| recovery_path_clarity | every avoid or failure case names the rollback, escalation, or next-reference route | inspect failure-mode and adjacent-routing sections together |

## Failure Mode Table

**Decision supported.** This section helps decide which delegation-workflow failures deserve standing mitigations and how each is detected before it corrupts integrated work. The seed failure table lists source drift, generic advice, context loss, and tool fanout generically but omits the delegation-specific failures its own earlier sections rank highest, such as false task independence and report-trusted review.

**Recommended default and causal basis.** Keep the four generic rows and add the delegation-native failures: hidden task coupling, report-only acceptance, review-order inversion, open-finding carryover, and constraint loss between user and worker prompts. Failure tables pay off in the moment of triage, and triage needs the failures that actually occur in this workflow, ranked by blast radius rather than by genericity.

**Operating conditions and assumptions.** Each row names its trigger, earliest observable signal, blast radius, containment step, corrective action, and the journey stage where detection belongs. The table covers orchestration and reference-usage failures and cannot enumerate domain-specific code defects, which belong to the repository's own test regime.

**Failure boundary and alternatives.** Rows describe failures too abstractly to match live symptoms, mitigations restate the failure as an imperative, detection lands after integration where evidence is gone, or the table grows without pruning until triage is slower than guessing. Bounded alternatives and recoveries: order rows by observed frequency once journals accumulate, merge overlapping rows into failure families with shared containment, or link each row to the checklist item or gate that operationalizes it.

**Counterexample, gotchas, and operational comparison.** Two failure modes often co-occur and mask each other, mitigation cost varies wildly across rows, and a well-worded row can create false confidence that detection is actually wired into the workflow. Good: catching hidden coupling at dependency-map time and merging the two tasks. Bad: discovering shared schema edits during final integration. Borderline: proceeding with a suspected-independent pair under an explicit watch condition and a prepared revert.

**Verification, evidence, and uncertainty.** Inject one representative failure per row in a drill, confirm the named signal fires at the named stage, and check that containment leaves the workspace recoverable. The anti-pattern registry earlier in this file already names the delegation-native failures, so the table's gap is internal inconsistency rather than missing knowledge. Real frequency and cost rankings await accumulated journal data, so today's ordering encodes expected rather than observed risk.

**Second-order consequence.** When two sections of one reference disagree about which failures matter, agents inherit the disagreement as unpredictable behavior; internal consistency is itself a reliability control.

**Revision decision.** Merge the registry's delegation-native failures into the table and give every row an earliest-signal and journey-stage column.

**Retained seed evidence.** All four seed failure rows with their triggers and mitigation actions remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| failure_mode_name | likely_trigger_condition | required_mitigation_action |
| --- | --- | --- |
| source drift hides truth | external or local guidance changes after the reference was written | refresh public evidence, rerun local corpus gate, and mark stale claims before reuse |
| generic advice escapes review | agent copies plausible best practices without theme-specific verification | block completion until the verification gate names concrete command, reviewer question, or metric |
| context window loses plan | long-running session forgets early constraints or overwrites user intent | write checkpoint summaries and re-read plan before each destructive step |
| tool fanout outruns budget | parallel actions create conflicts, duplicate work, or unbounded external calls | cap fanout, assign ownership, and require merge/audit checkpoints |

## Retry Backpressure Guidance

**Decision supported.** This section helps decide when a failed delegation step should be retried, escalated, or halted, and how the workflow sheds load when gates go red. The seed retry bullets classify failure causes and cap retries sensibly but never define who classifies, where the classification is recorded, or how backpressure releases once gates recover.

**Recommended default and causal basis.** Classify each failure once in the journal, allow a single bounded retry only for transient or stale-evidence causes, halt dispatch while any gate is red, and resume only after the blocking evidence is recorded green. Retries without recorded classification become infinite loops with amnesia, and dispatch during red gates multiplies unverifiable work faster than the controller can review it.

**Operating conditions and assumptions.** The guidance assumes journaled failure records, gates that report red or green unambiguously, one owner per file, and a controller empowered to pause its own dispatch. This governs retry of orchestration steps like dispatch, review, and verification, not application-level retry logic inside the code being written.

**Failure boundary and alternatives.** A true contradiction is retried as if transient, backpressure stops work but nothing records why, the halt lifts because time passed rather than because evidence changed, or escalation has no named recipient. Bounded alternatives and recoveries: escalate immediately for authority or contradiction failures instead of consuming the retry, re-prompt with amended context rather than replaying, or hand persistent blockers to a fresh session through the journal.

**Counterexample, gotchas, and operational comparison.** Transient and systematic failures look identical on first occurrence, retrying a worker with the same prompt reproduces the same blind spot, and paused lanes silently expire context that resumption then rebuilds wrongly. Good: one retry after refreshing a stale source, then escalation with the diff attached. Bad: three silent replays of a failed spec review. Borderline: retrying a flaky-looking test once while logging that flakiness itself is an unverified hypothesis.

**Verification, evidence, and uncertainty.** Audit journals for classification-before-retry ordering, count retries per failure to confirm the bound held, and replay one halt to confirm resumption required green evidence rather than elapsed time. The seed's four-way failure classification and its checkpoint-before-destructive-step rule match the persistence cadence this workstream already enforces. The right retry budget for semantic failures like weak packets is judgment; one bounded retry is a defensible default, not a derived optimum.

**Second-order consequence.** Backpressure is a memory discipline as much as a flow control, because a halt that does not record its cause converts recoverable congestion into permanent context loss.

**Revision decision.** Add classification ownership, journal recording, and an evidence-based release condition to the existing retry and halt rules.

**Retained seed evidence.** All five retry and backpressure bullets, including the distributed one-owner-per-file rule, remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- Retry only after the failed verification signal is classified as transient, stale evidence, missing context, or true contradiction.
- Use one bounded retry for stale external evidence refresh, then escalate to a human or a narrower source-specific reference.
- Apply backpressure by stopping new generation or implementation work when source coverage, critique coverage, or verification gates are red.
- For long-running agent workflows, checkpoint after each batch and re-read the current spec before any broad rewrite, commit, push, or destructive operation.
- For distributed execution, assign one owner per generated file or theme batch and require merge-time verification of exact path, heading, and evidence-boundary invariants.

## Observability Checklist

**Decision supported.** This section helps decide what evidence each delegation run must emit so a later reader can reconstruct decisions without replaying the session. The seed observability bullets say record sources, commands, latencies, and counters but never state where records live, which journey stage writes them, or who consumes each signal.

**Recommended default and causal basis.** Write observations into the lane journal at fixed stages: sources and skips at load, task packets at dispatch, review findings at each gate, and a compact audit block with counters and unresolved risks at completion. Evidence captured at the stage that produced it stays accurate and cheap, while end-of-session reconstruction forgets skipped sources and silently flattens the decision path.

**Operating conditions and assumptions.** The checklist assumes a persistent journal, stable stage names shared with the journey scenario, and reviewers who actually read audit blocks before accepting work. Observability here serves workflow reconstruction and review, not runtime telemetry of shipped software, which belongs to the repository's own monitoring.

**Failure boundary and alternatives.** Records are written only after success, latency percentiles are quoted for workflows nobody timed, raw transcripts get dumped as audit evidence, or signals accumulate that no reviewer ever consumes. Bounded alternatives and recoveries: derive counters mechanically from journal structure instead of hand-logging, sample deep audits on a fraction of runs, or attach evidence to queue completion notes when a lane journal is unavailable.

**Counterexample, gotchas, and operational comparison.** Recording effort competes with task effort so under-pressure sessions log least when it matters most, and summaries can launder a bad decision into a tidy narrative. Good: a completion audit naming two skipped sources and one unresolved risk. Bad: p95 latency claims for a documentation workflow with no timer. Borderline: retroactively reconstructing one missing dispatch record and labeling it reconstructed.

**Verification, evidence, and uncertainty.** Pick one completed run and rebuild its decision sequence solely from records, then list what could not be recovered and fix the stage that failed to write it. This workstream's own lane journals demonstrate the load-dispatch-gate-completion recording rhythm the seed bullets gesture at. The minimum record set that keeps runs reconstructable without drowning reviewers is workload-dependent and must be tuned from actual audit attempts.

**Second-order consequence.** Observability that depends on discipline fails under pressure; whatever the workflow does not record automatically will be missing precisely on the runs worth investigating.

**Revision decision.** Bind each recorded signal to a journey stage, a storage location, and a named consumer, and drop untimed latency claims.

**Retained seed evidence.** All six observability bullets including the small-audit-evidence preference remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- Record which local sources were loaded and which were intentionally skipped.
- Record the exact verification command, reviewer question, or rendered artifact used as proof.
- Record p50/p95/p99 latency or reviewer-time measurements when the reference affects runtime or workflow speed.
- Capture tool-call count, context files loaded, delegated tasks, retry count, and completion-audit outcome.
- Record leading indicator and failure signal from this file in the coverage manifest or journal when the reference drives real work.
- Keep audit evidence small enough to review: command output summary, changed-file list, and unresolved-risk notes are preferred over raw transcript dumps.

## Performance Verification Method

**Decision supported.** This section helps decide how to prove this reference improves delegation outcomes enough to justify its reading and maintenance cost. The seed performance method demands latency percentiles and measurement packets while its own pass condition is reviewer comprehension, mixing runtime metrics into a document whose real performance is decision quality.

**Recommended default and causal basis.** Verify performance as decision quality by measuring whether a reader reaches the correct next action, gate, and stop condition faster and with fewer errors than without the reference, reserving latency packets for workflows that actually execute. A reference performs by changing decisions, so its verification must compare decisions made with and against it rather than timing operations it never performs.

**Operating conditions and assumptions.** The method assumes access to representative tasks, at least two comparable runs or reviewers, journaled outcomes to score against, and agreement on what the correct next action was. This method evaluates the document's operational usefulness and does not benchmark agent platforms, model quality, or repository build performance.

**Failure boundary and alternatives.** Percentile theater replaces judgment, pass is declared because a reviewer liked the prose, comparison runs differ in task difficulty so the delta is noise, or the measurement packet is demanded but never collected. Bounded alternatives and recoveries: run structured walkthroughs where a reviewer must locate five answers with citations, A-B test two versions of one section across lanes, or accept expert review as interim evidence while usage data accumulates.

**Counterexample, gotchas, and operational comparison.** Comprehension tests measure the reader as much as the document, familiarity effects make second runs faster regardless of the reference, and small samples make every delta look significant. Good: timing how quickly a reviewer finds the correct dispatch precondition and stop rule. Bad: reporting p99 latency for reading markdown. Borderline: counting tool calls saved in one paired run while flagging the sample of one.

**Verification, evidence, and uncertainty.** Define the answer key first, run the with-and-without comparison, score next-action correctness and time-to-answer, and record the delta with its sample-size caveat in the journal. The seed's own pass condition, that a reviewer identifies the correct next action without reading unrelated files, is already the right criterion and anchors the revised method. Effect sizes from single-reviewer comparisons are unstable, so early performance claims must carry explicit low-confidence labels until several runs accumulate.

**Second-order consequence.** Measuring a document with runtime metrics is a category error that crowds out the harder, more valuable measurement of whether it changes decisions.

**Revision decision.** Recenter measurement on decision-quality comparison and restrict latency packets to workflows with actual runtime.

**Retained seed evidence.** The budget requirement, both indicator lines, the measurement packet, and the pass and fail conditions remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Performance method: require tool-call budgets, timeout budgets, and a resumable journal when the workflow exceeds one focused session.
Leading indicator to measure: the next run needs fewer clarifications and produces fewer unverifiable claims.
Failure signal to watch: the reference tells agents what to do without defining context budget or escalation rules.
Required measurement packet: capture input size, source count, tool-call count, wall-clock time, p50/p95/p99 latency where runtime applies, and reviewer decision time where documentation applies.
Pass condition: the reference must let a reviewer identify the correct next action, verification gate, and stop condition without reading unrelated files.
Fail condition: the reference encourages implementation before the workload, reliability target, and failure-mode table are explicit.

## Scale Boundary Statement

**Decision supported.** This section helps decide at what task, team, or codebase scale this reference stops being sufficient and what must replace or supplement it beyond that line. The seed scale statement names multi-system spans, ownership boundaries, and SLO-bearing traffic as limits but gives no early indicators that a session is approaching them before quality fails.

**Recommended default and causal basis.** Treat rising clarification rates, cross-boundary file touches, growing unreviewed-artifact backlogs, and dependency maps that no longer fit one screen as approach signals, and split work or escalate before crossing the stated limits. Scale failures are gradual capacity failures that announce themselves through backlog and rework signals well before the hard boundary, so leading indicators buy the time that hard limits cannot.

**Operating conditions and assumptions.** The boundaries assume one controller, one workspace, journaled checkpoints, and tasks whose dependency structure can be mapped before dispatch. The statement bounds this orchestration reference and does not define scaling architecture for the software being built, which needs its own capacity design.

**Failure boundary and alternatives.** Limits are read as targets to approach, splits happen after context is already drifting, merge checkpoints are skipped because parallel writers seem disjoint, or an SLO-bearing change proceeds because no one owned the escalation. Bounded alternatives and recoveries: shard by theme file with one verification owner per shard, hand off through journals to fresh sessions at checkpoint boundaries, or downgrade ambition to research-only work when limits are near but unquantified.

**Counterexample, gotchas, and operational comparison.** Boundaries interact, since a modest codebase with many owners can exceed coordination capacity sooner than a huge single-owner one, and drift accumulates silently across long sessions that each seem fine locally. Good: splitting a two-system change into sequenced single-system sessions with an interface freeze between them. Bad: letting parallel agents rewrite one reference without a merge checkpoint. Borderline: continuing a long session past a drift warning with doubled checkpoint frequency.

**Verification, evidence, and uncertainty.** Track approach indicators per session in the journal, review incidents for which boundary was actually crossed, and test one planned split to confirm the handoff preserved constraints. The four seed boundary classes match the failure surfaces this file's workload and failure sections independently identify, giving the statement internal corroboration. Exact thresholds where sufficiency ends are unmeasured and task-dependent, so the boundaries mark judgment lines rather than calibrated limits.

**Second-order consequence.** Scale limits protect a workflow only when paired with early-warning signals; a boundary detected at the boundary has already been crossed.

**Revision decision.** Add leading approach indicators and pre-crossing actions for each stated boundary.

**Retained seed evidence.** All four scale boundary statements including the distributed split and context-drift rules remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Subagent Development Execution Patterns stops being sufficient when the task spans multiple independent systems, more than one ownership boundary, unbounded source discovery, or production traffic without an explicit SLO.
Under distributed execution, split work by theme file and preserve one verification owner per split; do not let parallel agents rewrite the same reference without a merge checkpoint.
Under long-running agent workflows, treat context drift as a reliability failure: checkpoint state, summarize open risks, and verify against the spec before continuing.
Under large-codebase scale, require dependency or source-graph narrowing before applying this reference; a source list without ranked canonical guidance is not enough.

## Future Refresh Search Queries

**Decision supported.** This section helps decide which future searches would actually refresh this reference's external evidence when a scheduled or event-driven update runs. The seed query table pastes the theme name into three generic templates whose literal phrasing would return noise, since subagent development execution patterns is this corpus's coinage rather than ecosystem vocabulary.

**Recommended default and causal basis.** Search the vocabulary the ecosystem uses: multi-agent orchestration and subagent features in Claude and Codex documentation, AGENTS.md adoption, agent isolation and worktree behavior, and prompt-template practices for implementer and reviewer roles. Refresh queries only pay off when their phrasing matches how sources describe the topic, and platform docs describe delegation through their own feature names rather than this file's internal label.

**Operating conditions and assumptions.** Queries assume an authorized browsing session, primary-source preference, retrieval-date recording, and the external map's promotion gate before any result becomes a fact. Queries feed the refresh workflow for this file's external claims and do not license opportunistic mid-task browsing outside an authorized refresh.

**Failure boundary and alternatives.** Literal theme-name queries return search noise, results are pasted without the evidence-boundary labels, refresh updates the map but not the sections that cited stale behavior, or queries fossilize while platforms rename features. Bounded alternatives and recoveries: subscribe to platform changelogs instead of re-searching, pin the Codex repository and diff releases, or ask the user for the current platform of record before spending a refresh budget.

**Counterexample, gotchas, and operational comparison.** Search engines personalize results so recorded queries do not reproduce, marketing pages outrank changelogs for feature claims, and a query that worked last quarter can silently start returning a renamed product. Good: querying claude code subagent isolation against official docs and recording the retrieval date. Bad: searching the literal phrase subagent development execution patterns changelog. Borderline: using a community comparison post as a candidate lead pending primary confirmation.

**Verification, evidence, and uncertainty.** Dry-run each query in an authorized session, score the first page for primary-source hits, and confirm every adopted result lands in the external map with date, version, and applicability fields. The external source map already names the OpenAI Codex docs, agents.md, and the Codex repository as the primary surfaces these queries should target. Which agent platforms will matter at the next refresh is unknowable now, so the query set itself must be reviewed as part of each refresh rather than trusted as stable.

**Second-order consequence.** Refresh queries encode a prediction about where truth will live later; reviewing the queries is therefore as important as running them.

**Revision decision.** Replace literal theme-name phrasing with ecosystem vocabulary targeted at the mapped primary sources.

**Retained seed evidence.** All three labeled query rows for official docs, repositories, and release notes remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| search_query_label_name | search_query_text_value |
| --- | --- |
| `official_docs_query_phrase` | subagent development execution patterns official documentation best practices |
| `github_repository_query_phrase` | subagent development execution patterns GitHub repository examples |
| `release_notes_query_phrase` | subagent development execution patterns changelog release notes migration |

## Evidence Boundary Notes

**Decision supported.** This section helps decide which evidence label every statement in this file must carry and how those labels constrain reuse of its guidance. The seed boundary notes define three labels but omit the retrieval-status nuance this file actually needs, where the external URLs are unbrowsed candidates rather than verified facts.

**Recommended default and causal basis.** Keep the three-label scheme and qualify it so local facts require a readable path, external labels carry retrieval status and date, and inference notes name which facts they combine so a reader can re-derive them. Labels earn trust by being checkable, and an external-fact label on an unread URL is exactly the unverifiable claim the labeling system exists to prevent.

**Operating conditions and assumptions.** The scheme assumes statements are label-attributable, that maintainers update labels when sources are read or refreshed, and that downstream reuse preserves labels verbatim. The labels classify evidence provenance in this reference and do not grade the correctness of the underlying sources themselves.

**Failure boundary and alternatives.** External labels imply verification that never happened, inference notes hide which premises they rest on, labels vanish when sections are quoted elsewhere, or a fourth ad hoc label appears and fragments the scheme. Bounded alternatives and recoveries: add an unverified-candidate qualifier instead of a fourth label, move retrieval metadata into the external map and reference it, or enforce label presence mechanically through the corpus verifier.

**Counterexample, gotchas, and operational comparison.** Label drift is invisible at read time since a stale fact looks identical to a fresh one, and inference chains can quietly cite other inferences until nothing bottoms out at a source. Good: an inference note naming the two local facts it synthesizes. Bad: labeling agents.md content an external fact while its retrieval status says unbrowsed. Borderline: keeping a fact label on a hash-verified local claim whose live file could have changed since checking.

**Verification, evidence, and uncertainty.** Sample statements per label and walk each back to its path, dated retrieval, or named premises, and reject any label whose chain breaks. This evolution itself demonstrates the scheme's value, since the byte-identical duplicate finding and the unbrowsed-URL status both came from enforcing label discipline. Whether three qualified labels remain sufficient as the corpus adds tool-generated evidence is an open design question deferred to corpus-level review.

**Second-order consequence.** An evidence label is a promise about how a claim can be audited; labels that cannot be audited invert into camouflage for the weakest claims.

**Revision decision.** Qualify each label with checkability requirements: paths for local facts, retrieval status for external facts, and named premises for inferences.

**Retained seed evidence.** All three evidence boundary label definitions remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- `local_corpus_sourced_fact`: statements tied directly to the local source paths above.
- `external_research_sourced_fact`: statements tied to the public URLs above.
- `combined_evidence_inference_note`: synthesis that combines local and public evidence into agent guidance.
