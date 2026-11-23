---
name: tir-algorithmic-art
description: >-
  Seeded algorithmic art with p5.js and HTML5 canvas, deterministic parameter exploration, and interactive visual artifacts. Use when generating procedural or mathematical visuals in code.
---

# TIR Algorithmic Art

Focused skill for deterministic, seeded algorithmic art (p5.js / canvas). Companion reference: [reference.md](reference.md). Related: [tir-image-prompts-and-vision](../tir-image-prompts-and-vision/SKILL.md).

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
