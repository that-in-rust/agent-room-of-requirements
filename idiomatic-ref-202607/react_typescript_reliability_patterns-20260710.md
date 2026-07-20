# React Typescript Reliability Patterns

**Decision supported.** This section helps decide which reliability posture a React TypeScript task adopts and which of the twelve scored patterns govern its implementation. The seed title promises React reliability but the seed never states the bundle's own thesis, the 202602 agent file declares that reliable React TypeScript comes from modeling UI as a typed state machine around trustworthy server-state boundaries, and its premise check disclaims being a generic style guide.

**Recommended default and causal basis.** Treat the UI as a typed state machine, separate client-only from server-capable code, parse transport data before components trust it, and test behavior over implementation. The agent file targets seven failure modes frontend LLMs miss, widened state, overgrown client state, duplicated fetch logic, inconsistent form validation, optimistic UI without rollback, timing-dependent components, and UI that collapses under navigation misbehavior, and every scored pattern maps to one of them.

**Operating conditions and assumptions.** The task involves .tsx components, hooks, route boundaries, forms, query layers, optimistic mutations, or frontend reviews asking whether the UI survives slow data, bad data, retries, or navigation changes, per the SKILL.md when-to-use list. This reference governs typed React and TSX reliability decisions, the shared TypeScript baseline it inherits, strict railguards, schema-first parsing, unknown at boundaries, lives in the companion typescript-coder-01 and is assumed, not restated.

**Failure boundary and alternatives.** Reading this theme as a component cookbook loses its point, the twelve patterns are reliability countermeasures ordered by failure cost, not a menu of stylistic options. Bounded alternatives and recoveries: the 1750-line historical Idiom-React file for teams wanting worked TDD specifications and naming conventions beyond the scored bundle, at five times the reading cost.

**Counterexample, gotchas, and operational comparison.** The agent file assumes the typescript-coder-01 baseline silently, applying its React patterns over loose compiler settings rebuilds the widened-state failure the premise check names first. Good: a form task routed to schema-validated forms and exhaustive unions before code is written. Bad: treating the file as optional style advice and shipping optimistic writes with no rollback. Borderline: applying the patterns to a plain JavaScript React app, directionally useful, the typed guarantees do not exist there.

**Verification, evidence, and uncertainty.** Check delivered components against the seven premise-check failure modes and confirm each touched boundary cites its governing scored pattern. Full reads this session of the 394-line agent file, the 38-line SKILL.md, the 22-line reference map, and the 1750-line historical corpus. How well the 202602 pattern set tracks React releases after its preparation window is unverifiable without external retrieval.

**Second-order consequence.** The premise check is itself a routing device, by declaring what the file is not, a generic style guide, it deflects the most common misuse before a single pattern is read.

**Revision decision.** Open by stating the typed-state-machine thesis and the seven LLM failure modes it exists to counter, so readers know which mistakes this file is armed against.

**Retained seed evidence.** The exact theme title and reliability framing remain unchanged. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

## Source Evidence Mapping Table

**Decision supported.** This section helps decide which local file, copy, or unretrieved link may justify each class of claim in this theme. The seed table lists six local rows under two generic roles while the mapped set actually contains one canonical agent file, two byte-identical copies of it inside the codex skill, a 22-line router, a 38-line skill wrapper, and one 1750-line historical corpus from a different lineage.

**Recommended default and causal basis.** Cite the 202602 agent file as the canonical pattern source, the SKILL.md for workflow claims, the map for routing claims, and the historical corpus for worked-example and naming claims. Diffing the three 394-line files this session confirmed react-reliability-reference.md and typescript-react-coder-01.md are exact copies of the claude-skills-202602 agent file, so six paths carry only four distinct documents.

**Operating conditions and assumptions.** The archive paths stay byte-stable so the identity claims established by diff this session remain checkable. The table records provenance for this document's claims, it does not certify that the six external URLs resolve or that the historical corpus's 2026-01-30 content matches current React guidance.

**Failure boundary and alternatives.** Citing the two copies as independent corroboration double-counts one author's judgment, agreement among identical files is not evidence of anything. Bounded alternatives and recoveries: collapsing the two copy rows into a single canonical row with copy locations noted, cleaner provenance at the cost of diverging from the seed's path-per-row convention.

**Counterexample, gotchas, and operational comparison.** The external rows include Express, MongoDB, and Three.js links that belong to sibling stack themes, none of the four distinct local documents cites any of them for React reliability claims. Good: citing the agent file's scoreboard for a pattern-priority claim. Bad: citing the reference copy and the claude original as two agreeing sources. Borderline: citing the historical corpus for a hook-naming rule, valid as historical fact, its 4-word convention is not part of the 202603 skill.

**Verification, evidence, and uncertainty.** Rerun the diff between the three 394-line paths and confirm identity before repeating any copy-related claim. The diff run this session showing zero differences between the three copies, plus full reads of all four distinct documents. Whether the copies were intentional pinning or accidental duplication is not recorded anywhere in the bundle.

**Second-order consequence.** The duplication is informative rather than wasteful, it shows the 202603 skill deliberately froze the 202602 agent file as its reference text, dating the entire pattern set to one authoring moment.

**Revision decision.** Annotate the six rows with distinct-document identity, one canonical agent file, two verbatim copies, one router, one wrapper, one historical corpus.

**Retained seed evidence.** All six local rows and all six external rows with their column values remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| source_location_path_key | source_category_artifact_type | source_authority_confidence_level | source_usage_synthesis_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/claude-skills-202602/typescript-react-coder-01.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/codex-skills-202603/typescript-react-coder-01/SKILL.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/codex-skills-202603/typescript-react-coder-01/references/react-reliability-reference.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/codex-skills-202603/typescript-react-coder-01/references/reference-map.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/codex-skills-202603/typescript-react-coder-01/references/typescript-react-coder-01.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/idiomatic-references-202602/Idiom-React-Frontend-Patterns.md | local_corpus_source_material | local_corpus_sourced_fact | historical idiomatic pattern corpus |
| https://www.typescriptlang.org/docs/handbook/intro.html | external_research_source_material | external_research_sourced_fact | primary TypeScript language documentation |
| https://expressjs.com/en/ | external_research_source_material | external_research_sourced_fact | Node.js web framework documentation |
| https://www.mongodb.com/resources/products/compatibilities/using-typescript-with-mongodb-tutorial | external_research_source_material | external_research_sourced_fact | MongoDB TypeScript integration guidance |
| https://react.dev/learn | external_research_source_material | external_research_sourced_fact | primary React learning and component model documentation |
| https://www.typescriptlang.org/docs/handbook/intro.html | external_research_source_material | external_research_sourced_fact | TypeScript language model for React applications |
| https://threejs.org/docs/ | external_research_source_material | external_research_sourced_fact | primary Three.js API documentation |

## Pattern Scoreboard Ranking Table

**Decision supported.** This section helps decide which of the twelve scored patterns a constrained effort adopts first. The seed scores three document-hygiene rules while the canonical agent file publishes a real twelve-row scoreboard from 97 behavior-first testing down to 88 component boundary normalization that the seed never mentions.

**Recommended default and causal basis.** Adopt patterns in scoreboard order when triaging an unfamiliar codebase, starting from behavior-first tests and boundary discipline before micro-optimizations. The agent file's scores encode failure cost, testing tops at 97 because regressions land where users feel them, client-server boundary discipline and schema-validated forms share 96 because both prevent whole classes of runtime confusion, and boundary normalization anchors at 88 as the last line against wire noise.

**Operating conditions and assumptions.** The task allows incremental adoption, a greenfield feature can apply all twelve at once while a legacy refactor takes them in descending score order. This ranking orders the bundle's twelve reliability patterns for adoption priority, it does not rank the historical corpus's naming or architecture patterns, which carry no scores at all.

**Failure boundary and alternatives.** Treating the seed's 95, 91, and 88 as measured React data fabricates evidence, they are the corpus template's authorial emphasis and say nothing about component reliability. Bounded alternatives and recoveries: the historical corpus's quick-reference card, which pairs each pattern with its anti-pattern in one table, better for review checklists than for adoption sequencing.

**Counterexample, gotchas, and operational comparison.** The two 91-92 rows, progressive enhancement and optimistic rollback, invert in priority for content-heavy versus interaction-heavy apps, the scoreboard is a default ordering, not a law. Good: a legacy triage that lands tests, then boundary splits, then form schemas. Bad: starting with memoization tuning while forms validate inconsistently. Borderline: elevating abortable effects above its 89 score for an app with heavy background fetching, defensible when timing bugs dominate the incident log.

**Verification, evidence, and uncertainty.** Check each adopted pattern's claimed score against the agent file's scoreboard table before citing priority. The twelve-row scoreboard read in full from the canonical agent file. The scores are one author's calibration from 202602, no repository measurement validates the ordering.

**Second-order consequence.** The scoreboard's top four rows are all boundary disciplines, tests at the user boundary, client-server splits, form schemas, and query layers, the file bets that React fails at its edges before it fails in its middles.

**Revision decision.** Import the agent file's twelve-row scoreboard as the operative ranking and keep the seed rows as corpus-process guidance.

**Retained seed evidence.** The three scored seed rows with tier labels remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| pattern_identifier_stable_key | pattern_score_numeric_value | pattern_tier_adoption_level | pattern_failure_prevention_target |
| --- | ---: | --- | --- |
| `react_typescript_reliability_patterns` | 95 | default_adoption_pattern_tier | Source Map First: Load local react typescript material before synthesizing reliability patterns recommendations. |
| `react_typescript_reliability_patterns` | 91 | default_adoption_pattern_tier | Evidence Boundary Split: Separate local facts, external facts, and inference before giving agent instructions. |
| `react_typescript_reliability_patterns` | 88 | default_adoption_pattern_tier | Verification Gate Coupling: Attach each recommendation to at least one command, checklist, or review gate. |

## Idiomatic Thesis Synthesis Statement

**Decision supported.** This section helps decide what organizing principle new React TypeScript guidance for this theme must satisfy. The seed recites the generic load-local-first formula while the canonical file states a sharp domain thesis, reliable React TypeScript comes from modeling UI as a typed state machine around trustworthy server-state boundaries.

**Recommended default and causal basis.** Evaluate any new React guidance against both thesis halves before adopting it into this theme. Every scored pattern derives from one of the thesis's two halves, exhaustive unions, typed contracts, and boundary normalization serve the typed state machine, while query layers, schema forms, and rollback-ready mutations serve trustworthy server-state boundaries.

**Operating conditions and assumptions.** The app has genuine server state, purely local tools like canvas editors exercise only the state-machine half and the boundary half idles. The thesis governs React and TSX reliability guidance, the underlying TypeScript language discipline is inherited from typescript-coder-01 and the thesis presumes it.

**Failure boundary and alternatives.** A thesis that drops either half degrades predictably, state machines over untrusted transport render garbage safely, and parsed transport feeding boolean-soup state reintroduces impossible UI states. Bounded alternatives and recoveries: the historical corpus's implicit thesis, semantic anchoring through naming conventions and TDD specifications, which optimizes LLM code generation rather than runtime reliability.

**Counterexample, gotchas, and operational comparison.** The thesis is framed for App Router style client-server splits, apps on purely client-side routers still benefit but the client-server boundary vocabulary maps loosely. Good: rejecting a proposed pattern that stores server responses in component state, it violates the boundary half. Bad: adopting a state library because it is popular with no thesis test. Borderline: accepting a purely ergonomic naming rule, orthogonal to both halves, harmless but belonging to the historical corpus's lineage.

**Verification, evidence, and uncertainty.** Trace each thesis clause to its supporting patterns, unions and contracts to the machine half, queries and schemas to the boundary half. The chosen-thesis section and final synthesis of the canonical agent file read in full. Whether the two-half thesis stays complete as React server components mature is a judgment the 202602 file could not have settled.

**Second-order consequence.** The final synthesis compresses the thesis to five habits, explicit client-server boundaries, schema-driven forms, server state as query state, exhaustive unions, and behavior testing, a mnemonic form the thesis statement itself lacks.

**Revision decision.** Restate the thesis verbatim with its two-half structure made explicit, typed state machines on the inside, trustworthy server-state boundaries on the outside.

**Retained seed evidence.** The three labeled thesis statements remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`local_corpus_sourced_fact`: The local row for `react_typescript_reliability_patterns` contains 6 source path(s), which should be treated as the first retrieval surface for this theme.
`external_research_sourced_fact`: The external source map provides public documentation, repository, or ecosystem analogues where available.
`combined_evidence_inference_note`: Reliable use of React Typescript Reliability Patterns comes from loading the local corpus first, checking public ecosystem guidance second, and converting both into verification-backed agent decisions.

## Local Corpus Source Map

**Decision supported.** This section helps decide which mapped document a given question should open first. The seed map lists six paths with heading signals but no guidance on which document answers which question class, and it hides that three of the six paths are the same 394-line document.

**Recommended default and causal basis.** Classify the incoming question as pattern, activation, navigation, or worked-example before opening anything, then open exactly one distinct document. The four distinct documents partition cleanly by question class, the agent file answers pattern and priority questions, SKILL.md answers when-to-activate and workflow questions, the reference map answers where-to-read questions, and the historical corpus answers worked-example, naming, and TDD-specification questions.

**Operating conditions and assumptions.** Questions arrive separable into those four classes, mixed questions must be split before routing. This map routes between the mapped local documents, routing within the agent file's own sections is the job of its reference map, one level down.

**Failure boundary and alternatives.** Routing by path count misleads, a reader opening all six paths reads the same scored patterns three times and concludes the bundle is deeper than it is. Bounded alternatives and recoveries: merging the SKILL wrapper and agent file mentally into one skill unit, workable for humans, but agents given all six paths verbatim will re-read copies unless told of the identity.

**Counterexample, gotchas, and operational comparison.** The copies are not harmless padding for search tooling, heading-based rg across the bundle returns every scored-pattern heading three times, and a reader may treat triplicate hits as strong signal. Good: opening only SKILL.md to decide whether a review task activates the skill. Bad: reading both reference copies hunting for differences that a diff already ruled out. Borderline: opening the historical corpus for a memoization question, its decision matrix answers it, though the agent file's store-subscription pattern is the bundle's current word.

**Verification, evidence, and uncertainty.** Spot-check the heading signals of each row against the live files and confirm the question-class key still matches their sections. Section-by-section content audit of all four distinct documents performed this assignment. Whether future bundle revisions de-duplicate the copies or let them drift apart independently is a maintainer choice this map cannot constrain.

**Second-order consequence.** The historical corpus is the only mapped document from a different lineage, its 202602 idiomatic-references origin makes it the bundle's external memory, everything else is one skill's self-description.

**Revision decision.** Attach a question-class key to each row and mark the two copy rows as duplicates of the canonical agent file.

**Retained seed evidence.** All six local source rows with title, heading signals, and usage role remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| local_source_filepath_value | local_source_title_text | local_source_heading_signals | local_source_usage_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/claude-skills-202602/typescript-react-coder-01.md | typescript-react-coder-01 | TypeScript React Coder 01; Premise Check; Inherited Baseline; Chosen Thesis; Pattern Scoreboard; Core Patterns | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/codex-skills-202603/typescript-react-coder-01/SKILL.md | typescript-react-coder-01 | TypeScript React Reliability; Overview; When To Use; Workflow; Reference Use; Output Expectations | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/codex-skills-202603/typescript-react-coder-01/references/react-reliability-reference.md | typescript-react-coder-01 | TypeScript React Coder 01; Premise Check; Inherited Baseline; Chosen Thesis; Pattern Scoreboard; Core Patterns | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/codex-skills-202603/typescript-react-coder-01/references/reference-map.md | Reference Map | Reference Map; Jump Points; Section Search; Use Order | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/codex-skills-202603/typescript-react-coder-01/references/typescript-react-coder-01.md | typescript-react-coder-01 | TypeScript React Coder 01; Premise Check; Inherited Baseline; Chosen Thesis; Pattern Scoreboard; Core Patterns | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/idiomatic-references-202602/Idiom-React-Frontend-Patterns.md | Idiom-React-Frontend-Patterns.md | Idiom-React-Frontend-Patterns.md; React Idiomatic Patterns Reference (LLM Context Anchor); Section 1: The Four-Word Naming Convention (React Adaptation); 1.1 Components (PascalCase, 4 semantic units); 1.2 Custom Hooks (camelCase, 4 words); 1.3 Event Handlers (camelCase, 4 words) | historical idiomatic pattern corpus |

## External Research Source Map

**Decision supported.** This section helps decide what confidence external links may contribute to this theme's claims and which links a refresh should fetch first. The seed map carries six URL rows of which three, Express, MongoDB, and Three.js, serve sibling stack themes and are cited by none of the four distinct local documents for React reliability claims.

**Recommended default and causal basis.** Treat react.dev and the TypeScript handbook as the retrieval queue for freshness challenges and quote all rows only as candidate pointers. The canonical agent file's own source trail names five local notebook paths, none of them public URLs, so this theme's genuine external anchors are only the React and TypeScript documentation rows, and even those arrive from the corpus template rather than the bundle.

**Operating conditions and assumptions.** The linked doc sites keep their URL structure, react.dev and typescriptlang.org are stable, tool tutorial links are the volatile minority. This map queues external verification targets, it grants no live-fact authority until a dated retrieval of a specific page exists.

**Failure boundary and alternatives.** None of the six URLs was retrieved during this evolution, every row is candidate material and no current-behavior claim about React, TypeScript, or any listed tool may rest on them. Bounded alternatives and recoveries: checking a target repository's pinned React and TypeScript versions and changelogs directly, which answers current-behavior questions faster than documentation pages.

**Counterexample, gotchas, and operational comparison.** The duplicated TypeScript handbook row appears twice with different role texts, quoting role text without noticing the shared URL manufactures a phantom second source. Good: writing that exhaustive-union guidance aligns with discriminated-union documentation as an unverified candidate pointer. Bad: asserting current React server-component behavior from the unretrieved react.dev row. Borderline: citing the MongoDB row for a fullstack MERN task, on-topic for the stack, off-topic for this React reliability theme.

**Verification, evidence, and uncertainty.** Confirm every externally-flavored claim in this document carries an unretrieved-candidate label and no retrieval date it cannot show. Zero external fetches recorded in this assignment's working notes, and the source trail's machine-local paths read from the agent file. Which linked pages have changed materially since the bundle's 202602-202603 preparation window is unknowable without fetching them.

**Second-order consequence.** The agent file's source trail points at unavailable machine-local notebook paths, meaning the bundle's true research basis is unauditable from this repository, a sharper provenance gap than unretrieved public links.

**Revision decision.** Mark the React and TypeScript rows as this theme's priority retrieval targets and flag the Express, MongoDB, and Three.js rows as sibling-theme inheritance.

**Retained seed evidence.** All six external rows with their boundary labels remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| external_source_url_value | external_source_name_text | external_source_usage_role | evidence_boundary_label_value |
| --- | --- | --- | --- |
| https://www.typescriptlang.org/docs/handbook/intro.html | TypeScript handbook | primary TypeScript language documentation | external_research_sourced_fact |
| https://expressjs.com/en/ | Express documentation | Node.js web framework documentation | external_research_sourced_fact |
| https://www.mongodb.com/resources/products/compatibilities/using-typescript-with-mongodb-tutorial | MongoDB TypeScript guide | MongoDB TypeScript integration guidance | external_research_sourced_fact |
| https://react.dev/learn | React documentation | primary React learning and component model documentation | external_research_sourced_fact |
| https://www.typescriptlang.org/docs/handbook/intro.html | TypeScript handbook | TypeScript language model for React applications | external_research_sourced_fact |
| https://threejs.org/docs/ | Three.js documentation | primary Three.js API documentation | external_research_sourced_fact |

## Anti Pattern Registry Table

**Decision supported.** This section helps decide which React code behaviors this theme must reject on sight in review. The seed lists three generic documentation failures while the mapped sources publish sixteen concrete React rejections, the agent file's seven anti-patterns and the historical corpus's nine across state, effect, and rendering trios.

**Recommended default and causal basis.** Review React diffs against the sixteen combined rows, prioritizing the state trio, prop-state syncing, eager initializers, and stored derived state, which the historical corpus ranks first. Each source anti-pattern inverts a scored pattern, whole-store subscriptions invert minimal subscription, duplicated form rules invert schema-validated forms, nullable property soup inverts exhaustive unions, missing rollback inverts optimistic transactions, and index keys invert stable identity.

**Operating conditions and assumptions.** Reviews see the diff plus surrounding component context, several rows, like missing AbortController cleanup, are invisible in isolated hunks. This registry names React and TSX code failures, corpus-document process failures stay in the seed rows, and TypeScript language-level failures belong to the companion baseline.

**Failure boundary and alternatives.** A registry without the React-specific rows cannot catch the failures this bundle exists to prevent, generic advice-quality checks pass code that resets forms on parent re-render. Bounded alternatives and recoveries: lint automation for the mechanically detectable rows, index keys, inline object props, components defined inside render, leaving human review for the semantic rows.

**Counterexample, gotchas, and operational comparison.** Arbitrary waitForTimeout thinking in UI tests is the agent file's most easily missed row, it hides inside green test suites and only surfaces as flakiness under load. Good: bouncing a diff that adds a whole-store subscription to a leaf component. Bad: approving optimistic writes because the happy path demos well. Borderline: allowing index keys in a static never-reordered list, technically safe, the corpus still forbids it to keep the rule teachable.

**Verification, evidence, and uncertainty.** Cross-check each registry row against the scored pattern it inverts and confirm its detection signal is observable in an ordinary diff review. The seven-item anti-pattern list and the three TDD-specified anti-pattern trios read in full from both sources. Relative base rates of the sixteen failures in real codebases are unmeasured here, the ordering is authorial judgment.

**Second-order consequence.** The two sources attack the same failures from different angles, the agent file names what reviewers reject while the historical corpus pairs each rejection with a corrected code sample and a TDD specification that would have caught it.

**Revision decision.** Import both source sets with their detection signals, review-time greps for store subscriptions and index keys, test-time checks for rollback paths and cleanup functions.

**Retained seed evidence.** The three seed process rows with their detection signals remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| anti_pattern_failure_name | failure_cause_risk_reason | safer_default_replacement_pattern | detection_signal_review_method |
| --- | --- | --- | --- |
| context_free_summary_output | agent skips local corpus and produces generic advice | source_map_first_synthesis | verify every listed local path appears in the generated file |
| unsourced_recommendation_claims | guidance appears authoritative without source boundary | evidence_boundary_split_pattern | check for local, external, and inference labels |
| unverified_agent_instruction | recommendation cannot be checked by command or review gate | verification_gate_coupling | require concrete gate in generated reference |

## Verification Gate Command Set

**Decision supported.** This section helps decide which commands and test layers constitute the verification gate for React reliability claims. The seed supplies only the corpus document verifier while the mapped sources define real React gates, the behavior-first test pyramid with its four layers and named stack, the map's two rg routing commands, and the historical corpus's Parseltongue dependency-graph queries.

**Recommended default and causal basis.** Run the full pyramid on core journeys, behavior tests on changed components, and the rg heading scan before trusting any bundle jump point. The agent file names Vitest or Jest, React Testing Library, MSW, and Playwright as the minimum stack because each layer catches what the previous cannot, pure helpers, component behavior, mocked network boundaries, and end-to-end journeys.

**Operating conditions and assumptions.** The project has the named stack installed or equivalents mapped, and tests target data-testid attributes as both testing sections prescribe. These commands verify React component behavior and bundle navigation, TypeScript compile-level gates belong to the inherited baseline, and corpus document verification stays with the seed command.

**Failure boundary and alternatives.** Gates that only run unit tests certify the layer React breaks least, the pyramid's value concentrates in the integration and journey layers where timing and navigation failures live. Bounded alternatives and recoveries: the corpus's Playwright page-object model for teams scaling E2E suites, heavier setup than inline locators but it keeps selectors in one maintainable place.

**Counterexample, gotchas, and operational comparison.** The map's rg lines reference references/ relative paths that only resolve from the skill root, run elsewhere they return empty and a naive reader concludes the sections are gone. Good: a form change gated by an RTL behavior test plus an MSW integration test. Bad: certifying a mutation flow with only unit tests on its helpers. Borderline: skipping E2E for an internal admin tool, defensible on traffic grounds, the journey layer is still the only gate that sees navigation recovery.

**Verification, evidence, and uncertainty.** Execute the pyramid layers on a changed feature and record which layer each caught defect belongs to. The test pyramid pattern, the map's Section Search block, and the corpus's testing and Parseltongue sections read in full. Whether the 202602 stack recommendation still names the ecosystem defaults is unverifiable without external retrieval.

**Second-order consequence.** The historical corpus's TDD specifications are executable gate definitions in prose, each WHEN-THEN block names an assertion a reviewer can demand before any test framework is even chosen.

**Revision decision.** Import the four-layer pyramid with its stack, the map's rg lines with their working-directory caveat, and the dependency-graph check as the theme's layered gate set.

**Retained seed evidence.** The seed's document verifier command block remains preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`verification_gate_command_set`: Run the repository verifier after editing this file.

```bash
python3 agents-used-monthly-archive/idiomatic-references-202606/tools/verify_reference_generation.py --stage final
```

## Agent Usage Decision Guide

**Decision supported.** This section helps decide what procedure an agent follows when a task requires the React TypeScript bundle. The seed gives four generic bullets while SKILL.md already scripts a five-step agent workflow, decide the client boundary, route through the map, apply the default patterns in order, normalize transport data, and validate with behavior-first tests.

**Recommended default and causal basis.** Have agents execute the five steps literally, logging the boundary decision at step one and the sections opened at step two. The workflow's ordering is load-bearing, boundary decisions constrain which patterns apply, routing prevents full-file context loads, and normalization must precede trust because every downstream pattern assumes UI-shaped data.

**Operating conditions and assumptions.** The task names or implies a component, hook, route, or form surface so step one has a boundary to decide. This guide scripts agent behavior over the React bundle, what the agent does inside destination patterns is governed by those patterns' own rules.

**Failure boundary and alternatives.** An agent that skips step one drags whole trees into the client and then optimizes the wrong architecture with the remaining steps, the workflow degrades worst from the top. Bounded alternatives and recoveries: embedding the routed pattern spans directly in recurring agent prompts, skipping live routing at the cost of freezing the pattern content.

**Counterexample, gotchas, and operational comparison.** Output expectations are part of the contract, an agent that completes all five steps but leaves the tree harder to reason about has failed the skill's own closing test. Good: an agent log showing a server-capable decision, two map-routed sections, and a union-typed diff with rollback. Bad: an agent pasting the full 394-line reference into context for a one-line prop fix. Borderline: skipping step two on the fifth identical form task of a session, efficient, should be logged as a deliberate skip.

**Verification, evidence, and uncertainty.** Reject agent sessions whose logs cannot show the step-one boundary decision and the step-two routing trace. The five-step workflow, reference-use rules, and output expectations read in full from SKILL.md. Whether five steps stay sufficient as the bundle grows more reference files is untested.

**Second-order consequence.** Step three's pattern order, forms, queries, unions, subscriptions, recovery, rollback, is the scoreboard's top rows in application order, the workflow operationalizes the ranking without naming the scores.

**Revision decision.** Restate the guide as the five-step SKILL workflow with the map's three-step use order embedded at step two.

**Retained seed evidence.** The four seed usage bullets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`agent_usage_decision_guide`: Use this reference when a task mentions this theme, one of the listed local source paths, or a nearby technology/workflow surface.

- Start with the local corpus source map.
- Prefer patterns with explicit verification gates.
- Treat external sources as freshness and ecosystem checks, not replacements for local repo conventions.
- Preserve the evidence boundary labels when reusing recommendations.

## User Journey Scenario

**Decision supported.** This section helps decide whether the reader's current moment, building or reviewing, is one this reference serves. The seed describes a generic frontend engineer while the mapped sources serve two sharper moments, a builder holding an unstarted component or form task deciding its state and boundary design, and a reviewer holding a diff deciding whether it survives slow data, bad data, retries, and navigation.

**Recommended default and causal basis.** Enter at the scoreboard when building, enter at the anti-pattern rows when reviewing, and exit with either a pattern shortlist or a verdict. SKILL.md's when-to-use list names both moments explicitly, implementation surfaces first and frontend reviews second, and the bundle's content splits the same way, patterns for builders, anti-patterns for reviewers.

**Operating conditions and assumptions.** The task or diff is scoped to nameable components and boundaries, exploratory prototyping without a reliability requirement defeats the routing. The journey covered runs from task-in-hand to design-decided for builders and diff-in-hand to verdict for reviewers, the coding between those moments belongs to the destination patterns.

**Failure boundary and alternatives.** Arriving mid-debugging misfires, someone chasing a live hydration failure needs the specific recovery or cleanup pattern directly, forcing them through scoreboard routing adds ceremony while the incident burns. Bounded alternatives and recoveries: for learning-oriented visits, the historical corpus's worked examples with TDD specifications teach the same patterns in tutorial form.

**Counterexample, gotchas, and operational comparison.** The builder journey is skippable in a way the reviewer journey is not, nothing blocks a builder who dives straight into JSX, which is why the review moment carries the enforcement weight. Good: a builder spending five minutes here and leaving with unions, query layer, and rollback named for a checkout form. Bad: a responder mid-incident reading the scoreboard top to bottom. Borderline: an agent re-routing on every subtask of one feature, correct per script, wasteful past the first.

**Verification, evidence, and uncertainty.** Ask whether an unstarted task or an unreviewed diff exists, any other moment routes to a destination pattern directly. The when-to-use list and premise check framing both moments, read in full. Median time from task receipt to a correct pattern shortlist has never been measured for this bundle.

**Second-order consequence.** The review journey is the cheaper habit to install, a reviewer armed with sixteen rejection rows improves every contributor's output, while the build journey improves one task at a time.

**Revision decision.** Recast the scenario around the build moment and the review moment, with the anti-pattern rows as the reviewer's entry point.

**Retained seed evidence.** The role, starting state, decision, and trigger lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Role based opening scenario: The frontend product engineer is starting from a user workflow that must become a typed, accessible, resilient interface and needs a reference that turns source evidence into an executable next step.
Primary user starting state: The user has a `react_typescript_reliability_patterns` task, one or more local source paths, and uncertainty about which pattern should drive implementation.
Decision being made: choosing component boundaries, state ownership, loading/error/empty states, and visual verification.
Reference opening trigger: Open this file when the task mentions react typescript reliability patterns, any mapped local source path, or an adjacent workflow with the same failure mode.

## Decision Tradeoff Guide

**Decision supported.** This section helps decide how much client capability, optimism, and memoization each React surface deserves. The seed offers the generic adopt-adapt-avoid rows without this theme's live tensions, client capability versus server simplicity, optimistic speed versus rollback complexity, and memoization gains versus memoization overhead.

**Recommended default and causal basis.** Prefer server-capable code, transactional optimism, and unmemoized simplicity, deviating only at documented boundaries. The sources resolve each tension with a stated default, keep code server-capable unless a leaf needs interactivity, never ship optimistic writes without rollback, and memoize only above the expensive-computation threshold per the corpus's decision matrix.

**Operating conditions and assumptions.** The team can articulate why a component needs client state, why a write needs optimism, or why a computation crosses the expensive threshold, if no reason can be named the default stands. This guide tunes choices within the bundle's patterns, choosing whether the bundle applies at all is the user journey's question.

**Failure boundary and alternatives.** Resolving the tensions by habit instead of by boundary produces the two signature failures, client-everything apps with hydration-scale blast radius, and useCallback-everywhere codebases whose memoization costs exceed their savings. Bounded alternatives and recoveries: uniform strictness regimes, ban optimistic UI outright or memoize everything by lint rule, simpler to audit and defensible in high-churn teams where per-case judgment cannot be trusted.

**Counterexample, gotchas, and operational comparison.** The memoization matrix's none column is its most violated cell, primitive computations and callbacks to unmemoized children gain nothing from wrapping, yet wrapping is the reflex. Good: a dashboard leaving read paths server-rendered and reserving optimism for its one high-frequency mutation. Bad: memoizing a doubled count while raw payloads flow into props. Borderline: optimistic toggles without rollback for idempotent boolean flips, low-stakes, the pattern still demands the rollback story be written.

**Verification, evidence, and uncertainty.** Sample recent components for each axis and check deviations from the defaults carry a named reason. The client-boundary rule, rollback rule, and memoization decision matrix read in full across both sources. The exact computation cost where memoization pays is workload-dependent, the corpus's threshold is a heuristic, not a measurement.

**Second-order consequence.** All three tensions are the same shape, a capability that feels free at adoption time and charges its cost later, the guide's job is moving that deferred cost into the initial decision.

**Revision decision.** Add the three tension axes with their source defaults and the boundary conditions where each default flips.

**Retained seed evidence.** The adopt, adapt, avoid, and cost-of-being-wrong rows remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| decision_option_name | when_to_choose_condition | tradeoff_cost_description | verification_question_prompt |
| --- | --- | --- | --- |
| Adopt when | local corpus and external evidence agree on the react typescript reliability patterns pattern | fastest path, but can copy stale local assumptions | Does the selected pattern appear in the canonical source and current external evidence? |
| Adapt when | local sources are strong but public ecosystem guidance has changed | preserves repo fit, but requires explicit inference notes | Did the reference label the local fact, external fact, and combined inference separately? |
| Avoid when | source evidence is thin, conflicting, or unrelated to the user journey | prevents false confidence, but may require deeper research | Is there a confidence warning or adjacent reference route? |
| Cost of being wrong | wrong react typescript reliability patterns guidance can send an agent to the wrong files, tests, or abstraction | wasted implementation loop and weaker verification | Would a reviewer know what to undo and what to inspect next? |

## Local Corpus Hierarchy

**Decision supported.** This section helps decide which file's word governs when the six mapped paths appear to disagree. The seed assigns canonical, legacy, and supporting roles but misstates the structure, it crowns the claude agent file canonical while labeling SKILL.md legacy, when SKILL.md is the newer 202603 wrapper that operationalizes the same frozen reference text.

**Recommended default and causal basis.** Resolve pattern disputes in the agent file, activation and workflow disputes in SKILL.md, and treat historical-corpus divergences as evolution evidence rather than contradiction. The lineage runs 202601 historical corpus, then 202602 agent file, then 202603 skill packaging that copied the agent file verbatim as its reference, so precedence is temporal for workflow claims, SKILL.md speaks last, and content-identical for pattern claims.

**Operating conditions and assumptions.** All bundle files remain at their archived paths so the lineage comparison stays mechanically checkable. This hierarchy settles precedence among the six mapped paths, precedence between this bundle and the corpus's other React or TypeScript themes belongs to adjacent routing.

**Failure boundary and alternatives.** Reading the copies as supporting detail sources invites circular confirmation, a claim checked against the reference copy has been checked against its own origin. Bounded alternatives and recoveries: treating this corpus's own react and typescript themes as a second-opinion layer above the bundle when the internal hierarchy cannot settle a question.

**Counterexample, gotchas, and operational comparison.** The historical corpus's context-boundary and naming rules are stricter than anything the agent file kept, treating the stricter old rule as current bundle doctrine overstates the 202603 skill's demands. Good: taking SKILL.md's five-step workflow over the agent file's implicit ordering for an activation question. Bad: citing the reference copy to confirm the claude original. Borderline: enforcing the corpus's four-word naming on new hooks, a defensible team choice, not a bundle requirement.

**Verification, evidence, and uncertainty.** Diff the copies at each audit and confirm role claims against file dates and lineage. The diff-confirmed identity and the 202601 to 202603 dating read across all mapped files. Whether the 202603 packaging intended to supersede or merely repackage the 202602 agent file is not documented.

**Second-order consequence.** The historical corpus is the only mapped source that can disagree with the others, the rest are one lineage's self-consistent restatements, so any genuine conflict found in this bundle necessarily involves the 202601 file.

**Revision decision.** Declare pattern content canonical in the 202602 agent file with copies noted, workflow canonical in SKILL.md, navigation canonical in the map, and the historical corpus a distinct-lineage supplement.

**Retained seed evidence.** All six hierarchy rows and the confidence warning remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Classification vocabulary includes canonical, supporting, legacy, duplicate, and conflicting source roles.

| local_source_filepath_value | corpus_hierarchy_role | heading_signal_to_convert | reviewer_question_to_answer |
| --- | --- | --- | --- |
| agents-used-monthly-archive/claude-skills-202602/typescript-react-coder-01.md | canonical primary source | TypeScript React Coder 01; Premise Check; Inherited Baseline | What guidance, warning, or example should this source contribute to React Typescript Reliability Patterns? |
| agents-used-monthly-archive/codex-skills-202603/typescript-react-coder-01/SKILL.md | legacy historical source | TypeScript React Reliability; Overview; When To Use | What guidance, warning, or example should this source contribute to React Typescript Reliability Patterns? |
| agents-used-monthly-archive/codex-skills-202603/typescript-react-coder-01/references/react-reliability-reference.md | supporting detail source | TypeScript React Coder 01; Premise Check; Inherited Baseline | What guidance, warning, or example should this source contribute to React Typescript Reliability Patterns? |
| agents-used-monthly-archive/codex-skills-202603/typescript-react-coder-01/references/reference-map.md | supporting detail source | Reference Map; Jump Points; Section Search | What guidance, warning, or example should this source contribute to React Typescript Reliability Patterns? |
| agents-used-monthly-archive/codex-skills-202603/typescript-react-coder-01/references/typescript-react-coder-01.md | supporting detail source | TypeScript React Coder 01; Premise Check; Inherited Baseline | What guidance, warning, or example should this source contribute to React Typescript Reliability Patterns? |
| agents-used-monthly-archive/idiomatic-references-202602/Idiom-React-Frontend-Patterns.md | legacy historical source | Idiom-React-Frontend-Patterns.md; React Idiomatic Patterns Reference (LLM Context Anchor); Section 1: The Four-Word Naming Convention (React Adaptation) | What guidance, warning, or example should this source contribute to React Typescript Reliability Patterns? |

## Theme Specific Artifact

**Decision supported.** This section helps decide what concrete object a team maintains to make React reliability reviewable per feature. The seed names a component ownership map with state, data boundary, render budget, and tests but gives only generic completion rules, while the mapped sources supply the concrete column set the artifact needs.

**Recommended default and causal basis.** Instantiate the map per feature at design time and update it in the same pull request as any boundary change. Each artifact column maps to a source pattern, the state column records the union type per exhaustive-unions, the data boundary column records the query hook and normalization point per the query-layer and boundary rules, the render budget column records memoization decisions per the matrix, and the tests column records pyramid coverage per the testing pattern.

**Operating conditions and assumptions.** Features have identifiable owning components, atomized design systems where every component is shared need the map at the page level instead. The artifact standardizes per-feature reliability records, it does not replace the dependency-graph constraints, which govern import structure across features.

**Failure boundary and alternatives.** An ownership map without the union-type column degenerates into a file listing, the typed state machine is the thesis and the artifact must capture it or capture nothing. Bounded alternatives and recoveries: colocating the record as a doc comment on the owning component, cheaper to maintain than a central map, at the cost of cross-feature visibility.

**Counterexample, gotchas, and operational comparison.** A stale ownership map misleads more than none, a row claiming rollback coverage that a later diff removed sends reviewers past the exact gap they exist to catch. Good: a checkout row naming its four-state union, two query hooks, one mutation with rollback, and RTL plus E2E coverage. Bad: a spreadsheet of component names with owner initials. Borderline: rows only for high-traffic features, defensible triage, the uncovered features are where reviewers still fly blind.

**Verification, evidence, and uncertainty.** Sample two rows per quarter and check the named union, hooks, and tests still exist in the code. The artifact's column derivation from the four scored patterns read in full. The maintenance cost at which teams abandon ownership maps is unmeasured here.

**Second-order consequence.** The artifact doubles as a review index, a reviewer who reads the row before the diff knows which union must stay exhaustive and which query keys are contractual, converting review from archaeology to verification.

**Revision decision.** Define the artifact as one row per feature component, union type, owning query hooks, normalization site, client-server designation, memoization notes, and test layers present.

**Retained seed evidence.** The artifact field rows with completion rules and evidence hints remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Theme specific artifact: component ownership map with state, data boundary, render budget, and tests.

| artifact_field_name | artifact_completion_rule | evidence_source_hint |
| --- | --- | --- |
| user_goal_statement | state the user's concrete goal before applying React Typescript Reliability Patterns | local corpus hierarchy plus critique findings |
| decision_boundary_rule | define the point where this reference should be used or avoided | decision tradeoff guide |
| verification_gate_rule | define the command, checklist, or review question that proves the artifact worked | verification gate command set |

## Worked Example Set

**Decision supported.** This section helps decide which exercises most efficiently teach this theme's reliability discipline. The seed describes usage abstractly while the mapped sources are dense with runnable examples, the agent file's login form, profile query, and rename-with-rollback snippets, and the historical corpus's full container-presenter, virtualization, and page-object walkthroughs each paired with a TDD specification.

**Recommended default and causal basis.** Train newcomers on the composed walkthrough first, then hand them a failure-mode task, a slow network rename, before certifying them on the bundle. The examples chain into one teachable feature, a schema-validated form submits through a feature-collocated mutation with optimistic rollback, renders through an exhaustive union, and is verified by behavior tests, five scored patterns in one artifact.

**Operating conditions and assumptions.** Training tasks include a real server boundary, MSW-mocked at minimum, examples without transport teach the state half and silently skip the trust half. Worked examples here teach the bundle's reliability patterns, examples of TypeScript language technique live in the companion baseline's material.

**Failure boundary and alternatives.** Examples taught in isolation lose the composition, a learner who can write each snippet separately still wires raw fetch results into boolean flags when assembling a real feature. Bounded alternatives and recoveries: paired implementation, a newcomer builds the feature aloud while a veteran observes, slower than solo walkthroughs but surfaces misconceptions live.

**Counterexample, gotchas, and operational comparison.** The corpus's ❌-marked counterexamples are half its teaching value, walkthroughs that only show correct code never train the rejection reflex the anti-pattern registry needs. Good: a trainee's rename flow that rolls back visibly when MSW injects a 500. Bad: memorizing the twelve pattern names without composing any two. Borderline: practicing only on forms, fluency in the densest pattern cluster, fragility everywhere else.

**Verification, evidence, and uncertainty.** Have the trainee compose the walkthrough solo and check the result against the corpus's TDD specifications. The code snippets and their paired TDD specifications read in full across both sources. How many composed exercises produce durable habit is unmeasured.

**Second-order consequence.** The historical corpus's TDD specifications make each example self-verifying, the WHEN-THEN blocks are the assertions a trainee's reimplementation must pass, turning examples into exercises with built-in grading.

**Revision decision.** Anchor the section on the composed feature walkthrough, form to mutation to union to test, plus one deliberate failure case showing the rollback path firing.

**Retained seed evidence.** The good, bad, and borderline seed lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Good example: Use React Typescript Reliability Patterns after loading the canonical source, confirming the external evidence boundary, and writing a verification gate before implementation.
Bad example: Use React Typescript Reliability Patterns as a generic tutorial while ignoring the mapped local paths, source hierarchy, and cost of being wrong.
Borderline case: Use React Typescript Reliability Patterns only after adding a confidence warning when local evidence is thin or conflicts with current ecosystem guidance.

## Outcome Metrics and Feedback Loops

**Decision supported.** This section helps decide which measurements justify this pattern set's continued emphasis and drive its revision. The seed names a workflow-completion indicator but no loop connects shipped React code back to the pattern set, nothing counts which anti-patterns recur in review, which unions were retrofitted after incidents, or which rollbacks actually fired.

**Recommended default and causal basis.** Classify every review rejection and frontend incident against the registry rows and read the quarterly distribution before adjusting review emphasis. Review rejections, incident retrospectives, and rollback firings are each classifiable against the sixteen anti-pattern rows and twelve patterns, so tallying them shows exactly which disciplines the team has absorbed and which it re-learns per incident.

**Operating conditions and assumptions.** Reviews and retrospectives record enough detail to classify, one-word rejections starve the tally. This loop tunes pattern adoption and review emphasis, runtime product metrics like conversion belong to the product, not this reference.

**Failure boundary and alternatives.** Measuring only delivery speed rewards the deferred-cost failures this theme targets, optimistic UI without rollback demos faster than the transactional version right up to the first conflicted write. Bounded alternatives and recoveries: lint-rule telemetry for the mechanically detectable rows, complete capture for index keys and inline objects, blind to the semantic rows.

**Counterexample, gotchas, and operational comparison.** Falling rejection counts are ambiguous between absorbed discipline and eroding review attention, corroborate with an occasional seeded anti-pattern diff. Good: a quarter showing stored-derived-state rejections falling while union retrofits stay at zero. Bad: declaring the patterns absorbed because velocity rose. Borderline: publishing per-person rejection stats, motivating for some teams, surveillance for others, aggregate by pattern instead.

**Verification, evidence, and uncertainty.** Confirm review and incident records for recent quarters carry registry classifications and that the last review consumed them. The classifiable rejection structure implied by the sixteen anti-pattern rows read in full. Expected rejection base rates for a well-trained team have no baseline yet in this repository.

**Second-order consequence.** Rollback firings are the loop's healthiest signal, each firing is a conflict the transactional design absorbed silently, a rising firing count with flat incident count is the rollback pattern visibly paying rent.

**Revision decision.** Add the tally loop, per-anti-pattern rejection counts from review, per-pattern retrofit counts from incidents, and rollback firing counts from telemetry, reviewed quarterly.

**Retained seed evidence.** The leading indicator, failure signal, and review cadence lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Leading indicator: primary workflow completion improves without introducing layout, accessibility, or state regressions.
Failure signal: the reference lists tools without describing the user workflow and failure states.
Review cadence: Re-run the verifier after every generated-reference edit and refresh external sources when public APIs, docs, or tooling releases change.

## Completeness Checklist

**Decision supported.** This section helps decide what must be confirmed before declaring this reference complete and faithful to its six mapped paths. The seed confirms this document's sections exist but never audits its content against the mapped sources, no item catches a dropped scored pattern, a paraphrased workflow step, or a misstated anti-pattern count.

**Recommended default and causal basis.** Run the count audit, the copy diff, and the score spot-check at every reread and refresh cycle before accepting this document as complete. This theme's correctness is largely transcription correctness, twelve scored patterns, seven agent-file anti-patterns, nine corpus anti-patterns, five workflow steps, five jump points, and five final-synthesis habits, all countable against short sections in minutes.

**Operating conditions and assumptions.** The mapped files remain available at their archived paths for line-level comparison. This checklist audits this reference document's fidelity to its sources, auditing the bundle's internal consistency is the hierarchy and verification sections' job.

**Failure boundary and alternatives.** Count checks miss identity drift, if a future edit changes one reference copy the three-way identity claim silently breaks while every count still passes. Bounded alternatives and recoveries: checksumming all six source files and re-auditing only on checksum change, near-zero steady-state cost, trades away drift detection in this document's own text.

**Counterexample, gotchas, and operational comparison.** Auditing against memory of the files rather than the files themselves recreates the pedigree-free-synthesis failure inside the audit itself. Good: an audit catching that a transcribed anti-pattern list dropped the waitForTimeout row. Bad: passing the audit because all 26 headings exist. Borderline: accepting paraphrased workflow steps, tolerable if the client-boundary-first ordering survives verbatim.

**Verification, evidence, and uncertainty.** Count patterns, anti-patterns, steps, jump points, and habits in this document against the source files and spot-check three scores. The fully countable structure of all four distinct documents read in full. Whether count-plus-identity auditing catches all meaningful drift in pattern guidance is unproven.

**Second-order consequence.** The count audit doubles as a staleness detector, any future bundle revision that adds a thirteenth pattern or sixth workflow step fails this document's counts immediately, flagging the refresh before content drift misleads anyone.

**Revision decision.** Add fidelity items with the exact counts plus an identity item, rerun the copy diff, and a role item spot-checking three pattern scores against the scoreboard.

**Retained seed evidence.** All seven seed checklist bullets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- The role scenario names the user, starting state, decision, and trigger for React Typescript Reliability Patterns.
- The decision guide includes Adopt when, Adapt when, Avoid when, and Cost of being wrong.
- The local corpus hierarchy identifies canonical and supporting sources or gives a confidence warning.
- The theme specific artifact is concrete enough to review without reading every mapped source.
- The examples cover good, bad, and borderline usage.
- The metrics section names one leading indicator and one failure signal.
- The adjacent routing section points to a better reference when this one is not the right fit.

## Adjacent Reference Routing

**Decision supported.** This section helps decide where to send a question that arrived at this theme but is not a React component reliability question. The seed splits the theme name into react, typescript, and reliability tokens, producing self-referential rows, while the real neighbors are the TypeScript baseline this bundle inherits, the frontend design and Three.js themes its own guidance names, and the testing-focused themes for pyramid depth.

**Recommended default and causal basis.** Classify arriving questions as language, canvas, visual design, or component reliability, and keep only the last. The agent file routes explicitly, its inherited-baseline section sends language-level questions to typescript-coder-01, and the seed's own adjacent guidance names React, Three.js, and design references for component logic, canvas behavior, and UI quality.

**Operating conditions and assumptions.** The named destination themes exist in the corpus and cover their assigned question classes. Routing sends away questions this theme cannot close, it does not summarize what the destination themes contain.

**Failure boundary and alternatives.** The commonest misroute arriving here is the language question, how strict should tsconfig be, which this bundle inherits rather than answers, the tell is any question about TypeScript settings rather than React behavior. Bounded alternatives and recoveries: for framework-specific server-component questions no local theme answers, external documentation explicitly labeled unretrieved, never presented as verified.

**Counterexample, gotchas, and operational comparison.** Form questions look like they might route to a dedicated forms theme, none exists in this corpus, schema-validated forms live here and routing them away strands the asker. Good: sending an exactOptionalPropertyTypes question to the TypeScript baseline. Bad: routing to the reliability adjacent reference, a token synonym for this same file. Borderline: keeping a state-management library comparison, answerable here via the subscription pattern, though it strains toward architecture themes.

**Verification, evidence, and uncertainty.** Confirm each named destination exists in the corpus and matches its assigned question class. The inherited-baseline pointer and the seed's own adjacent guidance line read in full. Actual misroute frequency into this theme is estimated, not measured.

**Second-order consequence.** This theme is unusually self-sufficient for testing questions, its pyramid, RTL, MSW, and Playwright coverage means test-strategy questions that would route away from most themes stay home here.

**Revision decision.** Route language and compiler questions to the TypeScript baseline theme, canvas and 3D questions to the Three.js lineage, visual and layout quality to design references, and keep component reliability, state, forms, queries, and frontend testing here.

**Retained seed evidence.** The three seed adjacent-reference lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Adjacent reference guidance: Use React, Three.js, or design references when the task is component logic, canvas behavior, or UI quality.
Adjacent reference 1: consider the react adjacent reference when the current task pivots away from react typescript reliability patterns.
Adjacent reference 2: consider the typescript adjacent reference when the current task pivots away from react typescript reliability patterns.
Adjacent reference 3: consider the reliability adjacent reference when the current task pivots away from react typescript reliability patterns.

## Workload Model

**Decision supported.** This section helps decide how much React reliability work one team can sustain per feature without the discipline decaying. The seed budgets one audience and twelve source documents, an authoring workload, while this theme's operational unit is the feature boundary, one user flow with its viewports, loading, error, and keyboard paths as the seed's own capacity row already hints.

**Recommended default and causal basis.** Scope each unit of work to one feature boundary and budget the pyramid's integration and journey layers as first-class effort, not test overhead. The bundle's patterns each carry a per-feature cost profile, unions and schemas are one-time design costs, query layers amortize across every consumer, rollback logic is per-mutation, and the test pyramid is the recurring cost that scales with journey count.

**Operating conditions and assumptions.** Features decompose into flows with nameable owning components, cross-cutting refactors need their own splitting discipline. This model budgets implementation and review effort for bundle consumers, authoring effort for this corpus document is a separate, rarer workload.

**Failure boundary and alternatives.** The model breaks when one pull request spans several feature boundaries, review attention degrades to skimming and the per-boundary checks, union exhaustiveness, rollback presence, cleanup paths, silently drop. Bounded alternatives and recoveries: pattern-based estimation, costing each scored pattern the feature touches, finer-grained but demands the ownership-map artifact to already exist.

**Counterexample, gotchas, and operational comparison.** Rollback and cleanup work hides inside mutation counts, a feature with five mutations carries five rollback designs the flow-level estimate never surfaced. Good: a checkout flow scoped with its union, two hooks, one rollback, and three test layers named before estimation. Bad: a single PR rewriting state management across four features. Borderline: batching three trivial display components into one review, defensible when none owns state, should be logged as one boundary decision.

**Verification, evidence, and uncertainty.** Track review units per feature boundary in the journal and watch for multi-boundary PR signatures. The seed capacity row and the per-pattern cost structure read across both sources. The boundary count at which review attention measurably decays is judgment, not measured.

**Second-order consequence.** The seed's bounded capacity row, one flow, three viewports, one loading state, one error state, one keyboard path, is secretly a definition of done, work that cannot enumerate those five elements is not yet scoped to a reviewable boundary.

**Revision decision.** Restate capacity in feature-boundary terms, one flow with its union, query hooks, and test layers per review unit, splitting anything larger.

**Retained seed evidence.** The workload dimension rows with boundary values remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`combined_evidence_inference_note`: Treat React Typescript Reliability Patterns as a frontend experience operating reference, not as a prose summary.

| workload_dimension_name | workload_boundary_value | verification_pressure_point |
| --- | --- | --- |
| primary_usage_surface | interface implementation, visual verification, accessibility review, and browser/runtime behavior checks where perceived reliability is user-visible | verify that the reference changes the next implementation or review action |
| bounded_capacity_model | one user flow, three viewport classes, one loading state, one error state, and one keyboard-only path | split the task or create a narrower reference when this boundary is exceeded |
| source_pressure_model | local heading signals include TypeScript React Coder 01; Premise Check; Inherited Baseline; Chosen Thesis; Pattern Scoreboard; Core Patterns; TypeScript React Reliability; Overview | compare guidance against canonical local sources before following external examples |
| artifact_pressure_model | required artifact is component ownership map with state, data boundary, render budget, and tests | require the artifact before claiming the reference is operationally usable |

## Reliability Target

**Decision supported.** This section helps decide what reliability the shipped React surface must demonstrate for this theme's guidance to count as working. The seed measures document properties like label preservation while the shipped UI's own reliability question goes unstated, do core journeys survive slow data, bad data, retries, and navigation, the exact stress list SKILL.md names for reviews.

**Recommended default and causal basis.** Audit the four pattern-derived targets per release and triage any violation to a missing pattern before the next release. The bundle's patterns define measurable targets directly, exhaustive unions imply zero impossible-state renders, rollback patterns imply zero stuck optimistic writes, cleanup patterns imply zero post-unmount state updates, and the pyramid implies journey coverage of every core flow.

**Operating conditions and assumptions.** Production error telemetry exists and console warnings are collected, silent environments make two of the four targets unobservable. Targets here cover React component and journey reliability, transport-layer and backend availability targets belong to their own systems.

**Failure boundary and alternatives.** Targets measured only in test environments miss the timing failures the premise check names, components that only work under ideal timing pass every fast local test and fail on slow networks. Bounded alternatives and recoveries: sampled manual journey walkthroughs under throttled network where telemetry is too sparse to trust.

**Counterexample, gotchas, and operational comparison.** Zero recorded violations over a long window more often means telemetry gaps than perfection, corroborate quiet windows with a seeded failure drill on staging. Good: a release audit finding one mutation without rollback and blocking on it. Bad: declaring the UI reliable because unit coverage is high. Borderline: tolerating a missing keyboard path on an internal tool, a scoped waiver, it should be recorded against the seed's capacity row, not silently dropped.

**Verification, evidence, and uncertainty.** Review the four target audits together at each release checkpoint. The review stress list and the pattern-to-target derivations read in full. This repository's baseline violation rates are unknown until instrumentation begins.

**Second-order consequence.** The four targets are cheap to instrument because the patterns make their violations loud, an inexhaustive union is a compile error, a missing rollback is a greppable mutation without onError, the discipline converts reliability from observation into static structure.

**Revision decision.** Add the operational targets, zero unhandled union states in production error logs, zero optimistic writes without registered rollback, zero can't-perform-state-update warnings, and journey tests for every core flow.

**Retained seed evidence.** All four seed reliability rows with thresholds remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| reliability_target_name | measurable_threshold_value | evidence_collection_method |
| --- | --- | --- |
| source_boundary_preservation | 100 percent of recommendations keep local, external, and inference boundaries visible | review generated text for the three evidence labels before reuse |
| decision_accuracy_sample | at least 18 of 20 sampled uses route to the correct adopt, adapt, avoid, or adjacent-reference decision | sample downstream tasks and record reviewer verdicts |
| unsupported_claim_rate | zero unsupported production, security, latency, or reliability claims in final guidance | reject claims without source row, explicit inference note, or verification method |
| recovery_path_clarity | every avoid or failure case names the rollback, escalation, or next-reference route | inspect failure-mode and adjacent-routing sections together |

## Failure Mode Table

**Decision supported.** This section helps decide which ways this theme's discipline silently fails and how each failure is caught. The seed covers drift and process failures plus two UI rows but not the decay modes specific to this theme's discipline, pattern erosion where new code quietly reverts to boolean flags, copy divergence where the bundle's identical files are edited apart, and baseline drift where the inherited TypeScript rules loosen underneath the React patterns.

**Recommended default and causal basis.** Attach each failure row to its own detection cadence, review tallies quarterly, identity diffs per audit, compiler checks per tsconfig change. Each mode follows from the theme's construction, the patterns demand ongoing discipline nothing enforces, the bundle carries three copies nothing keeps synchronized, and the thesis presumes a companion baseline nothing pins.

**Operating conditions and assumptions.** Someone owns the probes, a failure table without assigned owners is itself the erosion mode it describes. This table catalogs failures of the theme's discipline and bundle integrity, individual code anti-patterns are the registry's subject one level down.

**Failure boundary and alternatives.** All three modes produce healthy-looking codebases at first, boolean-flag state renders fine until the impossible state arrives, diverged copies mislead only the reader who trusted the stale one, and loosened strictness fails at runtime instead of compile time. Bounded alternatives and recoveries: automating the identity diff and compiler check into repository CI, converting the two mechanical modes from probed to enforced.

**Counterexample, gotchas, and operational comparison.** Baseline drift is the stealthiest mode because it lives in another file's settings, a React reviewer never sees the tsconfig diff that turned off the strictness the union patterns depend on. Good: a quarterly tally catching boolean-flag state rising in new components. Bad: praising a quiet quarter no one actually probed. Borderline: a deliberate strictness waiver in one legacy package, tolerable when documented, indistinguishable from drift when not.

**Verification, evidence, and uncertainty.** Confirm each failure row names its probe, owner, and cadence, and that the journal shows the probes ran. The copy identity, inherited-baseline dependency, and discipline-based construction read across the mapped files. Actual onset times for pattern erosion among real teams are unmeasured.

**Second-order consequence.** The three modes decay on different clocks, erosion tracks team churn, divergence tracks bundle edits, and baseline drift tracks tsconfig changes, so one annual review cannot cover them and each needs its own trigger.

**Revision decision.** Add rows for pattern erosion caught by registry-classified review tallies, copy divergence caught by the identity diff at each audit, and baseline drift caught by checking compiler settings against the inherited railguards.

**Retained seed evidence.** All four seed failure rows with mitigations remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| failure_mode_name | likely_trigger_condition | required_mitigation_action |
| --- | --- | --- |
| source drift hides truth | external or local guidance changes after the reference was written | refresh public evidence, rerun local corpus gate, and mark stale claims before reuse |
| generic advice escapes review | agent copies plausible best practices without theme-specific verification | block completion until the verification gate names concrete command, reviewer question, or metric |
| viewport state breaks flow | layout, loading, or error state was not rendered across target viewports | capture screenshots and check text overlap, focus order, and interaction latency |
| client error lacks recovery | network, auth, or hydration failure leaves user stuck | add retry affordance, empty state, and instrumentation event |

## Retry Backpressure Guidance

**Decision supported.** This section helps decide how many recovery attempts a failed UI interaction gets and through which mechanism. The seed covers document-verification retries but not the runtime retry surfaces this theme owns, query retries with invalidation, navigation-aware error recovery instead of dead ends, and abort-then-refetch as the clean cancellation path.

**Recommended default and causal basis.** Route all retries through the query layer's invalidation machinery and give every error state a recovery affordance per the navigation-aware pattern. The bundle's recovery patterns compose into a retry ladder, a failed query invalidates and retries through the query layer, a failed journey recovers through route-level error boundaries with reset flows, and stale in-flight work aborts through controller cleanup rather than racing the retry.

**Operating conditions and assumptions.** Server state flows through query hooks, ad hoc fetches scattered in effects have no invalidation surface for the ladder to use. This section governs UI-level retry and recovery behavior, transport-level backoff policy belongs to the API client, and corpus-process retries stay in the seed bullets.

**Failure boundary and alternatives.** Retries without abort discipline create the race the cleanup pattern exists to prevent, a slow first attempt resolving after its retry overwrites fresh data with stale, the corpus's fetch anti-pattern in retry clothing. Bounded alternatives and recoveries: full-page error boundaries with reload prompts, cruder than granular recovery but bounded and predictable where journey complexity outgrows per-route reset flows.

**Counterexample, gotchas, and operational comparison.** Optimistic mutations complicate retries doubly, the rollback must complete before the retry fires or the retried write races its own compensation. Good: a failed profile save rolling back, offering retry, and succeeding through invalidation. Bad: a hydration error page whose only exit is a hard refresh. Borderline: silent automatic retry on background refetch, invisible when it works, it should still cap and surface after repeated failure.

**Verification, evidence, and uncertainty.** Test each error state's recovery affordance under MSW-injected failures and confirm aborts precede retries in the network log. The navigation-recovery, rollback, and AbortController patterns read in full. The right user-facing retry cap differs by product tolerance and is a local policy choice.

**Second-order consequence.** The recovery pattern reframes errors as state transitions rather than exits, an error state in the union with a retry affordance is backpressure the user operates themselves, no engineering pager required.

**Revision decision.** Add the UI retry ladder, abort in-flight work, retry through query invalidation, recover through route boundaries, capped before the user faces a dead end.

**Retained seed evidence.** All five seed retry and backpressure bullets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- Retry only after the failed verification signal is classified as transient, stale evidence, missing context, or true contradiction.
- Use one bounded retry for stale external evidence refresh, then escalate to a human or a narrower source-specific reference.
- Apply backpressure by stopping new generation or implementation work when source coverage, critique coverage, or verification gates are red.
- For long-running agent workflows, checkpoint after each batch and re-read the current spec before any broad rewrite, commit, push, or destructive operation.
- For distributed execution, assign one owner per generated file or theme batch and require merge-time verification of exact path, heading, and evidence-boundary invariants.

## Observability Checklist

**Decision supported.** This section helps decide what evidence each shipped React surface must produce for the reliability loops to function. The seed logs document-usage evidence and generic viewport captures but not the React-specific signals the patterns make observable, union state distributions, rollback firings, aborted-fetch counts, and post-unmount update warnings.

**Recommended default and causal basis.** Emit the reliability record for core journeys and review it beside the release-time target audit. The discipline's structures are exactly its instrumentation points, every union transition is a loggable event, every rollback handler is a countable firing, every abort is a cancellation record, and every state-update warning is a cleanup defect announcing itself.

**Operating conditions and assumptions.** Record emission stays cheap, sampling union transitions rather than logging every render keeps the habit sustainable. This checklist specifies observability of React reliability behavior, business analytics and backend tracing belong to their own systems.

**Failure boundary and alternatives.** Observability that stops at error counts cannot distinguish the failure modes, a spike of errors reads identically whether unions are missing branches or mutations are stranding optimistic state. Bounded alternatives and recoveries: session-replay tooling for teams that cannot instrument, richer context per failure at much higher cost and privacy weight.

**Counterexample, gotchas, and operational comparison.** Rollback counts without mutation names are unactionable, five firings mean nothing until they concentrate on one endpoint whose conflict rate is the real story. Good: a dashboard showing rollback firings by mutation with one hot spot flagged. Bad: a quarter summarized as no frontend incidents with no telemetry behind it. Borderline: logging only error-state entries and skipping success transitions, compact but erases the base rates the distributions need.

**Verification, evidence, and uncertainty.** Sample recent records and check every field of the minimal schema is present and consistent. The instrumentable structure of unions, rollbacks, and cleanup read across the pattern sources. The sampling rate at which union telemetry stays affordable is workload-dependent.

**Second-order consequence.** The checklist's cheapest item is the highest-signal one, collecting the can't-perform-state-update warning from production consoles turns the cleanup anti-pattern from a code-review judgment into a counted production fact.

**Revision decision.** Define the minimal reliability record, per-journey union transitions sampled, rollback firings counted with mutation names, abort counts, and console warning collection wired to telemetry.

**Retained seed evidence.** All six seed observability bullets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- Record which local sources were loaded and which were intentionally skipped.
- Record the exact verification command, reviewer question, or rendered artifact used as proof.
- Record p50/p95/p99 latency or reviewer-time measurements when the reference affects runtime or workflow speed.
- Capture viewport, browser, console error count, interaction latency, and screenshot evidence.
- Record leading indicator and failure signal from this file in the coverage manifest or journal when the reference drives real work.
- Keep audit evidence small enough to review: command output summary, changed-file list, and unresolved-risk notes are preferred over raw transcript dumps.

## Performance Verification Method

**Decision supported.** This section helps decide how to prove React rendering performance without rewarding wrong-but-fast fixes. The seed demands a latency ceiling and screenshot checks while the sources define the mechanism-level method, the memoization decision matrix, the virtualization benchmark discipline, and subscription-scope checks that explain why latency regresses.

**Recommended default and causal basis.** Profile re-render counts on the changed flow, check list sizes against the virtualization threshold, and audit memo calls against the matrix before accepting a latency measurement. The corpus's virtualization section models the method, it states the mechanism, fifteen DOM nodes versus ten thousand, and the measured consequence, fifty-millisecond renders versus eight-second jank, so performance claims ride on countable structure rather than vibes.

**Operating conditions and assumptions.** Profiling tooling is available in development builds, production-only regressions need the telemetry checklist's records instead. This method verifies React rendering performance, network latency and backend query cost belong to their own verification methods.

**Failure boundary and alternatives.** Verifying only the latency number invites the wrong fix, a slow list gets memoization sprinkled over it when the actual defect is ten thousand mounted DOM nodes no cache can hide. Bounded alternatives and recoveries: periodic timed interaction drills on standard flows instead of continuous profiling, coarser but immune to inconsistent tooling.

**Counterexample, gotchas, and operational comparison.** Averages hide the tail here as everywhere, one whole-store subscription re-rendering on every keystroke disappears into a mean while destroying the typing experience. Good: a list regression traced to node count and fixed by virtualization with before-after render counts. Bad: wrapping every callback in useCallback after one slow interaction report. Borderline: accepting a memo call justified by referential equality for an effect dependency, valid per the matrix, worth a comment naming the row.

**Verification, evidence, and uncertainty.** Inspect re-render and node counts beside the latency numbers before drawing any conclusion. The memoization matrix and the virtualization benchmark figures read in full from the historical corpus. The corpus's benchmark numbers are illustrative magnitudes from its authoring context, not reproducible measurements from this repository.

**Second-order consequence.** The memoization matrix is a verification tool as much as a design tool, any memo call that cannot name its matrix row is unverifiable overhead, and auditing memo usage against the matrix is a performance review that needs no profiler.

**Revision decision.** Measure mechanism first, DOM node counts, re-render counts per interaction, and subscription breadth, then confirm the seed's latency ceiling as the user-facing consequence.

**Retained seed evidence.** The method, indicator, measurement packet, and pass and fail lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Performance method: require interaction latency p95 under 100 ms for local UI actions and no layout overlap across mobile, tablet, and desktop screenshots.
Leading indicator to measure: primary workflow completion improves without introducing layout, accessibility, or state regressions.
Failure signal to watch: the reference lists tools without describing the user workflow and failure states.
Required measurement packet: capture input size, source count, tool-call count, wall-clock time, p50/p95/p99 latency where runtime applies, and reviewer decision time where documentation applies.
Pass condition: the reference must let a reviewer identify the correct next action, verification gate, and stop condition without reading unrelated files.
Fail condition: the reference encourages implementation before the workload, reliability target, and failure-mode table are explicit.

## Scale Boundary Statement

**Decision supported.** This section helps decide at what component-tree size or state breadth this theme's guidance must change shape rather than merely stretch. The seed bounds document scale but not the discipline's scaling seams, context depth capped at two levels, list sizes beyond which rendering must virtualize, and the store-subscription breadth at which state management must restructure.

**Recommended default and causal basis.** Apply the patterns as written within one app's component tree and treat any seam crossing as a design event requiring restructure, not parameter tuning. The sources state the seams directly, the corpus caps context nesting at two levels and splits contexts by change frequency, the virtualization pattern takes over when lists reach thousands of rows, and the subscription pattern demands slice-level access precisely because whole-store reads stop scaling with component count.

**Operating conditions and assumptions.** Growth is observable, someone notices the third context level or the two-thousand-row table and asks whether the current shape still serves. This statement marks where this theme's component-level guidance stops, application architecture beyond the component tree, micro-frontends and state federation, is out of scope.

**Failure boundary and alternatives.** Scaling by growing the existing structures defeats them, a five-level context tree re-renders half the app per change, and a monolithic store subscribed everywhere turns every write into a global render event. Bounded alternatives and recoveries: server-driven pagination instead of client virtualization where the backend can bound the data, removing the seam rather than engineering across it.

**Counterexample, gotchas, and operational comparison.** The seams interact, virtualized lists inside deeply nested context can re-render their visible window on unrelated context changes, hitting two seams at once while each looks individually tolerable. Good: splitting a user context into identity and actions contexts at the second nesting level. Bad: threading one app-wide context through five levels because adding a provider felt heavy. Borderline: virtualizing a three-hundred-row table, below the corpus's dramatic threshold, defensible when rows are expensive to render.

**Verification, evidence, and uncertainty.** Check context depth, list sizes, and subscription breadth at each architecture review against the stated seams. The two-level context rule, virtualization benchmark, and slice-subscription rule read in full. The exact list size where virtualization pays depends on row cost and is an estimate, not a constant.

**Second-order consequence.** All three seams are subscription-breadth problems in different clothes, context, lists, and stores each fail when too many consumers observe too much state, the bundle's minimal-subscription instinct is the general answer wearing three costumes.

**Revision decision.** Add the seams, context past two levels needs splitting by change frequency, lists past the render budget need virtualization, and stores past slice discipline need restructuring or a query layer.

**Retained seed evidence.** All four seed scale-boundary paragraphs remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

React Typescript Reliability Patterns stops being sufficient when the task spans multiple independent systems, more than one ownership boundary, unbounded source discovery, or production traffic without an explicit SLO.
Under distributed execution, split work by theme file and preserve one verification owner per split; do not let parallel agents rewrite the same reference without a merge checkpoint.
Under long-running agent workflows, treat context drift as a reliability failure: checkpoint state, summarize open risks, and verify against the spec before continuing.
Under large-codebase scale, require dependency or source-graph narrowing before applying this reference; a source list without ranked canonical guidance is not enough.

## Future Refresh Search Queries

**Decision supported.** This section helps decide which searches and probes reveal that this theme's patterns or stack claims have gone stale. The seed recycles the theme name while this theme's staleness lives in three specific places, the React and TypeScript releases since the 202602-202603 preparation window, the testing stack's evolution, and the bundle's own upstream lineage.

**Recommended default and causal basis.** Run the release-note probes on a slower cadence than the lineage watch, dating every finding against the 2026 anchors. The theme's claims are pattern claims tied to a frozen authoring moment, the agent file predates whatever React and tooling shipped afterward, so its refresh probes are release-note reads for React, TypeScript, and the four named test tools, plus a watch on the typescript-react-coder lineage for newer bundle revisions.

**Operating conditions and assumptions.** Refresh effort stays bounded, probes are ordered by expected impact so the budget goes to React releases first. These probes refresh this file's pattern and stack claims, refreshing the TypeScript language baseline belongs to the companion theme's own queries.

**Failure boundary and alternatives.** Theme-name searches return this corpus's own files and generic React listicles, neither can reveal that a new React release changed effect timing or that a testing tool deprecated an API the examples use. Bounded alternatives and recoveries: watching the upstream skill archive for a newer typescript-react-coder revision, if the authors ship an updated bundle, diffing it beats re-deriving changes from release notes.

**Counterexample, gotchas, and operational comparison.** Pattern-level guidance ages slower than API surface, a React release rarely invalidates the union or rollback disciplines, so probe findings need triage into pattern-breaking versus example-breaking before any rewrite. Good: a probe finding a test tool renamed an API the login example uses, and the example gains a dated caveat. Bad: logging that the theme-name query returned nothing new. Borderline: probing state-library ecosystems for new entrants, adjacent to the subscription pattern, unbounded if not capped.

**Verification, evidence, and uncertainty.** Record each probe with its date and the specific pattern or example it confirmed or invalidated. The version anchors, 2026-01-30 and the 202602-202603 lineage, read from the mapped files. How fast the React ecosystem invalidates 202602 guidance is unknowable without the fetches these queries queue.

**Second-order consequence.** The bundle's version anchors order its own refresh queue, the historical corpus is dated 2026-01-30 and the skill lineage runs 202602 to 202603, so any query can be scoped since early 2026 and anything older is already absorbed.

**Revision decision.** Replace the name-based trio with targeted probes, React and TypeScript release notes since the preparation window, test-stack changelogs for the four named tools, and a lineage watch for a 202604-or-later bundle revision.

**Retained seed evidence.** The three seed query rows remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| search_query_label_name | search_query_text_value |
| --- | --- |
| `official_docs_query_phrase` | react typescript reliability patterns official documentation best practices |
| `github_repository_query_phrase` | react typescript reliability patterns GitHub repository examples |
| `release_notes_query_phrase` | react typescript reliability patterns changelog release notes migration |

## Evidence Boundary Notes

**Decision supported.** This section helps decide which of this document's statements may travel elsewhere and under what label. The seed defines the three labels but omits this evolution's concrete ledger, four distinct local documents read fully with two byte-identical copies confirmed by diff, zero external URLs retrieved, and every operational policy above marked as inference.

**Recommended default and causal basis.** When reusing a claim from this file, ask first whether the count audit could verify it, citing the source heading if yes and carrying the reasoning along if no. The scored patterns, anti-pattern lists, workflow steps, thesis, and benchmark figures are transcribable local facts with named source headings, while the ownership-map columns, target derivations, retry ladder, tally loop, and scale-seam framings are this evolution's constructed machinery built on those facts.

**Operating conditions and assumptions.** The mapped files stay at their archived paths so fact-class claims remain mechanically re-checkable. These notes govern reuse of this document's claims, the transcribed patterns travel freely with citations, the constructed machinery travels only with its reasoning attached.

**Failure boundary and alternatives.** The highest-risk mislabel here is presenting the corpus's benchmark numbers or the 202602 stack recommendation as current external facts, both are archive-local statements about their authoring moment. Bounded alternatives and recoveries: inline per-claim labels throughout the document if the section-level split proves too coarse for downstream disputes.

**Counterexample, gotchas, and operational comparison.** The copy identity is a local fact with a shelf life, it was true at this session's diff and any later edit to either copy silently invalidates every claim that leaned on it. Good: reusing the twelve-pattern scoreboard with its agent-file heading cited. Bad: citing the quarterly tally cadence as a typescript-react-coder rule. Borderline: reusing the virtualization benchmark magnitudes, sourced but illustrative, the archival context should travel with them.

**Verification, evidence, and uncertainty.** Sample claims from earlier sections and confirm each falls cleanly on one side of the published split. This assignment's read ledger, four distinct documents read in full, one identity diff run, zero retrievals. Readers cannot re-verify the reading itself, only the citations and the rerunnable diff it produced.

**Second-order consequence.** The fact-inference split again follows the countability line, everything the completeness audit can count against the sources is fact, everything it cannot count is this evolution's machinery, one boundary serving both the audit and the label.

**Revision decision.** Publish the split explicitly, patterns, scores, anti-patterns, steps, thesis, and benchmarks are local corpus facts, maps, targets, ladders, loops, and seams are combined-evidence inference.

**Retained seed evidence.** The three labeled boundary definitions remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- `local_corpus_sourced_fact`: statements tied directly to the local source paths above.
- `external_research_sourced_fact`: statements tied to the public URLs above.
- `combined_evidence_inference_note`: synthesis that combines local and public evidence into agent guidance.
