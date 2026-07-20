# Image Generation Prompt Patterns

**Decision supported.** This section helps decide whether a visual request should be served by generated raster output at all and, if so, through which of the skill's two top-level modes. The seed title opens the theme without naming the source's governing split, a default built-in image_gen mode and an explicit-only CLI fallback whose controls must never leak into each other.

**Recommended default and causal basis.** Prompt through the shared labeled-spec schema and run the built-in image_gen tool, reserving the scripts/image_gen.py CLI for explicit user requests only. The local skill states the CLI may be used only when the user explicitly asks, so any guidance that blurs the mode boundary teaches agents to break the skill's first rule.

**Operating conditions and assumptions.** The request genuinely wants a bitmap asset, the built-in tool is available, and prompt inputs like exact text and constraints were collected up front. The patterns govern prompting and mode selection for raster image generation and do not govern vector asset editing or code-native visuals.

**Failure boundary and alternatives.** The two-mode framing does not apply when the task should not use image generation at all, such as extending an existing SVG icon system or building visuals in HTML/CSS. Bounded alternatives and recoveries: editing existing repo-native SVG or vector assets, building the visual directly in HTML/CSS or canvas, or declining generation when deterministic code-native output is wanted.

**Counterexample, gotchas, and operational comparison.** Agents silently switch to the CLI when the built-in tool fails, which the skill forbids, requiring instead that the fallback be offered and explicitly accepted. Good: built-in generation with a labeled spec and constraints. Bad: auto-falling back to the CLI after a tool error. Borderline: a raster mockup for a repo whose icons are all SVG, flagged before generating.

**Verification, evidence, and uncertainty.** Check that the transcript shows the built-in tool by default and an explicit user request preceding any scripts/image_gen.py invocation. The local SKILL.md defines exactly two top-level modes and rules that forbid automatic CLI switching and modification of the bundled script. How often built-in tool failures actually force the fallback conversation is unmeasured in this corpus, so escalation frequency stays unknown.

**Second-order consequence.** The skill treats mode choice as a permission question rather than a capability question, the CLI exists but consent, not convenience, gates it.

**Revision decision.** Open by stating the two top-level modes and the rule that fallback CLI mode is entered only on explicit user request, never automatically.

**Retained seed evidence.** The exact theme title and its framing as image generation prompt patterns remain unchanged. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

## Source Evidence Mapping Table

**Decision supported.** This section helps decide which recorded source may back which claim about image prompting and which files an agent may open in each mode. The seed map lists six local rows flatly although the skill itself partitions them, two files shared by both modes and three that must not be read outside the explicit CLI fallback.

**Recommended default and causal basis.** Keep all six local rows but mark mode scope per row and leave both external URLs labeled as unretrieved candidates. The SKILL.md reference map labels cli.md, image-api.md, and codex-network.md fallback-only, so a flat table invites loading mode-restricted material into default-mode prompting.

**Operating conditions and assumptions.** Rows resolve to real archive paths and the mode-scope labels mirror the SKILL.md reference map exactly. The table records provenance for this document's claims and does not restate the mode rules that make the partition matter.

**Failure boundary and alternatives.** The shared-versus-fallback partition says nothing about staleness, and codex-network.md warns about itself that its environment guidance may become stale. Bounded alternatives and recoveries: split the table into shared and fallback-only sub-tables, add line counts as staleness tripwires, or date external rows at first retrieval.

**Counterexample, gotchas, and operational comparison.** The OpenAI images guide URL looks authoritative enough to quote, but nothing in this corpus records its content ever being fetched. Good: citing prompting.md for structure rules in either mode. Bad: quoting image-api.md parameters as built-in tool arguments. Borderline: citing the codex repository URL for CLI context with the unretrieved label attached.

**Verification, evidence, and uncertainty.** Diff each mapped path against the SKILL.md reference map and confirm every external citation carries its candidate marker. The SKILL.md reference map assigns each of the five reference files an explicit shared or fallback-only role. Whether the two public URLs still describe current API behavior is unknown because neither was retrieved during this evolution.

**Second-order consequence.** The source corpus encodes access control in prose, a reference map that tells readers which files not to open is part of the skill's behavior contract.

**Revision decision.** Annotate each local row with its mode scope, shared for prompting.md and sample-prompts.md, fallback-only for cli.md, image-api.md, and codex-network.md.

**Retained seed evidence.** All eight source rows with their category, confidence, and synthesis-role columns remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| source_location_path_key | source_category_artifact_type | source_authority_confidence_level | source_usage_synthesis_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202603/.system/imagegen/SKILL.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/codex-skills-202603/.system/imagegen/references/cli.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/codex-skills-202603/.system/imagegen/references/codex-network.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/codex-skills-202603/.system/imagegen/references/image-api.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/codex-skills-202603/.system/imagegen/references/prompting.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/codex-skills-202603/.system/imagegen/references/sample-prompts.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| https://platform.openai.com/docs/guides/images | external_research_source_material | external_research_sourced_fact | primary image generation API documentation |
| https://github.com/openai/codex | external_research_source_material | external_research_sourced_fact | agent runtime and CLI reference point |

## Pattern Scoreboard Ranking Table

**Decision supported.** This section helps decide which prompting habits deserve default adoption when an agent writes or adapts an image prompt. The seed scoreboard scores 95, 91, and 88 for corpus hygiene and never ranks the source's own load-bearing patterns, labeled-spec prompting, invariant repetition on edits, and single-change iteration.

**Recommended default and causal basis.** Rank the shared labeled-spec schema first, invariant repetition for edits second, and deliberate single-change iteration third. Authors imitate what a scoreboard promotes, and a board silent on the shared prompt schema licenses free-text prompts the whole local corpus is built to prevent.

**Operating conditions and assumptions.** Each promoted row names the concrete output failure it prevents, such as edit drift or unwanted invented story elements. The scoreboard ranks prompting practices for this theme and does not rank image models or API parameters.

**Failure boundary and alternatives.** The numeric scores were never measured in this corpus, so quoting them as findings rather than emphasis fabricates rigor. Bounded alternatives and recoveries: order rows by the SKILL.md workflow step sequence, replace scores with a must-do flag, or keep a plain tier without numbers.

**Counterexample, gotchas, and operational comparison.** Specificity-policy violations masquerade as helpfulness, adding brands, characters, or slogans a generic prompt never implied. Good: a generic prompt normalized into the labeled spec before generation. Bad: rewriting the whole prompt on every retry. Borderline: keeping the seed's numeric scores with an editorial-only caveat.

**Verification, evidence, and uncertainty.** Trace each promoted row to the SKILL.md workflow step or prompting.md section that mandates it. Prompting.md's structure, invariants, and iterate-deliberately sections document each promoted practice explicitly. Which omitted practice causes the most real output failures is unmeasured, so ordering encodes expected cost.

**Second-order consequence.** The source's practices form a pipeline, spec the prompt, pin the invariants, then iterate narrowly, and dropping any stage reopens the failure the next stage assumes closed.

**Revision decision.** Promote labeled-spec prompting, edit-invariant repetition, and one-targeted-change iteration above the hygiene rows, marked editorial.

**Retained seed evidence.** All three scored rows with their tier labels and failure-prevention targets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| pattern_identifier_stable_key | pattern_score_numeric_value | pattern_tier_adoption_level | pattern_failure_prevention_target |
| --- | ---: | --- | --- |
| `image_generation_prompt_patterns` | 95 | default_adoption_pattern_tier | Source Map First: Load local image generation material before synthesizing prompt patterns recommendations. |
| `image_generation_prompt_patterns` | 91 | default_adoption_pattern_tier | Evidence Boundary Split: Separate local facts, external facts, and inference before giving agent instructions. |
| `image_generation_prompt_patterns` | 88 | default_adoption_pattern_tier | Verification Gate Coupling: Attach each recommendation to at least one command, checklist, or review gate. |

## Idiomatic Thesis Synthesis Statement

**Decision supported.** This section helps decide what single orienting claim should govern how agents turn user intent into image prompts. The seed thesis counts six local paths and repeats the load-local-first formula instead of the theme's central claim, that image prompts are structured specs whose specificity is set by the user, not the agent.

**Recommended default and causal basis.** Phrase the thesis as prompt equals labeled spec plus specificity discipline, with the three evidence labels kept on its clauses. The thesis is the sentence that survives quotation, and a retrieval slogan cannot stop an agent from padding a detailed user prompt with invented creative requirements.

**Operating conditions and assumptions.** The labels stay attached so local skill rules remain distinguishable from ecosystem inference when the thesis is reused. The thesis orients how this reference is used and does not restate the workflow the artifact and examples carry.

**Failure boundary and alternatives.** A spec-first thesis under-serves genuinely exploratory requests where the user wants variety before constraints. Bounded alternatives and recoveries: quote the SKILL.md specificity policy verbatim, split the thesis per evidence label, or phrase it as a pre-generation gate condition.

**Counterexample, gotchas, and operational comparison.** Paraphrases drop the do-not-add clause first, leaving a be-detailed platitude that licenses exactly the augmentation the source forbids. Good: citing the thesis to justify normalizing without expanding a detailed prompt. Bad: quoting it as public consensus on prompt engineering. Borderline: compressing it for a prompt while keeping the no-invention clause.

**Verification, evidence, and uncertainty.** Check the local clause against the SKILL.md prompt-augmentation section and confirm the combined clause carries the inference label. The SKILL.md specificity policy distinguishes normalizing detailed prompts from tastefully augmenting generic ones. Whether external prompt-engineering guides endorse the same no-invention boundary is unknown without retrieval.

**Second-order consequence.** The specificity policy is a conservation law, the agent may reshape the user's intent into structure but may not add creative mass to it.

**Revision decision.** Restate the combined inference as normalize specific prompts, augment generic ones tastefully, and never invent unimplied elements.

**Retained seed evidence.** The three labeled thesis lines with their local, external, and combined-inference structure remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`local_corpus_sourced_fact`: The local row for `image_generation_prompt_patterns` contains 6 source path(s), which should be treated as the first retrieval surface for this theme.
`external_research_sourced_fact`: The external source map provides public documentation, repository, or ecosystem analogues where available.
`combined_evidence_inference_note`: Reliable use of Image Generation Prompt Patterns comes from loading the local corpus first, checking public ecosystem guidance second, and converting both into verification-backed agent decisions.

## Local Corpus Source Map

**Decision supported.** This section helps decide which local file a specific image-generation question should open first. The seed map lists titles and truncated heading signals but not the division of labor, SKILL.md owns modes and workflow, prompting.md owns principles, sample-prompts.md owns recipes, and three files serve the CLI fallback only.

**Recommended default and causal basis.** Route what-mode and workflow questions to SKILL.md, how-to-phrase questions to prompting.md, and starting-recipe questions to sample-prompts.md. A reader with a concrete question needs to know which file answers it, and undifferentiated rows force reading six files to find one parameter.

**Operating conditions and assumptions.** All six files remain readable at the mapped archive paths and their headings still match the recorded signals. The map indexes the six local sources and does not summarize their content, which later sections synthesize.

**Failure boundary and alternatives.** Heading signals go stale if the archived skill is ever revised, and the map records no snapshot date. Bounded alternatives and recoveries: add a row for the bundled script, record per-file line counts as staleness tripwires, or fold the three fallback files into one logical row.

**Counterexample, gotchas, and operational comparison.** The bundled scripts/image_gen.py is referenced throughout but has no row here, so CLI implementation questions have no mapped destination. Good: opening image-api.md for input_fidelity semantics after the user chose CLI mode. Bad: skimming SKILL.md for mask flags it does not contain. Borderline: answering a size-options question from memory with cli.md cited for the path.

**Verification, evidence, and uncertainty.** Open each file at its mapped path and confirm the recorded heading signals appear in order. All six files were read in full during this evolution, 279, 160, 33, 49, 98, and 376 lines respectively. Whether a newer copy of this skill exists elsewhere in the repository was not established, so the archive's currency is unconfirmed.

**Second-order consequence.** The file layout mirrors the mode boundary, everything shared sits in two prompting files while everything dangerous to the default mode is quarantined in fallback docs.

**Revision decision.** Annotate each row with its question type, mode rules and workflow to SKILL.md, prompt principles to prompting.md, copy-paste specs to sample-prompts.md, CLI flags and API parameters and network setup to the three fallback files.

**Retained seed evidence.** All six local source rows with their titles, heading signals, and usage roles remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| local_source_filepath_value | local_source_title_text | local_source_heading_signals | local_source_usage_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202603/.system/imagegen/SKILL.md | "imagegen" | Image Generation Skill; Top-level modes and rules; When to use; When not to use; Decision tree; Workflow | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/codex-skills-202603/.system/imagegen/references/cli.md | CLI reference ('scripts/image_gen.py') | CLI reference ('scripts/image_gen.py'); What this CLI does; Quick start (works from any repo); Quick start; Guardrails; Defaults | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/codex-skills-202603/.system/imagegen/references/codex-network.md | Codex network approvals / sandbox notes | Codex network approvals / sandbox notes; Why am I asked to approve image generation calls?; Important note about approvals vs network; How do I reduce repeated approval prompts?; Safety note | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/codex-skills-202603/.system/imagegen/references/image-api.md | Image API quick reference | Image API quick reference; Scope; Endpoints; Core parameters for GPT Image models; Edit-specific parameters; Output | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/codex-skills-202603/.system/imagegen/references/prompting.md | Prompting best practices | Prompting best practices; Contents; Structure; Specificity policy; Allowed and disallowed augmentation; Composition and layout | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/codex-skills-202603/.system/imagegen/references/sample-prompts.md | Sample prompts (copy/paste) | Sample prompts (copy/paste); Generate; photorealistic-natural; product-mockup; ui-mockup; infographic-diagram | reference detail file for deeper pattern evidence |

## External Research Source Map

**Decision supported.** This section helps decide how much weight external rows may carry in image-prompting guidance. The seed map presents the OpenAI images guide and the Codex repository as external facts although neither was retrieved and neither is known to match the archived skill's parameter tables.

**Recommended default and causal basis.** Rest all current claims on the six local files and treat both URLs as leads for a dated refresh pass. An external-fact label promises documentary support, and an unretrieved URL can only supply a pointer, not evidence about current API behavior.

**Operating conditions and assumptions.** Each row keeps a role note explaining what question a future retrieval should answer. The map catalogs candidate external references for this theme and does not certify their content or freshness.

**Failure boundary and alternatives.** Dropping the rows entirely would hide the most likely refresh surface for a fast-moving image API. Bounded alternatives and recoveries: retrieve and date both URLs in a dedicated pass, add the platform release-notes page as a third candidate, or drop the table until retrieval happens.

**Counterexample, gotchas, and operational comparison.** Candidate rows quietly harden into citations when text is reused, unless the unretrieved marker sits inside the row itself. Good: citing the images guide as the place to verify parameter currency. Bad: claiming the guide endorses the local labeled-spec schema. Borderline: using the repository URL for CLI provenance as labeled inference.

**Verification, evidence, and uncertainty.** Confirm no claim in this document cites an external row as fact and that each row carries its unretrieved marker. No external retrieval was performed during this evolution, so the candidate labels reflect the actual evidence state. Whether either URL still documents the parameters the local corpus lists is entirely unknown.

**Second-order consequence.** This theme's local facts have short half-lives, model names like gpt-image-1.5 and size lists are exactly the claims a dated retrieval would either confirm or retire.

**Revision decision.** Downgrade both rows to unretrieved candidates and name what each would confirm, current API parameters from the guide and CLI runtime context from the repository.

**Retained seed evidence.** Both external rows with their names, roles, and boundary labels remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| external_source_url_value | external_source_name_text | external_source_usage_role | evidence_boundary_label_value |
| --- | --- | --- | --- |
| https://platform.openai.com/docs/guides/images | OpenAI image generation guide | primary image generation API documentation | external_research_sourced_fact |
| https://github.com/openai/codex | OpenAI Codex repository | agent runtime and CLI reference point | external_research_sourced_fact |

## Anti Pattern Registry Table

**Decision supported.** This section helps decide which recurring image-generation failures deserve standing detection rules. The seed registry lists three corpus-hygiene failures and omits the anti-patterns the source itself legislates against, silent CLI fallback, unimplied creative augmentation, forgotten edit invariants, and assets stranded at default save paths.

**Recommended default and causal basis.** Screen every generation or edit session against the registry before delivering the asset, treating any hit as a rework trigger. The SKILL.md writes explicit never-rules for these behaviors because they are the failures that actually ship, wrong-mode runs and drifting edits.

**Operating conditions and assumptions.** Each row pairs a failure with an observable signal a reviewer can check, like a project asset whose only path is under $CODEX_HOME. The registry names prompting and mode failures with detection signals and does not restate the full workflow.

**Failure boundary and alternatives.** An exhaustive import of every source rule would duplicate the skill instead of registering the highest-cost patterns. Bounded alternatives and recoveries: fold detection into the completeness checklist, keep a short top-four registry with links into the skill, or auto-grep final reports for save paths.

**Counterexample, gotchas, and operational comparison.** Invariant drift is cumulative, each iteration that omits the keep-Y-unchanged clause loses a little more of the original image. Good: catching a hero image left at $CODEX_HOME before the PR ships. Bad: an edit chain whose later prompts dropped all constraints. Borderline: mild composition augmentation on a generic prompt, allowed but recorded.

**Verification, evidence, and uncertainty.** Replay each registry row against the skill section that forbids it and confirm the detection signal is observable before delivery. The SKILL.md rules section forbids automatic CLI switching and its save-path policy forbids leaving project assets at default paths. Relative frequency of each anti-pattern in this team's practice is unmeasured, so row order encodes expected cost.

**Second-order consequence.** Most rows are omissions rather than actions, the failure is what the agent stopped repeating, invariants, constraints, save-path checks, which makes them invisible in any single prompt.

**Revision decision.** Add silent-cli-switch, unimplied-augmentation, dropped-edit-invariants, and codex-home-stranded-asset rows with the source's own detection cues.

**Retained seed evidence.** All three original registry rows with their causes, replacements, and detection methods remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| anti_pattern_failure_name | failure_cause_risk_reason | safer_default_replacement_pattern | detection_signal_review_method |
| --- | --- | --- | --- |
| context_free_summary_output | agent skips local corpus and produces generic advice | source_map_first_synthesis | verify every listed local path appears in the generated file |
| unsourced_recommendation_claims | guidance appears authoritative without source boundary | evidence_boundary_split_pattern | check for local, external, and inference labels |
| unverified_agent_instruction | recommendation cannot be checked by command or review gate | verification_gate_coupling | require concrete gate in generated reference |

## Verification Gate Command Set

**Decision supported.** This section helps decide which gates must pass before a generated or edited image is delivered or this reference's guidance is relied on. The seed gate names one repository verifier command while the source's real gates are visual and procedural, output inspection against the spec, text-verbatim checks, and the CLI's --dry-run payload preview.

**Recommended default and causal basis.** Run the corpus verifier for structure, --dry-run before live CLI calls, and a recorded inspection of subject, style, composition, text accuracy, and invariants. An image can pass every text lint and still fail its only meaningful test, looking wrong, so gates must include the inspect-and-validate step the workflow mandates.

**Operating conditions and assumptions.** Outputs are viewable for inspection and the original spec's constraints list is available to check against. The gate set defines what must pass before generated assets are trusted and does not implement the review itself.

**Failure boundary and alternatives.** Visual gates cannot be scripted into this corpus's verifier, so the section must distinguish automatable from judgment gates. Bounded alternatives and recoveries: a checklist-only gate for preview-only images, paired review for brand-sensitive assets, or automated text extraction where in-image copy is critical.

**Counterexample, gotchas, and operational comparison.** Green mechanical gates create false confidence precisely because the visual gate is the one that catches real failures. Good: a dry-run catching a bad output path before spending a live call. Bad: shipping an infographic without reading its rendered labels. Borderline: skipping inspection for a throwaway preview, noted as preview-only.

**Verification, evidence, and uncertainty.** Execute the listed commands on a sample request and confirm the inspection gate demands recorded findings rather than assertion. Cli.md documents --dry-run requiring no key or network, and the SKILL.md workflow step twelve mandates inspecting outputs against invariants. How to standardize visual inspection records as reviewable evidence is unresolved in the source.

**Second-order consequence.** The CLI's --dry-run is the theme's one true mechanical gate, it validates the request payload and output paths with no network, no key, and no cost.

**Revision decision.** Keep the repository verifier and add the source's checkable gates, --dry-run payload preview for CLI work, verbatim text comparison, and the subject-style-composition inspection pass.

**Retained seed evidence.** The original verification gate line and its repository verifier command block remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`verification_gate_command_set`: Run the repository verifier after editing this file.

```bash
python3 agents-used-monthly-archive/idiomatic-references-202606/tools/verify_reference_generation.py --stage final
```

## Agent Usage Decision Guide

**Decision supported.** This section helps decide when a working agent should open this reference and which classification path it should take. The seed guide says use this reference when the theme is mentioned, but the real trigger is an act, an agent is about to generate, edit, or batch raster assets and must first decide mode and intent.

**Recommended default and causal basis.** Open this reference before any raster generation, classify the request into the use-case taxonomy, then follow the decision tree for generate-versus-edit and single-versus-batch. Mode and intent decisions attach at request time, and a guide keyed to topic mentions fires too late or not at all.

**Operating conditions and assumptions.** The reader can see the user's input images and label each one's role before choosing the edit or generate path. The guide routes readers into this reference and does not decide augmentation depth, which the tradeoff guide owns.

**Failure boundary and alternatives.** Keying to every image mention would open this reference for tasks the skill itself excludes, like extending an SVG icon set. Bounded alternatives and recoveries: a pre-delivery-only trigger for teams that review in batches, embedding the trigger in an asset-request template, or a taxonomy-slug lookup shortcut for repeat users.

**Counterexample, gotchas, and operational comparison.** Agents assume every provided image is an edit target, while the source says reference-only images mean the request is generation with references. Good: labeling two user images as style references and choosing generate. Bad: running an edit on a mood-board image the user never asked to change. Borderline: a local file edit routed through view_image first to stay on the built-in path.

**Verification, evidence, and uncertainty.** Walk a generate, an edit, and a batch request through the guide and confirm each lands on a mode, an intent, and a taxonomy slug. The SKILL.md decision tree separates intent from execution strategy and defaults ambiguous requests to generation. Where exactly a reference-guided generation ends and an edit begins for heavily-referenced requests remains a judgment the source leaves open.

**Second-order consequence.** The source splits every request into two orthogonal questions, intent and execution strategy, and most misfires come from answering only one of them.

**Revision decision.** Trigger on generate, edit, and batch events, with the skill's decision tree resolving intent and its two-mode rule resolving execution.

**Retained seed evidence.** The original usage line and all four guidance bullets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`agent_usage_decision_guide`: Use this reference when a task mentions this theme, one of the listed local source paths, or a nearby technology/workflow surface.

- Start with the local corpus source map.
- Prefer patterns with explicit verification gates.
- Treat external sources as freshness and ecosystem checks, not replacements for local repo conventions.
- Preserve the evidence boundary labels when reusing recommendations.

## User Journey Scenario

**Decision supported.** This section helps decide what end-to-end shape a competent image-generation session should take. The seed scenario shows a creative builder choosing a reading path and stops before the journey the source scripts, classify, spec, generate, inspect, iterate with one change, then place the asset in the workspace.

**Recommended default and causal basis.** Narrate a landing-page hero request taken from vague intent to a taxonomy slug, a labeled spec, an inspected render, one targeted revision, and a workspace-committed file. A journey that ends at reading cannot rehearse the decisions that matter, which mode, which invariants, and when to stop iterating.

**Operating conditions and assumptions.** The reader can render images inline for inspection and can move files into the project workspace. The scenario dramatizes one representative generation journey and does not enumerate every asset-type path.

**Failure boundary and alternatives.** One linear journey cannot cover both generate and edit intents, whose invariant disciplines differ materially. Bounded alternatives and recoveries: a second journey for an invariant-locked edit, a failure journey where the built-in tool fails and the CLI is offered but declined, or the skill's own hero example cited directly.

**Counterexample, gotchas, and operational comparison.** Journeys written without a real inspection beat read as tidy fiction, real sessions loop on composition and text accuracy. Good: a journey ending with the final path, prompt, and mode reported. Bad: one ending at the first render. Borderline: a preview-only journey that legitimately leaves the file at the default path, labeled preview.

**Verification, evidence, and uncertainty.** Check each journey beat against the SKILL.md seventeen-step workflow and confirm no step is skipped. The SKILL.md workflow scripts exactly this journey from mode decision through final path reporting. Typical iteration counts before an asset is accepted are unrecorded in this corpus.

**Second-order consequence.** The journey's pivotal moment is the save-path decision, a beautiful render stranded at $CODEX_HOME is a failure the source treats as seriously as a bad image.

**Revision decision.** Extend the journey through a spec built from the labeled schema, a first render inspected against constraints, a single-change follow-up, and a final move into the workspace with the path reported.

**Retained seed evidence.** The role-based opening, starting state, decision, and trigger lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Role based opening scenario: The creative tool builder or artifact creator is starting from vague creative intent that needs constraints, iteration, and quality review and needs a reference that turns source evidence into an executable next step.
Primary user starting state: The user has a `image_generation_prompt_patterns` task, one or more local source paths, and uncertainty about which pattern should drive implementation.
Decision being made: choosing the prompt, controls, taste rubric, regeneration trigger, and final acceptance bar.
Reference opening trigger: Open this file when the task mentions image generation prompt patterns, any mapped local source path, or an adjacent workflow with the same failure mode.

## Decision Tradeoff Guide

**Decision supported.** This section helps decide how much prompting effort and constraint discipline a given image request deserves and what being wrong costs. The seed guide keys adopt, adapt, and avoid to generic evidence agreement instead of the variables the source uses, prompt specificity, intent type, and whether the asset is preview-only or project-bound.

**Recommended default and causal basis.** Match augmentation to specificity, match invariant discipline to intent, and match delivery rigor to whether the asset is project-bound. Augmentation depth is the real decision, and the source allocates it by how specific the user already was, not by evidence agreement.

**Operating conditions and assumptions.** The request's specificity and destination can be judged before prompting begins. The guide calibrates prompting effort per request and cannot waive the no-invention rule once a prompt is specific.

**Failure boundary and alternatives.** Specificity-keyed advice under-determines edits, where the binding variable is invariant preservation rather than augmentation. Bounded alternatives and recoveries: default everything to full-spec prompting when classification is doubtful, pilot with one render before committing to a batch, or let the user set the polish level explicitly.

**Counterexample, gotchas, and operational comparison.** Agents treat sample-prompts.md recipes as the default augmentation level, while the source says they are fully-authored examples, not a baseline. Good: normalizing a detailed product-shot prompt untouched. Bad: padding it with brand palettes the user never implied. Borderline: adding negative-space guidance to a generic hero request, allowed as practical layout help.

**Verification, evidence, and uncertainty.** Audit recent sessions for specificity-to-augmentation match and check over-augmented cases against user corrections. The SKILL.md specificity policy and prompting.md's allowed and disallowed augmentation lists define this allocation. Borderline specificity assignments remain judgment, and the source offers no tiebreak rule.

**Second-order consequence.** The source prices effort by reversibility, preview-only work tolerates loose prompting while project-bound and edit work demand full constraint discipline.

**Revision decision.** Rekey adopt to normalizing detailed prompts, adapt to tastefully augmenting generic ones, and avoid to declining generation when vector or code-native output fits better.

**Retained seed evidence.** The Adopt when, Adapt when, Avoid when, and Cost of being wrong rows with their verification prompts remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| decision_option_name | when_to_choose_condition | tradeoff_cost_description | verification_question_prompt |
| --- | --- | --- | --- |
| Adopt when | local corpus and external evidence agree on the image generation prompt patterns pattern | fastest path, but can copy stale local assumptions | Does the selected pattern appear in the canonical source and current external evidence? |
| Adapt when | local sources are strong but public ecosystem guidance has changed | preserves repo fit, but requires explicit inference notes | Did the reference label the local fact, external fact, and combined inference separately? |
| Avoid when | source evidence is thin, conflicting, or unrelated to the user journey | prevents false confidence, but may require deeper research | Is there a confidence warning or adjacent reference route? |
| Cost of being wrong | wrong image generation prompt patterns guidance can send an agent to the wrong files, tests, or abstraction | wasted implementation loop and weaker verification | Would a reviewer know what to undo and what to inspect next? |

## Local Corpus Hierarchy

**Decision supported.** This section helps decide which local file outranks which when image-generation guidance conflicts or overlaps. The seed hierarchy labels SKILL.md canonical and all five reference files uniformly supporting, hiding that two are shared prompting canon while three are mode-gated documents an agent may be forbidden to apply.

**Recommended default and causal basis.** Consult SKILL.md first for any mode or workflow question and gate the three fallback files behind an explicit CLI request. A flat supporting tier invites citing image-api.md parameters in built-in mode, exactly the boundary the source repeats in every fallback file's header.

**Operating conditions and assumptions.** The mode of the current session is known before fallback rows are consulted. The hierarchy ranks retrieval priority within this corpus and does not restate the mode rules that gate three of its rows.

**Failure boundary and alternatives.** Mode-gating is not a quality ranking, the fallback files are authoritative within their mode and demoting them would misdescribe that. Bounded alternatives and recoveries: split the table into shared and fallback sub-hierarchies, add a mode column to every row, or annotate rows with their self-declared scope lines.

**Counterexample, gotchas, and operational comparison.** Each fallback file opens by restricting its own use, and skimming past those headers is how their controls leak into default-mode guidance. Good: resolving a schema question from SKILL.md over a recipe's phrasing. Bad: citing cli.md defaults to describe built-in tool behavior. Borderline: reading codex-network.md for background while flagging its self-declared staleness warning.

**Verification, evidence, and uncertainty.** Confirm each fallback row's header restriction is quoted or reflected in its hierarchy entry. Cli.md, image-api.md, and codex-network.md each open by declaring themselves fallback-only documents. Whether the archived hierarchy matches any live copy of this skill elsewhere was not established.

**Second-order consequence.** This corpus's hierarchy is conditional rather than linear, a file's authority depends on which mode the session is in, not on how central it is.

**Revision decision.** Rank SKILL.md canonical, prompting.md and sample-prompts.md as shared supporting canon, and the three fallback files as mode-gated authorities applicable only after explicit CLI opt-in.

**Retained seed evidence.** The classification vocabulary line and all six hierarchy rows with reviewer questions remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Classification vocabulary includes canonical, supporting, legacy, duplicate, and conflicting source roles.

| local_source_filepath_value | corpus_hierarchy_role | heading_signal_to_convert | reviewer_question_to_answer |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202603/.system/imagegen/SKILL.md | canonical primary source | Image Generation Skill; Top-level modes and rules; When to use | What guidance, warning, or example should this source contribute to Image Generation Prompt Patterns? |
| agents-used-monthly-archive/codex-skills-202603/.system/imagegen/references/cli.md | supporting detail source | CLI reference ('scripts/image_gen.py'); What this CLI does; Quick start (works from any repo) | What guidance, warning, or example should this source contribute to Image Generation Prompt Patterns? |
| agents-used-monthly-archive/codex-skills-202603/.system/imagegen/references/codex-network.md | supporting detail source | Codex network approvals / sandbox notes; Why am I asked to approve image generation calls?; Important note about approvals vs network | What guidance, warning, or example should this source contribute to Image Generation Prompt Patterns? |
| agents-used-monthly-archive/codex-skills-202603/.system/imagegen/references/image-api.md | supporting detail source | Image API quick reference; Scope; Endpoints | What guidance, warning, or example should this source contribute to Image Generation Prompt Patterns? |
| agents-used-monthly-archive/codex-skills-202603/.system/imagegen/references/prompting.md | supporting detail source | Prompting best practices; Contents; Structure | What guidance, warning, or example should this source contribute to Image Generation Prompt Patterns? |
| agents-used-monthly-archive/codex-skills-202603/.system/imagegen/references/sample-prompts.md | supporting detail source | Sample prompts (copy/paste); Generate; photorealistic-natural | What guidance, warning, or example should this source contribute to Image Generation Prompt Patterns? |

## Theme Specific Artifact

**Decision supported.** This section helps decide what concrete evidence object must exist before this reference counts as operational. The seed artifact names a prompt contract with bad-prompt rewrite while the source's operational artifact is richer, a labeled spec instance with taxonomy slug, role-tagged input images, verbatim text, and an explicit constraints block.

**Recommended default and causal basis.** Carry the skill's own hero-image example, a product-mockup spec with composition, lighting, and constraints lines, as the reviewable instance. A spec built on the shared schema is reviewable line by line, since each labeled field either matches the user's intent or does not.

**Operating conditions and assumptions.** The spec names its use-case slug and distinguishes user-provided requirements from agent augmentation. The artifact certifies this reference is operational and does not require every historical asset to retro-produce specs.

**Failure boundary and alternatives.** A full labeled spec is overkill for quick preview renders the source explicitly allows to stay informal. Bounded alternatives and recoveries: point at sample-prompts.md recipes as reference instances, accept a two-line spec for preview work, or pair each spec with its final render for visual diffing.

**Counterexample, gotchas, and operational comparison.** Specs written after the render look identical to real ones, so provenance notes matter. Good: a spec whose constraints line survived every iteration. Bad: a bare one-line prompt for a project-bound hero. Borderline: a preview spec with only use case, request, and constraints, labeled preview.

**Verification, evidence, and uncertainty.** Check the artifact shows a taxonomy slug, labeled fields, and a workspace path for project-bound output. The SKILL.md shared prompt schema and its generation example define exactly this artifact shape. Whether spec quality correlates with fewer iterations is untested in this corpus.

**Second-order consequence.** The schema doubles as an audit trail, a reviewer can reconstruct what was asked, what was constrained, and what was forbidden without seeing the conversation.

**Revision decision.** Define the artifact as one completed labeled-spec instance, taxonomy slug, primary request, role-labeled inputs, verbatim text line, and constraints, paired with its accepted render path.

**Retained seed evidence.** The artifact definition line and the three artifact field rows with completion rules remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Theme specific artifact: prompt contract with bad-prompt rewrite and evaluation criteria.

| artifact_field_name | artifact_completion_rule | evidence_source_hint |
| --- | --- | --- |
| user_goal_statement | state the user's concrete goal before applying Image Generation Prompt Patterns | local corpus hierarchy plus critique findings |
| decision_boundary_rule | define the point where this reference should be used or avoided | decision tradeoff guide |
| verification_gate_rule | define the command, checklist, or review question that proves the artifact worked | verification gate command set |

## Worked Example Set

**Decision supported.** This section helps decide which prompting behaviors should be taught as exemplary, negligent, or conditionally acceptable. The seed examples restate generic load-canon verdicts and never show actual prompting conduct judged, a spec honored, an augmentation overreach, or an edit that lost its invariants.

**Recommended default and causal basis.** Grade every example by two questions, did augmentation respect the specificity policy and did every iteration restate its invariants. Authors calibrate on instances, and the source teaches through eight generate and eight edit recipes rather than abstract verdicts.

**Operating conditions and assumptions.** Each example names its use-case slug, its mode, and the delivery consequence. The examples grade prompting conduct, not the aesthetic quality of the resulting images.

**Failure boundary and alternatives.** Examples drawn only from generation transfer poorly to edits, whose failure mode is drift rather than invention. Bounded alternatives and recoveries: draw examples from this repository's actual asset history, add a fourth case for a silent CLI switch, or pair each verdict with its registry row.

**Counterexample, gotchas, and operational comparison.** Invariant loss is invisible in any single prompt and only shows across the iteration chain. Good: the mug-hero spec generated, inspected, and placed in the workspace. Bad: a background-replacement edit whose third iteration forgot keep-the-product-unchanged. Borderline: adding soft studio lighting to a generic product prompt, allowed and noted.

**Verification, evidence, and uncertainty.** Scan each verdict against the specificity policy and the invariants rules and confirm the graded behavior is observable in a transcript. The SKILL.md edit example and prompting.md's invariant rules anchor the recast verdicts. Which negligent pattern dominates real practice here is unmeasured, so the chosen cases reflect expected shapes.

**Second-order consequence.** The most instructive bad example is helpful-looking, an agent enriching a detailed prompt with unimplied polish, which the source classifies as a violation rather than a favor.

**Revision decision.** Recast good as a spec-driven generation with constraints intact, bad as an edit chain that dropped its invariants, and borderline as tasteful augmentation of a generic prompt.

**Retained seed evidence.** The good, bad, and borderline example lines with their original verdict framing remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Good example: Use Image Generation Prompt Patterns after loading the canonical source, confirming the external evidence boundary, and writing a verification gate before implementation.
Bad example: Use Image Generation Prompt Patterns as a generic tutorial while ignoring the mapped local paths, source hierarchy, and cost of being wrong.
Borderline case: Use Image Generation Prompt Patterns only after adding a confidence warning when local evidence is thin or conflicts with current ecosystem guidance.

## Outcome Metrics and Feedback Loops

**Decision supported.** This section helps decide which observable signals should trigger revising a prompt practice or this reference. The seed metrics watch whether iteration improves taste and never measure the theme's operational outcomes, iterations per accepted asset, constraint violations caught at inspection, and assets stranded at default save paths.

**Recommended default and causal basis.** Track per session the iteration count, each constraint violation found at inspection, and whether the final path landed in the workspace. This theme improves outcomes through disciplined specs and inspections, so its instruments must watch those, not just aesthetic progress.

**Operating conditions and assumptions.** Sessions record their specs and final paths somewhere queryable. The metrics gauge the prompting discipline this reference teaches, not the image model's intrinsic quality.

**Failure boundary and alternatives.** Operational metrics need session records to produce data, which makes them costlier than impressions and tempting to skip. Bounded alternatives and recoveries: sample audits of delivered assets instead of full coverage, reviewer-graded spec quality scores, or text-accuracy spot checks on label-bearing images.

**Counterexample, gotchas, and operational comparison.** Counting iterations rewards premature acceptance, a one-iteration session may just mean nobody inspected the text. Good: tightening the verbatim-text habit after two label typos ship. Bad: celebrating low iteration counts while nobody reads rendered text. Borderline: skipping audits in a period with no image work, noted.

**Verification, evidence, and uncertainty.** Audit recent deliveries for spec records and confirm each stranded-asset event produced a save-path correction. The seed's review-cadence line ties re-verification to edits, a loop the operational metrics extend. Healthy baselines for these rates are unmeasured, so first thresholds are provisional.

**Second-order consequence.** Rising iteration counts implicate the spec, not the model, since the source's remedy for weak output is a better-constrained prompt, not a retry storm.

**Revision decision.** Adopt iterations-per-accepted-asset, inspection-caught violations, and stranded-asset count as the primary signals.

**Retained seed evidence.** The leading indicator, failure signal, and review cadence lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Leading indicator: iteration improves the artifact against named taste criteria rather than random novelty.
Failure signal: the reference celebrates creativity without defining what good output looks like.
Review cadence: Re-run the verifier after every generated-reference edit and refresh external sources when public APIs, docs, or tooling releases change.

## Completeness Checklist

**Decision supported.** This section helps decide when this reference may be declared ready to hand to an agent. The seed checklist confirms generic sections exist and never checks the theme's own obligations, that both modes, the decision tree, the specificity policy, and the save-path rules are all represented.

**Recommended default and causal basis.** Tick structural items with citations, then verify mode, tree, specificity, and save-path coverage by grepping this document against the skill's rule lists. This document teaches a mode-gated workflow, so its readiness check must confirm the workflow survives intact, not just that prose sections exist.

**Operating conditions and assumptions.** Each added item names its target section and whether a script or human verifies it. The checklist gates this document's readiness, not the quality of assets later produced under it.

**Failure boundary and alternatives.** A reference that dropped the save-path policy would still pass the current checklist and teach a stranded-asset habit. Bounded alternatives and recoveries: generate coverage items mechanically from the SKILL.md rules list, deep-check two random items per review, or pair-review the artifact spec.

**Counterexample, gotchas, and operational comparison.** Coverage can pass while descriptions contradict the source, so coverage ticks and fidelity ticks stay separate. Good: a coverage tick citing the line stating fallback is explicit-only. Bad: all ticks green from a headings glance. Borderline: carrying forward last review's taxonomy tick with a staleness note.

**Verification, evidence, and uncertainty.** List the skill's modes, tree branches, and policies, then grep this document for each and record the misses. The seed's seven structural items map onto real sections here and anchor the added coverage layer. How much fidelity checking each item needs per revision depends on edit volume, so depth stays judgment.

**Second-order consequence.** A checklist for a mode-boundary document inherits the boundary's failure mode, silently letting fallback-only controls describe the default path.

**Revision decision.** Append items requiring both top-level modes documented, the generate-versus-edit tree represented, the specificity policy stated, and the save-path precedence present.

**Retained seed evidence.** All seven structural checklist items covering scenario, decision guide, hierarchy, artifact, examples, metrics, and routing remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- The role scenario names the user, starting state, decision, and trigger for Image Generation Prompt Patterns.
- The decision guide includes Adopt when, Adapt when, Avoid when, and Cost of being wrong.
- The local corpus hierarchy identifies canonical and supporting sources or gives a confidence warning.
- The theme specific artifact is concrete enough to review without reading every mapped source.
- The examples cover good, bad, and borderline usage.
- The metrics section names one leading indicator and one failure signal.
- The adjacent routing section points to a better reference when this one is not the right fit.

## Adjacent Reference Routing

**Decision supported.** This section helps decide when a question should leave this reference and which neighbor owns it. The seed routing splits the theme name into image, generation, and prompt keywords aimed at unnamed destinations instead of routing by question type to real corpus neighbors.

**Recommended default and causal basis.** Keep prompting, mode, and taxonomy questions here, send vision and media processing questions and campaign-state questions to their evolved neighbors. Readers leave this reference with distinct needs, media pipelines beyond raster prompting and long-session state management, and each need has an evolved neighbor in this corpus.

**Operating conditions and assumptions.** Each route names its trigger, a destination resolving to a real file, and what stays here. Routing redirects within this corpus and cannot authorize work in a destination's domain.

**Failure boundary and alternatives.** Keyword routes point at references that exist only as words, stranding the reader who follows them. Bounded alternatives and recoveries: consult the corpus index before adding routes, keep unresolved needs here with a gap note, or escalate genuine overlap to the user.

**Counterexample, gotchas, and operational comparison.** Media-processing questions masquerade as prompting questions, and over-eager routing scatters a reader who needed one recipe. Good: sending a video-frame-analysis question to the vision media reference. Bad: routing to the image adjacent reference, a keyword with no file. Borderline: answering a small batch-orchestration question inline with a route noted for depth.

**Verification, evidence, and uncertainty.** Resolve each named destination to an existing corpus file and walk one sample question through each trigger. The local vision media patterns file sits pending in this same queue and the journal schema reference was evolved earlier in this lane. The best split between answering inline and routing away depends on question depth, so borderline calls stay recorded judgment.

**Second-order consequence.** Batch generation is where this theme meets workflow management, a long generate-batch campaign needs journaling discipline this file does not teach.

**Revision decision.** Route local media pipeline questions to the local vision media patterns reference and long-session checkpoint questions to the tdd progress journal schema reference.

**Retained seed evidence.** The adjacency guidance line and the three keyword-derived route stubs remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Adjacent reference guidance: Use image, art, playground, or timeline references when the artifact type is specific.
Adjacent reference 1: consider the image adjacent reference when the current task pivots away from image generation prompt patterns.
Adjacent reference 2: consider the generation adjacent reference when the current task pivots away from image generation prompt patterns.
Adjacent reference 3: consider the prompt adjacent reference when the current task pivots away from image generation prompt patterns.

## Workload Model

**Decision supported.** This section helps decide how much generation work one request may consume before escalation or acceptance. The seed model caps work at ten source files and three delegated subtasks per run, while image workload is really bounded by assets per request, iterations per asset, and batch concurrency.

**Recommended default and causal basis.** Plan one labeled spec per asset, expect a small number of targeted iterations, and treat batch work as an explicit strategy decision, not an accident of retries. The costly unit here is a generation call, and a model blind to call counts cannot budget the thing that actually consumes time and spend.

**Operating conditions and assumptions.** Call costs are acknowledged and batch runs have a declared output directory and concurrency. The model bounds generation effort per request and does not bound the creative scope of the assets themselves.

**Failure boundary and alternatives.** Call-count budgets vary by asset stakes, a brand hero justifies iterations a placeholder never will. Bounded alternatives and recoveries: time-boxed sessions with explicit incompleteness notes, shared spec templates amortized across similar assets, or reviewer-set iteration budgets for costly assets.

**Counterexample, gotchas, and operational comparison.** The n parameter generates variants of one prompt while generate-batch runs many prompts, and conflating them wastes calls on the wrong axis. Good: a batch of eight game icons run once through a JSONL manifest. Bad: twelve full-prompt rewrites chasing one hero image. Borderline: three extra variants via n for a shortlist, labeled as variant exploration.

**Verification, evidence, and uncertainty.** Count calls and iterations in recorded sessions and test whether spec-first sessions accept assets in fewer iterations. Cli.md documents generate-batch's required --out-dir, default concurrency five, and the n-versus-batch distinction. Typical iteration distributions across asset types are unmeasured, so the small-number expectation is a defensible default.

**Second-order consequence.** The source builds backpressure into batch tooling itself, generate-batch defaults to concurrency five and requires an output directory, bounding both parallelism and file sprawl.

**Revision decision.** Rebound the model around one spec per asset, single-change iterations until acceptance, and batches run through per-asset built-in calls or explicit CLI generate-batch with bounded concurrency.

**Retained seed evidence.** The four workload dimensions with their boundary values and verification pressure points remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`combined_evidence_inference_note`: Treat Image Generation Prompt Patterns as a agent workflow operating reference, not as a prose summary.

| workload_dimension_name | workload_boundary_value | verification_pressure_point |
| --- | --- | --- |
| primary_usage_surface | agent planning, tool use, context loading, delegation, or skill/plugin execution where bad guidance compounds across long-running sessions | verify that the reference changes the next implementation or review action |
| bounded_capacity_model | one primary task, up to 10 source files, up to 3 delegated subtasks, and a written completion audit for every run | split the task or create a narrower reference when this boundary is exceeded |
| source_pressure_model | local heading signals include Image Generation Skill; Top-level modes and rules; When to use; When not to use; Decision tree; Workflow; CLI reference ('scripts/image_gen.py'); What | compare guidance against canonical local sources before following external examples |
| artifact_pressure_model | required artifact is prompt contract with bad-prompt rewrite and evaluation criteria | require the artifact before claiming the reference is operationally usable |

## Reliability Target

**Decision supported.** This section helps decide what measurable reliability this reference must demonstrate before its guidance is trusted. The seed table demands perfect boundary preservation and an 18-of-20 decision sample with no sampling procedure, and omits the theme's own reliability notions, verbatim text accuracy and invariant preservation across edits.

**Recommended default and causal basis.** Keep the four dimensions with methods attached and lead with verbatim-text checks and edit-invariant audits. The source defines success operationally, right subject, right style, exact text, invariants intact, and that definition is checkable where the seed's percentages are not.

**Operating conditions and assumptions.** Each target names its metric, sampling method, population, owner, and the corrective action a miss triggers. The targets judge this reference and the prompting discipline, not the image model's generation quality.

**Failure boundary and alternatives.** Quoting the unmeasured percentages as achieved performance manufactures rigor this corpus never earned. Bounded alternatives and recoveries: binary pass-fail delivery audits, pooled sampling across the corpus's media themes, or postmortems on every shipped defect instead of rates.

**Counterexample, gotchas, and operational comparison.** Invariant checks against only the latest iteration miss cumulative drift, so audits must compare against the original image. Good: three sampled infographics with every label matching its quoted text. Bad: reporting the 18-of-20 nobody sampled. Borderline: an edit audit against the previous iteration only, recorded with that caveat.

**Verification, evidence, and uncertainty.** Run one text-verbatim audit and one original-versus-final edit comparison per review cycle. Prompting.md's text-in-images rules and the workflow's validate step give the operational definitions the added targets measure. No baseline exists for any threshold here, so the first measured cycle defines what is achievable.

**Second-order consequence.** Text accuracy is this theme's cheapest objective check, rendered words either match the quoted string or they do not.

**Revision decision.** Add a text-verbatim target for label-bearing assets and an invariant-preservation target for edit chains, with every threshold marked unbaselined and owned.

**Retained seed evidence.** All four reliability rows with their threshold values and evidence-collection methods remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| reliability_target_name | measurable_threshold_value | evidence_collection_method |
| --- | --- | --- |
| source_boundary_preservation | 100 percent of recommendations keep local, external, and inference boundaries visible | review generated text for the three evidence labels before reuse |
| decision_accuracy_sample | at least 18 of 20 sampled uses route to the correct adopt, adapt, avoid, or adjacent-reference decision | sample downstream tasks and record reviewer verdicts |
| unsupported_claim_rate | zero unsupported production, security, latency, or reliability claims in final guidance | reject claims without source row, explicit inference note, or verification method |
| recovery_path_clarity | every avoid or failure case names the rollback, escalation, or next-reference route | inspect failure-mode and adjacent-routing sections together |

## Failure Mode Table

**Decision supported.** This section helps decide which failures in the image-generation fabric deserve standing mitigations. The seed table carries hygiene rows and omits how image work itself fails, edits drifting past their invariants, in-image text rendering wrong, assets stranded at default paths, and fallback controls assumed on the built-in tool.

**Recommended default and causal basis.** Detect drift by comparing against the original image, text errors by reading every rendered label, and stranded assets by grepping delivery reports for $CODEX_HOME paths. Triage during a bad delivery needs rows describing how generation decays, ranked by how silently each failure ships.

**Operating conditions and assumptions.** Each row names its trigger, earliest observable signal, blast radius, containment, and correction. The table covers generation-process failures, while failures of the consuming project belong to its own references.

**Failure boundary and alternatives.** Rows are worthless if their earliest signal fires only after the asset has shipped into the project. Bounded alternatives and recoveries: wire path checks into the delivery workflow, audit delivered assets on a sampled cadence, or require the constraints block in every review.

**Counterexample, gotchas, and operational comparison.** Mode-parameter confusion fails politely, a built-in call silently lacking the quality control the agent believed it set. Good: a pre-delivery read catching a misspelled infographic label. Bad: a PR referencing an image that exists only under $CODEX_HOME. Borderline: minor edit drift accepted for a preview asset, flagged as preview-only.

**Verification, evidence, and uncertainty.** Seed one failure per row in a drill and confirm the named signal fires before a simulated delivery would ship the defect. The SKILL.md save-path policy and the fallback files' boundary warnings document these failures explicitly. Observed frequency of each failure in this team's history is unmeasured, so ordering encodes expected silence.

**Second-order consequence.** Every one of these failures is invisible in the prompt and visible only in the output or the filesystem, which is exactly why the workflow ends with inspection and path reporting.

**Revision decision.** Add invariant-drift, text-mismatch, stranded-asset, and mode-parameter-confusion rows with pre-delivery detection signals.

**Retained seed evidence.** All four seed failure rows with their triggers and mitigation actions remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| failure_mode_name | likely_trigger_condition | required_mitigation_action |
| --- | --- | --- |
| source drift hides truth | external or local guidance changes after the reference was written | refresh public evidence, rerun local corpus gate, and mark stale claims before reuse |
| generic advice escapes review | agent copies plausible best practices without theme-specific verification | block completion until the verification gate names concrete command, reviewer question, or metric |
| context window loses plan | long-running session forgets early constraints or overwrites user intent | write checkpoint summaries and re-read plan before each destructive step |
| tool fanout outruns budget | parallel actions create conflicts, duplicate work, or unbounded external calls | cap fanout, assign ownership, and require merge/audit checkpoints |

## Retry Backpressure Guidance

**Decision supported.** This section helps decide when a failing generation cycle should be retried, redesigned, or escalated. The seed bullets classify verification failures generically and never define this theme's retry semantics, what to change when a render misses, when to stop iterating, and how batch retries are bounded.

**Recommended default and causal basis.** Iterate with a single targeted change while re-specifying critical constraints, and escalate to spec redesign when repeated retries chase the same defect. An unguided retry loop rewrites the whole prompt each time, destroying the attribution that tells you which change fixed what.

**Operating conditions and assumptions.** Iteration outcomes are recorded per attempt so stalls are detectable rather than felt. This governs retries of generation attempts, not retries of the network layer, which the fallback CLI's max-attempts flag handles.

**Failure boundary and alternatives.** Single-change iteration is slow for exploratory work where the user wants divergent options rather than convergence. Bounded alternatives and recoveries: escalate to the user after a fixed attempt budget, switch taxonomy slugs when the framing itself misfires, or use n variants to explore before converging.

**Counterexample, gotchas, and operational comparison.** The tempting failure is loosening constraints until something passes, which converts a spec miss into a silent scope change. Good: one lighting fix per attempt with constraints restated each time. Bad: three full rewrites chasing a composition miss. Borderline: one exploratory variant round before converging, labeled exploration.

**Verification, evidence, and uncertainty.** Audit stalled sessions for whether retries were single-change and whether constraints survived every attempt. Prompting.md's iterate-deliberately section and cli.md's max-attempts and fail-fast flags define the two retry layers. How many single-change iterations typically precede acceptance is unmeasured, so attempt budgets stay judgment.

**Second-order consequence.** The source's retry unit is a delta, not a do-over, each follow-up changes exactly one thing so failure attribution survives the loop.

**Revision decision.** Add iteration semantics, one targeted change per retry with invariants restated, and batch semantics, bounded concurrency with per-job failure isolation.

**Retained seed evidence.** All five retry and backpressure bullets, including the one-owner-per-file rule, remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- Retry only after the failed verification signal is classified as transient, stale evidence, missing context, or true contradiction.
- Use one bounded retry for stale external evidence refresh, then escalate to a human or a narrower source-specific reference.
- Apply backpressure by stopping new generation or implementation work when source coverage, critique coverage, or verification gates are red.
- For long-running agent workflows, checkpoint after each batch and re-read the current spec before any broad rewrite, commit, push, or destructive operation.
- For distributed execution, assign one owner per generated file or theme batch and require merge-time verification of exact path, heading, and evidence-boundary invariants.

## Observability Checklist

**Decision supported.** This section helps decide what evidence must exist that a generation session happened as claimed. The seed bullets recycle source-loading and latency records and never name this theme's evidence stream, the final spec, the mode used, input-image roles, iteration deltas, and the final saved path.

**Recommended default and causal basis.** Record per session the spec, the mode, each input image's role, what each iteration changed, and where the final file landed. The SKILL.md's last workflow step mandates reporting the final path, the final prompt, and the mode, making session records the theme's native telemetry.

**Operating conditions and assumptions.** Sessions can persist small text records alongside delivered assets. This covers observing generation sessions, while the assets' runtime behavior is observed by the consuming project.

**Failure boundary and alternatives.** Full render retention for every iteration can outgrow the project, so retention needs selection rules. Bounded alternatives and recoveries: retain only final specs plus paths instead of full iteration chains, sample-audit recorded sessions, or accept commit history as a secondary trace.

**Counterexample, gotchas, and operational comparison.** Paraphrased specs drift from what was actually sent, so the recorded spec must be the literal final prompt. Good: a delivery note with spec, mode, and workspace path. Bad: an asset in the repo with no recorded prompt. Borderline: iteration notes summarized after acceptance with the final spec kept verbatim.

**Verification, evidence, and uncertainty.** Spot-check delivered assets for accompanying spec records and confirm each records mode and final path. SKILL.md workflow step seventeen mandates reporting saved path, final prompt, and mode for every workspace-bound asset. The retention horizon for iteration-level records is untuned, so the keep-final-spec rule is provisional.

**Second-order consequence.** The mandated final report is a one-line provenance record, everything needed to regenerate or audit the asset months later.

**Revision decision.** Recenter the checklist on session evidence, final spec text, mode and intent, image-role labels, per-iteration change notes, and the delivered path.

**Retained seed evidence.** All six observability bullets including the small-audit-evidence preference remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- Record which local sources were loaded and which were intentionally skipped.
- Record the exact verification command, reviewer question, or rendered artifact used as proof.
- Record p50/p95/p99 latency or reviewer-time measurements when the reference affects runtime or workflow speed.
- Capture tool-call count, context files loaded, delegated tasks, retry count, and completion-audit outcome.
- Record leading indicator and failure signal from this file in the coverage manifest or journal when the reference drives real work.
- Keep audit evidence small enough to review: command output summary, changed-file list, and unresolved-risk notes are preferred over raw transcript dumps.

## Performance Verification Method

**Decision supported.** This section helps decide how to prove prompting discipline is buying more than it costs. The seed method demands tool-call budgets and reader-time packets, while this theme's performance is calls and iterations per accepted asset, batch throughput under bounded concurrency, and latency driven by size and quality choices.

**Recommended default and causal basis.** Log per asset the call count, chosen size and quality, iteration count, and wall-clock time, publishing ratios with their sample sizes. Generation cost scales with the size and quality parameters the source documents, so verification must attribute spend to those choices rather than to generic tool counts.

**Operating conditions and assumptions.** Session records include per-call parameters and batches record their concurrency and job counts. This evaluates the prompting discipline's cost and benefit, not the image model's pricing itself.

**Failure boundary and alternatives.** Cost comparisons need enough recorded sessions to average over, making early ratios unstable. Bounded alternatives and recoveries: compare spec-first against free-text sessions on iteration counts, use reviewer judgment as interim evidence, or track only call counts at first.

**Counterexample, gotchas, and operational comparison.** Iterations-per-asset is inflatable by premature acceptance, so the count needs the inspection record alongside it. Good: a report showing spec-first sessions accepting in two iterations at auto quality. Bad: quoting reader-minutes for a generation workflow. Borderline: an early ratio published with a sample-of-one caveat.

**Verification, evidence, and uncertainty.** Collect call and iteration counts across several sessions and publish the ratio with its sample size. Image-api.md states that large sizes and high quality increase latency and cost, and high input fidelity increases token usage. Actual per-call cost figures are absent from the local corpus, so spend claims stay parameter-relative.

**Second-order consequence.** The API's own docs make cost a prompt-level decision, large sizes and high quality increase latency and cost, so the spec is also the budget.

**Revision decision.** Measure calls and iterations per accepted asset, record size and quality per call, and time batch runs against their concurrency setting.

**Retained seed evidence.** The performance method line, both indicator lines, the measurement packet, and the pass and fail conditions remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Performance method: require tool-call budgets, timeout budgets, and a resumable journal when the workflow exceeds one focused session.
Leading indicator to measure: iteration improves the artifact against named taste criteria rather than random novelty.
Failure signal to watch: the reference celebrates creativity without defining what good output looks like.
Required measurement packet: capture input size, source count, tool-call count, wall-clock time, p50/p95/p99 latency where runtime applies, and reviewer decision time where documentation applies.
Pass condition: the reference must let a reviewer identify the correct next action, verification gate, and stop condition without reading unrelated files.
Fail condition: the reference encourages implementation before the workload, reliability target, and failure-mode table are explicit.

## Scale Boundary Statement

**Decision supported.** This section helps decide at what scale ad-hoc prompting stops sufficing and what structure replaces it. The seed statement recites multi-system and SLO limits and misses this theme's scale walls, batch jobs beyond ad-hoc prompting, asset libraries needing consistent style across many sessions, and model churn retiring parameter facts.

**Recommended default and causal basis.** Prompt individually while asset counts are small, switch to manifest-driven batches with shared templates as libraries grow, and re-check model-specific facts after upgrades. Prompting patterns scale by templating, and past some asset count the unit of work becomes the JSONL manifest and the shared spec template, not the individual prompt.

**Operating conditions and assumptions.** Batch outputs land under a declared directory and templates version alongside the assets they produce. The boundaries bound the prompting discipline, not the number of assets a team may produce.

**Failure boundary and alternatives.** Template discipline is overhead for one-off assets where a single labeled spec suffices. Bounded alternatives and recoveries: rolling re-verification quotas per review period, per-asset-type template libraries, or freezing rarely used templates with staleness banners.

**Counterexample, gotchas, and operational comparison.** Model upgrades silently retire parameter facts, the corpus's gpt-image-1.5 fidelity notes are model-specific and dated. Good: a forty-icon set run as one manifest with a shared template. Bad: forty hand-typed prompts drifting in style. Borderline: eight assets prompted individually against one written template, template noted.

**Verification, evidence, and uncertainty.** Measure style consistency across batch outputs and confirm parameter claims are re-checked after each model release. Cli.md documents JSONL per-job overrides and image-api.md ties input-fidelity behavior to specific model versions. The asset count where manifests beat individual prompting is unmeasured, so the boundary stays a monitored judgment.

**Second-order consequence.** The CLI already encodes the scale transition, per-job overrides in JSONL are spec templating industrialized, one schema stamped across many jobs.

**Revision decision.** Add batch-scale signals, JSONL manifests with per-job overrides once asset counts grow, shared spec templates for style consistency, and parameter re-verification after model releases.

**Retained seed evidence.** All four scale boundary statements including the distributed split and context-drift rules remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Image Generation Prompt Patterns stops being sufficient when the task spans multiple independent systems, more than one ownership boundary, unbounded source discovery, or production traffic without an explicit SLO.
Under distributed execution, split work by theme file and preserve one verification owner per split; do not let parallel agents rewrite the same reference without a merge checkpoint.
Under long-running agent workflows, treat context drift as a reliability failure: checkpoint state, summarize open risks, and verify against the spec before continuing.
Under large-codebase scale, require dependency or source-graph narrowing before applying this reference; a source list without ranked canonical guidance is not enough.

## Future Refresh Search Queries

**Decision supported.** This section helps decide which future searches would genuinely refresh this reference's external evidence. The seed query table drops the internal theme name into three templates whose literal phrasing targets a coinage no external author uses.

**Recommended default and causal basis.** Search for image API parameter changes and image-model release notes on a periodic trigger, feeding the external map and the parameter-bearing sections. Useful refresh queries speak the ecosystem's vocabulary, image API parameter docs, GPT image model releases, prompt-structure guides, not this corpus's file-naming scheme.

**Operating conditions and assumptions.** Each query names its target section, source type, and firing trigger. The queries refresh external analogues for this theme, while the local skill changes only through repository edits.

**Failure boundary and alternatives.** Empty results from a coinage query logged as freshness confirmed convert search blindness into false confidence. Bounded alternatives and recoveries: follow the platform changelog directly, track the codex repository's releases, or drive refresh from dated retrieval records.

**Counterexample, gotchas, and operational comparison.** Image-generation search results skew toward marketing and gallery content, so result screening matters more here than in framework themes. Good: a query on gpt-image model parameter changes feeding the API-facts sections. Bad: searching the literal theme title and logging zero hits as freshness. Borderline: adopting a well-argued practitioner guide with an inference label pending corroboration.

**Verification, evidence, and uncertainty.** Run each query once, grade the top results for on-topic value, and rewrite phrasings that return mostly noise. The seed's three-row structure targeting docs, repositories, and release notes is sound scaffolding for the revised vocabulary. Which phrasings will track this vocabulary is unknowable in advance, so the queries need their own review cadence.

**Second-order consequence.** This theme's most perishable facts are enumerable, model names, size lists, and fidelity behaviors, which makes refresh queries unusually targetable.

**Revision decision.** Rephrase toward ecosystem vocabulary, OpenAI image API parameters, gpt-image model release notes, and image prompt structure best practices, each tied to the section it refreshes.

**Retained seed evidence.** All three labeled query rows with their official-docs, repository, and release-notes targets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| search_query_label_name | search_query_text_value |
| --- | --- |
| `official_docs_query_phrase` | image generation prompt patterns official documentation best practices |
| `github_repository_query_phrase` | image generation prompt patterns GitHub repository examples |
| `release_notes_query_phrase` | image generation prompt patterns changelog release notes migration |

## Evidence Boundary Notes

**Decision supported.** This section helps decide how statements in this reference must be labeled so readers know what each claim rests on and where it applies. The seed notes define the three labels but ignore this file's specific hazards, mode-gated local facts that are true only in the CLI fallback and model-version facts that expire silently.

**Recommended default and causal basis.** Label per claim, attach mode scope to fallback-derived facts, and mark both external URLs as unretrieved candidates. Downstream confidence calibrates on these labels, and a fallback-only fact quoted without its mode scope misleads exactly the default-mode reader most likely to reuse it.

**Operating conditions and assumptions.** Labels stay stable corpus-wide and every combined-inference clause names the local and external inputs it merges. The notes govern labeling in this reference and its reuses, not the ranking of sources, which the hierarchy owns.

**Failure boundary and alternatives.** Labels applied per section rather than per claim let one labeled sentence launder its unlabeled neighbors. Bounded alternatives and recoveries: introduce an explicit mode-scope tag, inline labels parenthetically on key claims, or index claims to labels during verification.

**Counterexample, gotchas, and operational comparison.** Packet and prompt reuse strips labels mechanically, so load-bearing claims need labels embedded in their own sentences. Good: the quality-flag fact cited as local fact scoped to CLI fallback. Bad: presenting gpt-image-1.5 defaults as timeless truths. Borderline: the built-in save-path default quoted with a version-of-the-archive date attached.

**Verification, evidence, and uncertainty.** Sample load-bearing claims, confirm correct labels, and verify no fallback-only fact appears without its mode scope. The three seed definitions match the corpus-wide label vocabulary and the boundary-preservation target elsewhere in this file. Label durability through packet reuse and prompt quotation is unaudited, so leakage risk remains an assumption.

**Second-order consequence.** This corpus needs a fourth dimension beyond the three labels, validity scope, because a claim can be locally sourced, true, and still wrong in the mode where it gets quoted.

**Revision decision.** Add rules scoping fallback-only facts to their mode and dating model-specific facts, with URL-derived material marked inference pending retrieval.

**Retained seed evidence.** All three label definitions, local fact, external fact, and combined inference, remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- `local_corpus_sourced_fact`: statements tied directly to the local source paths above.
- `external_research_sourced_fact`: statements tied to the public URLs above.
- `combined_evidence_inference_note`: synthesis that combines local and public evidence into agent guidance.
