# Algorithmic Art Generation Patterns

Use this reference when code is responsible for the composition, motion, or emergent behavior of a visual artifact and aesthetic quality is part of correctness. Its central decision is not merely which drawing library to select. It is which observable behavior can carry the concept clearly enough that palette, texture, and interface chrome support the work instead of rescuing a weak system.

**Recommended operating loop:** state one conceptual seed; choose one dominant visual-system family; expose a small set of perceptibly meaningful controls; implement with the simplest renderer that can express the required behavior; preserve deterministic replay when collaboration or comparison matters; and inspect the rendered result at representative states, times, and viewports. Iteration may loop backward when a prototype falsifies the concept-system mapping, but every accepted candidate should make that mapping explicit.

Apply this reference directly to p5.js or canvas sketches, seeded editions, motion studies, mathematically driven compositions, and focused interactive visual experiments. Use it as companion guidance when algorithmic art is one bounded subsystem inside a site, tool, installation, or game. Route elsewhere when factual data encoding, image retouching, product-interface ergonomics, photorealistic generation, or 3D camera and spatial behavior owns the primary correctness contract.

The minimum proof is dual: software evidence shows that the piece runs, replays as promised, resizes, and remains stable under its declared workload; visual evidence shows that the intended behavior is visible, framed correctly, and accepted against named criteria. A passing build or document verifier cannot prove that meaningful pixels rendered, while a compelling screenshot cannot prove temporal stability, interaction, or reproducibility.

`local_corpus_sourced_fact`: the mapped local algorithmic-art sources support the concept-to-system workflow, compact parameter surfaces, seeded behavior, simple-renderer default, graceful density reduction, and rendered-software checks. `combined_evidence_inference_note`: recommendations about a particular concept, family, parameter range, performance budget, or artistic stop condition remain reversible task-specific judgments to be tested against the actual artifact.

## Source Evidence Mapping Table

Use this map at claim level rather than treating the six entries as interchangeable endorsements. Authority answers "who can establish this kind of fact?" while relevance answers "does that fact decide this artwork?" An official automation source may be authoritative for a CI behavior and still provide no evidence for choosing particles over oscillators. A listed path or URL therefore becomes operational only when a reviewer can connect a specific claim to the source's actual scope and to a check on the resulting artifact.

| source_location_path_key | evidence_status_in_this_pass | source_authority_confidence_level | decisions_it_can_support | limitation_and_recheck_rule |
| --- | --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202604/algorithmic-art/SKILL.md | complete local read from frozen corpus | local_corpus_sourced_fact | workflow order; compact controls; seeded replay; simple renderer default; update/render/input separation; graceful density reduction; output contract | It supplies method defaults, not universal taste or current runtime API facts. Re-read when workflow or guardrail guidance is revised. |
| agents-used-monthly-archive/codex-skills-202604/algorithmic-art/references/algorithmic-philosophy-template.md | complete local read from frozen corpus | local_corpus_sourced_fact | movement framing; concept sentence; principle extraction; philosophy-to-code translation; perceptual failure check | Its movement names and examples illustrate a format rather than prescribe an aesthetic. Verify every translation in the render. |
| agents-used-monthly-archive/codex-skills-202604/algorithmic-art/references/generative-pattern-menu.md | complete local read from frozen corpus | local_corpus_sourced_fact | comparison among flow, particles, oscillators, cellular rules, packing/growth, recursive geometry, and noise-driven terrain or ink | The menu supplies selection cues and candidate controls, not a proof that one family fits a particular brief. Compare plausible families when motion logic is ambiguous. |
| https://developers.openai.com/codex/guides/agents-md | inherited external mapping; not browsed or refreshed in this pass | external_mapping_unrefreshed_note; seed label: external_research_sourced_fact | future checks about agent-instruction context and repository guidance when the exact page is refreshed | Do not use its presence as artistic evidence or make current-content claims from the URL alone. Record checked date, relevant heading, and decision impact after any future refresh. |
| https://docs.github.com/actions | inherited external mapping; not browsed or refreshed in this pass | external_mapping_unrefreshed_note; seed label: external_research_sourced_fact | future checks about GitHub Actions behavior and automation when CI is part of delivery | It cannot validate concept, visual-system fit, or rendered quality. Link availability would not by itself validate a semantic claim. |
| https://agents.md/ | inherited external mapping; not browsed or refreshed in this pass | external_mapping_unrefreshed_note; seed label: external_research_sourced_fact | future comparison with a general agent-instruction format when instruction portability matters | Treat any transfer into this domain as an explicitly labeled process analogy and verify that local constraints survive it. |

**Default evidence sequence:** read the compact canonical local skill; load the philosophy template when intent must be articulated or tested; load the pattern menu when system selection is uncertain; prototype the resulting decision; and refresh an external primary source only when a current platform or instruction-format claim can change implementation. This is progressive disclosure, not local-source immunity: direct contrary evidence may justify adaptation, but the conflict, scope, and artifact result must be recorded.

**Claim record:** for every material recommendation, retain `(claim, evidence class, supporting source, source scope, artifact verification, uncertainty)`. A good record says, "Seeded replay is a local default; this piece intentionally disables it for an ephemeral performance; two captured runs confirm the accepted nonrepeatability." A bad record says, "Best practice requires determinism," with several links but no source scope or rendered check. A borderline cross-domain analogy is usable only after its assumptions are restated and a direct artifact test is named.

This mapping is also a recovery mechanism. If a source drifts or a rendered test falsifies an inference, reviewers can revise the affected claim without discarding unrelated guidance. Record intentionally skipped sources and the reason: a deliberate omission is reviewable, while silent nonreading makes source-count claims meaningless.

## Pattern Scoreboard Ranking Table

The three numeric values below are inherited editorial priorities from the seed. No calibration method, probability interpretation, benchmark population, or cross-reference scoring scale is available, so do not add them, average them, or cite "95" as evidence that a pattern works 95 percent of the time. Their defensible content is the ordering, named failure target, and observable gate. Artifact-building priorities below them are intentionally trigger-based rather than assigned invented numbers.

| pattern_name_and_stable_key | inherited_score_or_operational_priority | when_it_leads | pattern_failure_prevention_target | direct_verification_gate |
| --- | --- | --- | --- | --- |
| Source Map First (`algorithmic_art_generation_patterns`) | 95; inherited `default_adoption_pattern_tier` | Before synthesizing or changing reference guidance | Prevent context-free advice that ignores the frozen local algorithmic-art corpus. | Every material source-backed claim names a loaded local path and its actual scope. |
| Evidence Boundary Split (`algorithmic_art_generation_patterns`) | 91; inherited `default_adoption_pattern_tier` | Whenever local facts, inherited external mappings, experiments, and editorial judgment are combined | Prevent authoritative tone from laundering inference into fact. | Claim records distinguish inspected local evidence, unrefreshed external records, measured artifact behavior, and artistic judgment. |
| Verification Gate Coupling (`algorithmic_art_generation_patterns`) | 88; inherited `default_adoption_pattern_tier` | Before a recommendation or artifact is called accepted | Prevent prose-only instructions that cannot be checked. | Each claim points to a command, state replay, capture, metric, reviewer question, or explicit uncertainty. |
| Concept-System Alignment | First artifact-building priority for a new brief | When the concept exists but no visual mechanism has been selected | Prevent palette and effect layers from compensating for behavior that does not embody the premise. | In a representative render, the reviewer can identify how the primary mechanism expresses the concept without relying on an explanatory paragraph. |
| Seeded Causal Iteration | Foundational diagnostic priority when comparison matters | Before comparing parameter, code, or palette variants | Prevent random-state changes from being mistaken for design improvements or regressions. | Re-running the same recorded seed and candidate state reproduces the promised class of result within declared environment limits. |
| Compact Meaningful Controls | Leads when a sketch exposes parameters or user input | Before adding a control and during candidate convergence | Prevent dead, redundant, unsafe, or conceptually irrelevant controls from widening the search space. | A bounded sweep shows that each advertised control causes a perceptible, interpretable change without breaking the artifact. |
| Graceful Density Degradation | Leads after a frame-stability or device-capacity failure | When the concept survives with fewer agents, samples, trails, or updates | Prevent slowdown from changing temporal character, blocking interaction, or producing a blank frame. | A density step-down restores the declared frame envelope while preserving the dominant behavior and composition intent. |
| Rendered State Inspection | Hard gate regardless of static ranking | At first representative prototype, candidate milestones, and final acceptance | Prevent technically valid code from shipping blank, clipped, unreadable, or temporally wrong output. | Fresh evidence covers intended viewports and meaningful temporal or interaction states, with console and runtime failures recorded. |

**Default ordering:** reference authors use the three inherited governance patterns first; artifact builders use concept-system alignment, seeded iteration, compact controls, implementation, and rendered inspection. Maintenance work starts with the observed failure instead. A blank canvas makes rendered-state diagnosis the immediate priority; a nondeterministic regression makes seeded replay lead; an overloaded mobile render elevates graceful degradation.

**Override rule:** reorder only for a concrete failed gate, changed requirement, or newly discovered hard boundary, and record the reason. Static priority prevents aimless work; observed evidence corrects it. A lower everyday priority may still be a hard completion gate, and no score can waive visible output inspection.

## Idiomatic Thesis Synthesis Statement

`local_corpus_sourced_fact`: The frozen local row for `algorithmic_art_generation_patterns` contains three source paths. Together they establish a coherent default: distill a feeling, metaphor, motion, or mathematical premise; decide whether the piece is static, animated, interactive, or seed-driven; choose the smallest visual-system family whose motion logic expresses that premise; expose a compact parameter surface; implement with p5.js or plain canvas unless the behavior genuinely requires a heavier stack; separate update, render, and input logic; and verify resize behavior, seed behavior, frame stability, and code readability. The supporting material adds a philosophy-to-code translation test and a menu of flow, particle, oscillator, cellular, growth, recursive, and noise-driven families.

`external_mapping_unrefreshed_note`: The seed classifies three public evidence surfaces for agent instructions, automation, and a general instruction format as `external_research_sourced_fact`. This pass preserves those inherited mappings but did not browse them, so they cannot support present-tense external claims here. Their legitimate future role is to check current process or platform claims after a claim-specific refresh; they do not establish which artistic system, palette, composition, or emotional effect is correct.

`combined_evidence_inference_note`: Idiomatic algorithmic art is a correspondence among intent, mechanism, controls, and observed output. The recommended loop is:

1. Write a one-sentence conceptual seed that names what behaves and how it changes.
2. Select one primary family by motion logic, not by fashionable appearance. If two families are genuinely plausible, compare minimal monochrome prototypes before committing.
3. Define only controls with perceptible, concept-relevant effects, including a replay seed whenever repeatable critique, export, or debugging matters.
4. Build the smallest representative state before adding polish or an application shell.
5. Inspect fixed-seed output, a bounded parameter sweep, target viewports, meaningful temporal states, console behavior, and frame stability.
6. Keep, simplify, switch family, optimize, or stop according to the first material failed gate; preserve the rationale with the selected candidate.

This sequence is a loop rather than a one-way production line. A prototype may expose a better concept, a control sweep may reveal that two parameters are redundant, and density stress may require a different renderer. The loop remains disciplined because a stable seed and named rubric make those revisions comparable instead of confusing code changes with random state.

The default is strongest for bounded, inspectable sketches in which one field, lifecycle, rhythm, local rule, growth process, recursion, or noise structure can carry the premise. It becomes secondary when factual encoding, product ergonomics, photorealistic editing, 3D spatial interaction, or several independently owned systems dominate the task. A hybrid remains valid when every subsystem has a distinct concept-bearing role, a narrow interface, and separate evidence; "more layers" is not itself a rationale.

Confidence is high about what the inspected local files say. The best family for a particular feeling, the useful parameter ranges, the final backend, the performance budget, and the artistic stop condition remain bounded judgment. Test those choices through representative renders and say when evidence is inconclusive. The practical failure check is perceptual: if the philosophy can be understood only after a paragraph of explanation, strengthen or replace the behavior before strengthening the prose.

The second-order benefit is maintainability without aesthetic standardization. A clear system can be replayed, ablated, simplified under load, handed to another agent, and migrated between renderers while preserving intent. Rigor protects surprise by making exploration reversible; it does not convert taste into an automated assertion.

## Local Corpus Source Map

Use progressive disclosure rather than loading the three files as an undifferentiated dump. Read the compact canonical skill for every in-scope task; open the philosophy template when the uncertainty is conceptual articulation or perceptual strength; open the pattern menu when the uncertainty is which motion logic should carry the work. Loading a source counts only when it changes a decision, confirms a decision against an explicit rule, or is declined as inapplicable with a reason.

| local_source_filepath_value | hierarchy_and_read_trigger | local_source_heading_signals | concrete_guidance_to_extract | limitation_or_misuse_warning |
| --- | --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202604/algorithmic-art/SKILL.md | Canonical entrypoint; always read before implementation or substantive reference evolution | Algorithmic Art; Overview; Workflow; Default Rules; Reference Use; Output Contract; Guardrails | Concept to system to parameter surface to implementation; one dominant behavior; p5.js or canvas default; seeded repeatability; deliberate color; graceful density reduction; update/render/input separation; software checks | It is a compact operating method, not an API manual or universal theory of taste. "Prefer living motion" is a default that a justified static work may adapt. |
| agents-used-monthly-archive/codex-skills-202604/algorithmic-art/references/algorithmic-philosophy-template.md | Supporting detail; read when the user asks for a manifesto, design note, movement framing, or a stronger concept-to-code bridge | Algorithmic Philosophy Template; Template; Movement Name; Concept Seed; Core Principles; Translation To Code; Parameter Surface; Failure Check | A short textured name; one-sentence emotional or mathematical premise; three to five behavioral principles; mappings such as gentle drift to low-frequency noise and memory decay to alpha fade plus sparse respawn | Example movement names and metaphors are illustrative. If the concept becomes visible only through explanatory prose, strengthen the behavior rather than elaborating the narrative. |
| agents-used-monthly-archive/codex-skills-202604/algorithmic-art/references/generative-pattern-menu.md | Supporting detail; read when two or more system families seem plausible or the first idea does not match the requested motion | Generative Pattern Menu; Flow Fields; Particle Systems; Oscillator Systems; Cellular Or Rule Systems; Packing And Growth; Recursive Geometry; Noise-Driven Terrain Or Ink; Selection Rule | Family cues and good control candidates: force and migration; birth and death; rhythm and interference; local-rule emergence; crowding and territory; self-similar branching; geological or organic fields | The menu narrows a choice; it is not permission to stack all families. Palette, line style, and layering should support the selected motion rather than compensate for a weak match. |

**Minimum retrieval rule:** use the canonical skill plus only the supporting material required by the unresolved question. Read both supporting files when the task genuinely requires a written artistic philosophy and a nontrivial family comparison. Record an intentional skip when a supplement would add no decision value; this keeps context focused without pretending complete coverage was needed.

**Source disposition format:** `(path, question asked, rule extracted, decision affected, artifact check, exception if any)`. For example: the menu is opened to decide between flow and particles for "memory losing cohesion"; particles are selected because lifecycle and decay are concept-bearing, while a low-frequency field is retained only as the particles' force model; a monochrome fixed-seed capture tests whether lifecycle remains legible without palette.

Bad use cites the menu but implements flow, particles, oscillators, recursive branches, and postprocessing without assigning roles. Borderline use combines two families because each has a distinct responsibility; it becomes acceptable only when ablation shows that removing either one breaks a named criterion and target-runtime evidence remains stable.

These paths are frozen 202604 evidence. A future comparison with a newer local skill should identify concrete changed guidance rather than assume that newer is automatically better. When sources appear to conflict, first compare claim, scope, version, and target artifact; then choose the most relevant rule, test the exception in the render, and record the outcome. Repeated verified exceptions are a refresh signal, not permission to mutate the hierarchy silently.

## External Research Source Map

No browsing occurred during this evolution pass. The URLs, names, and intended seed roles below are therefore preserved as inherited mapping facts, not presented as freshly checked descriptions of current page contents. Use present-tense external claims only after a future reviewer opens the primary source and records the exact relevant material.

| external_source_url_value | external_source_name_text | inherited_usage_role | legitimate_claim_scope_after_refresh | prohibited_extrapolation_in_current_state |
| --- | --- | --- | --- | --- |
| https://developers.openai.com/codex/guides/agents-md | OpenAI Codex AGENTS.md guide | primary agent instruction context model | Repository-scoped agent instruction behavior or context conventions supported by the refreshed page | Do not use the URL to select a visual system, assert an artistic workflow, or claim current Codex behavior without checking the page. |
| https://docs.github.com/actions | GitHub Actions documentation | verification and automation model | Current GitHub Actions syntax, workflow behavior, or CI constraints needed for a concrete delivery gate | Do not treat automation authority as proof that the reference is coherent, the sketch runs, or the intended render state is visually correct. |
| https://agents.md/ | AGENTS.md open format | general agent instruction format | Current general instruction-format conventions when portability or interoperability is an explicit requirement | Do not allow a general format analogy to override frozen local art guidance or project-specific ownership and testing constraints. |

**Claim-triggered refresh default:** stay with the inspected local corpus and direct artifact evidence for stable creative-method decisions. Refresh a public source only when a current platform, format, API, or automation fact could change the implementation or completion gate. This avoids broad research that enlarges context without resolving the failing decision.

A future external evidence record should contain:

- the direct URL and source owner;
- the date checked and, where exposed, the relevant version or update context;
- the exact heading or narrowly summarized passage that supports the claim;
- the claim being supported and the source's domain scope;
- any conflict with local guidance and the reason for adopting, adapting, or declining it;
- the implementation or verification action that changed as a result;
- residual uncertainty, including environment or version boundaries.

Link availability and semantic support are different checks. An accessible page may no longer contain the mapped guidance, and a page that contains it may still be irrelevant to the artwork's central decision. Likewise, three external links that repeat one process assumption do not provide independent evidence for visual quality. Pair process guidance with direct execution and rendered-output checks.

**Use examples:** citing refreshed GitHub Actions documentation to correct a concrete CI workflow is a good external use. Citing it to defend a palette or particle model is a category error. Borrowing a general instruction structure for an art run card is borderline: label it as an analogy, restate its assumptions in this domain, and confirm that it does not erase the concept, seed, renderer, and visual-evidence fields required here.

When a prototype exposes a platform boundary, let the failure produce the search target. A browser error, nondeterministic export, unsupported API, or device-specific frame collapse yields a narrower and more useful official-documentation query than "algorithmic art best practices." After refresh, record whether the source changed a claim, confirmed it, or had no material impact. Honest nonverification is preferable to implied freshness.

## Anti Pattern Registry Table

Use this registry to classify the earliest broken link, then repair that layer before polishing downstream symptoms. A diagnosis needs an observed impact, a violated requirement, or a credible reproduction risk; unconventional style alone is not a defect. Intentional exceptions are valid when the supposedly risky behavior is named as part of the concept and accepted with direct evidence.

| anti_pattern_failure_name | failure_cause_and_consequence | detection_signal_review_method | safer_default_replacement_pattern | valid_exception_boundary |
| --- | --- | --- | --- | --- |
| `context_free_summary_output` | The agent skips the local corpus and emits generic creative-coding advice, losing repository-specific workflow and guardrails. | No loaded-source disposition connects a local rule to a decision or explicit decline. | `source_map_first_synthesis`: read the canonical skill, load only relevant supplements, and trace extracted constraints into the artifact. | A source may be skipped when it cannot affect the declared task, but the reason is recorded. |
| `unsourced_recommendation_claims` | Artistic or engineering judgment is phrased as established fact, making disagreement and refresh impossible to locate. | A material recommendation has no local fact, refreshed external fact, measured behavior, inference label, or uncertainty. | `evidence_boundary_split_pattern`: attach confidence to each claim rather than to the document as a whole. | Personal taste can remain a preference when named as such and owned by the designated reviewer. |
| `unverified_agent_instruction` | Advice cannot be falsified, so implementation can appear complete without a working or accepted artifact. | The instruction names no command, replay, capture, metric, reviewer question, or stop condition. | `verification_gate_coupling`: define the smallest evidence capable of disproving the claim. | Early ideation may use provisional guidance, but it cannot be promoted to acceptance without a gate. |
| `effect_stack_without_roles` | Several systems, filters, or layers accumulate because each looks interesting, weakening conceptual identity and multiplying diagnosis cost. | The owner cannot state one concept-bearing role for each layer, or ablation changes spectacle but not a named criterion. | Select one primary family; retain a secondary system only for a distinct responsibility demonstrated by ablation. | Deliberate maximalism is valid when interactions are the concept and remain observable under the target workload. |
| `palette_rescues_weak_motion` | Color contrast creates apparent richness while the underlying behavior is static, incoherent, or semantically unrelated. | A monochrome or low-saturation render loses all structure and no motion logic remains perceptible. | Strengthen field, lifecycle, rhythm, local rule, growth, or geometry before restoring palette. | A color-system artwork may make palette the primary mechanism, but then color transitions require their own explicit model and evidence. |
| `unseeded_comparison_drift` | Every run changes random state, so reviewers attribute differences to code or controls that may not have caused them. | The selected variant cannot be replayed, and before/after captures use unrelated initial conditions without an intentional-chaos rationale. | Record random and noise seeds, initialization order, code revision, viewport, and candidate parameters. | Ephemeral nonrepeatability is valid when it is the accepted behavior rather than an accidental omission. |
| `control_surface_sprawl` | Parameters are added for flexibility without distinct perceptual purpose, widening search and exposing unsafe combinations. | Controls are dead, redundant, hypersensitive, unlabeled in effect, or capable of driving NaN, runaway density, or illegible states. | Keep a compact surface; bound values; sweep each control; merge correlated parameters; expose presets only after evidence. | An expert instrument may expose many controls when the user explicitly needs them and interactions are documented and stable. |
| `coupled_update_render_input` | Simulation state, drawing, and input mutate one another in one loop, making replay, resizing, and tests order-dependent. | A redraw changes state, a resize silently restarts the piece, or identical inputs diverge because render order altered simulation. | Separate initialization, update, render, and input transitions; state reset and resize policy become explicit. | A tiny throwaway study may stay compact, but candidate promotion requires reproducible lifecycle behavior. |
| `rendered_output_uninspected` | Text, tests, or build output are accepted without opening the visual result. | The canvas is blank, clipped, obscured, incorrectly framed, or in an unintended state despite successful execution. | Capture and inspect representative pixels, layout, temporal state, console state, and interaction on target viewports. | There is no completion exception for an inherently visual artifact; evidence form may vary, but the output must be observed. |
| `single_frame_motion_proof` | A first-frame screenshot is used to claim animation, decay, emergence, or long-run stability. | Temporal behavior has no sampled times, video, state trace, or live review, and later states may saturate or disappear. | Inspect startup, representative mid-state, stress or long-run state, and any interaction-dependent transition. | A genuinely static deliverable needs only its declared final state plus resize and export evidence. |
| `density_without_backpressure` | Particle count, spawn rate, trail buffers, or update work grows until slowdown changes the piece's temporal character. | Frame intervals degrade, input lags, memory grows, or the artifact becomes blank or unstable under target density. | Cap work, pool reusable state where appropriate, cull invisible entities, and reduce density before adding complexity. | High-density offline export may trade latency for fidelity when completion time and memory are explicitly bounded. |
| `resize_state_corruption` | Coordinate assumptions or buffer recreation destroy composition, crop content, or reset the seed unexpectedly. | Target viewport changes produce clipping, stretched geometry, blank regions, or a different edition with no reset policy. | Define normalized coordinates or a deliberate recomposition policy and test all target dimensions. | A fixed-format installation may reject responsive resizing when its physical canvas is part of the specification. |
| `invisible_state_accumulation` | Offscreen particles, stale trails, event listeners, or detached buffers continue consuming work while output looks superficially stable. | Resource use or frame cost rises over time although visible density does not; reset or teardown leaves work active. | Cull, expire, detach, or reuse state; include long-run and teardown checks. | Persistent hidden state is valid only when it has a future concept-bearing effect and remains bounded. |
| `generic_frontend_takeover` | The agent builds navigation, cards, settings panels, and marketing copy before proving the artwork, shifting effort from the requested visual system. | The shell has more behavior than the art core, while no representative render or concept gate exists. | Prototype the art full-bleed or minimally framed; integrate into an existing shell through a narrow dimensions/input/performance contract. | A requested polished tool may need a substantial shell, but product-interface guidance becomes the primary companion workflow. |

**Diagnosis order:** restore observability first with a reproducible seed and actual render; classify whether the first material failure is conceptual, mechanistic, control-related, computational, presentational, or evidential; then change the smallest upstream cause. A stable seed often reveals that a "taste" problem is a dead control, that a "performance" problem is invisible state growth, or that a "visual" problem is resize corruption.

For a disposable sketch, the lightweight gate is simple: run it, inspect it, verify the declared seed policy, resize or confirm fixed-format intent, and identify the dominant mechanism. For a reusable or shipped artifact, add parameter sweeps, representative temporal states, target-device frame observations, long-run cleanup, candidate manifests, and reviewer evidence. Do not expand rigor merely to create records; retain evidence only when it supports reproduction, diagnosis, selection, or acceptance.

## Verification Gate Command Set

`verification_gate_command_set`: From the repository root, run the repository-specified final-stage reference verifier after editing this file:

```bash
python3 agents-used-monthly-archive/idiomatic-references-202606/tools/verify_reference_generation.py --stage final
```

Record the exact exit status and relevant output. The command's name and seed role establish it as a generated-reference gate; they do not establish that it builds artwork code, launches a browser, checks console errors, samples animation, measures frame stability, or inspects pixels. A passing document gate must never be reported as rendered-art proof. In a shared corpus, also distinguish a failure in this owned file from a failure caused by another incomplete path rather than concealing either result.

Use the following claim-to-gate model for an actual algorithmic-art artifact. Project-specific launch, test, capture, and build commands must come from the implementation repository rather than being invented by this reference.

| claim_to_verify | minimum_method | evidence_to_retain | pass_condition | important_limit |
| --- | --- | --- | --- | --- |
| Reference structure and repository conventions | Run the exact verifier above plus focused structural checks for this file. | Command, exit status, scoped failures, heading and placeholder audit. | The owned reference meets its declared structural contract; unrelated failures are reported with their owners or conditions. | This says nothing about artwork pixels or runtime behavior. |
| Executable artifact | Use the repository's documented build or launch path and inspect runtime errors. | Actual command, environment, exit state, and concise console summary. | The representative state launches without an unhandled error. | Successful launch can still produce blank or wrong output. |
| Seed policy | Run the same candidate twice with recorded random/noise seeds and initialization order; also test intentional nonrepeatability when declared. | Seed manifest and matched captures or state hashes appropriate to the medium. | Replay matches the promised level of determinism in the declared environment. | Cross-browser, GPU, font, floating-point, and timing differences may require bounded visual rather than byte identity. |
| Control meaning and safety | Sweep minimum, representative, and maximum values one control at a time after a baseline is fixed. | Parameter values, captures, observed effect, invalid-state or clamp result. | Every exposed control has a perceptible and interpretable effect and remains within safe execution bounds. | Early exploratory controls may remain internal until this gate passes. |
| Viewport and framing | Render every declared target size and any fixed-format export dimensions. | Fresh viewport-labelled captures and resize/reset policy. | The intended composition remains visible, correctly framed, and free of incoherent overlap or clipping. | A fixed installation may deliberately reject responsive behavior if that boundary is explicit. |
| Temporal behavior | Inspect startup, representative mid-state, stress or long-run state, and interaction-driven transitions. | Time-labelled captures, short video, live-review note, or state trace as appropriate. | Motion, emergence, decay, trails, and lifecycle remain intentional over the required interval. | A single screenshot cannot establish this claim. |
| Runtime stability | Measure after initialization under representative and stress density on target-class hardware. | Environment, workload, warmup, sample window, observed frame intervals, memory trend where material, and degradation event. | The project-defined envelope holds or the system degrades density while preserving its dominant behavior. | This reference defines no universal frame-rate threshold. |
| Visual and conceptual acceptance | Compare fresh renders against criteria written before candidate selection; use monochrome and layer-ablation probes when useful. | Rubric version, reviewer verdict, rationale, disagreement, selected candidate, and materially informative rejection. | The designated reviewer accepts the visible concept-system correspondence and knows the stop condition. | Aesthetic acceptance is bounded judgment, not an automated truth claim. |
| Export reproducibility | Regenerate the selected artifact from its code revision, seed, parameters, viewport, and environment notes. | Candidate manifest, output identity, export settings, and second-run result. | Another run reaches the intended state without unrecorded oral instructions. | External assets and platform rendering can constrain exact identity and must be named. |

**Evidence packet example:** `code revision + run command + seed + candidate parameters + viewport + temporal state + fresh capture + console result + runtime observation + rubric verdict`. A bad packet contains only "tests pass." A borderline packet contains one desktop screenshot for an animated responsive piece; report exactly which mobile, temporal, interaction, and long-run claims remain untested.

Run cheap gates during exploration: syntax or launch, one fixed-seed state, and direct visual inspection. Run the full matrix only at representative candidate milestones and final acceptance. Include at least one perturbation, such as increased density, resize, layer ablation, or reset, because a happy-path still cannot demonstrate graceful behavior. Preserve failed variants only when their evidence explains a rejected mechanism, boundary, or recurring regression.

Classify results as `pass`, `scoped_failure`, or `external_shared_state_failure`, with the failing claim and next owner or action. Verification is useful only when it can route the next decision; raw output without interpretation is audit noise.

## Agent Usage Decision Guide

`agent_usage_decision_guide`: Use the artifact's dominant correctness contract, not keyword occurrence alone, to decide whether this reference owns the work.

| usage_mode | choose_when | ownership_and_next_action | route_or_limit |
| --- | --- | --- | --- |
| Primary | Code-generated composition, motion, geometry, emergence, or interaction is the requested artifact and aesthetic quality is part of acceptance. | Follow the complete concept, family, controls, prototype, and rendered-evidence loop here. | Examples include focused p5.js/canvas sketches, seeded editions, motion studies, and computational visual experiments. |
| Companion | Algorithmic art is one bounded layer inside a site, creative tool, game, installation, or branded experience. | This reference owns the art core; the parent workflow owns navigation, content, product ergonomics, deployment, or game rules. Define a narrow dimensions, input, lifecycle, and performance contract. | Do not let expressive settings spread into unrelated application state or let shell work postpone a representative art render. |
| Avoid as primary | Factual data encoding, photo editing, image generation, icon/logo systems, document layout, or conventional product UI defines correctness. | Route to the relevant visualization, image, design-system, document, or frontend workflow. | Algorithmic techniques may style a nonsemantic layer but must not distort facts, legibility, or user action. |
| Escalate or combine | Required depth, camera behavior, shaders, audio, high-resolution offline export, installation hardware, or several independent systems exceeds a simple 2D sketch. | Add a domain-specific companion and split ownership at explicit subsystem boundaries. | Keep this reference's concept, seed, controls, and visual evidence contract for the algorithmic subsystem. |

Before implementation, write a compact preflight decision record:

1. **Artifact:** static, animated, interactive, seed-driven edition, or hybrid; include final inspection and export surfaces.
2. **Concept seed:** one sentence naming what behaves, what constrains it, what introduces variation, and what the viewer should perceive or feel.
3. **Primary family:** one motion logic from the local menu or another explicitly justified computational model; record one plausible rejected alternative when ambiguity is material.
4. **Control surface:** a small list of seed, palette, density, tempo, noise scale, trail decay, lifetime, drag, or other controls with their intended perceptual effects and safe bounds.
5. **Renderer:** existing project stack first; otherwise p5.js or plain canvas for fast 2D iteration, escalating only for a behavior, dimensionality, or density requirement the simpler path cannot meet.
6. **Acceptance evidence:** target viewports, meaningful temporal states, deterministic or intentionally nondeterministic policy, runtime envelope, named visual criteria, reviewer, and stop condition.

If the brief lacks a concept but is otherwise workable, propose a small set of distinct conceptual seeds and select one before broad implementation. If family choice remains uncertain, compare minimal monochrome prototypes that demonstrate each candidate's defining behavior. Do not build several polished alternatives or a large shell merely to postpone the choice.

During implementation, keep update, render, and input transitions legible; preserve a fixed baseline seed; add controls only after their hypotheses are named; and render the smallest representative state early. After each candidate, classify the first material failure:

- **Concept failure:** the intended idea is not perceptible; revise the premise or its translation.
- **System failure:** the selected family cannot express the premise; compare or switch families.
- **Control failure:** an input is dead, redundant, unsafe, or too sensitive; remove, merge, or bound it.
- **Runtime failure:** workload changes temporal character or interaction; reduce density, bound work, or justify renderer escalation.
- **Presentation failure:** framing, resize, contrast, or temporal state is wrong; fix the delivery surface without disguising a mechanism failure.
- **Evidence failure:** the output cannot be replayed or reviewed; restore observability before more creative changes.

**Good primary use:** "Build a seeded canvas study in which particles lose cohesion in a slow current; preserve readable trails on desktop and mobile." **Bad primary use:** "Build a revenue dashboard with generative shapes," where shape must encode accurate values. **Borderline companion use:** a generative full-bleed background in a branded site; the art core may follow this guide, but site design owns content hierarchy, motion accessibility, navigation, and user interaction.

Preserve evidence labels when reusing recommendations. Local source facts define the repository method; unrefreshed external mappings remain bounded; prototypes supply measured implementation evidence; and final aesthetic selection remains designated reviewer judgment. Record rejected families briefly so a later agent reopens them only when new requirements or evidence justify the cost.

## User Journey Scenario

The representative journey is hypothetical; it demonstrates operational reasoning rather than claiming that the described render was measured in this repository.

**Role and starting state:** A creative-tool builder has a browser-capable workspace and the brief, "Make memory feel as if it is losing cohesion in a slow current." The user wants an animated code-native artifact, a repeatable selected edition, responsive framing, and an exportable still. They have not chosen a visual family, controls, taste rubric, or stop condition. The mapped local skill is the entrypoint because generated visual behavior is the primary artifact.

**Initial decision record:**

- Concept seed: "Discrete memories drift through an invisible current, briefly cluster, then fade and sparsely return."
- Observable principles: particles move; a low-frequency field constrains direction; drag prevents frantic motion; alpha decay and lifetime represent forgetting; sparse respawn preserves continuity without restoring the exact past.
- Mode: animated and seed-driven, with a still exported from a named temporal state.
- Primary family: particle lifecycle, because birth, cohesion loss, death, and reappearance are concept-bearing. A flow field is an internal force model, not a second independently decorated system.
- Plausible rejected alternative: phased oscillators express rhythm well but make discrete loss and respawn less direct for this interpretation.
- Compact controls: `seed`, `density`, `flow_scale`, `drag`, `lifetime`, `trail_decay`, and `palette`; each receives safe bounds and a stated perceptual effect.
- Provisional criteria: slow coherent drift; visible but not grid-like clustering; legible decay; empty space remains intentional; behavior stays structurally interesting in monochrome; the selected state is framed at declared desktop and mobile viewports.

| journey_phase | agent_action | evidence_or_decision | failure_branch |
| --- | --- | --- | --- |
| Source and brief intake | Read the canonical skill, then the philosophy template and pattern menu because both concept articulation and family selection are material. | Record extracted constraints and the primary/secondary system roles above. | If the user actually needs a still image edit or product shell, route before implementing the sketch. |
| Minimal concept prototype | Render monochrome particles with field, drag, lifetime, decay, and a fixed baseline seed; omit UI and decorative postprocessing. | Capture startup and one representative mid-state at a single target viewport. | If memory loss is not perceptible, revise lifecycle or concept mapping before palette work. If flow obscures lifecycle, simplify the force model. |
| Exploration | Vary a coarse but bounded set of density, lifetime, and decay combinations; permit broader changes while labeling runs `exploration`. | Retain only the baseline and materially informative results; note what each teaches. | If two families remain plausible, build equally minimal defining-behavior prototypes rather than stacking them. |
| Convergence | Freeze code revision, seed, viewport, rubric version, and all but one changed variable per comparison. Add deliberate palette only after monochrome structure holds. | Pairwise captures and reviewer notes identify a candidate and rejected alternatives. | If criteria change after a surprising render, version the rubric before judging the next batch; do not silently rescore prior work. |
| Runtime and delivery | Sweep controls, resize to every target viewport, observe representative and stress density, inspect long-run cleanup, and exercise reset/export. | Record console state, frame observations, density-degradation behavior, candidate parameters, and time used for the still. | If runtime fails while concept remains strong, reduce density or bound work first. If simplification erases identity, consider a renderer change with measured justification. |
| Acceptance and restore | Review a fixed-seed run, a small robustness seed set, target captures, temporal evidence, and the exported still against the frozen rubric. | The designated reviewer records accept, reject, or bounded uncertainty and the reason. A second run reconstructs the candidate from its manifest. | If only one seed works, accept it as a curated edition when explicitly labeled; do not generalize system robustness. |

**Good outcome:** the selected candidate is reproducible, its particle lifecycle carries the concept without explanatory rescue, every exposed control has a visible role, the composition survives target viewports, and density reduction preserves slow drift rather than merely lowering a counter. **Bad outcome:** every comparison changes seed, color, particle count, and field code at once; several effects create movement but no mechanism represents forgetting; a desktop screenshot is accepted without mobile, temporal, or restore evidence. **Borderline outcome:** the field becomes visually dominant enough to look like a separate system. Ablate it and compare a simpler directional force; keep the field only if it contributes a named current criterion that particles alone cannot express.

The retained completion packet is intentionally small: concept record, selected and baseline seeds, code revision, candidate parameters, rubric version, target viewports, meaningful temporal state, fresh captures, runtime observations, reviewer verdict, export identity, and one or two informative rejections. Unselected exploratory runs are not archival obligations. The durable output is both the artwork and enough evidence for another agent to regenerate and judge the intended state without oral context.

## Decision Tradeoff Guide

Choose by artifact fit and dominant correctness before choosing by source agreement. The inspected local corpus is sufficient to start a bounded creative prototype; external refresh becomes necessary only when a volatile platform, format, or automation fact can change delivery.

| decision_option_name | when_to_choose_condition | tradeoff_cost_description | falsification_or_verification_question |
| --- | --- | --- | --- |
| Adopt when | Code-generated visual behavior is the primary artifact; one owner can select one dominant system, expose compact controls, and inspect representative output. | Fastest route to useful evidence, but the first plausible family may bias later exploration. | Does a minimal monochrome prototype make the concept perceptible, and can the candidate be replayed or intentionally classified as ephemeral? |
| Adapt when | The task is hybrid, the existing stack constrains implementation, the delivery surface is fixed, or a source-backed default conflicts with direct artifact evidence. | Preserves project fit and artistic intent, but exceptions add rationale, integration, and verification work. | Is the changed default tied to a requirement or observed gate, with source fact, implementation evidence, and judgment kept separate? |
| Avoid as primary when | Factual encoding, image editing, conventional UI, 3D spatial behavior, or another discipline owns the central correctness contract. | Prevents category error, but algorithmic techniques may need a clearly bounded companion role. | Would following this guide risk misleading data, obscuring user action, or delivering the wrong artifact medium? |
| Switch or escalate when | A representative prototype falsifies the family choice, or measured density, dimensionality, export, or interaction requirements exceed the simple renderer. | A switch creates rework; delaying it can create deeper lock-in and decorative compensation. | What exact failed gate can the new family or renderer pass that the current one cannot, and can a small comparison demonstrate it? |
| Cost of being wrong | The agent chooses the wrong artifact owner, motion logic, seed policy, parameter surface, or renderer. | Rework includes discarded code, irreproducible selection, hidden runtime risk, and potentially a visually polished but conceptually false result. | Can a reviewer identify what to undo, which evidence invalidated the decision, and the cheapest next discriminating test? |

Choose the primary visual family by what changes over time or space:

| candidate_family | choose_when_the_concept_depends_on | principal_tradeoff | cheapest_discriminating_probe |
| --- | --- | --- | --- |
| Flow fields | wind, current, migration, or an invisible force shaping trajectories | Coherent motion is easy to produce, but field texture can dominate the subject or make agents look interchangeable. | Render sparse monochrome tracers at two noise scales and ask whether the force itself is the intended subject. |
| Particle systems | birth, death, lifetime, clustering, dispersal, or swarm behavior | Lifecycle is explicit, but high density and spawn work can hide individual meaning and destabilize runtime. | Use low density with visible lifecycle markers before trails or postprocessing. |
| Oscillator systems | rhythm, interference, breathing, phase, or wave superposition | Strong temporal structure can feel mechanical or repetitive when coupling and phase lack purpose. | Compare a few phased elements across one complete period and inspect whether interference carries the concept. |
| Cellular or rule systems | local interactions producing emergent global structure | Emergence is powerful but often difficult to direct, reproduce perceptually, or explain through individual controls. | Run fixed-rule, fixed-seed generations and vary one neighborhood or mutation decision. |
| Packing and growth | crowding, territory, expansion, collision, or pressure | Spatial negotiation is legible, but convergence cost and edge cases can grow with entity count. | Compare early, mid, and saturated states at bounded population. |
| Recursive geometry | branching, hierarchy, self-similarity, or architectural order | Coherence is immediate, but repetition can become decorative and depth can amplify cost. | Render low depths with angle variance disabled and enabled; verify that branching, not texture, carries the premise. |
| Noise-driven terrain or ink | geological, cloudy, watery, topographic, or organic material | Texture arrives quickly, but noise can substitute for composition and expose many correlated parameters. | Inspect contours in monochrome at a small scale set and remove palette-dependent appeal. |

**Mode tradeoff:** static output makes composition and export easier to verify but cannot express lifecycle or temporal causality unless time is encoded spatially. Animation expresses change but requires temporal sampling and frame stability. Interaction gives the viewer agency but adds input state, accessibility, reset, and discoverability contracts. Seed-driven editions improve reproduction and controlled variation; intentionally ephemeral runs exchange replayability for nonrepeatability that must itself be part of the brief.

**Renderer tradeoff:** prefer the existing project renderer; otherwise use p5.js or plain canvas for fast 2D iteration. Escalate to WebGL, shaders, or a heavier stack only when a measured density, required effect, dimensionality, or interaction cannot be achieved acceptably by the simpler path. A heavier backend may improve throughput while increasing debugging, portability, capture, and deterministic-replay cost. It cannot repair a weak concept-system match.

Compare alternatives fairly: give each candidate enough implementation to reveal its defining behavior, keep the brief and acceptance criteria stable, use comparable fixed seeds where meaningful, and record implementation familiarity as a possible bias. Do not demand identical line counts or polish. Prefer the candidate that gains the most decision-relevant information before expensive commitment.

Preserve reversibility at costly boundaries rather than building generic abstraction everywhere. A disposable prototype may use direct code; its durable outputs are the concept, selected mechanism, rejected rationale, controls, seed policy, and evidence. Commit to an elaborate renderer, multi-system architecture, or public control API only after the representative prototype makes that cost necessary.

## Local Corpus Hierarchy

Classification vocabulary includes `canonical`, `supporting`, `legacy`, `duplicate`, and `conflicting`, but those labels govern retrieval and reconciliation rather than automatic truth. `Canonical` means the compact entrypoint and coordinator of broad defaults. `Supporting` means narrower detail that can constrain the default when its scope matches the task more precisely. `Legacy` identifies historically retained guidance requiring comparison before reuse. `Duplicate` signals no independent support. `Conflicting` is reserved for claims that remain incompatible after version, scope, and target artifact are compared.

| local_source_filepath_value | corpus_hierarchy_role | primary_question_it_answers | contribution_to_preserve | limitation_and_conflict_action |
| --- | --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202604/algorithmic-art/SKILL.md | canonical primary source in the frozen 202604 corpus | What end-to-end workflow, defaults, output order, and guardrails should govern a code-native artwork? | Concept to system to controls to implementation; simple renderer default; seeded repeatability; deliberate color; graceful density reduction; update/render/input separation; software verification. | It is broad and compact. When a narrower source or artifact result appears to differ, compare scope before treating the difference as conflict. |
| agents-used-monthly-archive/codex-skills-202604/algorithmic-art/references/algorithmic-philosophy-template.md | supporting conceptual-detail source | How should an emotional or mathematical premise become behavioral principles and code choices? | One-sentence concept seed, three to five principles, philosophy-to-code mapping, compact parameter suggestions, and the perceptual failure check. | Example language is illustrative. Adapt it to the brief and reject any concept that remains visible only in prose after a representative render. |
| agents-used-monthly-archive/codex-skills-202604/algorithmic-art/references/generative-pattern-menu.md | supporting system-selection source | Which primary family matches the requested motion logic, and which controls expose its meaningful variation? | Seven family cues, candidate controls, and the rule that palette and layers support rather than rescue motion. | It is a menu for choosing, not a composition recipe. Compare only genuinely plausible families and document why one leads. |

**Progressive-disclosure default:** read the canonical skill first. Load the philosophy source when intent, manifesto, or concept-to-code translation is unresolved. Load the menu when the motion model is unresolved. At final review, cross-check the selected decision against the canonical guardrails and the relevant supporting detail. This shortens context while preserving the caveat most likely to reverse the choice.

**Conflict procedure:**

1. State the exact claims that appear incompatible; do not classify a difference in examples or emphasis as conflict.
2. Compare source path, frozen version, scope, target medium, and whether the claim is a default, requirement, or illustration.
3. Check the current user goal and existing project constraints. Relevance does not erase authority, but it determines which source addresses the decision.
4. Choose `keep`, `adapt`, `decline`, or `defer`, and identify the artifact test that could falsify the resolution.
5. Preserve both observations and the result. A local rendered exception may override a default for this artifact without rewriting the general source.

A good hierarchy use reads the skill, opens the menu to compare flow and particles, selects particles for lifecycle semantics, and confirms the choice with a sparse monochrome prototype. A bad use loads only example names from the philosophy template and imitates their tone without a behavior. A justified borderline adaptation produces a static edition even though the skill prefers living motion: the user requested print, recursive growth still carries temporal process spatially, and export inspection verifies the result.

Use a concise source disposition record: `(role, question, extracted constraint, decision, exception, artifact evidence)`. Do not duplicate the full question packet. Verify that the canonical source's highest-risk guardrails survive implementation: one dominant behavior, meaningful controls, declared seed policy, graceful slowdown, and direct rendered inspection.

These role assignments are well-supported corpus organization, not intrinsic authority claimed by the source files. A future refresh may compare a newer active skill, but age alone neither invalidates the frozen material nor proves the replacement. Multiple recurring, relevant, and verified exceptions are a refresh trigger; one unusual artwork is not. This lets the hierarchy learn through deliberate revision instead of silent drift.

## Theme Specific Artifact

Theme-specific artifact: a compact **creative run card** that joins the conceptual seed, primary system, bounded controls, candidate identity, iteration verdict, and export QA. It should remain small enough to diff and review. Link captures and code revisions rather than embedding large outputs, and omit any field that cannot change implementation, comparison, reproduction, diagnosis, or acceptance.

| artifact_field_name | completion_rule | why_the_field_changes_a_decision | evidence_boundary |
| --- | --- | --- | --- |
| `user_goal_statement` | State the requested artifact, intended audience or viewing context, and concrete delivery surface before selecting a system. | Prevents a technically interesting sketch from becoming the wrong medium or product. | User requirement or explicitly stated inference awaiting confirmation. |
| `concept_seed` | Write one sentence naming what behaves, what constrains it, how it changes, and the intended perception or feeling. | Gives family selection and visual critique a causal target. | Source-backed format; actual concept is artistic judgment. |
| `artifact_mode` | Choose static, animated, interactive, seed-driven, or a justified hybrid; name the target temporal states. | Determines lifecycle, capture, accessibility, and export gates. | Requirement plus implementation inference. |
| `primary_visual_system` | Name one dominant family and explain why its motion or spatial logic carries the seed; record a plausible rejected family when ambiguity is material. | Prevents effect stacking and preserves a falsifiable hypothesis. | Local pattern-menu guidance plus prototype evidence. |
| `system_role_map` | For every retained secondary mechanism, state one nonoverlapping concept-bearing or delivery role. | Makes ablation and integration review possible. | Editorial synthesis verified in the render. |
| `parameter_surface` | List each exposed control, safe bounds, baseline value, and intended perceptual effect; include random and noise seeds where replay matters. | Bounds exploration and exposes dead, redundant, or unsafe controls. | Local defaults plus measured sweeps. |
| `renderer_and_structure` | Name the existing or selected renderer and how initialization, update, render, input, reset, and resize responsibilities are separated. | Keeps backend escalation and state behavior reviewable. | Source-backed default adapted to project architecture. |
| `workload_and_delivery_boundaries` | Record target viewports, representative and stress density, interaction, export dimensions, temporal interval, and known device class. | Makes performance and framing claims interpretable. | Task requirements and measured environment evidence. |
| `acceptance_rubric` | Name observable visual criteria, mechanical gates, designated reviewer, rubric version, and stop condition before candidate selection. | Limits random novelty and retrospective preference changes. | Human judgment made explicit; mechanics may be automated. |
| `candidate_identity` | Record code revision, run phase, seed and initialization order, parameters, viewport, temporal state, environment factors, and capture references. | Lets another run reconstruct the compared or exported state. | Direct execution evidence. |
| `iteration_verdict` | Mark keep, simplify, switch, optimize, reject, or accept; state the first material failed or passed criterion and the next action. | Converts observation into controlled feedback rather than another unbounded variant. | Reviewer judgment supported by artifact evidence. |
| `export_qa` | Record export settings and identity, target-state capture, console result, restore result, framing review, and residual uncertainty. | Prevents a selected live state from diverging silently from the delivered asset. | Direct artifact and reviewer evidence. |

Use four lifecycle states:

1. `draft`: concept, family, controls, and criteria may be provisional; broad exploration is allowed and evidence is lightweight.
2. `candidate`: code revision, baseline seed, rubric, viewport, and comparison variables are frozen enough for attributable review.
3. `accepted`: designated software and visual gates pass, the reviewer records a verdict, and the candidate can be restored from the card.
4. `archived_study`: the hypothesis was rejected or delivery deferred, but the card records a reusable learning and does not claim export readiness.

**Filled compact example:**

```text
goal: Animated responsive canvas and selected still; memory should appear to lose cohesion in a slow current.
concept: Discrete memories drift, briefly cluster, fade, and sparsely return under an invisible force.
mode: Animated, seed-driven; inspect startup, 12-second candidate state, and 90-second stability state.
primary_system: Particle lifecycle; low-frequency flow is the force model, not a separate decorative layer.
controls: seed=1842; density=bounded preset; flow_scale, drag, lifetime, trail_decay, palette each have recorded safe ranges.
renderer: Existing 2D canvas; initialization/update/render/input/reset/resize responsibilities are separate.
criteria_v3: slow coherent drift; decay remains legible; monochrome structure holds; intentional empty space; target framing; graceful density reduction.
candidate: code revision + seed + values + viewport + 12-second state + browser/device note + capture references.
verdict: keep particle lifecycle; simplify field detail; reject glow layer because ablation changes spectacle but not a named criterion.
export_qa: restore candidate; capture target viewports; export still at named state; inspect framing and visible pixels; record reviewer acceptance.
```

This example is illustrative, not measured repository output or a prescribed aesthetic. A bad card says only "make it organic" and "looks good," omits seed and temporal state, and links a screenshot unrelated to current parameters. A borderline card may stop after a concept study; it is complete only as `archived_study` with a clear learning, such as "oscillation communicates rhythm but not discrete loss," and must not claim final readiness.

Reproduction can be bounded rather than byte-identical. Browser, GPU, font, floating-point, and timing differences may change pixels even when visual state is acceptably stable; record the environment factors that matter and define the promised level of identity. When deterministic behavior uses separate random and noise streams, preserve both seeds and initialization order.

The local sources directly support the concept, system, controls, seed, renderer-default, and software-verification core. Lifecycle states, rubric versioning, candidate manifests, and export retention are operational inferences added for collaboration and QA. Scale them to the task. One run card should represent one falsifiable visual hypothesis; split independent scenes or systems when they have separate owners, lifecycles, or acceptance gates.

## Worked Example Set

These are hypothetical operational examples, not measured render results. They hold the brief constant so the contrast exposes decision quality rather than unrelated taste: "Make memory feel as if it is losing cohesion in a slow current." Actual aesthetic verdicts must come from actual rendered evidence.

**Good example:**

- **Source use:** The agent reads the canonical skill, opens the philosophy template to sharpen the premise, and uses the pattern menu to compare particles with oscillators. It records that lifecycle, dispersal, death, and sparse respawn make particles the more direct carrier; low-frequency flow remains a force model.
- **Design:** One primary particle system uses bounded lifetime, drag, sparse respawn, and trail decay. The compact surface contains a replay seed plus density, flow scale, drag, lifetime, trail decay, and palette. A monochrome baseline tests behavior before color.
- **Implementation:** Existing 2D canvas is sufficient. Initialization, update, render, input, reset, and resize policy are legible. Density is capped, expired particles leave active state, and the selected seed can be restored.
- **Evidence:** Fixed-seed comparisons vary one convergence control at a time. Captures cover startup, an equivalent mid-state time, long-run stability, and target mobile and desktop framing. A density stress run demonstrates graceful thinning. The reviewer accepts slow coherent drift, perceptible decay, intentional empty space, and structure that survives monochrome.
- **Verdict:** Keep the particle lifecycle; simplify field detail; retain the chosen palette only after structural acceptance. Archive the baseline, selected candidate, one informative rejected oscillator study, and the export manifest.

This process is good because every retained mechanism has a role, comparison is attributable, and both software and aesthetic claims have direct evidence. It does not prove that particles are universally better for memory; it proves why they fit this interpretation and delivery surface.

**Bad example:**

- **Source use:** The agent cites the source paths but extracts no constraint, then adds particles, turbulent flow, phased waves, recursive branches, glow, blur, and a settings dashboard because each looks "generative."
- **Design:** The brief becomes "organic and futuristic." Every run uses fresh randomness. Twelve sliders have unclear effects, several controls overlap, and palette changes are used to hide incoherent trajectories.
- **Implementation:** Rendering mutates simulation state, resize resets unpredictably, offscreen particles never expire, and spawn rate rises without a cap. The shell is polished before a representative art state exists.
- **Evidence:** A single desktop first-frame screenshot and a successful build are reported as completion. No temporal state, mobile framing, console review, fixed seed, density stress, restore test, or designated taste criteria are recorded.
- **Observed consequence:** Reviewers cannot tell which mechanism represents memory or which change improved the piece. A later mobile run clips the canvas and slows until trails become discontinuous. The selected screenshot cannot be regenerated.
- **Recovery:** Restore observability first: freeze one seed and remove the shell from the diagnosis path. Ablate glow, waves, and branches; reduce density; separate update from render; inspect sparse monochrome particles. If lifecycle still does not communicate loss, change the primary system rather than adding another layer.

The example is bad because mechanism, evidence, and brief no longer correspond, not because maximalism, glow, or unseeded art is inherently invalid.

**Borderline example:**

- **Proposal:** A flow field and particle lifecycle both remain visually prominent. The owner argues that the field represents environmental pressure while particles represent memories.
- **Evidence already available:** Fixed-seed output is reproducible and target framing passes. Reviewers perceive drift and decay, but disagree whether field texture adds conceptual pressure or simply visual activity. At stress density, frame stability is near the project boundary.
- **Why judgment remains open:** Two roles are plausible, yet the field may duplicate what particle velocity already communicates. Source guidance prefers one dominant behavior, but it permits justified supporting mechanisms; no universal rule decides this render.
- **Discriminating test:** Produce equivalent-time fixed-seed captures for full field, simplified directional force, and particles without field texture. Keep density and palette constant. Use monochrome, compare concept criteria, inspect frame behavior, and ask whether removing field detail loses a distinct accepted quality.
- **Possible outcomes:** Keep both if field ablation removes a named pressure criterion and runtime remains bounded; simplify to directional force if the concept survives with clearer lifecycle and better stability; switch family if neither version makes loss perceptible.

"Borderline" means the current evidence is insufficient, not that the output is mediocre. The example models a bounded uncertainty statement and names the cheapest test that can turn it into an accept, simplify, or reject decision. A later reviewer may overturn any initial classification when actual renders contradict the narrative.

Across all three cases, reproducibility is a collaboration property rather than proof of artistic merit. The good case makes acceptance and rejection cheap to explain; the bad case has no stable causal anchor; the borderline case preserves one precise open question instead of manufacturing confidence.

## Outcome Metrics and Feedback Loops

Metrics exist to choose the next action, not to manufacture objectivity. Mechanics such as launch, replay, cleanup, bounds, and framing can use binary or measured gates. Aesthetic selection remains reviewer judgment made more accountable through criteria, pairwise comparison, captures, and recorded rationale. Discard any telemetry that cannot support `keep`, `simplify`, `switch`, `optimize`, `reject`, `accept`, or `archive`.

| outcome_or_signal | collection_method | decision_it_should_route | boundary_or_counterexample |
| --- | --- | --- | --- |
| Concept-system legibility | Before candidate selection, write observable criteria; inspect a representative fixed-seed render, monochrome probe, and useful layer ablations. | Keep the family when its defining behavior carries the concept; simplify or switch when explanation carries more meaning than the pixels. | Reviewers may disagree, and monochrome is a probe rather than a universal final-style requirement. |
| Attributable iteration | Freeze baseline code, seed, viewport, temporal state, and rubric; change one convergence variable and compare equivalent states. | Keep the change only when its observed benefit and cost can be named. | Broad exploration may vary several dimensions, but it must be labeled exploration and cannot support a precise causal claim. |
| Control sensitivity | Sweep minimum, representative, and maximum values for each exposed control and record perceptual and runtime effects. | Remove dead controls, merge redundant controls, clamp unsafe ranges, and retain controls with interpretable leverage. | Some nonlinear controls are valid; the requirement is interpretable behavior, not monotonicity in every visual property. |
| Seed robustness | Converge on one baseline seed, then inspect a small declared seed set or label the result a curated edition. | Generalize a preset only when behavior survives the promised variation; otherwise accept one edition with a narrower claim. | There is no universal seed count. The set should expose known composition and density risks for this artifact. |
| Viewport and temporal coverage | Capture each target size at startup, representative mid-state, long-run or stress state, and interaction transitions as required. | Fix framing, resize policy, lifecycle, or temporal saturation before acceptance. | A static fixed-format piece can explicitly narrow this matrix. |
| Runtime envelope | On target-class hardware, record workload, environment, initialization, sampling window, observed frame intervals, long-run resource trend, and degradation event where material. | Bound work, reduce density, cull state, or justify backend escalation when runtime alters motion or interaction. | This reference supplies no universal frame-rate or latency threshold; the project defines the envelope. |
| Restore and export integrity | Reconstruct the candidate from revision, seeds, initialization order, parameters, viewport, temporal state, environment notes, and export settings. | Accept export only when another run reaches the promised state without hidden context. | Cross-platform rendering may support bounded visual equivalence rather than byte identity. |
| Reviewer decision yield | For each review observation, record verdict, affected criterion, evidence, uncertainty, and next action. | Continue only when review narrows a decision or an explicit exploration budget remains. | Short review time is not automatically better; speed without adequate evidence can indicate shallow inspection. |

Use a two-stage loop. **Exploration** searches broadly with coarse prototypes, retains few runs, and asks which concept or family deserves investment. **Convergence** freezes comparison identity, varies one material factor at a time, uses the current rubric version, and accumulates acceptance evidence. Label the phase in every saved candidate so a surprising exploratory result is not mistaken for an export-ready state.

The default causal loop is:

1. Record the current hypothesis, baseline identity, criterion, and smallest useful probe.
2. Render and collect only evidence needed by that probe.
3. Classify the first material failure as concept, system, control, runtime, presentation, or evidence.
4. Choose one routed action and state what result would reverse it.
5. Save a candidate only when it becomes the new baseline, an accepted result, or an informative rejection.
6. Before final acceptance, run seed, viewport, temporal, runtime, restore, and reviewer gates promised by the run card.

Rubrics may evolve after a render reveals a missing quality, but changes must be versioned with rationale before the next comparison. Do not silently rescore earlier captures under new criteria; note that the comparison basis changed. Pairwise review is often more useful than absolute taste scoring because reviewers can point to visible differences, while an ordinal rubric can summarize direction without implying measurement precision.

**Leading indicator:** iteration makes a named concept or delivery criterion more legible under controlled comparison. **Failure signals:** novelty is celebrated without a definition of good output; the seed, rubric, and several parameters change together; one seed or viewport is generalized without evidence; runtime metrics improve while the dominant behavior loses identity; or reviews accumulate observations that produce no next decision.

Stop when required mechanics pass, the designated reviewer accepts the frozen criteria, the candidate can be restored, residual uncertainty is recorded, and another iteration has no named decision value. Pivot when repeated changes fail the same concept-system criterion. Archive a rejected hypothesis when its evidence can prevent circular experimentation. Extend exploration only deliberately; an endless variant stream is not a feedback loop.

Re-run the generated-reference verifier after reference edits. Refresh external sources only when a current external fact could change a claim, and record whether the refresh changed, confirmed, or did not affect the guidance. These process checks complement rather than replace direct artifact evidence.

## Completeness Checklist

Use this gate against one identified candidate, not against the project in the abstract. Begin with `(code revision, run-card version, seed policy, candidate parameters, viewport, temporal state, environment, rubric version)`. Reuse earlier evidence only when those identity fields still match and the checked behavior cannot have changed. Every inapplicable item needs a concrete scope reason; an unexplained omission is a failed gate.

**Routing and evidence**

- [ ] The requested artifact, audience or viewing context, delivery surface, and dominant correctness contract are explicit.
- [ ] This reference is classified as primary, companion, or avoided; companion ownership and integration boundaries are named.
- [ ] The canonical local skill was read, relevant supporting sources were dispositioned, and unrefreshed external mappings are not presented as current facts.
- [ ] Material claims distinguish local source fact, refreshed external fact if any, measured artifact behavior, editorial inference, reviewer judgment, and residual uncertainty.
- [ ] Adopt, adapt, avoid, switch, and cost-of-error decisions name evidence and reversal conditions rather than relying on the inherited scoreboard values.

**Concept and visual system**

- [ ] The concept seed states what behaves, what constrains it, how it changes, and the intended perceptual or emotional effect.
- [ ] Static, animated, interactive, seed-driven, or hybrid mode is chosen with required temporal and interaction states.
- [ ] One dominant system family is named and its motion or spatial logic maps causally to the concept.
- [ ] Every secondary mechanism has one distinct role; useful ablation evidence supports retaining it.
- [ ] At least one plausible alternative was compared or explicitly declined when family ambiguity could materially change implementation.
- [ ] The behavior remains structurally meaningful under a suitable simplification probe, such as monochrome, sparse density, reduced layers, or low recursion depth.

**Controls, state, and implementation**

- [ ] The parameter surface is compact; each exposed control has safe bounds, a baseline, and a perceptible, interpretable effect.
- [ ] Randomness and noise use a recorded replay policy, including seeds and initialization order where repeatability is promised, or intentional ephemerality is explicit.
- [ ] Initialization, update, render, input, reset, resize, and teardown responsibilities are legible enough to inspect and reproduce state transitions.
- [ ] Work is bounded through caps, expiration, culling, pooling, controlled sampling, or another mechanism appropriate to the system.
- [ ] The renderer follows existing project conventions or has a measured behavior, density, dimensionality, interaction, or export reason for escalation.
- [ ] No generic application shell, effect layer, or public control exists without a requirement or concept-bearing role.

**Execution, runtime, and delivery**

- [ ] The repository's actual build or launch path succeeds for the representative state, and relevant console or runtime errors are recorded.
- [ ] Every declared target viewport or fixed-format dimension is inspected with an explicit resize, reset, or recomposition policy.
- [ ] Startup, representative mid-state, stress or long-run state, and required interaction transitions are checked when temporal behavior matters.
- [ ] Representative and stress workload observations use a named environment and project-defined envelope; no universal performance threshold is invented.
- [ ] Graceful degradation restores the envelope while preserving the dominant behavior, or the accepted fixed-capacity boundary is stated.
- [ ] Long-run cleanup and teardown are checked when hidden state, listeners, buffers, trails, or offscreen entities can accumulate.

**Visual acceptance and export**

- [ ] Fresh captures or live evidence show nonblank, correctly framed, readable output in every promised state; a text-only pass is insufficient.
- [ ] The acceptance rubric predates candidate selection or carries a versioned change rationale, and every criterion is observable enough to guide an intervention.
- [ ] The designated reviewer records accept, reject, or bounded uncertainty with rationale and disagreement where relevant.
- [ ] A fixed-seed baseline supports causal comparison, followed by the declared seed-robustness check or an honest curated-edition boundary.
- [ ] The selected export records format, dimensions, temporal state, parameters, and identity; it is inspected separately from the live preview.
- [ ] A second run restores the promised candidate state from the retained record without unrecorded oral setup, within declared environment limits.

**Reference, recovery, and handoff**

- [ ] The repository reference verifier and focused heading, packet, uniqueness, expansion, and forbidden-placeholder checks are run with fresh results.
- [ ] Good, bad, and borderline examples remain operational illustrations and do not claim unrendered configurations were measured.
- [ ] Leading indicators, failure signals, stop conditions, and the next action are recorded; metrics that cannot change a decision are omitted.
- [ ] The accepted candidate, baseline, one materially informative rejection, final evidence, residual risks, and reopening triggers are retained; low-value variant noise is discarded.
- [ ] Adjacent routing names the correct next discipline when this reference ceases to own the dominant failure.
- [ ] Another owner can state what is proven, environment-bounded, artistically judged, intentionally excluded, and still uncertain.

**Completion outcomes:** `accepted_artifact` requires all applicable delivery and restore gates. `archived_study` requires a rendered observation, a falsified or supported hypothesis, and a reusable learning, but must not claim export readiness. `rejected_candidate` records the failed criterion and recovery or route. `blocked_candidate` names the external condition and owner; it is not complete.

An accepted curated edition may intentionally validate one seed rather than claim cross-seed robustness. An ephemeral performance may replace exact replay with a declared nonrepeatability contract and direct live evidence. Those are bounded choices, not loopholes. No inherently visual outcome is complete without the output being observed.

## Adjacent Reference Routing

Route by dominant correctness contract, then resolve the exact local reference or skill through repository context. The categories below are decisions, not invented filenames. Select one primary owner, give each companion a narrow responsibility, and name one owner for integrated acceptance.

| adjacent_discipline_or_workflow | make_it_primary_when | retain_from_this_reference | boundary_and_handoff_evidence |
| --- | --- | --- | --- |
| Raster image generation or editing | The requested result is a specific bitmap, photo transformation, texture, sprite, or visual variant rather than code-native behavior. | Preserve concept, visible acceptance criteria, variant rationale, and export inspection where useful. | Hand off the source image or prompt context, target dimensions, edit constraints, and visual verdict; do not build a canvas runtime merely to deliver one image. |
| Data visualization | Position, size, color, motion, or interaction must truthfully encode data and support interpretation. | Algorithmic behavior may style nonsemantic layers or bounded transitions after semantic mappings are fixed. | Visualization owns scales, labels, data integrity, accessibility, and misleading-encoding checks; integrated QA proves generative styling does not obscure truth. |
| Frontend or application-shell design | Repeated user action, navigation, forms, information hierarchy, settings, responsiveness, and accessibility define success. | Keep the art core independently renderable with declared inputs, lifecycle, dimensions, and workload. | Define art-shell contracts for container size, input events, motion preferences, pause/reset, loading, and performance; the shell must not postpone art proof. |
| Interactive creative tool or playground | The user must author, save, compare, export, or manipulate the system through a polished control surface. | Reuse the compact parameter model, seed manifest, candidate identity, and render QA. | Tool workflow owns state persistence, undo/redo, presets, validation, discoverability, and export UX; this reference still owns whether controls change meaningful visual behavior. |
| Three-dimensional scene or spatial visualization | Depth, camera, lighting, materials, geometry, spatial picking, or 3D navigation is concept-bearing. | Retain concept-system mapping, deterministic state where feasible, workload boundaries, and visual inspection across meaningful states. | A 3D workflow owns scene graph, camera controls, GPU resources, asset loading, and spatial interaction; verify nonblank framing and motion on target viewports. |
| Game development | Rules, physics, player agency, progression, win/loss state, or game feel is the primary artifact. | Algorithmic art may own procedural backgrounds, effects, environments, or generation subsystems. | The game workflow owns rule correctness and input loops; define seed, state, and performance contracts so decorative generation cannot alter gameplay semantics accidentally. |
| Manual graphic, illustration, or brand design | Authored composition, typography, identity consistency, or print production matters more than emergent behavior. | Concept and critique structure may transfer, but a generative system is optional rather than presumed. | Design guidance owns grid, type, brand assets, color standards, and production output; route away when code adds no required variability or interaction. |
| Timeline, simulation analysis, or scenario planning | The user needs causal futures, decision branches, event sequences, or risk comparison rather than an artwork. | A generative visual may later illustrate results, but it must not substitute atmosphere for causal analysis. | Analysis owns assumptions, states, transitions, probabilities if justified, and decision consequences; any art layer remains downstream and nonauthoritative. |
| Audio-reactive or installation work | Sensors, sound, projection hardware, physical dimensions, calibration, or live operation materially shape the piece. | Preserve the creative seed, system roles, parameter policy, degradation behavior, and candidate evidence. | Add domain ownership for signal processing, hardware lifecycle, calibration, failover, and venue tests; browser-preview evidence alone is insufficient. |

**Primary-owner test:** ask which failure would most mislead or harm the user. Wrong data encoding makes visualization primary even if the canvas is visually elaborate. Broken navigation makes frontend ownership primary even if the hero is generative. Incorrect game rules make the game workflow primary even if procedural graphics dominate rendering. For a focused motion study, weak concept-system correspondence makes this reference primary.

**Hybrid contract:** record subsystem owner, inputs, outputs, shared state, lifecycle, error behavior, dimensions, timing, accessibility obligations, workload budget, graceful-degradation order, and evidence. Avoid dual ownership of the same decision. Multiple specialists may review, but one person or agent decides each subsystem and one named owner accepts the integrated artifact.

Good direct use is a seeded canvas study whose generated motion is the entire deliverable. A bad route uses this reference to invent ornamental geometry for a revenue chart before semantic scales are correct. A borderline data-driven artwork assigns data truth and encoding to visualization, gives nonsemantic particle texture to algorithmic art, and runs integrated checks showing that density and motion never conceal values or controls.

Routing is reversible until a representative prototype confirms the dominant model. Record what observation would reverse the route. If uncertain, build the smallest cross-boundary prototype that exercises real data, input, camera, export, or hardware behavior; do not launch simultaneous full implementations. Prototype medium may differ from final owner, so preserve concept and acceptance knowledge while re-verifying backend-specific behavior.

Primary ownership also determines context and backpressure. Each worker receives only the sources and state required by its subsystem. Under shared runtime pressure, degrade the nonprimary decorative layer first unless that would erase the stated artwork; record the priority rather than letting subsystems compete unpredictably.

## Workload Model

`combined_evidence_inference_note`: Treat Algorithmic Art Generation Patterns as a creative artifact operating reference, not as a prose summary. Its basic unit of work is one falsifiable visual hypothesis: one concept-system correspondence that can be prototyped, observed, accepted, rejected, or archived with a reusable learning.

The seed's bounded envelope remains a useful planning default: one artifact family, three representative variants, one accessibility/readability pass, and one render verification path. These quantities are not universal limits. Extend only the dimension that closes a named uncertainty, and split when ownership, lifecycle, evidence, or failure recovery becomes independent.

| workload_dimension_name | default_boundary_or_record | extension_or_split_trigger | verification_pressure_point |
| --- | --- | --- | --- |
| `primary_usage_surface` | One code-native visual artifact or independently testable art subsystem where observable output quality is part of correctness. | The task's primary failure becomes data truth, product interaction, image editing, 3D spatial behavior, game rules, or another adjacent contract. | Confirm primary/companion/avoid routing before broad implementation. |
| `concept_hypothesis_count` | One active concept sentence and one selected interpretation during convergence. | Several concepts require unrelated mechanisms or separate reviewer decisions. | Every retained concept has its own system mapping and stop condition; do not merge slogans into one vague brief. |
| `system_family_count` | One dominant family; a secondary mechanism only for a distinct role. | Two systems have independent state, controls, lifecycle, ownership, or acceptance gates. | Use ablation and role evidence; split genuinely independent systems while retaining an integrated render gate. |
| `exploration_capacity` | A small coarse comparison of genuinely plausible families or parameter regions; retain few informative outcomes. | A new render reveals a materially different hypothesis that current samples cannot discriminate. | Label exploration, state the question, and stop generating when review capacity or concept clarity saturates. |
| `candidate_capacity` | One fixed baseline plus approximately three representative variants from the seed envelope. | Another candidate is needed to test a newly named uncertainty, not merely to add aesthetic variety. | Compare equivalent seed, viewport, temporal state, and rubric version; each candidate receives keep, reject, or next-test disposition. |
| `seed_coverage` | One baseline seed for causal iteration, followed by a small declared robustness set or a curated-edition boundary. | Composition or lifecycle is known to vary materially across random states, or the product promises generative range. | Explain sampling rationale and avoid claiming general robustness from one favorable state. |
| `state_and_viewport_coverage` | Declared target dimensions plus startup, representative, and long-run or interaction states required by mode. | Additional delivery surfaces have distinct framing, timing, input, or accessibility risks. | Add coverage by risk; do not multiply every exploratory variant across every surface prematurely. |
| `accessibility_and_readability_pass` | One dedicated pass, preserving the seed's envelope, after the representative behavior exists. | Motion sensitivity, contrast, input alternatives, or shell integration creates independent requirements. | Verify reduced-motion or pause behavior where applicable, visible structure, and nonoverlapping presentation on target surfaces. |
| `runtime_environment_count` | One representative target-class environment plus a stress case sufficient for the declared delivery scope. | GPU, browser, mobile, installation, or export environments have materially different behavior and are all promised. | Record environment and workload; split platform-specific diagnosis while retaining shared concept evidence. |
| `render_verification_path` | One executable path that can reach and capture the intended state, preserving the seed's original boundary. | Live preview, offline export, installation output, or alternate renderer produces a separately delivered result. | Inspect every delivered path; a passing preview does not validate a distinct export. |
| `source_pressure_model` | Canonical local skill plus only the philosophy or menu supplement needed by the unresolved decision. | Current platform facts, source conflict, or recurring verified exception makes a targeted refresh necessary. | Every additional source changes, confirms, or is declined for a named claim. |
| `artifact_record_capacity` | One run card containing baseline, selected candidate, one materially informative rejection, final evidence, and reopening triggers. | Independent scenes or systems cannot share candidate identity or acceptance without ambiguity. | Split records at independent hypotheses; avoid raw transcript and low-value variant archives. |
| `ownership_capacity` | One owner for the art core and one integrated acceptance owner, with companions bounded by contracts. | Parallel work would require two agents to mutate the same visual state or make the same acceptance decision. | Preserve disjoint write surfaces and reconcile through explicit interfaces and integrated evidence. |

Use different budgets by phase. **Exploration** can vary several factors coarsely but must name the search question and retain little. **Convergence** freezes baseline identity and varies one material factor for attributable comparison. **Acceptance** runs the promised seed, state, viewport, environment, accessibility, runtime, restore, and export matrix only on the selected candidate. This prevents target coverage from multiplying every early study while still proving delivery.

Choose workload shaping deliberately:

- A **vertical slice** is preferred when the largest uncertainty is whether concept, system, renderer, and capture work end to end.
- A **system split** is appropriate when mechanisms have independent lifecycle, controls, or failure recovery.
- A **scene split** fits multi-scene works whose outputs and acceptance can proceed separately.
- A **backend spike** answers one measured feasibility question and remains disposable; it should not become architecture merely because it exists.
- A **platform split** isolates device-specific runtime diagnosis while preserving shared seed and concept evidence where possible.

Keep a compact workload ledger: active hypothesis; source set; family count; baseline and candidate count; seed policy; target states and viewports; environments; evidence paths; owner; unresolved risk; next action; and review capacity. Counts expose drift but do not measure creative difficulty. Every added dimension must close a named uncertainty or meet a declared delivery promise.

**Good bounded work:** one responsive particle study, one primary canvas path, one baseline, three representative candidates, desktop/mobile acceptance, and a restoreable still. **Bad unbounded work:** all seven system families, exhaustive parameter combinations, unlimited seeds, every device, a settings product, and no active hypothesis. **Borderline extension:** a fourth candidate is justified because earlier renders reveal that trail decay and lifetime produce two distinct forgetting behaviors; the new comparison freezes every other factor and names what result will decide.

Apply backpressure at the first saturated stage. If generation outruns review, stop generating and compare. If context no longer holds the active hypothesis, baseline, and next test, checkpoint and split. If runtime evidence cannot be interpreted across platforms, isolate environments. If two owners would edit the same system, serialize or divide by a real interface. The bottleneck is often judgment rather than rendering; restoring attention may improve quality more than producing another batch.

## Reliability Target

Reliability means keeping an explicit promise under stated conditions. It does not mean maximizing every metric or converting aesthetic agreement into a percentage. Separate the **target** from the **observed result**, and for every measured target record population, candidate identity, environment, method, pass condition, exceptions, and scope of the conclusion.

The seed proposed `100 percent` source-boundary preservation, `at least 18 of 20` correct sampled routes, `zero` unsupported production/security/latency/reliability claims, and a recovery path for every avoid or failure case. These are inherited target proposals, not documented observed results. Preserve their strict intent, but do not report them as achieved or universally calibrated without the protocols below.

| reliability_target_name | target_form_and_default_promise | evidence_collection_method | failure_or_boundary_interpretation |
| --- | --- | --- | --- |
| `source_boundary_preservation` | Hard invariant for every material evidence-backed recommendation: identify inspected local fact, refreshed external fact if any, measured behavior, or explicit inference/judgment. | Parse and review claim records; verify named sources were actually read or honestly marked unrefreshed. | "100 percent" is a valid desired invariant only after the recommendation population is defined and counted; it is not an observed result here. |
| `unsupported_claim_rejection` | Hard gate: no final production, security, latency, reliability, platform, or artistic-universality claim lacks evidence, method, or uncertainty. | Search claims, trace source or run evidence, and challenge whether the evidence supports the stated scope. | The seed's zero target is normative. A detected unsupported claim blocks that claim and must be removed, bounded, or verified. |
| `routing_decision_quality` | Sample-based target defined by the team before evaluation; each task receives primary, companion, avoid, or escalate routing plus rationale. | Build a representative, noncherry-picked task set; hide expected verdict where practical; record reviewer agreement, disagreements, and error consequence. | The inherited 18-of-20 proposal requires a declared sample composition and adjudication rule. One sample does not establish universal routing accuracy. |
| `recovery_path_clarity` | Hard invariant for every documented failure or avoid decision: name rollback, simplification, switch, escalation, owner, or adjacent route. | Cross-check anti-patterns, failure modes, routing, and candidate verdicts against next actions and reopening conditions. | A path is not clear when it says only "retry" or points to a generic adjacent theme without ownership and evidence. |
| `render_presence_and_framing` | Every promised visual state is directly observed and nonblank, correctly framed, readable, and free of incoherent overlap or clipping. | Fresh viewport- and state-labelled captures, pixel-presence probe where blank output is plausible, console review, and designated visual inspection. | A passing build, launch, or reference verifier cannot satisfy this gate. Fixed-format work may narrow viewports explicitly. |
| `seed_and_state_replay` | Reproducible profile: recorded seeds, initialization order, controls, viewport, and state restore the promised class of output; curated profile: one edition restores; ephemeral profile: nonrepeatability is declared and accepted live. | Repeat candidate runs and compare state or visual output at equivalent temporal points in the declared environment. | Cross-platform pixels may differ; define bounded visual equivalence when byte identity is neither feasible nor promised. |
| `control_bounds_and_meaning` | Every exposed control remains safe over its documented range and produces a perceptible, interpretable effect. | Minimum/representative/maximum sweeps, invalid-input checks, runtime observations, and reviewer description of effect. | Nonlinear behavior is allowed; dead, redundant, or runaway controls fail until removed, merged, or bounded. |
| `viewport_and_temporal_coverage` | The candidate passes every declared delivery dimension and meaningful startup, mid-state, long-run, and interaction transition required by its mode. | Risk-based state/viewport matrix with fresh evidence tied to candidate identity. | Do not generalize beyond tested surfaces. A static or fixed installation can declare a narrower matrix. |
| `runtime_envelope` | Project-defined workload and environment remain within a measured frame, memory, interaction, or completion-time envelope appropriate to delivery. | Record target-class hardware/browser, workload, warmup, sample window, distribution or trend relevant to the claim, and stress behavior. | This reference supplies no universal threshold. A local observation is not a cross-device guarantee. |
| `graceful_degradation_identity` | When capacity is exceeded, bounded work or density reduction restores the envelope while the dominant concept-bearing behavior remains perceptible. | Compare fixed-seed normal and degraded states against both runtime and visual criteria. | Meeting timing by erasing lifecycle, rhythm, composition, or interaction is a failed degradation strategy. |
| `restore_and_export_integrity` | A second run recreates the selected live or export state from retained revision, seeds, controls, viewport, temporal state, environment notes, and export settings. | Independent restore attempt plus inspection of the delivered file, not only the preview. | Missing external assets or platform differences become named dependencies and scope limits rather than hidden setup. |
| `aesthetic_acceptance` | The designated reviewer accepts the candidate against a versioned set of observable criteria and records rationale and uncertainty. | Pairwise comparison, rubric notes, monochrome or ablation probes where useful, and final verdict. | This is bounded judgment. Reviewer agreement is evidence of acceptance ownership, not objective beauty or population-wide preference. |

Choose a reliability profile before testing:

- **Reproducible candidate:** promises replay, control stability, target-surface behavior, runtime envelope, visual acceptance, and restore/export.
- **Curated edition:** promises one named seed or state and its restore path; it does not claim robust output across arbitrary seeds.
- **Ephemeral run:** explicitly rejects exact replay but promises live execution, bounded workload, framing, safety, and observed concept behavior.
- **Interactive tool:** adds input validation, persistence or reset policy, control semantics, accessibility, and repeated-session behavior owned by the tool workflow.

A good target says: "On the named mobile browser and workload, the selected edition remains within the project frame envelope for the declared interval; fixed-seed degraded density preserves slow coherent drift; observed result and capture are attached." A bad target says: "Runs at 60 FPS everywhere," with no environment, sample, artifact identity, or evidence. A borderline but valid target says: "Only seed 1842 is accepted as this edition; other seeds were not evaluated for composition," avoiding a false robustness claim.

Include one adverse case for each material promise: maximum supported density, resize, reset, long-run cleanup, invalid control, layer ablation, or an alternate seed as appropriate. A beauty-state-only pass is selection bias. Sample risks deliberately, publish exclusions, and rerun only gates affected by a bounded change. If controls change, repeat control and candidate evidence; if renderer changes, repeat runtime, determinism, framing, and export; if only prose clarification changes, rerun reference structure and claim traceability.

Narrow, honest reliability creates more trust and future option value than a broad untested guarantee. A candidate may complete with known uncertainty only when its consequence, owner, reopening trigger, and excluded claim are explicit.

## Failure Mode Table

This table addresses observed symptoms and recovery. The anti-pattern registry addresses practices that make those symptoms likely. For a material failure, preserve candidate identity and one safe failing state where possible, then follow `detect -> contain -> diagnose -> correct -> verify -> record`. Contain crashes, runaway resources, data corruption, or unsafe interaction immediately; restore reproducible evidence as soon as practical.

| failure_mode_name | observable_signal_and_likely_causes | immediate_containment | root_correction_options | proof_of_recovery_and_escalation |
| --- | --- | --- | --- | --- |
| Source drift hides truth | A local path, public page, or extracted rule no longer matches the claim; inherited external mappings are presented as current. | Mark affected claims unverified and stop reusing them as fact. | Re-read frozen local sources; perform a claim-triggered primary-source refresh when allowed; compare scope and record keep/adapt/decline. | Trace every affected recommendation to current evidence or bounded uncertainty. Escalate source conflicts that can change ownership or delivery. |
| Generic advice escapes review | Guidance sounds plausible but names no local rule, artifact decision, or verification gate. | Block the claim from final guidance. | Replace it with source-scoped guidance, direct artifact evidence, explicit reviewer judgment, or remove it. | A reviewer can identify the next action, evidence, stop condition, and what would reverse the recommendation. |
| Rendered output was not inspected | Build and prose pass while output is blank, clipped, obscured, unreadable, or in the wrong temporal state. | Stop completion claims and capture the actual target state. | Inspect console and canvas dimensions; verify initialization, assets, camera or transform, visibility, resize, and state timing. | Fresh target-state evidence shows visible pixels and correct framing. Escalate renderer or asset failures with exact runtime evidence. |
| Variant search becomes random | Seed, code, controls, palette, viewport, and rubric change together; novelty replaces a decision question. | Freeze a baseline and pause new generation. | Label exploration versus convergence; restore fixed identity; choose one criterion and one material variable; retain few variants. | Equivalent-state comparison yields keep, reject, or next-test rationale. Escalate to concept selection when no criterion can be named. |
| Concept is invisible despite valid execution | The sketch moves and renders but reviewers cannot perceive the intended premise without explanatory prose. | Stop downstream polish and effect additions. | Simplify to the dominant mechanism; use monochrome or ablation; revise philosophy-to-code mapping; compare or switch primary family. | Representative renders make the named behavior perceptible to the designated reviewer. Archive a falsified concept rather than forcing it. |
| Candidate cannot be reproduced | The selected image or motion state cannot be regenerated, or identical instructions produce unexplained divergence. | Preserve current output and environment; avoid destructive cleanup of evidence. | Record code revision, random/noise seeds, initialization order, controls, viewport, temporal state, assets, and environment; separate update from render. | A second run restores the promised class of state. If ephemerality is intentional, change the reliability profile and collect direct live evidence. |
| Control is dead, redundant, or unsafe | A control has no visible effect, duplicates another, causes abrupt instability, or drives invalid numeric or resource state. | Hide or disable the control from accepted surfaces. | Sweep bounds; clamp or validate input; merge correlated controls; redesign mapping; keep it internal until behavior is interpretable. | Minimum, representative, maximum, and invalid cases pass with recorded perceptual effects and bounded workload. Route tool-UX concerns to the companion owner. |
| Resize or framing corrupts the composition | Target dimensions crop content, stretch geometry, reveal blank regions, overlap UI, or silently create a different edition. | Restore the last known valid viewport and record the failing size. | Use normalized coordinates or a deliberate recomposition policy; define buffer recreation and seed/reset behavior; fix container and pixel-ratio assumptions. | Every declared viewport passes fresh visual inspection with documented resize semantics. Fixed installations may constrain dimensions explicitly. |
| Temporal state saturates, disappears, or drifts | Trails fill the frame, particles die permanently, oscillation loses intended phase, or long-run behavior diverges from the accepted state. | Cap run duration or pause at a safe state when delivery allows. | Bound accumulation; correct lifecycle and respawn; stabilize integration; sample equivalent times; revise decay or reset policy. | Startup, representative, and long-run states satisfy the temporal rubric. Escalate numerical or simulation-specific faults with a minimal replay. |
| Runtime collapse changes artistic identity | Frame intervals grow, input lags, animation jumps, export stalls, or memory rises under representative or stress work. | Reduce density or disable nonessential layers; cap spawn/update work. | Cull invisible state, expire entities, pool resources where useful, reduce sampling, optimize measured hotspots, or justify renderer escalation. | The project-defined envelope returns and fixed-seed degraded output preserves the dominant behavior. Faster but conceptually erased output is not recovery. |
| Invisible state or listeners accumulate | Visible density appears stable while CPU, memory, buffers, events, or offscreen entities grow across time, reset, or remount. | Stop repeated mounts or long-running sessions and capture resource trend. | Add expiration, teardown, listener removal, buffer reuse, culling, and lifecycle ownership. | Long-run, reset, and teardown observations show bounded state with no duplicate updates. Escalate host-shell lifecycle issues to its owner. |
| Export diverges from accepted preview | The delivered still or recording has different dimensions, timing, color, assets, density, seed, or framing from the reviewed live state. | Preserve both preview and export identities and halt replacement of the accepted asset. | Record export settings; use a named temporal state; load required assets deterministically; inspect the delivered file separately. | Restore and regenerate the export from its manifest, then obtain a fresh visual verdict. Route codec or production constraints to the relevant workflow. |
| Ownership or route collision | Two agents mutate the same art state, product shell overrides art constraints, or data/game semantics become subordinate to decoration. | Freeze overlapping edits and identify the dominant correctness contract. | Assign one owner per subsystem and integrated acceptance; define input/output/lifecycle/performance contracts; reroute category errors. | Disjoint work passes subsystem and integrated gates. Escalate unresolved ownership rather than merging conflicting implementations. |

Do not select a row by resemblance alone. First record the candidate revision, seed policy, parameters, viewport, state, environment, and symptom. State at least two plausible causes when evidence is weak, then choose the cheapest test that separates them. A visual slowdown may come from density, invisible accumulation, resize pixel ratio, or host-shell re-rendering; optimizing the most familiar loop without evidence can move or worsen the failure.

**Confirmed example:** seed 1842 reproduces clipping at the declared mobile viewport while desktop remains correct. The agent captures both, fixes normalized framing without changing simulation parameters, reruns all target sizes, and records that composition and temporal state remain stable. **Unsupported diagnosis:** "the work looks flat, so add more noise" names neither reviewer criterion nor causal evidence; restore monochrome and ablation comparisons before changing the system. **Bounded uncertainty:** one reviewer experiences stress-density motion as frantic while another accepts it; preserve both observations, compare the declared calm-motion criterion at normal and degraded density, and let the designated owner decide rather than averaging away the concern.

Recovery evidence must test the original symptom and the most likely adjacent regression. A density fix checks both runtime and concept identity. A resize fix checks framing and seed/reset policy. A control fix checks safety and visual meaning. A renderer change establishes a new baseline and reruns runtime, determinism, viewport, and export gates because direct pixel identity may no longer be meaningful.

After recovery, record recurrence, residual risk, rollback, owner, and whether an earlier gate should change. Promote new prevention only for recurring, high-consequence, or broadly causal failures. One local taste rejection should remain local; a repeated blank-render escape justifies an earlier pixel-presence gate. The best prevention is the smallest upstream check that would have exposed the same failure cheaply.

## Retry Backpressure Guidance

A retry is an experiment intended to change knowledge about a failure. Before spending it, preserve one safe failing state where possible and record `(candidate identity, failed claim, observed signal, failure class, hypothesis, controlled change, expected discriminator, budget, owner, stop condition)`. Running again without that record is justified once only when the experiment is explicitly testing whether the signal was transient.

| failure_or_blocker_class | eligible_next_action | retry_discipline | stop_or_escalation_condition |
| --- | --- | --- | --- |
| Transient launch, capture, or environment interruption | Repeat the same command or capture with unchanged candidate identity and record environment state. | One identical confirmation distinguishes a transient from a repeatable failure; do not alter art code simultaneously. | Repetition converts the issue into a reproducible execution failure requiring diagnosis. |
| Stale local or external evidence | Re-read the frozen local source or perform one claim-specific primary-source refresh when browsing is permitted. | Preserve old and new claims, scope, checked date, conflict, and decision impact. | If one bounded refresh cannot resolve material conflict, escalate to the source owner, a narrower reference, or explicit uncertainty; do not broaden search indefinitely. |
| Missing candidate or context identity | Stop implementation and restore revision, seed policy, parameters, viewport, temporal state, rubric, and latest evidence. | Resume from the first explicit next step after snapshot; avoid guessing shifted state. | If the accepted state cannot be reconstructed, classify it as a recovery failure or curated-output loss rather than continuing blind. |
| True source or requirement contradiction | State both claims, compare authority, relevance, version, scope, and user goal, then design a discriminating prototype or seek owner judgment. | Change no broad architecture until the contradiction's decision consequence is clear. | Escalate when the conflict changes primary ownership, irreversible delivery, safety, or a requirement only the user can resolve. |
| Concept or visual-family mismatch | Simplify, use monochrome or ablation, compare one plausible family, or archive the hypothesis. | Preserve the brief and failed criterion; establish a new baseline when system identity changes. | Stop polishing when repeated variants fail the same concept criterion; switch or return to concept selection. |
| Control or state failure | Freeze seed and state, sweep or isolate one control, validate bounds, and separate state transitions as needed. | One retry may include coordinated code edits only when they implement one shared hypothesis, such as removing render-side mutation. | Escalate to tool or host owners when persistence, input, or lifecycle outside the art core causes the failure. |
| Runtime overload or resource growth | Contain by reducing density or disabling nonessential layers; instrument the measured hotspot or lifecycle leak. | Change one workload cause, replay equivalent normal and stress states, and verify concept identity as well as timing. | Stop local micro-optimization when the simple renderer cannot meet a measured required behavior; justify backend escalation. |
| Blank, clipped, or temporally wrong render | Preserve console, dimensions, state time, capture, and candidate identity; inspect initialization, visibility, resize, assets, and transforms. | Correct the smallest likely presentation or lifecycle cause and recapture every affected target state. | Escalate renderer, asset, camera, or shell integration failures with exact evidence rather than generic screenshots. |
| Ownership or write collision | Freeze overlapping changes, identify primary correctness, and restore one owner per mutable subsystem. | Resume only after inputs, outputs, lifecycle, and integrated acceptance responsibilities are explicit. | Escalate unresolved authority instead of merging competing state models or overwriting another worker. |
| External unavailable state | Preserve the last reproducible baseline and wait, reroute, or narrow work to independent evidence. | Do not churn local code to simulate a service, device, venue, approval, or source state that owns the blocker. | Resume when the external condition changes or the owner deliberately changes scope. |
| Review or candidate backlog | Stop new generation, group candidates by the active criterion, discard low-information runs, and compare a bounded set. | Generation resumes only after reviewers select, reject, or name a new discriminating question. | Escalate decision ownership when disagreement or absence of a reviewer, not rendering capacity, is the bottleneck. |

Separate phases. During **exploration**, a bounded variant budget may deliberately vary several dimensions to discover promising concepts, but every retained run needs a learning. During **convergence**, freeze baseline identity and change one material factor per comparison. During **acceptance**, do not retry a failing gate by weakening or silently changing the rubric; version any legitimate requirement change before producing new evidence.

Apply backpressure at the saturated stage:

- **Generation pressure:** stop producing variants when the active question is missing or retained candidates exceed review capacity.
- **Review pressure:** present fewer equivalent-state comparisons and name the decision owner; more renders cannot resolve ownerless taste.
- **Context pressure:** checkpoint hypothesis, baseline, exact failing gates, files, risks, and next action; reread the current specification before broad edits.
- **Runtime pressure:** cap work and preserve a stable diagnostic state before optimization or renderer migration.
- **Source pressure:** narrow to the claim that can alter implementation; record unrefreshed external facts honestly.
- **Ownership pressure:** keep one owner per generated file or mutable subsystem and verify path, heading, packet, evidence, and integration invariants at handoff.

**Good retry:** mobile clipping reproduces under seed 1842, unchanged controls, and a named viewport. The hypothesis is coordinate scaling; the agent changes only normalized framing, recaptures all target sizes, verifies no reset or composition regression, and closes the retry. **Bad retry:** "make it more organic" regenerates with a new seed, higher density, changed colors, and extra noise until one image is preferred; no cause is tested. **Borderline coordinated retry:** a renderer migration changes several files but tests one measured hypothesis that the current renderer cannot sustain required density; it establishes a new baseline and reruns determinism, framing, runtime, and export gates.

Retain disproven hypotheses when they were expensive or likely to recur. Count retry budget by unchanged hypothesis rather than shell commands: diagnosis, implementation, and recapture may form one experiment. Budgets are local policy based on consequence and information value; the seed's one bounded stale-evidence refresh is a conservative default, not a universal law.

Resume only when the retry can distinguish the suspected cause, the saturated resource has capacity, or the external condition has changed. Strategic waiting preserves the last reliable baseline; continued local modification during an external blocker often destroys the evidence needed when work can resume.

## Observability Checklist

Observability is selective decision memory, not total surveillance of the creative process. Retain an observation only when a named consumer uses it for reproduction, diagnosis, comparison, acceptance, source refresh, backpressure, or handoff. Raw diagnostic data may exist briefly, but summarize the decision and expire the noise after the failure is understood.

**Core candidate event:**

- `run_phase`: exploration, convergence, acceptance, recovery, or export;
- `candidate_identity`: code revision, run-card version, seed and initialization order, parameters, viewport, temporal or semantic state, renderer, and material environment factors;
- `active_hypothesis`: the concept, control, runtime, or delivery claim being tested;
- `source_disposition`: local paths loaded, intentionally skipped sources with reasons, and any external mapping refresh status;
- `evidence`: exact command and result summary, fresh capture or video reference, state snapshot, runtime observation, and relevant console outcome;
- `rubric_identity`: criteria version, designated reviewer, verdict, rationale, disagreement, and bounded uncertainty;
- `decision`: keep, simplify, switch, optimize, reject, accept, archive, wait, or escalate;
- `next_trigger`: the evidence, source change, external state, or requirement that will resume or reopen work;
- `retention_reason`: baseline, selected candidate, informative rejection, regression evidence, or final export.

| claim_or_decision | smallest_useful_observation | conditional_addition | main_limit_or_cost |
| --- | --- | --- | --- |
| Source-backed guidance | Loaded path, extracted constraint, decision impact, and explicit unrefreshed status for external mappings. | Checked date, relevant heading, and conflict record after a permitted primary-source refresh. | Path presence alone does not show that the source was understood or applicable. |
| Concept-system fit | Representative fixed-seed render, named visual criterion, and reviewer rationale. | Monochrome probe, layer ablation, or pairwise family comparison when mechanism roles are uncertain. | The result is designated judgment, not proof of universal preference. |
| Reproducibility | Revision, seeds, initialization order, controls, viewport, state, environment, and second-run result. | State snapshot or visual-difference aid when precise replay matters. | Instrumentation and cross-platform rendering may alter timing or pixels; define the promised equivalence. |
| Control behavior | Bounded sweep with input value, visible effect, runtime effect, and invalid-state result. | Trace or state snapshot for nonlinear interactions that cannot be understood from captures alone. | Large combinatorial sweeps create evidence that exceeds review capacity. |
| Framing and visibility | Fresh capture for every declared viewport and state, plus console result. | Pixel-presence or canvas-bound probe when blank or offscreen output is a recurring risk. | Screenshots do not establish motion, interaction, or long-run stability. |
| Temporal behavior | Time- or state-labelled samples covering startup, representative, and required long-run or interaction transitions. | Short video, live-review note, or state trace for motion qualities that stills cannot express. | Wall-clock time alone is ambiguous when performance changes system age; retain semantic or frame context. |
| Runtime envelope | Environment, workload, initialization, sample window, observed frame intervals or completion times, and degradation event. | p50, p95, p99, memory trend, or trace only when sample size, population, and decision threshold make them meaningful. | Small samples, nonstationary animation, device variation, and instrumentation overhead can make percentiles misleading. |
| Reviewer workflow | Reviewer, rubric version, evidence viewed, verdict, rationale, uncertainty, and next action. | Decision-time measurement only with task complexity and outcome if review throughput is an actual bottleneck. | Faster review is not necessarily better and can reward shallow inspection. |
| Recovery | Failing candidate, reproduced symptom, hypothesis, controlled change, after-state, adjacent regression result, and residual risk. | Trace, resource sample, or cross-subsystem evidence appropriate to the cause. | A fix report without replay of the original symptom does not prove recovery. |
| Export | Export settings, dimensions, temporal state, output identity, restore path, and separate visual verdict. | Codec, color, asset, or platform metadata when those can change delivery. | A correct live preview is not evidence for a separately generated asset. |

**Phase depth:** exploration needs a concept question, enough candidate identity to learn from a run, and a visual observation; retain little. Convergence freezes identity and adds comparable evidence. Acceptance adds every promised viewport, state, environment, restore, export, and reviewer gate. Ephemeral work replaces exact replay with live-state evidence and an explicit nonrepeatability promise, while installations add hardware and long-run observations through their companion workflow.

**Quality checks:**

- Every evidence item matches the current candidate or is labelled historical.
- Every metric names population, environment, sample window, threshold or intervention, and conclusion scope.
- Every capture names viewport and temporal or semantic state.
- Runtime and visual evidence share candidate identity; do not pair the fastest run with the most attractive render.
- Instrumentation overhead is noted when it can change timing or interaction.
- No secrets, private user content, or host-prohibited telemetry enters the creative run record.
- Every retained variant has a decision reason; temporary raw output has an expiry.
- The evidence store is durable enough for the declared handoff, and essential results are summarized when links may disappear.

**Good record:** one compact candidate event links seed 1842, exact controls, mobile and desktop captures at equivalent state, a density observation, rubric version, reviewer acceptance, export settings, and restore result. **Bad record:** an unlabelled console transcript, percentile chart with no sample window, and screenshot from unknown parameters. **Bounded qualitative record:** an ephemeral live performance note names reviewer, venue state, calm-motion criterion, observed instability, instrumentation limits, and the next rehearsal test without pretending exact replay is available.

Test observability itself. Deliberately replay a seed, resize, increase density, reset, or cause another safe high-risk perturbation; confirm that the evidence identifies the candidate and routes a next action. An undetected blank render, stale capture accepted as current, or accepted state that cannot be reconstructed is an observability failure even after the art bug is fixed.

The best durable packet is smaller than a transcript because it preserves decisions rather than chronology. Uncertainty intrinsic to the artwork may remain; the record should make that uncertainty visible without biasing the system toward only what is easy to measure.

## Performance Verification Method

Performance is both computational and perceptual. Slow or uneven execution can change rhythm, decay, trails, interaction, and the apparent force of a system; an optimization can also destroy the behavior that made the work meaningful. Require direct rendered-output inspection and reject text-only success claims for a visual or interactive artifact.

Define the promise before measuring:

- artifact mode and delivered path: static preview, animation, interaction, live installation, recording, or offline export;
- candidate identity: revision, seeds, controls, viewport, temporal or semantic state, and renderer;
- target-class environment: relevant device, browser or runtime, display context, and material platform conditions;
- representative and stress workload: entity count, spawn behavior, samples, recursion, trails, buffers, interaction, duration, and export dimensions as applicable;
- project envelope: user-visible frame behavior, interaction response, resource trend, or completion-time requirement, with a reason;
- graceful-degradation policy: what work reduces first and which concept-bearing behavior must remain;
- evidence scope: which environments and states the conclusion covers and which remain untested.

Use staged gates so exploration stays fast without weakening acceptance:

| performance_stage | minimum_protocol | decision_enabled |
| --- | --- | --- |
| Quick exploration | Launch a minimal fixed-seed state, inspect visible output, note gross frame or interaction failure, and avoid elaborate profiling. | Decide whether the concept-system prototype deserves further work or a simpler mechanism. |
| Representative candidate | Separate initialization from steady behavior; run the target viewport and normal workload after an appropriate warmup; observe frame intervals or completion time plus the rendered state. | Decide whether controls, density, renderer, and composition are viable for convergence. |
| Stress and degradation | Increase only the declared stress dimension, capture the failure boundary, activate bounded degradation, and compare fixed-seed normal/degraded visuals. | Set safe caps or presets, change work bounds, optimize a measured cause, or justify platform scope. |
| Long-run and lifecycle | Observe the promised duration, reset, resize, remount or teardown, resource trend, and accumulated state. | Detect leaks, temporal saturation, duplicate listeners, stale buffers, or lifecycle drift. |
| Final export or delivery | Measure the actual delivered path separately, inspect output dimensions/state/assets, and perform restore from the candidate manifest. | Accept, narrow, or reject the delivery promise; a live preview cannot stand in for a distinct export. |

Choose the method according to the claim:

| performance_claim | useful_evidence | when_more_detail_is_warranted | caution |
| --- | --- | --- | --- |
| Animation smoothness or stability | Frame-interval samples or another user-visible cadence observation tied to workload and state. | Use distributions and inspect spikes when intermittent stutter changes perception; use traces only to discriminate causes. | Average FPS can hide disruptive episodes, and display refresh or background throttling can distort interpretation. |
| Interaction response | Input-to-visible-state observation under representative workload with event and render state aligned. | Add traces or state timestamps when delay source is uncertain. | Instrumentation may perturb the same interaction being measured. |
| Memory or lifecycle stability | Active entity/buffer/listener counts and resource trend across the declared duration, reset, and teardown. | Profile allocations or retainers after a reproducible upward trend appears. | One short run cannot establish long-run bounds; visible density can remain stable while hidden state grows. |
| Offline render or export | Wall-clock completion, output integrity, dimensions, peak resource concerns where material, and separate visual inspection. | Repeat runs or sample several inputs when the product promises batch behavior. | A slow export can be acceptable if its explicit completion boundary and operational context allow it. |
| Reference-authoring workflow | Input size, inspected source count, tool calls only when they affect process cost, wall-clock duration, reviewer decision, and whether the next action is clear. | p50, p95, or p99 may be useful only with a defined repeated-task population and enough observations. | Reviewer speed without quality and complexity context is a vanity metric. Documentation timing does not validate artwork runtime. |

Percentiles are conditional tools, not mandatory decoration. Report p50, p95, or p99 only when the sampled population, observation count, warmup, window, environment, and decision threshold are stated and the distribution answers a real claim. Small samples, nonstationary animation, garbage collection, thermal state, device pixel ratio, background tabs, and profiler overhead can make precise-looking summaries misleading. Record these factors when they materially affect the conclusion rather than pretending to eliminate all variability.

For time-based simulations, distinguish simulation-step stability from render cadence when dropped frames could alter physics or lifecycle. Use elapsed time, fixed steps, or another deliberate model consistent with the piece; verify behavior under slower rendering rather than assuming frame count and time are interchangeable. Platform-specific implementation details require current project or primary documentation when they become material.

**Required candidate packet:** target and rationale; candidate identity; environment; normal and stress workloads; initialization/warmup; sampling window; raw or summarized observation appropriate to the claim; fixed-seed normal/degraded captures; rubric verdict on preserved identity; observed result; uncertainty; excluded environments; and retest trigger. Repeat enough to distinguish a stable local observation from a one-run anomaly, but do not claim population behavior from one machine.

**Pass:** the declared project envelope holds on tested surfaces, or bounded degradation restores it while the concept-bearing mechanism remains perceptible; the delivered render is visible and correctly framed; the reviewer knows the next action and stop condition. **Fail:** metrics pass only after removing the artwork's identity, evidence belongs to another candidate, only a happy beauty state is tested, or performance is claimed without environment and workload. **Borderline:** a high-density preset exceeds the default envelope but can be retained when clearly labelled, optional, and visually and operationally bounded while the default remains stable.

After optimization, replay the original symptom and one adjacent regression. A density correction verifies runtime and composition. A renderer migration establishes a new baseline and reruns seed, viewport, frame, and export evidence. A faster result is not recovery when it moves cost to initialization, leaks state over time, or damages the accepted visual criterion.

Performance findings can change artistic design legitimately. Entity count, trail persistence, spatial scale, update cadence, and temporal integration are compositional parameters. Systems that retain identity under simplification are easier to deploy widely; intentionally extreme work may instead choose fixed hardware or offline delivery, but its boundary and failure behavior remain explicit.

## Scale Boundary Statement

This reference is sufficient while one bounded code-native visual hypothesis has one dominant system, compact controls, one primary renderer, known delivery surfaces, directly inspectable states, and one owner who can reproduce failures and accept evidence. Technical difficulty alone does not force a split: a dense shader or recursive system may remain one coherent core when concept, state, lifecycle, and recovery are singular.

It stops being sufficient as the sole workflow when a new surface has independent correctness, state, lifecycle, ownership, delivery, or recovery that this guide cannot verify. Add a domain companion or hand off primary ownership rather than stretching algorithmic-art language over an unowned contract.

| scale_dimension | boundary_crossing_signal | response_options | retained_algorithmic_art_contract | integrated_proof |
| --- | --- | --- | --- | --- |
| Multiple visual systems | Systems have independent state, controls, lifecycles, owners, or acceptance and can fail separately. | Simplify to one carrier; extract subsystems; or keep a justified coupled model with one owner. | Shared concept, explicit role map, random-stream ownership, workload priority, and ablation evidence. | Subsystem gates plus one render showing intended interaction and degradation order. |
| Multiple scenes or outputs | Scenes have separate candidate identities, exports, viewports, timelines, or reviewer verdicts. | Split run cards and ownership by scene while sharing stable palette or concept constraints deliberately. | One concept hierarchy and clear rules for what must remain consistent. | Each scene restores independently and the complete sequence or installation receives integrated review. |
| Product or authoring shell | Saving, undo, presets, forms, navigation, accessibility, and repeated user workflows become first-class. | Add a frontend or creative-tool workflow through a narrow art-core API. | Meaningful controls, seed/state manifest, render lifecycle, dimensions, and performance envelope. | Real user flow manipulates and exports the art without invalid states or visual regressions. |
| Three-dimensional behavior | Camera, depth, lighting, materials, spatial picking, scene resources, or geometry becomes concept-bearing. | Add a 3D workflow or migrate ownership; retain a simple 2D prototype only as concept evidence. | Concept-system correspondence, deterministic state where promised, workload bounds, and visual acceptance. | Nonblank target-viewport captures, meaningful camera states, interaction, resource cleanup, and integrated visual verdict. |
| Audio, sensors, or physical installation | Signal processing, calibration, projection hardware, venue geometry, failover, or live operation determines output. | Add specialized signal/hardware/operations ownership; constrain supported venue when appropriate. | Parameter intent, live-state criteria, graceful degradation, and declared ephemerality or replay policy. | Venue-class rehearsal covers calibration, failure behavior, framing, timing, and operator recovery. |
| High-resolution or offline production | Delivered output uses a separate renderer, tile process, codec, color path, long job, or memory envelope. | Add export/production workflow, constrain format, or isolate an offline renderer. | Candidate identity, seed, temporal state, composition criteria, and export manifest. | Delivered file is reconstructed and inspected separately from preview; failure and resume behavior are bounded. |
| Multi-platform delivery | Browser, mobile, GPU, installation, recording, or other promised surfaces have materially different behavior. | Narrow platform support; split platform diagnosis; or establish a shared core with adapters. | Shared system semantics and profile-specific workload, resize, input, and evidence. | Each promised surface passes local gates and equivalent concept behavior is reviewed across them. |
| Production traffic or multi-user state | Concurrent sessions, persistence, isolation, abuse, availability, or operational recovery becomes user-facing. | Add backend, security, persistence, and operations ownership with explicit SLOs and data contracts. | Visual state schema, seed policy, bounded rendering client, and user-visible degradation. | End-to-end tests cover state correctness, failure isolation, load boundary, and rendered recovery; this art guide alone is insufficient. |
| Distributed agent execution | Parallel workers would edit the same file, state model, scene, or acceptance decision. | Preserve one owner per generated file or mutable subsystem; serialize shared decisions; merge through contracts. | Exact paths, heading/evidence invariants, candidate identity, and one integrated visual owner. | Scoped tests pass independently, then merge-time state and render evidence confirms no semantic drift. |
| Long-running context | The active hypothesis, baseline, exact failing gate, or next action no longer fits reliably in working context. | Checkpoint through the journal, narrow sources, split independent hypotheses, and resume from evidence. | Current concept, files in motion, candidate identity, risks, and next discriminating action. | Snapshot matches filesystem and tests before changes resume; context drift is treated as reliability failure. |
| Large repository or source graph | Source discovery is unbounded or a flat source list cannot identify canonical guidance and blast radius. | Narrow with repository graph or structured search, rank canonical/supporting/conflicting sources, and isolate the art core. | Claim-scoped provenance and project pattern compatibility. | Relevant dependencies and ownership are known before integration; broad source count is not mistaken for context quality. |

Choose the least costly response that restores coherent ownership and evidence:

- **Reduce scope** when optional platforms, variants, or controls create disproportionate uncertainty.
- **Constrain the environment** when fixed hardware, venue, format, or offline delivery is part of the artistic and operational specification.
- **Build a vertical slice** when the hardest risk is whether real subsystems compose end to end.
- **Extract a subsystem** when state, lifecycle, acceptance, and recovery are independently testable.
- **Run a disposable backend spike** when one measured feasibility question blocks system or renderer choice.
- **Hand off primary ownership** when another discipline's failure now has the highest consequence.

At every boundary, record owner; inputs and outputs; shared and private state; random and noise stream ownership; clock or temporal semantics; lifecycle; error and recovery behavior; target dimensions; interaction; accessibility; workload; degradation priority; evidence; and integrated acceptance owner. A single global seed does not guarantee determinism if subsystems consume randomness in order-dependent ways. A single clock does not guarantee temporal coherence if one subsystem drops or accumulates work differently.

**Good direct scale:** one dense WebGL piece remains one core because its hypothesis, state, controls, target installation, and recovery are singular, even though implementation requires specialized profiling. **Bad overgrowth:** five scenes, sensors, an authoring dashboard, mobile clients, and offline export share one run card and two agents mutate the same state. **Good split:** a multi-scene sensor installation gives each scene and hardware bridge explicit ownership, retains one concept and degradation hierarchy, and proves the complete venue path in rehearsal.

Modularity is not enough; verify interaction and failure isolation. Demonstrate that one subsystem can pause, degrade, reset, or fail without silently corrupting shared state or erasing the primary experience. Under resource pressure, the system must know which layer yields first and why. At scale, graceful degradation is governance as much as optimization.

When the split point is uncertain, use a vertical slice through the hardest real boundary. Avoid speculative frameworks that model every future platform before a representative render exists. Preserve the smallest coherent art core and add architecture only where separate correctness and evidence make it necessary.

## Future Refresh Search Queries

No search or browsing occurred in this evolution pass. Query strings are future research instructions, not evidence. Refresh only when a volatile external claim, observed platform failure, source conflict, deprecation risk, or depended-on release can change implementation or verification. Stable creative-method decisions should continue to use the inspected local corpus and direct rendered experiments.

The three inherited broad seeds remain available, but they should usually be narrowed before use:

| search_query_label_name | search_query_text_value | legitimate_future_use | limitation_and_narrowing_rule |
| --- | --- | --- | --- |
| `official_docs_query_phrase` | algorithmic art generation patterns official documentation best practices | Discover candidate official documentation surfaces when the responsible product or standard is still unknown. | Too broad to support a claim directly. Replace the theme phrase with the exact renderer, API, behavior, symptom, target platform, and version context. |
| `github_repository_query_phrase` | algorithmic art generation patterns GitHub repository examples | Find implementations that may reveal vocabulary, reproductions, or practical techniques after the contract is understood. | Repositories and examples vary in authority, maintenance, license, and compatibility. Treat them as examples or leads, not current contracts. |
| `release_notes_query_phrase` | algorithmic art generation patterns changelog release notes migration | Find change history when a library, renderer, browser, tool, or export path may have altered behavior. | Name the exact dependency and version boundary; a generic migration search invites unrelated results. |

Build targeted queries from `preferred authority + exact surface + observed symptom or required contract + platform/version`. Useful templates include:

| targeted_query_purpose | query_shape | expected_evidence_and_decision |
| --- | --- | --- |
| Current API contract | `[official owner] [renderer or API] [exact method or behavior] documentation [target platform/version]` | Primary documentation that confirms supported behavior, required syntax, lifecycle, or environment boundary. |
| Deprecation or migration | `[official owner] [dependency] [from version] [to version] migration deprecation release notes` | Primary release or migration material that changes implementation, compatibility, or retest scope. |
| Reproduced runtime symptom | `[official owner] [exact API/renderer] [error or symptom] [browser/device/version] known issue` | Primary issue, release note, or contract that distinguishes project defect from platform limitation and names a workaround boundary. |
| Rendering or resize contract | `[official owner] [canvas/WebGL/library surface] resize pixel ratio context loss lifecycle documentation` | Current platform guidance for the exact failing resize, density, or lifecycle claim; the local artifact must still be retested. |
| Export behavior | `[official owner] [export API/format] dimensions timing color assets documentation release notes` | Current contract or change record for delivered-file behavior and environment limitations. |
| Repository implementation example | `[exact library and version] [specific system family or technique] repository example` | A candidate example to inspect for structure or terminology, followed by primary-source and artifact verification. |
| Counterevidence | `[current belief or API] limitation deprecation incompatibility known issue` | Evidence that can falsify the preferred solution instead of only confirming it. |

Use this refresh protocol:

1. State the exact stale or uncertain claim and why it can change a current decision.
2. Reproduce the local symptom or establish the missing contract before broad research when feasible.
3. Choose the primary authority expected to own that claim; use community material as a lead or example, not a substitute for a public contract.
4. Run the narrow query and record direct source URLs rather than depending on result ranking.
5. Capture checked date, relevant version and heading, narrowly summarized support, counterevidence, source status, and unresolved scope.
6. Decide `change`, `confirm`, `no_material_impact`, `narrow_claim`, or `unresolved`.
7. Re-run the local artifact gate affected by the conclusion; external documentation cannot prove the local render.
8. Stop when the claim is resolved enough for the decision, or escalate the bounded uncertainty instead of widening search without limit.

**Good future query design:** a reproducible mobile resize defect yields the exact renderer, resize behavior, browser/device, and version terms, with official documentation or a primary issue as the preferred result; the corrected implementation is then captured on the failing viewport. **Bad design:** search "algorithmic art best practices," collect several tutorials, and override the local skill without a changed claim. **Borderline evidence:** a community workaround fixes one environment but lacks an official contract; retain it as a guarded local adaptation, document the tested boundary, and keep a refresh trigger.

Source code and issue trackers can explain implementation context but may expose unsupported internals, unresolved discussion, or behavior that is not a contract. Local repository history can explain project intent but not current external compatibility. Direct experiments establish local behavior strongly and general behavior weakly. Select the evidence route by claim, not prestige or quantity.

Use event-driven refresh for failures, source conflicts, API changes, migration, and platform boundaries. Schedule periodic refresh only for volatile surfaces the artifact actively depends on and whose changes may arrive without a local failure signal. A future refresh should always report what changed; `no_material_impact` is useful evidence that prevents repeated research churn.

## Evidence Boundary Notes

Attach confidence to individual claims, not to the reference as a whole. Use visible labels for material, disputed, numerical, external, compatibility, production, reliability, or universal-sounding claims. For dense evidence, keep one canonical claim record and summarize or link it elsewhere rather than duplicating prose.

- `user_requirement_fact`: a goal, artifact surface, constraint, target environment, reviewer role, or acceptance condition explicitly provided by the user or governing specification. If the agent inferred it, it belongs under inference until confirmed.
- `local_corpus_sourced_fact`: a statement tied directly to an inspected local source path and bounded by what that source actually says. Path presence is not enough; record the relevant rule and scope.
- `external_mapping_unrefreshed_note`: the seed records a public URL and intended role, but this pass did not browse or verify current contents. The mapping may guide future research but cannot support a present-tense external claim.
- `external_research_sourced_fact`: a statement tied to a public primary source that a future permitted pass actually opened, scoped, dated, and summarized accurately. Source authority transfers only to the domain documented.
- `measured_artifact_behavior`: an observation from an identified revision, seed policy, parameters, viewport, temporal state, workload, environment, method, and result. It supports that tested scope, not every browser, device, seed, or artwork.
- `reviewer_judgment_note`: a designated reviewer's acceptance, rejection, preference, or uncertainty against named criteria and observed output. It is accountable artistic judgment, not objective beauty or population-wide taste.
- `combined_evidence_inference_note`: a recommendation synthesized from source facts, artifact observations, requirements, and systems or creative judgment. State assumptions, boundaries, alternatives, and what evidence would change the decision.

A material claim record should answer:

| claim_record_field | completion_rule |
| --- | --- |
| `claim` | Make one proposition with one evidence scope; split mixed fact, inference, measurement, and taste when their confidence differs. |
| `class` | Choose the evidence category above; a label describes provenance but does not make weak reasoning sound. |
| `source_or_method` | Name the inspected path, refreshed direct URL, user requirement, run identity and protocol, or designated review event. |
| `scope` | State versions, environment, artifact mode, seed/state population, viewport, workload, and audience boundaries that matter. |
| `decision_impact` | Explain what implementation, routing, verification, acceptance, or refresh action follows. |
| `counterevidence_or_limit` | Record conflicting source, failed state, alternative explanation, untested surface, or reviewer disagreement. |
| `confidence_and_owner` | State what is known, inferred, judged, or unresolved and who can accept or reopen it. |
| `change_trigger` | Name the source update, artifact failure, requirement change, measurement, or review result that would revise the claim. |

**Good claim chain:**

1. `local_corpus_sourced_fact`: the inspected canonical skill recommends repeatable seeded behavior when the medium allows it.
2. `user_requirement_fact`: the selected edition must be reproducible for export and handoff.
3. `combined_evidence_inference_note`: record random and noise seeds plus initialization order before candidate comparison because replay is required here.
4. `measured_artifact_behavior`: two runs of the identified candidate reach the promised visual state in the named environment.
5. `reviewer_judgment_note`: the designated reviewer accepts that state against the frozen rubric, while cross-browser pixel identity remains untested.

**Bad chain:** "External best practices prove seeded art is always better." It launders an unrefreshed mapping, converts a local default into a universal aesthetic claim, omits the user's mode, and offers no artifact evidence. Correct it by removing the claim, bounding it to the local default, or adding a permitted refreshed source and task-specific test.

**Borderline claim:** "Particles are the right family for memory." The pattern menu supports particles for birth, death, and clustering, but does not establish a universal metaphor. Make it usable as `combined_evidence_inference_note`: this interpretation treats memory as discrete entities that lose cohesion and sparsely return; a monochrome particle prototype is compared with one plausible oscillator alternative; the reviewer decides from rendered evidence. If neither communicates loss, the inference is falsified for this brief.

Avoid these boundary errors:

- Labelling a whole paragraph `local_corpus_sourced_fact` when its final recommendation is an unstated inference.
- Treating a mapped URL, successful HTTP response, repository example, or search query as a refreshed authoritative fact.
- Reporting a performance target as an observed result or one local run as a population guarantee.
- Pairing runtime evidence from one candidate with a visual capture from another.
- Presenting reviewer agreement as universal taste or disagreement as measurement noise to be averaged away.
- Retaining a correct label while wording the claim more broadly than the source or experiment supports.
- Omitting negative evidence, no-impact refreshes, rejected hypotheses, or known untested environments when they change reuse risk.

Run a skeptical audit by extracting material claims and asking: Was the source actually read? Does it support this exact scope? Is the external record fresh or merely inherited? Does measured evidence identify the candidate and environment? Is the statement a target or a result? Who owns the artistic judgment? What would falsify or refresh the conclusion? Correct failures through `remove`, `bound`, `source`, `measure`, or `relabel`; do not preserve authority theater for smoother prose.

**Confidence summary for this evolved reference:** the three frozen local algorithmic-art files were read completely, so their workflow, philosophy template, pattern families, examples, and guardrails are represented as local facts. The three public URLs are inherited, unrefreshed mapping facts only. No artwork described in the operational examples was rendered by this reference-evolution task, so those scenarios remain explicit illustrations. Detailed guidance on manifests, workload, reliability, observability, failure recovery, and scale is systems-informed synthesis that must be adapted and verified in the implementation context. Final concept selection and aesthetic acceptance remain user or designated-reviewer judgment.

Evidence boundaries exist to make decisions reversible and confidence transferable. Their long-term value is not that the reference can never be wrong; it is that a wrong, stale, or overbroad claim can be located, bounded, corrected, and retested without discarding unrelated guidance.
