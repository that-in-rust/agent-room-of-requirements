## Section 001: Ascii Diagram Layout Patterns
### Question 01: What decision does this reference help make?
- **current_section_observation:** The title identifies ASCII layouts but does not state the medium, page-system, or diagram-choice decisions readers must make.
- **supporting_reason:** Decision framing prevents authors from drawing boxes before choosing reading order, width budget, and explanatory purpose.
- **counterargument_or_limit:** A single tiny figure may not need a full terminal-page system or editorial outline.
- **assumptions_and_boundaries:** The guidance applies when output must remain intelligible as raw monospaced ASCII after copy-paste.
- **revision_decision:** Add an opening that separates medium choice, page composition, local figure choice, and verification.
- **additional_insight_to_add:** State that page architecture precedes diagram grammar because scroll order controls how readers construct the model.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** No opening default currently directs the author toward vertical composition or a stable canvas.
- **supporting_reason:** An 84-column, top-down page with narrow prose and one visual job per section fits most terminal explainers.
- **counterargument_or_limit:** Compact terminals favor 72 columns, while comparison-heavy pages may legitimately require 96 columns.
- **assumptions_and_boundaries:** Choose one declared preset and keep every line within it rather than mixing local widths.
- **revision_decision:** Recommend outline, preset, anchors, modules, local figures, prose tightening, and full-scroll review in sequence.
- **additional_insight_to_add:** Explain that height is cheap in terminals, so vertical splitting is the primary remedy for cognitive overload.
### Question 03: When does the default work well?
- **current_section_observation:** The title does not identify strong-fit outputs such as raw Markdown, design notes, or terminal walkthroughs.
- **supporting_reason:** Plain ASCII excels when portability, source readability, copy-paste stability, and linear teaching matter more than visual polish.
- **counterargument_or_limit:** Rich spatial topology can become harder to parse when forced into a narrow monospaced canvas.
- **assumptions_and_boundaries:** The explanation can be decomposed into screenfuls with clear reading direction and limited primary nodes.
- **revision_decision:** Name architecture maps, flows, sequences, trees, comparisons, and long walkthrough pages as direct fits.
- **additional_insight_to_add:** Include commit messages and code-review notes as small-format cases where raw-text resilience is especially valuable.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The title lacks an exit condition for dense graphs, curves, freeform geometry, or screenshot-level visual polish.
- **supporting_reason:** Routing early prevents unreadable connector crossings and excessive width from masquerading as terminal sophistication.
- **counterargument_or_limit:** A simplified ASCII overview may still complement a richer diagram used for detailed inspection.
- **assumptions_and_boundaries:** ASCII becomes secondary when spatial precision or interactive exploration carries essential meaning.
- **revision_decision:** Add avoid and companion boundaries for Mermaid, HTML, image, and graph-visualization outputs.
- **additional_insight_to_add:** Distinguish a deliberate abstraction from information loss by stating what the ASCII overview intentionally omits.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The title does not compare ASCII with prose-only, Markdown tables, Mermaid, HTML, or rendered images.
- **supporting_reason:** Alternatives optimize different properties: portability, semantic structure, automation, spatial freedom, styling, or interaction.
- **counterargument_or_limit:** Medium comparisons can distract from the requested deliverable when the user explicitly requires plain text.
- **assumptions_and_boundaries:** Compare formats only when the medium is undecided or ASCII cannot preserve a required relationship.
- **revision_decision:** Add a concise routing principle and defer a fuller matrix to the decision and adjacent-reference sections.
- **additional_insight_to_add:** A hybrid can pair a small ASCII orientation map with a richer artifact, provided each has a distinct job.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** No opening warning covers Unicode, tabs, trailing spaces, line wrapping, drifting panels, or overloaded figures.
- **supporting_reason:** These defects often appear only after copy-paste or narrower rendering, where alignment and meaning collapse together.
- **counterargument_or_limit:** Some controlled environments can render Unicode box-drawing reliably, but that violates this reference's portability contract.
- **assumptions_and_boundaries:** Strict ASCII, spaces-only alignment, and a tested width are required for the default profile.
- **revision_decision:** Surface portability, width, connector, label, and page-density traps before pattern selection.
- **additional_insight_to_add:** Warn that a box containing prose usually indicates the explanation and diagram zones were never separated.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** The title provides no contrast between a composed page and decorative ASCII art.
- **supporting_reason:** A good top-down flow, a wrapped all-in-one map, and a bounded hybrid make quality differences concrete.
- **counterargument_or_limit:** One example cannot represent every valid page system or terminal width.
- **assumptions_and_boundaries:** Judge examples by stated purpose, raw-text readability, and width compliance rather than ornament.
- **revision_decision:** Add compact orientation examples here and reserve full cases for the worked-example section.
- **additional_insight_to_add:** Use the same system explanation across examples so medium and layout choices, not subject matter, drive comparison.
### Question 08: How can the important claims be verified?
- **current_section_observation:** The title does not mention validator, plain-text inspection, narrow-width review, or reader-path testing.
- **supporting_reason:** Automated ASCII, tab, whitespace, and width checks complement human review of reading order and semantic clarity.
- **counterargument_or_limit:** A validator cannot determine whether the chosen figure type matches the reader's actual question.
- **assumptions_and_boundaries:** Mechanical checks gate portability; reader review owns explanation quality and pattern fit.
- **revision_decision:** Introduce dual verification and reference the bundled editorial validator without claiming it proves comprehension.
- **additional_insight_to_add:** Require inspection outside syntax highlighting because styling can hide weak raw-text hierarchy.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The title carries no boundary between source-backed grid rules and editorial choices for a particular audience.
- **supporting_reason:** Local sources explicitly support ASCII-only output, width presets, vertical scrolling, pattern selection, and validator use.
- **counterargument_or_limit:** Optimal width, section rhythm, labels, and level of detail remain audience- and context-dependent.
- **assumptions_and_boundaries:** Treat presets as defaults tested against the target surface, not universal readability constants.
- **revision_decision:** Add evidence labels and make local design choices reversible through plain-text review.
- **additional_insight_to_add:** Reader confusion is useful evidence even when every mechanical layout check passes.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The title does not explain how stable grids improve maintenance, diffs, or collaborative editing.
- **supporting_reason:** Repeated anchors and narrow modules localize edits, reduce alignment churn, and make raw diffs easier to understand.
- **counterargument_or_limit:** Overrigid grids can make distinct ideas look falsely equivalent or prevent necessary emphasis.
- **assumptions_and_boundaries:** Repetition should encode peer relationships; deliberate asymmetry needs an explanatory purpose.
- **revision_decision:** Frame composition discipline as semantic infrastructure rather than visual decoration.
- **additional_insight_to_add:** A well-designed terminal page doubles as a context-management tool because its scroll order progressively discloses complexity.

## Section 002: Source Evidence Mapping Table
### Question 01: What decision does this reference help make?
- **current_section_observation:** The table lists eight sources but does not identify which source supports page systems, local patterns, grid rules, or review.
- **supporting_reason:** Claim-scoped roles let authors load only the material needed by the unresolved layout decision.
- **counterargument_or_limit:** Source mapping cannot establish that a finished diagram actually teaches the intended concept.
- **assumptions_and_boundaries:** Local files are frozen and inspectable; public URLs remain inherited records during this no-browse pass.
- **revision_decision:** Add inspected status, supported decisions, limitations, and refresh or artifact checks for every source.
- **additional_insight_to_add:** Separate source authority from diagram relevance so automation guidance cannot decide connector grammar.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** Row order implies local-first retrieval without explaining progressive disclosure among five local files.
- **supporting_reason:** The canonical skill supplies workflow, then specialized references answer pattern, review, editorial-page, or grid questions.
- **counterargument_or_limit:** Reading only one supplement can miss a width or finish criterion that invalidates the draft.
- **assumptions_and_boundaries:** Always read the compact skill and review checklist; load other supplements according to artifact scale.
- **revision_decision:** Define canonical-first retrieval with decision-triggered supplements and a final checklist cross-check.
- **additional_insight_to_add:** Record intentionally skipped references so context reduction remains a deliberate decision rather than silent omission.
### Question 03: When does the default work well?
- **current_section_observation:** The table does not distinguish stable local composition rules from volatile external tool or format claims.
- **supporting_reason:** Local-first works for ASCII character policy, widths, page rhythm, figure selection, alignment, and finish checks.
- **counterargument_or_limit:** Current terminal, Markdown, CI, or agent-format behavior may require refreshed primary documentation.
- **assumptions_and_boundaries:** Stable editorial method uses local evidence; time-sensitive platform behavior uses future targeted refresh.
- **revision_decision:** Add claim-volatility conditions and forbid unnecessary external research for source-backed layout choices.
- **additional_insight_to_add:** Direct copy-paste testing can be stronger than ecosystem analogy for the actual target surface.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** Equal-looking rows can encourage citation by presence without reading or applying source constraints.
- **supporting_reason:** Requiring a source disposition prevents decorative provenance and generic advice.
- **counterargument_or_limit:** A loaded source may legitimately confirm a decision without changing it.
- **assumptions_and_boundaries:** Each read produces change, confirmation, explicit decline, or unresolved conflict.
- **revision_decision:** Add disposition semantics and mark public mappings unrefreshed until opened in a permitted pass.
- **additional_insight_to_add:** A URL can remain a useful refresh target while supporting no present-tense claim.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The section does not compare full-source loading, progressive disclosure, direct artifact tests, or external refresh.
- **supporting_reason:** Full loading maximizes immediate coverage; progressive loading protects context; artifact tests prove actual layout behavior.
- **counterargument_or_limit:** Progressive loading can prematurely narrow the design to the first familiar page system.
- **assumptions_and_boundaries:** Compare at least two plausible patterns when the reader's question does not imply one clearly.
- **revision_decision:** Recommend a hybrid of targeted reading, bounded pattern comparison, and plain-text validation.
- **additional_insight_to_add:** Evidence diversity should cover different failure modes rather than multiply sources that repeat one rule.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Missing risks include stale paths, heading-only reading, example copying, external scope laundering, and source-role duplication.
- **supporting_reason:** These failures create polished references whose recommendations cannot be traced or defended.
- **counterargument_or_limit:** Detailed provenance for every minor label choice would overwhelm the diagram task.
- **assumptions_and_boundaries:** Track material medium, page, pattern, width, and verification decisions rather than every character.
- **revision_decision:** Add concise detection checks for source use, scope, freshness, and decision impact.
- **additional_insight_to_add:** Example skeletons should transfer structure, not their sample nouns or domain assumptions.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** Existing source roles are generic and do not demonstrate a claim-to-source decision.
- **supporting_reason:** Pattern selection, width correction, and an unrefreshed external analogy provide useful contrasts.
- **counterargument_or_limit:** One source can legitimately support several related decisions across a long page.
- **assumptions_and_boundaries:** Examples should name the exact extracted rule and artifact test.
- **revision_decision:** Add row-specific use and misuse statements beneath the evidence map.
- **additional_insight_to_add:** A borderline cross-domain process analogy requires an inference label and a local layout check.
### Question 08: How can the important claims be verified?
- **current_section_observation:** Paths and URLs appear without existence, heading, content, freshness, or incorporation gates.
- **supporting_reason:** Local reads, heading checks, source dispositions, validator output, and plain-text review verify separate links.
- **counterargument_or_limit:** This task cannot establish current public-page content because browsing is prohibited.
- **assumptions_and_boundaries:** Honest inherited status is sufficient until an external claim becomes decision-critical.
- **revision_decision:** Add a source-to-decision-to-artifact verification chain and future refresh record.
- **additional_insight_to_add:** Verify that loaded guidance survives the final page instead of merely appearing in notes.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** Local paths and headings are factual, while terse usage roles are editorial and public freshness is unknown.
- **supporting_reason:** Complete reads confirm page systems, local figures, grid presets, review questions, and validator guidance.
- **counterargument_or_limit:** No source proves one layout universally best for all readers, terminals, or concepts.
- **assumptions_and_boundaries:** Confidence is high for source content and conditional for task-specific synthesis.
- **revision_decision:** Label inspected local facts, inherited external mappings, artifact observations, and layout judgment separately.
- **additional_insight_to_add:** Reader testing can justify a local exception without misrepresenting the general source rule.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The map is presented as documentation rather than as maintenance and recovery infrastructure.
- **supporting_reason:** Claim-scoped provenance identifies which guidance changes when a source, width target, or output medium changes.
- **counterargument_or_limit:** Fine-grained mapping adds maintenance cost when no downstream reuse occurs.
- **assumptions_and_boundaries:** Retain mappings for reusable, disputed, volatile, or high-consequence layout decisions.
- **revision_decision:** Turn the table into an operational evidence index with correction and refresh semantics.
- **additional_insight_to_add:** Provenance makes format migration cheaper because transferable semantics are separated from ASCII-specific mechanics.

## Section 003: Pattern Scoreboard Ranking Table
### Question 01: What decision does this reference help make?
- **current_section_observation:** The scoreboard ranks three evidence patterns but omits the layout decisions that determine an ASCII page's readability.
- **supporting_reason:** A broader priority set can focus effort on page system, width, figure fit, alignment, labels, and verification.
- **counterargument_or_limit:** Static ranking cannot anticipate whether the current defect is wrapping, ambiguity, or wrong medium.
- **assumptions_and_boundaries:** Scores orient new work; observed failures override them during review or repair.
- **revision_decision:** Preserve inherited rows and add trigger-based domain priorities without invented numeric values.
- **additional_insight_to_add:** Treat the earliest irreversible choice as the page system, not the box style.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** Source-map-first ranks highest, while terminal page composition is absent from artifact-building order.
- **supporting_reason:** New work should establish reader question, page system, width, anchors, local pattern, labels, and full-scroll verification.
- **counterargument_or_limit:** A repair should begin at the observed failed gate rather than rebuilding the outline automatically.
- **assumptions_and_boundaries:** The default sequence governs new composed pages and can be shortened for one small figure.
- **revision_decision:** Distinguish reference-authoring order from diagram-building and repair order.
- **additional_insight_to_add:** A declared width turns wording into a design variable before alignment debt accumulates.
### Question 03: When does the default work well?
- **current_section_observation:** `default_adoption_pattern_tier` currently has no task conditions or figure-scale boundary.
- **supporting_reason:** Stable ordering fits bounded pages with one audience, one output surface, and decomposable screenfuls.
- **counterargument_or_limit:** Dense cross-cutting architecture may require medium reassessment before any ASCII priority applies.
- **assumptions_and_boundaries:** Required relationships can be represented with straight paths and limited crossings.
- **revision_decision:** Add selection conditions and a direct gate to every domain pattern.
- **additional_insight_to_add:** Priorities should optimize reader reconstruction, not visual novelty or node count.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** Bare scores can be mistaken for measured confidence or universal effectiveness.
- **supporting_reason:** Explicitly bounding their semantics prevents unsupported arithmetic and authority theater.
- **counterargument_or_limit:** Numbers can remain useful stable reminders of prior editorial ordering.
- **assumptions_and_boundaries:** Retain the seed values but state that calibration and comparison methodology are unavailable.
- **revision_decision:** Prohibit probability interpretations and let failed gates reorder work.
- **additional_insight_to_add:** A lower-priority ASCII-only violation remains a hard completion failure despite its static rank.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The section offers one numeric ranking without risk matrices, ordered checklists, or failure-trigger routing.
- **supporting_reason:** Ordered defaults are simple, while failure routing responds better to existing diagrams and regressions.
- **counterargument_or_limit:** A detailed scoring formula would add unsupported complexity and distract from direct inspection.
- **assumptions_and_boundaries:** Use the least elaborate scheme that changes sequence or catches a material failure.
- **revision_decision:** Keep an ordered table plus a concrete override rule instead of inventing a composite score.
- **additional_insight_to_add:** Separate semantic, spatial, mechanical, and evidence risks so one aggregate cannot hide the failing layer.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Duplicate identifiers and uniform tiers encourage top-score fixation and obscure distinct pattern names.
- **supporting_reason:** Distinct labels and triggers make each row actionable during review.
- **counterargument_or_limit:** A shared stable key remains useful for grouping the reference theme.
- **assumptions_and_boundaries:** Keep the theme key while adding unique pattern names and observable gates.
- **revision_decision:** Add trigger, prevented failure, and direct evidence columns.
- **additional_insight_to_add:** Width overflow should preempt polishing because downstream alignment work will otherwise be discarded.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** Existing rows name prevention targets without showing how priorities alter author behavior.
- **supporting_reason:** A new walkthrough, a wrapped legacy diagram, and a dense topology case can illustrate default, override, and route-away use.
- **counterargument_or_limit:** Examples cannot cover every terminal or Markdown renderer.
- **assumptions_and_boundaries:** Each scenario names the current failure and output contract.
- **revision_decision:** Add concise scenario guidance below the scoreboard.
- **additional_insight_to_add:** A borderline topology should begin with a small ASCII orientation map and route detailed exploration elsewhere.
### Question 08: How can the important claims be verified?
- **current_section_observation:** No rubric validates scores or demonstrates that following a row prevents its failure.
- **supporting_reason:** Each domain priority can point to a width check, pattern-fit question, alignment audit, or reader test.
- **counterargument_or_limit:** One successful page cannot establish a universal ranking.
- **assumptions_and_boundaries:** Verification establishes current-task utility rather than statistical generality.
- **revision_decision:** Attach one falsifiable artifact gate per row and mark score calibration unavailable.
- **additional_insight_to_add:** Record override outcomes over time only if the team later intends to revise the ordering.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** Seed values and descriptions are factual, but their derivation and predictive power are undocumented.
- **supporting_reason:** Local sources directly support page-first design, width constraints, pattern selection, and review discipline.
- **counterargument_or_limit:** Relative priority among those practices depends on task state and reader needs.
- **assumptions_and_boundaries:** Present source-backed patterns and editorial ordering as different evidence classes.
- **revision_decision:** Remove implied measurement while retaining useful failure-prevention intent.
- **additional_insight_to_add:** The gate and failure target are more defensible than the numeric spacing between scores.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The scoreboard is static even though each validator or reader failure changes the next best action.
- **supporting_reason:** Dynamic override creates a feedback controller without abandoning a stable starting sequence.
- **counterargument_or_limit:** Reacting to every preference can destabilize composition and create endless rewrites.
- **assumptions_and_boundaries:** Override only on explicit requirement, mechanical failure, or reader misunderstanding.
- **revision_decision:** Add a first-failed-gate rule and retain the reason for reordering.
- **additional_insight_to_add:** Static defaults reduce search; failure evidence supplies correction; together they support calm iteration.

## Section 004: Idiomatic Thesis Synthesis Statement
### Question 01: What decision does this reference help make?
- **current_section_observation:** The thesis currently describes retrieval order but not what makes an ASCII page idiomatic or teachable.
- **supporting_reason:** A domain thesis can unify medium, page system, local figures, width, prose, and review choices.
- **counterargument_or_limit:** One thesis must allow small standalone figures as well as long editorial pages.
- **assumptions_and_boundaries:** The output promises raw-text portability and a monospaced reading surface.
- **revision_decision:** Center the thesis on composed vertical pages whose local diagrams answer one reader question each.
- **additional_insight_to_add:** State that whitespace and repetition encode hierarchy as materially as connectors do.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** Local-first and external-second guidance omits the canonical outline-to-review workflow.
- **supporting_reason:** Outline, page system, canvas, anchors, modules, local figure, labels, validator, and scroll review follow source guidance.
- **counterargument_or_limit:** Iteration may return to the outline when a local diagram exposes a missing teaching layer.
- **assumptions_and_boundaries:** The sequence is a reversible loop rather than a mandatory one-pass production line.
- **revision_decision:** Present the workflow as a default loop with explicit backtracking triggers.
- **additional_insight_to_add:** Fix wording before widening a shared grid because label economy often preserves the whole composition.
### Question 03: When does the default work well?
- **current_section_observation:** The thesis lacks high-fit conditions for terminal-native explanation.
- **supporting_reason:** It excels for linear walkthroughs, bounded maps, flows, sequences, hierarchies, and comparisons that fit stable widths.
- **counterargument_or_limit:** Dense nonplanar graphs and freeform visual relationships resist vertical decomposition.
- **assumptions_and_boundaries:** The concept can be revealed through a small number of aligned modules and straight paths.
- **revision_decision:** Add direct-fit and route-away conditions to the synthesis.
- **additional_insight_to_add:** A long page works when every 20-to-40-line screenful teaches exactly one new layer.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** Retrieval-focused prose does not stop authors from forcing incompatible topology into ASCII.
- **supporting_reason:** An explicit medium boundary prevents connector ambiguity, wrapping, and decorative noise.
- **counterargument_or_limit:** Simplified ASCII orientation can remain useful beside a richer detailed artifact.
- **assumptions_and_boundaries:** The overview states omitted detail and routes readers to the authoritative richer representation.
- **revision_decision:** Add failure boundaries for curves, dense crossings, interaction, and style-dependent meaning.
- **additional_insight_to_add:** Medium failure is semantic when compression removes relationships readers need for action.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The thesis names no balance among vertical height, horizontal comparison, prose, and diagrams.
- **supporting_reason:** Vertical stacking protects portability, while limited horizontal layouts improve direct comparison of peers.
- **counterargument_or_limit:** Stacking two alternatives can weaken simultaneous contrast and increase scrolling.
- **assumptions_and_boundaries:** Use horizontal space only when comparison is the primary question and width remains verified.
- **revision_decision:** Explain height-versus-comparison and prose-versus-figure tradeoffs without prescribing one layout universally.
- **additional_insight_to_add:** Repeated panels justify horizontal alignment; unrelated content should not share a row merely to fill space.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** The thesis omits page dumps, mixed visual vocabularies, label paragraphs, width drift, and redundant narration.
- **supporting_reason:** These failures break the correspondence between conceptual structure and visual structure.
- **counterargument_or_limit:** Occasional grammar changes can signal a deliberate shift from topology to time or comparison.
- **assumptions_and_boundaries:** A grammar change needs a section boundary and reader cue rather than appearing accidentally within one figure.
- **revision_decision:** Add a compact perceptual and mechanical failure test.
- **additional_insight_to_add:** If prose must narrate every line, the figure likely lacks an obvious path or chose the wrong pattern.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** No thesis example maps a reader question to page and local diagram systems.
- **supporting_reason:** A layered request-lifecycle walkthrough can show progressive disclosure and pattern changes by section.
- **counterargument_or_limit:** One software example may bias users toward architecture content.
- **assumptions_and_boundaries:** The example illustrates translation mechanics, not a required subject domain.
- **revision_decision:** Add a compact mapping and defer full alternatives to worked examples.
- **additional_insight_to_add:** Include a borderline two-column section that stacks vertically when the declared width is reduced.
### Question 08: How can the important claims be verified?
- **current_section_observation:** "Verification-backed decisions" lacks exact mechanical and comprehension gates.
- **supporting_reason:** Editorial validator output plus raw-text cold reading tests both portability and semantic reconstruction.
- **counterargument_or_limit:** Cold-reader results vary with domain knowledge and cannot isolate every layout cause.
- **assumptions_and_boundaries:** Name the intended audience and ask task-specific questions rather than requesting general preference.
- **revision_decision:** Define dual gates and their distinct claim scopes.
- **additional_insight_to_add:** Test copied output in the narrowest promised surface, where hidden alignment assumptions are most likely to fail.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** Existing labels overstate external freshness and understate task-specific editorial judgment.
- **supporting_reason:** Five inspected local sources establish explicit medium, width, pattern, grid, and review defaults.
- **counterargument_or_limit:** Reader vocabulary, optimal pacing, and acceptable density remain contextual.
- **assumptions_and_boundaries:** Record target audience, surface, and page purpose when adapting defaults.
- **revision_decision:** Preserve source facts while labeling synthesis and reader judgments honestly.
- **additional_insight_to_add:** Mechanical correctness increases confidence in portability, not necessarily in explanation quality.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The thesis does not connect page composition to maintainability or context management.
- **supporting_reason:** Modular sections, stable anchors, and progressive depth reduce edit blast radius and cognitive load.
- **counterargument_or_limit:** Excessive modularity can fragment a mechanism that must be understood continuously.
- **assumptions_and_boundaries:** Keep the dominant path continuous and split only at genuine teaching-layer boundaries.
- **revision_decision:** State that page systems organize both reader attention and future edits.
- **additional_insight_to_add:** A terminal page is an executable explanation contract when width, grammar, and reader questions are testable.

## Section 005: Local Corpus Source Map
### Question 01: What decision does this reference help make?
- **current_section_observation:** The map lists titles and headings but not which file resolves workflow, pattern, review, page, or grid uncertainty.
- **supporting_reason:** Distinct retrieval roles reduce context while preserving the source most likely to reverse a layout choice.
- **counterargument_or_limit:** A long page often needs several sources because composition, grid, local figures, and finish interact.
- **assumptions_and_boundaries:** Progressive disclosure narrows initial reading but final review reconciles all relevant guardrails.
- **revision_decision:** Expand each row with trigger, contribution, misuse warning, and artifact gate.
- **additional_insight_to_add:** Define a minimum source set by artifact scale rather than always loading everything.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** The canonical skill appears first without a complete source-loading sequence.
- **supporting_reason:** Skill first, then page/grid/pattern supplements, and review checklist last follows the decision lifecycle.
- **counterargument_or_limit:** Pattern selection may need to precede page selection for a tiny standalone figure.
- **assumptions_and_boundaries:** Small figures shorten the sequence but still validate width and finish.
- **revision_decision:** Document long-page and small-figure retrieval profiles.
- **additional_insight_to_add:** The review checklist should be reread after drafting because pre-reading cannot reveal every actual failure.
### Question 03: When does the default work well?
- **current_section_observation:** Current usage roles do not connect sources to concrete author states.
- **supporting_reason:** Triggered loading works when the author can name whether uncertainty is page, grid, figure, or finish.
- **counterargument_or_limit:** Ambiguous briefs may require a broader scan before the uncertainty can be classified.
- **assumptions_and_boundaries:** Begin with the canonical decision tree and expand only where two plausible paths remain.
- **revision_decision:** Add state-based examples and cross-source handoff points.
- **additional_insight_to_add:** Source headings are navigation aids, not evidence that the body was read.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** Path appearance can satisfy the map without affecting the output.
- **supporting_reason:** A disposition rule makes source use observable and prevents performative retrieval.
- **counterargument_or_limit:** Confirmation is a legitimate outcome even when the draft remains unchanged.
- **assumptions_and_boundaries:** Record extracted constraint, confirmation or change, and final page check.
- **revision_decision:** Require source disposition and reject title-only reuse.
- **additional_insight_to_add:** A source is applied only when its highest-risk constraint survives the final scroll.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** No comparison exists among full loading, progressive loading, skeleton copying, and memory-based authoring.
- **supporting_reason:** Progressive loading saves context; full loading reduces missed caveats; skeletons accelerate geometry; memory is fastest but drift-prone.
- **counterargument_or_limit:** Copying a skeleton can bias the author toward the wrong semantic pattern.
- **assumptions_and_boundaries:** Select the relationship first, then copy only the matching structural grammar.
- **revision_decision:** Recommend progressive loading with a finish-time full guardrail cross-check.
- **additional_insight_to_add:** Treat examples as parameterized structures whose labels, widths, and domains must be recomputed.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** The map omits archived-version context, overlapping advice, copied widths, and examples mistaken for mandates.
- **supporting_reason:** These mistakes create false confidence and layouts incompatible with the target canvas.
- **counterargument_or_limit:** Frozen historical sources are intentionally authoritative for this evolution pass.
- **assumptions_and_boundaries:** Preserve frozen facts while identifying future refresh triggers separately.
- **revision_decision:** Add version, overlap, and example-scope cautions to each row.
- **additional_insight_to_add:** A preset width must be chosen for the target, not inherited from an example's accidental line length.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** Generic usage roles provide no actual retrieval and application examples.
- **supporting_reason:** Long walkthrough, tiny sequence, and ambiguous comparison cases can demonstrate source selection quality.
- **counterargument_or_limit:** The same page may evolve from small to editorial scope during iteration.
- **assumptions_and_boundaries:** Re-evaluate the source profile when artifact scale or purpose changes.
- **revision_decision:** Add examples of direct, insufficient, and expanded retrieval.
- **additional_insight_to_add:** Borderline scope should trigger an outline before loading every pattern skeleton.
### Question 08: How can the important claims be verified?
- **current_section_observation:** No gate proves source paths exist, relevant sections were read, or constraints appear in the artifact.
- **supporting_reason:** Existence checks, dispositions, validator results, and reader review cover provenance through outcome.
- **counterargument_or_limit:** Presence and validator success still cannot prove the selected pattern teaches the right concept.
- **assumptions_and_boundaries:** A target-reader question must accompany mechanical evidence.
- **revision_decision:** Add a three-link verification chain for each loaded source.
- **additional_insight_to_add:** Use a fixed target width during comparison so source-driven changes are not confounded by canvas drift.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** Paths, titles, and headings are factual; role and priority assignments are editorial synthesis.
- **supporting_reason:** Full reads confirm distinct but complementary responsibilities for all five files.
- **counterargument_or_limit:** The best retrieval subset depends on output scale and author familiarity.
- **assumptions_and_boundaries:** State the selected profile and why omitted sources cannot reverse the current decision.
- **revision_decision:** Keep factual map fields and label usage guidance as bounded synthesis.
- **additional_insight_to_add:** Confidence grows when source constraints and cold-reader evidence agree, without becoming a universal rule.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The map does not show how source order shapes context and implementation surface.
- **supporting_reason:** Progressive disclosure prevents a pattern library from becoming an invitation to combine every diagram grammar.
- **counterargument_or_limit:** Too little comparative context can create premature convergence on a familiar layout.
- **assumptions_and_boundaries:** Compare two candidates only when the reader question genuinely admits both.
- **revision_decision:** Add choose, defer, or reject disposition for every loaded option.
- **additional_insight_to_add:** A useful source map narrows the page, while an ineffective one merely enlarges the prompt.

## Section 006: External Research Source Map
### Question 01: What decision does this reference help make?
- **current_section_observation:** Three public resources are listed without explaining their process-only relevance to ASCII layout.
- **supporting_reason:** Narrow roles prevent respected external sources from lending accidental authority to unrelated diagram choices.
- **counterargument_or_limit:** Current agent and automation behavior can still affect how validation and instructions are delivered.
- **assumptions_and_boundaries:** URLs are inherited and unrefreshed because this pass performs no browsing.
- **revision_decision:** Add allowed claim scope, prohibited extrapolation, status, and future refresh triggers.
- **additional_insight_to_add:** External authority transfers only to the documented format or platform contract.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** The map implies routine ecosystem checking even for stable terminal composition rules.
- **supporting_reason:** Local evidence and target-surface tests are sufficient until a volatile external behavior can change implementation.
- **counterargument_or_limit:** Delaying refresh can miss a changed renderer or automation constraint.
- **assumptions_and_boundaries:** Refresh only depended-on current claims with material decision impact.
- **revision_decision:** Adopt claim-triggered primary-source refresh rather than broad periodic research.
- **additional_insight_to_add:** A local validator failure should generate the query more precisely than the theme title can.
### Question 03: When does the default work well?
- **current_section_observation:** Current rows do not distinguish stable editorial choices from current platform facts.
- **supporting_reason:** External checks help with instruction formats, CI syntax, and rendering behavior when those surfaces are used.
- **counterargument_or_limit:** They add no direct evidence for choosing a tree over a sequence diagram.
- **assumptions_and_boundaries:** The source must own the exact process or platform claim being refreshed.
- **revision_decision:** Add supported-use examples and explicit non-layout scope.
- **additional_insight_to_add:** Always retest the local raw text after applying externally sourced process guidance.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** Stable-looking URLs can mask changed contents, indirect authority, and mere analogy.
- **supporting_reason:** Marking them unrefreshed prevents present-tense claims from being fabricated.
- **counterargument_or_limit:** Strong caveats should not erase their usefulness as future targets.
- **assumptions_and_boundaries:** Historical mapping presence is known even when current semantic support is not.
- **revision_decision:** Preserve URLs while withholding current-content conclusions.
- **additional_insight_to_add:** Link availability and claim validation must remain separate checks.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** No comparison exists among official docs, community examples, local conventions, and direct rendering experiments.
- **supporting_reason:** Official sources define contracts; local files define method; experiments test the actual target surface.
- **counterargument_or_limit:** Community examples can reveal practical failures absent from official documentation.
- **assumptions_and_boundaries:** Use examples as leads and verify contracts and artifact behavior independently.
- **revision_decision:** Add source-selection rules instead of expanding the frozen map speculatively.
- **additional_insight_to_add:** One target-terminal copy test may answer portability better than several generic articles.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Risks include stale links, secondary summaries, scope laundering, and external overrides of local requirements.
- **supporting_reason:** These failures create authoritative prose without a reproducible page decision.
- **counterargument_or_limit:** Local guidance itself may need adaptation when direct target evidence disagrees.
- **assumptions_and_boundaries:** Record conflict and artifact result rather than silently privileging either source.
- **revision_decision:** Add freshness, primacy, scope, conflict, and decision-impact checks.
- **additional_insight_to_add:** A source conflict can narrow support scope without invalidating the entire reference.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** Public rows lack examples and may be read as general endorsements.
- **supporting_reason:** CI validation, diagram grammar, and borrowed instruction structure provide useful contrasts.
- **counterargument_or_limit:** Current page details cannot be cited because they were not opened.
- **assumptions_and_boundaries:** Examples describe future permissible roles, not refreshed source contents.
- **revision_decision:** Add role-level good, bad, and analogy cases.
- **additional_insight_to_add:** A process analogy becomes usable only after local ASCII constraints are restated and checked.
### Question 08: How can the important claims be verified?
- **current_section_observation:** No access date, heading, extracted claim, or changed action is recorded.
- **supporting_reason:** A future refresh packet makes external evidence repeatable and bounded.
- **counterargument_or_limit:** Search ordering and pages may change after the record is created.
- **assumptions_and_boundaries:** Preserve direct URLs and concise claim summaries rather than rankings.
- **revision_decision:** Add source owner, checked date, relevant section, claim, decision, and local retest.
- **additional_insight_to_add:** Record `no_material_impact` so future authors do not repeat fruitless refreshes.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** Names and seed roles are known; current page contents and applicability are not.
- **supporting_reason:** The seed accurately preserves these public evidence surfaces.
- **counterargument_or_limit:** No current product, automation, or format assertion follows without browsing.
- **assumptions_and_boundaries:** Use `external_mapping_unrefreshed_note` until a permitted refresh occurs.
- **revision_decision:** Replace categorical freshness with an explicit confidence boundary.
- **additional_insight_to_add:** Honest nonverification is stronger than inferred currency from a familiar URL.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** External evidence is additive rather than treated as limited context capacity.
- **supporting_reason:** Event-driven refresh keeps the ASCII page and its actual failing decision central.
- **counterargument_or_limit:** Purely reactive refresh may miss proactive deprecation signals.
- **assumptions_and_boundaries:** Schedule checks only for volatile surfaces the workflow actively depends on.
- **revision_decision:** Add event and scheduled triggers with explicit stop conditions.
- **additional_insight_to_add:** Search belongs to observability when an external change signal maps to one local retest.

## Section 007: Anti Pattern Registry Table
### Question 01: What decision does this reference help make?
- **current_section_observation:** The registry covers evidence failures but omits the layout defects that make ASCII pages unreadable.
- **supporting_reason:** Domain failures can route authors to narrow, split, realign, relabel, simplify, or change medium.
- **counterargument_or_limit:** Anti-pattern labels must not prohibit deliberate asymmetry or dense specialist diagrams automatically.
- **assumptions_and_boundaries:** A finding requires violated purpose, width, portability, or reader evidence.
- **revision_decision:** Add semantic, spatial, textual, mechanical, and page-composition anti-patterns.
- **additional_insight_to_add:** Pair every pattern with a detection signal and valid exception boundary.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** Existing replacements address provenance but provide no repair order for a broken page.
- **supporting_reason:** Restore medium and width first, then reading path, pattern fit, grid, labels, and prose.
- **counterargument_or_limit:** Wrong pattern fit can require redesign before small width repairs are worth doing.
- **assumptions_and_boundaries:** Repair the earliest upstream failure that invalidates downstream alignment work.
- **revision_decision:** Add a causal diagnosis order and smallest-safe correction rule.
- **additional_insight_to_add:** Preserve a failing copy so repair can be compared at the same target width.
### Question 03: When does the default work well?
- **current_section_observation:** No context distinguishes quick figures from reusable terminal pages.
- **supporting_reason:** Explicit registry review pays off for repeated panels, long pages, handoffs, and copied documentation.
- **counterargument_or_limit:** A disposable three-node flow needs a lighter process.
- **assumptions_and_boundaries:** Every artifact still receives ASCII, width, direction, and raw-text checks.
- **revision_decision:** Define lightweight and editorial review depths.
- **additional_insight_to_add:** The smallest figure can still fail semantically by choosing topology when order matters.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** Labels can turn stylistic preferences into alleged defects without reader evidence.
- **supporting_reason:** Requiring an observable collapse or ambiguity limits prescriptive taste enforcement.
- **counterargument_or_limit:** Some portability risks appear only on another surface, not in the author's preview.
- **assumptions_and_boundaries:** Validator and target-copy evidence can establish latent mechanical risk.
- **revision_decision:** Add exception conditions and require purpose-linked impact.
- **additional_insight_to_add:** Deliberate asymmetry is valid only when readers infer the intended distinction correctly.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** One safer replacement per row hides choices among tightening, stacking, splitting, or rerouting.
- **supporting_reason:** Different remedies preserve comparison, continuity, detail, or portability differently.
- **counterargument_or_limit:** Multiple options can delay an obvious width or character fix.
- **assumptions_and_boundaries:** Apply hard mechanical corrections first; prototype alternatives for semantic layout failures.
- **revision_decision:** Add mitigation choices and the evidence selecting among them.
- **additional_insight_to_add:** Shortening labels often preserves a comparison row better than widening the page.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Tabs, Unicode, wrap, crossings, paragraphs, floating labels, drift, random centering, and blobs are absent.
- **supporting_reason:** These are directly named or implied by the local skill and checklist.
- **counterargument_or_limit:** Controlled renderers may permit Unicode, but that is outside the strict profile.
- **assumptions_and_boundaries:** This reference promises bare-terminal ASCII portability.
- **revision_decision:** Add the highest-consequence terminal-specific rows with concrete checks.
- **additional_insight_to_add:** Include prose-diagram duplication because semantic redundancy inflates scroll without teaching.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** Current rows provide no visible layout-level contrasts.
- **supporting_reason:** A straight flow, wrapped mega-map, and deliberate asymmetric callout clarify classification.
- **counterargument_or_limit:** Examples depend on the declared canvas and audience.
- **assumptions_and_boundaries:** Compare artifacts at the same width and reader question.
- **revision_decision:** Add concise examples and route full cases to the worked-example section.
- **additional_insight_to_add:** Borderline cases need the next reader question that will accept or reject the exception.
### Question 08: How can the important claims be verified?
- **current_section_observation:** Detection methods are mostly textual and omit the bundled validator and cold-reader tasks.
- **supporting_reason:** Machine checks expose characters, whitespace, and widths; readers expose ambiguity and overload.
- **counterargument_or_limit:** Reader disagreement may reflect domain unfamiliarity instead of layout failure.
- **assumptions_and_boundaries:** Ask structure-specific questions appropriate to the intended audience.
- **revision_decision:** Add a direct test and evidence artifact to every row.
- **additional_insight_to_add:** Validate after copying into the target container, not only the source file.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** Generic rows are plausible, while ASCII-specific priority is not quantified by incident data.
- **supporting_reason:** Local sources explicitly enumerate the major layout and finish failures.
- **counterargument_or_limit:** Frequency and severity vary with page size, renderer, and reader expertise.
- **assumptions_and_boundaries:** Present the registry as diagnostic guidance, not a statistical ranking.
- **revision_decision:** Add source-backed confidence and task-specific exception language.
- **additional_insight_to_add:** Width and character violations are objective within the profile; density remains partly editorial judgment.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** Failures appear independent despite common cascades from poor page planning.
- **supporting_reason:** Wrong width drives label compression, connector crossings, panel drift, and explanatory prose bloat.
- **counterargument_or_limit:** Not every clustered defect shares one cause, so diagnosis still needs evidence.
- **assumptions_and_boundaries:** Trace only causal chains that alter repair order.
- **revision_decision:** Add width and page-system cascades to the diagnosis guidance.
- **additional_insight_to_add:** Restoring observability means fixing the canvas and copy target before debating aesthetics.

## Section 008: Verification Gate Command Set
### Question 01: What decision does this reference help make?
- **current_section_observation:** One repository command is listed without separating reference validation from ASCII artifact quality.
- **supporting_reason:** Layered gates decide whether structure, characters, widths, composition, and reader understanding each pass.
- **counterargument_or_limit:** Project-specific launch or rendering commands cannot be invented generically.
- **assumptions_and_boundaries:** The bundled ASCII validator applies to file-backed pages; manual review covers semantic fit.
- **revision_decision:** Preserve the repository command and add exact ASCII validator, scope, and reader gates.
- **additional_insight_to_add:** Explicitly prohibit treating a document verifier as proof of terminal rendering quality.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** The seed provides no cheap-to-expensive execution order.
- **supporting_reason:** Reference checks, ASCII validator, target copy inspection, and cold-reader review minimize feedback cost.
- **counterargument_or_limit:** A small inline figure may not exist as a standalone file for the validator.
- **assumptions_and_boundaries:** Validate through stdin or a temporary permitted artifact when file backing is absent.
- **revision_decision:** Define minimum and editorial verification sequences.
- **additional_insight_to_add:** Use `--editorial` only for composed pages because heuristics can misclassify tiny figures.
### Question 03: When does the default work well?
- **current_section_observation:** No artifact size or delivery condition accompanies the command.
- **supporting_reason:** Layered validation fits file-backed documentation, long terminal pages, and repeated review workflows.
- **counterargument_or_limit:** Copy-paste destinations may impose wrapping or styling not represented by local file checks.
- **assumptions_and_boundaries:** Inspect every promised destination at its narrowest supported width.
- **revision_decision:** Add target-surface adaptation and evidence fields.
- **additional_insight_to_add:** Validate rendered code blocks and raw files separately when both are delivered.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** A command may pass while the diagram answers the wrong question or overwhelms readers.
- **supporting_reason:** Separating mechanical and comprehension claims prevents false completion.
- **counterargument_or_limit:** Reader review can be subjective and unavailable for low-risk work.
- **assumptions_and_boundaries:** The author can perform an unstaged cold-read with explicit reconstruction questions.
- **revision_decision:** Bound each gate's claim and report unavailable reader evidence honestly.
- **additional_insight_to_add:** A validator failure should route to a specific line or rule, not a generic rewrite.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** No comparison exists among validator text, JSON output, manual width checks, screenshots, or reader tasks.
- **supporting_reason:** Text suits authors, JSON suits automation, target rendering exposes wrap, and readers test meaning.
- **counterargument_or_limit:** More evidence increases maintenance and can duplicate the same claim.
- **assumptions_and_boundaries:** Select the smallest evidence set that can falsify promised behavior.
- **revision_decision:** Add a claim-to-gate table with limitations.
- **additional_insight_to_add:** Screenshots are secondary because the raw-text contract must survive without image evidence.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Wrong paths, stale outputs, permissive Unicode flags, mismatched widths, and styled-only review are unmentioned.
- **supporting_reason:** These conditions create misleading green results.
- **counterargument_or_limit:** `--allow-unicode` is legitimate for a declared nonstrict profile.
- **assumptions_and_boundaries:** This reference's default strict profile omits that flag.
- **revision_decision:** Add candidate identity, exact options, target width, and fresh-output checks.
- **additional_insight_to_add:** Record the command's working directory because archived relative paths otherwise fail silently in handoff.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** The section contains a command but no evidence packet examples.
- **supporting_reason:** Fresh validator output, an exit-zero-only report, and a mechanically valid ambiguous diagram show distinctions.
- **counterargument_or_limit:** Hypothetical outputs should not be presented as observed results.
- **assumptions_and_boundaries:** Examples define evidence shape, not repository measurements.
- **revision_decision:** Add good, bad, and borderline verification records.
- **additional_insight_to_add:** Borderline evidence needs the exact reader task that will resolve semantic uncertainty.
### Question 08: How can the important claims be verified?
- **current_section_observation:** Verification is an instruction rather than a mapping from claims to proof.
- **supporting_reason:** Characters, tabs, whitespace, width, grid, direction, and comprehension require distinct checks.
- **counterargument_or_limit:** No automated rule can prove aesthetic calm or teaching quality universally.
- **assumptions_and_boundaries:** Editorial heuristics flag risk; human judgment decides purpose and clarity.
- **revision_decision:** Add method, evidence, pass condition, and limit for each claim.
- **additional_insight_to_add:** Include one deliberate narrow-width perturbation to test graceful stacking.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** Exact repository and validator interfaces are known; their current run results are not yet recorded here.
- **supporting_reason:** Local help output confirms validator options and purpose.
- **counterargument_or_limit:** Passing heuristics do not establish reader success.
- **assumptions_and_boundaries:** Report command evidence and editorial verdict as separate classes.
- **revision_decision:** Bound command semantics and avoid promising checks not implemented.
- **additional_insight_to_add:** Derive verification claims from observed output rather than reassuring script names.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** Verification appears terminal rather than feeding composition iteration.
- **supporting_reason:** Width and reader failures identify whether wording, stacking, pattern, or medium should change next.
- **counterargument_or_limit:** Full checks after every keystroke would slow drafting unnecessarily.
- **assumptions_and_boundaries:** Use cheap width checks during drafting and full gates at candidate milestones.
- **revision_decision:** Add staged cadence and evidence retention guidance.
- **additional_insight_to_add:** Keep one failed validator or reader example when it captures a recurring regression.

## Section 009: Agent Usage Decision Guide
### Question 01: What decision does this reference help make?
- **current_section_observation:** The guide opens on theme keywords but does not route by output contract or reader question.
- **supporting_reason:** Primary, companion, and avoid modes prevent overusing ASCII or underusing its portability strengths.
- **counterargument_or_limit:** Hybrid documentation may need several formats for distinct audiences.
- **assumptions_and_boundaries:** One format owns each claim and the handoff between artifacts is explicit.
- **revision_decision:** Replace keyword routing with medium-fit, page-scale, and relationship decisions.
- **additional_insight_to_add:** Choose the discipline whose failure would most obstruct reader action.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** Existing bullets prioritize sources but omit an artifact-building preflight.
- **supporting_reason:** Reader, question, surface, canvas, page system, figure, anchors, and evidence define an executable start.
- **counterargument_or_limit:** A tiny requested figure may need only relationship, width, and finish decisions.
- **assumptions_and_boundaries:** Scale the preflight without skipping medium and pattern fit.
- **revision_decision:** Add full-page and small-figure action paths.
- **additional_insight_to_add:** Require one sentence stating what the reader should know after each section.
### Question 03: When does the default work well?
- **current_section_observation:** Nearby workflow triggers are broad and can overfire on any mention of diagrams.
- **supporting_reason:** The method fits raw Markdown, terminals, text files, design notes, and copy-stable explanations.
- **counterargument_or_limit:** Styled documents and interactive graph tools may still include a small ASCII summary.
- **assumptions_and_boundaries:** ASCII owns orientation while richer media own detail when relationships exceed the canvas.
- **revision_decision:** Add direct, companion, and bounded-summary modes.
- **additional_insight_to_add:** The raw-text requirement is a stronger trigger than the word "diagram."
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** No negative trigger covers curves, dense topology, rich styling, or interaction.
- **supporting_reason:** Early route-away avoids unreadable compression and connector ambiguity.
- **counterargument_or_limit:** A simplified abstraction may intentionally omit nonessential edges.
- **assumptions_and_boundaries:** The omission is documented and does not remove action-critical relationships.
- **revision_decision:** Add medium-boundary and adjacent-routing tests.
- **additional_insight_to_add:** A diagram that needs horizontal panning has already violated the default terminal workflow.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The guide does not compare prose, table, Mermaid, HTML, image, or graph explorer.
- **supporting_reason:** Each alternative supports different density, automation, styling, spatial freedom, and interaction.
- **counterargument_or_limit:** Explicit user medium requirements can settle the choice immediately.
- **assumptions_and_boundaries:** Compare only when the requested contract remains satisfiable by multiple formats.
- **revision_decision:** Add concise selection cues and route details later.
- **additional_insight_to_add:** Prose plus one small figure often outperforms a larger diagram that contains prose inside boxes.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** The guide lacks stop signals for unclear purpose, no width, several jobs, or unavailable target rendering.
- **supporting_reason:** These signals expose category and planning failures before alignment work begins.
- **counterargument_or_limit:** Exploration may legitimately sketch several alternatives before width and page system freeze.
- **assumptions_and_boundaries:** Label exploration and select one baseline before acceptance work.
- **revision_decision:** Add preflight blockers and phase distinctions.
- **additional_insight_to_add:** Every public panel is a claim about peer relationships and therefore needs semantic justification.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** Process bullets provide no triggering scenarios.
- **supporting_reason:** Terminal walkthrough, dense dependency graph, and hybrid overview cases clarify routing.
- **counterargument_or_limit:** Domain expertise can change which edges are essential.
- **assumptions_and_boundaries:** The intended reader and task define necessary detail.
- **revision_decision:** Add scenario examples with primary and companion ownership.
- **additional_insight_to_add:** A hybrid should state which artifact is authoritative when representations differ.
### Question 08: How can the important claims be verified?
- **current_section_observation:** Pattern gates are encouraged but no preflight verifies correct workflow selection.
- **supporting_reason:** Artifact, audience, relationship, width, page system, and evidence records expose category errors.
- **counterargument_or_limit:** A prototype may reveal the initial route wrong despite careful planning.
- **assumptions_and_boundaries:** Routing remains reversible until target-copy and reader evidence exists.
- **revision_decision:** Add preflight and post-copy decision checks.
- **additional_insight_to_add:** Record rejected media briefly so later authors reopen them only with new constraints.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** Source description clearly targets terminal-native ASCII, while hybrid boundaries require contextual judgment.
- **supporting_reason:** Local guardrails explicitly identify when dense, curved, or polished needs should route away.
- **counterargument_or_limit:** Simplicity and acceptable information loss depend on reader purpose.
- **assumptions_and_boundaries:** State omitted relationships and authoritative follow-up artifacts.
- **revision_decision:** Present fit rules as strong defaults with documented exceptions.
- **additional_insight_to_add:** Uncertainty should prompt the smallest representative page skeleton, not full parallel artifacts.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The guide does not connect routing to ownership, maintenance, or evidence.
- **supporting_reason:** Medium choice determines source grammar, verification, width, and future edit cost.
- **counterargument_or_limit:** Overformal ownership is unnecessary for one small personal note.
- **assumptions_and_boundaries:** Add contracts only when multiple artifacts or owners exist.
- **revision_decision:** Explain routing's architectural consequences for documentation.
- **additional_insight_to_add:** Medium selection is an information architecture decision, not merely formatting.

## Section 010: User Journey Scenario
### Question 01: What decision does this reference help make?
- **current_section_observation:** The scenario is generic and does not show a reader question becoming a page and figure system.
- **supporting_reason:** A concrete journey demonstrates how source guidance changes outline, canvas, patterns, labels, and evidence.
- **counterargument_or_limit:** One asynchronous-system example cannot represent every documentation genre.
- **assumptions_and_boundaries:** The example teaches process, not mandatory technical content.
- **revision_decision:** Expand from cold start through candidate, failure recovery, and handoff.
- **additional_insight_to_add:** Keep one stable brief so each layout choice has a visible consequence.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** Reading path, example, diagram, and rewrite choices are listed without sequence.
- **supporting_reason:** Audience, question, section jobs, page system, canvas, local figures, and review form a coherent path.
- **counterargument_or_limit:** First drafts may reveal the audience lacks vocabulary assumed by the outline.
- **assumptions_and_boundaries:** The journey may add a glossary layer before mechanism detail.
- **revision_decision:** Use a staged journey with explicit re-outline checkpoints.
- **additional_insight_to_add:** Freeze target width before label convergence to keep comparisons causal.
### Question 03: When does the default work well?
- **current_section_observation:** The starting state does not describe a relationship structure suitable for ASCII.
- **supporting_reason:** A bounded async request path has actors, order, handoff, and outcome that fit layered figures.
- **counterargument_or_limit:** Full service topology may exceed the selected walkthrough's purpose.
- **assumptions_and_boundaries:** Include only components required to answer the reader's next operational question.
- **revision_decision:** State high-fit conditions and documented omissions.
- **additional_insight_to_add:** Use a small system map for orientation and a sequence only for time-sensitive exchange.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** No branch handles width overflow, duplicated sections, or dense cross-service topology.
- **supporting_reason:** Explicit branches prevent endless local realignment when the page system or medium is wrong.
- **counterargument_or_limit:** Several iterations may be needed before the root cause becomes clear.
- **assumptions_and_boundaries:** Preserve target width and reader question while testing one structural change.
- **revision_decision:** Add tighten, stack, split, re-pattern, or route-away decisions.
- **additional_insight_to_add:** A failed cold-reader task with clean validation points to semantics rather than mechanics.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The journey does not compare layered walkthrough, mechanism trace, or one all-in-one sequence.
- **supporting_reason:** Layering supports teaching; trace supports action; one sequence preserves time but may overload width.
- **counterargument_or_limit:** Splitting can force readers to integrate state across sections.
- **assumptions_and_boundaries:** Repeat stable actors and vocabulary while adding one new layer.
- **revision_decision:** Include a bounded candidate comparison before full drafting.
- **additional_insight_to_add:** Reuse anchors across layers so progressive disclosure feels cumulative rather than disconnected.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** The scenario lacks safeguards against changing width, labels, patterns, and scope simultaneously.
- **supporting_reason:** A stable baseline makes reader and validator feedback actionable.
- **counterargument_or_limit:** Broad exploration may intentionally vary several dimensions early.
- **assumptions_and_boundaries:** Label exploration, then freeze page system and canvas for convergence.
- **revision_decision:** Distinguish exploration, convergence, and acceptance evidence.
- **additional_insight_to_add:** Record which section owns each fact to prevent prose and figures from duplicating it.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** The role description offers no actual page skeleton or failure contrast.
- **supporting_reason:** A layered async walkthrough, a 120-column mega-sequence, and a hybrid overview clarify outcomes.
- **counterargument_or_limit:** Hypothetical examples cannot prove real reader performance.
- **assumptions_and_boundaries:** Label them as operational illustrations requiring actual tests.
- **revision_decision:** Add good, bad, and borderline states with next actions.
- **additional_insight_to_add:** Borderline work becomes acceptable when detailed topology is delegated to an authoritative richer artifact.
### Question 08: How can the important claims be verified?
- **current_section_observation:** Final acceptance bar is named without validator options, copy targets, or reader questions.
- **supporting_reason:** Exact width checks and reconstruction tasks make the journey reviewable.
- **counterargument_or_limit:** One reader cannot represent all audience backgrounds.
- **assumptions_and_boundaries:** Select a representative reader or document knowledge assumptions explicitly.
- **revision_decision:** Add a completion packet containing mechanical and reader evidence.
- **additional_insight_to_add:** Ask readers to predict the next message or owner, not merely rate visual appeal.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The scenario implies structured process guarantees an actionable page.
- **supporting_reason:** Structure improves traceability and catches common mechanical failures reliably.
- **counterargument_or_limit:** It cannot guarantee vocabulary fit, domain correctness, or reader learning.
- **assumptions_and_boundaries:** Subject matter facts require separate technical review.
- **revision_decision:** Bound success to layout and scoped comprehension evidence.
- **additional_insight_to_add:** A well-documented rejection remains useful when it prevents shipping a misleading page.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The journey ends at acceptance without future edits or format migration.
- **supporting_reason:** A page manifest and stable anchors support maintenance, reuse, and handoff.
- **counterargument_or_limit:** Archiving every draft creates noise and obscures the selected baseline.
- **assumptions_and_boundaries:** Retain baseline, accepted page, and one informative structural rejection.
- **revision_decision:** Add a compact completion and retention record.
- **additional_insight_to_add:** The page's durable product includes its reader contract and declared omissions, not only its characters.

## Section 011: Decision Tradeoff Guide
### Question 01: What decision does this reference help make?
- **current_section_observation:** Adopt/adapt/avoid rows focus on evidence agreement rather than medium, page, pattern, and width choices.
- **supporting_reason:** A domain guide can route among ASCII, page systems, local figures, canvases, and richer media.
- **counterargument_or_limit:** Too many matrices can overwhelm readers before they have a concrete brief.
- **assumptions_and_boundaries:** Include only choices that change structure, portability, or verification.
- **revision_decision:** Expand source routing into artifact, page-system, figure, and canvas tradeoffs.
- **additional_insight_to_add:** Name false-adoption and false-rejection costs because avoiding ASCII can also lose portability.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** Adoption currently requires external agreement despite complete local method guidance.
- **supporting_reason:** Local sources plus target fit justify an ASCII skeleton; external refresh is conditional on volatile platform claims.
- **counterargument_or_limit:** Target renderer limitations can invalidate a local preset or delivery assumption.
- **assumptions_and_boundaries:** Prototype at the narrowest promised surface before committing to a long page.
- **revision_decision:** Recommend adopt for raw-text needs, adapt for hybrids, and avoid for irreducible visual complexity.
- **additional_insight_to_add:** Let the skeleton generate evidence before expensive prose and border polishing.
### Question 03: When does the default work well?
- **current_section_observation:** Evidence agreement does not mention audience, relationship type, or canvas feasibility.
- **supporting_reason:** ASCII fits bounded relationships, clear direction, limited nodes, and stable monospaced surfaces.
- **counterargument_or_limit:** Domain jargon can still make a mechanically clear page inaccessible.
- **assumptions_and_boundaries:** Vocabulary and technical facts receive audience and subject review.
- **revision_decision:** Add concept, surface, scale, and audience fit conditions.
- **additional_insight_to_add:** Inspectability is a selection criterion because hidden styling weakens the raw-text contract.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** Avoid conditions mention thin evidence rather than dense topology, curves, styling, or interaction.
- **supporting_reason:** Medium mismatch is more decisive than missing ecosystem analogues for stable local guidance.
- **counterargument_or_limit:** A simplified overview can remain valuable beside detailed media.
- **assumptions_and_boundaries:** The overview's omissions and authority relationship are explicit.
- **revision_decision:** Add dominant-information and horizontal-scan tests to avoidance.
- **additional_insight_to_add:** Wrong format can create false certainty by hiding relationships it cannot draw.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** Core page and figure alternatives are absent.
- **supporting_reason:** Gallery, glossary, layers, compare, trace, map, flow, sequence, tree, and grid answer different questions.
- **counterargument_or_limit:** Some pages legitimately combine several local patterns across sections.
- **assumptions_and_boundaries:** One grammar owns each local figure and shared anchors preserve page continuity.
- **revision_decision:** Add compact selection tables and falsification questions.
- **additional_insight_to_add:** Choose the relationship model before aesthetics or skeleton copying.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Reversal cost, wrap risk, duplicated explanation, and unfamiliar-reader burden are omitted.
- **supporting_reason:** These costs determine whether a plausible choice remains maintainable and actionable.
- **counterargument_or_limit:** Early sketches can tolerate imperfect alignment and temporary labels.
- **assumptions_and_boundaries:** Prototype debt is acceptable only while clearly labelled and cheaply discardable.
- **revision_decision:** Add semantic, spatial, maintenance, and evidence costs to major choices.
- **additional_insight_to_add:** Prefer options that are cheap to falsify before writing long explanatory prose.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** Verification questions lack actual choice outcomes.
- **supporting_reason:** Topology map, time sequence, and overloaded hybrid show semantic selection quality.
- **counterargument_or_limit:** A reader can need both topology and sequence in adjacent sections.
- **assumptions_and_boundaries:** The issue is simultaneous grammar within one local figure, not page-level variety.
- **revision_decision:** Add examples below each decision family.
- **additional_insight_to_add:** Borderline two-column content stacks when width evidence disproves side-by-side comparison.
### Question 08: How can the important claims be verified?
- **current_section_observation:** Current questions do not prescribe skeleton comparison or target-width evidence.
- **supporting_reason:** Minimal skeletons, equal content, fixed canvas, validator, and reader tasks create fair comparison.
- **counterargument_or_limit:** Authors may favor the grammar they know best.
- **assumptions_and_boundaries:** Record familiarity bias and test defining behavior, not equal line count.
- **revision_decision:** Add a bounded comparative-prototype protocol.
- **additional_insight_to_add:** A fair pattern comparison asks the same reader question of each candidate.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** Routing categories are useful, but source agreement alone cannot select layout.
- **supporting_reason:** Local sources establish explicit pattern semantics and width defaults.
- **counterargument_or_limit:** Reader expertise, content density, and target renderer shape final choice.
- **assumptions_and_boundaries:** Mark source defaults, mechanical results, and editorial judgments separately.
- **revision_decision:** Remove automatic adoption implications and retain bounded recommendations.
- **additional_insight_to_add:** Uncertainty can be reduced by choosing the most reversible skeleton first.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** Decisions are treated as one-time choices rather than commitments with maintenance cost.
- **supporting_reason:** Width, anchors, and page-system choices affect every later edit and format migration.
- **counterargument_or_limit:** Designing for every future migration overabstracts small notes.
- **assumptions_and_boundaries:** Preserve reversibility at high-cost page boundaries, not every character.
- **revision_decision:** Add option-value and migration considerations to tradeoffs.
- **additional_insight_to_add:** The best early choice maximizes reader information gained per line of draft.

## Section 012: Local Corpus Hierarchy
### Question 01: What decision does this reference help make?
- **current_section_observation:** Five rows share one generic reviewer question despite distinct canonical, pattern, review, editorial, and grid roles.
- **supporting_reason:** Specific hierarchy questions clarify which source leads and which constrains a decision.
- **counterargument_or_limit:** Canonical status should not override narrower evidence in its exact scope.
- **assumptions_and_boundaries:** Authority coordinates defaults; relevance selects the immediate answer.
- **revision_decision:** Replace generic prompts with contribution, limit, and conflict actions.
- **additional_insight_to_add:** Define canonical as entrypoint, not monopoly on detail.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** Classification vocabulary exceeds the populated canonical/supporting roles.
- **supporting_reason:** Canonical-first retrieval plus specialized constraints creates consistent progressive disclosure.
- **counterargument_or_limit:** Archived and newer active material may conflict in a future refresh.
- **assumptions_and_boundaries:** Frozen 202603 sources govern this pass until concrete changed guidance is compared.
- **revision_decision:** Add version-aware hierarchy and future refresh procedure.
- **additional_insight_to_add:** Newer is a trigger for comparison, not automatic superiority.
### Question 03: When does the default work well?
- **current_section_observation:** No scenario shows hierarchy reducing context while retaining decisive caveats.
- **supporting_reason:** It works when authors can load one entrypoint and one or two focused supplements.
- **counterargument_or_limit:** Long editorial pages need all source roles reconciled.
- **assumptions_and_boundaries:** Source breadth scales with artifact breadth and unresolved risk.
- **revision_decision:** Add small-figure and long-page hierarchy profiles.
- **additional_insight_to_add:** Final review always checks the canonical guardrails and checklist even after narrow drafting.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** No procedure resolves source examples, presets, target evidence, or newer conventions that disagree.
- **supporting_reason:** Conflict classification prevents silent cherry-picking and hierarchy overreach.
- **counterargument_or_limit:** Many apparent conflicts are scope differences rather than contradictions.
- **assumptions_and_boundaries:** Compare claim, version, canvas, artifact scale, and audience before declaring conflict.
- **revision_decision:** Add classify, decide, test, and record steps.
- **additional_insight_to_add:** Target rendering may override a preset locally without changing the general source.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** Flat citation, newest-wins, and relevance-only alternatives are unexamined.
- **supporting_reason:** Hierarchy improves consistency; recency improves currency; relevance prevents canonical overreach.
- **counterargument_or_limit:** Flat citation preserves neutrality but shifts resolution to every downstream author.
- **assumptions_and_boundaries:** Use frozen hierarchy, question relevance, and artifact evidence together.
- **revision_decision:** Explain the hybrid and reject automatic dominance rules.
- **additional_insight_to_add:** Authority, relevance, and recency are independent axes.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Generic prompts, role inflation, duplicate advice, and example mandates weaken the hierarchy.
- **supporting_reason:** These defects obscure whether the correct source governed the correct claim.
- **counterargument_or_limit:** Excess metadata can duplicate the source map and drift.
- **assumptions_and_boundaries:** Keep only fields that change retrieval, conflict, or verification.
- **revision_decision:** Emphasize primary question, contribution, limit, and disposition.
- **additional_insight_to_add:** A supporting source may constrain the canonical default within its narrower domain.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** Identical questions produce no contrast among source roles.
- **supporting_reason:** Skill-to-grid, example-only copying, and static-width adaptation illustrate hierarchy behavior.
- **counterargument_or_limit:** Examples cannot settle every renderer-specific exception.
- **assumptions_and_boundaries:** Exceptions require target evidence and preserved source representation.
- **revision_decision:** Add source-specific examples and an adaptation record.
- **additional_insight_to_add:** Hierarchy should preserve legitimate divergence rather than enforce identical pages.
### Question 08: How can the important claims be verified?
- **current_section_observation:** Reviewer questions do not prove sources were loaded or conflicts reconciled.
- **supporting_reason:** A compact source ledger can trace constraints, decisions, exceptions, and artifact evidence.
- **counterargument_or_limit:** A large ledger would duplicate the section packet.
- **assumptions_and_boundaries:** Retain concise dispositions and detailed rationale only for material conflict.
- **revision_decision:** Add minimum source and conflict records.
- **additional_insight_to_add:** Verify that high-risk canonical guardrails survive the final page.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** Role assignments are editorial classifications, though source structure supports them strongly.
- **supporting_reason:** The skill is clearly an entrypoint and four references provide focused detail.
- **counterargument_or_limit:** Source files do not declare their own canonical status universally.
- **assumptions_and_boundaries:** Present hierarchy as this reference's corpus organization.
- **revision_decision:** Add a confidence note and task-specific exception scope.
- **additional_insight_to_add:** Hierarchy quality is measured by decision clarity, not label prestige.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** Static roles do not learn from repeated target-surface exceptions.
- **supporting_reason:** Recurring verified divergence can signal a boundary or source refresh need.
- **counterargument_or_limit:** One unusual page should not rewrite general guidance.
- **assumptions_and_boundaries:** Promote changes only after repeated relevant cases or direct source updates.
- **revision_decision:** Add a deliberate hierarchy-refresh trigger.
- **additional_insight_to_add:** Artifact evidence proposes evolution; explicit refresh changes authority.

## Section 013: Theme Specific Artifact
### Question 01: What decision does this reference help make?
- **current_section_observation:** The artifact names a rubric but defines only goal, boundary, and verification fields.
- **supporting_reason:** A concrete run card can hold every layout decision needed to draft, review, reproduce, and hand off a page.
- **counterargument_or_limit:** Oversized templates can become documentation work detached from reader outcomes.
- **assumptions_and_boundaries:** Every field must change structure, portability, review, or maintenance.
- **revision_decision:** Expand into a compact terminal-page run card with a filled example.
- **additional_insight_to_add:** Separate fixed page constraints from provisional wording and local geometry.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** No field order links reader goal to page and local figure selection.
- **supporting_reason:** Audience, task, surface, canvas, system, sections, figures, anchors, labels, and gates form a traceable progression.
- **counterargument_or_limit:** Some values emerge only after a target-width skeleton is tried.
- **assumptions_and_boundaries:** Mark draft values provisional and freeze them during convergence.
- **revision_decision:** Define draft, candidate, accepted, and archived-study states.
- **additional_insight_to_add:** Version the run card with the text so validator evidence never drifts from its candidate.
### Question 03: When does the default work well?
- **current_section_observation:** No fit condition bounds one artifact card.
- **supporting_reason:** It works for one coherent page, one audience contract, and one set of width and style rules.
- **counterargument_or_limit:** Multi-document suites need shared and page-specific records.
- **assumptions_and_boundaries:** Split when pages have independent audiences, canvases, ownership, or acceptance.
- **revision_decision:** Add workload and split criteria.
- **additional_insight_to_add:** One card should correspond to one falsifiable reader journey.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** Generic fields can be populated without a skeleton, target copy, or reader task.
- **supporting_reason:** Requiring artifact evidence prevents administrative completion.
- **counterargument_or_limit:** A rejected study may finish without production-quality page polish.
- **assumptions_and_boundaries:** Studies close with a tested learning and cannot claim delivery readiness.
- **revision_decision:** Add accepted, rejected, and study outcomes.
- **additional_insight_to_add:** Failure is useful when it falsifies a page or pattern choice explicitly.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The section does not compare prose brief, width manifest, review log, or integrated card.
- **supporting_reason:** Separate artifacts are simple, while one card improves traceability and handoff.
- **counterargument_or_limit:** Integration can duplicate content already obvious in the page.
- **assumptions_and_boundaries:** Link stable evidence and summarize decisions instead of embedding outputs.
- **revision_decision:** Use one diffable card with external evidence references.
- **additional_insight_to_add:** The card should preserve semantic choices even if the page later migrates formats.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Missing fields allow width drift, stale validation, ambiguous anchors, and undocumented omissions.
- **supporting_reason:** These failures make accepted layout impossible to reproduce or explain.
- **counterargument_or_limit:** Capturing every transient label length is unnecessary.
- **assumptions_and_boundaries:** Snapshot values when a candidate is saved, rejected materially, or accepted.
- **revision_decision:** Add candidate identity, widths, anchors, target surfaces, and evidence freshness.
- **additional_insight_to_add:** Record longest labels because they often determine shared card geometry.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** Field names lack a completed artifact example.
- **supporting_reason:** A filled 84-column walkthrough card demonstrates sufficient brevity and operational detail.
- **counterargument_or_limit:** A polished example can look mandatory for every tiny figure.
- **assumptions_and_boundaries:** Mark optional fields and supply a reduced small-figure profile.
- **revision_decision:** Add good card plus bad and study contrasts.
- **additional_insight_to_add:** A study can complete after proving two-column comparison cannot fit 72 columns.
### Question 08: How can the important claims be verified?
- **current_section_observation:** Verification field points elsewhere without a reproducibility test.
- **supporting_reason:** Another author should regenerate the intended layout from the card and source text.
- **counterargument_or_limit:** Editorial judgment may vary even with identical geometry.
- **assumptions_and_boundaries:** Reproduction promises mechanics and declared reader tasks, not identical taste.
- **revision_decision:** Add card self-test and second-review evidence.
- **additional_insight_to_add:** A complete card lets a reviewer reach the target state without oral setup.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** Core widths and pattern fields are source-backed; lifecycle and retention are operational additions.
- **supporting_reason:** Local files directly support page system, grids, figures, labels, and validation.
- **counterargument_or_limit:** Exact field set and retention depth depend on collaboration scale.
- **assumptions_and_boundaries:** Require source-backed core and make extended handoff fields conditional.
- **revision_decision:** Label core versus inferred operational fields.
- **additional_insight_to_add:** Reader uncertainty deserves rationale, not artificial scoring precision.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The artifact is framed as a completion form rather than iterative memory.
- **supporting_reason:** A compact card reduces context loss and prevents width or pattern decisions from being rediscovered.
- **counterargument_or_limit:** Presets can encourage repetitive pages and suppress content-specific composition.
- **assumptions_and_boundaries:** Treat retained cards as reproducible anchors, not taste defaults.
- **revision_decision:** Add lifecycle, retention, and format-migration guidance.
- **additional_insight_to_add:** Separating reader intent from ASCII mechanics preserves meaning during migration.

## Section 014: Worked Example Set
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed offers generic good, bad, and borderline usage sentences but no ASCII artifact whose layout can be inspected.
- **supporting_reason:** A worked set should help an author decide how reader questions become page systems, figure grammars, labels, and verification evidence.
- **counterargument_or_limit:** Examples cannot replace analysis of the actual content, audience, and target renderer.
- **assumptions_and_boundaries:** Each example must teach a transferable layout decision while remaining small enough to audit line by line.
- **revision_decision:** Replace abstract usage claims with concrete good, bad, and borderline terminal-page examples plus diagnoses.
- **additional_insight_to_add:** The contrast between artifacts should expose causal layout differences, not merely attach different quality labels.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** There is no default composition for demonstrating the reference's central rules together.
- **supporting_reason:** One end-to-end async request walkthrough can show hierarchy, straight flow, aligned cards, progressive disclosure, and target-width checks in a coherent task.
- **counterargument_or_limit:** A single domain example may imply that operational request flows are the only suitable subject.
- **assumptions_and_boundaries:** Name the domain-specific content separately from the reusable page and figure decisions.
- **revision_decision:** Lead with one annotated 84-column good example, then derive compact anti-example and constrained-width variant.
- **additional_insight_to_add:** Holding the reader task constant across variants makes layout consequences easier to attribute.
### Question 03: When does the default work well?
- **current_section_observation:** The generic good sentence does not identify the learning conditions under which an example is useful.
- **supporting_reason:** A shared scenario works well for onboarding, design review, and regression testing because readers compare the same states and questions.
- **counterargument_or_limit:** Specialized trees, dense matrices, and long editorial pages need additional pattern-specific studies.
- **assumptions_and_boundaries:** Treat the walkthrough as a composition example rather than exhaustive coverage of every diagram family.
- **revision_decision:** State the example's intended teaching scope and point to separate local-pattern substitutions.
- **additional_insight_to_add:** A worked example is strongest when readers can predict which decision changes before seeing the revised artifact.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The bad example criticizes source neglect but does not show a visually plausible layout that fails in use.
- **supporting_reason:** Authors need to recognize deceptive failures such as balanced boxes with crossed flow, clipped labels, duplicated prose, or hidden terminal assumptions.
- **counterargument_or_limit:** Deliberately broken diagrams must remain readable enough for the failure to be diagnosed.
- **assumptions_and_boundaries:** Keep anti-examples short and annotate the defect outside the figure rather than corrupting every dimension.
- **revision_decision:** Include an attractive-but-wrong horizontal flow and explain its width, ordering, and omission failures.
- **additional_insight_to_add:** The most educational bad example often passes a superficial symmetry check while failing the reader's task.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The seed does not compare a complete page, isolated pattern snippets, before-and-after transformations, or renderer screenshots.
- **supporting_reason:** Complete pages teach composition, snippets isolate grammar, transformations show causality, and screenshots reveal surface behavior.
- **counterargument_or_limit:** Including all forms for every pattern would overwhelm the reference and duplicate the local library.
- **assumptions_and_boundaries:** Use the complete page for the main thesis and select smaller forms only when they resolve a distinct ambiguity.
- **revision_decision:** Combine one end-to-end text artifact with a focused before-and-after and a constrained borderline case.
- **additional_insight_to_add:** Example diversity should cover different failure mechanisms rather than cosmetic variants of one drawing.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** No guard prevents a copied example from being unverified, renderer-dependent, semantically stale, or wider than its stated canvas.
- **supporting_reason:** Example code acquires normative authority and can propagate defects more quickly than prose guidance.
- **counterargument_or_limit:** Revalidating every historical example on every renderer may exceed the maintenance budget.
- **assumptions_and_boundaries:** Validate current normative examples mechanically and mark archival studies with their tested surfaces and date.
- **revision_decision:** Attach width, character, fence, target-surface, and reader-task evidence to the example set.
- **additional_insight_to_add:** Longest-label fixtures should be retained because later copy edits can silently invalidate otherwise unchanged geometry.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** Quality categories are asserted without observable layout criteria or reader outcomes.
- **supporting_reason:** A good vertical sequence answers where timeout and retry occur; a bad row forces horizontal scanning; a borderline 72-column version remains correct but reveals less context.
- **counterargument_or_limit:** Compact representations may be preferable when readers already know the domain vocabulary.
- **assumptions_and_boundaries:** Judge each artifact against its declared reader, width, and disclosure contract rather than visual density alone.
- **revision_decision:** Show all three artifacts or compact excerpts and list the precise pass, fail, or conditional evidence.
- **additional_insight_to_add:** Borderline means conditionally fit with an explicit cost, not an artifact awaiting an arbitrary confidence warning.
### Question 08: How can the important claims be verified?
- **current_section_observation:** The examples have no commands, measured dimensions, target-surface observations, or comprehension tasks.
- **supporting_reason:** Automated scans catch syntax and width defects while reader tasks test whether the visual structure communicates the intended answer.
- **counterargument_or_limit:** A successful validator run cannot prove that grouping, emphasis, or omission choices are helpful.
- **assumptions_and_boundaries:** Require both mechanical evidence and at least one question-based editorial review for normative examples.
- **revision_decision:** Specify validator invocation, longest-line report, fence check, target render, and reader-answer record.
- **additional_insight_to_add:** Verification should test the claim each example teaches, such as main-path straightness or state discoverability.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The seed presents its categories as settled despite providing no artifact evidence.
- **supporting_reason:** ASCII-only characters, bounded widths, coherent grammar, and unbroken fences are mechanically knowable; perceived balance and ideal disclosure depth remain contextual.
- **counterargument_or_limit:** Reader tests also vary with domain familiarity and terminal configuration.
- **assumptions_and_boundaries:** Report tested conditions and avoid generalizing a small review beyond comparable readers and surfaces.
- **revision_decision:** Separate deterministic checks, observed reader outcomes, and editorial judgment in each diagnosis.
- **additional_insight_to_add:** Uncertainty becomes actionable when tied to the next discriminating render or reader question.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** Examples are treated as explanatory prose rather than maintained assets with downstream influence.
- **supporting_reason:** Once teams copy a figure, its labels, widths, and connector grammar become de facto templates across documentation.
- **counterargument_or_limit:** Freezing examples too tightly can discourage better compositions for new content.
- **assumptions_and_boundaries:** Preserve semantic assertions and verification fixtures while allowing deliberate visual revision.
- **revision_decision:** Promote normative examples into a small regression corpus governed by the run card and review loop.
- **additional_insight_to_add:** An example set can reveal reference drift when a recommended pattern no longer passes its own acceptance gates.

## Section 015: Outcome Metrics and Feedback Loops
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed names one leading indicator, one failure signal, and one cadence without defining evidence or response thresholds.
- **supporting_reason:** Metrics should help maintainers decide whether a page communicates its reader task, survives target surfaces, and remains economical to change.
- **counterargument_or_limit:** Documentation quality cannot be reduced to a single score without hiding audience and task differences.
- **assumptions_and_boundaries:** Use a small metric portfolio tied to declared claims rather than an aggregate quality index.
- **revision_decision:** Define outcome, conformance, portability, and maintenance measures with corresponding actions.
- **additional_insight_to_add:** A useful metric changes a revision decision; otherwise it is inventory rather than feedback.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** "Apply without hidden context" is directionally useful but not an observable test protocol.
- **supporting_reason:** Ask representative readers to complete explicit locate, explain, and act tasks while recording success, hesitation, wrong turns, and requested context.
- **counterargument_or_limit:** Small reader samples cannot establish population-wide comprehension rates.
- **assumptions_and_boundaries:** Report observations with audience and environment metadata instead of unsupported percentages.
- **revision_decision:** Pair per-candidate reader tasks with automated ASCII, width, fence, table, and target-render checks.
- **additional_insight_to_add:** Reader questions should be authored before the final layout so success criteria cannot be retrofitted to the artifact.
### Question 03: When does the default work well?
- **current_section_observation:** No scope distinguishes new pages, stable runbooks, local figures, or rapidly changing dashboards.
- **supporting_reason:** The paired loop works well when a page has repeatable reader tasks and at least one reproducible rendering surface.
- **counterargument_or_limit:** Ephemeral incident notes may justify only lightweight checks before their value expires.
- **assumptions_and_boundaries:** Scale evidence effort with reuse, operational consequence, audience breadth, and expected lifetime.
- **revision_decision:** Provide small-figure, maintained-page, and high-consequence verification profiles.
- **additional_insight_to_add:** Long-lived low-risk pages can accumulate more maintenance cost than short-lived high-attention artifacts.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The literature-dump warning identifies a prose problem but not metric failure modes.
- **supporting_reason:** Metrics fail when authors optimize line width while readers miss decisions, test only experts, or count questions as defects without diagnosing cause.
- **counterargument_or_limit:** Strict protocols can slow exploratory composition before a stable candidate exists.
- **assumptions_and_boundaries:** Collect formal outcome evidence at candidate state; use informal observations during sketching.
- **revision_decision:** Add anti-Goodhart rules and prohibit acceptance based on mechanical checks alone.
- **additional_insight_to_add:** A mechanically perfect page can be an editorial failure, while a useful study may intentionally fail acceptance.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The section does not compare task observation, surveys, support-question logs, change reviews, or passive telemetry.
- **supporting_reason:** Tasks reveal behavior, surveys reveal perception, question logs reveal recurring gaps, diffs reveal drift, and telemetry may show navigation paths.
- **counterargument_or_limit:** Passive telemetry can create privacy, interpretation, and instrumentation burdens disproportionate to plain-text artifacts.
- **assumptions_and_boundaries:** Prefer direct low-volume evidence unless an existing ethical telemetry system already serves the documentation surface.
- **revision_decision:** Recommend task review and defect logging by default, with surveys and telemetry as conditional supplements.
- **additional_insight_to_add:** Different evidence sources should triangulate a decision rather than be averaged into a misleading score.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** No warning covers stale baselines, changed labels, reviewer familiarity, terminal variance, or unresolved feedback ownership.
- **supporting_reason:** These conditions can make apparent improvement reflect easier tasks, expert memory, or a friendlier renderer instead of a better layout.
- **counterargument_or_limit:** Perfect experimental controls are unrealistic for routine documentation work.
- **assumptions_and_boundaries:** Preserve enough context to compare candidates honestly without presenting the review as laboratory research.
- **revision_decision:** Record candidate identity, task wording, reader profile, target surface, observed defect, owner, and disposition.
- **additional_insight_to_add:** Unassigned feedback is not a loop because no mechanism returns evidence to the artifact.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** The seed supplies no sample metric record or interpretation.
- **supporting_reason:** A concrete record can distinguish "reader found retry route unaided" from "diagram looked clean" and "validator passed."
- **counterargument_or_limit:** One successful reader does not prove the layout works for every expected user.
- **assumptions_and_boundaries:** Treat single observations as evidence for revision, not statistical certification.
- **revision_decision:** Add good, bad, and borderline measurement examples with next actions.
- **additional_insight_to_add:** Borderline evidence should trigger a discriminating follow-up test instead of a vague request for more feedback.
### Question 08: How can the important claims be verified?
- **current_section_observation:** Re-running the repository verifier alone checks structural conformance but not the reference's promised reader outcomes.
- **supporting_reason:** Verification requires traceability from each important claim to a command result, render observation, reader response, or maintenance record.
- **counterargument_or_limit:** Some aesthetic judgments remain irreducible to binary evidence.
- **assumptions_and_boundaries:** Record the reviewer and rationale for judgments while keeping mechanical facts separately reproducible.
- **revision_decision:** Define per-edit, per-candidate, and periodic review loops with retained evidence.
- **additional_insight_to_add:** Feedback closure is verified by the disposition and rerun, not by the existence of a comment.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The seed does not distinguish deterministic validator outcomes from interpretive reader evidence or ecosystem-change risk.
- **supporting_reason:** Bytes, widths, delimiters, and table shapes are directly measurable; comprehension and ideal cadence depend on content and context.
- **counterargument_or_limit:** Even deterministic checks can encode the wrong width or character policy if the run card is stale.
- **assumptions_and_boundaries:** Validate the contract itself during periodic review, not only conformance to its current values.
- **revision_decision:** Label each metric as mechanical, observed, inferred, or externally volatile.
- **additional_insight_to_add:** Confidence attaches to a claim under tested conditions, never to the page as an undifferentiated whole.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** Review cadence is calendar-driven and release-driven but not connected to accumulated layout debt or repeated reader failures.
- **supporting_reason:** Drift signals such as widening labels, recurring clarification, and frequent anchor repair can justify review before an arbitrary date.
- **counterargument_or_limit:** Event-triggered reviews may create noise when every minor edit opens the full process.
- **assumptions_and_boundaries:** Use lightweight checks per edit and escalate only when defined risk or drift triggers fire.
- **revision_decision:** Add a tiered closed loop from detection through ownership, correction, rerun, and retained learning.
- **additional_insight_to_add:** The best long-term outcome may be lower repair cost, because maintainable geometry keeps future clarity improvements affordable.

## Section 016: Completeness Checklist
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed checklist confirms seven topics are present but cannot decide whether the evolved reference is ready for operational use.
- **supporting_reason:** A completeness gate should connect required content to inspectable evidence, failure handling, and the next responsible action.
- **counterargument_or_limit:** A checklist cannot guarantee sound judgment when its items are interpreted mechanically.
- **assumptions_and_boundaries:** Use it as a final release aid after section-level reasoning, not as a substitute for that reasoning.
- **revision_decision:** Reframe completeness as evidence-backed readiness across source, decision, artifact, example, verification, and routing contracts.
- **additional_insight_to_add:** Presence is a weak proxy; closure requires that each promised reader action can actually be performed.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** Existing bullets have no state, evidence location, owner, or failure disposition.
- **supporting_reason:** A pass, fail, or not-applicable result with linked evidence prevents silent interpretation differences and unresolved exceptions.
- **counterargument_or_limit:** Requiring ownership metadata for a small personal sketch may add little value.
- **assumptions_and_boundaries:** Keep the evidence contract mandatory and scale owner or approval detail to collaboration risk.
- **revision_decision:** Organize the gate into invariant structure, operational guidance, artifact evidence, and maintenance readiness.
- **additional_insight_to_add:** Not applicable is valid only when the boundary and consequence are written, not when evidence is inconvenient.
### Question 03: When does the default work well?
- **current_section_observation:** The checklist gives no workload threshold or release moment.
- **supporting_reason:** It works best for maintained references and reusable pages whose claims will guide later authors without immediate access to the original reasoning.
- **counterargument_or_limit:** Early exploration benefits from incomplete studies that should not be forced into release shape.
- **assumptions_and_boundaries:** Apply the full gate at candidate acceptance and a reduced structural gate during drafting.
- **revision_decision:** Distinguish draft progress checks from acceptance completeness.
- **additional_insight_to_add:** Explicit study status preserves useful failures without lowering the accepted-artifact standard.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** Topic-oriented items can all be checked while examples remain misleading, metrics remain unmeasured, or routing remains circular.
- **supporting_reason:** Checkbox theater occurs when evidence quality and reader outcomes are outside the gate.
- **counterargument_or_limit:** Very detailed acceptance wording can become brittle as the reference evolves.
- **assumptions_and_boundaries:** Test stable contracts and evidence types rather than exact paragraph locations or phrasing.
- **revision_decision:** Replace content-presence checks with behavior and traceability checks wherever possible.
- **additional_insight_to_add:** A checklist should fail loudly when it cannot distinguish a placeholder-shaped section from an operational one.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The seed does not compare a single final checklist, per-section gates, automated tests, or reviewer sign-off.
- **supporting_reason:** Final lists support overview, local gates shorten feedback, automation catches syntax, and review handles semantic fitness.
- **counterargument_or_limit:** Duplicating identical criteria at every level increases drift and maintenance burden.
- **assumptions_and_boundaries:** Keep one canonical gate and reference focused subsets during section work.
- **revision_decision:** Combine automated invariants with one skeptical human reread and retained exception decisions.
- **additional_insight_to_add:** Automation should eliminate avoidable review work so human attention can stay on causality and reader fit.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** No item catches self-attested evidence, stale command output, malformed tables, duplicate rationale, unsupported precision, or changed heading order.
- **supporting_reason:** These defects can satisfy superficial topic checks while violating the evolution contract or obscuring maintenance risk.
- **counterargument_or_limit:** The checklist should not duplicate every implementation detail of repository tests.
- **assumptions_and_boundaries:** Name critical invariants and point to authoritative commands for their exact mechanics.
- **revision_decision:** Add freshness, uniqueness, structural integrity, source fidelity, and skeptical-reread gates.
- **additional_insight_to_add:** Evidence freshness should be tied to candidate identity because a passing result from another revision is functionally missing.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** The checklist itself has no examples showing acceptable evidence or invalid completion.
- **supporting_reason:** A good item cites a verifier result and reader record; a bad item says "looks fine"; a borderline item documents an unresolved renderer exception.
- **counterargument_or_limit:** Examples can age when command names or repository layout change.
- **assumptions_and_boundaries:** Illustrate evidence qualities while sourcing executable syntax from the current verification section.
- **revision_decision:** Add concise completion and exception examples after the gate.
- **additional_insight_to_add:** Borderline readiness is a blocked decision with an owner, not a lower undocumented pass threshold.
### Question 08: How can the important claims be verified?
- **current_section_observation:** None of the seven bullets states how a reviewer proves completion.
- **supporting_reason:** Mapping each gate to packet counts, heading comparison, section-length checks, validators, render evidence, or reader tasks makes completion independently auditable.
- **counterargument_or_limit:** Manual evidence links may break when artifacts move.
- **assumptions_and_boundaries:** Prefer stable repository paths and regenerate reports at acceptance.
- **revision_decision:** Include a minimum evidence bundle and require all blocking gates to pass.
- **additional_insight_to_add:** The final verifier should report counts and failed identities, not only a process exit code.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The current list treats all checks as equivalent despite differing determinism.
- **supporting_reason:** Counts, order, encoding, fences, tables, and placeholders are deterministic, while detail sufficiency and reader value require judgment.
- **counterargument_or_limit:** Deterministic length expansion can still reward verbosity without substance.
- **assumptions_and_boundaries:** Pair quantitative expansion with a skeptical qualitative reread for filler and unsupported claims.
- **revision_decision:** Mark mechanical gates and editorial gates separately while requiring both.
- **additional_insight_to_add:** Uncertainty belongs in the evidence record when it affects release, not hidden behind a completed checkbox.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The checklist is static and does not feed defects back into reference maintenance.
- **supporting_reason:** Repeated failures reveal unclear guidance, weak defaults, or missing automation that should change the reference itself.
- **counterargument_or_limit:** One unusual failure may reflect a special artifact rather than a general gap.
- **assumptions_and_boundaries:** Promote checklist changes after recurring evidence or a high-consequence escape.
- **revision_decision:** Add a feedback rule for evolving gates without weakening prior invariants silently.
- **additional_insight_to_add:** A maintained completeness gate becomes an executable index of the reference's actual promises.

## Section 017: Adjacent Reference Routing
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed routes by generic words such as visual, ASCII, diagram, and layout without naming a concrete destination or discriminating trigger.
- **supporting_reason:** Routing should decide whether raw monospace text is the primary artifact or whether another medium better satisfies interaction, argument, interface, art, or spatial needs.
- **counterargument_or_limit:** A project may need both a terminal summary and a richer companion rather than one exclusive route.
- **assumptions_and_boundaries:** Route the primary deliverable by its hardest reader and surface constraint, then define companion artifacts explicitly.
- **revision_decision:** Replace circular categories with a concrete adjacent-reference matrix and hybrid rules.
- **additional_insight_to_add:** Medium is only one signal; reader action and information topology often determine the better destination.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** "Use visual, ASCII, HTML, or writing references when the output medium is fixed" does not say when this reference remains primary.
- **supporting_reason:** Stay here when the artifact must remain legible, copyable, diffable, and useful as raw fixed-width text without a rendering runtime.
- **counterargument_or_limit:** Markdown source may still be rendered, and a browser artifact can also expose downloadable plain text.
- **assumptions_and_boundaries:** Test the required lowest-capability surface rather than inferring format from the authoring file extension.
- **revision_decision:** Make raw-text survivability and terminal scanning the default adoption test.
- **additional_insight_to_add:** The weakest required surface sets the baseline, while richer surfaces may add nonessential enhancement.
### Question 03: When does the default work well?
- **current_section_observation:** No positive routing examples cover logs, runbooks, command help, reviews, or source-controlled explanations.
- **supporting_reason:** These contexts reward stable alignment, low tooling dependence, grep-friendly labels, and meaningful plain-text fallback.
- **counterargument_or_limit:** Dense tables or highly connected graphs can exceed the cognitive and geometric capacity of a terminal page.
- **assumptions_and_boundaries:** Keep ASCII primary only while the reader task remains answerable inside the declared canvas.
- **revision_decision:** List terminal-native fit signals and a capacity stop rule.
- **additional_insight_to_add:** Distribution convenience is not enough if compression removes the relationships readers need.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The three adjacent labels do not identify interaction, accessibility, responsive layout, data density, animation, or 3D as routing failures.
- **supporting_reason:** Those needs depend on semantics and behaviors that static character geometry cannot provide reliably.
- **counterargument_or_limit:** A small ASCII overview may still improve fallback, logs, or review even when the primary artifact is richer.
- **assumptions_and_boundaries:** Preserve a companion summary only when it has its own reader task and maintenance owner.
- **revision_decision:** Add explicit avoid triggers and companion-only use cases.
- **additional_insight_to_add:** A fallback that silently omits critical state is worse than an honest route to the required medium.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The seed omits concrete choices among HTML explainers, argument writing, product UI design, generative art, and Three.js visualization.
- **supporting_reason:** Each adjacent reference optimizes a different primary outcome and incurs different runtime, maintenance, and accessibility costs.
- **counterargument_or_limit:** Filename-level routing does not guarantee the neighboring reference currently covers every specialized requirement.
- **assumptions_and_boundaries:** Open and verify the destination's scope before transferring the task.
- **revision_decision:** Name exact repository paths with trigger, gain, and retained ASCII role.
- **additional_insight_to_add:** Routing decisions should preserve useful analysis artifacts even when the final medium changes.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Generic routing can loop back to the same method, split ownership, duplicate content, or choose technology before clarifying the reader task.
- **supporting_reason:** These failures create conflicting artifacts and make neither source authoritative.
- **counterargument_or_limit:** Some duplication is necessary for accessibility, offline use, or incident resilience.
- **assumptions_and_boundaries:** Duplicate only the stable semantic core and designate a source of truth for volatile detail.
- **revision_decision:** Add anti-loop, authority, synchronization, and accessibility checks.
- **additional_insight_to_add:** Every hybrid route needs a declared degradation contract describing what remains usable when the rich surface fails.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** No route demonstrates how the same task changes destination under different constraints.
- **supporting_reason:** A deployment flow belongs here for terminal review, in an HTML explainer for interactive drill-down, and in Minto guidance when the central problem is an approval argument.
- **counterargument_or_limit:** A real deliverable may combine all three needs for different audiences.
- **assumptions_and_boundaries:** Choose one primary artifact per audience and connect companions through explicit routes.
- **revision_decision:** Add contrasting route examples and one hybrid boundary case.
- **additional_insight_to_add:** Borderline routing should identify which constraint would flip the decision, such as required keyboard exploration or offline incident use.
### Question 08: How can the important claims be verified?
- **current_section_observation:** The adjacent labels provide no test that the destination exists, fits the task, or improves the result.
- **supporting_reason:** A route is auditable when its path resolves, its scope was read, and a small artifact probe satisfies the constraint that forced departure.
- **counterargument_or_limit:** Building full prototypes for every possible destination would waste effort.
- **assumptions_and_boundaries:** Use the cheapest discriminating probe, such as raw-text fallback, keyboard traversal, responsive resize, or data-density sketch.
- **revision_decision:** Require path, scope, constraint, probe, and ownership evidence for material reroutes.
- **additional_insight_to_add:** Verify the reason for leaving ASCII, not merely the technical ability to produce another format.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The seed presents adjacent categories without acknowledging that neighboring files and capabilities may evolve.
- **supporting_reason:** Current repository paths are directly inspectable, while the best medium for a mixed audience remains a design judgment.
- **counterargument_or_limit:** Tool availability, renderer support, and accessibility behavior can change after this reference is accepted.
- **assumptions_and_boundaries:** Recheck volatile capabilities at use time and keep routing triggers technology-neutral where possible.
- **revision_decision:** Separate stable task constraints from current destination inventory.
- **additional_insight_to_add:** Confidence in the route rises when multiple constraints point to the same medium, not when a filename sounds relevant.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** One-way routing ignores what learned page structure can contribute to a richer artifact.
- **supporting_reason:** Reader questions, section jobs, omission routes, and verified labels remain useful inputs to HTML, UI, visual, or presentation work.
- **counterargument_or_limit:** Carrying fixed-width geometry into responsive design can constrain the new medium unnecessarily.
- **assumptions_and_boundaries:** Transfer semantic structure and evidence, then redesign geometry for the destination.
- **revision_decision:** Add a handoff packet and reverse-route rule for terminal fallbacks.
- **additional_insight_to_add:** Good routing changes representation while preserving intent, traceability, and known failure boundaries.

## Section 018: Workload Model
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed offers one bounded-capacity row but does not explain how to size, split, or stage an ASCII layout task.
- **supporting_reason:** A workload model should decide whether the work is one local figure, one composed terminal page, or a coordinated artifact suite.
- **counterargument_or_limit:** Apparent size before drafting may change when real labels and target surfaces are tested.
- **assumptions_and_boundaries:** Treat initial sizing as a hypothesis that must survive an early copy-and-canvas probe.
- **revision_decision:** Define workload profiles and observable split triggers rather than one fixed artifact quota.
- **additional_insight_to_add:** Semantic independence is a better split axis than equal line counts or box counts.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** "One artifact family, three representative variants" is too rigid to guide common page work.
- **supporting_reason:** The smallest unit with one coherent reader journey, one canvas contract, one owner, and one acceptance packet minimizes coordination while preserving completeness.
- **counterargument_or_limit:** Shared visual vocabulary and repeated structures may still justify planning several pages together.
- **assumptions_and_boundaries:** Share stable conventions across a suite but keep page-specific reader and evidence contracts separate.
- **revision_decision:** Default to one independently verifiable page or figure, then split when a contract diverges.
- **additional_insight_to_add:** A workload is bounded when its acceptance can fail without making unrelated artifacts indeterminate.
### Question 03: When does the default work well?
- **current_section_observation:** Primary usage surface combines creative, diagram, media, and generation work without matching capacity to task shape.
- **supporting_reason:** A single unit works well when readers follow one main question, labels fit one width regime, and local figures share a reading order.
- **counterargument_or_limit:** One page may contain several figure grammars if section jobs remain distinct and transitions are clear.
- **assumptions_and_boundaries:** Grammar diversity alone does not force a split; competing journeys and incompatible canvases do.
- **revision_decision:** Add cohesion tests for reader question, surface, vocabulary, and revision ownership.
- **additional_insight_to_add:** Strong global rhythm can make heterogeneous local figures easier to maintain than several loosely related files.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The seed says to split when a capacity boundary is exceeded but does not define symptoms.
- **supporting_reason:** Repeated crossovers, unreadable compression, independent audiences, incompatible target widths, and unrelated acceptance criteria reveal overloaded scope.
- **counterargument_or_limit:** Splitting too early can force readers to reconstruct a relationship that one page would show naturally.
- **assumptions_and_boundaries:** Preserve an overview and explicit routes when separation would hide the system-level question.
- **revision_decision:** Name overload and fragmentation signals with corrective choices.
- **additional_insight_to_add:** If every split needs extensive duplicated context, the proposed boundaries are probably wrong.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** No comparison exists among a compact figure, composed page, linked series, dashboard, or richer-medium route.
- **supporting_reason:** Smaller units reduce reflow, pages preserve narrative, series isolate ownership, dashboards support repeated scanning, and richer media handles interaction or density.
- **counterargument_or_limit:** Multiple artifacts add navigation, synchronization, and source-of-truth costs.
- **assumptions_and_boundaries:** Choose the least fragmented form that meets the narrowest required surface and reader task.
- **revision_decision:** Add profile selection and escalation guidance.
- **additional_insight_to_add:** The cost of a split includes every future semantic update that must cross the new boundary.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Workload pressure ignores longest labels, relationship density, copy volatility, reviewer count, surface variance, and evidence collection.
- **supporting_reason:** These factors drive actual geometry and coordination more than nominal section count.
- **counterargument_or_limit:** Detailed estimation can become expensive before the content stabilizes.
- **assumptions_and_boundaries:** Sample the hardest labels, densest relationship, narrowest surface, and most consequential reader task first.
- **revision_decision:** Add early pressure probes and rescoping triggers to the run card.
- **additional_insight_to_add:** Verification effort is part of workload, not a final overhead applied after composition.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** The workload table provides abstract dimensions but no sizing examples.
- **supporting_reason:** A four-state lifecycle can be one figure, an incident walkthrough can be one page, and a multi-team platform guide usually needs an overview plus owned pages.
- **counterargument_or_limit:** Domain complexity and audience familiarity can shift each example across profiles.
- **assumptions_and_boundaries:** Diagnose examples by contract cohesion and tested fit, not by their subject names.
- **revision_decision:** Add compact, page, suite, overloaded, and borderline cases.
- **additional_insight_to_add:** A borderline page should be split only after a probe shows that progressive disclosure cannot preserve its main journey.
### Question 08: How can the important claims be verified?
- **current_section_observation:** The pressure points ask whether guidance changes action but offer no reproducible capacity test.
- **supporting_reason:** Skeletons populated with longest labels at the narrowest canvas reveal compression, crossings, and routing needs before polish.
- **counterargument_or_limit:** Early skeletons may overstate pressure if labels later shorten legitimately.
- **assumptions_and_boundaries:** Use realistic source terminology and record any semantic cost of abbreviation.
- **revision_decision:** Require a capacity probe, split rationale, per-unit acceptance map, and whole-suite navigation check.
- **additional_insight_to_add:** The probe should test the densest local region and the global reading path separately.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The bounded model reads as a fixed capacity claim without evidence for universal numbers.
- **supporting_reason:** Canvas width, label lengths, ownership, and target surfaces are observable; optimal artifact boundaries remain contextual.
- **counterargument_or_limit:** Even observed inputs can change during review or after localization.
- **assumptions_and_boundaries:** Retest sizing when material copy, audience, or surface contracts change.
- **revision_decision:** Remove unsupported quotas and present profiles as operational heuristics with evidence triggers.
- **additional_insight_to_add:** Uncertainty should reserve room for rescoping rather than inflate buffers with arbitrary precision.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The workload model treats splitting as a one-time planning decision.
- **supporting_reason:** Layout debt and changing readers can make a once-coherent page require extraction, or make fragmented pages worth recombining.
- **counterargument_or_limit:** Frequent restructuring damages stable links and reader memory.
- **assumptions_and_boundaries:** Rescope only when measured comprehension, maintenance, or surface failures exceed migration costs.
- **revision_decision:** Add ongoing split and recombination review tied to feedback signals.
- **additional_insight_to_add:** Workload boundaries are maintainable interfaces whose quality appears in future change propagation.

## Section 019: Reliability Target
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed lists four thresholds but does not define the reliability claim that the reference and its artifacts are expected to uphold.
- **supporting_reason:** Reliability here means repeatably routing the right task, preserving evidence boundaries, rendering under declared contracts, and recovering clearly when a check fails.
- **counterargument_or_limit:** Editorial references cannot promise identical comprehension across all readers and environments.
- **assumptions_and_boundaries:** State reliability per claim, audience, surface, and candidate rather than as a universal page score.
- **revision_decision:** Define a layered target covering source integrity, decision fitness, artifact conformance, reader outcome, and recovery.
- **additional_insight_to_add:** Reliability is an evidence chain from source to reader action, not merely the absence of malformed text.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** One hundred percent and zero-defect rows express release invariants, while the 18-of-20 decision sample lacks rationale.
- **supporting_reason:** Enumerated structural or attribution defects can be required to reach zero, but reader sampling must be scaled to consequence and reported without invented statistical authority.
- **counterargument_or_limit:** A minimum sample can still enforce discipline in a large standardized evaluation program.
- **assumptions_and_boundaries:** Use numeric sample thresholds only when a documented protocol, population, and consequence model justify them.
- **revision_decision:** Keep exact invariants for enumerable defects and use predeclared risk-based task review for interpretation.
- **additional_insight_to_add:** Critical misroutes should block acceptance regardless of a favorable aggregate percentage.
### Question 03: When does the default work well?
- **current_section_observation:** The seed does not distinguish stable local references, volatile renderer behavior, or high-consequence operational pages.
- **supporting_reason:** Layered targets work when each claim has an owner, observable failure signal, and evidence collection path.
- **counterargument_or_limit:** Tiny disposable figures may not justify retained multi-layer reliability records.
- **assumptions_and_boundaries:** Apply deterministic conformance everywhere and add reader, surface, and recovery evidence according to reuse and consequence.
- **revision_decision:** Define small, maintained, and high-consequence reliability profiles.
- **additional_insight_to_add:** Volatile dependencies need freshness targets, while stable geometry needs regression targets.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** Fixed percentages can conceal severity, cherry-picked tasks, repeated reviewers, and untested target surfaces.
- **supporting_reason:** Aggregates appear reassuring even when one safety-critical route or narrow terminal fails.
- **counterargument_or_limit:** Per-defect severity classification adds editorial judgment and review cost.
- **assumptions_and_boundaries:** Define critical failures before testing and retain the sampled tasks and environments.
- **revision_decision:** Prohibit aggregate passing when any predeclared critical contract fails.
- **additional_insight_to_add:** A reliability target without a failure taxonomy encourages metric gaming.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The table does not compare hard invariants, service-level objectives, sampled evaluations, checklists, or continuous defect tracking.
- **supporting_reason:** Invariants fit syntax, objectives fit repeated operations, samples fit comprehension, checklists fit judgment, and defect logs reveal drift.
- **counterargument_or_limit:** Too many parallel mechanisms can make a small reference harder to operate than its artifacts.
- **assumptions_and_boundaries:** Select the cheapest mechanism that can falsify each material claim.
- **revision_decision:** Map reliability layers to evidence types rather than forcing every claim into a percentage.
- **additional_insight_to_add:** Evidence diversity is useful only when every source can trigger a concrete response.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** No rule addresses stale evidence, changed denominators, reruns after edits, correlated reviewers, or partial-surface success.
- **supporting_reason:** These defects make a reported target incomparable with the accepted candidate or intended population.
- **counterargument_or_limit:** Capturing full experimental metadata is excessive for routine page review.
- **assumptions_and_boundaries:** Retain candidate, task, audience, surface, date, result, severity, and disposition as the minimum useful context.
- **revision_decision:** Add freshness, identity, severity, and rerun requirements.
- **additional_insight_to_add:** A passing result expires when a material label, canvas, renderer, or source contract changes.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** Threshold rows provide no sample reliability statement with supporting evidence.
- **supporting_reason:** Concrete examples show the difference between an enumerated zero-defect gate, an observed reader result, and an arbitrary success claim.
- **counterargument_or_limit:** One reference's example severity may not transfer to another operational domain.
- **assumptions_and_boundaries:** Tie examples to ASCII layout consequences such as wrong routing, clipped state, or stale evidence.
- **revision_decision:** Add good, bad, and borderline target declarations and interpretations.
- **additional_insight_to_add:** Borderline evidence should narrow the claim or expand the test, never be rounded into success.
### Question 08: How can the important claims be verified?
- **current_section_observation:** Evidence methods are broad review instructions without candidate identity, commands, or retained result schema.
- **supporting_reason:** A reliability report should enumerate invariant checks, bind render observations to surfaces, and trace reader tasks through dispositions and reruns.
- **counterargument_or_limit:** The exact repository verifier may evolve independently of this prose.
- **assumptions_and_boundaries:** Point to the current verification section for syntax while keeping required evidence semantics stable.
- **revision_decision:** Define a candidate-bound reliability packet and acceptance algorithm.
- **additional_insight_to_add:** Verification completeness can be checked by missing claim-to-evidence links before evaluating outcomes.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The table presents all thresholds with equal certainty despite different evidence bases.
- **supporting_reason:** Heading order, encoding, widths, and attribution labels are enumerable; route correctness and comprehension depend on reviewer judgment and task coverage.
- **counterargument_or_limit:** Even deterministic policy can be wrong if the declared canvas or source hierarchy is inappropriate.
- **assumptions_and_boundaries:** Review contract validity separately from conformance and disclose untested populations.
- **revision_decision:** Label targets as invariant, observed, inferred, or volatile.
- **additional_insight_to_add:** High confidence in conformance should not be misreported as high confidence in reader usefulness.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** Reliability is framed as a final threshold rather than a property designed into page structure and workflow.
- **supporting_reason:** Stable grids, bounded vocabulary, run-card identity, and early probes reduce both failure incidence and diagnosis cost.
- **counterargument_or_limit:** Excessive defensive structure can reduce expressiveness or slow low-risk work.
- **assumptions_and_boundaries:** Increase controls with consequence, volatility, and reuse rather than applying one heavy process universally.
- **revision_decision:** Connect reliability targets to workload profiles and feedback-triggered review.
- **additional_insight_to_add:** Fast, localized recovery is a reliability outcome because failures are inevitable as copy and renderers evolve.

## Section 020: Failure Mode Table
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed lists four broad failures but only one directly addresses rendered layout, and it assumes pixel inspection rather than raw-text behavior.
- **supporting_reason:** A failure table should help authors classify a signal by source, decision, content, geometry, encoding, rendering, comprehension, or maintenance stage.
- **counterargument_or_limit:** Stage labels can overlap because one stale source may later appear as a misleading diagram.
- **assumptions_and_boundaries:** Classify by the earliest controllable cause while retaining downstream symptoms.
- **revision_decision:** Replace generic rows with ASCII-specific failure modes, detection signals, containment, repair, and rerun gates.
- **additional_insight_to_add:** Earliest-cause classification reduces cosmetic fixes that leave the actual defect active.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** Required mitigation actions are broad and omit immediate containment or proof of recovery.
- **supporting_reason:** Stop propagation, preserve the failing candidate, repair the smallest responsible layer, and rerun affected upstream and downstream checks.
- **counterargument_or_limit:** Preserving every trivial draft failure creates noise and storage burden.
- **assumptions_and_boundaries:** Retain failures that reach candidate state, recur, or reveal a reference weakness.
- **revision_decision:** Give each row signal, likely cause, containment, correction, and recovery evidence.
- **additional_insight_to_add:** A mitigation is incomplete until the artifact no longer reproduces the original reader-visible symptom.
### Question 03: When does the default work well?
- **current_section_observation:** The table does not state whether it is for drafting, review, maintenance, or incident response.
- **supporting_reason:** Stage-based diagnosis works across those phases when candidate identity and target-surface contracts are known.
- **counterargument_or_limit:** In early sketching, exact root-cause recording may interrupt useful exploration.
- **assumptions_and_boundaries:** Use lightweight classification during sketches and full records for accepted, shared, or recurring artifacts.
- **revision_decision:** Define phase-scaled failure handling.
- **additional_insight_to_add:** The same symptom can deserve different urgency depending on whether the page is exploratory or operational.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** Generic rows encourage authors to select the closest label without testing competing causes.
- **supporting_reason:** Premature classification can blame the renderer for source tabs, blame copy for a wrong canvas, or blame readers for ambiguous arrows.
- **counterargument_or_limit:** Exhaustive root-cause analysis is disproportionate for obvious low-risk defects.
- **assumptions_and_boundaries:** Test the cheapest plausible causes first and escalate when the symptom persists or consequence is high.
- **revision_decision:** Add differential-diagnosis questions and an unknown category with a bounded probe.
- **additional_insight_to_add:** "Unknown" with a discriminating experiment is safer than confident misclassification.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The seed does not compare a failure table with checklist prevention, FMEA scoring, mutation tests, or incident retrospectives.
- **supporting_reason:** Checklists prevent known defects, tables support diagnosis, FMEA prioritizes consequence, mutations test detectors, and retrospectives evolve controls.
- **counterargument_or_limit:** Formal severity scoring can create unsupported arithmetic for documentation defects.
- **assumptions_and_boundaries:** Use qualitative consequence classes unless historical data supports calibrated scoring.
- **revision_decision:** Keep the table operational and pair it with focused mutation probes and feedback review.
- **additional_insight_to_add:** Prevention and diagnosis artifacts should share failure names so observed escapes improve the correct gate.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Missing ASCII-specific risks include wrong figure grammar, label overflow, grid drift, connector ambiguity, Unicode leakage, tab expansion, fence breakage, and stale omission routes.
- **supporting_reason:** These defects either change meaning, destroy portability, or make the artifact impossible to maintain reliably.
- **counterargument_or_limit:** Not every spacing variation is a material failure.
- **assumptions_and_boundaries:** Treat variation as failure when it violates the declared contract or reader task.
- **revision_decision:** Add high-signal modes across semantic, geometric, syntactic, and lifecycle boundaries.
- **additional_insight_to_add:** Meaning-changing connector defects deserve higher priority than harmless visual asymmetry.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** No row demonstrates a complete diagnosis from observed signal through rerun.
- **supporting_reason:** A clipped label traced to stale width assumptions differs from one traced to an unexpected renderer font or tab.
- **counterargument_or_limit:** Compact examples cannot cover all interacting causes.
- **assumptions_and_boundaries:** Show one semantic, one portability, and one maintenance diagnosis with explicit uncertainty.
- **revision_decision:** Add example failure records and a borderline unknown-cause probe.
- **additional_insight_to_add:** Good diagnosis names what evidence would falsify the proposed cause.
### Question 08: How can the important claims be verified?
- **current_section_observation:** Mitigations are stated without tests that detectors fire or repairs remove symptoms.
- **supporting_reason:** Controlled mutations such as a long label, tab, Unicode border, reversed arrow, broken fence, or stale route can exercise the gate chain.
- **counterargument_or_limit:** Mutation coverage does not prove detection of every natural defect.
- **assumptions_and_boundaries:** Select mutations from high-consequence and previously escaped failure modes.
- **revision_decision:** Add detector tests, target render reproduction, reader-task rerun, and regression retention.
- **additional_insight_to_add:** A detector that catches only a synthetic form should not be credited for broader failure coverage.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The table states likely triggers without confidence or alternative-cause boundaries.
- **supporting_reason:** Character, width, whitespace, and fence defects are directly observable; semantic ambiguity and reader overload require interpretation.
- **counterargument_or_limit:** Observable syntax defects may still have multiple upstream process causes.
- **assumptions_and_boundaries:** Separate symptom certainty from root-cause confidence and record unresolved alternatives.
- **revision_decision:** Add confidence-aware diagnosis language and avoid authoritative trigger claims without tests.
- **additional_insight_to_add:** High symptom certainty can coexist with low cause certainty, so containment should not wait for perfect diagnosis.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** Failure modes are independent rows and do not expose cascades or control weaknesses.
- **supporting_reason:** Source drift can lengthen labels, cause reflow, obscure branches, and invalidate reader evidence in one chain.
- **counterargument_or_limit:** Modeling every cascade would make the table unusable.
- **assumptions_and_boundaries:** Document recurring or high-consequence chains and keep ordinary rows concise.
- **revision_decision:** Add cascade notes, leading indicators, and gate-evolution triggers.
- **additional_insight_to_add:** Repeated downstream repairs often signal that an earlier contract or probe is missing.

## Section 021: Retry Backpressure Guidance
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed says to classify failures before retrying but does not define which next action follows each class.
- **supporting_reason:** Retry guidance should decide whether to rerun unchanged, refresh evidence, add context, revise the artifact, narrow scope, route elsewhere, or escalate.
- **counterargument_or_limit:** Some commands fail nondeterministically and justify a simple rerun before deeper diagnosis.
- **assumptions_and_boundaries:** Permit an unchanged retry only for a recorded transient mechanism with bounded attempts.
- **revision_decision:** Define a failure-to-action matrix and require a changed condition for ordinary retries.
- **additional_insight_to_add:** A retry is an experiment only when its changed variable and expected signal are explicit.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** One bounded external-evidence refresh is specified, but geometry, renderer, comprehension, and ownership failures lack defaults.
- **supporting_reason:** Preserve the failing candidate, stop dependent work, apply the smallest causal correction, and rerun the failed gate plus invalidated downstream checks.
- **counterargument_or_limit:** Very small edits may make full evidence preservation feel disproportionate.
- **assumptions_and_boundaries:** Always retain candidate identity; scale detailed failure records to recurrence and consequence.
- **revision_decision:** Make stop, change, retry, compare, and either accept or escalate the standard loop.
- **additional_insight_to_add:** Preserving the pre-retry artifact makes improvement falsifiable instead of anecdotal.
### Question 03: When does the default work well?
- **current_section_observation:** Transient, stale, missing-context, and contradiction categories are named without fit examples.
- **supporting_reason:** Bounded retries work for temporary command failures, clearly stale source snapshots, omitted labels, or a localized width correction.
- **counterargument_or_limit:** Even localized changes can invalidate reader evidence when they alter order or emphasis.
- **assumptions_and_boundaries:** Map the repair's blast radius before choosing which checks to rerun.
- **revision_decision:** Add fit cases and downstream-evidence rules for each retry class.
- **additional_insight_to_add:** Retry scope should follow semantic impact, not the number of edited lines.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The seed does not explicitly forbid repeating generation with identical constraints or retrying through a true source contradiction.
- **supporting_reason:** Unchanged attempts consume time, produce variant noise, and can overwrite evidence without resolving the cause.
- **counterargument_or_limit:** Stochastic generators may yield useful variation under identical prompts during deliberate exploration.
- **assumptions_and_boundaries:** Exploration requires a fixed scoring contract and variant budget separate from failure recovery.
- **revision_decision:** Stop automatic retries on repeated unchanged failures, contradictions, wrong-medium constraints, or ownership conflicts.
- **additional_insight_to_add:** Random variation is not backpressure-aware recovery unless selection criteria prevent drift.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** Human escalation and narrower references are mentioned, while rollback, defer, route, isolate, and accept-known-limit choices are absent.
- **supporting_reason:** Different failures call for restoring a known candidate, postponing volatile evidence, switching medium, reducing scope, or documenting a bounded limitation.
- **counterargument_or_limit:** Too many branches can make operators hesitate during simple failures.
- **assumptions_and_boundaries:** Present a short priority order and reserve specialized actions for diagnosed conditions.
- **revision_decision:** Add an action ladder from local correction through rollback, narrowing, routing, and escalation.
- **additional_insight_to_add:** The safest next action often minimizes irreversible change while increasing diagnostic information.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Checkpoint guidance is batch-oriented and may still permit unsaved sections, stale journals, concurrent ownership, or broad rewrites after failure.
- **supporting_reason:** These behaviors increase lost work, conflict risk, and uncertainty about which candidate evidence covers.
- **counterargument_or_limit:** Excessively frequent journaling can interrupt flow if it duplicates saved artifacts.
- **assumptions_and_boundaries:** Save each complete section and journal at meaningful milestones, failures, and phase transitions.
- **revision_decision:** Add persistence, exclusive ownership, candidate identity, and no-destructive-recovery rules.
- **additional_insight_to_add:** Filesystem persistence is a backpressure mechanism because it limits the amount of unverified state at risk.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** The seed has no retry trace showing classification, changed condition, or escalation.
- **supporting_reason:** A width failure repaired by rewrapping differs from a second identical generation attempt or a renderer contradiction requiring reroute.
- **counterargument_or_limit:** Example actions can appear universal despite differing consequences.
- **assumptions_and_boundaries:** Tie each example to its failure signal, contract, and permitted retry budget.
- **revision_decision:** Add successful, wasteful, and uncertain retry records.
- **additional_insight_to_add:** Borderline cases should use a probe that separates transient failure from persistent incompatibility.
### Question 08: How can the important claims be verified?
- **current_section_observation:** No evidence schema proves that backpressure stopped work or that the retry changed the failed condition.
- **supporting_reason:** A retry record can compare candidate identities, failure output, classification, changed input, rerun result, and downstream checks.
- **counterargument_or_limit:** Detailed traces for every command rerun can become noisy.
- **assumptions_and_boundaries:** Retain traces for blocking, recurring, externally volatile, or high-consequence retries.
- **revision_decision:** Define a compact retry packet and closure criteria.
- **additional_insight_to_add:** Successful command output does not close recovery if invalidated reader or render evidence remains stale.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** Failure categories appear discrete even though symptoms may not reveal whether evidence is stale, context is missing, or guidance contradicts itself.
- **supporting_reason:** Command status and candidate differences are observable, while causal classification can remain provisional.
- **counterargument_or_limit:** Waiting for certainty can block low-risk corrective action unnecessarily.
- **assumptions_and_boundaries:** Use reversible probes under uncertainty and escalate before irreversible or broad changes.
- **revision_decision:** Mark classifications provisional until discriminating evidence supports them.
- **additional_insight_to_add:** Backpressure manages uncertainty by reducing change rate while information quality rises.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The guidance focuses on individual retry events rather than queue behavior across long-running or distributed work.
- **supporting_reason:** Continuing new sections while an earlier gate is red compounds invalid assumptions and enlarges recovery scope.
- **counterargument_or_limit:** Independent work can proceed safely when it shares no failed contract or files.
- **assumptions_and_boundaries:** Block only dependent work and preserve explicit ownership boundaries for independent tasks.
- **revision_decision:** Add dependency-aware backpressure and phase-transition checkpoints.
- **additional_insight_to_add:** Effective backpressure limits both attempt count and the amount of downstream state built on an unresolved premise.

## Section 022: Observability Checklist
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed lists facts to record but does not define which evidence is necessary to reconstruct an ASCII artifact decision.
- **supporting_reason:** Observability should let a later reviewer identify the candidate, loaded and skipped sources, governing contracts, checks, decisions, unresolved risks, and refresh triggers.
- **counterargument_or_limit:** Recording every drafting action would obscure material decisions and increase review cost.
- **assumptions_and_boundaries:** Retain events that change authority, geometry, acceptance, recovery, or future maintenance.
- **revision_decision:** Define a minimal candidate-bound evidence record and phase-specific observation points.
- **additional_insight_to_add:** Observability is sufficient when another reviewer can reproduce the decision without replaying the full conversation.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** Exact commands and reviewer questions are requested, but no shared record shape ties them to a revision or result.
- **supporting_reason:** A compact event with candidate identity, event type, input contract, evidence summary, decision, owner, and next trigger supports comparison and handoff.
- **counterargument_or_limit:** A rigid schema may feel heavy for a single local figure.
- **assumptions_and_boundaries:** Use a reduced record for disposable sketches and the full schema for maintained or shared pages.
- **revision_decision:** Make structured summaries the default and link bulky outputs externally.
- **additional_insight_to_add:** Candidate identity is the join key that prevents individually valid observations from describing different artifacts.
### Question 03: When does the default work well?
- **current_section_observation:** The checklist does not distinguish solo drafting from distributed, long-running, or operational maintenance workflows.
- **supporting_reason:** Structured evidence is most valuable when context will be compacted, ownership changes, target surfaces vary, or accepted pages evolve over time.
- **counterargument_or_limit:** Short-lived exploratory work can cost more to instrument than to recreate.
- **assumptions_and_boundaries:** Scale retention with expected reuse, consequence, volatility, and number of reviewers.
- **revision_decision:** Provide sketch, candidate, accepted, and maintenance observation profiles.
- **additional_insight_to_add:** Context-loss risk, not artifact length alone, determines observability value.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** Raw transcript dumps are discouraged, yet percentile timing fields can still produce high-volume or misleading records without a protocol.
- **supporting_reason:** Unbounded logs, vanity timing, sensitive content, and evidence without dispositions make review slower without improving decisions.
- **counterargument_or_limit:** Detailed traces can be indispensable when diagnosing a rare tool or renderer defect.
- **assumptions_and_boundaries:** Capture expanded traces temporarily for a named investigation and summarize retained findings afterward.
- **revision_decision:** Remove unconditional latency percentiles and require metrics only for defined repeated workflows.
- **additional_insight_to_add:** More telemetry can reduce observability when signal location and evidence ownership become unclear.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The seed does not separate run cards, progress journals, command reports, review notes, and source manifests.
- **supporting_reason:** Run cards hold intent, journals hold phase state, reports hold reproducible results, notes hold judgment, and manifests hold coverage.
- **counterargument_or_limit:** Duplicating the same decision across artifacts creates synchronization failures.
- **assumptions_and_boundaries:** Assign one authoritative home per fact and link it from other records.
- **revision_decision:** Define artifact roles and a compact evidence index rather than one monolithic log.
- **additional_insight_to_add:** Good observability is a navigable graph of small authoritative records, not a chronological pile.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Missing safeguards include stale candidate IDs, unexplained skipped sources, redacted context, unresolved risk without owner, and changed commands without reruns.
- **supporting_reason:** These gaps prevent a later reviewer from determining what was tested, why evidence is absent, or who must act.
- **counterargument_or_limit:** Some source omissions are self-evident when they are outside the declared task boundary.
- **assumptions_and_boundaries:** Record omissions that a reasonable reviewer might otherwise interpret as accidental coverage gaps.
- **revision_decision:** Add identity, omission rationale, privacy, ownership, freshness, and closure checks.
- **additional_insight_to_add:** A skipped-source reason is evidence about scope, not an apology for incomplete discovery.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** The checklist has no example showing the difference between an evidence summary and a transcript dump.
- **supporting_reason:** A good record names the 84-column candidate, exact validator, two surfaces, reader result, one unresolved risk, owner, and trigger.
- **counterargument_or_limit:** Compact summaries can omit diagnostic detail needed after a future regression.
- **assumptions_and_boundaries:** Link retained raw output for material failures while keeping the primary record reviewable.
- **revision_decision:** Add good, noisy, and under-specified observation examples.
- **additional_insight_to_add:** Borderline records should be repaired by adding the missing decision link, not by appending unrelated output.
### Question 08: How can the important claims be verified?
- **current_section_observation:** No test proves the record is complete enough to reconstruct acceptance or that its links resolve.
- **supporting_reason:** A second reviewer can use only the evidence index to identify sources, rerun commands, inspect surfaces, repeat reader tasks, and explain open risks.
- **counterargument_or_limit:** Exact reproduction may be impossible when a volatile external renderer has changed.
- **assumptions_and_boundaries:** Preserve environment identity and distinguish reproducible mechanics from time-bounded observations.
- **revision_decision:** Add an observability reconstruction test and link-integrity scan.
- **additional_insight_to_add:** Reconstruction failure pinpoints which context was tacit rather than merely declaring the record incomplete.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** Commands and decisions are listed together without separating direct facts from reviewer interpretation.
- **supporting_reason:** Candidate hashes, paths, outputs, dimensions, and timestamps are observable; severity, sufficiency, and ideal refresh cadence remain judgments.
- **counterargument_or_limit:** A timestamp does not guarantee that an observation still applies to the current external surface.
- **assumptions_and_boundaries:** Bind confidence to candidate and environment, and retain explicit volatility triggers.
- **revision_decision:** Label records as mechanical result, observed behavior, reviewer inference, or unresolved uncertainty.
- **additional_insight_to_add:** Observability should preserve disagreement when reviewers interpret the same mechanical fact differently.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The seed treats observability as retrospective recordkeeping rather than a control on workflow behavior.
- **supporting_reason:** Required candidate IDs, dispositions, and checkpoints encourage smaller changes, clearer ownership, and faster recovery before failures occur.
- **counterargument_or_limit:** Teams may optimize for complete forms instead of better artifacts.
- **assumptions_and_boundaries:** Review whether each retained field changed a decision or reduced recovery uncertainty.
- **revision_decision:** Make observability itself subject to periodic pruning and failure-driven evolution.
- **additional_insight_to_add:** The smallest useful evidence record is the one that preserves causal continuity across context and ownership boundaries.

## Section 023: Performance Verification Method
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed mixes rendered inspection, hidden-context avoidance, workflow timing, and action discovery without defining the performance claim under test.
- **supporting_reason:** Verification should decide whether a layout improves a declared reader task or maintenance operation enough to justify its composition and upkeep cost.
- **counterargument_or_limit:** Some ASCII artifacts exist for accuracy or resilience where speed is not the primary outcome.
- **assumptions_and_boundaries:** Measure time only when the reader or workflow contract names timeliness as material.
- **revision_decision:** Separate semantic correctness, task effectiveness, rendering conformance, and workflow-efficiency claims.
- **additional_insight_to_add:** A page can improve decision latency while increasing authoring time, so the evaluated perspective must be explicit.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** The measurement packet requests percentiles regardless of sample size or repeatability.
- **supporting_reason:** A predeclared task protocol with baseline, candidate, comparable inputs, observed outcomes, and qualitative error notes produces interpretable evidence.
- **counterargument_or_limit:** Establishing a baseline can be expensive when no prior artifact exists.
- **assumptions_and_boundaries:** Use a task success and error record without comparative speed claims when a credible baseline is unavailable.
- **revision_decision:** Make reader-task verification default and reserve latency distributions for repeated, adequately sampled workflows.
- **additional_insight_to_add:** No-baseline evidence can support fitness but not a claim of improvement.
### Question 03: When does the default work well?
- **current_section_observation:** The seed does not identify repeatable tasks suitable for measurement.
- **supporting_reason:** Locating a retry route, tracing a state transition, comparing options, or repairing a widened label can be reproduced with controlled inputs.
- **counterargument_or_limit:** Real incidents include stress and domain context that a quiet review cannot simulate fully.
- **assumptions_and_boundaries:** Report the test environment and avoid generalizing beyond comparable conditions.
- **revision_decision:** Add reader and maintainer task families with fit boundaries.
- **additional_insight_to_add:** Maintenance tasks reveal performance costs that first-read comprehension tests miss.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** "A new reader can apply the reference" can become a vague pass when task, prompt, and allowed context are unspecified.
- **supporting_reason:** Ambiguous protocols permit coaching, cherry-picked readers, changed questions, and post hoc success criteria.
- **counterargument_or_limit:** Excessive experimental control can make documentation review artificial and slow.
- **assumptions_and_boundaries:** Standardize only the variables needed to interpret the claim and preserve natural reading otherwise.
- **revision_decision:** Add protocol invalidation conditions and prohibit unsupported comparative or percentile claims.
- **additional_insight_to_add:** Reviewer assistance is part of the outcome and must be recorded rather than silently excluded.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The method treats rendered inspection as the main alternative to text-only claims but omits static checks, task observation, A/B comparison, and maintenance simulation.
- **supporting_reason:** Static checks prove conformance, renders expose surface behavior, tasks show usefulness, comparisons estimate change, and simulations expose repair cost.
- **counterargument_or_limit:** Running every method on every figure would dominate the work itself.
- **assumptions_and_boundaries:** Match evidence depth to claim consequence and choose the cheapest method that can falsify it.
- **revision_decision:** Provide a claim-to-method routing guide.
- **additional_insight_to_add:** Multiple weak measures do not equal one discriminating test of the actual claim.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Input size and tool-call count are requested without controls for reader familiarity, warmed caches, terminal width, copy changes, or task order.
- **supporting_reason:** These confounders can make a candidate seem faster for reasons unrelated to layout.
- **counterargument_or_limit:** Perfect counterbalancing and large samples are unrealistic for ordinary reference maintenance.
- **assumptions_and_boundaries:** Record major confounders, randomize or alternate order when feasible, and narrow conclusions.
- **revision_decision:** Add comparability, coaching, environment, sample, and Goodhart warnings.
- **additional_insight_to_add:** Timing precision should never exceed the protocol's ability to control variation.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** Pass and fail conditions are broad statements rather than observed measurement records.
- **supporting_reason:** A good task record names the candidate, width, reader, question, allowed context, answer, wrong turns, assistance, and elapsed interval when relevant.
- **counterargument_or_limit:** Elapsed time may reflect typing or environment latency rather than comprehension.
- **assumptions_and_boundaries:** Interpret timing alongside error path and assistance, not in isolation.
- **revision_decision:** Add complete, misleading, and inconclusive performance examples.
- **additional_insight_to_add:** Borderline results should identify whether the next test needs more readers, a cleaner baseline, or a revised task.
### Question 08: How can the important claims be verified?
- **current_section_observation:** Required inspection lacks a repeatable sequence from claim definition through evidence retention.
- **supporting_reason:** Freeze the claim and candidate, validate mechanics, render surfaces, execute tasks, compare only compatible observations, and retain raw and interpreted results.
- **counterargument_or_limit:** Human task results cannot be reproduced exactly like deterministic commands.
- **assumptions_and_boundaries:** Seek procedural reproducibility and transparent variation rather than identical human timing.
- **revision_decision:** Define a staged verification method and stopping rules.
- **additional_insight_to_add:** Mechanical failure should stop reader timing because a malformed candidate makes downstream measurements uninterpretable.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The seed combines exact input counts with reviewer decisions without confidence labels.
- **supporting_reason:** Dimensions, bytes, commands, and recorded intervals are direct observations; causal improvement and transfer to production readers require inference.
- **counterargument_or_limit:** Even direct timing observations depend on clock and event-boundary definitions.
- **assumptions_and_boundaries:** Document measurement resolution and avoid causal language when only correlation was observed.
- **revision_decision:** Separate measured facts, observed behavior, comparative inference, and untested populations.
- **additional_insight_to_add:** Honest uncertainty makes performance evidence reusable because later reviewers know what a new test must resolve.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** Performance is framed around applying the reference once rather than total artifact lifecycle cost.
- **supporting_reason:** A dense page may save initial lines but increase repeated reader errors, renderer fixes, and label-reflow work.
- **counterargument_or_limit:** Lifecycle costs are harder to observe before an artifact has aged.
- **assumptions_and_boundaries:** Use maintenance simulations initially and replace assumptions with actual change records over time.
- **revision_decision:** Add reader, author, reviewer, and maintainer perspectives to performance claims.
- **additional_insight_to_add:** Optimize the cost of reaching and preserving a correct decision, not the speed of producing the first diagram.

## Section 024: Scale Boundary Statement
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed names multiple systems, ownership, discovery, traffic, distributed work, context drift, and large codebases without one coherent sufficiency test.
- **supporting_reason:** A scale boundary should decide when one ASCII reference and page can no longer preserve a complete reader journey under bounded source, canvas, owner, and evidence contracts.
- **counterargument_or_limit:** Multiple systems or owners do not automatically make an overview page ineffective.
- **assumptions_and_boundaries:** Treat each scale dimension as pressure to probe, not an automatic count-based rejection.
- **revision_decision:** Define dimensional stop signals, adaptations, and routes instead of categorical size claims.
- **additional_insight_to_add:** Scale failure appears when coordination or compression destroys a required relationship, not when an arbitrary entity count is crossed.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** Splitting by theme file and owner is recommended without first preserving a global reader question and navigation layer.
- **supporting_reason:** Keep one bounded overview for cross-boundary relationships, then split independently verifiable detail by audience, surface, ownership, or update cadence.
- **counterargument_or_limit:** An overview can become another stale source of duplicated truth.
- **assumptions_and_boundaries:** The overview owns topology and routes, while detail pages own volatile facts.
- **revision_decision:** Adopt overview-plus-owned-pages as the default scale adaptation.
- **additional_insight_to_add:** Explicit ownership of relationship edges is as important as ownership of component pages.
### Question 03: When does the default work well?
- **current_section_observation:** The seed does not state when a single page remains sufficient despite organizational or system breadth.
- **supporting_reason:** One page still works when all readers need the same overview, terminology is stable, the narrowest canvas preserves key edges, and one evidence packet can validate it.
- **counterargument_or_limit:** A stable overview may hide fast-changing operational exceptions required by some readers.
- **assumptions_and_boundaries:** Route volatile detail and retain only durable relationships in the overview.
- **revision_decision:** Add positive sufficiency conditions and progressive-disclosure rules.
- **additional_insight_to_add:** Semantic stability can offset structural breadth when the page deliberately excludes volatile detail.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** Production traffic and explicit service-level objectives are mentioned even though ASCII layout sufficiency is not directly determined by traffic volume.
- **supporting_reason:** The relevant failure is whether operational consequence, realtime state, interaction, or update frequency exceeds static text's evidence and freshness model.
- **counterargument_or_limit:** Static runbooks remain valuable in high-traffic systems for failure recovery and offline access.
- **assumptions_and_boundaries:** Route live monitoring to operational tooling while preserving stable response guidance in text.
- **revision_decision:** Replace traffic-count language with consequence, volatility, and interaction boundaries.
- **additional_insight_to_add:** High scale may strengthen the need for a resilient ASCII fallback while disqualifying it as the live source of state.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** Source-graph narrowing is the only large-codebase adaptation, leaving linked suites, generated indexes, dashboards, and richer explainers unexamined.
- **supporting_reason:** Graph narrowing limits evidence, suites separate ownership, indexes preserve discovery, dashboards show live state, and rich explainers handle exploration.
- **counterargument_or_limit:** Every added artifact introduces synchronization and navigation cost.
- **assumptions_and_boundaries:** Assign one source of truth per fact and test cross-artifact routes.
- **revision_decision:** Add an escalation ladder based on which scale dimension fails.
- **additional_insight_to_add:** Scaling the representation and scaling the evidence-gathering process are separate decisions.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Parallel rewrite conflict is named, but hidden dependencies, duplicate overview facts, orphaned edges, localization growth, and renderer diversity are absent.
- **supporting_reason:** These pressures cause accepted fragments to disagree or fail when assembled.
- **counterargument_or_limit:** A comprehensive dependency model may exceed the value of a small documentation suite.
- **assumptions_and_boundaries:** Track only dependencies that change ownership, ordering, terminology, or acceptance.
- **revision_decision:** Add coordination, vocabulary, link, localization, and integration gates.
- **additional_insight_to_add:** Local passes do not imply suite reliability when cross-page relationships lack an owner and integration test.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** No artifact examples show sufficient, adapted, or exceeded scale.
- **supporting_reason:** A service map can remain one overview, a multi-team platform can use overview plus service pages, and a live dependency explorer should route to an interactive medium.
- **counterargument_or_limit:** Domain familiarity can allow expert audiences to use denser pages than onboarding readers.
- **assumptions_and_boundaries:** Evaluate examples against their declared audience and narrowest operational surface.
- **revision_decision:** Add keep, split, route, and fallback cases.
- **additional_insight_to_add:** A borderline artifact needs a probe of the exact relationship most likely to disappear under compression.
### Question 08: How can the important claims be verified?
- **current_section_observation:** The seed requires narrowing and checkpoints but no measurable scale probe or suite integration test.
- **supporting_reason:** Hardest-label, densest-edge, narrowest-surface, source-closure, ownership, and cross-route probes reveal different scale failures.
- **counterargument_or_limit:** Probes sample pressure and can miss future growth patterns.
- **assumptions_and_boundaries:** Retest on material audience, source, localization, ownership, or renderer changes.
- **revision_decision:** Define a scale evidence packet and escalation decision record.
- **additional_insight_to_add:** Test the overview's global path separately from each child page's local completeness.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** Scale limits are expressed categorically despite lacking universal empirical thresholds.
- **supporting_reason:** Widths, labels, sources, owners, surfaces, and failed tasks are observable; ideal decomposition remains contextual.
- **counterargument_or_limit:** Observed current fit may not survive expected growth or localization.
- **assumptions_and_boundaries:** State forecast assumptions and preserve headroom as a qualitative risk, not invented precision.
- **revision_decision:** Present boundaries as evidence-triggered operational judgments.
- **additional_insight_to_add:** Uncertainty about growth should prompt a reversible architecture rather than premature fragmentation.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** Context drift is treated as one large-workflow failure rather than a scale dimension coupled to artifact structure.
- **supporting_reason:** More pages, owners, and sources increase the number of contracts that can diverge and the cost of reconstructing decisions.
- **counterargument_or_limit:** Strong automation and stable schemas can keep large suites coherent.
- **assumptions_and_boundaries:** Add coordination controls only where divergence could change reader action or evidence validity.
- **revision_decision:** Connect scale boundaries to observability, backpressure, and suite-level verification.
- **additional_insight_to_add:** The scalable unit is not a page alone but a page plus its authority, routes, tests, and recovery contract.

## Section 025: Future Refresh Search Queries
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed provides generic official-documentation, repository-example, and release-note queries without tying them to a claim or refresh trigger.
- **supporting_reason:** A refresh query should help a future maintainer locate current primary evidence for a specific volatile assumption, renderer behavior, or tool contract.
- **counterargument_or_limit:** Search results are discovery aids and cannot establish authority or applicability by themselves.
- **assumptions_and_boundaries:** Every discovered source must be opened, scoped, dated, and reconciled before guidance changes.
- **revision_decision:** Replace topic-wide phrases with claim-driven query templates and a source acceptance procedure.
- **additional_insight_to_add:** Search quality improves when the maintainer states what evidence would change the current decision before querying.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** "Official documentation best practices" assumes one canonical authority exists for a multi-surface ASCII workflow.
- **supporting_reason:** Start with known local sources and direct specification or official renderer documentation, then use narrow search only to find missing current evidence.
- **counterargument_or_limit:** Official sources may describe syntax but omit practical cross-renderer behavior.
- **assumptions_and_boundaries:** Supplement primary rules with clearly labeled observed surface tests or community examples when necessary.
- **revision_decision:** Order refresh work as local diff, direct primary source, targeted discovery, artifact probe, and synthesis update.
- **additional_insight_to_add:** Authority and ecological validity are separate; a specification and a real render may answer different parts of one claim.
### Question 03: When does the default work well?
- **current_section_observation:** No trigger says when future searching is worth the cost.
- **supporting_reason:** Refresh is useful after renderer releases, specification changes, validator updates, recurring portability defects, new target surfaces, or stale inherited evidence.
- **counterargument_or_limit:** Calendar-only searches can create churn when relevant contracts have not changed.
- **assumptions_and_boundaries:** Use event triggers plus a bounded periodic review for externally volatile claims.
- **revision_decision:** Add trigger-to-query mapping and a stop condition once the claim is resolved.
- **additional_insight_to_add:** A failed target-surface regression is often a stronger refresh trigger than elapsed time alone.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** Broad GitHub example searches can return copied snippets, abandoned repositories, or aesthetically attractive but unverified layouts.
- **supporting_reason:** Unranked examples encourage popularity-based guidance and can erase the local corpus boundary.
- **counterargument_or_limit:** Community issue reports may reveal renderer defects before formal documentation changes.
- **assumptions_and_boundaries:** Use issues as leads or observed reports, not normative authority, and reproduce material behavior locally.
- **revision_decision:** Add source rejection criteria and forbid query-result snippets as final evidence.
- **additional_insight_to_add:** Discovery breadth should contract quickly once a primary contract and discriminating probe are available.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The seed omits direct bookmarks, release feeds, repository history, local corpus diffs, issue trackers, and controlled render tests.
- **supporting_reason:** Direct sources reduce noise, history explains change, issues expose edge cases, and probes test the exact environment.
- **counterargument_or_limit:** Maintaining a large monitoring surface can exceed the value of a compact reference.
- **assumptions_and_boundaries:** Track only sources connected to accepted material claims and target surfaces.
- **revision_decision:** Recommend source-specific refresh routes before open-ended web discovery.
- **additional_insight_to_add:** The best refresh mechanism is often a regression fixture that signals when external research is needed.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Query phrases lack version, date, target renderer, exact symptom, primary-domain preference, and exclusion of stale mirrors.
- **supporting_reason:** Missing qualifiers produce ambiguous results that are difficult to compare with the existing evidence boundary.
- **counterargument_or_limit:** Over-constrained queries can miss renamed features or emerging terminology.
- **assumptions_and_boundaries:** Begin claim-specific, broaden one dimension at a time, and record terminology changes.
- **revision_decision:** Add query construction fields and a broadening ladder.
- **additional_insight_to_add:** Query revisions are evidence about vocabulary drift and should inform future search templates.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** Existing query examples merely repeat the reference title and desired source category.
- **supporting_reason:** Good queries name a governing specification, renderer, behavior, or tool plus change intent; bad queries ask for undifferentiated best practices.
- **counterargument_or_limit:** A precise source name can bias discovery toward an outdated authority.
- **assumptions_and_boundaries:** Pair named-source checks with one terminology-neutral discovery query when authority may have shifted.
- **revision_decision:** Add concrete official-spec, renderer-release, validator-history, accessibility, and defect queries with limits.
- **additional_insight_to_add:** Borderline queries become useful when accompanied by explicit source-ranking and reproduction rules.
### Question 08: How can the important claims be verified?
- **current_section_observation:** No method validates whether future results actually support the claim they are collected for.
- **supporting_reason:** A refresh ledger can record trigger, query, result, authority, version, claim excerpt in paraphrase, applicability, conflict, probe, and disposition.
- **counterargument_or_limit:** Detailed ledgers can duplicate source maps when no decision changes.
- **assumptions_and_boundaries:** Record concise dispositions and expand only material conflicts or updates.
- **revision_decision:** Add source acceptance, conflict reconciliation, and regression rerun gates.
- **additional_insight_to_add:** A refresh is complete when affected guidance and evidence are reconciled, not when searching stops.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The generic phrases imply that future search will reliably find a definitive current answer.
- **supporting_reason:** Local source identities and current query intent are known, while future rankings, documentation structure, and renderer behavior are volatile.
- **counterargument_or_limit:** Even primary documentation may lag deployed behavior or omit platform-specific details.
- **assumptions_and_boundaries:** Preserve uncertainty until direct artifact probes and multiple relevant sources converge.
- **revision_decision:** Label query outputs as discovered, inspected, reproduced, reconciled, or rejected.
- **additional_insight_to_add:** Confidence should rise by evidence state, not by search-result rank or repeated secondary summaries.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** Search queries are static strings rather than maintained interfaces to evolving evidence.
- **supporting_reason:** Changes in terminology, source authority, and recurring defects can make old queries systematically blind.
- **counterargument_or_limit:** Continuously optimizing queries can become research work detached from artifact needs.
- **assumptions_and_boundaries:** Evolve a query only when a failed refresh, changed vocabulary, or new material claim justifies it.
- **revision_decision:** Add query lifecycle, retirement, and learning rules.
- **additional_insight_to_add:** Future-search guidance should minimize rediscovery while preserving the right to reject its own inherited assumptions.

## Section 026: Evidence Boundary Notes
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed defines three evidence labels but does not explain how to classify a material claim or resolve mixed support.
- **supporting_reason:** Evidence boundaries help readers decide what can be trusted directly, what must be refreshed, what is synthesized, and what was merely observed under a test environment.
- **counterargument_or_limit:** Labelling every sentence can make the reference unreadable without improving traceability.
- **assumptions_and_boundaries:** Apply explicit labels to material, disputed, numeric, volatile, or decision-governing claims and use section-level framing for stable clusters.
- **revision_decision:** Expand the taxonomy into a claim classification and reconciliation protocol.
- **additional_insight_to_add:** The right boundary is determined by how a claim could fail and be refreshed, not by where it appears in the document.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** Local and external facts are distinguished, while direct artifact observations and unresolved uncertainty are forced into synthesis or omitted.
- **supporting_reason:** Six states distinguish inspected local fact, inspected external fact, unrefreshed external mapping, combined inference, observed artifact behavior, and unresolved uncertainty without pretending they are interchangeable.
- **counterargument_or_limit:** More states increase authoring and review burden.
- **assumptions_and_boundaries:** Use the smallest state set that preserves authority, freshness, and falsifiability for the claim.
- **revision_decision:** Retain the original three labels, add observation and uncertainty, and define unrefreshed mapping as a non-evidentiary holding state.
- **additional_insight_to_add:** Tested behavior is evidence about a candidate and environment, not automatic proof of a universal rule.
### Question 03: When does the default work well?
- **current_section_observation:** The labels lack fit guidance for source summaries, operational defaults, examples, and verification results.
- **supporting_reason:** Classification works when the claim has a clear provenance, scope, candidate, or inference chain and when that distinction changes maintenance action.
- **counterargument_or_limit:** Some editorial recommendations emerge from many weak signals rather than one traceable source.
- **assumptions_and_boundaries:** Mark such recommendations as synthesis and disclose decisive assumptions or counterexamples.
- **revision_decision:** Add claim-type examples and grouping rules.
- **additional_insight_to_add:** Evidence boundaries can be concise when a source map and claim ledger carry detailed provenance.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** A label can create false confidence even when the cited source does not support the wording or applies to another surface.
- **supporting_reason:** Label laundering, stale inheritance, citation chains, and paraphrase drift preserve the appearance of evidence while losing its substance.
- **counterargument_or_limit:** Rechecking every commonplace statement against primary text can be disproportionate.
- **assumptions_and_boundaries:** Prioritize claims that govern defaults, compatibility, risk, numeric assertions, or rejection decisions.
- **revision_decision:** Add source-entailment, scope, freshness, and transitive-citation failure rules.
- **additional_insight_to_add:** A source path proves availability, not support; reviewers must inspect the relevant span and claim relationship.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The seed does not compare inline tags, section prefaces, source-map rows, footnotes, or a separate claim ledger.
- **supporting_reason:** Inline tags maximize locality, prefaces reduce noise, maps aid overview, footnotes support reading flow, and ledgers support audits.
- **counterargument_or_limit:** Splitting provenance across formats can make a claim difficult to follow.
- **assumptions_and_boundaries:** Use section framing for homogeneous claims and a ledger for material exceptions or conflicts.
- **revision_decision:** Recommend layered provenance with one authoritative detailed record.
- **additional_insight_to_add:** Provenance representation should optimize both normal reading and skeptical audit, which are different navigation tasks.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** No warnings cover combined claims with unequal support, external facts inherited without current browsing, local examples mistaken for universal guidance, or conflicts hidden by synthesis.
- **supporting_reason:** These cases can convert bounded evidence into authoritative-sounding recommendations.
- **counterargument_or_limit:** Excessive caveats can obscure a useful default.
- **assumptions_and_boundaries:** State the default plainly, then attach the shortest boundary that changes its application.
- **revision_decision:** Add mixed-support decomposition, freshness, scope, and conflict-disclosure rules.
- **additional_insight_to_add:** Split a sentence when its clauses require different evidence states; grammatical convenience should not blur provenance.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** The three definitions provide no classified examples from this ASCII reference.
- **supporting_reason:** Local width guidance, inherited public-source metadata, synthesized run-card lifecycle, and observed target renders demonstrate distinct evidence states.
- **counterargument_or_limit:** Examples can become stale when sources or test environments change.
- **assumptions_and_boundaries:** Bind examples to current source identity or candidate evidence and refresh them with the claim.
- **revision_decision:** Add good classifications, a mislabeled universal claim, and a mixed borderline sentence that must be split.
- **additional_insight_to_add:** Good classification names the smallest claim the evidence actually supports.
### Question 08: How can the important claims be verified?
- **current_section_observation:** No audit checks that labelled facts are entailed, current, scoped, or consistently used across the file.
- **supporting_reason:** A material-claim ledger can trace wording to source span or observation, classify it, record freshness, test conflicts, and identify dependent sections.
- **counterargument_or_limit:** Full claim-level ledgers are expensive for low-risk descriptive prose.
- **assumptions_and_boundaries:** Audit all decision-governing and volatile claims, then sample lower-risk exposition skeptically.
- **revision_decision:** Define claim audit, conflict reconciliation, and dependency refresh checks.
- **additional_insight_to_add:** Verification should fail when a claim is stronger than its source even if the source itself is authoritative.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The labels identify provenance category but not confidence, freshness, or applicability.
- **supporting_reason:** A local fact can be high-confidence yet narrow, while a synthesis can be useful but explicitly judgmental.
- **counterargument_or_limit:** Confidence scoring can introduce unsupported numerical precision.
- **assumptions_and_boundaries:** Describe confidence through evidence state, scope, conflicts, and missing tests rather than arbitrary scores.
- **revision_decision:** Add qualitative confidence and uncertainty language per material claim.
- **additional_insight_to_add:** Provenance, confidence, and applicability are independent axes and should not be collapsed into one label.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** Evidence boundaries are presented as static notes at the file end rather than maintenance infrastructure.
- **supporting_reason:** Clear dependencies allow a source change or failed render to identify exactly which recommendations, examples, and gates need review.
- **counterargument_or_limit:** Maintaining fine-grained dependency links can become burdensome as prose is reorganized.
- **assumptions_and_boundaries:** Track dependencies at the material-claim or section level and refresh links during skeptical rereads.
- **revision_decision:** Connect evidence labels to observability, search refresh, reliability, and change propagation.
- **additional_insight_to_add:** Evidence boundaries make disagreement productive because reviewers can challenge authority, inference, or applicability separately.
