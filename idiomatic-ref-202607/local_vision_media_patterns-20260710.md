# Local Vision Media Patterns

**Decision supported.** This section helps decide whether an image-analysis request should be served by the local Ollama vision pipeline and what preparation it must get first. The seed title names the theme without its operating claim, that reliable local vision analysis is mostly input preparation, resizing, filename sanitization, and staging, done before the model ever runs.

**Recommended default and causal basis.** Pre-resize every image to 800px longest edge, sanitize names through Python listdir and join, stage in /tmp with clean ASCII names, and keep concurrency at two to three. The source opens by naming its three handled pitfalls, oversized images causing timeouts, Unicode filenames breaking paths, and batch processing, so the theme's identity is pitfall management around a fixed local model.

**Operating conditions and assumptions.** An Ollama runtime with the configured vision model is reachable at localhost and the images are ordinary raster files. This reference operationalizes the local-vision-ollama skill's rules and does not evaluate alternative vision models.

**Failure boundary and alternatives.** The guidance is hardware-coupled, its numbers assume a 24GB M4 mini running qwen3.5:4b on Ollama, and transfer to other hosts only as a pattern, not as figures. Bounded alternatives and recoveries: cloud vision APIs when local hardware is absent, smaller resize targets when single images still time out, or raising the configured timeout for unavoidable large inputs.

**Counterexample, gotchas, and operational comparison.** Full-resolution Retina screenshots look like normal inputs and generate around 6,500 vision tokens whose O(n^2) ViT prefill will time out at the default 120 seconds. Good: a screenshot batch resized and staged before analysis. Bad: passing a 10 MB Retina capture straight to the model. Borderline: bumping the timeout to 240 seconds for one oversized diagram instead of resizing, which the source allows.

**Verification, evidence, and uncertainty.** Confirm analyzed images in a session were staged /tmp copies at or under 800px rather than original paths. The local SKILL.md states the model, runtime, hardware, four critical rules, and the token and timing figures quoted here. How the figures shift on other hardware or model versions is unaddressed by the source.

**Second-order consequence.** The skill inverts where quality effort goes, none of its rules concern prompts or model choice at analysis time, all four police the file path between disk and model.

**Revision decision.** Open with the input-preparation claim, name the four critical rules, and state the hardware and runtime the numbers assume.

**Retained seed evidence.** The exact theme title and its framing as media patterns remain unchanged. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

## Source Evidence Mapping Table

**Decision supported.** This section helps decide which recorded source may back which claim about local vision media handling. The seed map pairs the one read local row with three external URLs about AGENTS.md formats and GitHub Actions, none of which concerns local vision analysis at all.

**Recommended default and causal basis.** Cite the SKILL.md for every operational claim and treat any externally-flavored statement as inference. This document's claims are token counts, timeout figures, and filename rules from the local skill, so the map must say the external rows are generic corpus scaffolding, unretrieved and thematically off-target.

**Operating conditions and assumptions.** The hermes-skills path stays valid and the skill file keeps its four-rule structure. The table records provenance for this document's claims and does not endorse the external rows' relevance.

**Failure boundary and alternatives.** Dropping the external rows would alter the seed's table, so they stay preserved but downgraded rather than removed. Bounded alternatives and recoveries: replace the candidates with Ollama and Qwen vision documentation in a future retrieval pass, or keep the seed rows with mismatch notes.

**Counterexample, gotchas, and operational comparison.** The external rows' fact labels invite citing AGENTS.md guides for vision advice they cannot contain. Good: citing the SKILL.md for the 800px rule. Bad: citing the GitHub Actions docs for anything in this theme. Borderline: naming Ollama docs as the natural future candidate, labeled proposal-only.

**Verification, evidence, and uncertainty.** Confirm every operational claim traces to the SKILL.md and no external row is cited as fact. The mapped skill file was read in full during this evolution and no external retrieval occurred. Whether better-matched external sources exist for qwen vision behavior is unchecked.

**Second-order consequence.** The mismatch is diagnostic of template generation, the external rows repeat corpus-wide defaults, which makes the local row the only evidence surface this theme actually has.

**Revision decision.** Mark the local row as read in full and label all three external URLs unretrieved candidates whose subject matter does not match this theme.

**Retained seed evidence.** All four source rows with their category, confidence, and synthesis-role columns remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| source_location_path_key | source_category_artifact_type | source_authority_confidence_level | source_usage_synthesis_role |
| --- | --- | --- | --- |
| hermes-skills/media/local-vision-ollama/SKILL.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt |
| https://developers.openai.com/codex/guides/agents-md | external_research_source_material | external_research_sourced_fact | primary agent instruction context model |
| https://docs.github.com/actions | external_research_source_material | external_research_sourced_fact | verification and automation model |
| https://agents.md/ | external_research_source_material | external_research_sourced_fact | general agent instruction format |

## Pattern Scoreboard Ranking Table

**Decision supported.** This section helps decide which preparation habits deserve default adoption when running local vision analysis. The seed scoreboard scores corpus hygiene while the skill's own load-bearing patterns go unranked, pre-resize first, sanitize filenames through Python, stage in /tmp, and bound concurrency.

**Recommended default and causal basis.** Apply the four rules in the source's order on every analysis run, treating rule one as non-negotiable. The source numbers its rules and marks resizing as rule one with an ALWAYS, so the ranking it implies is explicit and should be transmitted.

**Operating conditions and assumptions.** Each promoted row keeps the concrete symptom it prevents, timeouts, path errors, GPU contention. The scoreboard ranks input-preparation practices and does not rank vision models or hardware.

**Failure boundary and alternatives.** The seed's numeric scores were never measured, so the promoted ordering is source emphasis, not data. Bounded alternatives and recoveries: order rows by failure frequency once measured, or collapse to a single staging script that performs all four steps.

**Counterexample, gotchas, and operational comparison.** Staging without resizing still times out, agents who copy to /tmp often believe they completed preparation. Good: a run whose transcript shows sips resize before every analysis. Bad: analysis invoked on original folder paths. Borderline: skipping the concurrency bound for a single-image job, where it cannot bind.

**Verification, evidence, and uncertainty.** Trace each promoted row to its numbered critical rule in the source. The SKILL.md numbers its four critical rules and capitalizes ALWAYS on the resize rule. Which rule violations occur most often in real sessions is unmeasured.

**Second-order consequence.** The top two rules fail differently, oversize fails loudly with a timeout while Unicode names fail confusingly with missing-file errors, so rank order also encodes debuggability.

**Revision decision.** Promote pre-resize to the top slot, filename sanitization second, /tmp staging third, and concurrency bounding fourth, marked as the source's own ordering.

**Retained seed evidence.** All three scored rows with their tier labels and failure-prevention targets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| pattern_identifier_stable_key | pattern_score_numeric_value | pattern_tier_adoption_level | pattern_failure_prevention_target |
| --- | ---: | --- | --- |
| `local_vision_media_patterns` | 95 | default_adoption_pattern_tier | Source Map First: Load local local vision material before synthesizing media patterns recommendations. |
| `local_vision_media_patterns` | 91 | default_adoption_pattern_tier | Evidence Boundary Split: Separate local facts, external facts, and inference before giving agent instructions. |
| `local_vision_media_patterns` | 88 | default_adoption_pattern_tier | Verification Gate Coupling: Attach each recommendation to at least one command, checklist, or review gate. |

## Idiomatic Thesis Synthesis Statement

**Decision supported.** This section helps decide what single orienting claim should govern local vision analysis sessions. The seed thesis repeats the load-local-first formula instead of the theme's claim, that local vision reliability is won in preprocessing, small clean staged inputs, and lost in raw inputs.

**Recommended default and causal basis.** Phrase the thesis as inputs prepared, resources bounded, config verified, with the three evidence labels kept on its clauses. Every pitfall in the source's table is an input defect, none is a model defect, so the thesis should locate reliability at the input boundary.

**Operating conditions and assumptions.** The labels stay attached so skill-derived clauses remain distinguishable from inference. The thesis orients use of this reference and does not restate the workflow steps.

**Failure boundary and alternatives.** An input-only thesis understates the config layer, the .env-over-config precedence rule is the one reliability rule that is not about inputs. Bounded alternatives and recoveries: quote the skill's pitfall-handling opening sentence verbatim, or phrase the thesis as the four rules in order.

**Counterexample, gotchas, and operational comparison.** Paraphrases keep resize and drop the filename rule, which is invisible until a macOS screenshot name breaks a path. Good: citing the thesis to demand staging before a batch run. Bad: quoting it as advice for cloud vision APIs. Borderline: compressing to resize-then-analyze for a prompt with the other clauses noted.

**Verification, evidence, and uncertainty.** Check the thesis clauses against the four critical rules and the config reference section. The source's critical rules and pitfalls table ground every clause of the restated thesis. Whether the same input-first framing holds for non-Ollama local runtimes is unknown.

**Second-order consequence.** The thesis has a cost shape, preprocessing costs seconds per image while each skipped step costs a 120-second timeout or a confusing path failure, an asymmetry that makes the default self-justifying.

**Revision decision.** Restate the combined inference as resize, sanitize, and stage every image before analysis, bound concurrency, and check .env precedence when routing misbehaves.

**Retained seed evidence.** The three labeled thesis lines with their local, external, and combined-inference structure remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`local_corpus_sourced_fact`: The local row for `local_vision_media_patterns` contains 1 source path(s), which should be treated as the first retrieval surface for this theme.
`external_research_sourced_fact`: The external source map provides public documentation, repository, or ecosystem analogues where available.
`combined_evidence_inference_note`: Reliable use of Local Vision Media Patterns comes from loading the local corpus first, checking public ecosystem guidance second, and converting both into verification-backed agent decisions.

## Local Corpus Source Map

**Decision supported.** This section helps decide which part of the local source a specific vision question should open first. The seed map records heading signals without the file's real topology, an architecture block, four numbered critical rules, a six-step workflow, a pitfalls table, a model-choice rationale, and a config reference.

**Recommended default and causal basis.** Enter through the pitfalls table when something failed and through the numbered rules when planning a run. A troubleshooting reader needs the pitfalls table while a setup reader needs the config reference, and an undifferentiated row sends both through the whole file.

**Operating conditions and assumptions.** The file remains readable at the mapped path with rules, workflow, and tables intact. The map indexes the single mapped local source and does not cover other hermes media skills.

**Failure boundary and alternatives.** The topology note goes stale if the hermes skill is revised, and no snapshot date is recorded. Bounded alternatives and recoveries: record line anchors per section, snapshot-date the mapping, or inline the precedence rule here as a quoted fact.

**Counterexample, gotchas, and operational comparison.** The config appears twice, as YAML and as .env, and the precedence sentence that reconciles them sits at the very last line of the file. Good: routing an invalid-image-source error to the Unicode pitfall row. Bad: rereading the whole file for a timeout question the awareness section answers. Borderline: answering a model-choice question from the why-qwen section alone.

**Verification, evidence, and uncertainty.** Open the mapped file and confirm the architecture, rules, workflow, pitfalls, and config sections appear as described. The mapped file was read in full, 149 lines with the topology recorded here. Whether sibling hermes media skills overlap this one is unknown until read.

**Second-order consequence.** The pitfalls table is a symptom-first inverse index of the rules, each row maps an observed failure back to the rule that prevents it, making it the fastest entry for debugging.

**Revision decision.** Annotate the row with question routing, symptom questions to the pitfalls table, procedure questions to the workflow, tuning questions to timeout awareness, and routing questions to the config reference.

**Retained seed evidence.** The single local source row with its title, heading signals, and usage role remains preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| local_source_filepath_value | local_source_title_text | local_source_heading_signals | local_source_usage_role |
| --- | --- | --- | --- |
| hermes-skills/media/local-vision-ollama/SKILL.md | local-vision-ollama | Local Vision via Ollama (qwen3.5:4b); Architecture; Critical Rules; 1. ALWAYS Pre-Resize Images Before Analysis; Single image; Batch - copy and resize all images in a folder | skill entrypoint or reusable agent prompt |

## External Research Source Map

**Decision supported.** This section helps decide how much weight external rows may carry in local vision guidance. The seed map lists AGENTS.md guides and GitHub Actions docs as external facts although none was retrieved and none addresses local vision at all.

**Recommended default and causal basis.** Rest all claims on the read local skill and treat external corroboration as absent until a targeted retrieval pass. External rows are meant to corroborate the theme, and rows about agent-instruction formats cannot corroborate token counts or resize rules.

**Operating conditions and assumptions.** Each row keeps a note naming what it could and could not confirm. The map catalogs candidate external references and does not certify content, freshness, or relevance.

**Failure boundary and alternatives.** Removing the rows would break seed preservation, so they stay with downgraded labels and a mismatch note. Bounded alternatives and recoveries: a retrieval pass against Ollama and Qwen sources, dropping the mismatched rows in a future spec revision, or leaving the table annotated as is.

**Counterexample, gotchas, and operational comparison.** The rows' authoritative names lend false weight, GitHub docs are real and authoritative, just not about this. Good: naming Ollama docs as where timeout semantics would be verified. Bad: citing agents.md for image staging advice. Borderline: using the AGENTS.md guide for generic skill-format questions, outside this theme.

**Verification, evidence, and uncertainty.** Confirm no claim cites an external row as fact and the mismatch note is present. No external retrieval was performed and the three URLs' subject matter is evident from their titles. Whether Ollama or Qwen documentation confirms the quoted figures is unknown.

**Second-order consequence.** This theme's real external anchors are implementation-defined, timeout behavior belongs to Ollama and token scaling to the Qwen ViT, so even good future retrieval must target those projects, not agent-format guides.

**Revision decision.** Downgrade all three rows to unretrieved candidates, note their topical mismatch, and name Ollama documentation and Qwen model cards as the natural replacement candidates.

**Retained seed evidence.** All three external rows with their names, roles, and boundary labels remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| external_source_url_value | external_source_name_text | external_source_usage_role | evidence_boundary_label_value |
| --- | --- | --- | --- |
| https://developers.openai.com/codex/guides/agents-md | OpenAI Codex AGENTS.md guide | primary agent instruction context model | external_research_sourced_fact |
| https://docs.github.com/actions | GitHub Actions documentation | verification and automation model | external_research_sourced_fact |
| https://agents.md/ | AGENTS.md open format | general agent instruction format | external_research_sourced_fact |

## Anti Pattern Registry Table

**Decision supported.** This section helps decide which recurring local-vision failures deserve standing detection rules. The seed registry lists corpus-hygiene failures while the source's pitfalls table names five concrete operational anti-patterns with symptoms and fixes.

**Recommended default and causal basis.** Grep session transcripts for analysis calls on non-/tmp paths and for filenames pasted from ls output. The pitfalls table is already a registry, oversized inputs, Unicode names, excess concurrency, extension mismatches, and misrouted models, each with a detection symptom.

**Operating conditions and assumptions.** Each row pairs its smell with the observable symptom the source records. The registry names operational anti-patterns with signals and does not restate full rule doctrine.

**Failure boundary and alternatives.** Copying the table verbatim would duplicate the seed content below, so the registry should add detection context, not repeat rows. Bounded alternatives and recoveries: encode staging checks in a wrapper script, keep the registry as symptom-to-rule pointers, or fold detection into the observability section.

**Counterexample, gotchas, and operational comparison.** The wrong-model pitfall produces slow or bad results rather than errors, making it the only registry row detectable by quality rather than failure. Good: catching an analysis call on an original folder path at review. Bad: retrying a timed-out full-res image unresized. Borderline: two concurrent requests on a batch job, at the source's stated bound.

**Verification, evidence, and uncertainty.** Replay each registry row against the pitfalls table and confirm its symptom is observable in a transcript. The source's five-row pitfalls table names every symptom and fix the added rows key to. Relative frequency of each pitfall in real sessions is unmeasured.

**Second-order consequence.** The most deceptive anti-pattern is typed filenames, the U+202F character is visually identical to a space in terminal output, so the error message blames a file that appears to exist on screen.

**Revision decision.** Add rows for raw-path analysis, typed-filename handling, unbounded concurrency, and unchecked .env routing, each keyed to its pitfall symptom.

**Retained seed evidence.** All three original registry rows with their causes, replacements, and detection methods remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| anti_pattern_failure_name | failure_cause_risk_reason | safer_default_replacement_pattern | detection_signal_review_method |
| --- | --- | --- | --- |
| context_free_summary_output | agent skips local corpus and produces generic advice | source_map_first_synthesis | verify every listed local path appears in the generated file |
| unsourced_recommendation_claims | guidance appears authoritative without source boundary | evidence_boundary_split_pattern | check for local, external, and inference labels |
| unverified_agent_instruction | recommendation cannot be checked by command or review gate | verification_gate_coupling | require concrete gate in generated reference |

## Verification Gate Command Set

**Decision supported.** This section helps decide which gates must pass before local vision output or this reference's guidance is trusted. The seed gate names the corpus verifier while the theme's real gates are operational, image dimensions checked after resize, staged paths confirmed, and a bounded test analysis before a batch.

**Recommended default and causal basis.** Gate every batch on dimension checks, staged-path checks, and one timed smoke analysis. The skill's reliability comes from preparation steps, so verification means proving the preparation happened, dimensions, paths, and timing.

**Operating conditions and assumptions.** Shell access to inspect staged files and time a test call is available. The gate set defines what must pass before a batch analysis is trusted and does not implement the pipeline.

**Failure boundary and alternatives.** Dimension checks prove resize but not content integrity, a corrupted copy passes the size gate. Bounded alternatives and recoveries: a wrapper script that stages, resizes, and verifies in one step, or checksum comparisons when copy integrity is in doubt.

**Counterexample, gotchas, and operational comparison.** Sips -Z mutates in place when out equals input, so a gate that reruns resize is idempotent and safe, while re-copying after resize silently restores the original. Good: a batch preceded by a 15-second smoke run. Bad: a batch launched on unmeasured images. Borderline: skipping the smoke run for a two-image job, accepted with the risk noted.

**Verification, evidence, and uncertainty.** Run the gates against a sample folder and confirm they catch an oversized and a misnamed input seeded deliberately. The source's timing figures, staging rules, and last-line config precedence note ground each added gate. The right smoke-run time threshold on other hardware is unknown.

**Second-order consequence.** The smoke run doubles as a routing gate, a single resized image that still runs slow implicates the .env model routing, catching the config pitfall before a batch amplifies it.

**Revision decision.** Add operational gates, sips or file inspection confirming 800px bounds, a staged-path check that all inputs live in /tmp with ASCII names, and a single-image smoke run timed under thirty seconds before batches.

**Retained seed evidence.** The original verification gate line and its repository verifier command block remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`verification_gate_command_set`: Run the repository verifier after editing this file.

```bash
python3 agents-used-monthly-archive/idiomatic-references-202606/tools/verify_reference_generation.py --stage final
```

## Agent Usage Decision Guide

**Decision supported.** This section helps decide when a working agent should open this reference and which section it should enter through. The seed guide keys usage to theme mentions instead of the acts that trigger it, an agent about to analyze local images, especially macOS screenshots, through a local Ollama vision model.

**Recommended default and causal basis.** Open this reference whenever local vision analysis is planned and walk the four rules before the first call. The skill exists to prevent preparation mistakes, so it must be opened before the first analysis call, not after the first timeout.

**Operating conditions and assumptions.** The runtime is Ollama-local and the inputs are files on disk rather than URLs. The guide routes readers into this reference and does not choose between local and cloud analysis.

**Failure boundary and alternatives.** Keying to every image mention would drag the skill into cloud-API or generation tasks it does not govern. Bounded alternatives and recoveries: cloud vision documentation for API-based analysis, image-generation skills for creation tasks, or direct Ollama docs for runtime administration.

**Counterexample, gotchas, and operational comparison.** Agents open the skill mid-failure and jump to the retry advice while skipping the resize rule the retry assumes. Good: opening at the workflow before batch-analyzing a screenshots folder. Bad: opening it to pick a cloud vision provider. Borderline: consulting only the pitfalls table after an unexpected timeout, acceptable with the rules read next.

**Verification, evidence, and uncertainty.** Walk a batch request and a failure scenario through the guide and confirm each lands on the intended section. The source's workflow, pitfalls, and config sections partition the entry points as described. How often analysis requests arrive mid-failure rather than at planning time is unmeasured.

**Second-order consequence.** The highest-value trigger is the screenshot folder, macOS screenshot names carry the exact Unicode character this skill's second rule exists for, so folder analysis requests are presumptively in scope.

**Revision decision.** Trigger on local image-analysis intent, route batch jobs to the workflow section, failures to the pitfalls table, and slow-or-wrong results to the config reference.

**Retained seed evidence.** The original usage line and all four guidance bullets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`agent_usage_decision_guide`: Use this reference when a task mentions this theme, one of the listed local source paths, or a nearby technology/workflow surface.

- Start with the local corpus source map.
- Prefer patterns with explicit verification gates.
- Treat external sources as freshness and ecosystem checks, not replacements for local repo conventions.
- Preserve the evidence boundary labels when reusing recommendations.

## User Journey Scenario

**Decision supported.** This section helps decide what end-to-end shape a competent local vision session should take. The seed scenario shows a builder choosing a pattern and stops before the journey the skill scripts, discover, sort, stage, resize, analyze, and bound concurrency.

**Recommended default and causal basis.** Narrate three oldest screenshots taken from raw folder to analyzed output using the source's exact example script. The source's workflow is a six-step script with example code, so the journey should walk those steps on a concrete folder rather than end at selection.

**Operating conditions and assumptions.** The folder is readable and Ollama is serving the configured model. The scenario dramatizes one representative batch-analysis journey and does not cover config setup.

**Failure boundary and alternatives.** One journey cannot cover both the happy path and the debugging path the pitfalls table serves. Bounded alternatives and recoveries: a debugging journey entering through a timeout symptom, or a config journey reconciling .env against config.yaml.

**Counterexample, gotchas, and operational comparison.** Journeys that sort by name on screenshot folders silently reorder chronology, the source sorts by mtime for exactly this case. Good: a journey ending with analyses of staged 800px copies. Bad: one ending at model invocation on raw paths. Borderline: a single-image journey that skips sorting, harmless for one file.

**Verification, evidence, and uncertainty.** Check each journey beat against the six workflow steps and confirm none is skipped silently. The source's workflow section and its analyze-three-oldest example script exactly this sequence. Typical batch sizes in real sessions are unrecorded.

**Second-order consequence.** The journey's decisive beat is discovery, using os.listdir instead of typing names determines whether the Unicode hazard exists at all downstream, everything after inherits that choice.

**Revision decision.** Extend the journey through a screenshots folder, Python discovery of Unicode names, mtime sorting, clean /tmp copies, sips resizing, a smoke run, and a bounded parallel batch.

**Retained seed evidence.** The role-based opening, starting state, decision, and trigger lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Role based opening scenario: The new contributor or agent is starting from an unfamiliar theme and deciding whether this reference is the right tool and needs a reference that turns source evidence into an executable next step.
Primary user starting state: The user has a `local_vision_media_patterns` task, one or more local source paths, and uncertainty about which pattern should drive implementation.
Decision being made: choosing what to load, what to trust, what to avoid, and what evidence proves success.
Reference opening trigger: Open this file when the task mentions local vision media patterns, any mapped local source path, or an adjacent workflow with the same failure mode.

## Decision Tradeoff Guide

**Decision supported.** This section helps decide how strictly the preparation rules bind for a given job and what being wrong costs. The seed guide keys adopt, adapt, and avoid to generic evidence agreement instead of this theme's variables, image size, filename origin, batch volume, and hardware headroom.

**Recommended default and causal basis.** Apply all four rules unless the image is verified under the size threshold, and never skip filename sanitization for macOS-originated files. The skill's rules bind conditionally in only one direction, small clean single images tolerate shortcuts while large batches of screenshots tolerate none.

**Operating conditions and assumptions.** Image dimensions and name origins are checkable before the strictness decision. The guide calibrates preparation strictness per job and cannot waive the timeout physics.

**Failure boundary and alternatives.** Judging images small by eye fails, dimensions and file size need checking because Retina captures look ordinary. Bounded alternatives and recoveries: always-full-preparation as a simpler policy, a wrapper script that removes the decision, or escalation when hardware differs from the documented host.

**Counterexample, gotchas, and operational comparison.** Being wrong costs a timeout at minimum and a misdiagnosed session at worst, a Unicode path error reads like a missing file and sends agents hunting the wrong bug. Good: full preparation for a twelve-screenshot batch. Bad: raw-path analysis because the images seemed small. Borderline: skipping staging for one hand-named ASCII file, accepted with dimensions verified.

**Verification, evidence, and uncertainty.** Audit recent sessions for preparation level against job shape and check failures for skipped rules. The source's timing figures and pitfall symptoms define both sides of the tradeoff. The true size threshold below which preparation is safely skippable is unmeasured.

**Second-order consequence.** The source prices the tradeoff numerically, ten to twenty seconds prepared versus ninety to one-twenty unprepared, so adaptation decisions can be made by arithmetic rather than taste.

**Revision decision.** Rekey adopt to full four-rule preparation for batches and screenshots, adapt to reduced ceremony for single verified-small images, and avoid to using this skill for cloud APIs or generation.

**Retained seed evidence.** The Adopt when, Adapt when, Avoid when, and Cost of being wrong rows with their verification prompts remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| decision_option_name | when_to_choose_condition | tradeoff_cost_description | verification_question_prompt |
| --- | --- | --- | --- |
| Adopt when | local corpus and external evidence agree on the local vision media patterns pattern | fastest path, but can copy stale local assumptions | Does the selected pattern appear in the canonical source and current external evidence? |
| Adapt when | local sources are strong but public ecosystem guidance has changed | preserves repo fit, but requires explicit inference notes | Did the reference label the local fact, external fact, and combined inference separately? |
| Avoid when | source evidence is thin, conflicting, or unrelated to the user journey | prevents false confidence, but may require deeper research | Is there a confidence warning or adjacent reference route? |
| Cost of being wrong | wrong local vision media patterns guidance can send an agent to the wrong files, tests, or abstraction | wasted implementation loop and weaker verification | Would a reviewer know what to undo and what to inspect next? |

## Local Corpus Hierarchy

**Decision supported.** This section helps decide which local file outranks which when local vision guidance conflicts or runs out. The seed hierarchy names one canonical source with a thin-corpus warning and does not situate it, this is a hermes-skills media skill whose siblings and config files form its actual neighborhood.

**Recommended default and causal basis.** Consult the skill first, check the live config files it names when routing misbehaves, and mark sibling skills unread. Questions this file cannot answer, other media types, hermes config semantics, go to its directory neighbors, so the hierarchy should record the neighborhood even unread.

**Operating conditions and assumptions.** The hermes-skills tree remains at its current path. The hierarchy ranks local retrieval priority for this theme and does not certify unread files.

**Failure boundary and alternatives.** Naming unread neighbors as supporting sources would fabricate authority, they are discovery targets only. Bounded alternatives and recoveries: a follow-up pass reading sibling media skills, inlining the config excerpts as dated quotes, or leaving the single-row hierarchy with its warning.

**Counterexample, gotchas, and operational comparison.** The config excerpts in the skill can drift from the user's actual files, and the skill itself warns the .env overrides what config.yaml shows. Good: escalating a routing question from the skill's excerpt to the live .env. Bad: quoting an unread sibling skill as doctrine. Borderline: citing the config excerpt as the expected shape while noting drift risk.

**Verification, evidence, and uncertainty.** Confirm the mapped path exists and the config paths the skill names are recorded as external-to-repo. The source names its config locations explicitly and sits alone in its media subdirectory as mapped. Whether other hermes skills share or contradict these staging conventions is unknown until read.

**Second-order consequence.** Part of this skill's doctrine lives outside the repository entirely, in the user's ~/.hermes config and .env, so the canonical file is authoritative about rules but only descriptive about live configuration.

**Revision decision.** Keep the skill canonical, record the hermes-skills media directory and the referenced config files as unread discovery surfaces, and retain the confidence warning.

**Retained seed evidence.** The classification vocabulary line, the confidence warning, and the single hierarchy row with its reviewer question remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Classification vocabulary includes canonical, supporting, legacy, duplicate, and conflicting source roles.
Confidence warning: only one local corpus source is mapped, so this reference should invite adjacent-source discovery before becoming canonical policy.

| local_source_filepath_value | corpus_hierarchy_role | heading_signal_to_convert | reviewer_question_to_answer |
| --- | --- | --- | --- |
| hermes-skills/media/local-vision-ollama/SKILL.md | canonical primary source | Local Vision via Ollama (qwen3.5:4b); Architecture; Critical Rules | What guidance, warning, or example should this source contribute to Local Vision Media Patterns? |

## Theme Specific Artifact

**Decision supported.** This section helps decide what concrete evidence object must exist before this reference counts as operational. The seed artifact names a lifecycle diagram while this theme's operational artifact is a staging manifest, the mapping from original Unicode-named files to clean resized /tmp copies with their dimensions.

**Recommended default and causal basis.** Carry one filled manifest from a real screenshot batch as the reviewable instance. Every rule in the skill produces or protects that mapping, so evidence of correct operation is the manifest plus the analysis outputs keyed to it.

**Operating conditions and assumptions.** The manifest records dimensions after resizing, not before, and timings per analysis call. The artifact certifies this reference is operational and does not grade analysis quality.

**Failure boundary and alternatives.** Manifests for one-off single images are ceremony, the null-instance convention applies. Bounded alternatives and recoveries: a compressed manifest for small jobs, the manifest embedded in session notes, or a wrapper script that emits it automatically.

**Counterexample, gotchas, and operational comparison.** Manifests reconstructed after the fact lose the original names, the discovery script should print them at copy time as the source's example does. Good: a manifest showing three originals with escaped names mapped to timed analyses. Bad: analysis outputs with no record of what was analyzed. Borderline: a manifest without timings for a job where nothing was slow.

**Verification, evidence, and uncertainty.** Check the artifact maps every analyzed output back to an original file and shows sub-threshold dimensions. The source's example script already prints index, repr name, and staged path, the manifest's exact seed. Whether manifest discipline measurably reduces rework is untested here.

**Second-order consequence.** The repr-escaped original name is the manifest's forensic core, it is the only place the invisible U+202F character becomes visible evidence rather than a silent hazard.

**Revision decision.** Define the artifact as one staging manifest, original path with repr-escaped name, staged path, post-resize dimensions, analysis timing, and result pointer per image.

**Retained seed evidence.** The artifact definition line and the three artifact field rows with completion rules remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Theme specific artifact: worked local vision media patterns example with user goal, decision point, failure mode, and verification gate.

| artifact_field_name | artifact_completion_rule | evidence_source_hint |
| --- | --- | --- |
| user_goal_statement | state the user's concrete goal before applying Local Vision Media Patterns | local corpus hierarchy plus critique findings |
| decision_boundary_rule | define the point where this reference should be used or avoided | decision tradeoff guide |
| verification_gate_rule | define the command, checklist, or review question that proves the artifact worked | verification gate command set |

## Worked Example Set

**Decision supported.** This section helps decide which session behaviors should be taught as exemplary, negligent, or conditionally acceptable. The seed examples restate corpus verdicts and never grade real conduct, a prepared batch, a raw-path failure, or a justified timeout bump.

**Recommended default and causal basis.** Grade every example by whether preparation preceded analysis and whether retries changed the input rather than just repeating it. The source teaches through commands and symptoms, so graded examples should be command-shaped with observable outcomes.

**Operating conditions and assumptions.** Each example names its observable outcome, timing, error, or clean result. The examples grade preparation conduct, not the quality of the model's descriptions.

**Failure boundary and alternatives.** Examples fixed to this hardware's numbers mislead on other hosts, so verdicts should cite the pattern, not the milliseconds. Bounded alternatives and recoveries: draw examples from recorded sessions, add a Unicode-failure example with its exact error text, or grade the source's own batch script.

**Counterexample, gotchas, and operational comparison.** The borderline timeout bump is legitimate only after resizing has been tried, the source offers 600px before suggesting config changes. Good: discovery, staging, resize, then analysis in the source's order. Bad: an unresized retry after a timeout. Borderline: timeout raised to 240 after a 600px resize still failed, per the source's escalation path.

**Verification, evidence, and uncertainty.** Scan each verdict against the rules and confirm the graded behavior is visible in a command transcript. The source's example scripts, retry advice, and timeout escalation ground all three verdicts. Which negligent shape dominates real sessions is unmeasured.

**Second-order consequence.** The bad example is a doubled loss, an unresized retry spends another full timeout window to reproduce the same failure, which is why the source's retry advice says resize smaller, then retry.

**Revision decision.** Recast good as the source's three-oldest script followed by resized staged analysis, bad as retrying a timed-out full-res image without resizing, and borderline as raising the timeout to 240 for a legitimately dense diagram.

**Retained seed evidence.** The good, bad, and borderline example lines with their original verdict framing remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Good example: Use Local Vision Media Patterns after loading the canonical source, confirming the external evidence boundary, and writing a verification gate before implementation.
Bad example: Use Local Vision Media Patterns as a generic tutorial while ignoring the mapped local paths, source hierarchy, and cost of being wrong.
Borderline case: Use Local Vision Media Patterns only after adding a confidence warning when local evidence is thin or conflicts with current ecosystem guidance.

## Outcome Metrics and Feedback Loops

**Decision supported.** This section helps decide which observable signals should trigger revising preparation practice or this reference. The seed metrics name lead time and generic signals without this theme's observables, timeout rate per batch, resize compliance, and analysis seconds per image.

**Recommended default and causal basis.** Record timing per analysis call and review the trend when any call exceeds twice the expected band. The skill's promise is numeric, ten to twenty seconds per prepared image, so its health check is comparing observed timings against that band.

**Operating conditions and assumptions.** Sessions can capture call timings cheaply. The metrics gauge pipeline health, not description accuracy, which needs human grading.

**Failure boundary and alternatives.** Timing metrics conflate model load, first calls after idle include load time and read as false alarms. Bounded alternatives and recoveries: sampled session audits, wrapper-emitted timing logs, or timeout-only tracking at first.

**Counterexample, gotchas, and operational comparison.** A zero-timeout record can mean good preparation or tiny inputs, so compliance ratios are the independent check. Good: investigating a batch averaging forty seconds per image. Bad: ignoring timings until a hard timeout. Borderline: skipping metrics for a single-image session, noted.

**Verification, evidence, and uncertainty.** Reconcile recorded timings against the source's expected band and check outliers for skipped preparation. The seed's lead-time indicator and the source's timing figures anchor the trend metrics. Expected bands on hardware other than the documented M4 host are unknown.

**Second-order consequence.** Seconds-per-image is a drift detector for the whole stack, a slow creep implicates model routing or host load before outright failures appear, catching the wrong-model pitfall early.

**Revision decision.** Adopt per-batch timeout counts, staged-versus-raw path ratios, and a seconds-per-image trend as primary signals alongside the seed's indicator.

**Retained seed evidence.** The leading indicator, failure signal, and review cadence lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Leading indicator: the next task uses the reference to make a better decision with less ambiguity.
Failure signal: the reference remains a source map and never becomes an operating guide.
Review cadence: Re-run the verifier after every generated-reference edit and refresh external sources when public APIs, docs, or tooling releases change.

## Completeness Checklist

**Decision supported.** This section helps decide when this reference may be declared ready to hand to an agent. The seed checklist confirms generic sections exist and never checks this document's specific obligations, all four critical rules present, the six workflow steps ordered, the five pitfalls represented, and the config precedence rule preserved.

**Recommended default and causal basis.** Tick structural items with citations, then grep this document for each rule, pitfall, and the precedence clause. This document transmits an operational skill, so readiness means the rules, workflow, pitfalls, and precedence sentence survived transmission intact.

**Operating conditions and assumptions.** Each added item names its target and whether a script or human verifies it. The checklist gates this document's readiness, not the pipeline's runtime health.

**Failure boundary and alternatives.** A reference that dropped the .env-precedence rule would pass a section check while omitting the fact the source saves for its final line. Bounded alternatives and recoveries: generate coverage items from the source's headings, deep-check two random items per review, or pair-review the manifest artifact.

**Counterexample, gotchas, and operational comparison.** Rule presence can pass while numbers drifted, the 800px and 120s figures deserve a spot-check against the source. Good: a tick citing the line carrying the precedence rule. Bad: all ticks green from a headings glance. Borderline: carrying forward last cycle's figure check with a staleness note.

**Verification, evidence, and uncertainty.** Grep this document for the rules, pitfalls, figures, and precedence clause, then spot-read two against the source. The seed's seven structural items map onto real sections here and anchor the added fidelity layer. How much spot-reading each cycle needs depends on edit volume.

**Second-order consequence.** The precedence rule is the checklist's canary, it is the fact most likely to be dropped in summarization because it lives at the file's end and contradicts the more visible YAML block.

**Revision decision.** Append items requiring the four rules named, the workflow steps ordered, the pitfalls table reachable, and the precedence rule quoted or pointed to.

**Retained seed evidence.** All seven structural checklist items covering scenario, decision guide, hierarchy, artifact, examples, metrics, and routing remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- The role scenario names the user, starting state, decision, and trigger for Local Vision Media Patterns.
- The decision guide includes Adopt when, Adapt when, Avoid when, and Cost of being wrong.
- The local corpus hierarchy identifies canonical and supporting sources or gives a confidence warning.
- The theme specific artifact is concrete enough to review without reading every mapped source.
- The examples cover good, bad, and borderline usage.
- The metrics section names one leading indicator and one failure signal.
- The adjacent routing section points to a better reference when this one is not the right fit.

## Adjacent Reference Routing

**Decision supported.** This section helps decide when a question should leave this reference and which neighbor owns it. The seed routing splits the theme name into keywords aimed at unnamed destinations instead of routing by need, generation questions to the image-generation reference and skill-authoring questions to authoring references.

**Recommended default and causal basis.** Ask whether the image is input or output, route output questions to the generation reference, and keep input questions here. Readers confuse analysis with generation, and this corpus already evolved an image-generation reference that owns the creation side of media work.

**Operating conditions and assumptions.** Each route names its trigger, a destination resolving to a real file, and what stays here. Routing redirects within this corpus and cannot authorize work in a destination's domain.

**Failure boundary and alternatives.** Keyword routes point at references that exist only as words, stranding the reader who follows them. Bounded alternatives and recoveries: consult the corpus index before adding routes, keep unresolved needs here with a gap note, or escalate genuine overlap to the user.

**Counterexample, gotchas, and operational comparison.** Edit requests blur the direction test, an image goes in and comes out, and those belong to the generation reference's edit doctrine, not here. Good: sending a style-prompt question to the generation reference. Bad: routing to the media adjacent reference, a keyword with no file. Borderline: an OCR-then-redraw request split across both references with the seam named.

**Verification, evidence, and uncertainty.** Resolve each named destination to an existing corpus file and walk one sample question through each trigger. The image generation prompt patterns reference was completed earlier in this same queue and covers the outbound direction. Whether future media themes will redraw this input-output split is unknown.

**Second-order consequence.** The media split in this corpus mirrors data direction, this file owns images flowing into models and the generation reference owns images flowing out, a one-question routing test.

**Revision decision.** Route image-creation and editing questions to the image generation prompt patterns reference, keep analysis, staging, and local-runtime questions here, and record unowned needs as gaps.

**Retained seed evidence.** The adjacency guidance line and the three keyword-derived route stubs remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Adjacent reference guidance: Use the nearest language, workflow, agent, or documentation reference when the theme becomes concrete.
Adjacent reference 1: consider the local adjacent reference when the current task pivots away from local vision media patterns.
Adjacent reference 2: consider the vision adjacent reference when the current task pivots away from local vision media patterns.
Adjacent reference 3: consider the media adjacent reference when the current task pivots away from local vision media patterns.

## Workload Model

**Decision supported.** This section helps decide how much analysis work one session may take on before splitting or throttling. The seed model bounds endpoints per batch but not this theme's working unit, images per staged batch with a concurrency ceiling the source sets at two to three.

**Recommended default and causal basis.** Stage the whole batch up front, analyze two at a time, and split sessions when batches grow beyond easy manifest review. The binding resource is GPU memory and contention on a single local host, which the source prices as OOM or extreme slowdown beyond two concurrent requests.

**Operating conditions and assumptions.** One local GPU host serves all requests and timings are observable. The model bounds analysis throughput per session and does not bound the corpus documentation work.

**Failure boundary and alternatives.** The ceiling is hardware-specific, other hosts may sustain more or fewer concurrent analyses. Bounded alternatives and recoveries: strictly serial processing for reliability, host-specific ceilings once measured, or chunked sessions with manifest handoffs.

**Counterexample, gotchas, and operational comparison.** Batch staging tempts unbounded folders, staging two hundred screenshots produces a manifest nobody reviews and a session nobody finishes. Good: a twelve-image batch staged once and analyzed two at a time. Bad: eight concurrent calls on a 24GB host. Borderline: three concurrent on small images, the top of the source's stated range.

**Verification, evidence, and uncertainty.** Compare per-image timings across concurrency levels on the actual host and record where slowdown begins. The source's workflow step six and pitfalls table state the two-to-three bound and the OOM symptom. The exact contention curve on the documented hardware is unmeasured beyond the source's bound.

**Second-order consequence.** Concurrency here buys less than it seems, analysis is GPU-bound on one device, so parallel calls mostly interleave, and the third concurrent request risks OOM for near-zero throughput gain.

**Revision decision.** Rebound the model around staged batches of modest size, two concurrent analyses as the default ceiling, and per-image timing as the split signal.

**Retained seed evidence.** The four workload dimensions with their boundary values and verification pressure points remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`combined_evidence_inference_note`: Treat Local Vision Media Patterns as a creative artifact operating reference, not as a prose summary.

| workload_dimension_name | workload_boundary_value | verification_pressure_point |
| --- | --- | --- |
| primary_usage_surface | creative generation, visual artifact, diagram, or media workflow where correctness includes observable output quality | verify that the reference changes the next implementation or review action |
| bounded_capacity_model | one artifact family, three representative variants, one accessibility/readability pass, and one render verification path | split the task or create a narrower reference when this boundary is exceeded |
| source_pressure_model | local heading signals include Local Vision via Ollama (qwen3.5:4b); Architecture; Critical Rules; 1. ALWAYS Pre-Resize Images Before Analysis; Single image; Batch - copy and resize | compare guidance against canonical local sources before following external examples |
| artifact_pressure_model | required artifact is worked local vision media patterns example with user goal, decision point, failure mode, and verification gate | require the artifact before claiming the reference is operationally usable |

## Reliability Target

**Decision supported.** This section helps decide what measurable reliability this reference must demonstrate before its guidance is trusted. The seed table demands unmeasured percentages while this theme supports binary targets, zero analyses on raw paths and zero unresized inputs above the threshold reaching the model.

**Recommended default and causal basis.** Keep the four seed dimensions with methods attached and lead with the two per-call scans. The preparation rules are checkable per call, an input either was staged and resized or was not, so targets can be scanned rather than sampled.

**Operating conditions and assumptions.** Each target names its metric, scan method, population, owner, and corrective action. The targets judge this reference and the preparation discipline, not the model's descriptive accuracy.

**Failure boundary and alternatives.** Quoting the seed's percentages as achieved performance manufactures rigor this corpus never earned. Bounded alternatives and recoveries: wrapper enforcement instead of scanning, sampled manifest audits, or postmortems per timeout instead of rates.

**Counterexample, gotchas, and operational comparison.** A staged path does not prove resizing happened, the two scans are independent and both needed. Good: a session scan showing all calls on staged paths. Bad: reporting the seed's 18-of-20 nobody sampled. Borderline: one raw-path call on a verified-small image, recorded as an accepted deviation.

**Verification, evidence, and uncertainty.** Scan one session's transcript for both targets and record hits with resolutions. The source's staging and resize rules give the operational definitions the scans check. No baseline exists for either target, so the first scanned session defines achievability.

**Second-order consequence.** Path-based targets are self-auditing, the /tmp naming convention makes compliance visible in any transcript grep without tooling.

**Revision decision.** Add binary targets, every analysis call uses a staged /tmp path and every staged image measures at or under the resize bound, each marked unbaselined and owned.

**Retained seed evidence.** All four reliability rows with their threshold values and evidence-collection methods remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| reliability_target_name | measurable_threshold_value | evidence_collection_method |
| --- | --- | --- |
| source_boundary_preservation | 100 percent of recommendations keep local, external, and inference boundaries visible | review generated text for the three evidence labels before reuse |
| decision_accuracy_sample | at least 18 of 20 sampled uses route to the correct adopt, adapt, avoid, or adjacent-reference decision | sample downstream tasks and record reviewer verdicts |
| unsupported_claim_rate | zero unsupported production, security, latency, or reliability claims in final guidance | reject claims without source row, explicit inference note, or verification method |
| recovery_path_clarity | every avoid or failure case names the rollback, escalation, or next-reference route | inspect failure-mode and adjacent-routing sections together |

## Failure Mode Table

**Decision supported.** This section helps decide which failures in the local vision pipeline deserve standing mitigations. The seed table carries hygiene and traffic rows and omits how this pipeline actually fails, timeouts from oversize, path errors from Unicode, OOM from concurrency, and misrouting from config drift.

**Recommended default and causal basis.** Map any observed symptom through the pitfalls table first, and check .env routing whenever results are slow or poor without errors. The source's pitfalls table already names symptom, cause, and fix, so the failure table should adopt those rows with blast radius and containment added.

**Operating conditions and assumptions.** Each row names its trigger, earliest observable signal, blast radius, containment, and correction. The table covers pipeline-operation failures, while documentation-process failures stay with the seed rows.

**Failure boundary and alternatives.** Rows tuned to this host's symptoms may mislabel failures on different hardware or Ollama versions. Bounded alternatives and recoveries: wrapper checks that pre-empt the loud failures, periodic .env-versus-config audits for the quiet one, or timing trends as the catch-all.

**Counterexample, gotchas, and operational comparison.** The config-drift failure produces plausible outputs from the wrong model, the only row where the failure can pass unnoticed through an entire session. Good: a slow-result session diagnosed by checking .env first, per the source's last line. Bad: a timeout retried without any input change. Borderline: an OOM on the third concurrent call, at the boundary the source warns about.

**Verification, evidence, and uncertainty.** Seed one failure per row in a drill and confirm the named signal fires and maps to the right fix. The source's pitfalls table and its closing check-.env-first sentence supply every added row. Failure frequencies and their hardware sensitivity are unmeasured.

**Second-order consequence.** The four failures sort by honesty, timeouts and path errors announce themselves, OOM announces the wrong thing, and config drift announces nothing, so detection investment should run in reverse order of loudness.

**Revision decision.** Add timeout, path-error, GPU-OOM, and config-drift rows, each with its source-named symptom, earliest signal, and fix.

**Retained seed evidence.** All four seed failure rows with their triggers and mitigation actions remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| failure_mode_name | likely_trigger_condition | required_mitigation_action |
| --- | --- | --- |
| source drift hides truth | external or local guidance changes after the reference was written | refresh public evidence, rerun local corpus gate, and mark stale claims before reuse |
| generic advice escapes review | agent copies plausible best practices without theme-specific verification | block completion until the verification gate names concrete command, reviewer question, or metric |
| rendered output not inspected | textual description passes while the actual asset is blank, clipped, or unreadable | open or screenshot the artifact and verify pixels, layout, and intended state |
| variant search becomes random | generation explores without preserving acceptance criteria | score variants against prompt constraints and retain the chosen rationale |

## Retry Backpressure Guidance

**Decision supported.** This section helps decide when a failing pipeline call should be retried, downgraded, or escalated. The seed bullets classify verification failures generically and never carry this theme's retry rule, a timed-out image is retried smaller, not merely again.

**Recommended default and causal basis.** For pipeline failures, apply the matching downgrade before any retry, and for reference work keep the seed's one-bounded-retry-then-escalate rule. The source's retry advice mutates the input, resize to 600px then retry, because repeating an unchanged oversized input deterministically reproduces the timeout.

**Operating conditions and assumptions.** The failing condition is identifiable from the symptom before the retry is chosen. This governs both retrying pipeline calls and retrying reference-verification work, kept as two labeled layers.

**Failure boundary and alternatives.** Input-mutation retries apply to size failures, not to path errors, whose fix is re-staging rather than resizing. Bounded alternatives and recoveries: serialization instead of retry for OOM, timeout config increases after resize options are exhausted, or escalation when failures persist across downgrades.

**Counterexample, gotchas, and operational comparison.** Backpressure here is physical, hammering a contended GPU with retries worsens the contention that caused the failure. Good: a 600px resize before the second attempt at a timed-out image. Bad: three identical retries of an unchanged input. Borderline: a timeout bump to 240 after both resize steps failed, the source's sanctioned last resort.

**Verification, evidence, and uncertainty.** Audit retry sequences for input or condition changes between attempts and check verification reruns stayed within the bounded-retry rule. The source's timeout section prescribes resize-smaller-and-retry and offers the config bump as the explicit fallback. How often persistent failures survive all downgrades is unmeasured.

**Second-order consequence.** Every legitimate retry in this skill is a downgrade of demand, smaller input, cleaner path, less concurrency, which makes retry-without-change detectable as a rule violation by diffing the two attempts.

**Revision decision.** Add the pipeline-layer rule, retries must change the failing condition, smaller image for timeouts, restaged path for name errors, fewer concurrent calls for OOM, with the config bump as the last resort.

**Retained seed evidence.** All five retry and backpressure bullets, including the one-owner-per-file rule, remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- Retry only after the failed verification signal is classified as transient, stale evidence, missing context, or true contradiction.
- Use one bounded retry for stale external evidence refresh, then escalate to a human or a narrower source-specific reference.
- Apply backpressure by stopping new generation or implementation work when source coverage, critique coverage, or verification gates are red.
- For long-running agent workflows, checkpoint after each batch and re-read the current spec before any broad rewrite, commit, push, or destructive operation.
- For distributed execution, assign one owner per generated file or theme batch and require merge-time verification of exact path, heading, and evidence-boundary invariants.

## Observability Checklist

**Decision supported.** This section helps decide what evidence must exist that an analysis session happened as claimed. The seed bullets recycle generic evidence records and never name this theme's evidence stream, the staging manifest, per-call timings, and the config snapshot in effect.

**Recommended default and causal basis.** Record per session the manifest, timings, verbatim errors, and the effective vision config, keeping raw model outputs summarized. The artifact section defines the manifest and the metrics section the timings, so observability means persisting both plus the routing config that determined which model ran.

**Operating conditions and assumptions.** Sessions can persist small text records alongside their outputs. This covers observing analysis sessions, not the Ollama server's own logs.

**Failure boundary and alternatives.** Full manifest retention for every trivial call outgrows its value, the null-instance convention applies. Bounded alternatives and recoveries: wrapper-emitted logs, config snapshots only on failure, or sampled retention for high-volume sessions.

**Counterexample, gotchas, and operational comparison.** Error texts paraphrased lose the diagnostic character, the Unicode failure is identifiable only by its exact wording. Good: a session record with manifest, timings, and the .env values used. Bad: analysis conclusions with no record of inputs or model. Borderline: a null-instance record for one small ASCII-named image.

**Verification, evidence, and uncertainty.** Spot-check session records for the manifest, timing, and config fields and confirm errors are verbatim. The seed's small-audit-evidence preference and the source's check-.env-first rule anchor the config-snapshot requirement. The retention horizon for session records is untuned.

**Second-order consequence.** The config snapshot is the evidence most often missing when it matters, routing bugs are diagnosed by knowing which model actually served the call, which nothing else in the session records.

**Revision decision.** Recenter the checklist on session evidence, the manifest, call timings, error texts verbatim, and the AUXILIARY_VISION values in effect at run time.

**Retained seed evidence.** All six observability bullets including the small-audit-evidence preference remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- Record which local sources were loaded and which were intentionally skipped.
- Record the exact verification command, reviewer question, or rendered artifact used as proof.
- Record p50/p95/p99 latency or reviewer-time measurements when the reference affects runtime or workflow speed.
- Capture reviewer decision, unresolved uncertainty, and next refresh trigger.
- Record leading indicator and failure signal from this file in the coverage manifest or journal when the reference drives real work.
- Keep audit evidence small enough to review: command output summary, changed-file list, and unresolved-risk notes are preferred over raw transcript dumps.

## Performance Verification Method

**Decision supported.** This section helps decide how to prove the preparation discipline is buying the speedup it claims. The seed method fixes handler latency numbers while this theme's performance question is concrete and local, do prepared images process inside the ten-to-twenty-second band the source promises.

**Recommended default and causal basis.** Run the paired test once per new host or model version and log routine timings against the resulting local band. The skill quantifies its own benefit, roughly 6,500 tokens down to 600 and ninety-plus seconds down to twenty, so verification means reproducing that ratio on the actual host.

**Operating conditions and assumptions.** Timing capture is available and one sacrificial raw-image run is acceptable. This evaluates the preparation discipline's timing benefit, not model output quality.

**Failure boundary and alternatives.** The band was measured on one host and model version, and divergence may indicate hardware difference rather than regression. Bounded alternatives and recoveries: band-only monitoring without the paired test, token-count inspection where the runtime exposes it, or reviewer-time metrics for the documentation layer.

**Counterexample, gotchas, and operational comparison.** The raw half of the paired test may simply time out, which is itself the measurement, record it as the timeout bound rather than a failure. Good: a paired test logging 110 seconds raw versus 14 prepared. Bad: quoting the source's figures as this host's performance. Borderline: adopting the source band unverified on identical-spec hardware, noted as assumed.

**Verification, evidence, and uncertainty.** Execute the paired measurement and publish both timings with the host and model version. The source states the token counts and both timing bands the paired test reproduces. How the band shifts across Ollama releases and quantizations is unknown.

**Second-order consequence.** One paired measurement is the highest-information test, the same image analyzed raw and prepared yields the local speedup ratio directly and validates the entire doctrine in two calls.

**Revision decision.** Measure per-image seconds for prepared inputs, compare against the source band, and re-baseline when hardware or model versions change, keeping the seed's latency defaults as the absent-SLO fallback.

**Retained seed evidence.** The performance method line, both indicator lines, the measurement packet, and the pass and fail conditions remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Performance method: require rendered-output inspection and reject text-only claims when the artifact is inherently visual or interactive.
Leading indicator to measure: the next task uses the reference to make a better decision with less ambiguity.
Failure signal to watch: the reference remains a source map and never becomes an operating guide.
Required measurement packet: capture input size, source count, tool-call count, wall-clock time, p50/p95/p99 latency where runtime applies, and reviewer decision time where documentation applies.
Pass condition: the reference must let a reviewer identify the correct next action, verification gate, and stop condition without reading unrelated files.
Fail condition: the reference encourages implementation before the workload, reliability target, and failure-mode table are explicit.

## Scale Boundary Statement

**Decision supported.** This section helps decide at what scale this pipeline stops sufficing and what structure replaces it. The seed statement recites multi-system limits and misses this theme's scale walls, batch sizes beyond manifest review, sustained volume beyond one GPU host, and image types beyond the raster screenshots the doctrine assumes.

**Recommended default and causal basis.** Serve occasional batches within the ceiling, queue overflow serially, and flag sustained saturation as a hardware or architecture decision above this reference. The pipeline is a single-host, single-model design, its concurrency ceiling and timeout budget define a throughput wall that no preparation discipline moves.

**Operating conditions and assumptions.** Demand is observable enough to distinguish bursts from sustained load. The boundaries bound this reference and its pipeline, not local vision as a technique.

**Failure boundary and alternatives.** Scaling advice beyond one host is out of the source's scope and would be pure inference here. Bounded alternatives and recoveries: a second host once sustained saturation is proven, cloud fallback for overflow with its own doctrine, or scheduled batch windows to shape demand.

**Counterexample, gotchas, and operational comparison.** Video and PDF inputs look adjacent but break the staging assumptions silently, frame extraction and rasterization are separate problems this doctrine does not cover. Good: queueing a burst of thirty images serially overnight. Bad: promising real-time analysis at sustained high volume on one host. Borderline: rasterizing a short PDF to pages before staging, adjacent but explicitly out of doctrine.

**Verification, evidence, and uncertainty.** Track backlog and saturation against the ceiling and confirm out-of-scope input types are flagged rather than improvised. The source's hardware line, concurrency bound, and timeout budget together define the throughput wall. The sustained-load point at which queueing becomes unacceptable is unmeasured.

**Second-order consequence.** The natural scale response is queueing rather than parallelism, throughput at the ceiling is fixed, so growth changes waiting time first, which makes backlog length the earliest scale signal.

**Revision decision.** Add scale signals, batches outgrowing single-session review, sustained demand saturating the two-call ceiling, and non-raster or non-file inputs the staging rules cannot serve.

**Retained seed evidence.** All four scale boundary statements including the distributed split and context-drift rules remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Local Vision Media Patterns stops being sufficient when the task spans multiple independent systems, more than one ownership boundary, unbounded source discovery, or production traffic without an explicit SLO.
Under distributed execution, split work by theme file and preserve one verification owner per split; do not let parallel agents rewrite the same reference without a merge checkpoint.
Under long-running agent workflows, treat context drift as a reliability failure: checkpoint state, summarize open risks, and verify against the spec before continuing.
Under large-codebase scale, require dependency or source-graph narrowing before applying this reference; a source list without ranked canonical guidance is not enough.

## Future Refresh Search Queries

**Decision supported.** This section helps decide which future searches would genuinely refresh this reference's external evidence. The seed query table drops the internal theme name into three templates whose literal phrasing targets a coinage no external author uses.

**Recommended default and causal basis.** Search Ollama and Qwen release channels on a periodic trigger, feeding the architecture figures and the timing bands. Useful refresh queries speak the ecosystem's vocabulary, Ollama vision model documentation, Qwen VL model updates, vision token scaling, not this corpus's file-naming scheme.

**Operating conditions and assumptions.** Each query names its target section, source type, and firing trigger. The queries refresh external analogues for this theme, while the local skill changes only through repository edits.

**Failure boundary and alternatives.** Empty results from a coinage query logged as freshness confirmed convert search blindness into false confidence. Bounded alternatives and recoveries: follow Ollama's changelog directly once retrieval is authorized, track the Qwen model cards, or drive refresh from dated retrieval records.

**Counterexample, gotchas, and operational comparison.** Vision-model search results skew toward cloud API content whose token economics differ from local inference. Good: an Ollama release-notes query feeding the timeout section. Bad: searching the literal theme title and logging zero hits as freshness. Borderline: adopting a practitioner benchmark post with an inference label pending corroboration.

**Verification, evidence, and uncertainty.** Run each query once, grade the top results for local-inference relevance, and rewrite phrasings that return mostly cloud-API noise. The seed's three-row structure targeting docs, repositories, and release notes is sound scaffolding for the revised vocabulary. Which phrasings will track this vocabulary is unknowable in advance, so the queries need their own review cadence.

**Second-order consequence.** This theme's perishable facts are version-coupled figures, the 3.4 GB size, the token counts, and the timing bands all decay with model and runtime releases, so release-note queries dominate the refresh value.

**Revision decision.** Rephrase toward ecosystem vocabulary, Ollama vision API and timeout documentation, Qwen vision model release notes, and ViT token-scaling guidance, each tied to the figures it would refresh.

**Retained seed evidence.** All three labeled query rows with their official-docs, repository, and release-notes targets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| search_query_label_name | search_query_text_value |
| --- | --- |
| `official_docs_query_phrase` | local vision media patterns official documentation best practices |
| `github_repository_query_phrase` | local vision media patterns GitHub repository examples |
| `release_notes_query_phrase` | local vision media patterns changelog release notes migration |

## Evidence Boundary Notes

**Decision supported.** This section helps decide how statements in this reference must be labeled so readers know what each claim rests on and where it applies. The seed notes define the three labels but ignore this file's specific hazards, hardware-coupled figures that read as universal and external rows whose subject matter never matched the theme.

**Recommended default and causal basis.** Label per claim, attach host and version context to every figure, and keep all three external URLs as unretrieved non-matching candidates. Downstream confidence calibrates on these labels, and a timing band quoted without its M4-host caveat misleads exactly the reader planning capacity on other hardware.

**Operating conditions and assumptions.** Labels stay stable corpus-wide and every combined-inference clause names the inputs it merges. The notes govern labeling in this reference and its reuses, not source ranking, which the hierarchy owns.

**Failure boundary and alternatives.** Labels applied per section rather than per claim let one labeled sentence launder its unlabeled neighbors. Bounded alternatives and recoveries: an explicit host-conditioned tag for figures, inline labels parenthetically on key claims, or claim-to-label indexing during verification.

**Counterexample, gotchas, and operational comparison.** Packet and prompt reuse strips labels mechanically, so load-bearing figures need their hardware context embedded in the same sentence. Good: the 800px rule cited as local fact with its rationale. Bad: the ten-to-twenty-second band quoted as universal local-vision performance. Borderline: the token-scaling claim carried as local fact with an unverified-mechanism note.

**Verification, evidence, and uncertainty.** Sample load-bearing claims, confirm correct labels, and verify every figure carries its host and version context. The three seed definitions match the corpus-wide label vocabulary and the source's architecture block supplies the host context the rules bind to. Label durability through packet reuse and prompt quotation is unaudited, so leakage risk remains an assumption.

**Second-order consequence.** This theme needs a hardware qualifier inside the local label itself, a claim can be perfectly sourced and still wrong on the reader's machine, a failure mode the three standard labels cannot express.

**Revision decision.** Add rules binding every numeric figure to its host and model version and marking the mismatched external rows as non-corroborating placeholders.

**Retained seed evidence.** All three label definitions, local fact, external fact, and combined inference, remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- `local_corpus_sourced_fact`: statements tied directly to the local source paths above.
- `external_research_sourced_fact`: statements tied to the public URLs above.
- `combined_evidence_inference_note`: synthesis that combines local and public evidence into agent guidance.
