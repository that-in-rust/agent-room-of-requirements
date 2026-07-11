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

An anti-pattern is operational only when the reviewer can detect its trigger, rank its consequence, contain any effect, choose a safer replacement, identify an owner, and prove recovery. Phrase-presence checks are useful for structure but cannot establish setup behavior.

| anti_pattern_failure_name | trigger_and_observable_signal | consequence | immediate_containment | safer_default_replacement | recovery_and_regression_proof |
| --- | --- | --- | --- | --- | --- |
| context_free_summary_output | Recommendations could be copied to an unrelated repository; no active command, owner, or workflow changes the list | Generic automation adds noise and authority without project value | Stop implementation and retain the unchanged baseline | Repository-signal-first diagnosis with explicit no-change option | Each accepted item maps to an active signal, outcome, owner, and focused case |
| unsourced_recommendation_claims | A current product, availability, security, or compatibility claim has no inspected source or explicit inference boundary | Reviewers cannot distinguish local fact from stale catalog advice | Withhold the claim and dependent setup item | Claim-scoped evidence ledger with access and version state | Source and local behavior support the bounded claim; unresolved parts remain labeled |
| unverified_agent_instruction | Setup is accepted because prose looks detailed or configuration parses | Invalid matching, permissions, or behavior escapes review | Block release of the affected automation | Verification-gate coupling with positive, negative, and rollback cases | Exact focused results and owner verdict travel with the setup version |
| recommendation_implementation_conflation | A read-only analysis immediately writes settings, installs software, or connects a service | Recommendation scope launders unapproved mutation | Stop writes and inspect changed state | Separate recommendation artifact from explicitly authorized implementation | Prior state restored or accepted by owner; implementation scope and cases are approved |
| dependency_name_automation_match | A dependency, directory, or config filename directly triggers a hook, plugin, or MCP recommendation | Vestigial or incidental signals create irrelevant setup | Reclassify the signal as unconfirmed | Verify active command, repeated task, owner, and failure cost | Evidence shows the workflow is active and the chosen surface changes it usefully |
| duplicate_surface_ownership | Two hooks, skills, agents, plugins, or integrations own the same trigger and output | Duplicate actions, conflicting edits, or unclear diagnosis | Disable one path and freeze expansion | One primary owner with explicit composition only for independent outcomes | Event and task matrix shows no overlapping effect or ambiguous owner |
| blocking_or_recursive_hook | Event invocation repeats, blocks normal edits, or calls a command that retriggers itself | Development stalls or files churn indefinitely | Disable the hook and restore affected files or settings | Narrow matcher, idempotent command, timeout, and fail-open or fail-closed policy | Simulated event runs once, handles failure, and ignores unrelated paths |
| sensitive_path_or_secret_exposure | Setup reads, logs, transmits, or edits secrets beyond the declared task | Credential or private-data compromise | Revoke access, restrict logs, and follow local incident policy | Data minimization, deny rules, least privilege, and redacted fixtures | Authorized owner confirms containment and negative secret-handling cases pass |
| overbroad_mcp_authority | External integration receives write, administrative, or unrelated service scopes | Agent can mutate external state outside user intent | Disconnect or revoke scopes and inspect external activity | Necessary service only, least-privilege credentials, read-only probe, explicit approvals | Permission matrix and service audit show no undeclared access or effect |
| unverified_external_catalog_entry | A plugin, server, command, or taxonomy is assumed current from local catalog text | Installation fails or incompatible behavior enters team policy | Keep the item as an unrefreshed lead | Versioned primary-source refresh plus compatible local test | Current source, revision, permissions, install behavior, and uninstall path are recorded |
| opaque_plugin_bundle_adoption | A bundle is installed without inventorying skills, agents, hooks, commands, or permissions | Hidden overlap and update dependencies enter the repository | Disable the bundle and compare prior behavior | Inspect bundle contents and prefer maintained bundle only when it replaces known local duplication | Representative features pass; overlaps, permissions, version, owner, and removal are documented |
| overpowered_or_self_grading_subagent | An analysis agent receives writes or judges its own preferred output without independent criteria | Isolated context becomes unreviewed authority or conflicting mutation | Cancel writes and quarantine the result | Least-privilege tools, immutable inputs, explicit return artifact, independent evaluator | Same task passes with no ownership violation and integrator can reproduce the verdict |
| unsafe_skill_invocation_or_script | Automatic invocation or bundled script can deploy, commit, send, migrate, or alter shared state unexpectedly | Reusable expertise becomes a hidden side-effect channel | Disable invocation and inspect script effects | User-controlled invocation for side effects, constrained tools, safe fixtures, and failure checks | Argument, path, permission, failure, cleanup, and negative invocation cases pass |
| stale_or_divergent_team_configuration | Checked-in, personal, and archived settings or sources no longer agree | Team members receive inconsistent behavior and evidence | Pin the trusted state and stop rollout | Named owner, versioned shared config, compatibility notes, and migration plan | Clean-environment replay matches documented behavior and stale copies are invalidated |
| ownerless_setup_and_rollback | No person or process owns updates, alerts, failures, credentials, or removal | Broken automation persists as invisible repository policy | Pause adoption or disable active effects | Assign accountable owner, support boundary, rollback, and retirement trigger | Owner accepts evidence and a second reviewer can restore the prior state |

**Default response.** Stop the affected behavior, preserve configuration and action evidence, classify the failed layer, inspect side effects, restore or bound state, choose the least-powerful replacement, and rerun the trigger plus nearby negative cases. A recommendation-only defect may need no fictional rollback; an active credentialed integration requires state and access review.

Use structural lint for missing fields, event simulation for hook matching and recursion, inert fixtures for skills and subagents, sandboxed integration tests where authorized, and human review for authority and surface fit. Production or credential incidents remain with domain owners.

**Good handling.** A database integration is paused because no service owner or read-only scope exists. **Bad handling.** It is approved from a package dependency and a catalog row. **Borderline handling.** A local read-only probe is allowed under isolated credentials while every write scope remains disabled; promotion requires owner approval, current compatibility, negative permission cases, and revocation proof.

The seed establishes three generic failures but provides no incident distribution. Expanded severity is systems judgment until calibrated with versions, incidents, near misses, detection delay, containment success, false positives, and recurrence. Repeated failures at the same layer should change the mechanism or permission boundary, not merely lengthen the prompt.

## Verification Gate Command Set

`verification_gate_command_set`: Preserve the inherited archive verifier as one evidence layer:

```bash
python3 agents-used-monthly-archive/idiomatic-references-202606/tools/verify_reference_generation.py --stage final
```

That command validates the archived corpus and its encoded specification. It does not by itself prove that this dated working reference is expanded, that its question packet is complete, or that any proposed Claude Code automation is safe and useful. The focused working-file gate is:

```bash
python3 tests/verify_idiomatic_reference_file.py --path idiomatic-ref-202607/claude_code_setup_patterns-20260710.md
```

Project-specific setup commands must be discovered from the repository and recorded exactly. Do not invent `npm`, `pytest`, `cargo`, formatter, plugin, or runtime commands from a catalog match.

| verification_gate_layer | claim_it_can_falsify | required_evidence | important_limit |
| --- | --- | --- | --- |
| frozen_source_identity_gate | The intended seed and semantic spans were used before edits | Seed digest, 146 source-span hashes, path owner, heading inventory, and line coverage | Identity does not establish guidance quality |
| focused_reference_structure_gate | All 26 headings, section growth, packet counts, mandatory fields, uniqueness, and placeholder rules hold | Canonical focused verifier output and static checks | Structure does not prove setup behavior |
| source_and_repository_signal_gate | A recommendation is grounded in applicable source material and an active project workflow | Passage locator, command or ownership evidence, exclusions, and source access state | Signal presence does not grant permission |
| configuration_shape_gate | The selected runtime accepts the settings, frontmatter, manifest, or connection schema | Compatible parser, built-in diagnostic, or isolated load result with version | A valid configuration can still be unsafe or irrelevant |
| permission_and_data_boundary_gate | Tools, paths, credentials, services, and data handling stay within declared authority | Permission matrix, secret exclusions, approval record, and denied-action cases | Paper permissions need behavior confirmation |
| surface_behavior_gate | The hook, skill, subagent, plugin, or MCP integration performs the intended task | Fixed positive case, expected output or action, exact command, and observed result | One happy case does not establish scope |
| unrelated_task_negative_gate | The setup remains silent or refuses when trigger, path, authority, or prerequisite is absent | Unrelated file, denied action, malformed input, missing service, and injected instruction cases | Negative cases must rotate to avoid memorization |
| overlap_and_fan_in_gate | Several setup items do not duplicate effects or create ambiguous ownership | Trigger-to-output matrix, parallel result audit, and one integration owner | Low-frequency conflicts may need longer observation |
| rollback_and_revocation_gate | The prior safe state can be restored and external authority can be removed | Before/after config, uninstall or disable step, credential revocation, state inspection, and rerun | Some external effects are irreversible and need stronger prevention |
| semantic_owner_review_gate | The chosen surface, maintenance cost, residual risk, and no-change comparison are acceptable | Independent reviewer or accountable owner decision with rejected alternatives | Human judgment can disagree and must expose uncertainty |

**Default order.** Run cheap identity and shape checks first, then permission review, then inert or reversible behavior, then negative scope, overlap, rollback, and semantic acceptance. A passing earlier layer never overrides a later authority or effect failure. Skip a gate only when the reason is explicit and the omitted claim is not part of completion.

**Evaluation record.** Capture setup version, source and repository signal, exact command or review procedure, runtime and tool versions, fixture, trusted and untrusted inputs, expected behavior, observed output and actions, violations, state before and after, reviewer disposition, and residual uncertainty. Keep evidence compact and redact secrets; raw transcripts and credentials are not release artifacts.

**Failure interpretation.** A deterministic contract or permission failure requires changing the owning source inference, configuration, surface, evaluator, or integration before rerun. An isolated transient environment failure may justify a bounded unchanged retry after it is demonstrated to be transient. A global suite can remain red because other owned files are incomplete; report that condition and continue focused checks without editing another owner's work. Never weaken expected behavior merely to make the setup green.

**Good evidence.** A hook configuration parses, runs once on an intended fixture, ignores unrelated and sensitive paths, handles command failure without recursion, and can be disabled cleanly. **Bad evidence.** "The plugin installed successfully." **Borderline evidence.** An MCP configuration parses and connects but requests broader service scopes than the task needs; the permission failure blocks adoption despite structural success.

Verification is executable setup memory. Every accepted recommendation maps to a gate capable of disproving it, and every failed gate maps back to the source, authority, configuration, evaluator, or mechanism that owns repair.

## Agent Usage Decision Guide

`agent_usage_decision_guide`: Use this reference when the user wants to analyze, recommend, review, implement, or simplify repository-level Claude Code setup and the choice among hooks, skills, subagents, plugins, MCP servers, existing commands, documentation, or no change is material. A theme word alone is not sufficient. Route product support, credential issuance, security incidents, and production operations to their controlling workflows.

1. **State the outcome and phase.** Is the user exploring options, requesting a recommendation, reviewing existing setup, or authorizing implementation? Name the recurring task or failure, affected users, consequence, and prohibited actions.
2. **Capture the unchanged baseline.** Inventory active commands, tests, formatters, CI, service dependencies, existing `.claude/` configuration, team practices, owners, and current pain. A file or dependency is only a lead until active use is confirmed.
3. **Decide whether setup is the problem.** Resolve unclear product requirements, missing data, or ordinary code defects before proposing automation. Keep no change, documentation, or an existing command in the option set.
4. **Classify recurrence and consequence.** One reversible lookup needs less machinery than a shared auto-invoked control or an external service integration.
5. **Map evidence and authority.** Separate direct task instructions, repository policy, inspected local facts, source-authored guidance, untrusted content, unrefreshed public leads, design inference, and unresolved owner decisions.
6. **Choose the least-powerful adequate surface.** Match deterministic events to hooks, reusable expertise to skills, independent specialist analysis to subagents, maintained bundles to plugins, and necessary external operations to MCP. Compose surfaces only for distinct outcomes.
7. **Design permission and ownership.** Record invocation, tools, paths, service scopes, credentials, data handling, approvals, idempotency, owner, failure behavior, rollback, and retirement before implementation.
8. **Recommend before mutating unless implementation is explicit.** A recommendation report does not authorize settings writes, installation, network access, commits, or service connection.
9. **Run focused positive and negative cases.** Verify intended behavior, unrelated-task silence, denied actions, failure containment, overlap, and restoration to the prior state.
10. **Close with a lifecycle state.** Mark each item proposed, adopted, observed, narrowed, paused, replaced, rejected, or retired, and name the evidence that triggers reconsideration.

| setup_branch | choose_when | avoid_or_route_when | minimum_evidence |
| --- | --- | --- | --- |
| No change, existing command, or documentation | Current workflow is sufficient, task is rare, or automation cost exceeds recurring value | A stable repeated failure remains unaddressed | Baseline command or process, owner confirmation, and reason automation adds no net value |
| Hook | Behavior is deterministic, event-bound, narrow, fast, and safely repeatable | Judgment is contextual, command can recurse, event is unclear, or blocking semantics are unsafe | Active command, compatible event and matcher, timeout/failure policy, unrelated-path test, and disable path |
| Skill | A repeatable workflow benefits from instructions, templates, scripts, examples, arguments, or controlled invocation | Task is one-off, schema is unknown, or bundled actions cannot be safely scoped | Repeated task sample, current schema, tool and invocation controls, fixture, failure behavior, and maintenance owner |
| Subagent | Work is independently scoped, context isolation helps, tool access can be least privilege, and one return artifact can be evaluated | Work shares mutable state, ownership overlaps, or independent evaluation is absent | Immutable inputs, owned paths, tool list, return contract, evaluator, fan-in owner, and conflict case |
| Plugin | A maintained bundle replaces several related local capabilities and team distribution matters | Contents or marketplace status are unknown, bundle overlaps local setup, or update ownership is absent | Current version and source, content inventory, permissions, representative tests, owner, and uninstall plan |
| MCP server | A necessary external service operation cannot be met by local tools and approved least-privilege access exists | Dependency presence is the only signal, credentials or data policy are unresolved, or write effects lack recovery | Service owner, current compatibility, data flow, scopes, read-only probe where possible, denied-action test, revocation, and audit |

**Stop and route.** If the user outcome is undecided, ask the smallest material question. If product behavior is freshness-sensitive, create a permitted primary-source refresh task. If service or credential authority is missing, return a permission and data-flow artifact to the owner. If production traffic, security response, or irreversible state is involved, this reference remains supporting guidance rather than the controlling process.

**Gotchas.** Do not trigger a mega-analysis from a theme keyword, list every category to appear comprehensive, implement a recommendation without authorization, load every catalog into context, or retain overlapping controls. When candidate recommendations accumulate faster than the user can evaluate them, stop discovery and narrow by outcome, consequence, and owner.

**Examples.** A repository with an active formatter and repeated churn may receive one narrowly tested hook. A recurring migration procedure may receive a user-controlled skill with validation and rollback. Applying a full setup portfolio to a one-time timestamp request is misuse. A proposed MCP integration with a real service need but no owner or scope is a valid pause: deliver the missing permission, compatibility, and probe requirements without connecting it.

**Verification.** The decision log records outcome, phase, baseline, evidence, selected branch, rejected alternatives, permissions, cases, observed result, owner, rollback, residual risk, and lifecycle state. Include cases where no change and routing are correct so evaluation does not reward automation by default.

The branch thresholds are design guidance, not universal measurements. Revisit setup when runtime or source versions change, ownership disappears, permissions expand, failure recurs, surfaces overlap, or the original repository signal vanishes. A mature setup can shrink.

## User Journey Scenario

Role based opening scenario: An agent-system designer or repository maintainer has a recurring workflow problem, an existing or proposed Claude Code setup, and uncertainty about whether no change, documentation, a hook, a skill, a subagent, a plugin, or an MCP integration is the right control.

Primary user starting state: The user can describe an outcome or pain point but may not know which project signals are active, which setup already exists, which authority boundary controls implementation, or how to verify value without creating external side effects.

Decision being made: Determine whether setup is the problem, select the least-powerful adequate surface, separate recommendation from implementation permission, validate behavior and rollback, and assign an observed lifecycle state.

Reference opening trigger: Open this file when repository-level setup choice or review is material. Do not open it merely because Claude Code is mentioned; route debugging, product support, incident response, and ordinary feature work to their own workflows.

**End-to-end journey.**

1. **Intake.** Record the user-visible outcome, current phase, affected users, recurrence, consequence of error, and prohibited actions. Decide whether the request is exploration, recommendation, review, or implementation.
2. **Baseline.** Inspect active project commands, tests, CI, service dependencies, ownership, existing `.claude/` files, personal-versus-project configuration, and the current manual path. Save the unchanged state needed for comparison and rollback.
3. **Problem-fit check.** Ask whether an unresolved requirement, missing data, code defect, or organization policy owns the pain instead. Close with no setup change or route when automation is not the repair.
4. **Evidence map.** Load the read-only entry skill and only the relevant detail lineage. Separate source fact, heuristic, unrefreshed public lead, untrusted content, design inference, and controlling authority.
5. **Candidate narrowing.** Generate only decision-relevant options, including no change. Apply backpressure when candidates outnumber the user's ability to compare evidence and ownership.
6. **Surface selection.** Match deterministic events to hooks, reusable workflows to skills, independent analysis to subagents, maintained bundles to plugins, and necessary external operations to MCP. Record why the simpler and nearest adjacent alternatives were rejected.
7. **Authority design.** Specify invocation, tools, paths, service scopes, credentials, data handling, approvals, idempotency, failure behavior, owner, rollback, and retirement. Unknown authority creates a pause artifact rather than implied permission.
8. **Recommendation close or implementation approval.** Recommendation-only work ends with evidence, ranked items, rejected alternatives, risks, and next approval. Configuration changes begin only when the user has authorized exact owned paths and effects.
9. **Reversible implementation.** Change one major setup item at a time, preserve prior state, validate compatible schema, and avoid simultaneous prompt, evaluator, and mechanism changes that destroy attribution.
10. **Focused evaluation.** Run positive behavior, unrelated-task silence, denied action, malformed input, overlap, failure containment, rollback, and regression cases. Inspect state, not only output text.
11. **Observation.** Compare with the unchanged baseline for workflow value, noise, latency, review burden, duplicate effects, and user adoption. Installation alone is not success.
12. **Lifecycle close.** Mark the item proposed, adopted, observed, narrowed, paused, replaced, rejected, or retired. Record owner, version assumptions, residual risk, next trigger, and a resumable checkpoint if another session or owner continues.

**Failure transitions.** An ambiguous outcome returns to intake. Inactive repository signals return to baseline or no change. Missing current-product evidence creates a permitted refresh task. Missing service ownership or credentials creates a permission and data-flow handoff. Configuration failure returns to the schema or version layer. Unauthorized behavior stops effects and invokes containment. Failed rollback blocks rollout and may change the selected surface. Unmeasurable value returns the recommendation to provisional or retired rather than inviting more automation.

**Good journey.** Repeated formatting churn is confirmed against an active command, one hook is selected over a broader plugin, a narrow matcher and failure policy are approved, related and unrelated fixtures pass, and the team observes lower churn without blocking edits. **Bad journey.** Dependency names produce a multi-category installation list that is implemented immediately and closed when each item reports success. **Borderline journey.** A service integration addresses a real need, but owner, credential scope, and current compatibility are absent; the correct artifact is a bounded permission and refresh packet while all connection changes remain frozen.

**Success condition.** Another reviewer can reconstruct why setup was or was not chosen, what evidence and authority controlled each transition, which behavior passed or failed, what state changed, how to restore it, and who owns the next lifecycle event. Test the journey with no-change, missing-authority, incompatible-version, negative-scope, rollback-failure, and retirement cases, not only a clean adoption path.

The exact approval channels and surface syntax vary by organization and runtime. The durable insight is that setup is a recoverable loop: evidence justifies a control, operation produces new evidence, and that evidence can narrow or remove the control later.

## Decision Tradeoff Guide

Use two independent gates. The **fit gate** asks whether the setup item addresses the observed repository outcome with the right mechanism and evaluator. The **authorization gate** asks whether its invocation, tools, paths, service scopes, data handling, and side effects are allowed. Passing either gate cannot substitute for the other.

| decision_option_name | when_to_choose_condition | required_evidence | safe_fallback_and_tradeoff | revisit_trigger |
| --- | --- | --- | --- | --- |
| No change | Existing commands, documentation, or human process already meet the outcome, or automation cost exceeds recurring value | Baseline workflow, active use, owner confirmation, and comparison with the best setup candidate | Preserves zero new authority and low maintenance but may leave repeated manual cost | Workflow volume, failure rate, ownership, or available capability changes |
| Adopt | Repository need, source scope, surface fit, authorization, cases, rollback, owner, and observed result all align | Active signal, bounded configuration, positive and negative results, permission review, and lifecycle owner | Fastest reuse after evidence, but can preserve stale assumptions if observation stops | Source, runtime, permission, owner, task, evaluator, or failure distribution changes |
| Adapt | The outcome or invariant is valid but syntax, tool, model, event, repository convention, or permission differs | Kept requirement, changed mechanism, explicit design inference, rejected alternatives, and new cases | Preserves intent while adding local maintenance and migration responsibility | Adapted behavior fails, stronger current evidence appears, or upstream support changes |
| Pause for evidence | A material compatibility, owner, permission, data, evaluator, or rollback question is finite and answerable | Exact missing fact, acquisition step, responsible owner, safe interim state, and decision-changing result | Delays adoption while preventing uncertainty from becoming policy | Evidence arrives, deadline or scope changes, or safe collection proves impossible |
| Avoid | The item is unrelated, duplicates stronger setup, conflicts with authority, cannot be evaluated, or requires unavailable capability | Conflict or failure evidence, consequence, rejected repair, and safer alternative | Prevents false confidence but may require manual work or narrower design | Need, authority, capability, or evaluator changes materially |
| Route | Security, service ownership, credential policy, production operations, product support, or incident handling controls the unresolved risk | Destination owner, bounded handoff payload, expected artifact, and return rule | Adds coordination but places the decision under proper authority | Returned artifact resolves the fit or authorization gate |
| Replace | Another surface or maintained bundle provides the same outcome with clearer authority, lower overlap, or stronger lifecycle | Before/after behavior, dependency map, migration plan, compatibility, and rollback | Consolidates control but can break dependents or introduce new ownership | Replacement regressions, source drift, or maintenance failure |
| Retire | Original workflow signal is gone, value no longer exceeds cost, owner is absent, permissions are excessive, or behavior is fully superseded | Usage and failure evidence, dependency and credential inventory, disable or removal test, and owner decision | Reduces invisible policy and maintenance but can remove a rarely used safeguard | Recurrence returns or retirement exposes a missing control |
| Cost of being wrong | Evaluate for every branch, especially automatic, write-capable, shared, credentialed, or external setup | Blast radius, detection delay, unauthorized effects, secrets, duplicate work, rollback, review burden, and trust impact | More evidence costs time; too little evidence shifts cost into diagnosis and recovery | New dependency, scope, user group, side effect, or irreversibility increases consequence |

**Surface tradeoffs.** A manual command has low setup and removal cost but weak discoverability and repeated human effort. Documentation improves shared understanding but cannot enforce behavior. A hook is deterministic and immediate but can block or recurse. A skill packages context and scripts but can hide invocation and side effects. A subagent isolates specialist context but creates fan-in and evaluator questions. A plugin reduces local duplication but adds bundle and update dependency. MCP provides direct service capability but introduces credentials, data flow, external authority, and revocation obligations.

The least-powerful surface is a default, not a dogma. A maintained, inspected plugin may be safer than several improvised hooks and skills. A read-only external integration may have narrower effect than a skill script that writes files. Compare concrete configurations under one outcome, owner, permission model, and evaluator.

**Branch gotchas.** Source agreement does not prove fit. A reversible local trial does not authorize production. Adaptation cannot invent permission. Pause without an owner and movement condition becomes indefinite. Avoid without a fallback transfers the problem. Replacement without dependency review creates breakage. Retirement without credential and state cleanup leaves residual authority. Sunk cost is not evidence for continued adoption.

**Examples.** Adopt a formatter hook after active command and negative matcher evidence. Adapt a local skill when the workflow is sound but current schema differs. Pause an unrefreshed plugin recommendation with an owner and compatibility task. Route database credentials to the service owner. Replace overlapping review agents with one independently evaluated role. Retire a shared integration only after dependents, credentials, and rollback are checked.

**Verification.** Record branch, fit evidence, authorization evidence, rejected alternatives, surface, versions, observed behavior, rollback, owner, residual risk, and revisit trigger. Another reviewer should be able to reach the same branch from the saved record. Include no-change and route cases so the evaluator does not reward automation by default.

The inherited branch vocabulary is useful, but thresholds are local judgment. The second-order decision is portfolio coherence: an individually strong setup item can still be wrong when another control already owns the same outcome or when their combined authority is excessive.

## Local Corpus Hierarchy

The local corpus is a six-lineage evidence set, not twelve independent votes. Each lineage has a current locator under `claude-skills/` and an archived locator under `agents-used-monthly-archive/claude-skills-202603/`. At the time of this evolution, every current/archive pair is byte-identical. That identity establishes provenance and prevents accidental double counting; it does not mean that two copies corroborate a claim, that an archive is obsolete, or that a current path is automatically more authoritative.

Hierarchy is assigned to an atomic claim, not permanently to an entire file. One source can be primary for the workflow it defines, supporting for an example, provisional for a product-specific name, negative for a pattern that violates local constraints, and silent about a permission question it never addresses. This claim-scoped model allows useful material to survive without importing every instruction around it.

**Classification Vocabulary**

| role | operational meaning | evidence needed to assign it | effect on setup decisions |
| --- | --- | --- | --- |
| primary | The source directly defines the local workflow, contract, or owner-approved rule for the exact claim. | Relevant passage, applicable scope, identifiable authority, and no stronger controlling instruction. | May anchor guidance, but still requires compatibility and behavioral verification before implementation. |
| supporting | The source adds an example, rationale, implementation pattern, or warning consistent with a primary claim. | Traceable passage plus a clear connection to the claim being evaluated. | Can refine or illustrate a recommendation; cannot independently grant permission or settle a conflict. |
| provisional | The source offers a plausible claim whose freshness, version, availability, schema, or local fit has not been established. | Direct passage plus an explicit statement of the missing evidence and a way to obtain it. | May motivate a bounded investigation; must not be presented as current fact or enabled by default. |
| negative | The source contains an example or instruction that should not be copied under the current task's constraints. | Specific risk, violated policy, failed case, excessive permission, or contradicted behavior. | Retain as a warning with its cause; exclude it from generated setup and recommendation defaults. |
| duplicate | Two locators resolve to the same content lineage for the relevant version. | Byte identity or an exact semantic comparison, plus provenance linking the copies. | Count the content once. Prefer the operational locator while retaining the archive for provenance. |
| conflicting | Two applicable claims recommend incompatible actions or assign different authority. | Both passages, their versions and owners, and the decision that cannot simultaneously hold. | Freeze dependent adoption until controlling authority, implementation evidence, or an owner resolves the conflict. |
| stale | A claim was once applicable but no longer matches the supported version, implementation, policy, or observed behavior. | Historical applicability plus evidence of the change that invalidated it. | Preserve for migration history and failure prevention; do not use as current setup guidance. |
| superseded | A controlling source intentionally replaced an earlier claim while preserving the same decision domain. | Explicit replacement, owner decision, or versioned migration evidence. | Route new work to the replacement and keep the old claim only for historical traceability. |
| silent | The source does not answer the claim being decided. | Review of the relevant scope showing no applicable statement. | Do not infer approval, rejection, compatibility, or safety from absence. |

`Canonical` is deliberately not used as a blanket file label. It can imply universal authority that the corpus does not possess. A local skill can be primary for how to produce a read-only recommendation report while remaining silent about current marketplace inventory and subordinate to repository security policy.

**Six Content Lineages**

| content lineage and locators | initial claim roles | authority boundary | evidence required before use |
| --- | --- | --- | --- |
| Entry workflow: `claude-skills/plugins/claude-code-setup/SKILL.md`; archive: `agents-used-monthly-archive/claude-skills-202603/plugins/claude-code-setup/SKILL.md` | Primary for the local read-only recommendation workflow, report shape, analysis sequence, and automation taxonomy. Duplicate across the two locators. | It does not establish present Claude Code behavior, prove that an automation improves outcomes, or authorize repository changes. A direct user instruction, repository policy, or security owner can narrow it. | Cite the exact workflow clause, confirm it applies to the requested task, inspect repository evidence, and obtain authorization before changing setup. |
| Hook details: `claude-skills/plugins/claude-code-setup/references/hooks-patterns.md`; archive: `agents-used-monthly-archive/claude-skills-202603/plugins/claude-code-setup/references/hooks-patterns.md` | Supporting for candidate event patterns, formatting examples, and hook-specific risks. Product syntax and event availability are provisional until locally verified. Broad blocking, recursive, or unbounded examples become negative when they violate the task boundary. | A detail file can suggest implementation mechanics but cannot make an automatic action desirable, safe, or permitted. | Verify the installed event schema, matcher behavior, exit semantics, timeout, idempotence, failure visibility, and a disable path in a disposable case. |
| MCP details: `claude-skills/plugins/claude-code-setup/references/mcp-servers.md`; archive: `agents-used-monthly-archive/claude-skills-202603/plugins/claude-code-setup/references/mcp-servers.md` | Supporting for MCP capability categories and configuration concerns. Server names, installation steps, authentication shape, and scope are provisional without a permitted current check. Dependency-match claims and broad credential patterns can be negative. | The file cannot prove that a named server is installed, maintained, compatible, least-privilege, or appropriate for the repository. | Confirm current availability, owner, data boundary, credential scope, tool inventory, failure behavior, and whether a local CLI or existing integration already satisfies the need. |
| Plugin details: `claude-skills/plugins/claude-code-setup/references/plugins-reference.md`; archive: `agents-used-monthly-archive/claude-skills-202603/plugins/claude-code-setup/references/plugins-reference.md` | Supporting for bundle concepts and examples. Package names, marketplace status, contents, and compatibility remain provisional. Opaque bundles or overlapping automations are negative until inspected. | A plugin label does not reveal all skills, hooks, agents, tools, permissions, or lifecycle obligations carried by the bundle. | Inventory the actual installed contents, compare overlap with existing controls, review permissions and triggers, run representative tasks, and identify update and removal owners. |
| Skill details: `claude-skills/plugins/claude-code-setup/references/skills-reference.md`; archive: `agents-used-monthly-archive/claude-skills-202603/plugins/claude-code-setup/references/skills-reference.md` | Supporting for progressive disclosure, packaging, trigger design, and reusable procedure examples. Schema details are provisional. Skills that run unsafe scripts or cause automatic side effects are negative for read-only recommendation work. | A skill can organize guidance but cannot make stale instructions current, replace domain authority, or guarantee that triggering and full-document loading behave as expected. | Validate metadata and path structure with the installed runtime, test intended and non-intended triggers, inspect bundled scripts, and confirm that instructions respect repository and user constraints. |
| Subagent details: `claude-skills/plugins/claude-code-setup/references/subagent-templates.md`; archive: `agents-used-monthly-archive/claude-skills-202603/plugins/claude-code-setup/references/subagent-templates.md` | Supporting for context isolation, role focus, and tool-scope examples. Model names and delegation thresholds are provisional. Shared writes, circular delegation, or self-grading without independent evidence are negative. | A template cannot establish that delegation is cheaper, faster, or safer for a particular task, and it does not create ownership boundaries by itself. | Give each worker a non-overlapping scope, bounded tools, acceptance evidence, and a merge owner; compare output quality and coordination cost against a single-agent baseline. |

The current locator is the default operational path because it is where active setup work would look first. The archive locator is the provenance anchor because it preserves the earlier captured state. While their hashes match, either path yields the same content and should be treated as one source. If a pair later diverges, preserve both versions and compare them; never silently overwrite the difference or assume that directory age settles authority.

**Claim Classification Procedure**

For every recommendation-changing claim:

1. State the claim narrowly enough that it has one subject, one behavior, and one decision consequence. "Hooks are useful" is too broad; "a post-edit formatter hook may reduce unformatted JavaScript changes" can be evaluated.
2. Record the exact source passage, content lineage, locator, version or capture date, and known owner. A heading alone is a discovery signal, not supporting evidence.
3. Separate four dimensions: source content, authority, present compatibility, and local effectiveness. A direct quote can establish content while all three other dimensions remain unresolved.
4. Assign one or more roles for this claim and explain the scope. Mixed classification is expected when an otherwise useful file contains a stale name or unsafe example.
5. Compare controlling instructions in this order: direct user constraint, organization or repository policy, security and data rules, compatible implementation behavior, owner-approved local workflow, then supporting examples. This order is a decision boundary for this reference, not a universal governance model.
6. Link any setup item that depends on the claim. A change to a hook event should identify the matching configuration and cases; it should not automatically reopen unrelated subagent guidance.
7. Record what evidence would promote, narrow, reject, mark stale, or supersede the role. A provisional label with no path to resolution is merely vague.

The procedure should remain proportional. A harmless wording example does not need a governance ledger. A claim that enables shell execution, sends repository data externally, stores credentials, blocks normal work, delegates writes, or installs a bundle does.

**Conflict and Containment**

When two applicable claims conflict, retain both passages and stop the dependent change. Do not settle the conflict by counting files, favoring the longer explanation, selecting the newest-looking path, or choosing the most confident wording. Instead:

1. Identify the exact incompatible actions and the artifacts that would depend on either choice.
2. Check whether one claim has direct authority over the repository, security boundary, supported runtime, or requested outcome.
3. Compare lineage, owner, version, implementation behavior, and representative local cases.
4. Ask the controlling owner when the dispute concerns permission, policy, data exposure, or operational responsibility.
5. Record the resolution, rejected alternative, evidence, and conditions that would reopen it.
6. Reclassify downstream guidance and remove or disable any setup that relied on the losing claim.

Containment is a valid result. For example, if a detail file names a hook event that the installed runtime does not recognize, retain the event name as provisional historical material, leave the hook disabled, and continue with a manual command or existing formatter integration. If a skill recommends browsing but the active task forbids browsing, reject that clause for the task without demoting the skill's unrelated packaging guidance.

**Examples and Boundary Cases**

**Good classification:** The entry workflow explicitly says to inspect a repository before recommending automation and to return a read-only report. Treat that workflow shape as primary for this recommendation task. Treat the hook file's formatter command as supporting mechanics, verify the repository actually uses the formatter, and seek permission before installing an automatic hook.

**Bad classification:** A reviewer sees the word `canonical` beside the archived entry skill, copies every named plugin and MCP server into configuration, and claims the duplicate current files independently confirm the choices. This collapses provenance, product freshness, local fit, permission, and outcome evidence into one label.

**Borderline classification:** A subagent template describes a focused code reviewer and the repository has recurring review work, but no local comparison shows that delegation improves coverage or cost. The role is supporting for isolation design and provisional for adoption. A bounded parallel review with non-overlapping read-only scope, independent findings, and measured coordination cost can promote or reject the adoption claim.

**Mixed-role source:** The skills reference provides a useful progressive-disclosure structure but includes a script with side effects inappropriate for read-only analysis. Preserve the structure as supporting, mark the script negative for this task, and require an explicit implementation review before any future use.

**Silent source:** The plugin reference does not state who owns credentials for an external service. Its silence is neither permission nor rejection. The setup remains paused until repository policy or the responsible owner answers the question.

**Verification and Change Review**

Hierarchy evidence should support both backward and forward traceability:

- Backward trace starts at a recommendation or configuration clause and reaches the exact source passage, role decision, authority, compatibility result, local case, and owner decision.
- Forward trace starts at a changed source claim and reaches every recommendation, configuration, credential, test case, observation, rollback step, and lifecycle record that depends on it.

Automate only the mechanical parts. Hashes can detect identical or diverged copies; path checks can find missing locators; schemas can validate known fields; behavior cases can exercise an adopted configuration. Human review is still required to classify mixed claims, interpret policy authority, and decide whether external access is acceptable. No hash, parser, or classifier should grant permission.

Sample the trace after each material change. A later reviewer should be able to explain why a claim is primary, supporting, provisional, or negative without relying on the original conversation. For high-impact setup, use an independent reviewer and more than one representative task because a clean table and a single passing case can still encode reviewer bias.

**Uncertainty and Role Movement**

Known facts in this corpus include the file paths, inspected wording, heading inventory, and byte identity of each current/archive pair at the recorded review boundary. The corpus does not by itself prove current marketplace availability, supported configuration schemas, maintainer status, universal value, or owner approval. Those are refresh-dependent or judgment-dependent claims.

Roles move when evidence changes:

- Provisional becomes supporting after current compatibility and source purpose are verified.
- Supporting becomes primary only when an applicable authority explicitly adopts the claim for its decision domain.
- Primary narrows when a stronger instruction, policy, or implementation boundary applies.
- Any role becomes stale after incompatible product or policy change.
- A failed local trajectory can make an example negative while leaving its surrounding principle useful.
- A versioned owner decision can supersede an earlier claim without deleting its history.
- Unresolved evidence remains provisional, conflicting, or silent; confidence is not manufactured to fill a table.

This hierarchy is also retrieval policy. Labels influence which files later agents load, which examples they copy, and which risks stay visible. Therefore, failed trajectories should update future retrieval priority, and negative examples should retain their causes. Historical legibility is not archival decoration: it prevents a rejected pattern from silently regaining authority when a later agent rediscovers it.

## Theme Specific Artifact

The operational artifact for this reference is a **Claude Code Setup Decision Record**. It turns a request such as "improve our Claude setup" into one bounded candidate that a repository owner can inspect, authorize, test, disable, and eventually retire. The record is recommendation-only until an authorized person approves implementation. It must not disguise an unverified product name, event, schema field, marketplace package, or credential procedure as current fact.

Start with the unchanged repository. A new control must close an observed gap more effectively than existing scripts, documentation, editor behavior, CI, or team practice. Prefer the least-powerful surface that covers the outcome: explicit instructions before delegated work, delegated work before automatic mutation, and local execution before an external data boundary. This ordering is a risk-sensitive default, not a ban on stronger controls.

**Decision Record Schema**

| artifact field | completion rule | why it is required |
| --- | --- | --- |
| decision identifier and status | Give the record a stable identifier and mark it proposed, paused, rejected, authorized, trialing, adopted, disabled, replaced, or retired. | Separates analysis from permission and makes lifecycle movement observable. |
| user outcome | State the human-visible result in one sentence without naming a preferred automation. | Prevents a tool request from substituting for the actual problem. |
| scope and owner | Name the repository, affected users, workflow boundary, decision owner, implementation owner, and observation owner. | Exposes split authority and avoids ownerless shared setup. |
| observed friction | Record concrete skipped steps, repeated effort, review defects, latency, or confusion, including the observation window. | Establishes that there is a gap worth changing. |
| unchanged baseline | Describe current scripts, CI, documentation, and manual sequence and what happens if setup remains unchanged. | Supplies the counterfactual for later value measurement. |
| local evidence | Cite exact paths, commands, configuration, and representative behavior inspected. | Grounds the candidate in the repository rather than generic feature lists. |
| evidence boundary | Separate local fact, inherited corpus claim, unrefreshed product claim, inference, owner decision, and measured result. | Keeps confidence proportional to evidence freshness and authority. |
| candidate surface | Name the smallest suitable surface and describe its trigger, inputs, outputs, tools, writes, external access, and stop behavior. | Makes authority and context cost reviewable before implementation. |
| credible alternatives | Compare no change and every materially plausible surface; record adopt, adapt, pause, avoid, route, replace, or retire reasons. | Prevents feature count or novelty from deciding the setup. |
| permissions and data boundary | List files, commands, network destinations, secrets, production access, and human approvals the candidate would require. | Turns least privilege into an inspectable contract. |
| overlap and dependencies | Name existing controls that duplicate, call, trigger, or are triggered by the candidate. | Prevents double execution and reveals replacement impact. |
| failure model | For each likely failure, give trigger, observable signal, containment action, recovery, and escalation owner. | Converts warnings into operational response. |
| verification packet | Define source trace, structural checks, intended cases, non-intended cases, forced failure, rollback rehearsal, baseline comparison, and independent review. | Requires evidence across correctness, safety, and usefulness. |
| rollout and rollback | Specify disabled default, trial scope, observation period, enable authority, disable mechanism, and restoration of the prior workflow. | Keeps adoption reversible and limits blast radius. |
| success and removal criteria | Name the outcome measure, acceptable false-trigger or failure level, review date, refresh signal, replacement rule, and retirement condition. | Prevents a once-useful control from becoming permanent by inertia. |
| unresolved questions | Assign every material unknown to an owner, evidence source, and resolution gate. | Makes a pause actionable instead of leaving an ambiguous recommendation. |

Use the full schema for shared, automatic, side-effecting, externally connected, security-sensitive, or difficult-to-remove setup. A reversible personal preference can use a shorter record containing outcome, baseline, candidate, authority, verification, and disable path. Split the record when two candidates cross different ownership, credential, production, or data boundaries.

**Completed Worked Scenario**

The following is an illustrative decision record, not a claim about this repository or the currently installed Claude Code schema.

| field | completed value |
| --- | --- |
| decision identifier and status | `CCR-REVIEW-001`; proposed recommendation only. No configuration or repository file has been authorized for change. |
| user outcome | Contributors should run the repository's established lint, focused test, and change-summary checks consistently before asking for code review. |
| scope and owner | One TypeScript repository; contributors invoking the procedure; repository maintainer owns approval; a designated tooling maintainer would own implementation and observation. |
| observed friction | In the scenario's last ten review handoffs, contributors used inconsistent command sequences and three handoffs omitted either lint or focused tests. This is scenario data for demonstrating the artifact, not measured corpus evidence. |
| unchanged baseline | Contributors read package scripts and run checks manually. CI eventually catches some omissions, but feedback is delayed and the review handoff lacks a uniform evidence summary. |
| local evidence | The hypothetical repository exposes `pnpm lint`, `pnpm test -- <affected-test>`, and `pnpm format:check`; contributor guidance requires changed-file and test evidence. Exact commands must be re-read from the real target repository before use. |
| evidence boundary | The procedure shape comes from the inspected local setup corpus. Command names and omission counts belong only to this scenario. Present skill metadata and invocation behavior are unverified until checked against the installed environment. Expected reduction in missed checks is an inference awaiting a trial. |
| candidate surface | A repository-scoped, user-invoked review skill containing the existing command-selection procedure and a compact evidence report. It receives the user's review request and changed-file context, reads relevant repository guidance, proposes or runs only approved local checks, writes no source files, uses no network service, and stops on command failure or an unresolved destructive step. |
| trigger contract | Explicit contributor invocation for review preparation. Ordinary editing, commits, pushes, and unrelated questions must not activate it. If trigger discrimination cannot be established, keep the procedure as plain documentation. |
| output contract | Changed-file summary, checks selected with reasons, summarized command outcomes, skipped checks with reasons, unresolved risks, and an explicit statement that no commit or push occurred. |
| permissions | Read repository instructions and diffs; execute only repository-approved read-only or test commands after user authorization under local command policy. No credential access, network calls, production environment, source mutation, commit, or push. |
| overlap and dependencies | Reuses package scripts and contributor policy as sources of truth. It does not replace CI, formatter configuration, test ownership, code review, or security approval. It must not duplicate an equivalent maintained skill already present. |

**Alternatives Ledger**

| option | decision | decisive evidence and tradeoff |
| --- | --- | --- |
| No setup change | Adapt as fallback | Safest and maintenance-free, but the scenario shows repeated omission. Improve contributor documentation first if a reusable procedure cannot trigger predictably. |
| Plain checklist in repository guidance | Viable simpler alternative | Lowest runtime and permission cost. Prefer it when the sequence is short, rarely changes, and contributors reliably follow it without contextual command selection. |
| User-invoked review skill | Recommend for bounded trial | Reuses current commands, packages a multi-step procedure, and preserves explicit invocation. It adds trigger, instruction-drift, and maintenance obligations that must be tested. |
| Focused review subagent | Route only for broad independent review | Useful when isolated analysis or parallel issue classes materially improve coverage. Excessive for merely sequencing three local checks and more costly to coordinate. |
| Automatic post-edit or pre-action hook | Pause | Could enforce consistency, but it introduces automatic execution, latency, reentrancy, and failure-blocking risk. The relevant event schema and repository approval are not established in this scenario. |
| Plugin bundle | Avoid absent inventory | Bundle contents, overlap, version, and permissions are unknown; installing multiple controls to obtain one procedure expands maintenance and authority without evidence. |
| MCP integration | Avoid | The outcome uses local repository evidence and commands; no external capability or data boundary is needed. |

**Failure, Detection, and Recovery**

| failure | detection signal | containment and recovery |
| --- | --- | --- |
| Skill activates for unrelated work | Non-review prompts select the procedure in negative trigger cases. | Disable the skill, narrow its trigger description, rerun negative cases, or retain the workflow as plain documentation. |
| Procedure invokes a stale command | Package scripts or repository guidance no longer match the recorded sequence; command reports missing target. | Stop execution, re-read current repository contracts, update the candidate under review, and do not guess replacement commands. |
| A check mutates source unexpectedly | Clean-worktree snapshot differs after a command classified as read-only. | Stop subsequent commands, preserve the diff for inspection, restore only with owner approval, and reclassify the command's authority. |
| A failed check is hidden by the summary | Raw exit status is nonzero while the report claims success or omits the failure. | Mark the run failed, expose the command and concise error, repair output handling, and add a forced-failure case. |
| Contributors trust the skill instead of CI or review | Handoff language treats the summary as final approval. | Add an explicit boundary to output, retain CI and human review, and evaluate misuse during the trial. |
| Equivalent setup already exists | Inventory finds another skill, script, or plugin owning the same sequence. | Prefer the maintained owner, reconcile useful differences, and reject or retire the duplicate candidate. |
| Maintainer becomes unavailable | Refresh date passes or failures have no responding owner. | Disable shared invocation, route users to repository-native commands, and assign or retire the control before reenabling it. |

**Verification Packet**

Before authorization, a reviewer should be able to replay these checks:

1. Trace every command and instruction to current repository files; label scenario-only and unrefreshed product claims.
2. Confirm the candidate's metadata and location against the installed runtime without assuming the archived schema remains current.
3. Run positive cases for an ordinary source change, a focused test selection, and a documentation-only change where some checks may be intentionally skipped.
4. Run negative trigger cases for editing, casual questions, commit requests, and unrelated planning; the candidate must remain inactive.
5. Force lint failure, test failure, missing command, timeout, and unexpected dirty-worktree conditions; each must stop safely and remain visible.
6. Disable or remove the candidate and confirm contributors can return immediately to the documented native command sequence.
7. Compare a bounded sample against the unchanged baseline: missed required checks, unnecessary command runs, contributor effort, reviewer clarification time, false triggers, hidden failures, and maintenance interventions.
8. Obtain repository-owner approval for the final authority contract and an independent reviewer verdict on the saved evidence.

Passing one happy path is insufficient. The candidate passes trial only when intended invocation is predictable, non-intended activation is absent in the agreed sample, failures remain visible, no unapproved mutation or external access occurs, rollback restores the baseline, and the owner judges the review evidence more consistent at acceptable cost. Exact thresholds belong to the repository and must be set before the trial rather than inferred from this example.

**Rollout and Lifecycle**

Keep the candidate disabled until compatibility, cases, rollback, and permission gates pass. Trial it with one repository and a small contributor group for a fixed period. Save aggregate outcomes, not raw conversational transcripts or unnecessary source content. At the review boundary, adopt, adapt, pause, reject, or route based on evidence.

Refresh the record when repository scripts, contributor policy, skill runtime behavior, ownership, or the candidate's dependencies change. Disable it immediately after unexplained mutation, external access, concealed failure, repeated false activation, or owner loss. Retire it when the workflow disappears, a repository-native control covers the outcome more directly, or maintenance cost exceeds measured benefit. Preserve the concise decision history so the same rejected automation is not repeatedly rediscovered without its earlier evidence.

The completed record is also an authorization interface. Approval should name the exact candidate, scope, permissions, evaluator, and trial boundary. Approval of the general goal does not authorize a plugin installation, automatic hook, external connection, commit, push, or any other unlisted action.

## Worked Example Set

These examples calibrate setup decisions; they are not current installation instructions. Every case is hypothetical. Keep the user outcome fixed within each set and compare the evidence, authority, trigger, failure handling, and lifecycle state. A good result is not necessarily adoption: choosing no change or routing to a domain owner can be the best setup decision.

Use these classifications:

| classification | required state |
| --- | --- |
| good | The recommendation is grounded in current local evidence, uses proportionate authority, exposes uncertainty, has approval appropriate to its effect, and includes replayable behavior, failure, rollback, and lifecycle evidence. |
| bad | The action crosses a material evidence, authority, data, behavior, or recovery gate. Formatting quality and confident language do not repair the missing control. |
| borderline | The candidate remains disabled or otherwise contained, the unresolved fact can change the decision, a named evaluator can resolve it, and a safe interim workflow exists. |

**Set 1: Repeated Review Preparation**

User outcome: contributors should present consistent lint, test, and change-summary evidence before review.

| case | reasoning and action | classification evidence |
| --- | --- | --- |
| Existing contributor guidance and CI already produce consistent handoffs; a sample finds no repeated omission or costly clarification. The reviewer records the baseline and recommends no setup change. | New instructions would duplicate maintained controls and add another drift point without an observed gap. Revisit only if omission or review-delay evidence appears. | Good: no change is an explicit decision, local controls were inspected, and the refresh trigger is visible. |
| A generic guide says skills improve consistency, so the reviewer creates a repository skill that invents command names and describes passing output without running or tracing any checks. | The surface label replaces repository evidence. The new procedure can mislead contributors and compete with CI. Remove it and return to current guidance. | Bad: unsupported commands, fabricated evidence, duplicate authority, and no failure path. |
| The repository has repeated omissions and suitable native commands, but current skill metadata and trigger behavior have not been verified. | Save a recommendation-only decision record, use a plain checklist as the interim behavior, and keep the skill candidate disabled until structural and positive/negative trigger cases pass. | Borderline: fit evidence exists, compatibility does not, and one bounded verification packet can move the case. |

Replay question: if the trigger check fails, does the recommendation safely fall back to documentation, or does the workflow remain dependent on an unavailable skill?

**Set 2: Automatic Formatting**

User outcome: source changes should satisfy the repository's established formatter without creating surprise mutations or blocking unrelated work.

| case | reasoning and action | classification evidence |
| --- | --- | --- |
| The repository owner requires deterministic formatting, an existing formatter command is authoritative, automatic execution is approved, and the installed environment confirms the selected event. A disabled trial proves matcher scope, idempotence, bounded runtime, visible failure, no recursive activation, and one-step disable. | Adopt the hook for the proven file scope, retain CI as independent enforcement, observe latency and false activation, and assign an owner for command or event drift. | Good: automatic authority is justified by the invariant and backed by compatibility, failure, recovery, and owner evidence. |
| A reviewer copies a JavaScript formatter example into an unknown project, uses an unverified event name, applies it to every file, and treats a clean happy path as completion. | The hook can mutate generated or unsupported files, trigger recursively, conceal nonexecution, or block work. Disable it and inspect the actual repository and runtime before any retry. | Bad: generic command, broad matcher, unknown trigger, no negative cases, and no rollback rehearsal. |
| The formatter and policy are clear, but the available event, timeout semantics, or failure-blocking behavior remains unrefreshed. | Continue with the native formatter command and CI, preserve the hook as a paused candidate, and assign compatibility checks in a disposable worktree. | Borderline: the desired invariant is real, but automation mechanics could change safety; manual enforcement preserves work meanwhile. |

Replay question: which evidence proves that the hook ran exactly when intended, rather than merely proving that one file happened to be formatted?

**Set 3: Isolated Migration Review**

User outcome: a broad dependency migration should receive focused analysis without parallel workers overwriting each other's conclusions or files.

| case | reasoning and action | classification evidence |
| --- | --- | --- |
| The migration has separable dependency, test-impact, and data-contract questions. Three read-only subagents receive non-overlapping scopes, bounded source sets, identical evidence labels, and one merge owner; each returns findings and uncertainty rather than edits. A sample shows additional issue coverage at acceptable coordination cost. | Adopt isolated analysis for similarly shaped migrations, keep implementation under one owner, and compare future coverage and merge effort against a single-agent baseline. | Good: delegation follows real separability, shared writes are excluded, and value plus cost are observed. |
| Three agents are told to "fix the migration" in the same checkout, all may edit shared manifests, and each self-reports completion without an independent build or merge review. | Conflicting writes and implicit decisions make provenance unrecoverable. Stop workers, preserve their findings separately, restore single ownership, and rerun verification after reconciliation. | Bad: overlapping authority, shared state, no deterministic merge, and self-grading as evidence. |
| The questions appear separable, but the repository is small enough that delegation overhead may exceed analysis value. | Run one bounded read-only comparison: a single reviewer versus two focused analyses on the same frozen revision. Keep one implementation owner regardless of outcome. | Borderline: safety is contained, and measured coverage, latency, and reconciliation effort can decide future routing. |

Replay question: does the subagent boundary follow independent evidence domains, or was delegation chosen merely because parallelism is available?

**Set 4: Plugin Bundle Adoption**

User outcome: the team wants a maintained set of related review controls without duplicating its current hooks, skills, or agents.

| case | reasoning and action | classification evidence |
| --- | --- | --- |
| The reviewer inspects the exact compatible bundle contents, versions, triggers, tools, permissions, update channel, and removal behavior. The owner maps each bundled component against current controls, rejects unneeded capabilities, replaces only true duplicates, and runs representative workflows plus rollback. | Trial the reduced authorized bundle with one owner and an inventory record; adopt only the components whose outcomes and failure paths remain observable. | Good: the decision concerns inspected contents rather than the plugin label, and portfolio effects are reconciled. |
| A package name looks official and advertises code quality, so the reviewer installs it without reading its manifest or discovering that it adds an automatic hook and an external integration overlapping local controls. | Disable and remove the bundle, rotate or revoke any unnecessary credentials, inspect changed files, and restore the prior portfolio before reconsideration. | Bad: brand inference, hidden authority, overlap, data-boundary expansion, and untested removal. |
| The bundle appears relevant in an archived reference, but current availability, included surfaces, and supported version are unknown. | Do not install it. First obtain a permitted current inventory and compare that inventory to the local control map; continue with existing individual controls meanwhile. | Borderline: the package claim is provisional, the setup is contained, and inventory evidence can resolve fit. |

Replay question: can a reviewer name every behavior and permission being adopted, or is the bundle still functioning as an opaque unit of trust?

**Set 5: External Issue Context Through MCP**

User outcome: an agent reviewing a change needs authoritative issue acceptance criteria while respecting repository and service data boundaries.

| case | reasoning and action | classification evidence |
| --- | --- | --- |
| Repeated tasks require issue lookup, the service owner approves access, the exact server and tools are current and compatible, credentials are read-only and narrowly scoped, repository content sent externally is prohibited, and audit plus revocation paths are tested in a non-production boundary. | Trial only issue-read operations, expose source identifiers in outputs, stop on authorization or service failure, and retain a manual issue-link workflow. | Good: external capability is necessary, data and credentials are bounded, and loss of service degrades safely. |
| A dependency appears in the repository, so the reviewer assumes a matching MCP server is needed and grants broad workspace credentials to every agent. Tool inventory, outbound data, and revocation are not inspected. | Revoke access, audit calls and data, remove the configuration, and route the question to the service and security owners. | Bad: dependency matching is not need evidence, and the credential plus data boundary is unjustified. |
| Only one short task needs two acceptance criteria, and the service owner has not approved an integration. | Use user-provided, source-labeled issue text or a permitted manual lookup. Keep MCP adoption paused unless recurrence and ownership justify its standing cost. | Borderline: a lower-authority interim route meets the immediate outcome while integration value and permission remain unresolved. |

Replay question: does the task require a persistent external capability, or can explicit bounded context satisfy it with less credential and maintenance cost?

**Set 6: Production and Security Operations**

User outcome: a contributor asks Claude Code setup to automate a production deployment approval or security exception workflow.

| case | reasoning and action | classification evidence |
| --- | --- | --- |
| The setup reviewer identifies that production authorization, secret handling, and compliance ownership exceed this reference. It records the requested outcome and evidence already gathered, makes no configuration change, and routes to the deployment or security owner and their specialized controls. | Resume setup analysis only after the controlling domain defines permitted actions, audit, evaluator, failure containment, and human review points. | Good: routing preserves evidence while respecting authority; refusal to automate is an operational decision. |
| The reviewer treats a shell-capable hook or agent as a convenient deployment wrapper, embeds credentials, and calls a successful non-production command sufficient verification. | Disable the control, contain credentials, audit effects, and follow the owning incident or security process. Do not reuse the generic setup example as a production design. | Bad: capability availability is mistaken for authorization and the verification boundary does not match the consequence. |
| The request concerns only generating a read-only deployment checklist, but some items encode organization policy that the repository does not contain. | Draft a source-labeled outline without asserting missing policy, assign the unknown clauses to the deployment owner, and prohibit execution until the completed artifact is approved. | Borderline: a low-authority artifact is possible, but policy silence must remain visible and actionable. |

Replay question: which part is ordinary agent setup, and at what exact clause does a domain owner become the only valid authority?

**How to Use and Verify the Set**

For a proposed recommendation, select the closest case by outcome rather than by product noun. Then answer:

1. What local fact establishes the gap?
2. What is the unchanged baseline and safe interim behavior?
3. Why is this surface the least authority that covers the outcome?
4. Which direct permission applies to its files, commands, data, and external effects?
5. What positive, negative, forced-failure, and rollback evidence exists?
6. Who owns observation, refresh, disablement, replacement, and retirement?
7. What single missing fact keeps a borderline case from moving?

Have a second reviewer classify a sample of decisions without seeing the original label. Disagreement should trigger a boundary review, not a vote based on confidence. Capture which variable caused the difference: evidence freshness, surface fit, permission, behavior, recovery, or ownership. Use failed real trajectories to add or revise cases, but keep stable decision invariants separate from versioned product details.

A confidence warning alone never converts a bad case into a borderline one. Borderline means the risky action is contained, the resolution path is owned, and useful work can continue safely while evidence is gathered.

## Outcome Metrics and Feedback Loops

Measure whether a setup item improves its stated human outcome without exceeding authority, hiding failure, increasing total workflow cost, or becoming ownerless. Installation, invocation, tool-call volume, and generated text are activities, not outcomes. A setup item can be frequently used and still be the wrong control.

The default measurement sequence is:

1. Freeze the setup version and describe the unchanged workflow.
2. Select one primary outcome, several non-negotiable guardrails, and a small number of cost and reliability measures.
3. Record a baseline from comparable tasks when feasible; otherwise label the baseline weak and use paired review plus conservative rollout.
4. Trial one item in one bounded scope with a named observation owner and review date.
5. Include intended, non-intended, failed, skipped, and disabled opportunities in the denominator.
6. Compare like-for-like tasks and state confounders such as simultaneous CI, policy, staffing, or repository changes.
7. Adopt, adapt, pause, disable, replace, retire, or collect a predefined next tranche of evidence.

Do not invent universal targets from this reference. Repositories should set thresholds from consequence, baseline variation, task frequency, and owner tolerance before seeing trial results. Percentiles are useful only when enough comparable observations exist to make their tails meaningful; sparse workflows need case review instead.

**Metric Portfolio**

| evidence class | candidate measure and denominator | interpretation boundary | action it can support |
| --- | --- | --- | --- |
| Primary outcome | The task-specific result named in the decision record, such as required review checks completed per eligible handoff, supported acceptance criteria recovered per issue-driven task, or independently confirmed issue classes per broad review. | Choose one outcome that represents user value. A proxy such as invocation count cannot replace it. | Expand, preserve, narrow, or reject the candidate based on baseline-relative outcome and confidence. |
| Clarification load | Clarification requests caused by missing procedure, ambiguous output, or unsupported claims per comparable completed task. | Fewer questions can mean better context, concealed uncertainty, or disengaged users; sample semantic quality before interpreting a decrease. | Adapt instructions, context selection, output contract, or routing. |
| Evidence support | Recommendation or output claims with traceable source and verification status divided by claims requiring evidence. | Style and citations do not establish authority or applicability. Sample whether links and local paths actually support the claim. | Repair evidence boundaries, mark provisional claims, or stop reuse. |
| Trigger precision | Correct activations per expected activation opportunity and unwanted activations per non-intended opportunity. Also record expected events where the control did not run. | Execution logs alone miss silent non-invocation; negative prompts or events are part of the sample. | Narrow triggers, change invocation mode, return to explicit documentation, or disable. |
| Behavioral reliability | Successful contract-compliant runs per invocation, categorized by normal completion, expected stop, command failure, timeout, and partial result. | Retried runs must not be counted as independent successes, and a produced artifact can still violate its contract. | Repair handling, reduce scope, adjust timeout, or suspend rollout. |
| Safety guardrails | Unauthorized writes, commands, external calls, credential use, production effects, concealed failures, and unrecoverable mutations. | These are hard events, not weighted productivity metrics. One material occurrence can require immediate containment. | Disable, revoke, restore, audit, escalate, and reauthorize only after corrective evidence. |
| Recovery quality | Successful disable or rollback rehearsals, time and steps to restore the native workflow, and residual changed state. | A documented command is not a recovery path until it is safely exercised at the appropriate boundary. | Keep, simplify, or reject rollout; improve restoration and owner readiness. |
| Workflow cost | Contributor time, reviewer clarification time, command runtime, waiting time, context loaded, tool calls, delegated tasks, and reconciliation effort per comparable outcome. | Lower agent latency can shift work to reviewers or maintainers. Report total relevant cost and avoid billing precision unsupported by actual data. | Choose a smaller surface, reduce context, consolidate controls, or accept cost for higher-value outcomes. |
| False work | Unnecessary commands, duplicate checks, duplicate agent findings, repeated context loading, and setup-generated changes later discarded. | Some redundancy is intentional independent verification; classify it rather than treating every duplicate as waste. | Remove overlap, revise routing, or preserve deliberate defense in depth. |
| Maintenance burden | Updates, compatibility repairs, permission reviews, false-trigger investigations, credential rotations, and owner interventions per setup version and period. | A quiet month may mean stability or non-use; pair maintenance with eligible opportunities and lifecycle state. | Replace a bundle with a smaller control, assign ownership, or retire. |
| User and reviewer judgment | Structured verdict on usefulness, trust, output clarity, interruption, and whether the control changed the correct next action. | Satisfaction can reward polished but inaccurate output. Review a sample against objective contracts. | Refine ergonomics, surface uncertainty, or challenge a misleading quantitative trend. |
| Portfolio health | Number of overlapping triggers, duplicated outcomes, shared credentials, circular dependencies, and setup items without active owners. | A single item can be healthy while the combined portfolio creates excessive authority or maintenance. | Consolidate, sequence, replace, isolate, or retire adjacent controls. |

**Guardrail Precedence**

Convenience gains do not compensate for unauthorized behavior. Unless a controlling policy defines a stricter response, immediately contain and review:

- an external call or data transfer outside the approved boundary;
- secret access broader than the declared credential contract;
- an unapproved commit, push, deployment, production mutation, or destructive command;
- source mutation by a control classified as read-only;
- failure or non-execution hidden behind a success report;
- rollback that cannot restore the agreed baseline; or
- shared automatic behavior with no responsible owner.

Containment means stopping new invocations, disabling the item where safe, preserving a minimal audit record, restoring state under the appropriate owner, and invoking the repository's security or incident process when relevant. It does not mean repeatedly retrying until the metric turns green.

**Measurement Methods and Tradeoffs**

| method | strength | blind spot | appropriate use |
| --- | --- | --- | --- |
| Minimal command and trigger counters | Low-cost evidence of opportunities, activation, exit status, and runtime. | Cannot determine semantic correctness, authority, or user value. | Recurring local commands and automatic triggers, with privacy-minimal metadata. |
| Sampled artifact review | Tests whether outputs preserve source boundaries, uncertainty, next actions, and contract fields. | Reviewer judgment can vary and sampling can miss rare cases. | Skills, subagents, decision records, and generated guidance. |
| Paired baseline tasks | Improves attribution by comparing the same task class with and without the candidate. | Learning, order, and novelty effects can distort results. | Bounded trials where replay or comparable tasks are available. |
| Limited canary rollout | Reveals real workflow fit while restricting affected users and repositories. | Short windows underrepresent rare failures and maintenance drift. | Shared hooks, skills, subagents, or bundles after static and forced-failure gates. |
| Structured user or reviewer interview | Exposes interruption, trust, hidden correction work, and unclear outputs. | Memory and preference bias can conflict with actual behavior. | Small samples and cases where workflow cost is largely cognitive. |
| Longitudinal lifecycle record | Captures compatibility repairs, owner interventions, replacements, and retirement pressure. | Slow feedback can leave a harmful control active if guardrails are weak. | Adopted shared setup with explicit periodic and event-driven review. |

Collect the least sensitive evidence that can change the decision. Prefer aggregate counts, source identifiers, concise command outcomes, decision labels, and redacted risk notes over raw prompts, full transcripts, credentials, or source dumps. Monitoring itself requires approval when it captures user or external-service data.

**Data Quality Checks**

Before interpreting a trend, ask:

- Does the denominator include failures, skipped opportunities, expected triggers that did not fire, and disabled periods?
- Are retried attempts deduplicated into one workflow outcome?
- Did task difficulty, repository size, contributor experience, setup version, or other controls change?
- Did the automation move work to a reviewer, tooling maintainer, service owner, or incident responder outside the measured boundary?
- Does sampled semantic quality agree with activity data and user experience?
- Is the observation window long enough for the decision being made, without extending a weak trial indefinitely?
- Could a favorable number be produced by non-invocation, narrower task selection, concealed uncertainty, or users avoiding the control?

Record plausible alternative explanations. Imperfect data can justify a bounded adaptation or pause, but the confidence of the action must match the confidence of the evidence.

**Feedback Loop**

| step | required action | saved evidence |
| --- | --- | --- |
| Observe | Collect the declared outcome, guardrail, cost, reliability, and lifecycle signals for the frozen version. | Version, task class, opportunities, outcomes, failures, and observation boundary. |
| Classify | Distinguish trigger, instruction, command, compatibility, permission, external service, overlap, ownership, and measurement failures. | Failure class and why an ordinary retry would or would not help. |
| Contain | Stop expansion and disable or isolate material red behavior before diagnosis continues. | Time, affected scope, residual state, responsible owner, and safe interim workflow. |
| Diagnose | Trace from signal to source claim, configuration, dependency, behavior case, and authority decision. | Reproduction, competing explanations, and evidence boundary. |
| Change | Narrow, repair, reroute, replace, remove, or update the candidate and its dependent guidance. | Exact changed item, rejected alternatives, and expected effect. |
| Verify | Rerun structural, positive, negative, forced-failure, rollback, and outcome checks proportionate to the change. | Command or review summaries plus remaining uncertainty. |
| Learn | Add durable negative examples, routing rules, source-role changes, or evaluation cases only when evidence warrants generalization. | Scope of lesson, version dependence, and overturn condition. |
| Revisit | Review on the next date or event and decide whether continued ownership still repays its cost. | Adopt, adapt, pause, disable, replace, retire, or next bounded evidence request. |

Review is event-driven as well as periodic. Reopen the record after a product or schema change, repository command or policy change, credential or owner change, guardrail event, repeated false activation, unexplained non-invocation, dependency replacement, setup overlap, or failed rollback. Rerun the reference's static verifier after reference edits, but do not mistake document validity for behavioral value.

**Illustrative Lifecycle Decisions**

Good trial: in a declared sample of comparable review handoffs, required-check omissions decrease, false activations are absent in the sampled negative opportunities, failures remain visible, rollback succeeds, reviewer correction does not increase, and the owner accepts maintenance cost. The evidence supports a bounded adoption, not a universal claim.

Bad dashboard: a team reports hundreds of skill invocations and shorter average runtime but excludes failed runs, cannot count expected triggers that did not fire, stores no semantic sample, and ignores reviewer cleanup. The data cannot establish value; pause expansion and repair the evaluator.

Borderline trial: an explicit review procedure appears to reduce omissions, but the sample is small and CI changed during the same period. Keep the rollout narrow, compare a new tranche under the stable CI version, and set the decision rule before collecting it. Do not repeatedly extend observation merely to obtain a preferred result.

Guardrail override: an external integration saves reviewer time but makes one unapproved data transfer. Disable and audit it regardless of the favorable timing result. Any future trial requires corrected scope, owner approval, revocation evidence, and a regression case for the escaped path.

The inherited candidates "fewer clarifications" and "fewer unverifiable claims" can be useful leading signals, but they are not self-interpreting. A clarification decrease may indicate better context or concealed uncertainty. A claim-support increase may reflect more citations without better applicability. Validate both against the primary outcome, semantic samples, and guardrails.

Finally, feed only durable lessons back into this reference. A recurring trigger failure can refine skill guidance; a high-consequence credential escape can become a negative MCP case; sustained bundle maintenance can justify portfolio consolidation. Keep one-off product details in versioned local records. This preserves general decision quality without teaching future agents to overfit one repository's temporary conditions.

## Completeness Checklist

Completeness is a point-in-time permission boundary, not a claim that setup is permanently correct. Define the target state before running the checklist. A recommendation can be complete while implementation remains blocked, and a no-change decision can be complete when it is supported by evidence and a revisit trigger. Conversely, a syntactically valid enabled control is incomplete if its authority, failure behavior, or owner is unresolved.

Use these statuses for each gate: `not applicable`, `unmet`, `blocked`, `failed`, `passed`, or `passed with bounded uncertainty`. A `not applicable` decision needs a scope reason. `Passed with bounded uncertainty` is valid only when the risky behavior remains contained and the record identifies the evidence and owner that can resolve it. Do not calculate a composite score; one material failed gate can block progression.

**Target Completion States**

| target state | minimum claim that may be made | action that remains prohibited |
| --- | --- | --- |
| Analysis complete | The repository, user outcome, baseline, evidence boundaries, candidate surfaces, and adjacent routes were assessed. | Claiming that a candidate is authorized, compatible, effective, or safe. |
| No-change decision complete | Current controls cover the outcome or the gap does not repay added setup; evidence and a revisit signal are recorded. | Installing a convenience control outside the decision. |
| Recommendation complete | One bounded candidate, alternatives, authority needs, verification plan, rollback, owner, and unresolved questions are reviewable. | Implementing, installing, connecting, or enabling without separate authorization. |
| Trial ready | Exact configuration or artifact, compatible environment, permission, positive and negative cases, forced-failure behavior, disable path, baseline, evaluator, and scope are accepted. | Expanding beyond the approved canary, users, repository, tools, or data boundary. |
| Adopted | Trial evidence meets the predeclared outcome and guardrail decision, residual uncertainty is accepted by the owner, and maintenance plus retirement duties are assigned. | Treating adoption as permanent or silently increasing authority. |
| Disabled or blocked | Risky behavior is contained, the native fallback works, and the resolution or escalation owner is named. | Repeated retries, partial reenablement, or describing the control as operational. |
| Replaced or retired | Dependents are migrated or removed, credentials and automatic triggers are revoked, restoration is verified, and concise decision history remains. | Leaving duplicate execution, orphaned configuration, or an ambiguous active owner. |

**Core Evidence Contract**

| gate | pass evidence | common incomplete state |
| --- | --- | --- |
| User and outcome | Named user, starting workflow, observable friction, desired result, consequence of error, and task trigger. | A request for a tool or feature with no human outcome. |
| Scope and ownership | Repository and user scope, decision owner, implementation owner, observation owner, escalation owner, and affected ownership boundaries. | "The team" owns the setup, or one reviewer implicitly approves another domain. |
| Unchanged baseline | Existing scripts, guidance, CI, editor behavior, integrations, and measured or sampled behavior are recorded. | New setup is evaluated without its no-change counterfactual. |
| Local source trace | Every recommendation-changing local claim reaches an exact path and passage; duplicate lineages are counted once. | A source heading or confident summary substitutes for the supporting passage. |
| External and freshness boundary | Public claims are either refreshed under the task's rules or explicitly marked unrefreshed; versions and dates are attached where drift matters. | Archived product names or schema examples are asserted as current. |
| Inference and uncertainty | Local fact, external fact, inherited claim, inference, owner decision, and measured outcome are distinguishable. Each material unknown has an overturn condition. | A confidence warning appears, but no action remains contained and no evaluator is assigned. |
| Surface decision | No change, hook, skill, subagent, plugin, MCP, or adjacent route is chosen from outcome, trigger, context, authority, data, overlap, recovery, and maintenance evidence. | Feature availability or novelty chooses the surface. |
| Alternatives | Credible options include no change and the safest interim behavior; rejected and paused reasons are recorded. | The candidate is presented as inevitable because no alternatives were inspected. |
| Authority contract | Allowed files, commands, writes, tools, network destinations, credentials, production effects, and human approvals are explicit. | General approval of the outcome is treated as permission for every implementation action. |
| Overlap and dependency map | Existing controls with the same outcome, trigger, command, data source, credential, or owner are reconciled; downstream dependents are listed. | Two controls run independently because each looked reasonable in isolation. |
| Artifact completeness | The setup decision record contains status, evidence, candidate, failure model, verification packet, rollout, rollback, measures, owners, and lifecycle triggers. | A recommendation requires the original conversation to understand its boundaries. |
| Verification design | Structural, source, positive, non-intended, forced-failure, rollback, outcome, and independent-review evidence is specified proportionately. | One happy-path command or a document validator is called end-to-end proof. |
| Safe fallback | Users can continue through a documented repository-native or manual workflow while the candidate is absent, paused, or disabled. | Failure of the setup blocks the only known route to complete ordinary work. |
| Outcome and guardrails | Baseline, primary measure, denominators, hard guardrails, trial scope, observation period, and decision rule are declared before results. | Invocation count, generated output, or installation is reported as value. |
| Lifecycle | Refresh events, review date, compatibility owner, disable condition, replacement rule, retirement condition, and retention boundary are recorded. | A control remains enabled after owner loss or dependency drift because it once passed. |
| Adjacent routing | Clauses outside generic setup authority are handed to the relevant context, verification, security, production, service, or architecture owner with current evidence preserved. | The reference stretches to answer a specialist question it cannot authorize. |

**Conditional Surface Gates**

Apply only the rows for candidate surfaces, but document why every excluded surface was not material to the outcome.

| surface | additional required evidence before trial |
| --- | --- |
| Hook | Installed event and matcher semantics; exact command source; invocation opportunity; idempotence; recursion prevention; timeout; visible exit behavior; mutation boundary; latency; disable mechanism; manual fallback. |
| Skill | Current metadata and location; intended and non-intended trigger cases; progressive-disclosure behavior; bundled scripts and references; allowed tools; command authorization; output contract; instruction-drift owner. |
| Subagent | Separable task boundary; non-overlapping tool and write authority; frozen input revision; context budget; result schema; stop condition; merge owner; independent verification; coordination-cost comparison. |
| Plugin | Exact compatible package and version; full component inventory; triggers; tools; permissions; external services; overlap map; update channel; maintainer; migration behavior; component and whole-bundle removal. |
| MCP | Current server and tool inventory; owner; transport and authentication shape; least-privilege credentials; outbound and inbound data boundary; audit; timeout and partial failure; revocation; local fallback. |
| Automatic or shared setup | Controlling owner approval; canary scope; guardrail monitoring; disable authority; notification and support route; no single maintainer dependency. |
| Production, secrets, compliance, or security effect | Acceptance from the controlling domain process and owner; generic setup review cannot self-certify this gate. |

**Phase Transition Rules**

Analysis may end in no change, recommendation, pause, rejection, or adjacent routing. It does not have to produce an automation. Recommendation moves to trial readiness only after compatibility and authority are established for the exact saved candidate. Trial moves to adoption only after the predeclared outcome and guardrail review. Adoption can move backward to disabled or blocked after drift or failure. Replacement and retirement require downstream cleanup, not merely a changed label.

Block progression when any of these remain unresolved:

- permission for file mutation, external access, credentials, production action, or shared automatic behavior;
- a source conflict that changes the recommended action;
- compatibility of the chosen trigger, schema, package, server, or tool;
- detection of non-execution, partial failure, or hidden error;
- a safe disable and repository-native fallback;
- an owner for observation, maintenance, escalation, and retirement; or
- a material contradiction between the decision record, configuration, tests, and lifecycle state.

Ordinary uncertainty can remain in a complete recommendation when the candidate is disabled, the unknown is explicit, the next evidence is owned, and users retain a safe path. A blocked state with these properties is more complete than an enabled candidate whose uncertainty is concealed.

**Invalid Completion Patterns**

- All headings and tables validate, but the automatic behavior has never been observed or forced to fail.
- The artifact cites a current path whose content is byte-identical to an archive and counts the two locators as independent support.
- A product-specific name is copied from the corpus without a permitted current compatibility check.
- A trial reports only successful invocations and omits expected triggers that did not run, negative opportunities, retries, and disabled periods.
- Rollback is a prose command that has not restored the relevant baseline safely.
- A permission field says "approved" but does not identify who approved which files, commands, data, or scope.
- A `not applicable` label removes the difficult gate without explaining why the candidate cannot cross that boundary.
- An adopted control has no current owner, refresh event, or retirement condition.

**Worked Completion Judgments**

Complete no-change decision: repository-native checks cover the outcome, sampled handoffs show no recurring gap, a new skill would duplicate guidance, and the record names the omission or policy change that would reopen analysis. No implementation gate is needed because no candidate is being enabled.

Incomplete hook: the configuration parses and one source file is formatted, but the event is unverified, negative matchers were not tested, failure can block editing, and no disable owner exists. Structural success cannot advance this item to trial readiness.

Complete recommendation, blocked implementation: a plugin candidate has a clear user outcome, alternatives, expected permissions, and verification plan, but current bundle contents and owner approval are missing. The record is reviewable, the plugin remains uninstalled, current controls continue, and named inventory plus owner gates define resumption.

**Fresh-Reviewer Replay**

Before claiming the target state, ask a reviewer who did not write the recommendation to reconstruct from saved evidence:

1. What exact outcome and scope are being decided?
2. What happens if the repository remains unchanged?
3. Which evidence is local fact, unrefreshed claim, inference, owner decision, or measured result?
4. Why is this surface preferable to the credible alternatives?
5. What authority is and is not granted?
6. Which behavior, failure, rollback, and outcome checks passed for which exact revision?
7. What remains blocked or uncertain, and what safe fallback is active?
8. Who owns the next action, observation, disablement, refresh, and retirement?
9. Which dependency or event invalidates the current completion claim?

If the reviewer cannot answer without the original conversation, the artifact is not handoff-complete. If fields give individually plausible but incompatible answers, reopen the relevant gates rather than choosing the most favorable status.

Completion evidence should decay visibly. Bind version-sensitive results to the exact setup and environment, timestamp owner and credential decisions where required, and invalidate only affected evidence plus the core regression set after change. Retain concise rationale and identifiers under local retention policy; do not preserve sensitive values or raw conversational content merely to make the checklist look comprehensive.

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
