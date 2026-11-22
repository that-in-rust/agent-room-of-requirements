---
name: visual-explainers
description: Explains code or ideas visually as a single-file HTML explainer page with an act-based narrative, a strict-ASCII terminal page or diagram, a plain-English ELI5 note about AI-native engineering, or an interactive single-file playground, and checks that the result renders. Use when the request says "explain how X works", "help me understand Y", "ELI5", "visual explainer", "make an elegant HTML explainer", "build a visual journey", "onboard someone on this subsystem", "docs that are not boring", "ASCII diagram", "plain text diagram", "make a playground or explorer for X", or when the output is an .html explainer under .prd/ELI5/, a .txt file, a fenced text block, a commit message or a runbook that needs a diagram, or when the bundled create_elegant_explainer_html.py or check_ascii_diagram_quality.py is to be run. Not for exhaustive API or lookup documentation, recommendation or approval memos, production frontends or dashboards with auth or live state, Mermaid or image diagrams, slides, or benchmark and security claims that need their own governing document.
---

# Visual Explainers

## Purpose

This skill turns source code, notes or a dense idea into an explanation a named reader can follow in one pass, in one of four forms: a single-file HTML page, a strict-ASCII page, a plain-English ELI5 note, or an interactive playground. It also carries the checks that the result is true to its sources and actually renders on the surface it was promised for.

## When to use it

- Someone asks how a subsystem, protocol, pipeline or method works and wants more than prose.
- A new teammate must be onboarded on a bounded subject.
- Dense AI-native engineering notes (four-word naming, TDD-first, context engineering, sub-agents) must be made simple.
- A diagram must survive a terminal, a raw Markdown block, a log, a commit message or a `.txt` file.
- The reader must change variables, see a consequence, compare options and hand a decision back.

Do not use it when:

- The reader needs exhaustive lookup. Write reference documentation.
- The document must argue for a decision. Write a memo.
- The page needs auth, live or server state, or irreversible actions. Build a tested application.
- The question is two lines long. Answer in chat with a short ELI5.
- Exact behaviour, commands, security policy or benchmark numbers govern. Point to the governing artifact, using the handoff steps under "Rules for every mode". An overview may introduce it and must not replace it.

Requests that should trigger this skill:

1. "Explain how the MongoDB source connector actually works. Make it a page a new hire can open."
2. "Give me an ASCII diagram of the async request path that I can paste into the runbook."
3. "ELI5 our context-engineering notes for the product team."
4. "Build a playground so I can try card spacing and shadow options and copy the result back."
5. "Turn these notes and source files into a polished standalone explainer HTML page."

Requests that should not trigger it:

1. "Document every endpoint of the billing API." (reference documentation)
2. "Write the recommendation memo for choosing Postgres over Mongo." (argument, not explanation)
3. "Build the admin dashboard for live queue depth." (production frontend)

## Choose the mode

| Signal in the request | Mode | Deliverable |
| --- | --- | --- |
| Narrative order and visual relations matter; a browser is available; subsystem scale | HTML explainer | one `.html` file, inline CSS and JS |
| Terminal, `.txt`, raw Markdown, log, runbook, commit message; must diff and copy cleanly | ASCII page or figure | printable ASCII inside a `text` fence or a `.txt` file |
| Dense notes, beginner or non-engineer reader, small question | ELI5 note | short Markdown |
| Reversible variables interact; feedback changes judgment; a decision must be exported | Playground | one `.html` file with state, preview and export |

Modes combine. ELI5 owns the plain-English teaching arc. ASCII owns monospaced layout. HTML owns staged browser reading. A playground owns exploration before a decision. Give each artifact a distinct job and name which one is authoritative for facts that change.

The sources disagree on visual richness. Keep both positions and select by audience:

- Novice onboarding, long page: apply the full teaching set (metaphor for each concept, at least three component types, comparison where alternatives exist, summary table).
- Expert or short page: one dominant visual direction, a metaphor only where it helps, one or two code excerpts, little motion.
- In both cases every component must answer a question that prose answers worse. Monotony bores. A component gallery distracts.

## Workflow

1. Name the reader and the outcome. Write one reader, their starting knowledge, and what they must be able to predict or decide afterwards.
2. Pick the mode from the table above. Say so if another medium fits better.
3. Read the sources before writing a word of explanation. Find the main loop, lifecycle or handshake first. List actors, state, boundaries, failure classes and the exact terms the code uses. Record file paths and line numbers. Delegate exploration to sub-agents if useful, but keep narrative and writing in one place. Do not skip this because the code seems familiar.
4. Write a claim ledger. For each major claim note the source span, what it establishes, and whether it is a source fact, a source-reported measurement, an inference or an analogy. Mark gaps as unknown. Never invent state, guarantees, failure classes or ownership.
5. Outline before layout. HTML: 5 to 8 acts with the mechanism by Act II. ASCII: page system, canvas width, one job per section. ELI5: one-sentence idea, then three layers. Playground: the decision, then the state.
6. Check the outline. Each act or section answers one question. Split any that carries two new ideas. Repairs are cheap here.
7. Build from the bundled scaffold or skeleton for the mode. Adapt it. Do not start from scratch when the scaffold exists.
8. Remove scaffold residue: placeholder text, generic "Path A / Path B" labels, unused acts, sample failures.
9. Run the mechanical gates for the mode (below).
10. Open the result on its real surface. Read it as the reader would. Check narrow width, keyboard, reduced motion and script failure for HTML; raw paste into each promised surface for ASCII.
11. Check fidelity and comprehension separately. A reviewer checks claims against sources. A representative reader restates the mechanism and applies it to a new case. If no reader is available, record comprehension as `not_evaluated`.
12. Hand off: path, sources used, commands run, what passed, what was not evaluated, and what change in the source should trigger a refresh.

A failed gate is a failed stage. Go back to the stage that caused it: an ungrounded claim returns to the code, a dense act returns to the outline, a broken metaphor is replaced and not softened.

## Rules for every mode

Evidence:

- Extract the explanation from evidence. Every major claim maps to a source or is visibly marked as inference or unknown.
- Use the exact nouns and verbs from the source where precision matters. Define each once in plain words.
- Numbers from the source stay attributed to the source. "67% faster" and "90% fewer bugs" are claims from source notes until measured in the target project.
- If sources are incomplete or conflict, say so on the page.
- A source's role depends on the claim, not on the file. Canonical governs a defined decision. Supporting adds detail. Legacy informs history and not current behaviour. A duplicate is the same source twice and is not independent corroboration. A conflicting source pauses the affected recommendation until its owner resolves it.
- Do not infer authority or obsolescence from a file's location or name.
- After a source changes, reopen only the claims, examples and fixtures that depend on it, then check the whole artifact for coherence.

Teaching:

- One new idea per act, section or screenful.
- Concrete before abstract. Show `SELECT * FROM users WHERE id > 42` before "tracking offset pattern".
- Open with the problem or mystery, not a definition. A familiar audience may start at the mechanism.
- The mystery opening assumes the subject has a real problem-and-solution shape: there is a problem the thing exists to solve. A purely arbitrary convention has no problem to dramatise, so do not force acts onto it. A config-file explainer is the borderline case: find the tension the configuration resolves before writing Act I.
- A metaphor lowers the entry cost and is followed at once by the exact mechanics. State where it breaks. Removing it must leave a complete explanation.
- Explain why, not only what. Calm, factual tone. Do not oversell.
- End with one sentence the reader can repeat, for example "Poll. Transform. Deliver. Checkpoint. Repeat."

Reusing an existing explanation:

- Adopt it when the reader, decision, sources, consequence and example all match. Adapt it when the mechanism fits but audience, authority or stakes differ. Pause or route when evidence is absent or conflicting, or exact behaviour governs.
- State the cost of error. Record the conditions, the rejected alternative, the reversal trigger (changed source, failed reader check, new audience, higher consequence) and, later, the correction or refresh cost actually observed.
- Progressive disclosure can put an overview before a specification. It cannot turn qualitative guidance into an exact contract.

Checking:

- Automated checks prove characters, widths, structure and residue. They do not prove truth or comprehension.
- A presentation defect that hides a caveat or changes apparent order or causality is a correctness defect.
- Any change to the file invalidates earlier render evidence for the changed parts.

Measuring (only when a pass rate, a timing or a metric is reported):

- Before collecting, define the task, the artifact version or hash, the environment, the population and sample, the rubric, the severity levels and how reviewer disagreement is handled.
- Report the numerator and denominator, the misses, the disagreement and the uncertainty. A small pass count is not a reliability percentage.
- A critical misroute overrides a good aggregate.
- Never change the denominator, count duplicate cases, coach answers, or drop slow or failing runs after the fact. Exclusions are declared in advance.
- Fixture results and live results answer different questions. Do not pool them without saying so.
- A timed run is one observation. It does not show that the explanation caused the result.
- For an ELI5 note, useful measures are time to first correct action, time to verified action, irrelevant files or searches opened, substantive corrections, confidence calibration, runtime, reviewer decision time, trend over repeated use and downstream rework. Each has blind spots. Keep reviewer time apart from tool latency. The leading indicator is a correct route, with its rationale, on an unseen case.
- "Completion increased" means nothing without the task, versions, population, window, baseline, guardrail, owner and evidence location. Compare only compatible tasks.
- Carry each claim's status (source fact, source-reported, inference, unknown) into prompts, slides and other copies.

Handing off (when exact behaviour, commands, policy or numbers govern and another artifact owns them):

1. State the unresolved decision in one sentence and the consequence of getting it wrong.
2. Name the capability that governs it: implementation, testing, prompt construction, state persistence, current documentation, evidence adjudication or release operation.
3. Preflight the destination: its stated purpose, its authority and its verification gate. "Nearest" means fit of scope and verification, not a similar filename.
4. Carry the context forward and say what result returns control or completes the task.

Handoff payload: reader and prerequisites, starting state, unresolved decision, consequence, sources loaded, settled claims, evidence labels, open question, destination, expected gate, and the return or completion condition. If no adequate authority exists, keep the bounded explanation and record the gap. Do not pick a plausible file to hide it.

## HTML explainer (act-based, single file)

### Scaffold

Two templates are bundled. Pick one and use its class names.

| Template | Fill method | Extra components |
| --- | --- | --- |
| `assets/elegant-explainer-template.html` | `scripts/create_elegant_explainer_html.py` writes seven scaffold acts | numbered `.metaphor-mark`, null-checked navigation, two accent colours |
| `assets/template.html` | copy, then replace `{{TITLE}}`, `{{CATEGORY}}`, `{{SUBJECT}}`, `{{SUBTITLE}}` by hand and add acts | syntax span classes, `.animated-flow`, `.branch`, `.tag-yes` / `.tag-no`, five accent colours |

Both define hero, acts, dividers, scroll reveal, dot navigation, metaphor cards, flow steps, insight callouts, code blocks, diagram blocks, `.vs-grid` comparison cards, `.options-grid` option cards and `.comparison-table`.

```bash
python3 scripts/create_elegant_explainer_html.py \
  --output .prd/ELI5/index.html \
  --hero-label "Connector Explainer" \
  --hero-title "How the Source Connector Actually Works" \
  --hero-subtitle "A visual journey through the polling loop, state, and failure handling." \
  --source core/connectors/sources/mongodb_source/src/lib.rs \
  --source core/connectors/sdk/src/lib.rs
```

Other flags: `--page-title`, `--footer-label`, `--force`. The script refuses to overwrite an existing file without `--force`, creates parent directories, and HTML-escapes its inputs. It must stay next to `assets/` because it loads the template from `../assets/`.

Output location: `.prd/ELI5/` in the project root, `index.html` for one topic or `<topic-name>.html` for several. This is one author's convention. Follow the project's own location if it has one, and keep pages findable.

If the request points at an existing explainer, inspect it first and keep its density, pacing and tone unless a redesign is asked for.

### Act outline

Use 5 to 8 acts. The seven-act default:

| Act | Job | Typical component |
| --- | --- | --- |
| 1 | Problem or mystery in human terms: "You have data at rest. You need it in motion." | hero, one metaphor card |
| 2 | Core loop or data path, in the code's verbs | numbered flow, 4 to 6 steps |
| 3 | Modes, variants or implementations | side-by-side cards |
| 4 | State and safety: what is remembered, when it is persisted, what a crash or retry does | small diagram or branch view |
| 5 | Architecture and extension points: what the author implements, what the runtime owns | diagram, two cards |
| 6 | Failure modes and tradeoffs: transient vs fatal, correctness vs performance | cards with real examples |
| 7 | Big picture and one-line takeaway | summary table, insight callout |

Follow the concept arc, not the file tree. Keep comparisons asymmetric when reality is. A decision tree or transformation may replace the loop when that is the real mechanism.

### Components

Markup that works in both templates:

```html
<section class="act" id="act1">
  <div class="reveal">
    <div class="act-label">Act I</div>
    <h2>Section title</h2>
    <p>Short paragraph.</p>

    <div class="flow">
      <div class="flow-step">
        <div class="flow-num">1</div>
        <div class="flow-content"><h4>Step</h4><p>What happens and why, with <code>names</code>.</p></div>
      </div>
    </div>

    <div class="insight">
      <div class="insight-label">Key Insight</div>
      <p>The one thing to keep from this act.</p>
    </div>

    <div class="diagram">read() --> tentative state --> commit | discard</div>

    <div class="code-block">
      <div class="code-header">Rust: poll loop</div>
      <pre>// one short excerpt, not a file</pre>
    </div>

    <div class="options-grid">
      <div class="option-card"><code>json</code><h4>Payload format</h4><p>One card per finite choice.</p></div>
    </div>

    <table class="comparison-table">
      <tr><th>Dimension</th><th>Polling</th><th>Change stream</th><th>Why it matters</th></tr>
      <tr><td>State</td><td>last seen id</td><td>resume token</td><td>decides where a restart resumes</td></tr>
    </table>
  </div>
</section>
<div class="divider"><hr></div>
```

Use option cards for finite lists such as payload formats, offset types or configuration modes. Put the summary table near the end.

Template-specific class names:

| Component | `elegant-explainer-template.html` | `template.html` |
| --- | --- | --- |
| Metaphor card | `.metaphor` > `.metaphor-mark` (a number) + `.metaphor-body` | `.metaphor` > `.metaphor-icon` + `.metaphor-body` |
| Comparison card | `.vs-grid` > `.vs-card.accent-primary` / `.accent-secondary` | `.vs-grid` > `.vs-card.accent-1` / `.accent-2` / `.accent-brand` / `.accent-purple` / `.accent-pink` |
| Code header dot | none | `.code-dot.c1` / `.c2` / `.rust` / `.brand` |
| Syntax spans in `pre` | none | `.kw .fn .str .cmt .type .num` |
| Diagram spans | none | `.node .arrow .label-1 .label-2 .label-brand .dim` |
| Table tags | none | `.tag-yes` / `.tag-no` |
| Navigation | `.story-nav` > `.nav-dot[data-target]` | `.nav-dots` > `.nav-dot[data-target]` |

Older examples use topic classes such as `vs-card pg`, `vs-card mongo` or diagram spans `.str` and `.fn`. Neither bundled template defines them. Use the names above or add matching CSS. The metaphor icon in `template.html` is often an emoji; use a number or word where the project rejects emoji.

Component rules: one idea per metaphor card; one or two code excerpts per page; every diagram must make sense as plain text; one `.nav-dot` per section and each `data-target` must match a section `id`; the footer lists key source files; add inline attribution for surprising or disputed points.

### Harden the scaffold

Observed in both bundled templates: `.reveal` content starts at `opacity: 0` and appears only when the script runs; there is no `prefers-reduced-motion` rule; navigation dots are `div` elements that the keyboard cannot reach; fonts load from Google Fonts with system fallbacks. In `template.html` a dot whose target is missing throws on click.

Apply this to the generated or copied file before writing content. It was run against both bundled templates:

```bash
f=.prd/ELI5/index.html
sed -i -E \
  -e 's/^  \.reveal \{/  .js .reveal {/' \
  -e 's/^  \.reveal\.visible \{/  .js .reveal.visible {/' \
  -e 's|<head>|<head>\n<script>document.documentElement.classList.add("js");</script>|' \
  -e 's|<div class="nav-dot( active)?" data-target="([^"]+)">(<span class="nav-tooltip">[^<]*</span>)</div>|<a class="nav-dot\1" href="#\2" data-target="\2">\3</a>|' \
  "$f"
python3 - "$f" <<'PY'
import sys
path = sys.argv[1]
text = open(path, encoding="utf-8").read()
css = """  .nav-dot { display: block; }
  .nav-dot:focus-visible { outline: 2px solid currentColor; outline-offset: 3px; }
  @media (prefers-reduced-motion: reduce) {
    html { scroll-behavior: auto; }
    .js .reveal { opacity: 1; transform: none; transition: none; }
    * { animation: none !important; }
  }
</style>"""
assert text.count("</style>") == 1, "expected exactly one </style>"
open(path, "w", encoding="utf-8").write(text.replace("</style>", css))
PY
```

What it does: content is hidden for the reveal effect only after a script has started; each navigation dot becomes a link that works without the script and can take keyboard focus; motion stops when the reader asks for reduced motion. If the page script fails after the first line has run, content can still stay hidden, so keep the script small and check the console. `sed -i` is GNU syntax; on macOS use `sed -i ''`. Any dot added later must use the link form:

```html
<a class="nav-dot" href="#act1" data-target="act1"><span class="nav-tooltip">The Problem</span></a>
```

If the page must work offline or must not call a third party, delete the `@import url("https://fonts.googleapis.com/...")` line. The font stacks fall back to system fonts.

## ASCII pages and diagrams

Compose a terminal page, not one great diagram. Height is cheap. Width is expensive.

### Choose the page system first

| Page system | Use when |
| --- | --- |
| Tall Variation Gallery | many small variations stacked like a field guide |
| Glossary Plus Panels | 3 to 6 concepts that need a name, then a repeated visual row |
| Layered Walkthrough | intuition first, mechanism second |
| Two-Column Compare | exactly two options with the same categories on both sides |
| Mechanism Trace | one sequence carries the explanation, with short side notes |

### Then the local figure, by the reader's question

| Reader's question | Figure |
| --- | --- |
| What exists and how is it connected? | System Map |
| What happens next? | Flow Diagram |
| Who exchanges what, in what order? | Sequence Diagram |
| What contains what? | Tree Diagram |
| How do peers differ? | Comparison Grid |
| How does input become output? | Mechanism Trace |
| Several concepts as a gallery | Card Strip |
| Exactly two alternatives | Two-Column Compare |

If one diagram tries to do two of these jobs, split it. If the subject needs curves or dense graph topology, recommend a non-ASCII format.

### Canvas and grid

- Canvas: 84 columns for most pages, 72 for compact terminal output, 96 only for comparison-heavy pages that survive the target surface.
- Prose 52 to 64 columns. Side notes 18 to 28. Gutters 2 to 4 spaces. These are defaults, not measurements.
- One left margin. One card width per repeated row. One glossary separator column. One side-note column.
- One blank line between local blocks, two between major sections on tall pages. `---` only for real section breaks.
- Each 20 to 40 line stretch is one screenful with one job: define, compare, trace or summarise.
- If one line breaks the grid, fix the wording before changing the layout. Stack before you widen.

### Drawing rules

- Printable ASCII only. Spaces, never tabs. No trailing spaces. No Unicode box-drawing, emoji or decoration.
- One vocabulary: boxes from `+ - |`; arrows `-->`, `<--`, `|`, `v`, `^`; branches from `|`, `+`, `\`.
- Nouns in boxes, actions on arrows. Labels, not paragraphs. 3 to 7 primary nodes per figure.
- Keep the main path straight. Go top-down when width is tight.
- Prose sets up the figure and stays outside it. Do not narrate the figure afterwards.
- A side note is shorter than the line it annotates. Legend only when symbols would confuse.
- Do not centre content at random. Centring is for a headline.

### Page skeleton

Order: title, one short setup paragraph, sections, legend if needed, short reading notes. Wrap in a `text` fence when embedding in Markdown. This page passes the validator at 84 columns:

```text
How A Queued Request Finishes

A request is accepted first and finished later. Read top to
bottom: each section adds one idea.

Level 1: The Essence

The API answers before the work is done.

+---------+      +---------+      +---------+
| Client  | ---> | API     | ---> | Queue   |
+---------+      +---------+      +---------+

---
Level 2: The Parts

API    = accepts and validates the request
Queue  = holds work until a worker is free
Worker = does the work and records the result

+-------------+  +-------------+  +-------------+
| API         |  | Queue       |  | Worker      |
|             |  |             |  |             |
| validates   |  | holds work  |  | does work   |
| replies 202 |  | keeps order |  | writes row  |
+-------------+  +-------------+  +-------------+

---
Level 3: The Write Path

Step 1: validate(request)         <- reject bad input early
    |
    v
Step 2: enqueue(job)              <- reply 202 after this
    |
    v
Step 3: worker runs job           <- may be retried
    |
    v
Step 4: persist(result)           <- durable from here

Reading notes

- A 202 reply means accepted, not finished.
- Look at the queue first when work seems stuck.
```

Sequence skeleton (actors on one line, time moves down, short labels):

```text
Client        API         Worker       Database
  |            |            |             |
  |-- request->|            |             |
  |            |-- enqueue->|             |
  |            |            |-- write --->|
  |            |<-- ack ----|             |
  |<- 202 -----|            |             |
```

More skeletons are in [reference.md](reference.md) under Theme Specific Artifact.

## ELI5 notes (AI-native engineering and other dense ideas)

Default readers: a curious 12-year-old, a non-engineer teammate, or a new developer who wants the idea before the jargon. Name one of them and one next decision.

Steps:

1. Find the core claim: what is this really saying?
2. Give the main idea in one sentence.
3. Explain in three layers: one-sentence takeaway, short story version, concrete rules or examples.
4. Use one everyday analogy per major concept and say where it stops fitting.
5. Give one concrete example and, where it helps, a counterexample.
6. Keep source numbers attributed. Keep facts apart from interpretation.
7. End with one sticky sentence.

Analogy map for AI-native engineering:

| Source idea | Plain translation |
| --- | --- |
| LLMs are search and assimilation tools | The model matches patterns better than it magically understands |
| Four-word naming | Labels on drawers: clear names help people and models find the right one |
| Iteration | The first answer is a draft, not the finish line |
| Summary documents | Bookmarks: long chats forget, so write checkpoints |
| Self-reasoning | Talking out loud helps catch weak logic |
| Anti-pattern lists | A "do not step here again" map |
| TDD-first | The answer key before building: tests say what done looks like |
| Context engineering | Pack the right tools in a backpack, not everything in a dump truck |
| Give agents a computer | Real work needs files, a shell and scripts, not one giant prompt |
| Context offloading | Save old details to files instead of stuffing the prompt |
| Sub-agents, context isolation | Teammates in different rooms so they do not trip over each other |

Output shape, Markdown unless asked otherwise:

```markdown
# <Topic in simple words>

## Big Idea
## Why It Matters
## Core Ideas Made Simple
## Tiny Example
## What To Remember
```

Example to reuse:

```markdown
Bad name: `filter()`
Better name: `filter_implementation_entities_only()`

Why? The better name tells you:
- what it does
- what it looks at
- what it keeps
```

Guardrails: not "wrong but cute"; keep nuance where safety, correctness or measurement matters; no hype as universal truth; no jargon flood; keep only details that unlock understanding; do not claim that exactly four words produce a given speed-up; add an ASCII diagram only when the reader wants a visual or layout clearly helps.

## Interactive playgrounds

A playground is a decision laboratory. The user changes meaningful state, sees an honest consequence, compares alternatives and exports a decision that someone else can act on.

Use it when reversible variables interact and feedback changes judgment. Use a static explainer for fixed choices, a form for known exact values, an editor for free-form text, a notebook for computation with narrative, and the production tool for permissions, collaboration or irreversible actions.

| Kind | The user decides | Export |
| --- | --- | --- |
| Design explorer | spacing, colour, type, layout, responsive behaviour | direction for a developer, with context and non-default choices |
| Data explorer | query, API, pipeline, schedule, regex | candidate plus schema-aware specification |
| Concept map | what they know, relationships | learning request or scope record |
| Document critique | accept, reject, comment on suggestions | approved changes and retained objections |
| Diff review | findings on changed lines | comments with file, side, line, context |
| Code map | which components to discuss | feedback per component with file path and provenance |

Choose by state and output meaning, not by visual similarity.

Build order:

1. Write the decision and who consumes the export.
2. Define one state object with defaults. Every control and drag writes to it. Every preview, summary and export reads from it.
3. Build one control -> state -> preview -> export path first.
4. Add named presets that set the whole state, a reset, and undo where work can be lost.
5. Handle empty, invalid, long and imported input. Explain invalid combinations instead of silently changing them.
6. Give every pointer action a keyboard or list equivalent. Do not rely on colour, hover or drag alone.
7. Verify in a real browser and with the real consumer of the export.

Skeleton, a complete file that passes the playground check below. Replace the controls, the state fields and the export wording:

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Card playground</title>
<style>
  body { font: 16px/1.5 system-ui, sans-serif; margin: 1rem; max-width: 60rem; }
  main { display: grid; gap: 1rem; grid-template-columns: repeat(auto-fit, minmax(16rem, 1fr)); }
  #card { padding: 1rem; border: 1px solid #888; }
  #export { white-space: pre-wrap; user-select: all; border: 1px solid #888; padding: .5rem; }
</style>
</head>
<body>
<h1>Card playground</h1>
<main>
  <form id="controls">
    <label>Corner radius (px) <input name="radius" type="number" min="0" max="32" step="1"></label><br>
    <label>Shadow blur (px) <input name="shadow" type="number" min="0" max="40" step="1"></label><br>
    <label>Title <input name="title" type="text" maxlength="60"></label><br>
    <button type="button" data-preset="flat">Flat</button>
    <button type="button" data-preset="raised">Raised</button>
    <button type="button" id="reset">Reset</button>
  </form>
  <section aria-label="Preview (simulation, not the production component)">
    <div id="card"><strong id="card-title"></strong><p>Preview only.</p></div>
  </section>
</main>
<h2>Export</h2>
<p id="export"></p>
<button type="button" id="copy">Copy</button> <span id="status" role="status"></span>
<script>
const DEFAULTS = Object.freeze({ radius: 8, shadow: 0, title: "Card" });
const PRESETS = {
  flat:   { radius: 0,  shadow: 0,  title: "Card" },
  raised: { radius: 12, shadow: 24, title: "Card" },
};
let state = { ...DEFAULTS };
let notice = "";
const form = document.getElementById("controls");
const clamp = (n, lo, hi) => Math.min(hi, Math.max(lo, Number.isFinite(n) ? n : lo));

function setState(patch) {                       // the only way state changes
  const next = { ...state, ...patch };
  const radius = clamp(Number(next.radius), 0, 32);
  const shadow = clamp(Number(next.shadow), 0, 40);
  notice = (radius !== Number(next.radius) || shadow !== Number(next.shadow))
    ? "A value was outside its range and was limited: radius 0 to 32, shadow 0 to 40."
    : "";
  state = { radius, shadow, title: String(next.title).slice(0, 60) };
  render();
}

function render() {                              // every view reads state
  for (const key of Object.keys(state)) {
    if (form.elements[key] !== document.activeElement) form.elements[key].value = state[key];
  }
  const card = document.getElementById("card");
  card.style.borderRadius = state.radius + "px";
  card.style.boxShadow = state.shadow ? `0 4px ${state.shadow}px rgba(0,0,0,.3)` : "none";
  document.getElementById("card-title").textContent = state.title;   // text, never markup
  document.getElementById("export").textContent = buildExport();
  document.getElementById("status").textContent = notice;  // say so, do not hide it
}

function buildExport() {                         // built from state, never from the DOM
  const parts = [];
  if (state.radius !== DEFAULTS.radius) parts.push(`corner radius ${state.radius}px`);
  if (state.shadow !== DEFAULTS.shadow) {
    parts.push(`${state.shadow > 16 ? "a pronounced" : "a subtle"} shadow (${state.shadow}px blur)`);
  }
  if (state.title !== DEFAULTS.title) parts.push(`title ${JSON.stringify(state.title)}`);
  return parts.length
    ? `Update the card component: ${parts.join(", ")}. Keep everything else as it is.`
    : "No changes from the defaults.";
}

form.addEventListener("input", (e) => setState({ [e.target.name]: e.target.value }));
form.addEventListener("click", (e) => {
  if (e.target.dataset.preset) setState(PRESETS[e.target.dataset.preset]);
  if (e.target.id === "reset") setState(DEFAULTS);
});
document.getElementById("copy").addEventListener("click", async () => {
  const status = document.getElementById("status");
  try {
    await navigator.clipboard.writeText(buildExport());
    status.textContent = "Copied.";
  } catch {
    status.textContent = "Copy failed. Select the export text and copy it by hand.";
  }
});
render();
</script>
</body>
</html>
```

Rules:

- Insert user or imported text with `textContent`, never as markup. Do not parse SQL, Markdown or diffs with regular expressions and inject the result.
- The export is an instruction or structured record with enough context to act on without the playground. A prompt is one export format, not the only one.
- A preview is a simulation unless it uses the real renderer. A generated query is a candidate until its parser accepts it. Label both.
- Review anchors carry revision, side, line range and a context digest. If the text changed, mark the comment stale. Never move it to a nearby line.
- Comment and node identifiers must not be timestamps if state is ever imported or merged.

The sources disagree on three points. Keep both and select by cost:

- Update on every change with no Apply button for cheap, reversible, local work. Use an explicit Apply for expensive, irreversible or privileged effects.
- A single self-contained file with no external dependency suits a trusted, portable prototype. Use an application structure when reuse, tests, data or operations matter.
- A handful of presets and a dark theme are a starting habit, not a rule. Presets must be reviewed whole-state combinations. Colours and counts from an example are not policy.

## Output contract

Every delivery includes:

1. The artifact at its agreed path (`.html`, `.txt`, or Markdown).
2. The reader and the outcome it was written for.
3. The sources used, as paths, in the footer or reading notes.
4. Commands run and their results.
5. Checks recorded as `pass`, `fail`, `not_applicable` with a reason, or `not_evaluated`. An omitted check is not a pass.
6. Open risks and the source changes that should trigger a refresh.

Per mode:

- HTML: one file, inline CSS and JS, opens from disk, one `h1`, `lang` and viewport set, navigation targets resolve, footer lists sources, no scaffold residue.
- ASCII: title, short setup, sections, optional legend, reading notes; declared canvas width; validator clean.
- ELI5: the five-heading shape, an analogy per major concept, one concrete example, one closing sentence.
- Playground: one state object, live preview, export built from state, reset, keyboard path, honest copy status.

## Quality gates

ASCII (file-backed page; drop `--editorial` for a single small figure; use 72 or 96 when that canvas is declared; never pass `--allow-unicode` under a strict-ASCII promise):

```bash
python3 scripts/check_ascii_diagram_quality.py path/to/page.txt \
  --max-width 84 --max-prose-width 64 --editorial
```

The script's default width is 100, so always pass `--max-width`. Exit code 0 is pass, 1 is fail. Lines containing `|` or `/` are treated as diagram lines and skip the prose-width check.

HTML generator preflight (proves the generator, not the story):

```bash
python3 scripts/create_elegant_explainer_html.py --output /tmp/explainer-preflight/index.html \
  --hero-title "Preflight" --hero-subtitle "Check"
python3 scripts/create_elegant_explainer_html.py --output /tmp/explainer-preflight/index.html \
  --hero-title "Preflight" --hero-subtitle "Check"   # must refuse without --force
```

HTML residue scan (must print nothing):

```bash
grep -n -E 'Replace this|Path A|Path B|Choose One Helpful Metaphor|\{\{[A-Z_]+\}\}|__[A-Z_]+__' .prd/ELI5/index.html
```

HTML structure, navigation and fallback scan:

```bash
python3 - .prd/ELI5/index.html <<'PY'
import re, sys
from html.parser import HTMLParser

text = open(sys.argv[1], encoding="utf-8").read()

class Scan(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags, self.ids, self.targets = [], set(), []
        self.lang = self.viewport = False
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        self.tags.append(tag)
        if a.get("id"):
            self.ids.add(a["id"])
        if a.get("data-target"):
            self.targets.append(a["data-target"])
        if tag == "a" and (a.get("href") or "").startswith("#") and len(a["href"]) > 1:
            self.targets.append(a["href"][1:])
        if tag == "html" and a.get("lang"):
            self.lang = True
        if tag == "meta" and a.get("name") == "viewport":
            self.viewport = True

s = Scan()
s.feed(text)
problems = []
for tag in ("html", "head", "title", "body", "h1", "footer"):
    if tag not in s.tags:
        problems.append(f"missing <{tag}>")
if s.tags.count("h1") != 1:
    problems.append(f"expected one <h1>, found {s.tags.count('h1')}")
if not s.lang:
    problems.append("<html> has no lang attribute")
if not s.viewport:
    problems.append("no viewport meta tag")
for target in s.targets:
    if target not in s.ids:
        problems.append(f"navigation target '{target}' has no matching id")
if re.search(r"(?m)^\s*\.reveal\s*\{[^}]*opacity:\s*0", text):
    problems.append("unscoped .reveal hides content when the script does not run")
if "prefers-reduced-motion" not in text:
    problems.append("no prefers-reduced-motion rule")
print("\n".join(problems) if problems else "PASS: structure, navigation targets, fallbacks")
sys.exit(1 if problems else 0)
PY
```

This scan is not full HTML validation.

Rendered check. Open the file from disk (`xdg-open`, `open`, or a browser). For a first-viewport screenshot without a display:

```bash
google-chrome --headless --disable-gpu --hide-scrollbars --window-size=390,844 \
  --screenshot=/tmp/explainer-narrow.png "file://$PWD/.prd/ELI5/index.html"
```

Then check by hand and record each as pass, fail or `not_evaluated`: desktop and narrow width without clipping or sideways page scroll; every act reachable by keyboard with visible focus; nothing depends on hover; reduced-motion setting; content visible with scripts blocked; fonts blocked; browser console clean; navigation dots match acts. In a headless environment, defer the interaction checks to the first human view and say so.

Reading gates for an HTML explainer:

1. Opens with a problem or question, or the mechanism for a familiar audience.
2. Mechanism named by Act II.
3. Metaphor before code where a metaphor is used; mechanism stated right after.
4. One concept per act.
5. Comparison where two or more approaches exist.
6. Code blocks labelled and short.
7. Ends with a summary table and one-line takeaway.
8. Footer lists sources; every major claim traces to one.

ELI5 done check: first paragraph gives the big idea; each major concept has an analogy with its limit; at least one concrete example; readable by a smart beginner; ends in one sentence; source numbers attributed.

Playground check: change every control and confirm preview and export both change; apply each preset, then reset; paste `<img src=x onerror=alert(1)>` into every text input and confirm it shows as text; complete the task with the keyboard only; deny clipboard permission and confirm the failure message; give the export to its real consumer.

## Anti-patterns

- Explaining before understanding the code. Fluent narrative teaches the misreading.
- Opening with a definition in vendor vocabulary.
- A metaphor that replaces the mechanism, or is merely relatable. "AI forgets like a child" is wrong but cute.
- Burying the main loop after pages of context.
- Scaffold text or invented symmetric "Path A / Path B" content left as fact.
- A component gallery, or one component repeated for the whole page.
- Code dumps in place of explanation.
- Essential content that appears only when a script runs, or only on hover.
- Motion with no reduced-motion fallback.
- A source footer that lists a root folder with no traceable claims.
- One giant ASCII figure for topology, sequence, glossary and tradeoffs at once.
- Paragraphs inside boxes; diagonal or crossing connectors; drifting panel widths; lines wider than the canvas.
- Repeating a source's performance number as a universal fact.
- Playground controls that change nothing, exports read from the DOM, raw markup rendering, pointer-only canvases, a "Copied" message shown without checking.
- A dark theme and act layout with no source citations. That is decoration, not this method.

## Bundled files

| File | Use |
| --- | --- |
| `scripts/create_elegant_explainer_html.py` | Writes a seven-act HTML scaffold from `assets/elegant-explainer-template.html` |
| `scripts/check_ascii_diagram_quality.py` | Validates ASCII-only, tabs, trailing spaces, width, and page composition with `--editorial`; `--json` for machine output; `-` reads stdin |
| `assets/elegant-explainer-template.html` | Template with `__PLACEHOLDER__` tokens, filled by the script |
| `assets/template.html` | Richer hand-filled template with `{{PLACEHOLDER}}` tokens |

[reference.md](reference.md) holds the pattern rankings, all ASCII skeletons, the brief and run-card templates, worked examples, failure tables and evidence notes.

## Self-check before delivery

- Can I name the one reader and what they should predict or decide?
- Did I read the code or notes before writing, and can every major claim point to a source?
- Is the mechanism visible by the second act, section or paragraph?
- Does each act, section or screenful carry one idea?
- Does every metaphor have its mechanism and its limit beside it?
- Are source numbers attributed and unknowns stated?
- Did I run the gate commands for the mode and record the results?
- Did I look at the result on its real surface, at narrow width, without scripts?
- Is all scaffold text gone?
- Did I say what was not evaluated?
- If I reported a count, a rate or a timing, did I give the denominator, the version and the misses?
- If I handed part of the question to another artifact, did I check that artifact's scope and gate, and say what closes the handoff?
