## Section 001: Branch Finish Worktree Patterns

### Question 01: What decision does this reference help make?
- **current_section_observation:** The title names branch finishing and worktrees but does not state that the core decision is how to preserve, publish, integrate, keep, or discard completed work from the repository state that actually exists.
- **supporting_reason:** Finishing is a state transition with consequences for commits, remotes, branches, worktrees, and uncommitted files, so user intent and observed state must govern the path.
- **counterargument_or_limit:** Some requests are only conceptual and should not trigger repository mutation.
- **assumptions_and_boundaries:** Use this reference for completion decisions after implementation work is saved enough to inspect; route unfinished development or conflict resolution elsewhere.
- **revision_decision:** Expand the opening around intent, state discovery, verification, choice execution, and recoverable handoff.
- **additional_insight_to_add:** A branch is not finished merely because coding stopped; it is finished when the chosen outcome and remaining recovery path are explicit.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The bare title supplies no safe ordering for status inspection, tests, user choice, mutation, or cleanup.
- **supporting_reason:** Default to inspect repository and worktree state, separate owned from unowned changes, run relevant checks, honor an explicit user path or present bounded options, execute minimally, and verify the resulting state.
- **counterargument_or_limit:** Repeating an option menu after the user already requested commit, push, or PR creation adds friction and can contradict intent.
- **assumptions_and_boundaries:** Direct requests bypass menu selection but never bypass quality evidence, destructive confirmation, or ownership checks.
- **revision_decision:** State an intent-first workflow that combines the older four-option model with the later Codex direct-request behavior.
- **additional_insight_to_add:** Choice discovery and action safety are independent gates: a clear request can remove ambiguity without making a destructive command automatically safe.

### Question 03: When does the default work well?
- **current_section_observation:** No fit conditions distinguish a finishable feature branch from a dirty, conflicted, detached, or still-developing workspace.
- **supporting_reason:** The workflow works when a branch or worktree can be identified, intended changes can be scoped, relevant verification is known, and the user wants a completion or preservation outcome.
- **counterargument_or_limit:** A checkpoint commit may be useful even when full verification cannot pass, provided the user explicitly understands that it is not release-ready.
- **assumptions_and_boundaries:** Label checkpoint preservation separately from completion and do not claim readiness from a save-only action.
- **revision_decision:** Add positive fit criteria and a distinct checkpoint path.
- **additional_insight_to_add:** The same Git command can mean completion or temporary preservation; the surrounding contract determines which claim is honest.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The title does not exclude active conflict resolution, unfinished implementation, repository repair, release orchestration, or unknown ownership.
- **supporting_reason:** Applying finish commands in those states can hide failures, mix another person's edits, publish the wrong branch, or delete recoverable work.
- **counterargument_or_limit:** State discovery from this reference can still identify the correct adjacent workflow.
- **assumptions_and_boundaries:** Stop before mutation when intent, branch identity, ownership, base, remote, or verification scope remains consequentially ambiguous.
- **revision_decision:** Add stop and route conditions for unfinished, conflicted, detached, shared, and high-consequence release states.
- **additional_insight_to_add:** Refusing to finish an ambiguous branch is not inactivity; it preserves optionality while evidence is gathered.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The title does not compare local merge, push plus pull request, keep-as-is, discard, commit-only preservation, or leaving a worktree attached.
- **supporting_reason:** These paths trade integration speed, reviewability, remote durability, cleanup, reversibility, and coordination risk differently.
- **counterargument_or_limit:** Too many choices can obscure the four default outcomes when the user has not stated a preference.
- **assumptions_and_boundaries:** Keep the four source-backed options as the default menu and treat commit-only or draft publication as explicit direct-request variants.
- **revision_decision:** Preview the option space and make preservation the fallback when cleanup intent is unclear.
- **additional_insight_to_add:** Cleanup is a separate decision from publication; creating a pull request does not by itself imply that the worktree should be removed.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** No warning covers dirty trees, mixed ownership, detached HEAD, stale base assumptions, wrong remotes, linked worktrees, failing merged tests, or the source conflict about PR cleanup.
- **supporting_reason:** Those conditions can turn an ordinary finish path into data loss, incorrect publication, or an unreproducible handoff.
- **counterargument_or_limit:** Exhaustive Git edge-case handling would overwhelm a concise operating reference.
- **assumptions_and_boundaries:** Prioritize conditions that change mutation safety, user intent, or the ability to recover.
- **revision_decision:** Add a state-first warning and explicitly resolve the cleanup conflict in favor of preservation unless the user chooses otherwise.
- **additional_insight_to_add:** A clean `git status` is not sufficient evidence when the branch, upstream, base, or worktree association is wrong.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** The title provides no contrast between safe completion and command-first behavior.
- **supporting_reason:** A good agent scopes changes, runs tests, honors a requested draft PR, and preserves the worktree; a bad agent force-deletes a dirty branch; a borderline agent pushes correctly but assumes `origin` and cleans up without asking.
- **counterargument_or_limit:** Examples cannot encode every repository convention or hosting workflow.
- **assumptions_and_boundaries:** Show the decision variables and verification evidence rather than treating literal commands as universal recipes.
- **revision_decision:** Add concise contrasts here and defer full matrices to the artifact and worked-example sections.
- **additional_insight_to_add:** Borderline completion is dangerous because the visible outcome succeeds while hidden recovery or ownership assumptions are lost.

### Question 08: How can the important claims be verified?
- **current_section_observation:** The title gives no evidence model for readiness or successful branch transition.
- **supporting_reason:** Inspect branch and worktree identity, status, diff scope, upstream and base relationship, relevant tests, intended remote action, and post-action status.
- **counterargument_or_limit:** No generic command set can know every project-specific quality gate or protected-branch policy.
- **assumptions_and_boundaries:** Use repository instructions and user constraints to choose checks, then report uncovered gates rather than inventing a pass.
- **revision_decision:** Establish precondition, action, and postcondition verification layers.
- **additional_insight_to_add:** Verification after mutation matters because a command can succeed while leaving the wrong branch checked out, an unpushed commit, or a still-attached dirty worktree.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The local sources agree on test-first completion, explicit choices, destructive confirmation, and clear handoff, but differ on direct requests and pull-request worktree cleanup.
- **supporting_reason:** The later Codex source explicitly honors a chosen path, while the older source contains internally inconsistent cleanup instructions for the pull-request option.
- **counterargument_or_limit:** Repository-specific instructions may intentionally choose a different cleanup convention.
- **assumptions_and_boundaries:** Treat user and repository policy as authoritative, preserve work by default, and label unresolved source conflict rather than silently selecting convenience.
- **revision_decision:** State the agreement, conflict, and conservative local synthesis in the opening.
- **additional_insight_to_add:** Confidence can be high about the need for confirmation while remaining contextual about the exact branch integration strategy.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The title frames finishing as an endpoint and not as a handoff into review, deployment, later continuation, or cleanup.
- **supporting_reason:** Branch state becomes shared coordination state once it is pushed, merged, retained, or referenced by another person or agent.
- **counterargument_or_limit:** Not every local experiment needs durable organizational metadata.
- **assumptions_and_boundaries:** Scale handoff detail with remote publication, ownership transfer, consequence, and expected delay before reuse.
- **revision_decision:** Frame completion as a verified transition with explicit next owner and remaining work.
- **additional_insight_to_add:** The best finish report minimizes future state reconstruction by naming what changed, where it lives, what was verified, and what remains open.

## Section 002: Source Evidence Mapping Table

### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed lists five local paths and three public links but does not say which source governs direct requests, option selection, worktree creation, cleanup, verification, or repository-specific policy.
- **supporting_reason:** A source map must route each consequential branch action to the evidence that can actually authorize or constrain it.
- **counterargument_or_limit:** A compact finish request may not require consulting every historical variant.
- **assumptions_and_boundaries:** Always inspect current user and repository state; load source variants only where their policy changes the action.
- **revision_decision:** Preserve all rows and add claim-specific authority, duplicate status, conflict notes, and retrieval order.
- **additional_insight_to_add:** Source count overstates independence here because four paths collapse into two byte-identical Claude artifacts.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** Every local row has the same generic usage role and every public row appears equally current.
- **supporting_reason:** Default to explicit user intent and repository instructions, current inspected Git state, the later Codex finish behavior, the Claude finish and worktree procedures, then refreshed public documentation for unresolved platform facts.
- **counterargument_or_limit:** A repository may explicitly invoke the Claude option menu as its governing process.
- **assumptions_and_boundaries:** Local project policy can override the general synthesis when it is current, applicable, and nondestructive.
- **revision_decision:** Add an authority ladder that separates intent, policy, observed state, workflow guidance, and external freshness.
- **additional_insight_to_add:** Commands such as `git status` provide state evidence, while skills provide decision policy; neither substitutes for the other.

### Question 03: When does the default work well?
- **current_section_observation:** The map is well matched to feature-branch completion and isolated worktrees but not every Git lifecycle operation.
- **supporting_reason:** Its local sources cover tests, base discovery, four finish outcomes, direct requests, worktree placement, ignore safety, setup, baseline tests, and handoff reporting.
- **counterargument_or_limit:** They do not fully define protected-branch policy, force-push governance, release trains, submodules, or multi-repository publication.
- **assumptions_and_boundaries:** Route missing operational authority to repository policy or the relevant platform workflow.
- **revision_decision:** Add positive scope and explicit evidence gaps.
- **additional_insight_to_add:** A source map can be complete for one decision surface while remaining intentionally incomplete for adjacent Git administration.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The flat table can count duplicates as corroboration and hides the older source's contradictory pull-request cleanup instructions.
- **supporting_reason:** Treating repeated text as independent agreement or silently choosing one conflicting line can justify destructive cleanup without user intent.
- **counterargument_or_limit:** Duplicate current paths remain useful because an active workflow may refer to them directly.
- **assumptions_and_boundaries:** Preserve duplicate paths for retrieval while collapsing their evidentiary weight and recording conflict at the claim level.
- **revision_decision:** Add duplicate lineage and contradiction handling around the table.
- **additional_insight_to_add:** Internal contradiction within one source cannot be resolved by counting another identical copy as a second vote.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The seed omits current repository instructions, local Git help, remote configuration, hosting CLI state, branch-protection policy, and user confirmation as evidence types.
- **supporting_reason:** Those sources answer project convention, installed semantics, actual destination, platform workflow, authorization, and intent questions more directly.
- **counterargument_or_limit:** Loading every evidence type can delay an ordinary commit or push.
- **assumptions_and_boundaries:** Retrieve only evidence that can reverse or constrain the requested state transition.
- **revision_decision:** Add source-type routing and a stop rule based on decision impact.
- **additional_insight_to_add:** Destructive intent is not inferable from documentation; only the user's explicit confirmation can authorize discard.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Path presence can masquerade as source inspection, archives can appear stale by location alone, public URLs can imply freshness, and current copies can imply independent authority.
- **supporting_reason:** These mistakes produce confident guidance without proving applicability to the checked-out repository or installed tools.
- **counterargument_or_limit:** Stable hashes and paths still support reproducible review.
- **assumptions_and_boundaries:** Record identity, content role, inspection status, applicable claim, and known conflict for selected evidence.
- **revision_decision:** Add evidence hygiene for duplicates, versions, public pointers, and environment state.
- **additional_insight_to_add:** An archive can preserve the exact governing instruction for a historical workflow, while a current path can still be semantically obsolete.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** No scenario demonstrates how the map changes a branch-finishing decision.
- **supporting_reason:** Good use combines a direct draft-PR request, scoped status, tests, and Codex handoff guidance; bad use follows the older cleanup step blindly; borderline use cites GitHub Actions for local branch readiness without repository checks.
- **counterargument_or_limit:** A single repository can intentionally clean PR worktrees through automation.
- **assumptions_and_boundaries:** Accept that behavior only when current policy and postcondition evidence make it explicit.
- **revision_decision:** Add selection examples tied to user intent, local state, source conflict, and external limits.
- **additional_insight_to_add:** The borderline case becomes valid when the automation is inspected as project policy rather than treated as a universal Git rule.

### Question 08: How can the important claims be verified?
- **current_section_observation:** The table offers labels but no path, identity, content, freshness, or claim-trace gate.
- **supporting_reason:** Verify local existence and hashes, read complete sources, compare duplicate pairs, map conflicting instructions, inspect live repository state, and record public access status.
- **counterargument_or_limit:** Hash equality proves byte identity but not current authority or correctness.
- **assumptions_and_boundaries:** Combine deterministic identity checks with semantic and repository-state review.
- **revision_decision:** Add inventory, policy, state, and reader-action verification layers.
- **additional_insight_to_add:** A reverse trace from each destructive command to explicit authorization catches advice that is well sourced but still unauthorized.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** All local files were inspected, two pairs are byte-identical, and the Codex file differs; no public source was opened during this task.
- **supporting_reason:** Local hashes and complete reads establish content identity and the cleanup contradiction directly.
- **counterargument_or_limit:** Which workflow is canonical for a future repository remains dependent on its active instructions and user request.
- **assumptions_and_boundaries:** State content facts confidently, label authority synthesis as contextual, and retain public links as unrefreshed.
- **revision_decision:** Add a current evidence ledger and avoid present-tense public claims.
- **additional_insight_to_add:** Confidence in a source's bytes, interpretation, applicability, and normative precedence should be recorded separately.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The source map is static and does not show which decision rules or recovery steps depend on each artifact.
- **supporting_reason:** Changes to direct-request behavior, cleanup policy, worktree ignore safety, or hosting workflows affect different sections and fixtures.
- **counterargument_or_limit:** A full provenance graph may be excessive for five local paths.
- **assumptions_and_boundaries:** Maintain lightweight claim-to-section dependencies and expand only when variants proliferate.
- **revision_decision:** Add targeted refresh and conflict-regression guidance.
- **additional_insight_to_add:** Deduplicated provenance reduces maintenance because one semantic change can update all aliases without rereading them as independent evidence.

## Section 003: Pattern Scoreboard Ranking Table

### Question 01: What decision does this reference help make?
- **current_section_observation:** The scoreboard ranks source mapping, evidence separation, and verification but does not say whether 95, 91, and 88 measure safety, confidence, effectiveness, or adoption order.
- **supporting_reason:** The useful decision is which controls remain mandatory when a branch finish must be completed quickly without losing state or authority boundaries.
- **counterargument_or_limit:** User intent, dirty-state ownership, destructive confirmation, and postcondition checks are not represented in the three generic rows.
- **assumptions_and_boundaries:** Treat scores as inherited corpus priority metadata rather than measured Git reliability or universal weights.
- **revision_decision:** Preserve all numbers and tiers, define their status, and attach each row to branch-specific evidence and failures.
- **additional_insight_to_add:** The scoreboard controls information quality, while state safety controls mutation; a safe finish requires both systems.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** All rows say default adoption without a branch-finishing execution loop.
- **supporting_reason:** Map user, repository, and source authority; separate observed state from policy and inference; choose the least surprising authorized path; then verify preconditions and postconditions.
- **counterargument_or_limit:** A failed test or dirty-state discovery may require returning to implementation rather than continuing the loop.
- **assumptions_and_boundaries:** Stop at the smallest failed dependency and route it instead of treating the sequence as inevitable progress toward mutation.
- **revision_decision:** Add an iterative intent-to-state-to-action-to-postcondition workflow around the three rows.
- **additional_insight_to_add:** A control is operational only when its failure can prevent, narrow, or reverse the proposed action.

### Question 03: When does the default work well?
- **current_section_observation:** The scoreboard provides no proportionality guidance for a local checkpoint versus a shared pull request or discard.
- **supporting_reason:** All three controls are especially valuable for remote publication, integration, cleanup, and any path containing unowned or destructive state.
- **counterargument_or_limit:** A clean local commit on an isolated branch may need only compact evidence.
- **assumptions_and_boundaries:** Scale documentation depth with consequence while retaining status, ownership, and relevant verification.
- **revision_decision:** Add light, shared, and destructive operating modes.
- **additional_insight_to_add:** The cost of reconstructing intent rises after publication, so shared outcomes deserve stronger evidence than ephemeral local preservation.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The patterns can become checkboxes: paths can be listed without reading, labels can decorate unsupported claims, and commands can pass on the wrong branch.
- **supporting_reason:** Formal compliance does not protect work unless evidence changes the selected state transition.
- **counterargument_or_limit:** Even shallow checks can catch obvious omissions and improve review.
- **assumptions_and_boundaries:** Count a pattern as applied only when it affects authority, scope, action, confidence, or completion status.
- **revision_decision:** Add misuse signals and semantic acceptance criteria.
- **additional_insight_to_add:** A verifier that ignores branch identity can confidently validate the wrong checkout.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The scoreboard omits state-first inspection, least-destructive defaults, explicit authorization, transaction-style preconditions, and recovery-first planning.
- **supporting_reason:** Those patterns directly reduce Git mutation risk but add discovery and reporting steps.
- **counterargument_or_limit:** Excess ceremony can make straightforward direct requests feel obstructed.
- **assumptions_and_boundaries:** Compress evidence presentation, not the safety decisions that determine recoverability.
- **revision_decision:** Add complementary branch-operation controls and consequence-based overrides.
- **additional_insight_to_add:** A concise direct path can still be rigorous when state and authorization are already known and recorded.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Precise scores can be mistaken for empirical success rates, confidence levels, or permission to follow a higher row over a destructive guardrail.
- **supporting_reason:** That interpretation can turn corpus ordering into unsafe command precedence.
- **counterargument_or_limit:** Stable numeric metadata supports deterministic comparison across generated references.
- **assumptions_and_boundaries:** Preserve scores for corpus use and explicitly forbid deriving action safety from them.
- **revision_decision:** Add a score warning and an override hierarchy led by user intent, repository policy, ownership, and data preservation.
- **additional_insight_to_add:** A lower-scored recovery check outranks a higher-scored retrieval convenience whenever work could be lost.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** The rows contain generic prevention targets and no branch finish scenario.
- **supporting_reason:** Good use maps the direct PR request, labels the cleanup conflict, and verifies the pushed branch; bad use lists sources and force-deletes; borderline use runs tests but never checks changed-file ownership.
- **counterargument_or_limit:** One scenario cannot represent protected branches, forks, or multiple remotes.
- **assumptions_and_boundaries:** Compare invariant decisions and gates rather than prescribing one command sequence.
- **revision_decision:** Add branch-specific good, bad, and borderline contrasts.
- **additional_insight_to_add:** Borderline cases reveal why test success and repository-state safety are independent dimensions.

### Question 08: How can the important claims be verified?
- **current_section_observation:** The failure-prevention targets lack evidence that they stop wrong-branch publication, mixed commits, or unintended cleanup.
- **supporting_reason:** Use fixtures that alter branch, dirty ownership, upstream, cleanup intent, and test result, then verify that the selected path changes correctly.
- **counterargument_or_limit:** Simulated fixtures cannot cover every Git hosting policy.
- **assumptions_and_boundaries:** Test local decision logic and separately validate platform-specific behavior against current authority.
- **revision_decision:** Attach one discriminating gate and one failure fixture to each pattern.
- **additional_insight_to_add:** A mutation test that removes the cleanup confirmation can show whether review detects unauthorized destruction.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The rows and scores are explicit seed facts, but their provenance and relationship to branch outcomes are not documented.
- **supporting_reason:** The three practices coherently address source, certainty, and verification failures seen in the local corpus.
- **counterargument_or_limit:** Their exact order and adequacy for every repository remain editorial judgments.
- **assumptions_and_boundaries:** State confidence in their local default usefulness without calling them measured safety controls.
- **revision_decision:** Separate inherited ranking, source-supported workflow, and contextual branch policy.
- **additional_insight_to_add:** Future score changes should cite observed failure prevention rather than aesthetic preference.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The scoreboard treats each finish as isolated and omits learning from repeated state mismatches or cleanup reversals.
- **supporting_reason:** Traced failures can reveal weak repository instructions, missing worktree policy, ambiguous remotes, or unreliable finish reports.
- **counterargument_or_limit:** Tracking every local experiment would create low-value noise.
- **assumptions_and_boundaries:** Retain recurrent, shared, destructive, or diagnostically novel cases.
- **revision_decision:** Add lifecycle feedback from failure fixtures to source roles, gates, and scores.
- **additional_insight_to_add:** The durable unit of improvement is the state transition contract, not the exact wording of one finish menu.

## Section 004: Idiomatic Thesis Synthesis Statement

### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed says local first, public second, and verification-backed decisions last, but it does not define the branch state transition this sequence should authorize.
- **supporting_reason:** The thesis should decide whether to save, publish, integrate, preserve, clean, discard, narrow, or stop based on intent and evidence.
- **counterargument_or_limit:** No single thesis can encode every repository's branch protection and release policy.
- **assumptions_and_boundaries:** It governs general completion reasoning while deferring exact platform and project authority.
- **revision_decision:** Replace generic synthesis with an intent-state-verification-transition-postcondition thesis.
- **additional_insight_to_add:** Safe branch finishing is less about reaching a clean tree than preserving the intended ownership and recovery story.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The seed gives retrieval order but no rule for a user who already selected commit, push, or pull request.
- **supporting_reason:** Honor the explicit path after state and quality checks; otherwise offer the four source-backed options and default to preservation when cleanup intent is absent.
- **counterargument_or_limit:** An explicit checkpoint request may intentionally accept failing tests.
- **assumptions_and_boundaries:** Save that state with a clear non-ready label and do not merge or publish it as verified completion.
- **revision_decision:** Add direct-request, option-menu, checkpoint, and least-destructive branches.
- **additional_insight_to_add:** Readiness claims and persistence actions should be decoupled so work can be saved without overstating quality.

### Question 03: When does the default work well?
- **current_section_observation:** The synthesis has no fit criteria for ordinary feature branches and isolated worktrees.
- **supporting_reason:** It works when branch identity, change ownership, relevant checks, target outcome, and recovery path can be established.
- **counterargument_or_limit:** Shared worktrees or long-lived integration branches may have several legitimate owners and policies.
- **assumptions_and_boundaries:** Use repository-specific coordination and avoid unilateral cleanup when ownership is shared.
- **revision_decision:** Add fit conditions and shared-ownership escalation.
- **additional_insight_to_add:** A branch can be technically mergeable and still not be socially or procedurally authorized to merge.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The thesis omits unresolved conflicts, uncertain bases, mixed dirty state, inaccessible remotes, and high-consequence release actions.
- **supporting_reason:** Continuing through those states can publish or remove the wrong work even if generic tests pass.
- **counterargument_or_limit:** A bounded checkpoint may preserve evidence while the blocker is resolved.
- **assumptions_and_boundaries:** Stop completion mutation but permit explicitly requested reversible preservation.
- **revision_decision:** Add pause, checkpoint, route, and recovery outcomes for ambiguous state.
- **additional_insight_to_add:** When uncertainty concerns the destination, preservation is safer than integration; when it concerns content ownership, even committing may need scoping first.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The synthesis omits transaction framing, recovery-first planning, change-set isolation, and review-first publication.
- **supporting_reason:** Those alternatives emphasize atomicity, reversibility, ownership, or collaboration at different costs.
- **counterargument_or_limit:** Treating every Git action as a formal transaction can overcomplicate a small branch.
- **assumptions_and_boundaries:** Use the conceptual precondition-action-postcondition model without requiring heavyweight process.
- **revision_decision:** Add alternatives as reasoning aids and preserve the simple default flow.
- **additional_insight_to_add:** Draft pull requests can increase remote durability and review without asserting merge readiness.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** "Local first" can be misread as local sources always winning, and "verification-backed" can be reduced to tests alone.
- **supporting_reason:** Repository policy, live state, and user authorization can override generic workflow text, while tests do not prove scope or destination.
- **counterargument_or_limit:** The local corpus remains valuable for consistent baseline behavior.
- **assumptions_and_boundaries:** Use it as defaults bounded by current authority and observed state.
- **revision_decision:** Add claim-specific precedence and multidimensional verification.
- **additional_insight_to_add:** A green test suite cannot authorize a push any more than a configured remote can prove the code is ready.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** The seed contains no complete synthesis example.
- **supporting_reason:** Good synthesis follows a requested PR, excludes unrelated edits, verifies checks, pushes the intended branch, and reports preserved worktree state; bad synthesis force-cleans; borderline synthesis creates a PR but calls it release-ready without all gates.
- **counterargument_or_limit:** Project conventions may require cleanup or additional CI after publication.
- **assumptions_and_boundaries:** State current evidence and leave platform-controlled checks unresolved until observed.
- **revision_decision:** Add one direct-request example with explicit confidence and remaining work.
- **additional_insight_to_add:** A truthful finish report can call publication successful while merge readiness remains pending.

### Question 08: How can the important claims be verified?
- **current_section_observation:** "Verification-backed agent decisions" has no trace from intent to final state.
- **supporting_reason:** Verify request, policy, repository identity, scope, tests, selected action, command outcome, postcondition, and recovery path.
- **counterargument_or_limit:** Some hosting outcomes, such as required CI completion, occur asynchronously.
- **assumptions_and_boundaries:** Report pending external gates and do not collapse publication with acceptance.
- **revision_decision:** Add a nine-link transition evidence chain.
- **additional_insight_to_add:** Asynchronous postconditions need an owner and follow-up trigger so pending does not silently become assumed success.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The local sources agree on tests, options, confirmation, and handoff, while direct requests and PR cleanup require synthesis.
- **supporting_reason:** Complete local reads and hashes establish those agreements and contradictions.
- **counterargument_or_limit:** Repository-specific policy can select a different valid outcome.
- **assumptions_and_boundaries:** Present common rules as source-backed and preservation-first conflict resolution as local editorial judgment.
- **revision_decision:** Separate source fact, state observation, user authorization, and synthesized default.
- **additional_insight_to_add:** An explicit evidence boundary makes conservative judgment reviewable rather than disguising it as Git law.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The thesis treats one finish event and not the chain of future review, deployment, continuation, or cleanup.
- **supporting_reason:** Publication and preservation create dependencies for later people and agents who need stable identifiers and state evidence.
- **counterargument_or_limit:** Local throwaway work may never be handed off.
- **assumptions_and_boundaries:** Increase traceability with shared visibility, delay, consequence, and ownership transfer.
- **revision_decision:** Extend the thesis through handoff and eventual cleanup.
- **additional_insight_to_add:** Cleanup should happen when its recovery value has expired, not merely because the initial publication command succeeded.

## Section 005: Local Corpus Source Map

### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed lists five local paths and headings but does not assign claim-level responsibility for finish choice, direct requests, worktree safety, cleanup, or handoff.
- **supporting_reason:** The local map should tell an agent which complete artifact to read for the exact branch lifecycle question at hand.
- **counterargument_or_limit:** Repeating source roles can overlap with the broader evidence table.
- **assumptions_and_boundaries:** This section owns local retrieval detail; the broader table owns external and state evidence relationships.
- **revision_decision:** Preserve every path and add artifact identity, claim scope, exclusion, and conflict guidance.
- **additional_insight_to_add:** Alias-aware retrieval lets workflows keep their expected path without inflating the apparent evidence base.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** Every row says skill entrypoint or reusable prompt, offering no minimum or conditional reading order.
- **supporting_reason:** Read the Codex variant for a direct completion request, the Claude finish artifact for choice and discard behavior, and the worktree artifact when creation, baseline, retention, or removal matters.
- **counterargument_or_limit:** Repository instructions may embed a complete finish procedure and make generic skill loading unnecessary.
- **assumptions_and_boundaries:** Read only enough generic source to resolve unaddressed decisions while retaining current project policy.
- **revision_decision:** Add task-triggered source selection and a stop rule.
- **additional_insight_to_add:** Reading the worktree creation skill at finish time matters because cleanup safety depends on how and where the worktree was created.

### Question 03: When does the default work well?
- **current_section_observation:** The local map assumes ordinary branch and worktree operations using the workflows these skills describe.
- **supporting_reason:** It works for isolated feature development, common base branches, standard remotes, project setup, test baselines, pull requests, preservation, and confirmed discard.
- **counterargument_or_limit:** Bare repositories, submodules, nested worktrees, sparse checkouts, and custom hosting may require different mechanics.
- **assumptions_and_boundaries:** Preserve the decision model and replace commands with verified environment-specific operations.
- **revision_decision:** Add environmental fit and command-portability boundaries.
- **additional_insight_to_add:** A source can supply reliable sequencing even when its literal setup command is wrong for the current project.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The map does not explain what to do when current and archived paths are identical, source instructions conflict, or the active repository rejects a generic default.
- **supporting_reason:** Blind precedence can duplicate work or override a safer current policy.
- **counterargument_or_limit:** Stable duplicate paths can serve different agent ecosystems even with identical content.
- **assumptions_and_boundaries:** Preserve aliases for invocation and resolve semantics once per content identity.
- **revision_decision:** Add alias, conflict, and project-override procedures.
- **additional_insight_to_add:** Canonicality belongs to a decision and environment, not permanently to whichever path appears first in a generated table.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** No local rows cover repository instructions, project test documentation, Git configuration, hosting metadata, or prior handoff notes.
- **supporting_reason:** Those sources can be more current and specific but may omit general safety fallbacks.
- **counterargument_or_limit:** Combining every local artifact can create contradictory or stale instruction layers.
- **assumptions_and_boundaries:** Establish precedence and read only sources relevant to the unresolved action.
- **revision_decision:** Add local evidence gaps and adjacent source routing.
- **additional_insight_to_add:** Prior finish reports are observations of what happened, not automatic policy for what should happen now.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Heading-only reading, alias double counting, archive-age assumptions, command copying, and unresolved cleanup conflict are the main local-map risks.
- **supporting_reason:** Each can produce a confident procedure detached from current state or authority.
- **counterargument_or_limit:** Heading signals still provide fast orientation before complete relevant reading.
- **assumptions_and_boundaries:** Use headings to locate, then read complete applicable sections and inspect live state.
- **revision_decision:** Add anti-anchoring and semantic identity checks.
- **additional_insight_to_add:** The most dangerous copied command is one whose success hides a policy error, such as pushing to the wrong but valid remote.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** The table provides no retrieval examples for actual finish requests.
- **supporting_reason:** Good retrieval uses Codex direct behavior plus worktree safety for a requested PR; bad retrieval reads only discard commands; borderline retrieval follows Claude base detection without checking a repository-specific base.
- **counterargument_or_limit:** A common `main` or `master` heuristic often works.
- **assumptions_and_boundaries:** Treat heuristics as discovery and confirm when the integration target changes consequences.
- **revision_decision:** Add request-to-source examples and verify their unresolved assumptions.
- **additional_insight_to_add:** A borderline heuristic becomes safe when its output is reported as a candidate rather than an established base.

### Question 08: How can the important claims be verified?
- **current_section_observation:** Paths and heading signals are visible, but identity, complete-read coverage, and output mapping are not checked.
- **supporting_reason:** Verify existence, hashes, duplicate pairs, relevant complete sections, source conflicts, and each resulting decision rule against live repository state.
- **counterargument_or_limit:** Revalidating unchanged duplicate files on every use is wasteful.
- **assumptions_and_boundaries:** Cache identity evidence and reopen semantics when hashes or applicable policy change.
- **revision_decision:** Add reproducible local-source and change-impact gates.
- **additional_insight_to_add:** Source identity caching is safe only when the current path still resolves to the recorded bytes.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The complete local contents and duplicate hashes are known, while current canonical precedence depends on the invoking environment.
- **supporting_reason:** The files expose their workflows directly but do not define every repository's policy hierarchy.
- **counterargument_or_limit:** The generated seed labels one archive file canonical and other variants legacy or supporting.
- **assumptions_and_boundaries:** Preserve those lineage labels as seed metadata while making action authority claim-specific.
- **revision_decision:** Separate generated classification from operational precedence.
- **additional_insight_to_add:** A later source may refine user interaction without superseding an older source's detailed worktree mechanics.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The map is file-oriented and not organized around the create-use-finish-clean lifecycle.
- **supporting_reason:** Lifecycle mapping reveals that creation choices determine later cleanup, and finish outcomes determine future retention.
- **counterargument_or_limit:** Another lifecycle layer can repeat the same five paths.
- **assumptions_and_boundaries:** Describe responsibilities by phase without duplicating full inventory rows.
- **revision_decision:** Add lifecycle synthesis and source-change propagation.
- **additional_insight_to_add:** The branch finish reference should remember creation invariants, because cleanup cannot be reasoned about safely from the final branch name alone.

## Section 006: External Research Source Map

### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed maps GitHub Actions, reusable workflows, and a Codex repository instruction path without saying which finish question each can answer.
- **supporting_reason:** External evidence should resolve a named CI, workflow-composition, or repository-instruction uncertainty without authorizing unrelated Git state changes.
- **counterargument_or_limit:** Many branch finishes need no public evidence when local policy and live state are sufficient.
- **assumptions_and_boundaries:** Consult external sources only when their current semantics can reverse readiness, publication, or handoff.
- **revision_decision:** Preserve all URLs and add claim scope, freshness status, and invalid extrapolations.
- **additional_insight_to_add:** Public automation evidence can show a pending gate but cannot determine who owns a dirty file.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** All three rows carry a current-fact label despite the no-browse constraint.
- **supporting_reason:** Use repository and installed evidence first, then official versioned documentation for unresolved platform behavior, and repository examples only at a pinned revision.
- **counterargument_or_limit:** A public repository may expose the exact policy the task asks about.
- **assumptions_and_boundaries:** Inspect its revision and precedence before treating it as applicable authority.
- **revision_decision:** Relabel rows as unrefreshed pointers and add an authority sequence.
- **additional_insight_to_add:** A URL is a retrieval address, not evidence that the current page still supports the seed's assigned role.

### Question 03: When does the default work well?
- **current_section_observation:** The external map is relevant when remote CI or reusable checks affect a pull request's readiness and handoff.
- **supporting_reason:** Official documentation can clarify workflow triggers, reuse behavior, or status semantics after the repository's actual configuration is identified.
- **counterargument_or_limit:** Documentation of platform capability does not prove that a repository enables or requires that capability.
- **assumptions_and_boundaries:** Pair public semantics with inspected local configuration and observed check state.
- **revision_decision:** Add fit conditions and a two-source platform-plus-repository rule.
- **additional_insight_to_add:** Readiness evidence belongs to the intersection of what the platform supports and what the repository configured.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The map can encourage CI documentation to stand in for tests, branch protection, cleanup policy, or user consent.
- **supporting_reason:** Those decisions have different authorities and failure consequences.
- **counterargument_or_limit:** Platform documentation can still explain why a local check is pending or reusable.
- **assumptions_and_boundaries:** State the exact shared mechanism and what remains local.
- **revision_decision:** Add example-versus-authority boundaries and route unrelated Git questions elsewhere.
- **additional_insight_to_add:** If the finish decision remains unchanged after reading a public source, the source likely does not belong in the immediate working set.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The seed omits official Git documentation, installed `git help`, hosting CLI help, remote metadata, workflow files, and branch-protection settings.
- **supporting_reason:** Those alternatives may provide closer, version-specific evidence for mechanics and policy.
- **counterargument_or_limit:** Some protected settings are inaccessible to the agent.
- **assumptions_and_boundaries:** Report inaccessible authority as pending rather than inferring it from generic docs.
- **revision_decision:** Add alternative evidence routes by question type.
- **additional_insight_to_add:** Local command help can establish installed syntax while remaining unable to authorize the intended remote effect.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Public links create risks of stale content, unpinned revisions, cross-repository inference, action-versus-policy conflation, and research sprawl.
- **supporting_reason:** These failures make a finish report look current while its actual repository assumptions remain unverified.
- **counterargument_or_limit:** Stable pointers still help future maintainers begin refresh work.
- **assumptions_and_boundaries:** Record access status, revision, product scope, claim, and local applicability for any public evidence used.
- **revision_decision:** Add freshness and stopping rules.
- **additional_insight_to_add:** Stop research when another source cannot change the action, boundary, postcondition, or recovery plan.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** No bounded external-evidence example appears in the seed.
- **supporting_reason:** Good use checks official Actions semantics after seeing a referenced workflow; bad use says Actions proves the branch is safe to delete; borderline use copies another repository's instructions without confirming local precedence.
- **counterargument_or_limit:** A repository template may intentionally standardize policy across projects.
- **assumptions_and_boundaries:** Require explicit adoption or shared ownership before transferring that policy.
- **revision_decision:** Add good, bad, and borderline uses with local-state pairings.
- **additional_insight_to_add:** External precedent becomes stronger only when the target repository declares the same contract, not when filenames merely resemble each other.

### Question 08: How can the important claims be verified?
- **current_section_observation:** The map records no access date, revision, relevant passage, local workflow file, observed check, or applicability decision.
- **supporting_reason:** A refresh must capture each of those items and trace the resulting finish rule to a precondition or postcondition.
- **counterargument_or_limit:** Full research records are disproportionate for a low-impact explanatory link.
- **assumptions_and_boundaries:** Scale detail to consequence while retaining source identity, date, claim, and applicability.
- **revision_decision:** Add a minimal external-evidence packet and local confirmation gate.
- **additional_insight_to_add:** Verify that removing the public example does not remove the user authorization or live-state evidence needed for the action.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The URLs and intended seed roles are known, but their current content, revision validity, and relevance were not inspected.
- **supporting_reason:** No browsing occurred, so present-tense platform claims would be unsupported.
- **counterargument_or_limit:** Future refresh can make them useful authoritative or illustrative sources.
- **assumptions_and_boundaries:** Preserve them as planned entrypoints and state uncertainty explicitly.
- **revision_decision:** Add a no-browse evidence ledger and prohibit hypothetical citations.
- **additional_insight_to_add:** Confidence in a public source should distinguish reachability, authorship, version, content, and local applicability.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** External evidence is framed as one-time research rather than a volatile dependency on branch finish guidance.
- **supporting_reason:** CI semantics, reusable workflows, repository instructions, and hosting rules can change independently of core Git preservation principles.
- **counterargument_or_limit:** Constant refresh would create unnecessary work for stable local operations.
- **assumptions_and_boundaries:** Isolate volatile platform examples and refresh them on named triggers.
- **revision_decision:** Add modular external dependencies and event-based maintenance.
- **additional_insight_to_add:** Stable finish reasoning should survive replacement of the hosting platform example because intent, ownership, and recoverability are platform-neutral.

## Section 007: Anti Pattern Registry Table

### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed lists three generic documentation failures but does not identify which branch-operation defects block mutation, publication, integration, or cleanup.
- **supporting_reason:** The registry should determine whether a proposed finish is authorized, scoped, verified, recoverable, and safe to execute.
- **counterargument_or_limit:** Treating every style issue as a repository blocker would slow harmless reporting improvements.
- **assumptions_and_boundaries:** Block defects that can change content, destination, ownership, readiness, or recovery; repair lower-impact prose proportionately.
- **revision_decision:** Preserve the generic rows and add branch-specific anti-patterns with severity, detection, and remediation.
- **additional_insight_to_add:** A clean-looking final state can conceal the highest-risk defects because the evidence that was swept away is no longer visible.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** Each seed row has a replacement but no common inspection sequence before a state-changing command.
- **supporting_reason:** Review intent, identity, ownership, scope, quality, target, reversibility, action, and postcondition in that order.
- **counterargument_or_limit:** A direct local save may not require every remote and base check.
- **assumptions_and_boundaries:** Skip only dimensions irrelevant to the requested action and record why.
- **revision_decision:** Add a consequence-scaled anti-pattern review loop.
- **additional_insight_to_add:** The cheapest time to detect wrong scope is before a commit combines changes into a new unit of ownership.

### Question 03: When does the default work well?
- **current_section_observation:** The registry assumes nonmutating discovery can establish enough state to classify risks.
- **supporting_reason:** It works for ordinary repositories where branch, worktree, status, diff, remotes, and checks are inspectable.
- **counterargument_or_limit:** Hosting permissions or branch-protection details may remain hidden until a remote action is attempted.
- **assumptions_and_boundaries:** Distinguish locally verified safety from pending platform acceptance.
- **revision_decision:** Add local and remote review layers.
- **additional_insight_to_add:** A failed publication attempt can be useful evidence without authorizing a broader retry or force operation.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** A fixed registry can miss repository-specific hazards or encourage reviewers to stop after known checks.
- **supporting_reason:** Custom hooks, protected branches, submodules, generated files, and shared worktrees can introduce distinct failure mechanisms.
- **counterargument_or_limit:** Unlimited local exceptions make a common reference hard to use.
- **assumptions_and_boundaries:** Keep a stable core and route project-specific hazards through current instructions and observed failures.
- **revision_decision:** Add extension and unknown-state rules.
- **additional_insight_to_add:** Unknown consequential state should trigger preservation and clarification, not a generic "best effort" finish.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** Remediation alternatives such as pathspec commits, patch staging, temporary checkpoints, draft pull requests, branch copies, and delayed cleanup are absent.
- **supporting_reason:** They preserve different combinations of scope, durability, review, reversibility, and workspace availability.
- **counterargument_or_limit:** Extra branches or checkpoints can create cleanup debt and confusion.
- **assumptions_and_boundaries:** Name temporary state, owner, purpose, and retirement trigger.
- **revision_decision:** Add smallest-safe remediation choices for each failure class.
- **additional_insight_to_add:** A temporary preservation branch is useful only when future reviewers can distinguish it from the authoritative integration branch.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Missing failures include mutation before status, mixed-change commits, wrong branch or remote, assumed base, tests-only readiness, forced menus, automatic cleanup, unconfirmed discard, and unauthorized `.gitignore` commits.
- **supporting_reason:** These can lose work or publish incorrect state even when commands return zero.
- **counterargument_or_limit:** Some repositories explicitly automate these actions.
- **assumptions_and_boundaries:** Automation is acceptable only when current policy, scope, and postconditions are inspectable.
- **revision_decision:** Add these high-impact rows and source-conflict warnings.
- **additional_insight_to_add:** Automation reduces keystrokes, not the need to establish authority and ownership.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** The registry has no before-and-after branch examples.
- **supporting_reason:** Good remediation stages only task paths and preserves the PR worktree; bad behavior runs `git add -A` in a mixed tree and force-deletes; borderline behavior commits an ignore change required by generic setup without user approval.
- **counterargument_or_limit:** `git add -A` is valid when every change is intentionally in scope.
- **assumptions_and_boundaries:** Verify scope from diff and ownership rather than banning a command by spelling.
- **revision_decision:** Add contextual good, bad, and borderline cases.
- **additional_insight_to_add:** Command safety is relational: the same command can be correct in a clean owned tree and destructive in a shared dirty tree.

### Question 08: How can the important claims be verified?
- **current_section_observation:** Existing detection checks path and label presence, not actual branch state or mutation effects.
- **supporting_reason:** Use status, diff, branch, worktree, upstream, remote, test, confirmation, and postcondition fixtures that deliberately vary one risk.
- **counterargument_or_limit:** Automated fixtures cannot prove human ownership or intent.
- **assumptions_and_boundaries:** Pair command evidence with explicit user and repository authorization.
- **revision_decision:** Add semantic and state-based detection for every blocker.
- **additional_insight_to_add:** A dry inspection should predict the changed-file and reference outcome before the real mutation is accepted.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** Test verification, discard confirmation, ignore safety, and worktree preservation concerns are source-backed; severity ordering and conservative conflict resolution are synthesized.
- **supporting_reason:** Complete local sources expose these risks but provide no measured frequency or universal repository policy.
- **counterargument_or_limit:** Rare destructive failures still justify strong prevention.
- **assumptions_and_boundaries:** Prioritize by consequence and recoverability rather than invented prevalence.
- **revision_decision:** Label source-backed rules and contextual risk ranking separately.
- **additional_insight_to_add:** Near misses should be retained when they expose a missing state check even if Git prevented the final deletion.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The registry focuses on one operation and not on anti-patterns copied into scripts, hooks, skills, or team conventions.
- **supporting_reason:** An unsafe cleanup shortcut can propagate across many repositories and bypass individual judgment.
- **counterargument_or_limit:** Shared automation also makes one correction propagate efficiently.
- **assumptions_and_boundaries:** Durable automation needs ownership, fixtures, rollback, and explicit scope.
- **revision_decision:** Add propagation and retirement guidance for operational anti-patterns.
- **additional_insight_to_add:** A repeated manual mistake may signal that the repository should expose a safer command or policy rather than relying on memory.

## Section 008: Verification Gate Command Set

### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed supplies one generated-reference verifier but no gate set proving that a branch or worktree transition is safe and complete.
- **supporting_reason:** The section should decide whether evidence is sufficient to save, publish, integrate, preserve, clean, or discard the observed state.
- **counterargument_or_limit:** A documentation verifier cannot execute or authorize a real repository finish.
- **assumptions_and_boundaries:** Separate reference-file policy from branch-operation evidence and user authorization.
- **revision_decision:** Build two verification ladders: one for this artifact and one for applying it to Git state.
- **additional_insight_to_add:** Passing the reference verifier proves the guide's shape, not that any particular branch is ready.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** No order distinguishes cheap nonmutating discovery from project checks, authorization, mutation, and postconditions.
- **supporting_reason:** Run identity and status checks first, scope the diff, run relevant quality gates, confirm the action, execute minimally, and verify outcome-specific state.
- **counterargument_or_limit:** Some checks are expensive or unavailable before remote publication.
- **assumptions_and_boundaries:** Record pending gates and avoid stronger readiness claims than current evidence supports.
- **revision_decision:** Add an ordered, consequence-aware command and review ladder.
- **additional_insight_to_add:** Cheap-first ordering improves feedback only when later semantic and authorization gates remain mandatory.

### Question 03: When does the default work well?
- **current_section_observation:** Standard Git inspection commands fit ordinary non-bare repositories with accessible worktree and remote metadata.
- **supporting_reason:** They provide reproducible evidence for root, branch, status, diff, worktree, upstream, and remotes before mutation.
- **counterargument_or_limit:** Hooks, submodules, sparse checkout, hosting permissions, and custom tooling can add hidden state.
- **assumptions_and_boundaries:** Extend the ladder through repository instructions and platform-specific checks when those features apply.
- **revision_decision:** Add applicability conditions and extension points.
- **additional_insight_to_add:** Nonmutating Git evidence is necessary but not exhaustive when policy lives outside the object database.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** Blind command execution can run from the wrong worktree, use stale output, expose secrets in remote URLs, or mutate state during supposed verification.
- **supporting_reason:** A verification procedure that changes or leaks state can invalidate its own baseline.
- **counterargument_or_limit:** Some authoritative checks, such as a push or merge test, inherently attempt mutation.
- **assumptions_and_boundaries:** Perform them only after preconditions and authorization, then treat their result as action evidence.
- **revision_decision:** Mark commands as inspect, project-check, mutation, or postcondition and redact sensitive output.
- **additional_insight_to_add:** The shell working directory is part of every Git command's input and must be visible in durable evidence.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** Alternatives include porcelain output, human-readable status, explicit pathspecs, patch review, hosting CLI checks, repository scripts, and manual review.
- **supporting_reason:** They trade stability, readability, scope control, platform coverage, and reviewer effort.
- **counterargument_or_limit:** Porcelain formats remain Git-version contracts, not universal schemas across unrelated tools.
- **assumptions_and_boundaries:** Prefer structured output for automation and concise human views for interpretation.
- **revision_decision:** Add command-choice guidance and coverage limits.
- **additional_insight_to_add:** Pairing a machine-stable inventory with a human diff review provides stronger evidence than either alone.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Likely errors include ignoring exit codes, checking unstaged but not staged changes, omitting untracked files, assuming an upstream, leaking credentials, and treating tests as timeless.
- **supporting_reason:** These can create false green evidence or unsafe logs.
- **counterargument_or_limit:** Capturing every command output verbatim can overwhelm the handoff.
- **assumptions_and_boundaries:** Retain decisive results, exact invocation, target, and unresolved risk rather than raw dumps.
- **revision_decision:** Add completeness, freshness, redaction, and failure-attribution rules.
- **additional_insight_to_add:** Verification evidence should be invalidated when the relevant tree changes after the check.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** The seed shows a command but no pass, fail, or misleading outcome.
- **supporting_reason:** Good evidence names branch, scoped diff, test result, intended push, and verified upstream; bad evidence says "Git clean"; borderline evidence checks status before a later generated file changes.
- **counterargument_or_limit:** Exact output wording differs across Git versions and projects.
- **assumptions_and_boundaries:** Anchor examples to invariant state facts and exit behavior.
- **revision_decision:** Add contrastive verification records with freshness boundaries.
- **additional_insight_to_add:** A formerly green snapshot becomes historical evidence after mutation, not current readiness proof.

### Question 08: How can the important claims be verified?
- **current_section_observation:** The seed does not verify that its archived command exists, that the focused verifier applies, or that branch commands cover claimed invariants.
- **supporting_reason:** Inspect command help and source, run focused policy checks, map each branch claim to an observable command or review question, and test failure fixtures.
- **counterargument_or_limit:** Commands cannot establish human intent or ownership.
- **assumptions_and_boundaries:** Require explicit request and review evidence beside machine state.
- **revision_decision:** Add gate-to-claim coverage and known blind spots.
- **additional_insight_to_add:** Review the assertions inside a verifier before inferring what its successful exit means.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The current focused verifier and archived final-stage interface are locally inspectable, while project-specific test and hosting gates vary.
- **supporting_reason:** Local commands can confirm their accepted arguments but not future compatibility or hidden platform policy.
- **counterargument_or_limit:** Rechecking stable command help for every read adds little value.
- **assumptions_and_boundaries:** Reconfirm when tools, paths, versions, policies, or expected outputs change.
- **revision_decision:** Label command interface observations separately from branch readiness judgment.
- **additional_insight_to_add:** Confidence decays when either repository state or the verifier implementation changes.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** Verification is framed as an endpoint and not as data for improving repository finish automation.
- **supporting_reason:** Repeated wrong-scope, stale-test, or cleanup failures reveal missing checks or unclear policy.
- **counterargument_or_limit:** Adding a gate for every rare event can create slow, ignored pipelines.
- **assumptions_and_boundaries:** Promote recurrent or high-consequence escapes and retire redundant checks.
- **revision_decision:** Add a feedback rule from failures to commands, fixtures, and instructions.
- **additional_insight_to_add:** The best gate set is the smallest maintained set that independently covers every consequential state transition claim.

## Section 009: Agent Usage Decision Guide

### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed says when to consult the reference but not whether the agent should finish, checkpoint, publish, route, or stop.
- **supporting_reason:** Usage must be selected from user intent, implementation state, ownership, consequence, and required authority.
- **counterargument_or_limit:** A task can ask for both conceptual explanation and actual branch mutation.
- **assumptions_and_boundaries:** Separate orientation from execution and make the operational path authoritative for state changes.
- **revision_decision:** Put finishability and artifact routing before command selection.
- **additional_insight_to_add:** Triggering the reference is an invitation to inspect state, not permission to mutate it.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The four seed bullets do not form a complete agent workflow.
- **supporting_reason:** Clarify or infer the requested outcome, read current policy, inspect state and ownership, run applicable checks, follow direct intent or present options, execute minimally, verify, and report.
- **counterargument_or_limit:** Asking about every low-risk detail can frustrate a user who gave a complete direct request.
- **assumptions_and_boundaries:** Ask only for missing facts that could change content, destination, destruction, or readiness claims.
- **revision_decision:** Add an eight-step operating sequence with stop conditions.
- **additional_insight_to_add:** Good autonomy removes redundant choice questions while preserving consequential consent.

### Question 03: When does the default work well?
- **current_section_observation:** Theme and path mentions are broad triggers that do not prove implementation is complete.
- **supporting_reason:** The guide fits completed work, intentional checkpoints, branch publication, local integration, preservation, and explicit cleanup decisions.
- **counterargument_or_limit:** A user may use "finish" to mean finish coding rather than finish the branch.
- **assumptions_and_boundaries:** Resolve the intended deliverable from context or ask when the difference changes action.
- **revision_decision:** Add positive task signals and ambiguity handling.
- **additional_insight_to_add:** Vocabulary is weaker than state and outcome; an agent should route on what must be true afterward.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The seed gives no negative routing signals for conflicts, unfinished work, repository repair, release management, or unowned changes.
- **supporting_reason:** Those tasks require different expertise and stop conditions before ordinary finishing can resume.
- **counterargument_or_limit:** This reference can still preserve a checkpoint and produce a precise handoff.
- **assumptions_and_boundaries:** Do not represent checkpointing as resolution of the underlying blocker.
- **revision_decision:** Add route-away and return conditions.
- **additional_insight_to_add:** A safe handoff should name which failed precondition must become true before branch finishing resumes.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** Nearby workflows such as verification, conflict resolution, worktree creation, GitHub publication, release management, and repository recovery are not compared.
- **supporting_reason:** They own quality, integration repair, isolation, hosted review, deployment, and damaged-state decisions respectively.
- **counterargument_or_limit:** Splitting a small task across many references can fragment context.
- **assumptions_and_boundaries:** Route only when another artifact has distinct authority or verification responsibility.
- **revision_decision:** Add an adjacent-workflow matrix with handoff payloads.
- **additional_insight_to_add:** One finish report can bridge several workflows without absorbing their commands or policies.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Mechanical trigger use can force an option menu, assume origin or main, cleanup after PR, ignore mixed changes, or overclaim tests.
- **supporting_reason:** These errors follow familiar patterns while violating the current request or repository.
- **counterargument_or_limit:** Defaults remain useful when state is conventional and verified.
- **assumptions_and_boundaries:** Use defaults as hypotheses and expose any consequential assumption.
- **revision_decision:** Add assumption checks and direct-request behavior.
- **additional_insight_to_add:** An agent should be predictable in safeguards and adaptable in the exact finish path.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** No request-to-action examples demonstrate agent usage.
- **supporting_reason:** Good use commits and pushes after an explicit request and checks; bad use offers four choices instead of executing; borderline use executes but publishes unrelated changes.
- **counterargument_or_limit:** A direct request may still omit commit scope or remote destination.
- **assumptions_and_boundaries:** Clarify only those missing consequential details and preserve the rest of the request.
- **revision_decision:** Add direct, ambiguous, blocked, and destructive usage scenarios.
- **additional_insight_to_add:** The strongest direct-request behavior is not blind obedience; it is low-friction execution bounded by visible safety gates.

### Question 08: How can the important claims be verified?
- **current_section_observation:** The seed advises verification but does not test correct workflow selection or handoff closure.
- **supporting_reason:** Inspect trigger, requested outcome, preconditions, selected authority, mutation scope, postcondition, and next owner.
- **counterargument_or_limit:** Correct routing can remain judgment when several paths are viable.
- **assumptions_and_boundaries:** Record rejected alternatives and reversal triggers for consequential cases.
- **revision_decision:** Add a routing and execution audit.
- **additional_insight_to_add:** Evaluate success against the state the user requested, not the number of Git commands completed.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** Direct-request behavior, four default options, tests, and destructive confirmation are locally sourced; route thresholds remain contextual.
- **supporting_reason:** The sources define those behaviors but cannot know every project policy or user meaning.
- **counterargument_or_limit:** Excessive qualification can make the guide indecisive.
- **assumptions_and_boundaries:** Give a strong default and name only exceptions that reverse or block it.
- **revision_decision:** Separate firm safeguards from adaptable workflow selection.
- **additional_insight_to_add:** Confidence in route choice should decrease as ownership and destination become less observable.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** Agent usage is framed as one interaction rather than reusable repository behavior.
- **supporting_reason:** Repeated finish requests reveal preferred remotes, checks, worktree retention, and handoff conventions that should live in repository instructions.
- **counterargument_or_limit:** Learning from one request can encode a temporary preference as policy.
- **assumptions_and_boundaries:** Promote only repeated or explicitly approved conventions with an owner.
- **revision_decision:** Add feedback from execution history to maintained policy.
- **additional_insight_to_add:** The reference succeeds at scale when common choices become explicit project defaults and agents reserve questions for true exceptions.

## Section 010: User Journey Scenario

### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed names an unfamiliar user, sources, and a broad decision but does not show how repository state becomes a verified finish outcome.
- **supporting_reason:** A journey should expose discovery, ownership, quality, choice, mutation, postcondition, and handoff states with recovery branches.
- **counterargument_or_limit:** One linear journey can imply that direct requests and ambiguous requests follow the same interaction.
- **assumptions_and_boundaries:** Present a default path plus branches for direct intent, failing checks, mixed changes, conflict, keep, and discard.
- **revision_decision:** Expand the role statement into staged states with observable exits.
- **additional_insight_to_add:** A journey reveals where human authorization enters a technical workflow and cannot be replaced by automation.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** The starting state supplies no order after the reference is opened.
- **supporting_reason:** Frame the requested outcome, inspect authority and state, scope changes, verify quality, choose or confirm the path, execute, verify postconditions, and hand off.
- **counterargument_or_limit:** A direct keep request may require no mutation or expensive test rerun.
- **assumptions_and_boundaries:** Run only checks needed to support the requested claim and confirm that no unintended action occurred.
- **revision_decision:** Add a seven-stage default with consequence-based compression.
- **additional_insight_to_add:** The shortest safe journey is outcome-specific; keeping a branch and merging it do not share the same necessary gates.

### Question 03: When does the default work well?
- **current_section_observation:** The journey assumes accessible Git state and a user or policy able to select the outcome.
- **supporting_reason:** It works for ordinary feature branches and worktrees with inspectable diffs, known project checks, and identifiable remotes or bases.
- **counterargument_or_limit:** Asynchronous review and CI can leave the final acceptance state pending.
- **assumptions_and_boundaries:** End the local journey at verified publication and explicit pending ownership rather than pretending remote completion.
- **revision_decision:** Add local-complete and externally-pending exits.
- **additional_insight_to_add:** A journey can complete its handoff even when the broader integration lifecycle remains open.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** No branch handles unresolved conflict, detached state, mixed ownership, missing remote access, or a requested destructive action with unrecoverable files.
- **supporting_reason:** Continuing can hide or lose the evidence needed to resolve the blocker.
- **counterargument_or_limit:** A checkpoint can improve recoverability before escalation.
- **assumptions_and_boundaries:** Use reversible preservation only after scoping what it will contain.
- **revision_decision:** Add stop, checkpoint, and route branches with return conditions.
- **additional_insight_to_add:** Failed preconditions should redirect the journey to the owner of that state, not merely lengthen the branch-finish checklist.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The seed omits self-service finish, guided option selection, direct execution, review-first publication, and human-administered cleanup journeys.
- **supporting_reason:** They trade speed, user control, remote durability, review, permission, and recovery.
- **counterargument_or_limit:** Too many variants can obscure the standard path.
- **assumptions_and_boundaries:** Branch only where intent, authority, or consequence changes the required evidence.
- **revision_decision:** Add journey variants at explicit decision points.
- **additional_insight_to_add:** Draft-first publication is a useful middle path when work should be durable and visible but not yet represented as merge-ready.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** The scenario does not expose stale status, tests run before final edits, changed upstream, hidden untracked files, cleanup conflict, or lost handoff ownership.
- **supporting_reason:** These failures occur between stages and can invalidate earlier green evidence.
- **counterargument_or_limit:** Rechecking everything after every read-only operation is unnecessary.
- **assumptions_and_boundaries:** Invalidate only evidence affected by a tree, configuration, policy, or destination change.
- **revision_decision:** Add stage-transition invalidation rules.
- **additional_insight_to_add:** Evidence freshness is relational: a test remains current until relevant content or environment changes, while status can change with any file mutation.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** No person or agent completes a real finish journey in the seed.
- **supporting_reason:** A good agent follows a draft-PR request through scoped commit, push, preserved worktree, and pending-CI handoff; a bad agent deletes after push; a borderline agent preserves unrelated files but omits them from the report.
- **counterargument_or_limit:** A single pull-request scenario may overemphasize hosted workflows.
- **assumptions_and_boundaries:** Include local merge, keep, and discard branches as contrasts.
- **revision_decision:** Add a complete primary journey and concise alternative exits.
- **additional_insight_to_add:** A retained unrelated change is safer than a deleted one, but invisible retained state still creates future confusion.

### Question 08: How can the important claims be verified?
- **current_section_observation:** Success is called an executable next step without stage evidence.
- **supporting_reason:** Verify request, repository identity, ownership, scope, checks, action selection, command outcome, postcondition, recovery, and owner at the corresponding stage.
- **counterargument_or_limit:** Capturing every detail can burden a simple local operation.
- **assumptions_and_boundaries:** Reuse concise command summaries and omit irrelevant dimensions with reason.
- **revision_decision:** Attach one pass question and evidence artifact to each stage.
- **additional_insight_to_add:** Stage evidence localizes whether a failure came from wrong intent, stale state, unsafe scope, failed quality, or incorrect mutation.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The source sequence and safeguards are known, while optimal pacing and exact repository commands remain contextual.
- **supporting_reason:** User intent, project tooling, remotes, and hosting policy alter journey depth.
- **counterargument_or_limit:** Too much conditional language can obscure the default.
- **assumptions_and_boundaries:** Keep one strong sequence and isolate variability at named gates.
- **revision_decision:** Separate required decisions from adaptable mechanics.
- **additional_insight_to_add:** Time and evidence should scale with irreversibility and sharing, not a fixed count of Git commands.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The journey ends at one handoff and does not feed recurring friction into repository design.
- **supporting_reason:** Repeated base questions, wrong-remotes, mixed changes, or cleanup ambiguity reveal missing conventions and automation.
- **counterargument_or_limit:** A few exceptional branches do not justify new policy.
- **assumptions_and_boundaries:** Promote repeated or high-consequence patterns with owner approval and regression evidence.
- **revision_decision:** Add feedback from journey friction to repository instructions and safer tools.
- **additional_insight_to_add:** The most effective finish journey eventually makes ordinary cases boring and reserves human attention for exceptional ownership or risk.

## Section 011: Decision Tradeoff Guide

### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed offers adopt, adapt, avoid, and cost-of-error rows but does not compare the actual branch outcomes or conditions that reverse them.
- **supporting_reason:** The guide should choose among local save, remote review, local integration, preservation, checkpoint, cleanup, discard, or route based on intent and state.
- **counterargument_or_limit:** Too many variables can delay a clear direct request.
- **assumptions_and_boundaries:** Evaluate only tradeoffs capable of changing the requested action or its safety.
- **revision_decision:** Preserve the seed options and add outcome-specific decision matrices and reversal triggers.
- **additional_insight_to_add:** "Adapt" often means changing mechanics for the repository while preserving the same state-transition contract.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** "Adopt when sources agree" ignores user intent and observed repository conditions.
- **supporting_reason:** Adopt when request, policy, state, source guidance, and verification align; adapt mechanics when the contract still fits; route or preserve when authority or safety does not.
- **counterargument_or_limit:** Exact alignment is uncommon in repositories with custom workflows.
- **assumptions_and_boundaries:** Transparent adaptation is expected and should name the changed condition.
- **revision_decision:** Make matched conditions, not verbal similarity, the adoption criterion.
- **additional_insight_to_add:** Minimum unmarked transformation is safer than either blind copying or unnecessary reinvention.

### Question 03: When does the default work well?
- **current_section_observation:** The table focuses on source agreement without requiring reversibility or review needs.
- **supporting_reason:** It works when state can be inspected, outcomes have clear postconditions, and relevant owners can authorize irreversible steps.
- **counterargument_or_limit:** A remote service or reviewer may delay final acceptance.
- **assumptions_and_boundaries:** Choose a locally complete handoff with explicit pending state.
- **revision_decision:** Add bounded completion and asynchronous-review conditions.
- **additional_insight_to_add:** The best current choice can be publication without cleanup because it preserves both review flow and recovery.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** "Avoid" does not distinguish blocked quality, unclear ownership, conflicting policy, missing permission, or destructive uncertainty.
- **supporting_reason:** Those causes require repair, clarification, checkpoint, administration, or confirmed discard rather than one generic stop.
- **counterargument_or_limit:** Multiple recovery paths can confuse a user asking for a simple outcome.
- **assumptions_and_boundaries:** Present only the path relevant to the diagnosed blocker.
- **revision_decision:** Add cause-specific pause and route actions.
- **additional_insight_to_add:** Diagnosis determines whether preservation helps or merely freezes an unsafe mixed state.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The seed omits local versus remote durability, review versus speed, cleanup versus recovery, fix versus checkpoint, and direct execution versus menu choice.
- **supporting_reason:** These tensions determine collaboration cost, reversibility, workspace use, and truthfulness of readiness.
- **counterargument_or_limit:** Layered outcomes can combine benefits, such as checkpoint plus draft review.
- **assumptions_and_boundaries:** Compose paths only when each state and authority remains explicit.
- **revision_decision:** Add a tradeoff table with default, cost, and reversal signal.
- **additional_insight_to_add:** Publication and integration are separate milestones, allowing review durability without accepting code into the base.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Source agreement can hide different preconditions, and cleanup savings can hide lost recovery value.
- **supporting_reason:** A superficially efficient choice may increase correction cost or ownership ambiguity.
- **counterargument_or_limit:** Retaining every worktree and branch forever creates clutter and stale state.
- **assumptions_and_boundaries:** Delay cleanup until durability, ownership, and retirement conditions are known, then remove intentionally.
- **revision_decision:** Add hidden-cost and lifecycle checks.
- **additional_insight_to_add:** Cleanup debt and premature cleanup are opposite failures managed by an explicit retirement trigger.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** The rows provide no contrast across the same repository state.
- **supporting_reason:** A good direct PR preserves worktree recovery; a bad local merge targets an assumed base; a borderline checkpoint saves mixed changes because future ownership was not separated.
- **counterargument_or_limit:** A mixed checkpoint can be intentionally requested during an emergency.
- **assumptions_and_boundaries:** Inventory and label every included change so the tradeoff is conscious.
- **revision_decision:** Add contrastive outcome cases with reversal variables.
- **additional_insight_to_add:** Borderline decisions become acceptable when their debt, owner, and exit condition are explicit.

### Question 08: How can the important claims be verified?
- **current_section_observation:** Seed questions check labels but not whether the chosen tradeoff minimizes expected loss under current conditions.
- **supporting_reason:** Record selected outcome, rejected alternatives, state evidence, authorization, expected cost, recovery, and reversal trigger.
- **counterargument_or_limit:** Expected cost remains judgment until a failure or delay occurs.
- **assumptions_and_boundaries:** Label prospective risk and update it from observed cleanup or correction work.
- **revision_decision:** Add a compact branch decision record.
- **additional_insight_to_add:** A reversal trigger makes preservation temporary rather than indefinite by defining when cleanup becomes the better choice.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The four outcomes and core safeguards are source-backed, while relative cost and ideal retention duration are unmeasured.
- **supporting_reason:** Repository traffic, review latency, disk constraints, and team practice change the tradeoff.
- **counterargument_or_limit:** Open-ended retention guidance can feel indecisive.
- **assumptions_and_boundaries:** Give preservation as the default under ambiguity and require owners to set local retirement policy.
- **revision_decision:** Separate firm safety defaults from environment-specific lifecycle choices.
- **additional_insight_to_add:** Reversibility can be valued qualitatively even when its monetary benefit is not measured.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The guide considers one branch but not portfolio effects from many retained worktrees, open PRs, and checkpoint branches.
- **supporting_reason:** Individually conservative choices can accumulate operational clutter and stale ownership.
- **counterargument_or_limit:** Aggressive global cleanup recreates the original data-loss risk.
- **assumptions_and_boundaries:** Use inventory, owners, retirement triggers, and verified batch cleanup rather than age alone.
- **revision_decision:** Add lifecycle portfolio management as a later distinct process.
- **additional_insight_to_add:** Safe local defaults need a complementary maintenance loop so preservation does not become permanent ambiguity.

## Section 012: Local Corpus Hierarchy

### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed assigns canonical, legacy, and supporting roles but does not say which role governs user interaction, finish mechanics, worktree lifecycle, or repository policy.
- **supporting_reason:** Hierarchy must be claim-relative so one file does not gain authority over decisions it never specifies.
- **counterargument_or_limit:** Fine-grained roles can appear to contradict the seed's simple classification.
- **assumptions_and_boundaries:** Preserve seed roles as corpus metadata and add operational scope for current use.
- **revision_decision:** Expand the table with identity, claim authority, exclusions, and conflict response.
- **additional_insight_to_add:** A source can be historical in one taxonomy and still contain the most detailed current fallback for one mechanic.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** No precedence sequence connects user intent, project policy, observed state, and the five local paths.
- **supporting_reason:** Explicit request governs outcome, repository policy constrains it, live state supplies facts, Codex guides direct interaction, Claude finish guides choices, and worktree guidance controls isolation mechanics.
- **counterargument_or_limit:** An active repository may explicitly nominate one skill as canonical for all finish behavior.
- **assumptions_and_boundaries:** Follow that current instruction unless it conflicts with higher authority or destructive confirmation.
- **revision_decision:** Add a decision-authority ladder above the generated source roles.
- **additional_insight_to_add:** Precedence should resolve one claim at a time rather than replacing an entire source wholesale.

### Question 03: When does the default work well?
- **current_section_observation:** The hierarchy works best when source responsibilities are distinct and current repository instructions are available.
- **supporting_reason:** Then direct requests, option menus, worktree setup, tests, cleanup, and handoff can be composed without hidden overlap.
- **counterargument_or_limit:** The finish source's internal cleanup contradiction prevents simple canonical precedence.
- **assumptions_and_boundaries:** Resolve conflicting claims through user intent and least-destructive state, then retain the disagreement.
- **revision_decision:** Add fit conditions and claim-conflict handling.
- **additional_insight_to_add:** Hierarchy reduces ambiguity only when it can represent contradiction instead of suppressing it.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** Latest-file-wins, archive-first, or current-path-wins rules can each select the wrong instruction.
- **supporting_reason:** Dates and paths do not establish applicability, ownership, or safety by themselves.
- **counterargument_or_limit:** Simple precedence is faster when sources are coherent and environments standardized.
- **assumptions_and_boundaries:** Use shortcuts only after content identity and applicable scope are known.
- **revision_decision:** Add failure cases for alias, age, and global-rank precedence.
- **additional_insight_to_add:** Canonicality is a maintained relationship that should have an owner and reversal trigger.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** Flat aggregation, newest-source precedence, project-only policy, user-only intent, and expert adjudication are not compared.
- **supporting_reason:** They trade speed, consistency, local fit, authorization, and specialist cost.
- **counterargument_or_limit:** Claim-level reconciliation costs more than following one file.
- **assumptions_and_boundaries:** Apply deeper reconciliation to destructive, shared, conflicting, or high-consequence actions.
- **revision_decision:** Add alternative hierarchy models and their blind spots.
- **additional_insight_to_add:** User intent selects among valid outcomes but cannot make an unsafe or unauthorized repository mechanic valid.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Duplicate aliases, misleading legacy labels, internal contradiction, implicit project override, and method-versus-state confusion are key risks.
- **supporting_reason:** These can turn hierarchy into false certainty rather than decision support.
- **counterargument_or_limit:** The generated labels remain useful for inventory and lineage.
- **assumptions_and_boundaries:** Keep them visible but do not derive command authority from labels alone.
- **revision_decision:** Add role-misuse warnings and claim-specific reviewer questions.
- **additional_insight_to_add:** Observed Git state can falsify a source precondition without reducing the source's general value.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** Every row asks the same generic contribution question.
- **supporting_reason:** Good hierarchy uses Codex for a direct push and Claude for worktree preservation; bad hierarchy follows the first cleanup line; borderline hierarchy treats the later Codex file as globally superior despite missing cleanup details.
- **counterargument_or_limit:** The later file may be the active invoked skill in the current agent environment.
- **assumptions_and_boundaries:** Use it for its declared scope and pair missing mechanics with other evidence.
- **revision_decision:** Replace generic questions with role-specific tests.
- **additional_insight_to_add:** Completeness often comes from composition, not declaring one source winner.

### Question 08: How can the important claims be verified?
- **current_section_observation:** The seed does not require content identity, complete reads, claim mapping, or a precedence rationale.
- **supporting_reason:** Verify hashes, aliases, relevant passages, conflicting lines, project instructions, live preconditions, and selected rule.
- **counterargument_or_limit:** Hash checks cannot prove that generated hierarchy labels remain useful.
- **assumptions_and_boundaries:** Use deterministic identity for reproducibility and semantic review for authority.
- **revision_decision:** Add hierarchy integrity and decision-trace gates.
- **additional_insight_to_add:** A changed source hash should reopen only dependent claims before whole-reference coherence review.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** Seed roles, file contents, duplicate pairs, and conflict are known; operational precedence beyond explicit policy is synthesized.
- **supporting_reason:** The sources do not publish a shared cross-file authority specification.
- **counterargument_or_limit:** A strong local default is still needed for agents to act predictably.
- **assumptions_and_boundaries:** Use explicit intent, current policy, observed state, and preservation-first conflict resolution as the declared synthesis.
- **revision_decision:** State certainty and judgment per layer.
- **additional_insight_to_add:** Transparency about synthesized precedence makes exceptions easier to review than an implied universal hierarchy.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The hierarchy is static and does not account for source consolidation or retirement.
- **supporting_reason:** Duplicate paths and contradictory variants increase maintenance and agent disagreement over time.
- **counterargument_or_limit:** Aliases may be necessary for compatibility across agent systems.
- **assumptions_and_boundaries:** Retain aliases while centralizing semantic ownership and conflict tests.
- **revision_decision:** Add consolidation, alias, and retirement guidance.
- **additional_insight_to_add:** A compatibility alias should point to one maintained contract rather than silently fork behavior.

## Section 013: Theme Specific Artifact

### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed names a dirty-worktree matrix with commit scope, push decision, and recovery commands but defines only goal, boundary, and gate fields.
- **supporting_reason:** The artifact must let a reviewer decide exactly which state is owned, what transition is authorized, what remains untouched, and how to recover.
- **counterargument_or_limit:** A large matrix can become paperwork for a clean single-file commit.
- **assumptions_and_boundaries:** Provide compact and durable modes based on dirty complexity, sharing, and irreversibility.
- **revision_decision:** Define a complete branch-finish state-transition record and instantiate realistic cases.
- **additional_insight_to_add:** The artifact is most valuable before mutation because it makes hidden scope assumptions reviewable.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** No field order turns the three seed concepts into an executable decision.
- **supporting_reason:** Record identity and intent, inventory state and ownership, define readiness evidence, select the transition, specify cleanup separately, and state postcondition plus recovery.
- **counterargument_or_limit:** Some fields emerge only after repository discovery.
- **assumptions_and_boundaries:** Fill iteratively but reconcile all applicable values before action.
- **revision_decision:** Add ordered completion and consistency rules.
- **additional_insight_to_add:** Contradictory fields, such as cleanup requested while local-only changes remain, are failure evidence rather than template noise.

### Question 03: When does the default work well?
- **current_section_observation:** The artifact has no trigger threshold for clean, mixed, shared, remote, or destructive work.
- **supporting_reason:** It works especially well for dirty trees, linked worktrees, several remotes, pull requests, local merges, checkpoints, and discard.
- **counterargument_or_limit:** A no-mutation keep decision may need only a status summary and next owner.
- **assumptions_and_boundaries:** Use the compact record while preserving any state another person must reconstruct.
- **revision_decision:** Add light and durable completion modes.
- **additional_insight_to_add:** Remote sharing raises the record value because hidden local context no longer travels with the branch.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** A matrix can falsely legitimize a mutation when ownership, policy, or destructive consent is still unknown.
- **supporting_reason:** Complete-looking fields do not manufacture authority.
- **counterargument_or_limit:** The artifact can expose precisely which authority is missing.
- **assumptions_and_boundaries:** Permit blocked and pending states and prohibit forced completion values.
- **revision_decision:** Add stop, pending, and not-applicable semantics with reasons.
- **additional_insight_to_add:** Blank authority should produce no action, while explicit non-applicability should show why the dimension cannot change the result.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** Alternatives include a prose handoff, command transcript, staged-diff review, checklist, issue, pull-request template, or automated status report.
- **supporting_reason:** They trade structure, readability, reproducibility, collaboration, and automation.
- **counterargument_or_limit:** Duplicating the same state across artifacts creates drift.
- **assumptions_and_boundaries:** Use one canonical decision record and derive concise reports or PR metadata.
- **revision_decision:** Add artifact alternatives and precedence.
- **additional_insight_to_add:** Raw command output is evidence input, not a substitute for the ownership and authorization decisions in the matrix.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Likely failures include stale status, missing untracked files, ownership marked by guess, implicit remote, merged publication and cleanup fields, generic recovery, and absent pending checks.
- **supporting_reason:** These defects can make a polished matrix materially unsafe.
- **counterargument_or_limit:** Requiring every remote detail is unnecessary for local keep or checkpoint.
- **assumptions_and_boundaries:** Make fields conditional on the transition and require reasons for consequential omissions.
- **revision_decision:** Add field-level validity and freshness rules.
- **additional_insight_to_add:** A timestamp alone does not make state fresh; relevant mutations since capture determine invalidation.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** The seed promises an artifact without a completed example.
- **supporting_reason:** A good matrix excludes an unrelated note from `feature/auth`, pushes the intended commit, and preserves the worktree; a bad matrix says "all changes"; a borderline matrix records pending CI but not its owner.
- **counterargument_or_limit:** Example branches and paths are illustrative rather than repository facts.
- **assumptions_and_boundaries:** Label examples and teach the invariant fields, not their literal names.
- **revision_decision:** Add worked clean, mixed, checkpoint, and discard rows.
- **additional_insight_to_add:** Contrastive rows help reviewers detect when a field value is too generic to distinguish safe from unsafe state.

### Question 08: How can the important claims be verified?
- **current_section_observation:** A command, checklist, or question can be present without covering the matrix's action.
- **supporting_reason:** Trace each field to user request, policy, Git output, diff review, test result, command outcome, or postcondition evidence.
- **counterargument_or_limit:** Human ownership remains partly declarative.
- **assumptions_and_boundaries:** Require explicit owner acknowledgment for disputed or shared changes.
- **revision_decision:** Add field provenance and gate coverage.
- **additional_insight_to_add:** Review can sample from the planned mutation backward to every input that authorizes it.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The artifact type is a seed requirement, while the expanded schema and mode thresholds are local synthesis.
- **supporting_reason:** The fields follow source safeguards and observed Git state needs but are not empirically proven optimal.
- **counterargument_or_limit:** Presenting them too flexibly can invite generic completion.
- **assumptions_and_boundaries:** Keep semantic obligations firm while allowing equivalent repository-specific representations.
- **revision_decision:** Label mandatory decisions and adaptable format separately.
- **additional_insight_to_add:** Track fields that never change a decision and defects that escape so the schema becomes evidence-shaped.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The artifact is framed as a finish record and not a coordination interface among author, reviewer, maintainer, and future cleaner.
- **supporting_reason:** Each role needs different state and may act after local conversational context disappears.
- **counterargument_or_limit:** One person may hold every role for a local branch.
- **assumptions_and_boundaries:** Keep role fields concise but explicit when state is shared or delayed.
- **revision_decision:** Add owner and retirement responsibilities.
- **additional_insight_to_add:** A complete matrix can become the handoff contract for later cleanup, preventing preservation from turning into ownerless debris.

## Section 014: Worked Example Set

### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed labels good, bad, and borderline use but does not show inputs, repository states, chosen transitions, or postconditions.
- **supporting_reason:** Worked examples should demonstrate how branch finish guidance changes under scope, quality, destination, and recoverability differences.
- **counterargument_or_limit:** Long examples can be copied as universal recipes.
- **assumptions_and_boundaries:** Annotate decision variables and require transfer to changed fixtures.
- **revision_decision:** Replace generic labels with end-to-end draft-PR, merge, checkpoint, and discard examples.
- **additional_insight_to_add:** A set of near cases teaches state-sensitive reasoning better than one ideal command transcript.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** No common schema lets readers compare examples.
- **supporting_reason:** Each case should name request, pre-state, ownership, checks, transition, cleanup, postcondition, and recovery.
- **counterargument_or_limit:** Rigid presentation can obscure the natural user-facing report.
- **assumptions_and_boundaries:** Standardize the analysis while keeping final communication concise.
- **revision_decision:** Add an eight-part annotation frame.
- **additional_insight_to_add:** Consistent hidden analysis supports varied user-facing language without weakening gates.

### Question 03: When does the default work well?
- **current_section_observation:** The seed does not say when examples are representative enough for reuse.
- **supporting_reason:** Controlled contrasts work when one consequential variable changes while expected state and rationale remain inspectable.
- **counterargument_or_limit:** Real incidents often combine several failures.
- **assumptions_and_boundaries:** Start with isolated risks and include one mixed case for integration judgment.
- **revision_decision:** Add controlled and combined fixtures.
- **additional_insight_to_add:** Single-variable cases diagnose decision logic; mixed cases test whether the logic composes under pressure.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** Worked commands can become stale or unsafe across Git versions, hosting platforms, and repository conventions.
- **supporting_reason:** Readers may imitate syntax while missing the intent and postcondition structure.
- **counterargument_or_limit:** Removing commands makes operational examples less concrete.
- **assumptions_and_boundaries:** Keep commands illustrative, verify them locally, and make state invariants primary.
- **revision_decision:** Add portability and refresh notes to every case.
- **additional_insight_to_add:** Retire an example when readers can pass by command memorization but fail a changed branch or remote state.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** Counterexamples, recovery drills, partial matrices, command simulations, and repository-specific variants are absent.
- **supporting_reason:** They teach failure boundaries, reversibility, completion judgment, behavior, and local adaptation.
- **counterargument_or_limit:** Including all forms would inflate the reference.
- **assumptions_and_boundaries:** Choose one form for each high-consequence misconception and route deeper training elsewhere.
- **revision_decision:** Combine positive, failed, borderline, and unseen-transfer fixtures.
- **additional_insight_to_add:** Recovery drills reveal whether a finish path preserved enough state, not merely whether it looked correct initially.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Examples can accidentally normalize `origin`, `main`, broad staging, automatic cleanup, force operations, or fabricated check success.
- **supporting_reason:** Incidental syntax can become copied policy.
- **counterargument_or_limit:** Concrete examples need some branch and remote names.
- **assumptions_and_boundaries:** Label names illustrative and show the evidence that selected them.
- **revision_decision:** Add anti-copy boundaries and no-browse evidence status.
- **additional_insight_to_add:** An example should model how to discover values, not only display chosen values.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** Existing examples describe reference process rather than branch behavior.
- **supporting_reason:** Good behavior isolates owned changes and proves the outcome; bad behavior destroys or publishes from assumptions; borderline behavior succeeds technically while losing ownership, pending-state, or recovery context.
- **counterargument_or_limit:** A borderline outcome may be accepted under explicit emergency tradeoffs.
- **assumptions_and_boundaries:** Record the exception, debt, owner, and exit trigger.
- **revision_decision:** Add contrastive state transitions and remediation notes.
- **additional_insight_to_add:** Borderline examples are valuable because technical success can hide a violated coordination contract.

### Question 08: How can the important claims be verified?
- **current_section_observation:** The seed does not require examples to be executable, source-mapped, or checked against postconditions.
- **supporting_reason:** Verify fixture setup, nonmutating baseline, expected decision, scoped action, resulting state, unrelated-state preservation, and recovery.
- **counterargument_or_limit:** Destructive cases should not be exercised on valuable repositories.
- **assumptions_and_boundaries:** Use disposable test repositories or reasoned simulations for deletion and force paths.
- **revision_decision:** Attach a safe verification method and failure signal to each example.
- **additional_insight_to_add:** A disposable repository fixture can test Git mechanics while human review tests authorization and ownership.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** Source safeguards and Git state relationships support the examples, while their pedagogical effectiveness and exact mechanics remain environment-dependent.
- **supporting_reason:** No reader study or cross-platform execution was performed during this prose evolution.
- **counterargument_or_limit:** The cases still provide useful local regression hypotheses.
- **assumptions_and_boundaries:** Label scenario outcomes as illustrative until tested in the target environment.
- **revision_decision:** Separate source rule, example design, and observed result.
- **additional_insight_to_add:** Confidence should attach to each fixture and environment rather than the example set globally.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** Examples are treated as teaching content rather than regression tests for future source and policy changes.
- **supporting_reason:** Stable fixtures can detect lost confirmation, wrong target selection, mixed scope, stale checks, and premature cleanup.
- **counterargument_or_limit:** Semantic fixtures need maintenance and cannot automate user intent.
- **assumptions_and_boundaries:** Keep a small high-value suite with explicit human and command assertions.
- **revision_decision:** Reframe the set as living state-transition tests.
- **additional_insight_to_add:** A fixture failure can identify whether the defect belongs to policy, source synthesis, command mechanics, or handoff reporting.

## Section 015: Outcome Metrics and Feedback Loops

### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed names one leading indicator, one failure signal, and a cadence but does not determine whether a finish transition improved safety, clarity, and recoverability.
- **supporting_reason:** Evaluation should separate source process, scope accuracy, quality truthfulness, action correctness, postconditions, recovery, handoff, and maintenance.
- **counterargument_or_limit:** Collecting every layer for every local commit would be disproportionate.
- **assumptions_and_boundaries:** Match evidence depth to sharing and irreversibility while retaining ownership and outcome checks.
- **revision_decision:** Build a branch-finish metric stack with interpretation and response.
- **additional_insight_to_add:** Metrics should identify the failed transition layer rather than compress safety into one score.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** "Better decision with less ambiguity" lacks observable branch outcomes.
- **supporting_reason:** Default to scoped-change accuracy, current quality evidence, correct requested transition, postcondition match, unrelated-state preservation, and complete next-owner handoff.
- **counterargument_or_limit:** Downstream review and merge outcomes can be influenced by code quality and team latency beyond the finish guide.
- **assumptions_and_boundaries:** Treat downstream results as contributory observations, not proof of sole causality.
- **revision_decision:** Define leading, transition, lagging, and guardrail measures.
- **additional_insight_to_add:** Unrelated-state preservation is a first-class success signal even though nothing visible changed in that state.

### Question 03: When does the default work well?
- **current_section_observation:** The loop assumes repeated finish operations or fixtures are available.
- **supporting_reason:** It works for teams, agents, or repositories with recurring commits, pull requests, worktrees, checkpoints, and cleanup.
- **counterargument_or_limit:** One-off local experiments may never produce comparable outcomes.
- **assumptions_and_boundaries:** Use a concise postcondition and handoff audit for isolated cases.
- **revision_decision:** Add ephemeral and maintained measurement modes.
- **additional_insight_to_add:** A small portfolio of failure fixtures can make low-frequency destructive risks observable without waiting for real loss.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** Raw speed, clean-tree rate, commit count, PR count, or test pass rate can reward broad staging, premature cleanup, or overclaiming.
- **supporting_reason:** These proxies improve while ownership and recoverability decline.
- **counterargument_or_limit:** They remain useful operational diagnostics when interpreted narrowly.
- **assumptions_and_boundaries:** Never use one proxy alone to assert safe completion.
- **revision_decision:** Add anti-gaming guardrails and severity overrides.
- **additional_insight_to_add:** One irreversible wrong-scope event can outweigh many routine fast finishes.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** Alternatives such as audit sampling, incident review, disposable-repository fixtures, handoff surveys, diff statistics, and cleanup inventory are absent.
- **supporting_reason:** They trade realism, safety, reproducibility, cost, and diagnostic depth.
- **counterargument_or_limit:** Extensive measurement can make branch finishing slower than the work warrants.
- **assumptions_and_boundaries:** Select methods tied to the claimed benefit and highest consequence.
- **revision_decision:** Add question-to-method routing.
- **additional_insight_to_add:** Qualitative error categories often guide repair better than a total failure count.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Missing denominator, repeated branch effects, hidden untracked files, unobserved CI, stale test results, and severity-blind counting can distort metrics.
- **supporting_reason:** These produce precise-looking but noncomparable outcomes.
- **counterargument_or_limit:** Full experimental control is unnecessary for local process improvement.
- **assumptions_and_boundaries:** Report raw cases and conditions honestly before aggregating.
- **revision_decision:** Add measurement metadata and claim-language limits.
- **additional_insight_to_add:** "No unrelated changes lost" requires an inventory baseline; absence after cleanup is otherwise uninterpretable.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** No sample metric record demonstrates correct interpretation.
- **supporting_reason:** Good evidence records exact scoped commit and preserved note; bad evidence celebrates a clean tree; borderline evidence reports a successful PR while cleanup recovery is unknown.
- **counterargument_or_limit:** One finish may reflect agent expertise rather than reference quality.
- **assumptions_and_boundaries:** Compare repeated patterns and preserve task context before generalizing.
- **revision_decision:** Add contrastive records and triggered revisions.
- **additional_insight_to_add:** Disagreement between command success and postcondition safety is valuable diagnostic evidence.

### Question 08: How can the important claims be verified?
- **current_section_observation:** The leading indicator lacks a baseline, fixture, observer, or state definition.
- **supporting_reason:** Define pre-state, expected transition, unrelated-state invariant, quality claim, postcondition, observer, and comparison period.
- **counterargument_or_limit:** Small samples cannot support precise rates.
- **assumptions_and_boundaries:** Report counts and cases without universal percentages until design supports them.
- **revision_decision:** Add a minimal outcome record and regression loop.
- **additional_insight_to_add:** Version the reference, fixture, and repository policy together when attributing a changed result.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** Re-running verifiers after edits and capturing branch state are firm local practices, while ideal cadence and causal effect are unmeasured.
- **supporting_reason:** Repository change rate, branch volume, and incident history alter review needs.
- **counterargument_or_limit:** Pure event-driven review can miss quiet accumulation of stale worktrees.
- **assumptions_and_boundaries:** Combine event triggers with owner-selected inventory review without inventing a universal interval.
- **revision_decision:** Separate mandatory events from local cadence policy.
- **additional_insight_to_add:** Confidence in a process improvement should reflect the observation design, not the cleanliness of the final report.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The feedback loop repairs the reference but does not route recurring defects to repository policy, tooling, or ownership.
- **supporting_reason:** Repeated wrong bases, remotes, mixed commits, or stale worktrees may originate upstream in missing defaults.
- **counterargument_or_limit:** Broad policy changes exceed the scope of one anomalous branch.
- **assumptions_and_boundaries:** Escalate recurrent or severe evidence with an owner and regression case.
- **revision_decision:** Add defect routing from outcome to owning layer.
- **additional_insight_to_add:** Measuring correction recurrence can prioritize a safer repository command over repeated reminder prose.

## Section 016: Completeness Checklist

### Question 01: What decision does this reference help make?
- **current_section_observation:** The seed checks seven document categories but not whether a real branch transition has all required authority, state, quality, action, postcondition, recovery, and handoff evidence.
- **supporting_reason:** Completeness should determine whether the reference or an applied finish record is ready for its stated use.
- **counterargument_or_limit:** Presence checks can pass incorrect or stale content.
- **assumptions_and_boundaries:** Treat completion as necessary structure and require semantic and state verification separately.
- **revision_decision:** Expand the checklist into reference-release and operation-release categories.
- **additional_insight_to_add:** Completeness and safety are orthogonal; a complete inventory can still contain the wrong owner or destination.

### Question 02: What is the recommended default, and why?
- **current_section_observation:** Existing bullets have no evidence location, owner, failure action, or conditional applicability.
- **supporting_reason:** Each item should resolve to a source, command result, review, explicit authorization, postcondition, or reasoned exclusion.
- **counterargument_or_limit:** Repeating evidence can create a second paperwork system.
- **assumptions_and_boundaries:** Link the packet, matrix, verifier, and operation record rather than duplicating them.
- **revision_decision:** Convert bullets into evidence-bearing release questions.
- **additional_insight_to_add:** A checklist is strongest as an index into existing proof, not as a place to restate generic policy.

### Question 03: When does the default work well?
- **current_section_observation:** The seed assumes a durable generated reference rather than a quick local keep or commit.
- **supporting_reason:** The full checklist fits shared publication, integration, destructive cleanup, reusable automation, and maintained guidance.
- **counterargument_or_limit:** A low-risk no-mutation keep request needs fewer fields.
- **assumptions_and_boundaries:** Use a compact mode with outcome, identity, status, and handoff while retaining consequential safeguards.
- **revision_decision:** Add compact, shared, and destructive modes.
- **additional_insight_to_add:** Mode selection should occur before action so an ordinary request cannot silently grow into high-consequence cleanup.

### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** A universal list can ignore protected-branch, compliance, release, or hosting-specific gates and encourage stopping after boxes are present.
- **supporting_reason:** Domain authority may add conditions this reference cannot know.
- **counterargument_or_limit:** Unlimited extensions make completion inconsistent.
- **assumptions_and_boundaries:** Keep a stable core and link environment-specific authorities.
- **revision_decision:** Add extension, unresolved, and route semantics.
- **additional_insight_to_add:** "Not applicable" needs a reason; otherwise it is indistinguishable from an unexamined risk.

### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** Rubrics, automated tests, peer review, pull-request templates, branch-protection checks, and disposable fixtures are not compared with checklist use.
- **supporting_reason:** They offer different consistency, depth, automation, authority, and safety.
- **counterargument_or_limit:** Combining all methods for every outcome wastes effort.
- **assumptions_and_boundaries:** Route each consequential item to the strongest appropriate evidence type.
- **revision_decision:** Add method references without turning each bullet into a full procedure.
- **additional_insight_to_add:** A checklist can orchestrate heterogeneous proof while acknowledging that human consent and machine state are different evidence classes.

### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Generic completion, stale snapshots, missing untracked files, unexplained exclusions, copied remote names, pending checks without owners, and duplicate proof can satisfy form.
- **supporting_reason:** These defects obscure the actual release decision.
- **counterargument_or_limit:** Some repetition supports independent review of high-consequence actions.
- **assumptions_and_boundaries:** Repeat decisive facts and link detailed output.
- **revision_decision:** Add anti-ceremony and freshness checks.
- **additional_insight_to_add:** If the checklist never blocks or narrows any action, test whether it still discriminates safety.

### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** The seed gives assertions rather than sample evidence responses.
- **supporting_reason:** Good completion points to scoped diff and postcondition; bad completion says "covered"; borderline completion has all fields but a pending CI result with no next owner.
- **counterargument_or_limit:** Inline evidence can make the checklist difficult to scan.
- **assumptions_and_boundaries:** Use concise references and preserve analysis elsewhere.
- **revision_decision:** Add pass, fail, pending, and needs-review examples.
- **additional_insight_to_add:** Pending is a valid state only when its consequence and owner are explicit.

### Question 08: How can the important claims be verified?
- **current_section_observation:** The checklist's risk coverage is not traced to anti-patterns, reliability targets, or failure fixtures.
- **supporting_reason:** Map each high-consequence failure and outcome claim to at least one item and one independent gate.
- **counterargument_or_limit:** Full traceability is excessive for style-only defects.
- **assumptions_and_boundaries:** Prioritize work loss, wrong publication, false readiness, and ownerless state.
- **revision_decision:** Add risk-to-check coverage and final sampling.
- **additional_insight_to_add:** Unmapped risk is invisible, while many redundant checks indicate maintenance waste.

### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** The seven seed categories are local requirements; expanded operation gates and mode thresholds are synthesized.
- **supporting_reason:** They follow mapped safeguards but vary with repository consequence and policy.
- **counterargument_or_limit:** Qualification can weaken decisive release behavior.
- **assumptions_and_boundaries:** Keep core invariants firm and label adaptable mechanics.
- **revision_decision:** Separate nonnegotiable authority and preservation from risk-scaled evidence depth.
- **additional_insight_to_add:** Bounded uncertainty should be recorded as output rather than forced into a false pass or fail.

### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** Completion is treated as permanent even though tree, policy, remote, checks, and ownership change.
- **supporting_reason:** Previously valid evidence can expire before publication or cleanup.
- **counterargument_or_limit:** Rechecking every item after every read-only operation is wasteful.
- **assumptions_and_boundaries:** Reopen only dependent categories plus final whole-state coherence.
- **revision_decision:** Add invalidation and selective revalidation rules.
- **additional_insight_to_add:** A completion record is durable only when it states the assumptions that made its pass valid.
## Section 017: Adjacent Reference Routing
### Question 01: What decision does this reference help make?
- **current_section_observation:** The routing section must decide whether the next consequential action still belongs to branch finishing or should transfer to an adjacent implementation, conflict-recovery, release, platform, or repository-repair authority.
- **supporting_reason:** A finish procedure is reliable only when its ownership boundary is explicit; otherwise a familiar Git command can conceal that the real task is code completion, conflict resolution, deployment, or administrative approval.
- **counterargument_or_limit:** Routing too early can fragment a simple finish into needless handoffs, especially when a nonmutating inspection can answer a small uncertainty without changing task ownership.
- **assumptions_and_boundaries:** This decision assumes the current state audit is available and limits this reference to preservation, publication, integration, retention, cleanup, and confirmed discard of already finishable or deliberately checkpointed work.
- **revision_decision:** Replace the seed's generic adjacent-reference suggestions with a trigger-and-return routing table that names the receiving authority, information to transfer, and condition for resuming the finish workflow.
- **additional_insight_to_add:** A route is part of the safety model rather than a reading recommendation: it prevents an agent from treating every obstructed finish as permission to broaden scope.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** The recommended default is to keep control in the finish workflow while identity, ownership, readiness, and the requested outcome can be established non-destructively, then hand off before crossing another authority's mutation boundary.
- **supporting_reason:** This default preserves continuity for ordinary commits, pushes, pull requests, keeps, and local merges while ensuring specialist procedures govern unresolved code, conflicts, releases, hosting controls, and damaged Git state.
- **counterargument_or_limit:** A repository may define a single integrated runbook whose finish phase legitimately includes release or deployment steps, so the local policy can supersede the generic handoff point.
- **assumptions_and_boundaries:** The default presumes adjacent procedures are discoverable and that handoff does not itself authorize writes, force operations, elevated access, or cleanup.
- **revision_decision:** State a conservative rule: inspect enough to classify the boundary, preserve current evidence, route with a concrete return condition, and do not continue mutating under the finish label.
- **additional_insight_to_add:** Keeping the classification step local but the specialist mutation external minimizes context loss without allowing authority to expand silently.
### Question 03: When does the default work well?
- **current_section_observation:** Boundary-first routing works well when a clean feature is ready to save, an unfinished test clearly returns to implementation, a merge conflict clearly needs recovery, or a published change clearly enters a separate release process.
- **supporting_reason:** These cases expose observable state transitions and named owners, making it practical to pause one workflow and resume it after a verifiable condition such as green checks or resolved conflicts.
- **counterargument_or_limit:** Small repositories may have one person performing every role, but role separation still matters because authorization and verification obligations differ even when the human owner is unchanged.
- **assumptions_and_boundaries:** The effective cases assume the route can carry branch identity, worktree path, dirty summary, evidence already collected, unresolved blocker, and requested outcome without losing local-only work.
- **revision_decision:** Add concrete routing rows for unfinished implementation, merge or rebase conflict, release orchestration, platform administration, repository recovery, and documentation-only clarification.
- **additional_insight_to_add:** The same operator can execute adjacent procedures sequentially, yet an explicit logical handoff still resets which claims are valid and which checks must be rerun.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** Generic routing fails when the receiving reference is unnamed, stale, less authoritative than repository policy, or unable to preserve the state needed to return safely.
- **supporting_reason:** A vague direction such as "consider the branch reference" transfers neither evidence nor responsibility, so it can produce loops, duplicated checks, or destructive action based on a partial snapshot.
- **counterargument_or_limit:** If no specialist reference exists, stopping indefinitely may be worse than following a bounded manual recovery plan approved by the user and supported by current Git evidence.
- **assumptions_and_boundaries:** A route is wrong when the issue can be resolved by a read-only finish check, when the user expressly requested a safe in-scope action, or when handoff would abandon an atomic operation already underway.
- **revision_decision:** Require each route to specify a trigger, prohibited finish action, destination capability, transfer bundle, and observable return condition; otherwise classify it as an unresolved blocker.
- **additional_insight_to_add:** Routing quality should be judged by whether the next worker can act without reconstructing hidden state, not by whether another document was merely named.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** Relevant alternatives are continuing under this reference, pausing for clarification, invoking a repository runbook, handing off to a specialist workflow, or escalating to a human administrator.
- **supporting_reason:** These alternatives trade speed and context continuity against specialist correctness, authorization, recovery depth, and the risk of acting outside the user's requested outcome.
- **counterargument_or_limit:** A many-route catalog can create decision overhead for routine finishes, so only boundaries that change authority, reversibility, or verification should trigger a formal handoff.
- **assumptions_and_boundaries:** Choosing among routes depends on observed state and policy rather than tool availability alone; possession of a deployment CLI or force option does not make its use part of branch finishing.
- **revision_decision:** Present a compact decision rule before the detailed table: continue for finish-state operations, clarify unknown intent, route specialist mutations, and escalate when authorization or repository integrity is uncertain.
- **additional_insight_to_add:** A return-to-finish route is preferable to an open-ended transfer because it preserves the original outcome while allowing a narrower authority to clear the blocker.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** The highest-risk routing failures are circular handoffs, stale state snapshots, implied authorization, cleanup before transfer, scope expansion, and confusing remote CI or hosting administration with local Git readiness.
- **supporting_reason:** Each failure severs the causal link between the user's request and the eventual mutation, making it difficult to establish who owned local changes or which evidence remained current.
- **counterargument_or_limit:** Not every context change invalidates every fact; immutable commit identities and captured command output can remain useful if their time and applicability are recorded.
- **assumptions_and_boundaries:** The route must preserve local-only files, avoid mutation during classification, and mark which status, diff, check, base, remote, and policy observations require refresh on return.
- **revision_decision:** Add explicit warnings that handoff does not equal consent, that publication does not equal deployment, and that conflict resolution does not imply approval to rewrite shared history.
- **additional_insight_to_add:** Cleanup is especially dangerous at a boundary because it can erase the evidence bundle the receiving workflow needs to diagnose or recover the state.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** A good route reports a failing required test, preserves the branch, transfers the scoped diff and failure evidence to implementation, and resumes finishing only after the relevant checks pass.
- **supporting_reason:** That example has a specific trigger, no unauthorized mutation, a complete handoff bundle, and a measurable return condition tied to the original finish claim.
- **counterargument_or_limit:** A passing rerun after implementation may still be insufficient if code scope, ownership, or remote review changed, so return does not automatically restore all prior readiness evidence.
- **assumptions_and_boundaries:** A bad route says "use another skill" and deletes the worktree; a borderline route opens a pull request correctly but then starts deployment without a release request or runbook.
- **revision_decision:** Include one concise good, bad, and borderline scenario beneath the routing table, each identifying the decisive boundary rather than teaching unrelated command syntax.
- **additional_insight_to_add:** Borderline examples are valuable because most authority violations begin with a technically successful adjacent action whose user authorization was never established.
### Question 08: How can the important claims be verified?
- **current_section_observation:** Routing claims can be verified by recording the triggering state, selected authority, preserved handoff evidence, prohibited actions, return condition, and post-return refresh of invalidated checks.
- **supporting_reason:** These artifacts make the handoff auditable and allow a reviewer to distinguish a justified boundary transfer from avoidance, tool preference, or accidental scope growth.
- **counterargument_or_limit:** There is no universal command that proves the correct conceptual owner; repository instructions and user intent require interpretation alongside observable Git state.
- **assumptions_and_boundaries:** Verification should use read-only status and configuration queries before handoff and operation-specific tests afterward, without presenting document existence as proof that its instructions applied.
- **revision_decision:** Add a route-verification checklist and a small trace schema containing from-state, trigger, destination, evidence bundle, blocked mutation, return predicate, and refreshed evidence.
- **additional_insight_to_add:** Sampling completed handoffs for loops, repeated discovery, lost local state, and unauthorized follow-on actions provides a maintenance signal for improving the routing map.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** It is confident that destructive cleanup, conflict repair, release, deployment, and platform administration require distinct evidence or authority; the exact local owner and runbook remain repository-specific.
- **supporting_reason:** Local finish sources establish tests, outcome selection, direct requests, worktree handling, and conservative state management, while they do not define every project's release or recovery topology.
- **counterargument_or_limit:** Even a well-classified specialist route may be unavailable, contradictory, or outdated, requiring explicit user judgment rather than automatic delegation.
- **assumptions_and_boundaries:** Public documentation was not refreshed in this evolution, so platform-specific routing names and capabilities must be validated when a real operation depends on them.
- **revision_decision:** Label universal boundary principles as high confidence and identify destination selection, required approvals, and return gates as policy-dependent judgments that need current evidence.
- **additional_insight_to_add:** Uncertainty should narrow action to preservation and clarification; it should not be converted into a generic permission to choose whichever adjacent tool is available.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** Explicit routing turns branch finishing into a composable state machine: specialist workflows may transform the state, but they must return evidence compatible with the original outcome and ownership constraints.
- **supporting_reason:** This model explains why prior checks can become stale, why cleanup belongs after durable handoff, and why a successful specialist action does not itself prove finish completion.
- **counterargument_or_limit:** A formal state-machine vocabulary can become ceremonial if teams do not connect it to observable fields and stop conditions in their actual tooling.
- **assumptions_and_boundaries:** The deduction applies where workflows are sequentially composable; emergency recovery or policy escalation may terminate the original finish request instead of returning to it.
- **revision_decision:** End the section with invalidation and resumption rules: retain immutable evidence, refresh mutable observations, reconfirm intent after material scope change, and rerun the finish postconditions.
- **additional_insight_to_add:** Routing telemetry can reveal missing runbooks and recurrent ownership ambiguity, allowing teams to improve repository instructions rather than compensating with increasingly broad agent discretion.
## Section 018: Workload Model
### Question 01: What decision does this reference help make?
- **current_section_observation:** The workload model must decide whether a branch-finishing operation is small and coherent enough to verify as one transition or should be split, checkpointed, or escalated before mutation.
- **supporting_reason:** Finish safety depends on the number of repositories, worktrees, ownership domains, requested outcomes, change classes, checks, remotes, and active collaborators, not merely on a raw changed-file count.
- **counterargument_or_limit:** A large mechanical change can be easier to finish than a two-file security change, so no single dimension should be treated as a universal capacity threshold.
- **assumptions_and_boundaries:** The decision applies after read-only discovery and before staging, integration, cleanup, or discard; it does not estimate implementation effort or release duration.
- **revision_decision:** Recast the seed table as an operating-capacity model with compact, full, and split-or-escalate modes selected from observable workload dimensions.
- **additional_insight_to_add:** Workload is best measured by independent decisions and invalidation paths because each one can require separate authorization, evidence, and recovery.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** The recommended default is one repository, one identified branch or worktree, one requested outcome, and one reviewable ownership scope per finish operation.
- **supporting_reason:** A single coherent transition makes it possible to connect intent, diff, checks, action, and postcondition without letting one success mask an unrelated failure.
- **counterargument_or_limit:** Coordinated multi-package or multi-repository releases may intentionally require atomic choreography, but that belongs to an explicit orchestration runbook rather than this default.
- **assumptions_and_boundaries:** The default permits multiple commits or test commands when they support the same owned outcome and remain individually inspectable; it does not require an artificially tiny diff.
- **revision_decision:** Remove the unsupported fixed limit of 500 changed files and define escalation through mixed ownership, multiple destinations, destructive consequences, stale evidence, and inability to review the effective diff.
- **additional_insight_to_add:** A workload remains bounded when the operator can state one causal story from request through postcondition, even if a generated or mechanical change touches many paths.
### Question 03: When does the default work well?
- **current_section_observation:** The one-transition default works well for an isolated feature worktree, a scoped checkpoint, a single pull-request publication, or a local merge with known base and repository-defined checks.
- **supporting_reason:** These scenarios normally have a stable branch identity, separable change ownership, one durability destination, and a finite set of relevant quality gates.
- **counterargument_or_limit:** Isolation by worktree does not prove change ownership or branch correctness, so status, diff, and repository instructions still require inspection.
- **assumptions_and_boundaries:** The effective case assumes no concurrent mutation changes the tree between evidence capture and action, or that such mutation is detected and dependent checks are refreshed.
- **revision_decision:** Describe the compact mode for low-risk keep or scoped commit and the full mode for remote publication, integration, shared state, cleanup, or discard.
- **additional_insight_to_add:** Operational simplicity comes from aligned identity, ownership, and destination rather than from a small command count.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** A single finish operation becomes wrong when it spans repositories, unrelated owners, conflicting outcomes, several remotes or bases, unresolved conflicts, unreviewable generated changes, or independently failing gates.
- **supporting_reason:** Combining these dimensions creates partial-success states in which it is unclear what can be retried, rolled back, reported as durable, or safely cleaned.
- **counterargument_or_limit:** Some repository automation can prove and perform a coordinated transition atomically, reducing the need for manual splits when its contract and recovery behavior are current.
- **assumptions_and_boundaries:** Failure of the default means split or route the operation, not silently discard difficult paths or weaken the acceptance claim.
- **revision_decision:** Add explicit split triggers and require each resulting unit to retain its own outcome, ownership, evidence, action, and postcondition record.
- **additional_insight_to_add:** The first unbounded dimension should stop expansion because later evidence gathered across an incoherent scope is expensive and likely to become stale.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** Alternatives include finishing one scoped unit, creating a preservation checkpoint, sequencing several finish units, using a repository orchestrator, or pausing for owner coordination.
- **supporting_reason:** These options trade immediate throughput against reviewability, atomicity, coordination cost, recovery clarity, and the amount of evidence invalidated by each mutation.
- **counterargument_or_limit:** Excessive splitting can create noisy commits, repeated checks, and integration overhead that obscure a legitimately cohesive change.
- **assumptions_and_boundaries:** A useful split follows ownership, behavior, destination, or recovery boundaries rather than arbitrary file counts, directory names, or agent convenience.
- **revision_decision:** Add a selection table comparing compact, full, sequenced, orchestrated, and blocked modes with their entry and exit conditions.
- **additional_insight_to_add:** Checkpointing preserves optionality but must be labeled incomplete when required checks or outcome verification remain pending.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Major workload gotchas include generated trees, vendored code, submodules, sparse checkouts, large-file pointers, nested repositories, renamed files, concurrent worktree edits, and path-count inflation.
- **supporting_reason:** These conditions make ordinary status summaries or numeric thresholds poor proxies for semantic scope, ownership, storage durability, and review effort.
- **counterargument_or_limit:** Not every repository uses these features, so discovery should be evidence-driven rather than a ritual that probes every possible Git capability.
- **assumptions_and_boundaries:** The model treats unknown ownership, hidden worktree state, and unexplained generator output as pressure to inspect or split, not as permission for broad staging.
- **revision_decision:** Introduce pressure indicators for reviewability, concurrency, external state, destructive reach, and evidence freshness alongside path volume.
- **additional_insight_to_add:** A small diff with one unknown untracked secret can carry more finish risk than thousands of reproducible generated lines.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** A good workload is one feature branch with owned source and generated output, a reproducible generator check, one pull-request destination, and preserved unrelated files.
- **supporting_reason:** Its potentially large path volume remains coherent because provenance, regeneration, review method, verification, and durability are all explicit.
- **counterargument_or_limit:** Generated output can still exceed reviewer or platform limits, requiring artifact-specific review or a split even when ownership is clear.
- **assumptions_and_boundaries:** A bad workload combines two repositories, three owners, cleanup, and deployment; a borderline workload is one monorepo branch with several packages and partially shared checks.
- **revision_decision:** Add worked capacity examples that explain why each case selects compact, full, sequenced, or orchestrated handling.
- **additional_insight_to_add:** Borderline workloads should be resolved by identifying the first independent outcome or recovery boundary, not by debating an arbitrary maximum file count.
### Question 08: How can the important claims be verified?
- **current_section_observation:** Workload classification can be verified with repository and worktree inventory, scoped diff statistics, ownership review, active-operation detection, remote and base mapping, check coverage, and concurrency rechecks.
- **supporting_reason:** These observations show whether the proposed finish has one coherent state transition and whether the operator can prove its postcondition without hidden partial outcomes.
- **counterargument_or_limit:** Diff statistics and automated ownership files are signals rather than proof; semantic coupling and current human ownership can differ from path-based metadata.
- **assumptions_and_boundaries:** Verification must use repository-appropriate commands and avoid exposing secrets or loading enormous binary content merely to count it.
- **revision_decision:** Provide an evidence record with scope units, pressure indicators, selected mode, split rationale, invalidation triggers, and postcondition owner.
- **additional_insight_to_add:** Rechecking the workload classification just before mutation detects collaborator edits that can turn a previously bounded operation into a mixed one.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** It is confident that mixed ownership, multiple irreversible outcomes, and stale state increase finish risk; the exact reviewable size and acceptable concurrency remain repository- and team-dependent.
- **supporting_reason:** Local sources strongly support state inspection, tests, explicit outcome choice, intentional saving, and conservative cleanup but provide no universal numeric capacity limit.
- **counterargument_or_limit:** Repository history may supply measured thresholds for CI duration, pull-request size, or platform constraints that are more useful than this generic qualitative model.
- **assumptions_and_boundaries:** Any numeric boundary should be labeled as measured local policy with its unit, environment, observation window, and failure consequence rather than inherited from the seed.
- **revision_decision:** Mark fixed capacity claims as judgment unless backed by current repository evidence, and make qualitative stop conditions the portable default.
- **additional_insight_to_add:** Uncertainty about scale should lead to a reversible checkpoint or narrower unit, while uncertainty about ownership should stop mutation entirely.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The workload model implies that finish throughput is limited by coherent evidence refresh and recovery capacity, not by how many Git commands an agent can issue in one run.
- **supporting_reason:** Every additional owner, destination, or concurrent mutation adds an invalidation edge that can force tests, diffs, policy, or postconditions to be recomputed.
- **counterargument_or_limit:** Strong transaction-like automation can collapse several invalidation edges, but only if its atomicity, idempotency, and failure recovery are themselves verified.
- **assumptions_and_boundaries:** This deduction applies to stateful repository operations and should not be misread as a prohibition on parallel read-only discovery across independent units.
- **revision_decision:** Close the section with a rule to parallelize observation where safe, serialize mutations by coherent unit, and persist evidence at each durable boundary.
- **additional_insight_to_add:** Tracking why workloads are split can expose recurring repository architecture or ownership coupling that deserves structural remediation outside the finish workflow.
## Section 019: Reliability Target
### Question 01: What decision does this reference help make?
- **current_section_observation:** The reliability section must decide which finish properties are mandatory for every operation and which performance or quality indicators may be sampled and calibrated locally.
- **supporting_reason:** State preservation, authorization, destination correctness, claim honesty, and postcondition closure are safety invariants, whereas routing accuracy rates and retry frequencies are monitoring signals rather than permissions to fail a specific operation.
- **counterargument_or_limit:** Some organizations express all obligations as service objectives, but a statistical target can obscure that one unauthorized discard is unacceptable even when an aggregate percentage remains high.
- **assumptions_and_boundaries:** The section evaluates the branch-finish process and reference, not application runtime reliability or the business correctness of the feature itself.
- **revision_decision:** Replace the flat seed targets with an invariant table, a locally calibrated audit table, and explicit rules for evidence, exceptions, and remediation.
- **additional_insight_to_add:** Reliability must attach to the requested state transition; a perfectly executed push to the wrong remote is operationally unreliable despite command success.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** The recommended default is zero tolerated known loss of unrelated work, zero destructive action without exact authorization, and complete evidence for identity, ownership, selected outcome, destination, relevant checks, and postcondition.
- **supporting_reason:** These properties directly protect user work and make the finish report falsifiable from Git and platform state rather than from the operator's confidence.
- **counterargument_or_limit:** Complete evidence does not mean exhaustive inspection of irrelevant repository history; the evidence set should remain proportional to the chosen action and consequence.
- **assumptions_and_boundaries:** A requested checkpoint may legitimately omit merge-readiness evidence, but it must state that narrower claim and still satisfy preservation, ownership, and destination invariants.
- **revision_decision:** Define risk-tiered evidence depth while keeping preservation, authorization, and claim-labeling requirements constant across compact and full operations.
- **additional_insight_to_add:** Honest incompleteness is more reliable than an unsupported ready claim because downstream owners can plan around a named pending gate.
### Question 03: When does the default work well?
- **current_section_observation:** The invariant-first default works well for scoped commits, pull-request handoffs, local merges, deliberate keeps, and cleanup where current state and intended destination are observable.
- **supporting_reason:** Git identities, diffs, status, refs, worktree listings, command results, and platform checks can provide independent precondition, action, and postcondition evidence for these transitions.
- **counterargument_or_limit:** Remote review, asynchronous CI, protected settings, or inaccessible hosting state may prevent immediate closure even when the local transition is sound.
- **assumptions_and_boundaries:** Pending external evidence is acceptable only when its consequence, owner, and follow-up are explicit and the report avoids claiming the stronger state.
- **revision_decision:** Add a reliability-state vocabulary of verified, pending, not observed, not applicable with reason, and blocked instead of collapsing all gates to pass or fail.
- **additional_insight_to_add:** Separating local durability from remote readiness allows useful progress without laundering asynchronous uncertainty into completion.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The target model fails when metrics are treated as ceremony, thresholds lack denominators or observation windows, or evidence is collected before a later mutation invalidates it.
- **supporting_reason:** A dashboard can show excellent averages while a particular operation loses an untracked file, publishes the wrong revision, or reports stale tests.
- **counterargument_or_limit:** Lightweight teams may not need formal metric storage, but they still need operation-level checks and an incident record when a safety invariant fails.
- **assumptions_and_boundaries:** The model becomes excessive when it requires remote or release evidence for a local keep that makes no such claim; reliability depth follows consequence, not documentation volume.
- **revision_decision:** Remove the seed's unsupported 18-of-20 accuracy threshold as a default and require any sampled objective to state population, rubric, period, owner, and response to misses.
- **additional_insight_to_add:** A target without a defined remediation path rewards measurement rather than reducing recurrence.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** Alternatives include uniform hard gates, risk-tiered gates, sampled review, automated policy enforcement, and human approval for destructive or shared-state actions.
- **supporting_reason:** These approaches trade latency and operator burden against coverage, consistency, interpretive judgment, and the ability to detect semantic ownership errors.
- **counterargument_or_limit:** Automation can make evidence repeatable but may overfit path rules or normal branch layouts and miss detached heads, generated content, or current user intent.
- **assumptions_and_boundaries:** Human review is not automatically stronger than tooling; reliable design combines machine-observable state with explicit authorization and reasoned scope review.
- **revision_decision:** Recommend invariant gates for every operation, additional full-mode checks by consequence, and periodic sampled audits to improve the procedure rather than excuse individual misses.
- **additional_insight_to_add:** The best tradeoff reduces repeated manual work by automating observations while leaving consequential policy and ownership decisions visible.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Key reliability failures are wrong-repository execution, branch or worktree confusion, broad staging, stale checks, wrong remote or base, partial publication, cleanup before durability, and misleading completion language.
- **supporting_reason:** These errors can all produce successful commands while violating the requested outcome, preserving the wrong state, or removing recovery options.
- **counterargument_or_limit:** A command failure can be safe and informative when it stops before mutation, so failure rate alone is also a poor reliability measure.
- **assumptions_and_boundaries:** Relevant hooks, aliases, submodules, and concurrent processes should be considered when observed, but the target does not require speculative enumeration of every Git extension.
- **revision_decision:** Tie each reliability target to a concrete evidence method and a fail-closed response when the result can change safety.
- **additional_insight_to_add:** Postcondition mismatch is often the earliest measurable symptom of a wrong precondition, so it deserves its own incident category rather than being labeled a retry.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** A good pull-request finish verifies branch, scoped diff, checks, upstream, remote, published commit, pull-request identity, preserved unrelated state, and pending remote gates without deleting the worktree.
- **supporting_reason:** That record connects intent to durable destination and distinguishes verified local facts from asynchronous platform status.
- **counterargument_or_limit:** The same evidence would be excessive for a read-only recommendation, demonstrating why reliability targets must match the claimed transition.
- **assumptions_and_boundaries:** A bad finish reports success after `git push` without checking the revision; a borderline checkpoint is safely committed but mislabeled as merge-ready despite unrun integration tests.
- **revision_decision:** Include contrastive examples that score outcome correctness and claim fidelity rather than number of commands or absence of errors.
- **additional_insight_to_add:** Borderline cases show that preservation can succeed while communication reliability fails, creating downstream risk even though no bytes were lost.
### Question 08: How can the important claims be verified?
- **current_section_observation:** Verify reliability through before-and-after state captures, immutable revision comparison, scoped diff and ownership review, current check records, destination inspection, and sampled handoff audits.
- **supporting_reason:** Multiple independent observations reduce the chance that a successful action is accepted despite a wrong target, stale input, or incomplete postcondition.
- **counterargument_or_limit:** Evidence can still be forged, truncated, or misinterpreted, so sensitive workflows may require protected platform logs or reviewer approval beyond local records.
- **assumptions_and_boundaries:** Verification commands must be selected for the repository and action; this section specifies evidence classes rather than pretending one shell script is universal.
- **revision_decision:** Add an operation reliability record containing requested outcome, risk tier, invariant result, exceptions, destination identity, residual state, and remediation owner.
- **additional_insight_to_add:** Correlating invariant failures with workload and routing records can reveal whether the root cause is procedure design, repository policy, tooling, or ambiguous ownership.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** It is confident that unrelated work preservation, explicit destructive authorization, current evidence, and verified postconditions are necessary; acceptable latency, sample size, and review frequency remain local judgments.
- **supporting_reason:** The local sources consistently emphasize tests, intentional outcomes, state preservation, confirmation, and handoff, but they do not provide a measured universal reliability distribution.
- **counterargument_or_limit:** Even invariant language needs interpretation for exceptional recovery cases where preserving one corrupted state may threaten another, requiring a specialist procedure and explicit authority.
- **assumptions_and_boundaries:** Quantitative targets should be presented only with repository-derived baselines and should never weaken a per-operation safety gate.
- **revision_decision:** Label portable invariants separately from candidate metrics and state that absent measurement is uncertainty, not evidence that a numerical target is met.
- **additional_insight_to_add:** Confidence should be highest around what must be proven and lower around how cheaply or quickly a team can prove it in its environment.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The reliability model implies a three-part result for every finish: state safety, outcome fidelity, and evidence fidelity can succeed or fail independently.
- **supporting_reason:** Work may be preserved safely but sent to the wrong destination, or the correct outcome may occur while the report falsely claims tests or cleanup status.
- **counterargument_or_limit:** More categories can complicate reporting unless the record stays concise and maps each failure to a concrete next action.
- **assumptions_and_boundaries:** The decomposition applies to finish operations; feature correctness and production reliability remain owned by their respective tests and release controls.
- **revision_decision:** Add a reliability envelope that reports these three dimensions, treats invariant breach as an incident, and uses sampled metrics only to prioritize process improvement.
- **additional_insight_to_add:** Because evidence fidelity is independently important, low-drama precise handoffs are a reliability mechanism rather than merely a communication preference.
## Section 020: Failure Mode Table
### Question 01: What decision does this reference help make?
- **current_section_observation:** The failure table must decide what kind of finish failure occurred and whether the next safe response is containment, evidence refresh, bounded retry, roll-forward, recovery, or specialist escalation.
- **supporting_reason:** A precondition refusal, transient remote rejection, partial publication, wrong-target mutation, and destructive data loss have different consequences and must not share a generic "try again" response.
- **counterargument_or_limit:** Classification can delay urgent containment if the operation is still mutating, so stopping further writes and preserving evidence precede fine-grained diagnosis.
- **assumptions_and_boundaries:** The table covers failures of the branch/worktree finish process; implementation defects and production incidents route to their own diagnostic authorities after local state is secured.
- **revision_decision:** Expand the seed's four generic rows into a phase-aware registry with symptom, immediate containment, recovery route, retry gate, and closure evidence.
- **additional_insight_to_add:** Failure classification protects optionality because it prevents a harmless refusal from becoming a destructive incident through an inappropriate recovery command.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** The recommended default is stop mutation, capture actual state and command evidence, preserve local-only work, compare intended with observed state, then choose the narrowest authorized recovery.
- **supporting_reason:** Immediate repeated actions can invalidate refs, logs, status, remote evidence, or worktree contents that reveal what happened and support safe correction.
- **counterargument_or_limit:** A documented idempotent retry may be appropriate immediately for a known transient read or transport failure when no mutation occurred and retry policy permits it.
- **assumptions_and_boundaries:** The default prohibits speculative reset, cleanup, force, or deletion and assumes secrets are redacted from retained diagnostics.
- **revision_decision:** Put a universal containment sequence before the table and require every row to state whether ordinary retry is safe.
- **additional_insight_to_add:** Preserving the failure state is often more valuable than restoring a cosmetically clean tree because recovery depends on knowing the exact partial transition.
### Question 03: When does the default work well?
- **current_section_observation:** Stop-capture-classify works well for failed checks, non-fast-forward push rejection, hook failure, pull-request creation failure, local merge conflict, stale state, and blocked cleanup.
- **supporting_reason:** These cases usually leave observable refs, index state, command output, remote state, or worktree entries from which a bounded next action can be selected.
- **counterargument_or_limit:** External platform outages may offer little diagnostic detail, requiring a pending handoff rather than an immediate causal conclusion.
- **assumptions_and_boundaries:** The approach works when the operator can distinguish no mutation, complete mutation, and partial mutation and can requery any relevant destination.
- **revision_decision:** Organize examples by discovery, verification, save, publication, integration, cleanup, destructive action, and reporting phases.
- **additional_insight_to_add:** Phase location narrows likely invalidated evidence: a pre-save test failure differs materially from a post-push pull-request API failure even if both end with nonzero status.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The generic recovery sequence becomes insufficient when repository integrity is uncertain, credentials may be compromised, user work appears lost, shared history changed unexpectedly, or a production release was triggered.
- **supporting_reason:** Those conditions cross into security, repository recovery, platform administration, or incident-response authority and can worsen under ordinary finish commands.
- **counterargument_or_limit:** Routing should not be used to avoid a simple known correction such as refreshing stale status after a harmless read-only failure.
- **assumptions_and_boundaries:** If containment itself requires mutation, the responsible specialist must authorize and document it; this table can preserve evidence and name the route but not improvise emergency policy.
- **revision_decision:** Mark terminal escalation triggers explicitly and state that the original finish outcome may be suspended or abandoned after a severe incident.
- **additional_insight_to_add:** A failure can change task ownership, so recovery success does not necessarily return control to the original finish flow without reconfirmed intent.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** The main responses are retry, rollback, roll-forward, checkpoint, compensate, wait for external state, or escalate to a specialist owner.
- **supporting_reason:** They trade restoration speed against evidence preservation, history stability, shared-state impact, user-visible interruption, and the chance of compounding partial success.
- **counterargument_or_limit:** Git does not provide true rollback for every untracked deletion or expired object, and remote platforms may make some actions irreversible or permission-bound.
- **assumptions_and_boundaries:** Response selection depends on actual state, authorization, idempotency, and recovery evidence rather than a preference for returning to the pre-action shape.
- **revision_decision:** Add response-selection columns and reserve rollback language for operations whose inverse and durability are genuinely established.
- **additional_insight_to_add:** Roll-forward is often safer after remote publication because deleting shared history to recreate a prior state may have greater blast radius than correcting visibly.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Highest-risk modes include wrong repository or worktree, mixed staging, stale checks, wrong remote or base, rejected push after local commit, pull request absent after push, conflicted local merge, premature cleanup, and unconfirmed discard.
- **supporting_reason:** These modes span identity, ownership, quality, destination, partial transition, and irreversibility, the dimensions most likely to violate the reliability invariants.
- **counterargument_or_limit:** Hooks, aliases, submodules, sparse checkouts, and concurrent automation add variants, but they should be included when observed rather than assumed universally.
- **assumptions_and_boundaries:** A successful command can still instantiate these failures, so symptoms include mismatched postconditions as well as error output.
- **revision_decision:** Include both explicit command failures and silent semantic failures such as pushing the wrong revision or leaving unrelated state staged.
- **additional_insight_to_add:** Silent semantic failures need postcondition checks because no retry loop or shell exit code can detect them reliably on its own.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** A good response to rejected push preserves the local commit, inspects upstream divergence and policy, reports no remote mutation, and waits for an authorized integration decision.
- **supporting_reason:** It contains the failure, retains durable work, avoids history rewrite, and distinguishes local success from remote publication failure.
- **counterargument_or_limit:** If the repository runbook explicitly requires a rebase and the branch is private, that authorized path may proceed after evidence refresh rather than wait for new user input.
- **assumptions_and_boundaries:** A bad response force-pushes immediately; a borderline response retries pull-request creation without first confirming whether the first request succeeded server-side.
- **revision_decision:** Add contrastive cases for no-mutation failure, partial remote success, and destructive incident to demonstrate different retry eligibility.
- **additional_insight_to_add:** Borderline duplicate-action risks show why idempotency keys or destination requery can matter even in workflows that appear to be simple Git operations.
### Question 08: How can the important claims be verified?
- **current_section_observation:** Verify failure handling by capturing pre-action state, command and exit result, actual local and remote post-state, preserved work, selected classification, authorized response, and closure check.
- **supporting_reason:** This sequence reveals whether the mitigation addressed the observed failure or merely changed the repository until the command stopped complaining.
- **counterargument_or_limit:** Some remote details may be inaccessible, so closure can remain pending with an owner rather than falsely verified.
- **assumptions_and_boundaries:** Test fixtures should use disposable repositories, remotes, and worktrees and must never simulate destructive cases against user data.
- **revision_decision:** Add focused fixtures for wrong target detection, mixed staging, non-fast-forward rejection, merge conflict, duplicate pull-request request, and cleanup refusal.
- **additional_insight_to_add:** A failure registry becomes useful when every recurrent row has a reproducible fixture or a documented reason why only review evidence is feasible.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** It is confident that mutation should stop after unexpected state and that local-only evidence should be preserved; the safest correction for a specific history or platform failure remains context-dependent.
- **supporting_reason:** Local sources support inspection, tests, confirmation, intentional saving, and conservative cleanup but do not establish universal recovery commands for every topology.
- **counterargument_or_limit:** Current repository policy can confidently prescribe a response for a known failure, provided its preconditions match the observed state.
- **assumptions_and_boundaries:** Public platform documentation was not refreshed, so API retries, pull-request deduplication, and permission behavior require current verification when consequential.
- **revision_decision:** Distinguish source-backed containment principles from operation-specific recovery judgments and avoid promising universal reversibility.
- **additional_insight_to_add:** Uncertainty is itself a classification input: when it concerns identity, ownership, or loss, escalation is safer than experimentation.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** A structured failure table enables recovery to be designed as a state transition with preconditions and postconditions rather than an improvised list of Git commands.
- **supporting_reason:** This framing makes retry eligibility, invalidated evidence, authorization, and closure measurable and connects directly to reliability and observability records.
- **counterargument_or_limit:** The registry can become stale or enormous if every incidental error receives a permanent row without recurrence or consequence evidence.
- **assumptions_and_boundaries:** New rows should represent distinct causal or recovery behavior, not merely different error wording from the same class.
- **revision_decision:** Add maintenance rules to merge duplicate modes, promote recurrent incidents into tooling or policy, and retire rows only after the prevention mechanism is verified.
- **additional_insight_to_add:** The best failure-table outcome is fewer table lookups over time because common hazards move into precondition checks, idempotent tools, and repository instructions.
## Section 021: Retry Backpressure Guidance
### Question 01: What decision does this reference help make?
- **current_section_observation:** The retry section must decide whether another attempt is safe, useful, authorized, and likely to preserve the intended state after a classified finish failure.
- **supporting_reason:** Retrying a read-only query differs from repeating a commit, push, pull-request creation, merge, cleanup, or discard because those actions have different idempotency and partial-effect risks.
- **counterargument_or_limit:** Some tools provide transactional or idempotent semantics that make repetition safe, but those guarantees must be current and applicable to the exact operation.
- **assumptions_and_boundaries:** The decision begins after the failure table's containment and actual-effect classification; retry is never the first response to unknown destructive or wrong-target state.
- **revision_decision:** Replace generic retry prose with an operation-class matrix covering eligibility, pre-retry revalidation, pacing, attempt budget source, and stop conditions.
- **additional_insight_to_add:** Backpressure protects repository state and operator attention by preventing one unresolved transition from spawning additional mutations or increasingly broad recovery attempts.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** The recommended default is no automatic mutating retry until actual state, failure class, idempotency, authorization, and invalidated evidence have been rechecked.
- **supporting_reason:** A client error may follow a successful server effect, a hook may modify files before failing, or another collaborator may advance the branch while the operator is preparing a retry.
- **counterargument_or_limit:** Read-only observations with classified transient transport failure may use a small policy-bounded retry without full workflow reclassification.
- **assumptions_and_boundaries:** Retry limits come from repository or platform policy when present; absent such evidence, use a conservative bounded attempt and escalate rather than inventing an exponential schedule.
- **revision_decision:** State a gate sequence of classify, requery, refresh, authorize, retry once within policy, verify effect, and stop when any precondition changes.
- **additional_insight_to_add:** A retry budget belongs to the state transition, not each command invocation, preventing nested tools from multiplying attempts invisibly.
### Question 03: When does the default work well?
- **current_section_observation:** Bounded retry works well for transient read queries, temporary network interruption with verified no effect, stale remote observation, and asynchronous platform availability after local durability is secured.
- **supporting_reason:** These cases can often be revalidated without modifying local work and can preserve one clear destination and postcondition across attempts.
- **counterargument_or_limit:** Repeated authorization or policy failures are not transient, even if the platform occasionally returns inconsistent error text.
- **assumptions_and_boundaries:** The action must remain relevant to the same user request, revision, branch, remote, and destination after the wait and requery.
- **revision_decision:** Define safe retry classes separately from wait-and-observe, manual-decision, and never-automatic classes.
- **additional_insight_to_add:** Waiting is sometimes stronger backpressure than retrying because remote CI or review may converge without any new write.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** Retry becomes wrong when the first attempt may have mutated state, the target changed, ownership is uncertain, a destructive action failed partially, policy denies access, or repository integrity is in question.
- **supporting_reason:** Repetition under those conditions can duplicate platform objects, overwrite shared history, compound loss, or invalidate the evidence needed for recovery.
- **counterargument_or_limit:** A specialist recovery procedure may intentionally repeat a lower-level operation after establishing stronger invariants, but that is not ordinary finish retry.
- **assumptions_and_boundaries:** A changed commit, index, branch, worktree, remote ref, pull-request state, policy, or user outcome consumes the current retry decision and requires reclassification.
- **revision_decision:** Add hard stop conditions and forbid automatic retry for force, reset, discard, cleanup, conflict resolution, and unknown-effect shared mutations.
- **additional_insight_to_add:** The point of backpressure is not merely rate control; it prevents authority and scope from expanding as frustration increases.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** Alternatives are immediate bounded retry, delayed retry with jitter, destination requery, wait for asynchronous convergence, roll-forward, preservation checkpoint, or human and specialist escalation.
- **supporting_reason:** These options trade latency against duplicate effects, load, coordination, evidence freshness, and the cost of holding local state unresolved.
- **counterargument_or_limit:** Elaborate backoff is unnecessary for one-off local commands and can create false sophistication when the real blocker is policy or intent.
- **assumptions_and_boundaries:** Timing parameters should follow current platform guidance or repository tooling; this reference supplies selection logic rather than universal seconds and attempt counts.
- **revision_decision:** Use qualitative pacing categories and require locally configured numeric schedules to name their source and expiration trigger.
- **additional_insight_to_add:** A durable checkpoint can release operator pressure without pretending the blocked publication or integration completed.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Retry gotchas include hidden retries in clients, duplicate pull requests, repeated hooks, expiring credentials, rate limits, non-fast-forward divergence, changing CI status, and retries after cleanup removed context.
- **supporting_reason:** These mechanisms can multiply effects or change preconditions between visible attempts, making a nominal one-retry rule inaccurate.
- **counterargument_or_limit:** Not every client retries automatically, so inspect actual tool behavior rather than assuming hidden repetition.
- **assumptions_and_boundaries:** Retry records should count logical attempts across wrappers and subprocesses when observable and avoid logging secrets or sensitive remote responses.
- **revision_decision:** Require visibility into tool-level retry behavior for consequential actions and requery destination state after ambiguous transport failures.
- **additional_insight_to_add:** Cleanup should be held behind a stability window or explicit postcondition because it removes the easiest local basis for diagnosing delayed remote failures.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** A good retry after a pull-request API timeout queries existing requests by verified head and base, finds none, confirms the same revision and intent, retries within policy, then verifies one resulting request.
- **supporting_reason:** It controls duplicate risk, refreshes mutable inputs, uses one logical budget, and validates the postcondition independently.
- **counterargument_or_limit:** If the API query is itself unavailable, waiting and reporting publication-only partial success is safer than blind creation.
- **assumptions_and_boundaries:** A bad retry force-pushes after rejection; a borderline retry repeats a safe read indefinitely while preventing a clear human handoff.
- **revision_decision:** Include examples for safe read retry, ambiguous remote mutation, policy denial, and destructive failure.
- **additional_insight_to_add:** A retry can be technically harmless yet operationally harmful when it delays escalation past the point where a maintainer could resolve the blocker.
### Question 08: How can the important claims be verified?
- **current_section_observation:** Verify retry behavior with a logical-attempt record containing failure class, actual effect, pre-retry state hash or identities, policy budget, delay rationale, result, and stop reason.
- **supporting_reason:** This record exposes duplicate attempts, changing targets, hidden mutations, and whether the eventual success actually belongs to the same state transition.
- **counterargument_or_limit:** A full record may be excessive for a harmless local read, so compact logging can retain only classification, count, and final observation.
- **assumptions_and_boundaries:** Tests should inject transient, permanent, and ambiguous failures in disposable fixtures and assert both action count and preserved state.
- **revision_decision:** Add verification cases for no-effect retry, server-effect/client-error ambiguity, changed-remote stop, hook mutation stop, and exhausted-budget escalation.
- **additional_insight_to_add:** Measuring retries per completed transition rather than per command better reveals unstable dependencies and misleading automation wrappers.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** It is confident that unknown-effect mutation and destructive failure should not be retried automatically; exact delay, count, and jitter values remain platform- and policy-dependent.
- **supporting_reason:** State and authorization logic are portable, while service rate limits, idempotency behavior, and recommended backoff can change and were not externally refreshed here.
- **counterargument_or_limit:** A repository-owned tool may encode current safe values and stronger guarantees, making its documented policy more authoritative than generic caution.
- **assumptions_and_boundaries:** The reference does not claim that one retry is universally optimal and labels external platform semantics as requiring current verification.
- **revision_decision:** Preserve high-confidence stop rules, make numeric budgets configurable, and require provenance for any asserted retry schedule.
- **additional_insight_to_add:** When uncertainty concerns whether an effect occurred, observation has higher priority than another action; when observation is unavailable, escalate or wait.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** Retry backpressure implies a monotonic safety rule: each failed attempt must add evidence or reduce uncertainty, or the sequence should stop.
- **supporting_reason:** Attempts that merely repeat the same inputs against unchanged unknown state consume time and may increase side effects without improving the decision basis.
- **counterargument_or_limit:** Truly stochastic transient systems can succeed without new evidence, but retries still need a bounded externally justified policy and harmless semantics.
- **assumptions_and_boundaries:** The monotonic rule measures decision information and state safety, not guaranteed progress toward the user's preferred outcome.
- **revision_decision:** End with a retry ledger and escalation trigger that require every attempt to state what changed, what remained invariant, and why another attempt is justified.
- **additional_insight_to_add:** Aggregated exhausted budgets can identify unreliable platform dependencies or weak idempotency, guiding investment in wrappers, caching, or clearer handoff tooling.
## Section 022: Observability Checklist
### Question 01: What decision does this reference help make?
- **current_section_observation:** The observability section must decide which evidence is necessary to reconstruct and audit a branch-finish transition without collecting irrelevant, sensitive, or unreviewable data.
- **supporting_reason:** Reliable diagnosis requires intent, state identity, ownership, checks, action, destination, postcondition, retries, and residual risk, while raw terminal transcripts can obscure those facts and expose secrets.
- **counterargument_or_limit:** Highly regulated or incident-prone repositories may require stronger immutable audit records than this portable minimum.
- **assumptions_and_boundaries:** The checklist governs finish-process telemetry and handoff evidence, not general application logging or production tracing.
- **revision_decision:** Replace the seed's loose bullet list with a compact transition schema, event timeline, redaction rules, retention ownership, and consequence-based optional fields.
- **additional_insight_to_add:** Observability is useful only when each field can change a decision, verify a postcondition, or explain a failure; everything else competes with the signal.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** The recommended default is a structured precondition-action-postcondition record linked by one transition identity and summarized for human review.
- **supporting_reason:** Structured fields make missing ownership, stale checks, wrong targets, partial effects, and pending gates visible without requiring a reviewer to replay an entire session.
- **counterargument_or_limit:** A concise record may omit diagnostic detail needed after a rare failure, so retain bounded supporting output or pointers when the consequence warrants it.
- **assumptions_and_boundaries:** Sensitive values, credentials, tokens, private file contents, and unnecessary personal data are excluded or redacted under repository policy.
- **revision_decision:** Define mandatory core fields for all mutations and extended fields for remote, integration, cleanup, discard, retry, and recovery operations.
- **additional_insight_to_add:** The same schema can drive both real-time safety gates and later metrics, reducing divergence between operational evidence and retrospective reporting.
### Question 03: When does the default work well?
- **current_section_observation:** A compact structured record works well for commits, pushes, pull requests, local merges, keeps, checkpoints, cleanup, and blocked handoffs with observable repository state.
- **supporting_reason:** These transitions expose stable identifiers such as repository path, worktree, branch, commit, remote ref, pull-request identity, and command result.
- **counterargument_or_limit:** Repository corruption or inaccessible platforms may make some fields unknown, which must be represented explicitly rather than guessed.
- **assumptions_and_boundaries:** The operator can persist the record in an authorized journal or handoff channel and can state the time or ordering relationship between observations and mutations.
- **revision_decision:** Include evidence states for verified, pending, unavailable, inapplicable with reason, and blocked values.
- **additional_insight_to_add:** Ordering matters more than wall-clock precision for many local transitions because it determines whether a check preceded or followed the mutation it is claimed to cover.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The default fails when records are generated after the fact from memory, copied between revisions, detached from the actual target, or so verbose that reviewers cannot locate consequences.
- **supporting_reason:** Such telemetry creates confidence without traceability and can preserve stale or misleading claims longer than the underlying state exists.
- **counterargument_or_limit:** Emergency containment may prioritize preserving raw evidence first, with structured summarization performed after the repository is stable.
- **assumptions_and_boundaries:** Observability must not delay a required stop or expose secrets; when storage policy is unknown, retain the smallest safe handoff and name the limitation.
- **revision_decision:** Add freshness, correlation, size, and privacy gates plus a prohibition on treating logs as authorization.
- **additional_insight_to_add:** Excess data can be an observability failure because it raises review cost and hides the one state mismatch that matters.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** Alternatives include a concise handoff, structured journal entry, command-output attachment, immutable platform audit log, or full incident evidence bundle.
- **supporting_reason:** They trade storage and privacy cost against diagnostic depth, tamper resistance, portability, and the speed of human review.
- **counterargument_or_limit:** A single format cannot satisfy all repositories, so the reference should specify semantic fields rather than mandate a logging backend.
- **assumptions_and_boundaries:** Retention duration, access controls, and data location follow repository and organizational policy, not generic agent preference.
- **revision_decision:** Recommend the smallest evidence tier that supports the action consequence, with pointers to larger artifacts rather than duplication.
- **additional_insight_to_add:** Separating summary from evidence location allows concise handoff while preserving deeper diagnostics only where governance permits.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Observability gotchas include secrets in remote URLs, environment output, or diffs; truncated status; misleading changed-file counts; stale commit IDs; hidden retries; and missing unrelated-state evidence.
- **supporting_reason:** These gaps can expose sensitive material or make a partial or wrong-target action look complete.
- **counterargument_or_limit:** Aggressive redaction can remove the identifiers needed to distinguish destinations, so preserve non-secret canonical identity or an authorized opaque reference.
- **assumptions_and_boundaries:** The record should not store full file contents by default and should note when submodules, sparse checkouts, generated files, or linked worktrees affect interpretation.
- **revision_decision:** Add field-level redaction guidance and require before/after summaries to share a transition identity.
- **additional_insight_to_add:** Logging the reason a field is absent is more useful than leaving it blank because absence can mean inapplicable, inaccessible, forgotten, or intentionally redacted.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** A good record names the requested pull request, repository/worktree, owned diff summary, checks and revision, remote/base, push result, pull-request head, preserved unrelated file, pending CI, and cleanup status.
- **supporting_reason:** It supports outcome verification and next-owner action without exposing raw source or credentials.
- **counterargument_or_limit:** A security-sensitive repository may need destination identifiers masked in the user-facing summary while retaining protected audit correlation.
- **assumptions_and_boundaries:** A bad record dumps a transcript containing a token; a borderline record lists commands and success codes but omits the branch revision and postcondition.
- **revision_decision:** Include a compact good record and contrast it with raw-dump and command-only anti-examples.
- **additional_insight_to_add:** Command lists describe activity, whereas observability must describe state change and consequence.
### Question 08: How can the important claims be verified?
- **current_section_observation:** Verify observability by schema validation, required-field coverage by operation type, redaction tests, before/after identity correlation, and reviewer reconstruction exercises.
- **supporting_reason:** These checks demonstrate that a record is complete enough to reproduce the decision while remaining bounded and privacy-aware.
- **counterargument_or_limit:** Automated schema checks cannot establish whether an ownership judgment or narrative consequence is truthful, so sampled review remains necessary.
- **assumptions_and_boundaries:** Fixtures use synthetic repositories and synthetic secrets; they do not copy real credentials or user content into tests.
- **revision_decision:** Add acceptance checks that a reviewer can identify intended outcome, actual result, preserved state, pending gates, and next owner from the record alone.
- **additional_insight_to_add:** Time-to-reconstruct can be measured locally when workflow speed matters, but the seed's percentile targets should not be demanded without a defined population and collection method.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** It is confident that target identity, state transition, evidence scope, residual risk, and authorization boundaries must be observable; retention period and logging platform remain local choices.
- **supporting_reason:** The local corpus emphasizes intentional state handling and concise handoff but does not establish universal telemetry infrastructure or latency distributions.
- **counterargument_or_limit:** Legal, privacy, or compliance requirements may forbid retaining some otherwise useful evidence or may mandate additional immutable records.
- **assumptions_and_boundaries:** The reference treats public platform fields as potentially changeable and requires current policy before claiming a retention or audit guarantee.
- **revision_decision:** Label the semantic minimum as portable guidance and route storage, access, and retention decisions to current organizational authority.
- **additional_insight_to_add:** Unknown governance should reduce collection to the minimum safe operational record, not trigger indiscriminate logging.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** A shared transition schema can connect workload classification, reliability invariants, failure modes, retry budgets, and outcome metrics into one traceable control loop.
- **supporting_reason:** Reusing the same identifiers and evidence states prevents each section from producing incompatible narratives about the same branch action.
- **counterargument_or_limit:** A unified schema can become rigid if repositories cannot extend it for submodules, release gates, or specialized hosting workflows.
- **assumptions_and_boundaries:** Extensions must preserve core meaning and privacy controls while adding repository-specific fields through owned policy.
- **revision_decision:** End with extension and maintenance rules: stable core fields, namespaced local additions, versioned schema changes, and fixture-backed redaction.
- **additional_insight_to_add:** Observability quality can be improved upstream by designing commands and tools to emit state identities and postconditions directly rather than parsing prose after execution.
## Section 023: Performance Verification Method
### Question 01: What decision does this reference help make?
- **current_section_observation:** The performance section must decide whether a finish workflow or guidance change reduces time or effort without degrading state safety, outcome fidelity, evidence fidelity, or reviewer clarity.
- **supporting_reason:** Faster commands are not a useful improvement when they increase retries, wrong-target actions, unsupported claims, or recovery work.
- **counterargument_or_limit:** Many teams need no formal benchmark for infrequent branch finishes; a qualitative verification and invariant pass can be sufficient.
- **assumptions_and_boundaries:** The method measures repository workflow performance, not application runtime, compiler speed, or production deployment performance unless a separate owner defines those scopes.
- **revision_decision:** Replace mandatory generic counts with a quality-adjusted measurement protocol selected only for a named workflow decision.
- **additional_insight_to_add:** Performance should be measured from actionable request to verified durable handoff, because optimizing an internal command can shift cost to reviewers or recovery.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** The recommended default is establish correctness invariants first, define one start and stop event, segment by workload mode, and compare end-to-end duration plus rework on representative cases.
- **supporting_reason:** This design prevents compact commits, remote pull requests, and destructive cleanup from being pooled into a misleading average.
- **counterargument_or_limit:** Controlled fixtures cannot reproduce all network, policy, review, or human coordination variability present in real repositories.
- **assumptions_and_boundaries:** Timing begins only after the required request/context is available and ends at a verified postcondition or explicit blocked handoff, not at the last command invocation.
- **revision_decision:** Add a measurement packet with hypothesis, cohort, workload dimensions, start/stop, safety gates, attempts, active versus waiting time, result, and uncertainty.
- **additional_insight_to_add:** Separating active effort from external waiting reveals whether a change improves operator workflow or merely observes a faster platform interval.
### Question 03: When does the default work well?
- **current_section_observation:** The protocol works well for repeated scoped commits, pull-request handoffs, repository wrappers, verification scripts, and reviewer checklists with enough comparable operations.
- **supporting_reason:** These workflows expose stable transition boundaries and can be exercised on disposable fixtures or sampled from structured operational records.
- **counterargument_or_limit:** Rare destructive incidents should be evaluated through safety fixtures and recovery exercises rather than optimized from sparse live timings.
- **assumptions_and_boundaries:** Comparisons use equivalent repository state, checks, remote conditions, and operator authority or explicitly model those differences.
- **revision_decision:** Define fixture, shadow, and observational evaluation modes with clear claims each can support.
- **additional_insight_to_add:** Reviewer reconstruction time is useful when the change primarily improves evidence structure rather than shell execution.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** Performance verification fails when samples mix outcomes, omit failed or blocked runs, use tool-call count as productivity, or report percentiles without a defined population.
- **supporting_reason:** These practices reward batching, hidden retries, and unsafe shortcuts while excluding precisely the cases that create operational cost.
- **counterargument_or_limit:** Tool-call count can diagnose a specific wrapper regression when command semantics remain fixed, but it is not a general quality metric.
- **assumptions_and_boundaries:** Any invariant breach invalidates a performance win for the affected cohort and is reported as an incident rather than folded into average latency.
- **revision_decision:** Add exclusion and validity rules for warm caches, network outages, asynchronous waits, policy changes, reviewer interruptions, and changed workload mix.
- **additional_insight_to_add:** A benchmark that cannot explain its missing and failed runs is measuring survivorship rather than workflow performance.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** Alternatives include deterministic fixture benchmarks, before-and-after operational sampling, shadow decision review, expert walkthrough, and no timing measurement when consequence is low.
- **supporting_reason:** They trade realism, repeatability, privacy, sample volume, setup cost, and exposure to live repository risk.
- **counterargument_or_limit:** Live A/B experiments may be inappropriate for destructive or shared-state behavior because the cost of a variant failure is not ethically or operationally acceptable.
- **assumptions_and_boundaries:** Choose a method that can answer the named hypothesis without mutating user data or weakening repository controls.
- **revision_decision:** Recommend fixtures for command mechanics, shadow review for decision accuracy, and observational cohorts for end-to-end workflow effects.
- **additional_insight_to_add:** Combining methods can separate a faster mechanism from a clearer decision interface without claiming either study proves the other.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Performance gotchas include warm caches, repository size, generated output, CI queue time, network locality, hidden retries, human wait, concurrent edits, and different check coverage.
- **supporting_reason:** Each factor can change elapsed time independently of the reference or workflow change being evaluated.
- **counterargument_or_limit:** Perfect control is impossible in operational samples, so stratification and uncertainty reporting are more realistic than pretending all variance can be removed.
- **assumptions_and_boundaries:** Sensitive repository names, paths, timing traces, and reviewer identities follow privacy policy and can be aggregated or pseudonymized.
- **revision_decision:** Require workload and environment descriptors plus explicit treatment of censored, blocked, failed, and abandoned runs.
- **additional_insight_to_add:** Hidden retry count is both a reliability and performance signal because apparent success latency can conceal repeated external load and duplicate risk.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** A good study compares the same pull-request fixtures before and after a destination-verification helper, preserves all invariants, reports active and wait time, retries, errors, and reviewer reconstruction.
- **supporting_reason:** The result can attribute reduced wrong-destination rework or faster verification to a specific mechanism within a bounded cohort.
- **counterargument_or_limit:** Fixture results do not prove the helper behaves identically under every hosting permission or outage condition.
- **assumptions_and_boundaries:** A bad study celebrates fewer commands after removing checks; a borderline study reports lower median duration while excluding blocked and failed finishes.
- **revision_decision:** Include contrastive studies showing valid improvement, unsafe shortcut, and incomplete percentile reporting.
- **additional_insight_to_add:** A slower median can still be a better system if it eliminates high-consequence recovery tails, so distribution and incident context matter.
### Question 08: How can the important claims be verified?
- **current_section_observation:** Verify a performance claim with a preregistered hypothesis, reproducible fixture or defined cohort, raw operation records, invariant results, statistical summary appropriate to sample size, and independent review.
- **supporting_reason:** These artifacts let another reviewer check start/stop boundaries, exclusions, segmentation, and whether the claimed causal mechanism actually changed.
- **counterargument_or_limit:** Small samples may support only descriptive observations, not stable percentile or causal claims.
- **assumptions_and_boundaries:** Repeated fixture runs randomize or alternate variants where feasible and isolate destructive actions in disposable repositories.
- **revision_decision:** Add a pass rule requiring the claimed improvement, no invariant regression, bounded uncertainty, and no unexplained missing cohort.
- **additional_insight_to_add:** Publishing the measurement packet alongside the claim prevents future maintainers from carrying forward a number after its tooling or workload assumptions change.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** It is confident that status-before-mutation, scoped review, and postcondition verification are necessary; no local evidence supports universal latency percentiles or speed improvements for this reference.
- **supporting_reason:** The local source corpus provides workflow procedures and qualitative safety rationale, not a benchmark dataset or controlled timing study.
- **counterargument_or_limit:** A repository may already collect valid operational telemetry that supports precise local targets once its methodology is reviewed.
- **assumptions_and_boundaries:** Without such data, performance language remains a verification method and candidate metric set rather than a claimed result.
- **revision_decision:** Remove implied quantitative pass thresholds and clearly separate measured local findings from portable recommendations.
- **additional_insight_to_add:** Refusing unsupported precision makes later real measurements more useful because their scope and evidence cannot be confused with inherited numbers.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** Quality-adjusted performance implies that the optimization target is expected total handling cost, including review, retries, waiting, and recovery, constrained by safety invariants.
- **supporting_reason:** A shortcut can reduce the happy-path command sequence while increasing rare but expensive wrong-target or cleanup incidents.
- **counterargument_or_limit:** Converting every consequence into a single cost number can hide ethical or irreversible boundaries that should remain hard constraints.
- **assumptions_and_boundaries:** The guidance therefore uses multi-dimensional reporting rather than monetizing user work loss or unauthorized publication.
- **revision_decision:** End with a decision rule: optimize active and elapsed time only after invariant gates, report tails and incidents separately, and revisit the method when workload mix changes.
- **additional_insight_to_add:** Performance instrumentation can reveal architecture and policy friction, but those findings should route to the owning system instead of encouraging broader agent privileges.
## Section 024: Scale Boundary Statement
### Question 01: What decision does this reference help make?
- **current_section_observation:** The scale section must decide when a finish remains one coherent repository transition and when it requires sequencing, coordination, or a separate multi-repository and release orchestrator.
- **supporting_reason:** Scale risk grows with independent owners, indexes, branches, destinations, approvals, checks, and failure recovery, not simply with lines or files changed.
- **counterargument_or_limit:** A repository-owned transactional tool can coordinate several units safely, so multiple components do not automatically require manual fragmentation.
- **assumptions_and_boundaries:** This guide can classify and hand off a scaled operation but does not invent distributed locks, release atomicity, or cross-repository rollback semantics.
- **revision_decision:** Define portable stop conditions and a routing contract for multi-worktree, multi-owner, multi-remote, multi-repository, and long-running workflows.
- **additional_insight_to_add:** The key scale question is how many independently mutable truths must remain coherent between inspection and postcondition.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** The recommended default is one accountable mutation owner per branch/worktree unit, with parallelism limited to independent read-only discovery or separately owned units.
- **supporting_reason:** Serializing writes to a shared index, branch, worktree, remote ref, or cleanup target prevents stale evidence and conflicting ownership from being converted into nondeterministic state.
- **counterargument_or_limit:** Merge queues and transaction-aware orchestrators may safely serialize or reconcile writes internally, making external one-at-a-time execution unnecessary.
- **assumptions_and_boundaries:** The default requires a coordinator when several units share a destination or ordering constraint and does not equate one owner with one person permanently.
- **revision_decision:** State that mutation ownership may transfer only at a durable checkpoint with current state, evidence, and next-action authority recorded.
- **additional_insight_to_add:** Scale safely by partitioning authority and postconditions, not by giving every worker broader Git permissions.
### Question 03: When does the default work well?
- **current_section_observation:** Single-owner units work well for independent feature worktrees, separate repositories with independent outcomes, and monorepo changes that can be sequenced through one verified destination.
- **supporting_reason:** Each unit retains a complete request-to-postcondition story while a coordinator manages only shared ordering and integration evidence.
- **counterargument_or_limit:** Cross-cutting schema or API changes may require synchronized commits and compatibility staging that cannot be safely treated as independent finishes.
- **assumptions_and_boundaries:** The effective case has explicit dependency order, stable identifiers, bounded checks, and a recovery plan for each partial result.
- **revision_decision:** Add a scale-mode table for single unit, sequenced units, merge-queue coordination, and explicit orchestration.
- **additional_insight_to_add:** Independent read analysis can run concurrently, but its conclusions must be refreshed if another unit mutates the shared state before action.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** This reference becomes insufficient when an outcome requires atomic cross-repository release, coordinated migrations, shared-history rewrites, production rollout, platform administration, or conflict resolution across owners.
- **supporting_reason:** Those workflows need ordering, approvals, rollback or roll-forward, observability, and partial-failure contracts beyond one branch finish.
- **counterargument_or_limit:** The finish guide may still own the final branch preservation or pull-request handoff for each unit after the orchestrator defines the broader plan.
- **assumptions_and_boundaries:** If no orchestrator or owner exists, the safe response is preservation and escalation rather than ad hoc parallel mutation.
- **revision_decision:** Name terminal handoff triggers and require the orchestrator to return per-unit durable state plus global outcome evidence.
- **additional_insight_to_add:** A scaled workflow can terminate the original finish request if its assumptions no longer hold, so return is conditional rather than guaranteed.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** Alternatives are sequential finishing, independent parallel units, merge-queue serialization, coordinated two-phase handoff, preservation checkpoints, or a specialized release orchestrator.
- **supporting_reason:** They trade throughput against atomicity, stale-state risk, coordinator load, review complexity, and recoverability after partial success.
- **counterargument_or_limit:** A two-phase protocol can create long-lived prepared state and blocking coordination without providing true atomicity across Git and hosting systems.
- **assumptions_and_boundaries:** Select an approach from current repository tooling and failure semantics; this reference does not promise distributed transactions.
- **revision_decision:** Compare alternatives by shared resources, ordering, partial-effect visibility, cancellation, and recovery ownership.
- **additional_insight_to_add:** Explicitly accepting visible partial progress can be safer than simulating atomicity with forceful rollback across already shared revisions.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Scale gotchas include two workers staging in one worktree, stale branch heads, shared remote-ref races, duplicate pull requests, cleanup of an active worktree, submodule drift, and coordinator context loss.
- **supporting_reason:** These failures arise when an observation or authorization is assumed to remain exclusive while another participant changes the same state.
- **counterargument_or_limit:** Isolation tooling can prevent some collisions, but it does not resolve semantic ownership, destination selection, or global ordering.
- **assumptions_and_boundaries:** Locks and leases require owners, expiry, recovery, and verification; an abandoned lock must not be removed merely because it is old.
- **revision_decision:** Add coordination invariants for exclusive mutation, state version checks, durable checkpoints, and no cleanup while another unit depends on the state.
- **additional_insight_to_add:** Context drift is a concurrency problem across time: a long-running agent can conflict with its own earlier assumptions just as two agents can conflict concurrently.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** A good scaled finish assigns independent worktrees and owners, records each revision and checks, then lets one verified merge queue serialize updates to the shared base.
- **supporting_reason:** Local work remains isolated, shared mutation has one authority, and every partial outcome is observable and recoverable.
- **counterargument_or_limit:** A merge queue may rerun or alter integration order, so source-branch checks do not substitute for queue-result evidence.
- **assumptions_and_boundaries:** A bad case lets three agents commit and clean the same worktree; a borderline case isolates worktrees but lets each push to the same remote ref without coordination.
- **revision_decision:** Include examples showing that filesystem isolation alone does not establish destination or integration safety.
- **additional_insight_to_add:** Good scale design centralizes only the truly shared decision and keeps independent evidence local to each unit.
### Question 08: How can the important claims be verified?
- **current_section_observation:** Verify scaled handling with unit ownership records, worktree and ref inventories, state-version checks before writes, orchestrator logs, per-unit postconditions, and partial-failure drills in disposable environments.
- **supporting_reason:** These artifacts demonstrate that concurrent work did not share an uncoordinated mutation target and that recovery can identify every durable result.
- **counterargument_or_limit:** Logs cannot prove absence of an uninstrumented writer, so repository permissions, hooks, or coordination controls may be needed for stronger guarantees.
- **assumptions_and_boundaries:** Verification avoids destructive live experiments and uses synthetic remotes for race, cancellation, lease, and partial-success fixtures.
- **revision_decision:** Add a scale handoff packet with dependency graph, unit owners, shared resources, ordering, mutation leases, evidence invalidation, and global closure.
- **additional_insight_to_add:** A state-version mismatch should fail closed before mutation and feed a coordination metric rather than trigger an automatic forceful reconciliation.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** It is confident that shared mutable state needs coordination and that per-unit ownership and postconditions reduce ambiguity; the best orchestration mechanism remains repository-specific.
- **supporting_reason:** Git and worktree state are observable locally, while merge queues, hosting guarantees, deployment systems, and organizational authority vary and can change.
- **counterargument_or_limit:** Some small teams can coordinate effectively through a simple explicit handoff rather than adopting formal locking infrastructure.
- **assumptions_and_boundaries:** No external platform guarantees were refreshed, so atomicity, queue semantics, lease behavior, and rate limits require current verification.
- **revision_decision:** Keep portable invariants strong and label coordination technology, throughput limits, and timeout values as local policy judgments.
- **additional_insight_to_add:** Scale uncertainty should reduce simultaneous mutation, not motivate optimistic parallel writes to discover conflicts empirically.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The scale boundary implies that a finish workflow is composable when each unit exports a durable revision, verified local state, dependency declaration, and explicit next-owner contract.
- **supporting_reason:** These outputs let an orchestrator reason about ordering and partial success without sharing every worker's full context or granting all workers access to global mutation.
- **counterargument_or_limit:** Compact unit summaries can omit hidden semantic coupling, so dependency declarations still need review and integration tests.
- **assumptions_and_boundaries:** Composition requires stable identities and evidence freshness; mutable branch names alone are inadequate handoff keys.
- **revision_decision:** End with a scale contract that favors immutable revisions, one writer per shared target, checkpointed context, and global verification after integration.
- **additional_insight_to_add:** Repeated coordination pressure can indicate architectural coupling or unclear ownership that should be improved outside the branch-finish process.
## Section 025: Future Refresh Search Queries
### Question 01: What decision does this reference help make?
- **current_section_observation:** The refresh section must decide which potentially stale claim deserves new evidence, where to search, and what result would change branch-finish guidance.
- **supporting_reason:** Generic searches for "best practices" collect plausible prose without resolving concrete uncertainty about Git semantics, hosting behavior, repository policy, or local source drift.
- **counterargument_or_limit:** Stable Git concepts may not need frequent external refresh when local commands and current installed documentation already establish the relevant behavior.
- **assumptions_and_boundaries:** These are future query plans only; no query was executed and no public source was refreshed during this no-browse evolution.
- **revision_decision:** Replace the three generic seed phrases with a claim-triggered query registry covering local corpus drift, Git worktree/history semantics, and hosting-specific pull-request, CI, and protection behavior.
- **additional_insight_to_add:** A useful query names the decision it can change and the authority level required, preventing search volume from being mistaken for evidence quality.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** The recommended default is inspect current repository policy and local source versions first, then query primary official documentation only for a consequential unresolved or changed fact.
- **supporting_reason:** User intent, live Git state, and repository instructions govern the operation, while public documentation cannot establish local ownership, remote choice, or cleanup authorization.
- **counterargument_or_limit:** A local source can itself be stale or conflict with current tool behavior, so primary upstream documentation becomes necessary when the operation depends on that fact.
- **assumptions_and_boundaries:** Search should be permitted, network evidence should be accessible, and the operator should record product/version applicability rather than relying on snippets.
- **revision_decision:** Add a retrieval order and stop rule requiring one current authoritative answer or an explicit unresolved boundary before broader searching.
- **additional_insight_to_add:** Refresh effort should follow expected decision impact, not calendar age alone; a changed branch-protection rule matters more than a cosmetic documentation update.
### Question 03: When does the default work well?
- **current_section_observation:** Claim-driven refresh works well when a command version changed, local source hashes drift, hosting APIs behave ambiguously, protection rules block publication, or reusable CI configuration affects required checks.
- **supporting_reason:** Each case has a specific primary authority and an observable operation whose decision can be reevaluated after retrieval.
- **counterargument_or_limit:** Some platform semantics are account- or repository-configured and cannot be inferred from public docs without live authorized state.
- **assumptions_and_boundaries:** The query log includes access date, URL, relevant version or product scope, extracted claim, conflict, and resulting guidance change.
- **revision_decision:** Group queries by local corpus, Git core, GitHub pull requests/protection, GitHub Actions, and repository instruction examples.
- **additional_insight_to_add:** Search results can narrow what to inspect live, but live state remains necessary for whether a documented capability is enabled or required here.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** The method fails when search is broad, secondary-source-led, snippet-based, detached from version, or used to override explicit repository policy and user authorization.
- **supporting_reason:** Such evidence can be current yet inapplicable, or authoritative generally while irrelevant to the configured repository and requested outcome.
- **counterargument_or_limit:** A high-quality secondary technical analysis can identify an issue or terminology, but the consequential claim should still be checked against primary sources or direct behavior.
- **assumptions_and_boundaries:** Do not browse merely to avoid read-only local inspection, and do not expose repository-sensitive terms in external queries without authorization.
- **revision_decision:** Add reject criteria for SEO summaries, undated copies, search snippets, examples without revision, and claims that cannot name their operational consequence.
- **additional_insight_to_add:** More sources can worsen confidence when they describe different Git versions, hosts, or repository configurations without explicit applicability mapping.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** Alternatives include installed command help, local source diffing, official manuals, official hosting docs, release notes, repository history, direct disposable experiments, and maintainer clarification.
- **supporting_reason:** They trade freshness, specificity, authority, reproducibility, network dependence, and risk of testing against live state.
- **counterargument_or_limit:** Command help describes installed syntax but may not explain hosting policy or local organizational intent.
- **assumptions_and_boundaries:** Disposable experiments validate behavior only for the tested version and configuration and must not mutate user repositories or remote production state.
- **revision_decision:** Pair each query family with its preferred fallback and the claim type it cannot answer.
- **additional_insight_to_add:** Triangulation is strongest when documentation explains intended semantics and a disposable fixture confirms the locally installed behavior.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Refresh gotchas include moved URLs, versionless pages, default-branch drift, product-tier differences, deprecated API fields, conflicting cleanup guidance, and confusing examples with guarantees.
- **supporting_reason:** These issues can turn a correct historical source into unsafe current advice or make an illustrative command appear universally authorized.
- **counterargument_or_limit:** Not every moved page changes semantics, so a URL change alone is a refresh signal rather than evidence of behavioral drift.
- **assumptions_and_boundaries:** Preserve prior evidence and label supersession instead of silently replacing it, especially where the local source conflict remains informative.
- **revision_decision:** Require query results to record unchanged, clarified, contradicted, superseded, or unresolved status and which sections need reevaluation.
- **additional_insight_to_add:** Hash drift in a local skill should trigger semantic comparison, not automatic trust in the newer file or duplicate counting as independent corroboration.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** A good refresh asks whether current Git worktree removal semantics preserve dirty state for the installed version, reads the matching official manual, and tests only a disposable repository if ambiguity remains.
- **supporting_reason:** The query has a concrete cleanup decision, primary authority, local applicability, and a safe verification path.
- **counterargument_or_limit:** Official semantics still do not authorize removal of a user's worktree; intent and local policy remain separate.
- **assumptions_and_boundaries:** A bad query searches "best Git workflow"; a borderline query reads current GitHub docs but assumes those controls are configured in the target repository.
- **revision_decision:** Add contrastive query records showing decision linkage, source authority, and live-state boundary.
- **additional_insight_to_add:** Good refresh output often narrows a claim rather than replacing it with a stronger universal rule.
### Question 08: How can the important claims be verified?
- **current_section_observation:** Verify the refresh process by replaying queries, opening primary pages, recording exact applicability, comparing local hashes or versions, and tracing each accepted finding to a changed or reaffirmed guidance sentence.
- **supporting_reason:** This chain demonstrates that search affected a real decision and that the reference did not merely accumulate links.
- **counterargument_or_limit:** Pages and search indexes change, so a future reviewer may need archived revision identifiers or local notes rather than assuming identical results.
- **assumptions_and_boundaries:** Verbatim quotation remains minimal and copyright-compliant; the record emphasizes paraphrased claim, evidence location, and operational consequence.
- **revision_decision:** Add a refresh-result schema with trigger, query, source, version/date, claim, conflict, local experiment, decision, sections affected, and next expiry signal.
- **additional_insight_to_add:** A no-change refresh is still valuable when it records that a high-consequence assumption was checked and remains applicable.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** It is confident that local policy and state must precede public guidance and that primary sources outrank generic examples; exact current public semantics remain unverified here.
- **supporting_reason:** The five local source files were read completely, while the three public pointers were deliberately preserved as unrefreshed under the no-browse constraint.
- **counterargument_or_limit:** Local source completeness does not establish current upstream Git or GitHub behavior, so affected claims must stay bounded until refreshed.
- **assumptions_and_boundaries:** Query strings are plans, not citations, and their inclusion does not raise evidence confidence.
- **revision_decision:** Mark every listed query as unexecuted and state which existing recommendation remains conservative pending refresh.
- **additional_insight_to_add:** Explicitly preserving uncertainty avoids the common failure in which a plausible search phrase is later mistaken for completed research.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** A refresh registry converts external research into dependency management: claims have authorities, versions, invalidation triggers, and downstream sections that must be reverified.
- **supporting_reason:** This model makes source drift observable and limits updates to guidance actually affected by a changed fact.
- **counterargument_or_limit:** Maintaining claim-level dependencies costs effort and may be excessive for low-consequence explanatory text.
- **assumptions_and_boundaries:** Apply the registry most rigorously to destructive operations, remote publication, protection, CI, recovery, and platform idempotency claims.
- **revision_decision:** End with event-driven refresh triggers such as local hash change, tool upgrade, policy change, contradictory incident, moved official page, or failed fixture.
- **additional_insight_to_add:** Event-driven refresh is more efficient than periodic broad search because it targets facts whose change can alter the next safe action.
## Section 026: Evidence Boundary Notes
### Question 01: What decision does this reference help make?
- **current_section_observation:** The evidence notes must decide what kind of support each consequential claim has and how that support limits the action or confidence a reader may derive from it.
- **supporting_reason:** User authorization, repository policy, observed Git state, local workflow sources, unrefreshed public pointers, synthesis, and normative safety defaults answer different questions and cannot be pooled as interchangeable proof.
- **counterargument_or_limit:** Labeling every sentence mechanically would make the reference unreadable without improving decisions, so boundaries should be explicit at claim clusters and conflicts.
- **assumptions_and_boundaries:** The taxonomy describes provenance and authority, not mathematical certainty, and current live state must still be reobserved for each real operation.
- **revision_decision:** Expand the seed's three labels into an evidence-and-authority matrix with permitted use, prohibited inference, confidence update, and refresh trigger.
- **additional_insight_to_add:** Evidence class should constrain verbs: a source can suggest, policy can require, live state can establish, and only explicit intent can authorize certain consequences.
### Question 02: What is the recommended default, and why?
- **current_section_observation:** The recommended default is claim-level separation of observed state, authorization, policy, sourced procedure, inference, and unresolved uncertainty, using the least authoritative class that fully describes support.
- **supporting_reason:** This prevents a conservative synthesis from masquerading as documented policy and prevents an example command from becoming user consent.
- **counterargument_or_limit:** A current repository runbook may combine procedure and policy legitimately, but its scope and authority must be explicit rather than inferred from location alone.
- **assumptions_and_boundaries:** Where multiple classes support one recommendation, retain each role and expose conflicts instead of collapsing them into a generic combined label.
- **revision_decision:** Use inline labels in evidence maps and concise boundary notes in operational prose, with a final audit for unsupported authority escalation.
- **additional_insight_to_add:** The strongest source does not necessarily decide the action; user intent and local policy can govern while upstream documentation only explains mechanics.
### Question 03: When does the default work well?
- **current_section_observation:** The taxonomy works well for direct-request routing, PR cleanup conflict reconciliation, repository-specific checks, remote selection, destructive confirmation, and public-documentation refresh decisions.
- **supporting_reason:** Each case combines mechanics, state, authority, and judgment whose distinct roles affect whether the workflow may proceed or must preserve and stop.
- **counterargument_or_limit:** Routine low-risk examples can use a short surrounding boundary statement rather than annotating every command and noun.
- **assumptions_and_boundaries:** Readers can trace local-source facts to the five fully read paths and can see that the four Claude aliases collapse into two byte-identical artifacts.
- **revision_decision:** Add worked evidence decompositions for pull-request cleanup and discard to demonstrate the taxonomy operationally.
- **additional_insight_to_add:** Conflict-aware provenance is stronger than majority counting because duplicated sources do not create independent confirmation.
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** Evidence labeling fails when labels are decorative, public pointers are called sourced facts without inspection, inferred defaults are presented as commands, or repository observations are treated as stable policy.
- **supporting_reason:** These errors inflate confidence and can authorize cleanup, force, destination choice, or readiness claims that the actual evidence never supports.
- **counterargument_or_limit:** Excessive uncertainty language can paralyze safe direct requests, so once intent, policy, state, and required checks align, the guide should act decisively.
- **assumptions_and_boundaries:** Unknown evidence blocks only claims and actions it can materially change; irrelevant gaps should be marked outside scope rather than loaded indefinitely.
- **revision_decision:** Add misuse tests and a stop-loading rule tied to decision sufficiency and consequence.
- **additional_insight_to_add:** Evidence discipline should reduce both overconfidence and endless research by stating what would be sufficient to decide.
### Question 05: Which alternatives and tradeoffs matter?
- **current_section_observation:** Alternatives include inline tags, source footnotes, claim tables, decision records, executable fixtures, and repository-policy references.
- **supporting_reason:** They trade reading flow against traceability, maintenance burden, machine validation, and the ability to expose conflicting authority.
- **counterargument_or_limit:** Footnotes and links can decay, while duplicated inline provenance can become stale when a source changes.
- **assumptions_and_boundaries:** This reference favors source maps plus boundary prose and operation records; repositories may add machine-readable claim registries for high-consequence workflows.
- **revision_decision:** Recommend the lightest representation that preserves claim, source role, applicability, conflict, and verification method.
- **additional_insight_to_add:** Executable fixtures complement but do not replace provenance because behavior tests cannot establish user intent or organizational policy.
### Question 06: Which gotchas and failure modes matter most?
- **current_section_observation:** Evidence gotchas include duplicate local aliases, stale hashes, examples mistaken for guarantees, future queries mistaken for completed research, and live command output mistaken for authorization.
- **supporting_reason:** The current corpus contains byte-identical source aliases and unrefreshed public URLs, making these confusions concrete rather than hypothetical.
- **counterargument_or_limit:** Duplicate aliases still improve discoverability and can show active versus archived location even though they add no independent corroboration.
- **assumptions_and_boundaries:** Hash equality establishes byte identity at capture time, not semantic authority, future immutability, or applicability to the current repository.
- **revision_decision:** Include explicit duplicate-counting, no-browse, version, and applicability caveats in the final notes.
- **additional_insight_to_add:** Provenance needs both identity and role: two different files can share one lineage, while one authoritative file can contain internal conflict.
### Question 07: What do good, bad, and borderline examples look like?
- **current_section_observation:** A good cleanup recommendation states the conflicting local-source guidance, observed worktree state, repository policy, explicit intent, conservative inference, and postcondition verification separately.
- **supporting_reason:** The reader can see why preservation is the default, what evidence could override it, and which facts must be refreshed for the actual operation.
- **counterargument_or_limit:** If current policy explicitly mandates cleanup and all safety preconditions pass, lengthy conflict discussion can be shortened while retaining provenance in the record.
- **assumptions_and_boundaries:** A bad claim says GitHub best practice requires deletion without reading a source; a borderline claim cites official Git mechanics as if mechanics authorize discard.
- **revision_decision:** Add good, bad, and borderline evidence decompositions tied to actual finish decisions.
- **additional_insight_to_add:** Borderline examples reveal category errors between "can," "should," "must," and "was authorized."
### Question 08: How can the important claims be verified?
- **current_section_observation:** Verify evidence boundaries by sampling consequential recommendations and tracing each to exact source path or observation, authority role, applicability, conflict, inference, and operational check.
- **supporting_reason:** This audit detects unsupported precision, duplicated corroboration, stale public claims, and normative guidance presented as external fact.
- **counterargument_or_limit:** Traceability does not prove the source itself is correct, so current behavior and repository policy still need direct verification where consequential.
- **assumptions_and_boundaries:** The audit includes source hashes and complete-read evidence already captured but does not browse or alter the source corpus.
- **revision_decision:** Add a claim-audit checklist and require every high-consequence recommendation to name a verification or stop condition.
- **additional_insight_to_add:** Automated path and hash checks can validate identity, while human review remains necessary for semantic conflict and authority interpretation.
### Question 09: What is known confidently, and what remains judgment or uncertainty?
- **current_section_observation:** It is confident which five local paths were read, which pairs are byte-identical, and that public pointers were not opened; current upstream behavior and repository-specific policy remain outside that evidence.
- **supporting_reason:** Local hashes and complete reads are direct workspace evidence, whereas no-browse constraints prevent converting URLs into externally sourced facts.
- **counterargument_or_limit:** Even complete local reading does not prove the source authors' empirical claims or universal applicability.
- **assumptions_and_boundaries:** Recommendations such as preserving PR worktrees by default are conservative synthesis from conflict and intent principles, not a quoted universal rule.
- **revision_decision:** State confidence and uncertainty explicitly and require live state plus current policy before real mutation.
- **additional_insight_to_add:** Honest bounded synthesis can still be actionable when it selects the least destructive reversible default and names what would change it.
### Question 10: What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?
- **current_section_observation:** The evidence taxonomy implies an authority lattice rather than a source hierarchy: mechanics, observed state, policy, and user intent constrain different dimensions of the decision.
- **supporting_reason:** No amount of upstream documentation can authorize deleting local work, and no user request can make a technically impossible or policy-prohibited transition valid without resolution.
- **counterargument_or_limit:** A rigid lattice can oversimplify emergencies or delegated authority, so repositories must state exceptions and escalation ownership explicitly.
- **assumptions_and_boundaries:** The model applies to ordinary branch-finishing operations and routes damaged repositories, security incidents, and production emergencies to specialist governance.
- **revision_decision:** End the file with a decision sufficiency rule: proceed when authority, state, mechanics, and evidence align; preserve and route when any consequential dimension remains unresolved.
- **additional_insight_to_add:** Keeping these dimensions separate makes future source refresh safer because a mechanics update cannot silently rewrite authorization or ownership policy.
