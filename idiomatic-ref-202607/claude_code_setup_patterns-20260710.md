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

Remain in this reference while deciding the repository outcome, unchanged baseline, candidate surface, portfolio overlap, authority envelope, trial shape, metrics, and lifecycle. Route only the smallest unresolved question that controls the next decision. The setup owner retains the original outcome and incorporates the returned evidence; opening an adjacent reference does not transfer ownership automatically.

The filenames below are confirmed members of the local reference inventory. Their names provide discovery signals only. This section has not evaluated every target's evolved content, freshness, evidence, or fitness, so inspect the relevant target before relying on it. Current product behavior, policy authority, and external effects may require primary documentation or a responsible human owner rather than another pattern reference.

**Stay, Route, Compose, or Stop**

| decision | use when | required result |
| --- | --- | --- |
| Stay | The unresolved question concerns setup portfolio selection, no-change comparison, cross-surface overlap, generic authority, trial, rollback, observation, or retirement. | Update the setup decision record directly. |
| Route | One narrow question has a recognizable specialist domain and its answer can change the next setup action. | Return the controlling evidence, decision boundary, uncertainty, and impact to the original record. |
| Compose | Two specialist questions interact materially, such as durable instructions plus context loading or subagent isolation plus completion verification. | Freeze shared assumptions, assign non-overlapping outputs, and name one reconciliation owner. |
| Stop and escalate | The unresolved question concerns permission, organization policy, secrets, production, compliance, security incident response, or another domain this corpus cannot authorize. | Keep risky setup disabled and obtain the controlling owner's decision or process. |

**Inventory-Derived Routing Matrix**

| unresolved setup question | provisional adjacent reference path | expected return to this reference | remain here when |
| --- | --- | --- | --- |
| Which durable repository instructions belong in a Claude-facing project file, and how should they be scoped and maintained? | `idiomatic-ref-202607/claude_md_management_patterns-20260710.md` | Instruction ownership, placement, precedence, duplication, validation, and refresh evidence. | The question is whether durable instructions are the right surface at all. |
| Which instructions and context should an agent receive for the next action, and how are conflicts bounded? | `idiomatic-ref-202607/agent_context_instruction_patterns-20260710.md` | Context-selection rule, authority ordering, token boundary, and conflict result. | The issue is portfolio-level context cost across several setup items. |
| How should a long conversation preserve a precise resume point? | `idiomatic-ref-202607/chat_checkpoint_context_patterns-20260710.md` | Checkpoint artifact, resume evidence, stale-state rule, and compaction boundary. | The decision is whether a checkpoint control belongs in the setup portfolio. |
| How should test-driven work retain Red, Green, and Refactor state across interruptions? | `idiomatic-ref-202607/tdd_context_retainer_skills-20260710.md`, `idiomatic-ref-202607/tdd_checkpoint_cadence_playbook-20260710.md`, or `idiomatic-ref-202607/tdd_resume_handoff_prompts-20260710.md` | Phase-specific journal contract, cadence, resume point, and next test evidence. | The workflow is not test-driven or only needs a general conversation checkpoint. |
| Should independent workers be dispatched in parallel, and how are scopes reconciled? | `idiomatic-ref-202607/parallel_agent_dispatch_patterns-20260710.md` | Separability decision, worker ownership, shared-state restriction, merge plan, and cost evidence. | A single focused subagent or ordinary sequential work is sufficient. |
| How should one focused subagent be defined, tooled, executed, and evaluated? | `idiomatic-ref-202607/subagent_development_execution_patterns-20260710.md` | Role contract, context boundary, tool permissions, output schema, stop rule, and evaluator. | The unresolved issue is whether delegation improves the repository outcome. |
| A consequential decision has credible competing interpretations that require explicit evidence and convergence. | `idiomatic-ref-202607/agent_debate_evidence_patterns-20260710.md` | Claims, counterevidence, unresolved disputes, convergence rule, and final owner decision. | Ordinary alternative comparison already reaches a bounded decision. |
| The desired behavior is still ambiguous and needs testable requirements or traceability. | `idiomatic-ref-202607/executable_specification_skill_patterns-20260710.md` or `idiomatic-ref-202607/executable_traceability_template_patterns-20260710.md` | Requirement identifiers, preconditions, observable outcomes, negative cases, trace links, and acceptance evidence. | The setup outcome and behavior contract are already precise. |
| What evidence proves completion, and which red signals block a completion claim? | `idiomatic-ref-202607/completion_verification_gate_patterns-20260710.md` | Gate topology, evidence types, failure semantics, reviewer independence, and final decision record. | This reference's proportional completion contract already covers the low-risk candidate. |
| How should code-review findings be produced, prioritized, grounded, and closed? | `idiomatic-ref-202607/code_review_feedback_patterns-20260710.md` | Finding schema, severity, file and line evidence, resolution state, and residual risk. | The question is only whether a review procedure should be automated. |
| How should a skill be structured, triggered, packaged, or evaluated? | `idiomatic-ref-202607/skill_development_reference_patterns-20260710.md`, `idiomatic-ref-202607/openai_skill_yaml_patterns-20260710.md`, or `idiomatic-ref-202607/skill_creator_evaluation_patterns-20260710.md` | Current structure, metadata, trigger cases, progressive disclosure, evaluation, and packaging constraints. | The repository has not yet established that a skill is the right surface. |
| How should a plugin's structure, manifest, commands, or settings be implemented? | `idiomatic-ref-202607/plugin_structure_manifest_patterns-20260710.md`, `idiomatic-ref-202607/plugin_command_development_patterns-20260710.md`, or `idiomatic-ref-202607/plugin_settings_configuration_patterns-20260710.md` | Exact artifact contract, current compatible fields, structural validation, and removal behavior. | Bundle adoption, overlap, permission, and ownership are still undecided. |
| How should a plugin hook be implemented and behaviorally verified? | `idiomatic-ref-202607/plugin_hook_development_patterns-20260710.md` | Current event and matcher mechanics, exit behavior, timeout, reentrancy, failure cases, and disable path. | The setup decision still needs to compare automatic execution with explicit alternatives. |
| How should an MCP integration be configured and validated at implementation level? | `idiomatic-ref-202607/plugin_mcp_integration_patterns-20260710.md` | Current transport, server and tool inventory, authentication, data boundary, failure behavior, and revocation evidence. | The external capability, permission, or standing integration need is not yet justified. |
| How should a plugin or skill be created, demonstrated, installed, or distributed? | `idiomatic-ref-202607/codex_plugin_creator_patterns-20260710.md`, `idiomatic-ref-202607/example_plugin_demonstration_patterns-20260710.md`, or `idiomatic-ref-202607/skill_installer_distribution_patterns-20260710.md` | Packaging and distribution contract, current validation, installation boundary, and uninstall path. | The portfolio decision has not selected a component or resolved trust and maintenance. |
| How should repository history, pull requests, issues, or discussions be captured as evidence? | `idiomatic-ref-202607/github_context_capture_patterns-20260710.md` | Source-linked evolution history, relevant conversation, temporal boundary, and unresolved decisions. | Current local code and guidance already answer the setup question. |
| How should prompting or AI-native instruction design be analyzed beyond setup selection? | `idiomatic-ref-202607/ai_native_prompt_engineering-20260710.md` | Prompt contract, context and evaluator design, uncertainty, iteration, and failure analysis. | The question concerns which Claude Code surface should own a repository workflow. |
| A security, production, language, or backend reliability question controls the decision. | The applicable domain reference, such as a security-resilience or language-specific entrypoint, plus the responsible human process. | Domain requirements, approved authority, tests, escalation, and acceptance owner. | The clause is generic setup mechanics with no domain-specific consequence. |

Do not load the entire matrix. Start from the next blocked claim, inspect the candidate target's relevant headings and evidence, and stop when the return can settle or safely block that claim. If the target turns out stale, incomplete, or inapplicable, record that result and use primary documentation, implementation behavior, or the controlling owner rather than opening adjacent files indefinitely.

**Handoff Packet**

A consequential route should carry:

| handoff field | completion rule |
| --- | --- |
| original outcome and owner | Preserve the user-visible setup outcome and the person or agent responsible for the final portfolio decision. |
| exact specialist question | Ask one answerable question whose resolution changes the next action. |
| frozen revision and evidence | Name the repository revision, source paths, observed behavior, and setup record being analyzed. |
| controlling constraints | Include user restrictions, policy, allowed tools, write scope, external boundary, time or context budget, and prohibited actions. |
| current decision state | State adopted, adapted, paused, rejected, routed, disabled, replaced, or retired candidates and why. |
| expected return | Request the decisive source or behavior evidence, uncertainty, rejected alternative, and recommended impact; avoid an unbounded tutorial. |
| ownership and write boundary | Assign non-overlapping artifacts and name the merge or reconciliation owner. |
| stop and escalation rule | Define what proves the question answered, what constitutes an owned block, and who decides unresolved authority. |

The return packet should be concise enough to merge into the setup decision record. Preserve negative evidence and rejected options; a conclusion without its decisive evidence is likely to be lost or misapplied after context compaction.

**Conflict and Loop Rules**

- Direct user constraints, repository or organization policy, security and data rules, compatible implementation behavior, and responsible owner decisions outrank a generic adjacent pattern.
- If two routes return incompatible actions, keep both, stop the dependent setup, and reconcile their authority, scope, version, and evidence. Do not average the recommendations.
- Stop a routing loop when a target returns no new controlling evidence. Escalate the exact unresolved question or preserve it as a blocked state.
- Parallel routes may read shared evidence but should not edit the same setup artifact unless a single merge owner and deterministic reconciliation plan exist.
- Do not route all of setup to a specialist because one clause needs review. Return to the original decision record after the clause is resolved.
- Product-currentness questions require a permitted current source or installed behavior check. Another historical pattern reference cannot make an archived name current.

**Worked Routes**

Good: a repository has chosen a hook candidate but needs exact event, matcher, timeout, and exit semantics. The setup owner freezes the candidate and routes only those mechanics to `plugin_hook_development_patterns-20260710.md`. The return includes compatible behavior evidence and failure cases; the setup owner then revisits permission, overlap, rollout, and lifecycle here.

Bad: a vague request to improve Claude Code is dispatched simultaneously to context, skill, subagent, plugin, MCP, and verification workers, all allowed to edit setup files. Their recommendations overlap and no one owns reconciliation. Stop, restore one portfolio owner, and return to outcome plus baseline before specialist work.

Borderline: an archived MCP reference names a plausible integration, but current server availability and credential scope are unrefreshed. Route the implementation questions provisionally, keep the integration absent, use a user-provided source-labeled excerpt for the immediate task, and require service-owner approval plus current inventory before returning an adoption recommendation.

Good stop: a proposed setup would approve production deployment or security exception behavior. Preserve the setup evidence and route the controlling clauses to the production or security owner. No generic pattern reference can self-authorize those actions.

**Route Verification**

Verify a route by tracing:

1. outgoing question and why it controlled the next action;
2. target existence, relevant scope, freshness, and authority boundary;
3. preserved constraints, revision, evidence, and excluded actions;
4. returned source or behavior evidence and remaining uncertainty;
5. reconciliation of conflicts and ownership;
6. the exact setup decision, gate, or blocked state changed by the return; and
7. regression checks rerun because the incorporated result affected behavior or authority.

A route passes when it narrows uncertainty or establishes a safe, owned block. Merely reading another file, producing more prose, or delegating work is not a routing outcome.

Track recurring route patterns carefully. Repeated successful claim-level routes can improve future progressive disclosure and trigger descriptions. Repeated loops may expose missing policy, unclear ownership, or references that should be consolidated. Generalize stable decision boundaries, not temporary product names or one repository's vocabulary.

## Workload Model

Treat Claude Code setup as a bounded decision workflow, not a prose-summary task. Workload depends on unresolved interactions and consequences more than raw file, token, tool, or worker counts. Ten files from one duplicated lineage may be easier than one external integration with credentials; one automatic hook may need more review than several read-only instruction documents.

Start with one user outcome, one repository, a read-only discovery pass, no implementation, and a minimal evidence set. Reserve capacity for contradiction review, negative behavior, rollback, owner review, and journaling before expanding discovery. Add a source, tool, worker, or artifact only when it answers a declared question or satisfies a declared gate.

**Workload Classes**

| class | entry conditions | operating pattern | exit or escalation condition |
| --- | --- | --- | --- |
| Focused | One repository and outcome; one decision owner; a coherent local evidence set; one candidate or no-change decision; explicit invocation or read-only behavior; local reversible verification; no new external, secret, production, or organization-policy boundary. | Sequential discovery, one setup decision record, minimal relevant source loading, repository-native checks, and direct owner review. | Complete when evidence and gates close. Escalate when automatic shared reach, a second owner, external data, credential scope, coupled surfaces, or nonlocal recovery appears. |
| Coordinated | Multiple interacting setup surfaces or evidence domains; shared or automatic behavior; several affected users; bounded delegation; one external service with defined owner; replacement of existing controls; or verification requiring independent reviewers. | Stage by decision or surface, freeze shared assumptions, assign non-overlapping read or write ownership, maintain one portfolio owner, use merge checkpoints, and trial in a narrow canary. | Downgrade after evidence removes the interaction; complete after reconciliation and owner acceptance; escalate if authority or recovery crosses specialist domains. |
| Specialist | Production, secrets, security, compliance, incident response, multiple independent systems, unbounded source discovery, conflicting ownership, unsupported current behavior, or effects the generic setup owner cannot authorize or safely reverse. | Contain risky behavior, preserve current evidence, route the exact clause to the controlling process or owner, and keep the generic setup record as the integration boundary. | Return only after the specialist supplies controlling requirements, approved authority, acceptance evidence, and escalation rules; otherwise remain blocked. |

Classify by the highest-consequence unresolved dimension. A task can move down after discovery proves that an apparent boundary is absent. Record why the class changed; class selection is a hypothesis updated by evidence, not a permanent label inferred from request length.

**Workload Dimensions**

| dimension | focused signal | coordination or specialist pressure |
| --- | --- | --- |
| Decision breadth | One observable outcome and one candidate decision. | Several outcomes, candidate portfolio changes, or clauses that require independent acceptance. |
| Source diversity | A few relevant content lineages with known provenance and compatible scope. | Conflicting owners, product-currentness requirements, implementation evidence, external sources, or unbounded discovery. |
| Surface interaction | One explicit, local, reversible surface or a no-change result. | Hooks trigger skills, plugins bundle several controls, agents share writes, or multiple items own the same outcome. |
| Authority | Read-only recommendation and ordinary repository-owner review. | Automatic mutation, shared policy, secret access, external data, production effect, or authority split across domains. |
| Ownership | One decision and maintenance owner. | Separate security, service, deployment, data, compliance, or team owners whose decisions can conflict. |
| Reversibility | Disablement returns immediately to a documented native workflow with no residual state. | Credential revocation, data remediation, migration, shared configuration cleanup, or incident handling is required. |
| Verification | Local structure, behavior, failure, rollback, and user-outcome checks are safe and bounded. | Non-production fixtures, independent reviewers, cross-system observability, long-tail monitoring, or specialist acceptance is needed. |
| Context coupling | Evidence can be loaded progressively for one next decision. | Many sources must be jointly interpreted, early constraints repeatedly disappear, or source roles are disputed. |
| Delegation | Sequential work is adequate. | Independent evidence domains justify workers, but merge ownership and coordination cost must be managed. |
| Lifecycle | One maintainer can refresh, disable, and retire the item. | Bundles, shared credentials, external services, dependencies, or organization-wide rollout create persistent obligations. |

**Budget Ledger**

Set local budgets from consequence, available evidence, and evaluator capacity. Do not reuse the seed's file or subtask counts as universal limits.

| budget | plan before work | update during work | backpressure condition |
| --- | --- | --- | --- |
| Decision budget | User outcome, target state, candidate surfaces, and clauses explicitly out of scope. | Record new decisions created by discovery and which owner controls each. | Stop expansion when the task accumulates outcomes that cannot share one acceptance decision. |
| Source budget | Initial lineages and the question each is expected to answer. | Mark loaded, skipped, duplicate, stale, conflicting, and newly required sources. | Do not load more material when current sources are unlinked to a decision or the next query is undefined. |
| Context budget | Stable instruction prefix, current decision record, minimal relevant evidence, and reserved completion summary. | Offload durable evidence and reread constraints at phase boundaries. | Checkpoint when early constraints, source roles, or open gates can no longer be recalled and verified directly. |
| Tool budget | Discovery, validation, behavior, and audit actions needed; external and destructive calls excluded by default. | Record material calls, retries, unexpected fanout, and commands that changed state. | Stop when retries widen scope, tool outputs are not being used, or an unapproved boundary is reached. |
| Delegation budget | Independent questions, frozen inputs, non-overlapping artifacts, tools, result schemas, and merge owner. | Track worker status, evidence returned, conflicts, and reconciliation effort. | Do not add workers when separability is unclear, shared writes overlap, or merge debt exceeds expected evidence value. |
| Write budget | Authorized paths, one owner per artifact, save cadence, and restoration method. | Record exact changed files and unexpected state. | Stop on an unauthorized path, concurrent ownership conflict, unexplained mutation, or unavailable rollback. |
| External and credential budget | Approved service, tool inventory, data classes, credential scope, calls, retention, and revocation. | Capture aggregate approved usage and boundary events without sensitive payloads. | Disable and escalate on unapproved destination, data, tool, credential, or production effect. |
| Verification reserve | Structural, source, positive, negative, forced-failure, rollback, outcome, independent-review, and final reread gates. | Mark evidence saved and tests invalidated by change. | Do not claim completion or expand rollout when discovery or implementation consumed the reserved evaluator capacity. |
| Recovery reserve | Disable owner, native fallback, backup or restoration plan, incident route, and time to inspect residual state. | Rehearse proportionately and record remaining uncertainty. | Keep the candidate disabled if recovery is theoretical or responsibility is absent. |
| Journal budget | Checkpoints after meaningful batches and before class changes, implementation, external or destructive action, and final completion. | Save phase, exact evidence, changed paths, open risks, and next action. | Pause when the durable record no longer identifies the current revision or first unmet gate. |

The ledger may use approximate categories such as low, expected, and high pressure. Exact token, time, or cost precision is unnecessary unless the environment measures it reliably and the number can change a decision.

**Strategy Selection**

| strategy | use when | tradeoff and verification |
| --- | --- | --- |
| Sequential narrowing | Sources and decisions are coupled, one owner needs a coherent model, or each result determines the next query. | Slower elapsed time but lower merge cost; checkpoint when the source trail becomes long. |
| Parallel read-only research | Evidence questions are independent, inputs can be frozen, and returns have a common schema. | Faster discovery but higher reconciliation cost; verify non-overlapping scope and preserve negative results. |
| Per-surface staging | Hook, skill, plugin, agent, or MCP candidates have distinct behavior and permission gates. | Improves containment but can hide portfolio overlap; reconcile triggers, outcomes, credentials, and owners before adoption. |
| Per-owner routing | Policy or authority, rather than implementation knowledge, blocks progress. | Produces valid decisions but may add waiting time; retain a safe interim workflow and exact return question. |
| Representative sampling | Many repetitive files or trajectories share one lineage or pattern. | Bounds review cost but can miss rare variation; state sampling logic and inspect outliers or high-consequence cases separately. |
| Dependency or source graph narrowing | The repository is large and relevance depends on callers, dependents, ownership, or configuration relationships. | Reduces raw context but graph edges can be stale or incomplete; verify decisive paths against source. |
| Full-corpus read | Source set is small, every part controls the decision, or conflict cannot be resolved by narrowing. | Maximizes coverage but consumes context; summarize claim roles and avoid repeatedly reloading duplicates. |

Progressive disclosure is useful only when every additional source answers a declared question. Loading everything in several delayed batches is still bulk loading.

**Pressure Signals and Immediate Responses**

| pressure signal | likely failure | immediate response |
| --- | --- | --- |
| The next action cannot be tied to the user outcome. | Plan drift or activity replacing decision progress. | Reread the decision record, stop unrelated calls, and restate the next gate. |
| Loaded sources outnumber source-to-decision links. | Discovery fanout without assimilation. | Stop loading, classify current sources, discard duplicates from active context, and define the next question. |
| Early constraints or role decisions are repeatedly contradicted. | Context saturation or stale checkpoint. | Save a durable summary, reread controlling instructions, and resolve contradictions before action. |
| Workers request overlapping writes or return incompatible assumptions. | Bad decomposition and merge debt. | Freeze writes, preserve findings, restore one artifact owner, and reconcile shared premises. |
| Retries add tools, permissions, sources, or scope. | Failure misclassified as transient. | Stop automatic retry, classify the failure, and require a new decision for expanded authority. |
| Structural work advances while negative, failure, or rollback gates remain unscheduled. | Verification starvation. | Reserve evaluator time immediately or keep implementation disabled. |
| A controlling owner is unavailable. | Unowned authority or lifecycle obligation. | Use the safe fallback and mark the candidate blocked; do not infer consent. |
| External or destructive behavior appears unexpectedly. | Boundary escape. | Contain, preserve minimal audit evidence, invoke the responsible process, and suspend ordinary workload progression. |
| The journal no longer names the exact saved revision or open gate. | Resume state is unreliable. | Stop, inspect disk and test evidence, persist a corrected checkpoint, then continue from the durable boundary. |

**Worked Classifications**

Focused: six current/archive source pairs are byte-identical and represent six lineages. One reviewer reads each lineage once, records claim roles, writes one recommendation-only decision record, and runs static checks. Twelve paths do not require twelve workers because provenance is duplicated and the decision owner is singular.

Bad split: file count triggers three workers who each rewrite the same setup recommendation and independently choose plugins. The split creates shared-write conflict, duplicate discovery, and a reconciliation problem larger than the original analysis. Restore one portfolio owner and delegate only distinct read-only questions if needed.

Coordinated transition: a formatter-hook recommendation begins as focused, then discovery shows it will run automatically for all contributors and replace an existing CI check. Move to coordinated review before writing shared configuration; add the repository owner, matcher and failure cases, canary, overlap migration, observation, and disable ownership.

Specialist transition: an MCP candidate would expose repository context through organization credentials to a production service. Keep it absent, preserve the capability question, and route data, security, service, and production clauses to their owners. A small configuration file does not make this a small workload.

Safe downgrade: a suspected external dependency turns out to be a local command with no network behavior, and one repository owner controls it. Record the evidence, remove the external gate, and return to focused analysis rather than retaining unnecessary coordination.

**Workload Audit**

At each checkpoint compare the plan with disk and execution evidence:

1. current workload class and the highest-pressure dimension;
2. user outcome, exact next decision, and target completion state;
3. source lineages planned, loaded, skipped, duplicated, conflicting, and linked to decisions;
4. tools used, retries, external calls, and unexpected state changes;
5. delegated questions, frozen inputs, outputs, writes, and reconciliation status;
6. exact changed paths and one owner per artifact;
7. verification and recovery gates still reserved and evidence already saved;
8. unresolved permissions, owners, conflicts, and adjacent routes; and
9. evidence needed to complete, downgrade, escalate, split, or stop.

The audit passes when actual work remains inside declared boundaries, every expansion has a reason, verification capacity is intact, and the journal can resume from the first unmet gate. Budget compliance alone is not enough: sample a source-to-decision path to verify that loaded evidence is relevant.

Over time, use workload history as an architectural signal. Repeated coordination around overlapping triggers can justify portfolio consolidation. Chronic owner waits can expose missing policy. Frequent source fanout can justify better indexes or claim hierarchies. Do not respond automatically by granting larger budgets; first ask whether the setup and evidence architecture can become simpler.

## Reliability Target

A reliability target belongs to one candidate, scope, revision, environment, and lifecycle decision. It is not a universal score for the reference. The inherited `100 percent` and `18 of 20` thresholds have no supplied calibration evidence and can hide severity: two wrong routes are not tolerable if they authorize production or external-data behavior. Preserve the concerns behind those numbers while selecting evidence and thresholds from local consequence and baseline.

Use a hybrid contract:

- **Hard invariants** protect authority, data, visible failure, and recoverability. Any observed material breach triggers containment regardless of productivity gains.
- **Finite acceptance cases** cover bounded behavior such as a known configuration schema, a declared set of trigger classes, or required output fields.
- **Baseline-relative targets** assess workflow value, latency, review effort, missed steps, and maintenance where recurring comparable tasks exist.
- **Error budgets** can manage low-consequence recurring trigger or command failures when a repository explicitly defines tolerated classes and response.
- **Structured human acceptance** evaluates semantic quality, trust, and usefulness when rates would be misleading.

A target matters only if missing it changes scope, configuration, rollout, ownership, or lifecycle state.

**Reliability Contract Record**

| contract field | required content |
| --- | --- |
| Candidate identity | Exact setup item, revision, environment, repository, user scope, invocation mode, and lifecycle state. |
| Eligible opportunity | Observable condition under which behavior is expected or prohibited; include how silent non-invocation is counted. |
| Contract result | Intended output, action, stop, failure visibility, source boundary, and safe fallback. |
| Consequence classes | Separate harmless inconvenience, workflow interruption, incorrect guidance, unauthorized mutation, external exposure, credential event, and production effect. |
| Hard invariants | Events that require immediate disablement, restoration, audit, or domain escalation. State them as policy constraints, not predictions of future perfection. |
| Calibrated target | Baseline-relative or locally chosen behavior, outcome, cost, latency, trigger, recovery, or maintenance level and why it is appropriate. |
| Numerator and denominator | Define successful, failed, skipped, non-invoked, retried, disabled, and excluded cases. Group retries under the originating workflow. |
| Case diversity | Task classes, positive and negative triggers, failure paths, authority boundaries, versions, and outliers included. |
| Observation boundary | Start and end, canary scope, sample size, setup version, confounders, and evidence not observed. |
| Collection and evaluator | Minimal telemetry, behavior fixture, artifact review, user verdict, independent reviewer, and privacy or retention limits. |
| Miss response | Predeclared adapt, narrow, pause, disable, restore, revoke, escalate, requalify, replace, or retire action by consequence class. |
| Owner and refresh | Person responsible for measurement, containment, interpretation, maintenance, next review, and invalidation after change. |

Define this record before trial results. Otherwise, an attractive candidate can cause its own target to be relaxed after weak evidence appears.

**Target Families**

| family | contract question | suitable evidence | typical miss response |
| --- | --- | --- | --- |
| Authority and data | Did the control operate only on approved files, commands, tools, credentials, destinations, and environments? | Permission review, controlled fixture, tool and network audit, changed-state inspection, owner approval. | Disable; revoke; restore; audit; route to security, service, or production owner; reauthorize only after corrective evidence. |
| Source and claim boundary | Can a reviewer distinguish local fact, refreshed external fact, inherited claim, inference, owner decision, and measured result, and does the source support the claim? | Field validation plus sampled backward trace from consequential claims to passages and behavior. | Block reuse; repair or narrow claims; mark provisional; refresh or remove stale guidance. |
| Trigger correctness | Did the item run for intended opportunities, remain inactive for non-intended opportunities, and reveal expected events where it did not run? | Positive and negative prompts or events, opportunity counters, invocation logs, user reports, and silent-failure cases. | Narrow trigger; move to explicit invocation; return to documentation; disable automatic behavior. |
| Behavioral correctness | Did output, command selection, state change, stop condition, and failure report satisfy the candidate contract? | Finite cases, repository-native commands, forced failures, state diffs, semantic artifact review. | Repair and requalify; reduce capability; pause rollout. |
| Recovery | Can users disable or remove the item and resume the native workflow without unexplained residual state? | Rollback rehearsal, credential revocation, configuration diff, fallback run, owner response exercise. | Keep disabled; simplify design; improve restoration; reject adoption if recovery cost is disproportionate. |
| User outcome | Did the setup improve the decision-record outcome relative to comparable unchanged work? | Baseline or paired task, eligible handoff sample, reviewer verdict, missed-step or correction record. | Adapt instructions or routing, preserve narrow scope, or retire if benefit does not repay cost. |
| Workflow cost | What contributor, reviewer, runtime, context, tool, reconciliation, and waiting cost accompanies the outcome? | Minimal timing and count data, structured effort report, maintenance record. | Reduce context or fanout, choose a smaller surface, consolidate, or accept explicitly for higher-value coverage. |
| Lifecycle reliability | Does the item retain an owner, compatible dependencies, observable health, and working disable path over time? | Scheduled and event-driven review, owner acknowledgment, version check, incident and maintenance history. | Assign owner, suspend, replace, or retire before continued shared use. |

**Method Selection**

| task shape | preferred target form | important limitation |
| --- | --- | --- |
| Finite structural contract | Exhaustive schema, field, path, inventory, and deterministic behavior cases. | Passing structure cannot establish permission, usefulness, or unseen runtime behavior. |
| Frequent low-consequence workflow | Baseline-relative rates or error budget with visible denominators and periodic semantic samples. | Task mix and non-invocation can distort aggregate rates. |
| Sparse semantic decisions | Case-based independent review with explicit evidence and disagreement record. | Reviewer agreement is not ground truth and needs authority plus behavior evidence. |
| Rare high-consequence path | Hard invariant, controlled scenario exercise, specialist acceptance, and immediate stop rule. | Lack of observed failure does not estimate future failure probability. |
| New workflow with no baseline | Conservative canary, explicit expectations, paired review where possible, and bounded qualitative acceptance. | Value claims remain weak until comparable use accumulates. |
| Long-running shared setup | Hybrid outcome, guardrail, recovery, maintenance, and owner-response targets with event-driven invalidation. | Historical success decays after dependency, policy, or owner change. |

Do not add statistical sophistication unsupported by the data. A confidence interval over a biased or incomplete opportunity set is still misleading. Conversely, a concrete material failure should not be dismissed because the sample is too small to estimate a stable rate.

**Surface-Specific Contract Sketches**

Hook: define eligible events, intended match set, explicit non-match set, command source, allowed state changes, latency observation, recursion prevention, failure visibility, timeout, disable path, and manual fallback. Any unapproved mutation or hidden nonexecution breaks the hard contract; ordinary latency and low-consequence command errors may use local targets.

Skill: define intended and non-intended prompts, progressive-disclosure boundary, allowed tools, output fields, source trace, command authorization, refusal behavior, and fallback to instructions. Sample semantic correctness as well as trigger activity; frequent invocation is not proof of usefulness.

Subagent: define separable question, frozen input, context and tool scope, write exclusion or ownership, result schema, stop rule, merge owner, independent verifier, additional coverage, and reconciliation cost. A worker returning text is not a reliable outcome if its evidence cannot be merged or reproduced.

Plugin: define exact component inventory, versions, triggers, permissions, shared dependencies, external services, overlap, update behavior, and complete removal. Evaluate bundled components and portfolio interactions separately; a healthy component does not make an opaque bundle reliable.

MCP: define approved tools, credential and data scope, destinations, audit, source attribution, timeout and partial failure, revocation, and local fallback. Unauthorized tool use, destination, data transfer, or credential expansion is a hard contract break even if issue lookup becomes faster.

**Invalid Target Patterns**

- `18 of 20 routes are correct` without saying whether the two misses are harmless, external, production, or security decisions.
- `100 percent of outputs are labeled` when sampled labels point to sources that do not support the claim.
- `Zero observed failures` when expected opportunities and non-invocations are not counted.
- `Average runtime decreased` after failed and retried runs were excluded or work shifted to reviewers.
- `All tests passed` when cases cover one happy path and omit negative triggers, partial failure, and rollback.
- `No unauthorized action` inferred from a log source that cannot observe all tools, writes, network, or delegated effects.
- `Users are satisfied` without checking semantic correctness or whether users understand the control's boundary.
- `Recovery is documented` without safely exercising disablement and native fallback for the candidate revision.

**Worked Interpretations**

Good: before a user-invoked review-skill canary, the owner defines intended review prompts, unrelated negative prompts, supported source claims, visible command failure, no mutation, native fallback, and an outcome based on omitted required checks per eligible handoff. The sample includes failures and non-invocations, a reviewer checks semantic output, and the predeclared rule supports limited adoption. The conclusion remains scoped to the tested repository and version.

Bad: a route classifier receives a pass because eighteen of twenty decisions match reviewer labels. The two misses both send production and credential questions to ordinary setup automation. Severity was averaged into a favorable score. The candidate fails the hard boundary and must be contained regardless of the aggregate rate.

Borderline: a hook behaves correctly in a small diverse case suite and has no observed guardrail breach, but the sample cannot characterize ordinary latency or rare false activation. Keep the canary narrow, retain the manual formatter path, add different eligible and non-eligible workflows, and do not expand merely by repeating the easiest case.

Misleading success: a plugin reports low failure and short runtime because it stopped activating after a version change. Opportunity evidence shows expected runs with no invocation. Treat silent nonexecution as a reliability failure, not a performance improvement.

**Reliability Audit**

For every trial or review:

1. Confirm candidate revision, environment, owners, scope, and current lifecycle state.
2. Reconstruct the eligible opportunity definition and check whether missed, skipped, disabled, and non-intended cases are represented.
3. Replay one numerator, one denominator, and each material guardrail event from minimal saved evidence.
4. Deduplicate retries and stratify failures by trigger, behavior, dependency, authority, consequence, and recovery.
5. Inspect case diversity rather than counting correlated repetitions as independent breadth.
6. Sample source support and semantic output; structural labels alone are insufficient.
7. Verify disablement, fallback, and owner response for the exact candidate where consequence warrants it.
8. State confounders, unobserved tails, collection blind spots, and evidence invalidated by version or policy change.
9. Trace the result to the promised adapt, narrow, pause, disable, restore, replace, retire, or expansion action.

The last step is essential. A red target that does not alter the setup is not an operational target. Verify the feedback behavior itself: containment should occur when a hard event appears, corrected setup should rerun impacted cases, and broader rollout should require new evidence rather than inherited confidence.

Reliability targets also shape surface selection. If automatic trigger opportunities cannot be observed, explicit invocation may be safer. If rollback is expensive, choose a smaller canary or reject the control. If owner response is unavailable, avoid shared automatic scope. If semantic value cannot be reduced to a rate, pair hard guardrails with structured human acceptance instead of optimizing for measurability alone.

## Failure Mode Table

Use this table to triage Claude Code setup behavior, not to replace repository incident, security, production, service, or compliance procedures. The same symptom can have several causes. Begin with the highest plausible consequence, contain in a way that is safe across competing causes, preserve minimal evidence, and narrow classification before retry or reenablement.

**Severity and Initial Action**

| severity | examples | initial action |
| --- | --- | --- |
| Degraded | A bounded explicit invocation is slow, produces a recoverable formatting error, or asks an unnecessary clarification without changing state. | Preserve the native workflow, classify before retry, and repair under the normal setup owner. |
| Blocking | Shared work cannot proceed, an expected control silently does not run, repeated false activation interrupts users, or rollback is uncertain. | Disable or bypass the setup, restore the documented fallback, freeze expansion, and assign diagnosis. |
| Boundary breach | Unapproved write, command, network destination, data transfer, credential use, production effect, concealed failure, or overlapping agent mutation occurs. | Stop affected behavior, preserve audit state, restore only under authority, and invoke the controlling owner or response process. |
| Unclassified | Evidence is insufficient and a material cause remains plausible. | Apply containment appropriate to the highest plausible class; continue only read-only diagnosis inside approved boundaries. |

**Failure Record**

For a material event, record candidate and revision, time and scope, expected contract, observed symptom, before and after state, plausible causes, evidence preserved, containment, native fallback, affected users or systems, responsible owner, prohibited next actions, and the gate required for requalification. Separate observed fact from suspected cause and explicitly list causes excluded by evidence.

**Operational Failure Taxonomy**

| failure class | trigger or causal condition | discriminating signal | immediate containment | recovery and requalification |
| --- | --- | --- | --- | --- |
| Wrong outcome or unnecessary setup | A tool request bypasses the user outcome or no-change baseline; a surface is selected because it is available. | Candidate cannot name a recurring gap, duplicates a maintained control, or improves an activity without the target outcome. | Stop implementation or rollout; return users to existing controls. | Redo baseline and alternatives; adopt only if new evidence demonstrates a gap and proportional surface. |
| Surface mismatch | Explicit instructions, skill, subagent, hook, plugin, or MCP receives authority poorly matched to trigger, context, or consequence. | Work requires constant manual intervention, automatic behavior surprises users, or a simple local task gains external or bundled complexity. | Disable the candidate while preserving the native route. | Reevaluate at the outcome level; replace the surface and rerun authority, behavior, recovery, and value gates. |
| Source drift or role inversion | Product, repository, policy, or owner changes; archive, current path, supporting example, or confident wording is mistaken for controlling authority. | Configuration disagrees with installed behavior; duplicate copies are counted as corroboration; a provisional name appears as current fact. | Block dependent setup and mark affected claims stale, provisional, or conflicting. | Compare versions and authority, refresh permitted current evidence, update dependents, and sample backward plus forward trace. |
| Instruction conflict or context loss | Long work drops early constraints, summaries overwrite user intent, or several instruction surfaces disagree. | Current action contradicts saved scope, permission, evidence boundary, or first unmet gate; workers use incompatible premises. | Stop state-changing work, persist current disk evidence, and reread controlling instructions plus decision record. | Resolve precedence with the appropriate owner, update the durable checkpoint, and replay the next action from the corrected state. |
| Trigger false positive | Hook or skill activates outside intended files, events, prompts, users, or workflows. | Negative cases produce invocation; users report unrelated interruption; matcher scope exceeds the contract. | Disable automatic behavior or move to explicit invocation. | Narrow trigger, add negative regression cases, verify opportunity logging, and requalify in a limited canary. |
| Trigger false negative or silent non-invocation | Event, metadata, matcher, version, or dependency prevents expected activation. | Eligible opportunities lack invocation or outcome while execution-only logs look healthy. | Restore manual or native enforcement and mark the setup degraded. | Verify current trigger semantics, count expected opportunities, add non-invocation detection, and test compatible versions. |
| Command drift or partial execution | Repository scripts, paths, dependencies, environment, timeout, or output handling change. | Missing command, unexpected exit, partial artifact, stale argument, or success summary inconsistent with raw status. | Stop chained steps; expose partial state and run no guessed replacement. | Re-read repository commands, restore state if needed, force each failure branch, and bind evidence to the exact revision. |
| Automatic mutation, recursion, or fanout | A hook rewrites files repeatedly, triggers itself, invokes broad commands, or causes nested agent or tool activity. | Rapid repeated events, expanding diffs, duplicate commands, latency spike, or worktree changes beyond matcher scope. | Disable the trigger, stop downstream processes, preserve state, and prevent automatic restart. | Inspect event graph, enforce idempotence and bounded scope, add recursion and fanout cases, or choose explicit invocation. |
| Delegated ownership collision | Subagents receive overlapping writes, mutable inputs, incompatible assumptions, or no merge owner. | Conflicting diffs, duplicate findings, overwritten evidence, or each worker self-reports completion on a different revision. | Freeze writes, preserve outputs separately, and restore one owner per artifact. | Reconcile against a frozen revision, redefine independent scopes and output schema, rerun integration checks, and measure merge cost. |
| Plugin opacity or portfolio overlap | A bundle adds undisclosed hooks, skills, agents, MCP services, settings, or commands that duplicate current controls. | Unexpected triggers, double execution, permission expansion, conflicting owners, or uninstall leaving active components. | Disable or remove the bundle under owner control; revoke unnecessary access and restore prior controls. | Inventory exact contents and versions, map overlap, test component and whole-bundle removal, then adopt only justified capabilities. |
| MCP credential or data boundary escape | Server, tool, destination, input, credential, or retention exceeds the approved integration contract. | Unapproved tool call, repository content sent externally, broader token scope, unknown destination, or missing audit and revocation. | Stop calls, revoke or narrow credentials, preserve minimal audit evidence, and notify the service or security owner. | Complete the controlling response, verify tool and data scope in a safe boundary, test revocation and fallback, and obtain renewed approval. |
| External dependency degradation | An approved service is unavailable, rate-limited, slow, inconsistent, or returns partial data. | Timeout, transient status, stale response, partial result, or service health evidence without local mutation. | Use the documented local or manual fallback and avoid request fanout. | Retry only under the bounded retry policy after side effects are excluded; preserve source freshness and partial-result labels. |
| Verification proxy or hidden failure | Syntax, file presence, label count, invocation, or self-review is treated as proof of behavior and outcome. | Structural checks pass while negative, failure, rollback, semantic, or authority cases are absent; summaries conceal nonzero status. | Block completion and expansion; surface raw concise failure evidence. | Add the missing evidence layer, use an independent reviewer where consequential, and trace the decision to actual behavior. |
| Recovery or fallback failure | Disablement, removal, credential revocation, restoration, or repository-native workflow is incomplete or untested. | Residual triggers, changed files, active credentials, broken native command, or users still depend on the faulty item. | Keep the candidate disabled and assign restoration to the appropriate owner. | Reconcile residual state, rehearse rollback safely, verify native operation, and redesign or reject if recovery remains disproportionate. |
| Metric blind spot or gaming | Denominator omits failures and non-invocation, retries count as successes, task mix changes, or activity substitutes for value. | Dashboard improves while artifacts, users, or reviewers report worse outcomes; no trace exists from signal to action. | Pause rollout decisions based on the measure and preserve current scope. | Repair opportunity and failure collection, sample semantic outputs, restate confounders, and predeclare a new decision rule. |
| Routing loop or authority deadlock | Adjacent references return no new evidence, owners disagree, or each route passes the question onward. | Repeated handoff, growing context, unchanged blocked claim, or conflicting approvals without a controlling decision. | Stop routing, retain the exact unresolved clause, and keep dependent behavior disabled. | Identify controlling authority, reconcile evidence and scope, or record an owned block with a safe interim workflow. |
| Lifecycle and owner drift | Maintainer departs, dependency or policy changes, review date passes, credentials outlive purpose, or a replacement makes the control duplicate. | No response to red signals, stale versions, orphaned configuration, repeated manual repairs, or parallel old and new controls. | Suspend shared or automatic behavior when safe ownership is absent; use the native fallback. | Assign owner and refresh evidence, migrate dependents, revoke obsolete access, or retire and verify removal. |

**Response Choice**

| response | use only when | do not use when |
| --- | --- | --- |
| Bounded retry | Evidence classifies a transient failure, prior attempt had no material side effect, retry cannot expand authority, and a finite attempt plus stop rule exists. | Root cause is unknown, external or destructive effect is plausible, credentials failed, or retry changes scope. |
| Native fallback | The repository has a documented manual or existing control that preserves the user outcome safely. | The fallback itself is stale, unverified, or crosses the same failed dependency. |
| Disable or isolate | Automatic, shared, recurring, or boundary-crossing behavior may continue causing harm or interruption. | Disablement would itself create a higher-consequence failure without controlling-owner coordination. |
| Restore or rollback | Desired prior state is known, evidence is preserved, and the responsible owner approves the operation. | Restoration could erase legitimate user work or audit evidence, or the baseline is uncertain. |
| Repair in place | Surface remains appropriate, cause is bounded, recovery works, and regression evidence can cover the change. | The surface makes trigger, authority, failure, or recovery inherently unobservable. |
| Replace surface | A different invocation, context, or authority model directly resolves the recurring design failure. | Replacement only hides an implementation defect or creates greater migration risk without outcome evidence. |
| Escalate | Policy, permission, security, service, production, data, or unresolved ownership controls the next safe action. | Ordinary technical diagnosis remains within the setup owner's bounded authority. |
| Retire | Outcome disappeared, a maintained control supersedes it, owner or compatibility cannot be restored, or ongoing cost exceeds measured value. | Dependents, credentials, triggers, or fallback migration remain unresolved. |

**Worked Triage**

Good: an automatic formatter hook rapidly repeats and expands a diff. The owner disables the hook without erasing the worktree, records event and command evidence, restores the manual formatter path, and classifies recursion as plausible. A disposable case then proves the event graph and idempotence. The candidate returns only after negative, recursion, failure, and rollback gates pass, or it is replaced by explicit invocation.

Bad: an MCP call returns an authorization error and the agent retries with broader credentials and a larger tool scope. The symptom could indicate policy or revoked access, and retry expands the boundary. Stop calls, revoke or inspect credentials under the service owner, preserve audit evidence, and do not treat this as ordinary transient backoff.

Borderline: a repository-native test command times out once, produces no writes, and the service it contacts is known to have a transient health event. One bounded retry may be permitted after confirming idempotence, timeout behavior, and no external side effect. A second failure stops the setup and uses the fallback; the retry does not add tools, permissions, or scope.

Competing causes: a skill output is absent. Possible causes include false-negative triggering, stale metadata, command failure, or user non-invocation. Execution logs alone cannot discriminate them. Compare expected opportunity, trigger evidence, invocation, command status, and output path before changing the skill description or retrying the command.

**Requalification Gate**

Do not reenable or close a material failure until the record shows:

1. observed symptom and affected state are preserved without unnecessary sensitive content;
2. plausible high-consequence causes are excluded or transferred to the controlling response process;
3. root cause is reproduced safely or supported by sufficient evidence;
4. containment remains effective and the repository-native fallback works;
5. repair or replacement changes the causal boundary rather than only suppressing the visible symptom;
6. positive, negative, forced-failure, non-invocation, and rollback regressions cover the affected contract;
7. permissions, external boundaries, owners, and dependents are reconciled;
8. residual uncertainty and recurrence signal are recorded; and
9. the authorized owner explicitly selects reenable, remain narrow, replace, or retire.

Recovery is verified only when ordinary work succeeds without depending on the faulty control. For external, destructive, or production failures, use sanitized fixtures and specialist acceptance instead of reproducing harm.

After recovery, update general guidance only when the causal lesson is recurring or materially consequential. A repeated trigger problem can change surface selection; recurring bundle overlap can drive portfolio consolidation; owner loss can strengthen retirement gates. Keep environment-specific defects in local records. Concentrated failures through one command, credential, service, or owner are architectural evidence of a shared dependency, not isolated bad luck.

## Retry Backpressure Guidance

A retry repeats the same authorized operation against the same logical input and effect boundary after a classified failure. Changing tools, command, files, credentials, destination, data, permissions, candidate surface, or side-effect model is re-planning. Running again after an owner changes authority is a newly authorized attempt. Restoring state is recovery. Keep these transitions explicit so error handling cannot smuggle in broader capability.

Default to no automatic retry. Permit retry only through a preapproved operation-specific policy or a documented human decision after inspecting the prior attempt. This reference does not prescribe a universal attempt count, delay, timeout, or jitter formula; those values depend on service behavior, command cost, consequence, idempotency, and local policy.

**Retry Eligibility Gate**

All applicable conditions must be satisfied:

| eligibility question | evidence required | result if unresolved |
| --- | --- | --- |
| Is the failure classified? | Concrete signal supports transient dependency, stale read, lost response, or another retryable class; deterministic logic, authority, policy, and design causes are considered. | Do not retry; preserve evidence and diagnose. |
| Is the prior effect known? | Before and after state, command or tool status, downstream effect, and partial result are inspectable at the consequence boundary. | Treat material side effect as plausible and contain. |
| Is the operation idempotent or safely compensable? | Repetition cannot duplicate writes, notifications, charges, deployments, agent fanout, or irreversible external activity, or a tested compensation exists under owner control. | Use fallback, recovery, or specialist handling. |
| Is the logical input unchanged and still current? | Repository revision, request parameters, source version, credential scope, and target are identical or intentionally refreshed under the same contract. | Re-plan and reverify; do not call it a retry. |
| Is authority unchanged and valid? | The same owner-approved tools, files, commands, data, destination, environment, and effect remain allowed. | Obtain new authorization or stop. |
| Is a retry signal observable? | The next result can distinguish recovery from repeated or partial failure, including non-invocation and downstream status where relevant. | Prefer fallback; consequential blind retries are prohibited. |
| Is the attempt budget finite and predeclared? | Local policy defines remaining attempts, delay or backoff, deadline, total workload budget, and exhaustion action. | Pause until an owner defines a bounded policy. |
| Is a safe fallback available? | Users can continue or stop safely through repository-native, cached, user-provided, or manual behavior. | Keep setup disabled if retry exhaustion would trap the workflow. |
| Is the setup version stable? | No concurrent edit, dependency change, owner change, or worker conflict invalidates the original classification. | Checkpoint, reconcile, and requalify the changed candidate. |

Idempotency must cover the whole effect graph. A nominal read can consume quota, create an audit event, trigger downstream processing, or expose data. A local command can invoke a network service or mutate caches. Verify the boundary that matters, not only the immediate API verb or command name.

**No-Retry Classes**

Do not automatically retry after:

- permission, policy, approval, credential-scope, or production-authority denial;
- unknown, partial, destructive, externally visible, or unrecoverable state change;
- unapproved data transfer, destination, tool, command, write, or secret access;
- deterministic syntax, schema, configuration, command, or logical contradiction;
- a hook recursion, agent fanout, shared-write collision, or duplicate side effect;
- hidden nonexecution or concealed failure whose observability remains broken;
- a repeated failure with unchanged evidence and no new transient signal;
- an ownerless operation or unresolved conflict between controlling authorities;
- exhausted local attempt, wall-clock, rate, context, or recovery budget; or
- a proposed second attempt that expands capability or scope.

Backoff changes timing, not causality. It cannot repair an unsupported field, invalid command, denied permission, wrong surface, or missing owner.

**Backpressure States**

| state | entry signal | permitted work | release condition |
| --- | --- | --- | --- |
| Open | Sources, ownership, configuration, behavior, verification reserve, and journal state are current; no material red signal exists. | Continue the next declared bounded action. | Any pressure signal moves the run to cautious, paused, or stopped. |
| Cautious | Low-consequence transient failure, rising source or tool fanout, uncertain task comparability, or nearing local budget. | Read-only diagnosis, one eligible policy-bound retry, fallback preparation, and checkpoint update. No authority expansion. | Classified recovery plus updated evidence, or escalation to paused. |
| Paused | Verification gate is red, prior effect is uncertain, source conflict controls the action, worker scopes overlap, owner decision is pending, or retry budget is exhausted. | Containment, evidence preservation, native fallback, read-only diagnosis, owner communication, and plan repair. | Exact blocker resolves, impacted gates pass, and a durable checkpoint names the resumed action. |
| Stopped and escalated | Boundary breach, destructive or external consequence, credential or production concern, rollback failure, or controlling process requires specialist handling. | Actions authorized by the responsible response process only; ordinary setup retries and expansion cease. | Controlling owner records recovery, residual risk, reauthorization, and requalification requirements. |

Backpressure applies to new generation and implementation, not only the failing command. When evidence quality is red, producing more recommendations can amplify stale or partial conclusions. When workers conflict, stop new delegation. When verification reserve is consumed, stop feature expansion. When the journal is stale, stop state-changing work until the disk boundary is reconstructed.

**Failure-Class Response Matrix**

| classified condition | retry posture | safer alternative | evidence to resume |
| --- | --- | --- | --- |
| Transient read timeout with no effect | Eligible under a finite local policy when target and input remain current. | Cached source with freshness label, user-provided excerpt, or manual lookup. | Service signal, attempt record, unchanged authority, and complete or explicitly partial result. |
| Stale external evidence | A fresh read may be a new authorized source action rather than a retry; use the task's browsing and source rules. | Mark claim unrefreshed, pause the product-specific recommendation, or use installed behavior evidence. | Current primary source, date or version, changed-claim review, and dependent-gate rerun. |
| Missing local context | Do not rerun implementation blindly. Load only the source required by the blocked question. | Reread decision record, source hierarchy, or repository-native guidance. | Exact missing claim resolved without exceeding context or source budget. |
| Repository command transient failure | Eligible only if command and downstream effects are known, input is unchanged, and no mutation occurred. | Preserve failure, use documented alternate verification, or wait for dependency recovery. | State diff, dependency evidence, command contract, and bounded rerun result. |
| Deterministic configuration or schema error | Not retryable unchanged. | Repair through current compatible evidence and rerun structural plus behavioral gates. | Reviewed change, exact revision, negative case, and no authority expansion. |
| Hook recursion or automatic fanout | Not retryable while enabled. | Disable trigger, run the native command explicitly, and inspect the event graph. | Idempotence, recursion prevention, bounded scope, failure, latency, and rollback cases. |
| Subagent shared-write conflict | Workers must not independently retry edits. | Freeze writes, preserve findings, assign one artifact owner, and reconcile against one revision. | Non-overlapping scopes, deterministic merge, repository tests, and owner acceptance. |
| Plugin partial installation or removal | Do not repeat until component state is inventoried. | Restore prior portfolio and use individual native controls. | Exact bundle inventory, residual-state audit, migration and removal tests, renewed approval. |
| MCP authorization or credential error | Not retryable by broadening token, tool, or workspace scope. | Manual source-labeled context or service-owner resolution. | Approved credential and tool scope, revocation evidence, data boundary, audit, and safe test. |
| Verification tool failure | Retry only if the verifier itself failed transiently and no setup result is being inferred from its absence. | Preserve the candidate as unverified and use an independent equivalent check if authorized. | Verifier health, exact command output, result consistency, and remaining test coverage. |
| True evidence contradiction | Repetition cannot reconcile incompatible claims. | Preserve both, freeze the dependent action, and route to controlling authority or behavior evidence. | Written resolution, rejected alternative, impacted records, and regression checks. |

**Attempt Record**

For each material attempt, save:

| field | value to record |
| --- | --- |
| operation identity | Stable logical operation and candidate revision, not merely a tool-call sequence number. |
| attempt state | Initial, eligible retry, re-planned attempt, newly authorized attempt, fallback, recovery, exhausted, or escalated. |
| input and scope | Repository revision, source version, parameters, files, tools, destination, credential class, environment, and allowed effects. |
| prior result and effect | Failure signal, partial output, before and after state, downstream evidence, and uncertainty. |
| classification | Failure class, confidence, competing causes, and why retry is or is not allowed. |
| policy | Remaining local budget, delay reason, deadline, rate boundary, and stop condition. Do not store sensitive credential values. |
| owner | Person or process authorizing retry, fallback, recovery, re-plan, or escalation. |
| outcome | Success, partial, repeated failure, new failure, non-invocation, restored fallback, or boundary event. |
| next transition | Continue, cautious, pause, stop, requalify, replace, or retire with exact evidence needed. |

An interrupted run must recover this state from disk rather than assuming an attempt did or did not complete. Inspect changed state and durable logs before issuing another operation.

**Distributed and Long-Running Work**

- Assign one owner per writable artifact. Workers can retry read-only evidence questions under their own bounded policy, but a write retry returns to the artifact owner.
- Coordinate backoff for a shared service. Independent workers following identical local policies can create a collective request storm.
- Include attempt identity and frozen input revision in worker returns so duplicate work and stale results can be detected.
- Stop new delegation when reconciliation debt, conflicting assumptions, or worker failure consumes the verification reserve.
- Checkpoint before class escalation, implementation, shared configuration, external calls, destructive or production action, and final completion.
- Reread the current decision record and first unmet gate after a pause; do not let a stale plan authorize a resumed retry.
- Treat commit, push, deployment, credential change, or destructive restoration as separate explicitly authorized actions, never as implicit recovery.

**Worked Decisions**

Good retry: an approved read-only source request times out, service evidence indicates a transient issue, no response or side effect was recorded, input and destination remain unchanged, and the local policy permits a finite delayed retry. The attempt record groups both calls under one workflow outcome and falls back to an unrefreshed label if the budget is exhausted.

Bad retry: an MCP operation is denied, so the second attempt requests broader credentials and enables more tools. That is a new authority proposal, not a retry. Stop calls, preserve the denial, keep the integration absent, and route to the service and security owners.

Borderline retry: a local test command times out and the worktree remains unchanged, but downstream service effects are not observable. Keep the setup paused and use a safe alternate check or owner evidence; do not rerun until the relevant effect boundary is known.

Recursive hook: repeated formatting events appear. Disable automatic execution first. Running the same hook again to "confirm" recursion can enlarge the diff and event queue. Reproduce only in a disposable fixture after idempotence and event controls are understood.

Verifier outage: the static validator process fails before reporting a result. The setup remains unverified, not failed and not passed. A bounded verifier retry may be valid if the tool failure is transient and cannot change setup state; otherwise use an authorized independent check and preserve the discrepancy.

**Backpressure Audit**

Verify that the mechanism, not only the prose, works:

1. A red gate prevents new implementation, rollout, and confident recommendation generation.
2. Attempt identity, prior effects, classification, scope, and budget can be reconstructed.
3. An eligible transient case recovers or exhausts exactly through the local policy without duplicate effect.
4. A permission, deterministic, unknown-effect, and boundary-breach case receives no automatic retry.
5. Fallback lets ordinary work continue without the faulty control.
6. Distributed workers stop shared writes and service fanout when pressure rises.
7. Resume occurs from an updated durable checkpoint only after the exact blocker and impacted gates clear.
8. Exhaustion updates reliability, failure, dependency, and lifecycle records rather than disappearing into logs.

Repeated retry pressure is design evidence. It may justify explicit invocation, better observability, a local fallback, dependency replacement, smaller scope, or retirement. Do not reflexively enlarge budgets; first ask whether the chosen surface or external dependency makes the contract unnecessarily fragile.

## Observability Checklist

Observability should answer whether an eligible setup opportunity occurred, whether the control invoked, what contract path it took, what effect it produced, whether failure remained visible, and what lifecycle action followed. It should not become a transcript archive or a second uncontrolled data boundary.

Collect only evidence capable of changing a setup decision, reliability judgment, diagnosis, recovery, or retirement. By default, do not record raw prompts, full source text, full diffs, secrets, tokens, credential values, personal data, or external payloads. Use concise classifications and policy-approved references to source or artifacts. Logging, storage, and export are themselves setup effects and belong in the authority and data review.

**Minimum Conceptual Event**

Map these fields to the repository's approved local tools; they are not a claim about a current product telemetry schema.

| field | required meaning | privacy and quality boundary |
| --- | --- | --- |
| workflow identifier | Joins one user outcome across opportunity, invocation, retry, fallback, verification, and lifecycle decision. | Use a bounded opaque identifier; do not encode prompt or user content. |
| candidate identifier and revision | Exact hook, skill, subagent, plugin, MCP, or instruction version under observation. | Historical evidence does not transfer silently to a changed candidate. |
| environment and scope class | Repository or approved environment, user or canary class, and explicit or automatic invocation mode. | Avoid sensitive machine or identity detail unless required and approved. |
| event family and time | Opportunity, invocation, source use, tool action, effect, result, retry, fallback, verification, owner action, or lifecycle transition. | Record clock and ordering limitations; timestamps alone do not prove causality. |
| contract path | Intended, non-intended, expected stop, success, partial, failed, timed out, non-invoked, disabled, rolled back, or escalated. | Use explicit partial and unknown states; do not collapse them into failure or success. |
| allowed effect class | Read, local command, bounded write, external read, external write, credential use, delegation, or production class approved by the record. | Store class and approval pointer, never credential material. |
| observed effect class | Independently observable files, commands, network class, delegated work, residual state, or no observed effect. | `No observed effect` is not `no effect` when coverage is incomplete. |
| concise result | Exit class, output contract status, changed-path summary, source-support status, or reviewer verdict. | Prefer bounded summaries and artifact identifiers over payloads. |
| failure and retry state | Failure class, prior-effect confidence, attempt grouping, remaining local policy state, and stop reason. | Group retries under one workflow and avoid storing sensitive service errors verbatim. |
| evidence pointer | Approved command summary, state snapshot, behavior case, artifact, source passage, service audit reference, or owner decision. | Pointer access and retention must match the underlying data policy. |
| owner action | Continue, adapt, narrow, pause, disable, restore, revoke, route, replace, retire, or requalify with responsible owner. | A red event without an action path is an observability failure. |

Also record expected opportunities that produce no invocation. Execution-only data can make a disabled or broken automatic control appear fast and reliable.

**Event Families**

| family | question answered | representative signals |
| --- | --- | --- |
| Opportunity | When should the control have run or remained inactive? | Eligible event or prompt class, non-intended class, excluded reason, source revision, and expected owner. |
| Invocation | Did the declared surface activate, and through which trigger? | Explicit request, matcher result, selected skill, delegated task, plugin component, MCP tool, or no invocation. |
| Context and source | What evidence was planned, loaded, skipped, duplicated, stale, conflicting, and actually used? | Content-lineage identifiers, query purpose, source role, freshness state, and claim link; no raw dump by default. |
| Tool and action | What authorized command, file, tool, service, or worker action occurred? | Action class, approved scope, concise status, timeout, and attempt identity. |
| Effect | What state, data, destination, downstream action, or residual condition is independently visible? | Changed-path class, network destination class, credential class, child worker, audit reference, or unknown effect. |
| Result | Did the output and stop behavior satisfy the contract? | Complete, partial, failed, hidden-failure check, source support, unresolved risk, and user-visible fallback. |
| Verification | Which structural, positive, negative, forced-failure, rollback, outcome, and reviewer gates ran? | Gate identifier, exact candidate revision, pass or fail, evidence pointer, and invalidated evidence. |
| Lifecycle | How did the evidence change portfolio state? | Proposed, paused, trialing, adopted, disabled, replaced, retired, next review, owner change, or escalation. |

**Risk-Scaled Coverage**

Focused, explicit, read-only setup may use a local decision record, concise command summaries, sampled outputs, and owner verdict. Shared automatic setup adds expected opportunities, trigger positives and negatives, latency or interruption, state effects, failure visibility, disablement, and owner response. Delegated or bundled setup adds child identity, frozen input, write ownership, component inventory, merge result, and residual component state. External, credential, production, or security-sensitive behavior requires the audit, data, retention, and response evidence approved by the controlling domain; local setup logs cannot self-certify that boundary.

**Surface-Specific Signals**

| surface | minimum useful observability | material blind spot to avoid |
| --- | --- | --- |
| Durable instructions | Instruction revision, applicable scope, conflicting source, task sample, followed or violated clause, and owner change. | Assuming a file was loaded, understood, or obeyed because it exists. |
| Hook | Expected event, matcher decision, invocation, command, duration class, exit, changed-state class, recursion indicator, disablement, and fallback. | Logging executions but not expected events that failed to invoke or broad events that should not match. |
| Skill | Intended and non-intended prompt class, selection, progressive source load, allowed tools, output contract, refusal or stop, and user verdict. | Storing raw prompts or treating selection frequency as correctness. |
| Subagent | Parent workflow, frozen revision, delegated question, context and tool scope, write owner, result state, evidence, merge, and verification. | Each worker self-reporting success without shared-state or integration evidence. |
| Plugin | Exact version and component, component trigger and effect, shared permissions, overlap, update, disable, removal, and residual inventory. | One plugin-level healthy signal hiding a failing or unobserved bundled component. |
| MCP | Approved server and tool class, request purpose, destination class, credential class, outbound data class, result freshness, timeout, partial state, audit, revocation, and fallback. | Payload or token logging, and inferring no external effect from local client status alone. |

**Evidence Sources and Tradeoffs**

| source | strength | blind spot | default handling |
| --- | --- | --- | --- |
| Structured local event | Compact, joinable, and suitable for opportunity, invocation, result, and owner-action counts. | Producer can omit or misclassify its own behavior. | Keep bounded cardinality and corroborate material effects independently. |
| Command summary | Exposes command identity, concise exit, duration, and selected output. | Exit status does not prove semantic result or absence of side effects. | Save command source and state comparison where mutation matters. |
| State snapshot or diff summary | Reveals file or configuration change and residual state. | Can contain sensitive source and may miss external effects. | Store changed paths or classes by default; retain full detail only under approved need. |
| Sampled artifact review | Evaluates semantic quality, source boundary, uncertainty, and next action. | Reviewer bias and sampling gaps. | Use a stable rubric and independent review for consequential claims. |
| External service audit | Can establish tool, destination, credential class, and server-side result. | Access may be restricted; service logs can be delayed, incomplete, or differently scoped. | Use owner-approved references and state coverage limits. |
| User or maintainer report | Exposes interruption, trust, hidden correction, and owner burden. | Memory, selection, and preference bias. | Pair with an observable case when it changes a technical claim. |
| Full trace | Helps rare cross-process diagnosis and ordering analysis. | High privacy, retention, cardinality, and review cost. | Use only for approved bounded investigation; minimize and expire it. |

Choose one primary signal and independent corroboration for the highest-risk claim. Do not duplicate every low-value counter merely to make the trace look comprehensive.

**Data and Trust Controls**

- Define event producer, transport, storage, readers, retention, deletion, and incident owner before collecting sensitive or cross-system evidence.
- Bound labels and identifiers so user input, source text, paths with secrets, issue content, or external payload cannot become unbounded telemetry dimensions.
- Redact before storage where possible and test redaction with representative secret, personal-data, and source-content fixtures.
- Keep setup revision, environment, workflow, and attempt alignment; otherwise events from different candidates can be joined into a false trace.
- Mark delayed, missing, duplicate, malformed, reordered, and untrusted events explicitly. Do not silently repair them into favorable counts.
- Treat agent-generated success as a claim. Corroborate consequential file state, network effect, credential state, and production behavior from an independent source.
- Include logging and export in the effect graph. A log write can trigger a hook, consume quota, or transmit data.
- Expire diagnostic detail after its approved purpose; retain only minimal durable decision evidence under local policy.

**Observability Failure Modes**

| symptom | likely gap | response |
| --- | --- | --- |
| Invocations look healthy but users report missed automation. | Expected opportunities or non-invocation are absent. | Add independent opportunity evidence, keep manual fallback, and pause automatic expansion. |
| One workflow appears as several successes. | Retries or delegated child actions are not correlated. | Introduce stable workflow and attempt identity; recompute outcomes without duplicate credit. |
| Result is `success` despite partial artifact or nonzero command status. | Producer collapses contract paths or self-certifies. | Add explicit partial and failure states plus independent verifier evidence. |
| External calls appear absent locally. | Client log cannot see downstream or delegated effects. | Obtain approved server-side evidence or reduce authority and treat effect as unknown. |
| Metrics shift after an update with no behavior change recorded. | Setup versions, clocks, schema meanings, or task mix are misaligned. | Freeze revision, validate event schema, state confounders, and invalidate incompatible history. |
| Audit storage contains prompt text, tokens, issue payload, or source content. | Data minimization and redaction failed. | Stop collection, follow the applicable data response, repair and test redaction, and narrow retention. |
| Logging creates repeated triggers or high fanout. | Observability path participates in the setup event graph. | Disable recursive path, bound event emission, and verify no feedback loop. |
| Red events accumulate without lifecycle change. | Owner-action signal or operational response is missing. | Apply backpressure, assign owner, and verify containment before resuming. |

**Worked Traces**

Good hook trace: one opaque workflow identifier links an eligible file event, matcher decision, hook revision, approved formatter command class, concise exit, changed-path class, no recursion, verification result, and owner rollout action. Negative events show non-matching files remain inactive. No file content or user prompt is stored.

Bad MCP trace: the log writes full request payload, issue content, repository snippets, bearer token, response body, and user identity to a general store while omitting the approved tool and destination class. Stop collection, contain and respond under the data and credential owners, and redesign around minimal classes plus approved audit references.

Borderline plugin trace: the host records plugin invocation and overall success but cannot identify which bundled hook, skill, or external component acted. Keep use narrow or disabled, inventory components, add component-level effects and removal evidence, or prefer individually observable controls.

Good skill sample: the record stores intended prompt class, candidate revision, selected or not selected, source-lineage identifiers loaded, tool classes used, output contract status, unsupported-claim count from a reviewer, and final user action. Raw prompt and output remain outside telemetry; a separately approved artifact sample supports semantic review.

**Observability Acceptance**

Generate fixtures for intended opportunity, non-intended opportunity, silent non-invocation, normal success, expected stop, partial result, command failure, timeout, retry, fallback, unauthorized effect, disablement, rollback, and lifecycle change. Then verify:

1. Expected events appear exactly once per logical state transition or are detectably missing.
2. Workflow, candidate revision, environment, attempt, child work, and result join without merging unrelated runs.
3. Partial, failed, unknown, and non-invoked states cannot be reported as success.
4. Hard boundary events receive independent effect evidence and trigger the promised owner action.
5. Redaction and bounded-cardinality tests prevent secret, prompt, source, personal, and external payload leakage.
6. Retention, access, deletion, and outage behavior match local policy; observability failure does not authorize blind operation.
7. One end-to-end trace can be replayed from opportunity through invocation, effect, verification, fallback, and lifecycle decision.
8. Missing, duplicate, delayed, malformed, and untrusted events are visible and cannot silently improve reliability measures.

Use sampled real aggregate evidence only where permitted; synthetic acceptance cannot cover every live path. State coverage and trust limits beside conclusions. If consequential effects cannot be observed safely, narrow authority, require a controlling owner, or select a more observable surface.

Observability burden belongs in the setup tradeoff. A control that needs expensive cross-system traces to prove basic boundaries may not repay its value. Conversely, a common minimal event model can expose trigger overlap, shared credentials, duplicate commands, and owner gaps across the portfolio. Use that map to simplify setup, not to justify collecting more data by default.

## Performance Verification Method

Performance means the cost of producing a contract-compliant user outcome, not the speed of invocation or volume of activity. Measure performance only after correctness, source fidelity, authorization, failure visibility, and recovery meet their gates. A fast wrong answer, a silent non-invocation, an unauthorized external call, or a low-latency control that shifts cleanup to reviewers is not a performance success.

No universal tool-call, timeout, context, latency, or reviewer-time budget is established here. Choose local decision thresholds from the unchanged baseline, consequence, task frequency, user tolerance, and evaluator capacity. Use percentiles only when enough comparable observations make their tails meaningful; otherwise report raw ranges, case summaries, or qualitative evidence without invented precision.

**Performance Question**

Write the claim before collecting results:

> For candidate revision `[identity]`, does `[surface and invocation mode]` improve `[human outcome]` for `[workload classes]` relative to `[unchanged or alternative baseline]`, while preserving `[quality and guardrail contract]`, across `[declared environment and observation boundary]`, at an acceptable cost in `[human, machine, context, external, and maintenance dimensions]`?

The claim determines the workload, metrics, and conclusion. "Is the skill faster?" is insufficient because it omits outcome, baseline, quality, environment, and cost shifted downstream.

**Metric Families**

| dimension | start and stop boundary | include | interpretation warning |
| --- | --- | --- | --- |
| End-to-end elapsed time | From an eligible user need to an accepted result or safe fallback. | Waiting, retries, delegated work, verification, correction, and recovery required by the workflow. | Parallelism can reduce elapsed time while increasing aggregate work and cost. |
| User active effort | Time or steps requiring contributor attention, decisions, approvals, correction, or manual command execution. | Interruptions, clarification, repeated prompts, fallback, and review handoff. | Less interaction can mean smooth automation or concealed uncertainty. |
| Reviewer effort | From receipt of artifact to a correct next decision, including evidence lookup, correction, merge, and residual-risk assessment. | Independent verification and reconciliation of subagent outputs. | A polished artifact can be quick to read but costly to validate if evidence links are weak. |
| Machine execution | Runtime, startup, parsing, indexing, command, child process, network wait, and teardown by setup version. | Failed, timed-out, retried, and canceled runs. | Machine time alone omits human and external cost. |
| Context work | Sources planned, loaded, reused, duplicated, skipped, summarized, and reread; stable versus dynamic context where observable. | Progressive disclosure and checkpoint overhead that supports later tasks. | One-task overhead may repay across repeated tasks, so choose the intended horizon. |
| Tool and delegation work | Material tool actions, external calls, workers, child tasks, retry attempts, and reconciliation steps per accepted outcome. | Duplicate and intentionally independent verification classified separately. | Low tool count is not inherently good if it omits needed evidence. |
| Trigger overhead | Eligible-event latency, user interruption, non-intended activation, silent non-invocation, and work blocked by automatic behavior. | Startup and no-op cost for events that correctly match or do not match. | Execution-only measurements exclude false negatives and can reward broken triggers. |
| External and monetary cost | Approved service calls, quota, billable work, credential or audit operations, and data-transfer class where measured. | Retries, fanout, and fallback cost. | Do not infer price or billing without current measured records and policy-approved data. |
| Maintenance cost | Compatibility repairs, instruction changes, trigger tuning, plugin updates, credential rotation, incident response, ownership, and retirement work over the review horizon. | Costs shifted to tooling, security, service, or repository owners. | A short canary rarely captures long-term maintenance. |
| Outcome quality | Candidate-specific accepted result, missed required steps, supported claims, issue coverage, false findings, correction, and guardrail status. | Same rubric for baseline and candidate. | Never collapse quality and speed into one opaque score that can hide a hard failure. |

Report elapsed and aggregate cost when parallelism is used. Report outcome and guardrails beside every speed or cost result. Group retries under their originating workflow rather than giving each attempt a fresh success opportunity.

**Protocol**

1. Define the adoption decision and performance claim. State which result would retain, tune, narrow, replace, or retire the candidate.
2. Freeze candidate revision, repository revision, environment, dependencies, instruction set, allowed tools, external boundary, and evaluator rubric.
3. Select an unchanged or credible alternative baseline. Verify that it can complete the same accepted outcome.
4. Build representative workload strata: ordinary, edge, negative-trigger, failure, fallback, and high-consequence cases relevant to the candidate. State exclusions.
5. Preserve identical quality, source, authority, and completion gates across baseline and candidate. Do not let one path omit difficult checks.
6. Define start and stop events, attempts, retries, non-invocation, timeout, cancellation, partial output, and accepted result before measurement.
7. Decide whether cold startup, warm reuse, prompt or tool caching, repository indexing, network state, and learning are part of ordinary use. Measure or stratify them consistently.
8. Order or randomize paired cases where learning and sequence matter; state when exact replay is impossible.
9. Capture privacy-minimal raw observations sufficient to recompute summaries, including failed and excluded cases with reasons.
10. Run correctness and hard guardrail review before interpreting performance. A breached boundary stops the favorable performance claim.
11. Analyze variation, confounders, downstream work, and unobserved maintenance rather than reporting one average without context.
12. Save the scoped conclusion, residual uncertainty, expiry event, and resulting lifecycle decision.

For work spanning sessions, use the resumable journal and workload budgets to preserve the benchmark revision, completed strata, raw observation location, failed cases, and next run. The journal supports continuity; it does not improve benchmark validity by itself.

**Method Tradeoffs**

| method | best use | validity risk | completion evidence |
| --- | --- | --- | --- |
| Mechanism microbenchmark | Hook matcher, startup, local command wrapper, parsing, source lookup, or isolated tool overhead. | Omits user outcome, semantic quality, downstream effects, and portfolio interactions. | Repeated controlled observations plus environment, setup revision, and correctness of the mechanism. |
| End-to-end fixture replay | Stable repository workflow with reproducible inputs, accepted output, failure, and rollback. | Fixtures can be easier and cleaner than live work. | Baseline and candidate traces through the same gate, including failures and non-invocation. |
| Paired reviewer task | Guidance, review skill, or subagent output where semantic decision time matters. | Learning, order, and reviewer preference can bias the pair. | Stable rubric, source evidence, correction record, and order or independence notes. |
| Limited canary | Real users and workflow under bounded scope after static and failure gates. | Task mix and novelty confound results; rare failures may not appear. | Eligible opportunities, outcomes, guardrails, user effort, maintenance, and predefined expansion decision. |
| Trace bottleneck analysis | Complex tool, context, worker, or external dependency sequence. | Instrumentation can add overhead and expose data; a trace does not prove value. | Approved minimal trace with critical path, aggregate work, and independent outcome evidence. |
| Workload simulation | Fanout, scale, timeout, or rate behavior unsafe or rare in ordinary use. | Simulated services and tasks may not match real dependencies. | Scenario assumptions, controlled effects, invariant checks, and limited extrapolation. |
| Longitudinal lifecycle review | Compatibility, maintenance, owner burden, repeated correction, and retirement value. | Concurrent changes make attribution weak. | Versioned incidents, interventions, task mix, owner record, and bounded qualitative conclusion. |

Design the method from the decision backward. Do not run a microbenchmark merely because it is easy when the adoption question concerns reviewer quality and maintenance.

**Benchmark Integrity Checks**

- Include failed, timed-out, canceled, retried, partial, disabled, and expected-but-non-invoked workflows in the declared accounting.
- Record cache and startup state. A warm reused agent and a cold baseline are not a fair comparison unless that asymmetry is the ordinary intended workflow.
- Keep repository and task difficulty comparable. Stratify rather than averaging unrelated task classes.
- Measure reviewer correction, merge, and reconciliation when setup shifts work downstream.
- Separate wall-clock improvement from total compute, tool, service, and human effort.
- Detect censored data: a timeout is an outcome, not a missing observation to drop.
- Preserve configuration and environment identity so results from different versions are not combined silently.
- State network, service, model, user, and order variability that can change results.
- Avoid optimizing after seeing the same evaluation cases without holding out or refreshing representative tasks where feasible.
- Do not claim p50, p95, p99, throughput, cost, or scaling behavior when sample and measurement cannot support them.

**Setup-Specific Evaluation Sketches**

Hook: compare eligible edit workflows under native manual formatting and the candidate hook. Hold formatter output and policy constant. Include matching, non-matching, command failure, recursion, disablement, and fallback. Measure end-to-end edit interruption, trigger overhead, false work, state correctness, and owner intervention. Any unauthorized mutation defeats the performance result.

Skill: compare the existing guidance or manual procedure with explicit skill invocation across the same task strata. Hold required evidence and output rubric constant. Measure user active effort, clarification attributable to missing procedure, context loaded, tools, accepted output, reviewer correction, non-intended triggering, and maintenance of instructions. Fewer questions alone is ambiguous.

Subagent: compare one reviewer with delegated analysis on a frozen revision. Measure elapsed time, aggregate worker work, unique supported issue coverage, duplicate findings, reconciliation effort, merge conflicts, and final accepted outcome. Parallel wall time without merge and verification is incomplete.

Plugin: compare the existing portfolio with the exact component set, not the bundle label. Include startup, duplicate triggers, component outcomes, external calls, update and removal work, and residual state. Short execution can be outweighed by persistent overlap or maintenance.

MCP: compare approved manual or user-provided context with standing integration for recurring eligible tasks. Measure freshness, lookup effort, accepted source use, latency, calls, retries, credential operations, audit, fallback, and service-owner burden. External authorization and data boundaries remain hard gates.

**Worked Interpretations**

Good hook study: baseline and candidate process the same diverse edits to identical formatted output. The study records cold and ordinary warm conditions, eligible and non-eligible events, failures, rollback, contributor interruption, and state effects. Results support only the tested repository, formatter, event behavior, and canary expansion rule.

Bad subagent claim: three workers finish sooner on the clock than one reviewer, so the workflow is declared faster. Their total tool and context work triples, findings overlap, one assumption conflicts, and a maintainer spends longer reconciling them. The claim omitted the accepted-outcome stop boundary and aggregate cost.

Borderline skill result: sampled tasks show fewer clarifications and similar accepted output, but the candidate handled easier task classes after a documentation update. Preserve scope, freeze the new documentation state, stratify the next sample, and predeclare the conclusion rule instead of tuning prompts against the confounded result.

No-change win: a proposed plugin duplicates current commands and adds startup, updates, observability, rollback, and owner obligations without improving the accepted outcome. Rejecting it is a measurable performance improvement for the setup portfolio.

**Performance Audit**

A fresh reviewer should be able to:

1. reconstruct claim, baseline, candidate, workload strata, setup and environment revision, and quality gate;
2. verify start, stop, eligible opportunity, attempt, failure, retry, fallback, and accepted-result definitions;
3. recompute at least one summary from privacy-safe raw observations, including excluded cases and reasons;
4. confirm cache, startup, order, concurrency, network, tool, and reviewer conditions relevant to the claim;
5. inspect outcome parity, hard guardrails, and downstream correction before accepting speed or cost;
6. distinguish elapsed time from total human, machine, context, external, and maintenance work;
7. identify confounders, variation, unobserved tails, and unsupported extrapolation; and
8. reach the same scoped lifecycle decision without needing the original conversation.

Exact numeric repetition is not always possible with model, network, service, or human variability. Reproducibility means the protocol, observations, and decision boundary support the same bounded interpretation.

Use verified bottlenecks to change architecture carefully. Repeated source loading can justify progressive disclosure or cache-aware reuse; trigger overhead can favor explicit invocation; merge cost can reduce delegation; duplicate checks can justify portfolio consolidation. Preserve correctness and authority while optimizing. The conclusion expires after material candidate, repository, model, service, workload, policy, or owner-workflow change.

## Scale Boundary Statement

This reference is sufficient while one valid setup owner can decide, observe, contain, reverse, and retire the candidate's complete effect graph. Cross that boundary when systems, owners, automatic reach, data, credentials, production, concurrency, dependencies, recovery, or lifecycle obligations require authority and evidence the generic setup owner does not possess.

Scale is not a file, repository, user, or worker count. One small MCP configuration can be specialist-scale because it crosses credentials and external data; many read-only repositories can share a low-risk evaluation method. Classify the highest-consequence dimension and preserve the ability to move back down after discovery removes a suspected boundary.

**Scale Zones**

| zone | conditions | generic setup role | expansion boundary |
| --- | --- | --- | --- |
| Local | One rollout unit can independently accept and reverse the setup; one repository outcome; one valid owner; bounded local evidence; explicit or low-reach behavior; no new specialist boundary. | Own outcome, candidate selection, local authority, verification, trial, metrics, rollback, and retirement. | Move to coordinated when shared behavior, dependencies, users, owners, or replacement create cross-unit interaction. |
| Coordinated | Several rollout units or surfaces interact; shared automatic behavior; bounded external service; common policy with local variance; distributed evidence or implementation; or replacement across an existing portfolio. | Preserve one portfolio owner, common contract, staged cohorts, per-unit acceptance, dependency and overlap review, and selective rollback. | Move clauses to specialist owners when permission, production, data, security, compliance, incident, or independent-system authority controls them. |
| Specialist | Multiple independent systems or controlling domains; production or secret effects; unbounded source or service discovery; correlated failure beyond local recovery; or authority and observability not held by setup owners. | Contain, preserve the integration decision record, route exact clauses, and incorporate approved requirements and evidence. | Return only after controlling owners define authority, acceptance, observability, fallback, escalation, and residual risk. |

The rollout unit is the smallest scope that can independently approve, observe, disable, restore, and retire the setup. It may be one user, repository, service boundary, team, environment, or another policy-defined unit. Do not assume the repository is always the correct unit.

**Scale Dimensions**

| dimension | local evidence | pressure that changes the zone |
| --- | --- | --- |
| Outcome and policy | One observable outcome and one applicable local decision. | Several outcomes, organization-wide invariant, or policy whose owner differs from implementation. |
| User and automatic reach | Explicit invocation or bounded canary with local fallback. | Shared default, automatic trigger, broad interruption potential, or users unable to opt out safely. |
| Systems and data | Local repository and commands inside one approved boundary. | External service, cross-system workflow, data classification, retention, or destination ownership. |
| Credentials and production | No new secret or production authority. | Shared tokens, privilege, deployment, production traffic, incident, compliance, or security consequence. |
| Ownership | One decision, maintenance, and recovery owner. | Independent owners can accept or reject different clauses, or one central owner cannot operate local recovery. |
| Configuration variance | One compatible command and setup behavior. | Repository, language, policy, environment, or runtime differences require local adaptation. |
| Dependency coupling | Local dependencies and isolated failure. | Shared service, package, command, credential, event, or owner creates correlated blast radius. |
| Observability | Opportunity, effect, failure, fallback, and owner action visible in the unit. | Cross-process traces, inaccessible audit, unknown downstream effect, or no selective health signal. |
| Reversibility | One local disable restores a tested native workflow. | Migration, shared credential revocation, global shutdown, data remediation, or residual components. |
| Evidence and context | Ranked lineages and decision-linked source set remain bounded. | Unbounded discovery, incompatible source domains, context drift, or relevance requiring specialist graphs and owners. |
| Concurrency | One owner per writable artifact with simple reconciliation. | Parallel agents or teams share control-plane files, assumptions, rollout state, or merge queues. |
| Lifecycle | Local owner can refresh and retire the item. | Common templates, cohorts, compatibility matrix, support rotation, migration waves, or long-lived external obligations. |

**Default Expansion Model**

1. Start with no change as a real option and define the unchanged repository workflow.
2. Select one representative local rollout unit with an owner and a meaningful but containable workload.
3. Use the least-authority surface, explicit invocation where feasible, and a tested native fallback.
4. Pass local source, compatibility, positive, negative, forced-failure, rollback, outcome, observability, and owner-response gates.
5. Identify which evidence is stable invariant and which is local configuration, permission, command, data, or user workflow.
6. Create the next cohort from a meaningful variant, not merely another identical easy unit.
7. Require each unit's owner to accept the applicable authority, fallback, and lifecycle duties.
8. Test a shared-dependency failure and selective disablement before broad automatic rollout.
9. Advance, hold, shrink, adapt, federate, or stop from predeclared evidence; never expand because installation itself succeeded.
10. Preserve versioned inventory and a way to retire or roll back by cohort and unit.

Organization-wide policy can require a different rollout model, but that policy and its controlling process must supply authority, service objectives, change management, incident response, and acceptance. Generic setup guidance cannot self-authorize production reach.

**Scale Topologies and Tradeoffs**

| topology | use when | risk | required control |
| --- | --- | --- | --- |
| Local per-unit setup | Commands, users, permissions, and workflows vary materially. | Configuration drift and duplicated maintenance. | Shared decision and verification schema, local owner, version inventory, and periodic divergence review. |
| Reusable template with local parameters | Outcome and behavior are stable while commands, paths, or thresholds vary predictably. | Template upgrade can overwrite local policy or hide unsupported variants. | Declared extension points, compatibility cases, local diff review, pinning, migration, and rollback. |
| Central policy with federated execution | One controlling invariant applies, but units own implementation and recovery. | Ambiguous precedence or uneven enforcement. | Policy owner, unit acceptance, evidence reporting, exception path, and conflict resolution. |
| Central shared control | Behavior, authority, dependency, support, and rollback truly belong to one central owner. | Correlated interruption, global credential or event failure, and local loss of control. | Service-level governance, canaries, health and guardrail telemetry, capacity, selective kill scope, incident response, and local fallback. |
| Opt-in capability | Demand and local fit vary, and absence is safe. | Biased adoption evidence and incompatible self-service configurations. | Eligibility contract, safe defaults, local validation, inventory, support, and removal. |
| Manual guidance or no automation | Outcome is infrequent, variance is high, authority is consequential, or setup cost exceeds benefit. | Inconsistent execution and slower work. | Clear source-labeled procedure, responsible owners, and revisit triggers. |
| Specialist service or process | Production, security, data, compliance, or independent-system behavior dominates. | Handoff latency and context fragmentation. | Exact integration contract, domain authority, evidence return, escalation, and setup fallback. |

Centralize stable invariants and reusable evaluators more readily than exact commands, credentials, or automatic configuration. Reasoning and rollback contracts often travel farther than implementation details.

**Distributed Execution**

- Split by independent outcome, source domain, rollout unit, or artifact with one writable owner; do not split merely because many files exist.
- Freeze shared assumptions, candidate revision, policy, and evaluation schema before parallel work.
- Permit read-only evidence work in parallel when scopes are separable. Route writes through the owner of each control-plane artifact.
- Use a merge or reconciliation owner who can reject incompatible returns and rerun integration gates.
- Preserve cohort, dependency, and lifecycle state in a shared inventory; avoid relying on worker conversations as the source of truth.
- Apply backpressure when workers use different revisions, request overlapping writes, broaden authority, or consume the verification reserve.
- Treat merge-queue and reviewer capacity as rollout limits; faster generation cannot compensate for unreviewed shared controls.

For long-running work, context drift is a reliability failure. Save exact revision, owner, cohort, open risks, changed paths, evidence, and first unmet gate. Reread them before shared configuration, external calls, destructive action, rollout advancement, or completion.

For large codebases, narrow by source lineage, dependency, ownership, configuration, and effect graph when those relationships control relevance. Verify decisive graph paths against source and retain negative or conflicting evidence. A long unranked source list is not context strategy.

**Scale Failure Signals**

| signal | implication | response |
| --- | --- | --- |
| Local variants require repeated exceptions or copied patches. | Shared template or policy does not represent actual invariants. | Stop rollout, classify variance, localize configuration, or abandon centralization. |
| One update causes simultaneous failures across otherwise independent units. | Shared dependency or rollout cohort creates correlated blast radius. | Halt expansion, use selective disablement, test dependency loss, and redesign isolation. |
| A unit cannot disable without central intervention. | Rollout unit lacks real reversibility. | Restore local fallback and redesign kill scope before further scale. |
| Shared credentials or external service scope grow with user count. | Authority and data boundary are scaling without equivalent ownership and audit. | Pause, route to service and security owners, narrow credential and tool scope, and test revocation. |
| Central owner cannot review changes or respond to red signals. | Governance and support capacity lag rollout. | Hold or shrink cohorts, federate ownership, or retire automatic scope. |
| Portfolio inventory cannot identify active version, owner, trigger, dependency, or rollback per unit. | Selective diagnosis and retirement are impossible. | Freeze rollout and reconcile inventory from actual configuration and behavior. |
| Parallel agents edit the same setup files or rollout state. | Work decomposition creates control-plane races. | Stop writes, restore one owner, reconcile revisions, and rerun gates. |
| Aggregate metrics look healthy while one variant repeatedly fails. | Central averages hide local consequence. | Stratify by meaningful unit and failure class; contain the affected cohort. |
| The setup needs ever-larger context to choose ordinary behavior. | Policy, routing, or surface boundaries are too coupled. | Simplify, split stable domains, improve progressive disclosure, or choose a smaller control. |

**Worked Scale Decisions**

Good expansion: a formatter control proves idempotent, visible, reversible behavior in one repository. The next cohort uses the same policy but a different command variant and owner. A parameterized template keeps local commands explicit, each unit can disable independently, and shared dependency loss is tested before broader automatic use.

Bad expansion: an official-looking plugin is copied across repositories with one shared credential and no component inventory. Local owners cannot disable it, and one update activates overlapping hooks everywhere. Stop rollout, revoke unnecessary access, restore local controls, inventory residual state, and route shared service and security clauses to their owners.

Borderline expansion: a review-skill template is useful in one repository, but trigger behavior and contributor workflow differ elsewhere. Share the decision schema, examples, and evaluator while keeping automation local and disabled. Each owner qualifies trigger, commands, output, and fallback before opting in.

Good scale-down: maintenance and overlap increase while a repository-native command now covers the original outcome. Retire the shared setup by cohort, verify native fallback, remove triggers and credentials, update inventory, and retain concise rationale. Scale-down is an ordinary lifecycle success, not an admission that the original pilot was wrong.

**Scale Readiness Review**

Before advancing a cohort, verify:

1. rollout-unit inventory includes exact version, owner, authority, dependencies, enablement, health, fallback, and retirement state;
2. the invariant and local variation are explicit, with no hidden copy-pasted assumptions;
3. each owner has accepted permissions, data, automatic reach, observation, support, and recovery duties;
4. local behavior and outcome gates pass on meaningfully diverse variants;
5. shared dependency, correlated failure, version skew, and capacity are exercised or bounded by specialist evidence;
6. selective disablement, rollback, and native fallback work without global interruption;
7. observability can detect and stratify local, cohort, and shared failures without unsafe data collection;
8. distributed edits, rollout changes, and inventory updates have deterministic ownership and merge verification;
9. support and reviewer capacity can respond to red signals throughout the proposed scope; and
10. advance, hold, shrink, federate, route, or stop criteria are recorded before seeing the next results.

Pilot success does not prove organization-wide reliability. State the observed variants, untested combinations, shared dependencies, and expiry conditions. The safest scalable asset may be a common evaluation, evidence, and rollback contract rather than a common automatic control.

## Future Refresh Search Queries

No browsing was performed during this evolution. Every locator and query in this section is a future research plan, not evidence of current contents, availability, support, compatibility, security, or value. Execute a query only when browsing is permitted and a freshness-sensitive fact can reverse a setup decision.

Begin with the exact claim, not a general request for best practices. Record the installed or target environment, the local evidence gap, the possible actions for each answer, and the setup clauses that depend on it. If local source, current installed help, implementation behavior, repository policy, or a responsible owner already decides the claim, do not browse merely to add links.

**Refresh Triggers**

- A candidate depends on a current event, matcher, field, package, plugin, server, tool, transport, model, permission, or installation behavior.
- Installed behavior contradicts the local corpus or a saved configuration.
- A release, migration, deprecation, security notice, ownership change, or source update can invalidate adopted setup.
- A package, server, or public source becomes unavailable, unmaintained, forked, archived, or license-ambiguous.
- A reliability, retry, failure, or observability event suggests that current product semantics changed.
- A planned rollout adds a new environment, version, user group, data class, credential, or production boundary.
- A review or retirement decision requires evidence that the original capability still exists and remains appropriate.

**Claim-Driven Query Templates**

Replace the bracketed concepts with actual values before searching. Confirm the current official product domain rather than assuming a historical domain remains authoritative.

| claim family | future query intent and template | preferred evidence | decision changed by result |
| --- | --- | --- | --- |
| Surface taxonomy | `official Claude Code documentation hooks skills subagents plugins MCP definitions [target-version]` | Current primary overview plus linked surface-specific documentation and installed behavior. | Keep, narrow, or revise the surface comparison and adjacent routing. |
| Settings and scope | `official Claude Code settings configuration scope project user organization [field-name] [target-version]` | Primary schema and precedence documentation, migration note, and local validation. | Decide placement, authority, sharing, and rollback of configuration. |
| Hook events and matchers | `official Claude Code hooks [event-name] matcher exit timeout failure behavior [target-version]` | Primary event contract, release or migration history, and safe local positive plus negative case. | Adopt, adapt, pause, or retire an automatic hook candidate. |
| Hook migration or deprecation | `Claude Code release notes hook [event-or-field] deprecated migration replacement [current-version]` | Dated primary release note, old and new contract, compatibility range, and rollback implication. | Mark old example stale, update migration and regression cases, or preserve a pinned legacy path. |
| Skill structure and trigger | `official Claude Code skills metadata trigger progressive disclosure [field-name] [target-version]` | Current primary structure, installed validator or help, and intended plus non-intended trigger behavior. | Validate skill packaging, narrow trigger guidance, or fall back to documentation. |
| Subagent behavior | `official Claude Code subagents tools permissions context isolation [target-version]` | Primary behavior and permission docs plus local scope, merge, and evaluator cases. | Decide whether delegation is compatible and sufficiently isolated. |
| Plugin inventory and compatibility | `official Claude Code plugins marketplace [package-name] contents version compatibility manifest` | Official package or marketplace record, exact versioned manifest, maintainer, component inventory, and removal behavior. | Install nothing until inventory supports adopt, adapt, replace, or reject. |
| Plugin update and removal | `[package-name] official changelog migration uninstall remove hooks skills MCP [version]` | Versioned release or migration record and local residual-state test. | Plan safe update, rollback, replacement, or retirement. |
| MCP transport and configuration | `official Claude Code MCP [server-or-transport] configuration authentication tools [target-version]` | Primary product and server documentation, exact tool inventory, transport and auth contract, and compatible local case. | Define or reject integration mechanics without inferring need or permission. |
| MCP data and credential scope | `[server-name] official documentation least privilege read only tools data retention audit revocation` | Service-owner security and auth documentation, approved local policy, audit, and revocation test. | Establish a bounded external contract or keep the integration absent. |
| Permissions and safety | `official Claude Code permissions allowed tools deny rules sandbox external access [target-version]` | Current primary permission semantics, precedence, known limitations, and local boundary tests. | Narrow authority, add guardrail cases, or reject automatic or external setup. |
| Current package or server status | `[exact-name] official repository release supported Claude Code [target-version] archived deprecated` | Owner-controlled repository or registry record, signed or tagged release where available, maintenance and archival state. | Reclassify availability and maintenance; remove unsupported recommendations. |
| Error or incompatibility | `"[exact-error-fragment]" [surface-name] [target-version] official issue release note` | Primary docs first, then owner repository issue or implementation evidence tied to version. | Distinguish stale guidance, defect, configuration error, or unsupported environment. |
| Security notice | `[exact-component] official security advisory credential data exposure [version-range]` | Controlling advisory and organization security process. | Contain, patch, disable, revoke, migrate, or retire under specialist authority. |
| Maintained implementation example | `[surface-name] [specific-behavior] official repository example [target-version]` | Version-pinned owner implementation with license and local compatibility test. | Inform mechanics only; it cannot grant policy authority or prove outcome value. |
| Community contrast | `[specific-decision] Claude Code [surface-a] versus [surface-b] [target-version]` | Maintained source with author, date, version assumptions, direct passages, and contrary primary sources. | Clarify alternatives or discover edge cases; keep claims provisional until primary or local evidence supports them. |

Do not execute all templates. Select the smallest query that can settle the next claim. Search snippets, generated summaries, landing-page labels, popularity, and result count are discovery signals, not evidence.

**Existing Cataloged Leads**

| locator | inherited role | current status and future use |
| --- | --- | --- |
| `https://github.com/davepoon/buildwithclaude` | Cataloged ecosystem collection. | Unrefreshed. If permitted, inspect a pinned revision, owner, relevant path, license, maintenance, and exact example only for discovery or comparison. It cannot establish supported behavior or repository authority. |
| `https://github.com/Cranot/claude-code-guide` | Cataloged community guide. | Unrefreshed. If permitted, capture commit or release, chapter, author context, version assumption, relevant passage, contradiction, license, and local compatibility. |
| `https://www.claudedirectory.org/blog/claude-code-skills-vs-subagents-vs-mcp` | Cataloged concept-comparison article. | Unrefreshed. If permitted, verify publication and update metadata, taxonomy, product assumptions, author basis, contrary sources, and installed behavior before using it as explanatory support. |

These three URLs are known locators only. Their present contents and maintenance have not been verified. An unavailable, moved, copied, archived, injected, incompatible, or license-unclear source remains discovery, stale, negative, or unresolved evidence and cannot support adoption.

**Source Selection**

| evidence need | preferred source | what it cannot establish alone |
| --- | --- | --- |
| Supported product behavior | Current primary documentation for the applicable version and surface. | Local compatibility, organization permission, edge-case reliability, or workflow value. |
| Product change over time | Primary release notes, migration guide, deprecation notice, or version history. | Whether the local environment completed migration or intentionally remains pinned. |
| Concrete implementation | Owner repository code, versioned example, manifest, tests, or installed help and behavior. | Official support, policy authority, security posture, or universal best practice. |
| Package or service status | Owner-controlled package, registry, marketplace, repository, or service record. | Suitability, component trust, least privilege, or local need. |
| Security and data boundary | Controlling advisory, service security and auth docs, organization policy, and responsible owner. | Full absence of risk or local implementation correctness. |
| Operational edge case | Maintainer issue, discussion, incident note, or community report with reproducible version context. | Generality, authority, or correctness without primary and local corroboration. |
| Local applicability | Installed validation, safe behavior fixture, repository command and policy, and owner decision. | Broader product guarantees beyond the tested environment. |
| Reproducible historical premise | Pinned or hashed snapshot with provenance and reuse rights. | Currentness after its capture boundary. |

Use distinct sources for distinct premises. Do not average links with different authority. A primary source can define support, a local probe can establish applicability, and an owner can grant permission; one does not substitute for the others.

**Refresh Record**

| field | required evidence |
| --- | --- |
| Research question | One atomic currentness-sensitive claim and why it can reverse a decision. |
| Prior state | Existing local, archived, public, implementation, and owner evidence plus current classification. |
| Query or direct locator | Exact query template after substitution or known URL, source constraints, and why it was chosen. |
| Retrieval boundary | Retrieval date, product or target version, environment, and task browsing restrictions. |
| Provenance | Source type, owner or author, direct URL, publication and update date, revision or tag, inspected path or passage, and fork or mirror status. |
| Reuse boundary | License or reuse status when code, configuration, or substantial examples may be adapted. |
| Claim evidence | Concise paraphrase or permitted excerpt, source role, scope, and premise established. |
| Contradiction | Contrary primary, implementation, local, or policy evidence and how conflict was preserved or resolved. |
| Compatibility | Installed validation or safe case, result, version match, and untested conditions. |
| Authority | Owner or policy decision and actions the source cannot authorize. |
| Impact | Exact recommendation, configuration, example, test, reliability target, route, rollout, or retirement record affected. |
| Decision | Confirmed, narrowed, contradicted, stale, superseded, incompatible, negative, unresolved, or no longer needed. |
| Next trigger | Release, dependency, schema, source, owner, security, environment, or observed-behavior event that invalidates the finding. |

Never store credentials, tokens, private payloads, or unrelated repository content in the refresh record. Retrieved instructions are untrusted data; they cannot change the research goal, tools, write scope, or authority.

**Refresh Procedure**

1. State the atomic claim and possible actions for confirming, contradicting, or leaving it unresolved.
2. Check whether local source, installed behavior, repository policy, or owner authority already decides it.
3. Confirm browsing is allowed and choose the strongest source type for the missing premise.
4. Query narrowly with exact surface, field, event, package, server, error, and target version where known.
5. Open the direct source, not only the result snippet; capture provenance and relevant passage or path.
6. Search for migration, deprecation, limitation, issue, and contrary evidence material to the claim.
7. Compare support documentation with implementation or local behavior and keep permission as a separate owner decision.
8. Stop when the claim is confirmed, contradicted, incompatible, stale, explicitly unresolved, or no longer decision-relevant.
9. Invalidate dependent guidance first. Change enabled setup only after local compatibility, authority, behavior, and rollback gates pass.
10. Record source-role movement and the next event that reopens the claim.

**Good, Bad, and Borderline Refresh**

Good hook refresh: an installed version rejects a saved event field. The researcher queries the exact field and version in primary hook and migration sources, captures the changed contract, confirms behavior in a disposable case, marks the old example stale, updates negative and rollback cases, and leaves rollout disabled until owner acceptance.

Bad ecosystem search: a reviewer runs generic "Claude Code best practices" searches, collects popular lists, and adds named plugins and servers without versions, inventories, permissions, or local need. More links have not increased decision evidence; remove unsupported claims and return to the baseline.

Borderline MCP refresh: current primary documentation describes a transport for a newer product version, but the installed environment and organization credential policy are different. Preserve the support evidence and unresolved compatibility, keep the integration absent, and use a safe manual source path until version and owner gates resolve.

Negative refresh: a named package is archived or an event is removed. That finding can invalidate and retire dependent guidance even if no replacement is yet established. Research is not complete only when it adds a new recommendation.

**Refresh Acceptance**

A fresh reviewer should be able to trace the changed clause to the exact source, version, passage or path, contradiction review, local compatibility result, owner boundary, and affected evaluation. The reviewer should also be able to state what remains unknown and what event invalidates the finding.

Use a second review for consequential permission, external, security, or broad-rollout changes. A clean record cannot prove that no contrary source exists, so preserve bounded uncertainty. If a source changes, propagate invalidation through dependent setup, tests, examples, reliability contracts, rollout units, and retirement decisions; do not silently update enabled behavior.

Maintain query vocabulary as product terminology evolves. Repeated refresh history becomes a temporal index: it can show which premises are stable, which are volatile, which sources repeatedly conflict, and which obsolete claims should be removed rather than rediscovered. That index reduces future search cost without pretending historical evidence is current.

## Evidence Boundary Notes

Evidence category, compatibility, and authority are separate dimensions. A statement can be true in current official documentation but incompatible with the installed environment. An owner can authorize a local action without proving a product claim. A local behavior case can establish applicability without granting organization policy authority. Keep these distinctions visible for every recommendation-changing premise.

The three inherited labels remain valid when used narrowly:

- `local_corpus_sourced_fact`: a claim directly supported by an inspected local passage, file property, hash, path, or behavior observation at a named revision and environment.
- `external_research_sourced_fact`: a claim directly supported by a retrieved public source with provenance, version, relevant passage or path, and a stated retrieval boundary.
- `combined_evidence_inference_note`: a synthesis whose local and external premises are separately traceable and whose reasoning, uncertainty, and local applicability are explicit.

During this evolution no public source was opened. Therefore, the three cataloged URLs and all future queries are locators or plans, not `external_research_sourced_fact` evidence.

**Complete Evidence Vocabulary**

| category | meaning | what it can support | what it cannot support alone |
| --- | --- | --- | --- |
| `direct_user_instruction` | An explicit current request, constraint, permission, prohibition, priority, or desired outcome from the user. | Task scope and actions the user is authorized to decide. | Product behavior, organization authority the user does not hold, or correctness of implementation. |
| `organization_or_repository_policy` | A controlling policy, repository instruction, ownership rule, security boundary, or accepted process with applicable scope. | Local authority, required controls, escalation, and acceptance criteria. | Current product mechanics or empirical effectiveness. |
| `local_corpus_sourced_fact` | An atomic claim supported by inspected local source or file evidence. | What the corpus says, file identity, source purpose, and bounded historical guidance. | Present external behavior, permission, universal value, or compatibility after drift. |
| `installed_behavior_observation` | An observed result from the applicable local runtime, configuration, command, or safe behavior case. | Compatibility and behavior under the exact tested revision, environment, inputs, and authority. | General support across versions, absent edge cases, or policy permission. |
| `external_research_sourced_fact` | An atomic claim supported by a retrieved external source with direct provenance and version boundary. | Public product support, change history, package status, implementation example, or service premise within source scope. | Local applicability, organization permission, source completeness, or workflow value. |
| `owner_decision_record` | A named responsible owner accepts, rejects, pauses, scopes, or escalates a decision. | Authority and residual-risk acceptance inside that owner's domain. | Truth of technical facts outside the owner's evidence or authority. |
| `measured_outcome_observation` | A result from a declared workload, candidate revision, evaluator, metric, sample, and observation period. | Behavior, cost, or value within observed conditions. | Causality without comparison, unseen tails, other environments, or permanent reliability. |
| `combined_evidence_inference_note` | Reasoned conclusion combining separately classified premises. | Surface fit, tradeoff, likely consequence, or a bounded recommendation. | Certainty beyond premises, hidden assumptions, or permission not independently supplied. |
| `working_hypothesis` | A plausible explanation or candidate claim awaiting discriminating evidence. | Safe read-only investigation and test design. | Adoption, authority expansion, or confident final guidance. |
| `negative_or_stale_evidence` | A failed case, superseded passage, incompatible example, removed capability, or historical warning with cause. | Rejection, containment, migration, regression cases, and prevention of rediscovery. | Current positive behavior or universal prohibition outside its scope. |
| `conflicting_evidence` | Applicable evidence sources or authorities imply incompatible actions and the conflict is unresolved. | A completion block, owner escalation, and comparison plan. | Choosing either action by vote, recency, confidence tone, or source count. |
| `unknown_or_silent` | Relevant support, compatibility, authority, outcome, or owner answer is absent or not observed. | A bounded pause, safe fallback, explicit research question, or route. | Approval, rejection, safety, currentness, or a guessed default. |

One claim may have several dimensions but should not inherit the strongest label from a neighboring clause. Split mixed sentences. For example: "The local hook reference names an event, the event is currently supported, and the repository should enable it" contains a local corpus fact, a freshness and compatibility claim, and an owner-dependent recommendation. Each needs separate evidence.

**Claim Record**

| field | completion rule |
| --- | --- |
| Claim identifier and text | One atomic, falsifiable or decision-relevant statement; avoid combining source content, compatibility, permission, and value. |
| Evidence category | Select the primary category above and list additional dimensions without label inflation. |
| Locator or record | Exact local path and passage, external URL and revision, behavior case, owner decision, or measurement artifact. |
| Source role | Primary, supporting, provisional, negative, duplicate, conflicting, stale, superseded, or silent for this claim. |
| Observation and freshness | Date or revision, applicable product and repository version, environment, and event that invalidates the evidence. |
| Compatibility | Confirmed, contradicted, untested, partially tested, version-mismatched, or not applicable, with evidence. |
| Authority | Who can decide the resulting action, which scope was accepted, and which actions remain outside permission. |
| Inference | Premises, reasoning, alternatives, assumptions, causal limitations, and counterargument where synthesis is used. |
| Confidence and unknowns | What is directly known, what remains judgment, unobserved conditions, and evidence that can overturn the claim. |
| Allowed action | Inform, investigate, recommend, pause, block, trial, adopt, disable, restore, route, replace, retire, or no change. |
| Dependents | Guidance, configuration, cases, reliability targets, rollout units, credentials, owners, and lifecycle records invalidated if the claim changes. |

Keep one authoritative evidence ledger and link it from concise prose. Inline labels are useful for consequential claims, but duplicating full provenance throughout the reference creates drift. Deterministic identity, existence, schema, and link checks can be automated; semantic support, authority, synthesis, and residual risk require human review.

**Classification Procedure**

1. Split the statement into atomic content, currentness, compatibility, authority, outcome, and recommendation claims.
2. Identify direct user and controlling repository or organization instructions before secondary sources.
3. Locate the exact supporting passage, behavior case, owner record, or measurement rather than relying on a heading, path name, snippet, or confident paraphrase.
4. Determine source lineage so current/archive duplicates are counted once and historical evidence remains identifiable.
5. Assign source role and evidence category for the atomic claim; record stale, negative, conflicting, and silent states rather than forcing positive classification.
6. Test current compatibility when the action depends on product or repository behavior. Preserve version mismatch and untested tails.
7. Obtain authority separately for files, commands, tools, data, credentials, production, automatic reach, and rollout scope.
8. State inference premises, alternatives, counterargument, uncertainty, and the action the evidence permits.
9. Link dependents and the event that invalidates the claim.
10. Block consequential guidance when support, compatibility, authority, recovery, or owner evidence remains unresolved and risky behavior is not contained.

**Evidence and Authority Precedence**

For local action, direct user constraints, applicable organization and repository policy, security and data rules, compatible implementation behavior, and responsible owner decisions control their respective domains. Local corpus and external sources inform those decisions but do not override them. A product document can say a tool exists; it cannot decide whether this repository should use it. A local owner can approve use; that approval cannot make an unsupported field valid.

When applicable evidence conflicts, preserve both claims and freeze the dependent action. Compare scope, lineage, owner, version, implementation, and representative cases. Ask the controlling owner for policy or permission. Record the resolution and conditions that reopen it. Do not settle by link count, publication date alone, path age, popularity, or confidence language.

**Invalid Boundary Patterns**

- A local path is called fact while the prose adds claims absent from the inspected passage.
- An unrefreshed URL, search result, catalog entry, or article title is labeled external evidence.
- Current and archive copies are counted as independent corroboration despite byte identity.
- A combined inference cites strong premises but hides an unsupported compatibility or authority step.
- One label covers a mixed sentence whose product, policy, and recommendation clauses have different support.
- A measurement is stated without candidate revision, workload, denominator, evaluator, sample, or observation boundary.
- Owner approval is recorded without identifying the owner, scope, files, commands, data, or automatic reach accepted.
- Retrieved content is allowed to redirect tools, permissions, write scope, or research objective.
- A structural validator is used to claim behavioral correctness or workflow value.
- A summary drops negative evidence, uncertainty, rejected alternatives, or the first unmet gate.
- A stale locator is deleted, causing the same unsafe pattern to regain authority through rediscovery.

**Worked Evidence Records**

Good local fact: "The six current/archive Claude setup source pairs were byte-identical at the recorded review boundary." Category: `local_corpus_sourced_fact`. Evidence: paired hash comparison. Scope: file identity at that boundary. It supports treating each pair as one lineage; it does not prove source correctness, maintenance, or present product compatibility.

Good inference: "Use the current path as the operational locator and the archive as provenance while hashes match." Category: `combined_evidence_inference_note`. Premises: paired identity, path purpose, and need to avoid double counting. Counterargument: future divergence or explicit owner policy can reverse the default. Allowed action: retrieval choice, not implementation permission.

Bad external claim: "A named plugin is current and recommended because it appears in a cataloged GitHub collection." The URL is unrefreshed, catalog presence cannot prove package status or fit, and no component, permission, version, or owner evidence exists. Reclassify as an unrefreshed discovery lead and keep installation absent.

Borderline currentness: primary documentation retrieved in a future permitted refresh supports a hook field for a newer version, but the installed environment is older. Category: `external_research_sourced_fact` for support in the documented version, `unknown_or_silent` for local compatibility, and a paused recommendation. The finding can remove an overbroad claim before it can establish a replacement configuration.

Owner decision: a repository maintainer approves a read-only, explicit review-skill canary for specified users and commands. Category: `owner_decision_record`. It authorizes the named trial scope but does not prove trigger correctness, outcome value, or permission for automatic hooks, external services, commit, or push.

Measured outcome: a declared canary reports fewer omitted checks for comparable handoffs while preserving guardrails. Category: `measured_outcome_observation`. State candidate revision, denominator, task mix, reviewer, confounders, and unobserved tails. It may support bounded adoption; it does not prove universal improvement.

**Evidence Audit**

Sample both directions:

- Backward trace starts from a recommendation, configuration, permission, reliability target, or completion claim and reaches atomic premises, locators, source roles, compatibility, owner authority, behavior, measurement, and uncertainty.
- Forward trace starts from a changed, contradicted, stale, or revoked premise and reaches every dependent setup item, example, case, credential, rollout unit, owner, observation, and lifecycle state.

For a final audit:

1. Verify consequential claims have categories and stable evidence identifiers.
2. Inspect whether the cited passage or behavior actually supports the claim at its stated scope.
3. Confirm duplicate lineages are counted once and negative or stale evidence retains its cause.
4. Separate current support, installed compatibility, local authority, and measured value.
5. Scan synthesis for hidden premises and meaningful counterarguments.
6. Reconcile conflicts and block unresolved consequential actions.
7. Check versions, dates, environment, owners, and invalidation events.
8. Follow one changed premise forward through guidance, configuration, verification, rollout, and retirement.
9. Ask a fresh reviewer to reconstruct the decision, excluded actions, residual uncertainty, and first unmet gate without the original conversation.
10. Verify compaction and handoff preserve constraints, negative evidence, and overturn conditions rather than only the favored conclusion.

Automation can verify file identity, label presence, field shape, links, and invalidation references. It cannot decide semantic entailment, policy authority, acceptable risk, or generalization. Use independent human review where those judgments can authorize consequential behavior.

**Current Evidence Status**

Known at this review boundary: the working seed began with 26 headings; the six local current/archive source pairs were inspected and byte-identical within each pair; the local source wording and paths were available; the three public locators were inherited; and no browsing occurred during this evolution.

Bounded judgment: the claim-scoped hierarchy, surface tradeoffs, artifact design, workload classes, reliability contracts, failure taxonomy, retry policy, observability model, performance method, scale zones, and evidence architecture are reasoned guidance derived from the local corpus and systems practice. They require repository-specific evaluation and owner acceptance.

Unknown or refresh-dependent: present public-source contents, current product schemas and events, named package or server availability, marketplace status, external maintenance, universal outcome value, organization policy not supplied here, and compatibility outside observed local cases.

Confidence is granular. The file can pass structural and packet verification while a product claim remains provisional, a compatibility case remains unrun, or an owner decision remains blocked. Evidence boundaries are the setup control plane's memory model: they determine which facts persist, which claims expire, what context future agents load, and which actions remain impossible until support, compatibility, and authority converge.
