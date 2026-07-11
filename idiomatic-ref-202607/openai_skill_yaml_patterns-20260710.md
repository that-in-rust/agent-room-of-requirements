# Openai Skill Yaml Patterns

**Decision supported.** This section helps decide whether and how to add an `agents/openai.yaml` file that exposes a skill's interface metadata, MCP dependencies, and implicit-invocation policy without moving behavioral instructions into the wrong layer. The seed title names a YAML theme but does not distinguish the machine-read `agents/openai.yaml` product configuration from a skill's agent-facing instructions or repository-wide AGENTS.md guidance.

**Recommended default and causal basis.** Treat `agents/openai.yaml` as optional product metadata, keep behavioral procedure in SKILL.md, add only fields the harness needs, quote every string value, keep keys unquoted, use relative asset paths, mention the exact `$skill-name` in the default prompt, and validate dependency and policy semantics. Separating machine configuration from model instructions prevents silent metadata drift, avoids bloating agent context, and keeps activation behavior reviewable.

**Operating conditions and assumptions.** The skill already has a stable name and purpose, UI metadata is useful, dependency requirements are known, assets exist, and the target product consumes this configuration. Use this reference only for OpenAI product-specific skill metadata in `agents/openai.yaml`, not general YAML or agent instruction authoring.

**Failure boundary and alternatives.** The task is really about writing SKILL.md, AGENTS.md, plugin manifests, or arbitrary YAML; the product contract is unknown; or optional metadata is added with no consumer or verification. Bounded alternatives and recoveries: omit `openai.yaml`, keep only SKILL.md frontmatter, use another product-specific file in `agents/`, route repository instructions to AGENTS.md, or defer version-sensitive fields until the harness contract is inspected.

**Counterexample, gotchas, and operational comparison.** Putting agent instructions in machine metadata, unquoted strings, quoted keys, wrong relative paths, a default prompt that omits `$skill-name`, unsupported dependency types, accidental implicit activation, and assuming optional fields are mandatory. Good: add a short display name, 25-64 character description, valid asset path, one-sentence prompt naming `$my-skill`, and an intentional policy flag. Bad: paste the skill body into YAML. Borderline: omit icons and dependencies when the skill has none rather than inventing placeholders.

**Verification, evidence, and uncertainty.** Parse the YAML structurally, inspect top-level and nested keys, check quoted scalar style where required, resolve asset paths, count the short description, verify `$skill-name` mention, validate MCP dependency fields, and exercise explicit plus implicit activation behavior when the harness is available. The fully read local source directly defines the file's machine-facing purpose, complete example, supported field meanings, string and key style, prompt requirement, MCP-only dependency type, and implicit-invocation default. The public Codex sources were not refreshed and no target harness or skill directory was supplied, so current parser strictness and optional-field support remain conditional.

**Second-order consequence.** `openai.yaml` is an activation and presentation boundary, not a second prompt; keeping it small reduces configuration authority and makes changes easier to audit.

**Revision decision.** Add a layer-separation contract, minimal-field default, field-specific validation, omission rules, and explicit activation tests.

**Retained seed evidence.** The exact title and all mapped source rows remain unchanged as the evidence inventory. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

## Source Evidence Mapping Table

**Decision supported.** This section helps decide which source owns a claim about `openai.yaml`, repository instructions, implementation behavior, or icon assets and how uninspected public links should be labeled. The seed maps one local field contract and three public resources but does not state which YAML claims each source can support or that the image guide is relevant only to asset production rather than schema semantics.

**Recommended default and causal basis.** Use the local `openai_yaml.md` file for field names and constraints, the AGENTS.md guide only for repository instruction boundaries, the Codex repository for future implementation corroboration, and the image guide only when producing bitmap assets; keep all public rows unrefreshed until inspected. Narrow source ownership prevents a related OpenAI page from being stretched into authority over a distinct configuration contract.

**Operating conditions and assumptions.** Each recommendation names one claim, one source role, a target-directory observation, and a parser or behavior check. Use this map to route evidence, not to certify current OpenAI behavior from retained links alone.

**Failure boundary and alternatives.** The AGENTS.md guide is used as `openai.yaml` schema proof, repository code is cited without version inspection, image API guidance determines SVG path rules, or the local archive is treated as current product behavior. Bounded alternatives and recoveries: inspect the current harness source, locate a repository-local schema or examples, omit uncertain fields, preserve a provisional inference, or route asset generation separately.

**Counterexample, gotchas, and operational comparison.** Source laundering, link existence presented as freshness, circular generated-reference citations, conflating icon production with icon path validation, and ignoring local skill naming. Good: cite the local source for `allow_implicit_invocation` semantics and test the target harness. Bad: cite image-generation docs for the dependency schema. Borderline: use repository examples as corroboration only after matching the installed version.

**Verification, evidence, and uncertainty.** Record claim, source row, evidence label, inspected heading or commit, version or date, target applicability, contrary evidence, parser result, behavior observation, and unresolved uncertainty. The local source was read completely and directly owns the exact field contract; the three public rows remain useful routing surfaces. None of the external sources was browsed, so present contents and current compatibility are unknown.

**Second-order consequence.** The source map should prevent authority bleed between metadata schema, repository instructions, runtime implementation, and asset generation.

**Revision decision.** Add claim-to-source ownership, disallowed joins, freshness state, and target-harness corroboration.

**Retained seed evidence.** All four original paths, categories, labels, and synthesis roles remain verbatim. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| source_location_path_key | source_category_artifact_type | source_authority_confidence_level | source_usage_synthesis_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202603/.system/skill-creator/references/openai_yaml.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| https://developers.openai.com/codex/guides/agents-md | external_research_source_material | external_research_sourced_fact | primary Codex custom instruction documentation |
| https://github.com/openai/codex | external_research_source_material | external_research_sourced_fact | GitHub implementation and project conventions |
| https://platform.openai.com/docs/guides/images | external_research_source_material | external_research_sourced_fact | primary image generation API documentation |

## Pattern Scoreboard Ranking Table

**Decision supported.** This section helps decide how to prioritize the three retained controls while authoring or reviewing a small product-specific YAML file. The seed ranks source-first, evidence separation, and verification coupling at 95, 91, and 88 without a scoring method or an explanation of their dependency order.

**Recommended default and causal basis.** Treat the rows as a required sequence rather than calibrated scores: read the field contract, keep local fact and current-product inference separate, then parse and behavior-test the resulting configuration. Verification cannot rescue a field invented from the wrong source, and accurate field names still fail when paths, prompts, or invocation behavior are not exercised.

**Operating conditions and assumptions.** The target skill and consumer are known, each field has source support, and structural plus behavioral checks are available. Use the order inside this reference and do not compare its numbers with unrelated pattern scores.

**Failure boundary and alternatives.** Numbers are read as probabilities, the lower-ranked verification gate is skipped, metadata is copied from an unrelated product, or a parser check is promoted into activation proof. Bounded alternatives and recoveries: apply a hard stop for unsupported keys, omit optional metadata, prioritize accidental implicit invocation as a safety risk, or keep a field provisional pending harness inspection.

**Counterexample, gotchas, and operational comparison.** False precision, checkbox implementation, source labels without faithful claims, and relying on visual YAML plausibility. Good: inspect the local constraints, label version assumptions, parse the file, then test explicit and implicit invocation. Bad: copy the example and stop after formatting. Borderline: omit a field when behavior cannot be verified rather than assigning a guessed value.

**Verification, evidence, and uncertainty.** Audit a sample configuration for source mapping, evidence labels, parser success, path resolution, prompt contract, dependency semantics, and activation behavior; record any omitted gate. The original table directly supplies the three names, order, values, tiers, and failure targets. The seed provides no empirical scoring basis, so numerical calibration is unsupported.

**Second-order consequence.** The scoreboard represents a metadata control pipeline whose value lies in preventing silent configuration from outrunning provenance and observable behavior.

**Revision decision.** Explain causal ordering, prohibit probability interpretation, and add field-level plus behavior-level completion evidence.

**Retained seed evidence.** All three original rows and numeric values remain unchanged. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| pattern_identifier_stable_key | pattern_score_numeric_value | pattern_tier_adoption_level | pattern_failure_prevention_target |
| --- | ---: | --- | --- |
| `openai_skill_yaml_patterns` | 95 | default_adoption_pattern_tier | Source Map First: Load local openai skill material before synthesizing yaml patterns recommendations. |
| `openai_skill_yaml_patterns` | 91 | default_adoption_pattern_tier | Evidence Boundary Split: Separate local facts, external facts, and inference before giving agent instructions. |
| `openai_skill_yaml_patterns` | 88 | default_adoption_pattern_tier | Verification Gate Coupling: Attach each recommendation to at least one command, checklist, or review gate. |

## Idiomatic Thesis Synthesis Statement

**Decision supported.** This section helps decide what governing principle should turn the local field contract into reliable product metadata. The seed states a generic local-first synthesis but does not explain why `openai.yaml` should remain a compact machine interface or how field omission reduces risk.

**Recommended default and causal basis.** Encode only product-facing presentation, dependency, and activation facts that the harness consumes; keep model behavior in the skill instructions; omit unsupported optional fields; and verify both syntax and activation semantics. Configuration fields can silently alter discovery, invocation, or tool availability, so minimizing authority and separating layers reduces hidden behavior.

**Operating conditions and assumptions.** The skill identity is stable, every included field has a consumer, strings and paths are deterministic, dependencies are intentional, and invocation policy is reviewed. Apply the thesis to `agents/openai.yaml` only, while preserving behavior and procedural depth in SKILL.md.

**Failure boundary and alternatives.** YAML becomes a second prompt, optional keys are populated with guesses, implicit invocation is enabled without trigger review, or metadata is considered correct merely because it parses. Bounded alternatives and recoveries: omit the file, include only interface metadata, disable implicit invocation, defer dependencies, or use another product-specific file for a different harness.

**Counterexample, gotchas, and operational comparison.** Long descriptions, prompts without `$skill-name`, relative paths from the wrong directory, unsupported tool types, URL and transport mismatch, and unstated defaults. Good: a minimal interface block and deliberate false policy for a sensitive skill. Bad: embed operational procedure in `default_prompt`. Borderline: omit dependency metadata when installation is external and the harness contract is uncertain.

**Verification, evidence, and uncertainty.** Compare keys against the local contract, parse YAML, resolve paths from the skill directory, inspect prompt and description constraints, verify dependency availability, and test explicit versus implicit activation. The local source directly defines machine ownership, product-specific placement, field semantics, supported dependency category, and policy default. Current harness validation behavior and cross-product portability are not established by the archive.

**Second-order consequence.** Minimal metadata is a least-authority design: every omitted field removes a silent product behavior that would otherwise require maintenance and testing.

**Revision decision.** Replace generic synthesis with least-authority metadata, omission defaults, layer ownership, and dual structural-behavioral verification.

**Retained seed evidence.** The original evidence labels and local-first sequence remain verbatim. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`local_corpus_sourced_fact`: The local row for `openai_skill_yaml_patterns` contains 1 source path(s), which should be treated as the first retrieval surface for this theme.
`external_research_sourced_fact`: The external source map provides public documentation, repository, or ecosystem analogues where available.
`combined_evidence_inference_note`: Reliable use of Openai Skill Yaml Patterns comes from loading the local corpus first, checking public ecosystem guidance second, and converting both into verification-backed agent decisions.

## Local Corpus Source Map

**Decision supported.** This section helps decide how to extract the complete useful contract from the sole local source without treating an example as mandatory boilerplate. The seed identifies one 49-line canonical source but does not expand its example into field clusters, required versus optional status, defaults, or validation responsibilities.

**Recommended default and causal basis.** Read the source end to end, classify `interface`, `dependencies.tools`, and `policy` separately, treat described fields as optional unless the contract states otherwise, preserve explicit constraints, and record omitted fields with reasons. A complete field-level map prevents copying every example key and makes defaulted behavior, path ownership, and nested-list semantics visible.

**Operating conditions and assumptions.** The target skill can answer whether each field is useful, assets and dependencies exist, and policy intent is explicit. Treat this file as canonical for the archived field vocabulary, not as proof of present product implementation.

**Failure boundary and alternatives.** The example becomes a required template, only headings are read, one source is promoted to universal current policy, or unspecified transport values are invented. Bounded alternatives and recoveries: use a minimal interface-only file, omit the file, inspect current harness schema, or add another product-specific config under `agents/`.

**Counterexample, gotchas, and operational comparison.** Single-source authority inflation, optionality confusion, failing to distinguish default true from explicitly true, and assuming `icon_large` must be SVG because the example is. Good: include display metadata and omit dependencies for a tool-free skill. Bad: copy the GitHub MCP row into every skill. Borderline: explicitly set `allow_implicit_invocation: true` only when documenting that choice adds review value.

**Verification, evidence, and uncertainty.** Build a field matrix with source wording, target need, value, validation, default, omission reason, and behavior test; compare every emitted key to the source. The local source was fully read and contains one complete example plus explicit descriptions for every shown field. A single archived source cannot prove current parser acceptance of unknown or newly added fields.

**Second-order consequence.** With a small canonical source, field-by-field completeness matters more than adding more prose, while authority remains bounded to the documented contract.

**Revision decision.** Convert the heading map into field clusters, optionality and default rules, omission decisions, and a target-value matrix.

**Retained seed evidence.** The original source path, title, heading signals, and usage role remain unchanged. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| local_source_filepath_value | local_source_title_text | local_source_heading_signals | local_source_usage_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202603/.system/skill-creator/references/openai_yaml.md | openai.yaml fields (full example + descriptions) | openai.yaml fields (full example + descriptions); Full example; Field descriptions and constraints | reference detail file for deeper pattern evidence |

## External Research Source Map

**Decision supported.** This section helps decide when a future maintainer should consult each external source to resolve a repository-instruction, implementation, or asset question. The seed lists AGENTS.md guidance, the Codex repository, and image-generation documentation without defining their narrow relevance or an explicit no-browse state.

**Recommended default and causal basis.** Use the AGENTS.md guide only for instruction-layer boundaries, inspect the Codex repository for current config consumption and examples, and consult image documentation only for generating suitable raster assets; verify schema claims against the owning current source. Related product documentation can answer neighboring questions while remaining nonauthoritative for `openai.yaml` field syntax.

**Operating conditions and assumptions.** A specific disputed claim is routed to the owning source and reproduced against the installed harness or actual asset. Use these rows as research routes rather than current evidence.

**Failure boundary and alternatives.** The links are cited as read, AGENTS.md rules become YAML fields, repository main is assumed to match an installed release, or image API output is treated as path-resolution proof. Bounded alternatives and recoveries: retain local archived guidance provisionally, inspect packaged examples, omit uncertain metadata, or request a current product schema.

**Counterexample, gotchas, and operational comparison.** Version drift, branch mismatch, icon-format assumptions, external URL churn, and source-domain bleed. Good: inspect the installed Codex version before adopting a newly observed field. Bad: use the AGENTS.md page to invent `policy` keys. Borderline: generate an icon from current image guidance but still validate file path and rendering locally.

**Verification, evidence, and uncertainty.** Log source, date, version or commit, exact claim, target consumer, contradiction, reproduction, and resulting config decision; otherwise state that the source was not refreshed. The seed accurately names three relevant external domains but none was accessed in this task. All present external content and compatibility remain unknown under the no-browse constraint.

**Second-order consequence.** An unopened source can still improve safety by identifying the precise place where uncertainty must later be resolved.

**Revision decision.** Add domain ownership, version and reproduction requirements, and an explicit uninspected state.

**Retained seed evidence.** All three original public rows and evidence labels remain verbatim. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| external_source_url_value | external_source_name_text | external_source_usage_role | evidence_boundary_label_value |
| --- | --- | --- | --- |
| https://developers.openai.com/codex/guides/agents-md | OpenAI Codex AGENTS.md guide | primary Codex custom instruction documentation | external_research_sourced_fact |
| https://github.com/openai/codex | OpenAI Codex repository | GitHub implementation and project conventions | external_research_sourced_fact |
| https://platform.openai.com/docs/guides/images | OpenAI image generation guide | primary image generation API documentation | external_research_sourced_fact |

## Anti Pattern Registry Table

**Decision supported.** This section helps decide which metadata defects should block completion and what safer replacement preserves the intended skill behavior. The seed catches generic provenance failures but omits malformed or semantically unsafe `openai.yaml` patterns.

**Recommended default and causal basis.** Retain the three provenance rows and detect agent instructions in machine metadata, copied optional boilerplate, unquoted strings, quoted keys, invalid description length, missing `$skill-name`, broken asset paths, unsupported dependency types, incomplete MCP entries, and accidental implicit invocation. These defects either make parsing fragile or silently change discovery, tools, and activation behavior.

**Operating conditions and assumptions.** Each detector has a concrete YAML or harness signal, a false-positive boundary, and a minimal correction. Apply detectors only to `agents/openai.yaml` and its actual consumer.

**Failure boundary and alternatives.** The registry becomes a style linter detached from the consumer, every omitted field is called an error, or parser acceptance is mistaken for semantic safety. Bounded alternatives and recoveries: omit unnecessary fields, use explicit invocation, keep assets absent, defer dependencies, or follow a stronger target schema when verified.

**Counterexample, gotchas, and operational comparison.** Placeholder icons, copied GitHub URLs, multiline prompts that become procedures, implicit true left unnoticed, and keys accepted but ignored. Good: reject a default prompt that fails to name `$review-skill`. Bad: require icons for a text-only skill. Borderline: keep an explicit true policy only when the review benefits from visibility despite matching the default.

**Verification, evidence, and uncertainty.** Capture field, raw value, source constraint, parser observation, path or dependency resolution, activation behavior, false-positive example, and correction. The local source directly supports every field-specific detector except unknown-key behavior, which remains a target-harness question. Parser strictness and diagnostics vary by product version.

**Second-order consequence.** Metadata anti-patterns should target silent behavioral divergence, not cosmetic preferences.

**Revision decision.** Extend the registry with field-level signals, omission-safe alternatives, and structural plus behavior checks.

**Retained seed evidence.** The three original provenance rows remain verbatim. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| anti_pattern_failure_name | failure_cause_risk_reason | safer_default_replacement_pattern | detection_signal_review_method |
| --- | --- | --- | --- |
| context_free_summary_output | agent skips local corpus and produces generic advice | source_map_first_synthesis | verify every listed local path appears in the generated file |
| unsourced_recommendation_claims | guidance appears authoritative without source boundary | evidence_boundary_split_pattern | check for local, external, and inference labels |
| unverified_agent_instruction | recommendation cannot be checked by command or review gate | verification_gate_coupling | require concrete gate in generated reference |

## Verification Gate Command Set

**Decision supported.** This section helps decide which layered checks prove the evolved reference and a derived `openai.yaml` are structurally and behaviorally valid. The seed offers one archive-wide generation command but not a YAML parser, schema, asset, dependency, or activation gate.

**Recommended default and causal basis.** Run the focused reference verifier, retain the archive command in its original context, parse the target YAML with a structured parser, compare keys and types to the contract, resolve asset paths, inspect prompt and description constraints, validate dependencies, and test invocation policy in the target harness. Document structure, YAML syntax, field semantics, resource existence, and runtime activation are separate claims.

**Operating conditions and assumptions.** Each check runs from the correct root, records its scope and exit status, and uses the actual skill name and directory. Use corpus commands for the reference and target-native tools for configuration behavior.

**Failure boundary and alternatives.** A linter pass proves activation, assets exist but cannot render, dependencies are syntactically valid but unavailable, or a planned harness test is reported as observed. Bounded alternatives and recoveries: perform static-only review with runtime claims withheld, omit untestable fields, or inspect installed product examples before enabling behavior.

**Counterexample, gotchas, and operational comparison.** Parser differences, wrong relative base, shell quoting, Unicode length assumptions, stale assets, network dependency checks, and implicit behavior hidden by cached state. Good: parse, resolve both icons, verify the prompt token, and observe explicit plus implicit invocation. Bad: run only the Markdown verifier. Borderline: accept a structure-only change while clearly deferring activation approval.

**Verification, evidence, and uncertainty.** Record command, root, parser, product version, file, exit status, field assertions, resource checks, behavior result, exclusions, and rerun trigger. The seed and local source define structural requirements; runtime verification remains target-dependent. No universal repository command or harness fixture is supplied.

**Second-order consequence.** Verification should fail at the cheapest responsible layer while never promoting that layer's success into a broader claim.

**Revision decision.** Define document, parse, contract, resource, dependency, and activation gates while preserving the original command.

**Retained seed evidence.** The original bash command remains unchanged. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`verification_gate_command_set`: Run the repository verifier after editing this file.

```bash
python3 agents-used-monthly-archive/idiomatic-references-202606/tools/verify_reference_generation.py --stage final
```

## Agent Usage Decision Guide

**Decision supported.** This section helps decide how an agent should decide whether to create or edit `agents/openai.yaml` and which fields to include. The seed says to start local and preserve evidence labels but does not guide an agent from skill inspection through minimal YAML, verification, and safe stopping.

**Recommended default and causal basis.** Read the skill name and purpose, confirm the OpenAI product consumer, inspect existing metadata and assets, map desired UI, dependency, and invocation behavior to supported fields, omit everything else, write structured YAML, and run field plus activation gates. A deterministic flow prevents generic YAML generation and copied dependencies from silently changing a skill.

**Operating conditions and assumptions.** The agent owns the skill files, knows the intended activation policy, and can inspect or test the consumer. Use this flow for one skill's OpenAI metadata, not general skill creation or plugin configuration.

**Failure boundary and alternatives.** The task concerns another product, current schema is unknown for a sensitive change, assets or dependencies are missing, or implicit invocation lacks an approved trigger model. Bounded alternatives and recoveries: leave the file absent, make an interface-only edit, disable implicit invocation, prepare assets separately, or ask for product-version evidence.

**Counterexample, gotchas, and operational comparison.** Editing SKILL.md unnecessarily, inventing names, forcing every example field, omitting explicit uncertainty, and failing to reconcile file paths. Good: add only display metadata and a prompt for a tool-free skill. Bad: copy the full GitHub MCP example. Borderline: stage dependency metadata but withhold completion until the server is configured and tested.

**Verification, evidence, and uncertainty.** Require a decision record with user goal, consumer, selected and omitted fields, source support, actual paths, dependency ownership, policy rationale, parser result, activation result, and rollback. The local contract gives a complete enough field vocabulary for a bounded flow. Target harness availability and current schema determine whether runtime completion is possible.

**Second-order consequence.** A successful agent may deliberately produce no YAML when metadata adds no validated product value.

**Revision decision.** Turn generic bullets into inspect-map-minimize-write-verify-stop steps with an omission record.

**Retained seed evidence.** The original four usage bullets remain intact. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`agent_usage_decision_guide`: Use this reference when a task mentions this theme, one of the listed local source paths, or a nearby technology/workflow surface.

- Start with the local corpus source map.
- Prefer patterns with explicit verification gates.
- Treat external sources as freshness and ecosystem checks, not replacements for local repo conventions.
- Preserve the evidence boundary labels when reusing recommendations.

## User Journey Scenario

**Decision supported.** This section helps decide how a contributor moves from a skill's user-facing need to a minimal, validated `openai.yaml` and a clear completion or stop state. The seed names a new contributor choosing what to load and trust but does not walk through a concrete skill metadata change.

**Recommended default and causal basis.** Start with the skill name and user-visible invocation, decide whether UI metadata, assets, tools, or implicit activation are needed, map each need to one supported field, write only those fields, parse, resolve resources, and test the resulting product behavior. Starting from observable skill use keeps the full example from dictating unnecessary keys and makes silent activation consequences visible.

**Operating conditions and assumptions.** The skill is present, the product consumer is identified, assets and dependencies are owned, and explicit and implicit invocation can be observed. Scope the journey to one skill and one OpenAI product metadata file.

**Failure boundary and alternatives.** The contributor lacks the skill name, confuses agent instructions with metadata, cannot validate a sensitive policy, or is configuring another product. Bounded alternatives and recoveries: omit metadata, add interface fields only, defer assets or dependencies, disable implicit invocation, or route to skill and plugin authoring guidance.

**Counterexample, gotchas, and operational comparison.** Display text that overpromises, inaccessible icon contrast, stale asset paths, prompt mismatch, hidden dependency installation, and inability to undo implicit activation. Good: add a concise listing for `$release-notes`, verify icons and explicit invocation, then test implicit activation only if intended. Bad: paste a long workflow into `default_prompt`. Borderline: ship metadata without icons when the UI supports omission and no approved asset exists.

**Verification, evidence, and uncertainty.** Capture user goal, skill identifier, included and omitted fields, source basis, generated file, path checks, parser result, UI observation, invocation tests, failure case, and rollback. The local field contract directly supports every decision point in the journey. Target UI rendering and harness behavior require a live consumer not supplied here.

**Second-order consequence.** The journey converts optional metadata into user-observable claims, so every field should have a corresponding observation or explicit deferment.

**Revision decision.** Add a start-to-finish field-selection journey with omission, runtime observation, and rollback states.

**Retained seed evidence.** The original role, starting state, decision, and opening trigger remain verbatim. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Role based opening scenario: The new contributor or agent is starting from an unfamiliar theme and deciding whether this reference is the right tool and needs a reference that turns source evidence into an executable next step.
Primary user starting state: The user has a `openai_skill_yaml_patterns` task, one or more local source paths, and uncertainty about which pattern should drive implementation.
Decision being made: choosing what to load, what to trust, what to avoid, and what evidence proves success.
Reference opening trigger: Open this file when the task mentions openai skill yaml patterns, any mapped local source path, or an adjacent workflow with the same failure mode.

## Decision Tradeoff Guide

**Decision supported.** This section helps decide when to adopt the local example, adapt selected fields, avoid metadata, or escalate a policy or dependency choice. The seed provides generic adopt, adapt, avoid, and cost rows but does not compare omission versus declaration, implicit versus explicit activation, or metadata versus behavioral instruction.

**Recommended default and causal basis.** Adopt exact syntax and constraints, adapt optional fields to the skill's real interface, omit values with no consumer, choose implicit invocation only after false-positive and sensitivity review, and escalate unknown dependency or harness behavior. The safest file is not the most complete example but the smallest one whose user and runtime consequences are intentional.

**Operating conditions and assumptions.** Field value, consumer, evidence, and behavior are all known. Apply to field selection within the documented contract, not general agent architecture.

**Failure boundary and alternatives.** Adoption copies placeholders, adaptation invents unsupported keys, avoidance hides required dependencies, or cost of wrong implicit activation is ignored. Bounded alternatives and recoveries: interface-only metadata, explicit-only invocation, no icons, external dependency documentation, or no `openai.yaml`.

**Counterexample, gotchas, and operational comparison.** Default true treated as neutral, false reducing discoverability, a short description becoming vague, icon formats chosen from examples, and MCP URL metadata exposing an unavailable service. Good: disable implicit invocation for a destructive deployment skill. Bad: enable it because true is the default. Borderline: retain true for a benign formatter after testing false-positive task samples.

**Verification, evidence, and uncertainty.** Write a tradeoff record for user benefit, activation risk, dependency availability, maintenance cost, omission behavior, test evidence, and rollback. The local source directly documents the policy semantics, default, supported dependency type, and interface fields. Actual product behavior for omitted keys and unsupported values should be confirmed per version.

**Second-order consequence.** Optional metadata choices are policy choices because they shape what users see and when the model receives a skill.

**Revision decision.** Add field-level alternatives, activation-risk review, omission semantics, and escalation triggers.

**Retained seed evidence.** The four original decision rows remain unchanged. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| decision_option_name | when_to_choose_condition | tradeoff_cost_description | verification_question_prompt |
| --- | --- | --- | --- |
| Adopt when | local corpus and external evidence agree on the openai skill yaml patterns pattern | fastest path, but can copy stale local assumptions | Does the selected pattern appear in the canonical source and current external evidence? |
| Adapt when | local sources are strong but public ecosystem guidance has changed | preserves repo fit, but requires explicit inference notes | Did the reference label the local fact, external fact, and combined inference separately? |
| Avoid when | source evidence is thin, conflicting, or unrelated to the user journey | prevents false confidence, but may require deeper research | Is there a confidence warning or adjacent reference route? |
| Cost of being wrong | wrong openai skill yaml patterns guidance can send an agent to the wrong files, tests, or abstraction | wasted implementation loop and weaker verification | Would a reviewer know what to undo and what to inspect next? |

## Local Corpus Hierarchy

**Decision supported.** This section helps decide how much authority the archived field reference should carry when target examples or current harness behavior differ. The seed correctly names one canonical local source and a confidence warning but does not define canonical scope, override rules, or conflict handling.

**Recommended default and causal basis.** Treat it as canonical for archived field vocabulary and stated constraints, then let target parser behavior, installed-version examples, and current official product evidence determine present applicability; record every conflict. Corpus canonicality supports consistent routing but cannot override the live machine that consumes the file.

**Operating conditions and assumptions.** The claim lies within the source's scope, the target behavior corroborates it, and no stronger current owner conflicts. Use hierarchy inside this corpus and initial review, not as an immutable current product schema.

**Failure boundary and alternatives.** Canonical becomes timeless, one example makes all keys mandatory, current unknown fields are accepted without evidence, or conflict is silently harmonized. Bounded alternatives and recoveries: classify a claim as supporting, prefer installed schema, omit the disputed field, retain competing interpretations, or assign a product owner.

**Counterexample, gotchas, and operational comparison.** Authority by path, absence of multiple sources treated as consensus, defaults confused with requirements, and runtime acceptance generalized across versions. Good: preserve the documented prompt requirement and test it in the installed harness. Bad: reject a verified new field solely because the archive lacks it. Borderline: retain an older field provisionally when the parser accepts it but UI behavior is unobserved.

**Verification, evidence, and uncertainty.** Record claim scope, source wording, target version, parser and behavior evidence, conflict, override reason, owner, and reclassification trigger. The source is complete for its small archived contract and the seed explicitly labels it canonical. Single-source coverage and archive age limit current policy confidence.

**Second-order consequence.** Hierarchy should specify legal overrides, enabling evolution without either freezing old metadata or discarding stable constraints.

**Revision decision.** Define canonical scope, live-consumer override order, conflict records, and omission-safe resolution.

**Retained seed evidence.** The original vocabulary, warning, canonical row, and reviewer question remain verbatim. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Classification vocabulary includes canonical, supporting, legacy, duplicate, and conflicting source roles.
Confidence warning: only one local corpus source is mapped, so this reference should invite adjacent-source discovery before becoming canonical policy.

| local_source_filepath_value | corpus_hierarchy_role | heading_signal_to_convert | reviewer_question_to_answer |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202603/.system/skill-creator/references/openai_yaml.md | canonical primary source | openai.yaml fields (full example + descriptions); Full example; Field descriptions and constraints | What guidance, warning, or example should this source contribute to Openai Skill Yaml Patterns? |

## Theme Specific Artifact

**Decision supported.** This section helps decide what reviewable artifact should accompany a new or changed `agents/openai.yaml`. The seed names a skill activation contract but its three rows do not capture actual YAML fields, omission decisions, resources, dependencies, or activation evidence.

**Recommended default and causal basis.** Produce a metadata activation contract containing skill identity, user goal, target product, selected and omitted fields, rendered labels, asset inventory, default prompt, dependency ownership, implicit policy, misuse case, parse result, runtime observations, rollback, and evidence labels. The artifact exposes every silent product behavior introduced by a compact configuration and lets a reviewer replay the decision.

**Operating conditions and assumptions.** One skill owns the artifact and expected results become observed after checks. One contract per skill metadata change.

**Failure boundary and alternatives.** The artifact copies the example, omits omitted-field rationale, describes planned tests as passed, or lacks a misuse and rollback case. Bounded alternatives and recoveries: use a minimal interface review for display-only changes, an asset sheet for icon work, or a dependency readiness record for MCP integration.

**Counterexample, gotchas, and operational comparison.** Skill name mismatch, hidden default policy, inaccessible or missing icons, dependency ownership ambiguity, and stale screenshots. Good: document why a release skill is explicit-only and show the explicit invocation result. Bad: list YAML keys without user consequences. Borderline: record an untested icon as pending while accepting other fields.

**Verification, evidence, and uncertainty.** Compare artifact to YAML and skill name, resolve resources, inspect constraints, execute tests, record observations, have another reviewer reproduce, and exercise rollback. The local source and seed artifact concept directly support the expanded fields. UI screenshots and activation evidence require a live target.

**Second-order consequence.** The activation contract is a compact behavioral diff for metadata that otherwise has no code-level execution trace.

**Revision decision.** Expand the three rows into field inventory, omission log, misuse case, observations, and rollback.

**Retained seed evidence.** The original user-goal, decision-boundary, and verification-gate rows remain mandatory. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Theme specific artifact: skill activation contract with progressive disclosure, misuse case, and verification gate.

| artifact_field_name | artifact_completion_rule | evidence_source_hint |
| --- | --- | --- |
| user_goal_statement | state the user's concrete goal before applying Openai Skill Yaml Patterns | local corpus hierarchy plus critique findings |
| decision_boundary_rule | define the point where this reference should be used or avoided | decision tradeoff guide |
| verification_gate_rule | define the command, checklist, or review question that proves the artifact worked | verification gate command set |

## Worked Example Set

**Decision supported.** This section helps decide which contrasting configurations teach minimal metadata, activation policy, dependency readiness, and safe omission. The seed's examples discuss source use rather than valid and invalid metadata decisions.

**Recommended default and causal basis.** Show good, bad, and borderline cases with skill context, selected fields, user consequence, parser result, behavior observation, and correction. Operational examples reveal silent activation and dependency failures that abstract YAML rules do not.

**Operating conditions and assumptions.** Cases differ on a governing condition and avoid asserting unverified current keys. Examples teach decision logic and must be adapted to the target skill.

**Failure boundary and alternatives.** Examples are copied templates, bad cases are trivial syntax errors only, or borderline cases lack an expiry condition. Bounded alternatives and recoveries: compare explicit and implicit policy, interface-only and full metadata, tool-free and MCP-dependent skills, or valid and broken asset paths.

**Counterexample, gotchas, and operational comparison.** Prompt missing skill token, copied dependency, overlong description, icons outside assets, and accidental default policy. Good: an explicit-only destructive skill with a short prompt naming `$deploy-check`. Bad: a generic prompt, nonexistent icon, and copied GitHub dependency. Borderline: a benign skill keeps implicit activation after false-positive evaluation and records a review trigger.

**Verification, evidence, and uncertainty.** For each case, parse, inspect constraints, resolve paths and dependency, test activation, record user-visible result, and show recovery. The local source supplies precise constraints for realistic examples. Exact UI rendering and parser diagnostics are product-version dependent.

**Second-order consequence.** Borderline cases are useful only when they expose the evidence that makes an otherwise risky choice acceptable.

**Revision decision.** Replace generic source examples with field-level operational cases while retaining the originals.

**Retained seed evidence.** The original good, bad, and borderline source-discipline sentences remain verbatim. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Good example: Use Openai Skill Yaml Patterns after loading the canonical source, confirming the external evidence boundary, and writing a verification gate before implementation.
Bad example: Use Openai Skill Yaml Patterns as a generic tutorial while ignoring the mapped local paths, source hierarchy, and cost of being wrong.
Borderline case: Use Openai Skill Yaml Patterns only after adding a confidence warning when local evidence is thin or conflicts with current ecosystem guidance.

## Outcome Metrics and Feedback Loops

**Decision supported.** This section helps decide which measurements show that `openai.yaml` guidance improves safe skill discovery and activation without encouraging unnecessary metadata. The seed says the next task should be less ambiguous and the reference should become operational, but it lacks defined metadata quality, invocation, and maintenance signals.

**Recommended default and causal basis.** Track parser failures, broken resource paths, prompt-token compliance, description-length violations, missing dependencies, explicit invocation success, implicit false positives and misses, user selection accuracy, rollback clarity, and stale-field rework. A file can be syntactically green while confusing users or activating a skill at the wrong time.

**Operating conditions and assumptions.** Metrics have denominators, task samples, versions, owners, and a concrete field or gate change on failure. Measure within one product and comparable skills, not as a universal skill benchmark.

**Failure boundary and alternatives.** More populated fields count as quality, one successful invocation proves policy, user behavior is inferred without observation, or repeated defects only add prose. Bounded alternatives and recoveries: use small decision audits, UI review, activation confusion reports, dependency readiness checks, or qualitative analysis when usage volume is low.

**Counterexample, gotchas, and operational comparison.** Selection bias, harmless implicit misses mixed with dangerous false positives, cache effects, product-version changes, and conflating absent metadata with failure. Good: sample explicit and implicit tasks and investigate two false-positive activations. Bad: claim success because YAML parses. Borderline: use reviewer decision time for a metadata-only corpus when live product telemetry is unavailable.

**Verification, evidence, and uncertainty.** Define unit, population, sample, version, collection method, severity, threshold, owner, action, and follow-up evidence. The seed supplies useful qualitative leading and failure signals; operational measurements are bounded inference. No baseline, telemetry, or product usage sample exists.

**Second-order consequence.** Feedback should remove or narrow a field before adding more metadata when confusion or false activation appears.

**Revision decision.** Define structural, resource, dependency, discovery, and activation metrics with denominators and actions.

**Retained seed evidence.** The original leading indicator, failure signal, and cadence remain verbatim. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Leading indicator: the next task uses the reference to make a better decision with less ambiguity.
Failure signal: the reference remains a source map and never becomes an operating guide.
Review cadence: Re-run the verifier after every generated-reference edit and refresh external sources when public APIs, docs, or tooling releases change.

## Completeness Checklist

**Decision supported.** This section helps decide what evidence must exist before a metadata change is complete. The seed checks document ingredients but not whether emitted YAML fields, resources, dependencies, and policies are complete and connected.

**Recommended default and causal basis.** Require skill identity, product consumer, selected and omitted fields, quoted strings, unquoted keys, valid description length, exact `$skill-name` prompt, resolvable assets, supported dependencies, intentional invocation policy, parse result, runtime observations, uncertainty, and rollback. Connected field evidence prevents a structurally polished file from carrying broken or unintended behavior.

**Operating conditions and assumptions.** Each item links to source text, YAML, a resource, command result, or justified non-applicability. Apply to one `openai.yaml` change.

**Failure boundary and alternatives.** Boxes are checked from intent, optional fields are required, runtime behavior is skipped, or non-applicable conceals missing ownership. Bounded alternatives and recoveries: use a reduced interface-only checklist, an asset-only review, or a dependency readiness gate.

**Counterexample, gotchas, and operational comparison.** Wrong skill token, path base, short-description counting, hidden default, untested MCP, and stale screenshot. Good: mark dependency complete only after server availability and invocation test. Bad: mark icons complete because paths look plausible. Borderline: justify absent icons and close every other field.

**Verification, evidence, and uncertainty.** Perform a field evidence pass and then replay explicit, implicit, and failure journeys; reopen any unsupported item. The seed and local source directly define structural minimums. Target products may require additional checks.

**Second-order consequence.** Completeness is connectivity between metadata intent, stored value, resource, and observed product behavior.

**Revision decision.** Retain seven seed bullets and add field, resource, dependency, policy, and runtime evidence.

**Retained seed evidence.** All original checklist bullets remain verbatim. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- The role scenario names the user, starting state, decision, and trigger for Openai Skill Yaml Patterns.
- The decision guide includes Adopt when, Adapt when, Avoid when, and Cost of being wrong.
- The local corpus hierarchy identifies canonical and supporting sources or gives a confidence warning.
- The theme specific artifact is concrete enough to review without reading every mapped source.
- The examples cover good, bad, and borderline usage.
- The metrics section names one leading indicator and one failure signal.
- The adjacent routing section points to a better reference when this one is not the right fit.

## Adjacent Reference Routing

**Decision supported.** This section helps decide when this field reference stops owning the task and what context must accompany a handoff. The seed points generically to OpenAI, skill, and YAML references without concrete triggers for instruction authoring, plugin metadata, MCP setup, or asset creation.

**Recommended default and causal basis.** Stay here for `agents/openai.yaml`; route skill behavior to skill-authoring guidance, repository instructions to AGENTS.md guidance, plugin structure to plugin references, MCP server setup to integration guidance, image creation to asset tooling, and generic syntax to a YAML parser reference. Explicit ownership prevents a small metadata guide from issuing shallow instructions across distinct schemas and runtime systems.

**Operating conditions and assumptions.** The disputed question is named and the adjacent owner receives skill name, target product, existing metadata, evidence, and expected return. Keep field semantics here and route implementation of adjacent systems.

**Failure boundary and alternatives.** Routing follows keywords, cycles among references, dumps all context, or returns without reconciling changed fields. Bounded alternatives and recoveries: finish an in-scope metadata decision, omit a field, inspect the target consumer, or stop with a missing authority.

**Counterexample, gotchas, and operational comparison.** Sending default-prompt wording to AGENTS.md, treating MCP setup as one YAML row, conflating asset generation and path validation, and failing to merge policy decisions. Good: route server credentials to MCP integration while retaining dependency declaration here. Bad: use image guidance to decide invocation policy. Borderline: split icon creation from metadata validation with one shared asset-path contract.

**Verification, evidence, and uncertainty.** Record trigger, owner, compact handoff, expected answer, return condition, conclusion, reconciled field, and cycle check. The seed names broad neighbors and the local source clearly limits this file to product metadata. Current repository references and ownership must be discovered.

**Second-order consequence.** Routing is a typed handoff that preserves the unresolved field decision rather than a generic link list.

**Revision decision.** Add concern-specific routes, handoff schema, cycle prevention, and reconciliation.

**Retained seed evidence.** The original adjacent guidance and three pointers remain verbatim. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Adjacent reference guidance: Use the nearest language, workflow, agent, or documentation reference when the theme becomes concrete.
Adjacent reference 1: consider the openai adjacent reference when the current task pivots away from openai skill yaml patterns.
Adjacent reference 2: consider the skill adjacent reference when the current task pivots away from openai skill yaml patterns.
Adjacent reference 3: consider the yaml adjacent reference when the current task pivots away from openai skill yaml patterns.

## Workload Model

**Decision supported.** This section helps decide what metadata change can be reviewed coherently before sources, skills, products, or ownership must be split. The seed frames an agent workflow and gives one task, ten files, three subtasks, and a completion audit, but field metadata usually has a smaller natural unit and the numbers are uncalibrated.

**Recommended default and causal basis.** Scope one batch to one skill, one target product, one `openai.yaml`, its directly referenced assets and dependencies, one activation policy, and one rollback; treat seed counts as context-pressure prompts. Skill and product ownership keep field intent, resources, and invocation behavior causally connected.

**Operating conditions and assumptions.** All fields share one skill identity and consumer, resources can be verified, and rollback is independent. Use for review decomposition, not production capacity or agent-performance claims.

**Failure boundary and alternatives.** Multiple skills or products share a batch, dependencies have different owners, asset generation dominates, source discovery is unbounded, or activation tests cannot isolate behavior. Bounded alternatives and recoveries: split by skill, product, dependency, asset package, or policy; create a shared asset contract; or route broad automation planning elsewhere.

**Counterexample, gotchas, and operational comparison.** File count as complexity, three subtasks as entitlement, shared icons changed globally, dependency rollout hidden in metadata, and nonreversible discovery effects. Good: review one skill's display fields, two icons, one MCP declaration, and one policy together. Bad: bulk-copy metadata across twenty unrelated skills. Borderline: batch several skills only when a generated template, independent validation, and per-skill rollback prevent coupling.

**Verification, evidence, and uncertainty.** Record skills, products, files, assets, dependencies, owners, activation samples, rollback units, and split rationale. The seed directly supplies workflow bounds and the local contract indicates a single skill-relative file. Numeric thresholds have no calibration.

**Second-order consequence.** The coherent scale unit is one independently reversible skill activation contract, not a raw source or subtask count.

**Revision decision.** Center one-skill ownership, demote numeric values to prompts, and add product, dependency, asset, and rollback dimensions.

**Retained seed evidence.** The original operating note and four workload rows remain unchanged. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`combined_evidence_inference_note`: Treat Openai Skill Yaml Patterns as a agent workflow operating reference, not as a prose summary.

| workload_dimension_name | workload_boundary_value | verification_pressure_point |
| --- | --- | --- |
| primary_usage_surface | agent planning, tool use, context loading, delegation, or skill/plugin execution where bad guidance compounds across long-running sessions | verify that the reference changes the next implementation or review action |
| bounded_capacity_model | one primary task, up to 10 source files, up to 3 delegated subtasks, and a written completion audit for every run | split the task or create a narrower reference when this boundary is exceeded |
| source_pressure_model | local heading signals include openai.yaml fields (full example + descriptions); Full example; Field descriptions and constraints | compare guidance against canonical local sources before following external examples |
| artifact_pressure_model | required artifact is skill activation contract with progressive disclosure, misuse case, and verification gate | require the artifact before claiming the reference is operationally usable |

## Reliability Target

**Decision supported.** This section helps decide what reliable outcome this reference should produce and how corpus accuracy differs from target metadata behavior. The seed measures provenance, 18-of-20 routing, unsupported claims, and recovery but not field correctness, resource resolution, dependency readiness, or activation safety.

**Recommended default and causal basis.** Require preserved provenance, correct route decisions, zero unsupported field claims, complete recovery, valid structure, resolvable resources, intentional dependencies, and observed explicit and implicit activation outcomes. A well-routed reference can still generate a broken icon or unsafe policy, while target behavior without provenance may institutionalize accidental parser quirks.

**Operating conditions and assumptions.** Samples cover interface, dependency, and policy cases and high-severity false activations are isolated. Evaluate the reference and metadata decisions, not overall product reliability.

**Failure boundary and alternatives.** 18-of-20 masks a destructive false activation, labels are decorative, parser success substitutes for resource checks, or metadata reliability is called product reliability. Bounded alternatives and recoveries: severity-weighted audits, perfect safety samples for sensitive skills, uncertainty calibration, or product-specific acceptance targets.

**Counterexample, gotchas, and operational comparison.** Small samples, duplicate configurations, easy display-only cases, missing negative invocation tests, and vague recovery. Good: fail the gate for one dangerous implicit invocation despite nineteen correct field routes. Bad: pass twenty parse-only samples. Borderline: retain 18-of-20 as a corpus smoke test with stricter policy behavior gates.

**Verification, evidence, and uncertainty.** Publish sample selection, field coverage, severity, reviewer rubric, evidence trace, target behavior, numerator and denominator, correction, and rerun. The four seed rows are direct facts; added field and activation targets follow from the local contract. The routing threshold lacks a supplied validation study.

**Second-order consequence.** Activation harm is asymmetric, so aggregate accuracy must never average away a high-cost false positive.

**Revision decision.** Retain rows, add field/resource/dependency/activation checks, severity, and target evidence.

**Retained seed evidence.** All four original reliability rows remain verbatim. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| reliability_target_name | measurable_threshold_value | evidence_collection_method |
| --- | --- | --- |
| source_boundary_preservation | 100 percent of recommendations keep local, external, and inference boundaries visible | review generated text for the three evidence labels before reuse |
| decision_accuracy_sample | at least 18 of 20 sampled uses route to the correct adopt, adapt, avoid, or adjacent-reference decision | sample downstream tasks and record reviewer verdicts |
| unsupported_claim_rate | zero unsupported production, security, latency, or reliability claims in final guidance | reject claims without source row, explicit inference note, or verification method |
| recovery_path_clarity | every avoid or failure case names the rollback, escalation, or next-reference route | inspect failure-mode and adjacent-routing sections together |

## Failure Mode Table

**Decision supported.** This section helps decide which failures invalidate a metadata recommendation and what signal should trigger containment or correction. The seed covers source drift, generic advice, context loss, and tool fanout but omits YAML, resource, dependency, and activation failure classes.

**Recommended default and causal basis.** Classify failures as stale contract, syntax or type error, unsupported key, invalid UI text, broken asset, prompt mismatch, unavailable MCP dependency, transport or URL mismatch, implicit false positive, implicit miss, context drift, or conflicting ownership. Distinct classes require different recoveries; retrying or rewriting YAML does not repair an unavailable server or unsafe activation policy.

**Operating conditions and assumptions.** Each class has an observable detector, owner, containment, correction, and recovery test. Use for metadata authoring and controlled product tests.

**Failure boundary and alternatives.** All failures become parser errors, implicit behavior is unobserved, dependency failure triggers repeated generation, or stale context overwrites user intent. Bounded alternatives and recoveries: omit the field, disable implicit invocation, restore the prior file, repair the asset, configure the dependency, or escalate a schema conflict.

**Counterexample, gotchas, and operational comparison.** Silent ignored keys, cached UI, relative path ambiguity, policy default hidden by omission, and unreachable URLs accepted as strings. Good: detect a false-positive activation, set policy false, and verify explicit invocation. Bad: retry loading a nonexistent icon. Borderline: preserve a dependency declaration while blocking release until the server is available.

**Verification, evidence, and uncertainty.** Reproduce safely, capture distinguishing signal, contain impact, verify file and skill integrity, rerun original trigger, and record residual risk. Field-specific modes follow directly from the local source; context and fanout rows are retained seed facts. Diagnostic behavior depends on the target parser and harness.

**Second-order consequence.** Failure classification should separate static metadata defects from external-resource and activation-policy failures before choosing recovery.

**Revision decision.** Add field, resource, dependency, and activation modes with original-trigger recovery.

**Retained seed evidence.** All four original failure rows remain verbatim. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| failure_mode_name | likely_trigger_condition | required_mitigation_action |
| --- | --- | --- |
| source drift hides truth | external or local guidance changes after the reference was written | refresh public evidence, rerun local corpus gate, and mark stale claims before reuse |
| generic advice escapes review | agent copies plausible best practices without theme-specific verification | block completion until the verification gate names concrete command, reviewer question, or metric |
| context window loses plan | long-running session forgets early constraints or overwrites user intent | write checkpoint summaries and re-read plan before each destructive step |
| tool fanout outruns budget | parallel actions create conflicts, duplicate work, or unbounded external calls | cap fanout, assign ownership, and require merge/audit checkpoints |

## Retry Backpressure Guidance

**Decision supported.** This section helps decide when a failed metadata check should be retried and when work must stop or roll back. The seed governs evidence refresh and agent workflow retries but does not distinguish parser reruns, asset repair, dependency probes, or activation evaluation.

**Recommended default and causal basis.** Classify the failure first, allow one stale-source refresh retry, rerun deterministic parsing only after a file change, bound dependency probes, avoid repeated activation tests without new evidence, and stop new edits when ownership, policy safety, or verification is red. Repetition without a state change creates noise, external calls, and context drift while leaving semantic failures unresolved.

**Operating conditions and assumptions.** The failure is transient, an input changed, retry budget is explicit, and no user-facing activation harm can compound. Apply to metadata workflow and checks, not general MCP runtime resilience.

**Failure boundary and alternatives.** Invalid YAML is rerun unchanged, nonexistent assets are polled, unavailable MCP servers trigger unbounded calls, or unsafe implicit activation remains live during testing. Bounded alternatives and recoveries: fail fast, restore the prior file, omit the field, disable implicit invocation, repair the resource, or escalate.

**Counterexample, gotchas, and operational comparison.** Nested tool retries, cached results, network flakiness mistaken for schema failure, repeated generation, and no rollback snapshot. Good: fix a path then rerun resolution once. Bad: repeatedly test a missing server URL. Borderline: probe a known transient MCP outage within a bounded operational policy.

**Verification, evidence, and uncertainty.** Record failure class, changed input, attempts, elapsed time, external calls, rollback, stop condition, and final observation. The seed directly supports bounded evidence retries and red-gate backpressure. Target product retry behavior is not documented locally.

**Second-order consequence.** Retry is justified by new information or changed state, not by discomfort with an unchanged failure.

**Revision decision.** Separate deterministic and external checks, require state change, cap probes, and protect activation during recovery.

**Retained seed evidence.** The five original retry and ownership bullets remain verbatim. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- Retry only after the failed verification signal is classified as transient, stale evidence, missing context, or true contradiction.
- Use one bounded retry for stale external evidence refresh, then escalate to a human or a narrower source-specific reference.
- Apply backpressure by stopping new generation or implementation work when source coverage, critique coverage, or verification gates are red.
- For long-running agent workflows, checkpoint after each batch and re-read the current spec before any broad rewrite, commit, push, or destructive operation.
- For distributed execution, assign one owner per generated file or theme batch and require merge-time verification of exact path, heading, and evidence-boundary invariants.

## Observability Checklist

**Decision supported.** This section helps decide what compact evidence makes a skill metadata change diagnosable and reviewable. The seed tracks source loading, commands, latency, tool calls, delegated tasks, retries, and audit outcomes but not metadata field or activation observations.

**Recommended default and causal basis.** Record skill and product version, file hash, fields present and omitted, parser result, resolved assets, dependency checks, explicit and implicit invocation samples, false positives and misses, retries, reviewer decision, and rollback. Silent metadata has little execution trace unless authoring and activation observations are captured deliberately.

**Operating conditions and assumptions.** Records are low-volume, redact credentials, identify versions, and map each failure to a field and action. Capture authoring and controlled activation evidence only.

**Failure boundary and alternatives.** Raw secrets or prompts are logged, UI screenshots lack version context, tool counts replace outcomes, or activation samples cannot be reproduced. Bounded alternatives and recoveries: structured audit notes, parser output, asset manifest, dependency readiness report, or sampled activation matrix.

**Counterexample, gotchas, and operational comparison.** MCP URLs with credentials, cached UI, mutable assets under same path, no file hash, and only successful samples. Good: record a false-positive task, policy change, and passing explicit invocation. Bad: store a raw authorization header. Borderline: retain screenshots as supplemental evidence alongside field and version records.

**Verification, evidence, and uncertainty.** Exercise parse, resource, dependency, explicit, implicit, misuse, and rollback paths; inspect redaction, version, reproducibility, and actionability. The seed gives workflow audit signals and local source defines observable field consequences. Product telemetry and privacy rules vary.

**Second-order consequence.** Metadata observability is primarily decision provenance plus activation sampling, not high-volume runtime logging.

**Revision decision.** Add field inventory, hashes, resource/dependency status, activation matrix, redaction, and rollback evidence.

**Retained seed evidence.** All six original observability bullets remain verbatim. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- Record which local sources were loaded and which were intentionally skipped.
- Record the exact verification command, reviewer question, or rendered artifact used as proof.
- Record p50/p95/p99 latency or reviewer-time measurements when the reference affects runtime or workflow speed.
- Capture tool-call count, context files loaded, delegated tasks, retry count, and completion-audit outcome.
- Record leading indicator and failure signal from this file in the coverage manifest or journal when the reference drives real work.
- Keep audit evidence small enough to review: command output summary, changed-file list, and unresolved-risk notes are preferred over raw transcript dumps.

## Performance Verification Method

**Decision supported.** This section helps decide how to measure authoring and activation efficiency without optimizing for fewer checks or more populated fields. The seed requires tool-call and timeout budgets for long workflows but does not define what efficient metadata work means or prevent speed from replacing correctness.

**Recommended default and causal basis.** Measure source-to-decision time, parser and resource-check time, activation evaluation time, tool and external-call counts, context loaded, retry waste, reviewer decision time, and false-activation outcomes alongside correctness. Metadata is small, so excessive context and tool fanout often signal poor routing, while a very fast edit may simply skip behavior verification.

**Operating conditions and assumptions.** Task scope, target version, included fields, environment, and observations are comparable. Measure this workflow, not general agent or product performance.

**Failure boundary and alternatives.** Tool count becomes a quality target, p95 timing lacks a population, one quick edit proves efficiency, or runtime checks are omitted to save time. Bounded alternatives and recoveries: use a qualitative audit for rare changes, compare repeated similar skill edits, or measure decision ambiguity and rework.

**Counterexample, gotchas, and operational comparison.** Warm caches, network dependency latency, asset generation mixed into metadata time, and reviewer differences. Good: compare two similar edits and investigate repeated dependency probes. Bad: celebrate one tool call that copied invalid YAML. Borderline: exclude asset-generation time while reporting that boundary.

**Verification, evidence, and uncertainty.** Capture task class, sources, fields, environment, tool calls, external calls, retries, wall time, reviewer time, correctness results, and confounders. The seed directly supports workflow budgets and measurement packets. No baseline or meaningful sample is supplied.

**Second-order consequence.** Efficient metadata work minimizes irrelevant context and repeated calls while preserving every semantic gate.

**Revision decision.** Define scoped efficiency and require correctness plus activation outcomes beside timing.

**Retained seed evidence.** All original performance statements remain verbatim. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Performance method: require tool-call budgets, timeout budgets, and a resumable journal when the workflow exceeds one focused session.
Leading indicator to measure: the next task uses the reference to make a better decision with less ambiguity.
Failure signal to watch: the reference remains a source map and never becomes an operating guide.
Required measurement packet: capture input size, source count, tool-call count, wall-clock time, p50/p95/p99 latency where runtime applies, and reviewer decision time where documentation applies.
Pass condition: the reference must let a reviewer identify the correct next action, verification gate, and stop condition without reading unrelated files.
Fail condition: the reference encourages implementation before the workload, reliability target, and failure-mode table are explicit.

## Scale Boundary Statement

**Decision supported.** This section helps decide when a single-file field reference is insufficient and how bulk metadata work can avoid coupled activation errors. The seed stops at multiple systems, ownership boundaries, unbounded discovery, or production traffic but does not describe metadata-specific coordination across many skills and products.

**Recommended default and causal basis.** Split when skills have independent owners, products consume different schemas, assets or dependencies are shared, activation policies vary in risk, source discovery is unbounded, or changes cannot roll back independently. Bulk copying creates correlated discovery, resource, and dependency failures across otherwise unrelated skills.

**Operating conditions and assumptions.** Each unit has exclusive skill files, a known consumer, independent resources, validation, activation samples, and rollback. Use to decompose metadata evolution, not marketplace architecture.

**Failure boundary and alternatives.** Agents edit shared assets, templates overwrite intentional policy, products diverge, dependency rollout is unsynchronized, or merge checks only syntax. Bounded alternatives and recoveries: sequence coupled changes, version a shared template, assign asset and dependency owners, use per-skill generated validation, or escalate product-schema planning.

**Counterexample, gotchas, and operational comparison.** Parallelizing by field, global icon replacement, shared prompt text, implicit policy copied across sensitivity levels, and non-atomic product rollout. Good: split skills by owner and run per-skill activation matrices. Bad: copy one full example across a marketplace. Borderline: use a template only when optional fields, policy, and resources remain parameterized and independently verified.

**Verification, evidence, and uncertainty.** Audit ownership, products, template version, assets, dependencies, policies, validation, rollout, rollback, conflicts, and final per-skill behavior. The seed provides scale and ownership principles; metadata specifics are direct operational inference. Exact bulk thresholds depend on product and team topology.

**Second-order consequence.** Metadata scaling is coordination scaling: independence is proven by separate behavior and rollback, not file count.

**Revision decision.** Add skill/product/resource/dependency split criteria and per-skill reconciliation.

**Retained seed evidence.** The four original scale paragraphs remain verbatim. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Openai Skill Yaml Patterns stops being sufficient when the task spans multiple independent systems, more than one ownership boundary, unbounded source discovery, or production traffic without an explicit SLO.
Under distributed execution, split work by theme file and preserve one verification owner per split; do not let parallel agents rewrite the same reference without a merge checkpoint.
Under long-running agent workflows, treat context drift as a reliability failure: checkpoint state, summarize open risks, and verify against the spec before continuing.
Under large-codebase scale, require dependency or source-graph narrowing before applying this reference; a source list without ranked canonical guidance is not enough.

## Future Refresh Search Queries

**Decision supported.** This section helps decide which future searches should refresh a disputed metadata claim without mixing AGENTS.md, skill body, plugin, and image concerns. The seed's broad theme queries do not isolate current field schema, parser implementation, invocation policy, or asset constraints.

**Recommended default and causal basis.** Search by exact file path, field name, product version, and evidence type; prefer official docs, installed source, release notes, migration guides, and repository examples, then reproduce the behavior. Claim-specific queries reduce unrelated OpenAI results and reveal actual schema changes.

**Operating conditions and assumptions.** The researcher records version, domain, query, selected authority, conflict, and target observation. Queries are plans, not evidence.

**Failure boundary and alternatives.** Broad phrases return tutorials, main branch is treated as installed release, image results decide schema, or search rank means authority. Bounded alternatives and recoveries: inspect packaged files, search target history, parse a minimal example, omit the field, or retain uncertainty.

**Counterexample, gotchas, and operational comparison.** Renamed fields, product-specific config collision, stale examples, generated docs, and undocumented parser tolerance. Good: search the installed Codex source for `allow_implicit_invocation`. Bad: search 'OpenAI YAML best practices'. Borderline: use a repository example only after matching version and reproducing behavior.

**Verification, evidence, and uncertainty.** Store query, filters, date, version, source, claim, conflict, reproduction, and reference change. The seed supplies documentation, repository, and release-note categories. No searches ran under the no-browse rule.

**Second-order consequence.** Refresh should be triggered by a disputed field, product upgrade, failed test, or scheduled staleness review.

**Revision decision.** Add exact field, product, version, source, trigger, and reproduction qualifiers.

**Retained seed evidence.** The three original query rows remain verbatim. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| search_query_label_name | search_query_text_value |
| --- | --- |
| `official_docs_query_phrase` | openai skill yaml patterns official documentation best practices |
| `github_repository_query_phrase` | openai skill yaml patterns GitHub repository examples |
| `release_notes_query_phrase` | openai skill yaml patterns changelog release notes migration |

## Evidence Boundary Notes

**Decision supported.** This section helps decide how each metadata recommendation should expose provenance and applicability. The seed defines local, external, and combined inference labels but not target parser observations, runtime activation results, resource checks, conflicts, or freshness.

**Recommended default and causal basis.** Separate archived local contract, inspected external fact, target file observation, parser result, resource or dependency check, activation result, and combined inference; attach version, scope, conflict, confidence, and falsifier. A reader must know whether a field is documented, accepted, rendered, and behaviorally effective rather than collapsing those claims.

**Operating conditions and assumptions.** Every consequential claim traces to a source or observation and downstream reuse preserves labels. Apply expanded labels while retaining exact seed vocabulary.

**Failure boundary and alternatives.** An URL is evidence without inspection, parse success becomes activation proof, a screenshot becomes schema fact, or local archive guidance becomes current universal policy. Bounded alternatives and recoveries: retain separate facts, mark guidance provisional, request target evidence, omit the field, or assign a conflict owner.

**Counterexample, gotchas, and operational comparison.** Citation laundering, missing versions, expected results as observed, cached activation, and ignored negative tests. Good: label policy semantics local, parser acceptance target-observed, and safe activation inferred after samples. Bad: call the Codex repository link proof without opening it. Borderline: preserve conflicting archive and installed behavior until owner resolution.

**Verification, evidence, and uncertainty.** Audit claim type, source, version, scope, command, resource, behavior, conflict, confidence, uncertainty, and falsifier. Local source was fully read and all public rows remain unrefreshed. Current product and target skill evidence are absent.

**Second-order consequence.** Explicit evidence interfaces localize revalidation when the product schema or skill changes.

**Revision decision.** Add target, parser, resource, dependency, activation, conflict, freshness, and falsifier rules.

**Retained seed evidence.** The three original evidence bullets remain verbatim. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- `local_corpus_sourced_fact`: statements tied directly to the local source paths above.
- `external_research_sourced_fact`: statements tied to the public URLs above.
- `combined_evidence_inference_note`: synthesis that combines local and public evidence into agent guidance.
