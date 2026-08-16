## Section 001: Html Explainer Page Patterns
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed title names a theme but does not say that the governing decision is whether a source-grounded, standalone HTML journey is the right explanatory medium for a technical subject.
- **supporting_reason:** Readers need this decision stated first because choosing HTML commits the author to browser behavior, visual hierarchy, interaction, and local-open portability that a prose note does not require.
- **counterargument_or_limit:** A title section cannot resolve every implementation choice, and forcing a full decision tree into the opening would duplicate later routing and tradeoff sections.
- **assumptions_and_boundaries:** The decision applies to explanatory artifacts derived from code, architecture notes, specifications, workflows, or mixed evidence, not to product landing pages or ordinary application screens.
- **revision_decision:** Expand the opening into a concise scope statement that identifies the medium choice, the intended reader outcome, and the source-grounding obligation.
- **additional_insight_to_add:** Treat medium selection as an engineering decision because a visually polished page that obscures mechanism can cost more understanding than a plain document.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** The local skill establishes a self-contained single HTML file, inline CSS and JavaScript, a guided narrative, and direct browser opening as the baseline rather than optional flourishes.
- **supporting_reason:** A single-file artifact minimizes setup friction, preserves the story as one reviewable unit, and lets a teammate inspect the explanation without installing a build toolchain.
- **counterargument_or_limit:** Inline assets become awkward when an explainer grows into a maintained application, needs shared components, or carries media whose size makes one file impractical.
- **assumptions_and_boundaries:** The default assumes a bounded technical story, a local or repository-hosted audience, and no requirement for server-side data, authentication, or continuous live updates.
- **revision_decision:** State the default as source-first, single-file, mystery-to-mechanism storytelling with restrained interaction and an explicit source footer.
- **additional_insight_to_add:** Portability is part of explanatory quality: removing the build step reduces the chance that only the author can reproduce what the page claims to show.
### Question 03: When does the default work well?
- **current_section_observation:** The seed offers no fit criteria even though the local sources describe explainers for source code, architecture, connectors, lifecycles, and executive or ELI5 understanding.
- **supporting_reason:** The pattern is strongest when a reader benefits from staged disclosure, a visible core loop, comparisons, state transitions, and a small number of telling code excerpts.
- **counterargument_or_limit:** Even a complex system may be better served by searchable prose when readers primarily need exhaustive API facts rather than a guided mental model.
- **assumptions_and_boundaries:** Good-fit subjects have a defensible thesis, a discoverable lifecycle or data path, enough reliable evidence to support major claims, and a reader who can consume a scrollable page.
- **revision_decision:** Add positive fit signals covering bounded system stories, cross-role onboarding, architecture walkthroughs, and mechanisms whose sequence is easier to grasp visually.
- **additional_insight_to_add:** The page earns its cost when ordering matters: scroll position can make conceptual dependencies explicit in a way that an unordered source dump cannot.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The title alone hides the failure boundary between a technical explainer and a decorative microsite, a complete reference manual, or an interactive production tool.
- **supporting_reason:** Without an avoid condition, agents can reach for HTML whenever a request says "visual," even when the deliverable needs editability, exhaustive lookup, or real application behavior.
- **counterargument_or_limit:** A small HTML page can still complement a reference manual or application, so the medium should not be rejected merely because other artifacts also exist.
- **assumptions_and_boundaries:** The default becomes wrong when evidence is too thin to explain honestly, the subject cannot be bounded, static opening is prohibited, or required interactions demand an application architecture.
- **revision_decision:** Name clear stop conditions and route those cases to Markdown, ASCII or Mermaid explanation, code documentation, a generated document, or a tested web application.
- **additional_insight_to_add:** The costliest misuse is not visual imperfection but false comprehension, where smooth pacing makes an unsupported mental model feel settled.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The seed title does not distinguish HTML explainers from neighboring media whose lower production cost or stronger searchability may better fit the reader's task.
- **supporting_reason:** Explicit alternatives prevent the recommendation from becoming self-selecting and expose the trade between narrative control, portability, accessibility effort, maintenance, and depth.
- **counterargument_or_limit:** Medium boundaries overlap; a Markdown document can embed diagrams, while a single HTML file can remain mostly textual and highly searchable.
- **assumptions_and_boundaries:** Relevant alternatives include structured Markdown, terminal-safe ASCII, Mermaid-backed documentation, slide decks, recorded demos, and full frontend applications.
- **revision_decision:** Preview an adopt-adapt-avoid model and defer detailed comparisons to the dedicated decision and adjacent-routing sections.
- **additional_insight_to_add:** Choose the least powerful medium that preserves the essential explanatory experience, because every extra runtime capability creates another state to verify.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** The opening currently gives no warning about invented behavior, metaphor drift, buried core loops, retained scaffold copy, broken local opening, or inaccessible interaction.
- **supporting_reason:** These failures are systemic: they can undermine trust across the whole page even if individual paragraphs and visual components look polished.
- **counterargument_or_limit:** Listing every browser and content defect in the opening would make the entry section heavy and weaken the narrative orientation it is meant to provide.
- **assumptions_and_boundaries:** The opening should identify only high-leverage risks, while later tables and checklists carry detailed detection and recovery procedures.
- **revision_decision:** Add a compact warning that source fidelity, mechanism visibility, direct-disk operation, responsive reading, and claim traceability are non-negotiable.
- **additional_insight_to_add:** Scaffold residue is an evidence problem as well as an editorial problem because generic labels can silently substitute template assumptions for the system's own nouns and verbs.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** The seed heading supplies no example that lets a reader recognize whether an intended deliverable belongs inside this reference's scope.
- **supporting_reason:** A concrete contrast makes the decision operational faster than an abstract definition, especially for agents that otherwise imitate surface style.
- **counterargument_or_limit:** Opening examples must remain short and hypothetical so they do not imply that one connector-shaped story arc fits every technical domain.
- **assumptions_and_boundaries:** A good case explains a bounded lifecycle from cited code; a bad case decorates generic prose; a borderline case needs either narrower scope or a companion reference.
- **revision_decision:** Include one-sentence good, bad, and borderline signals in the scope block, then reserve developed examples for Section 014.
- **additional_insight_to_add:** The borderline category should trigger a deliberate split between guided understanding and exhaustive detail rather than a compromise artifact that serves neither purpose.
### Question 08: How can the important claims be verified?
- **current_section_observation:** No verification contract appears beside the title, so the reader cannot yet tell that narrative accuracy and rendered behavior both require evidence.
- **supporting_reason:** The artifact has two independent truth surfaces: claims must trace to source, and the page must actually open, render, navigate, and remain legible across target conditions.
- **counterargument_or_limit:** The opening should not hard-code tool commands that may differ by repository or available browser automation environment.
- **assumptions_and_boundaries:** Verification can combine source-to-claim review, direct local opening, console inspection, keyboard checks, responsive screenshots, and placeholder scans.
- **revision_decision:** Introduce a dual gate in the opening and point forward to the command set, observability checklist, and performance verification method.
- **additional_insight_to_add:** A screenshot proves appearance at one moment but not semantic accuracy, keyboard reachability, or behavior after scripts fail, so evidence must be layered.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The local files confidently prescribe the artifact shape and narrative baseline, while the seed's public links have not been refreshed and provide no inspected support in this no-browse run.
- **supporting_reason:** Separating local instruction from unverified external pointers prevents inherited URLs and numeric scores from masquerading as current research findings.
- **counterargument_or_limit:** Local guidance itself is a workflow convention, not universal proof that every audience learns better from the same act count, palette, or pacing.
- **assumptions_and_boundaries:** Confident facts are limited to repository source content and observable template behavior; audience comprehension, optimal density, and performance budgets require local measurement.
- **revision_decision:** Mark the opening's defaults as local-corpus guidance and identify adaptation choices as reviewer judgment rather than externally validated laws.
- **additional_insight_to_add:** Confidence should attach to individual claims, not the page as a whole, because one explainer can contain source facts, design choices, hypotheses, and unresolved ambiguities together.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The seed does not derive the consequence that an explainer is a maintained interface between evolving source code and a reader's mental model.
- **supporting_reason:** Once the page is treated as an interface, source drift, browser degradation, and narrative ambiguity become regression classes rather than cosmetic imperfections.
- **counterargument_or_limit:** Applying full product governance to a one-off internal explainer can create review overhead disproportionate to its audience and lifetime.
- **assumptions_and_boundaries:** Maintenance rigor should scale with reuse, decision impact, system volatility, and the harm caused by stale explanations.
- **revision_decision:** Close the opening with a lifecycle principle: scope, build, verify, and refresh the explainer according to its expected operational life.
- **additional_insight_to_add:** The best compression sentence can double as a drift detector; if source changes invalidate that sentence, the narrative spine probably needs review before individual styling does.
## Section 002: Source Evidence Mapping Table
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed table lists five locations but does not help a reviewer decide which source can establish narrative rules, implementation behavior, ecosystem context, or only a future research lead.
- **supporting_reason:** Evidence roles determine how strongly a recommendation can be stated and whether a disagreement should be resolved by local convention, direct artifact inspection, or refreshed research.
- **counterargument_or_limit:** A mapping table can describe provenance but cannot prove that every downstream interpretation of a source is accurate.
- **assumptions_and_boundaries:** The map covers sources relevant to this frozen reference; it is not an inventory of every HTML, accessibility, or browser standard available elsewhere.
- **revision_decision:** Expand the map with authority, freshness, inspected status, concrete contribution, and verification implications for each source family.
- **additional_insight_to_add:** Source selection is itself a design control because weak evidence admitted early tends to become confident page copy later.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** The canonical `SKILL.md` and supporting pattern are the only mapped files whose content was directly read for this no-browse evolution.
- **supporting_reason:** Starting with those local files preserves repository intent, while reading their linked generator and template reveals executable behavior hidden behind prose summaries.
- **counterargument_or_limit:** Repository-local status does not make a source universally correct or current with browser platform guidance.
- **assumptions_and_boundaries:** External URLs remain inherited pointers until a separately authorized refresh inspects them; linked assets support implementation facts but do not replace the narrative sources.
- **revision_decision:** Make local canonical and supporting sources the default evidence chain, then use linked artifacts to test operational claims and external material only after freshness review.
- **additional_insight_to_add:** A linked script can falsify an assumed workflow detail, such as overwrite behavior, even when it contributes no general design principle.
### Question 03: When does the default work well?
- **current_section_observation:** Local-first mapping works when the deliverable must fit the existing skill, bundled scaffold, and repository-specific tone.
- **supporting_reason:** The source pair jointly covers intent, story shape, component selection, guardrails, and final checks, while the assets expose concrete defaults.
- **counterargument_or_limit:** Local-first evidence is insufficient for claims about broad accessibility conformance, browser support, or current external tool APIs.
- **assumptions_and_boundaries:** The default presumes the task asks for this repository's explainer pattern rather than an independent survey of web-documentation practices.
- **revision_decision:** Add a fit note showing that local evidence governs artifact construction and refreshed primary standards should govern externally sensitive claims.
- **additional_insight_to_add:** Evidence sufficiency depends on claim type, so one source set can be complete for narrative pacing yet incomplete for runtime compatibility.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The seed's uniform row shape can encourage readers to treat an unvisited URL as equivalent to an inspected local implementation file.
- **supporting_reason:** That equivalence fails when freshness, exact semantics, or version-specific behavior matters, producing attribution without actual support.
- **counterargument_or_limit:** Removing inherited external pointers entirely would erase useful refresh routes and weaken future maintenance.
- **assumptions_and_boundaries:** A source becomes unusable for a claim when it was not inspected, conflicts with direct artifacts, lacks relevant scope, or cannot be reproduced.
- **revision_decision:** Preserve external rows but label them unrefreshed and prohibit using them as proof in the current synthesis.
- **additional_insight_to_add:** An honest unknown is more reusable than a guessed fact because a future maintainer can see exactly what evidence still needs collection.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The table does not compare prose instructions, executable scaffolds, existing output pages, standards, and ecosystem examples as distinct evidence forms.
- **supporting_reason:** Prose explains intent, code reveals actual defaults, rendered artifacts expose usability, standards define normative requirements, and examples reveal conventions with varying authority.
- **counterargument_or_limit:** Adding every evidence class would make this compact source map harder to scan and could imply unavailable artifacts were reviewed.
- **assumptions_and_boundaries:** Only present local files and inherited URLs should receive rows; missing classes belong in a gap note rather than fabricated entries.
- **revision_decision:** Add the linked bootstrap and template as implementation-support rows, then explain absent rendered-example and refreshed-standard evidence below the table.
- **additional_insight_to_add:** Triangulation is strongest when intent, implementation, and observed output agree; any two can conceal a drift in the third.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Major risks include stale links, title-based inference, indirect citation, source duplication, and treating template defaults as mandatory design law.
- **supporting_reason:** These errors distort both content accuracy and the freedom to adapt the scaffold to a subject's actual needs.
- **counterargument_or_limit:** A detailed provenance scheme can become bureaucratic if the page is small and every claim already has an obvious source.
- **assumptions_and_boundaries:** Mapping detail should scale with claim consequence, source conflict, maintenance lifetime, and the number of contributors.
- **revision_decision:** Add review signals for inspected bytes, source role, claim scope, and refresh status without inventing a heavyweight citation system.
- **additional_insight_to_add:** Template code is descriptive evidence of the bundled baseline, not prescriptive evidence that its palette, rounded corners, or motion is always appropriate.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** A good row says what was inspected and what it can support; a bad row names a prestigious URL without connecting it to a claim.
- **supporting_reason:** Role-specific examples show reviewers how to reject source theater while retaining useful provenance.
- **counterargument_or_limit:** Table examples can oversimplify mixed-role files that contain both authoritative instructions and illustrative suggestions.
- **assumptions_and_boundaries:** Borderline sources should remain visible with a narrow contribution and an uncertainty label rather than being promoted or discarded wholesale.
- **revision_decision:** Include contribution and limitation columns whose cell text demonstrates good evidence scoping directly.
- **additional_insight_to_add:** The most credible source may still support only one sentence, while a lower-authority artifact may provide extensive operational observations.
### Question 08: How can the important claims be verified?
- **current_section_observation:** The seed map has no test that mapped local paths exist, linked artifacts were read, or external evidence remains clearly unrefreshed.
- **supporting_reason:** Simple path, hash, and status checks prevent silent drift between the map and the actual evidence package.
- **counterargument_or_limit:** File existence and matching hashes do not verify that the synthesis accurately represents each source.
- **assumptions_and_boundaries:** Verification requires both machine checks for inventory integrity and human comparison for semantic faithfulness.
- **revision_decision:** Add row-level verification actions: read local files, inspect linked behavior, record hashes when frozen, and mark external refresh dates only after browsing is authorized.
- **additional_insight_to_add:** A source map should fail closed on missing canonical evidence but remain usable with an explicit warning when optional comparative evidence is absent.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** Local source contents, paths, and linked scaffold behavior are directly known; the relevance and current content of the three public URLs are not known here.
- **supporting_reason:** This boundary follows the actual retrieval history rather than the authority implied by a domain name.
- **counterargument_or_limit:** Even directly read local files leave interpretation choices, especially where terms such as elegant, polished, or ELI5 are subjective.
- **assumptions_and_boundaries:** Confidence labels describe evidence access and role, not a numeric probability that every recommendation will suit every audience.
- **revision_decision:** Replace unsupported confidence scoring with categorical status and state all adaptation judgments explicitly.
- **additional_insight_to_add:** Evidence certainty and recommendation strength should be tracked separately because a confidently observed template choice may still be a weak default.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The combined package reveals a chain from instruction to pattern to generator to template, which the seed's flat map conceals.
- **supporting_reason:** Making that chain visible helps maintainers locate drift: conceptual mismatch belongs in prose, scaffold mismatch in the script, and visual or behavior mismatch in the template.
- **counterargument_or_limit:** The linked assets are archived evidence and must not be edited through this reference-evolution task.
- **assumptions_and_boundaries:** The map can diagnose ownership without granting permission to change any source outside Gamma's exclusive files.
- **revision_decision:** Present evidence as a hierarchy with explicit downstream dependency, while keeping archive materials immutable.
- **additional_insight_to_add:** Provenance doubles as a change-impact map, reducing the chance that maintainers patch generated pages repeatedly instead of correcting the responsible upstream layer.
## Section 003: Pattern Scoreboard Ranking Table
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed ranks three generic evidence practices numerically but does not tell an explainer author which construction patterns must be established first.
- **supporting_reason:** A useful ranking should allocate limited review effort toward failures that most directly corrupt understanding or make the artifact unusable.
- **counterargument_or_limit:** Pattern importance changes with audience, subject, lifetime, and delivery environment, so a universal total order can mislead.
- **assumptions_and_boundaries:** The scoreboard ranks defaults for bounded, source-grounded, standalone technical explainers rather than all web documentation.
- **revision_decision:** Reframe the table as an adoption sequence with priority, dependency, failure prevented, and proof signal.
- **additional_insight_to_add:** Ranking by dependency reveals that visual polish cannot compensate for a missing source model or narrative spine.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** Source grounding, early core-loop visibility, and dual content-render verification are the highest-leverage local patterns.
- **supporting_reason:** Together they answer whether the page is true, understandable in sequence, and operational in a browser.
- **counterargument_or_limit:** Some subjects lack a literal loop and need a decision tree, state transition, or dependency path as their early heartbeat.
- **assumptions_and_boundaries:** "Core loop" denotes the primary mechanism or causal path, not necessarily cyclical execution.
- **revision_decision:** Assign mandatory priority to evidence inventory, mechanism-first narrative, and two-surface verification before optional visual enrichment.
- **additional_insight_to_add:** The first three priorities form a minimum viable explanation contract that remains valuable even if all animation is removed.
### Question 03: When does the default work well?
- **current_section_observation:** An ordered scoreboard helps when an agent must choose what to preserve under schedule, token, or page-length pressure.
- **supporting_reason:** Dependency-aware priorities let the author reduce component variety without sacrificing claim fidelity or causal comprehension.
- **counterargument_or_limit:** A rigid sequence can slow exploratory work where the narrative only emerges after sketching several visual representations.
- **assumptions_and_boundaries:** Exploration may be nonlinear, but the completed artifact should satisfy higher priorities before lower ones receive polish.
- **revision_decision:** Explain that build order may iterate while acceptance order remains strict.
- **additional_insight_to_add:** Separating discovery order from acceptance order protects creative exploration without weakening the final gate.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** Numeric scores fail when their measurement basis is absent, and default rankings fail when a specialized audience has different critical risks.
- **supporting_reason:** Unsupported numbers create false comparability, while context-blind rankings can underweight privacy, localization, or regulated accessibility needs.
- **counterargument_or_limit:** Numbers can be useful after repeated review data establishes a stable scoring rubric.
- **assumptions_and_boundaries:** No measured corpus or calibrated weighting model is supplied by the frozen sources.
- **revision_decision:** Remove unexplained numeric values and invite project-specific promotion of additional gates when evidence warrants it.
- **additional_insight_to_add:** A scoreboard should expose why a row moves, making policy changes reviewable instead of silently changing a score.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** Alternatives include risk tiers, pairwise comparison, a simple checklist, or measurable quality scores derived from user studies.
- **supporting_reason:** Tiers communicate default precedence cheaply, whereas measured scores support trend analysis but demand consistent data collection.
- **counterargument_or_limit:** Checklists avoid ranking disputes but provide little guidance when time forces tradeoffs.
- **assumptions_and_boundaries:** This reference needs operational prioritization now and has no outcome dataset for calibrated scoring.
- **revision_decision:** Use `required`, `strong_default`, and `conditional` tiers plus explicit dependency notes.
- **additional_insight_to_add:** Conditional does not mean decorative; it means the pattern activates only when a subject or delivery condition creates the relevant risk.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Common ranking errors are polishing before evidence review, forcing a metaphor, hiding the heartbeat, and treating animation as proof of explanation.
- **supporting_reason:** These errors consume effort while leaving the reader with an attractive but unstable or incomplete model.
- **counterargument_or_limit:** Visual iteration can uncover conceptual flaws, so presentation work should not be postponed categorically.
- **assumptions_and_boundaries:** Visual prototypes are acceptable discovery tools when their claims remain provisional and source reconciliation follows.
- **revision_decision:** Add failure-prevention targets and stop signals to every ranked pattern row.
- **additional_insight_to_add:** Review should demote any component whose removal improves clarity without losing a verified causal relation.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** A good scoreboard links each priority to evidence; a bad one assigns precise numbers from taste; a borderline one lists valid patterns without dependencies.
- **supporting_reason:** Concrete distinctions help reviewers tell prioritization from decoration or inventory.
- **counterargument_or_limit:** Even a good generic ranking needs adaptation when the page communicates a high-consequence operational procedure.
- **assumptions_and_boundaries:** The examples evaluate scoreboard design, not the quality of any particular rendered page.
- **revision_decision:** Demonstrate good ranking through the evolved table's rationale and verification columns.
- **additional_insight_to_add:** A borderline inventory becomes actionable when each row names the earlier condition it assumes and the evidence that closes it.
### Question 08: How can the important claims be verified?
- **current_section_observation:** The seed provides no evidence that its scores predict better explainers or fewer failures.
- **supporting_reason:** Verification should test each pattern's observable result rather than reassert its rank.
- **counterargument_or_limit:** Some outcomes, such as comprehension, require reader studies and cannot be proven by static linting alone.
- **assumptions_and_boundaries:** Available gates can verify source coverage, heartbeat placement, local opening, keyboard paths, responsive layout, and scaffold cleanup.
- **revision_decision:** Pair each tier with a direct artifact check and reserve comprehension claims for measured feedback.
- **additional_insight_to_add:** A pattern should lose priority if repeated evidence shows its cost exceeds the failure reduction it was meant to provide.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The local corpus explicitly supports source grounding, early mechanism, intentional components, mobile readability, and final checks, but not numeric effectiveness scores.
- **supporting_reason:** Those instructions justify categorical defaults while leaving outcome magnitude and universal ordering uncertain.
- **counterargument_or_limit:** Local authorship still embeds design judgment, and no reader sample is attached to validate the recommended act structure.
- **assumptions_and_boundaries:** Confidence is strongest for what the workflow requires and weaker for how much each requirement improves understanding.
- **revision_decision:** Label ranks as local operating priorities rather than empirical performance measurements.
- **additional_insight_to_add:** Preserving uncertainty makes the scoreboard easier to evolve because future metrics can refine tiers without contradicting invented history.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The patterns form a causal chain: evidence constrains narrative, narrative selects components, and verification tests both content and rendering.
- **supporting_reason:** A chain-oriented ranking exposes where downstream repair cannot fix an upstream omission.
- **counterargument_or_limit:** Feedback can travel backward; rendering a diagram may reveal that the source model or narrative ordering is wrong.
- **assumptions_and_boundaries:** Dependencies govern acceptance but allow iterative loops during authoring.
- **revision_decision:** Add dependency and feedback-loop language beneath the scoreboard.
- **additional_insight_to_add:** The most efficient workflow validates the cheapest upstream assumption before investing in expensive downstream visual composition.
## Section 004: Idiomatic Thesis Synthesis Statement
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed thesis says to load local and public evidence but never defines what makes an HTML explainer idiomatic or successful.
- **supporting_reason:** A governing statement should let every later recommendation be tested against one coherent purpose rather than a collection of page components.
- **counterargument_or_limit:** A compact thesis cannot encode all accessibility, maintenance, or audience-specific constraints.
- **assumptions_and_boundaries:** The thesis governs standalone technical explainers whose primary outcome is a traceable mental model, not conversion, entertainment, or application task completion.
- **revision_decision:** Define the artifact as an evidence-grounded guided tour that makes a causal model understandable and inspectable through narrative, visuals, and browser behavior.
- **additional_insight_to_add:** Idiomatic quality lies in alignment among source truth, conceptual order, and rendered experience rather than in copying a particular visual theme.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** The local sources consistently recommend source reading, a mystery-first opening, early mechanism, selective components, one file, and explicit source listing.
- **supporting_reason:** This sequence minimizes unsupported invention while reducing the reader's cognitive load in controlled stages.
- **counterargument_or_limit:** Mystery-first pacing can feel artificial for readers who already know the problem and need a direct operational answer.
- **assumptions_and_boundaries:** Adapt the opening to audience knowledge while retaining an early statement of purpose and mechanism.
- **revision_decision:** State a source-first, mechanism-early, single-file default with deletable acts and restrained enhancement.
- **additional_insight_to_add:** The page should optimize time to a correct mental model, not time spent scrolling or quantity of visual novelty.
### Question 03: When does the default work well?
- **current_section_observation:** The thesis fits systems with a bounded causal story, meaningful state, distinguishable actors, and a small set of consequential tradeoffs.
- **supporting_reason:** Those properties support staged explanation without requiring an exhaustive encyclopedia.
- **counterargument_or_limit:** A concept without lifecycle or state can still benefit from HTML through comparisons or progressive examples.
- **assumptions_and_boundaries:** The mechanism may be a loop, branch, transformation, protocol exchange, or dependency structure.
- **revision_decision:** Generalize "heartbeat" to the earliest causal structure a reader must retain.
- **additional_insight_to_add:** A subject is ready for an explainer when its author can name what the reader should predict after finishing.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The seed thesis does not identify polished misinformation, script-dependent invisibility, or unbounded detail as thesis-level failures.
- **supporting_reason:** These conditions defeat inspectable understanding even if individual page features follow the template.
- **counterargument_or_limit:** Not every incomplete detail invalidates a high-level explanation when scope and uncertainty are explicit.
- **assumptions_and_boundaries:** Omission is acceptable when deliberate and disclosed; contradiction or invented mechanics is not.
- **revision_decision:** Add falsifiers covering unsupported claims, obscured core mechanism, inaccessible essentials, and absent scope boundaries.
- **additional_insight_to_add:** A strong explainer teaches the limits of its model, preventing readers from applying a simplified story beyond its valid domain.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The thesis should distinguish narrative coherence from comprehensive reference coverage and static portability from richer application behavior.
- **supporting_reason:** Those tradeoffs determine whether a single-file journey is an advantage or an artificial constraint.
- **counterargument_or_limit:** Hybrid deliverables can combine a guided page with links to exhaustive documentation or runnable tools.
- **assumptions_and_boundaries:** Companion artifacts are allowed when the explainer remains self-sufficient for its declared takeaway.
- **revision_decision:** Frame HTML as the guided entry surface, not necessarily the sole documentation surface.
- **additional_insight_to_add:** Links should deepen or verify the model rather than carry essential steps the page claims to explain.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** A thesis can become empty branding if terms such as elegant, visual, and source-grounded lack observable consequences.
- **supporting_reason:** Operational qualifiers make the statement useful during content cuts, component selection, and final review.
- **counterargument_or_limit:** Overloading the thesis with test language would reduce memorability.
- **assumptions_and_boundaries:** Detailed proof belongs later, while the thesis names the invariant outcomes those proofs support.
- **revision_decision:** Use concrete verbs: trace, reveal, distinguish, open, read, and verify.
- **additional_insight_to_add:** A memorable thesis should function as a rejection test for attractive additions that do not improve explanation.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** A good thesis predicts reader capability; a bad thesis promises polish; a borderline thesis describes format without evidence or outcome.
- **supporting_reason:** Outcome language anchors author decisions to what the reader can understand or verify.
- **counterargument_or_limit:** Predicting comprehension still requires feedback rather than author confidence alone.
- **assumptions_and_boundaries:** Static review can assess structural support for learning, while user evidence assesses actual learning.
- **revision_decision:** Include a concise good-form thesis and explicit failure contrast.
- **additional_insight_to_add:** The strongest outcome statement names a question the reader can answer, not an emotion the page should evoke.
### Question 08: How can the important claims be verified?
- **current_section_observation:** The thesis currently has no acceptance questions tied to its terms.
- **supporting_reason:** A short set of falsifiable prompts turns the governing statement into a review instrument.
- **counterargument_or_limit:** Review questions cannot substitute for target-audience observation on high-impact explainers.
- **assumptions_and_boundaries:** At minimum, reviewers can test source traceability, mechanism placement, static readability, and takeaway accuracy.
- **revision_decision:** Add a four-question thesis gate immediately after the synthesis statement.
- **additional_insight_to_add:** Ask a reviewer to predict one failure or recovery outcome from the page; prediction exposes shallower understanding than summary recall.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The local workflow and scaffold are known, but their learning effectiveness and aesthetic suitability across audiences remain unmeasured.
- **supporting_reason:** The thesis must not turn local design preference into a universal cognitive claim.
- **counterargument_or_limit:** Lack of formal study does not erase practical value observed by the workflow's authors.
- **assumptions_and_boundaries:** Treat source-grounding and artifact constraints as instructions, and treat comprehension effects as hypotheses to measure.
- **revision_decision:** Label the synthesis as combined local evidence and engineering inference, with external freshness explicitly unresolved.
- **additional_insight_to_add:** Honest status labels allow the same thesis to guide work while inviting evidence-driven adaptation.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** If the artifact's purpose is an inspectable mental model, then narrative order and interaction states become part of semantic correctness.
- **supporting_reason:** Hiding a caveat behind inaccessible navigation can change what the reader believes just as surely as an inaccurate sentence.
- **counterargument_or_limit:** Not every layout defect changes meaning; severity should reflect semantic and task impact.
- **assumptions_and_boundaries:** Review prioritizes failures that alter access, ordering, contrast, attribution, or causal interpretation.
- **revision_decision:** State that presentation defects are correctness defects when they change available or perceived information.
- **additional_insight_to_add:** This semantic view of presentation justifies testing reduced-motion, script-off, narrow-screen, and keyboard paths as alternate readings of the same argument.
## Section 005: Local Corpus Source Map
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed map names two local files and selected headings but does not guide the agent through the order or purpose of reading them.
- **supporting_reason:** Retrieval order matters because the entry skill establishes task boundaries while the detail pattern explains how to realize them.
- **counterargument_or_limit:** A fixed order is unnecessary once a maintainer already knows the package and needs only one narrow fact.
- **assumptions_and_boundaries:** First-time or cold-context work should read both mapped files completely before selecting guidance.
- **revision_decision:** Convert the source map into a reading sequence with extraction targets, authority roles, and stop conditions.
- **additional_insight_to_add:** Heading signals are navigation hints, not substitutes for reading surrounding caveats and examples.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** The best default is `SKILL.md` first, the elegant pattern second, then the linked script and template when artifact construction or behavior is in scope.
- **supporting_reason:** This moves from intent to method to executable implementation without letting template details define the problem prematurely.
- **counterargument_or_limit:** A task that only critiques an existing page may need the output artifact before the generator.
- **assumptions_and_boundaries:** The reading sequence adapts to the task while preserving complete inspection of all evidence used for claims.
- **revision_decision:** Add default and alternate retrieval paths, including existing-output-first for redesign or regression tasks.
- **additional_insight_to_add:** The artifact under review can outrank its generator for observed behavior while remaining lower authority for intended workflow.
### Question 03: When does the default work well?
- **current_section_observation:** The canonical-to-supporting sequence works well for creating a new explainer from mixed technical sources.
- **supporting_reason:** It first defines deliverable constraints and then supplies a narrative and component vocabulary that can be adapted.
- **counterargument_or_limit:** It provides little subject matter evidence; the actual system files still dominate factual content.
- **assumptions_and_boundaries:** These local explainer sources govern how to explain, not what the target system does.
- **revision_decision:** State explicitly that theme sources and subject sources are separate required inputs.
- **additional_insight_to_add:** Confusing those layers causes generic connector language to leak into unrelated domains through the scaffold.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The map fails when agents read only heading names, copy the default seven acts, or treat archived assets as the current runtime.
- **supporting_reason:** Those shortcuts ignore deletable sections, environmental differences, and the requirement to mirror source-specific nouns and verbs.
- **counterargument_or_limit:** A scaffold can still accelerate work when the author performs a deliberate replacement and deletion pass.
- **assumptions_and_boundaries:** Archived local sources describe the frozen package, not an automatically installed or active tool.
- **revision_decision:** Add failure warnings for partial reads, unverified execution, and scaffold literalism.
- **additional_insight_to_add:** A copied section title is a latent claim about subject structure and must be justified like prose.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** Retrieval may begin from instructions, an existing explainer, a failing rendered state, or a subject's implementation entry point.
- **supporting_reason:** Each starting point optimizes a different task: creation, style preservation, debugging, or factual reconstruction.
- **counterargument_or_limit:** Multiple entry paths can fragment review unless they converge on a shared evidence inventory.
- **assumptions_and_boundaries:** Every path must eventually reconcile observed output, local explainer convention, and subject truth.
- **revision_decision:** Include a task-to-starting-source guide beneath the map.
- **additional_insight_to_add:** Convergence matters more than identical reading order because unresolved disagreement is where explanatory defects hide.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Key local-source traps are stale relative links, reading generated examples as requirements, skipping source footers, and overlooking overwrite protection.
- **supporting_reason:** These details affect reproducibility, provenance, and whether a bootstrap command can destroy an existing artifact.
- **counterargument_or_limit:** The overwrite guard belongs to the archived generator and may differ in another implementation.
- **assumptions_and_boundaries:** Operational claims must name the exact artifact version observed.
- **revision_decision:** Add artifact-specific observations and prohibit generalizing them beyond the mapped package.
- **additional_insight_to_add:** Safety behavior in a helper script belongs in the author workflow even when it never appears in the explainer itself.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** Good retrieval extracts exact constraints and subject-neutral patterns; bad retrieval copies visual CSS; borderline retrieval reads prose but not linked behavior.
- **supporting_reason:** These examples distinguish learning the method from imitating its archived surface.
- **counterargument_or_limit:** CSS inspection is appropriate when diagnosing the bundled template or preserving an explicitly requested house style.
- **assumptions_and_boundaries:** Visual details become evidence only for tasks that name or inherit that specific template.
- **revision_decision:** Add usage examples that vary by creation, critique, and template-maintenance scenarios.
- **additional_insight_to_add:** The same file can be canonical for one decision and merely illustrative for another.
### Question 08: How can the important claims be verified?
- **current_section_observation:** A local map can be verified through path existence, complete reads, linked-resource resolution, and comparison between instructions and implementation.
- **supporting_reason:** These checks catch missing evidence and intent-behavior drift before page authoring begins.
- **counterargument_or_limit:** Reading completion is difficult to prove mechanically without reducing it to superficial access logs.
- **assumptions_and_boundaries:** The journal should record inspected paths and semantic findings rather than private reasoning transcripts.
- **revision_decision:** Add compact evidence-record requirements and concrete cross-check questions.
- **additional_insight_to_add:** A useful read record names the decision changed by a source, not merely that a file was opened.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** File content and linked implementation behavior are known from complete reads, while source hierarchy labels are an informed local interpretation.
- **supporting_reason:** The skill declares resources and workflow, but it does not formally assign every file an authority rank.
- **counterargument_or_limit:** Calling the entry skill canonical remains practical because it is the package's declared activation surface.
- **assumptions_and_boundaries:** Hierarchy terms guide this reference and do not alter ownership or archive status.
- **revision_decision:** Keep categorical roles while noting that task-specific evidence can alter precedence.
- **additional_insight_to_add:** Authority should be decided per claim, especially when implemented behavior contradicts prose intent.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The local corpus separates reusable explainer method from subject evidence, implying a two-axis source model.
- **supporting_reason:** One axis answers how to communicate; the other answers what is true about the system being communicated.
- **counterargument_or_limit:** Some sources, such as an existing explainer, contain both method and subject claims.
- **assumptions_and_boundaries:** Mixed sources should be decomposed by claim role rather than assigned one global label.
- **revision_decision:** Add a two-axis retrieval note and require both axes before drafting claims.
- **additional_insight_to_add:** This separation allows a visual pattern to transfer across domains without transferring its example system's accidental semantics.
## Section 006: External Research Source Map
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed external map lists three broad URLs without saying whether external research is required for the current recommendation or what question each source should answer.
- **supporting_reason:** A decision-oriented map prevents browsing from becoming ceremonial and keeps uninspected links from inheriting factual authority.
- **counterargument_or_limit:** Future maintainers may discover more relevant primary sources than the inherited list.
- **assumptions_and_boundaries:** This no-browse evolution preserves pointers but makes no claim about their current content.
- **revision_decision:** Recast the map as a refresh queue with trigger, expected contribution, insufficiency warning, and evidence-record requirement.
- **additional_insight_to_add:** External research should begin from an unresolved decision, not from a desire to make the bibliography look complete.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** Local sources are sufficient for repository workflow defaults, while externally sensitive claims should remain unknown until authorized primary-source inspection.
- **supporting_reason:** This preserves useful local guidance without laundering stale or adjacent public material into normative web advice.
- **counterargument_or_limit:** Delaying external review can leave important accessibility or browser constraints undiscovered during early design.
- **assumptions_and_boundaries:** High-consequence public delivery should authorize and complete relevant standards research before implementation acceptance.
- **revision_decision:** Make local guidance the current default and define research triggers for normative, versioned, compatibility, and automation claims.
- **additional_insight_to_add:** Unknown external status is a planning input that may narrow the artifact's declared support rather than blocking every internal draft.
### Question 03: When does the default work well?
- **current_section_observation:** A local-only evidence base works for frozen-reference synthesis and internal prototypes that make no current ecosystem claim.
- **supporting_reason:** The author can still verify source fidelity and observed browser behavior within declared local targets.
- **counterargument_or_limit:** Observing one browser locally does not establish portability, conformance, or broad accessibility.
- **assumptions_and_boundaries:** Claims must remain limited to inspected local sources and recorded test environments.
- **revision_decision:** Add examples of safe local claims and prohibited generalizations.
- **additional_insight_to_add:** Narrow evidence can support a narrow claim strongly when environment and scope are stated precisely.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** Deferring research fails when the page is public, regulated, dependent on current APIs, or expected to work across an explicit browser matrix.
- **supporting_reason:** Those contexts require normative and version-specific evidence beyond an archived template.
- **counterargument_or_limit:** External documentation can still be incomplete or wrong for the actual runtime, so direct testing remains necessary.
- **assumptions_and_boundaries:** Research complements artifact evidence and does not replace it.
- **revision_decision:** Add mandatory-refresh triggers and require both primary documentation and observed behavior where practical.
- **additional_insight_to_add:** The cost of stale research rises with the gap between authored assumptions and the reader's execution environment.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** Alternatives include no refresh, targeted primary-source review, broad ecosystem survey, or empirical browser testing without documentation.
- **supporting_reason:** Targeted review minimizes context and freshness cost, while broad surveys may reveal conventions but carry weaker authority and more noise.
- **counterargument_or_limit:** A narrow search can miss a decisive constraint that the author did not know to ask about.
- **assumptions_and_boundaries:** Start targeted, then broaden only when contradictions or missing coverage remain.
- **revision_decision:** Describe a question-first escalation path from primary docs to examples and direct tests.
- **additional_insight_to_add:** Research breadth should expand in response to uncertainty, not page ambition alone.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Broad documentation roots, redirected pages, version drift, search snippets, and adjacent agent guidance can all appear relevant without supporting a specific HTML claim.
- **supporting_reason:** Citation presence does not establish entailment, freshness, or applicability.
- **counterargument_or_limit:** Root pages can still be useful navigation starting points when treated honestly.
- **assumptions_and_boundaries:** Final evidence must link to the precise inspected page and record the supported proposition.
- **revision_decision:** Add an insufficiency column and a rule against citing search results or broad roots as final proof.
- **additional_insight_to_add:** The reviewer should be able to remove a source and name exactly which recommendation loses support.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** Good external evidence answers a named current question; bad evidence is an unvisited URL; borderline evidence is current but adjacent to the claim.
- **supporting_reason:** These distinctions expose why reputable domains can still be weak support.
- **counterargument_or_limit:** Adjacent sources may contribute useful analogies or process ideas when labeled as inference.
- **assumptions_and_boundaries:** Analogy must never be presented as normative HTML behavior.
- **revision_decision:** Encode good evidence records in the refresh protocol and keep current rows visibly pending.
- **additional_insight_to_add:** Relevance is relational: it exists between a source passage and a claim, not between a website and a theme name.
### Question 08: How can the important claims be verified?
- **current_section_observation:** A refreshed row needs inspection date, exact page, relevant section, extracted claim, applicability, and an artifact test where behavior is observable.
- **supporting_reason:** That record makes freshness and entailment reviewable without preserving a raw browsing transcript.
- **counterargument_or_limit:** Dates do not guarantee stability, and quoted sections may change without obvious version markers.
- **assumptions_and_boundaries:** Refresh cadence should follow dependency volatility and consequence rather than a universal interval.
- **revision_decision:** Add a minimum external evidence packet and stale-state rule.
- **additional_insight_to_add:** Store the smallest reviewable citation record that can reproduce the decision, not an indiscriminate page dump.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The URLs and inherited role labels are known from the seed; their availability, content, and relevance today remain unverified.
- **supporting_reason:** No network retrieval occurred, as required by the task.
- **counterargument_or_limit:** Their domain names provide weak contextual clues, but those clues cannot support detailed recommendations.
- **assumptions_and_boundaries:** All current external rows carry pending status regardless of presumed publisher authority.
- **revision_decision:** State the no-browse boundary above and below the table and avoid `external_research_sourced_fact` claims beyond pointer provenance.
- **additional_insight_to_add:** A pending source can still be valuable when its unresolved question and activation trigger are explicit.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The inherited links focus on agent instructions and automation rather than core HTML semantics, revealing a coverage mismatch.
- **supporting_reason:** That mismatch means future research should be selected from the actual unresolved web, accessibility, or browser decision.
- **counterargument_or_limit:** Agent and automation sources may still matter for repository workflow and repeatable verification.
- **assumptions_and_boundaries:** Their role is process-adjacent unless a precise inspected passage connects them to the artifact workflow.
- **revision_decision:** Preserve them as secondary leads and require future refreshers to add better primary sources when the claim demands it.
- **additional_insight_to_add:** A source map should expose coverage holes, not hide them behind the number of rows.
## Section 007: Anti Pattern Registry Table
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed registry names three generic evidence failures but omits the content, narrative, visual, accessibility, and scaffold failures specific to HTML explainers.
- **supporting_reason:** Authors need to recognize when an apparently polished page should be blocked, repaired, narrowed, or replaced.
- **counterargument_or_limit:** A registry cannot enumerate every browser defect or subject-specific misinformation risk.
- **assumptions_and_boundaries:** It should prioritize recurring failures with high impact on truth, comprehension, access, or reproducibility.
- **revision_decision:** Expand the registry into theme-specific anti-patterns with detection signals, consequence, repair, and stop condition.
- **additional_insight_to_add:** Anti-patterns are most useful when they describe observable artifact behavior instead of presumed author intent.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** The safest default is to block unsupported mechanics, hidden essential content, and unreplaced scaffold assumptions before reviewing decorative quality.
- **supporting_reason:** Those failures corrupt the explanation's meaning or accessibility and cannot be offset by visual polish.
- **counterargument_or_limit:** A block-everything posture can delay low-risk internal drafts where uncertainty is visibly disclosed.
- **assumptions_and_boundaries:** Severity depends on whether the artifact is exploratory, shared, decision-bearing, or public.
- **revision_decision:** Add severity and response guidance that distinguishes block, repair, and document decisions.
- **additional_insight_to_add:** A disclosed draft can tolerate incompleteness, but it cannot label invented behavior as settled fact.
### Question 03: When does the default work well?
- **current_section_observation:** Registry-first review works during scaffold cleanup, content critique, browser QA, and pre-publication acceptance.
- **supporting_reason:** Named patterns help independent reviewers classify the same symptom and choose a consistent response.
- **counterargument_or_limit:** Early ideation may benefit from rough metaphors or incomplete components that would fail a final registry.
- **assumptions_and_boundaries:** Draft artifacts need visible provisional status and a scheduled reconciliation pass.
- **revision_decision:** Apply the full registry at acceptance and a smaller truth-and-safety subset during exploration.
- **additional_insight_to_add:** Stage-aware enforcement keeps creative sketches cheap without allowing provisional shortcuts to become durable content accidentally.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** A static anti-pattern list fails when reviewers use it mechanically without considering audience, semantic impact, or intentional adaptation.
- **supporting_reason:** For example, asymmetric cards may be correct, motion may be absent by design, and a long page may be necessary for a bounded complex story.
- **counterargument_or_limit:** Context should not become an excuse to waive source fidelity or essential access.
- **assumptions_and_boundaries:** Exceptions require a rationale and evidence that the underlying risk is controlled another way.
- **revision_decision:** Add a waiver rule tied to the failure prevented rather than surface conformance.
- **additional_insight_to_add:** Good review asks whether a risk exists, not whether the artifact resembles the preferred component palette.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** Failure controls can be expressed as a registry, checklist, lint rule, browser test, content review, or reader study.
- **supporting_reason:** Machine checks scale for syntax and residue, while humans assess causal accuracy and actual comprehension.
- **counterargument_or_limit:** Reader studies offer strong outcome evidence but may be too costly for a short-lived internal page.
- **assumptions_and_boundaries:** Use the cheapest method capable of detecting the specific failure with acceptable confidence.
- **revision_decision:** Map each anti-pattern to its primary detection mode and avoid implying one verifier covers all risks.
- **additional_insight_to_add:** Combining independent weak signals can be stronger than overclaiming certainty from one screenshot or lint pass.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Highest-impact traps are source-free claims, buried heartbeat, metaphor substitution, scaffold residue, false symmetry, script-hidden content, keyboard dead ends, and unreadable narrow layouts.
- **supporting_reason:** Each can materially change what a reader understands or can reach.
- **counterargument_or_limit:** External font failure, subtle motion, and minor style inconsistency usually have lower semantic impact.
- **assumptions_and_boundaries:** Severity rises when a lower-level defect makes essential content unavailable or falsely prioritized.
- **revision_decision:** Order registry rows by semantic and access consequence rather than visual annoyance.
- **additional_insight_to_add:** Several minor defects can combine into a major failure when they all burden the same reader path.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** Good pages bind metaphors to mechanics and delete unused acts; bad pages paste generic scaffold copy; borderline pages disclose uncertainty but leave weak navigation.
- **supporting_reason:** Examples show that one artifact can pass content integrity while still needing interaction repair.
- **counterargument_or_limit:** Labels should apply to behaviors, not globally brand an entire page as good or bad.
- **assumptions_and_boundaries:** Review records each finding with location, impact, and recovery action.
- **revision_decision:** Put concrete bad signals and safer replacements in each table row.
- **additional_insight_to_add:** Component-level findings support incremental repair without losing a page's valid narrative work.
### Question 08: How can the important claims be verified?
- **current_section_observation:** Registry verification requires source comparison, text scans, DOM inspection, script-off rendering, keyboard traversal, responsive screenshots, and console review.
- **supporting_reason:** These methods cover different failure classes and expose gaps hidden by a normal pointer-driven desktop pass.
- **counterargument_or_limit:** Passing these checks still does not prove a new reader formed the intended mental model.
- **assumptions_and_boundaries:** High-impact explainers should add a comprehension task or short target-reader review.
- **revision_decision:** Include detection methods and route outcome validation to the metrics section.
- **additional_insight_to_add:** A reviewer who can locate claims but cannot predict behavior reveals a narrative failure that static source traceability misses.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** Local sources explicitly reject invented behavior, metaphor replacement, detail overload, buried core loops, missing sources, and retained scaffold copy.
- **supporting_reason:** Those anti-patterns can be stated as direct local guidance.
- **counterargument_or_limit:** Severity ordering, accessibility extensions, and browser-fallback recommendations are engineering inferences not measured in the source package.
- **assumptions_and_boundaries:** Mark inferred controls and calibrate them to the artifact's declared audience and support matrix.
- **revision_decision:** Preserve evidence labels in the explanatory note around the table.
- **additional_insight_to_add:** Directly sourced prohibitions and inferred controls can coexist if their provenance and acceptance role remain visible.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** Many anti-patterns share a root cause: the scaffold or visual form begins making decisions before the evidence model is stable.
- **supporting_reason:** Addressing that root can prevent multiple downstream defects more efficiently than polishing each symptom.
- **counterargument_or_limit:** Some browser and accessibility defects arise even from a sound evidence model and still need direct engineering work.
- **assumptions_and_boundaries:** Root-cause repair complements, rather than replaces, artifact-specific verification.
- **revision_decision:** Add a diagnostic sequence from source model to narrative to component to runtime.
- **additional_insight_to_add:** Review findings should point to the earliest responsible layer so fixes do not repeatedly patch generated surface output.
## Section 008: Verification Gate Command Set
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed gives one repository verifier command but does not say what it validates or how to prove a produced HTML explainer works.
- **supporting_reason:** Reviewers must decide whether evidence covers reference integrity, HTML structure, rendered behavior, and semantic accuracy as distinct layers.
- **counterargument_or_limit:** No universal command set can know every repository's browser tooling or artifact path.
- **assumptions_and_boundaries:** The section should provide runnable local baselines and adaptation slots without claiming unavailable tools.
- **revision_decision:** Organize commands by preflight, artifact structure, rendered experience, and this-reference validation.
- **additional_insight_to_add:** A passing command only closes the failure class named by that gate; it should never imply whole-artifact correctness.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** The default gate should combine a clean bootstrap or direct-open check, scaffold scan, source review, browser matrix, keyboard path, and console inspection.
- **supporting_reason:** This combination spans generation safety, content completion, visual access, interaction, and runtime failures.
- **counterargument_or_limit:** A small internal static page may not justify a full automated browser matrix.
- **assumptions_and_boundaries:** Gate depth scales with audience reach, reuse, and consequence while essential source and local-open checks remain mandatory.
- **revision_decision:** Define minimum, maintained, and high-impact gate tiers.
- **additional_insight_to_add:** Tiering reduces both under-testing of durable artifacts and excessive ceremony for disposable explanations.
### Question 03: When does the default work well?
- **current_section_observation:** Layered gates work when the artifact has a stable output path and declared browser, viewport, input, and motion targets.
- **supporting_reason:** Explicit targets make failures reproducible and prevent reviewers from testing arbitrary conditions inconsistently.
- **counterargument_or_limit:** Early content drafts may not yet have a stable layout or complete support matrix.
- **assumptions_and_boundaries:** Draft gates can focus on source fidelity and static visibility before visual baselines stabilize.
- **revision_decision:** Sequence gates so cheap content failures stop expensive screenshot and interaction runs.
- **additional_insight_to_add:** Verification order should follow expected information value, not merely tool availability.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** Command-heavy guidance fails when copied commands reference absent tools, pass against the wrong file, or produce screenshots nobody inspects.
- **supporting_reason:** Ritual execution creates evidence volume without decision value.
- **counterargument_or_limit:** Reusable command templates are still helpful when their variables and assumptions are explicit.
- **assumptions_and_boundaries:** Every command record needs working directory, target artifact, environment, exit status, and interpretation.
- **revision_decision:** Mark environment-dependent examples and require reviewers to record the actual command used.
- **additional_insight_to_add:** Evidence becomes stale when the artifact bytes change, even if the command itself remains current.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** Alternatives include manual browser review, headless automation, static parsing, accessibility scanners, screenshot comparison, and target-reader walkthroughs.
- **supporting_reason:** Automation improves repeatability while human and reader review catch semantic and comprehension failures inaccessible to syntax tools.
- **counterargument_or_limit:** Screenshot baselines can become noisy under font, browser, or rendering changes unrelated to meaning.
- **assumptions_and_boundaries:** Use visual diffs for stable high-value regions and semantic assertions for critical content and navigation.
- **revision_decision:** Pair each method with its coverage and blind spot rather than prescribing one stack.
- **additional_insight_to_add:** A resilient gate uses overlapping evidence where failure cost is high and cheap single checks where it is low.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Gate risks include testing only desktop, relying on hover, omitting script-off behavior, ignoring external font failure, and scanning for too few scaffold phrases.
- **supporting_reason:** The bundled template itself includes hidden mobile navigation, scroll observers, and an external font import that create alternate conditions.
- **counterargument_or_limit:** Not every generated page retains those exact template behaviors after adaptation.
- **assumptions_and_boundaries:** Inspect actual artifact source before selecting runtime scenarios.
- **revision_decision:** Add scenario derivation from retained dependencies and components.
- **additional_insight_to_add:** Test cases should shrink when a risky component is removed, rewarding simpler artifacts with lower maintenance cost.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** A good gate names artifact, condition, expected result, and evidence; a bad gate says "looks good"; a borderline gate captures screenshots without interaction or claim review.
- **supporting_reason:** Complete gate records let another reviewer reproduce both the setup and verdict.
- **counterargument_or_limit:** Some exploratory visual judgments remain qualitative even with a clear record.
- **assumptions_and_boundaries:** Qualitative findings should still identify viewport, location, symptom, and consequence.
- **revision_decision:** Provide a compact evidence packet schema following the commands.
- **additional_insight_to_add:** Reproducible qualitative evidence is more useful than a precise metric with an undefined measurement path.
### Question 08: How can the important claims be verified?
- **current_section_observation:** Important claims include local opening, no scaffold residue, complete source footer, visible essential content, navigability, responsive fit, and accurate mechanism.
- **supporting_reason:** Each claim maps to a distinct command, browser action, or human comparison.
- **counterargument_or_limit:** Comprehension cannot be inferred solely from DOM presence or screenshot layout.
- **assumptions_and_boundaries:** Add a reader prediction task when the page informs onboarding or consequential decisions.
- **revision_decision:** Build a claim-to-gate matrix and state pass, fail, and not-evaluated outcomes.
- **additional_insight_to_add:** `Not evaluated` is a valid result that prevents missing coverage from being silently counted as pass.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The archive verifier command is known from the seed, and the bootstrap interface is known from inspected code; browser-tool commands are repository-dependent.
- **supporting_reason:** Separating fixed local commands from adaptable examples prevents false portability.
- **counterargument_or_limit:** Even known commands may fail if run from a different working directory or missing archived dependencies.
- **assumptions_and_boundaries:** Commands state their expected working directory and purpose, not universal availability.
- **revision_decision:** Preserve the known verifier, add standard-library checks, and describe browser acceptance without inventing a package manager.
- **additional_insight_to_add:** Tool-neutral acceptance criteria survive tool migration better than a command list alone.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** Verification design feeds back into page design because each dependency, interaction, and hidden state adds a scenario that must be proved.
- **supporting_reason:** Authors can reduce verification burden by making essential content static, reducing motion, and eliminating unnecessary external assets.
- **counterargument_or_limit:** Simplicity should not remove an interaction that materially improves understanding for the target audience.
- **assumptions_and_boundaries:** Retain complexity when its explanatory benefit is named and tested.
- **revision_decision:** Add a verification-cost question to component review.
- **additional_insight_to_add:** The cheapest reliable test is often architectural: design the page so the failure cannot hide essential meaning.
## Section 009: Agent Usage Decision Guide
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed trigger is theme-name matching, which does not tell an agent whether to create, adapt, diagnose, review, or route away from an HTML explainer.
- **supporting_reason:** Mode selection changes the evidence order, permissible edits, verification scope, and expected output.
- **counterargument_or_limit:** Real tasks can combine modes, such as correcting source claims while redesigning a broken page.
- **assumptions_and_boundaries:** Choose a primary mode and record secondary obligations rather than forcing one label.
- **revision_decision:** Add a mode table with triggers, first reads, required actions, stop conditions, and completion evidence.
- **additional_insight_to_add:** Mode ambiguity is an early warning that the requested artifact or ownership boundary may need clarification.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** The default agent sequence is clarify audience question, inspect subject evidence, inspect local method sources, outline the causal journey, build, and verify.
- **supporting_reason:** This order prevents the scaffold from selecting the story and gives every component an evidence-backed purpose.
- **counterargument_or_limit:** For an observed rendering bug, reproducing the artifact should precede broad source reconstruction.
- **assumptions_and_boundaries:** Diagnosis mode starts from the symptom but still checks source meaning before declaring repair complete.
- **revision_decision:** State a default sequence plus mode-specific entry-point exceptions.
- **additional_insight_to_add:** Starting point may vary, but all successful paths converge on evidence, narrative, artifact, and proof.
### Question 03: When does the default work well?
- **current_section_observation:** The sequence works for new explainers when the task supplies or permits access to bounded implementation and design sources.
- **supporting_reason:** The agent can derive the thesis, actors, state, failures, and final compression before investing in layout.
- **counterargument_or_limit:** Sparse or conflicting sources may prevent an honest causal story.
- **assumptions_and_boundaries:** The agent may narrow scope and expose uncertainty but must not fill missing mechanics from convention.
- **revision_decision:** Add a source-sufficiency checkpoint before implementation.
- **additional_insight_to_add:** A smaller accurate explainer is a successful outcome when evidence cannot support the requested breadth.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The guide fails if agents treat any request for visuals as permission to build HTML or overwrite an existing artifact.
- **supporting_reason:** Medium and edit authority are separate decisions that require explicit fit and ownership evidence.
- **counterargument_or_limit:** Direct implementation is appropriate when the request, scope, and exclusive file ownership are already clear.
- **assumptions_and_boundaries:** Shared workspaces require strict path ownership and preservation of concurrent edits.
- **revision_decision:** Add route-away and stop-before-write conditions, including unclear ownership and missing required sources.
- **additional_insight_to_add:** The safest agent can still be proactive by producing a bounded evidence map while waiting on a genuinely blocking decision.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** Agents can output Markdown guidance, an ASCII or Mermaid diagram, a standalone page, a reusable template change, or a full application.
- **supporting_reason:** These outputs differ in portability, maintenance, interaction, visual control, and ownership surface.
- **counterargument_or_limit:** A user may explicitly require HTML even when another medium would be cheaper.
- **assumptions_and_boundaries:** Honor explicit output requirements while communicating material risks and narrowing unsupported features.
- **revision_decision:** Include an output-routing branch tied to essential experience rather than agent preference.
- **additional_insight_to_add:** Medium choice should be revisited when requirements change from explanation to repeated user operation.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Agent-specific traps include partial source reads, silent redesign, bulk scaffold retention, unsaved multi-section work, and completion claims without browser evidence.
- **supporting_reason:** These behaviors create drift, merge risk, and unverifiable output even when prose quality is high.
- **counterargument_or_limit:** Not every workflow needs per-section persistence, but this shared evolution task explicitly does.
- **assumptions_and_boundaries:** The guide distinguishes general explainer defaults from current-task coordination requirements.
- **revision_decision:** Add operational discipline covering source completion, edit boundaries, incremental saves, and evidence-before-claim.
- **additional_insight_to_add:** Agent reliability includes preserving the workspace's coordination model, not only producing correct artifact content.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** A good agent narrows a sparse story, a bad agent invents missing transitions, and a borderline agent builds accurate content in the wrong medium.
- **supporting_reason:** These cases expose independent dimensions of truth, scope, and format fit.
- **counterargument_or_limit:** Medium mismatch can be acceptable when the user prioritizes a specific deliverable for integration reasons.
- **assumptions_and_boundaries:** The agent records the tradeoff and verifies the required medium's weakest path.
- **revision_decision:** Add examples to mode rows and connect developed scenarios to Section 010.
- **additional_insight_to_add:** Correct content in an unusable artifact is incomplete, while usable presentation of incorrect content is unacceptable.
### Question 08: How can the important claims be verified?
- **current_section_observation:** Agent completion should be checked against read inventory, claim ledger, changed-path list, artifact behavior, and unresolved-risk record.
- **supporting_reason:** These signals reveal both semantic and coordination failures.
- **counterargument_or_limit:** A checklist can be filled performatively unless outputs and commands are inspectable.
- **assumptions_and_boundaries:** Evidence references actual paths, hashes, screenshots, and concise command results.
- **revision_decision:** Add per-mode exit evidence and a universal completion gate.
- **additional_insight_to_add:** Exit evidence should let another agent resume or challenge the work without reconstructing the full conversation.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** Local source order and artifact constraints are explicit; task-mode taxonomy and stopping thresholds are synthesized engineering guidance.
- **supporting_reason:** The taxonomy operationalizes source rules without claiming it was measured by the archived skill.
- **counterargument_or_limit:** Teams may define different review roles, artifact lifecycles, or ownership mechanisms.
- **assumptions_and_boundaries:** Adapt role names while preserving the underlying evidence and safety decisions.
- **revision_decision:** Label mode guidance as combined inference grounded in local constraints.
- **additional_insight_to_add:** A portable decision guide specifies obligations rather than assuming one agent framework's tool vocabulary.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The same explainer may move through creation, review, diagnosis, and refresh modes over its lifetime.
- **supporting_reason:** Designing handoff evidence at creation time reduces later maintenance and debugging cost.
- **counterargument_or_limit:** One-off artifacts may not justify extensive lifecycle metadata.
- **assumptions_and_boundaries:** Retention depth scales with expected reuse and harm from staleness.
- **revision_decision:** Add lifecycle handoff fields to the universal completion evidence.
- **additional_insight_to_add:** Source lists, declared targets, and final compression form a compact maintenance contract for future mode transitions.
## Section 010: User Journey Scenario
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed names a generic reader and task but does not show how evidence, narrative, implementation, and verification decisions unfold in practice.
- **supporting_reason:** A complete journey demonstrates how the reference changes concrete actions and where the author should stop or adapt.
- **counterargument_or_limit:** One scenario cannot represent every audience, subject type, or repository workflow.
- **assumptions_and_boundaries:** The journey should be explicitly illustrative and expose transferable decisions rather than pretend to be production history.
- **revision_decision:** Build a bounded onboarding scenario from request through handoff, with decision points and evidence artifacts at each stage.
- **additional_insight_to_add:** A scenario is valuable when readers can substitute their own actors and still retain the decision sequence.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** The scenario should begin with the reader's prediction goal, not with page layout or a generic desire for better documentation.
- **supporting_reason:** A prediction goal determines which mechanics, failures, and state transitions deserve explanation.
- **counterargument_or_limit:** Some executive explainers aim at decision comparison rather than operational prediction.
- **assumptions_and_boundaries:** In those cases, the equivalent goal is a specific choice the reader can justify after the page.
- **revision_decision:** Give the example reader a concrete question about restart and duplicate behavior.
- **additional_insight_to_add:** Prediction tasks reveal causal understanding more reliably than asking whether a page was clear.
### Question 03: When does the default work well?
- **current_section_observation:** A lifecycle scenario works when subject sources expose initialization, processing, persistence, failure, and recovery.
- **supporting_reason:** The page can stage these relations while preserving a clear heartbeat.
- **counterargument_or_limit:** Sparse evidence may only support an architecture map or interface comparison.
- **assumptions_and_boundaries:** The scenario's artifact scope must contract when source coverage does.
- **revision_decision:** Include an explicit sufficiency decision before outlining acts.
- **additional_insight_to_add:** Scope negotiation is part of the user journey, not a backstage authoring concern.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The journey would fail if it implies an agent can infer delivery guarantees from retry code or template examples alone.
- **supporting_reason:** Guarantees emerge from combined state, ordering, acknowledgment, persistence, and failure semantics.
- **counterargument_or_limit:** A page can still explain observed behavior without naming a formal guarantee.
- **assumptions_and_boundaries:** Unproven semantics are labeled as unknown and routed to source owners.
- **revision_decision:** Add a decision point where the author excludes or qualifies a guarantee lacking evidence.
- **additional_insight_to_add:** Showing what the page refuses to claim teaches evidence discipline more effectively than a flawless happy path.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The scenario should compare a standalone journey against a long Markdown note and a live debugging dashboard.
- **supporting_reason:** This demonstrates why the selected medium fits onboarding while acknowledging that operations need different tools.
- **counterargument_or_limit:** A Markdown note may be sufficient if diagrams and interaction add little to the causal model.
- **assumptions_and_boundaries:** The illustrative system has sequential state and a recovery branch that benefit from staged visual explanation.
- **revision_decision:** Record the medium choice and keep the dashboard outside explainer scope.
- **additional_insight_to_add:** A good explainer can prepare readers to use an operational tool without attempting to become that tool.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Scenario risks include fabricated source paths, overly idealized review, omitted narrow-screen checks, and a conclusion unsupported by reader feedback.
- **supporting_reason:** These details can turn an educational example into disguised evidence or an unrealistic success story.
- **counterargument_or_limit:** Excessive caveats can make the journey difficult to follow.
- **assumptions_and_boundaries:** A short evidence-status note can preserve honesty without interrupting every step.
- **revision_decision:** Label all actors, paths, timings, and outcomes as illustrative unless tied to the mapped local corpus.
- **additional_insight_to_add:** Hypothetical scenarios should be realistic in process while remaining modest about outcomes.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** A good journey shows decisions and rejected claims; a bad journey jumps from request to polished page; a borderline journey verifies rendering but not understanding.
- **supporting_reason:** Contrasting these paths reveals the hidden work the reference is meant to make explicit.
- **counterargument_or_limit:** Reader feedback may be unavailable for a short-lived internal artifact.
- **assumptions_and_boundaries:** In that case, report comprehension as not evaluated rather than inferred from author review.
- **revision_decision:** End the scenario with both artifact evidence and a small reader prediction check.
- **additional_insight_to_add:** An incorrect reader prediction is design input, not merely a pass-fail score.
### Question 08: How can the important claims be verified?
- **current_section_observation:** The scenario can verify source coverage, narrative placement, scaffold cleanup, local opening, alternate reading paths, and the reader's recovery prediction.
- **supporting_reason:** These checks connect abstract guidance to observable outputs.
- **counterargument_or_limit:** A single reader does not establish general comprehension.
- **assumptions_and_boundaries:** The example records individual evidence and avoids population-level claims.
- **revision_decision:** Include a final evidence packet with pass, fail, and unresolved items.
- **additional_insight_to_add:** Scenario evidence should show one repaired failure so verification appears diagnostic rather than ceremonial.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The workflow steps derive from local guidance, while the example system, reader response, and artifact results are invented for illustration.
- **supporting_reason:** Explicit status prevents the journey from being mistaken for a measured case study.
- **counterargument_or_limit:** Illustrative detail can still encode plausible but domain-specific assumptions.
- **assumptions_and_boundaries:** Transfer the process, not the example's technical semantics or thresholds.
- **revision_decision:** Place an evidence-boundary note before the scenario and avoid unsupported metrics.
- **additional_insight_to_add:** An example becomes safer when it names which details readers must replace with their own evidence.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The journey shows that authoring is a sequence of narrowing decisions rather than a linear page-production task.
- **supporting_reason:** Each gate reduces uncertainty about audience, truth, structure, runtime, or comprehension before downstream investment.
- **counterargument_or_limit:** Real work often loops when rendering or reader review exposes an earlier model error.
- **assumptions_and_boundaries:** The scenario should include a feedback loop rather than imply one-pass completion.
- **revision_decision:** Add a reader misunderstanding that sends the author back to the state-and-recovery act.
- **additional_insight_to_add:** The fastest path to a durable explainer may include deliberate rework at the first point where a wrong mental model becomes observable.
## Section 011: Decision Tradeoff Guide
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed table offers only theme-level adopt, adapt, and avoid choices, leaving concrete design and architecture tradeoffs unresolved.
- **supporting_reason:** Authors need to choose not just whether to use the pattern, but how much narrative, runtime, visual, and maintenance complexity to accept.
- **counterargument_or_limit:** A comprehensive tradeoff matrix can become a substitute for audience judgment.
- **assumptions_and_boundaries:** The guide should frame consequential choices and require task-specific evidence rather than produce an automatic design.
- **revision_decision:** Expand the table across medium, packaging, scaffold, pacing, visuals, interaction, dependencies, detail, and review depth.
- **additional_insight_to_add:** The cost of a choice includes its future verification and refresh burden, not only initial build effort.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** Recommended defaults favor bounded scope, one file, source-named mechanics, early causal structure, static essential content, and minimal dependencies.
- **supporting_reason:** These choices maximize portability and reduce hidden states while preserving the local narrative method.
- **counterargument_or_limit:** Richer interactions or shared assets may materially improve a long-lived explainer family.
- **assumptions_and_boundaries:** Departures are justified by a named reader benefit and supported by proportionate tests.
- **revision_decision:** Give each row a conservative default plus explicit promotion conditions.
- **additional_insight_to_add:** Complexity earns its place only when the improvement survives comparison against a simpler artifact.
### Question 03: When does the default work well?
- **current_section_observation:** Conservative defaults work for internal onboarding, design walkthroughs, bounded architecture stories, and repository-local handoffs.
- **supporting_reason:** These uses value direct opening, inspectable source, and clear sequencing more than dynamic data.
- **counterargument_or_limit:** Public education, multilingual delivery, or repeated interactive exploration may need stronger infrastructure.
- **assumptions_and_boundaries:** Audience reach and artifact lifetime influence packaging and review decisions.
- **revision_decision:** Add context signals that move a choice from default to adaptation.
- **additional_insight_to_add:** Reuse converts a one-file convenience into a potential duplication cost, so architecture should be reconsidered at that boundary.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** Defaults fail when they force oversized inline media, inaccessible custom controls, unmaintainable duplication, or a narrative that hides lookup needs.
- **supporting_reason:** The medium's strengths become liabilities when requirements shift from guided reading to stateful operation or systematic reference.
- **counterargument_or_limit:** A companion artifact can absorb secondary requirements without replacing the explainer.
- **assumptions_and_boundaries:** Split responsibilities when one page cannot satisfy both journey and operational surface cleanly.
- **revision_decision:** Add avoid and split signals for each major tradeoff.
- **additional_insight_to_add:** The correct response to scope pressure is often another artifact, not another component inside the same page.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** Material alternatives include Markdown versus HTML, single file versus built site, static versus interactive, inline versus external assets, and concise versus exhaustive content.
- **supporting_reason:** Each pair changes portability, visual control, reuse, failure states, and reviewer effort.
- **counterargument_or_limit:** Binary framing can hide intermediate options such as a mostly static page with one accessible control.
- **assumptions_and_boundaries:** Treat choices as continuums and select the smallest sufficient point.
- **revision_decision:** Describe default, adapt-when, avoid-when, and proof for each option rather than declaring winners universally.
- **additional_insight_to_add:** Tradeoffs become manageable when the chosen point is tied to one essential reader task.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Hidden costs include external font dependence, screenshot instability, duplicated styles, motion preferences, table overflow, and source excerpts that drift.
- **supporting_reason:** These concerns often appear only after the first polished render and can dominate maintenance.
- **counterargument_or_limit:** Some costs are acceptable for a short-lived artifact with a narrow known environment.
- **assumptions_and_boundaries:** Temporary exceptions still need declared environment and lifetime.
- **revision_decision:** Add downstream cost and verification questions to the guide.
- **additional_insight_to_add:** A short-lived page should be cheap to delete, while a long-lived page should be cheap to refresh.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** Good choices name benefit and proof; bad choices copy template defaults; borderline choices add complexity for plausible but unmeasured value.
- **supporting_reason:** The contrast makes design rationale reviewable without privileging taste.
- **counterargument_or_limit:** Early prototypes often test plausible value before measurement exists.
- **assumptions_and_boundaries:** Prototype complexity is temporary and must be evaluated before acceptance.
- **revision_decision:** Put a verification question beside every tradeoff row.
- **additional_insight_to_add:** A borderline feature should have an expiration condition so experiments do not become permanent by inertia.
### Question 08: How can the important claims be verified?
- **current_section_observation:** Tradeoff validation requires comparing alternatives against reader outcome, artifact size, failure modes, and maintenance cost.
- **supporting_reason:** A chosen option is defensible only relative to the simpler or more capable alternative it displaced.
- **counterargument_or_limit:** Maintenance cost estimates remain uncertain before the artifact experiences change.
- **assumptions_and_boundaries:** Record assumptions and revisit them at the first meaningful refresh.
- **revision_decision:** Add proof prompts and refresh triggers rather than fabricated cost numbers.
- **additional_insight_to_add:** The first update provides valuable empirical evidence about whether the original packaging choice was sound.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** Single-file, inline, restrained, source-first guidance is locally explicit; its optimality under every workload is not.
- **supporting_reason:** The guide can recommend the local baseline while exposing conditions that weaken it.
- **counterargument_or_limit:** Even adaptation conditions are engineering judgments without corpus-wide outcome data.
- **assumptions_and_boundaries:** Project owners decide acceptable cost, support matrix, and lifetime.
- **revision_decision:** Mark defaults as local and proofs as task-specific.
- **additional_insight_to_add:** Transparent tradeoffs make deviation safer than rigid conformance because reviewers can see what new risks were accepted.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** Many decisions couple: external assets affect local opening, motion affects accessibility tests, and reusable components affect single-file portability.
- **supporting_reason:** Evaluating rows independently can miss compound failure and cost.
- **counterargument_or_limit:** Modeling every interaction would make the guide unusable.
- **assumptions_and_boundaries:** Call out the highest-leverage couplings and rely on artifact verification for the rest.
- **revision_decision:** Add a coupling note beneath the table and require re-evaluation when two adapted choices interact.
- **additional_insight_to_add:** Two individually reasonable exceptions can jointly invalidate the original default's portability or accessibility argument.
## Section 012: Local Corpus Hierarchy
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed labels one file canonical and one supporting but does not explain how authority changes across workflow, narrative, generator, template, and subject claims.
- **supporting_reason:** Claim-level hierarchy resolves apparent conflicts more accurately than assigning one global rank to an entire artifact.
- **counterargument_or_limit:** Fine-grained authority can feel complex for a small two-file corpus.
- **assumptions_and_boundaries:** Linked assets and task-specific subject sources create enough role diversity to justify the distinction.
- **revision_decision:** Define hierarchy roles, precedence rules, conflict handling, and reviewer questions by claim type.
- **additional_insight_to_add:** Canonical status is scoped power, not a blanket statement that one file overrides all observable behavior.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** Use the entry skill for activation and deliverable intent, the pattern for narrative detail, executable artifacts for their observed behavior, and subject sources for technical truth.
- **supporting_reason:** Each source answers the question closest to its purpose and evidence form.
- **counterargument_or_limit:** Prose intent may deliberately describe desired behavior not yet implemented.
- **assumptions_and_boundaries:** Inconsistency should be reported as drift rather than silently resolved in favor of code or prose.
- **revision_decision:** Add precedence by decision plus an explicit contradiction state.
- **additional_insight_to_add:** Desired and actual behavior are separate facts that may both belong in a maintenance finding.
### Question 03: When does the default work well?
- **current_section_observation:** Role-based hierarchy works when sources are versioned together and their ownership or linkage is visible.
- **supporting_reason:** Reviewers can trace a recommendation upstream and assign repair to the responsible layer.
- **counterargument_or_limit:** Forked templates or copied scripts may no longer share the same intent source.
- **assumptions_and_boundaries:** Copied artifacts need provenance and local override records.
- **revision_decision:** Add a rule that local modified output outranks archived implementation only for observed local behavior.
- **additional_insight_to_add:** Provenance loss turns a hierarchy problem into a discovery problem and increases false confidence.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** A hierarchy fails when labels are used to suppress contradictory evidence or when a source is stale, duplicate, or outside the current task.
- **supporting_reason:** Authority does not repair scope mismatch or freshness gaps.
- **counterargument_or_limit:** A stale canonical source may still establish historical intent useful for diagnosis.
- **assumptions_and_boundaries:** Historical evidence must be labeled and cannot automatically govern current behavior.
- **revision_decision:** Include legacy, duplicate, conflicting, and task-irrelevant states with handling guidance.
- **additional_insight_to_add:** Conflict is information about system evolution, not merely noise to remove.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** Alternatives include flat source lists, strict file precedence, owner declarations, or claim-level evidence graphs.
- **supporting_reason:** Flat lists are simple, while claim graphs better handle mixed-role and conflicting artifacts.
- **counterargument_or_limit:** Full evidence graphs may be excessive for one page.
- **assumptions_and_boundaries:** A compact table plus claim sampling provides sufficient rigor here.
- **revision_decision:** Use a role table and conflict protocol without creating a new graph artifact.
- **additional_insight_to_add:** The hierarchy should become more granular only when actual disputes demand it.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Common mistakes are treating archived code as installed behavior, treating existing output as intended policy, and letting method sources establish subject facts.
- **supporting_reason:** Each mistake crosses an evidence boundary and can lead to wrong implementation or narrative claims.
- **counterargument_or_limit:** Existing output can establish local tone and observed behavior when explicitly requested.
- **assumptions_and_boundaries:** Its authority remains limited to those observations and does not validate embedded technical claims.
- **revision_decision:** Add "can establish" and "cannot establish" columns.
- **additional_insight_to_add:** Negative authority boundaries are often more useful than rank labels because they prevent category errors.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** Good hierarchy assigns a claim to its closest source; bad hierarchy says local always wins; borderline hierarchy identifies roles but ignores conflict.
- **supporting_reason:** These examples make precedence conditional and evidence-sensitive.
- **counterargument_or_limit:** Owner decisions may legitimately override a local default for a new task.
- **assumptions_and_boundaries:** Overrides are decisions with rationale, not retroactive claims about what sources said.
- **revision_decision:** Add owner-override handling distinct from source interpretation.
- **additional_insight_to_add:** Separating authority to decide from evidence about current behavior prevents governance from rewriting history.
### Question 08: How can the important claims be verified?
- **current_section_observation:** Hierarchy verification samples claims, checks source role and version, resolves links, and records contradictions without collapsing them.
- **supporting_reason:** Sampling tests whether labels change actual synthesis behavior.
- **counterargument_or_limit:** A small sample may miss isolated misattribution.
- **assumptions_and_boundaries:** Sample all high-consequence claims and representative lower-risk claims.
- **revision_decision:** Add a bidirectional review: claim to authority and source to represented decision.
- **additional_insight_to_add:** Bidirectional review catches both unsupported claims and important source constraints omitted from the page.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** Source linkage and contents are observed, while hierarchy terminology and precedence protocol are synthesized for this reference.
- **supporting_reason:** The local package implies roles but does not publish a formal conflict-resolution standard.
- **counterargument_or_limit:** The implied package structure strongly supports treating the skill as the entry authority.
- **assumptions_and_boundaries:** Use the protocol operationally while remaining open to owner clarification.
- **revision_decision:** Label role assignments as local interpretation backed by artifact purpose.
- **additional_insight_to_add:** Explicitly provisional hierarchy is safer than an unstated hierarchy that still influences every decision.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** Claim-scoped hierarchy reveals two independent ownership questions: who defines the explainer method and who defines subject truth.
- **supporting_reason:** A method maintainer should not adjudicate undocumented system behavior, and a system owner need not control presentation defaults.
- **counterargument_or_limit:** Small teams may combine these roles in one person.
- **assumptions_and_boundaries:** Keep roles conceptually separate even when one owner fills both.
- **revision_decision:** Add escalation routing for method conflict, subject conflict, and artifact behavior conflict.
- **additional_insight_to_add:** Correct escalation shortens review because questions reach the owner capable of supplying the missing kind of evidence.
## Section 013: Theme Specific Artifact
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed calls for a responsive outline but supplies only goal, boundary, and verification fields, which is too thin to govern an actual explainer build.
- **supporting_reason:** A reviewable artifact should connect audience outcome, source model, narrative acts, component choices, alternate states, and proof before implementation expands.
- **counterargument_or_limit:** An overly detailed brief can duplicate the final page and discourage iteration.
- **assumptions_and_boundaries:** The artifact records decisions and evidence pointers, not polished prose or complete CSS.
- **revision_decision:** Define a compact source-grounded explainer brief and storyboard with mandatory and conditional fields.
- **additional_insight_to_add:** The brief is the cheapest place to detect a wrong story because layout investment has not yet made it emotionally expensive to change.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** The default brief should begin with one reader, one question or prediction, one thesis, and one bounded causal path.
- **supporting_reason:** These constraints prevent a page from becoming an undifferentiated tour of everything in the source set.
- **counterargument_or_limit:** A page may legitimately serve two closely related roles or compare several paths.
- **assumptions_and_boundaries:** Multiple audiences require shared prerequisites and explicitly separated outcomes.
- **revision_decision:** Make audience and outcome singular by default, with a documented multi-audience exception.
- **additional_insight_to_add:** A precise outcome makes section deletion easier because content that changes no reader prediction has weaker claim to space.
### Question 03: When does the default work well?
- **current_section_observation:** A storyboard works when sources are sufficient to list actors, state, steps, boundaries, failures, and surprising details.
- **supporting_reason:** Those elements map naturally to the local narrative spine and component palette.
- **counterargument_or_limit:** A conceptual or comparative subject may lack persisted state or failures.
- **assumptions_and_boundaries:** Conditional fields can be marked not applicable with rationale rather than filled artificially.
- **revision_decision:** Distinguish mandatory core fields from subject-dependent modules.
- **additional_insight_to_add:** A justified absence is stronger than a generic section that teaches readers to expect nonexistent behavior.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The artifact fails when authors fill it from the scaffold, use unsupported phrases, or treat approval of the outline as proof of the final page.
- **supporting_reason:** Planning quality cannot replace rendered, interaction, or comprehension evidence.
- **counterargument_or_limit:** A well-reviewed brief still reduces downstream risk significantly.
- **assumptions_and_boundaries:** The brief is an entry gate whose decisions must be reconciled after implementation.
- **revision_decision:** Add evidence pointers to each core field and a post-build reconciliation column.
- **additional_insight_to_add:** Any final component not predicted by the brief should trigger either brief revision or artifact removal.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** Alternatives include a prose outline, wireframe, claim ledger, storyboard, or working scaffold prototype.
- **supporting_reason:** Wireframes expose hierarchy, ledgers expose truth, and prototypes expose runtime behavior, but none alone spans all decisions.
- **counterargument_or_limit:** Combining every artifact can produce redundant documentation.
- **assumptions_and_boundaries:** A single Markdown brief can link lightweight sketches and source pointers without embedding full implementations.
- **revision_decision:** Use a unified table plus optional visual sketch and artifact-specific verification plan.
- **additional_insight_to_add:** Artifact choice should minimize duplicated truth that can drift independently.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Brief-level traps include vague audience labels, thesis-as-topic, acts without questions, visuals without information roles, and targets without failure states.
- **supporting_reason:** These omissions later manifest as generic copy, decorative components, and incomplete testing.
- **counterargument_or_limit:** Early drafts may begin vague while evidence discovery continues.
- **assumptions_and_boundaries:** Unresolved fields remain visibly open and block only dependent implementation decisions.
- **revision_decision:** Add quality tests and dependency links to important fields.
- **additional_insight_to_add:** Partial planning is safe when uncertainty is explicit and downstream work cannot silently assume an answer.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** A good brief ties every act to a question and source; a bad brief lists seven template acts; a borderline brief has a strong story but no alternate reading plan.
- **supporting_reason:** These contrasts demonstrate that narrative and runtime planning are equally necessary.
- **counterargument_or_limit:** A fully static page may need little interaction planning.
- **assumptions_and_boundaries:** It still needs narrow-screen, keyboard reading order, asset failure, and source-footer checks.
- **revision_decision:** Include acceptance prompts that apply even when no custom control exists.
- **additional_insight_to_add:** Static does not mean stateless from the reader's perspective because viewport, input, preference, and dependency conditions still vary.
### Question 08: How can the important claims be verified?
- **current_section_observation:** Brief verification can sample source pointers, test act order, challenge exclusions, inspect component purpose, and execute the planned target matrix after build.
- **supporting_reason:** This validates both planning coherence and eventual reconciliation.
- **counterargument_or_limit:** Reviewers may agree on an outline yet target readers still misunderstand it.
- **assumptions_and_boundaries:** Reader validation is added according to consequence and reuse.
- **revision_decision:** Add pre-build, post-build, and reader-evidence columns to the artifact contract.
- **additional_insight_to_add:** A brief earns durability when it becomes the index to final proof rather than an abandoned planning document.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** Required source inputs and common narrative beats are locally grounded; the exact brief schema is synthesized for operational use.
- **supporting_reason:** The sources describe what to gather and build but do not package those decisions into one review artifact.
- **counterargument_or_limit:** Other teams may prefer issue templates, design documents, or visual boards.
- **assumptions_and_boundaries:** Preserve the information contract even if the storage format changes.
- **revision_decision:** Label the brief as a recommended implementation of local guidance, not a source-mandated file format.
- **additional_insight_to_add:** Schema portability comes from stable questions, not stable column names.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** A complete brief creates traceability from source to reader outcome to act to component to verification evidence.
- **supporting_reason:** That chain supports impact analysis when sources or audience needs change.
- **counterargument_or_limit:** Maintaining full traceability has a cost for ephemeral artifacts.
- **assumptions_and_boundaries:** Scale record depth to lifecycle while retaining at least source, outcome, causal path, targets, and final proof.
- **revision_decision:** Add a minimal durable subset and a fuller maintained-artifact subset.
- **additional_insight_to_add:** Traceability converts refresh from whole-page rereading into targeted revalidation of affected claims and components.
## Section 014: Worked Example Set
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed's good, bad, and borderline sentences identify quality labels but do not show the decisions that produce each outcome.
- **supporting_reason:** Developed examples let authors compare evidence use, scope, story, components, and verification rather than imitate surface prose.
- **counterargument_or_limit:** Examples can accidentally become templates and transfer domain assumptions.
- **assumptions_and_boundaries:** Each case must be explicitly illustrative and identify which details are not reusable facts.
- **revision_decision:** Provide three compact cases with inputs, decisions, artifact shape, finding, and disposition.
- **additional_insight_to_add:** Examples should teach diagnostic moves, not a preferred visual composition.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** The good example should demonstrate a bounded question, sufficient sources, early mechanism, selective components, and layered proof.
- **supporting_reason:** Showing the whole chain reveals why the result is good rather than merely asserting compliance.
- **counterargument_or_limit:** A case that passes every gate can feel unrealistically frictionless.
- **assumptions_and_boundaries:** Include at least one defect found and repaired during verification.
- **revision_decision:** Make the good case evolve through a claim correction or layout repair.
- **additional_insight_to_add:** A repaired finding demonstrates that verification contributes information instead of decorating completion.
### Question 03: When does the default work well?
- **current_section_observation:** Worked comparisons are useful during onboarding, review calibration, and brief critique.
- **supporting_reason:** Teams can discuss concrete evidence and failure signals without debating abstract taste.
- **counterargument_or_limit:** Domain experts may need examples closer to their architecture or audience.
- **assumptions_and_boundaries:** Replace subject details while preserving the reasoning structure.
- **revision_decision:** State transferable lesson after each case.
- **additional_insight_to_add:** A cross-domain example is successful when readers can explain the decision pattern without copying its nouns.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** Examples fail when they imply fixed act counts, universal aesthetics, guaranteed metrics, or production evidence that was never collected.
- **supporting_reason:** Such examples become another source of unsupported authority.
- **counterargument_or_limit:** Concrete detail is necessary for examples to be useful.
- **assumptions_and_boundaries:** Detail remains safe when its illustrative status and replacement boundary are clear.
- **revision_decision:** Avoid numeric outcome claims and identify evidence status at the top.
- **additional_insight_to_add:** Realistic uncertainty often teaches more than invented precision.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** Example formats include before-and-after prose, annotated storyboard, mini case study, or a table comparing decisions.
- **supporting_reason:** A structured case makes evidence and disposition easy to scan, while prose preserves causal sequence.
- **counterargument_or_limit:** A large matrix could overwhelm the section and repeat earlier guidance.
- **assumptions_and_boundaries:** Three short cases with consistent fields balance depth and scanability.
- **revision_decision:** Use bold case labels and compact decision bullets without new Markdown headings.
- **additional_insight_to_add:** Consistent case fields make differences visible without forcing false symmetry in technical content.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Example-specific risks are hidden source gaps, hindsight bias, mislabeled borderline cases, and a bad example so exaggerated it offers no diagnostic value.
- **supporting_reason:** Plausible failure is easier to recognize in real work than a caricature.
- **counterargument_or_limit:** Strong contrasts still help readers remember core guardrails.
- **assumptions_and_boundaries:** Combine an obvious symptom with a subtle root cause.
- **revision_decision:** Make the bad case visually competent but semantically weak, and make the borderline case repairable.
- **additional_insight_to_add:** The most dangerous bad example is one a reviewer might initially approve.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** Good means traceable and testable; bad means polished but source-shaped only by convention; borderline means useful scope with a material unresolved risk.
- **supporting_reason:** These definitions separate quality state from effort or visual sophistication.
- **counterargument_or_limit:** A single critical false claim can make an otherwise strong artifact unacceptable.
- **assumptions_and_boundaries:** Classification follows highest unresolved semantic or access risk.
- **revision_decision:** Give each case a final disposition rather than averaging strengths and weaknesses.
- **additional_insight_to_add:** Borderline is a temporary decision state with a named path to accept, narrow, or reject.
### Question 08: How can the important claims be verified?
- **current_section_observation:** Each case should identify what evidence would confirm its classification and what finding would change it.
- **supporting_reason:** This makes examples falsifiable and useful for review calibration.
- **counterargument_or_limit:** Hypothetical artifacts cannot produce actual screenshots or reader data.
- **assumptions_and_boundaries:** Verification plans are illustrative and outcomes are not claimed as observed.
- **revision_decision:** Include classification evidence and next gate for every case.
- **additional_insight_to_add:** A hypothetical example remains rigorous when it distinguishes proposed proof from collected proof.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The quality criteria derive from local guardrails and this synthesis, while all case facts and outcomes are invented.
- **supporting_reason:** Clear labeling prevents readers from treating examples as repository incidents.
- **counterargument_or_limit:** Synthesized cases still reflect author judgment about severity.
- **assumptions_and_boundaries:** Reviewers should transfer principles and recalibrate severity to local consequences.
- **revision_decision:** Add one evidence-status sentence before the case set.
- **additional_insight_to_add:** Separating status from lesson lets examples remain vivid without claiming historical authority.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The cases reveal that page quality is multi-dimensional but acceptance is constrained by the highest-risk unresolved dimension.
- **supporting_reason:** Strong visuals and navigation cannot offset a false guarantee, while accurate content may remain unshareable if essential caveats are inaccessible.
- **counterargument_or_limit:** Low-impact defects should not block use unnecessarily.
- **assumptions_and_boundaries:** Severity considers semantic impact, access, audience, and artifact status.
- **revision_decision:** Add a disposition rule based on blocking risk rather than average polish.
- **additional_insight_to_add:** This rule prevents compensatory reasoning in which unrelated strengths are used to waive a critical failure.
## Section 015: Outcome Metrics and Feedback Loops
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed names one leading indicator and one failure signal but does not show how to measure quality, interpret evidence, or change the page.
- **supporting_reason:** Metrics should help owners decide whether to accept, repair, narrow, refresh, or replace an explainer.
- **counterargument_or_limit:** Quantifying every aspect of explanation can encourage metric gaming and ignore qualitative insight.
- **assumptions_and_boundaries:** Use a small balanced set tied to actual reader and maintenance decisions.
- **revision_decision:** Define structural, behavioral, comprehension, and lifecycle signals with collection and response rules.
- **additional_insight_to_add:** A metric is operational only when a result changes a named action.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** Default measurement should combine claim traceability, mechanism discoverability, alternate-path coverage, reader prediction, and refresh effort.
- **supporting_reason:** These signals span truth, narrative, access, actual understanding, and maintainability.
- **counterargument_or_limit:** Short-lived internal pages may lack reader samples or a second refresh cycle.
- **assumptions_and_boundaries:** Mark unavailable outcomes not evaluated and retain cheaper structural evidence.
- **revision_decision:** Provide a minimal set and an extended maintained-artifact set.
- **additional_insight_to_add:** Missing outcome data should reduce claim strength, not be filled by proxy metrics silently.
### Question 03: When does the default work well?
- **current_section_observation:** Balanced metrics work when the reader outcome and declared support conditions are known before collection.
- **supporting_reason:** Clear denominators and tasks make results comparable across revisions of the same artifact.
- **counterargument_or_limit:** Comparing different subjects or audiences can still be misleading.
- **assumptions_and_boundaries:** Use trends within a stable context unless normalization is explicitly designed.
- **revision_decision:** Add audience, task, artifact hash, and environment to every measurement record.
- **additional_insight_to_add:** Versioned context turns feedback into diagnostic history instead of anecdote.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** Metrics fail when thresholds are invented, samples are undefined, easy clicks replace comprehension, or feedback is collected without follow-up.
- **supporting_reason:** These practices create precise-looking but non-actionable evidence.
- **counterargument_or_limit:** Simple satisfaction feedback can still reveal confusion worth investigating.
- **assumptions_and_boundaries:** Treat self-report as a signal, not proof of causal understanding.
- **revision_decision:** Require method, denominator, context, uncertainty, and response for each metric.
- **additional_insight_to_add:** The absence of a feedback response is itself an observability failure for a maintained artifact.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** Alternatives include static conformance, expert review, reader interviews, task tests, analytics, support-question counts, and maintenance logs.
- **supporting_reason:** Each varies in cost, privacy, sample bias, and proximity to the intended outcome.
- **counterargument_or_limit:** Analytics can measure behavior at scale but may be inappropriate for local files or privacy-sensitive teams.
- **assumptions_and_boundaries:** Prefer low-data direct tasks before adding instrumentation.
- **revision_decision:** Include collection alternatives and privacy boundaries in the metric table.
- **additional_insight_to_add:** The least invasive evidence often asks a reader to predict one outcome and explain why.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Risks include survivor bias, author-led prompting, ambiguous prediction rubrics, changing source and layout simultaneously, and counting unresolved claims as traced.
- **supporting_reason:** These distort attribution and can hide regressions.
- **counterargument_or_limit:** Perfect experimental control is unrealistic for routine documentation work.
- **assumptions_and_boundaries:** Record confounders and seek directional evidence appropriate to consequence.
- **revision_decision:** Add collection cautions and require separate unknown status.
- **additional_insight_to_add:** A failed reader task can still be highly valuable even when the sample is too small for a rate claim.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** Good metrics specify task and response; bad metrics count page views; borderline metrics measure recall without testing prediction or transfer.
- **supporting_reason:** Examples clarify the distinction between exposure, engagement, and understanding.
- **counterargument_or_limit:** Recall may be an appropriate outcome for terminology or policy pages.
- **assumptions_and_boundaries:** Match the task to the page's declared outcome.
- **revision_decision:** Add interpretation notes preventing cross-purpose comparisons.
- **additional_insight_to_add:** The correct metric for an explainer is the smallest task that demonstrates its promised mental model.
### Question 08: How can the important claims be verified?
- **current_section_observation:** Metric integrity can be checked through formulas, sample records, artifact hashes, repeatable prompts, blinded review where feasible, and linked repair decisions.
- **supporting_reason:** These controls make results auditable without demanding a full research study.
- **counterargument_or_limit:** Small teams may not support blinded review or repeated sampling.
- **assumptions_and_boundaries:** State limitations and avoid generalizing beyond observed readers.
- **revision_decision:** Add a measurement record schema and a closed-loop review cadence.
- **additional_insight_to_add:** Feedback quality rises when the exact misconception is retained alongside the aggregate result.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** Local sources require source grounding and final review, but no measured target values or effectiveness dataset accompany them.
- **supporting_reason:** This reference can define methods and signals, not universal success thresholds.
- **counterargument_or_limit:** Some structural conditions, such as zero unresolved scaffold tokens, can have binary acceptance expectations.
- **assumptions_and_boundaries:** Binary gates apply to defined defects; outcome targets need local calibration.
- **revision_decision:** Separate invariant defect gates from owner-set metric targets.
- **additional_insight_to_add:** Refusing unsupported thresholds improves future comparability because baseline data remains unpolluted by fabricated goals.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** Metrics create their own incentives, so measuring component engagement can encourage unnecessary interaction while measuring prediction encourages causal clarity.
- **supporting_reason:** The measurement system can reshape the artifact in ways unrelated to reader value.
- **counterargument_or_limit:** No metric is entirely incentive-neutral.
- **assumptions_and_boundaries:** Use several complementary signals and review unintended behavior.
- **revision_decision:** Add a metric-gaming check at each review cadence.
- **additional_insight_to_add:** Measure what the page promises the reader, then audit whether optimization is making that promise narrower or less honest.
## Section 016: Completeness Checklist
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed checklist covers role, tradeoffs, hierarchy, artifact, examples, metrics, and routing but omits most conditions needed to accept an actual HTML explainer.
- **supporting_reason:** Completion requires evidence, narrative, content, browser, accessibility, provenance, and handoff checks across the artifact lifecycle.
- **counterargument_or_limit:** A very long checklist can encourage box-ticking and hide the few risks that matter most.
- **assumptions_and_boundaries:** Organize checks by phase and classify blockers by semantic or access impact.
- **revision_decision:** Expand into a phase-based checklist with required evidence, conditional items, and explicit not-applicable rationale.
- **additional_insight_to_add:** Completeness is a coverage claim, not a statement that every optional feature exists.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** The default should check scope and truth before story, story before components, and artifact behavior before handoff.
- **supporting_reason:** This order catches cheap upstream failures before expensive visual and runtime review.
- **counterargument_or_limit:** Iterative design may reveal upstream issues late despite the sequence.
- **assumptions_and_boundaries:** The checklist allows feedback loops but retains ordered acceptance dependencies.
- **revision_decision:** Group items into readiness, narrative, build, alternate paths, and closeout phases.
- **additional_insight_to_add:** A late upstream finding invalidates dependent downstream evidence and should trigger focused reruns.
### Question 03: When does the default work well?
- **current_section_observation:** Phase gates work for maintained pages, shared teams, and agents that need a deterministic resume or review boundary.
- **supporting_reason:** The artifact can stop cleanly at a known incomplete state without hiding what remains.
- **counterargument_or_limit:** Disposable exploratory pages may not need every closeout record.
- **assumptions_and_boundaries:** Truth, ownership, and essential access checks remain even when retention depth is reduced.
- **revision_decision:** Mark a minimum core and extended maintained-artifact items.
- **additional_insight_to_add:** Scaled rigor should remove low-value records, not weaken high-impact truth gates.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** Checklists fail when items are vague, evidence is not linked, exceptions are implicit, or the artifact changes after the check.
- **supporting_reason:** Completion state then becomes unauditable and stale.
- **counterargument_or_limit:** Requiring evidence for every line can create administrative overhead.
- **assumptions_and_boundaries:** High-risk items need proof; low-risk editorial checks can use concise reviewer attestation.
- **revision_decision:** Add evidence expectations to critical items and artifact-hash invalidation to final status.
- **additional_insight_to_add:** A checklist should reveal uncertainty and staleness, not coerce every item into pass.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** Alternatives include one flat list, role-specific lists, automated gates, issue templates, and definition-of-done policies.
- **supporting_reason:** Role-specific and automated checks reduce noise, while one integrated list preserves end-to-end visibility.
- **counterargument_or_limit:** Splitting ownership can create gaps at handoff boundaries.
- **assumptions_and_boundaries:** Keep one artifact-level checklist and assign owners per group.
- **revision_decision:** Use grouped bullets with responsible evidence type rather than separate documents.
- **additional_insight_to_add:** Integrated visibility matters most at transitions where each specialist assumes another closed the gap.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Common omissions are unknown claims, mobile overflow, script-off invisibility, keyboard focus, reduced motion, external asset failure, stale footer paths, and unreconciled brief changes.
- **supporting_reason:** These defects often survive a normal desktop author review.
- **counterargument_or_limit:** Tests should reflect only retained components and declared dependencies.
- **assumptions_and_boundaries:** Remove irrelevant checks when the corresponding risk was architecturally eliminated.
- **revision_decision:** Include conditional triggers beside component-specific items.
- **additional_insight_to_add:** Simpler pages earn shorter checklists by construction, creating a useful incentive for restraint.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** A good checklist item names evidence; a bad item says "page looks polished"; a borderline item passes because a scenario was never declared.
- **supporting_reason:** Clear examples prevent omission from masquerading as success.
- **counterargument_or_limit:** Not every visual quality judgment can be reduced to binary language.
- **assumptions_and_boundaries:** Qualitative checks still record condition, location, consequence, and reviewer.
- **revision_decision:** Use testable verbs and include `not_evaluated` where evidence is absent.
- **additional_insight_to_add:** Explicit non-evaluation turns a silent blind spot into a deliberate risk decision.
### Question 08: How can the important claims be verified?
- **current_section_observation:** Checklist integrity can be verified by mapping each critical item to a source sample, command result, screenshot finding, interaction trace, or reader response.
- **supporting_reason:** Evidence links allow independent spot checks and efficient refresh.
- **counterargument_or_limit:** Screenshots and logs can become bulky and hard to review.
- **assumptions_and_boundaries:** Retain concise evidence that proves the decision and discard raw noise.
- **revision_decision:** Add a completion record schema after the checklist.
- **additional_insight_to_add:** Evidence quality is measured by reproducibility and decision relevance, not file count.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** Several content and finish checks are directly local, while broader accessibility and lifecycle items are synthesized from artifact risks.
- **supporting_reason:** The checklist can still include inferred controls with clear purpose and scope.
- **counterargument_or_limit:** It does not claim formal conformance to an external standard in this no-browse reference.
- **assumptions_and_boundaries:** Formal claims require refreshed normative evidence and appropriate specialist review.
- **revision_decision:** Avoid compliance language and frame checks as minimum artifact risk controls.
- **additional_insight_to_add:** A practical accessibility review can improve access without overstating certification.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** Completeness is compositional: each act may be accurate while the page omits an essential transition or alternate reading path.
- **supporting_reason:** Section-level review must be complemented by whole-journey and cross-condition review.
- **counterargument_or_limit:** Whole-page review is more expensive and prone to fatigue.
- **assumptions_and_boundaries:** Use targeted section checks during construction and a fresh complete pass before acceptance.
- **revision_decision:** Add mandatory full-story and full-artifact reread items after local checks.
- **additional_insight_to_add:** The final reread tests emergent meaning that no isolated component gate can see.
## Section 017: Adjacent Reference Routing
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed routes to vague html, explainer, and page neighbors without naming actual repository candidates or selection criteria.
- **supporting_reason:** Concrete routing prevents this reference from absorbing tasks better served by prose, terminal diagrams, interactive visualizations, image assets, or API documentation.
- **counterargument_or_limit:** Filenames alone do not prove the current content or suitability of an adjacent reference.
- **assumptions_and_boundaries:** Adjacent files are candidates that must be inspected before use.
- **revision_decision:** Route by essential output experience and list exact candidate paths with a verification note.
- **additional_insight_to_add:** Good routing preserves the source model already built so changing medium does not restart factual discovery.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** Keep this reference when a bounded, directly openable narrative page is itself the required experience.
- **supporting_reason:** That is the local pattern's distinctive combination of source grounding, staged story, visual relations, and browser portability.
- **counterargument_or_limit:** A user may need a hybrid with an HTML entry page and deeper companion artifacts.
- **assumptions_and_boundaries:** Route secondary needs without stripping essential explanation from the primary page.
- **revision_decision:** Add retain, pair, and replace decisions rather than one-way redirects.
- **additional_insight_to_add:** Pairing is correct when artifacts serve different reader moments, not when they duplicate the same explanation.
### Question 03: When does the default work well?
- **current_section_observation:** HTML remains the right center when visual sequencing and local browser reading materially improve a causal explanation.
- **supporting_reason:** The page can integrate prose, text-first diagrams, comparisons, and small interactions in one journey.
- **counterargument_or_limit:** If these capabilities are barely used, Markdown may be easier to maintain and review.
- **assumptions_and_boundaries:** Medium value must be demonstrated against the declared outcome.
- **revision_decision:** Include a retention test asking what is lost in the nearest simpler medium.
- **additional_insight_to_add:** A medium should be justified by an essential relation, not by the request's adjective "visual."
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The pattern is wrong when terminal fidelity, exhaustive reference, generated imagery, immersive 3D, or stateful operation dominates the request.
- **supporting_reason:** Those surfaces have different implementation and verification needs.
- **counterargument_or_limit:** HTML can embed many of them, but embedding does not make one reference sufficient.
- **assumptions_and_boundaries:** Route when the adjacent capability is essential rather than incidental.
- **revision_decision:** Add explicit replace conditions and handoff information.
- **additional_insight_to_add:** Capability creep is easier to control when the primary owner of each artifact is named.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** Relevant repository candidates include visual explainer, ASCII diagram, pyramid writing, image generation, Three.js visualization, API documentation, and writing-skill validation references.
- **supporting_reason:** These candidates represent materially different media, depth, and runtime burdens.
- **counterargument_or_limit:** Their exact guidance may evolve independently and was not read for this section.
- **assumptions_and_boundaries:** Route provisionally, then inspect the candidate's current headings, evidence, and gates.
- **revision_decision:** List candidate paths and the question that should trigger inspection, without asserting detailed contents.
- **additional_insight_to_add:** Routing metadata should be maintained as an index, not copied guidance that drifts from the destination.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Routing failures include circular references, vague "consider another page" language, duplicate outputs, and losing unresolved source questions during handoff.
- **supporting_reason:** These failures waste work and weaken accountability at medium boundaries.
- **counterargument_or_limit:** Some overlap is healthy because each artifact needs enough context to stand alone.
- **assumptions_and_boundaries:** Share the evidence model and outcome, but tailor presentation to each medium.
- **revision_decision:** Add a handoff packet with reader, thesis, sources, scope, uncertainty, and required proof.
- **additional_insight_to_add:** A routed task should become more specific, not merely move to a different filename.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** Good routing sends a terminal diagram to ASCII guidance; bad routing adds JavaScript to a lookup table; borderline routing pairs an HTML overview with a full API reference.
- **supporting_reason:** The examples distinguish replacement from useful complement.
- **counterargument_or_limit:** Even a terminal diagram may later be embedded in HTML as a text-legible component.
- **assumptions_and_boundaries:** The source of truth and verification owner remain explicit across reuse.
- **revision_decision:** Include retain, pair, and replace examples around the route table.
- **additional_insight_to_add:** Reuse is safest when the embedded artifact remains valid in its native medium.
### Question 08: How can the important claims be verified?
- **current_section_observation:** Routing can be verified by comparing essential reader task, medium capabilities, maintenance model, and destination acceptance gates.
- **supporting_reason:** This exposes whether routing reduced mismatch or merely displaced it.
- **counterargument_or_limit:** Destination files may be incomplete or stale.
- **assumptions_and_boundaries:** Inspect destination status before committing to the route.
- **revision_decision:** Add a route verification checklist and fallback to general planning when no candidate fits.
- **additional_insight_to_add:** A valid route names both why the current reference stops and why the destination begins.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** Candidate paths exist in the current repository inventory, but their contents and completion status were not assessed in this evolution.
- **supporting_reason:** The reference can provide discoverability without overstating destination authority.
- **counterargument_or_limit:** Path existence may change after this frozen snapshot.
- **assumptions_and_boundaries:** Verify path and current file before use.
- **revision_decision:** Label every row as a candidate and preserve evidence status.
- **additional_insight_to_add:** Discoverability claims should be cheap to refresh through repository inventory checks.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** Adjacent routing reveals that explanation architecture can be separated from output rendering while retaining a shared evidence core.
- **supporting_reason:** This enables multiple media to serve different contexts without independently inventing subject truth.
- **counterargument_or_limit:** Each medium can reorder or omit content, so one shared outline cannot replace medium-specific design.
- **assumptions_and_boundaries:** Share claims and boundaries, then revalidate narrative and access in each output.
- **revision_decision:** Add a reusable handoff core and prohibit treating one artifact's passing evidence as another's.
- **additional_insight_to_add:** Evidence can transfer across media; usability and comprehension evidence generally cannot.
## Section 018: Workload Model
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed imposes a fixed flow and state count without evidence and does not explain when an explainer workload should be narrowed, split, or re-architected.
- **supporting_reason:** Workload modeling should expose pressure from claims, causal branches, sources, components, runtime states, targets, and ownership.
- **counterargument_or_limit:** A qualitative model cannot predict exact authoring time or page length.
- **assumptions_and_boundaries:** Its purpose is scope control and verification planning, not scheduling precision.
- **revision_decision:** Replace arbitrary counts with dimensions, healthy signals, pressure signals, and required response.
- **additional_insight_to_add:** Workload is driven more by independent claims and states than by source file count alone.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** The local default is a bounded one-file journey of roughly five to eight useful acts, with only essential components and interactions.
- **supporting_reason:** This range supports progressive depth while keeping the narrative inspectable and directly openable.
- **counterargument_or_limit:** Act count is guidance, not a capacity guarantee or reason to pad a simple story.
- **assumptions_and_boundaries:** Delete inapplicable acts and split when independent outcomes compete for the same page.
- **revision_decision:** Retain the sourced act range as a pacing signal and reject unsupported state quotas.
- **additional_insight_to_add:** A short page can still be overloaded if each act carries several unrelated causal models.
### Question 03: When does the default work well?
- **current_section_observation:** A single-file workload is healthy when one audience outcome, one coherent causal spine, and a manageable support matrix organize the page.
- **supporting_reason:** Shared context lets acts build on one another without duplicating prerequisites.
- **counterargument_or_limit:** Several variants may still fit when they answer one comparison decision.
- **assumptions_and_boundaries:** Variants belong together only when shared dimensions make the comparison meaningful.
- **revision_decision:** Add cohesion and shared-prerequisite tests.
- **additional_insight_to_add:** Narrative cohesion is a stronger boundary than raw act or source count.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The model fails when multiple audiences, independent systems, live state, large media, or conflicting owners force unrelated proof into one file.
- **supporting_reason:** Coupling those concerns increases refresh blast radius and obscures which artifact state is authoritative.
- **counterargument_or_limit:** A high-level overview can still unify several systems if it stays explicit about abstraction and routes detail outward.
- **assumptions_and_boundaries:** Split detailed journeys while preserving a bounded overview when that serves a real reader decision.
- **revision_decision:** Add split, overview, companion, and application-boundary responses.
- **additional_insight_to_add:** Scope pressure can be relieved by changing abstraction level rather than adding more sections.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** Alternatives include narrowing claims, dividing by audience or lifecycle, adding companion references, creating a series, or moving to an application architecture.
- **supporting_reason:** Each response trades continuity against maintainability and verification isolation.
- **counterargument_or_limit:** Splitting too aggressively forces readers to reconstruct the model across files.
- **assumptions_and_boundaries:** Preserve shared thesis and routing while isolating independent detail.
- **revision_decision:** Tie each pressure signal to the least disruptive response.
- **additional_insight_to_add:** The right split minimizes both duplicated truth and cross-artifact navigation cost.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Workload traps include counting files instead of claims, underestimating alternate states, hiding uncertainty in dense acts, and letting reusable styles justify a built site prematurely.
- **supporting_reason:** These proxies misrepresent actual semantic and verification complexity.
- **counterargument_or_limit:** File and component counts can still signal pressure when interpreted with context.
- **assumptions_and_boundaries:** Use counts as observations, not universal thresholds.
- **revision_decision:** Add qualitative pressure questions and locally calibrated metrics.
- **additional_insight_to_add:** Every retained dependency creates a state transition in the verification workload even if the narrative does not mention it.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** A good workload has one prediction and shared actors; a bad workload combines tutorial, reference, dashboard, and simulator; a borderline workload compares two implementations with diverging state models.
- **supporting_reason:** These cases demonstrate cohesion and verification blast radius.
- **counterargument_or_limit:** A comparison page can handle diverging models when asymmetry is the central point.
- **assumptions_and_boundaries:** The brief must show why joint presentation improves the reader decision.
- **revision_decision:** Add fit and pressure examples below the model.
- **additional_insight_to_add:** Borderline workloads become healthy when the central contrast, rather than each full subsystem, defines scope.
### Question 08: How can the important claims be verified?
- **current_section_observation:** Workload fit can be tested through brief review, claim-to-act mapping, component-purpose inventory, support-matrix enumeration, and refresh impact analysis.
- **supporting_reason:** These checks expose disconnected content and hidden states before they accumulate.
- **counterargument_or_limit:** Future maintenance costs remain uncertain until change occurs.
- **assumptions_and_boundaries:** Record assumptions and revisit after first refresh.
- **revision_decision:** Add a pre-build capacity review and post-refresh calibration step.
- **additional_insight_to_add:** The first real change is the best test of whether workload boundaries matched ownership and source volatility.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** Five-to-eight acts and single-file intent are local guidance; all other capacity thresholds require task evidence.
- **supporting_reason:** The sources do not establish universal limits for sources, states, components, bytes, or viewports.
- **counterargument_or_limit:** Owners may define local thresholds after repeated artifact data.
- **assumptions_and_boundaries:** Such thresholds belong to the project and should record their measurement basis.
- **revision_decision:** Remove seed precision and preserve only sourced or locally calibrated boundaries.
- **additional_insight_to_add:** Qualitative pressure signals are more honest than portable-looking numbers detached from audience and consequence.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** Narrative workload and verification workload can diverge: one simple visual may depend on complex script, assets, and browser behavior.
- **supporting_reason:** Evaluating only visible content underestimates operational burden.
- **counterargument_or_limit:** Complex implementation can be acceptable when it is shared, mature, and well tested.
- **assumptions_and_boundaries:** Reuse evidence and ownership must be real rather than anticipated.
- **revision_decision:** Model semantic and runtime pressure separately and combine them at the split decision.
- **additional_insight_to_add:** A page is outgrowing the standalone pattern when its runtime needs become independent of its explanatory story.
## Section 019: Reliability Target
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed mixes source boundaries, sampled routing accuracy, unsupported claims, and recovery clarity without defining reliability for an explainer.
- **supporting_reason:** Authors need to decide which failures block acceptance, which require calibrated targets, and which remain advisory observations.
- **counterargument_or_limit:** Documentation reliability cannot be reduced to service-style availability numbers.
- **assumptions_and_boundaries:** Reliability here means preserving truthful, reachable, reproducible, and refreshable explanation under declared conditions.
- **revision_decision:** Define dimensions, invariants, owner-set targets, evidence, and failure responses.
- **additional_insight_to_add:** Explainer reliability concerns the continuity of meaning, not merely whether bytes are served.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** Critical defaults are no unsupported high-consequence claim, essential content reachable on every declared path, and reproducible provenance for the artifact.
- **supporting_reason:** Violating any of these can materially mislead or exclude the intended reader.
- **counterargument_or_limit:** Lower-risk uncertainty and cosmetic defects need not block every internal draft.
- **assumptions_and_boundaries:** Status and audience determine severity, while uncertainty remains visible.
- **revision_decision:** Separate invariant blockers from calibrated quality objectives.
- **additional_insight_to_add:** Reliability policies should protect the reader from false certainty before protecting the page from minor visual inconsistency.
### Question 03: When does the default work well?
- **current_section_observation:** Dimension-based targets work when support conditions, reader outcome, source set, and artifact status are declared.
- **supporting_reason:** Evidence can then be tied to a bounded promise rather than an imagined universal environment.
- **counterargument_or_limit:** Public artifacts may require broader normative and browser evidence than this local reference supplies.
- **assumptions_and_boundaries:** Owners must extend the matrix using current primary standards and local requirements.
- **revision_decision:** Add a declared-support prerequisite to every target.
- **additional_insight_to_add:** A narrow reliable promise is stronger than a broad untested one.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** Reliability tables fail when they use inherited percentages without measurement, treat unknown as pass, or ignore semantic severity.
- **supporting_reason:** Precision without basis encourages compliance theater and poor prioritization.
- **counterargument_or_limit:** Calibrated rates can support trend tracking after sufficient repeated data.
- **assumptions_and_boundaries:** Any numeric target needs owner, baseline, sample definition, and decision consequence.
- **revision_decision:** Remove the seed's ungrounded sample threshold and specify calibration requirements.
- **additional_insight_to_add:** A metric becomes a target only when missed performance triggers an agreed response.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** Targets may be binary invariants, sampled objectives, qualitative review standards, or risk budgets.
- **supporting_reason:** Binary gates suit critical defects, while sampled objectives suit reader outcomes and ongoing improvement.
- **counterargument_or_limit:** Binary rules can be brittle when claim consequence or audience changes.
- **assumptions_and_boundaries:** Scope each invariant to high-consequence content and declared essential paths.
- **revision_decision:** Match target form to failure class and evidence quality.
- **additional_insight_to_add:** Using one target form for every dimension obscures both uncertainty and severity.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Reliability blind spots include script-visible content, stale source footers, untested asset failure, unresolved claim conflicts, and reader predictions collected on old hashes.
- **supporting_reason:** These conditions make apparent evidence irrelevant to the current artifact or support promise.
- **counterargument_or_limit:** Not every byte change affects every gate.
- **assumptions_and_boundaries:** Impact analysis can limit reruns when dependencies are explicit.
- **revision_decision:** Add evidence validity and change-impact rules to each target.
- **additional_insight_to_add:** Provenance is a reliability mechanism because it determines whether prior proof still applies.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** Good targets name condition and response; bad targets claim 99 percent clarity; borderline targets demand zero console errors without classifying harmless messages.
- **supporting_reason:** Concrete examples distinguish actionable reliability from impressive language.
- **counterargument_or_limit:** A strict console policy may be appropriate in a controlled artifact.
- **assumptions_and_boundaries:** Define severity and accepted environment before enforcing it.
- **revision_decision:** Add pass evidence and failure action columns rather than unsupported rates.
- **additional_insight_to_add:** Reliability evidence should make triage easier, not simply increase the number of red indicators.
### Question 08: How can the important claims be verified?
- **current_section_observation:** Verify truth through source sampling, reachability through alternate paths, reproducibility through fresh open or generation, and refreshability through impact records.
- **supporting_reason:** Each method directly exercises the dimension it claims to support.
- **counterargument_or_limit:** Reader comprehension remains probabilistic and audience-dependent.
- **assumptions_and_boundaries:** Use task evidence and confidence limits rather than declaring certainty.
- **revision_decision:** Define a reliability evidence packet with artifact hash and scope.
- **additional_insight_to_add:** Independent evidence dimensions prevent one successful render from masking a semantic or provenance failure.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** Source guardrails justify strict truth and provenance expectations, while routing rates and latency targets lack local measurement.
- **supporting_reason:** The evolved table can state critical invariants without preserving unsupported seed precision.
- **counterargument_or_limit:** Severity classification and essential-path designation remain owner judgments.
- **assumptions_and_boundaries:** Record those decisions before testing.
- **revision_decision:** Label target provenance and calibration status per row.
- **additional_insight_to_add:** Reliability governance is transparent when reviewers can challenge both the result and the boundary being protected.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** Truth, access, and provenance interact: a correct claim hidden on one path or tied to stale evidence is not reliably communicated.
- **supporting_reason:** Reliability emerges from the weakest required dimension rather than an average score.
- **counterargument_or_limit:** Low-severity deficits should not dominate unrelated critical strengths.
- **assumptions_and_boundaries:** Apply the weakest-link rule only across declared essential dimensions.
- **revision_decision:** Add a no-compensation rule for critical blockers and separate advisory findings.
- **additional_insight_to_add:** Reliability review should prevent compensating a semantic blocker with excellent performance or visual quality.
## Section 020: Failure Mode Table
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed lists four broad failures but does not help an owner classify severity, contain reader harm, assign repair, or prove recovery.
- **supporting_reason:** An operational table should convert a symptom into the next safe action and durable prevention.
- **counterargument_or_limit:** Failure catalogs can overlap with anti-patterns and checklists.
- **assumptions_and_boundaries:** This section emphasizes detected runtime or lifecycle states, impact, ownership, and recovery evidence.
- **revision_decision:** Expand rows across evidence, narrative, rendering, interaction, dependency, comprehension, and maintenance failures.
- **additional_insight_to_add:** The same visible symptom can originate in different layers, so classification must precede repair.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** The default response is contain misleading or inaccessible output, identify the earliest responsible layer, repair there, and rerun dependent evidence.
- **supporting_reason:** This minimizes repeated surface patches and reduces continued reader exposure.
- **counterargument_or_limit:** Immediate containment may be unnecessary for an unshared draft.
- **assumptions_and_boundaries:** Severity and distribution status determine urgency, while root-cause discipline remains.
- **revision_decision:** Add containment and durable repair as separate columns.
- **additional_insight_to_add:** A temporary warning can reduce harm but is not a substitute for fixing a high-consequence false claim.
### Question 03: When does the default work well?
- **current_section_observation:** Layered failure handling works when artifact ownership, source ownership, and support conditions are documented.
- **supporting_reason:** Findings can reach the person able to supply evidence or modify the correct component.
- **counterargument_or_limit:** Ownership may be fragmented or unavailable in archived contexts.
- **assumptions_and_boundaries:** Unowned critical failures narrow or block the artifact until responsibility is assigned.
- **revision_decision:** Add escalation and no-owner handling.
- **additional_insight_to_add:** Ownership uncertainty is itself a reliability risk for durable explanatory claims.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** A table fails when every symptom gets the same retry, when low-impact defects block all use, or when semantic errors are delegated to CSS repair.
- **supporting_reason:** Poor classification wastes effort and can preserve reader harm.
- **counterargument_or_limit:** A simple internal workflow may use fewer severity labels.
- **assumptions_and_boundaries:** At minimum distinguish critical semantic or access blockers from recoverable quality findings.
- **revision_decision:** Include severity basis without inventing universal incident levels.
- **additional_insight_to_add:** Severity follows consequence for the declared reader, not the technical layer where the bug appears.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** Responses include warning, rollback, feature removal, scope narrowing, source refresh, layout repair, rerouting, and full replacement.
- **supporting_reason:** The least disruptive safe response depends on whether truth, access, or maintainability is affected.
- **counterargument_or_limit:** A narrow repair can leave systemic causes untouched.
- **assumptions_and_boundaries:** Repeated symptoms trigger upstream workflow changes.
- **revision_decision:** Pair immediate containment with prevention and recurrence signals.
- **additional_insight_to_add:** Recovery is complete only when prior invalid evidence is replaced or explicitly retired.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** High-risk modes include false guarantees, stale causal models, hidden essential content, keyboard traps, narrow overflow, missing assets, broken local opening, and source-owner conflict.
- **supporting_reason:** They can mislead, exclude, or make the artifact unreproducible.
- **counterargument_or_limit:** Cosmetic drift and optional enhancement loss may have low impact.
- **assumptions_and_boundaries:** Classify based on essential meaning and declared support.
- **revision_decision:** Order rows by reader impact and add conditional severity notes.
- **additional_insight_to_add:** Several low-impact failures can combine into an essential-path outage and should be reviewed together.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** Good handling disables an unsupported guarantee; bad handling adds a caveat below it; borderline handling removes animation but leaves orientation unclear.
- **supporting_reason:** These examples show containment quality and residual risk.
- **counterargument_or_limit:** A prominent caveat can be adequate for genuinely uncertain, noncritical content.
- **assumptions_and_boundaries:** The main claim must not visually contradict the caveat.
- **revision_decision:** Add residual-risk checks to repair proof.
- **additional_insight_to_add:** A repair that changes wording but not perceived emphasis may leave the same mental-model failure intact.
### Question 08: How can the important claims be verified?
- **current_section_observation:** Recovery proof reruns reproduction, source comparison, target condition, and reader task affected by the failure.
- **supporting_reason:** A generic full-page screenshot may miss the specific causal or access regression.
- **counterargument_or_limit:** Some failures have broad impact and require a complete reread.
- **assumptions_and_boundaries:** Use focused regression first and whole-artifact reconciliation when dependencies are uncertain.
- **revision_decision:** Add proof and invalidated-evidence fields per row.
- **additional_insight_to_add:** The repair plan should name which earlier pass results are no longer trustworthy.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** Local sources directly warn against several content failures, while severity, containment, and owner routing are synthesized operations guidance.
- **supporting_reason:** The operational additions follow observable artifact risks but are not measured incident data.
- **counterargument_or_limit:** Projects may use established incident taxonomies that should take precedence.
- **assumptions_and_boundaries:** Map these modes into local process without changing their semantic distinctions.
- **revision_decision:** Avoid fixed severity numbers and state the consequence basis.
- **additional_insight_to_add:** A portable failure table describes reader harm and proof, leaving labels to the owning organization.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** Explanatory failures can persist socially after the page is fixed because readers retain the earlier mental model or screenshots circulate.
- **supporting_reason:** Artifact repair alone may not correct already distributed misinformation.
- **counterargument_or_limit:** Broad correction campaigns may be disproportionate for a tiny internal audience.
- **assumptions_and_boundaries:** Response scope follows distribution and decision impact.
- **revision_decision:** Add downstream correction and evidence retirement to high-impact recovery.
- **additional_insight_to_add:** Reliability ownership includes correcting the explanation's propagation, not only updating its source file.
## Section 021: Retry Backpressure Guidance
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed recommends bounded retries and checkpoints but does not decide which explainer failures are retryable or when downstream work must stop.
- **supporting_reason:** Retry without classification can repeat destructive generation, stale research, flaky screenshots, or unsupported reasoning without adding information.
- **counterargument_or_limit:** Some failures contain both transient and semantic components.
- **assumptions_and_boundaries:** Decompose the failure and retry only the transient operation after preserving state.
- **revision_decision:** Add a classification matrix, retry preconditions, backpressure boundaries, and escalation evidence.
- **additional_insight_to_add:** A retry is justified only when repetition can plausibly change the result without changing the question.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** The default is classify, preserve, diagnose, bound, retry the smallest idempotent step, then compare evidence.
- **supporting_reason:** This prevents context drift and limits blast radius in shared or long-running work.
- **counterargument_or_limit:** Immediate retry can be efficient for an obvious one-off tool interruption.
- **assumptions_and_boundaries:** Even fast retries must not overwrite valued output or hide repeated instability.
- **revision_decision:** State an explicit retry sequence and require a stop after unchanged failure evidence.
- **additional_insight_to_add:** Comparing pre- and post-retry evidence distinguishes recovery from mere repetition.
### Question 03: When does the default work well?
- **current_section_observation:** Bounded retries fit temporary file locks, interrupted browser capture, transient local server startup, or a known unavailable optional resource.
- **supporting_reason:** The underlying artifact and expected result remain stable while the environment may recover.
- **counterargument_or_limit:** A consistent failure often indicates deterministic code or configuration, not transience.
- **assumptions_and_boundaries:** Retry count is set by local cost and evidence rather than a universal number.
- **revision_decision:** Add evidence of transience and idempotency as eligibility gates.
- **additional_insight_to_add:** Cheap retries can still create expensive confusion when their outputs are not labeled by attempt and artifact hash.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** Retry is wrong for missing sources, contradictory claims, unclear ownership, false audience assumptions, or reader misconceptions.
- **supporting_reason:** Repeating the same operation cannot supply the absent decision or repair the model.
- **counterargument_or_limit:** A refreshed source retrieval may resolve stale evidence when browsing is authorized.
- **assumptions_and_boundaries:** That is a changed input and new evidence cycle, not blind retry.
- **revision_decision:** Mark semantic and governance failures non-retryable until their inputs change.
- **additional_insight_to_add:** Calling changed-input work a retry hides the decision that actually enabled progress.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** Alternatives are retry, fallback, degrade, narrow scope, rollback, reroute, escalate, or stop.
- **supporting_reason:** The safest response depends on whether essential meaning, optional enhancement, evidence, or ownership failed.
- **counterargument_or_limit:** Fallback paths add implementation and test burden.
- **assumptions_and_boundaries:** Prefer architectural fallback only for a declared condition worth supporting.
- **revision_decision:** Map failure classes to response options and proof.
- **additional_insight_to_add:** Removing a nonessential failing feature can be a better recovery than making its retry logic more elaborate.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Retry hazards include overwriting output, duplicating source claims, accepting a later flaky screenshot, compounding context, and allowing red upstream gates to coexist with downstream polish.
- **supporting_reason:** These behaviors can erase durable work or create inconsistent evidence.
- **counterargument_or_limit:** Parallel work can continue on independent sections when dependencies are explicit.
- **assumptions_and_boundaries:** Backpressure stops only dependent work, not the entire workspace automatically.
- **revision_decision:** Add dependency-scoped stop rules and atomic save requirements.
- **additional_insight_to_add:** Precise backpressure preserves throughput by distinguishing blocked dependencies from independent safe work.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** Good retry reruns a failed capture after browser recovery; bad retry regenerates over a page; borderline retry repeats a reader task without changing ambiguous wording.
- **supporting_reason:** These examples show idempotency, state preservation, and information gain.
- **counterargument_or_limit:** Repeating a reader task can measure stability when the prompt and artifact are already clear.
- **assumptions_and_boundaries:** That is intentional replication with a measurement plan, not defect recovery.
- **revision_decision:** Include concrete response examples in the matrix.
- **additional_insight_to_add:** The same repeated action can be a retry, experiment, or regression test depending on its stated hypothesis.
### Question 08: How can the important claims be verified?
- **current_section_observation:** Retry quality is verified by attempt log, preserved artifact hash, classified cause, changed environmental evidence, bounded count, and final disposition.
- **supporting_reason:** This shows whether repetition was safe and informative.
- **counterargument_or_limit:** Extensive attempt logs can become noise.
- **assumptions_and_boundaries:** Retain concise summaries and decisive output rather than raw transcript volume.
- **revision_decision:** Add a minimal retry record schema.
- **additional_insight_to_add:** A useful retry record explains why another attempt should differ before it is run.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** Checkpointing and bounded retry are in the seed, while detailed classification and idempotency rules are synthesized systems guidance.
- **supporting_reason:** The additions operationalize safe repetition without claiming measured optimal retry counts.
- **counterargument_or_limit:** Existing repository tooling may have its own retry and backoff policies.
- **assumptions_and_boundaries:** Use those policies when present and record how they apply to artifact work.
- **revision_decision:** Avoid fixed delays or counts and state decision criteria instead.
- **additional_insight_to_add:** Tool-level backoff and workflow-level backpressure solve different problems and should not be conflated.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** Backpressure also protects narrative coherence because downstream polish can make an unresolved upstream claim harder to remove.
- **supporting_reason:** Investment and visual integration create resistance to correcting the evidence model.
- **counterargument_or_limit:** Prototyping downstream can expose an upstream flaw productively.
- **assumptions_and_boundaries:** Prototype work remains disposable and visibly provisional until upstream gates pass.
- **revision_decision:** Permit isolated experiments while blocking acceptance and dependent durable work.
- **additional_insight_to_add:** Backpressure manages cognitive commitment as well as technical resource use.
## Section 022: Observability Checklist
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed checklist mixes source logs, browser facts, latency percentiles, and journal notes without defining which evidence is needed for which decision.
- **supporting_reason:** Observability should let owners reproduce a finding, assess coverage, locate responsibility, and detect drift without storing an indiscriminate transcript.
- **counterargument_or_limit:** More telemetry can create privacy, maintenance, and review burden.
- **assumptions_and_boundaries:** Collect the minimum decision-bearing evidence for the artifact's audience, lifetime, and failure cost.
- **revision_decision:** Group observability by provenance, artifact identity, browser conditions, reader outcomes, change history, and ownership.
- **additional_insight_to_add:** Observability quality is the ability to answer a future question, not the volume of retained data.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** Default records should include source set, claim status, artifact hash, exact conditions, concise gate outcomes, findings, residual risk, and owner.
- **supporting_reason:** These fields support independent reproduction and targeted refresh with low overhead.
- **counterargument_or_limit:** Artifact hashes and environment details may be unnecessary for an ephemeral private sketch.
- **assumptions_and_boundaries:** At minimum retain source provenance and unresolved claims whenever the page can influence another person's understanding.
- **revision_decision:** Define minimal and maintained-artifact evidence sets.
- **additional_insight_to_add:** Retention depth scales with reuse, but truth provenance scales with consequence from the first share.
### Question 03: When does the default work well?
- **current_section_observation:** Compact evidence packets work when test targets and expected outcomes are declared before collection.
- **supporting_reason:** Reviewers know which conditions are covered and can distinguish absence from failure.
- **counterargument_or_limit:** Unexpected behavior may require exploratory logging beyond the initial plan.
- **assumptions_and_boundaries:** Temporary diagnostic detail can be collected and then distilled into durable findings.
- **revision_decision:** Separate transient diagnostic data from retained decision evidence.
- **additional_insight_to_add:** Distillation preserves signal while reducing privacy and context cost.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** Observability fails when screenshots lack viewport, logs lack artifact version, metrics lack denominator, or reader analytics are collected without need or consent.
- **supporting_reason:** Such data is irreproducible, misleading, or ethically costly.
- **counterargument_or_limit:** Informal evidence can still aid a quick local diagnosis.
- **assumptions_and_boundaries:** Informal findings must not become formal completion proof without context.
- **revision_decision:** Add minimum metadata and privacy review requirements.
- **additional_insight_to_add:** Uncontextualized evidence can be worse than no evidence because it invites false comparison.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** Evidence may live in a journal, issue, test output, screenshot bundle, artifact footer, analytics system, or source ledger.
- **supporting_reason:** Different storage fits different lifetimes and collaboration models.
- **counterargument_or_limit:** Dispersed evidence can become impossible to reconstruct.
- **assumptions_and_boundaries:** Keep one index pointing to authoritative artifacts and avoid duplicating mutable facts.
- **revision_decision:** Require a compact evidence index even when supporting files live elsewhere.
- **additional_insight_to_add:** An index is most useful when every entry names the decision it supports and its staleness trigger.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Major traps are raw transcript retention, sensitive source leakage, screenshot overcollection, silent skipped scenarios, and latency numbers from uncontrolled runs.
- **supporting_reason:** These practices increase cost or false confidence without improving diagnosis.
- **counterargument_or_limit:** Detailed traces may be necessary during a difficult runtime investigation.
- **assumptions_and_boundaries:** Sanitize and expire diagnostic traces after extracting the durable conclusion.
- **revision_decision:** Add data minimization, sensitivity, and expiration checks.
- **additional_insight_to_add:** Explanatory artifacts can leak system details through provenance even when the visible narrative is sanitized.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** Good evidence says what failed where and on which hash; bad evidence says mobile looked wrong; borderline evidence supplies a screenshot but no semantic impact.
- **supporting_reason:** Examples show what makes a finding actionable rather than merely visual.
- **counterargument_or_limit:** Semantic impact may be uncertain at first observation.
- **assumptions_and_boundaries:** Record uncertainty and assign follow-up rather than guessing.
- **revision_decision:** Include a concise finding schema and status vocabulary.
- **additional_insight_to_add:** A finding can be valid before root cause is known if reproduction and consequence are explicit.
### Question 08: How can the important claims be verified?
- **current_section_observation:** Observability itself can be audited by reproducing sampled findings, checking evidence-to-hash links, and locating all not-evaluated conditions.
- **supporting_reason:** This tests whether retained records support independent decisions.
- **counterargument_or_limit:** Reproduction cost may be high for old environments.
- **assumptions_and_boundaries:** Preserve enough environment description to decide whether reconstruction is warranted.
- **revision_decision:** Add an evidence audit at final handoff and refresh.
- **additional_insight_to_add:** The ability to declare evidence irreproducible honestly is better than silently treating it as current.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** Local sources require source listing and verification, while the detailed observability schema is synthesized from maintenance needs.
- **supporting_reason:** The schema operationalizes reproducibility without claiming universal telemetry practice.
- **counterargument_or_limit:** Existing organizational observability systems may provide stronger conventions.
- **assumptions_and_boundaries:** Integrate with local systems while preserving required evidence semantics.
- **revision_decision:** Make storage implementation flexible and information contract explicit.
- **additional_insight_to_add:** Tool-neutral evidence fields remain durable when browsers, runners, and issue systems change.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** Observability influences author behavior: measuring every interaction can encourage unnecessary controls and surveillance.
- **supporting_reason:** Collection choices create product and privacy incentives beyond diagnosis.
- **counterargument_or_limit:** Aggregate usage can help prioritize improvements for widely deployed public pages.
- **assumptions_and_boundaries:** Add analytics only with a decision need, lawful basis, minimization, and retention policy.
- **revision_decision:** Prefer direct low-data reader tasks and artifact evidence by default.
- **additional_insight_to_add:** The most respectful explainer often observes its own build and review process more than its readers.
## Section 023: Performance Verification Method
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed mandates p95 under 100 milliseconds without defining an interaction, environment, workload, sampling method, or evidence basis.
- **supporting_reason:** Performance guidance should decide what is worth measuring, how to measure it reproducibly, and which result affects artifact acceptance.
- **counterargument_or_limit:** A mostly static local page may have no meaningful runtime performance objective beyond usable loading and stable reading.
- **assumptions_and_boundaries:** Measure only behavior material to the declared reader experience.
- **revision_decision:** Replace the universal threshold with a claim-driven method spanning load, interaction, stability, dependency, and authoring workflow where applicable.
- **additional_insight_to_add:** Avoiding meaningless performance metrics is itself a quality improvement because it keeps attention on observable reader costs.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** Default verification starts with direct opening, essential-content availability, dependency inspection, layout stability, and responsive fit before timing optional interactions.
- **supporting_reason:** Correct and reachable content is prerequisite to interpreting speed.
- **counterargument_or_limit:** Severe performance problems can themselves prevent content access.
- **assumptions_and_boundaries:** Classify availability and stability failures alongside timing, without allowing fast failure to pass.
- **revision_decision:** Sequence correctness, dependency, and timing checks explicitly.
- **additional_insight_to_add:** A fast blank reveal state has excellent latency and zero explanatory value.
### Question 03: When does the default work well?
- **current_section_observation:** Claim-driven measurement works when the page retains controls, heavy assets, long scripts, or an HTTP deployment whose responsiveness affects use.
- **supporting_reason:** Defined interactions and conditions create reproducible boundaries for observation.
- **counterargument_or_limit:** Direct file loads and cached local resources may not represent deployed network behavior.
- **assumptions_and_boundaries:** Test each claimed delivery surface separately.
- **revision_decision:** Add cold and warm condition selection based on the actual promise.
- **additional_insight_to_add:** Environment mismatch is often a larger source of error than sample size for small artifact tests.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** Percentile measurement fails with tiny uncontrolled samples, mixed interactions, changing artifacts, or absent user consequence.
- **supporting_reason:** The resulting number looks rigorous but cannot guide a decision.
- **counterargument_or_limit:** Small repeated samples can still diagnose regressions when conditions are controlled.
- **assumptions_and_boundaries:** Report observations and uncertainty without pretending to population percentiles.
- **revision_decision:** Require sufficient sample rationale before percentile language and permit qualitative or per-run evidence otherwise.
- **additional_insight_to_add:** Precision should follow measurement design, not be added through decimal places or percentile labels.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** Methods include browser traces, manual observation, static dependency review, file-size checks, visual stability inspection, synthetic interaction timing, and reader task timing.
- **supporting_reason:** Each addresses a different cost and has different tooling and interpretive limits.
- **counterargument_or_limit:** Reader task time combines page quality with reader background and should not be labeled runtime latency.
- **assumptions_and_boundaries:** Keep technical timing, workflow timing, and comprehension timing separate.
- **revision_decision:** Add metric families and prohibit cross-family substitution.
- **additional_insight_to_add:** A slower deliberate reading path can improve understanding, so speed is not always the desired direction.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Measurement traps include font-cache variance, animation masking, first-run versus warm-run mixing, devtools overhead, external request variability, and screenshot timing before reveals settle.
- **supporting_reason:** These factors can dominate a small page's observed timing and visual state.
- **counterargument_or_limit:** Perfect isolation may be unnecessary when testing the exact end-user environment.
- **assumptions_and_boundaries:** Record conditions and select realism or control deliberately.
- **revision_decision:** Add confounder and artifact-hash fields to the method.
- **additional_insight_to_add:** The chosen measurement environment is part of the claim, not a footnote.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** Good measurement times a named control under fixed conditions; bad measurement says the page feels fast; borderline measurement reports p95 from a handful of mixed clicks.
- **supporting_reason:** These examples separate reproducible observation from impression and pseudo-statistics.
- **counterargument_or_limit:** Perceived responsiveness remains relevant and can be captured qualitatively.
- **assumptions_and_boundaries:** Pair perception with a defined scenario and technical evidence where consequence warrants it.
- **revision_decision:** Include valid and invalid claim examples after the procedure.
- **additional_insight_to_add:** Qualitative performance evidence becomes actionable when it names the blocking moment and reader consequence.
### Question 08: How can the important claims be verified?
- **current_section_observation:** Verification needs claim, boundary, workload, environment, dependency state, run protocol, sample, statistic, acceptance rule, and artifact hash.
- **supporting_reason:** These fields let another reviewer repeat and challenge the conclusion.
- **counterargument_or_limit:** Not every artifact needs a statistical summary.
- **assumptions_and_boundaries:** Use the simplest reporting form justified by the question.
- **revision_decision:** Provide a stepwise method and evidence packet.
- **additional_insight_to_add:** A performance claim without a predeclared acceptance consequence is descriptive, not a gate.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The seed's latency threshold is unsupported, while no-overlap review aligns with artifact verification but is layout correctness rather than performance.
- **supporting_reason:** Reclassification improves conceptual accuracy and prevents one gate from hiding another.
- **counterargument_or_limit:** Layout shifts over time can be a performance-related visual stability concern.
- **assumptions_and_boundaries:** Distinguish static fit from temporal instability and measure each appropriately.
- **revision_decision:** Move overlap to correctness and retain stability as a timed concern when observed.
- **additional_insight_to_add:** Clear metric taxonomy makes failures easier to assign to content, layout, dependency, or runtime owners.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** Performance burden grows from design choices such as external fonts, image media, hidden reveal states, and custom controls.
- **supporting_reason:** Removing unnecessary dependencies can eliminate both latency and entire verification scenarios.
- **counterargument_or_limit:** A meaningful asset or interaction may justify its cost.
- **assumptions_and_boundaries:** Retained cost must connect to a named explanatory benefit.
- **revision_decision:** Add design elimination as the first optimization step.
- **additional_insight_to_add:** The most reliable optimization often removes work from the browser and the test matrix simultaneously.
## Section 024: Scale Boundary Statement
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed says the pattern stops at multiple systems or ownership boundaries but does not distinguish a high-level multi-system explanation from an overloaded implementation.
- **supporting_reason:** Authors need to decide whether to narrow, split, create a series, share infrastructure, or move to an application architecture.
- **counterargument_or_limit:** Scale boundaries are contextual and should not be triggered by file or system count alone.
- **assumptions_and_boundaries:** Cohesion, reader outcome, runtime need, ownership, and verification capacity govern the decision.
- **revision_decision:** Define scale dimensions, transition signals, and safe migration responses.
- **additional_insight_to_add:** Scale is reached when coordination becomes independent work, not merely when content becomes long.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** Keep one standalone page while one owner, one audience outcome, one causal spine, and one manageable support promise remain coherent.
- **supporting_reason:** These conditions preserve direct portability and focused review.
- **counterargument_or_limit:** Multiple owners can collaborate successfully with exclusive section or source responsibilities.
- **assumptions_and_boundaries:** One artifact owner still reconciles final narrative and behavior.
- **revision_decision:** State one final ownership and coherence contract rather than banning collaboration.
- **additional_insight_to_add:** Shared contribution scales safely only when synthesis responsibility stays singular.
### Question 03: When does the default work well?
- **current_section_observation:** The pattern can summarize several systems when their interaction is the bounded subject and details route outward.
- **supporting_reason:** A high-level causal model may be more useful than isolated subsystem pages for one cross-boundary decision.
- **counterargument_or_limit:** The overview must not imply details or guarantees omitted from source evidence.
- **assumptions_and_boundaries:** Abstraction level and non-goals remain explicit.
- **revision_decision:** Add overview-as-subject guidance and companion routes.
- **additional_insight_to_add:** Multiple systems are not automatically multiple stories when the relation among them is the story.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The standalone pattern fails when live data, authentication, personalization, complex state, shared releases, or broad dynamic support becomes essential.
- **supporting_reason:** Those requirements introduce application operations and governance beyond a document artifact.
- **counterargument_or_limit:** A static explainer can remain a companion even after an application is required.
- **assumptions_and_boundaries:** Separate explanatory truth from operational control and test each surface independently.
- **revision_decision:** Define application-boundary triggers and companion retention.
- **additional_insight_to_add:** Moving runtime behavior out of the explainer can preserve its clarity while enabling a richer tool alongside it.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** Scale responses include narrowing, chapter series, overview plus deep dives, generated static site, shared component system, or full application.
- **supporting_reason:** They trade direct portability against reuse, navigation, release discipline, and runtime capability.
- **counterargument_or_limit:** Introducing infrastructure early can cost more than maintaining a few independent files.
- **assumptions_and_boundaries:** Demonstrated reuse and coordinated change justify shared architecture.
- **revision_decision:** Map each transition to evidence and migration safeguards.
- **additional_insight_to_add:** Reuse should be measured through repeated change, not predicted from visual similarity.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Scaling risks include duplicated facts, diverging templates, broken cross-page navigation, distributed ownership gaps, stale evidence, and one build failure taking down every explainer.
- **supporting_reason:** Shared infrastructure reduces duplication but increases correlated failure and migration cost.
- **counterargument_or_limit:** Strong tests and ownership can manage correlated risk.
- **assumptions_and_boundaries:** Shared systems need versioning, rollback, and per-page regression evidence.
- **revision_decision:** Add coupling and blast-radius checks before consolidation.
- **additional_insight_to_add:** The optimal architecture minimizes correlated semantic drift as well as code duplication.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** Good scale is an overview plus owned deep dives; bad scale is a single file with several unrelated tools; borderline scale is a growing family with copied styles but shared facts.
- **supporting_reason:** The examples distinguish narrative cohesion from implementation reuse pressure.
- **counterargument_or_limit:** Copied styles may remain cheaper when pages are stable and independently owned.
- **assumptions_and_boundaries:** First-refresh evidence determines whether consolidation pays.
- **revision_decision:** Add example transitions and review timing.
- **additional_insight_to_add:** Style duplication and truth duplication have different risks and may warrant different solutions.
### Question 08: How can the important claims be verified?
- **current_section_observation:** Scale decisions can be tested through dependency maps, ownership maps, change-impact records, page cohesion review, build reproduction, and support-matrix capacity.
- **supporting_reason:** These show where coupling and coordination cost actually exist.
- **counterargument_or_limit:** Future growth remains uncertain.
- **assumptions_and_boundaries:** Prefer reversible changes and revisit at observed pressure points.
- **revision_decision:** Add transition evidence and rollback requirements.
- **additional_insight_to_add:** A reversible migration protects explanatory continuity while infrastructure assumptions are tested.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** Single-file intent is local fact, while the exact boundary for series, site, or application is engineering judgment.
- **supporting_reason:** No production scale study accompanies the archived pattern.
- **counterargument_or_limit:** Existing repository conventions may provide stronger architecture signals.
- **assumptions_and_boundaries:** Follow current local platform ownership and verification when present.
- **revision_decision:** Avoid universal page, source, or traffic counts and state qualitative triggers.
- **additional_insight_to_add:** Honest qualitative boundaries remain useful when they name observable transition symptoms.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** Scaling presentation and scaling subject evidence are separate problems; shared components do not solve conflicting claims.
- **supporting_reason:** Infrastructure consolidation can hide semantic divergence behind visual consistency.
- **counterargument_or_limit:** Shared evidence tooling can improve provenance across a page family.
- **assumptions_and_boundaries:** Content and presentation layers need distinct ownership and tests.
- **revision_decision:** Add dual migration tracks for source truth and rendering infrastructure.
- **additional_insight_to_add:** A page family is healthy when common style can change without rewriting truth and source truth can change without uncontrolled cross-page drift.
## Section 025: Future Refresh Search Queries
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed preserves three generic searches but does not say what unresolved decision triggers them or when a search result is sufficient.
- **supporting_reason:** Query plans should guide targeted freshness work rather than imply that searching itself validates the reference.
- **counterargument_or_limit:** Future search engines, terminology, and authoritative sources may differ from current assumptions.
- **assumptions_and_boundaries:** Preserve the required query strings as frozen leads and permit evidence-driven refinement during an authorized refresh.
- **revision_decision:** Add purpose, preferred evidence, stop condition, and recording rule around each exact inherited query.
- **additional_insight_to_add:** A search query is an acquisition instrument, not an evidence source.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** The default refresh begins from a named stale or unknown claim, then seeks current primary material and tests observable behavior.
- **supporting_reason:** This minimizes broad context, weak secondary sources, and irrelevant best-practice lists.
- **counterargument_or_limit:** The inherited queries are broad and may help discover terminology before precise sources are known.
- **assumptions_and_boundaries:** Use broad results only to refine the route, not as final support.
- **revision_decision:** Define a two-stage discovery then verification process.
- **additional_insight_to_add:** Search refinement should narrow the claim and authority requirement simultaneously.
### Question 03: When does the default work well?
- **current_section_observation:** Planned refresh works for versioned platform guidance, changed tool behavior, new browser constraints, and migration-sensitive recommendations.
- **supporting_reason:** These claims have identifiable freshness triggers and primary-source destinations.
- **counterargument_or_limit:** Audience comprehension and local narrative fit are not answered well by web search.
- **assumptions_and_boundaries:** Use artifact and reader evidence for those questions.
- **revision_decision:** Add a non-searchable-question warning.
- **additional_insight_to_add:** Choosing not to search is correct when the uncertainty concerns local readers rather than public facts.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** Search fails when results are copied from snippets, broad roots, undated examples, or repositories without applicability review.
- **supporting_reason:** Discovery relevance is not entailment, freshness, or authority.
- **counterargument_or_limit:** Community examples can reveal practical edge cases absent from official documentation.
- **assumptions_and_boundaries:** Use them as comparative evidence and verify behavior directly.
- **revision_decision:** Add source-role and corroboration requirements.
- **additional_insight_to_add:** A useful contradictory example may weaken a claim even when it cannot establish the replacement rule alone.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** Refresh methods include direct known-page inspection, targeted site search, repository history, release notes, issue evidence, and local browser experiments.
- **supporting_reason:** Each method balances authority, recency, implementation detail, and reproducibility.
- **counterargument_or_limit:** A comprehensive survey can consume more effort than the claim warrants.
- **assumptions_and_boundaries:** Scale research to consequence and volatility.
- **revision_decision:** Add an escalation order from primary docs to code history, comparative evidence, and direct tests.
- **additional_insight_to_add:** The cheapest authoritative source should close the claim before broader research continues.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Query risks include confirmation bias, date confusion, renamed products, copied examples, search ranking effects, and losing the exact inherited strings.
- **supporting_reason:** These issues compromise reproducibility and can silently shift scope.
- **counterargument_or_limit:** Query variation is necessary when terminology changes.
- **assumptions_and_boundaries:** Retain the frozen query and record every refined query separately with rationale.
- **revision_decision:** Preserve exact strings once and add a query lineage record.
- **additional_insight_to_add:** Query lineage makes search drift visible without pretending the original wording remains optimal.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** Good refresh links a precise claim to an inspected primary passage; bad refresh cites a result page; borderline refresh uses a current repository example without version context.
- **supporting_reason:** These examples separate discovery, evidence, and applicability.
- **counterargument_or_limit:** Repository code at a pinned revision can be strong implementation evidence.
- **assumptions_and_boundaries:** Record revision, path, behavior, and relevance to the artifact environment.
- **revision_decision:** Add evidence acceptance criteria beneath the query table.
- **additional_insight_to_add:** Version-pinned implementation can outrank narrative documentation for observed behavior while remaining non-normative.
### Question 08: How can the important claims be verified?
- **current_section_observation:** Verify refresh through exact query log, inspected URLs or revisions, dates, claim excerpts paraphrased within limits, contradiction notes, and artifact consequences.
- **supporting_reason:** This makes the decision reproducible without copying whole sources.
- **counterargument_or_limit:** External pages can change after inspection.
- **assumptions_and_boundaries:** Record date and mark evidence stale on relevant change triggers.
- **revision_decision:** Define a compact refresh evidence packet and stop rule.
- **additional_insight_to_add:** Research is complete when the decision is supported or explicitly unresolved, not when a target number of sources is reached.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The three query strings and labels are frozen seed facts; their current results and usefulness are unknown because none was executed.
- **supporting_reason:** The no-browse task forbids claiming refreshed external evidence.
- **counterargument_or_limit:** Their wording indicates intended categories of docs, repositories, and release changes.
- **assumptions_and_boundaries:** Category intent can guide future work but not support present claims.
- **revision_decision:** Mark every row unexecuted and preserve exact text once.
- **additional_insight_to_add:** Explicit unexecuted status prevents a future reader from mistaking a research plan for completed research.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** Search freshness and artifact freshness are related but independent; current guidance can still be misapplied to an old generated page.
- **supporting_reason:** Updating citations does not update the story, code, layout, or test evidence automatically.
- **counterargument_or_limit:** A refresh may conclude no artifact change is needed.
- **assumptions_and_boundaries:** Record that impact decision and its evidence.
- **revision_decision:** Require post-research claim and artifact impact analysis.
- **additional_insight_to_add:** The output of research is a changed or reaffirmed decision, not merely a refreshed bibliography.
## Section 026: Evidence Boundary Notes
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed defines three labels but does not help readers classify implementation observations, illustrative scenarios, conflicts, unknowns, or recommendations with mixed support.
- **supporting_reason:** Final evidence notes should determine how strongly each kind of statement may be reused and what proof is still required.
- **counterargument_or_limit:** Excessive labels can interrupt reading and create a false appearance of formal certainty.
- **assumptions_and_boundaries:** Label at section or claim clusters where provenance changes, with closer attribution for high-consequence statements.
- **revision_decision:** Expand the vocabulary, reuse rules, conflict handling, and no-browse disclosure while retaining the three required core labels.
- **additional_insight_to_add:** Evidence boundaries are most valuable at transitions where a reader might otherwise mistake recommendation for observation.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** Default classification separates directly read local guidance, observed linked-artifact behavior, refreshed external evidence, combined inference, illustration, and unresolved status.
- **supporting_reason:** These categories map to distinct verification and maintenance actions.
- **counterargument_or_limit:** One sentence can contain several categories.
- **assumptions_and_boundaries:** Split or qualify mixed statements rather than assigning one broad label that hides composition.
- **revision_decision:** Add a classification table with allowed claim strength and required follow-up.
- **additional_insight_to_add:** Granular labeling makes later refresh targeted because maintainers know which evidence class changed.
### Question 03: When does the default work well?
- **current_section_observation:** Explicit boundaries work well for synthesized references that combine archived workflow, implementation inspection, design judgment, and future research pointers.
- **supporting_reason:** The reader can adopt local defaults without assuming universal validation.
- **counterargument_or_limit:** A simple source-only note may need less labeling.
- **assumptions_and_boundaries:** Use the least labeling that preserves material distinctions.
- **revision_decision:** Add proportionality guidance and examples of boundary placement.
- **additional_insight_to_add:** Boundary density should follow consequence and source transition, not paragraph count.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** Labeling fails when local facts are generalized universally, unvisited URLs are called external facts, or inference is phrased as measured outcome.
- **supporting_reason:** The label then launders rather than clarifies authority.
- **counterargument_or_limit:** Strong recommendations can still be made from local evidence when explicitly scoped to the workflow.
- **assumptions_and_boundaries:** Claim strength follows scope and entailment, not whether evidence is local or external alone.
- **revision_decision:** Add misuse warnings and require claim-scope alignment.
- **additional_insight_to_add:** Narrow local evidence can support a strong local rule, while broad weak evidence supports little.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** Alternatives include inline citations, footnotes, source ledgers, confidence scores, or unlabeled prose with a bibliography.
- **supporting_reason:** Labels are lightweight and readable, while claim ledgers handle complex traceability better.
- **counterargument_or_limit:** Confidence scores imply calibration that is absent here.
- **assumptions_and_boundaries:** Use labels plus source ledger and avoid unsupported numeric confidence.
- **revision_decision:** Explain when close inline attribution is needed beyond a section-level label.
- **additional_insight_to_add:** Confidence and provenance answer different questions and should not be collapsed into one score.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Risks include stale local archives, copied label text, hidden contradictions, examples read as cases, and evidence transferred across media without retesting usability.
- **supporting_reason:** These failures create subtle authority and applicability drift.
- **counterargument_or_limit:** Some source truth can transfer safely when scope and bytes are unchanged.
- **assumptions_and_boundaries:** Transfer semantic evidence only after checking claim identity; recollect artifact-specific evidence.
- **revision_decision:** Add transfer and staleness rules.
- **additional_insight_to_add:** Evidence attaches to a claim under conditions, not permanently to a sentence or file.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** Good labeling says the generator refuses overwrite in the inspected archive; bad labeling says best practice requires it; borderline labeling infers accessibility from semantic-looking markup.
- **supporting_reason:** Examples reveal the difference between observation, scoped recommendation, and unverified outcome.
- **counterargument_or_limit:** Semantic structure can still be useful supporting evidence for accessibility review.
- **assumptions_and_boundaries:** It cannot establish conformance or actual usability alone.
- **revision_decision:** Add concise classification examples below the table.
- **additional_insight_to_add:** A borderline claim often becomes safe by weakening its verb and naming the missing test.
### Question 08: How can the important claims be verified?
- **current_section_observation:** Boundary accuracy can be tested by sampling statements, reopening sources, checking retrieval history, reproducing observed behavior, and locating unresolved statuses.
- **supporting_reason:** This verifies both attribution and the absence of fabricated refresh.
- **counterargument_or_limit:** Full claim auditing is costly for large references.
- **assumptions_and_boundaries:** Audit every high-consequence claim and representative lower-risk sections.
- **revision_decision:** Add a final evidence-boundary audit procedure.
- **additional_insight_to_add:** Sampling should target transitions and strong verbs because they carry the greatest laundering risk.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** Complete local reads and archived script behavior are known; external content, audience outcomes, universal design effects, and numeric targets remain unverified or locally judged.
- **supporting_reason:** This summary accurately reflects the work performed and the no-browse constraint.
- **counterargument_or_limit:** Direct reading does not eliminate interpretation error.
- **assumptions_and_boundaries:** Complete-file reread and source comparison reduce but do not abolish that risk.
- **revision_decision:** State known, inferred, illustrative, and unknown categories explicitly in the final notes.
- **additional_insight_to_add:** Epistemic humility is operational when it routes the next verification rather than merely adding a disclaimer.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** Evidence boundaries form a maintenance architecture connecting claim, source, artifact, condition, and owner.
- **supporting_reason:** This architecture enables selective refresh, safe handoff, and correction after drift.
- **counterargument_or_limit:** Maintaining it has overhead that may exceed value for ephemeral drafts.
- **assumptions_and_boundaries:** Preserve a minimal source and uncertainty record whenever another reader may act on the page.
- **revision_decision:** End with a minimum reusable evidence packet and a stop condition for unsupported reuse.
- **additional_insight_to_add:** The boundary system succeeds when a future maintainer can tell what may be reused, what must be retested, and what remains unknown without contacting the original author.
