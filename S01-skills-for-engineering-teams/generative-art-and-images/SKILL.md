---
name: generative-art-and-images
description: >-
  Algorithmic art as code (concept and philosophy first, then one seeded generative system in
  p5.js or plain canvas, verified by rendering it), prompts for image generation models
  (labeled spec for a new raster image, an edit with locked invariants, or a batch, and where
  the file is saved), and reading image files with a local Ollama vision model after resizing
  and staging them. Use when the request says "generative art", "creative coding", "p5.js
  sketch", "flow field", "particle system", "manifesto for this piece", "generate an image",
  "hero image", "sprite", "product shot", "edit this photo but keep X", "remove the
  background", "write a prompt for the image model", "describe these screenshots", or "read
  this PNG with the local model"; files .html/.js sketches, .png/.jpg/.webp, .jsonl prompt
  batches. Not for product UI, data charts, explanatory diagrams or explainer pages, extending
  an existing SVG, icon or logo system, 3D scenes, cloud vision APIs, video or PDF extraction,
  or Ollama administration.
---

# Generative Art and Images

This skill covers three jobs that all end in pixels: writing code that draws (algorithmic art), writing the prompt that makes a model draw (image generation), and getting a local vision model to read a picture file reliably. In all three the work is not done until someone has looked at the actual image and checked it against what was asked.

One-line brief for the art mode: turn the concept into a code-driven generative art system with a clear visual idea, a small expressive parameter set, and a clean implementation plan.

## When to use, and when not

Use it when the deliverable is:

- code that produces visual behavior, motion, or emergent composition, and how it looks is part of being correct;
- a bitmap asset made or changed by an image model (photo, illustration, texture, sprite, mockup, transparent cutout), or the prompt for one;
- a description, transcription or answer extracted from image files by a vision model running locally under Ollama.

Requests that should trigger it:

1. "Make a p5.js piece that feels like memory dissolving in a slow current."
2. "I want a generative background for the talk. Same seed should give the same picture."
3. "Generate a hero image for the landing page and put it in `public/img/`."
4. "Edit this product photo: swap the backdrop, keep the product exactly as it is."
5. "Go through the screenshots in `~/Desktop/bug-1432/` with the local vision model and tell me what each shows."

Requests that should not:

1. "Build the settings page with a dark-mode toggle." This is product UI. Use `react-frontend`.
2. "Draw the architecture of this service as a diagram" or "make an explainer page for this module." Use `visual-explainers`.
3. "Add one more icon to our SVG icon set." Edit the vector source directly. A generated bitmap will not match the set.

Also route elsewhere when factual data encoding, photo retouching by hand, product ergonomics, or 3D camera and spatial behavior decides correctness.

## Pick the mode

| The user wants | Mode | First decision |
| --- | --- | --- |
| Code that draws, animates, or reacts | A. Algorithmic art | static, animated, interactive, or seed-driven |
| A picture that a model paints, or a change to one | B. Image generation prompt | generate or edit; one asset or many; preview or project asset |
| To know what is in existing image files, using the local model | C. Local vision reading | one file or a batch; which order |

The modes combine. A common chain is A or B to produce an image, then C to read it back as a check (for example, reading rendered label text). Each mode keeps its own rules when combined.

If a deterministic, exact visual is wanted (a precise diagram, a logo that must match, text that must be pixel-true), do not use mode B. Edit the repo's own vector file, build it in HTML/CSS/canvas (mode A or a front-end skill), or decline raster generation and say why.

## Workflow

1. Route. Pick the mode from the table. If the request mixes modes, split it and name the hand-off between them.
2. Collect before producing. Mode A: one concept sentence. Mode B: exact text, constraints, input images and their roles, destination. Mode C: folder, order, question to ask of each image.
3. Follow the numbered workflow of that mode (sections below).
4. Produce the smallest thing that can be looked at: a monochrome prototype, one render, one timed smoke analysis.
5. Inspect the real output. Open the capture, read the rendered text, check the timing. A passing command is not an inspected image.
6. Change one thing, then look again. Keep the baseline and what you changed.
7. Deliver in the mode's output contract, with the identity of what was accepted: seed and parameters, final prompt and path, or staging manifest.

## Rules for all three modes

- Look at pixels. Build output, a returned file path, or a model's fluent answer does not prove the image is right.
- One targeted change per iteration. Changing several things at once destroys the ability to say what helped.
- Do not add what was not asked. Extra layers, extra props, extra polish, and guessed file names are the same mistake in three forms.
- Record identity next to every result: for art, code revision, seed, parameters, viewport, time; for generation, mode, final prompt, saved path; for vision, original name, staged path, dimensions, seconds.
- A retry must change the failing condition. Repeating the same call unchanged is allowed once, only to test whether the failure was transient.
- Numbers in this skill that come from one machine carry that machine's name. Do not quote them as your own measurement.
- Aesthetic acceptance is a judgment by a named reviewer against written criteria. Mechanics can be tested; taste cannot be automated.

## Mode A: Algorithmic art

Use this mode when the deliverable is code that produces visual behavior, motion, or emergent composition. Keep the workflow tight: concept -> system -> parameter surface -> implementation.

### A.1 Workflow

1. Distill the conceptual seed.
   - Identify the feeling, metaphor, motion, or mathematical idea the piece should express.
   - Decide whether the work is static, animated, interactive, or seed-driven.
   - Write it as one sentence that names the behavior, the constraint, the variation, and the effect on the viewer.
   - If the user gave no concept, propose a few distinct seeds and let one be chosen.
2. Pick one dominant visual system.
   - Choose the smallest fitting family from the pattern menu (A.3).
   - Prefer one strong behavior over a pile of loosely related effects.
   - Name one plausible alternative you rejected and why. If you cannot choose, build two minimal monochrome prototypes and compare them. Do not build several polished versions or a large shell.
3. Define the control surface.
   - Pick a small set of expressive parameters such as seed, palette, density, decay, noise scale, velocity, or spawn rate.
   - Give each a safe range, a baseline value, and a visible, describable effect.
   - Make randomness reproducible when the medium allows it.
4. Translate the concept into implementation.
   - Default to p5.js or plain canvas for fast iteration.
   - Move to shaders, WebGL, or heavier stacks only when the effect genuinely depends on them.
   - Separate update, render, and input logic. Also give initialization, reset, and resize their own clear place.
5. Verify the piece as software.
   - Check resize behavior, seed behavior, frame stability, and readability of the code.
   - Capture and look at representative states: start, a typical mid-state, a long-run state, and every target viewport.
   - Add comments only where they clarify the system or the controls.

Reverse course when a prototype shows the concept does not come through in that system. Change the system or the concept sentence, not the decoration.

### A.2 Default rules

- Prefer living motion over static ornament.
- Keep the parameter count small but meaningful.
- Make the same seed produce the same result unless the user asks for pure chaos.
- Use color deliberately; the motion system should still be interesting in monochrome.
- Make failure graceful: if the browser slows down, degrade density before adding complexity.
- The visual system must make the concept perceptible before palette, texture, glow, interface, or polish are added.
- Keep state bounded: cap spawning, expire or cull what is off screen or dead, and reuse objects.
- Reproducibility lets people collaborate and compare. It says nothing about whether the piece is good.
- Once representative behavior exists, do one accessibility and readability pass: a pause or reduced-motion path where motion could bother a viewer, visible structure, enough contrast, nothing overlapping on the target surfaces.

### A.3 Generative pattern menu

Choose one primary family before coding.

| Family | Use when the piece should feel like or be about | Good knobs |
| --- | --- | --- |
| Flow fields | wind, currents, migration, invisible force | noise scale, particle count, step size, trail decay |
| Particle systems | birth, motion, death, clustering, swarm behavior | emitter count, lifetime, drag, spawn rate |
| Oscillator systems | rhythm, interference, breathing, wave superposition | frequency, phase offset, amplitude, coupling |
| Cellular or rule systems | large structure evolving from local rules | neighborhood rule, mutation rate, update cadence |
| Packing and growth | crowding, expansion, territory, pressure | growth rate, collision margin, spawn strategy |
| Recursive geometry | branching, self-similarity, architectural order | depth, angle variance, shrink factor |
| Noise-driven terrain or ink | geological, cloudy, watery, organic surfaces | octave count, persistence, contour threshold |

Selection rule: pick the family that matches the motion logic first. Palette, line style, and layering should support that motion, not rescue a weak system.

The menu gives cues and candidate knobs. It does not prove a family fits. When the motion logic is ambiguous, compare the plausible families in a render.

### A.4 Algorithmic philosophy template

Use this when the user wants the art system explained as an intentional movement rather than a pile of implementation notes, or wants the concept as a short manifesto or design note. Write it before the code. It is the "philosophy first" half of the job.

```markdown
### Movement Name
<one short name with texture, e.g. `Organic Turbulence`, `Quiet Interference`, `Luminous Drift`>

### Concept Seed
<the emotional or mathematical premise in one sentence>
e.g. "This piece treats memory like particles losing cohesion in a slow current."
e.g. "This piece treats traffic as a pressure field that folds light into lanes."

### Core Principles
<3 to 5 bullets>
- what moves
- what constrains it
- what introduces variation
- what makes each run unique
- what the viewer should feel

### Translation To Code
| philosophy idea | code move |
| --- | --- |
| gentle drift | low-frequency noise field |
| memory decay | alpha fade plus sparse respawn |
| tension release | spring easing after threshold |
| hidden rhythm | phased oscillators or periodic emitters |

### Parameter Surface
<keep it compact>
- `seed`
- `palette`
- `density`
- `tempo`
- `noise_scale`
- `trail_decay`

### Failure Check
If the philosophy can only be felt after a paragraph of explanation, the system is too abstract
or too weak. Strengthen the behavior, not the prose.
```

The movement names and the table rows are examples of the format, not a house style. Check every "code move" in a render.

### A.5 Preflight (answer before writing code)

```text
Mode:            static | animated | interactive | seed-driven
Where it is seen: <browser page / export PNG / installation>, target viewports: <e.g. 1280x720, 390x844>
Concept:         <one sentence: behavior, constraint, variation, viewer effect>
Primary system:  <family>      Rejected alternative: <family, one-line reason>
Controls:        <name: range, baseline, visible effect> x 3-7
Renderer:        <existing project stack | p5.js | plain canvas | escalation + measured reason>
Replay policy:   same seed same result | curated single seed | no replay (user asked for chaos)
States to check: start, <typical time>, <long-run time>, interaction
Runtime envelope: <device class, what counts as too slow; set per project>
Criteria:        <3-6 things a reviewer can see, e.g. slow coherent drift, legible decay>
Reviewer:        <who accepts>     Stop when: <condition>
```

### A.6 Starter: plain canvas, no dependencies

A complete single file. It has a seeded control surface, separate init / update / render / resize / input, a density fallback, and a `?steps=N` mode that renders exactly N steps and stops, so two captures can be compared.

```html
<!doctype html>
<meta charset="utf-8">
<title>sketch</title>
<style>html,body{margin:0;height:100%;background:#000}canvas{display:block;width:100vw;height:100vh}</style>
<canvas id="c"></canvas>
<script>
// ---- control surface: few knobs, each with a safe range and a visible effect ----
const q = new URLSearchParams(location.search);
const P = {
  seed:       Number(q.get('seed') ?? 1842),      // same seed -> same piece
  density:    clamp(Number(q.get('density') ?? 900), 50, 4000),    // particle count
  flowScale:  clamp(Number(q.get('flow') ?? 1.6), 0.2, 8),         // field frequency
  drag:       clamp(Number(q.get('drag') ?? 0.92), 0.5, 0.999),    // velocity kept per step
  lifetime:   clamp(Number(q.get('life') ?? 420), 30, 5000),       // steps before respawn
  trailDecay: clamp(Number(q.get('decay') ?? 0.04), 0.005, 1),     // 1 = no trails
  ink:        q.get('ink') ?? '#e8e6df',                           // monochrome first
};
function clamp(v, lo, hi) { return Number.isFinite(v) ? Math.min(hi, Math.max(lo, v)) : lo; }

// ---- seeded randomness: two streams so init order cannot disturb the field ----
function mulberry32(a) {
  return () => { a |= 0; a = a + 0x6D2B79F5 | 0; let t = Math.imul(a ^ a >>> 15, 1 | a);
    t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t; return ((t ^ t >>> 14) >>> 0) / 4294967296; };
}
function makeNoise(seed) {              // small value noise on a hashed lattice
  const r = mulberry32(seed), g = Float32Array.from({ length: 4096 }, r);
  const at = (x, y) => g[((x & 63) << 6) | (y & 63)];
  const s = t => t * t * (3 - 2 * t);
  return (x, y) => { const xi = Math.floor(x), yi = Math.floor(y), u = s(x - xi), v = s(y - yi);
    const a = at(xi, yi), b = at(xi + 1, yi), c = at(xi, yi + 1), d = at(xi + 1, yi + 1);
    return a + (b - a) * u + (c - a) * v + (a - b - c + d) * u * v; };
}

// ---- state: normalized 0..1 coordinates, so resize never touches the simulation ----
const S = { rand: null, noise: null, parts: [], step: 0, active: 0, paused: false };
function spawn(p) { p.x = S.rand(); p.y = S.rand(); p.vx = p.vy = 0; p.age = Math.floor(S.rand() * P.lifetime); return p; }
function init() {
  S.rand = mulberry32(P.seed); S.noise = makeNoise(P.seed ^ 0x9E3779B9);
  S.parts = Array.from({ length: P.density }, () => spawn({}));
  S.step = 0; S.active = P.density;
}

// ---- update: fixed step, no drawing, no DOM ----
function update() {
  const t = S.step * 0.002;
  for (let i = 0; i < S.active; i++) {
    const p = S.parts[i];
    const a = S.noise(p.x * P.flowScale + t, p.y * P.flowScale) * Math.PI * 4;
    p.vx = p.vx * P.drag + Math.cos(a) * 0.00012;
    p.vy = p.vy * P.drag + Math.sin(a) * 0.00012;
    p.px = p.x; p.py = p.y; p.x += p.vx; p.y += p.vy;
    if (++p.age > P.lifetime || p.x < 0 || p.x > 1 || p.y < 0 || p.y > 1) { spawn(p); p.px = p.x; p.py = p.y; }
  }
  S.step++;
}

// ---- render: reads state, never mutates it ----
const canvas = document.getElementById('c'), ctx = canvas.getContext('2d');
let W = 0, H = 0;
function render() {
  ctx.globalAlpha = P.trailDecay; ctx.fillStyle = '#000'; ctx.fillRect(0, 0, W, H);
  ctx.globalAlpha = 0.7; ctx.strokeStyle = P.ink; ctx.lineWidth = 1; ctx.beginPath();
  for (let i = 0; i < S.active; i++) { const p = S.parts[i]; ctx.moveTo(p.px * W, p.py * H); ctx.lineTo(p.x * W, p.y * H); }
  ctx.stroke();
}

// ---- resize policy: re-fit the buffer, clear trails, keep the simulation ----
function resize() {
  const dpr = Math.min(window.devicePixelRatio || 1, 2);
  W = canvas.width = Math.round(innerWidth * dpr); H = canvas.height = Math.round(innerHeight * dpr);
  ctx.fillStyle = '#000'; ctx.fillRect(0, 0, W, H);
}

// ---- loop: fixed simulation steps; shed density before anything else ----
const STEP_MS = 1000 / 60, BUDGET_MS = 24;   // BUDGET_MS is a project choice, not a standard
let last = performance.now(), acc = 0, slow = 0;
function frame(now) {
  const dt = Math.min(now - last, 250); last = now;
  if (!S.paused) {
    acc += dt; let n = 0;
    while (acc >= STEP_MS && n++ < 4) { update(); acc -= STEP_MS; }
    render();
    slow = dt > BUDGET_MS ? slow + 1 : 0;
    if (slow > 30 && S.active > 50) { S.active = Math.floor(S.active * 0.85); slow = 0;
      console.info('density reduced to', S.active); }
  }
  requestAnimationFrame(frame);
}

// ---- input: only changes parameters or lifecycle, never draws ----
// ?steps=N renders exactly N steps and stops: a reproducible still for capture and comparison
const fixed = Number(q.get('steps')) || 0;
function still() { init(); resize(); for (let i = 0; i < fixed; i++) { update(); render(); }
  document.title = `done seed=${P.seed} step=${S.step} ${W}x${H}`; }
addEventListener('resize', () => fixed ? still() : resize());   // a still is replayed, a live run keeps going
addEventListener('keydown', e => {
  if (e.key === ' ') S.paused = !S.paused;
  if (e.key === 'r') { P.seed = (P.seed + 1) | 0; fixed ? still() : (init(), resize()); }
  if (e.key === 's') { const a = document.createElement('a'); a.download = `sketch-seed${P.seed}-step${S.step}.png`;
    a.href = canvas.toDataURL('image/png'); a.click(); }
});

if (fixed) still(); else { init(); resize(); requestAnimationFrame(frame); }
</script>
```

Controls by URL: `?seed=1842&density=900&flow=1.6&drag=0.92&life=420&decay=0.04&ink=%23e8e6df`. Keys: space pauses, `r` advances the seed, `s` saves a PNG named with seed and step.

Notes on the choices in this file:

- Two random streams (one for placement, one for the field) so a change in spawn order does not change the field.
- Positions are stored in 0..1 and scaled at draw time. Resize never touches the simulation. The aspect ratio stretches the field; if that is wrong for the piece, recompose deliberately instead.
- In `?steps=N` mode a resize replays the still. Without that, a resize handler that clears trails leaves a blank frame, and a headless capture shows nothing. This was found by looking at the capture, not by reading the code.
- `BUDGET_MS` is a project choice. This skill supplies no frame-rate threshold.

### A.7 Starter: p5.js

Same structure with p5's own seeded functions. Load p5 from a local copy or a CDN.

```html
<!doctype html>
<meta charset="utf-8">
<style>html,body{margin:0;background:#000}canvas{display:block}</style>
<script src="p5.min.js"></script>
<script>
const q = new URLSearchParams(location.search);
const P = { seed: Number(q.get('seed') ?? 1842), density: 600, noiseScale: 1.6, trailDecay: 10, steps: Number(q.get('steps')) || 0 };
let parts = [], stepCount = 0;

function initState() {                      // every random draw happens here, in a fixed order
  randomSeed(P.seed); noiseSeed(P.seed);
  parts = Array.from({ length: P.density }, () => ({ x: random(), y: random(), px: 0, py: 0 }));
  stepCount = 0; background(0);
}
function updateState() {                    // no drawing
  for (const p of parts) {
    const a = noise(p.x * P.noiseScale, p.y * P.noiseScale, stepCount * 0.002) * TAU * 2;
    p.px = p.x; p.py = p.y; p.x += cos(a) * 0.0015; p.y += sin(a) * 0.0015;
    if (p.x < 0 || p.x > 1 || p.y < 0 || p.y > 1) { p.x = p.px = random(); p.y = p.py = random(); }
  }
  stepCount++;
}
function renderState() {                    // no state changes
  noStroke(); fill(0, P.trailDecay); rect(0, 0, width, height);
  stroke(232, 230, 223, 180);
  for (const p of parts) line(p.px * width, p.py * height, p.x * width, p.y * height);
}
function still() { initState(); for (let i = 0; i < P.steps; i++) { updateState(); renderState(); } }

function setup() { createCanvas(windowWidth, windowHeight); pixelDensity(1); initState(); if (P.steps) { noLoop(); still(); } }
function draw() { if (!P.steps) { updateState(); renderState(); } }
function windowResized() { resizeCanvas(windowWidth, windowHeight); P.steps ? still() : background(0); }
function keyPressed() {
  if (key === 'r') { P.seed++; P.steps ? still() : initState(); }
  if (key === 's') saveCanvas(`sketch-seed${P.seed}-step${stepCount}`, 'png');
}
</script>
```

`randomSeed` and `noiseSeed` are both needed: `random()` and `noise()` are separate streams in p5.

### A.8 Run card (one per hypothesis)

```yaml
goal: <what the user asked for>
concept: <one sentence>
mode: animated            # static | animated | interactive | seed-driven
primary_system: particle lifecycle
rejected: oscillators     # and why, in implementation notes
controls: {seed: 1842, density: 900, flow_scale: 1.6, drag: 0.92, lifetime: 420, trail_decay: 0.04, palette: mono}
renderer: plain canvas
criteria_version: 1
criteria: [slow coherent drift, legible decay, structure holds in monochrome, intentional empty space, framed on 1280x720 and 390x844]
candidate:
  code_revision: <commit or file hash>
  seeds: {random: 1842, noise: derived}
  init_order: placement then field
  viewport: 1280x720
  temporal_state: step 600
  environment: <browser and version, device>
  captures: [cap-1280-step600.png, cap-390-step600.png]
status: draft             # draft | candidate | accepted | archived_study
verdict: <pass | scoped_failure | external_shared_state_failure> + reviewer + reason
export_qa: <regenerated from this card: yes/no>
```

`draft` is loose exploration. `candidate` means identity and criteria are frozen enough to attribute a change. `accepted` means software and visual gates pass and the piece can be regenerated from the card. `archived_study` is a rejected or deferred idea kept for what it taught. One card holds one falsifiable hypothesis.

### A.9 Verification

Two kinds of proof are needed, and neither replaces the other. Software evidence covers execution, replay, resize, and the declared workload. Visual evidence covers whether the intended behavior is visible, framed, and meets the named criteria. A passing build cannot prove meaningful pixels. A screenshot cannot prove temporal stability, interaction, or reproducibility.

Cheap gate for a throwaway sketch: it runs, you looked at it, the seed policy holds, it resizes (or the format is declared fixed), and you can name the dominant mechanism.

Runnable gates for the starter above (headless Chrome and ImageMagick; swap in the project's own launch and capture commands when it has them, and never invent commands for a project you have not inspected):

```bash
F="file://$PWD/sketch.html"
shot() { google-chrome --headless=new --disable-gpu --hide-scrollbars --window-size="$2" --screenshot="$PWD/$1" "$F?$3" >/dev/null 2>&1; }

# 1. Seed policy: same seed twice, then a different seed
shot a.png 1280,720 "seed=1842&steps=600"
shot b.png 1280,720 "seed=1842&steps=600"
shot c.png 1280,720 "seed=7&steps=600"
compare -metric AE a.png b.png null: ; echo     # expect 0 differing pixels
compare -metric AE a.png c.png null: ; echo     # expect a large number

# 2. Not blank: brightest pixel must be well above the background
identify -format "%f %wx%h max=%[fx:maxima]\n" a.png   # max near 0 means an empty canvas

# 3. Viewports and temporal states
shot mobile.png 390,844  "seed=1842&steps=600"
shot early.png  1280,720 "seed=1842&steps=30"
shot long.png   1280,720 "seed=1842&steps=5000"

# 4. Console: no uncaught errors, and the still finished
google-chrome --headless=new --disable-gpu --enable-logging=stderr --dump-dom "$F?seed=1842&steps=600" 2>&1 \
  | grep -E "<title>|Uncaught|CONSOLE"
```

Then open every capture and look at it. On the starter, gate 1 gave 0 differing pixels for the same seed and about 160,000 for a different seed at 1280x720 in one headless Chrome on one Linux machine. That shows the gate discriminates; it is not a property of your piece.

Exact pixel identity can fail across browsers, GPUs, fonts and floating-point paths. When it does, decide whether bounded visual equivalence is acceptable and write that down.

At a milestone or before final acceptance, add one perturbation: maximum density, a resize while running, a reset, or removing a layer (ablation). Passing only in the prettiest state is selection bias.

### A.10 Guardrails

- Do not mistake extra layers for depth.
- Do not ship unseeded randomness when repeatability matters.
- Do not turn a visual-art request into generic frontend scaffolding.
- If the user actually wants a polished application shell, bring in `frontend-design` or `playground` as a companion (in this library: `react-frontend` for the shell, `visual-explainers` for an interactive playground page), but keep this skill focused on the art system itself.
- When art lives inside a site, tool, or game, the art core owns concept, seed, and render contract. The parent owns navigation, content, accessibility, deployment, and game rules.
- When a failure appears, name its class first: concept, system, control, runtime, presentation, or evidence. Then change the smallest upstream cause. "It looks flat, add noise" is not a diagnosis.

## Mode B: Prompts for image generation models

Use this mode for raster generation and editing, and for deciding how the request is executed. A reliable prompt is a labeled spec plus discipline about specificity: structure what the user said, and do not add creative content they did not imply.

### B.1 Two execution paths

| Path | What it is | When |
| --- | --- | --- |
| Built-in tool (default) | The host agent's own image tool. In Codex this is `image_gen`; it needs no API key. | Every normal generate or edit request. |
| CLI (explicit request only) | A script that calls the image API directly. In Codex this is `image_gen.py` from the OpenAI imagegen skill, usually at `$CODEX_HOME/skills/imagegen/scripts/image_gen.py`. It needs `OPENAI_API_KEY` and network access. | Only after the user asks for the CLI path. |

Rules:

- The choice is gated by permission, not by capability. Never switch to the CLI on your own after the built-in tool fails. Say that the CLI exists and what it needs, and continue only if the user accepts.
- CLI-only controls (quality, input fidelity, masks, output format, output paths, batch files, network settings) do not describe the built-in tool. Do not put them in a built-in-mode answer.
- Do not write a one-off SDK runner, and do not modify the CLI script. If it lacks something, ask.
- Never ask for an API key in chat. The user sets it in their own shell and confirms.
- Do not answer size, model-name, or fidelity questions from memory. Those facts change with model releases. Read the CLI's `--help` or current documentation and date what you find.

This skill bundles no image CLI. If the host has none, the built-in tool is the only path.

### B.2 Three decisions before the prompt

1. Intent: generate or edit.
   - The user wants parts of an existing image preserved while something changes: edit.
   - Images are supplied only for style, composition, mood, or subject guidance: generate with references.
   - No images, or unclear: generate.
2. Strategy: one asset, several variants of one prompt, or many different assets.
   - Built-in path: one call per asset or variant.
   - CLI path: `--n` makes variants of one prompt; `generate-batch` runs many prompts from a JSONL file.
3. Destination: preview only, or an asset the project will use. This sets how much spec, inspection, and file handling is needed.

Intent and strategy are separate questions. Most misfires come from answering only one of them. Also classify the use case with one slug from B.4 and keep it the same across iterations.

### B.3 Workflow

1. Choose the path: built-in unless the user asked for the CLI.
2. Decide intent, strategy, and destination (B.2).
3. Collect inputs up front: the request in the user's words, exact text to render (verbatim), must-keep and must-avoid constraints, and every input image.
4. Label each input image by index and role: edit target, reference (style / composition / mood / subject), or insert for compositing.
5. For a built-in edit of a file on disk, load the file into the conversation first so the tool can see it. Do not promise editing by arbitrary file path in built-in mode.
6. If the user asked for a raster asset (photo, illustration, sprite, banner), make one. Do not substitute an SVG or HTML placeholder. If the asset must match existing vector assets in the repo, edit those instead and leave this mode.
7. Write the labeled spec (B.5). Apply the specificity policy (B.6). If a missing detail blocks success, ask one question. Otherwise proceed.
8. Generate. In CLI mode, run `--dry-run` first.
9. Inspect the output against the spec: subject, style, composition, every rendered word against the quoted text, constraints, and for edits the invariants compared with the original image.
10. Iterate with one targeted change. Restate the invariants and critical constraints every time.
11. Place the file by the save-path rules (B.7).
12. For batches, keep only the selected finals in the workspace unless the user asked to keep the rest.
13. Report the final saved path, the final prompt, the path used (built-in or CLI), and what you added that the user did not say.

### B.4 Use-case slugs

Generate:

| Slug | For |
| --- | --- |
| `photorealistic-natural` | believable photos with real texture and natural light |
| `product-mockup` | product and packaging shots, catalog and merchandise images |
| `ui-mockup` | app or web screens and wireframes; state the fidelity wanted |
| `infographic-diagram` | structured layouts with labels and text |
| `logo-brand` | logo and mark exploration |
| `illustration-story` | comics, picture-book art, narrative scenes |
| `stylized-concept` | style-led concept art and stylized or 3D-look renders |
| `historical-scene` | scenes that must match a place and period |

Edit:

| Slug | For |
| --- | --- |
| `text-localization` | replace or translate text inside an image, layout kept |
| `identity-preserve` | change clothing or setting while a person stays the same |
| `precise-object-edit` | remove or replace one named element |
| `lighting-weather` | change time of day, season, or atmosphere only |
| `background-extraction` | cutout on a transparent or clean background |
| `style-transfer` | apply a reference's style to a different subject |
| `compositing` | merge several images with matched light and perspective |
| `sketch-to-render` | turn a drawing into a finished render |

### B.5 The labeled spec

Short labeled lines, not a paragraph. Use only the lines that help. Add another labeled line if it makes the request clearer. Order: setting, subject, details, constraints, intended use.

```text
Use case: <slug from B.4>
Used for: <where the image goes: landing hero, game icon, blog header; preview or project asset>
Request: <the user's request, in their words>
Inputs: <Image 1: edit target | Image 2: style reference | Image 3: insert>   (only if images are supplied)
Setting: <environment or backdrop>
Subject: <main subject>
Medium: <photo | illustration | 3D look | wireframe ...>
Framing: <wide / close / top-down; where the subject sits; empty space only if the layout needs it>
Light and mood: <...>
Palette: <...>
Surfaces: <materials and textures>
Exact text: "<verbatim text>" + typeface style, size, colour, placement
Keep unchanged: <for edits: everything that must survive>
Change only: <for edits: the one thing that changes>
Must not appear: <logos, watermark, extra text, extra people ...>
Added by agent: <every line above that the user did not state, or "nothing">
```

Notes:

- "Setting" is the visual scene. It is not the CLI's `background` option, which controls transparency.
- "Used for" and "Inputs" are prompt text only. No CLI flag exists for them.
- Quote the exact text. For an unusual word, spell it letter by letter and require verbatim rendering with no extra characters.
- For photorealism, use camera language: lens feel, viewpoint, depth of field, light direction.
- Do not choose left or right placement unless the user or the surrounding layout decides it.
- For compositing, say how the images relate: which element from which image goes where.
- Keep the "Added by agent" line in your record even if you strip it from the text sent to the model. It keeps user requirements and your additions apart.
- A spec written after the render is not the spec that produced it. Save the spec before generating.

Generate example (generic request, so light augmentation is allowed and listed):

```text
Use case: product-mockup
Used for: landing page hero, project asset -> public/img/hero-teapot.png
Request: a hero image of our cast-iron teapot
Subject: one cast-iron teapot, matte black
Medium: clean studio product photo
Framing: wide; teapot off-centre with open space for a headline
Light and mood: soft diffuse studio light, calm
Must not appear: text, logos, watermark, cups or other props
Added by agent: studio medium, wide framing with open space, soft light
```

Edit example (invariants locked):

```text
Use case: precise-object-edit
Used for: shop listing photo, project asset -> assets/listing/backpack-sand.png
Inputs: Image 1: edit target
Request: replace the grey backdrop with a pale sand studio sweep
Change only: the backdrop
Keep unchanged: the backpack, its edges, straps, stitching, label text, colour, shadows on the product, camera angle, crop
Must not appear: new objects, text, watermark
Added by agent: nothing
```

Two-line preview spec (only for an explicitly informal preview; label it as a preview):

```text
Preview only. Use case: stylized-concept. Request: three moods for a foggy harbour at dawn.
Must not appear: text, logos, watermark.
```

### B.6 Specificity policy

Treat the user's specificity as something to conserve. Restructure their intent; do not add creative mass.

| The request is | Do | Do not |
| --- | --- | --- |
| Specific and detailed | Normalize it into the labeled lines. Keep every stated requirement. | Add props, polish, brands, slogans, palettes, or story that were not implied. |
| Generic | Add a little, only where it clearly improves the result, and list it under "Added by agent". | Treat a fully written sample recipe as the normal amount to add. |
| An edit | Put invariant preservation ahead of any improvement. | "Improve" anything outside the requested change. |
| Hard to classify | Write the full spec, pilot one render before a batch, or ask what polish level is wanted. | Guess and run a batch. |

Additions that are allowed for a generic request: framing and composition hints, intended-use or polish level, practical layout guidance, and enough scene concreteness to support what was asked.

Additions that are never allowed: characters, objects, or props that were not implied; brand names, slogans, palettes, or story beats that were not implied; a left or right placement with no layout reason.

### B.7 Where the file goes

In Codex the built-in tool writes under `$CODEX_HOME/generated_images/`. Other hosts differ; find the default output location before you report a path. Do not rely on a destination argument of the built-in tool. Generate first, then move or copy.

Precedence:

1. The user named a destination: put the selected output there.
2. The image is for the current project: copy the final selected image into the workspace before finishing, and update the code or document that refers to it.
3. Preview or brainstorming only: show it inline. The file may stay where the tool put it. Say so.

A project asset left only in the tool's default folder is a delivery failure. Do not overwrite an existing asset unless replacement was asked for. Write a versioned sibling such as `hero-v2.png` or `item-icon-edited.png`.

### B.8 CLI path (only after the user asks for it)

Facts below describe the Codex imagegen CLI as of its March 2026 snapshot. Confirm with `python "$IMAGE_GEN" --help` before relying on any of them.

```bash
export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
export IMAGE_GEN="$CODEX_HOME/skills/imagegen/scripts/image_gen.py"

# 1. Always dry-run first: prints the payload and output path, needs no key, no network, no cost
python "$IMAGE_GEN" generate --prompt "Matte black cast-iron teapot, studio product photo" \
  --use-case product-mockup --composition "wide, open space for a headline" \
  --constraints "no text, no logos, no watermark" \
  --out output/imagegen/hero-teapot.png --dry-run

# 2. Live generate (needs OPENAI_API_KEY and network)
python "$IMAGE_GEN" generate --prompt "Matte black cast-iron teapot, studio product photo" \
  --size 1536x1024 --out output/imagegen/hero-teapot.png

# 3. Edit with invariants restated in the prompt
python "$IMAGE_GEN" edit --image backpack.png \
  --prompt "Change only the backdrop to a pale sand studio sweep; keep the backpack unchanged" \
  --input-fidelity high --out output/imagegen/backpack-sand.png

# 4. Many different prompts: one JSONL manifest, bounded concurrency
mkdir -p tmp/imagegen output/imagegen/icons
cat > tmp/imagegen/icons.jsonl <<'EOF'
{"prompt":"Round wooden shield, painted game icon, centered, clear silhouette","use_case":"stylized-concept","constraints":"no text; no watermark","out":"shield.png"}
{"prompt":"Corked blue potion bottle, painted game icon, centered, clear silhouette","use_case":"stylized-concept","constraints":"no text; no watermark","out":"potion.png"}
EOF
python "$IMAGE_GEN" generate-batch --input tmp/imagegen/icons.jsonl --out-dir output/imagegen/icons --concurrency 5
rm -f tmp/imagegen/icons.jsonl
```

CLI facts worth knowing (same date caveat):

- Subcommands: `generate`, `edit`, `generate-batch`. `generate-batch` requires `--out-dir`; default concurrency is 5.
- Defaults: model `gpt-image-1.5`, size `1024x1024`, quality `auto`, format `png`. Sizes: `1024x1024`, `1536x1024`, `1024x1536`, `auto`.
- `--quality low|medium|high|auto` works everywhere. `--input-fidelity low|high` and `--mask` are edit-only. One mask, PNG preferred. Masking is guided by the prompt; exact shapes are not guaranteed.
- Repeat `--image` for multi-image edits. Order matters; refer to images by index in the prompt.
- A rerun fails if the target exists unless `--force` is passed. A transparent background needs `png` or `webp`.
- Keep scratch files in `tmp/imagegen/` and delete them; keep finals in `output/imagegen/`.
- The CLI builds its own labeled prompt from `--use-case`, `--scene`, `--subject`, `--style`, `--composition`, `--lighting`, `--palette`, `--materials`, `--text`, `--constraints`, and `--negative`. When the prompt is already a complete labeled spec, pass `--no-augment`.
- Dependencies: the `openai` package (`uv pip install openai`); Pillow only for downscaled copies.
- Larger size and higher quality cost more time and money; high input fidelity uses more input tokens. No prices are given here.
- If the sandbox blocks the network, silencing approval prompts does not enable network access. That is a separate setting. Lowering either raises risk in an untrusted repository.

## Mode C: Reading images with a local vision model

Use this mode before any local, file-based analysis with an Ollama vision model, especially a folder of macOS screenshots. Use it before the first call, not after the first timeout. Reliability here is decided on the path from disk to model: inputs prepared, resources bounded, configuration verified.

The documented setup: model `qwen3.5:4b` (about 3.4 GB) under Ollama at `http://localhost:11434`, on a 24 GB M4 Mac mini, called through the Hermes agent's `vision_analyze` tool. Every number in this section was reported for that host and model. It has not been re-measured elsewhere.

### C.1 Four rules

1. Always resize first. Target 800 px on the longest edge. A full-resolution Retina screenshot (10 MB or more, 2880x1800 or larger) costs about 6,500 vision tokens, and the vision transformer's prefill grows with the square of the patch count, so the call runs 90 to 120 s and often hits the 120 s default timeout. At 800 px the same image costs about 600 tokens and takes about 10 to 20 s.
2. Discover file names with code. Use Python `os.listdir()` and `os.path.join()`. Never type or paste a name from `ls` output. macOS screenshot names contain U+202F (narrow no-break space) before AM/PM. It looks like a space, and the error it causes looks like a missing file.
3. Stage clean copies. Copy to plain ASCII names under `/tmp` and pass only those paths to the model. The staged name must end in an image extension the tool recognises.
4. Bound concurrency. Two analyses at a time is the default. Three is the upper limit, for small images on a host you have measured. More causes GPU contention, out-of-memory errors, or extreme slowdown.

Staging without resizing still times out. A staged path does not prove a resized image; check both.

### C.2 Workflow

1. Discover the files with Python (handles Unicode names).
2. Sort: by modification time when chronology matters (name order can scramble it), by name when alphabetical order is wanted.
3. Copy to `/tmp` under clean names and print each original name with `repr()` at copy time.
4. Resize every staged copy to 800 px on the longest edge.
5. Run one timed smoke analysis on one staged image.
6. Analyze the rest, at most two at a time, passing only staged paths. Key every answer to its original file.

A single image may skip the sort. A batch must never end with a call on a raw path.

### C.3 Staging script

Complete and copyable. It discovers, sorts oldest first, copies, resizes with `sips` on macOS (ImageMagick or Pillow elsewhere), and writes a manifest.

```python
#!/usr/bin/env python3
"""Stage images for a local vision model: discover, sort, copy to ASCII names, resize, record."""
import json, os, shutil, subprocess, sys, time

SRC = sys.argv[1]                                   # folder to read; never type file names by hand
LIMIT = int(sys.argv[2]) if len(sys.argv) > 2 else 0  # 0 = all
MAX_EDGE = int(os.environ.get("MAX_EDGE", "800"))   # drop to 600 for a dense image that still times out
STAGE = os.environ.get("STAGE", "/tmp/vision_stage")
EXTS = (".png", ".jpg", ".jpeg", ".webp")
FORCE_PNG = os.environ.get("FORCE_PNG") == "1"      # convert (not rename) when the tool only accepts .png

def resize(path):
    if shutil.which("sips"):                        # macOS; in place, safe to rerun
        subprocess.run(["sips", "-Z", str(MAX_EDGE), path, "--out", path], check=True, capture_output=True)
    elif shutil.which("magick") or shutil.which("convert"):   # ImageMagick; ">" = only shrink
        tool = shutil.which("magick") or shutil.which("convert")
        subprocess.run([tool, path, "-resize", f"{MAX_EDGE}x{MAX_EDGE}>", path], check=True)
    else:
        from PIL import Image                       # Pillow fallback
        im = Image.open(path); im.thumbnail((MAX_EDGE, MAX_EDGE)); im.save(path)

def size(path):
    if shutil.which("sips"):
        out = subprocess.run(["sips", "-g", "pixelWidth", "-g", "pixelHeight", path],
                             check=True, capture_output=True, text=True).stdout.split()
        return int(out[out.index("pixelWidth:") + 1]), int(out[out.index("pixelHeight:") + 1])
    if shutil.which("identify"):
        w, h = subprocess.run(["identify", "-format", "%w %h", path + "[0]"],
                              check=True, capture_output=True, text=True).stdout.split()
        return int(w), int(h)
    from PIL import Image
    return Image.open(path).size

os.makedirs(STAGE, exist_ok=True)
for old in os.listdir(STAGE):                       # a rerun must not leave stale copies behind
    if old.startswith("vision_"):
        os.remove(os.path.join(STAGE, old))
names = [n for n in os.listdir(SRC) if n.lower().endswith(EXTS)]
names.sort(key=lambda n: os.path.getmtime(os.path.join(SRC, n)))   # oldest first; sort by name if order is alphabetical
if LIMIT:
    names = names[:LIMIT]
with open(os.path.join(STAGE, "manifest.jsonl"), "w") as manifest:
    for i, name in enumerate(names):
        ext = os.path.splitext(name)[1].lower()
        staged = os.path.join(STAGE, f"vision_{i:03d}{ext}")       # keep the true extension
        shutil.copy2(os.path.join(SRC, name), staged)
        if FORCE_PNG and ext != ".png":
            png = os.path.splitext(staged)[0] + ".png"
            if shutil.which("sips"):
                subprocess.run(["sips", "-s", "format", "png", staged, "--out", png], check=True, capture_output=True)
            else:
                subprocess.run([shutil.which("magick") or shutil.which("convert"), staged, png], check=True)
            os.remove(staged); staged = png
        resize(staged)
        w, h = size(staged)
        row = {"index": i, "original_dir": SRC, "original_name_repr": repr(name), "staged": staged,
               "width": w, "height": h, "staged_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
               "seconds": None, "result": None}
        manifest.write(json.dumps(row) + "\n")
        print(f"{i}: {name!r} -> {staged} {w}x{h}")
```

```bash
python3 stage_images.py ~/Desktop/bug-1432        # all images, oldest first
python3 stage_images.py ~/Desktop/bug-1432 3      # the three oldest
MAX_EDGE=600 python3 stage_images.py ./dense 1    # second attempt for a dense image
FORCE_PNG=1 python3 stage_images.py ./mixed       # convert to PNG when the tool rejects other types
```

One-off equivalents: `sips -Z 800 in.png --out /tmp/vision_input.png` (macOS), `magick in.png -resize '800x800>' /tmp/vision_input.png` (ImageMagick). When input and output are the same file, `sips -Z` changes it in place and running it again is harmless. Copying the original over the staged file again after resizing silently undoes the resize.

### C.4 Calling the model

Through an agent tool: pass each `/tmp/vision_stage/vision_NNN.ext` path to the vision tool (`vision_analyze` in Hermes) with the question.

Directly against Ollama, when no tool wraps it (standard Ollama HTTP API; check it against your installed version):

```bash
python3 - /tmp/vision_stage/vision_000.png "Describe what this screenshot shows. Quote any error text exactly." <<'EOF'
import base64, json, sys, time, urllib.request
path, question = sys.argv[1], sys.argv[2]
body = {"model": "qwen3.5:4b", "prompt": question, "stream": False,
        "images": [base64.b64encode(open(path, "rb").read()).decode()]}
req = urllib.request.Request("http://localhost:11434/api/generate", json.dumps(body).encode(),
                             {"Content-Type": "application/json"})
t = time.time()
print(json.loads(urllib.request.urlopen(req, timeout=120).read())["response"])
print(f"{time.time() - t:.1f} s", file=sys.stderr)
EOF
```

Write the seconds and a pointer to the answer back into the manifest row for that image.

### C.5 Configuration check

In the Hermes setup two places set the vision route, and they must agree:

| Place | Keys |
| --- | --- |
| `~/.hermes/config.yaml`, section `auxiliary.vision` | `provider` (custom), `model` (`qwen3.5:4b`), `base_url` (`http://localhost:11434/v1`), `api_key` (any placeholder), `timeout` (120) |
| `~/.hermes/.env` | `AUXILIARY_VISION_PROVIDER`, `AUXILIARY_VISION_MODEL`, `AUXILIARY_VISION_BASE_URL`, `AUXILIARY_VISION_API_KEY` |

`.env` overrides `config.yaml`. If routing is slow or wrong, check `.env` first. A wrong model usually gives no error, only slow or poor answers that still look plausible, so a resized image that is still slow is a configuration signal.

```bash
curl -s http://localhost:11434/api/tags | python3 -c "import json,sys; print([m['name'] for m in json.load(sys.stdin)['models']])"
grep -n '^AUXILIARY_VISION_' ~/.hermes/.env | sed 's/\(API_KEY=\).*/\1<redacted>/'
grep -n -A6 '^ *vision:' ~/.hermes/config.yaml
```

### C.6 Symptoms and fixes

| Symptom | Likely cause | Fix |
| --- | --- | --- |
| Timeout at about 120 s | Image too large | Resize to 800 px; if it still times out, 600 px; only then raise the timeout |
| "No such file or directory" or "Invalid image source" for a file you can see | U+202F or other Unicode in a typed name | Rediscover with `os.listdir`, stage an ASCII copy |
| GPU out of memory or extreme slowdown | Too many calls at once | Two at a time, or one |
| Tool will not open the staged file | Staged path lacks a recognised image extension | Keep the real extension, or convert to PNG while staging |
| Slow or poor answers, no error | Wrong model routed | Compare `.env` `AUXILIARY_VISION_*` with `config.yaml`; `.env` wins |

Retry rule: change the failing condition first. Timeout: resize to 600 px. Path error: rediscover and restage. Out of memory: fewer or serial calls. Raising the timeout to 180 to 240 s (`auxiliary.vision.timeout: 240`) is for a legitimately dense image after the smaller size has been tried. Three identical retries are wrong, and hammering the GPU makes contention worse. When no local hardware is available, use a cloud vision service under its own rules.

Reduced ceremony is acceptable only for one file that you have verified is small (check dimensions and file size; do not judge by eye) and that has a hand-chosen ASCII name. Record that you skipped staging. The safe threshold for skipping is not measured.

## Output contract

Mode A, in this order when the task is substantial:

1. `Concept`: the one-sentence seed, and the philosophy note if one was asked for.
2. `Visual System`: the family, why it carries the concept, the alternative rejected.
3. `Parameter Plan`: each control with range, baseline, visible effect; the seed policy.
4. `Implementation Notes`: renderer and why, update / render / input split, resize policy, density fallback, what was verified and what was not (states, viewports, environment).
5. `Code`: complete and runnable.

For a small sketch, code plus two lines on concept and controls is enough.

Mode B:

- the final saved path (workspace path for a project asset; "preview only, left at tool default" otherwise);
- the final prompt, as sent;
- the path used: built-in tool or CLI;
- the labeled spec with the "Added by agent" line;
- for edits, the invariants and the result of comparing final against original;
- inspection findings: text read back word for word, any constraint violations and how they were fixed;
- iteration count and what changed at each step.

Mode C:

- the staging manifest: original directory and `repr()` name, staged path, post-resize dimensions, seconds per call, pointer to the answer;
- the answers, each keyed to its original file;
- the model and effective configuration used, verbatim error text if any, and any deviation (for example a raw path used for a verified-small file).

## Quality gates

Mode A: the commands in A.9, then eyes on every capture.

Mode B:

```bash
# CLI path only: payload and output path look right before spending a call
# (--no-augment sends a complete labeled spec as written; without it the file is wrapped as one "Primary request")
python "$IMAGE_GEN" generate --prompt-file tmp/imagegen/spec.txt --no-augment --out output/imagegen/hero.png --dry-run

# The asset is in the workspace, and is what it claims to be
test -f public/img/hero-teapot.png && identify -format "%f %m %wx%h\n" public/img/hero-teapot.png

# The delivery note does not point at the tool's private folder
grep -n -E 'CODEX_HOME|generated_images' delivery-note.md && echo "FAIL: stranded asset" || echo "ok"

# Every invariant from the spec is still present in the last prompt of an edit chain
grep -n -i -E 'keep unchanged|change only' tmp/imagegen/last-prompt.txt || echo "FAIL: invariants dropped"
```

Human gate, never skipped: open the image and check subject, style, composition, each rendered word against the quoted text, constraints, and for edits the original against the final (not just against the previous iteration). For a quick preview a lighter checklist is fine. Brand-sensitive work deserves a second reviewer. Label-critical work can add text extraction through mode C.

Mode C, before every batch:

```bash
# Staged names are ASCII (grep prints nothing and exits 1 when clean)
ls /tmp/vision_stage | LC_ALL=C grep -n '[^ -~]'

# Every staged image is under /tmp, ASCII-named, and at most 800 px on the longest edge
python3 - <<'EOF'
import json
rows = [json.loads(l) for l in open('/tmp/vision_stage/manifest.jsonl')]
bad = [r for r in rows if max(r['width'], r['height']) > 800
       or not r['staged'].startswith('/tmp/') or not r['staged'].isascii()]
print('staged', len(rows), 'violations', len(bad)); raise SystemExit(1 if bad else 0)
EOF

# One timed smoke analysis (C.4). On the documented host the target is under 30 s.
```

To test the gates themselves, seed a folder with one oversized image and one file with U+202F in its name and confirm both are caught and fixed.

## Where the guidance pulls two ways

Both positions are kept. The selector says which applies.

| Topic | Position 1 | Position 2 | What selects |
| --- | --- | --- | --- |
| Motion | Prefer living motion over static ornament | A static piece is a valid deliverable; it needs its declared final state plus resize and export evidence | The mode the user asked for. With no preference stated, motion. |
| Renderer | Default to p5.js or plain canvas | Use the project's existing stack first | Whether the piece lands in an existing codebase. Standalone: p5.js or canvas. |
| Replay | Same seed, same result | No replay is acceptable for a live, ephemeral run; or bounded visual equivalence across machines | The user asked for pure chaos, or the reliability profile is ephemeral, or environments differ and the difference was accepted in writing. |
| Vision concurrency | 2 to 3 at once | At most 2 | Default 2. Use 3 only for small images on a host where you measured it. |
| Vision timeout | Config can be raised to 180 to 240 s if needed | Raise only as a last resort | Resize to 600 px first. Raise only for a dense image that still fails. |
| Vision ceremony | Always apply all four rules | One verified-small ASCII-named file may skip staging | Batch or macOS-originated files: always. Single verified file: may skip, recorded. |
| Spec size | Full labeled spec | Two-line preview spec | Destination: project asset gets the full spec; explicit informal preview may be short and labeled as such. |
| Exploration | One change per iteration | A round of several variants at once | Label the round as exploration, keep only what taught something, then converge with one change at a time. |

## Anti-patterns

Mode A:

- Layer pile-up: particles, waves, branches, glow and UI compete and nothing carries the concept. Remove layers until one system does. (A maximal piece is fine when every mechanism has a named, demonstrated role.)
- Random novelty loop: seed, code, controls, palette and viewport all change between looks.
- Update, render and input tangled together, so resize resets the piece and replay depends on call order.
- Uninspected output: the build passes while the canvas is blank, clipped, or in the wrong state.
- One screenshot offered as proof of motion, decay, or stability.
- Unbounded density or state: particles that never expire, spawn without a cap.
- Resize corruption: crop, stretch, blank regions, or a silent reseed.
- Generic front-end takeover: the shell is polished before any representative art exists.

Mode B:

- Silent CLI fallback after a built-in failure.
- Padding a detailed prompt with unimplied polish, props, or brands.
- Dropping "keep X unchanged" somewhere in an edit chain. The loss accumulates.
- Leaving a project asset in the tool's default folder.
- Rewriting the whole prompt twelve times for one image instead of making targeted changes.
- Quoting CLI controls as if the built-in tool had them.
- Accepting without reading the rendered text.

Mode C:

- Passing the original folder path or a full-resolution image to the model.
- Typing or pasting a file name.
- Retrying unchanged after a timeout. That spends another full timeout window on the same failure.
- Eight calls at once on one GPU.
- Renaming a file to `.png` without converting it.
- Trusting plausible output without checking which model answered.

## Bundled scripts

This skill bundles no script files. The plain-canvas starter (A.6), the p5.js starter (A.7), and the staging script (C.3) are inline; copy them into the working directory as `sketch.html` and `stage_images.py`. The image-generation CLI in B.8 belongs to the host's image tooling and is not part of this skill. More depth on every mode is in [reference.md](reference.md): the full failure tables, workload and retry guidance, reliability profiles, scale boundaries, worked examples, and evidence limits. Nothing in this file depends on it.

## Self-check before handing back

- [ ] The mode was chosen on purpose, and anything that belongs to another skill was routed there.
- [ ] Mode A: one concept sentence exists; one dominant system is named with a rejected alternative; controls are few, bounded, and each visibly does something.
- [ ] Mode A: same seed gives the same result (or the exception is stated); update, render, and input are separate; resize was tested at every target size; density drops before anything else when slow.
- [ ] Mode A: captures at start, mid, and long-run states were opened and looked at; the piece still reads in monochrome.
- [ ] Mode A: the answer follows Concept, Visual System, Parameter Plan, Implementation Notes, Code.
- [ ] Mode B: built-in path unless the user asked for the CLI; intent, strategy, and destination were each decided.
- [ ] Mode B: the spec was saved before generating; every addition is listed; exact text is quoted; invariants are restated in every edit iteration.
- [ ] Mode B: the image was opened and its text read; an edit was compared with the original; the project asset is in the workspace and the path, prompt, and mode are reported.
- [ ] Mode C: names came from `os.listdir`; every call used an ASCII path under `/tmp`; every staged image is at most 800 px (or 600 px on retry); at most two calls ran at once.
- [ ] Mode C: one timed smoke call ran first; the manifest keys every answer to its original; the effective model configuration is known.
- [ ] No number from another machine is presented as measured here.
