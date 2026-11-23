# Visual Explainers Reference

This file holds the deeper material behind [SKILL.md](SKILL.md): rankings, decision tables, briefs and run cards, every ASCII skeleton, worked examples, failure tables, verification commands and evidence notes. SKILL.md is enough to produce an artifact. Come here when a choice is unclear, when a review needs a checklist, or when something failed.

Read it in pipeline order when producing an artifact. Read the Completeness Checklist and the Anti Pattern Registry first when reviewing one.

## Idiomatic Thesis Synthesis Statement

An explainer is a maintained interface between a changing source and a reader's mental model. It is judged by how fast a named reader reaches a correct model and can predict a state, a failure or a recovery outcome. It is not judged by component count, scroll depth or novelty.

The chain every mode follows:

```text
source -> claim -> teaching choice -> reader model -> next action -> check
```

Evidence constrains the narrative. The narrative selects the components. Verification on the real surface tests the artifact. If a diagram or a browser review exposes a faulty source model, go back to the source and do not polish the component.

Narrative order reveals the mechanism. Visuals compress relationships that prose handles badly. Browser behaviour keeps the content reachable under declared conditions. Style is not evidence. Intuition earns the reader's entry and then yields to exact mechanics. A familiar audience may start at the mechanism, and a decision tree or a transformation may replace a loop as the spine. Leaving detail out is acceptable only when the scope and the uncertainty are visible.

Thesis check for a page: name the audience's question and trace where it is answered; restate the causal path early; reach the mechanism and the caveats by keyboard, on a narrow screen, with reduced motion and with scripts failing; use the closing compression to predict a state, failure or recovery outcome within scope. A presentation defect that changes availability, order, attribution or apparent causality is a correctness defect, not decoration.

Presentation is the last step of a comprehension pipeline. The five stages run in order: explore the source, plan the narrative, apply the teaching rules, build from a scaffold, check and deliver.

### The core trio

These three are conjunctive. Skipping one is non-compliance, not a style choice.

1. Understanding before writing. Every later technique amplifies what the author believes. A vivid metaphor for a misunderstood mechanism teaches the misunderstanding.
2. Intuition before code. A metaphor or concrete case lowers the entry cost, then the exact mechanism follows at once.
3. One concept per act, section or screenful. Two tightly coupled concepts in one act still count as two. Split at the seam between motivation and mechanism.

The claim that metaphors-first teaches better is a design hypothesis in the sources, not a cited result.

### The four mode contracts

| Mode | The medium's promise | What breaks the promise |
| --- | --- | --- |
| HTML explainer | Opens from disk, reads in order, works at declared widths, by keyboard, with reduced motion, and when scripts or fonts fail | Invented behaviour, scaffold residue, content gated behind a script |
| ASCII page | Survives a monospaced terminal, raw copy and paste, and a diff | Unicode, tabs, lines wider than the canvas, one overloaded figure |
| ELI5 note | A smart beginner gets the idea in one pass and the nuance is kept | Cute but wrong analogies, hype, missing limits |
| Playground | Changing state shows an honest consequence and the export can be acted on | Controls that change nothing, a preview passed off as production, unsafe rendering |

Polished invented behaviour fails. Accurate prose in a broken or unreachable page also fails. A presentation defect that changes availability, order, attribution or apparent causality is a correctness defect.

### Invariants for any variant

A variant may swap HTML for slides or a terminal page. It keeps the method only if it keeps:

- the stage order with understanding first;
- the core trio;
- the full set of quality gates, applied together;
- an honest statement of which scaffold was used and what was checked.

A dark theme and an act layout without source citations is decoration, not adoption of this method.

### Where the sources disagree

| Topic | Position A | Position B | Selector |
| --- | --- | --- | --- |
| Visual richness | Apply every teaching technique: a metaphor per concept, at least three component types, animated flows | One dominant visual direction, metaphor only when it helps, one or two code excerpts, little motion | Novice onboarding and long pages lean to A. Expert readers and short pages lean to B. Every component still needs a job |
| Metaphor marker | An emoji icon in the metaphor card | A number mark | Use the number or a word where the project rejects emoji |
| Class names | `accent-1`, `accent-2`, `code-dot c1` (and older topic names such as `pg`, `mongo`) | `accent-primary`, `accent-secondary`, no code dots | Use the names of the template you chose, or add CSS |
| Missing metaphor layer | Styled code with no metaphor is a failure | A metaphor that does harm should be deleted | Keep a metaphor only when its mapping preserves the mechanism. A familiar audience may start at the mechanism |
| Playground updates | Always live, no Apply button | Live only for cheap, reversible, local work; explicit Apply for expensive, irreversible or privileged effects | Cost and reversibility of the effect |
| Playground packaging | Always one file, no external dependency | One file is a portable prototype shape, not a universal architecture | Trust, reuse, tests, data and operations |
| Presets and theme | A few named presets and a dark theme by default | Presets are reviewed whole-state hypotheses; example colours and counts are not policy | Whether the artifact is disposable or shared |
| Copy feedback | Show "Copied" briefly | Await the clipboard result, show failure, keep the output selectable | Always B when the export is a handoff |
| Numeric reliability targets | One source lists pass-rate targets such as 18 of 20 | Another rejects them as unfounded | No such target is stated here. See Reliability Target |

## Pattern Scoreboard Ranking Table

Ranks are editorial order, not measured scores. The numeric scores attached to some rows in the sources were ordering metadata and are not reproduced. No score waives a required row. Fail closed at the earliest unresolved required row. Promote a conditional row to required only for a named project risk such as localisation, privacy or formal accessibility.

### Across all modes

| Rank | Pattern | Tier | Prevents | Direct gate |
| --- | --- | --- | --- | --- |
| 1 | Source map first | required | Fluent explanation of a misread source | Every major claim has a source span or an inference label |
| 2 | Evidence boundary split | required | Source claims, measurements and analogies blending into fact | Each number and guarantee carries its status |
| 3 | Verification gate coupling | required | Advice nobody can check | Each recommendation has a command, a reviewer question or an observable result |
| 4 | One reader, one decision | required | Averaged audience, no next action | The brief names both |
| 5 | Mechanism early | required | The main loop buried under context | Reviewer can restate it after Act II or section two |
| 6 | Bounded analogy | required | Analogy overreach | Mapping, non-mapping and stopping point are written down |
| 7 | Fidelity and comprehension tested apart | strong default | Readable but wrong, or right but unusable | Reviewer check and reader teach-back recorded separately |

### HTML explainer

| Rank | Pattern | Tier | Direct gate |
| --- | --- | --- | --- |
| 1 | Inventory evidence first | required | Claim ledger exists; inference and uncertainty are visible on the page |
| 2 | Source-named loop, lifecycle, decision path or state transition by Act II | required | Reviewer restates it |
| 3 | Analogy only to lower initial cost, each element bound to exact mechanics | required | Remove the analogy; the explanation is still complete |
| 4 | Semantic claims and rendered behaviour verified independently | required | Claim-source review plus direct-open, keyboard, viewport, console and content-state checks |
| 5 | Inline CSS and JS, no build step | strong default | A copy of the file opens in a fresh local browser |
| 6 | Each visual answers a named question that prose handles worse | strong default | Each component has a written role |
| 7 | Unused acts, generic labels, sample failures and template assumptions removed | strong default | Residue scan plus human read |
| 8 | Subtle motion and persistent navigation | conditional | Only when length or audience justify them, with reduced-motion, keyboard, static and no-script fallbacks |

### ASCII page

| Rank | Pattern | Prevents | Direct gate |
| --- | --- | --- | --- |
| 1 | Page system first | A pile of unrelated figures | The run card names the system before any figure is drawn |
| 2 | Width budget before wording | Wrapped or panned lines | Canvas and prose widths declared; validator run with them |
| 3 | Reader question matches figure | Wrong grammar for the task | Type identifiable in under five seconds |
| 4 | Straight main reading path | Ambiguous direction | Reader traces the path unaided |
| 5 | Stable grid and repetition | Drift, noisy diffs | Same card width and gutter in each repeated row |
| 6 | Tight labels, prose outside | Paragraphs in boxes | Labels are nouns; actions sit on arrows |
| 7 | Validator plus reader review | Clean bytes with no meaning, or meaning with broken bytes | Both recorded |

Default order of work: reader question, page system, canvas and anchors, modules, local figures, connectors, labels, prose tightening, validator, cold-reader review, full-scroll reconciliation. A small figure may skip the page ceremony. It may not skip the medium decision, the width, the pattern fit or the finish gates.

### Playground

Construction order, each with the observation that falsifies it:

| Order | Gate | Falsified when |
| --- | --- | --- |
| 1 | Decision before controls | Nobody can name the uncertainty or the consumer of the export |
| 2 | Kind fits the domain | The kind was chosen because it looked similar |
| 3 | One canonical state | Two views disagree after an edit |
| 4 | Invalid-state semantics | An invalid combination changes silently |
| 5 | Truthful preview | A simulation or stale result looks current |
| 6 | Safe rendering | Imported text runs or reshapes the page |
| 7 | Equivalent interaction | The core task cannot be done by keyboard or list |
| 8 | Output fidelity | The export differs from the state or needs the playground to be understood |
| 9 | Comparison and recovery | No named alternatives, reset or undo |
| 10 | Source and anchor provenance | An edge or comment cannot be traced to a revision |
| 11 | Responsive and full-state rendering | Empty, loading, error or narrow states hide actions |
| 12 | Persistence and migration | Old saved state corrupts the new version |
| 13 | Downstream validation | The real consumer rejects the export |

Repair starts at the earliest broken gate.

## Agent Usage Decision Guide

### Kinds of request

| Request | What to do |
| --- | --- |
| Create a new explainer | Full workflow in SKILL.md |
| Adapt an existing explainer | Inspect it first; keep its density, pacing and tone unless a redesign is asked for |
| Diagnose rendering or interaction | Reproduce on the stated surface; fix the responsible layer; rerun affected checks |
| Review content and narrative | Inspect the output first, then the sources. Report findings. Do not rewrite when the request is review only |
| Refresh a stale explainer | Re-verify citations per act. Replace the page if the old narrative now teaches the wrong model |
| Route to another medium | Say which and why: Markdown, ASCII, Mermaid, slides, a generated document, or a tested frontend |

Sequence common to all of them: clarify what the reader must predict or decide; confirm which paths you may write; gather the minimum honest evidence; read the method material; fix the spine; save incrementally; verify meaning and rendering; report exact changes, evidence and risks.

### What to read and write down before outlining

Read: core implementation files; supporting interfaces, traits or protocols; specs, notes or the PRD; existing diagrams, tests and issue threads; an earlier explainer for local tone.

Write down:

- a one-sentence thesis;
- the main loop or lifecycle, in the code's verbs;
- primary actors and nouns (state objects, checkpoints, queues, topics, tables, offsets, retries);
- boundaries: where data enters, transforms, persists, fails and is retried;
- what state is persisted and when;
- failure classes;
- extension points or plugin boundaries;
- the three details most likely to surprise or be misunderstood;
- file paths and line numbers for all critical code.

Keep two inventories apart. Method evidence says how an explainer is shaped. Subject evidence says what the system does. Flag any subject "fact" that came from a scaffold example. Archived styles and breakpoints are not requirements.

Source order for an ELI5 note: the actual subject source, the explanation method, a worked reference when relevant, public documentation only for a named question. Stop when the claim, terms, caveats, example and verification are covered.

A source list is a retrieval map, not a vote count. Use code and tests for executable detail, product documentation for current behaviour, primary research for scientific claims, and representative readers for comprehension. Audience evidence governs comprehension, not truth. If a supporting claim disappears from the source, remove or replace the memorable analogy that rested on it.

Public material is a freshness check, not a replacement for the local source. Authority order for public material: supported official versioned documentation; then installed help, schemas and observed local behaviour; then public repositories, for implementation detail only; then community formats, for portability only. Keep disagreements visible. Before using a public page in the present tense, record the access date, the product and version, the passage, the concept it illustrates and where the analogy stops. Until then it is an unrefreshed pointer and supports nothing. A public example of instruction files or automated checks illustrates the idea. It does not define all agents and does not replace local authority.

### Delegation

Use exploration sub-agents for comprehension: structs, flows, error paths, with file and line citations. Keep narrative, teaching choices and generation with the invoking agent. Do not skip exploration because the code seems familiar; fluent but shallow context is the characteristic failure. Requests arrive as "explain how this works", "ELI5", onboarding, or documentation that should not be boring, so routing only on the word "visual" misses most of them. Keep the exploration notes beside the page, including sources loaded and sources skipped on purpose.

### Loading profiles for ASCII work

- Small figure: SKILL.md rules, one skeleton from Theme Specific Artifact, the review checklist, the validator.
- Long page: SKILL.md rules, the page systems, the grid rules, local skeletons, the review checklist, the validator with `--editorial`, a full-scroll read.

### Preflight questions

ASCII, full page: reader goal; target surfaces; canvas width; page system; one job per section; figure per section; grid anchors; longest realistic labels; vocabulary; what is left out and where it lives; how the result will be verified.

ASCII, small figure: relationship type; direction; target width; label vocabulary; finish gate.

Playground: audience, task, uncertainty, alternatives, consequence and owner; what success looks like; source identity and trust; typed state; invalid, destructive, undo and reset behaviour; how authoritative the preview is; keyboard paths; viewports; export consumer; persistence; evidence.

### Stop or route

Stop before drafting an ASCII page when the purpose is unclear, the width is undeclared, sections repeat one job, or the target rendering cannot be inspected.

Block or route a playground when there is no decision or consumer; the source is untrusted or stale; the domain's semantics would be flattened; a simulation would be taken as authority; an action is privileged or irreversible; the graph is pointer-only or colour-only; markup is unsafe; shared state is unversioned; the consumer rejects the export; or the thing is really a production workflow. Route again when illustrative data becomes real, state gets saved or shared, a prompt becomes executable, a graph gains source claims, or collaboration appears.

Pause an ELI5 note when evidence is absent or conflicting, or when exact behaviour governs. Either ask for the evidence or publish a bounded framework that says what is unknown.

### Precedence when guidance conflicts

Quality gates, then the process, then the component catalogue, then the template. A non-standard component passes if every gate holds. The output location is a gate in practice: a page nobody can find has failed. A page that uses the exact skeletons and still opens with definitions fails.

What each layer costs when it is lost: without the template the work is slower and degraded; without the component skeletons the classes can be reinvented; without the gates there is no definition of done.

When two sources conflict:

1. Name the disputed claim exactly, and each source's role, version and scope. Keep "what was intended" apart from "what was observed".
2. Send it to the owner of that kind of truth. A conflict about method goes to the owner of the method material. A conflict about the subject goes to the owner of the system. A conflict about rendering goes to the owner of the artifact, with a reproduction.
3. Until a high-consequence conflict is resolved, narrow the claim or mark it uncertain. Keep both positions. Do not average them.
4. Record an override as a new decision, not as a silent edit.

For ASCII layout conflicts compare version, scope, artifact size, canvas and audience, then choose one of keep, adapt, decline or defer. Name the target-width or reader test that settles it and keep the observations. A verified 72-column target may override the 84-column default for that page without invalidating the default. Record the role, the question, the constraint, the decision, the exception and the evidence. One unusual page is a local adaptation. Repeated exceptions for the same target are a reason to refresh the default.

For playgrounds, promote a rule to shared status only after fixtures from more than one playground kind pass it. Demote it after an unsafe copy, an incompatibility, a user failure or the loss of its owner.

## Decision Tradeoff Guide

### Which medium

| Need | Use | Cost |
| --- | --- | --- |
| Staged reading, visual relations, browser available | HTML explainer | Rendering and accessibility checks; refresh burden |
| Portability, diffs, terminals, low maintenance | ASCII page | Less rich; width discipline |
| Fast orientation for a beginner | ELI5 note | Leaves out depth; needs a route to the governing document |
| Reversible variables that interact | Playground | State, safety and consumer checks |
| Exhaustive lookup | Reference documentation | Slow for orientation |
| Structured diagram with a renderer | Mermaid or similar | Depends on the renderer |
| Auth, live or personal state | Tested application | Build and operations |

A live walkthrough is richer once and unavailable to the next hire. Plain Markdown is the bounded alternative when interactivity adds nothing; the act structure transfers to Markdown.

### Signal to artifact

| The reader needs | Produce |
| --- | --- |
| A mental model | Plain-language explanation |
| An exact release procedure | Runbook |
| The truth about latency | Benchmark plan |
| Why tests help | Explanation linked to the actual acceptance tests |
| Security or legal approval | Policy, threat model or specification |
| An architecture choice | Decision memo |

A mixed request gets an orienting model, a handoff to the authoritative document, and an explicit statement of which one wins.

A one-sentence answer may need one source and one teach-back. Durable or quantitative work needs the full trace: source, claim, analogy or rule, reader check, owner. When an explanation is stored, templated, widely linked or consequential, promote it to a maintained artifact with an owner, sources, refresh triggers and a regression example. A reduced brief is fine for a low-risk chat answer, which then cannot claim broad reuse.

### Adopt, adapt or pause

- Adopt when the reader, decision, sources, consequence and example all match.
- Adapt when the mechanism fits but audience, authority or stakes differ.
- Pause or route when evidence is absent or conflicting, or exact behaviour governs.

Example: adopt the context-selection explanation for code review; adapt it for legal review; reject it as a numerical token-accounting specification. What reverses the choice is the decision and its consequence, not the topic name.

State the cost of error before choosing. A wrong explanation sends an agent or a reader to the wrong files, tests, abstraction or level of confidence. A reviewer must be able to tell which belief and action to undo and which derived artifacts may carry it.

Record with the choice:

```text
option chosen        : adopt | adapt | pause or route
source conditions    : what had to match for the choice to hold
rejected alternative : and why
cost of error        : judgment until observed; no invented forecast
reversal trigger     : changed source, failed reader fixture, new audience,
                       higher operational consequence
observed cost        : actual correction and refresh work, filled in later
```

Small vocabulary or example changes are still adaptations and belong in the record even when they add no new fact. The observed cost is what shows, over time, which cheap-looking simplifications cause the most rework.

Progressive disclosure can sequence an overview before a specification, or an analogy before a mechanism. It cannot turn qualitative guidance into an exact contract. Each added layer needs a stable purpose, a stated precedence and a refresh path for when its source changes.

### HTML explainer tradeoffs

| Choice | Gain | Burden |
| --- | --- | --- |
| Rich components | Engagement, parallel structure | Effort; risk of a gallery |
| Adapt the template | Consistency, speed | Template assumptions leak in |
| Completeness | Coverage | Pacing suffers; split instead |
| Accessible metaphor | Low entry cost | Accuracy; state the breaking point |
| External fonts or media | Look | Portability, privacy, fallback |
| Motion | Orientation | Reduced-motion states |
| Wide comparison | Scannable contrast | Narrow-screen reflow |
| Shared components across pages | Reuse | Build and version dependencies |

Metaphor fidelity test: grade the mapping, not the charm. The worked mappings show a discipline; they are not a library of metaphors to paste. Microphone versus mailbox preserves push versus poll. A car metaphor for a queue is merely relatable. A bank transaction works for two-phase commit only if "both sides must agree" is preserved. Every metaphor breaks somewhere: a postal worker does not batch; USB is wrong for a plugin system with no discovery.

### ASCII tradeoffs

| Page system | Tradeoff | Proof it fits |
| --- | --- | --- |
| Tall Variation Gallery | Long scroll, easy scanning | Each variation is small and self-contained |
| Glossary Plus Panels | Names first, then pictures | 3 to 6 concepts share one shape |
| Layered Walkthrough | Repeats context per layer | Reader needs intuition before mechanism |
| Two-Column Compare | Needs width | Exactly two options, same categories; at 72 columns stack unless the contrast survives |
| Mechanism Trace | One path dominates | Side notes stay shorter than the lines they annotate |

Side-by-side panels assert that the items are peers. Deliberate asymmetry is valid when it encodes a real difference. A change of figure grammar needs a section boundary and a cue to the reader. A request lifecycle may use a system map for participants, a sequence for the exchange and a comparison for retry policies, each in its own section.

Modes for ASCII in a document set: primary (the ASCII page is the deliverable), companion (an orientation map beside a richer artifact, each with a distinct job), or avoid as primary (the subject needs curves, dense topology or live values).

| Mode | Choose when | Cost | Question that can disprove the choice |
| --- | --- | --- | --- |
| Primary | Raw portability, vertical reading, stable alignment, bounded relations | Less spatial freedom and styling; strong for copying and diffing | Does the narrowest surface keep every action-critical relation without panning? |
| Companion | A richer artifact owns the detail; a terminal overview or fallback is still useful | Two representations to keep from drifting | Are omissions explicit, links stable, and conflicts resolved to one source? |
| Avoid as primary | Curves, crossings, exact geometry, rich hierarchy or interaction are essential | Rendering dependencies, in exchange for no semantic compression | Would simplification hide a relationship the reader needs? |

A wrong medium, page system or grammar costs rework, misleading edges, wrapping and confusion. Ask whether a skeleton at the target width can disprove the choice early. A companion never carries a model that silently conflicts with its authority. When ASCII is avoided as primary, keep ASCII or prose only for orientation, with no action-critical relation lost.

Do not create a row of panels to fill space. Stack unrelated jobs and keep their order distinct. During exploration compare small skeletons with identical content, canvas and reader question; then freeze one baseline. Record the target output, validator result, reader answer, omissions, reversal condition and the author's familiarity. Record the media that were rejected and what would reopen the choice. State vocabulary assumptions and send technical facts to subject review. Prefer the choice with the least irreversible investment in alignment and prose.

Source roles for ASCII guidance are organisational, not intrinsic. A coordinating file is a broad entry point, not the sole authority, and a supporting file can constrain it. Record each local decision as role, question, constraint, decision, exception and evidence. Repeated exceptions on real targets may justify refreshing the default. One unusual page is a local adaptation. Shorten labels to hold 84 columns only after the page system is chosen.

### Playground tradeoffs

Add structure only when it protects a state, an interaction, a handoff or a lifecycle obligation.

The durable artifact is a reversible, inspectable choice whose meaning survives beyond the browser tab. A single file with inline CSS and JS is portable and costs maintainability, security, testing and bundle size; it is not a universal architecture. The older playground material supplies a model for decision, state, rendering, safety, accessibility, output and verification. It does not choose a framework, state library, visual engine, schema, look or production service. Strong reuse keeps projections of one state and output derived from state, replaces unsafe markup with structured rendering, and rejects matching by line number, stale hard-coded maps and unsupported production claims.

Profiles to route between: design explorer; data or configuration explorer with a typed expression tree and an escaped preview; concept map that separates sourced edges from hypotheses; document critique; diff review anchored by file, side, line and hunk; code map bound to provenance; repair of an existing playground; promotion of a shared template; embedding in a product; orientation only. Avoid a playground as the primary artifact for a static explanation, a form, an editor, a notebook, an authoritative compiler, a privileged console, or an irreversible or collaborative product.

Further choices: one authoritative export, with a human explanation added only when people need it, both generated from state and compared for coverage. One responsive composition at first; distinct layouts only when the priority of interactions changes. Platform primitives for bounded behaviour; a library for established graph, editor, parser, state or accessibility complexity, after checking support, keyboard behaviour, bundle size, licence and upgrade path. A sanitiser needs a hostile corpus specific to its context. Adopt a mechanism only when a current obligation and a focused gate show its value. Adapt when the responsibility fits and the trust, consumer or framework differs. Avoid mechanisms with no owner, no recovery or no downstream use. Escalate policy, domain truth, threat, regulated accessibility, privileged data and operations.

Authority differs between a historical archive, a shared contract, a kind-specific candidate, an illustrative mechanism, negative evidence, a target's own policy or observation, and a promoted shared rule. Illustrative HTML, JS and CSS values, counts, colours, coordinates and layouts never become policy without independent acceptance. Demote a shared rule after an unsafe copy, an incompatibility, a user failure or the loss of its owner.

Keep one authoritative write model. Two canonical copies maintained by hand recreate the synchronisation problem. Do not execute or ship output from a packet that is still exploratory. Turn adaptations into conformance fixtures for schemas, renderers, anchor migration, interaction equivalence, persistence and consumers, including bad, borderline and incident-derived cases.

External authority classes for a playground: browser platform, accessibility standards, framework and build tool, security parser or sanitiser, domain schema or parser, visualisation engine, design system, clipboard or export consumer, persistence and sharing, automation, and hosting with its security headers. Do not invent links while the mechanism, framework, browser and hosting are unknown. Reproduce success, denial, unavailable, malformed, quota, zoom, input, migration and fallback cases locally. Before testing a target, inspect its package scripts, framework, state schema, parser, browser matrix, design system, accessibility policy, automation, hosting and consumer; a matching filename is not evidence. Gates include equality of all projections and a production build checked at its served address.

| Decision | Lighter choice, when | Heavier choice, when |
| --- | --- | --- |
| Packaging | One file: trusted, portable prototype | Application structure: reuse, content security policy, tests, data, routing, operations |
| State | Plain object: small, synchronous | Reducer or store: complex history, async, collaboration |
| Update | Immediate: cheap, reversible | Explicit apply; debounce, queue or cache remote work |
| Controls | Familiar inputs: exact, accessible | Drag, canvas, graph: when spatial action means something, always with a list or keyboard equivalent |
| Number entry | Typed input: reproducible | Slider: bounded perceptual exploration, paired with exact entry, min, max, step and unit |
| Rendering | Semantic DOM: ordinary text | SVG for scalable graphs; canvas only for dense drawing with structured accessibility beside it |
| Layout | Manual: small stable diagrams | Layout engine: dense or changing graphs, with deterministic fixtures, bounds, overlap checks, cancellation and reduced motion |
| Text | Text nodes | Sanitiser or parser for controlled rich text |
| Export | Prompt: conversational consumer | JSON, query, config, patch, review record or state: exact structure |
| Data | Synthetic: safer | Real metadata: with revision, redaction and refresh |
| Sharing | URL state: small, public | Opaque authorised identifiers: sensitive or large |
| Validation | Local: pure rules | Remote authority: current external truth, with pending, failure, cancel and stale handling |
| Responsiveness | One composition that reflows | Distinct layouts only when interaction priority changes |
| Libraries | Platform primitives | Libraries after support, keyboard, bundle, licence and upgrade checks |
| Visual checks | Human screenshots early | Deterministic baselines for repeated states |

Keep one authoritative export and generate the explanation from the same state. Illustrative values, counts, colours, coordinates and layouts from any example never become policy without independent acceptance. When advice conflicts, keep both positions; do not average them.

## Theme Specific Artifact

### Explanation brief (any mode)

```text
audience and prerequisites :
concrete goal              :
consequence or reuse       :
governing claim            :
causal steps               :
exact terms                :
bounded analogy            : maps / does not map / stops at
positive example           :
counterexample             :
decision boundary          :
next action, when to widen, when to stop :
evidence status            :
verification gates         :
confidence and unknowns    :
owner and refresh trigger  :
```

### Claim ledger row

```text
claim | source path and span | what it establishes | status | distortion check
```

Status is one of: source fact, source-reported measurement, observation made now, inference, analogy, recommendation, unresolved or conflicting. Give priority to memorable numbers, analogies and action rules.

A source's role is relative to the claim or task. It is not a permanent rank. The same file can be canonical for how to explain a concept and only supporting for whether a technical or numerical claim is true.

| Role | Meaning for this claim | What to do |
| --- | --- | --- |
| Canonical | Governs a defined decision | Record the scope and why it takes precedence |
| Supporting | Adds detail, examples or corroboration | Do not let it replace the canonical rule for another concern |
| Legacy | Informs history, no longer governs current behaviour | Find its successor before reusing its normative guidance |
| Duplicate | Repeats another source with no authority of its own | Count the pair as one source. Repetition is not independent corroboration. Keep the copy that ownership and freshness establish |
| Conflicting | Two applicable sources imply incompatible beliefs or actions | Show the disagreement, note owners and dates where known, and pause the affected recommendation until its owner resolves it |

Do not infer authority or obsolescence from a file's location or name, its age, or its resemblance to another file. Legacy, duplicate and conflicting are findings that need evidence of version, overlap or incompatible claims. Use the task instructions, lineage, content, ownership evidence and explicit supersession.

Canonical means the coordinating entry point for a decision. It is not the sole authority: a supporting source can constrain it.

For an HTML explainer four more roles are useful: executable (a script or template whose behaviour can be run), observed output (what a run actually produced), subject truth (the system being explained), and task-irrelevant (loaded and set aside). Scaffold text is never subject truth.

Read in two passes: the method source first, to fix the reader and the guardrails without locking in an analogy; then the subject source, to extract the claim, mechanism, terms, examples, conditions and evidence status. A heading is an orientation signal. Read the whole passage under it so that a condition outside the quoted line is not lost.

A method instruction is not subject evidence. "End with a sticky sentence" does not support a performance claim. Copying a reported number accurately while dropping its source-specific status is a fidelity failure: the reader repeats it as a universal fact. A content hash shows that reviewers inspected the same bytes. It does not show that the file is still correct or canonical.

After a source change, reopen only the rules, claims, examples, metrics and reader fixtures that depend on it, then check the whole file for coherence. Widen the review when the changed claim is foundational.

### HTML explainer brief and storyboard

```text
reader and starting state          :
observable outcome or prediction   :
bounded thesis                     :
scope and non-goals                :
source and claim ledger            :
actors and exact vocabulary        :
causal path and earliest reveal    :
state: tentative / durable, commit / crash / retry, unknown guarantees :
variants, boundaries, tradeoffs that bear on a decision :
misconceptions with evidence       :
acts: question / answer / sources / transition / takeaway :
component roles (one per component):
fallback plan: static / keyboard / reduced motion / narrow / no script / no assets :
visual density and tone            :
source footer and inline attribution :
verification: owner, targets, methods, refresh trigger :
```

Minimum subset for a short-lived internal page: outcome, thesis, scope, source ledger, causal path, storyboard, fallback plan, targets, final proof. For a stateless subject mark the state fields `not_applicable` with the reason.

The brief is a decision contract before the build and an index of evidence after it. It is not a duplicate of the page. List at most three misconceptions, each backed by evidence. An unresolved field blocks only the work that depends on it. Any substantial component in the final page that is absent from the brief needs evidence and a rationale, or removal. The verification line also names what evidence is retained.

The conservative architecture: one standalone file with inline CSS and JS that opens directly; scaffold deleted in favour of the source; the real problem, then the mechanism by Act II; at most one short metaphor mapped immediately; one dominant visual direction; static semantic order; typography that works with system fonts; text-first diagrams; one or two short excerpts. Depart from it only for a named benefit that can be tested. Each departure has a cost: external assets add portability, privacy and fallback work; motion adds reduced-motion states; shared components add build and version dependencies; wide comparisons add narrow-screen work. Re-evaluate the choice at the first substantive refresh. A wrong choice costs misleading decisions, caveats that cannot be reached, evidence that cannot be reproduced, and repeated patching of the wrong layer.

### Seven narrative beats in detail

1. Mystery in human terms. Why the thing exists and why it is hard. Patterns: "Data lives here, but it needs to move there." "It looks simple; the tricky part is not losing state." "Same protocol, different native dialects."
2. Core loop early, as a numbered flow: open or initialise, read or poll, transform, deliver or apply, commit or checkpoint. Mirror the code's verbs.
3. Compare modes with side-by-side cards: polling versus event-driven, source versus sink, implementation A versus B, happy path versus recovery, sync versus async. Keep it asymmetric when reality is.
4. State and safety. Slow down here. What is remembered, when it is persisted, what a crash or retry does, committed versus tentative, at-most, at-least or effectively once. Use a small diagram or branch view for commit and discard.
5. Architecture boundaries. What is pluggable, what is fixed, what the runtime does. What the component author implements, what the framework provides, where adapters attach.
6. Failure buckets. Transient versus fatal, recoverable versus not, user error versus infrastructure error, correctness versus performance. Use real examples.
7. Compression. "Poll. Transform. Deliver. Checkpoint. Repeat." or "Read state, decide, apply, persist, recover."

### Component palette rules

| Component | Rule |
| --- | --- |
| Hero | Plain-language title that answers "what is this page explaining?"; subtitle says why the page exists; one framing line |
| Metaphor card | One idea; short; followed by the exact mechanics; delete it if it does more harm than good |
| Flow steps | 4 to 6 steps for a loop or lifecycle |
| Code block | One or two per page; a representative query, a trait or interface shape, a retry condition, a configuration fragment; never a large file; always labelled |
| Diagram block | Small ASCII sketch, pipeline view or branch logic; must make sense pasted as plain text |
| Comparison cards | Clear labels, tight text, only shared decision dimensions |
| Option cards | Finite lists: payload formats, offset types, cleanup strategies, configuration modes |
| Summary table | Near the end; a compact sweep; columns readable on a laptop |
| Insight callout | The one thing to keep from the act |

Writing rules: short paragraphs, scannable on a laptop; define jargon once; exact nouns from the source where precision matters; explain why; calm and factual. Visual rules: one file; coherent palette (change the CSS colour variables per topic, for example blue for a database subject and green for networking); subtle motion for orientation only; readable on a phone; text-first diagrams over image dependencies.

### Components found only in `assets/template.html`

Animated flow (CSS-only pulsing arrows) and branch view:

```html
<div class="animated-flow">
  <div class="af-box c1"><h5>Source</h5><p>rows at rest</p></div>
  <div class="af-arrow">--></div>
  <div class="af-box brand"><h5>Connector</h5><p>poll and map</p></div>
  <div class="af-arrow">--></div>
  <div class="af-box c2"><h5>Stream</h5><p>messages in motion</p></div>
</div>

<div class="branch">
  <div class="branch-path success"><h4>Success</h4><p>Commit the tentative state.</p></div>
  <div class="branch-path failure"><h4>Failure</h4><p>Discard it and retry from the last commit.</p></div>
</div>

<table class="comparison-table">
  <tr><th>Feature</th><th>Polling</th><th>Change stream</th></tr>
  <tr><td>Needs a replica set</td><td><span class="tag-no">No</span></td><td><span class="tag-yes">Yes</span></td></tr>
</table>
```

Highlight spans: `.hl-1`, `.hl-2`, `.hl-brand` in `template.html`; `.highlight-primary`, `.highlight-secondary`, `.highlight-strong` in `elegant-explainer-template.html`.

Navigation dots are hidden at 900 px and below in `template.html` and at 960 px and below in the elegant template. Both collapse comparison grids to one column at 640 px and below. These are properties of the bundled files, not requirements.

### If a template file is missing

Rebuild from the component markup in SKILL.md and say that the page was built without the bundled template. This is a degraded path. Do not promise scroll reveal or navigation behaviour that was not seen working.

### ASCII run card

```text
reader_goal          :
target_surfaces      :
canvas_contract      : 84 cols, prose 60, gutter 2
page_system          :
section_jobs         : one line per section
local_figure_map     : section -> figure type
grid_anchors         : left margin, card width, glossary column, side-note column
label_budget         : longest realistic label per box
visual_vocabulary    : + - | --> <-- v ^
omissions_and_routes : what is left out -> where it lives
candidate_identity   : file path and revision
verification_packet  : validator command and result, surfaces pasted into,
                       reader check
```

The run card is a compact, diffable rationale for one reader journey that can be proved wrong, under one audience, owner, canvas and acceptance contract. It is not a second copy of the page. Split the card when any of those contracts diverges.

What each field is for: the reader goal stops decorative figures replacing the task; surfaces set the portability boundary; the canvas contract (hard, default and prose widths, tab policy, ASCII-only policy) makes wrapping and character checks reproducible; section jobs expose duplication and gaps; anchors prevent page-wide drift; the label budget treats text as geometry and records the shorten, wrap or widen decision; omissions and routes separate deliberate disclosure from missing evidence; candidate identity pairs a stable revision with the exact text and prevents stale validation.

A draft may have provisional geometry. A candidate freezes copy, anchors and canvas so evidence can be collected. A rejected card records the contract that was violated and the next route or stop. A study kept on file records what was learned (for example, a two-column compare that was not legible at 72 columns) and does not imply readiness.

Example card: 84 hard canvas, 60 prose, layered walkthrough, vertical sequence, shared card width, straight arrows, a retry appendix. Its packet holds the validator result, a longest-line scan, every render, and a second reader who found the timeout and retry path unaided. "Readable diagram, check formatting" is inadequate. Widths with no reader goal or candidate identity are borderline.

Geometry and validation that come from the source rules stay mandatory. Lifecycle, retention and handoff depth depend on how many people collaborate. Link bulky evidence. When migrating to a man page or another text format, carry the reader goal, omission routes and figure semantics before the border characters. A maintained card passes when a second author can rebuild the skeleton, run the checks and answer the task with no spoken setup. Missing anchors, changed semantics or evidence that cannot be found mean the card is incomplete.

Lifecycle: draft, candidate, then accepted, rejected or kept as a study. For a disposable figure reduce the card to: reader question, surface and width, relationship and grammar, hardest labels, candidate identity, result.

### ASCII skeletons

System Map. Good for service boundaries, data stores and integration points. Avoid when time order matters more than topology.

```text
+---------+      +-----------+      +----------+
| Client  | ---> | API Layer | ---> | Database |
+---------+      +-----------+      +----------+
     |                  |
     |                  v
     |            +-----------+
     +----------> | Cache     |
                  +-----------+
```

Flow Diagram. Good for ETL flows, request lifecycles and job pipelines.

```text
+--------+
| Input  |
+--------+
    |
    v
+-----------+
| Validate  |
+-----------+
    |
    v
+-----------+
| Transform |
+-----------+
    |
    v
+--------+
| Output |
+--------+
```

Sequence Diagram. Good for request and response flows, async handoffs and retry sequences. Keep actors on one line, move downward in time, keep message labels short.

```text
Client        API         Worker       Database
  |            |            |             |
  |-- request->|            |             |
  |            |-- enqueue->|             |
  |            |            |-- write --->|
  |            |<-- ack ----|             |
  |<- 202 -----|            |             |
```

Tree Diagram. Good for directory layouts, menu structures and taxonomies.

```text
project/
+-- src/
|   +-- main.rs
|   +-- lib.rs
+-- tests/
|   +-- smoke.rs
+-- Cargo.toml
```

Comparison Grid. Good for tool tradeoffs, before and after snapshots, and feature matrices.

```text
+------------+------------+------------+
| Option     | Strength   | Risk       |
+------------+------------+------------+
| ASCII      | Portable   | Less rich  |
| Mermaid    | Structured | Renderer   |
| HTML       | Flexible   | Heavier    |
+------------+------------+------------+
```

Card Strip. Good for visual metaphors, ownership or tier comparisons, and compact concept galleries.

```text
+-------------+  +-------------+  +-------------+
| In-Memory   |  | Frozen      |  | Persisted   |
|             |  |             |  |             |
|   [data]    |  |   [data]    |  |   [data]    |
|             |  |             |  |             |
| writable    |  | readable    |  | durable     |
| hot path    |  | shared      |  | on disk     |
+-------------+  +-------------+  +-------------+
```

Two-Column Compare. Good for before versus after, approach A versus B, read path versus write path.

```text
Option A: Read Optimized            Option B: Write Optimized

+--------------------+             +--------------------+
| old data on disk   |             | new data in memory |
| simpler reads      |             | faster writes      |
| slower ingestion   |             | more coordination  |
+--------------------+             +--------------------+

Tradeoff:
- left side reduces moving parts
- right side reduces write latency
```

Mechanism Trace. Good for write paths, lifecycles, and commit or state transitions.

```text
Producer sends batch
    |
    v
Step 1: journal.append(batch)    <- instant, RAM only
    |
    v
Step 2: threshold check          <- commit if size is large enough
    |
    v
Step 3: batch.freeze()           <- becomes read-safe
    |
    v
Step 4: persist                  <- data reaches disk
```

Glossary Plus Panels. Use when the topic has 3 to 6 concepts and the reader benefits from naming and visual repetition.

```text
Variation 6: Smart Pointers

These wrappers change who owns the value and where it can travel.

Box<Self>      = one owner on the heap
Rc<Self>       = many owners, one thread
Arc<Self>      = many owners, many threads
Pin<&mut Self> = writable, cannot move

+-------------+  +-------------+  +-------------+  +-------------+
| Box<Self>   |  | Rc<Self>    |  | Arc<Self>   |  | Pin<&mut>   |
|             |  |             |  |             |  |             |
| 1 owner     |  | N owners    |  | N owners    |  | fixed in    |
| heap        |  | 1 thread    |  | N threads   |  | place       |
+-------------+  +-------------+  +-------------+  +-------------+
```

Layered Walkthrough. Use when the page goes intuition first, mechanism second, or one section would be too dense.

```text
Level 1: The Essence

Every message lives in exactly one tier at any moment.

Producer                          Consumer
   |                                 ^
   v                                 |
TIER 1           TIER 2           TIER 3
+---------+      +---------+      +---------+
| Disk    |      | Frozen  |      | Journal |
+---------+      +---------+      +---------+

read direction:  ======= left to right =======>
write direction: <====== right to left ========

---
Level 2: The Write Path

Producer sends batch
    |
    v
Step 1: append(batch)           <- RAM only
    |
    v
Step 2: threshold check
```

Tall Variation Gallery. Use when each variation is small and the page should read like a field guide.

```text
Variation 1: Direct Ownership

+-------------+
| owner = one |
| move = yes  |
+-------------+

Variation 2: Shared Ownership

+-------------+
| owners = N  |
| thread = 1  |
+-------------+

Variation 3: Shared + Thread-Safe

+-------------+
| owners = N  |
| thread = N  |
+-------------+
```

### ASCII alignment examples

Glossary lines share one separator column:

```text
Box<Self>      = one owner on heap
Rc<Self>       = many owners, one thread
Arc<Self>      = many owners, many threads
Pin<&mut Self> = writable, cannot move
```

Side notes share one anchor column:

```text
Step 1: append(batch)             <- RAM only
Step 2: threshold check           <- decides commit
Step 3: persist                   <- disk write
```

Peer cards share width, height and gutter. Use parallel phrasing. No "special" middle card unless the contrast is the point.

Section anatomy: heading, short setup paragraph, figure or panel row, optional note or legend. The setup is short enough that the figure dominates.

Page composition rules: lead with a title, not a diagram; prose outside boxes; each section adds one idea; card widths and gutters stay stable; glossary separators align; `---` only for real section breaks; another section before another column.

### Playground decision packet

```text
packet_id               :
decision                : audience, uncertainty, alternatives, consequence,
                          owner, scope
kind                    : design | data | concept map | document critique |
                          diff review | code map
source_bindings         : what real source the data came from, at which revision
state_schema            : typed fields, defaults, valid combinations, version
candidate_states        : named alternatives
transition_contract     : how each control and gesture changes state;
                          what is rejected
projection_contract     : which views read state; what is approximate,
                          truncated or simulated
interaction_equivalence : keyboard or list path for every pointer action
safety_boundary         : how imported and user text stay inert
recovery_contract       : reset scope, undo, import failure behaviour
output_contract         : format, consumer, context included
persistence_contract    : where state is saved, version, migration, privacy
evidence                : checks run and results
disposition             : exploratory | modeled | interactive | reviewable |
                          accepted | conditional | rejected | superseded
invalidation_triggers   : what change makes this packet stale
```

Do not execute or ship the output of a packet still marked exploratory. A conditional acceptance records scope, owner, compensation and expiry. A rejection keeps its reason.

Pick one place where state is written: embedded JSON for a portable prototype; a separate state file for fixtures and tests; an issue or review record for approval; append-only events for audited collaboration; server state for shared mutable data. Two hand-maintained copies recreate the synchronisation problem.

State inventory before building: authoritative or source state, user state, derived state, transient state such as focus and hover, and state that needs external validation.

### Playground responsibilities

| Responsibility | Content | If omitted |
| --- | --- | --- |
| Decision | The question, audience and consumer | Controls with no purpose |
| State schema | Typed values, defaults, valid combinations, version, provenance | Drift and unreproducible results |
| Transitions | One validated path for every change | Views disagree |
| Preview or analysis | Discloses approximation, truncation, loading, error | Simulation taken as truth |
| Explanation | Why a state is invalid, partial or simulated | Silent correction |
| Output | Export with target context | A value dump nobody can act on |
| Comparison | Named alternatives, before and after | No basis for judgment |
| Recovery | Deterministic reset and undo | Lost work |
| Accessibility | Keyboard path, visible focus, programmatic name, non-visual equivalent | Core task unreachable |
| Safety | Imported and user text stay data | Script injection, broken page |
| Verification | State, renderer, output, viewport, input, error, round trip | False confidence |

### Record shapes for review playgrounds

Review comment anchor:

```text
comment_id, source_id, source_revision, side, start_line, end_line,
context_digest, target_excerpt, disposition, comment
```

A comment may be reattached only when the unchanged context matches exactly and the user confirms. Otherwise mark it stale.

Diff data:

```text
files[] -> { path, hunks[] }
hunks[] -> { header, lines[] }
lines[] -> { type: context | addition | deletion, oldNum, newNum, content }
```

Document suggestion:

```text
id, line reference, target text, suggestion, category,
status: pending | approved | rejected, user comment
```

Code map comment: stable id, target node id, label, file path, text. Concept map: nodes, typed edges, whether each came from the user or the source, and knowledge level per node, all stored outside the canvas. Layout is derived unless spatial grouping is the decision.

To seed a diff review from a real commit, read it with a command that does not change repository state:

```bash
git show <commit> --format="%H%n%s%n%an%n%ad" -p
```

Parse the result into the diff data shape and put the commit metadata in the header.

### Playground layouts by kind

| Kind | Layout idea | Non-colour cue to keep |
| --- | --- | --- |
| Design | Grouped controls beside a live component, with a toggle for light and dark context and a width control to watch reflow | Text labels on every control |
| Data | Controls grouped by source, fields, filters, grouping, ordering, limit; formatted candidate output | Explicit operator and precedence text |
| Concept map | Canvas with a sidebar listing every node, level and edge | The list carries everything the canvas shows |
| Document critique | Document with line numbers beside a filterable suggestion list with counts per status | Status text, not only a coloured border |
| Diff review | Commit header, files, hunks with old and new numbers, comment box under a line | `+` and `-` prefixes |
| Code map | Layer bands, view presets, layer and connection-type filters, comment list | Dash pattern per connection type |

Control choice by decision: chips for picking items, add-row for conditions, a dropdown per row for join or aggregate, exact number entry for limits, dropdown plus direction for ordering, toggles for on and off, clickable cards for layout structure.

Ideas for subjects: button, card, type scale, palette, dashboard density, modal (design); SQL, API endpoint, transformation pipeline, regex, cron schedule, GraphQL (data); framework learning, system design, task decomposition (concept map); skill file, README, spec, proposal (critique); commit, pull request, refactor before and after, merge conflict, per-line security audit (diff); microservices, component tree, agent system, data pipeline, plugin architecture (code map).

### Explainer inventory

One row per page, kept beside the pages:

```text
topic | act count | component types | source citations |
citations verified on | checklist walked on | stale acts
```

Staleness is per act, not per page. Citations age fastest. Re-verify them before reuse.

### Finding record

```text
status; artifact_hash; condition; location; observed_behavior;
reader_or_system_impact; evidence; responsible_layer; owner; next_action;
rerun_scope
```

### Refresh record

```text
trigger | claim affected | query or source consulted | result |
decision | impact | remaining uncertainty
```

Field detail: the trigger is a changed source, product, example, command or reader check. The claim is the exact statement with its evidence label. The query entry holds the text, restrictions, date and tool. The result holds authority, version, passage and conflicts. The decision is one of preserve, revise, narrow, route or retire. The impact lists dependent sections, examples, derivatives and the gates rerun. The uncertainty lists what was not inspected or not resolved.

## Worked Example Set

"Borderline" below means accepted for a declared audience at a known cost. Classify an artifact by its highest unresolved risk to meaning or access, not by its average. Uneven spacing may not block an internal draft; an invented guarantee or a caveat nobody can reach does. A check that was only imagined is not collected evidence. Presence of an element in the DOM is not comprehension.

### ELI5: AI-native engineering, full note

The note follows the five-heading output shape. Its headings are shown one level down so that they nest here; use `#` and `##` in a real note.

**Getting good help from an AI coding assistant**

#### Big Idea

AI coding works better when we make the work easier to understand: clear names,
tests before code when possible, short notes, and big jobs split into small ones.

#### Why It Matters

Think of a very fast helper who has read a huge part of the internet. It guesses
from patterns. Vague instructions confuse it. It forgets the older parts of a long
conversation. It does better when the task is clearly labelled. So do not just ask
the AI to be smart. Shape the work so the AI can succeed.

#### Core Ideas Made Simple

1. Names are drawer labels. A clear name tells people and the model which drawer
   to open.
2. Tests are the answer key before the exam. They say what success is, what goes
   in and what comes out. The work becomes less like guessing and more like
   filling in a known shape. The answer key only covers the questions on it.
3. Summary notes are bookmarks. Write down what was decided, what is left to do,
   and which mistakes to avoid, because long chats forget.
4. Self-checking is talking out loud. Ask the model to explain its reasoning,
   what could be wrong, and which edge case it missed.
5. Old bugs are warning signs. Keep a list, like bright tape where people tripped.
6. Context is a backpack, not a dump truck. Pack the relevant files, keep
   summaries handy, move old details into documents. Unlike a backpack, clutter
   can hurt even when it fits.
7. Agents need a real workspace: files, a shell, scripts and small tools. Real
   work happens on a computer, not inside one giant prompt.

#### Tiny Example

Vague: "Make this better and faster."

Clear:
- Write `filter_implementation_entities_only()`.
- Write the test first.
- Return only implementation entities.
- Preserve order.
- Return an empty list when nothing matches.

The clear version leaves much less room to drift.

#### What To Remember

Clear names, tests, checkpoints, boundaries. Claims of faster development, fewer
bugs or better onboarding are claims until you measure them in your own project.
The better you package the task, the better the AI can help.

### ELI5: three explanations graded

Context.

- Good: "Start with the changed function, its direct callers, the affected tests and the error path. Widen when you hit a dependency or an uncertainty. Stop when the conclusion is supported by the source and the remaining uncertainty is named."
- Bad: "Give the model everything." This mistakes volume for coverage.
- Borderline: "Only direct callers and tests." Too rigid; some changes need an indirect file.
- Test it with relevant, indirect, unrelated and stale files mixed together.

Tests.

- Good: a test is a question you can inspect plus a correction signal. Failing run, smallest passing change, refactor while green. It does not prove requirements nobody tested.
- Borderline: "Tests are the model's answer key", unless gaps and refactoring are explained.

Naming.

- Good: a name made of action, scope, target and qualifier works like a search query. Four words is a local heuristic. Keep short idioms. Do not pad.
- Bad: "Exactly four words makes development 67% faster."

Mixed request (context offloading plus recovery): explain how durable state moves into files, then hand off to the runbook for the recovery procedure.

### Analogies graded

| Grade | Analogy | Why |
| --- | --- | --- |
| Good | "Context is like a backpack: capacity is limited, so choose relevant material; unlike a backpack, distracting text can degrade attention even when it fits." | States mapping and non-mapping |
| Good | Microphone in the database room versus checking a mailbox, for change streams versus polling | A deliberate contrast that preserves push versus poll |
| Good | A backpressure metaphor that keeps the feedback from consumer to producer | Preserves the mechanism |
| Bad | "AI forgets like a child." | Cute, wrong, no mechanism |
| Bad | A car for a queue | Relatable only |
| Borderline | One concept with two redundant metaphors | Keep the stronger one |

Other mappings from the sources: polling as a postal worker checking a mailbox; a plugin system as USB devices that plug in and are recognised; a retry protocol as a bank transaction where money moves only if both sides agree.

Exercise: map three unfamiliar mechanisms to metaphors, then write for each what maps, what does not, and where it stops. Grade the mapping.

### HTML explainer graded

- Good: a six-act page on where an ingestion worker resumes after a crash. Poll, transform, apply, persist appears in Act II. Unsupported exactly-once wording is excluded. One comparison, one branch view, one excerpt.
- Good: an eight-act explainer of a queue subsystem, opened in a browser and walked against the checklist. The new hire later asks questions by act number.
- Bad: a page built from a README and file names. Seven scaffold acts, invented symmetric paths, a metaphor used as storage semantics, sections hidden behind scroll scripts, a footer citing only a root folder.
- Bad: styling started before the code was read.
- Borderline: the happy path is supported but there is no evidence for recovery, and a restart arrow implies a recovery point. Narrow the scope or get the evidence.
- Fits one page: two adapters compared on shared setup, state and recovery. Overloaded: a tutorial, an API reference, a dashboard and a simulator for three systems.

### ASCII: a request with a retry branch

Good. A vertical spine; the timeout branch leaves from the step that owns it; detail is routed elsewhere.

```text
+---------------------+
| Accept and validate |
+---------------------+
           |
           v
+---------------------+   timeout    +--------------+
| Call upstream       | -----------> | Retry policy |
+---------------------+              +--------------+
           |
           v
+---------------------+
| Classify result     |
+---------------------+
           |
           v
+---------------------+
| Persist and reply   |
+---------------------+

Retry limits and backoff -> see "Retry policy" appendix.
```

Bad. Retry looks like a mandatory step.

```text
[Accept] -> [Call] -> [Classify] -> [Retry] -> [Persist] -> [Reply]
```

Borderline. At 72 columns the pairs are merged. Acceptable for an on-call reader who knows the steps. Wrong for onboarding.

```text
+----------------------+      +----------------------+
| Accept + call        | ---> | Classify + persist   |
+----------------------+      +----------------------+
           |
           +-- timeout --> [Retry policy]
```

Why the good version works: the common path is uninterrupted; the branch begins at its cause; the omission route is explicit; equal widths and a centre anchor expose drift; retry is not implied to be mandatory. Why the bad one fails: tidy symmetry makes retry look mandatory, hides where the timeout originates and where the policy lives, and real labels would overflow or shrink into opaque abbreviations. The borderline version is wrong for onboarding or incident analysis unless prose restores the merged distinctions.

The fixed reader question for these three is "Where can an async request stop, and where does retry enter the path?" They teach flow, exception routing and constrained disclosure. They are not studies of a tree, a dense matrix or a full page.

Keep examples as regression fixtures. Keep the source and the longest labels with them. Growth of a label such as `Call upstream`, or moving retry onto the spine, triggers the checks even when the prose is unchanged. Preserve the task and the semantic assertions; change the drawing only when the fixtures pass more clearly. Character, width and fence results are deterministic. Balance, disclosure depth and comprehension are editorial observations bounded by audience and terminal. A retired example is archival, with its identity, surfaces and observation date, and is not normative after the contract or environment changes.

Other gradings: five calm screenfuls with no line over 84 columns is good; one 120-column sequence carrying everything is bad; a five-node orientation map with a link to an authoritative explorer is borderline. If a fact appears in the setup, the figure and a note, choose one owner for it. Short two-line peer attributes inside a box are fine. A continuous trace may stay dense if a break would cut causality. A 96-column page is valid once it has been verified on its surface.

### Playground graded

- Good (data): validated query tree, escaped literals, an explanation for an unsupported join, named alternatives, an export with schema context, acceptance by the target parser.
- Bad: unlabelled sliders, raw values dumped into a prompt, no reset, one wide viewport.
- Conditional: a one-time code map is orientation only, and only when every edge has provenance and a scan revision.

Design explorer. Use the real content, token-backed shape, elevation and density, every component state, and responsive content. Named reviewed presets keep undo. Reject a design that overlaps or loses focus under long content, narrow width, keyboard use or an error state, even if the default looks polished.

Concept map. Nodes, typed edges, user versus source provenance and knowledge levels live outside the canvas. A searchable list supports focus, edge creation and deletion, knowledge changes, bounded movement and export. A list that can only be read is not equivalent exploration. Export a learning request that lists what the user knows, is unsure of and does not know, plus the relationships they drew.

Review. Use the anchor record in Theme Specific Artifact. Build the output from approved items and comments, grouped as approved changes, further feedback, and rejected items kept for context.

Imported data. Labels and literals stay strings. Escape for the target dialect. Render with text nodes. Preserve and report malformed state. Hidden controls must not change the export. Clipboard denial exposes selectable output.

Export wording. Compare each value with its default and mention only what changed. Pair numbers with a plain word, as in "a pronounced shadow (24px blur)". For a design export, match the project's styling system. For a data export, describe what to build and include the schema context instead of pasting only the raw query.

## User Journey Scenario

These journeys are illustrations from the sources, not observed sessions.

### Onboarding a new teammate on a subsystem (HTML)

1. Explore structs, flow and error paths. Collect file and line citations.
2. Plan seven acts from the concept arc, not the file tree.
3. Give each concept a metaphor and its limit.
4. Adapt the template: colours, titles, navigation dots.
5. Write to `.prd/ELI5/`.
6. Walk the checklist with the page open.

Each stage feeds the next: citations become act evidence, acts become navigation dots, techniques become checklist conditions. A good result is a new hire who asks questions by act number.

### Predicting restart behaviour (HTML)

A new teammate must predict where an ingestion worker resumes after a crash. Success: trace discovery to transformation to application, identify durable progress, predict the restart point.

HTML is chosen over long Markdown because it controls the order of introduction. A dashboard is rejected because it shows current state, not recovery reasoning. Six acts: mystery; the source-named loop; tentative versus durable state; the crash branch; ownership; failure tradeoffs and compression. Do not infer exactly-once from the existence of retries.

Verification catches loose persistence wording and a state table that overflows on a narrow screen. If the reader predicts "it never repeats after application", strengthen the state act and test again. If no reader is available, record comprehension as `not_evaluated`.

### An async request path for an operations reader (ASCII)

The reader arrives cold. Surfaces: raw Markdown and an 84-column terminal. They must be able to say who accepts the request, where work queues, when persistence happens, why a 202 comes before completion, and where to look after a failure.

A Layered Walkthrough is chosen: essence, components, actor exchange, mechanism trace, failure notes. Hard canvas 84, prose 60, two-space gutters, one side-note column. The page skeleton in SKILL.md is the first three layers of this page.

The journey is hypothetical. It is not measured reader evidence.

1. Intake: state the audience, the operational question, the surfaces and the authoritative facts. Send domain correctness to technical review before any layout polish.
2. Outline: compare a layered walkthrough with a mechanism trace and pick one. Add a glossary only when vocabulary blocks the mechanism. Merge repetition. Split topology from time.
3. Grid: stable actor anchors. Tighten or stack before widening.
4. Figures: a system map for components, a sequence for messages, a mechanism trace for worker persistence. Replace an all-in-one sequence when labels wrap or paths cross.
5. Convergence: freeze the width and the system; shorten nouns; put actions on arrows; keep paragraphs outside figures; align repeated actors. Go back to the outline if the prose narrates every line or the sections redraw unrelated grammars.
6. Acceptance: the validator with `--editorial`, a copy on each promised surface, and questions to the target reader about direction, ownership, when the reply returns and where to inspect a failure. A mechanical pass with wrong answers needs a repair to meaning or vocabulary.

Good outcome: the reader predicts that the API returns before the worker persists, and finds the failure note unaided. If a reader cannot explain a term, add the smallest glossary layer. Keep the widths, the choices made, the validator result, the reader questions, the omissions and one informative rejected skeleton.

### A read-only SQL report (playground)

Decision: which report query to hand to the data owner. Inputs: a versioned schema and synthetic rows. Nothing runs against production.

State: schema revision; source and selected fields; typed joins; a filter expression tree; grouping; aggregates; ordering; limit; candidate name and version. Example conditions: `customers.status = active`, `orders.status = paid`, `orders.created_at` on or after 2026-01-01, group by customer id and region, order by paid total descending, limit 100.

Controls: searchable typed fields, relation-aware joins, typed values, explicit precedence, keyboard reordering, exact date and limit inputs. Invalid rows keep the input and explain the repair. Arbitrary cross-table strings and slider-only exact values are not supported. Candidates are compared only across compatible schema revisions. The target parser and the reviewer own the validity of the query and its business meaning. The serializer and the plain-language explanation both read the tree. Parser evidence is bound to the state digest, the schema revision and the dialect. Hidden panels cannot affect the export.

Tests: markup in literals; wrong aggregation type; missing grouping; a delayed, stale parser response; clipboard denial with manual selection; preset then undo restores the whole tree; old saved state whose types changed; keyboard and high zoom; narrow, tablet and wide.

Good outcome: every projection agrees, literals are inert, the keyboard task completes, the parser accepts the exact output, and the data owner accepts the meaning. A schema change invalidates only the affected candidates. A remote query plan is scoped evidence and never authorisation to run in production.

### An ELI5 note in six stages

1. Frame the reader, the decision and the consequence.
2. Map the evidence and label it.
3. Build the mechanism before the analogy.
4. Test with teach-back and an unseen case.
5. State the action, when to widen and when to stop.
6. Preserve sources, uncertainty, owner and refresh triggers.

If teach-back fails, repair the earliest faulty assumption and do not append detail. Reversed causality: fix the core model. Undefined term: fix the definition. Wrong choice on a new case: add a contrasting example or rule.

Worked rule for stage 5, on choosing context for a code change: start with the changed function, its direct callers, the affected tests and the error path. Widen when a dependency or an uncertainty appears. Stop when the conclusion is supported by the source and the remaining uncertainty is named. A security review may need broader policy and threat evidence from the start.

A good outcome is a correct action on a changed case and a handoff to the right authority. Liking the story or repeating it is not the outcome. Compress the stages for low risk. Add expert review when uncertainty or consequence is high.

## Anti Pattern Registry Table

Diagnose in this order: source model, narrative, component, surface. Machine scans find tokens, attributes, links, syntax and overflow. Humans find wrong causality and false symmetry. Target readers show comprehension.

The presentation failures share one root. Definition-first openings, abstractions before concrete cases, dense acts and bare unlabelled code are how a subject looks to someone who already knows it. The teaching rules deliberately invert an expert's defaults, so they work as a checklist against the curse of knowledge. Definitions are how experts start and how novices stop reading, which is why the first author check is the mystery opening. Authors who already know the abstraction resist concrete-before-abstract the most, so a reviewer should expect that and check for it. Explanation before understanding differs in kind: the other rows degrade presentation, that one makes the content wrong (see "The core trio").

### All modes and ELI5

| Anti-pattern | Repair |
| --- | --- |
| Explanation before understanding | Return to the source; no styling until the loop is found |
| Context-free summary | Name the reader and the decision |
| Unsourced recommendation | Attach a source check, reader exercise, observable result or named authority |
| Unverified agent instruction | Add a command or reviewer question |
| Wrong but cute simplification; analogy overreach | State mapping, non-mapping, stopping point and a counterexample near the boundary |
| Jargon substitution or jargon flood | Plain words first; define each exact term once |
| Hype as explanation | Mechanism, then attributed evidence, then uncertainty and project scope |
| Audience-free explanation; audience averaging | One reader; split for the second |
| Source list without synthesis | Write the claim each source supports |
| Actionless summary | End with a rule, an example, a limit and an observable completion check |
| Slogan without causal steps | Add the steps |
| Definitions before the mystery | Open with the problem |
| Ending without a summary and takeaway | Add both |

### HTML explainer

| Anti-pattern | Repair |
| --- | --- |
| Visual confidence without evidence | Claim ledger; visible uncertainty |
| Heartbeat buried after context | Move the loop to Act II or earlier |
| Metaphor replaces mechanism | Follow each metaphor with exact mechanics; remove it if the page fails without it |
| Code before intuition | Concrete case or metaphor first |
| Two concepts in one act | Split at the motivation and mechanism seam |
| Scaffold residue as fact | Residue scan and human read |
| Forced symmetric comparison | Compare only shared decision dimensions; give space by evidence |
| Omitted comparison when alternatives exist | Add side-by-side cards |
| Component gallery; single-component monotony | Keep the lowest-complexity component with a unique role; vary where the content varies |
| Code dump; unlabelled code block | Short, labelled, interpreted excerpts |
| Script-gated essential content | Visible semantic order by default; enhancement optional |
| Motion without reader control | Reduced-motion rule |
| Narrow viewport overflow | Reflow grids, contain code and tables, wrap long identifiers |
| Source footer without traceability | Inline attribution for disputed or surprising points |
| Template overwrite or orphan | New or disposable path; keep the command and source list; confirm overwrite refusal |
| File-tree tour | Re-plan from the concept arc |

### ASCII page

| Anti-pattern | Repair |
| --- | --- |
| Unicode leak | Replace with the ASCII vocabulary |
| Tabs or trailing spaces used for alignment | Spaces only; strip line ends |
| Width overrun | Shorten wording, stack, or declare and verify a wider canvas |
| One giant figure | Split by job |
| Paragraph inside a box | Move prose out; keep labels |
| Ambiguous connector crossing; diagonal connectors | Reroute; at most one bridged crossing, and only after a reader confirms it |
| A label floating between two arrows | Attach it to one |
| Mixed visual grammar | One vocabulary; a section break before changing figure type |
| Panel grid drift | Rebuild the row on one width and gutter |
| Random centring | Align to the column system |
| Prose duplicates the figure, or the figure needs line-by-line narration | Prose states purpose, figure shows structure, notes interpret exceptions |
| Screenful blob | One job per 20 to 40 lines |
| The same word repeated in every node | Move it to the heading |
| Decorative art | Remove it |
| Horizontal panning | Stack vertically |

Repair order: hard portability, then width and page structure, then figure pattern, connectors, grid, labels, prose. Keep the failing copy at its target width while you repair. Validate again after copying into the promised container.

Diagnose the earliest broken layer (medium, canvas, page system, local pattern, connector path, grid, labels, prose or evidence) from an observable signal of portability, ambiguity or reader cost. A wrong page system can cause every downstream defect. An unconventional composition is not a defect by itself.

Boundaries on the rows above:

- Generic advice with no source decision behind it: load the relevant sources and trace the rules. Skip a source only with a reason showing that no decision could reverse.
- A universal-sounding claim about width or readability: separate fact, observed behaviour and judgment. A preference that is named and owned is allowed.
- Advice with no validator, target copy or reader question: tie material advice to mechanical or comprehension evidence. A draft may defer the gates and cannot claim acceptance.
- When Unicode is truly required, use another declared medium. Tabs and line-end padding have no exception under strict file portability.
- A verified 96-column comparison is valid when the surfaces support it. An overview may summarise a large figure when it states what it leaves out.
- A composed page may change grammar between layers. Asymmetry in a panel row is valid only when it encodes a named difference the reader perceives. Centring is for a headline, not for arbitrary blocks.
- Duplication test: if removing either the prose or the figure loses nothing, one of them is redundant.

A tiny figure needs the ASCII, width, direction, pattern-fit and raw-text checks. An editorial page adds grid, screenful rhythm, repetition, full-scroll and cold-reader evidence.

Signs that a composed page has failed: a page dump; vocabulary that changes by accident; nodes filled with paragraphs; drifting widths; prose that narrates every connector. Each screenful adds one layer without sending the reader back to an earlier figure. Mechanical confidence (characters, tabs, trailing spaces, widths, editorial heuristics) is a different thing from explanatory confidence (a cold reader understands).

### Playground

| Anti-pattern | Consequence | Repair or exception |
| --- | --- | --- |
| Topic without a decision | Controls with no downstream action | Name decision, audience, consequence, consumer. Open-ended art is an explicit exception |
| Kind chosen by visual similarity | Domain meaning lost | Choose by semantics; hybrids need explicit contracts |
| Control theatre | Preview or export ignores a control | Remove it or connect it through state |
| DOM as source of truth; parallel state islands | Drift after filter or re-render | Structured state and validated transitions. Focus and hover may stay transient |
| Silent invalid normalisation | Intent clamped, reordered or dropped without notice | Reject or show the invalid state. Formatting-only normalisation is fine |
| Hidden default dependency | Consumer reproduces a different result | Include baseline identity or full state |
| Random presets; destructive preset apply | Arbitrary comparisons; lost work | Reviewed whole-state presets, undo or a warning |
| Reset that does not reset | Visible and saved defaults diverge | Name the scope; rebuild defaults atomically |
| Preview as authority; stale preview shown as success | Simulation or old data looks current | Label approximation and revision; cancel, refresh or mark stale |
| Raw markup rendering | Imported text executes or corrupts the page | Text nodes or a reviewed sanitiser |
| Regex as a domain parser | Escapes and nesting handled wrongly | Typed parser or tokenizer; a tiny tested mini-language at most |
| Pointer-only manipulation; colour-only state | Keyboard, touch and colour-blind users lose meaning | Focusable list, keyboard actions, names, announcements, text or shape redundancy |
| Layout equals relationship; unvalidated edges | Proximity becomes false architecture | Store typed edges; validate endpoints, direction, type, duplicates, self-edges, hidden nodes |
| Fuzzy review anchor | Feedback drifts after edits | Revision, side, range, context digest; otherwise stale |
| Timestamp comment identity | Collisions on import or concurrency | Stable collision-resistant identifiers. Simple ones only for comments that are never merged |
| Value dump; prompt-only completion | Consumer lacks intent and structure | Domain-language or structured export |
| Fake copy success | User believes stale or empty text was copied | Await the result, show failure, keep selectable output |
| Unversioned browser storage; share-link leak | Corruption on upgrade; private data in a URL | Version, validate, migrate or reject; opaque identifiers |
| Render everything on input; focus lost on re-render | Lag, races | Debounce, cancel, coalesce; stable regions; restore focus on purpose |
| Happy-path first frame only | Empty, loading, error, zoom and mobile failures hidden | A state by viewport matrix |
| Single-file dogma; accidental external dependency | Unreviewable shared artifact; blank page offline | Choose architecture from the boundary; bundle, provide a fallback, or disclose |
| Too many controls | Nobody finds the decision | Group by concern; fold away advanced ones |
| Empty or broken first load | No starting point | A coherent default state |

Repair order: contain unsafe or private content; preserve the revision, state and output; stop misleading authority; repair the domain model; restore canonical transitions; add safe and equivalent interactions and explicit states; repair projections, output, persistence and consumer validation; add regression fixtures.

## Verification Gate Command Set

All commands assume the working directory is this skill's folder unless a path says otherwise.

### What each check can and cannot show

| Claim | Check | Limit |
| --- | --- | --- |
| Characters and whitespace are clean | ASCII validator | Says nothing about meaning |
| Canvas and prose widths hold | Validator with explicit limits | The destination may wrap differently |
| The page is composed | `--editorial` plus a full-scroll read | Heuristics are not teaching quality |
| It renders on the target | Paste raw text into every promised surface; open HTML from disk | A screenshot is a diagnosis; the text or file is the deliverable |
| Structure and residue of an HTML page | Residue and structure scans | Not full HTML validity; presence in the DOM is not comprehension |
| The reader understands | Reader names type, direction, main path, key relation and next action; or restates and predicts | One reader is one observation |
| Claims are true | Reviewer checks claims against sources, in both directions | Needs someone who knows the code |

### ASCII

```bash
# Long page
python3 scripts/check_ascii_diagram_quality.py page.txt --max-width 84 --max-prose-width 64 --editorial

# Compact terminal output
python3 scripts/check_ascii_diagram_quality.py page.txt --max-width 72 --max-prose-width 60 --editorial

# Single figure, from standard input, machine-readable
python3 scripts/check_ascii_diagram_quality.py - --max-width 84 --json < figure.txt

# Independent byte check: must print nothing
LC_ALL=C grep -n -P '[^\x00-\x7F]|\t| +$' page.txt

# Lines over the canvas: must print nothing
awk '{ if (length($0) > 84) print FILENAME ": " FNR ": " length($0) }' page.txt
```

What the validator reports:

| Kind | Meaning |
| --- | --- |
| `empty` | No content |
| `structure` | No box or connector characters at all |
| `tab` | Tab character |
| `trailing_whitespace` | Spaces at a line end |
| `width` | Line longer than `--max-width` (default 100) |
| `non_ascii` | Non-ASCII character, with column |
| `composition` (editorial) | A page of ten or more lines with fewer than two blank lines, or fewer than two blocks |
| `setup` (editorial) | No prose or glossary block without connectors |
| `diagram_zone` (editorial) | No block that is a diagram |
| `glossary_alignment` (editorial) | ` = ` columns drift by more than one within a block |
| `side_note_alignment` (editorial) | `<-` columns drift by more than two within a block |
| `prose_width` (editorial) | A prose line longer than `--max-prose-width` (default 64) |
| `panel_width` (editorial) | Two or more box borders on one line with different widths |
| `gutter_alignment` (editorial) | Gaps between boxes on one line drift by more than one |

Mutation test for the checks themselves: insert a tab, a Unicode border, a longer label, a reversed arrow, a broken fence or a stale route; confirm the matching detector or reviewer catches it; remove the mutation; confirm the pass returns. Do not claim wider coverage than the mutations tried.

Stress probe before acceptance: try one narrower preset, or lengthen the hardest realistic label. The page must stack or reflow without changing meaning, or fail with a stated boundary. Keep a representative failed width or reader case as a regression fixture when it is likely to recur.

While drafting, run the cheap ASCII and width checks. At candidate stage add the target copy and the reader check. The packet records path, revision, widths, the exact command, the result, the surfaces, the questions, the verdict and the uncertainty. Exit status zero and an attractive screenshot are not enough. A screenshot supports diagnosis; the raw text is the deliverable.

Review checklist, first pass: figure type identifiable in under five seconds; reading direction obvious; makes sense as raw text; strict ASCII; composed, not dumped; whitespace gives the eye a rest; each section has one job.

Layout: within the width budget; prose within its width; main path straight; related boxes aligned; crossings minimised; overloaded figure split; prose and figure in their own zones; repeated concepts aligned in a row or column, not staggered; repeated cards the same width and height; each screenful coherent.

Labels: short box labels; actions on arrows; no word repeated in every node; legend only when abbreviations or symbols would confuse; side notes shorter than the annotated line; glossary separators aligned.

Finish: readable in a monospaced block; structure clear without explanation; labels short and specific; survives copying; validator clean, including `--editorial` for a page; composition deliberate across the whole scroll.

Mechanical statements and judgments are different kinds of evidence. "Longest line is 83 under an 84 contract" is mechanical. "The timeout branch competes with the main path" is judgment. Record both.

### HTML explainer

Gate A, generator preflight. Proves the generator, not the story.

```bash
python3 scripts/create_elegant_explainer_html.py --output /tmp/explainer-preflight/index.html \
  --hero-title "Preflight <b>&" --hero-subtitle "Check" --source a/b.rs
grep -n 'Preflight' /tmp/explainer-preflight/index.html     # title must appear escaped
python3 scripts/create_elegant_explainer_html.py --output /tmp/explainer-preflight/index.html \
  --hero-title "Preflight" --hero-subtitle "Check"          # must refuse: file exists
```

Gate B, residue and structure. Use the two scans in SKILL.md. `rg` may replace `grep -E` in the residue scan.

Gate C, rendered behaviour. Open from disk, and over HTTP if it will be deployed. For each declared target record pass, fail or `not_evaluated`:

- desktop and narrow widths: no clipping, no hidden caveat, no uncontrolled sideways scroll;
- keyboard: order, visible focus, nothing depends on hover;
- reduced motion;
- scripts off or failing;
- fonts and media unavailable;
- console and network;
- source truth: sample claims against sources in both directions;
- for consequential onboarding, a reader restates the mechanism and predicts an outcome.

Evidence packet for a page that matters: artifact hash, exact commands, working directory, browser and version, targets, outcomes, screenshots that prove a finding, unresolved risks. Any byte change invalidates the visual evidence it affects.

```bash
sha256sum .prd/ELI5/index.html
google-chrome --version
```

The ten author checks from the older HTML skill, split by kind. Reading checks: mystery opening; metaphor before code; one concept per act; at least three component types; side by side where two or more approaches exist; code blocks labelled; ends with a summary table and one-line takeaway. Interaction checks: navigation dots match acts; scroll reveal works; the page opens in a browser. These verify structure and behaviour, not truth. In a headless environment the interaction checks are deferred to the first human view and reported as deferred.

### ELI5

Six review passes: reader and decision; claim trace; analogy correspondence; examples and counterexamples; teach-back and a new case; delete prose that adds neither fidelity, understanding nor action.

```bash
# Numbers and strong verbs to audit by hand: each hit needs attribution or removal
grep -n -E '[0-9]+ ?%|[0-9]+x\b|always|never|guarantee|proves|prevents' note.md
```

### Playground

Find what the target project already has before choosing tools. File names alone are not evidence; open what you find.

```bash
rg --files | rg '(^|/)(package.json|vite.config|playwright|cypress|tests?|src|public|fixtures?|schemas?|workflows?|design-tokens|stories)(/|\.|$)'
```

Static scan of a single-file playground. Each hit needs a reason or a fix:

```bash
grep -n -E 'innerHTML|outerHTML|insertAdjacentHTML|document\.write|eval\(|Date\.now\(\)|https?://' playground.html
```

Gates: schema, default, preset and import validity; every adapter goes through one transition function; all projections agree; hostile text stays inert; the exact consumer accepts the export; the whole task completes by keyboard; direct manipulation has an equivalent; responsive, zoom and lifecycle states; for canvas or SVG, both the pixels and the structured data; honest clipboard fallback; persistence and migration; stable anchors and stale handling; stale async results rejected; for a deployed tool, the production build at its served address.

Fixtures: default; each preset; minimum and maximum; long text; empty; invalid; old, corrupt, oversized and privacy-sensitive saved state; stale source; hostile markup; keyboard only; reduced motion; high zoom; clipboard denial; timeout; consumer rejection.

Ladder, cheapest first: parse schemas and versions; apply every adapter and compare state; compare controls, preview, explanation, export and saved state; hostile and malformed input; keyboard and list paths; preset, undo, reset, import, stale, cancel and clipboard failure; persistence, migration and privacy from a clean profile; the exact consumer; source or schema invalidation; reconstruct the rationale without the browser.

Recovery drill: record a known-good state; trigger the failure; assert no prohibited effect and no state loss; inspect status, focus and next action; exercise retry, cancel and rollback; compare projections; confirm diagnostics omit sensitive payloads; repeat under rapid changes; keep the fixture.

### Observations made while assembling this skill

These were made once, on one Linux machine with headless Google Chrome, against the bundled files. They are observations, not guarantees for other environments.

| Check | Result |
| --- | --- |
| Generator with `--hero-title "Preflight <b>&"` | File created; title written as `Preflight &lt;b&gt;&amp;` |
| Generator run again on the same path without `--force` | Refused with exit code 1 |
| Structure scan on the unedited scaffold | Fails: unscoped `.reveal`, no reduced-motion rule, residue lines |
| Scaffold with its scripts removed | Computed opacity of the first `.reveal` block is 0: act content is invisible |
| Same after the hardening step in SKILL.md, scripts removed | Computed opacity is 1 |
| Hardened scaffold with scripts on | Blocks in the viewport gain `visible` and opacity 1, the same as the unhardened file |
| Structure scan after hardening, both templates | Passes apart from scaffold residue |
| ASCII page skeleton in SKILL.md | Validator passes at `--max-width 84 --max-prose-width 64 --editorial` |
| A line containing a tab, piped to the validator | Fails with `tab`, exit code 1 |
| Playground skeleton in SKILL.md | Markup typed into the title shows as text; out-of-range radius is limited with a notice; preset and reset change the export; clipboard failure shows the failure message |

Not evaluated: keyboard focus order in a headed browser, the reduced-motion setting in a real browser, any browser other than Chrome, macOS `sed`.

## Failure Mode Table

Classify by the earliest cause you can control and keep the reader-visible symptom on record. Lifecycle: detect, stop reuse, preserve the failing copy, find the owner, make the smallest causal repair, rerun the failed gate and every check the repair invalidated, then inspect derivatives. Several small failures can add up to a failure of the essential path.

### All modes and ELI5

| Failure | Signal | Response |
| --- | --- | --- |
| Source drift | Citations no longer match the code | Block the affected claims; re-read; revise dependents |
| Generic advice | No command, reviewer question or metric attached | Attach one or delete |
| Implicit decision path | Reader cannot say what to do next | State the action, when to widen, when to stop |
| Wrong analogy | Reader predicts the wrong outcome | Replace it; do not soften it |
| Confidence escalation | "May" became "does" between source and page | Restore the source's strength |
| Audience averaging | Too basic and too dense at once | Pick one reader; split |
| Teach-back without transfer | Reader repeats the words but fails a new case | Add a contrasting case |
| Wrong authority | A writing guide cited for a performance number | Cite the governing source or drop the claim |
| Verification theatre | Checks listed but not run | Record commands and results, or `not_evaluated` |
| Proxy metric | Length, views or satisfaction used as proof | Use reader outcome |
| Stale derivative | A copy or screenshot outlives a correction | Find and update or retire copies |
| Dead-end route | "See the runbook" points nowhere | Exercise the route |
| Lost plan in a long session | Steps repeated or skipped | Keep the brief on disk; re-read before destructive steps |
| Exploration fan-out | Sub-agents return more than can be used | Cap the scope; assign ownership |

Close a failure only when a changed representative case passes, the evidence and source status are correct, the file checks and the required route pass, and any severe risk is still watched. A failure that recurs points upstream: to provenance, to two authorities that overlap, to the audience model, or to ownership.

Four ways the method itself decays: the template is lost; the method is superseded without notice; the teaching rules are diluted into friendly summaries; the format is copied without the exploration. To check a variant, look for the understanding-first mandate, the ordering rules, the gate set and file-and-line evidence. Stage order is the tripwire: a variant that opens with components licenses explaining before understanding. A diluted retelling that still links the original is recoverable. How often the format is copied without exploration is unmeasured.

### HTML explainer

| Failure | Response |
| --- | --- |
| False high-consequence claim | Remove or correct at once; if already shared, correct linked documents, tell readers, retire stale screenshots, publish the superseding page |
| Source drift | Re-verify per act; mark stale acts |
| Hidden conflict between sources | Show the conflict on the page |
| Outcome mismatch | Return to the brief; the page answers the wrong question |
| Scaffold semantics kept | Residue scan; re-derive the act from sources |
| Essentials hidden behind a script | Make content visible by default |
| Keyboard or focus break | Use links or buttons; visible focus |
| Reduced-motion disorientation | Add the media rule; drop smooth scrolling under it |
| Narrow-screen distortion | Reflow; contain code and tables |
| Optional asset turned out to be required | Provide a fallback or remove the dependency |
| Irreproducible build or overwrite risk | Keep the command; write to a new path; confirm refusal without `--force` |
| Stale evidence | Bind evidence to the artifact hash; redo after changes |
| Ownership collision | One writer per file; stop and resolve |

Containment first, then the durable response:

| Failure | Contain | Durable response |
| --- | --- | --- |
| False high-consequence claim | Withdraw or block sharing | The subject owner supplies evidence or narrows the claim; reconcile diagrams and takeaway; resample the affected reader prediction |
| Source drift | Mark stale; restrict use | Trace source to claims, acts, components and gates; record old and new compression sentence, hashes, checks and uncertainty |
| Hidden conflict | Restore the disagreement | Route by owner (method, subject or rendering); resolve or keep a bounded unknown |
| Outcome mismatch | Do not claim comprehension | Find the earliest misunderstood relation; retest the same task on the new hash |
| Scaffold semantics | Remove, or label incomplete | Rebuild from subject evidence; scan, then review the categories by hand |
| Essentials hidden by script | Disable the hiding, or give a static fallback | Visible by default; prove reachability with scripts off and on script failure |
| Keyboard or focus break | Static equivalent, or remove a nonessential control | Semantic controls, visible focus and order; rerun the keyboard path |
| Reduced-motion disorientation | Disable transitions | Preference-aware implementation; verify the same meaning and order |
| Narrow distortion | Narrow the support promise, or give an alternate representation | Reflow or contain with no silent change of priority; rerun dependent proof |
| Optional asset required | Fallback or remove | Or document the required runtime, privacy and loading; block the resource and verify meaning, layout and console |
| Irreproducible or overwrite risk | Preserve the bytes | Record invocation, environment, dependencies and hash; reproduce in a fresh temporary directory; confirm refusal |
| Stale evidence | Mark stale | Analyse impact; recollect under the current hash and conditions |
| Ownership collision or absence | Freeze overlapping writes | Exclusive paths, escalation, checkpoints, one final verifier |

A warning does not neutralise a contradiction that dominates the page visually.

### ASCII page

| Failure | Response |
| --- | --- |
| Source-boundary drift | Block affected claims; restore labels from the source |
| Wrong grammar | Return to the reader's question; test the figure with labels temporarily removed |
| Label or canvas overflow | Freeze the longest labels and the surface; shorten without losing meaning, wrap on purpose, widen within the contract, move detail elsewhere, or split |
| Grid or connector ambiguity | Stop nudging locally; rebuild the grid and reattach from named points |
| Character or whitespace leakage | Inspect bytes; replace Unicode, tabs, trailing spaces and mixed line endings |
| Markdown breakage | Repair unclosed fences, table shape or heading order before judging appearance |
| Target-render mismatch | Reproduce the exact copy under the destination's rules; adapt or route |
| Reader-comprehension failure | Keep the observation; test wording, emphasis, order and grammar; ask the same question of a comparable reader |
| Stale route or evidence | Repair the route; exercise the destination, not only the path text |
| Unbounded variant search | Stop generating; return to the run card; compare only named tradeoffs |

For an unknown cause run a discriminating probe. For a clipped label, compare bytes, measured width and render before blaming the copy step or the renderer.

### Playground

| Failure | Signal | Response |
| --- | --- | --- |
| State divergence | DOM, canvas and state disagree | Stop export and save; keep the canonical candidate; reconcile through transitions |
| Invalid coercion | An invalid combination changes silently | Reject or surface the conflict; keep the last valid state |
| History loss | Undo restores appearance only | Keep semantic snapshots or narrow the support claim |
| Stale projection | An async view lags | Tag revisions; discard stale completions |
| Unsafe render | Imported text acts as markup | Isolate the source; inert text or a reviewed sanitiser |
| Partial import | A half-migrated file corrupts active state | Parse and migrate in isolation; activate atomically |
| Partial save | An incomplete save replaces the recovery copy | Validate the new version before switching to it |
| Stale anchor | Line comments float | Revision-aware anchors, context digest, explicit confirmation |
| Access path | Core action unreachable | Equivalent keyboard or list path, or an honest narrower claim |
| Viewport flow | Long, narrow, zoomed or loading layout hides actions | Keep state; predictable focus; reachable output and recovery |
| False success | Effect denied or timed out after an optimistic message | Await confirmation; keep the output; retry only when known safe |
| Authorisation mismatch | Syntax passes, policy rejects | Separate the two; disable execution; route to the owner |
| Consumer drift | Consumer, schema or dialect changed | Mark unsupported; pin versions; golden output plus real validation |
| Async race | Completion order overwrites intent | Cancel; compare revisions; idempotency tokens |
| Retry storm | Retries amplify a failure | Bounded policy; keep local work; degraded or manual route |
| Resource exhaustion | Large or hostile input freezes the page | Limits, cancellation, chunking or a worker, a known-good save, a stated boundary |
| Collaboration conflict | Concurrent writers overwrite | Single writer, or explicit merge with a conflict record |
| Telemetry blind spot | Only successes are recorded | Record bounded failures and recovery; fix the denominator |
| Diagnostic leak | Logs or screenshots expose source | Redact or hash; restrict retention and access |
| Route lock-in | A prototype becomes an unsupported operation | Freeze it or hand it to a product owner |

Specialist owners handle security, privacy, authorisation, irreversible effects, collaboration consistency, safety-critical decisions and assistive-technology policy. The playground still owns truthful status, state preservation, accessible recovery and the handoff.

## Workload Model

The sources give no measured capacity figures. Their source-count and sub-task caps were unmeasured and are not repeated. Treat the items below as pressure signals, not thresholds.

### Units of work

| Mode | Healthy unit |
| --- | --- |
| HTML explainer | One reader and outcome, one causal spine, one question per act, a unique role per component, one refresh owner. One subsystem, one 5 to 8 act arc |
| ASCII | A local figure, a composed terminal page, or a suite of pages with an overview |
| ELI5 note | One audience, one decision, one checklist. Split by decision or by source of truth |
| Playground | The smallest decision that can be accepted or rejected end to end. The first slice crosses the riskiest boundary |

Size an ELI5 note by the decision to be verified and the evidence behind it, not by words or files. Split by decision or by source of truth, never into arbitrary batches, and carry the audience, claims, evidence, open question and gate into each part. Many duplicate files can stay one workload. Two safety authorities that conflict may need resolving before any writing. Token budget, claim graph, time box, audience layers and artifact pipeline are different pressures with different remedies. What a durable note costs to maintain depends on its dependency edges, volatility, how often its triggers fire, how often corrections recur, and ownership. It does not depend on how large the note was to create.

Spend the effort on exploration, narrative and teaching choices. The template amortises the build. Rushed pages become file-tree tours. A tiny question gets a chat-length ELI5; a subsystem gets the full artifact.

### Pressure signals for a single HTML page

| Signal | Response |
| --- | --- |
| Incompatible audiences | Overview plus companion pages |
| Independent heartbeats | Split by lifecycle or subsystem |
| Stale or contradictory owners | Isolate or stop the affected act |
| Variants that are not really symmetric | Keep the central dimensions; move the rest to deep dives |
| Catalogue density | Companion reference |
| Widget gallery | Simplify |
| Runtime, auth or live data became essential | Tested application |
| Too many targets to verify | Narrow the support promise |
| Duplication across pages | Shared static parts, only after reuse is demonstrated |
| Concurrent edits | One writer per path |

Capacity review for a page: map each claim to an act and an outcome, each component to a role, and each dependency to an alternate-state check. Use the counts you observe locally; they are not universal thresholds. Concurrent edits need exclusive paths, checkpoints and one final verifier. A healthy page also has a manageable amount of evidence and conflict, shared state dimensions across what it compares, static essentials with a bounded fallback, and a support matrix in proportion to its readers.

### Estimating a playground

The workload is the effort to make one bounded decision trustworthy across state, interaction, projections, lifecycle, environment and handoff. It is not the screen count.

Inventory of pressure: decision scope; canonical state, coupling and migrations; source trust, revision, sensitivity and refresh; projections, hidden state and consumers; pointer, keyboard, touch and undo; lifecycle, save, share and collaboration; effects, network and authorisation; environment; consumer; evidence and owners. Do not convert pressure into universal points or day multipliers. Pressure is lower when the work is bounded, reversible, synthetic, kept to one session and local. It rises with coupled constraints, uploads, private or live data, several projections or consumers, graph gestures, migrations, effects, broad support, parsers, production policy, or evidence that is scarce and spread across owners.

The first slice includes a representative and an adversarial fixture, a minimal schema, one valid and one invalid or stale transition, controls with an equivalent input, preview and explanation, the exact handoff, a lifecycle path, recovery, the target viewport, zoom and motion, and the real consumer boundary.

To estimate transitions: define the invariants; find the boundaries of constraint, source, lifecycle, effect and consumer; group equivalent projections and environments; select positive, negative, recovery and migration paths; add pairwise or property-based coverage; keep incidents as fixtures.

Keep one slice when decision, state, owner, consumer and acceptance line up. Split in sequence for projections that are valuable independently. Split into separate tools for different users, permissions, lifecycles or consumers. Never duplicate semantic state. Send operational writes, execution, roles and collaboration to product architecture; use a static explainer for comprehension and a component lab for isolated states. A sensitive multi-dialect query tool with persistence, execution, row policy, streaming and concurrent edits is not playground work; separate the read-only exploration from the effects.

Count semantic transitions, not the product of all control values. Three viewports, one error and one keyboard path are samples, not sufficiency. A tiny concept map is high pressure if the canvas is the only store, edges are pointer-only, labels are unsafe or files are unversioned.

For ASCII, probe capacity with the real longest labels before committing to a layout.

### Sizing ASCII work

The workload is source text plus geometry plus reader tasks plus evidence, not paragraph count. Choose the smallest unit that has one coherent journey, one canvas contract, one revision owner and one acceptance packet. A unit is bounded when it can fail without leaving unrelated artifacts indeterminate.

| Unit | Shape | Note |
| --- | --- | --- |
| Local figure | One question, one grammar, one width, context nearby | Verify it in its final surroundings; indentation and wrapping change there |
| Composed terminal page | One journey across several section jobs and figures under a shared grid and vocabulary | Grammars may differ if the transitions and order stay clear |
| Artifact suite | An overview plus independently owned pages when audiences, canvases, cadence or acceptance differ | Vocabulary is shared; each page has its own goal, run card and evidence. The overview owns navigation and cross-page relationships, not duplicated detail |

Capacity probe:

1. Collect the real longest labels and the densest relations.
2. Set the narrowest canvas and a skeleton with jobs, anchors, gutters and routes.
3. Populate the hardest region. Record abbreviations, wraps, crossovers and relocated branches.
4. Test the global reading path.
5. Run the checks and one reader question.

Keep the profile only if progressive disclosure preserves the answer without hidden context.

Split for incompatible audiences, surfaces or canvases, owners, a path that repeatedly crosses sections, or essential labels and relations lost to compression. Do not split merely because flow and state figures are mixed, or by box count. Do not keep a giant page merely because the product is shared. If the child pages duplicate context, move the boundary or keep a concise relationship overview. Recombine when duplication costs more than stable links, ownership and memory save.

| Grade | Case |
| --- | --- |
| Good | A retry lifecycle with its true labels as one state figure |
| Good | An async walkthrough under one 84-column contract and one packet |
| Good | A multi-team guide as an overview plus accepted pages per service |
| Bad | All ownership, runtime flow and incident recovery in one screenful |
| Borderline | Split only after a narrow-canvas probe disproves progressive disclosure |

Estimate the verification work as well. Record the profile, the probe candidate, the narrowest canvas, the labels, the pressure found, the reason for any split, acceptance per unit and suite navigation. Revisit after label growth, a renderer change, a clarification or a reflow.

## Reliability Target

No numeric reliability target is set here. The sources that proposed pass-rate thresholds reported no measurements behind them, and one source rejects such a target outright. A small sample pass count is not a reliability percentage.

What "reliable" means for these artifacts: truthful, reachable, reproducible and maintainable under declared conditions. It does not mean universal browser support, formal accessibility conformance or measured comprehension. Formal accessibility or broad compatibility claims need current standards evidence and a specialist process.

Invariants that block delivery when broken:

- no knowingly unsupported high-consequence claim (production, security, latency, reliability);
- the essential mechanism, caveats, source route and takeaway are reachable under every declared condition;
- narrative and visuals preserve causality;
- proof is tied to the artifact and source versions;
- for a playground: no silent corruption, no false success, no unsafe effect, no inaccessible core task.

Core objectives beyond the invariants: reproducibility; visible uncertainty and recovery ownership; reader task quality; stable responsive and interactive behaviour; traceable refresh. A numeric target needs an owner, a sample, a method, a baseline, a consequence and a stated uncertainty. Record hash, audience, conditions, versions, methods, status and residual risk. When the impact of a change is unclear, rerun conservatively.

For a playground, reliability means preserving the decision, reporting uncertainty and operation outcomes truthfully, producing an artifact the consumer can interpret, and bounded recovery. It does not mean instant animation or one universal percentage. Keep reference reliability (consistent sources, routing, assumptions and verification) apart from implementation reliability (state, projections, persistence, effects, accessibility, consumer, detection, recovery). Conformance to this guidance cannot prove production reliability.

Deterministic gates for a playground: source-boundary integrity; canonical-state integrity; save and migration round trip; consumer acceptance; truthful status for copy, download, upload, network and execution; clear recovery. Priority among failures depends on reversibility, detectability, scope, sensitivity, effects and downstream use, not on frequency. The four blockers in the invariant list stop release. Visible, retryable failures of availability, performance or appearance get bounded degradation and a target budget.

An operational objective specifies the task and consequence, the accurate event, the population and exclusions, versions, window and segments, target and baseline, detection, containment, recovery and escalation, a guardrail against gaming, and what invalidates it.

Visual quality, speed and satisfaction cannot offset an unsupported claim or an essential caveat that cannot be reached. "Zero unsupported claims" cannot be proven; "no knowingly unsupported consequential claim remains" can be defended.

Five layers for an ASCII page, each checked on its own: source integrity, artifact conformance, fitness for the decision, observation on the reader's surface, recovery.

| Layer | Passes when |
| --- | --- |
| Source integrity | Each material claim is labelled local, inherited external or synthesis; local references resolve; freshness is stated. An unlabelled material claim blocks acceptance |
| Artifact conformance | Encoding, whitespace, fences, tables and width hold for the exact candidate. No tolerance for a malformed or stale artifact |
| Decision fitness | The adopt, adapt, avoid and adjacent routes were exercised. A critical misroute blocks |
| Reader and surface observation | Every required render was inspected and representative locate, explain and act tasks were run, with audience and environment recorded |
| Recovery | Each failure names the work stopped, the action, the owner or escalation and the reruns, or an honest stop or adjacent method |

For ASCII, reliability means keeping evidence boundaries, routing tasks correctly under declared conditions, surviving the required surfaces and explaining recovery. It does not mean identical interpretation in every terminal. Without a maintained sampling protocol, test the highest-risk cases directly and report bounded observations.

Controls grow with consequence, volatility and reuse. A disposable figure still obeys the character, width and connector rules and may rely on the author's check. A maintained page adds an independent reader and every render. A high-consequence runbook adds broader coverage, critical-failure cases and a recovery rehearsal. Volatile renderers and external claims need freshness triggers. Stable geometry needs regression fixtures.

A good target names the structural status, the required renders, an unaided reader task and the hesitation that was corrected. Disagreement between an expert and a new maintainer calls for a narrower audience or a revision and retest. Bind each report to identity, claim, layer, task, audience, surface, date, result, severity, owner, disposition and rerun. A material change to labels, canvas, renderer, source or routing expires the evidence.

Why the controls work: stable anchors localise reflow; a bounded vocabulary reduces drift; longest-label probes expose capacity; identity prevents stale evidence.

Unknown is not pass. Use `pass`, `fail`, `not_applicable` with a reason, and `not_evaluated`.

Guardrails for an ELI5 note. These are policy, not observed results:

- every material recommendation keeps its boundary;
- every failure route names a rollback, an escalation, the evidence and the next reference, plus a completion condition;
- sampled claims keep the source's causal direction, conditions and status;
- the reader passes one unseen case and identifies one boundary.

### When a pass rate is measured

A project may choose to sample how often an explanation routes readers to the right decision. No threshold is prescribed. These rules keep the sample honest.

Before measuring, define:

- the target population and the explanation version;
- the audience groups and the task strata, with realistic borderline cases included;
- the sampling method;
- the rubric for a correct route;
- the severity levels;
- reviewer independence;
- how disagreement between reviewers is handled.

While measuring:

- Synthetic fixtures test conformance to the policy. Live samples test fit to real work. They answer different questions and are not pooled without explanation. Before live uses exist, bootstrap with fixtures that cover ordinary, boundary and high-consequence routes, and report them as fixture results.
- Repeated judgments by one user are correlated. Twenty decisions are not twenty independent users or contexts.
- Severity overrides the aggregate. A critical misroute blocks reuse even when the count looks good. A critical defect is one that changes a consequential action, an authority boundary or a level of confidence in a way that can propagate. A harmless extra source read is not in that class.
- Never choose only obvious tasks, adjust the denominator after seeing failures, count duplicate cases as independent coverage, coach readers toward the expected answer, redefine the unit to leave out inconvenient prose, or exclude slow or failing runs after the fact.
- Keep every miss. Repair it, add it as a regression fixture, and rerun the affected strata.

When reporting:

- Give the numerator and denominator first, then the sample, audience, version, misses, reviewer disagreement and uncertainty. A statistical interval is useful only when the sampling design makes it meaningful.
- Keep target, observation and inference apart. "The policy allows no unsupported high-consequence claim" is a rule. "The reviewed version contained none in the sampled claims" is a bounded observation. "Future readers will never meet one" is unsupported.
- Ambiguous classification is a finding. It may mean the guidance is not stable enough to measure.

Report shapes, illustrative and not measured:

| Report | Verdict |
| --- | --- |
| "On the tested version, N of M stratified routing fixtures matched the adjudicated route. The misses were one audience mismatch and one late handoff to a specification. Both were repaired and kept as regression cases. No critical unsupported claim was found in the inspected claims." | Good |
| "The reference is 90% reliable." | Bad: no denominator, sample, version or misses |
| The count meets the project's bar, and one miss is a severe operational misroute | Borderline: not released until that miss is corrected |

Carry each claim's status into derivatives. An accurate explanation loses its caveats when copied into a prompt, a slide or an onboarding summary. List the durable high-consequence copies, keep the governing claim and its evidence status as part of their contract, and sample them when propagation matters. When a model is withdrawn, name the affected copies and the corrected route. Do not fix only the source file.

## Retry Backpressure Guidance

A gate failure is a stage failure. Go back to the stage that caused it.

| Failure | Go back to |
| --- | --- |
| Ungrounded claim | The source |
| Dense act | The outline: split or re-plan |
| Broken metaphor | Replace it. Never soften it |
| Checklist failure | The failing stage, not only the markup |

Catch failures on the outline, before the template is touched. A gate failure is a stage failure, so it routes backward. A dense act that will not split usually bundles motivation with mechanism. For stale external evidence make one bounded retry, then escalate to a person or narrow the claim. Stop new generation while source, critique or verification coverage is failing. A long run keeps a resumable record that names the next action, the gate and the stop condition.

Retry only after classifying the failure and changing a causal input. "More detail" on the same evidence is not a retry. Before retrying record the failed candidate, the signal, the provisional class, what changed, the expected result and which checks may now be invalid.

| Class | Action |
| --- | --- |
| Credible transient | Keep the output; retry once unchanged; a second identical failure is undiagnosed |
| Stale evidence | Refresh only the affected source or render; re-evaluate dependents. One bounded refresh, then escalate |
| Missing context | Load the smallest discriminating source, label, constraint or task |
| Local defect | Patch the responsible character, width, fence, table or heading; rerun; widen to renders and readers if meaning changed |
| Semantic or layout problem | Return to the question and the run card; compare a bounded set of named variants |
| Contradiction | Stop writing; record authority, scope and consequence; keep both positions; ask the owner |
| Wrong medium or capacity | Narrow, split with an overview, or route |
| Ownership conflict | Stop writes; keep identities; resolve ownership; no destructive recovery |
| Deterministic command failure | Change the command, input or path |
| Flaky visual | Fix the bytes and conditions; state a hypothesis for the instability |
| Reader misunderstanding | Not solved by repetition; repair the teaching |

For an ELI5 note:

| Failure | Action |
| --- | --- |
| Transient read failure | Keep the path and the output; retry an idempotent check once; escalate when it repeats or the state is uncertain |
| Stale external fact | One bounded refresh, or mark and narrow the claim; after that request access or route |
| Missing context | Read the smallest authority, or publish the bounded portion |
| Contradiction | Keep both positions and pause the synthesis |
| Analogy or terminology | Repair the mapping or the definition, then run a fresh transfer and teach-back |
| Routing | Carry the handoff payload to the destination |
| Structural | A small repair on a path you own |
| Correct teach-back, wrong action | Triage whether the tool, the procedure or the skill is at fault |

Stop or escalate when the evidence cannot distinguish between causes. Hold back only the work that depends on the failed item, and release it only on evidence that the dependency was repaired. Checkpoint the objective, owned paths, sections, evidence, failures and next steps. One owner per file or batch.

Minimal retry record: failure class, decision, fixture, evidence, changed hypothesis, paths, gate, result, residual risk, next state. No universal retry count or time budget exists.

An unchanged retry needs a named transient mechanism and a bounded count. Defer a volatile claim only after narrowing the guidance that depends on it and recording the trigger for returning. Accept a limitation only when it lies outside the contract, its consequence and route are stated, and no action-critical state is hidden. Hold back dependent work, not independent tasks. Before a broad rewrite or a handoff, reread the specification, the working journal and the candidate. For blocking, recurring, volatile and high-consequence retries keep the candidate's identity from before and after.

For an HTML explainer, retry only when repeating the smallest operation could plausibly change the result without changing the question. The contract: classify the failure; persist the artifact and evidence; make sure the target is idempotent or disposable; state why this attempt differs; bound the attempts; compare outcomes; then accept, fall back, escalate, narrow or stop. An unchanged failure after the bound is evidence for diagnosis.

- A temporary tool or capture interruption may be retried after the environment visibly recovers.
- An optional resource is retried only if declared transient. Otherwise test the fallback.
- Missing authority and ownership collisions are not solved by repetition.
- A stale external pointer is refreshed only when that is authorised and relevant to a decision.
- Backpressure is scoped to the dependency: stop only the acts, diagrams and metrics that depend on the failure. A failure in essential content stops authoritative sharing on that path.
- Record hash, class, gate, preserved state, hypothesis, what differed in operation or environment, outcome, comparison and disposition.

On regression restore the last accepted candidate before any broad redesign. A changed source or requirement starts a new evidence cycle. Close a recovery only when the signal no longer reproduces and the invalidated checks have fresh results.

### Playground runtime

No universal attempt count or delay exists. By class: safely repeatable transient, bounded retry; stale completion, discard; missing context, pause or narrow; deterministic invalidity, correct the input; authorisation denial, escalate; overload, apply backpressure; unknown effect, inspect and deduplicate before repeating; cancellation, cancel queued work.

A repeat is safe only with an idempotent or isolated effect, valid preconditions, no duplicate consequence, the current state revision, cancellation, a budget, a degraded mode and a terminal recovery. A changed input, policy, source or authorisation makes a new operation, not another attempt. Stale evidence is refreshed. A contradiction stops for the owner. Whatever attempt count, delay, jitter or timeout the target adopts must be bounded and reviewable. Retries in a running playground and retries while authoring guidance are different systems.

Under load keep, in this order: canonical editing that stays responsive and recoverable; exact current output if valid; coalescing of obsolete work; deferral of decorative or expensive enrichment; bounds on import, layout and parsing; disabling of effects that lack freshness, authorisation or idempotency; a visible degraded status with a safe action. Coalesce renders from continuous controls but keep each semantic change as its own undo step. Never hide partial success across several systems behind one Apply button.

## Observability Checklist

The artifact is a trace of the author's understanding: acts show the concept sequence, citations pin claims, metaphors expose the author's model, navigation dots segment reader behaviour.

- [ ] Exploration notes kept beside the page, with sources loaded and sources skipped on purpose. Final citations keep the conclusions and lose what was explored and rejected. Notes kept privately preserve the path but give no accountability.
- [ ] Claim ledger kept.
- [ ] Commands run, with results. A command summary, a changed-file list and unresolved-risk notes are more useful than a raw transcript.
- [ ] Findings recorded in the finding shape from Theme Specific Artifact.
- [ ] Screenshots kept only when they prove a finding.
- [ ] Misconceptions reviewed at the metaphor layer by someone who knows the code.
- [ ] For each check: not observed, not collected, not applicable and measured zero are kept distinct.
- [ ] One timed run is one observation. No percentiles from a handful of runs.
- [ ] Reader signals kept apart: exposure, recall, navigation, prediction, decision quality, clarity.
- [ ] Any analytics has a stated decision it serves, plus privacy and consent.
- [ ] Summaries are compact and decision-bearing. Identity is redacted and the local retention policy is followed.
- [ ] A fresh reviewer can reconstruct the release decision or the failure from the record, with no hidden conversation state.

What the record holds for an ELI5 note: intake (identity, audience, decision, consequence, reuse, owner); source paths and intentional skips; for each claim its origin, conditions, confidence and how it was transformed; the artifact change and version; each verification with its exact command or question, path, result and coverage; each reader check with its fixture, action, rationale, confidence, limit and any coaching; handoffs; retries; reliability samples; refreshes and withdrawals.

Speed evidence needs the input, source, task, environment, start and stop points, warm-up, concurrency, sample and a stated percentile method.

For an HTML explainer:

- Collect the smallest set of evidence that reproduces the result. Do not keep raw transcripts, sensitive source or screenshot collections merely because it is easy.
- Sources: versions or hashes, decisions, sources skipped with the reason, claim status, footer and attribution, and a review for sensitive data.
- Output: path and hash, the opening or generation command, working directory and runtime, proof of disposable generation and overwrite refusal, audience, outcome, scope, non-goals, compression sentence, owner, refresh trigger, and where the page diverges from its brief.
- Screenshots and interactions: hash, browser, viewport, input method, motion setting, script and asset state, and the consequence. Results for keyboard and focus, reduced motion, script failure, assets, console and network. `not_evaluated` kept separate.
- Reader checks: task, prior knowledge, rubric, answers, misconceptions and the limits of the sample.
- Analytics, if any: the decision it serves, privacy and consent, minimisation, access, retention and deletion.
- Changes: paths, sources and claims changed, evidence invalidated, reruns, risks, retry hypothesis and outcome, ownership and checkpoint, stale status.

For a maintained ASCII candidate:

- Keep the events that changed authority, geometry, acceptance, recovery, ownership or maintenance.
- The record holds: identity, event and path; goal, profile, canvas and surfaces; sources loaded and skipped, with reasons; inherited external claims and their freshness; exact commands, environment, results and links to raw failures; target observations and reader questions; decision, severity, owner, disposition and rerun; uncertainty, containment and next refresh; any sensitive detail redacted on purpose, the reason, and enough left to reconstruct the decision.
- Use the candidate identity as the join key across the run card, journal, command report, reader notes and source manifest. Give each fact one authoritative home and link to it from elsewhere.
- Scale the record. A disposable sketch keeps the question, canvas and check. A candidate adds source, command, render and reader evidence. An accepted page keeps the decision and its triggers. Maintenance records changed inputs, invalidated evidence and reruns. Distributed work adds owner, checkpoint and handoff.
- Classify each entry as mechanical result, observed behaviour, reviewer inference or unresolved uncertainty. Keep disagreement.
- Collect no latency percentiles without a repeated workflow, defined start, end and population, and a decision the number would change. Report small observations directly. Expanded traces are for a named investigation and are summarised.
- Reconstruction test: a second reviewer, with no spoken setup, identifies the governing sources, reruns the checks, locates the renders, repeats the reader task, explains the risk and names the next trigger. Links must resolve. Record the limits of reproduction when a volatile surface changes.
- Prune fields that never affect a decision. Add a field only after a recurring or consequential failure shows the context was missing. Causal continuity matters more than a completed form.

Playground, when it is more than disposable: observe semantic boundaries, not every pointer move. Transition (versions, prior and next digests, outcome); projection (requested and completed revision, duration); validation; persistence; external operation; consumer; recovery; accessibility task. Do not record raw labels, documents, prompts, credentials, query text or user identity; use opaque local identifiers. Emit "accepted" only after the consumer returns. A disposable local tool may have no telemetry at all when fixtures, visible status and a voluntary export are enough.

Before adding any telemetry, say which diagnostic, recovery, release or guidance question it answers, who acts on it, what data is permitted, and how long it is kept before deletion. An event carries an event-schema version, an event name, template, state-schema and source revisions, a local operation identifier, requested and completed revision numbers, an outcome such as accepted by the target parser, the consumer version and whether recovery is required. Use a keyed or opaque digest when low entropy would make a value guessable. Async evidence records request and completion revisions, operation and attempt identities, cancellation, stale discard and the terminal outcome. External operations record attempt, cancellation, effect and authorisation. Correlate events only across an explicit contract.

## Performance Verification Method

No performance numbers were measured for these artifacts. A page-load or response percentile with no measurement behind it is rejected. Static pages often need no percentile.

Correctness first. Optimise after, then rerun correctness and accessibility checks.

HTML explainer:

- The implicit budget is CSS-only animation, one file, no framework. An imported library voids it.
- Syntax highlighting with a span per token multiplies the DOM on code-heavy pages. Use excerpts.
- An eight-act page should scroll smoothly on an old laptop. This is a qualitative check; no weight budget exists. One animated diagram is acceptable only if its value survives that test.
- What can be measured if a project needs it: load and availability; response of a named control; visual stability; file weight and dependency count; authoring and refresh effort; reader task time.
- Improve the structure first: remove unnecessary requests, hidden reveals, heavy media, duplicate scripts and unproven controls.
- Measure only when a bounded runtime cost affects the reader's outcome. Keep the families listed above separate.
- Procedure: state the reader consequence and the claim. Define trigger, start, end, result, hash, delivery, viewport, input, motion, scripts, assets and browser. Establish correctness. Choose controlled conditions and do not mix cache states or artifacts. Sample in proportion to the claim. Agree the consequence with the owner in advance. Investigate confounders. Report method, raw summary, statistic, uncertainty, result, environment and repair. Rerun correctness and accessibility after any optimisation.
- Valid: a keyboard-operated comparison toggle reaching the correct labelled state under fixed conditions. Invalid: a percentile over mixed clicks and scrolls.

```bash
wc -c .prd/ELI5/index.html                                 # file weight
grep -c -E 'https?://' .prd/ELI5/index.html                # external references to review
grep -c '<span' .prd/ELI5/index.html                       # rough token-span count
```

ASCII. Verify the claim that is being made: canvas fit, survival in a renderer, reader action, or repair effort. Never collapse them into one speed score.

| Claim | Evidence |
| --- | --- |
| Character and width | Deterministic checks plus copies on the target surfaces |
| Reader effectiveness | A locate, explain, compare or act task written in advance, with context and assistance recorded |
| Comparative speed | A credible baseline, comparable inputs and readers, event boundaries, repeated observations, errors and assistance |
| Maintenance effort | A realistic change to a label, state or route, with the complete repair and rerun |
| Workflow cost | Source, tool, reviewer and time, only with a defined start and stop and a decision the figure affects |

Stages:

1. State the perspective, task, candidate, surface, consequence and claim, with criteria for pass, fail and inconclusive.
2. Keep a credible baseline, or claim fitness only.
3. Run mechanics first and stop on failure.
4. Copy the exact candidate to every surface.
5. Run the task uncoached. Record answers, wrong turns, context requested and assistance, and time only when it matters.
6. Compare only compatible wording, copy, width, environment, familiarity and events. Note order and cache confounders.
7. Separate measurements from interpretation and list the untested scope.

Pass when the declared mechanical and task outcomes hold with no critical error. Fail for misrouting, lost state, a broken surface or hidden author context. Inconclusive when confounded; then narrow the claim or design a test that discriminates. Percentiles need a documented population, sampling, enough tail observations and a controlled protocol. Timing precision cannot exceed the control over familiarity, latency, order and boundaries.

Look at lifecycle cost. First-draft speed can hide the cost of understanding, localisation and repair. Use change simulations first, then real defect and reflow records. The objective is the cost of reaching and keeping correct decisions across author, reviewer, reader and maintainer.

ELI5 note. Performance means time to a correct next action with quality preserved. It does not mean reading speed. Timing is judged with correctness. Illustration from the sources, not a measurement: a slow note with the right caveat passes; a fast note that routes the reader to the wrong authority fails; a very slow review that finds an omitted conflict suggests the example set or the target was wrong.

Define a run before starting the clock:

1. Reader: role, prerequisites, earlier exposure to the note, and whether the run is individual, assisted or agent-mediated.
2. Fixture: a representative task with its input size, source count, consequence, distractors that discriminate, and one unseen variation. State the adjudicated action, acceptable alternatives, the verification gate and the stop condition.
3. Environment: artifact version, permitted files and tools, cache or warm-up state where runtime applies, concurrent delays, any assistance.
4. Clock: start when the reader receives the task and the note. Record time to the first proposed action, time to the verified action, pauses and excluded delays. Stop only when the action, rationale, gate and boundary are stated.
5. Guardrails: an independent review of source fidelity, correct route, transfer to a new case, and uncertainty. A wrong or unsupported action fails whatever its speed.
6. Record: every valid run, slow and failed ones included, with the real denominator.

What can be measured, and what each measure misses:

| Measure | Question it answers | Blind spot |
| --- | --- | --- |
| Time to first correct action | How quickly the reader finds a viable route | Ignores later verification or boundary errors |
| Time to verified action | How long until action, gate and stop condition are all correct | Mixes the note's usability with tool and workflow latency |
| Irrelevant files or searches opened | Whether the note reduces navigation and ambiguity | Fewer steps are not better if needed evidence was skipped |
| Substantive corrections | How much reviewer intervention was needed | Reviewer style and expertise vary |
| Confidence calibration | Whether confidence tracks correctness and limits; capture it before the expected result is shown | Self-report is noisy |
| Runtime | Whether a tool-backed workflow meets its operational target; needs input distribution, repeated runs, warm-up and a percentile method | Says nothing about conceptual quality |
| Reviewer decision time | Whether the next decision is easier to locate and justify | Learning and task mix confound comparison |
| Trend over repeated use | Whether the mental model reduces later effort on unseen tasks | Practice and outside learning contribute |
| Downstream rework | Whether a fast first decision caused later correction | Attribution to the note alone is rarely justified |

Rules for the record:

- The measurement packet holds input size, source count, the number of distinct claims or conflicts when known, tool-call count, wall-clock time, reader decision time, correction categories, action correctness, confidence and artifact version.
- Keep slow, failed and conflicting runs. Exclusions follow validity rules declared in advance and are reported. Do not drop a run after seeing the results.
- Separate reviewer time from tool latency. Their repairs differ: reorganise navigation for human search cost, tune tooling for runtime delay, repair evidence or teaching for decision error.
- The leading indicator is a correct route with its rationale on an unseen representative case, with fewer irrelevant searches or substantive corrections when a suitable baseline exists.
- The failure signal: the reader can list files but cannot choose an action, a gate and a stop condition. A source map with no operating action is a failure. A run also fails when it is fast but picks the wrong authority, repeats unsupported evidence or skips a consequential condition.
- The reader should be able to name a case where the action changes.

What a timed observation establishes:

- One run is an observation under named conditions.
- Repeated runs with one reader show a learning trajectory, confounded by practice.
- A matched or within-reader comparison can suggest a difference when task order and earlier exposure are handled.
- A broader comparison needs a defined population, sampling, enough observations and stable fixtures.
- A causal claim that the note produced the improvement needs stronger controls than this method provides.

For a note that is reused, look at cumulative correct work. A slower first encounter can establish an exact model that removes later ambiguity. A shortcut can win the first timing and cause rework. Optimise the first encounter only when that is the real requirement and the reliability invariants still hold.

Playground: measure task continuity and correctness, not a speed badge. Layers: input acknowledgement, state computation, local projection, serialisation, persistence, import, remote enrichment, consumer validation, long session. Fixture sizes: smallest contract, representative, largest supported, invalid or adversarial. Unsupported input must fail or degrade on purpose and never freeze the browser or lose work. Separate cold and warm runs. Report observed ranges when the sample does not support percentiles.

Each layer, reviewer workflow included, gets a budget or qualitative condition set by the target's owner, plus a semantic guardrail. Variables that scale, by kind: design (content, states, history, assets, viewport); concept map (nodes, edges, layout, undo); data (fields, rows, filters, groups, query chunks); diff (files, lines, hunks, comments, anchors); document (length, claims, comments, revisions); configuration (options, conditional groups, presets, versions, output).

Freeze the environment for a run: application, template, schema, source, fixture and consumer revisions; browser, runtime, device, viewport, zoom, input, motion and theme; cache, worker, storage and network; instrumentation and background activity; run counts, exclusions, failures and cancellations.

Runs to include: functional baseline; cold initialisation; warm sequencing; rapid input, races and cancellation; the maximum and beyond it; a long session; remote timeout, denial and worker failure; equality of projection, state and output; attribution of a slow trace; the optimisation repeated under the same profile.

What to measure: main-thread and input delay; processor time by phase; memory, retained growth, history and cache; waits on worker, network, storage and consumer; requests issued, coalesced, cancelled, retried and stale; bytes against scale; frames and long tasks; pending, degraded and recovery states. Microbenchmark only a stable, pure, hot boundary, then rerun the full task. Unsupported input keeps the editing state and the exact export. A faster serializer that changes escaping or order is a regression. Options after correctness: a worker or incremental parsing, revision scheduling, virtualisation, bounded history and cache, dropping projections, narrower support, or removing the feature.

## Scale Boundary Statement

Count of systems or pages is a pressure signal, not a threshold. Test the dimension that is growing.

HTML explainer: stay with one file while one outcome, one spine, one owner and one support promise hold together. One page is one subsystem and one novice arc. Grow by federation: bounded topic pages plus an index, not a 15-act epic. A two-page arc needs an explicit seam. Least disruptive order: narrow the claim, change the level of abstraction, add a companion, make a series, share static parts after demonstrated reuse, move to an application only when runtime behaviour is essential. Keep a static companion beside an application so caveats are not hidden in the control plane. Split for incompatible audiences, competing heartbeats, pressure on sources or ownership, duplicated or contradictory claims, essential live, authenticated, personalised or server state, an excessive support matrix, unbounded discovery, or concurrent edits to one file. Shared style and shared source truth are separate migration tracks. Consolidating early can make build and migration failures correlated; checkpoint atomic units, keep exclusive write boundaries and keep one final verifier. Experts looking for one forgotten detail find the format slow; conventional reference documentation stays necessary.

ASCII stops sufficing when compression, coordination, volatility or verification destroys a relationship the reader needs.

| Dimension | Sign | Response |
| --- | --- | --- |
| Reader | Incompatible starting points, terms or actions | Pages per audience; a shared overview only for common relations |
| Canvas | Labels cannot fit the narrowest surface without ambiguous abbreviation | Split, move detail, or use a richer medium |
| Relationship | The path needs repeated jumps between pages, or edges are unreadable | A bounded overview plus owned detail pages |
| Source | Discovery is open-ended or authority is unranked | Rank authority; stop composing until the boundary is clear |
| Ownership | No owner for shared vocabulary or cross-page edges | Assign contracts first |
| Volatility | Live values, changing topology, filtering or zoom | Operational or interactive tooling; ASCII holds stable guidance and the fallback |
| Verification | One packet cannot cover the surfaces and readers | A run card per page plus a suite-level vocabulary check |

The overview owns durable topology, vocabulary, entry points and routes. Child pages own volatile facts and procedures. Never copy volatile detail into the overview. A generated index may list owners, audiences and routes, and source and link checks then become part of acceptance. An index cannot fix an unclear decomposition or an orphan edge.

One page stays valid when the readers share the overview, the vocabulary is stable, the edges survive the narrowest canvas and one packet is enough. Different grammars or components do not force a split. One product does not justify one page.

Probe the hardest label, the densest edges, the narrowest surface, source closure, a change that crosses owners and the highest-consequence task. For a suite, test the overview journey, each child page, every route and the shared terms. Retest after localisation or a change of renderer, audience, source or ownership. Do not invent numeric capacity buffers. Keep boundaries reversible.

Distributed work: one writer per file, frequent durable checkpoints, and no overlapping rewrites without an owner for reconciliation. Context drift is a reliability failure; reread the specification, the journal and the candidate. The unit that scales is a page with its authority, routes, tests, ownership and recovery. A static runbook helps when a dashboard or the network is down, but it is not a source of live traffic or health; say what the fallback enables and what must be refreshed elsewhere.

Playground: it is the right tool while one bounded exploratory decision has coherent state and an accountable handoff. Stop or route when the prototype serves stable operations; when it writes live data, executes, pays, or does anything legal or irreversible; when tenancy, authorisation or audit matter; with several writers; under a production service objective; with regulated storage; when discovery is unbounded; when there is no degraded mode; when there is no owner. The lab can survive as a local simulator, a fixture generator or a read-only comparison.

The playground guidance becomes supporting, not primary, when operational coordination, domain policy, shared effects, distributed consistency or governance owns more of the risk. Raw counts are not the boundary. Review these axes: decision, state, source, data, projection, persistence, effects, users, traffic, collaboration, ownership, evidence, codebase and agent workflow. Continue when the decision is reversible, the schema is coherent, versions are frozen or marked stale, effects are local or review-only, one owner verifies the handoff, support and failure boundaries are explicit, and a vertical slice was accepted independently. Adapt for one technique that has evidence on the target. Split only where decisions, users, owners, consumers or acceptance are independent and no semantic state is duplicated.

Explicit interfaces may chain a local candidate to traceability, to a domain validator, to an operator, with schema, version, owner, failure handling and evidence at each handoff.

ELI5: a mixed request is split by decision. The note orients; the governing document decides.

- An overview alone is not enough across incompatible contracts, across ownership boundaries, for open-ended discovery, or for production traffic without explicit objectives.
- Keep one note while one owner verifies the claims, the readers share a layer and the sources are bounded.
- Split by audience, decision, system, source, artifact, agent concurrency, workflow or rate of change. Keep one source of truth and carry the handoff payload across each split.
- Progressive disclosure solves reader load. Ownership solves governance load. They are different problems.
- Checkpoint a long workflow. A fresh agent resuming from the checkpoint is the evidence that it works.
- Exact API, recovery, policy, service-objective and incident behaviour go to the artifacts that own them.
- Nearness in a link or call graph is not relevance and not authority.
- Clear names, interfaces, tests, documentation, defaults and tooling reduce the need for explanation in the first place.

## Outcome Metrics and Feedback Loops

No effectiveness figure is established. The teaching benefit of the act-based format is a coherent design inference that the sources did not measure. Do not cite improved onboarding as a result. A reader study is the natural upgrade. Do not infer comprehension from views, scroll depth, polish or author confidence.

Before interpreting any result, define the reader task, the artifact version or hash, the environment, the sample, the rubric and the response the result will trigger. For a page that is maintained, attach the artifact hash, audience, task prompt, rubric, environment and source versions to every measurement record.

### Signals worth keeping

| Signal | How to collect |
| --- | --- |
| Reader completion | Did they reach the takeaway |
| Comprehension | Questions about the mechanism in a named act, a week later in an onboarding retro. Test the mechanism, not recall of the metaphor |
| Transfer | Reader applies the rule to an unseen case |
| Action and stop | Reader names the next action and when to stop |
| Source fidelity | Reviewer samples claims against sources |
| Reuse | The page is linked or opened again |
| Staleness | Citation drift per act; review on a regular schedule, for example quarterly |
| Production health | Share of pages passing the checklist at first review |
| Correction burden | Fixes needed after release |
| Confidence calibration | Stated confidence against later corrections |

An author's own checklist pass is necessary and blind to the audience. A leading sign of health is a new reader applying the page with no hidden context. A sign of failure is a dump of sources where a guided explanation should be. Collect at least informal completion and comprehension signals for each page.

Keep these as independent signals. Do not fold them into one composite score. For an ELI5 note the set is: process and provenance, source fidelity, teach-back, transfer to an unseen case, action and stop condition, confidence calibration, correction burden, and maintenance health.

Readability scores, length, satisfaction, link counts and passing commands are diagnostics only. They prove neither conceptual nor operational correctness. A convenience sample cannot support a universal percentage. Downstream success does not prove the explanation caused it. High fidelity with low transfer calls for a teaching repair. High memorability with low fidelity calls for a content repair. Production volume alone breeds a gallery of decaying pages.

Repair map: a metric problem goes to evidence; confusion goes to teaching structure; an analogy problem goes to its boundary or a replacement; an action problem goes to operating guidance.

Repair the layer that owns the fault:

| Fault found | Layer to repair |
| --- | --- |
| A claim cannot be traced to a source | The source map |
| Wrong causality or a misleading analogy | The model, or add a counterexample |
| Terms misread | The definitions |
| Failure on a new case | The rule or the example set |
| Wrong action | Decide whether the explanation, the tool, the procedure or the skill is at fault, then fix that one |
| Stale content | The dependencies recorded in the provenance |

Rerun the deterministic checks after every edit. Review again when the source, the audience or the workflow changes, or when a failure repeats. No universal calendar interval applies; a schedule such as quarterly is a local choice.

### HTML explainer

What to sample and observe:

- High-consequence claims, each classed as supported, inferred, conflicting or unknown.
- A cold reviewer locates and restates the mechanism.
- A target reader predicts a transition, a failure or a recovery.
- A reviewer identifies where the page is uncertain.
- Every declared alternate path is executed (scripts off, keyboard, reduced motion, narrow width).
- Scaffold residue is scanned for.
- The exact artifact is reproduced.
- Each defect is assigned to a repair layer.
- The effort of a refresh, and how far readers still depend on the author for support.

Unknown is not pass. A reader who finds the mechanism late signals a pacing risk. A small reader sample is not generalised. Repair the earliest responsible act or component, rerun on the new hash, and keep the misconceptions and decisions found, in words.

Loop for an internal page: structural and alternate-path gates; claim sampling; one outcome-aligned task if a reader is available; classify the layer; make the highest-impact repair; rerun what it affected; record remaining uncertainty. A maintained page repeats the loop after a change of source, target or audience, a reported misconception, a failed gate or dependency drift. Audit the metrics so that clicks, views or easy recall do not distort what the page promises.

### ASCII

Four families: reader outcome; mechanical conformance (including final newline, fences and table shape); portability across surfaces; maintenance cost. Scale the effort by consequence: disposable figure, maintained page, high-consequence runbook.

Loop: on every edit run the validator; at candidate stage paste into each surface; at acceptance run the reader check; in maintenance watch for a renderer change, a label that outgrew its budget, recurring support questions, a source change, or anchors that reflowed.

Detail for each stage:

1. Every edit: character, width, whitespace, fence, table and heading checks. Repair mechanics first.
2. Candidate: freeze the copy and the geometry, render on each surface, ask locate, explain and act questions, and bind the answers to the candidate's identity.
3. Acceptance: assign an owner and a disposition to each defect and rerun the affected checks.
4. Maintenance: light checks after edits; a full review after any of the triggers above.

Measure task completion, not the presence of a diagram. For the reader outcome record hesitation, wrong turns, context the reader had to ask for, and the final answer. For maintenance cost record the anchors, cards and routes repaired after an edit, any widening, clarification or reflow.

Effort by consequence, with no universal sample size or comprehension threshold:

| Artifact | Review |
| --- | --- |
| Disposable figure | Quick scan plus the author's own check |
| Maintained page | Target renders plus a second reader who was not involved |
| High-consequence runbook | Independent review across the audience and the surfaces |

Default evidence is direct observation of a task plus a defect log. Surveys show perception. Support logs show recurring gaps. Diffs show structural drift. Passive telemetry needs an existing, ethical system and an answerable question, and it adds privacy and interpretation cost. Triangulate around one decision. Never average unlike evidence into one score.

Periodically question the run card itself. Conformance to a stale width, character policy, surface list, audience or task set is not reliability.

Record identity, task, reader profile, surface, behaviour, mechanical evidence, severity, owner, decision and rerun. Keep fact apart from interpretation: "the longest line is 83 bytes under an 84-byte contract" is mechanical; "the timeout branch competes with the main path" is judgment. Good evidence names the audience, the task, the surfaces and the label budget. "Looks clean and the validator passed" is inadequate. If an expert succeeds and a new maintainer reverses a branch, test the wording and placement; do not ask for unspecified further feedback. Prefer geometry that keeps a correction cheap.

### Playground

Ladder: integrity, then usability, then decision quality, then consumer outcome. A higher level is not credible while a lower one fails. Do not use slider changes, canvas density, query count, comment count, word count, preset selection or copy success alone. Watch for everyone converging on one preset or staying at the default, and for samples drawn only from successful sessions. A healthy loop simplifies: remove controls nobody needs.

What each rung covers: integrity is state, undo, save, restore and projections; usability is completing and recovering the task by pointer, keyboard and mobile and through an error; decision quality is fit to the criteria plus the reasons for rejecting alternatives; consumer outcome is the parser, compiler, reviewer or implementer accepting the export, and the rework that follows.

Signals by kind:

| Kind | Signals |
| --- | --- |
| Design | Criteria covered; implementation intent carried into the handoff |
| Concept map | Accuracy of the typed edges; uncertainty that changed |
| Data or query | Valid filters, provenance, agreement between query and explanation, recoverable errors, analysis reproducible on a named dataset |
| Review | Stable anchors, dispositions, stale detection, less rework |
| Critique | Claim coverage, evidence links, a revision free of contradiction |
| Configuration | Exact output, migration and restore, consumer acceptance |

Observe at four moments: before the session, during it, immediately after, and after the handoff. Keep sensitive raw content to a minimum. A loop is closed only when the evidence changed a criterion, fixture, schema, interaction, output, default or recommendation, migrations were accounted for, the gates were rerun and the outcome was recorded.

Good evidence combines invariants, a representative task done by pointer and by keyboard, a rejection justified by a criterion, acceptance by the consumer and a review of the implementation. Failure patterns: high activity with no criteria; output that is faster but invalid or inaccessible; resets or recovery that fail; a regression in one segment; a metric that improves with no downstream use.

Review on invalidation events (a change to schema, consumer, framework, design, accessibility, security, source, audience or persistence, or evidence that a metric is being gamed), not on the calendar alone. Stop when criteria and guardrails pass, the risks have owners, the evidence is in proportion, and further controls would not change the decision. Remove metrics nobody uses, split claims that were bundled, and turn recurring failures into fixtures.

Define each metric before collecting it. A metric record names:

```text
decision and claim : the accepted user decision and the claim being evaluated
versions           : task, fixture, source revision, state schema, output contract
population         : who was evaluated; excluded and abandoned attempts
frame              : observation window, denominator, segments, comparison baseline
result             : value, guardrail, interpretation, confidence, known confounders
threshold          : the number or qualitative condition that changes the
                     recommendation
stewardship        : owner, review date, expiry trigger, evidence location
```

"Completion increased" means nothing without these. Completion can rise because a necessary validation step was removed, the fixture got easier, failed sessions were excluded, or users learned to click the recommended preset without understanding it. Keep definitions stable, compare only compatible tasks, and keep the old definition on record when a metric changes. A comparison is invalid when the task or the denominator changed between the two runs.

## Completeness Checklist

Statuses: `pass`, `fail`, `not_applicable` with a reason, `not_evaluated`. An omitted item is not a pass. A complete review may correctly conclude "do not build this". Counting ticked boxes proves nothing by itself; each tick needs the evidence behind it.

### Scope and evidence

- [ ] Reader, starting state, outcome and trigger named.
- [ ] Thesis, causal path and non-goals written.
- [ ] The medium is justified against the alternatives.
- [ ] Output path and ownership explicit.
- [ ] Claim ledger covers every major claim.

### Narrative

- [ ] Mechanism by Act II or section two.
- [ ] Each metaphor is removable and has its limit stated.
- [ ] Only supported guarantees.
- [ ] Comparisons asymmetric where reality is.
- [ ] The compression sentence is accurate and lets the reader predict an outcome.

### Components

- [ ] One question per act or section.
- [ ] A unique role for each visual or control.
- [ ] Excerpts short, interpreted and linked to a source.
- [ ] Diagrams make sense as text.

### HTML and alternate paths

- [ ] `lang`, title, viewport, semantic order, one `h1`.
- [ ] Content visible with scripts off.
- [ ] Keyboard reachable, visible focus, no hover dependency.
- [ ] Reduced motion honoured.
- [ ] Declared widths without clipping; long tokens handled.
- [ ] Optional assets have a fallback and a privacy review.
- [ ] Console and network reviewed.
- [ ] Navigation dots match acts; scroll reveal seen working or reported as not seen.

### ASCII

- [ ] Run card filled, or its reduced form for a small figure.
- [ ] Validator clean at the declared widths.
- [ ] Pasted raw into every promised surface.
- [ ] Reader names type, direction, main path and next action.
- [ ] Every item is recorded with evidence specific to this candidate and a written boundary or consequence. Evidence that is unavailable is a fail.
- [ ] Numeric and compatibility claims are evidenced or presented as bounded defaults.
- [ ] Good, bad and borderline artifacts carry a causal diagnosis and a reader outcome.
- [ ] Each defect has an owner, a disposition and a rerun.
- [ ] A sceptical reread finds no duplicated generic prose, unsupported precision, source-role inflation or wording that is merely authoritative.
- [ ] An unfamiliar reader can find the workflow, the figure family, the commands and the routes.
- [ ] Maintenance covers renderer changes, label growth, recurring questions, source updates and anchor drift.
- [ ] The completion record names the command that produced the counts, links the target renders and records a named reader's success. "Reviewed" or "looks fine" fails.

An unresolved misalignment in a renderer stays failed until it is resolved, or until the contract is deliberately changed and verified again. A gate that fails repeatedly is a reason to inspect the guidance: automate the check for a recurring table defect, or clarify the branch grammar. Change a gate only when the promise changed, and keep the earlier invariant on record.

### ELI5

- [ ] Big idea first.
- [ ] Analogy with limit for each major concept.
- [ ] Example, and counterexample where it helps.
- [ ] Numbers attributed.
- [ ] One closing sentence.
- [ ] Route to the governing document where exact behaviour matters.

### Playground, by profile

- [ ] Disposable exploration: decision, state, basic keyboard path, safe rendering, disposal.
- [ ] Shared decision aid: adds full state handling, accessibility, persistence, provenance, output and recovery.
- [ ] Executable or sensitive tool: adds the full fixture matrix, the consumer, authorisation and abuse review, migrations, observability and release ownership. At this point it is usually a product, not a playground.

A playground that grows a new lifecycle (saving, sharing, executing) reopens the review. Row statuses for a playground matrix: verified, observed, judgment, not applicable with a reason and what would invalidate it, blocked, failed. Never "done" or an empty box. Contradictory evidence reopens a row.

Rows to cover: role scenario and consumer; adopt, adapt or avoid for the chosen kind; adjacent routing; scope and non-goals; reversibility and escalation; source roles and duplicate identity; claim evidence, freshness and conflicts; one typed state; validated transitions; recovery from invalid input; semantic undo and redo; derived layout kept apart from meaning; preservation of values behind hidden controls; keyboard and pointer equivalence; alternatives to focus and hover; structure beside canvas or SVG; safe rendering; output context and consumer; persistence, migration and privacy; source anchors; responsive, error, loading and zoom states; browser, console, network and build; owner and invalidation.

Release when the required rows have evidence in proportion, failures are fixed, blockers are resolved by policy, residual risk has an owner and a sceptical reread is done.

### Handoff

- [ ] Claims sampled against sources in both directions.
- [ ] Cold restatement by a reviewer.
- [ ] Reader prediction, or `not_evaluated`.
- [ ] Hash, commands, working directory and browser conditions recorded.
- [ ] Owner and refresh triggers named.
- [ ] Source footer or inline attribution present.
- [ ] The page reconciled against its brief; differences recorded.
- [ ] The matrix of conditions tested, the outcomes and the risks recorded.
- [ ] Companion detail exists without hiding anything essential from the page.
- [ ] A final end-to-end reread, the narrow keyboard path and every high-risk condition done. Warnings, exceptions and whole-page contradictions reviewed.

## Adjacent Reference Routing

Route to the reference that owns the reader's next authoritative decision. "Nearest" means fit of scope and verification, not similarity of filename. The explanation may stay as an orientation layer. It keeps no authority over exact work that another artifact defines.

### Handoff procedure

1. State the unresolved decision in one sentence, and the consequence of getting it wrong.
2. Identify the capability that governs that decision: implementation, testing, prompt construction, state persistence, current documentation, evidence adjudication, or release operation.
3. Preflight the destination before handing off: that it exists, its stated purpose, its authority, and its verification gate. Read enough of its scope to establish fit, then load its details on demand.
4. Carry the reader and the evidence context forward, and define what result returns control or completes the task.

Handoff payload:

```text
reader and prerequisites :
starting state           :
unresolved decision      :
consequence              :
sources already loaded   :
settled claims           :
evidence labels          : source fact | source-reported | observed |
                           inference | analogy | unresolved
open question            :
destination              :
expected gate            :
return or completion     : what result hands control back or closes the task
```

Keep the payload compact. Carry decisions and evidence, not the whole explanation. Missing authority, changed confidence and unclear ownership must be visible to the receiving artifact.

If no adequate authority exists, keep the bounded explanation, name the missing authority and record the gap. Do not pick a plausible file to avoid admitting that the route is unresolved.

Examples of trigger, what to carry, and what closes the handoff:

| Trigger | Carry | Closed when |
| --- | --- | --- |
| The reader understands prompting in concept and must now write or evaluate a prompt | Audience, desired decision, sources, claim boundaries, a failure fixture. The prompt guidance governs structure; the explanation governs why the choices matter | The prompt has an inspectable contract and gate, or a prompt-specific question comes back |
| The task becomes defining an agent or its context instructions | Agent goal, trigger conditions, constraints, evidence state, assumptions made in the explanation | The agent definition is reviewable and its behaviour can be tested |
| The concept becomes test-first implementation | Behaviour contract, current test state, source-specific caveats, expected evidence | The behaviour has current test evidence and a recorded next step or completion |
| The reader must preserve or resume long-running context | Objective, settled decisions, exact paths, current evidence, open uncertainty, ownership boundary | A fresh agent can resume without rebuilding hidden assumptions |
| A claim depends on current API or product behaviour | The exact fact to verify, with static local prose marked insufficient for freshness. Current official documentation outranks an old teaching example | The fact has current authoritative support, or stays explicitly unresolved |
| Sources disagree and the task needs convergence | Each claim, source, condition and consequence, with no averaging of positions | Resolved with evidence, narrowed to a bounded uncertainty, or escalated to an owner |
| Explaining a branch or release concept turns into executing it | Repository state, test evidence, user intent, changes owned by others, prohibited operations | The outcome is verified, or a blocker and a safe next step are recorded |
| The output becomes a generated image | Subject, audience, visual purpose, factual boundaries, inspection criteria | The image conveys the model and adds no unsupported visual claim |

Graded routing. Good: explain test-first feedback briefly, then send exact phase behaviour and evidence recording to the test-first workflow with the behaviour contract intact. Bad: send a question about current API behaviour to a static analogy because both mention AI. Borderline: link the prompt guidance but drop the source-specific status of a performance number; the topic survives and the evidence boundary does not.

Four routing faults:

- Premature: the reader crosses several files for one simple concept.
- Delayed: an analogy is left governing commands or contracts.
- Circular: responsibility is passed around and the decision is never resolved.
- Dead end: the destination has no suitable gate or owner.

Split when the adjacent artifact has its own source of truth or its own verification duty. Otherwise embed the small necessary detail and keep one authority.

Verify a route by checking six things: the destination exists, its scope fits, it has authority, the payload arrived intact, the destination's gate ran, and the original open decision is closed. The return condition is what keeps a handoff from becoming abandonment. Keep a light record of repeated routes and unresolved gaps; over time it shows duplicate authorities, cycles and missing bridges. Aim for the shortest maintainable path to a verified decision, not the largest network of links.

### Destinations

Route by composition. This skill owns the explainer format: acts, metaphors, components and gates. The subject's own reference owns the technical truth. Exploration skills own the search machinery, so do not answer questions about exploration tactics from the one-line summary given here. A question about metaphor quality needs both the format guidance and fidelity to the subject. For print or slide output no equivalent method is established in the sources; say so and keep only the invariants, without stretching the HTML rules.

| The request is really | Go to |
| --- | --- |
| A recommendation, approval memo or argument | [structured-writing](../structured-writing/SKILL.md) |
| Finding the code paths before explaining them | [codebase-navigation](../codebase-navigation/SKILL.md) |
| Reviewing or verifying a change | [review-verify-debug](../review-verify-debug/SKILL.md) |
| Requirements, acceptance tests and traceability | [executable-specs](../executable-specs/SKILL.md) |
| Writing or merging a skill file | [authoring-skills-and-references](../authoring-skills-and-references/SKILL.md) |
| Comparing options before a decision | [explore-and-decide](../explore-and-decide/SKILL.md) |
| Authored imagery or generative art | An image or generative-art skill |
| A settled operational interface | Frontend engineering with tests |
| An explorable 3D scene | A 3D or visualisation toolkit |
| Exhaustive lookup | Reference documentation |
| Current product or API facts | Current official documentation |
| Temporal or causal branching over time | A timeline or simulation tool |

Within this skill:

- Terminal or copy and paste: ASCII.
- Staged understanding in a browser: HTML explainer.
- Plain-English orientation: ELI5.
- Exploring counterfactuals: playground. It stays primary while reversible controls and projections explore a bounded decision before a saved candidate, explanation, prompt, query, review or handoff. Route when the interaction is really navigation, the output is already settled, or another artifact owns the goal. Move to a product when the population and workflow stabilise, the comparison collapses to one operation, permissions, collaboration, reliability, audit or support dominate, real systems change, or the controls no longer affect decisions. Move to an explainer when the counterfactuals add no information. Move to art when visual authorship is the outcome.
- One primary reference owns the core workflow and supporting references own narrow contracts. Pass explicit data and verification at each boundary. A playground may emit a palette, seed, density or motion setting, or a versioned candidate. It cannot claim final media, causal validity or production acceptance.

Keep ASCII primary for raw fixed-width command help, logs, source-controlled runbooks, terminal walkthroughs and review notes. The lowest-capability surface that is required sets the baseline. A richer surface cannot become necessary unless the contract says so. Do not keep ASCII primary for filtering, zoom, detail on demand, semantic navigation for assistive technology, very dense comparison, animation or 3D. A terminal summary may stay for logs and failure recovery only if its reader task is complete and no safety-critical state is silently left out.

One subject, three media: a deployment flow fits ASCII for pull-request review and for pasting into an incident; HTML for interactive evidence per stage; a structured memo for persuading an approver about a staged rollout.

A destination needs its scope confirmed. Transfer is not automatic. Verify why ASCII fails, not merely that another technology renders. When moving to another medium, carry the questions, section jobs, omission routes and verified terminology, and redesign the fixed geometry.

Hybrid: an ASCII spine owns incident order; a browser explorer owns optional detail; name which one is authoritative for volatile labels, for duplicated semantics, for synchronisation and for a reader with degraded capability. To choose between media cheaply, run the probe that discriminates: resize the HTML, traverse it by keyboard, render the raw fallback, sketch the dense data, or remove the geometry and see what is lost.

For an HTML explainer there are three outcomes. Retain it for a bounded browser journey that opens directly. Pair it with another artifact for lookup, terminal use, operations or a different reader moment. Replace it when another medium or runtime carries the outcome better. A handoff from an explainer includes the reader and starting state, outcome, thesis, source and claim ledger, scope and non-goals, unknowns, ownership, and proof that the destination fits.

Subject truth may move between media when the source, scope and conditions stay identical. Evidence about rendering, interaction, accessibility and comprehension must be collected again for each medium.

Background on working with language models in large codebases is in [A00-LLM-Principles01.md](../../A00-LLM-Principles01.md) and [A01-LLM-Workflow01.md](../../A01-LLM-Workflow01.md).

## Source Evidence Mapping Table

| Material merged here | What it contributed | Where it landed |
| --- | --- | --- |
| Personal act-based visual explainer skill and its HTML template | Five-stage process, act table, teaching rules, component markup, ten author checks, `.prd/ELI5/` convention, `assets/template.html` | SKILL.md HTML section; Theme Specific Artifact; Verification |
| Standalone HTML explainer skill, its pattern guide, generator and template | Seven-act default, source-reading rules, component palette rules, guardrails, finish checks, `scripts/create_elegant_explainer_html.py`, `assets/elegant-explainer-template.html` | SKILL.md HTML section; seven beats; Bundled files |
| ASCII diagram layout skill with four references and a validator | Page systems, figure skeletons, grid rules, review checklist, `scripts/check_ascii_diagram_quality.py` | SKILL.md ASCII section; skeletons; Verification |
| AI-native ELI5 skill and its ready-made note | Reader defaults, writing rules, analogy map, output shape, guardrails, the worked note | SKILL.md ELI5 section; Worked Example Set |
| Pattern digest on AI-native explanation | Brief fields, fidelity versus comprehension, anti-patterns, evidence labels | Thesis; briefs; registries; Evidence Boundary Notes |
| Pattern digest on ASCII layout | Run card, reader-question mapping, repair order, failure modes, retry ladder, scale dimensions | ASCII tables throughout |
| Pattern digest on HTML explainer pages | Gates A to C, rendering conditions, brief and storyboard, failure table, completeness groups | HTML tables throughout |
| Pattern digest on interactive playgrounds | Canonical state, six kinds, decision packet, hazards, failure table, fixtures | SKILL.md playground section; playground tables |
| Pattern digest on the visual explainer method | Core trio, invariants, decay modes, inventory, metrics | Thesis; inventory; metrics |
| Third-party playground plugin | Ideas only: single-file shape, live preview, prompt-style export, presets, per-kind layouts and subjects | SKILL.md playground section; layouts by kind |

### Sources

- Owner-authored skills: a personal visual explainer skill; an HTML explainer skill with generator and template; an ASCII diagram layout skill with references and validator; an AI-native ELI5 skill with a reference note.
- Owner-authored pattern digests on the five subjects listed in the table above.
- Third-party: the `playground` plugin for Claude Code, from a Claude plugin collection (the copy read did not record its publisher or licence). Its skill file and six templates were read ( code map, concept map, data explorer, design playground, diff review, document critique). It was used for ideas only. No passage was copied. Where its templates use raw markup injection, regex rendering, nearby-line matching, timestamp identifiers, pointer-only canvases or exports read from the DOM, this skill replaces them with the rules in SKILL.md.
- Inspiration named by the personal skill: the "How LLMs Work" visual essay by Paras Chopra (paraschopra.github.io/how-llms-work/). Not re-fetched; liveness unknown.

## Evidence Boundary Notes

Label a statement when you reuse it. Unlabelled statements default to inference. A finding that something is absent carries a date; it is not proof the thing never existed. Audit a source clause by clause, since a check of heading shape alone can miss its most important negative claim. Recommending the format on the coherence of its design is sound when the inference label travels with the recommendation.

| Label | Meaning |
| --- | --- |
| Source fact | Stated in the local source material |
| Source-reported measurement | A number the source reports; not re-measured |
| Observation made now | Seen while doing the current task, with command and result |
| Inference | Derived from combining evidence |
| Illustration | An example that was not observed |
| Policy or guardrail | A target someone chose, not a result |
| Recommendation | Editorial advice |
| Unrefreshed external pointer | A link or product fact not checked recently |
| Unresolved or conflicting | Sources disagree, or nobody has checked |
| Owner decision | A local override by whoever owns the artifact |

Boundaries that apply to this skill:

- The teaching rules (metaphor first, one concept per act, mystery opening) are doctrine from the sources and a design inference. No reader study backs them.
- "67% faster" and "90% fewer bugs" are source-reported claims about AI-native practices. They were not verified.
- Canvas widths 72, 84 and 96, prose 52 to 64, and screenfuls of 20 to 40 lines are authoring defaults.
- The template facts (fonts, breakpoints, reveal behaviour, navigation) and the generator facts (escaping, overwrite refusal, seven acts) were observed in the bundled files. The check results in Verification Gate Command Set were observed once in one environment.
- An older note said the personal template could not be inspected. It is now bundled as `assets/template.html` and was inspected, so that caveat no longer applies. The rebuild-from-markup path stays for a missing file.
- Component class names are conventions of the bundled templates, not standards.
- The journeys and graded examples are illustrations.
- No current browser, framework, accessibility-standard, security or product behaviour was researched. Do not infer any from this file.
- Authority is specific to the claim. A writing method does not validate a performance number. An analogy does not prove a naming rule. An automated check does not establish correctness. Reader feedback shows usability, not engineering truth.
- Confidence has separate dimensions: source identity, authority, applicability, freshness, directness, reproducibility, coverage, independence, consequence. Two copies of one file are one fact. One keyboard task in one browser supports only that path. "Current browsers reliably support clipboard access" is unsupported without a retrieval and a test matrix.
- Labels govern reuse, refresh, testing and escalation. They do not confer quality. A label per claim is needed where a wrong class would change implementation or release. A fact derived from structure (a count, an ordering) is its own class.
- Local playground material supports historical examples of interaction, state and output. It does not support current browser or framework behaviour, a target's architecture or policy, universal accessibility, security, latency, reliability, authorisation, user outcomes or adoption.
- Coverage has parts: positive, negative, recovery, migration and environment. A parser fixture can establish syntax for one version while authorisation and usefulness stay unresolved.
- Illustrative identifiers, latencies, radii and counts never become a target's defaults without evidence.
- Audit strong verbs: requires, prevents, proves, reliable, always, never. For each high-consequence claim reopen the source, reproduce any runtime observation, look for conflicts and not-evaluated states, keep illustrative labels, and check both directions: claim to source, and source to decision.
- Evidence transfers only when claim, scope, version and conditions are identical. A change to the artifact invalidates the proof that depends on it.
- The reliability tiers, workload signals, retry rules, record lists, performance method, scale boundaries and fallback controls in this file are bounded engineering synthesis. They are not current normative evidence, specialist review or reader data.
- Reusable evidence packet: reader and outcome; thesis and scope; claim ledger; conflicts and unknowns; path and hash; conditions; exact methods and results; notes marked illustrative; owner; refresh trigger; residual risk.
- Apply labels to causal, quantitative, historical, normative and action-bearing claims. Connective prose needs less. Split a sentence that mixes two statuses.
- An external fact counts only when the page was opened and is authoritative, dated, versioned and applicable. An unvisited link supports nothing.
- An inference carries its reasoning, its boundary and what would reverse it.
- A provenance label is routing metadata. It is not a certificate of truth. Check labels against the complete passage, its conditions, authority, version and confidence, and check them again in derivatives.
- A derivative carries the governing claim, its status, its conditions, its authority and its refresh trigger.
- Classify the smallest material claim. A source path proves that evidence exists. It does not prove entailment, applicability or freshness. Label defaults, rejection rules, numeric and compatibility claims, volatile behaviour and disputed guidance explicitly; one label for a homogeneous passage is acceptable.
- An observation of an artifact holds for the named candidate under the recorded command, canvas, renderer, terminal and reader task. It is not universal. A local fact stays bounded by audience, surface and version.
- An unresolved item names the affected decision, the containment, the owner or route and the next probe.
- Provenance, confidence and applicability are independent. A narrow local fact may be certain; a synthesis stays a judgment; an authoritative external specification may be stale. Describe limits in words, not invented confidence scores.
- When a source or a render changes, update claims, examples, search prompts, reliability evidence and regression fixtures together.

## Future Refresh Search Queries

Nothing here was refreshed against the web. Use these as leads. Order of refresh: the target project's manifests, lockfiles, source and tests; then the official publisher; then release notes; then community sources for alternatives and failure reports; then reproduce in the target. Never put private code, credentials, customer data or internal host names in a query.

If browsing is not authorised, keep the local evidence, mark changing behaviour for the owner to verify and narrow the claims. Start from the stale or missing claim and the selected mechanism, version, consumer and authority, not from the title of the topic. Reject snippets, pages with an unclear publisher, version or environment, pages about a different threat, framework, browser or consumer, generated summaries, anecdotes from unresolved issues and sources that conflict with the target. Keep conflicts; do not average them. Add a query for the real consumer's parser, version migration and escaping. After a refresh, rerun the implicated state, browser, accessibility, security, migration, performance and consumer gates.

Good queries name a behaviour and an authority:

```text
site:developer.mozilla.org Clipboard writeText permissions browser compatibility
site:developer.mozilla.org prefers-reduced-motion media query
site:developer.mozilla.org IntersectionObserver threshold rootMargin
site:developer.mozilla.org IndexedDB versionchange transaction abort migration
site:developer.mozilla.org Web Workers terminate message event structured clone
site:w3.org/WAI ARIA Authoring Practices keyboard drag and drop alternative
site:w3.org/WAI WCAG reflow focus visible
site:owasp.org DOM based XSS prevention innerHTML textContent sanitization
site:react.dev preserving and resetting state keys official
site:w3.org performance timeline user timing specification marks measures
CommonMark fenced code block info string whitespace handling
<renderer name> code block line wrapping monospace width
<terminal name> tab width default
Google Fonts css2 import privacy self-hosting
```

Weak queries: "ascii diagram layout best practices", "best explainer page design". They return opinion without an authority or a behaviour to test. They leave out the task, surface, authority, version and failure. Broaden one dimension at a time, only to learn changed terminology, and record what unlocked the primary evidence.

What to do with each ASCII lead:

| Lead | Handling |
| --- | --- |
| Fenced code behaviour | Prefer the specification and the exact rule that applies |
| Renderer wrapping or collapse | Official documentation and release notes; confirm the deployed version; copy the exact candidate |
| Terminal alignment | Test bytes, font, tabs and the ASCII vocabulary on the named terminal and version |
| Validator change | Inspect local history and tests first |
| Accessibility of text diagrams | Decide which medium's guidance governs; do not transfer it silently |
| Renderer defect | Reproduce it and look for an official fix or release note before making it a rule |
| Stale external evidence | The known primary source first; a terminology-neutral search if the naming changed |
| New example | Use it to discover alternatives; it never outranks the canonical workflow |

Refresh order for ASCII: local corpus and tool history; the direct primary source; targeted discovery; a probe of the exact artifact; then update the synthesis and the regression evidence together.

Local probes:

- Vocabulary fingerprint of a successor method: "metaphors first, code second", "one concept per act", "mystery opening". A successor counts only when it carries the process structure, not the slogans.
- Template presence: both files exist in `assets/` and the generator runs.
- Liveness of the inspiration link in Sources.
- Validator behaviour after any edit to `scripts/check_ascii_diagram_quality.py`: rerun the mutation tests.

External pointers recorded by the sources and not refreshed: developers.openai.com/codex/guides/agents-md, docs.github.com/actions, agents.md. The first is a future check on repository-instruction behaviour and cannot decide a page system, width, connector or figure type. The second is a future check on running a file-backed validator in automation and cannot prove readability, alignment or comprehension. The third is a portability comparison for instruction structure and cannot override local ASCII rules or project instructions. A link that loads is not semantic support. Refresh an external claim only when it is volatile and could change implementation or completion. Record the URL, owner, date checked, version or section, the claim supported, any conflict, the action changed and the remaining uncertainty. Record confirmations that changed nothing as well.

Record each refresh with the refresh record in Theme Specific Artifact. Track each lead as discovered, inspected, reproduced, then reconciled or rejected. Search rank and repeated summaries do not advance a lead. Stop when the claim is resolved for the declared surface and the uncertainty is removed or bounded; then update the source notes, guidance, examples and fixtures together. Retire a query when the authority or the terminology changes, and keep the decision it led to. Prefer refresh on an event (a regression, a release, a new surface, a stale claim). Periodic checks are for external surfaces that are actively depended on.

Start from a named claim that is stale, conflicting or unknown. Use the listed query if it helps, record refinements separately, inspect the precise primary source, and stop when the claim is supported, narrowed or explicitly unresolved. Record page or revision, section or path, date, proposition, scope, contradictions, confidence and the consequence for the artifact. Reconcile with local and subject evidence, then rerun the affected claim and browser gates. Search is the wrong method for local comprehension, for an owner's intent, or for an artifact you can inspect directly.

Refresh an external claim when it is normative, versioned, sensitive to compatibility, security or accessibility, or dependent on a current API or service. A public or regulated page needs current primary standards, not an archived template. Search snippets, site roots and a domain's reputation help navigation and prove nothing. Cite an external source only when removing it would leave a recommendation unsupported. Mark a refreshed claim stale again when the dependency, browser matrix, delivery environment or requirement changes.

A query is a plan, not evidence. Run one only on a trigger: a mapped source, a product, an example, a command or a reader check changed. Use local sources for local behaviour, official documentation and release notes for current products, primary studies or local measurement for outcomes, and representative readers for teaching effect. Reject results that are undated, for the wrong version, circular, or written for search ranking. Popularity is not authority. Keep volatile examples modular so one can be replaced without rewriting the note. There is no universal refresh interval.

Leads for an ELI5 note on AI-native engineering: changes to the local method or subject source; official documentation on context windows and caching; research on long-context behaviour, test-first development and naming; public implementation examples; release notes; research on how readers learn from explanations.
