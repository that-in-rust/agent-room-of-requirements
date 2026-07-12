# Frontend Design Quality Patterns

This reference helps an implementation agent, designer-engineer, or reviewer decide **how to turn a known user workflow into a functional, accessible, responsive, visually intentional interface and how to prove that the delivered experience matches that decision**. It is not a substitute for product discovery, content authority, domain policy, causal debugging, or a target-specific performance study.

The governing question is:

> Who is trying to do what, in which states and environments, which visual and interaction choices support that task, and what rendered evidence would expose a failure before release?

**Default experience workflow**

| stage | required input | produced decision | stop or route signal |
| --- | --- | --- | --- |
| Understand the product | Primary user, job, context, content, frequency, consequence, and product category. | One bounded workflow and success state. | Desired behavior, audience, or authority remains undecided. |
| Inspect the existing system | Repository instructions, framework, routes, components, tokens, assets, tests, and current rendered behavior. | Reuse, adapt, or intentionally diverge decision. | A second design system would be created without ownership. |
| Model interaction states | Default, loading, empty, partial, error, disabled, permission, offline, success, and recovery states as applicable. | State graph with user actions and feedback. | Static composition hides material runtime behavior. |
| Establish constraints | Accessibility, keyboard, content, viewport, browser, localization, performance, security, and data boundaries. | Observable experience obligations and no-go conditions. | A domain owner or target environment is required. |
| Choose a visual direction | Typography, color, density, composition, media, motion, and distinctive product signal. | Small coherent design system tied to audience and task. | Novelty conflicts with familiarity, trust, readability, or product conventions. |
| Implement behavior first | Repository-native components, data/state ownership, semantics, controls, and recovery. | Working user journey in real code. | Placeholder behavior or decorative facade substitutes for the requested app. |
| Refine presentation | Stable dimensions, responsive constraints, hierarchy, assets, micro-interaction, and detail. | Polished states without layout instability or interaction loss. | Styling requires hidden overflow, inaccessible semantics, or brittle positioning. |
| Verify rendered experience | Behavior checks, keyboard path, accessibility evidence, desktop/mobile screenshots, runtime/console review, and task-oriented human inspection. | Proceed, revise, narrow, or route decision. | Source looks plausible but actual pixels or interaction state remain unobserved. |

This order is a default, not a demand to redesign an established product. When an existing design system, component, workflow contract, and regression test already settle a narrow correction, reuse them and verify the affected state. A new aesthetic direction needs an explicit product reason; visual novelty is not evidence of quality by itself.

**Quality dimensions**

| dimension | minimum question | common false positive | capable evidence |
| --- | --- | --- | --- |
| Task success | Can the intended user complete the primary job and recover from likely failure? | A polished first screen with no working workflow. | End-to-end or interaction checks plus task walkthrough. |
| State completeness | Does every material asynchronous and data state have a coherent interface? | Only populated happy-path fixtures are rendered. | State matrix, fixtures, and screenshots for boundary states. |
| Accessibility | Can people perceive, understand, navigate, and operate the interface through required modes? | Automated scanner passes while focus order or naming is confusing. | Semantic inspection, automated checks, keyboard and assistive-technology review as consequence requires. |
| Responsive composition | Does hierarchy remain usable across required containers, content lengths, and viewports? | One desktop screenshot is scaled down visually. | Rendered viewport/container matrix with overflow and text-fit checks. |
| Visual coherence | Do typography, color, spacing, imagery, density, and motion express one context-appropriate direction? | Every element is individually attractive but the page has no hierarchy. | Token/style audit and experienced human review against the stated direction. |
| Interaction clarity | Are controls familiar, states visible, commands discoverable, and feedback timely? | Decorative affordances look clickable or icon-only controls are ambiguous. | Interaction tests, hover/focus/pressed/disabled states, and usability review. |
| Runtime resilience | Do data, auth, network, hydration, asset, and rendering failures leave a safe next action? | Error is logged but the user remains stuck. | Fault fixtures, recovery checks, console/network evidence, and observability. |
| Performance fit | Does the experience meet an owner-approved budget under a defined workload? | One warm local interaction is called universally fast. | Controlled browser/runtime measurement with functional and visual counter-gates. |
| Maintainability | Do components, state ownership, tokens, and assets follow the repository's architecture? | A visually strong page duplicates primitives and creates a parallel system. | Source/diff review, project checks, and design-system ownership. |

These dimensions are coupled. A display font can strengthen identity while increasing overflow risk. Dense tables can improve expert scanning while failing touch or small-screen use. Motion can communicate causality while blocking input or violating reduced-motion expectations. Evaluate the trade, not the isolated property.

**Minimum inputs**

- A concrete user and primary task, including frequency and consequence.
- The product mode: operational tool, content experience, commerce surface, venue/brand page, game, editor, dashboard, or another explicit category.
- Current repository and design-system conventions, including ownership and compatibility.
- Material content and data states rather than placeholder-only layouts.
- Target devices, viewports or containers, input modes, browsers, and accessibility expectations.
- A verification surface that can render the real implementation and exercise its important states.

**Required outputs for durable frontend work**

| output | minimum content | what it must not imply |
| --- | --- | --- |
| Experience statement | User, task, product context, visual direction, familiarity needs, and non-goals. | That an aesthetic adjective defines product behavior. |
| State model | Inputs, transitions, loading/empty/error/recovery, permissions, and side effects as applicable. | That every application needs every possible state. |
| Interface contract | Semantic structure, controls, content priority, responsive behavior, accessibility, and failure handling. | That a static design file proves runtime behavior. |
| Visual system | Type roles, color roles, spacing/density, surfaces, media, motion, and stable dimensions. | That novelty or a large token set creates coherence. |
| Implementation | Working repository-native code with real navigation and state ownership. | That a landing page is an acceptable substitute for an app request. |
| Evidence matrix | State/viewports, behavior checks, keyboard/accessibility, screenshots, runtime errors, and known gaps. | That a green build proves rendered quality. |
| Handoff | Changed paths, checks, rendered artifacts, residual risks, rollback/recovery, and invalidation triggers. | That acceptance remains valid after content, browser, data, tokens, or workflow changes. |

**Fit and route-away guide**

| pending question | use this reference? | stronger or preceding route |
| --- | --- | --- |
| Build or refine a known component, page, app, game, dashboard, portal, editor, or interaction | Yes. | Repository implementation and browser verification. |
| Decide which customer problem or business workflow to build | Only to define prototype/evaluation criteria. | Product discovery and accountable stakeholder. |
| Determine legal, medical, financial, privacy, or regulated content | No authority here. | Qualified domain/content owner. |
| Explain why an existing runtime interaction fails | Use after cause is known to define corrected experience. | Systematic reproduction, instrumentation, and diagnosis first. |
| Choose a new product-wide design system | Use as one evaluation reference. | Design-system governance, migration, consumer inventory, and owner decision. |
| Claim a precise speed or capacity result | Use to define quality counter-gates only. | Browser profiling, controlled measurement, and operational telemetry. |
| Prove security or authorization behavior | Auxiliary traceability only. | Threat-specific implementation, configuration, negative tests, and authorized review. |

**Evidence states**

- `source_observed`: local instructions, component source, tokens, rendered state, or check output was inspected under a named identity.
- `design_inference`: a visual or interaction recommendation follows from stated users, tasks, constraints, and design principles but remains a judgment.
- `specified`: the experience behavior and its pass/fail conditions are explicit.
- `rendered_for_scope`: actual pixels and interaction state were observed at named content, viewport, browser, and configuration.
- `verified_for_scope`: claim-capable checks and review support the bounded release decision.
- `unresolved`: product authority, content, environment, assistive-technology evidence, workload, or owner acceptance is missing.
- `invalidated`: a workflow, component, token, asset, data shape, viewport requirement, browser, or policy premise changed.

Good use: an operational queue page preserves the product's compact navigation, defines loading/empty/error/retry states, uses familiar icon controls with accessible names, fixes stable table dimensions, and is verified through keyboard paths plus desktop and narrow screenshots.

Bad use: an agent replaces a requested dashboard with a large marketing hero, nests decorative cards, uses one fashionable palette everywhere, explains features inside the UI, and reports success from source inspection without opening the rendered page.

Conditional use: a visually distinctive concept can precede production when its assumptions, placeholder behavior, accessibility gaps, and promotion gates are explicit. It becomes release evidence only after implementation, real content, required states, and target rendering are verified.

This reference is complete for a frontend decision when another reviewer can identify the user task, explain why the composition fits the product, exercise material states, navigate the required input paths, inspect actual desktop and mobile rendering, see what remains unknown, and know which future change reopens the decision.

## Source Evidence Mapping Table

The source map routes claims; it does not count citations. Local byte identity proves what a file contains. Product requirements and current repository conventions choose the experience contract. Target source, browser rendering, and interaction checks establish implemented behavior. A retained public URL proves only that a future research location was suggested until it is actually opened and reconciled.

No public page was opened while evolving this reference.

**Mapped local source family and process controls**

| source_location_path_key | observed identity | evidence class | strongest legitimate use | important boundary |
| --- | --- | --- | --- | --- |
| `agents-used-monthly-archive/claude-skills-202603/plugins/frontend-design/SKILL.md` | SHA-256 `d39adf3a983de7dafc75991590d54f091755f7e4163d5a5ed085ecd719157184` | Dated archive snapshot in one duplicate family. | Establish the exact 202603 guidance about purpose, tone, constraints, differentiation, typography, color, motion, composition, and visual detail. | It does not define a target product workflow, accessibility sufficiency, supported framework behavior, or measured user outcome. |
| `claude-skills/plugins/frontend-design/SKILL.md` | Same observed SHA-256 as the archive copy. | Current repository-local duplicate of the mapped skill body. | Show that the same aesthetic guidance is available at the current local path. | Equal bytes are not independent corroboration and do not explain package activation, owner, or precedence. |
| `agents-used-monthly-archive/idiomatic-references-202606/generated-references/frontend_design_quality_patterns.md` | SHA-256 `ea3cd4775cda2613c9b863c3d24b0c0f18acfabcd5242ff1f4ea0b7e25cb33c5` before evolution. | Frozen structural seed. | Establish the 26 original headings, baseline prose, inherited figures, and exact section expansion target. | The seed is not evidence that its fixed capacity, percentile, or reliability values apply. |
| `idiomatic-reference-evolution-spec-202607.md` and `tests/test_idiomatic_reference_evolution.py` | Current shared process controls read by this lane. | Evolution specification and structural test implementation. | Define packet questions, field shape, persistence, uniqueness, heading/order, expansion, and marker requirements. | Passing these controls does not prove an interface is usable, accessible, responsive, or visually coherent. |

The two frontend-design skill paths are one semantic source family. Read one body completely for meaning, retain both path identities for archive/current provenance, and inspect surrounding context only when packaging or historical role matters. Two identical files do not create two independent design observations.

**Target evidence sources for real interface work**

| target question | first authority | corroborating evidence | source that must not overrule it |
| --- | --- | --- | --- |
| Which user workflow should exist? | User, product, domain, content, and policy owner under explicit scope. | Current requirements, research, analytics, support evidence, and established workflow. | A generic design skill cannot invent product intent. |
| Which visual system should be preserved? | Current design-system governance, product tokens, component conventions, brand/content standards, and owner decision. | Existing pages, component stories, design files, and migration history. | A fashionable example cannot silently replace a maintained product language. |
| What does the current interface implement? | Target source, routes, state/data ownership, configuration, content, and assets at a named revision. | Build, component tests, and code history. | A screenshot or prose brief cannot override current implementation facts. |
| What pixels and interactions actually render? | Browser output under named viewport, content, state, browser, and input method. | Screenshots, DOM/accessibility tree, video/trace, console/network evidence, and human inspection. | Component source alone cannot establish layout or focus behavior. |
| Is behavior correct? | Claim-capable user-flow, component, integration, and end-to-end checks. | Negative states, keyboard path, runtime observation, and owner review. | A successful build cannot prove a workflow or recovery path. |
| Is accessibility sufficient? | Applicable product policy and user needs plus semantic, automated, keyboard, and assistive-technology evidence proportional to consequence. | Experienced review and target fixtures. | One automated score cannot establish usability or legal compliance. |
| Is responsive behavior sufficient? | Supported container/viewport/content matrix and task requirements. | Rendered pixel inspection, overflow checks, and interaction evidence. | One desktop or mobile screenshot cannot represent the range. |
| Does a quantitative performance claim hold? | Controlled target measurement under a frozen workload and owner-approved budget. | Profiling, repeated browser data, field telemetry where authorized, and quality counter-metrics. | The seed's 100 ms example or a single local observation cannot set a universal target. |
| Is release risk acceptable? | Accountable product, engineering, design, accessibility, security, or operations owner as policy requires. | Technical evidence, known gaps, rollback, and dissent. | A reference or automated suite cannot assume organizational authority. |

**Retained public research pointers**

| external_source_url_value | seed description | current state | future promotion gate |
| --- | --- | --- | --- |
| `https://react.dev/learn` | React component-driven frontend behavior reference. | `unrefreshed_no_browse`; content, version, route stability, and applicability were not checked. | Under authorization, retrieve the exact current primary page needed, match the target React/toolchain version, and reproduce the claim locally. |
| `https://threejs.org/docs/` | Three.js visual scene API documentation. | `unrefreshed_no_browse`; no scene, API, rendering, or performance behavior is asserted from it here. | Retrieve version-relevant API guidance, inspect target dependencies, and verify a real canvas on required browsers/viewports with pixel and interaction checks. |
| `https://docs.github.com/actions` | GitHub Actions delivery verification and automation reference. | `unrefreshed_no_browse`; no workflow feature, permission, or runner behavior is claimed. | Retrieve feature-specific official documentation and test the repository workflow safely under its runner and permission model. |

These descriptions are locally observed seed metadata, not refreshed public facts. Familiarity with a URL, search snippets, or remembered framework behavior cannot promote the row.

**Claim-specific read route**

1. Read the complete user request, newest instructions, repository guidance, and current progress state.
2. Inspect existing routes, components, tokens, content, assets, tests, and rendered product behavior before choosing a parallel visual system.
3. Read one representative frontend-design skill copy for inherited aesthetic rationale and constraints.
4. Separate product authority, local design guidance, implementation facts, rendered observations, examples, inference, owner decisions, and unknowns.
5. Select complete target source sections and real states needed for the pending workflow; do not reason from component names alone.
6. Refresh an external source only when permission exists and a version-sensitive public contract can change the decision.
7. Bind every durable recommendation to its target state, viewport/content conditions, capable check, owner, and invalidation trigger.

**Evidence promotion rules**

| starting evidence | permitted use | promotion requirement |
| --- | --- | --- |
| Local skill statement | Inspiration, critique vocabulary, and reasoned default. | Product fit, repository compatibility, implementation, and rendered verification. |
| Existing design file or screenshot | Intent reconstruction and visual comparison. | Current state identity, behavior contract, and browser evidence. |
| Current source code | Implementation structure and candidate behavior. | Run/build/render/check evidence for dynamic and visual claims. |
| Browser screenshot | Pixel observation for one named state. | Viewport/content matrix and interaction/accessibility evidence for broader claims. |
| Automated accessibility result | Deterministic findings inside tool capability. | Keyboard, semantics, content, and assistive-technology review as required. |
| Public documentation pointer | Future research location. | Direct access, version scope, narrow extraction, and local reproduction. |
| User or owner approval | Authorized preference or risk decision. | Recorded scope, evidence reviewed, expiry/invalidation, and applicable policy. |

**Conflict handling**

| conflict | required response |
| --- | --- |
| Local skill encourages dramatic novelty while the product is a high-frequency operational tool | Preserve intentionality but prioritize scanability, familiar controls, stable layout, and repository design conventions; record why restraint fits the task. |
| Design file and current implementation disagree | Identify whether the design is future intent, stale artifact, implementation defect, or approved divergence before editing either source. |
| Static screenshot looks correct but keyboard or data-state check fails | Treat the rendered state as incomplete; behavior and accessibility evidence block acceptance. |
| Automated check passes but human review finds hierarchy or focus confusion | Preserve both results, narrow the tool claim, and correct the user-impacting defect. |
| Refreshed official framework guidance conflicts with installed behavior | Match versions and configuration, reproduce locally, and route compatibility rather than averaging. |
| Target measurement contradicts a copied performance budget | Use the controlled target evidence for its scope and return the budget to its accountable owner. |

Good source use says, "The duplicate local skill recommends a deliberate visual direction; this established product requires dense operational scanning; the implemented state is supported by the named browser and keyboard evidence." Bad source use says, "Two local skills and three public links prove that a bold bespoke interface is the best design."

The map is versioned and causal. Product authority and current conventions constrain design; design decisions guide implementation; browser and user-flow evidence support or refute the result; failures can change later components, tests, or guidance. A later correction creates a new trajectory rather than rewriting what an earlier source contained.

## Pattern Scoreboard Ranking Table

The seed's values are preserved as **inherited editorial scores**. The local source family supplies no formula, denominator, user cohort, project sample, reviewer rubric, outcome study, or uncertainty. The numbers express historical emphasis inside the generated seed; they are not effectiveness percentages or universal frontend priorities.

**Preserved inherited scoreboard**

| pattern_identifier_stable_key | inherited_score_value | inherited_tier | protected failure | current interpretation |
| --- | ---: | --- | --- | --- |
| `workflow_context_first_design` | 95 | `default_adoption_pattern_tier` | Generic visual treatment is selected without understanding user task, product mode, constraints, or current design system. | Inspect the actual workflow and product before choosing composition or aesthetic direction. |
| `state_complete_interface_contract` | 91 | `default_adoption_pattern_tier` | A polished happy path hides loading, empty, partial, error, permission, disabled, and recovery behavior. | Make material interaction/data states explicit before treating the interface as complete. |
| `rendered_evidence_gate_coupling` | 88 | `default_adoption_pattern_tier` | Source-level confidence replaces browser, accessibility, responsive, and interaction evidence. | Attach each material recommendation to a capable rendered or behavioral rejection mechanism. |

The repeated seed key `frontend_design_quality_patterns` names the theme rather than three independently addressable controls. The evolved keys preserve the original values while making each protected failure, exception, and gate reviewable.

**Causal adoption order**

1. `workflow_context_first_design`: establish user, task, product category, existing patterns, constraints, and consequence.
2. `source_authority_boundary_split`: separate product decisions, local design guidance, current implementation, rendered observation, external pointers, and inference.
3. `state_complete_interface_contract`: define meaningful state transitions, controls, feedback, and recovery.
4. `accessibility_semantics_input_path`: establish semantic structure, accessible naming, focus behavior, keyboard/input modes, and product-specific needs.
5. `responsive_content_composition`: define hierarchy under real content, containers, viewports, zoom, and localization pressure.
6. `coherent_visual_system_direction`: choose a context-appropriate type, color, spacing, density, media, and motion system.
7. `repository_native_implementation_boundary`: reuse architecture, components, tokens, assets, and conventions where they remain suitable.
8. `rendered_evidence_gate_coupling`: inspect real pixels, states, interactions, console/runtime behavior, and claim-capable checks.
9. `experience_invalidation_and_recovery`: name what token, content, data, browser, workflow, component, or policy change reopens acceptance.

This is a dependency order, not a demand for a long document. An established component may already satisfy the first seven controls. Reuse is valid when current identity and failure behavior are checked. Mentioning the controls without exercising their rejection paths is not adoption.

**Current qualitative register**

| pattern | default posture | apply when | adapt or avoid when | verification gate | counter-signal |
| --- | --- | --- | --- | --- | --- |
| Workflow context first | Default for any visible change. | User task, product category, frequency, and consequence shape hierarchy or interaction. | A current narrow contract already settles a token or defect correction. | Reviewer can state user, primary job, current system, non-goals, and why the direction fits. | Discovery grows but no interface decision changes. |
| Existing system reuse | Default in mature products. | Components, tokens, navigation, and behavior remain suitable and owned. | Existing system causes the exact usability/accessibility failure or a governed migration is approved. | Diff and rendered result preserve compatibility or document intentional change. | New page creates duplicate primitives or visual vocabulary. |
| State-complete contract | Required for dynamic workflows. | Data, auth, network, permissions, async actions, or recovery affect use. | A truly static content surface may have a smaller applicable state set. | Fixtures and checks cover every consequence-relevant state and transition. | Only ideal populated screenshots exist. |
| Familiar control semantics | Default for repeated commands. | Users benefit from learned icons, patterns, labels, and predictable placement. | A novel interaction has evidence and does not hide behavior. | Controls have correct semantics, names, states, focus, and discoverability. | Decorative shape or text pill replaces a familiar icon without benefit. |
| Product-specific distinctiveness | Conditional but encouraged. | Brand, content, place, game, portfolio, or object needs a memorable first signal. | Operational tools need restraint, density, and repeated-action efficiency. | A reviewer identifies the distinctive decision and how it reinforces the subject. | Novelty is distributed across every element or resembles a generic trend. |
| Stable responsive composition | Required. | Content length, viewport, container, zoom, or state can alter layout. | No exception for required supported surfaces; narrow the supported matrix explicitly. | Rendered matrix has no incoherent overlap, clipping, hidden commands, or text loss. | Success depends on fixed sample copy or one viewport. |
| Accessibility as behavior | Required within product policy and user need. | Any interactive or informational interface is delivered. | Evidence depth varies by consequence; accessibility cannot be reduced to one scanner. | Semantic, automated, keyboard, focus, contrast/content, and assisted review as required. | Scanner score is cited while control names or focus order fail. |
| Deliberate motion | Conditional. | Motion communicates hierarchy, causality, continuity, or character. | Reduced-motion, low-power, input blocking, latency, or operational focus makes it harmful. | Animations preserve interaction, stable layout, cancellation, and required preference behavior. | Many unrelated micro-animations compete or delay the task. |
| Purposeful media/3D | Conditional. | Users need to inspect a product/place/object/state or gameplay benefits from the scene. | Atmospheric media obscures the subject, or 3D adds cost without task value. | Asset renders reliably, remains legible/framed, and has fallback/performance evidence. | Image is dark, generic, cropped, broken, or decorative only. |
| Rendered evidence | Required before completion. | Layout, assets, canvas, browser state, or interaction quality is claimed. | Source-only checks may suffice only for nonvisual logic with no presentation claim. | Actual browser states and target viewports are inspected and relevant tests pass. | Agent reports quality from code without opening the page. |

**Adoption profiles**

| profile | minimum visible controls | prohibited promotion |
| --- | --- | --- |
| Focused correction | Current product/design authority, affected state, regression reproduction, scoped implementation, rendered comparison, and invalidation. | Cannot support a product-wide visual, accessibility, compatibility, or performance claim. |
| Standard experience | User workflow, source map, state matrix, responsive/accessibility contract, coherent visual system, repository-native implementation, browser evidence, and recovery. | Cannot claim every browser, content length, input method, or user need without corresponding evidence. |
| High-assurance interface | Standard controls plus domain/content authority, localization/zoom, assistive-technology and device/browser matrix, security/privacy states, operational failures, rollback, and accountable acceptance. | One screenshot suite or automated score cannot substitute for the required evidence floor. |

**Pattern admission and lifecycle**

A new frontend quality pattern enters the current register only when it:

- prevents a distinct recurring user, design, implementation, or verification failure;
- states product/task preconditions and known exceptions;
- names the unsafe state and a concrete detection mechanism;
- can fail without checking only for its own terminology;
- records design, implementation, maintenance, and performance cost;
- has a counter-signal that reveals overuse;
- identifies which changed premise invalidates its prior adoption.

Promote a candidate after controlled states or repeated target observations show that it catches the intended defect without creating a worse usability, accessibility, compatibility, or maintenance outcome. Adapt it when the existing design system preserves the protected behavior another way. Retire or narrow it when enforcement creates visual ceremony without affecting user task success or defect detection.

Good scoreboard use: a reviewer recognizes an operational page, preserves its compact controls, adds explicit empty/error/retry states, and blocks completion when narrow rendering clips the primary action. Bad scoreboard use: an agent says score 95 proves a bespoke visual direction is 95 percent more effective. Conditional reuse: a token-only correction can satisfy the chain implicitly, but the changed state must still be rendered and checked.

Future calibration must separate pattern conformance from outcome. Conformance asks whether context, states, and rendered evidence were handled. Outcome research asks whether comparable users completed tasks with fewer errors, reversals, or accessibility barriers. Only bounded outcome evidence could support a new empirical ranking.

## Idiomatic Thesis Synthesis Statement

**Governing thesis:** A high-quality frontend is a coherent user task expressed through complete interaction states, accessible semantics, responsive composition, a context-appropriate visual system, repository-native implementation, and actual rendered evidence. A distinctive screenshot, formal design token set, or green build is insufficient when behavior, focus, content, recovery, layout, or product fit is wrong.

The seed's evidence labels remain, with narrower meanings:

- `local_corpus_sourced_fact`: the two mapped frontend-design skill paths are one hash-identical local source family. They establish inherited guidance about purpose, tone, constraints, differentiation, and aesthetics, not target product behavior or measured effectiveness.
- `external_research_sourced_fact`: no refreshed fact of this type was created. The three public URLs remain unrefreshed pointers because browsing was prohibited.
- `combined_evidence_inference_note`: local guidance and frontend systems reasoning support the pipeline below; target fit and release quality still require repository, browser, accessibility, and owner evidence.

**Evidence-to-experience pipeline**

| conversion | required input | emitted artifact | gate before promotion | failure state |
| --- | --- | --- | --- | --- |
| Request -> user task | User goal, actor, environment, frequency, consequence, content, and product mode. | Bounded journey, non-goals, and open decisions. | Product/content owner confirms desired outcome and authority. | Clarification, prototype, or product route required. |
| Product task -> interface states | Inputs, dependencies, permissions, async behavior, success, and failures. | State/transition model with user-visible feedback and recovery. | Every consequence-relevant branch is specified or explicitly unresolved. | Static composition is nonaccepting. |
| State -> semantic contract | Structure, control purpose, labels, navigation, focus, keyboard/input, status, and errors. | Accessible interaction contract. | Required modes can perceive and operate the task under stated policy. | Route to stronger accessibility or domain review. |
| Contract -> composition | Information priority, density, content lengths, containers, viewports, and product conventions. | Responsive layout rules and stable dimensions. | Real content and boundary states fit without incoherent overlap or hidden commands. | Revise hierarchy or support matrix. |
| Composition -> visual system | Audience, tone, subject, brand, differentiation, trust, and familiarity. | Type, color, spacing, surface, media, icon, and motion decisions. | Choices form one direction and reinforce rather than obscure the task. | Simplify, adapt, or return to product/design authority. |
| Visual system -> implementation | Current architecture, components, tokens, data/state ownership, assets, and build constraints. | Working repository-native interface. | Behavior and design decisions survive code without unauthorized parallel primitives. | Reuse/migration or implementation revision required. |
| Implementation -> rendered evidence | Real browser, data fixtures, viewports, input modes, runtime, and check plan. | Screenshots, accessibility/DOM evidence, interaction results, runtime diagnostics, and review. | Claim-capable checks and human review support the bounded state. | Fix, narrow, reject, or route. |
| Rendered evidence -> accepted experience | Current source/diff, state matrix, counterevidence, risks, recovery, and owners. | Proceed, scoped proceed, revise, reject, or escalation decision. | Evidence depth matches user consequence and policy. | Acceptance remains blocked or limited. |

The pipeline fails early. A refined visual system cannot repair a workflow no owner selected. An accessible name cannot make the wrong command safe. Responsive CSS cannot compensate for omitted error recovery. A visual regression cannot prove business semantics. Each conversion must earn the next.

**Operational principles**

1. **Design the user task, not a generic page category.** A dashboard for repeated incident response needs different density, navigation, and interruption handling than a venue page or game.
2. **Reuse current product language deliberately.** Existing tokens and components preserve familiarity and maintenance when they remain fit. Diverge only for a named user or product reason with an owned migration boundary.
3. **Treat states as first-class composition inputs.** Loading, empty, partial, error, disabled, permission, offline, success, and recovery can change hierarchy and space. Do not bolt them onto the happy path later.
4. **Treat accessibility as interaction behavior.** Semantic elements, accessible names, focus, keyboard operation, status communication, contrast/content, zoom, motion preferences, and assisted use need evidence appropriate to the product.
5. **Choose one visual point of view.** Distinctiveness comes from coherent hierarchy, type, color roles, imagery, spacing, density, and motion. It does not require novelty in every component.
6. **Match expression to product mode.** Operational tools favor scanability, restraint, predictable controls, and stable density. Branded and object-focused pages foreground the subject. Games can be expressive and animated when gameplay remains legible.
7. **Use familiar controls where they reduce learning.** Icons, toggles, segmented controls, tabs, menus, sliders, and text commands have different semantic jobs. An unusual shape must not hide a common action.
8. **Make responsive behavior structural.** Use stable grid tracks, aspect ratios, min/max constraints, container rules, wrapping, and content-aware composition rather than one desktop canvas with emergency media queries.
9. **Use media to reveal the real subject.** Product/place/object/gameplay images should be inspectable. Atmospheric media is insufficient when users need to understand the thing itself.
10. **Observe actual pixels and interaction.** Source, types, and tests are necessary but cannot establish canvas visibility, asset framing, text fit, overlap, focus order, or motion behavior alone.

**Visual direction without dogma**

| principle | useful interpretation | misuse to reject |
| --- | --- | --- |
| Bold direction | Make a small set of memorable, audience-relevant choices and execute them consistently. | Maximal decoration regardless of task, density, trust, or performance. |
| Refined restraint | Use hierarchy, spacing, type, color roles, and detail precisely. | Generic defaults, empty beige surfaces, or lack of a product signal. |
| Distinctive typography | Choose readable type with character appropriate to content and product. | Breaking established brand/system, poor glyph coverage, slow loading, or overflow merely to avoid a common font. |
| Cohesive color | Define semantic and expressive roles with adequate state distinction. | One hue family everywhere, trend-driven gradients, inaccessible contrast, or color-only status. |
| Purposeful motion | Explain change, focus attention, or create fitting character. | Blocking input, animating layout unpredictably, ignoring reduced motion, or scattering effects. |
| Unexpected composition | Create subject-appropriate hierarchy through asymmetry, overlap, rhythm, or density. | Occluding content, breaking reading/focus order, or forcing brittle absolute coordinates. |
| Rich visual detail | Use textures, borders, shadows, imagery, or depth to support the direction. | Decorative orbs, stock atmosphere, nested cards, and effects unrelated to subject or task. |

The local skill's call for boldness is an inspiration default, not a universal product law. A quiet operations console can be more intentional than a dramatic hero when compact scanning, familiar commands, and stable state are the design problem.

**Verification modes and blind spots**

| mode | strongest use | blind spot | complement when consequential |
| --- | --- | --- | --- |
| Component/unit interaction test | Local state transitions, events, labels, and deterministic behavior. | Browser layout, integration, focus sequence, actual assets, and product task. | Browser flow and rendered states. |
| Semantic/static check | Markup, types, lint rules, token or policy constraints. | Dynamic announcements, visual order, user understanding, and layout. | Keyboard, browser, and human review. |
| Automated accessibility scan | Detectable semantic and contrast classes in rendered state. | Full usability, appropriate names, focus logic, content, and all assistive technologies. | Manual keyboard/semantic review and targeted assisted testing. |
| Screenshot/visual regression | Pixel/layout change for named state and viewport. | Interaction semantics, off-screen states, causal intent, and invisible accessibility tree. | User-flow and DOM/accessibility evidence. |
| Browser end-to-end test | Integrated navigation, data state, recovery, and user-visible outcome. | Aesthetic coherence, unsupported variants, and all human needs. | Visual review, state matrix, and performance evidence. |
| Performance/profile trace | Runtime cost and timing under a frozen workload. | Experience correctness, visual fit, other devices, and owner value judgment. | Functional/visual equivalence and target policy. |
| Designer/user/owner review | Context, hierarchy, trust, content, tradeoffs, and acceptance. | Hidden technical defects, reviewer bias, and unreproducible environment. | Captured technical and rendered evidence plus dissent. |

Choose the least costly bundle that can expose the pending consequential failure. More checks are not automatically independent: a component story and screenshot can share the same unrealistic fixture and miss the same empty state.

**False-quality checks**

Reject or revise an interface claim when:

- the page category or aesthetic was selected before the user task and product mode;
- the requested app is replaced by a landing page or explanatory marketing surface;
- loading, empty, error, permission, disabled, or recovery behavior is material but absent;
- controls look interactive without correct semantics, names, states, focus, and commands;
- nested cards, pill-shaped text controls, or decorative sections weaken hierarchy and scanability;
- text, content expansion, zoom, or long words overflow or occlude other UI;
- one viewport, browser, ideal fixture, or pointer input is generalized to all supported use;
- motion blocks interaction, moves layout incoherently, or ignores required preferences;
- media obscures the actual subject or fails to render under target conditions;
- source review or a build result is reported as proof of visual quality;
- a quantitative target is copied from the seed or template without owner, workload, and measurement;
- a new design system appears without consumer, migration, and ownership evidence.

Good operational example: a repeated-action admin surface keeps compact navigation and familiar icon controls, defines async/error/retry states, uses stable table dimensions, and is verified under keyboard plus narrow/wide browser states.

Bad generic example: a page uses an oversized hero, gradient headline, decorative cards, and explanatory copy for a workflow that users need to operate immediately. Static polish has replaced the product.

Conditional expressive example: a game or venue page can use full-bleed imagery, unusual type, and orchestrated motion when the subject appears in the first viewport, gameplay/content remains legible, reduced-motion and loading states work, and the next section remains discoverable.

**Second-order consequences**

The user journey is an intermediate representation consumed by components, data queries, content, accessibility semantics, responsive layout, tests, telemetry, and future agents. A missing state multiplies ambiguity downstream. A stable state contract lets each layer specialize without losing the reason for the interface.

The resulting evidence is also an invalidation graph. A content expansion reopens text-fit screenshots; a token change reopens affected components; a workflow change reopens state and navigation tests; a browser or asset change reopens rendering; a policy change reopens accessibility or authorization acceptance. Unrelated verified states can remain intact.

Frontend quality is therefore not a single score or static finish. It is controlled coherence across behavior, perception, context, and operation, with explicit contradiction, recovery, and renewal when one premise changes.

## Local Corpus Source Map

The local corpus contains one short design-guidance body at two path identities. Because the bodies are hash-identical, read one completely for meaning and retain both for archive/current provenance. The map routes decisions and cautions; it does not copy the source or promote its broad techniques into target requirements.

**Content-family inventory**

| family | local paths | observed SHA-256 | read strategy | authority boundary |
| --- | --- | --- | --- | --- |
| Frontend design skill | `agents-used-monthly-archive/claude-skills-202603/plugins/frontend-design/SKILL.md`; `claude-skills/plugins/frontend-design/SKILL.md` | `d39adf3a983de7dafc75991590d54f091755f7e4163d5a5ed085ecd719157184` | Read one 42-line body completely; preserve both path/package identities. | Creative design guidance and invocation intent, not product behavior, browser support, accessibility sufficiency, or outcome measurement. |

Hash equality establishes matching observed bytes. It does not establish that both paths have the same loader, plugin metadata, license context, owner, activation state, or precedence. Inspect surrounding package context only when one of those questions affects use.

**Complete source-section routing**

| source section | load when the pending question is | useful contribution | required caution and next evidence |
| --- | --- | --- | --- |
| YAML frontmatter and opening | Whether the skill is intended for the task and what output it promises. | Names components, pages, applications, production-grade function, visual quality, and avoidance of generic output. | Invocation intent does not authorize a redesign or prove production readiness; inspect user request, repository, and target checks. |
| `Design Thinking` | How to establish purpose, audience, tone, constraints, and differentiation before coding. | Pushes the agent to choose a clear conceptual direction and connect implementation complexity to that direction. | The supplied tone list is a search space, not a checklist; product category and existing design system can constrain or replace a new direction. |
| `Frontend Aesthetics Guidelines` | How typography, color, motion, composition, backgrounds, and detail can express the selected direction. | Supplies critique vocabulary and pressure against generic, trend-convergent output. | Each technique needs readability, glyph/content, performance, accessibility, responsive, asset, and maintenance evidence in the target. |
| Final implementation reminder | Whether visual ambition should be reduced automatically. | Preserves the principle that expressive and restrained designs both require precise execution. | Ambition must not bypass user task, state completeness, policy, or rendered verification. |

The source is small and conceptually coupled, so a new durable design task should read it completely. Heading search is sufficient only for locating a known quotation or comparing a changed version; it should not replace the full argument.

**Heuristic-to-operational translation**

| local heuristic | preserved intent | operational boundary | capable target evidence |
| --- | --- | --- | --- |
| Understand purpose and users. | Design should solve a real problem for a known audience. | Do not infer product intent, content, or authority from a page category. | Product/user decision, workflow contract, current usage evidence, and task walkthrough. |
| Commit to a clear tone. | Coherence improves when choices reinforce one concept. | Existing brands/design systems and operational familiarity may govern tone. | Direction statement, alternatives, owner review, rendered state comparison. |
| Respect constraints. | Framework, performance, and accessibility shape the design. | Constraints include content, data, browser, input, localization, security, ownership, and release policy. | Target manifests/source, state matrix, browser/accessibility/performance evidence. |
| Make the experience memorable. | A subject-appropriate distinctive signal can prevent generic output. | Memorability cannot obscure commands, trust, reading order, or real product subject. | First-viewport and task review with actual media/content and required states. |
| Avoid generic fonts automatically. | Typography should be intentional rather than an unexamined default. | Established product type, readability, glyph coverage, loading, licensing, and layout can justify common or system fonts. | Font loading, content/locale matrix, text fit, performance, and design-system authority. |
| Use dominant color and sharp accents. | Color roles should feel deliberate and hierarchical. | Accessibility, semantic states, brand, dark/light modes, and color blindness constrain palettes. | Token/state audit, contrast and non-color cues, screenshots, owner review. |
| Prefer high-impact motion moments. | Motion should support hierarchy and character instead of random noise. | Input, reduced-motion, low-power, layout stability, cancellation, and task frequency matter. | Browser interaction, preference state, timing/profile, and no-blocking check. |
| Explore asymmetry, overlap, and unusual composition. | Layout can create a distinctive reading rhythm. | DOM/focus order, content occlusion, responsive range, zoom, and stable dimensions must survive. | Viewport/container/content matrix plus keyboard/read-order review. |
| Add texture, depth, and atmosphere. | Surfaces can communicate subject and mood beyond flat defaults. | Decoration must not become bokeh/orb filler, obscure the real object, weaken contrast, or impose excessive cost. | Actual asset rendering, subject legibility, performance, and visual critique. |
| Match implementation complexity to vision. | Refined minimalism and maximalism each require appropriate craft. | Complexity needs maintainable ownership and measurable user value; restraint is not underdesign. | Diff/architecture review, project checks, interaction evidence, and ongoing owner. |

**Target corpus to inspect before implementation**

The local skill is only one input. For an established repository, inspect the complete relevant portions of:

- user and repository instructions, including frontend and accessibility requirements;
- routes, shells, navigation, layout primitives, and state/data boundaries;
- current component library, token/theme definitions, icon library, typography, and media conventions;
- existing page and state behavior in a real browser;
- component/unit/integration/end-to-end tests and visual or story fixtures;
- supported viewport, container, browser, input, localization, and content policies;
- build, asset, rendering, and performance constraints;
- current design, content, product, and domain owner decisions.

Do not load every file indiscriminately. Select complete semantic modules and state fixtures that can change the pending experience decision, and preserve why other candidates were excluded.

**Observed tensions and synthesis**

| local guidance pressure | target-system counterpressure | synthesis |
| --- | --- | --- |
| Choose a bold new visual direction. | Mature product has a governed design system and repeated expert workflows. | Make product-specific hierarchy or content decisions inside the current system; diverge through an owned migration only. |
| Avoid familiar generic type choices. | Brand, native platform, internationalization, loading, or accessibility requires established typography. | Require intentional type roles and fit, not novelty for its own sake. |
| Add motion and surprising hover states. | Touch, keyboard, reduced motion, high-frequency use, and latency limit animation. | Use motion for causality or one meaningful moment with complete input/preference states. |
| Use overlaps and grid-breaking composition. | Operational content, responsive text, zoom, and reading/focus order need stability. | Reserve expressive composition for subject-appropriate bands; keep controls and data structurally predictable. |
| Create atmosphere with visual effects. | Users need to inspect the actual product, place, object, state, or gameplay. | Foreground real subject media and use atmosphere only when it improves context without hiding detail. |
| Match complexity to visual ambition. | Repository maintenance and load/runtime cost constrain complexity. | Treat maintainability and performance as part of execution quality, not external objections to design. |

**Retrieval profiles**

| profile | required local reads | safe stopping point |
| --- | --- | --- |
| Focused correction | Current user/repository rules, affected component/state, governing token or design contract, and focused checks. | Existing authority plus rendered regression settles the narrow change. |
| Standard new experience | Complete local skill, complete request/context, relevant routes/components/tokens/content, target states, and verification surfaces. | Workflow, direction, implementation, and evidence are reviewable. |
| Design-system change | Standard reads plus consumer inventory, token/component dependency graph, migration/history, documentation, and governance. | Supported consumers, rollout, rollback, and ownership are explicit. |
| Global visual review | Complete applicable product surface/state inventory, current system, cross-page relationships, and explicit screenshot/browser matrix with checkpoints. | Cross-surface consistency and user-critical flows pass. |
| Historical comparison | Both path/package contexts, relevant previous versions, design artifacts, and implementation history. | Temporal claim separates observed changes from inferred rationale. |

**Map integrity rules**

1. Verify both paths and capture identities before relying on the family.
2. Read one distinct body completely for every new durable design task.
3. Preserve duplicate provenance without multiplying substantive confidence.
4. Treat tone and technique lists as design search space rather than requirements.
5. Reconcile broad aesthetic advice with target product mode and current conventions.
6. Bind selected guidance to real content, states, semantics, viewports, and browser evidence.
7. Rebuild the map after source hash, product system, or heading changes.
8. Escalate to broader target reads when the decision affects shared components or global consistency.

Good retrieval: an agent building a branded venue page reads the whole skill, inspects existing brand assets and page shell, selects one editorial direction, and verifies real imagery plus mobile states. Bad retrieval: the agent copies every listed aesthetic technique into an operations dashboard. Conditional use: a team may standardize a distinctive type or motion rule after accessibility, performance, consumer, and owner evidence makes it a target policy.

## External Research Source Map

No external query or page retrieval was performed. Every URL is preserved exactly from the seed with state `unrefreshed_no_browse`. The locally observed fact is that the seed associates each URL with a role; current content, version, authority, route stability, and applicability are unknown until a future authorized refresh.

**Decision-bound external queue**

| external_source_url_value | seed role | trigger to refresh | primary question | required local closure | current state |
| --- | --- | --- | --- | --- | --- |
| `https://react.dev/learn` | Component-driven frontend behavior reference. | A React component, state, rendering, composition, hydration, or framework convention is version-sensitive and can change implementation. | For the installed React/toolchain version, what contract governs the exact component or rendering behavior, and which behavior belongs to surrounding frameworks? | Compare package and wrapper identity, inspect target source, and reproduce positive plus failure behavior in the application. | `unrefreshed_no_browse` |
| `https://threejs.org/docs/` | Visual scene API documentation. | A 3D scene, renderer, asset, animation, disposal, interaction, or browser behavior affects the requested experience. | Which versioned Three.js API and renderer assumptions govern the target scene, lifecycle, and supported browsers? | Match dependency/version, build a controlled target fixture, and verify nonblank pixels, framing, interaction, cleanup, fallback, and performance. | `unrefreshed_no_browse` |
| `https://docs.github.com/actions` | Delivery verification and automation reference. | Frontend screenshot, browser, build, artifact, deployment, permission, matrix, or cancellation behavior is moved into GitHub Actions. | Which official workflow contract governs the exact runner, permission, artifact, matrix, and failure semantics used? | Test a safe repository fixture under the selected runner/configuration and preserve logs plus rejection behavior. | `unrefreshed_no_browse` |

These are hypotheses about where primary evidence may live. They do not assert that a feature exists, that the root path is stable, or that documentation describes the installed environment.

**Local-first and external-first routes**

| situation | first move | external move | stop condition |
| --- | --- | --- | --- |
| Existing component behavior is clear | Read target source, types, tests, and browser state. | Do not browse unless current framework support changes the decision. | Local evidence settles the bounded claim without a portability assertion. |
| Known package upgrade caused a regression | Freeze package lock, wrappers, browser, and exact symptom. | Retrieve official release/migration/API material for those versions. | Change is confirmed or remains version-ambiguous with an owner route. |
| New Three.js scene is requested | Define gameplay/product need, target browsers, assets, interaction, fallback, and performance evidence locally. | Retrieve only exact versioned APIs needed for the design. | Real target canvas passes pixel, lifecycle, input, and fallback gates. |
| New hosted visual gate is needed | Define repository acceptance, data/security, browser matrix, and artifact retention. | Retrieve feature-specific workflow and runner documentation. | Safe fixture demonstrates success and intentional failure under the repository policy. |
| Stack comparison is exploratory | Record product requirements, maintenance, accessibility, rendering, and performance criteria. | Time-box primary-source candidate discovery. | No implementation contract changes until selected candidates are reproduced. |
| Required hosted/GPU/credential environment is unavailable | Preserve the blocked claim and consequence. | Do not infer target behavior from documentation alone. | Access changes, scope narrows with owner acceptance, or the route is rejected. |

**Source-quality ladder**

| source class | strongest use | limitation |
| --- | --- | --- |
| Versioned official API/specification/manual | Establish publisher-supported contract for a named version or date. | Does not prove package integration, wrapper, browser, configuration, or product fit. |
| Official release notes, migration guide, or maintained source history | Explain changed behavior and compatibility boundaries. | Unreleased, unresolved, or implementation detail may not be supported policy. |
| Installed package source, types, lockfile, help, or generated output | Establish actual local capability and integration shape. | Can omit public support guarantees and runtime/browser effects. |
| Controlled component/browser/scene fixture | Establish causal behavior for selected state and environment. | Does not prove all content, devices, browsers, or production workloads. |
| Representative product workflow | Establish bounded applicability to the actual interface. | Remains scoped to selected users, states, content, and conditions. |
| Community article, example, or discussion | Generate vocabulary, alternatives, and edge-case hypotheses. | Not decision authority; confirm through primary and target evidence. |

**External evidence promotion protocol**

1. State the blocked frontend claim and the consequence of being wrong.
2. Confirm browsing authorization, sensitive-data boundaries, and acceptable source classes.
3. Record exact query, access date, publisher, direct URL, title, version, and relevant section.
4. Paraphrase only the narrow contract needed, including prerequisites and explicit limitations.
5. Match the installed package, wrapper, build tool, browser/runner, and configuration.
6. Reproduce a positive and negative case in a safe fixture or record why target authority is unavailable.
7. Compare the result with product requirements, repository conventions, current implementation, and rendered behavior.
8. Decide adopt, adapt, reject, no change, or escalation required.
9. Name the release, package, wrapper, browser, runner, repository, or policy change that invalidates the result.

Finding a plausible page completes retrieval only. The refresh completes when the extracted external claim changes or confirms a bounded local decision under explicit applicability.

**Refresh result card**

| field | required content |
| --- | --- |
| `research_identifier` | Stable link to the interface claim or unresolved state. |
| `trigger_and_consequence` | Why current producer behavior matters to user, release, compatibility, or evidence. |
| `retrieval_identity` | Query, direct primary source, publisher, date, version, section, and source class. |
| `narrow_claim` | Bounded paraphrase with conditions and exclusions. |
| `target_identity` | Application revision, dependencies, wrapper/build, browser/runner, configuration, state, and content. |
| `reproduction` | Positive, negative, conflicting, unavailable, or not-applicable result. |
| `decision_effect` | Requirement, component, scene, test, workflow, or explicit no-change outcome. |
| `counterevidence` | Local source, rendered behavior, version difference, product rule, or owner constraint. |
| `invalidation` | Producer/local/environment/policy change that reopens the result. |
| `owner_and_next_action` | Accountable reviewer, follow-up mechanism, and stop condition. |

**Research failure states**

| failure | response |
| --- | --- |
| URL unavailable or moved | Search within the official publisher only under authorization, retain old pointer historically, and do not invent continuity. |
| Current page lacks version identity | Record access date, narrow the claim, and rely on installed/target reproduction for applicability. |
| Official contract conflicts with installed behavior | Verify versions, wrappers, flags, bundler, and browser; preserve both and route compatibility. |
| Example code appears sufficient | Read its surrounding primary contract and reproduce the relevant failure state; examples can omit production boundaries. |
| Community guidance is the only source | Keep it as a hypothesis and require target fixture plus owner review. |
| Hosted or GPU/browser test cannot run safely | Preserve blocked evidence and define the required authorized environment. |
| External result does not affect the decision | Close or retire the item instead of adding a ceremonial citation. |

Good React research use: a concrete hydration or state behavior differs after a known package upgrade. The engineer freezes versions, retrieves the exact official contract, reproduces the before/after state in the target wrapper, and updates the component check.

Good Three.js research use: a scene renders blank on one supported browser. The engineer records renderer/canvas/asset state, consults the exact versioned API, checks pixels and console/graphics state, and verifies cleanup plus fallback after correction.

Bad research use: "React and Three.js documentation prove this interface is production-grade." Documentation roots cannot establish product workflow, accessibility, visual framing, actual browser behavior, or performance.

Conditional exploration: a team may compare scene libraries or CI visual-test approaches before selection. The result is a candidate matrix, not an adopted stack, until target build, behavior, maintenance, security, accessibility, and performance evidence exists.

**Queue lifecycle**

- Prioritize a release blocker or consequential mismatch before a planned upgrade or exploratory item.
- Assign one owner and one decision effect to every active question.
- Close an item when local source and fixtures settle it more directly.
- Retire a pointer when the integration or trigger disappears, preserving historical rationale.
- Refresh event-driven claims after relevant producer or installed-version changes; do not invent periodic schedules.
- Preserve prior retrieval identity when guidance changes so earlier decisions remain interpretable.

The external map is a queue of falsifiable future questions, not current source attribution. Success includes the decision not to browse when the target code and browser evidence already answer the narrower question.

## Anti Pattern Registry Table

Use the registry to locate the earliest failed premise and change what the workflow may claim or ship. Do not use it to shame stylistic preference. A matched entry should identify the user consequence, affected states, evidence that remains valid, and the gate that releases the block.

**Common containment and recovery**

1. Stop acceptance of every experience claim that depends on the suspected defect.
2. Preserve the exact user state, content, viewport, input, source, screenshot, DOM/accessibility, and runtime evidence needed to reproduce it.
3. Identify the earliest stage: product fit, source authority, state model, semantics, composition, visual system, implementation, asset/runtime, verification, or handoff.
4. Select the smallest mechanism capable of distinguishing the leading failure from alternatives.
5. Correct the premise or route to a stronger owner; do not hide the symptom with overflow, extra decoration, or a special-case position.
6. Replay the affected positive and negative states, then reopen only dependent surfaces.
7. Add a shared primitive or regression fixture when the mechanism is recurring, consequential, and safe to encode.

**Cross-cutting frontend anti-pattern registry**

| anti_pattern_failure_name | stage and mechanism | observable signal | user or system consequence | safer default and containment | release evidence |
| --- | --- | --- | --- | --- | --- |
| `context_free_visual_direction` | Product fit: agent selects a fashionable page style before reading user, product, and current system context. | Direction could fit any company after replacing the logo and copy. | Generic output, poor trust, workflow mismatch, and unnecessary redesign. | Stop visual commitment; write task/product statement and inspect current design system. | Reviewer can connect each distinctive choice to subject, user, or workflow. |
| `application_replaced_by_landing_page` | Product form: requested tool is delivered as marketing hero and explanatory sections. | Primary commands/data are below promotional copy or absent. | User cannot perform the requested work on first screen. | Build the actual operating surface; reserve hero composition for a genuine offer or branded content page. | User-flow fixture completes the primary task without marketing detour. |
| `source_authority_blending` | Evidence: local guidance, public pointer, design preference, and target fact share one authoritative voice. | No distinction among source, observation, inference, and owner decision. | Unsupported redesign or behavior claim becomes hard to challenge. | Type claims and bind target decisions to current authority. | Claim-to-source audit and explicit unknowns pass. |
| `duplicate_design_source_voting` | Evidence weighting: two hash-equal skill paths are counted as independent support. | Several citations share exact bytes. | Confidence increases without another observation model. | Treat one content family substantively and retain paths for provenance. | Hash ledger and corrected rationale. |
| `happy_path_static_mockup` | State model: only populated/default state is designed and implemented. | Loading, empty, partial, error, permission, disabled, or recovery fixtures are missing. | Real data conditions create blank, unstable, or stuck interfaces. | Define applicable state graph before polish and allocate stable composition. | State matrix plus rendered and behavioral checks. |
| `client_failure_without_recovery` | Runtime behavior: auth, network, hydration, asset, or mutation error ends in a dead screen. | Error text or console event exists without safe next action. | User loses work or cannot continue. | Preserve context, explain state, offer authorized retry/back/correction, and instrument outcome. | Fault fixture reaches expected containment and recovery. |
| `nested_card_hierarchy_collapse` | Composition: page sections and controls are wrapped in cards inside cards. | Borders, shadows, and equal radii create several competing containers. | Hierarchy, density, and scan path become unclear. | Use unframed page bands/layout; reserve cards for repeated items, modals, or genuinely framed tools. | Rendered review identifies one clear structural hierarchy. |
| `rounded_text_control_overuse` | Control semantics: rounded rectangles with text replace familiar icons or appropriate controls. | Undo, save, zoom, formatting, toggle, mode, or options use verbose pills. | Toolbars expand, scanning slows, and semantics become inconsistent. | Use established icon/control types with accessible names and tooltips where unfamiliar. | Control audit plus keyboard/accessible-name checks. |
| `feature_explanation_inside_product_ui` | Content: interface narrates its features, styling, shortcuts, or how to use itself instead of exposing clear controls. | Visible copy explains obvious functionality or aesthetic intent. | Product becomes noisy and commands remain indirectly expressed. | Make controls and states self-evident; place help only where user consequence requires it. | Content review shows every visible instruction serves a real task gap. |
| `generic_card_grid_template` | Visual system: every page becomes heading, gradient, and interchangeable cards. | Composition and content remain unchanged across product types. | Subject identity and workflow priorities disappear. | Choose product-specific hierarchy, density, media, and interaction patterns. | Blind comparison can distinguish the product without relying only on logo. |
| `one_note_palette_system` | Color: one fashionable hue family dominates surfaces, states, accents, and data. | Status and hierarchy differ mainly by saturation. | Weak semantic distinction, trend convergence, and possible contrast issues. | Define neutral, semantic, content, and accent roles appropriate to product and modes. | Token/state and contrast/non-color-cue review. |
| `decorative_orb_background_filler` | Background: gradients, bokeh, blobs, or floating orbs are added without subject or interaction purpose. | Decoration could be removed without changing meaning and may obscure content. | Generic atmosphere, poor contrast, and rendering cost. | Use real subject media, material texture, structural pattern, or restrained surface treatment with rationale. | Visual critique and performance/contrast checks support retention. |
| `hero_subject_signal_missing` | Branded/object page: product, place, person, or offer appears only as small nav/eyebrow text. | First viewport could describe an unrelated brand. | Weak identity and delayed user orientation. | Make literal subject/name/offer a first-viewport signal and expose a hint of subsequent content. | Desktop/mobile first-viewport review with real media/content. |
| `split_card_hero_composition` | Hero layout: main experience is divided into text and media cards or text itself is placed in a decorative card. | Hero reads like a component demo rather than an immersive subject. | Reduced impact and generic layout. | Use relevant full-bleed media/scene with overlaid hierarchy when a hero is genuinely required. | Subject remains inspectable and text legible at target viewports. |
| `atmospheric_media_hides_subject` | Asset selection: image is dark, blurred, cropped, stock-like, or purely atmospheric when inspection matters. | User cannot see the actual product, place, object, state, gameplay, or person. | Misleading presentation and poor decision support. | Use direct high-information media, generated assets when authorized, or a truthful fallback. | Asset review confirms real subject visibility and provenance. |
| `asset_failure_without_layout_fallback` | Runtime/media: missing, slow, denied, or invalid asset collapses composition. | Broken image, zero-height media, layout jump, or unreadable text appears. | Primary content or command is lost. | Stable aspect/dimensions, accessible fallback, loading/error state, and retry only when useful. | Failed-asset fixture preserves hierarchy and task. |
| `blank_or_unframed_3d_scene` | 3D: canvas exists but pixels are blank, camera framing is wrong, assets fail, or UI overlays conflict. | Source contains Three.js but screenshots/canvas pixel checks show no intended scene. | Expensive nonfunctional primary experience. | Verify renderer, size, camera, lights/materials, assets, animation, input, cleanup, fallback, and real pixels. | Desktop/mobile screenshots, nonblank pixel test, interaction and runtime checks. |
| `motion_without_causal_role` | Motion: effects are scattered, block input, shift layout, or ignore required preferences. | Many hover/reveal animations compete or delay repeated actions. | Disorientation, latency, reduced accessibility, and unstable tests. | Use a few moments for continuity or emphasis; support reduced motion and interruption. | Preference/input/browser checks and visual review. |
| `responsive_shrink_only_layout` | Responsive composition: desktop geometry is scaled or hidden without rethinking hierarchy. | Dense controls overflow, text shrinks excessively, or columns become unusable. | Primary tasks fail on narrow containers or zoom. | Define container/viewport transformations, wrapping, stable tracks, and priority changes. | Required viewport/content/zoom matrix passes. |
| `fixed_copy_layout_assumption` | Content resilience: layout depends on short sample labels or ideal numbers. | Long words, localization, errors, empty state, or large values overlap/clip. | Information and commands disappear for real content. | Test representative extremes, wrap/reflow, constrain media, and size controls stably. | Long-content screenshots and no-overlap/text-fit checks. |
| `viewport_scaled_typography` | Typography: font size tracks viewport width directly instead of semantic role and container. | Type changes unpredictably across wide screens and compact panels. | Poor hierarchy, readability, and text fit. | Use stable role-based sizes with breakpoint/container adaptation only when necessary. | Typography audit across content and containers. |
| `unstable_control_dimensions` | Component layout: icon buttons, counters, boards, grids, tiles, or toolbars resize with labels/state. | Hover, loading, counts, or icons shift surrounding UI. | Misclicks, visual jitter, and fragile screenshots. | Define stable dimensions/aspect/grid constraints and fit dynamic content inside them. | State-transition screenshot and interaction checks. |
| `visual_order_semantic_order_split` | Accessibility/composition: CSS placement or overlap creates a reading/focus sequence different from visual hierarchy. | Tab or assistive reading jumps incoherently. | Users cannot understand or operate the intended flow. | Align DOM, visual, reading, and focus order; use explicit focus only for real state transitions. | Keyboard and accessibility-tree walkthrough. |
| `icon_without_accessible_name` | Control semantics: icon-only action relies on visual recognition or hover tooltip alone. | Accessible name missing, duplicated, or state not announced. | Nonvisual and voice users cannot identify or operate command. | Use semantic element, programmatic name, state, focus, and optional tooltip. | Accessibility-tree and keyboard checks. |
| `color_only_state_communication` | Visual semantics: status or selection differs only by color. | Shape, label, icon, or text provides no second cue. | Users miss critical state under color-vision or display conditions. | Add meaningful non-color indication without duplicating noise. | State review under grayscale/contrast and semantic inspection. |
| `renderless_source_acceptance` | Verification: interface is called polished from source, typecheck, or build only. | No actual browser, screenshot, interaction, or state evidence exists. | Asset, overflow, canvas, focus, and composition defects escape. | Start local app when required and inspect target browser states. | Captured rendered evidence plus behavior/accessibility gates. |
| `single_viewport_confidence` | Verification: one screenshot stands for all supported containers/content. | No narrow, wide, dynamic-state, or content-extreme samples. | Hidden responsive failures reach users. | Define risk-based matrix and inspect all material transformations. | Matrix reconciliation and no-claim boundary. |
| `screenshot_only_accessibility_claim` | Verification: pixels are used to infer semantics, keyboard, and announcements. | Screenshot looks correct while accessibility tree/focus fails. | Visual acceptance launders interaction barriers. | Combine pixels with DOM/accessibility, keyboard, and targeted assisted evidence. | Required multimodal checks pass. |
| `visual_regression_as_design_authority` | Verification: baseline screenshot is treated as inherently correct. | Intended fix is rejected or existing defect is preserved because pixels changed. | Stale design becomes self-validating. | Review baseline authority and classify intended, unintended, and unresolved diffs. | Owner-approved visual contract and updated bounded baseline. |
| `new_design_system_without_migration` | Architecture: page introduces parallel tokens/components without consumer and ownership plan. | Similar primitives differ across surfaces and no authority governs them. | Drift, bundle/maintenance cost, inconsistent behavior. | Reuse/adapt current system or execute an explicit versioned migration. | Consumer inventory, compatibility, rollout/rollback, and owner acceptance. |

**Severity and handling**

| class | meaning | default response |
| --- | --- | --- |
| Advisory | A contextual visual choice could be stronger, but current reversible task remains usable. | Record rationale and refine without inventing a blocker. |
| Visual-review blocking | Hierarchy, coherence, subject visibility, or responsive fit is materially wrong. | Revise affected states before presentation acceptance. |
| Behavior blocking | Primary task, state transition, accessible operation, recovery, or required viewport fails. | Stop completion and implementation promotion until claim-capable evidence passes. |
| High-assurance stop | Regulated content, destructive action, security/privacy, critical accessibility, or production risk lacks required evidence or authority. | Route to domain mechanisms and accountable owner; no local aesthetic override. |

**Registry admission and maintenance**

Add an entry only when the mechanism is observed or strongly supported, recurs or carries serious consequence, has a stable signal, and offers a safer route plus replayable evidence. Preserve an unclassified category for novel failures. A registry entry passes when an affected target or controlled fixture shows that its gate rejects the defect and releases only after the correct premise changes.

Good recovery: mobile error copy pushes the retry command under a fixed-height panel. The agent removes the brittle height, defines a stable action region, adds long-error and narrow fixtures, and verifies focus/recovery. Bad recovery: hide overflow and shorten the sample text. Conditional overlap: a branded editorial page can overlap image and type when real content, reading order, contrast, zoom, and narrow rendering remain coherent.

The registry feeds components, tokens, state fixtures, browser checks, and design review. Repeated asset failures improve fallback primitives; repeated clipped actions improve layout contracts; repeated source-only acceptance improves rendered gates. Retire rules whose cost exceeds the distinct failure they prevent.

## Verification Gate Command Set

`verification_gate_command_set`: Select gates by evidence population and pending claim. Run cheap identity and structural checks first, repository-native behavior checks next, and actual browser/rendered review before making visual, accessibility, responsive, media, canvas, or interaction claims.

**Gate dependency order**

| gate | property checked | evidence produced | what a pass does not prove | failure response |
| --- | --- | --- | --- | --- |
| A. Environment and ownership | Correct root, active instructions, authorized output paths, current owner, required tools. | Preflight and path record. | Product intent or source freshness. | Stop before writes or side effects. |
| B. Frozen identity | Seed/source hashes, target revision, dirty state, dependencies, design-system and content identity. | Reproducible input manifest. | That inherited guidance or current design is correct. | Mark stale, reconcile, and never guess around mismatch. |
| C. Packet/reference integrity | Exact headings/questions/fields, uniqueness, expansion, source boundaries, and hygiene. | Focused parser result. | Interface quality or target behavior. | Fix atomic packet/reference section before continuing. |
| D. Project source and build | Repository-native lint, type, static, unit, build, asset, and schema properties. | Source/build evidence under target config. | Actual pixels, integrated workflow, focus, or media framing. | Repair source/config or narrow claim. |
| E. Interaction behavior | User actions, state transitions, recovery, side effects, navigation, and integration. | Component/integration/end-to-end results. | Visual coherence, all viewports, or assisted use. | Reopen state contract or implementation. |
| F. Accessibility and input | Semantics, names, states, focus, keyboard, preferences, and target assisted evidence. | Automated and manual mode results. | Product fit or every disability/user context. | Block affected task or route to stronger review. |
| G. Rendered composition | Actual pixels, text fit, overflow, layout stability, assets, responsive hierarchy, and visual direction. | State/viewports screenshots and critique. | Invisible semantics or production performance. | Revise composition and rerender exact states. |
| H. Specialized media/3D | Nonblank canvas/media, framing, loading/failure, interaction, lifecycle, fallback, and performance. | Pixel/canvas/runtime and browser evidence. | Every GPU/device/workload. | Fix or fall back; no source-only acceptance. |
| I. Quantitative experience | Owner-approved workload, baseline/candidate, timing/resources, equivalence, and uncertainty. | Controlled measurement packet. | Unmeasured users, devices, networks, or future behavior. | Reject or relabel result. |
| J. Handoff and invalidation | Changed paths, evidence, residual gaps, rollback/recovery, owners, and premise changes. | Bounded release decision. | Permanent validity. | Block completion until reconstructable. |

**Current 202607 shared structural checks**

These read-only tests validate shared inventory and hygiene properties without requiring another owner to finish every reference:

```bash
python3 -m pytest -q \
  tests/test_idiomatic_reference_evolution.py::IdiomaticReferenceEvolutionTests::test_inventory_matches_specification \
  tests/test_idiomatic_reference_evolution.py::IdiomaticReferenceEvolutionTests::test_owner_mapping_unique \
  tests/test_idiomatic_reference_evolution.py::IdiomaticReferenceEvolutionTests::test_assignment_manifests_match \
  tests/test_idiomatic_reference_evolution.py::IdiomaticReferenceEvolutionTests::test_packet_content_uniqueness \
  tests/test_idiomatic_reference_evolution.py::IdiomaticReferenceEvolutionTests::test_reference_placeholders_absent
```

The complete module also checks all references, packets, and shared queue rows. While other owners are active it may report external unfinished work. Preserve exact failure population and do not edit another lane to make it green.

```bash
python3 -m pytest -q tests/test_idiomatic_reference_evolution.py
```

**Assignment-focused verifier contract**

After each atomic section and after the complete reread, use the current test module's parsers to assert:

- 26 reference headings retain exact levels, text, and seed order;
- every evolved section is strictly longer than its matching seed section;
- the packet has 26 exact section headings and 260 exact question headings;
- each question has the six required fields in order with nonempty values;
- all 1,560 values are unique both raw and after current context-prefix normalization;
- both outputs are ASCII, end with a newline, have balanced fences/tables, no tabs or trailing whitespace, and no prohibited placeholders;
- immutable seed and mapped local source hashes remain frozen;
- only authorized paths changed.

The focused verifier proves the evolution contract. Complete semantic reread proves that packet conclusions actually inform the reference.

**Scoped diff and immutable-source checks**

```bash
git diff --check -- \
  idiomatic-ref-202607/frontend_design_quality_patterns-20260710.md \
  idiomatic-reference-evolution-work/delta/packets/frontend_design_quality_patterns-20260710-question-packets.md \
  idiomatic-reference-evolution-work/delta/progress.md
```

Capture SHA-256 for the seed, both duplicate skill paths, final reference, and final packet. Equal source hashes prove matching bytes, not truth or applicability.

**Legacy archive verifier**

The original command is preserved only for the 202606 generated archive:

```bash
python3 agents-used-monthly-archive/idiomatic-references-202606/tools/verify_reference_generation.py --stage final
```

Its implementation does not certify the 202607 Delta packet or any target frontend. Report its result as historical archive evidence only.

**Project gate discovery**

This reference cannot name one universal frontend command. Before implementation:

1. Read repository instructions and package/workspace manifests.
2. Inspect existing scripts, CI workflows, test configuration, story/fixture setup, and supported browsers.
3. Identify the real app entry point and dev/preview server behavior.
4. Record which command observes which requirement and whether it writes artifacts or starts a long-lived process.
5. Reuse repository-native runners and fixture conventions before adding a new stack.
6. Start a local server after implementation when the application requires it, verify the actual bound URL, and stop only sessions not needed for user trial.

| pending claim | likely gate family | mandatory rejection question |
| --- | --- | --- |
| Pure state or formatting transformation | Unit/property/type/schema. | Would representative wrong output fail independently of the implementation? |
| Component interaction | Component/browser interaction test. | Are semantic controls, states, events, focus, and failure behavior exercised? |
| Integrated workflow | Browser end-to-end or integration. | Can the user complete and recover through real boundaries? |
| Accessibility | Semantic/static, automated browser check, keyboard/focus, and targeted assisted review. | Does evidence cover the actual task and states rather than one score? |
| Responsive/text fit | Screenshot/DOM geometry across content, container, viewport, and zoom matrix. | Can long/error/dynamic content overlap, clip, or hide commands? |
| Visual direction | Rendered state comparison and experienced critique against stated product direction. | Is the judgment tied to audience/task rather than a generic trend? |
| Asset/media | Network/load/failure fixture, dimensions, alt/content, pixel inspection, and fallback. | Does real subject media render and remain inspectable? |
| 3D/canvas | Browser screenshot, canvas pixel nonblank test, interaction/animation, resize, cleanup, console, and fallback. | Could source execute while canvas remains blank or misframed? |
| Performance | Browser/profile/benchmark under frozen workload with visual/functional equivalence. | Are workload, environment, sample, and uncertainty sufficient? |
| Compatibility | Consumer/browser matrix, build, migration, and rollback. | Do supported old states/consumers still work as promised? |

**Rendered evidence matrix**

For each user-critical surface, record:

| dimension | minimum identity |
| --- | --- |
| State | Default, loading, empty, partial, error, disabled, permission, success, and recovery as applicable. |
| Content | Realistic normal, longest/error, missing media, large values, localization/zoom cases as required. |
| Viewport/container | Named narrow, intermediate, wide, and component-container states based on supported product surfaces. |
| Input | Pointer, keyboard, touch, voice/switch/assistive path as product evidence requires. |
| Browser/device | Target engine/device/configuration rather than a universal sample. |
| Preference | Reduced motion, color/theme, contrast, text scaling, or other supported preferences. |
| Runtime | Network/auth/data/asset/graphics conditions and console errors. |
| Expected result | Task, hierarchy, text fit, focus, feedback, recovery, and no-claim boundary. |

Do not invent three fixed viewport widths merely to fill a table. Derive the matrix from product support, component containers, content pressure, and failure consequence. Stable dimensions and responsive constraints should make intermediate widths unsurprising, but they still need risk-based inspection.

**Browser and screenshot evidence rules**

- Capture the exact URL/route, app revision, fixture/data, state, viewport, device scale, browser, theme, locale, and reduced-motion setting.
- Wait for the intended stable state, not arbitrary delay alone; record pending animations and network dependencies.
- Inspect full page and task-critical crops without hiding overflow or occluded content.
- Check DOM/accessibility evidence separately because pixels cannot prove semantics or focus.
- Record console/page/network errors and asset failures; a pretty screenshot with runtime exceptions is not complete.
- Compare intended versus unintended diffs; a baseline is evidence, not permanent design authority.
- For canvas/3D, verify nonblank meaningful pixels, camera framing, animation/input, resize, assets, cleanup, and fallback at desktop and mobile states.
- Keep screenshots and logs inside authorized locations with privacy/retention controls.

**Gate-harness verification**

Test the gates against controlled bad states:

| injected failure | expected rejection |
| --- | --- |
| Duplicate normalized packet answer | Focused packet uniqueness gate fails. |
| Changed seed heading or unexpanded section | Reference structure/evolution gate fails. |
| Missing loading/error fixture | State completeness review blocks broad acceptance. |
| Long error text clips primary action | Responsive/text-fit gate fails. |
| Icon button loses accessible name | Accessibility-tree or semantic check fails. |
| Focus order differs from visual/task order | Keyboard/accessibility review fails. |
| Asset request fails | Fallback state preserves hierarchy and identifies failure. |
| Canvas is transparent/blank | Pixel/canvas gate fails even when source and build pass. |
| Reduced-motion setting ignored | Preference interaction gate fails. |
| Faster candidate omits content | Functional/visual equivalence rejects performance adoption. |

Good use: project source/build checks pass, but a narrow error-state screenshot reveals the retry action clipped below the panel. The visual gate blocks only that state, the layout contract is fixed, and relevant behavior plus screenshot evidence is replayed.

Bad use: the archive verifier exits successfully and the agent declares a new React page accessible, responsive, and production-ready without starting it.

Conditional manual use: a static single-file page may rely on direct browser, keyboard, semantic, and viewport review when no project harness exists. Record the limitations rather than inventing a package command.

Verification is a dependency graph. A changed product requirement reopens state/composition; changed tokens reopen affected pixels; changed browser or asset reopens rendering; changed check harness reopens the evidence that depended on it. Selective invalidation is stricter and cheaper than ignoring a red gate or rerunning unrelated evidence blindly.

## Agent Usage Decision Guide

`agent_usage_decision_guide`: A request for a component, page, site, application, dashboard, portal, editor, game, design refinement, responsive repair, or visual verification should trigger a fit check. Use the reference when the next decision concerns the user experience, implementation, or rendered quality. A keyword alone does not authorize a redesign.

**Trigger and fit table**

| task signal | likely fit | first question | primary action |
| --- | --- | --- | --- |
| Build a known component/page/application | Strong fit. | Who uses it, what must they do, and what current system should be reused? | Model states, choose direction, implement actual workflow, render and verify. |
| Improve an existing interface | Strong fit after evidence. | Which user or rendered failure exists and which current contract governs it? | Reproduce, preserve fit, correct smallest boundary, verify affected states. |
| Make a site with no product/category context | Conditional fit. | Is this an app, branded offer, content experience, portfolio, venue, object page, or another explicit mode? | Inspect repository/context, infer only when evidence is strong, otherwise clarify the material choice. |
| Build an operations/CRM/SaaS surface | Strong fit with restrained product mode. | Which repeated actions and comparisons need dense predictable access? | Prioritize task surface, compact hierarchy, familiar controls, and complete states. |
| Build a brand/product/place/person page | Strong fit with subject-first mode. | What literal subject and real media must appear in the first viewport? | Build full-bleed or content-led experience with inspectable subject and next-section cue. |
| Build a game or interactive 3D tool | Strong fit plus specialized engine guidance. | Which established engine/library owns rules or scene behavior, and what counts as visible gameplay? | Use proven domain library, implement primary scene, verify pixels/input/mobile/fallback. |
| Fix unknown UI failure | Partial fit after diagnosis. | Can the failure be reproduced and causally isolated? | Diagnose first; use this guide to define corrected states and regression evidence. |
| Choose a product-wide design system | Auxiliary fit. | Who owns consumers, compatibility, migration, and design policy? | Route governance/architecture; use quality criteria and rendered validation here. |
| Decide legal/domain content or accessibility policy | No authority here. | Which qualified owner defines content and evidence floor? | Route to domain owner and retain frontend implementation/traceability. |
| Claim precise experience performance | Method fit only. | What workload, browser/device, baseline, metric, and owner decision apply? | Design controlled study; do not invent a result. |
| Explain code without changing UX | Usually too broad. | Can direct source navigation answer it? | Use repository explanation; invoke this guide only if experience decisions are evaluated. |

**Agent state machine**

| state | entry evidence | permitted work | prohibited promotion | exit |
| --- | --- | --- | --- | --- |
| `orienting` | User request, newest instructions, repository root, and current progress are available. | Read product/category context, existing system, routes, components, tokens, tests, and target state. | No product behavior or visual system invention. | Bounded user task and source authority stated. |
| `clarification_or_prototype` | Material product/content/owner choice is missing. | Search repository evidence, ask concise question, or build isolated reversible concept with assumptions. | No concept becomes production or current-system mutation silently. | Owner decision, current authority, or explicitly evaluated concept. |
| `experience_specified` | User journey, states, semantics, responsive/accessibility boundaries, direction, and non-goals are reviewable. | Design fixtures, tests, component/state ownership, and implementation plan. | No completion or performance claim before capable evidence. | Implementation scope and verification surface ready. |
| `behavior_implemented` | Working primary task and material states exist in target code. | Refine composition, visual system, assets, stable dimensions, and motion. | No decorative work may hide missing or broken states. | Project checks pass and target app can render. |
| `rendered_for_scope` | Actual target browser states and required viewports/content/input are observed. | Correct layout, assets, focus, accessibility, runtime errors, and visual coherence. | No generalization beyond matrix or source-only acceptance. | All affected rendered and behavior gates pass or branch is narrowed. |
| `verification_ready` | Implementation, rendered states, and direct checks are stable. | Run final relevant suite, state matrix, diff/ownership, performance and owner review as required. | No unsupported all-browser, accessibility, security, or speed claim. | Proceed, revise, reject, or escalate. |
| `verified_for_scope` | Evidence profile matches the bounded experience and owner accepts where needed. | Handoff, provide URL/artifact access, document recovery and invalidation. | No silent reuse after product/content/token/browser premise changes. | Complete or later invalidated. |
| `blocked_or_unresolved` | Product authority, content, asset rights, browser/GPU environment, credentials, policy, or evidence is insufficient. | Preserve valid branches, blocker, owner, required mechanism, and release condition. | No confidence inflation or repetitive same-method generation. | New evidence, narrower scope, or owner decision. |
| `invalidated` | Workflow, content, component, token, asset, state, browser, dependency, or policy changed. | Reopen dependent design claims and replay their gates. | No stale screenshot/baseline acceptance. | New scoped verification. |

Tiny reversible corrections need not print state names, but the transitions remain. A component that compiles but has never rendered has not reached `rendered_for_scope`.

**Default agent sequence**

1. Read the newest user request, active instructions, repository rules, ownership, progress, and existing changes.
2. State the exact user, task, product category, consequence, non-goals, and unresolved owner/content choices.
3. Inspect current route/page, design system, components, tokens, data/state ownership, assets, tests, and actual browser behavior before creating alternatives.
4. Read the complete local frontend-design source when visual reasoning is material; classify it as guidance rather than target authority.
5. Choose reuse, adaptation, deliberate divergence, or isolated exploration with a named reason.
6. Model material default/loading/empty/partial/error/permission/disabled/success/recovery states and transitions.
7. Define semantic controls, input/focus behavior, content hierarchy, responsive constraints, accessibility needs, and no-claim boundaries.
8. Commit to one product-appropriate visual direction; select typography, color roles, spacing/density, media, icons, surfaces, and motion coherently.
9. Implement the actual requested experience proactively inside authorized paths, using repository-native frameworks and proven domain libraries.
10. Make controls feature-complete, dimensions stable, text content-resilient, assets truthful, and failure/recovery usable.
11. Run repository-native checks and start the required local server when browser rendering needs it; provide the actual URL after verification.
12. Inspect real target states across risk-based viewport/content/input/browser matrix, including console/network, accessibility, and specialized canvas/media gates.
13. Reconcile screenshots and behavior with the stated direction, user task, design system, and counterevidence; fix owned defects rather than narrating them.
14. Return changed paths, checks/results, rendered access, residual limits, rollback/recovery, and invalidation triggers.

**Operating modes**

| mode | use when | output | stop condition |
| --- | --- | --- | --- |
| Planning-only | User requests a plan/alternatives or must approve a consequential product/design-system choice. | Experience/state contract, visual directions, tradeoffs, evidence plan, and open decisions. | Do not mutate until requested or authority exists. |
| End-to-end implementation | User expects a build and intent/write scope are clear. | Working repository-native interface, all material states, visual refinement, browser evidence, and handoff. | Stop only at verified completion or a material blocker after self-service investigation. |
| Focused correction | Existing contract and rendered failure are clear. | Minimal behavior/style change, focused regression, affected screenshots, and scope limit. | Do not opportunistically redesign unrelated surfaces. |
| Design exploration | Product wants alternatives before commitment. | Isolated concepts with assumptions, real representative content, comparison criteria, and promotion gates. | No production promotion without selected authority and full implementation evidence. |
| Code and experience review | Existing code/interface needs challenge. | Findings ordered by user consequence with source/state/rendered evidence and remediation. | Do not rewrite unless fixes are in scope. |
| Recovery | Prior work is stale, broken, interrupted, or based on wrong state. | Reconstructed target/source/browser state, earliest false premise, affected claims, and changed-premise next attempt. | Preserve valid work and other owners' changes. |
| Global visual review | Cross-page/system consistency and all critical states truly matter. | Complete surface/state inventory, checkpointed rendered matrix, cross-system reconciliation, and final gates. | Do not disguise global review as a few representative screenshots. |

**Context and tool discipline**

- Prefer repository-native components, tokens, icon libraries, scripts, fixtures, and browser harnesses over parallel abstractions.
- Read small required design sources completely. For large products, use route/component/state search and then complete selected modules; declare global review explicitly.
- Use image search or generation only when authorized and when real subject media improves the requested experience; preserve provenance and fallback.
- Use familiar icon libraries rather than drawing arbitrary SVG controls when an established icon exists.
- Use proven libraries for established game rules, physics, parsing, interaction engines, and 3D scene behavior unless from-scratch work is explicitly requested.
- Use scripts for hashes, parsing, screenshot orchestration, geometry/pixel checks, and validation. Do not let a deterministic score choose aesthetic fit or risk acceptance.
- Parallelize independent reads and disjoint assets only; preserve one writer per shared component/file/artifact and one integration owner.
- Never revert unrelated user or agent changes. Treat unexpected current work as evidence to integrate, not noise to clean.

**Minimum agent output**

| field | required answer |
| --- | --- |
| Experience decision | Which user task and product mode were implemented or reviewed, with non-goals? |
| Evidence | Which exact local sources, target source, rendered states, and owner decisions support it? |
| State contract | Which data/interaction/failure/recovery states and input paths govern the work? |
| Visual direction | Which coherent choices create hierarchy and product-specific character, and why do they fit? |
| Change | Which paths, components, assets, tokens, routes, and interfaces changed? |
| Verification | Which project/browser/accessibility/visual/performance gates ran and what remains outside them? |
| Uncertainty | Which content, browser, user, policy, or evidence branches remain unresolved and who owns them? |
| Recovery | How can the change be reversed, contained, or diagnosed if a premise fails? |
| Invalidation | Which future workflow, content, component, token, asset, dependency, browser, or policy change reopens it? |
| Next action | What executable step, owner, and stop condition follows? |

Good use: a user requests an inventory operations tool. The agent opens the existing app rather than building a marketing page, preserves compact navigation and familiar icon controls, implements loading/empty/error/retry states, and verifies actual wide/narrow browser pixels plus keyboard behavior.

Bad use: the word "frontend" triggers a generic gradient hero and card grid, while the requested workflow, current components, real content, and browser states remain absent.

Conditional use: product direction is unresolved but a component's validation and recovery states are authoritative. The agent can implement those independent states within the current system while keeping visual-system migration blocked and owned.

Appropriate abstention is successful when the guide prevents invented content, unauthorized redesign, inaccessible assets, or source-only completion. Its purpose is not maximum visual intervention; it is the right high-quality experience action for the evidence available.

## User Journey Scenario

Every repository, product name, requirement, component, check, screenshot, and outcome in this journey is illustrative. It demonstrates a mechanism grounded in local guidance; no target console, fixture, browser session, benchmark, or operator study was created for this reference evolution.

Role based opening scenario: A frontend product engineer and operations lead receive the request, "Modernize the shipment exception console before regional rollout. Make it faster to triage and easier to use on laptops and tablets."

Primary user starting state: Operators repeatedly filter a dense exception queue, compare status and age, open one shipment, assign an action, and recover when data or mutation requests fail. The repository has a navigation shell, tokens, data-table primitives, icon library, and scattered tests. The current page is usable on a wide monitor but clips actions in narrow containers and has no coherent empty, partial, stale, or mutation-error experience.

Decision being made: Which current patterns should remain, how the workflow and state ownership should be reorganized, which visual direction fits repeated operational use, and what browser/accessibility evidence can support rollout.

Reference opening trigger: Open this file after recognizing that the request is a real application workflow whose behavior, composition, accessibility, and rendered quality must survive implementation and handoff.

**Step 1: Separate the surface request into experience branches**

| branch | decision question | consequence if wrong | initial state |
| --- | --- | --- | --- |
| Queue scanning | Which fields and statuses let an operator identify the next exception quickly? | Important shipment is missed or page becomes visually noisy. | Product/operations owner plus current usage evidence required. |
| Filtering and selection | Which filters persist, how multi-selection behaves, and what stale data does? | Action targets the wrong rows or user loses context. | Existing behavior/source and owner decision required. |
| Detail and action | Should detail open in split pane, route, or modal, and which commands are authorized? | Context loss, cramped content, or unsafe mutation. | Product, auth, responsive, and repository evidence required. |
| Async and failure states | How loading, partial data, empty, stale, permission, network, and mutation errors appear and recover. | Blank or stuck UI and repeated unsafe actions. | Interface state contract required. |
| Responsive behavior | Which tasks remain supported on laptop, tablet, and narrow containers? | Controls clip, data disappears, or interaction becomes touch-hostile. | Product support matrix and rendered evidence required. |
| Accessibility/input | Which keyboard, focus, naming, status, zoom, and assisted paths must work? | Operators cannot perceive or complete the workflow. | Product policy and task evidence required. |
| Performance | Which operation and workload need which budget on which devices? | Copied target or a fast but incomplete interface drives rollout. | Baseline and accountable owner remain unresolved. |

Non-goals are explicit: the work does not create a marketing home page, redesign global navigation, choose operations policy, promise mobile-phone parity without support evidence, or declare one local timing representative of rollout traffic.

**Step 2: Build the illustrative evidence ledger**

| evidence item | illustrative observation | legitimate use | missing evidence |
| --- | --- | --- | --- |
| Operations owner interview | Operators triage by severity, age, destination, and last failure; they compare several rows before acting. | Product priority and density rationale. | Representative usage and regional differences remain to validate. |
| Current route/source | Queue, filters, and detail are coupled in one page component; row action performs direct mutation. | Implementation observation at one revision. | Runtime failure and concurrency behavior require fixtures. |
| Existing design system | Compact table, icon buttons, neutral surfaces, and semantic status colors already exist. | Current product visual/interaction authority. | Some narrow behavior and accessible names are incomplete. |
| Current browser state | Wide populated fixture scans well; narrow container clips final column and action menu. | Rendered defect for named content/state. | Other data lengths, zoom, and browsers remain outside evidence. |
| Current tests | Filter success and row navigation have unit coverage; stale data and mutation failure do not. | Verification inventory. | Oracle capability and integrated focus/recovery remain unknown. |
| Request phrase "faster" | No operation, workload, device, baseline, or bound is stated. | Unresolved aspiration only. | Product consequence, measurement method, and owner decision. |

The local frontend skill contributes intentionality and visual-system vocabulary. It does not justify replacing the compact operational model with an expressive hero, card grid, or novel control language.

**Step 3: Choose product mode and visual direction**

The team classifies the surface as a high-frequency operational tool. The direction is "quiet control room": compact but not cramped, neutral structural surfaces, high-information type hierarchy, semantic status accents, crisp dividers, stable row/action geometry, and restrained motion only for selection, state transition, and recovery feedback.

Distinctive character comes from shipment timeline markers, status language, and deliberate data hierarchy, not decorative gradients or card proliferation. This is a bold decision through specificity and restraint.

| candidate composition | benefit | risk/cost | evidence needed |
| --- | --- | --- | --- |
| Card per shipment | Strong item separation and touch targets. | Poor row comparison, excessive vertical length, nested-card pressure. | Low-density/touch workflow evidence. |
| Full-width data table with separate detail route | Maximum scanning space and stable table semantics. | Navigation loses list context and slows repeated actions. | Frequency, back/selection preservation, and narrow behavior. |
| Queue plus responsive detail pane | Preserves scan context and supports repeated triage. | More state synchronization and limited width. | State model, keyboard/focus, content pressure, and breakpoint/container evidence. |
| Modal detail | Keeps page context and is quick to add. | Long content, nested actions, URL/history, focus, and narrow layout can degrade. | Content/action complexity and modal semantics. |

Assume the owned decision selects queue plus responsive detail pane: side-by-side when sufficient container width exists, detail route/sheet behavior under the approved narrower mode, and no unsupported phone claim.

**Step 4: Define the state graph**

| state | user sees | permitted action | recovery or next transition |
| --- | --- | --- | --- |
| Initial loading | Stable toolbar, table skeleton sized to final structure, and status text. | Change route/back only; destructive actions unavailable. | Loaded, empty, partial, auth, or load-error. |
| Loaded populated | Sortable/filterable queue, counts, current freshness, selection, and detail entry. | Filter, select, inspect, assign authorized action. | Refresh, stale, action-pending, or permission change. |
| Empty by filter | Current filters, zero result explanation, and clear-filter command. | Edit/clear filters. | Populated or true-empty. |
| True empty | No open exceptions and last refresh context. | Refresh or leave. | Loading/populated/error. |
| Partial data | Rows that loaded, explicit unavailable fields/source, and nonblocking warning. | Inspect safe data; actions requiring missing fields disabled with reason. | Recovery refresh or full data. |
| Stale selection | Changed/removed rows identified before mutation. | Review latest state, remove invalid selections, retry only under current data. | Loaded or action-ready. |
| Permission denied | Task context preserved; unavailable actions absent/disabled according to product policy. | Navigate and request appropriate route if authorized. | Permission refresh or exit. |
| Action pending | Selected scope and operation remain visible; duplicate command prevented. | Cancel only if supported. | Success, conflict, validation, network error, or timeout state. |
| Action success | Updated row/status plus concise confirmation linked to affected shipment. | Continue triage or inspect. | Loaded/current selection. |
| Action failure | Error class, preserved safe selection/context, corrected fields or retry where legitimate. | Retry only for approved class, revise input, or cancel. | Pending, loaded, or escalation. |
| Load error | Page shell, filters if safe, error context, and retry/back. | Retry with changed/transient premise or leave. | Loading or blocked. |

The layout reserves stable space for toolbar, status, and primary action regions so state copy does not resize controls or hide commands.

**Step 5: Compile illustrative interface requirements**

```markdown
### REQ-EXC-001.0: Scan current exception queue

WHEN an authorized operator opens a successfully loaded exception queue
THEN the interface SHALL present owner-approved priority fields in a stable comparison layout
AND SHALL expose sort, filter, freshness, row status, and detail entry through semantic controls
SHALL preserve the visible task hierarchy across supported container states and representative content lengths

### REQ-EXC-002.0: Preserve valid selection across refresh

WHEN selected rows change or disappear during a queue refresh
THEN the interface SHALL identify stale selections before any mutation
AND SHALL preserve still-valid selections and user context
SHALL prevent an action from applying to unreviewed stale scope

### REQ-EXC-003.0: Recover failed exception action

WHEN an authorized queue action fails
THEN the interface SHALL preserve safe task context and identify the failure class
AND SHALL expose correction, retry, cancellation, or escalation only when that route is valid
SHALL prevent duplicate submission while the prior attempt remains unresolved
```

The exact fields, actions, error classes, support widths, and authorization semantics must come from the target product and service contract, not this example.

The performance branch remains a measurement question:

```markdown
### REQ-EXC-PERF-001.0: Measure triage interaction readiness

WHEN the owner-approved queue population, browser/device, network, data state, and cache conditions are frozen
THEN the measurement SHALL record the selected interaction boundary, raw observations, failures, and environment
AND SHALL preserve functional, visual, and accessibility equivalence
SHALL remain nonaccepting until an accountable owner chooses a budget from baseline and rollout consequence
```

**Step 6: Design bidirectional verification**

| requirement/state | illustrative check | observation | critical negative |
| --- | --- | --- | --- |
| Queue scan | Component plus browser flow. | Fields, sort/filter, freshness, status, and detail entry are correct. | Long destination/status does not clip action or reorder meaning. |
| Loading/empty/partial/error | State fixtures and screenshots. | Stable structure, accurate message, and safe next action. | Empty-by-filter is not confused with true-empty or failed load. |
| Selection refresh | Integration/browser state test. | Valid selection persists; stale rows are identified before mutation. | Removed row cannot receive action. |
| Action recovery | Controlled service responses and browser flow. | Pending prevents duplicate; failure preserves context and correct recovery. | Nonretryable conflict is not presented as blind retry. |
| Keyboard/focus | Manual plus browser assertions. | Toolbar, rows, detail, actions, errors, and return path follow coherent order. | Detail closure does not lose focus or selected context. |
| Responsive composition | Named container/content screenshots and geometry checks. | Queue/detail transform according to support policy without overlap or hidden primary commands. | Narrow error text and selected-count extremes fit. |
| Accessibility semantics | DOM/accessibility tree, automated findings, keyboard, and targeted review. | Names, roles, states, status feedback, table relationships, and errors support task. | Color/status icon alone does not communicate severity. |
| Performance method | Controlled measurement design. | State/workload/environment and counter-gates are complete. | Missing bound or workload prevents rollout claim. |

The reverse audit asks whether old tests encode behavior not present in the requirements, such as keeping selection after filter changes or opening detail in a modal. The team must decide whether each is an intended invariant, stale expectation, or migration constraint before editing it.

**Step 7: Implement the requested experience**

The implementation reuses the current shell, table, icons, tokens, focus primitives, and data/query layer. It extracts explicit queue/detail/action state only where current coupling obstructs behavior. It does not create a new design system, add a marketing hero, or replace familiar controls with custom pills.

Polish occurs after the state behavior works: stable column/action widths, coherent type roles, clear status accents with non-color cues, compact spacing, detail hierarchy, real error content, touch-safe controls where supported, and restrained transition feedback. No decorative media is added because it would not help triage.

**Step 8: Verify with split outcomes**

| branch | illustrative final evidence | state |
| --- | --- | --- |
| Queue scanning/filtering | Product fields, component checks, wide and approved narrow states, content extremes, and human scan review pass. | `verified_for_scope` under named data and containers. |
| Selection/action recovery | Pre-change stale/mutation fixtures expose defects; final integrated checks pass approved branches. | `verified_for_scope` under selected service semantics. |
| Accessibility/input | Automated findings, keyboard/focus path, semantic/status checks, and targeted owner review pass. | `verified_for_scope` for recorded modes; no universal disability claim. |
| Visual direction | Rendered states show one restrained operational hierarchy and current design-system fit. | `rendered_for_scope` and owner-reviewed. |
| Performance | Measurement method exists but rollout workload and budget remain absent. | `unresolved`; no speed or capacity claim. |
| Unsupported phone workflow | Product has not committed to full task parity. | `out_of_scope` with explicit route rather than hidden broken layout. |

This split can permit rollout only if policy does not require the unresolved performance or phone branches. Otherwise those branches remain release blockers.

**Step 9: Handoff and invalidation**

The record names changed routes/components/tokens/assets, exact commands, fixture identities, browser states, screenshots, accessibility evidence, known browser/content gaps, rollback, and owners. It states that changes to operator priority fields, action/auth semantics, data freshness, navigation shell, table/detail primitives, tokens/type, locale/content distribution, supported containers, browser matrix, or performance budget reopen dependent evidence.

Good result: a restrained, high-information console supports real loading/error/stale/recovery states and actual keyboard/narrow rendering, while performance remains honestly unresolved.

Bad result: a polished card grid and dashboard headline replace the table, one populated desktop screenshot is accepted, and an arbitrary 100 ms target is copied into release criteria.

Conditional pilot: one regional team may use a narrower device/browser set under named users, duration, monitoring, rollback, and no-generalization language. That is a new product policy, not evidence that all regions are supported.

**Future replay criteria**

A safe fixture should cover initial loading, populated, filtered empty, true empty, partial data, load failure, stale selection, permission loss, action pending/success/validation/conflict/network failure, content extremes, keyboard/focus return, reduced motion where used, and approved container transitions. It should demonstrate pre-change failures and final behavior without claiming production data or operator equivalence.

The transferable lesson is that a frontend request becomes reliable when the team follows the user task across behavior, semantics, composition, visual system, and browser evidence, allowing each branch to earn its own state.

## Decision Tradeoff Guide

Use the least costly option capable of preserving and falsifying the pending user-experience claim, then escalate when a remaining blind spot can change the action. Cost includes implementation, context, user relearning, accessibility barriers, performance, asset lifecycle, maintenance, migration, rollback, and option loss. Evidence adequate for a color-token correction can be inadequate for a new navigation model or design-system replacement.

**Preserved posture guide**

| decision_option_name | when_to_choose_condition | tradeoff_cost_description | verification_question_prompt |
| --- | --- | --- | --- |
| Adopt when | Product task, local guidance, current system, target implementation, and capable rendered evidence support the full context/state/visual/verification workflow. | Fastest durable route for a new experience, but can add ceremony when a current component already settles a narrow change. | Does each material experience claim have current authority, complete applicable states, capable checks, rendered evidence, and recovery? |
| Adapt when | The principle is sound but product mode, design system, content, accessibility, framework, performance, or compatibility needs another representation. | Preserves intent and local fit, but requires explicit equivalence and review. | Which protected behavior remains, which mechanism changes, and how does evidence show equal or stronger quality? |
| Avoid when | User/product intent is unresolved, causal diagnosis is primary, domain authority is missing, browser evidence is unavailable, or the reference would create a second design authority. | Prevents false precision and unauthorized redesign, but may pause or route work. | Which missing observation or owner makes frontend design execution premature or redundant? |
| Cost of being wrong | Wrong guidance can hide primary commands, break accessibility, lose state, clip content, misrepresent the subject, fragment the design system, or anchor on fabricated performance. | Rework ranges from a token correction to user exclusion, failed rollout, compatibility migration, or production incident. | Can a reviewer identify the failed premise, affected states/surfaces, rollback, owner, and next evidence without reconstructing the session? |

Agreement between local and public prose is not a universal adoption test. Duplicate local files can agree because they are identical; public documentation can be current but inapplicable; current UI can be consistent but wrong. The user task, product/design authority, target state, and claim-capable browser evidence decide sufficiency.

**Current-system choices**

| choice | choose when | benefit | cost or blind spot | escalation trigger |
| --- | --- | --- | --- | --- |
| Reuse existing component/tokens | Current primitive fits behavior, semantics, states, and visual direction. | Familiarity, consistency, smaller diff, and shared maintenance. | Existing defects or missing variants can be inherited. | Reproduction shows the primitive causes the user failure. |
| Augment existing primitive | Core contract is sound but one state, size, content, or accessibility path is absent. | Smallest shared improvement. | Shared change can affect many consumers. | Consumer matrix or API change requires versioned migration. |
| Compose existing primitives differently | User hierarchy differs but controls and tokens remain valid. | Product-specific layout without new system. | Composition can create focus/order/overflow issues. | Cross-page pattern or shared layout primitive becomes justified. |
| Create a bounded new component | No current primitive expresses the behavior and reuse would distort semantics. | Clear target contract and contained experimentation. | New API, variants, docs/tests, and ownership. | Similar consumers appear or design-system governance is required. |
| Introduce/replace design system | Product-wide inconsistency or capability gap has owner-approved migration. | Coherent future language and shared quality controls. | Large consumer, compatibility, rollout, training, and maintenance cost. | No owner, consumer inventory, migration, or rollback exists. |
| Decline redesign | Current system already solves the task or missing authority makes divergence unsafe. | Avoids duplicate truth and unnecessary user relearning. | Visual opportunity may remain. | Resume after material product/evidence change. |

**Product-mode choices**

| mode | design priority | common mismatch | verification emphasis |
| --- | --- | --- | --- |
| Operational/SaaS/CRM/dashboard | Repeated action, scanability, comparison, stable navigation, controlled density, recovery. | Oversized hero, decorative cards, low information density, novel controls. | Task flows, state matrix, keyboard, narrow containers, content extremes. |
| Commerce/service transaction | Product information, trust, choices, forms, totals, errors, progress, recovery. | Atmospheric imagery hides product or optimistic action masks failure. | Content accuracy, form semantics, validation, mutation recovery, device/browser. |
| Editorial/content | Reading hierarchy, media, narrative rhythm, navigation, source/author context. | Card grid fragments story or expressive layout breaks reading order. | Content lengths, semantics, zoom, media, responsive hierarchy. |
| Brand/product/place/person/portfolio | Literal subject signal, real inspectable media, memorable direction, conversion or exploration. | Tiny subject name, generic split hero, stock atmosphere, no next-section cue. | First viewport, real assets, responsive crop, text contrast, task/CTA. |
| Editor/creative tool | Stable workspace, familiar tools, mode/state clarity, undo/recovery, precision. | Verbose pill controls, shifting toolbars, hidden selection/state. | Commands, keyboard, stable dimensions, persistence/recovery, canvas. |
| Game/interactive scene | Gameplay readability, feedback, motion, input, assets, performance, expression. | Decorative UI overwhelms play or hand-built rules/physics fail. | Proven engine logic, pixel/input/animation, mobile framing, fallback/performance. |

**Information and composition choices**

| option | strongest use | cost or failure | deciding evidence |
| --- | --- | --- | --- |
| Dense table | Expert comparison, sorting, scanning, repeated actions. | Narrow/touch complexity, row semantics, horizontal pressure. | Field priority, content distribution, task frequency, responsive policy. |
| List | Sequential scan with moderate metadata and simple actions. | Weak cross-row comparison or excessive vertical space. | User decision pattern and item structure. |
| Repeated cards | Distinct items with media, varied content, and low comparison need. | Nested hierarchy, poor density, generic template. | Item independence, media need, and task frequency. |
| Split pane | Preserve list context while inspecting/acting on one item. | State synchronization and width constraints. | Repeated triage frequency, content length, focus, narrow transformation. |
| Separate detail route | Deep content, shareable URL, history, and full-width tasks. | Context switching and selection restoration. | Task depth, navigation semantics, back/refresh behavior. |
| Modal/dialog | Short focused interruption with clear completion/cancel. | Long/complex content, nested actions, focus and mobile pressure. | Scope, duration, content, semantics, escape/recovery. |
| Full-width unframed band | Page hierarchy and content sections. | Needs strong spacing and separators without card borders. | Product/content rhythm and responsive composition. |
| Hero/full-bleed scene | Genuine branded offer, subject, place, person, product, or immersive entry. | Wrong for repeated operational tasks; media and text can obscure each other. | Product mode, actual subject media, first viewport, next-section hint. |

**Control choices**

| action type | preferred control | tradeoff or exception | gate |
| --- | --- | --- | --- |
| Familiar tool command | Established icon button with accessible name and tooltip where useful. | Text may be clearer for infrequent/consequential commands. | Meaning, hit target, focus, pressed/disabled states. |
| Clear command | Text or icon+text button. | Avoid verbose toolbars for repeated known actions. | Label, consequence, state, layout fit. |
| Binary setting | Checkbox, switch, or toggle according to semantics/current system. | A button may represent an immediate action, not a persistent state. | Programmatic state and announcement. |
| Mode among few peers | Segmented control or tabs when views/modes fit their semantics. | Too many options need menu/select or other pattern. | Selection, keyboard, route/history as applicable. |
| Option set | Menu, select, radio, command palette, or list based on count/frequency. | Hidden menus reduce discoverability for primary actions. | Task frequency and keyboard/touch behavior. |
| Numeric value | Input, stepper, slider, or range control based on precision and bounds. | Slider is poor for exact unbounded values. | Label, units, validation, keyboard, errors. |
| Color | Visible swatch plus accessible label/value and current-system picker. | Color alone cannot convey status or selection. | Naming, contrast, input, and non-color cues. |

**State and data choices**

| approach | benefit | risk | safe use |
| --- | --- | --- | --- |
| Pessimistic mutation | Clear server authority and easier conflict handling. | Slower perceived completion. | Consequential or hard-to-reverse actions; show pending context. |
| Optimistic mutation | Immediate feedback and fluid repeated tasks. | Rollback, conflicts, duplicate actions, and lost context. | Reversible behavior with explicit reconciliation and failure recovery. |
| Skeleton loading | Preserves rough structure. | False precision, motion/noise, mismatched final layout. | Stable known geometry; include status semantics and timeout/error route. |
| Progressive/partial data | Useful content arrives early. | Misleading completeness and shifting hierarchy. | Mark source/freshness, disable unsafe actions, stabilize composition. |
| Inline error | Error is close to control/state. | Can overflow or be missed. | Local correctable failure with focus/announcement and stable action region. |
| Page-level error | Boundary failure affects whole task. | Loses context if generic. | Preserve safe prior choices and offer valid recovery/route. |

**Visual-system choices**

| choice | benefit | risk | decision rule |
| --- | --- | --- | --- |
| Existing product typography | Familiar, performant, compatible, internationalized. | May feel undifferentiated or carry known weaknesses. | Preserve unless target evidence and owner justify migration. |
| Distinctive display type | Strong subject/brand signal. | Loading, glyph, readability, crop, and overflow. | Reserve for fitting roles; verify real content/locales and fallback. |
| Controlled density | Efficient expert scanning and repeated action. | Touch, zoom, fatigue, and content pressure. | Use stable hierarchy and targets; transform rather than merely shrink. |
| Generous space | Emphasis, readability, premium/editorial rhythm. | Low task throughput or excessive scroll. | Use where content/task frequency supports it. |
| Restrained neutral surfaces | Quiet structure and semantic accents. | Can become bland or one-note. | Add product-specific type, data, media, border/rhythm decisions. |
| Expressive palette/detail | Memorable identity and atmosphere. | Trend convergence, contrast, semantic confusion, rendering cost. | Tie each role to subject and preserve accessibility/performance. |

**Media, motion, and 3D choices**

| choice | choose when | cost/blind spot | required counter-gate |
| --- | --- | --- | --- |
| Real product/place/object media | Users need inspection, trust, or subject orientation. | Asset rights, crop, bandwidth, loading/failure. | Provenance, real subject visibility, responsive crop, fallback. |
| Generated image | Authorized custom visual better expresses the subject and no existing asset suffices. | Accuracy, rights/policy, style drift, artifacts. | Prompt/provenance, review, subject truthfulness, fallback. |
| Decorative texture/pattern | Supports the chosen material/brand direction. | Noise, contrast, generic filler, cost. | Removal test: retain only if it improves hierarchy or subject. |
| CSS motion | Small transitions and orchestrated page moments. | Input/motion preference/layout stability. | Reduced-motion and interruption checks. |
| Motion library | Coordinated React/app interactions with lifecycle control. | Bundle/complexity and stale animation state. | Repository fit, cleanup, performance, preferences. |
| Three.js scene | Real 3D inspection, gameplay, simulation, or immersive subject. | GPU, assets, lifecycle, input, framing, accessibility, fallback. | Nonblank pixels, mobile/desktop, interaction, cleanup, performance, fallback. |

**Responsive choices**

| strategy | use when | tradeoff | hard boundary |
| --- | --- | --- | --- |
| Fluid/container-aware layout | Components live in varied shells and content widths. | More local layout rules and test states. | Text and commands must remain complete at supported containers. |
| Discrete composition change | Hierarchy genuinely changes between wide and narrow modes. | More state variants and potential DOM/focus drift. | Preserve task, semantics, and state through transformation. |
| Horizontal overflow | Dense data comparison cannot fit and product explicitly supports scroll. | Discoverability and touch/keyboard complexity. | Frozen columns/controls, indication, semantics, and alternative as required. |
| Feature reduction | Product explicitly narrows tasks on a device/mode. | Capability mismatch and user surprise. | Owner-approved support matrix and clear route, never accidental hiding. |

**Verification choices**

| mechanism | strongest economical use | blind spot | complement |
| --- | --- | --- | --- |
| Unit/component | State logic and local semantics. | Actual integrated layout/browser. | Browser state and screenshots. |
| End-to-end | Integrated task and recovery. | Visual coherence and all variants. | State matrix and visual/accessibility review. |
| Screenshot | Pixel/layout regression. | Semantics, focus, offscreen behavior. | DOM/accessibility and interactions. |
| Automated accessibility | Detectable rendered issues. | Full usability and product-specific meaning. | Keyboard, semantics, assisted/human review. |
| Human visual critique | Context, hierarchy, subject, coherence, trust. | Hidden behavior and reviewer bias. | Reproducible technical evidence and alternatives. |
| Performance measurement | Quantitative target under workload. | Other conditions and experience correctness. | Functional/visual equivalence and owner interpretation. |

Two checks are not independent because they use different tools. A component story and screenshot that share one ideal fixture can both miss an error state and long content.

**Recommended evidence bundles**

| decision | minimum complementary bundle | stop rule |
| --- | --- | --- |
| Token/spacing correction | Current authority, affected states, focused source check, before/after rendered evidence, regression/no-overlap. | Stop when bounded state and consumers remain valid. |
| New product workflow | Product/owner decision, state contract, semantics, responsive/accessibility matrix, working implementation, browser flow, visual review, recovery. | Stop when material claims are verified or explicitly split. |
| Shared component/system change | Consumer inventory, API/variant contract, accessibility, visual states, migration, rollout/rollback, governance. | Stop only when supported consumers and ownership pass. |
| Media/3D primary experience | Subject/interaction requirement, assets, loading/error/fallback, browser pixel/input, mobile/desktop, lifecycle, performance. | Stop when scene/media is truthful, usable, recoverable, and bounded. |
| Quantitative experience target | Functional/visual equivalence, workload, baseline/candidate, raw results, uncertainty, counter-metrics, owner decision. | Stop at bounded decision or unresolved state. |

**Pre-action tradeoff audit**

1. Which exact user task and state are being changed?
2. What product/design/content authority can choose it?
3. What is the cost, detectability, reversibility, and consumer scope of likely errors?
4. Which current components/tokens/contracts should be reused, adapted, or retired?
5. Which visual choice reinforces the subject or workflow rather than a trend?
6. Which methods share the same fixture, browser, or assumption?
7. What independent evidence could expose the most consequential miss?
8. Does the choice create another design system or state authority?
9. Which option becomes costly or impossible once implementation begins?
10. What owner decision or evidence state ends exploration?

Good: reuse a current table, add the missing error/recovery state, fix narrow action geometry, and verify real content without creating a new packet of primitives. Bad: write a complete design rationale for a card-grid redesign while the required operational comparison and keyboard behavior remain absent. Conditional: replace an established primitive only through an owned consumer/migration plan with stronger target evidence.

The deeper tradeoff is option preservation. Early work should make the next decision more informative without locking the team into unsupported layout, component, asset, or design-system commitments. A concise direction is valuable when it creates a falsifiable next state; it stops being valuable when aesthetic confidence closes a decision that only product, browser, user, or owner evidence can close.

## Local Corpus Hierarchy

Classification vocabulary includes canonical, supporting, historical, current, duplicate, product-authoritative, design-authoritative, target-semantic, rendered, measured, owner-accepted, unrefreshed, conflicting, and unknown-authority roles. These form a partial order by claim rather than one universal rank.

**Preserved seed role metadata**

| local_source_filepath_value | corpus_hierarchy_role | heading_signal_to_convert | observed identity and reviewer question |
| --- | --- | --- | --- |
| `agents-used-monthly-archive/claude-skills-202603/plugins/frontend-design/SKILL.md` | canonical primary source | `Design Thinking`; `Frontend Aesthetics Guidelines` | Hash-equal to current local path. What exactly did this dated snapshot recommend, and which caveats constrain reuse? |
| `claude-skills/plugins/frontend-design/SKILL.md` | supporting context source | `Design Thinking`; `Frontend Aesthetics Guidelines` | Same observed bytes as archive copy. What current local routing/package value does this identity provide? |

The seed labels are retained as corpus metadata. No mapped content explains why the archive copy is canonical while the same current body is supporting. The hierarchy does not invent a rationale or allow those labels to decide target workflow, visual system, browser behavior, or release.

**Role definitions**

| role | authority | limitation | conflict response |
| --- | --- | --- | --- |
| Canonical historical snapshot | Exact content of the designated dated file. | Designation does not establish current applicability or design effectiveness. | Preserve the snapshot and test derived guidance against current target evidence. |
| Current local guidance | Present local skill text and invocation intent. | Can be duplicated, stale, generic, or unsuitable for product mode. | Use as creative/process guidance after active instructions and fit review. |
| Duplicate content | Same observed bytes under another path identity. | Adds provenance, not independent substantive support. | Read once for meaning; retain all identities and surrounding context. |
| Product/content authority | User, product, domain, content, legal, or policy owner chooses desired task and content. | Owner choice is not implementation or outcome evidence. | Record exact decision, scope, date, and invalidation. |
| Design-system/brand authority | Governed components, tokens, interaction, brand, and migration decisions. | Existing system can contain defects and may not cover new product modes. | Reuse by default; challenge through target evidence and owned governance. |
| Target semantic evidence | Routes, components, state/data ownership, DOM, configuration, tests, and source. | Source and tests can omit browser and user effects. | Use for implementation claims under named revision; render dynamic/visual claims. |
| Rendered target evidence | Pixels, DOM/accessibility tree, focus/input, asset/runtime, and browser behavior under named state. | One state, browser, fixture, or viewport cannot support universal claims. | Preserve scope and expand matrix only when decision requires it. |
| Measured target evidence | Controlled task, accessibility, performance, visual, defect, or operational study. | Cohort, workload, environment, and confounding limit generalization. | Use only for its bounded quantitative or outcome claim. |
| Owner-accepted decision | Accountable owner accepts behavior, direction, support scope, or residual risk. | Acceptance is not empirical truth outside authority or period. | Record reviewed evidence, recovery, and expiry/invalidation. |
| Unrefreshed external pointer | Local source retains public locator and description. | No current remote content, version, access, or applicability. | Refresh only under authorization and decision need. |
| Conflicting source | Applicable evidence makes incompatible claims under overlapping scope. | Fixed rank can conceal version, state, user, or owner differences. | Narrow scope, preserve both, and choose a capable resolver. |
| Unknown authority | Artifact exists but provenance, owner, binding status, or freshness is unclear. | Cannot authorize consequential design or release alone. | Use as hypothesis/navigation and route to accountable evidence. |

**Claim-specific precedence matrix**

| claim | first authority | corroborating evidence | source that must not overrule it |
| --- | --- | --- | --- |
| What the 202603 skill said | Exact archive bytes and package context. | Hash comparison with current copy. | Current product evidence cannot rewrite the historical file. |
| What guidance is locally available now | Current local skill bytes and active invocation context. | Archive comparison and current instructions. | Canonical archive label cannot make old/generic guidance binding. |
| Which user workflow should exist | User/product/domain/content authority within scope. | Existing requirements, usage/research, support evidence, and current behavior. | A creative skill or template cannot invent product intent. |
| Which visual system is governed | Current design-system/brand authority and owner. | Existing components/tokens, design artifacts, history, and consumer behavior. | One generated page cannot silently become product-wide authority. |
| What implementation currently does | Target source, state/data flow, configuration, dependencies, and tests. | History and product contract for intended meaning. | Design prose or screenshot cannot override source facts. |
| What actually renders | Browser output under exact state/content/viewport/input/configuration. | Source, tests, screenshots, DOM/accessibility, console/network, and human review. | Component code cannot overrule observed pixels or focus. |
| Whether behavior satisfies the task | Claim-capable user-flow and state checks plus semantic review. | Browser evidence, negative cases, and owner acceptance as required. | Build success and visual polish cannot settle task semantics. |
| Whether accessibility is sufficient | Applicable user/product policy and multimodal target evidence. | Automated findings, keyboard, semantic, assisted, and expert review. | One screenshot or automated score cannot settle it. |
| Whether a visual direction fits | Product/brand/design authority plus experienced review against user/task/content. | Rendered alternatives, current system, and user evidence. | Popularity, score, or generic external example cannot settle it. |
| Whether speed or outcome improvement is real | Controlled target measurement with workload, baseline, environment, sample, uncertainty, and counter-gates. | Representative users/devices and operational evidence where authorized. | Seed examples, inherited scores, or one warm run cannot settle it. |
| Whether residual risk is acceptable | Accountable product/design/engineering/domain owner under policy. | Technical evidence, known gaps, rollback, and dissent. | A test suite or design reference cannot assume authority. |

**Observed content families**

| family | identities | SHA-256 | hierarchy consequence |
| --- | --- | --- | --- |
| Frontend design skill | Archive and current local path. | `d39adf3a983de7dafc75991590d54f091755f7e4163d5a5ed085ecd719157184` | One substantive guidance source with two path/package contexts; no multiplied confidence. |
| Frozen reference seed | One archive path. | `ea3cd4775cda2613c9b863c3d24b0c0f18acfabcd5242ff1f4ea0b7e25cb33c5` | Structural/historical baseline, not target quality authority. |

Equal bytes establish content identity. They do not show equal ownership, activation, package context, or applicability.

**Default retrieval route**

1. Start with complete user request, newest instructions, target repository rules, and existing product/design contract.
2. Inspect actual route/components/tokens/content/states and browser behavior relevant to the task.
3. Read one representative local skill copy completely for creative guidance and caveats.
4. Use product/content owners for intent and design-system governance for shared visual/interaction authority.
5. Use target source and tests for implementation semantics and browser evidence for actual experience.
6. Route numeric claims to measurement and high-consequence acceptance to accountable owners.
7. Revisit both duplicate path contexts only for history, packaging, or activation questions.
8. Refresh a public pointer only when authorization and a version-sensitive decision justify it.

This route optimizes orientation and current fit. It does not make the first-read source globally canonical.

**Conflict resolution**

| conflict | resolution |
| --- | --- |
| Local skill encourages novelty while current product requires familiar operational controls | Preserve intentionality and product-specific detail inside current semantics; require governance for broad divergence. |
| Design file and current source disagree | Classify future intent, stale design, implementation defect, or approved divergence before changing either. |
| Product requirement and existing behavior disagree | Decide bug, migration, experiment, compatibility behavior, or mistaken requirement with owner. |
| Screenshot baseline and desired change disagree | Determine baseline authority; classify intended/unintended pixels rather than preserving every old defect. |
| Automated accessibility pass and keyboard/user review disagree | Narrow automated claim and fix the user-impacting behavior. |
| Refreshed framework guidance and installed target disagree | Version and reproduce both; route packaging/compatibility instead of averaging. |
| Target measurement contradicts a copied budget | Use target result for its cohort and return acceptance value to owner. |
| Two owners disagree | Preserve both decisions and block dependent implementation until authority is resolved. |

**Targeted invalidation**

| changed node | reopen | retain unless separately affected |
| --- | --- | --- |
| Historical skill snapshot | Claims about that snapshot and duplicate family. | Independently verified target experience. |
| Current local skill | Creative/process recommendations derived from it. | Historical content and target behavior. |
| Product/content decision | User task, copy, state semantics, implementation, and acceptance linked to it. | Unrelated source facts. |
| Design system/token/component contract | Consumer pixels, behavior, migration, and visual claims that depend on it. | Product goals not tied to changed mechanism. |
| Target source/config/dependency | Implementation and rendered evidence under old state. | General guidance and owner intent. |
| Test/browser/screenshot harness | Evidence relying on its fixtures, oracle, browser, timing, or capture. | Desired behavior unless mismatch reveals contract issue. |
| Content/locale/viewport/browser | Text fit, responsive, asset, focus, and visual claims under old matrix. | Pure logic evidence under unaffected assumptions. |
| Workload/device/network | Performance and operational applicability. | Functional evidence under unaffected state. |
| Owner/policy | Acceptance and risk decision. | Technical observations kept separate. |
| Public primary source | Current external framework/workflow claim. | Historical pointer and prior retrieval record. |

Good historical claim: "The 202603 archive path contains this guidance and its bytes match the current local path." Good current claim: "The product owner chose compact triage, current components implement it, and the named browser states support the bounded experience." Bad claim: "Two local files independently prove that bold visual design improves frontend quality."

The hierarchy is causal and versioned: product/design authority and guidance shape a state/visual contract; implementation and browser evidence support or refute it; owners accept bounded results; outcomes inform a later revision. Feedback creates a new trajectory and must not retroactively strengthen earlier sources.

## Theme Specific Artifact

Theme specific artifact: **Frontend Experience Evidence Packet**, whose review view is a quality-bar rubric with behavior blockers, accessibility/input blockers, rendered-composition blockers, project gates, release criteria, and explicit unresolved states.

The packet is a provenance and invalidation graph for one bounded user journey and target revision. It links existing product, design, code, test, browser, and review artifacts instead of copying them. No separate target packet was created during this evolution because the authorized write surface contains only this reference, its question packet, and the Delta journal. The schema below is the completion contract for future authorized frontend work.

**Completion profiles**

| profile | use | required depth | explicitly unnecessary unless consequence changes |
| --- | --- | --- | --- |
| `focused_correction` | Current product/design authority and regression state settle one reversible component, token, content-fit, or style defect. | Journey/state ID, target/source identity, defect reproduction, changed boundary, project result, before/after rendering, stop reason, and invalidation. | New visual system, full product source map, broad browser study, or unrelated state catalog. |
| `standard_experience` | New page/workflow, meaningful redesign, multi-agent handoff, or repeated state behavior. | Full decision/source ledger, state graph, semantics, responsive/accessibility boundaries, visual system, component/state ownership, behavior checks, rendered matrix, runtime, recovery, and invalidation. | Domain assurance beyond actual user consequence. |
| `high_assurance_interface` | Regulated content, critical operation, destructive action, shared design system, broad compatibility, security/privacy, or material accessibility claim. | Standard profile plus qualified domain authority, content/locale/device/browser/input/assistive variants, independent evidence, operations, rollback, residual risk, and accountable acceptance. | No material omission may be silent; unavailable evidence blocks or becomes explicit owner-accepted risk only under policy. |

Profiles prevent both bureaucracy and under-specification. A spacing regression can reuse one current state. A destructive transfer flow cannot inherit that evidence merely because both interfaces render.

**Block A: packet and experience identity**

| artifact_field_name | artifact_completion_rule | evidence_source_hint |
| --- | --- | --- |
| `packet_identifier` | Stable unique identifier for journey and revision; do not encode an unverified conclusion in its name. | Issue, review, incident, or local decision sequence. |
| `packet_profile` | Explain profile using user consequence, reversibility, shared consumers, novelty, and lifespan. | Tradeoff and reliability sections plus project policy. |
| `user_goal_statement` | State user/actor, concrete job, context, frequency, and desired outcome. | User request, product/content authority, current workflow. |
| `product_mode` | Operational, transactional, editorial, branded, game, editor, dashboard, or another explicit category with rationale. | Task and audience evidence. |
| `decision_question` | One falsifiable experience branch; split behavior, visual, accessibility, compatibility, performance, and owner-policy questions. | Journey decomposition. |
| `non_goals` | List systems, users, devices, states, content, migrations, and optimizations outside scope. | User and owner decision. |
| `decision_consequence` | False-positive/negative effects, detectability, reversibility, consumers, and who bears risk. | Product/domain context. |
| `decision_owner` | Name who chooses task/content/design/support scope and who accepts residual risk. | Project ownership and policy. |
| `packet_state` | `collecting`, `experience_specified`, `behavior_implemented`, `rendered_for_scope`, `verification_ready`, `verified_for_scope`, `refuted`, `unresolved`, or `invalidated`, with actor/time. | Gate transitions. |

Prohibited state values include "looks polished," unexplained confidence, and "accessible" or "responsive" without scope and evidence.

**Block B: target, instruction, source, and authority identity**

| artifact_field_name | artifact_completion_rule | evidence_source_hint |
| --- | --- | --- |
| `target_identity` | Repository/app root, revision, branch/working state, route/build/deployment, dependencies, browser config, and sensitive-data boundary. | Version control, manifests, environment. |
| `instruction_chain` | Applicable user, repository, directory, frontend, product, content, accessibility, and domain instructions with precedence. | Active instruction sources. |
| `source_registry` | Stable IDs for product/design/source/rendered/public evidence with path/URL, hash/version, date, scope, authority, and read state. | Source hierarchy. |
| `duplicate_and_conflict_state` | Group hash-equal sources and preserve design/code/product contradictions without voting. | Hash and mismatch ledger. |
| `existing_system_inventory` | Routes, shells, navigation, components, tokens, type, icons, assets, stories/tests, data/state/query layers, and consumers. | Target repository and browser. |
| `owner_authority_state` | Exact task, content, visual, support, accessibility, or residual-risk decision accepted, with scope/date. | Review/approval system. |
| `source_invalidation` | Name product, hash, dependency, token, content, browser, policy, or owner change that reopens claims. | Dependency graph. |

**Block C: user journey and state registry**

| artifact_field_name | artifact_completion_rule | evidence_source_hint |
| --- | --- | --- |
| `journey_identifier` | Stable ID for one actor-visible task from entry through completion/recovery. | User goal and routes. |
| `journey_entry_and_exit` | Preconditions, start route/state, success outcome, cancellation, and recovery exit. | Product contract. |
| `state_identifier` | Stable state/transition identity for default, loading, empty, partial, error, permission, disabled, pending, success, stale, offline, or product-specific states. | State model. |
| `state_trigger` | User action, data response, permission, time, browser/runtime, content, or external event. | Query/mutation/runtime semantics. |
| `user_visible_outcome` | Content, structure, control state, feedback, focus, announcement, and next valid action. | Experience contract. |
| `side_effect_and_safety` | Mutation, persistence, navigation, data loss, idempotency, cancellation, and duplicate-action behavior. | Service/product contract. |
| `state_dependencies` | Shared data, components, tokens, assets, content, owner decisions, and downstream transitions. | Claim graph. |
| `state_invalidation` | Premise changes that require redesign, reimplementation, or rerender. | Product/source graph. |

Do not require every generic state in every interface. Require every state whose omission can alter the bounded task or claimed quality.

**Block D: semantic, accessibility, and input contract**

| artifact_field_name | artifact_completion_rule | evidence_source_hint |
| --- | --- | --- |
| `semantic_structure` | Landmarks, headings, regions, lists/tables/forms, reading order, and content relationships. | DOM/product content. |
| `control_contract` | Familiar control type, accessible name, role, value/state, disabled/pending/error behavior, and tooltip/help where needed. | Component/design system. |
| `input_paths` | Pointer, keyboard, touch, voice/switch or other applicable modes with equivalent task outcome. | Product support and tests. |
| `focus_contract` | Initial, transition, modal/pane, error, removal, and return focus behavior. | State graph and browser evidence. |
| `status_and_error_communication` | Visible text, programmatic relationship/announcement, timing, persistence, and recovery. | Product/accessibility policy. |
| `preference_and_display_states` | Reduced motion, theme, contrast, zoom/text, and other supported preferences. | Target policy and browser. |
| `assurance_boundary` | Automated, keyboard, semantic, assistive, expert, and owner evidence required plus explicit exclusions. | Consequence and policy. |

**Block E: composition and visual system**

| artifact_field_name | artifact_completion_rule | evidence_source_hint |
| --- | --- | --- |
| `information_hierarchy` | Primary task/content, secondary context, command priority, reading/scan order, and density rationale. | User journey and product mode. |
| `responsive_contract` | Container/viewport transformations, stable tracks/dimensions, wrap/reflow, overflow policy, content extremes, and unsupported modes. | Layout source and support matrix. |
| `typography_roles` | Display/body/label/data/status roles, current-system fit, content/locale/loading/fallback, and text-fit expectations. | Tokens/brand/content. |
| `color_and_surface_roles` | Neutral/semantic/accent/background/border/focus/selection/error roles with non-color cues and modes. | Design system and accessibility evidence. |
| `spacing_density_geometry` | Grid, rhythm, card/surface boundaries, control targets, aspect ratios, and stable dynamic-state dimensions. | Product frequency and rendered state. |
| `icon_and_control_language` | Established library, icon semantics, text exceptions, tooltips, and state variants. | Current design system. |
| `media_asset_contract` | Actual subject, provenance, crop/fit, dimensions, loading/error/fallback, alt/content purpose, and privacy. | Asset system and content owner. |
| `motion_contract` | Causal role, trigger, duration/easing policy if owned, interruption, reduced motion, layout stability, and performance. | State transitions and product direction. |
| `distinctive_signal` | Small set of memorable product/subject-specific choices and why they fit. | Direction review. |
| `visual_non_goals` | Trend, effect, component, palette, or composition deliberately avoided and why. | Tradeoff record. |

**Block F: component, implementation, and ownership plan**

| artifact_field_name | artifact_completion_rule | evidence_source_hint |
| --- | --- | --- |
| `component_boundary` | Existing/new components, responsibilities, semantic root, state/data ownership, composition contract, and consumers. | Architecture/source. |
| `reuse_adapt_diverge` | For each current primitive, record reuse, bounded adaptation, new component, or governed migration rationale. | Design-system inventory. |
| `data_and_async_boundary` | Query/mutation/auth/cache/subscription ownership, cancellation, stale/conflict, errors, and recovery. | Target stack. |
| `route_and_navigation` | URL/history/back/deep-link, shell, pane/modal, selection restoration, and unauthorized/not-found behavior. | Router/product contract. |
| `asset_and_dependency_change` | New/changed media, font, icon, library, engine, bundler, permissions, and lifecycle. | Manifest/assets. |
| `changed_path_ownership` | Exact owned paths and preservation of unrelated user/agent work. | Status and assignment map. |
| `implementation_recovery` | Revert, feature flag, fallback, migration rollback, or diagnostic route. | Project operations. |

**Block G: bidirectional behavior and quality matrix**

| artifact_field_name | artifact_completion_rule | evidence_source_hint |
| --- | --- | --- |
| `check_identifier` | Stable unit/component/integration/browser/accessibility/screenshot/performance/review identity. | Project verification. |
| `journey_state_links` | Link every check to user journey, state, requirement, visual claim, or invariant it observes. | State registry. |
| `fixture_content_environment` | Exact data, auth, errors, content lengths, viewport/container, browser/device, input, preferences, theme/locale, and network. | Test/render plan. |
| `oracle_or_review_rule` | Independently observable pass and fail outcome; visual criteria include direction and hierarchy, not pixel sameness only. | Experience contract. |
| `expected_failure_reason` | Why pre-change behavior should fail and which unrelated harness failures invalidate evidence. | Reproduction. |
| `coverage_and_no_claim` | States, users, browsers, content, assistive paths, and performance conditions left outside. | Risk/support matrix. |
| `reverse_traceability` | Orphan stories/tests/screenshots, undocumented current behavior, and stale baselines resolved or retained explicitly. | Complete audit. |

**Block H: rendered evidence manifest**

| artifact_field_name | artifact_completion_rule | evidence_source_hint |
| --- | --- | --- |
| `render_identifier` | Stable ID linked to target revision, state, check, and attempt. | Screenshot/browser run. |
| `route_state_content` | Exact URL/entry, data/auth/async state, representative and extreme content, and selected element. | Fixture. |
| `viewport_environment` | Container/viewport, DPR, browser/device, theme, locale, preferences, network, and graphics as applicable. | Browser config. |
| `artifact_locator_hash` | Authorized screenshot/video/trace/DOM/accessibility/log locator, size/hash, and retention/privacy. | Evidence storage. |
| `pixel_geometry_result` | Text fit, overlap, clipping, spacing, stable dimensions, image/canvas visibility, and first-viewport checks. | Rendered inspection. |
| `interaction_runtime_result` | Focus, input, animation, state change, console/page/network errors, and recovery. | Browser run. |
| `visual_review_result` | Direction fit, hierarchy, coherence, subject signal, density, alternatives, dissent, and owner decision. | Experienced review. |
| `render_invalidation` | Component, token, content, fixture, asset, browser, or capture-harness change that stales it. | Dependency graph. |

**Block I: measurement and performance status**

| artifact_field_name | artifact_completion_rule | evidence_source_hint |
| --- | --- | --- |
| `measurement_hypothesis` | One interaction/rendering change, metric direction, causal mechanism, and decision effect. | Performance section. |
| `baseline_and_candidate` | Code/build/assets/config/fixture identities with unrelated changes excluded. | Version control. |
| `workload_environment` | State, data/content, browser/device, network/cache, concurrency, graphics, and instrumentation. | Benchmark/profile. |
| `sample_statistics` | Raw count, failures/exclusions, summary method, uncertainty, and outlier policy. | Measurement output. |
| `quality_countermetrics` | Task/functional, visual, accessibility, errors, resources, layout stability, and recovery equivalence. | Behavior/rendered gates. |
| `measurement_result_state` | Unexecuted design, diagnostic observation, controlled result, representative result, or operational observation. | Evidence taxonomy. |
| `owner_decision` | Adopt, reject, investigate, reroute, or select budget with scope and rationale. | Accountable owner. |

**Block J: mismatch, release, recovery, and invalidation**

| artifact_field_name | artifact_completion_rule | evidence_source_hint |
| --- | --- | --- |
| `mismatch_identifier` | Earliest product/source/state/semantic/composition/visual/implementation/render/measurement stage. | Failed gate. |
| `expected_and_actual` | Separate intended experience from exact observation. | Contract and evidence. |
| `bounded_hypotheses` | Product, state, content, component, token, browser, asset, fixture, or harness causes. | Diagnostic record. |
| `distinguishing_check` | Smallest observation that separates leading causes. | Verification routes. |
| `affected_claims_surfaces` | Every state, component, viewport, screenshot, metric, or release decision invalidated. | Dependency links. |
| `verification_outcome` | Pass, fail, contradiction, not applicable with reason, or not run with blocker. | Captured gate. |
| `decision_result` | Proceed, proceed within scope, revise, reject, or escalation required per branch. | Claim and owner record. |
| `residual_risk_owner` | Remaining uncertainty, consequence, accountable acceptance, policy, and review trigger. | Owner decision. |
| `rollback_or_recovery` | Exact reversal/containment and evidence to inspect after failure. | Project operation. |
| `next_action` | Nonempty executable step, owner, prerequisite, and stop condition. | Unresolved or accepted work. |

**Quality-bar blocker view**

| blocker class | block when | release when |
| --- | --- | --- |
| Product/task blocker | User goal, content, or authority is materially unresolved. | Owner/current contract establishes the bounded experience. |
| State/behavior blocker | Primary task, error, permission, pending, stale, or recovery behavior is missing/wrong. | Claim-capable checks and rendered state pass. |
| Accessibility/input blocker | Required semantics, names, focus, keyboard/input, status, or preference path fails. | Applicable multimodal evidence passes. |
| Responsive/content blocker | Text, controls, media, or hierarchy overlap/clip/hide under supported conditions. | Risk-based container/content matrix passes. |
| Visual-direction blocker | Interface is generic, incoherent, subject-hidden, or mismatched to product mode. | Experienced review can trace coherent decisions to task/subject and actual render. |
| Asset/media/3D blocker | Primary media is broken, misleading, blank, misframed, inaccessible, or lacks required fallback. | Target pixel/runtime/input/fallback gates pass. |
| Runtime blocker | Console/page/network failures or stuck state affect the task. | Corrected behavior and observability/recovery evidence pass. |
| Quantitative blocker | Accepted budget/result lacks workload, baseline, sample, equivalence, or owner. | Controlled packet and bounded owner decision exist. |
| Ownership/lifecycle blocker | Shared change lacks owner, migration, rollback, or invalidation. | Governance and consumer evidence pass. |

**Packet acceptance checklist**

A standard or high-assurance packet is accepted only when:

- user, product mode, target, instructions, source, design authority, and working state are reconstructable;
- duplicate sources and product/design/code/rendered conflicts are explicit;
- every material state and transition has user-visible behavior or an owned unresolved branch;
- semantics, controls, input, focus, status, responsive, content, and accessibility boundaries match consequence;
- visual direction is coherent, product-specific, and expressed through a bounded system rather than decorative accumulation;
- shared components/tokens/assets have consumer, compatibility, ownership, and migration evidence as needed;
- material states have capable checks and every retained test/story/screenshot names what it governs;
- actual rendered evidence covers the risk-based state/content/container/browser/input matrix;
- expected failures demonstrate that behavior and visual gates can reject the named defect;
- quantitative language has a complete result or remains explicitly unexecuted/unresolved;
- implementation stayed inside authorized paths and preserved unrelated work;
- each pass states its no-claim boundary;
- split outcomes, residual risk, rollback/recovery, invalidation, and next action are nonempty;
- evidence storage and assets follow privacy, security, licensing, and retention policy.

Good packet: links an operator workflow and current design system to loading/error/stale/action states, keyboard and browser checks, narrow/wide rendered evidence, a restrained visual direction, and an unresolved performance branch.

Bad packet: pastes ideal screenshots, labels the design modern and accessible, omits state/content/browser identity, and declares release from a build result.

Recoverable packet: preserves current browser pixels and source identity but lacks product intent. It can support a narrow visual-regression observation; redesign, user-outcome, and release-policy claims remain downgraded until authority is reconstructed.

The packet is a human-readable experience graph. For durable work it enables review of the smallest changed state/surface cut. For focused corrections the reduced profile prevents evidence management from costing more than the user problem it protects.

## Worked Example Set

All products, routes, components, assets, states, checks, and outcomes below are illustrative. The examples use mechanisms supported by local guidance and frontend systems reasoning, but no target fixture or browser session was created for this assignment.

Every example answers:

| field | question |
| --- | --- |
| User task and product mode | What is the person trying to do, how often, and what kind of interface is this? |
| Authority | Which product, content, design-system, code, or owner source can choose the experience? |
| State and visual decision | Which behavior and presentation choice controls the action? |
| Expected failure | How can the pre-change or unsafe version demonstrate the defect? |
| Verification | Which independent mechanisms can support or refute the claim? |
| Missing evidence | Which users, states, content, browsers, devices, or outcomes remain outside? |
| Bounded conclusion | What can be implemented or accepted now? |
| Rejected overclaim | Which attractive statement exceeds the evidence? |
| Invalidation | What future change reopens the result? |

**Example 1: Build the requested application, not a landing page**

User task and product mode: authenticated support agents need to search conversations, compare priority, open one case, reply, and recover a failed send. This is a repeated operational application.

Authority: current product workflow, routes, design system, messaging contract, and support owner. The local design skill contributes intentional visual direction, not page category.

Bad route: create an oversized gradient hero, feature cards, testimonial copy, and a "Get started" call to action while the inbox is a small preview below the fold.

Better route: render the real inbox as the first screen with stable navigation, search/filter, queue/list, detail/reply, loading/empty/error/permission/send-pending/send-failure states, familiar icon controls with accessible names, and a quiet product-specific visual hierarchy.

Expected failure: a user-flow fixture cannot search, select, or send through the marketing composition; error/retry state is absent.

Verification: repository behavior checks, keyboard/focus flow, representative message lengths, populated/empty/error/send-failure states, and wide/narrow browser screenshots.

Missing evidence: production message volume, every locale, every assistive technology, and real support-agent outcome.

Bounded conclusion: the operational interface form is supported for the named workflow and matrix. Rejected overclaim: "This is the best possible support design." Invalidation: product task, navigation shell, message contract, support matrix, or design-system change.

Future replay: inject a request description containing marketing language while the authoritative route is an app. The planning gate must preserve the app form and expose the requested task on first screen.

Transferable rule: page form follows the user's primary job, not the most visually dramatic template an agent can generate.

**Example 2: Preserve comparison density without nested cards**

User task and product mode: finance operators compare many invoice exceptions and apply a small set of repeated commands.

Authority: operator workflow, current table semantics, product density policy, and design-system primitives.

Alternatives:

| option | benefit | failure risk | target evidence |
| --- | --- | --- | --- |
| Card per invoice | Clear item boundaries and flexible content. | Weak comparison, long page, nested controls/cards, low density. | Low-volume or touch-first workflow. |
| Dense table | Cross-row comparison and repeated scan. | Content overflow, narrow/touch pressure, table semantics. | Field priority, content distribution, support matrix. |
| Grouped list with aligned metadata | Responsive compromise and clearer hierarchy. | Less precise comparison and custom alignment complexity. | Operator task and container evidence. |

Assume target evidence favors a table. The design uses an unframed full-width work surface, restrained dividers, stable columns/action width, semantic status text plus color, row focus/selection, and a detail route or pane. It does not put the table in a card inside a dashboard card.

Expected failure: long vendor/status text and high selected-count state clip actions in the current narrow layout.

Verification: content-extreme fixtures, horizontal/transform policy, keyboard/table semantics, selection/action states, and container screenshots.

Missing evidence: phone parity and every data distribution. Bounded conclusion: current operator matrix supports the chosen dense composition. Rejected overclaim: "Cards are always bad." Invalidation: task frequency, data fields, input support, or component contract changes.

Future replay: render many rows, long fields, empty/error states, row action menus, zoom, and the narrow supported container. The primary command and semantic order must remain available.

Transferable rule: density is a user-task choice; structure and stable geometry make dense interfaces designed rather than cluttered.

**Example 3: Use a familiar icon control with complete semantics**

Decision: replace a toolbar's rounded text pills "Undo change," "Redo change," "Zoom in," and "Zoom out" with the current icon library where users repeat these actions frequently.

Authority: editor command semantics, current icon system, keyboard shortcuts, accessibility policy, and user frequency.

Contract:

- Each action is a semantic button with a unique accessible name.
- Disabled state reflects command availability and is programmatically exposed.
- Familiar icons occupy stable dimensions; hover/focus/pressed/disabled states do not shift layout.
- Tooltips may reinforce meaning but are not the accessible name.
- Keyboard shortcuts remain discoverable through the product's existing mechanism, not explanatory clutter inside the canvas.

Tradeoff: an infrequent consequential command may remain icon+text because clarity outweighs density. A novel domain tool may need a label or onboarding evidence.

Expected failure: remove the accessible name or change state without disabling; semantic/keyboard checks must fail even though the screenshot looks normal.

Verification: accessibility-tree inspection, keyboard path, command behavior, tooltip/focus behavior, stable-state screenshots, and design-system review.

Missing evidence: every user's icon familiarity. Bounded conclusion: the current repeated tools use established semantics without losing accessibility. Rejected overclaim: "Icon-only controls are always better." Invalidation: command meaning, icon library, toolbar density, input mode, or accessibility contract changes.

Future replay: test enabled/disabled states, focus order, accessible names, pointer and keyboard activation, and longest localized tooltip.

Transferable rule: choose the control whose learned semantics and evidence best fit the command; do not use text pills or icons mechanically.

**Example 4: Design responsive behavior around content pressure**

Decision: a booking summary has a two-column desktop composition but long venue names, validation messages, dynamic prices, and narrow embedded containers cause overlap.

Authority: booking workflow, content/localization policy, current form controls, supported containers, and payment/recovery contract.

Bad repair: reduce font size with viewport width, hide secondary labels, set a fixed panel height, and clip overflow.

Better repair:

- Keep semantic type roles stable and allow controlled wrapping/reflow.
- Define grid tracks with min/max behavior and a composition change when the task hierarchy no longer fits.
- Reserve stable regions for totals and primary action without fixed content height.
- Keep field errors adjacent, focusable/announced, and inside the flow.
- Constrain media/aspect rather than letting it push commands out of view.
- Preserve DOM/focus order through visual transformation.

Expected failure: longest venue, large price, several field errors, increased text scale, and narrow container overlap the primary action in the old layout.

Verification: geometry/text-fit assertions, screenshots across content/container/zoom states, keyboard/error focus, and actual form behavior.

Missing evidence: all languages, devices, and payment provider states. Bounded conclusion: named extremes and supported containers no longer overlap. Rejected overclaim: "The page is responsive everywhere." Invalidation: content distribution, form fields, type tokens, container embedding, or support policy changes.

Future replay: inject longest localized content and multiple errors rather than a short ideal fixture. Any clipping or occlusion must fail before screenshot acceptance.

Transferable rule: responsive quality is content and task preservation, not shrinking a desktop screenshot.

**Example 5: Make a branded subject visible without a generic split hero**

User task and product mode: a visitor evaluates a coastal hotel and needs to recognize the place, inspect rooms/setting, understand the literal offer, and continue to availability.

Authority: brand/content owner, accurate property media, booking workflow, current shell, and asset rights.

Direction: a full-bleed first viewport uses a clear high-information property image, hotel name as the main heading, concise supporting proposition, and direct availability action. Text is not placed inside a decorative card, and a visible next-section cue reveals room/location content on wide and mobile viewports.

Bad route: put copy on the left and a dark atmospheric image card on the right, use a vague aspirational headline instead of the hotel name, and hide actual property imagery below several cards.

Expected failure: replace the primary image with a broken, dark, generic, or severely cropped asset. The subject-visibility/fallback gate must reject or preserve a truthful usable state.

Verification: media provenance/content review, first-viewport desktop/mobile screenshots, text contrast/crop, failed/slow asset state, keyboard/CTA, and next-section visibility.

Missing evidence: real conversion improvement and every device crop. Bounded conclusion: the place and literal offer are legible/inspectable in the supported matrix. Rejected overclaim: "Full-bleed heroes always convert better." Invalidation: offer, media rights/content, brand type/color, page shell, or booking route changes.

Future replay: test real aspect ratios, slow/failure states, longest offer copy, and target viewports; the property and command must remain clear.

Transferable rule: branded/object pages should reveal the actual subject early; atmosphere supports identity but cannot substitute for evidence-rich media.

**Example 6: Verify a full-bleed Three.js product viewer**

User task and product mode: a shopper rotates and inspects a configurable object whose shape and finish are important to selection. 3D is the primary inspection tool, not decoration inside a preview card.

Authority: product geometry/material content, interaction requirements, current Three.js dependency, supported browsers/devices, accessibility/fallback policy, and performance owner.

Contract:

- Scene fills the intended primary region without a decorative card frame.
- Canvas has stable size and correct device-pixel handling; camera frames the object on required viewports.
- Assets/materials/lights produce meaningful nonblank pixels and truthful finishes.
- Pointer/touch/keyboard alternatives and reset/help follow product policy.
- Loading, asset error, context loss, unsupported graphics, reduced motion, and fallback states preserve product information and purchase path.
- Animation/input stops or disposes correctly when route/component state changes.

Bad check: source imports Three.js and build passes, so the scene is declared complete. The canvas can still be transparent, zero-sized, off-camera, asset-failed, or covered by UI.

Expected failure: move camera away or fail model load. Canvas pixel/asset/fallback checks must reject the intended scene claim.

Verification: target browser screenshots at wide/mobile, meaningful nonblank pixel analysis, camera/object framing, input/animation, resize, console/WebGL, asset/network, cleanup, fallback, and controlled performance with functional/visual equivalence.

Missing evidence: every GPU, production network, and user outcome. Bounded conclusion: the viewer functions for the named matrix. Rejected overclaim: "Three.js support guarantees the product viewer works everywhere." Invalidation: model/material, renderer/dependency, camera, container, device/browser matrix, interaction, or fallback changes.

Future replay: test successful model, delayed model, failed model, context loss/unsupported path where practical, resize/orientation, route unmount, and overlapping UI. The scene must be visible and the fallback actionable.

Transferable rule: a 3D implementation is a rendered system with pixels, lifecycle, input, and fallback; source structure cannot certify it.

**Good, bad, and borderline synthesis**

| classification | behavior | promotion or downgrade trigger |
| --- | --- | --- |
| Good example | Uses current product authority, complete relevant states, coherent product-mode direction, repository-native implementation, and complementary rendered evidence. | Promote only after claim-specific behavior, accessibility/input, visual, and owner gates pass. |
| Bad example | Copies page forms, effects, components, screenshots, or green output while hiding user task, state, semantics, content pressure, or runtime. | Withdraw/reconstruct before implementation or release. |
| Borderline case | Retains a concept, manual screenshot, stale hint, or focused correction only for a narrow reversible decision with visible limitations. | Promote through missing states/contexts before broader use; downgrade immediately after invalidation. |

**Fixture promotion criteria**

Promote an explanatory example into a component story, browser fixture, regression screenshot, or shared quality gate when the mechanism recurs or carries severe consequence, can use safe representative data/assets, has deterministic expected state differences, and has an owner. Record the unsafe inference, positive/negative cases, environment, no-claim boundary, and retirement conditions. Do not encode every visual preference as a brittle snapshot; preserve cases whose replay protects a user decision.

## Outcome Metrics and Feedback Loops

No outcome value was measured while evolving this reference. Every measure below is a future capture definition, not a current result, universal target, user-satisfaction claim, or productivity improvement. Establish target baselines under stable definitions, retain raw evidence and cohort identity, and refuse comparison when product mode, user/task, state fixtures, content, browser, component/design-system version, or review method changes materially.

Leading indicator: every material user journey reaches its defined outcome and recovery across the required state/input/render matrix without introducing a known layout, accessibility, runtime, or design-system regression. Count material journeys and states; do not reward extra components, tokens, screenshots, or checks.

Failure signal: the work is called frontend quality improvement while the actual user workflow, failure states, current system, rendered evidence, or no-claim boundary is absent.

Review cadence: run focused structural gates after every atomic reference/packet edit; review each changed frontend state as it is implemented; rerender affected state/content/container/browser evidence after the relevant source changes; run complete user-critical flow and system-level review before release. Refresh public sources only after an applicable producer/version change or blocked decision. Do not invent periodic schedules without workload and owner evidence.

**Metric card contract**

| field | completion rule |
| --- | --- |
| Decision purpose | Name the component, pattern, design-system, workflow, support matrix, or release decision the result can change. |
| Definition | State numerator, denominator, unit, inclusion/exclusion, materiality, deduplication, and success/failure rules. |
| Cohort | Record product mode, journey/state, users, repository/revision, component/token version, content/data, browser/device/input/preferences, and period. |
| Sampling | Exhaustive, fixture, random, stratified, risk-based, usability-task, or incident selection and why it represents the claim. |
| Raw evidence | Retain state/check IDs, screenshots/geometry, accessibility findings, task outcomes, errors, timings, reversals, or recalculation source. |
| Counter-metric | Name the quality/safety signal that prevents optimizing appearance, speed, density, or output volume alone. |
| Uncertainty | Report sample size, missing states/users, bias, reviewer disagreement, environment limits, and no-comparison state. |
| Trigger | Define what change prompts investigation rather than an unsupported universal threshold. |
| Action | Fix, adapt, reroute, retire, collect evidence, narrow support, or no change. |
| Invalidation | Product, state, content, component, token, asset, browser, harness, reviewer, or policy change that breaks comparability. |

**Deterministic integrity gates**

These establish enumerated properties, not user satisfaction or visual effectiveness.

| gate metric | definition | pass interpretation | what it does not prove |
| --- | --- | --- | --- |
| `source_authority_identity_complete` | Every material product/design/source/render/public claim has required identity, scope, authority, and freshness state. | Decision provenance can be reconstructed. | That desired workflow or design is correct. |
| `journey_state_population_complete` | Every material journey branch and applicable loading/empty/error/permission/pending/success/recovery state is present or explicitly excluded. | No known enumerated state is silently omitted. | That state behavior is usable or sufficient. |
| `state_check_link_complete` | Every material state/claim maps to at least one capable candidate check and every retained check/story/screenshot maps back. | No structural orphan remains. | Oracle independence or appropriate fixture coverage. |
| `render_manifest_complete` | Every required rendered artifact has target revision, route/state/content, viewport/container, browser/input/preferences, locator/hash, and review state. | Pixel evidence is traceable. | Correct pixels, semantics, or broad support. |
| `text_overlap_blocker_clear` | Enumerated required state/content/container renders contain no detected clipping/occlusion/hidden command under defined geometry checks and review. | Named matrix avoided observed text/layout defects. | All possible content or devices. |
| `accessible_control_identity_complete` | Enumerated interactive controls have semantic type, accessible name/state, focus/input contract, and relevant error/status linkage. | Required control metadata exists. | Full usability or every assistive technology. |
| `runtime_error_gate_clear` | Named user-critical browser runs contain no unclassified console/page/network/asset/graphics error affecting task. | Observed runs have classified runtime state. | Unexercised paths or production reliability. |
| `invalidation_route_complete` | Durable experience claims name premise changes, dependent evidence, owner, and replay route. | Reuse lifecycle is explicit. | That future drift will be detected automatically. |

Do not combine deterministic passes into a synthetic interface-quality score. All can pass while information hierarchy or product intent is wrong.

**Sampled experience quality indicators**

| indicator | numerator | denominator | required stratification | misuse warning |
| --- | --- | --- | --- | --- |
| `primary_task_completion` | Sampled users/fixtures completing the defined journey outcome without prohibited side effect. | All sampled journey attempts. | User type, product mode, state, input, device/browser, familiarity, and consequence. | Completion alone can hide confusion, accessibility barriers, or unsafe workarounds. |
| `failure_state_recovery_success` | Sampled error/stale/permission/offline/mutation cases reaching the approved recovery/containment. | Applicable sampled failure cases. | Failure class, reversibility, data loss, auth, and environment. | More retries can look like recovery while repeating unsafe actions. |
| `keyboard_task_path_success` | Sampled required tasks completed with coherent focus and no pointer dependency. | Required keyboard task attempts. | Journey, component, browser, focus complexity, and state. | Keyboard success does not establish all accessibility needs. |
| `control_semantic_capability` | Sampled controls whose names/roles/states/errors are correct and whose checks fail under representative violation. | Sampled material controls with injected/reviewed violations. | Control type, state, design-system primitive, and consequence. | Easy metadata checks can overstate real usability. |
| `responsive_content_fit` | Sampled state/content/container combinations with no task-breaking overlap, clipping, hidden command, or incoherent hierarchy. | Sampled required combinations. | Content type/length, viewport/container, zoom/locale, product mode. | Screenshot count can reward redundant easy cases. |
| `visual_direction_reconstruction` | Reviews where another qualified reviewer identifies the intended product mode, hierarchy, distinctive signal, and rejected alternatives from the actual interface/evidence. | Sampled reviewed surfaces. | Reviewer role, product familiarity, surface type, and state. | Agreement does not prove user preference or outcome. |
| `subject_visibility_success` | Branded/product/place/object/gameplay states where required real subject is identifiable and inspectable. | Sampled subject-critical renders. | Asset type, crop, loading/failure, viewport, and content. | Recognition is not conversion or truthfulness without content authority. |
| `state_visual_regression_resolution` | Material visual diffs classified as intended, corrected, baseline defect, or explicitly unresolved. | All material diffs reviewed in cohort. | Component/state, browser, snapshot harness, and risk. | Forced baseline acceptance can hide design regressions. |
| `reviewer_handoff_reconstruction` | Packets another reviewer can use to identify task, state, direction, evidence, blockers, and next action without original conversation. | Packets audited. | Profile, age, reviewer familiarity, and complexity. | Familiar reviewers can fill missing context implicitly. |

Report raw counts alongside ratios. Keep controlled fixtures, expert critique, usability tasks, and production observations in separate cohorts.

**Workflow and maintenance indicators**

| indicator | definition | useful interpretation | counter-metric |
| --- | --- | --- | --- |
| `time_to_first_rendered_task` | Elapsed/active time from clarified task to first retained working browser state with direct checks. | Source/state routing reaches actionable implementation quickly. | Final state sufficiency, rework, and late contradictions. |
| `existing_system_reuse_acceptance` | Current components/tokens accepted after fit/state/consumer review divided by reuse candidates. | Native system avoids duplicate design when appropriate. | Inherited defects and duplicate-system incidents. |
| `selected_context_usefulness` | Complete source/state units supporting, refuting, or materially contextualizing final decisions divided by inspected units under one definition. | Retrieval limits irrelevant reads while valuing eliminated options. | Missed-source and post-action reversal review. |
| `state_fixture_maintenance_rework` | Changes caused by stale stories, screenshots, content, browser, or state ownership rather than intended product behavior. | Reveals evidence lifecycle cost. | Defects prevented and handoff value. |
| `design_system_divergence_events` | New parallel primitives/tokens/interaction rules requiring reconciliation. | Signals ownership or capability gaps. | Legitimate bounded innovation and migration outcomes. |
| `visual_review_active_time` | Carefully bounded review time under stated surfaces/states and reviewer method. | Compares review burden inside stable cohorts. | Task difficulty, expertise, quality, and observation effect. |
| `route_escalation_yield` | Escalations that find confirming, refuting, or boundary-changing evidence. | Stronger product/accessibility/performance routes are selected usefully. | Necessary precaution can find no defect. |

Collect time/context only when workflow efficiency is a real decision. Do not compare unlike product modes, state counts, shared-component scope, or reviewer expertise without stating uncertainty.

**Performance and runtime indicators**

| indicator family | definition requirement | quality counter-gates |
| --- | --- | --- |
| Interaction readiness/response | Exact user action/start/stop, state/data, browser/device, network/cache, sample, failures, and statistic. | Correct state transition, no duplicate/lost action, visual feedback, accessibility status. |
| Rendering/layout | Exact navigation/update boundary, content, viewport, assets/fonts, animation, and instrumentation. | Complete pixels/content, no overlap, stable task, no hidden errors. |
| Media/3D | Asset/load/camera/frame/input/animation boundary, GPU/browser/device, failures, and resources. | Meaningful nonblank subject pixels, interaction, fallback, cleanup, and fidelity. |
| Workflow completion | User/task start/end and active time under representative conditions. | Correct outcome, errors, accessibility, user cohort, and no workarounds. |

Do not report p50/p95/p99 merely because the seed requests them. Tail labels require enough comparable observations, a stated quantile method, raw counts, failure treatment, and a decision that needs them.

**Downstream outcome indicators**

| indicator | definition | feedback meaning | latency |
| --- | --- | --- | --- |
| `pre_release_experience_reversal` | Product, state, visual, or evidence claim downgraded before release by counterevidence. | Often healthy detection that prevented escape. | Immediate. |
| `post_release_experience_reversal` | Accepted claim reopened because a material user/state/content/browser premise was missed or stale. | Investigate source, packet, gate, and owner failure. | Delayed. |
| `escaped_primary_task_defect` | Released interface claimed sufficient but a user cannot complete/recover the promised task. | High-severity lagging signal. | Potentially long. |
| `escaped_accessibility_barrier` | Required user/input/semantic path was blocked after acceptance. | Audit policy, state matrix, tools, review, and ownership. | Immediate or delayed. |
| `responsive_content_escape` | Real supported content/container causes overlap, clipping, hidden control, or incoherent order after acceptance. | Improve content/state matrix and layout primitives. | After content/device exposure. |
| `generic_form_mismatch_event` | Delivered page form conflicts with actual product mode or task. | Improve fit/agent trigger and product-context evidence. | Review or user feedback. |
| `safe_abstention_or_route` | Consequential content/design/accessibility/performance claim remained unresolved or moved to capable owner before unsupported action. | Shows appropriate containment. | Immediate; do not maximize without context. |
| `experience_invalidation_timeliness` | Time between known premise change and downgrade/rerender of dependent evidence. | Tests stale screenshot/contract reuse control. | Event-driven. |
| `recovery_record_success` | Failure record identifies premise, states/surfaces, rollback, owner, and next evidence without full-session reconstruction. | Tests durable handoff. | Review/incident time. |

A pre-release reversal is not necessarily failure. Discovering that a current screenshot baseline preserves a clipped action before rollout shows that the loop worked. The same discovery after a supported user fails is more concerning.

**Feedback routing**

| observed signal | likely stage | first investigation | possible durable action |
| --- | --- | --- | --- |
| Users cannot find the primary command. | Product/hierarchy/control. | Product mode, task frequency, visual priority, label/icon, and state. | Change hierarchy/control primitive and add task fixture. |
| Error/recovery often missing. | State model. | Happy-path bias, service contract, mutation/query ownership, and fixture coverage. | Add state-contract field and shared failure primitive. |
| Long content repeatedly clips controls. | Composition/token/component. | Fixed heights, unstable dimensions, typography, grid tracks, and fixture content. | Improve layout primitive and long-content screenshot gate. |
| Automated accessibility passes but keyboard fails. | Verification capability. | Focus, semantic state, hidden content, overlay, and tool blind spot. | Add keyboard/focus gate and narrow scanner claim. |
| Visual baselines preserve known defects. | Evidence authority. | Baseline owner, update policy, intended/unintended diff, and stale product contract. | Add baseline classification and owner review. |
| New pages duplicate current system. | Source/architecture. | Agent fit, component discovery, capability gap, and ownership. | Improve reuse inventory or launch governed system migration. |
| 3D/media looks complete in code but fails in browser. | Render/runtime gate. | Canvas size, camera, assets, graphics, overlay, lifecycle, fallback. | Add pixel/runtime/failure fixture and specialized route. |
| Faster completion correlates with later state regressions. | Workflow incentive. | Skipped state mapping, screenshots, or final browser verification. | Add counter-metric and revise completion gate. |

**Good, bad, and sentinel interpretations**

Good: "Under the same component/state/content/browser matrix, more sampled controls exposed their injected semantic/state failures while post-release reversals and task completion did not worsen. Raw cases and disagreements are retained." This is bounded local process evidence.

Bad: "The redesign generated more components, screenshots, and a higher automated score, so frontend quality improved." Volume and tool scores can rise while users lose the task.

Sentinel: one destructive action applied to a stale selection or one primary control inaccessible by required input can justify a mandatory blocker even with too few events for a stable rate. Preserve causal evidence rather than manufacturing a percentage.

**Feedback loop**

1. Capture a deterministic gate failure, rendered mismatch, user/task outcome, reversal, accessibility barrier, or runtime defect with exact identity.
2. Classify the earliest verified product/source/state/semantic/composition/visual/implementation/render/measurement mechanism.
3. Decide whether to fix a component/token, improve a fixture/gate, adapt guidance, route to product/domain authority, retire a pattern, or gather a better cohort.
4. Replay relevant controlled states and representative target surfaces under the new version.
5. Begin a new comparable series only when definitions and cohorts remain compatible; retain prior results historically.
6. Confirm improvement in the protected user decision without degrading counter-metrics or silently narrowing support.

The most important outcome can be an earlier stop. If recurring evidence shows that a claim class cannot be decided safely without product, content, accessibility, runtime, or owner authority, success is routing it before polished weak evidence reaches release.

## Completeness Checklist

Use this checklist as revisitable phase gates, not a one-pass form. Every completed item points to evidence. Every conditional omission explains why it does not apply to the user task. A critical failure blocks dependent promotion even if later artifacts were previously green.

**Status types**

| status | meaning | valid evidence |
| --- | --- | --- |
| Machine pass | Deterministic identity, shape, schema, hash, link, syntax, geometry, or hygiene property passed. | Captured parser, command, or browser-geometry result. |
| Semantic/product/design pass | Task, authority, hierarchy, state, visual direction, alternatives, and meaning were reviewed. | Decision record with exact locators, rendered states, and rationale. |
| Project behavior pass | Target implementation produced required task/state observation under named environment. | Unit/component/integration/browser/runtime result. |
| Rendered experience pass | Actual pixels, DOM/accessibility, input, content, assets, and runtime were inspected for a named matrix. | Render manifest and review. |
| Authorized acceptance | Accountable owner accepted behavior, direction, support scope, or residual risk under policy. | Project approval mechanism with invalidation. |

A machine or screenshot pass never implies the other statuses.

**Gate A: reference-construction completeness**

| seed requirement | completion evidence | severity if missing |
| --- | --- | --- |
| The role scenario names user, starting state, decision, and trigger. | Section 010 follows an operations request through evidence, product mode, state graph, requirements, implementation, split evidence, and invalidation. | Stop reference completion because use remains abstract. |
| Decision guide includes Adopt when, Adapt when, Avoid when, and Cost of being wrong. | Section 011 preserves all four and adds system, product, composition, control, state, visual, media, motion, responsive, and verification decisions. | Stop recommendations until fit and error cost are explicit. |
| Local corpus hierarchy identifies canonical/supporting sources or warns. | Section 012 preserves seed roles, records duplicate bytes and unexplained rationale, and adds claim-specific authority. | Stop source-backed claims until authority/uncertainty are visible. |
| Theme-specific artifact is reviewable without every source. | Section 013 defines a linked experience packet with stable locators, states, design system, implementation, render, blockers, and invalidation. | Stop durable handoff; focused direct evidence may continue. |
| Examples cover good, bad, and borderline usage. | Section 014 provides six orthogonal examples, rejected overclaims, replay gates, and lifecycle transitions. | Stop training/reference completion if boundaries remain abstract. |
| Metrics name leading indicator and failure signal. | Section 015 defines both plus deterministic, sampled, workflow, runtime, downstream, and feedback measures without results. | Stop outcome claims; implementation can continue. |
| Adjacent routing points to a better reference. | Section 017 must route by missing product, code, accessibility, asset, 3D, performance, security, or operational capability with return states. | Stop claims outside method fit. |

Additional evolution requirements:

| requirement | verification | severity |
| --- | --- | --- |
| Exactly 26 original heading levels/text/order remain. | Fence-aware parse against immutable seed. | Critical structural stop. |
| Every evolved section is strictly longer than matching seed. | Compare stripped section character lengths. | Critical evolution stop. |
| Packet has 26 sections and 260 exact question headings. | Parse and compare every question cycle with specification. | Critical rationale stop. |
| Packet has 1,560 populated raw and normalized-unique values. | Parse six ordered fields and current normalizer. | Critical quality stop. |
| Source/outcome claims preserve evidence types. | Audit duplicate hashes, local reads, no-browse, illustration, measurement, and owner language. | Stop or narrow unsupported claim. |
| Exclusive write ownership is preserved. | Status and scoped diff review. | Critical shared-workspace stop. |
| Markdown/text hygiene passes. | ASCII, tables, fences, tabs, whitespace, final newline, prohibited markers, and diff check. | Correct before handoff. |

**Gate B: task fit and product authority**

| check | completion evidence | response if failed |
| --- | --- | --- |
| Primary user, task, frequency, environment, and consequence are explicit. | Experience statement and non-goals. | Clarify or route product discovery. |
| Product mode matches requested experience. | Operational, transactional, content, branded, editor, game, or other rationale. | Do not default to landing-page form. |
| Desired behavior/content has legitimate authority. | User, product, domain, content, protocol, or current repository contract. | Keep unresolved; do not invent copy/policy. |
| This reference is the right next method. | Fit rationale and alternatives. | Route diagnosis, design-system governance, security, content, accessibility, performance, or operations. |
| Write, asset, browser, data, and command boundaries are authorized. | Owned paths, rights/privacy, side-effect review, and owner. | Continue read-only or stop. |
| Existing components/tokens/tests were inspected before creating new system. | Reuse/adapt/diverge record. | Inspect native authority and prevent duplicate truth. |

**Gate C: source and evidence integrity**

| check | evidence | pass limitation | severity |
| --- | --- | --- | --- |
| Every source identity is reconstructable. | Path/URL, hash/version, date, scope, read state, and authority. | Does not prove truth or fit. | Critical for durable claim. |
| Duplicate paths do not multiply weight. | Hash family and path/package identities. | Does not provide independent corroboration. | Stop inflated claim. |
| Product/design/code/render conflicts remain separate. | Mismatch, owners, and affected states. | Conflict may require owner, not technical fix. | Stop dependent implementation. |
| External status is accurate. | Unrefreshed/refreshed/reproduced/conflicting/unavailable/inapplicable. | Does not prove target behavior without target gate. | Stop current external claim. |
| Inference and illustration are visible. | Premises, conditions, and falsification route. | Does not prove user outcome. | Narrow wording. |
| Freshness and invalidation are explicit. | Trigger mapped to states/components/evidence. | Does not guarantee notification. | Critical for reuse. |

**Gate D: user journey and state quality**

| check | completion evidence | response if failed |
| --- | --- | --- |
| Journey entry, success, cancellation, and recovery are explicit. | Task/state graph. | Clarify behavior before visual commitment. |
| Every material default/loading/empty/partial/error/permission/disabled/pending/success/stale/offline branch is handled or excluded. | State applicability matrix. | Add state or narrow claim. |
| User-visible outcome, feedback, focus, and next action are clear. | Reviewer can exercise pass/fail transition. | Rewrite hidden or vague state. |
| Mutation/side-effect safety is defined. | Pending, duplicate, cancel, rollback, conflict, and data-loss behavior as applicable. | Block consequential action. |
| Shared premises and invalidation are linked. | State dependency graph. | Prevent one branch's Green from broadening. |

**Gate E: semantic, accessibility, and input quality**

| check | completion evidence | response if failed |
| --- | --- | --- |
| Semantic structure and reading order match visual/task hierarchy. | DOM/accessibility and content review. | Correct structure before presentation acceptance. |
| Every control uses appropriate semantics, accessible name, state/value, and error/status relationship. | Component and accessibility-tree evidence. | Block affected command. |
| Required pointer/keyboard/touch/other input paths complete the task. | Input-mode walkthrough/check. | Add equivalent path or narrow support explicitly. |
| Focus starts, transitions, errors, overlays, removal, and return states are coherent. | Focus trace and browser checks. | Repair before release. |
| Status/error feedback is visible and programmatically appropriate. | State tests and targeted review. | Add communication and recovery. |
| Preference/zoom/theme/contrast/motion states match policy. | Named matrix and no-claim boundary. | Strengthen evidence or route. |

**Gate F: composition and visual-system quality**

| check | completion evidence | response if failed |
| --- | --- | --- |
| Information hierarchy serves primary task and product mode. | Direction statement, rendered states, alternatives, owner review. | Revise composition before polishing detail. |
| Responsive contract covers supported containers/content/zoom without overlap, clipping, hidden commands, or incoherent order. | Geometry and screenshot matrix. | Fix structural constraints; do not hide overflow. |
| Typography roles are intentional, readable, content/locale safe, and current-system compatible. | Token/content/render/load evidence. | Adapt type roles/fallback. |
| Color/surface roles distinguish states with required contrast and non-color cues. | Token/state and accessibility review. | Correct semantic roles. |
| Spacing/density/cards/surfaces create clear hierarchy. | Product-mode critique and actual pixels. | Remove redundant frames or adjust rhythm. |
| Icons/controls use familiar semantics or justified alternatives. | Control audit and task evidence. | Use appropriate control or add explicit label. |
| Media reveals the required subject and handles load/failure truthfully. | Asset provenance, pixels, crop, fallback, privacy. | Replace/fix/route content owner. |
| Motion has causal role, remains interruptible/stable, and supports required preferences. | Interaction/preference/performance evidence. | Remove or adapt motion. |
| Distinctive signal is product-specific rather than generic trend accumulation. | Experienced blind/contextual review. | Revisit direction and alternatives. |

**Gate G: component, architecture, and implementation**

| check | completion evidence | severity |
| --- | --- | --- |
| Components/state/data boundaries match repository architecture and journey. | Source/architecture review. | Stop parallel or tangled system. |
| Existing primitives were reused or divergence is justified and owned. | Reuse/adapt/diverge matrix. | Block ungoverned duplicate system. |
| Route/history/deep-link/back and overlay/pane behavior are correct. | Browser/navigation checks. | Block workflow completion. |
| Async/auth/cache/error/cancellation/stale behavior is implemented. | Component/integration/browser evidence. | Block affected states. |
| Assets/fonts/icons/dependencies have ownership, build, lifecycle, rights/privacy, and fallback. | Manifest/build/runtime/content review. | Block primary media or unauthorized asset. |
| Change remains inside authorized paths and preserves unrelated work. | Status/diff ownership. | Critical shared-workspace stop. |
| Relevant complete project gates run. | Exact commands/config/results/limits. | No implementation-complete state. |

**Gate H: rendered and browser evidence**

| check | completion evidence | response if failed |
| --- | --- | --- |
| Every required state/content/container/browser/input render has complete identity. | Render manifest. | Rerun correct state; no unlabeled screenshot. |
| Text, controls, media, overlays, and dynamic content fit without incoherent overlap/clipping. | Pixels, geometry, and human review. | Revise stable constraints and replay. |
| Runtime console/page/network/asset/graphics errors are absent or classified. | Browser diagnostics. | Diagnose/fix/narrow. |
| Actual asset/subject/canvas is visible, framed, and interactive as required. | Screenshot/pixel/input evidence. | Fix/fallback; source is insufficient. |
| DOM/accessibility evidence accompanies pixels for semantic claims. | Multimodal review. | Withdraw semantic/accessibility conclusion. |
| Intended/unintended visual diffs are classified by current authority. | Baseline review and owner decision. | Correct or update bounded baseline. |

**Gate I: measurement and nonfunctional evidence**

| check | completion evidence | response if failed |
| --- | --- | --- |
| Hypothesis, interaction boundary, and owner decision effect are predeclared. | Experiment card. | Keep timing diagnostic only. |
| Baseline/candidate, state/content, browser/device, network/cache, and instrumentation are comparable. | Frozen manifests and abort criteria. | Abort or relabel. |
| Raw observations, failures, statistics, and uncertainty are retained. | Recalculation source. | No percentile/improvement claim. |
| Functional, visual, accessibility, error, and resource counter-gates pass. | Equivalence matrix. | Reject faster/worse candidate. |
| Owner interprets bounded result. | Adopt/reject/investigate/support decision. | Report result without policy conclusion. |

**Gate J: handoff, recovery, and lifecycle**

| check | completion evidence |
| --- | --- |
| Each experience branch is supported, refuted, unresolved, out-of-scope, or invalidated. | Claim/state cards. |
| Split outcomes cannot broaden one another silently. | Dependency and branch decisions. |
| Remaining uncertainty has owner, mechanism, release, and stop conditions. | Route ledger. |
| Authorized change boundary and user/product support matrix are explicit. | Decision record. |
| Rollback/recovery identifies what to inspect after failure. | Project recovery plan. |
| Invalidation maps product, source, state, component, token, content, asset, browser, workload, owner, and policy changes. | Invalidation matrix. |
| Handoff names changed paths, commands, browser evidence, blockers, and next action. | Concise summary linked to canonical packet. |
| Sensitive/customer/assets evidence follows policy. | Storage/redaction/rights/access review. |

**Gate K: final evolution and complete-file QA**

Before declaring this evolved reference complete:

1. Confirm packet counts `26`, `260`, and `1,560`, with raw and prefix-stripped normalized unique counts both `1,560`.
2. Confirm exact reference heading levels/text/order and all 26 strict seed expansions.
3. Run assignment-focused verifier and shared invariant tests that do not require other lanes to finish.
4. Confirm immutable seed, source family, and queue-span hashes remain unchanged.
5. Check ASCII, tables, fences, tabs, trailing whitespace, final newline, prohibited markers, and scoped diff.
6. Reread complete packet and reference in groups of at most five sections, persisting each checkpoint.
7. Record Green after production and Refactor after corrections and final focused PASS.
8. Report exact paths, counts, hashes, current shared-suite state, blockers, and next assigned file without opening it early.

**Quality contrasts**

Good: a standard packet links a product-approved task to complete error/recovery states, semantic controls, responsive content evidence, actual browser pixels, a coherent visual direction, and an unresolved unmeasured performance branch.

Bad: every heading, component, screenshot, and check exists, but user authority, state semantics, content extremes, browser identity, focus, and recovery are absent. This is artifact completeness without experience completeness.

Recoverable reuse: a current component contract and rendered regression support one spacing correction. If the work later becomes a shared token migration, that focused pass cannot promote; consumer, system, browser, rollout, and owner gates must run.

The checklist is a prerequisite graph. Green propagates forward only from valid premises. Browser or user contradiction propagates backward to reopen the earliest wrong assumption and dependent evidence. Selective invalidation avoids both ceremonial full replay and unsafe stale screenshot reuse.

## Adjacent Reference Routing

Adjacent reference guidance: route when the pending frontend claim needs an authority, implementation discipline, observation model, content/asset capability, or operational control this digest does not supply. Route by the missing capability, not by topic resemblance.

Adjacent reference 1: use product discovery, design/content ownership, or user research when the desired task, audience, content, or value choice is not established.

Adjacent reference 2: use the applicable frontend/framework, language, design-system, media, or Three.js guidance after the experience/state contract is scoped and implementation quality is the next question.

Adjacent reference 3: use browser diagnosis, accessibility/domain assurance, performance measurement, operations, review, hosting, or release guidance when their evidence is required; a polished specification does not supply those outcomes.

Candidate names below are route examples, not assertions that a particular skill, binary, connector, browser environment, credential, asset right, or owner is available. Inspect the selected capability and repository policy before use.

**Capability-gap router**

| unresolved question | digest boundary | primary route or candidate capability | evidence expected on return |
| --- | --- | --- | --- |
| What user problem, task, or product mode should be chosen? | Frontend quality cannot select stakeholder value. | Product discovery, brainstorming, PRD, user research, and accountable owner. | User/task alternatives, consequence, owner decision, non-goals, and evaluation criteria. |
| What content, legal/domain language, or asset may be used? | Visual implementation cannot authorize content, claims, rights, privacy, or policy. | Qualified content/domain/legal/brand/asset owner. | Approved content/assets, provenance/rights, constraints, expiry, and fallback. |
| What does current code implement and where? | A design reference does not navigate target source. | Direct search, code graph, language server, repository index, and source reading. | Revision-bound routes/components/state/data/tokens/assets/consumers and limits. |
| Why is the interface failing? | Desired experience does not establish causal mechanism. | Systematic debugging, reproduction, instrumentation, browser devtools, or diagnosis workflow. | Reproduction, minimized case, hypotheses, distinguishing evidence, cause, fix, and regression. |
| How should a React/TypeScript component or app be implemented reliably? | Generic design guidance lacks framework state, server/client, query, form, navigation, type, and test detail. | Applicable React/TypeScript frontend implementation guidance and repository tests. | Architecture matching local idioms, typed boundaries, state/error behavior, tests, and browser evidence. |
| How should a non-React or platform-specific frontend be built? | This digest is framework-neutral. | Target framework/language guidance, official installed docs/source, and native project conventions. | Versioned implementation, lifecycle, state, build, and target rendering evidence. |
| Should a shared component/token/design-system boundary change? | Experience requirements do not establish consumer impact and governance. | Design-system architecture, dependency map, consumer inventory, migration/design review. | Current graph, alternatives, API/variants, consumers, rollout/rollback, ownership, and decision. |
| Does an accessibility or regulated interaction claim hold? | Traceability and general checks cannot substitute for qualified evidence/policy. | Accessibility specialist/domain assurance, semantic/static/browser checks, keyboard/assistive tests, owner review. | User/task scope, applicable standard/policy, findings, negative paths, residual risk, and acceptance. |
| Is a visual asset needed and how should it be sourced? | The reference cannot grant rights or create/choose truthfully by itself. | Current asset system, authorized image search/generation/editing, content/brand review. | Asset provenance, subject accuracy, usage rights/policy, variants, loading/fallback, and target render. |
| How should a 3D scene, product viewer, or game be built? | Generic composition does not supply scene graph, renderer, assets, camera, engine, lifecycle, input, or performance. | Three.js/game/engine guidance and versioned primary docs when authorized. | Working target scene, meaningful pixels, framing, input/animation, cleanup, browser/mobile, fallback, and profile. |
| Does latency, layout stability, memory, bundle, or frame behavior meet a target? | A budget or method is not a measured result. | Browser profiling, benchmark, load/task study, field telemetry, and performance owner. | Frozen workload/environment, raw data, uncertainty, functional/visual/accessibility equivalence, and decision. |
| Does a security, auth, permission, privacy, or destructive-action claim hold? | Frontend appearance cannot establish backend policy or threat resistance. | Security/domain requirements, config/source/runtime analysis, adversarial tests, authorized owner. | Threat scope, server authority, negative states, residual risk, and bounded acceptance. |
| How should live failure be observed or recovered? | Component contract does not create operational telemetry, access, or incident controls. | Observability, SRE/operations, incident/runbook, service owner. | Deployment identity, signals, safe actions, correlation, rollback, escalation, and runtime evidence. |
| Why and when did the interface/design contract change? | Current files/screenshots do not reconstruct historical intent automatically. | Version-control history, issue/PR/design archaeology, and decision records. | Dated source/design changes, discussion/decision identity, exact rationale evidence, and separated inference. |
| Is the implementation complete and ready for independent review? | Authoring guidance does not perform independent final challenge. | Verification-before-completion, code review, design/accessibility review. | Fresh commands, diff, state/render matrix, findings, residual risk, and no-overclaim audit. |
| Should the site/app be hosted or published? | This digest grants no deployment, branch, commit, or publication authority. | Project hosting/deployment/release workflow after user direction. | Confirmed scope, built artifact, environment/config, checks, URL, rollback, and ownership. |
| How should one large product surface be reviewed across many routes/states? | Generic incremental reading can omit cross-page system behavior. | Deterministic route/component/state inventory, explicit global review, browser orchestration. | Complete candidate inventory, stable identity, checkpointed state/render matrix, and integrated gates. |

**Route-entry contract**

Before handoff, record:

| field | required content |
| --- | --- |
| Original user decision | User task/product mode and non-goals, not only the latest build or visual symptom. |
| Unresolved experience claim | One falsifiable product, behavior, semantic, visual, asset, causal, quantitative, or policy question. |
| Consequence | User harm, reversibility, detectability, consumers, owner, and deadline where material. |
| Current evidence | Product/design/source/state/check/render results and contradictions already established. |
| Exact state/environment | Route, data/content, auth, browser/device/container, input/preferences, runtime, and target revision. |
| Earliest verified gap | Intent, authority, content, source, state, oracle, implementation, browser, asset, performance, history, policy, or authorization. |
| Current method boundary | Why more visual/specification work cannot settle the claim or why another route is stronger. |
| Destination capability | Authority or observation needed, independent of tool name. |
| Expected return | Evidence form that can support, refute, narrow, or safely own the claim. |
| Stop condition | When to return, proceed, reject, wait, narrow, or escalate. |
| Sensitive/asset boundary | Customer/source/runtime/credential/media/licensing data that cannot transfer. |

This prevents the destination from restarting generic design orientation or losing the task and rendered state that made the problem important.

**Route-return contract**

The destination returns:

1. Tool/reference/owner/system identity, version, configuration, and observation scope.
2. Exact experience claim addressed and why this method could decide or observe it.
3. Reproducible source, test, browser trace, screenshot, accessibility finding, asset, measurement, history, or owner evidence.
4. Agreement and contradiction with the existing journey/state/visual packet.
5. Bounded state: supported, refuted, unresolved, invalidated, not applicable, or escalation required.
6. Remaining users, states, content, containers, browsers, inputs, assets, workloads, owners, and invalidation triggers.
7. Updated original decision and every dependent state/surface to reopen.

**Complementary routes**

| gap | primary route | secondary route | why both may matter |
| --- | --- | --- | --- |
| Existing behavior conflicts with desired workflow | Target source/tests/history. | Product/content owner. | History/source explain current state; owner decides preserve, fix, or migrate. |
| Dynamic responsive defect | Browser reproduction/geometry. | Source/layout and content policy. | Pixels expose occurrence; source/content explain mechanism and support. |
| Accessibility failure | Qualified semantic/input review. | Component/source and browser state tests. | User/policy evidence defines consequence; implementation evidence creates durable repair. |
| Visual direction mismatch | Product/design/brand review. | Rendered alternatives with real content/states. | Authority chooses direction; browser evidence proves execution. |
| Performance regression | Controlled browser profile. | Functional/visual/accessibility equivalence and source review. | Profile locates cost; counter-gates prevent faster wrong experience. |
| Blank 3D canvas | Browser/graphics diagnosis. | Three.js/source/assets and fallback/product review. | Runtime identifies cause; implementation and owner establish corrected scene/fallback. |
| Shared component redesign | Dependency/design-system analysis. | Experience states and framework implementation. | Consumers/governance, desired behavior, and code idioms are separate questions. |
| Requirement-caused incident | Systematic diagnosis. | Experience packet/history audit. | Diagnosis establishes cause; audit repairs source/state/gate/invalidation. |

Add a second route only when it can fail differently in a way that affects the user action.

**Good, bad, and conditional routes**

Good: a Three.js product viewer is blank in one target browser. The handoff includes package/renderer, URL/state, viewport, asset network, console/graphics output, screenshot, pixel result, and fallback requirement. The returned diagnosis identifies a camera/asset lifecycle defect and updates scene plus regression evidence.

Bad: the same blank canvas is sent through another visual-style critique. Better prose cannot establish why pixels are absent.

Conditional: a second static search cannot prove absence of an inaccessible control, but it can find a direct counterexample that refutes a universal claim cheaply. Use it for falsification, not completeness.

**Loop detection and terminal routes**

Stop routing and escalate when:

- the same experience claim returns twice without new evidence, narrower support, or a changed premise;
- destinations share the same ideal fixture, browser, source, or reviewer blind spot;
- required product/content/design/domain owner, credentials, production state, sensitive data, asset rights, GPU/device, or qualified reviewer is unavailable;
- sources or owners conflict on a consequential action and no designated resolver exists;
- policy/risk acceptance rather than technical observation is the remaining question;
- time/cost requires an explicit bounded decision under uncertainty.

Terminal escalation is not empty. Preserve task/state, current evidence, rendered artifacts, contradictions, unavailable capability, consequence, candidate options, and exact owner decision required.

**Route verification**

A route succeeds when the destination consumes the stated gap, uses capable authority or observation, returns reproducible evidence, updates the original journey/state, preserves sensitive and ownership boundaries, and reduces, refutes, narrows, or safely assigns uncertainty. If none changes, the route added activity rather than information.

Adjacent routing is an experience evidence graph: each edge means "this claim lacks this capability," and each return means "this evidence changes this user-state decision." That precision keeps specialized tools modular without fragmenting the interface into disconnected designs.

## Workload Model

`combined_evidence_inference_note`: Treat Frontend Design Quality Patterns as a frontend experience operating reference, not as a prose summary.

The seed's `one user flow, three viewport classes, one loading state, one error state, and one keyboard-only path` boundary is not retained as an operational capacity. No local browser study, product support matrix, content distribution, reviewer experiment, state coupling model, or risk threshold supports it. One destructive action can require more assurance than many static pages; one responsive component can live in dozens of containers. Measure the actual experience graph.

**Reconciled seed dimensions**

| workload_dimension_name | evolved boundary | verification pressure point |
| --- | --- | --- |
| `primary_usage_surface` | Product clarification, interface/state design, implementation, accessibility/input, rendered review, performance, and handoff where user-visible reliability matters. | Confirm the reference changes a bounded implementation, rejection, or route rather than adding design prose. |
| `bounded_capacity_model` | No universal flow/state/viewport count; bound by journey/state coupling, components/consumers, content/support matrix, environments, owner capacity, and assurance. | Change mode, scope, or route before required users/states/content/evidence are omitted. |
| `source_pressure_model` | Distinct product/design/source families, bytes/modules, churn, conflicts, authority diversity, and required complete/global review. | Compare recommendations with current product/system/target evidence rather than following duplicate headings or external examples. |
| `artifact_pressure_model` | Experience packet, state/check/render graph, screenshot/trace volume, reread cost, update frequency, handoffs, and invalidation fan-out. | Require reviewable evidence or native equivalent before durable quality claim. |

**Workload variables**

| symbol | dimension | why it matters |
| --- | --- | --- |
| `J` | Material user journeys and actor roles. | Product decisions, entry/exit, and cross-journey consistency grow with distinct tasks/users. |
| `S` | Material interface/data/runtime states and transitions. | Behavior, composition, feedback, focus, recovery, and fixtures grow with the state graph. |
| `C` | Components, routes, layouts, shared primitives, and tokens affected. | Architecture, variants, documentation, rendering, and change review grow with implementation surface. |
| `U` | Shared consumers of changed components/tokens/contracts. | Compatibility, migration, rollout, and invalidation can dominate a small source diff. |
| `L` | Product-source-state-component-check-render-invalidation links. | Reconstruction and selective rollback depend on many-to-many integrity. |
| `D` | Data/content/locale/value/length/media variants. | Text fit, hierarchy, errors, subject truth, and state behavior depend on real content pressure. |
| `V` | Containers, viewports, zoom/text scale, orientation, themes, and display modes. | Layout and hierarchy can change without source logic changing. |
| `B` | Browsers, devices, rendering engines, graphics capabilities, and network/cache conditions. | Runtime, fonts, assets, focus, canvas, and performance differ by environment. |
| `I` | Input/accessibility/preference modes required. | Pointer, keyboard, touch, focus, semantics, assistive paths, reduced motion, and contrast evidence add distinct obligations. |
| `A` | Assets, fonts, images/video, models/materials, canvas/3D scenes, and lifecycle. | Rights, loading/failure, fidelity, framing, fallback, performance, and cleanup add work. |
| `K` | Checks across source, unit, component, integration, browser, accessibility, screenshot, pixel, performance, and review layers. | Setup, execution, flakiness, oracle, storage, and review grow with evidence surface. |
| `E` | Build, server, auth/data, browser/runner, hosted, device/GPU, and production environments. | Reproduction and permissions can dominate apparent interface size. |
| `O` | Product, content, design, engineering, accessibility, security, operations, and release owners. | Conflict, acceptance, handoff, and decision latency increase with organizational boundaries. |
| `Q` | Number/diversity of revisions, consumers, or decisions reusing evidence. | Determines whether packets/fixtures amortize before becoming stale. |

No scalar describes complete frontend workload. A page with many static sections may be simple. One shared date picker or destructive transfer journey can require broad locale, keyboard, focus, browser, consumer, and recovery evidence.

**Pipeline stage model**

| stage | work | primary growth drivers | evidence output |
| --- | --- | --- | --- |
| Orient and fit | Read request/instructions, inspect current product, choose mode/profile. | `J`, `O`, repository maturity, product ambiguity. | User task, product mode, non-goals, owners, open questions. |
| Map sources/system | Read product/design/source, hash/version, inventory components/tokens/assets/tests, reconcile conflicts. | Source families, `C`, `U`, churn, conflicts. | Evidence/system registry and invalidation. |
| Model journeys/states | Split tasks, data/runtime states, transitions, side effects, shared premises. | `J`, `S`, `D`, external services, consequence. | Journey/state graph. |
| Define semantics/access | Structure, controls, labels, focus, input, status, preferences, support. | `S`, `I`, product policy, content. | Semantic/input/accessibility contract. |
| Design composition/system | Hierarchy, responsive transformations, type, color, spacing/density, media, motion. | `D`, `V`, product mode, current system, `A`. | Visual system and responsive contract. |
| Implement | Components, routes, state/data, assets, dependencies, compatibility. | `C`, `U`, architecture, framework, `A`, diff size. | Source changes and direct behavior evidence. |
| Render/verify | Run checks, browsers, state/content/container matrix, pixels, accessibility, runtime, performance. | `K`, `S`, `D`, `V`, `B`, `I`, `A`, `E`. | Render manifest and branch states. |
| Review/handoff | Reconstruct task/direction, resolve mismatches, accept risk, document recovery/invalidation. | `L`, `O`, packet age, consequence, reviewer familiarity. | Bounded decision and next action. |
| Maintain | Detect stale premises, update fixtures/baselines, replay affected matrix, evolve components/patterns. | `Q`, churn, invalidation fan-out, outcome feedback. | New versioned experience trajectory. |

**Workload modes**

| mode | operation | best fit | stop or switch signal |
| --- | --- | --- | --- |
| Focused native correction | Validate one existing state/component/token/fixture, reproduce, apply bounded correction, rerender. | Reversible local defect with current authority. | Shared consumers, state conflict, broader design-system or support implication. |
| Standard journey | Map one bounded journey and its material states, implement, render, verify, hand off. | New page/workflow or meaningful redesign. | Claims span independent systems/owners or matrix exceeds available evidence. |
| Shared component/system | Inventory consumers and variants, version contract, migrate, verify representative plus critical consumers. | Component/token/navigation/design-system change. | Consumer completeness or governance cannot be established. |
| Indexed/incremental product review | Use deterministic route/component/state/render manifests and complete selected surfaces. | Large product with repeated local edits and material full-review cost. | Inventory misses candidates, identities stale, or global consistency is claimed. |
| Explicit global experience review | Review complete critical journey/surface/state/system matrix with checkpoints. | Initial/final system review, redesign, theme/token migration, broad consistency claim. | Input/evidence cannot be handled safely; change phase/model or split with global join contract, never silently sample. |
| High-assurance augmentation | Add domain/content/security/accessibility/device/browser/operations/owner evidence. | Regulated, destructive, critical, or production-risk interface. | Required authority/environment unavailable; escalate. |
| Specialized route | Transfer product, diagnosis, asset, 3D, performance, security, or operations gap. | This digest cannot observe or decide consequential premise. | Return when specified evidence changes original journey claim. |

**Favorable workload signature**

- User task, product mode, and owners are identifiable.
- Existing design system/components/tests and actual browser behavior provide anchors.
- Material states, content classes, supported containers/browsers/inputs can be bounded explicitly.
- Project/browser checks reliably demonstrate wrong state and final behavior.
- Several revisions/consumers reuse stable state and render evidence.
- Reviewers can reconstruct links without opening unrelated product surfaces.
- Any inventory/index has complete candidate recall and stale-state rejection.

**Unfavorable workload signature**

- Product/content/policy choices remain unresolved across owners.
- Security, production, third-party, GPU/device, or domain behavior dominates and cannot be reproduced safely.
- State/content/browser/input cross-product matters but no support/sampling/assurance policy exists.
- Product/design/source changes faster than packets and screenshots can invalidate.
- Browser checks are slow, flaky, animation-dependent, credential-bound, or use unrealistic fixtures.
- Parallel agents share components/tokens/design authority without merge semantics.
- Reviewers cannot understand the state/render graph within available time.
- The packet/design becomes a second unsynchronized authority beside product components/tests.

**Safe narrowing contract**

Narrowing journeys, states, components, content, containers, browsers, inputs, assets, or owners is safe only when:

1. The user decision can be restated entirely inside the narrower boundary.
2. External interfaces, consumers, data/content, support modes, and owners are listed.
3. No universal accessibility, responsiveness, compatibility, performance, or product-wide claim is made from local evidence.
4. Cross-boundary behavior has a separate capable route and integration owner.
5. The narrowed scope reaches implementation, behavior/render checks, handoff, and invalidation.
6. New evidence crossing the boundary has an explicit expansion trigger.

Arbitrary sampling to satisfy a screenshot, time, or context quota creates a different evidence product; it is not a capacity solution.

**Fixture equivalence and sampling**

Risk-based equivalence classes can reduce combinations when the team records why members share behavior. Examples include:

- content classes by wrapping, glyph/script, media, numeric range, and error length;
- container classes by actual composition transition rather than arbitrary device labels;
- browsers/devices by engine/input/graphics behavior relevant to the claim;
- states by shared layout/control semantics while preserving critical negative branches;
- consumers by component API/variant/theme/container usage and consequence.

Always include boundary and counterexamples that could disprove the equivalence. A passing representative cannot authorize omitted critical variants silently.

**Sharding and multi-agent contract**

| concern | required rule |
| --- | --- |
| Partition | Stable journey, state family, route, component/consumer, design-system, asset, or evidence boundary; avoid arbitrary equal page chunks. |
| Shared identity | One product decision, target revision, instruction set, design system, and evidence schema. |
| Coverage | Union, overlap, excluded states/content/browsers, and no-claim policy are explicit. |
| Shared premises | Product/content decisions, components/tokens, route/data contracts, support policy, and visual direction have one authority. |
| Cross-shard links | Journey transitions, shared components, consumers, visual tokens, and invalidation edges reconcile. |
| Writer ownership | One writer per reference, packet, route/component/token/asset, screenshot directory, or baseline. |
| Merge | Structured state/evidence reconciliation and integrated browser checks, not concatenated design summaries. |
| Conflict | Named product/design/engineering owner and deciding evidence for incompatible results. |
| Verification | Per-shard behavior/render gates plus global navigation, component, token, support, and recovery gates. |
| Handoff | Every shard persists exact source, state, rendered evidence, blocker, and next action before integration. |

Parallel work reduces elapsed time only when writes and decisions are independent. It increases merge and browser-matrix cost; measure both.

**Pressure signals and responses**

| observed pressure | investigate first | avoid | possible response |
| --- | --- | --- | --- |
| Product/source loading dominates | Distinct versus duplicate sources, question breadth, route/component dependency, and phase. | Skipping current product/design authority. | Deduplicate bytes, complete selected modules, or declare global review. |
| State count grows rapidly | Compound journeys, duplicate states, shared state machine, and hidden side effects. | Omitting failure/recovery or merging unrelated states. | State families with shared premises and independent critical branches. |
| Screenshot matrix explodes | Real layout transitions, equivalence classes, content/state/browser risk, and duplicate pixels. | Arbitrary three-view screenshot claim. | Risk-based matrix with hard critical variants and no-claim boundary. |
| Shared-component consumers expand | Consumer inventory, variants/themes/containers, migration, and owner. | Updating snapshots without compatibility plan. | Versioned component contract, representative plus critical consumer gates. |
| Browser suite dominates | Flake, animation, server/data setup, wrong layer, and consequence. | Replacing strong checks with fast irrelevant source checks. | Stabilize fixtures, focused iteration plus final matrix, parallel safe browsers. |
| Asset/3D cost dominates | Subject need, sizes, loading/fallback, lifecycle, browser/GPU, and performance. | Dropping fallback or accepting source-only. | Optimize assets/scene, narrow support with owner, or use simpler truthful medium. |
| Context compaction recurs | Canonical packet, source/state inventory, render manifest, and checkpoint quality. | Resume from summary/screenshots alone. | Persist/reload canonical state and change phase if needed. |
| Reviewers cannot reconstruct | Link density, unclear product authority, duplicate prose/screens, and weak hierarchy. | Add narrative indiscriminately. | Improve stable IDs, focused views, and route/owner decisions. |
| Evidence stales before reuse | `Q`, content/product/browser churn and native tests/stories. | Fixed ceremonial refresh. | Event-driven update, native-source reuse, or retire duplicate packet. |

**Workload measurement card**

| category | measurements |
| --- | --- |
| Identity | Product/system/packet/component/token versions, target revision, working state, profile, phase, and owners. |
| Sources/system | Distinct families/modules, complete/selected reads, components/tokens/routes/assets, consumers, conflicts, and freshness. |
| Experience graph | `J`, `S`, `C`, `U`, `L`, `D`, `V`, `B`, `I`, `A`, and cross-boundary joins. |
| Context | Input bytes/tokens where observable, compactions, inventories, selected units, and required global units. |
| Execution | Project/browser commands, server/setup, wall/CPU time where relevant, failures, retries, flake, screenshots/traces, storage. |
| Review | Active time under defined method, handoffs, dissent, blocked-owner time, and reconstruction results. |
| Utility | Claims retained/refuted, states added, contradictions caught, routes changed, rework avoided/caused, and next decision enabled. |
| Quality | Task/state capability, accessibility/input, overlap/content fit, runtime errors, visual reversals, escaped defects, recovery, invalidation timeliness. |

Repeat comparisons only under compatible conditions and disclose instrumentation/review overhead. Do not extrapolate from one page, fixture, browser, or reviewer to a heterogeneous product.

**Optimization impact ledger**

| optimization | likely benefit | evidence-contract impact |
| --- | --- | --- |
| Reuse current components/tokens | Avoid duplicate design and preserve familiarity. | Safe after fit, state, consumer, and rendered checks. |
| Deduplicate hash-equal guidance | Reduce repeated context. | Preserve path/package provenance and role differences. |
| State/content equivalence classes | Reduce fixtures/screenshots. | Require rationale, boundary/counterexamples, and critical-state hard gates. |
| Deterministic route/component/render inventory | Reduce repeated discovery and stale evidence. | Adds completeness, identity, invalidation, and schema lifecycle. |
| Focused browser reruns | Faster iteration. | Final integrated user-critical and support matrix remains required. |
| Shared state/layout primitives | Reduce repeated implementation/fixes. | Adds consumer/variant/compatibility and ownership obligations. |
| Parallel independent surfaces/browsers | Reduce elapsed time. | Adds exclusive artifacts, merge, shared-premise, and integration verification. |
| Native story/test/issue metadata | Reduce separate packet maintenance. | Must preserve product authority, rendered state, recovery, and invalidation. |

Good workload decision: reuse a current component for one long-content defect, add boundary state/render evidence, and avoid a product-wide packet. Bad decision: declare three generic viewport screenshots sufficient while omitting error, zoom, and container consumers. Conditional sharding: split a redesign by independent journey/component ownership only when shared navigation, tokens, transitions, and final integrated checks remain explicit.

Workload optimization and frontend reliability are coupled. Every scope, fixture grouping, inventory, sampling, reuse, or parallelization change must state whether it alters the user/state/content population, semantic selection, rendered evidence, support matrix, freshness, or only presentation. Faster work is valuable only when the bounded experience remains equally or more falsifiable and recoverable.

## Reliability Target

`combined_evidence_inference_note`: Reliability here means preserving a material user outcome across stated states and supported environments, detecting violations with an appropriate oracle, containing harm, and providing a usable recovery path. It does not mean visual sameness, a universal pass percentage, or confidence inferred from polished screenshots.

The seed proposes four useful concerns but combines unlike measurements. Its `100 percent`, `18 of 20`, `zero`, and `every` values are inherited editorial targets, not results from a product, browser, accessibility, reviewer, or incident study in the local corpus. Keep the concerns; calibrate obligations and thresholds against the target product.

**Seed target reconciliation**

| inherited target | preserved intent | why the seed threshold is not portable | evolved treatment |
| --- | --- | --- | --- |
| `source_boundary_preservation` at `100 percent` | Do not present local evidence, external research, or inference as interchangeable authority. | Label presence can be checked deterministically, but a label alone does not prove the underlying source supports the claim or is current. | Make claim-to-source/inference identity a structural invariant, then audit semantic support and invalidation separately. |
| `decision_accuracy_sample` at `18 of 20` | Check whether users reach the intended adopt, adapt, avoid, or route decision. | The population, sampling method, task difficulty, reviewer agreement, error severity, and acceptance rationale are undefined. | Design a local decision study with frozen tasks, representative users/reviewers, error classes, and disagreement review before choosing a threshold. |
| `unsupported_claim_rate` at `zero` | Reject consequential production, security, latency, or reliability assertions without evidence or an explicit verification route. | A universal rate requires a complete claim inventory and classification oracle; minor design judgments also differ from operational facts. | Treat a detected unsupported consequential assertion as a sentinel failure while reporting inventory completeness and judgment boundaries. |
| `recovery_path_clarity` for `every` avoid/failure case | Make rejection actionable through rollback, escalation, or another capable reference. | Some findings are observations rather than failures, and naming a route does not prove the recovery works. | Require recovery for material user or process failures and replay representative recovery paths under named ownership. |

**Reliability evidence classes**

| class | meaning | suitable evidence | release use |
| --- | --- | --- | --- |
| Hard invariant | A supported material outcome that must hold for every enumerated instance in the declared boundary. | Deterministic unit/component/integration/browser/accessibility checks plus direct review where the oracle is visual or semantic. | A known violation blocks the affected claim or release boundary until fixed, removed from support, or escalated through product policy. |
| Sentinel event | One occurrence is evidence that a consequential safeguard or evidence process failed. | Claim audit, destructive-action fixture, data-preservation check, keyboard-trap check, blank-render detector, or injected known failure. | Stop the affected claim, investigate population exposure, correct cause, and replay the evidence path. |
| Sampled indicator | A bounded sample estimates consistency or usability across a larger declared population. | Risk-based state/content/container/browser sample, reviewer rubric, usability study, or production signal with denominator. | Informs confidence and prioritization; it cannot authorize unsampled critical paths or a broader support promise by itself. |
| Operational signal | Runtime evidence detects environment-specific behavior after release. | Privacy-reviewed errors, latency distributions, abandonment/recovery events, client capability failures, or support reports. | Complements pre-release evidence and activates containment/recovery; absence of reports is not proof of correctness. |
| Owner judgment | A named owner accepts a bounded uncertainty or visual/product tradeoff. | Decision record with alternatives, affected users/states, consequence, expiration, and reconsideration trigger. | Permits a scoped decision, never an unlabeled global reliability claim. |
| Unknown | Required authority, environment, population, or oracle is unavailable. | Explicit gap record and adjacent specialist/product/operations route. | Narrow the claim, stage the rollout with controls, or pause; do not convert missing evidence into a passing value. |

**Five-part experience reliability model**

1. **Prevent:** Define the user outcome, material negative states, semantic/input obligations, ownership, and support matrix before implementation.
2. **Detect:** Choose independent oracles for behavior, semantics, render composition, assets, performance, and source boundaries. Verify that a deliberately broken branch is observable.
3. **Contain:** Limit blast radius through reversible changes, feature controls, guarded destructive actions, safe defaults, and explicit no-claim boundaries.
4. **Recover:** Preserve user work where possible, expose truthful state and next action, restore focus/navigation, retry only eligible operations, and provide rollback or escalation.
5. **Learn:** Link escaped failures and reviewer disagreements to the state graph, fixtures, checks, component/system guidance, owner decisions, and invalidation rules.

Passing only prevention-time checks is insufficient for states that can fail because of network, device, content, browser, graphics, authorization, or external-service conditions. Conversely, production monitoring cannot retroactively justify shipping a known unsupported material path.

**Default reliability profiles**

| profile | default boundary | required evidence | escalation trigger |
| --- | --- | --- | --- |
| Focused correction | One reversible component/state defect with known consumers and current fixtures. | Reproduce the failure, add the nearest deterministic check, render affected state plus relevant counterstate, inspect direct consumers, and replay recovery if applicable. | Shared contract/token, unknown consumers, unsupported environment, or consequential side effect. |
| Standard journey | One bounded user journey with material success, empty, loading, error, validation, permission, and recovery branches that apply. | State/transition inventory, semantic and input contract, representative content/container/browser evidence, source checks, rendered review, and release handoff. | Omitted critical branch, unresolved product decision, broad support claim, or cross-owner dependency. |
| Shared system | Component, token, navigation, form primitive, or layout contract used across multiple consumers. | Consumer inventory, versioned contract, representative and critical consumer matrix, migration/rollback plan, invalidation, and system-level visual/semantic review. | Candidate recall cannot be established or consumers have incompatible consequence classes. |
| High assurance | Destructive, financial, identity, safety, regulated, sensitive-data, or otherwise high-consequence path. | Product/domain/security/accessibility/operations authority as relevant, independent negative testing, failure injection, recovery rehearsal, controlled rollout, and accepted residual risk. | Required specialist authority or realistic environment is unavailable. |

These profiles are starting points, not rankings. Promote a profile when consequence, irreversibility, silent failure, shared reach, environment variance, or support obligation increases. A visually small change can require high assurance; a visually large static surface may not.

**Outcome contract template**

| field | required content |
| --- | --- |
| `outcome_identity` | Stable journey, actor, entry, intended result, and affected product revision. |
| `material_branches` | Success and applicable loading, empty, validation, permission, partial, timeout, offline, external-failure, cancellation, and recovery states. |
| `owned_invariants` | Product-owned behavior, data preservation, semantics, input/focus, truthful feedback, and fallback obligations. |
| `support_matrix` | Content classes, containers/viewports, zoom/text scale, themes, browsers/devices, input/accessibility modes, networks, and graphics capabilities actually claimed. |
| `consequence_class` | User harm, reversibility, detectability, shared reach, and operational impact if the outcome fails. |
| `oracle_and_evidence` | Check/render/reviewer/telemetry method, fixture, environment, baseline, and location sufficient to falsify the claim. |
| `indicator_definition` | Numerator, denominator, sampling frame, exclusion rule, observation period, severity mix, and uncertainty when a rate is used. |
| `containment_recovery` | Feature control, rollback, preserved work, truthful error/status, retry eligibility, escalation, and recovery owner. |
| `accepted_unknowns` | Named missing evidence, bounded no-claim area, accepting owner, expiry, and trigger for reassessment. |

**Typical hard invariants**

- The intended action reaches the correct product state or exposes a truthful actionable failure; success is never inferred merely because a control was clicked.
- A failed or cancelled destructive action does not silently report success, lose unrelated user work, or leave the next state ambiguous.
- Supported keyboard and assistive paths preserve control semantics, operability, focus movement/return, status announcement, and recovery for the material journey.
- Material loading, empty, permission, validation, partial, and error branches cannot collapse into a blank or stale-success interface.
- Images, fonts, media, canvas, and 3D surfaces have declared loading/failure behavior; a nonblank pixel test complements but does not replace subject, framing, and interaction review.
- A recommendation presented as source-backed retains its exact source identity or is labeled inference; high-consequence claims carry direct evidence or a capable verification route.

Do not apply an absolute invariant to browser antialiasing, subjective taste, or every incidental pixel. For those dimensions, define tolerance, review rubric, representative population, and support boundary.

**Verification protocol**

1. Freeze the outcome contract, target revision, instruction set, fixtures, support matrix, and evidence environment.
2. Enumerate material branches and map each obligation to at least one oracle; mark genuinely unobservable branches as unknown rather than passing.
3. Run deterministic source/behavior/semantic checks and confirm the expected failure state before trusting a new or changed oracle.
4. Render representative content, state, container, browser/input, and asset classes, including boundaries that could disprove the grouping rationale.
5. Inject a known sentinel defect where safe, such as an unsupported consequential claim, missing accessible name, broken recovery link, or blank canvas fixture; confirm the process rejects it.
6. Record pass, fail, blocked, accepted-risk, and not-applicable separately. Preserve raw evidence and reviewer disagreement instead of averaging unlike outcomes.
7. Exercise containment and recovery for material failures, including focus/navigation restoration and preservation of user-entered state where promised.
8. Compare baseline and candidate under equivalent conditions, then publish the exact claim boundary, exceptions, owners, and invalidation triggers.

**Anti-gaming rules**

- Do not improve a rate by deleting difficult states, users, browsers, content, or checks from the denominator without a visible support-policy decision.
- Do not convert a failure to passing by retrying until green unless the original failure is independently classified as infrastructure-only and the retry record remains visible.
- Do not approve a screenshot baseline solely because it is new; review the state identity, content, composition, semantics, assets, and intended product direction.
- Do not average a catastrophic branch with many trivial passes. Preserve severity and sentinel-event reporting.
- Do not infer reliability from absence of telemetry when instrumentation, population, consent, retention, or detection sensitivity is unknown.
- Do not leave accepted exceptions ownerless or permanent by default; attach expiration and reassessment triggers.

**Examples**

| quality | example | verdict |
| --- | --- | --- |
| Good | "For the account-deletion journey, cancellation and server rejection preserve the account and entered reason; keyboard focus returns to the initiating control; the supported browser/input matrix and recovery fixtures pass." | Outcome, negative branches, support boundary, and recovery are falsifiable. |
| Bad | "The redesigned settings page is 99 percent reliable." | No population, denominator, failure definition, consequence, environment, evidence, or recovery exists. |
| Borderline | "Five representative cards render correctly, so the shared card system is reliable." | Useful sampled visual evidence only if consumer/content/container equivalence is documented; it cannot establish all-consumer behavior or accessibility. |
| Good operational complement | "A controlled rollout monitors declared client render failures and recovery completion, while pre-release browser and accessibility invariants remain release gates." | Runtime detection complements rather than replaces owned contracts. |

**Target review and retirement**

Review the reliability profile when journeys, states, content, components, support promises, browsers/devices, assets, external dependencies, consequence, or owners change. Retire a metric when it no longer changes a decision, when its denominator cannot be trusted, or when a stronger direct invariant replaces the proxy. A rising score is not inherently progress: compare evidence-population integrity, escaped severity, detection latency, recovery success, reviewer disagreement, and user outcome together.

No product reliability rate is reported by this reference. Quantitative targets belong to a named product population, observation period, environment, consequence model, and accountable owner. The portable default is stricter evidence classification and explicit uncertainty, not inherited precision.

## Failure Mode Table

`combined_evidence_inference_note`: Use this registry to turn an observed frontend failure into containment, recovery, prevention, and verification. The local frontend-design source supports product-fit context, distinctive direction, hierarchy, implementation completeness, and considered accessibility; the detailed causal taxonomy below is systems inference to apply against the actual product.

A failure label is not a diagnosis. Preserve the difference between:

- **symptom:** what the user, reviewer, check, or runtime observed;
- **proximate trigger:** the state, content, input, environment, dependency, or change associated with the observation;
- **provisional or confirmed cause:** the responsible product/source/component/runtime/evidence mechanism;
- **consequence:** task, data, accessibility, trust, support, performance, or review impact;
- **response:** immediate containment and user recovery;
- **prevention:** contract, component, fixture, check, process, or ownership change;
- **proof:** evidence that reproduces the failure and distinguishes the corrected behavior from relevant counterexamples.

**Failure record**

| field | required question |
| --- | --- |
| `failure_identity` | Which journey, actor, state/transition, component/consumer, revision, and environment failed? |
| `observed_symptom` | What was directly seen, measured, announced, logged, or reported without causal interpretation? |
| `expected_outcome` | Which product, semantic, visual, performance, or recovery contract should have held? |
| `trigger_and_evidence` | Which fixture/content/input/network/browser/asset/dependency condition reproduces it, and where is raw evidence? |
| `cause_confidence` | Is the causal account confirmed, probable, competing, or unknown? What would discriminate alternatives? |
| `consequence_class` | Is the result task-blocking, harmful/irreversible, silently degrading, claim-blocking, optional degradation, or a method boundary? |
| `affected_population` | Which declared users, content, states, containers, browsers/devices, inputs, consumers, or owners may be exposed? |
| `containment_and_recovery` | How is harm bounded now, user work preserved, truth exposed, focus/navigation restored, and escalation offered? |
| `prevention_and_replay` | Which contract/system/check changes, and which original plus neighboring branches must pass afterward? |
| `owner_and_expiry` | Who owns resolution or accepted risk, and when does the decision invalidate? |

**Consequence classes**

| class | interpretation | default response |
| --- | --- | --- |
| Material or harmful failure | Claimed task cannot complete, wrong/destructive action occurs, sensitive or important state is exposed/lost, or recovery is absent. | Contain immediately, block affected claim/release, preserve evidence, route needed authority, restore a safe truthful path, and verify recovery. |
| Silent degradation | Interface appears successful or unchanged while data/state/semantics/asset/runtime behavior is wrong or stale. | Treat detection as urgent because users and checks may not recognize harm; inspect population and add an independent oracle. |
| Evidence or claim blocker | Required source, fixture, browser state, accessibility proof, render, performance method, or owner decision is missing or invalid. | Mark the claim blocked/unknown; do not convert absence into a product failure or a passing result. |
| Recoverable user degradation | A supported path fails visibly but preserves work and provides a truthful successful fallback or retry. | Fix according to product priority, retain operational detection, and verify fallback/recovery semantics. |
| Optional enhancement loss | Nonessential motion, media, 3D, or decoration is unavailable while task, meaning, and support contract remain intact. | Degrade deliberately, avoid broken empty surfaces, and verify that the fallback remains coherent. |
| Method boundary | Product/domain/security/operations/accessibility authority or a realistic environment is outside this reference. | Route with a precise evidence request and return condition; narrow the current claim rather than guessing. |

Severity is contextual. A missing image can be optional decoration or the primary product evidence; a slow transition can be polish debt or make a time-sensitive operation unsafe; a focus defect can be inconvenient or completely block a supported user.

**Layered failure registry**

| failure mode | likely trigger or causal layer | user/process consequence | detection evidence | containment, recovery, and prevention |
| --- | --- | --- | --- | --- |
| Product task modeled incorrectly | Agent optimizes a generic page type instead of the actual actor, job, consequence, and product state. | Polished interface solves the wrong task or omits a necessary decision. | Compare implementation and state graph with current product behavior, request, content, and product-owner decision. | Pause visual expansion; restate journey/non-goals, reconcile authority, update acceptance fixtures, then rerender the corrected task. |
| Source drift hides truth | Local source, product, design system, external evidence, or support policy changes after the packet/reference. | Guidance appears authoritative while using stale premises. | Hash/version checks, change inventory, claim-to-source audit, and invalidation links. | Mark affected claims stale, reread changed authority completely, replay dependent decisions/checks, and version evidence. |
| Authority collision remains hidden | Request, current product, design system, source, external research, or owner decisions disagree. | Agent silently chooses a convenient premise; reviewers cannot reconstruct why. | Conflict register with exact propositions, authority type, owner, and decision status. | Preserve current safe behavior, escalate consequential policy, record resolution and invalidated artifacts. |
| Generic advice escapes review | Plausible frontend conventions are copied without product/theme/state evidence. | Output is competent-looking but interchangeable, unsupported, or wrong for domain workflow. | Ask which concrete user decision, source row, product state, render, or check each recommendation changes. | Reject generic claims, ground the decision, render operational examples, or remove the recommendation. |
| Material state omitted | Loading, empty, validation, permission, partial, timeout, cancellation, or error branch is absent from model/fixtures. | Blank, stale, blocked, or misleading interface appears outside the happy path. | State-transition inventory, branch coverage, negative fixtures, browser trace, and rendered matrix. | Add truthful state and recovery, preserve work, update state contract and regression evidence. |
| Stale success or race | Concurrent request, navigation, cache, hydration, optimistic update, or out-of-order response overwrites newer truth. | User sees or acts on incorrect state while the screen appears successful. | Deterministic scheduling, request identity, transition trace, stale-response test, and operational correlation. | Ignore/cancel obsolete work, reconcile server truth, expose pending/failure states, and test ordering/cancellation. |
| Control semantics mismatch | A styled element lacks native behavior, accessible name, role/state, disabled semantics, or correct form association. | Keyboard/assistive users cannot operate or understand the control; automation may be false-green. | Semantic query, keyboard path, accessibility tree, form submission behavior, and assistive review where warranted. | Prefer native controls, repair name/state/relationship, preserve visual design, and add behavior-level checks. |
| Focus or navigation continuity fails | Dialog, validation, route transition, async replacement, or recovery removes/misplaces focus. | User loses location, cannot continue, or reaches hidden/inert content. | Keyboard walkthrough, focus trace, browser check across open/close/error/retry, and screen-reader review as needed. | Define initial/return focus and logical order, avoid traps, announce state, and replay transitions. |
| Text/content overflows or occludes | Real labels, localization, long identifiers, errors, zoom/text scale, or narrow containers exceed ideal fixtures. | Meaning/actions disappear, overlap, clip, or force incoherent scrolling. | Boundary content classes, container queries/viewports, zoom/text-scale renders, visual diff and DOM geometry checks. | Permit wrapping/growth, constrain fixed-format controls deliberately, revise hierarchy, and test longest meaningful variants. |
| Responsive transformation breaks hierarchy | Components merely shrink or reorder without preserving task priority and relationships. | Primary action/context becomes hidden, sequence changes meaning, or dense tools become unusable. | Compare composition at actual transition boundaries with task/hierarchy rubric and input checks. | Define mode-specific layout transformation, stable control geometry, overflow behavior, and representative container evidence. |
| Visual direction collapses into defaults | Unexamined framework patterns, decorative effects, generic cards, or one-note palette replace domain/product intent. | Interface becomes interchangeable, noisy, or less scannable despite technical validity. | Product-mode comparison, token/component inventory, screenshot review against stated direction and current system. | Reassert product-specific hierarchy, typography, palette, density, imagery, and restrained component structure; rerender complete states. |
| Contrast or state distinction fails | Token/theme change, overlay, image background, disabled treatment, focus style, or forced mode reduces legibility. | Text/control/status becomes hard or impossible to perceive; state may rely only on color. | Automated contrast where applicable, theme/high-contrast review, focus/status inspection, and actual composite render. | Correct token/overlay/state treatment, add non-color cues, test relevant themes/states and content backgrounds. |
| Asset, font, or media failure | Missing file, wrong path, blocked origin, decode error, unavailable font, rights issue, oversized resource, or absent fallback. | Primary product/subject becomes wrong or invisible; layout shifts; task may lose meaning. | Network/console trace, asset manifest, load/error fixtures, rendered subject review, dimensions and rights/source record. | Provide truthful fallback, stabilize dimensions, repair source/loading, optimize delivery, and preserve primary subject inspectability. |
| Canvas or 3D surface is blank/misframed | Renderer lifecycle, camera, lighting, material, resize, device capability, context loss, or asset load fails. | Main interactive experience is absent, cropped, noninteractive, or misleading. | Console/network trace, nonblank pixel check, deterministic camera/state, desktop/mobile screenshots, interaction/motion and context-loss checks. | Fix lifecycle/framing/assets, add capability fallback and cleanup, verify actual subject and interactions on declared matrix. |
| Client error lacks recovery | Network, authentication, authorization, hydration, dependency, or mutation failure leaves no truthful next action. | User is stuck, repeats unsafe action, loses work, or mistakes failure for success. | Fault injection for each eligible failure class, user-state inspection, focus/status check, retry/idempotency evidence, operational event. | Preserve input, distinguish retryable/nonretryable outcomes, reauthenticate or route appropriately, prevent duplicate effects, instrument recovery. |
| Implementation contract drifts | Component API, token, route, data schema, or shared behavior changes without consumer migration. | Some consumers silently render wrong variants or fail only in specific states. | Consumer inventory, type/build tests, representative and critical consumer renders, deprecation/migration record. | Version/migrate contract, add compatibility layer only when bounded, update consumers and rollback plan. |
| Performance hides feedback or blocks input | Main-thread work, layout shift, asset/3D load, network waterfall, or repeated rerender delays meaningful state. | User acts twice, cannot tell progress, sees unstable composition, or abandons task. | Controlled trace with user-centric milestones, interaction checks, layout/asset evidence, representative device/network; visual/functional equivalence. | Reduce/sequence work, reserve layout, show truthful progress, support cancellation where relevant, set local budgets and rerun equivalent scenario. |
| False-green verification | Snapshot is permissive/stale, fixture misses branch, retry masks failure, test asserts implementation detail, or screenshot is not reviewed. | Process reports reliability while material user behavior remains broken. | Seed known defects, inspect expected failure, review baseline changes, compare independent oracle, audit exclusions/retries. | Repair oracle/population, restore failing evidence, rerun affected claims, and disclose prior blind interval. |
| Packet/render evidence goes stale | Product/source/components/content/support matrix changes without invalidating decisions or screenshots. | Reviewers approve an obsolete experience and later changes inherit wrong guidance. | Revision/hash mismatch, dependency/invalidation graph, fixture/render manifest age and changed-consumer check. | Mark stale, refresh only after complete changed-source review, rerender affected states and update decision version. |
| Parallel ownership conflicts | Agents edit shared tokens/components/routes or make incompatible product/design decisions in isolated packets. | Individually coherent changes break integration or overwrite authority. | Shared-surface inventory, overlap map, target revision, conflict detection, integration renders/tests. | Assign one authority for shared premises, partition by stable boundaries, merge deliberately, replay cross-shard journeys. |
| Handoff lacks recovery or no-claim boundary | Final report says avoid/fail without rollback, next owner, missing evidence, or return condition. | Work stalls or a downstream user treats an unresolved gap as completion. | Reconstruct the decision from packet, evidence, changed paths, failures, owners, and next action. | Add rollback/escalation/adjacent route, exact evidence request, accepted risk, expiry, and reentry criterion. |

**Response sequence**

1. **Make the user state safe and truthful.** Stop duplicate/destructive effects, preserve work, expose current status, and provide a valid fallback or escalation.
2. **Freeze evidence.** Record revision, environment, fixture/content, browser/device/input, console/network/trace, screenshot, and exact reproduction without overwriting the failing baseline.
3. **Bound exposure.** Identify journeys, states, components/consumers, content, support modes, and owners that share the causal premise.
4. **Separate competing causes.** Change one relevant condition at a time or use an independent oracle; retain uncertainty when evidence does not discriminate.
5. **Correct the nearest responsible contract.** Fix product decision, source mapping, state machine, semantic component, visual system, asset/runtime lifecycle, verification oracle, or ownership process.
6. **Replay failure and neighbors.** Confirm the original trigger now reaches the intended outcome, recovery works, negative branches remain truthful, and nearby consumers do not regress.
7. **Promote learning.** Update reusable components/tokens, fixtures, checks, support policy, source guidance, observability, and invalidation when the cause is systemic.

Containment and diagnosis can proceed in parallel, but do not require speculative root-cause certainty before protecting users. Also avoid destructive containment that erases evidence; use reversible controls and preserve artifacts whenever consequence permits.

**Method selection**

| situation | proportionate method |
| --- | --- |
| Isolated reversible visual mismatch with deterministic reproduction | Component/state render, token/source inspection, local correction, counterstate check, and direct-consumer review. |
| Multi-state behavioral or accessibility failure | State-transition model, semantic/input checks, browser fixtures, focus/status evidence, and recovery replay. |
| Intermittent browser/network/client failure | Controlled scheduling or fault injection, environment trace, request/state identities, operational correlation, and bounded fallback. |
| Shared design-system/component regression | Consumer/invalidation inventory, contract migration, representative plus critical consumer matrix, integration review, and rollback. |
| High-consequence or specialist boundary | Domain/product/security/accessibility/operations authority, formal hazard or incident method where warranted, independent negative evidence, and accepted residual risk. |

**Focused verification protocol**

- Capture the expected wrong-state evidence first; a check that never failed for the defect does not prove the correction.
- Use realistic boundary content and material negative states, not only ideal demo data.
- Inject dependency failures only in isolated or controlled environments when direct injection could harm users or data.
- Verify user-visible truth, semantics, focus/input, data/state preservation, logs/signals, and recovery as applicable; one screenshot is rarely a complete oracle.
- Rerun a neighboring state or consumer that should remain unchanged to detect overbroad mitigation.
- Record cause confidence independently from mitigation confidence. A safe correction can be well verified while deeper origin remains provisional.

**Worked classifications**

| observation | weak response | stronger response |
| --- | --- | --- |
| Session expires while a long form is submitted. | Change the error color and add a generic retry button. | Reproduce expiry, preserve draft data, show truthful authentication state, make the operation idempotent or clearly non-retryable, restore focus after reauthentication, and add the branch to browser evidence. |
| Long localized action label overlaps an icon at narrow container width. | Reduce font size globally. | Classify content/container boundary, allow deliberate wrapping or layout transformation, preserve control geometry and hierarchy, verify longest relevant scripts plus adjacent actions, and update component contract. |
| Main 3D product viewer is a nonblank dark rectangle on one device. | Accept the pixel check because some pixels rendered. | Inspect asset/network/console/graphics/camera/material lifecycle, verify actual product subject and interaction framing, add capability fallback, and test declared device classes. |
| Screenshot suite passes after a navigation refactor, but keyboard focus disappears. | Approve because visual diff is unchanged. | Classify false-green verification plus focus continuity failure, add semantic/browser focus oracle, repair route transition behavior, and replay keyboard recovery. |

The seed's four original failures remain represented: source drift is a version/invalidation problem, generic advice is an evidence/product-fit problem, viewport-state breakage is a state/content/composition verification problem, and client recovery is a truthful-state plus side-effect problem. Their mitigations are not interchangeable. Diagnose at the causal layer, preserve the user outcome, and make the final claim no broader than the evidence.

## Retry Backpressure Guidance

`combined_evidence_inference_note`: Retry and backpressure are operational controls around frontend work; the local design source does not prescribe attempt counts, delays, queue limits, or distributed-system policy. The rules below preserve the seed's conservative posture while separating product operations, resource loading, browser verification, evidence refresh, and agent execution.

**Default rule:** do not retry merely because an operation failed. First classify the failure. A reattempt is eligible only when it has a credible changed premise or a known transient mechanism, can be replayed without unacceptable duplicate effect, has a bounded budget/deadline, remains observable, and ends in a truthful user/process state.

The seed's `one bounded retry` remains a useful local heuristic for a stale evidence read or isolated tool/runner startup fault. It is not a universal frontend product constant. Product operations must use the current service/platform contract, measured dependency behavior, user consequence, and support policy.

**Retry domains**

| domain | examples | primary risk | authority |
| --- | --- | --- | --- |
| User operation | Save, submit, upload, search, authenticate, destructive command. | Duplicate side effects, lost input, stale success, inaccessible pending state. | Product/data/API contract and owning service. |
| Resource retrieval | Data read, image/font/media/model, lazy module, cache refresh. | Retry storm, bandwidth/energy cost, blank surface, stale overwrite. | Resource/cache/network contract and product fallback policy. |
| Browser verification | Test runner startup, navigation, screenshot, accessibility scan, trace collection. | Flakiness laundering, changed environment, overwritten evidence, false green. | Verification harness and claim contract. |
| Evidence refresh | Local source reread, version/hash check, external source refresh when permitted. | Silent source substitution, stale premise, unsupported public evidence. | Current task instructions and evidence hierarchy. |
| Agent workflow | Packet/reference batch, code/edit/check loop, long reread, context recovery. | Lost work, repeated edits, partial artifacts, drift from current instructions. | Task contract, exclusive path ownership, durable journal. |
| Distributed ownership | Multiple agents or workers on separate files/shards. | Shared-component conflict, duplicate work, incompatible decisions, merge ambiguity. | Assignment manifest, shared authority owner, integration contract. |

**Eligibility gate**

Before any automatic or manual retry, answer all applicable questions:

1. **Classification:** Is the failure transient infrastructure, stale evidence, missing context, overload, conflict, permission/policy, validation, deterministic product defect, unsupported capability, or unknown?
2. **Changed premise:** What changed since the previous attempt: time-bound dependency health, refreshed credential, corrected input, new source version, restarted isolated runner, changed code, or released capacity?
3. **Replay safety:** Is the operation read-only, idempotent by contract, protected by an idempotency identity, or otherwise proven not to duplicate harmful effects?
4. **Budget:** Which local attempt/deadline/load budget governs it, who owns that value, and what terminal state follows exhaustion?
5. **Coordination:** Could components, tabs, workers, or agents retry the same dependency independently? If so, where are requests coalesced or globally limited?
6. **Cancellation and stale result:** Can navigation, user cancellation, newer requests, changed revision, or scope invalidation stop work and prevent an obsolete completion from winning?
7. **Visibility:** What stable pending, degraded, failed, blocked, cancelled, and recovered state will users/reviewers observe? Where is detailed attempt evidence retained?
8. **Recovery:** Is user input/work preserved, can focus/navigation continue, and is there a safe fallback or escalation after terminal failure?

If replay safety or consequence cannot be determined, do not auto-retry. Contain the operation, preserve evidence and user work, expose an honest state, and route the missing decision.

**Failure classification and action**

| classification | retry decision | immediate action | terminal or escalation path |
| --- | --- | --- | --- |
| Confirmed transient infrastructure | Bounded retry may be valid if replay-safe and dependency guidance permits. | Retain first failure, coordinate load, apply locally justified delay/backoff, support cancellation. | Degraded/failure state after budget; operations route if systemic. |
| Stale evidence or revision | Refresh once against the intended authority after validating identity/version. | Invalidate dependent claim and prevent stale completion from overwriting newer work. | Escalate conflict or narrow claim if authority remains unavailable. |
| Missing context or incomplete read | Do not repeat generation; obtain the exact missing source/state/environment first. | Pause downstream implementation or conclusion. | Route to owner/reference if context cannot be acquired. |
| Capacity overload or rate limit | Apply backpressure before another attempt. | Stop speculative work, coalesce requests, honor service guidance, release resources, preserve priority recovery. | Degrade, queue with bounded wait, or escalate capacity policy. |
| Validation failure | Not retryable with identical input. | Explain field/state problem without erasing input; focus/associate error appropriately. | User supplies changed valid input, creating a new operation. |
| Authentication or permission state | Invisible repetition is usually wrong until credentials/authorization change. | Preserve safe work, expose required action, prevent duplicate mutation. | Reauthenticate/request access or route to policy owner; then start a new authorized attempt. |
| Deterministic semantic, visual, state, asset, or implementation defect | Rerunning unchanged code is not remediation. | Capture reproduction, fix nearest responsible contract, add/check oracle. | Replay after implementation change; route specialist boundary if needed. |
| Unsupported browser/device/graphics capability | Repetition cannot create support. | Activate declared fallback and truthful support message. | Product/support decision or capability-specific implementation. |
| Source or owner contradiction | Repeated selection cannot resolve authority. | Freeze consequential change and record competing propositions. | Named owner decides; invalidate dependent artifacts. |
| Unknown | At most one diagnostic reattempt only when it can distinguish a hypothesis safely. | Preserve full evidence and bound harm. | Stop and escalate if the reattempt adds no information. |

**Attempt state model**

`idle -> pending -> succeeded | failed_retryable | failed_terminal | cancelled | degraded`

From `failed_retryable`, an attempt may return to `pending` only after the eligibility gate records a changed premise and remaining budget. A newer operation, navigation, revision, or cancellation makes older completions obsolete. `degraded` is a deliberate product state with known limitations and recovery, not a euphemism for an unhandled error. Exhaustion always reaches a terminal or explicit degraded state; it must not remain an indefinite spinner.

**Product operation guidance**

- Keep mutation identity separate from visual control state. Disabling a button reduces duplicate input but does not prove server-side exactly-once behavior.
- Preserve entered data and user position whenever the product contract allows. A retry affordance that first destroys input is not recovery.
- Distinguish safe read refresh from state-changing retry. For mutations, rely on authoritative idempotency/conditional-write semantics rather than frontend hope.
- Keep pending, success, partial success, validation, permission, timeout, cancellation, and terminal failure truthful. Do not announce success until the owned outcome is confirmed.
- Allow cancellation when the operation and product contract support it; cancellation should stop obsolete UI updates even when underlying work cannot be revoked.
- Restore or deliberately move focus after failure, reauthentication, retry, cancellation, and success; expose status to assistive technology without noisy repeated announcements.
- Coordinate retries across nested components and tabs where practical. Independent timers can convert a small outage into a client-generated load surge.
- Use stale/cached content only with a product-approved freshness boundary and visible semantics when staleness changes user decisions.

**Resource and rich-media guidance**

Images, fonts, video, models, textures, and lazy modules require fixed or reserved geometry where layout stability matters, explicit loading/error states, and a fallback proportional to their role. Retrying a decorative texture is different from recovering the only product image or a required form module. For canvas/3D, release renderer/resources on cancellation or route changes, ignore stale asset completion, and verify actual subject framing/interaction after recovery; a nonblank canvas is not sufficient proof.

**Verification rerun policy**

| observed check failure | acceptable next action | unacceptable shortcut |
| --- | --- | --- |
| Expected product assertion fails deterministically | Preserve failing artifact, diagnose/fix code or fixture contract, then rerun affected and neighboring checks. | Repeat until a random pass and report only the final run. |
| Browser/runner fails before target state because of known isolated startup fault | Record infrastructure classification and environment, perform one bounded clean restart, retain both results. | Relabel an in-product timeout or console error as runner noise without evidence. |
| Screenshot differs | Inspect state/revision/content/environment and review visual meaning before baseline decision. | Overwrite baseline automatically or retry until antialiasing happens to match. |
| Accessibility result changes | Verify DOM/state/timing and scanner configuration; reproduce the relevant user path. | Suppress the rule or add delay until the scan passes without causal proof. |
| Performance run is noisy | Stabilize scenario, warmup/cache policy, environment, trace, sample method, and equivalence before repeating. | Select the fastest run or compare different functional/visual states. |
| Failure disappears on rerun | Keep the first failure, classify flakiness or race, and investigate sensitivity before claiming resolution. | Treat disappearance alone as proof that no defect exists. |

**Backpressure signals**

| pressure signal | work to stop or reduce first | work to preserve |
| --- | --- | --- |
| Source or product authority unresolved | New variants, broad visual generation, implementation based on contested premise. | Conflict record, safe current behavior, exact owner question. |
| Material state/semantic/recovery gate failing | Additional polish, optional motion/media, unrelated screenshot expansion. | Diagnosis, containment, user recovery, nearest deterministic evidence. |
| Dependency overload or rate limiting | Speculative requests, duplicate component refresh, noncritical prefetch. | User-initiated critical path, cached/degraded fallback, cancellation and status. |
| Browser runner or environment unstable | Large matrix reruns and automatic baseline updates. | One diagnostic case, environment evidence, failing artifact, harness repair. |
| Reviewer or context capacity saturated | New branches, duplicate packets, ornamental prose, arbitrary evidence volume. | Atomic completed unit, decision summary, unresolved conflicts, highest-consequence examples. |
| Parallel edit/ownership conflict | Further edits to shared component/token/authority. | Durable per-owner artifacts, overlap map, integration decision and replay. |

Backpressure is not simply waiting. It prioritizes truthful state, diagnosis, recovery, and authoritative decisions while shedding speculative generation, duplicate capture, and low-consequence polish. Resume only when the blocking signal changes and the remaining scope is still valid.

**Long-running agent workflow**

1. Work in one atomic unit such as one heading-defined section, component/state slice, or independently reviewable change.
2. Persist decision rationale before its dependent implementation when the process requires that ordering; then save the implementation and run immediate structural/behavioral sanity.
3. Checkpoint progress at the declared cadence with exact paths, counts, evidence, active phase, and a nonempty next action.
4. On interruption, reread the durable boundary and current instructions; continue from the next incomplete unit rather than regenerating valid unique work.
5. Stop broad generation when exact-heading, uniqueness, placeholder, source-boundary, build, browser, or verification invariants fail. Repair the earliest broken artifact first.
6. During complete rereads, persist bounded review checkpoints so later context loss cannot erase what was actually inspected.
7. Before broad, destructive, release, or shared-state operations, revalidate scope, ownership, target revision, and explicit authorization.

The durable file is the process state. An in-memory answer, unverified patch result, or final message is not a checkpoint.

**Distributed execution**

- Assign one exclusive owner per file or stable theme shard and one authority for shared product/design/system premises.
- Record target revision, exact paths, allowed writes, section/state boundary, expected artifact schema, and completion verifier before work begins.
- Do not solve overload by allowing several agents to edit the same component, token, packet, or source of truth concurrently without explicit merge semantics.
- Preserve union, overlap, exclusions, cross-shard journey/component links, and a final integration owner.
- Merge-time verification must recheck exact path/heading/order, evidence identity, shared-component compatibility, state/render matrix, and recovery claims.
- A failed shard should not trigger blind duplicate regeneration; determine whether its durable artifacts are valid and resume from the first incomplete atomic unit.

**Attempt ledger**

Record only fields needed for the decision, but make them precise:

| field | content |
| --- | --- |
| `operation_identity` | Journey/action, resource/check/evidence/agent unit, target revision, and owner. |
| `attempt_identity` | Monotonic or otherwise unique attempt plus relation to prior operation. |
| `classification` | Failure class, cause confidence, and direct evidence location. |
| `changed_premise` | What specifically makes the new attempt informative or safer. |
| `replay_contract` | Read-only/idempotent/conditional behavior, effect identity, and duplicate protection. |
| `budget_and_schedule` | Locally authoritative attempts/deadline/backoff/load policy; no copied universal numbers. |
| `state_and_recovery` | Pending/degraded/terminal user state, preserved work, focus/status, fallback, cancellation. |
| `outcome` | Success, terminal failure, cancelled, blocked, or degraded plus resulting side-effect count. |

**Verification scenarios**

1. Inject a transient read/resource failure and verify bounded attempts, coordinated load, truthful pending/degraded state, and eventual success or terminal recovery.
2. Inject validation, permission, unsupported capability, and deterministic rendering defects; verify identical automatic retry does not occur.
3. Delay an older response until after a newer operation completes; verify the stale completion cannot overwrite current truth.
4. Trigger repeated submit input and navigation/cancellation; assert effect count, input preservation, focus/status, cleanup, and obsolete-result suppression.
5. Force sustained dependency failure or rate limit; confirm speculative work stops, budgets are honored, fallback remains usable, and recovery/escalation is visible.
6. Make a browser check flaky; confirm the first failure remains in evidence and a rerun cannot alone convert the claim to passing.
7. Interrupt an agent after packet/rationale persistence but before dependent reference/implementation save; verify resume detects the exact incomplete boundary and does not duplicate valid work.

**Examples**

| quality | example | assessment |
| --- | --- | --- |
| Good | A timed-out idempotent draft save preserves text, reports pending/failure accessibly, coalesces repeated clicks, performs a policy-approved bounded retry, and ends with confirmed save or explicit offline recovery. | Replay contract, user state, load, terminal outcome, and recovery are defined. |
| Bad | A destructive request recursively resubmits behind a spinner until one call appears successful. | Duplicate effects, no budget, no truthful terminal state, and no diagnostic evidence. |
| Borderline | A screenshot check passes on its second clean browser startup after the first runner process died before navigation. | Potentially acceptable only if infrastructure classification, environment identity, both attempts, and unchanged product premise are retained. |
| Good backpressure | Source authority conflicts, so the agent freezes implementation, persists completed unique packet work, asks the exact owner question, and keeps unrelated speculative variants out of the queue. | Capacity is redirected toward resolving the blocking premise without losing durable progress. |

No attempt count, timeout, delay, jitter, queue depth, or browser-rerun threshold is established by this reference. Calibrate those values with the authoritative dependency contract and measured product/workflow behavior. The portable invariants are changed-premise reasoning, replay safety, bounded resource use, visible terminal state, preserved evidence, and accountable recovery.

## Observability Checklist

`combined_evidence_inference_note`: Observability here covers both the evidence needed to review frontend work and the signals needed to detect/recover from product failures. This reference defines an evidence contract; it does not install runtime instrumentation, collect user data, establish a telemetry backend, or report target-product measurements.

**Default principle:** capture the smallest privacy-safe evidence set that lets an authorized reviewer answer a concrete question, reproduce or falsify the claim, identify owner/action, and determine when the evidence becomes stale. Volume without lineage is not observability.

**Minimum evidence envelope**

| field | minimum content | why it matters |
| --- | --- | --- |
| `decision_identity` | User journey, actor, material state/transition, claim or reviewer question, and consequence class. | Prevents metrics/screenshots from becoming detached from the product decision. |
| `artifact_identity` | Packet/reference/code/check/render/event identity and exact location. | Supports reconstruction without searching a transcript. |
| `source_identity` | Local/external/inference class, path/URL where permitted, version/hash/date, authority, and intentional exclusions. | Makes evidence boundary and staleness visible. |
| `implementation_identity` | Repository/workspace, exact changed paths, revision or dirty-state description, build/config/feature identity. | Links observed behavior to the code actually evaluated. |
| `state_fixture_identity` | State, content/data class, permissions, service/failure conditions, seed and fixture version as applicable. | Distinguishes meaningful branches and makes reruns comparable. |
| `environment_identity` | Viewport/container, zoom/text scale, theme, browser/engine/version, device/input, network/cache, graphics capability, locale/time zone where relevant. | Explains environment-dependent composition, behavior, assets, and timing. |
| `proof_identity` | Exact command/check, screenshot/trace/snapshot/report, reviewer rubric/question, oracle version, and evidence location. | States how the claim could fail rather than merely saying it was checked. |
| `result_identity` | Pass, fail, blocked, accepted-risk, not-applicable, degraded, or unknown plus direct observation. | Keeps missing evidence and exceptions out of passing aggregates. |
| `attempt_recovery_identity` | Attempt sequence, failure class, changed premise, retry/cancellation, final user state, side-effect count, and recovery outcome. | Preserves failures that precede eventual success. |
| `owner_time_identity` | Responsible owner/reviewer, capture time, expiration/invalidation trigger, retention/access policy. | Makes evidence governable and prevents indefinite authority. |

Stable identifiers should link these records; do not copy sensitive user content into every artifact. Hashes or opaque correlation identities may support linkage, but they do not themselves prove semantic equivalence or grant permission to retain data.

**Decision and source checklist**

- [ ] Name the exact user task, state, intended outcome, non-goals, affected population, consequence, and current owner.
- [ ] List every local source loaded completely and every candidate intentionally excluded, with reason and current version/hash where useful.
- [ ] Separate current product/source facts, authorized external evidence, inference, proposal, owner decision, and unknown.
- [ ] Record conflicts between request, product, design system, source, external research, and implementation; do not hide which authority resolved them.
- [ ] Link each consequential recommendation to supporting evidence or a capable verification route.
- [ ] Record the invalidation trigger for source, product decision, support matrix, component contract, and evidence environment.

**Journey, state, and content checklist**

- [ ] Inventory material success, loading, empty, validation, permission, partial, timeout, offline, cancellation, external-failure, and recovery branches that apply.
- [ ] Give each fixture/state a stable identity and record transition, side effects, preserved user work, focus/status behavior, and eligible next actions.
- [ ] Define content classes that pressure wrapping, script/glyphs, media, numeric/date ranges, identifiers, user-generated text, and error length without retaining unnecessary real content.
- [ ] Record declared support and deliberately excluded combinations of container, zoom/text scale, theme, browser/device, input/accessibility mode, network/cache, and graphics capability.
- [ ] Preserve failure and counterexample fixtures, not just successful demo states.

**Implementation and design-system checklist**

- [ ] Record exact changed paths plus affected routes, layouts, components, consumers, variants, tokens, assets, data/API contracts, and dependencies.
- [ ] Distinguish reused native component/system behavior from newly introduced behavior; capture migration, compatibility, and rollback implications.
- [ ] State the chosen product mode and visual direction: hierarchy, typography, palette, density, composition, imagery/media, motion, responsive transformations, and anti-patterns rejected.
- [ ] Link implementation decisions to the state/semantic/visual contracts they satisfy; source presence alone is not proof of rendered behavior.
- [ ] Record console/build/type/lint/test/accessibility warnings and failures, including accepted exceptions with owner and expiry.

**Render and browser checklist**

- [ ] Identify every capture by revision, route/component, state, fixture/content class, container/viewport, zoom/text scale, theme, browser/engine, device/input, and capture method.
- [ ] Review hierarchy, task visibility, text fit, overlap/occlusion, stable control geometry, responsive transformation, focus/status, loading/error/recovery, and actual subject/media fidelity.
- [ ] Capture browser console and relevant network failures, unhandled errors/rejections, asset/font/model status, hydration/client transitions, and blank canvas/3D detection where applicable.
- [ ] For canvas/3D or motion, include nonblank pixels plus actual subject framing, lifecycle, interaction/movement, reduced-motion or capability fallback, resize, and cleanup evidence.
- [ ] Store baseline and candidate separately; require human or domain-specific review before accepting a changed visual baseline.
- [ ] Mark incomplete captures, animation/font instability, unavailable environments, and visual-oracle limits rather than treating them as passing.

**Product runtime checklist**

Only instrument runtime behavior under the product's approved telemetry, privacy, consent, security, and retention regime.

- [ ] Choose events from user outcomes and recovery decisions, not DOM clicks alone: task started/completed/failed/cancelled/degraded, material branch entered, work preserved, retry offered/used, recovery completed.
- [ ] Preserve operation, state-transition, dependency, and attempt identities sufficient to distinguish duplicate effects, stale completion, retry recovery, and terminal failure.
- [ ] Capture environment/capability classes only at the granularity needed for action; avoid raw content, secrets, form values, sensitive URLs, accessibility details, or unrestricted high-cardinality labels.
- [ ] Define numerator, denominator, exclusion, sampling, observation period, version, and late/missing-event handling for every aggregate.
- [ ] Name the owner, action, escalation, and retirement condition for alerts/dashboards. A signal with no response path is inventory, not a control.
- [ ] Record known blind spots such as blocked scripts, offline clients, unsupported devices, consent exclusions, assistive-path invisibility, or third-party surfaces.

**Performance and workflow measurement checklist**

The seed names `p50/p95/p99`. Quantiles can be useful only when there are enough valid observations and the measurement population is defined. Do not emit all three mechanically for tiny samples or one-off reviewer tasks.

| measurement class | required definition before reporting | common confounder |
| --- | --- | --- |
| Interaction/runtime latency | User action and end condition, warm/cold/cache/network/device/browser state, sample population, clock/trace method, errors, and functional/visual equivalence. | Faster candidate omits work, content, state, animation, asset, or error handling. |
| Render/asset/3D performance | Scene/content/assets, dimensions, graphics capability, lifecycle, frame or milestone definition, loading/fallback behavior, and resource cleanup. | Comparing a blank/misframed or lower-fidelity surface with the intended subject. |
| Browser-check duration | Matrix, runner/workers, retries, fixtures, capture set, environment, setup/teardown, and pass/fail population. | Dropped states or retry-hidden failures improve duration. |
| Reviewer time | Review task, artifact size, reviewer role/familiarity, correctness rubric, disagreements, missed failures, and rework. | Faster review is achieved by lower evidence coverage or weaker questions. |
| Agent workflow time | Exact atomic units, context/source volume, tool environment, failure/retry counts, durable writes, verification, and output quality. | Unsaved work, omitted rereads, or broader unsupported claims make the process look faster. |

Report distributions or robust summaries that match the sample and decision. Preserve failures/censored runs and disclose outliers, warmup, selection, and instrumentation overhead. A latency number without the state and user outcome is not a frontend quality result.

**Signal selection guide**

| modality | strongest use | major blind spot or risk |
| --- | --- | --- |
| Structured event | Queryable state/outcome/recovery counts and correlations. | Schema can flatten semantics; careless properties leak sensitive/high-cardinality data. |
| Trace/timeline | Ordering, dependency, main-thread, network, retry, and stale-result diagnosis. | Expensive/noisy; timing alone does not prove visual or semantic correctness. |
| Metric/distribution | Population trend and capacity/latency comparison under a stable definition. | Aggregation hides severity, rare branches, and changing denominator. |
| Screenshot/video | Composition, state, content fit, motion sequence, and visual regression. | Does not establish semantics, side effects, accessibility, or causal timing alone. |
| DOM/accessibility snapshot | Structure, roles, names, state, relationships, and queryable semantics. | Does not prove assistive usability, visual hierarchy, focus sequence, or runtime recovery alone. |
| Console/network capture | Asset, client, API, caching, and dependency failure evidence. | Technical symptoms may not reveal user consequence or product correctness. |
| User report/study | Intent, comprehension, trust, task outcome, and unanticipated environment. | Sampling/recall/recruitment constraints; requires ethical and privacy-aware handling. |
| Review packet | Reconstructable source-decision-implementation-render handoff. | Can become stale or a second authority if not linked/invalidation-aware. |

Use independent modalities when a claim crosses their blind spots. For example, a screenshot plus semantic query plus interaction check can provide stronger evidence than three screenshots of the same state.

**Attempt and retry observability**

- Record every material failed attempt before eventual success, its classification, changed premise, retry budget, delay/backpressure policy source, and final result.
- Preserve side-effect identity/count for mutations and stale-result suppression for reads/navigation.
- Distinguish user-initiated new operations from automatic retries, and infrastructure reruns from product reruns.
- Include cancellation, degraded fallback, terminal exhaustion, and recovery completion; an endless pending state is not a missing metric but a product failure.
- Do not collapse retry sequences into one success rate when repeated attempts affect load, user wait, duplicate risk, or confidence.

**Compact review packet**

Prefer an indexed summary over a raw transcript dump:

```text
decision: <journey/state/outcome and bounded claim>
sources: <local/external/inference identities, versions, exclusions, conflicts>
change: <exact paths, components/consumers, revision>
matrix: <material states/content/containers/browsers/inputs/assets>
proof: <commands, checks, renders/traces, reviewer questions, result classes>
failures: <direct observations, attempts, containment/recovery, unresolved risk>
owners: <decision/review/recovery owners and invalidation/expiry>
next: <one concrete action or completed boundary>
```

The summary must link to durable evidence rather than paraphrasing it beyond recognition. Keep raw logs/traces only when they are needed for diagnosis, audit, or reproduction and are safe to retain.

**Privacy, security, and governance gate**

| question | required response |
| --- | --- |
| Is collection authorized and necessary? | Name the approved purpose, owner, legal/policy basis where applicable, and less invasive alternatives considered. |
| Could evidence contain secrets or personal/sensitive content? | Redact at source, use synthetic fixtures/opaque IDs, restrict capture and access, and test redaction. |
| Is cardinality bounded? | Use controlled classes for state/environment/content and reject arbitrary user strings, URLs, stack payloads, or component-generated identifiers. |
| Is retention proportional? | Set local retention/deletion policy, access/audit rules, and expiration for screenshots, traces, logs, and packets. |
| Are under-observed users/states represented safely? | Use deliberate synthetic, accessibility, participatory, support, or controlled test evidence rather than invasive blanket capture. |
| Can evidence be weaponized or misread? | Limit access, preserve definitions/denominators, separate fact from inference, and show blind spots. |

**Verification of observability itself**

1. Inject or stage one known material failure in each active class: behavior/state, semantic/input, asset/runtime, retry/recovery, and evidence/source as applicable.
2. Confirm the signal fires with correct journey/state/revision/environment and result classification while prohibited sensitive values remain absent.
3. Starting from the compact packet or dashboard, have a reviewer locate direct evidence, reproduce the state, identify affected scope, and name the next owner/action.
4. Verify failed and retried attempts remain visible, stale evidence invalidates, and a newer revision cannot be overwritten by older capture.
5. Exercise retention/deletion/access controls and schema-version compatibility in the approved environment.
6. Check that every alert or leading indicator maps to containment, recovery, investigation, or retirement; remove unactionable noise.
7. Record blind spots and no-claim boundaries that the test cannot observe.

**Good, bad, and borderline records**

| quality | record | assessment |
| --- | --- | --- |
| Good | Account-recovery timeout state links revision, fixture class, browser/input, network fault, screenshot, semantic/focus check, attempt trace, preserved input, successful recovery, and owner. | Supports consequence, diagnosis, replay, and invalidation without requiring raw user content. |
| Bad | "p95 is 180 ms and console errors are zero." | Scenario, population, sample, browser/device, state, collection method, functional equivalence, error capture, and action are absent. |
| Borderline | Desktop screenshots for success/loading/error are stored with revision but no content class, keyboard path, or browser engine. | Useful visual evidence for a narrow claim; insufficient for responsive, accessibility, or browser-wide reliability. |
| Good compact audit | Changed-path list and exact check/render identities summarize results, link raw bounded failures, name unresolved risks, and provide expiry. | Reviewable size preserves rather than discards reconstructability. |

**Leading indicators and failure signals**

Choose only signals that map to the current reference use. Candidate leading indicators include material-state fixture coverage, supported keyboard-path evidence, changed-consumer render coverage, source-invalidation freshness, and recovery-branch checks. Candidate failure signals include blank/stale-success states, duplicate effects, inaccessible controls/focus loss, unhandled client/asset failures, retry exhaustion, unresolved source conflicts, and stale evidence reuse. These are categories, not measured target values; define local population, severity, owner, and action before operational use.

Retire or revise a signal when its product state, denominator, schema, support matrix, or action changes; when teams repeatedly work around it; or when a more direct outcome contract replaces a proxy. Good observability makes failure and recovery more legible. It should not incentivize suppressing reports, excluding difficult populations, or collecting more user data than the decision requires.

## Performance Verification Method

`combined_evidence_inference_note`: This section defines how to test a frontend or evidence-workflow performance claim. It reports no target-product benchmark, browser profile, user distribution, reviewer study, or measured speedup. Targets must come from a current product/service requirement, an established platform budget, or a locally approved experiment, not from the seed's uncalibrated number.

**Seed claim reconciliation**

| seed statement | preserved concern | correction |
| --- | --- | --- |
| `interaction latency p95 under 100 ms for local UI actions` | User input needs timely truthful feedback and must not be blocked by avoidable work. | No action boundary, product, browser/device, sample, clock, workload, or source supports a portable `100 ms` p95 gate. Define a local milestone and target provenance. |
| `no layout overlap across mobile, tablet, and desktop screenshots` | Content and controls must remain coherent at supported responsive states. | Overlap is a visual/functional invariant, not a latency percentile; arbitrary device labels may miss container, zoom, content, and transition boundaries. Verify the declared matrix separately. |
| `primary workflow completion improves without layout, accessibility, or state regressions` | Optimization must preserve the user outcome and quality contract. | Define completion, population, baseline, state/accessibility/visual equivalence, failures, and practical effect before claiming improvement. |
| Input/source/tool-call/wall-clock/quantile/reviewer-time packet | Process performance needs reproducible workload and quality evidence. | Counts alone do not show useful work; capture artifact/evidence scope, retries, correctness, reviewer decisions, missed defects, and rework. |
| Reviewer identifies next action/gate/stop without unrelated files | The reference should reduce reconstruction burden. | Test with a frozen review task and rubric; do not claim better decision time without an executed comparison. |

**Performance claim contract**

Every claim must identify:

1. **Outcome:** the user journey, state/transition, actor, intended result, and consequence being measured.
2. **Metric:** the exact start event, end event, units, clock/mark source, aggregation, error/cancellation treatment, and why it reflects the outcome.
3. **Target provenance:** product requirement, service/platform contract, measured baseline plus approved budget, or explicit experiment hypothesis with owner and date.
4. **Population:** content/data, state, device/browser/input, network/cache, graphics capability, locale, build/revision, and user/request classes represented or excluded.
5. **Equivalence:** behavior, data/result, semantics/accessibility, visual composition/fidelity, assets, error/recovery, and support contract that must remain equal or deliberately change.
6. **Method:** controlled lab, component profiler, browser trace, synthetic journey, field measurement, review study, or combination plus blind spots.
7. **Decision rule:** practical regression/improvement boundary, uncertainty treatment, required independent gates, owner, and next action.

If any field is missing, describe the work as investigation or a measurement proposal rather than a verified performance result.

**Measurement domains**

| domain | useful measures | mandatory companion evidence | common invalid comparison |
| --- | --- | --- | --- |
| Interaction responsiveness | Input-to-feedback, event delay, main-thread task/queue, update/paint milestone, completion, duplicate action. | Correct state/result, pending/status semantics, input/focus behavior, errors/cancellation, representative device/browser. | Candidate acknowledges input quickly but defers or omits necessary work without truthful state. |
| Navigation/data workflow | Start-to-usable state, phase timings, dependency waterfall, completion/failure/recovery. | Same route/data/content/auth/cache/network, state graph, rendered usable milestone, failure population. | Warm successful candidate versus cold/error baseline or different result volume. |
| Layout/render stability | Unexpected movement, overlap/occlusion, content fit, stable control geometry, composition transition. | Screenshots/video/geometry at boundary content, containers, zoom/text scale, fonts/themes, interaction states. | Faster paint shows fallback font/blank media or ignores late content shift. |
| Asset/media/3D | Fetch/decode/parse/upload, first meaningful subject, interaction/frame behavior, memory/resource lifecycle. | Same assets/fidelity/camera/material, actual subject/framing, fallback, graphics/device, cleanup/context-loss evidence. | Candidate renders a blank, lower-detail, cropped, static, or noninteractive surface. |
| Resource use | Transfer/requests, CPU/main thread, memory, graphics resources, energy proxy where available. | Equivalent outcome, declared lifecycle, representative concurrency and device constraints. | Resource reduction comes from dropped states, assets, checks, or user value. |
| Browser verification | Setup, journey/check/capture phases, retry/failure rate, matrix throughput. | Same tests/states/content/browsers/captures, expected failure sensitivity, retained first failures, result quality. | Faster suite silently samples or retries away difficult cases. |
| Agent/reference workflow | Source volume, atomic sections/changes, tool work, failures/retries, durable writes, wall time. | Same exact artifact/evidence contract, uniqueness/completeness, verification, reviewer correctness and rework. | Faster run leaves unsaved sections, generic packets, omitted rereads, or unsupported claims. |
| Reviewer decision | Time to correct adopt/adapt/avoid/route/approve/reject decision, confidence, disagreement, missed defects, rework. | Frozen tasks/artifacts, reviewer role/familiarity, rubric, ground truth or adjudication, sample/exclusions. | Shorter review is achieved by hiding evidence or asking an easier question. |

**Method selection**

| question | preferred starting method | add when needed |
| --- | --- | --- |
| Did a code change regress a reproducible interaction? | Controlled browser trace/profile with fixed state fixture and direct behavior/render gates. | Representative low-capability device or field distribution if environment sensitivity matters. |
| Which component/render phase consumes time? | Component/framework profiler and targeted trace under realistic props/state. | End-to-end journey to confirm local improvement changes user outcome. |
| Does page/journey behavior hold across real environments? | Synthetic controlled journey plus privacy-approved field outcome/latency evidence. | Segmented device/network/content analysis with denominator and blind-spot review. |
| Does responsive composition remain usable? | Boundary content/container/zoom render matrix and geometry/interaction checks. | Device/browser sampling, visual reviewer, accessibility/input evidence. |
| Does an asset or 3D optimization help? | Frozen asset/scene/camera/fidelity trace and rendered subject/interaction comparison. | Graphics capability/device matrix, context-loss/cleanup and fallback testing. |
| Does a packet/reference reduce workflow burden? | Controlled reviewer task and reconstruction rubric with equivalent artifact scope. | Multiple reviewers, disagreement adjudication, downstream error/rework observation. |

Microbenchmarks are useful for isolated mechanisms but do not establish end-user improvement. Field data is realistic but confounded and privacy-sensitive. Synthetic journeys are repeatable but can miss real content and behavior. Use the smallest complementary set that answers the claim.

**Measurement card**

| field | required record |
| --- | --- |
| `hypothesis_and_decision` | Expected mechanism, practical outcome, target provenance, owner, and action for pass/regress/inconclusive. |
| `baseline_candidate` | Exact revisions/build flags/configuration/dependencies and why they differ only in intended factors. |
| `scenario` | Journey/state/transition, input, fixture/content/result size, auth/dependency/failure conditions, and completion oracle. |
| `environment` | Hardware/device, OS, browser/engine/version, viewport/container, zoom/text scale, theme, input, network/cache, graphics, locale/time zone where relevant. |
| `equivalence_contract` | Behavior/result, state coverage, semantics/accessibility, visual/fidelity/assets, error/recovery, and support policy comparisons. |
| `instrumentation` | Clock/marks, trace/profile tools, collection version, overhead assessment, screenshot/semantic/console/network evidence. |
| `run_protocol` | Setup, warmup, cold/warm policy, ordering/interleaving, repetition, concurrency, cleanup, retries, failures/censoring, and stopping rationale. |
| `analysis` | Raw run location, distribution/summary suited to sample, variability/outliers, practical effect, confounders, and uncertainty/no-claim boundary. |
| `verification` | Independent correctness/render/accessibility/state checks, slow/failing-run inspection, and counterexample or neighboring scenario. |
| `result` | Observed evidence, bounded conclusion, target decision, owner sign-off, and invalidation/retest trigger. |

Do not prefill numeric run counts, percentile thresholds, warmups, or significance rules from this digest. Choose them from expected variability, product risk, available population, and an analysis plan that can support the intended decision.

**Comparability gate**

Before interpreting timing/resource differences, confirm:

- baseline and candidate implement the same intended user task and result;
- material success, loading, error, cancellation, and recovery branches remain covered;
- content/result volume and expensive transformations are equivalent or deliberately analyzed;
- semantic controls, keyboard/focus/status behavior, accessibility requirements, and support modes remain intact;
- typography, imagery/media, motion, layout, responsive behavior, and visual fidelity are equivalent or the product-approved change is part of the hypothesis;
- asset/model/texture resolution, camera/framing, interaction, and fallback are not silently reduced;
- browser/device/network/cache/graphics/build/configuration differences are controlled or segmented;
- failures, timeouts, cancellations, retries, and incomplete runs stay in the population with explicit treatment;
- no measurement work shifts outside the interval without being accounted for in the full journey.

Failure of comparability does not always invalidate the product change, but it changes the claim. Report a staged-experience or fidelity tradeoff, not a pure optimization.

**Controlled comparison protocol**

1. Write the card and expected mechanism before examining favorable results.
2. Validate state fixtures, build identity, instrumentation marks, clocks, and independent outcome/render/accessibility oracles.
3. Capture baseline and candidate evidence under matched conditions. Interleave or randomize ordering where drift could bias one side.
4. Retain raw runs, including slow, failed, cancelled, retried, and outlier observations; investigate distinct states rather than deleting them automatically.
5. Inspect traces/profiles to determine whether the proposed mechanism changed and whether work merely moved to another phase.
6. Review rendered and semantic evidence at representative and boundary states. For 3D/canvas, verify actual subject, framing, interaction, fallback, and cleanup.
7. Summarize with statistics appropriate to the observations. Quantiles such as p50/p95/p99 require a defined population and enough observations to be meaningful; report uncertainty and sample limitations.
8. Compare the practical effect with the locally authoritative target and user consequence, not only statistical or decimal differences.
9. Rerun a neighboring scenario expected to remain stable and any failure branch affected by the mechanism.
10. Publish the bounded result, confounders, no-claim area, raw evidence location, owner decision, and invalidation trigger.

**Field and operational complement**

Where authorized product telemetry exists, segment outcome and latency by relevant release, journey/state, device/browser/network/content class, success/failure/retry/recovery, and capability without collecting unnecessary sensitive content. Define numerator, denominator, sampling, missing events, consent exclusions, bot/internal traffic, and late data. Compare before/after populations cautiously; release, traffic, content, dependency, and instrumentation changes can mimic performance effects.

Operational evidence can reveal long-tail environments but rarely proves mechanism by itself. Reproduce representative regressions in a controlled trace, and use a controlled improvement to predict which field segment should change. If the prediction fails, retain the conflict rather than selecting the nicer dataset.

**Responsive and layout verification**

Treat overlap, clipping, occlusion, reflow, hidden actions, and unstable geometry as quality outcomes alongside performance, not as a substitute for latency measurement.

- Select containers/viewports from actual composition transitions, then include boundary widths rather than only named phone/tablet/desktop classes.
- Use realistic long/short content, localization/script classes, errors, user data, zoom/text scale, themes, fonts/loading states, and dynamic updates.
- Inspect primary task/hierarchy, wrapping, overflow, focus order, status, sticky/fixed elements, menus/dialogs, and late media/font arrival.
- Automated DOM geometry or screenshot diffs can identify candidates; rendered human review determines whether composition remains coherent.
- Keep fixed-format controls/boards/canvases dimensionally stable where required and test overflow/fallback deliberately.

**Asset and 3D performance verification**

- Freeze asset/model versions, dimensions/fidelity, scene/camera/material/lighting, animations, and target subject.
- Separate fetch, decode/parse, upload/initialization, first meaningful subject, interaction/frame behavior, resize, and cleanup/context-loss phases.
- Verify the candidate is nonblank, correctly framed, visually equivalent for the product decision, interactive/moving where intended, and usable with fallback/reduced-motion/capability paths.
- Inspect network, console, memory/resource lifecycle, stale loads, cancellation, and route transitions on desktop/mobile and representative graphics classes.
- Do not call a blank canvas, missing model, lower-resolution product, or disabled interaction faster.

**Reference and reviewer workflow study**

To test the seed's pass condition, create a frozen set of representative frontend decisions with adjudicated expected actions or a clear expert rubric. Give reviewers versioned reference/packet artifacts and record:

- whether they identify user task, evidence boundary, adopt/adapt/avoid/route action, verification gate, stop condition, and recovery;
- decision time plus reading/search path, unresolved questions, disagreements, confidence, and requested unrelated files;
- correctness/severity of missed issues, not only speed;
- reviewer role, familiarity, artifact order, interruptions, and learning effects;
- downstream rework or escaped error when feasible.

Compare against a defined baseline artifact under equivalent tasks. A reference that is quicker because it omits evidence is not better. This evolution did not execute such a study, so reviewer-time improvement remains a future measurement proposal.

**Anti-gaming and validity checks**

- Reject fastest-run selection, unreported retries, silent failure deletion, changed fixtures, and unmatched cache/device/browser conditions.
- Reject optimizations that drop supported states, accessible semantics/input, real content, assets/fidelity, recovery, or verification unless the product explicitly changes its contract and the tradeoff is measured.
- Treat instrumentation overhead, thermal/load drift, background work, dependency variation, and build differences as confounders to record and control where possible.
- Keep distribution and state classes visible; one aggregate can hide a slower critical branch or constrained device population.
- Do not infer causality from before/after field trends alone, or generalize one lab device to the support matrix.
- Do not claim a percentile from a sample that cannot estimate it meaningfully; report raw observations or a simpler summary with limits.

**Worked examples**

| quality | example | assessment |
| --- | --- | --- |
| Good runtime comparison | The same authenticated search fixture, result count, error handling, semantics, and rendered composition are compared on declared browser/device/network classes; interleaved traces show less main-thread work and a practically better completion distribution without regressions. | Mechanism, outcome, population, equivalence, and uncertainty are reviewable. |
| Bad runtime claim | "Reload was twice as fast after optimization" based on one warm candidate after a cold baseline with fewer images. | Cache, sample, and asset fidelity confound the result. |
| Borderline responsive claim | Three screenshots show no overlap at chosen widths. | Useful evidence for those exact states; not a latency result and insufficient for content, zoom, input, or transition-wide support. |
| Good 3D comparison | Same model/material/camera and interaction are traced on representative graphics classes; subject framing, nonblank pixels, motion/input, fallback, memory cleanup, and completion milestones remain equivalent. | Resource/timing gain does not depend on losing the actual product experience. |
| Bad workflow claim | Packet generation uses fewer tool calls after skipping complete source reads and final verification. | It is cheaper work with a weaker artifact, not a process optimization. |
| Borderline reviewer result | One author finds their own digest faster to navigate. | A useful anecdote; familiarity and sample prevent a general reviewer-performance claim. |

**Result statement template**

```text
claim: <bounded outcome and locally sourced target>
population: <states/content/environments represented and excluded>
comparison: <baseline/candidate identities and equivalence result>
method: <protocol, observations, failures/retries, analysis>
evidence: <raw distributions, traces, renders, semantic/behavior gates>
result: <observed practical effect and uncertainty>
decision: <pass, regress, inconclusive, product tradeoff, or more evidence>
boundary: <what cannot be inferred>
owner_and_retest: <decision owner and invalidation trigger>
```

The portable pass condition is methodological: the intended user outcome is explicit; target and population have provenance; baseline and candidate are comparable; raw failures remain visible; independent functional, state, accessibility, visual, and recovery gates pass; and the conclusion is no broader than the evidence. The portable fail condition is claiming improvement from unmatched, incomplete, cherry-picked, or lower-quality work. No universal latency target or measured gain is established here.

## Scale Boundary Statement

`combined_evidence_inference_note`: This reference can frame, implement, and verify bounded frontend experience work. It is not a product portfolio control plane, production observability/SLO system, security or domain authority, device lab, migration orchestrator, or substitute for a maintained design system. Scale by preserving the user decision and transferring only premises that require another method.

**Sufficiency decision**

The reference is sufficient only when all of the following can be made explicit and reviewable:

1. The material user journey, states/transitions, consequences, and product owner are bounded.
2. Current product, design system, local source, implementation, and permitted external evidence can be identified and reconciled.
3. Affected components/consumers, content classes, support environments, assets, and shared contracts can be inventoried with a credible completeness boundary.
4. The team can implement or specify the change, render material states, verify behavior/semantics/accessibility/visuals/performance as claimed, and provide recovery.
5. Cross-boundary dependencies have named interfaces, authorities, evidence requests, and integration owners.
6. Evidence can be persisted, invalidated, and reviewed without silently sampling away critical users or states.

If one condition fails, choose among narrowing the claim, indexing the surface, sharding by stable boundaries, federating with another authority, or stopping. Do not compensate with more prose.

**Scale dimensions**

| dimension | local signal | scale pressure | boundary implication |
| --- | --- | --- | --- |
| User journeys and state coupling | One bounded task with explicit branches. | Cross-product/role journeys, shared side effects, many interdependent transitions. | Need journey ownership, system integration, possibly domain/product architecture. |
| Components and consumers | Direct component/route with known consumers. | Shared primitives/tokens/navigation/forms across many products or unknown consumers. | Need design-system/API versioning, migration governance, and integration matrix. |
| Content/data variability | Known fixture and boundary content classes. | Open-ended user content, many locales/scripts, media, policy-sensitive or regulated data. | Need content/localization/domain/privacy authority and maintained fixture strategy. |
| Responsive/support matrix | Bounded containers, zoom, themes, browsers/devices, inputs, graphics. | Broad device/browser/assistive/graphics/offline support with environment-specific failures. | Need support policy, device/accessibility labs, capability telemetry, and release controls. |
| Assets/media/3D | Known files and lifecycle with inspectable fallback. | Large pipelines, rights/provenance, streaming, scene/toolchain/device specialization. | Need asset/content pipeline, legal/source authority, graphics/performance specialists. |
| Source and evidence discovery | Ranked current local authority and bounded permitted research. | Unbounded public discovery, conflicting canonical sources, many changing repositories/systems. | Need research/source governance, deterministic indexes, and explicit open-discovery boundary. |
| Verification/evidence | Reproducible focused checks and reviewable render matrix. | Combinatorial suites, flaky environments, large baseline stores, production-only behavior. | Need test/visual platform, sampling policy, operational observability, and evidence retention governance. |
| Ownership and coordination | One decision owner and a few explicit collaborators. | Multiple independent systems, organizations, release trains, or contested product/design authority. | Need program/architecture governance, merge/release coordination, and accepted-risk ownership. |
| Runtime consequence | Reversible local behavior with controlled rollout. | High traffic, destructive/sensitive paths, explicit service levels, incident/rollback obligations. | Need production operations, security/domain review, SLO/telemetry and incident controls. |
| Reviewer/context capacity | Complete evidence fits a coherent review. | Packets, screenshots, traces, and conflicts exceed reviewer reconstruction capacity. | Need indexing, staged decisions, specialized review, and persistent governance artifacts. |

No one dimension or count defines scale. A single shared authentication form or product viewer may cross several boundaries; many independent static components may remain straightforward.

**Operating levels**

| level | this reference's role | required control | stop/promotion signal |
| --- | --- | --- | --- |
| Focused local | Own one reversible state/component correction end to end. | Current source/product anchor, direct consumers, reproduce/fix/render/check/recover. | Shared contract, unknown consumers, product-policy conflict, or broader support claim. |
| Bounded journey | Own one material journey and applicable state/content/environment matrix. | Journey/state contract, product/design owner, implementation and complete declared verification. | Multiple independent systems/owners or evidence matrix cannot be bounded safely. |
| Shared frontend system | Coordinate component/token/navigation/form/layout change across consumers. | Stable consumer inventory, version/migration/rollback, representative plus critical integration evidence. | Incomplete candidate recall, portfolio-wide governance, incompatible product/domain policies. |
| Indexed product program | Guide repeated bounded decisions using deterministic route/component/state/render/source indexes. | Freshness/hash checks, complete candidate recall for each claim, invalidation, global consistency checkpoints. | Index cannot detect staleness or the claim requires open-ended discovery/production control. |
| Sharded program | Define common contract and integrate parallel stable journey/component/system shards. | Exclusive ownership, union/overlap/exclusions, shared authority, merge semantics, integration owner and replay. | Shards share unresolved semantics or integration evidence cannot reconstruct end-to-end journeys. |
| Federated specialist program | Retain frontend outcome while domain/security/accessibility/operations/assets/performance/research methods own specific premises. | Exact evidence request, authority, handoff artifact, conflict rule, return condition, final decision owner. | No capable owner/environment exists or risk cannot be bounded; pause/narrow the claim. |
| Product operations/portfolio governance | Supply frontend evidence into maintained organizational systems. | Production SLO/telemetry, rollout/incident controls, design-system governance, support policy, privacy/security, portfolio ownership. | This digest is advisory only; it cannot authorize product-wide operational claims. |

These are modes, not maturity scores. A task may stay a focused change technically while requiring one high-assurance federated decision.

**Choose a scaling strategy**

| pressure | strategy | safety condition | tradeoff |
| --- | --- | --- | --- |
| Complete review is cheap | Read/render/check the bounded surface directly. | Scope and authority genuinely complete. | Least infrastructure, but poor fit once review cost or churn rises. |
| Large stable code/source surface | Deterministic index or dependency/source graph, then retrieve complete selected candidates. | Index inputs/version/hash, candidate recall, stale-state rejection, and direct source verification. | Faster orientation; index can become a stale second authority. |
| Repeated component/state review | Component stories/fixtures/render manifests with targeted replay. | State/content/support identities and invalidation remain current. | Reuse improves speed; fixture idealization can hide product reality. |
| Independent journey/component slices | Parallel exclusive shards with shared contract and integration checkpoint. | Low semantic overlap, explicit union/exclusions, one shared-premise authority. | Throughput increases; coordination and merge evidence become work. |
| Broad but risk-skewed matrix | Equivalence classes plus critical/boundary representatives and no-global-claim boundary. | Grouping rationale, disconfirming examples, omissions, and escalation trigger are explicit. | Reduces combinations; a wrong equivalence silently removes users/states. |
| Multiple specialized concerns | Federate with adjacent references/owners while preserving frontend outcome. | Typed handoff, return evidence, contradiction handling, terminal owner. | Better authority; handoff latency and evidence translation increase. |
| Production-scale release | Use native rollout, telemetry, SLO, incident, security/privacy, and change-governance systems. | Current operational owners and policies control values and action. | Real control; this digest remains one input rather than the authority. |

Prefer existing codebase/component/design/test/observability systems when they are current and capable. A new packet, index, graph, dashboard, or rendering layer must have an owner, validity check, measured benefit, and retirement path.

**Safe narrowing contract**

Narrowing is valid when the resulting claim can be fully stated inside the boundary and all external interfaces are visible. Record:

- included journey/state/component/consumer/content/support/environment/owner population;
- excluded population and why it cannot invalidate the local claim;
- cross-boundary data, side effects, shared components/tokens, product decisions, and recovery;
- separate owner and verification for omitted consequential behavior;
- explicit prohibition on product-wide, all-browser, all-user, accessibility-wide, reliability, or performance inference from local evidence;
- trigger that expands scope when a new shared link or counterexample appears.

Arbitrary truncation because context, screenshot, or deadline capacity was reached is not safe narrowing. It is incomplete evidence and must be reported as such.

**Stable partition contract**

Partition in this preference order when it matches the actual system:

1. Independent user journey or actor outcome.
2. State family with clear transition and side-effect interfaces.
3. Route/layout boundary whose product task and components are substantially independent.
4. Component/consumer migration slice under one shared component contract.
5. Design-system or asset subsystem with one governing owner.
6. Evidence specialization such as accessibility, performance, device, security, or content under a typed return contract.

Theme-file, equal-page, equal-line, or equal-screenshot splits are only valid if they also satisfy semantic independence. The partition record must include shared source/product revision, design direction/system, support policy, fixture/evidence schema, ownership, overlap, exclusions, shared-premise authority, and integration tests/renders.

**Source and dependency narrowing**

A source list is not a context strategy. For large codebases or corpora:

- rank canonical product/source/design/system artifacts before related commentary;
- index deterministic identities such as route, component, consumer, token, state fixture, test, asset, owner, and revision;
- preserve source spans or exact locations rather than relying on generated summaries alone;
- verify index candidate recall against complete known samples and seed deliberately stale/missing entries;
- reject results when source revision/hash no longer matches;
- traverse inbound consumers and cross-journey dependencies before changing shared contracts;
- use complete direct reads for selected authoritative artifacts and retain conflict/unknown status;
- mark open-ended public discovery as open; do not pretend a bounded index is exhaustive.

Graph or index output prioritizes what to inspect; it does not replace semantic reading, rendered verification, or product authority.

**Distributed execution contract**

| concern | required rule |
| --- | --- |
| Ownership | One exclusive editor per file/shard and one owner for each shared product/design/system premise. |
| Identity | Frozen target revision, exact writable paths, instruction/spec version, artifact schema, and evidence environment. |
| Coverage | Explicit union, overlap, exclusions, critical/boundary representatives, and no-claim zones. |
| Shared surfaces | Components, tokens, routes, data contracts, assets, support policy, and product decisions cannot diverge silently. |
| Persistence | Save one complete atomic rationale unit before its dependent implementation where required; sanity-check immediately and journal at declared cadence. |
| Merge | Reconcile conflicts through authority, not last writer; rerun exact heading/schema plus cross-shard journey/component/render checks. |
| Failure | Preserve valid durable work, resume at first incomplete unit, and do not duplicate regeneration merely because a worker stopped. |
| Final authority | One integration reviewer owns end-to-end claim, unresolved risks, recovery, and release/handoff decision. |

Parallelism is unsafe when agents need to make the same unresolved semantic decision. Serialize that decision, then parallelize independent evidence or implementation.

**Long-running workflow boundary**

Context drift is a reliability failure when it changes instructions, evidence identity, ownership, or completed-work recognition. Mitigate by:

- persisting exact atomic boundaries rather than relying on conversation memory;
- recording phase, changed paths, section/state counts, current checks, unresolved conflicts, and next action;
- rereading current task/spec and durable artifact around interruption/resume;
- saving review checkpoints during long complete rereads;
- rerunning normalized uniqueness, heading/order, placeholder, table/fence, build/browser, hash, and focused evidence gates as applicable;
- stopping broad work at the first structural or authority failure and repairing it before expansion.

Summaries are indexes to durable evidence, not substitutes for inspecting the changed artifact.

**Terminal boundaries and typed routes**

| boundary | why this digest is insufficient | required route and return evidence |
| --- | --- | --- |
| Product/domain policy | User eligibility, consequence, content truth, regulated or business rule is unresolved. | Product/domain owner returns approved decision, affected states/users, exceptions, and verification examples. |
| Security/privacy | Auth, sensitive data, threat, permission, telemetry collection, or abuse risk dominates. | Security/privacy authority returns constraints, tests/review, accepted residual risk, and operational owner. |
| Accessibility specialist/device lab | Complex assistive behavior, platform accessibility, or broad device/input support cannot be observed locally. | Specialist returns tested matrix, findings, limitations, and required implementation/retest. |
| Production SLO/traffic | Real latency/reliability, rollout, capacity, incident, or operational recovery claim is required. | Operations/service owner supplies current SLO/telemetry method, rollout/rollback, alert/action, and measured evidence. |
| Large migration/portfolio system | Many products/releases/components require governance and compatibility sequencing. | Architecture/design-system/program owner supplies version/migration plan, consumer inventory, integration/release gates. |
| Asset/content/3D pipeline | Rights, provenance, production assets, streaming, graphics pipeline, or specialist fidelity dominates. | Content/legal/graphics owner returns authorized assets, lifecycle/performance/fallback and device evidence. |
| Open research | Current public evidence must be discovered beyond the authorized local corpus. | Research process returns source identities, dates, authority, conflicts, and exact claims; browsing permission remains task-specific. |

The frontend owner then reconciles returned evidence with user journey, state, semantics, composition, implementation, render, and recovery. Routing does not transfer the final product outcome silently.

**Promotion and stop signals**

Promote or route when any of these becomes true:

- material journeys/states cross independent systems or release owners;
- a component/token/contract change has unknown or incompatible consumers;
- support requires environments, assistive paths, devices, graphics, or production conditions unavailable to the current method;
- source discovery is open-ended or canonical authority cannot be ranked;
- product/domain/security/operations policy remains unresolved;
- evidence matrices exceed safe complete review and no defensible equivalence/shard model exists;
- retries/flakiness/overload prevent trustworthy verification;
- reviewers cannot reconstruct claims, conflicts, and recovery within the available decision process;
- local evidence is being used to imply product-wide reliability, accessibility, compatibility, or performance.

Stop means narrow, contain, or transfer authority with a return contract. It does not mean produce a confident generic answer.

**Scale verification**

1. Freeze the scale card: dimensions, population, pressure, strategy, owner, and claim boundary.
2. For indexes/graphs, compare candidates with complete known slices, inject stale/missing records, and verify revision/hash rejection.
3. For equivalence classes, include boundary and counterexamples that could disprove grouping; retain critical variants regardless of convenience.
4. For shards, audit union/overlap/exclusions and shared-premise ownership before work, then replay cross-shard journeys and shared consumers after integration.
5. For packets/renders, test invalidation when source, component, fixture, support matrix, or product decision changes.
6. For reviewers, perform reconstruction from the indexed handoff and record unresolved questions, disagreement, and evidence search cost.
7. For production claims, verify that native operational owners, targets, telemetry, rollout, and recovery controls exist; otherwise narrow the claim.
8. Record measured benefit and maintenance cost of the scale mechanism; retire it when direct/native methods become cheaper or its validity cannot be maintained.

**Worked boundaries**

| case | scale decision | reason |
| --- | --- | --- |
| One existing settings toggle has a narrow focus-state regression and known consumers. | Focused local. | Direct source/behavior/render/recovery evidence is complete and reversible. |
| A shared form field changes label, error, focus, and spacing contracts across products. | Shared system with consumer migration; federate product/accessibility decisions as needed. | Small diff has broad semantic and ownership reach. |
| Hundreds of independent content pages need the same current typography token correction. | Indexed/sharded execution under one token authority and integration sample. | Large count is manageable because shared contract and invalidation are stable. |
| Agents receive equal page ranges and each independently modifies global navigation tokens. | Invalid partition. | Shared semantics and implementation collide; local success cannot integrate safely. |
| A product needs verified real-user latency, rollout guardrails, and incident recovery under production traffic. | Product operations boundary. | This digest can define user milestones but cannot establish SLO, telemetry population, or release authority. |
| A broad redesign has no settled product task or content policy. | Provisional exploration or pause. | Visual generation cannot substitute for unresolved product authority; no global quality claim is available. |

No page, component, source, agent, screenshot, browser, or owner count is established as a universal capacity. Scale is a property of coupling, consequence, variability, observability, and governance. The durable principle is to keep each local claim complete, make shared boundaries explicit, and require evidence that the integration mechanism itself detects omission and staleness.

## Future Refresh Search Queries

`local_evidence_observation`: The seed supplies three future search phrases. Current instructions prohibit browsing, so they are preserved as unexecuted maintenance proposals, not as evidence that any official documentation, repository example, release note, or migration guidance exists.

**Exact seed query registry**

| search_query_label_name | search_query_text_value | execution_status | future decision target |
| --- | --- | --- | --- |
| `official_docs_query_phrase` | frontend design quality patterns official documentation best practices | `unexecuted_no_browse` | Discover current primary documentation only if a named frontend behavior, accessibility, design-system, browser, or framework claim needs external authority. |
| `github_repository_query_phrase` | frontend design quality patterns GitHub repository examples | `unexecuted_no_browse` | Find maintained implementation examples for a bounded pattern after product/system fit and repository authority are defined. |
| `release_notes_query_phrase` | frontend design quality patterns changelog release notes migration | `unexecuted_no_browse` | Check a known tool/framework/component/platform version change when local implementation or support guidance may have drifted. |

The query strings are intentionally preserved verbatim for seed traceability, but they are broad and may have low precision. A future maintainer should not run them mechanically. First identify the decision and current product/version; then create a narrower query while retaining the seed label as provenance.

**Refresh triggers**

Research may be warranted only when explicitly authorized and one of these triggers exists:

- a consequential statement depends on current browser, platform, framework, accessibility, security/privacy, or tooling behavior not established locally;
- a known dependency/version changed and the local implementation conflicts with current primary documentation or release evidence;
- a local source references public evidence whose identity, scope, or freshness must be verified;
- target-product browser/device behavior contradicts the current reference and direct diagnosis does not resolve whether guidance changed;
- an adjacent specialist route requires current standards or official support policy;
- a maintained example is needed to compare a bounded alternative, not to copy generic visual style.

Do not browse merely to decorate the reference with links, replace product authority with popularity, or search for confirmation after the decision is already made.

**Decision-bound future query plan**

Every row remains `unexecuted_no_browse` in this evolution. Angle-bracket terms are placeholders for a future authorized maintainer to replace with exact current identities.

| future query family | query template | preferred evidence | decision it may change | execution_status |
| --- | --- | --- | --- | --- |
| Browser/platform behavior | `<browser-or-platform> <version> <feature-or-failure> official documentation support` | Current vendor/platform documentation and compatibility/release record. | Support matrix, fallback, semantic/input behavior, asset/canvas lifecycle, or verification environment. | `unexecuted_no_browse` |
| Web standard or accessibility semantics | `<control-or-pattern> <state-or-interaction> current standard accessibility official` | Current standards body and authoritative accessibility/platform guidance; specialist review where needed. | Semantic contract, keyboard/focus/status behavior, support boundary, or route to specialist evidence. | `unexecuted_no_browse` |
| Framework/runtime change | `<framework> <exact-version> <feature> official migration release notes` | Official versioned documentation, changelog/release, and migration guide. | Implementation pattern, compatibility, hydration/state behavior, dependency decision, or required regression matrix. | `unexecuted_no_browse` |
| Component/design-system implementation | `<component-pattern> <framework> maintained official example accessibility states` | Maintainer-owned repository/docs with current tests/examples and version identity. | Adopt/adapt/avoid comparison after product task and local system are known. | `unexecuted_no_browse` |
| Performance method | `<metric-or-interaction> official measurement methodology browser` | Primary browser/platform measurement documentation and, where appropriate, original research/standard. | Measurement marks, instrumentation, population, known limitations; never a copied universal budget by itself. | `unexecuted_no_browse` |
| Asset/media/3D behavior | `<graphics-or-media-api> <failure-or-lifecycle> official documentation <version>` | Current API/vendor/runtime docs and maintained implementation evidence. | Loading/fallback, cleanup/context loss, device capability, fidelity, or performance verification. | `unexecuted_no_browse` |
| Security/privacy/telemetry boundary | `<telemetry-or-client-pattern> official security privacy guidance <jurisdiction-or-policy-if-authorized>` | Authorized security/privacy standards and organizational policy; specialist owner remains required. | Data collection, consent, redaction, retention, access, and no-collection boundary. | `unexecuted_no_browse` |
| Repository issue/regression | `<known-repository> <exact-version> <error-or-behavior> issue release` | Maintainer repository issue/commit/release linked to exact version and direct reproduction. | Whether a behavior is known, fixed, regressed, or requires workaround; local browser proof remains necessary. | `unexecuted_no_browse` |

**Source preference order**

1. Current target product behavior, approved product/support policy, local code/tests/design system, and direct reproduction for product-specific facts.
2. Current official standards, browser/platform/framework/library documentation and versioned release/migration artifacts for public contracts.
3. Maintainer-owned repositories, tests, issues, commits, and examples tied to the exact version.
4. Original research or authoritative specialist guidance when the decision requires it.
5. High-quality secondary sources only as discovery leads or contextual explanation, with consequential claims traced to stronger evidence.
6. Search snippets, popularity, generic showcases, copied benchmark tables, and undated tutorials never serve as final authority.

This order is not absolute across claim types. Product policy can own intended behavior while a standard owns semantics and a browser trace owns observed implementation behavior. Preserve conflicts rather than forcing them into one ranking.

**Future execution protocol**

1. Confirm browsing/research authorization, writable scope, security/privacy restrictions, and the exact claim to refresh.
2. Freeze the current reference/source/product versions and record why local evidence is insufficient.
3. Choose one decision-bound query and preferred primary domains/source types; avoid broad parallel searching until terminology is validated.
4. Record exact query text, filters/domains, execution date, operator, and result-selection rationale. Search snippets are leads only.
5. Open and inspect the direct source. Capture title/publisher, direct location, publication/update date, version/scope, source class, relevant claim, and limitations.
6. Seek a second independent or directly observed source only when consequence, conflict, or source limitations justify it; do not collect links by default.
7. Compare external evidence with current local product/source/system behavior. Record agreement, conflict, uncertainty, and authority owner.
8. Update only the dependent claim and its source map, examples, failure modes, verification, future query status, and invalidation links.
9. Rerun target product/browser/component evidence where external guidance changes an implementation or support claim.
10. Mark the query executed with outcome such as adopted, adapted, rejected, conflict-open, or no-authoritative-result. Preserve a no-claim boundary when evidence remains insufficient.

**Future result record**

| field | required content |
| --- | --- |
| `query_identity` | Seed/future label, exact executed text, filters/domains, authorization, date, and maintainer. |
| `decision_target` | Exact section/claim, user journey/state, and why local evidence was insufficient. |
| `source_identity` | Direct location, publisher/maintainer, title, version/date, source class, and retrieval evidence. |
| `claim_support` | Exact paraphrased proposition supported, source boundary, applicability, and counterevidence/limitations. |
| `product_fit` | Agreement/conflict with current product, design system, implementation, browser evidence, and owner decision. |
| `outcome` | Adopt, adapt, avoid, route, conflict-open, no-authoritative-result, or no-change plus rationale. |
| `dependent_changes` | Reference sections, source rows, examples, checks, support policy, components, fixtures, or renders invalidated. |
| `verification` | Direct source reread plus local reproduction/check/render/specialist evidence required before claim reuse. |
| `freshness` | Next invalidation event such as version/release/standard/product/support change; avoid arbitrary freshness dates without reason. |

**Acceptance and rejection rules**

Accept a public source for a bounded claim only when its identity and authority are clear, its version/scope matches the decision, direct content was inspected, limitations/conflicts are visible, and target-product evidence does not contradict the adopted conclusion without resolution.

Reject or downgrade:

- snippets without direct source inspection;
- anonymous, mirrored, generated, undated, or versionless guidance for consequential claims;
- examples that omit material state, accessibility, error/recovery, browser, or product-context constraints;
- benchmark numbers without workload/environment/method/equivalence;
- repository popularity as proof of correctness or fit;
- a newer publication date as automatic authority over a current product/standard contract;
- search results selected only because they confirm the existing thesis.

A `no-authoritative-result` outcome is valid. It should narrow the claim or trigger a specialist/direct-test route, not invite an unsourced best practice.

**Good, bad, and borderline future research**

| quality | future action | assessment |
| --- | --- | --- |
| Good | After a known framework upgrade changes hydration behavior, query the exact official version's release/migration documentation, inspect direct source, reproduce the target error state, and update only affected guidance. | Decision, authority, version, product fit, and verification are bounded. |
| Bad | Search "best frontend UI 2026," copy a highly ranked visual convention, and present it as the product default. | Popularity and recency do not establish task fit, source authority, state behavior, accessibility, or implementation evidence. |
| Borderline | Use the broad seed repository query to discover terminology and candidate maintainers. | Acceptable discovery only; no recommendation changes until direct current authoritative evidence and local fit are checked. |
| Good negative result | Official and maintainer sources do not establish the claimed support behavior, so the maintainer records uncertainty and narrows the support claim pending direct device/specialist evidence. | Research improves honesty without inventing closure. |

**Refresh verification gate**

- Exact seed labels and query strings remain traceable even when narrower executed variants are added.
- Every query has authorization and execution status; this version's rows all remain `unexecuted_no_browse`.
- Every adopted external claim links to a direct inspected source with publisher, version/date, scope, and limitation.
- Conflicts with local product/source/browser evidence are resolved by a named authority or remain visibly open.
- Dependent sections and artifacts are invalidated and reverified; adding links alone is not a refresh.
- No external result is presented as measured target-product behavior without local or operational evidence.
- Query entries that no longer change a decision are retired rather than accumulated indefinitely.

Search discovery is inherently variable: indexes, personalization, pages, repositories, and terminology change. Preserve enough query/source provenance to reconstruct the decision, but do not overstate exact result reproducibility. In this evolution, the confident facts are limited to the three seed query strings and their nonexecuted status under the no-browse instruction. No current external evidence was gathered or refreshed.

## Evidence Boundary Notes

The seed's three evidence labels are retained exactly, but their use is narrowed so a path, URL, or nearby citation cannot lend authority to a larger unsupported claim.

**Core evidence labels**

| exact label | use it for | required identity | cannot establish by itself |
| --- | --- | --- | --- |
| `local_corpus_sourced_fact` | A proposition directly observed in the named local file bytes, metadata, code, test, or other inspected artifact. | Exact path/artifact, relevant location or bounded paraphrase, observed revision/hash/date where useful, and scope. | Current runtime behavior, user outcome, publisher intent beyond text, loader/precedence, production readiness, or portability unless separately observed. |
| `external_research_sourced_fact` | A narrow proposition directly supported by an inspected current public source during an authorized research pass. | Direct URL, publisher/maintainer, title/section, access/publication/update date, version/scope, source class, and limitations. | Target-product applicability, installed-version behavior, or independent corroboration without local reproduction and conflict review. |
| `combined_evidence_inference_note` | An explicit synthesis that connects observed evidence and systems reasoning into bounded guidance, alternatives, causal explanation, or verification method. | Premises used, inferential step, applicability boundary, counterargument, uncertainty, and target evidence needed. | A quotation, measured target result, owner policy, or universal rule merely because the inference is plausible. |

In this version, `external_research_sourced_fact` has no populated current claims. The three seed URLs are preserved with `unrefreshed_no_browse`, and all future query families are `unexecuted_no_browse`. A URL identity or planned query is proposal/provenance evidence, not retrieved external evidence.

**Additional status classes**

These names are an evolved operational vocabulary, not replacements for the exact seed labels.

| status | meaning | appropriate next action |
| --- | --- | --- |
| `target_product_observation` | Direct observation from the actual application, browser, component fixture, design system, build, trace, or operational evidence under stated conditions. | Preserve revision/state/environment/oracle and bound the claim to the observed matrix. |
| `verification_result` | A named check, render review, experiment, audit, or reconstruction exercise produced pass/fail/blocked/inconclusive evidence. | Retain method, population, raw evidence, failures/retries, reviewer/owner, and no-claim boundary. |
| `proposal_not_executed` | A recommended workflow, query, measurement, check, component change, or target has not been carried out. | Do not use future-tense method as a result; name owner, prerequisites, and execution gate. |
| `owner_decision` | An authorized product/design/domain/security/accessibility/operations/release owner selected a policy or accepted bounded risk. | Record authority, alternatives, affected population, rationale, expiry, and verification/recovery obligations. |
| `conflicting_evidence` | Two or more relevant sources, observations, tests, or owners disagree at the same claimed scope. | Preserve each proposition and identity, narrow safe behavior, and route resolution to the correct authority. |
| `unknown_or_blocked` | Required source, environment, product decision, population, oracle, or authority is absent or unavailable. | Narrow or pause the claim, state consequence, request exact evidence, and define return condition. |
| `not_applicable` | A class was evaluated and does not apply to the bounded product/task, with reason. | Preserve the reason and revisit when scope/support/product changes. |

An owner decision can be authoritative for intended product behavior while still requiring implementation and rendered verification. A passing check can establish observed behavior in its matrix while not authorizing product policy. Keep authority type and evidence type distinct.

**Observed local evidence ledger**

| observation | classification | confidence and boundary |
| --- | --- | --- |
| `agents-used-monthly-archive/claude-skills-202603/plugins/frontend-design/SKILL.md` and `claude-skills/plugins/frontend-design/SKILL.md` were read as the mapped local source family. | `local_corpus_sourced_fact` | High confidence for path/body observation during this evolution; surrounding package activation/precedence was not established. |
| Both mapped bodies were observed as 42 lines with SHA-256 `d39adf3a983de7dafc75991590d54f091755f7e4163d5a5ed085ecd719157184`. | `local_corpus_sourced_fact` | Byte/hash equality is direct; it does not prove independent corroboration, ownership, licensing, or runtime loading equivalence. |
| The local skill asks agents to understand context, choose a clear aesthetic direction, implement functioning code, and avoid generic output while discussing typography, color, motion, composition, and atmosphere. | `local_corpus_sourced_fact` | Direct bounded paraphrase of the local body; it does not prove any technique fits a target product. |
| The evolved reference treats those design pressures as search space constrained by user task, current system, states, semantics, content, browser evidence, accessibility, performance, maintenance, and ownership. | `combined_evidence_inference_note` | Systems synthesis; adoption requires target product and rendered evidence. |
| The seed associates `https://react.dev/learn`, `https://threejs.org/docs/`, and `https://docs.github.com/actions` with future external roles. | `local_corpus_sourced_fact` about the seed | High confidence that the URL strings and seed roles exist; current page content, version, authority details, stability, and applicability were not retrieved. |
| No external query or URL retrieval was performed in this evolution because browsing was prohibited. | Process observation and `unknown_or_blocked` for current public content | Confident within this work process/artifact record; it is not a claim about unrelated browsing histories or the current state of the public web. |
| No target application, user study, accessibility audit, production telemetry analysis, browser performance experiment, or reviewer-time study was executed for this reference. | `proposal_not_executed` boundary for target claims | Therefore no product quality, speedup, support, reliability, usability, or capacity result is reported. |

**What the local source can and cannot support**

| source-supported intent | defensible synthesis | evidence still required before target adoption |
| --- | --- | --- |
| Understand purpose, audience, tone, and constraints before coding. | Start from user task/product mode and select a coherent direction instead of decorating a generic template. | Current product/content/owner decision, workflow/state contract, and rendered task review. |
| Make intentional typography, color, motion, composition, and visual-detail choices. | Treat each technique as an alternative with semantic, responsive, accessibility, performance, and maintenance boundaries. | Target fonts/content/locales, tokens/themes, inputs/preferences, assets, browser renders, performance and owner evidence. |
| Avoid unexamined generic design and framework defaults. | Require product-specific hierarchy or a distinctive signal appropriate to the subject and repeated workflow. | Existing design system/brand/product conventions and comparison showing that divergence improves the actual experience. |
| Match implementation complexity to the visual vision. | Include functioning states and technical craft as part of design quality; restraint may require equal precision. | Working target code, state/error/recovery behavior, build/browser checks, shared-consumer and maintenance evidence. |

The source cannot establish a universal font blacklist, palette, motion amount, layout composition, card policy, responsiveness matrix, accessibility conformance, performance threshold, browser support, production reliability, or measured development benefit. This evolved reference supplies causal boundaries and verification proposals; the target system supplies decisions and results.

**Claim record**

For a consequential or reusable claim, retain:

| field | content |
| --- | --- |
| `claim_identity` | Exact atomic proposition and the user/implementation decision it changes. |
| `evidence_class` | One or more labels/statuses above, without merging fact, inference, policy, result, and unknown. |
| `evidence_identity` | Path/URL/artifact/check/render/owner plus exact location, revision/version/date, and direct bounded support. |
| `scope` | Product/journey/state/content/environment/population and exclusions. |
| `authority` | Why this source or owner can decide this claim type; conflicts and precedence remain visible. |
| `confidence` | High/moderate/provisional/unknown with the concrete reason, not emotional certainty. |
| `counterevidence_limit` | Contradictions, plausible alternative, oracle blind spot, and what cannot follow. |
| `target_verification` | Check, render, experiment, specialist review, or owner decision needed before action/reuse. |
| `invalidation` | Source/product/component/support/environment/owner event that reopens the claim. |

One paragraph may contain several claim records. If source, scope, confidence, or verification differs, split it. Do not attach a source to a paragraph and assume every sentence inherits support.

**Authority and inference rules**

1. **Directness:** The source must support the exact proposition, not merely discuss the same topic.
2. **Scope:** A source statement retains its prerequisites, version, product context, exclusions, and uncertainty.
3. **No transitive authority:** Source A citing B does not make A primary evidence for B's claim; inspect the needed direct source when consequence warrants it.
4. **No duplicate inflation:** Hash-identical or copied sources add provenance identities, not independent substantive confidence.
5. **No URL promotion:** A preserved or plausible URL becomes external evidence only after authorized direct inspection and metadata capture.
6. **No inference laundering:** Synthesis must not be phrased as source wording or a measured result.
7. **No test overreach:** A check/render supports only its fixture, state, environment, oracle, and declared equivalence/generalization.
8. **No owner substitution:** A technical observation cannot choose product policy; an owner preference cannot prove implementation behavior.
9. **Negative evidence matters:** Failures, blocked environments, disagreements, and counterexamples remain visible alongside passing artifacts.
10. **Current beats ceremonial:** When product behavior conflicts with a generic pattern, diagnose and resolve authority; do not preserve the pattern merely because it is documented.

**Promotion ladder**

| starting status | evidence needed for promotion | resulting bounded status |
| --- | --- | --- |
| Design idea or workflow proposal | Product fit/non-goals, owner decision where needed, implementation plan, and falsifiable checks. | Approved bounded proposal, still not an outcome. |
| Combined inference | Supporting premises, explicit counterconditions, target component/state implementation, and relevant render/behavior evidence. | Target-verified guidance for the observed matrix. |
| Preserved external URL/query | Explicit research authorization, direct current source inspection, version/scope/limitations, and local applicability. | `external_research_sourced_fact` for one narrow proposition. |
| Component/browser fixture result | Representative/boundary state/content/environment rationale and direct product comparison. | Product observation for the stated population; no universal promotion. |
| Owner decision | Implementation and verification under declared support/recovery contract. | Operational product policy for the named revision/population. |
| Performance/reliability method | Executed controlled/operational measurement with equivalent outcome, population, raw evidence, and owner decision. | Bounded result with uncertainty; not a portable constant. |

Promotion is reversible. Changed source bytes, dependency/browser version, product decision, component consumer set, state/content/support matrix, evidence oracle, environment, or owner policy can invalidate it.

**Evidence anti-patterns**

- "The documentation says" without a direct source, version, section, and bounded proposition.
- "Research shows" when only a future query or preserved URL exists.
- "The local corpus confirms" when two paths contain identical bytes and no independent source.
- "Production-ready" inferred from a skill description, build success, or one polished screenshot.
- A numerical target or improvement copied without workload, environment, population, method, result, and uncertainty.
- A generic systems recommendation presented as if quoted from the 42-line frontend-design source.
- A passing screenshot generalized to semantics, accessibility, behavior, devices, content, or reliability.
- An owner choice hidden as neutral evidence, or a test result treated as authority over product intent.
- A conflict silently resolved by selecting whichever evidence supports the desired implementation.
- A stale packet/reference/source map reused after its invalidation event.

**Worked classifications**

| statement | correct treatment |
| --- | --- |
| "The local skill advises committing to a clear aesthetic direction before implementation." | `local_corpus_sourced_fact`, with exact local source identity and paraphrase scope. |
| "Therefore every operations dashboard should use unusual typography and asymmetrical overlap." | Unsupported overgeneralization; product mode, readability, density, design-system, and rendered evidence are missing. |
| "For repeated operational tools, distinctive hierarchy can come from task-specific information architecture while controls remain predictable." | `combined_evidence_inference_note`; verify against target users, current system, states, and browser evidence. |
| "The Three.js documentation proves the target viewer will render correctly." | Invalid in this version: URL unrefreshed, installed version/scene/browser unknown, and no target render occurred. |
| "A controlled target fixture renders the named model nonblank and correctly framed in the declared browsers, with interaction and fallback checks." | `target_product_observation` plus `verification_result` for that matrix; not all-device production proof. |
| "The candidate reduces p95 interaction latency." | A result only after metric/population/method/equivalence and observed distribution exist; otherwise `proposal_not_executed`. |
| "Product owner accepts a restrained design-system-compatible direction for this workflow." | `owner_decision`; still requires implementation, state, accessibility, visual, and performance verification as claimed. |

**Evidence audit protocol**

1. Inventory consequential, quantitative, current, external, product-wide, and production claims first; then risk-sample lower-consequence synthesis.
2. For each sampled claim, identify its atomic proposition, evidence/status label, exact source/artifact, authority, scope, confidence, and invalidation.
3. Open the direct local or authorized external evidence and confirm the paraphrase without expanding prerequisites or certainty.
4. Verify external rows are truly refreshed before any `external_research_sourced_fact`; preserved URLs and query plans must remain proposal/unknown.
5. Trace combined inference to premises, counterargument, operational example, and target verification; reject authoritative tone without support.
6. Trace target results to revision, state/content/environment, oracle, raw failures/retries, and no-generalization boundary.
7. Inject a deliberately unsupported consequential claim or stale identity in a controlled audit; confirm the gate rejects or blocks it.
8. Change one source/component/fixture/support identity and verify dependent claims/renders/checks become stale rather than silently passing.
9. Record conflicts and unresolved evidence with owner/next action; absence of closure is not a failed audit if the claim is narrowed honestly.

**Known, inferred, proposed, and unknown summary**

| category | current boundary |
| --- | --- |
| Known locally | Two mapped path identities share one observed hash-identical 42-line frontend-design body; exact seed headings, URLs, and query strings exist; local files were read for this evolution. |
| Inferred | State-aware, evidence-linked, accessibility-conscious, product-mode-specific, rendered verification and recovery guidance follows from local design pressure plus general frontend/systems reasoning. |
| Proposed | Reliability profiles, failure registry, retry/backpressure, observability schema, performance protocol, scale mechanisms, future research, and many target checks are methods to execute, not measured outcomes. |
| Unknown | Actual target users/product states, support matrix, accessibility, browser/device behavior, assets/3D, performance, production reliability, telemetry/privacy policy, current external-source content, and organizational capacity. |
| Owner-dependent | Product direction, brand/design-system divergence, support policy, accepted risk, SLO/telemetry, rollout, security/privacy, and specialist route decisions. |

**Reuse and invalidation**

- Reuse stable principles only with their counterconditions; do not inherit examples or local thresholds as universal requirements.
- Recheck product/version-specific guidance after source, framework/browser, component/token, content/state, asset, support, or owner changes.
- Preserve superseded evidence and rationale when historical interpretation matters, but mark it noncurrent.
- Prefer target components, tests, render manifests, design-system records, and approved operational systems as living authority; prevent this prose reference from becoming a competing source of truth.
- Retire claims, queries, metrics, and evidence artifacts that no longer change a decision or whose validity cannot be maintained.

The strongest conclusion available is methodological: frontend quality improves when a clear product-specific direction is reconciled with complete states, semantic/input obligations, real content and assets, maintainable implementation, rendered evidence, explicit failure/recovery, and honest source boundaries. Whether a particular design is usable, accessible, fast, reliable, production-ready, or better remains a target-system claim that this corpus and no-browse evolution did not establish.
