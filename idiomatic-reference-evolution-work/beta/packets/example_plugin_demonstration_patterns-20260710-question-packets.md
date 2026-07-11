## Section 001: Example Plugin Demonstration Patterns
### Question 01: What decision does this reference help make?
- **current_section_observation:** The title says example plugin, while the only local artifact is a standalone `SKILL.md` that demonstrates model-invoked guidance rather than a complete installable plugin.
- **supporting_reason:** The reference should help a builder choose the smallest demonstrable extension surface and decide which lifecycle claims the available evidence can actually support.
- **counterargument_or_limit:** A target platform may require every skill to live inside a packaged plugin even when the teaching focus is the skill itself.
- **assumptions_and_boundaries:** Separate the capability surface from its distribution wrapper and verify both only when the target environment supplies both contracts.
- **revision_decision:** Open with an evidence-bounded demonstration method centered on a skill, then route commands, hooks, MCP, settings, manifests, installation, and removal to conditional companion work.
- **additional_insight_to_add:** A demonstration is copied more often than prose, so every omitted boundary and permissive default can become an inherited production assumption.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** No opening sequence defines user request, trigger, minimal files, expected behavior, negative behavior, verification, or cleanup.
- **supporting_reason:** A smallest runnable teaching slice makes one capability, one invocation mechanism, one expected observation, and one failure path easy to inspect and reproduce.
- **counterargument_or_limit:** A documentation-only fixture can still be useful when the required host runtime is unavailable.
- **assumptions_and_boundaries:** Label static inspection separately from executed installation and invocation evidence.
- **revision_decision:** Recommend capability contract, surface choice, minimal artifact, deterministic example, positive and negative trigger checks, lifecycle proof, and handoff in that order.
- **additional_insight_to_add:** The example should make the first successful path short while keeping optional complexity visibly outside the baseline.
### Question 03: When does the default work well?
- **current_section_observation:** The title provides no fit conditions for a skill-focused demonstration.
- **supporting_reason:** The local pattern fits model-invoked contextual guidance with a narrow domain, recognizable requests, no required external side effect, and inspectable Markdown support material.
- **counterargument_or_limit:** User-invoked commands, event-driven hooks, service integrations, and permissioned tools have different invocation and failure contracts.
- **assumptions_and_boundaries:** Use this opening directly for a skill and retain it as a demonstration-quality layer when a broader plugin wrapper is later proven necessary.
- **revision_decision:** State direct-fit conditions and explicit reroute triggers before any file tree is prescribed.
- **additional_insight_to_add:** A capability can be simple in code yet require broader evidence when activation is implicit and overlap with neighboring triggers can surprise users.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The seed role scenario implies install, permissions, invocation, and removal even though none of those behaviors appears in the mapped local corpus.
- **supporting_reason:** Claiming a complete plugin lifecycle from a skill template would make an illustrative directory look operationally verified.
- **counterargument_or_limit:** Another target repository may contain a manifest, installer, or host-level plugin contract not present in this corpus.
- **assumptions_and_boundaries:** Discover and inspect those artifacts before extending the demonstration's claims.
- **revision_decision:** Add stop conditions for unknown host, unsupported packaging, unowned permissions, nondeterministic side effects, and absent uninstall behavior.
- **additional_insight_to_add:** A demonstration should fail closed on capabilities it cannot prove rather than silently suggesting that the host will supply missing lifecycle behavior.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The title collapses skill, command, hook, MCP server, setting, and plugin manifest into one apparent extension category.
- **supporting_reason:** These surfaces differ in who invokes them, when they run, what context they receive, which permissions they need, and how failures are recovered.
- **counterargument_or_limit:** A real plugin can combine several surfaces behind one user goal.
- **assumptions_and_boundaries:** Demonstrate one primary surface first and add another only when it owns a distinct interaction or automation responsibility.
- **revision_decision:** Introduce a surface-selection matrix later while making skill-only the evidence-supported default here.
- **additional_insight_to_add:** Combining surfaces is justified by one coherent capability lifecycle, not by a desire to showcase every extension mechanism.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** The duplicate local paths, Unicode tree diagrams, broad trigger phrases, optional file list, and unverified frontmatter fields can all be mistaken for independent or current normative evidence.
- **supporting_reason:** Those mistakes produce duplicated confidence, non-ASCII output, accidental activation, stale host assumptions, and decorative files without a consumer.
- **counterargument_or_limit:** The historical template remains a useful compact teaching skeleton when each claim is bounded.
- **assumptions_and_boundaries:** Preserve observed content, translate trees to ASCII, and verify current host semantics before asserting required fields or activation behavior.
- **revision_decision:** Surface provenance, trigger overlap, minimality, ASCII, host-version, and optional-file ownership as opening cautions.
- **additional_insight_to_add:** An optional directory is not a feature until the primary skill links to it and a demonstration path proves why it exists.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** No title-level example distinguishes a teaching fixture from a production-ready plugin.
- **supporting_reason:** A good example has one narrow skill and two positive plus two negative trigger cases, a bad example advertises unimplemented commands and MCP tools, and a borderline example wraps the skill in an unverified manifest.
- **counterargument_or_limit:** Exact trigger counts are illustrative rather than a universal sufficiency rule.
- **assumptions_and_boundaries:** Select cases from realistic user phrasing, neighboring skills, and the consequences of accidental activation.
- **revision_decision:** Add good, bad, and conditional opening contrasts tied to observable behavior.
- **additional_insight_to_add:** The negative example should show what does not activate, because silence and noninterference are part of an implicit invocation contract.
### Question 08: How can the important claims be verified?
- **current_section_observation:** The title supplies no distinction among file inspection, schema validation, host loading, trigger selection, invocation, side effects, permissions, and removal.
- **supporting_reason:** A claim-to-gate ladder prevents a valid Markdown file from being reported as an installed and usable plugin.
- **counterargument_or_limit:** The generic reference cannot know the target host's exact commands or installation layout.
- **assumptions_and_boundaries:** Discover supported commands and record only observed results; otherwise retain conditional gate semantics.
- **revision_decision:** Require structural, trigger, behavior, lifecycle, isolation, and cleanup evidence proportional to the surfaces included.
- **additional_insight_to_add:** A valid positive trigger is insufficient unless a neighboring negative request proves the example does not capture unrelated work.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The two local files are byte-identical historical skill templates, while current host rules, plugin packaging, MCP behavior, and installation commands were not inspected externally.
- **supporting_reason:** Their exact content supports a bounded skill demonstration and exposes its trigger-oriented teaching intent.
- **counterargument_or_limit:** Even the template's frontmatter options and activation claims may have changed in a current host.
- **assumptions_and_boundaries:** Treat current syntax and runtime behavior as target-verified concerns rather than historical facts.
- **revision_decision:** Label duplicate historical observation, systems synthesis, hypothetical lifecycle, and unresolved currentness separately.
- **additional_insight_to_add:** Strong evidence about what a file contains can coexist with low confidence about how a contemporary host interprets it.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The title does not address how an example becomes a template, copied dependency, compatibility promise, or maintenance burden.
- **supporting_reason:** Once reused, names, triggers, folder choices, permissions, and verification gaps propagate into many extensions.
- **counterargument_or_limit:** A disposable workshop artifact may intentionally optimize for explanation over long-term maintenance.
- **assumptions_and_boundaries:** Label disposable examples and prevent them from being installed or published as supported templates without promotion review.
- **revision_decision:** Frame demonstration quality as safe replication, with explicit promotion, ownership, versioning, and retirement triggers.
- **additional_insight_to_add:** The most successful example is not the one with the most surfaces; it is the one whose copied assumptions remain visible and testable.

## Section 002: Source Evidence Mapping Table
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed gives two identical local skill files and three uninspected MCP links equal-looking authority for a broad plugin demonstration.
- **supporting_reason:** Claim-scoped source roles let a reviewer decide which artifact can support skill structure, protocol questions, ecosystem examples, GitHub integration, or target-host lifecycle behavior.
- **counterargument_or_limit:** A future target plugin may legitimately combine the local skill with an MCP server and GitHub tools.
- **assumptions_and_boundaries:** Each surface still requires its own current source, project artifact, and executable gate before the combined example claims support.
- **revision_decision:** Map inspection status, duplicate identity, permitted claim scope, prohibited extrapolation, and first applicability gate for every source.
- **additional_insight_to_add:** Evidence about one extension surface should not acquire package-wide authority merely because all files share a plugin directory.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** `local_corpus_sourced_fact` appears twice and can be misread as independent confirmation.
- **supporting_reason:** Deduplicating by content hash preserves both provenance paths while preventing duplicated confidence.
- **counterargument_or_limit:** The working path may indicate current repository placement even when its bytes match the archive.
- **assumptions_and_boundaries:** Treat path presence as a separate local observation and content as one historical claim source.
- **revision_decision:** Designate the archive as frozen provenance, the working copy as a duplicate locator, and the target host as the current applicability gate.
- **additional_insight_to_add:** Duplicate content can still reveal distribution history, but it cannot increase confidence in the repeated technical claim.
### Question 03: When does the default work well?
- **current_section_observation:** The local skill contains durable teaching questions about focus, triggers, required and optional files, structure, actions, examples, and overlap.
- **supporting_reason:** Those questions remain useful for evaluating a skill demonstration even when exact frontmatter or host behavior changes.
- **counterargument_or_limit:** The template's precise field list and activation language are version-sensitive.
- **assumptions_and_boundaries:** Reuse the design question and verify its current mechanism against the target environment.
- **revision_decision:** Separate stable demonstration responsibilities from historical syntax and runtime claims.
- **additional_insight_to_add:** A dated example retains value when it teaches what to verify rather than declaring how every current host works.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The MCP specification URL is date-pinned, the repositories were not inspected, and none can validate a skill-only plugin lifecycle in this pass.
- **supporting_reason:** Treating those rows as current facts would import protocol, server, authentication, or GitHub behavior into a demonstration that contains no such implementation.
- **counterargument_or_limit:** They remain plausible future retrieval surfaces if an MCP boundary becomes material.
- **assumptions_and_boundaries:** Preserve the links as unrefreshed mappings and reopen only after the capability contract selects that surface.
- **revision_decision:** Remove current external-fact labels and add explicit out-of-baseline dispositions.
- **additional_insight_to_add:** A reputable protocol source can still be irrelevant to the extension decision currently being taught.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The map omits target manifests, validators, host help, installation records, permission declarations, package contents, trigger traces, tests, and cleanup observations.
- **supporting_reason:** These artifacts establish what the demonstration actually loads and does more directly than a generic ecosystem repository.
- **counterargument_or_limit:** Local project artifacts can encode stale or accidental behavior.
- **assumptions_and_boundaries:** Combine descriptive artifacts with current host validation and positive plus negative behavior checks.
- **revision_decision:** Add target-project evidence as a required applicability layer without inventing paths or commands.
- **additional_insight_to_add:** Packaging truth is the intersection of declared manifest, files actually shipped, host loader behavior, and removal residue.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Source rows omit byte identity, checked date, source version, host version, content scope, executable status, permissions, transitive files, and changed-decision fields.
- **supporting_reason:** Those omissions let directory names, stale links, and static examples masquerade as installed behavior.
- **counterargument_or_limit:** Full provenance is excessive for a harmless wording example.
- **assumptions_and_boundaries:** Increase evidence detail when claims involve invocation, automation, external access, secrets, installation, compatibility, or removal.
- **revision_decision:** Add concise risk and verification fields proportional to the claimed lifecycle.
- **additional_insight_to_add:** The first useful gate is the one that can falsify the source's proposed role, not merely confirm that its path exists.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** The seed provides no extraction examples for its local or public rows.
- **supporting_reason:** Good use derives trigger tests from the skill, bad use cites the GitHub MCP repository to claim installation, and borderline use consults the MCP resource spec after a real resource-sharing requirement appears.
- **counterargument_or_limit:** Even the borderline use needs target transport, security, and shutdown evidence.
- **assumptions_and_boundaries:** Label external protocol evidence separately from host integration and user-journey results.
- **revision_decision:** Add accepted, rejected, and conditional source uses with changed-action criteria.
- **additional_insight_to_add:** A source can answer a protocol semantic question while leaving the package and user experience entirely unresolved.
### Question 08: How can the important claims be verified?
- **current_section_observation:** Paths and URLs have no source-span, hash, page, version, load, trigger, lifecycle, or package-incorporation evidence.
- **supporting_reason:** A source disposition can bind exact claim, scope, target artifact, selected decision, executed gate, observation, and residual uncertainty.
- **counterargument_or_limit:** This reference has no target host project in which to run installation or invocation commands.
- **assumptions_and_boundaries:** Specify the evidence contract now and report actual results only in a concrete target.
- **revision_decision:** Define a source-to-artifact-to-host-to-user verification chain.
- **additional_insight_to_add:** A syntactically valid skill proves neither correct activation nor clean distribution inside a plugin wrapper.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** Both local files exist, contain identical bytes, and describe a historical skill; current external content and contemporary host interpretation remain unknown.
- **supporting_reason:** Complete local reading supports precise content inventory and duplicate classification without requiring web or runtime claims.
- **counterargument_or_limit:** The archive version may still match a current host by coincidence.
- **assumptions_and_boundaries:** Coincidence becomes applicability only after current validation and behavior evidence.
- **revision_decision:** Label historical observation, duplicate locator, unrefreshed mapping, target observation, synthesis, and unresolved currentness distinctly.
- **additional_insight_to_add:** Confidence can be high about provenance and low about runtime behavior at the same time.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The map is a bibliography and does not reveal how adding one surface expands permissions, package contents, failure ownership, or maintenance.
- **supporting_reason:** A source-to-decision dependency map allows later host, protocol, or integration changes to invalidate only affected guidance.
- **counterargument_or_limit:** Fine-grained provenance can overburden a one-file workshop skill.
- **assumptions_and_boundaries:** Track dependencies for reusable templates and for claims about install, external effects, security, compatibility, or removal.
- **revision_decision:** Turn the source table into a scope, risk, and refresh index.
- **additional_insight_to_add:** The safest demonstration grows its evidence graph only when its capability graph actually grows.

## Section 003: Pattern Scoreboard Ranking Table
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed ranks three evidence-process patterns under one repeated identifier but omits the demonstration choices that determine invocation, scope, side effects, lifecycle, and safe reuse.
- **supporting_reason:** Trigger-based priorities can order capability contract, primary surface, minimal artifact, activation isolation, host validation, permissions, lifecycle, and handoff.
- **counterargument_or_limit:** A static order cannot know whether the current failure is a bad trigger, invalid manifest, leaked side effect, stale protocol, or incomplete removal.
- **assumptions_and_boundaries:** Use the scoreboard for new construction and let the first observed failed boundary lead repair.
- **revision_decision:** Preserve inherited rows with caveats and add unscored demonstration priorities with direct falsifiers.
- **additional_insight_to_add:** A demonstration's highest-priority property is the one whose failure teaches users the wrong capability contract.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** Source loading leads the seed, while no dependency order moves from user goal to safely repeatable example.
- **supporting_reason:** Capability, invocation surface, target host, minimal files, deterministic behavior, trigger isolation, lifecycle, and evidence form a causal construction sequence.
- **counterargument_or_limit:** Repair work should not rebuild unaffected stages merely to follow the default order.
- **assumptions_and_boundaries:** New examples use the full sequence; repairs start at the earliest divergence and rerun dependent gates.
- **revision_decision:** Add a construction order plus failed-gate override rule.
- **additional_insight_to_add:** Freeze the user-visible contract before packaging so a manifest cannot legitimize an incoherent or oversized example.
### Question 03: When does the default work well?
- **current_section_observation:** `default_adoption_pattern_tier` has no fit conditions for skill-only, multi-surface, external-service, or distributable demonstrations.
- **supporting_reason:** The order fits a bounded example with one primary user goal, inspectable host, reproducible environment, and limited side effects.
- **counterargument_or_limit:** A protocol server or hook may require lifecycle and failure design before any user-facing walkthrough exists.
- **assumptions_and_boundaries:** Move the material trust or automation boundary earlier while retaining the capability contract.
- **revision_decision:** Attach fit and override triggers to each priority rather than claiming one universal rank.
- **additional_insight_to_add:** Implicit activation and automatic execution deserve earlier isolation checks than an explicitly invoked, read-only command.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** Bare values 95, 91, and 88 can be misread as calibrated confidence, effectiveness, or measured adoption success.
- **supporting_reason:** The seed provides no sample, scoring protocol, or outcome data for those numbers.
- **counterargument_or_limit:** Retaining them preserves provenance and the seed's intended evidence-process ordering.
- **assumptions_and_boundaries:** Treat them only as inherited editorial metadata and never compare their spacing or average them.
- **revision_decision:** Add a score warning and prohibit numeric order from overriding security, host validation, behavior, or cleanup failure.
- **additional_insight_to_add:** An unscored permission leak is still blocking because consequence outranks presentation metadata.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The scoreboard does not compare dependency order, risk severity, teaching value, first-failed-boundary repair, or release checklist priority.
- **supporting_reason:** Dependency order supports construction, severity supports containment, teaching value supports simplification, and failure routing supports diagnosis.
- **counterargument_or_limit:** Combining these into one formula would create false precision and hide context.
- **assumptions_and_boundaries:** Keep them as separate qualitative dimensions that change the next action.
- **revision_decision:** Use ordered defaults, consequence flags, and direct falsifiers without a composite score.
- **additional_insight_to_add:** A compact example can rank highly for teaching while remaining ineligible for distribution until lifecycle evidence exists.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Duplicate identifiers and uniform tiers hide different responsibilities, while trigger overlap, optional-file drift, current-host mismatch, permission denial, nondeterminism, and uninstall residue are absent.
- **supporting_reason:** Unique pattern names, applicability triggers, prevented failures, and direct gates make priority operational.
- **counterargument_or_limit:** The shared theme key remains useful as historical provenance.
- **assumptions_and_boundaries:** Retain it only on inherited rows and give new patterns descriptive names.
- **revision_decision:** Expand the scoreboard with demonstration-specific failures and evidence.
- **additional_insight_to_add:** Package validation should never rank ahead of proving that the packaged capability is the one the user intended to learn.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** Failure-prevention text gives no scenario where the priority order changes.
- **supporting_reason:** A narrow skill uses the default order, an auto-running hook elevates isolation and rollback, and an MCP example elevates protocol and least-privilege gates.
- **counterargument_or_limit:** Consequence and host architecture can change which boundary is most urgent.
- **assumptions_and_boundaries:** Every override names user impact, surface, environment, and evidence that returns to the default sequence.
- **revision_decision:** Add scenario-based override guidance beneath the table.
- **additional_insight_to_add:** Borderline multi-surface examples become acceptable only after each surface proves a distinct responsibility and shared lifecycle.
### Question 08: How can the important claims be verified?
- **current_section_observation:** Seed rows do not map to structural validation, trigger tests, host loading, side-effect isolation, permission denial, installation, removal, or copyability review.
- **supporting_reason:** One direct falsifier per priority prevents a slogan from becoming a template without evidence.
- **counterargument_or_limit:** Exact validators and commands differ by target host and package format.
- **assumptions_and_boundaries:** Define evidence semantics here and discover concrete invocations from the target environment.
- **revision_decision:** Add prevented failure and direct gate columns with candidate-bound observations.
- **additional_insight_to_add:** The strongest gate crosses the same invocation or lifecycle boundary the pattern claims to make safe.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The inherited numbers and three ordering labels are factual seed content, but calibration and predictive value are unknown.
- **supporting_reason:** The local corpus directly supports focus, description-led triggers, minimal required file, optional support, structure, actionability, examples, and overlap checks.
- **counterargument_or_limit:** Current host semantics and relative implementation priority require target evidence.
- **assumptions_and_boundaries:** Separate historical proposal, editorial order, target observation, and verified behavior.
- **revision_decision:** Preserve numeric provenance while grounding new rows in causal risks and falsifiers.
- **additional_insight_to_add:** Confidence should attach to an observed capability boundary, not to a pattern label or directory name.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The scoreboard is static and does not learn when copied examples repeatedly fail at one trigger, lifecycle, or permission boundary.
- **supporting_reason:** Retained override reasons can expose a weak default, missing negative case, unsafe fixture, or packaging gap.
- **counterargument_or_limit:** Reacting to every isolated workshop mistake can destabilize a useful teaching order.
- **assumptions_and_boundaries:** Revise the default after repeated relevant evidence or one high-consequence escape.
- **revision_decision:** Add override retention, copy-feedback review, and deliberate scoreboard refresh triggers.
- **additional_insight_to_add:** A demonstration library improves when failure evidence changes the order without pretending that its priorities were statistically optimized.

## Section 004: Idiomatic Thesis Synthesis Statement
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed thesis describes source retrieval order but never defines what makes an extension demonstration idiomatic, operational, or safe to copy.
- **supporting_reason:** A governing thesis can unite capability intent, invocation semantics, minimal artifact closure, deterministic behavior, host compatibility, failure recovery, lifecycle, and reuse.
- **counterargument_or_limit:** Different hosts and surfaces require different schemas, commands, and runtime evidence.
- **assumptions_and_boundaries:** Define stable demonstration responsibilities while leaving exact host mechanisms conditional on discovery.
- **revision_decision:** Replace bibliography-first prose with an executable-teaching-contract thesis.
- **additional_insight_to_add:** The example's public API includes its walkthrough and omissions because learners treat both as design signals.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** No workflow orders user goal, surface selection, host inspection, file creation, activation, behavior, lifecycle, and promotion.
- **supporting_reason:** Dependency ordering prevents packaging and optional files from hardening before the capability and invocation contract are settled.
- **counterargument_or_limit:** Existing plugins may require characterization and compatibility preservation before simplification.
- **assumptions_and_boundaries:** Start from deployed behavior when modifying a supported example and use additive migration for copied consumers.
- **revision_decision:** Define a reversible loop from behavior through minimal artifact, gates, lifecycle, and handoff.
- **additional_insight_to_add:** A demonstration is incomplete until a non-goal and negative invocation path are as clear as the success path.
### Question 03: When does the default work well?
- **current_section_observation:** The seed does not distinguish contextual guidance, explicit operations, automatic events, protocol tools, configuration, or distribution.
- **supporting_reason:** The thesis works when one primary surface and one bounded user observation can be exercised in an inspectable environment.
- **counterargument_or_limit:** Multi-service integrations, production automation, and destructive workflows need specialized security and operations guidance.
- **assumptions_and_boundaries:** This reference may coordinate the teaching slice while routing system-level guarantees to an accountable companion.
- **revision_decision:** Add direct-fit cases and transition boundaries.
- **additional_insight_to_add:** A multi-surface example is still bounded when every surface contributes to one lifecycle and no surface exists merely for coverage.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** Local-first wording can preserve every historical field and folder or import MCP examples without asking whether they serve the current user goal.
- **supporting_reason:** Anti-dogma boundaries prevent directory shape, protocol choice, or plugin wrappers from becoming cargo-cult requirements.
- **counterargument_or_limit:** Consistent scaffolding lowers learning cost when the target host and organization deliberately standardize it.
- **assumptions_and_boundaries:** Keep standardized structure when its owner and current validator establish value; otherwise require a demonstrated consumer.
- **revision_decision:** State that each artifact and surface must own a teaching or runtime responsibility.
- **additional_insight_to_add:** Removing a decorative file can improve reliability by eliminating a stale path learners would otherwise copy.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The thesis gives no balance among static walkthrough, runnable fixture, model-invoked skill, explicit command, automatic hook, MCP server, and packaged plugin.
- **supporting_reason:** These choices optimize accessibility, determinism, interactivity, automation, integration, and distribution differently.
- **counterargument_or_limit:** A thesis overloaded with mechanisms becomes another catalog.
- **assumptions_and_boundaries:** Compare alternatives where invocation, side effects, trust, or lifecycle differs and defer syntax to current host evidence.
- **revision_decision:** Add selection principles and route detailed choices to the tradeoff guide.
- **additional_insight_to_add:** Prefer the least powerful surface that can prove the user outcome because privilege and lifecycle cost grow with capability.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** The current thesis ignores broad activation, overlapping triggers, unreferenced support files, live side effects, excessive permissions, nondeterminism, stale host fields, package omissions, and removal residue.
- **supporting_reason:** These failures are likely to be copied from an example and can survive superficial structure review.
- **counterargument_or_limit:** Not every example needs installation, secrets, network, or cleanup states.
- **assumptions_and_boundaries:** Include controls only for surfaces and effects the capability actually exercises.
- **revision_decision:** Add a boundary-specific failure scan to the thesis loop.
- **additional_insight_to_add:** Absence of an explicit cleanup path is a lifecycle decision whenever the demonstration creates durable state.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** Retrieval prose offers no extension behavior contrast.
- **supporting_reason:** A narrow skill with negative triggers, a kitchen-sink folder with fake surfaces, and a real manifest without removal evidence expose thesis quality.
- **counterargument_or_limit:** A workshop can intentionally use mock surfaces to teach composition.
- **assumptions_and_boundaries:** Label mocks unmistakably and prevent them from being validated or published as supported integration.
- **revision_decision:** Add complete, misleading, and conditional demonstration contrasts.
- **additional_insight_to_add:** A good example teaches the user's recovery from failure, not only the maintainer's preferred file layout.
### Question 08: How can the important claims be verified?
- **current_section_observation:** "Verification-backed" is not decomposed into source, structure, host load, activation, behavior, denial, side-effect, package, removal, and copyability gates.
- **supporting_reason:** Layered evidence localizes defects while one walkthrough proves that files and host behavior agree.
- **counterargument_or_limit:** A generic reference cannot promise exact commands without a target host.
- **assumptions_and_boundaries:** Provide gate semantics and require discovered commands with honest observations.
- **revision_decision:** Add an evidence ladder with at least one meaningful negative path.
- **additional_insight_to_add:** A package contents check must accompany manifest validation because declared files and shipped files can diverge.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The seed claims public ecosystem analogues exist but does not distinguish mapped links from inspected current facts.
- **supporting_reason:** Historical skill content and duplicate identity are known, while current host rules and external repositories remain unverified.
- **counterargument_or_limit:** Systems reasoning can still recommend minimality, least privilege, deterministic fixtures, and negative tests.
- **assumptions_and_boundaries:** Label those as bounded synthesis and make target mechanisms conditional.
- **revision_decision:** Separate historical fact, unrefreshed mapping, synthesis, target observation, and unresolved current behavior.
- **additional_insight_to_add:** A strong local result can justify one template without becoming an ecosystem-wide plugin recommendation.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The thesis ends at implementation and omits copying, publication, upgrades, deprecation, ownership transfer, and residue.
- **supporting_reason:** Demonstrations become dependencies when scaffolds, documentation, and agents reuse their assumptions.
- **counterargument_or_limit:** Disposable internal examples may not warrant a long support lifecycle.
- **assumptions_and_boundaries:** Mark disposal scope and prohibit promotion without a support decision.
- **revision_decision:** Extend the thesis through promotion, versioning, feedback, and retirement.
- **additional_insight_to_add:** The durable unit is a verified capability lesson plus lifecycle boundaries, not a memorable directory tree.

## Section 005: Local Corpus Source Map
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed repeats two identical file rows and summarizes only their first headings, hiding where trigger, structure, frontmatter, content, and overlap guidance lives.
- **supporting_reason:** Region-level retrieval lets a builder load the smallest historical material that can change the current demonstration decision.
- **counterargument_or_limit:** A complete skill example often needs several regions reconciled because description, applicability, files, and tests form one activation contract.
- **assumptions_and_boundaries:** Start narrowly and include every region that owns a claimed behavior or support artifact.
- **revision_decision:** Replace duplicate file summaries with one content-region map plus a duplicate-location note.
- **additional_insight_to_add:** A heading map is navigation evidence, while applicability still depends on the target host and user journey.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** The seed gives no retrieval sequence beyond opening both paths.
- **supporting_reason:** Read frontmatter and overview, applicability, required structure, optional supports, description guidance, content rules, and best practices in causal order.
- **counterargument_or_limit:** A question about one trigger phrase may not require every optional-file example.
- **assumptions_and_boundaries:** Stop only after neighboring activation and copied-file risks are addressed.
- **revision_decision:** Define full-skill, trigger-only, structure-only, and promotion-review retrieval profiles.
- **additional_insight_to_add:** Pair a positive description pattern with overlap and negative-trigger review before adopting it.
### Question 03: When does the default work well?
- **current_section_observation:** The source map does not identify stable teaching responsibilities that survive host changes.
- **supporting_reason:** Focus, user-language triggers, required-versus-optional separation, structured guidance, actionability, examples, and overlap avoidance are durable review questions.
- **counterargument_or_limit:** Exact activation behavior, frontmatter keys, and directory names remain host- and version-dependent.
- **assumptions_and_boundaries:** Reuse the question and revalidate the mechanism.
- **revision_decision:** Label durable demonstration prompts separately from historical syntax.
- **additional_insight_to_add:** The source's strongest lasting value is its focus discipline, not its particular tree rendering.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** Treating both files as canonical sources would duplicate confidence and preserve Unicode trees, broad triggers, optional folders, and field claims without current checks.
- **supporting_reason:** Region-level caveats prevent observed examples from becoming universal package requirements.
- **counterargument_or_limit:** The copied working location may still matter for repository navigation.
- **assumptions_and_boundaries:** Preserve locator provenance while deduplicating technical content.
- **revision_decision:** Add duplicate, ASCII, currentness, and demonstrated-consumer warnings to relevant regions.
- **additional_insight_to_add:** Repeated bytes can indicate copying history without proving maintenance or support.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** Full-file loading, heading retrieval, snippet copying, and target-host-first investigation are not compared.
- **supporting_reason:** Full reading exposes the complete teaching contract, targeted reading conserves context, snippets accelerate adaptation, and host evidence prevents stale syntax.
- **counterargument_or_limit:** Host-first work can reproduce a broad local convention without learning the source's focus rationale.
- **assumptions_and_boundaries:** Use the source to propose a bounded example and the host to select and verify its mechanism.
- **revision_decision:** Recommend progressive retrieval with mandatory cross-region reconciliation before publication.
- **additional_insight_to_add:** Additional source context is justified when the proposed change affects activation or file closure, not by document length alone.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** The map omits description overbreadth, positive-only triggers, optional-folder cargo cult, unlinked references, unsafe helper scripts, frontmatter drift, and missing install or removal evidence.
- **supporting_reason:** These omissions can propagate directly when the historical skill is copied as a complete plugin template.
- **counterargument_or_limit:** Some support folders may be populated later in a staged workshop.
- **assumptions_and_boundaries:** Label staged material, exclude it from distributable claims, and set a removal or completion condition.
- **revision_decision:** Add a region-specific defect and gate index.
- **additional_insight_to_add:** A comment saying a file is optional does not protect learners if the published tree implies it is standard.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** No retrieval example shows which source regions a concrete task should combine.
- **supporting_reason:** A trigger refinement loads applicability, descriptions, and overlap practices; a minimal-tree task loads structure and content rules; a plugin install task must route beyond this corpus.
- **counterargument_or_limit:** Actual host documentation can group these responsibilities differently.
- **assumptions_and_boundaries:** Match regions by behavior and claim rather than copied heading name.
- **revision_decision:** Add trigger, structure, and route-away examples.
- **additional_insight_to_add:** Borderline reuse becomes useful when it ends in a target-host experiment instead of a claim of current correctness.
### Question 08: How can the important claims be verified?
- **current_section_observation:** No record proves the relevant region was read, its caveat captured, or its proposal tested.
- **supporting_reason:** Region disposition, adapted artifact, host validation, activation cases, support-file reachability, and lifecycle boundaries trace source to result.
- **counterargument_or_limit:** A generic reference cannot execute target-host checks.
- **assumptions_and_boundaries:** Require exact future gates and report only actual observations in the target project.
- **revision_decision:** Add a region-to-artifact-to-host verification record.
- **additional_insight_to_add:** Test the failure the region claims to prevent, such as trigger overlap, rather than only its preferred positive example.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** Paths, bytes, headings, prose, and examples are inspectable, while current field support, activation, plugin packaging, and teaching effectiveness are not established.
- **supporting_reason:** Complete reading supports a precise inventory without ecosystem or runtime overclaim.
- **counterargument_or_limit:** Some historical mechanisms may remain supported unchanged.
- **assumptions_and_boundaries:** Treat unchanged support as a target observation only after current validation.
- **revision_decision:** Separate source-content certainty, inferred reuse risk, and host-tested behavior.
- **additional_insight_to_add:** Confidence varies by region, so one whole-file authority label is too coarse.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The map treats retrieval as a one-time prerequisite rather than an input to template maintenance.
- **supporting_reason:** Region provenance lets later trigger, schema, loader, or support-file changes invalidate only dependent guidance.
- **counterargument_or_limit:** Fine-grained tracking is unnecessary for a disposable personal example.
- **assumptions_and_boundaries:** Retain it for reusable, published, permissioned, or externally integrated demonstrations.
- **revision_decision:** Turn the map into progressive disclosure and refresh routing.
- **additional_insight_to_add:** Cross-region dependencies reveal when a description change also expires activation tests and walkthrough evidence.

## Section 006: External Research Source Map
### Question 01: What decision does this reference help make?
- **current_section_observation:** Three external rows are labeled as sourced facts without current inspection or a rule connecting them to plugin, skill, MCP, server-index, or GitHub claims.
- **supporting_reason:** A scoped map can decide whether to refresh, reject, or conditionally consult a source for one volatile surface decision.
- **counterargument_or_limit:** Target-host artifacts and local behavior may answer the question without external research.
- **assumptions_and_boundaries:** No public URL was opened, so this section can preserve future roles but no current content.
- **revision_decision:** Mark each mapping unrefreshed, define permitted future scope, and identify missing authority categories.
- **additional_insight_to_add:** A current protocol source cannot establish that a particular host packages or exposes that protocol in the way the example assumes.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** The seed implies generic ecosystem checking after the local corpus regardless of selected surface or decision volatility.
- **supporting_reason:** Discovering the target host, schemas, help, manifests, validators, and executable behavior usually provides the fastest applicability evidence.
- **counterargument_or_limit:** A project can rely on deprecated behavior that still works locally until an upgrade breaks it.
- **assumptions_and_boundaries:** Refresh primary guidance when a changing public contract affects schema, permissions, protocol, migration, security, or completion.
- **revision_decision:** Prefer event-driven, surface-specific refresh over routine browsing of all inherited links.
- **additional_insight_to_add:** A failed local gate should produce a narrower external question than the phrase example plugin.
### Question 03: When does the default work well?
- **current_section_observation:** The date-pinned MCP resource page is not separated from repository examples or a GitHub-specific server.
- **supporting_reason:** A specification can clarify resource semantics, an implementation index can aid discovery, and a service server can illustrate one integration under distinct evidence roles.
- **counterargument_or_limit:** None establishes target-host installation, skill activation, or generic plugin packaging.
- **assumptions_and_boundaries:** Pair any refreshed source with the exact target surface and end-to-end behavior.
- **revision_decision:** Add source-role and host-applicability checks to every row.
- **additional_insight_to_add:** The narrower the public source's ownership, the less likely it is to leak into unrelated extension architecture.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** Familiar official-looking URLs and `external_research_sourced_fact` labels can be cited as present authority despite no browse evidence.
- **supporting_reason:** That launders freshness and can import MCP or GitHub requirements into a skill-only demonstration.
- **counterargument_or_limit:** Protocol analogies can expose a missed trust, malformed-input, or shutdown question.
- **assumptions_and_boundaries:** Translate only the question and derive implementation from current target sources.
- **revision_decision:** Forbid present claims and direct transfer from unrefreshed or unselected surfaces.
- **additional_insight_to_add:** Rejecting a reputable source as irrelevant is evidence discipline, not incomplete coverage.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The map omits current host plugin and skill documentation, manifest schema, command and hook contracts, settings precedence, permission guidance, migration notes, and package lifecycle material.
- **supporting_reason:** Those sources would answer the actual extension contract more directly than generic server repositories.
- **counterargument_or_limit:** Adding guessed URLs would create a precise-looking bibliography without evidence.
- **assumptions_and_boundaries:** Record source categories and future questions now; add exact locations only after an authorized refresh.
- **revision_decision:** Keep inherited mappings small and name missing authority classes explicitly.
- **additional_insight_to_add:** An honest missing source is safer than a plausible link whose version and applicability were never checked.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Rows lack checked date, protocol or host version, relevant section, publisher role, sample support status, authentication model, target match, contradiction, and changed-action fields.
- **supporting_reason:** Without those fields, an external citation cannot be reproduced or distinguished from decorative research.
- **counterargument_or_limit:** Full provenance for a low-risk wording choice can exceed its value.
- **assumptions_and_boundaries:** Retain expanded records for schema, permission, lifecycle, protocol, security, compatibility, and deprecation decisions.
- **revision_decision:** Define a compact future refresh packet with accepted, rejected, and no-impact states.
- **additional_insight_to_add:** Public currency and installed-host applicability are independent checks.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** The external map provides no examples of responsible future use or scope violation.
- **supporting_reason:** Good use refreshes the applicable MCP spec after selecting a resource surface, bad use cites the server index to claim a skill is installable, and borderline use studies the GitHub server for a real least-privilege repository task.
- **counterargument_or_limit:** Even the borderline case needs current host, authentication, denial, side-effect, and cleanup evidence.
- **assumptions_and_boundaries:** Label protocol fact, implementation example, target observation, and systems inference separately.
- **revision_decision:** Add accepted, rejected, and conditional scenarios.
- **additional_insight_to_add:** A refresh can produce no material impact, which is useful when it prevents repeated research without forcing a design change.
### Question 08: How can the important claims be verified?
- **current_section_observation:** No current-content, publisher, claim-entailment, release, target-host, security, or local-retest evidence exists.
- **supporting_reason:** A future record can bind direct source, checked date, revision, bounded claim, target applicability, conflict, decision, and rerun observation.
- **counterargument_or_limit:** Public pages and repository branches can move after capture.
- **assumptions_and_boundaries:** Preserve source identity, release or commit, and bounded paraphrase rather than search ranking.
- **revision_decision:** Add refresh completion and affected-artifact retest requirements.
- **additional_insight_to_add:** External verification remains incomplete until the target demonstration's user behavior is re-exercised.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** URL strings and inherited roles are known, while current content, revisions, recommendations, support, and host applicability are unknown.
- **supporting_reason:** Honest unrefreshed status preserves future discoverability without fabricating evidence.
- **counterargument_or_limit:** Recognizable domains can still tempt readers to infer authority.
- **assumptions_and_boundaries:** Use a distinct non-evidentiary mapping class until full inspection occurs.
- **revision_decision:** Replace external fact labels with `external_mapping_unrefreshed_note` throughout this section.
- **additional_insight_to_add:** Confidence should advance through discovered, inspected, applicable, reproduced, and reconciled states.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** External research is only additive and has no lifecycle for narrowing, superseding, or retiring irrelevant mappings.
- **supporting_reason:** A maintained map should remove noise when repeated decisions prove a source outside the example's real capability boundary.
- **counterargument_or_limit:** Premature retirement can hide a future integration route.
- **assumptions_and_boundaries:** Preserve retirement rationale and reopen only when a new capability contract supplies relevance.
- **revision_decision:** Add source lifecycle, no-impact disposition, and event-driven refresh triggers.
- **additional_insight_to_add:** External-map quality is measured by decision precision and reproducibility, not reputable link count.

## Section 007: Anti Pattern Registry Table
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed registry covers generic source failures but omits defects that make an extension demonstration misleading, unsafe, untestable, or difficult to remove.
- **supporting_reason:** A causal registry can route a builder to narrow, validate, isolate, deny, clean, or remove the earliest faulty lesson.
- **counterargument_or_limit:** An example should not be rejected solely because its structure resembles a known failure.
- **assumptions_and_boundaries:** Name the violated capability, invocation, trust, lifecycle, or copyability contract before applying a label.
- **revision_decision:** Add activation, structure, host, permission, side-effect, protocol, lifecycle, and reuse anti-patterns with valid exceptions.
- **additional_insight_to_add:** The earliest misleading assumption often propagates through every plugin copied from the example.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** Existing replacements prescribe source practices but give no order for containing an unsafe demonstration.
- **supporting_reason:** Stop destructive effects and secret exposure first, then excessive permissions, automatic invocation, lifecycle residue, contract mismatch, trigger overlap, optional-file drift, and presentation issues.
- **counterargument_or_limit:** A syntax or host-load failure can block observation of deeper behavior and need immediate correction.
- **assumptions_and_boundaries:** Restore enough mechanical validity to exercise behavior, then repair by consequence and causal depth.
- **revision_decision:** Add containment, smallest causal repair, dependent rerun, and exception evidence to each failure family.
- **additional_insight_to_add:** Preserve the failing fixture and host state before repair so a clean rerun cannot be attributed to changed inputs.
### Question 03: When does the default work well?
- **current_section_observation:** No review depth distinguishes a one-file skill, explicit command, automatic hook, external server, setting, or packaged plugin.
- **supporting_reason:** The registry is most valuable where invocation is implicit, side effects cross trust boundaries, or distribution leaves durable state.
- **counterargument_or_limit:** A static read-only example does not need network, permission, process, or uninstall checks.
- **assumptions_and_boundaries:** Apply only rows whose failure can reach the claimed demonstration surface.
- **revision_decision:** Define static, runnable, automatic, integrated, and distributable review profiles.
- **additional_insight_to_add:** Small file count does not imply low review scope when the example can modify repositories or expose credentials.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** Generic labels can turn preferences for minimal folders or one surface into prohibitions without a reproduced failure.
- **supporting_reason:** Requiring a signal and exception prevents cargo-cult enforcement while preserving preventive review for high-consequence risks.
- **counterargument_or_limit:** Security and cleanup failures should be prevented before a published incident exists.
- **assumptions_and_boundaries:** A threat model, permission boundary, controlled mutation, or residue scan can establish risk without waiting for harm.
- **revision_decision:** Distinguish observed escape, credible preventive risk, and aesthetic preference.
- **additional_insight_to_add:** Not observed is weak evidence when the example never exercises denial, overlap, repeated invocation, or removal.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** One generic safer replacement hides choices among narrowing a skill, splitting surfaces, adding adapters, mocking integrations, sandboxing fixtures, or removing package claims.
- **supporting_reason:** Different repairs preserve teaching simplicity, realism, isolation, compatibility, and least privilege differently.
- **counterargument_or_limit:** Multiple options can delay an obvious secret or destructive-side-effect correction.
- **assumptions_and_boundaries:** Apply hard containment first and compare structural alternatives only after the invariant is restored.
- **revision_decision:** Add remediation choices and the evidence selecting among them.
- **additional_insight_to_add:** Prefer the correction that reduces unowned boundaries without hiding the failure the example needs to teach.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Missing risks include directory-name authority, kitchen-sink surfaces, duplicate-source confidence, broad triggers, positive-only tests, orphan files, stale fields, live credentials, excessive permissions, nondeterminism, fake install, and removal residue.
- **supporting_reason:** Each can be copied directly from a demonstration even when its prose calls the example minimal or safe.
- **counterargument_or_limit:** Workshop mocks and staged files can be legitimate teaching devices.
- **assumptions_and_boundaries:** Mark them clearly, isolate them from real credentials and distribution, and define promotion or deletion conditions.
- **revision_decision:** Register high-propagation and high-consequence demonstration failures with concrete signals.
- **additional_insight_to_add:** A mock becomes dangerous when the same command or package name can be mistaken for a live integration.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** Current rows contain no extension-specific contrast or justified exception.
- **supporting_reason:** A skill that declines unrelated prompts is good, a hook that rewrites files on every event is bad, and an unused examples folder is borderline in a staged workshop.
- **counterargument_or_limit:** A carefully sandboxed file-writing hook can be the correct demonstration subject.
- **assumptions_and_boundaries:** State event, side effect, permission, isolation, rollback, and proof when classifying it.
- **revision_decision:** Add contrasts that separate failure mechanism from surface name.
- **additional_insight_to_add:** A borderline artifact becomes acceptable when its temporary scope and deletion or completion trigger are visible.
### Question 08: How can the important claims be verified?
- **current_section_observation:** Detection checks labels and source presence rather than activation overlap, invalid schema, denied permission, repeated runs, package contents, process shutdown, or residue.
- **supporting_reason:** Controlled negative and mutation tests can prove that a gate catches the misleading behavior and that repair removes it.
- **counterargument_or_limit:** Destructive or external tests need isolated targets and bounded credentials.
- **assumptions_and_boundaries:** Use fixtures, disposable repositories, fake services, and explicit stop conditions unless live integration is the capability under test.
- **revision_decision:** Add structure, host, activation, behavior, permission, side-effect, protocol, package, and cleanup evidence routes.
- **additional_insight_to_add:** A detector earns only the surface and failure timing it actually exercises.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** Local duplicate and skill-shape failures are directly inspectable, while frequency, host behavior, and downstream harm are not measured.
- **supporting_reason:** Systems behavior supports plausible causal risks, but target tests and copied-template history determine priority.
- **counterargument_or_limit:** Some apparent issues may be resolved by host behavior or omitted wrapper files in another project.
- **assumptions_and_boundaries:** Describe the observed omission, potential consequence, and discriminating gate separately.
- **revision_decision:** Present the registry as diagnostic and preventive guidance rather than incident ranking.
- **additional_insight_to_add:** Containment can be justified under uncertainty while root-cause and current-host claims remain provisional.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** Seed failures appear independent and do not expose cascades across trigger, permissions, packaging, teaching, and copied templates.
- **supporting_reason:** One overbroad description can activate an unsafe script, require excess privilege, leave residue, and propagate through scaffolds.
- **counterargument_or_limit:** Mapping every possible cascade would make the registry unusable.
- **assumptions_and_boundaries:** Retain recurring or high-consequence chains that change repair order.
- **revision_decision:** Add cascade notes and feedback triggers for strengthening earlier boundaries.
- **additional_insight_to_add:** Repeated lifecycle patches often indicate that the example's primary surface or capability contract is too broad upstream.

## Section 008: Verification Gate Command Set
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed supplies one repository-wide documentation command and does not distinguish reference conformance from target skill, plugin, protocol, permission, or lifecycle evidence.
- **supporting_reason:** A layered gate set lets a reviewer choose the cheapest observation that can falsify each demonstration claim.
- **counterargument_or_limit:** Exact host validators and installation commands cannot be prescribed without discovering the target environment.
- **assumptions_and_boundaries:** Provide executable self-checks and conditional host gate semantics without inventing results.
- **revision_decision:** Add the focused verifier, retain the shared verifier, and define project-discovered structural, behavioral, and lifecycle layers.
- **additional_insight_to_add:** A passing reference verifier proves document conformance, not that the historical skill loads or activates in a current host.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** No cheap-to-expensive order prevents install or external integration testing before file shape and capability scope are coherent.
- **supporting_reason:** Reference checks, project discovery, schema validation, file closure, host load, activation, behavior, permission, package, lifecycle, and compatibility minimize diagnostic cost.
- **counterargument_or_limit:** A reproduced installation or side-effect defect may justify starting with the failing end-to-end path.
- **assumptions_and_boundaries:** Preserve the failure first, then use the ladder to localize and repair it.
- **revision_decision:** Add construction and incident-repair sequences with stop conditions.
- **additional_insight_to_add:** Stop packaging work when the minimal artifact has an unexplained schema, path, or trigger failure.
### Question 03: When does the default work well?
- **current_section_observation:** The command has no conditions for static examples, skills, commands, hooks, MCP servers, or distributable wrappers.
- **supporting_reason:** Layered verification fits any surface when each claim selects only its relevant gates and records exclusions.
- **counterargument_or_limit:** A one-file documentation fixture needs far fewer lifecycle tests than a privileged plugin.
- **assumptions_and_boundaries:** Gate depth follows invocation power, side effects, trust, and distribution, not file count.
- **revision_decision:** Define static, skill, explicit-action, automatic, integrated, and packaged profiles.
- **additional_insight_to_add:** An implicit trigger can require more behavioral evidence than a larger explicitly invoked read-only command.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** Running one broad command can hide skipped cases, mocked host behavior, missing packaged files, excessive permission, removal residue, or version incompatibility.
- **supporting_reason:** Claim-to-gate mapping prevents an aggregate green result from being interpreted beyond coverage.
- **counterargument_or_limit:** Too many overlapping gates can make a small example slow and fragile.
- **assumptions_and_boundaries:** Retain the smallest nonduplicative set that crosses every material boundary.
- **revision_decision:** Add candidate identity, environment, pass observation, coverage limit, and expiry to evidence records.
- **additional_insight_to_add:** A command named validate or test is not evidence until its selected files, host, configuration, and exit behavior are known.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The seed does not compare parser checks, schema validators, link scans, host loading, trigger matrices, fixture snapshots, sandbox runs, package inspection, or lifecycle tests.
- **supporting_reason:** These methods trade speed, realism, determinism, safety, and failure localization.
- **counterargument_or_limit:** More realistic tests may require credentials, processes, network, or disposable environments.
- **assumptions_and_boundaries:** Use deterministic lower layers broadly and a small number of isolated realistic paths for boundary agreement.
- **revision_decision:** Add a claim-to-method matrix with each method's blind spot.
- **additional_insight_to_add:** Package inventory detects missing files, while a clean-host load proves the host can actually use them.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Missing risks include wrong working directory, stale host process, cached plugin, personal config, hidden credentials, edited package, mock/live confusion, skipped negative triggers, and dirty removal state.
- **supporting_reason:** Each can create misleading green output or an irreproducible handoff.
- **counterargument_or_limit:** Capturing every environment detail is excessive for a pure Markdown structure check.
- **assumptions_and_boundaries:** Record details that influence loading, selection, side effects, permissions, compatibility, or cleanup.
- **revision_decision:** Require exact command, working directory, candidate, host version, fixture state, result, and limit.
- **additional_insight_to_add:** Host restart and cache invalidation can be part of the load contract rather than incidental troubleshooting.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** The single command offers no evidence-packet contrast.
- **supporting_reason:** Good evidence binds schema, negative activation, isolated behavior, permission denial, package contents, and clean removal; bad evidence reports only Markdown lint; borderline evidence validates a manifest but never installs it.
- **counterargument_or_limit:** Installation is legitimately out of scope for an unwrapped skill fixture.
- **assumptions_and_boundaries:** Judge evidence against declared surfaces and lifecycle claims.
- **revision_decision:** Add complete, insufficient, and conditionally scoped examples.
- **additional_insight_to_add:** A failed negative trigger with a clear diagnosis can be more useful than a broad positive-only green suite.
### Question 08: How can the important claims be verified?
- **current_section_observation:** Verification is not mapped to provenance, current schema, file reachability, trigger isolation, deterministic output, least privilege, automatic-event safety, protocol behavior, package closure, or cleanup.
- **supporting_reason:** Explicit mappings give every high-consequence recommendation a direct falsifier crossing its claimed boundary.
- **counterargument_or_limit:** Some production host behavior requires staged observation rather than local tests alone.
- **assumptions_and_boundaries:** Combine isolated tests with controlled rollout and audit when environment behavior is material.
- **revision_decision:** Add method, pass evidence, and limitation for each claim family.
- **additional_insight_to_add:** Verify denial and removal end to end because happy-path loading can coexist with unsafe privileges and residue.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The exact repository verifiers and frozen file paths are known, while target host, commands, schema, installation, and protocol setup are absent.
- **supporting_reason:** Self-verification can execute here; target gates can only be discovered in a concrete project.
- **counterargument_or_limit:** Repository scripts can also evolve.
- **assumptions_and_boundaries:** Record current command evidence and avoid promising checks that do not exist.
- **revision_decision:** Separate observed self-verification from conditional host guidance.
- **additional_insight_to_add:** Missing target evidence should narrow the claim to a static or conceptual demonstration, not become an implicit pass.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** Verification is framed as a final command rather than feedback into capability scope, surface choice, permissions, and lifecycle.
- **supporting_reason:** A failed gate identifies which upstream assumption changed and which downstream evidence expired.
- **counterargument_or_limit:** Reinstalling and retesting every surface after each wording edit is wasteful.
- **assumptions_and_boundaries:** Use affected-gate selection plus structural invariants.
- **revision_decision:** Add staged cadence, invalidation mapping, and retained negative fixtures.
- **additional_insight_to_add:** Verification architecture should mirror artifact and lifecycle dependencies so a description edit reopens triggers while a manifest edit reopens package and install gates.

## Section 009: Agent Usage Decision Guide
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed opens this reference for any theme keyword or nearby workflow, which can overroute production commands, hooks, MCP services, settings, manifests, and security work.
- **supporting_reason:** Routing by learner goal, primary surface, target host, side effects, distribution claim, and evidence need selects the smallest applicable profile.
- **counterargument_or_limit:** Early discovery may not reveal whether an example will remain a skill or become a packaged plugin.
- **assumptions_and_boundaries:** Begin with a reversible preflight and reroute when a new invocation or lifecycle owner appears.
- **revision_decision:** Replace keyword matching with skill-demo, surface-companion, package-lifecycle, promotion-review, and avoid modes.
- **additional_insight_to_add:** The strongest trigger is a request to teach one extension capability safely, not the presence of the word plugin.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** Four process bullets do not state what an agent must know before creating files.
- **supporting_reason:** Learner outcome, user request, host, invocation, side effects, permissions, durability, distribution, and gates form an executable preflight.
- **counterargument_or_limit:** A tiny static correction can inherit most of these values unchanged.
- **assumptions_and_boundaries:** Confirm inherited boundaries and focus only what the edit can invalidate.
- **revision_decision:** Add full and reduced preflights with blocked-start conditions.
- **additional_insight_to_add:** Require one sentence naming who invokes the example and who owns every durable side effect.
### Question 03: When does the default work well?
- **current_section_observation:** The guide does not identify profiles such as trigger lesson, command walkthrough, safe hook fixture, protocol mock, manifest exercise, or template promotion.
- **supporting_reason:** Explicit profiles reduce context while retaining the evidence required by each teaching surface.
- **counterargument_or_limit:** A demonstration can gain a script, external service, or package during implementation.
- **assumptions_and_boundaries:** Re-run preflight when invocation, privilege, persistent state, external dependency, distribution, or support ownership changes.
- **revision_decision:** Add skill, companion, integrated, packaged, and promotion profiles.
- **additional_insight_to_add:** Profile selection remains provisional until the first real host load and user-behavior probe succeeds.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** There are no negative triggers for production implementation, security architecture, protocol conformance, incident response, marketplace publishing, or generic plugin development.
- **supporting_reason:** Early route-away prevents a small historical skill from replacing specialist host, protocol, security, or release guidance.
- **counterargument_or_limit:** This reference can still contribute the demonstration and copyability layer to specialized work.
- **assumptions_and_boundaries:** Retain it only for the bounded teaching artifact and its evidence.
- **revision_decision:** Add avoid and companion conditions with return artifacts.
- **additional_insight_to_add:** A task can involve a skill yet fall outside this reference when its decisive risk is privileged production automation rather than teaching.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** No routing comparison exists among example design, skill authoring, command implementation, hook safety, MCP servers, settings, manifests, testing, and distribution.
- **supporting_reason:** Each discipline owns different schemas, failure signals, permissions, and environments.
- **counterargument_or_limit:** Splitting guidance can obscure one capability that crosses several surfaces.
- **assumptions_and_boundaries:** Name one primary profile and exchange a compact capability contract at companion boundaries.
- **revision_decision:** Add routing matrix semantics and defer verified local paths to adjacent routing.
- **additional_insight_to_add:** Companion guidance should return a tested constraint or artifact, not a second competing walkthrough.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** The guide permits creation without confirming target host, schema, existing examples, neighboring triggers, package builder, permission model, fixture isolation, or lifecycle commands.
- **supporting_reason:** Missing facts make surface choice speculative and can invalidate every downstream file.
- **counterargument_or_limit:** An exploratory mock may intentionally precede host access.
- **assumptions_and_boundaries:** Label the mock, isolate it from live names and credentials, and define convergence evidence.
- **revision_decision:** Add project-discovery blockers, exploration state, and promotion criteria.
- **additional_insight_to_add:** An example with no known host or invocation path is a concept sketch, not an installable extension.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** The guide provides no profile contrasts.
- **supporting_reason:** A trigger-focused `SKILL.md` lesson is primary, a production GitHub MCP deployment routes away, and a real manifest wrapping the skill is a package-lifecycle companion case.
- **counterargument_or_limit:** A demonstration of the GitHub integration itself can remain in scope for teaching quality.
- **assumptions_and_boundaries:** Specialist guidance owns live protocol and security behavior; this reference owns the bounded lesson and safe fixture.
- **revision_decision:** Add primary, avoid, and conditional scenarios with reversal signals.
- **additional_insight_to_add:** Borderline work becomes in scope when the deliverable is explicitly an example and production guarantees have separate owners.
### Question 08: How can the important claims be verified?
- **current_section_observation:** The seed encourages gates but provides no evidence that this reference was the correct one to open.
- **supporting_reason:** A routing record can trace learner goal, target surface, host evidence, effects, permissions, lifecycle, omitted concerns, and expected gates.
- **counterargument_or_limit:** A prototype can disprove a careful initial route.
- **assumptions_and_boundaries:** Keep routing reversible until host discovery and first invocation confirm scope.
- **revision_decision:** Add preflight, post-load, and completion route checks.
- **additional_insight_to_add:** Record rejected profiles briefly so they reopen only when a named capability or lifecycle constraint changes.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The local source clearly targets a skill demonstration, while exact host fit, package rules, and current extension behavior are unknown.
- **supporting_reason:** Target schemas, help, existing artifacts, loader output, tests, and package contents can establish the local surface directly.
- **counterargument_or_limit:** Future distribution ownership and support commitments may not be encoded in source files.
- **assumptions_and_boundaries:** Ask for or record unresolved product and operational ownership before promotion.
- **revision_decision:** Present routing as project-evidence defaults with explicit human-owned uncertainty.
- **additional_insight_to_add:** Repository topology shows current files, while support ownership determines how safely an example can become a template.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** Usage routing is framed as document selection rather than allocation of schema, permissions, tests, package, lifecycle, and support ownership.
- **supporting_reason:** Choosing a profile determines which owner must prove host compatibility, trigger behavior, side effects, distribution, and cleanup.
- **counterargument_or_limit:** Ownership metadata can be disproportionate for a disposable personal lesson.
- **assumptions_and_boundaries:** Add coordination when examples are shared, installed, privileged, external, or published.
- **revision_decision:** Connect routing to handoff artifacts and change impact.
- **additional_insight_to_add:** A correct route minimizes duplicated walkthroughs while ensuring no extension failure falls between teaching and production owners.

## Section 010: User Journey Scenario
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed names a platform builder and several extension surfaces but does not trace one demonstration from user request through activation, behavior, evidence, and lifecycle boundary.
- **supporting_reason:** A stable show-skill-format journey can reveal how each design choice changes what the learner can observe and safely copy.
- **counterargument_or_limit:** A read-only skill does not cover hook reentrancy, protocol transport, live credentials, or destructive side effects.
- **assumptions_and_boundaries:** The scenario teaches surface and evidence reasoning, not every plugin mechanism.
- **revision_decision:** Expand the journey from target-host discovery through minimal skill, trigger isolation, walkthrough, conditional packaging, and handoff.
- **additional_insight_to_add:** Hold the learning outcome constant so optional wrapper and support-file choices can be compared without changing the lesson.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** Surface selection appears before the exact learner request, non-goal, host behavior, and evidence are established.
- **supporting_reason:** Discovery, capability contract, primary surface, minimal tree, description, content, validation, activation, behavior, and promotion form a causal sequence.
- **counterargument_or_limit:** An existing installed example may require characterization before redesign.
- **assumptions_and_boundaries:** Preserve observed supported behavior and copied consumers before changing the teaching contract.
- **revision_decision:** Use phased actions with candidate evidence and explicit stop or rework branches.
- **additional_insight_to_add:** Freeze the capability and non-goal before metadata so trigger wording cannot expand the lesson accidentally.
### Question 03: When does the default work well?
- **current_section_observation:** The starting state does not describe host version, validator, neighboring skills, distribution, or support ownership.
- **supporting_reason:** The chosen journey has bounded contextual guidance, deterministic Markdown output, no required external effect, and clear positive and negative requests.
- **counterargument_or_limit:** A host that cannot load local skills or requires a wrapper changes the minimum artifact.
- **assumptions_and_boundaries:** Add only the current host-required wrapper and retain skill behavior as the primary lesson.
- **revision_decision:** State fit conditions and conditional wrapper branch.
- **additional_insight_to_add:** Nonactivation is especially observable here because MCP, hook, and production-install requests should route elsewhere.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** No branch handles unsupported metadata, missing host refresh, broad activation, overlap, unused files, nondeterministic output, or fake install claims.
- **supporting_reason:** Named branches prevent a polished walkthrough from hiding an invalid or misleading artifact.
- **counterargument_or_limit:** Testing every wording variation would overwhelm a small lesson.
- **assumptions_and_boundaries:** Select cases from realistic phrasing, neighboring capabilities, and consequence of accidental selection.
- **revision_decision:** Add stop, narrow, repair, and route-away decisions at each phase.
- **additional_insight_to_add:** If the example must advertise a surface it cannot execute, split the lesson or label a mock rather than adding unverified files.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The scenario does not compare one-file skill, linked references, helper script, explicit command, or packaged wrapper.
- **supporting_reason:** These alternatives differ in context size, discoverability, determinism, executable risk, and lifecycle burden.
- **counterargument_or_limit:** Comparing every combination would distract from the skill-format lesson.
- **assumptions_and_boundaries:** Compare one disputed boundary at a time under the same learner outcome.
- **revision_decision:** Include decision branches without prescribing unsupported file schemas.
- **additional_insight_to_add:** The simplest candidate is one `SKILL.md`; another file must demonstrate why its separate lifetime or format is useful.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** The journey lacks a baseline, host identity, neighboring-trigger map, ASCII tree check, support-file closure, clean-state run, package status, and promotion decision.
- **supporting_reason:** These omissions make feedback ambiguous and allow author state to leak into the example.
- **counterargument_or_limit:** A disposable text-only sketch may not need package or clean-host evidence.
- **assumptions_and_boundaries:** Label it static and withhold host and distribution claims.
- **revision_decision:** Add candidate identity and phase-specific evidence to the journey.
- **additional_insight_to_add:** The walkthrough should run from a clean reader perspective, not from the author's remembered local setup.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** The generic scenario provides no complete outcome contrast.
- **supporting_reason:** A good skill activates for format requests and declines MCP deployment, a bad one triggers on generic plugin words and lists fake files, and a borderline wrapper has an untested manifest.
- **counterargument_or_limit:** A routing skill can intentionally accept broad extension requests.
- **assumptions_and_boundaries:** Broad routing must be its declared capability and produce tested specialist handoffs.
- **revision_decision:** Add good, bad, and conditional phase outcomes.
- **additional_insight_to_add:** The good result includes both a useful answer and proof that unrelated requests are untouched.
### Question 08: How can the important claims be verified?
- **current_section_observation:** Visual or structural review is implied, but no schema, host load, activation, output, link, ASCII, clean-copy, or optional lifecycle evidence is attached.
- **supporting_reason:** A phase packet proves that the lesson, files, and host interpretation agree.
- **counterargument_or_limit:** One scenario cannot establish every host version, language phrasing, or copier environment.
- **assumptions_and_boundaries:** Scope observed evidence and retain consequential untested combinations.
- **revision_decision:** Add exact gate categories and expected observations per phase.
- **additional_insight_to_add:** Verify one neighboring negative request in the host because trigger mistakes occur before the skill's well-written body can help.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The role narrative implies a structured process automatically yields an installable and recoverable plugin.
- **supporting_reason:** The process can establish a bounded skill lesson and expose missing lifecycle evidence.
- **counterargument_or_limit:** It cannot establish current APIs, all natural-language selection, teaching effectiveness, or distribution compatibility without target evidence.
- **assumptions_and_boundaries:** Separate historical illustration, target observation, test result, reviewer judgment, and unresolved risk.
- **revision_decision:** Label the journey as a worked decision model rather than measured outcome.
- **additional_insight_to_add:** A documented rejection is valuable when it prevents a wrapper or script from hardening around the wrong teaching goal.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The scenario ends at invocation and omits copying, maintenance, host upgrades, support transfer, and retirement.
- **supporting_reason:** The same evidence bundle can make later template reuse and breakage diagnosis safer.
- **counterargument_or_limit:** Archiving every workshop variant obscures the accepted path.
- **assumptions_and_boundaries:** Retain the accepted minimal artifact, one informative rejection, current host assumptions, and unresolved risks.
- **revision_decision:** Add durable handoff, promotion, and refresh triggers after acceptance.
- **additional_insight_to_add:** The journey's product is a retestable learning contract and clean-copy record, not merely a polished example directory.

## Section 011: Decision Tradeoff Guide
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed offers adopt, adapt, and avoid labels for the reference as a whole, but a demonstration contains independent choices about surface, files, fixtures, permissions, packaging, and promotion.
- **supporting_reason:** Separating choices lets a builder use the least complex option that still owns the teaching behavior and failure boundary.
- **counterargument_or_limit:** A tiny host-required scaffold may settle several choices together.
- **assumptions_and_boundaries:** Use the guide when a choice changes invocation, side effects, permissions, distribution, support, or verification.
- **revision_decision:** Replace generic confidence rows with an ordered demonstration decision ledger.
- **additional_insight_to_add:** A mechanism should earn its cost at the boundary where it is introduced rather than borrowing justification from the word plugin.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** The current adopt row treats local and external agreement as sufficient without asking whether a mechanism serves the learner goal.
- **supporting_reason:** Freeze the capability, inspect current host convention, choose the smallest surface and artifact, and add complexity only for demonstrated responsibility.
- **counterargument_or_limit:** Organizational training standards or host schemas can require a wrapper or support structure early.
- **assumptions_and_boundaries:** Label mandatory scaffold separately from inferred best design.
- **revision_decision:** Make learner behavior and target evidence entry criteria for every choice.
- **additional_insight_to_add:** A rejected simpler candidate is valuable because it names the responsibility that forced the larger example.
### Question 03: When does the default work well?
- **current_section_observation:** The seed does not identify host, audience, side-effect, or distribution conditions under which a one-file skill remains sufficient.
- **supporting_reason:** A one-file baseline works when guidance is contextual, bounded, deterministic, read-only, and the target loader supports it directly.
- **counterargument_or_limit:** High-consequence guidance can need examples or references even without executable side effects.
- **assumptions_and_boundaries:** Add support material for comprehension and verification only when the main file cannot carry it clearly.
- **revision_decision:** Add fit conditions and a named signal that reopens each decision.
- **additional_insight_to_add:** Co-location is economical while content changes together; separation becomes useful when material has a distinct reader, format, or lifecycle.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** "Avoid when evidence is thin" does not describe how a locally valid skill can still fail under trigger overlap, live effects, host upgrade, packaging, or removal.
- **supporting_reason:** A default becomes wrong when it cannot express the invocation contract, isolate a consequential effect, or verify the claimed lifecycle.
- **counterargument_or_limit:** Hypothetical future growth is insufficient to expand a simple example now.
- **assumptions_and_boundaries:** Require a current host constraint, learner need, observed failure, or near-term promotion before paying recurring complexity.
- **revision_decision:** Attach reversal signals and failure consequences to every row.
- **additional_insight_to_add:** The costly mistake is often failing to record when the simple example's assumptions stop holding.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The original table omits skill versus command, inline versus linked material, static versus runnable, mock versus live, one surface versus composition, and unwrapped versus packaged.
- **supporting_reason:** These alternatives expose distinct costs in activation, discoverability, context, determinism, privilege, realism, lifecycle, and support.
- **counterargument_or_limit:** Labels can distract from the responsibility each mechanism owns.
- **assumptions_and_boundaries:** Compare alternatives under one frozen learning contract and current host.
- **revision_decision:** Add bounded option pairs with choose, avoid, and verification prompts.
- **additional_insight_to_add:** Alternatives are comparable only when they teach the same outcome; otherwise the apparent tradeoff is a scope change.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Cost-of-being-wrong mentions wasted implementation but misses accidental activation, mock confusion, hidden credentials, package drift, unsupported fields, and cleanup residue.
- **supporting_reason:** These failures propagate from examples and cannot be disproved by prose review alone.
- **counterargument_or_limit:** Not every choice reaches credentials, installation, or removal.
- **assumptions_and_boundaries:** Include a failure branch only when the selected surface can produce it.
- **revision_decision:** Add consequence and disconfirming check to each option.
- **additional_insight_to_add:** When documentation and runtime both normalize a missing surface as optional, learners can mistake absence for supported behavior.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** No example shows how the same lesson leads to different choices under different host facts.
- **supporting_reason:** One `SKILL.md` is good for contextual guidance, a helper script is bad without executable need, and a wrapper is conditional when the host requires distribution metadata.
- **counterargument_or_limit:** A script can be justified by a deterministic validation or transformation the prose cannot perform.
- **assumptions_and_boundaries:** Judge the responsibility proven in the target, not the file type itself.
- **revision_decision:** Include good, bad, and borderline selections with fact-based reversal.
- **additional_insight_to_add:** Borderline examples should name the missing observation, such as current manifest necessity or clean removal.
### Question 08: How can the important claims be verified?
- **current_section_observation:** The seed asks whether evidence exists but does not connect choices to activation, link, fixture, permission, package, or lifecycle gates.
- **supporting_reason:** A defensible choice has a failing baseline observation and an owner for added complexity.
- **counterargument_or_limit:** Teaching clarity and maintainability are not fully automatable.
- **assumptions_and_boundaries:** Combine behavior evidence with concise reviewer and copier feedback.
- **revision_decision:** Ask what lesson differs, which gate observes it, and what evidence would reverse the choice.
- **additional_insight_to_add:** If the simpler candidate passes all relevant gates and copier review, the larger candidate has not earned its place.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** Historical content supplies candidates, while current host convention, learner comprehension, future reuse, and support ownership remain unestablished.
- **supporting_reason:** File and behavior observations can be direct, but teaching value and future variation require bounded judgment.
- **counterargument_or_limit:** Repeated copier failures and support history can strengthen maintainability evidence.
- **assumptions_and_boundaries:** Label historical fact, target result, policy, reviewer observation, and forecast separately.
- **revision_decision:** Add confidence and refresh fields to changing choices.
- **additional_insight_to_add:** Uncertainty should narrow claims and strengthen reversibility, not select the most elaborate scaffold.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The original guide treats a decision as complete once a pattern is selected.
- **supporting_reason:** Demonstration choices alter copied defaults, permissions, test placement, package layout, support, and future migration.
- **counterargument_or_limit:** Recording every implication can overwhelm a disposable lesson.
- **assumptions_and_boundaries:** Capture second-order effects when the example is shared, executable, privileged, installed, or supported.
- **revision_decision:** End with a ledger containing lesson, selected option, rejected baseline, evidence, owner, reversal signal, and lifecycle impact.
- **additional_insight_to_add:** Reversible local structure can stay lightweight, while copied permissions or package lifecycle deserve disproportionate review.

## Section 012: Local Corpus Hierarchy
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed calls one identical file canonical and the other supporting, implying independent authority that their matching bytes do not provide.
- **supporting_reason:** Reviewers need to decide which claims are historical observations, candidates, negative evidence, duplicate locators, or current target policy.
- **counterargument_or_limit:** The working path can still show where dependent repository material may exist.
- **assumptions_and_boundaries:** Separate locator value from claim corroboration.
- **revision_decision:** Replace file-level canonization with claim-level roles and explicit duplicate treatment.
- **additional_insight_to_add:** One document can provide useful teaching candidates and expose missing lifecycle evidence at the same time.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** Classification vocabulary is listed but no assignment procedure or promotion gate is defined.
- **supporting_reason:** A conservative default treats the archive as historical provenance, the working copy as duplicate discovery, and target behavior as applicability authority.
- **counterargument_or_limit:** A project may deliberately designate the copied skill as current policy.
- **assumptions_and_boundaries:** That status needs present governance, validator, ownership, and behavior evidence rather than path inference.
- **revision_decision:** Define assignment tests and apply roles by source region and claim.
- **additional_insight_to_add:** Promotion to template policy requires support and refresh ownership in addition to plausible content.
### Question 03: When does the default work well?
- **current_section_observation:** The local file is compact but spans metadata, invocation, applicability, structure, support material, content, and best practices.
- **supporting_reason:** Claim-level classification preserves useful breadth while keeping stale field or lifecycle assumptions from controlling the whole reference.
- **counterargument_or_limit:** Excessive segmentation can slow a simple lookup.
- **assumptions_and_boundaries:** Split only where confidence, currentness, applicability, or required gate differs materially.
- **revision_decision:** Group related regions into a compact role table.
- **additional_insight_to_add:** Historical templates are strongest as candidate indexes when every extracted rule retains its target-host gate.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** Whole-file authority would preserve broad trigger patterns, Unicode trees, optional folders, frontmatter claims, and implicit plugin status without current evidence.
- **supporting_reason:** Those claims can cause accidental activation, non-ASCII output, cargo-cult structure, schema rejection, and false lifecycle confidence.
- **counterargument_or_limit:** Some may remain valid in a particular supported host.
- **assumptions_and_boundaries:** Missing current evidence lowers authority without declaring every historical mechanism broken.
- **revision_decision:** Mark version-sensitive and incomplete-lifecycle spans conditional or negative until target proof exists.
- **additional_insight_to_add:** Internal omission can be useful negative evidence when a copier might infer unsupported behavior from the directory context.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The seed offers only canonical and supporting roles, omitting whole-file rejection, region classification, and claim-level provenance.
- **supporting_reason:** Whole-file status is simple but overbroad; claim records are precise but costly; region-level roles balance navigation and caution.
- **counterargument_or_limit:** A published privileged template can justify claim-level traceability.
- **assumptions_and_boundaries:** Increase granularity with privilege, distribution, compatibility, and propagation risk.
- **revision_decision:** Use region roles by default and claim records for changing or consequential behavior.
- **additional_insight_to_add:** Hierarchy granularity is a risk-control decision because demonstrations are copied beyond their original context.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Filename and polished headings can hide duplicate bytes, historical schema, absent negative tests, no host load, and no install or removal evidence.
- **supporting_reason:** Structural clarity is not runtime or lifecycle proof.
- **counterargument_or_limit:** Compiling or installing every conceptual snippet is wasteful when only the teaching principle is reused.
- **assumptions_and_boundaries:** Verify the smallest executable claim on which the adapted example depends.
- **revision_decision:** Add duplicate, version, trigger, file-closure, runtime, permission, and lifecycle checks.
- **additional_insight_to_add:** A Unicode tree is editorial format, while a broad description causing wrong activation is a semantic defect; hierarchy should distinguish them.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** No example shows how one source claim changes role after target inspection.
- **supporting_reason:** Focused purpose is a strong candidate, universal current field support is bad authority, and optional scripts are borderline until a real executable need and sandbox exist.
- **counterargument_or_limit:** Even focused purpose can conflict with a broader routing skill's deliberate contract.
- **assumptions_and_boundaries:** Candidate quality never bypasses target behavior and neighboring-surface evidence.
- **revision_decision:** Add promoted, rejected, and conditional claims with criteria.
- **additional_insight_to_add:** A useful borderline item names the missing observation, such as current validator acceptance or cleanup.
### Question 08: How can the important claims be verified?
- **current_section_observation:** The reviewer prompt does not require hash comparison, region extraction, contradiction or omission logging, host probes, or behavior validation.
- **supporting_reason:** A claim is traceable when its source region, role, target boundary, gate, and disposition can be followed without rereading both duplicate files.
- **counterargument_or_limit:** Line numbers can drift in a mutable working copy.
- **assumptions_and_boundaries:** Use archive path plus heading signal and content hash; add spans where the workflow freezes them.
- **revision_decision:** Define an extraction record and require current target evidence before promotion.
- **additional_insight_to_add:** Record rejected claims so future refresh distinguishes deliberate exclusion from omission.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** Exact duplicate content is known, but current host fields, activation semantics, teaching quality, package behavior, and ecosystem recommendations are unrefreshed.
- **supporting_reason:** Source text and omissions are directly observable; current applicability and learner outcomes need separate evidence.
- **counterargument_or_limit:** Stable principles such as focus and actionable guidance are less version-sensitive.
- **assumptions_and_boundaries:** Confidence attaches to one claim and boundary, not the whole file.
- **revision_decision:** Label historical observation, synthesis, unresolved currentness, and target judgment in the hierarchy.
- **additional_insight_to_add:** A stable teaching principle may survive while its sample metadata and path expire.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The current hierarchy ends at source selection and omits maintenance after a claim becomes a reusable template rule.
- **supporting_reason:** Promoted guidance creates ownership, tests, compatibility, deprecation, and refresh obligations.
- **counterargument_or_limit:** Orientation-only notes may not warrant a formal lifecycle owner.
- **assumptions_and_boundaries:** Add lifecycle metadata when guidance is scaffolded, published, executable, privileged, or repeatedly reused.
- **revision_decision:** Define promotion, retention, demotion, supersession, and retirement rules.
- **additional_insight_to_add:** Hierarchy should be reversible so target evidence can demote a copied rule without rewriting the archive.

## Section 013: Theme Specific Artifact
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed's three artifact fields do not expose whether capability, surface, host, files, triggers, permissions, lifecycle, and evidence agree.
- **supporting_reason:** A demonstration contract can make the lesson and every operational claim reviewable before optional mechanisms fragment it.
- **counterargument_or_limit:** A static one-paragraph illustration does not need a full package ledger.
- **assumptions_and_boundaries:** Use the artifact for runnable, host-loaded, copied, packaged, permissioned, or promoted examples and scale it down for orientation.
- **revision_decision:** Replace the generic shell with a scope-and-evidence contract plus a completed skill example.
- **additional_insight_to_add:** The artifact should reveal missing proof rather than become a second manifest or duplicate of the skill body.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** The current fields start with user goal but provide no stable unit connecting invocation and lifecycle evidence.
- **supporting_reason:** One artifact centered on a capability identity and support status keeps files, triggers, effects, permissions, gates, and promotion causally aligned.
- **counterargument_or_limit:** A disposable workshop can omit long-term ownership and compatibility.
- **assumptions_and_boundaries:** It must still label disposal scope and prevent unsupported distribution.
- **revision_decision:** Make capability, status, and claimed surfaces the artifact spine, then link authoritative schemas and files rather than copying them.
- **additional_insight_to_add:** Status vocabulary prevents a statically valid file from being described as loaded, installable, or supported.
### Question 03: When does the default work well?
- **current_section_observation:** The seed gives no fit criteria beyond the topic name.
- **supporting_reason:** The contract works when several reviewers or copiers must agree on what the example teaches and which environment claims are proven.
- **counterargument_or_limit:** It is disproportionate for an ephemeral sentence with no code or host claim.
- **assumptions_and_boundaries:** Scale fields with invocation power, side effects, distribution, and reuse.
- **revision_decision:** Add required and conditional groups for static, loaded, integrated, packaged, and promoted status.
- **additional_insight_to_add:** Artifact size should track lifecycle and trust fan-out rather than source line count.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** A contract table can look complete while repeating metadata, listing generic gates, or marking absent behavior as optional.
- **supporting_reason:** Duplicated schema drifts and vague statuses allow unsupported surfaces to hide behind documentation.
- **counterargument_or_limit:** A short metadata excerpt can clarify a trigger or mapping.
- **assumptions_and_boundaries:** Link authoritative declarations and quote only the minimal discriminant needed for review.
- **revision_decision:** Add invalid-artifact checks for duplicated truth, unowned claims, generic evidence, and silent blanks.
- **additional_insight_to_add:** A blank must mean not applicable with a reason or unresolved with an owner, never unexamined.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The seed does not compare a demonstration contract with manifest, README, tutorial, test plan, package inventory, or architecture record.
- **supporting_reason:** These artifacts answer schema, onboarding, execution, package, and rationale questions differently.
- **counterargument_or_limit:** Maintaining all of them manually would multiply drift.
- **assumptions_and_boundaries:** Treat host schema, source files, and tests as authorities and use the contract as a pointer-rich reconciliation view.
- **revision_decision:** State when to link, generate, or omit companions and prohibit replacement of executable evidence.
- **additional_insight_to_add:** The contract adds value where individually valid files and walkthroughs disagree about supported status.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** No fields cover target version, non-goal, trigger negatives, overlap, side effects, credentials, permission denial, package contents, removal residue, clean copying, or promotion.
- **supporting_reason:** These concerns fail between author, host, learner, and distributor even when the happy path reads well.
- **counterargument_or_limit:** Adding every conditional field to a static sketch obscures its core lesson.
- **assumptions_and_boundaries:** Select groups by claimed surface and mark whole groups out of scope once with reason.
- **revision_decision:** Add preflight and conditional completion rules around the contract.
- **additional_insight_to_add:** Permission and cleanup belong at capability scope, while a malformed trigger case belongs to the specific invocation surface.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** The shell has no completed example showing sufficient specificity.
- **supporting_reason:** A good skill record names positive and negative triggers, no side effect, host-loaded status, and clean-copy evidence; a bad record says plugin works; a borderline record says installable from manifest validation alone.
- **counterargument_or_limit:** A distribution wrapper can be out of scope while the inner skill remains complete.
- **assumptions_and_boundaries:** Status each layer independently rather than lowering or raising all claims together.
- **revision_decision:** Include one completed skill record plus invalid and conditional contrasts.
- **additional_insight_to_add:** The best completed example highlights the boundary it deliberately does not claim.
### Question 08: How can the important claims be verified?
- **current_section_observation:** The original verification field points generally to a command set without mapping claims to observations.
- **supporting_reason:** Every claimed status should cite at least one direct gate and one copier- or user-observable result when behavior is involved.
- **counterargument_or_limit:** Production telemetry and broad teaching outcomes may be unavailable before publication.
- **assumptions_and_boundaries:** Prepublication evidence can prove mechanics and reviewer comprehension while later feedback tests repeated use.
- **revision_decision:** Add evidence identifiers, expected observations, limits, and unresolved combinations.
- **additional_insight_to_add:** A gate that cannot distinguish static, loaded, and installable status is too broad for the claim.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** Artifact completion can establish intended lesson and retained tests but not current public guidance, all host versions, or teaching success across users.
- **supporting_reason:** Explicit evidence classes keep mechanical observations separate from usability and support judgment.
- **counterargument_or_limit:** Repeated clean-copy and user studies can reduce teaching uncertainty.
- **assumptions_and_boundaries:** Label intended contract, target observation, automated result, reviewer result, and unresolved risk independently.
- **revision_decision:** Add confidence and freshness at artifact scope.
- **additional_insight_to_add:** Agreement among files can still encode the wrong lesson, so learner outcome remains a human-owned judgment.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The seed artifact ends at verification and omits maintenance when host schema, triggers, package, or support status changes.
- **supporting_reason:** The contract can become an impact map for future copies if it records authorities, owners, and invalidation triggers.
- **counterargument_or_limit:** Keeping every workshop contract forever creates stale parallel documentation.
- **assumptions_and_boundaries:** Retain while the example is published, copied, installed, supported, or used as a regression fixture.
- **revision_decision:** Define update, promotion, demotion, and retirement rules.
- **additional_insight_to_add:** Retiring the contract should leave authoritative files and tests intact because the artifact coordinates evidence rather than owning behavior.

## Section 014: Worked Example Set
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed's good, bad, and borderline statements discuss source usage but do not show how a demonstration contract becomes files, cases, and observations.
- **supporting_reason:** Worked examples should help a builder choose trigger scope, minimal structure, support material, status, and lifecycle evidence while seeing the failure each prevents.
- **counterargument_or_limit:** Example metadata can be mistaken for current host prescription.
- **assumptions_and_boundaries:** Label syntax illustrative, adapt it to target schema, and make behavior and gates explicit.
- **revision_decision:** Replace meta-usage prose with a bounded skill candidate, trigger matrix, optional-file contrast, fake-plugin anti-example, and conditional wrapper.
- **additional_insight_to_add:** All examples should share one skill-format lesson so file and lifecycle differences remain comparable.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** No default sequence connects user wording to metadata, body, host selection, result, and clean copying.
- **supporting_reason:** Capability, bounded description, minimal body, positive and negative cases, host evidence, and copier replay form a complete teaching loop.
- **counterargument_or_limit:** A host-required wrapper can add mandatory files before behavior is exercised.
- **assumptions_and_boundaries:** Keep wrapper mechanics separate and preserve the inner skill contract.
- **revision_decision:** Present examples in causal order and name authority at every conversion.
- **additional_insight_to_add:** Conversions should reduce ambiguity: user phrases to trigger contract, source to host-loaded artifact, and walkthrough to reproducible lesson.
### Question 03: When does the default work well?
- **current_section_observation:** The seed does not identify lessons that benefit from a one-file contextual skill.
- **supporting_reason:** The pattern fits bounded explanatory guidance with recognizable intents, no live side effect, and a deterministic answer shape.
- **counterargument_or_limit:** Commands, hooks, and protocol services need different runtime examples.
- **assumptions_and_boundaries:** Route those mechanics while retaining minimality, fixture, failure, and copyability principles.
- **revision_decision:** State the worked set's contextual-skill scope and intentional omissions.
- **additional_insight_to_add:** A bounded skill is useful because trigger overlap can be exercised without mixing in permission or network noise.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** Current examples do not expose broad trigger capture, stale fields, optional-file drift, hidden author state, mock/live confusion, or fake lifecycle.
- **supporting_reason:** These are common demonstration failures that polished happy-path prose conceals.
- **counterargument_or_limit:** A static example can intentionally omit host execution.
- **assumptions_and_boundaries:** Label conceptual status and do not infer selection or installation.
- **revision_decision:** Add negative examples and repair rules for each boundary.
- **additional_insight_to_add:** If a source tree looks installable while its lifecycle is absent, presentation has become misleading evidence.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The seed does not compare one-file skill with reference split, static fixture with runnable script, mock with live integration, or unwrapped with packaged form.
- **supporting_reason:** Each alternative shifts context, determinism, privilege, realism, package, and support obligations.
- **counterargument_or_limit:** Target tools can provide equivalent mechanisms under different names.
- **assumptions_and_boundaries:** Compare semantic responsibility and testability rather than labels.
- **revision_decision:** Pair each worked choice with an acceptable alternative and selection condition.
- **additional_insight_to_add:** Alternatives are equivalent only when they preserve user outcome, noninterference, and cleanup under the same evidence.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** The historical corpus supplies a broad description pattern and optional tree but no negative trigger, current schema, package, or clean-copy test.
- **supporting_reason:** Using those omissions in the worked set demonstrates how a plausible template becomes safer through added evidence.
- **counterargument_or_limit:** The source may have been intentionally introductory rather than operational.
- **assumptions_and_boundaries:** Preserve its teaching role while refusing unsupported status.
- **revision_decision:** Use source gaps as conditional branches rather than accusing the artifact of runtime failure.
- **additional_insight_to_add:** Tests should implement the production selection contract exactly; a keyword-only simulation can validate a different router.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** Labels are generic and do not show observable consequences.
- **supporting_reason:** A good candidate selects format requests and declines deployments, a bad directory advertises absent surfaces, and a wrapper is borderline until built-package lifecycle passes.
- **counterargument_or_limit:** A broad example router can intentionally hand off several extension requests.
- **assumptions_and_boundaries:** Routing must be its explicit outcome and specialist handoffs must be tested.
- **revision_decision:** Add file, behavior, and lifecycle contrasts.
- **additional_insight_to_add:** Negative examples should include the learner's false conclusion, not only the author's structural mistake.
### Question 08: How can the important claims be verified?
- **current_section_observation:** The seed says to write a gate but supplies no fixtures or expected observations.
- **supporting_reason:** Metadata validation, trigger cases, answer-shape review, ASCII scan, link closure, clean copying, and conditional lifecycle tests can verify the set.
- **counterargument_or_limit:** Illustrative snippets cannot be run against an unknown host.
- **assumptions_and_boundaries:** Adapt exact schema and commands, then preserve behavior vectors and assertions.
- **revision_decision:** Attach an evidence matrix instead of claiming the examples prove themselves.
- **additional_insight_to_add:** Mutating one trigger or removing one required file should fail a focused gate or the suite does not protect that lesson boundary.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** Focus, minimality, and negative-case principles are stable, but exact metadata, loader, routing, and package commands are unknown.
- **supporting_reason:** Examples can demonstrate bounded reasoning while leaving mechanics project-dependent.
- **counterargument_or_limit:** Even illustrative wording can shape learner expectations strongly.
- **assumptions_and_boundaries:** Review examples for misleading implication as well as syntax.
- **revision_decision:** Label semantic sketches with concrete obligations and target-owned adapters.
- **additional_insight_to_add:** A version-neutral example is useful only when it can still produce a disconfirming target test.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The seed does not explain how examples affect future scaffolds, permissions, support, or host migration.
- **supporting_reason:** Copied names and trigger phrases become coordination vocabulary and compatibility expectations.
- **counterargument_or_limit:** Exposing internal workshop names as public contracts can freeze incidental detail.
- **assumptions_and_boundaries:** Distinguish local teaching identity from published package and capability identity.
- **revision_decision:** Add evolution notes for copied examples, unknown host states, promotion, and retirement.
- **additional_insight_to_add:** Strict internal validation and tolerant migration can coexist when current and legacy examples are normalized deliberately.

## Section 015: Outcome Metrics and Feedback Loops
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed names install, invoke, debug, and remove usability without defining status, denominator, evidence, or which design action changes.
- **supporting_reason:** Teams need measures that can trigger narrowing, repair, demotion, promotion, rollback, or retirement of a demonstration.
- **counterargument_or_limit:** Metrics can distort teaching when treated as universal scores or author productivity measures.
- **assumptions_and_boundaries:** Evaluate the artifact and learner workflow, never rank individual creators or claim causality without comparison.
- **revision_decision:** Add learner, activation, behavior, safety, lifecycle, copyability, and evidence-quality measures tied to actions.
- **additional_insight_to_add:** Every retained measure should name the decision it changes or be removed as observation overhead.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** No baseline, denominator, sample, status, owner, or threshold-setting method accompanies the current indicator.
- **supporting_reason:** A target-specific baseline plus owner-defined decision threshold prevents arbitrary precision.
- **counterargument_or_limit:** A new lesson may begin with only deterministic cases and qualitative copier review.
- **assumptions_and_boundaries:** Start with gate pass or fail and classified feedback, then add rates or distributions when samples are trustworthy.
- **revision_decision:** Require definition, source, population, status level, window, owner, action, and blind spot.
- **additional_insight_to_add:** Explicitly lacking a baseline is better than a fabricated target because it identifies the first measurement task.
### Question 03: When does the default work well?
- **current_section_observation:** The seed does not distinguish authoring feedback, host validation, copier rehearsal, publication, and support incidents.
- **supporting_reason:** Layered loops work when fast gates prevent mechanical defects and slower user evidence tests comprehension and reuse assumptions.
- **counterargument_or_limit:** Low-use examples may never produce stable quantitative trends.
- **assumptions_and_boundaries:** Combine deterministic cases, small copier studies, and classified support feedback without overinterpreting sparse data.
- **revision_decision:** Organize loops by decision latency and evidence source.
- **additional_insight_to_add:** Feedback speed should match reversibility: a schema failure blocks a file, while a copied-template defect may require demotion and migration.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** Successful activation can rise while the skill captures unrelated work, emits misleading guidance, gains permissions, or leaves removal residue.
- **supporting_reason:** One positive outcome invites local optimization that shifts cost to noninterference and lifecycle.
- **counterargument_or_limit:** Too many guardrails make a small example hard to review.
- **assumptions_and_boundaries:** Retain guardrails only for claimed surfaces and credible copied harm.
- **revision_decision:** Pair each primary outcome with bounded counter-metrics and retirement rules.
- **additional_insight_to_add:** A higher invocation count can indicate trigger overbreadth rather than greater teaching value.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The seed does not compare automated gates, reviewer assessment, clean-copy tasks, support issues, telemetry, and template change history.
- **supporting_reason:** These sources differ in speed, realism, privacy, coverage, and causal interpretation.
- **counterargument_or_limit:** Correlating sources adds analysis and instrumentation cost.
- **assumptions_and_boundaries:** Use the cheapest source that can disconfirm the decision and add another only for an important blind spot.
- **revision_decision:** Map each outcome to evidence source and limitation.
- **additional_insight_to_add:** Disagreement between host tests and copier results often reveals hidden author context or unclear documentation.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** The feedback loop omits trigger sampling bias, natural-language drift, hidden cache, author-state contamination, sensitive logs, duplicate copies, denominator drift, stale host versions, and silent measurement failure.
- **supporting_reason:** Poor measurement can expose data or produce confident but misleading promotion decisions.
- **counterargument_or_limit:** Early workshops may rely on manual notes rather than instrumentation.
- **assumptions_and_boundaries:** Keep notes bounded and anonymous, record environment, and define production evidence before publication.
- **revision_decision:** Add privacy, sample, environment, version, status, and absence-path checks.
- **additional_insight_to_add:** Activation cases should record intent category without retaining private user content unnecessarily.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** No example distinguishes an actionable demonstration measure from a vanity count.
- **supporting_reason:** Clean-copy completion with failure classification is actionable, file count is irrelevant, and activation rate is borderline without negative-request denominator.
- **counterargument_or_limit:** File or time counts can aid planning even when they do not establish quality.
- **assumptions_and_boundaries:** Keep effort measures separate from learner, safety, and lifecycle claims.
- **revision_decision:** Add good, bad, and conditional measures with decisions supported.
- **additional_insight_to_add:** A metric is safer when a counter-measure can reveal the most likely gaming or reclassification path.
### Question 08: How can the important claims be verified?
- **current_section_observation:** Re-running the reference verifier proves structure but cannot validate target activation, clean copying, permissions, package lifecycle, or teaching.
- **supporting_reason:** Fixture tests, clean hosts, deliberate mutations, copier tasks, lifecycle drills, and support sampling can verify collection and interpretation.
- **counterargument_or_limit:** Teaching effectiveness remains uncertain without representative learners and context.
- **assumptions_and_boundaries:** Phrase observed task outcomes separately from general learning claims.
- **revision_decision:** Add a verification ladder from event or test construction through promotion review.
- **additional_insight_to_add:** Test the missing-signal path so absent feedback is not mistaken for successful silent use.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The reference can define gate categories but has no target host population, learner cohort, usage baseline, support history, or promotion objective.
- **supporting_reason:** Project and program data determine useful thresholds and meaningful change.
- **counterargument_or_limit:** Schema, noninterference, no-secret, and residue gates can be decisive without large samples.
- **assumptions_and_boundaries:** Separate invariant gates from distributional measures and reviewer judgment.
- **revision_decision:** Avoid universal percentages and require local baselines for improvement claims.
- **additional_insight_to_add:** Confidence should rise through convergence of independent evidence rather than more decimal places.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The seed refreshes on tooling release but not when trigger language, copied use, support ownership, or status changes.
- **supporting_reason:** Feedback definitions drift as examples move from conceptual to loaded, packaged, and promoted.
- **counterargument_or_limit:** Constant metric redesign destroys continuity.
- **assumptions_and_boundaries:** Version metric definitions, overlap old and new definitions during migration, and retire the old definition only after consumers move.
- **revision_decision:** Add feedback-to-example, feedback-to-test, and demotion loops with owners.
- **additional_insight_to_add:** The strongest long-term outcome is a shorter interval from copied failure to corrected lesson, regression gate, and migration note.

## Section 016: Completeness Checklist
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed checklist confirms seven narrative ingredients but cannot decide whether a demonstration is conceptual, source-valid, host-loaded, behavior-validated, packaged, or reusable.
- **supporting_reason:** Readiness depends on the highest claimed status because each status adds observable obligations that prose alone cannot satisfy.
- **counterargument_or_limit:** A single checklist is easier to scan than a status model with conditional branches.
- **assumptions_and_boundaries:** Keep one ordered checklist, but mark each item as universal or activated by a claimed surface and status.
- **revision_decision:** Convert completeness into a claim, artifact, evidence, failure, recovery, and lifecycle closure decision.
- **additional_insight_to_add:** A demonstration is complete only relative to a declared teaching outcome and evidence level, never complete in the abstract.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** Current checks ask whether content exists without requiring an owner, target version, expected observation, or disconfirming case.
- **supporting_reason:** Presence checks reward decorative coverage, while closure checks reveal whether a learner can reproduce and challenge the lesson.
- **counterargument_or_limit:** Requiring executable evidence for a conceptual example would erase useful early design artifacts.
- **assumptions_and_boundaries:** Conceptual artifacts may use review evidence, provided they explicitly decline runtime and package claims.
- **revision_decision:** Default to a tiered checklist whose first gate declares scope and whose later gates activate only for claimed capabilities.
- **additional_insight_to_add:** The smallest complete demonstration is the one with the fewest claims that still teaches the target decision end to end.
### Question 03: When does the default work well?
- **current_section_observation:** The seven seed bullets work as an editorial reminder after scope, host, and evidence obligations are already understood.
- **supporting_reason:** A tiered gate remains concise when the artifact has one primary lesson, a bounded surface, deterministic fixtures, and explicit non-goals.
- **counterargument_or_limit:** Composed demonstrations can require several interacting surfaces whose closure cannot be evaluated independently.
- **assumptions_and_boundaries:** For a composition lesson, declare the interaction itself as the teaching outcome and add cross-surface observations.
- **revision_decision:** Preserve the editorial checks inside a larger sequence from contract through clean-copy and retirement readiness.
- **additional_insight_to_add:** Checklist order should follow the learner journey so an early scope failure prevents expensive package and lifecycle work.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** A binary complete label fails when conditional requirements are silently skipped or when lower-level evidence is used to imply higher-level behavior.
- **supporting_reason:** A source-valid tree can look packaged, and a successful load can look behaviorally correct, even though neither inference is warranted.
- **counterargument_or_limit:** Excess status labeling can burden a one-file teaching note with release-process ceremony.
- **assumptions_and_boundaries:** Apply status labels at publication or handoff boundaries, not to every private drafting edit.
- **revision_decision:** Prohibit aggregate completion until every claimed-status gate passes or an exception names owner, consequence, and expiry.
- **additional_insight_to_add:** An unchecked conditional item is not automatically irrelevant; irrelevance itself should be justified by the declared surface matrix.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The seed does not compare a compact editorial checklist, a claim-evidence matrix, an automated verifier, and a release review.
- **supporting_reason:** These mechanisms trade scan speed, precision, enforceability, target coupling, and maintenance cost.
- **counterargument_or_limit:** Maintaining several representations can create conflicting definitions of done.
- **assumptions_and_boundaries:** Keep the reference checklist authoritative and derive automation or review forms from stable requirement identifiers when available.
- **revision_decision:** Use editorial review for conceptual claims, deterministic gates for machine-observable claims, and human rehearsal for copyability.
- **additional_insight_to_add:** Automation should remove repeated observation work while leaving judgment about lesson clarity visible and owned.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Existing bullets can all be checked while triggers overlap, fixtures depend on author state, permissions are excessive, removal leaves residue, or evidence is stale.
- **supporting_reason:** Those omissions are the common routes from an attractive example to an unsafe copied template.
- **counterargument_or_limit:** Permission, install, and removal checks do not apply to a static skill-format note without a distribution wrapper.
- **assumptions_and_boundaries:** Activate operational checks only when the demonstration claims the corresponding surface or lifecycle.
- **revision_decision:** Add noninterference, determinism, least privilege, clean-host closure, version, recovery, and residue checks.
- **additional_insight_to_add:** The checklist must catch misleading implication, not only malformed files, because learners copy inferred contracts too.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** The seed has no completed checklist example showing how evidence status affects a release decision.
- **supporting_reason:** A good skill-format example passes scope, schema-adapted review, positive and negative fixtures, and clean-copy checks; a directory-only showcase fails capability closure.
- **counterargument_or_limit:** A source tree can be useful even when the target host is temporarily unavailable.
- **assumptions_and_boundaries:** That tree is borderline only if it is labeled source-valid and carries a concrete host-validation next action.
- **revision_decision:** Add pass, fail, conditional, and not-claimed outcomes with examples of acceptable evidence.
- **additional_insight_to_add:** A not-claimed outcome is honest scope control, whereas an unexamined blank is missing evidence.
### Question 08: How can the important claims be verified?
- **current_section_observation:** The current checklist relies on reviewer interpretation and provides no mapping from item to command, fixture, observation, or failure response.
- **supporting_reason:** A claim-to-gate table, deliberate mutations, clean-host run, and independent copy rehearsal make completion falsifiable.
- **counterargument_or_limit:** Host-specific commands cannot be supplied accurately from the frozen local corpus alone.
- **assumptions_and_boundaries:** Preserve semantic assertions and require maintainers to bind them to authoritative target tooling.
- **revision_decision:** Require evidence references, recorded environment, and an explicit failing observation for each machine-checkable gate.
- **additional_insight_to_add:** Removing a required file or broadening a trigger should make the checklist fail, proving that its evidence protects the advertised boundary.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The corpus supports focus, minimal structure, descriptive activation, and examples, but not a current plugin schema or universal package workflow.
- **supporting_reason:** Completeness can be defined structurally while exact adapters and compatibility versions remain target-owned.
- **counterargument_or_limit:** Structural confidence does not guarantee that learners understand the intended decision.
- **assumptions_and_boundaries:** Treat independent copier observation as bounded evidence rather than a general usability statistic.
- **revision_decision:** Separate invariant completeness obligations, locally verified host facts, and reviewer judgment in the checklist result.
- **additional_insight_to_add:** Confidence should attach to individual claims and observations instead of inheriting from a single green release label.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The seed checklist ends at adjacent routing and does not cover ownership, copied descendants, demotion, migration, or retirement.
- **supporting_reason:** Published demonstrations become dependency roots whose examples and phrases can persist after their original host contract changes.
- **counterargument_or_limit:** Tracking every private copy is impossible and can create false inventory confidence.
- **assumptions_and_boundaries:** Track maintained distributions and known descendants, then provide discoverable migration guidance for unknown copies.
- **revision_decision:** Add ownership, refresh trigger, compatibility, promotion, demotion, and retirement closure to final readiness.
- **additional_insight_to_add:** Completeness is durable when every claimed dependency has both a verification path and a responsible change path.

## Section 017: Adjacent Reference Routing
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed says to use specialized references after selecting a surface but offers three circular non-destination labels named example, plugin, and demonstration.
- **supporting_reason:** A learner needs to know when the teaching-contract problem has become a command, hook, MCP, settings, manifest, skill, distribution, or plugin-creation problem.
- **counterargument_or_limit:** A demonstration can legitimately compose several surfaces and cannot always be routed to one document.
- **assumptions_and_boundaries:** Route the primary decision first, then identify secondary references for explicit composition obligations.
- **revision_decision:** Replace generic adjacency with concrete repository paths, entry signals, expected outcomes, and return conditions.
- **additional_insight_to_add:** Routing should occur at the first irreversible capability or lifecycle choice, before copied structure hardens the wrong contract.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** Current guidance begins after a surface is selected but gives no method for distinguishing teaching format from implementation mechanics.
- **supporting_reason:** The primary user decision and first durable side effect discriminate neighboring references more reliably than shared words such as plugin or example.
- **counterargument_or_limit:** Some requests are exploratory and do not yet have a stable primary decision.
- **assumptions_and_boundaries:** Keep the current reference for bounded comparison until one surface owns the acceptance criteria.
- **revision_decision:** Default to a decision table keyed by activation, effect timing, external protocol, configuration, packaging, and reuse intent.
- **additional_insight_to_add:** A good route states what question the destination answers and what evidence returns the user to demonstration-level review.
### Question 03: When does the default work well?
- **current_section_observation:** Surface-first routing works when a request names one mechanism and asks for its authoritative file, behavior, validation, or lifecycle.
- **supporting_reason:** Specialized references can then carry schema and operational detail without bloating the demonstration contract.
- **counterargument_or_limit:** A packaging tutorial may cross manifest, command, setting, and installation boundaries intentionally.
- **assumptions_and_boundaries:** Treat composition as a named lesson with one owner and a declared interaction matrix.
- **revision_decision:** Add direct routes for single-surface work and a composition route for coordinated examples.
- **additional_insight_to_add:** Route depth should follow risk: a conceptual comparison needs fewer destinations than a distributable, privileged integration.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** Filename similarity can route users to a broad plugin page even when they need a narrow trigger, protocol, or lifecycle answer.
- **supporting_reason:** Misrouting imports irrelevant structure and may hide permissions, external failure, or uninstall obligations.
- **counterargument_or_limit:** Over-specialization forces readers to assemble basic context from many references.
- **assumptions_and_boundaries:** Keep common teaching-contract decisions here and route only mechanics that have distinct evidence owners.
- **revision_decision:** Add avoid signals, escalation conditions, and a rule against circular referrals.
- **additional_insight_to_add:** If two references each defer the acceptance criterion to the other, ownership is missing rather than routing complete.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The seed does not compare one canonical destination, a route stack, an index search, and a bespoke composition guide.
- **supporting_reason:** These options trade speed, context fragmentation, duplication, discoverability, and cross-surface coherence.
- **counterargument_or_limit:** A route stack can overwhelm a learner who only needs one next action.
- **assumptions_and_boundaries:** List one primary destination and add secondary routes only for capabilities actually claimed.
- **revision_decision:** Prefer a single owner for each decision, with composition tables used only when interaction is the teaching outcome.
- **additional_insight_to_add:** Cross-links should share semantic entry criteria, not copy volatile schema instructions into several references.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Adjacent files can be absent, renamed, stale, semantically overlapping, or at a different evidence status than this evolved reference.
- **supporting_reason:** A valid path does not prove current guidance, and a current destination does not automatically validate the source example.
- **counterargument_or_limit:** Revalidating every destination on each local edit is expensive.
- **assumptions_and_boundaries:** Check path and purpose at authoring time; refresh target mechanics when the route is used for implementation.
- **revision_decision:** Add existence, heading, entry-condition, ownership, and freshness checks for routing.
- **additional_insight_to_add:** Treat a cross-reference as a dependency with compatibility risk rather than as decorative further reading.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** No scenario shows a request moving from demonstration design into a specialized reference and back to integrated review.
- **supporting_reason:** A command implementation routes directly to command development; a directory named plugin routes nowhere until capability is known; a command plus hook tutorial requires explicit composition.
- **counterargument_or_limit:** A user may ask for a complete plugin without knowing which surfaces it needs.
- **assumptions_and_boundaries:** Start with the capability contract and route each justified surface after scope discovery.
- **revision_decision:** Add good direct routes, bad label-based routes, and borderline multi-surface routes.
- **additional_insight_to_add:** The return path should reapply noninterference, clean-copy, permission, and lifecycle checks across the assembled demonstration.
### Question 08: How can the important claims be verified?
- **current_section_observation:** The seed provides no command to confirm that destinations exist or that their opening contracts match the route description.
- **supporting_reason:** Repository path checks and focused heading or thesis inspection can detect broken and semantically stale links.
- **counterargument_or_limit:** Static checks cannot establish that a destination reflects the current external host.
- **assumptions_and_boundaries:** Target implementation still requires the destination's own authoritative-source and focused-verifier gates.
- **revision_decision:** Add route-table validation and a manual cycle and ownership review.
- **additional_insight_to_add:** A route mutation test can replace a destination with a similarly named wrong file and verify that purpose checks reject it.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** Concrete neighboring paths exist in the repository, but their current evolution status and external-source freshness were not audited for this section.
- **supporting_reason:** Path existence supports navigation while destination authority must remain independently scoped.
- **counterargument_or_limit:** Users may interpret a concrete route as an endorsement of every claim in the target reference.
- **assumptions_and_boundaries:** State that routing selects a question owner, not a transitive guarantee of correctness.
- **revision_decision:** Separate confirmed path inventory from unverified content currentness.
- **additional_insight_to_add:** Confidence should transfer only for the destination's explicitly verified claims, versions, and evidence levels.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The seed treats adjacency as a final appendix rather than a control mechanism for scope and ownership.
- **supporting_reason:** Early routing reduces duplicated instructions, prevents capability theater, and exposes when no reference owns a cross-surface decision.
- **counterargument_or_limit:** Excessive routing can become bureaucracy that interrupts small teaching tasks.
- **assumptions_and_boundaries:** Route only when a specialized contract materially changes files, effects, evidence, or lifecycle.
- **revision_decision:** Turn adjacent routing into a reversible decision graph with primary, secondary, and return gates.
- **additional_insight_to_add:** Maintained routes form an architectural map of extension responsibilities and reveal missing ownership before failures do.

## Section 018: Workload Model
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed frames the reference as an agent workflow and imposes ten-source and three-delegation capacities without evidence linking those numbers to comprehension or reliability.
- **supporting_reason:** Authors need to decide whether one demonstration remains a coherent lesson, needs supporting artifacts, or should split into separately owned examples.
- **counterargument_or_limit:** File and task counts are quick planning heuristics even when they are not quality limits.
- **assumptions_and_boundaries:** Retain counts as locally measured descriptors, never as universal pass criteria.
- **revision_decision:** Model workload through lesson, surface, state, environment, evidence, lifecycle, and copy-support dimensions.
- **additional_insight_to_add:** The constraining workload is usually interaction uncertainty, not the number of source files.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** The current default mixes planning, tool use, context loading, delegation, and execution without selecting a primary learner outcome.
- **supporting_reason:** One primary lesson, one primary surface, one smallest complete fixture, and one explicit negative path minimize unrelated obligations.
- **counterargument_or_limit:** Some lessons concern coordination and cannot be reduced to a single surface.
- **assumptions_and_boundaries:** A composition example may remain unified when interaction is the named outcome and each surface has a specialized evidence owner.
- **revision_decision:** Default to a minimal workload envelope, then activate complexity dimensions deliberately.
- **additional_insight_to_add:** Supporting files are justified by reduced reasoning load or reusable verification, not by directory symmetry.
### Question 03: When does the default work well?
- **current_section_observation:** A narrow example works when inputs are deterministic, effects are local, compatibility is small, and the learner can inspect the complete contract in one session.
- **supporting_reason:** Under those conditions, authoring, review, clean copying, and failure diagnosis share the same bounded evidence set.
- **counterargument_or_limit:** A one-session review target varies with audience expertise and host tooling.
- **assumptions_and_boundaries:** Measure local completion and first-blocking assumptions rather than asserting a universal duration.
- **revision_decision:** Describe the low-complexity profile and its evidence needs without fixed time or file limits.
- **additional_insight_to_add:** A demonstration can be textually long yet operationally narrow when every paragraph supports one decision and its disconfirming cases.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The bounded seed fails to account for remote services, credentials, asynchronous hooks, shared settings, platform matrices, upgrades, and copied descendants.
- **supporting_reason:** These dimensions introduce state and ownership that cannot be made safe by keeping the source tree small.
- **counterargument_or_limit:** Splitting too early can hide interactions that learners must understand.
- **assumptions_and_boundaries:** Preserve a thin composition scenario while moving specialized mechanics and tests to owned references.
- **revision_decision:** Define split and escalation triggers based on coupled failure and lifecycle boundaries.
- **additional_insight_to_add:** When two parts cannot fail, recover, or version independently, splitting files alone does not reduce workload.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The seed offers only split or narrower reference as responses to exceeded capacity.
- **supporting_reason:** Other choices include static versus runnable, mock versus live, one example versus a graded set, local versus packaged, and monolithic versus composed teaching.
- **counterargument_or_limit:** Multiple variants increase maintenance and can confuse the recommended path.
- **assumptions_and_boundaries:** Keep one default variant and add alternatives only when they expose a decision-changing boundary.
- **revision_decision:** Add workload tradeoffs with activation costs and verification obligations.
- **additional_insight_to_add:** A variant earns its place when it teaches a new constraint, not merely a different syntax.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Visible file count omits prompt length, tool definitions, generated output, fixture data, environment setup, cleanup, retries, review state, and support burden.
- **supporting_reason:** Hidden workload migrates into the learner's context, machine state, or future maintainer queue.
- **counterargument_or_limit:** Exhaustively inventorying every cost can outweigh a tiny internal example.
- **assumptions_and_boundaries:** Track dimensions that can change safety, reproducibility, comprehension, or ownership.
- **revision_decision:** Add hidden-state, context, environment, privilege, nondeterminism, and descendant pressure checks.
- **additional_insight_to_add:** Complexity removed from the source but required in undocumented setup has been displaced rather than eliminated.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** The seed has no workload profiles that connect dimensions to authoring choices.
- **supporting_reason:** A one-skill fixture is low interaction; a command, hook, MCP, and settings package is high interaction; a command plus validation hook is borderline when coordination is the lesson.
- **counterargument_or_limit:** A large source corpus can support a small final demonstration through careful evidence extraction.
- **assumptions_and_boundaries:** Distinguish research workload from learner-facing artifact workload.
- **revision_decision:** Add representative profiles with keep, split, mock, escalate, and route decisions.
- **additional_insight_to_add:** Review both the authoring path and the copied path because a cheap author workflow can impose expensive learner setup.
### Question 08: How can the important claims be verified?
- **current_section_observation:** The artifact pressure row requires a worked example but does not test whether the workload is reproducible or bounded.
- **supporting_reason:** Inventorying surfaces and effects, tracing a clean learner journey, repeating fixtures, and recording first failures can expose hidden load.
- **counterargument_or_limit:** Small rehearsals cannot predict all production environments or support demand.
- **assumptions_and_boundaries:** Use local observations for local split decisions and label extrapolation.
- **revision_decision:** Add workload audit, clean-copy rehearsal, interaction matrix, and measured baseline procedure.
- **additional_insight_to_add:** A deliberate environment reset is a workload test because it removes the caches and implicit state that make examples appear simpler.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** Minimal focus and explicit structure are supported locally, while exact capacity thresholds and learner effort distributions are not.
- **supporting_reason:** Complexity dimensions are stable reasoning aids, but acceptable envelopes depend on audience, host, risk, and maintenance budget.
- **counterargument_or_limit:** Without a numeric limit, teams can postpone splitting indefinitely.
- **assumptions_and_boundaries:** Require observable split signals and an accountable reviewer rather than invented constants.
- **revision_decision:** Replace inherited capacities with locally calibrated thresholds and confidence notes.
- **additional_insight_to_add:** A threshold becomes defensible when crossing it repeatedly predicts a named failure or review cost in that environment.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The seed bounds an authoring run but not the multiplied workload of copied templates, host upgrades, security review, and support.
- **supporting_reason:** A small design decision can propagate across every descendant and compatibility combination.
- **counterargument_or_limit:** Unknown private copies make total downstream cost impossible to calculate.
- **assumptions_and_boundaries:** Track maintained copies and use migration signals to bound unknown consumers.
- **revision_decision:** Include propagation, support, and retirement cost in workload decisions before promotion.
- **additional_insight_to_add:** The appropriate optimization target is total lesson lifecycle cost, not minimum initial author effort.

## Section 019: Reliability Target
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed combines evidence-boundary policy, sampled routing accuracy, unsupported-claim rejection, and recovery completeness into one target table.
- **supporting_reason:** Maintainers need to decide the highest status that can be claimed and whether the demonstration may be promoted, retained, demoted, or retired.
- **counterargument_or_limit:** A broad reliability score is easier to communicate than several claim-specific gates.
- **assumptions_and_boundaries:** Avoid aggregation that allows strong formatting results to mask unsafe runtime or lifecycle behavior.
- **revision_decision:** Define reliability as status fidelity, reproducibility, noninterference, safe failure, and lifecycle closure at the claimed level.
- **additional_insight_to_add:** The reliability target should constrain what the artifact promises before it measures how often users invoke it.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** Fixed percentages and an eighteen-of-twenty sample appear without baseline, sampling method, risk model, or consequence analysis.
- **supporting_reason:** Invariant gates can require every applicable claim to have evidence, while empirical rates need local populations and decision thresholds.
- **counterargument_or_limit:** Refusing all numeric objectives can leave regressions without an operational trigger.
- **assumptions_and_boundaries:** Establish target-specific baselines and thresholds after the collection mechanism and denominator are verified.
- **revision_decision:** Separate binary release gates from calibrated operational objectives and exploratory indicators.
- **additional_insight_to_add:** A locally justified threshold is stronger than a precise inherited number because its failure action is known.
### Question 03: When does the default work well?
- **current_section_observation:** The seed's evidence and recovery ideas work well for a bounded example with deterministic fixtures and explicit source roles.
- **supporting_reason:** Stable inputs and a small surface allow every claimed path and credible failure to be observed directly.
- **counterargument_or_limit:** Natural-language activation and live integrations have open-ended input and environment distributions.
- **assumptions_and_boundaries:** Combine deterministic regression cases with sampled target observations and state confidence limits.
- **revision_decision:** Define low-variance and distributional reliability profiles separately.
- **additional_insight_to_add:** The evidence strategy should broaden as uncertainty moves from syntax to selection, environment, and copied use.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** A target can pass all sampled routes while missing a rare high-impact permission leak, destructive side effect, or uninstall residue.
- **supporting_reason:** Average or sampled success can hide categorical safety failures and correlated test cases.
- **counterargument_or_limit:** Exhaustive testing is impossible for open-ended host requests and environments.
- **assumptions_and_boundaries:** Make severe bounded invariants explicit and use risk-based sampling for the remaining distribution.
- **revision_decision:** Add hard gates, counter-metrics, mutation cases, and uncertainty reporting.
- **additional_insight_to_add:** Reliability claims should name which failures are intolerable and which are monitored, rather than implying uniform coverage.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The table does not compare release gates, property assertions, case suites, rolling rates, percentile distributions, compatibility matrices, and reviewer judgment.
- **supporting_reason:** These methods differ in falsifiability, realism, cost, variance, and suitability for structural versus behavioral claims.
- **counterargument_or_limit:** A complex portfolio can create reporting overhead disproportionate to a small lesson.
- **assumptions_and_boundaries:** Select the least costly method capable of detecting the named harm.
- **revision_decision:** Map reliability dimensions to evidence methods and escalation conditions.
- **additional_insight_to_add:** Use two independent methods only where their blind spots differ materially, such as host fixtures and clean-copy rehearsal.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** The seed omits denominator drift, unrepresentative samples, stale versions, hidden cache, flaky fixtures, silent telemetry loss, reviewer disagreement, and severity weighting.
- **supporting_reason:** Any of these can turn a green target into misleading evidence.
- **counterargument_or_limit:** Manual classification may be the only feasible method for sparse teaching feedback.
- **assumptions_and_boundaries:** Record classification rules, environment, and uncertainty even when automation is unavailable.
- **revision_decision:** Add evidence-health gates and invalidate conclusions when collection itself fails.
- **additional_insight_to_add:** Unknown measurement state is a reliability failure of the evaluation path, not evidence of successful quiet operation.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** No target profile illustrates how a demonstration earns a status without overclaiming.
- **supporting_reason:** A good source-valid example claims static closure only, a bad example calls successful parsing production-ready, and a borderline live example needs a declared compatibility sample.
- **counterargument_or_limit:** A small sample can still catch obvious regression even when it cannot justify a general rate.
- **assumptions_and_boundaries:** Report the exact sample outcome and avoid extrapolation beyond its population.
- **revision_decision:** Add status-aligned target examples and unacceptable inference examples.
- **additional_insight_to_add:** Reliability language should make the strongest unsupported inference easy for a reviewer to spot.
### Question 08: How can the important claims be verified?
- **current_section_observation:** Reviewer inspection alone cannot prove runtime repeatability, noninterference, permission denial, clean copying, or lifecycle symmetry.
- **supporting_reason:** Claim matrices, deterministic fixtures, negative activation cases, resource inventories, clean hosts, mutation tests, and removal comparisons cover distinct boundaries.
- **counterargument_or_limit:** Target commands and representative populations remain project-specific.
- **assumptions_and_boundaries:** Specify semantic observations here and bind them to authoritative adapters locally.
- **revision_decision:** Add a reliability evidence ladder and release-record schema.
- **additional_insight_to_add:** Reproduce at least one expected failure intentionally so recovery evidence is not inferred from success paths.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** Evidence visibility, claim traceability, explicit recovery, and no unsupported production claims are defensible policies; universal routing rates are not established.
- **supporting_reason:** Structural invariants derive from the reference contract, whereas behavioral frequency depends on target use.
- **counterargument_or_limit:** Even policy gates require judgment about what counts as an important claim or credible failure.
- **assumptions_and_boundaries:** Record reviewer rationale and disagreements for consequential classifications.
- **revision_decision:** State invariant confidence, local observations, and residual uncertainty separately.
- **additional_insight_to_add:** Reliability improves when uncertainty narrows the claim instead of being hidden behind a composite score.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The seed targets final guidance but not copied descendants, compatibility decay, or the reliability of its own verifier.
- **supporting_reason:** Promotion transforms local claims into dependencies whose evidence can expire and whose defects propagate.
- **counterargument_or_limit:** Maintainers cannot observe every downstream copy or host variation.
- **assumptions_and_boundaries:** Own known distributions and publish versioned demotion or migration signals for unknown consumers.
- **revision_decision:** Add evidence expiry, verifier mutation, descendant response, and retirement targets.
- **additional_insight_to_add:** Reducing the public claim surface is often the cheapest reliability improvement because it removes unsupported obligations at their source.

## Section 020: Failure Mode Table
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed lists source drift, generic advice, context loss, and tool fanout but does not connect them to demonstration status or learner harm.
- **supporting_reason:** Authors need to decide which failures block publication, require containment, permit a lower status, or justify retirement.
- **counterargument_or_limit:** A comprehensive registry can become harder to use than the example itself.
- **assumptions_and_boundaries:** Include failures that challenge a claimed boundary or credible copied use, and route unrelated mechanics elsewhere.
- **revision_decision:** Build a causal table from trigger through signal, consequence, containment, recovery, and prevention.
- **additional_insight_to_add:** Failure priority should follow irreversible or propagated harm, not how frequently the scenario is easy to imagine.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** Required mitigations in the current table combine prevention and recovery without naming the artifact state after failure.
- **supporting_reason:** Immediate containment limits harm, recovery restores a known state, and prevention protects the lesson from recurrence.
- **counterargument_or_limit:** Some conceptual failures have no runtime state to contain.
- **assumptions_and_boundaries:** For conceptual artifacts, containment means narrowing or demoting claims before reuse.
- **revision_decision:** Give each failure a status boundary, observable signal, safe end state, and regression gate.
- **additional_insight_to_add:** A failure response is complete only when the learner can tell whether retry, repair, route, rollback, or abandonment is safe.
### Question 03: When does the default work well?
- **current_section_observation:** Causal failure rows work for bounded surfaces with known triggers and observable outcomes.
- **supporting_reason:** They support pre-mortem review, fixture design, diagnostic text, and release decisions from the same contract.
- **counterargument_or_limit:** Emergent multi-surface and external failures may have several interacting causes.
- **assumptions_and_boundaries:** Add a state-transition or interaction analysis when one row cannot represent partial state accurately.
- **revision_decision:** Use concise rows for independent faults and escalation notes for coupled failure.
- **additional_insight_to_add:** A registry becomes more valuable when each new incident changes an example, a gate, and a migration decision.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** A static catalog can imply coverage while omitting novel requests, platform variation, supply-chain behavior, and unknown descendants.
- **supporting_reason:** Enumeration cannot prove absence of failure, especially for live integrations and open-ended activation.
- **counterargument_or_limit:** Refusing enumeration would discard useful known-harm prevention.
- **assumptions_and_boundaries:** Present the table as a minimum challenge set, not an exhaustive guarantee.
- **revision_decision:** Add residual-uncertainty and escalation boundaries around the registry.
- **additional_insight_to_add:** Unknown failure classes require containment defaults such as no fabricated success, no undeclared mutation, and status demotion.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The seed does not distinguish a failure table, state machine, fault tree, mutation suite, chaos exercise, and support-incident review.
- **supporting_reason:** Each representation fits different levels of coupling, runtime realism, cost, and diagnostic depth.
- **counterargument_or_limit:** Multiple analyses can duplicate the same risks with inconsistent names.
- **assumptions_and_boundaries:** Keep stable failure identities and link deeper artifacts only where the simple row loses state or ordering.
- **revision_decision:** Recommend the table by default, state transitions for partial effects, and controlled fault injection for runtime claims.
- **additional_insight_to_add:** Representation choice should be driven by the recovery state that must be proved, not by process preference.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Demonstrations can fail through source inflation, stale schema, wrong surface, trigger overlap, hidden state, nondeterminism, secrets, excess privilege, external dependency, package omission, residue, or blind verification.
- **supporting_reason:** These failures convert examples into misleading or unsafe copied templates.
- **counterargument_or_limit:** Not every surface activates every operational risk.
- **assumptions_and_boundaries:** Mark applicability by capability matrix and highest claimed status.
- **revision_decision:** Cover structural, selection, behavior, security, integration, lifecycle, evidence, and propagation categories.
- **additional_insight_to_add:** The earliest detectable signal should be preferred because it contains the defect before learners depend on it.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** Existing rows are plausible but do not show status-aligned response quality.
- **supporting_reason:** A good row demotes an unrefreshable schema claim, a bad row blindly retries a permission failure, and a borderline row isolates a flaky live check from the deterministic lesson.
- **counterargument_or_limit:** Retry can be correct for a transient remote failure when idempotency and budget are known.
- **assumptions_and_boundaries:** Require failure classification before retry guidance.
- **revision_decision:** Add representative response contrasts and explicit non-retry cases.
- **additional_insight_to_add:** The demonstration teaches failure handling through what it refuses to automate as much as through its recovery script.
### Question 08: How can the important claims be verified?
- **current_section_observation:** The seed proposes review actions but no deliberate trigger that proves detection and mitigation work.
- **supporting_reason:** Mutating metadata, removing files, broadening triggers, denying permissions, interrupting lifecycle, and corrupting observations can exercise the registry.
- **counterargument_or_limit:** Destructive failure drills are inappropriate outside disposable environments.
- **assumptions_and_boundaries:** Use synthetic fixtures and isolated hosts with bounded resources and known cleanup.
- **revision_decision:** Add fault-injection, expected-signal, recovery-state, and regression-evidence columns.
- **additional_insight_to_add:** A failure test should assert both the error and absence of forbidden residual effects.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** Local evidence supports structural focus and source boundaries, while actual host failure semantics, package behavior, and external-service responses remain target-dependent.
- **supporting_reason:** The registry can define questions and safe defaults without pretending to know uninspected mechanics.
- **counterargument_or_limit:** Generic safe defaults can still conflict with a host's transactional or retry contract.
- **assumptions_and_boundaries:** Adapt operational responses against current target authority and focused experiments.
- **revision_decision:** Label stable demonstration failures separately from conditional host failures.
- **additional_insight_to_add:** Uncertainty should lower status or trigger isolation, not be converted into confident recovery prose.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The seed focuses on the current authoring session and not on how copied examples preserve failure semantics over time.
- **supporting_reason:** Learners often copy retry, error, and cleanup behavior as implicit policy.
- **counterargument_or_limit:** Maintaining compatibility with every copied mistake can block necessary correction.
- **assumptions_and_boundaries:** Correct unsafe behavior and provide migration guidance rather than preserving it silently.
- **revision_decision:** Add propagation detection, descendant repair, verifier evolution, and retirement responses.
- **additional_insight_to_add:** A demonstration's failure contract is part of its public API once others use it as a template.

## Section 021: Retry Backpressure Guidance
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed classifies failed verification broadly and recommends bounded retry and work stoppage without distinguishing authoring, runtime, or lifecycle state.
- **supporting_reason:** Maintainers and copiers need to decide whether to retry, repair, roll back, route, wait, demote, or abandon after a specific failure.
- **counterargument_or_limit:** A detailed retry taxonomy may exceed the needs of a static source-valid lesson.
- **assumptions_and_boundaries:** Activate runtime and lifecycle guidance only when those behaviors are claimed.
- **revision_decision:** Separate retry domains and require classification, idempotency, budget, cancellation, state, and evidence before repetition.
- **additional_insight_to_add:** Retry is a state transition with duplicated-effect risk, not a generic response to uncertainty.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** One bounded retry for stale external evidence is stated as a rule without source cost, change rate, or authoritative availability context.
- **supporting_reason:** The safe default is no automatic retry until the failure is transient, the operation is repeatable, and a total budget is owned.
- **counterargument_or_limit:** Manual classification adds latency for common harmless transport failures.
- **assumptions_and_boundaries:** A target may automate known transient classes after proving idempotency, cancellation, observability, and bounded impact.
- **revision_decision:** Define retry eligibility first and leave counts and delays target-calibrated.
- **additional_insight_to_add:** A retry budget should cover the complete user operation, not reset independently at every nested layer.
### Question 03: When does the default work well?
- **current_section_observation:** Bounded retry works when the failed action has no effect or an idempotency mechanism makes repeated effect equivalent.
- **supporting_reason:** Transient read, authoritative refresh, and isolated verifier startup failures can then recover without changing the lesson contract.
- **counterargument_or_limit:** Even reads can consume quota, expose data, or return inconsistent versions.
- **assumptions_and_boundaries:** Include cost, privacy, freshness, and dependency load in eligibility.
- **revision_decision:** Provide eligible classes with required safeguards and stop conditions.
- **additional_insight_to_add:** The same error label can be retryable in a local mock and non-retryable against a metered or mutating remote service.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** Syntax defects, contract contradictions, denied permissions, missing files, unsafe partial state, and deterministic assertion failures do not improve through repetition.
- **supporting_reason:** Retrying these classes wastes budget, amplifies load, and can duplicate effects while hiding the root cause.
- **counterargument_or_limit:** A concurrent external change can make a prior contradiction disappear.
- **assumptions_and_boundaries:** Treat that as a new versioned observation after refresh, not as blind retry success.
- **revision_decision:** Add explicit never-retry classes and repair or escalation routes.
- **additional_insight_to_add:** Repeated success after an unexplained deterministic failure is evidence of hidden state or a flaky gate, not restored reliability.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The seed offers retry or escalation but omits cache, fallback, queueing, degradation, circuit breaking, manual approval, and source narrowing.
- **supporting_reason:** These choices trade latency, freshness, dependency pressure, semantic fidelity, operational complexity, and human attention.
- **counterargument_or_limit:** Production resilience mechanisms can distract from the demonstration's primary lesson.
- **assumptions_and_boundaries:** Keep the example's policy minimal and route full operational mechanics to the owning integration reference.
- **revision_decision:** Add a choice table centered on preserved outcome and safe state.
- **additional_insight_to_add:** A fallback is acceptable only when its result is distinguishable and still satisfies the stated teaching contract.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Nested retries, synchronized retries, unbounded queues, ignored cancellation, stale cache, duplicate mutation, swallowed cause, and retry-after-removal can all worsen a small failure.
- **supporting_reason:** Copied examples often turn simple retry snippets into system-wide policy accidentally.
- **counterargument_or_limit:** The local skill corpus supplies no runtime retry mechanics to validate.
- **assumptions_and_boundaries:** Present operational patterns as conditional requirements pending target authority and tests.
- **revision_decision:** Add anti-amplification and cleanup guards without invented timing constants.
- **additional_insight_to_add:** Backpressure must propagate toward request admission; slowing a worker alone still permits an unbounded backlog.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** No examples show when retry preserves or violates demonstration semantics.
- **supporting_reason:** A transient read with bounded budget and no effect is good, repeated permission denial is bad, and a remote mutation with idempotency is conditional.
- **counterargument_or_limit:** An idempotency key can be implemented incorrectly or expire before delayed retry.
- **assumptions_and_boundaries:** Verify deduplication across the entire supported retry window and failure sequence.
- **revision_decision:** Add retry, no-retry, and conditional cases with observable attempt and state outcomes.
- **additional_insight_to_add:** The example should reveal degraded or cached results rather than making them indistinguishable from fresh success.
### Question 08: How can the important claims be verified?
- **current_section_observation:** The seed does not assert attempt counts, total deadline, queue bounds, cancellation, duplicate effects, or final cleanup.
- **supporting_reason:** Injected transient and permanent failures can verify classification, backoff adapter, stop reason, effect count, and safe end state.
- **counterargument_or_limit:** Exact timing tests are flaky and target-specific.
- **assumptions_and_boundaries:** Test clock-controlled policy and semantic bounds rather than wall-clock precision where possible.
- **revision_decision:** Add a retry evidence matrix and mutation tests for budget bypass.
- **additional_insight_to_add:** Force failure at each effect boundary to prove retry resumes safely rather than replaying completed work.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** Classification, bounded work, exclusive ownership, checkpoints, and no retry for deterministic defects are stable; host retry signals and delays are unknown.
- **supporting_reason:** Operational policy depends on protocol semantics, quotas, idempotency, user latency, and dependency capacity.
- **counterargument_or_limit:** Excess conditional language can leave learners without a useful default.
- **assumptions_and_boundaries:** Default to stop and explicit failure when required safety facts are unavailable.
- **revision_decision:** Separate invariant eligibility questions from target-calibrated policy values.
- **additional_insight_to_add:** Unknown retry safety should reduce automation, not increase attempts in hope of success.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The seed applies backpressure to current generation but not to copied descendants, shared dependencies, or promotion queues.
- **supporting_reason:** A widely copied retry policy can synchronize load and magnify an upstream incident.
- **counterargument_or_limit:** The demonstration may never operate at scale.
- **assumptions_and_boundaries:** Promotion should still assess propagation risk because templates change future defaults.
- **revision_decision:** Add shared-budget, descendant migration, and demotion behavior to retry guidance.
- **additional_insight_to_add:** The safest demonstration often teaches how to stop, preserve state, and ask for a new decision rather than how to keep trying.

## Section 022: Observability Checklist
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed collects sources, proof, percentile latency, tool calls, context, delegation, retries, and audit outcome without tying each signal to a status or response.
- **supporting_reason:** Maintainers need enough evidence to explain selection, behavior, failure, side effects, lifecycle, and verifier health without retaining an internal transcript.
- **counterargument_or_limit:** Rich observability can outweigh the value of a small demonstration.
- **assumptions_and_boundaries:** Retain only signals that support a named verification, diagnosis, safety, compatibility, or retirement decision.
- **revision_decision:** Define minimum authoring, host-behavior, lifecycle, and evidence-health records by claimed status.
- **additional_insight_to_add:** An observable example makes consequential state transitions inspectable while keeping reasoning notes and user content appropriately bounded.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** Current guidance prefers summaries over transcript dumps but supplies no event identity, schema, privacy classification, or correlation rule.
- **supporting_reason:** A compact structured record enables comparison and diagnosis without making free-form logs the source of truth.
- **counterargument_or_limit:** Exact telemetry format depends on the host and may not exist for a conceptual artifact.
- **assumptions_and_boundaries:** Use a journal and claim-evidence record for static work, then adapt semantic fields to target-native telemetry for runtime claims.
- **revision_decision:** Default to artifact identity, evidence status, operation identity, intent class, decision, result class, effects, and recovery.
- **additional_insight_to_add:** The observation schema should distinguish not observed, not applicable, and observed success.
### Question 03: When does the default work well?
- **current_section_observation:** Small structured evidence works when one lesson, one operation identity, and a bounded set of states explain the outcome.
- **supporting_reason:** Reviewers can trace a claim from source through gate to final state without replaying every authoring action.
- **counterargument_or_limit:** Distributed or asynchronous integrations may require traces across several components and delayed events.
- **assumptions_and_boundaries:** Add correlation and causal fields only when the demonstration claims those interactions.
- **revision_decision:** Define a minimal record with conditional extensions for retry, external dependency, and lifecycle.
- **additional_insight_to_add:** Observability should expand at the same boundary as side effects and ownership, not at the same pace as prose length.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** Raw prompt capture, command output dumps, and high-cardinality tool details can expose secrets while obscuring the decisive signal.
- **supporting_reason:** Excess data increases privacy, storage, review, and interpretation risk without proving correctness.
- **counterargument_or_limit:** Fine-grained traces can be necessary for a difficult incident.
- **assumptions_and_boundaries:** Enable deeper diagnostics deliberately, minimize retention, and separate incident evidence from routine demonstration telemetry.
- **revision_decision:** Add minimization, classification, retention, access, and escalation controls.
- **additional_insight_to_add:** The ability to collect a field does not establish a legitimate purpose for retaining it.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The seed does not compare structured logs, metrics, traces, snapshots, journals, test reports, and reviewer notes.
- **supporting_reason:** These forms trade detail, aggregation, causality, privacy, portability, and target coupling.
- **counterargument_or_limit:** Multiple signal types can create fragmented evidence and inconsistent identifiers.
- **assumptions_and_boundaries:** Use one operation and artifact identity across all activated forms.
- **revision_decision:** Map evidence form to structural, behavioral, performance, lifecycle, and qualitative decisions.
- **additional_insight_to_add:** A snapshot is often stronger than a log for cleanup because it proves final resource state directly.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Success-only logging, missing denominator, stale version, broken collector, clock skew, sampling loss, secret leakage, unbounded cardinality, and missing correlation can invalidate conclusions.
- **supporting_reason:** These failures either conceal harm or make unrelated events appear causal.
- **counterargument_or_limit:** A static internal example may need only a verifier summary and changed-path record.
- **assumptions_and_boundaries:** Scale the checklist to the status while retaining evidence-health controls.
- **revision_decision:** Add expected-failure, missing-signal, redaction, correlation, and version checks.
- **additional_insight_to_add:** Collector failure must produce unknown evidence status rather than a default success classification.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** The seed gives no concrete record showing a useful signal and its privacy boundary.
- **supporting_reason:** A good record classifies an adjacent request without storing its private text, a bad record logs credentials, and a borderline trace requires incident-only retention.
- **counterargument_or_limit:** Intent classification can remove linguistic detail needed to diagnose trigger overlap.
- **assumptions_and_boundaries:** Preserve a sanitized representative fixture separately when exact wording is necessary and authorized.
- **revision_decision:** Add record examples for authoring, activation, failure, retry, and lifecycle.
- **additional_insight_to_add:** Routine telemetry and curated regression fixtures should have different retention and review contracts.
### Question 08: How can the important claims be verified?
- **current_section_observation:** The current checklist does not test whether signals appear on failure, remain correlated, redact sensitive values, or survive collector loss.
- **supporting_reason:** Known-success, known-failure, missing-collector, retry, cancellation, and cleanup cases can validate the observation path.
- **counterargument_or_limit:** Target-native telemetry APIs are outside the frozen local evidence.
- **assumptions_and_boundaries:** Assert semantic fields and outcomes, then bind them to current host adapters.
- **revision_decision:** Add observability contract tests and evidence-health mutations.
- **additional_insight_to_add:** Compare observed effects with a resource snapshot so logs cannot claim cleanup that state contradicts.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** Small auditable summaries, changed paths, verification evidence, and unresolved risk notes are defensible; universal percentile or tool-count targets are not.
- **supporting_reason:** Performance and workflow distributions depend on host, audience, task, and instrumentation overhead.
- **counterargument_or_limit:** Without measured distributions, slow regressions can remain anecdotal.
- **assumptions_and_boundaries:** Measure locally after defining the decision, environment, population, and collection cost.
- **revision_decision:** Keep required identity and status fields invariant while calibrating performance fields locally.
- **additional_insight_to_add:** Precision should follow a stable measurement contract rather than precede it.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** Demonstration observability is likely to be copied into templates, making its privacy and cardinality choices future defaults.
- **supporting_reason:** An educational log field can propagate to production systems and durable support workflows.
- **counterargument_or_limit:** A demonstration should remain simple enough to teach its primary capability.
- **assumptions_and_boundaries:** Include the minimum safe pattern and route advanced telemetry to the owning operational reference.
- **revision_decision:** Treat observation schema, retention, and redaction as part of template promotion review.
- **additional_insight_to_add:** The best copied default records decisions and effects, not private content or hidden-thought narration.

## Section 023: Performance Verification Method
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed mixes tool budgets, workflow resumability, usability, runtime percentiles, reviewer time, and readiness order in one performance method.
- **supporting_reason:** Maintainers need to decide whether performance matters to the lesson, which workload and resource express it, and whether observed change justifies redesign or scope reduction.
- **counterargument_or_limit:** Many static examples need correctness and copyability evidence but no performance claim.
- **assumptions_and_boundaries:** Record performance as not claimed when it does not change the teaching decision.
- **revision_decision:** Separate authoring, learner workflow, host selection, invocation, external dependency, and lifecycle performance.
- **additional_insight_to_add:** Performance verification begins by refusing to measure convenient proxies that have no causal connection to the learner outcome.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** Input size, source count, tool calls, wall time, percentiles, and reviewer time are required without workload definitions or baseline controls.
- **supporting_reason:** A reproducible workload, declared environment, current baseline, resource measure, and decision threshold make a performance result interpretable.
- **counterargument_or_limit:** Building a benchmark can cost more than the narrow example benefits.
- **assumptions_and_boundaries:** Use the smallest repeatable measurement capable of disproving the important performance claim.
- **revision_decision:** Default to no universal target, then add locally calibrated budgets only for claimed constraints.
- **additional_insight_to_add:** A budget should include setup, retry, cleanup, and failure work when users experience those costs.
### Question 03: When does the default work well?
- **current_section_observation:** Controlled comparison works when the operation, input distribution, environment, cache state, and success condition are stable.
- **supporting_reason:** Repeated baseline and candidate runs can then separate meaningful change from noise and correctness regressions.
- **counterargument_or_limit:** Natural-language selection and remote services remain variable even under careful control.
- **assumptions_and_boundaries:** Stratify inputs and dependency states rather than combining unlike observations.
- **revision_decision:** Add low-variance benchmark and distributional observation paths.
- **additional_insight_to_add:** Performance evidence is strongest when the same fixture also asserts semantic output and side effects.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** Percentiles over tiny mixed samples, cold and warm runs combined, hidden cache, and success-only timing can produce precise but misleading results.
- **supporting_reason:** Measurement bias can reward failures, omit queueing, or shift work outside the timed interval.
- **counterargument_or_limit:** A rough measurement can still reveal an order-of-magnitude regression.
- **assumptions_and_boundaries:** Label exploratory observations and repeat under a controlled method before promotion claims.
- **revision_decision:** Add invalidation conditions, correctness guards, and end-to-end boundaries.
- **additional_insight_to_add:** Faster failure is not improved task performance when the user still lacks the promised outcome or recovery.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The seed does not compare benchmark, profile, trace, resource inventory, clean-copy timing, reviewer study, and production observation.
- **supporting_reason:** Each answers a different question about speed, bottleneck, resource, causality, comprehension, or real workload.
- **counterargument_or_limit:** Combining methods adds instrumentation and analysis overhead.
- **assumptions_and_boundaries:** Start with end-to-end outcome measurement and add diagnostics only when a decision requires them.
- **revision_decision:** Map method choice to question and blind spot.
- **additional_insight_to_add:** Profiling explains where time goes but does not by itself establish that the user-facing workload improved.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** The current packet omits warmup, clock choice, instrumentation overhead, outliers, coordinated omission, concurrency, queue time, allocation, network cost, and environment drift.
- **supporting_reason:** These factors can dominate a small example or hide the system pressure introduced by retry and fanout.
- **counterargument_or_limit:** Not every demonstration needs production-grade benchmark statistics.
- **assumptions_and_boundaries:** Scale rigor to claim consequence and distribution scope.
- **revision_decision:** Add a skeptical measurement checklist without fixed sample counts.
- **additional_insight_to_add:** Measure rejected and degraded work when admission control is part of the performance contract.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** The seed supplies pass and fail prose but no measurement scenario with controlled inputs and correctness assertions.
- **supporting_reason:** A good clean-copy comparison includes full setup and verifies outcome, a bad microbenchmark times only a parser and claims installation speed, and a borderline live sample stays exploratory.
- **counterargument_or_limit:** Microbenchmarks are useful for isolating a known hot component.
- **assumptions_and_boundaries:** Keep component and end-to-end claims distinct.
- **revision_decision:** Add representative good, bad, and conditional performance cases.
- **additional_insight_to_add:** The measurement name should identify both operation boundary and workload class to prevent accidental extrapolation.
### Question 08: How can the important claims be verified?
- **current_section_observation:** No procedure currently freezes environment, checks output, compares baseline, reports variability, or archives the harness.
- **supporting_reason:** A versioned workload, repeated interleaved runs, correctness gate, resource capture, and regression decision provide reproducible evidence.
- **counterargument_or_limit:** Exact statistical methods depend on sample properties and team expertise.
- **assumptions_and_boundaries:** Report raw summary, method, uncertainty, and practical decision without overstating significance.
- **revision_decision:** Add a stepwise benchmark and workflow-study protocol.
- **additional_insight_to_add:** Deliberately slow or fail a dependency to verify that the measured boundary includes timeout, retry, and recovery behavior.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The reference can define method quality but has no target runtime, workload distribution, baseline measurements, or user-performance objective.
- **supporting_reason:** Numerical performance claims require implementation and environment evidence absent from the frozen corpus.
- **counterargument_or_limit:** The absence of a target should not excuse obviously unbounded work.
- **assumptions_and_boundaries:** Enforce bounded retry, queue, context, and artifact closure as safety properties while measuring local speed separately.
- **revision_decision:** Mark all numeric budgets project-owned and all current performance results unavailable.
- **additional_insight_to_add:** A bounded design can be safer without being demonstrably faster, and the reference should preserve that distinction.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** Demonstration benchmarks and shortcuts are likely to be copied into production templates and future evaluations.
- **supporting_reason:** An incomplete timing boundary can institutionalize hidden setup, omitted cleanup, and success-only measurement.
- **counterargument_or_limit:** Keeping a full benchmark harness can burden a simple educational repository.
- **assumptions_and_boundaries:** Preserve the smallest reproducible harness and route advanced load testing to the owning implementation reference.
- **revision_decision:** Add benchmark ownership, versioning, expiry, and promotion review.
- **additional_insight_to_add:** Performance guidance is durable when future maintainers can reproduce why a budget exists, not merely rerun a number.

## Section 024: Scale Boundary Statement
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed says the reference becomes insufficient across independent systems, ownership boundaries, unbounded discovery, production traffic, distributed work, long context, or large codebases.
- **supporting_reason:** Teams need to decide whether to stay with one demonstration, split lessons, route mechanics, create a maintained template, or invoke production architecture and operations guidance.
- **counterargument_or_limit:** A hard boundary can fragment a coherent integration lesson.
- **assumptions_and_boundaries:** Preserve a thin composition contract when interaction is the learner outcome and each subsystem remains independently owned.
- **revision_decision:** Define scale through teaching, interaction, evidence, runtime, environment, privilege, lifecycle, distribution, and coordination axes.
- **additional_insight_to_add:** Distribution scale can exceed runtime scale because one static example may seed many long-lived descendants.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** More than one ownership boundary is treated as automatically out of scope, even though specialized references can cooperate under one composition owner.
- **supporting_reason:** The safest default is one primary lesson and owner, controlled fixtures, bounded effects, declared environment, and no implicit production or distribution promise.
- **counterargument_or_limit:** Internal examples can still be copied beyond their intended audience.
- **assumptions_and_boundaries:** State reuse limits and apply promotion gates when independent copying becomes likely.
- **revision_decision:** Set a qualitative default envelope with observable exit signals instead of arbitrary file or task counts.
- **additional_insight_to_add:** Scope is bounded by responsibilities and consequences, not by repository size alone.
### Question 03: When does the default work well?
- **current_section_observation:** The current reference is sufficient when source roles are ranked, one learner journey is reproducible, and target-specific mechanics remain conditional or narrowly verified.
- **supporting_reason:** The example can then carry contract, evidence, failure, recovery, and copyability in one reviewable unit.
- **counterargument_or_limit:** A small example may still have high security or privacy consequence.
- **assumptions_and_boundaries:** Consequence can trigger escalation even when artifact size is small.
- **revision_decision:** Add both complexity and impact criteria to the sufficiency test.
- **additional_insight_to_add:** Low traffic does not reduce the need for safeguards when a capability can expose secrets or mutate shared state.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** Production traffic is named, but multi-tenancy, availability objectives, data governance, supply chain, regional behavior, and incident response are absent.
- **supporting_reason:** These concerns require operational architecture and ownership beyond an educational example.
- **counterargument_or_limit:** A demonstration can still provide a small reproducer inside a production program.
- **assumptions_and_boundaries:** Keep it as a diagnostic or teaching fixture, not the production authority.
- **revision_decision:** Add explicit escalation triggers and state which guidance this reference no longer supplies.
- **additional_insight_to_add:** A useful example can remain valid after crossing the boundary if its status is reduced to fixture rather than architecture.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The seed recommends splitting by theme and graph narrowing but not graded examples, composition harnesses, maintained templates, or production service references.
- **supporting_reason:** These forms trade coherence, duplication, operational realism, ownership, and learner accessibility.
- **counterargument_or_limit:** Promoting to a template or package creates durable support and compatibility work.
- **assumptions_and_boundaries:** Promote only when repeated independent reuse justifies lifecycle ownership.
- **revision_decision:** Add stay, split, compose, promote, and escalate choices with return gates.
- **additional_insight_to_add:** The right boundary response preserves the lesson while moving volatile mechanics to their real owner.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Hidden scale can appear through generated descendants, nested retries, shared queues, large tool schemas, many host versions, broad permissions, or one owner becoming a bottleneck.
- **supporting_reason:** Source size and request volume alone miss propagation, blast radius, and coordination pressure.
- **counterargument_or_limit:** Tracking every dimension can overburden a workshop artifact.
- **assumptions_and_boundaries:** Audit dimensions that can invalidate current status or ownership.
- **revision_decision:** Add hidden-scale indicators and a periodic boundary review for promoted examples.
- **additional_insight_to_add:** A boundary is already crossed when the team cannot confidently enumerate who must approve a change or who can be harmed by it.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** No scenarios distinguish a bounded lesson from an underspecified production pattern.
- **supporting_reason:** A local skill fixture is in scope, a multi-tenant remote execution platform is out of scope, and a command-plus-hook teaching harness is conditional.
- **counterargument_or_limit:** A remote example can remain bounded with a mock and explicit protocol contract.
- **assumptions_and_boundaries:** Separate deterministic teaching from live operational validation.
- **revision_decision:** Add representative scale profiles and the action at each crossing.
- **additional_insight_to_add:** Borderline cases become safer when the unbounded dimension is isolated behind a named adapter and owner.
### Question 08: How can the important claims be verified?
- **current_section_observation:** The seed gives no inventory or rehearsal proving that systems, owners, sources, traffic, and context are actually bounded.
- **supporting_reason:** Surface, interaction, data, effect, environment, distribution, and ownership inventories can reveal boundary crossings.
- **counterargument_or_limit:** Future traffic and unknown copies cannot be measured fully.
- **assumptions_and_boundaries:** Use declared support, known distributions, and explicit unknowns rather than false completeness.
- **revision_decision:** Add a scale review worksheet and threshold-trigger evidence.
- **additional_insight_to_add:** Re-run boundary review after any new surface, permission, external dependency, package claim, or audience expansion.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The reference clearly cannot replace production SLO, security, capacity, or incident design, but exact escalation thresholds depend on target risk and organization.
- **supporting_reason:** Responsibility categories are stable while acceptable scale and consequence are contextual.
- **counterargument_or_limit:** Purely qualitative thresholds can be interpreted inconsistently.
- **assumptions_and_boundaries:** Record local triggers, owner, evidence, and consequence in the release contract.
- **revision_decision:** State categorical out-of-scope domains and locally calibrated boundary values separately.
- **additional_insight_to_add:** Judgment becomes auditable when the condition and resulting ownership transfer are explicit.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The seed treats scale mainly as workload expansion, not as a transition in governance and support obligations.
- **supporting_reason:** Wider reuse changes compatibility, security response, migration, and retirement even if code and traffic stay small.
- **counterargument_or_limit:** Formal governance can discourage beneficial sharing.
- **assumptions_and_boundaries:** Use lightweight ownership for local artifacts and stronger controls only as consequence or distribution grows.
- **revision_decision:** Add governance transition and demotion paths to the boundary statement.
- **additional_insight_to_add:** Scale is the point where a lesson's externalities require a new operating contract, not merely more compute.

## Section 025: Future Refresh Search Queries
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed offers three generic searches for official practices, GitHub examples, and release notes without a selected host, surface, version, or unresolved claim.
- **supporting_reason:** A future maintainer needs to decide which changing public fact can alter metadata, discovery, behavior, security, compatibility, packaging, or lifecycle guidance.
- **counterargument_or_limit:** Broad discovery can reveal terminology and authorities not known in advance.
- **assumptions_and_boundaries:** Use broad search only to identify candidate owners, then narrow before accepting evidence.
- **revision_decision:** Organize refresh queries by frozen question, decision consequence, target identity, authority type, and reproduction gate.
- **additional_insight_to_add:** Search completeness is measured by resolved material decisions, not the number of collected links.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** Theme-only wording is likely to retrieve derivative advice that repeats the title rather than authoritative mechanics.
- **supporting_reason:** Target name, exact version, surface, field or operation, and document type increase relevance and expose version boundaries.
- **counterargument_or_limit:** Exact names can miss renamed or newly unified concepts.
- **assumptions_and_boundaries:** Add known aliases and inspect the target's official navigation and release index.
- **revision_decision:** Default to primary host documentation, published schema or help, release notes, migration guidance, security material, then maintained examples.
- **additional_insight_to_add:** Query both the current term and the previous supported term when migration is the decision.
### Question 03: When does the default work well?
- **current_section_observation:** Decision-specific refresh works when a validator failure, host upgrade, permission change, protocol revision, package defect, or copied-template conflict identifies the affected claim.
- **supporting_reason:** The search can stop after authority, applicability, and target behavior converge.
- **counterargument_or_limit:** New extension surfaces may require exploratory mapping before a claim exists.
- **assumptions_and_boundaries:** Record exploration separately and do not convert candidate concepts into recommendations prematurely.
- **revision_decision:** Add event triggers and stopping criteria to the query map.
- **additional_insight_to_add:** Refresh at change boundaries preserves currentness with less context than periodic indiscriminate research.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** Search results can surface stale versions, mirrors, generated summaries, snippets without context, popular repositories, and unrelated products sharing plugin terminology.
- **supporting_reason:** Relevance ranking and popularity do not establish authority, applicability, security, or support status.
- **counterargument_or_limit:** Community issues can reveal defects absent from polished official documentation.
- **assumptions_and_boundaries:** Use issues as problem evidence and confirm semantics against authoritative material and reproduction.
- **revision_decision:** Add rejection criteria and source-role labels to refresh handling.
- **additional_insight_to_add:** A current page can still be wrong for the selected host mode, transport, package channel, or threat model.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The seed groups all external evidence into docs, repositories, and release notes without distinguishing schema, CLI help, source, issues, security advisories, and package metadata.
- **supporting_reason:** These sources trade normative authority, executable precision, implementation realism, problem visibility, and version traceability.
- **counterargument_or_limit:** No single source may document an end-to-end lifecycle.
- **assumptions_and_boundaries:** Reconcile multiple source types by claim rather than averaging confidence.
- **revision_decision:** Add an authority ladder and claim-specific evidence combinations.
- **additional_insight_to_add:** Runtime reproduction resolves applicability but does not replace normative security or support boundaries.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Search personalization, regional mirrors, moving default branches, untagged examples, removed pages, conflicting dates, copied snippets, and protocol-host mismatch can contaminate refresh.
- **supporting_reason:** Without a recorded publisher, version, date, and bounded finding, later reviewers cannot reproduce why guidance changed.
- **counterargument_or_limit:** Some authoritative help is generated locally and has no stable public URL.
- **assumptions_and_boundaries:** Capture command version and bounded output as target-owned evidence where appropriate.
- **revision_decision:** Require provenance, version, content disposition, conflict notes, and target retest.
- **additional_insight_to_add:** Preserve rejected results and reasons when they are likely to recur, preventing future rediscovery from resetting confidence.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** The generic query rows do not show how a result changes or fails to change guidance.
- **supporting_reason:** A good query asks for current manifest schema and migration for a chosen host, a bad query seeks universal plugin best practices, and a GitHub example is borderline until version and threat model match.
- **counterargument_or_limit:** Broad best-practice searches can inspire review questions.
- **assumptions_and_boundaries:** Treat inspiration as contextual input, not implementation authority.
- **revision_decision:** Add query families with decisions, preferred authorities, and stop conditions.
- **additional_insight_to_add:** Every query should have an explicit no-material-impact outcome so research cannot force unnecessary edits.
### Question 08: How can the important claims be verified?
- **current_section_observation:** Finding a page or repository does not prove that a candidate schema loads, a trigger selects, a permission is sufficient, or removal cleans up.
- **supporting_reason:** The affected target behavior must be reproduced with a recorded artifact and environment after evidence reconciliation.
- **counterargument_or_limit:** Some lifecycle or production conditions require controlled environments unavailable during documentation refresh.
- **assumptions_and_boundaries:** Keep the claim conditional or demoted until the required environment exists.
- **revision_decision:** Pair each query family with a focused static, behavioral, security, compatibility, or lifecycle gate.
- **additional_insight_to_add:** Re-run a previously failing or deliberately mutated case to show that refreshed guidance changes the intended boundary.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** Three inherited external locations are known only as unrefreshed retrieval targets, and no current host authority was browsed in this evolution.
- **supporting_reason:** Future search plans can be precise while current facts remain explicitly unavailable.
- **counterargument_or_limit:** The target project's local validators may already embody current behavior.
- **assumptions_and_boundaries:** Treat local behavior as implementation evidence, not automatic proof of public support or future compatibility.
- **revision_decision:** State present evidence status before listing future queries.
- **additional_insight_to_add:** Separating query intent from query result prevents a research plan from being misread as sourced guidance.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The seed treats refresh as repeated search rather than a versioned change-detection and reconciliation workflow.
- **supporting_reason:** Useful refresh work records what changed, which claim moved, which test now differs, and which descendants need migration.
- **counterargument_or_limit:** Maintaining a full evidence ledger adds overhead for low-risk local examples.
- **assumptions_and_boundaries:** Scale the record to consequence while retaining source identity, decision, and retest.
- **revision_decision:** Add dispositions, stopping rules, diff focus, and descendant actions.
- **additional_insight_to_add:** A mature refresh process should shrink future search by preserving durable rejection and supersession knowledge.

## Section 026: Evidence Boundary Notes
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed offers three broad labels for local fact, external fact, and combined inference without distinguishing historical, duplicate, unrefreshed, observed, recommended, illustrative, or unknown material.
- **supporting_reason:** Readers need to decide which claims can be reused directly, which require target adaptation, and which remain hypotheses or teaching choices.
- **counterargument_or_limit:** Too many labels can interrupt readable guidance.
- **assumptions_and_boundaries:** Keep prose natural and apply explicit labels at consequential claims, evidence tables, and release records.
- **revision_decision:** Define a claim-level taxonomy with permitted use, prohibited inference, and upgrade gate.
- **additional_insight_to_add:** Evidence boundaries protect decisions only when they travel with the claim during copying and summarization.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** An external URL is currently eligible for the external-fact label even though none was browsed during this evolution.
- **supporting_reason:** Location, inspection, applicability, reproduction, and reconciliation are separate evidence states.
- **counterargument_or_limit:** Requiring every transition can add process to low-consequence context.
- **assumptions_and_boundaries:** Use the full transition record for changing implementation, security, compatibility, and lifecycle claims.
- **revision_decision:** Default to the weakest accurate role and upgrade only after recorded evidence.
- **additional_insight_to_add:** A plausible retrieval target should remain unrefreshed rather than borrowing factual status from its URL shape.
### Question 03: When does the default work well?
- **current_section_observation:** Explicit roles work when source spans, hashes, versions, target observations, and inference decisions are finite and reviewable.
- **supporting_reason:** Reviewers can trace disagreement and prevent lower-level evidence from inflating status.
- **counterargument_or_limit:** A long synthesis may contain many stable low-consequence recommendations that do not need inline provenance.
- **assumptions_and_boundaries:** Group claims under a scoped evidence note when they share exactly the same role and boundary.
- **revision_decision:** Use source maps for coverage and inline qualifiers for decision-changing uncertainty.
- **additional_insight_to_add:** Boundary granularity should follow the cost of a mistaken transitive inference.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** Broad labels can launder a historical example into current host guidance or make one duplicated file look like two independent confirmations.
- **supporting_reason:** Readers often remember the recommendation and lose the qualification during later summaries.
- **counterargument_or_limit:** Repetition of caveats can reduce readability and obscure the recommendation.
- **assumptions_and_boundaries:** Put durable qualification in the claim identity, status table, and migration record rather than repeating generic warnings.
- **revision_decision:** Add prohibited inference examples and copy-preserving language.
- **additional_insight_to_add:** If a qualifier disappears when a sentence is quoted alone, the claim may be scoped too weakly.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The seed does not compare inline citations, source maps, claim-evidence matrices, content hashes, executable tests, and versioned release records.
- **supporting_reason:** These mechanisms trade readability, retrieval cost, integrity, behavioral confidence, and maintenance.
- **counterargument_or_limit:** Hashes prove identity but not authority or semantic correctness.
- **assumptions_and_boundaries:** Combine integrity, authority, applicability, and reproduction evidence where the claim requires them.
- **revision_decision:** Map each evidence mechanism to the question it can and cannot answer.
- **additional_insight_to_add:** Strong evidence is multidimensional; more of one dimension cannot compensate for a missing one.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Evidence can decay through moved pages, branch drift, local edits, version mismatch, duplicate paths, selective spans, unsupported paraphrase, and target behavior outside public support.
- **supporting_reason:** Any of these can make a traceable claim materially wrong despite a valid-looking citation.
- **counterargument_or_limit:** Frozen historical evidence remains accurate about what the source once contained.
- **assumptions_and_boundaries:** Date and scope historical facts explicitly and never imply present support.
- **revision_decision:** Add identity, authority, currentness, applicability, reproduction, and inference checks.
- **additional_insight_to_add:** Observed behavior and supported behavior should remain separate because local success can depend on undocumented compatibility.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** No examples show correct evidence upgrades or invalid transitive conclusions.
- **supporting_reason:** A good claim says the identical historical skill files demonstrate optional structure, a bad claim calls them independent proof of current plugin schema, and a target load is borderline until support status is known.
- **counterargument_or_limit:** A local target observation can still be decisive for immediate debugging.
- **assumptions_and_boundaries:** Use it to describe the observed environment without generalizing compatibility.
- **revision_decision:** Add evidence-role examples with allowed and forbidden uses.
- **additional_insight_to_add:** Borderline evidence becomes useful when the exact environment and missing authority are named together.
### Question 08: How can the important claims be verified?
- **current_section_observation:** The seed labels do not require source existence, content identity, span integrity, exact question preservation, or target reproduction.
- **supporting_reason:** Hash checks, frozen source spans, claim mapping, focused tests, mutations, and skeptical reread can validate different evidence dimensions.
- **counterargument_or_limit:** Verification still depends on correct interpretation of source meaning.
- **assumptions_and_boundaries:** Preserve counterarguments and reviewer disagreement for high-consequence synthesis.
- **revision_decision:** Add a claim-evidence audit sequence and invalidation triggers.
- **additional_insight_to_add:** A verifier should reject a claim when its source changes silently, not merely report that the path still exists.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The archive and working local skill files are byte-identical historical evidence of one skill-format lesson, while current plugin and host mechanics remain unverified.
- **supporting_reason:** Hash and complete-read evidence establishes identity and content scope, not contemporary authority.
- **counterargument_or_limit:** The historical pattern can remain semantically useful despite age.
- **assumptions_and_boundaries:** Preserve durable focus and optional-structure insights as historical support, then adapt mechanics against the selected target.
- **revision_decision:** End with an exact known, inferred, illustrative, and unknown inventory.
- **additional_insight_to_add:** Honest uncertainty increases reuse because future maintainers know precisely which checks must be refreshed.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** Evidence boundaries are currently prose labels rather than a maintained dependency graph from claim to source, test, owner, and descendant.
- **supporting_reason:** Promotion and copying create relationships that need invalidation and migration when an authority or observation changes.
- **counterargument_or_limit:** A full graph is unnecessary for a private conceptual sketch.
- **assumptions_and_boundaries:** Increase traceability with distribution and consequence.
- **revision_decision:** Add invalidation propagation, evidence expiry, ownership, and descendant response to promoted artifacts.
- **additional_insight_to_add:** The durable unit of maintenance is not the document but the claim and every artifact that depends on it.
