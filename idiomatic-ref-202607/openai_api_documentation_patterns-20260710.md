# Openai Api Documentation Patterns

**Decision supported.** This section helps decide whether an OpenAI question should be answered from live docs, a bundled reference, or declared uncovered. The seed title names the theme without its governing rule, live official docs outrank every bundled reference, so guidance must be re-verified against current OpenAI docs before it is repeated.

**Recommended default and causal basis.** Search docs via the MCP tools first, load the matching reference file only for model-selection or GPT-5.4 upgrade requests, and cite the fetched doc source. The skill states that reference files are convenience guides only and that for volatile guidance such as recommended models or upgrade instructions, current OpenAI docs always win.

**Operating conditions and assumptions.** The question concerns building with OpenAI products or APIs and the answer must carry citations to current official documentation. This reference operationalizes the openai-docs skill's routing and upgrade doctrine and does not restate OpenAI's actual API documentation.

**Failure boundary and alternatives.** The doctrine presumes the developers.openai.com MCP server is installed and reachable, and its fallback path is restricted to official OpenAI domains. Bounded alternatives and recoveries: web search restricted to developers.openai.com and platform.openai.com when MCP returns nothing meaningful, or installing the MCP server via the documented codex command.

**Counterexample, gotchas, and operational comparison.** Answering from the bundled model map without re-verifying skips the exact step the skill makes mandatory, the map is curated helper text, not truth. Good: an answer citing a fetched doc section with the reference used only as routing. Bad: quoting the model map as current truth. Borderline: paraphrasing the upgrade checklist while the MCP server is down, delivered with a staleness warning.

**Verification, evidence, and uncertainty.** Confirm any answer produced under this reference names the live doc page it verified against or explicitly flags that verification was unavailable. The SKILL.md quality rules and tooling notes state the docs-win and MCP-first rules verbatim. How far the model names and upgrade guidance in the archive have drifted from live docs is unknowable without retrieval.

**Second-order consequence.** The skill designs for its own staleness, every reference file carries a self-deprecation clause telling the reader to verify against live docs, an unusual pattern where the corpus distrusts itself by construction.

**Revision decision.** Open with the docs-win rule, the MCP-first tool order, and the three request classes the workflow distinguishes, docs lookup, model selection, and GPT-5.4 upgrade.

**Retained seed evidence.** The exact theme title and its documentation-patterns framing remain unchanged. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

## Source Evidence Mapping Table

**Decision supported.** This section helps decide which recorded source may back which claim about OpenAI documentation patterns. The seed map's rows do not distinguish the corpus's two truth tiers, four read local files that are explicitly self-deprecating helper context, and the live-docs layer that outranks them but was never retrieved here.

**Recommended default and causal basis.** Cite the specific skill file for each claim and attach the docs-win caveat to any volatile fact such as a model ID or upgrade recommendation. Claims in this document quote the skill's routing rules and the upgrade doctrine, and each such claim inherits the archive's own caveat that current docs win.

**Operating conditions and assumptions.** The codex-skills-202603 archive paths stay valid and the four files keep their current structure. The table records provenance for this document's claims and does not certify any model name or upgrade step against live OpenAI docs.

**Failure boundary and alternatives.** The three generic external URLs, AGENTS.md guides and GitHub Actions docs, were never retrieved and mostly miss this theme, though developers.openai.com is at least the same vendor domain the skill targets. Bounded alternatives and recoveries: a live retrieval pass against developers.openai.com if authorized, or dating each volatile claim with the archive snapshot month.

**Counterexample, gotchas, and operational comparison.** The model map's specificity, exact model IDs in a table, makes it look authoritative although its own maintenance notes predict drift. Good: citing upgrading-to-gpt-5p4.md for the three upgrade classes. Bad: citing the model map as the current best model. Borderline: citing docs.github.com/actions for CI verification habits, real but outside this theme's doctrine.

**Verification, evidence, and uncertainty.** Confirm every claim traces to one of the four read files and volatile claims carry the docs-win caveat. All four mapped local files were read in full during this evolution and no external retrieval occurred. Whether the archived guidance still matches live OpenAI docs is unverifiable without the MCP tools.

**Second-order consequence.** This theme's evidence map has an unusual inversion, the highest-authority source is external and live while the read local files rank themselves below it, so local facts here are simultaneously verified-read and doctrine-subordinate.

**Revision decision.** Mark all four local paths as read in full, record that every reference file self-labels as drift-prone helper content, and downgrade the unretrieved external rows to candidates.

**Retained seed evidence.** All seven source rows with their category, confidence, and synthesis-role columns remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| source_location_path_key | source_category_artifact_type | source_authority_confidence_level | source_usage_synthesis_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202603/.system/openai-docs/SKILL.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/codex-skills-202603/.system/openai-docs/references/gpt-5p4-prompting-guide.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/codex-skills-202603/.system/openai-docs/references/latest-model.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/codex-skills-202603/.system/openai-docs/references/upgrading-to-gpt-5p4.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| https://developers.openai.com/codex/guides/agents-md | external_research_source_material | external_research_sourced_fact | primary Codex custom instruction documentation |
| https://github.com/openai/codex | external_research_source_material | external_research_sourced_fact | GitHub implementation and project conventions |
| https://platform.openai.com/docs/guides/images | external_research_source_material | external_research_sourced_fact | primary image generation API documentation |

## Pattern Scoreboard Ranking Table

**Decision supported.** This section helps decide which documentation-discipline rules deserve default adoption when answering OpenAI questions or planning upgrades. The seed scoreboard scores corpus hygiene while the doctrine's own load-bearing rules go unranked, MCP-first tool order, docs-win over references, narrowest safe change set, and blocked over improvised scope stretch.

**Recommended default and causal basis.** Apply all four top-tier rules on every OpenAI question, then the per-workflow prompt-block guidance beneath them. The sources mark their own priorities, always prioritize MCP doc tools, reference files are convenience only, reserve blocked for cases that truly require implementation changes.

**Operating conditions and assumptions.** Each promoted rule keeps its falsifiable phrasing so a reviewer can point at the violation. The scoreboard ranks documentation-and-upgrade discipline rules and does not rank OpenAI products against each other.

**Failure boundary and alternatives.** The seed's numeric scores were never measured, and ranking the four promoted rules among themselves would be invention beyond the sources. Bounded alternatives and recoveries: order the rules by observed violation frequency once measured, or rank by blast radius with unverified model claims as the widest.

**Counterexample, gotchas, and operational comparison.** The blocked verdict feels like failure, so agents stretch scope instead, exactly the improvised broader upgrade the guide forbids. Good: a review that checks the answer cited a fetched doc. Bad: a polished answer built entirely from the bundled references. Borderline: skipping MCP for a question the skill's own product snapshots answer, tolerable for orientation only.

**Verification, evidence, and uncertainty.** Trace each promoted rule to its stated line in SKILL.md or the upgrade guide. The tooling notes, quality rules, and upgrade posture sections state each promoted rule. Which rule violations occur most often in real sessions is unmeasured.

**Second-order consequence.** All four top rules are humility rules, each one stops the agent from trusting itself, its cache, or its scope instincts over the live source and the stated boundary.

**Revision decision.** Promote a top tier of four rules, MCP-first retrieval, docs-win authority, narrowest-safe-change upgrades, and honest blocked or unknown verdicts instead of improvisation.

**Retained seed evidence.** All three scored rows with their tier labels and failure-prevention targets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| pattern_identifier_stable_key | pattern_score_numeric_value | pattern_tier_adoption_level | pattern_failure_prevention_target |
| --- | ---: | --- | --- |
| `openai_api_documentation_patterns` | 95 | default_adoption_pattern_tier | Source Map First: Load local openai api material before synthesizing documentation patterns recommendations. |
| `openai_api_documentation_patterns` | 91 | default_adoption_pattern_tier | Evidence Boundary Split: Separate local facts, external facts, and inference before giving agent instructions. |
| `openai_api_documentation_patterns` | 88 | default_adoption_pattern_tier | Verification Gate Coupling: Attach each recommendation to at least one command, checklist, or review gate. |

## Idiomatic Thesis Synthesis Statement

**Decision supported.** This section helps decide what single orienting claim should govern OpenAI documentation and upgrade judgments. The seed thesis repeats the load-local-first formula although this theme's doctrine inverts it, live official docs outrank the local corpus, which serves only as routing and helper context.

**Recommended default and causal basis.** Phrase the thesis as live-first retrieval, helper-only local context, minimal-change upgrades, with the three evidence labels kept on its clauses. The skill's quality rules subordinate its own reference files to current docs, and the upgrade guide subordinates every intervention to the narrowest safe change set.

**Operating conditions and assumptions.** The labels stay attached so skill-derived clauses remain distinguishable from inference. The thesis orients use of this reference and does not compress the per-block prompt guidance it stands on.

**Failure boundary and alternatives.** A docs-first thesis understates the upgrade half, the three-class decision discipline that governs GPT-5.4 migrations. Bounded alternatives and recoveries: quote the docs-win quality rule verbatim as the thesis, or phrase it as the upgrade posture's four bullets.

**Counterexample, gotchas, and operational comparison.** Paraphrases keep MCP-first and drop the blocked-over-improvised clause, the rule that most constrains agent behavior under pressure. Good: citing the thesis to demand a live-docs check before naming a model. Bad: quoting it to justify skipping the bundled references entirely, they still own routing. Borderline: compressing to docs always win for a prompt, losing the upgrade clause.

**Verification, evidence, and uncertainty.** Check the thesis clauses against the quality rules and the upgrade posture section. The skill's quality rules and the upgrade guide's posture bullets ground every clause of the restated thesis. Whether OpenAI's own guidance phrases the discipline the same way is unknown without retrieval.

**Second-order consequence.** The thesis unifies documentation and migration under one stance, distrust of cached knowledge, live docs beat bundled maps exactly as evals beat assumed prompt regressions.

**Revision decision.** Restate the combined inference as retrieve from live docs first, use local references only to route and scaffold, and upgrade with the smallest change that recovers behavior, declaring blocked rather than improvising.

**Retained seed evidence.** The three labeled thesis lines with their local, external, and combined-inference structure remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`local_corpus_sourced_fact`: The local row for `openai_api_documentation_patterns` contains 4 source path(s), which should be treated as the first retrieval surface for this theme.
`external_research_sourced_fact`: The external source map provides public documentation, repository, or ecosystem analogues where available.
`combined_evidence_inference_note`: Reliable use of Openai Api Documentation Patterns comes from loading the local corpus first, checking public ecosystem guidance second, and converting both into verification-backed agent decisions.

## Local Corpus Source Map

**Decision supported.** This section helps decide which local file a specific OpenAI question should open first. The seed map records heading signals without the corpus's real topology, an entrypoint skill with three request-conditional references, model selection, upgrade planning, and prompt rewriting, each loaded on an explicit trigger.

**Recommended default and causal basis.** Enter through the SKILL.md workflow and load references exactly on its stated triggers, never all three by default. The SKILL.md's reference map already routes by request type and orders the loads, latest-model for selection questions, upgrading-to-gpt-5p4 for explicit upgrades, the prompting guide when prompt changes may be needed.

**Operating conditions and assumptions.** All four files remain readable at their mapped paths with their trigger sections intact. The map indexes the four mapped local files and does not cover the live docs layer they defer to.

**Failure boundary and alternatives.** The routing goes stale if the archive is revised, and the files themselves warn they drift against live docs. Bounded alternatives and recoveries: record line anchors per prompt block, snapshot-date the mapping, or inline the trigger list here as quoted facts.

**Counterexample, gotchas, and operational comparison.** The prompting guide is the largest file and the most tempting to skip, yet the workflow loads it for research-heavy, tool-heavy, coding, multi-agent, or long-running upgrades, most real cases. Good: routing a best-model question to latest-model.md then verifying live. Bad: loading all three references for a simple docs lookup. Borderline: answering an upgrade question from the upgrade file alone when prompt changes are likely needed.

**Verification, evidence, and uncertainty.** Open the four files and confirm the workflow, triggers, and self-deprecation clauses appear as described. All four files were read in full, 701 lines, with the topology and loading triggers recorded here. Whether sibling skills in the archive overlap this doctrine is unknown until read.

**Second-order consequence.** The corpus is triggered lazily by design, the skill says read only what you need, so the map's job is routing precision rather than coverage, a different goal than most themes' source maps.

**Revision decision.** Annotate the rows with the skill's own loading triggers and the read-only-what-you-need rule, plus each file's self-deprecation clause.

**Retained seed evidence.** All four local source rows with their titles, heading signals, and usage roles remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| local_source_filepath_value | local_source_title_text | local_source_heading_signals | local_source_usage_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202603/.system/openai-docs/SKILL.md | "openai-docs" | OpenAI Docs; Quick start; OpenAI product snapshots; If MCP server is missing; Workflow; Reference map | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/codex-skills-202603/.system/openai-docs/references/gpt-5p4-prompting-guide.md | GPT-5.4 prompting upgrade guide | GPT-5.4 prompting upgrade guide; Default upgrade posture; Behavioral differences to account for; Prompt rewrite patterns; Prompt blocks; 'output_verbosity_spec' | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/codex-skills-202603/.system/openai-docs/references/latest-model.md | Latest model guide | Latest model guide; Current model map; Maintenance notes | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/codex-skills-202603/.system/openai-docs/references/upgrading-to-gpt-5p4.md | Upgrading to GPT-5.4 | Upgrading to GPT-5.4; Upgrade posture; Upgrade workflow; Upgrade outcomes; 'model string only'; 'model string + light prompt rewrite' | reference detail file for deeper pattern evidence |

## External Research Source Map

**Decision supported.** This section helps decide how much weight external rows may carry in OpenAI documentation guidance. The seed map lists AGENTS.md guides and GitHub Actions docs as external facts although none was retrieved, and this theme's real external apex, developers.openai.com and platform.openai.com, appears only inside the skill's own text.

**Recommended default and causal basis.** Rest all claims on the four read local files and treat external corroboration as absent until the MCP tools or official domains are actually queried. External rows are meant to corroborate the theme, and the skill itself names the exact authoritative domains and even the MCP install command that reaches them.

**Operating conditions and assumptions.** Each row keeps a note naming what it could and could not confirm. The map catalogs candidate external references and does not certify content, freshness, or relevance.

**Failure boundary and alternatives.** Removing the seed rows would break preservation, so they stay with downgraded labels and a mismatch note. Bounded alternatives and recoveries: an authorized MCP retrieval pass, restricted web search on the two official domains, or leaving the table annotated as is.

**Counterexample, gotchas, and operational comparison.** Developers.openai.com in the seed rows looks like it corroborates this theme, but it was cited for an AGENTS.md guide, not for the API docs the theme concerns. Good: naming the MCP docs server as the retrieval target. Bad: citing agents.md for model-selection facts. Borderline: citing the seed's developers.openai.com row for this theme, right domain but wrong document.

**Verification, evidence, and uncertainty.** Confirm no claim cites an external row as fact and the mismatch note is present. No external retrieval was performed and the skill's tooling notes name the official domains. Whether the MCP server's current content confirms the archived guidance is unknown.

**Second-order consequence.** This theme is the corpus's clearest case of a named live oracle, the skill ships the exact command to install the docs server, so future refresh is an installation task rather than a search problem.

**Revision decision.** Downgrade the three seed rows to unretrieved candidates and name the skill's own targets, the developers.openai.com MCP server and platform.openai.com, as the natural retrieval candidates.

**Retained seed evidence.** All three external rows with their names, roles, and boundary labels remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| external_source_url_value | external_source_name_text | external_source_usage_role | evidence_boundary_label_value |
| --- | --- | --- | --- |
| https://developers.openai.com/codex/guides/agents-md | OpenAI Codex AGENTS.md guide | primary Codex custom instruction documentation | external_research_sourced_fact |
| https://github.com/openai/codex | OpenAI Codex repository | GitHub implementation and project conventions | external_research_sourced_fact |
| https://platform.openai.com/docs/guides/images | OpenAI image generation guide | primary image generation API documentation | external_research_sourced_fact |

## Anti Pattern Registry Table

**Decision supported.** This section helps decide which recurring documentation-and-upgrade failures deserve standing detection rules. The seed registry lists corpus-hygiene failures while the sources name this theme's own anti-patterns, answering from stale references, stretching a blocked upgrade into code changes, adding every prompt block by default, and raising reasoning effort before prompt-level fixes.

**Recommended default and causal basis.** Scan answers for missing live-docs verification, upgrade plans for out-of-scope edits, and prompts for blocks with no named regression behind them. Each is stated with its correction, docs win over references, report the blocker instead of improvising, use blocks selectively, treat reasoning effort as a last-mile knob.

**Operating conditions and assumptions.** Each row pairs its smell with the observable test the sources state. The registry names documentation-and-upgrade anti-patterns with detectors and does not police general coding conduct.

**Failure boundary and alternatives.** The registry cannot rank these by frequency, no violation data exists. Bounded alternatives and recoveries: encode the checks into the prompt regression checklist, fold detection into the completeness section, or keep the registry as smell-to-correction pointers.

**Counterexample, gotchas, and operational comparison.** Block-stuffing feels diligent, adding all the prompt scaffolding looks thorough while the guide explicitly says do not add all of them by default. Good: rejecting an upgrade plan that rewrites tool wiring. Bad: a prompt carrying ten blocks for a simple assistant. Borderline: adding a verbosity clamp preemptively, the guide says wait for the regression first.

**Verification, evidence, and uncertainty.** Replay each registry row against the sources' stated corrections and confirm its test is executable on a real answer or upgrade plan. The quality rules, upgrade posture, block-usage warning, and last-mile-knob rule supply every added row. Relative frequency of each anti-pattern in real sessions is unmeasured.

**Second-order consequence.** Three of the four anti-patterns are overcorrection failures, doing more than the situation warrants, which mirrors the guide's leanness rule that every added prompt block must address an observed regression.

**Revision decision.** Add rows for stale-reference answering, scope-stretched upgrades, block-stuffing, and premature effort-raising, each keyed to its source-stated correction.

**Retained seed evidence.** All three original registry rows with their causes, replacements, and detection methods remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| anti_pattern_failure_name | failure_cause_risk_reason | safer_default_replacement_pattern | detection_signal_review_method |
| --- | --- | --- | --- |
| context_free_summary_output | agent skips local corpus and produces generic advice | source_map_first_synthesis | verify every listed local path appears in the generated file |
| unsourced_recommendation_claims | guidance appears authoritative without source boundary | evidence_boundary_split_pattern | check for local, external, and inference labels |
| unverified_agent_instruction | recommendation cannot be checked by command or review gate | verification_gate_coupling | require concrete gate in generated reference |

## Verification Gate Command Set

**Decision supported.** This section helps decide which gates must pass before OpenAI upgrade guidance or this reference's own guidance is trusted. The seed gate names the corpus verifier while the theme's real gates are the sources' own checklists, the six-item no-code compatibility checklist, the validation plan, and the prompt regression checklist.

**Recommended default and causal basis.** Run the compatibility checklist per usage site, record the verdict with its failing item, and validate every upgraded site with existing evals or realistic spot checks. The upgrade doctrine is gate-driven by design, compatibility is checked before recommending, evals validate after upgrading, and each prompt block must prove it addresses an observed regression.

**Operating conditions and assumptions.** The reviewer can inspect the integration's model strings, prompt surfaces, and tool wiring. The gate set defines what must pass before upgrade guidance is trusted and does not automate the judgment.

**Failure boundary and alternatives.** The gates are judgment calls over a specific integration, two reviewers can disagree on whether a fix is prompt-only or needs implementation work. Bounded alternatives and recoveries: spot-checking only high-traffic usage sites, pair review for contested blocked verdicts, or eval-first gating where suites already exist.

**Counterexample, gotchas, and operational comparison.** Checklist item one, can the host accept the new model string without code changes, silently fails when configs are generated rather than edited, a case the checklist wording does not surface. Good: a per-site record with verdict, failing checklist item, and eval result. Bad: a sweeping viable verdict with no site inventory. Borderline: an unknown verdict where the user could locate the prompt surface, resolvable by asking.

**Verification, evidence, and uncertainty.** Run the compatibility checklist against a sample integration and confirm each item yields a decidable answer or an honest unknown. The no-code compatibility checklist, validation plan, and prompt regression checklist state every gate verbatim. Inter-reviewer agreement on prompt-only versus implementation-change judgments is unmeasured.

**Second-order consequence.** The gates encode a three-verdict logic rather than pass-fail, viable, blocked, and unknown, and the doctrine treats returning unknown as success, an honesty standard most gate systems lack.

**Revision decision.** Adopt the compatibility checklist as the pre-recommendation gate, the validation plan as the post-upgrade gate, and the regression checklist as the prompt-edit gate, with blocked and unknown as legitimate outcomes.

**Retained seed evidence.** The original verification gate line and its repository verifier command block remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`verification_gate_command_set`: Run the repository verifier after editing this file.

```bash
python3 agents-used-monthly-archive/idiomatic-references-202606/tools/verify_reference_generation.py --stage final
```

## Agent Usage Decision Guide

**Decision supported.** This section helps decide when a working agent should open this reference and which section it should enter through. The seed guide keys usage to theme mentions instead of the request classes the skill routes on, docs lookup, model selection, explicit GPT-5.4 upgrade, and prompt upgrade.

**Recommended default and causal basis.** Classify the request first, then open this reference at the section owning that class before touching any bundled file. The skill's workflow step one is exactly this classification, clarify whether the request is general lookup, model selection, an upgrade, or a prompt upgrade, and everything downstream branches on it.

**Operating conditions and assumptions.** The question concerns building with OpenAI products or APIs and needs current, citable guidance. The guide routes readers into this reference and does not choose models or upgrade classes itself.

**Failure boundary and alternatives.** Keying to every OpenAI mention would drag the doctrine into questions about the company rather than building with its APIs. Bounded alternatives and recoveries: generic API-integration references for non-OpenAI vendors, or the media references for image-generation workflow questions.

**Counterexample, gotchas, and operational comparison.** Prompt-upgrade requests hide inside upgrade requests, the workflow loads the prompting guide whenever the upgrade may require prompt changes, which agents skip when the model string swap looks clean. Good: classifying a which-model question and entering at the scoreboard's verification rules. Bad: opening this for OpenAI company news. Borderline: a prompt-tuning question with no upgrade attached, served by the block catalog alone.

**Verification, evidence, and uncertainty.** Walk one request of each class through the guide and confirm each lands on the intended entry point. The skill's description and workflow step one partition the entry points as described. The real mix of request classes agents encounter is unmeasured.

**Second-order consequence.** The highest-value trigger is the misclassified request, an upgrade question answered as a docs lookup skips the compatibility gate entirely, so classification errors cost more than retrieval errors.

**Revision decision.** Trigger on build-with-OpenAI questions, route selection requests through the model map with live verification, upgrades through the three-class doctrine, and prompt regressions through the block catalog.

**Retained seed evidence.** The original usage line and all four guidance bullets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`agent_usage_decision_guide`: Use this reference when a task mentions this theme, one of the listed local source paths, or a nearby technology/workflow surface.

- Start with the local corpus source map.
- Prefer patterns with explicit verification gates.
- Treat external sources as freshness and ecosystem checks, not replacements for local repo conventions.
- Preserve the evidence boundary labels when reusing recommendations.

## User Journey Scenario

**Decision supported.** This section helps decide what end-to-end shape a competent OpenAI upgrade session should take. The seed scenario shows a builder choosing a pattern and stops before the journey the upgrade doctrine scripts, inventory, pairing, classification, compatibility gate, recommendation, and structured delivery.

**Recommended default and causal basis.** Narrate an inventory-to-recommendation pass using the structured delivery fields as the destination shape. The upgrade workflow is a seven-step sequence with an explicit output contract, so the journey should walk one integration through all seven rather than end at selection.

**Operating conditions and assumptions.** The agent can search the integration's code and configs for model strings and prompt-bearing files. The scenario dramatizes one representative upgrade journey and does not cover realtime or image workflows.

**Failure boundary and alternatives.** One journey cannot cover both the upgrade path and the plain docs-lookup path, which is shorter and MCP-driven. Bounded alternatives and recoveries: a docs-lookup journey through search and fetch with citations, or a prompt-regression journey through the block catalog.

**Counterexample, gotchas, and operational comparison.** Journeys that skip the per-site reasoning-effort recommendation violate the output rule, every usage site must get a starting recommendation, never null. Good: a journey ending with the eight structured recommendation fields filled per site. Bad: one ending at replace the string everywhere. Borderline: a journey that returns blocked at the gate, complete despite recommending nothing.

**Verification, evidence, and uncertainty.** Check each journey beat against the seven workflow steps and confirm none is skipped silently. The upgrade workflow and its structured-recommendation field list script exactly this sequence. Typical integration sizes and usage-site counts are unrecorded.

**Second-order consequence.** The journey's decisive beat is the pairing step, tying each model usage to its prompt surface, because an unpairable prompt forces the honest unknown verdict that keeps the whole recommendation trustworthy.

**Revision decision.** Extend the journey through a GPT-4.1 assistant upgrade, usage sites inventoried, prompts paired, family classified, compatibility gated, gpt-5.4 recommended with none reasoning effort, and the structured recommendation delivered.

**Retained seed evidence.** The role-based opening, starting state, decision, and trigger lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Role based opening scenario: The reader or documentation author is starting cold and deciding whether the reference answers the next practical question and needs a reference that turns source evidence into an executable next step.
Primary user starting state: The user has a `openai_api_documentation_patterns` task, one or more local source paths, and uncertainty about which pattern should drive implementation.
Decision being made: choosing the reading path, example, diagram, or rewrite pattern that makes action obvious.
Reference opening trigger: Open this file when the task mentions openai api documentation patterns, any mapped local source path, or an adjacent workflow with the same failure mode.

## Decision Tradeoff Guide

**Decision supported.** This section helps decide how strictly the doctrine binds for a given request and what being wrong costs. The seed guide keys adopt, adapt, and avoid to generic evidence agreement instead of this theme's variables, upgrade class, workflow shape, and whether live verification is available.

**Recommended default and causal basis.** Choose the smallest upgrade class the evidence supports and never skip the compatibility gate even when compressing everything else. The doctrine itself grades intervention size by workflow shape, model string only for short bounded prompts, light rewrite for research or tool-heavy flows, blocked when implementation changes loom.

**Operating conditions and assumptions.** The integration's model usage and prompt surfaces are inspectable before the class decision. The guide calibrates intervention size per integration and cannot waive the docs-win rule where answers are delivered.

**Failure boundary and alternatives.** Judging workflow shape is subjective, a minimal visible snippet can hide a tool-heavy host, which the guide addresses by forbidding blocked verdicts on snippet minimalism alone. Bounded alternatives and recoveries: eval-driven class escalation, starting at model string only and moving up on observed regressions, or deferring the whole upgrade until MCP verification is restored.

**Counterexample, gotchas, and operational comparison.** Being wrong costs invisibly at first, a stale model recommendation reads fine today and fails when the customer builds on a deprecated ID. Good: model string only for a short bounded assistant prompt. Bad: a broad prompt cleanup bundled into an upgrade. Borderline: light rewrite chosen on suspicion of regressions before any eval, tolerated when the workflow shape matches the guide's named profiles.

**Verification, evidence, and uncertainty.** Audit recent recommendations for class against workflow shape and check failures for skipped gates. The three upgrade-class criteria sections state the intervention grading this guide rekeys onto. The regression base rates that would justify preemptive light rewrites are unmeasured.

**Second-order consequence.** The doctrine prices being wrong asymmetrically, an over-broad upgrade breaks working integrations while an honest blocked verdict merely defers value, which is why every ambiguity resolves toward the smaller intervention.

**Revision decision.** Rekey adopt to full doctrine for upgrades and cited answers, adapt to reference-only routing when MCP is unavailable with staleness flagged, and avoid for non-OpenAI or non-building questions.

**Retained seed evidence.** The Adopt when, Adapt when, Avoid when, and Cost of being wrong rows with their verification prompts remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| decision_option_name | when_to_choose_condition | tradeoff_cost_description | verification_question_prompt |
| --- | --- | --- | --- |
| Adopt when | local corpus and external evidence agree on the openai api documentation patterns pattern | fastest path, but can copy stale local assumptions | Does the selected pattern appear in the canonical source and current external evidence? |
| Adapt when | local sources are strong but public ecosystem guidance has changed | preserves repo fit, but requires explicit inference notes | Did the reference label the local fact, external fact, and combined inference separately? |
| Avoid when | source evidence is thin, conflicting, or unrelated to the user journey | prevents false confidence, but may require deeper research | Is there a confidence warning or adjacent reference route? |
| Cost of being wrong | wrong openai api documentation patterns guidance can send an agent to the wrong files, tests, or abstraction | wasted implementation loop and weaker verification | Would a reviewer know what to undo and what to inspect next? |

## Local Corpus Hierarchy

**Decision supported.** This section helps decide which source outranks which when OpenAI guidance conflicts or runs out. The seed hierarchy names sources without ranking them, while this corpus states its own ranking explicitly, live OpenAI docs above everything, the SKILL.md as process spine, and the three references as subordinate helper context.

**Recommended default and causal basis.** Resolve process questions by the skill, upgrade questions by the upgrade guide, and mark any suspected docs divergence as unverifiable here. The skill's quality rules subordinate the references, and each reference file repeats the subordination in its own header or maintenance notes.

**Operating conditions and assumptions.** The four files remain internally consistent as currently read. The hierarchy ranks local retrieval priority for this theme and cannot certify the live layer it defers to.

**Failure boundary and alternatives.** The apex of the hierarchy, live docs, was not consulted here, so archive-versus-docs conflicts are undetectable in this evolution. Bounded alternatives and recoveries: an authorized MCP pass to check the apex, inlining the self-deprecation clauses as the ranking record, or leaving the flat list with this note.

**Counterexample, gotchas, and operational comparison.** The model map ranks lowest yet gets quoted most, exact model IDs travel further than the caveats around them. Good: resolving an upgrade-scope question from the upgrade guide's boundaries. Bad: quoting the model map over a fetched doc page. Borderline: preferring the prompting guide's example profiles over the upgrade guide's class criteria, resolved by treating profiles as illustrations.

**Verification, evidence, and uncertainty.** Confirm the four paths exist and each file's self-ranking clause matches the hierarchy recorded here. The quality rules, maintenance notes, and per-file verification clauses state the structure described. Whether the archive diverges from live docs anywhere is unknowable without retrieval.

**Second-order consequence.** The hierarchy is self-declared rather than inferred, every file states its own rank relative to live docs, which makes conflicts easy to resolve on paper and impossible to detect without the MCP tools.

**Revision decision.** Rank live docs first though unread here, SKILL.md first among read files for process, the upgrade guide for migration doctrine, the prompting guide for block selection, and the model map last as the most drift-prone.

**Retained seed evidence.** The classification vocabulary line, the confidence warning, and the hierarchy rows with their reviewer questions remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Classification vocabulary includes canonical, supporting, legacy, duplicate, and conflicting source roles.

| local_source_filepath_value | corpus_hierarchy_role | heading_signal_to_convert | reviewer_question_to_answer |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202603/.system/openai-docs/SKILL.md | canonical primary source | OpenAI Docs; Quick start; OpenAI product snapshots | What guidance, warning, or example should this source contribute to Openai Api Documentation Patterns? |
| agents-used-monthly-archive/codex-skills-202603/.system/openai-docs/references/gpt-5p4-prompting-guide.md | supporting detail source | GPT-5.4 prompting upgrade guide; Default upgrade posture; Behavioral differences to account for | What guidance, warning, or example should this source contribute to Openai Api Documentation Patterns? |
| agents-used-monthly-archive/codex-skills-202603/.system/openai-docs/references/latest-model.md | supporting detail source | Latest model guide; Current model map; Maintenance notes | What guidance, warning, or example should this source contribute to Openai Api Documentation Patterns? |
| agents-used-monthly-archive/codex-skills-202603/.system/openai-docs/references/upgrading-to-gpt-5p4.md | supporting detail source | Upgrading to GPT-5.4; Upgrade posture; Upgrade workflow | What guidance, warning, or example should this source contribute to Openai Api Documentation Patterns? |

## Theme Specific Artifact

**Decision supported.** This section helps decide what concrete evidence object must exist before this reference counts as operational. The seed artifact names a lifecycle diagram while this theme's operational artifact is the structured upgrade recommendation, the eight-field per-site record the workflow requires as its deliverable.

**Recommended default and causal basis.** Carry one filled recommendation from a real or representative integration as the reviewable instance. The upgrade workflow's final step names the fields, current usage, model-string updates, starting reasoning recommendation, prompt updates, phase assessment, compatibility check, validation plan, and launch-day refresh items.

**Operating conditions and assumptions.** The record names each usage site, its verdict, and the checklist item behind any blocked or unknown outcome. The artifact certifies this reference is operational and does not grade the upgraded integration's runtime behavior.

**Failure boundary and alternatives.** Recommendation records for trivial single-site swaps are ceremony, the null-instance convention applies. Bounded alternatives and recoveries: a compressed record for single-site integrations, a docs-lookup citation log for non-upgrade sessions, or eval results as the post-upgrade companion artifact.

**Counterexample, gotchas, and operational comparison.** Records filled after the upgrade rationalize what was done rather than gate it, the workflow orders delivery before execution. Good: a record showing two viable sites and one blocked with its failing checklist item. Bad: an upgraded integration with no recorded verdicts. Borderline: a record without launch-day refresh items for an integration already on the final guidance.

**Verification, evidence, and uncertainty.** Check the artifact fills all eight fields per site and every reasoning-effort recommendation is explicit. The workflow's structured-recommendation step and output rule define the exact fields the artifact instantiates. Whether record discipline measurably improves upgrade outcomes here is untested.

**Second-order consequence.** The artifact doubles as an audit trail, its compatibility and phase fields record why an upgrade was or was not attempted, evidence that outlives the upgrade itself.

**Revision decision.** Define the artifact as one filled structured recommendation for a real integration, per usage site, with verdicts and the reasoning-effort recommendation never left null.

**Retained seed evidence.** The artifact definition line and the three artifact field rows with completion rules remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Theme specific artifact: worked openai api documentation patterns example with user goal, decision point, failure mode, and verification gate.

| artifact_field_name | artifact_completion_rule | evidence_source_hint |
| --- | --- | --- |
| user_goal_statement | state the user's concrete goal before applying Openai Api Documentation Patterns | local corpus hierarchy plus critique findings |
| decision_boundary_rule | define the point where this reference should be used or avoided | decision tradeoff guide |
| verification_gate_rule | define the command, checklist, or review question that proves the artifact worked | verification gate command set |

## Worked Example Set

**Decision supported.** This section helps decide which behaviors should be taught as exemplary, negligent, or conditionally acceptable. The seed examples restate corpus verdicts and never grade real conduct against the doctrine's own contrasts, verified versus stale answers, minimal versus stretched upgrades, selective versus stuffed prompt blocks.

**Recommended default and causal basis.** Grade every example by the doctrine's tests, was the claim verified live, was the change the narrowest safe one, does each prompt block answer an observed regression. The sources teach through explicit contrast, prefer light rewrite over blocked, do not add all blocks by default, remove blocks that are not earning their keep.

**Operating conditions and assumptions.** Each example names the rule it exercises and the test that decides the verdict. The examples grade documentation-and-upgrade conduct, not the quality of OpenAI's products.

**Failure boundary and alternatives.** Examples fixed to GPT-5.4 specifics will date as the model line moves, though the discipline transfers. Bounded alternatives and recoveries: draw examples from this repository's own upgrade sessions, grade the guide's example profiles directly, or add a docs-lookup example with citation discipline.

**Counterexample, gotchas, and operational comparison.** The borderline case is availability-dependent, reference-only answers are acceptable during outages and negligent when the MCP tools were reachable. Good: an upgrade delivering model string only with eval validation. Bad: an answer naming the best model straight from the bundled map. Borderline: adding tool_persistence_rules preemptively to a long-horizon agent, matching a named profile without an observed regression.

**Verification, evidence, and uncertainty.** Scan each verdict against its cited rule and confirm the graded behavior is visible in the described conduct. The block-usage warning, upgrade posture, and regression checklist ground all three verdicts. Which negligent shape dominates real sessions is unmeasured.

**Second-order consequence.** The sources' bad behaviors are all reasonable-looking diligence, exhaustive prompt scaffolding and ambitious upgrade scope read as thoroughness, which is why the doctrine names them explicitly instead of trusting judgment.

**Revision decision.** Recast good as a cited answer verified through fetched docs, bad as an upgrade that rewires tools to force compatibility, and borderline as a reference-only answer during MCP outage with staleness flagged.

**Retained seed evidence.** The good, bad, and borderline example lines with their original verdict framing remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Good example: Use Openai Api Documentation Patterns after loading the canonical source, confirming the external evidence boundary, and writing a verification gate before implementation.
Bad example: Use Openai Api Documentation Patterns as a generic tutorial while ignoring the mapped local paths, source hierarchy, and cost of being wrong.
Borderline case: Use Openai Api Documentation Patterns only after adding a confidence warning when local evidence is thin or conflicts with current ecosystem guidance.

## Outcome Metrics and Feedback Loops

**Decision supported.** This section helps decide which observable signals should trigger revising practice or this reference. The seed metrics name lead time and generic signals without this theme's observables, citation coverage on answers, verdict distribution across upgrade classes, and prompt blocks removed at regression review.

**Recommended default and causal basis.** Record per session the request class, whether live verification happened, the verdict or answer shape, and any blocks added with their named regressions. The doctrine's benefit is trustworthy guidance and minimal interventions, so its instruments must count verified citations, honest blocked and unknown verdicts, and blocks that earned their keep.

**Operating conditions and assumptions.** Sessions record verdicts against named checklist items rather than as general outcomes. The metrics gauge documentation-and-upgrade discipline, not the upgraded integrations' business outcomes.

**Failure boundary and alternatives.** Verdict distributions mislead without denominators, a spike in blocked may mean harder integrations rather than laxer effort. Bounded alternatives and recoveries: sampled answer audits, eval pass rates on upgraded sites, or tracking only the citation fraction at first.

**Counterexample, gotchas, and operational comparison.** A rising cited-answer fraction can mean better discipline or easier questions, so occasional deep audits serve as the independent check. Good: tightening gate guidance after repeated unknown verdicts traced to unpaired prompts. Bad: celebrating citation rates while audits find stale model names. Borderline: skipping metrics in a period with no OpenAI sessions, noted.

**Verification, evidence, and uncertainty.** Reconcile recorded verdicts against sampled audits and check the failing checklist items match the guidance being tightened. The seed's lead-time indicator and the sources' checklist-keyed verdicts anchor the added counters. Healthy baselines for citation coverage and verdict mix are unmeasured, so first thresholds are provisional.

**Second-order consequence.** The cheapest telemetry is the citation, its presence separates verified answers from cache-quoting without rereading the answer, mirroring the answer-sentence probe other themes use.

**Revision decision.** Adopt cited-answer fraction, per-class verdict counts with reasons, and block-retention rate after regression review as primary signals.

**Retained seed evidence.** The leading indicator, failure signal, and review cadence lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Leading indicator: a new reader can apply the reference without asking the author for hidden context.
Failure signal: the reference is a literature dump instead of a guided explanation.
Review cadence: Re-run the verifier after every generated-reference edit and refresh external sources when public APIs, docs, or tooling releases change.

## Completeness Checklist

**Decision supported.** This section helps decide when this reference may be declared ready to hand to an agent. The seed checklist confirms generic sections exist and never checks this document's specific obligations, the MCP-first order, the docs-win rule, all three upgrade classes, the compatibility gate, and the block-selectivity warning present and uninverted.

**Recommended default and causal basis.** Tick structural items with citations, then grep this document for each rule, class, gate, and warning. This document transmits a discipline whose value lies in its restraints, so readiness means the restraints survived transmission intact.

**Operating conditions and assumptions.** Each added item names its target and whether a script or human verifies it. The checklist gates this document's readiness, not the quality of upgrades later performed under it.

**Failure boundary and alternatives.** A reference that dropped the blocked-over-improvised rule would still describe upgrades while losing the boundary that makes them safe. Bounded alternatives and recoveries: generate coverage items from the sources' section lists, deep-check two random items per review, or pair-review the artifact record.

**Counterexample, gotchas, and operational comparison.** Rule presence can pass while phrasing drifted, narrowest safe change set weakened to prefer small changes materially loosens the doctrine. Good: a tick citing the line carrying the blocked-over-improvised rule. Bad: all ticks green from a headings glance. Borderline: carrying forward last cycle's phrasing check with a staleness note.

**Verification, evidence, and uncertainty.** Grep this document for the rules, classes, and gates, then spot-read two against the sources. The seed's seven structural items map onto real sections here and anchor the added fidelity layer. How much spot-reading each cycle needs depends on edit volume.

**Second-order consequence.** The doctrine's own regression checklist doubles as this document's fidelity probe, asking whether the transmitted guidance is leaner, not just longer, applies to this reference as much as to any prompt.

**Revision decision.** Append items requiring the tool order stated, the docs-win rule present, the three classes with their criteria, the six-item gate reachable, and the selective-blocks warning carried.

**Retained seed evidence.** All seven structural checklist items covering scenario, decision guide, hierarchy, artifact, examples, metrics, and routing remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- The role scenario names the user, starting state, decision, and trigger for Openai Api Documentation Patterns.
- The decision guide includes Adopt when, Adapt when, Avoid when, and Cost of being wrong.
- The local corpus hierarchy identifies canonical and supporting sources or gives a confidence warning.
- The theme specific artifact is concrete enough to review without reading every mapped source.
- The examples cover good, bad, and borderline usage.
- The metrics section names one leading indicator and one failure signal.
- The adjacent routing section points to a better reference when this one is not the right fit.

## Adjacent Reference Routing

**Decision supported.** This section helps decide when a question should leave this reference and which neighbor owns it. The seed routing splits the theme name into keywords aimed at unnamed destinations instead of routing by need, OpenAI docs discipline stays here while image generation, general prompting craft, and non-OpenAI API integration belong elsewhere.

**Recommended default and causal basis.** Ask whether the answer would change when OpenAI's docs change, and keep only such questions here. Readers arrive with OpenAI-adjacent needs this doctrine does not own, media production has its own references and generic prompt engineering is not this skill's subject.

**Operating conditions and assumptions.** Each route names its trigger, a destination resolving to a real file, and what stays here. Routing redirects within this corpus and cannot authorize work in a destination's domain.

**Failure boundary and alternatives.** Keyword routes point at references that exist only as words, stranding the reader who follows them. Bounded alternatives and recoveries: consult the corpus index before adding routes, keep unresolved needs here with a gap note, or escalate genuine overlap to the user.

**Counterexample, gotchas, and operational comparison.** Prompt-block questions blur the seam, the block catalog lives here because it serves upgrades, yet generic prompt-tuning requests will land on it. Good: keeping a which-model-for-classification question here. Bad: routing to the openai adjacent reference, a keyword with no file. Borderline: a gpt-image-1.5 usage question split between the model map here and workflow guidance in the media references.

**Verification, evidence, and uncertainty.** Resolve each named destination to an existing corpus file and walk one sample question through each trigger. The model map's image and audio rows and the skill's build-with-OpenAI scope define the seam the routes follow. Whether future themes will subdivide this doctrine's territory is unknown.

**Second-order consequence.** The doctrine's boundary is the vendor-and-currency seam, it owns questions whose answers must track OpenAI's live documentation, and disowns questions that are stable across vendors or time.

**Revision decision.** Keep docs retrieval, model selection, and GPT-5.4 upgrade doctrine here, route image-model usage to the media references, and record unowned needs like generic prompting craft as gaps.

**Retained seed evidence.** The adjacency guidance line and the three keyword-derived route stubs remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Adjacent reference guidance: Use visual, ASCII, HTML, or writing references when the output medium is fixed.
Adjacent reference 1: consider the openai adjacent reference when the current task pivots away from openai api documentation patterns.
Adjacent reference 2: consider the api adjacent reference when the current task pivots away from openai api documentation patterns.
Adjacent reference 3: consider the documentation adjacent reference when the current task pivots away from openai api documentation patterns.

## Workload Model

**Decision supported.** This section helps decide how much assessment work one session may take on before splitting. The seed model bounds endpoints per batch but not this theme's working unit, one integration's upgrade assessed per focused pass, with usage-site count as the real cost driver.

**Recommended default and causal basis.** Assess one integration per focused session, stopping at the site count where per-site records stay complete. The workflow inventories every usage site and pairs each with its prompt surface, so effort scales with sites and prompt-surface distance rather than codebase size.

**Operating conditions and assumptions.** The session can hold the full site inventory in view, in the artifact record. The model bounds assessment work per session and does not bound the eval runs that validate afterward.

**Failure boundary and alternatives.** Site-count bounds are estimates, one site with tangled shared templates can outweigh ten clean inline prompts. Bounded alternatives and recoveries: splitting inventory and recommendation into separate passes, batching sites by shared prompt surface, or pair sessions for contested blocked verdicts.

**Counterexample, gotchas, and operational comparison.** Docs-lookup sessions look free but each verified answer costs a search and a fetch, retrieval discipline has per-question overhead the model should not hide. Good: one integration inventoried, gated, and recorded in a pass. Bad: five integrations swept with unverified viable verdicts. Borderline: a large monorepo split by service with the inventory frozen between sessions.

**Verification, evidence, and uncertainty.** Compare session outcomes at different site counts and record where record completeness degrades. The workflow's inventory and pairing steps ground the site-based model. Typical site counts per integration are unmeasured.

**Second-order consequence.** The expensive case is the unpairable prompt, hunting a prompt surface that cannot be confidently tied to its usage is unbounded, which is why the doctrine licenses the unknown verdict as the workload escape valve.

**Revision decision.** Rebound the model around one integration per pass, per-site records as the unit of progress, and the prompting-guide load budgeted when any site needs a rewrite.

**Retained seed evidence.** The four workload dimensions with their boundary values and verification pressure points remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`combined_evidence_inference_note`: Treat Openai Api Documentation Patterns as a documentation reference operating reference, not as a prose summary.

| workload_dimension_name | workload_boundary_value | verification_pressure_point |
| --- | --- | --- |
| primary_usage_surface | reference selection, writing, roadmap, or explanation work where the output should improve the next human or agent decision | verify that the reference changes the next implementation or review action |
| bounded_capacity_model | one audience, one decision, up to 12 source documents, and one verification checklist per reference use | split the task or create a narrower reference when this boundary is exceeded |
| source_pressure_model | local heading signals include OpenAI Docs; Quick start; OpenAI product snapshots; If MCP server is missing; Workflow; Reference map; GPT-5.4 prompting upgrade guide; Default upgrad | compare guidance against canonical local sources before following external examples |
| artifact_pressure_model | required artifact is worked openai api documentation patterns example with user goal, decision point, failure mode, and verification gate | require the artifact before claiming the reference is operationally usable |

## Reliability Target

**Decision supported.** This section helps decide what measurable reliability this reference must demonstrate before its guidance is trusted. The seed table demands unmeasured percentages while this theme supports binary targets, every delivered answer carries a live citation or a staleness flag, and every upgrade recommendation carries a per-site verdict.

**Recommended default and causal basis.** Keep the four seed dimensions with methods attached and lead with the two per-deliverable scans. The doctrine's tests are per-deliverable and decidable, a citation exists or does not, a site record exists or does not, so targets can be scanned rather than sampled.

**Operating conditions and assumptions.** Each target names its metric, scan method, population, owner, and corrective action. The targets judge this reference and the discipline, not OpenAI's API reliability.

**Failure boundary and alternatives.** Quoting the seed's percentages as achieved performance manufactures rigor this corpus never earned. Bounded alternatives and recoveries: eval-pass targets on upgraded sites, sampled record audits, or postmortems per stale answer instead of rates.

**Counterexample, gotchas, and operational comparison.** A present citation does not prove the answer matches it, the deep audit remains the independent second gate. Good: a scan showing every answer cited or flagged. Bad: reporting the seed's numbers nobody sampled. Borderline: one uncited answer during a verified MCP outage, recorded with its staleness flag.

**Verification, evidence, and uncertainty.** Scan one period's deliverables for both targets and record hits with resolutions. The citation quality rules and the structured-recommendation contract give the operational definitions the scans check. No baseline exists for either target, so the first scanned period defines achievability.

**Second-order consequence.** The citation target audits the doctrine's core claim, that answers track live docs, and its absence predicts exactly the stale-model failures the model map's maintenance notes warn about.

**Revision decision.** Add binary targets, a citation or explicit staleness flag per answer and a complete verdict record per upgrade, each marked unbaselined and owned.

**Retained seed evidence.** All four reliability rows with their threshold values and evidence-collection methods remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| reliability_target_name | measurable_threshold_value | evidence_collection_method |
| --- | --- | --- |
| source_boundary_preservation | 100 percent of recommendations keep local, external, and inference boundaries visible | review generated text for the three evidence labels before reuse |
| decision_accuracy_sample | at least 18 of 20 sampled uses route to the correct adopt, adapt, avoid, or adjacent-reference decision | sample downstream tasks and record reviewer verdicts |
| unsupported_claim_rate | zero unsupported production, security, latency, or reliability claims in final guidance | reject claims without source row, explicit inference note, or verification method |
| recovery_path_clarity | every avoid or failure case names the rollback, escalation, or next-reference route | inspect failure-mode and adjacent-routing sections together |

## Failure Mode Table

**Decision supported.** This section helps decide which documentation-and-upgrade failures deserve standing mitigations. The seed table carries hygiene and traffic rows and omits how this discipline actually fails, stale model names delivered as current, upgrades stretched past the scope boundary, phase handling lost in long-running Responses flows, and MCP outages silently degrading answers.

**Recommended default and causal basis.** Check any failing session for its verification step first, then its scope boundary, matching repair cost to defect depth. The sources name each failure with its guard, the maintenance notes predict map drift, the scope boundaries forbid the stretch, the phase guidance flags the replay risk, the fallback rules govern outages.

**Operating conditions and assumptions.** Each row names its trigger, earliest observable signal, blast radius, containment, and correction. The table covers documentation-and-upgrade failures, while documentation-process failures stay with the seed rows.

**Failure boundary and alternatives.** Stale-answer failures surface downstream, usually in the user's broken build, which no in-session signal fully predicts. Bounded alternatives and recoveries: gate-driven prevention over detection, citation audits as cheap triage, or eval reruns to catch phase and behavior regressions.

**Counterexample, gotchas, and operational comparison.** The silent-outage failure masquerades as fluency, reference-quoted answers read identically to verified ones minus the citation. Good: a failing upgrade triaged at its compatibility record before touching prompts. Bad: patching prompts under a wrong viable verdict. Borderline: a valid recommendation with one stale launch-day item, repaired by the refresh list.

**Verification, evidence, and uncertainty.** Seed one failure per row in a review drill and confirm the named signal fires and maps to the right repair. The maintenance notes, scope boundaries, phase guidance, and fallback rules supply every added row. Failure frequencies in real sessions are unmeasured.

**Second-order consequence.** The failures sort by detectability, scope stretch is visible in the diff, phase loss in replay behavior, but staleness is invisible until an external event reveals it, so the cheapest guard is the citation habit rather than any detector.

**Revision decision.** Add stale-recommendation, scope-stretch, phase-loss, and silent-outage rows, each with its source-named signal, blast radius, and repair.

**Retained seed evidence.** All four seed failure rows with their triggers and mitigation actions remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| failure_mode_name | likely_trigger_condition | required_mitigation_action |
| --- | --- | --- |
| source drift hides truth | external or local guidance changes after the reference was written | refresh public evidence, rerun local corpus gate, and mark stale claims before reuse |
| generic advice escapes review | agent copies plausible best practices without theme-specific verification | block completion until the verification gate names concrete command, reviewer question, or metric |
| decision path remains implicit | reader cannot tell when to adopt, adapt, or avoid the pattern | add decision table, cost of being wrong, and adjacent-reference route |
| large corpus becomes list | many sources are indexed but not synthesized into ranked guidance | classify canonical, supporting, legacy, duplicate, and conflicting sources |

## Retry Backpressure Guidance

**Decision supported.** This section helps decide when a failing retrieval, install, or upgrade should be retried, escalated, or honestly surrendered. The seed bullets classify verification failures generically and never carry this theme's retry rules, the sources state exact retry ladders for empty retrievals, failed MCP installs, and under-complete model behavior.

**Recommended default and causal basis.** Climb each ladder in order, record what each rung tried, and never respond to a blocked verdict with scope expansion. The doctrine prescribes level-specific retries, two fallback strategies before declaring no results, escalated-permission retry before asking the user to install, and prompt-level fixes before raising reasoning effort.

**Operating conditions and assumptions.** The failing rung is identified from session evidence before the next retry is chosen. This governs retrying retrieval and upgrade work, kept alongside the seed's reference-verification retry rules as two labeled layers.

**Failure boundary and alternatives.** Retry ladders assume the failure is transient or steerable, a truly blocked upgrade must exit the ladder rather than climb it. Bounded alternatives and recoveries: escalation to the user when ladders exhaust, eval-driven retry selection, or deferring the request until the MCP layer recovers.

**Counterexample, gotchas, and operational comparison.** Raising reasoning effort feels like the natural first retry, yet the guide orders it last, after completeness contracts, verification loops, and persistence rules. Good: two query reformulations then a documented no-results report. Bad: five identical searches then a guessed answer. Borderline: a third fallback query after new keywords surfaced, legitimate because the input changed.

**Verification, evidence, and uncertainty.** Audit retry sequences for rung changes between attempts and check surrender reports name what was tried. The empty-result block, MCP install steps, and last-mile-knob rule prescribe the three ladders. How often each ladder resolves at its first rung is unmeasured.

**Second-order consequence.** All three ladders share one shape, cheap self-service retries first, escalation second, honest surrender third, and the doctrine treats the surrender step as a deliverable rather than a failure.

**Revision decision.** Add the theme's ladders, empty results get two fallback strategies then an honest report, MCP failures get self-install then escalated retry then a user ask, behavior regressions get prompt blocks before effort increases.

**Retained seed evidence.** All five retry and backpressure bullets, including the one-owner-per-file rule, remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- Retry only after the failed verification signal is classified as transient, stale evidence, missing context, or true contradiction.
- Use one bounded retry for stale external evidence refresh, then escalate to a human or a narrower source-specific reference.
- Apply backpressure by stopping new generation or implementation work when source coverage, critique coverage, or verification gates are red.
- For long-running agent workflows, checkpoint after each batch and re-read the current spec before any broad rewrite, commit, push, or destructive operation.
- For distributed execution, assign one owner per generated file or theme batch and require merge-time verification of exact path, heading, and evidence-boundary invariants.

## Observability Checklist

**Decision supported.** This section helps decide what evidence must exist that a session happened as claimed. The seed bullets recycle generic evidence records and never name this theme's evidence stream, the citation trail, the per-site verdict records, and the retry-ladder logs from failed retrievals.

**Recommended default and causal basis.** Record per session the request class, citations or staleness flags, verdict records, and ladder logs, keeping raw doc fetches out of the record. The artifact section defines the recommendation record and the gate section the verdicts, so observability means persisting citations, verdicts, and ladder outcomes for the feedback loop.

**Operating conditions and assumptions.** Sessions can persist small text records alongside their deliverables. This covers observing documentation-and-upgrade sessions, not the upgraded integrations' production behavior.

**Failure boundary and alternatives.** Full trails for trivial lookups outgrow their value, the null-instance convention applies. Bounded alternatives and recoveries: citation-only retention for lookup sessions, record-only retention for upgrades, or sampled retention at volume.

**Counterexample, gotchas, and operational comparison.** Verdicts recorded as a single outcome lose the failing checklist item the feedback metrics need. Good: a session record with two citations, one blocked verdict, and its failing item. Bad: a delivered answer with no source and no flag. Borderline: a null-instance record for a product-snapshot orientation question.

**Verification, evidence, and uncertainty.** Spot-check session records for citations, verdicts, and ladder logs. The seed's small-audit-evidence preference and the citation rules anchor the record contents. The retention horizon for session records is untuned.

**Second-order consequence.** The citation trail is self-documenting evidence, unlike prose it names its sources directly, so retaining it costs nothing beyond what the quality rules already required.

**Revision decision.** Recenter the checklist on session evidence, cited sources per answer, filled verdict records per upgrade, and what each retry rung tried before any surrender report.

**Retained seed evidence.** All six observability bullets including the small-audit-evidence preference remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- Record which local sources were loaded and which were intentionally skipped.
- Record the exact verification command, reviewer question, or rendered artifact used as proof.
- Record p50/p95/p99 latency or reviewer-time measurements when the reference affects runtime or workflow speed.
- Capture reviewer decision, unresolved uncertainty, and next refresh trigger.
- Record leading indicator and failure signal from this file in the coverage manifest or journal when the reference drives real work.
- Keep audit evidence small enough to review: command output summary, changed-file list, and unresolved-risk notes are preferred over raw transcript dumps.

## Performance Verification Method

**Decision supported.** This section helps decide how to prove the minimal-change discipline is buying the stability it claims. The seed method fixes handler latency numbers while this theme's performance question is doctrinal, does the minimal-change discipline produce upgrades that pass evals with less rework than broad rewrites.

**Recommended default and causal basis.** Track per upgraded site the class chosen, eval outcome, rework rounds, and prompt-size delta, reviewing the contrast quarterly. The doctrine claims lean interventions preserve behavior, a claim testable by comparing eval outcomes and rework rounds across upgrade classes.

**Operating conditions and assumptions.** Enough upgrades accumulate for the contrast to mean anything. This evaluates the discipline's efficiency claim, not model latency, keeping the seed's latency defaults as the absent-SLO fallback.

**Failure boundary and alternatives.** Class comparisons confound integration difficulty with method, hard integrations get bigger interventions and worse outcomes regardless. Bounded alternatives and recoveries: eval-only tracking, timed assessments against the workload model, or block-retention audits as the leanness proxy.

**Counterexample, gotchas, and operational comparison.** Rework rounds undercount silent failures, an upgrade that shipped with degraded behavior nobody evaled shows zero rework in this metric. Good: a contrast showing string-only upgrades passing evals with no rework. Bad: quoting the doctrine's benefit as measured when nothing was tracked. Borderline: adopting the claim unverified for one quarter while the record accumulates, noted as assumed.

**Verification, evidence, and uncertainty.** Publish the contrast with site counts and the eval-covered fraction. The validation plan and regression checklist state the efficiency claims the method tests. Effect size and the upgrade count needed for signal are unknown.

**Second-order consequence.** The highest-information comparison is the regression checklist's own question, is the new prompt leaner, not just longer, because prompt growth without eval improvement is the discipline failing measurably.

**Revision decision.** Measure eval pass rates and rework rounds per upgrade class, and re-baseline when the model line or guidance changes on launch day.

**Retained seed evidence.** The performance method line, both indicator lines, the measurement packet, and the pass and fail conditions remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Performance method: require the reader to find the correct next action in 10 minutes or less during review sampling.
Leading indicator to measure: a new reader can apply the reference without asking the author for hidden context.
Failure signal to watch: the reference is a literature dump instead of a guided explanation.
Required measurement packet: capture input size, source count, tool-call count, wall-clock time, p50/p95/p99 latency where runtime applies, and reviewer decision time where documentation applies.
Pass condition: the reference must let a reviewer identify the correct next action, verification gate, and stop condition without reading unrelated files.
Fail condition: the reference encourages implementation before the workload, reliability target, and failure-mode table are explicit.

## Scale Boundary Statement

**Decision supported.** This section helps decide at what scale single-integration discipline stops sufficing and what structure replaces it. The seed statement recites multi-system limits and misses this theme's scale walls, monorepos whose usage-site inventory outgrows one session, fleets of integrations upgrading together, and the launch-day event that invalidates in-flight recommendations at once.

**Recommended default and causal basis.** Assess single integrations fully, batch fleet work by shared prompt surface, and re-run the refresh items against every in-flight recommendation when guidance changes. The doctrine assumes one integration assessed by one agent against one guidance snapshot, and fleet upgrades and mid-flight guidance changes strain both assumptions.

**Operating conditions and assumptions.** Recommendation records are dated so a guidance change can identify which are stale. The boundaries bound this reference and its discipline, not OpenAI's platform scale.

**Failure boundary and alternatives.** Scaling advice beyond single-integration assessment is inference here, the sources address one upgrade at a time. Bounded alternatives and recoveries: a fleet-level inventory pass before any per-integration work, template-ownership records, or scheduled re-verification sweeps after major releases.

**Counterexample, gotchas, and operational comparison.** Shared templates couple integrations invisibly, one prompt edit for site A silently changes behavior at every site the template serves. Good: a fleet upgrade batched by template with one shared verdict per surface. Bad: fifty integrations swept in one undated pass. Borderline: two services sharing a template upgraded separately with the coupling noted.

**Verification, evidence, and uncertainty.** Track record completeness against inventory size and re-open rates after guidance refreshes to locate the wall empirically. The launch-day refresh items support the event-driven inference, marked as extension beyond the sources. The inventory size at which one session fails is unmeasured.

**Second-order consequence.** The natural scale response is the launch-day refresh list generalized, treat guidance changes as events that re-open every affected recommendation, which the sources already prescribe for the GPT-5.4 launch specifically.

**Revision decision.** Add scale signals, inventories that exceed a session's record capacity, shared prompt templates spanning many integrations, and guidance refreshes landing while recommendations are in flight.

**Retained seed evidence.** All four scale boundary statements including the distributed split and context-drift rules remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Openai Api Documentation Patterns stops being sufficient when the task spans multiple independent systems, more than one ownership boundary, unbounded source discovery, or production traffic without an explicit SLO.
Under distributed execution, split work by theme file and preserve one verification owner per split; do not let parallel agents rewrite the same reference without a merge checkpoint.
Under long-running agent workflows, treat context drift as a reliability failure: checkpoint state, summarize open risks, and verify against the spec before continuing.
Under large-codebase scale, require dependency or source-graph narrowing before applying this reference; a source list without ranked canonical guidance is not enough.

## Future Refresh Search Queries

**Decision supported.** This section helps decide which future searches would genuinely refresh this reference's external evidence. The seed query table drops the internal theme name into three templates whose literal phrasing targets a coinage no external author uses.

**Recommended default and causal basis.** Refresh through the MCP docs tools on a fast cadence for the model map and a slower one for upgrade doctrine. Useful refresh queries speak the ecosystem's vocabulary, OpenAI Responses API docs, GPT model deprecations, reasoning effort parameter, not this corpus's file-naming scheme.

**Operating conditions and assumptions.** Each query names its target section, source type, and firing trigger. The queries refresh external analogues for this theme, while the local skill changes only through repository edits.

**Failure boundary and alternatives.** Empty results from a coinage query logged as freshness confirmed convert search blindness into false confidence. Bounded alternatives and recoveries: subscribing to OpenAI changelog pages, restricted web search on the two official domains, or dated retrieval records as the refresh driver.

**Counterexample, gotchas, and operational comparison.** Model-name queries date fastest, a query phrased around GPT-5.4 becomes the stale artifact it was meant to catch. Good: an MCP fetch of the current models page feeding the model map. Bad: searching the literal theme title and logging zero hits as freshness. Borderline: a web search on platform.openai.com during an MCP outage, within the fallback rules.

**Verification, evidence, and uncertainty.** Run each query once, grade the top results for doctrinal substance, and rewrite phrasings that return mostly marketing noise. The seed's three-row structure targeting docs, repositories, and release notes is scaffolding, and the skill's tooling notes name the retrieval channel. Which phrasings surface substantive changes is unknowable in advance, so the queries need their own review cadence.

**Second-order consequence.** This theme's refresh mechanism is already installed doctrine, the skill's own MCP tools are the refresh channel, so the best query is not a web search but a docs-server session against the model and upgrade pages.

**Revision decision.** Rephrase toward ecosystem vocabulary, current OpenAI model lineup and deprecations, Responses API and phase handling changes, and MCP docs-server availability, each tied to the sections it would refresh.

**Retained seed evidence.** All three labeled query rows with their official-docs, repository, and release-notes targets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| search_query_label_name | search_query_text_value |
| --- | --- |
| `official_docs_query_phrase` | openai api documentation patterns official documentation best practices |
| `github_repository_query_phrase` | openai api documentation patterns GitHub repository examples |
| `release_notes_query_phrase` | openai api documentation patterns changelog release notes migration |

## Evidence Boundary Notes

**Decision supported.** This section helps decide how statements in this reference must be labeled so readers know what each claim rests on and how quickly it may expire. The seed notes define the three labels but ignore this file's specific hazards, archive-carried claims about a live-moving vendor surface and reference files that self-declare their own staleness.

**Recommended default and causal basis.** Label per claim, mark volatile facts as archive-dated with the docs-win caveat, and keep the three external URLs as unretrieved candidates. Downstream confidence calibrates on these labels, and a model ID quoted without the docs-win caveat overstates what the archive can promise.

**Operating conditions and assumptions.** Labels stay stable corpus-wide and every combined-inference clause names the inputs it merges. The notes govern labeling in this reference and its reuses, not source ranking, which the hierarchy owns.

**Failure boundary and alternatives.** Labels applied per section rather than per claim let one labeled sentence launder its unlabeled neighbors. Bounded alternatives and recoveries: an explicit volatile tag for model and version claims, inline labels parenthetically on key IDs, or claim-to-label indexing during verification.

**Counterexample, gotchas, and operational comparison.** Packet and prompt reuse strips labels mechanically, so volatile model IDs need their archive-dated context embedded in the same sentence. Good: the three upgrade classes cited as archive-local doctrine from the upgrade guide. Bad: quoting gpt-5.4 as the verified current default. Borderline: the fleet-scale advice carried as combined inference with its extension-beyond-source note.

**Verification, evidence, and uncertainty.** Sample load-bearing claims, confirm correct labels, and verify volatile claims carry the archive-dated qualifier. The three seed definitions match the corpus-wide label vocabulary and the files' self-deprecation clauses ground the volatility rule. Label durability through packet reuse and prompt quotation is unaudited, so leakage risk remains an assumption.

**Second-order consequence.** This theme needs a volatility qualifier inside the local label, a claim can be faithfully local and already false, since the corpus documents a vendor surface that moves faster than the archive.

**Revision decision.** Add rules marking every volatile claim, model IDs, upgrade steps, prompt-block semantics, as archive-dated rather than currently-verified, and the mismatched external rows as non-corroborating placeholders.

**Retained seed evidence.** All three label definitions, local fact, external fact, and combined inference, remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- `local_corpus_sourced_fact`: statements tied directly to the local source paths above.
- `external_research_sourced_fact`: statements tied to the public URLs above.
- `combined_evidence_inference_note`: synthesis that combines local and public evidence into agent guidance.
