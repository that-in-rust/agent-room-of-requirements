# Interactive Playground Template Patterns

Use this reference to build a **decision laboratory**: an interactive artifact in which a user changes meaningful state, sees an honest consequence, compares alternatives, and exports or records a decision that remains understandable outside the playground.

A playground is not defined by sliders, a two-column layout, dark styling, or prompt generation. Those are historical implementation choices. The durable contract is:

```text
accepted user question
        |
        v
canonical typed state <---- presets, direct manipulation, undo, import
        |
        +----> truthful preview or analysis
        |
        +----> explanation of constraints and invalid states
        |
        +----> actionable prompt, config, query, review, or state export
        |
        v
comparison, recovery, authoritative handoff, and verification
```

Every visible control and direct manipulation writes through validated transitions to one canonical state model. Every preview, summary, prompt, code fragment, comment set, and saved state reads from that model. If two projections disagree, the user cannot reproduce the decision and the playground has failed even if both views look polished.

**Choose the mode from the decision**

| Mode | User decision | Primary interaction | Truthful output |
|---|---|---|---|
| Design explorer | Compare spacing, typography, color, layout, responsive, and interaction choices | Grouped controls plus direct preview interaction | CSS or component direction with explicit context and nondefault choices |
| Data explorer | Compose queries, APIs, pipelines, schedules, or transformations | Structured rows, field pickers, ordering, and validated expressions | Executable candidate plus schema-aware specification and validation limits |
| Concept map | Mark knowledge, include concepts, and relate ideas or tasks | Keyboard-accessible node list plus optional spatial canvas | Learning request, dependency map, or scope record using selected relationships |
| Document critique | Decide which suggestions to accept, reject, revise, or discuss | Anchored suggestions, filters, comments, and status transitions | Approved changes, retained objections, and stable document references |
| Diff review | Attach findings to exact changed content and decide disposition | File and hunk navigation, stable line anchors, comments, and severity | Structured review comments with file, side, line, context, and rationale |
| Code map | Inspect architecture, filter relationship types, and annotate components | Searchable graph, layer or relation filters, focus, and comments | Provenance-bound architecture feedback and selected impact paths |

Use the nearest mode only when its state and output semantics fit. A document critique is not a diff review merely because both show lines; a diff needs old and new sides plus hunk identity. A code map is not a concept map when edges claim real imports, calls, or data flow; those claims need provenance.

**Minimum semantic contract**

| Responsibility | Required behavior | Failure if omitted |
|---|---|---|
| Decision statement | Name the user's uncertainty, available choices, consequence, and authoritative next step | Interactivity accumulates without resolving a question |
| State schema | Define typed values, defaults, valid combinations, version, and provenance | Controls create impossible or unrecoverable combinations |
| Transition model | Validate all control, preset, import, undo, and direct-manipulation changes | Different inputs bypass constraints or update only part of the UI |
| Preview or analysis | Render exactly the state and disclose approximation, truncation, loading, and error | Visual confidence exceeds what the artifact actually computed |
| Explanation | Show why a state is invalid, partial, simulated, or unsupported and how to recover | The user cannot distinguish a bad choice from a broken tool |
| Output projection | Export only supported decisions with enough target context to act without the playground | A value dump or screenshot loses intent and constraints |
| Comparison | Preserve named alternatives or before-and-after difference when comparison drives the task | Users rely on memory and cannot explain why one option won |
| Recovery | Reset deterministically and provide undo or equivalent reversal for consequential edits | Exploration becomes risky and presets destroy work silently |
| Accessibility | Give every operation a keyboard path, visible focus, programmatic name, and nonvisual equivalent | Canvas, color, hover, or drag becomes the only usable interface |
| Safety | Treat imported data and user text as data, never executable markup or code | A local tool turns untrusted content into script or markup injection |
| Verification | Exercise state, renderer, output, viewport, input, error, and round-trip behavior | A polished initial state hides broken combinations and handoff |

**Recommended workflow**

1. **Freeze the decision.** Write one sentence naming what the user should understand, compare, configure, or review by the end. Route product policy, architecture truth, or legal meaning to its owner first.
2. **Inventory state.** Separate authoritative source data, user decisions, derived values, transient UI state, and external validation. Only decision-bearing state belongs in saved output.
3. **Select controls by semantics.** Use toggles for binary choices, segmented controls for small exclusive sets, menus for larger sets, typed inputs for exact values, sliders only for bounded perceptual exploration, and direct manipulation when spatial action is the decision itself.
4. **Define invalid combinations.** Disable impossible transitions with an explanation or accept them into an explicit error state. Never normalize silently into a different decision.
5. **Design the first frame.** Load a coherent default that teaches the interaction, shows real or clearly illustrative content, fits the target viewport, and leaves the next action discoverable.
6. **Implement one state path.** Make control, state, preview, explanation, and output agree for one representative decision before adding breadth.
7. **Add comparison and recovery.** Presets should be named alternatives that change the whole relevant state; reset restores documented defaults; undo restores semantic decisions rather than only pixels.
8. **Handle the entire state space.** Include empty, loading, invalid, unavailable, oversized, imported, stale, and partial states that the chosen mode can encounter.
9. **Make interaction multimodal.** Pair drag with keyboard movement or list editing, hover details with focus and selection, color with text or shape, and canvas or SVG with a navigable structured representation.
10. **Build the handoff.** Generate a prompt, configuration, query, review packet, or state file from validated canonical state. Include target context, nondefault decisions, unresolved questions, and limitations.
11. **Verify in the real browser boundary.** Test controls, focus, clipboard fallback, persistence, import, viewport layout, reduced motion, zoom, console errors, and the authoritative downstream validator where one exists.
12. **Promote deliberately.** A disposable local HTML file can remain lightweight. Sharing, embedding, persistence, collaboration, privileged data, or production decisions require schema ownership, threat review, migrations, compatibility, and operational support.

**Direct fit**

Use a playground when several reversible variables interact, perceptual or structural feedback changes the decision, users benefit from comparing alternatives, and the result can be validated or handed to an authoritative system. Strong examples include component styling, schema-aware query composition, architecture exploration, line-anchored review, and knowledge-gap mapping.

Use a static explainer when the choices are fixed and interaction adds no information. Use a conventional form when users already know exact values and only submission matters. Use an editor or IDE when free-form text or code is the central artifact. Use a notebook when computation and narrative are primary. Use the production domain tool when permissions, collaboration, irreversible actions, or exact runtime semantics matter.

**Boundaries**

- A preview is not production evidence unless it executes the same authoritative renderer and data boundary.
- A generated query or configuration is a candidate until the target parser, compiler, service, or reviewer accepts it.
- A code or concept map must distinguish source-derived nodes and edges from user hypotheses and layout-only proximity.
- Line comments require stable content anchors; line numbers alone drift after edits.
- A prompt is one export format, not a universal completion condition.
- A single-file, inline-CSS-and-JavaScript artifact can be an excellent portable prototype, but it is a deployment choice with maintainability, security, testing, and bundle-size costs.
- Instant feedback means no deliberate submit step for reversible local decisions; it does not promise an unsupported latency number or permit expensive work on every keystroke.

**Good, bad, and conditional use**

Good: a data explorer stores a validated query AST, renders escaped syntax, explains unsupported joins, compares two named candidates, and exports both the query and schema context. The target parser confirms the exported candidate.

Bad: a design toy exposes many unlabelled sliders, writes raw values into a prompt, has no reset, and renders only one wide viewport. It is interactive but does not preserve intent or support a reliable handoff.

Conditional: a code map is prepopulated from a one-time repository scan. It is useful for orientation if every node and edge names provenance and scan revision. It must not claim current architecture after the source changes until refreshed.

This reference does not choose a frontend framework, state library, visualization engine, domain schema, aesthetic target, or production service objective. It supplies a decision, state, rendering, safety, accessibility, output, and verification model. The durable artifact is a reversible and inspectable choice whose meaning survives beyond the browser session.

## Source Evidence Mapping Table

The fourteen local paths are seven byte-identical archive/live pairs. Preserve both locators for lineage, but count each unique artifact once. Complete local reads establish historical content only; they do not establish current browser support, accessibility, security, target data accuracy, or user outcomes.

| Unique artifact and SHA-256 | Locators and inspection state | Direct historical contribution | Material limit | First target gate |
|---|---|---|---|---|
| Playground skill, `521a3d62211e5f47b65ed17b660e001b15cf8d88d058cbf31bc00e889bcb63cc` | Archive and live `plugins/playground/SKILL.md`; complete read; pair identical | Six mode routes, portable single-file default, live preview, prompt output, presets, one state object, and common mistakes | Dark theme, prompt-only export, external-dependency prohibition, and immediate update are historical defaults rather than universal requirements | Fix one real decision, define state and output authority, then test control-preview-export agreement |
| Code map template, `0eb7c0d1ac3dbd1401c4a2348631e7be2a02ec30739dd514aab6f162cfade77f` | Archive and live `templates/code-map.md`; complete read; pair identical | SVG nodes and typed edges, layer and relation filters, zoom, component comments, prompt synthesis, and real-data prepopulation | Hard-coded coordinates, color semantics, generated markup, timestamp comment IDs, and asserted architecture lack freshness and accessibility controls | Bind nodes and edges to source revision, add keyboard or structured graph access, and test unsafe text handling |
| Concept map template, `153810786435a1f3e3948aba075ebf3c887df827464bebca61f48ce7974e9622` | Archive and live `templates/concept-map.md`; complete read; pair identical | Direct manipulation, knowledge-state cycling, typed user-created relationships, node inclusion, auto-layout, and learning-oriented output | Canvas hit testing, drag, hover, and fixed simulation counts can exclude nonpointer users and confuse spatial layout with semantic truth | Provide list and keyboard operations, preserve user edges, label layout derivation, and verify round-trip state |
| Data explorer template, `4b884e4b400f3af82b7f33210c5c2017a5296cab16f1496963bd42061a1fe342` | Archive and live `templates/data-explorer.md`; complete read; pair identical | Structured source, field, filter, grouping, ordering, and limit decisions with syntax or pipeline preview and contextual prompt | Regex replacement into `innerHTML`, slider-only exact values, and sample schemas do not establish safe parsing or executable validity | Represent output as a typed model, escape rendered text, and validate export with the target parser or service |
| Design template, `190f7da424ebd3226a679045420b64171a98d081b7d84e26be4553de13c91fe7` | Archive and live `templates/design-playground.md`; complete read; pair identical | Controls selected by design decision, style projection, light and dark context, responsive preview, and developer-facing output | Sample pixel ranges, raw inline style application, palette derivation, and framework suggestions are illustrative and may hide content, interaction, or accessibility states | Use target tokens and component content, inspect all states and viewports, and validate generated implementation guidance |
| Diff review template, `32112ba4e82fbb8b656af166d1e21f8461cedbb4fdb5d2c314c43d210ea7e37d` | Archive and live `templates/diff-review.md`; complete read; pair identical | Structured files, hunks, line sides, line comments, commit metadata, filtering, theme support, and review prompt output | DOM lookup during export, raw content attributes, mutable line IDs, emoji markers, and informal diff parsing can misanchor or expose content | Parse a frozen diff structurally, use stable side and line anchors, escape content, and round-trip comments after rerender |
| Document critique template, `c5bd7a68a53f2075d127e482c93b5f3d0b51c24bf8d301c1124801cca7be2d41` | Archive and live `templates/document-critique.md`; complete read; pair identical | Full document view, suggestion statuses, filters, comments, prompt synthesis, and prepopulated actionable feedback | Fuzzy line proximity, ad hoc Markdown rendering, raw markup assembly, and line-number-only references can attach advice to changed or unsafe text | Anchor suggestions to document revision and context digest, sanitize rendering, and test status plus output after edits |

The identical live copies show that the same bytes exist in the current workspace. They do not prove active maintenance, current use, independent corroboration, or compatibility with a chosen target.

**What the local corpus establishes**

- A useful playground centers a user decision that benefits from visual or structural feedback.
- One state object can coordinate controls, preview, and output across several interaction families.
- Mode-specific controls matter: a diff line, graph edge, filter row, design dimension, and suggestion disposition are not interchangeable values.
- Coherent defaults and named presets reduce empty-first-frame failure.
- Generated natural-language output should preserve context and selected decisions rather than dump values.
- Code maps and critiques add comments or dispositions to source material; concept maps add user hypotheses and knowledge states.
- Real-data prepopulation can make a playground immediately useful when provenance and refresh are maintained.

These are historical pattern observations, not measured outcome claims. The source does not show browser runs, keyboard evidence, screen-reader behavior, unsafe-input probes, persistence migrations, collaborative conflict handling, target parser results, or downstream user studies.

**Source hazards to carry into adaptation**

| Source shortcut | Plausible failure | Safer adaptation question |
|---|---|---|
| Raw `innerHTML` built from query, Markdown, diff, or comment text | Markup or script injection and rendering corruption | Can tokens be created as text nodes or sanitized by a tested parser? |
| Fuzzy line matching within nearby lines | Suggestion attaches to the wrong sentence after edits | Can revision, exact context, side, range, and digest form a stable anchor? |
| Canvas drag and hover as primary operations | Keyboard, touch, zoom, and assistive-technology users lose access | Is there a structured list plus focus, selection, and keyboard manipulation? |
| SVG or canvas position used as meaning | Layout proximity is mistaken for a real relationship | Are semantic edges stored separately and visibly sourced? |
| Timestamp-only identifiers | Concurrent or restored comments collide or change identity | Does the state schema define stable collision-resistant IDs and migration? |
| Re-render followed by DOM lookup for export | Comment metadata changes or disappears with view filters | Does output derive from canonical structured state rather than current DOM? |
| Sample schemas, files, nodes, or suggestions | Illustrative data appears current or complete | What source revision and refresh event govern prepopulation? |
| Fixed numeric ranges or simulation iterations | Arbitrary values become product targets or performance claims | Which target content, device, and task establish the useful boundary? |

**Unrefreshed public locations**

| Location | Possible future question | What it cannot establish here | Applicability gate |
|---|---|---|---|
| `https://developers.openai.com/codex/guides/agents-md` | Current instruction discovery and precedence if playground guidance is exposed to Codex | Playground UX, renderer safety, state correctness, or user success | Retrieve the current direct source and test target instruction behavior |
| `https://docs.github.com/actions` | Current automation, artifact, permission, and browser-test workflow behavior if GitHub Actions is selected | Product acceptance, visual quality, assertion strength, or browser support by itself | Inspect exact current features and run known-pass, failure, cancellation, permission, and artifact cases |
| `https://agents.md/` | Current file-format and scope expectations if that instruction format is selected | Domain mode, control semantics, output truth, or production deployment | Confirm supported tools, precedence, version, and repository observation |

No browsing occurred, so current external content and recommendations remain unknown.

**Target evidence classes**

| Evidence | Question it answers | Required identity | Frequent overreach |
|---|---|---|---|
| User task and decision | What uncertainty should interaction resolve and what consequence follows? | Task, audience, owner, accepted scope | Treating a feature list as user need |
| Domain schema or source data | Which values, relationships, lines, or components are real and valid? | Schema or source revision, provenance, refresh | Treating a hard-coded example as current truth |
| State contract | Which decisions, defaults, invalid combinations, and versions exist? | Schema version and migration policy | Saving transient UI state as durable intent |
| Renderer and interaction | What consequence does each state show and how can all users operate it? | Build, browser, viewport, input mode, accessibility result | Equating one screenshot with complete behavior |
| Output validator | Can the prompt, query, config, review, or state export be consumed correctly? | Export version, target parser or reviewer, result | Assuming copy feedback proves useful output |
| Persistence and sharing | Can state survive reload, import, link sharing, and version change safely? | State digest, schema, storage boundary, migration | Treating browser storage as durable collaboration |
| User-decision evidence | Can representative users compare, understand, recover, and hand off the result? | Scenario, participant role, observed outcome, limitation | Claiming usability from builder preference |

**Source disposition record**

```text
Unique artifact, locator pair, revision, and content hash
Exact historical responsibility and bounded excerpt or paraphrase
Illustrative mechanism accepted, adapted, or rejected
Input trust and data provenance
Target decision, state field, renderer, and output consumer
Keyboard, safety, responsive, error, and round-trip gates
Observed result, limitation, owner, and invalidation trigger
```

Good reuse adopts the one-state projection model, derives output from validated state, and replaces unsafe markup with structured rendering. Bad reuse copies a line-number matcher and claims comments remain attached after document edits. Borderline reuse embeds a static code map: it is useful for a bounded revision when provenance and keyboard alternatives are visible, but it becomes stale after repository change until regenerated.

A source change should invalidate only its consumers. Shared state-contract changes reopen every mode; diff-anchor changes reopen review imports; graph-provenance changes reopen code and concept maps; rendering-safety changes reopen every mode that handles external text. Provenance becomes useful when it identifies that affected set rather than merely listing files.

## Pattern Scoreboard Ranking Table

The inherited 95, 91, and 88 values are seed editorial ordering. No rubric, sample, scale, calibration, or outcome supports interpreting them as confidence, coverage, adoption, quality, or effectiveness. Preserve them for provenance; do not average them or use them as release thresholds.

| Priority | Inherited value or role | Activate when | Failure prevented | Direct falsifier |
|---|---|---|---|---|
| Source Map First | 95; historical default tier | Adapting one of the seven local artifacts or a copied implementation technique | Historical example is presented as current target policy | Every promoted responsibility names source role, rejected sample detail, target gate, and observed result |
| Evidence Boundary Split | 91; historical default tier | Historical content, real target data, public guidance, user hypotheses, and synthesis appear together | A simulated or stale view gains authority it has not earned | State and output identify which values are sourced, user-authored, derived, illustrative, stale, or unknown |
| Verification Gate Coupling | 88; historical default tier | A recommendation claims useful, safe, accessible, responsive, performant, or implementation-ready behavior | Plausible prose or one screenshot substitutes for behavior evidence | The claim names a probe, expected observation, target boundary, and failure response |
| Decision Before Controls | First construction gate | A playground request arrives as a feature list or broad topic | Controls proliferate without resolving user uncertainty | One sentence states what the user compares or decides and where the result goes |
| Mode and Domain Fit | Hard routing gate | Choosing among design, data, concept, document, diff, code-map, or custom interaction | A convenient template distorts domain identity and output | Representative state and export retain the domain's real semantics |
| Canonical State Contract | Hard implementation gate | More than one control, projection, preset, import, or direct manipulation changes the artifact | UI regions hold conflicting decisions | Every transition changes validated state once and all projections derive from it |
| Invalid-State Semantics | Hard transition gate | Choices have constraints, dependencies, unavailable values, or partial data | Silent coercion turns the user's choice into another state | Invalid combinations are rejected or represented explicitly with recovery |
| Truthful Preview | Hard interpretation gate | A visual, query, graph, document, or diff projection informs the decision | Approximation, stale data, or truncation looks authoritative | Preview states source revision, approximation, loading, error, and omitted scope where applicable |
| Safe Content Rendering | Hard safety gate | Imported schema, source, Markdown, diff, comment, query, or user text reaches the DOM | Text becomes executable markup or corrupts structure | Markup payloads render inertly and output preserves literal content |
| Equivalent Interaction Paths | Hard accessibility gate | Drag, hover, canvas, SVG, color, pointer, or gesture is used | Some users cannot inspect or modify the same semantic state | Keyboard and structured alternatives reach every decision and expose equivalent labels |
| Output Fidelity | Hard handoff gate | The playground emits a prompt, query, configuration, review, or saved state | Export omits context, includes stale DOM, or disagrees with preview | Output generated from canonical state passes round-trip and target-consumer checks |
| Comparison and Recovery | Decision-quality gate | Presets, direct manipulation, bulk changes, or exploration can overwrite work | Users cannot explain alternatives or recover from experiments | Named states compare meaningfully; undo and reset restore documented state deterministically |
| Source and Anchor Provenance | Hard real-data gate | Nodes, edges, lines, suggestions, or schemas derive from changing artifacts | Feedback or architecture claims attach to stale content | Revision and stable context identify every source-derived object and detect drift |
| Responsive and Full-State Rendering | Experience gate | The artifact runs across viewports, zoom, themes, loading, empty, invalid, and error conditions | A polished default hides overlap, inaccessible controls, or dead ends | Browser evidence covers representative state and viewport combinations without lost operations |
| Persistence and Migration | Promotion gate | State is saved, linked, imported, resumed, shared, or embedded | Old states silently change meaning or expose sensitive data | Versioned states migrate, reject incompatibility, preserve provenance, and round-trip safely |
| Authoritative Downstream Validation | Final decision gate | Export will drive implementation, execution, review, or release | Playground confidence is mistaken for target acceptance | Target parser, compiler, service, repository, or accountable reviewer accepts the exact exported artifact |

**Default construction order:** freeze the user decision and downstream authority; select the domain mode; inventory source and decision state; define schema and valid transitions; implement one control-to-preview-to-output path; add safety and equivalent interaction; cover empty, loading, invalid, error, and responsive states; add comparison and recovery; validate export; then add persistence or promotion controls if the artifact crosses sessions or owners.

**Repair override:** preserve the failing state and begin at the earliest broken contract. A markup payload elevates safe rendering. A comment attached to a shifted line elevates source anchoring. A graph that no longer matches the repository elevates provenance and invalidation. A copied prompt that omits selected constraints elevates output fidelity. A keyboard trap elevates equivalent interaction before visual polish.

Use three profiles:

- **Disposable:** synthetic or trusted local data, one session, no sharing, concise state and browser checks, deterministic reset, and explicit non-authoritative output.
- **Shared:** real or imported data, saved states, several users or downstream consumers, versioned schema, provenance, keyboard coverage, safe rendering, import and export tests, and ownership.
- **Consequential:** privileged or sensitive data, implementation-driving output, formal review, production embedding, or expensive error; add threat review, independent accessibility evidence, compatibility, audit, recovery, and authoritative target validation.

Good prioritization follows the first contract that can make the user's decision wrong or irrecoverable. Bad prioritization perfects colors while preview and export disagree. Borderline simulation may remain useful for exploration when approximation is prominent and the final handoff requires independent validation.

Numeric rank cannot rescue an invalid state model or unsafe renderer. Retain override reasons and review recurring failures. Repeated anchor drift may justify a shared source-identity layer; repeated preset loss may require transactional history; repeated export rejection may expose a domain model that is too weak. Change priority only from relevant evidence, not from the apparent precision of inherited numbers.

## Idiomatic Thesis Synthesis Statement

`historical_local_observation`: Seven unique local artifacts appear at fourteen byte-identical archive/live locators. They demonstrate a shared state object, live preview, presets, prompt export, direct manipulation, filters, comments, line-oriented review, graph visualization, and six domain modes. They do not demonstrate current browser support, safe imported-content handling, complete keyboard access, persistence migration, target-parser acceptance, or improved user decisions.

`external_mapping_unrefreshed_note`: The Codex instruction guide, GitHub Actions documentation root, and agents.md format location were inherited and not opened. They establish no current external fact in this evolution.

`systems_synthesis_or_judgment`: An idiomatic playground is a reversible compiler from a user decision into validated canonical state, truthful projections, and an actionable output whose authority is explicit. Controls and direct manipulation are input adapters. Preview, explanation, prompt, query, review packet, and saved state are projections. None may invent or silently normalize meaning.

Use this loop:

1. **Name the decision.** State audience, uncertainty, available alternatives, consequence, and the authoritative next system or reviewer.
2. **Classify source data.** Separate source-derived facts, user choices, derived values, transient UI state, illustrative samples, and remote validation.
3. **Define canonical state.** Specify types, defaults, valid combinations, provenance, schema version, and what belongs in durable output.
4. **Design transitions.** Map each control, direct manipulation, preset, import, undo, and reset to validated semantic changes.
5. **Project honestly.** Render preview and explanation from state, including empty, loading, stale, invalid, partial, unavailable, and error conditions.
6. **Preserve equivalent access.** Give every pointer, hover, color, spatial, canvas, and SVG operation a named keyboard and structured alternative.
7. **Compare and recover.** Let users retain named alternatives, inspect differences, undo consequential changes, and reset deterministically.
8. **Export from state.** Generate natural language or structured output without reading meaning back from the DOM. Include target context, unresolved questions, and limitations.
9. **Validate downstream.** Send the exact query, config, review, prompt, or state to its parser, compiler, domain tool, or accountable reviewer.
10. **Propagate change.** When source data, schema, mode semantics, renderer, output contract, or consumer changes, invalidate affected saved states and projections.

**Core principles**

- **Decision before controls.** A control exists because one state dimension changes interpretation or output; decorative controls create unexplained state.
- **One semantic source of truth.** Canonical state owns meaning. DOM, canvas positions, open panels, selected tabs, and formatted text are derived or transient unless the decision explicitly includes them.
- **Typed domain state.** A query explorer should model query structure, a diff review should model file side and line anchors, and a code map should model sourced nodes and typed edges. Strings are not a substitute for domain identity.
- **Transitions are validated.** Presets, imports, drag, keyboard, and form controls follow the same invariant checks. Invalid input remains visible with a recovery route rather than becoming another value silently.
- **Preview is evidence with limits.** It states whether data is real, illustrative, cached, partial, stale, approximate, or authoritatively rendered.
- **Output is a consumer contract.** Natural language should explain intent and nondefault choices; structured formats should preserve schema and provenance. Copy feedback proves clipboard interaction, not output correctness.
- **Interaction is multimodal.** Drag has keyboard movement or list editing, hover has focus, color has text or shape, and spatial graphs have navigable structured views.
- **Imported text is data.** Build text nodes or use a reviewed sanitizer and parser; never trust a local-file boundary to make markup safe.
- **Comparison changes judgment.** Presets are coherent named alternatives, not random sample values. Saved comparisons should explain differences and preserve the user's chosen baseline.
- **Recovery enables exploration.** Undo, reset, cancellation, and import rejection make experimentation safe. Recovery restores semantic state, not only visible styling.
- **Lifecycle is proportional.** A one-session synthetic prototype can remain one file. Shared or authoritative states need versioning, migration, access, privacy, compatibility, and ownership.

**State partition**

| State class | Examples | Persistence rule |
|---|---|---|
| Authoritative source | Schema revision, diff object, document digest, repository graph scan | Store identity and provenance; refresh or reject when stale |
| User decision | Selected fields, design values, knowledge markings, approved suggestions, comments | Save and compare when it carries intent |
| Derived state | Formatted query, graph layout, prompt summary, counts, validation messages | Recompute from source and decision state unless expensive and integrity-bound |
| Transient UI | Hover, open menu, focus ring, pending toast, drag pointer | Usually do not persist |
| Remote evidence | Parser result, server preview, repository refresh, policy review | Record artifact, environment, status, time, and limitation separately |

**Interaction selection**

Use a toggle only for a genuine binary decision; a segmented control for a small exclusive set; a menu for larger choices; a typed input for exact values; a slider for bounded perceptual comparison where exact entry remains possible; reorder controls for ordering; structured rows for repeated conditions; and direct manipulation when position, connection, or target selection is itself meaningful. Familiar icons need accessible names and unfamiliar icons need visible or hover/focus explanations.

**Complete and misleading examples**

Complete: a document critique stores document revision and context-bound suggestion anchors, lets keyboard users accept or comment, preserves rejected items as context, and exports from structured suggestion state. Editing the document marks affected anchors stale rather than moving them to nearby lines.

Misleading: a query builder inserts imported schema and values into `innerHTML`, displays colorful SQL, and copies a sentence assembled from visible DOM. It looks correct but can execute markup, omit hidden filters, and has never passed the target parser.

Conditional: a force-directed concept map uses a canvas for exploration. It remains useful when a synchronized list exposes every node, edge, knowledge state, and editing operation; layout is labeled as derived and exports ignore accidental coordinates unless spatial grouping is an explicit user decision.

This thesis does not require a dark theme, a two-panel split, a prompt footer, a specific framework, a fixed control count, an arbitrary latency, or one-file delivery. Those are options. It requires coherent decision state, honest projection, safe and equivalent interaction, reversible exploration, and a verified handoff.

The permanent artifact is not a screenshot. It is a versioned decision state, its source and assumptions, the projections that explained it, the output accepted by a consumer, and the events that make it stale.

## Local Corpus Source Map

Use the March archive as frozen provenance and the corresponding `claude-skills/plugins/playground` paths as byte-identical live locators. Hash before loading both; when bytes match, read one artifact and use the second path only for consumer and lineage discovery.

**Common skill regions**

| Source region | Retrieve when | Durable question | Historical mechanism to reconsider | Target gate |
|---|---|---|---|---|
| Description and fit | Deciding whether interactivity adds decision value | Is the choice visual, structural, comparative, and difficult to express precisely once? | Any request containing "playground" automatically triggers a build | Compare with a static explainer, form, editor, notebook, or domain tool |
| Mode routing | Choosing among six source templates | Which domain identity and output contract does the task require? | Nearest visual layout is treated as sufficient semantic fit | Run representative state and export fixtures for the selected mode |
| Portable-file requirement | Building a shareable prototype | Does one-file delivery materially improve handoff or offline use? | Inline everything and prohibit dependencies regardless of bundle, policy, or maintainability | Verify offline behavior, security policy, size, browser support, and ownership |
| Live preview | Designing feedback cadence | Which reversible state changes should update without an explicit commit? | Every input event runs all expensive work immediately | Separate local projection from debounced or cancellable authoritative validation |
| Prompt output | Choosing downstream handoff | What must a consumer know without seeing the playground? | Every mode ends in natural-language prompt text | Validate the output form actually required: prompt, query, config, review, or state |
| Copy feedback | Implementing clipboard handoff | How does the user know exact content copied and recover if permission fails? | Success toast appears without verifying clipboard write | Exercise success, denial, insecure context, unavailable API, and manual fallback |
| Defaults and presets | Designing first use and comparison | Which coherent alternatives teach the decision space? | Arbitrary values and random novelty are called presets | Validate names, full-state application, unsaved-change behavior, undo, and reset |
| State pattern | Coordinating controls, preview, and output | Which values are canonical, derived, transient, or remote evidence? | A mutable untyped object becomes sufficient architecture | Add schema, transitions, provenance, version, round-trip, and invalid-state tests |
| Prompt example | Converting numeric state into intent | Which details are necessary, nondefault, and qualitative? | Hidden defaults and unsupported target syntax disappear | Compare generated output with canonical state and downstream consumer result |
| Common mistakes | Reviewing a candidate artifact | Which historical failures remain relevant and which new boundaries apply? | List is treated as exhaustive | Add safety, accessibility, stale data, persistence, anchor, and error-state probes |

**Mode template regions**

| Mode and region | Retrieve when | Contribution to preserve | Caveat to carry | Focused verification |
|---|---|---|---|---|
| Design: layout | Comparing controls with a component or page context | Decisions remain visible beside their consequence and output | Two-panel layout can crowd mobile and primary 3D or full-page experiences | Test content order, stable dimensions, zoom, long labels, and target viewports |
| Design: controls by decision | Mapping dimensions to familiar controls | Sliders, toggles, menus, cards, and viewport controls have distinct semantics | Slider-only exact values, huge ranges, and decorative cards reduce precision | Keyboard, typed entry, min/max, step, labels, units, and reset tests |
| Design: style projection | Applying state to preview | Direct state-to-style mapping makes causality easy to inspect | Inline styles can diverge from tokens, interaction states, content, and production CSS | Render default, hover, focus, active, disabled, error, light, dark, and reduced motion |
| Design: output | Handing design intent to implementation | Qualitative direction plus concrete nondefault values is more actionable than a dump | Framework-class suggestions may be stale or incompatible | Compare output with target design tokens and implemented component review |
| Data: structured decisions | Building queries, APIs, pipelines, regex, or schedules | Repeated rows and typed selections expose domain structure | A visual builder can permit invalid joins, types, precedence, or escaping | Validate a typed AST against target schema and negative fixtures |
| Data: syntax preview | Showing query or pipeline consequence | Token categories improve inspection | Regex replacements into raw markup are not a parser and may execute input | Render escaped tokens from a parser or safe tokenizer and test hostile literals |
| Data: output | Creating implementation request | Schema context and selected operations make a prompt self-contained | Natural language may disagree with executable output | Generate both from state and compare with target parser or service response |
| Concept: layout | Mapping learning, scope, or task dependencies | Direct manipulation and relation creation can reveal mental models | Spatial position can be accidental and canvas can be inaccessible | Synchronize semantic list, keyboard operations, focus, zoom, and screen-reader labels |
| Concept: knowledge state | Marking know, fuzzy, and unknown | User state can focus a learning request | Three labels may not fit all audiences and defaulting all values can bias results | Let target owner define states; test cycle order, explicit unset, and export |
| Concept: edge creation | Adding typed user relationships | User hypotheses remain distinguishable from preloaded edges | Invalid self-edges, duplicates, hidden nodes, and direction ambiguity are unspecified | Validate endpoint existence, direction, type, duplicate policy, and undo |
| Concept: auto-layout | Reducing manual arrangement cost | Derived layout can improve readability | Fixed simulation counts and unconstrained motion do not guarantee convergence or accessibility | Measure overlap and bounds; support cancellation, deterministic seed, reduced motion, and manual correction |
| Code map: graph model | Visualizing real architecture | Nodes, typed connections, layers, filters, and source labels form a useful review model | Hard-coded graph examples can claim imports or flows not observed in code | Bind source revision and edge provenance; detect missing, duplicate, stale, and unsupported edges |
| Code map: SVG renderer | Inspecting connections and comments | SVG supports scalable shapes, paths, markers, and focusable elements | Color and dash alone, clipped labels, crossings, and pointer-only nodes reduce comprehension | Test text alternatives, keyboard focus, relation labels, zoom, pan, overlap, and filters |
| Code map: comments | Attaching feedback to components | Target, label, file, and text can feed structured output | Timestamp IDs and renderer-derived metadata are unstable | Use state-owned IDs and source anchors; rerender, filter, import, and delete without drift |
| Diff: structured diff data | Reviewing file and hunk changes | File, hunk, old/new line, line type, and content are meaningful identities | Informal parsing can lose renames, binary files, no-newline markers, and side semantics | Parse frozen fixtures for additions, deletions, context, renames, and malformed input |
| Diff: line comments | Capturing review findings | Inline comments preserve changed-code context | Current DOM lookup and visible line number may misanchor after rerender or filtering | Export from state using file, side, line, hunk context, and content digest |
| Diff: rendered content | Showing additions and deletions | Line type styling supports scanning | Raw content attributes, markup, color-only meaning, and long lines create safety and access risk | Escape text; add prefixes, labels, horizontal strategy, keyboard navigation, and zoom checks |
| Document: full-text panel | Reviewing prose with line context | Document and suggestion views make source and decision visible together | Ad hoc Markdown replacement can execute or misrender complex content | Use trusted parser or escaped text; test code fences, markup payloads, long lines, and headings |
| Document: suggestion anchor | Connecting feedback to target text | Line range and suggestion content support review | Nearby-line fuzzy matching can silently attach advice to the wrong paragraph | Bind document revision, exact context digest, range, and stale-state behavior |
| Document: dispositions | Accepting, rejecting, resetting, and commenting | Explicit statuses turn critique into a decision workflow | Counts, filters, and output can diverge after mutation | State-machine tests cover every transition, filter, comment, import, and export |
| Document: output | Producing approved changes and retained context | Grouping accepted suggestions and comments is actionable | Rejected items may leak irrelevant content or approved items may duplicate comments | Define output policy and compare exact state to exported sections |

**Progressive retrieval profiles**

- **New single-mode artifact:** read common fit, mode routing, state, output, and mistakes; then read the selected mode completely.
- **State or persistence change:** read common state, defaults, and output plus every mode's state shape; define compatibility before editing renderers.
- **Rendering safety review:** read data, diff, and document rendering examples, then inspect every target path that accepts imported or user text.
- **Accessibility repair:** read concept and code-map direct manipulation plus the selected mode; inventory keyboard, focus, labels, color, zoom, motion, and structured alternatives.
- **Review anchoring change:** read both diff and document templates because line side, document revision, context, and stale behavior overlap but are not identical.
- **Shared generator promotion:** read all seven artifacts and add target framework, design-system, security, accessibility, browser, test, import, export, migration, and retirement evidence.
- **Orientation only:** read fit and mode routing, then provide options and unknowns without claiming implementation readiness.

**Region-specific traps**

- A coherent preset can still destroy unsaved work if application is not transactional.
- A single state object can still hold invalid combinations and leak transient or sensitive values into export.
- A prompt can mention only nondefault values yet omit a default that the target consumer does not share.
- A graph can be visually readable and semantically stale.
- A line number can be exact and still refer to the wrong revision or side.
- A syntax-highlighting regex can color text correctly while parsing it incorrectly or inserting unsafe markup.
- A canvas can look interactive and remain inaccessible to keyboard and assistive technology.
- A copy success message can appear after a rejected clipboard promise.
- One viewport screenshot can hide overflow, focus loss, modal trapping, and dynamic content shift.

**Extraction record**

```text
Unique source, region, locator pair, and content hash
Historical responsibility and risky implementation detail
Target decision and domain mode
State fields, transitions, projections, and output consumer
Source data identity, trust, and refresh rule
Adapted mechanism and rejected shortcut
Safety, accessibility, browser, round-trip, and consumer evidence
Residual uncertainty, owner, and invalidation trigger
```

Good retrieval combines common state and output contracts with one fully read mode template and target evidence. Bad retrieval loads all fourteen paths, counts repetition as confidence, and copies renderer snippets into a shared scaffold. Borderline reuse adopts the single-file shell: it is acceptable for a trusted disposable handoff after offline, size, CSP, input, and browser checks; it is not automatically the right production architecture.

The local artifacts are completely known at their frozen bytes. Current user needs, target design system, browser matrix, domain data, framework, downstream consumer, accessibility acceptance, and operational behavior remain unknown. When a source region changes, invalidate only its dependents: anchor changes reopen review imports, graph changes reopen provenance, state changes reopen all saved formats, and visual examples reopen only modes that adopted them.

## External Research Source Map

No browsing occurred. These inherited locations are `external_mapping_unrefreshed_note` records, not current facts, recommendations, or evidence that a target playground uses the associated mechanism.

| Inherited location | Possible future role | Permitted use after inspection | Current disposition | Target gate |
|---|---|---|---|---|
| `https://developers.openai.com/codex/guides/agents-md` | Codex repository-instruction discovery and precedence | Clarify current placement of playground-building instructions when Codex is the selected agent surface | Retain as product-owned retrieval target; content, version, and relevance unverified | Inspect the current direct source and test target discovery, nested scope, conflict, and update behavior |
| `https://docs.github.com/actions` | Automation, permissions, browser-test artifacts, status, cancellation, and retention | Clarify exact GitHub Actions mechanisms after that provider is selected for playground verification or hosting workflow | Retain as a broad product documentation root, not a claim about one workflow | Retrieve exact feature pages and run success, browser failure, cancellation, permission denial, artifact absence, and retention cases |
| `https://agents.md/` | General instruction-file format and scope | Clarify current format interoperability if playground conventions are deliberately distributed through that file type | Retain as a possible format authority; no current content or target compatibility established | Confirm version, supported tools, precedence, scope, conflict, and repository behavior |

These locations cannot decide the user's interactive task, state schema, control semantics, visual target, source-data truth, keyboard equivalence, renderer safety, output correctness, persistence policy, or production approval.

**Missing authority categories**

Select only categories activated by the target implementation:

| Decision | Preferred authority | Local reproduction required |
|---|---|---|
| DOM, events, clipboard, storage, file, history, canvas, or SVG behavior | Current browser-platform documentation plus target browser support policy | Success, denial, unavailable API, insecure origin, quota, reload, zoom, input, and fallback cases |
| Accessibility semantics | Current accepted accessibility standard, platform mapping, and organizational policy | Keyboard-only tasks, focus order, names, roles, state announcements, color independence, zoom, motion, and assistive-technology review |
| Framework rendering and state | Current selected framework and build-tool documentation | Hydration or mount, state update, error boundary, cleanup, strict mode, production build, and browser behavior |
| Safe imported content | Current platform security policy, trusted sanitizer or parser documentation, and target threat model | Markup payloads, URL schemes, attributes, encoded forms, large input, and output escaping |
| Domain parsing and validation | Owner documentation or schema for SQL, API, regex, cron, diff, Markdown, graph, or design tokens | Known-valid, known-invalid, boundary, version, and round-trip fixtures |
| Visualization engine | Current selected graph, canvas, SVG, or layout-engine contract | Determinism, bounds, overlap, cancellation, accessibility projection, large graph, and export |
| Design system | Current target tokens, components, interaction states, and content policy | Default, hover, focus, active, disabled, loading, error, responsive, and theme states |
| Clipboard and export consumer | Browser API plus target editor, parser, compiler, service, or reviewer policy | Exact output identity, fallback, paste, parse, semantic comparison, and rejected state |
| Persistence and sharing | Storage, URL, backend, privacy, retention, and schema-governance authority | Reload, import, old version, corrupt state, oversize state, access, deletion, and migration |
| Browser automation and artifacts | Current runner, browser, CI provider, screenshot, trace, and artifact documentation | Real server URL, interaction sequence, console, network, screenshots, focus, canvas pixels, failure, and artifact retrieval |
| Production hosting and security headers | Target platform, CSP, asset, cache, deployment, and incident authority | Clean deployment, offline assumption, headers, asset failures, rollback, telemetry, and recovery |

Do not invent URLs while browser, framework, parser, runner, and hosting choices are unknown. Record the authority class and question. Add a direct locator only when retrieval can affect an actual decision.

**Refresh triggers**

Refresh an external contract when browser support changes; clipboard or storage permissions differ; a framework upgrades rendering or hydration; an accessibility requirement changes; a sanitizer or parser reports a security issue; a visualization engine changes layout or event behavior; the design system changes tokens; CI browser or artifact behavior changes; a saved-state schema migrates; or observed target behavior contradicts recorded guidance.

Local success can depend on deprecated behavior. Current public guidance can be irrelevant to a pinned environment. Preserve both observations and reconcile them explicitly.

**Future refresh record**

```text
Frozen playground decision and affected state transition
Target browser, framework, API, tool, feature, and exact version
Primary source, publisher, release or revision, and checked date
Relevant section and bounded paraphrased finding
Evidence role: platform, accessibility, security, parser, framework, or operations
Applicability, conflict, changed action, and migration consequence
Target fixture, input trust, browser boundary, and observed result
Disposition, residual uncertainty, owner, and next refresh trigger
```

Classify results as `inspected`, `applicable`, `reproduced`, `reconciled`, `rejected`, `superseded`, or `no_material_impact`. Reading a browser API page does not prove a clipboard fallback. Running a screenshot does not prove keyboard access. Passing a domain parser does not establish that users understand the decision.

**Examples**

Good future use selects clipboard export for a shared review tool, retrieves exact current browser behavior, and tests secure-context success, denial, unavailable API, large content, feedback timing, and manual fallback in supported browsers.

Bad use cites the agents.md format site to claim that a canvas graph is keyboard accessible. Instruction-file authority has no bearing on graph interaction semantics.

Borderline use consults GitHub Actions for screenshot artifacts. It becomes applicable only after the chosen browser runner, server lifecycle, permissions, failure uploads, retention, and retrieval are exercised in the target workflow. The screenshots still require semantic visual review.

Prefer event-driven refresh over bibliography growth. Retire a repeatedly irrelevant mapping while preserving why and what selected mechanism would reopen it. External evidence is complete only when the affected state, interaction, or export edge is retested locally.

## Anti Pattern Registry Table

Classify an anti-pattern only after naming the user decision, state invariant, source identity, interaction, projection, output, or lifecycle contract it violates. Similar visual form is insufficient. Contain executable content, private-data exposure, false authority, and destructive state loss before cosmetic repair.

| Anti-pattern | Cause and consequence | Detection signal | Safer response | Valid boundary or exception |
|---|---|---|---|---|
| `topic_without_decision` | A broad subject becomes a collection of controls without a user uncertainty or downstream action | Builder cannot state what changes after exploration | Freeze one decision, audience, consequence, and consumer; remove unrelated controls | Open-ended art or play can prioritize exploration when explicitly non-authoritative |
| `template_by_visual_similarity` | Nearest layout is selected despite wrong domain identity | Diff loses old/new side or code map loses source edge provenance | Select mode by state and output semantics, then adapt layout | A custom hybrid is valid when combined contracts are explicit |
| `control_theater` | Widgets expose values that preview or output ignores | Changing a control leaves one projection unchanged without explanation | Remove it or connect it through canonical state to every relevant projection | A disabled future control can appear only when clearly unavailable and noninteractive |
| `dom_as_source_of_truth` | State is reconstructed from visible elements during export or save | Filters, rerenders, or hidden panels change output unexpectedly | Generate all projections from structured canonical state | Reading native form values at one validated submit boundary can be acceptable |
| `parallel_state_islands` | Controls, preview, prompt, comments, and persistence mutate separate objects | Undo or preset updates only part of the interface | Centralize semantic transitions and derive view state | Local transient focus or hover state need not enter the domain model |
| `silent_invalid_normalization` | Impossible combinations are clamped, reordered, or dropped without notice | Imported and exported decisions differ while validation appears green | Reject with explanation or preserve an explicit invalid state and repair route | Formatting-only canonicalization is acceptable when meaning is provably unchanged |
| `hidden_default_dependency` | Output omits defaults that the downstream consumer does not share | Reproducing export elsewhere yields another result | Include required baseline identity or full state, then mention nondefault choices for readability | Omission is safe when consumer contract fixes the same versioned defaults |
| `random_preset_novelty` | Presets are arbitrary values rather than coherent alternatives | Names do not explain intent and comparisons teach nothing | Define presets as reviewed full-state hypotheses with rationale | A randomize action can support inspiration when separate from recommended presets |
| `destructive_preset_apply` | Selecting a preset overwrites work with no comparison or recovery | User cannot restore the prior state | Apply transactionally, preserve undo, and warn or save named state where consequence warrants | Disposable first-use presets can replace untouched defaults without confirmation |
| `reset_that_does_not_reset` | Reset restores visible controls but leaves comments, derived state, history, or storage | Reload and reset produce different documented defaults | Define reset scope and reconstruct canonical defaults atomically | A scoped reset is valid when its target is named explicitly |
| `preview_as_authority` | Simplified rendering is presented as production, parser, or architecture truth | No source revision, approximation, or target result appears | Label simulation and require authoritative downstream validation | Exact shared renderer can provide stronger evidence when artifact identity matches |
| `stale_preview_success` | Remote or source-derived data changes while old projection remains active | Source revision differs from preview and no stale state appears | Mark stale, cancel obsolete work, refresh, or freeze the claim to a revision | Offline frozen snapshots are valid when their boundary is prominent |
| `raw_markup_rendering` | Imported document, diff, schema, query, graph label, or comment enters `innerHTML` | Markup payload changes structure or executes behavior | Render text nodes or use a reviewed parser and sanitizer with negative fixtures | Application-generated closed markup is acceptable when every interpolated value is escaped |
| `regex_as_domain_parser` | Highlighting replacements stand in for SQL, Markdown, diff, or language parsing | Strings, comments, escapes, nesting, or malformed input render incorrectly | Parse into typed tokens or label display as non-authoritative text coloring | A bounded trusted mini-language can use tested tokenizer rules |
| `pointer_only_direct_manipulation` | Drag, hover, node click, or line click is the only operation | Keyboard-only task cannot inspect or change equivalent state | Add focusable structured list, keyboard actions, names, and announcements | Pointer enhancement is valid when all semantic operations remain elsewhere |
| `color_only_state` | Edge type, diff side, suggestion status, or validation relies only on hue | Monochrome or color-vision review loses meaning | Pair color with text, icon, line style, prefix, or shape and sufficient contrast | Decorative color may remain redundant |
| `layout_equals_relationship` | Spatial proximity or force layout is treated as semantic edge | Moving nodes appears to change architecture or dependency | Store typed edges separately and label layout as derived | Position can be user data when spatial grouping is an explicit decision |
| `unvalidated_graph_edge` | User or generator creates missing, duplicate, self, reversed, or unsupported relationship | Export contains impossible topology | Validate endpoints, direction, type, duplicate policy, source, and visibility | Multi-edge graphs can permit duplicates when identities and semantics differ |
| `stale_code_map` | Hard-coded nodes and edges outlive repository revision | Files or connections no longer exist but map appears current | Bind scan identity, expose freshness, regenerate, and preserve user annotations through mapping | Historical architecture snapshots remain valid as dated evidence |
| `fuzzy_review_anchor` | Suggestion attaches to a nearby line instead of exact revision and context | Document edit moves feedback to another sentence silently | Bind revision, side, range, context digest, and stale-state behavior | Human-assisted reattachment can be offered as an explicit unresolved action |
| `timestamp_comment_identity` | Wall-clock value alone identifies comments or decisions | Concurrent imports collide or restored records change identity | Use stable generated IDs with collision and migration rules | Local single-process ephemeral comments may use simpler IDs if never merged |
| `value_dump_output` | Prompt or handoff lists raw controls without intent, context, constraints, or unresolved issues | Consumer cannot act without reopening playground | Generate domain-language instruction or structured export from state | Raw JSON is valid when it is the documented consumer contract |
| `prompt_only_completion` | Every playground ends at clipboard text even when parser, config, review, or saved state is authoritative | Natural-language export loses exact structure | Choose output from downstream consumer and optionally add explanatory prompt | Prompt is correct when the next actor is conversational and accepts its ambiguity |
| `fake_copy_success` | Feedback appears before clipboard promise resolves or when API is unavailable | User pastes stale or empty content | Await result, announce success or failure, preserve selection, and offer manual fallback | None for authoritative handoff; failure must remain visible |
| `unversioned_browser_storage` | Saved state has no schema, provenance, privacy, quota, or migration | Upgrade corrupts decisions or exposes data on a shared device | Version, validate, migrate or reject, minimize sensitive data, and support deletion | Session-only storage can be simpler when loss and privacy boundary are clear |
| `share_link_data_leak` | URL state contains private document, diff, query, comments, or tokens | Browser history, logs, analytics, and referrers expose content | Share opaque authorized identity or redact and bound state deliberately | Public synthetic configuration can be encoded visibly with size and integrity checks |
| `render_everything_on_input` | Expensive parsing, layout, network, or generation runs on each keystroke | Typing lags, requests race, stale result wins, or batteries drain | Keep local state immediate; debounce or schedule work, cancel obsolete jobs, and expose pending state | Cheap deterministic projection can update on every semantic input |
| `rerender_focus_loss` | Whole DOM is rebuilt after each state change | Keyboard focus, selection, scroll, and comment editor disappear | Update stable keyed regions and restore focus intentionally | Full rerender can be acceptable when no user operation is active and focus is reset predictably |
| `happy_path_first_frame_only` | Verification stops at one coherent default screenshot | Empty, loading, long content, invalid, error, zoom, mobile, or imported states overlap or dead-end | Exercise a state and viewport matrix with task completion | A static artifact can narrow its declared state space explicitly |
| `single_file_dogma` | Portability requirement overrides CSP, dependency, test, bundle, or maintenance needs | Shared artifact becomes unreviewable or insecure | Choose delivery architecture from user and operational boundary | One file remains strong for trusted offline handoff and disposable prototypes |
| `external_dependency_by_accident` | CDN, font, service, or remote data is required but not surfaced | Offline or blocked network leaves a blank artifact | Bundle, provide fallback, or state network dependency and error recovery | Managed production apps can depend on governed assets and services |

**Repair order**

1. Stop rendering or sharing unsafe and sensitive content.
2. Preserve source revision, imported state, browser boundary, and failing output.
3. Prevent misleading preview or export from driving an authoritative action.
4. Repair the user decision and typed domain model before adding UI workarounds.
5. Restore one canonical state and validated transitions.
6. Add safe, equivalent interactions and explicit invalid, loading, stale, and error states.
7. Repair preview, explanation, output, persistence, and downstream validation from that state.
8. Add regression fixtures, invalidate saved consumers, and restore status deliberately.

**Controlled probes**

- Add a control that is absent from export and confirm projection-equality checks fail.
- Import an impossible state and confirm it is rejected or shown invalid without silent change.
- Inject markup through every text-bearing source and confirm it renders inertly.
- Complete each graph, review, and design task with keyboard only and at high zoom.
- Shift document and diff content and confirm anchors become stale rather than moving nearby.
- Change repository revision and confirm sourced graph edges are refreshed or labelled historical.
- Apply a preset after edits and confirm comparison plus undo restore the exact prior state.
- Deny clipboard access and confirm no success feedback appears.
- Load an old, corrupt, oversized, and privacy-sensitive saved state and inspect recovery.
- Delay remote validation while changing local state and confirm obsolete result cannot win.

Good playgrounds fail visibly when decision state, source identity, rendering safety, or output fidelity is violated. Bad playgrounds can have polished controls and instant animation while exporting a different or unsafe decision. Cascades matter: an underspecified domain model can cause control theater, silent normalization, misleading preview, rejected output, and incompatible saved states in every generated mode. Repair the earliest supported cause and invalidate downstream artifacts.

## Verification Gate Command Set

Run the focused assignment verifier from the repository root after changing this reference and packet:

```bash
python3 tests/verify_idiomatic_reference_file.py --path idiomatic-ref-202607/interactive_playground_template_patterns-20260710.md
```

Then run the archived shared-generation contract:

```bash
python3 agents-used-monthly-archive/idiomatic-references-202606/tools/verify_reference_generation.py --stage final
```

These commands verify reference structure. They do not open a playground, exercise controls, inspect pixels, test accessibility, reject unsafe content, migrate state, validate output, or prove user success.

Discover target artifacts before binding commands:

```bash
rg --files | rg '(^|/)(package.json|vite.config|playwright|cypress|tests?|src|public|fixtures?|schemas?|workflows?|design-tokens|stories)(/|\.|$)'
```

Inspect project instructions, package scripts, framework entrypoint, state schema, domain parser, browser matrix, design system, accessibility policy, CI, hosting, screenshot storage, and downstream output consumer. A filename match is discovery only.

| Claim | Required gate | Passing observation | Limit |
|---|---|---|---|
| Frozen source was interpreted accurately | Reopen selected source regions, compare pair hashes, observation, and caveat | Seven-artifact and fourteen-locator identity plus bounded extraction agree | Historical accuracy does not establish target fitness |
| Canonical state is valid | Parse defaults, presets, imports, and transition results against a schema | Valid states round-trip; invalid and unknown fields fail with recovery | Schema validity does not prove a useful user model |
| Transitions preserve invariants | Exercise controls, keyboard operations, drag adapters, presets, undo, and reset through the same transition API | Every path reaches equivalent state and invalid combinations remain explicit | Unit transitions do not prove browser wiring |
| Projections agree | For representative states, compare preview, explanation, output, saved state, and visible controls | All projections represent the same canonical meaning and source revision | Agreement can still encode a wrong domain model |
| Imported content is inert | Inject markup, scripts, event attributes, URLs, escaped forms, and malformed domain text | Content displays as data or is rejected; no executable structure appears | Sanitizer coverage depends on target context and policy |
| Domain output is valid | Send query, config, diff, review, graph, or prompt to its target parser or accountable reviewer | Exact exported artifact is accepted or returns a useful bounded error | Target acceptance does not prove usability of authoring flow |
| Keyboard path is complete | Finish representative create, edit, compare, comment, export, undo, and recovery tasks without pointer | Focus is visible and ordered; names, states, errors, and results are available | Automated checks do not establish comprehension for every assistive technology |
| Direct manipulation has equivalence | Compare drag, click, hover, and spatial operations with structured and keyboard alternatives | Both paths produce the same semantic state without relying on color or position alone | Pixel layout can still need visual review |
| Responsive layout remains usable | Render long, empty, loading, invalid, error, and populated states across target viewports and zoom | No incoherent overlap, clipped controls, unreachable output, or content occlusion | Screenshots cannot prove interaction and focus behavior alone |
| Canvas or SVG is nonblank and framed | Inspect browser pixels and structured graph state after load, resize, pan, zoom, filter, and animation | Meaningful pixels render in expected bounds and equivalent data remains navigable | Pixel checks do not prove semantic graph accuracy |
| Clipboard and fallback are honest | Exercise success, denial, unavailable API, insecure context, and manual selection | Feedback matches actual result and exact output remains recoverable | Clipboard success does not validate output semantics |
| Persistence is compatible | Save, reload, export, import, migrate, corrupt, oversize, and delete states | Identity and meaning survive valid round-trip; incompatible state fails safely | Local browser storage is not automatically collaborative durability |
| Source anchors survive or stale | Edit document, diff, graph, or schema source around anchored feedback | Unchanged targets remain bound and changed targets become stale or require explicit reattachment | Heuristic reattachment still needs human review |
| Async validation cannot race | Delay, reorder, fail, cancel, and supersede remote operations | Obsolete results never replace current state; pending and error remain visible | Real service behavior may add failures absent from fixtures |
| Production build matches development | Run optimized target build at its actual served URL | Same state, interactions, output, assets, and error handling work without console failures | One browser and environment do not establish full support |

**Gate profiles**

- **Disposable trusted prototype:** schema defaults, representative transitions, projection equality, safe synthetic text, keyboard core task, reset, target viewports, console, output review, and explicit non-authoritative boundary.
- **Shared artifact:** disposable gates plus imported hostile input, stable source anchors, saved-state version and migration, clipboard failure, broad keyboard tasks, browser support, source freshness, and downstream validation.
- **Consequential or embedded tool:** shared gates plus threat review, sensitive-data handling, independent accessibility evidence, production build, permissions, collaboration or conflict semantics, telemetry, rollback, audit, and accountable acceptance.

**Browser evidence protocol**

1. Start the actual development or production-like server and record the bound URL, build identity, browser, viewport, zoom, input mode, and fixture revision.
2. Verify first meaningful render, not only page load. For canvas or 3D, inspect pixels as well as DOM presence.
3. Run one representative user journey from default through changes, comparison, export, reload, and recovery.
4. Exercise empty, loading, partial, stale, invalid, error, oversized, and imported states activated by the mode.
5. Capture desktop and mobile screenshots after fonts and asynchronous data settle; inspect long labels, focus, overlays, menus, modals, and dynamic output.
6. Complete the same core journey with keyboard and inspect names, roles, states, errors, announcements, and focus return.
7. Review console, failed requests, unhandled promises, asset errors, layout shifts, and stale async completions.
8. Compare output bytes or structured meaning with canonical state and send the exact artifact to its consumer.
9. Preserve screenshots, traces, state fixtures, console summary, command, and known limitation by candidate identity.

**State fixtures**

Keep fixtures for default, each coherent preset, minimum and maximum bounded values, long text, empty collections, invalid combination, imported old version, corrupt state, stale source, hostile markup, keyboard-only operation, reduced motion, high zoom, clipboard denial, remote timeout, and consumer rejection where those paths apply. Retain expected results so regression is observable rather than visually guessed.

Good evidence binds one canonical state to controls, preview, output, saved data, browser screenshots, keyboard completion, and consumer acceptance. Bad evidence reports that an HTML file opened. Borderline evidence includes attractive screenshots and no console failures but no state round-trip or output validator; it supports appearance for those frames only.

Stop downstream polish when the domain model is ambiguous, unsafe text executes, keyboard users cannot complete the decision, preview and output diverge, source identity is stale, or the target consumer rejects the export. Repair the earliest contract and rerun only affected evidence plus invariant state and safety gates.

## Agent Usage Decision Guide

Route by the user's unresolved decision and authoritative next step, not by the words playground, explorer, interactive, or visual.

| Usage profile | Choose when | Minimum action | Boundary and handoff |
|---|---|---|---|
| Design explorer | Users need to compare perceptual component, layout, responsive, or interaction choices | Load target content and tokens; model design decisions; render complete states; export implementation direction | Design owner accepts taste; implementation owner validates target component |
| Data or configuration explorer | Users compose structured queries, APIs, pipelines, schedules, regex, or config | Load authoritative schema; use typed AST; validate combinations; render escaped preview; export exact candidate plus explanation | Domain parser or service owns executable validity |
| Concept or learning map | Users mark knowledge, scope, or dependencies and need relationship-focused output | Separate sourced concepts from user hypotheses; provide list and spatial views; preserve typed edges and knowledge states | Domain expert owns factual relationship claims |
| Document critique | Users decide which proposed improvements to accept, reject, revise, or discuss | Freeze document revision; create stable suggestion anchors; model dispositions; export exact accepted feedback | Document owner applies and reconciles edits |
| Diff review | Users attach findings to changed code or compare implementations | Parse exact diff; preserve file, side, line, hunk, and context identity; model comments and severity; export structured review | Repository review system owns current diff and final resolution |
| Code map | Users inspect real components, layers, calls, dependencies, or data flow | Build provenance-bound graph; distinguish observed and inferred edges; filter without erasing state; provide accessible structured view | Code graph or repository evidence owns architecture truth |
| Existing-playground repair | State, interaction, layout, safety, accessibility, or output is broken | Preserve failing state and browser boundary; repair earliest contract; rerun affected plus invariant gates | Do not broaden features while decision integrity is red |
| Shared template promotion | One mode or state protocol will be copied across projects or agents | Define semantic core, adapters, versioning, threat and accessibility gates, migration, ownership, and retirement | Target repositories retain domain and design authority |
| Production embedding | Playground becomes part of a product workflow or handles privileged data | Add product requirements, framework integration, authentication, privacy, collaboration, operations, telemetry, and rollback | Route platform and governance decisions to accountable owners |
| Orientation only | User compares interaction models or reads historical templates | Produce bounded options, source facts, and unknowns without runtime claims | Browser, output, user-task, and production evidence remain unrun |
| Avoid as primary | Task is a static explanation, ordinary data form, free-form editor, authoritative compiler, privileged console, irreversible operation, or full collaborative review platform | Use the specialist surface and attach only relevant decision-state contracts | Do not stretch a prototype into production semantics |

**Preflight before controls or markup**

Record:

- audience, task, current uncertainty, alternatives, consequence, and decision owner;
- what a successful user can explain, compare, configure, review, or export;
- selected mode and why static content, form, editor, notebook, or production tool is less suitable;
- source data, revision, trust, refresh, privacy, and authority;
- canonical decision fields, defaults, presets, derived values, transient UI, and remote evidence;
- invalid combinations, dependency rules, destructive transitions, undo, reset, and cancellation;
- preview authority, approximation, loading, stale, partial, unavailable, and error states;
- primary and equivalent input paths, keyboard tasks, focus behavior, labels, color independence, zoom, and reduced motion;
- target content, design system, viewport classes, long values, and responsive composition;
- output consumer, exact format, required context, parser or reviewer, and rejection behavior;
- persistence, sharing, schema version, migration, access, deletion, and retention if activated;
- browser, build, test, screenshot, canvas, console, network, and downstream validation evidence required.

A reduced preflight fits a trusted one-session design sketch: confirm the design question, real target content, state fields, coherent defaults, keyboard controls, reset, representative viewports, safe text, and implementation handoff. Do not omit preview limits or output owner because the file is small.

**Start blockers**

Keep work exploratory or route elsewhere when:

- no user decision or output consumer can be named;
- source data is private, stale, or unauthoritative and no bounded synthetic fixture is acceptable;
- the mode cannot represent domain identity without flattening essential semantics;
- a preview would simulate production behavior that users may mistake for authority;
- irreversible or privileged actions would be wired directly into exploration;
- the only proposed graph or canvas interaction is pointer and color;
- imported text would enter markup without a safe rendering plan;
- persisted or shared state has no schema, privacy boundary, or invalidation rule;
- the target parser, reviewer, repository, or implementation workflow cannot accept the export; or
- the requested artifact is actually a production editor, console, workflow, or collaboration platform.

A discovery prototype may proceed with synthetic data and explicit non-authoritative status. Define what must converge before it can be shared or drive implementation.

**Route transitions**

Re-run routing when illustrative data becomes real; one-session state becomes saved or shared; prompt output becomes executable config; a graph gains source-derived claims; document or diff revisions change; collaboration appears; external validation becomes remote; a production component embeds the interface; or sensitive content enters the browser.

Good routing uses the data profile for a schema-aware query builder and brings back target-parser evidence. Bad routing uses a playground to execute privileged database mutations. A code map built from a frozen scan is borderline: it is in scope as dated orientation, but source changes reopen graph extraction before it can support architecture decisions.

**Routing evidence record**

```text
User decision, audience, consequence, and state
Source data, identity, trust, and freshness
Selected mode and rejected surfaces
Canonical state, invalid combinations, and recovery
Preview authority and approximation
Primary and equivalent interaction paths
Output form, consumer, and rejection behavior
Persistence, privacy, collaboration, and promotion status
First negative probe and observed evidence gap
Owners, companion workflows, return artifact, and reversal condition
```

Correct routing minimizes duplicated state. Domain owners return authoritative data and validators; design owners return accepted visual constraints; accessibility and security owners return requirements and evidence; browser and platform owners return operational behavior. This reference keeps those inputs connected without pretending the playground owns them all.

## User Journey Scenario

Use this hypothetical journey to hold one outcome constant: an analyst needs a read-only report showing active customers and their recent paid-order totals. The playground helps compose a query from a versioned schema, compare named alternatives, and export a candidate for an authoritative SQL parser and reviewer. It never connects to production or executes mutation.

**Starting state**

- A schema snapshot identifies `customers`, `orders`, field types, key relationships, and fields permitted for this report.
- The selected SQL dialect and parser exist outside the playground; actual command and service details must be discovered in the target.
- Synthetic rows can demonstrate output shape without private customer data.
- The analyst understands the report question but not every join, aggregate, null, or ordering rule.
- Product or data ownership must accept the business definition of active, recent, paid, and total.

| Phase | Action | Evidence to retain | Stop, repair, or route condition |
|---|---|---|---|
| Discover | Inspect report decision, schema identity, allowed operations, privacy policy, parser, browser support, saved-state policy, and output workflow | Direct target artifacts, owners, source revision, and unsupported operations | Keep conceptual when schema or business terms lack authority |
| Bound scope | Declare read-only generation, supported tables, joins, filters, aggregates, ordering, and limits | Mode contract, non-goals, and decision owner | Route execution, permissions, query planning, and arbitrary SQL editing elsewhere |
| Define state | Model source, selected fields, typed joins, filter expression tree, grouping, aggregates, ordering, limit, and schema revision | State schema, defaults, invalid combinations, and version | Stop when state cannot represent accepted precedence or null semantics |
| Design controls | Use searchable field choices, structured condition rows, relation-aware joins, typed values, ordering controls, exact numeric input, and keyboard reorder | Control-to-transition map and equivalent keyboard path | Replace slider-only or free-string controls that lose exact semantics |
| Render preview | Serialize from AST and display escaped tokens plus a plain-language explanation | State identity, serialized query, explanation, validation state, and limitations | Reject raw markup, DOM-derived output, or coloring that implies parser success |
| Handle invalidity | Explain incompatible fields, missing grouping, unsupported operations, stale schema, and incomplete rows | Error identity, affected control, recovery suggestion, and preserved input | Never drop or rewrite an invalid decision silently |
| Compare | Save named `Customer detail` and `Regional summary` candidates and show semantic differences | Candidate IDs, full states, source revision, baseline, and differences | Block comparison when candidates use incompatible schema revisions |
| Validate | Send exact serialized candidate to target parser or validation service without execution | Parser identity, artifact, response, time, cancellation, and current-state match | Mark pending, unavailable, stale, or rejected explicitly; obsolete responses cannot win |
| Export | Produce exact SQL, schema context, business assumptions, named unresolved questions, and optional natural-language request from canonical state | Output bytes, state digest, consumer, clipboard result, and manual fallback | Copy success cannot substitute for parse or review acceptance |
| Persist | Save a versioned state without private rows and reload it in a clean browser context | State version, source identity, storage boundary, round-trip result, and deletion behavior | Reject corrupt, oversized, unknown-version, stale-schema, or sensitive state safely |
| Review | Data owner confirms business semantics and implementation owner confirms target query boundary | Accepted, revised, rejected, or conditional disposition with rationale | Passing syntax never creates product meaning or production permission |
| Invalidate | Change a field type or remove a relationship in a new schema snapshot | Impact set, stale candidates, migration result, and restored decision | Existing filters and joins return to invalid or unknown until reconciled |

**Canonical state example**

The values below are illustrative rather than target schema or policy:

```json
{
  "schemaRevision": "reporting-schema-20260711-a",
  "source": "customers",
  "select": [
    {"field": "customers.id"},
    {"field": "customers.region"},
    {"aggregate": "sum", "field": "orders.total", "alias": "paid_total"}
  ],
  "joins": [
    {"type": "inner", "from": "customers.id", "to": "orders.customer_id"}
  ],
  "where": {
    "operator": "and",
    "conditions": [
      {"field": "customers.status", "operator": "equals", "value": "active"},
      {"field": "orders.status", "operator": "equals", "value": "paid"},
      {"field": "orders.created_at", "operator": "on_or_after", "value": "2026-01-01"}
    ]
  },
  "groupBy": ["customers.id", "customers.region"],
  "orderBy": [{"field": "paid_total", "direction": "descending"}],
  "limit": 100
}
```

The UI does not store rendered SQL as authority. A serializer and plain-language explainer both read this state. The target parser result is separate remote evidence bound to the state digest and schema revision.

**Mode-specific interaction**

- Selecting `orders.total` with `sum` proposes required grouping and explains why.
- Choosing a relationship creates a typed join from known schema keys; arbitrary cross-table strings are unsupported in the structured mode.
- Exact date and limit inputs remain editable by keyboard; sliders are inappropriate for identifiers, dates, and report limits that users must reproduce.
- Filter groups expose precedence explicitly. Indentation and labels accompany any visual nesting.
- Reordering selected columns is possible by buttons and keyboard in addition to drag.
- Each invalid row retains the entered value, identifies the failed type or operator, and offers a repair without changing it silently.

**Projection agreement**

For a valid candidate, verify:

| Projection | Must preserve |
|---|---|
| Controls | Every selected field, relation, operator, value, grouping, order, and limit |
| SQL preview | Exact dialect serialization with literals escaped by the serializer |
| Plain-language explanation | Source, joins, filters, grouping, aggregate, ordering, limit, and business assumptions |
| Saved state | Complete canonical decisions, schema identity, version, and candidate name |
| Clipboard output | Exact SQL plus enough schema and assumption context for the consumer |
| Parser evidence | Result for the same state digest, schema revision, dialect, and candidate |

If one projection omits the `orders.status = paid` filter, the candidate is inconsistent even if the SQL happens to parse.

**Negative and recovery cases**

- Import a filter value containing markup and verify both preview and explanation show literal text.
- Select a text field for numeric aggregation and verify state remains invalid with a specific repair route.
- Remove a grouping field and verify the parser or local invariant rejects the candidate.
- Delay parser response, edit the query, and verify the old response becomes stale and cannot mark current state valid.
- Deny clipboard permission and verify failure feedback plus manual selection contains exact current output.
- Apply a preset after editing and verify undo restores the complete prior AST and candidate name.
- Load an old state after a field type changes and verify affected filters become stale or invalid instead of converting.
- Complete create, compare, validate, copy, reload, and repair tasks using keyboard only at high zoom.
- Render narrow mobile, tablet, and wide desktop states with long table and field names and no occluded controls.

**Good outcome:** the analyst's state is valid for a named schema, every projection agrees, unsafe literals remain text, keyboard tasks complete, the target parser accepts the exact export, and the data owner accepts business meaning. A schema change invalidates only affected candidates.

**Bad outcome:** dropdown and filter values are concatenated into a colorful `innerHTML` preview, a prompt is copied from visible DOM, and no target parser sees it. The playground looks complete while hidden filters, injection, and invalid joins remain possible.

**Borderline outcome:** a remote query-plan preview arrives for a frozen candidate. Preserve it as scoped evidence only when service, permissions, dataset class, time, state digest, and staleness are visible. It does not authorize production execution.

The durable handoff contains accepted report terms, schema revision, named candidate state, rejected unsupported expression, exact output, parser evidence, user and owner review, persistence boundary, and schema invalidation rules. Its product is a replayable report decision, not a copied string alone.

## Decision Tradeoff Guide

Hold one accepted user decision and source boundary constant while comparing options. Add structure only when it protects a state, interaction, handoff, or lifecycle obligation that a simpler candidate cannot preserve.

| Decision boundary | Lightweight default | Choose the stronger alternative when | Cost if misapplied | Verification and reversal signal |
|---|---|---|---|---|
| Playground or static explainer | Use static content when choices are fixed and interaction adds no information | Build a playground when reversible variables interact and visible consequence changes judgment | Static content hides combinations; interactivity adds complexity without insight | Give representative users both and observe decision accuracy, explanation, and effort |
| Playground or conventional form | Use a form when users know exact values and submit once | Add live comparison when users need to discover values or understand interactions | Form lacks feedback; playground can obscure final commit semantics | Compare task completion and ensure authoritative submit remains explicit where needed |
| One file or application structure | Use one self-contained file for trusted portable prototypes | Use modules, dependencies, build, and server when reuse, CSP, tests, data, routing, or operations require them | One file becomes unmaintainable; app stack burdens a disposable artifact | Test offline handoff, size, policy, ownership, deployment, and change cost |
| Plain state object or reducer/store | Use a validated object and transition functions for small synchronous state | Add reducer, state machine, or store for complex transitions, history, async, collaboration, or modular adapters | Simple object drifts; store adds indirection and boilerplate | Inject invalid transitions, undo, async race, and cross-view updates |
| Immediate projection or explicit apply | Update cheap reversible local projections on every semantic change | Use apply for expensive, irreversible, privileged, or transaction-like operations | Apply interrupts exploration; immediacy causes races or side effects | Measure task flow and prove no operation exceeds its authority or stale-result boundary |
| Immediate remote call or scheduled validation | Keep local state and cheap preview immediate | Debounce, queue, cache, or explicitly validate expensive remote work | Scheduling makes status stale; eager calls overload and reorder | Delay and supersede requests; current state alone may receive result authority |
| Form controls or direct manipulation | Use familiar controls for exact and accessible state entry | Add drag, canvas, graph, or spatial editing when position or target selection is meaningful | Form is indirect; direct manipulation becomes pointer-only and imprecise | Complete identical state changes by pointer, keyboard, and structured list |
| Slider or exact input | Use typed numeric or domain input for reproducible values | Add slider for bounded perceptual comparison and pair exact entry | Slider hides precision and units; input makes exploration tedious | Check keyboard, min, max, step, clamping, unit, and export equality |
| Canvas, SVG, or DOM | Prefer semantic DOM for ordinary controls and textual structures | Use SVG for scalable graph objects; canvas for dense custom rendering after accessibility plan | DOM can be heavy; visual surfaces can be opaque to assistive technology | Inspect pixel bounds and complete tasks through synchronized structured representation |
| Manual layout or layout engine | Use deliberate positions for small stable diagrams | Add tested engine for changing or dense graphs | Manual layout drifts; engine moves unpredictably, overlaps, or burns CPU | Use deterministic fixtures, bounds, overlap, cancellation, and reduced-motion checks |
| Application-owned text rendering or sanitizer/parser | Build text nodes and structured tokens by default | Use reviewed sanitizer or parser when controlled rich content is required | Plain text loses formatting; sanitizer policy gaps enable injection | Run context-specific payload corpus and compare expected structured output |
| Prompt or structured export | Use natural language when a conversational actor is the consumer | Use JSON, query, config, patch, review, or state when exact structure matters | Prompt loses precision; structure loses rationale and readability | Round-trip state and have the exact consumer accept the export |
| One export or dual export | Emit the authoritative format only | Add explanation or prompt beside structure when humans need intent and constraints | Duplicated outputs drift | Generate both from state and compare semantic coverage automatically and by review |
| Synthetic or real source data | Use representative synthetic data for safe interaction design | Use real metadata when accuracy and immediate relevance require it | Synthetic model misleads; real data adds privacy, staleness, and access | Bind revision, redact content, refresh, and test a known source change |
| Hard-coded graph or generated graph | Use a clearly illustrative graph for bounded teaching | Generate when architecture claims, scale, and refresh matter | Hard-coded map goes stale; generator automates wrong edges | Inject missing, wrong, duplicate, and changed relationships and inspect provenance |
| Line number or stable source anchor | Use line number only for frozen disposable content | Add revision, side, range, context digest, and stale behavior for changing review | Strong anchor costs migration; line number misattaches comments | Edit around target, rename file, change side, and verify stale or exact reattachment |
| No persistence or browser persistence | Keep one-session state when loss is acceptable | Add session or local storage when resume value exceeds privacy and migration cost | No save frustrates users; storage leaks or corrupts state | Reload, delete, quota, shared-device, old-version, and corrupt-state tests |
| URL state or opaque share ID | Encode small public state when transparency and portability are desirable | Use authorized opaque ID for sensitive, large, collaborative, or mutable state | URL leaks or exceeds limits; server ID adds availability and access dependency | Inspect history, logs, referrers, size, permissions, expiry, and deletion |
| Local validation or authoritative remote validation | Use local schema and pure rules for immediate guidance | Add remote parser or service when truth depends on current external state | Local result overclaims; remote path adds latency, outage, and races | Compare known fixtures, service identity, pending, failure, cancellation, and stale response |
| One responsive composition or mode-specific layouts | Start with one content order and adapt tracks around it | Use distinct layouts when interaction priority genuinely changes by viewport or input | One layout crowds small screens; multiple layouts duplicate state and focus bugs | Run same task across viewports and confirm state, order, focus, and output continuity |
| Custom implementation or proven library | Use platform primitives for small bounded interactions | Adopt a library for established graph, editor, parser, state-machine, or accessibility complexity | Custom logic misses edge cases; library adds bundle, API, license, and migration | Compare fixtures, support boundary, keyboard behavior, bundle, and upgrade path |
| Manual screenshot review or automated visual baseline | Use focused human inspection for early changing visuals | Add stable screenshot or pixel regression when repeated states and viewports must remain consistent | Manual misses regressions; baselines become noisy or approve wrong pixels | Seed deterministic fixtures and require semantic review of changed images |

**Adopt, adapt, avoid, or escalate**

- **Adopt** a mechanism when a current target obligation needs it and a focused gate demonstrates value.
- **Adapt** historical state, control, preview, comment, or output patterns when responsibility fits but trust, accessibility, framework, or consumer differs.
- **Avoid** controls, projections, persistence, or infrastructure with no decision, owner, recovery, or downstream effect.
- **Escalate** product policy, visual acceptance, domain truth, threat model, regulated accessibility, privileged data, production operations, and authoritative execution to their owners.

**Worked choices**

Good lightweight choice: a trusted one-session button-style explorer uses target content and tokens, validated local state, semantic controls, keyboard tasks, deterministic reset, responsive screenshots, and an implementation-ready design summary. Server persistence adds no useful edge.

Bad heavyweight choice: the same explorer gains accounts, database storage, collaboration, graph library, analytics, and generated links before any user needs sharing. Operational burden grows without improving the style decision.

Borderline canvas choice: a dense concept map benefits from canvas performance. It becomes acceptable after a synchronized searchable list supports selection, edge editing, knowledge state, focus, and export; layout coordinates remain derived unless users deliberately save spatial grouping.

**Decision ledger**

```text
Accepted user decision and source boundary held constant
Target policy or mandatory platform constraint
Selected option and contract protected
Simpler candidate rejected because
State, browser, safety, accessibility, output, and consumer evidence
Privacy, persistence, migration, deployment, and ownership impact
Known untested state or environment
Owner and reopen condition
```

This guide does not establish current framework APIs, browser support, target parsers, design tokens, storage, hosting, or approval roles. Uncertainty should keep choices reversible and output narrow. A heavier mechanism earns its place only when it preserves a decision or lifecycle edge the lighter option demonstrably cannot.

## Local Corpus Hierarchy

The March archive is frozen historical provenance. Each `claude-skills/plugins/playground` file is a byte-identical duplicate locator at the observed hash, not independent supporting evidence. The skill is the strongest local source for integrated historical intent; that does not make its every mechanism current target policy. The six mode templates are focused illustrations rather than inferior merely because they are narrower.

| Hierarchy role | Assignment test | Permitted use | Promotion, demotion, or retirement trigger |
|---|---|---|---|
| Historical observation | Exact content is located in a frozen archive artifact | Describe the source's decision, state, interaction, and output ideas at capture time | Never promote from archive presence alone |
| Duplicate locator | Another path contains identical bytes | Find current consumers, copying lineage, and migration exposure | Reclassify after material divergence, ownership, and independent evidence |
| Shared-contract candidate | Responsibility appears across modes and fits a target need | Seed canonical state, projection, recovery, safety, or output design | Promote after cross-mode target fixtures; demote after counterexample |
| Mode-specific candidate | Responsibility fits one domain state and output | Seed design, data, concept, document, diff, or code-map interaction | Promote after domain and browser evidence |
| Illustrative mechanism | Concrete HTML, JavaScript, CSS, value, count, color, or layout teaches shape | Inspire a sanitized target implementation | Never use as policy or target without independent acceptance |
| Negative evidence | Shortcut or omission demonstrates a plausible failure | Populate threat, accessibility, stale-data, anchor, and migration tests | Retain while causal inference remains plausible; revise after target evidence |
| Target project policy | Current owned schema, design system, security, accessibility, browser, or workflow rule controls the target | Treat as local default inside its version and scope | Reopen after owner, framework, support, tool, or policy change |
| Target observation | A fixture, browser run, parser result, user task, or consumer review records bounded behavior | Support only the state, artifact, environment, and scenario observed | Invalidate on relevant source, state, build, browser, or consumer change |
| Legacy mechanism | A supported old state, renderer, browser API, or template remains in use | Explain existing artifacts and migration constraints | Retire for new work after consumers and saved states migrate |
| Conflict | Historical guidance disagrees with target policy, behavior, or another authority | Preserve disagreement and drive a focused decision | Resolve only with accountable ownership and reproducible evidence |
| Promoted shared rule | Repeated current use and evidence justify generation or distribution | Scaffold the bounded semantic contract with adapters | Demote after unsafe copy, incompatibility, user failure, or owner loss |

**Role assignment by source**

| Source | Strong candidate responsibilities | Conditional or illustrative mechanisms | Negative evidence and required promotion gate |
|---|---|---|---|
| Playground skill | User fit, mode routing, canonical state, live projections, coherent defaults, presets, contextual output | One HTML file, no dependencies, dark theme, two-column shell, prompt footer, immediate update | Missing safety, accessibility, persistence, and target validation; test shared contracts across representative modes |
| Design template | Control selection by decision, contextual visual preview, responsive exploration, qualitative implementation output | Pixel ranges, inline styles, palette rules, Tailwind or CSS suggestion | Missing complete component states and target tokens; test real content, all interaction states, viewports, zoom, and handoff |
| Data template | Structured repeated controls, schema context, syntax or pipeline projection, exact output intent | Slider ranges, regex coloring, example schemas, raw markup construction | Unsafe or invalid domain rendering; use typed model, escaped renderer, target parser, and hostile input |
| Concept template | Knowledge states, user-created typed edges, direct manipulation, node inclusion, learning-focused output | Canvas-only hit testing, fixed node counts, simulation iterations, all-fuzzy default | Pointer-only access and layout-as-truth; add synchronized structured editing, provenance, deterministic layout, and round-trip |
| Code-map template | Layer and relation filters, graph comments, source labels, architecture-focused prompt | Hard-coded nodes, SVG coordinates, palette, timestamp IDs, fixed connection types | Stale or inaccessible architecture; bind repository revision, edge evidence, keyboard access, safe labels, and comment identity |
| Diff-review template | File, hunk, line-side model, line comments, commit context, structured review output | Ad hoc parser, current DOM lookup, raw data attributes, theme colors, emoji badges | Misanchored or unsafe code content; use frozen parser fixtures, stable anchors, escaped text, state-derived export, and keyboard navigation |
| Document-critique template | Full-source review, suggestion statuses, filters, comments, accepted-output synthesis | Nearby-line matching, ad hoc Markdown replacement, raw markup, fixed categories | Feedback drift and injection; bind revision and context digest, sanitize rendering, and test every disposition plus stale source |

**Claim promotion tests**

- Does the source directly support the paraphrased responsibility?
- Is the detail semantic or merely a sample value, API, color, count, coordinate, and layout?
- Which target user or owner needs the responsibility?
- What state, transition, unsafe-input, keyboard, responsive, persistence, or consumer gate can disprove it?
- Which generated templates, saved states, links, and users will depend on promotion?
- What compatibility, privacy, migration, and retirement obligations appear?
- What event demotes, supersedes, or invalidates it?

**Examples of role decisions**

Good promotion: the one-state projection rule is adopted after design, data, and document fixtures prove controls, previews, outputs, undo, and imports remain synchronized. The target project owns the schema and transition API.

Bad promotion: the data template's regex-to-markup snippet is copied into a shared builder and called canonical because both archive and live paths contain it. Duplicate bytes do not establish safety.

Conditional promotion: one-file delivery is adopted for a trusted offline training artifact after size, CSP, browser, font, clipboard, import, and manual-open behavior pass. It remains a delivery profile, not a universal architecture rule.

Negative evidence: the document template's nearby-line match demonstrates why changing documents need stronger anchors. It supports a stale-anchor test, not one specific anchoring algorithm.

**Extraction record**

```text
Archive artifact, source region, locator pair, and content hash
Exact historical observation and candidate responsibility
Role: shared candidate, mode candidate, illustration, negative, duplicate, legacy, or conflict
Target user decision, source data, state, and output consumer
Current target policy and browser evidence inspected
Unsafe-input, keyboard, projection, round-trip, and consumer gates
Rejected mechanism or sample value
Disposition, residual risk, owner, migration, and refresh trigger
```

Promotion is reversible. Target evidence can demote a historical mechanism without altering archive provenance. Legacy state can remain readable after new imports stop accepting it. Rules affecting shared schemas, imported data, source anchors, safe rendering, accessibility, persistence, output, or production embedding need an owner and invalidation trigger; disposable orientation notes can use a lighter record.

**Hierarchy failures**

- Counting archive/live pairs as corroboration inflates confidence.
- Calling the skill canonical imports all historical defaults as one indivisible policy.
- Calling templates legacy dismisses mode-specific semantics still needed by target users.
- Calling a raw snippet sourced fact confuses existence with safety or applicability.
- Calling an omission proof overstates negative evidence; it identifies a test need, not the only solution.
- Promoting an attractive mode without state-schema compatibility fragments shared saved data.
- Rewriting historical provenance after a target decision destroys why and when the mechanism changed role.

The hierarchy is complete only when it can answer both why a mechanism was considered and what consumers must reopen if its evidence changes. Byte identity, historical integration, current target authority, and observed target outcome remain separate dimensions throughout.

## Theme Specific Artifact

Use a **Playground Decision Packet** when an interactive choice must remain explainable across sessions, users, implementations, source revisions, or downstream consumers. The packet is not a screenshot or second copy of the source data. It identifies the decision, canonical state, projections, evidence, and authority that make one candidate meaningful.

A compact packet is enough for a trusted local sketch: decision, source boundary, state version, output, reset behavior, browser result, and non-authoritative status. Use the full packet for imported real data, named comparisons, saved or shared state, review dispositions, generated templates, production embedding, or implementation-driving output.

**Minimum packet contract**

| Field | Completion rule | Failure prevented |
|---|---|---|
| `packet_id` | Assign immutable identity to one decision packet | Evidence and exports from unrelated sessions merge by filename |
| `decision` | Name audience, uncertainty, alternatives, consequence, owner, and accepted scope | Controls exist without a user outcome |
| `mode` | Identify design, data, concept, document, diff, code map, or bounded custom semantics | A visual template flattens domain identity |
| `source_bindings` | Record each real source revision, trust class, access boundary, and refresh trigger | Stale or illustrative data appears current |
| `state_schema` | Record schema identity, version, defaults, required fields, and invalid combinations | Imported or saved state changes meaning silently |
| `candidate_states` | Store named canonical alternatives and their source version | Comparison relies on memory or screenshots |
| `transition_contract` | Map controls, direct manipulation, presets, import, undo, reset, and async results to validated changes | Input paths bypass invariants or update only one view |
| `projection_contract` | Identify preview, explanation, output, and saved-state derivation plus limitations | Attractive projections disagree |
| `interaction_equivalence` | Record primary and keyboard or structured paths for every semantic operation | Canvas, hover, drag, or color excludes users |
| `safety_boundary` | Record input trust, rendering method, sensitive data, URLs, storage, and negative fixtures | Imported text executes or private state leaks |
| `recovery_contract` | Define undo, reset, cancellation, import rejection, stale handling, and fallback | Exploration becomes destructive or dead-ended |
| `output_contract` | Name exact format, consumer, required context, rejection behavior, and copy fallback | A value dump or stale DOM becomes handoff |
| `persistence_contract` | Record storage, state identity, version, migration, access, expiry, and deletion if used | Old, corrupt, or private states survive incorrectly |
| `evidence` | Bind schema, browser, state, screenshot, accessibility, safety, round-trip, and consumer observations | A complete packet has no observed behavior |
| `disposition` | Record exploratory, reviewable, accepted, conditional, rejected, or superseded state with authority | A prototype is mistaken for approved product behavior |
| `invalidation_triggers` | Name source, schema, renderer, browser, design, consumer, or policy changes that reopen the packet | Once-correct output remains trusted indefinitely |

**Lifecycle validity**

| State | Required observation | Rejected transition |
|---|---|---|
| `exploratory` | Decision question and non-authoritative boundary are explicit | Shipping or executing output as accepted |
| `modeled` | Source, schema, defaults, invalid states, and transitions are reviewable | Calling a default screenshot complete |
| `interactive` | Representative control, preview, output, and recovery paths agree | Reviewable status with pointer-only critical action |
| `reviewable` | Required safety, accessibility, browser, state, and consumer evidence is retrievable | Acceptance with stale source or rejected output |
| `accepted` | Accountable design or domain decision and exact consumer boundary are recorded | One reviewer accepting outside their authority |
| `conditional` | Limitation, enforced scope, owner, compensation, and expiry exist | Open-ended degraded mode |
| `rejected` | Reason, state, and counterevidence remain available | Deleting failure and repeating the same candidate |
| `superseded` | Replacement packet and state or source migration are linked | Reusing old evidence for a changed schema |

**Illustrative packet**

```yaml
packet_id: REPORT-PLAYGROUND-042
decision:
  audience: reporting-analyst
  question: Compose a read-only active-customer paid-order report.
  owner: reporting-data-owner
  consequence: Candidate query enters implementation review, not production execution.
mode: data-explorer
source_bindings:
  - id: reporting-schema-20260711-a
    trust: authoritative-metadata
    refresh_trigger: schema revision changes
state_schema:
  id: report-query-state
  version: 2
candidate_states:
  - id: candidate-customer-detail
    digest: state-report-042-detail
    status: accepted-for-review
  - id: candidate-regional-summary
    digest: state-report-042-summary
    status: exploratory
transition_contract:
  controls: typed-query-ast-actions
  presets: transactional-with-undo
  import: validate-version-and-schema
  async_result: require-current-state-digest
projection_contract:
  preview: escaped-sql-from-ast
  explanation: report-semantics-from-ast
  output: sql-plus-schema-and-assumptions
interaction_equivalence:
  reorder: pointer-buttons-and-keyboard
  filters: labeled-controls-and-keyboard
safety_boundary:
  data: schema-metadata-and-synthetic-rows-only
  rendering: structured-tokens-with-text-content
  hostile_fixture: markup-inside-filter-literal
recovery_contract:
  reset: documented-default-state
  undo: restore-complete-prior-candidate
  stale: preserve-state-and-block-current-claim
output_contract:
  consumer: target-sql-parser-and-data-reviewer
  clipboard_fallback: selectable-read-only-output
persistence_contract:
  storage: local-prototype-state
  sensitive_data: prohibited
  migration: versioned-import-or-explicit-rejection
evidence:
  - state-round-trip-pass
  - hostile-literal-inert-pass
  - keyboard-report-task-pass
  - target-parser-candidate-pass
disposition:
  state: reviewable
  authority: implementation-review-only
invalidation_triggers:
  - source schema revision changes
  - state schema version changes
  - serializer or parser dialect changes
  - output consumer contract changes
```

Every value is illustrative. The packet does not prove that active, recent, paid, or total has the correct business meaning; the named owner must accept those semantics. It proves which bounded state and evidence entered review.

**Representation choices**

| Representation | Best fit | Benefit | Main risk |
|---|---|---|---|
| Embedded JSON | Portable one-file prototype and import/export | Close to implementation and machine-validatable | Manual edits and source data can leak into bundle |
| Separate state file | Reusable fixtures and browser tests | Diffable, schema-checkable, and shareable | File and playground version can diverge |
| Issue or review record | Approval-heavy design or document workflow | Ownership, comments, and disposition history | Interactive state and evidence links can detach |
| Append-only event record | Collaborative or audited state transitions | Preserves rejected and superseded decisions | Projection and migration complexity |
| Server-backed authoritative state | Shared mutable workflows and access control | Concurrency, identity, permissions, and durability | Availability, privacy, conflict, and operational cost |
| Generated reviewer projection | Different audiences need concise views | One write model can serve design, engineering, and audit | Generator correctness becomes a dependency |

Choose one authoritative write model. Derive review summaries, prompts, screenshots, and dashboards. Two manually maintained canonical copies recreate the synchronization problem the packet is meant to prevent.

**Verification ladder**

1. Parse packet and state schemas; reject unknown versions, missing source identity, duplicate candidates, and impossible status.
2. Apply representative transitions through each input adapter and compare canonical state.
3. Compare controls, preview, explanation, output, and saved state for every candidate.
4. Inject hostile and malformed source data; verify inert rendering and bounded errors.
5. Complete core tasks by keyboard and structured alternatives across target viewports and zoom.
6. Apply preset, undo, reset, import, stale-source, cancellation, and clipboard-failure paths.
7. Reload or share state in a clean context and verify identity, privacy, migration, and semantic round-trip.
8. Send exact output to the target parser, implementation workflow, or accountable reviewer.
9. Change a source or state schema and verify only affected candidates reopen.
10. Reconstruct why the accepted candidate was chosen without relying on the author's browser session.

Good: the illustrative packet binds a schema, canonical candidates, safe projections, keyboard flow, parser evidence, and invalidation. Bad: a screenshot and copied prompt are called a saved state with no schema or source. Borderline: a valid packet loads against a newer schema; preserve it as historical, mark affected decisions stale, and migrate or review explicitly.

The packet is small at its authoritative write boundary and rich in reproducible projections. Design comparison, implementation handoff, accessibility review, migration, template generation, and incident reconstruction can consume stable identities without turning the packet into the owner of source data or domain execution.

## Worked Example Set

Use this transformation sequence:

1. State the accepted user decision and authoritative next step.
2. Bind real source data or label illustrative fixtures.
3. Define canonical state, invalid combinations, and recovery.
4. Map controls and direct manipulation to validated transitions.
5. Project preview, explanation, output, and saved state from the same model.
6. Demonstrate a negative case and validate exact output with its consumer.

All identifiers, values, technologies, and visual choices below are illustrative.

**Example A: replace a style-value dump with an implementation decision**

Raw request: "Make a playground for card styles."

A weak version adds radius, shadow, padding, and color sliders, updates inline styles, and copies every number. It never states which component, content, interaction states, design tokens, or viewport the choice must serve.

A stronger state separates exact values from intent and context:

| State group | Decision | Required projection | Consumer check |
|---|---|---|---|
| Target | Product card with title, metadata, action, image, and long-content fixture | Preview uses target-like content, not an empty rectangle | Component owner confirms representative content |
| Shape | Token-backed radius and border | Default, hover, focus, selected, disabled, and error states | Target token or CSS output resolves correctly |
| Elevation | Shadow intent, values, context background, and reduced-motion behavior | Light and dark contexts plus interaction | Visual review checks hierarchy and focus contrast |
| Density | Exact padding, gap, typography, and responsive behavior | Narrow, medium, and wide content compositions | Implementation output preserves content fit |
| Handoff | Chosen token values, qualitative intent, non-goals, and unresolved states | Prompt and structured token proposal from one state | Developer can implement without reopening the playground |

**Negative probe:** switch to the long title, narrow viewport, keyboard focus, and error message. A candidate whose text overlaps or focus disappears is rejected even if the default card looks polished.

**Good:** named `Quiet utility` and `Elevated feature` presets apply complete reviewed states and preserve undo. **Bad:** `Random` is presented as a recommended preset and output says only `radius 12, blur 18`. **Borderline:** the preview looks correct but uses fonts unavailable in the target; retain it as visual direction until the production typography boundary is verified.

**Example B: make a concept-map canvas semantically accessible**

The source suggests dragging nodes, clicking endpoints to create edges, and hovering for tooltips. Preserve the spatial affordance, but make semantic state independent of pixels:

```json
{
  "nodes": [
    {"id":"state-schema","label":"State schema","knowledge":"know","included":true},
    {"id":"output-contract","label":"Output contract","knowledge":"fuzzy","included":true}
  ],
  "edges": [
    {"id":"edge-1","from":"state-schema","to":"output-contract","type":"constrains","source":"user"}
  ],
  "layout": {
    "state-schema":{"x":120,"y":90},
    "output-contract":{"x":380,"y":210}
  }
}
```

Nodes and edges appear in a searchable structured list. Keyboard users can select a node, cycle knowledge state, choose an edge type, connect a target, delete an edge, and move layout in bounded steps. Focus reveals the same description as hover. Edge type uses text plus line style; layout is derived unless the user explicitly includes spatial grouping in output.

**Negative probe:** hide the canvas and complete the learning-state and relationship task from the structured view. Then restore it and confirm identical semantic state. **Borderline:** list users can inspect but not create edges; the artifact is accessible for reading, not equivalent exploration, and must say so.

**Example C: prevent review feedback from drifting to another line**

Line number alone is insufficient for a changing document or diff. A stable review anchor records:

```yaml
comment_id: review-comment-017
source_id: docs/specification.md
source_revision: source-revision-a12
side: current
start_line: 48
end_line: 50
context_digest: context-spec-48-50-a12
target_excerpt: Error states retain the user's entered values.
disposition: pending
comment: Clarify which validation errors permit retry without resetting state.
```

When the source revision changes, exact unchanged context may be reattached under an explicit mapping. Changed or ambiguous context becomes `stale`; the tool shows old and candidate locations for human confirmation. It never searches a nearby line and moves the comment silently.

**Good:** export retains file, side, range, revision, excerpt, disposition, and comment. **Bad:** a nearby-line regular expression attaches feedback to whichever line number is within two rows. **Borderline:** exact text occurs twice; both candidates remain unresolved until the reviewer selects one.

**Example D: render imported data safely and validate exact output**

A data explorer imports a schema containing a field label and filter literal that resemble markup. The state stores them as strings. A serializer emits query syntax with dialect escaping. A token renderer creates DOM text nodes or applies a reviewed safe parser; it does not run regex replacements into raw markup.

| Input | Required behavior | Failure signal |
|---|---|---|
| Field label containing markup delimiters | Literal label remains visible and inert | New element or event appears in DOM |
| Quote and comment syntax in value | Serializer escapes according to dialect | Preview and parser disagree |
| Malformed imported state | Preserve source and report version or schema error | Partial values enter current candidate |
| Hidden filtered control group | Export retains canonical decision | Output changes because panel is collapsed |
| Clipboard denial | Show failure and selectable exact output | Success feedback appears or stale content remains selected |

The exact output is submitted to the target parser. **Good:** state, preview, explanation, and parser input agree. **Bad:** colored markup looks plausible and a prompt says the query is valid without parsing. **Borderline:** local parser accepts syntax but production policy forbids one table; preserve syntax evidence and route authorization separately.

**Reuse questions**

- Which facts come from target data rather than the illustration?
- Which first draft was rejected and what decision did it lose?
- Which state transitions, invalid combinations, and recovery paths matter?
- Which negative input makes the relevant gate fail?
- Which browser, viewport, input mode, source revision, and consumer produced evidence?
- Which values, IDs, APIs, palettes, and support boundaries must change locally?
- What event invalidates or migrates the example state?

Promote stable adaptations into conformance fixtures for schemas, renderers, anchor migration, direct-manipulation equivalence, persistence, and output consumers. Include bad and borderline states. Add novel incident and user-task failures over time so the suite does not recognize only its teaching examples.

## Outcome Metrics and Feedback Loops

Measure whether the playground helps a person make a better bounded decision, not merely whether the person moved controls or produced an attractive screen. Interaction volume is activity. A useful outcome preserves state, survives recovery, satisfies the named criteria, produces a valid handoff, and leaves less consequential uncertainty than the starting point.

The default measurement order is a ladder. A higher-level result is not credible when a lower-level gate fails:

| Level | Decision question | Example evidence | Guardrail |
|---|---|---|---|
| Integrity | Did the tool preserve the user's actual candidate? | Transition tests, undo and redo replay, save and restore round-trip, projection equality | No silent reset, stale export, or hidden-state loss |
| Usability | Could the intended audience complete and recover from the task? | Representative task walkthroughs across pointer, keyboard, narrow viewport, and error paths | Do not improve speed by removing explanation, focus, or reversible exploration |
| Decision quality | Did the interaction improve the artifact against accepted criteria? | Before and after rubric, rejected-candidate reasons, unresolved-risk record, reviewer agreement | Novelty, confidence, and selection count do not substitute for criterion fit |
| Consumer outcome | Did the handoff work where it was intended to be used? | Parser or compiler result, implementation review, accepted change, later defect or rework record | Adoption alone does not prove correctness, authorization, accessibility, or maintainability |

Treat the first two levels as gates for every retained template. Select the decision-quality and consumer measures from the mode, risk, persistence, and target workflow. A disposable personal color exploration does not need production telemetry. A saved query builder that emits executable syntax needs exact serializer, parser, restoration, authorization, and error evidence even if only a few people use it.

**Define each metric before collecting it**

A metric record should identify:

- the accepted user decision and the claim being evaluated;
- the task, fixture, source revision, state schema, and output contract versions;
- the population or named evaluator, including excluded and abandoned attempts;
- the observation window, denominator, segmentation, and comparison baseline;
- the value, guardrail, interpretation, confidence, and known confounders;
- the threshold or qualitative condition that changes the recommendation;
- the owner, review date, expiry trigger, and evidence location.

Without this context, `completion increased` is not actionable. Completion may have risen because a difficult but necessary validation step disappeared, the fixture became easier, failed sessions were excluded, or users learned to click the recommended preset without understanding it. Compare only compatible tasks and preserve the old definition when a metric changes.

**Choose signals by playground mode**

| Mode | Useful leading evidence | Useful later evidence | Misleading shortcut |
|---|---|---|---|
| Design exploration | Criteria coverage, representative-state checks, explained candidate rejection | Implementation preserves intent across target states | Number of slider changes or preference votes alone |
| Concept mapping | Semantic node and edge accuracy, changed uncertainty labels, keyboard-equivalent edits | Learner can explain relationships or use the map in a later task | Canvas density or time spent arranging nodes |
| Data exploration | Valid filters, provenance visibility, query-result agreement, recoverable errors | Saved analysis reproduces against a named dataset revision | Query count, chart count, or copied rows |
| Diff and review | Stable anchors, disposition completeness, stale-comment detection | Accepted feedback maps to the intended revision and reduces rework | Comment count or fast approval |
| Document critique | Claim coverage, evidence links, preserved source boundaries | Revision resolves prioritized issues without introducing contradictions | Word count removed or issue count alone |
| Configuration | Valid combinations, exact output, migration and restore behavior | Consumer accepts configuration and operators can diagnose failures | Preset selection or successful copy feedback |

These are candidate measures, not universal thresholds. Establish a local baseline before declaring improvement. When sessions are sparse, outcomes are delayed, or consent and retention constraints preclude instrumentation, use a structured case record instead of manufacturing statistical certainty.

**Close the loop in four observation moments**

1. Before interaction, capture the initial candidate, accepted criteria, relevant uncertainty, fixture version, and expected consumer.
2. During interaction, record meaningful state transitions, invalid attempts, undo and recovery, rejected candidates, and explanation use. Avoid retaining sensitive raw content unless the accepted workflow requires and governs it.
3. Immediately after, save the chosen state, exact output, criterion assessment, unresolved issues, confidence, and whether the user could explain the choice.
4. After handoff, check the actual consumer result, implementation changes, rework, incidents, and criteria that proved missing or unnecessary.

An observation does not close the loop by itself. A closed feedback record connects evidence to a change in a criterion, fixture, schema, interaction, output contract, default, or recommendation; names any saved-state migration effect; reruns the affected gates; and records whether the expected outcome changed.

For example, suppose a card-design playground shows shorter completion time after making `Elevated feature` the initial preset. The result is not yet an improvement. Recheck long content, narrow width, keyboard focus, error text, dark context, and reduced motion. Compare whether participants can state why the preset fits the accepted hierarchy. Then confirm that the implementation output resolves to available tokens and survives the target component states. If speed improved but focus contrast failed, the integrity guardrail rejects the change.

**Match evidence cost to consequence**

| Evidence method | Strong for | Does not establish by itself |
|---|---|---|
| Automated state and projection tests | Deterministic transitions, invariants, migration, exact output | Human comprehension, taste, or target usefulness |
| Consumer parse, compile, or schema validation | Structural acceptance by a named consumer version | Semantic authorization, visual quality, or operational adoption |
| Moderated representative task | Confusion, mental model, recovery, explanation, accessibility barriers | Population-wide frequency or long-term downstream impact |
| Expert rubric review | Domain quality against explicit criteria | Ease of use for the intended audience or causal effect of one control |
| Local privacy-preserving session trace | Transition paths, abandonment points, repeated recovery | Why a person acted or whether the final artifact is good |
| Post-handoff review and incident analysis | Rework, defects, drift, missing contract boundaries | A clean causal attribution when many workflow factors changed |

Use overlapping methods at consequential boundaries. For example, a query output can be checked by an automated serializer fixture, parsed by the target dialect, exercised in a representative task, and reviewed for authorization separately. The parser proves syntax, not permission. The task proves one observed path, not universal usability.

**Interpret good, bad, and borderline records skeptically**

Good: all state invariants pass; representative users complete the named task with pointer and keyboard paths; rejected candidates name criterion failures; exact output passes the named consumer; and later implementation review confirms the selected intent without reopening basic decisions.

Bad: copied-output events increase, but restored sessions omit hidden filters and the target parser rejects quoted values. The engagement number is a vanity signal because the lower integrity and consumer gates fail.

Borderline: a small expert review rates the revised artifact more highly and all deterministic checks pass, but no downstream implementation has used it. Preserve the positive rubric evidence, label consumer outcome unknown, and request a target implementation check rather than averaging uncertainty into a pass.

Bad: the team compares completion times before and after replacing a complex fixture with a simple one, excludes abandoned sessions, and calls the new interaction faster. The denominator and task changed, so the comparison is invalid.

Borderline: the concept-map canvas is fully readable in a structured list but edge creation remains pointer-only. Reading evidence may pass; equivalent exploration does not. Track these as separate claims and prioritize the missing task path.

**Failure signals and corrective actions**

- High activity with unchanged criteria or unexplained choices: reduce decorative controls, surface the decision rubric, and test whether users can explain a rejected candidate.
- Faster completion with more invalid output or inaccessible paths: restore the guardrail and investigate which validation or affordance was bypassed.
- Strong final states with repeated resets or recovery failures: fix canonical-state and lifecycle behavior before optimizing the artifact.
- High preset convergence without independent comparison: rotate order in evaluation, reveal tradeoffs, and check for default anchoring.
- Positive feedback only from successful sessions: include abandonment, import rejection, clipboard denial, stale anchors, and malformed saved-state paths.
- Improving aggregate with one audience segment regressing: keep segmented evidence and do not let a majority average erase a consequential exclusion.
- Repeated metric optimization without downstream use: revisit whether the playground addresses a real decision or should be retired.

**Verification cadence**

Run structural and focused reference verification after every generated-reference edit. Run state, projection, serializer, migration, accessibility, and consumer checks whenever their contracts change. Recheck representative task paths when controls, defaults, fixtures, labels, support boundaries, or recommendation order changes. Revalidate local source mappings when repository evidence changes; when an external dependency matters and browsing is outside the current work boundary, mark that claim as needing owner verification rather than presenting remembered release behavior as current fact.

Use a review cadence driven by invalidation events, not a calendar alone. Relevant events include a state-schema revision, consumer-version change, target component redesign, accessibility defect, security incident, new audience, persistent artifact migration, source revision, and evidence that a metric is being gamed. Stable low-risk local experiments can use milestone review. Shared or executable outputs need review before release and after consequential incidents.

Stop an iteration when the accepted criteria and guardrails pass, unresolved risks are explicit and owned, the consumer evidence is proportionate to consequence, and further controls or measurements no longer change the decision. Continue when a lower gate fails, a borderline result lacks a named evidence request, or the apparent gain depends on an invalid comparison.

Known with high confidence: defined invariant and consumer checks can detect the failures encoded in them, saved comparison context prevents several common interpretation errors, and final success alone hides abandoned and recovery paths. Contextual judgment remains in the choice of taste criteria, representative users, evidence cost, baseline, and acceptable residual uncertainty. Date those judgments and identify who made them.

The second-order effect of a healthy loop is simplification. Evidence should remove controls that do not affect accepted decisions, retire metrics that invite gaming, split claims that require different proof, and promote recurring failures into fixtures. A playground with fewer well-evidenced decisions is often more useful than a feature-rich surface whose activity cannot be connected to a trustworthy artifact.

## Completeness Checklist

Use this checklist to decide whether playground guidance is ready for its declared lifecycle, not whether the document merely contains expected phrases. A checked row means that inspectable evidence supports the claim for the named task, fixture, audience, state schema, and consumer. Presence is not proof, and completeness is not correctness.

**Select a review profile first**

| Profile | Appropriate boundary | Minimum review |
|---|---|---|
| Disposable exploration | One person, synthetic or non-sensitive data, no saved artifact, no shared output | Decision preflight, canonical state, basic keyboard path, safe rendering, explicit disposal boundary |
| Shared decision aid | Multiple reviewers, link or file sharing, retained candidates, implementation handoff | Full decision, state, accessibility, persistence, provenance, output, and recovery rows |
| Executable or sensitive tool | Queries, configuration, code, uploads, private data, external effects, or broad audience | Full matrix plus target consumer checks, authorization and abuse review, migrations, observability, and release ownership |

Moving from disposable to shared, adding persistence, accepting imported content, emitting executable output, or widening the audience reopens completeness. A prototype does not inherit its earlier reduced review after its lifecycle changes.

**Use explicit statuses**

- `verified`: a reproducible automated check directly supports the row for named versions and fixtures;
- `observed`: a recorded user, browser, accessibility, or operational exercise supports it;
- `judgment`: a named reviewer made a contextual decision and recorded the basis and limitation;
- `not applicable`: a specific boundary makes the row irrelevant, with an invalidation trigger;
- `blocked`: required evidence or an owner is unavailable, so release follows the declared blocking policy;
- `failed`: evidence contradicts the required behavior.

Do not use `done`, `looks good`, or an empty checkbox as a substitute. `Not applicable` requires a reason; `blocked` is not a quiet pass; and contradictory evidence reopens a row even if another artifact passed.

**Decision and routing contract**

| Check | Required evidence | Blocking signal |
|---|---|---|
| Role scenario names the user, starting state, decision, trigger, downstream consumer, and cost of error | Accepted scenario and representative starting fixture | The interface exists before the decision is known |
| Adopt, adapt, avoid, and cost-of-error guidance is mode-specific | Decision record tied to one of the six playground modes | Every interactive idea is routed to a playground |
| Adjacent references receive out-of-scope work | Explicit route for passive explanation, production UI, benchmarking, security review, and non-interactive documentation | The reference claims authority beyond its evidence |
| Scope and non-goals are visible near implementation guidance | Reviewable boundary statement | A reader can interpret an example as a universal framework or policy |
| Recommendation identifies reversibility and escalation | Risk classification and owner | Consequential output uses a low-risk exploration gate |

**Source and claim contract**

| Check | Required evidence | Blocking signal |
|---|---|---|
| Local corpus map distinguishes integrating, mode-specific, duplicate, historical, target-authority, and missing roles | Path inventory, content identity check, and claim-level source role | File count is mistaken for independent corroboration |
| Every consequential claim has a source class or explicit synthesized status | Claim ledger or inline provenance | Remembered external behavior is stated as current fact |
| Source conflicts are preserved and resolved by authority and recency appropriate to the target | Conflict record and owner decision | Incompatible guidance is blended silently |
| Evidence freshness has an invalidation trigger | Revision, version, date, or owner confirmation | A stale screenshot or old consumer result remains a permanent pass |
| No-browse work marks externally changing behavior for later target verification | Confidence note and retrieval request | Unsupported precision fills a source gap |

**Canonical state and transition contract**

| Check | Required evidence | Blocking signal |
|---|---|---|
| One typed or structurally validated state owns all user decisions | State schema and initialization fixture | Preview styles, DOM text, or canvas coordinates become hidden authority |
| Every control and direct manipulation maps to a named validated transition | Transition table and event tests | Pointer gestures mutate one projection without updating output |
| Invalid combinations have prevention, explanation, and recovery | Negative fixtures and expected recovery state | Invalid state is silently coerced or discarded |
| Undo and redo preserve semantic state and bounded history | Replay check across representative edits | Undo restores appearance but not relationships, filters, or provenance |
| Derived layout and display state are separated from semantic decisions | Schema review and round-trip fixture | Window size or generated coordinates leak into implementation output |
| Hidden or collapsed controls retain canonical values | Projection comparison before and after visibility changes | Closing a panel changes the exported artifact |

**Interaction and accessibility contract**

| Check | Required evidence | Blocking signal |
|---|---|---|
| Core tasks work with keyboard and pointer where both are supported | Recorded task matrix with focus order and expected result | Drag, edge creation, reordering, or selection is pointer-only without an equivalent path |
| Hover-only information is available on focus and through persistent structure | Browser observation and accessibility inspection | Essential meaning disappears without a mouse |
| Canvas or SVG semantics have an inspectable structured alternative | Equivalent node, edge, item, or region representation | A visual surface is the only source of state or meaning |
| Color is supplemented by text, shape, pattern, or position and meets target contrast policy | State fixtures and target accessibility check | Knowledge, validity, or selection is encoded by hue alone |
| Narrow viewport, zoom, long content, error text, and focus indicators remain usable | Representative browser matrix | Controls overlap, clip, or move focus unpredictably |
| Motion and direct manipulation respect target support and reduced-motion behavior | Browser setting check and interaction fallback | Animation is required to understand or complete the task |

**Security, privacy, and data contract**

| Check | Required evidence | Blocking signal |
|---|---|---|
| Imported values are parsed as data and rendered inertly | Adversarial fixture with markup delimiters, quotes, comments, and malformed state | Raw imported strings reach `innerHTML` or equivalent unsafe rendering |
| Serialization is separate from syntax highlighting and preview formatting | Exact-output fixture and target parser result | Regex-colored markup is treated as proof of valid syntax |
| Sensitive data, retention, telemetry, export, and deletion boundaries are declared | Data-flow review and storage policy | A playground silently stores source content or session traces |
| Authorization is verified separately from syntactic validity | Target permission test or owner confirmation | A valid query or configuration is assumed to be allowed |
| Clipboard, download, upload, and network failures are recoverable and truthful | Denial and failure-path observations | Success feedback appears before an operation succeeds |
| Expensive or adversarial input has bounded size and computation | Limit fixtures and cancellation behavior | One imported artifact can freeze the interface or exhaust memory |

**Persistence, migration, and collaboration contract**

| Check | Required evidence | Blocking signal |
|---|---|---|
| Saved artifacts carry format, schema, template, and relevant source versions | Export fixture and schema definition | A bare state blob cannot be interpreted after change |
| Save and restore round-trip preserves semantic state exactly | Deep comparison after serialization and parse | Restore silently drops unknown or hidden decisions |
| Older supported versions migrate deterministically or fail with recovery guidance | Migration fixtures and expected diagnostics | Partial migration enters the active candidate |
| Autosave cannot overwrite a known-good artifact with invalid transient state | Lifecycle and interruption tests | A malformed intermediate edit replaces the last recoverable state |
| Concurrent or shared edits expose conflicts rather than last-write-wins surprise | Collaboration scenario or explicit single-writer boundary | One reviewer silently erases another's decision |
| Review anchors include source identity, revision, range, excerpt, and stale state | Changed-source fixtures | Feedback floats to a nearby line without confirmation |

**Projection and output contract**

| Check | Required evidence | Blocking signal |
|---|---|---|
| Preview, explanation, generated prompt, exact output, and saved artifact derive from one canonical state | Cross-projection equality fixture | Different panels describe different candidates |
| Output schema names required fields, ordering, escaping, omission, and unsupported values | Golden fixtures and schema or consumer contract | Human-readable text is the only handoff for structured decisions |
| Exact output is validated by the named consumer where feasible | Parser, compiler, schema, or target application result | A plausible preview substitutes for consumer acceptance |
| Generated prompts distinguish facts, selected decisions, constraints, uncertainty, and evidence requests | Prompt snapshot and reviewer inspection | The prompt turns assumptions into authoritative requirements |
| Copy and download actions use the current canonical state and report actual success | State-change and operation-failure checks | Stale DOM content is copied or failure is announced as success |
| Unsupported output and partial support are explicit | Capability table and negative fixture | The interface offers controls that serialization ignores |

**Examples, metrics, and maintenance contract**

| Check | Required evidence | Blocking signal |
|---|---|---|
| Worked examples include good, bad, borderline, and negative cases | Reproducible fixtures with expected observations | Only polished final screenshots are shown |
| Illustrative names, IDs, values, palettes, and APIs are labeled | Boundary notes near examples | Readers can mistake synthetic detail for repository fact |
| Outcome metrics cover integrity, usability, decision quality, and downstream use as applicable | Metric definitions with guardrails and denominators | Interaction count is presented as artifact quality |
| Failed, abandoned, and recovery paths remain in the evidence set | Session or case record | Only successful final states influence decisions |
| Feedback changes name the affected contract, migration effect, owner, and recheck | Closed-loop change record | Metrics change defaults without compatibility review |
| Template and source changes have review and expiry triggers | Maintenance record | Evidence stays green after its dependency changes |
| Repeated failures become shared fixtures and low-value controls are removed | Revision history and rationale | Complexity grows while decision quality remains unchanged |

**Good, bad, and borderline completion records**

Good state row: `verified`; evidence names a transition fixture that selects an edge with keyboard and pointer paths, proves identical semantic state, then replays undo and redo. The record names the state-schema revision and says a schema or event-model change invalidates it.

Bad accessibility row: `verified`; evidence is a screenshot showing visible focus on one button. It does not exercise graph navigation, edge creation, focus restoration, zoom, or the structured alternative. The status overclaims what the artifact proves and must be reopened.

Borderline consumer row: `judgment`; exact configuration passes the local schema, but the production owner has not confirmed one policy field. The release can remain blocked, or a non-executable preview can ship with that field disabled. It cannot be called fully consumer-validated.

Good exclusion: telemetry is `not applicable` for a disposable local exploration because no events leave memory, no content persists, and the artifact is destroyed after the session. The row reopens if sharing, analytics, persistence, or a network client is added.

Bad exclusion: migration is `not applicable` because the current build has no migration code, even though users can save artifacts. Lack of implementation makes the row failed or blocked; it does not remove the obligation.

**Freeze a release record**

Use repository-native metadata when available. A minimal human-readable record can look like this:

```yaml
artifact: interactive-query-playground
profile: executable-or-sensitive
state_schema: playground-state-v3
template_revision: template-revision-20260711
source_fixture: sales-schema-revision-18
consumer: target-query-parser-v6
decision_owner: data-platform-reviewer
reviewed_at: 2026-07-11
verdict: blocked
blocking_rows:
  - authorization-policy-confirmation
evidence:
  state_round_trip: artifacts/state-v3-round-trip.txt
  keyboard_task: artifacts/query-keyboard-task.txt
  parser_result: artifacts/query-parser-v6-result.txt
residual_risks:
  - Production row-level policy has not been confirmed.
reopen_when:
  - State schema, parser version, source schema, or authorization policy changes.
```

Paths and identifiers above are illustrative. A real record must point to artifacts that exist in the target repository and must not imply that a file name alone proves its claim.

**Final reconciliation procedure**

1. Confirm the exact heading order, packet shape, question text, mandatory-field uniqueness, expansion, ASCII, whitespace, table, fence, and placeholder gates required by this reference corpus.
2. Reconcile every section with its completed question packet; investigate conclusions that disappeared from the reference or claims that appeared without packet support.
3. Recheck the source inventory, duplicate-content findings, source roles, claim confidence, and unresolved conflicts against frozen inputs.
4. Select the lifecycle profile and mark each applicable matrix row with a status, evidence location, owner, limitation, and invalidation event.
5. Execute deterministic state, transition, persistence, serializer, migration, and consumer gates using target-discovered commands.
6. Exercise representative pointer, keyboard, narrow viewport, zoom, focus, invalid input, operation denial, recovery, and stale-source tasks.
7. Compare preview, explanation, prompt, exact output, and restored artifact against the same canonical state.
8. Review security, privacy, authorization, accessibility, and operational claims with the appropriate target owners; document unavailable confirmation as uncertainty or a blocker.
9. Challenge at least one passing row by reading its evidence and attempting the negative case. Reopen contradictions instead of voting them away.
10. Freeze the verdict and evidence hashes or revision identifiers, record residual risks and next steps, and rerun affected gates after any correction.

Release is ready only when required rows are supported at the evidence level appropriate to their claim, failed rows are corrected, blocking policy is satisfied, residual risk is explicit and owned, and the complete reference has received a skeptical reread. A complete matrix may still conclude `avoid`; that is a successful decision, not a failed document.

Over time, use the matrix as a diagnostic map. Repeated manual checks are candidates for shared fixtures or tooling. Rows that never affect a decision should be challenged and possibly retired with rationale. Rows repeatedly reopened by incidents deserve stronger defaults. The checklist remains useful only while it can both block unsafe confidence and remove obsolete ceremony.

## Adjacent Reference Routing

Choose the primary reference from the user's dominant decision and final deliverable, not from an incidental technology word. A canvas can host a concept map, a generative artwork, a spatial data visualization, or a production editor; those artifacts have different state, accessibility, evidence, and lifecycle obligations.

Keep this reference primary when reversible controls and immediate projections help a person explore a bounded decision space before producing a saved candidate, explanation, prompt, query, review record, or implementation handoff. Route elsewhere when interaction is merely navigation, when the output is already settled, or when another artifact class owns the user's real goal.

**Fast route test**

1. What must the user decide, learn, produce, or operate?
2. Do changes to canonical state produce meaningfully different candidates that the user must compare?
3. Must the user preserve, explain, restore, or export those choices?
4. Is the primary deliverable the exploration mechanism, or is it an image, artwork, diagram, explanation, product interface, three-dimensional scene, timeline analysis, or traceability record?
5. Which reference should own acceptance criteria, and which references, if any, own bounded supporting artifacts?

If Questions 2 and 3 are yes and the exploration mechanism is primary, remain here. If controls only paginate, reveal prose, or decorate a fixed answer, prefer the reference for the actual deliverable. If the task has become a stable repeated operation, route application design to the relevant product and domain guidance even if an earlier playground helped discover it.

**Repository-discovered adjacent candidates**

The paths below were discovered in the current reference directory. Their names provide routing candidates, not proof of their detailed contents or current suitability. Read the destination completely and verify its inputs before applying it.

| Dominant task or artifact | Candidate reference | Route away from this reference when | This reference can remain supporting when |
|---|---|---|---|
| Code-driven expressive artwork | `idiomatic-ref-202607/algorithmic_art_generation_patterns-20260710.md` | The goal is an authored generative visual whose behavior and aesthetic system are the product | A small parameter laboratory is used to compare algorithms or palettes before selecting the artwork |
| Generated bitmap or image direction | `idiomatic-ref-202607/image_generation_prompt_patterns-20260710.md` | The requested result is an image or image-edit prompt, not a persistent stateful decision tool | The playground assembles and compares grounded prompt decisions without pretending to generate or validate the media itself |
| Terminal-native static explanation | `idiomatic-ref-202607/ascii_diagram_layout_patterns-20260710.md` | Copyable fixed-width structure is the deliverable and no meaningful state needs manipulation | A playground produces alternative topologies and exports one verified ASCII view |
| Polished operational frontend | `idiomatic-ref-202607/frontend_design_quality_patterns-20260710.md` | Users repeatedly complete a settled product workflow rather than explore alternatives | An internal laboratory is retained separately for tuning defaults, fixtures, or design tokens |
| Interactive three-dimensional visualization | `idiomatic-ref-202607/threejs_react_visualization_patterns-20260710.md` | Scene, camera, rendering, and spatial interaction are central implementation contracts | Canonical decision state and exact handoff still follow the playground model while scene mechanics follow the visualization reference |
| Guided visual explanation | `idiomatic-ref-202607/visual_explainer_skill_patterns-20260710.md` | The objective is staged understanding and progressive disclosure rather than candidate selection | A bounded lab lets learners test one causal relationship inside the larger explanation |
| Causal scenario or future simulation | `idiomatic-ref-202607/timeline_decision_simulation_patterns-20260710.md` | Branching assumptions, temporal consequences, and scenario comparison are the core reasoning model | Controls edit assumptions while the timeline reference owns scenario semantics and comparison |
| Requirement and evidence governance | `idiomatic-ref-202607/executable_traceability_template_patterns-20260710.md` | The main artifact is a requirement, evidence, test, and decision ledger rather than an exploratory interface | The playground emits a candidate record that enters a separately governed traceability system |

Other domain references may be better destinations when the emitted artifact is code, configuration, a query, or a framework-specific application. Discover them from the current repository inventory, read them before use, and avoid treating this table as exhaustive.

**Primary and supporting ownership**

Use one primary reference for the core workflow. Supporting references should own narrow contracts, not duplicate the primary authority:

| Contract | Example owner | Prohibited ambiguity |
|---|---|---|
| User decision, canonical state, reversible exploration, projections | Interactive playground reference when exploration is primary | Two references define incompatible state models |
| Media generation and edit intent | Image or algorithmic-art reference | A playground preview is claimed as generated-media evidence |
| Static terminal layout | ASCII diagram reference | Browser layout assumptions leak into the exported diagram |
| Repeated operational workflow and product UI | Frontend and domain reference | Prototype shortcuts become production defaults without review |
| Scene rendering, camera, spatial performance | Three-dimensional visualization reference | Canonical decisions are stored only in scene objects |
| Pedagogical sequence and explanation | Visual explainer reference | More controls are added when guided disclosure is the accepted goal |
| Temporal assumptions and causal branches | Timeline simulation reference | Timeline semantics are reduced to arbitrary slider values |
| Requirement identity and evidence chain | Executable traceability reference | A generated summary replaces durable requirement-to-test evidence |

At each boundary, record the data passed between owners and the verification each side supplies. For example, a playground may output an explicit palette, seed, density, and motion policy to an algorithmic-art workflow. It should not claim that the final artwork satisfies the selected intent until the artwork is rendered and reviewed. Likewise, a timeline playground may own controls, undo, and save behavior while the timeline model owns causal assumptions and scenario validity.

**Pivot signals**

Route from playground to product interface when:

- the user population and repeated workflow are stable;
- candidate comparison has collapsed into one accepted operation;
- permissions, collaboration, service reliability, audit, and long-term support dominate exploratory value;
- the artifact now changes real systems rather than producing a reviewable handoff; or
- teams are maintaining prototype controls that no longer affect a decision.

Route from playground to passive or guided explanation when:

- the correct conceptual sequence is known and controls add no useful counterfactual;
- the user needs orientation rather than a saved candidate;
- interaction distracts from evidence or implies false precision; or
- the same understanding can be achieved through a clearer diagram, narrative, or staged explainer.

Route from playground to image or art generation when:

- visual authorship, composition, texture, motion, or rendering is the primary outcome;
- the user asked for a finished visual rather than a tool for selecting parameters;
- preview fidelity cannot represent the final medium; or
- state and output exist only to direct the generation workflow.

Route to timeline simulation when time, uncertainty, branching assumptions, regret, or downstream consequences are the actual model. Route to executable traceability when the enduring need is to connect requirements, implementation, tests, evidence, and decisions. Route to an ASCII diagram when terminal-native fixed-width communication is the accepted deliverable.

**Good, bad, and borderline routes**

Good: a team must compare a card's density, hierarchy, interaction states, and target tokens. A playground remains primary for canonical candidate state, negative fixtures, undo, and implementation output. Frontend quality guidance owns the eventual production component and accessibility acceptance.

Bad: a user asks for a final editorial illustration. The implementation builds sliders, preset storage, and copyable JSON even though no user decision requires a reusable tool. Route to image-generation guidance and produce the requested visual artifact.

Borderline: a learning page explains sorting algorithms and includes speed and data-shape controls. First prototype the smallest interaction that distinguishes algorithm behavior. If manipulation changes understanding and supports a testable learning task, keep a bounded playground inside a visual explainer. If users only press play, let the explainer own the artifact and remove unnecessary state machinery.

Good: a configuration laboratory emits a versioned candidate that a separate traceability record links to requirements and consumer tests. Each artifact has one owner and an explicit handoff.

Bad: a Three.js scene stores selection and semantic relationships only in mesh properties because a visualization reference is primary. Scene objects are projections; preserve canonical semantic state outside rendering objects.

Borderline: an internal query explorer becomes a shared operational console. Stop extending the prototype by habit. Reclassify data sensitivity, authorization, persistence, observability, service failures, and product support; then either rebuild under product and domain guidance or explicitly retain a non-operational exploration boundary.

**Verify a routing decision**

1. Confirm the candidate path exists in the current repository.
2. Read the destination reference completely rather than relying on its filename or this summary.
3. Write one sentence naming the user's dominant decision and one sentence naming the final deliverable.
4. Assign ownership for canonical state, interaction, media or scene, output, accessibility, security, persistence, and evidence.
5. Check that supporting references do not define conflicting defaults for the same contract.
6. Remove infrastructure that the new route does not require, or justify why it remains a bounded support artifact.
7. Validate the final artifact with the destination reference's own gates and validate any cross-reference handoff at both ends.
8. Record a pivot trigger, such as exploration becoming a repeated operation or a static explanation gaining a meaningful decision laboratory.

A route is successful when it reduces duplicated obligations, clarifies acceptance criteria, and gives the dominant deliverable an appropriate verification strategy. Consulting more references is not evidence of better routing. When destination content has not been inspected, state only that its repository path is a candidate. Route confidence becomes strong after the destination contract and target acceptance criteria agree.

Treat routing as a lifecycle decision, not a permanent label. A project may begin as a timeline exploration, use a playground to compare assumptions, produce an image or diagram for communication, and end as an operational frontend. Preserve the route history and remove machinery that belonged only to an earlier phase. This keeps accumulated controls, state, and governance from surviving after their decision value has disappeared.

## Workload Model

Treat this as an operating reference for a frontend decision experience, not as a prose summary or a screen-count estimate. Workload is the effort required to make a bounded decision trustworthy across state, interaction, projections, lifecycle, environment, and handoff. A page with four controls can be harder than a page with forty when those four controls affect authorization, persisted schemas, concurrent writers, or executable output.

The planning unit is the smallest end-to-end decision that can be accepted or rejected independently. It is not automatically one screen, component, route, user story, or file.

**Inventory workload pressure**

| Dimension | Questions to answer | Lower-pressure shape | Escalation signal |
|---|---|---|---|
| Decision scope | What choice or understanding must change? Which criteria settle it? | One bounded reversible decision | Several decisions with different owners, criteria, or release consequences |
| Canonical state | Which semantic variables, relationships, constraints, and invalid states exist? | One schema with mostly independent transitions | Coupled constraints, graph editing, conditional groups, or many migration versions |
| Source and data | What enters the tool, at which revision, sensitivity, and trust level? | Synthetic fixture or one read-only trusted source | Uploads, private data, multiple sources, live refresh, adversarial text, or stale-source reconciliation |
| Projection | Which preview, explanation, prompt, exact output, saved artifact, and structured alternative must agree? | Few deterministic projections from one state | Different consumers, partial support, expensive rendering, or projection-specific hidden state |
| Interaction | Which pointer, keyboard, touch, direct-manipulation, undo, and recovery paths matter? | Standard controls with native semantics | Canvas gestures, drag ordering, graph edges, complex focus restoration, or custom spatial input |
| Lifecycle | Does state survive reload, sharing, version change, or source change? | Session-only state with explicit disposal | Autosave, import and export, migrations, collaboration, conflicts, stale anchors, or long retention |
| Effects | What operations can fail or change an external system? | Pure local candidate generation | Network calls, clipboard and download, execution, writes, authorization, cost, or irreversible effects |
| Environment | Which viewport, zoom, input, browser, motion, theme, and assistive paths are supported? | Narrow declared support with native controls | Broad support, embedded hosts, performance-sensitive rendering, or custom accessibility semantics |
| Consumer | Who or what receives the output, and how is it validated? | Human review of a non-executable summary | Parser, compiler, production policy, implementation pipeline, or multiple incompatible consumers |
| Evidence | Which claims require automated, browser, expert, security, or operational proof? | Deterministic local checks and one representative review | Cross-owner confirmation, delayed outcomes, scarce users, sensitive telemetry, or incident evidence |

Classify pressure qualitatively and record the reason. Do not convert the table into a universal point score or engineering-day multiplier. Local architecture, fixtures, support policy, team experience, and consumer tooling determine cost. The inventory is valuable because it exposes missing boundaries and informs decomposition, not because it yields false precision.

**Default initial slice**

Start with one accepted user decision and the most consequential uncertainty within it. Build a vertical slice that includes:

- a representative source fixture and one adversarial or invalid fixture;
- the smallest canonical schema that can express the decision without storing DOM-derived authority;
- initial state, the important valid transition, and the transition most likely to expose invalid or stale state;
- the controls and direct-manipulation path needed for that transition;
- the preview and explanation required to judge the candidate;
- exact output or a reviewable handoff derived from the same state;
- one persistence or disposal path appropriate to the declared lifecycle;
- one recovery exercise, including undo, invalid input, denied operation, or stale source as applicable;
- keyboard and pointer coverage for the core task, plus target-required viewport, zoom, focus, and motion checks;
- the real consumer boundary with highest uncertainty, such as a parser, target component fixture, migration, or named reviewer.

This is deliberately broader than a visual happy path and narrower than the complete feature set. The first slice should cross the riskiest boundary. Implementing the easiest slider first can prove that browser events work while leaving the state model, output contract, or consumer feasibility unknown.

Three viewport classes, one error state, and one keyboard path can be useful starting samples, but they are not capacity limits or sufficiency claims. Select representative combinations from target support and failure risk. A narrow viewport with long content and keyboard focus may reveal more than three empty-layout screenshots. A query builder may need quote escaping, authorization denial, stale schema, and restore failure even if it has one visible route.

**Model combinations from valid transitions**

Do not estimate workload by multiplying every control value. Many combinations are impossible, equivalent, or derived. Instead:

1. Define semantic states and invariants.
2. Identify transitions that cross a constraint, source, lifecycle, effect, or consumer boundary.
3. Group equivalent projections and environment conditions.
4. Select representative positive, negative, recovery, and migration paths.
5. Add pairwise or property-based coverage where interactions are broad but structurally regular.
6. Preserve incidents and discovered defects as regression fixtures.

For a concept map, changing a node label and changing its canvas coordinates are different workload classes. The label affects semantic output, search, accessibility, and persistence. Coordinates may be derived layout unless the user explicitly includes spatial grouping in the decision. Keeping these separate prevents every drag position from inflating the semantic test model.

**Keep, split, or reroute**

Keep one slice when its decision, state, owner, consumer, and acceptance criteria are coherent and it can be released or rejected independently.

Split into sequential slices when a common canonical model supports independently valuable projections or modes. For example, first validate query state and exact serialization; then add schema-aware suggestions; then add saved artifacts and migration. Each slice must preserve prior contracts and produce a complete accepted increment.

Split into separate tools or bounded modules when decisions have different users, data permissions, lifecycles, or consumers. A public visual theme explorer and an internal production configuration editor should not share authority merely because both use sliders.

Do not split when doing so duplicates canonical state or requires temporary synchronization between two partial authorities. That is evidence the boundary follows components rather than the decision contract.

Reroute to a production application when live writes, service reliability, role permissions, collaboration, audit, support, and operational observability dominate exploration. Reroute to a static prototype or visual explainer when the uncertainty is about sequence or comprehension and browser-real behavior is not material. Use a component laboratory when isolated states are the decision and no cross-component state or handoff is required. Use a scripted scenario harness when the uncertain boundary is deterministic domain behavior rather than user-controlled exploration.

**Workload examples**

Lower pressure: a local design-token comparison uses target-like card fixtures, one canonical candidate, undo, narrow and wide views, keyboard controls, and a structured token proposal reviewed by one component owner. It does not persist after the session or execute changes. The first slice can be independently accepted.

Moderate pressure: a document critique tool imports a versioned source, anchors comments to ranges and excerpts, tracks dispositions, detects stale anchors, supports keyboard navigation, and exports a review record. Visible controls remain simple, but source revision and persistence expand the workload. Split anchor migration from collaboration unless both are needed for the accepted first decision.

High pressure: a query playground reads sensitive schemas, supports multiple dialects, persists shared filters, executes queries, enforces row-level policy, streams results, and allows concurrent edits. This is no longer just a playground workload. Separate read-only exploration from execution and route operational behavior to domain and application architecture with security ownership.

Deceptively high pressure: a concept map has only node, edge, and knowledge-state controls, but the canvas is the sole state store, edges are pointer-only, imports accept markup-like labels, and saved files have no version. The visual surface is small; state, accessibility, security, and migration pressure are high.

Borderline: a timeline explorer has one persona and synthetic data, but its causal model and uncertainty ranges are not agreed. Build a small simulation spike that crosses one disputed causal boundary. If the model cannot be made reviewable, reroute or stop before investing in polished controls and persistence.

**Record a workload ledger**

An illustrative ledger can make assumptions inspectable:

```yaml
decision: Compare and hand off one query filter candidate.
profile: shared-decision-aid
state:
  pressure: moderate
  reason: Conditional operators and typed values share one schema.
source:
  pressure: moderate
  reason: Read-only versioned schema; imported filter files are untrusted.
lifecycle:
  pressure: moderate
  reason: Export and restore required; collaboration excluded.
effects:
  pressure: low
  reason: Query execution excluded from this slice.
consumer:
  pressure: high
  reason: Target parser and authorization owner must accept exact output separately.
first_slice_boundary:
  - Build and edit one filter group with keyboard and pointer paths.
  - Reject malformed imported state without changing the active candidate.
  - Restore a versioned candidate exactly.
  - Parse exact output with the named target parser.
excluded:
  - Execute queries.
  - Share concurrent edits.
  - Support a second dialect.
reassess_when:
  - The first parser result or restore fixture changes a pressure classification.
```

The names and values are illustrative. In a target repository, replace them with accepted scope, actual source and consumer versions, real evidence locations, and owners.

**Exit and reassessment gates**

Before broadening the playground, verify that the first slice:

1. preserves exact heading, source, and requirement boundaries relevant to its reference work;
2. keeps one canonical state across controls, direct manipulation, preview, explanation, output, and save or disposal;
3. rejects or recovers from the selected negative case without losing the known-good candidate;
4. completes the core task through supported input modes and representative environment conditions;
5. validates exact output with the named consumer or records why only human review is available;
6. exposes source, state, and consumer uncertainty rather than replacing it with arbitrary values;
7. produces evidence that another reviewer can reproduce;
8. remains independently useful without unfinished future slices.

Then repeat the pressure inventory. Record what the slice revealed about coupling, reusable infrastructure, migration, support, evidence cost, and route fit. Change the plan only when observed pressure alters risk, ownership, or independent acceptance; do not repartition reflexively after every implementation detail.

Useful planning evidence includes the number and kind of contract boundaries crossed, defects found in negative and recovery paths, projection drift, unsupported consumer cases, and assumptions invalidated by the slice. Avoid converting local observations into universal productivity ratios. Future estimates can say, for example, that persisted versioned imports created more work than initially classified and identify the concrete migrations and recovery paths involved.

The second-order planning value is architectural. A pressure that recurs across many playgrounds, such as versioned state migration or accessible graph editing, may justify shared tested infrastructure. A pressure unique to a domain, such as query authorization or causal-timeline semantics, argues for domain ownership rather than a larger generic template. The workload model should help teams discover that distinction before a supposedly reusable playground framework absorbs every possible responsibility.

## Reliability Target

Reliability means that the playground preserves the user's decision, reports uncertainty and operation outcomes truthfully, produces artifacts the named consumer can interpret, and provides bounded recovery when the environment fails. It does not mean that every animation is instantaneous or that one percentage can summarize documentation, browser behavior, state integrity, and routing judgment.

Separate two contracts:

1. Reference reliability governs source boundaries, recommendation routing, explicit assumptions, verification guidance, and internal consistency of this document.
2. Playground reliability governs canonical state, projections, persistence, effects, accessibility, consumer output, detection, and recovery in a target implementation.

The first can be checked substantially within this corpus. The second requires target code, fixtures, browsers, users, consumers, and operational evidence. Do not convert reference conformance into a claim that an implementation is production-reliable.

**Use deterministic release gates where the contract is exact**

| Gate | Required behavior | Evidence | Reopen when |
|---|---|---|---|
| Heading and packet integrity | Frozen headings remain exact; packet shape, questions, fields, uniqueness, and expansion pass | Focused corpus verifier and strict local audit | Spec, seed, reference, packet, or verifier changes |
| Source-boundary integrity | Local evidence, external authority needs, and synthesis remain distinguishable for consequential claims | Claim review against frozen source map | A source, authority, or recommendation changes |
| Canonical-state integrity | Controls, direct manipulation, preview, explanation, output, and saved artifact represent one semantic candidate | Transition and cross-projection fixtures | State schema, event model, or projection changes |
| Save and migration integrity | A valid artifact round-trips; rejected or failed migration cannot corrupt the active known-good candidate | Versioned serialization and negative migration fixtures | Persistence format or support policy changes |
| Consumer integrity | Exact output passes the named parser, schema, compiler, or review contract | Frozen consumer version and result | Consumer version, policy, dialect, or output schema changes |
| Operation truthfulness | Copy, download, upload, network, and execution status reflects actual completion or failure | Denial, timeout, cancellation, partial-failure, and retry observations | Operation implementation or environment changes |
| Recovery clarity | Each documented consequential failure names containment, retained state, user action, escalation, and next route | Failure-table review plus behavioral exercise | A failure class or recovery mechanism changes |

These are release gates, not claims that unknown defects cannot exist. `No knowingly unsupported consequential claim remains after review` is defensible when the claim ledger is clean. `Zero unsupported claims exist` is stronger than any finite review can prove. Preserve that epistemic difference.

Similarly, requiring every documented avoid case to name a route is directly auditable. Claiming that at least 18 of 20 sampled tasks route correctly is not meaningful without defining the task population, sampling method, evaluator agreement, rejected cases, and intended inference. A convenience sample can find confusing guidance; it cannot establish a general accuracy rate.

**Classify failures by consequence**

| Failure class | Example | Default treatment |
|---|---|---|
| Silent state corruption | Hidden filters disappear on save or restore | Block release; preserve known-good state; add regression fixture and migration review |
| Misleading success | Clipboard denial is announced as copied, or parser rejection is shown as valid | Block consequential path; make failure visible and recoverable |
| Unsafe or unauthorized effect | Imported content executes, or syntactically valid output bypasses policy review | Contain immediately; disable effect; involve security or domain owner |
| Inaccessible core task | Keyboard users cannot create an edge or reach output | Block the claimed support path; provide equivalent semantics or narrow support honestly |
| Recoverable availability failure | A non-destructive remote preview times out while state and exact output remain available | Preserve state, show status, allow retry or degraded mode, then measure recurrence |
| Performance degradation | Large valid input delays preview but editing remains recoverable | Set a target-specific budget, instrument representative fixtures, and degrade expensive projection separately |
| Cosmetic inconsistency | Non-essential transition animation differs while semantic state and task remain clear | Prioritize against user impact; do not equate with corruption |
| Guidance disagreement | Reviewers choose different adopt, adapt, or route outcomes | Inspect scenario ambiguity, criteria, and evaluator rationale before claiming routing accuracy |

Severity depends on reversibility, detectability, scope, data sensitivity, effects, and downstream use. A one-second decorative delay and a one-second stale query result may have very different consequences. Do not prioritize by frequency alone; rare silent corruption can deserve stronger controls than common visible retryable failures.

**Define operational objectives locally**

When a shared or production-adjacent playground needs service-level indicators, define each one with:

- the user task and consequence being protected;
- an event or observation that can be collected accurately;
- the eligible population and exclusions;
- the source, state-schema, browser, consumer, and application versions;
- the observation window and segmentation;
- the target and its baseline or owner rationale;
- detection delay, containment, recovery, and escalation;
- a guardrail that prevents gaming;
- an invalidation trigger and review owner.

A target template can be expressed without inventing a universal number:

```yaml
objective: Saved candidates restore without semantic loss.
population: Supported artifacts written by state-schema-v3.
indicator: Deep semantic equality after parse and migration.
target: All release fixtures pass; observed production failures are reviewed individually.
guardrail: Unknown fields are preserved or rejected explicitly, never dropped silently.
detection: Import validation and post-restore projection comparison.
containment: Keep the current known-good candidate unchanged.
recovery: Offer original artifact export, diagnostic details, and supported migration route.
owner: Playground state maintainer.
reopen_when: Schema, serializer, migration policy, or supported version range changes.
```

For latency, availability, routing agreement, or task completion, the target repository must provide representative baselines and consequences. This reference does not supply a universal millisecond, percentile, percentage, or sample size. Small studies can identify defects and disagreement, but rate claims require a defined population and sampling design.

**Prevent misleading measurement**

- Include abandoned, invalid, inaccessible, and recovery sessions in the denominator when they belong to the task population.
- Separate first attempt from retries; automatic retries can hide environmental failure and inflate latency.
- Segment by artifact version, browser support, input mode, viewport, source size, and consumer where those factors change behavior.
- Record partial saves and stale projections, not just the final successful state.
- Distinguish a parser's syntax acceptance from authorization, semantic correctness, and target policy.
- Preserve severe incidents outside aggregate objectives; a low rate does not make silent corruption acceptable.
- Freeze fixture and consumer versions for comparison; do not call an easier task or changed dataset an improvement.
- Avoid telemetry that collects sensitive source content when local or aggregate evidence can answer the reliability question.

**Design detection, containment, and recovery together**

Prevention alone is incomplete because browsers, storage, networks, users, and downstream consumers can fail. For each consequential failure, answer:

1. How is the failure detected before misleading success reaches the user?
2. Which known-good state or artifact remains unchanged?
3. Which effects are stopped, isolated, cancelled, or made idempotent?
4. What does the user see, and which next action is safe?
5. Can the exact failing input and versions be reproduced without exposing sensitive content?
6. Who owns escalation, and what evidence changes the release decision?
7. Which regression fixture or operational monitor prevents recurrence?

For autosave, write a validated versioned candidate to a new record, confirm durable completion, and only then advance the active pointer. A failed validation or storage operation leaves the prior known-good version reachable. For imported state, parse and migrate into isolation; do not partially merge into the active candidate. For copy and download, announce success only after the relevant API confirms it; keep exact output selectable when the operation is denied.

**Good, bad, and borderline reliability claims**

Good: `All state-schema-v3 round-trip and supported migration fixtures preserve semantic equality; malformed and unsupported artifacts leave the active candidate unchanged.` The claim names the scope, versions, expected result, negative behavior, and evidence type. It does not imply that every unknown future artifact will restore.

Bad: `The playground is 99.9 percent reliable.` No task, event, population, window, consequence, or measurement source is defined. The number cannot guide design or release.

Borderline: `Nineteen of twenty reviewed scenarios were routed correctly.` The record may reveal one ambiguous case, but it cannot establish broad routing accuracy until scenario selection, evaluator independence, agreement criteria, and target population are stated. Use it as qualitative defect evidence and narrow the claim.

Good: an exact query passes the named parser and a separate authorization owner confirms the target policy. Syntax and permission remain two evidence rows.

Bad: a parser accepts output after the UI silently drops one hidden filter. Consumer syntax appears healthy while canonical-state integrity fails.

Borderline: a large visualization occasionally misses a preview frame, but canonical state, editing, output, and save remain responsive. Measure target user impact and consider degrading or scheduling the projection; do not classify it automatically with state loss.

**Verification portfolio**

| Method | Reliability claim supported | Important limitation |
|---|---|---|
| Example and property-based transition tests | Invariants across broad generated valid states | Generator may omit real invalid or lifecycle conditions |
| Golden serializer and consumer fixtures | Exact output compatibility for named versions | Does not prove authorization or user intent |
| Versioned migration matrix | Supported restore behavior and explicit rejection | Cannot cover unknown future corruption |
| Browser task matrix | Interaction, focus, operation status, and recovery in tested environments | Environment sample is not universal support |
| Fault injection | Behavior under denial, timeout, cancellation, partial write, and stale source | Injected failure may not match production timing |
| Accessibility inspection and representative tasks | Semantic exposure and core task completion | Needs target policy and relevant user expertise |
| Sampled routing review | Ambiguity and evaluator disagreement | Rate inference depends on population and sampling design |
| Operational observation and incident review | Real distributions and unanticipated paths | Can be delayed, confounded, sensitive, or incomplete |

Require frozen fixtures, commands, observed results, versions, and invalidation triggers. A test name or screenshot alone is not evidence. Challenge a passing path with the negative state it is supposed to detect. For recovery, begin from a known-good artifact, induce failure, and prove that state remains reachable and uncorrupted.

**Release and error-budget use**

For deterministic integrity, security, and consumer gates, a known failure normally blocks the affected consequential path. For retryable availability or performance objectives, a local error budget can guide whether to add features, harden recovery, narrow support, or degrade an expensive projection. The budget must not authorize silent corruption, unsafe effects, knowingly inaccessible core tasks, or unsupported claims.

Exploration and execution can have different profiles. A local preview may tolerate a visible retry while executable output remains disabled until current state passes validation, authorization, and consumer checks. This separation preserves experimentation without weakening the consequential boundary.

Known with strong confidence are results tied to exact fixtures, versions, and deterministic expectations. Sampled human judgments and operational observations support narrower conclusions whose uncertainty depends on selection, environment, and confounding. Every claim inherits the freshness of its least verified dependency: a passing serializer fixture is obsolete when the consumer dialect changes.

Reliability evidence should change architecture. Repeated partial-write pressure suggests transactional versioning. Recurrent projection stalls suggest isolating expensive rendering from editing state. Persistent routing disagreement suggests clearer scenarios or a different adjacent reference. If stronger controls overwhelm a low-risk disposable exploration, narrow or retire the artifact instead of importing production machinery by default. The objective is proportionate trustworthiness, not maximum reliability ceremony.

## Failure Mode Table

Use this table during design review, negative-case implementation, release, and incident learning. It is not a prediction that every failure is equally likely. Instantiate applicable rows with target-specific operations, owners, fixtures, evidence, and escalation policy.

Every consequential response follows this order unless a specialized safety or security procedure overrides it:

1. Detect the failure before presenting misleading success.
2. Stop, cancel, isolate, or disable the affected transition or effect.
3. Preserve the current known-good state, original imported artifact, and relevant source versions.
4. Explain what failed, what remains valid, and which action is safe.
5. Recover through retry, correction, rollback, migration, degraded mode, export, or an adjacent route appropriate to the failure semantics.
6. Capture bounded diagnostic evidence without leaking sensitive content.
7. Add prevention or regression evidence and name the invalidation trigger.

A retry is not a universal recovery action. It is safe only when duplicate effects, stale state, cancellation, authorization, and idempotency are understood. When recovery semantics are unknown, disable the consequential path and preserve an inspectable artifact for the relevant owner.

| ID and failure | Trigger and observable symptom | User consequence | Immediate containment and recovery | Prevention and evidence |
|---|---|---|---|---|
| FP-SOURCE-DRIFT: source or consumer drift | A local source revision, public authority, schema, parser, policy, or target component changes; prior evidence still appears current | Recommendations or output can be valid for an obsolete boundary | Mark dependent claims and artifacts stale; preserve prior versions; block consequential reuse until reconciled | Version evidence, track invalidation events, rerun local corpus and target consumer gates, and record owner confirmation |
| FP-SOURCE-CONFLICT: incompatible evidence blended | Sources with different authority, version, or scope disagree and the synthesis hides the conflict | Users receive one confident rule that no source actually supports | Expose alternatives and affected claims; use the most authoritative applicable source or escalate | Conflict ledger, source-role review, and a fixture or owner decision that demonstrates the chosen boundary |
| FP-GENERIC-ESCAPE: plausible advice lacks target evidence | Theme-neutral best practices or remembered API behavior enter final guidance | Readers may implement unsupported security, performance, browser, or production claims | Narrow or remove the claim; label synthesis; route changing behavior for target verification | Claim-to-source review, exact command or reviewer question, and no knowingly unsupported consequential claim at release |
| FP-STATE-DIVERGENCE: multiple authorities disagree | A control mutates DOM, canvas, or component-local state without updating canonical state | Preview, explanation, output, save, and restore describe different candidates | Stop output and persistence; retain canonical candidate; reconcile through one validated transition | Cross-projection equality fixtures, event-table review, and direct-manipulation parity tests |
| FP-INVALID-COERCION: invalid combination is silently changed | Constraint logic applies defaults or drops values without explanation | User intent disappears and later output looks valid for the wrong state | Reject or surface the specific conflict; keep last valid candidate; offer explicit correction choices | Schema validation, invalid-transition fixtures, and assertions that failed edits do not mutate accepted state |
| FP-HISTORY-LOSS: undo or recovery restores only appearance | Semantic relationships, hidden values, or provenance are excluded from history | Users cannot safely explore or understand what was restored | Disable misleading undo for unsupported transitions; preserve snapshots; offer explicit reset or artifact restore | Semantic replay tests across controls, graph edits, imports, and source changes |
| FP-PROJECTION-STALE: expensive or asynchronous view lags | A delayed render, worker result, or network response completes after state changes | User judges or copies an older candidate | Tag work with state revision; discard stale completion; show pending status without overwriting current projections | Cancellation or revision checks, interleaving tests, and output comparison after rapid changes |
| FP-RENDER-UNSAFE: imported text becomes active markup | Untrusted labels, values, prompts, or documents reach raw markup rendering | Script execution, DOM mutation, misleading display, or data exposure | Stop rendering the unsafe projection; keep raw source isolated; show inert text and validation error | DOM-safe rendering, adversarial text fixtures, reviewed sanitizer only where rich content is required, and security review |
| FP-IMPORT-PARTIAL: parse or migration mutates active state before completion | Malformed, unsupported, oversized, or partially compatible saved artifact is loaded | Known-good work is corrupted or only some decisions survive | Parse and migrate in isolation; leave active state unchanged; retain original artifact and diagnostics | Versioned migration matrix, size limits, atomic activation, and negative fixtures for every supported transition |
| FP-SAVE-PARTIAL: persistence advances before durable validation | Autosave or export is interrupted, storage is full, or serialization fails mid-operation | Last recoverable candidate is replaced by incomplete data | Write a validated new version first; advance active pointer only after success; expose failure and retain prior version | Atomic or transactional persistence, fault injection at write boundaries, and known-good recovery exercise |
| FP-ANCHOR-STALE: review comment floats after source change | Line numbers shift, context repeats, or source revision changes | Feedback is applied to the wrong claim or code region | Mark anchor stale; show original and candidate context; require reviewer confirmation | Revision-aware anchors, context digests, duplicate-match fixtures, and no nearby-line silent reattachment |
| FP-ACCESS-PATH: core task or recovery is inaccessible | Drag, hover, color, canvas, focus, or error behavior lacks an equivalent semantic path | Some users cannot create, inspect, correct, or export decisions | Narrow claimed support or provide keyboard and structured alternatives; preserve state while the path is repaired | Representative task matrix, focus and zoom checks, color-independent meaning, and accessibility-owner review |
| FP-VIEWPORT-FLOW: layout obscures state or action | Long content, zoom, narrow viewport, soft keyboard, loading, or error text changes geometry | Controls overlap, output disappears, focus jumps, or users cannot recover | Preserve state; move focus predictably; make exact output and recovery reachable without hidden gestures | Target viewport and zoom fixtures, screenshot inspection, DOM geometry assertions where useful, and long-content probes |
| FP-OPERATION-FALSE-SUCCESS: effect fails after optimistic feedback | Clipboard, download, upload, fetch, execution, or save is denied, cancelled, or times out | User believes an artifact or effect exists when it does not | Correct status; retain exact current output; permit safe retry only when semantics are known | Await confirmed completion, inject denial and timeout, verify feedback timing, and test duplicate-effect behavior |
| FP-AUTH-MISMATCH: syntax passes but policy rejects use | Parser or schema accepts output that target authorization forbids | A technically valid artifact is unusable or unsafe to execute | Disable execution; preserve candidate; display separate authorization status and owner route | Distinct syntax and permission gates, target policy confirmation, and least-privilege review |
| FP-CONSUMER-DRIFT: exact output and named consumer diverge | Dialect, compiler, schema, token set, or integration contract changes | Copied artifact fails or changes meaning downstream | Mark output unsupported for that consumer; retain state and provide inspectable diagnostics | Golden output plus actual consumer validation, version pinning, and compatibility fixtures |
| FP-ASYNC-RACE: completion order violates current intent | Rapid edits, retries, hydration, workers, or concurrent effects interleave | Old results overwrite new state, duplicate effects occur, or controls become stuck | Cancel obsolete work where possible; compare revisions before commit; isolate idempotency keys or operation tokens | Deterministic scheduler tests, rapid-input browser exercise, and service-side duplicate protection for effects |
| FP-RETRY-STORM: automatic recovery amplifies failure | Repeated transient errors trigger unbounded retries or synchronized clients | Interface freezes, service load increases, cost rises, and status becomes noisy | Stop retries at a bounded policy; preserve local work; expose manual next action and degraded mode | Backoff and cancellation appropriate to target, retry budget tests, and operational monitoring without sensitive payloads |
| FP-RESOURCE-EXHAUSTION: valid or adversarial input overwhelms client | Large graph, document, dataset, image, or expensive projection exceeds practical limits | Browser becomes unresponsive and unsaved decisions may be lost | Cancel or pause expensive work; keep editing state responsive; retain known-good save; offer bounded subset or route | Representative upper-bound fixtures, chunking or worker isolation, cancellation tests, and honest support limits |
| FP-COLLAB-CONFLICT: writers overwrite one another | Shared link or artifact permits concurrent or stale edits without a conflict model | Decisions and rationale disappear silently | Stop automatic overwrite; preserve both versions; surface conflict and require merge or ownership choice | Revision tokens, explicit single-writer boundary or conflict tests, and collaboration audit trail |
| FP-TELEMETRY-BLIND: final success hides failure paths | Only completed sessions are recorded, retries are collapsed, or diagnostic events lack versions | Reliability appears healthy while abandonment and corruption remain invisible | Retain bounded failure and recovery signals; correct denominators; avoid claiming a rate until the population is defined | Metric-contract review, event-version fixtures, abandonment inclusion, and privacy assessment |
| FP-DIAGNOSTIC-LEAK: error capture exposes source content | Logs, analytics, screenshots, or support exports include sensitive values or documents | Privacy, security, or policy breach occurs during diagnosis | Stop capture, restrict access, redact or hash appropriate fields, and follow target incident process | Data-flow review, synthetic diagnostic fixtures, retention limits, and security-owner approval |
| FP-ROUTE-LOCKIN: prototype becomes unsupported operation | Exploration gains users, persistence, live effects, or service dependencies without reclassification | Prototype shortcuts carry production consequence and no owner | Freeze scope or route to product and domain architecture; export current decisions; reassess lifecycle profile | Pivot-trigger review, workload inventory, completeness gate, and explicit production ownership |

Rows can cascade. Source drift can produce invalid state; invalid state can generate stale output; a retry can execute that output twice; incomplete telemetry can hide the entire chain. Link related failure IDs in target records instead of treating the last visible symptom as the root cause.

**Specialized escalation**

The table is sufficient for interface-level design and test planning when failures are local, reversible, and bounded. Escalate rather than improvise when:

- untrusted content, secrets, authorization, code execution, or cross-origin behavior creates a security boundary;
- personal, regulated, proprietary, or retained source data creates a privacy boundary;
- external writes, cost, legal commitments, or irreversible operations require domain and operational ownership;
- collaboration or distributed services require concurrency, consistency, idempotency, and incident procedures;
- safety-critical or high-impact decisions need a domain hazard analysis;
- target accessibility policy or assistive-technology support needs specialist validation.

The specialized owner determines threat, safety, policy, or service semantics. This reference still owns truthful UI status, state preservation, accessible recovery, and an explicit handoff to that process.

**Good recovery: failed imported-state migration**

The user has candidate A open and imports an older artifact. The tool parses the artifact into isolated memory, records its format and schema versions, and attempts a supported migration. One required field cannot be mapped. The tool rejects activation, leaves candidate A and its undo history untouched, preserves the original imported file, explains the unsupported field, and offers diagnostic export and a version-specific route. A negative fixture proves that no projection or saved pointer changed.

Bad recovery: the importer applies recognized fields immediately, ignores the unknown field, resets the rest to defaults, and announces `Imported`. The screen may look plausible, but the known-good candidate and source intent are lost.

Borderline recovery: the tool can render the old artifact read-only but cannot migrate it. This is acceptable only if the interface labels the artifact read-only, prohibits save over the original, exposes unsupported fields, and does not imply current-schema compatibility.

**Good recovery: denied output operation**

The user changes state, opens exact output, and selects copy. The clipboard API rejects permission. The tool reports the failure after rejection, keeps the current exact output selectable, preserves focus near the action, and offers no claim that content was copied. Retrying does not duplicate an external effect because copying is local and current state is reread at invocation.

Bad recovery: the control shows success immediately, catches the rejection silently, and leaves an earlier output string selected in a hidden text area.

Borderline recovery: an older environment lacks the preferred clipboard API. A deliberate fallback can be supported if it is tested, preserves current output, remains accessible, and reports actual success. Otherwise display selectable output and narrow support.

**Verification recipe for each applicable row**

1. Establish a known-good candidate and record its semantic digest or deep expected value.
2. Trigger the failure at the earliest, middle, and latest meaningful operation boundary where ordering matters.
3. Assert that prohibited effects did not occur and the known-good state remains reachable.
4. Inspect user-visible status, focus, explanation, and safe next action through supported input modes.
5. Exercise retry, cancellation, rollback, migration, degraded mode, or export according to the declared semantics.
6. Compare preview, explanation, exact output, persistence, and consumer state after recovery.
7. Confirm diagnostic evidence includes necessary versions and failure identity while excluding sensitive payloads.
8. Repeat with rapid state changes where stale completion or duplicate effects are possible.
9. Freeze the fixture and result, name the owner and invalidation event, and link any specialized review.
10. Add incident-derived conditions that the original synthetic fault did not reproduce.

Observed mechanisms, such as a failed write partially advancing a pointer, can be established directly. Likelihood and severity remain target judgments shaped by environment, data, audience, effects, and recurrence. Record both rather than allowing an estimated risk score to overwrite known behavior.

Feed failures back into the Reliability Target, Workload Model, Completeness Checklist, and template versioning. Repeated partial saves may justify transactional persistence; repeated projection races may justify worker isolation and revision tagging; recurrent authorization confusion may justify separating preview from execution. Conversely, the best mitigation can be removal: delete an unused effect, stop persisting a disposable artifact, or route an operational workflow away from a generic playground. Recovery branches are not automatically better than a smaller and safer decision surface.

## Retry Backpressure Guidance

Retry only after classifying the failed operation and preserving the current known-good state. Repetition is safe when the operation is idempotent or isolated, its preconditions still hold, and the next attempt cannot duplicate a consequential effect. Backpressure protects state, evidence quality, users, and shared resources when those conditions are absent.

This section covers two related but distinct systems:

- runtime retries inside a playground, such as source reads, previews, saves, clipboard access, or execution;
- authoring retries while evolving the reference, such as source reconciliation, packet generation, file writes, verification, and distributed lane coordination.

Do not apply a runtime network policy to authoring work or treat a document-verifier rerun like a service request. They share classification and state-preservation principles, but their operations, effects, budgets, and owners differ.

**Classify before choosing the next action**

| Failure class | Examples | Default response | Resume condition |
|---|---|---|---|
| Transient and safely repeatable | Version-checked read times out; optional preview worker is temporarily unavailable | Bounded retry or user retry with cancellation and current-revision check | Operation still applies to current state and budget remains |
| Stale completion | Earlier render or source response arrives after the candidate changed | Discard result; do not count as a retryable success | Start fresh work for the current revision only if still needed |
| Stale evidence | A source or consumer version changed after prior validation | Stop dependent reuse and refresh through the permitted source path | New evidence is reconciled and affected gates pass |
| Missing context | Required source, owner decision, schema, or fixture is unavailable | Pause affected claim or route; preserve completed work | Context arrives or scope narrows explicitly |
| Deterministic invalidity | Schema validation, parser, migration, or invariant fails for unchanged input | Do not retry; show correction and preserve known-good state | Input, schema, or implementation changes and a fresh validation begins |
| Authorization or policy denial | Target forbids an otherwise valid operation | Do not retry automatically; disable effect and escalate to owner | Authorization or policy changes through the proper process |
| True contradiction | Authoritative sources or requirements cannot both be satisfied | Stop synthesis or implementation at the conflict | Owner resolves priority, scope, or route and records the decision |
| Overload or rate pressure | Queue grows, service throttles, rendering starves input, or agents outpace review | Apply backpressure, shed optional work, pause intake, or degrade | Capacity and queue return to the declared operating range |
| Unknown effect status | Save, execution, upload, or external write may have partially succeeded | Block blind retry; inspect effect identity and preserve local state | Effect is confirmed absent, confirmed complete, or safely deduplicated |
| Explicit cancellation | User, owner, or coordinator stops the operation | Cancel queued and active retries; retain recoverable state | A new deliberate operation is requested |

Changing input, policy, source revision, or authorization creates a new operation. Do not hide it as another attempt in the old loop. A later successful run should record the new preconditions and versions.

**Runtime retry contract**

Before any automatic or manual retry, establish:

- an operation identity and the canonical state revision on which it depends;
- whether the operation is read-only, idempotent, deduplicated, compensatable, or unsafe to repeat;
- whether a stale result can be discarded before it mutates state or effects;
- how cancellation propagates to queued work, active work, and callbacks;
- the locally justified attempt, time, cost, and queue budget;
- what remains available in degraded mode;
- the terminal status, retained artifact, and escalation route after exhaustion.

The reference does not prescribe a universal attempt count, delay, exponential factor, jitter range, or timeout. Those values depend on service policy, user task, rate limits, cost, and consequence. A target policy should still be bounded and reviewable.

An illustrative policy record is:

```yaml
operation: refresh-read-only-schema
state_revision_required: true
effect_semantics: read-only
automatic_retry: bounded-by-target-policy
discard_when: Candidate source selection or schema request revision changes.
cancel_when: User cancels, navigates away, or begins a replacement refresh.
degraded_mode: Keep the prior schema visibly marked stale and disable executable output.
terminal_action: Preserve local filter state and route to source-owner diagnostics.
evidence: Timeout, stale-completion, cancellation, and budget-exhaustion fixtures.
```

Replace these labels with real mechanisms and values. A prior schema may remain visible only if its age and limitations are explicit and no consequential output is presented as current.

**Backpressure order for a playground**

When load or failure pressure rises, preserve the core decision before optional enrichment:

1. Keep canonical editing state responsive and recoverable.
2. Preserve exact current output inspection if it remains valid and safe.
3. Pause or coalesce redundant work for obsolete revisions.
4. Defer expensive decorative animation, previews, suggestions, analytics, or remote enrichment.
5. Bound new imports, graph layout, parsing, and result rendering according to declared support.
6. Disable consequential effects whose freshness, authorization, or idempotency cannot be established.
7. Expose degraded status and a safe next action; do not simulate success.

Coalescing is often better than retrying every intermediate state. If a user moves a continuous control rapidly, render the latest relevant revision rather than queueing all obsolete projections. Preserve semantic transitions needed for undo independently from optional render work.

**Authoring and evolution backpressure**

For long-running reference evolution, the durable unit is one complete section:

1. Complete all ten exact questions and six concrete fields per question.
2. Save that packet section before editing its matching reference section.
3. Rewrite and save the matching reference section from the packet conclusions.
4. Run immediate heading, count, uniqueness, expansion, placeholder, ASCII, whitespace, table, and fence sanity appropriate to the saved boundary.
5. Record a lane journal checkpoint no later than each three-section boundary and at phase transitions.
6. During full packet and reference rereads, persist review progress no later than each five-section boundary.

If a packet write fails, do not proceed to the reference rewrite. If a reference sanity gate fails, fix that saved section before starting another. If normalized uniqueness falls, rewrite only the duplicate values unless broader reconciliation is needed. Preserve all previously valid sections and continue from the next incomplete durable boundary.

Stop new generation when:

- exact question text or packet shape is uncertain;
- source spans or heading order no longer match the frozen seed;
- a consequential claim lacks a source boundary or verification path;
- current edits introduce duplicate normalized field values, forbidden markers, non-ASCII text, trailing whitespace, malformed tables, or unclosed fences;
- another agent's changes overlap the assigned ownership boundary;
- the current spec or coordinator instruction conflicts with the active plan.

Resume after rereading the governing input, reconciling the conflict, and rerunning the failed local gate. Do not respond to verification failure by producing more sections and hoping a final cleanup will absorb it.

**Distributed ownership and queue pressure**

Assign one owner per reference, packet, and lane journal scope. A worker must not reformat, revert, or complete another lane's files. Coordination should expose:

- exact owned paths and assignment order;
- last fully saved packet and reference section;
- current phase and latest test evidence;
- field, question, and section counts;
- frozen source, reference, and packet identities where required;
- next assigned file and explicit stop boundary;
- blockers and owner decisions needed to resume.

When review or merge capacity is saturated, pause new assignments rather than increasing partially complete files. A long queue of unverifiable artifacts is not progress. Backpressure should preserve complete atomic units and make the next safe action obvious.

**Good, bad, and borderline runtime traces**

Good transient read: candidate revision 41 requests a read-only schema. The first request times out. The operation remains relevant, a bounded retry starts, and the user then changes the source, creating revision 42. Cancellation dominates the queued retry; any late revision-41 response is discarded. Revision 42 starts a fresh operation with its own identity.

Bad stale completion: every slider event launches a render promise, and completion order controls the canvas. An old expensive render overwrites the newest candidate and its DOM-derived text becomes copy output. Backpressure and revision checks are missing at both projection and output boundaries.

Borderline cached source: the live schema endpoint is unavailable, but a prior version is available locally. The tool may offer read-only inspection with age and version visible. Execution and current-schema claims remain disabled until freshness and authorization are revalidated.

Good unknown-effect handling: a configuration upload loses its response after dispatch. The UI does not blindly retry. It queries by idempotency identity or routes to the operator to determine whether the effect occurred, while preserving the local artifact.

Bad authorization handling: an automatic retry loop repeats a denied query with increasing delays. No amount of waiting changes policy; the loop wastes resources and obscures the needed owner action.

**Good, bad, and borderline authoring traces**

Good: a section packet is saved, its reference rewrite is saved, and the immediate gate finds one non-ASCII quotation mark. The worker fixes that character, reruns the same cumulative gate, journals the passing boundary, and only then starts the next section.

Bad: an agent holds six packet sections and rewrites in memory, discovers duplicate generic fields at the end, and overwrites earlier valid work during a bulk repair. Atomic durability and backpressure were absent.

Borderline: an external source cannot be refreshed because browsing is outside the authorized method. Preserve local evidence, mark changing external behavior for owner verification, and narrow the recommendation. Repeated speculative retrieval attempts would violate the work boundary and would not increase confidence.

**Verification**

For runtime behavior, use controlled scheduling and fault injection to prove:

- attempts remain within the configured local budget;
- stale completion cannot mutate current state or output;
- cancellation stops queued and active work and prevents resurrection;
- success, deterministic failure, hard denial, and exhaustion are terminal;
- retries cease after a confirmed success;
- unknown effects are inspected or deduplicated before repetition;
- queue pressure coalesces or sheds optional work while preserving canonical state;
- terminal status and recovery remain reachable through supported input modes;
- retry diagnostics preserve failure class, attempts, versions, and abandonment without leaking sensitive payloads.

For authoring behavior, inspect the journal and filesystem history for packet-first/reference-second order, immediate gate evidence, three-section checkpoints, five-section reread checkpoints, exact ownership, and a nonempty next step. Run the canonical focused verifier only after all sections are complete, but use cumulative local gates throughout.

Attempt counts, revision comparisons, queue lengths, cancellation, and duplicate effects are observable. Safe timing, capacity, and acceptable degraded behavior remain target judgments. Version those policies and state their assumptions. Confidence in any retry policy is bounded by confidence in the operation's idempotency and in the mechanism used to observe whether its effect occurred.

Repeated retry pressure is architectural evidence. It may reveal a need for local caching, revisioned workers, transactional persistence, queue ownership, capability separation, or a product-level service boundary. Do not redesign around one harmless transient event, but do not normalize recurring exhaustion as expected behavior. A resilient playground preserves local decision work while shedding optional remote enrichment; when that cannot be achieved, narrow or reroute the artifact.

## Observability Checklist

Observability should answer a named diagnostic, recovery, release, or guidance question with the least sensitive evidence that is sufficient. More logging is not automatically more insight. A raw state dump may expose imported source content while still omitting the schema, consumer version, or operation ordering needed to explain the failure.

Maintain two evidence planes with separate purposes and retention:

1. Reference-evolution evidence shows how this document and its packet were derived, changed, verified, and reread.
2. Runtime evidence shows how a target playground moved through semantic state, projections, persistence, operations, failures, and recovery.

Reference conformance does not prove runtime reliability. Runtime telemetry does not prove that guidance is sourced or that a user made a good decision. Correlate evidence only across an explicit contract.

**Reference-evolution evidence**

For each completed file, record:

- exact reference, packet, archive seed, lane journal, and relevant local-source paths;
- frozen identities such as hashes or repository revisions where the workflow requires them;
- which local sources were fully read, which were content-identical locators, which were intentionally excluded, and why;
- the exact original heading count and order;
- packet section, question, mandatory-field, exact-unique, and prefix-stripped normalized-unique counts;
- per-section expansion evidence against the matching seed section;
- exact focused-verifier command and summarized result;
- strict checks for question text, field shape, headings, placeholders, ASCII, whitespace, tables, fences, unresolved tokens, and duplicate prose;
- shared-suite evidence with unrelated corpus-wide failures distinguished from the owned file;
- complete packet and reference reread checkpoints, including the five-section durable cadence;
- changed paths, current phase, residual uncertainty, blocker status, next assigned file, and stop boundary.

Prefer command, inputs, summarized result, and evidence location over a raw terminal transcript. Preserve enough failure output to identify the failing assertion and ownership boundary. Do not copy unrelated lane output into this file's evidence merely to increase volume.

For an in-progress atomic section, the useful record is small: packet saved, reference saved, immediate cumulative counts, heading equality, expansion, uniqueness, hygiene result, and next section. This supports exact resume without retaining hidden reasoning or unsaved prose.

**Runtime observability profile**

Before adding telemetry, write the question it will answer, the owner who will act, the permitted data, the retention, and the deletion or expiry condition. A disposable local playground can legitimately use no centralized telemetry when deterministic fixtures, visible status, and voluntary diagnostic export provide sufficient recovery.

Observe consequential semantic boundaries rather than every pointer movement:

| Event class | Minimum useful fields | Diagnostic question | Avoid by default |
|---|---|---|---|
| Candidate transition | Event schema, template, state-schema and source versions, transition name, prior and next state digests, outcome | Did the accepted semantic state change as intended? | Raw labels, imported documents, prompts, or full state |
| Projection update | Projection type, requested and completed state revisions, outcome, bounded duration | Did stale or expensive work overwrite the current candidate? | Pixel dumps and rendered content for every frame |
| Validation | Rule or schema identity, state revision, pass or failure class, recovery offered | Which contract rejected the candidate and did state remain valid? | Sensitive invalid values and unbounded error strings |
| Persistence | Operation identity, artifact format and schema versions, state digest, outcome, retained version | Did save, restore, or migration preserve a known-good artifact? | Full saved artifact unless a user deliberately exports it for support |
| External operation | Operation kind and identity, state revision, attempt, cancellation, effect status, authorization status | Was success truthful and was repetition safe? | Credentials, response bodies, query text, or unrestricted endpoint data |
| Consumer validation | Consumer identity and version, output-schema version, state digest, acceptance class | Which exact contract accepted or rejected output? | Full executable output when a synthetic fingerprint is sufficient |
| Recovery | Failure ID, retained-state digest, recovery action, outcome, state revision after recovery | Did the user regain a coherent candidate without corruption? | Private narrative or source content unrelated to recovery |
| Accessibility task | Task identity, supported input mode, environment profile, completion and barrier class | Was the core task and recovery path operable? | User identity, disability inference, or recordings without explicit governance |

Use opaque local correlation identifiers where needed. Avoid globally identifying a person unless the target workflow has a justified and governed need. High-cardinality values such as source paths, arbitrary labels, query text, or raw error messages can create both cost and disclosure risk.

**Illustrative event**

```json
{
  "event_schema": "playground-observation-v2",
  "event_name": "projection_completed",
  "template_revision": "template-revision-20260711",
  "state_schema": "playground-state-v3",
  "source_revision": "source-revision-18",
  "operation_id": "local-operation-417",
  "projection": "exact-output",
  "requested_state_revision": 42,
  "completed_state_revision": 42,
  "state_digest": "synthetic-digest-42",
  "outcome": "accepted-by-target-parser",
  "consumer": "target-parser-v6",
  "recovery_required": false
}
```

All values are illustrative. The record intentionally excludes source content and exact output. If a digest could reveal low-entropy sensitive values through guessing, use a target-reviewed keyed or opaque mechanism rather than a plain hash. Event creation must occur after the observed outcome is known; emitting `accepted` before the parser returns would make the instrumentation itself misleading.

**Correlation and ordering**

For async behavior, record requested state revision, completed state revision, operation identity, attempt identity, and terminal outcome. This makes stale completion and retry behavior visible without treating wall-clock order as semantic order. Use one documented time basis and preserve timezone or monotonic-duration semantics where relevant.

Correlate a failure with recovery through a bounded operation or failure identity. Do not use an unrestricted session dump. For unknown external effects, retain the idempotency or operation identity needed to inspect status, subject to target security policy.

Missing events are meaningful. Define expected event sequences for consequential paths, such as validation followed by persistence success or failure. A coverage check should detect when a required terminal or recovery event is absent. Eventual success must not erase failed attempts, cancellation, or abandonment from the record.

**Latency and workflow measurements**

Record p50, p95, p99, reviewer time, or task time only when all of the following are true:

- the metric protects a named task or user consequence;
- start and end semantics are stable and instrumented in the right order;
- the eligible population, window, exclusions, and missing observations are defined;
- sample volume makes the reported summary meaningful;
- fixture, source size, browser, device class, state schema, and consumer differences are segmented when material;
- a baseline or owner rationale explains the target;
- a guardrail prevents faster but invalid, inaccessible, or stale behavior from appearing better.

Otherwise report bounded observations, such as `the representative large-graph fixture caused input starvation in the tested browser profile`, and avoid unsupported percentiles. Reviewer time can change because task scope, source familiarity, or evidence quality changed; do not attribute causality to the reference without a suitable comparison.

Console error count is a diagnostic clue, not a reliability target. One swallowed state-corruption error can be worse than many expected development warnings, while a clean console does not prove accessibility, consumer validity, or recovery. Record classified errors tied to the task and root cause.

**Visual and browser evidence**

Capture screenshots or recordings when layout, focus visibility, rendering, motion, or visual comparison is the claim. Pair them with:

- viewport dimensions, zoom, browser and relevant runtime version;
- input mode, motion or contrast setting, theme, and representative fixture;
- canonical state revision and projection identity;
- exact task step and expected observation;
- source and component revision;
- limitation, such as absence of assistive-technology evidence.

A screenshot cannot prove focus order, keyboard completion, semantic structure, latency distribution, or output validity. Combine visual evidence with DOM or accessibility inspection, task execution, timing instrumentation, and consumer checks as appropriate. Prefer synthetic fixtures when images might expose source content.

**Diagnostic bundle**

When voluntary support export is justified, let the user inspect what will be included. A minimal manifest can contain:

```yaml
diagnostic_format: playground-diagnostic-v1
created_for: failed-state-restore
template_revision: template-revision-20260711
state_schema: playground-state-v3
artifact_schema: saved-artifact-v2
browser_profile: tested-browser-profile-a
failure_id: FP-IMPORT-PARTIAL
operation_outcomes:
  - parse-rejected
  - active-candidate-unchanged
included:
  - Version metadata
  - Failure classes
  - Redacted event sequence
  - Synthetic state digests
excluded:
  - Imported source content
  - Exact output
  - Credentials and authorization data
retention: Defined by the target support policy.
```

The target implementation must supply actual policy, access, encryption, transport, retention, and deletion behavior. This reference does not authorize diagnostic upload or establish a retention period.

**Good, bad, and borderline evidence**

Good authoring evidence: the journal names the focused verifier command, reports exact owned-file counts and the unrelated shared-suite failures separately, records hashes for frozen artifacts, and identifies the next assignment. A reviewer can reproduce the claim without reading a transcript.

Bad authoring evidence: `tests passed` with no command, input path, result, or acknowledgment that the shared suite contains failures outside the owned file.

Borderline visual evidence: a narrow-viewport screenshot shows no overlap, but no long-content fixture, zoom setting, keyboard path, or focus transition is recorded. It supports one visual observation and nothing broader.

Good runtime evidence: a failed migration event names schema versions, failure class, retained-state digest, and recovery result without storing the imported document. A fixture reproduces the transition.

Bad runtime evidence: every control change logs the complete state, user-entered text, source document, query, and generated prompt to a general analytics stream. The collection is high risk, high cardinality, and not tied to an owner action.

Borderline metric evidence: a latency percentile is computed across a mixed set of small and large graphs and several browser classes. Preserve the raw bounded observation, segment before interpretation, and do not claim one target from the aggregate.

**Verify observability itself**

1. Exercise each consequential transition and confirm the expected event is emitted only after the outcome is known.
2. Intentionally omit or suppress one required event and prove the coverage check finds the blind spot.
3. Trigger stale completion, cancellation, retry exhaustion, partial save, migration rejection, and consumer failure; inspect correlation and terminal outcomes.
4. Use adversarial source values and confirm logs, metrics, traces, screenshots, and diagnostics do not contain forbidden payloads.
5. Validate event schema compatibility, unknown-field behavior, and version migration or explicit rejection.
6. Confirm cardinality bounds and sampling do not erase severe failures, abandoned paths, or denominator context.
7. Verify retention, access, export, and deletion through target-owned policy and infrastructure checks.
8. Reproduce one diagnosis from the retained evidence; remove fields that do not contribute and add only the missing minimum.
9. Compare instrumentation order with state and operation order so success cannot be emitted prematurely.
10. Review whether every collected field still has a decision owner and action; retire purposeless collection.

Direct observations such as file identities, commands, state digests, versions, operation outcomes, and event shape are stronger than interpretations attached later. They can still be wrong when instrumentation timing, denominator, or missing data is flawed. Keep bounded facts and analysis distinct.

Feed actionable evidence into the Outcome Metrics, Reliability Target, Workload Model, Failure Mode Table, and template evolution. Repeated unused controls may be removed; recurring stale projections may be isolated; expensive enrichment that never changes decisions may be shed under backpressure. Combine these signals with user and domain review so instrumentation does not optimize away qualitative value it never measured. Retire an event when its owner and action disappear: permanent collection without purpose is risk, not observability.

## Performance Verification Method

Verify performance against a named user task, supported environment profile, representative fixture, and consequence. This reference does not establish a universal p95 under 100 ms. That value lacks a target device, browser, event boundary, sample, workload, baseline, and rationale, so it must not be reused as an authoritative requirement.

Keep performance and correctness coupled. A faster projection that shows stale state, a coalesced update that breaks undo, or a cached serializer that emits an older candidate fails regardless of timing. Layout overlap is a responsive-correctness failure; screenshots can help detect it, but it is not a latency percentile.

**Define the performance contract**

| Layer | Start and end to define | Representative consequence | Correctness guardrail |
|---|---|---|---|
| Input response | Accepted input event to visible acknowledgement or committed semantic transition | Control feels blocked or focus becomes unreliable | Exactly one intended transition occurs and invalid input remains recoverable |
| State computation | Validated transition start to canonical next state | Derived constraints or large graphs delay editing | State invariants and undo history remain exact |
| Local projection | State revision request to current preview or explanation commit | User compares a stale or incomplete candidate | Completed revision equals current revision; obsolete work is discarded |
| Serialization | Current state to exact output bytes or structured handoff | Copy or save blocks and may use old data | Output matches the current semantic state and target schema |
| Persistence | Save request to durable confirmation or restore to accepted state | User cannot trust that work survives | Known-good artifact remains recoverable through failure |
| Imported-source processing | Input accepted to validated isolated candidate | Large or malformed source freezes the interface | Limits, cancellation, safe rendering, and atomic activation hold |
| Remote enrichment | Current request to accepted response or declared degradation | Suggestions, schema, or preview delay core work | Local editing remains available and stale responses cannot commit |
| Consumer validation | Exact output dispatch to named consumer result | Handoff or execution blocks the workflow | Consumer version, authorization, and result are explicit |
| Long session | Repeated exploration over the declared session shape | History, listeners, caches, or detached objects accumulate | State remains correct, bounded, savable, and recoverable |
| Reviewer workflow | Accepted review task to evidence-backed next action | Reference use consumes unrelated context or produces indecision | Reviewer identifies route, gate, stop condition, and residual uncertainty correctly |

For each applicable layer, the target owner supplies a budget or qualitative acceptance condition and explains why it protects the task. A local control acknowledgement, a large graph layout, a file migration, and a remote consumer need different budgets. Optional projections may have a looser target if editing and exact output remain current and the delayed status is visible.

**Build a fixture matrix**

Use at least the smallest fixture that exercises the contract, a representative expected fixture, the largest declared supported fixture, and an invalid or adversarial fixture. Add mode-specific dimensions:

| Mode | Relevant scale variables | Required semantic check under load |
|---|---|---|
| Design exploration | Content length, component states, candidate history, image assets, viewport and zoom | Target-like content remains readable and output describes the current candidate |
| Concept mapping | Nodes, edges, labels, layout iterations, selection and undo depth | Semantic graph and structured alternative remain equivalent |
| Data exploration | Fields, rows displayed, filters, groups, query size, result chunks | Filter state, source revision, query serialization, and authorization status remain current |
| Diff and review | Files, lines, hunks, comments, anchor revisions, repeated excerpts | Comments retain correct source identity and stale anchors never float silently |
| Document critique | Source length, claims, comments, revisions, search and filter state | Evidence links and dispositions remain attached to the intended source |
| Configuration | Options, conditional groups, presets, saved versions, output size | Hidden values, constraints, migration, and exact consumer output remain correct |

Unsupported input should fail or degrade deliberately. A large graph may switch to a bounded overview while retaining semantic state and exact export. A document beyond the declared local limit may be rejected before parsing, with the source unchanged and a route to a narrower tool. Freezing the browser until the user loses work is not an acceptable overload policy.

**Freeze the environment profile**

Record:

- application, template, state-schema, source, fixture, and consumer revisions;
- browser and runtime version, operating environment, device or hardware profile, viewport, zoom, input mode, motion setting, and theme where material;
- power or throttling mode if deliberately applied;
- cold or warm cache, worker state, storage state, and network condition;
- instrumentation version and whether profiling perturbs the task;
- background activity and known sources of contention;
- run count, exclusions, failures, cancellation, and missing observations.

Do not mix materially different fixtures or environment profiles into one percentile without segmentation. A precise p99 from a tiny or heterogeneous sample is less useful than a bounded trace with honest variance. Use percentiles only when sample semantics and volume support them; otherwise report observed ranges and individual problematic traces.

**Run the verification in phases**

1. Confirm functional and state-invariant tests pass for the fixture without performance instrumentation.
2. Run a cold path that includes initialization, source parsing, schema setup, and first projection as applicable.
3. Run warm repeated transitions while preserving realistic user sequencing and idle boundaries.
4. Exercise rapid input to test coalescing, stale-result rejection, cancellation, and focus responsiveness.
5. Exercise the largest supported fixture and a deliberately beyond-range fixture.
6. Run a long-session scenario with repeated edits, undo and redo, save or export, restore, and projection changes.
7. Induce a remote timeout, denied operation, or worker failure where the layer applies; verify degraded behavior and state preservation.
8. Compare canonical state, preview, explanation, exact output, and restored artifact against expected results after every measured path.
9. Profile the slow trace to attribute time and resources by phase rather than optimizing from a total alone.
10. Repeat after a candidate optimization under the same frozen profile and report both performance and semantic differences.

Warm-up can change compilation, cache, font, image, storage, and parser behavior. Report cold and warm paths separately when both matter. Do not discard slow first runs merely to improve the summary if users experience them.

**Measure resources and continuity**

Wall-clock latency alone misses several playground failures. Observe as applicable:

- main-thread blocking and missed opportunities to process input;
- CPU work by parsing, validation, layout, rendering, serialization, and highlighting;
- memory baseline, peak, retained growth, history size, cache size, and detached resources;
- worker, network, storage, and consumer wait separately from local computation;
- requests launched, coalesced, cancelled, retried, discarded as stale, and completed;
- output bytes, imported-source size, node or row counts, and other scale dimensions;
- long-task or frame behavior when animation or direct manipulation matters;
- user-visible pending, degraded, cancelled, and recovery states.

Tool-call count is relevant to an agent workflow only if it explains cost, latency, or failure pressure. It is not inherently a quality metric. Source count can also mislead when many paths are duplicate locators. Record unique content identity and why each source was required.

**Compact measurement packet**

An illustrative record is:

```yaml
claim: Large supported concept-map fixture preserves responsive semantic editing.
task: Select a node, change knowledge state, create an edge, undo, and export.
fixture:
  id: concept-map-supported-large-a
  manifest: synthetic-concept-map-fixture-manifest-a
environment:
  profile: tested-browser-profile-b
  viewport_class: profile-defined-wide-layout
  input_mode: keyboard
revisions:
  template: template-revision-20260711
  state_schema: playground-state-v3
phases:
  - state-transition
  - graph-layout
  - canvas-projection
  - structured-list-projection
  - exact-export
guardrails:
  - Canonical graph equals expected graph.
  - Canvas and structured list expose the same semantic nodes and edges.
  - Stale layouts never commit.
  - Undo restores semantic state.
result: target-owner-review-required
limitations:
  - Observations apply only to the frozen fixture and environment profiles.
```

Replace all values with actual target evidence. Store summarized phase results, variability, failures, and artifact locations. Keep raw profiles only when their diagnostic value justifies size and sensitive-data review.

**Method selection**

| Method | Best use | Limitation |
|---|---|---|
| Instrumented task trace | Ordering and phase attribution across a real interaction | Instrumentation can perturb timing and requires stable event semantics |
| Browser performance profile | Main-thread, rendering, memory, and network diagnosis | Large, environment-specific, and easy to misread without a task trace |
| Benchmark harness | Stable pure parsing, validation, layout, or serialization kernels | Omits browser lifecycle and user-perceived continuity |
| Memory snapshot and long-session run | Retained growth, detached resources, cache and history pressure | Snapshot interpretation requires expertise and controlled fixtures |
| Screenshot and geometry check | Overlap, clipping, and representative visual state | Does not prove timing, focus order, semantics, or consumer validity |
| Moderated task observation | Perceived interruption, confusion, and recovery | Small observations do not establish broad rates or isolate system cause |
| Field telemetry | Real distributions and device diversity | Privacy, missing data, confounding, and delayed diagnosis require governance |

Use a microbenchmark only after a task trace identifies a stable hot pure boundary. Recheck the complete task after optimizing it. Faster serialization that changes escaping or field order is a correctness regression, not an optimization.

**Good, bad, and borderline evidence**

Good: a graph task uses frozen expected and supported-large fixtures, separates state transition from layout and canvas projection, proves stale layout rejection, checks semantic equality with the structured view, and reports tested browser profiles and variation. An optimization moves layout to an isolated worker while preserving current-state revision checks.

Bad: an empty canvas reports p95 below 100 ms over a small undocumented sample. No node count, environment, input boundary, warm-up, semantic check, or slow trace exists. The number cannot support a target.

Borderline: exact query serialization is stable and fast locally, but remote consumer validation varies. Keep the local measurement and report remote observations separately. Preserve editing and exact output during remote degradation; do not attribute service delay to serializer performance.

Good: a long design session exercises representative content, many reversible edits, save, restore, and output. Memory returns to a bounded range after discarded previews and history follows its declared policy.

Bad: request coalescing improves the average visual update time by skipping intermediate semantic transitions that undo history and generated explanation require.

Borderline: a beyond-range imported document is rejected quickly and safely. It fails a broad unlimited-input aspiration but passes an honest support contract if the size boundary, preserved source, and next route are clear.

**Reviewer-workflow performance**

The reference itself passes its workflow goal when a reviewer can identify the appropriate adopt, adapt, avoid, or adjacent route; the required verification gate; the stop condition; and residual uncertainty without opening unrelated files. Measure reviewer time only for a defined task, source familiarity, input version, and comparison. Faster review is not better when source boundaries or failure modes are skipped.

The leading outcome remains improvement against named decision criteria rather than random novelty. Treat that as decision quality, not a runtime performance metric. A failure signal is guidance that celebrates creativity while leaving accepted criteria, workload, reliability, or failure behavior unspecified.

**Interpretation and action**

Report measurements separately from the owner's target decision. A trace can establish that graph layout dominates one tested task; whether that delay is acceptable depends on audience, optionality, and support promise. Lab evidence does not automatically represent field devices or concurrent remote pressure.

Optimize only after correctness, workload representativeness, and measurement quality are established. Candidate actions include incremental or worker-isolated parsing, revision-aware scheduling, virtualization, bounded history, cache limits, reduced recomputation, projection shedding, or narrower support. Each adds tradeoffs in complexity, cancellation, determinism, accessibility, and recovery that must be tested.

Sometimes the strongest improvement is subtraction: remove an optional projection, reduce the decision-space complexity, stop persisting a disposable artifact, or route a large operational task elsewhere. Performance evidence should inform the Workload Model, Reliability Target, Retry Backpressure Guidance, and Completeness Checklist rather than serving as a standalone speed badge.

## Scale Boundary Statement

This reference is sufficient while one bounded exploratory decision can maintain a coherent canonical state, evidence chain, lifecycle, and accountable handoff. It becomes supporting guidance when operational coordination, domain policy, shared effects, distributed consistency, or governance owns more of the risk than reversible exploration.

Do not use a raw count such as one system, one owner, or one screen as the boundary. A cross-owner read-only handoff can remain simple when the interface is versioned and effects stop at review. A single-team playground can be high pressure when it executes sensitive queries, migrates shared state, or serves production traffic.

**Review scale by pressure axis**

| Axis | Bounded playground shape | Adapt or split signal | Route to broader architecture when |
|---|---|---|---|
| Decision | One accepted comparison or learning task with coherent criteria | Several independently valuable decisions or personas | Decisions have different policies, release owners, or operational consequences |
| State | One canonical schema and validated transition graph | Independent submodels can be accepted separately | Live distributed or multi-writer consistency dominates exploration |
| Source | Ranked, versioned, bounded local or read-only inputs | Several source classes need separate retrieval and freshness policy | Discovery is unbounded, continuously changing, or access-controlled across domains |
| Data | Synthetic or bounded target-like fixtures and explicit retention | Larger inputs need streaming, workers, limits, or specialized rendering | Sensitive, regulated, tenant-isolated, or operational data needs platform controls |
| Projection | Deterministic local views and one reviewable output | Expensive projections can be isolated or degraded | Multiple consumers require independent compatibility and release management |
| Persistence | Session state or versioned artifacts with bounded migrations | A reusable migration service or artifact registry is justified | Shared durable state needs transactions, backup, retention, conflict, and audit policy |
| Effects | Local computation or non-executable handoff | One effect can be isolated behind explicit confirmation and owner review | Irreversible writes, cost, external commitments, or service workflows are core |
| Users | Individual or bounded review group with explicit support | Multiple audience profiles need separate task and accessibility evidence | Broad tenancy, roles, permissions, support, and abuse controls define the product |
| Traffic | Local or bounded use with no production availability claim | Async work, caching, or queue limits protect a declared support profile | Capacity planning, service objectives, incident response, and deployments are required |
| Collaboration | Single writer or explicit artifact handoff | Versioned review and conflict display remain bounded | Realtime editing, merge semantics, presence, audit, and distributed conflicts are required |
| Ownership | One decision owner plus explicit supporting interface owners | Independent slices gain owners and acceptance gates | No owner can verify end-to-end failure containment or authorize consequential behavior |
| Evidence | Focused fixtures, browser tasks, consumer checks, and owner judgment | Specialized security, accessibility, performance, or domain review joins | Compliance, safety, operations, or multi-service evidence needs a governed program |
| Codebase | Ranked source map and bounded dependency impact | Graph-based narrowing identifies separable modules | Change impact crosses many independently released systems without a controlling contract |
| Agent workflow | One owner per atomic reference, packet, and journal scope | Independent files can proceed with frozen inputs and merge checks | Agents share mutable files, assumptions, or queues that cannot be isolated safely |

Classify each axis with evidence and uncertainty. The table informs a route decision; it does not calculate a universal score. Escalate promptly when sensitive data, authorization, irreversible effects, or shared persistence become real, because teams commonly discover their operational cost after a prototype has already acquired users.

**Continue, adapt, split, or stop**

Continue with this reference as primary when:

- the user decision remains exploratory and reversible;
- canonical semantic state fits one coherent contract;
- source and consumer versions can be frozen or marked stale;
- persistence and effects are absent, local, or review-only;
- one owner can verify state through handoff;
- support and failure boundaries are explicit;
- a complete vertical slice can be accepted independently.

Adapt within the reference when pressure is primarily one technique, such as worker-isolated graph layout, bounded source parsing, an accessible structured alternative, or versioned local artifacts. The adaptation must preserve canonical-state ownership and acquire target evidence for the changed boundary.

Split when separate decisions have independent state, users, owners, consumers, and acceptance. A valid split reduces coupling and creates complete interfaces. It does not duplicate semantic state and add synchronization between two partial tools.

Stop or reroute when:

- a prototype begins serving a stable repeated operational workflow;
- live writes, execution, payment, cost, legal commitment, or irreversible effects become core;
- broad roles, tenant isolation, authorization, abuse protection, or audit are required;
- multiple writers need conflict resolution and consistency guarantees;
- production traffic needs capacity, service objectives, deployment, incident, and support ownership;
- sensitive or regulated content requires governed storage, access, retention, or deletion;
- the discovery space cannot be bounded enough to rank sources and test claims;
- no safe degraded mode can preserve local decisions when dependent systems fail;
- no single owner can verify the state-to-consumer chain.

Rerouting does not mean discarding the playground. It may remain a local design laboratory, fixture generator, read-only simulator, migration test bench, or non-production comparison surface. Production services own effects; the smaller lab retains reversible exploration.

**Multi-system and ownership boundaries**

Multiple systems are acceptable when authority changes at explicit interfaces. For example, a local configuration playground can produce a versioned candidate; an executable traceability system can connect that candidate to requirements; a domain service can validate policy; and an operator can apply it through a production workflow. Each handoff names schema, versions, owner, failure behavior, and evidence.

The reference is insufficient when one user transition implicitly spans several systems and no owner can determine whether it partially succeeded. In that case, retries, idempotency, consistency, authorization, observability, and rollback require service and domain architecture. Do not conceal this behind a single `Apply` button.

**Distributed agent execution**

Parallelize only durable atomic units with exclusive write ownership. For this reference-evolution method:

- assign one owner to each reference, matching packet, and lane journal scope;
- freeze the spec, archive seed, assignment order, source-span identities, and exact questions before work;
- save one complete packet section, then its reference section, then immediate sanity;
- journal no later than every three completed sections and every phase transition;
- persist complete-reread checkpoints no later than every five sections;
- never let two agents rewrite the same reference or packet concurrently;
- verify exact paths, headings, counts, uniqueness, expansion, hygiene, and evidence boundaries before integrating results;
- stop at assignment boundaries and do not consume the next owner's work opportunistically.

A merge checkpoint cannot repair two agents making incompatible assumptions inside one section. Split by file only when source and shared-spec inputs are frozen and results can be verified independently. If workers require a shared mutable decision, centralize that decision before continuing.

Treat context drift as a reliability failure. The journal must identify the last fully saved section, exact current counts, failed or passing gates, open risks, next file, and stop boundary. On resume, reread governing inputs and the saved boundary; do not regenerate valid sections from memory.

**Large-codebase and source scale**

A flat source list is not enough. Before applying guidance across a large codebase:

1. Name the user decision and likely owning subsystem.
2. Discover candidate source paths and content-identical duplicates.
3. Rank integrating, mode-specific, historical, illustrative, target-authority, and missing claim roles.
4. Use repository-native dependency or source-graph analysis where available to narrow callers, consumers, state ownership, and change impact.
5. Read the selected sources completely and freeze revisions.
6. Identify independently released modules, generated artifacts, and policy owners.
7. Test one end-to-end slice across the riskiest boundary.
8. Reassess whether this remains a playground task or has become a cross-system product change.

Graph output can also become stale or incomplete. Record the indexed revision, language and file coverage, unresolved dynamic edges, and fallback inspection. Do not turn graph ranking into unquestioned authority.

**Scale review packet**

An illustrative record is:

```yaml
decision: Compare one read-only deployment configuration candidate.
current_route: interactive-playground-primary
axes:
  state: bounded-single-schema
  source: two-versioned-read-only-sources
  persistence: versioned-local-artifact
  effects: excluded
  users: bounded-review-group
  consumer: domain-validator-owned-interface
owners:
  decision: platform-design-reviewer
  consumer: deployment-domain-owner
interfaces:
  - Candidate schema revision 4 to domain validator revision 9.
degraded_mode: Preserve local editing and exact candidate inspection when validation is unavailable.
pivot_triggers:
  - Add live deployment.
  - Add shared concurrent editing.
  - Store tenant configuration centrally.
evidence:
  - State round-trip fixture.
  - Validator compatibility result.
  - Browser task matrix.
verdict: continue-as-bounded-review-tool
```

The values are illustrative. A target record must use real owners, revisions, artifacts, and route criteria.

**Good, bad, and borderline scale decisions**

Good cross-system boundary: a read-only query playground uses a versioned schema service, preserves local filter state when the service fails, emits exact non-executed syntax, and validates it with a named parser. Authorization and execution remain separate owned workflows. Multiple systems exist, but exploration and effects are cleanly separated.

Bad prototype promotion: the same playground gains shared saved queries, credentials, query execution, production datasets, tenant roles, and result export without reclassification. A local retry loop and browser storage are treated as service reliability and persistence. Route to domain, security, product, and operational architecture.

Borderline collaboration: reviewers share exported files and occasionally overwrite changes. If versioned artifacts and explicit single-writer handoff meet the accepted workflow, stay bounded. If simultaneous editing and merge become core, run one conflict-model spike and pivot when version conflicts cannot be resolved outside the tool.

Good agent split: separate assigned reference files use frozen shared inputs and separate packets; each owner journals atomic progress and passes a focused verifier. Integration checks shared corpus counts without rewriting another lane.

Bad agent split: two workers generate alternate halves of one packet and both normalize duplicated generic field values during a final merge. They share semantic and filesystem authority, so throughput creates rework.

Borderline large codebase: dependency analysis identifies one owning module but dynamic plugin registration is unresolved. Complete a bounded source and runtime registration check before claiming impact is local. Preserve the uncertainty and pivot if another independently released plugin owns the consumer.

**Verify a split or route**

1. Inventory all scale axes, evidence, owners, and uncertainty.
2. Map canonical state, sources, consumers, effects, persistence, and failure containment before and after the proposed boundary.
3. Confirm each split has an independently valuable user decision and complete acceptance criteria.
4. Prove semantic state is not duplicated or synchronized informally across splits.
5. Exercise interface version mismatch, unavailable dependency, stale response, cancellation, and partial effect.
6. Confirm a safe degraded mode or document why operational architecture must own the workflow.
7. Route security, privacy, accessibility, performance, service, and domain obligations to named owners without abandoning UI recovery.
8. Re-run dependency and source narrowing on the frozen codebase revision.
9. Verify the original playground can be retired, narrowed, or retained without ambiguous production authority.
10. Record pivot triggers and review again when one occurs.

Systems, schemas, effects, source paths, traffic profiles, and owners can be inventoried directly. The acceptable coordination cost remains judgment shaped by tooling, expertise, deployment, regulation, and incident capability. Confidence is weakest where ownership or failure containment is implicit.

Scale pressure can reveal reusable infrastructure, but centralize only stable mechanics such as versioned artifact envelopes, safe projection scheduling, or tested migration harnesses. Keep authorization, policy, domain semantics, and consequential decisions with their owners. Successful scaling often produces a smaller playground: operational systems take effects and governance, while the lab focuses on reversible comparison and reviewable handoff.

## Future Refresh Search Queries

Do not search for the title `interactive playground template patterns` and treat the results as authority. This reference is a synthesis, not a standardized product name. Future retrieval should begin with a stale or missing claim and the actual selected mechanism, version, consumer, or policy authority.

No web retrieval was performed while evolving this section. The queries below are maintenance examples for a later authorized refresh. Search syntax and result ranking can change; preserve the semantic constraints if the future search system uses different operators.

**Local-first retrieval order**

1. Name the exact claim, decision, and invalidation event that triggered refresh.
2. Inspect pinned dependency manifests, lockfiles, local source, tests, generated schemas, repository docs, and owner decisions.
3. Identify the selected mechanism and version. Do not research generic framework options when the target already pins one.
4. Search the primary publisher, standards body, or official project for that exact mechanism and version.
5. Use release notes, migration guides, compatibility data, and issue trackers only for the question they can answer.
6. Use community and repository examples to discover alternatives or failure cases, not to establish policy or support by themselves.
7. Open and read the selected source; a result title or snippet is not evidence.
8. Reconcile upstream guidance with actual target behavior through tests, probes, and owner review.
9. Update claim confidence, source map, invalidation trigger, examples, and affected fixtures.
10. Rerun focused structural and target verification and record whether guidance changed.

If browsing is not authorized, stop after local evidence. Mark changing external behavior for later owner verification and narrow the claim. Never include private code, source content, credentials, internal hostnames, customer data, or sensitive identifiers in a public query.

**Query ledger examples**

Each string is an example for a named claim. Adapt it to the selected target and pinned version rather than copying it blindly.

| Claim class | Example future query | Preferred evidence | Reject or limit |
|---|---|---|---|
| Browser clipboard operation | `site:developer.mozilla.org Clipboard writeText permissions browser compatibility` | Browser documentation and target browser exercise | Blog-only success pattern, omitted denial behavior, or unscoped compatibility claim |
| Browser persistence | `site:developer.mozilla.org IndexedDB versionchange transaction abort migration` | Browser documentation plus target migration fixtures | Example that partially mutates active state or ignores blocked upgrades |
| Structured cloning | `site:developer.mozilla.org structuredClone supported types exceptions browser compatibility` | Browser documentation and target state fixture | Claim that every application state value can be cloned |
| Focus and dialog behavior | `site:html.spec.whatwg.org dialog focus inert top layer` | Applicable platform standard and target browser task | Tutorial that treats one browser observation as universal behavior |
| Keyboard interaction semantics | `site:w3.org/WAI ARIA Authoring Practices keyboard interaction drag and drop alternative` | Current applicable accessibility guidance and representative task review | Copying a role or key map without matching widget semantics |
| Canvas accessibility | `site:w3.org/WAI canvas accessibility alternative content keyboard` | Applicable accessibility authority plus structured-view task evidence | Screenshot-only accessibility claim |
| Reduced motion | `site:w3.org/WAI prefers-reduced-motion animation accessibility` | Applicable accessibility guidance and target motion check | Disabling all feedback without preserving meaning |
| Untrusted DOM rendering | `site:owasp.org DOM based XSS prevention innerHTML textContent sanitization` | Security authority, selected rendering mechanism docs, and adversarial fixture | Treating syntax highlighting markup as inherently safe |
| Content security policy | `site:developer.mozilla.org Content-Security-Policy script-src trusted types` | Browser and target security policy evidence | Claim that policy headers replace safe rendering and validation |
| Framework state identity | `site:react.dev preserving and resetting state keys official` | Pinned framework documentation and target component test | Generic state advice applied to a different framework or version |
| Framework hydration | `site:react.dev hydration mismatch state browser only API official` | Pinned framework docs, release notes, and target hydration fixture | Workaround copied from an old issue without version review |
| Worker cancellation | `site:developer.mozilla.org Web Workers terminate message event structured clone` | Browser documentation and target stale-result tests | Assuming worker termination alone preserves semantic state |
| File import | `site:developer.mozilla.org File API text arrayBuffer size error` | Browser documentation, size limits, and malformed-input fixtures | Reading unrestricted files before validating support boundaries |
| Download behavior | `site:developer.mozilla.org Blob URL revokeObjectURL download` | Browser documentation and operation-lifecycle test | Leaking object URLs or reporting success before creation completes |
| Performance measurement | `site:w3.org performance timeline user timing specification marks measures` | Applicable specification, browser docs, and target event semantics | Percentiles with undefined start, end, population, or sample |
| Selected framework release | `React official release notes migration hydration state` | Official project release and migration material for the pinned line | Search snippet, package mirror, or unverified summary |
| Selected consumer schema | `official documentation query language parser version migration escaping` | Actual consumer publisher, pinned schema, and executable consumer result | Generic query-builder example used as syntax or authorization proof |
| Accessibility criterion change | `site:w3.org/WAI WCAG keyboard focus appearance current guidance` | Current applicable standard or guidance and target policy owner | Applying draft or superseded text without status and version review |
| Browser compatibility change | `site:developer.mozilla.org browser compatibility clipboard indexeddb structuredClone` | Current compatibility data and supported-browser exercise | Assuming documentation support means target policy support |
| Security guidance change | `site:owasp.org DOM XSS prevention cheat sheet update` | Current security authority and target security review | Importing a mitigation without its trust and parser assumptions |

The generic `official documentation query language parser version migration escaping` example must be replaced at refresh time by the actual consumer name, dialect, and version. It is retained here to show the required semantic terms, not to close any claim. If the selected consumer has no authoritative public documentation, use local schemas, executable probes, and its owner rather than widening to unrelated products.

**Repository and community discovery**

Repository examples can help discover architecture and edge cases after the official mechanism is known. Use a narrow query such as:

- `site:github.com "structuredClone" "undo" "state schema" language:TypeScript`
- `site:github.com "IndexedDB" "schema version" "migration" language:TypeScript`
- `site:github.com "aria" "keyboard" "canvas" "structured list"`
- `site:github.com "stale response" "state revision" worker`

Before using any result, inspect project maintenance, license where reuse matters, version, surrounding tests, issue history, and whether the example is production code, demo code, generated output, or an unresolved defect. A popular repository is not automatically an authority. Community code can show an alternative or counterexample; promote its claim only after target verification and appropriate primary support.

**Release and migration queries**

Run release-note searches only for dependencies actually selected or pinned. Construct the query from the project name, current and candidate versions, affected mechanism, and terms such as release notes, migration, deprecation, breaking change, security advisory, or compatibility. Examples:

- `React release notes hydration state preservation migration official`
- `browser IndexedDB versionchange compatibility release notes`
- `target query parser release notes escaping breaking change official`

Verify that the selected page comes from the official project or publisher and applies to the version transition under review. A changelog can establish that behavior changed; target tests still establish whether this repository is affected.

**Good, bad, and borderline queries**

Good: a target pins a framework version and a hydration test begins failing after an upgrade. The query names the framework, old and new version lines, hydration mechanism, official domain, and migration intent. The reviewer reads official release material, compares local code, reproduces the failure, and updates one scoped recommendation.

Bad: `interactive playground best practices 2026`. It has no mechanism, authority, target, version, or falsifiable claim. Results are likely to mix marketing, tutorials, unrelated products, and search-optimized summaries.

Borderline: a GitHub search finds a well-tested accessible graph editor. It can reveal keyboard and structured-view alternatives, but it does not establish that its semantics, framework version, support matrix, or license fit the target. Keep it as exploratory evidence until those boundaries are checked.

Good no-browse decision: the target behavior depends on a changing browser API, but current work forbids browsing. The reviewer records the API claim, local pinned behavior, target test, and an owner retrieval request. Guidance remains narrow and does not invent current compatibility.

Bad confidentiality decision: a query includes a private document excerpt, internal schema name, customer identifier, and production hostname to find a similar public issue. Stop and use sanitized mechanism terms or internal owners.

**Refresh evidence record**

Use a compact record such as:

```yaml
claim: Clipboard copy success is reported only after confirmed completion.
trigger: Supported browser policy or clipboard implementation changed.
local_evidence:
  - Operation denial fixture.
  - Current browser support configuration.
query: site:developer.mozilla.org Clipboard writeText permissions browser compatibility
retrieved_at: not-performed-during-current-no-browse-evolution
selected_source:
  publisher: none-selected
  title: none-selected
  version_or_date: none-selected
authority_reason: Browser mechanism documentation for the selected API.
target_check: Copy success and denial browser task.
conflicts: not-assessed-without-retrieval
decision: future-refresh-procedure-only
affected_sections: Future Refresh Search Queries
invalidation_event: Clipboard API, browser support, or target policy changes.
```

The values explicitly record that no retrieval occurred during this evolution; they are not missing evidence. A later authorized refresh creates a new dated record with the selected source and decision before citing it.

**Reject weak evidence**

Do not promote a source when:

- only a search snippet was read;
- publisher, version, status, or applicable environment is unclear;
- the page describes a different framework, browser, consumer, or threat model;
- the result is a generated summary with no inspectable primary support;
- a code example omits failure, cancellation, accessibility, security, or migration behavior material to the claim;
- an issue or discussion records one observation but no accepted resolution;
- the source conflicts with the pinned target and the conflict is unresolved;
- access requires exposing confidential terms or content beyond the authorized boundary.

Conflicting results may reveal a real version, environment, policy, or authority distinction. Preserve the disagreement and resolve its boundary; do not average incompatible advice.

**Verify the refresh**

1. Preserve the original claim, query, date, selected source, and target versions.
2. Summarize the source in your own words and quote only the minimum necessary under applicable limits.
3. Identify what the source proves, what it does not prove, and its authority for this target.
4. Reproduce the affected behavior in the pinned target where feasible.
5. Compare with local source, tests, policy, and owner decisions.
6. Update only affected guidance, confidence, invalidation events, and examples.
7. Rerun state, browser, accessibility, security, migration, performance, or consumer gates implicated by the change.
8. Rerun the reference focused verifier and strict hygiene audit.
9. Record a no-change result when evidence was checked and existing guidance remained valid.
10. Retire obsolete queries whose mechanism or decision no longer exists.

Repeated refresh gaps are architectural evidence. They may reveal volatile dependencies, missing local documentation, weak ownership, or claims that should move out of a durable generic reference into target-specific evidence. Automate discovery only when a named owner and decision threshold exist; otherwise change alerts can create review fatigue without improving guidance. Keep stable advice at the level of durable contracts and keep fast-changing API details versioned near the target implementation.

## Evidence Boundary Notes

Evidence labels determine how a claim may be reused, refreshed, tested, or escalated. They do not confer quality by themselves. A source can be accurately represented yet inapplicable to the target version or lifecycle; a synthesized recommendation can be useful yet still require target verification before consequential use.

No browsing or public-source retrieval was performed for this evolution. Therefore, this file currently contains no populated `external_research_sourced_fact` claim. Future-search queries are maintenance instructions, not public evidence. Any later external claim must add the actual source identity, retrieval date, authority rationale, applicable version, and claim scope before using that label.

**Evidence taxonomy**

| Label | Meaning | Permitted use | Required boundary |
|---|---|---|---|
| `local_corpus_sourced_fact` | A statement directly observable in the frozen local source corpus | Describe what a named source contains or requires | Exact path or content identity, source role, revision or hash, and applicable passage |
| `local_target_observation` | A result directly observed by executing or inspecting the current target | Support the exact tested mechanism, fixture, environment, and version | Command or task, input, expected and observed result, versions, and evidence location |
| `derived_structural_fact` | A deterministic result computed from frozen artifacts | Support counts, equality, expansion, heading order, duplicate identity, or schema shape | Inputs, derivation method, result, and invalidation event |
| `external_research_sourced_fact` | A claim directly supported by a retrieved public primary or authoritative source | Describe the exact external mechanism, policy, or version covered | URL or source identity, publisher, retrieval date, status, version, scope, and target reconciliation |
| `combined_evidence_inference_note` | A synthesis that reasons from one or more facts into guidance | Explain causal implications, tradeoffs, and likely design consequences | Supporting facts, assumptions, counterargument, uncertainty, and verification route |
| `illustrative_example` | A fabricated or adapted scenario used to make behavior concrete | Teach a pattern, failure, or verification method | Clear illustrative status and no implication that names, values, APIs, or results exist in the target |
| `recommendation` | A proposed default or action selected from evidence and judgment | Guide adoption, adaptation, avoidance, routing, or escalation | Decision context, alternatives, cost of error, owner, and conditions that reverse the recommendation |
| `unresolved_external_authority_need` | A changing external claim that was not retrieved or verified in the current boundary | Preserve a future research or owner-verification request | Exact claim, likely authority, no-browse or access reason, consequence, and safe interim scope |
| `unresolved_target_owner_need` | A repository, security, policy, accessibility, or domain decision no public source can settle | Route work without inventing authority | Named owner class, blocked decision, retained artifact, and resume condition |

Use claim-level labels where misclassification would change implementation or release. Stable connective prose does not need a tag on every sentence. A section-level boundary is acceptable only when all grouped claims share the same evidence role, scope, and invalidation trigger.

**Current local evidence boundary**

The local source audit established fourteen archive and live locators representing seven byte-distinct source contents. Archive and live copies for each mapped source were content-identical at the audited boundary, so duplicate paths are maintenance locators, not independent corroboration. The seven source contents were read completely and frozen by hash in the work evidence.

Those sources directly support statements about the guidance they contain, including interaction modes, state-management examples, prompt and output shapes, visual structure, and critique workflows. They do not automatically establish:

- current browser compatibility or framework behavior;
- target repository architecture, dependencies, support matrix, or product policy;
- universal accessibility conformance;
- security of a future implementation;
- a production latency or reliability threshold;
- authorization of generated queries, configuration, or effects;
- user preference, learning outcome, or downstream adoption in an unspecified audience.

The local source content also contains implementation hazards that informed synthesis: raw markup rendering patterns, fuzzy nearby-line matching, visual-only canvas or SVG state, timestamp-derived identifiers, DOM-derived exports, hard-coded topology, and arbitrary illustrative ranges or counts. Calling these hazards is a `combined_evidence_inference_note` when the conclusion goes beyond merely stating that the code shape exists. A target security, accessibility, state, or consumer check is still required before claiming an implementation fixes the risk.

**Current derived facts**

The following kinds of claims can be established directly by the final local verifier and strict audit when their commands pass:

- the reference preserves all twenty-six original Markdown headings in exact order;
- every evolved section is longer than its matching archive seed section;
- the packet contains twenty-six section headings and two hundred sixty exact question headings;
- the packet contains one thousand five hundred sixty populated mandatory field lines;
- exact and prefix-stripped normalized field values are all unique;
- reference and packet are ASCII-only, free of forbidden markers and trailing whitespace, and have balanced fences and well-formed tables under the configured checks;
- frozen source-span and artifact identity checks match their recorded inputs.

These are conformance and structural facts. They do not prove every recommendation is correct, every table is complete, every example is optimal, or every target implementation is reliable. The complete skeptical reread addresses prose quality and contradictions but remains human review evidence rather than a mathematical completeness proof.

**Claim record**

A consequential claim can use this compact shape:

```yaml
claim_id: playground-state-authority-001
claim: Preview, explanation, output, and persistence derive from one canonical semantic state.
evidence_role: recommendation
support:
  - local_corpus_sourced_fact: Local state-management sources use centralized state patterns.
  - combined_evidence_inference_note: One authority prevents projection drift and enables reproducible recovery.
scope: Interactive decision artifacts with multiple projections or persistence.
assumptions:
  - Projection functions are deterministic for the relevant inputs.
counterargument: A trivial disposable preview may not justify a formal schema.
target_verification:
  - Transition fixtures.
  - Cross-projection equality.
  - Save and restore round-trip.
confidence: strong-as-design-default, target-implementation-unverified
invalidate_when:
  - The artifact no longer has multiple semantic projections or retained state.
```

The example is a complete illustrative claim record, not evidence that a target has those fixtures. Replace it with repository-native identity and actual results during adoption.

**Confidence dimensions**

Do not collapse confidence into one number. Record dimensions that can differ:

| Dimension | Question |
|---|---|
| Source identity | Is the supporting artifact known, frozen, and independently distinct? |
| Authority | Is the source entitled to define this mechanism, policy, or target contract? |
| Applicability | Does it match the selected version, environment, audience, lifecycle, and consumer? |
| Freshness | Which event makes the evidence stale, and has it occurred? |
| Directness | Is the claim observed, deterministically derived, inferred, illustrative, or recommended? |
| Reproducibility | Can another reviewer rerun the command, task, or consumer check from the recorded inputs? |
| Coverage | Which positive, negative, recovery, migration, and environment paths were exercised? |
| Independence | Are supporting paths separate evidence or duplicate locators of the same content? |
| Consequence | What happens if the claim is wrong, and what evidence level is proportionate? |

Confidence can be high for mechanism behavior and low for product fit. For example, a serializer fixture and parser result may strongly establish exact syntax for one version while authorization and user usefulness remain unresolved.

**Good, bad, and borderline boundaries**

Good local fact: `The archived and live source locators for the mapped playground-builder source have identical audited content hashes.` The claim names the artifacts and equality boundary. It does not call them two confirming sources.

Bad external fact: `Current browsers reliably support this clipboard behavior.` No public source or target browser matrix was retrieved during this work. Recast it as an unresolved external authority need and a target operation-denial test.

Borderline synthesis: `Worker isolation will improve graph interaction.` The design may reduce main-thread contention, but benefit depends on serialization, graph size, scheduling, stale-result handling, and target profiles. Keep it as a candidate optimization until a task trace and semantic guardrails support it.

Good illustrative example: a YAML state or event record uses explicit synthetic identities and says the target must replace them with actual mechanisms. It teaches shape without asserting repository existence.

Bad example promotion: an arbitrary card radius, node count, retry interval, or latency value appears later as the recommended production default because it was concrete in a worked example.

Borderline target observation: one keyboard task passes in one browser profile. It supports that exact path and environment; it does not establish full accessibility or browser support.

**Provenance audit**

1. Freeze source, seed, reference, packet, spec, verifier, and assignment identities required by the workflow.
2. Verify local source paths exist, distinguish unique content from duplicate locators, and identify source roles.
3. Sample direct local facts and compare them with the complete source, not only a heading or excerpt.
4. Trace consequential recommendations to facts, assumptions, counterarguments, and target verification.
5. Search for external-sounding compatibility, security, performance, and reliability claims; confirm each has evidence or unresolved status.
6. Check that illustrative values and examples never reappear as target facts without new evidence.
7. Compare packet revision decisions with evolved prose and investigate unsupported additions or omitted limits.
8. Review conflicts and stale evidence instead of averaging or silently replacing them.
9. Attempt to disprove one high-confidence claim using its stated negative case and applicability boundary.
10. Rerun structural and target gates, then update confidence and invalidation events from observed results.

When a claim changes status, preserve the transition. A design hypothesis can become a `local_target_observation` after a scoped test, while the recommendation may remain judgment. A previously retrieved external fact can become stale after a release and return to `unresolved_external_authority_need` until refreshed.

Evidence metadata should scale with consequence, volatility, and reuse. A disposable private sketch needs less governance than a reusable template emitting executable output. For durable references, keep stable contracts in the narrative and move volatile browser, framework, consumer, and policy detail into versioned target evidence records. This reduces broad rewrites and lets refresh, testing, and ownership focus on the claims actually affected by change.
