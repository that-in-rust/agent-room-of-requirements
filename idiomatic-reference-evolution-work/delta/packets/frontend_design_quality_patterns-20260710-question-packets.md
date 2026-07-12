## Section 001: Frontend Design Quality Patterns
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed title does not tell an agent whether the reference chooses visual style, interaction architecture, implementation quality, or release readiness.
- **supporting_reason:** Frontend quality decisions couple user task completion, state behavior, accessibility, responsive composition, visual language, assets, and verification, so the opening must define their order and ownership.
- **counterargument_or_limit:** A narrow component correction may need only the repository's existing contract and regression evidence rather than a broad design workflow.
- **assumptions_and_boundaries:** Use this reference for a user-facing interface decision whose experience quality matters; route product discovery, domain policy, causal debugging, or platform-specific implementation to their owning methods.
- **revision_decision:** Turn the title into an operating contract for selecting, implementing, and verifying a frontend experience without inventing product intent.
- **additional_insight_to_add:** Visual polish is safe only after the interface's user, job, states, and evidence boundary are explicit.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The heading supplies no default sequence, while the local skill begins with purpose, tone, constraints, and differentiation before implementation.
- **supporting_reason:** A context-first sequence prevents generic styling and lets aesthetic choices reinforce the task instead of competing with it.
- **counterargument_or_limit:** Existing products often have a mature design system whose patterns should be reused before choosing a new visual direction.
- **assumptions_and_boundaries:** Start from current user workflow and repository conventions, then define state completeness, accessibility, responsive behavior, visual system, implementation, and rendered verification.
- **revision_decision:** Publish a default workflow with explicit reuse, adaptation, and route-away checks.
- **additional_insight_to_add:** Distinctiveness should come from a small number of coherent product-specific decisions rather than novelty applied to every control.

### Question 03: When does the default work well?
- **current_section_observation:** The title does not identify favorable tasks, even though the mapped skill assumes a page, component, application, or interface with a known audience and purpose.
- **supporting_reason:** The method works when the primary user journey, product context, target devices, technical stack, and verification surface can be inspected before coding.
- **counterargument_or_limit:** Concept exploration may intentionally compare several visual directions before one is selected for production.
- **assumptions_and_boundaries:** Exploratory concepts remain nonaccepting until a direction has an owner, a behavior contract, and evidence across required states and viewports.
- **revision_decision:** Add a fit checklist for known task, audience, product mode, design-system status, interaction states, and rendering environment.
- **additional_insight_to_add:** The reference is most valuable at handoffs where design intent would otherwise be reduced to screenshots without state semantics.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** A title-only opening offers no refusal path when product intent, content, accessibility policy, target environment, or behavior is unresolved.
- **supporting_reason:** CSS and component structure cannot decide business workflow, legal copy, authorization, or acceptable operational risk.
- **counterargument_or_limit:** A prototype can expose missing decisions by making alternatives concrete and testable.
- **assumptions_and_boundaries:** Keep prototypes reversible, label placeholder content and assumptions, and prevent them from becoming release evidence without owner review.
- **revision_decision:** Add route-away conditions for product discovery, content authority, domain accessibility review, runtime diagnosis, and performance measurement.
- **additional_insight_to_add:** The wrong-tool signal is an unresolved experience decision that visual execution would silently choose on the user's behalf.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The seed heading collapses adjacent choices such as design-system reuse, bespoke composition, information architecture, interaction prototyping, visual exploration, and production hardening.
- **supporting_reason:** Each alternative optimizes a different risk: consistency, differentiation, workflow clarity, learning speed, maintainability, or release confidence.
- **counterargument_or_limit:** Splitting design into many artifacts can fragment the relationship between behavior and presentation.
- **assumptions_and_boundaries:** Keep one experience decision record while routing specialized questions to existing design, content, accessibility, performance, or framework authorities.
- **revision_decision:** Add an alternative-routing view keyed by the unresolved decision and evidence expected back.
- **additional_insight_to_add:** Artifact boundaries should follow who can invalidate the decision, because visual tokens, product behavior, and legal content change for different reasons.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** The opening hides recurrent hazards such as generic templates, marketing composition for operational tools, incomplete states, inaccessible controls, responsive overflow, and unverified visual assets.
- **supporting_reason:** These defects can coexist with attractive static screenshots while making real use confusing or impossible.
- **counterargument_or_limit:** A reference overloaded with prohibitions can suppress appropriate experimentation and lead to visually timid output.
- **assumptions_and_boundaries:** Express constraints causally and allow exceptions when user context, product conventions, and rendered evidence support them.
- **revision_decision:** Include a concise opening hazard register and link each hazard to later checks.
- **additional_insight_to_add:** The most dangerous frontend failure is a presentation that signals completion while loading, error, focus, overflow, or recovery behavior remains unimplemented.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** The bare title provides no contrast between designed product behavior and a polished but generic mockup.
- **supporting_reason:** Examples should show that good work completes the workflow and states, bad work decorates an unsuitable layout, and borderline work is visually strong but lacks required runtime evidence.
- **counterargument_or_limit:** A static promotional page legitimately has fewer application states than an authenticated operational tool.
- **assumptions_and_boundaries:** Judge each example against its actual product category, user task, content, and expected interaction surface.
- **revision_decision:** Add opening examples for an operational interface, a decorative template mismatch, and a concept awaiting accessibility and responsive validation.
- **additional_insight_to_add:** Borderline designs should state the exact promotion gate, because visual quality is not binary before implementation evidence exists.

### Question 08: How can the important claims be verified?
- **current_section_observation:** No acceptance mechanism is attached to the heading, so a reviewer cannot tell whether the reference improved a user experience or only generated more design prose.
- **supporting_reason:** Behavior tests, keyboard review, accessibility checks, rendered screenshots, viewport inspection, console/runtime evidence, and task reconstruction observe complementary failure classes.
- **counterargument_or_limit:** Automated checks cannot judge contextual tone, hierarchy, trust, or aesthetic coherence fully.
- **assumptions_and_boundaries:** Combine deterministic and browser checks with human review against named users, tasks, visual direction, and design-system authority.
- **revision_decision:** Define a minimum done condition spanning function, states, accessibility, responsiveness, visual coherence, and recovery.
- **additional_insight_to_add:** Visual verification must inspect actual rendered pixels and interaction state, not infer quality from component source alone.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The two local source paths are byte-identical and directly recommend purpose, tone, constraints, differentiation, and coherent aesthetics, while the mapped public pages were not opened.
- **supporting_reason:** Complete local reads establish the inherited guidance; no target interface, user study, browser run, or external refresh was performed for this section.
- **counterargument_or_limit:** Strong systems and design reasoning can still justify accessible, state-complete, responsive defaults without a study of every product.
- **assumptions_and_boundaries:** Label local source content as observed, design defaults as reasoned guidance, target outcomes as unverified, and public pointers as unrefreshed.
- **revision_decision:** Put the known/unknown boundary in the opening and avoid presenting aesthetic preferences as universal facts.
- **additional_insight_to_add:** Confidence can be high in a rendered defect and low in its aesthetic remedy, so evidence state belongs to each claim rather than the page as a whole.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The title does not reveal that a frontend is a coupled state machine, information hierarchy, visual system, accessibility surface, and runtime boundary.
- **supporting_reason:** A decision in one layer can alter another: animation affects input, typography affects layout, density affects scanning, and data state affects composition.
- **counterargument_or_limit:** Modeling every visual detail as a formal dependency would make ordinary implementation cumbersome.
- **assumptions_and_boundaries:** Track dependencies for user-critical states and stable system decisions while leaving local decorative tuning lightweight.
- **revision_decision:** Frame frontend quality as coherent evidence across behavior, perception, and operation, with selective invalidation when premises change.
- **additional_insight_to_add:** The durable unit is not a screenshot or component but a user task across its meaningful states and environments.

## Section 002: Source Evidence Mapping Table
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed lists two local skill paths and three public documentation roots but does not distinguish historical design guidance, current local guidance, target product authority, runtime evidence, or an unvisited research pointer.
- **supporting_reason:** A frontend recommendation can be valid as aesthetic inspiration yet invalid for an existing design system, supported browser, accessibility policy, or user workflow.
- **counterargument_or_limit:** A compact bibliography is easier to scan than a claim-specific evidence map.
- **assumptions_and_boundaries:** Keep the first view concise while recording content identity, authority, freshness, applicability, and invalidation for durable use.
- **revision_decision:** Expand the table into local content families, current process controls, target evidence classes, and unrefreshed external queues.
- **additional_insight_to_add:** Source mapping must tell the agent which evidence can choose behavior, which can shape presentation, and which can only suggest a future check.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The seed implies local-first retrieval but counts two byte-identical frontend-design files as separate source rows.
- **supporting_reason:** Read one representative copy completely for meaning, retain both paths for temporal provenance, then inspect current repository conventions and rendered target behavior before adapting guidance.
- **counterargument_or_limit:** Equal bytes do not prove the archive and current path had identical surrounding plugin metadata, activation, ownership, or intended authority.
- **assumptions_and_boundaries:** Treat hash equality as content identity only and preserve path/date/package context separately.
- **revision_decision:** Define a default route from active instructions and target UI through one local design source, with external refresh only when authorized and decision-relevant.
- **additional_insight_to_add:** The best inspiration source and the source that settles release behavior are often different artifacts.

### Question 03: When does the default work well?
- **current_section_observation:** The typed route works when repository components, tokens, routes, tests, assets, and browser rendering are locally inspectable.
- **supporting_reason:** Those artifacts can reveal both design-system intent and the actual behavior that generic guidance cannot establish.
- **counterargument_or_limit:** A greenfield concept may have no existing system, content, or runtime baseline.
- **assumptions_and_boundaries:** In greenfield work, product/audience decisions and prototypes remain explicit authorities until stable code and tests exist.
- **revision_decision:** Add established-product and greenfield evidence profiles to the source map.
- **additional_insight_to_add:** Absence of a design system increases design responsibility; it does not make the inherited skill a product authority.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The map fails when duplicate files are counted as corroboration, a documentation root is treated as current fact, or visual source material overrules user, repository, accessibility, and runtime constraints.
- **supporting_reason:** These errors inflate confidence and can produce attractive but incompatible or unusable interfaces.
- **counterargument_or_limit:** Public primary documentation can become decisive for a versioned framework or rendering feature after retrieval and local reproduction.
- **assumptions_and_boundaries:** Promote an external pointer only with access date, version applicability, exact claim, and target check.
- **revision_decision:** Add duplicate, unrefreshed, refreshed, reproduced, conflicting, and inapplicable states.
- **additional_insight_to_add:** Fresh external advice can still be irrelevant when the product deliberately pins an older framework or interaction contract.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** Alternatives include repository source, rendered browser inspection, design files, design tokens, product requirements, accessibility policy, component stories, user research, official documentation, and community examples.
- **supporting_reason:** Each observes a different layer: intended workflow, implemented structure, actual pixels, supported API, or user outcome.
- **counterargument_or_limit:** Loading every source for every component can overwhelm context and slow a reversible correction.
- **assumptions_and_boundaries:** Select the smallest complementary set capable of settling the consequential claim and record omitted evidence.
- **revision_decision:** Add a claim-to-authority matrix and progressive source route.
- **additional_insight_to_add:** Source diversity matters only when the sources can fail differently, such as design intent versus rendered runtime behavior.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Hazards include machine-local paths, unexplained canonical roles, source drift, mutable public pages, source screenshots without state, aspirational design files, stale stories, generic examples, and inaccessible private assets.
- **supporting_reason:** Each can make a visual or behavioral claim appear more current, complete, or reproducible than it is.
- **counterargument_or_limit:** Historical screenshots and examples remain useful for intent reconstruction and regression comparison.
- **assumptions_and_boundaries:** Label historical, illustrative, and current-rendered evidence separately and preserve target identity.
- **revision_decision:** Add source-risk and invalidation columns plus conflict procedures.
- **additional_insight_to_add:** A screenshot proves pixels under one state; it cannot prove focus behavior, responsive range, data transitions, or source authority.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** The seed offers no example of reconciling local aesthetic guidance with an established product surface.
- **supporting_reason:** Good use takes intentionality from the skill while reusing product tokens and verifies real states; bad use treats two duplicate paths and three links as consensus for a redesign.
- **counterargument_or_limit:** A concise design note may cite one representative skill path when the complete provenance ledger exists elsewhere.
- **assumptions_and_boundaries:** Representative citation is safe only when duplicate identity, target authority, and unrefreshed status remain recoverable.
- **revision_decision:** Add good, bad, and conditional source-use examples.
- **additional_insight_to_add:** Concision should remove repeated locators, not erase the distinction between inspiration, contract, and observation.

### Question 08: How can the important claims be verified?
- **current_section_observation:** The seed labels sources but supplies no existence, hash, complete-read, rendered-state, external-refresh, or applicability gate.
- **supporting_reason:** Hashes establish local identity, diffs reveal drift, source/tests establish implementation, browser fixtures expose pixels and interaction, and authorized retrieval can refresh public contracts.
- **counterargument_or_limit:** None of these mechanisms alone establishes that the interface fits users or achieves visual coherence.
- **assumptions_and_boundaries:** Pair mechanical evidence with task-oriented and experienced visual review proportional to consequence.
- **revision_decision:** Add a reproducible source audit and claim-promotion protocol.
- **additional_insight_to_add:** Verification should run both directions so changed tokens, components, content, or external APIs identify which design claims must be reopened.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** Both mapped local paths exist and share SHA-256 `d39adf3...157184`; the working seed identity and structural process are also directly observable, while no external page was opened.
- **supporting_reason:** Complete local reads and hashes establish the local content family without relying on memory or public research.
- **counterargument_or_limit:** The reason one path is called canonical and the other supporting is not explained by their identical body text.
- **assumptions_and_boundaries:** Preserve role labels as corpus metadata and avoid deriving technical authority from unexplained classification.
- **revision_decision:** Add known, inferred, unrefreshed, and unknown-authority states alongside identities.
- **additional_insight_to_add:** Content confidence and governance confidence can diverge even when byte identity is exact.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The flat map can be modeled as a causal chain from product and design authority through implementation to browser evidence and later feedback.
- **supporting_reason:** Upstream intent guides choices, while downstream rendered behavior supports or refutes whether those choices survived code, content, and environment.
- **counterargument_or_limit:** Runtime feedback can change design guidance, so the graph includes versioned feedback rather than a one-way hierarchy.
- **assumptions_and_boundaries:** Record each update as a new state and retain prior evidence for regression interpretation.
- **revision_decision:** Add source dependency and targeted invalidation rules.
- **additional_insight_to_add:** A design reference becomes durable when it can explain why a visual decision changed after real usage without rewriting its historical premise.

## Section 003: Pattern Scoreboard Ranking Table
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed repeats one theme identifier for three scored practices and does not explain whether 95, 91, and 88 measure priority, evidence, effectiveness, maturity, or preference.
- **supporting_reason:** A useful register should tell an agent which frontend control prevents which failure and what evidence demonstrates adoption.
- **counterargument_or_limit:** Numeric ordering is compact and may preserve editorial emphasis even without calibration.
- **assumptions_and_boundaries:** Retain the values as frozen source metadata while refusing percentage or cross-project interpretation.
- **revision_decision:** Give the three rows distinct stable keys and convert the scoreboard into a causal adoption guide.
- **additional_insight_to_add:** Frontend priorities should follow user-impact containment and prerequisite order, not the authority implied by unexplained precision.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The seed order suggests source mapping, evidence boundaries, then verification, but it omits the frontend-specific transition from context to states to rendered result.
- **supporting_reason:** The agent must understand the product and existing system before choosing a direction, specify material states before polishing, and inspect real rendering before acceptance.
- **counterargument_or_limit:** An established component with a current visual regression may already satisfy earlier controls implicitly.
- **assumptions_and_boundaries:** Compress the visible process only when source identity, state contract, and rendered rejection behavior remain reconstructable.
- **revision_decision:** Establish `workflow_context_first -> state_complete_interface -> rendered_evidence_coupling` as the default chain.
- **additional_insight_to_add:** These controls are multiplicative: a distinctive page with missing recovery or a complete state model with no pixel inspection still fails quality.

### Question 03: When does the default work well?
- **current_section_observation:** Every seed row is marked default adoption without task profiles or proportionality guidance.
- **supporting_reason:** The chain works well for new pages, application workflows, component redesigns, design-system additions, and durable multi-agent handoffs.
- **counterargument_or_limit:** A one-line token correction may need only current authority, affected-state rendering, and a focused regression.
- **assumptions_and_boundaries:** Preserve the reasoning invariant while scaling artifact depth with consequence and change surface.
- **revision_decision:** Add lightweight correction, standard experience, and high-assurance interface profiles.
- **additional_insight_to_add:** Default adoption can be demonstrated in concise evidence; it does not require a large design packet for every CSS edit.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The scoreboard misleads when its numbers are treated as measured quality gains or when every pattern is applied mechanically to all product categories.
- **supporting_reason:** No scoring formula, user sample, project cohort, outcome metric, uncertainty, or reviewer rubric appears in the local source family.
- **counterargument_or_limit:** A maintained team rubric can legitimately rank practices when its owner, criteria, and review process are explicit.
- **assumptions_and_boundaries:** Freeze inherited values and calibrate any current priority against local failures and user consequence.
- **revision_decision:** Add no-claim, adaptation, counter-signal, and retirement conditions.
- **additional_insight_to_add:** A frontend pattern should lose default status when it produces visual ceremony without improving task success, state resilience, or detectability.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** Alternatives include qualitative tiers, prerequisite graphs, risk matrices, product-category rubrics, accessibility blockers, and outcome-calibrated rankings.
- **supporting_reason:** Graphs show order, matrices show fit, blockers express nonnegotiable constraints, and measured outcomes can support later prioritization.
- **counterargument_or_limit:** Multiple representations can drift and confuse which register governs review.
- **assumptions_and_boundaries:** Maintain one semantic pattern register and derive concise views from it.
- **revision_decision:** Pair preserved scores with a qualitative fit/evidence table rather than inventing replacement numbers.
- **additional_insight_to_add:** Visual preference should not compete on the same scale as a keyboard blocker or broken primary workflow.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Hazards include duplicate identifiers, score inflation, stale aesthetic fashion, absent implementation cost, correlated checks, and rewarding visual output volume.
- **supporting_reason:** These defects can steer agents toward fashionable artifacts rather than context-appropriate and verifiable experiences.
- **counterargument_or_limit:** Stable keys and compact tiers still improve retrieval and governance when semantics are explicit.
- **assumptions_and_boundaries:** Separate inherited score, current posture, protected failure, cost, verification, and review state.
- **revision_decision:** Add counter-signals and downgrade triggers for every current control.
- **additional_insight_to_add:** A pattern register needs a measure against overuse, such as card proliferation or motion density, because maximizing visible design can reduce clarity.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** The seed does not demonstrate how its ranking changes one frontend decision.
- **supporting_reason:** Good use inspects an operational workflow, completes failure states, and verifies mobile pixels; bad use cites score 95 to justify a bespoke hero; borderline reuse relies on a mature system but still renders the changed state.
- **counterargument_or_limit:** A marketing page can legitimately prioritize memorable visual composition more heavily than an internal tool.
- **assumptions_and_boundaries:** Apply product-category context before ranking visual differentiation against familiarity and density.
- **revision_decision:** Add adoption, misuse, and implicit-reuse examples.
- **additional_insight_to_add:** Pattern names and scores are retrieval aids; the observed user-state boundary is the real unit of adoption.

### Question 08: How can the important claims be verified?
- **current_section_observation:** The seed attaches no test to the score values, pattern execution, or failure-prevention effect.
- **supporting_reason:** Adoption can be audited through source/context records, state matrices, negative fixtures, keyboard paths, viewport screenshots, visual review, and downstream reversals.
- **counterargument_or_limit:** These checks establish process and bounded interface quality more directly than causal productivity or satisfaction improvement.
- **assumptions_and_boundaries:** Require representative task or user evidence before claiming broad effectiveness and keep conformance distinct.
- **revision_decision:** Add current process gates and a future calibration protocol.
- **additional_insight_to_add:** Verification must inject the failure a pattern claims to prevent; finding the pattern label in prose is not evidence.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The seed definitely contains values 95, 91, and 88 under default-tier labels, but the mapped skill provides no derivation for them.
- **supporting_reason:** Complete local reads establish table content while the missing method blocks empirical interpretation.
- **counterargument_or_limit:** The sequence aligns with a defensible design workflow and may encode undocumented editorial experience.
- **assumptions_and_boundaries:** Present the order as reasoned current guidance and the numbers as historical metadata.
- **revision_decision:** Label every inherited value and new qualitative recommendation by evidence basis.
- **additional_insight_to_add:** Unknown score provenance is a reason to rebuild present decisions from observable user risk, not to erase the historical row.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The three seed controls can expand into a lifecycle covering product fit, state architecture, accessibility, visual system, implementation, rendering, and invalidation.
- **supporting_reason:** Those stages close gaps between design intent and the browser experience that static guidance alone cannot address.
- **counterargument_or_limit:** An indefinitely expanding pattern catalog can bury the core defaults.
- **assumptions_and_boundaries:** Admit a pattern only when it prevents a distinct recurring failure and has a capable gate.
- **revision_decision:** Define admission, promotion, adaptation, and retirement rules for the frontend register.
- **additional_insight_to_add:** The register becomes executable when every pattern names prerequisites, a rejected state, actual evidence, and the future change that reopens it.

## Section 004: Idiomatic Thesis Synthesis Statement
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed says to load local evidence, check public guidance, and add verification, but it does not define what makes a frontend recommendation coherent or executable.
- **supporting_reason:** The decisive question is whether behavior, state, semantics, composition, visual language, and runtime evidence support the same user task.
- **counterargument_or_limit:** Some aesthetic judgments remain qualitative and cannot be reduced to automated assertions.
- **assumptions_and_boundaries:** Human review is a valid gate when its audience, direction, criteria, comparison states, and rejection conditions are explicit.
- **revision_decision:** State one governing thesis and derive conversion steps from product context through rendered acceptance.
- **additional_insight_to_add:** Frontend executability is a property of the experience decision flow, not merely component code or screenshot presence.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The seed omits the transformations between source discovery and implementation.
- **supporting_reason:** The default should convert product evidence into a workflow, workflow into states and semantics, constraints into composition, direction into a visual system, and implementation into browser evidence.
- **counterargument_or_limit:** Mature products can encode several conversions in current components and tests.
- **assumptions_and_boundaries:** Reuse is safe when the existing behavior, visual authority, state coverage, and rendered validity remain reconstructable.
- **revision_decision:** Express the thesis as an evidence-to-experience pipeline with fail and route states.
- **additional_insight_to_add:** The pipeline should fail at the earliest unsupported conversion so downstream polish cannot conceal a wrong product premise.

### Question 03: When does the default work well?
- **current_section_observation:** The seed thesis does not name the development conditions under which this synthesis adds value.
- **supporting_reason:** It works when design and implementation cross people or agents, components can drift, and browsers/tests can observe meaningful states.
- **counterargument_or_limit:** Disposable moodboards and visual spikes may prioritize exploration over durable traceability.
- **assumptions_and_boundaries:** Keep exploration nonaccepting and promote retained concepts through state, accessibility, repository, and rendering gates.
- **revision_decision:** Add lifespan, handoff, product maturity, and observability fit criteria.
- **additional_insight_to_add:** The longer an interface must evolve, the more valuable explicit visual rationale and invalidation become.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The thesis fails if context-first becomes resistance to innovation, accessibility becomes scanner worship, or intentionality becomes post hoc justification for a preferred style.
- **supporting_reason:** Existing systems can be wrong, tools have blind spots, and rationales can rationalize choices rather than challenge them.
- **counterargument_or_limit:** These are misuse boundaries, not reasons to abandon continuity, accessibility, or visual direction.
- **assumptions_and_boundaries:** Require counterexamples, user consequence, alternative comparison, and rendered negative states so each principle can reject its misuse.
- **revision_decision:** Add anti-dogma conditions to every thesis component.
- **additional_insight_to_add:** A design principle is trustworthy only when it names the product conditions under which another approach should replace it.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The seed offers one synthesis route without comparing design-system reuse, bespoke art direction, usability prototyping, semantic HTML, state-machine modeling, visual regression, and human critique.
- **supporting_reason:** These methods observe different concerns and should be combined according to the pending failure class.
- **counterargument_or_limit:** Using every method for every page creates disproportionate process and implementation cost.
- **assumptions_and_boundaries:** Select the least costly complementary bundle capable of falsifying the consequential experience claim.
- **revision_decision:** Add a verification and design-mode tradeoff table beneath the thesis.
- **additional_insight_to_add:** The thesis is method-neutral about visual style but strict about fit, behavior, evidence, and recovery.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Thesis hazards include static-only design, decorative controls, hidden state ownership, responsive patching, token proliferation, generic media, color monoculture, inaccessible motion, and source-only acceptance.
- **supporting_reason:** Each can make the interface look deliberate while leaving real task behavior unstable or incoherent.
- **counterargument_or_limit:** Overlap, asymmetry, expressive type, motion, and unusual composition can be excellent when controlled.
- **assumptions_and_boundaries:** Reject the failure mechanism rather than the style category and require target evidence for exceptions.
- **revision_decision:** Add a false-quality checklist tied to rendered behavior.
- **additional_insight_to_add:** The strongest smell is visual commitment that makes required states harder to represent or operate.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** The seed thesis has no complete path from user evidence to a verified interface decision.
- **supporting_reason:** A good example preserves dense scanning for operators while adding coherent recovery; a bad example replaces work with a generic hero; a borderline concept is visually strong but not state-complete.
- **counterargument_or_limit:** Marketing and game surfaces legitimately use composition and animation that would harm an operational console.
- **assumptions_and_boundaries:** Evaluate examples within their product mode and primary user intent.
- **revision_decision:** Include domain-contrasting examples and promotion gates.
- **additional_insight_to_add:** Executable design does not mean one visual style; it means every style can be rejected when it fails the named experience.

### Question 08: How can the important claims be verified?
- **current_section_observation:** The three seed labels are not paired with a thesis-level acceptance procedure.
- **supporting_reason:** Reviewers can audit each conversion edge, inject missing states and long content, exercise keyboard paths, render viewport variants, and challenge visual rationale.
- **counterargument_or_limit:** A complete audit is expensive for a large design system or application.
- **assumptions_and_boundaries:** Automate structural and behavioral checks, sample semantic/visual fit by consequence, and fully review user-critical flows.
- **revision_decision:** Add an acceptance ladder from evidence audit through actual browser and human review.
- **additional_insight_to_add:** Testing invalidation and recovery reveals more than replaying one ideal screenshot.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** Local source text clearly advocates purpose, constraints, differentiation, and visual cohesion, while broad user-outcome and effectiveness claims remain unmeasured.
- **supporting_reason:** Direct bytes support the design guidance but no target interface study or external refresh supports universal results.
- **counterargument_or_limit:** Established accessibility and systems principles still justify robust defaults without measuring every implementation.
- **assumptions_and_boundaries:** Present the thesis as a reasoned operating model and keep target effects bounded to observed evidence.
- **revision_decision:** Separate source-observed principles, synthesized guidance, and unverified outcomes.
- **additional_insight_to_add:** A strong frontend thesis can be operationally decisive while remaining modest about aesthetic universality.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The seed does not identify the user journey as an intermediate representation consumed by components, content, tests, accessibility, visual tokens, observability, and future agents.
- **supporting_reason:** Stable state and task claims let each consumer specialize without losing the purpose of the interface.
- **counterargument_or_limit:** A formal journey model can freeze premature product decisions.
- **assumptions_and_boundaries:** Preserve open questions, alternatives, experiments, and invalidation alongside accepted states.
- **revision_decision:** Add experience-state graph and selective invalidation deductions.
- **additional_insight_to_add:** A coherent frontend record is both an implementation interface and a context boundary that survives beyond its original designer.

## Section 005: Local Corpus Source Map
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed repeats two paths and two heading signals but does not tell an agent which complete source section answers purpose, direction, aesthetics, or implementation-fit questions.
- **supporting_reason:** Decision routing can save context while preserving the caveats around each local recommendation.
- **counterargument_or_limit:** The source is only 42 lines, so reading it completely is cheaper and safer than elaborate indexing.
- **assumptions_and_boundaries:** Use section routing for explanation and future drift, but require a complete read for a new durable frontend task.
- **revision_decision:** Map each distinct source section to its decision contribution, caution, and target evidence needed next.
- **additional_insight_to_add:** A small corpus map should optimize interpretation and authority, not pretend retrieval itself is expensive.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The seed treats both hash-identical paths as separate retrieval surfaces.
- **supporting_reason:** Read one representative copy in full, preserve both identities, then inspect current target instructions, components, tokens, content, and rendering.
- **counterargument_or_limit:** Archive/package comparisons may require both surrounding directory contexts even when bodies match.
- **assumptions_and_boundaries:** Separate semantic reading from temporal or packaging provenance review.
- **revision_decision:** Publish a representative-read route with a historical-context exception.
- **additional_insight_to_add:** Deduplicating bytes preserves attention while retaining evidence that guidance persisted across two locations.

### Question 03: When does the default work well?
- **current_section_observation:** Complete local reading works for tasks requiring a new page, component, app, or interface direction because the source is short and conceptually coupled.
- **supporting_reason:** Purpose, constraints, differentiation, typography, color, motion, composition, and detail influence one another.
- **counterargument_or_limit:** A narrow existing-product correction may need only the relevant product contract and current rendered defect.
- **assumptions_and_boundaries:** Load the skill when it can change visual reasoning, not as ceremony for every frontend edit.
- **revision_decision:** Add narrow-reuse, standard-design, and historical-review profiles.
- **additional_insight_to_add:** Progressive disclosure is useful only when omitted source content cannot hide a counterconstraint needed by the decision.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The map fails when heading signals become summaries, boldness overrides product mode, or examples such as font avoidance and atmospheric backgrounds become hard policy.
- **supporting_reason:** Local guidance is broad creative advice, while repository brands, performance, glyph coverage, accessibility, and established systems can require exceptions.
- **counterargument_or_limit:** Strong defaults help agents escape generic visual convergence and should not be weakened into vague neutrality.
- **assumptions_and_boundaries:** Preserve intentionality and differentiation while making each technique conditional on target evidence.
- **revision_decision:** Add caveat and route-away fields for every source theme.
- **additional_insight_to_add:** A strong creative default becomes more usable when its compatibility and user-cost boundaries are equally memorable.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** Retrieval alternatives include complete reads, heading search, summaries, copied excerpts, design-system docs, and target browser inspection.
- **supporting_reason:** Complete reads preserve argument, target docs supply current authority, and rendering establishes actual effects.
- **counterargument_or_limit:** Repeated complete reads of unchanged short material can still add noise in highly focused tasks.
- **assumptions_and_boundaries:** Retain a hash and concise decision locator after one complete read, reopening full content when source or question breadth changes.
- **revision_decision:** Add a retrieval method table based on source size, churn, and decision type.
- **additional_insight_to_add:** Context efficiency comes from reading fewer duplicate sources, not from converting nuanced guidance into slogans.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Hazards include duplicate paths, missing license/package context, aggressive typography, trend repetition, motion overload, background decoration, and advice detached from real assets or content.
- **supporting_reason:** These can turn creative direction into compatibility, accessibility, performance, or maintainability defects.
- **counterargument_or_limit:** The source explicitly asks implementation complexity to match aesthetic vision, which discourages shallow copying.
- **assumptions_and_boundaries:** Add target constraints, state matrix, and rendered evidence before promoting any technique.
- **revision_decision:** Put high-risk cautions beside each popular source recommendation.
- **additional_insight_to_add:** Corpus maps should make constraints as retrievable as inspirational phrases, because agents naturally remember the latter.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** The seed provides no example of reading the local sections without copying their aesthetic vocabulary literally.
- **supporting_reason:** Good use derives one coherent direction for a real audience; bad use cycles through listed tones and decorative techniques; borderline use adopts a distinctive font before checking content and loading.
- **counterargument_or_limit:** A concept phase can intentionally exaggerate options to discover a direction.
- **assumptions_and_boundaries:** Exploratory exaggeration remains separate from production acceptance and carries explicit promotion gates.
- **revision_decision:** Add retrieval-to-decision examples for established and greenfield products.
- **additional_insight_to_add:** The source's list is a search space, not a checklist of effects to combine.

### Question 08: How can the important claims be verified?
- **current_section_observation:** The seed map has no identity, complete-read, heading, drift, or target-application verification.
- **supporting_reason:** Existence and hash checks verify the local family, complete reads establish content, and browser/product review tests whether the selected guidance fits.
- **counterargument_or_limit:** Mechanical checks cannot decide whether a visual direction is distinctive or coherent.
- **assumptions_and_boundaries:** Pair source integrity with experienced review and rendered task evidence.
- **revision_decision:** Add map integrity and application-fit checks.
- **additional_insight_to_add:** A source-map pass requires another reviewer to reproduce both the selected guidance and why alternative techniques were rejected.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** Both local files have identical complete content and exact headings, while their role distinction and downstream effectiveness are undocumented.
- **supporting_reason:** Hash and complete-read evidence establish bytes; no history or user study establishes governance rationale or impact.
- **counterargument_or_limit:** The archive/current path relationship plausibly indicates persistence of intended guidance.
- **assumptions_and_boundaries:** State persistence as observed content identity and avoid inferring adoption or success.
- **revision_decision:** Add content-family and role-uncertainty notes.
- **additional_insight_to_add:** A corpus can be complete for available guidance while remaining incomplete for ownership and outcome lineage.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The local source reveals creative heuristics but not the operational guardrails needed for mature products and browser verification.
- **supporting_reason:** The evolved reference must translate memorable aesthetics into preconditions, exceptions, state contracts, and rejection behavior.
- **counterargument_or_limit:** Too much operational framing can dilute the source's useful pressure toward originality.
- **assumptions_and_boundaries:** Keep a strong requirement for intentional product-specific character while rejecting technique mandates.
- **revision_decision:** Add an evolution matrix from source heuristic to bounded operational guidance.
- **additional_insight_to_add:** Mature guidance does not become less creative; it makes creativity survive content, states, accessibility, and maintenance.

## Section 006: External Research Source Map
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed names React, Three.js, and GitHub Actions roots but does not identify the blocked claim, version, required source section, or evidence expected from each.
- **supporting_reason:** Decision-bound research prevents broad documentation links from replacing target code and rendered behavior.
- **counterargument_or_limit:** Exploratory research can reveal capabilities or terminology that a predetermined query misses.
- **assumptions_and_boundaries:** Keep horizon exploration nonaccepting and time-bounded until it changes a named frontend decision.
- **revision_decision:** Add trigger, primary question, applicability, local closure, and stop condition to every external row.
- **additional_insight_to_add:** An external map is actionable when each edge represents an unresolved contract rather than topical similarity.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The seed provides an evidence label without a promotion protocol or local-first exception.
- **supporting_reason:** Inspect the installed stack and target failure first, retrieve the smallest versioned official source only when authorized, then reproduce the claim in the application.
- **counterargument_or_limit:** Official migration guidance may be the right first source when a known framework or browser upgrade caused the mismatch.
- **assumptions_and_boundaries:** External-first is valid when target versions and the observed symptom are already frozen.
- **revision_decision:** Define local-first and known-version-change routes with identical applicability checks.
- **additional_insight_to_add:** Documentation freshness and installed behavior are independent evidence dimensions.

### Question 03: When does the default work well?
- **current_section_observation:** Triggered research fits version-sensitive React semantics, Three.js APIs/rendering, and hosted workflow behavior.
- **supporting_reason:** These producers can change outside the repository and may have primary documentation for selected versions.
- **counterargument_or_limit:** Local wrappers, pinned dependencies, bundlers, browser support, and repository policy can alter applicability.
- **assumptions_and_boundaries:** Record installed package, integration layer, configuration, browser, and runner before transferring guidance.
- **revision_decision:** Add version/configuration fields and wrapper exceptions.
- **additional_insight_to_add:** The more configurable a frontend stack is, the less a documentation root can prove without a target reproduction.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** External research fails when URLs are treated as opened, mutable roots lack dates, or framework examples overrule current product architecture.
- **supporting_reason:** Those errors introduce stale, generic, or incompatible authority into a specific interface.
- **counterargument_or_limit:** Continuously maintained official pages may be the clearest current contract even without immutable version URLs.
- **assumptions_and_boundaries:** Record retrieval date, applicable package/product state, and narrow claims when immutable identity is unavailable.
- **revision_decision:** Add unavailable, version-ambiguous, conflicting, inapplicable, and no-change outcomes.
- **additional_insight_to_add:** A page can be current and authoritative yet irrelevant to the component, renderer, or CI feature actually used.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** Alternatives include package source, installed type declarations, local help, changelogs, migration guides, issue history, browser probes, minimal fixtures, and owner review.
- **supporting_reason:** These sources observe contract, implementation, compatibility, runtime, and policy through different failure modes.
- **counterargument_or_limit:** Gathering all sources increases context and can expose contradictions without a resolver.
- **assumptions_and_boundaries:** Start with the narrowest authoritative mechanism capable of changing the decision and add complementary evidence only for remaining gaps.
- **revision_decision:** Add a source-quality ladder and disagreement handling.
- **additional_insight_to_add:** Research strength comes from complementary observation models, not link count.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Hazards include search snippets, outdated examples, version mismatch, API versus renderer behavior, SSR/client differences, browser extensions, hosted-runner variance, credentials, and broad copied text.
- **supporting_reason:** These defects weaken provenance, compatibility, security, and reproducibility while sounding current.
- **counterargument_or_limit:** Community discussions can surface real edge cases before official documentation does.
- **assumptions_and_boundaries:** Use secondary material as hypothesis input and verify consequential claims through primary and target evidence.
- **revision_decision:** Add source-quality, privacy, and environment cautions.
- **additional_insight_to_add:** Retain a bounded paraphrase and exact locator rather than copying large documentation bodies into another stale artifact.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** The seed does not show how an external source changes a component, scene, or delivery decision.
- **supporting_reason:** Good use retrieves one versioned API after a concrete failure and reproduces it; bad use says a documentation root proves correctness; borderline use surveys renderers before one is selected.
- **counterargument_or_limit:** An early stack survey can be useful architecture evidence without a current target implementation.
- **assumptions_and_boundaries:** Keep survey output as candidate comparison until compatibility, accessibility, performance, and maintenance gates run.
- **revision_decision:** Add decision-bound, misuse, and exploratory examples.
- **additional_insight_to_add:** Research becomes durable only when it changes a requirement, fixture, implementation route, or explicit no-change decision.

### Question 08: How can the important claims be verified?
- **current_section_observation:** The seed's external fact label lacks retrieval identity, supporting span, target version, positive/negative case, and browser or runner evidence.
- **supporting_reason:** Verification requires direct primary access, narrow extraction, installed-version match, controlled reproduction, and target review.
- **counterargument_or_limit:** Hosted runner, GPU/browser, or credential-dependent behavior may be impossible to reproduce locally.
- **assumptions_and_boundaries:** Preserve an unavailable or owner-blocked state rather than simulating evidence.
- **revision_decision:** Add an external result card and blocked-evidence return contract.
- **additional_insight_to_add:** A failed reproduction can be more informative than the documented capability because it exposes packaging or environment differences.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** It is known that the seed retains three URLs and descriptions; current pages, versions, availability, and applicability were intentionally not checked.
- **supporting_reason:** The no-browse constraint limits evidence to locally observed pointer metadata.
- **counterargument_or_limit:** Installed source and browser fixtures may already settle some questions the pointers were intended to answer.
- **assumptions_and_boundaries:** Close an external item through stronger local evidence when it directly answers the bounded claim.
- **revision_decision:** Mark every row `unrefreshed_no_browse` and list current unknowns.
- **additional_insight_to_add:** Choosing not to browse is a positive evidence decision when local target behavior is narrower and directly observable.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The links form three different research lanes: component/runtime semantics, 3D scene behavior, and delivery automation.
- **supporting_reason:** Each lane changes on its own cadence and invalidates different interface claims.
- **counterargument_or_limit:** Event-triggered research can miss ecosystem changes that have not yet produced symptoms.
- **assumptions_and_boundaries:** Allow bounded horizon scans while keeping production guidance tied to claim-specific refresh.
- **revision_decision:** Add ownership, priority, retirement, and invalidation rules to the queue.
- **additional_insight_to_add:** Research remains scalable only when irrelevant or superseded pointers are retired as carefully as new ones are added.

## Section 007: Anti Pattern Registry Table
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed names only context, sourcing, and verification failures, omitting product-fit, state, semantics, responsive, visual-system, asset, motion, and runtime defects.
- **supporting_reason:** A causal registry can identify which experience claims become unsafe and which evidence or implementation may remain valid.
- **counterargument_or_limit:** A long catalog can encourage superficial checklist enforcement and inhibit legitimate design variation.
- **assumptions_and_boundaries:** Prioritize entries by the active user task and consequence; treat style techniques as conditional rather than inherently wrong.
- **revision_decision:** Expand rows with stage, mechanism, signal, user consequence, containment, safer route, and release evidence.
- **additional_insight_to_add:** Frontend anti-patterns are valuable when they change workflow state, not when they merely label taste.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The seed's replacement labels do not define containment or recovery order.
- **supporting_reason:** Stop promotion of affected experience claims, locate the earliest wrong premise, preserve unaffected states, correct the smallest boundary, and replay rendered plus behavioral gates.
- **counterargument_or_limit:** Minor spacing or token inconsistencies can often be corrected directly without a formal failure record.
- **assumptions_and_boundaries:** Scale records with user consequence, recurrence, and shared-component blast radius.
- **revision_decision:** Add a common containment and recovery protocol before the registry.
- **additional_insight_to_add:** Correcting the earliest product or state premise prevents visual refinements from becoming internally consistent with the wrong experience.

### Question 03: When does the default work well?
- **current_section_observation:** Registry-driven prevention works when failures recur across pages, components, viewports, or agent-generated interfaces and expose stable signals.
- **supporting_reason:** Shared causal names and fixtures preserve why visual and interaction gates exist after context loss.
- **counterargument_or_limit:** Novel product-specific usability failures may not fit an existing category.
- **assumptions_and_boundaries:** Preserve an unclassified state and investigate rather than forcing the nearest familiar pattern.
- **revision_decision:** Add admission criteria and an unknown-class route.
- **additional_insight_to_add:** A healthy design registry removes rules that no longer change user outcomes or detection.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The registry fails when judgments are subjective slogans, every deviation is blocked, or mitigations prescribe one visual style.
- **supporting_reason:** That creates false positives, visual sameness, and compliance theater without protecting task behavior.
- **counterargument_or_limit:** Strong defaults and explicit prohibited patterns are useful when repeated evidence shows predictable harm.
- **assumptions_and_boundaries:** Hard-block deterministic behavior/accessibility failures; require contextual review for aesthetic fit.
- **revision_decision:** Separate advisory, visual-review blocking, behavior blocking, and high-assurance stop classes.
- **additional_insight_to_add:** Enforcement strength should track user harm and detection confidence, not how unfashionable a pattern appears.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** Enforcement alternatives include prose guidance, lint/style rules, component constraints, browser fixtures, visual regressions, accessibility tests, design critique, and incident records.
- **supporting_reason:** Automation catches deterministic shape, fixtures observe behavior/pixels, and experienced reviewers judge context and hierarchy.
- **counterargument_or_limit:** Duplicating one rule across design tools, code, tests, and docs creates drift.
- **assumptions_and_boundaries:** Assign one semantic authority per rule and let other systems reference its evidence.
- **revision_decision:** Add enforcement owner and capable mechanism to durable entries.
- **additional_insight_to_add:** Reject a defect at the earliest boundary where its user consequence is observable and correction is cheap.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Missing seed coverage includes marketing composition for apps, card nesting, text controls replacing icons, one-note palettes, decorative effects, hidden states, overflow, unstable dimensions, inaccessible focus, motion overload, broken assets, and blank 3D canvases.
- **supporting_reason:** These failures often survive source review and attractive ideal-state screenshots.
- **counterargument_or_limit:** Cards, text buttons, single-hue systems, overlap, and 3D are valid in the right product and hierarchy.
- **assumptions_and_boundaries:** Define the causal misuse and verification signal rather than banning a medium categorically.
- **revision_decision:** Add cross-cutting product, interaction, layout, visual, media, and evidence entries.
- **additional_insight_to_add:** False visual completion unifies the registry: the page looks finished while a real user state remains unoperable or unobserved.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** The seed provides detection phrases but no full classification and recovery example.
- **supporting_reason:** Good recovery turns a clipped mobile action into a stable layout fixture; bad recovery hides overflow; borderline expressive overlap is retained after content and focus evidence.
- **counterargument_or_limit:** A visually imperfect internal prototype may be safe when clearly nonproduction and used only to learn workflow.
- **assumptions_and_boundaries:** Prototype scope, users, expiry, and promotion gates must be explicit.
- **revision_decision:** Add good, bad, and conditional recovery cases.
- **additional_insight_to_add:** Recovery quality is visible when the unsafe claim is narrowed immediately while useful unaffected behavior continues.

### Question 08: How can the important claims be verified?
- **current_section_observation:** The seed checks labels and gates but does not prove that controls reject wrong product composition, missing state, overlap, focus, or asset failure.
- **supporting_reason:** Negative fixtures, long-content injection, viewport matrices, keyboard paths, failed assets, reduced motion, canvas pixel checks, and review samples can test mechanisms.
- **counterargument_or_limit:** Exercising every failure on every change is expensive and can create brittle visual snapshots.
- **assumptions_and_boundaries:** Run deterministic high-risk controls routinely and sample contextual visual controls by affected surface.
- **revision_decision:** Add anti-pattern acceptance tests and regression ownership.
- **additional_insight_to_add:** An entry is verified when its control rejects the named defect without destroying legitimate design variation.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** Local and active instructions support many failure categories, but occurrence rates and outcome effects are not measured here.
- **supporting_reason:** Source inspection and systems reasoning identify mechanisms without a representative interface corpus or user study.
- **counterargument_or_limit:** Structural impossibility and accessibility policy can justify hard gates without frequency data.
- **assumptions_and_boundaries:** Separate deterministic violations, reasoned risk, observed target defects, and empirical prevalence.
- **revision_decision:** Add evidence basis and prevalence status to the registry.
- **additional_insight_to_add:** Unknown frequency should not weaken a cheap gate against an invisible primary-action or keyboard failure.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The seed treats anti-patterns as end-state descriptions rather than feedback to components, tokens, templates, and verification.
- **supporting_reason:** Repeated causal records reveal which primitive, state fixture, design rule, or browser gate needs redesign.
- **counterargument_or_limit:** Overfitting shared components to rare one-page failures can burden the whole product.
- **assumptions_and_boundaries:** Promote recurring or severe transferable mechanisms and review enforcement cost.
- **revision_decision:** Add feedback, adaptation, and retirement lifecycle.
- **additional_insight_to_add:** A durable frontend anti-pattern should point to a preventive primitive and a replayable failure state.

## Section 008: Verification Gate Command Set
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed supplies one 202606 archive verifier without explaining that it cannot certify this 202607 packet or an actual frontend implementation.
- **supporting_reason:** Reviewers must choose different gates for source identity, artifact shape, behavior, accessibility, rendered pixels, runtime errors, performance, and release evidence.
- **counterargument_or_limit:** One established command is memorable and remains useful for its historical archive target.
- **assumptions_and_boundaries:** Preserve the legacy command with exact scope while making current focused and target-project gates primary.
- **revision_decision:** Replace the one-command implication with a dependency-ordered gate set.
- **additional_insight_to_add:** A frontend command is evidence only for properties its implementation and environment actually observe.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The seed has no order between structural checks, source review, project tests, and rendered inspection.
- **supporting_reason:** Cheap identity and contract checks should precede implementation, project behavior should precede visual polish claims, and browser evidence should precede completion.
- **counterargument_or_limit:** An urgent visual regression may be reproduced in-browser before documentation gates.
- **assumptions_and_boundaries:** Diagnostic reproduction can lead, but final acceptance requires all applicable upstream and downstream evidence.
- **revision_decision:** Order gates as preflight, frozen identity, packet/reference, project source/build, behavior, accessibility, rendering, performance, and handoff.
- **additional_insight_to_add:** Gate order is causal because each state supplies a trusted premise to the next expensive observation.

### Question 03: When does the default work well?
- **current_section_observation:** Layered verification fits repositories with discoverable scripts, component or browser tests, and a runnable local interface.
- **supporting_reason:** Existing commands and fixtures preserve framework configuration and reduce hand-built harness errors.
- **counterargument_or_limit:** Some static HTML or design-only artifacts have no package scripts or test runner.
- **assumptions_and_boundaries:** Use direct browser/manual evidence and lightweight validators when no application server or harness is required.
- **revision_decision:** Add application, static-page, and design-artifact profiles.
- **additional_insight_to_add:** Verification depth follows the claim, not whether a project uses a fashionable test stack.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** Verification fails when commands target the wrong corpus, source-only gates prove pixels, screenshots prove semantics, or broad global failures are ignored without attribution.
- **supporting_reason:** Scope mismatch produces false confidence and false blocking.
- **counterargument_or_limit:** Broad checks can reveal unrelated system regressions that still matter to release.
- **assumptions_and_boundaries:** Report evidence population and classify unrelated failures without modifying another owner's surface.
- **revision_decision:** Add wrong-target, unavailable-command, expected-external-red, and capability-overreach states.
- **additional_insight_to_add:** Gate output should identify target revision, state fixture, viewport/browser, and claim as prominently as pass/fail.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The seed omits lint, typecheck, unit, integration, browser flow, accessibility, screenshot, DOM, canvas pixel, visual review, and performance mechanisms.
- **supporting_reason:** Each observes a different failure class with distinct speed, determinism, maintenance, and semantic reach.
- **counterargument_or_limit:** Running all mechanisms for every styling edit wastes time and increases flaky evidence.
- **assumptions_and_boundaries:** Select the smallest complementary bundle that covers affected behavior, presentation, and consequence.
- **revision_decision:** Add a claim-to-gate matrix and focused-versus-final distinction.
- **additional_insight_to_add:** Gate diversity matters only when mechanisms can disagree in a decision-relevant way.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Command hazards include wrong root, hidden writes, stale snapshots, absent server, wrong port, network dependencies, browser variance, animation nondeterminism, clipped output, and screenshots of the wrong state.
- **supporting_reason:** These defects make visual evidence unreliable or destructive.
- **counterargument_or_limit:** Repository-native scripts often encapsulate environment and browser setup better than ad hoc commands.
- **assumptions_and_boundaries:** Inspect command side effects, server state, fixtures, expected population, and artifact destination before execution.
- **revision_decision:** Add preflight, side-effect, state-identity, and output-capture rules.
- **additional_insight_to_add:** The screenshot/browser harness is part of the design evidence chain and needs its own failure fixtures.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** The seed does not contrast correct use of archive, assignment, and project gates.
- **supporting_reason:** Good use runs focused 202607 checks and target browser states; bad use runs the archive verifier and calls the interface accessible; borderline use accepts manual screenshots for a static page with explicit limitations.
- **counterargument_or_limit:** A legacy verifier can still prove the frozen archive did not drift.
- **assumptions_and_boundaries:** Label historical evidence separately and never transfer it to current target behavior.
- **revision_decision:** Add scoped, mis-scoped, historical, and manual-evidence examples.
- **additional_insight_to_add:** The same command can be useful or irrelevant depending on the claim and target identity attached to it.

### Question 08: How can the important claims be verified?
- **current_section_observation:** The seed provides no test that its gate rejects duplicate packet fields, heading drift, missing states, overflow, blank canvas, focus error, or failed assets.
- **supporting_reason:** Malformed packets and controlled browser fixtures can demonstrate sensitivity across structural and experience failures.
- **counterargument_or_limit:** Visual fault fixtures can be costly and snapshot-heavy.
- **assumptions_and_boundaries:** Exercise deterministic gate mechanics and user-critical visual failures; sample lower-risk aesthetic review.
- **revision_decision:** Add gate-harness verification and expected rejection examples.
- **additional_insight_to_add:** A gate is trustworthy only after a representative wrong state makes it fail for the promised reason.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The legacy verifier target and current shared test mechanics can be inspected locally, while project-specific commands remain unknown until a target repository is analyzed.
- **supporting_reason:** This reference is documentation and contains no universal frontend build stack.
- **counterargument_or_limit:** Common tools can provide illustrative gate families and discovery hints.
- **assumptions_and_boundaries:** Require actual manifest/script discovery before presenting a project command as available or passing.
- **revision_decision:** State known assignment commands and use replaceable target command categories rather than fake exact scripts.
- **additional_insight_to_add:** Verification documentation should preserve both command text and implementation/version identity that gives it meaning.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The seed treats verification as a terminal command rather than a graph spanning design, implementation, rendering, and reuse.
- **supporting_reason:** Source authority supports state contracts, state contracts support tests, implementation supports rendering, and all support handoff.
- **counterargument_or_limit:** Explicit dependency tracking can be excessive for a tiny local correction.
- **assumptions_and_boundaries:** Track claim-critical edges and use concise records for low-risk changes.
- **revision_decision:** Model gates as state transitions with selective invalidation.
- **additional_insight_to_add:** A failed visual gate should reopen only dependent states and surfaces, not erase unrelated verified work or be ignored as cosmetic.

## Section 009: Agent Usage Decision Guide
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed triggers on theme words or nearby technology but does not help an agent choose planning, implementation, review, visual verification, recovery, or route-away state.
- **supporting_reason:** Keyword proximity cannot establish product intent, write authorization, existing design authority, or the next evidence gap.
- **counterargument_or_limit:** Broad triggers improve discoverability and can expose quality constraints before code begins.
- **assumptions_and_boundaries:** Let keywords trigger a fit check, not automatic redesign or mutation.
- **revision_decision:** Replace theme-only triggering with task/phase/evidence-capability guidance.
- **additional_insight_to_add:** Discovering a design reference does not authorize replacing the product's current interface model.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The seed's four bullets omit repository inspection, product category, states, actual implementation, rendered verification, and handoff.
- **supporting_reason:** A reliable agent reads current context, identifies the real task, reuses current systems, specifies states, chooses a direction, implements within scope, and verifies browsers before reporting.
- **counterargument_or_limit:** Mature repositories may already encode most decisions in components, routes, stories, and tests.
- **assumptions_and_boundaries:** Reuse native mechanisms when they preserve behavior, evidence, and visual intent.
- **revision_decision:** Add an end-to-end agent sequence with reuse and route branches.
- **additional_insight_to_add:** The best design action can be a small state repair inside the current system rather than a new page concept.

### Question 03: When does the default work well?
- **current_section_observation:** The seed does not name task shapes beyond frontend-related mention.
- **supporting_reason:** The guide fits building or refining components, pages, apps, dashboards, portals, editors, games, branded surfaces, and visual browser regressions with known goals.
- **counterargument_or_limit:** Product discovery, content decisions, causal debugging, design-system governance, and domain assurance need other primary methods.
- **assumptions_and_boundaries:** Use this reference only for the experience-design and verification portion of compound work.
- **revision_decision:** Add strong-fit, partial-fit, and route-away examples.
- **additional_insight_to_add:** Several specialized methods can operate in sequence when each returns evidence to one user-task record.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The seed lacks stop conditions for unresolved users, content, policy, restricted assets, unavailable browser evidence, or shared ownership.
- **supporting_reason:** Proceeding can invent product behavior, violate rights or privacy, or ship an unverified visual facade.
- **counterargument_or_limit:** A bounded prototype can expose alternatives and gather a decision.
- **assumptions_and_boundaries:** Mark prototype assumptions, prevent production promotion, and isolate it from current owned surfaces.
- **revision_decision:** Add clarification, prototype, partial-progress, blocked, and terminal-route states.
- **additional_insight_to_add:** A high-quality partial result can implement independent known states while preserving one blocked content or policy branch.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The seed does not compare direct correction, design exploration, planning-only, implementation, code review, visual review, design-system work, and specialized asset/3D routes.
- **supporting_reason:** Each mode has different authority, artifacts, speed, and evidence expectations.
- **counterargument_or_limit:** Excessive routing can make a simple interface change feel orchestrated and slow.
- **assumptions_and_boundaries:** Route only when another method can decide or observe a material gap this guide cannot.
- **revision_decision:** Add operating modes and return contracts.
- **additional_insight_to_add:** The route choice should minimize missing information for the next user-visible action, not maximize design ceremony.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Agent hazards include auto-generating a landing page, ignoring current tokens, using invented content, overusing cards and gradients, skipping states, parallel edit collision, source-only completion, and stopping at a mockup.
- **supporting_reason:** These failures confuse creative capability with user request, product authority, and completion evidence.
- **counterargument_or_limit:** Proactive agents should implement a clear request fully rather than ask for needless aesthetic confirmation.
- **assumptions_and_boundaries:** Act decisively after user, task, constraints, write scope, and verification surface are known.
- **revision_decision:** Add autonomy, ownership, asset, and rendered-evidence guardrails.
- **additional_insight_to_add:** Reliable design autonomy is neither timid nor indiscriminate; it follows visible evidence-state transitions.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** The seed gives no examples of selecting or rejecting the guide at agent level.
- **supporting_reason:** Good use builds the requested operational surface; bad use creates a generic hero; borderline use produces an isolated concept while waiting for product direction.
- **counterargument_or_limit:** A brief site request can legitimately mean a branded landing experience when context clearly supports it.
- **assumptions_and_boundaries:** Infer from product/category evidence and existing repository before asking clarification or choosing a mode.
- **revision_decision:** Add phase-aware examples with explicit outputs and stop states.
- **additional_insight_to_add:** Existing repository evidence can answer many apparent design questions without interrupting the user.

### Question 08: How can the important claims be verified?
- **current_section_observation:** The seed does not define how to tell whether using the guide improved the agent's decision or interface.
- **supporting_reason:** Review can compare requested task, mode, changed paths, reused systems, completed states, browser evidence, contradictions, and final user action.
- **counterargument_or_limit:** Success can depend on repository maturity, content quality, or agent expertise rather than the guide.
- **assumptions_and_boundaries:** Report bounded outcomes and do not infer productivity or satisfaction from one task.
- **revision_decision:** Add a usage record and post-task review questions.
- **additional_insight_to_add:** Correct abstention from unsupported redesign is a positive design outcome.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** Local skill intent clearly targets components, pages, applications, and production-grade visual quality; trigger accuracy and outcome utility are not measured.
- **supporting_reason:** Direct source text establishes intended use without a representative task corpus.
- **counterargument_or_limit:** The intended trigger remains useful as a discovery signal.
- **assumptions_and_boundaries:** Treat activation guidance as design intent and verify fit at runtime.
- **revision_decision:** Separate intended activation, observed task evidence, and future calibration.
- **additional_insight_to_add:** Trigger descriptions should evolve from false-positive and false-negative tasks rather than accumulating more frontend keywords.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The seed treats usage as a checklist instead of a state machine whose permitted actions change with product and rendered evidence.
- **supporting_reason:** Oriented, specified, implemented, rendered, verified, blocked, and invalidated states authorize different reads, writes, and claims.
- **counterargument_or_limit:** Formal state labels add overhead to a tiny token or spacing correction.
- **assumptions_and_boundaries:** Keep transitions implicit but evidence visible for narrow work; use full records for durable interfaces.
- **revision_decision:** Add entry evidence, permitted actions, prohibited promotions, and exit states.
- **additional_insight_to_add:** Design autonomy becomes safer when every action is enabled by an observable state and disabled when its premise changes.

## Section 010: User Journey Scenario
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed names a frontend product engineer and broad concerns but does not follow one user task through source evidence, states, visual direction, implementation, rendered verification, and handoff.
- **supporting_reason:** A complete journey can show how product category changes the design and how different quality branches earn independent evidence states.
- **counterargument_or_limit:** One operations scenario cannot represent commerce, editorial, brand, game, or immersive experiences.
- **assumptions_and_boundaries:** Use a shipment-exception console to teach transferable mechanisms, not a universal visual style.
- **revision_decision:** Expand the journey from request through split outcomes and invalidation.
- **additional_insight_to_add:** A realistic frontend journey should let behavior, accessibility, visual polish, and performance reach different states without hiding one another.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The seed moves directly from a named task to component and state choices without examining current workflow or product authority.
- **supporting_reason:** The journey should first inspect operator goals, existing navigation, data density, tokens, components, and actual browser states before selecting a direction.
- **counterargument_or_limit:** A greenfield product may have no current surface and needs prototypes to establish hierarchy.
- **assumptions_and_boundaries:** Prototype alternatives with representative data and promotion criteria, then implement the selected contract.
- **revision_decision:** Add source audit, state decomposition, and product-mode decision before visual styling.
- **additional_insight_to_add:** Early operational-task modeling prevents "modernization" from turning repeated work into marketing composition.

### Question 03: When does the default work well?
- **current_section_observation:** The seed assumes local paths and uncertainty but does not name data, team, or verification preconditions.
- **supporting_reason:** The scenario works when operator tasks, exception statuses, current components, auth/data boundaries, and a runnable browser environment are inspectable.
- **counterargument_or_limit:** Production-only integrations or restricted customer data can prevent realistic end-to-end fixtures.
- **assumptions_and_boundaries:** Use safe representative data and contract fixtures while preserving production no-claim boundaries.
- **revision_decision:** Add data/privacy, environment, and owner preconditions.
- **additional_insight_to_add:** Design evidence must identify which workflow guarantees belong to the local UI and which depend on external services.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The seed does not show what happens when operators disagree about priorities, content is restricted, or performance/accessibility policy is unknown.
- **supporting_reason:** A design cannot legitimately choose operational escalation, retention, or risk policy through visual layout.
- **counterargument_or_limit:** An isolated prototype can make tradeoffs concrete for owners.
- **assumptions_and_boundaries:** Keep policy-dependent actions nonfunctional or safely simulated until approved and never imply production authority.
- **revision_decision:** Add stop, owner, and experiment routes for missing decisions.
- **additional_insight_to_add:** Productive refusal returns the exact blocked branch while independent state and layout work continues.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The seed omits choices between table, list, cards, split pane, separate detail route, command density, responsive collapse, and optimistic actions.
- **supporting_reason:** These alternatives affect scanning, context preservation, touch, keyboard navigation, data visibility, error recovery, and implementation complexity.
- **counterargument_or_limit:** A reference should not choose one architecture without target data and usage frequency.
- **assumptions_and_boundaries:** Present alternatives with evidence needed, then let product and repository context select.
- **revision_decision:** Add a journey tradeoff checkpoint with rejected options.
- **additional_insight_to_add:** Information density is not the opposite of design quality; it is a task-dependent resource that must remain organized.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Scenario hazards include replacing the console with a hero, card-per-row layout, hidden filters, inaccessible row actions, stale selection, narrow overflow, optimistic failure, and fabricated latency targets.
- **supporting_reason:** These failures make a static ideal state attractive while degrading repeated operational work.
- **counterargument_or_limit:** Cards and progressive disclosure can help on touch or low-density consumer surfaces.
- **assumptions_and_boundaries:** Evaluate against operator frequency, comparison needs, supported containers, and actual data lengths.
- **revision_decision:** Include loading, empty, partial, error, stale, permission, action-failure, and responsive branches.
- **additional_insight_to_add:** Dense interfaces need more stable geometry and state discipline, not less visual craft.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** The seed journey has no contrast between a scoped verified result and a superficially complete design.
- **supporting_reason:** Good use delivers keyboard-operable triage states and stable screenshots; bad use ships a static card grid; borderline use has strong pixels but unresolved action recovery.
- **counterargument_or_limit:** An internal pilot can accept narrower browser/device evidence with owner and rollback.
- **assumptions_and_boundaries:** Temporary acceptance needs explicit users, duration, support matrix, monitoring, and promotion restrictions.
- **revision_decision:** Add good, bad, and conditional outcomes.
- **additional_insight_to_add:** Completeness is claim-specific, allowing a layout direction to be accepted while a mutation flow remains blocked.

### Question 08: How can the important claims be verified?
- **current_section_observation:** The seed names visual verification generally but no concrete scenario evidence.
- **supporting_reason:** Filters, selection, bulk actions, detail, loading, empty, errors, keyboard, focus, content extremes, and narrow/wide rendering need complementary fixtures.
- **counterargument_or_limit:** Controlled UI tests cannot establish all production data distributions or operator behavior.
- **assumptions_and_boundaries:** State fixture scope and add production observation only when the release decision requires it.
- **revision_decision:** Include a journey-specific behavior and rendering matrix.
- **additional_insight_to_add:** Verification should check prohibited side effects such as losing selection or applying an action to stale rows, not only visible success.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** Every console name, requirement, component, check, screenshot, and outcome in the expanded journey will be illustrative.
- **supporting_reason:** No target application or operator study is part of this reference evolution.
- **counterargument_or_limit:** A mechanism-grounded example can still assume a data or auth behavior that a real product does not have.
- **assumptions_and_boundaries:** Label all identities/results illustrative and keep external service behavior conditional.
- **revision_decision:** Add a prominent evidence boundary and future replay criteria.
- **additional_insight_to_add:** Detailed illustrative mechanics teach decision structure without manufacturing target observations.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The seed does not show that one user journey forms a graph of shared data, states, controls, layout, semantics, and evidence.
- **supporting_reason:** Filtering, selection, action, detail, recovery, and responsive hierarchy share premises but have different checks and owners.
- **counterargument_or_limit:** Fine-grained graphs can be cumbersome for a simple page.
- **assumptions_and_boundaries:** Use state-level links for consequential workflows and concise records for local display behavior.
- **revision_decision:** End with branch states and shared-premise invalidation.
- **additional_insight_to_add:** Split outcomes let teams deliver verified navigation and scanning while containing exactly the mutation or policy uncertainty that remains.

## Section 011: Decision Tradeoff Guide
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed preserves adopt, adapt, avoid, and cost-of-error postures but reduces choice to agreement between local and external evidence.
- **supporting_reason:** Real frontend decisions also involve product mode, system reuse, state architecture, composition, density, controls, media, motion, responsiveness, and verification.
- **counterargument_or_limit:** A short four-row guide is easier to remember than a multidimensional design matrix.
- **assumptions_and_boundaries:** Keep the four postures as an overview and add claim-specific decisions beneath them.
- **revision_decision:** Expand tradeoffs by user consequence, familiarity, reversibility, implementation cost, and evidence capability.
- **additional_insight_to_add:** One interface can adopt the state model, adapt the visual guidance, and avoid a new design system simultaneously.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The seed recommends adoption on source agreement but does not define frontend sufficiency or correlated blind spots.
- **supporting_reason:** Choose the least costly option that preserves the user task and can be falsified by complementary behavior, semantic, and rendered evidence.
- **counterargument_or_limit:** Estimating hierarchy, familiarity, and aesthetic fit requires judgment and may vary among reviewers.
- **assumptions_and_boundaries:** Make false-positive/negative consequence, reversibility, design authority, and no-claim boundaries explicit.
- **revision_decision:** Put a qualitative sufficiency and escalation rule above the tradeoff tables.
- **additional_insight_to_add:** Cheapest includes future inconsistency, user relearning, asset/runtime cost, and recovery, not only implementation time.

### Question 03: When does the default work well?
- **current_section_observation:** The seed does not identify profiles where incremental tradeoff resolution preserves options.
- **supporting_reason:** It works when an existing product supplies a baseline and stronger evidence is added only for unresolved consequential branches.
- **counterargument_or_limit:** New brands, games, and experimental experiences may need broad visual exploration before constraints converge.
- **assumptions_and_boundaries:** Keep exploration reversible and compare alternatives with real content/states before commitment.
- **revision_decision:** Add focused-correction, standard-product, expressive-experience, and high-assurance profiles.
- **additional_insight_to_add:** Weak early concepts are useful when they remain hypotheses and do not silently become component architecture.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** Tradeoff analysis fails when teams underestimate hidden consumers, use one viewport as universal, or compare methods sharing the same ideal fixture.
- **supporting_reason:** Correlated evidence can agree while missing the same state, browser, accessibility, or content defect.
- **counterargument_or_limit:** Perfect independence is costly and rarely available in frontend work.
- **assumptions_and_boundaries:** Seek materially different observation models proportional to user consequence.
- **revision_decision:** Add shared-blind-spot and unknown-authority checks.
- **additional_insight_to_add:** Agreement increases confidence only when the agreeing mechanisms could have exposed different failures.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The seed omits alternatives across design-system reuse, bespoke system, density, component containers, control semantics, media, motion, responsive strategy, and testing.
- **supporting_reason:** Each option exchanges familiarity, differentiation, task speed, accessibility, implementation, performance, maintenance, and evidence cost.
- **counterargument_or_limit:** Generic matrices can hide framework maturity and product-specific needs.
- **assumptions_and_boundaries:** Use dimensions as prompts and select with target evidence rather than treating rows as universal rankings.
- **revision_decision:** Add product, composition, control, media, motion, responsive, state, and verification tables.
- **additional_insight_to_add:** Bundles should close complementary experience gaps rather than stack several visual artifacts around one assumption.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Hazards include equating spacious with clear, dense with cluttered, bespoke with distinctive, familiar with generic, automated with accessible, and measured with representative.
- **supporting_reason:** Each shortcut ignores product category, user frequency, content, implementation, or evidence boundary.
- **counterargument_or_limit:** These qualities can be useful heuristics when context is stable and explicit.
- **assumptions_and_boundaries:** Require claim fit and a counter-signal instead of rejecting a style or method category.
- **revision_decision:** Add hidden-cost and no-claim columns.
- **additional_insight_to_add:** Detectability and reversibility determine whether a risky visual experiment can be contained safely.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** The seed gives no concrete choice beyond generic adoption language.
- **supporting_reason:** Good use reuses table semantics and improves narrow state; bad use creates a new card system; borderline bespoke media is justified only after subject and fallback evidence.
- **counterargument_or_limit:** A deliberate migration can replace weak current patterns when consumer and owner evidence exists.
- **assumptions_and_boundaries:** Consolidation or divergence needs versioning, migration, rollback, and adoption ownership.
- **revision_decision:** Add reuse, overdesign, and governed-divergence examples.
- **additional_insight_to_add:** The right artifact or component is the one that reduces future task ambiguity without creating competing truth.

### Question 08: How can the important claims be verified?
- **current_section_observation:** The seed's reviewer questions check source appearance but not whether the selected tradeoff improved the bounded experience.
- **supporting_reason:** Pre-action review can name likely misses while post-action user-flow, state, screenshot, accessibility, rework, and reversal evidence tests the route.
- **counterargument_or_limit:** Counterfactual review cannot expose every novel user or content failure.
- **assumptions_and_boundaries:** Combine historical failures, product/domain review, negative fixtures, and post-release evidence when authorized.
- **revision_decision:** Add pre-action and post-action tradeoff audits.
- **additional_insight_to_add:** Route quality improves when each selected mechanism names the plausible user failure it is meant to expose.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** Local sources establish available creative guidance, but no representative study compares design routes, task time, accessibility barriers, maintenance, or satisfaction.
- **supporting_reason:** This assignment reads sources and evolves documentation without target users or implementations.
- **counterargument_or_limit:** Strong qualitative defaults are still defensible for cases such as app versus landing-page form and current-system reuse.
- **assumptions_and_boundaries:** Label comparisons as reasoned defaults and define future target calibration.
- **revision_decision:** Add evidence-basis notes and prohibit unsupported outcome percentages.
- **additional_insight_to_add:** Local tradeoffs can be calibrated through reversals, support incidents, task evidence, and component migration records without universalizing them.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The seed's cost-of-error row does not identify option preservation and invalidation cost as design criteria.
- **supporting_reason:** Early concepts and state contracts should narrow choices without locking unsupported layout, component, or design-system architecture.
- **counterargument_or_limit:** Keeping every option open can create indecision and inconsistent interim UI.
- **assumptions_and_boundaries:** Define selection evidence and deadlines while keeping expensive irreversible branches behind stronger gates.
- **revision_decision:** Add option loss, migration, rollback, and escalation timing.
- **additional_insight_to_add:** The best early design move often maximizes informative next choices rather than immediate visual completeness.

## Section 012: Local Corpus Hierarchy
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed labels one hash-equal path canonical and one supporting but does not distinguish authority for historical content, creative guidance, product intent, design system, implementation, rendering, measurement, or risk.
- **supporting_reason:** Frontend authority is claim-specific, so a source can govern its own text while browser and product evidence govern different questions.
- **counterargument_or_limit:** A single total order is simpler and may reduce source debate.
- **assumptions_and_boundaries:** Offer a default retrieval route while prohibiting global prestige ranking.
- **revision_decision:** Replace implicit hierarchy with a claim-to-authority matrix and preserve seed role metadata.
- **additional_insight_to_add:** Canonicality should name the question it settles rather than travel with a file into every decision.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The archive is marked canonical even though its current counterpart has identical bytes and target product evidence is absent from the seed.
- **supporting_reason:** Use exact archive bytes for historical claims, current local skill for available guidance, repository/design authority for conventions, and browser evidence for actual experience.
- **counterargument_or_limit:** Current design systems and implementation can be stale, inaccessible, or wrong.
- **assumptions_and_boundaries:** Every source remains subject to identity, scope, conflict, applicability, and owner checks.
- **revision_decision:** Add typed precedence and explicit disagreement handling.
- **additional_insight_to_add:** The source that begins orientation can be weaker than the source that settles release.

### Question 03: When does the default work well?
- **current_section_observation:** Typed hierarchy is useful for long handoffs, redesigns, design-system changes, visual regressions, and source evolution.
- **supporting_reason:** It prevents duplicate bytes from multiplying confidence and supports targeted invalidation when one layer changes.
- **counterargument_or_limit:** A one-off local spacing correction may not justify a formal ledger.
- **assumptions_and_boundaries:** Use concise roles for reversible work and durable matrices for user-critical or shared changes.
- **revision_decision:** Add lightweight and durable hierarchy profiles.
- **additional_insight_to_add:** Typed authority lets a changed visual token reopen pixels without invalidating unrelated product intent.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** Hierarchy fails when canonical labels prove quality, newest wins automatically, code is treated as design intent, screenshots are treated as full behavior, or duplicate paths vote.
- **supporting_reason:** Metadata, recency, implementation, and pixels each answer narrower questions.
- **counterargument_or_limit:** Recency and executable behavior are useful heuristics when stronger authority is unavailable.
- **assumptions_and_boundaries:** Use heuristics only under explicit scope and uncertainty.
- **revision_decision:** Add duplicate, conflicting, historical, current, unknown-authority, and superseded-for-purpose states.
- **additional_insight_to_add:** An unresolved source conflict can be the evidence that should block a redesign.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** Alternatives include archive canon, newest-wins, design-file supremacy, code supremacy, owner decree, majority review, and provenance graph without one master source.
- **supporting_reason:** Each is effective for one claim class and dangerous when generalized.
- **counterargument_or_limit:** Full provenance graphs can overwhelm agents who need a starting point.
- **assumptions_and_boundaries:** Use a compact retrieval sequence backed by typed conflict and invalidation records.
- **revision_decision:** Combine starting order with a partial-order authority model.
- **additional_insight_to_add:** Reading convenience and decision authority should occupy different fields.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Hazards include unexplained canonical labels, identical content under different roles, machine-local paths, absent design history, screenshots as intent, examples as policy, and public pointers as current fact.
- **supporting_reason:** These make sources appear more independent, portable, binding, or complete than they are.
- **counterargument_or_limit:** Recording every contextual dimension burdens concise user-facing answers.
- **assumptions_and_boundaries:** Keep complete provenance durable and expose only claim-relevant authority in communication.
- **revision_decision:** Add identity, temporal scope, availability, role rationale, and applicability fields.
- **additional_insight_to_add:** An inaccessible source can remain historically authoritative while being insufficient for reproducible current work.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** The seed repeats one reviewer question for both paths and does not show claim-specific authority.
- **supporting_reason:** Good use cites archive bytes for history, current skill for guidance, design owner for direction, code/browser for behavior; bad use calls two files two studies.
- **counterargument_or_limit:** A concise summary can cite one representative path if durable duplicate metadata remains available.
- **assumptions_and_boundaries:** Preserve all required identities even when one supplies semantic content.
- **revision_decision:** Add historical, current-guidance, product, implementation, rendering, and measurement examples.
- **additional_insight_to_add:** Representative citation and complete provenance coexist when content and identity are separated.

### Question 08: How can the important claims be verified?
- **current_section_observation:** The seed has no hierarchy audit beyond role labels and heading signals.
- **supporting_reason:** Complete reads, hashes, package/path context, product ownership, source tests, browser states, and conflict records verify distinct dimensions.
- **counterargument_or_limit:** Hashes cannot explain why a role was assigned or whether guidance is good.
- **assumptions_and_boundaries:** Use metadata for routing and verify substantive claims through their capable authority.
- **revision_decision:** Add a hierarchy audit and disagreement protocol.
- **additional_insight_to_add:** A conflict resolves only when scope or stronger evidence explains divergence, not when one artifact is silently discarded.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The two seed paths have identical bodies, but no mapped note explains why the archive is canonical and current path is supporting.
- **supporting_reason:** Hash identity is observed directly while role rationale is absent.
- **counterargument_or_limit:** The roles may reflect corpus-generation policy outside the files.
- **assumptions_and_boundaries:** Preserve labels as historical metadata and quarantine unexplained rationale from technical conclusions.
- **revision_decision:** Add an uncertainty note beside seed roles.
- **additional_insight_to_add:** Unexplained metadata is evidence about corpus governance, not automatic evidence about design quality.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The hierarchy forms a versioned chain from product intent and guidance to state contract, visual system, code, browser outcome, owner acceptance, and feedback.
- **supporting_reason:** Upstream evidence constrains design while downstream observation can refute implementation and motivate later guidance.
- **counterargument_or_limit:** Feedback makes the chain cyclic and can blur historical versus current roles.
- **assumptions_and_boundaries:** Treat every feedback revision as a new trajectory instead of strengthening older evidence retroactively.
- **revision_decision:** Add causal edges and targeted invalidation.
- **additional_insight_to_add:** Versioned partial orders preserve learning while keeping prior design decisions interpretable under their original sources.

## Section 013: Theme Specific Artifact
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed requests a quality-bar rubric with three generic fields but does not connect product intent, states, visual direction, implementation, browser evidence, blockers, and release.
- **supporting_reason:** A concrete evidence packet lets another reviewer reconstruct why the interface is usable and which unverified branch still blocks promotion.
- **counterargument_or_limit:** A comprehensive packet can duplicate issue trackers, design files, component stories, tests, and review systems.
- **assumptions_and_boundaries:** Link existing authorities by stable identity and keep one mutable decision owner instead of copying bodies.
- **revision_decision:** Define a `Frontend Experience Evidence Packet` with profile-conditional blocks and a quality-bar view.
- **additional_insight_to_add:** The artifact's value is the graph among user task, states, design decisions, checks, and release actions, not another prose summary.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The seed does not define packet scope, identity, ownership, or state lifecycle.
- **supporting_reason:** One packet per bounded user journey and target revision keeps product, visual, behavior, and evidence branches coherent.
- **counterargument_or_limit:** Related surfaces may share tokens, components, data, and fixtures across several journeys.
- **assumptions_and_boundaries:** Share stable evidence IDs and system contracts while preserving claim/state-specific ownership and sufficiency.
- **revision_decision:** Add stable packet/journey/state IDs and split-outcome cards.
- **additional_insight_to_add:** Claim-local state prevents a polished happy path from laundering confidence into unresolved accessibility or recovery branches.

### Question 03: When does the default work well?
- **current_section_observation:** The seed does not identify artifact profiles or expected lifespan.
- **supporting_reason:** The packet helps new workflows, shared components, design-system changes, multi-agent implementation, release review, and recurring visual regressions.
- **counterargument_or_limit:** A tiny token correction with an authoritative component and screenshot can use a concise record.
- **assumptions_and_boundaries:** Scale depth by user consequence, shared consumers, novelty, handoffs, and reuse.
- **revision_decision:** Define focused correction, standard experience, and high-assurance profiles.
- **additional_insight_to_add:** The packet is most valuable where screenshots alone would lose state semantics and design rationale.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The artifact fails when completed after the fact as ceremony, used to make aesthetic preference look approved, or allowed to drift from code and browser states.
- **supporting_reason:** Structured fields can magnify trust in stale or unsupported evidence.
- **counterargument_or_limit:** Retrospective reconstruction can still expose assumptions and recover a broken handoff.
- **assumptions_and_boundaries:** Mark reconstructed/unknown fields and replay gates before current acceptance.
- **revision_decision:** Add anti-values, reconstruction state, and freshness rules.
- **additional_insight_to_add:** Honest incompleteness is essential because formal structure raises both usefulness and overconfidence risk.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** Alternatives include Markdown packets, issue fields, design specs, component stories, test metadata, screenshot manifests, CI artifacts, and structured schemas.
- **supporting_reason:** Each serves different human, machine, ownership, visual, and execution needs.
- **counterargument_or_limit:** Synchronizing several representations creates drift and unclear authority.
- **assumptions_and_boundaries:** Designate one decision authority and derive/link execution or visual views by immutable identity.
- **revision_decision:** Recommend human-readable packet with optional machine validation and external evidence links.
- **additional_insight_to_add:** Representation should follow the primary consumer while stable IDs bridge design, code, browser, and review systems.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Artifact hazards include screenshot dumps, vague user goals, missing states, orphan checks, unowned visual direction, copied budgets, hidden viewports, inaccessible assets, empty next action, and stale approval.
- **supporting_reason:** These defects make the artifact expensive yet unable to falsify or recover the experience.
- **counterargument_or_limit:** Some conditional fields genuinely do not apply to a static or narrow surface.
- **assumptions_and_boundaries:** Require an evidence-based not-applicable reason rather than silent omission.
- **revision_decision:** Add completion rules, prohibited values, and profile applicability.
- **additional_insight_to_add:** Invalidation is as important as original proof because content, state, tokens, and browsers drift frequently.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** The seed does not contrast complete and misleading quality-bar artifacts.
- **supporting_reason:** Good packet links state behavior to browser/accessibility evidence; bad packet pastes ideal screenshots; recoverable packet has current rendering but uncertain product intent.
- **counterargument_or_limit:** Screenshots and traces are valuable when tied to exact state, configuration, and claims.
- **assumptions_and_boundaries:** Evaluate whether another reviewer can reproduce, challenge, update, and invalidate the decision.
- **revision_decision:** Add good, bad, and recoverable packet examples.
- **additional_insight_to_add:** Missing authority can downgrade a packet to visual regression evidence without discarding its current pixel observations.

### Question 08: How can the important claims be verified?
- **current_section_observation:** The seed's three fields have no schema, state coverage, traceability, freshness, or acceptance test.
- **supporting_reason:** Verify shape, source identities, state/check links, browser matrix, accessibility/input evidence, blockers, screenshots, owner scope, and invalidation.
- **counterargument_or_limit:** A structurally complete packet can still encode a poor workflow or weak visual judgment.
- **assumptions_and_boundaries:** Automation enforces deterministic integrity while product/design/accessibility review assesses meaning and fit.
- **revision_decision:** Add acceptance and negative checklists.
- **additional_insight_to_add:** Verification must run both directions so every material state has evidence and every retained artifact names the claim it affects.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** Local guidance and systems constraints support the proposed fields, but no source defines this exact packet or measures its cost and outcome value.
- **supporting_reason:** The schema is synthesized from current evidence and recurring frontend failure modes.
- **counterargument_or_limit:** Direct derivation from practical source, browser, and handoff needs gives it a defensible basis.
- **assumptions_and_boundaries:** Present it as a recommended local default to calibrate, not an external standard.
- **revision_decision:** Label design rationale, unmeasured status, and future feedback metrics.
- **additional_insight_to_add:** Schema evolution should respond to reconstruction, defect, and release failures rather than fields added for appearance.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The three-field seed does not reveal that the artifact can function as a provenance, state, and invalidation graph.
- **supporting_reason:** Sources and owners define claims; claims define states and components; checks/rendering test them; changes reopen dependent evidence.
- **counterargument_or_limit:** Fine-grained edge maintenance can cost more than a low-impact change.
- **assumptions_and_boundaries:** Use claim/state-level edges for durable or consequential work and reduced profiles for corrections.
- **revision_decision:** Add dependency IDs and selective rollback across packet blocks.
- **additional_insight_to_add:** Linked premises let review focus on the smallest changed experience cut rather than replaying the whole product.

## Section 014: Worked Example Set
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed gives one sentence each for good, bad, and borderline use but does not show how evidence changes frontend form, controls, states, assets, or verification.
- **supporting_reason:** Orthogonal examples can teach when to preserve operational density, transform responsive composition, use familiar controls, foreground subject media, recover errors, or verify 3D.
- **counterargument_or_limit:** Too many examples can invite literal copying across unrelated products.
- **assumptions_and_boundaries:** Keep examples mechanism-focused, illustrative, and paired with transferable rules.
- **revision_decision:** Add six scenarios with decision, authority, contract, evidence, missing scope, overclaim, invalidation, and replay.
- **additional_insight_to_add:** Counterexamples teach design quality by revealing where visual confidence must stop or change route.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The seed examples have no shared structure, making comparison and promotion difficult.
- **supporting_reason:** Every example should identify user task, product mode, current authority, material state, visual decision, capable checks, no-claim boundary, and invalidation.
- **counterargument_or_limit:** A short before/after image can communicate one visual defect faster than a full evidence narrative.
- **assumptions_and_boundaries:** Use images/snippets as evidence inside the shared decision frame, not as the complete argument.
- **revision_decision:** Standardize examples on an experience-evidence frame with flexible presentation.
- **additional_insight_to_add:** Comparable fields reveal why different product modes legitimately require different visual and verification methods.

### Question 03: When does the default work well?
- **current_section_observation:** Detailed examples are valuable for onboarding, code/design review, prompt/tool guidance, component governance, and regression retrospectives.
- **supporting_reason:** They preserve both mechanism and rationale for future replay after the interface changes.
- **counterargument_or_limit:** Experienced teams may need only a terse failure rule for established recurring defects.
- **assumptions_and_boundaries:** Add a concise transferable rule to each complete example.
- **revision_decision:** End each scenario with replay and reusable principle.
- **additional_insight_to_add:** An example becomes organizational memory when it states the unsafe inference its future fixture prevents.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** Examples fail when illustrative screenshots appear observed, one architecture becomes universal, or one fixture is generalized to all users and browsers.
- **supporting_reason:** Realistic names and states can make pedagogy sound like target evidence.
- **counterargument_or_limit:** Concrete content and dimensions are often needed to reveal responsive and visual mechanisms.
- **assumptions_and_boundaries:** Label all identities/results illustrative and retain no-generalization boundaries.
- **revision_decision:** Add evidence status and target promotion requirements.
- **additional_insight_to_add:** Causal precision is more credible than realism theater; a good example explains what the check distinguishes.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** Example forms include narrative journeys, state tables, component contracts, before/after screenshots, geometry checks, accessibility trees, and executable fixtures.
- **supporting_reason:** Different forms expose route changes, syntax, links, pixels, semantics, and behavior efficiently.
- **counterargument_or_limit:** Combining every format in every scenario creates repetition.
- **assumptions_and_boundaries:** Select the minimum format that exposes the unique failure mechanism.
- **revision_decision:** Mix compact tables, prose, and future fixture criteria under one evidence frame.
- **additional_insight_to_add:** Format diversity is helpful only when claim state and conclusion boundaries remain comparable.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Hazards include side-effecting commands, fake file paths, source-coupled oracles, ideal copy, omitted states, unsupported performance, and examples that never demonstrate refusal.
- **supporting_reason:** Readers may execute or generalize examples literally, converting simplification into risk.
- **counterargument_or_limit:** Excessive caveats can obscure the central lesson.
- **assumptions_and_boundaries:** Place each warning next to the constrained step and avoid unnecessary exact commands or numbers.
- **revision_decision:** Include stop, downgrade, fallback, and route outcomes as normal examples.
- **additional_insight_to_add:** A safe frontend example demonstrates declining an attractive but wrong product form, not only producing visual success.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** The seed classifications do not show lifecycle promotion or changed use.
- **supporting_reason:** Good examples match evidence to task, bad examples promote appearance into truth, and borderline examples remain safe only for narrower decisions.
- **counterargument_or_limit:** New source, browser, product, or owner evidence can change classification.
- **assumptions_and_boundaries:** Include promotion, downgrade, and invalidation triggers.
- **revision_decision:** Add lifecycle transitions to the synthesis table.
- **additional_insight_to_add:** The same screenshot can be safe for visual discussion and unsafe for accessibility or release approval.

### Question 08: How can the important claims be verified?
- **current_section_observation:** The seed examples have no replay or negative assertion.
- **supporting_reason:** Fixtures can inject app/hero mismatch, long content, focus loss, asset failure, reduced motion, blank canvas, and failed mutations.
- **counterargument_or_limit:** This assignment cannot build target fixtures outside its authorized files.
- **assumptions_and_boundaries:** Specify future replay inputs and expected state transitions without claiming execution.
- **revision_decision:** Add a replay check and fixture-promotion rule to every example.
- **additional_insight_to_add:** The strongest example test proves when the agent stops, reroutes, or narrows, not only when ideal rendering passes.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** Example mechanisms follow local and active frontend guidance, but every repository, route, asset, browser result, and screenshot is illustrative.
- **supporting_reason:** No target implementation is authorized within this reference evolution.
- **counterargument_or_limit:** Mechanism-grounded examples can still omit domain-specific content, browser, or interaction constraints.
- **assumptions_and_boundaries:** Keep examples stack-neutral where possible and route target details to real evidence.
- **revision_decision:** Add known-mechanism versus illustrative-target notes.
- **additional_insight_to_add:** Separating mechanism from observation permits useful specificity without manufacturing proof.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The seed does not connect examples to reusable components, regression states, and evolving quality gates.
- **supporting_reason:** Each scenario names a failure class, unsafe inference, and capable repair that can become a fixture after recurrence.
- **counterargument_or_limit:** Turning every example into permanent code bloats test and story suites.
- **assumptions_and_boundaries:** Promote only recurring, deterministic, consequential mechanisms with ownership and retirement criteria.
- **revision_decision:** Add fixture admission and retirement guidance.
- **additional_insight_to_add:** The best examples seed durable gates because they preserve why the check exists and what false completion it prevents.

## Section 015: Outcome Metrics and Feedback Loops
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed names a leading indicator, failure signal, and cadence but gives no denominator, cohort, sampling, evidence source, or action rule.
- **supporting_reason:** Teams need to decide whether the reference improves user task, state resilience, accessibility, responsive fit, visual coherence, and maintenance or merely produces more screenshots and tokens.
- **counterargument_or_limit:** Measurement can cost more than a narrow frontend change and incentivize superficial numbers.
- **assumptions_and_boundaries:** Measure recurring or consequential work and tie each metric to a decision it can change.
- **revision_decision:** Define deterministic integrity, sampled experience quality, workflow, performance, and downstream outcome metrics.
- **additional_insight_to_add:** Metrics should localize which experience conversion failed rather than compressing the interface into one score.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The seed implies workflow completion without defining user, task, state, success, or regression population.
- **supporting_reason:** Establish local baselines under stable definitions, report raw counts, pair speed/visual volume with task/accessibility/error counter-metrics, and preserve no-comparison states.
- **counterargument_or_limit:** Local baselines can normalize poor design if no independent user or domain authority challenges them.
- **assumptions_and_boundaries:** Audit against product outcomes, negative states, accessibility evidence, and experienced external review as consequence requires.
- **revision_decision:** Add calibration, comparability, and audit rules without universal thresholds.
- **additional_insight_to_add:** Baseline change indicates direction, not adequacy for every user or risk.

### Question 03: When does the default work well?
- **current_section_observation:** Metrics are useful for repeated design-system/component work, high-frequency journeys, template changes, multi-agent handoffs, and recurring responsive/accessibility defects.
- **supporting_reason:** Comparable fixtures and retained state/render evidence provide denominators and reveal tradeoffs between speed and quality.
- **counterargument_or_limit:** One-off expressive pages and rapidly changing prototypes may not yield stable cohorts.
- **assumptions_and_boundaries:** Use qualitative critique, controlled fixtures, and sentinel events when aggregate rates would mislead.
- **revision_decision:** Add sparse-data and sentinel modes.
- **additional_insight_to_add:** Controlled state fixtures and real user outcomes answer different questions and must remain separate cohorts.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** Metrics fail when teams optimize component count, screenshot count, automated scores, short task time, low unresolved count, or visual novelty without outcome checks.
- **supporting_reason:** These values can improve through fragmentation, skipped states, forced decisions, or inaccessible shortcuts.
- **counterargument_or_limit:** Balanced metrics and review reduce but cannot eliminate gaming or confounding.
- **assumptions_and_boundaries:** Pair every gameable measure with errors, reversals, accessibility barriers, maintenance, or user-task counterevidence.
- **revision_decision:** Add misuse warnings and counter-metrics.
- **additional_insight_to_add:** A metric is dangerous when its easiest improvement bypasses the user state it was meant to protect.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** Alternatives include deterministic schema/geometry gates, state coverage, accessibility audits, visual critique, usability tasks, browser performance, support incidents, rework, and production telemetry.
- **supporting_reason:** Each differs in latency, cost, representativeness, and failure sensitivity.
- **counterargument_or_limit:** A full measurement program can become larger than the interface work.
- **assumptions_and_boundaries:** Select methods according to the design change and failure class under evaluation.
- **revision_decision:** Add metric selection by evidence strength and feedback latency.
- **additional_insight_to_add:** Leading signals should trigger investigation while lagging outcomes test whether they predict safer experiences.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Hazards include denominator drift, ideal fixtures, excluded blocked states, changing browsers/reviewers, mixed product modes, missing disabled users, survivorship bias, unrecorded reversals, and copied performance values.
- **supporting_reason:** These defects make hard users and failure states vanish from the reported population.
- **counterargument_or_limit:** Perfectly controlled experience data is rarely available in ordinary delivery.
- **assumptions_and_boundaries:** Retain cohort identity, missing data, dissent, and uncertainty; refuse comparisons after material definition change.
- **revision_decision:** Add comparability metadata and missing-data states.
- **additional_insight_to_add:** Incomparability can reveal evidence drift and is more honest than a smooth but meaningless trend.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** The seed offers no interpretation examples for its indicator or failure signal.
- **supporting_reason:** Good reports tie state recovery and responsive fit to the same cohort; bad reports celebrate more screenshots; sentinel reports preserve one severe inaccessible action.
- **counterargument_or_limit:** One severe defect can justify a blocker without a stable rate.
- **assumptions_and_boundaries:** Report sentinel mechanisms separately from percentages and retain causal evidence.
- **revision_decision:** Add good, bad, and sentinel interpretations.
- **additional_insight_to_add:** A single high-consequence counterexample can define a safety boundary while aggregate trends guide refinement inside it.

### Question 08: How can the important claims be verified?
- **current_section_observation:** The seed provides no metric audit, replay, or recalculation contract.
- **supporting_reason:** Freeze definitions, reproduce queries, audit state/browser/user sampling, inspect raw artifacts, replay fixtures, and compare independent downstream evidence.
- **counterargument_or_limit:** Reviewers and users can share product assumptions and miss the same issue.
- **assumptions_and_boundaries:** Include dissent, negative states, accessibility/domain review, and counterexamples for material claims.
- **revision_decision:** Add metric cards and consequence-based audit triggers.
- **additional_insight_to_add:** Frontend metrics need invalidation because component, content, fixture, browser, and product changes alter meaning quickly.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** Packet counts, state matrices, screenshot identities, geometry failures, and command outcomes are measurable, but no local dataset establishes user success, satisfaction, productivity, or defect prevention.
- **supporting_reason:** This evolution generated no target implementation or longitudinal user cohort.
- **counterargument_or_limit:** Deterministic properties such as missing accessible names or clipped text can have hard pass rules under defined populations.
- **assumptions_and_boundaries:** Keep deterministic interface invariants separate from empirical experience effects.
- **revision_decision:** Mark all proposed outcome indicators as future capture definitions.
- **additional_insight_to_add:** Guaranteed artifact shape and estimated user value are different evidence types and should never be averaged.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The seed suggests rerunning verification but not changing components, patterns, routing, or visual defaults based on outcomes.
- **supporting_reason:** Recurring misses can show a primitive needs a state, a visual gate needs long content, or a claim class needs domain/user evidence.
- **counterargument_or_limit:** Frequent process/system changes destabilize products and destroy comparability.
- **assumptions_and_boundaries:** Version changes, retain old cohorts, and require evidence that a new control addresses a verified mechanism.
- **revision_decision:** Add feedback actions of fix, adapt, reroute, retire, or collect stronger evidence.
- **additional_insight_to_add:** The highest-value metric can reveal that a visual pattern should stop earlier and hand a question to product or accessibility authority.

## Section 016: Completeness Checklist
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed checks whether seven topics exist but not whether a user journey, state, interface, render, or handoff is complete enough for its consequence.
- **supporting_reason:** Heading and example presence cannot establish product authority, state coverage, semantics, layout, accessibility, browser behavior, or recovery.
- **counterargument_or_limit:** Structural checks quickly catch omitted required reference content.
- **assumptions_and_boundaries:** Preserve seed construction requirements and add evidence-backed experience gates.
- **revision_decision:** Organize checks into reference, fit, source, journey/state, semantics, composition/visual, implementation, rendering, measurement, and lifecycle blocks.
- **additional_insight_to_add:** Completeness is profile-relative, so a token correction and a critical workflow share principles but not evidence depth.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The seed offers binary bullets without evidence type, severity, owner, or not-applicable reason.
- **supporting_reason:** Every completion item should link to observation; conditional omission should state why; critical failure should block dependent claims.
- **counterargument_or_limit:** Detailed evidence can burden a reversible local correction.
- **assumptions_and_boundaries:** Use the focused profile while preserving target/state/render identity and invalidation.
- **revision_decision:** Add profile, evidence class, severity, failure response, and reopening semantics.
- **additional_insight_to_add:** A checklist becomes operational when failure changes what the agent may claim or release.

### Question 03: When does the default work well?
- **current_section_observation:** Evidence-backed phase gates fit shared-agent work, new workflows, shared components, redesigns, release review, and recurring state maintenance.
- **supporting_reason:** They create durable trust boundaries and show which evidence can be reused after change.
- **counterargument_or_limit:** Rigid one-way sequencing can slow exploratory design where later renders alter earlier assumptions.
- **assumptions_and_boundaries:** Permit backtracking and contradiction while requiring gates before promotion.
- **revision_decision:** Model checklist blocks as revisitable state transitions.
- **additional_insight_to_add:** Reopening visual direction after real content fails is healthy evidence flow, not process failure.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The checklist fails when copied across product modes, completed from memory, or used to make one screenshot or scanner decide the whole experience.
- **supporting_reason:** Formal completion cannot make pixels prove semantics or make a visual review choose product policy.
- **counterargument_or_limit:** A strong task-fit item can reject unsuitable evidence early.
- **assumptions_and_boundaries:** Allow route-away, unresolved, and not-applicable outcomes with reasons.
- **revision_decision:** Add fit, skip, escalation, and owner-acceptance states.
- **additional_insight_to_add:** A checklist can be complete because it handed a claim to a more capable owner, not only because it approved release.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** Alternatives include parsers, typed schemas, lint/CI, component stories, browser automation, accessibility review, design critique, domain approval, and free-form narrative.
- **supporting_reason:** Automation catches structure, browsers observe behavior/pixels, reviewers judge fit, and owners accept policy.
- **counterargument_or_limit:** Duplicated checks across systems can drift and report conflicting status.
- **assumptions_and_boundaries:** Assign one semantic authority and stable evidence identity to each decision.
- **revision_decision:** Separate machine, semantic/design, project behavior, rendered, and owner acceptance statuses.
- **additional_insight_to_add:** Each item should route to the mechanism best able to reject it instead of pretending every quality claim is automatable.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Hazards include silent nonapplicability, stale screenshots, check existence without oracle review, ideal content, hidden browser/state gaps, copied numbers, missing owner, and empty next action.
- **supporting_reason:** These preserve visual completion while removing reproduction, falsification, and recovery.
- **counterargument_or_limit:** Raw browser evidence may be sensitive or too large to retain directly.
- **assumptions_and_boundaries:** Store secure locators, identity, bounded observation, and reproduction route under policy.
- **revision_decision:** Add freshness, privacy, content/state identity, and nonempty-lifecycle gates.
- **additional_insight_to_add:** Invalidation is one of the strongest completeness controls for rapidly changing content and interfaces.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** The seed has no contrast between document, screenshot, behavior, and decision completeness.
- **supporting_reason:** Good checklist blocks speed while allowing verified states; bad checklist marks sections present; focused reuse can pass reduced gates for one rendered correction.
- **counterargument_or_limit:** Later promotion can legitimately reuse current focused evidence.
- **assumptions_and_boundaries:** Promotion must run every missing user/state/browser/owner gate rather than inherit the lower profile silently.
- **revision_decision:** Add good, bad, and recoverable completion examples.
- **additional_insight_to_add:** Focused completeness becomes unsafe only when its output is reused for a stronger claim without reevaluation.

### Question 08: How can the important claims be verified?
- **current_section_observation:** The seed provides no negative test for checklist controls.
- **supporting_reason:** Remove product authority, state fixture, accessible name, viewport render, owner, or source hash and verify dependent promotion stops.
- **counterargument_or_limit:** Simulating every critical frontend failure is expensive and sometimes platform-specific.
- **assumptions_and_boundaries:** Test deterministic controls routinely and replay high-consequence blockers after policy/harness changes.
- **revision_decision:** Add rejection fixtures and risk-based semantic review.
- **additional_insight_to_add:** Refusal paths deserve the same design attention as successful checklist paths.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** Heading, packet, source, state-ID, link, manifest, geometry, and hygiene completeness can be checked, while desired workflow and visual sufficiency require judgment.
- **supporting_reason:** Parsers and browser geometry cannot universally decide trust, hierarchy, or product meaning.
- **counterargument_or_limit:** Product policies can encode stronger deterministic floors for repeated interfaces.
- **assumptions_and_boundaries:** Distinguish automated, semantic/design reviewer, rendered behavior, and authorized owner status.
- **revision_decision:** Add evidence type and owner to each gate.
- **additional_insight_to_add:** Separate statuses prevent machine-Green or attractive pixels from masquerading as accepted experience.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The seed list does not expose prerequisites among product authority, state, semantics, composition, implementation, browser evidence, and acceptance.
- **supporting_reason:** An upstream mismatch invalidates downstream screenshots and tests even when their artifacts still exist.
- **counterargument_or_limit:** Explicit dependency tracking adds complexity to small tasks.
- **assumptions_and_boundaries:** Encode only claim-critical edges and use selective invalidation.
- **revision_decision:** Add prerequisite and reopen rules to each block.
- **additional_insight_to_add:** Completeness should propagate forward from valid premises and backward when real rendering contradicts an earlier assumption.

## Section 017: Adjacent Reference Routing
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed mentions React, Three.js, design, and quality neighbors but does not identify which missing authority or observation each route supplies.
- **supporting_reason:** Frontend work may need product intent, code behavior, framework idioms, accessibility, media, 3D, performance, security, operations, or release evidence beyond this reference.
- **counterargument_or_limit:** Topic-level links are easy to scan and can inspire useful discovery.
- **assumptions_and_boundaries:** Allow bounded discovery, then require one claim, consequence, expected evidence, and return state.
- **revision_decision:** Build a capability-gap router with entry, return, complementary, and terminal routes.
- **additional_insight_to_add:** Good routing transfers the failed experience premise, not merely the latest tool or CSS symptom.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The seed provides no priority among adjacent references.
- **supporting_reason:** Route to the smallest missing capability at the earliest stage that blocks the highest-consequence claim.
- **counterargument_or_limit:** Product, architecture, behavior, content, and runtime issues can coexist.
- **assumptions_and_boundaries:** Choose the route that can first falsify or decide the branch controlling action.
- **revision_decision:** Add primary and complementary routes with evidence-return requirements.
- **additional_insight_to_add:** The best destination is the next evidence system that can change the user decision, not the closest frontend keyword.

### Question 03: When does the default work well?
- **current_section_observation:** Capability routing works when repository tools, specialized skills, browser harnesses, design/content owners, and project policies are discoverable.
- **supporting_reason:** Specialization improves depth without making one design reference encode every framework, domain, renderer, and operational method.
- **counterargument_or_limit:** A project may lack the named tool, environment, or qualified owner.
- **assumptions_and_boundaries:** Route by capability contract and verify current availability before use.
- **revision_decision:** Add direct-source, manual, and owner fallbacks.
- **additional_insight_to_add:** Modular methods remain coherent when all returned evidence updates one experience packet.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** Routing fails when agents bounce among guides without a falsifiable claim, transfer stale summaries, or select methods sharing the same blind spot.
- **supporting_reason:** More tools and context do not improve evidence when no destination can observe the unresolved premise.
- **counterargument_or_limit:** Initial exploration can legitimately read several local references to formulate the question.
- **assumptions_and_boundaries:** Time-box discovery and detect repeated routes with no state change.
- **revision_decision:** Add cycle detection, shared-blind-spot warnings, and terminal owner escalation.
- **additional_insight_to_add:** Repeated routing without new evidence is a backpressure signal rather than a reason to open another guide.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** Alternatives include one monolithic frontend guide, direct repository evidence, specialized implementation/design skills, browser tools, user research, expert review, or owner decision under uncertainty.
- **supporting_reason:** Monoliths reduce navigation but inflate context; modules deepen capability but add handoff; experts resolve nuance but can bottleneck.
- **counterargument_or_limit:** Excessive modularity makes simple tasks feel overengineered.
- **assumptions_and_boundaries:** Route only at a material boundary and stop when required evidence returns.
- **revision_decision:** Add information gain, setup, sensitivity, and ownership tradeoffs.
- **additional_insight_to_add:** Adjacent guidance should be demand-loaded like source modules rather than preloaded for every interface.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Hazards include unavailable skills, version mismatch, circular referrals, sensitive data/assets, duplicated analysis, split writers, context loss, and destination output disconnected from the original task.
- **supporting_reason:** These failures consume time or create technically sound evidence that cannot authorize the frontend decision.
- **counterargument_or_limit:** Full preflight for every possible route is excessive.
- **assumptions_and_boundaries:** Check instructions, availability, permissions, ownership, and data/asset boundaries only for selected routes.
- **revision_decision:** Add route preflight and minimal handoff packet.
- **additional_insight_to_add:** A route ledger prevents several agents from independently redesigning the same surface with incompatible assumptions.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** The seed lists generic neighbors but no good or failed handoff.
- **supporting_reason:** Good routing sends a blank canvas with exact browser state to 3D diagnosis; bad routing rewrites visual guidance for a runtime bug; borderline search can cheaply refute a universal claim.
- **counterargument_or_limit:** A weaker method can find a counterexample even when it cannot verify completeness.
- **assumptions_and_boundaries:** Use correlated routes for falsification candidates, not independent proof.
- **revision_decision:** Add good, bad, and conditional examples.
- **additional_insight_to_add:** Route quality depends on the logical role of returned evidence, not the apparent sophistication of the tool.

### Question 08: How can the important claims be verified?
- **current_section_observation:** The seed does not define route success.
- **supporting_reason:** Verify that the destination consumed the stated gap, used capable authority/observation, returned reproducible evidence, and changed or safely assigned the experience claim.
- **counterargument_or_limit:** Some routes only confirm that content, access, device, or owner evidence is unavailable.
- **assumptions_and_boundaries:** A supported escalation-required result is useful when it prevents unsupported release.
- **revision_decision:** Add route acceptance and reconstruction fields.
- **additional_insight_to_add:** Routing succeeds when uncertainty is reduced, reclassified, or owned safely, not only when the initial design is confirmed.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** Capability gaps are reasoned from method boundaries, while exact skill/tool/version availability and repository fit vary at execution.
- **supporting_reason:** This assignment does not invoke adjacent tools merely because route examples name them.
- **counterargument_or_limit:** Installed skills and repository scripts remain useful candidate destinations.
- **assumptions_and_boundaries:** Mark candidate versus verified availability and read selected instructions first.
- **revision_decision:** Separate conceptual route class from executable destination.
- **additional_insight_to_add:** Portable routing names the evidence contract first and product/tool name second.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The adjacent list can be modeled as a graph whose edges mean missing authority or observation rather than theme similarity.
- **supporting_reason:** That supports shortest useful routes, cycle detection, complementary evidence, and return-to-task semantics.
- **counterargument_or_limit:** Numeric graph optimization would be unnecessary for most design work.
- **assumptions_and_boundaries:** Use qualitative tables and loop checks rather than route scores.
- **revision_decision:** Add entry, return, contradiction, and terminal edge semantics.
- **additional_insight_to_add:** Clear method boundaries make the reference stronger by preserving one user decision across specialized work.

## Section 018: Workload Model
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed caps work at one flow, three viewport classes, one loading/error state, and one keyboard path without measurement or relation to product complexity.
- **supporting_reason:** Operators need to choose focused correction, standard journey, shared-system work, global review, sharding, or specialist routes from actual state/content/component/environment pressure.
- **counterargument_or_limit:** One memorable boundary is easier to apply than a multidimensional model.
- **assumptions_and_boundaries:** Remove unsupported universal counts and replace them with measurable local pressure plus explicit support policy.
- **revision_decision:** Define workload variables, stage drivers, modes, pressure signals, and measurement cards.
- **additional_insight_to_add:** One destructive dialog can require more assurance than dozens of static content components.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The seed does not distinguish initial product review, local implementation, browser iteration, and final system-wide validation.
- **supporting_reason:** Start with current product/state surface, measure larger matrices, reuse validated components, and choose an explicit phase before allocating context and rendering.
- **counterargument_or_limit:** Formal measurement for a small static correction adds overhead.
- **assumptions_and_boundaries:** Use direct complete reads/renders when cost is immaterial and instrument only when it changes route or support.
- **revision_decision:** Add focused, standard, shared-system, global, high-assurance, and specialized modes.
- **additional_insight_to_add:** Phase identity is workload because one component can be cheap to fix but expensive to validate across all consumers.

### Question 03: When does the default work well?
- **current_section_observation:** A staged model fits repeated page work, large apps, shared components, multi-agent handoffs, and stable browser fixtures.
- **supporting_reason:** Observable dimensions reveal whether product clarification, state modeling, code, rendering, accessibility, visual review, or owner coordination dominates.
- **counterargument_or_limit:** Rapid prototypes can invalidate measurements before reuse.
- **assumptions_and_boundaries:** Include churn and expected reuse horizon; keep prototypes lightweight until direction stabilizes.
- **revision_decision:** Add favorable and unfavorable workload signatures.
- **additional_insight_to_add:** A slower packet can be economical when reused across many states, while a fast design can be wasteful if stale immediately.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The model fails if pressure causes silent state omission, ideal content only, dropped accessibility modes, reduced browser coverage, arbitrary page splitting, or hidden owner boundaries.
- **supporting_reason:** These optimizations change the experience evidence while preserving the appearance of completion.
- **counterargument_or_limit:** Justified scoping and sharding can preserve bounded user journeys.
- **assumptions_and_boundaries:** Scope interfaces, shared premises, integration, and no-global-claim boundaries explicitly.
- **revision_decision:** Add safe narrowing, sharding, phase-change, and route-away contracts.
- **additional_insight_to_add:** A cheap partial render is dangerous when workload pressure is not carried into the final support claim.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** Alternatives include complete product review, route/state selection, component stories, screenshot matrices, deterministic inventories, multiple packets, parallel agents, and native design/test systems.
- **supporting_reason:** Each exchanges context, completeness, coordination, visual evidence, freshness, and maintenance.
- **counterargument_or_limit:** Operating several systems can cost more than one coherent packet and browser harness.
- **assumptions_and_boundaries:** Add complexity only when measured workload or assurance pays for lifecycle.
- **revision_decision:** Build a workload-route matrix with amortization and evidence-contract impact.
- **additional_insight_to_add:** Incrementality is valuable only when stale source, state, content, and screenshot detection is reliable.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Hazards include route/component inventories, combinatorial states/content/viewports, slow browser suites, flaky assets, animations, device variance, context compaction, edit collisions, and reviewer overload.
- **supporting_reason:** These costs vary independently of page or component count.
- **counterargument_or_limit:** Deterministic manifests, fixture equivalence classes, and focused reruns can control several dimensions.
- **assumptions_and_boundaries:** Automation may index/render/validate while semantic selection and support/risk acceptance remain explicit.
- **revision_decision:** Add per-stage context, execution, and owner pressure checks.
- **additional_insight_to_add:** Reviewer coherence and product-owner capacity can saturate before compute or screenshot storage.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** The seed offers no workload examples beyond its fixed boundary row.
- **supporting_reason:** Good handling reuses one component and risk-based matrix; bad handling declares three arbitrary viewports complete; borderline sharding is safe by independent journey/component ownership.
- **counterargument_or_limit:** A small count can still hide complex security, accessibility, or state consequence.
- **assumptions_and_boundaries:** Judge workload by relationships and assurance rather than scalar size.
- **revision_decision:** Add focused reuse, silent truncation, and scoped-shard examples.
- **additional_insight_to_add:** The same surface can be manageable for visual review and unmanageable for exhaustive user/browser/locale assurance.

### Question 08: How can the important claims be verified?
- **current_section_observation:** The seed does not define how to measure frontend workload or capacity.
- **supporting_reason:** Capture journeys, states, transitions, components, consumers, content variants, containers, browsers, inputs, assets, checks, screenshots, owner time, failures, and rework under frozen identity.
- **counterargument_or_limit:** Instrumentation and visual review-time measurement introduce overhead and confounding.
- **assumptions_and_boundaries:** Measure decision-relevant dimensions, disclose overhead, and avoid extrapolating from one page or reviewer.
- **revision_decision:** Add workload measurement card and comparison protocol.
- **additional_insight_to_add:** Measure evidence utility alongside screenshot/test volume because faster omission is not an optimization.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** Current process requires measured artifact handling and exact matrices, while no universal frontend scale or reviewer capacity was measured here.
- **supporting_reason:** This evolution performs structural work but no target app or browser workload study.
- **counterargument_or_limit:** Systems reasoning identifies likely growth, coupling, and coordination drivers.
- **assumptions_and_boundaries:** Present tendencies without concrete capacity, duration, or viewport thresholds.
- **revision_decision:** Remove fixed seed capacity and require local calibration.
- **additional_insight_to_add:** Capacity belongs to the user journey, product matrix, environment, assurance profile, and team rather than this reference.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The seed does not connect workload optimization to experience integrity and design governance.
- **supporting_reason:** Scoping, fixture grouping, screenshot sampling, component reuse, and parallelism can alter the evidence population and ownership.
- **counterargument_or_limit:** Some optimizations affect only redundant capture or serialization and preserve semantics.
- **assumptions_and_boundaries:** Classify every optimization by effect on source, state, content, render, verification, and invalidation.
- **revision_decision:** Add an optimization impact ledger and revalidation rules.
- **additional_insight_to_add:** Frontend process speed is valid only when the user task remains equally or more falsifiable and recoverable.

## Section 019: Reliability Target
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed mixes source-label presence, a twenty-use routing sample, unsupported-claim absence, and recovery wording as if they formed one calibrated frontend reliability target.
- **supporting_reason:** A practitioner instead needs to decide which interface outcomes are hard release invariants, which indicators need sampling, which failures are immediate claim blockers, and which residual risks require named-owner acceptance.
- **counterargument_or_limit:** A short scorecard is easier to communicate than a profile with several evidence classes.
- **assumptions_and_boundaries:** Reliability classification must stay proportional to user consequence and available observability; it cannot manufacture a numerical service level from editorial review alone.
- **revision_decision:** Replace the mixed target table with an experience reliability model spanning prevention, detection, containment, recovery, and learning.
- **additional_insight_to_add:** The useful unit is a recoverable user outcome under stated states and environments, not a percentage detached from the experience graph.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The inherited rows provide no rule for deciding when absolute language, sampled confidence, or qualitative review is appropriate.
- **supporting_reason:** Default to hard invariants for material task correctness and supported accessibility paths, sentinel rejection for unsupported consequential claims, sampled indicators for broad consistency, and explicit acceptance for unresolved bounded risk.
- **counterargument_or_limit:** Hard invariants can become impractical when third-party services, devices, or stochastic content are outside project control.
- **assumptions_and_boundaries:** Phrase invariants around behavior the product owns, then state external dependency, fallback, monitoring, and recovery obligations separately.
- **revision_decision:** Add focused, standard, shared-system, and high-assurance reliability profiles with local target cards rather than universal numeric constants.
- **additional_insight_to_add:** Separating an obligation from its measurement method prevents a flaky browser oracle from weakening the underlying product contract.

### Question 03: When does the default work well?
- **current_section_observation:** Profiled reliability works when journeys, material states, support modes, owners, fixtures, render environments, and release consequences can be bounded.
- **supporting_reason:** Those boundaries let teams choose deterministic checks for invariants and representative review for lower-consequence variation without confusing the two kinds of evidence.
- **counterargument_or_limit:** Early explorations may lack stable product direction or fixtures sufficient for a release-grade profile.
- **assumptions_and_boundaries:** Use a provisional exploration profile with explicit non-release status, then promote obligations when the intended user task and system stabilize.
- **revision_decision:** Describe favorable conditions and promotion triggers for each reliability profile.
- **additional_insight_to_add:** Reliability evidence becomes reusable when state identities and failure semantics stay stable even while visual styling evolves.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The model fails when teams label a narrow screenshot sample reliable, average away a catastrophic branch, or use unverifiable absolute claims to close review.
- **supporting_reason:** Aggregate pass rates can conceal keyboard traps, destructive-action mistakes, missing recovery, inaccessible status, or blank media/canvas states that matter independently of the average.
- **counterargument_or_limit:** Not every visual mismatch deserves release-blocking treatment, and zero variation is neither feasible nor desirable across rendering engines.
- **assumptions_and_boundaries:** Classify severity by user outcome, reversibility, support promise, and claim scope rather than pixel identity alone.
- **revision_decision:** Add downgrade and route-away conditions for unknown or unobservable high-consequence behavior.
- **additional_insight_to_add:** A reliability profile should become stricter when a failure is silent or irreversible, even if that branch is statistically uncommon.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** Candidate strategies include deterministic contracts, risk-based matrices, production telemetry, exploratory review, conformance audits, canary releases, feature rollback, and owner sign-off.
- **supporting_reason:** Each trades prevention strength, environment realism, detection latency, privacy, maintenance cost, and recovery speed.
- **counterargument_or_limit:** Combining every strategy can slow delivery while duplicating evidence and producing alert fatigue.
- **assumptions_and_boundaries:** Select the smallest complementary set that can falsify material outcomes before release and detect environment-specific escapes afterward.
- **revision_decision:** Add a strategy tradeoff table that names evidence strength and blind spots instead of ranking methods universally.
- **additional_insight_to_add:** Recovery controls may justify a staged rollout but cannot excuse a known violation of a supported critical user path.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Major hazards are vanity pass rates, unstable denominators, omitted negative states, permissive snapshots, unreviewed baselines, flaky retries, synthetic-only content, inaccessible fixtures, and ownerless exceptions.
- **supporting_reason:** These mechanisms make evidence look healthier while reducing sensitivity to the failures the target was meant to prevent.
- **counterargument_or_limit:** Sampling and retries remain legitimate when equivalence classes and transient infrastructure failures are defined independently of the desired result.
- **assumptions_and_boundaries:** Record denominator, exclusions, retry reason, baseline authority, environment identity, and exception expiry with every reported target.
- **revision_decision:** Add anti-gaming rules and sentinel-event escalation to the reliability contract.
- **additional_insight_to_add:** An improving metric with a shrinking or easier evidence population is a reliability regression, not progress.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** A good target states that a failed destructive action preserves data and exposes recovery; a bad target says the interface is ninety-nine-percent reliable without defining journeys, failures, or denominator.
- **supporting_reason:** Concrete outcomes connect the target to user consequence, fixtures, checks, and escalation, whereas an unlabeled percentage cannot guide implementation.
- **counterargument_or_limit:** A dashboard aggregate can still summarize a well-defined set of underlying contracts for operational scanning.
- **assumptions_and_boundaries:** Aggregates are secondary views whose numerator, denominator, severity mix, support matrix, and drill-down evidence remain available.
- **revision_decision:** Add good, bad, and borderline cases for hard invariants, sampled consistency, and accepted residual risk.
- **additional_insight_to_add:** Borderline evidence becomes acceptable only after its no-claim boundary and follow-up trigger are explicit.

### Question 08: How can the important claims be verified?
- **current_section_observation:** The seed suggests text review and twenty downstream verdicts but does not define sampling population, inter-reviewer agreement, browser fixtures, or false-negative checks.
- **supporting_reason:** Verification should freeze the target card, enumerate material branches, run deterministic checks, inspect representative renders, inject sentinel failures, record reviewer decisions, and replay recovery.
- **counterargument_or_limit:** Production telemetry may reveal device and content combinations that controlled verification cannot reproduce.
- **assumptions_and_boundaries:** Use privacy-preserving operational evidence as complementary detection, not as retrospective permission to skip pre-release contracts.
- **revision_decision:** Specify a target-card protocol with baseline, candidate, matrix, oracle, exclusions, failure injection, evidence location, owner, and expiration.
- **additional_insight_to_add:** Deliberately seeding a known unsupported claim or broken branch tests whether the reliability process can detect failure, not merely report passing artifacts.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** It is structurally clear that unsupported consequential claims and unrecoverable material task failures require stronger handling than stylistic variance, but this corpus contains no target-product reliability study.
- **supporting_reason:** The evolution can define evidence classes and safeguards while lacking empirical rates for browsers, users, reviewers, components, or production incidents.
- **counterargument_or_limit:** Product teams may already possess support policies and historical data that justify quantitative targets absent from this reference.
- **assumptions_and_boundaries:** Treat all numbers as local policies tied to named populations, periods, environments, and owners; do not inherit the seed's percentages as measured facts.
- **revision_decision:** Mark confidence by invariant, indicator, sentinel, judgment, and unknown categories.
- **additional_insight_to_add:** Honest uncertainty is operational when it changes rollout, monitoring, ownership, or route selection rather than appearing as a generic disclaimer.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** Reliability targets influence what teams render, what failures they prioritize, and which experience variants remain visible over time.
- **supporting_reason:** A target therefore changes product incentives: poorly chosen measures reward easy states, hide rare users, and normalize exceptions, while outcome contracts preserve attention on consequential paths.
- **counterargument_or_limit:** Rich contracts can decay into paperwork if they are not generated from and linked to executable state identities.
- **assumptions_and_boundaries:** Keep target cards close to tests, fixtures, render manifests, release controls, operational signals, and owning decisions with explicit invalidation.
- **revision_decision:** Add feedback-loop and target-retirement rules so reliability policy evolves when product states or support promises change.
- **additional_insight_to_add:** The second-order goal is not perpetual metric growth; it is faster trustworthy detection, bounded harm, and clearer recovery when assumptions fail.

## Section 020: Failure Mode Table
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed lists source drift, generic advice, viewport-state breakage, and client recovery as four flat rows without distinguishing user consequence, evidence failure, or method boundary.
- **supporting_reason:** Operators need to classify an observed frontend failure, determine whether it blocks a claim or release, choose containment and recovery, and route missing authority to the right owner.
- **counterargument_or_limit:** A large taxonomy can delay a straightforward local fix.
- **assumptions_and_boundaries:** Use the smallest class that changes mitigation; do not require exhaustive analysis for a reversible isolated mismatch with a known cause.
- **revision_decision:** Expand the registry across product/source, state, semantics/input, composition/content, assets/3D, implementation/runtime, verification/performance, and handoff/governance.
- **additional_insight_to_add:** The same visible symptom can arise from different causal layers, so remediation should follow evidence rather than appearance.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The inherited mitigation column jumps directly to refresh, block, screenshot, or retry without a common diagnostic contract.
- **supporting_reason:** Default to recording trigger, affected journey/state, user-visible consequence, detectability, evidence, scope, owner, containment, recovery, prevention, and replay check.
- **counterargument_or_limit:** Some exploratory visual defects lack enough evidence for confident causal assignment.
- **assumptions_and_boundaries:** Mark cause as provisional while still containing the observed consequence and preserving artifacts for diagnosis.
- **revision_decision:** Introduce a failure record and consequence classes before the detailed registry.
- **additional_insight_to_add:** Separating symptom, cause, and evidence prevents a cosmetic patch from masking a product-state or data-contract defect.

### Question 03: When does the default work well?
- **current_section_observation:** A structured registry works well when the product has identifiable journeys, state fixtures, component ownership, browser evidence, and a route for specialist authority.
- **supporting_reason:** Those anchors make failures reproducible and let teams attach corrective checks at the nearest responsible layer.
- **counterargument_or_limit:** Cross-browser, third-party, device, font, and network failures may remain intermittent despite good instrumentation.
- **assumptions_and_boundaries:** Preserve environment identity and confidence, and use operational detection when deterministic reproduction is unavailable.
- **revision_decision:** Add favorable diagnostic conditions and evidence-escalation paths.
- **additional_insight_to_add:** A registry gains value over time only when resolved cases update fixtures, checks, components, and source guidance rather than remaining isolated tickets.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** Failure analysis becomes harmful when labels substitute for reproduction, blame individuals, normalize known harm, or require speculative root causes before containment.
- **supporting_reason:** Users need a safe truthful state immediately even when the final causal chain spans product policy, data, framework, browser, or operations.
- **counterargument_or_limit:** Premature containment can itself remove important functionality or obscure evidence.
- **assumptions_and_boundaries:** Preserve diagnostic artifacts and choose reversible containment proportional to consequence.
- **revision_decision:** Add stop conditions for unsupported diagnosis and rules separating immediate response from long-term prevention.
- **additional_insight_to_add:** A useful failure mode is defined by the decision it changes, not by taxonomic elegance.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** Alternatives include lightweight defect labels, state-transition analysis, accessibility audits, browser matrices, fault trees, formal hazard analysis, incident review, telemetry clustering, and owner-specific runbooks.
- **supporting_reason:** They vary in causal depth, setup cost, coverage, operational realism, reviewer expertise, and suitability for high-consequence paths.
- **counterargument_or_limit:** Formal safety methods are disproportionate for ordinary reversible interface polish.
- **assumptions_and_boundaries:** Escalate method depth with harm, irreversibility, silent failure, shared reach, recurrence, and uncertainty.
- **revision_decision:** Add a method-selection guide rather than presenting one table as universal diagnosis.
- **additional_insight_to_add:** Combining a state graph with a compact failure registry often provides more actionable coverage than adding more symptom labels.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Important omissions include authority conflict, wrong task model, missing negative states, stale success, semantic control mismatch, focus loss, text overflow, hidden actions, asset failure, blank canvas, hydration races, and false-green verification.
- **supporting_reason:** These failures can preserve a superficially polished screen while breaking task completion, accessibility, truthfulness, recovery, or evidence integrity.
- **counterargument_or_limit:** Not every product uses canvas, 3D, authentication, localization, or client hydration.
- **assumptions_and_boundaries:** Mark non-applicable classes explicitly and derive active classes from the product's actual stack, content, support, and consequence.
- **revision_decision:** Add layered failure rows with concrete detection and response.
- **additional_insight_to_add:** Silent stale-state and false-green evidence deserve higher attention because they hide both the user failure and the process failure.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** Good handling reproduces an auth-expiry branch, preserves draft input, restores focus after reauthentication, and adds a browser check; bad handling changes an error color after one screenshot.
- **supporting_reason:** The good case connects trigger, outcome, recovery, prevention, and evidence, whereas the bad case treats a symptom without restoring the journey.
- **counterargument_or_limit:** A color correction can be complete when the defect truly is an isolated contrast-token regression.
- **assumptions_and_boundaries:** Confirm the causal layer and affected consumers before choosing a local visual remedy.
- **revision_decision:** Include good, bad, and borderline examples with explicit classification reasoning.
- **additional_insight_to_add:** Borderline cases become tractable when the registry records what evidence would distinguish competing causes.

### Question 08: How can the important claims be verified?
- **current_section_observation:** The seed names screenshots and instrumentation but not fault injection, expected wrong-state evidence, recovery replay, or recurrence checks.
- **supporting_reason:** Verification should reproduce trigger, observe failure independently, apply mitigation, rerun material branches, inject relevant dependency failures, and inspect user-visible plus operational recovery.
- **counterargument_or_limit:** Destructive or production-only failures may be unsafe to inject directly.
- **assumptions_and_boundaries:** Use isolated fixtures, staging, simulators, feature controls, or tabletop review and disclose fidelity limits.
- **revision_decision:** Add a focused failure-verification protocol and evidence checklist.
- **additional_insight_to_add:** A mitigation is not verified until the original trigger no longer harms the claimed journey and a neighboring counterexample still behaves correctly.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The local source strongly supports distinctive design, product-fit context, hierarchy, implementation, and accessibility-aware choices, while the broader failure taxonomy is systems inference.
- **supporting_reason:** No target application, browser trace, incident corpus, accessibility audit, or user study was executed during this reference evolution.
- **counterargument_or_limit:** Mature engineering practice makes several causal categories and verification methods broadly credible.
- **assumptions_and_boundaries:** Label product-specific likelihood and severity as local judgments and avoid implying measured frequencies.
- **revision_decision:** Add confidence and evidence-boundary fields to failure records.
- **additional_insight_to_add:** Confidence in a mitigation can be high while confidence in the original root cause remains provisional, and the record should preserve that distinction.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** Repeated frontend failures reveal missing product contracts, component semantics, fixture classes, support policy, or ownership rather than merely individual coding mistakes.
- **supporting_reason:** Aggregating causal records can identify systemic prevention opportunities and show when local fixes repeatedly transfer harm between states or consumers.
- **counterargument_or_limit:** Failure counts can be biased by reporting quality, observability, product usage, and changing taxonomies.
- **assumptions_and_boundaries:** Analyze recurrence qualitatively and retain denominator/context before prioritizing systemic changes.
- **revision_decision:** Add learning-loop rules that promote recurring failures into design-system, test-harness, source, or ownership changes.
- **additional_insight_to_add:** The registry should shrink repeated causal classes over time even if improved detection temporarily increases observed incidents.

## Section 021: Retry Backpressure Guidance
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed provides sound caution but combines external-evidence refresh, verification reruns, long agent workflows, and distributed ownership without distinguishing their side effects or users.
- **supporting_reason:** Practitioners need to decide whether a failed frontend operation, asset load, browser check, evidence read, or agent batch may be retried, paused, degraded, cancelled, or escalated.
- **counterargument_or_limit:** A separate policy for every failure class can overwhelm a small workflow.
- **assumptions_and_boundaries:** Use one shared eligibility contract while recording class-specific side-effect and recovery rules only where they change behavior.
- **revision_decision:** Define retry domains, eligibility predicates, backpressure signals, attempt records, and terminal outcomes.
- **additional_insight_to_add:** Retry is a state transition with product and evidence consequences, not a generic response to red output.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The seed's one-bounded-retry rule is useful as a conservative editorial default but is not a measured universal constant for browsers, networks, assets, or user mutations.
- **supporting_reason:** Default to no automatic retry until the operation is classified, replay-safe, bounded by deadline/attempt budget, cancellable where relevant, observable, and incapable of duplicating harmful effects.
- **counterargument_or_limit:** A single immediate reattempt can efficiently clear a known stale read or isolated runner startup fault.
- **assumptions_and_boundaries:** Permit that local reattempt only when the premise changed or infrastructure diagnosis is explicit; preserve both attempts in evidence.
- **revision_decision:** Retain one reattempt as a narrow process heuristic and require product-local policies elsewhere.
- **additional_insight_to_add:** An attempt should add information or use a changed premise; identical repetition without a hypothesis is delay disguised as resilience.

### Question 03: When does the default work well?
- **current_section_observation:** Bounded retry works for idempotent reads, cacheable assets, stale source refresh, deterministic fixture restart, and explicitly idempotent mutations with truthful pending state.
- **supporting_reason:** These operations can be replayed without multiplying user-visible effects and can expose success, terminal failure, cancellation, or degraded fallback clearly.
- **counterargument_or_limit:** Even read-only retries can overload a dependency or drain device/network resources during a widespread outage.
- **assumptions_and_boundaries:** Respect server guidance, shared budgets, connectivity, visibility, and client capability rather than retrying each component independently.
- **revision_decision:** Add favorable retry signatures and coordinated resource limits.
- **additional_insight_to_add:** Retry safety depends on system-wide arrival rate and dependency health, not only on one operation's idempotency.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** Retry is wrong for validation, authorization policy, unsupported capability, deterministic semantic/visual defects, destructive non-idempotent actions, missing owner decisions, and exhausted evidence boundaries.
- **supporting_reason:** Repetition cannot change these premises and may duplicate effects, erase diagnostic state, trap users, or turn a blocked claim into a false green.
- **counterargument_or_limit:** A user may intentionally change credentials, input, permission, or environment and initiate a new operation.
- **assumptions_and_boundaries:** Treat that as a new attempt with changed input/premise, not an invisible retry of the same failure.
- **revision_decision:** Add terminal classes and explicit user-action reentry rules.
- **additional_insight_to_add:** Calling every reentry a retry hides the product decision that made progress possible.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** Alternatives include immediate fail, manual retry, delayed retry with jitter, queueing, coalescing, cancellation, circuit breaking, stale-cache display, fallback content, offline persistence, and specialist escalation.
- **supporting_reason:** They trade latency, freshness, load, user control, complexity, energy/network use, evidence clarity, and risk of duplicate side effects.
- **counterargument_or_limit:** Sophisticated distributed patterns can be unnecessary or misleading in a local frontend or editorial workflow.
- **assumptions_and_boundaries:** Select mechanisms only when actual dependency behavior, volume, and consequence justify them; otherwise prefer explicit bounded state.
- **revision_decision:** Add a retry-versus-alternative matrix for product and process domains.
- **additional_insight_to_add:** A truthful cached or degraded state can serve the user better than repeated pursuit of fresh perfection.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Hazards include duplicate submissions, retry storms, nested component retries, stale completion overwrites, hidden spinners, lost form state, unbounded browser reruns, masked flakiness, and parallel edit collisions.
- **supporting_reason:** These failures multiply load and ambiguity while making the final success difficult to attribute or trust.
- **counterargument_or_limit:** Central request coordination, idempotency keys, cancellation, and attempt manifests can contain many hazards.
- **assumptions_and_boundaries:** Those controls themselves need lifecycle, timeout, cleanup, accessibility, and failure verification.
- **revision_decision:** Add storm, stale-result, false-green, user-state, and ownership protections.
- **additional_insight_to_add:** Backpressure should preserve the most consequential recovery and verification work while shedding speculative generation and duplicate capture first.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** Good behavior disables duplicate submission while preserving input and exposes a safe retry after classified timeout; bad behavior recursively resubmits a payment-like mutation behind an endless spinner.
- **supporting_reason:** The good case bounds side effects and preserves user agency, whereas the bad case hides state and can multiply harm.
- **counterargument_or_limit:** Disabling a control without status, cancellation, or recovery can itself create an inaccessible dead end.
- **assumptions_and_boundaries:** Pair suppression with truthful progress/status and an appropriate escape path.
- **revision_decision:** Add product, browser-verification, and agent-batch examples.
- **additional_insight_to_add:** A borderline rerun becomes trustworthy only when prior failure classification and retained evidence show why the second result is more credible.

### Question 08: How can the important claims be verified?
- **current_section_observation:** The seed does not define how to test duplicate effects, retry budgets, cancellation, backoff, user state preservation, or process checkpoints.
- **supporting_reason:** Verification should inject transient and terminal failures, control time, count attempts/effects, simulate cancellation/navigation, inspect focus/status, force overload, and resume from persisted atomic boundaries.
- **counterargument_or_limit:** Exact timing tests are often flaky and do not reproduce real dependency behavior.
- **assumptions_and_boundaries:** Assert scheduling ranges, state transitions, budgets, and side effects with fake time where possible; complement with controlled integration evidence.
- **revision_decision:** Add deterministic retry/backpressure test scenarios and attempt-ledger fields.
- **additional_insight_to_add:** The most important assertion is frequently effect count and final user state, not elapsed delay.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** Replay safety, bounded attempts, visible terminal state, preserved evidence, and ownership are defensible defaults, while no product traffic, dependency, browser-runner, or reviewer-capacity data was measured here.
- **supporting_reason:** The reference can specify decision logic but cannot choose universal attempt counts, delays, jitter, queue limits, or timeouts.
- **counterargument_or_limit:** Existing platform and service contracts may already supply tested retry headers, idempotency semantics, or budgets.
- **assumptions_and_boundaries:** Prefer those current authoritative contracts and record their scope instead of inventing frontend-local constants.
- **revision_decision:** Separate portable safety invariants from locally calibrated policy values.
- **additional_insight_to_add:** Uncertainty about a numeric budget should cause measurement or conservative containment, not an arbitrary copied constant.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** Retry policy shapes interface trust, dependency load, test credibility, agent progress durability, and which failures remain visible to owners.
- **supporting_reason:** Invisible automatic success can conceal recurring defects, while immediate terminal failure can abandon recoverable users or waste completed work.
- **counterargument_or_limit:** Exposing every transient attempt can burden users with implementation detail.
- **assumptions_and_boundaries:** Present stable user-relevant state and recovery while retaining detailed attempt telemetry/evidence for operators and reviewers.
- **revision_decision:** Add learning, escalation, and policy-invalidation loops across product and agent workflows.
- **additional_insight_to_add:** Mature backpressure is selective attention: it stops low-value work so diagnosis, recovery, and authoritative decisions can finish.

## Section 022: Observability Checklist
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed combines source manifests, proof records, latency quantiles, browser captures, leading indicators, and compact audit evidence without identifying distinct observers or decisions.
- **supporting_reason:** Teams need to decide what evidence must be captured for frontend implementation review, runtime diagnosis, user-outcome monitoring, reliability recovery, and future invalidation.
- **counterargument_or_limit:** Recording every possible field increases cost, privacy exposure, and reviewer noise.
- **assumptions_and_boundaries:** Capture only decision-relevant signals under explicit access, retention, and redaction rules; prefer reconstructability over raw volume.
- **revision_decision:** Split observability into decision, source, implementation, render, runtime, performance, retry, review, and governance layers.
- **additional_insight_to_add:** Observability quality is the ability to answer a bounded question and trigger action, not the number of logs or screenshots retained.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The seed's checklist lacks a stable identity connecting a user journey and state to source version, implementation revision, environment, render, check, reviewer, and outcome.
- **supporting_reason:** A minimal evidence envelope should preserve those links plus claim scope, timestamp, owner, result class, failure/recovery, and invalidation trigger.
- **counterargument_or_limit:** Full linkage can be excessive for a tiny isolated visual correction.
- **assumptions_and_boundaries:** Scale detail with consequence and reuse while retaining revision, state, environment, proof, and owner at minimum.
- **revision_decision:** Define a compact event/artifact envelope and profile-specific checklists.
- **additional_insight_to_add:** Stable identities make small evidence composable; giant transcripts make even complete evidence difficult to query or compare.

### Question 03: When does the default work well?
- **current_section_observation:** Layered observability works when states and transitions are explicit, environments are reproducible, evidence locations are durable, and owners know which signal changes action.
- **supporting_reason:** These conditions let reviewers connect source premises to rendered behavior and operators connect escaped failures back to components, fixtures, and support policy.
- **counterargument_or_limit:** Third-party clients, assistive technologies, privacy restrictions, and intermittent graphics/network behavior can limit visibility.
- **assumptions_and_boundaries:** Record blind spots and use complementary user reports, controlled reproduction, and specialist review rather than claiming complete telemetry.
- **revision_decision:** Add favorable conditions, blind-spot declarations, and escalation routes.
- **additional_insight_to_add:** The most reusable observation is often a typed relationship between artifacts, not another isolated metric value.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** Observability fails when it captures sensitive content, tracks users without authority, records only success, lacks denominators, samples away rare failures, or produces signals with no owner/action.
- **supporting_reason:** Such systems can harm users, misstate reliability, and consume attention without improving diagnosis or recovery.
- **counterargument_or_limit:** Some high-cardinality context is necessary to reproduce content-, locale-, browser-, or device-specific defects.
- **assumptions_and_boundaries:** Use privacy-reviewed classes, redaction, short retention, access controls, and synthetic correlation rather than raw user content whenever feasible.
- **revision_decision:** Add privacy, sampling, cardinality, retention, and actionability gates.
- **additional_insight_to_add:** A signal that cannot be safely retained may still be handled through ephemeral local diagnosis and aggregated outcome evidence.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** Alternatives include structured event logs, traces, metrics, screenshots, video, DOM/accessibility snapshots, network/console captures, user reports, session replay, synthetic checks, and review packets.
- **supporting_reason:** They differ in semantic depth, visual fidelity, privacy, storage, queryability, environmental realism, and ability to establish causality.
- **counterargument_or_limit:** No single modality proves user task correctness or design quality.
- **assumptions_and_boundaries:** Combine the minimum independent modalities needed for the claim and document each oracle's blind spots.
- **revision_decision:** Add a signal-selection tradeoff table and discourage transcript dumping.
- **additional_insight_to_add:** Screenshots explain composition, traces explain timing, semantic snapshots explain structure, and user outcomes explain consequence; conflating them weakens all four.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Hazards include missing state identity, stale screenshot reuse, source/revision mismatch, quantiles without sample population, swallowed console errors, retry collapse, PII leakage, cardinality explosions, and alert fatigue.
- **supporting_reason:** These defects sever evidence lineage or create misleading aggregates even when individual artifacts appear valid.
- **counterargument_or_limit:** Strict schemas can lag product evolution and cause teams to omit novel diagnostic fields.
- **assumptions_and_boundaries:** Version schemas, allow bounded extension, and preserve unknown fields without abandoning required core identities.
- **revision_decision:** Add lineage, denominator, retry, privacy, and schema-evolution checks.
- **additional_insight_to_add:** Retrying and then logging only the successful attempt is an observability failure because it erases the system's true recovery path.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** Good evidence links a checkout-error state to revision, browser, fixture class, console/network trace, screenshot, recovery outcome, and owner; bad evidence says p95 improved without scenario or population.
- **supporting_reason:** The good record supports diagnosis and replay, while the bad metric cannot establish equivalence or user impact.
- **counterargument_or_limit:** A compact dashboard can be useful when every aggregate drills into versioned definitions and raw bounded evidence.
- **assumptions_and_boundaries:** Treat dashboards as indexes, not sources of truth detached from schemas and artifacts.
- **revision_decision:** Include good, bad, and borderline observability records.
- **additional_insight_to_add:** Borderline evidence becomes decision-grade when its missing denominator, identity, or blind spot is supplied rather than when more decimal precision is added.

### Question 08: How can the important claims be verified?
- **current_section_observation:** The seed says to record proof but does not test whether evidence is emitted, linked, redacted, retained, queryable, or capable of detecting known failure.
- **supporting_reason:** Verification should inject representative failures, inspect emitted schema/linkage, confirm sensitive fields are absent, query the decision path, replay recovery, and test expiration/invalidation.
- **counterargument_or_limit:** Production telemetry behavior cannot be fully proven by local mocks.
- **assumptions_and_boundaries:** Combine schema/unit checks, controlled integration, staging/synthetic runs, privacy review, and sampled production audit where authorized.
- **revision_decision:** Add an observability verification protocol with sentinel events and evidence-reconstruction exercises.
- **additional_insight_to_add:** Ask a reviewer unfamiliar with the change to reconstruct one failure; reconstruction time and unanswered questions expose observability gaps directly.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** Exact source/revision/environment/state/proof linkage is a defensible process requirement, while no target product telemetry pipeline, user population, latency distribution, or privacy regime was observed here.
- **supporting_reason:** The reference can define fields and decision logic but cannot prescribe production event names, retention periods, quantiles, or alert thresholds.
- **counterargument_or_limit:** Existing organization-wide observability and privacy standards may provide those authoritative values.
- **assumptions_and_boundaries:** Integrate with current approved systems and state when this digest creates no runtime instrumentation itself.
- **revision_decision:** Separate portable evidence invariants from local telemetry policy.
- **additional_insight_to_add:** Absence of runtime evidence in this evolution is a boundary, not evidence that runtime outcomes are healthy or unhealthy.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** Observability choices determine which users, states, browsers, and failures become visible enough to influence design-system and product priorities.
- **supporting_reason:** Instrumentation therefore shapes organizational attention and can systematically underrepresent privacy-sensitive, low-volume, assistive, offline, or fallback paths.
- **counterargument_or_limit:** Maximizing capture for underrepresented paths can conflict with privacy, consent, and cost.
- **assumptions_and_boundaries:** Use deliberate synthetic/participatory/accessibility evidence and transparent blind-spot registers instead of invasive blanket capture.
- **revision_decision:** Add representation audits, feedback-to-guidance loops, and signal retirement criteria.
- **additional_insight_to_add:** Mature observability measures recovery and learning as well as failure, so teams do not optimize only for suppressing visible error counts.

## Section 023: Performance Verification Method
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed combines a universal local-interaction p95 target, screenshot overlap, workflow completion, reference quality, tool-call counts, reviewer time, and prerequisite gates under one performance heading.
- **supporting_reason:** Practitioners need to decide whether a frontend or evidence-workflow change is measurably better under an equivalent user outcome and a locally authoritative target.
- **counterargument_or_limit:** Separating measurement domains makes the method longer than a memorable single threshold.
- **assumptions_and_boundaries:** Use only the domain-specific card needed by the claim while preserving equivalence and uncertainty requirements.
- **revision_decision:** Split user interaction, load/render/asset, layout stability, workflow, and review-process performance methods.
- **additional_insight_to_add:** Performance is time and resource behavior of a particular outcome; it cannot be inferred from source brevity or visual smoothness alone.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** No target product, device, workload, interaction boundary, sample, clock, or baseline supports the inherited `p95 under 100 ms` value.
- **supporting_reason:** Default to a frozen hypothesis, locally sourced requirement, baseline/candidate scenario, controlled environment, equivalent behavior/content/visuals/accessibility, repeated observations, raw distributions, and bounded conclusion.
- **counterargument_or_limit:** Strict control can reduce realism and miss field-specific devices, networks, caches, or content.
- **assumptions_and_boundaries:** Pair controlled causal comparison with authorized field/synthetic evidence when production variability matters.
- **revision_decision:** Remove the universal threshold and require a target provenance plus measurement card.
- **additional_insight_to_add:** A target without provenance is design decoration; a comparison without equivalence is a different product.

### Question 03: When does the default work well?
- **current_section_observation:** Controlled comparison works for regressions and optimizations with reproducible fixtures, stable builds, defined milestones, representative devices/browsers, and inspectable traces.
- **supporting_reason:** These conditions let teams attribute changes to implementation rather than state, content, cache, network, animation, or asset differences.
- **counterargument_or_limit:** User-perceived responsiveness and long-tail production behavior can depend on factors that laboratory runs cannot recreate.
- **assumptions_and_boundaries:** Use field distributions and user-outcome signals as complementary evidence with privacy and denominator controls.
- **revision_decision:** Add favorable signatures and controlled-versus-field role separation.
- **additional_insight_to_add:** Repeatability and representativeness answer different questions; reliable guidance says which one each result supports.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The method fails when teams cherry-pick fastest runs, discard failures, change fixtures, disable features, lower image/model fidelity, omit error states, or compare unmatched cache/device conditions.
- **supporting_reason:** These changes improve the number by changing the evidence population or user experience rather than improving implementation.
- **counterargument_or_limit:** Product-approved progressive loading or fidelity adaptation can legitimately change when work occurs.
- **assumptions_and_boundaries:** Measure the new staged experience end to end, including fallback quality, task outcome, resource use, and affected users.
- **revision_decision:** Add comparability gates and optimization-impact classification.
- **additional_insight_to_add:** Moving latency outside the measured interval is not performance improvement unless the full user consequence remains accounted for.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** Available methods include microbenchmarks, component profiling, browser traces, synthetic journeys, lab audits, visual/layout metrics, real-user measurement, resource budgets, and reviewer-workflow studies.
- **supporting_reason:** They vary in causal isolation, environmental realism, cost, privacy, sample quality, and ability to diagnose or generalize.
- **counterargument_or_limit:** Running every method can exceed the value of optimizing a low-consequence path.
- **assumptions_and_boundaries:** Choose methods from claim, consequence, suspected bottleneck, and existing telemetry rather than tool popularity.
- **revision_decision:** Add a method-selection matrix with blind spots.
- **additional_insight_to_add:** Trace-based diagnosis and outcome-based validation are complements: one explains mechanism while the other tests whether users benefit.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Hazards include ambiguous start/end marks, warm/cold mixing, timer distortion, small samples, parallel noise, retries, layout instability, main-thread blocking, blank 3D frames, and reviewer-quality omission.
- **supporting_reason:** Each can produce precise-looking numbers that fail to represent the intended task or obscure correctness regressions.
- **counterargument_or_limit:** Perfectly isolated measurement is rarely possible on real browsers and devices.
- **assumptions_and_boundaries:** Capture confounders, randomize/interleave when suitable, retain raw runs, and bound claims rather than demanding impossible control.
- **revision_decision:** Add a confounder and validity checklist.
- **additional_insight_to_add:** Measurement variance is information about the environment or workload, not merely noise to delete.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** Good evidence compares the same search journey and result content on a declared device/browser with traces and no visual/accessibility regression; bad evidence reports one faster reload after cache warmup.
- **supporting_reason:** The good case holds outcome and conditions stable, while the bad case confounds cache and sample selection.
- **counterargument_or_limit:** A warm-cache journey may be the dominant intended use case.
- **assumptions_and_boundaries:** Measure warm and cold populations separately and state which product decision each supports.
- **revision_decision:** Add runtime, asset/3D, and reviewer-process examples.
- **additional_insight_to_add:** A borderline result becomes useful when its population and no-generalization boundary are explicit.

### Question 08: How can the important claims be verified?
- **current_section_observation:** The seed lists measurement fields but does not define baseline/candidate repetition, result retention, equivalence review, uncertainty, or regression criteria.
- **supporting_reason:** Verification should predeclare card, validate clocks/marks, freeze fixtures/build/environment, alternate runs, preserve failures, inspect traces/renders/semantics, summarize distribution, and rerun independent checks.
- **counterargument_or_limit:** Statistical inference can be misleading with autocorrelation, changing field populations, or too few observations.
- **assumptions_and_boundaries:** Report sample limits and practical effect without pretending unsupported significance.
- **revision_decision:** Add a stepwise protocol and result schema.
- **additional_insight_to_add:** Review the slow and failing runs, not just the aggregate, because tails often reveal distinct states or defects.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** Comparable scenarios and explicit evidence are necessary for credible claims, while this evolution executed no target frontend benchmark, browser profile, field analysis, or reviewer-time experiment.
- **supporting_reason:** The digest can prescribe method quality but cannot report a speedup, threshold, percentile, or capacity for unknown products.
- **counterargument_or_limit:** Existing product budgets and platform guidance may provide current targets outside this corpus.
- **assumptions_and_boundaries:** Cite those targets with version, environment, owner, and scope; otherwise describe a measurement proposal rather than a result.
- **revision_decision:** Add a no-results boundary and confidence taxonomy.
- **additional_insight_to_add:** Method confidence and result confidence are separate: a sound protocol can remain unexecuted, and a measured number can come from a weak protocol.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** Performance budgets alter design composition, asset selection, state feedback, verification breadth, and which devices/users remain supported.
- **supporting_reason:** Optimization is therefore a product and equity decision as well as a technical one, especially when adaptive fidelity or sampling excludes constrained environments.
- **counterargument_or_limit:** Not every resource reduction changes user meaning or support.
- **assumptions_and_boundaries:** Classify impact on task, content, semantics, visual direction, recovery, support matrix, and evidence before accepting an optimization.
- **revision_decision:** Add an impact ledger and feedback loop from measured tails to product/design-system choices.
- **additional_insight_to_add:** The best optimization can be eliminating unnecessary work, but only after proving that the work was not carrying user value or evidence.

## Section 024: Scale Boundary Statement
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed names independent systems, ownership, unbounded discovery, production traffic, distributed execution, context drift, and large codebases but offers no integrated sufficiency decision.
- **supporting_reason:** Operators need to decide whether this digest can guide a focused frontend change, requires indexed narrowing or sharding, must federate with adjacent specialties, or should yield to a product-scale control plane.
- **counterargument_or_limit:** A multidimensional boundary is less immediate than one page, file, or owner count.
- **assumptions_and_boundaries:** Scale should be judged by coupling, consequence, and evidence burden, because scalar size routinely misclassifies frontend work.
- **revision_decision:** Define scale dimensions, operating levels, promotion signals, and terminal method boundaries.
- **additional_insight_to_add:** A single shared primitive can be product-scale work while many isolated static surfaces remain locally tractable.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The seed recommends splitting by theme file but theme boundaries may not align with journeys, components, state contracts, or shared design authority.
- **supporting_reason:** Default to the smallest complete user-decision boundary, inventory cross-boundary links, and scale through stable journey/state/component/system partitions with one integration owner.
- **counterargument_or_limit:** Establishing complete candidate recall and ownership maps costs more than direct edits in a small codebase.
- **assumptions_and_boundaries:** Use complete direct review when cheap; introduce indexes and governance only after measured coordination or evidence pressure justifies them.
- **revision_decision:** Replace theme-file splitting as a universal rule with stable-boundary partition criteria.
- **additional_insight_to_add:** The correct shard minimizes shared semantic decisions, not merely equalizes file or screenshot counts.

### Question 03: When does the default work well?
- **current_section_observation:** The digest is strongest for bounded journeys, explicit material states, known sources, inspectable components/consumers, reproducible browser environments, and available product/design/engineering owners.
- **supporting_reason:** Those conditions allow complete orientation, implementation, render verification, recovery, and handoff inside a reviewable evidence graph.
- **counterargument_or_limit:** Some exploratory redesigns intentionally precede stable ownership, states, or architecture.
- **assumptions_and_boundaries:** Keep exploration provisional and prevent it from carrying product-wide reliability or support claims until authority stabilizes.
- **revision_decision:** Add favorable scale signatures and promotion from exploration to operational work.
- **additional_insight_to_add:** Reuse can make a larger surface cheaper than a smaller novel one when contracts, fixtures, and renders remain trustworthy.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** This reference becomes insufficient when domain policy, security, production SLO/telemetry, large migrations, device labs, multi-product design governance, or independent systems dominate the decision.
- **supporting_reason:** Those concerns require authority, tooling, operational control, and evidence that a frontend design digest cannot supply.
- **counterargument_or_limit:** The reference can still frame the user journey and evidence request before routing.
- **assumptions_and_boundaries:** Retain frontend outcome ownership while transferring specialist premises and return with specified evidence.
- **revision_decision:** Add explicit terminal boundaries and federated return contracts.
- **additional_insight_to_add:** Routing is successful scale handling when it preserves one decision across methods rather than abandoning it to another document.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** Alternatives include complete reads, deterministic indexes, dependency/source graphs, component catalogs, visual regression systems, design-system governance, multi-agent shards, staged rollouts, and specialist platforms.
- **supporting_reason:** They trade setup cost, recall, freshness, global consistency, review burden, ownership clarity, and operational control.
- **counterargument_or_limit:** New infrastructure can become a stale second authority and increase total coordination.
- **assumptions_and_boundaries:** Add a mechanism only with measured pressure, owner, validity checks, and retirement path.
- **revision_decision:** Add a scale-strategy tradeoff matrix and native-system preference.
- **additional_insight_to_add:** The cheapest long-term scale mechanism is often strengthening existing component, fixture, test, and design-token contracts rather than building another index.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Hazards include arbitrary sharding, incomplete inventories, stale graphs, cross-shard token changes, screenshot explosion, combinatorial matrices, reviewer saturation, and production assumptions without operational owners.
- **supporting_reason:** These failures preserve local progress while losing global journey integrity, support coverage, or evidence freshness.
- **counterargument_or_limit:** Risk-based equivalence classes and critical-path sampling can control combinatorics.
- **assumptions_and_boundaries:** Document grouping rationale, boundaries that could disprove it, exclusions, and no-global-claim policy.
- **revision_decision:** Add scale anti-patterns, overlap rules, and saturation signals.
- **additional_insight_to_add:** Reviewer coherence and decision latency can become the first bottleneck even when compute and storage remain abundant.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** Good scaling versions a shared form component, inventories consumers, partitions migrations, and integrates critical journeys; bad scaling assigns arbitrary page ranges while agents independently change tokens.
- **supporting_reason:** The good partition centralizes shared contracts and preserves integration evidence, whereas the bad one creates hidden semantic conflicts.
- **counterargument_or_limit:** Route/page partitioning can be valid when journeys and components are genuinely independent.
- **assumptions_and_boundaries:** Verify independence through shared-source/component/state/owner links rather than naming convention.
- **revision_decision:** Add focused, indexed, sharded, federated, and over-boundary examples.
- **additional_insight_to_add:** Borderline scale becomes manageable when the integration claim is narrower than the union of local claims and explicitly tested.

### Question 08: How can the important claims be verified?
- **current_section_observation:** The seed suggests dependency narrowing but does not verify index recall, stale detection, shard coverage, overlap, integration, or review capacity.
- **supporting_reason:** Verification should compare index candidates with complete samples, hash inputs, map shared links, audit union/exclusions, inject stale entries, replay cross-shard journeys, and measure reviewer reconstruction.
- **counterargument_or_limit:** Complete recall is expensive or impossible in genuinely open-ended source discovery.
- **assumptions_and_boundaries:** Mark discovery open, narrow the claim, and route research rather than presenting a bounded index as exhaustive.
- **revision_decision:** Add focused scale-verification checks and evidence cards.
- **additional_insight_to_add:** A scale mechanism is reliable only if it fails visibly when its inventory or premises go stale.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** Shared ownership, source discovery, state matrices, and production operations add distinct burdens, but no frontend corpus-scale experiment or team-capacity study was executed here.
- **supporting_reason:** Systems reasoning supports qualitative promotion signals while not supporting numeric page, component, agent, source, or screenshot limits.
- **counterargument_or_limit:** A specific organization may have measured limits and mature platform contracts.
- **assumptions_and_boundaries:** Use those local values with provenance and treat this section as a decision framework, not a capacity benchmark.
- **revision_decision:** Remove implied universal counts and add a no-capacity-result boundary.
- **additional_insight_to_add:** Scale is partly organizational: the same technical graph can be tractable with clear authority and unsafe with unresolved decision ownership.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** Scaling frontend work changes governance, evidence freshness, component incentives, and the relationship between local autonomy and product-wide coherence.
- **supporting_reason:** Indexes, shards, and automated renders determine what remains visible and can entrench obsolete structures if their invalidation is weak.
- **counterargument_or_limit:** Deliberate decentralization can improve domain fit and delivery when shared contracts are minimal.
- **assumptions_and_boundaries:** Centralize only shared semantics, support policy, system primitives, and integration evidence; leave bounded product decisions local.
- **revision_decision:** Add governance and retirement consequences to scale guidance.
- **additional_insight_to_add:** Healthy scale is not maximal centralization; it is explicit authority at each shared boundary plus cheap falsification of integration claims.

## Section 025: Future Refresh Search Queries
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed provides three broad official-documentation, repository-example, and release-note queries but does not say what future decision each query should update.
- **supporting_reason:** A later authorized maintainer needs to decide whether public research is warranted, which claim or boundary it can change, and when the current local corpus remains sufficient.
- **counterargument_or_limit:** Preplanning queries cannot predict future terminology, products, frameworks, or evidence gaps.
- **assumptions_and_boundaries:** Preserve seed phrases as historical refresh prompts while versioning new decision-specific variants at execution time.
- **revision_decision:** Add trigger, decision target, source priority, result schema, and stop condition to the query registry.
- **additional_insight_to_add:** A search phrase without a decision target encourages source accumulation rather than reference maintenance.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The current task explicitly prohibits browsing, so none of the listed or proposed queries has been executed or validated.
- **supporting_reason:** Default to `unexecuted_no_browse`, use current local evidence, and run future research only under explicit authorization with primary authoritative sources preferred.
- **counterargument_or_limit:** Delaying research can leave fast-changing browser, accessibility, framework, or platform guidance stale.
- **assumptions_and_boundaries:** Record invalidation triggers and elevate uncertainty rather than silently importing remembered external claims.
- **revision_decision:** Attach authorization/status and freshness triggers to every query family.
- **additional_insight_to_add:** Honest nonexecution is stronger evidence hygiene than converting plausible search intent into implied findings.

### Question 03: When does the default work well?
- **current_section_observation:** A structured refresh plan works when a specific claim depends on current public behavior, known official publishers exist, and versions/dates can be recorded.
- **supporting_reason:** Decision-bound queries reduce noise and let maintainers compare current primary evidence with local product/source authority.
- **counterargument_or_limit:** Design-quality judgments may not have one canonical public authority.
- **assumptions_and_boundaries:** Use external sources as context or alternatives while product needs and current local system retain their appropriate authority.
- **revision_decision:** Add source-type-specific acceptance and conflict rules.
- **additional_insight_to_add:** Public popularity cannot override a deliberate product-mode decision, but it can reveal changed platform constraints or counterexamples.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** Search-led refresh fails when snippets, SEO summaries, stale tutorials, undated examples, copied benchmarks, or repository popularity substitute for direct current sources.
- **supporting_reason:** Such evidence can look specific while omitting version, scope, conflicts, product context, and verification conditions.
- **counterargument_or_limit:** Secondary sources can help discover terminology and primary artifacts.
- **assumptions_and_boundaries:** Treat them as leads, not authority, and trace consequential claims to inspectable current evidence.
- **revision_decision:** Add rejection criteria and a no-authoritative-result outcome.
- **additional_insight_to_add:** A failed search is useful when it narrows the claim and records an unresolved evidence boundary instead of inviting invention.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** Alternatives include rereading local corpus/product code, opening known official URLs, searching official domains, inspecting repository releases/issues, consulting standards, testing browsers directly, or routing specialists.
- **supporting_reason:** They trade freshness, authority, reproducibility, discovery breadth, implementation realism, and access cost.
- **counterargument_or_limit:** Official documentation may omit real-world failure modes while community reports may lack controlled evidence.
- **assumptions_and_boundaries:** Triangulate only when the decision warrants it and keep each source's role visible.
- **revision_decision:** Add a source-escalation order and modality tradeoffs.
- **additional_insight_to_add:** Direct target-product/browser evidence can outrank generic guidance for behavior while still needing standards or official docs for support semantics.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Hazards include query drift, personalized results, inaccessible pages, dynamic content, version mismatch, mirrored docs, renamed repositories, cherry-picking, citation rot, and accidental browsing under prohibition.
- **supporting_reason:** These failures break reproducibility and can violate task scope even before a claim is evaluated.
- **counterargument_or_limit:** Exact result reproducibility is limited by changing indexes and pages.
- **assumptions_and_boundaries:** Preserve query, date, authorization, filters, selected source identity/version, relevant claim, and archived/local evidence where permitted.
- **revision_decision:** Add execution logging, version checks, and stop-on-permission rules.
- **additional_insight_to_add:** Query provenance should be versioned separately from source provenance because the discovery path and evidence artifact change independently.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** Good future research asks an official browser or framework source about one changed behavior and records version/date; bad research searches generic best practices and cites a snippet as a universal rule.
- **supporting_reason:** The good case can update a bounded claim, while the bad case imports authority-free advice.
- **counterargument_or_limit:** A broad query can be useful for initial vocabulary discovery.
- **assumptions_and_boundaries:** Mark broad results as candidate leads and require a second primary-source step before adoption.
- **revision_decision:** Add good, bad, and borderline query-to-decision examples.
- **additional_insight_to_add:** Borderline discovery becomes safe when it explicitly cannot change guidance until source authority and product fit are verified.

### Question 08: How can the important claims be verified?
- **current_section_observation:** The seed does not verify phrase preservation, nonexecution status, future result authority, conflict handling, or whether research changed a specific section.
- **supporting_reason:** Verification should compare exact seed queries, confirm no execution artifacts exist, audit future source metadata, trace each adopted claim, and rerun affected product/browser evidence.
- **counterargument_or_limit:** Absence of execution is difficult to prove beyond the current process and artifact record.
- **assumptions_and_boundaries:** State the observed process boundary precisely and avoid claiming global absence of browsing history.
- **revision_decision:** Add query-registry and post-refresh verification gates.
- **additional_insight_to_add:** A refresh is complete only when changed evidence invalidates and rechecks dependent guidance, not when links are collected.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** It is known that the three seed query strings exist and current instructions forbid browsing; no public result, current external fact, or search quality was observed in this evolution.
- **supporting_reason:** The maintained artifact records planned queries but contains no authorized retrieval evidence.
- **counterargument_or_limit:** Some external facts may also be represented in local source files, but their current public status remains unverified.
- **assumptions_and_boundaries:** Preserve local provenance and label future freshness questions without treating them as stale by default.
- **revision_decision:** Add a strong no-results statement and confidence categories for later refresh.
- **additional_insight_to_add:** A query plan is proposal evidence, not external evidence, even when its wording names official documentation.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** Future query design influences which authorities, communities, product modes, accessibility concerns, and implementation examples become visible during maintenance.
- **supporting_reason:** Repeated generic wording can reinforce fashionable defaults and under-sample dissenting constraints, specialist standards, or domain-specific evidence.
- **counterargument_or_limit:** Expanding every query for representational balance can produce unmanageable research scope.
- **assumptions_and_boundaries:** Derive query diversity from the unresolved decision and known blind spots, then stop when evidence is sufficient for that bounded claim.
- **revision_decision:** Add query-review, retirement, and bias-check rules.
- **additional_insight_to_add:** Treat the query registry like maintained code: each entry needs purpose, owner, execution status, dependencies, and deletion when it no longer changes guidance.

## Section 026: Evidence Boundary Notes
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed defines local, external, and combined-inference labels but does not tell readers how to classify observations, proposals, owner decisions, verification results, conflicts, or unknowns.
- **supporting_reason:** A user needs to decide what a claim is based on, how strongly it can govern implementation, which evidence can falsify it, and when another authority is required.
- **counterargument_or_limit:** Too many evidence classes can make readable guidance feel bureaucratic.
- **assumptions_and_boundaries:** Apply labels at the smallest consequential claim or table row, not mechanically to every sentence.
- **revision_decision:** Preserve the three exact seed labels and add a compact claim taxonomy plus authority rules.
- **additional_insight_to_add:** Evidence labels are useful only when they change interpretation, verification, or reuse.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** Two local paths contain one hash-identical 42-line frontend-design body, while the external URLs and all future queries remain unrefreshed under no-browse instructions.
- **supporting_reason:** Default to local fact for directly observed bytes/claims, combined inference for operational synthesis, proposal for unexecuted methods, and unknown for missing target/external evidence.
- **counterargument_or_limit:** Local hash equality proves byte identity only and does not establish loader, precedence, ownership, licensing, or current runtime activation.
- **assumptions_and_boundaries:** State exactly what was observed and separate surrounding-context questions that were not tested.
- **revision_decision:** Add evidence identity, scope, confidence, applicability, and invalidation fields.
- **additional_insight_to_add:** Precise narrow facts accumulate into stronger guidance more safely than broad labels that overclaim source authority.

### Question 03: When does the default work well?
- **current_section_observation:** Typed evidence works when source paths/versions are stable, inference is explicit, target verification is linked, conflicts remain visible, and owner decisions are recorded separately.
- **supporting_reason:** Readers can reconstruct how aesthetic guidance became a bounded product action and which premise must change to invalidate it.
- **counterargument_or_limit:** Fast exploratory design may rely heavily on provisional judgment before durable evidence exists.
- **assumptions_and_boundaries:** Mark exploration as proposal with no release/support claim and promote only after product, implementation, and rendered evidence.
- **revision_decision:** Add promotion rules from hypothesis to locally verified guidance.
- **additional_insight_to_add:** Evidence maturity can differ within one recommendation: source intent may be certain while product fit and performance remain unknown.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** Boundary labeling fails when one label covers a mixed paragraph, a URL is treated as a refreshed fact, inference is presented as source wording, or tests are generalized beyond their matrix.
- **supporting_reason:** These practices create authority laundering and let a narrow observation support a global frontend claim.
- **counterargument_or_limit:** Excessive fragmentation can make the core decision difficult to read.
- **assumptions_and_boundaries:** Group claims only when they share source, scope, confidence, and verification status; otherwise split them.
- **revision_decision:** Add claim-granularity and no-transitive-authority rules.
- **additional_insight_to_add:** Citation adjacency is not evidence linkage unless the source directly supports the proposition at the stated scope.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** Alternatives include inline labels, source maps, footnotes, claim ledgers, requirement-to-test matrices, decision records, provenance graphs, and executable evidence manifests.
- **supporting_reason:** They trade readability, queryability, maintenance, audit depth, machine validation, and risk of becoming a second stale authority.
- **counterargument_or_limit:** A sophisticated graph is unnecessary for a small stable design task.
- **assumptions_and_boundaries:** Start with compact source/claim tables and add structure only when reuse, conflicts, scale, or consequence justify it.
- **revision_decision:** Add a proportional evidence-format guide and native-system preference.
- **additional_insight_to_add:** The best evidence representation is the cheapest one that detects staleness and reconstructs a consequential decision.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Hazards include duplicate-source confidence inflation, stale hashes, URL existence mistaken for content, paraphrase drift, unlabeled owner policy, circular citations, unverifiable metrics, and missing negative evidence.
- **supporting_reason:** Each can make a polished reference appear more certain or current than the observed corpus permits.
- **counterargument_or_limit:** Not every inference requires a formal counterevidence search.
- **assumptions_and_boundaries:** Increase challenge and independent evidence with consequence, novelty, conflict, and portability of the claim.
- **revision_decision:** Add evidence anti-patterns, conflict states, and invalidation triggers.
- **additional_insight_to_add:** Duplicate paths improve provenance coverage but should not count as independent corroboration when their bytes match.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** Good labeling says the local skill urges a clear direction, then separately infers a state-aware design workflow; bad labeling says three preserved URLs prove production readiness.
- **supporting_reason:** The good example respects source content and synthesis scope, whereas the bad one invents retrieved evidence and target verification.
- **counterargument_or_limit:** A future authorized refresh could turn a preserved URL into external evidence for a narrow versioned claim.
- **assumptions_and_boundaries:** Promotion requires direct inspection, source identity, date/version, limitations, and local applicability checks.
- **revision_decision:** Add good, bad, and conditional promotion examples.
- **additional_insight_to_add:** Borderline evidence becomes safe when the final sentence states exactly what cannot be concluded.

### Question 08: How can the important claims be verified?
- **current_section_observation:** The seed gives label definitions but no audit for source existence/hash, direct support, external refresh state, inference separation, or claim-to-check linkage.
- **supporting_reason:** Verification should sample claims, open their exact sources, confirm scope/paraphrase, validate statuses, trace dependent examples/checks, inject a mislabeled sentinel, and test invalidation.
- **counterargument_or_limit:** Complete claim-level audit can be expensive for a very long reference.
- **assumptions_and_boundaries:** Audit all high-consequence/quantitative/current claims and risk-sample lower-consequence synthesis with explicit population.
- **revision_decision:** Add an evidence audit protocol and focused integrity gates.
- **additional_insight_to_add:** Testing whether the process rejects one deliberately unsupported claim provides evidence about the boundary mechanism itself.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** Known facts include exact local path/hash/body observations and preserved seed URL/query identities; target-product outcomes, current external content, performance, user impact, and production reliability were not measured.
- **supporting_reason:** The evolution read local artifacts and performed structural synthesis without browsing or running a target frontend.
- **counterargument_or_limit:** Several systems and frontend practices are strongly defensible as general engineering guidance.
- **assumptions_and_boundaries:** Present them as combined inference and require target evidence before product-specific adoption or quantitative claim.
- **revision_decision:** Add an explicit known/unknown ledger and no-results statement.
- **additional_insight_to_add:** Confidence in a general causal risk does not establish its frequency or severity in an unobserved product.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** Evidence boundaries shape organizational memory: future agents may treat this evolved reference as authority even after its sources, products, and platforms change.
- **supporting_reason:** Without invalidation and decision lineage, helpful synthesis hardens into folklore and copied precision.
- **counterargument_or_limit:** Constantly expiring guidance can make stable principles unnecessarily difficult to reuse.
- **assumptions_and_boundaries:** Invalidate event-driven product/version claims while retaining stable principles with their original scope and counterconditions.
- **revision_decision:** Add reuse, conflict, supersession, and retirement rules for evidence-backed guidance.
- **additional_insight_to_add:** The long-term value of the reference is not certainty preservation but preserving how to detect when certainty should change.
