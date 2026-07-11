# Ascii Diagram Layout Patterns

Use this reference when an explanation must remain readable as raw monospaced text in terminals, Markdown code blocks, design notes, commit messages, or copied `.txt` files. Decide the page system before drawing a local figure: establish the reader's question, vertical reading order, canvas preset, prose width, anchor columns, and the one visual job each section performs.

The default is a vertically composed 84-column page, with 52-to-64-column prose, stable margins and gutters, one dominant visual move per section, and top-down flow whenever width is constrained. Use 72 columns for compact terminals and 96 only for comparison-heavy pages that still survive the target surface. Height is cheap; split another section before making readers pan horizontally.

ASCII is first-class here: use only printable ASCII, spaces rather than tabs, short labels, straight connectors, and consistent boxes built from `+`, `-`, and `|`. Automated checks prove character, whitespace, and width constraints; a human review must still prove that the diagram type, reading direction, main path, and intended decision are obvious.

Route away when curves, dense graph topology, exact spatial geometry, rich styling, or interaction carries essential meaning. A small ASCII orientation map may still accompany Mermaid, HTML, an image, or a graph explorer, but the two artifacts need distinct purposes. Stable grids are semantic infrastructure: they reveal peer relationships, reduce diff churn, and let a long page disclose complexity one calm screenful at a time.

## Source Evidence Mapping Table

Use evidence at claim level. A source is operational only when its rule changes or confirms a page, pattern, width, label, or verification decision and that decision is checked in the resulting raw text. Authority and relevance are separate: official automation documentation may govern a CI command without supplying evidence for a comparison grid or connector direction.

| source_location_path_key | inspection_status | evidence_class | decisions_supported | limitation_and_artifact_gate |
| --- | --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202603/craft-ascii-diagram-layouts/SKILL.md | complete frozen local read | local_corpus_sourced_fact | Medium boundary; page-system selection; 72/84/96 canvas presets; 52-to-64 prose target; workflow; style rules; resource routing; output contract | Broad entrypoint, not a substitute for a local pattern or final checklist. Confirm the finished page follows one coherent reading order and declared width. |
| agents-used-monthly-archive/codex-skills-202603/craft-ascii-diagram-layouts/references/ascii-diagram-pattern-library.md | complete frozen local read | local_corpus_sourced_fact | System map, flow, sequence, tree, comparison grid, card strip, two-column compare, mechanism trace, and split conditions | Skeleton examples illustrate grammar rather than domain content. Verify the chosen figure answers topology, order, exchange, hierarchy, contrast, gallery, or trace questions directly. |
| agents-used-monthly-archive/codex-skills-202603/craft-ascii-diagram-layouts/references/ascii-diagram-review-checklist.md | complete frozen local read | local_corpus_sourced_fact | First-pass clarity; layout, label, and failure checks; finish criteria | Checklist compliance cannot prove reader comprehension. Pair mechanical checks with a cold-reader or author-withheld-context review. |
| agents-used-monthly-archive/codex-skills-202603/craft-ascii-diagram-layouts/references/editorial-monospace-layouts.md | complete frozen local read | local_corpus_sourced_fact | Glossary-plus-panels, layered walkthrough, two-column compare, mechanism trace, tall variation gallery, and long-page composition | Applies when the deliverable is a composed terminal page, not every tiny figure. Verify each screenful adds one new teaching layer without prose duplication. |
| agents-used-monthly-archive/codex-skills-202603/craft-ascii-diagram-layouts/references/terminal-page-grid-rules.md | complete frozen local read | local_corpus_sourced_fact | Canvas presets, prose and side-note widths, gutters, margins, card repetition, section anatomy, screenful rhythm, and anchors | Presets are defaults, not universal constants. Run the target-width validator and inspect actual terminal or Markdown rendering. |
| https://developers.openai.com/codex/guides/agents-md | inherited mapping; not browsed in this pass | external_mapping_unrefreshed_note; seed label: external_research_sourced_fact | Future checks about current repository instruction behavior when an exact claim becomes material | Its presence cannot decide ASCII layout or support current product claims. A future refresh records checked date, relevant section, and decision impact. |
| https://docs.github.com/actions | inherited mapping; not browsed in this pass | external_mapping_unrefreshed_note; seed label: external_research_sourced_fact | Future checks about current automation behavior for file-backed validation | It does not validate reading order or rendered alignment. Run the local validator and inspect plain text even after CI is configured. |
| https://agents.md/ | inherited mapping; not browsed in this pass | external_mapping_unrefreshed_note; seed label: external_research_sourced_fact | Future comparison with a general agent-instruction format when portability matters | Treat transferred structure as a process analogy, preserve project instructions, and verify the page under local constraints. |

**Progressive disclosure:** always read the canonical skill and final review checklist. Load the pattern library when the local figure is undecided, editorial layouts when the output is a long explainer, and grid rules when widths, gutters, or anchors are material. A long terminal page usually needs all four supplements; a tiny flow may need only the skill, pattern skeleton, and checklist.

Record `(source, question, extracted rule, decision, artifact check, exception)`. Good use loads the grid rules to choose 72 columns for a compact target, then runs the validator and inspects the copied result. Bad use cites all five paths while producing a 130-column figure with tabs. A borderline external analogy remains inference until its public source is refreshed and the resulting local page passes raw-text review.

This pass establishes the five local contents and the historical presence of three public mappings. It establishes no current public-page claim. If a source later drifts, revise only affected decisions; claim-scoped provenance makes correction and migration cheaper than treating the bibliography as one indivisible authority.

## Pattern Scoreboard Ranking Table

The inherited numbers are editorial priorities, not probabilities, benchmark results, or universal quality scores. Their calibration method is unavailable, so retain them as historical ordering and do not average or compare them mathematically. Domain priorities use explicit triggers instead of invented numbers.

| pattern_name_and_key | inherited_score_or_priority | when_it_leads | failure_prevented | direct_gate |
| --- | --- | --- | --- | --- |
| Source Map First (`ascii_diagram_layout_patterns`) | 95; inherited default tier | Before synthesizing reusable guidance | Generic layout advice ignores the five frozen ASCII sources. | Material source-backed recommendations name an inspected path and scope. |
| Evidence Boundary Split (`ascii_diagram_layout_patterns`) | 91; inherited default tier | When facts, external mappings, artifact checks, and judgment mix | Inference acquires authority it has not earned. | Claims distinguish local fact, unrefreshed mapping, observed page behavior, and editorial choice. |
| Verification Gate Coupling (`ascii_diagram_layout_patterns`) | 88; inherited default tier | Before reference or diagram acceptance | Prose describes quality without a checkable artifact. | Each material claim points to validator output, plain-text inspection, or reader review. |
| Page System First | First artifact decision for a substantial page | Before drawing boxes or choosing a local figure | Isolated diagrams accumulate without a coherent teaching sequence. | The outline names each section's one-sentence job and selected page system. |
| Width Budget Before Wording | Hard spatial constraint | Before labels, cards, side notes, or comparisons stabilize | Wrapping destroys alignment and forces late redesign. | Every line fits the declared 72, 84, or 96-column canvas and prose target. |
| Reader Question Matches Figure | Primary semantic decision | When choosing map, flow, sequence, tree, grid, gallery, compare, or trace | A visually valid diagram answers the wrong question. | A cold reader identifies topology, order, exchange, hierarchy, contrast, or mechanism without narration. |
| Straight Main Reading Path | Leads during connector layout | When order or dependency must be followed quickly | Crossings, diagonals, and floating labels create ambiguous edges. | Direction is obvious; primary connectors are straight; labels attach to one path. |
| Stable Grid And Repetition | Leads for peer panels and long pages | When cards, glossary lines, notes, or screenfuls repeat | Drifting widths and gutters imply false hierarchy and create visual noise. | Peer elements share anchors, dimensions, phrasing, and deliberate exceptions. |
| Tight Labels Outside Prose | Leads after geometry stabilizes | When boxes or arrows contain explanatory text | Paragraphs inflate nodes and obscure nouns, actions, and sequence. | Nouns stay in boxes, actions stay on arrows, prose occupies a separate zone. |
| Validator Plus Reader Review | Hard final gate | At candidate and completion review | Mechanically valid ASCII remains semantically confusing or styled-output dependent. | Editorial validator passes and an unstaged plain-text review reconstructs the intended model. |

**Default order for new pages:** reader question, page system, canvas and anchors, modules, local figures, connectors, labels, prose tightening, validator, cold-reader review, full-scroll reconciliation. A single small figure can omit page-level ceremony while retaining medium, width, pattern-fit, and finish gates.

**Override rule:** start with the first concrete failure. A 110-column wrap makes width reduction lead; an ambiguous arrow makes path repair lead; a diagram that passes validation but confuses readers makes pattern selection or explanation structure lead. No numeric score can waive ASCII-only output, width compliance, or visible reading direction.

## Idiomatic Thesis Synthesis Statement

`local_corpus_sourced_fact`: The frozen theme contains five inspected local sources. They define ASCII-only output; vertical-scroll page composition; 72-, 84-, and 96-column presets; narrow prose; stable anchors and gutters; page systems for galleries, glossary panels, layered walkthroughs, two-column comparisons, and mechanism traces; local figures for topology, order, actor exchange, hierarchy, and tradeoffs; and a validator-plus-review finish process.

`external_mapping_unrefreshed_note`: The seed lists three public instruction and automation surfaces under `external_research_sourced_fact`, but this pass did not browse them. They remain future refresh targets and supply no present-tense ASCII-layout claim.

`combined_evidence_inference_note`: An idiomatic ASCII artifact is a composed terminal page whose scroll order teaches a model progressively. The default loop is:

1. State the reader's next practical question and target raw-text surface.
2. Outline sections top to bottom, giving each one sentence and one visual job.
3. Select the page system before the local figure type.
4. Declare canvas, prose width, margins, gutters, card widths, glossary anchors, and note anchors.
5. Draft modules, then select maps, flows, sequences, trees, comparisons, galleries, or traces by the relationship being taught.
6. Keep the main path straight, nouns in boxes, actions on arrows, and paragraphs outside diagrams.
7. Run mechanical validation, inspect copied plain text, ask a target reader to reconstruct the structure, and reconcile the full scroll.

Map the reader's question before choosing geometry. "What exists and connects?" favors
a system map. "What happens next?" favors a flow. "Who exchanges what?" favors a
sequence. "What contains what?" favors a tree. "How do peers differ?" favors a
comparison. "How does an input become an output?" favors a mechanism trace. A long
page remains teachable when each roughly 20-to-40-line screenful adds one new layer
without requiring the prior figure to be reread from the beginning.

The loop may return to the outline when one figure tries to explain topology, time, glossary, and tradeoffs together. Height is cheap; add a vertical teaching layer before widening or crossing paths. Horizontal composition is justified when direct peer comparison is the point and the declared canvas still holds.

For example, a request-lifecycle page may use a system map for participants, a
sequence for the request exchange, and a comparison for retry policies, with explicit
section transitions between grammars. A two-column policy comparison is only
conditionally valid: when the target drops from 84 to 72 columns, stack the peers
vertically unless simultaneous contrast still survives with meaningful labels.

Treat a page dump, accidental vocabulary change, paragraph-filled node, drifting
width, or prose that narrates every connector as a failed composition signal. A
deliberate grammar change can teach a new relationship, but it needs a section
boundary and reader cue. Repeated peers may share a row; unrelated content should not
be aligned merely to fill horizontal space.

ASCII is the wrong primary medium when curves, dense graph topology, exact geometry, rich styling, or interaction carries essential information. A small terminal overview can accompany a richer representation if it names what was omitted and routes readers to the authoritative detail.

Mechanical confidence and explanatory confidence are different. The validator can establish ASCII-only characters, tabs, trailing space, width, prose width, and editorial heuristics. A cold reader establishes whether diagram type, direction, labels, section purpose, and next action are understandable. Stable grids and progressive sections improve portability, maintenance, and context management, but deliberate asymmetry remains valid when it encodes a real conceptual difference.

## Local Corpus Source Map

Use source loading as a decision tree rather than a completeness ritual. The canonical skill sets medium, workflow, page-system, width, style, and validator defaults. Supplements resolve narrower questions and should end in `choose`, `confirm`, `defer`, or `reject` decisions.

| local_source_filepath_value | retrieval_trigger | contribution_to_apply | misuse_or_limit | final_artifact_check |
| --- | --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202603/craft-ascii-diagram-layouts/SKILL.md | Every in-scope ASCII diagram or substantial terminal-page task | Decide medium fit, page system, canvas preset, anchors, module workflow, visual vocabulary, node count, labels, and output order | Compact overview cannot replace specialized pattern and finish detail | Page has a declared reader question, system, width, straight path, concise labels, and direct validator evidence. |
| agents-used-monthly-archive/codex-skills-202603/craft-ascii-diagram-layouts/references/ascii-diagram-pattern-library.md | Local figure type is unresolved or an existing figure answers several questions at once | Choose system map, flow, sequence, tree, comparison grid, card strip, two-column compare, or mechanism trace from relationship semantics | Copying sample content or combining skeletons without roles creates misleading structure | Reader identifies the intended topology, order, exchange, hierarchy, contrast, gallery, or mechanism without narration. |
| agents-used-monthly-archive/codex-skills-202603/craft-ascii-diagram-layouts/references/ascii-diagram-review-checklist.md | Before accepting any candidate and again after full-scroll reconciliation | Check first impression, direction, raw-text sense, ASCII policy, whitespace, alignment, crossings, labels, width, repetition, and finish | A checklist can become ceremonial when evidence belongs to a different revision or target width | Current file passes mechanical checks and a reader reconstructs the page purpose, direction, and main structure. |
| agents-used-monthly-archive/codex-skills-202603/craft-ascii-diagram-layouts/references/editorial-monospace-layouts.md | Output is a long explainer, atlas, field guide, comparison page, or progressive walkthrough | Select glossary-plus-panels, layered walkthrough, two-column compare, mechanism trace, or tall variation gallery and compose screenful rhythm | Editorial systems are unnecessary overhead for one tiny standalone figure | Every section adds one teaching layer, repeated panels align, prose remains outside figures, and the full scroll feels coherent. |
| agents-used-monthly-archive/codex-skills-202603/craft-ascii-diagram-layouts/references/terminal-page-grid-rules.md | Stable widths, gutters, glossary separators, side notes, repeated cards, or page pacing are material | Choose 72/84/96 canvas; 52-to-64 prose; 18-to-28 side notes; 2-to-4 gutters; one margin and repeatable anchors | Presets require target-surface confirmation and should not be copied from examples blindly | Validator and manual inspection confirm line width, prose width, anchor consistency, and deliberate exceptions. |

**Small-figure profile:** read the skill, choose one pattern skeleton, apply the review checklist, and run the validator. **Long-page profile:** read all five sources, outline with an editorial page system, establish grid anchors, choose local figures per section, and finish with both checklist and full-scroll review.

**Source disposition:** `(path, unresolved question, extracted rule, selected or rejected option, target width, final evidence)`. Confirmation counts as useful disposition. Title-only reading does not. Revisit the profile if a tiny figure grows into several sections or if a composed page collapses into one dominant local mechanism.

Good retrieval uses the editorial and grid files for a layered 84-column walkthrough, then the pattern library for one sequence section. Bad retrieval copies a four-card sample into a 72-column target and widens the canvas rather than tightening labels. Borderline work outlines first, compares two plausible page systems, and loads both supplements only until the reader question selects one.

These files are a frozen 202603 corpus. Their source facts remain stable for this pass; newer material would require a deliberate comparison of changed claims. Examples provide grammar, not mandatory vocabulary, widths, or domains. The finish gate remains the actual artifact, not the number of sources mentioned.

## External Research Source Map

No browsing occurred in this pass. Preserve the URLs and historical roles, but treat them as `external_mapping_unrefreshed_note`, not current external facts.

| external_source_url_value | inherited_role | future_supported_scope_after_refresh | current_limit |
| --- | --- | --- | --- |
| https://developers.openai.com/codex/guides/agents-md | OpenAI Codex agent-instruction context model | Current repository instruction behavior when that exact contract affects how ASCII guidance is delivered | Cannot decide page system, width, connector, or figure type; current contents were not checked. |
| https://docs.github.com/actions | Verification and automation model | Current GitHub Actions behavior for running a file-backed ASCII validator in CI | Cannot prove readability, raw-text composition, or reader comprehension; current syntax was not checked. |
| https://agents.md/ | General agent-instruction format | Current cross-tool instruction structure when portability is a stated requirement | A general format analogy cannot override local ASCII rules or project instructions. |

Refresh only when a volatile external claim can change implementation or completion. Record direct URL, owner, checked date, version context, relevant section, supported claim, conflict, changed action, and residual uncertainty. Then rerun the local validator and inspect the copied page; public documentation cannot prove local alignment.

Good future use refreshes automation documentation for a concrete CI failure. Bad use cites it to justify a two-column compare. Borderline use borrows an instruction layout as editorial structure, labels the transfer as inference, and confirms that canvas, ASCII-only, and raw-text constraints survive.

Link availability is not semantic support. Event-driven refresh is the default; schedule checks only for external surfaces the workflow actively depends on. Record a no-impact result when a source confirms that no local change is needed.

## Anti Pattern Registry Table

Diagnose the earliest broken layer: medium, canvas, page system, local pattern, connector path, grid, labels, prose, or evidence. A finding needs an observable portability, ambiguity, or reader-cost signal; unconventional composition alone is not a defect.

| anti_pattern_failure_name | cause_and_consequence | detection_signal | safer_replacement | exception_boundary |
| --- | --- | --- | --- | --- |
| `context_free_summary_output` | Local source constraints disappear into generic advice. | No source disposition affects a concrete layout decision. | Read the canonical skill and relevant supplements; trace rules into the page. | A source may be skipped with a reason proving it cannot reverse the decision. |
| `unsourced_recommendation_claims` | Editorial judgment sounds universal or measured. | Width, readability, or format claims have no source, target test, or uncertainty. | Separate fact, observed artifact behavior, and reader judgment. | A preference is valid when named and owned rather than disguised as fact. |
| `unverified_agent_instruction` | Quality language has no falsifiable gate. | No validator command, target copy, or reader question exists. | Couple each material recommendation to mechanical or comprehension evidence. | Exploratory drafts may defer full gates but cannot claim acceptance. |
| `unicode_portability_leak` | Box drawing, emoji, or typographic symbols render inconsistently or violate raw ASCII. | Any byte above ASCII appears under the strict profile. | Replace with printable ASCII grammar and rerun validation. | Use a different declared profile and medium when Unicode is a requirement. |
| `tab_or_trailing_space_alignment` | Invisible editor behavior creates unstable columns and noisy diffs. | Validator reports tabs or trailing whitespace; copied alignment changes. | Use spaces, remove line-end padding, and retest the target surface. | None under strict file-backed portability. |
| `width_budget_overrun` | The page widens to accommodate labels or topology, forcing wrap and horizontal scanning. | Any line exceeds the declared canvas or wraps in the promised renderer. | Tighten wording, stack modules, split figures, or choose a richer medium. | A verified 96-column comparison page is valid when target surfaces support it. |
| `one_giant_figure` | Topology, time, glossary, and tradeoffs share one dense canvas. | Reader cannot state the figure type or main path quickly. | Split into vertical sections with one job and one local grammar each. | A compact overview may summarize detail when omissions are explicit. |
| `paragraph_inside_box` | Explanatory prose inflates nodes and hides noun/action structure. | Box labels wrap or require line-by-line narration. | Keep nouns in boxes, actions on arrows, and prose in a separate zone. | Short two-line attributes remain labels when they scan as peers. |
| `ambiguous_connector_crossing` | Diagonal or crossed paths make edge ownership uncertain. | A label or arrow could belong to more than one relationship. | Straighten the main path, reroute vertically, split topology, or change medium. | One clearly bridged crossing may survive only after target-reader confirmation. |
| `mixed_visual_grammar` | Boxes, branches, timelines, and decorative symbols compete inside one figure. | Readers cannot infer whether space means topology, order, or hierarchy. | Use one visual vocabulary per figure and cue grammar changes at sections. | A composed page may use different grammars across labelled teaching layers. |
| `panel_grid_drift` | Peer cards vary widths, heights, gutters, or phrasing without semantic reason. | Visual emphasis appears accidental and diffs churn on unrelated edits. | Recompute shared dimensions and make exceptions deliberate. | Asymmetry is valid when it encodes a named difference readers perceive. |
| `random_centering_and_floating_labels` | Elements lack stable anchors, so labels and notes appear detached. | Alignment changes locally or a note could annotate two lines. | Choose margins, separator columns, and note anchors before wording. | Centering can serve a single headline, not arbitrary local blocks. |
| `prose_diagram_duplication` | Text narrates every visible line instead of adding interpretation. | Removing either artifact loses no information. | Let setup prose state purpose and the figure show structure; reserve notes for implications. | Brief reading notes may call out a nonobvious exception. |
| `screenful_blob` | A long page has no breathing space or single-purpose chunks. | A 20-to-40-line stretch performs several unrelated teaching jobs. | Add section boundaries, whitespace, and progressive layers. | A continuous mechanism trace may remain dense when interruption would break causality. |

Repair hard portability failures first, then width and page structure, then semantic pattern fit, connectors, grid, labels, and prose. Preserve the failing copy at the same target width. A wrong page system can cause width overflow, label compression, crossings, panel drift, and prose bloat; fix that upstream cause before polishing local borders.

For a tiny figure, require ASCII, width, direction, pattern fit, and raw-text checks. For an editorial page, add grid, screenful rhythm, repetition, full-scroll, and cold-reader evidence. Validation must occur after copying into the promised container because the source editor can conceal wrapping and font assumptions.

## Verification Gate Command Set

Run the generated-reference gate from the repository root after editing this reference:

```bash
python3 agents-used-monthly-archive/idiomatic-references-202606/tools/verify_reference_generation.py --stage final
```

That command validates the reference-generation contract, not an ASCII diagram's characters, widths, alignment, or meaning. For a file-backed composed page, run the bundled layout validator with the page's declared limits:

```bash
python3 agents-used-monthly-archive/codex-skills-202603/craft-ascii-diagram-layouts/scripts/check_ascii_diagram_quality.py path/to/page.txt --max-width 84 --max-prose-width 64 --editorial
```

Use 72, 84, or 96 for `--max-width` according to the run card. Omit `--editorial` for one minimal figure. The validator also accepts `-` on stdin and can emit `--json` for automation. Do not use `--allow-unicode` under this reference's strict ASCII profile.

| claim | gate | pass evidence | limit |
| --- | --- | --- | --- |
| Reference structure | Repository verifier plus focused 26-heading and packet checks | Fresh command status and scoped output | Does not inspect a delivered diagram. |
| Character and whitespace portability | ASCII validator | No Unicode, tab, or trailing-space violations | Cannot prove semantics. |
| Canvas and prose width | Validator with declared limits | Every line and prose zone fits the target | Destination rendering may still wrap differently. |
| Editorial composition | `--editorial` heuristics plus full-scroll inspection | Stable zones, spacing, and alignment with no flagged violation | Heuristics do not establish taste or teaching quality. |
| Target rendering | Copy raw text and code block into every promised narrow surface | No wrap, clipping, font-dependent symbol, or collapsed alignment | Screenshots are supporting evidence, not the raw-text deliverable. |
| Reader comprehension | Ask the intended reader to identify diagram type, direction, main path, key relation, and next action | Answers match the page's declared teaching goals without author narration | Results depend on audience knowledge and must be scoped. |

During drafting, run cheap ASCII and width checks. At candidate milestones, add target-copy and reader checks. A good packet records path, revision, declared widths, exact command, result, copied surfaces, reader questions, verdict, and uncertainty. Exit zero alone is insufficient, and a visually attractive screenshot cannot replace raw-text validation.

Before acceptance, run one bounded robustness probe: copy the candidate into the next
narrower promised preset, lengthen the hardest realistic label, or both. The page must
stack or reflow without changing meaning, or fail with an explicit surface boundary
and route. Retain one representative failed width or reader case as a regression
fixture when it captures a defect likely to recur.

## Agent Usage Decision Guide

Use the output contract and reader question, not keywords alone, to route the task.

| usage_mode | choose_when | next_action | boundary |
| --- | --- | --- | --- |
| Primary | The explanation must survive raw-text copy, terminal rendering, Markdown source, or a plain `.txt` file. | Select reader question, page system, canvas, anchors, local pattern, and verification path. | ASCII owns the authoritative explanation. |
| Companion | A richer document, slide, HTML page, Mermaid diagram, or graph explorer needs a portable orientation summary. | Build a small ASCII overview with explicit omissions and route to authoritative detail. | Do not maintain two silently conflicting models. |
| Avoid as primary | Curves, dense crossings, exact geometry, rich visual styling, or interaction carries essential meaning. | Route to the appropriate richer medium and retain prose or ASCII only for orientation. | Compression must not remove action-critical relationships. |

**Full-page preflight:** intended reader; next practical question; target surfaces; 72/84/96 canvas; prose and note widths; page system; section jobs; local figure per section; stable anchors; expected reader answers; exact validator command. **Small-figure preflight:** relationship type, reading direction, target width, label vocabulary, and finish gate.

Every side-by-side panel asserts that its contents are peers worth comparing. Do not
create a row merely to fill horizontal space; stack unrelated jobs and preserve their
distinct reading order.

Choose local figures semantically: topology -> system map; ordered process -> flow; actors over time -> sequence; hierarchy -> tree; several tradeoffs -> comparison grid; peer concepts -> card strip; exactly two alternatives -> two-column compare; one dominant path with notes -> mechanism trace. Split when one figure tries to answer two questions.

Stop before drafting when purpose is unclear, no width is declared, several sections repeat one job, or the target rendering surface cannot be inspected. Exploration may compare small skeletons, but convergence freezes one baseline. Record rejected media and the constraint that rejected each one, so they reopen only when that constraint changes. A good use builds an 84-column layered request walkthrough; a bad use compresses a dense dependency graph into crossing arrows; a borderline hybrid provides a five-node orientation map and links an interactive explorer for detail.

Preserve evidence boundaries: local sources define defaults, public mappings remain unrefreshed, validator output establishes mechanics, and readers establish scoped comprehension. Medium selection is information architecture: it determines grammar, ownership, verification, and maintenance cost.

## User Journey Scenario

This hypothetical journey demonstrates decisions rather than measured reader results.

**Brief:** a documentation author must explain an asynchronous request path to a cold operations reader. The reader needs to know who accepts the request, where work is queued, when persistence occurs, why `202` returns before completion, and where to inspect failure. The deliverable must survive raw Markdown and an 84-column terminal.

| phase | author_action | selected_evidence | failure_branch |
| --- | --- | --- | --- |
| Intake | State audience, next operational question, target surfaces, and facts that must remain technically authoritative. | Reader contract and omission list. | Route domain correctness to a technical reviewer before layout polish. |
| Outline | Compare a layered walkthrough and mechanism-trace skeleton, then choose `Layered Walkthrough`: essence, component orientation, actor exchange, mechanism trace, failure notes. | One sentence, one visual job, and one owning section or routed artifact for each fact. | Insert a glossary layer when vocabulary blocks the mechanism; merge repetition; split any section that teaches topology and time together. |
| Grid | Declare 84 columns, 60-column setup prose, stable actor anchors, two-space peer gutters, and one side-note column. | Page run card and empty skeleton. | Tighten wording or stack before widening. |
| Local figures | Use a small system map for components, a sequence for messages over time, and a mechanism trace for worker persistence. | Pattern-selection rationale from the library. | Replace an all-in-one mega-sequence when labels wrap or paths cross. |
| Convergence | Freeze width and page system; shorten nouns, move actions to arrows, keep explanatory paragraphs outside figures, and align repeated actors. | Equivalent-width before/after copies. | Re-outline if prose narrates every line or sections redraw unrelated grammars. |
| Acceptance | Run the strict editorial validator, paste into promised surfaces, and ask a target reader to identify direction, ownership, return timing, and failure inspection. | Command output, target copies, reader answers, uncertainty, and revision. | Mechanical pass plus wrong answers triggers semantic pattern or vocabulary repair. |

**Good outcome:** five calm screenfuls reveal one layer at a time; actor names and anchors remain stable; no line exceeds 84 columns; the reader predicts that the API returns before worker persistence and locates the failure note without narration. **Bad outcome:** one 120-column sequence includes every service, retry, database, and glossary definition, then prose repeats it line by line. **Borderline outcome:** a five-node ASCII orientation map is retained while dense dependency detail moves to an authoritative graph explorer with explicit linkage.

If a reader cannot explain a domain term, add the smallest glossary layer before
mechanism detail rather than expanding every box. If the same fact appears in setup
prose, a figure, and a note, choose one owner and let the other locations interpret or
route to it. This keeps progressive layers cumulative instead of repetitive.

Retain the accepted page, declared widths, pattern choices, validator result, reader questions, omissions, and one informative rejected skeleton. The durable artifact is both raw text and a reader contract another author can retest after edits.

## Decision Tradeoff Guide

Choose by reader task and output contract before source agreement.

| decision | choose_when | cost | falsification_question |
| --- | --- | --- | --- |
| Adopt ASCII as primary | Raw-text portability, vertical reading, stable monospaced alignment, and bounded relationships are central. | Less spatial freedom and styling, but excellent copy stability and diffability. | Does the narrowest target preserve every action-critical relation without horizontal panning? |
| Adapt as companion | A richer artifact owns detail while a terminal overview or fallback remains useful. | Two representations need authority and drift management. | Are omissions explicit, links stable, and conflicting detail resolved in favor of one source? |
| Avoid ASCII as primary | Curves, dense crossings, exact geometry, rich visual hierarchy, or interaction is essential. | Richer tooling adds rendering dependencies but avoids semantic compression. | Would simplification hide a relationship the reader needs to act correctly? |
| Cost of wrong choice | Format, page system, or figure grammar mismatches the question. | Rework, misleading edges, wrapped output, and reader confusion increase after prose and alignment harden. | Can a small target-width skeleton disprove the choice before full drafting? |

| page_system | choose_when | principal_tradeoff | proof |
| --- | --- | --- | --- |
| Tall Variation Gallery | Many small variations form an atlas. | Easy vertical scanning; weak for one continuous mechanism. | Every variation has parallel structure and adds distinct information. |
| Glossary Plus Panels | Readers need aligned definitions before peer cards. | Strong vocabulary support; can duplicate labels if prose and panels repeat. | Glossary separators and card grid align; panels add structure beyond definitions. |
| Layered Walkthrough | Intuition should precede components and mechanism. | Supports teaching; repeated anchors must remain coherent across layers. | Each screenful adds one layer and reuses stable vocabulary. |
| Two-Column Compare | Exactly two options need simultaneous category comparison. | Direct contrast consumes width and can wrap narrow terminals. | Both columns fit the declared canvas with matched categories and gutters. |
| Mechanism Trace | One sequence dominates and short side notes matter. | Excellent causality; poor for broad topology. | Main path is straight and every note has one unambiguous anchor. |

Local figure selection remains semantic: system map for topology, flow for ordered processing, sequence for actors over time, tree for hierarchy, comparison grid for several tradeoffs, card strip for peer concepts, two-column compare for exactly two alternatives, and mechanism trace for one path plus notes. Split a figure that tries to satisfy two of those questions.

Canvas choice is operational: 72 for compact terminals, 84 for most explainers, 96 for verified comparison-heavy pages. Prose stays near 52 to 64 columns; side notes near 18 to 28; peer gutters near 2 to 4 spaces. These are source-backed presets, not universal reader constants. Fix wording and stack content before widening.

Compare minimal skeletons with the same content, canvas, and reader question. Record target-copy output, validator result, reader answer, omitted detail, reversal condition, and the author's familiarity with each grammar. State reader vocabulary assumptions and route technical facts to subject review; a mechanically clear page can still be inaccessible or wrong. Prefer the choice that reveals the model with the least irreversible alignment and prose investment.

## Local Corpus Hierarchy

`Canonical` means entrypoint and coordinator of broad defaults, not sole authority. `Supporting` means narrower evidence that can constrain a canonical default. `Legacy`, `duplicate`, and `conflicting` require explicit version, overlap, or incompatible-claim evidence rather than age or resemblance alone.

| local_source_filepath_value | hierarchy_role | primary_question | contribution | limit_or_conflict_action |
| --- | --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202603/craft-ascii-diagram-layouts/SKILL.md | canonical frozen entrypoint | What medium, page system, workflow, style, and validation defaults govern the task? | Full decision sequence and guardrails for terminal-native pages. | Coordinate with narrower sources; do not use broad defaults to overrule target evidence silently. |
| agents-used-monthly-archive/codex-skills-202603/craft-ascii-diagram-layouts/references/ascii-diagram-pattern-library.md | supporting figure grammar | Which local skeleton represents the reader's relationship question? | Eight figure patterns and split conditions. | Examples are structural; recompute labels and dimensions for the target. |
| agents-used-monthly-archive/codex-skills-202603/craft-ascii-diagram-layouts/references/ascii-diagram-review-checklist.md | supporting finish authority | What visible and mechanical failures block acceptance? | First-pass, layout, label, failure, and finish checks. | A pass cannot prove technical facts or reader learning without scoped review. |
| agents-used-monthly-archive/codex-skills-202603/craft-ascii-diagram-layouts/references/editorial-monospace-layouts.md | supporting page composition | Which long-scroll teaching system organizes multiple local figures? | Five page patterns and composition rules. | Use only when the deliverable is a composed explainer rather than a tiny figure. |
| agents-used-monthly-archive/codex-skills-202603/craft-ascii-diagram-layouts/references/terminal-page-grid-rules.md | supporting spatial constraints | Which canvas, prose width, gutter, anchor, and rhythm rules stabilize the page? | Presets and repeatable grid contracts. | Validate against actual target width; presets are defaults rather than universal constants. |

**Hierarchy profiles:** small figures use skill -> pattern -> checklist. Long pages use skill -> editorial system -> grid -> local patterns -> checklist. Revisit the profile when scope changes. Always retain strict ASCII, declared width, clear direction, and final target-copy review.

When sources appear to conflict: state exact claims; compare source version, scope, artifact size, canvas, and audience; decide `keep`, `adapt`, `decline`, or `defer`; name a target-width or reader test; preserve both observations and the result. A verified 72-column target can override an 84-column default locally without making the preset incorrect.

Record `(role, question, constraint, decision, exception, evidence)`. Good hierarchy loads grid rules after choosing an editorial page and shortens labels to preserve 84 columns. Bad hierarchy copies a pattern skeleton and claims canonical authority without checking its semantics. A bounded adaptation may use deliberate asymmetric cards when reader evidence confirms that asymmetry communicates a real priority.

These roles organize the frozen corpus and are not intrinsic declarations by the files. Repeated relevant target exceptions may trigger a future refresh; one unusual page remains a local adaptation.

## Theme Specific Artifact

Use a terminal-page run card as the theme-specific artifact. The card is a compact,
diffable record of why a page has its current shape; it is not a second copy of the
page. One card covers one falsifiable reader journey under one audience, ownership,
canvas, and acceptance contract. Split the card when any of those contracts diverge.

| run_card_field | completion rule | why it is retained |
| --- | --- | --- |
| reader_goal | Name the question a reader must answer or the action they must take. | Prevents a decorative figure from replacing the task. |
| target_surfaces | List terminals, Markdown renderers, logs, or plain-text exports that must work. | Defines the portability boundary. |
| canvas_contract | Record hard width, default width, prose width, tab policy, and ASCII-only policy. | Makes wrapping and character failures reproducible. |
| page_system | Choose Tall Variation Gallery, Glossary Plus Panels, Layered Walkthrough, Two-Column Compare, Mechanism Trace, or a small-figure profile. | Connects the reader task to the global composition. |
| section_jobs | Give each page section one primary job and an intended reading order. | Exposes duplicated or missing content. |
| local_figure_map | Match each reader question to a flow, sequence, tree, state, comparison, or grid. | Keeps figure grammar intentional. |
| grid_anchors | Record shared left edges, gutters, columns, and repeated card dimensions. | Prevents local edits from causing page-wide drift. |
| label_budget | Capture the longest important labels and the chosen shorten, wrap, or widen response. | Treats text as geometry before final copy arrives. |
| visual_vocabulary | List the few border, connector, status, and emphasis forms allowed on the page. | Preserves scan consistency. |
| omissions_and_routes | State what detail is omitted and where a reader can obtain it. | Distinguishes progressive disclosure from missing evidence. |
| candidate_identity | Pair a stable name or revision with the exact source text under review. | Stops validator output from being attached to a stale candidate. |
| verification_packet | Link width scans, ASCII checks, target-surface renders, reader tasks, and review notes. | Supports mechanical and editorial acceptance. |

Move the card through `draft` and `candidate`, then close it as `accepted`, `rejected`,
or `archived-study`.
A draft may contain provisional geometry. A candidate freezes copy, anchors, and
canvas values long enough to collect evidence. An accepted card identifies the
validated page revision. A rejected card names the violated contract and the next
route or stop condition. An archived study records a tested learning, such as proving
that a two-column comparison cannot remain legible at 72 columns; it must not imply
delivery readiness.

For example, an async-request walkthrough might record an 84-column hard canvas, a
60-column prose measure, a Layered Walkthrough page system, a vertical request sequence, one
shared card width, straight main-path arrows, and a routed retry appendix. Its
verification packet would contain the ASCII validator result, longest-line scan,
renders from each required surface, and a second reader's successful attempt to
locate the timeout and retry states without oral setup. A bad card says only
"readable diagram" and "check formatting." A borderline card records the widths but
omits the reader question and candidate identity, so it cannot explain whether the
right page was checked.

Keep source-backed geometry and validation fields mandatory. Lifecycle, retention,
and handoff depth are operational extensions whose value depends on collaboration
scale. Link bulky evidence instead of embedding it. When the artifact migrates from
Markdown to a man page or another text format, carry forward the reader goal,
omission routes, and figure semantics first; those decisions matter more than the
original border characters.

For one disposable local figure, reduce the card to reader question, target surface
and width, relationship and figure grammar, hardest labels, candidate identity, and
verification result. Before accepting any maintained card, give it and the source
copy to a second author and ask them to reconstruct the intended skeleton, run the
declared checks, and answer the reader task without oral setup. Differences in taste
are allowed; missing anchors, changed semantics, or undiscoverable evidence mean the
card is incomplete.

## Worked Example Set

Use examples to expose layout consequences, not to award unexplained good or bad
labels. The examples below hold one reader question constant: "Where can an async
request stop, and where does retry enter the path?" That fixed task makes changes in
geometry and disclosure attributable to layout decisions rather than changed content.
This set teaches flow, exception routing, and constrained disclosure; it does not
stand in for separate tree, dense-matrix, or full-page composition studies.

**Good: a straight main path with one routed exception.**

```text
ASYNC REQUEST

+--------------------------+
| 1. Accept and validate   |
+------------+-------------+
             |
             v
+--------------------------+       timeout
| 2. Call upstream        |------------------> [Retry policy]
+------------+-------------+
             |
             v
+--------------------------+
| 3. Classify result      |
+------------+-------------+
             |
             v
+--------------------------+
| 4. Persist and reply    |
+--------------------------+

Details: retry limits and backoff -> Retry policy appendix
```

This version gives the common case one uninterrupted top-to-bottom scan. The timeout
branch starts at the operation that can time out, and the omission route states
where retry detail lives. Repeated widths and a shared center anchor make later
drift easy to notice. A reader can answer both questions without treating retry as
mandatory.

**Bad: a balanced row that changes the meaning.**

```text
[Accept] -> [Call] -> [Classify] -> [Retry] -> [Persist] -> [Reply]
```

The row looks tidy and fits this shortened sample, but it places retry on the main
path and therefore implies that every request retries. Restoring the real labels
would either exceed a narrow target or force opaque abbreviations. The artifact also
hides the timeout origin and provides no route to omitted policy. Symmetry does not
repair those semantic failures.

**Borderline: a 72-column operational summary.**

```text
+--------------------+
| Accept + validate  |
+---------+----------+
          |
          v
+--------------------+  timeout -> Retry appendix
| Call + classify    |
+---------+----------+
          |
          v
+--------------------+
| Persist + reply    |
+--------------------+
```

This variant is conditionally fit for a familiar on-call audience that needs only
the control path. It preserves timeout placement and the detail route, but combines
operations and removes sequence-specific diagnostics. It is wrong for onboarding or
incident analysis unless adjacent prose restores the lost distinctions. Borderline
therefore means "accepted for a declared audience at a known cost," not "probably
good after adding a warning."

For every normative example, retain the source text and longest labels, run the
ASCII quality validator, measure the longest line, check Markdown fences, and render
on each declared target surface. Also record whether a representative reader
answered the example's stated question. Character, width, and fence results are
deterministic.
Balance, disclosure depth, and comprehension remain editorial observations bounded
by the tested audience and terminal configuration.

Keep these examples as a small regression corpus. A copy change that lengthens
"Call upstream" or a grammar change that moves retry onto the spine must trigger the
same checks even if the surrounding prose is unchanged. Preserve the reader task and
semantic assertions as fixtures; allow the drawing to evolve when a new composition
passes those fixtures more clearly.

Mark retired examples as archival studies with their candidate identity, tested
surfaces, and observation date. They may explain a past failure, but they do not
remain normative after their contract or environment changes.

## Outcome Metrics and Feedback Loops

Measure whether the page helps its declared reader complete a task, not whether the
page merely contains diagrams. Use four evidence families together:

- **Reader outcome:** Can a representative reader locate the main path, explain a
  branch or state, and take the action named in the run card without oral context?
  Record hesitation, wrong turns, requested context, and the final answer. Do not
  convert a small sample into an unsupported success percentage.
- **Mechanical conformance:** Does the candidate contain only allowed characters,
  remain within its hard canvas, close every fence, preserve table shape, avoid tabs
  and trailing whitespace, and end with a newline? These results are reproducible,
  but they prove only the declared contract.
- **Surface portability:** Does every required terminal, Markdown renderer, log
  view, or text export preserve order, alignment, connectors, and readable
  wrapping? A passing source scan cannot substitute for a target-surface
  observation.
- **Maintenance cost:** When labels or sections change, how many anchors, cards, and
  omission routes require repair? Repeated widening, clarification requests, or
  page-wide reflow indicates structural debt even when the current render passes.

Scale the loop to consequence and lifetime. A disposable local figure needs a quick
mechanical scan and an author check against its reader question. A maintained page
also needs target-surface rendering and a second reader who was not involved in the
composition. A high-consequence runbook should use independent task review across
the expected audience and all operational surfaces. The run card states the actual
profile; this reference does not invent universal sample sizes or comprehension
thresholds.

Direct task observation and a small defect log are the default evidence sources.
Surveys can reveal reader perception, support-question logs can reveal recurring
gaps, and diff review can reveal structural drift. Passive telemetry is conditional
on an existing ethical collection system and a question it can actually answer; it
adds privacy and interpretation costs to a plain-text artifact. Triangulate these
signals around a decision instead of averaging unlike evidence into one score.

Use a tiered feedback loop:

1. **After every edit:** Run cheap character, width, whitespace, fence, table, and
   heading checks. Repair mechanical defects before interpreting the layout.
2. **At candidate state:** Freeze copy and geometry, render on declared surfaces,
   and ask the prewritten locate, explain, and act questions. Capture the exact
   candidate identity so results cannot drift to a later revision.
3. **Before acceptance:** Assign each observed defect to an owner and disposition.
   Rerun the affected mechanical and reader checks after correction. A comment with
   no disposition and rerun is not a closed loop.
4. **During maintenance:** Repeat lightweight checks after edits and reopen the full
   review when a target renderer changes, a longest label crosses its budget,
   support questions recur, a source changes materially, or an anchor repair causes
   page-wide reflow.

Periodic review must also challenge the contract itself: confirm that the declared
width, character policy, target surfaces, audience, and reader tasks still match
actual use. Deterministic conformance to a stale run card is not reliable evidence.

A minimal feedback record contains candidate identity, reader task, reader profile,
target surface, observed behavior, mechanical evidence, severity, owner, decision,
and rerun result. Keep deterministic facts separate from editorial interpretation.
For example, "maximum line is 83 bytes under an 84-byte contract" is mechanical;
"the timeout branch competes with the main path" is a reviewer judgment whose
rationale should be retained.

Good evidence says, "An on-call reader found the timeout origin and retry appendix
without prompting; the 72- and 84-column renders passed; no label crossed its shared
card budget." Bad evidence says, "The diagram looks clean and the validator passed,"
because it neither tests the reader task nor names the contract. Borderline evidence
says, "An expert found retry immediately, but a new maintainer followed the branch
backward." That result should trigger a focused test of branch labeling or
placement, not a demand for unspecified additional feedback.

Treat metric confidence per claim. Bytes, widths, delimiters, and table cells are
known directly under the recorded contract. Reader observations are bounded by
familiarity and environment. Ideal disclosure depth and visual balance remain
editorial judgment. External renderer behavior is volatile and must be refreshed
when its implementation changes. Over time, prefer layouts that keep correction
cheap: maintainable geometry makes future clarity improvements possible instead of
turning every copy edit into a full redraw.

## Completeness Checklist

Use this checklist when a reference candidate is ready for acceptance. During
drafting, run the structural and hygiene subset, but allow explicitly marked studies
to remain incomplete. At acceptance, record every item as `pass`, `fail`, or
`not_applicable` with candidate-specific evidence. That state requires a written
boundary and consequence. Unavailable evidence is a failure, not an exception
category.

**Deterministic structure and hygiene gates**

- The reference contains the exact 26 original heading texts in their original
  order, and no added heading changes the section model.
- Every evolved section is longer than its matching archive section and adds useful
  causal, boundary, alternative, example, verification, or uncertainty guidance.
- The packet contains 26 section headings, 260 exact question headings, and 1,560
  mandatory field lines; all 1,560 field values are exact-text unique and remain
  unique after Section or Question context prefixes are stripped and whitespace is
  normalized.
- The reference and packet are ASCII-only, contain no prohibited placeholder terms,
  have no trailing whitespace, and end with a newline.
- Every Markdown fence is closed, every table has a consistent column shape, and
  every width-sensitive example satisfies its declared canvas.
- Repository tests and the focused reference verifier pass against the exact
  accepted candidate. Reports identify counts and failed objects, not only an exit
  status.

**Source and decision gates**

- Every local source path in the source map exists and its claimed contribution was
  checked against the source. Inherited external claims retain an explicit freshness
  boundary when no current lookup was performed.
- The hierarchy states which source governs workflow, page systems, local figures,
  grids, and editorial composition, including how conflicts are resolved.
- The thesis, scoreboard, and decision guide agree on the default sequence: start
  from the reader question, choose a page system and canvas, then compose local
  figures and verify the result.
- Adopt, adapt, and avoid conditions name the consequence of a wrong route and point
  to a more suitable method where possible.
- Numeric or compatibility claims are either supported by retained evidence or
  written as bounded operational defaults rather than universal facts.

**Operational artifact and example gates**

- The run card names a reader goal, target surfaces, canvas, page system, section
  jobs, figure grammar, anchors, label budget, omissions, candidate identity, and
  verification packet, or explains why a reduced small-figure profile is sufficient.
- The worked set contains inspectable good, bad, and borderline artifacts. Each
  diagnosis identifies the causal difference and the reader outcome, not merely a
  quality label.
- Verification covers character policy, width, whitespace, fences, tables, target
  renders, and at least one question-based reader review for maintained candidates.
- The feedback record assigns observed defects, records dispositions, and contains
  rerun evidence after repair. An unassigned comment does not close the loop.

**Editorial and maintenance gates**

- A skeptical whole-file reread found no duplicated generic prose, unsupported
  precision, source-role inflation, or claims that merely sound authoritative.
- The complete packet and reference rereads persisted a review checkpoint at least
  every five sections, so no whole-file judgment depends on unsaved model context.
- The evolved guidance states where defaults work, where they fail, which
  alternatives matter, and what remains judgment or externally volatile.
- A reader unfamiliar with the drafting conversation can locate the main workflow,
  choose a suitable figure family, find verification commands, and route an
  unsuitable task without oral context.
- Adjacent-reference routes name a concrete destination and a trigger. They do not
  send the reader through circular categories such as "use an ASCII reference for
  ASCII work."
- Maintenance triggers cover changed renderers, widening labels, recurring reader
  questions, source updates, and page-wide anchor drift. Accepted evidence is tied
  to the revision it verifies.

A good completion record says which command produced the heading and packet counts,
links the target renders, and records that a named reader task succeeded. A bad
record says only "reviewed" or "looks fine." A borderline record identifies, for
example, an unresolved renderer misalignment with an owner and a planned
discriminating test. The candidate remains failed until the exception is resolved
or the target-surface contract is deliberately changed and reverified.

When a gate fails repeatedly, inspect the reference rather than normalizing the
failure. Recurring table defects may justify stronger automation; repeated confusion
about branches may require a clearer default grammar. Change the gate only with
evidence that the promise itself changed, and retain the prior invariant in the
decision record so a lowered standard cannot masquerade as progress.

## Adjacent Reference Routing

Keep this reference primary when the deliverable must remain legible, copyable,
diffable, and useful as raw fixed-width text without a rendering runtime. Typical
fits include command help, logs, source-controlled runbooks, terminal walkthroughs,
and review notes. The lowest-capability required surface sets the baseline; richer
surfaces may enhance it, but they must not become necessary unless the contract says
so.

Route elsewhere when a different reader action or information topology dominates:

- For an interactive browser explanation with progressive disclosure, responsive
  regions, or linked detail, inspect
  `idiomatic-ref-202607/html_explainer_page_patterns-20260710.md`.
- For a codebase explanation whose main deliverable is an interactive visual
  learning experience, inspect
  `idiomatic-ref-202607/visual_explainer_skill_patterns-20260710.md`.
- For a recommendation, approval memo, or analytical argument where logical
  hierarchy matters more than spatial topology, inspect
  `idiomatic-ref-202607/minto_pyramid_writing_patterns-20260710.md`.
- For an operational product interface with controls, navigation, responsive
  behavior, and accessible interaction states, inspect
  `idiomatic-ref-202607/frontend_design_quality_patterns-20260710.md`.
- For expressive computational visuals whose goal is aesthetic exploration rather
  than terminal explanation, inspect
  `idiomatic-ref-202607/algorithmic_art_generation_patterns-20260710.md`.
- For explorable 3D space, camera behavior, scene state, or React-integrated WebGL,
  inspect
  `idiomatic-ref-202607/threejs_react_visualization_patterns-20260710.md`.

These are current destinations, not automatic transfers. Open the destination and
confirm its scope before rerouting. Use the cheapest discriminating probe: resize an
HTML skeleton, traverse controls by keyboard, render the raw-text fallback, sketch
the dense data region, or test whether the reader's argument still works after all
geometry is removed. Verify the reason for leaving ASCII rather than merely proving
that another technology can render something.

Avoid ASCII as the primary artifact when readers must filter, zoom, disclose details
on demand, use semantic assistive navigation, compare data too dense for the canvas,
observe animation, or explore three-dimensional relationships. A small terminal
summary may remain useful for logs or failure recovery, but only if it has a
complete reader task and does not silently omit safety-critical state.

For example, a deployment flow belongs here when reviewers must inspect it in a pull
request and paste it into an incident channel. The same domain routes to an HTML
explainer when learners must reveal per-stage evidence interactively. It routes to
Minto guidance when the real task is persuading an approver that a staged rollout is
preferable. A mixed case may use an ASCII operational spine plus a linked browser
explorer; the spine remains authoritative for incident order, while the explorer
owns optional detail.

Every hybrid needs an authority and degradation contract. Name which artifact owns
volatile labels, what semantics are duplicated, how updates synchronize, and what a
reader can still accomplish when the rich surface is unavailable. Transfer reader
questions, section jobs, omission routes, and verified terminology to the new
medium, but redesign fixed-width geometry for its capabilities. Good routing changes
the representation while preserving intent, traceability, and known failure
boundaries.

## Workload Model

Treat the workload as a visual artifact with source text, geometry, reader tasks,
and verification evidence, not as a prose summary measured by paragraph count.
Choose the smallest unit that has one coherent reader journey, one canvas contract,
one revision owner, and one acceptance packet. A unit is genuinely bounded when it
can fail acceptance without making unrelated artifacts indeterminate.

Use these workload profiles:

- **Local figure:** One reader question, one primary grammar, one width contract,
  and nearby prose that supplies context. Examples include a four-state lifecycle, a
  compact call sequence, or a small comparison. Verify the figure in its final
  surrounding text because indentation and wrapping can change there.
- **Composed terminal page:** One main reader journey expressed through several
  section jobs and local figures under a shared grid and vocabulary. Examples include
  an incident walkthrough, deployment review, or architecture orientation page. The
  figures may use different grammars if their transitions and reading order remain
  clear.
- **Artifact suite:** An overview plus independently owned pages when audiences,
  canvases, update cadence, or acceptance criteria diverge. Share terminology and
  visual vocabulary, but give every page its own reader goal, run card, and evidence.
  The overview owns navigation and cross-page relationships, not duplicated detail.

Before choosing a profile, run a capacity probe:

1. Collect representative source copy, including the longest important labels and
   the densest relationship set. Do not estimate with convenient placeholder words.
2. Set the narrowest required canvas and sketch the page skeleton without decorative
   polish. Place section jobs, main-path anchors, gutters, and omission routes.
3. Populate the hardest local region. Record every semantic abbreviation, wrap,
   crossover, or branch relocation needed to fit it.
4. Test the global reading path independently. A locally tidy figure can still force
   readers to jump backward across the page.
5. Run the quick mechanical checks and ask the main reader question. Keep the
   profile only if progressive disclosure preserves the answer without hidden
   context.

Split the work when independent audiences need different starting points, required
surfaces impose incompatible canvases, unrelated owners must accept changes, the
main path repeatedly crosses section boundaries, or compression removes essential
labels and relationships. Route to a richer medium when filtering, zoom, responsive
interaction, animation, semantic navigation, or data density is the actual pressure.

Do not split merely because one page uses a flow and a state figure, or because a
fixed box count was exceeded. Conversely, do not retain a giant page because every
piece belongs to the same product. If each proposed child needs large amounts of
duplicated context, revise the boundary or retain a concise overview that explains
their relationship.

A good local workload is a retry lifecycle that fits its true labels and can be
verified as one state figure. A good page workload is the async request walkthrough:
one operational journey, several distinct section jobs, one 84-column contract, and
one reader-task packet. A good suite workload is a multi-team platform guide with a
shared overview and separately accepted service pages. A bad workload compresses all
service ownership, runtime flow, and incident recovery into one screenful because
they mention the same platform. A borderline page should be split only after the
narrow-canvas probe shows that progressive disclosure cannot preserve its main task.

Verification effort belongs in the estimate. Record the chosen profile, probe
candidate, narrowest canvas, sampled labels, observed pressure, split rationale,
per-unit acceptance map, and suite navigation check. Revisit the boundary when label
growth, renderer changes, repeated clarification, or page-wide reflow indicates that
the original cohesion has changed. Recombination is also valid when fragmented pages
accumulate duplicated context, but weigh that gain against stable links, ownership,
and reader memory before restructuring.

## Reliability Target

Reliability means that this reference repeatedly preserves its evidence boundaries,
routes a task under declared conditions, produces an artifact that survives its target
surfaces, and explains how to recover when a check fails. It does not mean that every
reader in every terminal will interpret one page identically.

Use five target layers:

- **Source integrity invariant:** Every material recommendation identifies whether it
  comes from inspected local evidence, inherited external evidence, or explicit
  synthesis. Referenced local paths resolve, and unrefreshed external claims retain
  their freshness boundary. An unlabelled material claim blocks acceptance.
- **Artifact conformance invariant:** Heading order, packet counts, exact field-value
  uniqueness, uniqueness after context-prefix stripping and whitespace normalization,
  encoding, placeholders, whitespace, fences, tables, and declared width contracts
  pass for the exact candidate. A malformed or stale artifact does not receive a
  tolerance percentage.
- **Decision fitness observation:** Representative tasks exercise adopt, adapt, avoid,
  and adjacent routes. Reviewers record the expected decision, actual decision,
  rationale, and severity. Any predeclared critical misroute blocks acceptance even
  when most sampled tasks route correctly.
- **Reader and surface observation:** The candidate renders on every required surface,
  and representative readers complete its locate, explain, and act tasks. Report the
  audience and environment; do not turn a small convenience sample into a universal
  comprehension rate.
- **Recovery invariant:** Every blocking failure names the stopped work, corrective
  action, owner or escalation route, and checks to rerun. Avoid guidance points to a
  concrete adjacent method or an honest stop condition.

Do not use an unexplained target such as "18 of 20 decisions." A numeric sample target
is defensible only when a maintained evaluation protocol defines the task population,
sampling method, severity model, and consequence of failure. Otherwise, predeclare
the highest-risk cases, test them directly, and report observations without false
statistical authority.

Scale evidence to the workload. A local disposable figure still obeys character,
width, and semantic-connector invariants, but may use an author task check. A
maintained page adds independent reader review and all target renders. A
high-consequence runbook uses broader representative task coverage, explicit critical
failures, and retained recovery rehearsal. Volatile renderers and external claims need
freshness triggers; stable geometry needs regression fixtures.

A good target says, "The accepted candidate has no missing source labels or structural
defects; both required terminal renders preserve the timeout branch; an on-call reader
located the retry route unaided; the one observed wording hesitation was corrected and
the task rerun." A bad target says, "Ninety percent reliable" without a denominator,
task set, or severity model. A borderline result says that an expert succeeded while a
new maintainer reversed a branch; narrow the audience claim or revise and retest rather
than averaging the disagreement into a pass.

Bind each reliability report to candidate identity and retain: claim, target layer,
task, audience, surface, date, result, severity, owner, disposition, and rerun result.
A material label, canvas, renderer, source, or routing change expires affected evidence.
Review the declared contracts as well as conformance to them; a perfect check against
the wrong canvas is still a design failure.

Reliability is designed in before final review. Stable anchors localize reflow, bounded
vocabulary reduces interpretation drift, early longest-label probes expose capacity,
and run-card identity prevents stale evidence. These controls should grow with
consequence, volatility, and reuse. Fast, localized diagnosis and recovery are part of
the target because copy, sources, and rendering surfaces will continue to change.

## Failure Mode Table

Classify a failure by its earliest controllable cause, while retaining the downstream
reader-visible symptom. First stop propagation and preserve the exact failing
candidate. Then test the cheapest plausible causes, repair the smallest responsible
layer, and rerun both the failed gate and any downstream evidence it invalidated.

- **Source-boundary drift:** A local file changed, inherited external evidence aged,
  or synthesis was restated as fact. Contain by blocking reuse of affected claims.
  Reinspect the source, restore evidence labels, revise dependent guidance, and rerun
  source-map and skeptical-reread checks.
- **Wrong page or figure grammar:** The artifact is tidy but cannot answer the reader
  question, such as a sequence rendered as an unordered grid. Return to the reader
  task and choose the grammar that exposes order, state, hierarchy, comparison, or
  relationship. Rerun the task with labels temporarily removed to test structure.
- **Label or canvas overflow:** Real copy wraps, clips, or forces opaque abbreviation.
  Freeze the longest labels and declared surface, then shorten without semantic loss,
  wrap deliberately, widen within contract, disclose detail elsewhere, or split the
  artifact. Verify source width and every target render.
- **Grid drift or connector ambiguity:** Repeated cards lose shared anchors, arrows
  cross content, or a branch appears to join the wrong state. Stop local nudging,
  reconstruct the governing grid, and reattach connectors from named semantic points.
  Ask a reader to trace direction and branch ownership without narration.
- **Character or whitespace leakage:** Unicode borders, tabs, trailing spaces, or
  mixed line endings make alignment environment-dependent. Inspect raw bytes, replace
  with the declared ASCII vocabulary, normalize indentation and line endings, and
  rerun the character and whitespace gates.
- **Markdown structure breakage:** An unclosed fence captures prose, a table row has
  the wrong number of cells, or a changed heading alters section order. Preserve the
  content, repair delimiters or shape, and rerun focused structure checks plus the
  repository verifier before reviewing appearance.
- **Target-render mismatch:** Source dimensions pass but a required destination wraps,
  collapses spaces, substitutes a proportional font, or strips a code block. Confirm
  the destination contract, reproduce with the exact copied artifact, and either
  adapt the representation or route that surface elsewhere. A screenshot supports
  diagnosis but does not replace the raw-text deliverable.
- **Reader-comprehension failure:** Mechanical checks pass while readers reverse a
  branch, miss an omission route, or cannot identify the next action. Preserve the
  observation, test competing causes such as label wording, emphasis, order, and
  grammar, then rerun the same question with a comparable reader.
- **Stale route or evidence packet:** The page points to moved detail or a validator
  result belongs to an earlier revision. Block acceptance, repair the route, bind all
  evidence to candidate identity, and exercise the destination rather than checking
  only that text resembles a path.
- **Unbounded variant search:** Alternative layouts multiply without a stable reader
  task or acceptance contract. Stop generation, restore the run card, compare only
  variants that test a named tradeoff, and retain the reason for selection or
  rejection.

If the cause is unknown, say so and define a discriminating probe. For a clipped label,
compare raw bytes, measured width, and target render before blaming copy or renderer.
High certainty that a symptom exists does not imply high certainty about its cause;
contain a consequential defect while investigation continues.

A good diagnosis records: "Signal: one 78-byte line under a 72-column contract;
proposed cause: the longest source label was added after grid freeze; falsifier: the
same bytes fit when the card is removed; repair: stack the peer cards without changing
the label; recovery: width, target-copy, and comparison-reader checks pass." A bad
diagnosis says "renderer problem," widens the page, and keeps no failing copy. A
borderline diagnosis says the source measures correctly but one target clips; it
holds acceptance and compares exact bytes, font mode, container width, and a minimal
copy before assigning the cause. Use qualitative consequence classes unless retained
history supports a calibrated severity model.

Exercise the control chain with focused mutations drawn from real escapes: insert a
tab, substitute a Unicode border, lengthen the hardest label, reverse one arrow, break
a fence, or stale an omission route. Confirm that the intended detector fires, then
remove the mutation and verify recovery. Do not claim broader coverage than the
specific mutation demonstrates.

Retain candidate-state, recurring, and high-consequence failures with signal, proposed
cause, alternatives considered, consequence, owner, repair, rerun, and reference
change. Cascades matter: source drift can lengthen copy, trigger reflow, obscure a
branch, and invalidate prior reader evidence. Repeated downstream repairs are a signal
to add or strengthen an earlier contract, pressure probe, or automated gate.

## Retry Backpressure Guidance

Retry only after recording the failed candidate, observable signal, provisional failure
class, changed condition, expected result, and checks that the change may invalidate.
An ordinary retry must be an experiment. Repeating an attempt with unchanged inputs is
allowed only for a named transient mechanism and a bounded attempt count.

Use this failure-to-action ladder:

1. **Transient process failure:** Preserve command output and retry once without
   changing the artifact when the mechanism is credibly temporary, such as an
   interrupted local process. A second identical failure changes the classification
   from transient to undiagnosed and stops automatic repetition.
2. **Stale evidence:** Refresh only the affected source or render evidence, record its
   new identity and date, and reevaluate dependent claims. Escalate or narrow the
   claim when the authoritative evidence remains unavailable or contradictory.
3. **Missing context:** Load the smallest source, label set, target constraint, or
   reader task that can discriminate the next decision. Do not answer uncertainty
   with an unstructured context dump.
4. **Local conformance defect:** Preserve the failing candidate, patch the responsible
   character, width, whitespace, fence, table, or heading layer, and rerun the failed
   gate. Expand the rerun to renders or reader tasks if order, emphasis, or meaning
   changed.
5. **Semantic or layout defect:** Return to the reader question and run card. Compare
   bounded variants only when each tests a named tradeoff under fixed acceptance
   criteria. Retain why a candidate was selected or rejected.
6. **True contradiction:** Stop dependent writing. Record the conflicting claims,
   authority, scope, and consequence; then seek owner judgment or a narrower
   source-specific rule. Do not blend contradictions into vague compromise prose.
7. **Incompatible medium or capacity:** Narrow the artifact, split it with an overview,
   or use the adjacent-reference route. More generations cannot make required
   interaction, density, or 3D behavior fit a static terminal page.
8. **Ownership conflict:** Stop writes to the contested file, preserve both candidate
   identities, and resolve ownership before editing. Never use destructive recovery
   to erase another worker's changes.

When a new candidate regresses, restore the last accepted candidate before attempting
a broader redesign. Defer a volatile external claim only after narrowing dependent
guidance and recording the refresh trigger. Accept a known limitation only when it is
outside the declared contract, has an explicit consequence and route, and does not
hide action-critical information.

Apply backpressure to dependent work, not automatically to every independent task.
When source coverage, packet rationale, candidate verification, or ownership is red,
do not build later sections on that premise. Independent files can proceed only when
their inputs and ownership do not intersect the failure.

Persist state frequently. Save each complete ten-question packet section before its
matching reference rewrite, save that rewrite before moving on, and run a focused
heading and placeholder check. Journal at least every three sections and at Red,
Green, and Refactor transitions. During complete packet and reference rereads,
persist a review checkpoint at least every five sections. Before a broad rewrite or
handoff, reread the current specification, latest journal checkpoint, and exact
candidate rather than relying on conversation memory.

A good retry record says: "The 72-column candidate failed at 76 bytes; the longest
label was wrapped without changing its term; the width gate and two target renders
now pass; the branch-reading task was rerun because line placement changed." A bad
retry says: "Generated again and this version looks better." A borderline renderer
failure uses a minimal copied probe to determine whether the cause is a transient
environment issue or a persistent surface incompatibility before changing the page.

Close recovery only when the failed signal no longer reproduces, the causal hypothesis
is supported or responsibly narrowed, and every invalidated downstream check has fresh
evidence. Retain blocking, recurring, externally volatile, and high-consequence retry
records with pre- and post-candidate identity. Backpressure limits not just attempts,
but also the amount of downstream state built on an unresolved premise.

## Observability Checklist

Observability should let a later reviewer reconstruct why a candidate was accepted,
rejected, or routed elsewhere without replaying a transcript. Retain events that change
source authority, geometry, acceptance, recovery, ownership, or future maintenance.
Everything else is optional diagnostic detail.

For each maintained candidate, record:

- candidate identity, event type, and exact reference or artifact path;
- reader goal, page profile, canvas contract, and required target surfaces;
- local sources loaded, material sources skipped, and the reason for each relevant
  omission;
- inherited external claims used, their freshness boundary, and any explicit
  synthesis that governs a decision;
- exact verification commands, environment assumptions, summarized results, and
  links to retained raw output when a material failure needs deeper diagnosis;
- target-surface observations and the exact reader questions asked;
- reviewer decision, severity of each defect, owner, disposition, and rerun result;
- unresolved uncertainty, affected claim, temporary containment, and next refresh
  trigger.
- sensitive detail intentionally redacted, why it was removed, and which decision can
  still be reconstructed without it.

Use candidate identity as the join key across the run card, progress journal, command
report, reader notes, and source manifest. Give each fact one authoritative home and
link it elsewhere. This avoids both a monolithic log and several conflicting copies of
the same decision.

Scale the record to the workflow. A disposable sketch can retain its reader question,
canvas, and quick check result. A candidate page adds full source, command, render,
and reader evidence. An accepted page preserves the decision and refresh triggers.
Maintenance events record changed inputs, invalidated evidence, and fresh reruns.
Distributed or long-running work also needs owner, durable checkpoint, and handoff
state because context loss is part of the operational risk.

Do not collect latency percentiles merely because they sound quantitative. Measure
runtime, reviewer time, or tool-call volume only when a repeated workflow has a
defined start, end, population, and decision that the measurement can change. Report
small observations directly instead of presenting unsupported percentiles. Expanded
traces are appropriate for a named renderer or tool investigation, but summarize the
retained finding after diagnosis and handle sensitive source content deliberately.

Classify each retained entry as a mechanical result, observed behavior, reviewer
inference, or unresolved uncertainty. Preserve disagreement when reviewers interpret
the same mechanical result differently instead of overwriting one judgment.

A good record says: "Candidate `async-page-c4`, hard width 84, local source set A-E,
validator command recorded, terminal and Markdown copies inspected, retry-route task
passed, one disclosure-depth concern assigned, rerun pending after wording repair."
A noisy record stores every shell line and conversation message but omits the accepted
candidate. An under-specified record says "all checks passed" without command, surface,
reader task, or revision; adding more unrelated output does not repair it.

Test observability through reconstruction. Give a second reviewer the evidence index
without oral setup and ask them to identify governing sources, rerun mechanical checks,
locate render evidence, repeat the reader task, explain unresolved risk, and name the
next trigger. Check that every link resolves. If a volatile external surface changed,
record that reproduction limit rather than rewriting the old observation as current.

Periodically prune fields that never affect decisions and add fields only after a
recurring or consequential failure shows missing context. The goal is causal
continuity across revisions and owners, not form completion. A compact record that
supports recovery is more observable than a comprehensive dump whose decisive signal
cannot be found.

## Performance Verification Method

Verify the claim the layout actually makes. ASCII performance may mean fitting a
canvas, surviving a renderer, helping a reader reach the right action, or reducing the
effort to repair future copy. Do not collapse those outcomes into one speed score.

Route claims to evidence as follows:

- A **character or width claim** needs deterministic source checks plus copies on the
  declared target surfaces.
- A **reader-effectiveness claim** needs a prewritten locate, explain, compare, or act
  task with allowed context and assistance recorded.
- A **comparative speed claim** needs a credible baseline, comparable inputs and
  readers, stable event boundaries, enough repeated observations for the reported
  summary, and error or assistance data alongside time.
- A **maintenance-effort claim** needs a realistic change probe, such as lengthening
  the hardest label, adding one state, or moving an omission route, followed by the
  complete repair and rerun scope.
- A **workflow-cost claim** may include source count, tool calls, reviewer effort, or
  wall time only when those measures have defined start and stop events and can change
  a decision.

Use this staged method:

1. State the perspective, task, candidate, target surface, consequence, and claim.
   Decide before testing what result would pass, fail, or remain inconclusive.
2. Preserve the baseline when one exists. If no credible baseline exists, test fitness
   without claiming improvement.
3. Run character, whitespace, structure, and declared-width gates. Stop if mechanics
   fail; reader timing on a malformed candidate is not interpretable.
4. Copy the exact candidate to every required surface and record wrapping, alignment,
   connector, and omission-route behavior.
5. Run the reader or maintenance task without author coaching. Record answer, wrong
   turns, requested context, assistance, and elapsed interval only when time matters.
6. Compare only observations with compatible task wording, source copy, width,
   environment, familiarity, and event boundaries. Note task order, warmed caches, or
   other major confounders; alternate candidate order when feasible.
7. Retain measured facts separately from interpretation and bind all evidence to the
   candidate. For timing, record clock resolution and exact start and stop events.
   State which audiences, surfaces, or workloads remain untested.

Do not report p50, p95, or p99 values from a convenience handful of reviews. A
percentile is warranted only for a repeated workflow with a documented population,
sampling method, and sufficient observations at the claimed tail. Otherwise report
the individual observations and their limits. Timing precision must not exceed the
protocol's control over reader familiarity, environment latency, task order, and
measurement boundaries.

A good record says: "Candidate C4 at 84 columns; a new on-call reader, using only the
page, located the timeout origin and retry route correctly, requested no assistance,
and initially followed one side note before returning to the main path." Add elapsed
time only if the operational contract cares about it. A bad record says, "The diagram
is 40 percent faster" after one coached comparison against different copy. An
inconclusive record says the candidate appeared quicker but the baseline used expert
terminology and a wider terminal; the next test must equalize those variables.

Pass when the declared mechanical and task outcomes hold under the tested contract and
no critical error is observed. Fail when the artifact misroutes the reader, loses
required state, breaks a target surface, or requires hidden author context. Mark a
result inconclusive when evidence cannot distinguish layout effect from a material
confounder; narrow the claim or run the discriminating test.

Evaluate lifecycle cost, not only first-draft speed. A compact page may be quick to
write yet expensive to understand, localize, or repair. Use early change simulations,
then replace those assumptions with actual defect and reflow records as the artifact
ages. The useful objective is the cost of reaching and preserving a correct decision,
including author, reviewer, reader, and maintainer work.

## Scale Boundary Statement

ASCII layout stops being sufficient as a primary artifact when compression,
coordination, volatility, or verification destroys a required reader relationship.
Multiple systems, owners, or pages are pressure signals, not universal rejection
thresholds. Test the dimension that is actually growing:

- **Reader scale:** Different audiences require incompatible starting points,
  terminology, detail, or actions. Split audience-specific pages and retain a shared
  overview only for relationships everyone must understand.
- **Canvas scale:** The longest labels or densest region cannot fit the narrowest
  required surface without ambiguous abbreviation, crossings, or lost state. Split,
  disclose detail, or route to a richer medium.
- **Relationship scale:** The global path cannot be traced because local figures need
  repeated cross-page jumps or an unreadable number of edges. Keep a bounded topology
  overview and give detailed relationships an owned destination.
- **Source scale:** Discovery is open-ended, authority is unranked, or the selected
  evidence cannot close the page's claims. Narrow with a source or dependency graph,
  rank governing sources, and stop composition until the evidence boundary is clear.
- **Ownership scale:** Independent teams can accept local pages, but no one owns shared
  terminology, cross-page edges, or integration verification. Assign those contracts
  explicitly before parallel work continues.
- **Volatility scale:** Live values, rapidly changing topology, filtering, zoom, or
  realtime state exceed static text's freshness model. Route live state to operational
  or interactive tooling and keep ASCII for stable guidance or resilient fallback.
- **Verification scale:** A single evidence packet cannot cover divergent surfaces,
  readers, release cadence, and consequence. Give each independently accepted page a
  run card and retain a suite-level navigation and vocabulary gate.

The default adaptation is an overview plus owned detail pages. The overview owns
durable topology, shared vocabulary, reader entry points, and routes. Child pages own
volatile facts and local procedures. Do not copy detailed state into the overview;
otherwise it becomes another stale source of truth. Give relationship edges an owner
as deliberately as component pages.

When a suite becomes difficult to discover, a generated index can list owned pages,
audiences, and routes without copying their volatile content. Its generation source
and link checks become part of suite acceptance; an index does not repair unclear
decomposition or orphaned relationships.

One page can still cover a broad system when all readers need the same overview,
terminology is stable, key edges survive the narrowest canvas, and one verification
packet can validate the result. Different local grammars or several components do not
force a split by themselves. Conversely, mentioning one product does not justify a
single page when readers, surfaces, and actions are independent.

High production volume does not by itself disqualify ASCII. A static runbook may be
more valuable at scale because it works during dashboard or network failure. It is
not, however, an appropriate live source for current traffic, health, or rapidly
changing dependencies. State that degradation contract: what the text still enables
when rich tooling is unavailable, and which facts must be refreshed elsewhere.

Before scaling, probe the hardest label, densest edge set, narrowest surface, source
closure, cross-owner change, and most consequential reader task. For a suite, test the
overview's global journey separately from each child page, then follow every route and
check shared terminology. Retest after material localization, renderer, audience,
source, or ownership changes.

Record expected terminology growth, localization, audience change, and renderer
diversity qualitatively. Do not invent a numeric capacity buffer. Keep overview and
child boundaries reversible so observed growth can trigger evidence-based extraction
or recombination.

A service map may remain one overview even when it spans several systems. A multi-team
platform guide usually needs that overview plus independently accepted service pages.
A live dependency explorer with filtering and zoom should use an interactive medium,
with an ASCII incident summary only if it remains operationally complete. A borderline
page is not split on intuition alone; probe the exact relationship most likely to
disappear under compression and choose the reversible response.

Under distributed work, keep one writer per file, checkpoint durable state frequently,
and prohibit overlapping rewrites without an explicit reconciliation owner. Under
long-running work, context drift is a reliability failure: reread the specification,
journal, and candidate before resuming. The scalable unit is a page together with its
authority, routes, tests, ownership, and recovery contract.

## Future Refresh Search Queries

These are future discovery prompts, not evidence. They were not executed during this
no-browse evolution. A maintainer must inspect each result, identify authority and
version, reproduce material behavior where possible, and reconcile the affected claim
before changing guidance.

Use this refresh order: compare the local corpus or tool history, open a known direct
primary source, run targeted discovery only for missing evidence, probe the exact
artifact behavior, then update synthesis and regression evidence together.

Start with the trigger and current claim, then use the narrowest relevant prompt:

- **Fenced-code contract changed:**
  `CommonMark specification fenced code blocks indentation whitespace current`
  Prefer the current specification and record the exact rule that affects raw layout.
- **A required Markdown surface wraps or collapses content:**
  `<renderer name> official documentation release notes code block whitespace wrapping`
  Confirm the deployed version and copy the exact candidate into that surface.
- **Terminal alignment differs across environments:**
  `<terminal name and version> documentation tab width monospace character width`
  Test raw bytes, configured font, tab policy, and the declared ASCII-only vocabulary.
- **The bundled validator changes behavior:**
  `check_ascii_diagram_quality max-width editorial changelog repository history`
  Inspect local tool history and tests before searching secondary descriptions.
- **Accessibility requirements expand:**
  `official accessibility guidance text diagrams reading order alternatives`
  Determine whether the primary source governs terminal text, web rendering, or a
  different medium; do not transfer requirements silently across surfaces.
- **A renderer-specific defect is suspected:**
  `<renderer version> code block alignment issue spaces wrapping`
  Treat issue reports as leads. Reproduce the symptom and look for an official fix or
  release note before making the report normative.
- **Existing external evidence is stale:**
  `<known primary source title> current specification release notes migration`
  Check the direct source first, then use terminology-neutral discovery if authority
  or naming may have changed.
- **A new pattern example is proposed:**
  `<diagram grammar> plain text accessibility width verified example`
  Use examples to discover alternatives, not to outrank the local canonical workflow.

Avoid searches such as `ascii diagram layout best practices` or `best GitHub ASCII
examples` as final research methods. They do not identify the reader task, target
surface, governing authority, version, or failure being investigated. If a broad
query is needed to learn changed terminology, broaden one dimension at a time and
record which term unlocked the relevant primary source.

For every material refresh, retain a compact ledger entry containing trigger, current
claim, query or direct source, source authority, version or date, applicability,
conflict, artifact probe, and disposition. Mark candidates as `discovered`,
`inspected`, `reproduced`, `reconciled`, or `rejected`. Search-result rank and repeated
secondary summaries do not advance that state.

Stop when the affected claim is resolved under the declared surface and uncertainty
is either removed or bounded. Update source mapping, guidance, examples, and regression
fixtures together. Retire a query when its authority disappears or terminology changes,
but preserve the decision so future maintainers understand why the inherited prompt
should no longer guide discovery.

Prefer event-driven refresh after a failed regression, relevant release, new surface,
or stale material claim. Use bounded periodic checks only for external surfaces the
workflow actively depends on; calendar churn is not evidence that guidance changed.

## Evidence Boundary Notes

- `local_corpus_sourced_fact`: A claim directly supported by an inspected local source
  path and relevant span. The label does not make the claim universal; retain the
  source's audience, surface, and version boundary.
- `external_research_sourced_fact`: A claim tied to an inspected public primary source.
  Record the checked date, version or section, supported wording, and applicability.
- `external_mapping_unrefreshed_note`: An inherited public URL or historical source
  role that was not inspected in the current no-browse pass. It is a future refresh
  target and supports no present-tense content claim.
- `combined_evidence_inference_note`: A recommendation synthesized from multiple
  sources, artifact experience, or systems judgment. State decisive assumptions,
  counterexamples, and the condition that would change the recommendation.
- `artifact_observation`: Behavior directly observed for a named candidate under a
  recorded command, canvas, renderer, terminal, or reader task. This supports a claim
  about those tested conditions, not a universal renderer or comprehension rule.
- `unresolved_evidence_uncertainty`: A material conflict, missing source, volatile
  behavior, or untested population that prevents a stronger conclusion. Name the
  affected decision, containment, owner or route, and discriminating next check.

Classify the smallest material claim, not an entire paragraph by convenience. Split a
sentence when one clause is locally sourced, another is inherited external evidence,
and a third is synthesis. A source path proves that evidence exists; it does not prove
that the source entails the wording, applies to the target surface, or remains fresh.

Use explicit labels for defaults, rejection rules, numeric statements, compatibility
claims, volatile behavior, disputed guidance, and other decisions whose provenance
changes application. Homogeneous descriptive passages can use a section-level source
frame to avoid tag noise. Keep detailed spans, freshness, conflicts, and dependencies
in the source map or material-claim ledger so normal reading and skeptical audit both
remain practical.

For example, the local corpus directly supports choosing a page system before local
figures and validating ASCII width. The `draft` to `candidate` run-card lifecycle is
an operational synthesis added here. A successful 84-column terminal copy is an
artifact observation bound to that candidate and environment. A statement that all
Markdown renderers preserve the same spacing would be unsupported unless the declared
surfaces were tested or authoritative current evidence established that scope.

Audit every decision-governing claim by asking:

1. Is the claim phrased no more strongly than its source or observation supports?
2. Does the authority govern this audience, medium, version, and consequence?
3. Is freshness stated when the evidence can change?
4. Are conflicts exposed rather than blended into authoritative-sounding synthesis?
5. Can a source or render change identify the dependent recommendation, example, and
   verification gate that must be revisited?

Provenance, confidence, and applicability are independent. A local fact may be highly
certain but narrow; a synthesis may be useful while remaining judgment; an external
specification may be authoritative but stale for a deployed renderer. Describe those
limits qualitatively instead of inventing confidence scores.

Maintain evidence boundaries as change infrastructure. When a source changes or a
target render fails, update affected claims, examples, search prompts, reliability
evidence, and regression fixtures together. This makes disagreement productive:
reviewers can challenge source authority, inference quality, or applicability without
discarding the parts of the guidance that remain supported.
