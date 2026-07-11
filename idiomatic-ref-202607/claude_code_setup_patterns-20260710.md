# Claude Code Setup Patterns

Claude Code setup is the design of a repository's agent control plane: which repeated work should be automated, which extension surface should own it, what authority that surface receives, and how the team will detect, reverse, and retire a bad choice. The decision is not "which features can we install?" It is "which small set of automations measurably improves this repository without bypassing its existing tools, permissions, and review path?"

**Recommended default.** Begin with read-only discovery and preserve the current workflow as the baseline. Then proceed in this order:

1. Inventory the language, frameworks, package managers, tests, formatters, CI, issue systems, service dependencies, existing `.claude/` files, and team-owned commands.
2. Name repeated friction or material risk in observable terms, such as formatting churn, missed security review, stale API knowledge, or manual browser verification.
3. Decide whether the existing command or documentation is already sufficient. Do not add automation merely because a matching extension exists.
4. Select one or two high-value setup items whose repository signals, owners, permissions, and expected outcomes are explicit.
5. Define invocation, allowed tools, external scopes, failure behavior, rollback, and retirement before enabling the item.
6. Validate syntax, then run a read-only or reversible positive case and a negative case that proves the automation stays out of unrelated work.
7. Observe whether the setup changes the intended workflow without adding duplicate effects, review noise, latency, or hidden maintenance.
8. Expand only when evidence identifies another recurring task or uncovered risk.

Use the extension surface that matches the behavior, not the product label that sounds most capable. A **hook** is appropriate for deterministic event enforcement, such as formatting an edited file or blocking a sensitive path, provided recursion and failure handling are bounded. A **skill** packages repeatable expertise, templates, scripts, and examples when the task benefits from a reusable workflow. A **subagent** isolates specialized analysis or parallel review when its inputs, ownership, tool access, and return artifact are independent. A **plugin** is useful when a maintained bundle of related capabilities reduces local duplication and the team accepts its lifecycle. An **MCP server** belongs at an external service boundary only when the service is actually needed, least-privilege access is available, data handling is acceptable, and local behavior can be verified. A manual command, documented convention, or no setup change remains a valid outcome.

**Fit and failure boundaries.** This method works best when repository signals are active, the target task recurs, a responsible owner can evaluate the result, and configuration can be tested without consequential external effects. File presence is only a lead: an abandoned test directory, obsolete formatter configuration, or unused SDK does not justify automation. Setup is the wrong repair when the real problem is an unresolved product requirement, missing service access, absent credentials, organization policy, production incident handling, or model capability. Prompt text and configuration cannot manufacture those prerequisites.

Stop or route the recommendation when permissions are unknown, a tool can mutate external state without an idempotency or rollback plan, public product availability has not been refreshed, two surfaces duplicate the same behavior, or nobody owns failures and updates. Low-impact defects such as a noisy matcher may be corrected locally; credential exposure, unauthorized mutation, blocking event loops, and untraceable external actions require containment before reuse.

**Operational contrast.** In a TypeScript repository with an active formatter and repeated review bottlenecks, a bounded post-edit formatting hook plus a read-only review subagent may be justified if both have narrow matchers and reproducible gates. Installing every cataloged plugin and MCP server because related dependencies appear in `package.json` is not evidence-led setup. A proposed database MCP integration is borderline when the service is relevant but the owner, credential scope, read-only probe, retention rule, or current compatibility is missing; keep it as a research item until those conditions are resolved.

**Verification contract.** Every recommendation should record the repository signal, user outcome, chosen surface, rejected alternatives, configuration location, owner, invocation rule, allowed tools or scopes, expected positive behavior, negative case, exact validation command or review gate, rollback, and retirement trigger. Syntax or installation success is necessary but insufficient. Verify that a hook ignores unrelated paths, a skill routes only on its declared tasks, a subagent cannot exceed its tool boundary, a plugin does not duplicate local automation, and an MCP server receives no authority beyond the stated service operation.

The local skill and five reference files directly establish this corpus's setup taxonomy and recommendation workflow. Their current and archived copies are byte-identical, so they are one content lineage rather than independent corroboration. The three public URLs are cataloged but were not refreshed in this no-browsing evolution; present availability, command syntax, and ecosystem status remain unresolved until checked against the relevant version.

The second-order rule is subtraction. Setup creates durable dependencies in future agent sessions, so each accepted item needs a version assumption, accountable owner, verification evidence, and removal condition. When the repository signal disappears, the owner changes, permissions widen, or measured value no longer exceeds maintenance and diagnosis cost, remove or replace the automation rather than retaining it as invisible policy.

## Source Evidence Mapping Table

This map routes claims; it is not a vote by path count. The twelve local rows represent six distinct files stored in current and archived locations. Each pair was verified byte-identical during this evolution, so a pair is one content lineage with two locators, not two independent confirmations. The public rows are preserved as future research leads and were not opened.

| source_location_path_key | lineage_and_access_state | prompt_setup_claim_scope | permitted_synthesis_use | limitation_and_recheck_rule |
| --- | --- | --- | --- | --- |
| agents-used-monthly-archive/claude-skills-202603/plugins/claude-code-setup/SKILL.md | Archived skill entrypoint; byte-identical to current counterpart; read locally | Read-only codebase analysis, output limits, setup taxonomy, recommendation phases, and decision framework | Establish what the archived recommender tells an agent to inspect and how it divides hooks, skills, subagents, plugins, and MCP servers | Source-authored guidance, not measured effectiveness or current product behavior; do not count separately from its current copy |
| agents-used-monthly-archive/claude-skills-202603/plugins/claude-code-setup/references/hooks-patterns.md | Archived hook catalog; byte-identical to current counterpart; read locally | Formatter, linter, type-check, test, protection, and notification hook examples plus placement guidance | Supply candidate repository signals and hook failure questions | Presence of a config file does not prove active use; exact events, matchers, and syntax require compatible-runtime verification |
| agents-used-monthly-archive/claude-skills-202603/plugins/claude-code-setup/references/mcp-servers.md | Archived MCP catalog; byte-identical to current counterpart; read locally | Categories for documentation, browser, database, version-control, cloud, monitoring, communication, file, container, and AI integrations | Identify possible external service boundaries after a real repository need is established | Catalog entries do not prove availability, safety, least-privilege scopes, or installed-version support; service access needs owner approval |
| agents-used-monthly-archive/claude-skills-202603/plugins/claude-code-setup/references/plugins-reference.md | Archived plugin catalog; byte-identical to current counterpart; read locally | Bundled development, review, Git, frontend, learning, security, and language-server capabilities | Explain when a maintained capability bundle might replace several local artifacts | Plugin names, marketplace status, install commands, and feature sets are unrefreshed source claims |
| agents-used-monthly-archive/claude-skills-202603/plugins/claude-code-setup/references/skills-reference.md | Archived skill guide; byte-identical to current counterpart; read locally | Skill structure, invocation controls, supporting files, templates, scripts, examples, arguments, and dynamic context | Support decisions about packaging a repeatable project workflow as a skill | Examples may be stale or unsafe for a different repository; frontmatter and invocation behavior require local schema validation |
| agents-used-monthly-archive/claude-skills-202603/plugins/claude-code-setup/references/subagent-templates.md | Archived subagent catalog; byte-identical to current counterpart; read locally | Review, security, test, documentation, performance, UI, dependency, and migration roles with suggested tools | Supply role boundaries and candidate tool scopes for isolated work | File-count thresholds and model choices are source-authored heuristics; parallelism and write access need task-specific proof |
| claude-skills/plugins/claude-code-setup/SKILL.md | Current skill entrypoint; same content lineage as archived counterpart; read locally | Current repository copy of the read-only recommender workflow and output contract | Use as the primary readable locator for this corpus's setup process | Current path does not imply present ecosystem freshness; verify implementation behavior before configuration changes |
| claude-skills/plugins/claude-code-setup/references/hooks-patterns.md | Current hook catalog; same content lineage as archived counterpart; read locally | Current repository copy of common event-driven automation patterns | Generate bounded hook hypotheses from active commands and policies | Never infer that a detected file authorizes auto-fix, blocking, or notifications; test match and failure behavior |
| claude-skills/plugins/claude-code-setup/references/mcp-servers.md | Current MCP catalog; same content lineage as archived counterpart; read locally | Current repository copy of candidate external integrations | Classify an already-identified service need and the questions its integration must answer | Do not recommend credentials, write access, or team sharing from dependency presence alone |
| claude-skills/plugins/claude-code-setup/references/plugins-reference.md | Current plugin catalog; same content lineage as archived counterpart; read locally | Current repository copy of capability-bundle examples | Compare a maintained bundle with custom local skills, hooks, or agents | Catalog status is unverified in this no-browsing pass; retain names as leads until refreshed |
| claude-skills/plugins/claude-code-setup/references/skills-reference.md | Current skill guide; same content lineage as archived counterpart; read locally | Current repository copy of skill packaging patterns and examples | Design a reviewable skill only after task recurrence and invocation authority are known | Bundled script examples can have side effects; validate tools, paths, argument handling, and failure behavior locally |
| claude-skills/plugins/claude-code-setup/references/subagent-templates.md | Current subagent catalog; same content lineage as archived counterpart; read locally | Current repository copy of specialized-agent examples | Compare isolated analysis with main-agent work and define an explicit return artifact | Suggested tools and models are not universal defaults; least privilege, ownership, and evaluator independence control adoption |
| https://github.com/davepoon/buildwithclaude | Cataloged public repository; not retrieved | Potential ecosystem collection of skills, agents, commands, hooks, and plugins | Future discovery and contrast after local needs are defined | Cannot support a current factual or compatibility claim until repository, revision, inspected path, and license are recorded |
| https://github.com/Cranot/claude-code-guide | Cataloged community guide; not retrieved | Potential community guidance on skills, hooks, plugins, and MCP | Future comparison of terminology and setup examples | Community advice cannot override local policy or official compatible-runtime behavior; current contents are unknown |
| https://www.claudedirectory.org/blog/claude-code-skills-vs-subagents-vs-mcp | Cataloged public article; not retrieved | Potential taxonomy comparison among extension surfaces | Future explanatory contrast if the taxonomy remains current and relevant | The seed's description of this page is not evidence of its present contents, authority, or version applicability |

**Default evidence workflow.**

1. Name the setup decision, such as whether an active formatter needs an event hook or whether repeated migration work needs a skill.
2. Select the skill entrypoint plus only the detail file whose claim scope matches that decision.
3. Collapse byte-identical archive/current pairs into one content lineage while retaining both locators for provenance.
4. Inspect the relevant passage and record whether it is a direct local fact, source-authored recommendation, negative example, or design inference.
5. Confirm the repository signal is active. A dependency, directory, or configuration file is a lead until its command, owner, or workflow is observed.
6. Keep public rows cataloged and unrefreshed unless browsing is permitted and a current-product claim materially affects the decision.
7. Attach local behavioral evidence to any recommendation; source agreement cannot prove fit, permissions, or value.

**Good use.** The active formatter command and its configuration are inspected, the hook catalog supplies a candidate post-edit pattern, and a dry run proves narrow matching and clean failure. **Bad use.** Twelve local paths are reported as twelve agreeing sources and used to justify installing several automations. **Borderline use.** A public taxonomy appears relevant but remains unread; preserve it as a refresh task and do not derive a current feature distinction from it.

**Verification and uncertainty.** Verify local path existence, paired content hashes, relevant passages, access state, and claim-to-recommendation links. A matching hash establishes shared identity, not correctness. Then trace each source change forward to affected setup items and their tests. The six local contents and their duplicate relationships are known. Current public content, command compatibility, marketplace availability, service behavior, and the effectiveness of any cataloged recommendation remain uncertain.

The second-order insight is that the map forms an evidence graph. Paths locate content, hashes identify lineages, claim edges bound authority, and verification edges decide whether source guidance survives local reality.

## Pattern Scoreboard Ranking Table

The seed's values are preserved for traceability, but no worksheet, sample, evaluator, scorer, or calibration record explains how `95`, `91`, and `88` were produced. They are inherited priority metadata. They are not success percentages, confidence probabilities, benchmark results, or evidence that the small gaps among rows are meaningful.

| pattern_identifier_stable_key | inherited_score | adoption_role | control_action | setup_failure_prevention_target | required_release_evidence |
| --- | ---: | --- | --- | --- | --- |
| `setup_signal_source_map_first` | 95 | required for consequential setup | Confirm active repository need and applicable source scope before recommending automation | Prevent catalog-driven setup, duplicated evidence, stale assumptions, and automation unrelated to an observed workflow | Each accepted item links to an active repository signal, relevant inspected source, owner, and explicitly rejected alternatives |
| `setup_evidence_authority_boundary_split` | 91 | required for consequential setup | Separate local fact, source-authored guidance, unrefreshed public lead, design inference, untrusted data, and action authority | Prevent dependency names or retrieved content from becoming permissions and prevent source prestige from authorizing external access | Every consequential claim and action records provenance, trust class, authority, uncertainty, and the owner able to resolve conflict |
| `setup_verification_gate_coupling` | 88 | required for consequential setup | Couple every recommendation to syntax checks, positive and negative behavior, permission review, rollback, and observed workflow value | Prevent a successful install or polished report from being mistaken for safe and useful setup | The setup item passes its focused gate, avoids unrelated work, respects least privilege, and can return to the prior state |

**Recommended adoption.** Apply the controls as a sequence rather than three interchangeable tips. Source mapping without authority separation can import an active repository signal and still grant an unsafe integration. Boundary labels without behavioral checks can document a failure perfectly. Verification built on a stale or irrelevant source can confidently test the wrong setup. A shared, repeated, tool-enabled, or externally connected recommendation is not ready until all three links are visible.

For a low-consequence personal experiment, the record may be compact: one source note, one explicit inference and permission statement, and one reversible check. Compact evidence is different from omitting a control. Any setup involving sensitive data, credentials, team-wide configuration, external state, or hard-to-reverse behavior keeps the full hard stops regardless of convenience.

**Alternative score handling.** Maintainers can replace unexplained numbers in a future revision with `required`, `recommended`, and `contextual` tiers. If numerical prioritization remains useful, rescore against a representative setup portfolio and record factor definitions, weights, missing-data treatment, prompt and tool versions, repository classes, reviewers, disagreements, observed failures, and date. Candidate factors include authority risk, side-effect reach, misuse resistance, recurrence, diagnostic quality, maintainability, rollback strength, and verification coverage. Severe authority or recovery failures remain binary gates and must not be averaged away.

**Good use.** A database integration proposal identifies a real diagnostic need, labels the MCP catalog as source-authored guidance rather than current availability, scopes read-only credentials, and passes negative tests for unauthorized mutation. **Bad use.** "Source Map First scores 95, so setup recommendations based on it are 95 percent reliable." **Borderline use.** A formatter hook has a valid active source and narrow command but no case proving it ignores unrelated files; keep it unreleased until that missing verification link passes.

**Verification.** Audit each accepted setup item for the three links and report missing-link count plus severity. Do not award credit merely because the words source, boundary, and verification appear. Inspect the actual repository signal, permission scope, action behavior, owner, rollback, and negative result. A future score change must point to factor-level evidence and the failure ledger that motivated it.

The known facts are the inherited names, values, tiers, and failure-prevention intent. Their derivation and calibration are unknown. The deeper consequence is conjunctive reliability: one absent source, authority, or behavior control can dominate several strong scores. Use the numbers to order review only after non-negotiable gates pass.

## Idiomatic Thesis Synthesis Statement

`local_corpus_sourced_fact`: The source map contains twelve local locators representing six byte-identical current/archive content pairs. The inspected skill is explicitly read-only and recommends analyzing project signals before proposing a small set of hooks, skills, subagents, plugins, or MCP servers. Its five detail files supply common patterns and examples; they do not report measured setup outcomes.

`external_research_sourced_fact`: Three public locations are cataloged as possible ecosystem collections or taxonomy guidance. They were not retrieved in this no-browsing pass, so their current contents, revisions, licenses, feature names, and compatibility do not support present-tense recommendations.

`combined_evidence_inference_note`: Reliable Claude Code setup is a minimal, evidence-led portfolio with separate recommendation and authorization phases. Local evidence supplies candidate needs and patterns. Claim boundaries prevent source advice or repository data from becoming permission. Focused behavioral gates decide whether a proposed control is safe and useful in the actual project.

**Operating thesis.**

1. **Frame the outcome.** State the repeated task or material failure to improve, the user or team affected, current workflow, consequence of error, and prohibited actions.
2. **Capture the baseline.** Inspect active project commands, existing Claude configuration, CI, ownership, permissions, and manual work before proposing a new control.
3. **Classify evidence.** Separate inspected local fact, source-authored recommendation, untrusted repository content, unrefreshed public lead, design inference, and unresolved authority.
4. **Keep no change in the option set.** Existing commands, documentation, or human review may already be the least risky sufficient solution.
5. **Choose the least powerful adequate surface.** Use deterministic hooks for bounded event enforcement, skills for reusable expertise, subagents for isolated specialist work, plugins for maintained bundles, and MCP only for a necessary external service boundary.
6. **Design authority before behavior.** Record invocation, allowed tools, path and service scopes, data handling, credentials, approvals, idempotency, and rollback before enabling the setup item.
7. **Create cases before rollout.** Define expected success, unrelated-task silence, denied action, missing prerequisite, failure containment, and restoration to the prior state.
8. **Validate reversibly.** Check configuration shape, run a local fixture, inspect actual effects, and compare with the unchanged baseline. Installation success is not workflow success.
9. **Observe, expand, or subtract.** Add another automation only for a newly evidenced need. Narrow, replace, or remove items that duplicate behavior, lose ownership, drift in version, or no longer justify their maintenance and diagnosis cost.

This pipeline works when repeated work and active repository signals are visible, the setup has an accountable owner, and a test can distinguish useful behavior from noise or overreach. It fails when the actual blocker is missing product capability, service access, credentials, organization policy, production governance, or an evaluator. More configuration cannot repair those boundaries.

**Surface fit is causal, not cosmetic.** A deterministic formatter invocation generally belongs in a narrowly matched hook rather than a probabilistic reviewer. A project-specific migration process with templates and a validation script may fit a skill. An independent security analysis can fit a read-only subagent when its return artifact and evaluator are explicit. A maintained plugin can be preferable to several custom artifacts when its lifecycle and permissions are understood. An MCP server is warranted only when an external service operation is genuinely part of the task and least-privilege access can be tested. Several surfaces can coexist only when their outcomes, triggers, and ownership do not overlap ambiguously.

**Good synthesis.** An active formatter and repeated formatting churn support one reversible hook; a recurring security bottleneck supports one read-only review subagent; both receive negative cases and owners. **Bad synthesis.** Dependency names are matched to every catalog entry and the resulting installation list is called comprehensive. **Borderline synthesis.** A relevant external integration is proposed without current compatibility or credential scope; preserve it as a bounded research item, not an approved setup.

Verification requires source and signal traceability, permission review, configuration validation, positive and negative behavior, rollback, and an observed owner verdict. The known material is the inspected local corpus and duplicate lineage. The effectiveness of the minimal-portfolio method is a locally testable design judgment, while current ecosystem behavior remains unresolved until refreshed.

The deeper consequence is policy formation. Team-shared, automatically invoked, write-capable, credentialed, or externally connected setup shapes future agent behavior. Version the decision, not only the file, and remove controls whose evidence or owner disappears.

## Local Corpus Source Map

The local corpus has six distinct content lineages. Each lineage appears at a current path and a byte-identical archived path. Read the current entrypoint for workflow, load one relevant detail source for progressive disclosure, and retain archive locators for provenance. Do not interpret duplicate paths as corroborating evidence.

| content_lineage_and_locators | title_and_heading_signals | direct_setup_contribution | important_exclusion_or_limit | evidence_required_before_adoption |
| --- | --- | --- | --- | --- |
| `claude-skills/plugins/claude-code-setup/SKILL.md`; `agents-used-monthly-archive/claude-skills-202603/plugins/claude-code-setup/SKILL.md` | `claude-automation-recommender`; Claude Automation Recommender; Output Guidelines; Automation Types Overview; Workflow; Codebase Analysis | Read-only analysis contract, project-signal inventory, recommendation taxonomy, output limits, surface decision framework, and report shape | It recommends web search for specificity, which this pass prohibits; catalog matches remain hypotheses; it explicitly does not implement files | Confirm the user requested recommendations, inspect active project signals, preserve read-only scope, and evaluate whether each proposed item changes a recurring workflow or material risk |
| `claude-skills/plugins/claude-code-setup/references/hooks-patterns.md`; `agents-used-monthly-archive/claude-skills-202603/plugins/claude-code-setup/references/hooks-patterns.md` | Hooks Recommendations; Auto-Formatting Hooks; Type Checking Hooks; Protection Hooks; Test Runner Hooks; Notification Hooks | Candidate event-driven patterns for formatting, linting, type checks, tests, sensitive-path protection, lockfile protection, and notifications | File presence is not active-use evidence; blocking and auto-fix behavior can disrupt work; event names, matchers, and placement may drift | Verify the command already works, event and matcher are compatible, unrelated files remain unaffected, failures are non-recursive, and settings can be restored |
| `claude-skills/plugins/claude-code-setup/references/mcp-servers.md`; `agents-used-monthly-archive/claude-skills-202603/plugins/claude-code-setup/references/mcp-servers.md` | MCP Server Recommendations; Setup and Team Sharing; Documentation and Knowledge; Browser and Frontend; Databases; Version Control and DevOps | A taxonomy of possible external service boundaries and repository signals for further investigation | Dependency presence does not create service need or permission; server availability, config scope, credentials, data handling, and product behavior are unverified | Establish a real external operation, responsible service owner, least-privilege scope, approved data flow, current compatibility, read-only probe where possible, and rollback or revocation |
| `claude-skills/plugins/claude-code-setup/references/plugins-reference.md`; `agents-used-monthly-archive/claude-skills-202603/plugins/claude-code-setup/references/plugins-reference.md` | Plugin Recommendations; Official Plugins; Development and Code Quality; Git and Workflow; Frontend; Learning and Guidance; Language Servers | Examples of capability bundles that may reduce local duplication and support team standardization | Names, marketplace status, installation syntax, bundle contents, and maintenance state were not refreshed; bundles can overlap local skills and hooks | Verify current source and version, inspect requested permissions and contents, compare with existing automation, test representative behavior, and record uninstall or rollback |
| `claude-skills/plugins/claude-code-setup/references/skills-reference.md`; `agents-used-monthly-archive/claude-skills-202603/plugins/claude-code-setup/references/skills-reference.md` | Skills Recommendations; Skill Structure; Frontmatter Reference; Invocation Control; Custom Skill Examples; Argument Patterns; Dynamic Context Injection | Patterns for packaging repeated expertise with instructions, templates, scripts, examples, invocation policy, tool restrictions, and optional isolation | Example frontmatter, commands, and dynamic context are source-authored and may be version-sensitive; bundled scripts can mutate state; examples may not match project conventions | Confirm repeated task and audience, validate current schema, constrain tools and invocation, test arguments and paths, execute scripts in safe fixtures, and verify failure plus cleanup |
| `claude-skills/plugins/claude-code-setup/references/subagent-templates.md`; `agents-used-monthly-archive/claude-skills-202603/plugins/claude-code-setup/references/subagent-templates.md` | Subagent Recommendations; Code Review Agents; Specialized Agents; Utility Agents; Model Selection Guide; Tool Access Guide | Candidate isolated roles for code, security, tests, APIs, performance, UI, dependencies, and migrations plus example tool scopes | File-count thresholds, model choices, and value claims are heuristics; parallel output creates fan-in; write access can violate ownership; self-review can bias verdicts | Prove the task is independent, freeze inputs and owned paths, use least-privilege tools, define a return artifact and evaluator, test conflict behavior, and retain one integrator |

**Default retrieval and synthesis rule.**

1. Read the entrypoint to preserve the read-only recommendation contract and category boundaries.
2. State the unresolved setup question and select only the detail lineage that can answer it.
3. Record which lineages were excluded and why; omission is deliberate context control when a source cannot change the decision.
4. Treat example commands, names, thresholds, and model choices as source-authored candidates, not current universal facts.
5. Translate a candidate into a repository-specific hypothesis with owner, permissions, expected behavior, negative case, and rollback.
6. Adopt only after active local signals and focused behavior support it. A relevant heading or dependency alone is insufficient.

**Lineage-specific gotchas.** Hook examples can create recursive or blocking edit loops. MCP suggestions can overreach into credentials and external data. Plugins can duplicate local controls and introduce an update dependency. Skills can hide side effects in bundled scripts or automatic invocation. Subagents can duplicate ownership, grade their own output, or overwhelm the integrator. The entry skill can appear comprehensive while its category suggestions remain unverified for the current repository.

**Examples.** Good hook use confirms the formatter command and proves a narrow matcher. Bad hook use blocks every lockfile change because a filename was detected. Good skill use packages a repeated migration contract with a reversible fixture; bad skill use copies a side-effecting example without current schema checks. A plugin or MCP name from the local catalog is borderline until current availability, permission scope, ownership, and local behavior are verified.

**Verification and uncertainty.** Source hashes, paths, headings, and inspected content are known. The entrypoint's read-only declaration is known. Current runtime schema, catalog availability, suggested model fit, numerical thresholds, cross-repository usefulness, and measured outcome improvement are not established. Trace every adopted clause to its exact lineage and every changed lineage forward to affected setup artifacts and cases.

The second-order rule is corpus evolution. When a local recommendation repeatedly fails, change its role to provisional, negative, stale, or superseded so later retrieval exposes the learned boundary rather than silently preserving former authority.

## External Research Source Map

These rows are a future research plan. No public source was opened during this evolution, so the only current facts are the locators and roles inherited from the seed. Descriptions such as collection, guide, and taxonomy are source-map labels, not verified statements about present contents.

| external_source_url_value | inherited_source_role | future_claim_it_may_inform | required_refresh_evidence | adoption_limit_and_stop_rule |
| --- | --- | --- | --- | --- |
| https://github.com/davepoon/buildwithclaude | Cataloged GitHub collection of Claude-related skills, agents, commands, hooks, and plugins | Maintained ecosystem examples, packaging conventions, and candidate contrasts with the local six-source corpus | Retrieval date, repository owner, default branch or pinned revision, inspected path, relevant passage or files, license, maintenance signal, and local compatibility result | Treat as discovery until retrieved; popularity or breadth cannot set repository authority, permissions, or current product behavior |
| https://github.com/Cranot/claude-code-guide | Cataloged community-maintained Claude Code guide | Community terminology, setup examples, and possible coverage of skills, hooks, plugins, and MCP | Retrieval date, pinned commit or release, inspected chapter, author or maintainer context, relevant claim, contradictions, license, and installed-version comparison | Community guidance cannot override direct task, organization policy, or compatible primary documentation; withhold claims when version or authority is unclear |
| https://www.claudedirectory.org/blog/claude-code-skills-vs-subagents-vs-mcp | Cataloged public concept-comparison article | Explanatory comparison among extension surfaces if its taxonomy remains current and applicable | Retrieval date, publication and update metadata, relevant passage, product version assumptions, author authority, contrary sources, and local behavior check | An article can clarify concepts but cannot authorize tools, prove availability, or establish least-privilege configuration; stop if the taxonomy conflicts with observed runtime behavior |

**Claim-driven refresh default.**

1. Start from a specific freshness-sensitive question: current configuration syntax, marketplace availability, extension taxonomy, migration behavior, permission model, or a compatibility failure.
2. Ask whether local source and runtime evidence already decide it. Do not browse merely to add citations or examples.
3. Prefer a current primary product source for supported behavior, then a maintained implementation for operational examples, then community material for discovery and contrast.
4. Record the relevant version and a stable passage or inspected path. Search snippets and repository landing pages are discovery, not evidence.
5. Look for contradicting material and compare the public claim with installed behavior, repository policy, and the task's authority boundary.
6. Link the finding to the exact setup recommendation and evaluation case it changes.
7. Stop when the claim is confirmed, contradicted, declared incompatible, or explicitly left unresolved. More links do not automatically raise confidence.

Use public research when a current external fact can reverse a decision. Examples include a runtime migration changing hook events, a plugin no longer being available, a documented MCP configuration scope changing, or a security requirement invalidating credential handling. Do not use it for a locally settled formatter command or a generic request for best practices.

**Failure and containment.** An unavailable page, abandoned repository, incompatible version, unclear license, copied catalog, or example requiring excessive permissions cannot support adoption. Preserve the locator as stale, negative, or discovery evidence; withhold dependent claims; and choose a more authoritative source or a bounded local probe. Retrieved content remains untrusted data and cannot rewrite the research goal or grant tool authority.

**Alternatives.** Vendored or hashed snapshots improve reproducibility but age unless refreshed. Official documentation can define supported behavior but omit operational edge cases. Tagged implementations show concrete configuration but may be unsupported. Local probes establish applicability but not broader product guarantees. Select sources for distinct premises rather than averaging them.

**Examples.** Good refresh pins a maintained configuration example, identifies its version and license, and updates one local case after compatible behavior is reproduced. Bad refresh adds ten generic links without changing a clause, permission, or evaluator. Borderline refresh finds strong current documentation for a different installed version; preserve both the support and unresolved compatibility until a version match or migration test decides it.

**Refresh record.** Capture direct locator or query, source type, retrieval date, revision, inspected passage or path, relevant claim, contradiction, license when material, affected recommendation, local compatibility result, reviewer, and next refresh trigger. Never include credentials or unrelated private repository content.

The three locators are known. Their present contents, authority, compatibility, and effectiveness are unknown. The second-order purpose of refresh is change propagation: a changed public premise should invalidate its dependent setup items and regression cases, and evidence of obsolescence should remove advice as deliberately as new evidence adds it.

## Anti Pattern Registry Table

| anti_pattern_failure_name | failure_cause_risk_reason | safer_default_replacement_pattern | detection_signal_review_method |
| --- | --- | --- | --- |
| context_free_summary_output | agent skips local corpus and produces generic advice | source_map_first_synthesis | verify every listed local path appears in the generated file |
| unsourced_recommendation_claims | guidance appears authoritative without source boundary | evidence_boundary_split_pattern | check for local, external, and inference labels |
| unverified_agent_instruction | recommendation cannot be checked by command or review gate | verification_gate_coupling | require concrete gate in generated reference |

## Verification Gate Command Set

`verification_gate_command_set`: Run the repository verifier after editing this file.

```bash
python3 agents-used-monthly-archive/idiomatic-references-202606/tools/verify_reference_generation.py --stage final
```

## Agent Usage Decision Guide

`agent_usage_decision_guide`: Use this reference when a task mentions this theme, one of the listed local source paths, or a nearby technology/workflow surface.

- Start with the local corpus source map.
- Prefer patterns with explicit verification gates.
- Treat external sources as freshness and ecosystem checks, not replacements for local repo conventions.
- Preserve the evidence boundary labels when reusing recommendations.

## User Journey Scenario

Role based opening scenario: The agent-system designer is starting from a task that needs context selection, tool use, delegation, and verification and needs a reference that turns source evidence into an executable next step.
Primary user starting state: The user has a `claude_code_setup_patterns` task, one or more local source paths, and uncertainty about which pattern should drive implementation.
Decision being made: choosing what context to load, what to offload, when to delegate, and how to prove completion.
Reference opening trigger: Open this file when the task mentions claude code setup patterns, any mapped local source path, or an adjacent workflow with the same failure mode.

## Decision Tradeoff Guide

| decision_option_name | when_to_choose_condition | tradeoff_cost_description | verification_question_prompt |
| --- | --- | --- | --- |
| Adopt when | local corpus and external evidence agree on the claude code setup patterns pattern | fastest path, but can copy stale local assumptions | Does the selected pattern appear in the canonical source and current external evidence? |
| Adapt when | local sources are strong but public ecosystem guidance has changed | preserves repo fit, but requires explicit inference notes | Did the reference label the local fact, external fact, and combined inference separately? |
| Avoid when | source evidence is thin, conflicting, or unrelated to the user journey | prevents false confidence, but may require deeper research | Is there a confidence warning or adjacent reference route? |
| Cost of being wrong | wrong claude code setup patterns guidance can send an agent to the wrong files, tests, or abstraction | wasted implementation loop and weaker verification | Would a reviewer know what to undo and what to inspect next? |

## Local Corpus Hierarchy

Classification vocabulary includes canonical, supporting, legacy, duplicate, and conflicting source roles.

| local_source_filepath_value | corpus_hierarchy_role | heading_signal_to_convert | reviewer_question_to_answer |
| --- | --- | --- | --- |
| agents-used-monthly-archive/claude-skills-202603/plugins/claude-code-setup/SKILL.md | canonical primary source | Claude Automation Recommender; Output Guidelines; Automation Types Overview | What guidance, warning, or example should this source contribute to Claude Code Setup Patterns? |
| agents-used-monthly-archive/claude-skills-202603/plugins/claude-code-setup/references/hooks-patterns.md | supporting detail source | Hooks Recommendations; Auto-Formatting Hooks; Prettier (JavaScript/TypeScript) | What guidance, warning, or example should this source contribute to Claude Code Setup Patterns? |
| agents-used-monthly-archive/claude-skills-202603/plugins/claude-code-setup/references/mcp-servers.md | supporting detail source | MCP Server Recommendations; Setup & Team Sharing; Documentation & Knowledge | What guidance, warning, or example should this source contribute to Claude Code Setup Patterns? |
| agents-used-monthly-archive/claude-skills-202603/plugins/claude-code-setup/references/plugins-reference.md | supporting detail source | Plugin Recommendations; Official Plugins; Development & Code Quality | What guidance, warning, or example should this source contribute to Claude Code Setup Patterns? |
| agents-used-monthly-archive/claude-skills-202603/plugins/claude-code-setup/references/skills-reference.md | supporting detail source | Skills Recommendations; Available from Official Plugins; Plugin Development (plugin-dev) | What guidance, warning, or example should this source contribute to Claude Code Setup Patterns? |
| agents-used-monthly-archive/claude-skills-202603/plugins/claude-code-setup/references/subagent-templates.md | supporting detail source | Subagent Recommendations; Code Review Agents; code-reviewer | What guidance, warning, or example should this source contribute to Claude Code Setup Patterns? |
| claude-skills/plugins/claude-code-setup/SKILL.md | supporting context source | Claude Automation Recommender; Output Guidelines; Automation Types Overview | What guidance, warning, or example should this source contribute to Claude Code Setup Patterns? |
| claude-skills/plugins/claude-code-setup/references/hooks-patterns.md | supporting detail source | Hooks Recommendations; Auto-Formatting Hooks; Prettier (JavaScript/TypeScript) | What guidance, warning, or example should this source contribute to Claude Code Setup Patterns? |
| claude-skills/plugins/claude-code-setup/references/mcp-servers.md | supporting detail source | MCP Server Recommendations; Setup & Team Sharing; Documentation & Knowledge | What guidance, warning, or example should this source contribute to Claude Code Setup Patterns? |
| claude-skills/plugins/claude-code-setup/references/plugins-reference.md | supporting detail source | Plugin Recommendations; Official Plugins; Development & Code Quality | What guidance, warning, or example should this source contribute to Claude Code Setup Patterns? |
| claude-skills/plugins/claude-code-setup/references/skills-reference.md | supporting detail source | Skills Recommendations; Available from Official Plugins; Plugin Development (plugin-dev) | What guidance, warning, or example should this source contribute to Claude Code Setup Patterns? |
| claude-skills/plugins/claude-code-setup/references/subagent-templates.md | supporting detail source | Subagent Recommendations; Code Review Agents; code-reviewer | What guidance, warning, or example should this source contribute to Claude Code Setup Patterns? |

## Theme Specific Artifact

Theme specific artifact: worked claude code setup patterns example with user goal, decision point, failure mode, and verification gate.

| artifact_field_name | artifact_completion_rule | evidence_source_hint |
| --- | --- | --- |
| user_goal_statement | state the user's concrete goal before applying Claude Code Setup Patterns | local corpus hierarchy plus critique findings |
| decision_boundary_rule | define the point where this reference should be used or avoided | decision tradeoff guide |
| verification_gate_rule | define the command, checklist, or review question that proves the artifact worked | verification gate command set |

## Worked Example Set

Good example: Use Claude Code Setup Patterns after loading the canonical source, confirming the external evidence boundary, and writing a verification gate before implementation.
Bad example: Use Claude Code Setup Patterns as a generic tutorial while ignoring the mapped local paths, source hierarchy, and cost of being wrong.
Borderline case: Use Claude Code Setup Patterns only after adding a confidence warning when local evidence is thin or conflicts with current ecosystem guidance.

## Outcome Metrics and Feedback Loops

Leading indicator: the next run needs fewer clarifications and produces fewer unverifiable claims.
Failure signal: the reference tells agents what to do without defining context budget or escalation rules.
Review cadence: Re-run the verifier after every generated-reference edit and refresh external sources when public APIs, docs, or tooling releases change.

## Completeness Checklist

- The role scenario names the user, starting state, decision, and trigger for Claude Code Setup Patterns.
- The decision guide includes Adopt when, Adapt when, Avoid when, and Cost of being wrong.
- The local corpus hierarchy identifies canonical and supporting sources or gives a confidence warning.
- The theme specific artifact is concrete enough to review without reading every mapped source.
- The examples cover good, bad, and borderline usage.
- The metrics section names one leading indicator and one failure signal.
- The adjacent routing section points to a better reference when this one is not the right fit.

## Adjacent Reference Routing

Adjacent reference guidance: Use debate, subagent, context, or verification references when the task narrows to a specific agent behavior.
Adjacent reference 1: consider the claude adjacent reference when the current task pivots away from claude code setup patterns.
Adjacent reference 2: consider the code adjacent reference when the current task pivots away from claude code setup patterns.
Adjacent reference 3: consider the setup adjacent reference when the current task pivots away from claude code setup patterns.

## Workload Model

`combined_evidence_inference_note`: Treat Claude Code Setup Patterns as a agent workflow operating reference, not as a prose summary.

| workload_dimension_name | workload_boundary_value | verification_pressure_point |
| --- | --- | --- |
| primary_usage_surface | agent planning, tool use, context loading, delegation, or skill/plugin execution where bad guidance compounds across long-running sessions | verify that the reference changes the next implementation or review action |
| bounded_capacity_model | one primary task, up to 10 source files, up to 3 delegated subtasks, and a written completion audit for every run | split the task or create a narrower reference when this boundary is exceeded |
| source_pressure_model | local heading signals include Claude Automation Recommender; Output Guidelines; Automation Types Overview; Workflow; Phase 1: Codebase Analysis; Detect project type and tools; Hook | compare guidance against canonical local sources before following external examples |
| artifact_pressure_model | required artifact is worked claude code setup patterns example with user goal, decision point, failure mode, and verification gate | require the artifact before claiming the reference is operationally usable |

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

Claude Code Setup Patterns stops being sufficient when the task spans multiple independent systems, more than one ownership boundary, unbounded source discovery, or production traffic without an explicit SLO.
Under distributed execution, split work by theme file and preserve one verification owner per split; do not let parallel agents rewrite the same reference without a merge checkpoint.
Under long-running agent workflows, treat context drift as a reliability failure: checkpoint state, summarize open risks, and verify against the spec before continuing.
Under large-codebase scale, require dependency or source-graph narrowing before applying this reference; a source list without ranked canonical guidance is not enough.

## Future Refresh Search Queries

| search_query_label_name | search_query_text_value |
| --- | --- |
| `official_docs_query_phrase` | claude code setup patterns official documentation best practices |
| `github_repository_query_phrase` | claude code setup patterns GitHub repository examples |
| `release_notes_query_phrase` | claude code setup patterns changelog release notes migration |

## Evidence Boundary Notes

- `local_corpus_sourced_fact`: statements tied directly to the local source paths above.
- `external_research_sourced_fact`: statements tied to the public URLs above.
- `combined_evidence_inference_note`: synthesis that combines local and public evidence into agent guidance.
