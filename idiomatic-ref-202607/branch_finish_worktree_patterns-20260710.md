# Branch Finish Worktree Patterns

Use this reference to decide how completed or deliberately checkpointed work should be preserved, published, integrated, kept, or discarded from the Git state that actually exists. The central inputs are the user's chosen outcome, current branch and worktree identity, dirty-state ownership, relevant verification, base and upstream relationships, and the reversibility of the proposed action. This is an operating guide for a state transition, not a generic list of Git commands.

Follow an intent-first sequence. Inspect before mutating: identify the repository root, current branch or detached state, linked worktree, status, scoped diff, upstream, likely base, and relevant project instructions. Separate changes produced for the current task from pre-existing or concurrent user work. Run the checks that support the claimed completion state. If the user already requested commit, push, draft pull request, preservation, cleanup, or discard, follow that path directly after its safety gates. Otherwise present the four source-backed choices: merge locally, push and create a pull request, keep the branch as-is, or discard after explicit confirmation.

Direct intent removes the need for an option menu; it does not remove verification, ownership, or destructive-action controls. A save-only checkpoint may be valid when full checks cannot pass and the user knowingly requests preservation, but report it as a checkpoint rather than finished or release-ready work. Stop before mutation when branch identity, ownership, base, remote, or test scope is consequentially ambiguous.

Treat publication and cleanup as separate decisions. The older branch source contains conflicting pull-request guidance: one step sends the PR path through worktree cleanup, while its quick reference and mistake guidance preserve that worktree. The later Codex source emphasizes explicit user intent and intentional handoff. This reference therefore defaults to preserving the branch and worktree after a pull request unless the user or repository policy explicitly requests cleanup and the state is safe to remove. Never infer discard or destructive cleanup from silence.

This workflow fits a finishable feature branch, an isolated worktree whose task is complete, a requested checkpoint, or a branch that needs a clear review handoff. Route elsewhere for unfinished implementation, unresolved merge or rebase conflicts, repository corruption, release orchestration, protected-branch administration, or production deployment. An initial state audit can identify those routes without attempting to finish them.

Verify three layers. Preconditions establish identity, ownership, scope, and quality evidence. Action evidence records the exact commit, branch, remote, pull request, merge, keep, or confirmed discard choice. Postconditions establish where the work now lives, whether expected changes remain, whether merged checks pass where applicable, and what the next owner must do. A successful Git command is not enough if it acted on the wrong branch or left the intended commit unpublished.

A good finish report names what was saved, where it was saved, what checks ran, what state remains, and the next action. A bad finish force-deletes a dirty branch because implementation seemed complete. A borderline finish pushes correctly but assumes `origin`, removes a useful worktree, or omits unverified gates. Preserve optionality when evidence is incomplete: refusing an ambiguous finish is safer than converting uncertainty into irreversible repository state.

## Source Evidence Mapping Table

This map routes claims; it is not a source-count vote. User intent and current repository policy authorize the outcome. Live Git state establishes what exists. Skills provide workflow defaults. Public links may refresh platform-specific facts when inspected. Four Claude paths below collapse into two byte-identical artifacts, so their aliases improve retrieval but do not provide independent corroboration.

| source_location_path_key | source_category_artifact_type | evidence_status | source_usage_synthesis_role | important_boundary_or_conflict |
| --- | --- | --- | --- | --- |
| `agents-used-monthly-archive/claude-skills-202603/superpowers/finishing-a-development-branch/SKILL.md` | local_corpus_source_material | local_corpus_sourced_fact | Historical lineage for test-first completion, base discovery, four options, destructive confirmation, and cleanup. | Byte-identical to the current Claude finish path; its PR flow conflicts internally about worktree cleanup. |
| `agents-used-monthly-archive/claude-skills-202603/superpowers/using-git-worktrees/SKILL.md` | local_corpus_source_material | local_corpus_sourced_fact | Historical lineage for worktree directory selection, ignore verification, setup, baseline tests, and location reporting. | Byte-identical to the current Claude worktree path; setup commands are examples and must follow project policy. |
| `agents-used-monthly-archive/codex-skills-202604/finishing-a-development-branch/SKILL.md` | local_corpus_source_material | local_corpus_sourced_fact | Later Codex variant for direct-request behavior, intentional saving, remote selection, and concise next-step handoff. | Does not fully specify worktree removal mechanics; pair it with state inspection and conservative cleanup. |
| `claude-skills/superpowers/finishing-a-development-branch/SKILL.md` | current_local_alias | local_corpus_sourced_fact | Active retrieval alias for the Claude finish procedure. | Same SHA-256 and bytes as the archived Claude finish source, so it is one evidence lineage. |
| `claude-skills/superpowers/using-git-worktrees/SKILL.md` | current_local_alias | local_corpus_sourced_fact | Active retrieval alias for the Claude worktree setup and baseline procedure. | Same SHA-256 and bytes as the archived Claude worktree source, so it is not a second independent policy. |
| `https://docs.github.com/actions` | external_research_source_material | unrefreshed_external_pointer | Future source for current automation and CI workflow facts when those facts affect finish readiness. | Not browsed in this evolution; CI documentation cannot establish local branch ownership or user intent. |
| `https://docs.github.com/en/actions/concepts/workflows-and-actions/reusing-workflow-configurations` | external_research_source_material | unrefreshed_external_pointer | Future source for current reusable-workflow composition when repository verification depends on it. | Not browsed here; reusable workflow semantics do not define Git cleanup policy. |
| `https://github.com/openai/codex/blob/-/AGENTS.md` | external_repository_pointer | unrefreshed_external_pointer | Future example of repository instructions and testing guidance after path and revision validation. | The seed URL was preserved but not opened; do not infer its contents, revision, or authority from the path. |

Use this retrieval order for a real operation:

1. Read the user's explicit request. Commit, push, draft pull request, keep, and discard are different authorizations; only explicit confirmation authorizes irreversible loss.
2. Read current repository instructions and ownership constraints. They can name protected branches, required checks, remotes, worktree policy, or prohibited operations.
3. Inspect live state with nonmutating Git commands: repository root, branch or detached state, status, diff scope, upstream, remotes, worktree list, and likely base. Commands provide state evidence, not policy.
4. Use the later Codex source for direct intent and save reporting, and the Claude sources for the four-option decision and worktree lifecycle. Reconcile conflicts conservatively.
5. Refresh public documentation only for a named platform question that remains unresolved and when browsing is permitted. Record the version, relevant passage, applicability, and access date.
6. Stop loading evidence when the requested outcome, ownership, state, applicable checks, destructive boundary, and postcondition are determined.

The local sources cover ordinary feature-branch completion well: quality checks, base discovery, local merge, push and pull request, keep, confirmed discard, project-local worktree safety, setup, baseline tests, and handoff. They do not independently govern protected-branch administration, release trains, force-push policy, submodules, multi-repository publication, deployment, or hosting permissions. Route those decisions to current repository and platform authorities.

Resolve the pull-request cleanup contradiction explicitly. The older finish procedure sends Option 2 through its cleanup step, but its quick-reference and common-mistake guidance say a PR keeps the branch and worktree. The identical current copy repeats that contradiction. This reference does not count the duplicate as another vote. Preserve the PR branch and worktree by default, then clean them only after explicit intent, a clean and recoverable state, and any repository-specific policy check.

Deterministic evidence from this source read includes SHA-256 `dd2f82c6dc8582b621f9eb57fcb65f557f88eadf872727ac81d0840ae12c504e` for both Claude finish paths, `de9dcde34840eee074047ec327d4ea6ca4954c5a73a6d874dc48f25fe46c9e7c` for both Claude worktree paths, and `9a0738cce13077cdc5c3299b4315fbdf3d8b1a597814a4a14e8f65ef5564126a` for the Codex variant. Hashes establish identity, not normative precedence.

For each consequential recommendation, retain the source or observed state, what it establishes, the user authorization it requires, the command or review gate that verifies it, and the recovery path. Reverse-trace destructive actions to explicit confirmation. If a source changes, reopen only dependent rules and fixtures first, then reread the complete reference for coherence.

## Pattern Scoreboard Ranking Table

The scores are inherited corpus-priority metadata. They are not success rates, confidence percentages, Git safety measurements, or permission to follow a higher-scored convenience over user intent, repository policy, ownership, or preservation of work. Consequence can override numeric order.

| pattern_identifier_stable_key | pattern_score_numeric_value | pattern_tier_adoption_level | pattern_failure_prevention_target |
| --- | ---: | --- | --- |
| `branch_finish_worktree_patterns` | 95 | default_adoption_pattern_tier | Source Map First: Load local branch finish material before synthesizing worktree patterns recommendations. |
| `branch_finish_worktree_patterns` | 91 | default_adoption_pattern_tier | Evidence Boundary Split: Separate local facts, external facts, and inference before giving agent instructions. |
| `branch_finish_worktree_patterns` | 88 | default_adoption_pattern_tier | Verification Gate Coupling: Attach each recommendation to at least one command, checklist, or review gate. |

Apply the rows through a branch-specific loop:

1. **Source Map First:** identify explicit user intent, current repository instructions, live state, relevant local workflow source, and only the platform evidence needed for an unresolved question. The output is an authority and state map, not a link inventory.
2. **Evidence Boundary Split:** distinguish user authorization, repository policy, observed Git state, local source guidance, unrefreshed public pointers, and conservative synthesis. A command result says what exists; it does not say what the user wants.
3. **Verification Gate Coupling:** attach each mutation to a precondition, expected state change, postcondition, and recovery path. Tests support quality but do not establish branch identity, commit scope, remote destination, or cleanup intent.
4. **Repair the failed dependency:** failing checks return to implementation or a checkpoint choice; mixed ownership returns to scoping; ambiguous base or remote returns to clarification; source conflict returns to conservative preservation; an unexpected postcondition stops further cleanup.

Use three evidence depths. A local save on a clean isolated branch can use compact status, diff, and requested commit evidence. A push, pull request, or merge adds upstream, remote, base, and shared verification. Discard, force deletion, or worktree removal adds exact confirmation, an inventory of what will disappear, and recovery analysis. Direct requests shorten choice discovery, not these safety layers.

The three generic controls need complementary branch-operation rules:

- **Intent First:** follow an already selected path instead of forcing a menu, while confirming destructive details.
- **State Before Mutation:** inspect branch, status, diff, worktree, upstream, remotes, and relevant instructions before changing them.
- **Least Destructive Default:** preserve commits, branches, worktrees, and user changes when cleanup intent is absent or source guidance conflicts.
- **Scoped Mutation:** use exact branches and pathspecs; never sweep unrelated dirty changes into a save merely to obtain a clean status.
- **Postcondition Proof:** verify where the work lives and what remains after every state-changing action.

Each pattern leaves inspectable evidence. Source Map First leaves selected sources, aliases, conflicts, and skipped-source reasons. Evidence Boundary Split leaves claim and authorization labels. Verification Gate Coupling leaves commands or review questions with current results. Intent First leaves the requested outcome. State Before Mutation leaves a snapshot. Least Destructive Default leaves preserved recovery options. Postcondition Proof leaves the resulting branch, commit, remote, pull request, worktree, and open work.

Good application takes a direct draft-PR request, inspects the scoped dirty state, runs relevant checks, creates the intended commit, verifies the pushed branch, reports the PR, and preserves the worktree because cleanup was not requested. Bad application cites all five local files and force-deletes a branch after tests pass. Borderline application runs the full test suite but never distinguishes pre-existing user edits from task changes; quality evidence is green while ownership evidence is missing.

Verify the controls with discriminating fixtures. Change the current branch while keeping test output constant; add an unrelated dirty file; remove upstream configuration; provide two remotes; request a checkpoint with failing tests; or omit cleanup consent after PR creation. The selected action and report should change. A review that produces the same finish command for every fixture is matching keywords rather than reasoning from state.

Change scores only with recorded criteria or observed failure-prevention evidence. More importantly, maintain the path `intent -> observed state -> authority -> chosen transition -> precondition -> mutation -> postcondition -> owner`. That contract supports targeted refresh and makes unsafe confidence upgrades visible.

## Idiomatic Thesis Synthesis Statement

`local_corpus_sourced_fact`: The five mapped local paths represent three distinct artifacts because each current Claude path is byte-identical to its archived counterpart. The source family agrees that relevant checks precede completion claims, unclear outcomes receive a four-option menu, discard requires explicit confirmation, and the final report names where work remains. The later Codex variant adds direct-request behavior and intentional save reporting. The Claude finish artifact contradicts itself about whether pull-request creation should remove or preserve the worktree.

`external_research_sourced_fact`: No public source was inspected during this no-browse evolution. The three external rows are unrefreshed pointers for future automation, reusable workflow, and repository-instruction questions. They provide no current evidence for branch cleanup, Git semantics, or this repository's policy.

`combined_evidence_inference_note`: Reliable branch finishing follows `intent -> observed state -> applicable authority -> readiness evidence -> chosen transition -> postcondition -> recovery or next owner`. Honor an already selected commit, push, pull-request, keep, or discard path after its safety gates. If the user has not selected a path, present the four source-backed outcomes. Preserve work when cleanup intent or source guidance is ambiguous, and require exact confirmation before irreversible loss.

Keep readiness and persistence claims separate. Relevant tests and checks support a completion or merge-readiness claim. A checkpoint commit can preserve incomplete or failing work when the user explicitly requests that tradeoff, but it must not be described as verified completion. A draft pull request can provide remote durability and review while required CI or merge policy remains pending.

The workflow is transaction-like without requiring ceremony. Preconditions establish repository, branch or detached state, worktree, scope, ownership, base, upstream, remote, and applicable checks. The action performs only the authorized state change. Postconditions prove the resulting commit, branch, remote, pull request, merge, retained worktree, or confirmed deletion. Recovery evidence identifies what can be restored and who owns the next move.

Use the synthesis for ordinary feature branches, isolated worktrees, explicit checkpoints, and review publication. Stop or route when implementation remains unfinished, conflicts are unresolved, the base or remote is consequentially uncertain, dirty changes have mixed ownership, repository state is damaged, or production release authority is required. A reversible checkpoint may preserve progress while those blockers remain, but it does not resolve them.

Adopt repository workflow verbatim when it is current, applicable, and consistent with user intent. Adapt generic source instructions to installed Git behavior, remotes, protected branches, and project checks. Avoid commands whose preconditions are unknown. Escalate source contradictions or shared ownership rather than selecting the most convenient line. The later Codex direct-request behavior and the older four-option model are complementary: one handles known intent, the other handles missing intent.

Good synthesis responds to a direct draft-PR request by scoping task changes, running relevant checks, committing intentionally, pushing the named or verified branch, creating the draft, preserving the worktree unless cleanup was requested, and reporting pending CI. Bad synthesis obtains a clean status by sweeping user changes into a commit or force-removing a branch. Borderline synthesis publishes correctly but calls the work merge-ready before asynchronous checks complete.

Verify the complete chain. A request must map to the action. Repository policy must apply to the observed state. The diff must match owned scope. Quality evidence must support the stated readiness. The command result must match its target. The postcondition must show where work lives, and pending external gates need an owner and follow-up trigger. A green test suite cannot authorize a push, and a configured remote cannot prove quality.

For shared outcomes, retain stable identifiers: branch, commit, remote, pull request or merge, worktree path, verification result, unresolved risk, and next owner. Cleanup belongs later when the recovery value of that state has expired or explicit policy requires removal. Successful publication alone is not sufficient evidence that a branch or worktree should disappear.

## Local Corpus Source Map

The local corpus contains three distinct artifacts exposed through five paths. Select by unresolved decision, not by row order. Current project instructions and observed Git state still outrank generic mechanics when they apply.

| local_source_filepath_value | local_source_title_text | local_source_heading_signals | local_source_usage_role | exclusion_or_conflict |
| --- | --- | --- | --- | --- |
| `agents-used-monthly-archive/claude-skills-202603/superpowers/finishing-a-development-branch/SKILL.md` | finishing-a-development-branch | `Finishing a Development Branch`; `Overview`; `The Process`; `Step 1: Verify Tests`; `Step 2: Determine Base Branch`; option and cleanup material. | Read for test-first completion, candidate base discovery, the four default outcomes, discard confirmation, and detailed branch/worktree finish mechanics. | Its PR path conflicts internally on worktree cleanup; do not follow cleanup without resolving intent and state. |
| `agents-used-monthly-archive/claude-skills-202603/superpowers/using-git-worktrees/SKILL.md` | using-git-worktrees | `Using Git Worktrees`; `Overview`; `Directory Selection Process`; existing directories; project instructions; ignore safety; setup; baseline tests. | Read when finish safety depends on where the worktree lives, whether project-local content is ignored, how the baseline was established, or whether the worktree should remain. | Setup commands are ecosystem examples, not permission to install or change dependencies against project policy. |
| `agents-used-monthly-archive/codex-skills-202604/finishing-a-development-branch/SKILL.md` | finishing-a-development-branch | `Finishing a Development Branch`; `Overview`; `Workflow`; `Direct-Request Behavior`; `Option Menu`; `Guardrails`. | Read first for a direct commit, push, pull-request, keep, checkpoint, or discard request and for intentional save and handoff reporting. | It leaves worktree removal details to companion evidence and does not supersede repository-specific verification. |
| `claude-skills/superpowers/finishing-a-development-branch/SKILL.md` | finishing-a-development-branch | Same headings and complete bytes as the archived Claude finish source. | Use as the active retrieval alias when an invoking workflow points here. | It is not independent evidence and repeats the same cleanup contradiction. |
| `claude-skills/superpowers/using-git-worktrees/SKILL.md` | using-git-worktrees | Same headings and complete bytes as the archived Claude worktree source. | Use as the active retrieval alias for current superpowers workflows. | It is not a separate corroborating worktree policy. |

Use task-triggered retrieval:

- For an explicit save or publication request, start with the Codex variant, then inspect repository instructions and live state.
- When the desired outcome is unknown, use the Claude finish artifact's four concise options after relevant checks pass or the status is explicitly labeled as a checkpoint.
- When the branch lives in a linked worktree or cleanup is proposed, read the worktree artifact as well as the finish artifact.
- When discard is requested, inspect the exact branch, commits, dirty files, worktree, and recoverability before requesting exact confirmation.
- When base, remote, tests, or hosting policy are repository-specific, stop generic retrieval and use the current local authority.

The worktree source contributes creation invariants that remain relevant at finish time. Project-local worktree directories should have been checked for ignore safety. Baseline test results distinguish pre-existing failures from task regressions. The worktree location and branch association determine whether removal targets the intended checkout. A final branch name alone cannot reconstruct those facts.

The corpus works best for ordinary isolated feature work using common branch and remote patterns. Literal commands need adaptation for bare repositories, submodules, sparse checkout, custom hosting, multiple remotes, protected branches, unusual base strategy, or project-specific dependency management. Preserve sequence and safety reasoning while verifying mechanics in the current environment.

Do not infer canonicality solely from archive age or current path. The seed calls the archived Claude finish source canonical, labels some variants legacy, and treats current copies as supporting. Operational precedence is narrower: the explicit user request governs the outcome, repository policy governs local constraints, live commands establish state, and a skill supplies defaults for gaps. A later source can refine interaction without replacing an older source's detailed worktree mechanics.

Good retrieval for a requested draft pull request uses the Codex direct-request rule, the Claude test and option safeguards, and the worktree preservation evidence. Bad retrieval opens only the force-delete example after seeing the word discard. Borderline retrieval accepts `main` from a common-base heuristic without checking a repository whose integration branch is different; report it as a candidate until confirmed.

Verify local use through path existence, content identity, complete applicable-section reads, conflict recording, and claim-to-action mapping. Cache duplicate hashes for efficiency, but confirm the alias still resolves to those bytes. When a source changes, reopen dependent lifecycle rules: directory and baseline changes affect setup and cleanup; option changes affect intent routing; save and handoff changes affect publication reports.

## External Research Source Map

These links are future retrieval entrypoints. No browsing occurred during this evolution, so current content, redirects, revisions, and supporting passages remain unverified. They do not presently authorize a push, merge, discard, branch deletion, or worktree removal.

| external_source_url_value | external_source_name_text | external_source_usage_role | evidence_boundary_label_value |
| --- | --- | --- | --- |
| `https://docs.github.com/actions` | GitHub Actions documentation | Future official source for current automation, check, and workflow semantics after the target repository's configuration is inspected. | unrefreshed_external_pointer |
| `https://docs.github.com/en/actions/concepts/workflows-and-actions/reusing-workflow-configurations` | Reusable workflow docs | Future official source for composed workflow behavior when a required local check delegates to another workflow. | unrefreshed_external_pointer |
| `https://github.com/openai/codex/blob/-/AGENTS.md` | OpenAI Codex repository AGENTS | Preserved repository-instruction example whose exact revision, content, and applicability require validation before use. | unrefreshed_external_pointer |

| external_source | appropriate_finish_use_after_refresh | invalid_extrapolation |
| --- | --- | --- |
| GitHub Actions documentation | Explain a named check's platform semantics, trigger, status, or asynchronous completion after the local workflow is identified. | Claiming that generic CI documentation proves this branch passed required checks, owns local test scope, or is safe to delete. |
| Reusable workflow documentation | Trace why a repository check calls another workflow and what evidence may still be pending. | Assuming every workflow composition is required, secure, or equivalent to local branch policy. |
| OpenAI Codex repository AGENTS pointer | Illustrate how a real repository may publish agent-specific test and workflow instructions after inspecting a pinned revision. | Copying another repository's instructions into this one or inferring current content from an unpinned seed URL. |

Use external evidence only after local state identifies a question it can answer. Inspect repository workflow files and observed check names first. Then consult current official documentation for the exact platform and feature. Pair capability evidence with repository configuration: documentation may show what Actions supports, while the checked-in workflow and branch policy show what this repository actually uses.

For Git mechanics, prefer current repository instructions, installed `git help`, and nonmutating state inspection. For hosting actions, inspect remote and hosting CLI state plus current authoritative platform documentation. For policy, use branch-protection settings, repository governance, and explicit user authorization. If a required authority is inaccessible, report it as pending rather than filling the gap with a generic web example.

Good external use says, for example, "The local pull request references check `verify`; the inspected workflow delegates through a reusable workflow; current official documentation explains the call behavior; the observed remote check is still pending." Bad use says "GitHub Actions proves the branch is safe to remove." Borderline use copies an AGENTS file from another repository because both projects use Codex, without evidence that the target adopted its rules.

When refreshed, record URL, access date, pinned revision or product version, relevant passage, local workflow or setting, observed state, applicable claim, and the exact finish decision it changes. A URL alone is not evidence. Product documentation cannot establish dirty-file ownership, and repository precedent cannot replace explicit discard confirmation.

Stop external research when additional material cannot change the selected action, readiness boundary, postcondition, or recovery plan. Keep platform-specific examples modular because they decay faster than the core principles of explicit intent, state-before-mutation, least-destructive handling, and postcondition verification.

## Anti Pattern Registry Table

Use this registry before any state-changing finish command. A blocker changes content, destination, ownership, readiness, authorization, or recoverability. A lower-impact wording defect may be repaired without stopping an otherwise safe preservation action, but it cannot justify an unsupported readiness claim.

| anti_pattern_failure_name | failure_cause_risk_reason | safer_default_replacement_pattern | detection_signal_review_method |
| --- | --- | --- | --- |
| `context_free_summary_output` | The agent skips local sources and repository state, then gives plausible generic Git advice. | `source_and_state_first_synthesis` | Require selected local source roles plus current branch, worktree, status, and policy evidence relevant to the requested action. |
| `unsourced_recommendation_claims` | Guidance appears authoritative without separating user authorization, repository policy, observed state, public evidence, and synthesis. | `evidence_and_authority_boundary_split` | Sample every consequential recommendation and identify who or what authorizes it. |
| `unverified_agent_instruction` | A mutation has no precondition, postcondition, or recovery check. | `verification_gate_coupling` | Predict the intended state change, run the scoped action, and compare actual branch, commit, remote, and worktree state. |
| `mutation_before_status_inspection` | Commit, merge, push, branch deletion, or worktree removal begins before repository identity and dirty state are known. | `state_before_mutation` | Capture nonmutating root, branch, worktree, status, diff, upstream, and remote evidence first. |
| `mixed_change_commit_scope` | Task edits are staged with unrelated user or concurrent changes to obtain a clean tree. | `owned_pathspec_or_patch_staging` | Compare staged and unstaged diffs with the task's owned paths; review every staged file before commit. |
| `wrong_branch_or_remote_target` | A valid command acts on an assumed current branch, upstream, base, or `origin`. | `explicit_verified_target` | Resolve branch, candidate base, remotes, tracking configuration, and requested destination; report assumptions that remain. |
| `tests_only_readiness_claim` | Green tests are treated as proof of correct scope, ownership, publication, or merge policy. | `multidimensional_finish_evidence` | Check quality gates separately from diff scope, branch identity, remote state, review status, and required asynchronous checks. |
| `forced_option_menu_after_direct_request` | The agent asks the user to choose again after an explicit commit, push, draft-PR, keep, or discard instruction. | `direct_request_after_safety_gates` | Map the request to one path and ask only for missing consequential details or confirmation. |
| `automatic_pr_worktree_cleanup` | Pull-request creation is interpreted as permission to remove the worktree despite conflicting source guidance. | `publication_cleanup_decoupling` | Preserve by default; require explicit cleanup intent, clean state, remote durability, and exact worktree target. |
| `discard_without_exact_confirmation` | Branch, commits, dirty files, or worktree are deleted from inferred intent. | `inventory_then_explicit_discard_confirmation` | Show what will disappear and wait for the required exact confirmation before destructive mutation. |
| `force_operation_as_first_recovery` | Force-delete or force-push is used to bypass an unexpected state rather than diagnose it. | `classify_preserve_escalate` | Stop, retain evidence, identify the failed precondition, and use force only under explicit policy and authorization. |
| `unauthorized_ignore_fix_commit` | Generic worktree setup automatically changes and commits `.gitignore` without current user or repository authorization. | `report_or_request_ignore_repair` | Confirm project-local directory risk, inspect policy, and obtain the requested save boundary before editing or committing. |
| `worktree_path_by_text_match` | A branch or path is selected through fragile substring matching and the wrong worktree is removed. | `porcelain_or_exact_worktree_identity` | Use structured or exact `git worktree list` evidence and compare the full target path and branch association. |
| `branch_deleted_before_postcondition` | Local branch cleanup occurs before merged or remote state and recovery references are verified. | `postcondition_before_cleanup` | Confirm the intended commit is integrated or remotely durable and record the remaining owner before deleting references. |
| `clean_tree_equals_finished` | A clean status is treated as completion even though commits may be unpushed, checks pending, or the wrong branch active. | `outcome_specific_completion_contract` | Verify the chosen outcome explicitly: local save, remote publication, merge, keep, or confirmed discard. |

Review in this order: intent, repository identity, ownership, diff scope, applicable quality gates, destination, reversibility, exact action, and postcondition. Skip a dimension only when it cannot affect the requested outcome. For example, a local checkpoint may not need base discovery, while a local merge does. The omission should remain explainable.

Do not ban commands by spelling alone. `git add -A` can be correct when every visible change is intentionally owned and reviewed; it is unsafe in a mixed shared tree. `git branch -D` can implement confirmed discard; it is unacceptable as an automatic response to an unexpected merge state. Command safety depends on scope, authority, and recoverability.

Use the smallest remediation that preserves intent. Pathspec or patch staging isolates task changes. A named checkpoint preserves progress without claiming readiness. A draft pull request supplies remote durability and review while checks remain pending. A retained worktree preserves local recovery. A temporary branch copy may protect uncertain state, but name its owner and retirement trigger so it does not become ambiguous debris.

Good remediation stages only task paths, records unrelated changes, follows a direct draft-PR request, and preserves the worktree. Bad behavior runs broad staging in a mixed tree and force-deletes after publication. Borderline behavior changes `.gitignore` because the generic worktree skill calls that directory unsafe, then commits the change without user approval. The safety diagnosis may be correct while the mutation authority is missing.

Verify blocker detection with contrasting fixtures: same tests on a different branch; one unrelated dirty file; two remotes; no upstream; a candidate base that differs from project policy; a PR request with no cleanup instruction; a confirmed discard with an untracked file; and a worktree path sharing a branch-name substring. Pair command evidence with explicit human authorization because ownership and intent cannot be inferred from Git alone.

If an anti-pattern appears in a script, hook, skill, or shared convention, contain its propagation and preserve a failing fixture before repair. Durable automation needs an owner, exact scope, recovery path, and regression test. Retire low-signal warnings so high-consequence blockers remain visible.

## Verification Gate Command Set

`verification_gate_command_set`: Verification has two independent targets: this reference artifact and the repository operation that uses it. A green documentation command does not make a branch ready, and green project tests do not prove the reference satisfies its 26-section contract.

For this evolved file, run the focused verifier from the repository root:

```bash
python3 tests/verify_idiomatic_reference_file.py \
  --path idiomatic-ref-202607/branch_finish_worktree_patterns-20260710.md
```

The intended final evidence is 26 reference sections in seed order, 26 packet sections, 260 exact questions, 1,560 populated mandatory fields, `uniqueFieldCount=1560`, `normalizedUniqueFieldCount=1560`, every section longer than its seed, and clean marker, ASCII, table, fence, and whitespace checks.

The archive seed also records this corpus-wide command:

```bash
python3 agents-used-monthly-archive/idiomatic-references-202606/tools/verify_reference_generation.py --stage final
```

It is broader than one owned assignment. Localize any failure to its path and do not modify another lane merely to make global output green.

For a real branch or worktree, use the following ladder. Run inspect commands before mutation and from the exact worktree under review.

| gate | example evidence | what it establishes | what it does not establish |
| --- | --- | --- | --- |
| Repository identity | `git rev-parse --show-toplevel` and current working directory. | The repository and worktree context receiving later commands. | User intent, branch ownership, or readiness. |
| Branch and detached state | `git branch --show-current`; if empty, record `git rev-parse --short HEAD`. | Named branch or detached commit. | Correct integration target or permission to create a branch. |
| Worktree identity | `git worktree list --porcelain`. | Exact linked paths, branches, detached states, and worktree metadata in a parseable form. | Whether a path is safe to remove or still needed. |
| Dirty-state inventory | `git status --porcelain=v1 --branch` plus a concise human-readable status if useful. | Staged, unstaged, untracked, and branch tracking indicators. | Which person or task owns each change. |
| Scope review | `git diff --name-status`, `git diff --cached --name-status`, and content review for the intended paths. | Changed-file and staged-file scope before saving. | Semantic correctness without reviewer and test evidence. |
| Whitespace sanity | `git diff --check` with an explicit pathspec when scope is narrow. | Conflict markers and whitespace errors encoded by Git's check. | Project formatting, compilation, tests, or policy. |
| Upstream and remotes | `git rev-parse --abbrev-ref --symbolic-full-name '@{upstream}'` when configured, plus `git remote -v` with credentials redacted. | Current tracking target and configured remote endpoints. | Which remote the user authorizes or whether pushing is permitted. |
| Candidate base | Repository policy first; `git merge-base HEAD main` or another named branch can test a candidate relationship. | Common ancestry with the candidate branch. | That the candidate is the repository's intended integration base. |
| Project quality | Repository-defined test, build, lint, type, format, or security commands. | Current results for the tested tree and environment. | Future CI results, correct commit scope, or remote acceptance. |
| Authorization | The explicit user request, repository instructions, and exact destructive confirmation where applicable. | Which state transition may be attempted. | That technical preconditions are satisfied. |
| Postcondition | Outcome-specific status, log, upstream, hosting, merge, and worktree checks. | Where the intended commit and working state now live. | Unobserved asynchronous checks or future deployment success. |

Classify evidence as inspect, project check, authorized mutation, or postcondition. Supposed verification should not silently change the baseline. A push, merge, branch delete, or worktree removal is an action, even when used to discover whether permissions or policy allow it. Attempt it only after relevant preconditions and authorization, then record its result without escalating to force.

Choose postconditions by outcome:

- **Commit or checkpoint:** verify the new commit identity, staged state cleared as expected, and unrelated dirty changes preserved.
- **Push or pull request:** verify the intended branch and remote contain the commit, capture the pull request identity and draft status, and report required checks as observed, pending, or inaccessible.
- **Local merge:** verify the merge occurred on the intended base, rerun required checks on the merged tree, and only then consider branch or worktree cleanup.
- **Keep:** verify no unintended mutation occurred and report exact branch and worktree path.
- **Discard:** after exact confirmation, verify the intended references and worktree were removed while unrelated work remains untouched; report any recovery reference intentionally retained.

Guard against false green evidence. Check staged and unstaged changes, include untracked files through status, capture exit codes, and rerun affected checks if the tree changes. Redact credential-bearing remote URLs. Report commands, target, current result, and coverage meaning rather than dumping sensitive or noisy transcripts.

A good verification record says: "In worktree `/repo/.worktrees/auth` on `feature/auth`, only three task files were staged; repository tests passed at commit `abc1234`; the user requested a draft PR to the verified remote; the pushed branch contains that commit; remote checks are pending; the worktree was preserved." A bad record says "Git clean." A borderline record reports a status snapshot taken before generated files changed; it is historical evidence, not current readiness.

Improve the ladder when a consequential defect escapes. Add a fixture or check that targets the failure mechanism, then confirm it distinguishes a safe and unsafe case. Retire redundant checks that never change action. The goal is a small maintained set that independently covers identity, ownership, quality, authorization, transition, and recoverability.

## Agent Usage Decision Guide

`agent_usage_decision_guide`: Use this reference when the user wants completed or checkpointed work saved, published, integrated, kept, cleaned, or discarded, or when a linked worktree needs a verified finish decision. A theme or source-path mention triggers state inspection, not automatic mutation.

Follow this operating sequence:

1. Name the requested outcome. If the user explicitly requested commit, push, draft pull request, merge, keep, cleanup, or discard, retain that path. Ask only about missing details that can change scope, destination, destruction, or readiness.
2. Read current repository instructions and the relevant local source. Use the Codex source for direct-request behavior, the Claude finish source when choice is unknown, and the worktree source when isolation or cleanup matters.
3. Inspect repository root, branch or detached state, worktree identity, dirty-state inventory, scoped diff, upstream, remotes, and candidate base as applicable.
4. Separate task-owned changes from pre-existing or concurrent work. Do not obtain a clean tree by absorbing unrelated edits.
5. Run relevant project checks and state their coverage. A checkpoint request may preserve failing work but must remain labeled non-ready.
6. If intent is still unknown, present the four concise options. If intent is known, proceed without forcing the menu.
7. Execute the smallest authorized transition. Publication and cleanup remain separate; discard and force operations need explicit confirmation and policy.
8. Verify the outcome and report what was saved, where it lives, what remains pending, and who owns the next action.

| task_signal | recommended_use_or_route | authority_boundary |
| --- | --- | --- |
| "Commit and push these task changes." | Follow the direct path after reviewing staged scope, relevant checks, branch, and verified remote. | The request authorizes save and publication, not unrelated changes, force push, or cleanup. |
| "Open a draft pull request." | Publish the intended branch, create a draft, report pending checks, and preserve the worktree by default. | Draft publication does not assert merge readiness or authorize branch deletion. |
| "Implementation is done; what next?" | Verify relevant checks and state, then present the four source-backed outcomes. | Do not preselect integration or discard for the user. |
| "Save this progress even though one test fails." | Use an explicitly labeled checkpoint path if scope and ownership are safe. | Persistence is not completion; report the failing check and recovery step. |
| "Discard this branch." | Inventory commits, dirty files, worktree, and recoverability; request exact destructive confirmation. | Do not infer confirmation from the initial phrase if the required inventory was not yet visible. |
| Merge or rebase conflict is active. | Route to conflict diagnosis and resolution, optionally preserving a checkpoint first. | Ordinary branch finish resumes only after conflict state and intended base are resolved. |
| The user wants deployment or release promotion. | Route to the current release or deployment authority after producing a branch handoff. | This reference does not govern production rollout, credentials, or service objectives. |
| Repository ownership or dirty-file scope is unclear. | Stop mutation, preserve evidence, and clarify or route to the owner. | A general Git skill cannot authorize another person's edits. |

This guide works for ordinary feature branches, isolated worktrees, local preservation, hosted review, and explicit cleanup. It is not the primary workflow for unfinished coding, merge-conflict repair, repository corruption, protected-branch administration, release orchestration, or production deployment. A bounded checkpoint and finishability report can bridge to those workflows without claiming they are complete.

Use defaults as hypotheses. `main`, `master`, `origin`, a configured upstream, and a clean status can all be valid while still being wrong for the requested outcome. Confirm any assumption that changes consequences. Be predictable about safeguards and adaptable about the actual path.

Good agent usage receives a direct commit-and-push request, reviews task scope, runs required checks, confirms the configured destination, executes, verifies the remote commit, and reports remaining CI. Bad usage ignores the direct request and asks the user to select from four options again. Borderline usage publishes successfully but includes an unrelated dirty file; the remote operation worked while the ownership contract failed.

Audit usage against the user's desired final state. Record the trigger, requested outcome, observed preconditions, selected authority, rejected alternative when consequential, exact mutation scope, postcondition, pending gate, and next owner. Success is not the number of Git commands run; it is a correct and recoverable transition to the requested state.

Repeated local choices can improve repository instructions. If a team consistently uses a named remote, draft-first review, specific check suite, or worktree retention policy, propose an explicit maintained convention. Do not promote one temporary request into policy without approval and ownership.

## User Journey Scenario

Role-based opening scenario: a contributor or agent has completed implementation or needs an intentional checkpoint and must decide how the current branch or worktree should end. The user may already want a commit, push, draft pull request, local merge, preserved branch, cleanup, or discard. The journey turns that intent plus live repository evidence into a bounded action and a reconstructable handoff.

Open this file when a task mentions branch finishing, worktree cleanup, one of the mapped local skills, or a nearby workflow where stale or ambiguous repository state could corrupt the next action. Do not treat the trigger as proof that implementation, tests, ownership, or authorization are complete.

**Stage 1, frame the outcome:** Record the requested final state and its consequence. A direct request such as "commit the task changes and open a draft pull request" selects a path; it does not authorize unrelated files, force operations, or cleanup. If the request is "what next," retain choice for the later option gate. The stage exits when the agent can state what should exist afterward and what must remain untouched.

**Stage 2, establish authority and identity:** Read current repository instructions and the relevant local source. Confirm repository root, working directory, current branch or detached commit, linked worktree, remotes, upstream, and candidate base as applicable. The stage exits when the intended repository object and governing policy are visible. If the checkout is detached, the base uncertain, or permissions external, stop or route before pretending a standard path applies.

**Stage 3, scope ownership:** Inventory staged, unstaged, and untracked state. Review the changed files and distinguish task-owned edits from pre-existing or concurrent work. Do not stage broadly merely to simplify the finish. The stage exits with an explicit save scope and a list of unrelated state that will be preserved. If ownership cannot be resolved, preserve evidence and return to the owner rather than creating a mixed commit.

**Stage 4, verify the claim:** Run the project-defined checks that support the requested outcome. A release-ready or merge-ready claim usually needs more evidence than a local checkpoint. If a relevant check fails, choose among repair, explicit non-ready checkpoint, or blocked handoff. Do not continue to merge or ordinary publication while calling failures irrelevant without policy evidence. Record the tested tree; later relevant edits invalidate the result.

**Stage 5, confirm the path:** If the user already chose, confirm only unresolved consequential details such as remote, branch scope, or destructive inventory. If no path is selected, present the four concise outcomes: merge locally, push and create a pull request, keep the branch as-is, or discard after confirmation. Publication and cleanup remain separate. The stage exits with one authorized transition and a stated recovery plan.

**Stage 6, execute minimally:** Save only the reviewed scope, publish only to the verified destination, merge only into the intended base, preserve when requested, or discard only after showing what will disappear and receiving exact confirmation. Stop after an unexpected result. Do not escalate to force, broaden staging, or remove another worktree merely to reach the expected appearance.

**Stage 7, prove and hand off:** Verify outcome-specific postconditions. Record commit, branch, remote, pull request or merge, worktree path or removal, relevant check status, unrelated dirty state, pending asynchronous gates, recovery reference, and next owner. A journey can end locally complete while CI or review remains explicitly pending.

The primary worked journey is a direct draft-PR request. The agent discovers a feature worktree with three task files and one unrelated user note, stages and reviews only the task files, runs current checks, creates the intentional commit, pushes the verified feature branch, creates the draft, confirms the remote commit, reports pending CI, and preserves both the user note and worktree because cleanup was not requested. The handoff names the draft and the next reviewer.

Alternative exits change the required evidence:

- **Local merge:** confirm the base, update according to repository policy, merge, rerun required checks on the merged tree, verify integration, and only then consider cleanup.
- **Keep:** make no unintended mutation; report branch, commit state, dirty summary, worktree path, and why it remains.
- **Checkpoint:** save the explicitly scoped state and report every failed or unrun gate plus the condition for resuming completion.
- **Discard:** inventory commits, tracked and untracked changes, and worktree; obtain exact confirmation; remove only the intended state; verify unrelated work remains.
- **Blocked:** preserve current evidence, name the failed precondition and owner, and state what result returns the task to Stage 2, 3, or 4.

Evidence can expire between stages. Any relevant tree mutation invalidates status, diff, and affected test evidence. A changed upstream or remote invalidates destination assumptions. Updated repository instructions invalidate policy decisions. A read-only operation does not require a full restart; rerun only dependent gates and preserve the rest.

Good completion is the requested, verified, and recoverable final state. Bad completion publishes or deletes from an assumed state. A borderline journey safely preserves an unrelated file but omits it from the handoff, causing the next agent to mistake it for new work. Visibility is part of preservation.

Repeated friction should improve the environment. Common base, remote, check, worktree-retention, and draft-first choices belong in maintained repository instructions after owner approval. Recurrent mixed-state or cleanup mistakes may justify safer scripts with regression fixtures. Ordinary cases should become predictable while exceptional ownership and destructive decisions remain visible to humans.

## Decision Tradeoff Guide

Choose by matched conditions, not source wording alone. User intent selects the desired outcome; repository policy and observed state determine whether that outcome is currently safe; source guidance supplies defaults where those inputs are silent.

| decision_option_name | when_to_choose_condition | tradeoff_cost_description | verification_question_prompt |
| --- | --- | --- | --- |
| Adopt when | Request, current policy, observed state, local source contract, and verification align. | Fastest and most predictable path, but copying literal commands can preserve stale environment assumptions. | Do the source preconditions hold for this exact branch, worktree, remote, base, and requested outcome? |
| Adapt when | The state-transition contract fits but repository mechanics, checks, remotes, hosting, or user interaction differ. | Preserves the safety model while adding author-owned inference and review responsibility. | Is every changed condition visible, and do postconditions prove the adapted path achieved the same authorized result? |
| Pause or route when | Ownership, policy, state, permissions, quality, or destination are missing, conflicting, or outside this guide. | Prevents false confidence but can delay integration or require another owner. | Does the handoff name the failed precondition, preserved state, responsible authority, and return condition? |
| Cost of being wrong | The wrong path can publish unrelated edits, merge into the wrong base, delete recoverable work, misstate readiness, or strand a reviewer. | Correction may require history repair, coordination, rework, or may be impossible after unreferenced data is removed. | Can a reviewer identify what to undo, which recovery references remain, who was affected, and what evidence prevents recurrence? |

| outcome | choose_when | accepted_cost | decisive_postcondition |
| --- | --- | --- | --- |
| Local commit | The user wants an intentional local save and reviewed scope can be isolated. | No remote durability or shared review; branch may still be behind or unready. | The new commit contains only intended changes and unrelated dirty state remains visible. |
| Checkpoint commit | Work must be preserved despite failed or incomplete gates and the user accepts that status. | Creates debt and can be mistaken for ready work. | Commit and report are clearly labeled non-ready with failures, owner, and resume condition. |
| Push branch | Remote durability or collaboration is requested without necessarily creating a review artifact. | Exposes state remotely and may trigger automation. | The intended remote branch contains the recorded commit and pending checks are named. |
| Draft pull request | Review and remote durability are useful before merge readiness. | Requires hosting access and ongoing review ownership. | Draft identity, base, head commit, pending gates, and preserved worktree state are reported. |
| Ready pull request | Local and repository-required readiness evidence supports formal review. | Asynchronous CI and reviewers can still reject it. | PR state, exact commit, applicable checks, and unresolved risks are current. |
| Local merge | Repository policy permits local integration and the intended base is confirmed. | Can diverge from remote policy or require updating the base first. | Merge exists on the correct base and required checks pass on the merged tree. |
| Keep branch and worktree | The user wants to continue later, ownership is pending, or recovery value remains high. | Consumes workspace and creates stale-state risk over time. | Exact branch, path, dirty summary, owner, and revisit trigger are reported. |
| Cleanup after durable outcome | The commit is integrated or remotely durable, no local-only state remains, and cleanup is explicitly requested or governed. | Removes convenient local recovery and environment state. | Only intended branch or worktree references disappear; shared and unrelated work remain. |
| Confirmed discard | The user knowingly rejects inventoried work and recovery limits are understood. | May be irreversible, especially for untracked or unreferenced data. | Exact confirmation precedes action and post-state proves only intended work was removed. |

Resolve major tradeoffs explicitly:

- **Direct execution versus option menu:** direct execution respects clear intent and saves time; the menu preserves choice when intent is absent. Never use the menu to avoid a complete request or direct execution to avoid missing confirmation.
- **Local versus remote durability:** local saves are fast and private; pushes and pull requests protect against local loss and enable review but expose work and may trigger policy.
- **Review versus integration speed:** draft or ready PRs add collaboration and asynchronous checks; local merge is faster only when current policy permits it.
- **Fix versus checkpoint:** repair supports readiness; checkpoint preserves progress. Label the latter so persistence is not mistaken for quality.
- **Cleanup versus recovery:** cleanup reduces clutter; retention preserves environment and recovery. Separate publication from cleanup and use a retirement trigger.
- **One broad commit versus scoped commits:** broad saves can preserve an emergency snapshot; scoped saves improve ownership and review. Inventory any knowingly mixed checkpoint.

For example, after a direct draft-PR request on a clean task scope, preserve the worktree and report pending CI. Do not locally merge into `main` merely because a merge-base command succeeds; project policy may use another target. A mixed emergency checkpoint is borderline rather than automatically wrong when every included change, owner, debt, and exit condition is recorded.

Record selected outcome, state evidence, authorization, rejected alternative when consequential, expected cost, recovery path, and reversal trigger. A branch retained for pending review can be cleaned after merge and confirmation; a checkpoint can be promoted after failures are fixed; a draft can become ready after checks pass. These triggers keep conservative choices temporary rather than vague.

Portfolio cleanup is a separate maintenance process. Many individually sensible retained worktrees and branches can accumulate stale ownership. Inventory them, find owners and durable outcomes, verify current state, and clean in reviewed batches. Do not use age alone as permission to delete.

## Local Corpus Hierarchy

Classification vocabulary includes canonical, supporting, legacy, duplicate, and conflicting source roles. These are claim-relative relationships, not permanent global quality ranks. Preserve the seed's lineage labels, then determine operational precedence from explicit intent, current repository policy, observed state, and the exact decision each source covers.

| local_source_filepath_value | seed_corpus_hierarchy_role | operational_claim_scope | exclusion_or_conflict | reviewer_question_to_answer |
| --- | --- | --- | --- | --- |
| `agents-used-monthly-archive/claude-skills-202603/superpowers/finishing-a-development-branch/SKILL.md` | canonical primary source | Detailed default finish mechanics: checks, candidate base, four outcomes, discard confirmation, branch and worktree cleanup. | Contradicts itself on PR cleanup and cannot override explicit user or project policy. | Which exact finish rule is being reused, do its preconditions hold, and does another line in the same source conflict? |
| `agents-used-monthly-archive/claude-skills-202603/superpowers/using-git-worktrees/SKILL.md` | legacy historical source | Worktree placement, ignore safety, setup examples, baseline checks, and creation-to-cleanup lifecycle. | Literal dependency and `.gitignore` mutations need current project authorization. | Which creation invariant affects finish safety, and has current state verified it? |
| `agents-used-monthly-archive/codex-skills-202604/finishing-a-development-branch/SKILL.md` | legacy historical source | Direct-request behavior, intentional saving, default remote behavior, concise option menu, and handoff runway. | Less detailed about worktree removal and not globally superior merely because it is later. | Did the user already choose a path, and which missing mechanic requires companion evidence? |
| `claude-skills/superpowers/finishing-a-development-branch/SKILL.md` | supporting context source | Active alias for workflows invoking the Claude finish skill. | Byte-identical duplicate of the archived canonical row, including its contradiction. | Is this path required for invocation, and has its semantic content already been counted once? |
| `claude-skills/superpowers/using-git-worktrees/SKILL.md` | supporting context source | Active alias for workflows invoking worktree creation and cleanup guidance. | Byte-identical duplicate of the archived worktree row. | Does the current alias still resolve to the recorded content, and which lifecycle rule applies? |

Use this decision-authority ladder:

1. **Explicit user authorization:** selects among valid outcomes and supplies exact destructive confirmation. It cannot make an impossible or policy-forbidden mechanic valid.
2. **Current repository policy:** defines required checks, protected branches, integration base, remotes, worktree conventions, and operational limits.
3. **Observed repository state:** confirms or falsifies source preconditions, including branch, worktree, dirty scope, upstream, and remote configuration.
4. **Codex finish interaction:** governs direct-request execution and intentional save reporting where current policy is silent.
5. **Claude finish decision model:** governs the concise four-option fallback, test-first completion, and destructive inventory, with the cleanup conflict resolved conservatively.
6. **Claude worktree lifecycle:** governs directory and baseline context needed for isolation and cleanup mechanics.
7. **External evidence:** after refresh, clarifies platform semantics but does not replace intent or local policy.

Precedence applies one claim at a time. The later Codex source can govern whether to force an option menu while the older worktree source still supplies the only mapped ignore-safety and baseline procedure. A project rule can replace the generic base branch without invalidating the generic discard-confirmation safeguard. Composition is more accurate than declaring one file the universal winner.

The hierarchy fails under simple latest-file-wins, archive-first, or current-path-wins rules. Date and location do not establish applicability. Duplicate current aliases support compatibility, not corroboration. Internal contradiction cannot be resolved by counting an identical alias as agreement. When no current authority settles the PR cleanup conflict, preserve the branch and worktree until explicit cleanup intent and safe postconditions exist.

Canonical means a maintained source governs a defined decision in a stated environment. Supporting adds applicable detail. Legacy preserves historical or still-useful mechanics without governing current policy by itself. Duplicate exposes the same semantic content through another path. Conflicting means applicable instructions imply different outcomes. Record which relationship applies to each claim and what evidence would reverse it.

Good hierarchy follows a direct push request through Codex interaction rules, uses Claude evidence for checks and worktree retention, and adapts the remote to observed configuration. Bad hierarchy follows the first cleanup line because its row is labeled canonical. Borderline hierarchy treats the later Codex file as globally superior, then has no rule for the linked worktree; add the older lifecycle evidence rather than inventing mechanics.

Verify hierarchy with content hashes, relevant complete reads, claim mappings, conflict fixtures, project instructions, and live preconditions. A changed hash reopens dependent claims first. If aliases are retained for multiple agent ecosystems, centralize semantic ownership and test that they do not silently fork. Retire an alias only after all invoking workflows have a compatible route.

## Theme Specific Artifact

Theme-specific artifact: a dirty-worktree state-transition matrix with commit scope, publication decision, cleanup boundary, postconditions, and recovery. Complete it before mutation when state is mixed, shared, remote, or destructive. For a clean low-risk local save, use the compact subset: identity, request, scope, checks, action, postcondition, and remaining state.

| artifact_field_name | artifact_completion_rule | evidence_source_hint | worked_feature_auth_value |
| --- | --- | --- | --- |
| `repository_and_worktree_identity` | Record repository root, exact working directory, linked worktree path, and branch or detached commit. | `git rev-parse`, branch inspection, and `git worktree list --porcelain`. | Repository `/repo`; worktree `/repo/.worktrees/auth`; branch `feature/auth`. |
| `user_goal_statement` | State the requested final state and whether the user already selected a direct path. | Current request and clarified consequence. | Create an intentional commit for task files, push the feature branch, and open a draft pull request. |
| `applicable_policy` | Name repository instructions, protected targets, required checks, remote convention, and cleanup rule. | Current repository files and accessible platform policy. | Use repository test script; draft targets `main`; no automatic worktree cleanup rule found. |
| `dirty_state_inventory` | Record staged, unstaged, untracked, conflicted, ignored-risk, and submodule state as applicable. | Porcelain status plus focused inspection. | Three task files unstaged; one unrelated untracked `notes.txt`; no conflict. |
| `ownership_classification` | Classify every changed path as task-owned, user-owned, shared, generated, unknown, or intentionally mixed. | Task scope, prior state, user confirmation, and diff review. | Three auth files task-owned; `notes.txt` user-owned and excluded. |
| `commit_scope_rule` | Name exact paths or patch hunks to stage, commit purpose, and excluded state. | Reviewed diff and ownership record. | Stage only the three auth paths; preserve `notes.txt`; commit explains auth behavior and tests. |
| `readiness_evidence` | List current tests, build, lint, formatting, policy, and known gaps with the tree identity they cover. | Repository commands and current results. | Auth tests and full project suite pass on the staged content; remote CI not yet observed. |
| `base_upstream_remote` | Record candidate base, tracking branch, named remote, and how each was verified when the action needs them. | Repository policy, merge-base discovery, upstream, and redacted remote data. | Base `main`; push branch `feature/auth` to verified remote `origin`; no force. |
| `selected_transition` | State one action: commit, checkpoint, push, draft PR, ready PR, local merge, keep, cleanup, or confirmed discard. | User goal plus decision tradeoff guide. | Commit, push, and draft PR; integration remains pending review. |
| `publication_boundary` | Separate remote publication from merge acceptance and asynchronous checks. | Hosting output and observed check state. | Draft PR is successful publication; merge readiness remains pending CI and review. |
| `cleanup_boundary` | State whether branch and worktree are preserved or removed, why, and which evidence would reverse the choice. | Explicit request, source conflict, worktree state, and retirement policy. | Preserve branch and worktree; reconsider after merge, clean state, and owner-confirmed cleanup. |
| `destructive_confirmation` | Inventory what will disappear and record exact confirmation only when discard or force removal applies. | User authorization and recovery analysis. | Not applicable because no destructive action is selected; this reason is part of the record. |
| `action_commands_and_results` | Record concise exact actions, targets, exit results, and unexpected behavior without leaking credentials. | Shell and hosting outputs. | Scoped staging and commit succeed; branch push succeeds; draft PR identity recorded. |
| `verification_gate_rule` | Define postconditions that prove the chosen transition rather than merely checking command presence. | Verification Gate Command Set. | Commit contains only task paths; remote branch contains commit; PR is draft; user note and worktree remain. |
| `recovery_path` | Name references and steps available if publication, integration, or cleanup is wrong. | Commit and branch identifiers, remote state, reflog where applicable, and retained worktree. | Retained worktree and feature branch preserve local recovery; revert or follow-up remains available after review. |
| `remaining_state_and_owner` | Record unrelated changes, pending checks, review, cleanup trigger, and next person or agent. | Post-action status and handoff decision. | `notes.txt` remains user-owned; CI and reviewer own next acceptance; author owns post-merge cleanup. |
| `freshness_trigger` | Name which mutation or policy change invalidates this matrix. | Change-impact analysis. | Any new tree change, remote retarget, base-policy update, or PR-head update reopens dependent fields. |

Use explicit states: `verified`, `pending`, `blocked`, `not applicable with reason`, or `unknown and action-stopping`. Do not fill unknown authority with a plausible default. A complete-looking matrix does not manufacture permission. If cleanup is selected while local-only changes remain, or publication targets a remote that was never verified, the contradiction blocks action.

| situation | safe_transition | state_that_must_remain | decisive_gate |
| --- | --- | --- | --- |
| Clean task-only branch and direct commit request | Scoped commit. | Branch remains local unless publication was also requested. | Commit tree and message match reviewed task scope. |
| Mixed dirty tree and draft-PR request | Commit only owned paths, push intended branch, create draft, preserve unrelated files and worktree. | User and unknown changes remain untouched and reported. | Staged diff, remote commit, draft identity, and post-status all match the matrix. |
| Relevant test fails but explicit checkpoint requested | Clearly labeled checkpoint of reviewed scope. | Failure evidence, unrelated changes, and resume condition remain. | Commit exists and report does not claim readiness. |
| Local merge requested | Confirm base and policy, integrate, rerun checks on merged tree, then decide cleanup. | Recovery references remain until merged postconditions pass. | Correct base contains intended commit and merged-tree checks pass. |
| Keep requested | No finish mutation beyond any explicitly requested save. | Branch, worktree, dirty state, and ownership remain visible. | Post-status matches pre-state except authorized save. |
| Discard requested | Inventory, exact confirmation, targeted removal, postcondition. | Unrelated branches, worktrees, and files remain. | Confirmation matches inventory and only intended state disappears. |

Raw command transcripts are evidence inputs, not the artifact. The matrix interprets state, ownership, authorization, and consequence. A prose handoff, issue, PR template, or automated status view may derive from it, but one canonical record should govern to avoid drift.

Good completion names `feature/auth`, excludes `notes.txt`, publishes the exact commit, records pending CI, and preserves the worktree. Bad completion writes "all changes" for scope and "recover with Git" for recovery. Borderline completion records pending CI but no owner or follow-up trigger; pending state without responsibility becomes assumed success.

Verify from the planned mutation backward. Every target, path, readiness claim, cleanup choice, and destructive permission must trace to current evidence. Then verify forward from the action to postconditions. When shared or delayed, the matrix also becomes the cleanup contract: it names who can retire the branch and worktree, under what trigger, and with which final checks.

## Worked Example Set

Treat each example as a state-transition fixture. Record request, pre-state, ownership, checks, selected transition, cleanup decision, postcondition, and recovery. Branch names, paths, and remotes are illustrative; discover and verify them in the target repository.

**Example 1, mixed dirty tree and direct draft pull request**

- **Request:** Commit the authentication task changes, push the feature branch, and open a draft pull request.
- **Pre-state:** Worktree `/repo/.worktrees/auth`, branch `feature/auth`, three task files changed, one unrelated untracked `notes.txt`, verified base `main`, and verified remote `origin`.
- **Good path:** Review and stage only the three task files, run relevant checks on the intended content, commit intentionally, push `feature/auth`, create the draft against the verified base, confirm the remote head commit, report pending CI, preserve `notes.txt`, branch, and worktree.
- **Bad path:** Run broad staging, include `notes.txt`, push, then remove the worktree because PR creation succeeded.
- **Borderline path:** Correctly exclude the note and create the draft, but describe the branch as merge-ready before required remote checks finish. Publication passed; readiness did not.
- **Recovery and verification:** Retained branch and worktree preserve local context. Verify staged diff, commit tree, remote head, draft state, post-status, and pending check ownership.

**Example 2, requested local merge**

- **Request:** Merge the completed feature locally into the repository's integration branch.
- **Pre-state:** Feature checks pass; the common-base heuristic finds `main`, but repository instructions designate `develop` as the integration branch.
- **Good path:** Follow current policy, confirm `develop`, update it through the permitted workflow, merge the intended feature, run required checks on the merged tree, verify the feature commit is integrated, then ask or follow explicit policy for cleanup.
- **Bad path:** Merge into `main` because the command succeeded and delete the feature branch before tests on the merged tree.
- **Borderline path:** Merge correctly into `develop` and pass checks but remove a linked worktree containing an unrelated untracked file. Integration succeeded while cleanup violated ownership.
- **Recovery and verification:** Preserve the feature reference until merged-tree evidence is current. Verify base identity, merge ancestry, test result, dirty state, and exact cleanup target.

**Example 3, explicit non-ready checkpoint**

- **Request:** Save progress before interruption even though one known test fails.
- **Pre-state:** Owned parser edits are isolated; the failure is reproducible and documented; no remote publication was requested.
- **Good path:** Review the scoped changes, create an intentionally labeled checkpoint commit, retain the failing-test evidence and resume condition, and report branch and worktree location without claiming completion.
- **Bad path:** Hide the failure from the report and call the branch ready because a commit now exists.
- **Borderline path:** Save a mixed checkpoint containing another person's edit during an emergency, but inventory every included file, obtain consent, assign ownership, and define a split or cleanup action. The state is accepted debt, not a clean default.
- **Recovery and verification:** Verify the checkpoint contains the declared scope and the handoff preserves failure output, owner, and next test.

**Example 4, confirmed discard**

- **Request:** Discard an abandoned experimental branch and worktree.
- **Pre-state:** Two local commits are absent from remotes, one untracked generated artifact is reproducible, and one untracked research note is not reproducible.
- **Good path:** Show the exact branch, commits, worktree, generated artifact, and research note. Preserve or explicitly exclude the valuable note, explain recovery limits, request exact confirmation for the revised inventory, perform only the confirmed removal, and verify unrelated state remains.
- **Bad path:** Force-delete branch and worktree immediately because the user used the word discard before seeing the inventory.
- **Borderline path:** Rely on reflog as guaranteed recovery for every item. Some references may remain recoverable, but untracked files and retention duration do not support that promise.
- **Recovery and verification:** Use a disposable repository to test mechanics. In real work, confirmation and post-state inspection are mandatory; never test destruction on valuable state merely to validate documentation.

The original process guidance remains: load relevant local sources, retain external evidence boundaries, and attach concrete gates. Generic Git tutorials are insufficient because safe actions depend on the live tree and authorization. A confidence warning alone does not repair unknown ownership or destination; stop or preserve until those facts are resolved.

Use unseen variations as regression tests. Swap the current branch while keeping tests green. Add one untracked user file. Remove upstream configuration. Change the repository base. Request a draft without cleanup. Make remote CI pending. Change an ordinary checkpoint into discard. A correct guide changes its action and report with those variables.

Commands in these examples are intentionally subordinate to invariants. Verify literal mechanics with installed Git, repository policy, and disposable fixtures where destruction is involved. Retire or revise an example when readers succeed by memorizing its branch names but fail an equivalent changed state.

## Outcome Metrics and Feedback Loops

The governing leading indicator remains: the next task uses the reference to make a better decision with less ambiguity. Measure that through the requested state transition and its invariants, not through one vanity score.

| outcome_layer | observable_signal | collection_method | interpretation_boundary | response_to_failure |
| --- | --- | --- | --- | --- |
| Source and policy use | The selected workflow and commands match current user intent, repository policy, and applicable source boundaries. | Decision record with source and policy references. | Process evidence does not prove live state or action success. | Correct authority mapping and reopen dependent decisions. |
| Scope accuracy | Every staged or removed path is intended, and unrelated tracked and untracked state remains. | Pre-state inventory, staged diff, post-state comparison, and owner review. | Git cannot determine human ownership alone. | Contain publication or cleanup, restore when possible, and repair staging rules. |
| Readiness truthfulness | Tests and checks support exactly the claimed checkpoint, publication, merge, or release status. | Commands, tree identity, timestamps or sequence, and pending-gate record. | Passing local checks does not predict every remote result. | Narrow the claim, fix failures, or preserve as a non-ready checkpoint. |
| Transition accuracy | The agent performs the explicit or selected commit, push, PR, merge, keep, cleanup, or discard outcome. | Requested outcome compared with command and hosting results. | Command success can still target the wrong valid branch or remote. | Stop, preserve evidence, recover, and repair target discovery. |
| Postcondition match | Expected commit, branch, remote, PR, base, worktree, and dirty state are observed afterward. | Outcome-specific status, log, upstream, hosting, and worktree inspection. | Asynchronous checks may remain pending. | Assign pending ownership or treat mismatch as an incomplete transition. |
| Recovery preservation | Recovery references and local-only state remain until their value is intentionally retired. | Branch, commit, worktree, remote, and backup inventory. | Reflog is not guaranteed recovery for every untracked or expired object. | Preserve additional state, disclose limits, or block cleanup. |
| Handoff closure | The report names what was saved, where, checks, unrelated state, pending work, cleanup trigger, and next owner. | Fresh-agent or reviewer reconstruction exercise. | A clear report cannot repair an unsafe underlying action. | Repair state first, then update the handoff and repository guidance. |
| Lifecycle health | Retained branches and worktrees have owners and retirement triggers; obsolete state is cleaned deliberately. | Periodic or event-triggered inventory chosen by repository owners. | Age alone does not prove safety to delete. | Locate owner and durable outcome before reviewed cleanup. |

Use two modes. A low-risk local commit needs scope, requested save, relevant checks, commit postcondition, and remaining-state report. A shared, integrated, or destructive outcome needs full authority, destination, recovery, handoff, and lifecycle evidence. Reuse the dirty-worktree matrix instead of creating a second record.

The original failure signal also remains: the reference is only a source map and never becomes an operating guide. Other failure signals include a clean tree produced by mixed staging, a successful push to the wrong destination, green tests attached to an older tree, a PR described as ready while checks are pending, a worktree removed before local-only files are inventoried, and retained state with no owner.

Avoid proxy optimization. Commit count does not measure scope quality. PR count does not measure review readiness. Test pass rate does not measure authorization. Short finish time does not measure recovery. Clean-tree rate can actively reward sweeping away evidence. Use each only for its narrow diagnostic role and retain severity: one irreversible wrong-scope deletion can outweigh many routine successes.

A good outcome record says: "Three reviewed task files were committed; `notes.txt` remained user-owned; project checks passed on the recorded tree; the requested draft PR points to that commit; CI is pending with the reviewer as next owner; worktree cleanup follows merge and author confirmation." A bad record says "clean and pushed." A borderline record proves the PR but cannot show whether an automatically removed worktree held local-only state.

Define the baseline before claiming improvement: pre-state, expected transition, unrelated-state invariant, applicable quality claim, postcondition, observer, reference version, and repository policy. Report raw cases and error categories before percentages. Small convenience samples do not support universal reliability or speed claims.

Close the feedback loop at the owning layer:

1. Wrong intent mapping returns to direct-request and option behavior.
2. Wrong scope returns to ownership inventory and staging tooling.
3. Stale quality evidence returns to invalidation rules and project checks.
4. Wrong target returns to repository base, remote, and upstream policy.
5. Premature cleanup returns to publication-cleanup separation and recovery gates.
6. Incomplete handoff returns to the artifact schema and next-owner contract.
7. Recurrent ambiguity returns to repository instructions or safer automation.

Re-run deterministic reference verification after every generated-reference edit. Refresh public sources only when browsing is permitted and a current platform claim matters. Review branch operations on source or policy change, repeated failure, new hosting behavior, or increased consequence. Repository owners may choose an inventory cadence for quiet worktree accumulation; no universal interval is asserted.

Retire a metric that never changes action or duplicates stronger evidence. Promote a new gate after a severe escape or recurrent failure. The goal is enough independent evidence to identify whether the defect belongs to intent, policy, state, quality, mechanics, recovery, or handoff.

## Completeness Checklist

Use this checklist as an index to evidence, not proof by enumeration. Complete can still be wrong, stale, unauthorized, or unsafe. Every consequential item needs a current source, state observation, explicit request, policy, review, command result, postcondition, or reasoned exclusion.

**Reference artifact contract**

- The 26 original heading texts remain in exact seed order and every evolved section is strictly longer than its seed counterpart.
- The packet has 26 sections, 260 exact question headings, and 1,560 populated mandatory fields.
- All 1,560 field values remain exact-text unique and unique after Section and Question context prefixes are stripped.
- Packet questions exactly match the specification and every field contains section- and question-specific rationale rather than repeated filler.
- Reference and packet are ASCII-only, contain no prohibited work markers, have clean whitespace, and end with a newline.
- Markdown tables have consistent columns and separator rows; fences are balanced and carry appropriate language identifiers.
- Public URLs not inspected in this no-browse evolution are labeled unrefreshed rather than presented as current facts.
- The complete packet and reference are reread with persisted review checkpoints at least every five sections.
- The focused verifier passes the exact target path and the progress journal records Green and final Refactor evidence.

**Reader and decision contract**

- The role scenario names the user, starting state, requested or unknown outcome, consequence, and trigger for Branch Finish Worktree Patterns.
- Direct commit, push, draft-PR, keep, checkpoint, cleanup, and discard requests are honored without a redundant option menu after safety gates.
- An unknown outcome receives the concise four-option choice after finishability is established.
- The guide states when it is only orienting and which adjacent authority owns conflict resolution, release, hosting administration, or repository recovery.
- The next state, stop condition, and next owner are observable.

**Source and authority contract**

- The local corpus hierarchy identifies canonical, supporting, legacy, duplicate, and conflicting roles at claim scope.
- All five local paths were read completely; byte-identical Claude pairs count as two artifacts exposed through four aliases, not four independent sources.
- The internal PR cleanup contradiction is visible and resolved conservatively unless current policy or explicit intent governs otherwise.
- User authorization, repository policy, observed Git state, local source guidance, external evidence, and synthesis remain distinct.
- Repository-specific bases, remotes, checks, and cleanup rules replace generic defaults when current and applicable.

**State and ownership contract**

- Repository root, working directory, branch or detached state, and linked worktree are identified before mutation.
- Staged, unstaged, untracked, conflict, and relevant submodule state are inventoried.
- Every changed path or hunk in the save scope has an ownership classification; unrelated and unknown work remains untouched or action-stopping.
- Base, upstream, and remote are verified only when the selected transition needs them; common names are not silently assumed.
- Any state mutation after capture reopens dependent status, diff, and quality evidence.

**Quality and readiness contract**

- Repository-defined checks run against the relevant tree, and their exact coverage is reported.
- A failing or unrun gate blocks a ready claim unless the user explicitly requests a clearly labeled checkpoint.
- Local checks, remote CI, review, merge readiness, and release readiness are reported as separate states.
- Tests do not substitute for scope, ownership, authorization, destination, or postcondition evidence.

**Transition contract**

- The chosen action matches the explicit request or selected menu option.
- Commit scope and message are intentional; broad staging occurs only when every change is reviewed and owned.
- Publication uses the verified branch and remote without force unless separately authorized and governed.
- Local merge uses the intended base and reruns required checks on the merged tree.
- Pull-request publication does not imply cleanup; branch and worktree remain by default when intent is absent.
- Discard inventories what will disappear and waits for exact confirmation before any destructive action.
- Unexpected action results stop escalation and preserve diagnostic evidence.

**Postcondition and recovery contract**

- The resulting commit, branch, upstream, remote, pull request, merge, worktree, and dirty state match the chosen outcome.
- Unrelated tracked and untracked work remains visible and is named in the handoff.
- Remote checks and review are observed, pending with an owner, inaccessible, or not applicable with reason.
- Cleanup happens only after remote or integrated durability, absence of local-only state, exact target verification, and explicit intent or policy.
- Recovery references and limits are stated; reflog is not promised for every untracked or expired object.
- The finish report names what was saved, where, checks, pending work, cleanup trigger, and next owner.

**Routing and maintenance contract**

- The adjacent routing section sends unfinished work, conflict, release, platform administration, and damaged repository state to an appropriate authority with a return condition.
- Durable scripts, hooks, prompts, and policies have owners, scoped fixtures, rollback, and update triggers.
- Recurrent wrong-base, wrong-remote, mixed-scope, stale-check, or premature-cleanup failures improve repository policy or tools.
- Retained branches and worktrees have owners and retirement triggers; age alone never authorizes deletion.
- The complete evolved file is reread for contradiction, duplicated generic prose, unsupported precision, and stale examples before final Refactor completion.

Use a compact mode for a low-risk local keep or scoped commit: requested outcome, identity, dirty summary, ownership, relevant checks, action, postcondition, and remaining state. Use the full operation checklist for remote publication, integration, shared state, cleanup, force, or discard. Add environment-specific gates through their authoritative policy; this reference does not supersede protected-branch, compliance, release, or hosting controls.

A good completion response points to the scoped diff, current checks, explicit request, resulting commit or PR, preserved unrelated file, pending owner, and cleanup trigger. A bad response says "covered" or "clean." A valid pending response names the asynchronous gate, consequence, owner, and follow-up. If an item cannot be answered and can change safety, the action remains blocked.

Reopen dependent items when the tree, policy, source, base, upstream, remote, check result, ownership, or requested outcome changes. Then perform a final whole-state coherence review. If the checklist never changes or blocks an action, inspect whether its questions still discriminate risk and retire low-signal duplication.

## Adjacent Reference Routing

Routing is an operational boundary, not a suggestion to read vaguely related material. Keep this reference in control while determining the requested finish outcome, repository identity, worktree state, change ownership, relevant quality evidence, and whether the proposed transition is reversible. Hand off before performing a mutation governed by implementation, conflict recovery, release, platform administration, security, or repository repair. A route must preserve the work and evidence needed to return; it does not grant new authorization.

Use this compact rule:

1. **Continue here** when the next action is a scoped commit, authorized push, pull-request handoff, local integration, deliberate keep, safe cleanup, or explicitly confirmed discard of finishable work.
2. **Clarify here** when the state is understood but the desired outcome or ownership is not. Preserve the branch and worktree while asking the smallest consequential question.
3. **Route out** when the next mutation changes implementation, resolves history or content conflicts, performs a release or deployment, administers a protected platform resource, or repairs damaged repository state.
4. **Return here** only after the receiving procedure supplies its named return evidence. Refresh every mutable observation invalidated during the handoff.

The same person or agent may execute both workflows. The logical boundary still matters because a code fix, conflict resolution, deployment, and branch cleanup have different authorization and verification contracts.

| observed_trigger | receiving_authority_or_procedure | action_this_reference_must_not_imply | minimum_transfer_bundle | return_or_stop_condition |
| --- | --- | --- | --- | --- |
| Required implementation or test behavior is incomplete | language-specific implementation and test workflow | Editing additional behavior merely to make the branch look finishable | repository and worktree path, branch and commit identity, scoped diff, failing command and output, ownership notes, requested outcome | Return after the intended behavior is implemented and relevant checks have current results; stop if scope or intent materially changes. |
| Merge, rebase, cherry-pick, or revert has unresolved content or history conflicts | repository conflict-resolution or history-recovery procedure | Choosing conflict content, rewriting shared history, or aborting an operation without understanding current state | active Git operation, conflict paths and stages, original heads when available, local-only changes, policy constraints, recovery objective | Return after the operation has an intentional resolved or aborted state and repository-required checks can run; stop for ambiguous ownership. |
| A commit or pull request is ready but release, package publication, deployment, migration, or rollout is requested | repository release or deployment runbook | Treating a push, merge, or green local test as production authorization | immutable revision, target environment or channel, release request, CI and review state, artifacts, approvals, rollback owner | Finish routing ends when the release authority accepts ownership; return only if that procedure requires a new branch-state transition. |
| Protected-branch settings, required checks, credentials, permissions, hosting configuration, or pull-request administration blocks progress | platform administrator or repository maintainer procedure | Bypassing protection, weakening checks, using alternate credentials, or force-updating because ordinary publication failed | exact platform error, repository and remote identity, requested operation, current access boundary, relevant policy, non-secret diagnostic evidence | Return when authorized configuration or access is confirmed; stop if the user or policy does not authorize the administrative change. |
| Objects, refs, index, worktree metadata, submodules, or repository storage appear damaged or inconsistent | repository diagnosis and recovery procedure | Deleting metadata, expiring recovery data, force-resetting, or recloning over local-only state | read-only diagnostics, repository and worktree locations, affected refs and paths, recent operations, backups, local-only inventory | Return only after integrity and ownership are established and the intended work is recoverable; otherwise terminate the finish attempt with recovery ownership. |
| The task only needs explanation, policy interpretation, or documentation correction | applicable documentation or policy owner | Mutating Git state to demonstrate an answer when no finish operation was requested | exact question, observed state if relevant, cited local policy, uncertainty and consequence | Resume only after the clarified rule changes a concrete finish decision; otherwise close without branch mutation. |

**Transfer contract**

Before handoff, capture enough current evidence for the receiving workflow without performing speculative cleanup:

- repository root, current working directory, branch or detached state, current commit, and linked worktree path;
- concise staged, unstaged, untracked, conflict, and relevant submodule state;
- change ownership classification, including unrelated or unknown user work that must remain untouched;
- the user's requested outcome and the exact boundary that prevented this workflow from completing it;
- commands already run, their scope and results, and which observations will become stale if the tree or configuration changes;
- base, upstream, remote, pull request, or platform identity only where already verified and relevant;
- the prohibited next action, receiving owner, return predicate, and recovery information needed if the handoff fails.

Do not remove the branch or worktree before transfer merely to make the environment tidy. A dirty worktree may be the only durable location of the evidence and local-only changes required for implementation or recovery. If the receiving workflow needs a cleaner environment, it must select a preservation strategy with the same ownership and authorization controls as this reference.

**Authority boundaries**

Handoff is not consent. A route to release guidance does not authorize deployment. A route to platform administration does not authorize changing branch protection. A route to conflict recovery does not authorize a force push. A route to implementation does not authorize broadening product scope. Each receiving procedure must obtain or inherit explicit authorization for its own consequential actions and respect repository-specific policy.

Likewise, a technically successful adjacent action does not prove the original branch finish succeeded. A resolved conflict can introduce new behavior. A platform setting can alter required checks. A release may reveal a packaging failure while leaving the branch intact. On return, evaluate the original finish preconditions and postconditions against the new state instead of restoring an old completion label.

**Routing examples**

- Good: a required integration test fails because the feature behavior is incomplete. Record the failing command and scoped diff, preserve unrelated files, route to the implementation workflow, and return after current relevant checks pass. Reinspect scope and ownership before committing.
- Bad: a merge conflict appears, so the agent chooses one side, force-pushes, deletes the worktree, and reports the branch finished. The route, authorization, recovery evidence, and postconditions are all missing even if the remote accepts the update.
- Borderline: a pull request is created correctly and local state is preserved, but the agent begins a production rollout because publication was interpreted as release intent. Stop at the pull-request handoff unless a separate request and runbook authorize the rollout.

**Route verification record**

For a consequential handoff, record a compact trace such as:

| trace_field | required_evidence |
| --- | --- |
| from_state | repository, worktree, branch or detached identity, current commit, dirty summary, and active Git operation |
| route_trigger | observed blocker or requested action that crosses this reference's authority boundary |
| destination | named procedure or owner capable of resolving that trigger |
| evidence_bundle | owned diff, local-only state, checks, policy, errors, and relevant destination identities |
| blocked_mutation | action deliberately withheld because it needs different authority or evidence |
| return_predicate | observable condition that permits branch finishing to resume, or an explicit terminal handoff |
| refresh_set | status, diff, checks, base, upstream, remote, review, or policy evidence invalidated by the adjacent work |

On return, retain immutable evidence such as a recorded commit ID only when it still identifies the relevant revision. Refresh mutable evidence after any tree, index, branch, worktree, configuration, policy, remote, CI, or review change. Reconfirm the user's outcome when the adjacent work materially changed scope or consequence. Then rerun this reference's transition and postcondition checks.

Treat routing loops, repeated rediscovery, lost local state, unexplained cleanup, and unauthorized follow-on actions as defects in the routing map. Record which trigger and transfer field failed. Recurrent failures should improve repository instructions or add a bounded specialist runbook; they should not broaden the finish agent's standing discretion. If no suitable authority exists and the missing decision can affect safety, preserve the current state, report the blocker and recovery options, and stop.

## Workload Model

`combined_evidence_inference_note`: Treat Branch Finish Worktree Patterns as an operating reference for one coherent repository state transition, not as a prose summary or a license to batch every nearby Git task. Local sources support explicit outcome selection, tests, base discovery, intentional saving, worktree handling, and conservative cleanup. They do not support a universal maximum changed-file count. Capacity therefore depends on reviewability, ownership, destinations, reversibility, concurrency, and evidence freshness.

The recommended workload is one repository, one identified branch or worktree, one requested finish outcome, and one reviewable ownership scope. That unit may contain several commits, packages, or test commands when they form one causal story: the user requested one outcome, the changes belong together, the checks cover the claimed behavior, the action has one durability destination, and the postcondition can be verified without hiding partial failure.

File count is only a diagnostic signal. A reproducible generated update can touch thousands of paths while remaining conceptually narrow; a two-file change can be unsafe when one file belongs to another user or contains an untracked secret. Do not inherit the seed's fixed 500-file threshold as policy. If a repository has measured limits for review size, CI duration, hosting payloads, or generated artifacts, use those current local limits and record their unit, scope, and consequence.

| workload_dimension | bounded_signal | pressure_or_split_signal | required_response |
| --- | --- | --- | --- |
| repository identity | one verified repository root and no unexplained nested repository | multiple repositories, unexpected nested metadata, or uncertain root | Split by repository or route to an explicit multi-repository orchestrator. Preserve local-only state before transfer. |
| branch and worktree identity | one named branch or deliberate detached revision in one known worktree | several linked worktrees with relevant edits, branch checked out elsewhere, or unclear active location | Inventory all relevant worktrees, identify the mutation target, and stop if concurrent ownership cannot be resolved. |
| requested outcome | one of commit, push, pull request, local merge, keep, checkpoint, cleanup, or confirmed discard | incompatible outcomes, implied release or deployment, or unresolved user intent | Clarify or separate transitions. Never use one authorization to infer another. |
| change ownership | every staged, unstaged, untracked, and conflict path in scope has one accountable owner | unrelated changes, unknown hunks, another worker's files, or mixed generated provenance | Narrow staging, split the unit, coordinate with the owner, or stop. Do not hide unknown work in a broad commit. |
| semantic scope | one behavior, maintenance objective, or deliberate checkpoint with explainable coupling | unrelated behaviors, several independent fixes, or changes that need different reviewers | Split by behavior or review boundary unless repository policy requires an atomic change. |
| diff reviewability | effective changes can be inspected directly or through a trustworthy generation and comparison method | binary or generated output cannot be explained, rename detection obscures content, or review tooling truncates material changes | Establish provenance and an artifact-specific review method; checkpoint or split when the effective diff remains unknowable. |
| verification scope | current commands cover the claimed tree and outcome, with failures attributable to the unit | independently failing packages, prohibitively broad suites, unavailable required environments, or checks invalidated during action | Separate claims, route missing environments, or label a requested preservation checkpoint as incomplete. |
| destination topology | one verified base, upstream, remote, or pull-request destination relevant to the chosen action | several remotes or bases, protected targets, cross-fork ambiguity, or multiple publication destinations | Split publication steps and verify authority for each destination. Do not silently choose a common remote name. |
| destructive reach | no deletion, or one exact cleanup/discard target with explicit authorization and recovery evidence | several branches or worktrees, local-only files, uncertain object durability, or broad cleanup | Use the full destructive gate, inventory every target, and require separate confirmation where consequences differ. |
| external state | remote CI, review, and platform policy are current or explicitly pending with an owner | stale or inaccessible checks, changing protection rules, concurrent merges, or platform administration | Refresh the relevant state or route to the responsible authority; local success cannot stand in for remote readiness. |
| concurrency | no relevant mutation since inspection, or changes are isolated and detected | another process, agent, hook, or user can modify the same index, branch, worktree, or destination | Reinspect immediately before mutation, serialize conflicting writes, and invalidate dependent evidence after any detected change. |
| recovery complexity | a failed action has a known bounded retry or preservation path | partial multi-target success, unknown history rewrite, repository damage, or cleanup that would erase diagnostics | Stop expansion and route to recovery or orchestration before attempting the transition. |

**Operating modes**

| mode | use_when | evidence_and_action_shape | exit_condition |
| --- | --- | --- | --- |
| compact | low-risk keep, status report, or scoped local commit with known identity and ownership | requested outcome, repository and branch identity, dirty summary, scoped diff, relevant checks, intentional save action, postcondition | Work is preserved at the stated location and remaining state is named. |
| full | push, pull request, local integration, shared branch, cleanup, or discard affects remote, shared, or less reversible state | all compact evidence plus base, upstream, remote, policy, concurrency, recovery, remote checks, and exact cleanup or discard target | Destination and durability are verified, unrelated state is preserved, and pending ownership is explicit. |
| sequenced | several coherent finish units exist but do not require atomic publication | separate evidence record and postcondition for each unit; serialize mutations that share index, branch, remote, or checks | Every completed unit is independently durable and failed units have not contaminated later claims. |
| orchestrated | current repository policy defines a coordinated multi-package or multi-repository transition | follow the named runbook with its atomicity, ordering, approvals, rollback, and partial-failure contract | The orchestrator's postconditions and this reference's branch-state handoff both pass. |
| blocked | ownership, intent, integrity, or destructive consequence remains consequentially unknown | preserve state, report observed facts and missing decision, avoid speculative mutation | Resume only when the missing authority or evidence is supplied; otherwise hand off terminally. |

Choose the smallest mode that covers the real consequence, but do not downgrade a shared or destructive operation because its diff is small. Conversely, do not force a large but coherent generated change into many arbitrary commits solely to satisfy a numeric threshold. A useful split follows an independent owner, behavior, destination, approval, verification scope, or recovery boundary.

**Split conditions**

Split, checkpoint, or route before mutation when any of these conditions cannot be resolved with read-only inspection:

- two changes require different user outcomes, reviewers, owners, or destination branches;
- a subset can be verified and preserved independently while another subset remains unfinished or failing;
- one action can succeed remotely while another can fail locally with no atomic rollback;
- generated, vendored, binary, submodule, sparse-checkout, or large-file state cannot be connected to an intentional source change;
- a nested repository or linked worktree introduces a second index, branch, or local-only state owner;
- cleanup or discard would remove evidence required to verify or recover another unit;
- current state can change between observation and action and the conflict cannot be detected or serialized;
- the operator cannot describe one unambiguous postcondition for the entire proposed batch.

Splitting does not mean dropping difficult state. Each unit needs its own requested outcome, owned scope, current checks, action, destination, recovery boundary, and postcondition. If required checks cannot pass but the user requests preservation, create an intentional checkpoint only after reporting the limitation. A checkpoint is durable work, not evidence of merge or release readiness.

**Repository features that distort apparent size**

Generated files can inflate path and line counts while hiding whether the generator was run from the right source and version. Vendored trees can be intentional snapshots or accidental broad updates. Submodules carry both a superproject pointer and state in another repository. Sparse checkouts can hide tracked paths from the working view. Large-file systems may show a small pointer while the required object is unavailable. Rename detection can make a semantic replacement look like mass deletion and creation. Nested repositories and linked worktrees can place relevant local-only changes outside the current status output.

Probe these features only when status, repository configuration, instructions, or the diff indicates they matter. Do not run an exhaustive feature ritual for every repository. When one is present, use its authoritative local workflow and report what was actually verified. Path-based ownership metadata and diff statistics are useful signals, but they do not replace review of current human ownership and semantic coupling.

**Examples**

- Good compact workload: one feature worktree contains an owned source change and a focused test. The user requested a local checkpoint, the scoped diff is reviewable, and an unrelated untracked note remains untouched. Save intentionally, verify the commit and residual status, and report that broader readiness was not claimed.
- Good full workload: one branch contains an owned feature plus reproducible generated output. The generator check explains the large diff, repository tests pass, one remote and pull-request base are verified, and the worktree remains after publication. High path volume does not make this multi-scope.
- Bad combined workload: one action attempts to commit two owners' changes, push to two remotes, merge locally, deploy, and remove several worktrees. Partial success would make durability and recovery ambiguous, so split or use a repository-defined orchestrator.
- Borderline monorepo workload: one behavior changes three packages, but each package has a different owner and one suite is unavailable. Determine whether repository policy treats them as an atomic contract. Otherwise sequence reviewable units or preserve a clearly incomplete checkpoint.

**Pre-mutation capacity record**

Before a full, sequenced, orchestrated, or destructive operation, record the scope unit, pressure signals, selected mode, split rationale, relevant checks, invalidation triggers, and postcondition owner. Recheck branch/worktree identity and dirty state immediately before mutation. If a collaborator, hook, generator, or tool changed the state, invalidate the affected diff, ownership, and test evidence and classify the workload again.

Parallel read-only discovery can reduce latency across independent units. Serialize writes that share an index, branch, worktree, remote destination, or cleanup target unless an authoritative orchestrator provides stronger concurrency guarantees. The practical capacity limit is the largest unit whose intent, evidence, action, failure recovery, and postcondition remain coherent after that recheck.

Record recurring split reasons. Repeated mixed ownership may indicate weak worktree isolation; repeated cross-package gating may reveal architectural coupling; repeated destination ambiguity may require better repository instructions. Those are maintenance inputs, not reasons to give the finish workflow broader standing authority.

## Reliability Target

Reliability means performing the state transition the user requested without losing or absorbing unrelated work, then reporting only what current evidence supports. It has three independent dimensions:

- **State safety:** intended work remains durable, unrelated state remains preserved, and destructive action has exact authorization.
- **Outcome fidelity:** the resulting branch, commit, remote, pull request, merge, keep, cleanup, or discard state matches the selected outcome.
- **Evidence fidelity:** checks, destination, pending work, cleanup, and readiness are described at their actual scope and freshness.

A finish can preserve bytes yet fail outcome fidelity by pushing the wrong revision. It can reach the correct destination yet fail evidence fidelity by claiming unrun tests. Evaluate all three dimensions; a successful Git exit status proves only that one command accepted its inputs.

**Per-operation invariants**

These are acceptance conditions for each applicable operation, not statistical service objectives. A known miss blocks the affected action or makes the result an incident requiring containment and an explicit handoff.

| reliability_invariant | applicability | passing_condition | primary_evidence | response_to_breach |
| --- | --- | --- | --- | --- |
| repository_identity | every operation | command target, repository root, working directory, worktree, and branch or detached revision are the intended ones | repository and worktree queries captured before mutation and checked again when concurrency matters | Stop, preserve diagnostics, and determine whether any prior mutation affected the wrong repository or worktree. |
| owned_scope | every save, integration, cleanup, or discard | every changed path or hunk included in the action is owned or explicitly authorized; unrelated and unknown state is excluded or action-stopping | staged and unstaged diff, untracked inventory, ownership classification, active-operation state | Unstage or narrow without discarding content; coordinate ownership or stop. |
| destructive_authorization | cleanup, discard, force, or history-affecting recovery | exact target and consequence were inventoried and explicitly authorized under current policy | user request or confirmation, policy, target identity, local-only state and recovery assessment | Do not execute; if already executed, preserve remaining evidence and route to recovery. |
| relevant_quality_claim | any report that calls work complete, ready, integrated, or verified | current repository-required checks cover the claimed tree and outcome, or the narrower pending state is stated | command, revision or tree scope, result, environment, and time relative to later mutations | Retract the unsupported claim, rerun applicable checks, or label a requested checkpoint incomplete. |
| destination_identity | commit publication, pull request, integration, or retention claim | saved revision exists at the verified local or remote destination intended by the user | commit ID, branch/ref, upstream, remote URL, pull-request head/base, merge result where applicable | Stop further publication or cleanup; identify the actual destination and recover or correct only with authorization. |
| unrelated_state_preservation | every mutating operation | pre-existing or concurrent user work remains unchanged and visible unless specifically included by authorization | before-and-after status and diff comparison, worktree inventory, scoped action record | Treat unexpected loss or mutation as an incident; avoid further cleanup and begin recovery. |
| postcondition_closure | every selected outcome | observed final state matches the outcome, residual state is named, and the next owner or stop condition is clear | post-action refs, status, log, worktree list, remote or pull-request state, and handoff | Do not report completion; classify partial success and follow bounded recovery or retry guidance. |
| source_and_policy_boundary | every recommendation and exception | user authorization, repository policy, observed state, local source defaults, unrefreshed external pointers, and synthesis are not conflated | decision record linked to the applicable source or observation | Reevaluate the decision under the actual authority before further mutation. |

The preservation and authorization invariants do not become optional for a low-risk mode. Evidence depth does vary by consequence. A local keep may need identity, dirty state, ownership, requested outcome, and a clear residual-state report. A remote push adds upstream, remote, revision, and remote postconditions. A local merge adds base identity and checks on the integrated tree. Cleanup and discard add exact targets, local-only inventory, durability, confirmation, and recovery boundaries.

**Evidence states**

Use precise states rather than treating every unavailable observation as a failure or silently marking it successful:

| evidence_state | meaning | permitted_claim |
| --- | --- | --- |
| verified | current evidence directly establishes the property for the relevant revision, tree, destination, and environment | State the property and name its evidence scope. |
| pending | an asynchronous check, review, or owner action is expected but not complete | State the durable progress plus pending consequence, owner, and follow-up; do not claim the stronger readiness state. |
| not_observed | evidence was unavailable, inaccessible, or not run | State the gap and its effect; block when it can change safety or the requested claim. |
| not_applicable_with_reason | the property does not apply to the selected outcome | Name the reason, such as no remote publication for a local keep. |
| blocked | a required property is false or consequentially ambiguous | Preserve state, identify the blocker, and route or request the missing decision. |

For example, a pull request can be **verified** as created at a particular URL and revision while remote CI is **pending**. That is a successful publication handoff, not verified merge readiness. A local checkpoint can be **verified** as durable while integration tests are **not_observed**; report it as a checkpoint rather than a completed feature.

**Audit and improvement metrics**

Sampled metrics improve the procedure but never excuse an invariant miss. The seed's "18 of 20" decision-accuracy threshold is not supported as a portable default. A team may adopt a quantitative target only after defining its population, rubric, observation window, owner, confidence limitations, and remediation when misses occur.

| candidate_metric | numerator_and_denominator | useful_segmentation | interpretation_boundary |
| --- | --- | --- | --- |
| correct_outcome_routing | sampled operations whose selected route and outcome match an independent reviewer verdict / all reviewed samples | direct request, unknown intent, conflict, release, recovery, destructive path | Reviewer agreement is a process signal, not proof that an unreviewed operation was correct. |
| precondition_escape | operations with a postcondition mismatch traced to wrong identity, ownership, base, remote, or stale checks / all completed operations | compact, full, sequenced, destructive | A low rate does not permit skipping preconditions; every escape needs causal remediation. |
| unrelated_state_incident | operations that unexpectedly modify or lose out-of-scope state / all mutating finish operations | staging method, worktree layout, concurrent activity | The desired operational invariant is no known incident; report absolute cases as well as any rate. |
| unsupported_readiness_claim | handoffs corrected because check, review, CI, merge, or release evidence was absent or stale / all audited readiness claims | local versus remote claim, checkpoint versus complete | Measures communication and evidence fidelity, not application defect density. |
| partial_transition_recovery | partial actions restored or advanced to an intentional durable state under the recovery contract / all partial transitions | push, pull request, merge, cleanup | A successful recovery does not make the initiating failure harmless; retain root-cause classification. |
| routing_rework | handoffs requiring repeated discovery, circular transfer, or lost context / all routed operations | destination procedure and missing transfer field | Indicates routing-map or transfer-bundle weakness rather than operator speed alone. |

Calibrate alerts from repository history and consequence. A threshold without a baseline can create false precision; a percentage without the absolute count can hide a serious rare event. Keep incident-level details for safety-invariant breaches and aggregate only data that does not expose secrets or private content.

**Verification pattern**

For each operation, record:

1. the user's requested outcome and any explicit destructive authorization;
2. risk mode and the applicable invariant rows;
3. pre-action repository, worktree, branch, dirty-state, ownership, and relevant destination evidence;
4. current checks with their revision or tree scope and any pending or unavailable gate;
5. the exact action result, including partial success rather than only the final command;
6. post-action revision, destination, residual state, preserved unrelated work, and cleanup status;
7. exceptions, recovery action, next owner, and evidence that must be refreshed.

Independent before-and-after observations are stronger than reusing the action's own output. After a push, compare the intended revision with the destination ref or pull-request head when access permits. After a local merge, inspect the resulting history and run the checks required on the integrated tree. After cleanup, verify the exact worktree or branch target is gone and that no unintended target changed. After a keep, verify that the branch and worktree still contain the expected state.

**Contrastive outcomes**

- Good: a pull-request finish identifies the repository and worktree, reviews the scoped diff, runs current relevant checks, verifies remote and base, pushes the intended revision, confirms the pull-request head, preserves an unrelated file, labels remote checks pending, and leaves cleanup to an explicit later decision.
- Bad: `git push` exits successfully, so the operator reports completion without noticing it targeted another remote and then removes the only worktree containing an untracked file. Command reliability did not produce state, outcome, or evidence reliability.
- Borderline: an intentional commit preserves the requested changes and leaves unrelated state untouched, but the handoff calls the branch merge-ready although required integration tests were not run. State safety passed; evidence fidelity failed. Correct the label or run the gate before further transition.

When an invariant fails, stop compounding the state. Preserve logs and remaining local-only work, determine actual versus intended state, name the owner, and use the retry or recovery guidance. Do not relabel a breach as normal retry merely because a later command succeeded. Recurrent failures should change a script, hook, repository instruction, routing rule, or training example with an owner and verification fixture.

Known high-confidence requirements are preservation of unrelated state, exact destructive authorization, current action-relevant evidence, verified destination, and honest postconditions. Acceptable execution time, sample size, reviewer frequency, and alert thresholds remain local judgments. This separation keeps portable safety obligations firm without inventing production statistics that the local corpus does not establish.

## Failure Mode Table

Classify the failure before choosing a corrective command. A failed precondition that made no mutation, a partial remote transition, a wrong-target success, and destructive loss have different recovery contracts. The first response to an unexpected consequential result is:

1. stop further mutation, including automatic cleanup and broad retry loops;
2. capture the command, result, repository, worktree, branch or detached identity, current revision, index and working-tree state, and any active Git operation;
3. inventory local-only and unrelated work without resetting or deleting it;
4. query the relevant remote or platform destination when authorized, because an error response does not prove no server-side effect;
5. compare intended state with actual state and classify no mutation, complete mutation, partial mutation, wrong-target mutation, or unknown effect;
6. select the narrowest authorized retry, roll-forward, preservation checkpoint, compensation, recovery route, or escalation;
7. verify the corrective postcondition and report any remaining uncertainty.

Redact credentials and sensitive content from diagnostics. Preserve immutable identifiers and exact error meaning, but do not retain secrets merely to make a failure record complete.

| failure_mode | phase_and_trigger | observable_symptom_or_risk | immediate_containment | retry_or_recovery_gate | closure_evidence |
| --- | --- | --- | --- | --- | --- |
| wrong_repository_or_worktree | discovery or action runs from an unintended root, linked worktree, or nested repository | status and branch do not describe the requested task; a successful command may mutate another checkout | stop all writes, identify every affected repository and worktree, preserve their current state | ordinary retry is forbidden until impact and ownership are established; route to recovery if unintended mutation occurred | intended and actual targets are named, unintended effects are contained, and any correction has explicit authorization |
| detached_or_wrong_branch | branch identity was assumed from directory name or stale context | commit lands on detached history or another branch; target branch lacks the revision | retain commit ID and reflog evidence, avoid checkout/reset that can obscure reachability | attach or transfer the commit only after destination and ownership are confirmed | intended branch references the intended commit, no unrelated branch changed, and residual detached state is reported |
| mixed_or_unknown_staging | broad staging or concurrent edits include unowned paths or hunks | staged diff exceeds reviewed scope, unrelated changes appear in commit candidate | do not commit; unstage without discarding working content and classify each path or hunk | retry staging only with explicit path/hunk scope and refreshed diff | staged content exactly matches authorized scope and unrelated state remains visible |
| stale_verification | tests or checks ran before later tree, index, config, generated, merge, or policy changes | reported result does not cover the current claimed revision or integrated tree | withdraw the readiness claim and identify the invalidating mutation | rerun the applicable gate against the actual target state; checkpoint only if the user requests the narrower outcome | command, environment, covered revision/tree, and current result are recorded |
| required_check_failure | repository-defined check fails or cannot run before completion claim | feature may be unfinished, environment unavailable, or suite failure unrelated but unresolved | preserve work and failure output; do not weaken the claim silently | route to implementation or environment owner, or create an explicitly incomplete checkpoint if requested | check passes for the claimed state, or the handoff accurately names pending failure, consequence, and owner |
| save_hook_or_commit_failure | hook, signing, identity, storage, or commit command fails | working state may remain staged while no intended commit exists, or a hook may have modified files | inspect status, index, commit history, and hook-produced changes; do not assume no side effect | retry only after resolving the specific policy or environment cause and reviewing modified state | intended commit exists once with reviewed content; hook and residual state are reported |
| wrong_base_selection | base inferred from a common branch name or stale ancestry | local merge or pull request targets an unintended line of development | stop integration or publication; preserve branch and collect base-policy evidence | select a base only from current repository/user evidence; undo or retarget through authorized platform/recovery procedure | actual base is verified and resulting diff/history matches the intended review scope |
| wrong_remote_or_upstream | remote name, URL, fork, or tracking branch is assumed | revision publishes to an unintended repository or fails to reach the intended destination | stop further pushes and cleanup; capture remote mappings and actual destination refs | correction may require maintainer/platform action; do not delete or rewrite remote state without authority | intended destination contains the intended revision and unintended publication is resolved or explicitly owned |
| non_fast_forward_rejection | upstream advanced or branch relationship differs from expectation | local commit is durable but remote publication did not advance | preserve local commit, fetch read-only state as allowed, inspect divergence and policy | retry only after authorized merge/rebase/update strategy; force requires separate explicit authority | remote ref and local history match the chosen strategy, with refreshed checks where history or tree changed |
| transport_or_auth_failure | network, credentials, permission, or server availability interrupts publication | no reliable conclusion about destination mutation from the client error alone | retain local state and query destination when possible; avoid credential workarounds | bounded retry only for classified transient failure; access or policy failure routes to owner | destination state is known, one intended publication is present or absence is verified, and access issue has an owner |
| push_succeeds_pr_fails | branch is published but pull-request creation or lookup fails | work is durable remotely but requested review handoff may be absent, duplicated, or mis-targeted | do not repush or clean up; inspect existing pull requests and published revision | retry creation only after confirming no equivalent request exists and head/base are correct | one intended pull request references the published revision, or publication-only partial success is reported with next owner |
| local_merge_conflict | merge or related integration enters conflicted state | index contains conflict stages; prior tests no longer establish integrated readiness | stop finish flow, record active operation and conflict paths, preserve unrelated changes | route to conflict-resolution authority; do not choose content or abort without objective and ownership | operation is intentionally resolved or aborted, repository state is coherent, and required checks run on the resulting tree |
| local_merge_checks_fail | merge completes but required checks fail on integrated tree | branch history advanced while completion quality is false | retain merge evidence, do not clean source worktree or report success | follow repository policy for fix-forward, revert, or recovery; avoid ad hoc history rewrite | integrated branch reaches an intentional state with current checks and explicit source-branch disposition |
| cleanup_precondition_failure | branch/worktree is dirty, checked out, unmerged, unpushed, or contains local-only state | deletion command refuses, or a broad cleanup would lose recovery evidence | treat refusal as protection; inventory exact target and durability | clean up only after explicit intent, verified durable destination, no local-only state, and exact target recheck | intended target alone is removed and remaining branches/worktrees and user state are unchanged |
| discard_not_exactly_confirmed | silence, ambiguous wording, or stale confirmation is interpreted as permission to destroy | user work may be unrecoverable, particularly untracked content | do not discard; show what would disappear and request exact confirmation | proceed only against unchanged inventoried state and current authorization | specified state is removed, unrelated state remains, and recovery limits were disclosed accurately |
| destructive_action_partial | deletion, reset, or cleanup affects some targets before failing | repository is neither fully preserved nor in the intended cleaned state | stop, preserve remaining refs/files/logs, and avoid garbage collection or further deletion | route to repository recovery; compensation requires exact current-state evidence and authorization | recoverable work is secured, actual loss is stated, and repository/worktree invariants are restored or owned |
| concurrent_state_change | user, agent, hook, generator, or process mutates relevant state after inspection | diff, branch head, checks, remote, or cleanup target no longer matches evidence | stop and capture both observed versions without overwriting the newer state | reclassify ownership and workload; serialize writes or obtain coordination | refreshed evidence covers the current state and the authorized operation has one accountable writer |
| source_or_policy_drift | local instruction, source guidance, branch protection, or required check changed | prior decision or verification no longer applies, even if commands still work | preserve state and identify the changed authority or requirement | refresh only the consequential source and reevaluate dependent decisions | applied policy/version is named and incompatible stale guidance is no longer used |
| misleading_finish_report | action succeeds partially or evidence is absent, but handoff states complete, clean, tested, or ready | downstream owner may merge, release, or delete based on a false claim | correct the report promptly and preserve underlying evidence | rerun missing observations or downgrade to verified durable progress with pending gates | report distinguishes state safety, outcome fidelity, and evidence fidelity with next owner |

**Selecting a response**

- **Retry** only when the failure class is known, the operation is idempotent or actual destination state has been queried, required state has not changed, and policy allows another attempt. Apply the retry limits in the next section.
- **Roll forward** when a durable shared effect already exists and an authorized visible correction has less blast radius than rewriting or deleting that effect.
- **Restore or roll back** only when the inverse operation, current preconditions, ownership, and recovery durability are established. Git cannot guarantee recovery of every untracked deletion or expired object.
- **Checkpoint** when the user wants preservation but completion gates remain unavailable or failing. Record the narrower claim; do not call the checkpoint ready.
- **Compensate** when an external effect cannot be erased safely but a separate authorized action can restore the intended invariant. Keep both effects visible in the audit trail.
- **Wait** when remote CI, review, or platform availability is the only unresolved state and local durability is already verified. Name the owner, consequence, and follow-up.
- **Escalate** when identity, ownership, repository integrity, credentials, shared history, destructive loss, or production effects are uncertain.

**Contrastive failure handling**

A non-fast-forward rejection after a local commit is normally a no-remote-mutation publication failure: preserve the commit, inspect divergence and policy, and choose an authorized integration path. It is not automatic permission to force-push.

A timeout while creating a pull request is an unknown-effect platform failure: query for an existing request before retrying, because the server may have created it despite the client error. Repeating blindly can create duplicates or target a now-stale revision.

A worktree-removal refusal caused by dirty state is a safe protective failure: retain the worktree, inventory local-only files, and report why cleanup is blocked. Overriding it simply to complete the checklist converts a safe refusal into a possible destructive incident.

If unrelated work appears missing after cleanup, stop all repository maintenance. Preserve refs, reflog information, remaining files, and command evidence; avoid expiration, pruning, reset, or reclone operations that could remove recovery paths. Route to repository recovery and state honestly that restoration is uncertain, especially for untracked content.

**Verification and maintenance**

Exercise common rows in disposable repositories and remotes: wrong-directory detection, mixed staging, stale test invalidation, non-fast-forward rejection, conflicted merge, push-success/pull-request-failure, cleanup refusal, and concurrent state change. A useful fixture asserts pre-state, command effect, preserved unrelated state, retry gate, and postcondition. Never test destructive fixtures against user data.

Add a new failure row when it has a distinct cause, containment action, retry eligibility, or recovery owner. Do not create permanent rows for every wording variant of the same error. Merge duplicates, and promote recurrent modes into earlier precondition checks, repository automation, or policy with an owner and regression fixture. Retire a row only after the prevention mechanism is verified and the remaining generic route still preserves safety.

The target is not zero command failures. Safe refusals and clear blocks are valuable. The target is zero known compounding after an unexpected result, no unsupported recovery claim, and an intentional durable state or explicit specialist handoff at closure.

## Retry Backpressure Guidance

Retry is a new decision, not an automatic continuation of the failed command. Begin only after the failure mode is classified and the actual effect is known as no mutation, complete mutation, partial mutation, wrong-target mutation, or unknown. For a mutating action, the default is no automatic retry while effect, identity, ownership, idempotency, authorization, or destination remains uncertain.

Use this gate before every logical retry:

1. **Classify:** Name the failure row and whether the cause appears transient, stale observation, missing authority, policy denial, state conflict, permanent input error, or unknown.
2. **Requery:** Inspect actual local and remote state independently. A timeout or connection error does not prove that the server performed no action.
3. **Refresh:** Recheck mutable inputs: repository, worktree, branch, revision, index, dirty state, owner scope, base, upstream, remote, pull-request state, policy, checks, and user outcome as relevant.
4. **Authorize:** Confirm that repeating the operation is still within the request and repository policy. Failure never creates permission for force, cleanup, discard, credential bypass, or broader scope.
5. **Budget:** Apply the repository or platform retry policy. If none is established, use a conservative bounded attempt only for a classified harmless/transient case; do not invent a universal schedule.
6. **Attempt:** Perform one logical action, accounting for retries hidden inside wrappers or clients when their behavior is known.
7. **Verify:** Query the postcondition and stop when success, a changed precondition, an unknown effect, a permanent failure, or the logical budget is reached.

The budget belongs to the requested state transition, not independently to each nested command. A wrapper that retries three times and an outer loop that retries twice can otherwise produce six effects while both layers claim a small limit.

| operation_class | ordinary_retry_eligibility | required_pre_retry_observation | pacing_and_budget_source | hard_stop_condition |
| --- | --- | --- | --- | --- |
| deterministic local read | retry only when the failure is environmental or state changed deliberately; repeated identical syntax errors add no value | repository path, command availability, permissions, and whether relevant state changed | local tool policy; usually correct the cause rather than back off | same permanent input error, access denial, or evidence that the command targets the wrong repository |
| remote read or status query | bounded retry for classified transient transport, service availability, or eventual-consistency observation | endpoint/destination identity, authentication boundary, last known revision, response class | current platform or repository client policy, including rate-limit guidance when available | permission/policy denial, changing destination, exhausted budget, or query result no longer relevant to the same revision |
| local check or test | rerun after a deliberate code/config/environment change or a known flaky-test policy; not merely until green | current tree/revision, command scope, environment, prior failure, and change intended to affect it | repository test policy; flaky retry requires a named rule and retained initial failure | unexplained nondeterminism, unrelated failure, changed ownership, or repeated failure without a new hypothesis |
| local commit or hook | retry only after inspecting index, history, hook effects, identity/signing state, and resolving the specific cause | staged diff, current head, whether a commit exists, files modified by hooks, policy error | repository hook/signing policy; no blind outer loop | unknown hook mutation, unexpected commit, unowned staged content, or request no longer matches the index |
| push with explicit no-effect rejection | bounded retry after authorized divergence resolution or a verified transient pre-transfer failure | local commit, upstream/remote mapping, actual remote ref, rejection class, policy | Git host and repository policy; history strategy must be explicit | non-fast-forward without authorized integration strategy, protected-branch denial, wrong remote, or changed remote ref |
| push with ambiguous transport result | do not repeat until destination is queried | intended revision, actual remote ref if observable, client retry behavior, credential and network state | wait/requery policy before any write budget | inability to determine effect, destination mismatch, or any evidence of partial/wrong-target publication |
| pull-request create/update | retry only after searching for an existing equivalent operation and revalidating head, base, repository, title/body intent, and permissions | published head revision, selected base, existing requests, first response and request identity if available | platform idempotency and rate-limit policy when refreshed | duplicate or conflicting request, unknown first effect, changed head/base, or access/policy failure |
| asynchronous CI or review | prefer wait and observe; do not mutate merely to make a pending gate complete | check/review identity, revision covered, current status, expected owner | repository polling cadence or event-driven notification; respect service limits | check covers a stale revision, terminal failure, approval required, or wait exceeds owned handoff window |
| local merge or rebase | no ordinary retry after conflict or partial history change; classify active operation and route | current heads, active operation, conflict stages, unrelated state, intended base | conflict/recovery procedure, not a generic time backoff | unresolved content, ambiguous history objective, shared-history consequence, or policy requiring review |
| cleanup or branch/worktree removal | retry only after the protective refusal's cause is intentionally resolved and all destructive preconditions are reverified | exact target, current worktree list, dirty/local-only state, durable destination, authorization | explicit cleanup policy and current intent; no autonomous repetition | target changed, state remains dirty/unique, durability is uncertain, or any refusal has unknown effect |
| discard, reset, force, or destructive recovery | never automatically retry | complete current-state inventory, exact authorization, recovery evidence, specialist procedure | each attempt needs a fresh explicit decision under the applicable policy | any partial effect, ownership uncertainty, recovery uncertainty, target drift, or missing authority |

**Backpressure states**

- **Proceed:** The previous attempt had a known harmless effect or no effect, all consequential preconditions remain true, and a current policy authorizes another bounded attempt.
- **Observe:** The remote or asynchronous system may converge without a write. Wait or query at the policy cadence while preserving the local durable revision.
- **Checkpoint:** The work can be saved intentionally, but publication, integration, or readiness remains blocked. Report the checkpoint's narrower status.
- **Hold:** A mutable input changed or a required observation is unavailable. Stop new finish mutations until evidence is refreshed.
- **Escalate:** Identity, ownership, policy, integrity, shared history, destructive impact, or unknown server effect needs another owner.
- **Terminate:** The original outcome is no longer authorized, possible, or appropriate. Preserve the best known state and provide a terminal handoff rather than retrying indefinitely.

Backpressure also applies to scope. Do not start implementation, broaden staging, switch remotes, alter history strategy, remove worktrees, or add cleanup merely because the requested finish is blocked. Those are separate decisions and may erase evidence or expand authority. In a shared workspace, one owner should coordinate each mutating branch/worktree unit while independent agents may perform read-only analysis whose outputs are reconciled before action.

**Failure-specific examples**

- Safe read retry: a remote-status query receives a classified temporary transport error. Repository, endpoint, revision, and authorization are unchanged. Retry under current client policy, then mark the status observed or still unavailable. Do not infer publication readiness from a cached result.
- Ambiguous write: pull-request creation times out after the branch is already published. Query existing requests for the verified head and base. If the query is unavailable, retain the branch and report publication-only partial success rather than creating blindly.
- Permanent policy denial: a protected branch rejects a direct push. Repeating with new credentials or force is not backoff. Preserve the commit and route to the authorized pull-request or maintainer procedure.
- Hook mutation: a commit hook reformats files and then fails. Inspect the index and working tree, review ownership, rerun relevant checks, and decide whether another commit attempt is appropriate. Repeating immediately can compound modifications.
- Destructive refusal: worktree removal refuses because local changes exist. Treat this as a successful safety signal. Inventory and preserve the changes; do not add force flags or retry until exact cleanup intent and durability are established.
- Borderline persistence: a harmless remote read remains unavailable after the local policy budget. Continuing forever may not mutate state, but it monopolizes the workflow and delays a clear pending handoff. Escalate or stop with an owner and follow-up.

**Retry ledger**

For any consequential retry sequence, record:

| ledger_field | content |
| --- | --- |
| transition_identity | requested outcome, repository/worktree, branch, revision, and destination |
| failure_class | table row, client result, and classified actual effect |
| attempt_budget | governing repository/platform policy or conservative rationale when no numeric policy exists |
| hidden_attempts | known retries performed by client, wrapper, hook, or subprocess |
| refreshed_inputs | state and authority observations repeated since the prior attempt |
| change_since_failure | new evidence, corrected input, elapsed external condition, or approved recovery decision that justifies another attempt |
| attempt_result | exact local and remote effect, including partial or unknown state |
| stop_reason | verified success, changed state, permanent denial, unknown effect, exhausted budget, escalation, or terminated outcome |

Every attempt should add evidence or reduce uncertainty. If the same inputs are being applied to unchanged unknown state with no policy-backed stochastic rationale, stop. Truly transient systems may succeed without new information, but attempts still need harmless semantics, bounded pacing, and a current external policy.

Do not assert universal seconds, jitter, or attempt counts from this reference. Service behavior and rate limits can change, and no external platform documentation was refreshed during this evolution. Repository-owned tooling may encode stronger current guarantees; verify its version, idempotency, and failure behavior before relying on them.

Aggregate exhausted budgets, duplicate-effect preventions, changed-state stops, and hidden retry counts by operation class. Recurrent remote ambiguity may justify an idempotent wrapper or destination lookup. Recurrent hook mutation may justify clearer hook output and fixtures. Recurrent policy denial may indicate an incorrect default route. Process improvements should reduce uncertainty before retry, not merely increase the allowed attempt count.

## Observability Checklist

Observe the transition, not merely the commands. A useful record lets a reviewer reconstruct what the user requested, which repository state was inspected, what was authorized, what changed, where the work became durable, what remains, and which evidence is current. It should be concise enough to review and specific enough to falsify.

Use one transition identity to correlate the precondition, action, retry, failure, and postcondition records. The identity may be a repository-owned operation ID, an authorized journal entry, or a locally unique handoff key. It is not itself authorization and must not expose a secret.

**Core transition record**

| field | required_content | why_it_matters | privacy_or_freshness_boundary |
| --- | --- | --- | --- |
| requested_outcome | commit, push, pull request, local merge, keep, checkpoint, cleanup, confirmed discard, or explicit blocked handoff | anchors every action to user intent and prevents adjacent actions from being inferred | record the request meaning, not private conversation irrelevant to the operation |
| repository_identity | verified root and canonical non-secret repository identity where needed | detects wrong-directory, nested-repository, and wrong-destination errors | redact credentials embedded in URLs; do not copy access tokens |
| worktree_identity | current working directory, linked worktree path, branch or detached state | distinguishes multiple checkouts and the index being mutated | paths may be sensitive in shared reports; use approved shortening while retaining correlation |
| revision_before | current commit and active operation before mutation | establishes history baseline and supports recovery | refresh after checkout, commit, merge, rebase, reset, or concurrent update |
| dirty_and_conflict_state | staged, unstaged, untracked, conflict, and relevant submodule summary | exposes local-only state and ownership pressure | summarize paths and classes; avoid file contents unless specifically required and authorized |
| owned_scope | included paths/hunks, excluded unrelated state, unknown ownership blockers | proves broad staging or cleanup did not absorb another owner's work | ownership is a current judgment and must be refreshed after scope change |
| policy_and_source_basis | applicable repository instruction, user authorization, local source default, and any labeled inference | separates authority from advice and observed state | record only consequential sources; public pointers remain unrefreshed unless actually inspected |
| verification_evidence | exact command or review method, covered revision/tree, environment when material, result, and ordering before/after mutations | prevents stale tests and command-name-only claims | summarize output and retain bounded diagnostic pointer; do not dump secrets or full private logs |
| chosen_action | exact semantic operation and target, including whether cleanup is excluded | connects decision to mutation and makes partial success visible | command text may be omitted when it contains sensitive arguments; retain safe semantics |
| action_result | success, failure, partial, wrong-target, or unknown effect plus immutable identifiers | distinguishes process activity from actual state change | capture server object IDs or refs only where access policy permits |
| destination_state | resulting commit/ref, remote/upstream, pull-request head/base, merge target, kept worktree, or removed target | verifies durability and outcome fidelity | remote observations become stale after later publication or platform changes |
| residual_state | remaining tracked/untracked work, pending checks/review, retained branch/worktree, cleanup trigger, recovery limit | prevents "clean" or "done" from hiding unfinished or unrelated state | represent absent fields as inapplicable, unavailable, redacted, or blocked with reason |
| next_owner_and_stop | person, workflow, or event responsible for the pending action and condition for resumption or closure | turns uncertainty into an actionable handoff | avoid unnecessary personal data; use repository roles when sufficient |

For a read-only recommendation, record only fields needed to explain the decision. For every mutation, use the core record. Extend it by consequence:

| operation | additional_observability |
| --- | --- |
| scoped commit | staged diff identity, commit message intent, resulting commit ID, hook/signing result, and residual dirty state |
| push | verified upstream and remote identity, local revision, pre-push remote ref where relevant, push result, actual destination ref, and any policy rejection |
| pull request | published head revision, verified base, existing-request lookup after ambiguous failure, resulting request identity, remote checks/review state, and retained cleanup state |
| local merge | source and base identities, pre-merge state, active-operation outcome, resulting history, checks on integrated tree, and source branch/worktree disposition |
| keep or checkpoint | exact durable or local-only location, checks that did and did not run, why the narrower state is intentional, and trigger for later finishing |
| cleanup | exact branch/worktree target, verified durable destination, local-only inventory, authorization, removal result, and unaffected remaining worktrees |
| discard | inventoried content and consequence shown for confirmation, exact authorization, recovery limits, final target absence, and preserved unrelated state |
| retry or recovery | failure class, actual prior effect, logical attempt budget, hidden client attempts, refreshed inputs, selected correction, stop reason, and closure evidence |

**Evidence-state vocabulary**

Use an explicit state for every consequential field:

- `verified`: directly observed for the relevant repository state, revision, destination, and time ordering;
- `pending`: expected asynchronous evidence with consequence, owner, and follow-up;
- `not_observed`: unavailable or not run, with the effect on the requested claim;
- `not_applicable_with_reason`: excluded because the selected outcome does not require it;
- `blocked`: false or consequentially ambiguous, preventing the affected transition;
- `redacted_with_reference`: sensitive detail omitted from the summary but available through an authorized protected record, when policy permits.

Do not leave an important field blank. Blank can mean forgotten, unavailable, irrelevant, or intentionally hidden, and those states lead to different decisions.

**Event ordering**

At minimum, preserve this order:

1. observed intent and applicable policy;
2. repository/worktree identity and pre-action state;
3. ownership and selected workload mode;
4. current verification evidence;
5. authorized action and target;
6. command or platform result, including ambiguous and partial effects;
7. independently observed postcondition;
8. remaining state, pending evidence, cleanup status, and next owner.

Wall-clock timestamps help correlate concurrent activity, but ordering relative to mutation is the essential fact. A test result gathered before a later merge or generated-file update cannot verify the resulting tree even if its timestamp is recent. Record the revision/tree and invalidating event, not time alone.

**Redaction and evidence size**

Never place credentials, access tokens, private keys, signing material, secret environment values, credential-bearing URLs, or unnecessary file contents in a finish record. Treat command output and diffs as potentially sensitive. Preserve canonical non-secret destination identity or an approved opaque reference so wrong-target diagnosis remains possible.

Prefer:

- status and diff summaries with reviewed path lists over complete source dumps;
- exact command name, scope, result, and a protected diagnostic pointer over unbounded terminal transcripts;
- immutable commit or platform identifiers over screenshots that omit machine-readable identity;
- concise failure meaning and retained raw evidence location over repeated copies of the same logs;
- explicit unresolved-risk notes over a generic successful/clean label.

Raw evidence may be captured first during severe containment when summarization would risk loss, but move it promptly into authorized storage and create the structured record after state is stable. Storage location, access, retention, and deletion follow current repository and organizational policy. This reference does not invent a universal retention period.

**Compact example**

| record_item | example_value |
| --- | --- |
| outcome | create a pull request; cleanup not requested |
| identity | verified repository and linked feature worktree; feature branch at commit `abc1234` |
| scope | three owned source/test paths; one unrelated untracked note explicitly excluded |
| checks | repository unit and lint commands passed on tree `abc1234`; remote CI pending |
| destination | verified fork remote and intended base; remote head observed at `abc1234` |
| action_result | push verified; one pull request created for the expected head/base |
| preservation | unrelated note still present; branch and worktree retained |
| pending | remote CI and review owned by pull-request workflow; no merge or release claim |
| next_step | review the request; reassess cleanup only after durable integration and explicit intent |

Bad observability is a raw transcript containing a credential and pages of successful output but no requested outcome, branch revision, or destination postcondition. Borderline observability lists `git status`, tests, and `git push` with zero exit codes yet never records which remote ref advanced or whether unrelated state remained. Activity is not the same as an observed transition.

**Verification of the checklist**

Validate that each operation type supplies its required fields, that before/after records share one transition identity, and that evidence states are explicit. Use synthetic secret fixtures to test redaction. In disposable repositories, exercise complete, partial, ambiguous, and blocked transitions and ask an independent reviewer to identify:

- the intended outcome and authority;
- the exact state and destination affected;
- evidence supporting the completion claim;
- unrelated state that remained preserved;
- any pending or unavailable gate and its consequence;
- the next owner and safe recovery or retry boundary.

If the reviewer cannot reconstruct those facts, the record is incomplete even if it matches a schema. If measuring reviewer time or workflow latency would improve a real process, first define the operation population, start and stop events, sampling method, and owner. Do not demand p50, p95, or p99 merely because the seed named them; no local timing distribution supports universal thresholds here.

Keep the semantic core stable and allow repository-specific namespaced extensions for submodules, large-file storage, protected environments, release gates, or regulated approvals. Version schema changes, supply migration or compatibility notes, and maintain redaction fixtures. Tools should emit revision, destination, and postcondition fields directly where feasible; parsing them later from prose is less reliable.

## Performance Verification Method

Measure performance only to answer a named workflow decision, such as whether a destination-verification helper reduces rework, whether a structured handoff shortens reviewer reconstruction, or whether a repository wrapper improves end-to-end finish time without weakening checks. This reference contains no benchmark dataset and makes no universal latency or productivity claim.

Correctness is the constraint, not a metric to average against speed. Every evaluated run must still satisfy applicable state-safety, outcome-fidelity, and evidence-fidelity invariants. An unauthorized action, unrelated-state loss, wrong destination, stale readiness claim, or unverifiable postcondition invalidates the performance win for that run and is reported separately as an incident.

**Define the transition boundary**

Use an end-to-end boundary that represents user value:

- **Start:** the actionable request and required repository context are available to the operator or workflow.
- **Stop-success:** the selected outcome has a verified durable postcondition and a concise handoff with residual state and next owner.
- **Stop-blocked:** the workflow has preserved state and produced an explicit blocker, consequence, owner, and safe resumption condition.
- **Stop-failure:** an invariant is breached, the outcome is wrong or unknown, or recovery ownership is required.

Do not stop the timer at the last Git command if destination verification and handoff remain. Do not start before the request exists simply to include unrelated queueing. Record both active handling time and external waiting time when asynchronous CI, review, network recovery, or human authorization materially affects the result.

**Choose an evaluation mode**

| evaluation_mode | best_use | strengths | limits_and_safety_boundary |
| --- | --- | --- | --- |
| disposable fixture | command mechanics, state detection, staging, retries, cleanup refusal, and postcondition checks | repeatable inputs, controlled faults, no user-data risk, easy before/after comparison | may not represent large repositories, real permissions, network behavior, or human review |
| shadow decision review | compare route, gate, and stop decisions without allowing the candidate workflow to mutate state | tests decision clarity and reviewer agreement against real cases with low operational risk | cannot measure actual command execution or side effects; needs an independent rubric |
| observational cohort | evaluate real end-to-end operations before/after or across versions | captures platform, policy, reviewer, and repository variability | confounding, privacy, changing workload mix, and survivorship require explicit treatment |
| repository-owned controlled rollout | assess a mature wrapper or policy change under current governance | combines realistic conditions with staged exposure and rollback ownership | inappropriate without authorization, monitoring, and a safe fallback; never experiment casually with destructive paths |
| expert walkthrough | rare, high-consequence, or insufficiently sampled operations | reveals missing decisions, recovery ambiguity, and cognitive load without unsafe live repetition | supports qualitative findings rather than stable latency distributions |

Use fixtures for destructive behavior and injected faults. Do not benchmark cleanup, discard, reset, or force behavior against user repositories. Use shadow or expert review when a candidate changes authority, routing, or destructive decisions. A live randomized comparison is not justified merely because it would produce stronger statistics.

**Measurement packet**

| measurement_field | required_definition |
| --- | --- |
| hypothesis | specific mechanism and expected outcome, such as "verified remote lookup reduces wrong-destination rework" |
| decision_owner | person or repository role authorized to act on the result |
| variant_identity | exact reference, script, tool, configuration, and version under comparison |
| operation_population | included outcomes, repositories, and time window or fixture set |
| workload_dimensions | compact/full/sequenced mode, diff reviewability, ownership, checks, destinations, concurrency, generated/submodule state, and consequence |
| start_and_stop_events | machine- or reviewer-observable events for success, blocked, and failure outcomes |
| invariant_results | state safety, outcome fidelity, evidence fidelity, and every breach retained as an incident |
| active_and_wait_time | operator/tool handling separated from CI, review, rate-limit, network, or authorization wait where feasible |
| attempts_and_rework | logical retries including hidden client attempts, repeated discovery, corrected staging, reruns, recovery, and reviewer clarification |
| exclusions_and_censoring | every omitted, abandoned, timed-out, inaccessible, or incomplete operation with reason |
| environment | repository/tool version, host conditions, cache state, network locality, and policy/check changes that can affect comparison |
| analysis_method | descriptive summary, paired comparison, distribution, or other method justified by the sample and design |
| uncertainty | sampling limits, confounding, missing evidence, and scope beyond which the result must not be generalized |
| retention_and_privacy | approved data location, redaction, access, and lifecycle under current policy |

Changed-file count, source count, and tool-call count are context descriptors, not default performance outcomes. A large generated diff may be easy to verify; fewer tool calls may simply omit required checks; more source reads may prevent a costly wrong-base action. Use a proxy only after explaining its causal relation to the named decision.

**Candidate outcomes**

| outcome | interpretation |
| --- | --- |
| verified_transition_elapsed | start to verified success or explicit blocked handoff; report outcome type rather than pooling them silently |
| active_handling_time | time spent inspecting, deciding, executing, verifying, and reporting, excluding separately identified external waits |
| reviewer_reconstruction_time | time for an independent reviewer to identify request, target, evidence, actual result, residual state, and next action |
| clarification_count | additional consequential questions required because initial guidance or handoff omitted intent, ownership, destination, or evidence |
| logical_retry_count | retries for the transition across wrappers and clients, segmented by failure class |
| rework_and_recovery | repeated staging, rerun checks after avoidable invalidation, wrong-target correction, duplicate-object cleanup, or incident recovery |
| blocked_handoff_quality | whether the stop preserved state and named consequence, owner, and resumption condition |
| invariant_incidents | absolute count and details of safety, outcome, or evidence breaches; never hidden in an average |

Report distributions only when the population and sample support them. A median can describe a modest sample; p95 or p99 require enough representative observations and a defined handling of ties, censored runs, and workload changes. The seed's request for p50/p95/p99 does not create evidence for those percentiles. When data is sparse, report individual cases, range, and uncertainty instead of false precision.

**Control and segmentation**

Compare like with like. Segment at least by outcome and workload mode, then by factors that materially affect the hypothesis: repository size and shape, generated files, submodules, check suite, cache warmth, network, host, remote provider, permissions, CI queue, review wait, concurrency, and policy changes. Paired disposable fixtures or alternating variants can reduce drift. Operational before/after studies must note that repository mix and team behavior may have changed.

Include blocked, failed, abandoned, and recovered runs. Excluding them can make a brittle workflow appear fast. Distinguish terminal policy denial from transient network delay; distinguish user wait from tool handling; distinguish a safe early stop from inability to finish. Report missing data and why it is missing.

**Examples**

- Valid: on the same set of disposable pull-request fixtures, compare the existing process with a helper that emits verified remote, head, base, and destination postconditions. Inject no-effect rejection and ambiguous create responses. Measure active handling, logical attempts, wrong-destination prevention, and reviewer reconstruction. Require all invariants in both variants.
- Invalid: claim a faster finish because the new path executes fewer commands after removing integration tests and destination verification. The apparent gain is an unsupported readiness shortcut.
- Borderline: report a lower median for successful operations while omitting blocked and failed cases. Reanalyze the full cohort and segment outcomes before drawing a conclusion.
- Nuanced: a workflow has a slower median but eliminates rare, expensive cleanup recovery. Report both the central distribution and incident/recovery tail; do not collapse irreversible consequence into one average cost.

**Pass and fail rules**

A performance claim passes when the measurement packet is complete enough to reproduce the cohort and boundaries, the named outcome improves under the stated analysis, no applicable invariant regresses, failures and missing runs are accounted for, and uncertainty does not exceed the claim. A documentation change also must let a reviewer identify the correct next action, verification gate, stop condition, and recovery owner without reading unrelated material.

A claim fails when it relies on tool-call count alone, mixes incompatible outcomes, reports unsupported percentiles, excludes inconvenient failures, changes verification coverage, uses stale or incomparable state, or treats speed as compensation for an authorization or preservation breach. A null or uncertain result is not a process failure; it means the evidence does not support rollout on performance grounds.

Persist the packet with the result and the exact tool/reference version. Reevaluate after material changes to repository topology, platform behavior, policy, checks, wrapper implementation, or workload mix. Performance instrumentation may reveal architecture, ownership, or platform friction; route those findings to the responsible system rather than granting the finish workflow broader authority.

## Scale Boundary Statement

This reference is sufficient for one coherent branch/worktree state transition: one accountable mutation owner, one reviewable ownership scope, one requested outcome, and a postcondition that can be verified from current local and destination state. It can also sequence several such units when each remains independently durable and partial results are visible.

It stops being the controlling procedure when the required outcome depends on atomic cross-repository publication, coordinated schema or data migration, multi-environment release, shared-history rewrite across owners, production rollout, platform administration, repository-integrity recovery, or conflict resolution whose content ownership is unresolved. It may still prepare or preserve individual branches, but an authoritative orchestrator or specialist procedure must own global ordering, approvals, partial-failure handling, and closure.

Scale is not a changed-file threshold. Evaluate the count of independently mutable truths:

- repository roots and indexes;
- branches, worktrees, and active Git operations;
- change owners and review authorities;
- bases, upstreams, remotes, remote refs, and pull-request destinations;
- verification environments and approval domains;
- cleanup or destructive targets;
- concurrent writers and long-running contexts;
- outcomes that can succeed or fail independently;
- recovery owners and externally visible effects.

A large reproducible generated change may remain one unit. Two small changes with different owners and destinations may require coordination.

**Scale modes**

| scale_mode | entry_condition | mutation_ownership | verification_and_closure | boundary |
| --- | --- | --- | --- | --- |
| single_unit | one repository/worktree unit, owned scope, one outcome and destination | one accountable writer for the relevant index, branch, and target | this reference verifies preconditions, action, postcondition, and handoff | default mode |
| sequenced_units | several units can be durable and reviewed independently but share ordering or later integration | one writer per unit; a coordinator controls sequence and shared target mutation | each unit closes independently, then shared integration receives refreshed checks | use when visible partial progress is acceptable |
| independent_parallel_units | repositories/worktrees, destinations, and outcomes truly do not share mutable resources or ordering | one owner for each isolated unit; no worker assumes another unit's state | per-unit evidence and postconditions remain separate; global report aggregates without overwriting | stop parallelism if a shared dependency or destination appears |
| merge_queue_or_serialized_integration | many source units target one shared base under repository-owned queue semantics | workers prepare source revisions; queue or designated integrator alone mutates shared base | source checks plus queue/integrated-tree checks; resulting order and failures are observable | verify current queue policy and do not infer release completion |
| explicit_orchestration | cross-repository, cross-package, migration, release, or platform workflow has a current runbook | orchestrator assigns leases/owners and controls shared mutations | per-unit durable outputs plus global approvals, ordering, rollback/roll-forward, and final outcome evidence | this reference becomes a subordinate branch-state procedure |
| blocked_unowned_scale | shared resources, atomicity, authority, or recovery cannot be established | no speculative writer | preserve every unit, publish a dependency and risk inventory, and request an owner | do not improvise coordination by force or broad access |

**Coordination invariants**

1. One accountable mutation owner controls each shared index, branch, worktree, remote ref, pull-request target, and cleanup target at a time, unless an authoritative tool supplies stronger concurrency semantics.
2. Read-only discovery may run in parallel, but its result carries the observed state identity. Refresh it before action if another unit can mutate that state.
3. Ownership transfers only at a durable checkpoint that names immutable revision where available, dirty/local-only state, checks, pending risks, destination, and next authorized action.
4. Shared target writes compare the current state with the state on which the decision was based. A mismatch fails closed and returns to classification; it does not authorize force.
5. No worker cleans a branch or worktree while another unit, reviewer, queue, recovery process, or orchestrator depends on its local-only state or diagnostics.
6. A source-unit success does not prove integrated, release, or production success. Each global layer verifies its own resulting state.
7. Partial success remains visible. Do not delete or rewrite durable shared effects merely to make the aggregate look atomic unless the orchestrator's recovery policy explicitly authorizes that action.

Filesystem separation alone is not sufficient. Separate worktrees protect working directories and indexes, but workers can still race on the same remote ref, choose inconsistent bases, duplicate pull requests, or delete a worktree another workflow needs. Conversely, one human may own several units safely when mutations are sequenced and every handoff remains current.

**Scale handoff contract**

When this reference routes to sequencing or orchestration, transfer:

| handoff_field | required_content |
| --- | --- |
| global_outcome | exact user or policy objective and what this branch-level procedure is and is not authorized to do |
| unit_inventory | repository, worktree, branch, immutable revision, owner, dirty/local-only state, and requested unit outcome |
| dependency_order | compatibility, migration, generation, integration, or release dependencies with reasons |
| shared_resources | bases, remote refs, pull-request targets, environments, credentials/permissions, and cleanup targets requiring serialization |
| current_evidence | per-unit checks, review state, source/policy basis, and observations invalidated by later units |
| coordination_control | writer owner, lock/lease or merge-queue mechanism, expiry/recovery owner, and state-version comparison |
| partial_failure_contract | which unit effects can remain, how they are reported, authorized roll-forward/compensation, and terminal escalation |
| global_closure | integrated revision or release identity, checks/approvals on resulting state, residual units, cleanup status, and next owner |

Locks and leases are not self-justifying. They need a current owner, protected identity, acquisition and release evidence, expiry semantics, and a recovery procedure. Age alone does not prove abandonment. If no coordination mechanism exists, serialize mutation through explicit human or workflow handoff.

**Long-running context**

A long-running worker can conflict with its own earlier assumptions. Checkpoint after each durable unit and before a consequential mutation. The checkpoint should preserve current repository/worktree identities, immutable revisions, dirty and ownership state, evidence freshness, selected outcome, open risks, retry budget, and next step. On resume, reread current policy and requery mutable state; do not assume that a remembered branch head, remote, pull request, or check remains current.

Treat context drift as an evidence invalidation, not automatically as an incident. It becomes a reliability failure when stale context drives a mutation or unsupported claim. Persistent summaries reduce reconstruction cost, but live Git and platform state remain authoritative for what exists now.

**Large repository and monorepo handling**

Narrow discovery around the owned behavior and its required checks, generated outputs, dependencies, and reviewers. Dependency graphs, ownership metadata, pathspecs, and diff statistics can reduce search, but each is a signal rather than proof. A ranked source list does not establish current change ownership or finish readiness. If package boundaries have independent checks or owners, model them as sequenced units unless repository policy declares an atomic contract.

Submodules and nested repositories are separate repository identities even when one pointer change appears in a parent diff. Sparse checkouts can hide tracked paths. Large-file systems can separate pointer durability from object availability. An orchestrated finish must state which layer owns each verification and destination.

**Examples**

- Good parallel preparation: two independent features use separate worktrees and branches with separate owners. Each produces a reviewed immutable revision and check record. A repository merge queue alone updates the shared base and reruns integrated checks. Source workers do not clean their worktrees until queue durability and policy permit it.
- Bad distributed finish: three agents stage and commit in one worktree, each trusting an earlier status snapshot, then all push and run cleanup. No owner can establish which diff, tests, or deletion belonged to which request.
- Borderline isolation: workers use separate worktrees but push different revisions to the same remote branch. Local filesystem isolation succeeded, but shared destination ownership did not. Add serialization or separate destination refs.
- Coordinated cross-repository change: a client and service require compatible revisions and a migration sequence. Preserve and verify each branch under this reference, then hand immutable revisions and dependency order to the release/migration orchestrator. Do not simulate cross-repository atomicity with ad hoc resets.

**Verification**

In disposable repositories and remotes, exercise two-writer state-version mismatches, merge-queue reorder, cancellation, owner transfer, stale checkpoint resume, cleanup while another unit depends on a worktree, and partial remote success. Assert that conflicting mutation fails closed, every durable revision remains discoverable, unrelated state survives, and the global record identifies partial outcomes.

Operationally, review unit ownership, worktree/ref inventory, state versions immediately before writes, orchestrator or queue events, per-unit postconditions, and global closure. Logs alone cannot prove no uninstrumented writer exists; repositories needing stronger guarantees should enforce permissions, protected refs, queue ownership, or hooks through current policy.

No external merge-queue, lease, or atomicity guarantee was refreshed for this evolution. Technology choice, throughput limit, timeout, and recovery mechanism remain local decisions. The portable rule is narrower: partition by authority and postcondition, use immutable revisions for handoff, give each shared target one accountable writer, persist context at durable boundaries, and verify the globally resulting state before cleanup or stronger completion claims.

## Future Refresh Search Queries

No query in this section was executed during this evolution. The task explicitly prohibited browsing. The three public pointers in the source maps remain unrefreshed, and the query strings below are plans rather than citations or evidence.

Refresh only when a named uncertainty can change an operation. Start with the user's request, live repository state, current repository instructions, installed tool/version information, and semantic diffs of the five local source paths. Public documentation can explain Git or hosting semantics; it cannot establish local change ownership, selected remote, configured protection, required checks, or cleanup authorization.

Use this retrieval sequence:

1. State the claim or decision that may be stale and the consequence of getting it wrong.
2. Inspect current local policy, tool version/help, source hashes, and observed repository/platform state where authorized.
3. Query the primary upstream manual or official hosting documentation with product and feature terms, not a broad "best practices" phrase.
4. Open the supporting page, verify version/product/configuration applicability, and record access date and revision where available. Search snippets are not evidence.
5. If documentation remains ambiguous, reproduce only in a disposable repository, worktree, or remote under the matching installed version and safe configuration.
6. Classify the result as unchanged, clarified, contradicted, superseded, or unresolved; name every section and fixture affected.
7. Stop when one authoritative applicable answer plus local state resolves the decision. Do not collect redundant sources merely to increase source count.

**Unexecuted query registry**

| query_label | refresh_trigger_and_decision | local_first_check | exact_future_query | preferred_authority | acceptance_and_stop_rule |
| --- | --- | --- | --- | --- | --- |
| `local_finish_source_drift` | a local finish skill hash or text changes; decide whether direct-request, option, save, or cleanup guidance changed | hash and semantic diff archived Claude, current Claude, and later Codex finish sources | `finishing a development branch skill commit push pull request worktree cleanup direct request source history` | current repository files and their revision history | accept only reviewed semantic changes; duplicate paths with identical bytes remain one lineage |
| `local_worktree_source_drift` | current worktree skill changes; decide whether location, ignore, setup, baseline-test, or cleanup assumptions changed | compare archived/current worktree hashes and read changed sections completely | `using git worktrees skill directory selection gitignore baseline tests cleanup source history` | current repository files and their revision history | stop after changed claims and affected reference sections are mapped |
| `git_worktree_remove_semantics` | installed Git version changes, cleanup refusal differs, or recovery incident contradicts guidance | record `git --version`, installed help, worktree list, and disposable dirty-worktree behavior if permitted | `site:git-scm.com/docs git-worktree remove force dirty locked prune repair version` | official Git manual matching installed release | accept documented semantics for that version; keep user intent and repository policy as separate authorization |
| `git_worktree_lock_prune_repair` | stale metadata, moved repository, or locked worktree affects cleanup/recovery | inspect current worktree metadata and installed help without mutating user state | `site:git-scm.com/docs git-worktree lock unlock prune repair move repository` | official Git manual and release notes | route damaged state to recovery; do not turn maintenance capability into automatic cleanup permission |
| `git_status_machine_format` | automation depends on status parsing across submodules, renames, or unusual paths | inspect installed help and existing repository scripts/tests | `site:git-scm.com/docs git-status porcelain v2 untracked submodule rename format stability` | official Git manual | accept only a documented stable format and validate parser fixtures against installed version |
| `git_push_rejection_and_force` | non-fast-forward or lease behavior affects a proposed recovery | inspect upstream, remote refs, repository policy, and installed push help | `site:git-scm.com/docs git-push non-fast-forward force-with-lease expected value safety` | official Git manual matching installed release | stop when ordinary integration route is clear; force still requires separate current authorization |
| `git_reflog_recovery_limits` | local commit appears unreachable or recovery guidance is invoked | preserve refs/reflog/object state and avoid pruning while recovery owns the task | `site:git-scm.com/docs git-reflog expire recover unreachable commit untracked files limitations` | official Git manuals for reflog, reset, restore, and maintenance | record exact recoverable object class; never imply reflog restores arbitrary untracked content |
| `github_pull_request_create_effect` | pull-request create/update returns timeout or unknown effect; decide whether retry can duplicate an object | query authorized repository state for existing head/base request before any repeat | `site:docs.github.com REST GraphQL pull request create head base duplicate idempotency retry timeout` | current official GitHub REST/GraphQL and pull-request docs | accept only behavior applicable to used API/tool; if effect remains unknown, preserve publication and stop blind retry |
| `github_head_base_and_forks` | cross-fork publication or base selection differs from examples | inspect configured remotes, repository ownership, existing pull-request state, and local policy | `site:docs.github.com pull request head repository fork base branch create permissions` | official GitHub pull-request documentation | documentation explains capability; live authorized state must establish actual repository and permissions |
| `github_branch_protection_rules` | direct push, merge, or cleanup depends on required reviews, checks, or rulesets | inspect current repository policy and authorized platform configuration | `site:docs.github.com repositories rulesets protected branches required status checks merge queue current` | official GitHub repository/ruleset documentation | do not infer enabled controls from docs; accept only live configuration or maintainer evidence for this repository |
| `github_actions_check_scope` | a readiness claim depends on Actions workflow, reusable workflow, event, or revision coverage | inspect repository workflow files, required-check policy, run revision, and current result | `site:docs.github.com actions workflow run event commit SHA reusable workflow required check status` | official GitHub Actions documentation, including the preserved reusable-workflow pointer | map documented semantics to the actual workflow and revision; local tests remain distinct from remote CI |
| `github_api_rate_retry_policy` | remote reads or writes are rate limited or a wrapper needs retry pacing | inspect client behavior, response headers, current repository tooling, and hidden retry settings | `site:docs.github.com REST API rate limits retry-after secondary rate limit best practices idempotent requests` | current official GitHub API documentation | adopt numeric pacing only with current source and tool applicability; expire it on API/client change |
| `codex_repository_instruction_example` | the preserved Codex repository pointer is needed as an example or authority claim | validate the exact local or remote path and revision before reading | `site:github.com/openai/codex AGENTS.md testing instructions branch workflow revision` | the repository file at a verified revision, then its history if relevant | use as an example only; it does not govern another repository and the seed URL alone proves no content |
| `git_release_semantic_change` | a Git upgrade changes worktree, push, status, or recovery behavior used here | compare installed version, release notes, and affected disposable fixtures | `site:git-scm.com/docs RelNotes git worktree push status reflog behavior change` | official Git release notes and updated manuals | refresh only affected claims and rerun their fixtures; do not rewrite unrelated guidance |
| `github_release_semantic_change` | GitHub changelog announces ruleset, pull-request, Actions, or API behavior changes | inspect repository usage and current feature configuration | `site:github.blog/changelog pull request rulesets Actions API breaking change retry` | official GitHub changelog followed by product documentation | a changelog is a trigger; current product docs and live configuration establish applicability |

Query text may need product-version or date terms when the installed tool or platform release is known. Do not include private repository names, confidential branch names, ticket content, or sensitive paths in public queries without authorization.

**Refresh result record**

| result_field | content |
| --- | --- |
| trigger | local hash drift, tool upgrade, policy change, contradictory incident, moved official page, failed fixture, or named unresolved decision |
| claim_at_risk | exact current recommendation and consequence if stale |
| local_state | repository policy, installed version, source hashes, relevant live configuration, and safe direct observation |
| query_and_source | exact query, opened primary URL, access date, document/product version, and revision where available |
| finding | concise paraphrase with applicability and any conflicting evidence |
| verification | disposable fixture or live read-only state check, including version and limitations |
| disposition | unchanged, clarified, contradicted, superseded, or unresolved |
| affected_artifacts | reference sections, scripts, hooks, prompts, tests, metrics, and recovery guidance requiring review |
| next_invalidation | source hash, version, policy, incident, URL, or fixture event that should trigger another refresh |

A good refresh asks a bounded question such as whether the installed Git version refuses ordinary removal of a dirty worktree, reads the matching official manual, and uses a disposable fixture only if interpretation remains unclear. The finding can explain semantics; it still cannot authorize removing the user's worktree.

A bad refresh searches "best Git workflow," copies a secondary summary, and turns an example command into universal policy. A borderline refresh reads current GitHub branch-protection documentation and then assumes the target repository has those controls enabled. Documentation establishes possible behavior; authorized live configuration establishes actual behavior.

Preserve prior evidence and conflicts when refreshing. The older local finish source's inconsistent pull-request cleanup guidance remains useful provenance even if a later source clarifies a preferred default. A moved page or hash change is a trigger for semantic review, not proof that behavior changed. A no-change result is legitimate evidence when recorded with scope and date.

Apply the most rigorous refresh discipline to destructive operations, history changes, remote destination behavior, branch protection, CI coverage, recovery guarantees, and platform retry/idempotency. Low-consequence explanatory wording may use a lighter review. Event-driven refresh is preferred to periodic broad search because it targets facts capable of changing the next safe action.

## Evidence Boundary Notes

Evidence and authority are related but not interchangeable. A Git manual can establish mechanics but cannot authorize cleanup. Live status can establish that a file exists but not who owns it. A user can choose an outcome but cannot make a policy-prohibited or technically unsafe transition complete without resolving the constraint. Read each consequential recommendation through the distinct classes below.

| evidence_or_authority_class | what_it_establishes | permitted_use | prohibited_inference | refresh_or_verification_trigger |
| --- | --- | --- | --- | --- |
| `user_authorization` | requested outcome and explicit consent for a named consequence | choose commit, push, pull request, keep, checkpoint, local integration, cleanup, or confirmed discard path within policy | silence authorizes destruction; a push request implies merge, release, cleanup, force, or unrelated staging | material scope/consequence change, stale destructive confirmation, or new policy/state conflict |
| `repository_policy` | current local requirements for branches, remotes, checks, protection, ownership, cleanup, release, and tooling | constrain or specify the operation and route exceptions to named owners | every nearby document is policy; generic source guidance overrides current repository rules | instruction revision, configured-policy change, maintainer clarification, or observed contradiction |
| `observed_repository_state` | what the inspected repository, worktree, branch, index, diff, refs, remotes, checks, and destination show at that point | prove preconditions and postconditions for the actual operation | observation grants authorization; a prior snapshot remains current after mutation or concurrent work | any relevant tree, index, ref, remote, policy, check, or platform change |
| `local_corpus_sourced_fact` | what one of the five completely read local source paths actually says | identify workflow lineage, procedures, defaults, examples, and internal conflict | source text is universally correct, independent corroboration, current repository policy, or live state | source hash/text change, superseding local authority, failed fixture, or consequential incident |
| `duplicate_local_alias` | an archived/current path exposes byte-identical content at capture time | improve discoverability and document lineage | each alias is an independent supporting source or hash equality proves future identity | either path hash changes or active/archive role changes |
| `external_research_sourced_fact` | a claim directly supported by an inspected applicable external primary source | reserved for future refreshed Git or hosting mechanics with URL, access date, version, and scope | a URL listed but unopened supplies evidence | primary page is actually opened and applicability recorded; none qualified in this evolution |
| `unrefreshed_external_pointer` | a public URL or future query may be relevant later | mark a refresh route and the question it could answer | current content, correctness, availability, revision, or applicability | a consequential unresolved claim permits browsing and follows the refresh protocol |
| `combined_evidence_inference_note` | reasoned synthesis across available local facts, observed constraints, and clearly bounded general systems reasoning | select a conservative operational default, explain causal implications, and name exceptions | the synthesis is quoted policy, measured performance, or refreshed public fact | source conflict changes, live counterexample, policy update, or failed operational fixture |
| `normative_safety_default` | least-destructive reversible behavior selected when authority or evidence is incomplete | preserve work, stop mutation, request clarification, separate publication from cleanup, and fail closed on consequential uncertainty | every repository mandates the default or the default can override an explicit safe policy/request | current policy and intent provide a safer applicable alternative with verified preconditions |
| `repository_specific_judgment` | a decision applying current local policy, state, ownership, risk, and tooling to one operation | choose exact base, remote, checks, split, retry, cleanup, and handoff under recorded evidence | portable guidance proves the local judgment without inspection | any input to the judgment changes before mutation or postcondition |
| `unresolved_uncertainty` | an evidence, authority, identity, or recovery gap remains consequential | block the affected action, preserve state, and name the owner or refresh route | unknown means probably safe or can be resolved by a broader command | missing evidence arrives, state changes, or specialist owner accepts the handoff |

Use the least authoritative label that accurately describes support. When several classes contribute, retain their separate roles. For example, current policy may require a particular test, observed state may show it passed on a revision, and user authorization may request publication. Calling all three "evidence" without role loses which fact can require, establish, or authorize the action.

**Captured local evidence**

Five local paths were read completely:

- `agents-used-monthly-archive/claude-skills-202603/superpowers/finishing-a-development-branch/SKILL.md`
- `agents-used-monthly-archive/claude-skills-202603/superpowers/using-git-worktrees/SKILL.md`
- `agents-used-monthly-archive/codex-skills-202604/finishing-a-development-branch/SKILL.md`
- `claude-skills/superpowers/finishing-a-development-branch/SKILL.md`
- `claude-skills/superpowers/using-git-worktrees/SKILL.md`

The archived/current Claude finish pair is byte-identical at SHA-256 `dd2f82c6dc8582b621f9eb57fcb65f557f88eadf872727ac81d0840ae12c504e`. The archived/current Claude worktree pair is byte-identical at SHA-256 `de9dcde34840eee074047ec327d4ea6ca4954c5a73a6d874dc48f25fe46c9e7c`. The later Codex finish source has SHA-256 `9a0738cce13077cdc5c3299b4315fbdf3d8b1a597814a4a14e8f65ef5564126a`.

Therefore, four Claude paths represent two byte-identical artifacts, not four independent confirmations. With the Codex source, the local corpus provides three distinct texts through five paths. Hash equality establishes byte identity at capture time; it does not establish correctness, authority, future immutability, or applicability to a particular repository.

The Claude finish artifact directly supports test-first completion, base discovery, the four outcome options, explicit confirmation before discard, and worktree cleanup mechanics. It also contains an internal pull-request cleanup contradiction: its option flow reaches cleanup, while quick-reference and common-mistake guidance preserve the worktree for the pull-request path. The later Codex artifact directly supports honoring an explicit request without a redundant menu, saving intentionally, and providing a concise handoff. The worktree artifact directly supports directory selection, ignore checks, setup, baseline testing, and location reporting. These are statements about source content, not proof that every example command or default applies now.

The conservative default to preserve the branch and worktree after pull-request publication unless explicit intent or repository policy requests safe cleanup is a `combined_evidence_inference_note` plus `normative_safety_default`. It is not a quotation from one uncontested source. It follows from the visible conflict, the later source's intent emphasis, the separation of publication from cleanup, and the reversibility advantage of retaining state.

**External evidence status**

The source maps preserve three public pointers: GitHub Actions documentation, GitHub reusable-workflow documentation, and a Codex repository `AGENTS.md` URL from the seed. None was opened or refreshed because browsing was prohibited. Consequently, this evolved reference contains zero `external_research_sourced_fact` claims. The URLs and future search strings are `unrefreshed_external_pointer` entries only. They do not establish current CI semantics, repository instructions, platform behavior, or URL validity.

No numerical performance, reliability, scale, retry, or productivity result is claimed from those pointers or the local corpus. Numeric thresholds require a defined local policy or a measurement packet with population, method, environment, uncertainty, and owner. The invariant words "every" and "zero known" in safety tables are normative acceptance conditions, not observed production rates.

**Applied evidence decomposition**

Pull-request cleanup:

- Source fact: older local guidance conflicts internally; later local guidance emphasizes explicit intent and intentional handoff.
- Observed state needed: branch/worktree identity, dirty and local-only files, published revision, pull-request head/base, and durability.
- Authorization needed: explicit cleanup request or applicable repository policy.
- Synthesis: publication and cleanup are separate transitions.
- Safety default: retain the branch/worktree when cleanup intent or preconditions are absent.
- Verification: report retained or removed state and prove unrelated work remains.

Discard:

- Source fact: local finish guidance requires typed confirmation before discard.
- Observed state needed: exact tracked, staged, unstaged, untracked, conflict, branch, worktree, and durable-copy inventory.
- Authorization needed: current exact confirmation for the unchanged target and consequence.
- Mechanics: installed Git behavior and repository recovery constraints determine how an authorized action could be performed.
- Safety default: silence, ambiguity, or changed inventory blocks destruction.
- Uncertainty: reflog cannot be promised to restore arbitrary untracked content or expired objects.

Remote publication:

- User authorization chooses whether publication is wanted.
- Repository policy constrains remote, base, protection, checks, and review path.
- Observed state establishes branch revision, upstream, remote identity, and actual destination result.
- Local sources provide a procedure and handoff defaults.
- Unrefreshed public pointers cannot establish current GitHub configuration or retry/idempotency behavior.
- Postcondition evidence, not command success, establishes where the work became durable.

**Bad and borderline claims**

Bad: "GitHub best practice requires deleting the worktree after opening a pull request." No inspected external source, user intent, repository policy, or conflict reconciliation supports that statement.

Borderline: "The official Git manual permits this cleanup, so proceed." Mechanics can establish that a command exists or how it behaves; they cannot authorize deletion of local work or prove durability and ownership preconditions.

Good: "The pull request references the intended revision, the worktree contains no local-only task state, current repository policy requests removal after publication, and the user requested cleanup. Remove only the verified target and recheck remaining worktrees." Each verb is supported by its proper authority and observable evidence.

**Claim audit**

For every high-consequence recommendation, ask:

1. What exact claim is being made: can, should, must, observed, requested, inferred, or unknown?
2. Which source, policy, user request, state observation, or reasoning supports it?
3. Is the supporting artifact current, independent, applicable, and completely understood at the relevant passage?
4. Does a duplicate lineage or internal conflict reduce apparent corroboration?
5. Is public evidence actually inspected, or is the item only a pointer/query?
6. What repository-specific fact must still be observed before action?
7. What would falsify or invalidate the recommendation?
8. Which verification or postcondition demonstrates the action matched its claim?
9. What uncertainty remains, and does it block this consequence or only a stronger claim?
10. Is the source set now sufficient to decide, or would more loading merely duplicate known material?

Automated checks can verify paths, hashes, headings, question text, field uniqueness, and fixture results. Human review remains necessary for semantic conflict, ownership, authorization, applicability, and unsupported authority escalation.

**Decision sufficiency rule**

Proceed decisively when four dimensions align: the user or delegated authority permits the outcome; current repository policy permits and constrains it; observed state establishes identity, ownership, and preconditions; and mechanics plus verification can produce and prove the postcondition. Use local source guidance to structure the procedure and label any synthesis.

When a consequential dimension is unresolved, preserve the state, name the missing evidence or owner, and route or clarify. Do not convert missing evidence into a destructive default, and do not load unrelated sources indefinitely once the decision is sufficient. This keeps the guide both cautious and operational: evidence boundaries constrain action without becoming an excuse to avoid a safe, explicitly requested finish.
