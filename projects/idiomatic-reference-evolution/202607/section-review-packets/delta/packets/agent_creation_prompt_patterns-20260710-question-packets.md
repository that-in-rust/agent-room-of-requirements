## Section 001: Agent Creation Prompt Patterns

### Question 01: What decision does this reference help make?
- **current_section_observation:** The title names a theme but does not yet tell the reader that the operative decision is whether a recurring task deserves a specialized agent and, if so, how its prompt should be bounded.
- **supporting_reason:** Treating agent creation as a decision problem prevents a prompt author from jumping directly to persona prose before defining the user, trigger, authority, outputs, and proof of success.
- **counterargument_or_limit:** Some readers already know they need an agent and only want syntax, so extensive framing can delay a mechanical conversion when requirements are already complete.
- **assumptions_and_boundaries:** This guidance applies to persistent or reusable autonomous roles; a one-off instruction, deterministic script, or user-invoked command may not justify a separate agent.
- **revision_decision:** Expand the title section into an orientation that states the decision, intended reader, required artifact, and explicit non-goals without renaming the heading.
- **additional_insight_to_add:** Agent creation has two coupled design problems, routing and execution, and a prompt can execute well while still being harmful if it activates for the wrong requests.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The bare title supplies no default sequence and leaves readers free to start with an attractive role description or copied template.
- **supporting_reason:** The safest default is charter first, then source hierarchy, positive and negative trigger examples, least-privilege tools, an execution process, and observable verification because each step constrains the next.
- **counterargument_or_limit:** A full charter is excessive for a narrow read-only agent whose trigger, input, and output are already fixed by a mature plugin convention.
- **assumptions_and_boundaries:** The default assumes the agent may act autonomously across several steps and that mistaken activation or excessive authority has a meaningful recovery cost.
- **revision_decision:** State a concise local-first and verification-backed default at the opening, while allowing abbreviated treatment for low-risk, convention-bound agents.
- **additional_insight_to_add:** Prompt length is not the optimization target; the useful target is the smallest instruction set that closes consequential ambiguity about activation, authority, completion, and escalation.

### Question 03: When does the default work well?
- **current_section_observation:** The title does not identify workloads for which a chartered agent prompt creates more value than ordinary instructions.
- **supporting_reason:** The default works well for repeated, multi-step tasks such as reviews, migrations, investigations, or documentation generation where stable triggers and output contracts reduce repeated clarification.
- **counterargument_or_limit:** Repetition alone is insufficient if the work remains highly context-specific and cannot share a stable process or verification contract across invocations.
- **assumptions_and_boundaries:** The task should have a recognizable user intent, bounded inputs, tool capabilities that can be enumerated, and a result that another person or command can inspect.
- **revision_decision:** Add fit criteria that distinguish durable agent responsibilities from transient prompting convenience.
- **additional_insight_to_add:** The strongest candidate tasks have both process regularity and decision locality: the agent can own a coherent outcome without silently inheriting decisions that belong to the parent or user.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** No opening warning distinguishes agent creation from simpler automation or from tasks that require direct human judgment.
- **supporting_reason:** A specialized agent is the wrong choice when the task is a single deterministic action, has no stable trigger boundary, requires unavailable authority, or would hide a consequential approval decision.
- **counterargument_or_limit:** A thin wrapper agent can still improve discoverability around a deterministic tool, provided it does not pretend to add autonomous expertise or bypass confirmation.
- **assumptions_and_boundaries:** Failure includes both poor task execution and routing damage such as frequent false activation, duplicate work, or delegation loops.
- **revision_decision:** Add explicit avoid conditions and route those cases to commands, scripts, skills, project instructions, or human approval.
- **additional_insight_to_add:** The decision should consider reversibility: the less reversible an action, the stronger the case for keeping approval outside the delegated agent even when the analysis itself is delegated.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The title does not position an agent against adjacent mechanisms, leaving the reader without a cost comparison.
- **supporting_reason:** Commands suit explicit deterministic actions, skills suit reusable methods loaded on demand, project instructions suit broad constraints, and agents suit bounded autonomous outcomes with their own context and tools.
- **counterargument_or_limit:** Real systems combine these mechanisms, so a strict one-artifact choice can be artificial; an agent may invoke a skill or tool while obeying project instructions.
- **assumptions_and_boundaries:** The comparison concerns the primary ownership and triggering surface, not a prohibition on composition.
- **revision_decision:** Introduce the alternatives in the opening and defer detailed routing criteria to the adjacent-reference section.
- **additional_insight_to_add:** Choosing an agent moves coordination cost rather than eliminating it: the parent gains context isolation but must define handoff inputs, output compression, failure reporting, and merge responsibility.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** The heading alone gives no early warning about the common tendency to overfocus on persona and underdefine operational constraints.
- **supporting_reason:** The most damaging prompt defects are broad triggers, missing negative cases, excessive tools, ambiguous completion, unbounded retries, and outputs that cannot be checked.
- **counterargument_or_limit:** Highly constrained host runtimes may enforce some of these boundaries externally, reducing how much must be repeated inside the prompt.
- **assumptions_and_boundaries:** The opening should name cross-cutting risks but should not duplicate the later failure-mode registry in full.
- **revision_decision:** Add a short stop-condition warning that makes routing, authority, and verification first-class before the detailed sections.
- **additional_insight_to_add:** A polished system prompt can mask a weak control plane; reviewers should evaluate the trigger description and tool grant independently from the quality of the agent's reasoning instructions.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** There is no immediate example showing what the document will help the reader produce.
- **supporting_reason:** A good case names a migration reviewer with repository-scoped reads and a findings contract; a bad case creates a generic helper with all tools; a borderline case wraps a single validator for discoverability.
- **counterargument_or_limit:** Opening examples can become stale or overly anchor later designs if they are mistaken for mandatory templates.
- **assumptions_and_boundaries:** Examples should illustrate decision quality rather than prescribe product-specific frontmatter that may vary by host.
- **revision_decision:** Add compact good, bad, and borderline signals to the orientation, with full operational examples retained later.
- **additional_insight_to_add:** Borderline cases are best resolved by asking what state the agent uniquely owns; if the answer is only forwarding an argument to one command, a command or skill is usually clearer.

### Question 08: How can the important claims be verified?
- **current_section_observation:** The title section supplies no definition of successful use.
- **supporting_reason:** Claims can be checked through schema validation, positive and negative routing scenarios, tool-denial tests, representative task runs, output-contract checks, and recorded recovery behavior.
- **counterargument_or_limit:** Trigger behavior may be model- and host-dependent, so a small scenario set cannot prove universal reliability.
- **assumptions_and_boundaries:** Verification should match the host system and distinguish static prompt checks from observed behavior over repeated runs.
- **revision_decision:** State that completion requires both artifact validation and behavioral evidence, not merely a syntactically valid Markdown file.
- **additional_insight_to_add:** Negative routing tests are as important as successful task tests because an agent that performs well but activates too broadly imposes hidden cost on unrelated workflows.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The title offers no evidence labels or qualification of the document's recommendations.
- **supporting_reason:** It is well supported by the mapped local corpus that agent files use structured metadata, trigger examples, process guidance, and output expectations; choosing exact boundaries remains contextual judgment.
- **counterargument_or_limit:** Even locally documented conventions can drift, and this evolution pass does not refresh public sources or execute every host behavior described.
- **assumptions_and_boundaries:** Confidence is highest for what the named local files contain and lower for score values, universal thresholds, and claims about current external implementations.
- **revision_decision:** Add an evidence notice that separates mapped facts, retained external pointers, and the document's synthesis.
- **additional_insight_to_add:** Uncertainty should alter action: stale syntax calls for source refresh, uncertain routing calls for scenario tests, and uncertain authority calls for a narrower tool grant.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The heading does not reveal that agent prompts are governance artifacts as much as writing artifacts.
- **supporting_reason:** A reusable prompt allocates decision rights, tool authority, context, and accountability, so design defects compound across every invocation rather than remaining local to one conversation.
- **counterargument_or_limit:** Governance framing can make small internal agents sound more consequential than they are and encourage unnecessary ceremony.
- **assumptions_and_boundaries:** The level of governance should scale with autonomy, action reversibility, data sensitivity, invocation frequency, and ownership complexity.
- **revision_decision:** Frame the reference as a proportional operating guide and make risk-scaled rigor an explicit principle.
- **additional_insight_to_add:** Prompt maintenance belongs to the lifecycle: ownership, telemetry, revision triggers, and retirement criteria should be designed at creation time because unused or stale agents still compete in routing space.

## Section 002: Source Evidence Mapping Table

### Question 01: What decision does this reference help make?
- **current_section_observation:** The table inventories twelve local paths and three public URLs but does not explain how a reader should choose among duplicated snapshots, examples, detailed references, and ecosystem sources.
- **supporting_reason:** A source map should decide retrieval order and evidentiary use, preventing the reader from treating every row as equally current, authoritative, or relevant.
- **counterargument_or_limit:** For a simple lookup, a flat inventory may be faster than a layered selection protocol.
- **assumptions_and_boundaries:** Path existence proves an artifact was mapped, not that its guidance is current, internally consistent, or applicable to the active host.
- **revision_decision:** Preserve all fifteen rows and add an explicit reading protocol, source-state distinctions, and row-level review questions around the table.
- **additional_insight_to_add:** Archive and live copies serve different purposes: the archive preserves provenance while the live path is the candidate operational convention, and divergence between them is itself evidence worth recording.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The existing synthesis role hints at priority but does not state which file to open first or when to stop loading more context.
- **supporting_reason:** Begin with the live skill entrypoint for current local conventions, consult its focused reference files for the disputed dimension, use examples to test artifact shape, and retain the archive snapshot for provenance comparison.
- **counterargument_or_limit:** If the task is historical reconstruction, the archived skill may be the primary source and the live copy merely a later comparator.
- **assumptions_and_boundaries:** The default targets creation or revision of an agent in the current repository rather than auditing how guidance evolved over time.
- **revision_decision:** Add a default retrieval sequence while preserving the table's existing source roles and labels.
- **additional_insight_to_add:** Retrieval should be question-driven: load triggering examples for routing uncertainty, system-prompt design for execution uncertainty, and complete examples only when integration shape remains unclear.

### Question 03: When does the default work well?
- **current_section_observation:** The table is useful when its paths exist, but it gives no conditions under which the local-first sequence is sufficient.
- **supporting_reason:** It works well when the target agent shares the same plugin format and local conventions, and when the live sources agree on frontmatter, triggering, prompt structure, and validation workflow.
- **counterargument_or_limit:** Agreement can reflect copied material rather than independent corroboration because several rows are duplicate archive/live versions of the same documents.
- **assumptions_and_boundaries:** Duplicate paths improve provenance coverage but do not multiply evidentiary confidence as if they were independent sources.
- **revision_decision:** Explain that local convergence establishes repository convention, not broad empirical effectiveness.
- **additional_insight_to_add:** A useful stopping rule is reached when the reader can cite one source for artifact schema, one for the uncertain behavior, and one executable or scenario-based verification method.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The inventory does not warn about missing paths, stale snapshots, format differences across agent hosts, or public links whose current content was not checked in this pass.
- **supporting_reason:** Local-first fails when the target runtime differs from the mapped Claude Code plugin format, the live and archive sources conflict without resolution, or the requested behavior is absent from the corpus.
- **counterargument_or_limit:** Local principles such as clear triggers and least privilege may transfer even when exact syntax does not.
- **assumptions_and_boundaries:** Transferring a principle requires labeling it as synthesis and validating it against the target host rather than copying fields verbatim.
- **revision_decision:** Add failure boundaries and a stop-and-refresh path instead of implying the table is universally sufficient.
- **additional_insight_to_add:** A missing local answer should narrow the claim, not automatically elevate a convenient public example to local policy.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The rows distinguish local and external categories but not primary documentation, implementation repositories, community formats, generated examples, and historical snapshots as competing evidence types.
- **supporting_reason:** Primary local instructions optimize repository fit, public documentation checks host semantics, implementation repositories can clarify behavior, community formats aid portability, and examples expose concrete shape.
- **counterargument_or_limit:** Implementation code and examples are costly to interpret and may encode incidental behavior rather than a supported contract.
- **assumptions_and_boundaries:** Authority depends on the question: syntax, behavior, history, portability, and usability may each have a different best source.
- **revision_decision:** Add a source-type tradeoff guide without changing the mapped URLs or file paths.
- **additional_insight_to_add:** The strongest synthesis is triangular rather than majoritarian: one normative source, one concrete artifact, and one behavioral verification can be more useful than many repetitive documents.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** The table can invite path counting, duplicate-source inflation, blind trust in labels, and unbounded context loading.
- **supporting_reason:** These failures distort confidence and consume attention without answering the active design question.
- **counterargument_or_limit:** A broad initial inventory still has value during discovery because it prevents invisible omissions.
- **assumptions_and_boundaries:** Discovery breadth should be followed by explicit ranking and selective reading before recommendations are formed.
- **revision_decision:** Add review rules for existence, duplication, freshness, scope, contradiction, and relevance.
- **additional_insight_to_add:** Record intentionally skipped sources and the reason; omission becomes auditable, while loading every file ceases to be mistaken for rigor.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** The map provides no worked retrieval decisions.
- **supporting_reason:** A good use opens the live skill, then the triggering guide for a routing question; a bad use cites twelve paths without reading the relevant one; a borderline use relies on archive guidance after live-path divergence.
- **counterargument_or_limit:** File names and heading signals may be enough for early triage, so reading every selected source in full is not always necessary.
- **assumptions_and_boundaries:** Final claims still need direct inspection of the source span that supports them.
- **revision_decision:** Add compact examples of correct source selection and evidence misuse.
- **additional_insight_to_add:** A source map should capture both selected and rejected candidates because rejection rationale helps later maintainers distinguish deliberate scoping from accidental omission.

### Question 08: How can the important claims be verified?
- **current_section_observation:** The table asserts categories and synthesis roles but offers no local existence check, duplicate comparison, or claim-to-source audit.
- **supporting_reason:** Verify local paths exist, compare archive/live hashes, inspect cited headings, and require each factual recommendation to resolve to a row or to an inference label.
- **counterargument_or_limit:** Hash equality proves byte identity, not authority or correctness; heading presence proves discoverability, not support for a nuanced claim.
- **assumptions_and_boundaries:** Content inspection and behavioral tests remain necessary after structural source checks.
- **revision_decision:** Add a small verification procedure and distinguish structural evidence from semantic support.
- **additional_insight_to_add:** Evidence audits should sample the highest-consequence claims first, such as tool permissions, automatic triggers, and destructive actions, rather than treating every sentence as equally risky.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The mapped local paths and URLs are concrete, but their authority labels and present freshness are not established by the table alone.
- **supporting_reason:** The local files can be inspected directly and their headings show relevant agent-development content; the public links remain preserved ecosystem pointers.
- **counterargument_or_limit:** This no-browse evolution pass cannot confirm whether public documentation or repository behavior has changed since the seed was assembled.
- **assumptions_and_boundaries:** Statements about external current behavior must be refreshed later or explicitly presented as retained, unverified pointers.
- **revision_decision:** Add confidence and freshness notes without deleting any source fact from the seed.
- **additional_insight_to_add:** Confidence should be claim-specific rather than source-wide; one document may be authoritative for schema while offering only judgment about ideal prompt length or testing sufficiency.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The map is static and does not expose how evidence changes should propagate into agent prompts and tests.
- **supporting_reason:** A source change can alter schema, routing semantics, tool availability, or recommended process, each of which has a different downstream blast radius.
- **counterargument_or_limit:** Not every textual change is behaviorally relevant, so automatic prompt churn can create noise and regress stable agents.
- **assumptions_and_boundaries:** Refresh decisions should compare semantic claims and affected tests, not merely timestamps or file hashes.
- **revision_decision:** Add maintenance guidance that links source drift to targeted prompt review and regression scenarios.
- **additional_insight_to_add:** Treat the source map as a dependency manifest: when a source changes, rerun only the agent checks tied to claims derived from that source, then broaden if behavior diverges.

## Section 003: Pattern Scoreboard Ranking Table

### Question 01: What decision does this reference help make?
- **current_section_observation:** The scoreboard lists three patterns with numeric scores but does not tell the reader whether the numbers rank implementation order, confidence, effectiveness, or adoption priority.
- **supporting_reason:** The useful decision is which safeguards should be treated as defaults when designing an agent prompt under limited attention.
- **counterargument_or_limit:** A single ranking can obscure task-specific priorities; verification may outrank source mapping when editing a mature, already sourced agent.
- **assumptions_and_boundaries:** The scores are inherited prioritization metadata, not measured probabilities, effect sizes, or universal weights.
- **revision_decision:** Preserve all scores and tiers, define their interpretation, and explain when ordering may change.
- **additional_insight_to_add:** The three patterns form a control chain rather than independent tips: source selection constrains claims, evidence labels constrain certainty, and verification constrains release.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** All three rows are marked default adoption, but the seed does not specify an execution sequence.
- **supporting_reason:** Apply Source Map First, then Evidence Boundary Split, then Verification Gate Coupling because that order moves from inputs to reasoning to observable acceptance.
- **counterargument_or_limit:** Iteration is expected; a failed verification may expose a missing source and send the workflow back to the first step.
- **assumptions_and_boundaries:** The ordering is a default loop, not a one-way waterfall or a requirement to finish all research before drafting any testable hypothesis.
- **revision_decision:** Add an explicit sequence and feedback loop around the existing rows.
- **additional_insight_to_add:** Each pattern should leave an artifact: a ranked source list, claim labels with uncertainty, and a gate matrix, so adherence can be reviewed without reconstructing hidden reasoning.

### Question 03: When does the default work well?
- **current_section_observation:** The scoreboard states adoption tier but omits fit conditions.
- **supporting_reason:** The sequence works well when a prompt combines repository conventions, external host behavior, and design judgment, especially when autonomous actions make unsupported assumptions costly.
- **counterargument_or_limit:** For a purely local formatting update with no behavioral change, a full external evidence pass may add little value.
- **assumptions_and_boundaries:** The depth of each pattern should scale with novelty, autonomy, irreversibility, and source disagreement.
- **revision_decision:** Add proportional application guidance so default adoption does not become maximal ceremony.
- **additional_insight_to_add:** A low-risk task can satisfy the same pattern trio with one canonical source, one explicit inference, and one focused validation command rather than a large dossier.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The table does not describe how the patterns themselves can be misapplied.
- **supporting_reason:** Source mapping fails as context hoarding, evidence labels fail as decorative prefixes, and verification coupling fails when gates check syntax but not routing or task behavior.
- **counterargument_or_limit:** Even imperfect use can expose omissions and improve reviewability compared with no structure.
- **assumptions_and_boundaries:** A pattern counts as applied only when it changes a decision, confidence statement, or release condition.
- **revision_decision:** Add misuse signals and require artifact-level evidence of application.
- **additional_insight_to_add:** Pattern compliance should be outcome-sensitive; a checklist that never blocks release is not a gate, and a label that never narrows a claim is not an evidence boundary.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The scoreboard excludes alternatives such as template-first generation, behavior-first prototyping, and policy-only review.
- **supporting_reason:** Template-first is fast, behavior-first reveals host realities early, and policy-first suits high-risk authority decisions, but each omits one leg of the source-reason-test chain if used alone.
- **counterargument_or_limit:** In mature environments, trusted generators and enforced host policies may already embed source and verification decisions.
- **assumptions_and_boundaries:** Embedded safeguards should be demonstrated rather than presumed from tooling reputation.
- **revision_decision:** Explain that alternatives can reorder or automate the three patterns but should not erase their outcomes.
- **additional_insight_to_add:** The scoreboard is best used as a coverage model, not a recipe monopoly: different workflows are acceptable when they produce equivalent evidence, boundary, and verification artifacts.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Numeric values of 95, 91, and 88 look precise enough to invite false quantitative interpretation.
- **supporting_reason:** Unsupported precision can cause readers to optimize tiny score differences or cite the values as empirical effectiveness.
- **counterargument_or_limit:** Stable numeric ranks can still make sorting and corpus generation deterministic.
- **assumptions_and_boundaries:** The values should be retained as corpus metadata while clearly disclaimed as non-probabilistic and non-comparative outside this reference set.
- **revision_decision:** Add an interpretation note and forbid using the scores as performance evidence.
- **additional_insight_to_add:** When patterns conflict, use consequence and evidence quality rather than arithmetic; a lower-ranked safety gate can dominate a higher-ranked convenience pattern for destructive actions.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** No examples show what adoption of the three ranked patterns changes in an agent file.
- **supporting_reason:** A good design cites local trigger guidance, labels a new negative-trigger rule as inference, and tests both activation and nonactivation; a bad design copies a persona and declares success after parsing.
- **counterargument_or_limit:** Small examples cannot model every host's trigger mechanism or validation tool.
- **assumptions_and_boundaries:** Examples should focus on observable decisions rather than host-specific syntax.
- **revision_decision:** Add a compact three-case comparison showing how each ranked pattern changes the resulting agent artifact and gate.
- **additional_insight_to_add:** A borderline design often has strong source mapping and weak verification; it should remain unreleased or read-only until routing and permission behavior are observed.

### Question 08: How can the important claims be verified?
- **current_section_observation:** The scoreboard's failure-prevention targets are asserted but not connected to evidence that the patterns actually prevented those failures.
- **supporting_reason:** Review the generated artifacts, trace sampled recommendations to sources, inject conflicting evidence, and run positive, negative, and failure-path scenarios against the agent.
- **counterargument_or_limit:** Prevention is counterfactual and cannot be proven from one successful run.
- **assumptions_and_boundaries:** Verification can establish process adherence and detect regressions, while causal effectiveness requires repeated comparative observations.
- **revision_decision:** Define per-pattern gates and avoid claiming measured prevention from the score alone.
- **additional_insight_to_add:** Track near misses, such as a gate catching an overbroad tool request, because they provide stronger evidence of control value than a pass with no challenged condition.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The table confidently labels all rows default adoption without documenting score provenance or observed outcome data.
- **supporting_reason:** The three practices are internally coherent and directly address source, reasoning, and verification failure classes found throughout the seed.
- **counterargument_or_limit:** Their exact ranking and numerical separation remain editorial judgment in this corpus.
- **assumptions_and_boundaries:** Confidence applies to their usefulness as defaults, not to a universal claim that they are always the top three agent-design practices.
- **revision_decision:** Preserve the ranking as inherited metadata and label its epistemic status plainly.
- **additional_insight_to_add:** Later refreshes should adjust scores only with recorded criteria or observations; silent number changes would destroy comparability without improving truth.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The rows are presented independently, hiding interactions and maintenance consequences.
- **supporting_reason:** When all three are applied, agent prompts become traceable decision systems: maintainers know why an instruction exists, what source could invalidate it, and what test should fail if behavior changes.
- **counterargument_or_limit:** Traceability adds maintenance overhead and can become stale if no owner updates the artifacts.
- **assumptions_and_boundaries:** The overhead is justified for reusable agents and should be compressed for ephemeral, low-risk experimentation.
- **revision_decision:** Add a lifecycle deduction that ties each ranked pattern to ownership and refresh triggers.
- **additional_insight_to_add:** The combined pattern enables targeted evolution: source drift identifies affected claims, claim labels identify affected prompt clauses, and gates identify the minimum regression suite.

## Section 004: Idiomatic Thesis Synthesis Statement

### Question 01: What decision does this reference help make?
- **current_section_observation:** The thesis says to load local material, check public guidance, and produce verification-backed decisions, but it does not state which conflicts this sequence resolves or what output constitutes a decision.
- **supporting_reason:** The thesis should guide whether a proposed agent instruction is adopted unchanged, adapted with an inference boundary, rejected, or deferred for evidence.
- **counterargument_or_limit:** A single thesis cannot decide host-specific syntax or every task-level tradeoff without the later tables and examples.
- **assumptions_and_boundaries:** The thesis governs synthesis discipline across the file rather than replacing direct source inspection or behavioral validation.
- **revision_decision:** Expand the three evidence labels into a causal decision rule with explicit outcomes and stop conditions.
- **additional_insight_to_add:** Local fit and external currency answer different questions; agreement raises confidence, while disagreement should produce a narrower instruction and a targeted test rather than a forced consensus.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The seed recommends local first and external second but does not explain why that order is preferable.
- **supporting_reason:** Local sources define repository conventions and expected artifact shape, while public sources can challenge stale assumptions about the host; synthesis then translates both into a testable charter and prompt.
- **counterargument_or_limit:** In a new repository with no established agent conventions, public primary documentation may need to lead.
- **assumptions_and_boundaries:** Local-first is a compatibility default, not a claim that local material is inherently more correct or more current.
- **revision_decision:** Retain the sequence, explain its causal purpose, and state exceptions for absent or contradictory local guidance.
- **additional_insight_to_add:** The final gate should test the combined decision, not each source independently, because a prompt can quote both accurately yet compose them into an unsafe behavior.

### Question 03: When does the default work well?
- **current_section_observation:** The thesis does not identify the conditions under which twelve mapped local paths are a sufficient first retrieval surface.
- **supporting_reason:** It works when the target is a Claude Code plugin agent, the local documents are accessible, and the task concerns the mapped dimensions of frontmatter, triggering, system prompts, examples, or validation.
- **counterargument_or_limit:** The count of twelve includes archive/live counterparts and should not be mistaken for twelve independent confirmations.
- **assumptions_and_boundaries:** The retrieval surface is a starting set whose relevance must be narrowed by the active question.
- **revision_decision:** Add fit conditions and explain that the source count measures inventory, not confidence.
- **additional_insight_to_add:** A source surface becomes operational only after it is converted into a claim ledger that records which prompt clause, trigger rule, or test each selected source informs.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The thesis does not state how to proceed when local guidance is stale, public guidance is unavailable, or the target host differs.
- **supporting_reason:** The default fails if local instructions conflict with actual runtime behavior, external freshness cannot be established for a consequential claim, or the requested agent is outside the mapped platform.
- **counterargument_or_limit:** General prompt-design principles can remain useful across hosts even when exact fields and tools differ.
- **assumptions_and_boundaries:** Cross-host transfer must be labeled as inference and verified against the destination runtime.
- **revision_decision:** Add explicit adapt, avoid, and escalate branches to the thesis.
- **additional_insight_to_add:** When evidence cannot resolve a conflict, reduce authority or switch the agent to advisory mode so uncertainty changes operational risk rather than merely appearing in prose.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The thesis presents one retrieval sequence without contrasting source-only, prototype-first, or policy-first approaches.
- **supporting_reason:** Source-only synthesis maximizes traceability, prototype-first reveals behavior quickly, and policy-first protects high-risk boundaries; the recommended loop combines their strengths.
- **counterargument_or_limit:** Combining all approaches can be slow for a small internal agent.
- **assumptions_and_boundaries:** The depth should be proportional, but every released agent still needs a basis, a bounded inference, and a checkable outcome.
- **revision_decision:** Describe the thesis as a minimum evidence-reason-verification loop that can be implemented with different workflow orders.
- **additional_insight_to_add:** A fast prototype should be treated as evidence about behavior, not as permission to retrofit rationale after deployment.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** The three labels can become formulaic prefixes that create the appearance of rigor without linking claims to sources or tests.
- **supporting_reason:** Decorative labeling does not prevent unsupported recommendations, stale facts, or unsafe synthesis.
- **counterargument_or_limit:** Consistent labels still improve scanning and can prompt reviewers to ask the right questions.
- **assumptions_and_boundaries:** A label is useful only when its scope is clear and its downstream decision changes if the underlying evidence changes.
- **revision_decision:** Add rules for claim-level scope, uncertainty, and action consequences.
- **additional_insight_to_add:** Mixed sentences should be split when facts and inferences have different confidence; otherwise one label can accidentally launder judgment as sourced fact.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** The thesis has no concrete synthesis example.
- **supporting_reason:** A good example ties local trigger format to an inferred negative case and a nonactivation test; a bad example labels a generic recommendation as combined evidence; a borderline example retains an unrefreshed public claim with a warning.
- **counterargument_or_limit:** Example labels can make prose cumbersome if every obvious local fact is repeated mechanically.
- **assumptions_and_boundaries:** Labels should appear where provenance changes a decision, not on every sentence.
- **revision_decision:** Add a concise worked claim showing fact, inference, operational rule, and verification.
- **additional_insight_to_add:** The strongest synthesis example includes a disconfirming condition, making clear what observation would cause the prompt instruction to be revised or removed.

### Question 08: How can the important claims be verified?
- **current_section_observation:** The thesis mentions verification-backed decisions but does not define the verification chain.
- **supporting_reason:** Verify source presence and meaning, inspect the resulting prompt clause, run the relevant routing or execution scenario, and record whether the observation supports or narrows the claim.
- **counterargument_or_limit:** Some design judgments, such as readability, require reviewer assessment rather than a deterministic command.
- **assumptions_and_boundaries:** Judgment-based gates should still name reviewers, criteria, fixtures, and failure consequences.
- **revision_decision:** Add a four-link verification chain and allow both executable and structured review evidence.
- **additional_insight_to_add:** Verification evidence should be attached to the smallest consequential claim so later failures identify what to revisit instead of invalidating the whole document indiscriminately.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The seed confidently reports twelve local source paths and three evidence categories but leaves the synthesis's prescriptive strength unstated.
- **supporting_reason:** The inventory and labels are directly inspectable; local-first compatibility and verification coupling are defensible engineering defaults.
- **counterargument_or_limit:** External freshness, numeric pattern scores, and universal effectiveness remain unverified or judgmental in this pass.
- **assumptions_and_boundaries:** Confidence should be revised when sources diverge, host behavior differs, or repeated agent runs expose routing or execution defects.
- **revision_decision:** Include a confidence paragraph that names both stable facts and unresolved judgments.
- **additional_insight_to_add:** Confidence is multidimensional: a clause can have high source confidence but low behavioral confidence until exercised in the actual agent host.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The thesis ends at synthesis and does not address maintenance after an agent is released.
- **supporting_reason:** Evidence-backed prompts create a maintainable dependency graph in which source, clause, scenario, and owner can be followed during refreshes.
- **counterargument_or_limit:** Maintaining a fine-grained graph manually may cost more than it saves for short-lived agents.
- **assumptions_and_boundaries:** Traceability granularity should scale with lifespan, invocation volume, risk, and number of contributors.
- **revision_decision:** Extend the thesis from creation to lifecycle evolution and retirement.
- **additional_insight_to_add:** An agent should be retired when its trigger space is absorbed by a broader maintained mechanism or its evidence and tests no longer have an owner, even if the prompt still parses.

## Section 005: Local Corpus Source Map

### Question 01: What decision does this reference help make?
- **current_section_observation:** The table lists twelve archive/live artifacts with titles, heading signals, and usage roles, but it does not tell the reader which source answers a particular agent-design question.
- **supporting_reason:** The map should decide which local artifact to inspect for schema, assisted generation, complete examples, system-prompt design, or triggering behavior.
- **counterargument_or_limit:** Heading signals are coarse summaries and may omit relevant details nested deeper in each file.
- **assumptions_and_boundaries:** Selection by heading is triage; any consequential claim still requires reading the relevant source text.
- **revision_decision:** Preserve every row and add a question-to-source routing guide plus a default reading order.
- **additional_insight_to_add:** Treat archive/live pairs as one lineage with two states, not as independent votes; compare them only when history or drift matters.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** Several rows are described as entrypoints, examples, or detail files, but the seed does not establish a retrieval sequence.
- **supporting_reason:** Read the live `SKILL.md` first for the integrated contract, then the single focused reference matching the uncertainty, then one complete example to test whether the guidance yields a coherent artifact.
- **counterargument_or_limit:** A maintainer investigating historical behavior should begin with the archived entrypoint and compare forward.
- **assumptions_and_boundaries:** The live path is preferred for current repository work only after existence and relevant content are confirmed.
- **revision_decision:** Add separate operational and historical reading orders.
- **additional_insight_to_add:** Stop loading sources once schema, disputed behavior, and verification are covered; extra examples can increase anchoring and context cost without adding independent evidence.

### Question 03: When does the default work well?
- **current_section_observation:** The source map assumes that the skill, examples, and references form a coherent local family.
- **supporting_reason:** It works when the integrated skill accurately summarizes its detail files and the examples instantiate the same field rules, trigger conventions, tool restrictions, and prompt structure.
- **counterargument_or_limit:** Examples may contain legacy patterns or illustrative shortcuts that should not override explicit validation rules.
- **assumptions_and_boundaries:** Normative prose outranks examples for contract questions unless the repository explicitly declares the example canonical.
- **revision_decision:** State the conditions for relying on the family and the precedence rule for contradictions.
- **additional_insight_to_add:** Coherence should be tested at artifact boundaries: name syntax, required frontmatter, trigger examples, model selection, tools, process, output, and edge handling.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The map does not discuss broken paths, mismatched versions, copied archive/live content, or a target format outside Claude Code plugins.
- **supporting_reason:** It fails when selected files are absent, archive and live copies diverge without a reason, examples violate current validators, or the host uses different metadata and invocation semantics.
- **counterargument_or_limit:** Conceptual guidance about triggers, responsibilities, and verification can survive exact format differences.
- **assumptions_and_boundaries:** Reuse outside the mapped host must separate transferable principles from incompatible syntax.
- **revision_decision:** Add source-health checks and a clear cross-host boundary.
- **additional_insight_to_add:** When a source family disagrees internally, create the smallest reproducible agent artifact and let the current validator or runtime behavior arbitrate only the disputed contract.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The map provides six artifact types in archive/live form but no tradeoff among concise entrypoints, comprehensive references, generators, and examples.
- **supporting_reason:** Entry points are efficient, references are precise, generation prompts accelerate drafting, and complete examples expose integration and edge cases.
- **counterargument_or_limit:** Generation templates and examples can perpetuate outdated defaults or encourage copying irrelevant persona and tool choices.
- **assumptions_and_boundaries:** Use templates as scaffolds and validate every copied field against the current task charter.
- **revision_decision:** Add a source-type selection matrix keyed by question and misuse risk.
- **additional_insight_to_add:** The more concrete a source is, the stronger its anchoring effect; reviewers should deliberately return to the task charter after reading examples to prevent template-shaped requirements.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Duplicate rows can inflate apparent coverage, heading snippets can be mistaken for full claims, and the canonical/supporting roles are not visible in this specific table.
- **supporting_reason:** These errors lead to false confidence, excessive context, and accidental elevation of historical examples over current rules.
- **counterargument_or_limit:** Redundancy helps preserve provenance and supports drift checks when handled explicitly.
- **assumptions_and_boundaries:** Every retrieval note should identify path state, selected span, question answered, and whether another row is a duplicate lineage.
- **revision_decision:** Add deduplication and claim-citation guidance beside the map.
- **additional_insight_to_add:** Record the reason a source was loaded before reading it; this reduces post hoc rationalization in which any discovered passage is treated as relevant evidence.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** The map itself contains no example of navigating the six source types.
- **supporting_reason:** A good routing investigation reads `SKILL.md` and `triggering-examples.md`; a bad investigation copies `complete-agent-examples.md` wholesale; a borderline one uses the generation prompt without revalidating tool permissions.
- **counterargument_or_limit:** Complete examples can be the fastest starting point when the target closely matches and all fields are reviewed.
- **assumptions_and_boundaries:** Similarity in task name does not establish similarity in authority, risk, input scope, or completion contract.
- **revision_decision:** Add source-selection examples tied to concrete uncertainties.
- **additional_insight_to_add:** The best example review asks what was intentionally omitted from the template, since missing negative triggers or recovery rules often matter more than visible formatting.

### Question 08: How can the important claims be verified?
- **current_section_observation:** The table's title and heading signals can be verified structurally, but its usage roles require semantic review.
- **supporting_reason:** Check each path, inspect the cited headings, compare archive/live bytes or relevant spans, and map extracted rules to validator checks or scenario tests.
- **counterargument_or_limit:** A valid file and matching heading still do not prove that the example is recommended or current.
- **assumptions_and_boundaries:** Verification must distinguish inventory accuracy, normative authority, and behavioral effectiveness.
- **revision_decision:** Add a three-level audit that separates path integrity, normative source authority, and observed target-host behavior.
- **additional_insight_to_add:** When archive/live content is identical, document one semantic read and one identity check rather than pretending to perform two independent reviews.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The paths and displayed headings are concrete local facts; the optimal reading order and relative authority are partly inferred.
- **supporting_reason:** The integrated skill explicitly points readers to the detail and example files, supporting their use as a coherent source family.
- **counterargument_or_limit:** Local documentation can contain unsupported claims such as universal length guidance or production-readiness language that should not be inherited automatically.
- **assumptions_and_boundaries:** Factual extraction is high confidence; prescriptions need cross-checking against current validators, project needs, and observed runs.
- **revision_decision:** Keep source facts intact while labeling the routing protocol as bounded synthesis.
- **additional_insight_to_add:** Confidence can differ within one row: its title and headings may be certain, its role plausible, and the effectiveness of its recommendations unmeasured.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The map is organized by file rather than by the agent lifecycle decisions those files influence.
- **supporting_reason:** Reorganizing mentally by lifecycle reveals coverage gaps across discovery, trigger design, execution design, validation, operation, and retirement.
- **counterargument_or_limit:** Adding another physical table could duplicate the existing inventory and make maintenance harder.
- **assumptions_and_boundaries:** A concise lifecycle routing layer can reference existing rows without repeating every path.
- **revision_decision:** Add a lifecycle coverage interpretation after the table instead of restructuring or renaming it.
- **additional_insight_to_add:** The current corpus is strong on creation and triggering but thinner on deployed-agent telemetry and retirement, so this evolved reference must supply bounded operational guidance as synthesis.

## Section 006: External Research Source Map

### Question 01: What decision does this reference help make?
- **current_section_observation:** The map names an OpenAI guide, the AGENTS.md community format, and the Codex repository, but it does not specify which external question each source can resolve.
- **supporting_reason:** External sources should decide whether local assumptions remain compatible with public host guidance, ecosystem conventions, and implementation behavior.
- **counterargument_or_limit:** These sources concern project instructions and Codex more broadly and may not directly specify Claude Code plugin agent frontmatter.
- **assumptions_and_boundaries:** They are analogues and freshness checks, not automatic replacements for the local agent-development corpus.
- **revision_decision:** Preserve all URLs and make their comparative, non-substitutive role explicit.
- **additional_insight_to_add:** External relevance is claim-specific: project instruction loading can inform context hierarchy without proving a particular agent description schema.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The table calls one source primary guidance and the others community or implementation analogues but lacks a use sequence.
- **supporting_reason:** Consult official documentation for supported semantics, use the public repository to clarify implementation or examples when needed, and use community format material for portability context.
- **counterargument_or_limit:** Repository behavior may lead released documentation, and community conventions can reveal interoperability concerns omitted from one vendor's docs.
- **assumptions_and_boundaries:** Documentation remains normative when it clearly states a supported contract; implementation inspection should be labeled if it reveals incidental behavior.
- **revision_decision:** Add a default authority order with an explicit contradiction protocol.
- **additional_insight_to_add:** A contradiction should be recorded with observation date and target version because external evidence decays faster than local design rationale.

### Question 03: When does the default work well?
- **current_section_observation:** The map is most useful as a check against insular local assumptions, but the seed does not say when that check changes a prompt.
- **supporting_reason:** It works when the agent depends on project instruction discovery, repository context loading, or conventions intended to interoperate across agent-capable tools.
- **counterargument_or_limit:** For local-only plugin metadata, external AGENTS.md sources may be adjacent rather than directly controlling.
- **assumptions_and_boundaries:** External material should affect only clauses within its demonstrated scope.
- **revision_decision:** Add fit conditions and prevent broad extrapolation from adjacent documentation.
- **additional_insight_to_add:** Public ecosystem checks are especially valuable for negative space, revealing assumptions the local corpus never states because its original authors treated them as implicit.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The seed does not warn that public content may change, become unavailable, or describe a different product surface.
- **supporting_reason:** External lookup fails as evidence when freshness is unknown, version context is missing, or an analogue is presented as direct support for incompatible syntax.
- **counterargument_or_limit:** Even stale public sources may retain historical value if labeled and compared against the target version.
- **assumptions_and_boundaries:** This pass explicitly performs no browsing, so the URLs cannot support newly asserted current-state facts.
- **revision_decision:** Add a no-browse freshness warning and a later refresh procedure.
- **additional_insight_to_add:** If freshness cannot be established, preserve the source as a search target while downgrading operational claims to local evidence plus inference.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The map omits release notes, schemas, runtime help, and controlled experiments as alternative external evidence.
- **supporting_reason:** Release notes establish change chronology, schemas define accepted structure, runtime help reflects installed behavior, and experiments expose actual routing or loading outcomes.
- **counterargument_or_limit:** Runtime experiments can be nondeterministic and version-specific, while implementation reading can be expensive.
- **assumptions_and_boundaries:** Select the cheapest source capable of resolving the consequential uncertainty, then corroborate high-risk behavior.
- **revision_decision:** Add alternative evidence types without inventing new current citations.
- **additional_insight_to_add:** Installed-runtime behavior may be more operationally relevant than the newest web documentation when a repository is pinned to an older version.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Named public URLs can create citation theater, false freshness, vendor-format conflation, and excessive research unrelated to the prompt decision.
- **supporting_reason:** These failures make the reference appear authoritative while weakening local compatibility and delaying implementation.
- **counterargument_or_limit:** Public links improve auditability and provide clear refresh entrypoints even when not opened during this pass.
- **assumptions_and_boundaries:** Each external source should have a stated question, observation date when refreshed, and bounded claim scope.
- **revision_decision:** Add external-evidence hygiene rules around the table.
- **additional_insight_to_add:** Research should stop when the unresolved uncertainty no longer changes the agent's trigger, authority, process, output, or release gate.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** The table lacks examples of proper and improper use of public analogues.
- **supporting_reason:** A good use checks official instruction precedence before defining context loading; a bad use cites the Codex repository for Claude-specific frontmatter; a borderline use adopts a community convention with an explicit compatibility test.
- **counterargument_or_limit:** Cross-ecosystem borrowing can be productive when treated as design inspiration rather than sourced compatibility.
- **assumptions_and_boundaries:** Inspiration must be labeled as inference and validated in the target host.
- **revision_decision:** Add claim-scoping examples that distinguish legitimate external analogy from unsupported cross-product syntax transfer.
- **additional_insight_to_add:** A borderline external pattern should first be trialed in read-only or advisory mode, reducing the cost of an incorrect compatibility assumption.

### Question 08: How can the important claims be verified?
- **current_section_observation:** The map contains no date, version, excerpt, or behavioral check for any public source.
- **supporting_reason:** A future refresh should record access date, target version, direct supporting passage or implementation location, and a local scenario that exercises the adopted behavior.
- **counterargument_or_limit:** Exact excerpts can become stale and may create maintenance burden or copyright concerns if copied extensively.
- **assumptions_and_boundaries:** Store concise paraphrases and precise links or versions rather than long quotations.
- **revision_decision:** Add a minimal external evidence record and state that current freshness is unverified here.
- **additional_insight_to_add:** Verification should include a mismatch path: define what local prompt clause and test are rolled back if the external behavior is absent in the installed host.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** It is certain that the seed maps three URLs with stated roles; their current contents and direct applicability were not checked in this no-browse pass.
- **supporting_reason:** Retaining the URLs preserves provenance and gives later maintainers authoritative starting points for refresh.
- **counterargument_or_limit:** A preserved URL can move, redirect, or cease to support the original role.
- **assumptions_and_boundaries:** No new factual claim about present external behavior should be derived solely from these retained entries.
- **revision_decision:** State the confidence boundary prominently and avoid language implying current confirmation.
- **additional_insight_to_add:** The map should distinguish source identity confidence from content freshness confidence so a stable URL is not confused with stable guidance.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The external map is treated as a static supplement rather than a controlled dependency with refresh cost.
- **supporting_reason:** External claims can change independently of the repository, causing silent prompt drift if they are not versioned or covered by behavior tests.
- **counterargument_or_limit:** Over-versioning every conceptual recommendation would make the reference brittle and noisy.
- **assumptions_and_boundaries:** Version tracking is most important for syntax, precedence, tool capability, security, and activation behavior, not timeless writing principles.
- **revision_decision:** Add risk-based refresh triggers and claim-level dependency guidance.
- **additional_insight_to_add:** Prefer local tests that encode required behavior over prose that merely mirrors external wording; tests expose when the installed system no longer satisfies the adopted contract.

## Section 007: Anti Pattern Registry Table

### Question 01: What decision does this reference help make?
- **current_section_observation:** The registry names three failure patterns, causes, replacements, and detection methods, but it does not tell a reviewer when a defect is severe enough to block an agent prompt.
- **supporting_reason:** The registry should decide whether a draft can proceed, needs bounded adaptation, or must stop because its claims, context, or verification are not reviewable.
- **counterargument_or_limit:** Treating every registry hit as a blocker could reject harmless exploratory drafts before they are ready for release review.
- **assumptions_and_boundaries:** Blocking applies to a prompt claimed ready for reuse; exploratory material may retain defects if it is clearly marked non-operational and lacks dangerous authority.
- **revision_decision:** Preserve the three rows, add severity and release consequences, and distinguish drafting warnings from completion blockers.
- **additional_insight_to_add:** A defect's severity depends on actionability: an unsourced style preference is lower risk than an unsourced instruction that broadens tools or authorizes destructive work.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** Each row provides a safer replacement but no common remediation order.
- **supporting_reason:** First identify the concrete unsupported or context-free decision, then load the smallest relevant source, label the resulting fact or inference, and attach a gate that can fail before release.
- **counterargument_or_limit:** Some generic prose should simply be deleted rather than researched and validated.
- **assumptions_and_boundaries:** Remediation effort should be reserved for statements that materially affect routing, authority, execution, output, or lifecycle.
- **revision_decision:** Add a triage-remediate-verify sequence and make deletion an explicit option.
- **additional_insight_to_add:** The safest replacement is not always more text; removing a vague autonomous instruction can reduce risk more effectively than surrounding it with caveats.

### Question 03: When does the default work well?
- **current_section_observation:** The seed assumes that source mapping, evidence labels, and concrete gates address the named failures.
- **supporting_reason:** They work when the agent's task has inspectable local conventions and observable routing or execution outcomes.
- **counterargument_or_limit:** Evidence and gates cannot make an inherently ambiguous responsibility stable without user or owner decisions.
- **assumptions_and_boundaries:** Requirements ambiguity must be resolved or bounded before anti-pattern remediation can succeed.
- **revision_decision:** Add fit conditions and an escalation path for unresolved ownership or success criteria.
- **additional_insight_to_add:** Anti-pattern remediation should be tested with adversarial examples, not only the happy path that originally motivated the agent.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The registry does not describe false positives, such as concise advice that is obvious from a stable local contract or an instruction verified by host policy outside the prompt.
- **supporting_reason:** A review rule becomes counterproductive if it demands redundant citations or duplicate gates for behavior already enforced and auditable elsewhere.
- **counterargument_or_limit:** External enforcement is often assumed rather than demonstrated, so exemptions can reopen the original failure.
- **assumptions_and_boundaries:** An exemption requires a named enforcing component, current evidence, and a failure path visible to reviewers.
- **revision_decision:** Add bounded exceptions while retaining strict release defaults.
- **additional_insight_to_add:** When a host policy supplies the gate, the prompt should reference the policy boundary rather than restate implementation details that can drift.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The registry presents one safer replacement per failure and omits alternatives such as narrower scope, human approval, read-only mode, or removal.
- **supporting_reason:** Narrowing scope reduces evidence needs, approval preserves human decision rights, read-only mode limits consequences, and removal avoids unsupported complexity.
- **counterargument_or_limit:** These alternatives reduce autonomy or capability and may weaken the original productivity goal.
- **assumptions_and_boundaries:** Capability should only be restored after evidence and verification justify the added risk.
- **revision_decision:** Add mitigation alternatives and state their autonomy tradeoffs.
- **additional_insight_to_add:** Progressive authority is a useful remediation pattern: prove routing and analysis first, then add writing or execution tools behind stronger gates.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** The registry covers generic advice, unsourced claims, and unverifiable instructions but omits overlapping triggers, privilege excess, contradictory steps, delegation loops, and missing stop conditions.
- **supporting_reason:** These defects can cause operational harm even when every recommendation is sourced and a syntax verifier passes.
- **counterargument_or_limit:** Later failure-mode sections already cover several operational risks, so duplication should be controlled.
- **assumptions_and_boundaries:** This table should remain a compact prompt-review registry and route detailed runtime failures to the later section.
- **revision_decision:** Expand detection coverage selectively and cross-reference operational failure analysis.
- **additional_insight_to_add:** Review for composition failures: individually reasonable instructions can conflict, such as “act autonomously” paired with “ask whenever uncertain,” creating unstable behavior.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** Rows describe abstract failure names but show no prompt snippets or reviewer decisions.
- **supporting_reason:** A good clause names the target files and pass gate; a bad clause says to improve quality using all available tools; a borderline clause is precise but relies on an unverified external capability.
- **counterargument_or_limit:** Snippets can oversimplify defects whose impact emerges only from the whole prompt and host configuration.
- **assumptions_and_boundaries:** Review examples should be followed by a whole-artifact consistency check.
- **revision_decision:** Add concise examples and emphasize prompt-level reconciliation.
- **additional_insight_to_add:** A borderline clause should include a feature-detection or fallback rule so uncertainty becomes executable behavior rather than a passive warning.

### Question 08: How can the important claims be verified?
- **current_section_observation:** Detection methods currently ask whether paths, labels, and gates are present, which can be satisfied mechanically without semantic quality.
- **supporting_reason:** Verification should trace a sampled instruction to evidence, show what observation can fail it, and execute at least one counterexample or denied-capability path.
- **counterargument_or_limit:** Full behavioral testing for every prompt sentence is infeasible and can create brittle tests.
- **assumptions_and_boundaries:** Prioritize high-consequence clauses and representative classes of behavior.
- **revision_decision:** Strengthen each detection rule from presence to semantic adequacy.
- **additional_insight_to_add:** Mutation testing is useful conceptually: remove a trigger boundary or broaden a tool grant and confirm that review or scenarios detect the degradation.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The three anti-patterns clearly represent review risks, but their frequency and relative impact are not measured in the seed.
- **supporting_reason:** Their causal mechanisms are understandable and align with the document's evidence and verification thesis.
- **counterargument_or_limit:** Calling them the most important failures across all agent systems would exceed available evidence.
- **assumptions_and_boundaries:** Treat them as high-value local review defaults, not an exhaustive or empirically ranked taxonomy.
- **revision_decision:** Preserve them, qualify scope, and add operational categories without unsupported prevalence claims.
- **additional_insight_to_add:** Record which registry rules actually catch defects during maintenance; this turns a static list into locally grounded evidence over time.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The registry focuses on preventing a bad generated reference, not on how anti-patterns propagate through copied agents.
- **supporting_reason:** Reusable templates amplify both good controls and subtle defects, so one broad trigger or unverifiable completion rule can spread across many agents.
- **counterargument_or_limit:** Central templates also make remediation efficient once a defect is found.
- **assumptions_and_boundaries:** Shared template ownership and downstream inventory must be visible for propagation control.
- **revision_decision:** Add template-level blast-radius review and regression guidance.
- **additional_insight_to_add:** Anti-pattern registries should include provenance and retirement rules; obsolete warnings create noise that can train reviewers to ignore current ones.

## Section 008: Verification Gate Command Set

### Question 01: What decision does this reference help make?
- **current_section_observation:** The section supplies one repository verifier command but does not state what that command proves or whether it validates the agent prompt itself.
- **supporting_reason:** The section should decide whether structural generation checks, prompt schema checks, routing scenarios, and representative task tests have supplied enough evidence to release the artifact.
- **counterargument_or_limit:** A single canonical verifier can remain the correct final entrypoint if it orchestrates all lower-level checks.
- **assumptions_and_boundaries:** The named archive verifier's actual coverage must be inspected or its result described narrowly; command presence alone does not establish behavioral validation.
- **revision_decision:** Preserve the command, define its bounded role, and add a layered gate matrix around it.
- **additional_insight_to_add:** Every gate needs an owner and a failure consequence; an unowned command that can fail without blocking release is monitoring, not verification.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The seed says to run the verifier after editing, with no preconditions or follow-up checks.
- **supporting_reason:** Run fast static checks first, then the repository verifier, then positive and negative trigger scenarios, a representative execution, and a final permission and output audit.
- **counterargument_or_limit:** Running behavioral scenarios may be impossible in offline documentation-only environments.
- **assumptions_and_boundaries:** When runtime tests are unavailable, the artifact should be labeled structurally verified and behaviorally unverified rather than fully validated.
- **revision_decision:** Add a default ordered gate sequence and honest partial-verification status.
- **additional_insight_to_add:** Gates should be fail-fast by cost: schema and placeholder checks precede model runs, while high-cost repeated scenarios run only after static defects are resolved.

### Question 03: When does the default work well?
- **current_section_observation:** The command works as a repository-level check when the expected tool and corpus layout exist.
- **supporting_reason:** Layered verification works well for reusable agents whose metadata can be parsed and whose routing, tools, process, and output can be exercised with stable fixtures.
- **counterargument_or_limit:** Model nondeterminism and host updates can make behavioral outcomes variable even with unchanged prompts.
- **assumptions_and_boundaries:** Scenario assertions should focus on invariant decisions and safety boundaries rather than exact prose.
- **revision_decision:** Add fit criteria for deterministic and probabilistic gates.
- **additional_insight_to_add:** Repeated behavioral sampling should target uncertain boundaries, while one run may suffice for deterministic schema and tool-denial checks.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The section does not address missing verifier scripts, obsolete flags, global corpus failures unrelated to the changed prompt, or commands that mutate state.
- **supporting_reason:** A gate is unusable if it cannot be reproduced, scopes failures ambiguously, or changes the repository while purportedly validating it.
- **counterargument_or_limit:** A broad verifier can intentionally expose integration regressions outside the edited file.
- **assumptions_and_boundaries:** Focused checks should isolate the artifact first, followed by broad checks whose unrelated failures are reported separately.
- **revision_decision:** Add command preflight, scope, side-effect, and failure-classification guidance.
- **additional_insight_to_add:** Preserve exact command output summaries and exit codes, but avoid raw transcript dumps that hide the decisive failure among noise.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** No alternatives are named for environments where the repository verifier is unavailable or insufficient.
- **supporting_reason:** Alternatives include schema parsers, lint rules, fixture comparisons, host-level dry runs, snapshot tests, reviewer checklists, and production canaries.
- **counterargument_or_limit:** Manual checklists are flexible but less reproducible; snapshots are reproducible but can approve semantically poor output.
- **assumptions_and_boundaries:** Combine deterministic structure checks with behavior-oriented review rather than relying on one evidence type.
- **revision_decision:** Add an alternative gate table with what each method can and cannot establish.
- **additional_insight_to_add:** Use canaries only after local safety gates pass and limit them to reversible, low-authority actions because production observation is not a substitute for pre-release control.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** The seed risks equating a passing generation verifier with prompt correctness.
- **supporting_reason:** Structural pass, stale fixtures, overfit examples, skipped negative cases, nonzero warnings, and ignored exit codes can all produce false assurance.
- **counterargument_or_limit:** Structural verification still catches valuable defects and should not be dismissed because it is incomplete.
- **assumptions_and_boundaries:** Every reported pass should name the layer and coverage it represents.
- **revision_decision:** Add false-pass signals and require layered status language.
- **additional_insight_to_add:** A verification report should expose untested claims explicitly; absence of a failed check is not evidence for behavior no check exercised.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** Only a command example is present, with no result interpretation.
- **supporting_reason:** A good run records command, scope, exit status, routing fixtures, and residual uncertainty; a bad run says “tests pass” after one parser check; a borderline run passes locally but lacks host access.
- **counterargument_or_limit:** Detailed evidence records can overwhelm small changes if not summarized.
- **assumptions_and_boundaries:** Keep a concise outcome ledger with links or paths to durable artifacts when available.
- **revision_decision:** Add pass, fail, and partial-verification records that state scope, evidence, and resulting authority.
- **additional_insight_to_add:** Partial verification should narrow deployment, such as read-only use or manual invocation, until the missing host-level behavior is tested.

### Question 08: How can the important claims be verified?
- **current_section_observation:** The section itself needs verification that the named command exists, runs from the stated directory, and covers the intended stage.
- **supporting_reason:** Preflight the path and help output, run the command, capture exit status, inspect reported checks, and independently test any critical behavior outside its coverage.
- **counterargument_or_limit:** Inspecting the verifier implementation may be unnecessary when its documented contract and machine-readable report are clear.
- **assumptions_and_boundaries:** High-consequence release decisions justify checking verifier coverage at least once per tool version.
- **revision_decision:** Add a verifier audit covering command availability, implemented checks, exit semantics, and shared-gate regressions.
- **additional_insight_to_add:** Gate changes should themselves receive regression tests because weakening a shared verifier can silently approve every downstream agent.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The exact command is a seed fact, while its current executability and semantic coverage have not yet been established by this section.
- **supporting_reason:** Retaining it preserves the repository's declared final-stage verification entrypoint.
- **counterargument_or_limit:** The path points into an archived tool directory, which may be intentional provenance or may become operationally stale.
- **assumptions_and_boundaries:** Any completion claim must report actual current execution evidence and distinguish focused from repository-wide failures.
- **revision_decision:** Preserve the command and qualify all claims until run evidence is available.
- **additional_insight_to_add:** Tool location is part of the contract; an archived verifier used operationally should have an owner or a documented immutability expectation.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** Verification is framed as a terminal action rather than a design input.
- **supporting_reason:** Defining gates before writing the prompt forces triggers, outputs, permissions, and stop conditions into observable forms.
- **counterargument_or_limit:** Some exploratory agent behaviors are learned only through prototypes, so gates may evolve during design.
- **assumptions_and_boundaries:** Evolving gates is acceptable when changed expectations are recorded and not silently fitted to one successful output.
- **revision_decision:** Reframe verification as contract design and preserve a final independent reread.
- **additional_insight_to_add:** A prompt clause that cannot be verified should be rewritten as a bounded heuristic with escalation, or removed if it controls consequential action.

## Section 009: Agent Usage Decision Guide

### Question 01: What decision does this reference help make?
- **current_section_observation:** The guide says when to open the reference and gives four broad bullets, but it does not walk from a user request to a decision to create, adapt, or reject an agent.
- **supporting_reason:** The guide should determine whether the theme applies, what minimum context to load, what artifact to produce, and when work must stop or route elsewhere.
- **counterargument_or_limit:** A full workflow can duplicate later user journey and tradeoff sections.
- **assumptions_and_boundaries:** This section should remain the concise operational entrypoint, with detailed rationale delegated to later sections.
- **revision_decision:** Expand it into a numbered decision sequence with explicit outputs at each gate.
- **additional_insight_to_add:** Entry criteria should be semantic, not keyword-only; mentioning “agent” in a task does not mean a new autonomous role is the right artifact.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The bullets correctly prioritize local sources, gates, external checks, and evidence labels but omit chartering and negative routing.
- **supporting_reason:** Default to classify the task, draft the charter, rank sources, define activation and nonactivation cases, grant minimum tools, specify process and output, then verify before reuse.
- **counterargument_or_limit:** Existing agents may need only one clause or test updated rather than a full redesign.
- **assumptions_and_boundaries:** For modifications, rerun the sequence only for affected decisions plus whole-artifact reconciliation.
- **revision_decision:** Add the missing charter, trigger, authority, and lifecycle steps while retaining the seed's four principles.
- **additional_insight_to_add:** Require a named parent-agent handoff contract so delegated context and returned evidence are bounded on both sides.

### Question 03: When does the default work well?
- **current_section_observation:** The guide is triggered by the theme, mapped paths, or nearby workflow surfaces, which is broad.
- **supporting_reason:** It works when the user needs a reusable specialist that can independently complete a coherent multi-step outcome with inspectable evidence.
- **counterargument_or_limit:** Nearby workflow similarity can be superficial, especially when a task needs a skill, command, or temporary subtask rather than persistent routing.
- **assumptions_and_boundaries:** At least one stable trigger, bounded responsibility, and verification contract should exist before creation proceeds.
- **revision_decision:** Add explicit fit tests before source loading expands.
- **additional_insight_to_add:** A good agent boundary minimizes shared mutable state; if two agents must continuously negotiate the same files or decision, the split is probably wrong.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The guide lacks stop conditions for ambiguous user intent, overlapping agents, unavailable tools, or nonverifiable outcomes.
- **supporting_reason:** Proceeding under those conditions creates routing conflicts, promises the host cannot keep, and makes completion subjective.
- **counterargument_or_limit:** A read-only exploratory prototype can help discover requirements without claiming production readiness.
- **assumptions_and_boundaries:** Prototypes must be explicitly isolated from automatic triggering and consequential tools.
- **revision_decision:** Add stop, clarify, prototype, and adjacent-route branches.
- **additional_insight_to_add:** Overlap should be resolved by narrowing trigger language or merging responsibilities before adding another agent to the routing surface.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The guide does not compare a persistent agent with direct parent execution, ephemeral delegation, skills, commands, hooks, or project instructions.
- **supporting_reason:** Persistent agents improve reuse and context isolation; ephemeral delegation avoids routing clutter; skills encode methods; commands encode explicit actions; hooks enforce lifecycle policy.
- **counterargument_or_limit:** Composition often provides the best design, such as an agent that loads a skill and invokes a validator.
- **assumptions_and_boundaries:** Choose the mechanism that owns the decision while composing lower-level mechanisms for execution.
- **revision_decision:** Add a compact mechanism-routing table or bullets.
- **additional_insight_to_add:** Persistent routing has a carrying cost because every new agent competes for activation and maintenance attention even when unused.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Existing bullets warn against replacing local conventions with external sources but omit trigger overlap, tool overgrant, context dumping, hidden retries, and missing retirement.
- **supporting_reason:** These operational defects often dominate prompt prose quality in real use.
- **counterargument_or_limit:** The guide should not become a complete failure registry.
- **assumptions_and_boundaries:** Name the highest-leverage screening questions here and route details to dedicated sections.
- **revision_decision:** Add a preflight stop list for overlap, unavailable authority, ambiguous ownership, and nonverifiable outcomes.
- **additional_insight_to_add:** Ask what the agent must never infer, because forbidden assumptions often reveal safer trigger and escalation boundaries more clearly than positive responsibilities.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** No usage example shows the guide applied to a task.
- **supporting_reason:** A good case creates a read-only migration-risk reviewer with explicit triggers and findings; a bad case creates a universal coding helper; a borderline case makes a validator agent around one command.
- **counterargument_or_limit:** The validator wrapper may be justified if proactive lifecycle invocation is the actual value.
- **assumptions_and_boundaries:** The wrapper must own routing and interpretation, not merely relay command arguments.
- **revision_decision:** Add three concise usage outcomes and their deciding factor.
- **additional_insight_to_add:** In borderline cases, run the workflow manually several times and observe stable handoffs before reserving a permanent agent identity.

### Question 08: How can the important claims be verified?
- **current_section_observation:** The guide says to prefer verification gates but does not define checks for the guide's own decisions.
- **supporting_reason:** Validate artifact schema, test positive and negative triggers, deny unavailable tools, execute a representative task, inspect output completeness, and rehearse one failure or escalation.
- **counterargument_or_limit:** Trigger decisions may vary across model versions, requiring repeated samples rather than exact expectations.
- **assumptions_and_boundaries:** Assert invariant route categories and safety outcomes, not word-for-word responses.
- **revision_decision:** Attach an evidence requirement to each decision step.
- **additional_insight_to_add:** Record false activation and missed activation separately because combining them into one success rate hides opposite routing defects.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The guide's local-first and evidence-preservation practices are grounded in the mapped corpus, while mechanism choice and trigger boundaries remain task-specific.
- **supporting_reason:** Local sources demonstrate concrete agent formats and trigger examples that justify the operational focus.
- **counterargument_or_limit:** The corpus's own platform and version assumptions may not match every target environment.
- **assumptions_and_boundaries:** Host-specific fields and tool names require current local confirmation.
- **revision_decision:** Mark stable process defaults separately from host-dependent details.
- **additional_insight_to_add:** Uncertainty should be assigned to an owner and next observation; anonymous “needs validation” notes tend to persist without changing release decisions.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The guide treats agent usage as a creation event rather than an ongoing portfolio decision.
- **supporting_reason:** Agents age, overlap, accumulate stale sources, and may lose their owner or invocation value.
- **counterargument_or_limit:** Portfolio governance can be disproportionate for a small plugin with one or two agents.
- **assumptions_and_boundaries:** Maintenance formality should scale with agent count, autonomy, risk, and invocation frequency.
- **revision_decision:** Include owner, refresh trigger, and retirement check in the minimum completion artifact.
- **additional_insight_to_add:** The best time to define retirement evidence is at creation, when intended value and expected usage are still explicit enough to measure.

## Section 010: User Journey Scenario

### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed names an agent-system designer, a broad starting state, and choices about context, delegation, and verification, but it does not carry one realistic request through those choices.
- **supporting_reason:** A complete journey should show how a user decides that a specialized agent is warranted and how the resulting charter constrains prompt generation.
- **counterargument_or_limit:** One scenario cannot represent every agent category and may overanchor readers on review-oriented work.
- **assumptions_and_boundaries:** The scenario should illustrate transferable decisions while clearly remaining an example, not a mandatory template.
- **revision_decision:** Expand the section around a concrete migration-risk reviewer journey from request through release and later review.
- **additional_insight_to_add:** Include both parent-agent and specialist responsibilities so the handoff boundary is visible rather than implied.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The journey starts with source paths and uncertainty but lacks a default first artifact.
- **supporting_reason:** Begin with a one-page charter that captures user outcome, trigger boundaries, input scope, tools, output, escalation, and retirement before selecting prompt phrasing.
- **counterargument_or_limit:** If an existing agent already has a charter, the user should amend the affected clauses rather than recreate it.
- **assumptions_and_boundaries:** The default applies to a new or materially changed persistent agent.
- **revision_decision:** Make the charter the scenario's first concrete output and trace later choices back to it.
- **additional_insight_to_add:** The charter should name what evidence the parent retains, because context isolation can otherwise discard facts needed to review the specialist's conclusion.

### Question 03: When does the default work well?
- **current_section_observation:** The seed implies a multi-step task but does not define why delegation improves it.
- **supporting_reason:** The default works when the specialist can inspect a bounded changeset, apply stable risk criteria, and return a structured finding set while the parent retains product decisions and write authority.
- **counterargument_or_limit:** Delegation adds overhead when the changeset is tiny or when parent and specialist need the same full context.
- **assumptions_and_boundaries:** The handoff must fit within a concise input contract and the specialist's output must be independently reviewable.
- **revision_decision:** Add explicit fit checks at the journey's decision point.
- **additional_insight_to_add:** Context isolation is valuable only when the compressed result retains provenance; summaries without file and evidence references merely move ambiguity downstream.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** No journey branch covers a user who actually needs a one-time review, a command, or a cross-system coordinator.
- **supporting_reason:** The agent path is wrong when the task is one-off, the input boundary cannot be stabilized, authority crosses several owners, or success depends on product judgment the specialist cannot own.
- **counterargument_or_limit:** A temporary subagent can still assist a one-time task without creating permanent routing metadata.
- **assumptions_and_boundaries:** The reference should distinguish persistent creation from ephemeral delegation.
- **revision_decision:** Add exit branches to direct execution, temporary delegation, adjacent references, and human approval.
- **additional_insight_to_add:** A journey should stop before artifact generation when the user cannot name who resolves disputed findings; otherwise escalation becomes circular.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The scenario does not compare a read-only reviewer, a write-enabled fixer, a parent-run checklist, or a command-backed validator.
- **supporting_reason:** Read-only review limits damage, a fixer reduces handoffs, a checklist keeps context centralized, and a validator maximizes determinism.
- **counterargument_or_limit:** Read-only specialists can create repeated remediation loops, while write-enabled agents can blur reviewer and implementer independence.
- **assumptions_and_boundaries:** Authority choice depends on reversibility, review independence, and the user's desired handoff cost.
- **revision_decision:** Show why the example chooses read-only findings first and names a later authority-expansion gate.
- **additional_insight_to_add:** Separating diagnosis from repair provides cleaner evidence during early deployment because observed quality is not confounded by unreviewed edits.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** The journey omits trigger overlap, stale source context, oversized handoffs, hidden write capability, and success declared without evidence.
- **supporting_reason:** These defects can make an apparently smooth scenario unsafe or impossible to audit.
- **counterargument_or_limit:** Listing every failure inside a narrative can disrupt usability.
- **assumptions_and_boundaries:** Include the failures that alter a journey decision and route the full taxonomy elsewhere.
- **revision_decision:** Add checkpoints that detect overlap, permission mismatch, evidence gaps, and unresolved escalation.
- **additional_insight_to_add:** The user journey should include one deliberate rejection so readers see that good agent design sometimes ends without creating an agent.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** The seed describes only a generic opening scenario.
- **supporting_reason:** A good journey yields a bounded migration reviewer; a bad journey generates a universal coding agent from a vague request; a borderline journey wraps a static analyzer with proactive routing.
- **counterargument_or_limit:** The static-analyzer wrapper may be valuable if it interprets results and owns lifecycle timing.
- **assumptions_and_boundaries:** Borderline value must come from routing, synthesis, or recovery rather than simple command relay.
- **revision_decision:** Embed all three outcomes at relevant branch points.
- **additional_insight_to_add:** Compare the artifacts produced, not just their prose: good design leaves a charter, agent file, scenario set, and owner record.

### Question 08: How can the important claims be verified?
- **current_section_observation:** The journey ends with “prove completion” but supplies no concrete observations.
- **supporting_reason:** Verify that representative migration requests route correctly, unrelated reviews do not, only approved read tools are used, findings cite evidence, and ambiguous ownership escalates.
- **counterargument_or_limit:** A few fixtures cannot estimate long-run false-trigger rates or performance across repositories.
- **assumptions_and_boundaries:** Initial verification supports bounded release; later telemetry informs expansion or retirement.
- **revision_decision:** Add acceptance evidence at every journey checkpoint and a post-release review.
- **additional_insight_to_add:** Include a deliberately clean changeset to verify that the agent can return “no findings” with checked scope rather than inventing issues to satisfy its role.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The role and design dimensions are grounded in the file, while the chosen migration-review scenario is new synthesis.
- **supporting_reason:** The scenario directly exercises mapped local patterns for triggering, system prompts, examples, tools, and output structure.
- **counterargument_or_limit:** Its usefulness for generation, orchestration, or security agents remains inferential.
- **assumptions_and_boundaries:** Readers should transfer decision questions, not copy domain details or tool sets.
- **revision_decision:** Label the scenario as illustrative and state which decisions generalize.
- **additional_insight_to_add:** Uncertainty about domain transfer should lead to a new representative fixture, not a larger generic persona.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The journey stops at initial completion and misses feedback into agent maintenance.
- **supporting_reason:** Real usage reveals false activations, missing evidence, escalation burden, and whether context isolation actually saves parent attention.
- **counterargument_or_limit:** Early metrics can be noisy and should not trigger constant prompt churn.
- **assumptions_and_boundaries:** Review after a meaningful sample or material failure, with changes tied to observed categories.
- **revision_decision:** Extend the journey through ownership, feedback, authority expansion, and retirement.
- **additional_insight_to_add:** The agent's first stable release should be treated as a hypothesis about workflow boundaries, with telemetry testing that hypothesis rather than merely counting invocations.

## Section 011: Decision Tradeoff Guide

### Question 01: What decision does this reference help make?
- **current_section_observation:** The table offers Adopt, Adapt, Avoid, and Cost of being wrong rows, but its conditions are broad and center on source agreement rather than the complete agent contract.
- **supporting_reason:** The guide should decide how much of a candidate pattern or generated agent can be reused under varying evidence, host compatibility, authority, and reversibility.
- **counterargument_or_limit:** A four-way table may oversimplify decisions that differ by clause; one agent can adopt its schema, adapt routing, and avoid a proposed tool grant.
- **assumptions_and_boundaries:** Apply decisions at the smallest consequential clause or contract dimension, then reconcile the whole artifact.
- **revision_decision:** Preserve the four decision labels and add clause-level criteria and resulting actions.
- **additional_insight_to_add:** “Cost of being wrong” should influence default authority and test depth, not remain a descriptive final row.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The seed implies adoption when local and external evidence agree, but agreement alone does not prove task fit or behavior.
- **supporting_reason:** Default to adapt unless schema, task boundary, host behavior, and verification all align; adopt unchanged only when copied choices are demonstrably relevant.
- **counterargument_or_limit:** Always adapting can create needless divergence from a stable canonical template.
- **assumptions_and_boundaries:** Adaptation should have a recorded reason and preserve proven conventions that do fit.
- **revision_decision:** Tighten adoption criteria and make bounded adaptation the normal response to task-specific differences.
- **additional_insight_to_add:** Every adaptation should add or update a regression scenario, otherwise local divergence becomes untracked folklore.

### Question 03: When does the default work well?
- **current_section_observation:** Conditions focus on source strength but not on the maturity or risk of the target agent.
- **supporting_reason:** Clause-level tradeoff analysis works well when the team can inspect current sources, identify the target host, estimate consequence, and run representative checks.
- **counterargument_or_limit:** Early experimentation may lack enough information for precise classification.
- **assumptions_and_boundaries:** Exploratory uncertainty should result in a narrow prototype, not premature adoption.
- **revision_decision:** Add maturity and risk conditions to each choice.
- **additional_insight_to_add:** Adoption is strongest for stable syntax and weakest for proactive routing and authority, which are more context-sensitive even within one host.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The guide can fail when evidence sources agree because they copy one another or when a reviewer treats Avoid as permanent rather than conditional.
- **supporting_reason:** Apparent consensus does not replace independent behavioral evidence, and an avoid decision can be revisited after a missing capability or test becomes available.
- **counterargument_or_limit:** Some boundaries, such as prohibited destructive authority, may be durable policy rather than temporary evidence gaps.
- **assumptions_and_boundaries:** Record whether avoidance is policy-based, capability-based, evidence-based, or task-fit-based.
- **revision_decision:** Add reason codes and explicit re-entry evidence for policy, capability, evidence, and task-fit avoidance.
- **additional_insight_to_add:** A reversible experiment can convert uncertainty into evidence, but it must not be used to bypass a policy-based avoid decision.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The current options omit defer, prototype, split, and retire.
- **supporting_reason:** Deferral waits for evidence, a prototype tests behavior with low authority, splitting isolates stable from uncertain responsibilities, and retirement removes obsolete routing.
- **counterargument_or_limit:** More categories can make the guide harder to use and invite indecision.
- **assumptions_and_boundaries:** Keep Adopt, Adapt, and Avoid as primary outcomes while describing prototype, split, defer, or retire as actions within them.
- **revision_decision:** Add these actions without changing the seed's decision vocabulary.
- **additional_insight_to_add:** Split when one responsibility has different trigger, authority, or lifecycle needs; do not split merely because the prompt is long.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** The guide warns about stale local assumptions and false confidence but omits copied tools, overlapping triggers, sunk-cost attachment, and adaptation without test updates.
- **supporting_reason:** These failures turn a reasonable choice label into an unsafe implementation.
- **counterargument_or_limit:** Later failure sections supply detailed controls, so this guide should retain only choice-changing screening questions.
- **assumptions_and_boundaries:** This guide should surface decision-specific gotchas and route operational details onward.
- **revision_decision:** Add reviewer questions about independence, authority, overlap, reversibility, and evidence consequences.
- **additional_insight_to_add:** Require the reviewer to name what would be undone if wrong; inability to answer reveals an unbounded or irreversible design.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** No concrete clause-level examples illustrate the four rows.
- **supporting_reason:** A good adoption reuses validated name syntax; a good adaptation adds negative triggers; an avoid rejects shell authority for a read-only reviewer; a borderline prototype tests proactive activation manually.
- **counterargument_or_limit:** Host versions may change which syntax is safe to adopt.
- **assumptions_and_boundaries:** Examples must be rechecked against current local contracts.
- **revision_decision:** Add clause-level examples and corresponding verification questions.
- **additional_insight_to_add:** Cost-of-error examples should include routing harm, not only bad task output, because unnecessary delegation can consume context and obscure user intent.

### Question 08: How can the important claims be verified?
- **current_section_observation:** Existing verification questions ask whether patterns appear in sources and whether boundaries are labeled, but not whether behavior supports the chosen option.
- **supporting_reason:** Verify source relevance, host acceptance, positive and negative scenarios, denied capabilities, output evidence, and rollback or escalation behavior.
- **counterargument_or_limit:** Some decisions depend on reviewer judgment about maintainability or ownership.
- **assumptions_and_boundaries:** Structured reviewer decisions should name criteria, owner, and uncertainty.
- **revision_decision:** Strengthen each row's verification question into an evidence bundle.
- **additional_insight_to_add:** Sample borderline decisions after deployment because they are the most likely to reveal that the original classification was too permissive or too cautious.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The four-way framing is a useful local decision model, but thresholds for evidence strength and acceptable error cost are not empirically established.
- **supporting_reason:** Explicit choices and verification questions improve reviewability regardless of exact thresholds.
- **counterargument_or_limit:** Different organizations and agent hosts may set very different authority and risk tolerances.
- **assumptions_and_boundaries:** Treat thresholds as policy inputs and document them rather than implying universal values.
- **revision_decision:** Separate invariant decision questions from local policy judgments.
- **additional_insight_to_add:** Uncertainty should be localized by clause; a single uncertain capability should not force either blind adoption or rejection of the entire agent.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The guide treats decisions as static and does not describe migration between states.
- **supporting_reason:** Evidence and host behavior change, so adapted clauses can become canonical, avoided capabilities can become testable, and adopted patterns can require retirement.
- **counterargument_or_limit:** Frequent reclassification can create churn and weaken stable contracts.
- **assumptions_and_boundaries:** Reclassify only on material source, behavior, policy, or ownership changes.
- **revision_decision:** Add state-transition triggers and require linked test and documentation updates.
- **additional_insight_to_add:** Track the reason and evidence for each transition; otherwise “adapted over time” conceals whether the design improved or merely drifted.

## Section 012: Local Corpus Hierarchy

### Question 01: What decision does this reference help make?
- **current_section_observation:** The hierarchy assigns canonical, legacy, supporting context, example, and detail roles to twelve paths, but every row repeats the same generic reviewer question.
- **supporting_reason:** The hierarchy should decide which source governs a conflict and what unique contribution each source type should make.
- **counterargument_or_limit:** Role labels can become stale when live files change or archived files are promoted for historical reconstruction.
- **assumptions_and_boundaries:** Authority is contextual and claim-specific, even when one file is the default primary source.
- **revision_decision:** Preserve every role assignment and replace generic interpretation with a conflict-resolution and contribution protocol.
- **additional_insight_to_add:** “Canonical” here names the frozen primary source for this corpus lineage; it does not automatically mean the archive is the current operational file.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The archived skill is marked canonical while the live skill is supporting context, which can confuse a reader doing current work.
- **supporting_reason:** Use the hierarchy for provenance claims, then prefer the live entrypoint for current operations after checking drift; consult detail sources for their bounded questions and examples only for instantiation.
- **counterargument_or_limit:** The live source may contain an unreviewed regression, so recency alone does not confer authority.
- **assumptions_and_boundaries:** Current operational use requires both role awareness and validation against the active repository.
- **revision_decision:** Explain that archived canonical status governs provenance while validated live guidance informs current repository operation.
- **additional_insight_to_add:** When live and archived guidance differ, the correct output may be an adaptation note and regression test rather than choosing one source wholesale.

### Question 03: When does the default work well?
- **current_section_observation:** The hierarchy assumes the six source types have distinct and complementary roles.
- **supporting_reason:** It works when the entrypoint defines the contract, detail files explain specific decisions, examples conform to that contract, and archive/live status is known.
- **counterargument_or_limit:** Generated documentation families often repeat content and may not maintain clean normative boundaries.
- **assumptions_and_boundaries:** Reviewers must inspect actual text when a consequential contradiction appears.
- **revision_decision:** Add coherence checks and a precedence rule based on explicitness, current validation, and scope.
- **additional_insight_to_add:** A source can be canonical for format but merely advisory for prompt quality, so authority should be recorded per claim dimension.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** No path handles missing canonical sources, contradictory validators, or a live example that intentionally demonstrates a newer contract.
- **supporting_reason:** A static hierarchy fails when repository behavior or explicit policy has moved beyond its labels.
- **counterargument_or_limit:** Discarding hierarchy whenever behavior differs would let accidental implementation bugs override documented contracts.
- **assumptions_and_boundaries:** Resolve conflict by identifying whether the question is normative, operational, historical, or illustrative, then obtain targeted evidence.
- **revision_decision:** Add a conflict-resolution ladder and a blocked state for unresolved high-risk discrepancies.
- **additional_insight_to_add:** A runtime mismatch should produce both a prompt decision and a documentation defect report; silently coding around it leaves future creators exposed.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The hierarchy uses fixed roles rather than confidence-weighted claims, versioned decision records, or source dependency graphs.
- **supporting_reason:** Fixed roles are simple, claim weighting is precise, decision records explain exceptions, and dependency graphs support targeted refresh.
- **counterargument_or_limit:** More formal systems add maintenance overhead and can exceed the needs of a small corpus.
- **assumptions_and_boundaries:** Use fixed roles by default and add claim-level records only for consequential conflicts or divergence.
- **revision_decision:** Retain the simple table while adding a minimal claim-conflict record format.
- **additional_insight_to_add:** A decision record should include rejected sources and why; otherwise later maintainers may reintroduce the same conflict without context.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Generic reviewer questions, duplicate lineage counting, archive/live ambiguity, and example authority inflation are the main hierarchy defects.
- **supporting_reason:** They obscure why a source was selected and allow a convenient example to override stricter local rules.
- **counterargument_or_limit:** Repetition in the table still ensures every path is covered by a review prompt.
- **assumptions_and_boundaries:** Coverage should become source-specific enough to change retrieval or synthesis decisions.
- **revision_decision:** Add role-specific reviewer questions and deduplication rules after the table.
- **additional_insight_to_add:** Ask what a source must not decide, not only what it contributes; negative authority boundaries prevent examples and generators from becoming accidental policy.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** The hierarchy does not demonstrate a conflict.
- **supporting_reason:** A good resolution uses the live validator for accepted syntax and archived docs for history; a bad resolution copies a legacy example; a borderline resolution adopts newer live behavior with a compatibility warning.
- **counterargument_or_limit:** Validator acceptance alone may permit fields whose semantics remain unsupported.
- **assumptions_and_boundaries:** Validate both parseability and behavior before promoting a divergent live pattern.
- **revision_decision:** Add three conflict cases covering validated live adoption, unsafe legacy copying, and reversible compatibility adaptation.
- **additional_insight_to_add:** Borderline promotion should be reversible and should preserve the old fixture until migration coverage demonstrates safe replacement.

### Question 08: How can the important claims be verified?
- **current_section_observation:** The role assignments can be checked against paths, but their governing authority and contribution require semantic and behavioral evidence.
- **supporting_reason:** Compare relevant spans, run current validators, instantiate a minimal artifact, and exercise the behavior affected by the disputed rule.
- **counterargument_or_limit:** Some prose recommendations have no direct runtime manifestation and need expert review.
- **assumptions_and_boundaries:** Expert review should name the decision dimension, competing evidence, and reason for precedence.
- **revision_decision:** Add a conflict-verification packet and outcome statuses.
- **additional_insight_to_add:** Verify that the selected source's rule composes with neighboring fields; a locally valid frontmatter choice can still conflict with trigger or tool semantics elsewhere.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** File roles and headings are recorded corpus facts, while the operational precedence between archived canonical and live supporting sources is an inferred maintenance rule.
- **supporting_reason:** The proposed dual interpretation preserves provenance without forcing current work to use an older path blindly.
- **counterargument_or_limit:** Repository owners may have intended the archived file to remain the normative frozen contract for this generation cycle.
- **assumptions_and_boundaries:** Do not rewrite source-role facts; document operational deviations and test them.
- **revision_decision:** Keep all existing classifications and clearly label added precedence guidance as synthesis.
- **additional_insight_to_add:** Confidence should attach to the decision record, not just the source label, because the same hierarchy can yield different correct choices for history and current execution.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The hierarchy is read-only documentation and lacks an explicit propagation model.
- **supporting_reason:** A changed canonical or live source can affect generated prompts, examples, validators, and tests in different directions.
- **counterargument_or_limit:** Full dependency tracking may be excessive when sources are rarely changed.
- **assumptions_and_boundaries:** Track only material clauses that affect schema, routing, authority, execution, or verification.
- **revision_decision:** Add a lightweight `source -> decision -> artifact -> gate` propagation record.
- **additional_insight_to_add:** Contradiction frequency is itself a quality signal; repeated exceptions suggest the hierarchy or source ownership model needs revision, not more one-off adaptations.

## Section 013: Theme Specific Artifact

### Question 01: What decision does this reference help make?
- **current_section_observation:** The section names an agent charter with owner, user, trigger, tool budget, escalation, and retirement, yet its table defines only user goal, decision boundary, and verification gate.
- **supporting_reason:** The artifact should decide whether the proposed agent is operationally complete enough to convert into an agent file and behavioral tests.
- **counterargument_or_limit:** A charter can become duplicative if every field is already enforced in structured frontmatter and policy.
- **assumptions_and_boundaries:** The charter may reference enforced fields, but it must make cross-field decisions and ownership visible in one review surface.
- **revision_decision:** Expand the table to cover all named fields plus inputs, authority, process, output, recovery, evidence, and refresh.
- **additional_insight_to_add:** The charter is not the prompt; it is the reviewable design contract from which prompt clauses and tests are derived.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The seed offers three generic completion rules without a concrete filled example.
- **supporting_reason:** Use a concise structured charter before generation, require every field to state a decision or bounded unknown, and reject blank assurances such as “use appropriate tools.”
- **counterargument_or_limit:** Highly constrained agents can inherit several fields from a documented host policy.
- **assumptions_and_boundaries:** Inherited values must identify the policy and remain testable in the active host.
- **revision_decision:** Add a complete field schema and one filled migration-reviewer charter.
- **additional_insight_to_add:** Each tool grant should map to a process step, and each process step should map to an output or checkpoint; unmapped items reveal excess authority or ritual.

### Question 03: When does the default work well?
- **current_section_observation:** The artifact is framed generally, with no fit conditions.
- **supporting_reason:** It works well for persistent or proactive agents, multi-step workflows, shared plugins, and tasks where another reviewer must understand authority and completion without reading all source material.
- **counterargument_or_limit:** A one-time temporary subagent may need only a task-specific handoff and result schema.
- **assumptions_and_boundaries:** Charter depth scales with reuse, autonomy, risk, and maintenance horizon.
- **revision_decision:** Add proportional charter requirements scaled by reuse, autonomy, consequence, and maintenance horizon.
- **additional_insight_to_add:** Even a compact charter should never omit owner, trigger, authority, output, and stop condition because those fields define accountability and blast radius.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The seed does not explain how a charter can be complete on paper yet operationally weak.
- **supporting_reason:** It fails when fields repeat vague prose, conflict with each other, promise unavailable tools, leave escalation ownerless, or cannot generate tests.
- **counterargument_or_limit:** Some qualitative goals require reviewer judgment and cannot be reduced to deterministic assertions.
- **assumptions_and_boundaries:** Qualitative fields still need observable criteria and examples.
- **revision_decision:** Add checks for contradictory fields, unavailable capabilities, ambiguous derivation, and testable completion.
- **additional_insight_to_add:** A charter should be rejected if two independent implementers would derive materially different authority or completion behavior from it.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The seed does not compare Markdown charters with machine-readable schemas, fixtures, or decision records.
- **supporting_reason:** YAML or JSON schemas improve validation, Markdown tables improve review, executable fixtures prove behavior, and architecture decision records preserve high-risk rationale.
- **counterargument_or_limit:** Splitting the design across too many artifacts creates synchronization failure.
- **assumptions_and_boundaries:** Keep one charter as the source of decisions and generate or link auxiliary tests and records from it.
- **revision_decision:** Explain that format is flexible but field coverage and traceability are not.
- **additional_insight_to_add:** Machine-readable fields are most valuable for trigger, tools, budgets, and statuses; nuanced rationale can remain prose linked to those fields.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** The current three-row table can falsely appear complete while omitting negative triggers, prohibited actions, state mutation, retry bounds, and ownership transfer.
- **supporting_reason:** These omissions are exactly where autonomous behavior escapes intent.
- **counterargument_or_limit:** A very large charter can bury the few decisions that matter.
- **assumptions_and_boundaries:** Prefer concise, decision-bearing entries and route detailed methods to the system prompt or skill.
- **revision_decision:** Add mandatory fields and a review rule against generic filler.
- **additional_insight_to_add:** Include a “must not decide” field because negative authority is easier to audit than relying on the absence of positive permission.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** The seed names the charter but provides no completed example showing how its fields constrain an agent.
- **supporting_reason:** A good charter names repository-scoped reads, migration findings, and escalation; a bad charter says “help with migrations using needed tools”; a borderline charter wraps a validator but lacks unique ownership.
- **counterargument_or_limit:** A validator wrapper can become valid after adding proactive lifecycle timing, interpretation, and recovery.
- **assumptions_and_boundaries:** The example should show how added responsibilities change artifact choice.
- **revision_decision:** Add a filled good example and short bad/borderline contrasts.
- **additional_insight_to_add:** Ask whether removing the agent identity changes the workflow; if not, the artifact likely describes a command or skill rather than an agent.

### Question 08: How can the important claims be verified?
- **current_section_observation:** Only the verification gate field points toward proof.
- **supporting_reason:** Validate field completeness, check cross-field consistency, derive prompt clauses and tests, run positive and negative routes, inspect tool usage, and rehearse escalation and retirement.
- **counterargument_or_limit:** Retirement cannot be fully tested at creation because value and overlap emerge over time.
- **assumptions_and_boundaries:** Define measurable review triggers and owner responsibilities even when future outcomes are unknown.
- **revision_decision:** Add bidirectional charter traceability from every consequential field to a prompt clause and enforcing observation.
- **additional_insight_to_add:** A field is complete only when a reviewer can identify either an enforcing mechanism or an observation that would reveal violation.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The need for an agent charter is synthesis, while local sources directly support many constituent fields such as triggers, tools, process, output, and examples.
- **supporting_reason:** Consolidating those decisions in one artifact reduces hidden coupling and review cost.
- **counterargument_or_limit:** The optimal field set and level of detail are not established empirically.
- **assumptions_and_boundaries:** Treat the proposed schema as a robust default and remove fields only when their decision is enforced elsewhere.
- **revision_decision:** Label the charter schema as combined inference grounded in mapped local concerns.
- **additional_insight_to_add:** Track which charter fields repeatedly produce no decisions; that evidence can simplify the schema without weakening control.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The artifact is described as a creation deliverable, not a lifecycle control surface.
- **supporting_reason:** Ownership, source dependencies, authority, metrics, and retirement criteria all change after release.
- **counterargument_or_limit:** Continual updates can cause charter and prompt divergence if not coupled.
- **assumptions_and_boundaries:** Material charter changes must update prompt clauses and linked tests in the same review.
- **revision_decision:** Add charter versioning rules that require prompt and fixture updates in the same material change.
- **additional_insight_to_add:** The charter can support agent portfolio review by exposing overlapping triggers and duplicate ownership before those conflicts appear in runtime telemetry.

## Section 014: Worked Example Set

### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed gives one-sentence good, bad, and borderline statements but no artifact fragments or consequences.
- **supporting_reason:** The examples should help a reviewer distinguish a releasable agent design from generic prompt prose and from a case that needs reduced authority or another mechanism.
- **counterargument_or_limit:** Examples can be copied mechanically and mistaken for universal templates.
- **assumptions_and_boundaries:** Each example should explain the deciding condition and what must be customized.
- **revision_decision:** Replace the terse statements with three operational cases using the same migration-review domain.
- **additional_insight_to_add:** Show inputs, trigger, tools, output, gate, and failure behavior so quality is visible across the whole contract.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The good example says to load sources and write a gate but omits negative routing and least privilege.
- **supporting_reason:** The good default is a read-only specialist with precise positive and negative triggers, repository-scoped inputs, evidence-bearing findings, one bounded retry, and escalation.
- **counterargument_or_limit:** Some generation agents must write artifacts to deliver value.
- **assumptions_and_boundaries:** Authority should match the task; read-only is the example's risk-scaled starting point, not a universal agent restriction.
- **revision_decision:** Make the good example complete and explain how a write-enabled variant would earn broader authority.
- **additional_insight_to_add:** Include a clean-input outcome to demonstrate that “no findings” is acceptable when supported by checked scope.

### Question 03: When does the default work well?
- **current_section_observation:** The example set does not state the fit conditions of the good pattern.
- **supporting_reason:** It works when the task has a bounded changeset, stable criteria, available read tools, and a parent or owner who decides remediation.
- **counterargument_or_limit:** It fails when meaningful risk assessment requires external systems or product context absent from the handoff.
- **assumptions_and_boundaries:** Missing required context should cause escalation rather than guessed conclusions.
- **revision_decision:** Add fit and prerequisite lines to the good case.
- **additional_insight_to_add:** Explicitly name context that should not be copied into the specialist, reducing accidental data exposure and attention dilution.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The bad case is generic but does not expose concrete failure behavior.
- **supporting_reason:** A universal helper with broad tools can overtrigger, duplicate parent work, mutate files unexpectedly, and return unverifiable claims.
- **counterargument_or_limit:** A broad generalist may be acceptable as the primary agent rather than a routed specialist.
- **assumptions_and_boundaries:** The defect is creating a competing specialist with no unique boundary, not general capability in every context.
- **revision_decision:** Show operational consequences and the preferred mechanism alternative.
- **additional_insight_to_add:** A bad example should fail a named gate, making the lesson executable rather than stylistic.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The borderline statement mentions thin or conflicting evidence but not mechanism alternatives.
- **supporting_reason:** The borderline validator wrapper could remain a command, become a skill, or become an agent if it owns proactive timing, interpretation, and escalation.
- **counterargument_or_limit:** Permanent routing may still be unnecessary even after interpretation is added if usage is rare.
- **assumptions_and_boundaries:** Invocation frequency and portfolio cost affect the final mechanism decision.
- **revision_decision:** Turn the borderline case into a branching decision with evidence needed for each path.
- **additional_insight_to_add:** Trial repeated manual use before creating permanent routing when frequency and handoff stability are unknown.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Terse examples hide subtle defects such as copied tool arrays, missing nonactivation cases, invented findings, and unbounded retry.
- **supporting_reason:** Readers need to see these defects in context to recognize them in plausible drafts.
- **counterargument_or_limit:** Overloading examples with every rule makes them difficult to scan.
- **assumptions_and_boundaries:** Focus each example on a coherent set of high-impact decisions and link to dedicated sections for exhaustive checks.
- **revision_decision:** Annotate decisive gotchas without turning examples into full prompts.
- **additional_insight_to_add:** Include a neighboring-agent overlap case because routing conflicts often remain invisible in isolated examples.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** The section technically answers this question but only at slogan level.
- **supporting_reason:** Good examples expose enforceable contracts, bad examples expose consequences and failed gates, and borderline examples expose the missing observation needed for a decision.
- **counterargument_or_limit:** Any fixed example remains incomplete relative to a real repository.
- **assumptions_and_boundaries:** Readers must substitute current source paths, host capabilities, owners, and tests.
- **revision_decision:** Provide structured mini-cases rather than copied full agent files.
- **additional_insight_to_add:** Make the borderline example's next experiment explicit so uncertainty drives action rather than cautionary prose alone.

### Question 08: How can the important claims be verified?
- **current_section_observation:** None of the seed examples contains acceptance evidence.
- **supporting_reason:** For each case, run representative route, nonroute, permission, output, clean-input, and failure fixtures and compare against the charter.
- **counterargument_or_limit:** The bad example need not be deployed to prove every predicted consequence.
- **assumptions_and_boundaries:** Static review can reject obvious violations; safe simulation can demonstrate subtle routing or recovery defects.
- **revision_decision:** Add route, permission, clean-input, failure, and output-verification results to each mini-case.
- **additional_insight_to_add:** Use the same fixture set when comparing alternatives so observed differences come from the agent design rather than changing tasks.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The quality distinctions follow the reference's logic, but the example outcomes are illustrative rather than measured production data.
- **supporting_reason:** They instantiate concrete local patterns for sources, trigger examples, tools, process, outputs, and validation.
- **counterargument_or_limit:** Actual routing and task quality remain host- and model-dependent.
- **assumptions_and_boundaries:** Present predicted failure mechanisms as design reasoning and require observation before broader claims.
- **revision_decision:** Label the cases as worked designs, not performance evidence.
- **additional_insight_to_add:** An example's confidence should be split across static contract quality and observed runtime behavior.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The examples do not show how a borderline design evolves after evidence arrives.
- **supporting_reason:** Lifecycle transitions teach readers how to expand, narrow, merge, or retire an agent based on observed use.
- **counterargument_or_limit:** Long narratives can distract from the immediate creation decision.
- **assumptions_and_boundaries:** Add one concise transition rather than a full case study.
- **revision_decision:** Show the borderline wrapper either remaining a command or earning agent status through stable repeated handoffs.
- **additional_insight_to_add:** Good agent evolution is evidence-driven capability migration, not prompt accretion; remove clauses and authority when they do not improve the owned outcome.

## Section 015: Outcome Metrics and Feedback Loops

### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed names one leading indicator, one failure signal, and a review cadence but does not define measurements, denominators, or actions.
- **supporting_reason:** Metrics should decide whether to keep, revise, narrow, expand, merge, or retire the agent and its prompt pattern.
- **counterargument_or_limit:** Poorly chosen metrics can reward fewer clarifications while hiding silent mistakes or user avoidance.
- **assumptions_and_boundaries:** Use a balanced set spanning routing, task evidence, authority, recovery, review effort, and user outcome.
- **revision_decision:** Expand the section into a measurement and feedback protocol with action thresholds expressed as local policy, not universal truth.
- **additional_insight_to_add:** Track missed activations and false activations separately because one aggregate routing score can conceal opposing harms.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** “Fewer clarifications” and “fewer unverifiable claims” are useful directions but lack baselines and review windows.
- **supporting_reason:** Establish a pre-agent or first-release baseline, record a small fixed event schema per run, review after a meaningful sample or material incident, and change one contract dimension at a time.
- **counterargument_or_limit:** Low-volume agents may never produce statistically meaningful samples.
- **assumptions_and_boundaries:** Low-volume review can rely on qualitative case inspection and consequence-weighted incidents rather than unstable percentages.
- **revision_decision:** Add baseline, sample, cadence, and change-isolation guidance.
- **additional_insight_to_add:** A severe authority violation should trigger immediate review regardless of sample size; not every metric needs a statistical threshold.

### Question 03: When does the default work well?
- **current_section_observation:** The seed assumes repeated use but does not state it.
- **supporting_reason:** Metrics work well when invocations can be classified consistently and reviewers can determine expected route, evidence quality, and outcome without excessive hindsight.
- **counterargument_or_limit:** Highly novel tasks may differ too much for aggregate comparisons.
- **assumptions_and_boundaries:** Segment by task class, repository, risk, or agent version when those differences change expectations.
- **revision_decision:** Add task-class comparability rules and segment observations when repository, risk, or agent version differs.
- **additional_insight_to_add:** Record the prompt or agent version with each outcome; otherwise improvements and regressions cannot be attributed to a specific change.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The section could encourage vanity metrics such as invocation count, shorter output, or fewer questions.
- **supporting_reason:** These measures can improve while correctness, user control, or evidence quality worsens.
- **counterargument_or_limit:** Usage and latency still matter when interpreted alongside quality and consequence.
- **assumptions_and_boundaries:** No efficiency metric should stand alone for release or authority expansion.
- **revision_decision:** Add anti-metrics that reject speed or usage gains when correctness, evidence, or user control declines.
- **additional_insight_to_add:** User bypass behavior is a failure signal: declining invocation or redoing work manually may reveal low trust even when formal checks pass.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The seed mentions rerunning a verifier and refreshing sources but omits manual audits, controlled comparisons, shadow mode, and canaries.
- **supporting_reason:** Manual audits provide nuance, controlled comparisons isolate prompt changes, shadow mode measures routing without action, and canaries expose real integration behavior.
- **counterargument_or_limit:** Experiments add operational cost and can expose sensitive tasks or users.
- **assumptions_and_boundaries:** Use privacy-preserving samples, reversible authority, and explicit owner approval.
- **revision_decision:** Add alternative feedback methods and their risk tradeoffs.
- **additional_insight_to_add:** Shadow-mode false activations are valuable evidence before proactive release because they reveal routing cost without mutating user workflows.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Missing denominators, selection bias, model-version drift, reviewer inconsistency, and metric gaming are not addressed.
- **supporting_reason:** These flaws can make prompt changes appear effective when task mix or evaluation standards changed.
- **counterargument_or_limit:** Perfect experimental control is unrealistic for internal agent workflows.
- **assumptions_and_boundaries:** Record enough context to identify major confounders and present conclusions as bounded judgments.
- **revision_decision:** Add measurement hygiene for denominators, version attribution, reviewer calibration, confounders, and uncertainty.
- **additional_insight_to_add:** Calibrate reviewers on a shared fixture set before comparing versions; disagreement itself is evidence that the output contract is ambiguous.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** No metric example shows numerator, denominator, decision, or uncertainty.
- **supporting_reason:** A good record states three false activations among forty labeled opportunities and the narrowing action; a bad record says usage increased; a borderline record reports faster runs on a changed task mix.
- **counterargument_or_limit:** Small numeric examples should not become universal thresholds.
- **assumptions_and_boundaries:** Values illustrate record shape only; teams set policy based on consequence and baseline.
- **revision_decision:** Add worked measurement records with explicit scope.
- **additional_insight_to_add:** Pair quantitative counts with sampled transcripts or artifacts so reviewers can tell whether classification labels reflect real user harm.

### Question 08: How can the important claims be verified?
- **current_section_observation:** The seed says to rerun a verifier but does not verify metric collection or causal conclusions.
- **supporting_reason:** Validate event completeness, sample labels, reviewer agreement, version attribution, and whether the proposed change improves the targeted fixture without regressing others.
- **counterargument_or_limit:** Causal proof may remain weak in observational workflows.
- **assumptions_and_boundaries:** State inference limits and use controlled fixtures where feasible.
- **revision_decision:** Add data-quality and regression gates before acting on metrics.
- **additional_insight_to_add:** Keep a holdout scenario set for material prompt revisions so repeated tuning does not overfit the visible examples.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The seed's indicators are sensible but unmeasured, and no historical values are provided.
- **supporting_reason:** They directly target clarification burden and unverifiable output, two relevant agent-prompt outcomes.
- **counterargument_or_limit:** Their relationship to user value and correctness is context-dependent.
- **assumptions_and_boundaries:** Treat them as proposed signals, not established performance results.
- **revision_decision:** Explicitly label targets and example thresholds as policy or future measurement.
- **additional_insight_to_add:** Confidence should increase only when multiple signals agree, such as fewer clarifications alongside stable correctness and lower reviewer rework.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** Feedback is described as refreshing sources and rerunning verification, not as a controlled prompt evolution loop.
- **supporting_reason:** Metrics can identify whether the problem lies in routing, context, authority, process, output, or recovery, enabling targeted revisions.
- **counterargument_or_limit:** Frequent local optimization can make the prompt fragmented and contradictory.
- **assumptions_and_boundaries:** After targeted edits, reread and retest the whole artifact.
- **revision_decision:** Add category-based diagnosis, one-change-at-a-time experiments, and periodic full reconciliation.
- **additional_insight_to_add:** Retirement is a successful metric outcome when another mechanism delivers the same result with lower routing and maintenance cost.

## Section 016: Completeness Checklist

### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed checklist covers scenario, tradeoff options, hierarchy, artifact, examples, metrics, and routing, but it does not decide whether the actual agent contract is releasable.
- **supporting_reason:** A completeness gate should decide whether discovery, routing, authority, execution, output, recovery, verification, ownership, and lifecycle decisions are all reviewable.
- **counterargument_or_limit:** A checklist can encourage box-ticking and cannot replace semantic review of how clauses interact.
- **assumptions_and_boundaries:** Completion requires both item evidence and a final whole-artifact reconciliation.
- **revision_decision:** Preserve all seven seed checks and expand them into an evidence-bearing release checklist with explicit fail conditions.
- **additional_insight_to_add:** Separate “present” from “adequate”; a trigger example exists only structurally until it distinguishes real neighboring routes.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The current bullets are phrased as content-presence statements without owners, evidence, or release consequences.
- **supporting_reason:** Require each item to name its supporting artifact or observation and block release when a high-consequence decision is missing or contradictory.
- **counterargument_or_limit:** Low-risk experimental agents may reasonably ship to manual read-only use with incomplete behavioral evidence.
- **assumptions_and_boundaries:** Partial verification must narrow invocation and authority and be labeled explicitly.
- **revision_decision:** Organize the expanded checklist by decision, evidence, and release status.
- **additional_insight_to_add:** Use “not applicable” only with a reason and named enforcing boundary; unexplained omission is not completion.

### Question 03: When does the default work well?
- **current_section_observation:** The seed applies generically but does not state which artifacts make its checks cheap and repeatable.
- **supporting_reason:** It works when the charter, source ledger, agent file, fixture set, command evidence, and ownership record are available together.
- **counterargument_or_limit:** Documentation spread across several systems can make complete evidence expensive to assemble.
- **assumptions_and_boundaries:** Link to durable artifacts and keep the checklist as an index rather than duplicating every detail.
- **revision_decision:** Add required evidence locations and a compact completion record.
- **additional_insight_to_add:** A checklist that is difficult to populate often reveals fragmented ownership or a prompt design that cannot be explained coherently.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The checklist can pass even if every individual section looks complete but trigger, tools, process, and output contradict each other.
- **supporting_reason:** Cross-field defects emerge only when the full agent is reread and exercised end to end.
- **counterargument_or_limit:** Detailed item-level checks still catch omissions efficiently before expensive integrated review.
- **assumptions_and_boundaries:** Use item checks as preconditions, not substitutes, for reconciliation.
- **revision_decision:** Add explicit contradiction, duplication, and end-to-end gates.
- **additional_insight_to_add:** Require one reviewer to explain the agent from user request through returned decision without consulting hidden conversation; gaps expose incomplete handoffs.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The seed uses a manual Markdown checklist and does not compare machine validation, peer review, or behavioral suites.
- **supporting_reason:** Schemas catch deterministic omissions, peer review catches judgment errors, and scenarios reveal host behavior; each covers a different failure class.
- **counterargument_or_limit:** Maintaining several gates can be burdensome and duplicated.
- **assumptions_and_boundaries:** Automate stable structural rules and reserve human review for consequence, ambiguity, and composition.
- **revision_decision:** Add evidence types per checklist category rather than prescribe one universal tool.
- **additional_insight_to_add:** Automation should fail on missing data, while reviewers decide whether present data is relevant and sufficient.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** The checklist omits negative triggers, prohibited actions, tool-to-step mapping, retry bounds, clean outcomes, partial verification, source freshness, and retirement ownership.
- **supporting_reason:** These omissions allow broad or ownerless agents to appear complete.
- **counterargument_or_limit:** An exhaustive list can become unreadable and stale.
- **assumptions_and_boundaries:** Group checks by contract dimension and keep details in linked sections.
- **revision_decision:** Add high-leverage omitted checks and a rule for maintaining the checklist from observed failures.
- **additional_insight_to_add:** Include neighboring-agent overlap as a first-class completeness item because isolated trigger tests systematically miss portfolio conflicts.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** No completed checklist example shows evidence or partial status.
- **supporting_reason:** A good record links each decision to evidence and reports residual risk; a bad record marks every box from prose presence; a borderline record is structurally complete but behaviorally unverified.
- **counterargument_or_limit:** Full example records can be too long for the reference.
- **assumptions_and_boundaries:** A concise status example can demonstrate the distinction without duplicating all artifacts.
- **revision_decision:** Add interpretations for full pass, failed release, and structurally verified but behaviorally constrained release.
- **additional_insight_to_add:** Constrained release should name exactly what is disabled, such as proactive routing or write authority, rather than using a vague caution label.

### Question 08: How can the important claims be verified?
- **current_section_observation:** The checklist claims completeness by inspection but has no meta-check that all original requirements or packet decisions were incorporated.
- **supporting_reason:** Trace charter fields and revision decisions to prompt clauses, fixtures, commands, and owner records, then reread the complete artifact.
- **counterargument_or_limit:** Full traceability for every low-impact sentence is unnecessary.
- **assumptions_and_boundaries:** Trace consequential routing, authority, output, recovery, and lifecycle decisions.
- **revision_decision:** Add a minimum traceability matrix and whole-file skeptical reread.
- **additional_insight_to_add:** Sample from both directions: every key requirement should reach a gate, and every granted capability should resolve back to an approved requirement.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The seed categories are clearly relevant, but their sufficiency and the proposed additions are engineering synthesis rather than measured guarantees.
- **supporting_reason:** Together they cover the contract surfaces identified across the local sources and evolved reference.
- **counterargument_or_limit:** Host-specific policy, security, or compliance may require additional checks.
- **assumptions_and_boundaries:** Treat this as a robust minimum and layer local mandatory gates on top.
- **revision_decision:** State scope and require explicit local additions where risk demands them.
- **additional_insight_to_add:** Checklist adequacy should be reviewed after incidents and near misses, not only during scheduled documentation refresh.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** Completion is framed as a one-time pre-release state.
- **supporting_reason:** Source, host, ownership, and routing portfolios evolve, so prior completeness can expire.
- **counterargument_or_limit:** Rechecking every item on every minor edit wastes effort.
- **assumptions_and_boundaries:** Material changes trigger affected checks plus full reconciliation; cosmetic changes need only structural confirmation.
- **revision_decision:** Add freshness and change-impact rules to the checklist.
- **additional_insight_to_add:** Record the last verified authority level and agent version so maintainers know what evidence must be renewed before expanding behavior.

## Section 017: Adjacent Reference Routing

### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed recommends debate, subagent, context, or verification references and then gives vague “agent,” “creation,” and “prompt” routes that do not identify a real alternative.
- **supporting_reason:** The section should decide when this creation reference stops being the primary guide and what narrower mechanism or reference owns the next question.
- **counterargument_or_limit:** Exact adjacent filenames can drift across a reference corpus and become stale.
- **assumptions_and_boundaries:** Route by decision category and name a concrete artifact or search criterion when a stable path is unavailable.
- **revision_decision:** Replace generic adjacency language with a decision matrix for mechanism, triggering, prompt design, delegation, context, verification, debate, and lifecycle.
- **additional_insight_to_add:** A route is complete only when it transfers the unresolved question, evidence already gathered, and the decision owner.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The seed says to use adjacent references when behavior narrows but does not give an escalation order.
- **supporting_reason:** First decide whether an agent should exist, then route the remaining specialized question to the narrowest source or workflow while retaining the charter as the integration contract.
- **counterargument_or_limit:** Some specialized questions, such as tools and triggers, determine whether the agent should exist and must be explored earlier.
- **assumptions_and_boundaries:** Routing is iterative; findings may return to mechanism classification.
- **revision_decision:** Add a default route-and-return loop rather than a one-way handoff.
- **additional_insight_to_add:** Preserve a single integration owner because multiple adjacent references can each be locally correct while producing a contradictory combined prompt.

### Question 03: When does the default work well?
- **current_section_observation:** No fit criteria show when narrowing reduces context rather than fragments the problem.
- **supporting_reason:** Routing works when the unresolved decision has a clear owner, specialized evidence, and a result that can be summarized back into the charter.
- **counterargument_or_limit:** Closely coupled trigger, tool, and output choices may be harder to split than to reason about together.
- **assumptions_and_boundaries:** Keep coupled contract decisions together and route only genuinely specialized methods or evidence gathering.
- **revision_decision:** Add a coupling test that keeps interdependent trigger, authority, context, and output decisions under one owner.
- **additional_insight_to_add:** Route by the next irreversible decision, not by keyword similarity; this keeps context focused on consequence.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** Generic adjacent labels can produce circular routing or send the reader to another broad reference with the same ambiguity.
- **supporting_reason:** Handoffs fail when no question, input, expected output, owner, or return condition is defined.
- **counterargument_or_limit:** A broad discovery reference can still help when the correct specialization is unknown.
- **assumptions_and_boundaries:** Discovery must end with a narrowed decision or an explicit request for user input.
- **revision_decision:** Add loop detection and blocked-handoff rules requiring a changed question, new evidence, or explicit escalation.
- **additional_insight_to_add:** Track visited routes and stop when the same unresolved condition returns unchanged; repeated routing is not progress.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The seed names reference families but not mechanism alternatives such as command, skill, hook, temporary subagent, persistent agent, or direct parent work.
- **supporting_reason:** Mechanism routing may resolve the task before any adjacent prompt-design reference is needed.
- **counterargument_or_limit:** A user explicitly creating an agent may still benefit from comparison without changing the requested artifact.
- **assumptions_and_boundaries:** Respect explicit user intent while surfacing material tradeoffs and unsafe boundaries.
- **revision_decision:** Include both mechanism alternatives and specialized reference routes.
- **additional_insight_to_add:** An adjacent route should state what context not to carry, preventing broad source dumps from defeating the purpose of narrowing.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** The section omits circular delegation, duplicated work, conflicting owners, context loss, stale links, and routes that silently broaden authority.
- **supporting_reason:** These failures turn modular guidance into coordination overhead and can hide consequential decisions between agents or references.
- **counterargument_or_limit:** Some duplication is useful for independent review of high-risk choices.
- **assumptions_and_boundaries:** Independent review should be deliberate and converge through a named adjudicator.
- **revision_decision:** Add handoff invariants and a conflict-resolution owner.
- **additional_insight_to_add:** Record why the current reference is insufficient; this prevents the adjacent specialist from repeating already completed discovery.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** The three adjacent examples are too vague to demonstrate routing quality.
- **supporting_reason:** A good handoff routes trigger overlap to focused examples with fixtures; a bad handoff says “use the prompt reference”; a borderline handoff delegates architecture debate without a decision owner.
- **counterargument_or_limit:** Stable local reference names may not exist for every category.
- **assumptions_and_boundaries:** A precise question and expected artifact can compensate for a category-based search route.
- **revision_decision:** Add concrete route examples with inputs and return conditions.
- **additional_insight_to_add:** A borderline debate becomes useful when options, constraints, and an adjudication criterion are supplied before delegation.

### Question 08: How can the important claims be verified?
- **current_section_observation:** The seed provides no check that an adjacent route resolved the question or preserved context.
- **supporting_reason:** Verify that the handoff names one decision, includes relevant evidence, excludes unrelated context, returns an artifact, and updates the charter or release status.
- **counterargument_or_limit:** Exploratory routes may legitimately return several candidate questions rather than one answer.
- **assumptions_and_boundaries:** Exploration must still identify the next owner and stop condition.
- **revision_decision:** Add a handoff acceptance checklist and loop detection.
- **additional_insight_to_add:** Measure routing value by reduced unresolved decision surface, not by the number of references or agents consulted.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** It is clear that agent creation overlaps triggering, context, delegation, debate, and verification, but the exact adjacent corpus paths are not listed.
- **supporting_reason:** Decision-category routing remains useful even when filenames change.
- **counterargument_or_limit:** Without exact paths, users may spend time rediscovering candidate references.
- **assumptions_and_boundaries:** Provide stable search terms and prefer a mapped path when the repository has one.
- **revision_decision:** State category-level routes with output expectations and avoid inventing unsupported filenames.
- **additional_insight_to_add:** Confidence in the route can differ from confidence in the specialist answer; record both rather than treating successful handoff as resolved truth.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** Routing is treated as a content-navigation convenience rather than part of agent architecture.
- **supporting_reason:** Persistent handoff patterns define ownership and context boundaries and can become a hidden multi-agent system.
- **counterargument_or_limit:** Most reference navigation remains lightweight and should not be overformalized.
- **assumptions_and_boundaries:** Apply stronger coordination controls only when multiple agents or owners act on shared state.
- **revision_decision:** Add coordination and merge requirements that scale with shared state, authority, and number of owners.
- **additional_insight_to_add:** Repeated adjacent routing around the same task suggests the original agent boundary may be too broad and should be split or replaced, not merely supplied with more prompt text.

## Section 018: Workload Model

### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed calls this an agent workflow operating reference and sets one task, ten source files, three delegated subtasks, and a completion audit, but it does not explain what those boundaries decide.
- **supporting_reason:** A workload model should decide whether one agent can retain ownership and context or whether the task must be narrowed, staged, or split across owners.
- **counterargument_or_limit:** File and subtask counts are weak proxies for semantic complexity, authority, and coupling.
- **assumptions_and_boundaries:** Treat the numeric values as conservative planning guardrails from the seed, not measured universal capacity limits.
- **revision_decision:** Preserve the values, label their epistemic status, and add consequence-based split criteria.
- **additional_insight_to_add:** The true scarce resources are decision coherence, attention, tool authority, and review capacity, not file count alone.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The bounded model lists limits but no operating sequence for staying within them.
- **supporting_reason:** Start with one owned outcome, rank sources by the active question, delegate only independent bounded investigations, checkpoint after each batch, and stop expansion when evidence no longer changes the contract.
- **counterargument_or_limit:** Some repositories require more than ten small source files to establish even one stable convention.
- **assumptions_and_boundaries:** Exceeding a guardrail is acceptable with an explicit reason, revised context plan, and preserved ownership.
- **revision_decision:** Add a default budget process and exception record.
- **additional_insight_to_add:** Budget source spans or decisions where possible, because one enormous file can exceed attention cost while twenty tiny schemas remain manageable.

### Question 03: When does the default work well?
- **current_section_observation:** The seed identifies agent planning, context, delegation, and plugin execution as the primary surface but does not state fit conditions.
- **supporting_reason:** The model works when one owner can define the charter, selected sources answer bounded questions, and delegated subtasks return independent evidence without editing shared state.
- **counterargument_or_limit:** Tightly coupled architecture choices and shared-file edits resist clean parallel decomposition.
- **assumptions_and_boundaries:** Parallelism is appropriate only when inputs, outputs, and ownership are disjoint or merge coordination is explicit.
- **revision_decision:** Add coupling and shared-state tests before delegation.
- **additional_insight_to_add:** Serial work can be faster than fanout when the next question depends on the previous answer, because speculative parallelism creates discarded context and reconciliation cost.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The model says to split when a boundary is exceeded but does not define how a bad split manifests.
- **supporting_reason:** It fails when several agents rewrite one artifact, delegated results conflict without an adjudicator, sources are loaded indiscriminately, or completion audits become too large to review.
- **counterargument_or_limit:** A coordinator and merge queue can safely support larger distributed work when boundaries and checks are mature.
- **assumptions_and_boundaries:** Scaling requires explicit ownership, immutable inputs, return contracts, checkpoints, and integration verification.
- **revision_decision:** Add stop conditions and a distributed-work alternative.
- **additional_insight_to_add:** Split by owned outcome or evidence question, not arbitrary file count, because semantic ownership determines conflict risk.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The seed implies only narrowing or splitting and does not compare staged, summarized, automated, or coordinated alternatives.
- **supporting_reason:** Alternatives include staged serial batches, source summarization, temporary specialists, graph-based context narrowing, deterministic scripts, and coordinated multi-agent execution.
- **counterargument_or_limit:** Summaries can lose provenance, specialists add handoff cost, and orchestration adds control-plane complexity.
- **assumptions_and_boundaries:** Choose the least complex mechanism that preserves evidence and ownership for the next decision.
- **revision_decision:** Add an escalation ladder from narrowing through distributed coordination.
- **additional_insight_to_add:** Automate deterministic extraction before delegating judgment; this reduces duplicated reading and leaves agent attention for synthesis.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** The seed warns generally that bad guidance compounds but omits context dumping, source-count gaming, hidden subtasks, retry fanout, and audit overload.
- **supporting_reason:** These behaviors can stay within nominal counts while exceeding practical attention and ownership capacity.
- **counterargument_or_limit:** Detailed resource accounting can become overhead for small tasks.
- **assumptions_and_boundaries:** Track only dimensions that influence split, authority, cost, or release decisions.
- **revision_decision:** Add pressure signals and stop rules rather than exhaustive accounting.
- **additional_insight_to_add:** Include unresolved-decision count in checkpoints; a growing count despite more sources indicates context expansion is not producing convergence.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** The workload table has no operational examples.
- **supporting_reason:** A good run loads three targeted sources and delegates two independent read-only checks; a bad run sends ten overlapping files to three agents; a borderline run exceeds ten sources because they are small and tightly indexed.
- **counterargument_or_limit:** Counts alone cannot make the examples good or bad.
- **assumptions_and_boundaries:** Explain ownership, dependency, and review cost in every example.
- **revision_decision:** Add examples that show why the same count can have different outcomes.
- **additional_insight_to_add:** A justified exception should state what was excluded and how the owner will detect context loss or contradiction.

### Question 08: How can the important claims be verified?
- **current_section_observation:** The model's boundaries and performance implications have no empirical evidence or measurement method.
- **supporting_reason:** Record source count and size, decisions resolved, delegated tasks, conflicts, retries, wall time, reviewer effort, and completion status across comparable runs.
- **counterargument_or_limit:** Small samples and changing tasks prevent universal capacity conclusions.
- **assumptions_and_boundaries:** Use measurements to tune local guardrails and report uncertainty rather than asserting a general optimum.
- **revision_decision:** Add an operational measurement packet and exception review.
- **additional_insight_to_add:** Measure discarded work and merge correction, because fast parallel completion can still be slower end to end after reconciliation.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The primary usage and artifact requirements are coherent, but the ten-source and three-subtask limits lack stated provenance or measured support.
- **supporting_reason:** Conservative bounds can prevent uncontrolled fanout even when their exact values are not universal.
- **counterargument_or_limit:** Presenting them as capacity facts would be unsupported precision.
- **assumptions_and_boundaries:** Label them as starting guardrails subject to local evidence and consequence.
- **revision_decision:** Retain the numbers with an explicit uncertainty and override protocol.
- **additional_insight_to_add:** Confidence in one-owner-per-artifact is stronger than confidence in count thresholds because shared-write conflicts have a direct causal mechanism.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The model focuses on completing one run and not on how scale changes prompt architecture.
- **supporting_reason:** Repeatedly exceeding workload boundaries may mean the proposed agent owns too many decisions or needs deterministic tooling and a coordinator architecture.
- **counterargument_or_limit:** Occasional large tasks do not necessarily justify permanent decomposition.
- **assumptions_and_boundaries:** Redesign after recurring, measured pressure rather than one exceptional case.
- **revision_decision:** Add architectural feedback from workload observations into charter revision.
- **additional_insight_to_add:** Capacity pressure is diagnostic: source overload points to context indexing, merge conflict points to ownership, and retry fanout points to unclear failure classification.

## Section 019: Reliability Target

### Question 01: What decision does this reference help make?
- **current_section_observation:** The table sets source-boundary, decision-sample, unsupported-claim, and recovery-path thresholds, but it does not state whether they are observed results, release policy, or aspirational goals.
- **supporting_reason:** Reliability targets should decide the approved invocation and authority level and identify which failures block release or require narrowing.
- **counterargument_or_limit:** A few numeric thresholds cannot capture consequence, model variability, or task diversity.
- **assumptions_and_boundaries:** Treat seed values as explicit policy targets for this reference, not as historical performance evidence or universal standards.
- **revision_decision:** Preserve all thresholds, define denominators and evidence, and add consequence-based interpretation.
- **additional_insight_to_add:** Reliability must be decomposed into routing, authority, evidence, recovery, and task outcome because a single aggregate can hide catastrophic failure.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The seed lists review methods but no release progression when a target is unmet.
- **supporting_reason:** Begin with structural and read-only manual use, collect labeled scenarios, and expand proactive or write authority only as the relevant targets and failure paths pass.
- **counterargument_or_limit:** Some agents require write capability to be meaningfully evaluated.
- **assumptions_and_boundaries:** Use reversible sandboxed or test-environment writes before production authority.
- **revision_decision:** Add staged reliability levels tied to observed evidence.
- **additional_insight_to_add:** An unmet target should reduce the capability connected to that target rather than produce an undifferentiated “unreliable” label.

### Question 03: When does the default work well?
- **current_section_observation:** The decision-accuracy sample assumes reviewer-labeled tasks and stable categories but does not state those prerequisites.
- **supporting_reason:** Targets work when fixtures are representative, labels are consistent, versions are recorded, and failure severity is reviewed separately from counts.
- **counterargument_or_limit:** Low-volume or novel agents may not yield twenty comparable uses.
- **assumptions_and_boundaries:** Use a smaller qualitative review without claiming the 18-of-20 sample target has been met.
- **revision_decision:** Add sample qualification rules and an insufficient-evidence status for low-volume or reviewer-disputed cases.
- **additional_insight_to_add:** Reviewer disagreement should block precision claims and trigger output or route-contract clarification before more samples are collected.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** A system could meet 18 of 20 routing decisions while the two failures are destructive, or preserve labels while citing irrelevant sources.
- **supporting_reason:** Threshold compliance without semantic adequacy or consequence weighting creates false assurance.
- **counterargument_or_limit:** Simple strict thresholds are easy to audit and communicate.
- **assumptions_and_boundaries:** Retain strict checks but supplement them with severity, relevance, and failure-class review.
- **revision_decision:** Add hard-stop conditions that override aggregate passes.
- **additional_insight_to_add:** One unexplained prohibited action or fabricated high-consequence claim should block authority expansion regardless of average success.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The table favors exact policy thresholds and sampled reviewer decisions but omits confidence intervals, risk-weighted gates, shadow mode, and service-level objectives.
- **supporting_reason:** Risk-weighted gates protect severe boundaries, shadow mode measures routing safely, and statistical intervals express sample uncertainty.
- **counterargument_or_limit:** Formal statistics can imply rigor unsupported by heterogeneous small samples.
- **assumptions_and_boundaries:** Use simple counts with denominators and bounded interpretation unless sample design justifies more.
- **revision_decision:** Add qualitative and staged alternatives without replacing the seed targets.
- **additional_insight_to_add:** The right tradeoff is often lower autonomy with better evidence, not relaxing a target to preserve a desired release date.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** The table omits sample selection, duplicate cases, version mixing, reviewer bias, severity masking, and target gaming.
- **supporting_reason:** These defects can satisfy formal thresholds without improving agent behavior.
- **counterargument_or_limit:** Heavy measurement governance can exceed the risk of a small internal read-only agent.
- **assumptions_and_boundaries:** Measurement rigor scales with authority and consequence.
- **revision_decision:** Add minimal data-quality rules and severe-failure overrides.
- **additional_insight_to_add:** Preserve failed and borderline cases in a regression set so future tuning cannot quietly redefine them out of the denominator.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** The seed provides target values but no sample report showing denominator, severity, version, or release consequence.
- **supporting_reason:** A good report shows numerator, denominator, versions, severity, and release action; a bad report says “90 percent reliable”; a borderline report has 18 of 20 routes but one prohibited tool attempt.
- **counterargument_or_limit:** Example numbers may be mistaken for general acceptance criteria beyond the explicit seed policy.
- **assumptions_and_boundaries:** Mark examples as interpretation aids and preserve local policy ownership.
- **revision_decision:** Add examples where aggregate targets pass, fail, or are overridden by a severe authority boundary event.
- **additional_insight_to_add:** Include an insufficient-sample example to normalize honest uncertainty instead of filling missing evidence with confident judgment.

### Question 08: How can the important claims be verified?
- **current_section_observation:** Evidence methods are listed per row but lack fixture labeling, version capture, and independent audit.
- **supporting_reason:** Verify claim provenance, route labels, denied capabilities, output evidence, recovery paths, reviewer agreement, and replay against a held-out set.
- **counterargument_or_limit:** Independent review of every low-risk run is impractical.
- **assumptions_and_boundaries:** Independently sample high-risk and changed behavior while automating deterministic checks.
- **revision_decision:** Add a reliability evidence packet and audit cadence.
- **additional_insight_to_add:** Test recovery using injected failures rather than waiting for production incidents to reveal whether escalation language works.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The numeric targets are explicit seed facts, but no current sample results demonstrate that this or any agent meets them.
- **supporting_reason:** Policy targets can still guide verification and release discipline without being historical claims.
- **counterargument_or_limit:** Their appropriateness for every agent type remains unproven.
- **assumptions_and_boundaries:** Owners may strengthen or supplement targets based on local risk but should not silently weaken or report them as achieved.
- **revision_decision:** Label status as target, observed, unmet, or insufficient evidence.
- **additional_insight_to_add:** Confidence should be reported per dimension because high source traceability can coexist with untested routing or recovery.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The table presents reliability as a final evaluation rather than a control on authority evolution.
- **supporting_reason:** Dimension-specific evidence can govern when an agent moves from manual to proactive, advisory to write-enabled, or active to retired.
- **counterargument_or_limit:** Capability staging adds operational complexity and may slow delivery.
- **assumptions_and_boundaries:** Staging is most valuable when authority and reversibility differ materially.
- **revision_decision:** Tie each reliability dimension to a capability gate and downgrade path.
- **additional_insight_to_add:** Reliability debt accumulates when authority grows faster than evidence; track the gap explicitly rather than treating tests as a one-time launch requirement.

## Section 020: Failure Mode Table

### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed lists source drift, generic advice, context loss, and tool fanout with mitigations, but it does not classify detection, severity, containment, or release consequence.
- **supporting_reason:** A failure registry should decide what to stop immediately, what can retry, what requires narrower authority, and who owns recovery.
- **counterargument_or_limit:** A universal severity table can misclassify failures whose consequence depends on the target workflow.
- **assumptions_and_boundaries:** Classify severity from actual authority, data, reversibility, and ownership while retaining default responses.
- **revision_decision:** Preserve the four modes and add trigger, signal, containment, recovery, and prevention fields plus missing operational modes.
- **additional_insight_to_add:** Separate failure cause from observed symptom because the same unsupported output can arise from stale evidence, missing context, or an ambiguous contract.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** Each row offers one mitigation but no shared incident sequence.
- **supporting_reason:** Detect, contain, classify, preserve evidence, recover through a bounded owner, verify the fix, and add a regression fixture before restoring authority.
- **counterargument_or_limit:** Low-impact formatting defects may not justify incident-style handling.
- **assumptions_and_boundaries:** Scale formality to consequence while preserving the same causal discipline.
- **revision_decision:** Add a common response protocol and distinguish warning from hard-stop failures.
- **additional_insight_to_add:** Containment should precede diagnosis when continued execution can mutate shared state or fan out more work.

### Question 03: When does the default work well?
- **current_section_observation:** The listed failures are observable only if source status, plan checkpoints, tool counts, and verification results are recorded.
- **supporting_reason:** The protocol works when the agent emits bounded statuses and the owner can inspect inputs, actions, evidence, and version.
- **counterargument_or_limit:** Privacy or context limits may prevent retaining full traces.
- **assumptions_and_boundaries:** Store minimal structured evidence and redact sensitive content rather than logging raw prompts indiscriminately.
- **revision_decision:** Add observability prerequisites that preserve reproducible failure evidence while minimizing sensitive context retention.
- **additional_insight_to_add:** Failure evidence should be sufficient to reproduce the decision class, not necessarily the user's complete data.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** Fixed mitigations can fail when the agent lacks authority to refresh evidence, rollback state, or contact the named owner.
- **supporting_reason:** A recovery plan that cannot execute in the active host creates false assurance.
- **counterargument_or_limit:** The agent can still return a blocked result and transfer recovery to the parent.
- **assumptions_and_boundaries:** Every mitigation must distinguish agent action from parent or human action.
- **revision_decision:** Add ownership and capability checks to each recovery path.
- **additional_insight_to_add:** If no actor can perform the named recovery, the charter is incomplete and the affected capability should not be enabled.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The table favors refresh, blocking, checkpointing, and fanout caps but omits read-only fallback, manual invocation, rollback, circuit breakers, and retirement.
- **supporting_reason:** Different containment tools trade autonomy, availability, and safety according to failure class.
- **counterargument_or_limit:** Too many recovery branches can make prompt behavior unpredictable.
- **assumptions_and_boundaries:** Define a small ordered recovery ladder and reserve exceptional paths for the parent or owner.
- **revision_decision:** Add an ordered recovery ladder spanning fallback, degraded authority, compensation, escalation, and retirement.
- **additional_insight_to_add:** Retirement is appropriate when repeated failures reveal an invalid ownership boundary rather than a fixable prompt clause.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Missing modes include overtrigger, undertrigger, excessive authority, fabricated evidence, ambiguous completion, retry loops, delegation loops, output overflow, and owner loss.
- **supporting_reason:** These can cause harm even when sources are fresh and context remains intact.
- **counterargument_or_limit:** A large table can duplicate anti-pattern, retry, and observability sections.
- **assumptions_and_boundaries:** Keep this section as the integrated operational registry and cross-reference specialized controls conceptually.
- **revision_decision:** Add high-impact modes while avoiding exhaustive host-specific errors.
- **additional_insight_to_add:** Include clean-result fabrication pressure, where a reviewer persona invents findings because the output contract lacks an acceptable no-issue state.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** The seed supplies conditions and mitigations but no incident examples.
- **supporting_reason:** A good response stops write authority after a denied-boundary event; a bad response retries with broader tools; a borderline response refreshes a source but cannot reproduce the original route.
- **counterargument_or_limit:** Incident examples can expose implementation details not common across hosts.
- **assumptions_and_boundaries:** Focus on invariant state transitions and ownership, not product-specific commands.
- **revision_decision:** Add short response examples and expected status.
- **additional_insight_to_add:** A borderline recovery should remain constrained until both cause and regression path are understood, even if a subsequent run succeeds.

### Question 08: How can the important claims be verified?
- **current_section_observation:** The seed prescribes mitigations but supplies no injected failures demonstrating containment, recovery, or post-fix regression.
- **supporting_reason:** Inject stale evidence, missing context, tool denial, overlap, persistent verification failure, and unavailable escalation, then inspect stop and recovery outcomes.
- **counterargument_or_limit:** Some production incidents cannot be safely reproduced exactly.
- **assumptions_and_boundaries:** Simulate the decision boundary with reversible fixtures and document residual risk.
- **revision_decision:** Add failure-injection coverage and post-fix replay requirements.
- **additional_insight_to_add:** Verify containment separately from successful recovery because stopping further harm can work even when the task remains incomplete.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The causal plausibility of the four seed failures is strong, but no frequency, severity distribution, or mitigation success data is provided.
- **supporting_reason:** They are defensible review defaults because their triggers and consequences are concrete.
- **counterargument_or_limit:** Ranking them as universally dominant would exceed the evidence.
- **assumptions_and_boundaries:** Treat the registry as a locally useful taxonomy that should evolve from observed incidents and near misses.
- **revision_decision:** Avoid prevalence claims and add evidence-status language.
- **additional_insight_to_add:** Record near misses where a gate blocked a failure; prevention evidence helps prioritize controls without waiting for user harm.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** Failures are treated as isolated events rather than signals about agent architecture and portfolio health.
- **supporting_reason:** Recurrent overlap, context loss, or fanout suggests a bad boundary, insufficient indexing, or missing coordinator rather than a wording defect.
- **counterargument_or_limit:** One incident should not trigger broad redesign without causal evidence.
- **assumptions_and_boundaries:** Look for repeated classified patterns across versions and comparable tasks.
- **revision_decision:** Add architectural escalation criteria after repeated failures.
- **additional_insight_to_add:** Couple each failure mode to a downgrade path so the system can remain useful at reduced authority while the deeper cause is investigated.

## Section 021: Retry Backpressure Guidance

### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed distinguishes transient, stale evidence, missing context, and contradiction, limits one stale-evidence retry, and advises checkpoints and ownership, but it lacks a complete retry decision table.
- **supporting_reason:** This section should decide whether to retry, wait, refresh, narrow, return blocked, rollback, or escalate after a failed agent step.
- **counterargument_or_limit:** Error taxonomies vary by tool and host, so one table cannot enumerate every failure.
- **assumptions_and_boundaries:** Use invariant classes based on whether the same input and authority can plausibly succeed without a decision change.
- **revision_decision:** Preserve seed rules and add classification, preconditions, budgets, state safety, and terminal outcomes.
- **additional_insight_to_add:** A retry is justified by new success conditions, not by optimism; the agent should name what changed before repeating work.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The seed permits retry after classification but does not require idempotency or preserved state.
- **supporting_reason:** Default to no retry until the failure is classified, state effects are known, the operation is idempotent or safely compensated, and a bounded budget remains.
- **counterargument_or_limit:** A harmless read timeout may be retried immediately with minimal ceremony.
- **assumptions_and_boundaries:** Fast-path retry applies only to clearly transient, side-effect-free operations.
- **revision_decision:** Add a preflight and one-retry default with explicit exceptions.
- **additional_insight_to_add:** Retry budgets should be shared across nested tools and delegates so fanout cannot multiply a nominal one-retry rule.

### Question 03: When does the default work well?
- **current_section_observation:** The guidance assumes failures can be classified and sessions can checkpoint.
- **supporting_reason:** It works when tools expose status, actions have visible side effects, the agent can persist progress, and escalation ownership is known.
- **counterargument_or_limit:** Opaque external systems may not reveal whether a timed-out write succeeded.
- **assumptions_and_boundaries:** Ambiguous write outcome is not transient; reconcile remote state before retrying.
- **revision_decision:** Add uncertainty-of-effect as a hard stop category.
- **additional_insight_to_add:** Read-after-write reconciliation can convert ambiguous outcome into evidence, but only if the read is authoritative and safe.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** Backpressure can reduce throughput unnecessarily when failures are isolated and harmless, or it can fail if new work continues through another agent.
- **supporting_reason:** Controls must apply at the ownership boundary and match consequence, not merely one local loop.
- **counterargument_or_limit:** Global circuit breakers can block unrelated work and reduce availability.
- **assumptions_and_boundaries:** Scope backpressure to the affected source, capability, artifact, or dependency while preserving disjoint safe work.
- **revision_decision:** Add scoped circuit-breaker behavior that halts dependent work while preserving disjoint safe evidence collection.
- **additional_insight_to_add:** A blocked dependency should prevent dependent generation but need not stop independent evidence collection that cannot mutate affected state.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** Alternatives are limited to retry or escalation.
- **supporting_reason:** Waiting with jitter, refreshing evidence, requesting input, using fallback tools, degrading authority, compensating state, or returning partial results each fits a different class.
- **counterargument_or_limit:** Multiple fallbacks can hide persistent service or design failures and complicate reproducibility.
- **assumptions_and_boundaries:** Fallbacks must preserve the same contract or explicitly narrow the result and verification status.
- **revision_decision:** Add an ordered response matrix and forbid silent semantic substitution.
- **additional_insight_to_add:** A fallback that changes evidence quality should change output confidence and downstream release decisions.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** The seed omits non-idempotent retries, retry storms, broadened permissions, reset budgets after delegation, lost checkpoints, and success after partial duplicate effects.
- **supporting_reason:** These failures turn recovery into additional harm and make audit trails misleading.
- **counterargument_or_limit:** Not every read-only workflow needs extensive compensation logic.
- **assumptions_and_boundaries:** Apply strong state controls to writes and external actions; keep read-only guidance simpler.
- **revision_decision:** Add high-impact retry anti-patterns and shared-budget rules.
- **additional_insight_to_add:** Never use broader authority as a retry strategy; capability changes require a new approved plan and verification level.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** The seed has no scenario showing how classification determines retry, backpressure, blocked status, or escalation.
- **supporting_reason:** A good case retries one read timeout; a bad case repeats an uncertain external write; a borderline case refreshes stale evidence once but still encounters contradiction.
- **counterargument_or_limit:** Retry signals and state semantics vary by host, so examples must assert invariant ownership and effects.
- **assumptions_and_boundaries:** Focus examples on state knowledge, changed conditions, and terminal status.
- **revision_decision:** Add examples for transient, ambiguous-effect, and contradiction classes.
- **additional_insight_to_add:** A successful retry record should still include the original failure and changed condition so reliability review can detect recurring instability.

### Question 08: How can the important claims be verified?
- **current_section_observation:** The guidance recommends limits but has no test method for budgets, checkpoints, or circuit breakers.
- **supporting_reason:** Inject repeated timeouts, stale sources, missing inputs, contradictions, and ambiguous writes; inspect call counts, state, status, escalation, and resume behavior.
- **counterargument_or_limit:** Ambiguous production side effects may require mocks or sandbox services that differ from reality.
- **assumptions_and_boundaries:** Validate invariant state transitions and retain residual integration risk.
- **revision_decision:** Add failure-injection and resume tests with exact budget evidence.
- **additional_insight_to_add:** Test nested delegation to ensure a parent and child cannot each consume a full retry budget for the same failing dependency.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The one bounded stale-evidence retry is an explicit seed policy, while optimal timing, jitter, and budgets for other classes are unspecified.
- **supporting_reason:** Conservative bounded retries and explicit escalation have clear causal safety benefits.
- **counterargument_or_limit:** Overly strict limits can reduce availability for genuinely transient systems.
- **assumptions_and_boundaries:** Tune local transient budgets from measured dependency behavior without changing authority or hiding failures.
- **revision_decision:** Preserve the one-retry seed rule and label other timing choices as local policy.
- **additional_insight_to_add:** Report reliability separately from recovery latency; faster retries do not imply safer or more correct recovery.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** Retry is framed as task-level recovery rather than feedback about source, tool, and architecture quality.
- **supporting_reason:** Repeated classified failures reveal unstable dependencies, stale evidence pipelines, unclear ownership, or non-idempotent interfaces.
- **counterargument_or_limit:** Occasional transient failures are normal and need not trigger redesign.
- **assumptions_and_boundaries:** Aggregate by failure class, dependency, version, and consequence before architectural action.
- **revision_decision:** Add operational feedback and retirement or redesign triggers.
- **additional_insight_to_add:** Backpressure protects context as well as systems: stopping speculative work prevents the agent from filling its attention with outputs derived from a failed premise.

## Section 022: Observability Checklist

### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed lists loaded sources, proof, latency percentiles, tool counts, delegation, retry, outcomes, and compact evidence, but it does not state which operational questions those records answer.
- **supporting_reason:** Observability should decide whether a run routed correctly, respected authority, used relevant context, produced checkable evidence, recovered safely, and remains worth maintaining.
- **counterargument_or_limit:** Logging every listed dimension can expose sensitive data and create more review burden than the agent saves.
- **assumptions_and_boundaries:** Collect the minimum structured event needed for a named decision and avoid raw transcript capture by default.
- **revision_decision:** Preserve all seed observations, organize them around decisions, and add privacy, retention, and correlation rules.
- **additional_insight_to_add:** Observability quality is measured by whether an owner can act on a failure, not by event volume.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The checklist has no canonical event schema or sampling rule.
- **supporting_reason:** Record run and version identity, expected and actual route, context manifest, capabilities used, verification outcomes, result status, recovery, reviewer decision, and residual uncertainty.
- **counterargument_or_limit:** Full per-run records may be unnecessary for deterministic low-risk agents.
- **assumptions_and_boundaries:** Sample routine successes while retaining complete high-risk, changed-version, failure, and authority events.
- **revision_decision:** Add a minimal event packet and risk-based sampling.
- **additional_insight_to_add:** Correlate parent and specialist run identifiers so a delegated result can be traced without merging their entire contexts.

### Question 03: When does the default work well?
- **current_section_observation:** The seed assumes source and tool activity can be recorded and reviewed.
- **supporting_reason:** It works when the host exposes stable identifiers, tool outcomes, timestamps, and versions, and when reviewers share result classifications.
- **counterargument_or_limit:** Some hosts provide only coarse logs or prohibit storing prompts and outputs.
- **assumptions_and_boundaries:** Use local counters, redacted manifests, hashes, and explicit unknowns when detailed telemetry is unavailable.
- **revision_decision:** Add a degraded-observability status with redacted manifests, local counters, hashes, and explicit unknown fields.
- **additional_insight_to_add:** Missing telemetry should narrow confidence and authority rather than encourage inferred success from a polished final message.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** Percentile latency and raw tool details can be meaningless or harmful for low-volume documentation agents.
- **supporting_reason:** Percentiles require enough comparable samples, and detailed payload logs can leak repository, user, or credential data.
- **counterargument_or_limit:** Even a few wall-time observations can expose gross regressions when interpreted individually.
- **assumptions_and_boundaries:** Report raw samples or ranges for small populations and reserve percentiles for qualified repeated runs.
- **revision_decision:** Bound percentile claims and add data-minimization rules.
- **additional_insight_to_add:** Reviewer decision time may be the relevant performance measure for documentation agents, while runtime latency matters more for interactive routing.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The seed favors structured counts and summaries but omits traces, metrics, audit logs, sampled artifacts, and synthetic probes as distinct tools.
- **supporting_reason:** Metrics show trends, traces explain one run, audit logs establish authority, sampled artifacts assess quality, and probes detect regressions without user data.
- **counterargument_or_limit:** Using separate traces, metrics, and audit systems increases correlation, retention, and access-control complexity.
- **assumptions_and_boundaries:** Choose the least invasive signal that resolves the operational question and use shared identifiers.
- **revision_decision:** Add signal-type tradeoffs and a decision-first selection rule.
- **additional_insight_to_add:** Synthetic negative-routing probes can monitor portfolio overlap without retaining real user requests.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** The checklist omits missing denominators, version mixing, high-cardinality labels, secret leakage, sampling only successes, and telemetry that cannot distinguish blocked from failed.
- **supporting_reason:** These defects produce misleading conclusions or security risk.
- **counterargument_or_limit:** Strong redaction can remove context needed for diagnosis.
- **assumptions_and_boundaries:** Preserve decision metadata and provenance while minimizing content payloads.
- **revision_decision:** Add data quality, status vocabulary, and privacy review checks.
- **additional_insight_to_add:** Record intentionally skipped sources without their sensitive contents so context selection remains auditable without duplication.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** The seed describes preferred summaries but gives no event examples.
- **supporting_reason:** A good event records scoped sources, route, tool categories, checks, status, and owner; a bad event stores a full transcript and says success; a borderline event reports p99 from six runs.
- **counterargument_or_limit:** Event schemas differ across hosts, so the reference should require semantic decisions rather than field names.
- **assumptions_and_boundaries:** Demonstrate semantic requirements rather than mandate one serialization format.
- **revision_decision:** Add compact event examples that connect recorded route, authority, recovery, and evidence to a maintenance decision.
- **additional_insight_to_add:** A useful event includes the decision that telemetry changed, preventing passive dashboards with no maintenance consequence.

### Question 08: How can the important claims be verified?
- **current_section_observation:** The checklist does not verify telemetry completeness, redaction, correlation, or actionability.
- **supporting_reason:** Inject known route, tool, retry, blocked, and escalation outcomes and confirm records capture them without sensitive payloads.
- **counterargument_or_limit:** Synthetic fixtures may not exercise every host logging path.
- **assumptions_and_boundaries:** Combine synthetic checks with periodic sampled audit under appropriate access controls.
- **revision_decision:** Add observability contract tests and retention review.
- **additional_insight_to_add:** Verify that deletion and retention policies operate, because data minimization is not satisfied by collection-time redaction alone.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The listed dimensions are relevant operational signals, but no evidence establishes that all are available, necessary, or currently measured.
- **supporting_reason:** They map directly to context, authority, performance, recovery, and completion decisions in this reference.
- **counterargument_or_limit:** Optimal sampling, retention, and latency summaries depend on host volume and risk.
- **assumptions_and_boundaries:** Label unavailable fields and choose local policy with privacy review.
- **revision_decision:** Distinguish required semantic evidence from optional implementation metrics.
- **additional_insight_to_add:** Confidence in an agent outcome and confidence in telemetry completeness should be reported separately.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** Observability is framed as proving one reference run rather than maintaining an agent portfolio.
- **supporting_reason:** Aggregated route, authority, and owner signals can reveal overlap, unused agents, repeated blocked states, and reliability debt.
- **counterargument_or_limit:** Portfolio analytics can encourage optimization for usage rather than user value.
- **assumptions_and_boundaries:** Interpret telemetry with qualitative outcome review and consequence.
- **revision_decision:** Add portfolio analysis for overlap, ownerless evidence, recurring blocks, and retirement without rewarding raw invocation volume.
- **additional_insight_to_add:** An agent with no recent justified routes and no active owner is a retirement candidate even if its historical success records are clean.

## Section 023: Performance Verification Method

### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed requires budgets, a resumable journal, a measurement packet, and reviewer-identifiable next actions, but it does not distinguish workflow performance from agent correctness or reliability.
- **supporting_reason:** Performance verification should decide whether an agent reduces end-to-end time or attention without degrading routing, evidence, authority, recovery, or user control.
- **counterargument_or_limit:** Some agents exist for quality or risk reduction and may intentionally take longer than direct execution.
- **assumptions_and_boundaries:** Define performance relative to the user outcome and alternative mechanism, not raw speed alone.
- **revision_decision:** Preserve seed measures and add baseline, workload, quality guardrail, and decision rules.
- **additional_insight_to_add:** Reviewer decision time and rework can dominate wall time for documentation and analysis workflows.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The seed names input size and percentiles but no benchmark protocol.
- **supporting_reason:** Establish a comparable baseline, freeze or classify fixtures, warm or cold conditions, versions, budgets, quality gates, and repeated samples before comparing.
- **counterargument_or_limit:** Formal benchmarking may be disproportionate for a rarely used internal agent.
- **assumptions_and_boundaries:** Use lightweight paired case review for low-volume agents and stronger sampling for latency-sensitive repeated workflows.
- **revision_decision:** Add a proportional benchmark method and minimum record.
- **additional_insight_to_add:** Compare the complete user journey, including clarification, retries, reviewer rework, and handoff, rather than timing only model execution.

### Question 03: When does the default work well?
- **current_section_observation:** The method assumes runs can be compared and source/tool counts reflect work.
- **supporting_reason:** It works when task class, input scope, agent and host versions, verification requirements, and output criteria are stable enough to compare.
- **counterargument_or_limit:** Novel or heterogeneous tasks can make averages and percentiles misleading.
- **assumptions_and_boundaries:** Segment results or use qualitative case analysis when workloads differ materially.
- **revision_decision:** Add fixture-equivalence criteria and segment results by task class, input scope, version, and environment.
- **additional_insight_to_add:** A stable synthetic fixture reveals regressions, while sampled real tasks test external validity; both are useful for different claims.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** Tool-call and context-file budgets may encourage gaming, and percentile claims can exceed sample support.
- **supporting_reason:** An agent can lower counts by skipping evidence or batching opaque actions, producing a faster but less trustworthy workflow.
- **counterargument_or_limit:** Budgets still expose runaway fanout and context growth.
- **assumptions_and_boundaries:** Treat budgets as guardrails paired with quality and coverage, not optimization objectives.
- **revision_decision:** Add anti-gaming checks and sample adequacy rules.
- **additional_insight_to_add:** A performance pass is invalid if the optimized run changes the decision quality or approved authority level.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The seed centers timing and counts but omits throughput, cost, attention, queue delay, and time-to-recovery.
- **supporting_reason:** Different workflows value interactive latency, batch throughput, reviewer effort, token or tool cost, or recovery speed.
- **counterargument_or_limit:** Tracking every dimension dilutes focus and increases instrumentation burden.
- **assumptions_and_boundaries:** Select metrics from the user journey and consequence rather than collect a universal set.
- **revision_decision:** Add metric-selection guidance based on the user's bottleneck, plus explicit quality and cost tradeoffs.
- **additional_insight_to_add:** Context offloading can reduce active tokens while increasing lookup latency; evaluate the combined effect on decision time and evidence quality.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Missing baseline, changed fixtures, cold-start differences, caching, concurrency, failed-run exclusion, and version mixing are unaddressed.
- **supporting_reason:** These confounders can create false performance improvements or hide tail failure cost.
- **counterargument_or_limit:** Perfect environment control is unnecessary for directional internal decisions.
- **assumptions_and_boundaries:** Record major conditions and bound conclusions to the observed environment.
- **revision_decision:** Add benchmark hygiene and require inclusion of retries and failures.
- **additional_insight_to_add:** Excluding blocked or failed runs systematically understates end-to-end cost and should be prohibited unless reported separately.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** The seed states pass and fail conditions abstractly without a measured example.
- **supporting_reason:** A good report compares equivalent tasks and includes quality; a bad report claims p99 from a tiny mixed sample; a borderline report saves time but raises reviewer corrections.
- **counterargument_or_limit:** Example figures can be mistaken for target thresholds.
- **assumptions_and_boundaries:** Use qualitative examples or explicitly illustrative values.
- **revision_decision:** Add interpretation examples without unsupported universal numbers.
- **additional_insight_to_add:** The borderline case should trigger a tradeoff decision, not automatic rejection, when the user's primary goal is risk reduction.

### Question 08: How can the important claims be verified?
- **current_section_observation:** The required measurement packet is listed but no calculation or result validation is specified.
- **supporting_reason:** Verify raw sample completeness, denominators, fixture equivalence, version attribution, timing boundaries, quality gates, and reproducible summaries.
- **counterargument_or_limit:** Reviewer-time measurements may be subjective or interrupt normal work.
- **assumptions_and_boundaries:** Use consistent definitions and sampled observation, reporting uncertainty.
- **revision_decision:** Add a measurement audit and focused regression protocol.
- **additional_insight_to_add:** Preserve raw per-run results behind summaries so percentile and average claims can be recomputed after classification changes.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The seed defines desired measures and pass logic but provides no current results or validated thresholds.
- **supporting_reason:** Its focus on budgets, journals, next action, and stop condition is operationally relevant.
- **counterargument_or_limit:** Claims about faster workflows remain unproven until comparable runs are observed.
- **assumptions_and_boundaries:** Present the section as a method, not evidence of achieved performance.
- **revision_decision:** State evidence status and prohibit achievement language without a measurement record.
- **additional_insight_to_add:** Confidence in efficiency and confidence in correctness should be reported independently before a combined release decision.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** Performance is treated as a verification endpoint rather than a diagnostic of agent boundaries.
- **supporting_reason:** High handoff cost, context reload, retry time, or reviewer reconstruction can reveal poor decomposition even when task logic is sound.
- **counterargument_or_limit:** Some overhead is the necessary cost of independent review or safer authority.
- **assumptions_and_boundaries:** Interpret overhead against the user goal and avoided risk.
- **revision_decision:** Add boundary-diagnosis and explicit quality-versus-speed tradeoff guidance.
- **additional_insight_to_add:** Optimize the bottleneck that controls the user's next decision; reducing model latency is irrelevant when evidence review dominates completion.

## Section 024: Scale Boundary Statement

### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed says the reference stops being sufficient across multiple systems, ownership boundaries, unbounded discovery, or production traffic without an SLO, then recommends splitting and graph narrowing.
- **supporting_reason:** The section should decide when one-agent prompt design must become explicit system architecture, coordination, and operational reliability work.
- **counterargument_or_limit:** A single agent can call several systems safely when actions are read-only, well-bounded, and owned by one team.
- **assumptions_and_boundaries:** Scale is driven by coupling, authority, failure independence, and ownership, not system count alone.
- **revision_decision:** Preserve seed boundaries and add diagnostic questions plus migration options.
- **additional_insight_to_add:** The reference can still define each specialist charter after architecture scales, but it no longer governs the whole system by itself.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The seed says to split by theme and preserve one verification owner but does not define the target architecture.
- **supporting_reason:** Keep one coordinator for user intent and integration, assign one owner per specialist outcome or artifact, use bounded message contracts, and verify cross-boundary behavior separately.
- **counterargument_or_limit:** A coordinator can become a bottleneck or single point of failure.
- **assumptions_and_boundaries:** Use a coordinator only for decisions requiring integration; allow disjoint work to proceed independently with merge rules.
- **revision_decision:** Add a default coordinator-specialist pattern with ownership and failure isolation.
- **additional_insight_to_add:** Verification ownership should follow the end-to-end user outcome, while component owners retain local gate responsibility.

### Question 03: When does the default work well?
- **current_section_observation:** The seed identifies distributed execution but does not state when splitting actually reduces complexity.
- **supporting_reason:** It works when specialists have stable inputs, distinct authority, independent failure domains, and outputs that a coordinator can reconcile without sharing mutable state.
- **counterargument_or_limit:** Highly coupled tasks can create more messages and inconsistent local decisions after splitting.
- **assumptions_and_boundaries:** Keep tightly coupled decisions under one owner until a stable interface exists.
- **revision_decision:** Add interface-readiness and coupling tests before decomposition.
- **additional_insight_to_add:** A split is successful when it reduces the context and decision surface each owner must hold, not merely when more agents run concurrently.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The seed warns against parallel rewrites but omits distributed transactions, partial failure, inconsistent policy, queue overload, and cross-system rollback.
- **supporting_reason:** These problems require operational controls beyond prompt wording.
- **counterargument_or_limit:** Not every multi-system read requires transactions or production-grade orchestration.
- **assumptions_and_boundaries:** Control depth scales with state mutation, user traffic, and recovery consequence.
- **revision_decision:** Add read-only versus mutating boundaries and explicit stop conditions.
- **additional_insight_to_add:** If no owner can describe compensation after a partial cross-system action, the workflow should remain advisory.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The only alternatives are splitting and source-graph narrowing.
- **supporting_reason:** Alternatives include deterministic orchestration, queues, workflow engines, transactional boundaries, human approval, batch processing, and keeping one sequential agent.
- **counterargument_or_limit:** Infrastructure can exceed the value or frequency of the task.
- **assumptions_and_boundaries:** Choose the simplest architecture that meets reliability, observability, and ownership needs.
- **revision_decision:** Add an escalation ladder and cost tradeoffs.
- **additional_insight_to_add:** Move stable repeatable coordination into code or workflow infrastructure rather than growing a prompt indefinitely.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Missing risks include shared-write conflict, inconsistent retries, lost correlation, stale summaries, policy divergence, and authority aggregation.
- **supporting_reason:** These risks grow nonlinearly as independently acting agents and systems interact.
- **counterargument_or_limit:** Strong platform enforcement can mitigate several risks outside the prompt.
- **assumptions_and_boundaries:** Name external controls and test their failure paths instead of restating them as wishes.
- **revision_decision:** Add invariants for correlation, policy, composed authority, partial failure, rollback ownership, and merge consistency.
- **additional_insight_to_add:** Least privilege must be evaluated across the composed system; individually narrow agents can collectively possess dangerous authority.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** No scale example illustrates sufficient versus insufficient use.
- **supporting_reason:** A good system has read-only specialists and one integration owner; a bad system lets several agents edit the same artifact; a borderline system reads two external services without an SLO but performs no writes.
- **counterargument_or_limit:** The borderline system may remain acceptable for low-volume advisory use.
- **assumptions_and_boundaries:** Release level depends on latency expectations, freshness, and failure disclosure.
- **revision_decision:** Add scale cases and corresponding authority levels.
- **additional_insight_to_add:** Manual invocation is a useful intermediate level when cross-system behavior is correct but operational guarantees are not established.

### Question 08: How can the important claims be verified?
- **current_section_observation:** The seed calls for merge checkpoints and graph narrowing but no end-to-end test method.
- **supporting_reason:** Verify ownership maps, message schemas, correlation, partial failure, retries, idempotency, policy consistency, rollback, load, and SLO behavior where claimed.
- **counterargument_or_limit:** Full failure testing can require expensive test environments.
- **assumptions_and_boundaries:** Simulate critical state transitions and clearly report untested production assumptions.
- **revision_decision:** Add component and end-to-end gate layers plus constrained release.
- **additional_insight_to_add:** Test the composed authority graph, not only component prompts, because risk emerges through allowed sequences across boundaries.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** Ownership and context-drift risks have clear causal bases, while exact thresholds for systems, agents, or traffic are unspecified.
- **supporting_reason:** Qualitative boundaries avoid false precision and guide safer architecture decisions.
- **counterargument_or_limit:** Teams still need local capacity and SLO numbers before production release.
- **assumptions_and_boundaries:** Derive those values from workload and risk evidence outside this generic reference.
- **revision_decision:** Keep qualitative limits and require local measured contracts for scale claims.
- **additional_insight_to_add:** State uncertainty as an operational limit, such as advisory-only or bounded batch use, rather than a general caution.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The section treats scale as a point where this reference ends rather than a source of feedback into agent design.
- **supporting_reason:** Scale pressure reveals where specialist boundaries, context interfaces, deterministic tooling, and governance need to mature.
- **counterargument_or_limit:** Premature architecture for hypothetical scale creates unnecessary complexity.
- **assumptions_and_boundaries:** Evolve only from recurring measured pressure or a known production requirement.
- **revision_decision:** Add migration signals and preserve simple modes for smaller workloads.
- **additional_insight_to_add:** The long-term direction is often less prompt coordination and more typed, testable infrastructure around narrower agents.

## Section 025: Future Refresh Search Queries

### Question 01: What decision does this reference help make?
- **current_section_observation:** The table provides three generic search phrases for official docs, GitHub examples, and release notes but does not state when a refresh is necessary or how results change the reference.
- **supporting_reason:** The section should decide when to investigate source drift, what question to search, and which claims, prompt clauses, and tests require review afterward.
- **counterargument_or_limit:** Generic search queries can return noisy secondary material and cannot establish authority by themselves.
- **assumptions_and_boundaries:** Queries are discovery templates, not evidence; selected results still need authority, version, scope, and direct inspection.
- **revision_decision:** Preserve the three phrases, add trigger and result protocols, and explicitly state that no browsing occurred in this pass.
- **additional_insight_to_add:** Refresh should begin from the affected claim rather than rerunning broad research whenever any source timestamp changes.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The seed does not prioritize official domains, installed versions, or local evidence before broad search.
- **supporting_reason:** Start with the local claim and installed host version, search official documentation and release notes, inspect the authoritative result, then use repositories or examples only for unresolved behavior.
- **counterargument_or_limit:** Implementation changes may precede formal documentation and require repository inspection.
- **assumptions_and_boundaries:** Label implementation observations and avoid treating unreleased or incidental behavior as a supported contract.
- **revision_decision:** Add an authority-ordered query sequence and contradiction handling.
- **additional_insight_to_add:** Include product, feature, version, and decision terms in searches to reduce cross-host conflation.

### Question 03: When does the default work well?
- **current_section_observation:** Search templates are useful for periodic maintenance but lack material refresh triggers.
- **supporting_reason:** They work when a public contract, installed tool, host behavior, local source, severe incident, or unresolved compatibility question materially affects an agent clause.
- **counterargument_or_limit:** Time-based refresh alone can waste effort on stable conceptual guidance.
- **assumptions_and_boundaries:** Prioritize semantic and operational triggers; use calendar review for high-risk dependencies with no other signal.
- **revision_decision:** Add refresh triggers based on material source, version, behavior, incident, compatibility, and risk changes.
- **additional_insight_to_add:** Record “no material change” with checked version and scope so repeated refreshes need not rediscover the same evidence.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** Broad queries can mix products, surface stale posts, reinforce confirmation bias, or lead to copied examples detached from local conventions.
- **supporting_reason:** Search ranking reflects relevance signals, not normative authority or compatibility.
- **counterargument_or_limit:** Secondary discussions can reveal failure modes and terminology that improve later primary-source queries.
- **assumptions_and_boundaries:** Use secondary material for discovery and counterexamples, then verify consequential claims through primary evidence or controlled behavior.
- **revision_decision:** Add result-rejection criteria for stale, secondary, cross-product, unsupported, or decision-irrelevant evidence.
- **additional_insight_to_add:** Stop when results no longer alter trigger, authority, process, output, recovery, or release status; more links do not necessarily reduce uncertainty.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The table omits local repository search, release feeds, installed-runtime help, schema diffs, commit history, issue trackers, and controlled experiments.
- **supporting_reason:** These alternatives may answer versioned operational questions more directly than web search.
- **counterargument_or_limit:** Implementation and issue evidence can be unstable, incomplete, or unsupported.
- **assumptions_and_boundaries:** Select evidence according to normative, operational, historical, or diagnostic purpose.
- **revision_decision:** Add non-web refresh routes and their evidentiary roles.
- **additional_insight_to_add:** A local schema or validator diff can be the earliest reliable signal that prompt syntax needs migration.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** The seed queries omit dates, versions, host names beyond the theme phrase, domains, and claim identifiers.
- **supporting_reason:** Missing qualifiers invite irrelevant or stale results and make refresh decisions difficult to reproduce.
- **counterargument_or_limit:** Overly constrained searches can miss renamed concepts or migration guidance.
- **assumptions_and_boundaries:** Begin precise, then broaden terminology deliberately while retaining the original question.
- **revision_decision:** Add query refinement, result logging, and confirmation-bias checks.
- **additional_insight_to_add:** Search for deprecation, breaking change, limitation, and failure terms as well as best practices to surface disconfirming evidence.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** Only generic query text is shown, with no result evaluation.
- **supporting_reason:** A good query names product, feature, version, and contract question; a bad query asks for best practices and copies a blog; a borderline query finds a repository example for undocumented behavior.
- **counterargument_or_limit:** Version terminology may be unavailable or inconsistent across sources.
- **assumptions_and_boundaries:** Record ambiguity and verify against the installed host.
- **revision_decision:** Add query and evaluation examples rather than fabricated search results.
- **additional_insight_to_add:** A borderline implementation example should motivate a controlled local experiment and a bounded inference, not immediate policy adoption.

### Question 08: How can the important claims be verified?
- **current_section_observation:** Search phrases themselves cannot verify freshness, authority, or behavioral impact.
- **supporting_reason:** Record query, date, selected source, version, relevant passage or location, rejected results, affected claim, and linked scenario; rerun behavior after updating.
- **counterargument_or_limit:** Full result logs can become noisy and retain unnecessary content.
- **assumptions_and_boundaries:** Keep concise decision records with links and paraphrased support.
- **revision_decision:** Add a refresh evidence packet and post-update regression step.
- **additional_insight_to_add:** Verify archive and local source integrity separately so external refresh does not silently rewrite provenance.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The exact three query phrases are seed facts; their future usefulness and current result sets are untested because this pass does not browse.
- **supporting_reason:** They remain reasonable broad entrypoints for official documentation, repositories, and release history.
- **counterargument_or_limit:** Search engines, terminology, domains, and product surfaces change.
- **assumptions_and_boundaries:** Treat them as editable templates and record any refined replacement with reason.
- **revision_decision:** Preserve the rows while labeling evidence status and maintenance ownership.
- **additional_insight_to_add:** Confidence should attach to the inspected result, not to the apparent specificity of the query.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** Future search is framed as refreshing prose rather than managing dependencies.
- **supporting_reason:** Each external claim can be linked to a prompt clause, fixture, owner, and refresh trigger, enabling targeted maintenance.
- **counterargument_or_limit:** Fine-grained dependency records can be excessive for low-impact conceptual advice.
- **assumptions_and_boundaries:** Track material syntax, capability, precedence, security, routing, and lifecycle claims first.
- **revision_decision:** Reframe searches as dependency refresh and add stop and propagation rules.
- **additional_insight_to_add:** A refresh that finds no relevant authoritative evidence may justify removing a claim rather than searching until confirmation appears.

## Section 026: Evidence Boundary Notes

### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed defines local fact, external fact, and combined inference in three bullets but does not explain how those labels affect prompt decisions, confidence, or verification.
- **supporting_reason:** Evidence boundaries should decide what can be asserted, what requires qualification, what must be tested, and what authority can be granted.
- **counterargument_or_limit:** Excessive labels can fragment readable prose and encourage formal compliance without semantic traceability.
- **assumptions_and_boundaries:** Label where provenance changes confidence or action, and keep a claim ledger for dense reasoning rather than prefixing every sentence.
- **revision_decision:** Preserve the three definitions and add scope, examples, conflict handling, propagation, and release consequences.
- **additional_insight_to_add:** Evidence labels describe support type, not truth; a local fact can be stale and a carefully tested inference can be operationally strong.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The seed gives definitions without an order for turning evidence into guidance.
- **supporting_reason:** Write atomic claims, attach the narrowest applicable label, record source and version, state uncertainty, derive the prompt clause, and attach a disconfirming gate.
- **counterargument_or_limit:** Some common connective reasoning does not need a formal ledger entry.
- **assumptions_and_boundaries:** Trace material routing, authority, behavior, performance, security, reliability, and lifecycle claims first.
- **revision_decision:** Add a claim-to-clause workflow and proportional labeling rule.
- **additional_insight_to_add:** Split mixed sentences when their clauses have different evidence types so one strong fact cannot launder a weak inference.

### Question 03: When does the default work well?
- **current_section_observation:** The labels assume sources are inspectable and claims can be separated cleanly.
- **supporting_reason:** It works when the designer records relevant spans, avoids duplicate-source inflation, and can exercise consequential synthesis in the target host.
- **counterargument_or_limit:** Complex architectural guidance may depend on interacting observations rather than one-to-one citations.
- **assumptions_and_boundaries:** Use a multi-source claim record that names each contribution and the remaining inference.
- **revision_decision:** Add support for compound evidence without collapsing provenance.
- **additional_insight_to_add:** The claim record should state what each source does not establish, preventing scope creep during later reuse.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** Labels can fail as decorative tokens, outdated source references, sentence-wide overclaims, or false equivalence between primary and secondary evidence.
- **supporting_reason:** These practices make text look rigorous while leaving decisions unsupported.
- **counterargument_or_limit:** Even imperfect labels can prompt useful review questions.
- **assumptions_and_boundaries:** Completion requires relevant support and action consequences, not label presence alone.
- **revision_decision:** Add semantic adequacy and stale-evidence failure rules.
- **additional_insight_to_add:** If changing or removing the source would not alter the recommendation or confidence, the citation may be ornamental rather than evidentiary.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The seed uses inline labels and omits footnotes, claim tables, decision records, confidence fields, and executable contracts.
- **supporting_reason:** Inline labels aid scanning, ledgers aid maintenance, decision records preserve conflict rationale, and tests encode operational expectations.
- **counterargument_or_limit:** Multiple representations can drift or burden small agents.
- **assumptions_and_boundaries:** Keep one primary claim record and generate concise prose or tests from it where practical.
- **revision_decision:** Describe acceptable evidence representations and synchronization needs.
- **additional_insight_to_add:** Tests can validate an inference's operational contract without converting that inference into an externally sourced fact.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Missing concerns include copied archive/live claims counted twice, unrefreshed URLs stated as current, inference hidden in table labels, and confidence that does not affect authority.
- **supporting_reason:** These errors directly undermine the reference's central thesis.
- **counterargument_or_limit:** Detailed provenance can distract from the user's immediate decision.
- **assumptions_and_boundaries:** Keep reader-facing guidance concise while retaining working evidence records for consequential clauses.
- **revision_decision:** Add a boundary review checklist and action mapping.
- **additional_insight_to_add:** Uncertainty without an owner, next observation, or capability consequence is passive disclaimer rather than risk control.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** The seed supplies no labeled claim example.
- **supporting_reason:** A good example separates local trigger format, unrefreshed external pointer, inferred negative case, and routing test; a bad example calls a best practice sourced; a borderline example relies on observed implementation behavior.
- **counterargument_or_limit:** Examples can become verbose if every clause is annotated inline.
- **assumptions_and_boundaries:** Show the claim ledger form and then natural reader-facing synthesis.
- **revision_decision:** Add good, bad, and borderline boundary examples.
- **additional_insight_to_add:** Borderline implementation evidence can justify a reversible local behavior while remaining insufficient for a portability claim.

### Question 08: How can the important claims be verified?
- **current_section_observation:** The seed defines three labels but provides no procedure for checking relevance, freshness, scope, or operational consequences.
- **supporting_reason:** Sample consequential claims, inspect source relevance and freshness, recompute archive/live identity, verify label scope, and run the linked disconfirming scenario.
- **counterargument_or_limit:** Auditing every low-impact phrase is costly and can make writing mechanical.
- **assumptions_and_boundaries:** Prioritize claims that change routing, authority, state, external behavior, or release status.
- **revision_decision:** Add bidirectional sampling from high-consequence claims to gates and from granted capabilities back to approved evidence.
- **additional_insight_to_add:** Audit from capability back to evidence as well as evidence forward to clauses; unexplained authority is easier to detect in reverse.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The three category definitions are explicit local reference conventions, while their optimal granularity and operational enforcement are synthesized.
- **supporting_reason:** The categories accurately separate provenance surfaces used throughout the file.
- **counterargument_or_limit:** They do not encode source quality, recency, independence, or behavioral confidence by themselves.
- **assumptions_and_boundaries:** Add those dimensions in claim records and status language rather than inventing certainty from the label.
- **revision_decision:** State what labels establish and what they do not.
- **additional_insight_to_add:** Report source confidence and runtime confidence independently because either can be high while the other is low.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** Evidence boundaries are presented as prose hygiene rather than a maintainability architecture.
- **supporting_reason:** Source-to-claim-to-clause-to-gate links enable targeted refresh, regression testing, authority downgrade, and retirement.
- **counterargument_or_limit:** Fine-grained traceability can become stale if no owner maintains it.
- **assumptions_and_boundaries:** Apply strongest traceability to long-lived and high-consequence agents and assign ownership at creation.
- **revision_decision:** End the reference with a maintenance and propagation rule.
- **additional_insight_to_add:** The evidence graph makes deletion safer: maintainers can remove a stale source or agent and identify which claims, tests, and routes must migrate.
