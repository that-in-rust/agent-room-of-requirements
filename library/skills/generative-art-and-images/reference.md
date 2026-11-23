# Generative Art and Images: Reference

Depth for [SKILL.md](SKILL.md). The rules and templates needed to do the job are in SKILL.md. This file holds the full catalogues, failure tables, operations guidance, and evidence limits. Sub-topics are marked A (algorithmic art), B (image generation prompts), C (local vision reading).

## Idiomatic Thesis Synthesis Statement

### A. Algorithmic art

Algorithmic art is a behavior-design problem. The visual system must make the concept perceptible before palette, texture, glow, interface, or polish. A good piece has one dominant carrier, compact controls a person can interpret, bounded state, an explicit lifecycle, a replay policy, and evidence tied to the exact candidate that was judged. Reproducibility enables collaboration and comparison. It does not establish artistic merit.

Proof is dual. Software evidence covers execution, replay, resize, and the declared workload. Visual evidence covers visible intended behavior, framing, and named acceptance criteria. Neither substitutes for the other.

### B. Image generation prompts

A reliable prompt is a labeled spec plus specificity discipline: normalize specific requests, augment generic ones lightly, never invent what was not implied. Execution path is permission-gated: the built-in tool by default, the CLI only on explicit request. Whether a better spec reduces the number of iterations is not measured.

### C. Local vision reading

Inputs prepared, resources bounded, configuration verified. Reliability is lost at the raw-input boundary: resize, discover names with code, stage ASCII copies, limit concurrency. Configuration precedence is the one cause that is not an input problem. This thesis applies to a local Ollama model on one host. Do not extend it to cloud APIs or untested runtimes.

## Pattern Scoreboard Ranking Table

No ranking here is measured. Orders are working priorities.

### A. Algorithmic art

Select a system family by five criteria, in this order of weight: concept-system correspondence, simplicity, control leverage, runtime envelope, delivery surface. Any score you assign is a reversible, task-specific judgment. Prefer the family whose defining behavior directly carries the premise. Keep a secondary mechanism only when it has a distinct, demonstrated role. Simplify or switch when the explanation carries more meaning than the pixels.

### B. Image generation prompts

| Priority | Practice | Prevents |
| --- | --- | --- |
| 1 | Use the labeled spec | Free-text prompts and omitted constraints |
| 2 | Repeat edit invariants on every iteration | Cumulative drift from the original image |
| 3 | Make one targeted change per iteration | Losing track of which change caused what |

### C. Local vision reading

| Order | Preparation | Prevents | Status |
| --- | --- | --- | --- |
| 1 | Always resize first | Timeouts from oversized inputs | Emphasized default, not empirically ranked |
| 2 | Discover names with Python | Unicode and path errors | Same |
| 3 | Stage ASCII copies under `/tmp` | Raw-path and path confusion | Same |
| 4 | Bound concurrency at 2 to 3, default 2 | GPU contention and out-of-memory | Same |

How often each rule is broken is not measured. A wrapper that performs all four would make the order irrelevant.

## Agent Usage Decision Guide

### A. Algorithmic art

| Mode | Choose when | Ownership |
| --- | --- | --- |
| Primary | Code-generated composition, motion, geometry, emergence, or interaction is the artifact and aesthetics matter | Follow the whole loop: concept, family, controls, prototype, render evidence |
| Companion | The art is a bounded part of a site, tool, game, installation, or branded experience | Art core owns concept, seed, and render contract. Parent owns shell, content, ergonomics, deployment, game rules |
| Avoid as primary | Data encoding, photo editing, image generation, icon or logo work, document layout, or conventional UI defines correctness | Route to the relevant workflow. Do not bend facts or usability to make art |
| Escalate or combine | 3D, shaders, audio, hardware, offline production, or independent systems exceed a simple 2D sketch | Add domain ownership at explicit subsystem boundaries |

Failure routing by class: concept -> revise the premise or its translation; system -> compare or switch family; control -> remove, merge, or bound; runtime -> reduce and bound work, or justify a renderer change; presentation -> fix framing, resize, contrast; evidence -> restore observability first.

### B. Image generation prompts

Open this guidance before any raster generate, edit, or batch request. Classify three things: use-case slug, intent (generate or edit), and execution strategy (one, variants, many). Reference-only images mean generation with references. An ambiguous request defaults to generation. Label input roles before choosing generate or edit. Do not trigger for extending an SVG system or other code-native work.

### C. Local vision reading

Open before any local file-based Ollama vision analysis. Batch jobs go to the six-step workflow. Failures go to the symptom table. Slow or wrong results go to the effective configuration. Not for cloud API analysis, image generation, or Ollama administration. A screenshot folder is presumed in scope.

## Decision Tradeoff Guide

### A. Algorithmic art

- Directness over novelty: one strong carrier generally beats many weakly related systems.
- Compact controls over configurability: a control needs safe bounds, a baseline, and an interpretable visible effect.
- Simple renderer over escalation, unless a need in dimensionality, density, interaction, or export is measured and unmet.
- Graceful degradation over preserving density: reduce work while keeping the behavior that carries the concept. Hitting a timing target by erasing the piece's identity is a failure.
- Bounded uncertainty over false certainty: state the unresolved question, the cheapest test that would discriminate, the owner, and the condition that reverses the decision.

### B. Image generation prompts

Match effort to three variables: how specific the user was, the intent, and the destination. A project asset needs the full spec, inspection, the correct save path, and acceptance. A quick preview may use a two-line spec and a lighter gate. For an edit, invariant preservation outranks augmentation. When the wanted output is unclear, ask or escalate instead of retrying.

Stakes set the iteration budget: a brand hero image deserves more calls than a placeholder.

### C. Local vision reading

| Choice | Condition | Action and cost |
| --- | --- | --- |
| Adopt | Local practice and current external documentation agree | Use the four rules as written; still watch for stale assumptions |
| Adapt | Local practice is strong but public guidance changed | Keep what fits the host; mark the inference |
| Avoid | Evidence is thin or conflicting, or the task is cloud analysis or generation | Research further or route elsewhere |
| Cost of a wrong choice | A timeout, or a "missing file" error that is really a Unicode name | The reviewer must know what to undo and what to inspect next |

A few seconds of preparation avoids a timeout window or a misleading path error. On different hardware, either prepare fully or measure first.

## Theme Specific Artifact

### A. Algorithmic art: families, translations, lifecycle

Family cues and knobs (same seven families as SKILL.md A.3), with implementation notes:

| Family | Typical state | Bound to set | Monochrome test |
| --- | --- | --- | --- |
| Flow fields | particles plus a noise or vector field | particle count, trail accumulation | do the streamlines read without color |
| Particle systems | entities with age, velocity, emitter | spawn rate, lifetime, pool size | are birth, clustering, and death legible |
| Oscillator systems | phases, frequencies, coupling terms | oscillator count, sample resolution | is the interference pattern visible |
| Cellular or rule systems | grid and rule table | grid size, update cadence | does structure emerge from the rule alone |
| Packing and growth | shapes with radii, spatial index | attempts per frame, shape count | is pressure or crowding visible |
| Recursive geometry | recursion depth, branch parameters | depth, total segment count | does self-similarity read at one stroke weight |
| Noise terrain or ink | scalar field, thresholds | octaves, resolution | do contours hold without shading |

The "typical state", "bound" and "monochrome test" columns are working suggestions, not sourced rules. Verify in the render.

Philosophy-to-code translations (extend per piece, then check each in a render): gentle drift -> low-frequency noise field; memory decay -> alpha fade plus sparse respawn; tension release -> spring easing after a threshold; hidden rhythm -> phased oscillators or periodic emitters.

Run-card lifecycle: `draft` (provisional, broad exploration) -> `candidate` (identity and rubric frozen enough to attribute changes) -> `accepted` (software and visual gates pass and a restore from the card works) or `archived_study` (rejected or deferred, kept for what it taught, not export-ready).

Candidate identity: code revision, phase, seed or seeds, initialization order, parameters, viewport, temporal state, environment, captures. Keep random and noise seeds as separate values and record the order of initialization. Reproduction may be bounded instead of byte-identical because browser, GPU, font, floating-point, and timing differ.

Evidence packet for one accepted candidate: `code revision + run command + seed + parameters + viewport + temporal state + fresh capture + console result + runtime observation + rubric verdict`.

Claim-to-evidence matrix:

| Claim | Minimum evidence | Pass condition | Limit |
| --- | --- | --- | --- |
| It runs | Real build or launch, environment, state, console summary | A representative state launches with no unhandled error | It may still be blank or wrong |
| Seed policy | Two runs with recorded random and noise seeds and init order | Promised determinism holds in the declared environment | Other platforms may need bounded visual equivalence |
| Controls | Sweeps at minimum, representative, maximum, and invalid input | Every control has a safe, perceptible, interpretable effect | Exploratory controls can stay internal |
| Viewport and framing | Fresh captures at every target size and export dimension | Visible, correctly framed, no incoherent clipping | A fixed installation may narrow the list |
| Temporal behavior | Start, mid-state, stress or long run, interaction transitions | Lifecycle, motion, decay, trails stay intentional | One screenshot is not enough |
| Runtime | Target-class device, workload, warmup, sample window, frame intervals, memory trend, stress behavior | The project's envelope holds, or bounded degradation keeps the dominant behavior | No universal frame-rate threshold exists |
| Visual acceptance | Versioned criteria, monochrome and ablation probes, reviewer's reasons | The named reviewer accepts concept-system correspondence | Judgment, not automated truth |
| Export | Regenerate from revision, seeds, controls, viewport, temporal state, environment, settings | An independent run reaches the delivered state | Assets and platforms may limit identity |

Verdict classes: `pass`, `scoped_failure`, `external_shared_state_failure`.

### B. Image generation prompts: per-slug guidance

Generate:

| Slug | What to specify | What to avoid |
| --- | --- | --- |
| `photorealistic-natural` | A moment as a camera would catch it: viewpoint, lens feel, light, real surface texture | Glossy over-styling unless asked |
| `product-mockup` | The product, its materials, a clean outline, readable label; exact label text with typography | Props and scenes that were not requested |
| `ui-mockup` | Fidelity first (shippable mockup or rough wireframe), then layout, hierarchy, real interface elements | Concept-art language |
| `infographic-diagram` | Audience, reading flow, every label quoted verbatim | Unlabeled parts, decorative clutter |
| `logo-brand` | Simple, scalable, strong outline, balanced empty space | Flourishes, gradients, mockup scenes unless asked |
| `illustration-story` | Panels or beats, one concrete action each | Vague action, unrequested text |
| `stylized-concept` | Style cues, material finish, rendering approach | New story elements |
| `historical-scene` | Place, date, and how period-accurate clothing, props, and setting must be | Modern objects |

Edit:

| Slug | Change only | Keep |
| --- | --- | --- |
| `text-localization` | The words | Layout, typography, spacing, hierarchy, imagery |
| `identity-preserve` | The named garment or setting | Face, body, pose, hair, expression; light and shadow must match |
| `precise-object-edit` | The one named element | Surrounding texture, light, everything else |
| `lighting-weather` | Light, shadow, atmosphere, precipitation | Geometry, framing, subject identity |
| `background-extraction` | The background, to transparent or clean | A crisp outline with no halo; label text exactly; no restyling |
| `style-transfer` | Subject or scene as stated | The reference's palette, texture, and stroke; add "no extra elements" |
| `compositing` | What moves where, by image index | Base framing; matched light, perspective, scale |
| `sketch-to-render` | Materials and light | Layout, proportion, perspective; nothing new added |

Asset-type starting points (fill the labeled spec from SKILL.md B.5):

- Website: hero, section illustration, blog header. Usually no text and no logos. Ask for open space only when copy will sit on the image.
- Game: environment concept, character concept, UI icon, tileable texture. Icons: centered, clear outline, generous padding, no scene behind. Textures: seamless edges, no focal object.
- Wireframe: `ui-mockup` at low fidelity, greyscale, sections listed in order, labels on major blocks, no real photos.
- Logo: centered mark, one or two high-contrast colors, exact name quoted only if a wordmark is wanted, no 3D or mockup scene.

API-level facts for the CLI path (Codex imagegen CLI, March 2026 snapshot; verify before use): models in the `gpt-image-*` family (`gpt-image-1.5`, `gpt-image-1`, `gpt-image-1-mini`); `n` from 1 to 10; `background` is `transparent`, `opaque`, or `auto`; formats `png`, `jpeg`, `webp`, with compression 0 to 100 for the last two; `moderation` is `auto` or `low`; up to 16 input images, each under 50 MB; `input_fidelity` defaults to low. On `gpt-image-1.5` the first five inputs keep higher fidelity; on the older models the first image is favored. The script caps a batch at 500 jobs, retries a failed job up to `--max-attempts` (default 3), and supports `--fail-fast`, `--prompt-file`, `--no-augment`, `--downscale-max-dim` (writes a second copy with a `-web` suffix), and per-job JSONL overrides (`size`, `quality`, `background`, `output_format`, `output_compression`, `moderation`, `n`, `model`, `out`, and the prompt fields). With `--out-dir`, single runs are named `image_1.<ext>`, `image_2.<ext>`. If an option is rejected by the chosen model, retry by hand without it. Dependencies: the `openai` package; Pillow only for downscaling.

The operational artifact for this mode is one completed labeled spec per asset: slug, request, role-labeled inputs, verbatim text line, constraints, the accepted render's path, and a clear split between user requirements and agent additions. For a campaign, add a prompt contract: the template, one bad prompt rewritten into it, and the evaluation criteria.

### C. Local vision reading: setup and manifest

Why a small local model fits this job on the documented host: it leaves memory headroom on 24 GB, runs fully on the GPU (about 35 tokens per second for text was reported, not re-measured), accepts any aspect ratio through a dynamic-resolution vision encoder, does usable OCR and scene description, and was stable on that machine.

Authority: the live `~/.hermes/config.yaml` and `~/.hermes/.env` decide actual routing. Written guidance describes the intended configuration but cannot tell you what is in effect. `.env` wins.

Staging manifest, one row per image: original directory, `repr()`-escaped original name, staged path, post-resize width and height, seconds per call, pointer to the answer. Print names at copy time. Rebuilding the manifest afterwards loses the evidence of which Unicode characters were in the name. For one small image, a one-line note or a wrapper's log is enough.

Dimension checks do not prove the staged copy is the right file. Use checksums or a wrapper when that matters.

## Worked Example Set

All examples are illustrations. None is a measured render or run unless it says so.

### A. Algorithmic art

- Good: one bounded particle lifecycle; fixed seed; readable responsibilities; capped density and expiring particles; a monochrome baseline; one-variable comparisons; captures at start, mid, and long run on mobile and desktop; thinning under stress; a selected candidate, an informative rejected oscillator version, and an export manifest.
- Bad: a brief of "organic and futuristic"; fresh randomness every run; twelve unclear sliders; layers added because they look generative; render mutates state; resize resets; particles never expire; uncapped spawn; shell before art; one desktop first frame as proof; no restore, stress test, or criteria. Recovery: freeze the seed, remove the shell, remove layers, reduce density, separate update from render, inspect in monochrome. If the lifecycle still fails to carry the concept, switch family.
- Borderline: a field texture that may represent pressure or may only duplicate particle velocity. Compare the full field, a simplified directional force, and no field, at the same times with fixed seed, density, and palette. Keep both mechanisms only if removing one loses a named criterion and runtime stays bounded. Otherwise simplify or switch.
- Measured on the SKILL.md plain-canvas starter (one headless Chrome on Linux, 1280x720, 600 steps): same seed twice gave 0 differing pixels; a different seed gave about 160,000. A first version cleared the canvas on resize and produced a blank headless capture while the script reported success; replaying the still on resize fixed it.

### B. Image generation prompts

- Good: spec written first, constraints preserved, output inspected, accepted, and placed in the workspace with path, prompt, and mode reported.
- Bad: an edit chain that drops "keep the product unchanged" at iteration three, or a detailed prompt padded with polish the user never implied. Invariant loss accumulates across iterations.
- Borderline: soft studio lighting added to a generic product request, listed as an addition; or a preview left at the tool's default path, labeled as a preview and accepted as such.
- Batch, good: eight game icons through one JSONL manifest. Bad: twelve full rewrites for one hero image. Borderline: three `n` variants for a shortlist, labeled exploration.

Grade these on conduct (additions versus specificity, invariant repetition), not on how the picture looks.

### C. Local vision reading

- Good: discover, sort, stage, resize, smoke-test, then analyze; keep the manifest and the observed outputs.
- Bad: pass a 10 MB Retina capture or the original folder path, then retry unchanged after the timeout.
- Borderline: after 600 px was tried, raise the timeout to 240 s for a legitimately dense diagram; or skip staging for one verified-small ASCII-named file with the risk recorded.

Judge by preparation order and whether each retry changed the failing condition, not by how good the description reads. Exact error text and timings should be visible in the record.

## User Journey Scenario

### A. Algorithmic art

Brief: "Make memory feel as if it is losing cohesion in a slow current." Wanted: animated, seed-driven, responsive, exportable as a still.

1. Seed sentence: discrete memories drift in an invisible current, briefly cluster, fade, and sparsely return.
2. System: particle lifecycle is primary, because birth, loss of cohesion, death, and reappearance carry the premise. A low-frequency flow is the internal force model. Oscillators are the plausible alternative, but they express rhythm more directly than discrete loss and return.
3. Controls: `seed`, `density`, `flow_scale`, `drag`, `lifetime`, `trail_decay`, `palette`, each with a safe range and a perceptual effect.
4. Criteria: coherent slow drift, clustering that is not a grid, legible decay, intentional empty space, structural interest in monochrome, framing on desktop and mobile.
5. Work order: monochrome minimal prototype -> bounded exploration, labeled as such -> freeze code, seed, viewport, and rubric and vary one factor -> add palette after structure holds -> sweep controls, resize, stress density, long-run cleanup, reset and export -> reviewer acceptance and an independent restore. Example identity: `seed=1842`, inspected at start, at a 12-second candidate state, and at a 90-second stability state.
6. If only one seed works, label it a curated edition and do not claim robustness. If runtime fails but the concept survives, reduce density and bound work first. Change renderer only with a measured reason.

### B. Image generation prompts

Generate journey: vague "we need a landing page hero" -> choose slug -> write the labeled spec (use case, request, role-tagged inputs, verbatim text, constraints) -> generate -> inspect subject, style, composition, text, constraints -> one targeted change -> accept -> move into the workspace -> report final path, final prompt, and mode.

Edit journey (separate, because invariants are locked): load the target so the tool can see it -> label it as edit target -> write "change only" and "keep unchanged" -> generate -> compare with the original -> one targeted change with invariants restated -> save as a versioned sibling, never over the original -> report.

Typical iteration counts are not recorded.

### C. Local vision reading

Screenshot batch: discover with `os.listdir`, keep `repr` names, sort by modification time, take the three oldest, copy to ASCII `/tmp` names, resize with `sips`, run a timed smoke test, then analyze in a bounded parallel batch. The decisive step is discovery: it stops the invisible U+202F from travelling further.

## Anti Pattern Registry Table

### A. Algorithmic art

| Anti-pattern | Symptom | Correction | Exception |
| --- | --- | --- | --- |
| Layer pile-up | Particles, waves, branches, glow, blur, and UI compete; no mechanism carries the concept | Remove down to one dominant system; keep a layer only for a named, accepted role | Maximalism is valid when every mechanism has a distinct, evidenced role |
| Random novelty loop | Seed, code, controls, palette, viewport, and rubric all change together | Freeze identity; vary one material factor while converging; keep only informative variants | Broad exploration may vary several dimensions if labeled exploration and each kept run teaches something |
| Coupled update, render, input | Render mutates state; resize resets unpredictably; replay depends on order | Separate initialization, update, render, input, reset, and resize policies | A tiny throwaway study may be lighter but must still run and be inspectable |
| Uninspected output | Build or text passes while the canvas is blank, clipped, obscured, or in the wrong state | Inspect pixels, dimensions, console, layout, temporal state, interaction, target viewports | None. Only the form of evidence may vary |
| Single-frame motion proof | One screenshot claims animation, decay, emergence, or stability | Check start, representative mid-state, stress or long run, interaction transitions | A static deliverable needs its declared final state plus resize and export evidence |
| Unbounded density or state | Spawn, trails, off-screen entities, or updates grow until motion changes or memory rises | Cap work; expire, cull, pool; reduce density before adding complexity | Offline high-density export may trade latency for explicitly bounded time and memory |
| Resize corruption | Crop, stretch, blank regions, or a silent seed reset at target dimensions | Normalized coordinates or deliberate recomposition; test every declared size | A fixed-format installation may reject responsive resizing explicitly |
| Generic front-end takeover | The shell is polished before representative art exists | Prototype the art full-bleed or minimally framed; integrate through a narrow contract | A true authoring tool needs a shell, owned by the product workflow |

### B. Image generation prompts

| Failure | Safer replacement | How to detect |
| --- | --- | --- |
| Silent CLI fallback | Offer the fallback and get explicit acceptance | The transcript shows the user's request before any CLI call |
| Unimplied creative augmentation | Normalize detailed prompts; augment only generic ones, lightly | Compare additions with what the user said |
| Dropped edit invariants | Restate keep-unchanged constraints every iteration | Compare each prompt with the original spec |
| Asset stranded in the tool's default folder (`$CODEX_HOME` in Codex) | Move project assets into the workspace and report that path | Search the delivery report for the default path |
| Recommendation with no stated basis | Say whether a claim comes from local practice, checked documentation, or inference | Look for the label on each load-bearing claim |
| Instruction that cannot be checked | Tie advice to a command, checklist, or review question | Ask "what would show this was done" |

These failures are mostly omissions, so a single prompt will not reveal them. Screen every generation and edit before delivery. Relative frequency is not measured.

### C. Local vision reading

| Anti-pattern | Symptom | Safer action |
| --- | --- | --- |
| Raw-path analysis | The call names the original folder, not `/tmp` | Inspect the transcript; stage clean copies |
| Typed file names | U+202F looks like a space; the error reads like a missing file | Discover with `os.listdir`; keep `repr(name)` |
| Oversized input | Timeout, often at about 120 s | Resize to 800 px, then 600 px, before any retry |
| Unbounded concurrency | GPU contention, out-of-memory, extreme slowdown | Serialize, or cap at 2 to 3 |
| Extension mismatch | The input cannot be opened or is misrouted | Check the extension and the staged file's real type |
| Unchecked `.env` routing | Slow or poor but plausible output from the wrong model, no error | Inspect the effective `.env` before retrying |

## Verification Gate Command Set

Runnable commands for all three modes are in SKILL.md (A.9 and "Quality gates"). Additions:

### A. Algorithmic art

- Use the implementation repository's real build, launch, and capture commands. Do not invent commands for a project.
- Cheap exploration gate: syntax and launch, one fixed-seed state, direct visual inspection.
- Milestone and final gate: the full claim-to-evidence matrix plus one perturbation (density, resize, reset, or ablation).
- Diagnosis order: restore observability with a reproducible seed and a real render; classify the first material failure as concept, system, control, runtime, presentation, or evidence; change the smallest upstream cause.
- Reusable or shipped work adds control sweeps, temporal states, target-device observations, cleanup checks, manifests, and reviewer evidence, but only where they support reproduction, diagnosis, selection, or acceptance.

Control sweep on the starter (each capture must differ visibly from the baseline and stay in frame):

```bash
for d in 50 900 4000; do shot "density-$d.png" 1280,720 "seed=1842&steps=600&density=$d"; done
shot invalid.png 1280,720 "seed=1842&steps=600&density=abc&drag=9"   # invalid input must clamp, not crash
```

### B. Image generation prompts

- CLI path: `--dry-run` before every live call. It previews payload and output paths with no key, network, or cost.
- Human gate: subject, style, composition, verbatim text, constraints, and for edits the invariants, all against the spec. A green mechanical check cannot replace looking. Rendered labels must be read.
- Lighter checklist for preview-only work; paired review for brand-sensitive work; automated text extraction for label-critical work. No standard format for visual-inspection records exists yet.
- Per review cycle, run at least one verbatim-text audit and one original-versus-final edit comparison.

### C. Local vision reading

- Before every batch: staged paths under `/tmp` and ASCII-named; longest edge at most 800 px after resizing; one timed smoke analysis (target under 30 s on the documented host; 15 s is a good result there).
- Seed a test folder with an oversized file and a misnamed file to prove the gates catch them.
- A resized image that is still slow is a routing check: inspect `.env` before batching.

```bash
# Dimension gate without the manifest
identify -format "%f %w %h\n" /tmp/vision_stage/vision_* | awk '$2>800||$3>800{print "TOO BIG:",$0; bad=1} END{exit bad}'
# macOS equivalent for one file
sips -g pixelWidth -g pixelHeight /tmp/vision_stage/vision_000.png
```

## Failure Mode Table

Handle every failure in the same order: detect, contain, diagnose, correct, verify, record. Keep the identity of the failing state.

### A. Algorithmic art

| Failure | Response |
| --- | --- |
| Blank, clipped, or wrong state | Capture console, dimensions, and time; inspect initialization, assets, transforms, resize; recapture the target state |
| Random variants with no learning | Freeze a baseline, one criterion, one variable |
| Concept not visible | Stop polishing; simplify, remove layers, compare, or switch family; archive the falsified idea |
| Cannot reproduce | Record revision, seeds, init order, controls, viewport, time, assets, environment; separate update from render; move to an ephemeral profile only on purpose |
| Dead, redundant, or unsafe control | Hide or disable it; sweep, clamp, validate, or merge; verify minimum, typical, maximum, and invalid input |
| Resize corruption | Restore a valid viewport; fix normalized framing, buffer size, pixel ratio, reset policy; test every declared size |
| Temporal saturation or drift | Cap duration; bound accumulation; fix lifecycle, integration, decay; test start, mid, long run |
| Runtime collapse or hidden accumulation | Reduce density and layers; cull, expire, pool, tear down, remove listeners; verify timing together with identity and long-run and reset behavior |
| Export differs from preview | Keep both identities; record settings and temporal state; inspect the delivered file itself; regenerate from the manifest |
| Ownership collision | Freeze overlapping edits; one owner per mutable subsystem and one for integrated acceptance; define contracts; do not merge competing state models |
| Guidance has gone stale | Mark the claim unverified; re-read or refresh the primary source; record scope and conflict |
| Generic advice | Replace it with scoped evidence or remove it |

When evidence is weak, consider at least two causes. A slowdown may be density, hidden state, pixel ratio, or a host page re-rendering. Run the cheapest test that separates them. Example of a confirmed diagnosis: clipping on mobile while desktop is correct -> fix normalized framing without touching the simulation, then rerun all sizes.

### B. Image generation prompts

| Failure | Earliest signal and containment |
| --- | --- |
| Edit invariant drift | Original-versus-final comparison; restate invariants before delivery |
| In-image text mismatch | Read every rendered label against the quoted text; correct before shipping |
| Stranded asset | The tool's default folder appears in the delivery report; move the file and report the workspace path |
| Mode or parameter confusion | Confirm each control belongs to the selected path before the call |
| Stale model facts | Refresh public documentation, rerun the local gate, mark stale claims |
| Lost context in a long run | Checkpoint; reread the plan and the current spec before destructive steps |
| Unbounded fan-out | Cap parallelism, assign ownership, require a merge or audit checkpoint |

Frequency is not measured. The order reflects how silent and costly each failure is expected to be.

### C. Local vision reading

| Failure | Trigger and signal | Containment and correction |
| --- | --- | --- |
| Oversized input timeout | Full-resolution or large image; timeout near 120 s | 800 px, then 600 px; only then consider a longer timeout |
| Unicode path error | Typed macOS name, often with U+202F | Rediscover with Python; clean ASCII copy under `/tmp` |
| GPU out-of-memory or contention | Too many calls at once, especially a third | Serialize or reduce concurrency |
| Configuration drift | Slow or poor but plausible output, no explicit error | Inspect the effective `.env` and model routing first |

Configuration drift is the quietest failure. It deserves the most deliberate detection.

## Workload Model

### A. Algorithmic art

The unit of work is one falsifiable visual hypothesis: one concept-to-system correspondence that can be prototyped, looked at, and then accepted, rejected, or archived with what it taught.

A planning default, not a limit: one artifact family, one fixed baseline plus about three representative variants, one accessibility and readability pass, one render verification path. Extend only the dimension that closes a named uncertainty. Split when ownership, lifecycle, evidence, or failure recovery becomes independent.

| Dimension | Default | Extend or split when | What to check |
| --- | --- | --- | --- |
| Primary surface | One code-native visual artifact, or one independently testable art subsystem | The main failure becomes data truth, product interaction, image editing, 3D behavior, or game rules | Confirm primary / companion / avoid routing before building broadly |
| Concepts | One active concept sentence and one chosen reading of it while converging | Several concepts need unrelated mechanisms or separate reviewer decisions | Each kept concept has its own system mapping and stop condition; do not merge slogans into one vague brief |
| System families | One dominant family; a second mechanism only for a distinct role | Two systems have independent state, controls, lifecycle, owner, or acceptance | Ablation and role evidence; split truly independent systems but keep one integrated render gate |
| Exploration | A small coarse comparison of plausible families or parameter regions; keep few outcomes | A render reveals a different hypothesis the current samples cannot separate | Label it exploration, state the question, stop when review capacity or concept clarity is used up |
| Candidates | Baseline plus about three variants | Another candidate tests a newly named uncertainty, not just more variety | Same seed, viewport, time, and criteria version; each candidate gets keep, reject, or next test |
| Seeds | One baseline seed for causal iteration, then a small declared robustness set or a curated-edition boundary | Composition or lifecycle varies a lot across seeds, or generative range is promised | Explain why those seeds; never claim robustness from one good state |
| States and viewports | Declared target sizes plus start, representative, and long-run or interaction states | Extra delivery surfaces bring different framing, timing, input, or accessibility risk | Add coverage by risk; do not run every exploratory variant on every surface |
| Accessibility and readability | One dedicated pass once representative behavior exists | Motion sensitivity, contrast, input alternatives, or shell integration create separate requirements | Reduced-motion or pause behavior where it applies, visible structure, nothing overlapping on target surfaces |
| Runtime environments | One representative target-class environment plus a stress case | GPU, browser, mobile, installation, or export environments differ and are all promised | Record environment and workload; split platform diagnosis, keep shared concept evidence |
| Render verification path | One executable path that reaches and captures the intended state | Live preview, offline export, installation output, or a second renderer is delivered separately | Inspect every delivered path. A passing preview does not validate a different export |
| Source reading | The working rules plus only the philosophy or pattern material the open decision needs | A current platform fact, a conflict, or a recurring exception needs a targeted refresh | Each extra source changes, confirms, or is declined for a named claim |
| Records | One run card: baseline, selected candidate, one informative rejection, final evidence, reopening triggers | Independent scenes or systems cannot share identity or acceptance | Split records at independent hypotheses; do not archive raw transcripts or low-value variants |
| Ownership | One owner for the art core, one for integrated acceptance; companions bounded by contracts | Two agents would edit the same visual state or make the same acceptance decision | Disjoint write surfaces, explicit interfaces, integrated evidence |

Budgets by phase. Exploration may vary several factors coarsely but must name the question and keep little. Convergence freezes the baseline and varies one material factor. Acceptance runs the promised seed, state, viewport, environment, accessibility, runtime, restore, and export matrix on the selected candidate only. That keeps target coverage from multiplying across every early study.

Ways to shape the work:

- Vertical slice: when the biggest unknown is whether concept, system, renderer, and capture work end to end.
- System split: when mechanisms have independent lifecycle, controls, or recovery.
- Scene split: for multi-scene works whose outputs and acceptance can proceed separately.
- Backend spike: answers one measured feasibility question and stays disposable. It does not become architecture because it exists.
- Platform split: isolates device-specific runtime diagnosis and keeps shared seed and concept evidence.

Keep a short workload ledger: active hypothesis, source set, family count, baseline and candidate count, seed policy, target states and viewports, environments, evidence paths, owner, unresolved risk, next action, review capacity. Counts reveal drift; they do not measure creative difficulty.

- Good bounded work: one responsive particle study, one canvas path, one baseline, three candidates, desktop and mobile acceptance, a restorable still.
- Bad unbounded work: all seven families, exhaustive parameter combinations, unlimited seeds, every device, a settings product, no active hypothesis.
- Borderline extension: a fourth candidate, justified because earlier renders showed trail decay and lifetime produce two different kinds of forgetting. Everything else is frozen and the deciding result is named in advance.

Runtime workload: entity count, trail persistence, spatial scale, update cadence, and temporal integration are compositional parameters, not just performance settings. Record environment, workload, initialization, warmup, sample window, frame intervals or their distribution, memory trend, and any degradation event. Cap spawn and update work, cull what is invisible, expire, pool, reduce sampling or density, and optimize only measured hot spots. Thresholds are set per project; none is supplied here. After an optimization, replay the original symptom and one adjacent regression. A renderer migration needs a new baseline.

Apply backpressure at the first saturated stage. If generation outruns review, stop generating and compare. If the active hypothesis, baseline, and next test no longer fit in working context, checkpoint and split. If runtime evidence cannot be read across platforms, isolate environments. If two owners would edit the same system, serialize or divide at a real interface. The bottleneck is usually judgment, not rendering.

### B. Image generation prompts

The costly unit is a generation call. Plan one labeled spec per asset, a small number of targeted iterations, and treat a batch as an explicit strategy decision, not an accident of retries. The budget bounds generation effort per request; it does not bound the creative scope of the assets.

- Stakes set the budget. A brand hero image justifies iterations a placeholder never will. Alternatives when the budget is unclear: a time-boxed session with an explicit note of what is incomplete, a shared spec template reused across similar assets, or an iteration budget set by the reviewer for costly assets.
- `n` makes variants of one prompt. `generate-batch` runs many prompts. Confusing them spends calls on the wrong axis.
- The CLI builds backpressure in: `generate-batch` requires an output directory and defaults to concurrency 5, which bounds both parallelism and file sprawl.
- Good: eight game icons run once through a JSONL manifest. Bad: twelve full-prompt rewrites chasing one hero image. Borderline: three extra `n` variants for a shortlist, labeled as variant exploration.
- A generic working size for agent sessions (one primary task, up to ten source files, up to three delegated subtasks, a written completion audit) is provisional and not specific to image work.

Typical iteration counts per asset type are not measured. "A small number" is a default, and whether writing the spec first reduces iterations is untested. To find out, count calls and iterations in recorded sessions.

### C. Local vision reading

Stage a modest batch once, analyze two at a time, and split the batch when the manifest becomes hard to review. Serial analysis is the reliability fallback.

- Bad: eight concurrent calls on the 24 GB host. Upper borderline: three calls on small images.
- A 12-image batch is manageable. Two hundred staged screenshots may produce a manifest nobody can use; split it.
- Gains beyond two concurrent calls are probably small, and a third risks running out of memory. Neither statement is measured.

## Reliability Target

No target below has been measured. Each is a promise to test, not a result.

### A. Algorithmic art

Reliability means keeping an explicit promise under stated conditions. It is not maximizing every metric, and aesthetic agreement is not a percentage. Keep the target separate from the observed result. For each measured target record population, candidate identity, environment, method, pass condition, exceptions, and how far the conclusion reaches.

Proposed targets with no baseline (not observed results): every material recommendation states its evidence basis; at least 18 of 20 sampled routing decisions are correct; no unsupported production, security, latency, or reliability claim; every avoid or failure case names a recovery path. The 18-of-20 figure needs a declared sample and an adjudication rule before it means anything.

| Target | Promise | How to collect evidence | Boundary |
| --- | --- | --- | --- |
| Evidence basis kept | Each material recommendation says whether it rests on something read, something refreshed, something measured, or inference or judgment | Review the claims; confirm named material was actually read or is marked unrefreshed | "100 percent" is a wish until the population of recommendations is defined and counted |
| No unsupported claim | No final production, security, latency, reliability, platform, or artistic-universality claim lacks evidence, method, or stated uncertainty | Search the claims and trace each to a source or run | A found unsupported claim is removed, bounded, or verified |
| Routing quality | Each task gets primary, companion, avoid, or escalate plus a reason; the team sets the sample target beforehand | A representative task set that is not cherry-picked; hide the expected verdict where practical; record disagreements and the cost of errors | One sample does not establish general routing accuracy |
| Recovery path clear | Every failure or avoid decision names rollback, simplification, switch, escalation, owner, or adjacent route | Cross-check anti-patterns, failure modes, routing, and verdicts against next actions | "Retry" alone, or a pointer to a neighbor with no owner, is not a path |
| Render present and framed | Every promised state is seen directly: not blank, framed, readable, no incoherent overlap or clipping | Fresh captures labeled by viewport and state, a pixel-presence probe where blank output is plausible, console review, a named person looking | A passing build or launch cannot satisfy this |
| Seed and state replay | Reproducible profile: recorded seeds, init order, controls, viewport, and state restore the promised output. Curated: one edition restores. Ephemeral: non-repeatability is declared and accepted live | Repeat runs; compare at the same temporal points in the declared environment | Pixels can differ across platforms; define bounded visual equivalence when identity is not feasible or promised |
| Control bounds and meaning | Every exposed control is safe over its range and has a perceptible, interpretable effect | Minimum, representative, maximum sweeps; invalid input; runtime observation; reviewer describes the effect | Nonlinear is fine. Dead, redundant, or runaway controls fail until removed, merged, or bounded |
| Viewport and temporal coverage | Passes every declared size and the start, mid, long-run, and interaction states its mode needs | A risk-based matrix of fresh evidence tied to candidate identity | Do not generalize past tested surfaces |
| Runtime envelope | The project-defined workload stays inside a measured frame, memory, interaction, or completion-time envelope | Target-class hardware and browser, workload, warmup, sample window, distribution or trend, stress behavior | No universal threshold; a local observation is not a cross-device guarantee |
| Degradation keeps identity | When capacity is exceeded, bounded work or lower density restores the envelope and the dominant behavior stays perceptible | Compare fixed-seed normal and degraded states against runtime and visual criteria | Meeting timing by erasing lifecycle, rhythm, composition, or interaction fails |
| Restore and export | A second run recreates the selected state from revision, seeds, controls, viewport, time, environment notes, export settings | An independent restore, and inspection of the delivered file, not only the preview | Missing assets or platform differences become named dependencies |
| Aesthetic acceptance | The named reviewer accepts against versioned observable criteria, with reasons and uncertainty | Pairwise comparison, rubric notes, monochrome or ablation probes, final verdict | Bounded judgment, not objective beauty or general preference |

Pick a reliability profile before testing:

- Reproducible candidate: promises replay, control stability, target-surface behavior, runtime envelope, visual acceptance, restore and export.
- Curated edition: promises one named seed or state and its restore path. No claim about other seeds.
- Ephemeral run: rejects exact replay on purpose, but promises live execution, bounded workload, framing, safety, and observed concept behavior.
- Interactive tool: adds input validation, a persistence or reset policy, control semantics, accessibility, and repeated-session behavior, owned by the tool workflow.

Targets, good to bad:

- Good: "On the named mobile browser and workload, the selected edition stays within the project's frame envelope for the declared interval; fixed-seed degraded density keeps slow coherent drift; result and capture attached."
- Bad: "Runs at 60 FPS everywhere", with no environment, sample, identity, or evidence.
- Borderline but valid: "Only seed 1842 is accepted as this edition; other seeds were not evaluated for composition."

Give every material promise one adverse case: maximum supported density, resize, reset, long-run cleanup, invalid control, layer ablation, or an alternate seed. Sample risks deliberately and publish exclusions. After a bounded change rerun only the affected gates: controls changed -> control and candidate evidence; renderer changed -> runtime, determinism, framing, export. A candidate may complete with known uncertainty only when the consequence, owner, reopening trigger, and excluded claim are written down.

### B. Image generation prompts

Success is defined operationally: right subject, right style, exact text, edit invariants intact. Those are checkable. These targets judge the prompting discipline, not the image model's quality.

Proposed targets, all without a baseline (the first measured cycle defines what is achievable):

- every recommendation keeps its evidence basis visible;
- at least 18 of 20 sampled uses route to the correct decision (no sampling procedure exists yet, so this number is a proposal only);
- no unsupported production, security, latency, or reliability claim;
- every avoid or failure case names rollback, escalation, or the next route;
- for assets that carry labels: every rendered word matches its quoted text;
- for edit chains: every invariant survives from original to final.

Each target needs a metric, a sampling method, a population, an owner, and the corrective action a miss triggers. Quoting unmeasured percentages as achieved performance is false rigor. Alternatives to rates: binary pass or fail delivery audits, or a postmortem on every shipped defect.

Text accuracy is the cheapest objective check in this mode: the rendered words match the quoted string or they do not. Compare edits against the original image, not only the previous iteration; checking the latest step alone misses cumulative drift.

- Good: three sampled infographics with every label matching its quoted text.
- Bad: reporting an 18-of-20 that nobody sampled.
- Borderline: an edit audit against the previous iteration only, recorded with that caveat.

### C. Local vision reading

Two targets, neither baselined: every call uses a staged `/tmp` path, and every staged image is at or below the resize bound. A staged path does not prove a resize, so both scans are required. A raw-path call on a verified-small file is recorded as a deviation, not silently counted as compliant.

## Retry Backpressure Guidance

A retry must change the failing condition or what is known about it.

### A. Algorithmic art

A retry is an experiment meant to change what you know about a failure. Before spending one, keep a safe failing state where possible and write down: candidate identity, failed claim, observed signal, failure class, hypothesis, the one controlled change, what result would discriminate, budget, owner, stop condition. Running again with no such record is justified once, and only to test whether the signal was transient.

| Failure or blocker | Next action | Discipline | Stop or escalate when |
| --- | --- | --- | --- |
| Transient launch, capture, or environment interruption | Repeat the same command with the same candidate identity; note the environment state | One identical repeat separates transient from repeatable. Do not edit art code at the same time | It repeats: now it is an execution failure to diagnose |
| Stale guidance or platform fact | Re-read the working rules, or do one claim-specific refresh from a primary source | Keep old and new claim, scope, checked date, conflict, decision impact | One bounded refresh does not resolve it: go to the owner, a narrower document, or stated uncertainty. Do not widen the search without limit |
| Missing candidate or context identity | Stop implementing; restore revision, seed policy, parameters, viewport, time, rubric, latest evidence | Resume from the first explicit next step after the snapshot; do not guess shifted state | The accepted state cannot be rebuilt: call it a recovery failure or the loss of a curated output |
| True contradiction between rules or requirements | State both claims; compare authority, relevance, version, scope, user goal; then build a discriminating prototype or ask the owner | No broad architecture change until the consequence is clear | The conflict changes primary ownership, irreversible delivery, safety, or something only the user can decide |
| Concept or family mismatch | Simplify, go monochrome or ablate, compare one plausible family, or archive the hypothesis | Keep the brief and the failed criterion; a new system identity needs a new baseline | Repeated variants fail the same concept criterion: switch, or return to concept selection |
| Control or state failure | Freeze seed and state; sweep or isolate one control; validate bounds; separate state transitions | Several coordinated edits count as one retry only when they implement one shared hypothesis, such as removing render-side mutation | Persistence, input, or lifecycle outside the art core is the cause: escalate to the tool or host owner |
| Runtime overload or resource growth | Contain by reducing density or disabling nonessential layers; instrument the measured hot spot or leak | Change one workload cause; replay the same normal and stress states; check concept identity as well as timing | The simple renderer cannot meet a measured required behavior: justify a backend change |
| Blank, clipped, or temporally wrong render | Keep console, dimensions, state time, capture, identity; inspect initialization, visibility, resize, assets, transforms | Fix the smallest likely presentation or lifecycle cause; recapture every affected target state | Renderer, asset, camera, or shell integration is at fault: escalate with exact evidence |
| Ownership or write collision | Freeze overlapping changes; decide whose correctness is primary; one owner per mutable subsystem | Resume after inputs, outputs, lifecycle, and integrated acceptance are explicit | Authority is unresolved: escalate, do not merge competing state models or overwrite someone's work |
| External state unavailable | Keep the last reproducible baseline; wait, reroute, or narrow to independent evidence | Do not churn local code to imitate a service, device, venue, approval, or source that owns the blocker | The external condition changes, or the owner changes scope |
| Review or candidate backlog | Stop generating; group candidates by the active criterion; drop low-information runs; compare a bounded set | Generate again only after reviewers select, reject, or name a new question | The bottleneck is disagreement or an absent reviewer: escalate decision ownership |

By phase. Exploration: a bounded variant budget may vary several dimensions, but every kept run needs a lesson. Convergence: frozen baseline, one material factor per comparison. Acceptance: never retry a failing gate by weakening or quietly changing the criteria. Version a legitimate requirement change before producing new evidence.

Backpressure by what is saturated:

- Generation: stop producing variants when the active question is missing or kept candidates exceed review capacity.
- Review: show fewer comparisons at equivalent states and name the decision owner. More renders cannot settle taste that nobody owns.
- Context: checkpoint hypothesis, baseline, exact failing gates, files, risks, next action. Reread the current specification before broad edits.
- Runtime: cap work and keep a stable diagnostic state before optimizing or changing renderer.
- Sources: narrow to the claim that can alter implementation; mark unrefreshed external facts as such.
- Ownership: one owner per generated file or mutable subsystem; check paths, evidence, and integration invariants at handoff.

Examples:

- Good retry: mobile clipping reproduces under seed 1842, unchanged controls, a named viewport. Hypothesis: coordinate scaling. Change only normalized framing, recapture all target sizes, confirm no reset or composition regression, close the retry.
- Bad retry: "make it more organic" regenerates with a new seed, higher density, new colors, and extra noise until one image is preferred. No cause was tested.
- Borderline coordinated retry: a renderer migration touches several files but tests one measured hypothesis (the current renderer cannot sustain the required density). It sets a new baseline and reruns determinism, framing, runtime, and export gates.

Keep disproven hypotheses when they were expensive or likely to recur. Count the retry budget by unchanged hypothesis, not by shell commands: diagnosis, implementation, and recapture can be one experiment. Budgets are local policy based on consequence and information value; one bounded refresh for stale evidence is a conservative default, not a law. Resume only when the retry can separate the suspected cause, the saturated resource has capacity, or the external condition changed. Editing locally during an external blocker often destroys the evidence needed later.

### B. Image generation prompts

Classify the failure before retrying: transient, stale fact, missing context, or a true contradiction.

- One targeted change per retry, with invariants restated.
- The same defect repeating means the spec needs redesign. Do not loosen constraints until something passes.
- A labeled round of `n` variants is allowed; converge afterwards with one change at a time.
- When stalled, use one of: a fixed attempt budget, a change of use-case slug, or escalation to the user.
- Stale external fact (model name, size list): one bounded refresh, then escalate.
- Batches: bounded concurrency and per-job failure isolation. Stop when gates are red. Checkpoint after each batch.
- Reread the spec before broad rewrites, commits, pushes, or anything destructive. One owner per file or batch.
- Network-level retry is separate from prompt retry. The CLI handles it with `--max-attempts`.

### C. Local vision reading

Change the failed condition first:

| Failure | First change | Then |
| --- | --- | --- |
| Timeout | Resize to 600 px | Only after resize options are used up, raise the timeout to 240 s |
| Path error | Rediscover with Python and restage | Check the staged extension |
| Out of memory or contention | Fewer concurrent calls | Serial |
| Slow but no error | Inspect `.env` routing | Then re-time one smoke call |

Three identical retries are wrong. Hammering the GPU makes contention worse. Queue a burst (for example 30 images overnight) instead of raising parallelism.

## Observability Checklist

### A. Algorithmic art

Observability here is selective decision memory, not surveillance of the creative process. Keep an observation only when someone will use it to reproduce, diagnose, compare, accept, refresh, apply backpressure, or hand off. Raw diagnostics may live briefly; summarize the decision and let the noise expire.

One candidate event records:

- phase: exploration, convergence, acceptance, recovery, or export;
- candidate identity: code revision, run-card version, seed and init order, parameters, viewport, temporal or semantic state, renderer, material environment factors;
- active hypothesis: the concept, control, runtime, or delivery claim under test;
- what was read and what was deliberately skipped, with reasons, and whether any external fact was refreshed;
- evidence: exact command and result summary, fresh capture or video, state snapshot, runtime observation, console outcome;
- rubric: criteria version, reviewer, verdict, reason, disagreement, bounded uncertainty;
- decision: keep, simplify, switch, optimize, reject, accept, archive, wait, or escalate;
- next trigger: what evidence, change, or requirement resumes or reopens work;
- why it is retained: baseline, selected candidate, informative rejection, regression evidence, or final export.

| Claim or decision | Smallest useful observation | Add when | Limit or cost |
| --- | --- | --- | --- |
| Guidance-backed choice | Which rule, what constraint was taken from it, decision impact, unrefreshed status of anything external | Checked date, heading, conflict record after a refresh | Having a document open does not show it was understood or applies |
| Concept-system fit | Representative fixed-seed render, named criterion, reviewer's reason | Monochrome probe, layer ablation, pairwise family comparison when roles are unclear | Designated judgment, not universal preference |
| Reproducibility | Revision, seeds, init order, controls, viewport, state, environment, second-run result | State snapshot or visual-difference aid when exact replay matters | Instrumentation and cross-platform rendering can shift timing or pixels |
| Control behavior | Bounded sweep: input value, visible effect, runtime effect, invalid-state result | A trace or snapshot for nonlinear interactions | Big combinatorial sweeps exceed review capacity |
| Framing and visibility | Fresh capture per declared viewport and state, plus console result | Pixel-presence or canvas-bounds probe when blank or off-screen output recurs | Screenshots do not establish motion, interaction, or long-run stability |
| Temporal behavior | Time- or state-labeled samples of start, representative, and long-run or interaction transitions | Short video, live-review note, or state trace for qualities stills cannot show | Wall-clock time is ambiguous when performance changes the system's age; keep the step or frame count |
| Runtime envelope | Environment, workload, initialization, sample window, frame intervals or completion times, degradation event | p50, p95, p99, memory trend, or a trace only when sample size, population, and threshold make them meaningful | Small samples, nonstationary animation, device variation, and instrumentation overhead make percentiles misleading |
| Reviewer workflow | Reviewer, rubric version, evidence viewed, verdict, reason, uncertainty, next action | Decision time, only if review throughput is the real bottleneck | Faster review can reward shallow inspection |
| Recovery | Failing candidate, reproduced symptom, hypothesis, controlled change, after-state, adjacent regression result, residual risk | Trace or resource sample suited to the cause | A fix report with no replay of the original symptom does not prove recovery |
| Export | Settings, dimensions, temporal state, output identity, restore path, separate visual verdict | Codec, color, asset, or platform metadata when they can change delivery | A correct live preview is not evidence for a separately generated file |

Depth by phase. Exploration: a concept question, enough identity to learn from a run, one visual observation; keep little. Convergence: frozen identity and comparable evidence. Acceptance: every promised viewport, state, environment, restore, export, and reviewer gate. Ephemeral work replaces exact replay with live-state evidence and a stated non-repeatability promise. Installations add hardware and long-run observations through their own workflow.

Quality checks on the record itself:

- Every evidence item matches the current candidate or is labeled historical.
- Every metric names population, environment, sample window, threshold or intervention, and how far the conclusion reaches.
- Every capture names viewport and temporal or semantic state.
- Runtime and visual evidence share one candidate identity. Do not pair the fastest run with the best-looking render.
- Instrumentation overhead is noted when it can change timing or interaction.
- No secrets, private user content, or telemetry the host prohibits enters the record.
- Every kept variant has a decision reason; temporary raw output has an expiry.
- The evidence store lasts as long as the handoff needs; essential results are summarized in case links disappear.

Examples. Good: one compact event links seed 1842, exact controls, mobile and desktop captures at the same state, a density observation, rubric version, reviewer acceptance, export settings, restore result. Bad: an unlabeled console transcript, a percentile chart with no sample window, a screenshot from unknown parameters. Bounded qualitative: a note on an ephemeral live performance names reviewer, venue state, the calm-motion criterion, the instability seen, instrumentation limits, and the next rehearsal test, with no pretense of exact replay.

Test the observability. Replay a seed, resize, raise density, reset, or cause another safe perturbation, and confirm the evidence identifies the candidate and points to a next action. An undetected blank render, a stale capture accepted as current, or an accepted state that cannot be rebuilt is an observability failure even after the art bug is fixed. The best packet is smaller than a transcript because it keeps decisions, not chronology.

### B. Image generation prompts

Record per asset: the final labeled spec, the execution path, each input image's role, the change made at each iteration, the final prompt, the final saved path, inspection findings, and accepted or rejected. Where relevant also record what guidance was read or skipped, the proof command or question or artifact, reviewer time or latency, tool calls, retries, and a completion audit. Prefer a compact summary over a raw transcript.

Long `generate-batch` campaigns need a journal: which jobs ran, which failed, which outputs were selected.

### C. Local vision reading

Keep: the staging manifest, per-call timings, error text verbatim, the effective vision configuration and model including the `AUXILIARY_VISION_*` values (key redacted), and a summary of the raw answers.

- Exact error text matters for diagnosing Unicode names.
- The evidence most often missing is the effective model configuration.
- How long to keep these records has not been tuned.

## Performance Verification Method

### A. Algorithmic art

Performance is computational and perceptual at once. Slow or uneven execution changes rhythm, decay, trails, interaction, and the apparent force of a system. An optimization can also destroy the behavior that made the piece meaningful. Always inspect the rendered output; a text-only success claim is not accepted for a visual or interactive artifact.

Define the promise before measuring:

- mode and delivered path: static preview, animation, interaction, live installation, recording, or offline export;
- candidate identity: revision, seeds, controls, viewport, temporal or semantic state, renderer;
- target-class environment: device, browser or runtime, display, material platform conditions;
- representative and stress workload: entity count, spawn behavior, samples, recursion, trails, buffers, interaction, duration, export dimensions;
- project envelope: the frame behavior, interaction response, resource trend, or completion time the user will notice, and why;
- degradation policy: what work is reduced first and which concept-bearing behavior must remain;
- scope: which environments and states the conclusion covers, and which are untested.

Staged gates keep exploration fast without weakening acceptance:

| Stage | Minimum protocol | Decision it enables |
| --- | --- | --- |
| Quick exploration | Launch a minimal fixed-seed state, look at it, note gross frame or interaction failure; no elaborate profiling | Is the prototype worth more work, or does it want a simpler mechanism |
| Representative candidate | Separate initialization from steady behavior; target viewport and normal workload after warmup; frame intervals or completion time plus the rendered state | Are controls, density, renderer, and composition viable for convergence |
| Stress and degradation | Raise only the declared stress dimension; capture the failure boundary; trigger bounded degradation; compare fixed-seed normal and degraded visuals | Set caps or presets, change work bounds, optimize a measured cause, or narrow platform scope |
| Long run and lifecycle | Watch the promised duration, reset, resize, remount or teardown, resource trend, accumulated state | Find leaks, temporal saturation, duplicate listeners, stale buffers, lifecycle drift |
| Final export or delivery | Measure the delivered path separately; inspect output dimensions, state, assets; restore from the candidate's manifest | Accept, narrow, or reject the delivery promise |

Method by claim:

| Claim | Useful evidence | More detail when | Caution |
| --- | --- | --- | --- |
| Smooth or stable animation | Frame-interval samples, or another cadence observation the user would notice, tied to workload and state | Intermittent stutter changes perception: use distributions and inspect spikes; traces only to separate causes | Average FPS hides bad episodes; display refresh and background throttling distort the reading |
| Interaction response | Input-to-visible-change observation under representative workload, with event and render state aligned | The source of delay is unclear: add traces or timestamps | Instrumentation can disturb the interaction being measured |
| Memory or lifecycle stability | Active entity, buffer, and listener counts and resource trend across duration, reset, teardown | A reproducible upward trend appears: profile allocations or retainers | One short run cannot bound a long run; visible density can stay flat while hidden state grows |
| Offline render or export | Wall-clock completion, output integrity, dimensions, peak resources where they matter, separate visual inspection | Batch behavior is promised: repeat runs or sample inputs | A slow export is fine if its completion boundary and context allow it |
| Time spent writing guidance or reviewing | Input size, number of documents inspected, tool calls only when they affect cost, wall-clock duration, reviewer decision, whether the next action is clear | A repeated-task population with enough observations exists | Reviewer speed without quality and complexity context is a vanity metric, and it says nothing about artwork runtime |

Percentiles are conditional tools. Report p50, p95, or p99 only when population, observation count, warmup, window, environment, and decision threshold are stated and the distribution answers a real claim. Small samples, nonstationary animation, garbage collection, thermal state, device pixel ratio, background tabs, and profiler overhead make precise-looking numbers misleading; record those factors when they affect the conclusion.

For time-based simulations, separate simulation-step stability from render cadence when dropped frames could change physics or lifecycle. Use elapsed time, fixed steps, or another deliberate model, and verify behavior under slower rendering. Frame count and time are not interchangeable. (The plain-canvas starter in SKILL.md uses fixed steps with a cap on catch-up steps per frame.)

Candidate packet: target and reason; candidate identity; environment; normal and stress workloads; initialization and warmup; sampling window; raw or summarized observation; fixed-seed normal and degraded captures; verdict on preserved identity; observed result; uncertainty; excluded environments; retest trigger. Repeat enough to tell a stable local observation from a one-run anomaly, and do not claim population behavior from one machine.

- Pass: the declared envelope holds on tested surfaces, or bounded degradation restores it while the concept-bearing mechanism stays perceptible; the delivered render is visible and framed; the reviewer knows the next action and stop condition.
- Fail: metrics pass only after the piece's identity is removed; evidence belongs to another candidate; only the best-looking state was tested; performance is claimed with no environment or workload.
- Borderline: a high-density preset exceeds the default envelope. It can stay when clearly labeled, optional, and bounded while the default remains stable.

After an optimization, replay the original symptom and one adjacent regression. A density correction verifies runtime and composition. A renderer migration sets a new baseline and reruns seed, viewport, frame, and export evidence. A faster result is not recovery when it moves cost to initialization, leaks state over time, or damages the accepted criterion.

Performance findings can legitimately change the artistic design. Systems that keep their identity under simplification deploy more widely. Deliberately extreme work may choose fixed hardware or offline delivery, with its boundary and failure behavior stated.

### B. Image generation prompts

Per asset log call count, size, quality, iteration count, and wall-clock time. For batches log concurrency and job count. Report ratios with their sample sizes.

Larger size and higher quality raise latency and cost. High input fidelity raises input token use. No prices are recorded here, so comparisons are relative to parameters only. Pair iteration counts with inspection records: a low count can mean nobody read the rendered text.

### C. Local vision reading

Once per new host or model version, run a paired measurement: the same image raw and prepared. Publish input size, host, model version, and both timings. A raw timeout is a valid measured outcome. An illustrative good result would read "110 s raw, 14 s prepared"; that pair is an example, not a measurement.

- Do not quote the documented host's figures as local performance.
- Re-baseline after any change of Ollama version, model, or quantization.
- Answer quality is outside this test.
- The first call after idle may include model load time. Treat it as a possible false alarm.

## Scale Boundary Statement

### A. Algorithmic art

This guidance is enough while one bounded code-native visual hypothesis has one dominant system, compact controls, one primary renderer, known delivery surfaces, states that can be inspected directly, and one owner who can reproduce failures and accept evidence. Technical difficulty alone does not force a split: a dense shader or recursive system can stay one core when concept, state, lifecycle, and recovery are singular.

It stops being enough as the only workflow when a new surface has its own correctness, state, lifecycle, ownership, delivery, or recovery. Add a domain companion or hand off primary ownership instead of stretching art vocabulary over a contract nobody owns.

| Dimension | Signal that the boundary is crossed | Options | What the art core still owns | Integrated proof |
| --- | --- | --- | --- | --- |
| Several visual systems | They have independent state, controls, lifecycle, owner, or acceptance and can fail separately | Simplify to one carrier; extract subsystems; or keep a justified coupled model under one owner | Shared concept, role map, ownership of random streams, workload priority, ablation evidence | Subsystem gates plus one render showing the intended interaction and degradation order |
| Several scenes or outputs | Scenes have separate identities, exports, viewports, timelines, or verdicts | Split run cards and ownership by scene; share palette or concept constraints on purpose | One concept hierarchy and rules for what stays consistent | Each scene restores alone; the whole sequence gets an integrated review |
| Product or authoring shell | Saving, undo, presets, forms, navigation, accessibility, repeated workflows become first-class | Add a front-end or creative-tool workflow through a narrow art-core API | Meaningful controls, seed and state manifest, render lifecycle, dimensions, performance envelope | A real user flow manipulates and exports the art with no invalid state or visual regression |
| 3D behavior | Camera, depth, lighting, materials, picking, scene resources, or geometry carries the concept | Add a 3D workflow or move ownership; keep a 2D prototype only as concept evidence | Concept-system correspondence, promised determinism, workload bounds, visual acceptance | Non-blank target captures, meaningful camera states, interaction, resource cleanup, integrated verdict |
| Audio, sensors, physical installation | Signal processing, calibration, projection hardware, venue geometry, failover, or live operation decides the output | Add signal, hardware, and operations ownership; constrain supported venues | Parameter intent, live-state criteria, graceful degradation, declared replay or ephemerality | A rehearsal in a venue of the same class: calibration, failure behavior, framing, timing, operator recovery |
| High-resolution or offline production | Output uses a separate renderer, tiling, codec, color path, long job, or memory envelope | Add an export workflow, constrain the format, or isolate an offline renderer | Candidate identity, seed, temporal state, composition criteria, export manifest | The delivered file is rebuilt and inspected apart from the preview; failure and resume are bounded |
| Multi-platform delivery | Browser, mobile, GPU, installation, or recording surfaces behave differently and are all promised | Narrow support; split platform diagnosis; or a shared core with adapters | Shared system semantics; per-profile workload, resize, input, evidence | Each promised surface passes its gates and equivalent concept behavior is reviewed across them |
| Production traffic or multi-user state | Concurrent sessions, persistence, isolation, abuse, availability, or operational recovery faces users | Add backend, security, persistence, and operations ownership with explicit service objectives and data contracts | Visual state schema, seed policy, bounded rendering client, visible degradation | End-to-end tests of state correctness, failure isolation, load boundary, rendered recovery |
| Parallel agents | Workers would edit the same file, state model, scene, or acceptance decision | One owner per generated file or mutable subsystem; serialize shared decisions; merge through contracts | Exact paths, evidence invariants, candidate identity, one integrated visual owner | Scoped tests pass alone, then merge-time state and render evidence shows no drift |
| Long-running context | The hypothesis, baseline, failing gate, or next action no longer fits reliably in working context | Checkpoint in a journal, narrow the reading, split independent hypotheses, resume from evidence | Current concept, files in motion, candidate identity, risks, next discriminating action | The snapshot matches the filesystem and tests before changes resume |
| Large repository | Discovery is unbounded, or a flat list of files cannot identify the governing guidance and blast radius | Narrow with a repository graph or structured search; rank governing, supporting, and conflicting material; isolate the art core | Claim-scoped provenance and fit with project patterns | Dependencies and ownership are known before integration; a large reading list is not context quality |

Pick the cheapest response that restores coherent ownership and evidence:

- Reduce scope when optional platforms, variants, or controls create disproportionate uncertainty.
- Constrain the environment when fixed hardware, venue, format, or offline delivery is part of the specification.
- Build a vertical slice when the hardest risk is whether the real subsystems compose end to end.
- Extract a subsystem when its state, lifecycle, acceptance, and recovery can be tested alone.
- Run a disposable backend spike when one measured feasibility question blocks the renderer choice.
- Hand off primary ownership when another discipline's failure now costs the most.

At each boundary record: owner; inputs and outputs; shared and private state; who owns the random and noise streams; clock or temporal semantics; lifecycle; error and recovery behavior; target dimensions; interaction; accessibility; workload; degradation priority; evidence; integrated acceptance owner.

Two traps. A single global seed does not guarantee determinism if subsystems consume randomness in an order-dependent way. A single clock does not guarantee temporal coherence if one subsystem drops or accumulates work differently.

- Good direct scale: one dense WebGL piece stays one core because hypothesis, state, controls, target installation, and recovery are singular, even though it needs specialist profiling.
- Bad overgrowth: five scenes, sensors, an authoring dashboard, mobile clients, and offline export share one run card, and two agents mutate the same state.
- Good split: a multi-scene sensor installation gives each scene and hardware bridge an owner, keeps one concept and one degradation hierarchy, and proves the whole venue path in rehearsal.

Modularity is not enough. Show that one subsystem can pause, degrade, reset, or fail without corrupting shared state or erasing the primary experience, and that under pressure the system knows which layer yields first and why. When the split point is unclear, cut a vertical slice through the hardest real boundary. Do not build a framework for every future platform before a representative render exists.

### B. Image generation prompts

Small counts: prompt each asset individually. Larger counts: one shared, versioned template plus a JSONL manifest with per-job overrides, declared output directories, and bounded concurrency. Forty icons are one manifest and one template. Eight assets can share one written template. The count at which a manifest starts to pay off is not measured.

Re-check model parameters after every model release.

### C. Local vision reading

The guidance covers a single host and a single model, for occasional batches of raster files. Queue bursts instead of raising parallelism. Sustained saturation is an architecture or hardware decision: a second host, scheduled windows, or a cloud fallback.

Video and PDF are out of scope; frame extraction and rasterization are separate jobs. Rasterizing a short PDF and then staging the pages is adjacent and not covered.

## Outcome Metrics and Feedback Loops

### A. Algorithmic art

Metrics exist to choose the next action. Mechanics (launch, replay, cleanup, bounds, framing) can use binary or measured gates. Aesthetic selection stays reviewer judgment, made accountable through criteria, pairwise comparison, captures, and recorded reasons. Drop any measurement that cannot support one of: keep, simplify, switch, optimize, reject, accept, archive.

| Signal | How to collect | Decision it routes | Boundary |
| --- | --- | --- | --- |
| Concept-system legibility | Write observable criteria before choosing a candidate; inspect a representative fixed-seed render, a monochrome probe, useful layer ablations | Keep the family when its defining behavior carries the concept; simplify or switch when the explanation carries more than the pixels | Reviewers may disagree. Monochrome is a probe, not a required final style |
| Attributable iteration | Freeze baseline code, seed, viewport, time, criteria; change one variable; compare equivalent states | Keep a change only when its benefit and cost can be named | Broad exploration may vary several things but cannot support a causal claim |
| Control sensitivity | Sweep minimum, representative, maximum for each exposed control; note perceptual and runtime effect | Remove dead controls, merge redundant ones, clamp unsafe ranges | Nonlinear controls are valid; the requirement is interpretable behavior, not monotonic response |
| Seed robustness | Converge on one baseline seed, then inspect a small declared set or call the result a curated edition | Generalize a preset only when behavior survives the promised variation | No universal seed count exists. Choose seeds that expose this piece's composition and density risks |
| Viewport and temporal coverage | Each target size at start, mid, long-run or stress, and interaction transitions | Fix framing, resize policy, lifecycle, or saturation before acceptance | A static fixed-format piece can narrow the matrix explicitly |
| Runtime envelope | On target-class hardware: workload, environment, initialization, sample window, frame intervals, resource trend, degradation event | Bound work, reduce density, cull state, or justify a backend change | The project defines the envelope |
| Restore and export | Rebuild the candidate from revision, seeds, init order, parameters, viewport, time, environment notes, export settings | Accept the export only when another run reaches the state with no hidden context | Bounded visual equivalence may replace byte identity across platforms |
| Review yield | For each observation: verdict, criterion affected, evidence, uncertainty, next action | Continue only while review narrows a decision or an exploration budget remains | Short review time is not automatically good |

Two-stage loop. Exploration searches broadly with coarse prototypes, keeps few runs, and asks which concept or family deserves investment. Convergence freezes identity, varies one factor, uses the current criteria version, and accumulates acceptance evidence. Label the phase on every saved candidate so a surprising exploratory result is not mistaken for something export-ready.

The causal loop:

1. Record the hypothesis, baseline identity, criterion, and the smallest useful probe.
2. Render and collect only the evidence that probe needs.
3. Classify the first material failure: concept, system, control, runtime, presentation, or evidence.
4. Choose one action and state what result would reverse it.
5. Save a candidate only when it becomes the new baseline, an accepted result, or an informative rejection.
6. Before final acceptance, run the seed, viewport, temporal, runtime, restore, and reviewer gates the run card promised.

Criteria may change after a render reveals a missing quality. Version the change with its reason before the next comparison, and do not rescore earlier captures under the new criteria without saying the basis changed. Pairwise review usually works better than absolute taste scores, because reviewers can point at visible differences.

- Leading indicator: iteration makes a named concept or delivery criterion more legible under controlled comparison.
- Failure signals: novelty is praised with no definition of good output; seed, criteria, and several parameters change together; one seed or viewport is generalized; runtime improves while the dominant behavior loses identity; reviews pile up observations that lead to no decision.

Stop when the required mechanics pass, the reviewer accepts against frozen criteria, the candidate can be restored, residual uncertainty is recorded, and another iteration has no named decision value. Pivot when repeated changes fail the same concept-system criterion. Archive a rejected hypothesis when its evidence can prevent going in circles. An endless variant stream is not a feedback loop.

### B. Image generation prompts

Track: iterations per accepted asset, constraint violations caught at inspection, stranded-asset count, and whether the output reached the workspace. No baselines exist.

- Rising iterations: suspect a weak spec first.
- Low iteration counts may mean nobody inspected the text.
- Leading indicator: each iteration improves against named taste criteria, not random novelty.
- Failure signal: the guidance or the session celebrates creativity without defining what good output is.

### C. Local vision reading

Track: timeout count per batch, ratio of staged to raw paths, resize compliance, and seconds per image.

- Review any call that takes more than twice the 10 to 20 s band of the documented host. Forty seconds per image is an investigation trigger there.
- A record with zero timeouts may only mean the inputs were tiny.

## Completeness Checklist

### A. Algorithmic art

Run this against one identified candidate, not the project in general. Start from: code revision, run-card version, seed policy, parameters, viewport, temporal state, environment, criteria version. Reuse earlier evidence only if those fields still match and the checked behavior cannot have changed. Every item marked not applicable needs a concrete scope reason.

Routing and evidence

- [ ] The artifact, the audience or viewing context, the delivery surface, and the contract that decides correctness are explicit.
- [ ] The art mode is primary, companion, or avoided; companion ownership and integration boundaries are named.
- [ ] Material claims separate what the rules say, what was refreshed externally, what was measured on the artifact, inference, reviewer judgment, and remaining uncertainty.
- [ ] Adopt, adapt, avoid, switch, and cost-of-error decisions name their evidence and what would reverse them.

Concept and visual system

- [ ] The concept sentence says what behaves, what constrains it, how it changes, and the intended effect.
- [ ] Static, animated, interactive, seed-driven, or a hybrid is chosen, with the temporal and interaction states it requires.
- [ ] One dominant family is named and its motion or spatial logic maps causally to the concept.
- [ ] Every secondary mechanism has one distinct role, supported by ablation evidence.
- [ ] One plausible alternative was compared or explicitly declined where the choice could change the implementation.
- [ ] The behavior still means something under a simplification probe: monochrome, sparse density, fewer layers, or low recursion depth.

Controls, state, and implementation

- [ ] The parameter surface is compact; each control has safe bounds, a baseline, and a perceptible, interpretable effect.
- [ ] Randomness and noise follow a recorded replay policy (seeds and init order where repeatability is promised), or ephemerality is explicit.
- [ ] Initialization, update, render, input, reset, resize, and teardown are legible enough to inspect and reproduce state transitions.
- [ ] Work is bounded by caps, expiration, culling, pooling, controlled sampling, or a mechanism suited to the system.
- [ ] The renderer follows project conventions or has a measured reason (behavior, density, dimensionality, interaction, export) for escalation.
- [ ] No application shell, effect layer, or public control exists without a requirement or a concept-bearing role.

Execution, runtime, and delivery

- [ ] The repository's real build or launch path succeeds for the representative state; console or runtime errors are recorded.
- [ ] Every declared viewport or fixed dimension was inspected under an explicit resize, reset, or recomposition policy.
- [ ] Start, mid, stress or long-run, and interaction transitions were checked where temporal behavior matters.
- [ ] Representative and stress observations name the environment and the project's envelope. No universal threshold was invented.
- [ ] Degradation restores the envelope and keeps the dominant behavior, or a fixed-capacity boundary is stated.
- [ ] Long-run cleanup and teardown were checked where state, listeners, buffers, trails, or off-screen entities can accumulate.

Visual acceptance and export

- [ ] Fresh captures or live evidence show non-blank, framed, readable output in every promised state.
- [ ] The criteria predate candidate selection or carry a versioned change with its reason; each criterion is observable enough to guide an intervention.
- [ ] The reviewer recorded accept, reject, or bounded uncertainty, with reasons and any disagreement.
- [ ] A fixed-seed baseline supports causal comparison, followed by the declared robustness check or an honest curated-edition boundary.
- [ ] The export records format, dimensions, temporal state, parameters, and identity, and was inspected apart from the live preview.
- [ ] A second run restored the candidate from the record with no unrecorded setup, within the declared environment limits.

Recovery and handoff

- [ ] Good, bad, and borderline examples are labeled as illustrations and do not claim that unrendered configurations were measured.
- [ ] Leading indicators, failure signals, stop conditions, and the next action are recorded; metrics that cannot change a decision are left out.
- [ ] The accepted candidate, the baseline, one informative rejection, final evidence, residual risks, and reopening triggers are kept; low-value variants are discarded.
- [ ] The next discipline is named when the art mode no longer owns the dominant failure.
- [ ] Someone else could state what is proven, what is bounded to an environment, what is artistic judgment, what is excluded, and what is uncertain.

Completion outcomes: `accepted_artifact` needs all applicable delivery and restore gates. `archived_study` needs a rendered observation, a supported or falsified hypothesis, and a reusable lesson, and must not claim export readiness. `rejected_candidate` records the failed criterion and the recovery or route. `blocked_candidate` names the external condition and its owner, and is not complete.

A curated edition may validate one seed on purpose. An ephemeral performance may replace exact replay with a declared non-repeatability contract and live evidence. These are bounded choices, not loopholes. No visual outcome is complete until the output has been observed.

### B. Image generation prompts

- [ ] Both execution paths are covered: built-in by default, CLI on explicit request.
- [ ] The generate-versus-edit decision and the one / variants / many decision were each made.
- [ ] The specificity policy was applied and additions are listed.
- [ ] Save-path precedence was followed.
- [ ] Coverage and fidelity were checked separately: every requirement appears in the spec (coverage), and the render matches the spec (fidelity).

### C. Local vision reading

Spot-check that a write-up of this mode still contains: the four rules, the six workflow steps, the five symptom rows, the 800 px and 120 s figures with their host, and `.env` taking precedence over `config.yaml`.

## Adjacent Reference Routing

### A. Algorithmic art

Route by the contract that decides correctness. Choose one primary owner, give each companion a narrow responsibility, and name one owner for integrated acceptance. In this library: product UI and shells go to `react-frontend`; diagrams, explainer and playground pages go to `visual-explainers`; a specific bitmap goes to mode B of this skill; long-session checkpoints go to `tdd-progress-and-resume`. The other rows have no dedicated skill here; treat them as disciplines to bring in.

| Neighbor | Make it primary when | Keep from the art mode | Boundary and handoff |
| --- | --- | --- | --- |
| Raster image generation or editing | The result is a specific bitmap, photo change, texture, sprite, or variant, not code-native behavior | Concept, visible acceptance criteria, reason for each variant, export inspection | Hand over source image or prompt context, target dimensions, edit constraints, visual verdict. Do not build a canvas runtime to deliver one image |
| Data visualization | Position, size, color, motion, or interaction must encode data truthfully | Generative behavior may style non-semantic layers or bounded transitions after the mappings are fixed | Visualization owns scales, labels, data integrity, accessibility, misleading-encoding checks; joint QA proves styling does not hide the truth |
| Front-end or application shell | Repeated user action, navigation, forms, hierarchy, settings, responsiveness, accessibility define success | Keep the art core renderable alone, with declared inputs, lifecycle, dimensions, workload | Contracts for container size, input events, motion preferences, pause and reset, loading, performance. The shell must not postpone proving the art |
| Interactive creative tool or playground | The user must author, save, compare, export, or manipulate the system through a polished control surface | Compact parameter model, seed manifest, candidate identity, render checks | The tool owns persistence, undo and redo, presets, validation, discoverability, export experience. The art mode still owns whether controls change visual behavior meaningfully |
| 3D scene or spatial visualization | Depth, camera, lighting, materials, geometry, picking, or navigation carries the concept | Concept-system mapping, determinism where feasible, workload bounds, inspection across meaningful states | The 3D workflow owns scene graph, camera, GPU resources, asset loading, spatial interaction |
| Game development | Rules, physics, player agency, progression, win and loss, or game feel is the artifact | Procedural backgrounds, effects, environments, generation subsystems | The game owns rule correctness and input loops. Define seed, state, and performance contracts so decoration cannot change gameplay |
| Manual graphic, illustration, or brand design | Authored composition, typography, identity consistency, or print production matters more than emergent behavior | Concept and critique structure; a generative system is optional | Design owns grid, type, brand assets, color standards, production output. Route away when code adds no needed variability or interaction |
| Timeline, simulation analysis, scenario planning | The user needs causal futures, decision branches, event sequences, or risk comparison | A generative visual may illustrate results later | Analysis owns assumptions, states, transitions, and consequences. Any art layer is downstream and carries no authority |
| Audio-reactive or installation work | Sensors, sound, projection hardware, physical dimensions, calibration, or live operation shape the piece | Creative seed, system roles, parameter policy, degradation behavior, candidate evidence | Add ownership for signal processing, hardware lifecycle, calibration, failover, venue tests. Browser-preview evidence alone is not enough |

Primary-owner test: which failure would most mislead or harm the user? Wrong data encoding makes visualization primary however elaborate the canvas. Broken navigation makes the front end primary even with a generative hero. Wrong game rules make the game primary. For a focused motion study, weak concept-system correspondence makes the art mode primary.

Hybrid contract: record subsystem owner, inputs, outputs, shared state, lifecycle, error behavior, dimensions, timing, accessibility duties, workload budget, degradation order, evidence. No decision has two owners. Several specialists may review; one decides each subsystem and one accepts the whole.

- Good direct use: a seeded canvas study whose motion is the entire deliverable. A generative background for a page is companion use.
- Bad route: ornamental geometry on a revenue chart before the scales are correct.
- Borderline: a data-driven artwork gives data truth and encoding to visualization, gives non-semantic particle texture to the art mode, and runs joint checks that density and motion never hide values or controls.

Routing is reversible until a representative prototype confirms the dominant model. Record what observation would reverse it. When unsure, build the smallest prototype that crosses the boundary with real data, input, camera, export, or hardware. Do not start full parallel implementations. Under shared runtime pressure the non-primary decorative layer degrades first, unless that would erase the stated artwork; write the priority down.

### B. Image generation prompts

- Reading or checking images with a model: mode C of this skill.
- Long sessions, checkpoints, resumable state for a batch campaign: `tdd-progress-and-resume`.
- Code-native visuals (HTML, CSS, canvas): mode A, `react-frontend`, or `visual-explainers`.
- Vector assets that already exist in the repository: edit them directly.

### C. Local vision reading

- Cloud or API image analysis: that provider's documentation.
- Creating images: mode B.
- Installing, updating, or tuning Ollama: Ollama's documentation.
- Other media (audio, video, PDF): their own tooling.
- Writing or restructuring a skill about this: `authoring-skills-and-references`.

## Source Evidence Mapping Table

Kinds of evidence: owner's working rules; local analysis (a synthesis, not a measurement); skill or tool snapshot from another project (documented intent at a date, restated here); observed (something run while preparing this skill, valid only for the listed conditions).

### A. Algorithmic art

| Topic in the skill | Evidence unit | Kind | Supports | Does not support |
| --- | --- | --- | --- | --- |
| Workflow order, default rules, output contract, guardrails | The owner's algorithmic-art skill (April 2026 snapshot) and its one-line invocation prompt | Owner's working rules | Method defaults: concept -> system -> controls -> implementation; one dominant behavior; p5.js or canvas; seeded replay; density reduction; update / render / input separation | Universal taste, or current runtime API facts. "Prefer living motion" is a default a justified static work may adapt |
| Philosophy template | The owner's algorithmic philosophy template | Owner's working rules | Movement framing, concept sentence, principles, philosophy-to-code table, failure check | An aesthetic. Names and metaphors illustrate a format; every translation is verified in a render |
| Pattern menu | The owner's generative pattern menu | Owner's working rules | Seven family cues and candidate knobs; the rule that palette and layers support the motion | Proof that a family fits a given brief, or permission to stack all families |
| Verification matrix, failure classes, run card, profiles, workload, retry, scale, metrics | Analysis digest on algorithmic art generation, dated 2026-07-10 | Local analysis | Synthesis of method and systems practice; identification of conflicts | Any rendered result. Its scenarios are illustrations |
| Starter behavior, gate discrimination, resize defect | Runs of the SKILL.md starters in headless Chrome with ImageMagick comparison | Observed | Exactly those runs: Linux, one Chrome build, 1280x720 and 390x844, p5.js 1.11.3 for the p5 starter | Other browsers, GPUs, devices, or any other piece |

Three public pages were attached to the analysis as generic process references and were not retrieved: the OpenAI Codex guide to AGENTS.md (`developers.openai.com/codex/guides/agents-md`), GitHub Actions documentation (`docs.github.com/actions`), and the AGENTS.md format site (`agents.md`). After a refresh they could support claims about agent-instruction conventions or CI syntax. They cannot support a choice of visual system, an artistic workflow, or a claim that a sketch runs or looks right. Citing refreshed CI documentation to fix a concrete workflow is a good use. Citing it to defend a palette or a particle model is a category error. Borrowing a general instruction layout for a run card is borderline: label it an analogy and confirm the concept, seed, renderer, and visual-evidence fields survive.

Order of reading for a task: the workflow and default rules always; the philosophy template when intent must be articulated or tested; the pattern menu when two or more families seem plausible or the first idea does not match the motion; then prototype; then refresh an external primary source only when a current platform fact can change the implementation. Opening a document counts only when it changes a decision, confirms one against an explicit rule, or is declined with a reason.

Per material recommendation keep: claim, evidence class, supporting source, source scope, artifact check, uncertainty.

- Good record: "Seeded replay is the default; this piece disables it on purpose for an ephemeral performance; two captured runs confirm the accepted non-repeatability."
- Bad record: "Best practice requires determinism", with links but no scope and no rendered check.
- Good use of the menu: opened to decide between flow and particles for "memory losing cohesion"; particles chosen because lifecycle and decay carry the concept; a low-frequency field kept only as the particles' force model; a monochrome fixed-seed capture tests whether the lifecycle reads without palette.
- Bad use: cites the menu, then implements flow, particles, oscillators, recursive branches, and post-processing with no roles assigned. Or borrows the template's example names and imitates their tone with no behavior behind them.
- Borderline: two families, each with a distinct job. Acceptable only when ablation shows that removing either breaks a named criterion and runtime stays stable.
- Justified adaptation: a static print edition although motion is the default. The user asked for print, recursive growth still shows a temporal process spatially, and export inspection verifies the result.

When two rules seem to conflict:

1. State the exact claims. A difference in examples or emphasis is not a conflict.
2. Compare version, scope, target medium, and whether each is a default, a requirement, or an illustration.
3. Check the user's goal and the project's constraints to see which rule addresses the decision.
4. Choose keep, adapt, decline, or defer, and name the artifact test that could falsify the choice.
5. Keep both observations and the result. A rendered exception can override a default for one piece without rewriting the general rule. Several recurring, verified exceptions are a signal to revise the rule; one unusual artwork is not.

### B. Image generation prompts

| Topic in the skill | Evidence unit | Kind | Supports | Does not support |
| --- | --- | --- | --- | --- |
| Two execution paths, permission gate, specificity policy, priorities, failure and retry guidance, metrics | Analysis digest on image generation prompt patterns, dated 2026-07-10 | Local analysis | Synthesis and conflict identification | Any measured rate. Its editorial priority scores were not measured and are not reproduced |
| Intent rules, save-path precedence, slugs, labeled spec idea, augmentation limits, CLI flags and defaults, API parameters, network note | OpenAI Codex `imagegen` system skill, March 2026 snapshot (Apache-2.0): skill text, prompting, CLI, image-API, network, and sample-prompt references | Third-party tool snapshot, restated | Documented intent at the snapshot | Current model names, sizes, fidelity behavior, sandbox settings, or the built-in tool's behavior on any host |
| CLI dry-run behavior | Dry runs of that snapshot's `image_gen.py` with the commands in SKILL.md B.8 | Observed | Flags parse; payload and output paths print with no key; a `--prompt-file` is wrapped as "Primary request" unless `--no-augment` is passed | Any live API call. None was made |

Not retrieved, named as leads: `platform.openai.com/docs/guides/images` (API parameters), `github.com/openai/codex` (CLI and runtime), and the image model release notes. Date anything taken from them. Model names, size lists, and fidelity behavior go stale quickly.

Validity scope: CLI flags, API parameters, and network or sandbox settings apply only after the user opts into the CLI path. Prompt structure, specificity, invariants, and sample recipes apply to both paths. A fact can be true and still wrong in the path where it is quoted. Do not answer mask-flag questions from the general rules; read `--help`.

### C. Local vision reading

| Topic in the skill | Evidence unit | Kind | Supports | Does not support |
| --- | --- | --- | --- | --- |
| Four rules, six steps, symptoms, configuration keys, host figures | The Hermes agent's local-vision skill for Ollama, restated | Skill snapshot, with figures reported for one host | The procedure, and the figures for a 24 GB M4 Mac mini with `qwen3.5:4b` | The same figures on other hardware, models, or quantizations |
| Manifest, gates, retry order, workload, metrics, scale | Analysis digest on local vision media patterns, dated 2026-07-10 | Local analysis | Synthesis | Measured rates. None exists |
| Staging script behavior | Runs of the SKILL.md script on Linux with ImageMagick: a 2880x1800 PNG with U+202F in its name, a small JPEG, a wide WebP | Observed | Discovery, ASCII staging, resize to 800 px, manifest rows, both gates passing | The `sips` branch (no macOS available), the Pillow branch (not installed), and any Ollama call (no model was run) |

No external corroboration was retrieved. Useful future sources: Ollama documentation for runtime and timeouts, Qwen model cards and release notes for vision-token scaling. The three generic process pages named under mode A are unrelated to vision and must never be cited as vision guidance.

## Evidence Boundary Notes

### A. Algorithmic art

Attach confidence to individual claims. Useful labels:

| Label | Meaning |
| --- | --- |
| `user_requirement_fact` | A goal, surface, constraint, environment, reviewer, or acceptance condition the user or a governing specification stated. If you inferred it, it is inference until confirmed |
| `local_corpus_sourced_fact` | A statement tied to working rules you actually read, bounded by what they say |
| `external_mapping_unrefreshed_note` | A public URL and its intended role are known, but the page was not opened. It can guide research; it cannot support a present-tense claim |
| `external_research_sourced_fact` | A statement tied to a public primary source that was opened, scoped, dated, and summarized accurately |
| `measured_artifact_behavior` | An observation from an identified revision, seed policy, parameters, viewport, temporal state, workload, environment, and method. It supports that scope only |
| `reviewer_judgment_note` | A named reviewer's acceptance, rejection, preference, or uncertainty against named criteria. Accountable judgment, not objective beauty |
| `combined_evidence_inference_note` | A recommendation synthesized from facts, observations, requirements, and judgment. State assumptions, boundaries, alternatives, and what would change it |

A material claim record answers: the claim (one proposition, one scope); its class; source or method; scope (versions, environment, mode, seed and state population, viewport, workload, audience); decision impact; counterevidence or limit; confidence and owner; what would change it.

Good claim chain: the rules recommend seeded behavior when the medium allows -> the user requires the edition to be reproducible for export and handoff -> therefore record random and noise seeds and init order before comparing candidates -> two runs of the identified candidate reach the promised state in the named environment -> the reviewer accepts that state against frozen criteria, with cross-browser pixel identity untested.

Bad chain: "External best practices prove seeded art is always better." It leans on an unopened page, turns a default into a universal aesthetic claim, ignores the user's mode, and has no artifact evidence. Fix it by removing the claim, bounding it to the default, or adding a refreshed source and a task-specific test.

Borderline: "Particles are the right family for memory." The menu supports particles for birth, death, and clustering; it does not establish a universal metaphor. Usable as inference: this reading treats memory as discrete entities that lose cohesion and sparsely return; a monochrome particle prototype is compared with one oscillator alternative; the reviewer decides from renders. If neither communicates loss, the inference is falsified for this brief.

Boundary errors to avoid:

- Labeling a whole paragraph as sourced fact when its last sentence is an unstated inference.
- Treating a mapped URL, a successful HTTP response, a repository example, or a search query as a refreshed fact.
- Reporting a performance target as a result, or one local run as a population guarantee.
- Pairing runtime evidence from one candidate with a capture from another.
- Presenting reviewer agreement as universal taste, or disagreement as noise to average away.
- Keeping a correct label while wording the claim more broadly than the evidence supports.
- Leaving out negative evidence, no-impact refreshes, rejected hypotheses, or known untested environments when they change reuse risk.

Skeptical audit: was the source actually read; does it support this exact scope; is the external record fresh or only inherited; does the measurement identify candidate and environment; is this a target or a result; who owns the artistic judgment; what would falsify or refresh the conclusion? Correct failures by remove, bound, source, measure, or relabel.

Status of this mode's content: workflow, philosophy template, pattern families, examples, and guardrails are the owner's working rules. The three public pages are unrefreshed. The operational scenarios (the memory-drift journey, good, bad, and borderline cases) were not rendered and are illustrations. Guidance on manifests, workload, reliability, observability, recovery, and scale is systems-informed synthesis to be adapted and verified in the implementation at hand. The only measurements are the starter runs listed in the evidence table. Concept selection and aesthetic acceptance remain the user's or the named reviewer's judgment.

Ranking of evidence when it disagrees: method guidance first, then the philosophy and pattern material, then direct artifact evidence for how this piece behaves, and reviewer judgment for aesthetic acceptance.

### B. Image generation prompts

- Label each load-bearing claim as local practice, checked external documentation, or inference, and add the path it is valid for (built-in, CLI, or both).
- Date model-specific facts: `gpt-image-1.5`, the size list, input-fidelity behavior, the 16-image and 50 MB input limits.
- No generation or edit was executed for this skill. The examples describe conduct, not results.
- Not measured: iteration counts, failure frequencies, whether a better spec reduces iterations, the batch crossover count, cost.
- The built-in tool's behavior (default folder, edit of visible images only, no destination argument) is documented for Codex at the snapshot. Check it on your host.

### C. Local vision reading

- Every number carries its host and model: 800 px; about 6,500 versus about 600 vision tokens; 90 to 120 s versus 10 to 20 s; the 120 s default timeout; about 3.4 GB model size; about 35 tokens per second for text. All are for the 24 GB M4 Mac mini with `qwen3.5:4b` (Q4_K_M) and were reported, not re-measured.
- Perishable: model size, token counts, and timing bands change with Ollama releases, model updates, and quantization.
- Not measured: how often each rule is broken, the safe size below which staging can be skipped, the benefit of a third concurrent call, record retention.
- The under-30 s smoke target and the 40 s investigation trigger are working thresholds for that host.
- The direct Ollama call in SKILL.md C.4 follows the standard `/api/generate` shape and was not executed.

## Future Refresh Search Queries

### A. Algorithmic art

Query strings are research instructions, not evidence. Refresh only when a volatile external claim, an observed platform failure, a conflict, a deprecation risk, or a depended-on release can change implementation or verification. Stable creative-method decisions keep using the working rules and rendered experiments.

Broad starting queries (narrow them before use):

| Purpose | Query | Limit |
| --- | --- | --- |
| Find official documentation when the responsible product is unknown | `algorithmic art generation patterns official documentation best practices` | Too broad to support a claim. Replace the theme with the exact renderer, API, behavior, symptom, platform, version |
| Find implementations that reveal vocabulary or techniques | `algorithmic art generation patterns GitHub repository examples` | Repositories vary in authority, maintenance, license, compatibility. Leads only |
| Find change history | `algorithmic art generation patterns changelog release notes migration` | Name the exact dependency and version boundary |

Targeted shape: preferred authority + exact surface + observed symptom or required contract + platform and version.

| Purpose | Query shape | Expected evidence |
| --- | --- | --- |
| Current API contract | `[official owner] [renderer or API] [exact method or behavior] documentation [platform/version]` | Primary documentation confirming behavior, syntax, lifecycle, or environment boundary |
| Deprecation or migration | `[official owner] [dependency] [from version] [to version] migration deprecation release notes` | Release or migration material that changes implementation or retest scope |
| Reproduced runtime symptom | `[official owner] [exact API/renderer] [error or symptom] [browser/device/version] known issue` | A primary issue or note that separates a project defect from a platform limit |
| Rendering or resize contract | `[official owner] [canvas/WebGL/library surface] resize pixel ratio context loss lifecycle documentation` | Current guidance for the failing resize, density, or lifecycle claim; the piece is still retested |
| Export behavior | `[official owner] [export API/format] dimensions timing color assets documentation release notes` | The contract or change record for delivered-file behavior |
| Implementation example | `[exact library and version] [system family or technique] repository example` | A candidate to inspect for structure or terminology |
| Counterevidence | `[current belief or API] limitation deprecation incompatibility known issue` | Evidence that can falsify the preferred solution |

Protocol:

1. State the exact stale or uncertain claim and why it can change a decision now.
2. Reproduce the local symptom or establish the missing contract first, when feasible.
3. Choose the primary authority for that claim. Community material is a lead or example.
4. Run the narrow query and record direct URLs, not result rankings.
5. Capture checked date, version and heading, a narrow summary of support, counterevidence, source status, unresolved scope.
6. Decide: `change`, `confirm`, `no_material_impact`, `narrow_claim`, or `unresolved`.
7. Rerun the local gate the conclusion affects. External documentation cannot prove a local render.
8. Stop when the claim is resolved enough for the decision, or escalate the bounded uncertainty.

- Good: a reproducible mobile resize defect yields the exact renderer, resize behavior, browser, device, and version as search terms; the fix is then captured on the failing viewport.
- Bad: search "algorithmic art best practices", collect tutorials, and override the working rules with no changed claim.
- Borderline: a community workaround fixes one environment but has no official contract. Keep it as a guarded local adaptation with its tested boundary and a refresh trigger.

Source code and issue trackers explain implementation context but can expose unsupported internals. Repository history explains intent, not current external compatibility. Direct experiments establish local behavior strongly and general behavior weakly. Refresh on events (failures, conflicts, API changes, migrations, platform boundaries); schedule periodic refresh only for volatile surfaces the piece depends on. A `no_material_impact` result is worth recording because it prevents repeated research.

### B. Image generation prompts

Prefer the vocabulary of the ecosystem over the literal topic title:

- `OpenAI image API parameters size quality background input_fidelity`
- `GPT image model release notes`
- `image generation prompt structure best practices labeled spec`
- Broad fallbacks: `image generation prompt patterns official documentation best practices`; `image generation prompt patterns GitHub repository examples`; `image generation prompt patterns changelog release notes migration`

Run each once, grade the top results, and rewrite a noisy query. Zero hits for a literal title does not mean the guidance is fresh.

### C. Local vision reading

- `Ollama vision API images parameter timeout documentation` (on each Ollama release)
- `Ollama OpenAI compatibility vision base64 image`
- `Qwen vision-language model card release notes dynamic resolution`
- `vision transformer image token count resolution scaling prefill latency`
- `macOS screenshot filename narrow no-break space U+202F`

Refresh when Ollama, the model, or the quantization changes, and re-run the paired raw and prepared timing afterwards.
