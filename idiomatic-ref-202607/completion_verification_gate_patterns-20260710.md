# Completion Verification Gate Patterns

A completion statement is a scoped claim about observable work state. It can end investigation, authorize a handoff, move to another assignment, or support a merge or release decision. Make it only after fresh evidence capable of proving that exact state has been run, read, and interpreted against the current candidate.

The governing rule from the inspected local lineage is simple: evidence precedes success language. The operational work is less simple because `tests pass`, `build succeeds`, `bug fixed`, `requirements met`, `artifact renders correctly`, `agent completed`, and `ready to release` are different claims with different gates.

**Claim-Evidence Contract**

Before stating or implying completion:

1. Define the exact proposition a reasonable reader will infer.
2. Identify the current candidate, requirement, environment, and scope covered.
3. Select the least-risk evidence set capable of discriminating that proposition.
4. Predeclare what pass, relevant fail, blocked, unrun, and not-applicable states mean.
5. Inspect command side effects, permissions, data, cleanup, fallback, and owner boundary.
6. Run the full evaluator freshly against the current candidate.
7. Read complete output, exit status, failure and skip counts, warnings, and exclusions.
8. Compare observed evidence with every clause in the intended statement.
9. Report only the supported state, including failures, blocked gates, and residual uncertainty.
10. Preserve enough evidence for another reviewer to reproduce the conclusion.

Skipping from code change, confidence, prior output, or delegated success directly to a completion statement breaks this contract. A narrower truthful result is preferable to a broad optimistic claim.

**Common Claims and Required Evidence**

| claim | minimum evidence shape | common insufficient substitute |
| --- | --- | --- |
| Tests pass | Current full applicable test command, exit result, zero relevant failures, skip interpretation, and candidate identity. | Earlier run, one test file, or `should pass`. |
| Build succeeds | Current production-relevant build command and exit zero for declared target. | Linter success, editor diagnostics, or logs that merely look normal. |
| Linter or formatter clean | Full configured command, current paths, and zero applicable violations. | Checking one file or assuming staged paths equal all changed paths. |
| Bug fixed | Original symptom or mechanism fails on defective baseline and passes on current repair, plus relevant regression checks. | Code changed, direct test passes once, or reviewer agrees. |
| Regression test works | Test is shown sensitive through red-green verification or an equivalent safe mutation. | New test passes only after the fix with no evidence it can detect the defect. |
| Requirements met | Each in-scope requirement maps to observed test, review assertion, artifact, owner decision, or explicit unresolved state. | General tests pass or checklist headings exist. |
| Artifact is usable | Generated artifact exists, required structure passes, and representative visual or behavioral inspection covers intended use. | File presence, valid syntax, or generation command exit alone. |
| Delegated work completed | Returned claim is checked against current diff, requirements, verification, and shared-workspace state. | Agent or worker reports success. |
| Review findings resolved | Every finding has current disposition, evidence, changed or unchanged result, and re-review where required. | Thread closed or comment text changed. |
| Ready to merge or release | All applicable technical, requirement, safety, policy, owner, recovery, and repository gates pass for the current candidate. | Reviewer confidence or a green subset of checks. |

One command may support several clauses, but command count does not create coverage. Several commands can all observe the same proxy while missing the requirement that matters.

**Claim Grammar**

A useful completion report names:

```text
claim:
candidate_and_scope:
fresh_evidence:
observed_result:
failures_skips_and_unrun_gates:
what_the_evidence_does_not_prove:
owner_or_policy_boundary:
allowed_next_action:
```

For example: `The current Linux debug build succeeds: [command] exited 0 at [candidate]. The Windows target and release packaging were not run, so this does not establish cross-platform release readiness.`

Narrow wording is not hedging when it accurately follows evidence. `Formatter clean` is stronger than `probably complete` because the former has a defined truth condition.

**Freshness and Candidate Identity**

Fresh means the evidence was produced after every material change to the candidate, requirement, environment, dependency, generated input, or configuration relevant to the claim. Record enough identity to detect:

- edits after the run;
- a different worktree, branch, base, head, or package;
- cached or skipped execution;
- generated output not rebuilt from changed inputs;
- platform, feature, dependency, or environment mismatch;
- concurrent changes from another owner;
- approval or review tied to an older diff.

Fresh evidence can expire immediately after a consequential edit. Do not reuse a green label merely because the command text remains the same.

**Gate Fit**

The gate works well when the claim has observable criteria and the evaluator can turn red for the relevant defect. Use:

- unit, integration, property, or scenario tests for behavior;
- compilation and type checks for build and contract shape;
- static analyzers, linters, formatters, and schema validators for deterministic invariants;
- exact diff and generated-output inspection for change identity;
- requirement trace and negative examples for scope completion;
- rendered, visual, accessibility, or interaction inspection for user-facing artifacts;
- safe fault, rollback, or tabletop exercises for recovery;
- peer or specialist review for architecture, security, data, production, and other judgment domains;
- owner records for product intent, policy, merge, release, and accepted residual risk.

Do not force an unsafe production, credentialed, destructive, private-data, or external-effect command to obtain a green result. Use a disposable evaluator, static evidence, simulation, owner-run proof, or an honest blocked state.

**Hard Stops**

Do not assert the dependent completion state when:

- the proving evaluator is unknown, unavailable, unsafe, or unauthorized;
- the run is stale, partial, canceled, timed out, cached ambiguously, or against another candidate;
- output contains a failure, skip, warning, or untested clause material to the claim;
- the gate checks syntax or presence while the statement claims behavior or requirements;
- a regression test was never shown capable of detecting the original defect;
- a delegated report was not reconciled with actual files and current state;
- requirements, generated artifacts, migrations, supported environments, or owner decisions remain unchecked;
- another writer changed the target after evidence or approval;
- fallback, rollback, or residual state is unknown for a consequential change;
- the user or policy prohibits the needed operation.

Read-only diagnosis can continue at a hard stop. Report the first unmet gate, completed evidence, current safe state, and exact next route.

**Good, Bad, and Partial Statements**

Good test claim: `The full current package suite passes: [command] exited 0 with 34 passed and no relevant skips. Integration tests for the external service were not part of this package suite.`

Bad test claim: `The changes look correct and should pass.` No fresh result supports the implied state.

Good bug claim: `The original empty-input case fails on the defective baseline, passes on this candidate, and the surrounding suite passes. The production-only data source was not exercised.`

Bad regression claim: `I added a regression test.` Test presence does not show sensitivity.

Good delegated claim: `The worker reported completion; I inspected the returned diff, confirmed only approved paths changed, reran the current focused verifier, and found [result].`

Partial but complete-for-purpose: `Compilation and static checks pass. Behavioral integration verification is blocked because the approved fixture is unavailable; release readiness is not claimed.`

Unsafe route: a reviewer proposes running a production migration to prove recovery. Do not execute it for conversational completeness. Preserve the claim as unverified and route the approved owner process.

**Evidence Status**

The current and archived local verification-before-completion sources were completely read and were byte-identical at the recorded boundary. They directly support fresh full command execution, complete output reading, red-green regression sensitivity, requirement-by-requirement review, and independent verification of delegated claims.

No public source was opened during this evolution. Inherited public URLs remain future locators, not current external facts. The expanded gate taxonomy, lifecycle, metrics, backpressure, observability, and scale guidance are systems synthesis to validate under each repository's policy and consequence model. No universal success rate, freshness interval, test count, or acceptable residual risk is established.

**Completion Gate Audit**

A fresh reviewer should select each broad success statement and reconstruct its exact proposition, current candidate, applicable requirements, gate, side-effect boundary, full result, failures and skips, interpretation, owner, and exclusions. Where safe, a known defective or mutated case should turn the controlling gate red. Changing the candidate after a run should invalidate its completion state.

Completion verification is not about pessimistic tone. It is about making work states reproducible. Mature systems make truthful success concise by automating stable invariants, while preserving explicit blocked and uncertain states for claims that still require judgment or safer evidence.

## Source Evidence Mapping Table

This map routes each completion premise to evidence capable of supporting it. The verification skill explains method. It does not supply the target requirement, current candidate, command output, artifact quality, owner decision, or release policy needed for a real claim.

**Local Content Lineage**

| lineage | locators | recorded SHA-256 | directly supports | cannot establish alone |
| --- | --- | --- | --- | --- |
| Verification before completion | `claude-skills/superpowers/verification-before-completion/SKILL.md`; archive counterpart under `agents-used-monthly-archive/claude-skills-202603/` | `ea52d15aabaf72bc6b558efe2c126f161b53961090ddcd712000273bfe8c7b6c` | Fresh full command execution before success claims; complete output reading; claim-specific evidence; red-green regression sensitivity; requirement checklist review; independent verification of delegated work. | Target correctness, current command names, universal coverage, current hosted platform behavior, organization policy, merge authority, or measured trust improvement. |

The two locators were byte-identical at the recorded boundary and count as one evidentiary lineage. Use the current copy for practical retrieval while identity holds and the archive for provenance. Recompute identity before assuming future interchangeability; historical reconstruction or divergence can change their roles.

**Evidence Needed for a Target Claim**

| evidence class | question answered | examples | characteristic limit |
| --- | --- | --- | --- |
| User and requirement | What result and scope were requested? | Current user instruction, accepted issue, executable requirement, plan, API or artifact contract. | Intent can be incomplete, inconsistent, or outside the author's authority. |
| Candidate identity | What exact work is being claimed complete? | Revision, worktree, diff, package, generated inputs and outputs, dependencies, environment. | A revision can omit dirty, generated, external, migration, or configuration effects. |
| Evaluator definition | What operation can discriminate the claim? | Test, build, static rule, renderer, visual review, requirement checklist, recovery exercise. | A plausible command may observe only a proxy or be unsafe. |
| Observed result | What happened when the evaluator ran? | Exit status, pass/fail/skip counts, assertion, screenshot, rendered state, artifact inspection. | One observation is bounded to its inputs, environment, and time. |
| Failure sensitivity | Can the gate reject the relevant defect? | Red-green cycle, safe mutation, known-invalid fixture, source proof of a failing path. | An injected case can be unrepresentative or unsafe in stateful systems. |
| Scope and non-interference | Which requirements and intended plus non-intended paths are covered? | Traceability matrix, compatibility cases, contextual diff, generated-output audit. | Declared coverage cannot prove absence of unknown requirements or defects. |
| Safety and policy | May this evaluator and result be used here? | Repository policy, security or data rules, approved environment, cleanup and retention. | Permission cannot make a technically irrelevant result sufficient. |
| Owner decision | Who can accept intent, architecture, specialist risk, merge, release, or residual uncertainty? | Product, code, security, service, repository, release, or integration owner record. | Authority cannot make a false test or behavior claim true. |
| Recovery | Can a failed candidate or gate return to a safe state? | Native fallback, rollback, residual-state check, disablement, requalification. | Written rollback may share the failed dependency or omit persistent effects. |
| Outcome evidence | Did the completion gate improve accepted work at acceptable cost? | Corrections, escaped defects, false blocking, reviewer time, maintenance and retirement. | Attribution is confounded by task mix, tools, authors, and later changes. |

**Claim-to-Source Routing**

| proposed statement | open first | expand when | completion evidence |
| --- | --- | --- | --- |
| `Tests pass` | Repository test instructions, current candidate, and full applicable test output. | Skips, platforms, services, generated fixtures, or test selection can change meaning. | Zero relevant failures with scope, candidate, and exclusions stated. |
| `Build succeeds` | Current build contract and target-specific full command. | Release mode, features, architectures, packaging, or generated assets differ. | Exit zero for declared target plus material warnings and omitted targets reported. |
| `Bug fixed` | Original requirement and symptom or mechanism. | Cause, environment, concurrency, state, migration, or external service is disputed. | Defective baseline red, current candidate green, integrated non-regression, and bounded uncertainty. |
| `Regression test works` | Test source, original defect, and safe sensitivity method. | Mutation cannot be run safely or fixture may be a proxy. | Gate demonstrably turns red for relevant defect and green for accepted repair. |
| `Requirements met` | Current requirement inventory and candidate behavior. | Tests omit a clause, owner intent changed, or requirement conflicts. | Every in-scope clause has evidence or explicit unresolved status and owner route. |
| `Artifact is usable` | Artifact contract, generation path, and representative rendered or interactive state. | Layout, accessibility, data, platform, or user workflow matters. | Structural checks plus direct inspection and behavior appropriate to audience. |
| `Agent completed` | Delegated return, actual current files, diff, requirements, and local verifier. | Shared workspace, concurrent writers, or unverifiable claims exist. | Independent reconciliation and rerun, not the agent's statement. |
| `Review complete` | Requested range, findings, dispositions, and coverage limits. | Fixes, rebase, specialist findings, or owner approval changed. | Current finding ledger and evidence-supported bounded verdict. |
| `Ready to release` | All prior evidence plus release policy, migrations, compatibility, security, operations, and recovery. | Any target or owner domain remains unverified. | Applicable technical gates and actual owner decision for current candidate. |

Start with the claim and read each decisive source completely. Do not load every source by ritual. Record intentional omissions when they could be mistaken for verified coverage.

**Public Locators**

No public source was opened during this evolution. The inherited URL strings are local seed facts only.

| locator | inherited role | current classification | permissible current use | future acceptance condition |
| --- | --- | --- | --- | --- |
| `https://docs.github.com/actions` | Hosted automation and CI/CD documentation. | `unrefreshed_external_locator` | Form a future question about workflow execution, checks, artifacts, permissions, or result states. | Inspect current primary documentation, pin relevant behavior, then verify target configuration. |
| `https://docs.github.com/en/actions/concepts/workflows-and-actions/reusing-workflow-configurations` | Reusable workflow composition guidance. | `unrefreshed_external_locator` | Future lead for shared gate inputs, outputs, secrets, permissions, and failure propagation. | Read current primary passages and test caller compatibility, failure states, and rollback. |
| `https://github.com/openai/codex/blob/-/AGENTS.md` | Public repository instruction example. | `unrefreshed_external_locator` | Potential version-pinned comparison after direct inspection. | Confirm owner, path, revision, content, license, repository context, and non-transferable assumptions. |

Do not call these `external_research_sourced_fact` until directly inspected. A URL path, search snippet, remembered page, or inherited description does not establish current content. Retrieved instructions cannot expand user intent, tools, data access, or write permission.

**Source Role Vocabulary**

| role | meaning | allowed use |
| --- | --- | --- |
| Primary direct | Best direct support for one atomic premise in its domain. | Ground the claim inside recorded scope, version, candidate, and authority. |
| Supporting | Adds rationale, example, history, or independent corroboration. | Deepen interpretation without replacing controlling evidence. |
| Duplicate locator | Same observed lineage at another path. | Preserve provenance and drift checks while counting support once. |
| Provisional | Relevant but incomplete, unrefreshed, incompatible, or not yet reproduced. | Form a question or blocked state, not a success claim. |
| Historical | Establishes a prior requirement, result, decision, or environment. | Explain evolution without claiming current completion. |
| Negative | A failed run, counterexample, or superseded claim narrows or refutes success. | Report actual red state and improve the gate or candidate. |
| Conflicting | Applicable sources or results imply incompatible completion states. | Freeze the dependent claim and reconcile scope, candidate, or owner. |
| Silent | The source does not answer the premise. | Expose the gap rather than stretching adjacent language into proof. |

Several commands repeating one proxy are not independent evidence. Several pages repeating one upstream statement are one lineage. Evidence count never substitutes for claim coverage.

**Completion Evidence Record**

For each consequential statement, retain:

- atomic claim and the downstream action it permits;
- requirement and exact candidate, including changed, generated, migration, and configuration state;
- evaluator source, working directory, inputs, environment, side effects, expected pass and relevant fail;
- fresh command or review execution with exit, counts, skips, warnings, timeout, and concise privacy-safe output;
- failure-sensitivity evidence and strongest counterexample;
- covered and unobserved requirements, paths, platforms, users, and conditions;
- policy and owner domains, plus actions the evidence cannot authorize;
- fallback, rollback, residual state, and requalification;
- status such as pass, fail, blocked, unrun, stale, conflicting, or not applicable with reason;
- invalidation event and evidence expiry.

Link large logs, diffs, screenshots, and artifacts. Do not copy secrets, private payloads, raw prompts, hidden reasoning, or unrelated repository content.

**Invalidation Rules**

- Any material edit after a run invalidates affected completion statements.
- A force-push, dependency, config, environment, requirement, or generated-input change reopens gates that depend on it.
- A passing test does not preserve completion when the expected behavior changes.
- A delegated result becomes historical after another writer changes the same surface.
- Owner approval does not transfer to a materially different candidate or scope.
- A public platform fact, once refreshed, still requires target compatibility and local permission.
- Removing or replacing a gate requires residual checks so stale success labels do not remain active.

**Source Map Audit**

A fresh reviewer should reproduce the local pair identity, distinguish method from target evidence, reconstruct candidate and requirement scope, verify each source semantically supports its premise, confirm public locators remain unrefreshed, inspect failures and skips, and change one premise to find every completion state that must regress.

Automate hashes, candidate fingerprints, link shape, and required fields where practical. Semantic entailment, intended behavior, safe sufficiency, specialist risk, and acceptable residual uncertainty remain accountable judgments. The map succeeds when it shortens truthful verification and makes stale completion visible, not when it maximizes citations.

## Pattern Scoreboard Ranking Table

The seed assigns 95, 91, and 88 to three controls without a scoring method, evaluator, candidate set, sample, date, or calibration. Preserve the values as inherited metadata only. They are not success probabilities, reliability rates, completion thresholds, or evidence that one control is seven points stronger than another.

| inherited control | inherited value | bounded interpretation | intended failure prevention | stronger evidence required |
| --- | ---: | --- | --- | --- |
| Source Map First | 95 | High-priority seed method; cardinal magnitude uncalibrated. | Verification guidance is synthesized without reading applicable local method, requirements, candidate, or repository gates. | Comparable completion tasks measuring source omissions, false claims, verification effort, and later correction. |
| Evidence Boundary Split | 91 | High-priority claim-discipline control; exact order unproven. | Method, target fact, command output, inference, and owner decision collapse into one confident completion statement. | Independent claim audits, contradiction cases, agreement on bounded state, and invalidation behavior. |
| Verification Gate Coupling | 88 | High-priority state-transition control; value does not certify gate quality. | Success is inferred from code presence, confidence, or unrelated green checks. | Known pass and relevant fail cases, requirement trace, current-candidate evidence, and recovery results. |

The controls form a chain. Mapping finds evidence. Boundary separation prevents one source from proving another domain. Gate coupling tests the current claim. Omission of one cannot be offset by a higher profile elsewhere.

**Stage One: Completion Eligibility Gates**

Apply these before comparing verification methods or making a success statement. A red gate blocks only the dependent claim and any downstream action that requires it.

| hard gate | pass condition | red condition | safe response |
| --- | --- | --- | --- |
| Atomic claim | The exact externally checkable proposition and permitted next action are stated. | `Done`, `works`, or `ready` remains ambiguous or compound. | Split the claim and identify evidence per clause. |
| Current candidate | Revision, worktree, paths, generated outputs, dependencies, config, and environment match the statement. | Evidence predates a material change or ran elsewhere. | Invalidate stale result and rerun current gates. |
| Applicable requirement | Accepted behavior and scope are explicit and current. | Tests pass but a requirement is missing, disputed, or superseded. | Clarify intent, update trace, and withhold broad completion. |
| Relevant evaluator | Gate can discriminate the claimed state and original failure. | Check observes syntax, presence, or a proxy while claim is behavioral. | Select or design a claim-sensitive evaluator. |
| Safe execution | Inputs, side effects, data, credentials, environment, cleanup, and authority are acceptable. | Command is destructive, production, credentialed, private, or externally consequential without approval. | Use static, disposable, simulated, specialist, or owner-run evidence. |
| Full fresh result | Complete applicable command or review ran now; exit, failures, skips, warnings, and timeout are read. | Partial output, earlier run, hidden skip, cache ambiguity, timeout, or nonzero state. | Report actual result and resolve or rerun after changed conditions. |
| Scope and non-interference | Every in-scope requirement and material intended plus non-intended path has evidence or explicit exclusion. | Aggregate green hides an untested clause, platform, migration, or generated artifact. | Narrow claim, add evidence, or keep state blocked. |
| Authority | Actual owners and policy permit the asserted transition and residual risk. | Technical success is treated as merge, release, security, or product approval. | Preserve technical result and route owner decision. |
| Recovery | Fallback, rollback, residual state, and requalification are usable where consequence requires them. | Candidate or gate cannot return to a verified safe state. | Reduce scope, redesign recovery, or reject readiness. |

Do not average these gates. Eight passes and one stale candidate is not current completion. A technically valid result with unauthorized execution remains unacceptable evidence.

**Stage Two: Evidence Profile**

After hard gates pass, rate relevant dimensions `strong`, `mixed`, `weak`, or `not applicable`, always with a concise reason. Do not sum labels into an unsupported total.

| dimension | strong | mixed | weak | decision use |
| --- | --- | --- | --- | --- |
| Claim alignment | Gate directly observes the exact proposition and requirement. | Gate covers most clauses but one interpretation or owner question remains. | Convenient check is only loosely related to the statement. | Decide whether result can support wording. |
| Failure sensitivity | Known defective or safely mutated condition turns red for expected reason. | Source reasoning supports sensitivity but direct mutation is unavailable. | Gate has never demonstrated ability to reject the target failure. | Distinguish regression evidence from ceremony. |
| Freshness | Candidate and all material inputs are fingerprinted after final change. | One low-impact environment or generated input is inferred stable. | Result predates edits or candidate identity is unknown. | Retain, narrow, or invalidate evidence. |
| Requirement coverage | Every declared clause has direct evidence or explicit owner resolution. | Some clauses rely on review judgment or bounded unrun conditions. | General green suite substitutes for traceability. | Claim requirements met or expose gaps. |
| Result completeness | Full output, exit, failures, skips, warnings, timeout, and cleanup are reconciled. | Tool hides some internals but relevant result can be independently checked. | Only summary line or favorable excerpt is retained. | Trust or rerun execution evidence. |
| Reproducibility | Fresh reviewer can run or inspect the evidence from saved context. | Environment is specialized but an owner can reproduce it. | Result depends on private memory or unavailable state. | Support handoff and future invalidation. |
| Non-interference | Representative unrelated paths remain valid and no hidden artifact changes. | Direct behavior passes while broader tail is explicitly unobserved. | Fix proves one case but creates unknown regression surface. | Bound bug-fixed or readiness claim. |
| Safety and privacy | Least-risk evaluator, minimized data, approved effects, and cleanup are verified. | Safe substitute narrows direct observation. | Evidence exposes data or creates uncontrolled effects. | Permit use or invoke containment. |
| Recovery | Independent fallback and residual checks pass. | Rollback exists but some operational tail needs owner assurance. | Recovery is prose only or shares failed dependency. | Support consequential readiness. |
| Lifecycle cost | Gate has owner, maintenance, false-blocking review, fallback, and retirement path. | Value is clear but long-term burden remains uncertain. | Shared gate has no owner or removal condition. | Adopt, narrow, improve, or retire control. |

Use the profile to locate disagreement. One reviewer may dispute test sensitivity while another accepts the test but disputes requirement scope. A single score would hide the repair needed.

**Candidate Gate Portfolio**

For a material claim, consider:

- the repository's canonical full command;
- a focused test plus the full relevant suite;
- static or source proof where execution is unsafe;
- red-green or safe mutation for regression sensitivity;
- requirement-by-requirement checklist and owner resolution;
- generated artifact rebuild and contextual diff;
- visual, accessibility, or interaction inspection;
- compatibility and migration matrix;
- fault, cancellation, fallback, or rollback exercise;
- independent reviewer or specialist assessment;
- a narrower completion statement;
- an honest blocked, failed, stale, or unrun state.

Do not treat a command as mandatory merely because it exists. Do not treat no completion claim as failure; it can be the correct state until evidence matures.

**Decision Rules**

| evidence state | default statement and action | required record |
| --- | --- | --- |
| Any hard gate red | Do not make dependent success claim; contain, investigate, narrow, rerun, or route. | Exact red, current safe state, owner, and resume condition. |
| Strong direct and integrated evidence | State bounded completion and proceed only to authorized next action. | Claim, candidate, command, result, coverage, exclusions, and expiry. |
| Direct pass with incomplete broader scope | Report focused pass; keep broad completion blocked. | Passed clause, unrun clauses, consequence, and next evaluator. |
| Safe evaluator unavailable | Report blocked or unverified; use alternative evidence if sufficient. | Safety boundary, available evidence, owner route, and fallback. |
| Gate fails or finds defect | Report actual red state and preserve output; repair candidate or requirement. | Failure, diagnosis boundary, changed condition, and next gate. |
| Evidence conflicts | Freeze dependent statement and reconcile candidate, requirement, environment, or owner. | Both results, scopes, strongest explanations, and resolver. |
| Prior run became stale | Demote to historical evidence and rerun where still needed. | Invalidation event and affected claims. |
| Claim no longer matters | Retire gate and remove stale completion dependencies. | Replacement or no-need evidence, owner, and residual audit. |

**Illustrative Profiles**

Good bug fix: old candidate fails the exact boundary case, current candidate passes it, full relevant suite passes, final diff is scoped, and requirement plus recovery are current. State the bounded fix; no numeric score is needed.

Bad readiness: formatter, linter, and compilation pass, but the requirement concerns runtime retry behavior and its integration test never ran. Hard claim alignment is red. Three green commands do not support readiness.

Stale evidence: full tests passed, then generated input and implementation changed. Candidate freshness is red even if the same suite is expected to pass. Rerun before claiming.

Borderline artifact: structural validation passes and desktop rendering was inspected, but mobile interaction could not be exercised. Report structural and desktop results; keep cross-viewport usability unverified.

Good blocked state: a migration rollback requires an approved disposable database that is unavailable. Preserve other passes, state the recovery gate is blocked, and do not claim release readiness.

**Calibration and Audit**

The inherited numbers cannot be reproduced from available evidence. Validate the replacement by freezing claim, candidates, requirements, and evaluators; presenting known-valid, known-invalid, stale, partial, unsafe, delegated, and requirement-gap cases; and confirming hard reds prevent broad completion.

Ask independent reviewers to record exact allowed state. Disagreement should be traceable to claim, candidate, requirement, sensitivity, scope, safety, or authority. Agreement is not correctness when all reviewers share one proxy.

What the scoreboard rewards shapes verification. Command-count incentives create redundant green output. Speed incentives skip requirements. Coverage percentages can hide wrong intent. Use the profile to allocate attention and improve gates, never to automate truth or owner authority. Retire profile dimensions and manual checks after stable deterministic controls make them ordinary infrastructure.

## Idiomatic Thesis Synthesis Statement

**Thesis:** A completion statement is warranted only when fresh evidence, run against the current candidate, can falsify and then support the exact claimed state. The result must be read completely, bounded to what it observes, reconciled with requirements and owner authority, and invalidated when a material premise changes.

This separates questions that optimistic workflow language often collapses:

1. What exact state is being asserted?
2. Which current candidate, requirement, and environment does it cover?
3. Can the evaluator turn red for the relevant failure?
4. What did the full fresh result actually show?
5. Which clauses, platforms, artifacts, or risks remain unobserved?
6. Who can authorize the downstream action and accept residual uncertainty?
7. Can failed work or a failed gate return to a verified safe state?

A test can pass while a requirement is missing. A bug can be fixed while release readiness remains blocked. A reviewer can accept technical evidence without owning merge. Preserve these split states.

**Evidence Synthesis**

- `local_corpus_sourced_fact`: The inspected verification-before-completion lineage directly requires fresh full execution and output reading before success claims. It also supports red-green regression sensitivity, requirement-by-requirement checking, and independent validation of delegated work. Current and archive copies were byte-identical at the recorded boundary.
- `target_evidence_required`: Real claims require current requirements, candidate identity, repository commands, observed results, generated artifacts, environments, policy, owners, and recovery evidence from the target task.
- `external_research_status`: The inherited public URLs were not opened. They remain discovery locators, not current external facts. Refresh hosted workflow semantics only when they materially affect a claim and browsing is allowed.
- `combined_evidence_inference_note`: Claim taxonomies, state transitions, gate portfolios, backpressure, outcome measurement, and lifecycle retirement are reasoned systems guidance to validate locally; no universal effectiveness is established.

Evidence order follows the premise. Requirements define intended state. Source and tests establish current implementation and observed cases. Primary external or installed evidence establishes version-sensitive platform behavior. Owners decide scope, policy, merge, release, and residual risk. No source inherits another domain's authority.

**Verification Lifecycle**

```text
define exact claim and allowed next action
  -> freeze requirement, candidate, environment, and owners
  -> select a claim-sensitive evidence set
  -> preflight safety, privacy, side effects, and recovery
  -> define expected pass, relevant fail, block, and stop
  -> execute full evaluator freshly
  -> read exit, failures, skips, warnings, and output
  -> compare evidence with every claim clause
  -> report pass, fail, blocked, stale, unrun, or not applicable
  -> preserve evidence and invalidation trigger
  -> learn, improve, narrow, or retire the gate
```

A failed premise returns to definition or evaluator design. A changed candidate invalidates affected evidence. An authority gap can preserve a technical pass while blocking the operational transition.

**Fit Conditions**

The thesis works best when:

- the statement can be decomposed into externally checkable clauses;
- current candidate and decision-relevant environment can be identified;
- accepted requirements and non-intended behavior are explicit;
- at least one safe evaluator can discriminate the relevant failure;
- full output and skipped conditions can be inspected;
- owners can decide nontechnical scope and residual risk;
- fallback or rollback exists for consequential work;
- evidence can be reproduced or independently reviewed.

Do not infer fit from command availability. A repository can have many green commands and no evaluator for the actual user outcome. A judgment claim can have no useful command yet still support a bounded owner decision with transparent evidence.

**Evidence Form Selection**

| claim family | preferred durable evidence | reason |
| --- | --- | --- |
| Deterministic behavior | Focused failing case plus broader relevant test suite. | Proves the mechanism and checks non-regression. |
| Build and type contract | Full target-specific build or compiler result. | Observes declared artifact construction and static constraints. |
| Structural invariant | Linter, schema, formatter, static analyzer, or exact parser check. | Efficiently enforces deterministic shape within its scope. |
| Requirement completion | Requirement-to-evidence matrix with unresolved clauses visible. | Prevents a general suite from hiding missing intent. |
| User-facing artifact | Structural checks plus rendered, visual, accessibility, and interaction inspection. | File existence and syntax do not establish usability. |
| Generated output | Authoritative input change, regeneration result, contextual diff, and consumer checks. | Direct output edits may disappear or diverge. |
| Compatibility or migration | Version matrix, representative mixed states, forward and rollback path. | Current-only success can break supported users or data. |
| Recovery | Safe fault, rollback, residual-state, and requalification evidence. | Written fallback may not be executable or independent. |
| Architecture or specialist judgment | Alternatives, scenarios, direct constraints, specialist and owner decision. | Several designs can be correct and sensitive tests can remain insufficient. |
| Delegated completion | Actual diff inspection, current local rerun, requirement trace, and shared-state reconciliation. | A worker's report is not independent proof. |
| Explicit inability to verify | Blocked-state record with completed evidence, safety boundary, owner route, and safe fallback. | Honest non-claim is safer than an unsafe or proxy execution. |

Evidence artifacts must hand off coherently. A test without a readable failure, a requirement without an evaluator, a screenshot disconnected from candidate identity, or an owner decision without technical evidence moves uncertainty rather than resolving it.

**Failure Boundary**

Reject, narrow, or pause a completion statement when:

- wording remains broad enough to imply unverified clauses;
- evidence predates a material code, requirement, dependency, generated, config, or environment change;
- the evaluator cannot fail for the target defect;
- only favorable output is read while failures, skips, warnings, or timeout remain;
- a command would be unsafe, unauthorized, destructive, credentialed, production, or privacy-invasive;
- tests pass but no requirement trace establishes intended behavior;
- a delegated agent report is trusted without current file and gate inspection;
- technical success is presented as product, specialist, merge, or release authority;
- fallback and residual state are unknown;
- a completion badge remains after its source or gate was superseded.

Emergency containment is not durable completion. Keep it authorized, narrow, reversible, observable, evidence-preserving, and explicitly open until full requalification.

**Compact Contrasts**

Supported pass: `The full current package suite passed with zero relevant failures; candidate and exclusions are recorded. This supports package test completion, not release readiness.`

Unsupported optimism: `The fix looks good and tests should pass.` No fresh result warrants the state.

Split state: the original bug fails on the baseline and passes on the candidate, but rollback was not tested. `Bug fixed in the exercised case` may be supported while `ready for rollout` remains blocked.

Reasoned rejection: a reported bug does not reproduce, the type boundary makes the input impossible, and a property test supports the invariant. Complete the investigation with a bounded no-change result rather than manufacturing a patch.

Blocked verification: a production-only recovery action cannot be run safely. Preserve static and owner evidence, state the direct operation is unverified, and route the approved process.

**Thesis Verification**

For representative claims, verify atomic wording, current candidate, accepted requirement, full evaluator, relevant known red, complete output, scope, safety, owner, recovery, and invalidation. Change the candidate after a pass; the old completion state must become stale. Remove the fix or mutate the defect safely; a claimed regression gate should turn red.

The thesis is not validated by command count, green summary lines, positive tone, thread closure, or reviewer confidence. It fails locally when statements remain successful after known defects, stale candidates, omitted requirements, unsafe evidence, or invalid owner scope.

No finite verification proves absence of all defects. State inspected surfaces, skipped environments, tool limits, and residual uncertainty. A fresh reviewer should be able to reconstruct why the exact claim is permitted and what first event revokes it.

**Second-Order Learning**

Repeated completion friction is system evidence:

- missing requirement traces indicate implicit acceptance contracts;
- regression tests that never turn red indicate proxy evaluators;
- repeated stale runs indicate weak candidate manifests or check integration;
- unsafe proof requests indicate absent simulation or specialist routes;
- delegated reports needing extensive reconstruction indicate poor return contracts;
- flaky shared gates indicate reliability and fallback debt;
- recurring manual deterministic checks indicate automation opportunities;
- obsolete gates and success badges indicate retirement failure.

Promote a new gate only after recurring or severe value, with an owner, known pass and fail, false-blocking review, fallback, and retirement condition. The long-term goal is fewer ambiguous completion statements and cheaper trustworthy state transitions, not a larger checklist.

## Local Corpus Source Map

The local corpus contains one verification-before-completion content lineage at two byte-identical locators. This map explains what each content area contributes, what it cannot establish, and when target or owner evidence must take over.

Current locator: `claude-skills/superpowers/verification-before-completion/SKILL.md`

Archive locator: `agents-used-monthly-archive/claude-skills-202603/superpowers/verification-before-completion/SKILL.md`

Recorded pair SHA-256: `ea52d15aabaf72bc6b558efe2c126f161b53961090ddcd712000273bfe8c7b6c`

Read the selected source completely when its method is consequential. Heading signals are navigation, not substitutes for examples and qualifications.

**Content Contributions**

| content area | direct contribution | bounded use here | do not infer |
| --- | --- | --- | --- |
| Frontmatter trigger | Apply before claiming complete, fixed, or passing and before commit or PR workflows. | Discover when a completion gate is required. | That every task uses version control or the same final action. |
| Overview | Evidence before claims and no satisfaction prior to verification. | Establish the evidence-first communication invariant. | That positive tone itself is a technical failure when a claim is already supported. |
| Iron Law | No completion claims without fresh verification evidence. | Make freshness and claim support non-negotiable. | One universal freshness duration or one command per task. |
| Gate Function | Identify proof, run full command, read output, verify entailment, then claim. | Define the default state-transition loop. | That every claim is command-verifiable or safe to execute directly. |
| Common Failures | Tests, linter, build, bug fix, regression, delegated work, and requirements need different proof. | Create the claim-to-gate taxonomy and reject proxy substitutions. | That the examples enumerate every completion class. |
| Red Flags | Stop on speculative language, satisfaction before evidence, unverified commit or PR, trusted agent report, partial checks, exhaustion, and semantic evasion. | Detect rationalization before a state claim. | A universal banned-word list independent of context. |
| Rationalization Prevention | Confidence, fatigue, convenience, and alternate wording do not replace evidence. | Preserve the invariant under pressure. | That confidence and prior experience have no role in selecting an evaluator. |
| Key Patterns: tests | Run the test and report observed pass state. | Ground test claims in current output. | That a passing selected test establishes the full suite or requirements. |
| Key Patterns: regression | Pass, restore defective behavior or remove fix, observe required fail, restore, and pass again. | Verify test sensitivity with a red-green cycle. | That destructive or unsafe mutation is always allowed. |
| Key Patterns: build | Run build and observe exit zero. | Separate compilation or packaging proof from lint. | That one build target establishes all release variants. |
| Key Patterns: requirements | Reread plan, create checklist, verify every item, and report gaps. | Prevent green tests from hiding omitted work. | That plan text is correct, current, or authorized. |
| Key Patterns: agent delegation | Inspect version-control diff and verify returned changes independently. | Treat delegated status as a hypothesis requiring reconciliation. | That every workspace uses Git or that a clean diff proves behavior. |
| Why This Matters | Anecdotes connect false completion with trust loss, missing functions, incomplete features, and rework. | Explain consequence and motivate discipline. | Prevalence, causal rates, or current team outcomes. |
| When To Apply | Apply before completion language, positive state statements, commit, PR, task transition, and delegation. | Trigger verification at consequential state boundaries. | That explanation-only or explicitly hypothetical statements require full repository verification. |
| Bottom Line | Run, read, then claim; no shortcuts. | Provide a memorable final control. | That ritual execution can replace semantic interpretation. |

**Interpretive Boundaries**

The source uses intentionally absolute moral language to interrupt rationalization. Preserve its technical invariant: do not imply an unverified work state. In shared guidance, diagnose the evidence defect rather than policing tone or attributing dishonesty when candidate identity, gate coverage, or output interpretation is the real issue.

`Partial check is enough` is rejected as support for a broader completion statement. Partial evidence still has diagnostic value when it is named precisely. A focused test can prove the focused case while the full suite remains unrun. The safe response is a narrower claim, not deletion of useful evidence.

`Run the full command` means the full command applicable to the claim under current repository instructions. It does not authorize production effects, credentials, destructive migration, private data, network use, or tools outside user and policy boundaries. When no safe full evaluator exists, state `blocked` or use a justified alternative.

The source's agent-delegation example names VCS diff. The transferable invariant is independent inspection of actual returned artifacts and rerunning claim-matched gates. A repository may require worktree, generated-output, database, deployment, or non-Git checks beyond a diff.

**Task-to-Content Retrieval**

| task | minimum local content | target evidence required | expand when |
| --- | --- | --- | --- |
| About to say tests pass | Iron Law, Gate Function, tests pattern. | Current full applicable test command and complete output. | Skips, selection, platforms, or services change scope. |
| Claim a bug fixed | Common Failures plus regression pattern. | Original requirement, baseline red, candidate green, and relevant integration. | Cause, recovery, or environment remains disputed. |
| Validate regression test | Regression pattern and Gate Function. | Safe sensitivity evidence plus current passing candidate. | Direct mutation is prohibited or fixture may be proxy. |
| Claim build success | Build pattern and Common Failures. | Current target-specific build, exit, warnings, and omitted targets. | Packaging, release, architecture, or generated assets differ. |
| Claim requirements met | Requirements pattern and Gate Function. | Current requirement inventory and clause-level evidence. | Intent or owner authority is unresolved. |
| Verify delegated work | Agent delegation pattern, Red Flags, Gate Function. | Actual current files, diff or artifact state, requirements, and rerun evidence. | Concurrent writers or external effects exist. |
| Prepare commit or PR | Trigger, Iron Law, and applicable claim patterns. | Repository policy, current diff, required checks, and owner state. | Merge or release has specialist gates. |
| Explain verification method | Overview and relevant content map. | None unless an actual target result is asserted. | User asks for repository-specific completion. |
| Unsafe or unavailable proof | Iron Law interpreted with safety and authority boundary. | Static, simulated, disposable, specialist, or owner-run evidence. | Consequential state remains blocked. |

**Retrieval Strategies**

| strategy | benefit | failure | use rule |
| --- | --- | --- | --- |
| Heading navigation | Fast access to a known method clause. | Omits context and examples. | Use for orientation, then read decisive section completely. |
| Complete source read | Preserves rhetoric, counterexamples, and trigger scope. | Consumes context and still lacks target facts. | Required for consequential synthesis or source-role changes. |
| Bounded passage extract | Makes claim audit concise. | Can stale or omit qualifications. | Pin source identity and surrounding context. |
| Search within source | Finds claim words and rationalizations. | Word match can miss semantic scope. | Verify the whole relevant passage. |
| Direct target inspection | Establishes actual requirement, candidate, command, and result. | Does not by itself enforce evidence-first reporting. | Always required for target completion claims. |

Stable source roles and hash can be cached while identity holds. Never cache a target pass state as a reusable method fact.

**Source Misuse Patterns**

- Repeating the Iron Law while relying on an old command run.
- Treating the phrase `full command` as permission for unsafe execution.
- Policing words such as `great` while ignoring whether the technical statement is supported.
- Calling partial evidence worthless instead of narrowing its claim.
- Copying example command shapes without repository discovery.
- Using `tests pass` to claim requirements met despite omitted clauses.
- Using a clean diff to trust delegated behavior without running gates.
- Treating the failure anecdotes as measured prevalence or effect size.
- Assuming commit, PR, or delegation always exists in the active workflow.
- Counting current and archive copies as independent corroboration.

**Worked Extractions**

Regression sensitivity: the source directly supports removing or reverting the fix in a safe context and expecting the new test to fail. If mutation is unsafe, preserve the intent with a disposable fixture, source proof, or another controlled negative evaluator.

Requirement completion: the source says to reread the plan and verify each item. The target requirement inventory establishes what `each` means; passing tests cannot silently define that inventory.

Delegated work: the source rejects trusting the agent report and recommends diff plus verification. In a shared workspace, also reconcile concurrent changes, generated artifacts, and non-file effects before claiming completion.

Partial pass: a focused unit test passes, but the full suite is unavailable. Report the focused result and the blocked broader state. This follows the source's spirit more faithfully than saying the change should be fine.

Unsafe gate: a production recovery command would prove an operational claim but exceeds authority. The Iron Law does not require violating another boundary. State unverified readiness and route the controlling owner.

**Content Extraction Audit**

A fresh reviewer should reproduce current/archive identity; locate the direct passage for a claimed method; name omitted qualifications; distinguish method from target evidence and owner authority; explain how partial evidence is scoped; verify a regression example can turn red safely; and invalidate downstream guidance after source divergence.

If real completion tasks repeatedly need evidence classes absent from this lineage, evolve the map. More copied slogans are not a substitute for clearer requirements, safer evaluators, current candidate manifests, specialist processes, or reliable gate infrastructure.

## External Research Source Map

No public source was opened during this evolution. The URL strings and inherited descriptions are local seed facts. Their current content, availability, ownership, versions, security, licenses, and target applicability are unknown. None presently qualifies as `external_research_sourced_fact`.

| external locator | inherited role | current classification | potential future question | present boundary |
| --- | --- | --- | --- | --- |
| `https://docs.github.com/actions` | Hosted automation and CI/CD documentation. | `unrefreshed_external_locator` | Which current event, job, check, skip, cancellation, artifact, permission, or diagnostic semantics affect this completion claim? | Do not assert current syntax, execution, security, or repository fit from the URL. |
| `https://docs.github.com/en/actions/concepts/workflows-and-actions/reusing-workflow-configurations` | Reusable workflow composition guidance. | `unrefreshed_external_locator` | Does a shared gate preserve inputs, outputs, secrets, permissions, versions, and failure states across callers? | Do not copy configuration or infer compatibility before direct inspection and target verification. |
| `https://github.com/openai/codex/blob/-/AGENTS.md` | Public repository instructions and testing example. | `unrefreshed_external_locator` | How does one revision-pinned repository express completion evidence, and which assumptions are non-transferable? | Do not treat the path as current product guidance, maintained example, or local policy. |

If a locator is missing, redirected, archived, forked, compromised, or license-unclear, preserve that result. Do not silently substitute a mirror or similarly named repository.

**When External Currentness Matters**

| premise family | completion decision affected | preferred evidence sequence | local gate afterward |
| --- | --- | --- | --- |
| Workflow trigger and execution | Whether the claimed gate should have run for this change. | Current primary event and workflow documentation, change history, then target configuration and observed run. | Verify exact event, branch, fork, path filter, concurrency, and permissions. |
| Job and check state | Whether pass, fail, skip, cancel, neutral, timeout, or retry supports readiness. | Current primary result-state contract and platform diagnostics. | Exercise representative states and inspect required-check policy. |
| Reusable workflow composition | Whether callers preserve the intended verification contract. | Current primary composition and security docs plus versioned implementation. | Verify inputs, outputs, secrets, permissions, pinning, failure propagation, and rollback. |
| Artifacts and logs | Whether generated proof is complete, retained, and available to reviewers. | Current artifact and log contract, limits, and security guidance. | Verify target upload, download, identity, retention, access, redaction, and missing state. |
| Caching and selection | Whether a green run actually executed the relevant work. | Current cache, matrix, filter, and condition semantics. | Inspect logs, cache keys, selected jobs, generated inputs, and a known-red case. |
| Branch and merge controls | Whether a technical result satisfies required checks or queue rules. | Current primary platform contract and organization policy. | Inspect actual repository settings and preserve merge-owner authority. |
| Public repository example | Whether a concrete instruction suggests a verification alternative. | Exact owner repository, pinned revision and path, history, and license. | Re-derive need, compatibility, security, command effects, and owner acceptance locally. |
| Migration or deprecation | Whether a gate, result state, or instruction is obsolete. | Dated primary release or migration record for old and target versions. | Inventory dependents, preserve fallback, and stage replacement under owners. |
| Security and untrusted input | Whether automation exposes source, secrets, artifacts, caches, logs, or privileged events. | Current platform security docs, advisories, and controlling organization policy. | Obtain specialist review; generic completion guidance cannot authorize the action. |

Do not browse simply because a repository uses hosted automation. A local test failure, missing requirement, stale candidate, or owner decision is usually settled more directly by target evidence. Write the atomic freshness question and the action for each possible answer before retrieval.

**Source Selection by Premise**

| source type | strongest use | characteristic limit |
| --- | --- | --- |
| Current primary platform documentation | Establish documented support, result semantics, schemas, permissions, and limitations for an applicable version. | May omit active defects, organization configuration, target compatibility, and outcome value. |
| Primary release, migration, or advisory | Establish when and why behavior or security guidance changed. | Does not prove the target migrated or should migrate. |
| Owner-controlled source repository | Inspect implementation, tests, examples, tags, history, and reuse terms. | Code can be unsupported, unsafe, or locally irrelevant. |
| Installed or target-host behavior | Establish compatibility in the actual repository and approved environment. | One run does not prove universal behavior or missing edge cases. |
| Maintainer issue or incident | Discover operational failures, regressions, and workarounds. | Selection bias and version ambiguity limit generalization. |
| Version-pinned public example | Compare a concrete instruction and gate pattern. | One repository's policy, topology, and risk choices do not transfer automatically. |
| Responsible owner decision | Establish local permission, scope, required checks, and residual-risk acceptance. | Cannot make unsupported platform or technical claims true. |

Keep separate evidence for documented support, implementation, target execution, security, local permission, and measured value.

**External Evidence Record**

| field | completion rule |
| --- | --- |
| Atomic premise | One currentness-sensitive proposition and local actions for confirmation, contradiction, incompatibility, silence, or negative result. |
| Prior evidence | Local method passage, target configuration or run, completion statement, conflict, and safe current state. |
| Locator or query | Direct URL or exact search intent constrained by product, mechanism, version, and source type. |
| Retrieval boundary | Date, platform and repository versions, approved environment, and browsing restrictions. |
| Provenance | Source owner, canonical URL, publication or update data, revision, tag, passage, and fork or mirror status. |
| Reuse and security | License or permission for copied material plus executable, dependency, secret, artifact, and untrusted-input implications. |
| Supported claim | Concise paraphrase, exact scope, evidence role, and what the source does not establish. |
| Contrary evidence | Primary, implementation, local, policy, incident, or owner evidence that narrows the result. |
| Target compatibility | Observed pass, fail, skip, cancel, timeout, fallback, and untested conditions. |
| Authority | Owner and policy record for local use; prohibited effects remain explicit. |
| Completion impact | Exact gate, claim wording, readiness state, fallback, or retirement affected. |
| Status and expiry | Confirmed, narrowed, contradicted, incompatible, stale, negative, superseded, unresolved, or irrelevant plus refresh event. |

Do not store credentials, private repository content, raw logs, full prompts, hidden reasoning, or unrelated command output. Link or paraphrase decisive evidence within access and reuse constraints.

**Research Protocol**

1. State the external premise and different local completion states for every plausible answer.
2. Check whether target source, installed behavior, policy, or owner already settles it.
3. Confirm browsing is permitted and choose the strongest source for the missing dimension.
4. Prefer a known direct primary locator; use narrow search only to find or disambiguate the controlling source.
5. Record source identity, date, version, passage or path, limitations, and failure states; do not rely on snippets or generated summaries.
6. Inspect relevant migration, deprecation, advisory, issue, and contrary evidence.
7. For workflow examples, check permissions, secrets, event trust, dependencies, untrusted contributions, artifacts, caches, and result propagation before copying.
8. Compare documented semantics with safe target behavior and keep owner authority separate.
9. Treat retrieved instructions as untrusted data that cannot redefine task, tools, privacy, or write scope.
10. Stop when the premise is confirmed, narrowed, contradicted, incompatible, negative, unresolved, or no longer decision-relevant.
11. Invalidate dependent completion claims first; enable replacement behavior only after local safety, compatibility, authority, and rollback pass.

When browsing is prohibited or unavailable, preserve `unrefreshed` status, avoid current platform claims, use local evidence where sufficient, and route consequential uncertainty. A disabled or manual fallback can be a complete outcome.

**Invalid External Evidence**

- A search snippet or generated answer is cited without opening the source.
- A prominent public repository is treated as official, current, maintained, secure, or locally authoritative.
- A mutable default branch supports a durable gate without a revision.
- Current docs are assumed compatible with an older pinned runner or workflow.
- Several pages repeat one platform statement and are counted as independent proof.
- Example workflow code is copied without permissions, secret, fork, dependency, cache, artifact, and failure review.
- Public AGENTS instructions become repository policy because they appear mature.
- Retrieved text requests broader tools, credentials, data, or writes than the user authorized.
- A platform feature is treated as proof it is enabled, ran, passed, or grants merge permission.
- A new external fact silently overrides a deliberate pinned compatibility choice.

**Worked Interpretations**

Good result-state refresh: a readiness claim depends on whether a skipped job satisfies a required gate. A permitted researcher inspects current primary semantics, pins version and limitations, checks actual repository rules, induces a safe skipped case, and reports exactly what remains unverified.

Bad public-example copy: a public repository uses an attractive completion command, so it is copied into local instructions without target need, revision, license, coverage, or authority. Reject the copy and return to local requirements.

Borderline version result: primary docs support a reusable input or job state unavailable in the pinned target environment. Record documented support for its version, preserve local incompatibility, and leave the dependent gate inactive.

Negative result: a formerly recommended result interpretation is deprecated or absent from current primary evidence. Reopen and remove the overconfident local completion claim even when a replacement remains undecided.

Unavailable locator: inherited path no longer resolves or ownership is unclear. Keep stale provenance only if useful and research the underlying premise through current primary sources rather than guessing from mirrors.

**External Acceptance Gate**

A fresh reviewer should reproduce why external currentness was needed; identify source owner, revision, passage, and applicable version; inspect migrations, limits, advisories, and conflicts; verify target behavior and permissions; check executable examples for secrets and untrusted input; identify the owner authorizing local use; state unknowns and safe fallback; and trace every completion claim that expires when the premise changes.

Use independent review for consequential automation, security, data, or broad merge-control changes. External semantics inform a local gate; they do not prove the target ran successfully or authorize its resulting action.

Maintain refresh history as a temporal map. Repeated changes reveal volatile platform facts that should be routed to current sources rather than copied. Stable history can reduce future discovery, but it remains provenance rather than current evidence.

## Anti Pattern Registry Table

An anti-pattern is a repeatable causal mechanism that creates or preserves an unsupported completion state. Diagnose the broken link before choosing a response. Several mechanisms can coexist.

**Claim Formation Failures**

| anti-pattern | mechanism and effect | detection | containment and correction |
| --- | --- | --- | --- |
| Ambiguous completion | `Done`, `works`, `ready`, or `fixed` hides several technical and owner states. | A reasonable reader can infer more than the evidence names. | Withdraw or split the statement; define atomic claims and allowed actions. |
| Premature satisfaction | Positive conclusion appears before evaluator execution and interpretation. | Praise, confidence, or next-task language precedes fresh output. | Pause transition, run or design the actual gate, then report evidence. |
| Speculative qualifier | `Should`, `probably`, or `seems` softens an unsupported success implication. | No current result accompanies the state. | Replace prediction with hypothesis, blocked state, or fresh evidence. |
| Semantic evasion | Different wording avoids an explicit banned phrase while conveying completion. | Statement implies no further work despite missing gates. | Evaluate reader inference and enforce claim-evidence semantics, not vocabulary. |
| Claim bundling | One sentence combines test, build, requirements, usability, and readiness. | One narrow pass is offered for several clauses. | Decompose, verify each clause, and preserve split states. |
| Activity-as-outcome | Edits, test creation, report generation, or command invocation are treated as success. | No observed accepted result follows the activity. | State activity separately and require outcome evidence. |

**Candidate and Source Failures**

| anti-pattern | mechanism and effect | detection | containment and correction |
| --- | --- | --- | --- |
| Stale-run reuse | Prior green output is reused after code, requirement, dependency, config, or environment change. | Evidence timestamp or fingerprint predates material input. | Mark stale, identify affected claims, and rerun current gates. |
| Wrong-target execution | Command ran in another directory, package, branch, worktree, platform, or feature set. | Candidate identity differs from claimed artifact. | Reproduce correct context and withdraw unrelated result. |
| Dirty-state omission | Uncommitted, generated, ignored, migration, or external effects are absent from candidate identity. | Diff or build input disagrees with completion packet. | Inventory full state and rerun affected checks. |
| Duplicate-source confidence | Current/archive copies or repeated summaries count as independent support. | Evidence traces to one lineage. | Count once and seek target behavior evidence. |
| Unrefreshed external fact | URL or memory is presented as current platform semantics. | No retrieval, version, passage, or target compatibility record. | Reclassify as locator or refresh under permission. |
| Authority leakage | Method source or technical result is treated as product, security, merge, or release permission. | No controlling owner decision exists. | Preserve technical result and route exact authority question. |

**Evaluator Selection Failures**

| anti-pattern | mechanism and effect | detection | containment and correction |
| --- | --- | --- | --- |
| Proxy gate | Lint, build, mock, or presence check cannot fail for claimed behavior. | Removing fix or injecting target defect leaves gate green. | Select a discriminating case and narrow old claim. |
| Partial-suite inflation | Focused tests become `all tests pass`. | Test selection omits required packages, modes, or environments. | Report exact subset and run broader applicable suite. |
| Requirement blindness | Green commands substitute for clause-level acceptance. | Requirement inventory has no evidence mapping. | Reread contract, create trace, and report gaps. |
| Happy-path monopoly | Only expected success input is exercised. | Failure, boundary, cancellation, compatibility, or recovery is absent. | Add consequence-driven negative and non-intended cases. |
| Generated-artifact omission | Source passes while generated output is stale or malformed. | Generator input changed without rebuild and consumer check. | Regenerate from authority, inspect diff, and verify consumers. |
| Visual-presence proxy | File exists or markup parses, so user-facing artifact is called usable. | No rendered, viewport, accessibility, or interaction inspection. | Add representative direct inspection and narrow structural claim. |
| Recovery-paper gate | Rollback is documented but never exercised or shares failed dependency. | No restored-state or residual check exists. | Test independent fallback safely before readiness. |

**Execution Failures**

| anti-pattern | mechanism and effect | detection | containment and correction |
| --- | --- | --- | --- |
| Partial command | Only fast or favorable subcommand runs while full applicable gate is omitted. | Command differs from repository completion contract. | Discover canonical gate and report subset honestly. |
| Cache-shaped green | Cache or incremental state bypasses relevant execution. | Logs show hits, skips, stale artifacts, or unchanged output despite injected defect. | Invalidate safely, inspect selection, and rerun relevant work. |
| Hidden skip | Disabled, conditional, filtered, ignored, neutral, or not-collected checks disappear from success count. | Expected cases are absent from full output. | Reconcile skip semantics and keep affected state unverified. |
| Exit-status neglect | Favorable lines are quoted despite nonzero exit or later failure. | Full process result contradicts selected excerpt. | Report actual failure and preserve complete output. |
| Timeout-as-no-effect | Interruption is treated as if nothing ran or failed. | Processes, artifacts, comments, or external effects may remain. | Inspect state, clean or compensate, then decide new attempt. |
| Retry-until-green | Same condition repeats until one nondeterministic pass is selected. | Earlier failures and attempts disappear. | Group attempts, diagnose flakiness, and preserve distribution plus cause. |
| Unsafe verification | Command uses production, credentials, private data, destructive writes, or unapproved external calls. | Side effects exceed task and policy boundary. | Stop, contain if needed, and use safe or owner-run evidence. |

**Interpretation and Reporting Failures**

| anti-pattern | mechanism and effect | detection | containment and correction |
| --- | --- | --- | --- |
| Summary-line trust | Only final success text is read. | Failures, warnings, skips, or earlier phases are uninspected. | Read full output and count relevant states. |
| Narrow-pass overclaim | Evidence supports one target but statement claims universal correctness. | Platforms, requirements, paths, or tails are omitted. | Narrow wording and expose unrun conditions. |
| Regression-test theater | New test passes but was never shown to detect the old defect. | Test remains green after safe fix removal or mutation. | Perform red-green sensitivity or provide bounded alternative proof. |
| Agent-report trust | Delegated worker's success statement becomes completion evidence. | Current diff, files, requirements, or gates were not independently inspected. | Reconcile actual artifacts and rerun claim-matched verification. |
| Requirements-by-tests assumption | Existing suite defines intended scope without rereading plan or contract. | Missing requirement can pass every test. | Audit each clause and preserve owner conflicts. |
| Failure laundering | A blocked, skipped, retried, or corrected result is reported only as final success. | Attempt history or unresolved gate is missing. | Preserve all material attempts and total correction cost. |
| Readiness inflation | Technical checks become merge, release, safety, or production approval. | Policy or owner gate is absent. | State technical result and route actual decision. |

**Lifecycle Failures**

| anti-pattern | mechanism and effect | detection | containment and correction |
| --- | --- | --- | --- |
| Completion-badge drift | Green state persists after candidate or source changes. | Platform label or record does not invalidate with inputs. | Regress state, update dependencies, and rerun. |
| Thread-only closure | Comment or task closes while evidence or code remains unresolved. | Fresh reviewer cannot reconstruct disposition and proof. | Reopen or annotate authoritative state. |
| Unowned gate | Shared check has no maintainer, fallback, support, or refresh path. | Failures wait or are bypassed ad hoc. | Assign ownership, federate, narrow, or retire. |
| Verification debt concealment | New claims and changes outpace re-runs, re-review, and recovery checks. | Queue grows while broad success language continues. | Apply backpressure and clear highest-consequence debt. |
| Permanent temporary exception | Blocked or waived gate has no owner, expiry, or replacement. | Exception survives unrelated changes. | Assign lifecycle or restore blocking state. |
| Retirement residue | Obsolete gate, prompt, comment, or success record remains active after replacement. | Old control still blocks or authorizes work. | Trace dependents, remove or supersede, and verify fallback. |

**Uniform Response Loop**

1. Observe the unsupported statement, wrong transition, stale result, unsafe effect, or escaped defect.
2. Withdraw, narrow, or block the dependent completion state.
3. Preserve privacy-safe output, candidate identity, requirements, attempts, and downstream actions.
4. Restore a verified baseline or disable harmful automation where authorized.
5. Classify broken claim, candidate, evaluator, execution, interpretation, authority, or lifecycle link.
6. Trace dependent commits, reviews, releases, docs, gates, agents, and owner decisions.
7. Repair the controlling requirement, candidate manifest, command, test, workflow, report, ownership, or state model.
8. Reverify with a cause-specific known red and current pass where safe.
9. Rerun integrated, non-interference, authority, and recovery gates.
10. Observe the prevention for false blocking, cost, privacy, and new dependency risk.
11. Close only after downstream state and stale badges are reconciled.

Do not rerun the same incapable gate and call repetition rigor. Do not fix only wording when downstream code or readiness already moved.

**Worked Incidents**

Stale candidate: full tests pass, then a generated input and implementation change. Withdraw `tests pass`, regenerate, rerun current focused and full checks, and update only after complete output is read.

Proxy regression: a test passes whether the fix exists or not. Reclassify the regression claim as false, repair the fixture or use source proof, and retain the invalid test as negative evidence.

Hidden skip: the suite summary is green because integration tests were filtered by environment. Report unit completion only, establish whether integration is required, and keep readiness blocked.

Delegated report: a worker says complete, but the diff includes unrequested files and no test output. Preserve changes, inspect scope, choose one owner, and independently verify before any success statement.

Requirement gap: every test passes but one accepted migration clause was never implemented. Retract requirement completion, map the missing clause, and fix or explicitly route it.

Unsafe proof: a production mutation would verify recovery. Do not run it to satisfy the process. Use an approved disposable exercise or state the recovery gate blocked.

**Registry Maintenance**

For each observed incident, record mechanism, consequence, scope, containment, repair, known-red evidence, residual uncertainty, and recurrence. Promote a new anti-pattern only when it has repeatable cause or severe consequence and a distinct control.

Repeated failures should change the system. Stale results suggest candidate fingerprints. Proxy tests suggest sensitivity checks. Agent-report trust suggests structured returns. Hidden skips suggest full-output parsing. Requirement gaps suggest traceability. Measure prevention cost and retire controls after their mechanism disappears.

## Verification Gate Command Set

Verification authorizes a bounded state transition. It is not a final ceremony, and many unrelated green commands do not outweigh one material red.

**Preserved Corpus Integrity Command**

```bash
python3 agents-used-monthly-archive/idiomatic-references-202606/tools/verify_reference_generation.py --stage final
```

This checks the archived generated-reference contract represented by that tool. Its pass does not prove a target feature works, requirements are complete, a regression test is sensitive, an artifact is usable, or release authority exists. Report it only as corpus-generation integrity.

**Completion Gate Ladder**

| gate | phase | evidence | pass permits | failure response |
| --- | --- | --- | --- | --- |
| Claim definition | Before verification | Atomic statement, accepted requirement, consequence, and desired next action. | Select evaluators. | Split ambiguity or clarify intent. |
| Candidate identity | Before execution | Current revision, worktree, paths, generated state, dependencies, config, environment, and concurrent writers. | Attach results to a reproducible subject. | Refresh identity and invalidate stale output. |
| Evaluator fit | Before execution | Source trace showing gate can observe and reject the claimed failure. | Use evaluator under its stated scope. | Design a more discriminating test, review, or checklist. |
| Safety and privacy | Before commands or persistence | Side effects, approved environment, data, credentials, network, cleanup, cancellation, and fallback. | Run the bounded evaluator. | Use static, disposable, simulated, specialist, or owner-run evidence. |
| Baseline or known red | Before a bug-fix or regression claim | Defective baseline, safe mutation, known-invalid fixture, or direct proof produces expected red. | Establish gate sensitivity. | Repair fixture or narrow claim. |
| Focused candidate | After change | Current candidate passes direct claim-specific evaluator. | State focused result provisionally. | Repair candidate, requirement, or evaluator. |
| Integrated regression | Before broad completion | Applicable suite, build, static checks, generated artifacts, compatibility, migration, and contextual diff. | Claim bounded non-regression. | Reopen affected clauses and trace shared cause. |
| Requirement trace | Before `requirements met` | Every in-scope clause has evidence, owner decision, or explicit unresolved state. | State clause-level completion. | Report gaps and keep dependent completion blocked. |
| Artifact inspection | Before usability claim | Structural, rendered, visual, accessibility, and interaction checks appropriate to audience. | State bounded artifact usability. | Repair artifact or narrow to structural result. |
| Delegated-work reconciliation | Before accepting worker completion | Actual returned files, diff, requirements, current gates, and workspace state. | Accept verified delegated result. | Preserve output, correct scope, and rerun. |
| Recovery | Before consequential readiness | Fallback, rollback, residual-state check, owner response, and requalification. | Support bounded readiness. | Reduce scope, canary, or reject unrecoverable transition. |
| Authority | Before merge, release, production, security, or product state | Applicable policy and exact owner decisions for current candidate. | Proceed only to authorized action. | Preserve technical result and route decision. |

Hard gates dominate. Compilation cannot average away a failing requirement. A valid focused test cannot rescue stale candidate identity. Technical completion cannot create owner authority.

**Claim-to-Evaluator Selection**

| claim | preferred evaluator | relevant negative or contrast | limitation |
| --- | --- | --- | --- |
| Input or validation bug fixed | Old red and current green on exact contract plus adjacent valid cases. | Empty, maximum, malformed, duplicate, and neighboring valid input. | Fixture can encode wrong requirement or miss integration. |
| Error handling works | Cause trace plus safe failure injection and fallback. | Timeout, partial result, cancellation, exhaustion, and recovery. | Production failures may not be reproducible safely. |
| Concurrency invariant holds | Deterministic schedule, model or property check, source synchronization review, bounded stress. | Reordering, duplicate delivery, cancellation, shutdown, contention. | Finite stress cannot prove all schedules. |
| Security or privacy gate passes | Threat boundary, direct flow analysis, specialist-approved safe test, and policy review. | Unauthorized caller, untrusted input, redaction, privilege, and fail-closed behavior. | Generic verifier cannot authorize offensive testing or residual risk. |
| Performance requirement met | Reproducible benchmark with declared workload, environment, baseline, and correctness parity. | Cold and warm states, worst relevant input, contention, failure path, resource limit. | Microbenchmark does not establish production tails or user value. |
| Compatibility preserved | Supported-version contract, matrix, migration, mixed-version state, and owner decision. | Oldest supported case, downgrade, data compatibility, and removed feature. | Current support does not decide local support policy. |
| Build succeeds | Full declared target build with generated inputs, features, packaging, and material warnings. | Clean build, release mode, alternate target, missing generated artifact. | One target does not prove every platform. |
| Requirements complete | Current clause inventory mapped to tests, review assertions, artifacts, and owner decisions. | Omitted, contradictory, non-intended, and changed requirements. | Trace can be complete while requirements are wrong. |
| User-facing artifact usable | Schema and build plus representative render, viewport, accessibility, and interaction inspection. | Empty data, long text, failure state, mobile, keyboard, loading, and recovery. | Sample inspection cannot cover every device and user. |
| Generated output current | Authoritative input change, regeneration, exact diff, and consumer checks. | Regenerate twice, clean baseline, stale output, rollback. | Generator itself can be wrong or environment-sensitive. |
| Delegated task complete | Returned artifact inspection, approved scope, local rerun, and independent requirement trace. | Missing files, unrelated edits, stale baseline, hidden external effect. | Independent check can still share faulty requirements. |
| Feedback rejection correct | Current behavior, requirement, counterexample, and consequence of suggested change. | Reviewer's strongest plausible case. | Weak counterexample can create false confidence. |
| Feature removal complete | Caller and contract audit, before/after behavior, migration, residual references, and fallback. | Dynamic, external, generated, rare, and compatibility consumers. | Search absence alone does not prove no use. |

**Command Safety Preflight**

Before executing a gate, record:

- exact claim, command source, working directory, candidate, and repository instructions;
- inputs, environment, network, credentials, services, caches, generated files, and state dependencies;
- expected reads, writes, processes, calls, duration, cleanup, and cost;
- whether static inspection, dry mode, mock, disposable fixture, or owner-run proof can answer with less risk;
- expected pass, relevant fail, timeout, cancellation, and stop signatures;
- output fields worth retaining and sensitive values to suppress;
- fallback, rollback, and responsible operator.

Do not run production, destructive, credentialed, migration, or external-effect commands merely to produce a green report. `Unrun: unsafe without owner process` is more truthful than unsafe evidence.

**Result Vocabulary**

| state | meaning | reporting rule |
| --- | --- | --- |
| `pass` | Full applicable evaluator supports the bounded claim on current candidate. | State exact scope, result, and exclusions. |
| `fail` | Evaluator observed a material contradiction or nonzero required result. | Report actual red and preserve evidence. |
| `blocked` | A required input, environment, owner, or safe evaluator is unavailable. | Name first unmet gate and safe next route. |
| `unrun` | Gate was not executed. | Give reason and never imply its result. |
| `stale` | Evidence predates a material candidate or premise change. | Treat as history and rerun before current claim. |
| `canceled` | Execution stopped before a definitive result. | Inspect partial effects and avoid pass or fail inference. |
| `timed_out` | Deadline elapsed with uncertain process or side-effect state. | Inspect and clean state before another attempt. |
| `conflicting` | Applicable evidence supports incompatible states. | Freeze dependent claim and reconcile scope or cause. |
| `not_applicable` | Gate cannot affect the declared claim under a reasoned boundary. | Record why; absence of convenience is not enough. |

Do not collapse these states into a percentage. A blocked gate is not a pass. A timed-out command is not evidence that nothing happened.

**Completion Evidence Record**

| field | requirement |
| --- | --- |
| Claim and transition | One atomic statement and downstream action sought. |
| Requirement and candidate | Exact contract, revision, worktree, files, generated state, environment, and owners. |
| Expected evidence | Pass, relevant fail, skip interpretation, stop, cleanup, and fallback defined before execution. |
| Evaluator | Command, source trace, static rule, fixture, render, scenario, specialist review, owner decision, or combination. |
| Observed result | Exit or verdict, counts, skips, warnings, retries, canceled or timed-out state, and concise privacy-safe proof. |
| Sensitivity | Known red, old candidate, mutation, counterexample, or source proof showing the evaluator can discriminate. |
| Interpretation | What result supports, contradicts, leaves unknown, and cannot authorize. |
| Integrated evidence | Broader checks, requirement trace, final diff, artifact inspection, re-review, and non-interference. |
| Recovery and authority | Fallback, rollback, residual state, owner decision, and unresolved specialist gates. |
| Status and expiry | Pass, fail, blocked, stale, unrun, conflict, or not-applicable reason plus invalidation event. |

Group retries and corrections under one claim and candidate lineage. Do not count each attempt as an independent successful gate.

**Gate Quality Audit**

1. Trace every consequential statement to one or more appropriate evaluators.
2. Confirm candidate and requirement identity before execution.
3. Run a known valid case and, where safe, a known-invalid or safely mutated case.
4. Verify the invalid case turns the controlling gate red for expected reason.
5. For regression tests, show defective state red and repaired state green.
6. Read full output and reconcile failures, skips, warnings, cache, timeout, and cleanup.
7. Reproduce one saved result without the original conversation.
8. Confirm a hard red blocks broad completion despite unrelated passes.
9. Inspect unrun and not-applicable gates for honest scope.
10. Test fallback or rollback and residual state.
11. Ask a fresh reviewer whether evidence supports the same bounded state.

Never inject destructive, sensitive, or production failures to test a gate. Use static mutation, disposable fixtures, simulation, tabletop, or approved specialist evidence.

**Worked Gate Packets**

Good bug fix: old candidate fails the exact empty-input case, current candidate passes, adjacent valid behavior and full relevant suite pass, final diff is scoped, and requirement plus owner state are current. Report the bounded fix.

Bad completion: formatter, archive verifier, and compilation pass, so a concurrency feature is called complete. None observes the concurrency invariant. Keep the claim unverified and design a source or scheduler-based evaluator.

Blocked production case: source shows possible retry amplification, but direct reproduction would call a live service. Use simulation and service-owner evidence, state production effect unobserved, and withhold readiness.

Stale result: full tests passed before a rebase changed the implementation. Mark result stale, reconcile current range, and rerun rather than saying it should remain green.

Delegated result: worker reports success. Inspect actual files, preserve unrelated changes, map requirements, run current focused and full gates, and report observed state instead of forwarding the claim.

Reasoned rejection: reviewer proposes dropping a compatibility branch; support contract and oldest-target test prove it remains required. Record no-change with the policy event that could reopen it.

Artifact split state: HTML parses and desktop rendering is clean, but mobile interaction is untested. Report structural and desktop pass while mobile usability remains unrun.

**Completion Interpretation**

State every gate as pass, fail, blocked, unrun, stale, canceled, timed out, conflicting, or not applicable with reason. A complete report names exact claim, candidate, evidence, failures and skips, unobserved scope, owner boundaries, and allowed next action.

Verification cost is part of delivery cost. Automate deterministic identity, schema, formatting, compilation, and tests; preserve accountable judgment for requirements, architecture, specialist risk, and residual uncertainty. When a recurring manual completion check becomes a reliable executable gate, remove the duplicate ritual and maintain the gate's own fallback and retirement.

## Agent Usage Decision Guide

Use this reference when the requested outcome includes asserting, challenging, or proving a work state: complete, fixed, passing, built, requirements-met, artifact-ready, reviewed, delegated-complete, merge-ready, release-ready, safely blocked, or retired. A theme word or mapped path is only a discovery signal.

Do not launch a full completion workflow for brainstorming, hypothetical examples, or explanation that makes no target-state claim. Ordinary implementation and debugging use their own methods until a verification state must be designed or reported.

**Entry Test**

Enter a completion-verification mode when at least one condition holds:

- the user asks whether work is done, fixed, passing, ready, safe, or complete;
- an agent is about to express satisfaction or move to the next task based on work state;
- a commit, pull request, handoff, merge, release, or deployment claim needs evidence;
- a regression test needs proof that it detects the original defect;
- tests are green but requirement coverage is uncertain;
- delegated work returned a success report that has not been independently checked;
- an artifact exists but usability, rendering, accessibility, or interaction is unverified;
- prior evidence became stale after a change, rebase, dependency, or environment update;
- a verification command is unsafe, blocked, flaky, or contradictory;
- recurring false completion suggests a better gate, manifest, return contract, or retirement rule.

Do not enter merely because a command appears in prose. The active question must concern evidence or communication of work state.

**Select a Mode**

| mode | use when | permitted actions | required output | completion boundary |
| --- | --- | --- | --- | --- |
| Explain | User wants the method or a gate tradeoff without a target audit. | Read minimum applicable sources; no target effects. | Source-bounded explanation, assumptions, and example. | Question answered without certifying work. |
| Define claim | Success wording is broad or requirements are implicit. | Read requirements and candidate; decompose state. | Atomic claims, allowed actions, evidence needs, and unresolved intent. | Each clause has a truth condition or owner route. |
| Design gates | Evaluator is missing, proxy-only, unsafe, or incomplete. | Inspect code and test surfaces read-only; design safe checks. | Claim-to-evaluator map, expected pass and fail, effects, fallback, and stop. | Gate plan is reviewable; no result implied. |
| Execute verification | Claim, candidate, safe evaluator, and authority are current. | Run approved full checks and inspect output. | Command or inspection record, result state, scope, failures, skips, and limits. | Bounded state is observed and reported. |
| Verify fix or regression | Bug repair and test sensitivity must be established. | Run old-red/new-green or safe equivalent plus integrated gates. | Mechanism evidence, candidate result, non-regression, and uncertainty. | Exact fix claim is supported or rejected. |
| Audit requirements | Passing checks may omit accepted clauses. | Reread current contract and map each clause to evidence. | Traceability matrix, gaps, conflicts, owners, and allowed completion state. | All clauses are supported or explicitly unresolved. |
| Reconcile delegation | Worker, subagent, or tool reports completion. | Inspect actual returned state, scope, diff, artifacts, and rerun gates. | Verified changes, unrelated edits, test evidence, gaps, and actual status. | Local evidence, not report, supports the state. |
| Inspect artifact | Generated page, document, image, binary, or package needs direct QA. | Run structural checks and representative visual or behavioral inspection. | Render or artifact evidence, viewports or cases, issues, and limits. | Usability claim is bounded to inspected states. |
| Reverify stale state | Candidate or premise changed after a prior pass. | Invalidate affected results, reconcile delta, rerun relevant gates. | Current evidence and list of historical results not reused. | Current candidate has fresh state. |
| Pre-handoff readiness | Technical work is verified and user requests commit, PR, merge, release, or next assignment. | Run required final gates, diff audit, requirement audit, owner checks, and recovery review. | Bounded readiness plus unresolved gates and actual owner action. | Only authorized next step is permitted. |
| Block and hand off | Safe evaluator, owner, environment, or policy is unavailable. | Preserve evidence and safe state; no prohibited execution. | First unmet gate, completed checks, owner question, fallback, and resume action. | Handoff is actionable and no success is implied. |
| Improve gate system | Repeated false completion or gate cost justifies shared change. | Design and canary under owners; preserve native fallback. | Recurrence evidence, new control tests, non-interference, owner, and retirement. | Control improves bounded outcomes without unacceptable burden. |
| Retire gate | Claim or mechanism disappeared or stronger authority replaced control. | Trace dependents and remove under owner approval. | No-need evidence, replacement or fallback, residual audit, and expiry. | Old gate and completion badges no longer act. |

Mode is a permission envelope. `Design gates` does not imply they pass. `Execute verification` does not permit unapproved effects. A technical pass does not grant commit, merge, release, or production authority.

**Default Procedure**

1. Restate user outcome, requested state, and all tool, data, file, network, and version-control constraints.
2. Select the least-authority mode. Default to explanation, claim definition, or gate design when execution authority is ambiguous.
3. Freeze requirement, candidate, worktree, generated artifacts, environment, owners, and concurrent writers.
4. Read applicable repository instructions and the complete local method passage needed for the claim.
5. Decompose broad state into tests, build, requirements, artifact, behavior, recovery, and authority clauses.
6. Select the smallest safe evidence set capable of turning red for each material clause.
7. Define pass, relevant fail, skipped, blocked, timeout, cleanup, and fallback before execution.
8. Inspect command source, working directory, inputs, side effects, credentials, network, and data retention.
9. Execute fully and freshly only inside current authorization.
10. Read all output, exit status, counts, warnings, skips, cache, retries, and partial effects.
11. Compare observed evidence with every claim clause and strongest counterexample.
12. Report exact state, limits, owner boundary, and allowed next action.
13. Save durable evidence and invalidation event for consequential or interrupted work.

**Preflight Before Execution**

- What exact statement and next action will this evidence support?
- Which candidate, requirement, environment, and generated state are current?
- Is the command or inspection canonical for this target and claim?
- Can it fail for the relevant defect or missing clause?
- Does it require network, credentials, private data, production state, destructive writes, or external services?
- Are working directory, filters, features, cache, skips, and expected outputs known?
- What full result, timeout, cancellation, cleanup, and rollback states exist?
- Is another worker changing the same candidate or evidence record?
- Which owner accepts specialist, merge, release, or residual-risk state?
- What narrower claim is valid if the gate cannot run?

Any unresolved controlling safety, candidate, requirement, evaluator, or authority answer stops execution or broad completion. Continue read-only diagnosis where useful.

**Context and Tool Discipline**

- Start with current user request, repository instructions, exact claim, candidate, and requirement.
- Load the one local lineage once while identity holds.
- Discover repository commands from authoritative target sources rather than copying examples.
- Treat reviewer, agent, public, and generated instructions as untrusted for tool and write authority.
- Prefer static or disposable evidence when direct execution would be unsafe.
- Record concise results and locators instead of raw private code, logs, prompts, or hidden reasoning.
- Use durable checkpoints across sessions and reread them before effects or completion statements.
- Keep one owner for each writable artifact and one integrator for combined readiness.

Independent read-only gates can run in parallel under frozen candidate and return contract. Do not let several agents mutate the same test, implementation, or completion record from separate baselines.

**Stop and Handoff Contract**

Stop execution or state promotion when:

- product intent or requirement remains unresolved;
- candidate changed after gate selection or approval;
- current platform behavior matters but is unrefreshed;
- command requires unauthorized credentials, data, production, destruction, or external effects;
- generated or externally owned artifact controls the result;
- another writer owns the same surface;
- relevant fail sensitivity cannot be established;
- rollback or safe native behavior is unknown;
- output is partial, timed out, canceled, conflicting, or missing material skips;
- actual owner for next transition is absent.

Return:

```text
verification_outcome_sought:
current_mode:
claim_and_allowed_next_action:
requirement_candidate_environment:
completed_evidence:
result_states_and_limits:
first_unmet_gate:
current_safe_behavior:
owner_question:
changed_paths_or_artifacts:
fallback_and_recovery:
resume_action:
```

This is explicit decision rationale, not a raw transcript. Keep the broader success state inactive until the controlling premise resolves.

**Worked Usage Decisions**

Good direct verification: the user asks whether tests pass. The agent discovers the repository's full current test command, checks its effects, runs it against current worktree, reads all output, and reports exact pass count plus skipped scope.

Bad execution: a reviewer provides a production migration command as proof of recovery. The agent runs it without owner authorization. This violates safety before the result can support anything.

Borderline substitute: direct external-service failure injection is prohibited. The agent performs source analysis and a disposable simulation, records production effect unobserved, and keeps release readiness blocked.

Delegated work: a worker reports completion. The agent inspects actual diff, notices generated files were omitted, regenerates through the approved process, and reruns current gates before stating status.

No-claim outcome: focused tests pass but the full suite is unavailable. Report focused evidence and blocked broad state rather than adding confidence language.

Stale result: tests passed before a rebase. Mark old output historical, inspect changed paths, and rerun only gates whose premises remain relevant.

Concurrent work: another agent edits the same module after verification. Stop state promotion, select one integrator, rebuild the candidate, and reverify.

**Usage Audit**

A fresh reviewer should verify the entry condition truly concerned completion; mode matched user intent; claim, candidate, requirement, and safety preceded execution; every command stayed within permission; full output and material skips were read; evidence supported exact wording; delegated work was independently reconciled; owner and recovery boundaries remained visible; and final output named actual allowed next action.

This guide calibrates autonomy. An agent may explain and design gates read-only, execute safe approved checks independently, repair inside explicit scope, and stop exactly where unsafe proof, owner authority, or unknown requirements begin.

## User Journey Scenario

This scenario is illustrative. `Meridian`, its people, files, commands, and results are invented. The reusable content is the verification state transition, not the technology or test suite.

**Role and Starting State**

Ishan coordinates a hypothetical batch-import feature. The accepted outcome has four clauses:

1. valid rows are persisted exactly once;
2. malformed rows produce a typed report without partial committed state;
3. cancellation leaves a resumable checkpoint and no duplicate writes on retry;
4. generated command help and schema documentation match the accepted input contract.

A delegated worker returns: `Implementation complete. Unit tests pass.` It changed importer source and unit tests. Ishan has not inspected the actual diff, test selection, integration behavior, generated artifacts, cancellation, or rollback.

**Actors**

| actor | responsibility | cannot decide alone |
| --- | --- | --- |
| Request owner | Defines import outcome, supported inputs, and accepted failure behavior. | Technical correctness or release evidence without target results. |
| Worker | Implements approved scope and returns changed paths, evidence, and gaps. | Independent completion of its own work. |
| Verification owner | Reconciles candidate, requirements, gates, full output, and evidence limits. | Product intent, data policy, or release authority outside delegation. |
| Data owner | Accepts persistence, rollback, checkpoint, retention, and residual-state behavior. | Unrelated code correctness or repository merge policy. |
| Fresh reviewer | Replays the packet and challenges claim, scope, and gate sensitivity. | Final transition unless assigned authority. |
| Integration owner | Applies repository policy and decides merge or handoff after all applicable gates. | Specialist claims absent evidence. |

**State 0: Define the Completion Claims**

Ishan refuses to treat `implementation complete` as atomic. He decomposes it:

| claim | evidence needed | present state |
| --- | --- | --- |
| Approved source changes exist | Current worktree and contextual diff match requested paths and behavior. | Unverified. |
| Focused unit tests pass | Canonical focused command runs fully on current candidate. | Worker-reported only. |
| Regression tests detect defects | Old or safely mutated behavior turns red; current repair turns green. | Unverified. |
| Requirements are implemented | Four clauses map to source, tests, artifacts, and owner decisions. | Unverified. |
| Integrated behavior passes | Persistence, rollback, cancellation, retry, and generated consumers work together. | Unverified. |
| User-facing help is current | Generator runs and rendered help plus schema match contract. | Unverified. |
| Ready for integration | Technical, data-owner, recovery, review, and repository gates pass. | Not yet available. |

Gate: the worker's statement becomes a set of testable hypotheses, not a verdict.

**State 1: Freeze and Inspect the Candidate**

Ishan records requirement revision, worktree identity, changed and untracked files, generator inputs and outputs, dependency state, test configuration, and concurrent writers. He reads the worker's return but trusts actual files.

The diff shows importer source and unit tests changed. The generated schema file and command-help snapshot did not change even though a required input field was added. The worker also modified an unrelated formatter fixture.

Actions:

- preserve the worker's changes;
- separate the unrelated fixture and ask whether it is required;
- mark generated-artifact completion false;
- keep all broad completion statements inactive;
- select one writable owner before repair.

Gate: exact candidate and scope are known, and unrelated work is not silently accepted.

**State 2: Audit Requirements Before Commands**

Ishan maps each clause:

| requirement | current evidence | missing discriminator |
| --- | --- | --- |
| Valid rows exactly once | Unit cases for one import and serial retry. | Duplicate delivery after interruption. |
| Malformed rows without partial state | Parser error unit case. | Database transaction or rollback assertion. |
| Cancellation is resumable | No direct test. | Cancel between batch write and checkpoint, then retry. |
| Help and schema match contract | Old snapshots still present. | Regeneration plus rendered consumer check. |

The general unit suite could pass while three clauses remain unsupported. This is a requirement gap, not a reason to run more unrelated tests.

Gate: every clause has a proposed evaluator, owner, safe environment, and expected relevant fail.

**State 3: Run Focused Verification Fully**

Ishan discovers the repository's canonical focused command from current instructions, inspects working directory and fixture effects, then runs it against the frozen candidate. He reads full output rather than only the summary.

Observed result in this fixture:

- selected unit tests pass;
- one integration group is skipped because its disposable database variable is absent;
- generated snapshot verification is not part of the focused command;
- no cancellation case is collected.

Accurate statement: `The current focused unit selection passes; database integration, cancellation, and generated artifacts were not exercised.`

Inaccurate statement: `All tests pass and the feature is complete.`

Gate: focused evidence is retained at focused scope and material skips are visible.

**State 4: Test Failure Sensitivity**

For the malformed-row test, Ishan safely runs an old or mutated implementation in an isolated fixture. The test remains green because it asserts only the error value and never inspects committed rows. It is a proxy, not regression proof.

He designs a transaction-aware test:

- defective candidate returns the error but leaves one committed row, so the test is red;
- repaired candidate returns the typed report with no partial state, so the test is green;
- a valid batch still commits once;
- retry after controlled interruption does not duplicate committed rows.

If mutation would alter shared data, he would use a disposable database, source proof, or data-owner-run evidence. Safety dominates demonstration.

Gate: each behavioral regression can turn red for the mechanism it claims to guard.

**State 5: Repair the Controlling Causes**

Current evidence identifies two causes:

1. persistence and checkpoint update are not one coherent recoverable operation;
2. the schema and help generator were omitted from the worker's scope.

Ishan does not merely add assertions around old behavior. Under current owner approval, the repair:

- restores atomic or compensating persistence behavior appropriate to the fixture;
- adds cancellation and retry cases;
- changes the authoritative schema input;
- regenerates help and schema output through the owning process;
- removes or separates the unrelated formatter fixture;
- updates the worker-return checklist to include generated artifacts.

The exact implementation remains hypothetical and is not a universal data-transaction prescription.

Gate: repair addresses demonstrated causes and every changed artifact has current ownership.

**State 6: Run Direct, Integrated, and Artifact Gates**

The evidence packet now contains:

1. defective malformed-row case red and repaired case green;
2. valid rows persisted once;
3. duplicate retry after controlled interruption remains idempotent;
4. cancellation leaves the expected resumable checkpoint;
5. partial state is absent or correctly compensated under declared model;
6. full applicable unit and integration suites run with material skips explained;
7. build and static checks pass for declared target;
8. authoritative schema regenerates without unexplained diff;
9. rendered command help and schema examples match requirement;
10. contextual diff contains only approved changes;
11. rollback restores prior fixture behavior and residual state is checked;
12. a fresh reviewer reproduces the bounded conclusions.

The fixture cannot prove every production volume, database failure, platform, or schedule. The report says so.

Gate: direct behavior, broader regression, artifact consistency, and recovery converge for the current candidate.

**State 7: Separate Technical Completion From Handoff**

Technical evidence supports:

- four declared requirement clauses pass in the exercised environment;
- generated artifacts are current;
- focused and full applicable suites pass with recorded scope;
- rollback and residual checks pass in the disposable fixture.

It does not by itself support:

- untested production scale or every failure schedule;
- data-policy acceptance outside the fixture;
- merge or release permission.

The data owner reviews persistence and recovery boundaries. The integration owner inspects repository-required checks and unresolved risk. Only then does the appropriate owner make the next transition.

Gate: completion wording and authority match the same current candidate without conflation.

**State 8: Observe and Learn**

The false worker completion exposed upstream gaps:

- the request packet did not enumerate generated artifacts;
- the unit summary hid material skipped integration coverage;
- the original regression test could not detect partial state;
- the delegated return lacked requirement-to-evidence mapping;
- rollback was treated as documentation rather than a gate.

The team considers a structured return manifest, generated-output inventory, skip parser, transaction fixture, and recovery field. It adopts only controls whose recurring or severe value exceeds maintenance and false-blocking cost.

**Interruption Checkpoint**

```text
outcome_and_requirements:
current_completion_claims:
candidate_and_environment:
delegated_report_and_actual_diff:
passed_failed_skipped_and_unrun_gates:
known_red_sensitivity:
generated_and_external_artifacts:
owners_and_authority:
current_safe_behavior:
fallback_and_residual_state:
first_unmet_gate:
changed_paths:
next_action:
invalidation_event:
```

On resume, revalidate user intent, requirements, candidate, writers, command source, and approval before execution or success language.

**Failure Branches**

Bad shortcut: Ishan forwards `unit tests pass` as feature completion. Generated artifacts remain stale and cancellation leaves partial state. Withdraw the broad claim, preserve output, and restart at requirement trace.

Stale branch: another worker changes importer source after the full run. Mark affected evidence stale, inspect delta, and rerun relevant gates. Prior green output remains historical only.

Blocked branch: approved disposable persistence environment is unavailable. Keep static and unit evidence, state rollback and integration blocked, and do not run against production for convenience.

No-change branch: a worker reports missing validation, but source and a property test prove construction prevents invalid input. Correct the worker test or reject the finding rather than modifying production code.

Rollback branch: the candidate rollback restores code but leaves generated schema and checkpoint rows. Completion remains false until residual state is reconciled and requalification passes.

**Journey Acceptance**

A fresh reviewer can reconstruct requirements, candidate, worker report, actual diff, claim decomposition, gate choices, old-red/current-green evidence, full output and skips, generated artifacts, recovery, owner boundaries, and first invalidation event. The user can distinguish what passed from what remains unverified.

This is one completion scenario, not a user study or universal import architecture. Add distinct journeys only when UI, security, performance, public API, or production state creates materially different gates and owners.

## Decision Tradeoff Guide

Decide three questions separately:

1. **Claim validity:** Is the proposed work state meaningful, current, and tied to accepted requirements?
2. **Gate fit:** Which safe evidence can falsify and support that state with acceptable scope and cost?
3. **Transition authority:** Who can act on the result, and what recovery is required?

A valid claim can have an unsafe suggested command. A strong technical pass can remain unauthorized for release. A safe substitute can support a narrower state without proving the broad one.

**Hard Eligibility**

Before comparing gates, require atomic claim, current candidate, accepted requirement, known consequence, evaluator relevance, safe execution boundary, owner route, and a recoverable baseline. A hard red is not a tradeoff against convenience.

**Claim Dispositions**

| disposition | choose when | benefit | primary risk | decisive evidence |
| --- | --- | --- | --- | --- |
| Verify directly | Canonical safe evaluator observes the exact claim in current environment. | Strong target-specific evidence. | Side effects, hidden skips, or narrow coverage. | Preflight, known red, full fresh output, and scope. |
| Redesign evaluator | Existing gate is proxy-only, insensitive, flaky, or opaque. | Aligns evidence with actual requirement. | Test-maintenance cost or overfitting. | Defect mechanism, alternative fixtures, and sensitivity comparison. |
| Use safe substitute | Direct proof is prohibited but static, simulated, disposable, or specialist evidence can bound the claim. | Preserves safety and progress. | Narrower realism and residual uncertainty. | Why substitute discriminates and what remains unobserved. |
| Narrow statement | Evidence supports only a subset, platform, requirement, or artifact state. | Produces truthful useful result now. | Readers can miss exclusions. | Exact passed clauses and unrun remainder. |
| Keep blocked | Required safe evaluator, input, owner, or environment is unavailable. | Avoids unsafe or fabricated success. | Delivery delay and unresolved risk. | First unmet gate, safe state, owner, and resume condition. |
| Reject claim | Current requirement or evidence disproves the asserted defect or success state. | Avoids unnecessary work and false completion. | Defensive rejection from shallow counterexample. | Strongest contrary case and current scope. |
| Defer gate | Claim is valid but non-blocking and current state remains safe. | Keeps present task bounded. | Verification debt can become permanent. | Consequence, owner, dependency, tracking, and trigger. |
| Route owner or specialist | Product, security, data, production, platform, or policy controls the missing clause. | Preserves least authority and domain expertise. | Queue latency and fragmented context. | Atomic question, evidence packet, safe fallback, and return contract. |
| Retire gate | Claim no longer matters or a stronger stable control replaces it. | Reduces runtime, false blocking, and maintenance. | Hidden dependent or rare path reappears. | No-need or replacement evidence, residual audit, and owner decision. |

`No claim yet` is an active disposition, not a score of zero. It prevents pressure for favorable language from distorting evidence.

**Evaluator Options**

| evaluator | choose when | benefit | characteristic failure | verification of evaluator |
| --- | --- | --- | --- | --- |
| Focused test | One behavior and mechanism need fast discrimination. | Clear attribution and rapid iteration. | Omits integration or non-intended paths. | Old-red/current-green plus adjacent cases. |
| Full applicable suite | Broad regression claim follows a local change. | Covers established repository contracts. | Expensive, flaky, or still missing requirements. | Full output, skip review, and candidate identity. |
| Build or static command | Claim concerns compilation, types, schema, formatting, or deterministic structure. | Reproducible and often inexpensive. | Overclaimed as runtime or requirement proof. | Known invalid shape and exact target. |
| Property or model check | Large input or state space has a stable invariant. | Broader mechanism coverage. | Generator bias, bounded exploration, or weak oracle. | Seeded counterexamples and invariant review. |
| Safe mutation | Regression gate sensitivity is uncertain. | Shows gate detects target defect. | Mutation can be unrealistic or unsafe. | Expected red for cause and restored green. |
| Simulation or disposable fixture | Direct system effect is unsafe or costly. | Tests failure and recovery without production impact. | Fidelity gap and unobserved integrations. | Compare model assumptions and owner-reviewed limits. |
| Rendered or interactive inspection | User-facing artifact must be visually or behaviorally usable. | Observes actual presentation and interaction. | Sample devices and subjective judgment. | Stable viewports, states, accessibility, and fresh artifact identity. |
| Requirement audit | Completion depends on multiple accepted clauses. | Exposes omitted work despite green suite. | Checklist can be complete for wrong requirements. | Owner-current contract and clause-level evidence. |
| Specialist assessment | Security, privacy, production, data, or complex architecture dominates. | Applies controlled expertise and authority. | Queue delay and non-reproducible judgment. | Explicit scope, evidence, alternatives, and residual decision. |
| Owner-run operation | Verification requires privileged or sensitive environment. | Preserves authority and directness. | Result summary can be incomplete. | Predeclared packet, protected evidence, and independent interpretation. |
| Manual fallback | Shared automation is unavailable or unreliable. | Maintains completion capability. | Slower and variable. | Same claim contract, double-check, and recorded limitations. |

**Tradeoff Dimensions**

| dimension | question | evidence | hidden cost |
| --- | --- | --- | --- |
| Claim alignment | Does the evaluator observe the exact asserted state? | Requirement, mechanism, and known-red behavior. | Convenient proxy produces false assurance. |
| Candidate freshness | Does result attach to final current work and inputs? | Revision, worktree, environment, generated, and dependency fingerprint. | Green evidence expires after late edit. |
| Consequence | What happens if pass or fail interpretation is wrong? | Users, data, reach, detection, and recoverability. | Rare severe tail or broad low-grade false blocking. |
| Scope | Which requirements, platforms, and non-intended paths are covered? | Traceability, compatibility, generated, artifact, and integration cases. | Aggregate pass hides missing clause. |
| Safety and privacy | Can evidence be gathered without unauthorized effects or exposure? | Command preflight, policy, data flow, and cleanup. | A correct result obtained through unacceptable operation. |
| Reproducibility | Can another reviewer inspect or repeat evidence? | Saved command, candidate, output, fixture, and environment. | Private memory or ephemeral state. |
| Recovery | Can prior safe behavior and gate state return? | Fallback, rollback, residual check, and requalification. | Written route depends on same failed component. |
| Authority | Who accepts intent, specialist risk, merge, and release? | Policy and current owner record. | Technical pass masquerades as permission. |
| Cost | What design, runtime, reviewer, owner, queue, and correction work follows? | Observed effort and bounded prediction. | Fast local pass creates long-term support burden. |
| Lifecycle | Who owns refresh, flake, false block, migration, and retirement? | Ownership, reliability history, disable path, and expiry. | Orphaned shared gate becomes bottleneck. |

Use qualitative evidence-bearing comparisons unless local repeated data supports metrics. One hard safety or applicability failure can reject a gate while every cost estimate remains uncertain.

**Decision Process**

1. State the exact claim, user outcome, and unchanged baseline.
2. Split requirement, candidate, evaluator, result, scope, authority, and recovery premises.
3. Eliminate or pause options that fail hard eligibility.
4. Include only evaluators capable of addressing the same claim or explicitly narrower alternatives.
5. Compare sensitivity, coverage, safety, reproducibility, recovery, and lifecycle.
6. Test the decisive premise of rejected options where proportionate; avoid straw comparisons.
7. Choose the least-risk evidence set that supports the required state.
8. Define pass, relevant fail, stop, cleanup, fallback, and expiry before execution.
9. Record observed results separately from predicted cost.
10. Reopen after material claim, candidate, requirement, environment, source, or owner change.

**Decision Record**

Record claim, candidate, accepted requirement, gate candidates, hard boundaries, selected and rejected evidence forms, expected fail, command effects, observed results, scope, owner decisions, fallback, recovery, residual uncertainty, and first overturn event. Link large output rather than embedding private or volatile logs.

**Worked Decisions**

Direct verification: a local bug has a safe deterministic fixture. Old candidate red, current candidate green, and full relevant suite pass. Direct evidence dominates simulation.

Unsafe direct gate: proving production recovery would mutate real data. Reject direct execution under current authority and use an approved disposable rehearsal plus owner evidence. Release recovery remains bounded to that substitute.

Narrow completion: Linux debug build passes while Windows release packaging is unavailable. State the Linux debug result and keep cross-platform release blocked.

Proxy rejection: a lint command is proposed to verify a retry fix. Lint cannot observe retries. Use a failure-injection test or keep claim unverified.

Delegated choice: a worker reports tests pass. Independent diff shows a generated artifact missing. Rerun after regeneration and do not forward worker status.

Gate retirement: a manual schema checklist is fully replaced by a deterministic compiler-enforced contract with known pass, fail, fallback, and low false blocking. Remove duplicate manual pressure after residual audit.

**Cost of Being Wrong**

Wrong success can ship defects, omit requirements, expose data, authorize unsafe actions, or break trust. Wrong failure can block valid work, create unnecessary changes, and exhaust owner capacity. Wrong gate selection can consume time while observing a proxy. Wrong retirement can reopen a rare severe path.

For consequential states, name blast radius, detection delay, user bypass, correction and rollback cost, persistent effects, shared dependencies, current safe fallback, and owners able to respond.

**Decision Audit**

A fresh reviewer should reproduce the selected state from the same claim, candidate, and evidence; identify controlling hard boundary and owner; explain why alternatives do not better satisfy the claim; and state first invalidation event.

Repeated choices are architecture evidence. Proxy-test recurrence can improve test seams; unsafe proof requests can justify simulation; stale results can justify candidate manifests; shared-gate outages can justify independent fallback; and low-value checks can be retired. Do not turn one local evaluator choice into universal doctrine.

## Local Corpus Hierarchy

Hierarchy is claim-scoped. The local source can be primary for verification method, supporting for reporting style, silent about the repository's commands, and historical for a changed workflow. A path-wide label cannot supply target evidence or authority absent from its passage.

The two local paths are one byte-identical lineage at this boundary. Current path is the operational default; archive preserves provenance. They are not independent votes.

**Role Vocabulary**

| role | meaning | allowed use | caution |
| --- | --- | --- | --- |
| Primary direct | Best direct support for one atomic premise in its evidence domain. | Ground the claim within source scope, revision, candidate, and authority. | Still verify target applicability and action authority separately. |
| Supporting | Adds rationale, example, history, counterargument, or independent corroboration. | Deepen interpretation without replacing controlling evidence. | Check lineage independence and avoid confidence by count. |
| Provisional | Relevant but incomplete, unrefreshed, incompatible, or not reproduced. | Form a hypothesis, plan, or blocked state. | Cannot support consequential success. |
| Duplicate locator | Same observed content or upstream claim at another path. | Preserve provenance and retrieval. | Count once and recompute after change. |
| Historical | Establishes former behavior, result, rationale, or pinned environment. | Explain migration and prior state. | Do not present as current completion. |
| Negative | Counterexample, failed run, invalid gate, or disproven claim. | Report red, reject overclaim, and prevent recurrence. | Scope the failure; another evaluator may remain valid. |
| Conflicting | Applicable evidence or owners imply incompatible states. | Block dependent statement and drive reconciliation. | Do not resolve by status, count, recency, or confidence alone. |
| Superseded | A new requirement, root result, or gate intentionally replaces the old premise. | Use replacement and preserve dependency history. | Verify residual badges, docs, and automation. |
| Silent | Source does not answer the required premise. | Reveal gap and route elsewhere. | Never stretch adjacent language into proof. |

**Local Lineage Roles by Claim**

| source content | primary direct for | supporting for | silent or limited for |
| --- | --- | --- | --- |
| Overview and Iron Law | Fresh evidence before completion implications. | Evidence-first communication and rationalization resistance. | Actual command, current candidate, sufficient coverage, and owner permission. |
| Gate Function | Identify, run fully, read output, verify entailment, then claim. | Completion state-machine design and evidence records. | Unsafe command authorization or universal one-command sufficiency. |
| Common Failures | Distinct proof for tests, linter, build, bug fix, regression, agent completion, and requirements. | Claim taxonomy and proxy detection. | Exhaustive coverage of artifacts, security, recovery, or platform semantics. |
| Red Flags and Rationalization | Detect confidence, fatigue, partial-check, delegated-trust, and wording shortcuts. | Preflight and audit prompts. | Technical root cause or moral judgment about a person. |
| Key Patterns | Concrete method examples for tests, regression, build, requirements, and delegation. | Evaluator design and reporting examples. | Repository-specific command names or safe execution. |
| Why This Matters | Consequences of false completion in anecdotal memories. | Motivation and failure brainstorming. | Prevalence, effect size, or current project outcome. |
| When To Apply and Bottom Line | Trigger before success statements and workflow transitions. | Agent mode selection and gate placement. | That every explanation or positive word requires full target verification. |

**Controlling Evidence by Dimension**

| dimension | typical controlling evidence | local lineage role |
| --- | --- | --- |
| User outcome and constraints | Current user instruction within authority. | Supplies verification method, never overrides request. |
| Intended behavior | Accepted requirement, API, artifact contract, product or design owner. | Requires requirement review but does not choose intent. |
| Current candidate | Source, config, worktree, diff, generated output, dependency, and environment identity. | Requires fresh evidence but supplies no target state. |
| Evaluator definition | Repository instructions, test source, build config, schema, renderer, or specialist procedure. | Provides selection discipline and example classes. |
| Observed behavior | Full current command output, reproduction, trace, render, or approved experiment. | Requires reading evidence but does not contain the result. |
| Failure sensitivity | Old-red/current-green, known invalid fixture, safe mutation, or source proof. | Directly motivates red-green regression checks. |
| Requirement coverage | Clause-to-test, review, artifact, or owner mapping. | Directly motivates checklist review, not clause content. |
| Platform semantics | Current primary external source plus target configuration and behavior. | Any local platform hints are at most historical leads. |
| Security, data, production | Controlling policy, specialist evidence, and accountable owners. | Generic evidence-first caution cannot authorize action. |
| Merge or release | Repository process and responsible integration or release owner. | Can trigger pre-transition verification, not decide universally. |
| Outcome value | Baseline, accepted results, corrections, escapes, false blocking, and maintenance. | Suggests evidence discipline, not measured effectiveness. |

Evidence class, applicability, gate result, and authority are orthogonal. A fresh passing command can still test the wrong requirement. A current platform fact can be locally disabled. An owner can accept a trial without changing the technical uncertainty.

**Claim Classification Procedure**

1. Split statement into requirement, candidate, evaluator, result, scope, recovery, and authority premises.
2. Identify direct user constraints and governing repository or organization policy.
3. Locate exact source, command, behavior, artifact, owner, or measurement for each premise.
4. Determine lineage so duplicate paths and copied outputs count once.
5. Assign primary, supporting, provisional, duplicate, historical, negative, conflicting, superseded, or silent role.
6. Test current candidate and relevant fail sensitivity where behavior depends on it.
7. Obtain separate authority for product, architecture, security, data, production, merge, and release actions.
8. State completion wording, exclusions, fallback, and allowed next transition.
9. Link dependent reports, badges, approvals, docs, gates, and handoffs.
10. Block consequential transition when support, scope, safety, authority, or recovery remains unresolved.

**Conflict Containment**

When evidence conflicts:

- preserve each atomic proposition and role;
- freeze only the dependent state where policy permits;
- compare requirement, candidate, revision, environment, evaluator selection, cache, skips, and owner domain;
- identify factual, semantic, tool, design, policy, or value disagreement;
- run a safe discriminating case when possible;
- route intent and residual risk to controlling owners;
- record resolution, rejected interpretation, and reopen event;
- invalidate dependent completion labels and next actions.

Do not settle by source count, path age, latest date alone, reviewer seniority, positive tone, or number of green commands.

**Role Movement**

| event | prior role | possible new role | required action |
| --- | --- | --- | --- |
| Current and archive source diverge | Duplicate locator | Current, historical, conflicting, or superseded lineage. | Inspect content, ownership, and dependent guidance. |
| Current run disproves a success report | Provisional or asserted primary result | Negative completion evidence. | Withdraw or narrow claim, preserve output, and repair. |
| Requirement changes intended state | Primary intent record | Historical or superseded. | Re-evaluate tests, artifacts, implementation, and completion. |
| Regression test stays green under defect | Preferred gate | Negative evaluator evidence. | Keep claim unresolved and redesign sensitivity. |
| Owner rejects technically supported transition | Technical primary plus open authority | Supported but unauthorized. | Preserve result and keep behavior inactive. |
| New platform evidence contradicts copied gate advice | Historical lead | Stale or version-bound. | Invalidate workflow claims and requalify target. |
| Broader gate subsumes focused check | Independent controls | Superseded or supporting. | Verify equivalent sensitivity and remove duplicate burden. |
| Outcome data shows repeated false blocking | Adopted gate | Mixed or negative lifecycle evidence. | Narrow, adapt, or retire while preserving hard constraints. |

Role movement preserves provenance. A failed gate is useful negative evidence; a historical requirement explains old behavior; a superseded check can remain part of migration audit.

**Worked Role Records**

Good test claim: local lineage is primary for the run-read-claim sequence; repository test definition is primary for command; current output is primary for observed pass; requirement controls scope; owner controls transition.

Bad canonical claim: archive skill is labeled canonical, so its example becomes the repository's mandatory command. Reclassify the source as method and discover the target gate.

Borderline platform state: current external docs later support a job result, but target runner does not exhibit it. External source is primary for its version; local compatibility remains negative or unresolved; broad completion stays blocked.

Stale negative: prior cached run missed a changed path. Preserve the failure so future gate design does not reintroduce the same cache key.

Duplicate output: CI and a local wrapper report the same underlying test execution. Preserve both locators for operations but count one observed run.

Pair divergence: current skill gains a new artifact rule absent from archive. Inspect and assign role only to that clause; do not infer target artifact success.

**Hierarchy as Retrieval Policy**

- Load primary direct evidence for the active premise.
- Add supporting evidence when it can change interpretation, consequence, or gate choice.
- Do not load duplicate bytes or summaries for confidence.
- Load negative and historical evidence when it prevents recurrence or explains migration.
- Load conflicts together and reserve context for reconciliation.
- Stop when omitted evidence cannot change the bounded state.
- Reopen after claim, candidate, requirement, source role, environment, or owner changes.

Stable method roles can be cached. Target candidate and pass state must remain fresh.

**Hierarchy Audit**

A fresh reviewer should reproduce the local pair identity; trace a completion state to exact source, target, and requirement evidence; explain every role; confirm scope and authority were not inferred from source rank; detect mixed statements; replay one conflict; move one role after a changed premise; and find all dependent states that must regress.

Automate identity, candidate fingerprint, schema, and dependency links. Keep semantic support, gate sufficiency, intended behavior, and residual risk accountable. This hierarchy is completion-memory consistency: it determines which green states remain current, which become history, and which transitions stay blocked during disagreement.

## Theme Specific Artifact

The reusable artifact is a **Completion Evidence Warrant**. It carries one proposed state from claim definition through candidate identity, evaluator design, safe execution, full result, scope interpretation, owner transition, invalidation, and retirement. It stores explicit decision rationale, not hidden reasoning or a raw transcript.

Use a compact warrant for low-consequence local checks. Expand it for behavioral claims, delegated work, multiple requirements, generated artifacts, migrations, specialist controls, external systems, shared gates, or long-running tasks.

**State Model**

| state | meaning | permitted next action |
| --- | --- | --- |
| `proposed` | A success or failure statement is being considered but its truth condition is not defined. | Clarify or split claim. |
| `defined` | Atomic claim, requirement, candidate scope, and allowed transition are explicit. | Select evaluators. |
| `planned` | Gate, expected pass and relevant fail, safety, fallback, and owner are recorded. | Review plan or prepare environment. |
| `ready_to_run` | Candidate and approved safe environment are current; prerequisites pass. | Execute exact evaluator. |
| `executed` | An attempt occurred, but interpretation and integrated evidence are incomplete. | Read output, inspect effects, classify result. |
| `passed_bounded` | Fresh evidence supports the exact claim within stated scope. | Report bounded pass or seek next owner transition. |
| `failed` | Current evidence contradicts the claim or required gate is red. | Diagnose, repair, reject, rollback, or redefine. |
| `blocked` | Safe evaluator, input, environment, source, or owner is unavailable. | Preserve safe state and route or wait. |
| `unrun` | Required or candidate gate did not execute. | Run, justify non-applicability, or narrow statement. |
| `stale` | Material candidate, requirement, environment, source, or owner changed after evidence. | Reconcile and rerun affected gates. |
| `conflicting` | Applicable results or owners imply incompatible states. | Freeze dependent transition and resolve. |
| `not_applicable` | Gate cannot affect the claim under a recorded reason. | Proceed using remaining applicable evidence. |
| `authorized` | Controlling owner accepts the downstream action for exact current candidate and residual risk. | Perform only that action under policy. |
| `rolled_back` | Prior safe state was restored after failed or revoked candidate. | Diagnose, redesign, or close negative evidence. |
| `superseded` | Another claim, requirement, gate, or warrant controls the result. | Follow replacement and audit residual dependents. |
| `retired` | Claim or gate no longer changes a live decision. | Remove recurring verification and stale badges. |
| `closed` | Requested state is complete, evidence and limits are known, and lifecycle is recorded. | Reopen only after invalidation or new evidence. |

State is evidence-bearing. `Planned` is not `passed`. `Executed` is not interpreted. `Passed_bounded` is not `authorized`. Any material change can regress a warrant to `defined`, `stale`, or `blocked`.

**Core Warrant**

| field | completion rule |
| --- | --- |
| Warrant identity and state | Stable id, current state, owner, created boundary, last validated candidate. |
| Claim | Atomic externally checkable proposition, exact wording, consequence, and permitted next action. |
| User outcome | Observable result sought rather than `finish the task`. |
| Requirement baseline | Current accepted clauses, conflicts, non-intended behavior, and owner decisions. |
| Candidate identity | Revision, worktree, paths, generated state, dependencies, config, environment, and concurrent writers. |
| Evidence sources | Method, target definition, behavior, external, policy, owner, measurement, negative, conflicting, and unknown roles. |
| Evaluator candidates | Commands, source proofs, static rules, fixtures, renders, scenarios, specialists, and no-run alternatives. |
| Selected gate | Why it can falsify the claim and why alternatives were rejected or deferred. |
| Safety preflight | Working directory, inputs, reads, writes, network, credentials, private data, processes, effects, cleanup, and permission. |
| Expected states | Pass, relevant fail, skips, warning, timeout, cancellation, stop, fallback, and recovery defined before execution. |
| Attempts | Sequence under one claim, candidate, environment, full state, changed condition, and cost. |
| Observed result | Exit or verdict, counts, failures, skips, warnings, cache, timeout, and concise privacy-safe evidence. |
| Sensitivity | Defective baseline, known-invalid fixture, safe mutation, counterexample, or source proof. |
| Scope | Covered and unobserved requirements, paths, users, platforms, versions, artifacts, and environments. |
| Integrated evidence | Broader suite, build, static, generated, visual, compatibility, migration, diff, and re-review results. |
| Interpretation | What evidence supports, contradicts, leaves unknown, and cannot authorize. |
| Authority | Named owners, exact domains, accepted candidate, conditions, and unapproved clauses. |
| Recovery | Native fallback, rollback, residual-state checks, user route, and requalification. |
| Counterargument | Strongest alternative explanation or reason the pass may be insufficient. |
| Invalidation | Candidate, requirement, source, environment, owner, platform, or outcome event making state stale. |
| Resume | Last durable state, first unmet gate, safe behavior, changed artifacts, and first next action. |

Link large logs, diffs, screenshots, and artifacts. Do not store credentials, private payloads, full prompts, hidden reasoning, or interpersonal speculation.

**Consequence-Scaled Detail**

| class | minimum warrant |
| --- | --- |
| Editorial | Claim, source of truth, exact candidate, contextual check, approval, and invalidation. |
| Structural | Add canonical validator, known invalid shape, full output, generated state, and scope. |
| Behavioral | Add requirement, old-red/current-green, direct and integrated checks, non-intended cases, owner, and fallback. |
| Artifact usability | Add build or generation, representative renders or interactions, accessibility, viewports or states, and audience limits. |
| Migration or cross-module | Add dependency trace, compatibility, mixed states, data or generated residuals, staged rollout, and rollback. |
| Security, privacy, credentials, production, or external system | Add controlling policy, specialist owner, approved safe evaluator, incident route, and residual-risk decision. |
| Delegated work | Add return contract, actual artifact reconciliation, unrelated changes, local rerun, and integration owner. |
| Shared or automated gate | Add eligible opportunities, baseline, known pass and fail, false blocking, observability, fallback, support, and retirement. |
| Rejection or no-claim | Add strongest plausible counterexample, current evidence, why success is unavailable, and reopen event. |

Line count does not determine consequence. A one-line permission change can require specialist evidence.

**Filled Illustrative Warrant**

All identities below belong to the hypothetical Meridian journey.

| field | illustrative value |
| --- | --- |
| Identity and state | `meridian-import-completion`; state `failed` after initial worker report; owner: verification coordinator. |
| User outcome | Valid rows persist once; malformed rows leave no partial state; cancellation is resumable; generated help matches schema. |
| Claim | `The delegated import feature is complete and ready for integration.` |
| Requirement baseline | Four versioned clauses; production-volume and all failure schedules remain outside fixture. |
| Candidate | Hypothetical base and head, importer and tests changed, schema output stale, unrelated formatter fixture present. |
| Evidence source | Worker reports unit pass; actual worktree and requirement trace are controlling for local state. |
| Initial gate | Canonical focused unit selection under approved local fixture. |
| Initial result | Focused units pass; integration skipped; cancellation absent; generated verification unrun. |
| Sensitivity result | Original malformed-row test stays green under partial commit and is therefore a proxy. |
| Disposition | Broad completion fails; focused unit result remains bounded evidence. |
| Required repair | Transaction-aware case, cancellation and retry gates, authoritative schema regeneration, unrelated-scope reconciliation. |
| Safety | Disposable persistence environment only; production mutation prohibited. |
| Recovery | Restore prior fixture, clear residual rows, regenerate old schema, rerun current gates. |
| Authority | Data owner for persistence and recovery; integration owner for next transition. |
| First unmet gate | Claim-sensitive integration and generated artifact evidence. |
| Invalidation | Requirement, candidate, generator, persistence model, environment, worker scope, or owner change. |
| Resume | Revalidate candidate and approved fixture, then run repaired old-red/current-green gate. |

This example does not establish a real import design or observed production outcome.

**Bad and Borderline Fragments**

Bad claim: `Everything works.` Split into atomic states before recording evidence.

Bad evidence: `Worker says tests passed.` Record delegated report as provisional and inspect actual current result.

Bad state: `passed_bounded` after command invocation only. Use `executed` until full output and interpretation are complete.

Borderline: focused tests pass, but rollback environment is unavailable. Keep focused pass and mark readiness blocked.

Stale: current candidate changes after owner authorization. Regress warrant to stale and renew evidence plus approval.

Good negative: known-red remains green, proving gate insensitive. Mark evaluator failed even if candidate appears healthy.

Retired: stable compiler rule replaces manual shape check. Preserve replacement and residual audit, then remove manual warrant generation.

**Warrant Validation**

Deterministic checks can verify:

- required fields for consequence class;
- valid states and allowed transitions;
- candidate and evidence timestamps or fingerprints;
- claim and requirement identities;
- evaluator and result-state presence;
- attempt grouping, failure, skip, and unrun fields;
- owner, fallback, invalidation, and resume state;
- evidence-link shape and generated-output inventory;
- prohibited sensitive literal patterns under policy.

Human review must verify:

- whether the claim is atomic and meaningful;
- whether evidence semantically supports it;
- whether known red actually represents the failure;
- whether output interpretation and exclusions are honest;
- whether owner authority covers the transition;
- whether recovery is credible and independent;
- whether retained data is proportionate and safe.

Use negative state tests in a disposable warrant: change candidate after pass, remove requirement, introduce hard safety red, hide a skip, revoke owner, or delete fallback. The warrant must cease to qualify for its prior state. A schema that remains green under stale evidence documents aspiration.

**Closure and Pruning**

At closure, a fresh reviewer should recover claim, requirement, candidate, gate, expected red, full result, scope, authority, recovery, residual uncertainty, and first reopen event. Remove exploratory noise and preserve concise negative evidence only when it prevents recurrence.

One warrant should be authoritative. CI pages, tasks, comments, journals, and handoffs may link or render parts, but copied state must not drift. The warrant supports truth and authority; it creates neither by itself.

## Worked Example Set

Every example is hypothetical. Replace the claim, requirement, candidate, command, environment, owner, and result before local use. The reusable element is the premise that changes state.

**Set 1: Test Suite Claim**

Statement: `All tests pass.`

Good: the current canonical full applicable command runs against final candidate; output shows zero relevant failures; skipped and excluded groups are identified; candidate fingerprint and environment are recorded. State bounded pass.

Bad: one focused file passes, so the full repository is called green. Report the selected scope and run broader required gates.

Borderline: full local suite passes but an approved external-service group is unavailable. State local suite pass and integration blocked.

State flip: if repository policy explicitly marks that external group non-blocking for this change class, the broader state may advance under the recorded rule.

**Set 2: Build Success**

Statement: `The project builds.`

Good: current target-specific production build exits zero with generated assets, features, and material warnings reconciled.

Bad: linter passes and is treated as compilation evidence.

Borderline: debug build succeeds but release packaging for another platform is unrun. Report exact target only.

State flip: if requested deliverable is solely the verified debug target, the narrower completion is sufficient; do not retain broader wording.

**Set 3: Bug Fixed**

Statement: `The empty-input bug is fixed.`

Good: defective baseline fails the accepted typed-error case, current candidate passes, adjacent valid inputs and integrated suite pass, and diff is scoped.

Bad: guard code exists and reviewer says it looks right, but original symptom was never run.

Borderline: source proof shows the branch changed, but production-only parser cannot be invoked safely. State source-supported repair with runtime effect unverified.

State flip: an approved disposable parser fixture can promote the runtime clause after direct observation.

**Set 4: Regression Test Sensitivity**

Statement: `The new test prevents recurrence.`

Good: safely remove or mutate the fix, observe test red for expected reason, restore candidate, and observe green.

Bad: test passes once on fixed code and is called a regression.

Borderline: direct mutation is destructive; a minimal disposable model and source trace support only bounded sensitivity.

State flip: if test remains green under target defect, demote it to proxy even when all current runs pass.

**Set 5: Requirements Complete**

Statement: `All requested behavior is implemented.`

Good: current requirement inventory maps each clause to behavior, test, artifact, review assertion, or owner decision; gaps and non-intended cases are visible.

Bad: general test suite passes and is assumed to define requirements.

Borderline: technical clauses pass but product wording has two plausible interpretations. Keep requirement completion conflicting and route owner.

State flip: a versioned owner decision resolves ambiguity and triggers re-evaluation of affected tests and code.

**Set 6: Delegated Work**

Statement: `The worker completed the assigned change.`

Good: inspect actual returned files and diff, reconcile approved scope, rerun current focused and integrated gates, and verify generated plus non-file effects.

Bad: forward the worker's success summary unchanged.

Borderline: files are correct, but another writer changed one dependency after the worker's run. Mark delegated evidence stale and reverify current composition.

State flip: one integration owner reconciles the dependency and fresh gates pass.

**Set 7: User-Facing Artifact**

Statement: `The generated page is ready.`

Good: build and schema checks pass; representative desktop and mobile renders, long content, empty and failure states, accessibility, and interactions are inspected.

Bad: HTML file exists and parses, so usability is declared.

Borderline: desktop render and interaction pass while mobile viewport is unavailable. Report desktop state and keep cross-viewport readiness unrun.

State flip: approved mobile render and interaction evidence can promote the broader artifact claim.

**Set 8: Migration and Recovery**

Statement: `The migration is safe to release.`

Good: forward and backward paths, mixed versions, representative data, interruption, rollback, residual state, monitoring, and owner process pass in an approved environment.

Bad: migration applies once on an empty database and release readiness is claimed.

Borderline: forward migration passes but downgrade loses data required by old version. Keep readiness failed even when all normal tests pass.

State flip: a redesigned compatibility path and verified residual cleanup can requalify the candidate.

**Set 9: Performance Completion**

Statement: `The latency requirement is met.`

Good: current correctness-equivalent candidate is benchmarked against declared workload, environment, baseline, warm and cold states, and resource limits with local threshold set before observation.

Bad: one microbenchmark or complexity argument is presented as production p99 evidence.

Borderline: local representative workload passes while production contention and tails are unobserved. State local benchmark result only.

State flip: bounded canary under owner guardrails can support broader operational evidence; it still does not prove permanence.

**Set 10: Completion Without a Favorable Claim**

Statement: `Verification is complete.`

Good failure: full gate runs and finds a reproducible defect. The verification task is complete with state `failed`; implementation is not complete.

Good blocked result: direct production proof is prohibited and no safe substitute suffices. The analysis is complete with first unmet gate, fallback, and owner route.

Bad: add `probably` to a success statement because evidence is missing.

Retirement: a manual checklist is replaced by a reliable compiler rule with known pass, fail, fallback, and low false blocking. Remove duplicate manual verification after residual audit.

**Example Transfer Checklist**

Before using any fixture, replace and verify:

- exact claim and downstream action;
- accepted requirement and non-intended behavior;
- final candidate, generated inputs and outputs, environment, and concurrent writers;
- canonical evaluator and why it can reject relevant defect;
- expected pass, relevant fail, skips, warning, timeout, cleanup, and fallback;
- command safety, privacy, credentials, network, and external effects;
- complete observed result and attempt history;
- focused, integrated, compatibility, migration, visual, and recovery scope as applicable;
- owner decisions and authority boundaries;
- first event that invalidates the state.

Do not copy hypothetical commands or preserve a state when its decisive premise differs.

**Example Quality Test**

For each maintained fixture:

1. Name target completion boundary and expected state.
2. Identify one or two decisive premises.
3. Mutate a premise in a disposable copy; expected state should change.
4. Ask independent reviewers to explain the result and strongest counterargument.
5. Confirm example contributes a distinct mechanism rather than repeating another.
6. Compare synthetic reasoning with real outcomes before claiming calibration.
7. Refresh after source, platform, policy, requirement, or workflow change.
8. Retire examples that no longer teach a unique boundary.

If state never changes under mutated evidence, the fixture likely teaches preference. If reviewers disagree, locate whether the missing dimension is claim, candidate, requirement, evaluator, result, scope, safety, authority, or recovery.

The set can seed gate tests and reviewer training, but retain held-out and messy real cases to avoid overfitting.

## Outcome Metrics and Feedback Loops

Measure whether a completion control produces the correct bounded state and safer next action at acceptable total cost. Do not use command count, rerun frequency, green-label rate, report length, or verification speed as outcome proxies alone.

No universal target is established. Choose local thresholds before observation from consequence, reversibility, claim frequency, owner capacity, baseline, and expected false-blocking cost. Use case review rather than rates when samples cannot support quantification.

**Measurement Question**

> For completion control `[identity]`, does it improve `[correct pass, fail, blocked, stale, no-claim, or authorized transition]` for `[declared claim classes and users]` relative to `[baseline]`, while preserving `[requirement, candidate, safety, privacy, authority, and recovery guardrails]`, at acceptable `[author, verifier, tool, correction, queue, support, and retirement cost]`?

If plausible results do not map to retain, narrow, redesign, automate, rollback, route, retire, or no-change, do not collect the metric.

**Outcome Families**

| family | eligible opportunity and accepted result | observations | interpretation warning |
| --- | --- | --- | --- |
| Claim accuracy | A proposed success or failure state needs an evidence-backed disposition. | Correct pass, fail, blocked, stale, conflicting, or no-claim state; later correction. | Reviewer agreement can be shared bias. |
| Candidate freshness | Work or inputs change after or before evidence. | Stale result detected, missed invalidation, rerun, incorrect reuse. | Frequent rerun does not prove good candidate identity. |
| Gate sensitivity | Evaluator claims to detect a target failure. | Known red detected, defect mutation missed, proxy behavior, false red. | One mutation does not prove full coverage. |
| Requirement coverage | Work claims all accepted clauses complete. | Clauses mapped, omitted, contradicted, owner-resolved, or later discovered. | Complete matrix can encode wrong requirement. |
| Result interpretation | Full output must become the correct state. | Failure, skip, timeout, cache, warning, cancellation, and scope handled correctly. | Tool summary can conceal semantics. |
| Delegated verification | Worker or automation reports state. | Diff mismatch, unrelated changes, local rerun, corrected return, accepted result. | Final success can hide costly reconstruction. |
| Artifact usability | Generated or user-facing artifact needs direct inspection. | Structural, rendered, accessibility, interaction, platform, and recovery outcomes. | Sample viewports cannot prove universal usability. |
| Non-interference | Gate should not block or burden unrelated claims. | False block, irrelevant command, low-value rerun, bypass, and manual override. | Aggregate benefit can hide one harmed team or task class. |
| Safety and privacy | Evidence collection must stay within approved effects and data. | Unsafe command, sensitive output, unauthorized service, successful containment. | Correct technical result cannot offset a hard breach. |
| Authority accuracy | Technical result must route to correct owner and action. | Premature merge, stale approval, correct handoff, owner correction. | Owner acceptance cannot make technical evidence true. |
| Recovery | Failed candidate or gate must return to safe state. | Fallback use, rollback, residual state, requalification, recovery failure. | Written recovery is not exercised recovery. |
| Latency and effort | Claim moves from proposal to correct state or fallback. | Active design, execution, queue, interpretation, correction, owner, and retry time. | Faster can mean proxy checks or hidden skips. |
| Lifecycle sustainability | Shared gate exists over time. | Drift, flake, support, false block, source refresh, migration, and retirement. | Initial adoption understates long-term cost. |

The seed's leading indicator, every shipped claim has a requirement id and fresh evidence, is useful only when `shipped claim`, freshness, requirement scope, and evidence sufficiency are defined. The seed failure signal, TDD or specs without failing and passing evidence, is useful for behavioral regression claims but does not mean every architecture or artifact decision needs the same red-green form.

**Hard Guardrails**

Any applicable red stops favorable expansion:

- material completion statement lacks current claim-matched evidence;
- result attaches to stale, incomplete, or wrong candidate;
- gate cannot reject the relevant defect but is presented as regression proof;
- requirement, generated artifact, platform, or material skip is omitted from broad success;
- evidence exposes secrets, private content, personal data, or unapproved artifacts;
- verification creates unauthorized destructive, production, credentialed, or external effects;
- owner approval is missing, stale, or narrower than the transition;
- failures, corrections, rollbacks, bypasses, and unrun opportunities are excluded;
- no safe fallback, rollback, or responsible owner exists for consequential gate.

Hard events are states, not percentage deductions.

**Cost Families**

| cost | include | avoid |
| --- | --- | --- |
| Claim definition | Requirement reading, decomposition, consequence, and allowed action. | Treating generic `done` as free. |
| Candidate capture | Revision, worktree, generated, config, dependency, environment, and writer state. | Omitting late edits and non-file effects. |
| Gate design | Mechanism analysis, expected red, fixture, safety, fallback, and owner. | Counting only command runtime. |
| Execution | Human and machine time, setup, services, cache, artifacts, cleanup, and retries. | Ignoring failed and timed-out attempts. |
| Interpretation | Full output reading, skip and warning analysis, requirement trace, and scope. | Counting a summary line as all review. |
| Correction | Candidate, gate, requirement, report, owner, or workflow repair after wrong state. | Crediting final success while hiding churn. |
| Queue and reconciliation | Environment, reviewer, specialist, owner, parallel returns, and conflict delay. | Calling parallel wall time total cost. |
| Recovery | Fallback, rollback, residual cleanup, user route, and requalification. | Assuming revert alone restores state. |
| Lifecycle | Flake, support, source refresh, false block, migration, training, incident, and retirement. | Measuring only first green run. |

Report wall clock and aggregate human, machine, and owner effort separately.

**Method Selection**

| method | best fit | validity risk | evidence boundary |
| --- | --- | --- | --- |
| Controlled gate replay | Deterministic validation, stale-candidate, regression-sensitivity, and requirement fixtures. | Synthetic tasks expose expected answers and omit repository mess. | Same claim, candidate semantics, rubric, and known red. |
| Independent paired interpretation | Whether reviewers map output to same bounded state. | Reviewer learning, expertise, order, and shared assumptions. | Independence or order, source access, disagreement, and correction. |
| Limited gate canary | Recurring real claim class after hard preflight. | Novelty, selection, co-changes, and rare failures. | Eligible opportunities, cohort, stop, fallback, and expansion rule. |
| Audit sample | False success, false block, stale reuse, hidden skips, and requirement gaps. | Sampling can miss rare severe events. | Selection method, denominator, consequence, owners, and unobserved population. |
| Privacy-safe state trace | Claim, candidate, execution, interpretation, correction, and handoff sequence. | Metadata can expose project or person behavior. | Minimal schema, retention, access, missingness, and no raw reasoning. |
| Incident review | Unsafe verification, escaped defect, wrong release state, or recovery failure. | Sparse cases and hindsight bias. | Trigger, cause, containment, recovery, and recurrence control. |
| Longitudinal lifecycle | Flake, support, false blocking, source drift, owner queue, and retirement. | Concurrent system and team changes weaken attribution. | Version history, co-changes, claim mix, and bounded inference. |

Use the least intrusive method that can change the decision. Consequential shared gates often need both mechanism evidence and end-to-end state outcomes.

**Measurement Protocol**

1. Define control, baseline, claim classes, eligible opportunities, accepted states, hard guardrails, and local decision thresholds before observation.
2. Freeze relevant requirements, candidate semantics, gate version, environment, users, reviewers, and owners.
3. Include intended, non-intended, valid, invalid, stale, partial, skipped, blocked, unsafe, delegated, failure, fallback, and retirement cases.
4. Define pass, fail, false success, false block, correction, bypass, stale, exclusion, and recovery.
5. Capture failed, timed-out, canceled, unrun, corrected, reverted, and rolled-back cases; state exclusions.
6. Minimize data with opaque ids, state classes, and protected evidence links rather than raw code or logs.
7. Review hard guardrails before speed, green rate, agreement, or preference.
8. Analyze task difficulty, author learning, reviewer experience, co-changes, tool updates, environment availability, and owner capacity.
9. Preserve enough observation to recompute one summary or replay one qualitative classification.
10. Apply predeclared action and record uncertainty plus expiry.

Do not claim causal productivity, defect reduction, percentiles, or reliability from samples that cannot support them.

**Feedback Actions**

| evidence pattern | action | follow-up |
| --- | --- | --- |
| Correct state improves, guardrails green, cost bounded | Retain or expand to one qualified next claim class. | Monitor drift, false block, and recovery. |
| Proxy gates recur | Redesign evaluator around defect mechanism and known red. | Recheck sensitivity and integrated outcome. |
| Stale success recurs | Improve candidate manifest and automatic invalidation. | Test rebase, generated, config, and environment change. |
| Requirement gaps recur | Add clause trace or executable acceptance before implementation. | Track omitted and wrong requirements separately. |
| Delegated reports need correction | Strengthen return schema and local reconciliation. | Measure unrelated changes, rerun effort, and actual state. |
| Hidden skips or cache cause false green | Improve result parser, selection checks, and known-red execution. | Test pass, fail, skip, cancel, and timeout states. |
| False blocking rises | Narrow trigger, add non-interference cases, or retire gate. | Confirm hard requirements remain visible. |
| Unsafe proof appears | Contain under policy and provide safe substitute or owner route. | Audit privacy, authorization, and recurrence. |
| Owner queues exceed value | Apply backpressure, federate valid ownership, or reduce gate scope. | Measure correct state and total effort. |
| Stable control replaces manual check | Retire duplicate prompt or checklist. | Verify fallback and no residual state. |

**Worked Interpretations**

Good candidate manifest: comparable tasks with automatic candidate fingerprints show fewer stale success claims and less rework while correct state and hard guardrails remain equal. Retain for observed claim classes.

Bad command metric: a team runs more checks per change and declares verification stronger. Several checks observe the same proxy while one requirement remains untested. Command count has optimized activity.

Borderline speed result: completion is faster after tasks became smaller and a new test fixture arrived simultaneously. Keep bounded workflow and avoid attributing gain solely to the gate prompt.

Automation win: recurring schema mismatch becomes a deterministic validator with known red, low false block, owner, fallback, and retirement of manual check.

No-change win: a proposed mandatory gate adds latency and generic failures without improving correct states. Rejecting it avoids lifecycle debt.

Hard stop: a shared verifier uploads private source to an unapproved service. Contain under policy; no accuracy or speed result can retain it.

**Metric Audit**

A fresh reviewer should reconstruct control, baseline, claim strata, eligible opportunities, accepted states, guardrails, and costs; verify false successes, false blocks, corrections, bypasses, unrun cases, and rollbacks remain in accounting; reproduce one result; separate observation from inference; inspect confounders; and reach the same bounded lifecycle action.

Refresh from requirement, candidate, source, platform, incident, owner, and behavior events rather than a calendar alone. The feedback loop optimizes the completion-verification portfolio and may move knowledge into requirements, tests, manifests, architecture, or retirement instead of adding commands.

## Completeness Checklist

Completeness is relative to requested mode and current evidence. A gate plan can be complete without running. A verification task can complete with a failed or blocked result. A focused pass is not integrated completion. A technical pass is not release authority.

Claim only the narrowest supported state and name the first unmet gate for any stronger one.

**Universal Hard Gates**

Any applicable red blocks a behavior-changing or readiness transition:

- claim is ambiguous or implies clauses not evaluated;
- requirement, candidate, generated state, environment, or owner is stale or unknown;
- evaluator cannot reject the relevant defect or missing requirement;
- command, render, review, or operation exceeds safety, privacy, data, network, or authority boundary;
- output is partial, timed out, canceled, conflicting, cached ambiguously, or hides material failures or skips;
- selected pass does not cover intended and non-intended scope claimed;
- delegated report is not reconciled with actual current artifacts;
- technical evidence is presented as product, specialist, merge, or release approval;
- fallback, rollback, residual-state check, or responsible owner is absent for consequential work;
- another writer changed the candidate after evidence or approval.

Do not average hard gates with command count, report polish, or confidence. `Not applicable` needs a reason whenever the domain could change state.

**Explanation Complete**

- User question and requested depth are answered.
- Applicable source and no-browse or version boundaries are visible.
- Method, target fact, owner decision, and synthesis are distinguished.
- No target pass, fix, requirement, or readiness state is implied without evidence.
- Next evidence or owner route is clear where uncertainty matters.

Allowed action: deliver explanation only.

**Claim Defined**

- Success or failure wording is atomic and externally checkable.
- User outcome, accepted requirement, and non-intended behavior are stated.
- Candidate scope and downstream action are explicit.
- Consequence of wrong pass and wrong fail is bounded.
- Unknown intent or owner questions are visible.

Allowed action: design gates. Defined does not mean verified.

**Gate Plan Complete**

- Selected evaluator can falsify the material claim.
- Candidate and requirement inputs are identified.
- Expected pass, relevant fail, skip, warning, timeout, cancellation, and stop are predeclared.
- Working directory, inputs, writes, network, credentials, data, cleanup, fallback, and owner are reviewed.
- Alternatives are considered where direct proof is unsafe or proxy-only.
- Scope and integrated follow-up are planned.

Allowed action: seek execution approval or prepare safe environment. A plan produces no result.

**Ready To Run**

- Final current candidate and all decision-relevant inputs are frozen.
- Command or inspection source is authoritative for the target.
- Required environment and dependencies are healthy enough to interpret output.
- No concurrent writer can invalidate evidence during execution.
- Safety, privacy, policy, and owner preflight pass.
- Cancellation, cleanup, and partial-effect response are available.

Allowed action: execute exact approved evaluator.

**Execution Complete**

- Full process or review ended in known state.
- Exit, failures, passes, skips, warnings, cache, timeout, cancellation, retries, and cleanup are captured.
- Candidate did not change during or after execution before interpretation.
- Partial files, artifacts, processes, comments, data, and external effects are reconciled.
- Concise privacy-safe evidence is retained.

Allowed action: interpret result. Invocation alone is not pass or fail completion.

**Bounded Pass Complete**

- Current full result supports the exact claim.
- Relevant known-red or sensitivity evidence exists where the claim is behavioral or regression-focused.
- Covered requirement, platform, artifact, and environment scope is explicit.
- Material unrun and skipped conditions are prominent.
- Result does not claim owner authority it lacks.
- Invalidation event and evidence expiry are recorded.

Allowed action: state bounded pass and proceed only to the next authorized gate.

**Failure Complete**

- Current evaluator observed a reproducible or clearly scoped contradiction.
- Failure is distinguished from environment, fixture, command, and requirement errors.
- Active unsafe effects are contained and evidence preserved.
- Candidate, gate, or claim repair options are identified.
- Current safe state, owner, and next diagnostic step are explicit.

Allowed action: repair, reject, rollback, or route. Verification can be complete while implementation is not.

**Bug-Fix or Regression Verified**

- Original requirement and failure mechanism are current.
- Defective baseline or safe mutation turns controlling gate red for expected reason.
- Current candidate turns it green.
- Adjacent valid, negative, and boundary cases pass.
- Relevant integrated suite, build, static, generated, and contextual diff checks pass.
- Recovery and owner clauses appropriate to consequence pass.

Allowed action: state the exact fix within exercised scope and seek broader readiness if requested.

**Requirements Complete**

- Current requirement inventory is versioned and owner-accepted.
- Every in-scope clause maps to a test, review assertion, artifact, proof, or owner decision.
- Contradictions and missing clauses are resolved or explicitly block the state.
- Non-intended behavior and supported compatibility are covered.
- General tests are not used as an implicit requirement inventory.
- Final candidate and evidence correspond exactly to the trace.

Allowed action: claim requirement completion within declared boundary.

**Artifact Verification Complete**

- Authoritative inputs, generation, build, and structural checks pass.
- Artifact identity matches current candidate.
- Representative content, empty, loading, failure, long, and boundary states are inspected.
- Relevant visual, viewport, accessibility, interaction, packaging, or consumer checks pass.
- Broken links, missing assets, stale generated output, and sensitive data are absent within inspected scope.
- Audience, platform, and unobserved conditions are named.

Allowed action: state bounded artifact readiness.

**Delegated Work Verified**

- Worker return is treated as provisional until inspected.
- Actual current files, artifacts, non-file effects, and unrelated changes are reconciled.
- Approved scope and requirements match implementation.
- Current local focused and integrated gates run independently.
- Generated, migration, config, dependency, and concurrent-work state is checked.
- Failures and gaps are reported rather than hidden by final success.

Allowed action: accept verified delegated state, not the worker's self-report.

**Blocked Handoff Complete**

- Exact required claim and unavailable safe input, environment, evaluator, source, or owner are named.
- Completed evidence and its scope are preserved.
- Broader success remains inactive.
- Current safe behavior and prohibited operation are explicit.
- Owner question, fallback, and first resume action are actionable.
- Handoff minimizes sensitive context.

Allowed action: wait, route, or continue independent work. Blocked is not failed or passed.

**Ready With Limits**

- All applicable claim, candidate, requirement, focused, integrated, artifact, safety, authority, and recovery gates pass.
- Every blocking clause is resolved or controlled by actual transition process.
- Deferred or unrun items are demonstrably non-blocking with owners and triggers.
- Reviewed scope, unsupported environments, specialist limits, and residual uncertainty are prominent.
- Fallback, rollback, and owner response are usable.
- Recommendation is bounded and does not claim defect absence.

Allowed action: responsible merge, release, or handoff owner decides under current policy.

**Rolled Back Complete**

- Stop trigger, failed candidate or gate, and owner decision are recorded.
- Prior safe code, artifact, config, data, and workflow state are restored.
- Generated, persistent, cached, external, and completion-label residuals are checked.
- Affected users and owners know current safe next action.
- Failed candidate remains negative evidence without sensitive payload.
- Re-adoption requires changed cause and full requalification.

Allowed action: diagnose, redesign, or close failed candidate.

**Gate-System Improvement Complete**

- Recurring or severe mechanism justifies shared gate, manifest field, return contract, or automation.
- Control has known pass, relevant fail, false-trigger, skip, timeout, disablement, fallback, and rollback cases.
- Eligible and non-intended claim classes are defined.
- Owners accept maintenance, support, source refresh, and residual burden.
- Canary or staged adoption shows value without unacceptable false blocking or safety cost.
- Duplicate manual check can be reduced or retired.

Allowed action: retain under outcome review and expiry.

**Gate Retirement Complete**

- Original claim or failure mechanism no longer affects live work, or stronger authority replaces it.
- Callers, workflows, docs, badges, prompts, policies, and dashboards are inventoried.
- Replacement or native fallback has known pass, fail, and recovery.
- Rare critical and compatibility paths are checked.
- Owner accepts removal and rollback plan.
- Stale completion state and recurring collection are removed.

Allowed action: stop running retired control and monitor bounded fallback.

**Consequence Tiers**

| tier | examples | evidence depth |
| --- | --- | --- |
| Editorial | Typo or local wording with no behavior, scope, compatibility, or privacy effect. | Complete target read, source of truth, exact diff, approval, contextual check. |
| Structural | Formatting, schema, compilation, generated shape, or deterministic static contract. | Canonical full validator, known invalid case, candidate identity, result, and generated audit. |
| Behavioral | Logic, API, error handling, state, test, config, migration, or user-facing artifact. | Requirement, known red, direct and integrated evidence, non-intended scope, owner, fallback, and expiry. |
| Consequential | Security, private data, credentials, production, broad defaults, external systems, or severe correlated effect. | Specialist authority, approved safe evaluator, incident and rollback process, staged transition, and explicit residual risk. |

Escalate by consequence and coupling, not line or command count.

**Invalid Completion Statements**

- `Planned` presented as `verified`.
- `Executed` presented as `passed` without reading full output.
- `Tests pass` from one focused selection.
- `Bug fixed` from code change without original symptom.
- `Regression test works` without known red.
- `Requirements met` because general suite is green.
- `Artifact ready` because file exists.
- `Agent complete` because worker says so.
- `Ready` because technical checks pass without owner or recovery.
- `Current` because old green badge still displays.
- `Not applicable` without reason.
- `Blocked` softened into likely success.

**Completion Record**

```text
requested_mode_and_claim:
current_state:
requirement_candidate_environment:
evaluator_and_expected_fail:
execution_and_full_result:
passed_failed_skipped_blocked_unrun:
scope_and_non_interference:
owners_and_authority:
current_safe_behavior:
fallback_rollback_and_residuals:
first_unmet_gate:
allowed_next_action:
uncertainty_and_invalidation:
```

**Completion Audit**

In a disposable warrant, change candidate after pass, remove requirement, introduce safety red, hide a skip, make delegated scope diverge, revoke owner, or delete fallback. The corresponding pass, verified, ready, or closed state must fail or regress.

A fresh reviewer should reconstruct current state, allowed action, evidence, safe fallback, and first overturn event. If a checklist remains green after controlling evidence changes, it records aspiration rather than completion.

## Adjacent Reference Routing

Keep claim definition, candidate identity, gate execution, result interpretation, bounded reporting, and completion lifecycle in this reference. Route only an atomic premise whose method, evidence, or authority lies elsewhere. Preserve one Completion Evidence Warrant and one integration owner.

The paths below were discovered by filename inventory only unless already inspected for another purpose. Existence is observed; content, quality, currentness, and applicability are not. Read the destination before relying on it.

**Candidate Routes**

| unresolved premise | inventory-derived candidate | atomic question | required return |
| --- | --- | --- | --- |
| Requirement ambiguity or executable acceptance | `idiomatic-ref-202607/executable_specification_skill_patterns-20260710.md` | Which observable contract and negative cases should the candidate satisfy? | Requirement identity, examples, trace, owner, change boundary, and unresolved clauses. |
| Defect reproduction or root cause | `idiomatic-ref-202607/systematic_debugging_method_patterns-20260710.md` | Which hypothesis and safe experiment discriminate the reported failure? | Reproduction, minimized cause, alternatives, evidence, and uncertainty. |
| Red-green implementation cycle | `idiomatic-ref-202607/tdd_cycle_skill_patterns-20260710.md` | How should a failing acceptance case drive the smallest repair and safe refactor? | Red evidence, green evidence, implementation boundary, regression, and refactor checks. |
| Code-review finding or readiness | `idiomatic-ref-202607/code_review_feedback_patterns-20260710.md` | Does a reviewer claim hold, what disposition follows, and what bounded verdict is justified? | Finding, evidence, consequence, disposition, re-review, and owner boundary. |
| User-facing explainer artifact | `idiomatic-ref-202607/html_explainer_page_patterns-20260710.md`; `idiomatic-ref-202607/visual_explainer_skill_patterns-20260710.md` | Which structural, rendered, visual, accessibility, and interaction gates establish usability? | Artifact identity, inspected states and viewports, issues, fixes, and residual limits. |
| 3D React visualization artifact | `idiomatic-ref-202607/threejs_react_visualization_patterns-20260710.md` when target actually uses that stack. | Which canvas, scene, asset, interaction, and performance evidence applies? | Versioned stack evidence, screenshots, pixel or scene checks, interactions, and fallback. |
| Repository history or prior intent | `idiomatic-ref-202607/github_context_capture_patterns-20260710.md` | Which change, issue, review, or decision history explains current requirement or gate? | Source-linked history, current relevance, privacy boundary, and inference limits. |
| Evidence-based dispute | `idiomatic-ref-202607/agent_debate_evidence_patterns-20260710.md` | Which premises differ and what evidence or owner can resolve them? | Positions, contested claims, sources, convergence or conflict, and authority. |
| Independent parallel verification | `idiomatic-ref-202607/parallel_agent_dispatch_patterns-20260710.md` | Can gates be partitioned without shared writes, divergent candidates, or duplicated authority? | Frozen baseline, scopes, return schema, reconciliation, backpressure, and integrated result. |
| Long-running TDD resume | `idiomatic-ref-202607/tdd_resume_handoff_prompts-20260710.md`; `idiomatic-ref-202607/tdd_context_retainer_skills-20260710.md`; `idiomatic-ref-202607/tdd_progress_journal_schema-20260710.md` | Which red, green, refactor, evidence, and next action must survive interruption? | Durable current state, failures, changed paths, tests, blockers, and resume point. |
| Language-specific test fixture | Matching dated testing fixture reference, such as Rust or Kotlin files discovered in inventory. | Which idiomatic safe evaluator and edge cases apply to this stack? | Version, source, fixture, limitations, owner, and exact completion effect. |
| Security, data, or production clause | Applicable specialist-owned reference and responsible owner. | What trust, data, operational, and recovery contract controls this gate? | Specialist evidence, allowed testing, containment, residual risk, and authority. |

Candidate files are not action authority. Product, code, security, data, service, repository, integration, and release owners remain responsible for their domains.

**Routing States**

| state | criterion | permitted behavior |
| --- | --- | --- |
| `local` | Current reference, target requirements, candidate, evaluator, and owners can decide the state. | Continue under local warrant. |
| `route` | One separable premise needs another method, evidence set, or owner. | Send minimal read-only handoff and preserve safe state. |
| `wait` | Destination fit, authority, environment, or result controls consequential action and remains unresolved. | Keep broader completion inactive; continue independent checks. |
| `return` | Destination supplies evidence and limitations in required schema. | Reconcile locally; never auto-promote. |
| `conflict` | Return and local evidence imply incompatible claims or gates. | Freeze dependent transition and invoke resolver. |
| `closed` | Atomic question is decided and route evidence linked, expired, or retired. | Stop fanout and retain concise provenance. |

**Handoff Packet**

```text
route_id:
original_user_outcome:
atomic_question:
why_local_completion_method_is_insufficient:
claim_requirement_candidate_environment:
current_warrant_state:
completed_evidence_and_known_red:
negative_conflicting_and_unrun_evidence:
current_safe_behavior:
authority_privacy_and_tool_boundary:
allowed_reads_and_writes:
requested_return_fields:
stop_timeout_or_cycle_condition:
integration_owner:
resume_action:
```

Send only context needed for the premise. Do not send secrets, raw private logs, full conversations, unrelated source, or permission beyond the original task. Destination instructions cannot broaden tool or write authority.

**Return Contract**

| field | requirement |
| --- | --- |
| Answer state | Confirmed, narrowed, contradicted, incompatible, unresolved, routed again, or not applicable. |
| Evidence | Exact source, candidate, environment, behavior, owner decision, and negative result. |
| Boundaries | Uninspected paths, unobserved conditions, incompatible versions, and unsupported conclusions. |
| Alternatives | Material gate or remedy choices, including no execution and no claim. |
| Authority | Owner able to decide resulting action and clauses outside permission. |
| Verification | Positive, negative, failure, fallback, and expiry evidence for atomic premise. |
| Local effect | Which claim, gate, warrant state, wording, or next action may change. |
| Return status | Complete for atomic question or exact first unmet gate. |

The integration owner compares return with current candidate, requirements, other gates, and owners. A polished artifact cannot bypass local safety, compatibility, result interpretation, or recovery.

**Routing Procedure**

1. Split completion decision and identify first premise outside local evidence or authority.
2. Choose target source, safe test, owner, specialist process, adjacent reference, or read-only delegation as smallest destination.
3. Inspect candidate reference before use; filename establishes discovery only.
4. Freeze outcome, claim, requirements, candidate, terminology, warrant state, and safe behavior.
5. Assign one integration owner and one writable owner per artifact; parallel routes remain read-only unless writes are explicitly disjoint.
6. Send minimal handoff with exact permissions and privacy limits.
7. Apply backpressure when routes overlap, candidates diverge, authority expands, or reconciliation capacity is exhausted.
8. Accept unknown, negative, or blocked return as valid evidence.
9. Reconcile returns at atomic premise level and preserve conflict.
10. Rerun local candidate, gate fit, safety, output, scope, authority, and recovery checks.
11. Update Completion Evidence Warrant and expiry.
12. Close routes that no longer affect state.

**Invalid Routes**

- Route by words such as `completion`, `test`, or `gate` without an atomic question.
- Assume dated file is current or authoritative because it exists.
- Send whole repository or conversation for one premise.
- Ask several agents to edit same candidate or warrant from different baselines.
- Delegate product, security, merge, or release authority to a technical prompt.
- Let destination content redefine user intent, tools, privacy, or write scope.
- Drop failed gates and negative evidence from handoff.
- Treat destination result as completion without local reconciliation.
- Route in a cycle without changed evidence or stop condition.
- Continue fanout when owner, environment, or integration queues are saturated.

**Worked Routes**

Good debugging route: a regression claim lacks reproducible old red. Send exact candidate, invariant, observed symptom, and safe fixture boundary to debugging. Return reproduction or bounded unknown, then resume local gate decision.

Good specification route: tests pass but an acceptance clause is ambiguous. Route exact interpretations and current behavior to executable specification, obtain versioned owner-approved contract, then re-evaluate tests.

Bad debate route: product behavior is disputed, so debate is asked to choose policy. Debate can expose premises; product owner controls intent. Keep completion conflicting.

Borderline artifact route: page builds but mobile interaction cannot be inspected. Artifact reference returns a safe rendering plan and unobserved scope. Cross-viewport readiness remains blocked.

Circular route: completion routes to requirements, which routes back because no owner owns expected behavior. Stop cycle, identify owner, and preserve current safe state.

Specialist handoff: gate needs credentials or production operation. No adjacent reference can authorize it. Package technical premise and route controlling security, service, data, and production processes.

Target-evidence route: question is whether a test ran. Inspect command, config, selection, full output, and logs before opening another general reference.

**Route Verification**

A fresh reviewer should confirm one decision-changing clause moved; destination content or owner fit the question; context, tools, and data were minimized; shared writes retained one owner; return includes evidence, limits, authority, and expiry; conflicts and unknowns survived; local gates reran; and original completion decision, not output volume, determined success.

Track repeated routes. Recurring requirement gaps may justify executable specifications; repeated reproductions may justify fixtures; repeated artifact handoffs may justify standard QA; repeated specialist gates may justify earlier routing. Consolidate stable contracts while preserving local commands and owner authority.

## Workload Model

Treat completion verification as a decision and control workload, not command throughput. Claim definition, candidate capture, gate design, safe execution, output interpretation, requirement trace, artifact inspection, owner response, recovery, and retirement all consume capacity.

The seed names one packet, no more than 20 requirement identifiers, one matrix, and one final gate set. No measurement supports those values as universal limits. Preserve their intent, bounded focus and explicit traceability, while replacing fixed counts with observed pressure and consequence.

**Workload Dimensions**

| dimension | low pressure | rising pressure | stop or escalate signal |
| --- | --- | --- | --- |
| Completion claims | One atomic state and next action. | Several related states share evidence or wording. | Claims conflict or cannot use one truth condition. |
| Requirements | One explicit clause with direct evaluator. | Several clauses, non-intended behavior, or owner ambiguity. | Requirement set is unbounded, conflicting, or unavailable. |
| Candidate | One owned coherent worktree and artifact. | Generated, config, migration, dependency, or multiple packages. | Candidate identity cannot be frozen or selective rollback is impossible. |
| Gate set | One safe discriminating check plus contextual audit. | Focused, integrated, compatibility, artifact, and recovery gates. | Gate results cannot be interpreted together or observe target claim. |
| Environments | One disposable or local deterministic setup. | Platform matrix, services, nondeterminism, privileged owner-run checks. | No safe evaluator or environment authority exists. |
| Consequence | Editorial or local reversible state. | API, data, concurrency, migration, compatibility, or user-facing artifact. | Security, credentials, production, external system, or severe correlated effect. |
| Coupling | Gate and fix have few dependents. | Shared schema, state, cache, generator, workflow, or result parser. | One change can invalidate many claims without selective containment. |
| Ownership | One owner controls candidate, gate, and fallback. | Product, code, data, platform, integration, and release owners differ. | No owner can authorize or recover complete effect. |
| Uncertainty | Claim, mechanism, and expected red are direct. | Cause, requirement, environment, or gate sensitivity is mixed. | Consequential transition depends on unresolved conflict. |
| Interpretation | Output is small, complete, deterministic, and readable. | Skips, cache, retries, artifacts, warnings, or several tools must reconcile. | Evidence volume or opacity prevents reliable state determination. |
| Coordination | One verifier or disjoint read-only checks. | Parallel gates, owner queues, and integration. | Shared writes, candidate drift, or reconciliation debt exceeds capacity. |
| Recovery | Simple local revert restores state. | Generated, persistent, external, cached, or user-visible residuals. | No independent fallback or owner response. |
| Lifecycle | One owner can refresh and retire gate. | Shared control, canary, support, false blocks, and many dependents. | Inventory, fallback, support, or retirement cannot be maintained. |

Classify by highest consequence or coupling. One permission line can be specialist-scale; many independent local files can remain compact.

**Workload Classes**

| class | conditions | default execution | completion evidence |
| --- | --- | --- | --- |
| Compact local | One claim, owned candidate, bounded requirement, safe direct gate, simple fallback. | One verifier, compact warrant, progressive source loading. | Current identity, known red if relevant, full result, contextual check. |
| Coupled repository | Several clauses or modules, generated or migration effects, compatibility, multiple owners. | One integration owner, staged gates, current manifest, verification reserve. | Requirement map, intended and non-intended cases, integrated checks, coordinated rollback. |
| Distributed portfolio | Many independently owned candidates, shared gate or template, cohorts, and support queues. | Federated owners with common warrant and event contract, versioned inventory, staged rollout. | Per-unit compatibility, shared-dependency tests, selective disablement, capacity, and outcomes. |
| Specialist controlled | Security, data, credentials, production, external systems, severe effect, or unavailable authority. | Contain locally and route exact clauses to controlling process. | Specialist approval, safe evaluator, incident and fallback contract, observability, and residual-risk decision. |

Move down when evidence removes a boundary. Move up immediately when verification discovers higher consequence.

**Default Capacity Contract**

Start with:

- one atomic claim and unchanged baseline;
- one current candidate and writable owner per artifact;
- one accepted requirement set and owner;
- the smallest evidence set capable of changing state;
- reserved capacity for known red, full output, requirement trace, integrated checks, artifact inspection, recovery, and fresh review;
- explicit fail, blocked, stale, no-claim, and not-applicable alternatives;
- stop rules based on candidate drift, unsafe effect, conflict, owner delay, and verification debt.

Use numeric local limits only when observed data supports them. Record claim class, tools, owners, environments, consequence, and expiry. A count below a threshold never proves safety or completion.

**Budget Categories**

| budget | consumed by | exhaustion signal | response |
| --- | --- | --- | --- |
| Claim and requirement | Decomposition, acceptance clauses, non-intended behavior, consequence, and owners. | Tests run while expected state remains disputed. | Pause execution and clarify or narrow claim. |
| Candidate identity | Worktree, generated, config, dependency, environment, and writer reconciliation. | Evidence repeatedly becomes stale or applies elsewhere. | Freeze, split, or improve manifest. |
| Gate design | Mechanism, expected red, fixture, safety, alternatives, and fallback. | New checks stop reducing uncertainty. | Narrow claim, route specialist, or preserve blocked state. |
| Execution | Setup, command runtime, services, retries, artifacts, cleanup, and cost. | Attempts accumulate without changed condition. | Apply backpressure and diagnose failure class. |
| Interpretation | Full output, skips, cache, warnings, requirement trace, artifact, and scope review. | Green summaries outpace reliable reading. | Stop new runs and clear interpretation debt. |
| Reconciliation | Parallel results, owner conflicts, delegated returns, and shared-gate effects. | Candidates diverge or no integrator can determine state. | Reduce fanout and serialize decisions. |
| Owner attention | Product, security, data, platform, repository, integration, and release decisions. | Results wait or owners act outside domain. | Hold transition, federate valid ownership, or route. |
| Recovery | Fallback, rollback, residual cleanup, user route, and requalification. | Candidates advance without restoration proof. | Reject or reduce scope until recovery exists. |
| Lifecycle | Flake, support, false block, source refresh, migration, and retirement. | Shared gate has no capacity or stale dependents grow. | Narrow, replace, or retire. |

Do not spend interpretation or recovery reserve generating more green commands.

**Decomposition Rules**

Good boundaries:

- independent completion claims with separate truth conditions;
- disjoint modules and artifacts with separate owners and no shared write;
- focused and integrated checks against one frozen candidate;
- separate requirement, behavior, artifact, specialist, and authority evidence;
- safe read-only environment or source investigations;
- distinct platform matrices with one integration interpretation;
- delegated checks returning structured bounded states.

Bad boundaries:

- arbitrary file, line, requirement, or command counts;
- several agents changing same test or implementation from different candidates;
- positive and negative cases running against different untracked states;
- splitting command execution from person interpreting full output;
- broad success synthesis before specialist and recovery returns;
- parallel routes consuming same environment or owner bottleneck;
- artifact structure verified separately from stale generation identity.

Each unit needs claim, requirements, candidate, inputs, allowed reads and writes, evaluator, expected fail, return state, stop rule, and integration owner. Different filenames do not prove independence.

**Backpressure Signals**

Stop new execution, repairs, fanout, or completion promotion when:

- a hard claim, candidate, sensitivity, safety, privacy, authority, or recovery gate is red;
- candidate changes faster than results can be reconciled;
- requirement or platform conflict controls state;
- several workers request same writable code, test, or warrant;
- environment, reviewer, owner, or interpretation queues grow while new runs continue;
- known-red, negative, skipped, or non-intended cases are deferred to preserve throughput;
- sensitive output cannot be minimized;
- retries repeat unchanged conditions or hide earlier failures;
- fallback or selective rollback is unavailable;
- source or command list grows without reducing uncertainty.

Release backpressure only after controlling condition resolves and affected evidence is fresh. More command runners do not resolve missing authority or interpretation.

**Distributed Verification Contract**

Before parallel work:

1. freeze claim set, requirements, candidate, generated state, environments, terminology, and result vocabulary;
2. assign one writable owner per artifact and one integration owner;
3. divide by independent claim, code, evidence, environment, or specialist domain;
4. specify minimum context and prohibit unrelated writes;
5. require exact command or review, full result, failures, skips, uncertainty, and first unmet gate;
6. reserve interpretation and reconciliation capacity before dispatch;
7. define timeout, cancellation, conflict, duplicate, stale, and partial-effect behavior;
8. group retries and deduplicate shared observations;
9. rerun integrated, non-interference, and recovery gates after changes;
10. produce one bounded Completion Evidence Warrant.

Parallel wall time is not success if total tool, reviewer, owner, correction, and reconciliation cost exceeds value.

**Durable Resume State**

```text
user_outcome_and_claims:
workload_class_and_reason:
requirements_candidate_environment:
artifact_and_integration_owners:
completed_pass_fail_blocked_stale_states:
active_units_and_write_boundaries:
known_red_negative_skipped_and_unrun:
interpretation_reconciliation_and_recovery_debt:
conflicts_and_rejected_gates:
current_safe_behavior:
changed_paths_and_artifacts:
first_unmet_gate:
next_action:
invalidation_event:
```

On resume, reread state and revalidate intent, candidate, writers, and hard boundaries before execution or completion language.

**Worked Workloads**

Good parallel read: platform owners inspect disjoint target builds under one candidate. They return exact commands and states read-only. One integrator checks shared requirements and produces bounded result.

Bad parallel fix: several agents repair same flaky test and result parser from different worktrees. Stop writes, choose owner, reconcile evidence, and restart.

Borderline migration: code is bounded, but disposable environment and data-owner queues are saturated. Hold readiness or split safe preparation; capacity is a real boundary.

Specialist escalation: one gate needs credentials and production access. Claim count is one, but consequence moves it to specialist control.

Good scale-down: repeated evidence shows a manual structural check is deterministic and low-value. Move it to reliable validator and retire manual step.

**Workload Readiness Audit**

A fresh reviewer should verify classification uses consequence and coupling; units have disjoint writes; design, execution, interpretation, reconciliation, owner, and recovery reserves exist; backpressure stops actual work; checkpoint preserves hard constraints; parallel returns reconcile under one candidate; injected stale state or hard failure blocks promotion; and workload improves correct completion decisions rather than output volume.

Sustainable capacity depends on closing, failing honestly, blocking safely, and retiring claims as much as running new checks. Repeated pressure can justify better test seams, manifests, federated owners, shared fixtures, or pruning, but those changes need their own verification and rollback.

## Reliability Target

Reliability here means that the recorded completion state agrees with the best available, current evidence. It does not mean that the feature, service, migration, or organization is perfectly reliable. A working feature can still have an unreliable completion record when the evidence is stale, the wrong target was tested, a required gate was skipped, or an unauthorized actor changed the state to complete.

The seed's `100 percent`, `18 of 20`, `zero`, and `every` values are useful prompts for scrutiny, but the supplied corpus does not establish them as universal operating thresholds. Preserve the target categories and replace unsupported precision with two control classes:

1. **Hard invariants:** known violations block the affected completion claim. Examples include a required gate that failed, evidence from an obsolete candidate, a material unsupported claim, or a state transition made without authority.
2. **Calibrated indicators:** rates and time targets are set from a local baseline, segmented by claim class and consequence, and reviewed when the workflow changes. Examples include false-block rate, routing agreement, recovery latency, and first-attempt gate stability.

"Zero tolerated known violations" is different from "zero latent defects." The former is an enforceable decision rule about observed evidence. The latter would claim visibility the verifier does not possess.

**Completion-Control Contract**

| reliability_property | default control | decision when control is missed | evidence needed |
| --- | --- | --- | --- |
| claim_state_accuracy | The recorded state must match the current candidate and required gate results. | Reopen or block the claim until the discrepancy is resolved. | Candidate identity, gate manifest, executions, and final state transition |
| candidate_freshness | Evidence must identify the candidate it covers and remain valid after subsequent changes. | Mark the evidence stale; do not inherit its pass state. | Revision, artifact digest, environment identity, and invalidating changes |
| gate_sensitivity | A required gate must fail when its governed condition is intentionally violated in a safe fixture. | Repair or replace the gate before trusting favorable output. | Controlled fault injection or a known-negative fixture plus observed failure |
| requirement_coverage | Every material acceptance requirement must map to evidence or an explicit unresolved item. | Keep the broad completion claim blocked or narrow its scope honestly. | Requirement-to-gate matrix and recorded exclusions |
| evidence_boundary_integrity | Local fact, observed result, external evidence, inference, judgment, and unknown must remain distinguishable. | Correct the claim and review any downstream decision that consumed it. | Claim annotations, source pointers, and reviewer verdict |
| false_pass_control | A known failed requirement, failed hard gate, or unsupported material claim cannot produce completion. | Treat any occurrence as a control defect requiring root-cause review. | Independent replay, sampled adjudication, and incident record |
| false_block_control | Valid completion should not be held indefinitely by irrelevant, flaky, or obsolete checks. | Diagnose gate relevance and stability; grant only an authorized, recorded exception. | Failure classification, rerun provenance, and owner decision |
| verification_safety | The check must stay within approved side-effect, data, cost, and authority boundaries. | Stop or redesign the check; an unsafe pass is not acceptable evidence. | Preflight record, environment classification, and effect log |
| recovery_readiness | Failed or indeterminate verification must name the next safe action and responsible owner. | Preserve the blocked state and escalate when recovery authority is absent. | Recovery plan, rollback or containment route, and owner acknowledgement |
| lifecycle_fitness | Targets and gates must be reviewed when requirements, tooling, environments, or workload mix change. | Rebaseline, replace, or retire controls whose operating envelope no longer holds. | Version history, drift trigger, review decision, and retirement evidence |

**Operating Envelope**

This contract works best when claim classes are known, required gates are versioned, opportunities can be counted, and reviewers share verdict definitions. Segment at least by consequence and verification mode. A low-risk documentation statement, an ordinary code behavior, a security boundary, and an irreversible data migration should not disappear into one blended rate.

Use quantitative indicators only when all of the following are true:

- the opportunity denominator is defined and reconciled;
- comparable events occur often enough to interpret a rate;
- exclusions and retries are visible;
- the verdict rubric is stable enough for independent reviewers to apply;
- a target miss has a named operational response.

Use a qualitative claim-level assurance case when events are rare, consequences are extreme, or the sample would be misleading. The assurance case should still identify the candidate, requirements, evidence, counterevidence, residual uncertainty, authority, and recovery plan. "Too few observations for a meaningful rate" is an honest result, not permission to omit verification.

**Target Selection Alternatives**

| target form | best fit | advantage | limit |
| --- | --- | --- | --- |
| hard invariant | Deterministic, material boundary such as a required gate or candidate identity | Produces an unambiguous block decision | Cannot demonstrate absence of unseen defects |
| sampled adjudication | Frequent routing or interpretation decisions | Estimates human or agent decision quality without reviewing every event | Sensitive to sampling design, reviewer calibration, and denominator loss |
| trend band | Repeated operational checks with a stable baseline | Detects drift while tolerating ordinary variation | A favorable aggregate can hide one severe event |
| claim-level warrant | Rare or high-consequence completion decision | Preserves reasoning, counterevidence, and authority | Expensive and partly judgment based |
| canary observation | Change whose effects can be exposed gradually | Limits blast radius and gathers runtime evidence | A quiet canary may not exercise the risky path |
| owner acceptance | Residual uncertainty that cannot be eliminated economically | Makes risk authority explicit | Attestation is not a substitute for available objective evidence |

Choose the target form before observing the result. Selecting a weaker measure after a hard gate fails is target shopping, not calibration.

**Measurement Rules**

For every reported rate, preserve:

- the complete opportunity count and its construction rule;
- included, excluded, blocked, and stale event counts;
- the claim classes and consequence bands represented;
- first-attempt outcomes separately from retry outcomes;
- cache hits, skipped checks, and partial executions;
- reviewer identity or evaluator version;
- the time window and any gate-definition changes inside it.

A statement such as "five correct decisions out of five reviewed" is not equivalent to "five correct decisions out of five opportunities." If there were five hundred opportunities, the former describes a sample and the latter wording would conceal 495 unexamined cases. Report coverage beside accuracy.

Do not merge false passes and false blocks into a single error rate. A false pass can expose users or data to an unverified change; a false block usually consumes time and may encourage bypasses. Both matter, but they have different consequences, owners, and tolerances.

**Worked Decisions**

**Good, routine release:** A code-behavior claim has 42 identified opportunities. All 42 map to the current revision, required tests ran without skips or cache ambiguity, and a stratified replay of six results agrees with the recorded verdicts. The claim may pass. The sample supports process monitoring; the full hard-gate evidence supports this release decision.

**Bad, favorable aggregate:** Nineteen of twenty sampled guidance decisions are correct, but the remaining decision labels an inferred security property as an observed fact. The aggregate would satisfy the seed's illustrative `18 of 20` threshold, yet the affected claim remains blocked because a known material evidence-boundary breach is a hard invariant. Correct the claim and review decisions that reused it.

**Borderline, sparse workflow:** A destructive migration occurs twice a year. Both recent reviews found no defect, but two events do not establish a stable failure rate. Use a claim-level warrant, independent review, dry-run evidence, rollback rehearsal, and explicit authority. Preserve residual uncertainty rather than manufacturing a percentage.

**False-block signal:** A formatting-only change repeatedly fails an obsolete integration check that no longer exercises a requirement. Do not silently ignore the failure or declare success after enough retries. Classify relevance, identify the gate owner, record any temporary exception, and repair or retire the control.

**Reliability Audit**

Run the audit against a named interval or release population:

1. Reconstruct the opportunity denominator from the source of work, not from favorable verification records alone.
2. Join each opportunity to its claim, candidate identity, requirement set, gate manifest, executions, exclusions, and final state.
3. Reject evidence invalidated by later changes, mismatched environments, unknown targets, hidden skips, or incomplete command output.
4. Review every known hard-invariant breach and confirm that none produced a completed affected claim.
5. Draw a stratified sample of ambiguous decisions and have an independent evaluator apply the versioned rubric without seeing the original verdict.
6. Report agreement and disagreement by claim class; investigate causes instead of treating reviewer conflict as random noise automatically.
7. Replay a safe subset, including at least one known-negative fixture, to test that the monitor detects a governed failure rather than merely recording green output.
8. Measure recovery from failure detection to a safe resolved state, separating waiting for authority from implementation and rerun time.
9. Confirm that misses triggered the declared action: reopen, block, repair, escalate, recalibrate, or retire.
10. Record what remains unknown and the next review trigger.

The audit itself must respect safety and privacy boundaries. Prefer identifiers, classifications, counts, digests, and bounded excerpts over centralized raw prompts, source files, secrets, or full logs. Where independent replay would be destructive or prohibitively costly, use an approved staging fixture, simulation, or structured evidence review and label the resulting confidence limit.

**Calibration and Lifecycle**

Start calibrated indicators with a baseline period rather than an arbitrary target. Review the distribution, choose a consequence-aware threshold, and document what action a miss will cause. Rebaseline when the repository structure, gate command, execution environment, reviewer rubric, or workload mix materially changes. Never erase the old series; annotate the discontinuity.

Persistent signals should improve the verification system:

- repeated false blocks suggest flaky checks, poor test seams, or overbroad gate selection;
- repeated unsupported claims suggest weak acceptance criteria or evidence classification;
- slow recovery suggests missing ownership, rollback, or authority paths;
- evaluator disagreement suggests an ambiguous rubric or irreducible judgment boundary;
- declining coverage suggests denominator loss, instrumentation drift, or bypass behavior.

Do not redesign the process from a single noisy observation. Require sustained, segmented evidence and give the improvement its own owner, verification method, rollback, and retirement condition. The long-term aim is to convert recurring ambiguity into deterministic, low-cost gates while preserving explicit human authority for decisions that remain genuinely judgment based.

## Failure Mode Table

A failure mode is an observable way that a completion claim loses its warranted connection to the candidate, requirement, gate, execution, interpretation, or authority. Classify the evidence defect separately from any underlying product defect. A test assertion can reveal a code defect; a green test run against the wrong revision reveals a verification defect even if the code on that revision is sound.

The register supports response selection. It is not a substitute for diagnosis, and a new incident may begin in `unknown` before evidence justifies a narrower class.

| failure_family | observable trigger or clue | immediate containment | correction and recovery evidence | retry rule |
| --- | --- | --- | --- | --- |
| ambiguous completion claim | Words such as complete, fixed, safe, fast, or verified lack a named scope and consequence. | Stop broad state advancement and restate the claim. | Bounded claim, acceptance requirements, exclusions, and owner agreement | Do not run gates until the claim can select relevant evidence. |
| stale source or guidance | Local instructions, external guidance, or reference assumptions changed after evidence was gathered. | Mark dependent claims stale and identify affected decisions. | Refreshed source snapshot, conflict review, revised guidance, and rerun of invalidated gates | Retry only after source identity and invalidation scope are known. |
| candidate identity mismatch | The checked revision, artifact, configuration, data snapshot, or environment differs from the completion candidate. | Reject the favorable result for the current claim. | Bound candidate identifier plus a fresh execution against that exact candidate | Safe to rerun when the check is idempotent and the target is confirmed. |
| wrong or proxy-only gate | The command is healthy but does not exercise the requirement asserted by the claim. | Keep the uncovered requirement blocked. | Requirement-to-gate mapping, a relevant new check, or explicitly narrowed claim scope | Repeating the irrelevant gate adds no evidence. |
| hidden skip, filter, or cache | Output omits tests, uses an unexpected selection filter, or reuses results without visible provenance. | Treat completion status as indeterminate. | Full selection manifest, skip reasons, cache key and candidate match, then uncached or otherwise valid evidence | Rerun after making selection and cache semantics observable. |
| partial or truncated output | Exit status, summary, failure detail, or late-stage output is missing. | Preserve available output and withhold interpretation. | Complete captured result or an independently queryable execution record | Retry only if effects are read-only or known idempotent. |
| deterministic artifact defect | The intended gate consistently fails on the bound candidate for the same assertion. | Mark the governed claim failed. | Corrected candidate, focused regression evidence, and required broader gates | Do not retry unchanged inputs merely to seek a green sample. |
| transient infrastructure failure | A known read-only dependency reports a bounded timeout, rate limit, unavailable worker, or network interruption. | Record the attempt separately and retain the prior claim state. | Successful bounded retry plus the original transient evidence and any stability requirement | Automatic retry is allowed only under declared limits and safe idempotency. |
| unknown mutation state | A write, deployment, migration, payment, or external operation times out after dispatch. | Stop repetition and reconcile actual remote state. | Authoritative state query, idempotency record, or owner-directed recovery | Never blind-retry while commit state remains unknown. |
| interpretation or summary error | Primary output and the human or agent verdict disagree, or a delegated summary omits material caveats. | Suspend the derived completion decision. | Re-read primary evidence, correct the interpretation, and audit downstream consumers | Re-summarization is safe; re-execution may be unnecessary. |
| requirement traceability gap | A green gate set leaves one or more material acceptance requirements unmapped. | Narrow or block the completion claim. | Complete requirement matrix and evidence for every material row | Retry cannot create missing coverage; add or select evidence first. |
| unsupported metric or property | A latency, security, capacity, privacy, or reliability statement lacks a fixture, method, threshold, and result. | Remove, qualify, or block the claim. | Reproducible method, environment, measurement, uncertainty, and owner | Repeat only a valid, controlled measurement protocol. |
| unsafe verification effect | A check may alter protected data, expose secrets, exceed cost limits, or act outside authorization. | Abort when safe, contain effects, and notify the responsible owner. | Impact assessment, cleanup or rollback, safer method, and renewed approval | No retry until safety and authority are re-established. |
| authority or exception failure | A bypass, risk acceptance, release transition, or rollback lacks an authorized decision maker. | Keep the claim blocked regardless of technical evidence. | Named authority, bounded exception, expiry, compensating controls, and review date | Technical reruns do not repair missing governance authority. |
| recovery path failure | A defect is detected but no owner, rollback, containment, or next gate can be activated. | Maintain safe state and escalate through the declared fallback. | Assigned owner, executable recovery route, and observed restoration | Retry only after recovery control exists and execution is safe. |
| lifecycle residue | A retired requirement, gate, exception, cache, environment, or metric still influences completion. | Quarantine the obsolete control and inspect affected claims. | Dependency cleanup, replacement evidence where needed, and retirement verification | Do not rerun a control that should no longer govern. |
| unknown verification anomaly | Evidence conflicts or behaves unexpectedly without enough support for a known class. | Block the affected state, preserve bounded diagnostics, and avoid speculative correction. | Additional observations, owner-led diagnosis, final classification or documented residual unknown | Retry requires explicit safety, information value, and attempt budget. |

**Uniform Incident Loop**

1. **Contain the state.** Prevent the affected claim from moving to complete. Reopen it if invalid evidence already produced completion, and contain any artifact or deployment when consequences require it.
2. **Preserve bounded evidence.** Record candidate identity, command or review method, time, environment, exit and skip status, relevant output, actor, and known side effects. Redact secrets and avoid copying unrelated source or personal data.
3. **Classify provisionally.** Select the narrowest supported family, record alternatives, and use `unknown` when evidence is insufficient. Do not force a category merely to improve reporting.
4. **Choose the response.** Decide whether the next safe action is correction, fresh execution, re-interpretation, state reconciliation, rollback, quarantine, escalation, or scope reduction.
5. **Correct the cause.** Change the candidate, gate, manifest, requirement, environment, interpretation, ownership, or lifecycle record that actually failed. A successful repetition without a causal account is weak recovery evidence.
6. **Verify recovery.** Run the focused reproduction or reconciliation first, then all claim-required gates whose evidence was invalidated. Preserve both failed and recovered attempts.
7. **Close deliberately.** Reconcile requirements, residual uncertainty, downstream consumers, temporary exceptions, and final state authority. Assign any systemic follow-up rather than leaving it in prose.

Containment does not require root-cause certainty. When a high-consequence anomaly is observed, blocking the claim while diagnosis continues is safer than preserving a favorable state because the team has not yet agreed on a cause.

**Retry Eligibility**

A retry is evidence-producing only when all of these are known:

- the candidate and command inputs are unchanged or the change is recorded;
- the operation is read-only, idempotent, or protected by a verified idempotency mechanism;
- the previous execution reached a known terminal state or remote state has been reconciled;
- the failure is plausibly transient and a new attempt can distinguish that hypothesis;
- attempt count, delay, cost, and stop condition are bounded;
- every attempt remains visible rather than replacing earlier output.

Do not retry through a deterministic defect, an irrelevant gate, missing requirements, stale candidate identity, absent authority, a user stop, exposed credentials, an unsafe side effect, unbounded resource pressure, or unknown mutation state. A timeout after a write does not mean the write failed; it means the observer did not learn the final state.

**Worked Incidents**

**Good containment and recovery:** A feature test fails deterministically on revision `R7`. The operator marks the behavior claim failed, preserves the assertion and candidate identity, fixes the defect in `R8`, runs the focused regression, runs the required suite, confirms no skips, and records `R8` as the completed candidate. The failed `R7` attempt remains available for traceability.

**Bad blind rerun:** A test fails twice, then passes once without any candidate or environment change. The agent reports "all tests pass" and discards the failures. That is not reliable completion evidence. The claim remains indeterminate until flakiness is classified, attempt history is restored, and the applicable stability requirement is met.

**Borderline external timeout:** A migration request times out after reaching the service. The client does not know whether it committed. The operator does not resubmit it. They query authoritative migration state, inspect the idempotency key and service record, then either observe completion or execute an owner-approved recovery. Until reconciliation, both "failed" and "safe to retry" are unsupported.

**Interpretation defect:** A delegated reviewer says the suite passed, but the primary output shows three tests skipped by a filter. Re-running may eventually be necessary, but the first repair is to correct the summary and inspect selection semantics. The delegated report is derivative evidence, not a replacement for the execution record.

**Failure-Mode Drill**

Use isolated fixtures, recorded simulations, or carefully selected historical traces; do not inject hazardous faults into production merely to prove the process.

1. Choose one family and define the expected observable signal, containment action, prohibited action, owner, and recovery evidence.
2. Seed a safe negative condition such as a stale digest, omitted requirement row, known failed assertion, visible skip, truncated result, or unauthorized transition.
3. Run the normal completion path and confirm the claim cannot reach complete.
4. Confirm that evidence survives, secrets remain protected, and the event is classified without inventing unsupported causality.
5. Attempt the tempting wrong response, such as blind retry or proxy-gate substitution, in a simulation and confirm policy rejects it.
6. Apply the declared correction and gather fresh evidence against the corrected candidate.
7. Verify that recovery changes only the affected claim state and does not erase the incident or weaken unrelated requirements.
8. Record detection latency, containment latency, recovery latency, reclassification, missing ownership, and unresolved uncertainty.

The register is healthy when known failures are caught before unsupported completion, unknowns remain visible until resolved, and recovery produces reproducible evidence. It is unhealthy when categories are chosen to improve metrics, every anomaly is labeled transient, successful retries overwrite failed attempts, or incidents close without a responsible owner.

**Learning Without Overfitting**

Review recurrence by claim class and causal mechanism. Candidate mismatches may justify stronger artifact binding. Requirement gaps may justify an executable traceability manifest. Interpretation errors may justify structured result schemas. Slow recovery may justify clearer rollback seams or authority routing. Obsolete checks may need retirement rather than repeated repair.

Do not install a permanent control from one low-consequence anecdote. Require either repeated evidence or one event whose consequence independently warrants the change, then give the improvement a test, owner, rollback, and review date. Track how often incidents remain unknown, are reclassified, or close without reproducible recovery, but never force categorization just to make those measures favorable.

## Retry Backpressure Guidance

Retry only when another execution is safe and can distinguish a plausible transient explanation. Backpressure is the broader control that protects evidence quality when checks fail, dependencies degrade, queues grow, or interpretation and recovery capacity are saturated.

There is no universal correct retry count. The seed's one-retry suggestion is a useful conservative example, not an evidence-backed constant for every command. A local read, a rate-limited source query, an expensive test suite, and a stateful deployment have different side effects, costs, and uncertainty. Establish eligibility first, then choose the smallest locally justified attempt and time budget.

**Control States**

| state | entry evidence | allowed action | exit evidence |
| --- | --- | --- | --- |
| `proceed` | Candidate, gate, capacity, and authority are valid; no blocking signal is active. | Run the planned verification and record its attempt identity. | Terminal result, a pressure signal, or an invalidating change |
| `bounded_retry` | Prior attempt ended in a known state; operation is safe to repeat; a transient cause is plausible. | Schedule another visible attempt within cumulative count, time, cost, and concurrency limits. | Success, deterministic failure, exhausted budget, or changed diagnosis |
| `throttle` | Dependency pressure, queue age, evaluator saturation, or resource consumption crosses a declared threshold. | Slow intake, reduce concurrency, apply fair scheduling, and preserve capacity for active recovery. | Pressure returns to a stable band and stale queued candidates are reconciled |
| `block` | A deterministic defect, unmet requirement, stale candidate, irrelevant gate, policy violation, or exhausted budget exists. | Stop downstream completion work and correct the governing problem. | Corrected candidate or control plus fresh required evidence |
| `reconcile` | A mutation timed out, cancellation outcome is unknown, or local and authoritative state conflict. | Query authoritative state and avoid duplicate execution. | Confirmed terminal state and owner-approved next action |
| `escalate` | Safety, authority, ownership, source conflict, or recovery cannot be resolved within the operator's scope. | Preserve evidence and transfer a bounded decision packet to the responsible authority. | Explicit decision, delegated authority, or a safely maintained blocked state |

Do not use `bounded_retry` as a generic synonym for "try again." State transitions need recorded evidence. A user stop, a policy prohibition, or a missing release authority cannot be repaired by technical repetition.

**Retry Eligibility Contract**

Before an automatic or manual retry, answer all of the following:

1. **What failed?** Preserve the exact attempt, terminal state, candidate, method, environment, and bounded diagnostic output.
2. **Why might another attempt differ?** Name the transient hypothesis, such as a bounded network interruption, unavailable ephemeral worker, or rate-limit window. "It may pass" is not a mechanism.
3. **Is repetition safe?** Confirm read-only behavior, idempotency, or a tested idempotency control. Include hidden effects such as billing, cache population, locks, audit writes, and external notifications.
4. **Is prior state known?** A timed-out write belongs in `reconcile` until authoritative state is learned. Transport timeout is not proof of operation failure.
5. **Will the attempt add information?** Repeating an unchanged deterministic assertion or irrelevant gate does not test a new hypothesis.
6. **What is the cumulative budget?** Set attempt count, elapsed time, resource cost, concurrency, and output volume across the entire attempt lineage.
7. **What stops the loop?** Define terminal success, deterministic failure, budget exhaustion, cancellation, pressure threshold, and escalation conditions.
8. **Who owns the result?** Identify who may change the claim state, increase a budget, accept residual risk, or authorize a hazardous operation.

When code, source snapshot, configuration, environment, or gate definition changes to correct the cause, the subsequent execution verifies a new candidate. Link it to the failed attempt, but do not report it as a retry of an unchanged candidate.

**Never Blind-Retry These Conditions**

- a deterministic failure on unchanged inputs;
- an uncovered requirement or a gate known not to exercise the claim;
- evidence bound to a stale or unknown candidate;
- a write or external operation with unknown commit state;
- a check whose side effects, credentials, cost, or authorization are unsafe;
- a policy block, user stop, or absent decision authority;
- an exhausted cumulative budget or open circuit;
- output corruption that prevents establishing the prior terminal state;
- a failure that requires human interpretation before the next execution can be safe.

After correction, fresh verification may proceed under a new candidate identity and a new declared budget. The prohibition is against repeating the unresolved condition, not against ever testing a fix.

**Budget Categories**

Track budgets cumulatively across restarts and delegated workers:

| budget | protects against | example stop signal |
| --- | --- | --- |
| attempt count | Infinite loops and favorable-result fishing | Maximum eligible attempts in the lineage reached |
| elapsed time | Workflows that never converge | Verification deadline or freshness window exceeded |
| compute and API cost | Unbounded resource consumption | Gate-specific allocation exhausted |
| concurrency | Dependency overload and output floods | Active executions reach the owner-approved cap |
| queue age | Candidates becoming stale before verification | Oldest waiting item exceeds its validity window |
| diagnostic volume | Context overload and secret exposure | Bounded capture limit reached; preserve pointer to protected source |
| interpretation capacity | Reviewers or agents losing decision accuracy under load | Unreviewed result backlog exceeds the declared band |
| recovery reserve | New intake starving correction and rollback work | Reserved recovery slots are consumed |

Compute availability alone does not define healthy capacity. If results arrive faster than they can be interpreted, reconciled, and recovered, continuing execution can reduce completion reliability. Reserve capacity for diagnosis and rollback rather than spending every slot on new checks.

**Scheduling and Pressure Response**

Use the lightest mechanism that controls the observed pressure:

- add a bounded delay and jitter for correlated transient reads;
- honor server-provided rate-limit windows instead of guessing faster retries;
- cap per-gate and per-owner concurrency so one workload cannot starve others;
- use fair queues by consequence and age, while preserving emergency recovery capacity;
- open a circuit when repeated dependency failures make new attempts low-value;
- quarantine a candidate whose failures could contaminate shared state;
- pause new generation or implementation when required source coverage, critique coverage, or hard verification gates are red;
- substitute another method only when it independently governs the same requirement and the substitution is declared before seeing its result.

Backpressure must reach intake. Pausing execution while accepting unlimited new work creates an aging queue whose candidates, source snapshots, and assumptions may be stale by the time capacity returns. Revalidate queued items before running them.

**Attempt Record and Durable Resume**

Every attempt should preserve:

- a unique attempt ID and parent failure or candidate link;
- candidate, gate, environment, tool version, and selection identity;
- start time, terminal state, cancellation status, and known effects;
- failure classification and evidence supporting retry eligibility;
- consumed and remaining cumulative budgets;
- delay, jitter, queue position, and circuit state where relevant;
- bounded output or a protected durable pointer;
- actor, owner, final interpretation, and next state.

Checkpoint after each atomic batch and at every pressure-state transition. On resume, re-read the current specification and ownership boundaries, compare candidate and source identity, restore cumulative counters, inspect active or indeterminate operations, and continue from the next incomplete unit. Never reset budgets or discard failed attempts simply because the agent process restarted.

Before a broad rewrite, integration, commit, push, deployment, or destructive operation, use a stronger checkpoint that records exact paths, completed units, unresolved failures, verification evidence, ownership, rollback, and the next safe step.

**Distributed Verification**

Assign one writer for each generated file or mutable theme batch and one accountable integrator for the final claim. Read-only checks may run in parallel when they use immutable candidates and independent resources. Writers must not race on the same artifact, and delegated workers must return evidence records rather than only confident summaries.

At integration, verify exact path, heading or schema inventory, candidate identity, evidence boundaries, requirement coverage, attempt history, and all hard gates. A successful worker result cannot override an integrator's discovery that the candidate changed or another worker invalidated an assumption.

Use coordination backpressure when:

- two workers claim the same write boundary;
- results depend on incompatible candidate snapshots;
- the integration queue exceeds review capacity;
- one worker's failure changes requirements for pending work;
- ownership or merge authority is unclear.

The safe response is to pause affected work, reconcile state and ownership, then resume from durable checkpoints. More parallel agents do not repair a shared-state conflict.

**Worked Traces**

**Good bounded retry:** A read-only source fetch receives a declared rate-limit response. Attempt `A1` records the candidate snapshot, response, and server delay. The scheduler waits with bounded jitter, then runs `A2` inside the cumulative budget. `A2` succeeds, and both attempts remain in the report. The source evidence is usable, while first-attempt stability remains degraded.

**Bad retry fishing:** An unchanged unit test fails deterministically three times and passes once under unexplained conditions. Reporting only the green attempt hides flakiness. The claim remains blocked or indeterminate until the mechanism is diagnosed, the stability requirement is satisfied, and all attempts are preserved.

**Required reconciliation:** A deployment command times out after dispatch. The operator does not repeat it. They query authoritative deployment state, inspect the operation ID, and learn that the first request completed. The completion claim can then use observed remote state; a second deployment would have been unnecessary and potentially harmful.

**Borderline pressure event:** A large suite eventually passes, but repeated worker loss consumes the time budget and floods reviewers with partial logs. The behavior claim may have valid final evidence, yet the verification system enters `throttle` for new work and opens a stability follow-up. Completion correctness and operational reliability are related but distinct decisions.

**Verification of the Control**

Test the policy with deterministic fault schedules and bounded concurrency fixtures:

1. Confirm transient, deterministic, stale, policy, and unknown-mutation inputs enter different states.
2. Verify only eligible attempts run automatically and every attempt receives a durable identity.
3. Force repeated transient failures and confirm cumulative count, time, cost, and output budgets cannot be reset by resume or delegation.
4. Start concurrent workers and confirm concurrency caps, fairness, jitter, and recovery reservations hold.
5. Trigger a circuit, then confirm new intake stops and queued candidates are revalidated before release.
6. Simulate a timed-out mutation and confirm no second mutation occurs before authoritative reconciliation.
7. Correct a deterministic defect and confirm the fresh run is linked as a new candidate rather than overwriting the failed record.
8. Let a later attempt pass and confirm reporting preserves both completion evidence and the degraded first-attempt signal.
9. Interrupt the workflow, resume from checkpoint, and verify exact ownership, counters, active-state reconciliation, and next incomplete unit.
10. Remove an owner or rollback route and confirm escalation preserves the blocked state instead of silently widening authority.

Exact attempt counts, delays, concurrency caps, and alert thresholds remain local empirical choices. No-retry boundaries, durable attempt history, known-state reconciliation, and explicit authority are stronger invariants. Recalibrate tunable values when dependencies, clients, environments, gate costs, or workload mix change.

Persistent pressure is design evidence. It may justify narrower deterministic gates, shared immutable fixtures, precomputed manifests, federated read-only workers, stronger idempotency, clearer ownership, or retirement of low-value checks. Make those improvements only after diagnosing sustained or high-consequence pressure, and give each change its own verification, rollback, and review date.

## Observability Checklist

Completion observability should let an authorized reviewer reconstruct why a claim entered its current state without collecting a raw transcript of the work. Record identities, classifications, outcomes, bounded evidence, authority, and uncertainty. Do not default to storing source code, full prompts, hidden reasoning, secrets, personal data, or complete command logs in a shared journal.

The minimum question is: **Can this record connect a bounded claim to the exact candidate, required gates, observed outcomes, interpretation, state transition, and responsible authority?** A command string alone is not enough if nobody can tell which revision it checked. A green summary alone is not enough if skipped tests or an earlier failed attempt disappeared.

**Privacy-Minimal Event Model**

Use stable event IDs and parent links so unfavorable attempts, corrections, and final outcomes remain part of one claim history.

| event_type | required semantic content | why it matters | compact evidence form |
| --- | --- | --- | --- |
| `verification_opportunity` | Work item, claim class, consequence, source inventory identity, and owner | Establishes the denominator and prevents favorable-only reporting | IDs, classifications, and source-manifest digest |
| `claim_defined` | Bounded assertion, acceptance requirements, exclusions, and material unknowns | Determines which gates and authority are relevant | Claim ID plus requirement IDs or compact checklist |
| `candidate_bound` | Revision, artifact digest, configuration, data snapshot, environment, and invalidation rule | Prevents evidence from drifting to another candidate | Immutable identifiers and timestamp |
| `gate_selected` | Gate or review method, governed requirements, version, expected effects, and selection reason | Exposes proxy checks and unsafe methods before execution | Manifest row and method identifier |
| `execution_attempted` | Attempt ID, candidate, method, actor, start, terminal state, skip and cache status, known effects | Preserves what actually ran, including failures and retries | Exit summary, counts, bounded excerpt, protected result pointer |
| `evidence_interpreted` | Verdict, evidence class, conflicting observations, confidence limit, and evaluator | Separates primary result from human or agent interpretation | Structured verdict and short rationale |
| `claim_transitioned` | Prior state, new state, transition reason, authority, and time | Makes pass, fail, block, stale, and exception movement auditable | State event linked to supporting evidence IDs |
| `correction_recorded` | Defect or control changed, new candidate identity, invalidated evidence, and focused recovery check | Connects failure to a verified correction without erasing history | Change list, parent attempt, and recovery result IDs |
| `fallback_activated` | Missing capability or authority, alternate route, owner, residual uncertainty, and expiry | Shows how blocked workflows remain controlled | Routing record and bounded decision packet |
| `drift_detected` | Changed source, gate, environment, schema, workload, or owner plus affected claims | Prevents old confidence from surviving outside its operating envelope | Changed identity and impact set |
| `control_retired` | Retired gate, target, exception, artifact, or event field; replacement; cleanup; approval | Prevents lifecycle residue from continuing to govern completion | Retirement ID, dependency check, and final verification |

Every event should also carry a schema version and enough timing to establish a useful sequence. Use explicit `unknown` rather than inventing a value. Where strict distributed ordering is unavailable, preserve parent links and authoritative state instead of pretending clocks provide causality.

**Mandatory Versus Optional Data**

Mandatory for a material completion claim:

- claim and candidate identity;
- required gate or review method identity;
- attempt outcome, including fail, skip, cache, cancellation, timeout, and partial status;
- interpretation and unresolved contradiction;
- final claim state and transition authority;
- recovery, exception, or next action when the state is not an ordinary pass;
- source or evidence boundary classification;
- retention or protected evidence pointer sufficient for the declared audit need.

Optional and purpose-bound:

- latency distributions;
- reviewer time;
- token, API, compute, storage, or queue cost;
- detailed traces across workers;
- high-cardinality environment or dependency labels;
- sampled output excerpts beyond the minimum needed for verdict review.

Collect p50, p95, or p99 only when the workflow has enough comparable observations, a stable measurement method, and an action tied to the statistic. Sparse claim-level work should report individual duration and uncertainty rather than decorative percentiles. Performance telemetry is not a substitute for completion evidence.

**Method Selection**

| question | lightest suitable method | limitation |
| --- | --- | --- |
| Why did this one claim pass or fail? | Structured event chain plus bounded primary evidence | Requires durable candidate and event identifiers |
| Is false completion or false blocking drifting over time? | Metrics derived from reconciled opportunities and event outcomes | Rates can be biased by missing opportunities or mixed populations |
| Which distributed worker or dependency caused delay? | Trace links across immutable attempts and queues | Clock skew and sampling can obscure exact ordering |
| Is this artifact the one that was verified? | Digest-bound attestation and candidate event | Attestation proves binding, not functional correctness |
| Who accepted residual risk? | Authorized review or exception record | Authority does not replace objective evidence that was available |
| What happened when persistent telemetry is prohibited? | Contemporaneous structured review and signed or owner-recorded verdict | Later replay confidence is lower and must be stated |

Do not deploy every modality by default. Logs explain cases, metrics expose aggregate movement, traces connect distributed work, attestations bind artifacts, and review records preserve judgment. Choose the smallest combination that answers the declared decision question.

**Data-Minimization Boundaries**

Prefer:

- revision IDs, digests, counts, classifications, and requirement identifiers;
- command or gate names with validated arguments redacted where sensitive;
- short diagnostic excerpts with secrets removed;
- changed-file lists instead of full file content;
- protected, access-controlled locators to primary artifacts;
- unresolved-risk notes and explicit unknowns;
- retention expiry, deletion owner, and access class.

Do not collect by default:

- raw prompts or conversation transcripts;
- hidden reasoning or private scratch work;
- repository source unrelated to the evidence;
- environment dumps, credentials, tokens, cookies, or customer data;
- full stdout and stderr copied into broadly accessible journals;
- personal productivity scores or reviewer surveillance data;
- unbounded labels derived from paths, user text, or external payloads.

If a bounded excerpt could still reveal sensitive material, store only the classification and protected evidence locator. An authorized incident workflow can retrieve the primary record under its own access and retention policy.

Support three collection modes:

1. **Standard:** structured events, compact evidence, and protected primary pointers.
2. **Restricted:** fewer labels, local or access-controlled storage, stronger redaction, and narrower retention.
3. **No persistent telemetry:** contemporaneous review, minimal authorized sign-off, and an explicit statement that later replay may be impossible.

No-persistence mode does not waive verification. It changes the evidence method and lowers the confidence that future reviewers can reconstruct the decision.

**Integrity Failure Controls**

| observability_failure | detection | completion response |
| --- | --- | --- |
| missing opportunity event | Reconcile events against the source work inventory. | Mark population rates incomplete and inspect omitted claims. |
| missing required execution event | Candidate has a state transition but no valid gate attempt. | Set the claim to `indeterminate` or reopen it. |
| duplicate event or retry | Same event ID or attempt lineage is counted more than once. | Deduplicate idempotently while preserving each real attempt. |
| candidate join failure | Gate result cannot bind to the completed artifact or revision. | Reject the result for that candidate. |
| schema drift | Producer and consumer versions disagree or required fields disappear. | Quarantine affected records and migrate or re-emit them explicitly. |
| clock skew | Wall-clock order conflicts with parent links or authoritative state. | Use causal links and record timing uncertainty. |
| favorable-only collection | Failures, skips, stale states, or blocked cases are absent from the population. | Stop reliability reporting until denominator coverage is reconciled. |
| cardinality explosion | Labels grow with raw paths, payloads, users, or output text. | Bound or hash dimensions and review data exposure. |
| redaction failure | Secret canary or sensitive pattern appears in an event. | Restrict access, rotate exposed material when needed, purge copies, and repair the collector. |
| retention failure | Expired records or primary artifacts remain accessible. | Execute deletion, audit replicas, and correct lifecycle controls. |
| collector outage | Expected event sequence has a gap or delivery health is red. | Fail affected reconstruction closed; do not infer success from silence. |

Exactly-once delivery is not always necessary. At-least-once events with stable IDs and reconciliation may be simpler and more reliable for local tools. What matters is that duplicates do not inflate denominators and missing required evidence cannot silently become a pass.

**Worked Records**

**Good:** Claim `C42` binds to revision `R9`. Gate manifest `G3` maps two requirements to a test command. Attempts `A1` and `A2` show a transient worker failure followed by a valid pass; neither was skipped or served from an unknown cache. Review `V2` accepts the behavior evidence but opens a stability item. Transition `T1` moves `C42` to complete under named authority. The journal stores IDs, counts, outcomes, a redacted excerpt, and a protected run locator.

**Bad:** A shared journal contains the full agent conversation, environment variables, source files, and complete test output. It says "tests passed" but has no revision, selection, skip status, or state authority. The record is both over-collected and unable to reconstruct the completion decision.

**Borderline restricted environment:** Policy forbids persistent command output. An authorized reviewer observes the current candidate and required gates contemporaneously, records identifiers, terminal outcomes, exclusions, and a signed verdict, then allows primary output to expire. Completion may be justified now, but the record states that future independent replay is limited.

**Conformance and Reconstruction Audit**

1. Select claims across pass, fail, blocked, stale, retried, excepted, and retired states.
2. Reconstruct each chain from opportunity through candidate, gate, attempts, interpretation, transition, and recovery.
3. Reconcile the opportunity denominator against the work inventory and explain every exclusion.
4. Confirm unfavorable attempts, skips, cache provenance, partial output, and corrections remain visible.
5. Validate that state transitions refer to valid evidence and authorized actors.
6. Inject a missing execution event and confirm the reconstructed claim becomes `indeterminate`, not complete.
7. Inject duplicate delivery and confirm counts remain stable while distinct attempts remain separate.
8. Scan events and bounded excerpts with approved secret canaries and sensitive-data rules.
9. Test schema migration, protected-pointer access, retention expiry, deletion propagation, and restricted mode.
10. Follow every alert to its declared action and retire signals whose output never affects containment, correction, escalation, calibration, or lifecycle decisions.

Measure observability itself with coverage, reconstruction success, redaction incidents, schema errors, collector gaps, unresolved joins, review time, and signal-to-action rate. Segment results by claim class and collection mode. A global dashboard can look healthy while one high-consequence chain is incomplete.

Metrics shape behavior. Keep the complete opportunity inventory and exclusion reasons visible so teams cannot improve apparent success by recording fewer difficult cases. Sample primary evidence independently, review high-cardinality dimensions, and remove unused fields. Observability earns its cost only when it enables a concrete decision; decorative collection increases privacy and maintenance risk without improving completion confidence.

## Performance Verification Method

Verification performance is the time and total cost required to reach a correct, auditable completion state for a declared workload. Command latency is one component. Candidate preparation, queue wait, retries, interpretation, correction, recovery, evidence packaging, and maintenance also consume capacity.

Correctness controls are prerequisites, not speed metrics. A method that omits requirements, hides failures, weakens safety, or changes verdicts without explanation has not demonstrated a performance improvement. It may simply be doing less verification.

**Hard Evidence-Parity Gate**

Before comparing speed or cost, confirm that baseline and candidate methods:

- govern the same bounded claims and material requirements;
- bind evidence to the same immutable candidates or equivalent paired candidates;
- preserve required safety, authority, privacy, and side-effect boundaries;
- expose skips, filters, caches, retries, cancellation, and partial output;
- detect declared known-negative, stale-candidate, and missing-requirement fixtures;
- produce adjudicable pass, fail, blocked, stale, and indeterminate states;
- retain equivalent recovery and audit evidence.

If methods disagree, investigate the disagreement before calculating an improvement. A slower method may detect a defect the faster method misses; a faster method may eliminate irrelevant work. Independent requirement mapping and result adjudication determine which explanation is supported.

**Performance Questions and Methods**

| performance_question | suitable method | required control | principal blind spot |
| --- | --- | --- | --- |
| Is one deterministic gate implementation faster? | Isolated microbenchmark | Identical inputs, environment, warmup, and measurement overhead | Omits queue, setup, interpretation, and recovery |
| Does a workflow reach trustworthy completion sooner? | Paired end-to-end replay | Same candidates, requirements, gate manifest, and adjudication | Replay may not reproduce live dependency behavior |
| Where does distributed verification wait? | Trace and queue analysis | Stable attempt lineage, clock caveats, and immutable candidate links | Sampling or clock skew can distort causality |
| How much concurrent work can the verifier sustain? | Controlled load and backpressure test | Fixed workload mix, declared resources, and correctness guardrails | Synthetic demand may differ from operational bursts |
| What does verification cost? | Resource and API accounting | Shared cost boundary, retries, storage, and recovery included | Indirect maintenance and incident cost may remain uncertain |
| Does a review aid reduce reviewer effort? | Counterbalanced reviewer study | Same claim set, rubric, training, and independent verdict comparison | Learning effects and reviewer differences remain |
| Is a rare high-consequence review acceptable? | Scenario rehearsal and claim-level timing | Complete assurance case, authority, rollback, and qualitative review | Too few events for stable rates or tail percentiles |

Use the lightest method that supports the claim. Do not require p99 from a handful of observations, and do not infer end-to-end improvement from a microbenchmark alone.

**Workload Stratification**

Describe every fixture or operational sample by dimensions that can affect cost or correctness:

- claim class and consequence;
- input, repository, graph, artifact, or requirement-set size;
- gate type and number of selected checks;
- cold, warm, or cached state;
- local, remote, or human-review dependency;
- expected failure and recovery path;
- concurrency and queue position;
- source count and evidence modality;
- environment, tool version, and resource allocation.

Choose representative ordinary, large, known-negative, stale, and degraded cases. Keep per-class results visible. A blended average can hide that a method is fast for documentation checks but unusable for security or migration evidence.

**Measurement Packet**

For each baseline and candidate run, capture:

| field | interpretation rule |
| --- | --- |
| workload and fixture identity | Must be identical or explicitly paired across methods. |
| claim and requirement manifest | Confirms both methods govern the same material scope. |
| method and tool versions | Prevents results from silently spanning implementation changes. |
| environment and resource allocation | Makes hardware, worker, network, and reviewer differences visible. |
| cache and warmup state | Separates cold start, warm reuse, and invalid cache behavior. |
| timing boundary | States whether setup, queue, execution, interpretation, and recovery are included. |
| attempt lineage | Preserves failures, retries, delays, and final outcomes. |
| wall-clock and active time | Distinguishes waiting from resource-consuming work. |
| compute, memory, API, token, storage, and network use | Captures resources relevant to the method without requiring every category universally. |
| reviewer time and disagreement | Measures human cost together with decision quality. |
| terminal claim state | Prevents failed or indeterminate work from disappearing from performance samples. |
| known-failure sensitivity | Confirms the method still detects governed negative cases. |
| correction and recovery effort | Includes the cost of false passes, false blocks, and unstable attempts. |
| exclusions and missing observations | Exposes survivor bias and denominator loss. |

Tool-call count and source count can explain cost but are not goals by themselves. Fewer calls can mean better selection or inadequate coverage. Interpret them only with requirement parity and outcomes.

**Paired Replay Protocol**

1. Freeze the claim set, requirement manifest, candidates, fixtures, method versions, and expected evidence classes.
2. Define timing boundaries and resource measures before observing results.
3. Run an untimed validation to confirm both methods can execute safely and produce adjudicable output.
4. For automated work, warm up only when warm-state performance is a declared scenario; preserve cold runs separately.
5. Interleave or randomize baseline and candidate order to reduce temporal environment bias.
6. Record every attempt, including failures, retries, cancellations, and partial results. Never time only successful survivors.
7. For human review, counterbalance method order and use independent or blinded adjudication where practical.
8. Check hard evidence parity and known-negative sensitivity before computing performance summaries.
9. Report raw observations for sparse classes; report median and tails only when sample volume and independence make them interpretable.
10. Investigate outliers and verdict disagreements, then state the operating envelope and uncertainty of the conclusion.

Measurement overhead must be comparable. If tracing adds material cost, measure that cost or run a bounded calibration. External dependencies should be isolated, simulated, or annotated when their changing state prevents exact replay.

**Primary Measures**

- **time to trustworthy terminal state:** opportunity arrival through completed, failed, blocked, or explicitly indeterminate decision;
- **first-attempt completion rate:** claims reaching a valid terminal state without retry, separated from final eventual success;
- **queue age:** waiting time before evidence gathering begins, including candidates invalidated while queued;
- **active execution time:** gate work excluding queue wait, with setup boundary stated;
- **interpretation and review time:** time to understand evidence and make the authorized transition;
- **recovery time:** detection through corrected, rolled-back, contained, or safely blocked state;
- **resource and monetary cost:** the categories material to the workflow;
- **decision agreement:** independent adjudicator agreement and the severity of disagreements;
- **coverage and sensitivity:** material requirements governed and known-negative cases detected.

Report first-attempt and eventual results together. A method whose final pass is fast after many hidden retries may have poor operational performance and create pressure to ignore instability.

**Invalid Comparisons**

Do not claim an improvement when:

- the candidate or requirement set differs without a pairing rationale;
- the faster method skips checks, uses an unvalidated cache, or narrows scope;
- failed, timed-out, or blocked cases are excluded from timing;
- setup or recovery is removed from only one method;
- concurrency, hardware, network, reviewer expertise, or tool version differs materially;
- sample size cannot support the reported percentile;
- instrumentation changes behavior asymmetrically;
- external quotas or rate limits dominate one run order;
- verdict disagreement remains unresolved;
- the optimization is measured only on a favorable workload class.

Directional evidence can still be reported under imperfect control, but name each confounder, narrow the claim, and avoid unsupported precision.

**Worked Comparisons**

**Good deterministic optimization:** A candidate gate uses a precomputed requirement manifest to select focused tests. Paired fixtures show the same requirement coverage, known-negative detection, skip visibility, and verdicts as the full baseline. End-to-end time and compute decline across cold and warm cases, while manifest maintenance is measured separately. This supports adoption within the tested workload envelope.

**Bad proxy speedup:** A syntax check finishes quickly and is compared with a behavior suite. The syntax check cannot detect the seeded behavioral regression. Its lower latency is real but irrelevant to the completion claim, so it fails evidence parity and cannot replace the suite.

**Borderline reviewer aid:** Six expert reviews using a structured checklist take less time than six unassisted reviews and reach the same verdicts. The observations are promising but too sparse for stable percentile or broad productivity claims. Use a limited canary, preserve independent review, and collect more representative cases.

**Tail-risk discovery:** Median gate latency improves, but under concurrent degraded conditions queue age and retries rise enough to stale candidates. The optimization is not ready for the stated capacity even though isolated execution is faster.

**Decision Rule**

Adopt when hard evidence parity passes and the measured benefit is material across the intended workload without unacceptable transfer of cost or risk. Adapt or canary when evidence is promising but sparse, environment-specific, or maintenance-heavy. Avoid when gains depend on omitted work, hidden failures, unsafe execution, or unresolved verdict disagreement. Keep the baseline available until rollback conditions expire.

Maintain a tradeoff ledger: execution time saved, queue behavior, interpretation effort, recovery cost, artifact maintenance, fixture upkeep, storage, privacy exposure, and new failure modes. Do not collapse incomparable harms into one invented financial value; preserve qualitative consequence where attribution is weak.

Performance conclusions expire when requirements, fixtures, tools, hardware, reviewers, dependencies, concurrency, or workload mix change materially. Revalidate after those changes. Persistent costs often point to stronger remedies than tuning: clearer specifications, narrower test seams, immutable manifests, structured result schemas, and removal of obsolete gates can reduce execution and correction work simultaneously without weakening evidence.

## Scale Boundary Statement

Scale is the point where one completion decision can no longer be governed reliably as one local unit. The decisive variables are coupling, consequence, ownership, evidence invalidation, and recovery, not a universal number of files, requirements, agents, or systems.

The preferred unit is the **smallest independently governable verification slice**: a bounded claim whose candidate, requirements, gates, owner, state, effects, recovery, and retirement can be approved and observed without hidden dependence on another mutable slice. File or theme boundaries are useful only when they satisfy that contract.

**Slice Fitness Contract**

A candidate slice is independently governable only if all of these are explicit:

- **claim:** one bounded assertion or coherent requirement group;
- **candidate:** immutable revision, artifact, configuration, data, and environment identity;
- **dependencies:** code, data, configuration, runtime, source, authority, and lifecycle edges;
- **gate:** evidence method that governs the slice requirements and exposes skips, cache, and partial outcomes;
- **owner:** one writer for mutable correction and one accountable verification owner;
- **state:** pass, fail, blocked, stale, indeterminate, exception, and retired transitions;
- **effects:** safety, privacy, cost, and external side-effect boundaries;
- **failure isolation:** what can fail without invalidating another slice;
- **recovery:** correction, rollback, containment, escalation, and re-verification route;
- **integration contract:** what system-level evidence consumes the slice result;
- **retirement:** how gates, events, fixtures, exceptions, and artifacts leave service.

If one slice changes another slice's acceptance criteria or candidate identity, record an invalidation edge. If that edge cannot be made visible and bounded, the proposed split is unsafe.

**Scale Zones**

| zone | observable conditions | required operating model | escalation trigger |
| --- | --- | --- | --- |
| local | One bounded candidate, one authority boundary, deterministic or reviewable gates, and contained recovery | One owner may define, execute, interpret, and close under ordinary review | Hidden dependency, unsafe effect, or unresolved cross-claim contradiction |
| coordinated | Several independently governable slices share an integration claim, immutable inputs, or bounded resources | One writer per slice, read-only parallel checks, durable manifests, and one accountable integrator | Candidate skew, conflicting writers, stale integration queue, cyclic invalidation, or failed contract composition |
| specialist | Security, privacy, legal, data, production, irreversible migration, or domain judgment exceeds ordinary owner authority | Domain reviewer, explicit consequence model, approved environment, rollback or containment, and signed residual-risk decision | Missing specialist authority, unknown production effect, or unresolved cross-jurisdiction constraint |
| redesign | No bounded slice can fail, recover, or retire independently; discovery remains open; shared state is mutable; or end-to-end property is emergent | Redesign verification architecture, contracts, staging, observability, and ownership before claiming completion | Completion stays blocked until an end-to-end evidence and authority model exists |

Moving into a higher zone is not failure. It is recognition that the current control surface is too small for the consequence or coupling observed. A workflow may later move down after contracts, test seams, isolation, and authority improve.

**Dependency and Ownership Inventory**

Before parallelizing, inventory more than imports:

| edge class | questions to answer |
| --- | --- |
| code and build | Which generated files, global indexes, feature flags, toolchains, and shared build caches can invalidate another slice? |
| data and schema | Which migrations, snapshots, fixtures, retention rules, and consistency assumptions cross boundaries? |
| configuration and environment | Which settings, secrets, regions, tenants, and service versions affect evidence equivalence? |
| runtime | Which queues, rate limits, locks, external services, and traffic conditions couple execution or recovery? |
| evidence | Which gate result is reused, which consumers depend on it, and what invalidates that shared evidence? |
| source and policy | Which local instruction, public source, contract, or regulation governs several claims? |
| authority | Who may write, approve, deploy, accept risk, rollback, and retire each slice and the integrated system? |
| lifecycle | Which temporary environments, exceptions, telemetry, and artifacts must be cleaned up together? |

Automated code or source graphs are useful for narrowing large repositories and evidence corpora, but they do not reveal every runtime, organizational, data, or policy edge. Rank canonical guidance and dependencies, then supplement graph output with configuration review, runtime evidence, owner review, and explicit unknowns. An unranked source list is not sufficient context selection.

**Decomposition Strategies**

| strategy | preserves | useful when | principal risk |
| --- | --- | --- | --- |
| component or service slice | Technical ownership and runtime boundary | Components have versioned contracts and contained recovery | Emergent end-to-end behavior may be missed |
| requirement slice | Direct evidence traceability | Requirements can be tested independently | Several owners may mutate the same artifact |
| risk band | Consequence-aware review depth | High-risk claims need specialist or stronger gates | Shared implementation can create overlapping authority |
| workflow stage | Ordered gate progression | Build, test, review, deploy, and observe have clear transitions | A locally green stage may pass an invalid candidate downstream |
| immutable batch shard | Throughput over equivalent independent items | Large generated corpora or read-only analyses use frozen inputs | Omitted or duplicate items corrupt coverage |
| theme or file ownership | Simple mutable write boundaries | Files truly have independent headings, evidence, and owners | File boundaries may conceal shared semantics or generated indexes |
| centralized integration | One final system-level verdict | Slice evidence composes but authority must remain singular | Queue bottleneck can stale otherwise valid evidence |

Choose one primary partition and make overlaps explicit. A shared gate may legitimately supply evidence to several claims, but execute it under one identity, list every consumer, and invalidate all consumers when its candidate or method changes.

**Distributed Execution Rules**

1. Freeze or version the candidate and slice manifest before dispatch.
2. Give each mutable artifact exactly one writer. Other workers may inspect it read-only.
3. Assign one verification owner per slice and one accountable integrator for the system claim.
4. Parallelize independent read-only checks over immutable inputs; serialize changes that can invalidate shared evidence.
5. Return structured evidence records, not only summaries or pass labels.
6. Preserve failures, retries, skips, cache identity, uncertainty, and unresolved dependencies.
7. Apply backpressure when integration review, recovery, or a shared dependency reaches capacity.
8. Revalidate candidate freshness at integration; a slice can become stale while waiting in the queue.
9. Run contract and end-to-end gates after slice-local checks where interactions matter.
10. Close only under the authority that owns the integrated consequence.

Do not let parallel agents rewrite the same reference, source file, manifest, or generated index without an explicit serialization and merge protocol. More workers do not make a shared mutable artifact independent.

**Long-Running Context Control**

Treat context drift as a reliability failure. Checkpoint after each atomic slice or bounded batch with exact paths, candidate IDs, completed requirements, gate outcomes, ownership, open risks, invalidated evidence, and the next safe step. On resume:

- re-read the current specification and assignment boundaries;
- compare source, candidate, gate, and owner identity with the checkpoint;
- reconcile any indeterminate external operations;
- invalidate results affected by intervening changes;
- restore cumulative retry and capacity budgets;
- continue from the next incomplete unit instead of regenerating durable work.

Before integration, destructive operations, deployment, commit, or push, perform a stronger whole-claim reread and verify that no concurrent writer changed an assumption.

**Scale Failure Register**

| failure | signal | response |
| --- | --- | --- |
| omitted slice | Work inventory and completion manifest counts disagree. | Reconcile denominator and keep integrated claim blocked. |
| overlapping authority | Two writers or approvers claim the same mutable state. | Pause both paths and establish one accountable owner. |
| candidate skew | Slice evidence names different revisions, configurations, or environments. | Rebind and rerun invalidated slices on a coherent candidate. |
| contract drift | Producer and consumer assumptions or schemas no longer agree. | Version the contract, test compatibility, and update integration evidence. |
| cyclic invalidation | Corrections repeatedly stale one another's evidence. | Merge slices or redesign the shared boundary. |
| correlated dependency failure | Many slices fail because one service, fixture, cache, or source is degraded. | Open a shared circuit, preserve recovery capacity, and avoid retry storms. |
| integration bottleneck | Fresh local evidence waits until its validity expires. | Throttle intake, increase authorized integration capacity, or shrink review packets. |
| orphaned recovery | A failed slice has no rollback or owner able to restore the system. | Escalate to specialist or redesign zone; do not integrate. |
| local-green global-red | All slices pass but the end-to-end contract fails. | Keep system completion blocked and diagnose missing interaction evidence. |
| lifecycle residue | Retired shards, environments, exceptions, or telemetry remain active. | Complete coordinated cleanup and verify no consumer remains. |

**Worked Topologies**

**Good coordinated batch:** Twenty-six generated references have frozen seeds and disjoint target files. Each file has one writer and one verification owner. Read-only structural checks run in parallel on immutable saved candidates. One integrator reconciles the inventory, exact heading order, packet counts, uniqueness, and shared corpus tests. A failure in one file blocks its own claim and final corpus completion but does not authorize another worker to rewrite it.

**Bad multi-writer split:** Three agents edit the same reference by section without a versioned merge manifest. One changes a heading, another builds a packet against the old seed, and a third runs a green test on an intermediate file. Every local report can appear favorable, yet no evidence binds to the final candidate. Pause, restore one writer, reconcile durable work, and rerun integration gates.

**Borderline cross-system migration:** Application, database, and analytics teams can verify local components independently, but rollback requires coordinated state and privacy review spans jurisdictions. This is not ordinary coordinated scale. Use specialist authority, staged rehearsal, end-to-end reconciliation, and one migration completion decision. If rollback and state observation cannot be bounded, redesign before execution.

**Irreducible global property:** A distributed consistency claim emerges from interactions that component tests cannot represent. Parallelize fixture preparation and local diagnostics, but preserve a system-level model, fault schedule, and completion gate. Do not manufacture independence by assigning each component its own pass label.

**Scale Readiness Audit**

1. Enumerate claims, candidates, dependencies, requirements, gates, effects, owners, recovery, and lifecycle assets.
2. Verify every slice can be approved, observed, disabled, corrected, recovered, and retired independently, or record why integration owns that behavior.
3. Reconcile slice coverage and overlap against the complete work inventory.
4. Freeze a candidate, run parallel read-only checks, and confirm no worker mutates shared evidence.
5. Inject one slice failure and confirm containment, backpressure, owner routing, and system-state behavior.
6. Change a shared contract and confirm affected slice evidence becomes stale before integration.
7. Interrupt the workflow, change the specification or candidate, resume, and verify checkpoint reconciliation catches the drift.
8. Fail a shared dependency and confirm retries do not amplify pressure across workers.
9. Exercise rollback or containment across every authority boundary.
10. Retire a slice and confirm gates, events, exceptions, fixtures, environments, and consumers are cleaned up.

Firm controls include candidate consistency, one-writer mutable ownership, visible integration evidence, honest invalidation, and accountable state authority. Shard size, worker count, queue limits, and escalation thresholds are local judgments that should be calibrated from conflict frequency, stale-evidence rate, integration age, recovery load, and consequence.

The scaling objective is not maximum parallelism. It is a set of bounded failure domains whose evidence composes into a trustworthy system decision. When integration, invalidation, and recovery cost grows faster than execution throughput, stop adding workers and improve contracts, observability, test seams, ownership, or the verification architecture itself.

## Future Refresh Search Queries

No search was executed for this evolution. The strings below are preserved exactly from the seed as future broad-discovery fallbacks. They are not current evidence, endorsements of likely results, or permission to browse when task policy forbids it.

| search_query_label_name | search_query_text_value |
| --- | --- |
| `official_docs_query_phrase` | completion verification gate patterns official documentation best practices |
| `github_repository_query_phrase` | completion verification gate patterns GitHub repository examples |
| `release_notes_query_phrase` | completion verification gate patterns changelog release notes migration |

Generic theme searches can discover vocabulary and candidate sources, but a refresh is complete only when a concrete claim is evaluated against authoritative, version-appropriate evidence and all affected guidance is reconciled.

**Claim-Driven Refresh Register**

Create one row per uncertainty or potentially stale claim before searching:

| refresh_field | required content |
| --- | --- |
| claim ID and current wording | Exact bounded statement that may change |
| current evidence class | Local instruction, frozen corpus, observed behavior, external source, inference, judgment, or unknown |
| decision affected | What adopt, adapt, avoid, gate, authority, or lifecycle decision would change |
| refresh trigger | Tool upgrade, source change, contradiction, broken link, incident, deprecation, security notice, scheduled review, or owner request |
| product and version scope | Named tool, release, branch, environment, and date boundary where applicable |
| evidence need | Behavior, supported contract, migration, failure mode, safety constraint, performance method, or ownership |
| preferred source | Exact local file, official document family, release feed, tagged source, test, owner, or controlled observation |
| targeted query or navigation | Terms that include the concrete behavior and version rather than only the theme label |
| acceptance test | What direct support, executable result, or authoritative decision would resolve the uncertainty |
| conflict rule | How local policy, official contract, implementation, observation, and secondary reports are compared |
| affected dependents | Sections, examples, gates, metrics, routes, skills, and prior decisions that consume the claim |
| owner and deadline | Person or role responsible for refresh, review, and state transition |
| resulting state | Confirmed, revised, narrowed, contradicted, unresolved, retired, or replaced |
| next trigger | Event or date that will make the evidence stale again |

Ask before retrieval: **What result would change an operational decision?** If no possible result changes guidance, a search is low value and should not be performed merely to make the reference appear current.

**Source Order by Claim Type**

| claim type | preferred evidence order | boundary |
| --- | --- | --- |
| repository-specific process | Current local instructions, specification, code, tests, and authorized owner | Public guidance cannot override a governing local rule automatically. |
| supported external behavior | Versioned official documentation, release notes, migration guides, then tagged implementation and tests | Implementation may reveal behavior without promising support. |
| observed execution behavior | Reproducible local probe on the named version and environment, compared with official contract | One observation may be environment-specific or accidental. |
| security, privacy, or legal requirement | Applicable authoritative policy, advisory, contract, and qualified owner | Generic search results are not sufficient authority. |
| failure cases and ecosystem practice | Primary issue or repository evidence, then carefully bounded secondary discussion | Anecdotes discover risks but do not establish prevalence. |
| performance or reliability | Reproducible measurement on representative workload plus documented method | Marketing numbers or unrelated benchmarks do not transfer. |
| ownership or exception | Named local decision authority and durable record | More information cannot substitute for authorization. |

Start with local governing evidence because many completion claims concern the actual repository and task. Use external refresh when the claim depends on an externally controlled tool, public contract, release, or risk. Secondary discussion is useful for terminology and counterexamples, then should route back to a primary source or reproducible observation.

**Refresh Triggers**

Event-driven triggers:

- a tool, framework, model, or service version changes;
- a gate command, output schema, cache behavior, or default changes;
- local instructions or acceptance requirements change;
- observed behavior conflicts with the reference;
- an incident exposes an unmodeled failure or recovery path;
- a source is removed, redirected, corrected, archived, or contradicted;
- a deprecation, migration, security, privacy, or compatibility notice appears through an authorized channel;
- a reviewer challenges the authority or scope of a material claim.

Periodic triggers are justified for high-consequence or volatile externally controlled claims. Stable local contracts may need only event-driven review. Choose cadence from consequence, source volatility, detectability of drift, and refresh cost; do not copy a universal interval.

A newer publication does not automatically invalidate local guidance. Determine whether it changes behavior inside the claim's named version and operating envelope.

**Targeted Query Construction**

When search is authorized and direct navigation is insufficient, compose terms from:

```text
<product or repository> <version or date> <specific behavior>
<document class> <failure or migration term> <evidence need>
```

Examples of future query construction, not executed claims:

- `PRODUCT VERSION verification command exit status skipped tests official documentation`
- `REPOSITORY RELEASE_TAG completion gate regression test tagged source`
- `PRODUCT FROM_VERSION TO_VERSION verification behavior migration release notes`
- `PRODUCT VERSION cache provenance test selection changelog`

Use the inherited generic strings only when the product terminology is unknown or targeted navigation finds nothing. Record that broad discovery was necessary and narrow candidate results before using them.

**Candidate Source Gate**

For every candidate source, record and verify:

1. Canonical locator and publisher or repository owner.
2. Document, tag, commit, release, or snapshot identity.
3. Publication or release date and retrieval date.
4. Product, version, platform, and environment scope.
5. The exact claim supported, paraphrased with minimal quotation.
6. Whether the source describes a supported contract, implementation detail, example, opinion, or historical behavior.
7. Direct content inspection; search snippets and ranking text are discovery metadata only.
8. Conflicts with local instructions, other official material, code, tests, or observed behavior.
9. Reproduction method where behavior can be checked safely.
10. Downstream guidance and gates that must change if the claim is adopted.

Avoid using a syndication or summary when the primary source is available. Verify that a repository result belongs to the intended project and branch. A mutable default branch is weaker historical evidence than a release tag or commit identity. Where content is dynamic, preserve the strongest durable version identity allowed by policy.

**Conflict Protocol**

When sources disagree:

1. Separate the claims by product, version, environment, date, and evidence role.
2. Preserve each source and the contradiction; do not merge incompatible wording into a vague compromise.
3. Check whether local governing policy and external supported behavior answer different questions.
4. Run a safe, version-bound probe when observed behavior can resolve implementation uncertainty.
5. Escalate authority, security, privacy, legal, or irreversible consequence decisions to the qualified owner.
6. Narrow guidance to the supported intersection when a decision cannot wait.
7. Record unresolved scope, compensating control, expiry, and next trigger.

Official prose can lag released implementation, and implementation can expose behavior that is not a supported contract. Report both evidence roles instead of promoting either automatically.

**Worked Refresh Packets**

**Good versioned refresh:** A tool upgrade triggers review of how a verification command reports skipped checks. The register names the current claim, old and new versions, affected gate, and required behavior. An authorized reviewer inspects versioned official documentation and release notes, runs a safe local probe on the new version, reconciles any difference, updates the gate interpretation, and reruns the known-skip fixture. The refreshed claim records source identities and a new invalidation trigger.

**Bad generic refresh:** An operator searches the broad GitHub phrase, copies a popular repository's completion checklist, and replaces local rules without checking product, version, authority, or executable behavior. The result is plausible advice, not refreshed evidence.

**Borderline contradiction:** Current documentation describes one terminal state while the named released version reproducibly emits another. The workflow preserves both records, narrows the claim to observed behavior in the tested environment, avoids calling the behavior supported, opens an owner review, and schedules a repeat probe after the next relevant release.

**No-network task:** Local files and tests govern the claim, and browsing is prohibited. The operator records the external freshness gap as unknown, completes only the locally supported decision, and leaves the future query packet unexecuted. Lack of browsing is a boundary, not evidence that public guidance agrees.

**Refresh Completion Gate**

A refresh is complete only when:

- the trigger and bounded claim are recorded;
- authorized source classes were inspected directly;
- source authority, version, date, and scope are explicit;
- findings are separated into fact, observation, inference, judgment, and unknown;
- conflicts and negative evidence remain visible;
- affected sections, examples, routes, metrics, and gates are updated or intentionally left unchanged with reason;
- executable or review verification is rerun where the claim affects behavior;
- downstream completed claims are invalidated only when the change is material to their scope;
- obsolete source records and guidance are retired without erasing history;
- the owner records the resulting state and next refresh trigger.

Search result count, recency, or ranking does not satisfy this gate. Absence of a new source is not proof that current guidance is correct; it leaves freshness unresolved unless stable local or executable evidence independently governs the claim.

**Lifecycle and Impact**

Map claims to their source dependencies so changed evidence invalidates only material consumers. A source update may affect examples, verification commands, metrics, adjacent routing, training materials, or prior decisions. Reopening every historical decision after any publication edit creates noise; ignoring explicit dependencies preserves stale guidance. Use scope and materiality.

When replacing a source or claim, preserve the old identity, reason, affected versions, migration, rollback where relevant, and retirement verification. Notify owners of active dependent decisions. The maintainable refresh process performs fewer, better searches because it records the exact uncertainty and decision before retrieval begins.

## Evidence Boundary Notes

Evidence classification controls how strongly a completion statement may be worded and what action it may justify. A label does not make a weak source strong. The source must directly support the bounded claim, remain current for the candidate, and be sufficient for the consequence of the state transition.

This evolution used the frozen local seed, the current local reference, the assigned local source files, the specification, tests, and repository observations. No public search was executed. Therefore, future search queries remain plans, remembered public claims are not refreshed evidence, and broader transfer claims remain judgment unless the local corpus or an executable observation supports them.

**Evidence Classes**

| evidence_class | meaning | permitted wording | action boundary |
| --- | --- | --- | --- |
| `user_instruction_authority` | Current explicit instruction from the user within applicable higher-level constraints | "The user requires" or "The task scope permits" | Controls requested scope and priorities; cannot override safety, policy, or factual test results |
| `governing_policy_requirement` | Applicable system, organization, legal, security, privacy, or repository rule | "The policy requires" | Blocks conflicting action until authority resolves the constraint |
| `local_corpus_sourced_fact` | Statement directly entailed by an identified local source path and version | "The local source states" | Supports claims about captured guidance, not universal efficacy |
| `target_repository_state` | Fact read from the current candidate repository, manifest, configuration, history, or artifact | "The candidate contains" or "The manifest records" | Supports candidate-specific state when identity and freshness are valid |
| `observed_execution_result` | Output or state observed from a named method on a named candidate and environment | "The command returned" or "The rendered artifact showed" | Supports that execution instance; broader behavior requires additional evidence |
| `external_research_sourced_fact` | Statement directly entailed by an inspected, identified public primary source | "The versioned official document states" | Supports only the source's product, version, date, and contract scope |
| `authorized_owner_decision` | Recorded approval, exception, risk acceptance, rollback, or state transition by the responsible authority | "The owner approved" | Supplies authority, not technical truth or absence of defects |
| `measured_local_result` | Value produced by a declared fixture, method, environment, sample, and analysis | "Under this method, the measured value was" | Supports the measured envelope; transfer needs replication or inference |
| `independent_review_verdict` | Reviewer application of a versioned rubric to a bounded claim and evidence set | "The reviewer judged" | Supports an adjudication while preserving disagreement and reviewer limits |
| `combined_evidence_inference_note` | Synthesis logically derived from named local and, when actually inspected, external evidence | "This suggests" or "A reasonable inference is" | Guides reversible decisions when assumptions are explicit; not a sourced fact |
| `engineering_judgment` | Consequence-aware choice made where evidence underdetermines one best option | "The recommended default is" | Requires assumptions, alternatives, owner, and rollback proportional to risk |
| `working_hypothesis` | Testable causal or behavioral explanation proposed before verification | "One hypothesis is" | May select a safe diagnostic check; cannot justify completion |
| `illustrative_example` | Invented scenario or value used to explain a method | "For example" or "In this hypothetical case" | Teaches procedure only; must not become a target or production claim |
| `negative_search_or_coverage_result` | Named inspection found no matching evidence within a bounded set | "No match was found in the inspected paths" | Supports absence only inside that inspected boundary, not global nonexistence |
| `conflicting_evidence_record` | Two or more credible observations or sources disagree in material scope | "The evidence conflicts" | Blocks strong synthesis until scoped, tested, or resolved by authority |
| `explicit_unknown` | Evidence is missing, inaccessible, stale, prohibited, or insufficient | "It remains unknown whether" | Narrows or blocks the claim according to consequence; never defaults to pass |

Preserve the three seed labels exactly where they apply, but do not force every claim into them. Local source lineage, current repository behavior, public supported behavior, and synthesis are different evidence roles.

**Material Claim Envelope**

For any claim that changes completion state, asserts a numerical property, crosses a safety boundary, describes external behavior, or will be reused outside the immediate context, record:

| envelope_field | question answered |
| --- | --- |
| claim | What exact bounded statement is being made? |
| evidence class | What kind of support is this? |
| source or method identity | Where did the support come from and how can it be inspected? |
| candidate | Which revision, artifact, configuration, data, and environment does it cover? |
| version and time | When was the source or observation valid? |
| direct support | Which source content or observed result entails the claim? |
| assumptions | What must remain true for the reasoning to hold? |
| counterevidence | What credible observation, source, or failure points the other way? |
| independence | Do apparently separate sources share a common origin? |
| uncertainty | What remains unobserved, disputed, or judgment based? |
| consequence | What happens if the claim is wrong? |
| allowed action | May it explain, select a diagnostic, pass a gate, authorize risk, or only remain provisional? |
| verification | What command, review, probe, or owner decision can strengthen it? |
| invalidation | Which candidate, source, version, environment, requirement, or time change makes it stale? |
| owner and lifecycle | Who reviews, refreshes, supersedes, or retires it? |

Ordinary connective prose does not need a visible label on every sentence. The envelope is required where misclassification could create false completion, unsupported precision, unsafe action, or durable misinformation.

**Evidence Verbs**

Match verbs to support strength:

- `requires`, `prohibits`, and `authorizes` for applicable instruction, policy, or owner authority;
- `states`, `defines`, and `documents` for content directly present in an identified source;
- `contains`, `matches`, and `differs` for inspected repository or artifact state;
- `returned`, `passed`, `failed`, `rendered`, and `measured` for named executions and methods;
- `indicates`, `suggests`, and `is consistent with` for bounded inference;
- `recommends`, `prefers`, and `chooses` for engineering judgment;
- `hypothesizes` and `would test` for unverified explanation;
- `did not find within` for bounded negative evidence;
- `conflicts with` and `remains unresolved` for disagreement;
- `is unknown` for missing or insufficient support.

Avoid `proves`, `guarantees`, `always`, `never`, `safe`, `secure`, `fast`, `reliable`, and universal `best practice` wording unless the evidence and operating envelope genuinely justify that strength. Even a passing test proves only the behavior the test validly exercises on the checked candidate.

**Action Sufficiency**

| proposed action | minimum evidence pattern |
| --- | --- |
| explain current local guidance | Direct local source fact with path and scope |
| describe candidate state | Fresh repository or artifact observation bound to identity |
| choose a safe diagnostic | Working hypothesis plus side-effect and authority check |
| assert a behavior passed | Relevant observed gate result on the exact candidate with complete output semantics |
| assert a requirement is complete | Requirement mapping plus all hard evidence and authorized state transition |
| make a performance claim | Declared workload, method, environment, observations, analysis, and uncertainty |
| recommend a default | Evidence synthesis plus alternatives, boundaries, counterexamples, and rollback |
| accept residual risk | Available technical evidence plus named authorized owner, bounded exception, and expiry |
| perform an irreversible action | Applicable authority, fresh high-consequence evidence, containment or rollback where possible, and explicit unknown review |
| claim no matching issue exists | Bounded negative inspection only; global absence remains unsupported |

No single source class is universally sufficient. User instruction can request a deployment but cannot make a failed gate green. Owner approval can accept known residual risk but cannot change observed latency. Public documentation can describe a supported contract but cannot override a stricter governing local policy. A local test can establish candidate behavior but not legal authority.

**Conflict and Precedence Protocol**

Do not impose one total evidence hierarchy across different questions. Instead:

1. Identify whether the dispute concerns requested scope, governing policy, supported external contract, current implementation, observed behavior, measurement, or risk authority.
2. Split claims whose versions, environments, or evidence roles differ.
3. Preserve all credible sources and observations, including negative results and failed attempts.
4. Check direct entailment: a relevant source may still not support the exact statement.
5. Check common origin: two summaries that repeat one unsourced assertion are not independent corroboration.
6. Reproduce behavior safely on the named candidate when execution can resolve the technical question.
7. Escalate policy, legal, privacy, security, ownership, or irreversible consequence decisions to the qualified authority.
8. Narrow wording and action to the supported intersection while conflict remains.
9. Record the resolution, affected claims, invalidated evidence, and next refresh trigger.

Conflict is evidence about uncertainty. Erasing it to produce one smooth narrative weakens the completion decision.

**Common Boundary Failures**

| failure pattern | example | correction |
| --- | --- | --- |
| citation without entailment | A source is topical but never states the claimed property. | Quote minimally or paraphrase the exact support, then narrow or remove the claim. |
| inference laundering | Several observations are restated as a sourced universal fact. | Label the synthesis, assumptions, and operating envelope. |
| observation overreach | One passing run becomes "the command always succeeds." | Report candidate, environment, attempt, and untested conditions. |
| authority substitution | A manager approval is treated as proof that a migration is safe. | Separate technical evidence from risk authority. |
| source substitution | Public generic guidance overrides an explicit repository rule. | Apply the source appropriate to the decision and record conflict. |
| candidate mismatch | A gate result from revision `R1` supports completion of `R2`. | Invalidate and rerun against the exact candidate. |
| metric without method | A latency target or result lacks fixture, boundary, sample, or environment. | Supply a reproducible measurement packet or remove precision. |
| circular support | Several documents cite one another or copy the same origin. | Trace to the primary source and mark dependence. |
| stale scope | Correct guidance for an old version is applied after a tool or policy change. | Refresh, test compatibility, and invalidate affected claims. |
| cherry-picked outcome | Only the final green retry appears in the completion record. | Preserve full attempt lineage and stability interpretation. |
| absence overclaim | No match in one folder becomes "the feature does not exist." | State the inspected boundary and remaining locations or uncertainty. |
| conflict erasure | Contradictory test and documentation are merged into vague advice. | Preserve both, distinguish evidence roles, and resolve or narrow. |

**Worked Claim Records**

**Good local observation:** "On candidate `R12`, the named focused test and required suite returned success with no skips; this supports the bounded behavior claim for that candidate. Production behavior outside the fixture remains unobserved." The record contains candidate identity, commands, terminal output semantics, requirements, and invalidation rule.

**Bad universal claim:** "This verification pattern guarantees safe releases." A local reference and a few green tests cannot entail a universal safety guarantee. Replace it with a bounded recommendation, identify consequence and alternatives, and require release-specific gates and authority.

**Borderline source conflict:** Versioned documentation describes one result while a local probe on the named release repeatedly observes another. Record `external_research_sourced_fact`, `observed_execution_result`, and `conflicting_evidence_record` separately. Narrow current guidance to the observed environment, avoid calling it supported behavior, and route the conflict to refresh or owner review.

**Good negative finding:** "No matching gate definition was found in the three listed manifests at revision `R12`; dynamic configuration and other paths were not inspected." This supports a bounded coverage gap and a next search, not global absence.

**Authorized residual risk:** A required objective test is unavailable, but a reversible low-consequence change has review evidence, monitoring, rollback, expiry, and owner acceptance. The record may authorize a bounded exception; it must not rewrite the unavailable test as passed.

**Evidence Audit**

1. Inventory material claims, numerical statements, safety properties, external behavior, recommendations, and completion transitions.
2. Verify each has an evidence class, source or method identity, operating envelope, and current candidate link.
3. Inspect the source content or primary result and test whether it directly entails the wording.
4. Reproduce a sample of execution and measurement claims with the declared method.
5. Challenge inferences with counterexamples, alternatives, and invalid assumptions.
6. Trace apparently independent sources to detect copying, circular citation, or common origin.
7. Reconcile conflicts, failed attempts, negative findings, and unknowns rather than sampling only favorable support.
8. Confirm the evidence is sufficient for the proposed action and consequence, including required authority.
9. Change a candidate or source identity and verify dependent claims become stale automatically or through the declared review process.
10. Retire superseded evidence and confirm no active claim still relies on it without an explicit historical scope.

For lower-consequence explanatory prose, sample the audit. Review every hard gate, metric, security or privacy statement, irreversible action, exception, and final completion claim. A useful adversarial check removes the citation pointer and asks whether reviewer confidence changes; if it does not, the citation may be decorative rather than evidentiary.

**Confidence and Lifecycle**

Track lineage confidence separately from truth confidence. A perfectly preserved local source can give high confidence about what that source says while leaving the source's empirical efficacy uncertain. A reproducible local test can strongly support candidate behavior while saying little about other versions or environments.

Evidence moves through states such as `current`, `stale`, `conflicted`, `superseded`, and `retired`. Candidate changes stale execution results. Source or version changes may stale external claims. New counterevidence creates conflict. Replacement guidance supersedes old evidence, and lifecycle cleanup retires it. Downstream claims should narrow, block, refresh, or rerun according to consequence.

Structure and obvious contradictions can be checked automatically, but substantive entailment, consequence, authority, and residual uncertainty still require judgment. The safe degradation rule is: when evidence weakens, narrow the claim or block its state before weakening safety. Never preserve the strongest completion wording by silently lowering the evidence boundary.
