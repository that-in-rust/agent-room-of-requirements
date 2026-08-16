## Section 001: Kotlin Quality Antipattern Gates
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed title names Kotlin quality and antipattern gates but does not say whether the reader is choosing a framework, reviewing a change, defining domain types, repairing coroutine behavior, or deciding release readiness.
- **supporting_reason:** Kotlin quality failures usually cross boundaries: uncertain input becomes a platform type, a platform type reaches domain code, a broad catch hides cancellation, or a boolean return erases a failure distinction that callers need.
- **counterargument_or_limit:** A narrow formatting correction or an already-specified local test change may need only the repository's existing command and not the full gate model.
- **assumptions_and_boundaries:** Apply this reference to Kotlin implementation or review decisions involving nullability, Java interop, domain modeling, coroutines, blocking work, mutable state, or verification; route framework policy and production SLO acceptance to their owners.
- **revision_decision:** Expand the title into an operating contract for selecting the smallest applicable Kotlin reliability controls and proving them with target evidence.
- **additional_insight_to_add:** The unit of quality is a preserved semantic distinction across a boundary, not the presence of an idiomatic-looking Kotlin construct.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The heading provides no default sequence even though the local source orders boundary normalization, explicit domain types, structured concurrency, blocking isolation, risk-focused tests, and repo-native gates.
- **supporting_reason:** Parse uncertain data once, contain platform types in adapters, model meaningful states explicitly, preserve caller-owned cancellation, isolate blocking calls, and then run the commands the repository already trusts.
- **counterargument_or_limit:** Existing generated clients, framework converters, persistence models, or lifecycle scopes may already implement part of that sequence and should not be duplicated reflexively.
- **assumptions_and_boundaries:** Reuse an existing mechanism only when its nullability contract, ownership, cancellation behavior, and failure semantics are inspectable for the changed path.
- **revision_decision:** Publish a dependency-ordered default with explicit reuse, adaptation, specialist-routing, and stop branches.
- **additional_insight_to_add:** Earlier boundary normalization reduces the number of later branches, so it improves both human reviewability and the precision of tests and agent-generated changes.

### Question 03: When does the default work well?
- **current_section_observation:** The title does not identify favorable tasks, code shapes, or evidence prerequisites.
- **supporting_reason:** The method fits bounded Kotlin services, libraries, Android components, command-line tools, adapters, and workers where inputs, call ownership, blocking dependencies, and expected outcomes can be inspected.
- **counterargument_or_limit:** Legacy code may expose platform types and mutable global state through many modules, making one-pass normalization impractical.
- **assumptions_and_boundaries:** For broad legacy surfaces, select one consequential path, add characterization evidence, and move the uncertainty boundary incrementally instead of promising a repository-wide cleanup.
- **revision_decision:** Add fit conditions based on bounded ownership, reproducible behavior, identifiable interop edges, and available project-native checks.
- **additional_insight_to_add:** The default is strongest when a reviewer can point to the exact line where uncertainty enters and the exact test where it is converted into a typed result.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** A title-only section offers no refusal path for unknown business states, framework lifecycle rules, Java annotation contracts, production dispatcher limits, or release authority.
- **supporting_reason:** Kotlin syntax cannot decide whether absence is valid, which failures are recoverable, what equality means for an entity, or how much blocking a deployment can tolerate.
- **counterargument_or_limit:** A small isolated experiment can reveal the missing contract without committing a production architecture.
- **assumptions_and_boundaries:** Keep experiments off production paths, use representative but non-sensitive fixtures, and label unresolved policy or capacity questions before reuse.
- **revision_decision:** Add route-away states for domain policy, framework lifecycle, Java API ownership, persistence identity, performance operations, and security/privacy review.
- **additional_insight_to_add:** The wrong-tool signal is a consequential product or operational choice being disguised as a nullable property, dispatcher selection, timeout, or default enum member.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The title collapses alternatives such as nullable values versus sealed outcomes, exceptions versus result types, plain classes versus data classes, explicit blocking APIs versus dispatcher isolation, and focused tests versus broad static gates.
- **supporting_reason:** These alternatives trade call-site friction, exhaustiveness, allocation and API cost, framework compatibility, cancellation transparency, migration effort, and defect visibility.
- **counterargument_or_limit:** Enumerating every Kotlin idiom can obscure a straightforward local correction that already follows repository convention.
- **assumptions_and_boundaries:** Compare only options that preserve the target behavior and interop contract; aesthetic preference alone is not a quality argument.
- **revision_decision:** Introduce consequence-based choice matrices and require each alternative to name the semantic distinction it preserves or sacrifices.
- **additional_insight_to_add:** A more verbose plain class or named local is often the safer Kotlin choice when lifecycle identity or receiver meaning would otherwise be implicit.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** The heading hides recurring hazards including `!!`, leaked platform types, broad `lateinit`, `GlobalScope`, swallowed `CancellationException`, hidden blocking in `suspend`, nested scope functions, boolean flags, and mutable global singletons.
- **supporting_reason:** These hazards often compile and pass happy-path tests while moving failure farther from the input, caller, lifecycle, or thread that owns it.
- **counterargument_or_limit:** Each construct has legitimate narrow uses, such as test setup, generated binding code, or a proven invariant adjacent to the assertion.
- **assumptions_and_boundaries:** Treat constructs as review signals rather than lexical bans; require a local invariant, owner, and verification path for an exception.
- **revision_decision:** Add a causal hazard registry that distinguishes prohibited production use, conditional use, and false-positive contexts.
- **additional_insight_to_add:** The most expensive Kotlin quality defects are ownership defects because the eventual crash, leak, blocked thread, or stale state appears far from the line that discarded ownership information.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** The title gives no contrast between reliable Kotlin and code that merely uses Kotlin syntax.
- **supporting_reason:** Good code converts a Java platform value in an adapter, returns a sealed domain outcome, uses caller-owned scope, rethrows cancellation, and proves malformed and cancelled paths; bad code uses `!!`, `GlobalScope`, and a boolean success flag.
- **counterargument_or_limit:** A private migration shim can temporarily accept a platform type or broad exception if it immediately normalizes and records the remaining boundary.
- **assumptions_and_boundaries:** Judge examples by exposure, reversibility, lifecycle, concurrency, and caller obligations rather than by isolated syntax.
- **revision_decision:** Include positive, unsafe, and conditional examples with the evidence needed to promote the conditional case.
- **additional_insight_to_add:** A borderline construct becomes acceptable only when its dangerous interpretation is made impossible or observable at the same boundary.

### Question 08: How can the important claims be verified?
- **current_section_observation:** No acceptance mechanism is attached to the heading, so a reviewer cannot distinguish guidance from enforced behavior.
- **supporting_reason:** Boundary tests, nullability and malformed-input fixtures, cancellation tests, dispatcher or blocking probes, equality/lifecycle tests, static analysis, and repository-native build commands observe different failure classes.
- **counterargument_or_limit:** Passing local tests and lint cannot establish production saturation, every Java annotation contract, or framework behavior on an untested version.
- **assumptions_and_boundaries:** Combine deterministic code evidence with versioned dependency contracts and operational measurement proportional to the claim being made.
- **revision_decision:** Define a layered done condition: semantic tests first, compile/build next, lint/static checks where configured, and runtime evidence only for runtime claims.
- **additional_insight_to_add:** Verification must include at least one rejected, cancelled, absent, or blocking path because a happy-path test cannot prove the distinctions these gates are meant to preserve.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The mapped local source directly lists ten anti-patterns, an eight-step reliability stack, gate discovery commands, and a six-axis review pass; none of the four public links was opened.
- **supporting_reason:** Complete local reading supports precise claims about inherited guidance, while target applicability and current external framework behavior require repository or authorized external evidence.
- **counterargument_or_limit:** Several recommendations follow stable language and concurrency principles even without a target repository.
- **assumptions_and_boundaries:** Label local text as observed, this reference's operational synthesis as reasoned guidance, target behavior as unverified until tested, and public links as unrefreshed pointers.
- **revision_decision:** Put the known/unknown ledger in the operating contract and reject universal defect, latency, or productivity numbers.
- **additional_insight_to_add:** Confidence may be high that a broad catch suppresses cancellation in a code path while remaining low about how often production reaches that path; code fact and incidence estimate need different evidence states.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The title does not reveal that nullability, interop, domain states, coroutine ownership, blocking, testing, and static gates form one causal system.
- **supporting_reason:** A leaked platform type creates `!!`; a crash may trigger retry; a detached coroutine loses failure ownership; a boolean result hides whether retry is safe; mutable global state makes the resulting test order-dependent.
- **counterargument_or_limit:** Formalizing every low-risk local value can add ceremony without changing a consequential decision.
- **assumptions_and_boundaries:** Model distinctions whose loss changes caller behavior, lifecycle, side effects, recovery, or auditability; keep reversible presentation details lighter.
- **revision_decision:** Frame Kotlin quality as information and ownership preservation from ingress through execution, state transition, and verification.
- **additional_insight_to_add:** Quality gates should be ordered by causal leverage: boundary and ownership errors must be fixed before style automation, because formatting cannot recover information already discarded.

## Section 002: Source Evidence Mapping Table
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed table mixes one local Kotlin quality file with four public roots while assigning broad categories that do not reveal which source can support a language rule, framework behavior, repository convention, or runtime claim.
- **supporting_reason:** A recommendation about `CancellationException`, Java platform types, data-class identity, or configured lint requires different evidence and can become wrong on different triggers.
- **counterargument_or_limit:** A compact source list is easier to scan than a full evidence graph and may be enough for initial discovery.
- **assumptions_and_boundaries:** Keep the first view compact, but require claim-level authority, freshness, target applicability, conflict, and invalidation before a source changes implementation.
- **revision_decision:** Expand the mapping into evidence classes and lifecycle states without removing any inherited path or URL.
- **additional_insight_to_add:** The map must distinguish a source that proposes a quality rule from an artifact that proves the target code follows it.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The seed labels public URLs as externally sourced facts even though no retrieval date, version, quoted span, or authorized browse is recorded.
- **supporting_reason:** Read local material first, inspect target build and code evidence next, and promote a public pointer only after direct retrieval and target reproduction.
- **counterargument_or_limit:** A known framework migration or compiler change may make current official documentation the necessary first retrieval surface.
- **assumptions_and_boundaries:** External-first research still records installed versions, target configuration, relevant source span, and the behavior that closes the local uncertainty.
- **revision_decision:** Give every row an initial state and a promotion rule rather than treating location alone as evidence.
- **additional_insight_to_add:** An unvisited official URL has high potential authority but zero observed content in the current evidence set.

### Question 03: When does the default work well?
- **current_section_observation:** The current map does not state when local-first evidence is sufficiently current or representative.
- **supporting_reason:** Local-first works when the repository owns the changed code, wrappers and dependency locks are inspectable, and the mapped quality source supplies stable reasoning rather than version-specific API detail.
- **counterargument_or_limit:** Generated clients, framework plugins, compiler diagnostics, and Java annotations can make upstream version contracts decisive.
- **assumptions_and_boundaries:** Use local evidence for repository policy and target behavior; retrieve upstream evidence for unresolved version semantics, then verify it against the installed target.
- **revision_decision:** Add favorable conditions for each evidence class and a target-closure column.
- **additional_insight_to_add:** Local and official evidence are complements: one says what this repository does, while the other may explain what the dependency promises.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The table has no route for stale local advice, conflicting source generations, undocumented Java APIs, or runtime behavior that contradicts prose.
- **supporting_reason:** Treating all listed sources as mutually confirming can preserve an obsolete command, miss a framework lifecycle constraint, or overstate a source-only conclusion.
- **counterargument_or_limit:** A conservative local convention can remain intentionally stricter than current upstream guidance.
- **assumptions_and_boundaries:** Preserve stricter policy when an accountable owner and rationale are explicit; otherwise expose the conflict rather than selecting silently.
- **revision_decision:** Add conflict states, precedence by claim type, and stop conditions for policy or operational uncertainty.
- **additional_insight_to_add:** Runtime contradiction invalidates a runtime claim but does not automatically erase a deliberately stricter review policy.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The seed offers no choice among source inspection, tests, compiler output, static analysis, official docs, implementation repositories, framework examples, and production telemetry.
- **supporting_reason:** These alternatives trade speed, authority, scope, reproducibility, version fit, and ability to observe dynamic effects.
- **counterargument_or_limit:** Requiring every evidence type for every change would make small reviews needlessly expensive.
- **assumptions_and_boundaries:** Select the minimum evidence bundle that can falsify the actual claim; add runtime or external evidence only when source and tests cannot close it.
- **revision_decision:** Add a claim-to-evidence matrix with escalation triggers instead of a universal research checklist.
- **additional_insight_to_add:** More sources do not increase confidence when they repeat one lineage or fail to observe the disputed behavior.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** The map hides duplicate lineage, URL-title authority bias, target-version mismatch, example-to-contract promotion, and source-only claims about runtime behavior.
- **supporting_reason:** Those errors make plausible guidance look independently confirmed and current while leaving the target mechanism untested.
- **counterargument_or_limit:** Duplicate copies can still help detect local drift if their identities and intended roles are recorded.
- **assumptions_and_boundaries:** Hash or otherwise identify local artifacts, label example status, and keep observed content separate from expected target behavior.
- **revision_decision:** Add evidence hazards, identity checks, and explicit prohibited promotions.
- **additional_insight_to_add:** A framework tutorial is evidence that one example was designed, not proof that the target project's version, plugins, and lifecycle behave identically.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** The seed rows do not demonstrate correct or incorrect reuse of their authority labels.
- **supporting_reason:** A good claim links local guidance to target code and a failing/passing test; a bad claim cites the Kotlin home page as proof that production cancellation is correct.
- **counterargument_or_limit:** A borderline review may have a source-confirmed language rule but no runnable target fixture yet.
- **assumptions_and_boundaries:** Keep such a review in proposed or blocked state and state exactly which target evidence is missing.
- **revision_decision:** Add contrastive evidence cards and promotion outcomes.
- **additional_insight_to_add:** Borderline evidence is useful when it narrows the next experiment instead of being rounded up into completion.

### Question 08: How can the important claims be verified?
- **current_section_observation:** No mechanism checks whether paths exist, files were read, URLs were retrieved, target versions match, or a cited artifact supports the nearby statement.
- **supporting_reason:** Path existence, complete-file hashes, build/dependency inspection, focused tests, configured analyzer output, retrieval metadata, and runtime probes verify complementary parts of the chain.
- **counterargument_or_limit:** A file hash proves identity but says nothing about correctness or target applicability.
- **assumptions_and_boundaries:** Pair identity checks with semantic review and claim-specific target evidence; do not use one gate as a substitute for another.
- **revision_decision:** Define source identity, semantic support, target closure, and invalidation as separate verification fields.
- **additional_insight_to_add:** Evidence is auditable only when another reviewer can reconstruct both the cited input and the promotion decision.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** It is known that the local file exists and was read, while the public rows are retained from the seed and were not opened in this pass.
- **supporting_reason:** The local file's hash and complete content establish the inherited anti-pattern and gate guidance exactly.
- **counterargument_or_limit:** Local guidance alone cannot establish current Kotlin, coroutine, Spring, or Ktor version behavior in an unspecified target.
- **assumptions_and_boundaries:** Keep local observations, unrefreshed pointers, operational synthesis, and future target results in distinct states.
- **revision_decision:** Add a known/unknown ledger and prohibit language implying that unvisited external content was confirmed.
- **additional_insight_to_add:** Confidence belongs to a claim-source-target tuple, not to a source brand in isolation.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The seed map is static even though Kotlin quality claims change when code, build configuration, dependency versions, framework lifecycle, or production workload changes.
- **supporting_reason:** A durable evidence map needs selective invalidation so a dependency upgrade reopens version-sensitive claims without discarding unrelated domain-state tests.
- **counterargument_or_limit:** Fine-grained dependency graphs add maintenance cost to small one-off reviews.
- **assumptions_and_boundaries:** Track invalidation at least for consequential, shared, externally versioned, or runtime-sensitive guidance; lighter notes are sufficient for reversible local decisions.
- **revision_decision:** Turn the table into a small evidence lifecycle with identity, authority, target closure, conflict, and refresh triggers.
- **additional_insight_to_add:** Selective invalidation prevents two opposite failures: trusting stale evidence and needlessly re-proving every stable Kotlin invariant after an unrelated change.

## Section 003: Pattern Scoreboard Ranking Table
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed ranks source-map-first, evidence-boundary, and verification-coupling patterns with unexplained values of 95, 91, and 88 but does not say how those numbers should affect a Kotlin change.
- **supporting_reason:** A pattern register can help a reviewer choose the next control when several quality risks compete for limited attention.
- **counterargument_or_limit:** Numeric ordering can create false precision and hide that nullability, cancellation, or blocking may dominate in a specific path.
- **assumptions_and_boundaries:** Treat inherited scores as historical editorial priorities, never as measured effectiveness or mandatory ordering for every task.
- **revision_decision:** Preserve the values for source fidelity while adding operational adoption criteria and consequence-based override rules.
- **additional_insight_to_add:** The highest local risk should select the next gate even when its pattern has no inherited score.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** All three seed rows use `default_adoption_pattern_tier` without entry, exit, or exception conditions.
- **supporting_reason:** Start with source identity, keep observed facts separate from inference, and attach verification before implementation claims are promoted.
- **counterargument_or_limit:** A reproduced cancellation failure or platform-type crash can justify immediate containment before completing a broad evidence inventory.
- **assumptions_and_boundaries:** Emergency containment remains narrow, reversible, and followed by evidence reconstruction before broader reuse.
- **revision_decision:** Convert each row into a lifecycle with trigger, default action, exception, verification, and invalidation.
- **additional_insight_to_add:** Defaults should reduce uncertainty in dependency order: locate authority, state the claim, then test the behavior.

### Question 03: When does the default work well?
- **current_section_observation:** The scoreboard does not name tasks where its three patterns provide high leverage.
- **supporting_reason:** They work well for generated guidance, unfamiliar Kotlin repositories, cross-framework reviews, mixed Java/Kotlin boundaries, and changes with several plausible quality claims.
- **counterargument_or_limit:** A one-line local correction with an existing regression test may already have complete authority and verification.
- **assumptions_and_boundaries:** Skip redundant ceremony only when the source, target path, expected behavior, and gate are already explicit and current.
- **revision_decision:** Add fit signals and a lightweight path for already-closed local changes.
- **additional_insight_to_add:** Pattern overhead should scale with uncertainty and consequence, not file size or syntactic complexity.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The seed table gives no failure state for stale sources, unavailable tests, disputed domain semantics, or urgent incident work.
- **supporting_reason:** Blindly applying the rank can delay containment, reward documentation volume, or promote a locally tidy but semantically wrong type model.
- **counterargument_or_limit:** Even incidents benefit from a minimal record of what was observed and how containment was verified.
- **assumptions_and_boundaries:** Use an incident mode that captures the failing path, reversible action, immediate evidence, owner, and required follow-up without pretending the full model ran.
- **revision_decision:** Add blocked, incident, route-away, and superseded states to the pattern lifecycle.
- **additional_insight_to_add:** A scoreboard becomes harmful when it optimizes process compliance instead of reducing the next consequential uncertainty.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The seed ranks only evidence-process patterns and omits direct Kotlin controls such as boundary normalization, typed outcomes, structured concurrency, blocking isolation, and state containment.
- **supporting_reason:** Process controls improve traceability, while Kotlin controls directly prevent information or ownership loss.
- **counterargument_or_limit:** Expanding the table into a complete style guide would duplicate later sections and make prioritization noisy.
- **assumptions_and_boundaries:** Register only cross-cutting patterns that change review or implementation decisions; keep syntax-level detail in the anti-pattern registry.
- **revision_decision:** Add a small qualitative Kotlin control set and show how it composes with the three inherited evidence patterns.
- **additional_insight_to_add:** Evidence patterns and code patterns are orthogonal: one determines confidence, the other determines behavior.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Unexplained scores can be mistaken for percentages, benchmark results, confidence levels, or universally optimized priorities.
- **supporting_reason:** Such interpretations encourage unsupported claims and can cause reviewers to ignore a lower-ranked but path-critical cancellation or identity defect.
- **counterargument_or_limit:** Removing all ordering would reduce the table's usefulness as a quick retrieval surface.
- **assumptions_and_boundaries:** Retain qualitative tiers and historical numbers only with explicit provenance and override criteria.
- **revision_decision:** Add interpretation warnings, anti-gaming rules, and evidence required before changing a pattern's status.
- **additional_insight_to_add:** A pattern can be frequently applicable without being sufficient, so adoption frequency and defect-prevention scope must remain separate.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** The scoreboard lacks examples of using or misusing a ranked pattern.
- **supporting_reason:** Good use starts with the local anti-pattern source, identifies a leaked platform type, and adds a boundary test; bad use cites score 95 as proof that the output is reliable.
- **counterargument_or_limit:** A borderline incident patch may apply structured cancellation before completing source-map documentation.
- **assumptions_and_boundaries:** That patch remains provisional until the code owner records the target contract and regression evidence.
- **revision_decision:** Add concise contrastive pattern applications and explicit promotion outcomes.
- **additional_insight_to_add:** A pattern is operational only when its use changes a code, test, routing, or stop decision.

### Question 08: How can the important claims be verified?
- **current_section_observation:** No seed column records whether a pattern was applied, whether its intended failure was exercised, or whether it later prevented recurrence.
- **supporting_reason:** Decision records, changed-path diffs, focused tests, analyzer findings, review outcomes, and recurrence tracking provide progressively stronger evidence.
- **counterargument_or_limit:** Recurrence data requires stable classification and enough observations; small teams may not have a meaningful sample.
- **assumptions_and_boundaries:** Use deterministic application checks immediately and treat outcome trends as optional, cohort-bound feedback rather than proof of causation.
- **revision_decision:** Add verification signatures and avoid unsupported effectiveness percentages.
- **additional_insight_to_add:** The first useful metric is whether the pattern exposed a previously implicit decision, not whether a broad defect rate moved.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The three pattern names and values are frozen seed facts, while their derivation, calibration population, and observed outcomes are absent.
- **supporting_reason:** Their conceptual ordering is reasonable for generated references because evidence identity logically precedes synthesis and verification.
- **counterargument_or_limit:** That logic does not establish the exact numeric gaps or priority for a target Kotlin defect.
- **assumptions_and_boundaries:** Preserve numbers as inherited metadata and express current recommendations qualitatively with target-specific overrides.
- **revision_decision:** Add provenance and uncertainty fields beside every score.
- **additional_insight_to_add:** Unknown calibration should narrow interpretation rather than force deletion of useful historical retrieval cues.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** A static scoreboard cannot react when a repository adds stricter compiler settings, adopts structured-concurrency helpers, changes framework lifecycle, or experiences a new failure class.
- **supporting_reason:** Pattern status should evolve from actual target findings and invalidation events, not remain frozen by initial editorial ranking.
- **counterargument_or_limit:** Continuous scoring can become bureaucratic and invite gaming without enough outcome data.
- **assumptions_and_boundaries:** Update qualitative status only on a recorded trigger such as repeated finding, source conflict, tool change, or verified control adoption.
- **revision_decision:** Introduce a simple lifecycle of candidate, default, conditional, superseded, and rejected for scope.
- **additional_insight_to_add:** The scoreboard should function as a retrieval index and decision history, not a universal optimization function.

## Section 004: Idiomatic Thesis Synthesis Statement
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed thesis says to load local material, check public analogues, and create verification-backed decisions, but it does not state the Kotlin quality decision produced by that sequence.
- **supporting_reason:** The central decision is where uncertainty and ownership are converted into explicit, testable Kotlin contracts before they spread through domain and concurrent code.
- **counterargument_or_limit:** Some changes affect only a stable internal value or formatting rule and do not cross an uncertain or concurrent boundary.
- **assumptions_and_boundaries:** Apply the full thesis to behaviorally consequential paths; use a lighter project-native check for reversible local presentation changes.
- **revision_decision:** Rewrite the thesis around information preservation, ownership preservation, and claim-matched verification.
- **additional_insight_to_add:** "Idiomatic" is useful only when it predicts safer caller obligations, not when it merely resembles common Kotlin syntax.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The seed sequence gives evidence order but no implementation order.
- **supporting_reason:** Normalize uncertainty, model closed states, contain Java interop, assign coroutine and state ownership, isolate blocking, and verify the highest-risk branches in that dependency order.
- **counterargument_or_limit:** A repository-native abstraction may combine several steps and should not be decomposed without evidence of failure.
- **assumptions_and_boundaries:** Reuse combined abstractions when their semantics, lifecycle, and tests remain visible for the target path.
- **revision_decision:** Add an explicit evidence-to-contract-to-execution-to-gate pipeline with reuse and stop branches.
- **additional_insight_to_add:** The order minimizes state-space growth because each early conversion removes ambiguous branches from every downstream caller.

### Question 03: When does the default work well?
- **current_section_observation:** The thesis does not identify when local guidance plus target evidence can close a decision without external research.
- **supporting_reason:** It works when the repository exposes build configuration, interop adapters, domain types, coroutine entry points, blocking dependencies, and focused tests.
- **counterargument_or_limit:** Closed-source Java libraries or framework-generated lifecycle code may leave crucial contracts opaque.
- **assumptions_and_boundaries:** Escalate opaque version behavior to official artifacts or black-box contract tests rather than guessing from Kotlin call syntax.
- **revision_decision:** Add fit conditions and an opacity route.
- **additional_insight_to_add:** A visible Kotlin wrapper does not make an opaque Java or native dependency semantically transparent.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The seed thesis can be read as a universal local-first recipe even when domain semantics or operational limits are unknown.
- **supporting_reason:** No evidence synthesis can decide whether `null` means forbidden, whether identity is value-based, or whether a blocking pool size is acceptable without accountable target context.
- **counterargument_or_limit:** The method can still identify the missing decision and prevent accidental implementation.
- **assumptions_and_boundaries:** Stop at an explicit blocked or route-away state when policy, lifecycle, or capacity authority is absent.
- **revision_decision:** Make refusal and escalation part of the thesis rather than an exception hidden later.
- **additional_insight_to_add:** Correctly locating an unresolved decision is a successful quality outcome even when no code is produced.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The seed thesis does not compare direct local correction, adapter containment, domain redesign, framework-native mechanisms, or external research.
- **supporting_reason:** These routes differ in blast radius, migration cost, caller disruption, long-term clarity, and dependence on framework lifecycle.
- **counterargument_or_limit:** A broad redesign can be attractive in theory while exceeding the evidence and ownership available for one change.
- **assumptions_and_boundaries:** Prefer the smallest route that preserves the required semantics and leaves an explicit future boundary.
- **revision_decision:** Add route selection based on uncertainty location and consequence.
- **additional_insight_to_add:** Adapter containment is often a valuable intermediate architecture, not merely technical debt, because it localizes interop uncertainty.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Generic synthesis can produce attractive Kotlin advice while missing platform-type leakage, swallowed cancellation, identity misuse, hidden blocking, or unconfigured gate commands.
- **supporting_reason:** Those defects arise when evidence, semantic modeling, execution ownership, and verification are treated as independent checklists.
- **counterargument_or_limit:** Not every path contains all four dimensions.
- **assumptions_and_boundaries:** Mark irrelevant dimensions with a reason, but never infer they are absent from silence.
- **revision_decision:** Add a causal completeness check that follows the target path end to end.
- **additional_insight_to_add:** Checklist completion without path tracing can produce green documentation around an unchanged ownership defect.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** The thesis has no demonstration of how evidence becomes an implementation decision.
- **supporting_reason:** Good synthesis traces a Java nullable return into an adapter, sealed outcome, caller branch, and test; bad synthesis simply says "avoid nulls" and runs a formatter.
- **counterargument_or_limit:** A borderline characterization test may preserve existing ambiguous behavior before redesign.
- **assumptions_and_boundaries:** Characterization is acceptable when labeled as current behavior rather than desired semantics and paired with an owner decision trigger.
- **revision_decision:** Add one complete causal example and one characterization-first alternative.
- **additional_insight_to_add:** Tests can preserve a defect as easily as they prevent one unless the intended contract is named separately from observed behavior.

### Question 08: How can the important claims be verified?
- **current_section_observation:** The seed says verification-backed but does not define verification layers or population boundaries.
- **supporting_reason:** Source inspection, boundary tests, coroutine tests, build and analyzer commands, and runtime probes each close a different part of the thesis.
- **counterargument_or_limit:** Running every layer for every change wastes time and can create irrelevant noise.
- **assumptions_and_boundaries:** Select layers from the claim; runtime claims require runtime evidence, while a sealed-outcome exhaustiveness claim may be closed by compilation and focused tests.
- **revision_decision:** Add a claim-to-gate selection rule and explicit no-claim outcome.
- **additional_insight_to_add:** A skipped gate is honest when its non-applicability or unavailable prerequisite is recorded; an implied green gate is not.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The local source supports the listed practices, but the seed thesis overstates public checking that did not occur in this evolution.
- **supporting_reason:** The causal pipeline is grounded in local content and strong Kotlin systems reasoning, while target and external applicability remain unobserved.
- **counterargument_or_limit:** Different Kotlin domains may prioritize UI lifecycle, server request scope, native memory, or batch throughput differently.
- **assumptions_and_boundaries:** Present the pipeline as a default decision model with domain-specific adaptation, not a complete platform policy.
- **revision_decision:** State known local facts, reasoned synthesis, and target unknowns explicitly.
- **additional_insight_to_add:** Stable reasoning can be confidently reusable while concrete configuration remains deliberately unresolved.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The seed thesis treats output quality as the end state rather than a feedback loop.
- **supporting_reason:** A gate finding should update adapters, domain models, shared coroutine helpers, tests, and future review triggers so the same ambiguity is cheaper to detect next time.
- **counterargument_or_limit:** Generalizing from one defect can overfit a shared abstraction or lint rule.
- **assumptions_and_boundaries:** Promote a local lesson only after recurrence, broad ownership, or a clearly shared causal mechanism is established.
- **revision_decision:** Add selective learning and invalidation to the thesis.
- **additional_insight_to_add:** The second-order goal is not more gates; it is moving semantic guarantees earlier so fewer gates are needed downstream.

## Section 005: Local Corpus Source Map
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed lists one local file and its headings but does not map those headings to concrete Kotlin decisions or evidence limits.
- **supporting_reason:** A semantic map lets a reviewer retrieve the anti-pattern, reliability, command, or review guidance needed without treating the whole file as authority for every claim.
- **counterargument_or_limit:** The source is only sixty lines, so an elaborate index can cost more to maintain than reading it completely.
- **assumptions_and_boundaries:** Always read the short source completely; use the map as a decision and invalidation aid, not as a substitute excerpt.
- **revision_decision:** Expand the row into heading-level contributions, prohibited inferences, and target closure.
- **additional_insight_to_add:** A small canonical source benefits most from complete reading plus precise scope, not fragmented quotation.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The seed usage role calls the detail file a skill entrypoint or reusable prompt even though its content is a focused reference, not an executable tool.
- **supporting_reason:** Treat it as canonical inherited quality guidance, then inspect the target repository before applying commands or abstractions.
- **counterargument_or_limit:** An installed newer skill may supersede archive guidance in another environment.
- **assumptions_and_boundaries:** This assignment records only the mapped archive source; a newer source must be explicitly identified and conflict-reviewed before promotion.
- **revision_decision:** Correct the role and add source identity, target applicability, and replacement rules.
- **additional_insight_to_add:** Source path taxonomy should describe what an artifact actually contains, not merely how it might be injected into an agent context.

### Question 03: When does the default work well?
- **current_section_observation:** The map provides no conditions for applying the source directly.
- **supporting_reason:** Direct use works for stable reasoning about nullability, platform-type containment, structured concurrency, cancellation, blocking visibility, typed outcomes, state scope, and existing project gates.
- **counterargument_or_limit:** Framework code generation, compiler settings, Java annotations, and lifecycle APIs can alter the implementation route.
- **assumptions_and_boundaries:** Preserve the principle but adapt the mechanism using target source, version, and tests.
- **revision_decision:** Add stable principle versus target mechanism columns.
- **additional_insight_to_add:** A principle can remain current while every command or framework example used to enact it changes.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The single-source map gives no signal for source staleness, omitted domain states, unsupported platforms, or target conflicts.
- **supporting_reason:** Applying archive guidance without target inspection can invent `detekt`, mis-handle Android lifecycle, or impose server coroutine assumptions on Kotlin/Native.
- **counterargument_or_limit:** The source itself tells readers to use commands the repository already uses and inspect build files before inventing tools.
- **assumptions_and_boundaries:** Honor that self-limiting instruction and route platform-specific behavior to target evidence.
- **revision_decision:** Add explicit stop conditions and platform/context qualifiers.
- **additional_insight_to_add:** The strongest local instruction may be a prohibition against blindly applying the rest of the local instruction set.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The seed does not compare complete-source reading, heading lookup, code search, build inspection, or target experimentation.
- **supporting_reason:** Complete reading preserves context, heading lookup speeds retrieval, and target evidence determines applicability.
- **counterargument_or_limit:** Re-reading the same source for every small change can be redundant when its hash and relevant contract are already journaled.
- **assumptions_and_boundaries:** Reuse a frozen reading only while the hash, task scope, and interpretation remain valid.
- **revision_decision:** Add a reuse protocol with hash and invalidation checks.
- **additional_insight_to_add:** Context reuse is safe when identity and scope are frozen, not merely because a source was read sometime before.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** One source can be over-promoted into a complete Kotlin standard or underused as a mere bibliography row.
- **supporting_reason:** Over-promotion hides missing platform and target evidence, while underuse loses its concrete anti-pattern and command guidance.
- **counterargument_or_limit:** A concise source cannot enumerate every legitimate exception or framework variant.
- **assumptions_and_boundaries:** Extract principles and named hazards, then document target-specific exceptions rather than editing the archive source.
- **revision_decision:** Add overreach, omission, stale-hash, and command-invention hazards.
- **additional_insight_to_add:** Canonical for an inherited theme does not mean exhaustive for Kotlin as a language or ecosystem.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** The row has no example of correctly applying one heading.
- **supporting_reason:** Good use reads `High-Value Anti-Patterns`, finds a broad catch in suspend work, and adds cancellation evidence; bad use runs `./gradlew detekt` without proving the task exists.
- **counterargument_or_limit:** A borderline project may configure a differently named aggregate task that includes Detekt.
- **assumptions_and_boundaries:** Inspect task configuration and record the actual command rather than requiring the example spelling.
- **revision_decision:** Add heading-to-action examples with target closure.
- **additional_insight_to_add:** Command intent should be preserved even when command syntax differs across repositories.

### Question 08: How can the important claims be verified?
- **current_section_observation:** The seed does not record file identity, complete reading, heading coverage, or whether target commands exist.
- **supporting_reason:** Hashing, complete-file review, heading inventory, build-file search, wrapper task inspection, and focused behavior tests create an auditable chain.
- **counterargument_or_limit:** Hash stability cannot prove that archive advice is still the preferred organizational policy.
- **assumptions_and_boundaries:** Pair source identity with current owner or target evidence when policy status matters.
- **revision_decision:** Add source and target verification signatures.
- **additional_insight_to_add:** The source's own discovery commands are part of its safety model because they prevent toolchain invention.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The source identity, complete text, headings, and hash are known; its authoring rationale, target applicability, and future status are not documented.
- **supporting_reason:** Exact content supports faithful synthesis without pretending to know why every item was selected.
- **counterargument_or_limit:** The ten listed anti-patterns may reflect broader experience not captured in the file.
- **assumptions_and_boundaries:** Do not manufacture provenance or effectiveness; evaluate each item causally against the target.
- **revision_decision:** Add a local known/unknown ledger.
- **additional_insight_to_add:** Missing historical rationale is a reason to preserve the text carefully and bound interpretation, not to invent authority.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The source's anti-pattern list, reliability stack, commands, and review pass are presented sequentially but form a reusable control loop.
- **supporting_reason:** Findings identify risks, the stack orders correction, commands test configured mechanics, and review dimensions check semantic coverage.
- **counterargument_or_limit:** Turning every review into a fixed loop can ignore task-specific entry points.
- **assumptions_and_boundaries:** Enter at the observed risk but ensure downstream verification and upstream boundary assumptions are still covered.
- **revision_decision:** Map the source as a loop with flexible entry and explicit completion.
- **additional_insight_to_add:** The local file's value is the composition of diagnosis, correction defaults, executable gates, and handoff review, not any isolated bullet.

## Section 006: External Research Source Map
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed lists four external roots but does not say which unresolved Kotlin quality question should trigger each source.
- **supporting_reason:** Decision-triggered retrieval avoids loading broad documentation that cannot close the target uncertainty.
- **counterargument_or_limit:** Broad orientation can be useful when the framework or dependency surface is initially unknown.
- **assumptions_and_boundaries:** Orientation may identify candidate topics, but promoted guidance still needs a precise artifact, version scope, and target link.
- **revision_decision:** Map each URL to concrete question classes, retrieval packets, and prohibited inferences.
- **additional_insight_to_add:** External research should begin with a falsifiable question, not a technology name.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** Every seed row is labeled as an external fact despite the no-browse execution state.
- **supporting_reason:** Retain each row as `unrefreshed_no_browse` until authorized retrieval records content and target applicability.
- **counterargument_or_limit:** The labels came from the frozen seed and must remain visible for provenance.
- **assumptions_and_boundaries:** Preserve the inherited label as historical metadata while overriding its current evidence status explicitly.
- **revision_decision:** Add status, retrieval trigger, capture schema, and promotion gate columns.
- **additional_insight_to_add:** Evidence status can change without changing source location or historical category.

### Question 03: When does the default work well?
- **current_section_observation:** The map does not define when external research adds value beyond local source and target inspection.
- **supporting_reason:** It is useful for ambiguous language rules, coroutine version behavior, framework lifecycle, migration, or generated integration patterns not resolved locally.
- **counterargument_or_limit:** Many quality decisions are fully closed by target code, tests, and stable local reasoning.
- **assumptions_and_boundaries:** Retrieve only after stating the remaining versioned uncertainty and inspecting installed dependencies.
- **revision_decision:** Add research entry criteria and a local-closure short path.
- **additional_insight_to_add:** Skipping unnecessary browsing improves evidence quality by reducing irrelevant authority cues.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The seed gives no stop rule for offline work, missing authorization, mismatched versions, tutorial-only evidence, or target reproduction failure.
- **supporting_reason:** External content can distract from a local defect or encourage adoption of APIs unavailable in the target.
- **counterargument_or_limit:** An external contract can still identify why local reproduction fails.
- **assumptions_and_boundaries:** Keep the result as informative but not adopted until version and target configuration match.
- **revision_decision:** Add no-browse, mismatch, unresolved-conflict, and non-reproducible states.
- **additional_insight_to_add:** Failure to reproduce an official example is evidence about target applicability, not permission to ignore the discrepancy.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The source map does not compare official language docs, implementation repositories, maintained guides, target tests, or framework source.
- **supporting_reason:** Documentation states intended contracts, implementation and tests expose mechanics, guides show composition, and target tests establish local behavior.
- **counterargument_or_limit:** Reading implementation internals may couple guidance to non-public details.
- **assumptions_and_boundaries:** Use internals for diagnosis and version-specific understanding, not as a stable public contract unless ownership accepts that coupling.
- **revision_decision:** Add artifact-type tradeoffs and authority limits.
- **additional_insight_to_add:** A maintained guide can be the best composition example while remaining weaker than API contracts for semantic guarantees.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** The rows hide root-URL citation, mutable default branches, missing retrieval dates, version drift, secondary-source promotion, and example overgeneralization.
- **supporting_reason:** These hazards can make guidance look current and official without an auditable supporting span.
- **counterargument_or_limit:** Capturing every revision can be expensive for low-consequence orientation.
- **assumptions_and_boundaries:** Full capture is mandatory only when external content supports a consequential implementation or completion claim.
- **revision_decision:** Add minimal and promoted capture levels with clear no-claim boundaries.
- **additional_insight_to_add:** Research metadata is part of correctness when the source is mutable.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** No row demonstrates how external evidence should alter a Kotlin quality decision.
- **supporting_reason:** Good research retrieves versioned coroutine cancellation guidance and reproduces it; bad research cites a repository root to justify `GlobalScope`; borderline research finds a Spring guide on a different major version.
- **counterargument_or_limit:** The different-version guide may still reveal a useful conceptual test.
- **assumptions_and_boundaries:** Reuse the concept only after adapting and verifying it against target APIs and lifecycle.
- **revision_decision:** Add good, unsafe, and informative-but-unpromoted cases.
- **additional_insight_to_add:** Borderline external evidence should narrow experiment design rather than silently cross the version gap.

### Question 08: How can the important claims be verified?
- **current_section_observation:** The seed lacks retrieval, integrity, semantic support, version-match, and reproduction checks.
- **supporting_reason:** URL/revision capture, retrieval date, relevant span, dependency match, target test, and conflict log make external use reconstructable.
- **counterargument_or_limit:** Some hosted docs do not expose immutable revisions.
- **assumptions_and_boundaries:** Record the best available date/version identity and archive or quote only within allowed limits; rely on target tests for behavior.
- **revision_decision:** Define a required research evidence packet.
- **additional_insight_to_add:** Target reproduction is the bridge between authoritative general guidance and local engineering evidence.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** Only the retained URL strings and intended source roles are known from the seed; current content and relevance were not inspected.
- **supporting_reason:** The no-browse constraint is explicit and prevents accidental promotion.
- **counterargument_or_limit:** The organizations behind the URLs suggest likely authority for their respective surfaces.
- **assumptions_and_boundaries:** Potential authority guides future retrieval order but contributes no present factual content.
- **revision_decision:** Publish a no-results ledger for all four rows.
- **additional_insight_to_add:** Knowing where to look next is operationally valuable even when it is not evidence for the current claim.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The static list does not connect research outcomes to selective updates in this reference.
- **supporting_reason:** A Kotlin language clarification, coroutine implementation change, Spring lifecycle pattern, or Ktor plugin contract should invalidate only related guidance.
- **counterargument_or_limit:** Fine-grained refresh tracking can become stale metadata if no owner maintains it.
- **assumptions_and_boundaries:** Record invalidation triggers for adopted external claims and keep untouched rows simply unrefreshed.
- **revision_decision:** Make external research a queued, claim-scoped lifecycle rather than a recurring broad browse.
- **additional_insight_to_add:** The absence of a refresh owner should lower claim durability, not be hidden behind an official URL.

## Section 007: Anti Pattern Registry Table
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed registry contains only three generic reference-generation hazards and omits every Kotlin anti-pattern named by the canonical local source.
- **supporting_reason:** A Kotlin review needs to decide whether a construct loses input, state, identity, lifetime, cancellation, execution, or failure information on the target path.
- **counterargument_or_limit:** A large catalog can become a lexical prohibition list that penalizes legitimate bounded uses.
- **assumptions_and_boundaries:** Register causal hazards and exception evidence, not banned tokens.
- **revision_decision:** Preserve the generic rows but add a Kotlin-specific registry with contract, symptom, replacement, exception, and verification fields.
- **additional_insight_to_add:** The same syntax can be safe or unsafe depending on which owner or state distinction it erases.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** Seed replacements name source mapping and verification but do not tell a reviewer how to repair Kotlin code.
- **supporting_reason:** Normalize uncertainty, model outcomes, make identity and ownership explicit, preserve cancellation, isolate blocking, simplify receiver flow, and scope mutable state.
- **counterargument_or_limit:** Replacing every flagged construct at once can enlarge blast radius and obscure the original behavior.
- **assumptions_and_boundaries:** Repair the highest-consequence path first and characterize adjacent behavior before broader migration.
- **revision_decision:** Order registry actions by causal leverage and provide incremental containment routes.
- **additional_insight_to_add:** A narrow adapter fix can safely stop platform-type spread while a later domain migration proceeds independently.

### Question 03: When does the default work well?
- **current_section_observation:** The current rows do not identify review contexts or observable symptoms.
- **supporting_reason:** The registry is effective during changed-path review, bug diagnosis, interop audits, coroutine changes, model design, and pre-handoff risk checks.
- **counterargument_or_limit:** Generated code and framework-owned glue may not be safely editable or may intentionally follow different conventions.
- **assumptions_and_boundaries:** Review owned adapters around generated/framework code and verify lifecycle contracts instead of mechanically rewriting generated artifacts.
- **revision_decision:** Add applicability and ownership columns.
- **additional_insight_to_add:** Non-editable code still creates an editable containment boundary.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** A flat anti-pattern table has no way to represent false positives, accepted debt, migration state, or unresolved policy.
- **supporting_reason:** Treating every match as a defect can produce incorrect sealed states, unnecessary dispatcher switches, or broken framework entities.
- **counterargument_or_limit:** Too many exception states can weaken useful defaults.
- **assumptions_and_boundaries:** Require concrete invariant, owner, scope, and evidence for every exception; absence of proof keeps the review signal open.
- **revision_decision:** Add conditional, accepted-risk, blocked, and not-applicable outcomes.
- **additional_insight_to_add:** Exceptions should be cheaper to audit than the hazard they permit.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The seed does not compare replacement choices within each hazard family.
- **supporting_reason:** `T?`, sealed outcomes, typed exceptions, `Result`, enums, value objects, plain classes, named blocking APIs, dispatcher isolation, and scoped state impose different caller and migration costs.
- **counterargument_or_limit:** One universal replacement would be simpler to teach.
- **assumptions_and_boundaries:** Choose representation from caller decisions, framework contracts, and lifecycle, not pedagogical uniformity.
- **revision_decision:** Add alternative branches and selection criteria per failure mechanism.
- **additional_insight_to_add:** Replacement quality is measured by preserved obligations, not by abstraction sophistication.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Missing registry hazards include assertion crashes, temporal initialization, detached work, swallowed cancellation, hidden blocking, receiver confusion, state collapse, identity mismatch, boolean ambiguity, and global-state leakage.
- **supporting_reason:** Each can compile successfully while failing under null input, cancellation, concurrency, restart, lifecycle transition, or a new caller.
- **counterargument_or_limit:** Static detection may over-report harmless tests, generated code, or adjacent proven invariants.
- **assumptions_and_boundaries:** Combine lexical search with semantic path inspection and behavior evidence.
- **revision_decision:** Add detection signals that distinguish finding from confirmed defect.
- **additional_insight_to_add:** A finding becomes consequential when it crosses an ownership or caller-action boundary.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** The three seed rows offer no Kotlin examples or conditional cases.
- **supporting_reason:** Contrastive snippets clarify why a safe assertion beside a proven invariant differs from `request.name!!` deep in domain logic.
- **counterargument_or_limit:** Snippets can omit framework and concurrency context that determines correctness.
- **assumptions_and_boundaries:** Treat examples as minimal causal illustrations and require target evidence for adoption.
- **revision_decision:** Add compact good, unsafe, and conditional examples across major hazard families.
- **additional_insight_to_add:** The borderline example should name the missing evidence that changes its status.

### Question 08: How can the important claims be verified?
- **current_section_observation:** Seed detection methods only inspect generated references, not Kotlin behavior.
- **supporting_reason:** `rg`, compiler diagnostics, build configuration, focused null/cancellation/equality tests, thread probes, and state-isolation tests expose different hazards.
- **counterargument_or_limit:** Search can find syntax but not prove semantics; tests can miss unmodeled schedules and callers.
- **assumptions_and_boundaries:** Use search for candidate population, source tracing for contract loss, and tests or runtime evidence for behavior.
- **revision_decision:** Attach a verification ladder to each registry family.
- **additional_insight_to_add:** The denominator of a clean scan must include its paths and exclusions or the absence claim is meaningless.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The ten local anti-patterns are observed source facts, while their prevalence and severity in any target are unknown.
- **supporting_reason:** Their causal risks can be explained without claiming every occurrence is defective.
- **counterargument_or_limit:** Some teams deliberately accept these risks under framework or migration constraints.
- **assumptions_and_boundaries:** Record target occurrence, consequence, exception evidence, and owner decision separately.
- **revision_decision:** Label source-derived hazard, target finding, and accepted exception as distinct states.
- **additional_insight_to_add:** Severity is a property of a hazard in context, not a fixed property of a token.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The seed registry treats failures independently and therefore misses compound paths.
- **supporting_reason:** Platform-type leakage can lead to `!!`; detached work can hide a blocking call; broad catch can swallow cancellation; boolean result can trigger unsafe retry; global state can make tests falsely pass.
- **counterargument_or_limit:** Modeling every combination would make the table unusable.
- **assumptions_and_boundaries:** Record common causal chains and trace only combinations present on the target path.
- **revision_decision:** Add compound-failure links and prioritize root contract loss over downstream symptoms.
- **additional_insight_to_add:** Fixing the earliest information or ownership loss often removes several later anti-pattern findings at once.

## Section 008: Verification Gate Command Set
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed provides only a 202606 archive verifier command, which cannot prove target Kotlin behavior or current packet completeness by itself.
- **supporting_reason:** Reviewers need to choose the command or assertion that matches boundary, type, coroutine, blocking, state, build, analyzer, and reference-structure claims.
- **counterargument_or_limit:** A long command catalog can imply tools that the target does not configure.
- **assumptions_and_boundaries:** Discover repository-native wrappers and tasks first; commands here are gated templates except for this repository's focused verifier.
- **revision_decision:** Replace the single-command model with a dependency-ordered gate set and explicit applicability checks.
- **additional_insight_to_add:** Command existence is a prerequisite, not evidence that the command's modeled behavior covers the claim.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The seed says to run a repository verifier after editing but omits behavioral tests and target build gates.
- **supporting_reason:** Run the narrowest failing/passing behavior test, then compile/build, configured lint/static analysis, focused artifact checks, and broader regression gates.
- **counterargument_or_limit:** Some documentation-only changes have no target Kotlin test or build surface.
- **assumptions_and_boundaries:** Documentation claims still need structural and evidence-boundary review; do not invent a runtime gate for a non-runtime claim.
- **revision_decision:** Add gate profiles for implementation, review-only, coroutine, interop, blocking, and reference evolution.
- **additional_insight_to_add:** Narrow-first execution improves diagnosis, while broad gates detect integration regressions after the local mechanism is understood.

### Question 03: When does the default work well?
- **current_section_observation:** The current command has no repository, module, wrapper, or environment prerequisites.
- **supporting_reason:** The layered default works when build files and wrappers are available and focused tests can reproduce the changed distinction.
- **counterargument_or_limit:** Multi-module, composite, Android, native, or CI-only projects may require different commands and environments.
- **assumptions_and_boundaries:** Record module/profile/target and use CI or owner-provided reproduction when local execution cannot represent the supported environment.
- **revision_decision:** Add execution context and population fields to every gate result.
- **additional_insight_to_add:** A passing command without module and target identity is difficult to reuse as evidence.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The seed offers no handling for absent commands, flaky tests, environment failure, broad-suite external failures, or unsupported target execution.
- **supporting_reason:** Treating those states as green or code failures corrupts the evidence chain.
- **counterargument_or_limit:** A known external failure should not indefinitely block an unrelated focused correction.
- **assumptions_and_boundaries:** Attribute failures by owner and mechanism, preserve focused evidence, and keep the broader gate red with an explicit external condition.
- **revision_decision:** Add pass, fail, blocked, unavailable, not-applicable, and expected-external-red outcomes.
- **additional_insight_to_add:** Honest partial evidence is stronger than a silently filtered broad-suite result.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The command set does not compare tests, compilation, lint, Detekt, source search, dependency inspection, and runtime probes.
- **supporting_reason:** Tests observe selected behavior, compilation enforces types, analyzers model known patterns, search defines candidate population, and probes observe dynamic execution.
- **counterargument_or_limit:** Running every gate can be slow and duplicate CI work.
- **assumptions_and_boundaries:** Select gates by claim and blast radius; defer expensive broad gates only with a named downstream owner and trigger.
- **revision_decision:** Add a claim-to-gate matrix and cost-aware sequence.
- **additional_insight_to_add:** Orthogonal gates are valuable; redundant green commands do not compensate for one missing behavioral dimension.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Hazards include running nonexistent tasks, using global tools instead of wrappers, grepping generated code, treating lint as semantic proof, and using a legacy verifier as current completion evidence.
- **supporting_reason:** These mistakes create false negatives, false positives, non-reproducible environments, and scope overreach.
- **counterargument_or_limit:** A global tool can be useful for orientation when its result is not promoted.
- **assumptions_and_boundaries:** Label exploratory results and rerun with pinned repository configuration before completion.
- **revision_decision:** Add command provenance, population, and result-promotion rules.
- **additional_insight_to_add:** The verification environment is part of the evidence artifact, not incidental shell context.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** The seed has no contrastive command evidence.
- **supporting_reason:** Good evidence records `./gradlew :service:test --tests ...` and the cancelled fixture; bad evidence runs `detekt` globally despite no config; borderline evidence passes focused tests while a different lane keeps the shared suite red.
- **counterargument_or_limit:** Exact commands vary by repository and may include custom scripts.
- **assumptions_and_boundaries:** Preserve intent, target, population, and output status even when syntax differs.
- **revision_decision:** Add command-result cards and attribution examples.
- **additional_insight_to_add:** A borderline broad red can coexist with a valid local green only when scope and ownership are explicit.

### Question 08: How can the important claims be verified?
- **current_section_observation:** The command block lacks preconditions, expected failure reason, result parsing, and evidence retention.
- **supporting_reason:** Gate cards with command, cwd/module, environment, population, expected assertion, exit code, summary, and owner make results reproducible.
- **counterargument_or_limit:** Capturing raw logs for every command creates noise and may expose sensitive data.
- **assumptions_and_boundaries:** Retain concise summaries and only the diagnostic spans needed, with redaction where appropriate.
- **revision_decision:** Define a minimal gate-result schema and retention rule.
- **additional_insight_to_add:** Verification evidence should be small enough to review but complete enough to rerun.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The local source names representative Gradle/Maven commands and discovery queries; the seed names a legacy verifier; target project commands are unspecified.
- **supporting_reason:** These observed examples support a discovery procedure, not a claim that any particular task exists elsewhere.
- **counterargument_or_limit:** This repository's current focused verifier path is directly inspectable and can be used for Assignment 9.
- **assumptions_and_boundaries:** Separate reference-artifact verification from hypothetical target Kotlin commands.
- **revision_decision:** Label commands as current-local, inherited-example, or target-discovered.
- **additional_insight_to_add:** The same command string can have different evidentiary status depending on repository and configuration identity.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The seed treats verification as a final action rather than feedback into design.
- **supporting_reason:** A failed cancellation test, absent analyzer task, or flaky global-state test reveals ownership or tooling decisions that should change implementation and future gates.
- **counterargument_or_limit:** Not every infrastructure failure justifies changing product code.
- **assumptions_and_boundaries:** Diagnose the failure layer before editing and route environment/tooling defects to their owner.
- **revision_decision:** Make gate outcomes state transitions with changed-premise retry rules.
- **additional_insight_to_add:** Verification is most valuable when failure classification prevents the wrong layer from being "fixed."

## Section 009: Agent Usage Decision Guide
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed says to use the reference when the theme or mapped paths are mentioned, but it does not define what an agent may decide or change.
- **supporting_reason:** An agent needs a stateful contract for orientation, diagnosis, design, implementation, verification, routing, and handoff.
- **counterargument_or_limit:** Too many states can slow a simple review.
- **assumptions_and_boundaries:** Use the smallest state sequence that preserves evidence and permissions for the task.
- **revision_decision:** Replace keyword-triggered usage with intent, consequence, and evidence-based states.
- **additional_insight_to_add:** Mention of an anti-pattern is a retrieval trigger, not automatic authorization to refactor it.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The seed defaults to local source, verification patterns, external checks, and label preservation without target inspection order.
- **supporting_reason:** Clarify task and write boundary, inspect project and changed path, classify the contract loss, reproduce it where possible, choose a bounded correction, and verify before completion.
- **counterargument_or_limit:** In a pure explanation request, implementation and execution may be out of scope.
- **assumptions_and_boundaries:** Stop after a sourced decision guide when the user asks for analysis only.
- **revision_decision:** Add default state transitions conditioned on user intent and permission.
- **additional_insight_to_add:** Good agent behavior includes knowing when not to edit or run a potentially mutating build task.

### Question 03: When does the default work well?
- **current_section_observation:** The seed does not describe tasks where an agent can act autonomously with low ambiguity.
- **supporting_reason:** It works for owned Kotlin paths with visible build configuration, reproducible tests, clear caller behavior, and bounded changes.
- **counterargument_or_limit:** Cross-team shared models, framework lifecycle, production concurrency, or policy-heavy states need additional owners.
- **assumptions_and_boundaries:** Keep the agent active on evidence gathering and containment while routing the consequential choice.
- **revision_decision:** Add autonomy and escalation criteria.
- **additional_insight_to_add:** Routing one decision does not require abandoning all useful local investigation.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** There is no stop condition for missing repository context, absent permission, disputed semantics, generated code, or unsupported runtime claims.
- **supporting_reason:** Continuing in those states can invent tools, break framework contracts, or manufacture confidence.
- **counterargument_or_limit:** A read-only spike or test sketch can still clarify the blocker.
- **assumptions_and_boundaries:** Keep spikes isolated and label them proposed; do not alter production or shared ownership without authorization.
- **revision_decision:** Add explicit blocked and route-away transitions with resumable evidence.
- **additional_insight_to_add:** A durable blocked state should name the exact decision or artifact that unlocks progress.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The seed offers only use or do-not-use, omitting review-only, containment, migration, and specialist modes.
- **supporting_reason:** Modes differ in write scope, evidence burden, blast radius, and owner involvement.
- **counterargument_or_limit:** Mode labels can become process jargon if they do not change behavior.
- **assumptions_and_boundaries:** Each mode must state allowed actions, required outputs, and exit gate.
- **revision_decision:** Add operational modes with a compact transition table.
- **additional_insight_to_add:** A characterization-first mode can reduce migration risk without endorsing current semantics.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Likely agent failures include lexical replacement, broad cleanup, dependency invention, unrequested architecture change, ignored cancellation, fabricated command success, and hidden external uncertainty.
- **supporting_reason:** Agent fluency can make these outputs plausible before target contracts are understood.
- **counterargument_or_limit:** Conservative behavior can also under-deliver by stopping at generic caveats.
- **assumptions_and_boundaries:** Continue with bounded evidence, concrete options, and safe local corrections while escalating only the missing authority.
- **revision_decision:** Add both overreach and underreach hazards.
- **additional_insight_to_add:** The safest agent is not the least active one; it is the one that advances only claims and changes supported by current authority.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** The seed gives no agent trajectory examples.
- **supporting_reason:** Good behavior inspects a Java adapter, writes a nullable-return test, and proposes typed translation; bad behavior replaces all `!!` repo-wide; borderline behavior finds a framework-owned data class with uncertain identity.
- **counterargument_or_limit:** Repository-wide migration may be explicitly requested and justified.
- **assumptions_and_boundaries:** Broad work then needs inventory, ownership, characterization, staged rollout, and regression gates.
- **revision_decision:** Add trajectories with permission and promotion conditions.
- **additional_insight_to_add:** Scope changes should be explicit state transitions, not accidental consequences of search-and-replace.

### Question 08: How can the important claims be verified?
- **current_section_observation:** The usage guide has no audit record for files read, decisions made, commands run, skipped gates, or unresolved risks.
- **supporting_reason:** A concise action ledger makes agent work reviewable and resumable without exposing hidden reasoning.
- **counterargument_or_limit:** Logging every tool call creates noise and can obscure decisions.
- **assumptions_and_boundaries:** Record only evidence-bearing inputs, actions, results, scope changes, and next conditions.
- **revision_decision:** Add a minimal agent handoff packet.
- **additional_insight_to_add:** The most useful journal entry explains why the next action follows from the last observed result.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The local source supports review dimensions and defaults, but no target agent capability, repository, or Kotlin task is specified.
- **supporting_reason:** The guide can confidently define safe process invariants while leaving target implementation choices open.
- **counterargument_or_limit:** Tool availability and permissions differ across agent environments.
- **assumptions_and_boundaries:** Discover capabilities and respect explicit write/network/commit boundaries before acting.
- **revision_decision:** Separate universal operating constraints from environment-specific actions.
- **additional_insight_to_add:** Capability discovery is part of planning because an unavailable gate changes evidence status, not just convenience.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The seed treats agent use as one prompt invocation rather than a resumable control loop.
- **supporting_reason:** Long tasks need durable checkpoints, selective context reload, and phase-linked verification to prevent drift and repeated work.
- **counterargument_or_limit:** Small tasks should not require elaborate journals.
- **assumptions_and_boundaries:** Scale persistence to duration and blast radius, but always retain current state and next evidence condition.
- **revision_decision:** Add resumable state, checkpoint cadence, and completion boundaries.
- **additional_insight_to_add:** Filesystem persistence is a reliability control when agent context is finite, especially for multi-section or multi-owner work.

## Section 010: User Journey Scenario
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed journey describes a generic production-safe backend pattern and does not exercise a Kotlin quality anti-pattern or gate decision.
- **supporting_reason:** A concrete end-to-end scenario can show how platform nullability, blocking, cancellation, typed outcomes, and project gates interact.
- **counterargument_or_limit:** One service scenario cannot represent Android, Ktor, batch, library, or Kotlin/Native lifecycles.
- **assumptions_and_boundaries:** Label the scenario illustrative and extract reusable decision points rather than framework-universal steps.
- **revision_decision:** Replace generic prose with a replayable Java-client adapter journey and route variants.
- **additional_insight_to_add:** The scenario should change one premise at a time so readers can see which gate detects each contract loss.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The seed does not specify how the user proceeds from uncertainty to verified handoff.
- **supporting_reason:** Freeze scope, inspect build and dependency contracts, reproduce null/cancellation/blocking behavior, design a typed adapter, implement narrowly, and run layered gates.
- **counterargument_or_limit:** A production incident may require immediate containment before complete redesign.
- **assumptions_and_boundaries:** Incident containment remains reversible and records deferred semantic and load evidence.
- **revision_decision:** Add phase states, artifacts, commands, decisions, and rollback for the journey.
- **additional_insight_to_add:** The first failing test should isolate the contract, not merely mirror the eventual implementation shape.

### Question 03: When does the default work well?
- **current_section_observation:** No prerequisites are listed for the journey.
- **supporting_reason:** It works when the Java dependency can be faked or wrapped, callers are bounded, and coroutine tests can control cancellation.
- **counterargument_or_limit:** Closed-source/native clients or framework-managed threads may resist deterministic fixtures.
- **assumptions_and_boundaries:** Use a contract adapter and black-box probe; route unobservable interruption or capacity semantics to the dependency/operations owner.
- **revision_decision:** Add prerequisite and fallback paths.
- **additional_insight_to_add:** Wrapping an opaque client creates a stable test boundary even when its internals remain unavailable.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The generic journey has no branch for disputed domain outcome meaning or broad shared callers.
- **supporting_reason:** A typed outcome is unsafe if product owners have not decided whether null means absent, denied, stale, or dependency failure.
- **counterargument_or_limit:** The adapter can preserve raw distinctions temporarily without choosing caller policy.
- **assumptions_and_boundaries:** Avoid collapsing states; expose a provisional internal taxonomy and route public meaning to the owner.
- **revision_decision:** Add blocked semantic and staged-migration branches.
- **additional_insight_to_add:** Delaying public naming is safer than prematurely naming the wrong domain state.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The seed journey does not compare nullable return, sealed outcome, typed exception, synchronous wrapper, dispatcher isolation, or durable async work.
- **supporting_reason:** Choices affect call-site exhaustiveness, framework mapping, cancellation, thread occupancy, migration, and operational complexity.
- **counterargument_or_limit:** Showing all alternatives can distract from the main path.
- **assumptions_and_boundaries:** Present a primary route plus branch conditions, not parallel full implementations.
- **revision_decision:** Add a decision table at the point each premise matters.
- **additional_insight_to_add:** Blocking versus durable async is an architecture decision; dispatcher isolation is only a local execution policy.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** The seed lacks journey-specific hazards such as fake clients that never return null, cancellation tests that do not enter the call, or boolean translation that recreates ambiguity.
- **supporting_reason:** A test can pass while failing to exercise the dangerous branch or while the public API still loses the distinction.
- **counterargument_or_limit:** Over-instrumented fixtures can diverge from the real dependency.
- **assumptions_and_boundaries:** Keep fixtures contract-focused and supplement with integration evidence where dependency behavior is consequential.
- **revision_decision:** Add fixture validity, call-entry synchronization, and caller-mapping checks.
- **additional_insight_to_add:** Deterministic cancellation tests need proof that cancellation occurs after the child enters the suspending or blocking boundary.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** The seed journey contains no concrete code or outcome comparison.
- **supporting_reason:** A good path converts nullable Java output and preserves cancellation; a bad path uses `!!`, detached work, and false; a borderline path safely wraps blocking but lacks load evidence.
- **counterargument_or_limit:** Code snippets can imply APIs that the target does not use.
- **assumptions_and_boundaries:** Use pseudocode-level Kotlin and label all identities and results illustrative.
- **revision_decision:** Add contrastive checkpoints rather than a copy-ready framework implementation.
- **additional_insight_to_add:** The borderline path can be behaviorally correct yet operationally unpromoted.

### Question 08: How can the important claims be verified?
- **current_section_observation:** The journey gives no tests, commands, result cards, or completion population.
- **supporting_reason:** Null fixture, exhaustive outcome test, parent-cancellation test, execution-context observation, build, configured analyzer, and broader regression gates close different claims.
- **counterargument_or_limit:** Runtime saturation remains unmeasured in a local deterministic journey.
- **assumptions_and_boundaries:** End the scenario with a no-capacity-claim state unless a controlled experiment runs.
- **revision_decision:** Add phase-linked evidence and explicit deferred runtime gate.
- **additional_insight_to_add:** Handoff should separate semantic completion from operational promotion.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The role, service, client, code, and outcomes in the rewritten journey will be invented for teaching rather than observed.
- **supporting_reason:** An illustrative fixture can faithfully demonstrate the local source's causal rules without claiming a real result.
- **counterargument_or_limit:** Readers may still mistake precise names or command outputs for repository facts.
- **assumptions_and_boundaries:** Mark identities, commands, and outcomes illustrative and avoid fabricated pass times or metrics.
- **revision_decision:** Include a scenario evidence legend and no-results statement.
- **additional_insight_to_add:** Precision in a teaching example should describe decisions and assertions, not invented measurements.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** A linear journey can hide that findings should update future adapters and shared tests.
- **supporting_reason:** Once one Java boundary demonstrates the failure family, the repository can inventory sibling adapters and standardize a narrow contract helper.
- **counterargument_or_limit:** Generalizing immediately can overfit one client and expand scope.
- **assumptions_and_boundaries:** Promote after confirming shared semantics or recurrence and obtaining owner scope.
- **revision_decision:** End with selective follow-up routes rather than automatic repository migration.
- **additional_insight_to_add:** A verified local fix creates a hypothesis for broader review, not proof that every sibling boundary shares the defect.

## Section 011: Decision Tradeoff Guide
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed table only says adopt, adapt, avoid, and cost of being wrong for the theme as a whole.
- **supporting_reason:** Kotlin quality choices need claim-specific comparisons because representation, concurrency, execution, and migration alternatives have different consequences.
- **counterargument_or_limit:** Too many matrices can imply that every small code choice requires architecture review.
- **assumptions_and_boundaries:** Use a matrix only when alternatives change caller behavior, lifecycle, failure, or blast radius.
- **revision_decision:** Replace generic rows with concrete decision families plus a compact adopt/adapt/avoid overlay.
- **additional_insight_to_add:** The relevant tradeoff is the one a caller or operator experiences, not which syntax looks most idiomatic.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The seed default depends on local/external agreement rather than target semantics.
- **supporting_reason:** Choose the simplest representation and ownership model that preserves all consequential distinctions and can be verified in the target.
- **counterargument_or_limit:** Compatibility or framework constraints may force a less direct public representation.
- **assumptions_and_boundaries:** Contain translation at the boundary and keep the internal contract explicit where possible.
- **revision_decision:** Add a consequence-first default and explicit compatibility adaptation.
- **additional_insight_to_add:** A locally verbose internal type can simplify the rest of the system even when the framework-facing boundary remains constrained.

### Question 03: When does the default work well?
- **current_section_observation:** The table lacks favorable conditions for each choice.
- **supporting_reason:** Simple explicit defaults work when state space is closed, callers are known, lifecycle ownership is bounded, and behavior tests are available.
- **counterargument_or_limit:** Plugin ecosystems, public libraries, persistence schemas, and open extension points may require compatibility and openness.
- **assumptions_and_boundaries:** Treat public and persistence contracts as migration surfaces with versioning and compatibility evidence.
- **revision_decision:** Add fit conditions per alternative.
- **additional_insight_to_add:** Internal and external representations can differ when one narrow translator owns the impedance mismatch.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The seed avoid row focuses on thin evidence but not semantic over-modeling or under-modeling.
- **supporting_reason:** Sealed outcomes fail for genuinely open protocols; nullable values fail when states differ; dispatcher isolation fails when durable work is required; data classes fail for lifecycle identity.
- **counterargument_or_limit:** Each choice can be adapted with boundaries and documentation.
- **assumptions_and_boundaries:** Adaptation is valid only if caller obligations and failure behavior remain testable.
- **revision_decision:** Add wrong-choice signals and route-away conditions.
- **additional_insight_to_add:** A choice becomes wrong when its convenience depends on callers reconstructing information that the API discarded.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** Concrete alternatives are absent from the seed.
- **supporting_reason:** Key pairs include `T?` versus closed state, sealed outcome versus typed exception, data versus plain class, `coroutineScope` versus supervision, blocking API versus isolation, injection versus global state, and focused repair versus migration.
- **counterargument_or_limit:** Some choices are not mutually exclusive and compose at different layers.
- **assumptions_and_boundaries:** State the layer and caller before comparing; avoid false either/or framing.
- **revision_decision:** Build matrices that show composition and boundary ownership.
- **additional_insight_to_add:** Many Kotlin tradeoffs are placement decisions: where translation, supervision, or execution policy should live.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** The generic table hides migration compatibility, exhaustiveness erosion, exception leakage, supervision misuse, and dispatcher cargo-culting.
- **supporting_reason:** These failures often appear when a locally appealing option is promoted without tracing all callers and lifecycle owners.
- **counterargument_or_limit:** Exhaustive analysis can be disproportionate for private leaf functions.
- **assumptions_and_boundaries:** Scale caller inventory and migration evidence to visibility and consequence.
- **revision_decision:** Add a cost-of-being-wrong column and minimal caller inventory rule.
- **additional_insight_to_add:** Publicness, persistence, and concurrency multiply the cost of a wrong representation choice.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** Seed examples are absent from the tradeoff table.
- **supporting_reason:** Good choices name caller actions and tests; bad choices follow fashion; borderline choices preserve compatibility through a translation shim.
- **counterargument_or_limit:** A shim can become permanent and duplicate semantics.
- **assumptions_and_boundaries:** Give shims ownership, deprecation or review trigger, and equivalence tests.
- **revision_decision:** Add contrastive option records and shim safeguards.
- **additional_insight_to_add:** A compatibility shim is architecture when it intentionally contains disagreement, not when it merely postpones understanding.

### Question 08: How can the important claims be verified?
- **current_section_observation:** Verification questions in the seed ask only whether evidence labels exist.
- **supporting_reason:** Caller inventory, exhaustive compilation, branch tests, cancellation tests, identity tests, concurrency probes, and migration compatibility checks verify option-specific risks.
- **counterargument_or_limit:** Some operational tradeoffs remain uncertain until production-like load.
- **assumptions_and_boundaries:** Separate semantic acceptance from operational promotion and record deferred measurement.
- **revision_decision:** Attach a verification signature to each decision family.
- **additional_insight_to_add:** Alternatives should be compared under equivalent behavior before cost or performance comparisons are accepted.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** Local source facts identify preferred defaults but do not rank every alternative or target cost.
- **supporting_reason:** The causal failure boundaries are strong; migration, framework fit, and performance cost are target-specific.
- **counterargument_or_limit:** Stable ecosystem conventions can make some target choices predictable.
- **assumptions_and_boundaries:** Verify conventions against installed configuration and avoid universal cost estimates.
- **revision_decision:** Label default rationale separately from target cost judgment.
- **additional_insight_to_add:** Confidence in semantic safety can coexist with uncertainty about migration effort or runtime cost.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The seed treats a decision as final once adopt/adapt/avoid is chosen.
- **supporting_reason:** Shared APIs, framework upgrades, new callers, and observed load can change the preferred tradeoff later.
- **counterargument_or_limit:** Constant reconsideration destabilizes code.
- **assumptions_and_boundaries:** Reopen only on explicit invalidation triggers, not preference changes.
- **revision_decision:** Add decision expiry and selective review triggers.
- **additional_insight_to_add:** Durable decisions record why the rejected alternatives lost under the current premises, making later reassessment faster.

## Section 012: Local Corpus Hierarchy
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed calls one source canonical and warns that one source is thin, but it does not explain authority when local guidance, target code, tests, build configuration, and owner policy differ.
- **supporting_reason:** Claim-specific authority prevents a prose source from overriding observed behavior or a passing test from inventing policy.
- **counterargument_or_limit:** A partial order is harder to scan than a single canonical label.
- **assumptions_and_boundaries:** Use a compact precedence rule per claim rather than one universal ranking.
- **revision_decision:** Expand the hierarchy into local evidence roles, conflicts, and target-closure requirements.
- **additional_insight_to_add:** Canonical describes authority for a question, not global superiority of one file.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The seed suggests adjacent-source discovery without defining what evidence gap should trigger it.
- **supporting_reason:** Begin with the archive source for inherited principles, then use target repository artifacts for actual configuration and behavior, and route policy or runtime acceptance to owners.
- **counterargument_or_limit:** Current installed guidance may exist outside the mapped corpus and be newer.
- **assumptions_and_boundaries:** Discover adjacent local sources when a concrete claim remains unresolved; identify and compare them before promotion.
- **revision_decision:** Add gap-triggered discovery and replacement rules.
- **additional_insight_to_add:** Adjacent-source discovery should be hypothesis-driven so more files do not masquerade as more certainty.

### Question 03: When does the default work well?
- **current_section_observation:** The hierarchy does not name claims the archive source can close directly.
- **supporting_reason:** It can close what inherited guidance says and support stable causal defaults for review and discovery.
- **counterargument_or_limit:** It cannot close target tool availability, framework version behavior, domain state meaning, or production capacity.
- **assumptions_and_boundaries:** Match each conclusion to the narrow authority that can own it.
- **revision_decision:** Add authority-by-claim examples.
- **additional_insight_to_add:** Thin source count is less dangerous when each claim's remaining evidence need is explicit.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** A canonical-primary label could be interpreted as overriding target code or newer local policy.
- **supporting_reason:** That would preserve stale commands or reject legitimate framework constraints.
- **counterargument_or_limit:** Target code can itself embody a defect and should not automatically outrank safer guidance.
- **assumptions_and_boundaries:** Target code is authoritative for current implementation fact, not desired behavior; combine it with tests and owner policy.
- **revision_decision:** Separate descriptive authority from normative authority and behavioral evidence.
- **additional_insight_to_add:** Conflict often disappears when claims are split into "what exists," "what should exist," and "what happens."

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The seed vocabulary lists canonical, supporting, legacy, duplicate, and conflicting roles but applies only canonical.
- **supporting_reason:** Additional roles help preserve historical rationale, independent evidence, and disagreement.
- **counterargument_or_limit:** Assigning roles without content identity can overstate independence.
- **assumptions_and_boundaries:** Hash or lineage-check local sources and assign role by claim contribution.
- **revision_decision:** Define every role and distinguish duplicate from corroborating evidence.
- **additional_insight_to_add:** Two files with different names can still be one evidence family.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Risks include canonical-by-path, newest-by-date, test-as-policy, code-as-correctness, duplicate counting, and silent conflict resolution.
- **supporting_reason:** Each shortcut hides one dimension of authority and produces non-auditable guidance.
- **counterargument_or_limit:** Formal conflict logs can be excessive for trivial stylistic differences.
- **assumptions_and_boundaries:** Record conflicts that change behavior, caller obligations, lifecycle, or completion; resolve cosmetic differences locally.
- **revision_decision:** Add hierarchy hazards and materiality threshold.
- **additional_insight_to_add:** A conflict is material when choosing either side changes a test, caller, operation, or risk acceptance.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** The seed reviewer question is generic and gives no authority example.
- **supporting_reason:** Good use treats the archive source as guidance, target tests as behavior, and domain owner as state-meaning authority; bad use lets a tutorial override all three.
- **counterargument_or_limit:** Borderline cases arise when target tests preserve legacy behavior that owners want to change.
- **assumptions_and_boundaries:** Label characterization versus desired contract and stage migration.
- **revision_decision:** Add conflict scenarios with resolution state.
- **additional_insight_to_add:** A failing desired-contract test can be stronger normative evidence than a passing characterization test, provided owner intent is explicit.

### Question 08: How can the important claims be verified?
- **current_section_observation:** No checks confirm source identity, role, independence, conflict coverage, or target closure.
- **supporting_reason:** Hashes, lineage notes, claim matrices, test results, config inspection, and owner decisions make hierarchy decisions reproducible.
- **counterargument_or_limit:** Independence is sometimes impossible to prove from local artifacts alone.
- **assumptions_and_boundaries:** Mark uncertain lineage rather than counting it as corroboration.
- **revision_decision:** Add an authority decision record and identity gate.
- **additional_insight_to_add:** Unknown lineage should lower evidence diversity without discarding potentially useful content.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** One mapped source and its hash are known; no adjacent source inventory or organizational designation was performed.
- **supporting_reason:** It is safely canonical for inherited content in this assignment, not necessarily current enterprise Kotlin policy.
- **counterargument_or_limit:** Archive placement and naming may reflect an established policy process not visible here.
- **assumptions_and_boundaries:** Do not infer governance from path; require explicit current owner evidence.
- **revision_decision:** Tighten the canonical claim and retain the confidence warning.
- **additional_insight_to_add:** Provenance certainty and governance authority are separate properties.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The hierarchy is static and file-centered rather than claim-centered and versioned.
- **supporting_reason:** A source can be canonical for anti-pattern definitions, supporting for commands, legacy for a plugin version, and conflicting for one framework behavior.
- **counterargument_or_limit:** Per-claim roles require maintenance.
- **assumptions_and_boundaries:** Apply fine-grained roles to consequential or reused claims; keep simple notes for one-off local decisions.
- **revision_decision:** Introduce claim-role-version tuples and selective invalidation.
- **additional_insight_to_add:** Source authority is multidimensional, so one file can legitimately occupy several roles at once.

## Section 013: Theme Specific Artifact
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed names a quality bar rubric but provides only goal, boundary, and verification rows, which are insufficient to review a Kotlin change.
- **supporting_reason:** A structured evidence packet can decide whether findings are confirmed, exceptions are bounded, gates match claims, and release blockers remain.
- **counterargument_or_limit:** A large artifact can burden tiny changes and duplicate pull-request templates.
- **assumptions_and_boundaries:** Make fields claim-relative and allow a compact profile when only one low-risk distinction changes.
- **revision_decision:** Define a scalable Kotlin Quality Evidence Packet with core and conditional fields.
- **additional_insight_to_add:** Artifact completeness should depend on the claims made, not on filling every possible field.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The seed does not define how to populate or approve the artifact.
- **supporting_reason:** Capture target identity, changed boundary, lost contract, chosen representation/ownership, findings, evidence, exceptions, blockers, rollback, and owners before completion.
- **counterargument_or_limit:** Some fields emerge only after reproduction and design.
- **assumptions_and_boundaries:** Treat the packet as a living decision record with state transitions, not a front-loaded form.
- **revision_decision:** Add required-at-entry, required-before-edit, and required-before-handoff stages.
- **additional_insight_to_add:** Stage-specific completeness prevents both premature paperwork and late discovery of missing authority.

### Question 03: When does the default work well?
- **current_section_observation:** No artifact profile or fit criteria exist.
- **supporting_reason:** It works for code review, focused repair, interop adaptation, coroutine changes, model redesign, staged migration, and release evidence.
- **counterargument_or_limit:** Pure orientation or a one-line private predicate may only need a short finding and test result.
- **assumptions_and_boundaries:** Select compact, standard, or migration profile by visibility, concurrency, persistence, and blast radius.
- **revision_decision:** Add profile selection and minimum fields.
- **additional_insight_to_add:** Profiles preserve one schema across task sizes without forcing identical evidence volume.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The seed artifact can be completed with generic prose while leaving code and gate status unclear.
- **supporting_reason:** Checkbox artifacts fail when evidence links, populations, owner decisions, and blocked claims are optional.
- **counterargument_or_limit:** Excessively rigid schemas encourage cosmetic compliance.
- **assumptions_and_boundaries:** Require evidence-bearing content but permit explicit not-applicable and blocked states with reasons.
- **revision_decision:** Add anti-filler validation and claim-to-evidence traceability.
- **additional_insight_to_add:** A blank field and a justified non-applicable field carry different operational information.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The seed does not compare inline review notes, pull-request templates, machine-readable manifests, test names, or separate design records.
- **supporting_reason:** Inline notes are local, templates aid handoff, structured manifests support automation, and design records preserve broad decisions.
- **counterargument_or_limit:** Splitting evidence across artifacts can fragment review.
- **assumptions_and_boundaries:** Choose one canonical packet and link supporting artifacts by stable identifiers.
- **revision_decision:** Define the schema independent of storage format and require one index.
- **additional_insight_to_add:** Artifact location is secondary to single-source traceability for claim status.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Missing hazards include generic goal text, unscoped clean scans, passing commands without populations, exceptions without invariants, and blocked decisions reported as complete.
- **supporting_reason:** These allow a polished rubric to conceal the exact risks it should expose.
- **counterargument_or_limit:** Reviewers can catch some defects informally.
- **assumptions_and_boundaries:** Formalize only high-value blockers and evidence links; keep narrative concise.
- **revision_decision:** Add artifact validation rules and blocker severity semantics.
- **additional_insight_to_add:** The packet should make false completion harder than honest uncertainty.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** No populated artifact example appears in the seed.
- **supporting_reason:** A good example links a platform-type finding to adapter diff and null test; a bad example says "null safety improved"; a borderline example has semantic gates green but runtime blocking unmeasured.
- **counterargument_or_limit:** A filled example can be mistaken for a mandated technology stack.
- **assumptions_and_boundaries:** Keep the example technology-light and label values illustrative.
- **revision_decision:** Add one compact populated packet and explicit no-result field.
- **additional_insight_to_add:** Borderline evidence should produce a split completion state rather than an all-or-nothing label.

### Question 08: How can the important claims be verified?
- **current_section_observation:** The seed artifact has no schema-level validation or traceability check.
- **supporting_reason:** Required-field states, stable claim IDs, evidence links, population declarations, uniqueness, and blocker rules can be reviewed or partially automated.
- **counterargument_or_limit:** Automation cannot judge whether domain states are meaningful.
- **assumptions_and_boundaries:** Use structural checks for completeness and human/behavior review for semantics.
- **revision_decision:** Add structural and semantic acceptance gates.
- **additional_insight_to_add:** Automation is most reliable for proving that evidence is present and linked, not that the evidence supports the conclusion.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The theme artifact type is a seed requirement, but no repository has adopted or measured this expanded schema.
- **supporting_reason:** The fields follow directly from local hazards and gate requirements.
- **counterargument_or_limit:** Usability, review cost, and tool integration remain untested.
- **assumptions_and_boundaries:** Present the schema as a proposed reusable contract and calibrate it in target workflows.
- **revision_decision:** Label adoption and efficiency outcomes as unknown.
- **additional_insight_to_add:** A well-reasoned schema still needs usage feedback before becoming mandatory organization-wide policy.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The seed frames the artifact as final review output rather than a source for future learning.
- **supporting_reason:** Structured finding and gate data can reveal recurring boundary, cancellation, blocking, identity, or state-scope failures.
- **counterargument_or_limit:** Aggregation can incentivize gaming and lose context.
- **assumptions_and_boundaries:** Aggregate stable categories with counter-metrics and retain links to original evidence.
- **revision_decision:** Add feedback and selective-control promotion fields.
- **additional_insight_to_add:** The artifact can justify removing obsolete gates as well as adding shared controls when evidence shows low value or duplication.

## Section 014: Worked Example Set
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed has one generic good, bad, and borderline sentence about source usage, not Kotlin code or review behavior.
- **supporting_reason:** Orthogonal examples help readers classify target findings without turning constructs into universal bans.
- **counterargument_or_limit:** Examples can become cargo-cult templates when context is omitted.
- **assumptions_and_boundaries:** Make each fixture minimal, causal, explicitly illustrative, and paired with a target verification requirement.
- **revision_decision:** Add six failure families with good, unsafe, and conditional variants.
- **additional_insight_to_add:** Examples should teach the decision boundary, not just the preferred syntax.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The seed good example focuses on source loading rather than a repair sequence.
- **supporting_reason:** For each fixture, name the lost contract, restore it at the earliest boundary, update callers coherently, and test the dangerous branch.
- **counterargument_or_limit:** Existing compatibility may require temporary translation after the earliest boundary.
- **assumptions_and_boundaries:** Keep translation narrow and test equivalence until migration completes.
- **revision_decision:** Structure examples as context, failure, repair, gate, and remaining uncertainty.
- **additional_insight_to_add:** A repair example is incomplete if it does not show what the caller must now do differently.

### Question 03: When does the default work well?
- **current_section_observation:** Seed examples have no prerequisites or applicability notes.
- **supporting_reason:** Minimal fixtures work when a single boundary or ownership mechanism can be isolated and its caller action observed.
- **counterargument_or_limit:** Framework proxies, generated models, and opaque clients may require integration rather than unit examples.
- **assumptions_and_boundaries:** Escalate fixture level while preserving the same causal assertion.
- **revision_decision:** Add fixture-level alternatives.
- **additional_insight_to_add:** Unit and integration examples can test the same contract at different evidence strengths.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The seed borderline case only mentions thin evidence and not misleading example transfer.
- **supporting_reason:** Copying a server dispatcher example into Android UI code or a value data class into persistence identity can create new defects.
- **counterargument_or_limit:** Cross-domain examples can still illustrate stable principles.
- **assumptions_and_boundaries:** Transfer the principle, then re-derive lifecycle, framework, and caller mechanics.
- **revision_decision:** Add explicit non-transfer warnings.
- **additional_insight_to_add:** Similar syntax does not imply similar ownership.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** No example compares multiple valid repairs.
- **supporting_reason:** Showing nullable, sealed, exception, plain-class, dispatcher, and scope alternatives reveals why context selects the route.
- **counterargument_or_limit:** Too many variants can overwhelm the causal lesson.
- **assumptions_and_boundaries:** Include one primary route and one conditional alternative per fixture.
- **revision_decision:** Add bounded alternatives with selection criteria.
- **additional_insight_to_add:** Examples are stronger when they demonstrate that the default is defeasible under a named premise.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Example hazards include fake fixtures that miss null/cancellation, equality tests that ignore persistence, thread switches that hide blocking, and isolated tests that mask global state leakage.
- **supporting_reason:** These fixtures can appear comprehensive while failing to exercise the mechanism.
- **counterargument_or_limit:** Perfect realism is impossible and can make tests flaky.
- **assumptions_and_boundaries:** Synchronize and minimize the causal event; supplement with integration/runtime evidence only where needed.
- **revision_decision:** Add fixture-validity questions to every example.
- **additional_insight_to_add:** Determinism should control the relevant schedule or input, not simulate the entire production system.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** This is the section's explicit purpose, but the seed examples are generic process slogans.
- **supporting_reason:** Concrete contrast across six Kotlin mechanisms exposes both unsafe defaults and legitimate exceptions.
- **counterargument_or_limit:** "Good" remains target-relative and should not be copied unchanged.
- **assumptions_and_boundaries:** Label all snippets conceptual and retain no-claim boundaries.
- **revision_decision:** Present a repeated comparison format for easy scanning.
- **additional_insight_to_add:** Borderline examples need a promotion gate, not a vague warning.

### Question 08: How can the important claims be verified?
- **current_section_observation:** The seed examples attach no commands, tests, or review assertions.
- **supporting_reason:** Null fixtures, cancellation synchronization, identity tests, thread observation, state isolation, and caller exhaustiveness each verify their example's mechanism.
- **counterargument_or_limit:** Example code cannot prove tool availability or framework integration.
- **assumptions_and_boundaries:** Use example assertions as test designs, then instantiate them in the target repository.
- **revision_decision:** Add evidence signatures and expected failure modes.
- **additional_insight_to_add:** A worked example should be falsifiable even when it is not directly executable.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** All expanded snippets and contexts will be newly synthesized, not observed target code.
- **supporting_reason:** They can faithfully express locally sourced causal risks and verification principles.
- **counterargument_or_limit:** Framework APIs, versions, and performance behavior remain unspecified.
- **assumptions_and_boundaries:** Avoid concrete external API claims and fabricated outputs.
- **revision_decision:** Add an illustrative-only legend and remaining uncertainty per fixture.
- **additional_insight_to_add:** The examples can be precise about invariants while remaining deliberately noncommittal about target tooling.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** Independent examples can still obscure shared root causes.
- **supporting_reason:** Comparing fixtures reveals recurring information and ownership loss across nullability, identity, cancellation, blocking, and state.
- **counterargument_or_limit:** A universal abstraction for all failures would be too broad.
- **assumptions_and_boundaries:** Reuse the review questions, not necessarily one code abstraction.
- **revision_decision:** End with cross-example deductions and selective promotion rules.
- **additional_insight_to_add:** Shared mental models often scale better than shared helper libraries when mechanisms differ.

## Section 015: Outcome Metrics and Feedback Loops
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed supplies a one-session lead-time target, a guessed-framework failure signal, and a refresh cadence without baseline, denominator, or measurement method.
- **supporting_reason:** Metrics should decide whether gates expose contract loss early, create useful evidence, reduce recurrence, or impose harmful review cost.
- **counterargument_or_limit:** Small samples and changing task mix make broad quality trends noisy.
- **assumptions_and_boundaries:** Use metric cards with cohort, denominator, counter-metric, uncertainty, and no-causal-overreach.
- **revision_decision:** Replace unsupported targets with proposed measures and explicit unbaselined status.
- **additional_insight_to_add:** The first feedback question is whether a metric can change a gate or workflow decision.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The seed does not separate deterministic gate data from sampled workflow or downstream outcome metrics.
- **supporting_reason:** Capture deterministic completeness and finding data first, then sampled review outcomes, and only later comparable downstream trends.
- **counterargument_or_limit:** Deterministic counts can be gamed and do not prove quality.
- **assumptions_and_boundaries:** Pair counts with reversals, false positives, rework, and escaped defects.
- **revision_decision:** Define three metric layers and mandatory counter-metrics.
- **additional_insight_to_add:** A rising finding count can mean worse code or better detection, so interpretation needs exposure and outcome context.

### Question 03: When does the default work well?
- **current_section_observation:** No data prerequisites or cohort boundaries are named.
- **supporting_reason:** Feedback works when finding classes are stable, claim populations are recorded, review outcomes are linked, and comparable tasks can be sampled.
- **counterargument_or_limit:** Early adoption may have too little data for trend claims.
- **assumptions_and_boundaries:** Use qualitative case review and deterministic checks until samples support aggregation.
- **revision_decision:** Add maturity stages and minimum interpretability criteria without invented sample sizes.
- **additional_insight_to_add:** Absence of enough data should produce no trend claim, not a favorable zero.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** A speed target can reward smaller scope, skipped gates, or premature completion.
- **supporting_reason:** Single-axis metrics invite gaming and can worsen semantic quality or reviewer burden.
- **counterargument_or_limit:** Time and cost still matter for sustainable gates.
- **assumptions_and_boundaries:** Pair lead time with blocker accuracy, rework, escaped mechanisms, and review burden.
- **revision_decision:** Add gaming signals and stop rules for harmful metrics.
- **additional_insight_to_add:** A gate that catches defects but doubles low-risk review cost may need targeting rather than removal.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The seed names only one leading indicator and one failure signal.
- **supporting_reason:** Alternatives include finding prevalence, boundary escapes, cancellation coverage, blocker age, gate precision, review reversals, rework, recurrence, and runtime regressions.
- **counterargument_or_limit:** Too many metrics create reporting overhead and contradictory incentives.
- **assumptions_and_boundaries:** Choose a small metric set tied to the control being calibrated.
- **revision_decision:** Provide a menu with decision use rather than a mandatory dashboard.
- **additional_insight_to_add:** Metrics should be retired when they no longer change a decision or their collection cost exceeds value.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Missing hazards include denominator drift, duplicate findings, severity mixing, survivorship bias, no-data-as-zero, unlinked rework, and correlation-as-causation.
- **supporting_reason:** These errors can make gate adoption look effective or harmful without comparable evidence.
- **counterargument_or_limit:** Perfect experimental control is unrealistic in normal engineering work.
- **assumptions_and_boundaries:** Record enough context for bounded interpretation and state uncertainty instead of claiming causality.
- **revision_decision:** Add metric validity checks and prohibited interpretations.
- **additional_insight_to_add:** A transparent imperfect metric is more useful than a precise-looking number with an unstable denominator.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** No metric examples or interpretation cases appear in the seed.
- **supporting_reason:** Good metrics define numerator, denominator, cohort, collection, counter-metric, and action; bad metrics count all `!!`; borderline metrics show fewer findings after an analyzer baseline change.
- **counterargument_or_limit:** Detailed cards take effort to maintain.
- **assumptions_and_boundaries:** Require full cards only for metrics used to govern policy or claim improvement.
- **revision_decision:** Add example metric cards and interpretation warnings.
- **additional_insight_to_add:** Tool configuration changes must create a series boundary rather than being interpreted as sudden code improvement.

### Question 08: How can the important claims be verified?
- **current_section_observation:** The seed offers no reproducible data collection or audit.
- **supporting_reason:** Stable IDs, packet states, gate results, review outcomes, escaped-defect links, and versioned metric definitions support reconstruction.
- **counterargument_or_limit:** Linking incidents or reviews may expose sensitive or personal data.
- **assumptions_and_boundaries:** Aggregate minimally, redact sensitive content, and avoid individual performance scoring.
- **revision_decision:** Add data provenance, privacy, and recomputation requirements.
- **additional_insight_to_add:** Quality metrics should evaluate controls and systems, not rank individual developers or agents.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** No target measurements were performed, so all expanded metric definitions lack baselines and observed values.
- **supporting_reason:** The reference can specify sound measurement contracts without fabricating results.
- **counterargument_or_limit:** Some deterministic counts will be available as soon as a packet is used.
- **assumptions_and_boundaries:** Report those counts as observations for their population, not as improvement.
- **revision_decision:** Label every metric proposed, observed, compared, or retired.
- **additional_insight_to_add:** Measurement readiness and positive performance are different states.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The seed feedback loop only reruns a verifier and refreshes sources.
- **supporting_reason:** Findings and outcomes should recalibrate gate targeting, exception policy, shared adapters, test helpers, and source freshness.
- **counterargument_or_limit:** Automated policy changes from noisy data can amplify errors.
- **assumptions_and_boundaries:** Require human review, causal case inspection, and reversible trials before changing defaults.
- **revision_decision:** Add observe, interpret, propose, trial, compare, adopt/rollback loop.
- **additional_insight_to_add:** Feedback can remove redundant gates or narrow scans, not only add restrictions.

## Section 016: Completeness Checklist
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed checklist checks whether seven document sections exist, not whether a Kotlin claim is semantically or behaviorally complete.
- **supporting_reason:** Completion must distinguish artifact integrity from target contract closure and operational promotion.
- **counterargument_or_limit:** A comprehensive checklist can become repetitive with the KQEP schema.
- **assumptions_and_boundaries:** Use the checklist as an acceptance projection over the packet, not a second narrative artifact.
- **revision_decision:** Replace presence checks with claim-relative prerequisite gates and profiles.
- **additional_insight_to_add:** A complete document can accurately describe incomplete engineering work.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The seed gives no order or blocker semantics.
- **supporting_reason:** Verify identity/scope, evidence boundaries, semantics, ownership, focused behavior, integration, configured checks, broader regression, operations, and handoff in dependency order.
- **counterargument_or_limit:** Not every change requires runtime or broad migration evidence.
- **assumptions_and_boundaries:** Mark non-applicable gates with claim-specific reasons and preserve no-claim boundaries.
- **revision_decision:** Add core and conditional completion layers.
- **additional_insight_to_add:** Conditional gates prevent universal process while keeping omitted claims visible.

### Question 03: When does the default work well?
- **current_section_observation:** No task profile connects to checklist depth.
- **supporting_reason:** Claim-relative completion works for compact repairs, standard changes, migrations, review-only tasks, and routed work.
- **counterargument_or_limit:** Emergency containment may intentionally leave several gates open.
- **assumptions_and_boundaries:** Report containment complete and full resolution incomplete, with owner and next trigger.
- **revision_decision:** Add completion profiles and split states.
- **additional_insight_to_add:** Completion should name the scope achieved rather than force one global done label.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** Checklist use can reward box-ticking or block harmless changes with irrelevant gates.
- **supporting_reason:** Generic green labels and unjustified mandatory gates both weaken trust.
- **counterargument_or_limit:** Strict defaults can expose routinely skipped negative paths.
- **assumptions_and_boundaries:** Require reasons and evidence for both pass and non-applicability; audit recurring exclusions.
- **revision_decision:** Add anti-filler and exclusion-review rules.
- **additional_insight_to_add:** Repeated not-applicable decisions may reveal a mis-targeted gate or an unmodeled common profile.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The seed has one flat checklist and no choice among code, review, migration, or release completeness.
- **supporting_reason:** Different completion lenses reduce ambiguity between semantic fix, integration readiness, operational promotion, and document quality.
- **counterargument_or_limit:** Multiple statuses can confuse stakeholders seeking one release decision.
- **assumptions_and_boundaries:** Provide one summary decision with the underlying split states visible.
- **revision_decision:** Add completion matrix and explicit summary rule.
- **additional_insight_to_add:** A single release decision can be derived without collapsing its evidence dimensions.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Missing checks include wrong target identity, unverified exceptions, lost caller branches, swallowed cancellation, hidden blocking, analyzer population gaps, and broad external reds.
- **supporting_reason:** These omissions let locally green evidence overstate completion.
- **counterargument_or_limit:** Some are already covered elsewhere in the file.
- **assumptions_and_boundaries:** The final checklist links to evidence rather than restating analysis.
- **revision_decision:** Add concise blocker-oriented assertions.
- **additional_insight_to_add:** Final review should search for contradictions between evidence states, not just missing fields.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** The seed checklist offers no completion examples.
- **supporting_reason:** Good completion links each applicable claim; bad completion says all checks passed; borderline completion has semantic green and operational no-claim.
- **counterargument_or_limit:** Borderline can be safe or unsafe depending on release claim.
- **assumptions_and_boundaries:** Permit it only when release does not depend on the unmeasured claim and an owner accepts the boundary.
- **revision_decision:** Add split-state examples.
- **additional_insight_to_add:** A no-claim state is not a failure unless someone attempts to rely on the missing claim.

### Question 08: How can the important claims be verified?
- **current_section_observation:** No traceability rule links checklist items to KQEP claims or gate records.
- **supporting_reason:** Stable IDs, evidence links, result states, and unresolved blockers make checklist verification deterministic at the structural layer.
- **counterargument_or_limit:** Structural traceability cannot judge whether an outcome taxonomy is meaningful.
- **assumptions_and_boundaries:** Pair automated link checks with semantic reviewer sign-off.
- **revision_decision:** Add traceability and reconciliation gates.
- **additional_insight_to_add:** Completeness verification should fail on contradictory statuses even when every field is populated.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** Local source supports its reliability and review checks, while the expanded completion model is synthesized and untested in a target workflow.
- **supporting_reason:** Its prerequisites follow the causal model and artifact schema.
- **counterargument_or_limit:** The optimal profile burden and release integration remain organizational judgments.
- **assumptions_and_boundaries:** Calibrate through bounded use and metrics rather than declaring universal policy.
- **revision_decision:** Label process adoption uncertainty and keep hard semantic blockers distinct.
- **additional_insight_to_add:** A proposed workflow can enforce evidence integrity before its efficiency has been proven.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The seed treats completion as terminal.
- **supporting_reason:** Source, dependency, caller, framework, and runtime changes can invalidate previously complete claims selectively.
- **counterargument_or_limit:** Reopening all work after every change is unsustainable.
- **assumptions_and_boundaries:** Attach invalidation triggers per claim and rerun only affected gates plus integration checks.
- **revision_decision:** Add validity window and selective re-open rules.
- **additional_insight_to_add:** Completion is a versioned evidence state, not a permanent property of code.

## Section 017: Adjacent Reference Routing
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed gives generic runtime, security, testing, kotlin, quality, and antipattern routes without exact entry conditions or handoff contracts.
- **supporting_reason:** Routing should decide when quality review remains primary and when another reference owns framework, runtime, security, testing, or broad reliability depth.
- **counterargument_or_limit:** Naming many adjacent files can create navigation overhead and stale links.
- **assumptions_and_boundaries:** Name available candidates while requiring selection-time existence, scope, and freshness checks.
- **revision_decision:** Build a capability-based route table with exact candidate paths, entry evidence, and return contract.
- **additional_insight_to_add:** Routing is a transfer of decision authority, not a dismissal of the original quality claim.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The seed says to consider adjacent references when the task pivots, but it does not define a pivot.
- **supporting_reason:** Keep this reference primary for information/ownership and gate questions; route when the unresolved claim requires deeper platform, framework, operations, security, fixture, or architecture authority.
- **counterargument_or_limit:** One task can legitimately require several references.
- **assumptions_and_boundaries:** Assign one primary owner per claim and integrate results through a shared handoff packet.
- **revision_decision:** Add claim ownership and multi-route reconciliation.
- **additional_insight_to_add:** Multiple references are safe when they own different claims rather than competing for one global conclusion.

### Question 03: When does the default work well?
- **current_section_observation:** No favorable route signals or prerequisites are listed.
- **supporting_reason:** Routing works when the missing question is explicit, the destination covers it, and evidence gathered here can be transferred without repeating discovery.
- **counterargument_or_limit:** Adjacent references may themselves be stale, incomplete, or too broad.
- **assumptions_and_boundaries:** Check destination availability, evidence boundary, and current owner before relying on it.
- **revision_decision:** Add route readiness and destination validation.
- **additional_insight_to_add:** A precise handoff lowers context cost and makes specialist disagreement visible.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** Generic adjacency can become an escape hatch whenever a decision is difficult.
- **supporting_reason:** Premature routing fragments ownership, loses evidence, and delays bounded local fixes.
- **counterargument_or_limit:** Staying too long can cause a quality reviewer to invent security, operations, or framework policy.
- **assumptions_and_boundaries:** Route only the missing authority while continuing safe local evidence work.
- **revision_decision:** Add over-routing and under-routing failure signals.
- **additional_insight_to_add:** The route boundary should be the smallest unanswered consequential claim.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The seed does not compare route, consult, compose, block, or return-to-primary modes.
- **supporting_reason:** A consult supplies one contract, composition shares claims, route transfers primary ownership, and block waits for authority.
- **counterargument_or_limit:** Mode distinctions can be excessive for small teams.
- **assumptions_and_boundaries:** Use simple labels only when they alter ownership and completion.
- **revision_decision:** Add route modes and return semantics.
- **additional_insight_to_add:** A consultation can resolve one version question without handing over the entire change.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Risks include circular routing, stale candidate paths, duplicate work, contradictory defaults, lost blockers, and specialist output promoted beyond its claim.
- **supporting_reason:** These failures occur when handoffs lack stable claim IDs, evidence states, and return conditions.
- **counterargument_or_limit:** Informal collaboration can resolve many cases quickly.
- **assumptions_and_boundaries:** Preserve a minimal shared record even when communication is informal.
- **revision_decision:** Add route-loop and conflict controls.
- **additional_insight_to_add:** A route should be idempotent: repeating it with unchanged evidence should not create a new interpretation.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** Seed adjacent rows provide no examples.
- **supporting_reason:** Good routing sends dispatcher saturation to runtime operations with measured inputs; bad routing sends every `!!` to security; borderline routing consults framework idioms for a data-class entity.
- **counterargument_or_limit:** Security can matter for nullability when absence changes authorization.
- **assumptions_and_boundaries:** Route by consequence and claim, not token category.
- **revision_decision:** Add contrastive route cases and return requirements.
- **additional_insight_to_add:** The same construct can route differently when its consequence changes.

### Question 08: How can the important claims be verified?
- **current_section_observation:** No check confirms destination existence, claim acceptance, returned evidence, or closure.
- **supporting_reason:** Path/capability verification, handoff ID, accepted owner, returned source/test/decision, and reconciliation status make routing auditable.
- **counterargument_or_limit:** Some owner decisions occur outside the repository.
- **assumptions_and_boundaries:** Record decision summary and scope without copying sensitive content.
- **revision_decision:** Add route receipt and closure fields.
- **additional_insight_to_add:** A route is complete only when the primary claim incorporates or explicitly rejects the returned result.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** Eleven Kotlin-related reference filenames are present, but their current content and completion status were not read for this section except the prior owned security reference.
- **supporting_reason:** Filenames establish candidate availability, not topical sufficiency or authority.
- **counterargument_or_limit:** Naming them improves practical navigation.
- **assumptions_and_boundaries:** Treat all as candidates and validate at selection time.
- **revision_decision:** Label candidate paths and avoid content claims about unopened files.
- **additional_insight_to_add:** Existence evidence and semantic-fit evidence must remain separate in routing tables.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The seed routing is one-way and does not explain how specialist results return to quality completion.
- **supporting_reason:** The original change still needs integration, caller, gate, and evidence reconciliation after a specialist decides one subclaim.
- **counterargument_or_limit:** A full ownership transfer may make return unnecessary.
- **assumptions_and_boundaries:** Explicitly mark transfer versus consultation and who owns final integration.
- **revision_decision:** Add return contracts, conflict handling, and final claim ownership.
- **additional_insight_to_add:** Routing architecture is part of quality because fragmented authority can recreate the same information loss at the process level.

## Section 018: Workload Model
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed defines workload as one packet, at most twenty requirement IDs, one matrix, and one command set without evidence that these counts predict Kotlin quality complexity.
- **supporting_reason:** Work should be sized by uncertainty, callers, lifecycle, concurrency, persistence, compatibility, evidence, and ownership rather than document counts.
- **counterargument_or_limit:** Numeric limits are easy to apply and can prevent unbounded work.
- **assumptions_and_boundaries:** Use measured pressure signals and owner-defined budgets; retain counts only as descriptive observations.
- **revision_decision:** Replace fixed capacities with a multidimensional workload envelope and split triggers.
- **additional_insight_to_add:** One coroutine ownership defect can be harder than dozens of independent null checks.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The seed tells users to split when the arbitrary boundary is exceeded but not how.
- **supporting_reason:** Start with one consequential path, map dimensions, choose compact/standard/migration mode, narrow by boundary or claim, and split only on independent ownership or verification seams.
- **counterargument_or_limit:** Narrowing too aggressively can miss cross-boundary causes.
- **assumptions_and_boundaries:** Preserve end-to-end caller and ownership trace for the selected claim even when implementation is sharded.
- **revision_decision:** Add safe narrowing, sharding, and integration rules.
- **additional_insight_to_add:** A good split reduces context while retaining causal closure.

### Question 03: When does the default work well?
- **current_section_observation:** No favorable workload shape is described.
- **supporting_reason:** Bounded work has one primary contract loss, inspectable callers, known lifecycle, reproducible fixture, and one integration owner.
- **counterargument_or_limit:** Shared models or framework configuration can create hidden blast radius.
- **assumptions_and_boundaries:** Perform a lightweight blast-radius and generated/framework boundary inventory before declaring work bounded.
- **revision_decision:** Add bounded-work criteria.
- **additional_insight_to_add:** Apparent file count is a weak proxy for semantic coupling.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The seed capacity model cannot recognize unbounded source discovery, disputed state semantics, multiple owners, production-only behavior, or irreversible migration.
- **supporting_reason:** Those conditions make a single local packet insufficient regardless of requirement count.
- **counterargument_or_limit:** The packet can still preserve current evidence and route the missing dimension.
- **assumptions_and_boundaries:** Stop code promotion, not evidence capture, when a hard boundary is reached.
- **revision_decision:** Add hard stops and route conditions.
- **additional_insight_to_add:** Workload sufficiency is a property of the next decision, not total project size.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The seed offers only continue or split.
- **supporting_reason:** Alternatives include narrow by path, characterize first, contain at adapter, shard by owner, stage migration, sample repeated patterns, automate deterministic scans, or route specialist claims.
- **counterargument_or_limit:** Each strategy can lose context or create coordination overhead.
- **assumptions_and_boundaries:** Keep shared invariants and final integration ownership explicit.
- **revision_decision:** Add strategy matrix with information-loss risk.
- **additional_insight_to_add:** Automation scales candidate discovery better than semantic classification.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Missing workload hazards include broad grep expansion, duplicate findings, context thrash, premature parallelism, shared-file collision, uneven fixtures, and verification bottlenecks.
- **supporting_reason:** These consume effort while reducing evidence coherence.
- **counterargument_or_limit:** Parallel independent adapters can accelerate a well-defined migration.
- **assumptions_and_boundaries:** Parallelize only disjoint write surfaces under one contract and merge gate.
- **revision_decision:** Add coordination and backpressure signals.
- **additional_insight_to_add:** Parallelism increases throughput only after semantic and ownership boundaries are stable.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** The seed gives no workload examples.
- **supporting_reason:** Good work narrows one adapter and callers; bad work replaces every `!!`; borderline work inventories many similar adapters but samples before migration.
- **counterargument_or_limit:** Sampling can miss rare high-consequence variants.
- **assumptions_and_boundaries:** Stratify by framework, lifecycle, caller action, and side effect, and inspect outliers.
- **revision_decision:** Add workload fixtures and sampling safeguards.
- **additional_insight_to_add:** Representative sampling requires semantic strata, not random files alone.

### Question 08: How can the important claims be verified?
- **current_section_observation:** No workload measurement, budget, or split-success criteria exist.
- **supporting_reason:** Inventory counts, dependency/caller edges, owner map, fixture availability, gate duration, conflict rate, and integration failures can inform capacity.
- **counterargument_or_limit:** Counts remain imperfect and environment-specific.
- **assumptions_and_boundaries:** Use them as routing signals, not universal limits.
- **revision_decision:** Define workload observations and post-split equivalence gates.
- **additional_insight_to_add:** A split is successful only if integrated behavior and evidence remain equivalent to the unsplit contract.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The seed's fixed counts are known historical text but have no calibration evidence; no target workload was measured.
- **supporting_reason:** Causal workload dimensions are defensible while thresholds remain local judgments.
- **counterargument_or_limit:** Teams may already have empirical budgets not represented here.
- **assumptions_and_boundaries:** Adopt target budgets when their measurement and owner are recorded.
- **revision_decision:** Preserve fixed counts only as rejected uncalibrated guidance and state no capacity result.
- **additional_insight_to_add:** A model can improve decisions without claiming a universal threshold.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** Workload is treated as static rather than changing as evidence closes or reveals new edges.
- **supporting_reason:** A failing test can narrow a hypothesis, while a caller trace can expand blast radius; plans need state-dependent recalculation.
- **counterargument_or_limit:** Constant replanning can interrupt implementation.
- **assumptions_and_boundaries:** Reassess only at material discoveries, ownership changes, or gate failures.
- **revision_decision:** Add workload state transitions and checkpoint triggers.
- **additional_insight_to_add:** Evidence can reduce workload by eliminating branches, so measurement should track unresolved dimensions rather than only accumulated tasks.

## Section 019: Reliability Target
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed mixes deterministic evidence invariants, a sampled 18-of-20 routing threshold, unsupported-claim prohibition, and recovery clarity as if they formed one reliability score.
- **supporting_reason:** Reliability targets should decide which failures must be prevented, detected, contained, recovered, and learned from for a named claim population.
- **counterargument_or_limit:** Splitting dimensions makes the summary less compact.
- **assumptions_and_boundaries:** Keep one profile summary while preserving distinct evidence methods and owners.
- **revision_decision:** Replace aggregate reliability language with hard invariants, sampled indicators, sentinel events, and accepted-risk states.
- **additional_insight_to_add:** Deterministic artifact integrity and probabilistic runtime behavior cannot share one denominator honestly.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The seed prescribes thresholds without stating target, timeframe, or owner.
- **supporting_reason:** Define claim population, consequence, invariant/indicator, evidence, owner, response, and review trigger before assigning a threshold.
- **counterargument_or_limit:** Some structural invariants can be universal within this artifact format.
- **assumptions_and_boundaries:** Use exact thresholds for mechanically decidable declared populations, not unknown production populations.
- **revision_decision:** Add reliability profile schema and bounded examples.
- **additional_insight_to_add:** "Zero unsupported claims" is meaningful only after defining which claims and what counts as support.

### Question 03: When does the default work well?
- **current_section_observation:** No favorable reliability context is stated.
- **supporting_reason:** Profiles work when claims and populations are stable, evidence is reproducible, failures have owners, and responses are actionable.
- **counterargument_or_limit:** Novel systems and early migrations may lack baselines or stable categories.
- **assumptions_and_boundaries:** Start with hard semantic invariants and sentinel failures; defer trend thresholds until data exists.
- **revision_decision:** Add maturity-dependent target selection.
- **additional_insight_to_add:** Early reliability can be governed by unacceptable events without pretending to know their frequency.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** Fixed percentages can be gamed, hide severity, and imply precision from tiny samples.
- **supporting_reason:** Nineteen correct routes and one catastrophic wrong route may be worse than a lower aggregate with harmless errors.
- **counterargument_or_limit:** Sample thresholds remain useful as regression gates for bounded fixtures.
- **assumptions_and_boundaries:** Keep fixture identity, error classes, and sentinel cases visible.
- **revision_decision:** Reframe 18-of-20 as an inherited illustrative sample gate, never a production accuracy claim.
- **additional_insight_to_add:** Reliability evaluation should weight consequence through sentinel events, not arbitrary numerical weighting alone.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The seed offers four targets but no prevention, detection, containment, recovery, or learning alternatives.
- **supporting_reason:** Some defects are best made impossible by types, others detected by tests/analyzers, and runtime failures contained and recovered operationally.
- **counterargument_or_limit:** Layering controls can duplicate effort and add latency.
- **assumptions_and_boundaries:** Select independent controls proportional to consequence and remove redundant low-value gates through feedback.
- **revision_decision:** Add control-layer matrix and tradeoff.
- **additional_insight_to_add:** Reliability is stronger when failures are caught at the cheapest layer capable of preventing their consequence.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Risks include denominator ambiguity, passing sample overreach, no-data-as-zero, unsupported universal targets, recovery text without drills, and ownerless alerts.
- **supporting_reason:** These create nominal targets with no operational behavior.
- **counterargument_or_limit:** Not every code-quality target needs production alerts or drills.
- **assumptions_and_boundaries:** Match evidence and response to the layer; semantic invariants may need tests, while saturation targets need operations.
- **revision_decision:** Add validity and response checks.
- **additional_insight_to_add:** A target without a failure response is descriptive at best, not a reliability control.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** Seed targets have no example profiles.
- **supporting_reason:** A good profile says all changed suspend paths preserve cancellation under named tests; a bad profile says 99 percent coroutine reliability; a borderline profile has 18-of-20 route fixtures.
- **counterargument_or_limit:** Deterministic test populations can still omit real variants.
- **assumptions_and_boundaries:** State coverage rationale and sentinel cases.
- **revision_decision:** Add contrastive targets and prohibited interpretations.
- **additional_insight_to_add:** Exact pass over a finite suite is a suite result, not a universal probability.

### Question 08: How can the important claims be verified?
- **current_section_observation:** Evidence methods are brief and do not define fixture, population, result state, or remeasurement.
- **supporting_reason:** Test IDs, analyzer populations, packet audits, runtime experiments, sampled reviews, and recovery exercises provide layer-specific evidence.
- **counterargument_or_limit:** Some recovery paths cannot be exercised safely in production.
- **assumptions_and_boundaries:** Use representative nonproduction drills and label residual uncertainty.
- **revision_decision:** Add verification and response signatures per target.
- **additional_insight_to_add:** Recovery clarity is better tested by executing or simulating the route than by reviewing prose alone.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** Seed values are known text, but their calibration and achieved status are unknown; no target reliability measurement ran.
- **supporting_reason:** Deterministic packet and code invariants can be proposed clearly without outcome claims.
- **counterargument_or_limit:** Whether they are proportionate or sufficient remains target judgment.
- **assumptions_and_boundaries:** Require owner acceptance and feedback before organization-wide mandates.
- **revision_decision:** Label proposed, observed, accepted, violated, and retired target states.
- **additional_insight_to_add:** Target definition and target achievement are separate evidence records.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** Reliability targets are static in the seed.
- **supporting_reason:** Findings, escaped defects, new caller classes, version changes, and gate noise should recalibrate controls and populations.
- **counterargument_or_limit:** Frequent threshold changes destroy comparability.
- **assumptions_and_boundaries:** Version target definitions and change them only after documented review.
- **revision_decision:** Add target lifecycle and series-boundary rules.
- **additional_insight_to_add:** Retiring a noisy target can improve reliability when stronger semantic controls already make it redundant.

## Section 020: Failure Mode Table
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed lists four generic evidence and metric failures, omitting concrete Kotlin failure chains and their stage of detection.
- **supporting_reason:** A failure table should help diagnose whether the defect originates in evidence, boundary conversion, state, identity, coroutine ownership, blocking, shared state, verification, migration, or operation.
- **counterargument_or_limit:** A very large table can duplicate the anti-pattern registry.
- **assumptions_and_boundaries:** Focus this section on failure progression, containment, and recovery; keep construct detection in the registry.
- **revision_decision:** Expand into stage-indexed causal failure modes with response fields.
- **additional_insight_to_add:** Diagnosis improves when downstream symptom and upstream contract loss are both named.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** Seed mitigation actions jump directly to refresh, block, audit, or replace claim without a classification process.
- **supporting_reason:** Detect, classify layer, stop harmful side effects, preserve evidence, repair earliest contract loss, verify recovery, and update prevention.
- **counterargument_or_limit:** Incident containment may precede full root-cause proof.
- **assumptions_and_boundaries:** Keep containment reversible and preserve a follow-up owner.
- **revision_decision:** Add state transition and changed-premise recovery guidance.
- **additional_insight_to_add:** Repairing the first visible symptom without preserving evidence can make recurrence harder to diagnose.

### Question 03: When does the default work well?
- **current_section_observation:** No failure preconditions or observability needs are listed.
- **supporting_reason:** Causal handling works when path identity, fixture or event, owner, and side effects can be observed.
- **counterargument_or_limit:** Rare production races or opaque dependencies may not reproduce.
- **assumptions_and_boundaries:** Use logs/traces/metrics within privacy limits, preserve build/config identity, and state unresolved causality.
- **revision_decision:** Add reproducible and non-reproducible branches.
- **additional_insight_to_add:** Non-reproduction should narrow certainty, not erase the incident evidence.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** A table can imply one trigger maps to one cause.
- **supporting_reason:** Null crashes, timeouts, and flaky tests often have multiple plausible mechanisms and compound interactions.
- **counterargument_or_limit:** Listing every hypothesis delays action.
- **assumptions_and_boundaries:** Prioritize hypotheses by evidence and consequence, test one variable, and contain high-risk effects.
- **revision_decision:** Add ambiguity and compound-failure fields.
- **additional_insight_to_add:** Failure classification should remain revisable until discriminating evidence exists.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** Seed mitigations do not compare fail-fast, typed failure, fallback, retry, circuit breaking, isolation, rollback, or route.
- **supporting_reason:** Responses trade availability, correctness, latency, data consistency, user recovery, and operational burden.
- **counterargument_or_limit:** This quality reference cannot design every distributed recovery policy.
- **assumptions_and_boundaries:** State the local failure contract and route distributed/security/operations policy when needed.
- **revision_decision:** Add response options with route boundaries.
- **additional_insight_to_add:** A fallback can be a correctness defect when it erases authorization, freshness, or state meaning.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Missing meta-failures include misclassified cancellation, retry amplification, fixture invalidity, analyzer blind spots, rollback incompatibility, and ownerless blocked states.
- **supporting_reason:** These can turn the response mechanism itself into a new failure.
- **counterargument_or_limit:** Not all targets use retries, analyzers, or migrations.
- **assumptions_and_boundaries:** Activate rows by mechanism and explicitly mark absence.
- **revision_decision:** Add response-induced and observability failures.
- **additional_insight_to_add:** Recovery code deserves the same state and ownership scrutiny as primary code.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** Seed rows have no end-to-end incidents or classifications.
- **supporting_reason:** Good handling rethrows cancellation and prevents side effects; bad handling retries false; borderline handling contains a blocking path but lacks capacity evidence.
- **counterargument_or_limit:** Example outcomes remain illustrative.
- **assumptions_and_boundaries:** Use them to show transitions and evidence, not production probabilities.
- **revision_decision:** Add contrastive failure trajectories.
- **additional_insight_to_add:** Borderline recovery can be locally correct while remaining operationally unpromoted.

### Question 08: How can the important claims be verified?
- **current_section_observation:** Seed methods rely on text audits rather than failure injection or recovery observation.
- **supporting_reason:** Negative fixtures, cancellation, concurrency, dependency faults, duplicate/restart, rollback, analyzer population, and route drills verify distinct failures.
- **counterargument_or_limit:** Destructive recovery tests may be unsafe in production.
- **assumptions_and_boundaries:** Use representative nonproduction environments and owner-approved drills.
- **revision_decision:** Attach detection and recovery proof to each row.
- **additional_insight_to_add:** A mitigation is incomplete until the system is observed returning to a defined state.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** Local source supports core causal hazards; expanded operational chains and responses are synthesized without target incidents.
- **supporting_reason:** The table can provide bounded diagnostic hypotheses and test designs.
- **counterargument_or_limit:** Frequency, severity, and best recovery remain target-specific.
- **assumptions_and_boundaries:** Avoid probability and universal timeout/retry claims; route owner choices.
- **revision_decision:** Label mechanisms as source-derived or inferred and outcomes unmeasured.
- **additional_insight_to_add:** A plausible failure mode is a test hypothesis, not evidence that it occurred.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The seed table ends after mitigation and does not feed lessons into source maps, gates, or models.
- **supporting_reason:** Confirmed root causes should update boundaries, shared tests, exception policy, observability, and reliability profiles.
- **counterargument_or_limit:** One incident can overfit a global control.
- **assumptions_and_boundaries:** Promote after recurrence, shared mechanism, or high-consequence sentinel review.
- **revision_decision:** Add learning and control-retirement outcomes.
- **additional_insight_to_add:** Failure review should sometimes remove a misleading gate that delayed diagnosis or hid the real mechanism.

## Section 021: Retry Backpressure Guidance
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed recommends one bounded stale-evidence retry and general backpressure but does not distinguish application, verification, external research, and agent-work retries.
- **supporting_reason:** Retry safety depends on failure class, side effects, cancellation/deadline, idempotency, owner budget, and whether a premise changed.
- **counterargument_or_limit:** This quality reference cannot define every service or distributed retry policy.
- **assumptions_and_boundaries:** Define local classification and route production retry budgets/idempotency to security/resilience or operations owners.
- **revision_decision:** Split retry domains and add explicit state transitions.
- **additional_insight_to_add:** Repetition is only retry when the system can explain why the next attempt has a better chance or safer effect.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The seed's one-retry rule is specific to stale external evidence but can be misread as universal.
- **supporting_reason:** Do not retry by default; classify, preserve cancellation, confirm side-effect safety, change a premise, consume the correct owner budget, and stop on unchanged failure.
- **counterargument_or_limit:** Transient idempotent reads may have well-established automatic policies.
- **assumptions_and_boundaries:** Reuse those policies when configured, bounded, observable, and within caller deadline.
- **revision_decision:** Replace universal count with domain-owned budgets and a changed-premise requirement.
- **additional_insight_to_add:** Nested retries consume one end-to-end attempt/deadline budget even when each layer looks locally bounded.

### Question 03: When does the default work well?
- **current_section_observation:** Favorable transient conditions and prerequisites are not listed.
- **supporting_reason:** Retry can help for classified transient, idempotent, deadline-compatible failures with backoff/jitter and observable attempt state.
- **counterargument_or_limit:** A repeated tool or test may reveal flakiness rather than recoverability.
- **assumptions_and_boundaries:** Record attempt outcomes and quarantine/diagnose flaky evidence instead of selecting a passing run.
- **revision_decision:** Add retryable-class criteria and evidence-flake handling.
- **additional_insight_to_add:** A flaky pass is evidence of nondeterminism, not confirmation that the defect disappeared.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** Seed guidance lacks explicit non-retryable classes such as cancellation, validation, policy denial, deterministic assertion, and unsafe mutation.
- **supporting_reason:** Retrying them wastes resources, violates caller intent, amplifies side effects, and masks defects.
- **counterargument_or_limit:** A policy/configuration change may make a previously deterministic failure worth rerunning.
- **assumptions_and_boundaries:** That is a new attempt after a changed premise, not blind repetition.
- **revision_decision:** Add non-retryable classes and reset conditions.
- **additional_insight_to_add:** Cancellation is a control signal, not a transient failure to be retried underneath the caller.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The seed offers retry or escalation but not fail-fast, fallback, queue, circuit, isolation, manual review, or defer.
- **supporting_reason:** Alternatives trade availability, correctness, latency, load, user control, and operational complexity.
- **counterargument_or_limit:** Detailed resilience design belongs in adjacent references.
- **assumptions_and_boundaries:** This section selects stop/route conditions and preserves local Kotlin semantics; specialist references own production policy.
- **revision_decision:** Add response alternatives and route boundaries.
- **additional_insight_to_add:** Backpressure can be a correct product response when accepting more work would destroy evidence or service health.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Missing hazards include swallowed cancellation, nested retry amplification, attempt state in global mutable storage, lost deadlines, duplicate writes, selective passing tests, and context-loop agent retries.
- **supporting_reason:** These failures convert recovery into load, corruption, or false confidence.
- **counterargument_or_limit:** Frameworks may implement safe policies internally.
- **assumptions_and_boundaries:** Inspect and account for lower-layer retries before adding another layer.
- **revision_decision:** Add retry topology and state-ownership checks.
- **additional_insight_to_add:** Hidden retries are another form of hidden ownership because no caller knows who controls time or side effects.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** The seed has no contrastive retry examples.
- **supporting_reason:** Good tool retry follows an environment fix; bad application retry catches cancellation and repeats a write; borderline test retry passes once after a race.
- **counterargument_or_limit:** A rerun can be useful diagnostic evidence if all attempts are retained.
- **assumptions_and_boundaries:** Never use rerun-to-green as completion; classify and fix nondeterminism.
- **revision_decision:** Add domain-specific good/unsafe/conditional trajectories.
- **additional_insight_to_add:** Attempt history is part of the evidence, not disposable noise.

### Question 08: How can the important claims be verified?
- **current_section_observation:** No attempt record, budget check, duplicate fixture, cancellation test, or queue signal is required.
- **supporting_reason:** Attempt IDs, failure classes, premise diffs, deadlines, side-effect keys, delays, results, and stop reasons make retry behavior auditable.
- **counterargument_or_limit:** Detailed tracing can expose sensitive inputs or add overhead.
- **assumptions_and_boundaries:** Record metadata and redacted classifications rather than payloads.
- **revision_decision:** Add minimal attempt schema and backpressure evidence.
- **additional_insight_to_add:** A retry policy should be testable with deterministic failure sequences and duplicate-side-effect assertions.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The seed supplies workflow guidance, while target retry semantics, budgets, idempotency, and load limits are unknown.
- **supporting_reason:** Strong defaults against cancellation/deterministic/unsafe retries can be stated, but production policy cannot.
- **counterargument_or_limit:** Some target frameworks may already guarantee idempotency or attempt bounds.
- **assumptions_and_boundaries:** Verify configured behavior and owner contract before relying on it.
- **revision_decision:** State no universal attempt, delay, timeout, or concurrency value.
- **additional_insight_to_add:** A policy can be locally correct yet globally unsafe when combined with upstream or downstream retries.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The seed treats backpressure as stopping new work but not preserving resumable state.
- **supporting_reason:** Durable checkpoints, pending/blocked queues, and attempt history prevent context loss and duplicate action when work resumes.
- **counterargument_or_limit:** Persistence overhead is excessive for tiny local commands.
- **assumptions_and_boundaries:** Scale persistence to duration, side effects, coordination, and restart consequence.
- **revision_decision:** Add durable agent/workflow backpressure and resume contracts.
- **additional_insight_to_add:** Backpressure protects decision quality as well as runtime capacity by preventing new work from burying unresolved evidence.

## Section 022: Observability Checklist
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed asks to record sources, verification, latency, reviewer decisions, metrics, and concise evidence but lacks an event model tied to Kotlin quality claims.
- **supporting_reason:** Observability should let reviewers reconstruct which boundary/ownership claim changed, what gate ran, and what remains unresolved.
- **counterargument_or_limit:** Excessive instrumentation can expose data, increase cardinality, and burden small changes.
- **assumptions_and_boundaries:** Capture minimal metadata proportional to consequence; avoid payloads and unbounded identifiers.
- **revision_decision:** Add artifact and runtime event schemas with privacy/cardinality controls.
- **additional_insight_to_add:** Observability quality is reconstruction ability, not log volume.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The checklist mixes workflow and runtime measurements without required fields or state semantics.
- **supporting_reason:** Use stable claim/finding/gate IDs, target/build/config identity, event state, population, result, owner, uncertainty, and next transition.
- **counterargument_or_limit:** Runtime systems may not expose all identities cheaply.
- **assumptions_and_boundaries:** Capture correlation at the safest available granularity and keep unavailable fields explicit.
- **revision_decision:** Define common envelope and specialized event types.
- **additional_insight_to_add:** One common envelope allows evidence across source, tests, runtime, and handoff to be correlated without merging their meanings.

### Question 03: When does the default work well?
- **current_section_observation:** No fit conditions for workflow versus runtime telemetry are named.
- **supporting_reason:** It works when event categories are bounded, identities stable, and owner response is linked.
- **counterargument_or_limit:** High-volume per-request events can overwhelm systems and create privacy risk.
- **assumptions_and_boundaries:** Prefer aggregates, exemplars, and sampled traces for runtime; keep deterministic packet/gate records separately.
- **revision_decision:** Add volume-sensitive capture strategies.
- **additional_insight_to_add:** Deterministic review evidence and sampled runtime telemetry should not be stored or interpreted identically.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The seed can encourage collecting p50/p95/p99 even when runtime does not apply or sample quality is absent.
- **supporting_reason:** Percentiles without enough representative observations and workload identity create false precision.
- **counterargument_or_limit:** Latency distributions are useful for real blocking/performance claims.
- **assumptions_and_boundaries:** Collect them only under the controlled performance method and report sample/uncertainty.
- **revision_decision:** Make runtime metrics conditional and prohibit universal percentile capture.
- **additional_insight_to_add:** A missing runtime measurement must remain unknown, not a zero or omitted success.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The seed does not compare logs, metrics, traces, test reports, analyzer reports, packet records, and owner decisions.
- **supporting_reason:** Each supports different reconstruction, aggregation, cost, and privacy needs.
- **counterargument_or_limit:** Duplicating the same event across systems can fragment truth.
- **assumptions_and_boundaries:** Assign one canonical record and reference it from derived telemetry.
- **revision_decision:** Add evidence-medium selection and provenance.
- **additional_insight_to_add:** Derived dashboards should link back to raw claim/gate definitions and version boundaries.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Missing hazards include secret/PII logging, exception-message taxonomy, high-cardinality IDs, dropped-event-as-zero, duplicate retries, clock skew, stale build identity, and ownerless alerts.
- **supporting_reason:** These defects can make observability unsafe or misleading.
- **counterargument_or_limit:** Strong redaction can remove diagnostic value.
- **assumptions_and_boundaries:** Prefer typed categories and correlation tokens over payload content; retain secure drill paths for deeper evidence.
- **revision_decision:** Add privacy, cardinality, completeness, and response checks.
- **additional_insight_to_add:** Error message strings are unstable labels and may leak details; typed failure categories are safer observability dimensions.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** No observability examples appear in the seed.
- **supporting_reason:** Good events record cancellation classification and no-side-effect result; bad logs include raw request and stack while omitting build; borderline telemetry shows zero failures during an outage in collection.
- **counterargument_or_limit:** Some debugging requires temporary detailed capture.
- **assumptions_and_boundaries:** Use time-bounded, approved, redacted diagnostic mode with explicit removal and access controls.
- **revision_decision:** Add contrastive event examples and diagnostic-mode rules.
- **additional_insight_to_add:** Collection health is a prerequisite signal for every zero-event interpretation.

### Question 08: How can the important claims be verified?
- **current_section_observation:** The seed does not test event emission, schema, redaction, correlation, cardinality, or alert response.
- **supporting_reason:** Schema tests, redaction tests, deterministic fixture events, collection-health checks, cardinality budgets, and recovery drills validate observability.
- **counterargument_or_limit:** Local tests cannot prove production delivery or dashboard correctness.
- **assumptions_and_boundaries:** Add integration/synthetic checks and operations ownership for runtime pipelines.
- **revision_decision:** Add observability verification gates.
- **additional_insight_to_add:** Telemetry about a failure is reliable only when the telemetry path's own failure is observable.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** This reference produced journal and artifact evidence, but no target runtime telemetry or operator workflow was inspected.
- **supporting_reason:** Workflow schema can be defined confidently; runtime fields and thresholds remain target-specific.
- **counterargument_or_limit:** Local source only briefly mentions review evidence, not the expanded event model.
- **assumptions_and_boundaries:** Label the event model as synthesis and require target privacy/operations review.
- **revision_decision:** Separate artifact observability from proposed runtime observability.
- **additional_insight_to_add:** The same claim ID can connect both without implying runtime data exists.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The seed treats observability as proof storage, not an input to gate calibration and ownership.
- **supporting_reason:** Finding recurrence, gate noise, retry amplification, cancellation signals, and collection gaps can change controls and routes.
- **counterargument_or_limit:** Automated reactions can amplify bad classifications.
- **assumptions_and_boundaries:** Use human-reviewed, reversible policy updates with counter-metrics.
- **revision_decision:** Link observability to the bounded feedback loop.
- **additional_insight_to_add:** Observability should reveal when a quality gate itself becomes a source of delay, noise, or false confidence.

## Section 023: Performance Verification Method
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed combines requirement mapping, one-session lead time, framework/coroutine guessing, mixed measurements, and reviewer action into one performance method.
- **supporting_reason:** Performance verification should decide whether a Kotlin quality change preserves correctness and meets a target-owned cost or runtime contract under controlled conditions.
- **counterargument_or_limit:** Most quality repairs make no performance claim and need no benchmark.
- **assumptions_and_boundaries:** Run performance experiments only when decision or release depends on performance; otherwise state no claim.
- **revision_decision:** Split runtime, build/gate, and workflow performance methods with an applicability gate.
- **additional_insight_to_add:** Avoiding an irrelevant benchmark is part of evidence quality.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The seed says fail closed on unmapped claims but gives no experiment sequence.
- **supporting_reason:** Define claim and threshold owner, freeze equivalent behavior, control environment/workload, warm up, collect repeated samples and counter-metrics, analyze uncertainty, then accept or reject.
- **counterargument_or_limit:** Strict control can be expensive for exploratory profiling.
- **assumptions_and_boundaries:** Use profiling for hypothesis generation and a controlled experiment for promoted conclusions.
- **revision_decision:** Add staged method from semantic gate to owner decision.
- **additional_insight_to_add:** A faster implementation with different failure or cancellation semantics is not a valid comparison.

### Question 03: When does the default work well?
- **current_section_observation:** No fit conditions or target mechanism are defined.
- **supporting_reason:** It works for dispatcher/blocking changes, allocation-sensitive state modeling, analyzer/build gate overhead, and review workflow trials with comparable populations.
- **counterargument_or_limit:** Production behavior may depend on infrastructure and workload unavailable locally.
- **assumptions_and_boundaries:** Use representative environments and keep local results local when equivalence is weak.
- **revision_decision:** Add mechanism-specific profiles and promotion levels.
- **additional_insight_to_add:** Performance evidence should travel with its environment and workload identity.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The seed encourages p50/p95/p99 capture without sample adequacy and one-session workflow claims without cohort definition.
- **supporting_reason:** Tail metrics and speed comparisons can be meaningless under small, changing, or biased samples.
- **counterargument_or_limit:** Raw timings can still reveal gross regressions.
- **assumptions_and_boundaries:** Report raw distributions/ranges and limitations; avoid unsupported percentile or causal language.
- **revision_decision:** Add sample adequacy and no-comparison states.
- **additional_insight_to_add:** Precision of a printed timer is not precision of the experiment.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The seed does not compare profiling, microbenchmark, integration load, production observation, gate timing, or reviewer study.
- **supporting_reason:** These methods trade control, realism, attribution, cost, and risk.
- **counterargument_or_limit:** A full method taxonomy can be excessive.
- **assumptions_and_boundaries:** Choose the least expensive method capable of falsifying the actual performance claim.
- **revision_decision:** Add method selection table.
- **additional_insight_to_add:** Mechanism discovery and release acceptance often need different experiments.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Missing hazards include changed outputs, JIT/warmup, caching, GC, shared machine noise, tiny samples, omitted failures, dispatcher saturation, and tool/config changes.
- **supporting_reason:** These confound results and can reward incorrect or incomplete code.
- **counterargument_or_limit:** Eliminating every source of noise is impossible.
- **assumptions_and_boundaries:** Control major variables, randomize/order where appropriate, repeat, and report uncertainty.
- **revision_decision:** Add validity checklist and abort conditions.
- **additional_insight_to_add:** Error-path and cancellation workload must be included when the change claims reliability under load.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** No performance examples exist beyond seed slogans.
- **supporting_reason:** Good comparison verifies equivalent outcomes and measures blocking queues; bad comparison times happy path only; borderline result is a local speedup with production no-claim.
- **counterargument_or_limit:** Example thresholds would be misleading.
- **assumptions_and_boundaries:** Show method and decision states without invented numeric outcomes.
- **revision_decision:** Add contrastive experiment records.
- **additional_insight_to_add:** A valid borderline result can guide further testing without authorizing release claims.

### Question 08: How can the important claims be verified?
- **current_section_observation:** Seed measurement packet lists many fields but lacks correctness oracle, baseline identity, statistical plan, and acceptance owner.
- **supporting_reason:** These elements make comparison reproducible and prevent post-hoc threshold selection.
- **counterargument_or_limit:** Statistical sophistication should match consequence and sample volume.
- **assumptions_and_boundaries:** Predefine simple comparisons for small experiments and seek specialist review for high-stakes claims.
- **revision_decision:** Add required experiment packet and audit.
- **additional_insight_to_add:** Owner-defined acceptance must precede result inspection when practical to reduce threshold shopping.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** No target, benchmark, workload, gate timing, or reviewer study ran during this reference evolution.
- **supporting_reason:** Method requirements can be stated, but no performance result or threshold can.
- **counterargument_or_limit:** Reference file and packet sizes are observable but unrelated to Kotlin target performance.
- **assumptions_and_boundaries:** Keep artifact metrics separate from engineering outcomes.
- **revision_decision:** Add explicit no-results statement.
- **additional_insight_to_add:** Measuring the reference generation process would not validate a Kotlin runtime claim.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The seed treats performance as a final pass/fail gate.
- **supporting_reason:** Results can reveal architecture changes, workload segmentation, analyzer targeting, or that no optimization is needed.
- **counterargument_or_limit:** Optimization feedback can distract from semantic quality.
- **assumptions_and_boundaries:** Correctness and ownership invariants remain non-negotiable; optimize only measured relevant costs.
- **revision_decision:** Add decision outcomes including retain, narrow, optimize, route, rollback, and no action.
- **additional_insight_to_add:** The best performance outcome can be rejecting an optimization whose complexity exceeds measured benefit.

## Section 024: Scale Boundary Statement
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed says the reference stops being sufficient across multiple systems, ownership boundaries, unbounded discovery, or production traffic without an SLO, but it does not define sufficiency per claim.
- **supporting_reason:** Scale guidance should decide whether local Kotlin quality controls remain enough or need framework, migration, durable, security, runtime, or coordination architecture.
- **counterargument_or_limit:** "Scale" is often used to justify premature complexity.
- **assumptions_and_boundaries:** Route on observed authority/topology/evidence pressure, not project reputation or anticipated growth.
- **revision_decision:** Add multidimensional sufficiency tests and reversible route states.
- **additional_insight_to_add:** Scale boundary is crossed when the next invariant cannot be owned or verified locally, not when a repository reaches an arbitrary size.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The seed recommends splitting by theme and one verification owner but not how to preserve shared contracts.
- **supporting_reason:** Keep local when one owner and test surface can close the claim; narrow or shard on independent boundaries; federate shared contracts; route durable/runtime/policy claims to specialists.
- **counterargument_or_limit:** Central integration can become a bottleneck.
- **assumptions_and_boundaries:** Decentralize implementation while retaining versioned shared contract and one integration decision owner.
- **revision_decision:** Add route ladder and merge/equivalence gates.
- **additional_insight_to_add:** Distributed implementation needs centralized contract coherence, not centralized editing.

### Question 03: When does the default work well?
- **current_section_observation:** No local-sufficiency conditions are stated.
- **supporting_reason:** This reference is sufficient for bounded owned paths whose state, lifecycle, callers, fixtures, and relevant gates are inspectable.
- **counterargument_or_limit:** A small path can still depend on enterprise policy or opaque production infrastructure.
- **assumptions_and_boundaries:** Evaluate authority and topology before file/module count.
- **revision_decision:** Add local sufficiency checklist.
- **additional_insight_to_add:** Organizational coupling can dominate code size.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** Seed boundaries are broad and do not distinguish warning pressure from hard stops.
- **supporting_reason:** Public schema migration, process-surviving work, cross-system side effects, disputed authority, and required unmeasured SLOs are hard boundaries; many callers are pressure only.
- **counterargument_or_limit:** Some teams have existing platforms that make those concerns locally routine.
- **assumptions_and_boundaries:** Reuse platform contracts only when current, owned, and target-verified.
- **revision_decision:** Separate pressure indicators, hard boundaries, and resolved platform capabilities.
- **additional_insight_to_add:** Existing infrastructure can move a scale boundary inward only when its guarantees are evidence, not assumption.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The seed offers split work but not local containment, federation, durable state, service boundary, or specialist ownership.
- **supporting_reason:** Routes trade consistency, autonomy, coordination, latency, operational cost, and migration risk.
- **counterargument_or_limit:** Creating services or platforms merely to distribute code can worsen ownership.
- **assumptions_and_boundaries:** Choose the smallest architecture that owns the missing invariant.
- **revision_decision:** Add route comparison and rollback.
- **additional_insight_to_add:** A new service is not a substitute for a clear state or error contract.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Missing scale hazards include shared-schema drift, duplicated retries, inconsistent null/state models, dispatcher contention, owner gaps, cross-worker file collisions, and global scans with no denominator.
- **supporting_reason:** These failures amplify local ambiguity across boundaries.
- **counterargument_or_limit:** Standardization can also constrain legitimate domain differences.
- **assumptions_and_boundaries:** Standardize contract shapes only where semantics align; version differences explicitly elsewhere.
- **revision_decision:** Add drift, amplification, and false-uniformity controls.
- **additional_insight_to_add:** Semantic consistency is more important than identical Kotlin types across independent domains.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** The seed provides no scale examples.
- **supporting_reason:** Good scaling shards independent Java adapters under one outcome contract; bad scaling runs a global replacement; borderline scaling centralizes a dispatcher without workload evidence.
- **counterargument_or_limit:** Central dispatcher policy can be appropriate with platform ownership.
- **assumptions_and_boundaries:** Require measured resource model, isolation, and operations contract.
- **revision_decision:** Add route examples and promotion gates.
- **additional_insight_to_add:** Borderline scale choices become safe through explicit platform contracts and observability, not larger constants.

### Question 08: How can the important claims be verified?
- **current_section_observation:** The seed mentions graph narrowing and merge verification but no concrete scale evidence.
- **supporting_reason:** Caller/dependency maps, owner maps, contract versions, per-shard gates, integration equivalence, runtime capacity tests, and rollback drills verify different routes.
- **counterargument_or_limit:** Graphs can be incomplete or stale.
- **assumptions_and_boundaries:** Record graph source/time and validate critical edges manually.
- **revision_decision:** Add route-specific verification signatures.
- **additional_insight_to_add:** A topology map is evidence for navigation, not proof of runtime or semantic behavior.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** No target system size, traffic, owner map, dependency graph, or SLO was observed.
- **supporting_reason:** Hard authority and lifecycle boundaries can be identified conceptually, while thresholds and route costs cannot.
- **counterargument_or_limit:** Seed statements already assert some broad insufficiency conditions.
- **assumptions_and_boundaries:** Preserve those as conservative routes and add evidence requirements.
- **revision_decision:** State no measured scale capacity or architecture recommendation.
- **additional_insight_to_add:** Scale guidance can be operational without forecasting a numeric limit.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The seed assumes scaling only expands work.
- **supporting_reason:** Better adapters, shared fixtures, platform contracts, and selective indexes can reduce unresolved complexity while system size grows.
- **counterargument_or_limit:** Central abstractions can become bottlenecks or erase domain differences.
- **assumptions_and_boundaries:** Measure adoption, exceptions, coordination cost, and failure containment before promotion.
- **revision_decision:** Add scale-in and rollback criteria for shared controls.
- **additional_insight_to_add:** Scalable quality is the ability to localize decisions and failures, not the ability to apply one rule everywhere.

## Section 025: Future Refresh Search Queries
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed lists three broad search phrases without saying which stale or unresolved claim each should refresh.
- **supporting_reason:** A refresh query should retrieve evidence for one versioned Kotlin quality decision, not generate a general trend summary.
- **counterargument_or_limit:** Broad phrases can be useful for discovering official terminology and repositories.
- **assumptions_and_boundaries:** Use broad queries only for orientation, then narrow to authoritative artifacts before promotion.
- **revision_decision:** Preserve exact seed strings and add claim triggers, preferred sources, capture, and stop rules.
- **additional_insight_to_add:** Search text is a plan for evidence acquisition, never evidence itself.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The seed does not mark whether queries were executed.
- **supporting_reason:** Keep all rows `unexecuted_no_browse`, require authorization, inspect target versions first, and search only when local/target evidence leaves a precise gap.
- **counterargument_or_limit:** Time-sensitive security or migration issues may require external-first retrieval.
- **assumptions_and_boundaries:** External-first still freezes target identity and records exact support/limits.
- **revision_decision:** Add execution state and a decision-triggered research packet.
- **additional_insight_to_add:** An explicit unexecuted state prevents future readers from mistaking a query inventory for a literature review.

### Question 03: When does the default work well?
- **current_section_observation:** No favorable research conditions are named.
- **supporting_reason:** Refresh works when an API/version/tooling claim is consequential, target versions are known, and official artifacts can be matched and reproduced.
- **counterargument_or_limit:** Domain-state and organizational-policy questions may not be answerable on the public web.
- **assumptions_and_boundaries:** Route those to owners rather than broadening search.
- **revision_decision:** Add query applicability and owner route.
- **additional_insight_to_add:** Knowing that a question is non-researchable is part of good research planning.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** Broad searches can return SEO summaries, outdated versions, examples, and unrelated Android/server guidance.
- **supporting_reason:** Adopting them can create version drift and authority errors.
- **counterargument_or_limit:** Secondary results can identify primary-source vocabulary.
- **assumptions_and_boundaries:** Use secondary material for discovery only and promote primary artifacts plus target evidence.
- **revision_decision:** Add source-quality filters and no-result/contradiction outcomes.
- **additional_insight_to_add:** Search failure includes finding many results that cannot answer the target claim.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The seed only lists web-search phrases, not direct official navigation, repository/release search, local source search, or target experiments.
- **supporting_reason:** Direct official artifacts reduce noise, repository history exposes implementation changes, and target experiments establish applicability.
- **counterargument_or_limit:** Direct navigation can miss newly renamed or moved content.
- **assumptions_and_boundaries:** Use broad discovery only when precise official routes fail.
- **revision_decision:** Add retrieval ladder and cost/authority tradeoff.
- **additional_insight_to_add:** Search should stop when a stronger direct source and target reproduction close the claim.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Missing hazards include query-result citation, undated mutable pages, default-branch drift, version mismatch, duplicate reposts, content over-quotation, and no target reproduction.
- **supporting_reason:** These make research non-reconstructable or legally/semantically unsafe.
- **counterargument_or_limit:** Not every orientation note needs immutable archival identity.
- **assumptions_and_boundaries:** Full capture applies when a result changes code, policy, or completion; orientation remains unpromoted.
- **revision_decision:** Add research integrity and minimal-quotation rules.
- **additional_insight_to_add:** A query can be reproducible while its results change, so artifact identity matters more than query identity.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** No search-to-decision examples exist.
- **supporting_reason:** Good refresh retrieves versioned official cancellation guidance and reproduces it; bad refresh cites snippets; borderline refresh finds a guide for a different framework version.
- **counterargument_or_limit:** Different-version evidence can suggest a hypothesis.
- **assumptions_and_boundaries:** Keep it informative only until adapted and verified.
- **revision_decision:** Add research outcome examples and promotion states.
- **additional_insight_to_add:** A useful research result can be rejection for scope when it prevents a mismatched adoption.

### Question 08: How can the important claims be verified?
- **current_section_observation:** The seed table has no query log, artifact capture, source span, version match, or target test.
- **supporting_reason:** Recording authorization, query, result identity, retrieval date, support/limit, target match, reproduction, and outcome makes research auditable.
- **counterargument_or_limit:** Search rankings and mutable pages remain irreproducible.
- **assumptions_and_boundaries:** Preserve the selected artifact identity and do not claim ranking completeness.
- **revision_decision:** Add research record schema and verification ladder.
- **additional_insight_to_add:** Research completeness should be defined by claim closure, not number of results read.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** Exact query strings are seed facts; none was executed and no result was observed.
- **supporting_reason:** Their state can be reported precisely without browsing.
- **counterargument_or_limit:** The phrases may be too broad or use noncanonical terminology.
- **assumptions_and_boundaries:** Refine only during authorized research and preserve original strings for provenance.
- **revision_decision:** Add no-results ledger and prohibit current external claims.
- **additional_insight_to_add:** Query quality is currently untested and should not be inferred from grammatical plausibility.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The seed implies periodic broad refresh rather than selective claim invalidation.
- **supporting_reason:** Dependency, framework, compiler, or source changes should reopen only related queries and guidance.
- **counterargument_or_limit:** Selective tracking needs maintenance and can miss ecosystem-wide shifts.
- **assumptions_and_boundaries:** Add periodic owner review only for high-impact shared references while retaining event-triggered refresh.
- **revision_decision:** Introduce queued, selective refresh lifecycle and retirement.
- **additional_insight_to_add:** A query should be retired when it repeatedly yields no decision-relevant evidence or a stable direct source replaces it.

## Section 026: Evidence Boundary Notes
### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed defines three labels but not how a claim is promoted, contradicted, invalidated, or reused.
- **supporting_reason:** Final evidence notes should let readers distinguish inherited guidance, target observation, owner policy, inference, proposal, result, and no-claim states.
- **counterargument_or_limit:** A detailed taxonomy can make prose cumbersome.
- **assumptions_and_boundaries:** Use concise claim cards for consequential/reused decisions and inline labels for simple orientation.
- **revision_decision:** Expand the three labels into a lifecycle and audit protocol while preserving their exact meanings.
- **additional_insight_to_add:** Evidence boundary is a property of each claim, not a label applied once to a whole section.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The seed does not state the safest initial evidence status.
- **supporting_reason:** Begin claims at observed local/target, inference, proposal, blocked, or no-claim; promote only with matching support and target closure.
- **counterargument_or_limit:** Stable language principles may not need a formal promotion record every time.
- **assumptions_and_boundaries:** State them as bounded inference with premises and limits when they direct consequential work.
- **revision_decision:** Add conservative initial states and promotion rules.
- **additional_insight_to_add:** Promotion should be monotonic in evidence quality but reversible when an invalidating premise changes.

### Question 03: When does the default work well?
- **current_section_observation:** No fit criteria for full claim cards or lightweight labels exist.
- **supporting_reason:** Full cards are valuable for public/persisted/concurrent/runtime/shared decisions; lightweight labels fit low-risk orientation.
- **counterargument_or_limit:** Risk can be underestimated initially.
- **assumptions_and_boundaries:** Escalate evidence form when caller/owner/runtime scope expands.
- **revision_decision:** Add evidence-profile selection and escalation.
- **additional_insight_to_add:** Evidence ceremony should follow claim durability and consequence.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** Labels can become decorative while prose still overstates source or target behavior.
- **supporting_reason:** A local-fact prefix does not support a sentence whose second half is an unverified runtime conclusion.
- **counterargument_or_limit:** Splitting every sentence can harm readability.
- **assumptions_and_boundaries:** Split materially different evidence states into separate claims or clauses.
- **revision_decision:** Add mixed-claim and label-washing audit rules.
- **additional_insight_to_add:** One sentence can contain several claims with different evidence boundaries.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The seed taxonomy lacks target source, tests, runtime, owner policy, characterization, accepted risk, and contradictory evidence.
- **supporting_reason:** These distinctions prevent tests from choosing policy and prose from claiming runtime results.
- **counterargument_or_limit:** Too many labels can confuse consumers.
- **assumptions_and_boundaries:** Group labels into observed, normative, synthesized, result, and unresolved families with precise subtypes when needed.
- **revision_decision:** Add a layered taxonomy and usage table.
- **additional_insight_to_add:** A small number of evidence families can preserve rigor while allowing richer internal states.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Missing hazards include official-URL promotion, test-population overreach, code-as-policy, owner-decision-as-enforcement, characterization-as-correctness, and stale-evidence reuse.
- **supporting_reason:** These category errors create false confidence even when every statement has a source.
- **counterargument_or_limit:** Readers may infer some limits from context.
- **assumptions_and_boundaries:** Make limits explicit for consequential or reusable guidance.
- **revision_decision:** Add prohibited inference table and selective invalidation.
- **additional_insight_to_add:** Sourced claims can still be unsupported when the source type cannot establish the conclusion.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** The seed lists definitions but no claim examples.
- **supporting_reason:** Good claims separate source guidance, target finding, proposed repair, test result, and no-capacity-claim; bad claims blend them; borderline claims have characterization but no owner policy.
- **counterargument_or_limit:** Examples remain context-specific.
- **assumptions_and_boundaries:** Use claim structure rather than copy wording.
- **revision_decision:** Add contrastive claim cards and promotion outcomes.
- **additional_insight_to_add:** A borderline claim can be highly informative while remaining unpromoted.

### Question 08: How can the important claims be verified?
- **current_section_observation:** The seed has no audit for source identity, label accuracy, support span, target closure, contradiction, or invalidation.
- **supporting_reason:** Claim cards, hashes/versions, test populations, owner records, no-results ledgers, and dependency triggers support a focused audit.
- **counterargument_or_limit:** Manual semantic review remains necessary.
- **assumptions_and_boundaries:** Automate structure and identity; review support and inference quality skeptically.
- **revision_decision:** Add final evidence audit checklist.
- **additional_insight_to_add:** Verification should sample both promoted claims and explicit non-claims to catch hidden overreach.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The seed, local source, specification, tests, queue rows, and current outputs are known local artifacts; public content and target Kotlin behavior are unobserved.
- **supporting_reason:** These facts support exact provenance and structural claims for Assignment 9.
- **counterargument_or_limit:** The reference's extensive operational guidance is synthesized rather than target-validated.
- **assumptions_and_boundaries:** Present it as decision guidance requiring target adaptation and verification.
- **revision_decision:** Add a complete known/unknown ledger.
- **additional_insight_to_add:** Structural verifier success is evidence about artifact contract, not about real-world Kotlin effectiveness.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The seed notes do not define how evidence boundaries survive copying into prompts, reviews, or new references.
- **supporting_reason:** Reuse can strip source identity, limits, no-claim state, or invalidation and turn bounded guidance into a universal rule.
- **counterargument_or_limit:** Copying full provenance everywhere is unwieldy.
- **assumptions_and_boundaries:** Carry a compact claim card or direct link plus target revalidation.
- **revision_decision:** Add reuse, derivation, and selective-refresh protocol.
- **additional_insight_to_add:** Provenance compression is safe only when it preserves authority, scope, limits, and reopening conditions.
