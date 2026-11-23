# Git Delivery Flow: Reference

Depth for [SKILL.md](SKILL.md). The skill file holds every rule and the working
procedure. This file holds the reasoning, the full tables, the worked examples, and the
failure and recovery detail.

## Idiomatic Thesis Synthesis Statement

Delivering a change is a state transition chosen by the user, not a list of Git
commands. The inputs are the user's chosen outcome, the identity of the current branch
and worktree, who owns each dirty file, the relevant checks, the base and upstream
relationships, and how reversible the proposed action is.

The chain to keep intact:

```text
user intent
-> repository policy
-> observed repository, worktree and branch state
-> ownership and scoped diff
-> readiness evidence (checks)
-> authorized transition
-> independently verified postcondition
-> residual state, recovery, next owner
```

Each link answers a different question, and no link can stand in for another:

- A green test suite cannot authorize a push.
- A configured remote cannot prove quality, and cannot prove that pushing is allowed.
- A successful push cannot prove that the right branch or commit was published.
- A pull request cannot imply merge readiness or worktree cleanup.
- A command result says what exists. It does not say what the user wants.

**Three layers of verification.** Preconditions establish identity, ownership, scope and
quality. Action evidence records the exact commit, branch, remote, pull request, merge,
keep, or confirmed discard. Postconditions establish where the work now lives, whether
the expected changes remain, whether the merged checks pass, and what the next owner must
do. A successful exit status proves only that one command accepted its inputs.

**The flow is transaction-like without ceremony.** The action performs only the
authorized state change. Recovery evidence identifies what can be restored and who owns
the next move.

**Readiness and persistence are separate claims.** Tests support a completion or
merge-readiness claim. A checkpoint commit can preserve incomplete or failing work when
the user explicitly asks for that tradeoff, but it is never described as verified
completion. A draft pull request can give remote durability and review while CI or merge
policy is still pending.

**Known intent and unknown intent are complementary cases.** Direct execution handles a
request that already names the outcome. The four-option menu handles a request that does
not. A direct request shortens the choice, not the safety layers.

**Preserve optionality when evidence is incomplete.** Refusing an ambiguous finish is
safer than turning uncertainty into irreversible repository state. Successful
publication alone is not evidence that a branch or worktree should disappear. Cleanup
belongs later, when the recovery value of that state has expired or an explicit policy
requires removal.

**Adopt, adapt, avoid, escalate.** Adopt the repository's own workflow as written when
it is current, applies, and matches the user's intent. Adapt generic instructions to the
installed Git, the remotes, protected branches and project checks. Avoid commands whose
preconditions are unknown. Escalate contradictions between sources, and shared
ownership, instead of choosing the most convenient line.

**Good, bad, borderline.**

- Good: named branch and worktree, reviewed scope, current checks, verified remote and
  base, exact pushed commit, pull request head confirmed, unrelated file preserved, CI
  reported as pending, cleanup deferred.
- Bad: force-deleting a dirty branch because the implementation "seems complete", or
  getting a clean status by sweeping the user's changes into the commit.
- Borderline: a correct push that assumed `origin`, removed a useful worktree, omitted
  the unverified gates, or called the work merge-ready before the asynchronous checks
  finished.

**A good finish report** names what was saved, where it was saved, which checks ran,
what state remains, and the next action. For shared outcomes keep stable identifiers:
branch, commit, remote, pull request or merge, worktree path, verification result,
unresolved risk, next owner.

**The commit-push-continue cycle.** In day-to-day development the delivery step sits in
a loop: complete work, verify, commit, push when allowed, pick the next task. The role of
the agent in that loop is to keep momentum, keep quality, and coordinate helpers. Use
the project's own documents to make informed decisions; take initiative on next steps;
ask before major architectural changes. Be bold but not reckless: always verify before
committing.

## Pattern Scoreboard Ranking Table

The order is a priority order for attention. It is not a success rate, a confidence
level, or a safety measurement (not measured). Consequence can override the order: user
intent, repository policy, ownership and preservation of work always outrank a
convenient higher-ranked pattern.

| Rank | Pattern | What it prevents | Evidence it leaves behind |
| --- | --- | --- | --- |
| 1 | Authority and state map first | Plausible generic Git advice applied to a repository whose rules and state were never read | The request, the policy lines that apply, the live state snapshot, the conflicts found |
| 2 | Evidence boundary split | Treating a command result, a skill default, or a web page as permission | A label on each consequential claim: user authorization, policy, observed state, source default, external pointer, or synthesis |
| 3 | Verification gate coupling | A mutation with no precondition, postcondition or recovery path | For each mutation: the precondition checked, the expected change, the postcondition observed, the recovery path |
| 4 | Intent first | Forcing a menu on someone who already chose; guessing for someone who did not | The requested outcome, stated |
| 5 | State before mutation | Committing on the wrong branch, in the wrong worktree, with unknown dirty files | The snapshot: root, branch, worktree, status, diff, upstream, remotes |
| 6 | Least destructive default | Losing commits, branches, worktrees or user edits when cleanup intent is absent or sources conflict | The preserved recovery options |
| 7 | Scoped mutation | Unrelated dirty changes swept into a save to get a clean status | The exact branches and pathspecs used |
| 8 | Postcondition proof | "It exited zero, so it worked" | The resulting branch, commit, remote, pull request, worktree and open work |

Supporting observations:

- A finish report must say what was saved, where, which checks ran, what remains, and
  who acts next.
- A kept branch or worktree needs a revisit or retirement trigger. Without one,
  conservative retention becomes stale debris.
- Baseline tests recorded when a worktree was created separate a pre-existing failure
  from a regression. Ignore safety and the branch-to-path association matter at cleanup
  time. A branch name alone cannot reconstruct those facts later.

**Repairing a failed dependency.** Send the failure back to the link that owns it:

| What failed | Where it goes |
| --- | --- |
| Checks fail | Back to implementation, or to an explicit checkpoint choice |
| Mixed ownership | Back to scoping |
| Ambiguous base or remote | Back to clarification |
| Sources conflict | Conservative preservation |
| Unexpected postcondition | Stop all further cleanup |

**Three evidence depths.**

| Action | Evidence |
| --- | --- |
| Local save on a clean, isolated branch | Compact: status, diff, the requested commit |
| Push, pull request, or merge | Adds upstream, remote, base, shared verification |
| Discard, force deletion, worktree removal | Adds exact confirmation, an inventory of what disappears, recovery analysis |

**Discriminating fixtures.** A procedure that produces the same finish command for every
one of these is matching keywords, not reasoning from state. The chosen action and the
report should change when you:

- change the current branch while the test output stays the same;
- add one unrelated dirty file;
- remove the upstream configuration;
- provide two remotes;
- request a checkpoint with failing tests;
- leave out cleanup consent after pull request creation.

Good application takes a direct draft pull request, inspects the scoped dirty state,
runs the checks, creates the intended commit, verifies the pushed branch, reports the
pull request and keeps the worktree. Bad application reads every guide and then
force-deletes a branch after tests pass. Borderline application runs the full test suite
but never separates pre-existing user edits from task changes: quality evidence is green
while ownership evidence is missing.

## Agent Usage Decision Guide

Use the skill when the user wants completed or checkpointed work saved, published,
integrated, kept, cleaned, or discarded, or when a linked worktree needs a verified
finish decision. A mention of the topic triggers state inspection, not automatic
mutation.

**Operating sequence.**

1. Name the requested outcome. If the user asked for commit, push, draft pull request,
   merge, keep, cleanup or discard, keep that path. Ask only about missing details that
   can change scope, destination, destruction or readiness.
2. Read the repository's current instructions.
3. Inspect root, branch or detached state, worktree identity, dirty-state inventory,
   scoped diff, upstream, remotes, and candidate base as the action needs them.
4. Separate task-owned changes from pre-existing or concurrent work. Do not get a clean
   tree by absorbing unrelated edits.
5. Run the relevant project checks and state what they cover. A checkpoint request may
   preserve failing work, labeled non-ready.
6. If intent is still unknown, present the four options. If it is known, proceed.
7. Execute the smallest authorized transition. Publication and cleanup stay separate.
   Discard and force need explicit confirmation and policy.
8. Verify the outcome and report what was saved, where it lives, what is pending, and
   who owns the next action.

**Routing by task signal.**

| Signal | Use or route | Authority boundary |
| --- | --- | --- |
| "Commit and push these task changes." | Direct path after reviewing staged scope, checks, branch and verified remote | Authorizes save and publication. Not unrelated changes, force push, or cleanup. |
| "Open a draft pull request." | Publish the intended branch, create the draft, report pending checks, keep the worktree | Draft publication does not assert merge readiness or authorize branch deletion. |
| "Implementation is done; what next?" | Verify checks and state, then present the four outcomes | Do not preselect integration or discard for the user. |
| "Save this progress even though one test fails." | Explicitly labeled checkpoint if scope and ownership are safe | Persistence is not completion. Report the failing check and the recovery step. |
| "Discard this branch." | Inventory commits, dirty files, worktree, recoverability; request exact confirmation | The opening phrase is not the confirmation if the inventory was not yet visible. |
| A merge or rebase conflict is active | Route to conflict diagnosis and resolution, optionally after a preserving checkpoint | Finishing resumes only after the conflict and the intended base are resolved. |
| Deployment or release promotion wanted | Produce a branch handoff, then route to the release or deployment authority | This skill does not govern rollout, credentials, or service objectives. |
| Ownership or dirty-file scope unclear | Stop mutation, preserve evidence, clarify or route to the owner | A general Git skill cannot authorize another person's edits. |

**Proactive use.** Start the flow without being asked for it by name when the user
signals that work is ready to persist: "this looks good", "let's save this progress",
"tests are passing", after a logical unit of work is complete. Casual save language
counts when code changes exist. Proactive applies to verifying and committing. It never
applies to pushing in a repository that requires the explicit word, and never to
cleanup or discard.

**When the user grants autonomy.** "Commit and push, and keep going, I trust you" names
three things: the save, the publication, and continuation. After the save: read the
project's priority document, read the architecture documents for the next step, delegate
research if needed, and propose or start the next logical task based on project goals,
current status and the user's stated direction. Seek confirmation for major
architectural changes.

**Delegation.**

| Situation | Route |
| --- | --- |
| A new approach must be researched, reference repositories studied, an unfamiliar domain understood, or architecture explored | An exploration agent |
| File operations, documentation updates, refactoring, utility scripts | A general-purpose agent |
| Standard Git operations, established patterns, well-defined features | Do it yourself |
| Ambiguous requirements; a decision that departs from the architecture documents; a merge conflict that needs human judgment | The user |

Brief delegated agents on the project context. Explain the handoff reasoning in a
sentence. Keep continuity between the agents: the result returns to this flow and is
re-verified here.

**Communication style.** Decisive and action-oriented. Give status updates during
multi-step operations. Suggest next steps. Match the user's collaborative tone. Use
structured output for complex workflows.

**Defaults are hypotheses.** `main`, `master`, `origin`, a configured upstream and a
clean status can all be valid and still wrong for the requested outcome. Confirm any
assumption that changes consequences. Be predictable about safeguards and adaptable
about the path.

**Evidence states.** Use one for every consequential item:

| State | Meaning | What you may claim |
| --- | --- | --- |
| `verified` | Current evidence directly establishes the property for the relevant commit, tree, destination and environment | The property, with its evidence scope |
| `pending` | An asynchronous check, review or owner action is expected but not complete | The durable progress, plus the pending consequence, owner and follow-up. Not the stronger readiness state. |
| `not observed` | The evidence was unavailable, inaccessible or not run | The gap and its effect. Block when it can change safety or the requested claim. |
| `not applicable, with reason` | The property does not apply to the selected outcome | The reason, for example "no remote publication for a local keep" |
| `blocked` | A required property is false or consequentially ambiguous (unknown counts as blocked) | Nothing. Preserve state, name the blocker, route or ask. |
| `redacted, with reference` | A sensitive detail is left out of the summary but exists in an authorized protected record | That the detail exists and where |

Do not leave an important field blank. Blank can mean forgotten, unavailable, irrelevant
or hidden, and each leads to a different decision.

Example: a pull request is `verified` as created at a given URL and commit while remote
CI is `pending`. That is a successful publication handoff, not verified merge readiness.
A local checkpoint is `verified` as durable while integration tests are `not observed`:
report a checkpoint, not a completed feature.

**Audit.** Judge usage against the user's desired final state. Record the trigger, the
requested outcome, observed preconditions, the authority used, the rejected alternative
when it mattered, the exact mutation scope, the postcondition, the pending gate and the
next owner. Success is not the number of Git commands run. It is a correct and
recoverable transition to the requested state.

**Turning repeated choices into convention.** If a team always uses one remote,
draft-first review, one check suite or one worktree retention rule, propose writing it
into the repository's instruction file. Do not promote one temporary request into policy
without approval and an owner.

## Decision Tradeoff Guide

Choose by matched conditions. User intent selects the outcome. Repository policy and
observed state decide whether that outcome is safe now. Source guidance supplies
defaults where those are silent.

| Decision | Choose when | Cost | Question to answer |
| --- | --- | --- | --- |
| Adopt | Request, policy, observed state, the procedure's preconditions and verification all align | Fastest and most predictable, but copying literal commands can carry stale assumptions about the environment | Do the preconditions hold for this exact branch, worktree, remote, base and outcome? |
| Adapt | The state-transition contract fits but mechanics, checks, remotes, hosting or interaction differ | Keeps the safety model; adds your own inference, which you must review | Is every changed condition visible, and do the postconditions prove the adapted path reached the same authorized result? |
| Pause or route | Ownership, policy, state, permissions, quality or destination is missing, conflicting, or outside this skill | Prevents false confidence; may delay integration or need another owner | Does the handoff name the failed precondition, the preserved state, the responsible authority and the return condition? |
| Cost of being wrong | The wrong path publishes unrelated edits, merges into the wrong base, deletes recoverable work, misstates readiness, or strands a reviewer | Correction may need history repair, coordination, rework, or may be impossible after unreferenced data is removed | Can a reviewer tell what to undo, which recovery references remain, who was affected, and what prevents recurrence? |

**The nine outcomes.**

| Outcome | Choose when | Accepted cost | Decisive postcondition |
| --- | --- | --- | --- |
| Local commit | The user wants an intentional local save and the reviewed scope can be isolated | No remote durability or shared review; branch may still be behind or unready | The new commit contains only intended changes; unrelated dirty state is still visible |
| Checkpoint commit | Work must be preserved despite failed or incomplete gates, and the user accepts that | Creates debt; can be mistaken for ready work | Commit and report are clearly labeled non-ready, with failures, owner and resume condition |
| Push branch | Remote durability or collaboration is wanted without a review artifact | Exposes state remotely; may trigger automation | The intended remote branch contains the recorded commit; pending checks are named |
| Draft pull request | Review and remote durability are useful before merge readiness | Needs hosting access and ongoing review ownership | Draft identity, base, head commit, pending gates and preserved worktree state are reported |
| Ready pull request | Local and repository-required readiness evidence supports formal review | CI and reviewers can still reject it | Pull request state, exact commit, applicable checks and unresolved risks are current |
| Local merge | Policy permits local integration and the base is confirmed | Can diverge from remote policy; the base may need updating first | The merge exists on the correct base and the required checks pass on the merged tree |
| Keep branch and worktree | The user will continue later, ownership is pending, or recovery value is high | Uses workspace; stale-state risk grows over time | Exact branch, path, dirty summary, owner and revisit trigger are reported |
| Cleanup after a durable outcome | The commit is integrated or on the remote, no local-only state remains, and cleanup is requested or governed | Removes convenient local recovery and environment state | Only the intended branch or worktree references disappear; shared and unrelated work remain |
| Confirmed discard | The user knowingly rejects inventoried work and understands the recovery limits | May be irreversible, especially for untracked or unreferenced data | Exact confirmation precedes the action; the post-state proves only the intended work was removed |

**Six tradeoffs to resolve out loud.**

- **Direct execution versus menu.** Direct execution respects clear intent and saves
  time. The menu preserves choice when intent is absent. Never use the menu to avoid a
  complete request, and never use direct execution to skip a missing confirmation.
- **Local versus remote durability.** Local saves are fast and private. Pushes and pull
  requests protect against local loss and enable review, but expose the work and may
  trigger policy or automation.
- **Review versus integration speed.** Draft or ready pull requests add collaboration
  and asynchronous checks. A local merge is faster only when current policy permits it.
- **Fix versus checkpoint.** Repair supports readiness. A checkpoint preserves progress.
  Label the checkpoint so persistence is not mistaken for quality.
- **Cleanup versus recovery.** Cleanup reduces clutter. Retention preserves environment
  and recovery. Separate publication from cleanup and attach a retirement trigger.
- **One broad commit versus scoped commits.** A broad save can preserve an emergency
  snapshot. Scoped saves improve ownership and review. Inventory any knowingly mixed
  checkpoint. A mixed emergency checkpoint is borderline, not automatically wrong, when
  every included change, owner, debt and exit condition is recorded.

**Decision record.** Selected outcome, state evidence, authorization, the rejected
alternative when it mattered, expected cost, recovery path, reversal trigger.

**Reversal triggers** keep conservative choices temporary: a branch kept for pending
review is cleaned after merge and confirmation; a checkpoint is promoted after the
failures are fixed; a draft becomes ready after checks pass.

**Portfolio cleanup is a separate maintenance job.** Many individually sensible kept
worktrees and branches add up to stale ownership. Inventory them, find owners and
durable outcomes, verify current state, and clean in reviewed batches. Age alone never
authorizes deletion.

**The authority ladder.** Apply it one claim at a time, not as "latest file wins".

1. **Explicit user authorization** selects among valid outcomes and supplies exact
   destructive confirmation. It cannot make an impossible or policy-forbidden mechanic
   valid.
2. **Current repository policy** defines required checks, protected branches, the
   integration base, remotes, worktree conventions, push permission, message rules.
3. **Observed repository state** confirms or falsifies preconditions: branch, worktree,
   dirty scope, upstream, remote configuration.
4. **Direct-request interaction default**: execute a named path without a menu, save
   intentionally, report concisely, where policy is silent.
5. **The four-option model, test-first completion and destructive inventory** for
   unknown intent.
6. **Worktree lifecycle guidance** for directory, ignore safety, baseline and cleanup
   mechanics.
7. **External documentation**, once actually read, clarifies platform behavior. It does
   not replace intent or local policy.

A project rule can replace the generic base branch without weakening the generic
discard confirmation. A later guide can refine interaction without replacing an older
guide's detailed worktree mechanics.

## Theme Specific Artifact

Three artifacts: the state-transition matrix, the repository profile, and the message
check.

### 1. Dirty-worktree state-transition matrix

Fill it in before mutation when the state is mixed, shared, remote or destructive. For a
clean, low-risk local save use the compact subset: identity, request, scope, checks,
action, postcondition, remaining state.

| Field | Completion rule | Where the evidence comes from | Worked value (`feature/auth`) |
| --- | --- | --- | --- |
| Repository and worktree identity | Root, exact working directory, linked worktree path, branch or detached commit | `git rev-parse`, branch inspection, `git worktree list --porcelain` | Repository `/repo`; worktree `/repo/.worktrees/auth`; branch `feature/auth` |
| User goal | The requested final state, and whether the user already chose a direct path | The request and any clarified consequence | Commit the task files, push the feature branch, open a draft pull request |
| Applicable policy | Instruction file rules, protected targets, required checks, remote convention, push permission, message rules, cleanup rule | Repository files and accessible platform policy | Use the repository test script; draft targets `main`; no automatic worktree cleanup rule found |
| Dirty-state inventory | Staged, unstaged, untracked, conflicted, ignored-risk and submodule state | Porcelain status plus focused inspection | Three task files unstaged; one unrelated untracked `notes.txt`; no conflict |
| Ownership classification | Every changed path is task-owned, user-owned, shared, generated, unknown, or intentionally mixed | Task scope, prior state, user confirmation, diff review | Three auth files task-owned; `notes.txt` user-owned and excluded |
| Commit scope | Exact paths or hunks to stage, the commit's purpose, the excluded state | Reviewed diff and ownership record | Stage only the three auth paths; keep `notes.txt`; message explains auth behavior and tests |
| Readiness evidence | Current tests, build, lint, formatting, policy checks and known gaps, with the tree they cover | Repository commands and current results | Auth tests and the full suite pass on the staged content; remote CI not yet observed |
| Base, upstream, remote | Candidate base, tracking branch, named remote, and how each was verified, when the action needs them | Policy, merge-base discovery, upstream, redacted remote data | Base `main`; push `feature/auth` to verified remote `origin`; no force |
| Selected transition | One of: commit, checkpoint, push, draft PR, ready PR, local merge, keep, cleanup, confirmed discard | User goal plus the tradeoff guide | Commit, push, draft PR; integration pending review |
| Publication boundary | Remote publication kept apart from merge acceptance and asynchronous checks | Hosting output and observed check state | Draft PR is successful publication; merge readiness pending CI and review |
| Cleanup boundary | Whether branch and worktree are kept or removed, why, and what would reverse the choice | Explicit request, worktree state, retirement policy | Keep both; reconsider after merge, clean state, and owner-confirmed cleanup |
| Destructive confirmation | Inventory of what disappears and the exact confirmation, only when discard or force applies | User authorization and recovery analysis | Not applicable: no destructive action selected. The reason is part of the record. |
| Actions and results | Concise exact actions, targets, exit results, unexpected behavior, no credentials | Shell and hosting output | Scoped staging and commit succeed; push succeeds; draft PR identity recorded |
| Verification rule | Postconditions that prove the transition, not just that a command ran | The gate set below | Commit contains only task paths; remote branch contains the commit; PR is a draft; note and worktree remain |
| Recovery path | References and steps available if publication, integration or cleanup is wrong | Commit and branch identifiers, remote state, reflog where applicable, kept worktree | Kept worktree and feature branch give local recovery; revert or follow-up available after review |
| Remaining state and owner | Unrelated changes, pending checks, review, cleanup trigger, next person or agent | Post-action status and handoff decision | `notes.txt` stays user-owned; CI and reviewer own acceptance; author owns post-merge cleanup |
| Freshness trigger | Which mutation or policy change invalidates this matrix | Change-impact analysis | Any new tree change, remote retarget, base-policy update, or PR-head update reopens dependent fields |

Rules for the matrix:

- Do not fill unknown authority with a plausible default. A complete-looking matrix does
  not manufacture permission.
- A contradiction blocks the action: cleanup selected while local-only changes remain;
  publication to a remote that was never verified.
- Raw command transcripts are inputs, not the artifact. The matrix interprets state,
  ownership, authorization and consequence. A prose handoff, a pull request description
  or a status view may be derived from it, but one record governs, to avoid drift.
- Verify backward from the planned mutation: every target, path, readiness claim,
  cleanup choice and destructive permission traces to current evidence. Then verify
  forward from the action to the postconditions.
- When work is shared or delayed, the matrix is also the cleanup contract: it names who
  may retire the branch and worktree, on what trigger, with which final checks.
- "All changes" is not a scope. "Recover with Git" is not a recovery path. Pending CI
  with no owner or follow-up trigger becomes assumed success.

| Situation | Safe transition | State that must remain | Decisive gate |
| --- | --- | --- | --- |
| Clean task-only branch, direct commit request | Scoped commit | Branch stays local unless publication was also requested | Commit tree and message match the reviewed task scope |
| Mixed dirty tree, draft pull request requested | Commit only owned paths, push the intended branch, create the draft, keep unrelated files and the worktree | User and unknown changes untouched and reported | Staged diff, remote commit, draft identity and post-status all match the matrix |
| A relevant test fails, explicit checkpoint requested | Clearly labeled checkpoint of the reviewed scope | Failure evidence, unrelated changes, resume condition | The commit exists and the report does not claim readiness |
| Local merge requested | Confirm base and policy, integrate, rerun checks on the merged tree, then decide cleanup | Recovery references until the merged postconditions pass | The correct base contains the intended commit; merged-tree checks pass |
| Keep requested | No finish mutation beyond any explicitly requested save | Branch, worktree, dirty state and ownership visible | Post-status equals pre-state except the authorized save |
| Discard requested | Inventory, exact confirmation, targeted removal, postcondition | Unrelated branches, worktrees and files | The confirmation matches the inventory; only the intended state disappears |

### 2. Repository profile

Collect once per task. Two filled examples follow the blank.

```text
Repository profile
- Purpose of the repository:
- Push permission (who may trigger a push, with what words):
- Working branch and remote convention:
- Integration (base) branch:
- Commit message format:
- Forbidden content in commit messages:
- Paths that must never be committed:
- Required checks before commit:
- Fallback when the checks cannot run:
- Structural rules a change must respect:
- Worktree location convention:
- Where the next priorities are written:
- Decisions that need the user:
```

**Profile A: a private research knowledge base** (analysis documents, thesis documents
and research notes for open source contributions).

| Slot | Value |
| --- | --- |
| Push permission | Never push without explicit permission. Do not run `git push` unless the user explicitly says "push". Always ask before pushing. |
| Commit message format | Plain imperative sentence describing the document or change |
| Forbidden in messages | External issue numbers in any form: `org/repo#123`, `apache/iggy#2739`, bare `#123`. Reason: the commits show up as cross-references on the GitHub issues they mention. |
| Where issue references go | Inside file content only |
| Example | Bad: `Add deep analysis for MongoDB connector (apache/iggy#2739)`. Good: `Add MongoDB connector deep analysis for iggy`. |
| Checks before commit | Links resolve; the document is where the structure says it belongs |

**Profile B: a Rust inference-server project** (Pensieve: a local LLM server for Apple
Silicon; Rust workspace of eight crates, a Python bridge for MLX inference, Metal GPU
acceleration, serving a 4-bit Phi-3-mini instruct model. The commit-push-continue cycle
was written for it). Names below are that project's own; they are values for the slots,
not rules for other repositories.

| Slot | Value |
| --- | --- |
| Push permission | The user directs it: "commit and push to origin `<branch>`". The working branch is a named long-lived development branch (typically `ultrathink`, or as the user directs), pushed with `git push origin <branch>`. |
| Commit message format | Conventional: `<type>(<scope>): <description>`; types `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`; for example `feat(engine): add MLX inference streaming support`, `feat(api): add streaming support` |
| Never-commit paths | The local research directory of cloned reference repositories (`.doNotCommit/`); anything `.gitignore` covers |
| Required checks | `cargo test --workspace`; tests are written first; all tests pass before commit; both unit and integration tests where appropriate |
| Fallback when checks cannot run | When the test build has known compilation problems recorded in the instruction file, test manually and document the results |
| Structural rules | Three layers. L1 core (`pensieve-07_core`): foundation, no external dependencies, minimal, `no_std` compatible. L2 engine (`pensieve-04_engine`, `pensieve-05_models`, `pensieve-06_metal`). L3 application (`pensieve-01` CLI, `pensieve-02` API, `pensieve-03` models). No circular dependencies between layers. Metal GPU code stays in `pensieve-06_metal`. Functional, idiomatic Rust as the project documentation defines it. |
| Where priorities live | In that project's tree: a steering document (`.steeringDocs/S01-README-MOSTIMP.md`) with the critical guidance and next priorities; an architecture directory (`.prdArchDocs/`) with the latest architecture and requirements; the instruction file with coding standards, architecture and build commands |
| Research context | The never-commit directory holds cloned repositories relevant to the work; exploration agents research there |
| Project goals that shape "next task" | A throughput target of 25+ tokens per second (the project's stated goal, not a measurement), the MLX migration, API compatibility |
| Decisions that need the user | Ambiguous requirements; architectural decisions that depart from the architecture documents; merge conflicts that need human judgment; major architectural changes |
| Quality notes | Commit messages must let future developers understand the history. Document deviations from standard patterns with a rationale. Check that performance implications fit the project's goals. |

The two profiles disagree on pushing and on message format. Neither is wrong. The
profile in force is the one written in the instruction file of the repository you are
standing in.

### 3. Message check

```bash
# Prints nothing when the message is clean.
check_msg() {
  grep -nE '([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)?#[0-9]+|GH-[0-9]+|/(issues|pull)/[0-9]+'
}

git log -1 --format=%B | check_msg                          # the commit just made
git log '@{upstream}..HEAD' --format='%h %B' | check_msg     # everything a push would publish
printf '%s\n' "$DRAFT_MESSAGE" | check_msg                   # before committing
```

What it catches: `org/repo#123`, bare `#123`, `GH-123`, and URLs of the form
`.../issues/123` or `.../pull/123`. What it cannot catch: a reference written in words.
Read the message as well.

Squash-merge hosting turns a pull request title into a commit subject and often appends
the pull request number itself. In a repository with the no-issue-number rule, check
what the host will write before choosing squash-merge, and keep the title clean.

## Worked Example Set

Treat each example as a fixture: request, pre-state, ownership, checks, transition,
cleanup decision, postcondition, recovery. Branch names, paths and remotes are
illustrative. Discover and verify the real ones.

**Example 1: mixed dirty tree, direct draft pull request**

- Request: commit the authentication changes, push the feature branch, open a draft
  pull request.
- Pre-state: worktree `/repo/.worktrees/auth`, branch `feature/auth`, three task files
  changed, one unrelated untracked `notes.txt`, verified base `main`, verified remote
  `origin`.
- Good: review and stage only the three task files; run the checks on that content;
  commit with intent; push `feature/auth`; create the draft against the verified base;
  confirm the remote head commit; report CI pending; keep `notes.txt`, the branch and
  the worktree.
- Bad: stage everything, include `notes.txt`, push, then remove the worktree because
  the pull request was created.
- Borderline: exclude the note and create the draft correctly, but call the branch
  merge-ready before the remote checks finish. Publication passed. Readiness did not.
- Verify: staged diff, commit tree, remote head, draft state, post-status, and who owns
  the pending check.

**Example 2: requested local merge**

- Request: merge the completed feature into the integration branch.
- Pre-state: feature checks pass; the common-ancestor heuristic finds `main`, but the
  repository's instructions name `develop` as the integration branch.
- Good: follow policy; confirm `develop`; update it by the permitted workflow; merge;
  run the required checks on the merged tree; verify the feature commit is integrated;
  then ask, or follow explicit policy, about cleanup.
- Bad: merge into `main` because the command worked, and delete the feature branch
  before testing the merged tree.
- Borderline: merge into `develop` correctly and pass the checks, then remove a linked
  worktree that held an unrelated untracked file. Integration succeeded. Cleanup
  violated ownership.
- Verify: base identity, merge ancestry, test result, dirty state, exact cleanup target.
  Keep the feature reference until the merged-tree evidence is current.

**Example 3: explicit non-ready checkpoint**

- Request: save progress before an interruption although one known test fails.
- Pre-state: owned parser edits are isolated; the failure is reproducible and
  documented; no publication was requested.
- Good: review the scoped changes; create a commit labeled as a checkpoint; keep the
  failing-test evidence and the resume condition; report branch and worktree location;
  claim nothing about completion.
- Bad: hide the failure and call the branch ready because a commit now exists.
- Borderline: in an emergency, save a mixed checkpoint that contains another person's
  edit, but inventory every included file, obtain consent, assign ownership and define
  the split. That is accepted debt, not a clean default.
- Verify: the checkpoint contains the declared scope; the handoff keeps the failure
  output, the owner and the next test.

**Example 4: confirmed discard**

- Request: discard an abandoned experimental branch and worktree.
- Pre-state: two local commits are on no remote; one untracked generated artifact can
  be regenerated; one untracked research note cannot.
- Good: show the exact branch, commits, worktree, artifact and note. Preserve or
  explicitly exclude the note. Explain the recovery limits. Request exact confirmation
  for the revised inventory. Remove only what was confirmed. Verify unrelated state
  remains.
- Bad: force-delete branch and worktree at once because the user said "discard" before
  seeing the inventory.
- Borderline: rely on the reflog as guaranteed recovery for everything. Some references
  may be recoverable; untracked files and retention duration do not support the promise.
- Verify: test the mechanics in a disposable repository. In real work the confirmation
  and the post-state inspection are mandatory. Never test destruction on valuable state.

**Example 5: commit in this repository, no push requested**

- Request: "Commit the new connector analysis."
- Pre-state: one new Markdown document, which links to an upstream issue in its body.
- Good: stage the one file; write `Add MongoDB connector deep analysis for iggy`; run
  the message check (prints nothing); commit; report the hash and "Not pushed. Say
  'push' and I will push `<branch>` to `origin`."
- Bad: write `Add deep analysis for MongoDB connector (apache/iggy#2739)` and push
  because the commit succeeded. Two rules broken, and the cross-reference now exists on
  the upstream issue.
- Borderline: the message is clean, but an older unpushed commit on the branch carries
  an issue number. The new commit passes; the push would still publish the old one.
  Check the whole unpushed range, tell the user, and reword only with agreement.

**Example 6: commit, push and continue (autonomy granted)**

- Request: "Commit and push to origin `<working-branch>`, and start going further. I
  trust you."
- Good: status; `cargo test --workspace` passes; no local-research path staged; layer
  rules hold; `git add <files>`; `feat(engine): add MLX inference streaming support`;
  commit; `git push origin <working-branch>`; confirm the remote ref; report the hash;
  then read the steering document and propose the next task.

  ```text
  ## Committing changes
  - Verified tests passing: `cargo test --workspace`
  - Staged files: `git add src/`
  - Committed: `git commit -m "feat(api): add streaming support"`
  - Pushed to origin/<working-branch> (commit: abc123f)

  ## Next steps
  Based on the steering document, the next priority is GPU integration.
  Starting an exploration task to research current patterns.
  ```
- Bad: tests fail, and the commit is made anyway to "keep momentum". Report the failing
  tests with their output and do not commit.
- Borderline: the push is rejected because the remote moved; the agent rebases and
  retries without rerunning the tests. The tree changed, so the earlier test result no
  longer covers it.

**Example 7: worktree created, baseline red**

- Request: "Set up a worktree for the parser rewrite."
- Good: `.worktrees/` exists and is ignored; `git worktree add .worktrees/parser -b
  feature/parser`; run the project's setup; run the tests; two fail before any change;
  report the two failures and ask whether to proceed or investigate.
- Bad: proceed silently. At finish time nobody can tell whether those two failures are
  regressions.
- Borderline: `.worktrees/` is not ignored, and the agent edits `.gitignore` and commits
  it without asking. The diagnosis is right. The authority for that commit is missing.

**Regression variations.** Swap the current branch while tests stay green. Add one
untracked user file. Remove the upstream. Change the repository's base. Request a draft
without cleanup. Make remote CI pending. Turn an ordinary checkpoint into a discard. Add
an older unpushed commit that carries an issue number. Ask for "commit" with no "push".
A correct procedure changes its action and its report with each.

Commands in the examples are subordinate to the invariants. Retire an example when
readers succeed by memorizing its branch names but fail on an equivalent changed state.

## User Journey Scenario

A contributor or agent has finished the implementation, or needs an intentional
checkpoint, and must decide how the branch or worktree ends. The journey turns the
user's intent plus live repository evidence into one bounded action and a handoff that
someone else can reconstruct.

| Stage | What happens | Exit condition |
| --- | --- | --- |
| 1. Frame the outcome | Record the requested final state and its consequence. "Commit the task changes and open a draft pull request" selects a path. It does not authorize unrelated files, force, or cleanup. "What next" keeps the choice open for stage 5. | You can state what should exist afterwards and what must remain untouched |
| 2. Establish authority and identity | Read the repository's instructions. Confirm root, working directory, branch or detached commit, linked worktree, remotes, upstream, candidate base. | The intended repository object and the governing policy are visible. If the checkout is detached, the base uncertain, or permissions external: stop or route. |
| 3. Scope ownership | Inventory staged, unstaged and untracked state. Separate task-owned edits from pre-existing or concurrent work. Do not stage broadly to simplify the finish. | An explicit save scope and a list of unrelated state to be preserved. If ownership cannot be resolved: preserve evidence and return to the owner. |
| 4. Verify the claim | Run the project-defined checks that support the requested outcome. A merge-ready claim needs more than a local checkpoint does. On failure choose repair, explicit non-ready checkpoint, or blocked handoff. | Checks recorded against the tested tree. Later relevant edits invalidate them. |
| 5. Confirm the path | If the user already chose: confirm only unresolved consequential details (remote, branch scope, destructive inventory, and in this repository the word "push"). If not: present the four options. | One authorized transition and a stated recovery plan |
| 6. Execute minimally | Save only the reviewed scope; publish only to the verified destination; merge only into the intended base; keep when asked; discard only after the inventory and exact confirmation. | The action ran once. On an unexpected result: stop. Do not force, widen staging, or remove another worktree to reach the expected appearance. |
| 7. Prove and hand off | Verify the outcome-specific postconditions. Record commit, branch, remote, pull request or merge, worktree path or removal, check status, unrelated dirty state, pending gates, recovery reference, next owner. | A journey may end locally complete while CI or review is explicitly pending |

**Primary journey: a direct draft pull request.** The agent finds a feature worktree
with three task files and one unrelated user note. It stages and reviews only the task
files, runs the checks, makes the commit, pushes the verified feature branch, creates
the draft, confirms the remote commit, reports CI pending, and keeps both the note and
the worktree because cleanup was not requested. The handoff names the draft and the
next reviewer.

**Alternative exits.**

- **Local merge:** confirm the base; update it by repository policy; merge; rerun the
  checks on the merged tree; verify integration; only then consider cleanup.
- **Keep:** no unintended mutation; report branch, commit state, dirty summary, worktree
  path, and why it remains.
- **Checkpoint:** save the explicitly scoped state; report every failed or unrun gate
  and the condition for resuming.
- **Discard:** inventory commits, tracked and untracked changes, and the worktree;
  obtain exact confirmation; remove only the intended state; verify unrelated work
  remains.
- **Blocked:** preserve the evidence; name the failed precondition and its owner; say
  which result returns the task to stage 2, 3 or 4.

**Evidence expires between stages.** A relevant tree mutation invalidates status, diff
and affected tests. A changed upstream or remote invalidates destination assumptions.
Updated repository instructions invalidate policy decisions. A read-only operation does
not require a full restart: rerun only the dependent gates.

**Visibility is part of preservation.** A journey that safely keeps an unrelated file
but leaves it out of the handoff makes the next agent mistake it for new work.

**The worktree journey before the finish.** Choose the directory (existing convention,
then the instruction file, then ask). Check that a project-local directory is ignored.
Create the worktree on a new branch. Run the project's setup. Run the baseline tests and
record the result. Report the path and readiness. Everything recorded here is used again
at finish time: the path identifies the cleanup target, the baseline separates old
failures from new ones.

**After the finish.** When the user asked to continue: read the priority document,
choose or propose the next task, and re-enter the development loop. Repeated friction
should improve the environment: common base, remote, check, retention and draft-first
choices belong in the instruction file after the owner approves. Recurring mixed-state
or cleanup mistakes may justify safer scripts with regression fixtures.

## Anti Pattern Registry Table

Check this registry before any state-changing command. A blocker changes content,
destination, ownership, readiness, authorization or recoverability. A lower-impact
wording defect may be repaired without stopping an otherwise safe preserving action, but
it cannot justify an unsupported readiness claim.

| Anti-pattern | Why it fails | Safer replacement | How to detect |
| --- | --- | --- | --- |
| Context-free advice | Skips the repository's rules and state, then gives plausible generic Git advice | Read policy and state first | Require the policy lines used plus current branch, worktree, status |
| Unsourced authority | Guidance sounds authoritative without separating user authorization, policy, observed state, public evidence and synthesis | Label the authority of each recommendation | Sample each consequential recommendation and ask who or what authorizes it |
| Unverified instruction | A mutation with no precondition, postcondition or recovery check | Couple each mutation to a gate | Predict the state change, run the scoped action, compare actual branch, commit, remote, worktree |
| Push without the word | A push follows a successful commit in a repository that requires explicit permission | Ask, then wait | Find the word "push" in the user's latest instruction |
| Issue number in a commit message | Creates a cross-reference on someone else's issue tracker | Reference inside file content only | The message check prints a match |
| Mutation before status | Commit, merge, push, deletion or worktree removal begins before identity and dirty state are known | State before mutation | Non-mutating root, branch, worktree, status, diff, upstream, remote evidence exists first |
| Mixed commit scope | Task edits staged with unrelated or concurrent changes to get a clean tree | Pathspec or patch staging | Compare staged and unstaged diffs with the task's owned paths; review every staged file |
| Wrong branch or remote | A valid command acts on an assumed branch, upstream, base or `origin` | Explicit, verified target | Resolve branch, base, remotes, tracking; report assumptions that remain |
| Tests-only readiness | Green tests treated as proof of scope, ownership, publication or merge policy | Multi-dimensional finish evidence | Quality gates checked separately from diff scope, identity, remote state, review, asynchronous checks |
| Forced menu after a direct request | The user is asked to choose again after an explicit instruction | Direct request after safety gates | The request maps to one path; only missing consequential details are asked |
| Automatic worktree cleanup after a pull request | Pull request creation read as permission to remove the worktree | Publication and cleanup decoupled | Kept by default; removal needs explicit intent, clean state, remote durability, exact target |
| Discard without exact confirmation | Branch, commits, dirty files or worktree deleted from inferred intent | Inventory, then explicit confirmation | The inventory was shown and the exact confirmation received before the action |
| Force as first recovery | Force-delete or force-push used to get past an unexpected state | Classify, preserve, escalate | The failed precondition is named; force appears only under explicit policy and authorization |
| Unauthorized ignore-file commit | Worktree setup changes and commits `.gitignore` on its own | Report the risk or request the repair | Policy inspected and the save boundary obtained before editing |
| Worktree chosen by text match | A substring of a branch name selects the wrong worktree for removal | Porcelain output or exact identity | Full target path and branch association compared |
| Branch deleted before the postcondition | Local cleanup before merged or remote state and recovery references are verified | Postcondition before cleanup | The commit is confirmed integrated or remote; the remaining owner is recorded |
| Clean tree equals finished | Clean status treated as completion while commits are unpushed, checks pending or the wrong branch active | Outcome-specific completion contract | The chosen outcome is verified explicitly |
| Committing broken code for momentum | Failing tests committed without a checkpoint request | Report failures; fix or ask for a checkpoint | Test result recorded against the committed tree |
| Proceeding on a red baseline | Work begins in a new worktree whose tests already fail, unreported | Report and ask | Baseline result recorded at creation |
| Hardcoded setup | One ecosystem's install command assumed for every project | Detect from project files | Setup command traced to a manifest file |
| Open question at finish | "What should I do next?" instead of structured choices | Exactly four options | The menu text |
| Vague report | "Clean and pushed" | Commit, branch, remote, checks, leftovers, owner | A reviewer can reconstruct the transition |

**Review order:** intent, repository identity, ownership, diff scope, quality gates,
destination, reversibility, exact action, postcondition. Skip a dimension only when it
cannot affect the requested outcome (a local checkpoint may not need base discovery; a
local merge does), and be able to explain the omission.

**Do not ban commands by spelling.** `git add -A` is correct when every visible change
is intentionally owned and reviewed, and unsafe in a mixed shared tree. `git branch -D`
implements a confirmed discard, and is unacceptable as an automatic response to an
unexpected merge state. Safety depends on scope, authority and recoverability.

**Use the smallest remediation that keeps the intent.** Pathspec or patch staging
isolates task changes. A named checkpoint preserves progress without claiming readiness.
A draft pull request gives remote durability and review while checks are pending. A kept
worktree preserves local recovery. A temporary branch copy can protect uncertain state,
if it has an owner and a retirement trigger.

**When an anti-pattern lives in a script, hook, skill or shared convention:** contain
its spread and keep a failing fixture before repairing it. Durable automation needs an
owner, an exact scope, a recovery path and a regression test. Retire low-signal warnings
so high-consequence blockers stay visible.

**Fixtures for blocker detection:** the same tests on a different branch; one unrelated
dirty file; two remotes; no upstream; a candidate base that differs from project policy;
a pull request with no cleanup instruction; a confirmed discard with an untracked file;
a worktree path that shares a substring with a branch name. Pair command evidence with
explicit human authorization, because ownership and intent cannot be read from Git.

## Verification Gate Command Set

Run inspect commands before mutation, from the exact worktree under review.

| Gate | Command or evidence | What it establishes | What it does not establish |
| --- | --- | --- | --- |
| Repository identity | `git rev-parse --show-toplevel` and the current directory | The repository and worktree that will receive later commands | User intent, branch ownership, readiness |
| Branch or detached state | `git branch --show-current`; if empty, `git rev-parse --short HEAD` | Named branch or detached commit | The correct integration target, or permission to create a branch |
| Worktree identity | `git worktree list --porcelain` | Exact linked paths, branches, detached states, in parseable form | Whether a path is safe to remove or still needed |
| Dirty-state inventory | `git status --porcelain=v1 --branch` | Staged, unstaged, untracked, tracking indicators | Who owns each change |
| Scope review | `git diff --name-status`, `git diff --cached --name-status`, plus reading the content | Changed-file and staged-file scope before saving | Semantic correctness |
| Whitespace sanity | `git diff --check`, with a pathspec when scope is narrow | Conflict markers and whitespace errors | Formatting, compilation, tests, policy |
| Upstream and remotes | `git rev-parse --abbrev-ref --symbolic-full-name '@{upstream}'`; `git remote -v` with credentials redacted | Tracking target and configured endpoints | Which remote the user authorizes, or whether pushing is permitted |
| Candidate base | Repository policy first; `git merge-base HEAD main` tests a candidate | Common ancestry with the candidate | That the candidate is the intended integration base |
| Project quality | The repository's test, build, lint, type, format and security commands | Current results for the tested tree and environment | Future CI results, commit scope, remote acceptance |
| Message rules | The message check in the artifact section | The message carries no issue-number pattern | That the message is meaningful |
| Authorization | The explicit request, the instruction file, the exact destructive confirmation | Which transition may be attempted | That the technical preconditions hold |
| Postcondition | Outcome-specific status, log, upstream, hosting, merge and worktree checks | Where the commit and working state now live | Unobserved asynchronous checks, future deployment success |

**Four classes of evidence:** inspect, project check, authorized mutation,
postcondition. Verification must not silently change the baseline. A push, merge, branch
delete or worktree removal is an action, even when used to find out whether permissions
allow it. Attempt it only after preconditions and authorization, and record its result
without escalating to force.

**Postcondition commands.**

```bash
# Commit or checkpoint
git rev-parse --short HEAD
git show --stat --format='%h %s' HEAD        # only intended paths
git status --porcelain=v1 --branch            # unrelated changes still listed

# Push
git rev-parse HEAD
git ls-remote <remote> "refs/heads/<branch>"  # same hash

# Pull request
gh pr view --json url,isDraft,headRefOid,baseRefName,statusCheckRollup
gh pr list --head <branch> --state open       # exactly one

# Local merge
git branch --show-current                     # the intended base
git merge-base --is-ancestor <feature-commit> HEAD && echo integrated
<project test command>                        # on the merged tree

# Keep
git status --porcelain=v1 --branch            # equals the pre-state

# Cleanup or discard
git worktree list --porcelain                 # only the confirmed target is gone
git branch --list
```

Report after a discard any recovery reference that was kept on purpose.

**Guards against a false green.**

- Check both staged and unstaged changes.
- Include untracked files, through status.
- Capture exit codes.
- Rerun affected checks whenever the tree changes.
- Record the tree or commit the checks covered, the environment, and their order
  relative to later mutations.
- Redact credential-bearing remote URLs.
- Report command, target, current result and what the result covers, not a noisy
  transcript.
- After a push, compare the destination ref or the pull request head with the intended
  commit yourself, instead of trusting the push output.

**Record quality.**

- Good: "In worktree `/repo/.worktrees/auth` on `feature/auth`, only three task files
  were staged; repository tests passed at commit `abc1234`; the user requested a draft
  pull request to the verified remote; the pushed branch contains that commit; remote
  checks are pending; the worktree was kept."
- Bad: "Git clean."
- Borderline: a status snapshot taken before generated files changed. It is historical
  evidence, not current readiness.

**Maintaining the ladder.** When a consequential defect escapes, add a fixture or check
aimed at its mechanism, and confirm it separates a safe case from an unsafe one. Retire
redundant checks that never change an action. The goal is a small maintained set that
independently covers identity, ownership, quality, authorization, transition and
recoverability.

## Failure Mode Table

Classify the failure before choosing a corrective command. A failed precondition that
changed nothing, a partial remote transition, a wrong-target success and a destructive
loss have different recovery contracts.

**First response to an unexpected consequential result.**

1. Stop further mutation, including automatic cleanup and broad retry loops.
2. Capture the command, the result, repository, worktree, branch or detached identity,
   current commit, index and working-tree state, and any active Git operation.
3. Inventory local-only and unrelated work without resetting or deleting it.
4. Query the remote or platform destination when authorized. An error response does not
   prove there was no server-side effect.
5. Compare intended with actual state and classify: no mutation, complete mutation,
   partial mutation, wrong-target mutation, or unknown effect.
6. Select the narrowest authorized retry, roll-forward, preserving checkpoint,
   compensation, recovery route, or escalation.
7. Verify the corrective postcondition and report any remaining uncertainty.

Redact credentials and sensitive content from diagnostics. Keep immutable identifiers
and the exact meaning of the error.

| Failure mode | Trigger | Symptom or risk | Immediate containment | Gate before retry or recovery | Closure evidence |
| --- | --- | --- | --- | --- | --- |
| Wrong repository or worktree | Discovery or action ran from an unintended root, linked worktree or nested repository | Status and branch do not describe the task; a successful command may have changed another checkout | Stop all writes; identify every affected repository and worktree; preserve their state | No ordinary retry until impact and ownership are known; route to recovery if something unintended changed | Intended and actual targets named; unintended effects contained; any correction explicitly authorized |
| Detached or wrong branch | Branch identity assumed from a directory name or stale context | The commit sits on detached history or another branch; the target lacks it | Keep the commit hash and reflog evidence; avoid checkout or reset that hides reachability | Attach or transfer the commit only after destination and ownership are confirmed | The intended branch references the intended commit; no unrelated branch changed; residual detached state reported |
| Mixed or unknown staging | Broad staging or concurrent edits brought in unowned paths or hunks | The staged diff exceeds the reviewed scope | Do not commit; unstage without discarding working content; classify each path or hunk | Restage only with explicit path or hunk scope and a refreshed diff | Staged content equals the authorized scope; unrelated state still visible |
| Stale verification | Checks ran before a later tree, index, config, generated-file, merge or policy change | The result does not cover the claimed commit or merged tree | Withdraw the readiness claim; identify the invalidating change | Rerun the gate against the actual state; checkpoint only if the user asks for the narrower outcome | Command, environment, covered tree and current result recorded |
| Required check failure | A repository-defined check fails or cannot run | The feature may be unfinished, the environment unavailable, or the failure unrelated but unresolved | Preserve the work and the failure output; do not quietly weaken the claim | Route to implementation or the environment owner, or make an explicitly incomplete checkpoint on request | The check passes for the claimed state, or the handoff names the pending failure, its consequence and owner |
| Hook or commit failure | A hook, signing, identity, storage or the commit command fails | Changes stay staged with no commit; a hook may have modified files | Inspect status, index, history and hook-made changes; do not assume no side effect | Retry only after fixing the specific cause and reviewing the modified state | The intended commit exists once with reviewed content; hook and residual state reported |
| Forbidden content in a commit message | An issue reference reached a local commit | A push would create a cross-reference on an external issue | Do not push; identify which unpushed commits match | Amend the tip; reword older unpushed commits only with the user's agreement; a commit already pushed cannot be fixed without rewriting shared history, so report it | The unpushed range passes the message check |
| Wrong base selection | Base inferred from a common name or stale ancestry | A merge or pull request targets an unintended line | Stop integration or publication; keep the branch; collect base-policy evidence | Select a base only from current repository or user evidence; undo or retarget through an authorized procedure | The actual base is verified; the resulting diff and history match the intended review scope |
| Wrong remote or upstream | Remote name, URL, fork or tracking branch assumed | The commit is published to an unintended repository or does not reach the intended one | Stop further pushes and cleanup; capture remote mappings and actual destination refs | Correction may need a maintainer; do not delete or rewrite remote state without authority | The intended destination holds the intended commit; the unintended publication is resolved or explicitly owned |
| Non-fast-forward rejection | The upstream advanced, or the branch relationship differs from what was expected | The local commit is durable but the remote did not advance | Keep the local commit; fetch; inspect divergence and policy | Retry only after an authorized merge, rebase or update strategy; force needs separate explicit authority | Remote ref and local history match the chosen strategy; checks refreshed where the tree or history changed |
| Transport or authentication failure | Network, credentials, permission or server availability interrupted publication | No reliable conclusion about the destination from the client error alone | Keep local state; query the destination when possible; no credential workarounds | Bounded retry only for a classified transient failure; access or policy failures go to the owner | Destination state known; one intended publication present or its absence verified; access issue has an owner |
| Push succeeds, pull request fails | The branch is published but creation or lookup of the pull request fails | Work is durable remotely; the review handoff may be absent, duplicated or mis-targeted | Do not push again or clean up; inspect existing pull requests and the published commit | Retry creation only after confirming no equivalent request exists and head and base are right | One intended pull request references the published commit, or publication-only partial success is reported with a next owner |
| Local merge conflict | A merge or related integration enters a conflicted state | The index holds conflict stages; earlier tests no longer establish readiness | Stop the finish flow; record the active operation and conflict paths; preserve unrelated changes | Route to conflict resolution; do not pick content or abort without an objective and an owner | The operation is intentionally resolved or aborted; the repository is coherent; checks run on the result |
| Merged checks fail | The merge completes but required checks fail on the merged tree | History advanced while completion quality is false | Keep the merge evidence; do not clean the source worktree or report success | Follow repository policy for fix-forward, revert or recovery; no ad hoc history rewrite | The integrated branch reaches an intentional state with current checks and an explicit disposition of the source branch |
| Cleanup precondition failure | The branch or worktree is dirty, checked out, unmerged, unpushed or holds local-only state | The deletion command refuses, or a broad cleanup would lose recovery evidence | Treat the refusal as protection; inventory the exact target and its durability | Clean up only after explicit intent, verified durable destination, no local-only state, and an exact target recheck | Only the intended target is removed; other branches, worktrees and user state unchanged |
| Discard not exactly confirmed | Silence, ambiguous wording or a stale confirmation is read as permission | User work may be unrecoverable, above all untracked content | Do not discard; show what would disappear; request exact confirmation | Proceed only against the unchanged inventoried state and current authorization | The specified state is gone; unrelated state remains; recovery limits were stated accurately |
| Destructive action partial | A deletion, reset or cleanup affected some targets before failing | The repository is neither fully preserved nor in the intended state | Stop; preserve remaining refs, files and logs; no garbage collection or further deletion | Route to repository recovery; compensation needs exact current-state evidence and authorization | Recoverable work is secured; actual loss is stated; invariants restored or owned |
| Concurrent state change | A user, agent, hook, generator or process changed relevant state after inspection | Diff, branch head, checks, remote or cleanup target no longer match the evidence | Stop; capture both observed versions without overwriting the newer one | Reclassify ownership and workload; serialize writes or obtain coordination | Refreshed evidence covers the current state; the operation has one accountable writer |
| Source or policy drift | A local instruction, guide, branch protection or required check changed | The earlier decision or verification no longer applies although commands still work | Preserve state; identify the changed authority or requirement | Refresh only the consequential source; reevaluate dependent decisions | The applied policy and version are named; stale guidance is no longer used |
| Misleading finish report | The action succeeded partially or evidence is absent, yet the handoff says complete, clean, tested or ready | A downstream owner may merge, release or delete on a false claim | Correct the report promptly; preserve the underlying evidence | Rerun the missing observations or downgrade to "durable progress with pending gates" | The report separates state safety, outcome fidelity and evidence fidelity, with a next owner |
| Documentation unclear about the next step | The project's documents do not say what to do next | Guessing the next task | Do not start work on a guess | Investigate, or delegate exploration, before proceeding | The next task traces to a document or to the user |
| Architectural question arises | The change raises a design decision | Deviating from the project's architecture silently | Pause the change | Read the architecture documents first; escalate if still ambiguous | The decision is recorded with its source |

**Selecting a response.**

- **Retry** only when the failure class is known, the operation is idempotent or the
  actual destination state has been queried, the required state has not changed, and
  policy allows another attempt.
- **Roll forward** when a durable shared effect already exists and an authorized,
  visible correction has less blast radius than rewriting or deleting that effect.
- **Restore or roll back** only when the inverse operation, current preconditions,
  ownership and recovery durability are established. Git cannot guarantee recovery of
  every untracked deletion or expired object.
- **Checkpoint** when the user wants preservation but completion gates are unavailable
  or failing. Record the narrower claim.
- **Compensate** when an external effect cannot be erased safely but a separate
  authorized action can restore the intended invariant. Keep both effects visible.
- **Wait** when remote CI, review or platform availability is the only unresolved state
  and local durability is verified. Name the owner, the consequence and the follow-up.
- **Escalate** when identity, ownership, repository integrity, credentials, shared
  history, destructive loss or production effects are uncertain.

**Contrastive handling.**

- A non-fast-forward rejection after a local commit is normally a publication failure
  with no remote change. Keep the commit, inspect divergence and policy, choose an
  authorized integration path. It is not permission to force-push. On a branch only you
  write to, the usual path is `git fetch origin`, then `git rebase origin/<branch>` or
  `git merge origin/<branch>`, resolve conflicts (escalating the complex ones), rerun
  the checks, push again.
- A timeout while creating a pull request is an unknown-effect platform failure. Query
  for an existing request before retrying. The server may have created it despite the
  client error. Repeating blindly can create duplicates or target a stale commit.
- A worktree removal refused because of dirty state is a safe, protective failure. Keep
  the worktree, inventory the local-only files, report why cleanup is blocked.
  Overriding it to complete a checklist turns a safe refusal into a possible incident.
- If unrelated work appears to be missing after cleanup, stop all repository
  maintenance. Preserve refs, reflog information, remaining files and command evidence.
  Avoid expiration, pruning, reset or reclone. Route to repository recovery and say
  honestly that restoration is uncertain, above all for untracked content.

**Never relabel a breach as a normal retry** because a later command succeeded. A failed
precondition with no mutation and a wrong-target success are different events even when
the final state looks the same.

**Maintaining the table.** Exercise the common rows in disposable repositories and
remotes: wrong-directory detection, mixed staging, stale test invalidation,
non-fast-forward rejection, conflicted merge, push-success with pull-request-failure,
cleanup refusal, concurrent change. A useful fixture asserts the pre-state, the command
effect, the preserved unrelated state, the retry gate and the postcondition. Never test
destructive fixtures on user data. Add a row when a failure has a distinct cause,
containment, retry eligibility or recovery owner; do not add one per wording variant of
the same error. Promote recurring modes into earlier precondition checks, automation or
policy, each with an owner and a regression fixture.

The target is not zero command failures. Safe refusals and clear blocks are valuable.
The target is no compounding after an unexpected result, no unsupported recovery claim,
and an intentional durable state or an explicit specialist handoff at closure.

## Workload Model

The unit of work is one repository, one identified branch or worktree, one requested
finish outcome, and one reviewable ownership scope. That unit may hold several commits,
packages or test commands when they form one causal story: one requested outcome,
changes that belong together, checks that cover the claimed behavior, one durability
destination, and a postcondition that can be verified without hiding partial failure.

**File count is only a diagnostic signal.** A reproducible generated update can touch
thousands of paths and stay conceptually narrow. A two-file change can be unsafe when
one file belongs to another user or holds an untracked secret. No fixed file-count
threshold is adopted. If the repository has measured limits for review size, CI
duration, hosting payloads or generated artifacts, use those local limits and record
their unit, scope and consequence.

| Dimension | Bounded signal | Pressure or split signal | Response |
| --- | --- | --- | --- |
| Repository identity | One verified root, no unexplained nested repository | Several repositories, unexpected nested metadata, uncertain root | Split by repository or route to a multi-repository orchestrator. Preserve local-only state first. |
| Branch and worktree identity | One named branch or deliberate detached commit in one known worktree | Several linked worktrees with relevant edits, branch checked out elsewhere, unclear active location | Inventory all relevant worktrees, identify the mutation target, stop if concurrent ownership cannot be resolved |
| Requested outcome | One of commit, push, pull request, local merge, keep, checkpoint, cleanup, confirmed discard | Incompatible outcomes, implied release or deployment, unresolved intent | Clarify or separate the transitions. One authorization never implies another. |
| Change ownership | Every staged, unstaged, untracked and conflict path in scope has one accountable owner | Unrelated changes, unknown hunks, another worker's files, mixed generated provenance | Narrow the staging, split, coordinate with the owner, or stop |
| Semantic scope | One behavior, maintenance objective or deliberate checkpoint with explainable coupling | Unrelated behaviors, several independent fixes, changes needing different reviewers | Split by behavior or review boundary unless policy requires an atomic change |
| Diff reviewability | Effective changes can be inspected directly or through a trustworthy generation-and-compare method | Unexplainable binary or generated output; rename detection obscures content; review tooling truncates | Establish provenance and an artifact-specific review method; checkpoint or split when the diff stays unknowable |
| Verification scope | Current commands cover the claimed tree and outcome; failures are attributable to the unit | Independently failing packages, prohibitively broad suites, unavailable environments, checks invalidated mid-action | Separate the claims, route the missing environment, or label a requested checkpoint incomplete |
| Destination topology | One verified base, upstream, remote or pull request destination | Several remotes or bases, protected targets, cross-fork ambiguity, several publication destinations | Split publication steps; verify authority for each destination; never silently pick a common remote name |
| Destructive reach | No deletion, or one exact target with explicit authorization and recovery evidence | Several branches or worktrees, local-only files, uncertain durability, broad cleanup | Full destructive gate; inventory every target; separate confirmation where consequences differ |
| External state | Remote CI, review and platform policy are current or explicitly pending with an owner | Stale or inaccessible checks, changing protection rules, concurrent merges | Refresh the state or route to the responsible authority |
| Concurrency | No relevant mutation since inspection, or changes are isolated and detected | Another process, agent, hook or user can modify the same index, branch, worktree or destination | Reinspect immediately before mutation; serialize conflicting writes; invalidate dependent evidence after any detected change |
| Recovery complexity | A failed action has a known, bounded retry or preservation path | Partial multi-target success, unknown history rewrite, repository damage, cleanup that would erase diagnostics | Stop expanding; route to recovery or orchestration first |

**Operating modes.**

| Mode | Use when | Evidence and action shape | Exit condition |
| --- | --- | --- | --- |
| Compact | Low-risk keep, status report, or scoped local commit with known identity and ownership | Requested outcome, repository and branch identity, dirty summary, scoped diff, relevant checks, intentional save, postcondition | The work is preserved at the stated location and the remaining state is named |
| Full | Push, pull request, local integration, shared branch, cleanup or discard | All compact evidence plus base, upstream, remote, policy, concurrency, recovery, remote checks, exact cleanup or discard target | Destination and durability verified; unrelated state preserved; pending ownership explicit |
| Sequenced | Several coherent units that do not need atomic publication | A separate evidence record and postcondition per unit; serialize mutations that share an index, branch, remote or checks | Every completed unit is independently durable; failed units have not contaminated later claims |
| Orchestrated | Repository policy defines a coordinated multi-package or multi-repository transition | Follow the named runbook: atomicity, ordering, approvals, rollback, partial-failure contract | The orchestrator's postconditions and this skill's branch-state handoff both pass |
| Blocked | Ownership, intent, integrity or destructive consequence is consequentially unknown | Preserve state; report observed facts and the missing decision; no speculative mutation | Resume only when the missing authority or evidence arrives; otherwise hand off terminally |

Choose the smallest mode that covers the real consequence. Do not downgrade a shared or
destructive operation because its diff is small. Do not force a large, coherent,
generated change into many arbitrary commits to satisfy a number. A useful split follows
an independent owner, behavior, destination, approval, verification scope or recovery
boundary.

**Split, checkpoint or route before mutation** when read-only inspection cannot resolve
any of these:

- two changes need different user outcomes, reviewers, owners or destination branches;
- a subset can be verified and preserved on its own while another subset is unfinished
  or failing;
- one action can succeed remotely while another fails locally, with no atomic rollback;
- generated, vendored, binary, submodule, sparse-checkout or large-file state cannot be
  tied to an intentional source change;
- a nested repository or linked worktree brings in a second index, branch or owner of
  local-only state;
- cleanup or discard would remove evidence needed to verify or recover another unit;
- state can change between observation and action and the conflict cannot be detected
  or serialized;
- you cannot describe one unambiguous postcondition for the whole batch.

Splitting does not mean dropping difficult state. Each unit keeps its own requested
outcome, owned scope, current checks, action, destination, recovery boundary and
postcondition.

**Repository features that distort apparent size.** Generated files inflate path and
line counts and hide whether the generator ran from the right source and version.
Vendored trees can be intentional snapshots or accidental broad updates. Submodules
carry a pointer in the parent and state in another repository. Sparse checkouts hide
tracked paths. Large-file systems show a small pointer while the object may be
unavailable. Rename detection can make a semantic replacement look like mass deletion
and creation. Nested repositories and linked worktrees place local-only changes outside
the current status output. Probe these only when status, configuration, instructions or
the diff says they matter. When one is present, use its own authoritative workflow and
report what was actually verified. Path-based ownership metadata and diff statistics
are signals, not proof.

**Examples.**

- Good compact: one feature worktree holds an owned source change and a focused test.
  The user asked for a local checkpoint. An unrelated untracked note is untouched. Save,
  verify the commit and residual status, and report that broader readiness is not
  claimed.
- Good full: one branch holds an owned feature plus reproducible generated output. The
  generator check explains the large diff, tests pass, one remote and base are verified,
  and the worktree remains after publication. High path volume does not make it
  multi-scope.
- Bad combined: one action commits two owners' changes, pushes to two remotes, merges
  locally, deploys and removes several worktrees. Partial success would make durability
  and recovery ambiguous. Split, or use a repository-defined orchestrator.
- Borderline monorepo: one behavior changes three packages, each with a different
  owner, and one suite is unavailable. Find out whether policy treats them as one atomic
  contract. Otherwise sequence reviewable units or keep a clearly incomplete checkpoint.

**Pre-mutation capacity record.** Before a full, sequenced, orchestrated or destructive
operation, record the scope unit, the pressure signals, the selected mode, the split
rationale, the relevant checks, the invalidation triggers and the postcondition owner.
Recheck branch, worktree and dirty state immediately before the write. If a
collaborator, hook, generator or tool changed the state, invalidate the affected diff,
ownership and test evidence and classify the workload again.

**Parallelism.** Read-only discovery may run in parallel across independent units.
Serialize writes that share an index, branch, worktree, remote destination or cleanup
target. The practical capacity limit is the largest unit whose intent, evidence, action,
failure recovery and postcondition stay coherent after that recheck.

**Recurring split reasons are maintenance inputs.** Repeated mixed ownership points to
weak worktree isolation. Repeated cross-package gating points to architectural coupling.
Repeated destination ambiguity calls for better repository instructions. None of them
is a reason to give the delivery flow broader standing authority.

## Reliability Target

Reliability means performing the transition the user asked for without losing or
absorbing unrelated work, then reporting only what current evidence supports. Three
independent dimensions:

- **State safety:** intended work stays durable, unrelated state is preserved, and any
  destructive action has exact authorization.
- **Outcome fidelity:** the resulting branch, commit, remote, pull request, merge, keep,
  cleanup or discard matches the selected outcome.
- **Evidence fidelity:** checks, destination, pending work, cleanup and readiness are
  described at their real scope and freshness.

A finish can preserve every byte and still fail outcome fidelity by pushing the wrong
commit. It can reach the right destination and fail evidence fidelity by claiming tests
that never ran.

**Per-operation invariants.** These are acceptance conditions for each operation, not
statistical objectives. No production rates were measured. "Every" and "no known" are
normative conditions. A known miss blocks the action or makes the result an incident
that needs containment and an explicit handoff.

| Invariant | Applies to | Passing condition | Primary evidence | Response to a breach |
| --- | --- | --- | --- | --- |
| Repository identity | Every operation | The command target, root, directory, worktree and branch or detached commit are the intended ones | Queries captured before mutation, checked again when concurrency matters | Stop; preserve diagnostics; find out whether an earlier mutation hit the wrong place |
| Owned scope | Every save, integration, cleanup, discard | Every included path or hunk is owned or explicitly authorized; unrelated and unknown state is excluded or stops the action | Staged and unstaged diff, untracked inventory, ownership classification, active-operation state | Unstage or narrow without discarding content; coordinate ownership or stop |
| Publication authorization | Every push | The repository's push rule is satisfied (in this repository: the user said "push") | The user's instruction, the instruction file | Do not push; if already pushed, report it at once |
| Message policy | Every commit | The message meets the repository's rules (in this repository: no issue numbers) | The message check on the tip and on the unpushed range | Amend before publishing; report if already published |
| Destructive authorization | Cleanup, discard, force, history-affecting recovery | The exact target and consequence were inventoried and explicitly authorized under current policy | The request or confirmation, policy, target identity, local-only state, recovery assessment | Do not execute; if executed, preserve what remains and route to recovery |
| Relevant quality claim | Any report that says complete, ready, integrated or verified | Current required checks cover the claimed tree and outcome, or the narrower pending state is stated | Command, tree scope, result, environment, order relative to later mutations | Retract the claim, rerun the checks, or label a requested checkpoint incomplete |
| Destination identity | Publication, pull request, integration, retention | The saved commit exists at the verified destination the user intended | Commit hash, ref, upstream, remote URL, pull request head and base, merge result | Stop further publication or cleanup; find the actual destination; correct only with authorization |
| Unrelated-state preservation | Every mutating operation | Pre-existing or concurrent user work is unchanged and visible unless explicitly included | Before-and-after status and diff, worktree inventory, scoped action record | Treat unexpected loss or change as an incident; no further cleanup; begin recovery |
| Postcondition closure | Every outcome | The observed final state matches the outcome; residual state is named; next owner or stop condition is clear | Post-action refs, status, log, worktree list, remote or pull request state, the handoff | Do not report completion; classify partial success; follow bounded recovery |
| Authority boundary | Every recommendation and exception | User authorization, policy, observed state, guide defaults, unread external pointers and synthesis are not conflated | A decision record linked to its source or observation | Reevaluate the decision under the real authority before further mutation |

Low-risk modes reduce the depth of evidence. They do not make preservation or
authorization optional. A local keep needs identity, dirty state, ownership, requested
outcome and a residual-state report. A push adds upstream, remote, commit and remote
postconditions. A local merge adds base identity and checks on the merged tree. Cleanup
and discard add exact targets, local-only inventory, durability, confirmation and
recovery boundaries.

**Verification pattern.** For each operation record:

1. the requested outcome and any explicit destructive authorization;
2. the risk mode and the invariants that apply;
3. pre-action repository, worktree, branch, dirty-state, ownership and destination
   evidence;
4. current checks with the tree they cover, and any pending or unavailable gate;
5. the exact action result, including partial success;
6. the post-action commit, destination, residual state, preserved unrelated work and
   cleanup status;
7. exceptions, recovery action, next owner, and evidence that must be refreshed.

Independent before-and-after observation is stronger than reusing the action's own
output.

**Contrastive outcomes.**

- Good: a pull request finish identifies repository and worktree, reviews the scoped
  diff, runs current checks, verifies remote and base, pushes the intended commit,
  confirms the pull request head, preserves an unrelated file, labels remote checks
  pending, and leaves cleanup to a later explicit decision.
- Bad: `git push` exits successfully, so completion is reported without noticing it
  went to another remote, and then the only worktree with an untracked file is removed.
- Borderline: an intentional commit preserves the requested changes and leaves
  unrelated state alone, but the handoff calls the branch merge-ready although the
  integration tests did not run. State safety passed. Evidence fidelity failed.

**When an invariant fails,** stop compounding the state. Preserve logs and remaining
local-only work, determine actual versus intended state, name the owner, and use the
retry or recovery guidance. Recurring failures should change a script, a hook, the
instruction file, a routing rule or a training example, with an owner and a fixture.

**What is firm and what is local.** Firm: preservation of unrelated state, exact
destructive authorization, current action-relevant evidence, verified destination,
honest postconditions. Local judgment: acceptable execution time, sample size, review
frequency, alert thresholds.

## Retry Backpressure Guidance

A retry is a new decision, not an automatic continuation of the failed command. Begin
only after the failure is classified and its actual effect is known. For a mutating
action the default is no automatic retry while effect, identity, ownership, idempotency,
authorization or destination is uncertain.

**The gate before every logical retry.**

1. **Classify.** Name the failure and whether the cause looks transient, a stale
   observation, missing authority, a policy denial, a state conflict, a permanent input
   error, or unknown.
2. **Requery.** Inspect actual local and remote state independently. A timeout or
   connection error does not prove the server did nothing.
3. **Refresh.** Recheck the mutable inputs: repository, worktree, branch, commit, index,
   dirty state, owner scope, base, upstream, remote, pull request state, policy, checks,
   and the user's outcome.
4. **Authorize.** Confirm that repeating is still within the request and the policy.
   Failure never creates permission for force, cleanup, discard, credential bypass or
   broader scope.
5. **Budget.** Apply the repository's or platform's retry policy. If none exists, make
   one conservative, bounded attempt, only for a classified harmless or transient case.
   No universal schedule is given here.
6. **Attempt.** Perform one logical action, counting retries hidden inside wrappers or
   clients when their behavior is known.
7. **Verify.** Query the postcondition. Stop on success, a changed precondition, an
   unknown effect, a permanent failure, or an exhausted budget.

The budget belongs to the requested transition, not to each nested command. A wrapper
that retries several times inside an outer loop that also retries multiplies the
effects while both layers claim a small limit. Budgets must also count repeated
discovery, corrected staging, check reruns, recovery and reviewer clarification.

| Operation class | Ordinary retry eligibility | Observe before retrying | Pacing and budget source | Hard stop |
| --- | --- | --- | --- | --- |
| Deterministic local read | Only when the failure is environmental or state changed deliberately; repeating the same syntax error adds nothing | Path, command availability, permissions, whether state changed | Local tool policy; usually fix the cause instead of backing off | The same permanent input error, access denial, or evidence the command targets the wrong repository |
| Remote read or status query | Bounded retry for a classified transient transport, availability or eventual-consistency case | Endpoint identity, authentication boundary, last known commit, response class | Platform or repository client policy, including rate-limit guidance | Permission or policy denial, changing destination, exhausted budget, a result no longer relevant to the same commit |
| Local check or test | Rerun after a deliberate code, config or environment change, or under a named flaky-test rule. Not "until green". | Current tree, command scope, environment, prior failure, the change meant to affect it | Repository test policy; a flaky retry needs a named rule and keeps the first failure on record | Unexplained nondeterminism, an unrelated failure, changed ownership, repeated failure with no new hypothesis |
| Local commit or hook | Only after inspecting index, history, hook effects and identity or signing state, and fixing the specific cause | Staged diff, current head, whether a commit exists, files changed by hooks, the policy error | Repository hook and signing policy; no blind outer loop | Unknown hook mutation, an unexpected commit, unowned staged content, a request that no longer matches the index |
| Push with an explicit no-effect rejection | Bounded retry after authorized divergence resolution or a verified transient pre-transfer failure | Local commit, upstream and remote mapping, actual remote ref, rejection class, policy | Git host and repository policy; the history strategy must be explicit | Non-fast-forward without an authorized integration strategy, protected-branch denial, wrong remote, changed remote ref |
| Push with an ambiguous transport result | Do not repeat until the destination is queried | Intended commit, actual remote ref if observable, client retry behavior, credential and network state | Wait and requery before spending any write budget | Effect cannot be determined, destination mismatch, any sign of partial or wrong-target publication |
| Pull request create or update | Only after searching for an existing equivalent and revalidating head, base, repository, title and body intent, permissions | Published head commit, selected base, existing requests, the first response | Platform idempotency and rate-limit policy, once read | A duplicate or conflicting request, unknown first effect, changed head or base, access or policy failure |
| Asynchronous CI or review | Prefer wait and observe; do not mutate to make a pending gate finish | Check or review identity, commit covered, current status, expected owner | Repository polling cadence or event notification; respect service limits | The check covers a stale commit, terminal failure, approval required, the wait exceeds the owned handoff window |
| Local merge or rebase | No ordinary retry after a conflict or partial history change; classify the active operation and route | Current heads, active operation, conflict stages, unrelated state, intended base | The conflict or recovery procedure, not a time backoff | Unresolved content, ambiguous history objective, shared-history consequence, policy requiring review |
| Cleanup or branch or worktree removal | Only after the cause of the protective refusal is intentionally resolved and every destructive precondition is reverified | Exact target, current worktree list, dirty and local-only state, durable destination, authorization | Explicit cleanup policy and current intent; no autonomous repetition | Target changed, state still dirty or unique, durability uncertain, any refusal with unknown effect |
| Discard, reset, force, destructive recovery | Never automatically | Complete current-state inventory, exact authorization, recovery evidence, specialist procedure | Each attempt needs a fresh explicit decision | Any partial effect, ownership uncertainty, recovery uncertainty, target drift, missing authority |

**Backpressure states.**

- **Proceed:** the previous attempt had a known harmless effect or none; all
  consequential preconditions still hold; policy authorizes another bounded attempt.
- **Observe:** the remote or asynchronous system may converge without a write. Wait or
  query at the policy cadence while the local durable commit is preserved.
- **Checkpoint:** the work can be saved intentionally but publication, integration or
  readiness is blocked. Report the narrower status.
- **Hold:** a mutable input changed or a required observation is unavailable. No new
  finish mutations until evidence is refreshed.
- **Escalate:** identity, ownership, policy, integrity, shared history, destructive
  impact or an unknown server effect needs another owner.
- **Terminate:** the original outcome is no longer authorized, possible or appropriate.
  Preserve the best known state and give a terminal handoff.

**Backpressure applies to scope as well.** Do not start implementation, widen staging,
switch remotes, change history strategy, remove worktrees or add cleanup because the
requested finish is blocked. Those are separate decisions and can erase evidence or
expand authority. In a shared workspace one owner coordinates each mutating branch or
worktree unit, while other agents do read-only analysis that is reconciled before
action.

**Examples.**

- Safe read retry: a remote-status query gets a classified temporary transport error.
  Repository, endpoint, commit and authorization are unchanged. Retry under the client
  policy, then mark the status observed or still unavailable. Do not infer readiness
  from a cached result.
- Ambiguous write: pull request creation times out after the branch was published.
  Query existing requests for the verified head and base. If the query is unavailable,
  keep the branch and report publication-only partial success.
- Permanent policy denial: a protected branch rejects a direct push. Repeating with
  other credentials or force is not backoff. Keep the commit and route to the pull
  request or maintainer procedure.
- Hook mutation: a commit hook reformats files and then fails. Inspect index and tree,
  review ownership, rerun the checks, then decide. Repeating at once can compound the
  modifications.
- Destructive refusal: worktree removal refuses because local changes exist. That is a
  successful safety signal. Inventory and preserve the changes. No force flag, no retry,
  until cleanup intent and durability are established.
- Borderline persistence: a harmless remote read stays unavailable after the local
  budget. Continuing forever changes nothing but monopolizes the workflow and delays a
  clear pending handoff. Escalate or stop with an owner and a follow-up.

**Retry ledger** for any consequential retry sequence:

| Field | Content |
| --- | --- |
| Transition identity | Requested outcome, repository and worktree, branch, commit, destination |
| Failure class | The failure row, the client result, the classified actual effect |
| Attempt budget | The governing policy, or the conservative rationale when no numeric policy exists |
| Hidden attempts | Known retries by a client, wrapper, hook or subprocess |
| Refreshed inputs | State and authority observations repeated since the previous attempt |
| Change since failure | New evidence, corrected input, elapsed external condition, or approved recovery decision that justifies another attempt |
| Attempt result | Exact local and remote effect, including partial or unknown state |
| Stop reason | Verified success, changed state, permanent denial, unknown effect, exhausted budget, escalation, terminated outcome |

Every attempt should add evidence or reduce uncertainty. If the same inputs are applied
to unchanged, unknown state with no policy-backed reason, stop. No universal seconds,
jitter or attempt counts are asserted. Repository-owned tooling may encode stronger
guarantees: verify its version, idempotency and failure behavior before relying on it.

Aggregate exhausted budgets, prevented duplicates, changed-state stops and hidden retry
counts by operation class. Recurring remote ambiguity may justify an idempotent wrapper
or a destination lookup. Recurring hook mutation may justify clearer hook output and
fixtures. Recurring policy denial may mean the default route is wrong. Improvements
should reduce uncertainty before the retry, not raise the allowed attempt count.

## Observability Checklist

Observe the transition, not only the commands. A useful record lets a reviewer
reconstruct what the user asked for, which state was inspected, what was authorized,
what changed, where the work became durable, what remains, and which evidence is
current. Use one transition identity (an operation ID, a journal entry, a handoff key)
to tie the precondition, action, retry, failure and postcondition records together. The
identity is not authorization and must not expose a secret.

**Core transition record.**

| Field | Content | Why it matters | Privacy or freshness boundary |
| --- | --- | --- | --- |
| Requested outcome | Commit, push, pull request, local merge, keep, checkpoint, cleanup, confirmed discard, or blocked handoff | Anchors every action to intent; stops adjacent actions being inferred | Record the meaning of the request, not unrelated conversation |
| Repository identity | Verified root and a non-secret repository identity | Catches wrong-directory, nested-repository and wrong-destination errors | Redact credentials in URLs; never copy tokens |
| Worktree identity | Working directory, linked worktree path, branch or detached state | Separates several checkouts and names the index being changed | Paths can be sensitive in shared reports; shorten in an approved way |
| Commit before | Current commit and any active operation before the mutation | History baseline; supports recovery | Refresh after checkout, commit, merge, rebase, reset or concurrent update |
| Dirty and conflict state | Staged, unstaged, untracked, conflict and submodule summary | Exposes local-only state and ownership pressure | Summarize paths and classes; no file contents unless required and authorized |
| Owned scope | Included paths or hunks, excluded unrelated state, unknown-ownership blockers | Proves staging or cleanup did not absorb another owner's work | Ownership is a current judgment; refresh after a scope change |
| Policy basis | The repository instruction, the user's authorization, any guide default, any labeled inference | Separates authority from advice and from observed state | Record only the consequential sources |
| Verification evidence | Exact command or review method, covered tree, environment where it matters, result, order relative to mutations | Prevents stale tests and command-name-only claims | Summarize output; keep a bounded pointer to diagnostics; no secrets |
| Chosen action | The exact operation and target, including whether cleanup is excluded | Connects the decision to the mutation; makes partial success visible | Omit command text with sensitive arguments; keep the safe meaning |
| Action result | Success, failure, partial, wrong-target or unknown effect, plus immutable identifiers | Separates activity from actual state change | Capture server identifiers only where access policy allows |
| Destination state | Resulting commit and ref, remote and upstream, pull request head and base, merge target, kept worktree, or removed target | Verifies durability and outcome fidelity | Remote observations go stale after later publication or platform changes |
| Residual state | Remaining tracked and untracked work, pending checks and review, kept branch and worktree, cleanup trigger, recovery limit | Stops "clean" or "done" hiding unfinished or unrelated state | Mark absent fields as inapplicable, unavailable, redacted or blocked, with a reason |
| Next owner and stop | The person, workflow or event responsible for the pending action, and the condition for resuming or closing | Turns uncertainty into an actionable handoff | Use repository roles when they are enough |

For a read-only recommendation record only the fields that explain the decision. For
every mutation use the core record and extend it:

| Operation | Additional fields |
| --- | --- |
| Scoped commit | Staged diff identity, commit message intent, message-check result, resulting hash, hook and signing result, residual dirty state |
| Push | The user's push authorization, verified upstream and remote, local commit, pre-push remote ref where relevant, push result, actual destination ref, any policy rejection |
| Pull request | Published head commit, verified base, lookup for an existing request after an ambiguous failure, resulting identity, remote checks and review state, kept cleanup state |
| Local merge | Source and base identities, pre-merge state, outcome of the active operation, resulting history, checks on the merged tree, disposition of source branch and worktree |
| Keep or checkpoint | Exact durable or local-only location, checks that did and did not run, why the narrower state is intentional, trigger for finishing later |
| Worktree creation | Directory choice and why, ignore check result, setup command, baseline test result |
| Cleanup | Exact branch or worktree target, verified durable destination, local-only inventory, authorization, removal result, unaffected remaining worktrees |
| Discard | Inventoried content and consequence shown for confirmation, the exact authorization, recovery limits, final absence of the target, preserved unrelated state |
| Retry or recovery | Failure class, actual prior effect, logical attempt budget, hidden client attempts, refreshed inputs, selected correction, stop reason, closure evidence |

**Event order to preserve.**

1. Observed intent and applicable policy.
2. Repository and worktree identity and pre-action state.
3. Ownership and selected workload mode.
4. Current verification evidence.
5. Authorized action and target.
6. Command or platform result, including ambiguous and partial effects.
7. Independently observed postcondition.
8. Remaining state, pending evidence, cleanup status, next owner.

Timestamps help correlate concurrent activity, but order relative to mutation is the
essential fact. A test result gathered before a later merge or generated-file update
cannot verify the resulting tree, however recent its timestamp. Record the tree and the
invalidating event, not time alone.

**Redaction and size.** Never put credentials, tokens, private keys, signing material,
secret environment values, credential-bearing URLs or unnecessary file contents in a
finish record. Treat command output and diffs as potentially sensitive. Keep a
non-secret destination identity or an approved opaque reference so that a wrong-target
diagnosis stays possible. Prefer:

- status and diff summaries with reviewed path lists over full source dumps;
- command name, scope, result and a protected pointer over unbounded transcripts;
- immutable commit or platform identifiers over screenshots;
- a concise failure meaning plus the location of the raw evidence over repeated copies
  of the same log;
- explicit unresolved-risk notes over a generic "successful" or "clean".

During severe containment raw evidence may be captured first, when summarizing would
risk loss. Move it promptly into authorized storage and write the structured record once
the state is stable. Storage, access, retention and deletion follow the repository's and
organization's policy; no retention period is asserted here.

**Compact example.**

| Item | Value |
| --- | --- |
| Outcome | Create a pull request; cleanup not requested |
| Identity | Verified repository and linked feature worktree; feature branch at commit `abc1234` |
| Scope | Three owned source and test paths; one unrelated untracked note excluded |
| Checks | Repository unit and lint commands passed on tree `abc1234`; remote CI pending |
| Destination | Verified fork remote and intended base; remote head observed at `abc1234` |
| Action result | Push verified; one pull request created for the expected head and base |
| Preservation | Unrelated note still present; branch and worktree kept |
| Pending | Remote CI and review owned by the pull request workflow; no merge or release claim |
| Next step | Review the request; reassess cleanup only after durable integration and explicit intent |

Bad observability is a raw transcript with a credential in it and pages of successful
output, but no requested outcome, branch commit or destination postcondition.
Borderline observability lists `git status`, the tests and `git push` with zero exit
codes and never records which remote ref advanced or whether unrelated state remained.
Activity is not an observed transition.

**Long-running work.** Checkpoint after each durable unit and before a consequential
mutation. The checkpoint holds: repository and worktree identities, immutable commits,
dirty and ownership state, evidence freshness, the selected outcome, open risks, the
retry budget, the next step. On resume, reread the policy and requery mutable state. A
remembered branch head, remote, pull request or check result is not authoritative.
Context drift invalidates evidence; it becomes a reliability failure only when stale
context drives a mutation or an unsupported claim. For the journal itself use
[tdd-progress-and-resume](../tir-tdd-progress-and-resume/SKILL.md).

**Limits.** Logs cannot prove that no uninstrumented writer exists. Repositories that
need stronger guarantees enforce permissions, protected refs, queue ownership or hooks.

**Reviewer reconstruction test.** In disposable repositories exercise complete,
partial, ambiguous and blocked transitions, use synthetic secrets to test redaction, and
ask an independent reviewer to identify: the intended outcome and authority; the exact
state and destination affected; the evidence behind the completion claim; the unrelated
state that was preserved; any pending or unavailable gate and its consequence; the next
owner and the safe retry or recovery boundary. If the reviewer cannot, the record is
incomplete even if it matches a schema. Tools should emit commit, destination and
postcondition fields directly; parsing them later from prose is less reliable. Keep the
core fields stable and allow namespaced repository-specific extensions (submodules,
large-file storage, protected environments, release gates, regulated approvals), with
versioned schema changes and maintained redaction fixtures.

## Performance Verification Method

No benchmark data exists for this flow. Latency, throughput and productivity: not
measured. Measure only to answer a named decision, for example whether a
destination-verification helper reduces rework, whether a structured handoff shortens
reviewer reconstruction, or whether a wrapper improves end-to-end finish time without
weakening checks.

**Correctness is the constraint, not a metric to average against speed.** Every
evaluated run must still satisfy state safety, outcome fidelity and evidence fidelity.
An unauthorized action, a loss of unrelated state, a wrong destination, a stale
readiness claim or an unverifiable postcondition cancels the performance win for that
run and is reported separately as an incident.

**Boundaries.**

- Start: the actionable request and the required repository context are available.
- Stop, success: the selected outcome has a verified durable postcondition and a concise
  handoff with residual state and next owner.
- Stop, blocked: state is preserved and there is an explicit blocker, consequence,
  owner and safe resumption condition.
- Stop, failure: an invariant is breached, the outcome is wrong or unknown, or recovery
  ownership is required.

Do not stop the clock at the last Git command if destination verification and handoff
remain. Do not start it before the request exists. Record active handling time and
external waiting time separately when CI, review, network recovery or human
authorization matters.

| Evaluation mode | Best use | Strengths | Limits |
| --- | --- | --- | --- |
| Disposable fixture | Command mechanics, state detection, staging, retries, cleanup refusal, postcondition checks | Repeatable, controlled faults, no risk to user data | May not represent large repositories, real permissions, networks or human review |
| Shadow decision review | Compare route, gate and stop decisions without letting the candidate mutate state | Tests decision clarity and reviewer agreement on real cases at low risk | Cannot measure execution or side effects; needs an independent rubric |
| Observational cohort | Real end-to-end operations before and after, or across versions | Captures platform, policy, reviewer and repository variability | Confounding, privacy, changing workload mix, survivorship |
| Repository-owned controlled rollout | A mature wrapper or policy change under current governance | Realistic conditions with staged exposure and rollback ownership | Needs authorization, monitoring and a fallback; never for destructive paths casually |
| Expert walkthrough | Rare, high-consequence or thinly sampled operations | Reveals missing decisions, recovery ambiguity, cognitive load | Qualitative; no stable latency distribution |

Use fixtures for destructive behavior and injected faults. Do not benchmark cleanup,
discard, reset or force against user repositories. Use shadow or expert review when a
candidate changes authority, routing or destructive decisions.

**Measurement packet.**

| Field | Definition |
| --- | --- |
| Hypothesis | The mechanism and expected result, for example "verified remote lookup reduces wrong-destination rework" |
| Decision owner | The person or role authorized to act on the result |
| Variant identity | Exact guide, script, tool, configuration and version compared |
| Operation population | Included outcomes, repositories, and time window or fixture set |
| Workload dimensions | Mode, diff reviewability, ownership, checks, destinations, concurrency, generated or submodule state, consequence |
| Start and stop events | Observable events for success, blocked and failure |
| Invariant results | State safety, outcome fidelity, evidence fidelity; every breach kept as an incident |
| Active and wait time | Operator and tool handling separated from CI, review, rate-limit, network and authorization waits |
| Attempts and rework | Logical retries including hidden client attempts, repeated discovery, corrected staging, reruns, recovery, reviewer clarification |
| Exclusions and censoring | Every omitted, abandoned, timed-out, inaccessible or incomplete operation, with its reason |
| Environment | Repository and tool versions, host conditions, cache state, network locality, policy or check changes |
| Analysis method | Descriptive summary, paired comparison, distribution, or another method justified by the sample |
| Uncertainty | Sampling limits, confounding, missing evidence, and the scope beyond which the result must not be generalized |
| Retention and privacy | Approved data location, redaction, access and lifecycle |

Changed-file count, source count and tool-call count describe context. They are not
default outcomes. A large generated diff may be easy to verify; fewer tool calls may
mean checks were skipped; more reading may prevent a costly wrong-base action.

| Candidate outcome | Interpretation |
| --- | --- |
| Verified transition elapsed | Start to verified success or explicit blocked handoff; report the outcome type, do not pool |
| Active handling time | Inspecting, deciding, executing, verifying, reporting; external waits excluded |
| Reviewer reconstruction time | Time for an independent reviewer to identify request, target, evidence, result, residual state, next action |
| Clarification count | Extra consequential questions needed because guidance or handoff omitted intent, ownership, destination or evidence |
| Logical retry count | Retries for the transition across wrappers and clients, by failure class |
| Rework and recovery | Repeated staging, checks rerun after avoidable invalidation, wrong-target correction, duplicate cleanup, incident recovery |
| Blocked handoff quality | Whether the stop preserved state and named consequence, owner and resumption condition |
| Invariant incidents | Absolute count and details; never hidden in an average |

Percentiles need a representative sample and a defined treatment of ties, censored runs
and workload changes. With sparse data report individual cases, range and uncertainty.
Compare like with like: segment by outcome and mode first, then by repository shape,
generated files, submodules, check suite, cache warmth, network, host, provider,
permissions, CI queue, review wait, concurrency and policy changes. Include blocked,
failed, abandoned and recovered runs. Separate a terminal policy denial from a transient
network delay, user wait from tool handling, and a safe early stop from inability to
finish.

**Examples.**

- Valid: on the same disposable pull request fixtures, compare the existing process
  with a helper that emits verified remote, head, base and destination postconditions.
  Inject a no-effect rejection and an ambiguous create response. Measure active
  handling, logical attempts, wrong-destination prevention and reviewer reconstruction.
  Require all invariants in both variants.
- Invalid: claim a faster finish because the new path runs fewer commands after
  removing integration tests and destination verification.
- Borderline: report a lower median for successful operations while leaving out blocked
  and failed cases. Reanalyze the full cohort.
- Nuanced: a workflow has a slower median but removes rare, expensive cleanup recovery.
  Report both the central distribution and the incident tail.

**Pass and fail.** A claim passes when the packet is complete enough to reproduce the
cohort and boundaries, the named outcome improves under the stated analysis, no
invariant regresses, failures and missing runs are accounted for, and uncertainty does
not exceed the claim. It fails when it relies on tool-call count alone, mixes
incompatible outcomes, reports unsupported percentiles, excludes inconvenient failures,
changes verification coverage, uses stale or incomparable state, or treats speed as
compensation for an authorization or preservation breach. A null or uncertain result is
not a process failure; it means the evidence does not support the change on performance
grounds. Keep the packet with the result and the tool version, and reevaluate after
material changes to repository topology, platform behavior, policy, checks, the wrapper
or the workload mix.

## Scale Boundary Statement

The flow is sufficient for one coherent branch or worktree transition: one accountable
mutation owner, one reviewable ownership scope, one requested outcome, and a
postcondition verifiable from current local and destination state. It can also sequence
several such units when each stays independently durable and partial results are
visible.

It stops being the controlling procedure when the outcome depends on atomic
cross-repository publication, coordinated schema or data migration, multi-environment
release, shared-history rewrite across owners, production rollout, platform
administration, repository-integrity recovery, or conflict resolution with unresolved
content ownership. It may still prepare or preserve individual branches, but an
orchestrator or specialist procedure owns global ordering, approvals, partial-failure
handling and closure.

**Scale is the count of independently mutable truths,** not of changed files:

- repository roots and indexes;
- branches, worktrees and active Git operations;
- change owners and review authorities;
- bases, upstreams, remotes, remote refs and pull request destinations;
- verification environments and approval domains;
- cleanup or destructive targets;
- concurrent writers and long-running contexts;
- outcomes that can succeed or fail independently;
- recovery owners and externally visible effects.

A large reproducible generated change can stay one unit. Two small changes with
different owners and destinations may need coordination.

| Scale mode | Entry condition | Mutation ownership | Verification and closure | Boundary |
| --- | --- | --- | --- | --- |
| Single unit | One repository and worktree, owned scope, one outcome and destination | One accountable writer for the index, branch and target | This flow verifies preconditions, action, postcondition, handoff | Default |
| Sequenced units | Several units that are durable and reviewable independently but share ordering or later integration | One writer per unit; a coordinator controls sequence and shared-target mutation | Each unit closes independently; shared integration then gets refreshed checks | Use when visible partial progress is acceptable |
| Independent parallel units | Repositories, worktrees, destinations and outcomes share no mutable resource or ordering | One owner per isolated unit; nobody assumes another unit's state | Per-unit evidence and postconditions stay separate; the global report aggregates without overwriting | Stop parallelism when a shared dependency or destination appears |
| Merge queue or serialized integration | Many source units target one shared base under a repository-owned queue | Workers prepare source commits; only the queue or a designated integrator changes the shared base | Source checks plus queue or merged-tree checks; resulting order and failures observable | Verify the current queue policy; do not infer release completion |
| Explicit orchestration | A cross-repository, cross-package, migration, release or platform workflow has a current runbook | The orchestrator assigns owners and controls shared mutations | Per-unit durable outputs plus global approvals, ordering, rollback or roll-forward, final outcome evidence | This flow becomes a subordinate branch-state procedure |
| Blocked, unowned scale | Shared resources, atomicity, authority or recovery cannot be established | No speculative writer | Preserve every unit; publish a dependency and risk inventory; request an owner | Do not improvise coordination through force or broad access |

**Coordination invariants.**

1. One accountable mutation owner at a time for each shared index, branch, worktree,
   remote ref, pull request target and cleanup target, unless an authoritative tool
   gives stronger concurrency guarantees.
2. Read-only discovery may run in parallel, but its result carries the identity of the
   state it observed. Refresh before acting if another unit can change that state.
3. Ownership transfers only at a durable checkpoint that names the immutable commit,
   dirty and local-only state, checks, pending risks, destination and next authorized
   action.
4. A write to a shared target compares the current state with the state the decision
   was based on. A mismatch fails closed and returns to classification. It does not
   authorize force.
5. No worker cleans a branch or worktree while another unit, reviewer, queue, recovery
   process or orchestrator depends on its local-only state or diagnostics.
6. A source-unit success does not prove integrated, release or production success. Each
   global layer verifies its own resulting state.
7. Partial success stays visible. Do not delete or rewrite durable shared effects to
   make the aggregate look atomic unless the orchestrator's recovery policy says so.

**Worktrees are not enough.** Separate worktrees protect working directories and
indexes. Workers can still race on one remote ref, choose inconsistent bases, open
duplicate pull requests, or delete a worktree another workflow needs. Conversely, one
person can safely own several units when mutations are sequenced and every handoff is
current.

**Handoff to sequencing or orchestration.**

| Field | Content |
| --- | --- |
| Global outcome | The exact objective, and what this branch-level procedure is and is not authorized to do |
| Unit inventory | Repository, worktree, branch, immutable commit, owner, dirty and local-only state, requested unit outcome |
| Dependency order | Compatibility, migration, generation, integration or release dependencies, with reasons |
| Shared resources | Bases, remote refs, pull request targets, environments, credentials or permissions, cleanup targets that need serialization |
| Current evidence | Per-unit checks, review state, policy basis, observations invalidated by later units |
| Coordination control | Writer owner, lock, lease or merge-queue mechanism, expiry and recovery owner, state-version comparison |
| Partial-failure contract | Which unit effects may remain, how they are reported, authorized roll-forward or compensation, terminal escalation |
| Global closure | Integrated commit or release identity, checks and approvals on the result, residual units, cleanup status, next owner |

Locks and leases need a current owner, a protected identity, evidence of acquisition and
release, expiry semantics and a recovery procedure. Age does not prove abandonment. With
no coordination mechanism, serialize mutation through explicit human or workflow
handoff.

**Large repositories and monorepos.** Narrow discovery to the owned behavior and its
checks, generated outputs, dependencies and reviewers. Dependency graphs, ownership
metadata, pathspecs and diff statistics reduce search; each is a signal, not proof. If
package boundaries have independent checks or owners, model them as sequenced units
unless policy declares an atomic contract. Submodules and nested repositories are
separate repository identities even when only a pointer changes in the parent diff. An
orchestrated finish states which layer owns each verification and destination.

**Examples.**

- Good parallel preparation: two independent features in separate worktrees and
  branches with separate owners. Each produces a reviewed immutable commit and a check
  record. Only the merge queue updates the shared base and reruns merged checks. Source
  workers keep their worktrees until queue durability and policy allow removal.
- Bad distributed finish: three agents stage and commit in one worktree, each trusting
  an earlier status snapshot, then all push and clean up. Nobody can say which diff,
  tests or deletion belonged to which request.
- Borderline isolation: workers use separate worktrees but push different commits to
  the same remote branch. Filesystem isolation worked; destination ownership did not.
  Add serialization or separate destination refs.
- Coordinated cross-repository change: a client and a service need compatible commits
  and a migration sequence. Preserve and verify each branch with this flow, then hand
  immutable commits and the dependency order to the release or migration orchestrator.
  Do not simulate atomicity with ad hoc resets.

**Fixtures.** In disposable repositories and remotes exercise two-writer state-version
mismatches, merge-queue reorder, cancellation, owner transfer, stale checkpoint resume,
cleanup while another unit depends on a worktree, and partial remote success. Assert
that conflicting mutation fails closed, every durable commit stays discoverable,
unrelated state survives, and the global record identifies partial outcomes.

The portable rule: partition by authority and postcondition, hand off immutable
commits, give each shared target one accountable writer, persist context at durable
boundaries, and verify the globally resulting state before cleanup or stronger
completion claims. Technology choice, throughput limits, timeouts and recovery
mechanisms are local decisions.

## Outcome Metrics and Feedback Loops

The leading indicator: the next task makes a better delivery decision with less
ambiguity. Measure that through the requested transition and its invariants, not through
one score.

| Outcome layer | Observable signal | How to collect | Interpretation boundary | Response to failure |
| --- | --- | --- | --- | --- |
| Policy use | The workflow and commands match the user's intent and the repository's rules | Decision record with policy references | Process evidence does not prove live state or action success | Correct the authority mapping; reopen dependent decisions |
| Scope accuracy | Every staged or removed path is intended; unrelated tracked and untracked state remains | Pre-state inventory, staged diff, post-state comparison, owner review | Git cannot determine human ownership | Contain publication or cleanup, restore when possible, repair staging rules |
| Readiness truthfulness | Checks support exactly the claimed checkpoint, publication, merge or release status | Commands, tree identity, sequence, pending-gate record | Passing local checks does not predict every remote result | Narrow the claim, fix failures, or preserve as a non-ready checkpoint |
| Transition accuracy | The agent performed the explicit or selected outcome | Requested outcome compared with command and hosting results | A command can succeed against the wrong valid branch or remote | Stop, preserve evidence, recover, repair target discovery |
| Postcondition match | Expected commit, branch, remote, pull request, base, worktree and dirty state are observed afterwards | Outcome-specific status, log, upstream, hosting, worktree inspection | Asynchronous checks may stay pending | Assign pending ownership or treat the mismatch as an incomplete transition |
| Recovery preservation | Recovery references and local-only state remain until intentionally retired | Branch, commit, worktree, remote and backup inventory | The reflog does not guarantee recovery of untracked or expired objects | Preserve more state, disclose limits, or block cleanup |
| Handoff closure | The report names what was saved, where, checks, unrelated state, pending work, cleanup trigger, next owner | A fresh agent or reviewer reconstructs the transition | A clear report cannot repair an unsafe action | Repair state first, then the handoff and the repository guidance |
| Lifecycle health | Kept branches and worktrees have owners and retirement triggers; obsolete state is cleaned deliberately | Periodic or event-triggered inventory chosen by the repository's owners | Age alone does not prove it is safe to delete | Find the owner and the durable outcome before reviewed cleanup |

**Failure signals:** a clean tree produced by mixed staging; a successful push to the
wrong destination; a push nobody asked for; an issue number in a published commit
message; green tests attached to an older tree; a pull request called ready while
checks are pending; a worktree removed before its local-only files were inventoried;
kept state with no owner.

**Proxies to avoid.** Commit count does not measure scope quality. Pull request count
does not measure review readiness. Test pass rate does not measure authorization. A
short finish time does not measure recovery. Clean-tree rate can reward sweeping
evidence away. One irreversible wrong-scope deletion can outweigh many routine
successes.

**Candidate audit metrics** (none has a measured baseline; no numeric threshold is
asserted):

| Metric | Numerator / denominator | Useful segmentation | Boundary |
| --- | --- | --- | --- |
| Correct outcome routing | Sampled operations whose route and outcome match an independent reviewer's verdict / all reviewed samples | Direct request, unknown intent, conflict, release, recovery, destructive path | Reviewer agreement is a process signal, not proof about unreviewed operations |
| Precondition escape | Operations with a postcondition mismatch traced to wrong identity, ownership, base, remote or stale checks / all completed operations | Compact, full, sequenced, destructive | A low rate does not permit skipping preconditions; every escape needs causal remediation |
| Unrelated-state incident | Operations that unexpectedly modify or lose out-of-scope state / all mutating operations | Staging method, worktree layout, concurrent activity | The invariant is no known incident; report absolute cases as well as any rate |
| Unsupported readiness claim | Handoffs corrected because check, review, CI, merge or release evidence was absent or stale / all audited readiness claims | Local versus remote claim, checkpoint versus complete | Measures communication and evidence fidelity, not defect density |
| Partial-transition recovery | Partial actions restored or advanced to an intentional durable state / all partial transitions | Push, pull request, merge, cleanup | A successful recovery does not make the initiating failure harmless; keep the root-cause class |
| Routing rework | Handoffs needing repeated discovery, circular transfer, or losing context / all routed operations | Destination procedure, missing transfer field | Points to a weak routing map or transfer bundle, not operator speed |

A team may adopt a numeric target only after defining population, rubric, window,
owner, confidence limits and remediation. A percentage without the absolute count can
hide a serious rare event. Define the baseline before claiming improvement: pre-state,
expected transition, unrelated-state invariant, quality claim, postcondition, observer,
guide version, repository policy. Report raw cases and error categories before
percentages. Keep incident-level detail for safety breaches and aggregate only data
that exposes no secrets or private content.

**Close the loop at the layer that owns the defect.**

1. Wrong intent mapping: direct-request and menu behavior.
2. Wrong scope: ownership inventory and staging tooling.
3. Stale quality evidence: invalidation rules and project checks.
4. Wrong target: the repository's base, remote and upstream policy.
5. Premature cleanup: publication-cleanup separation and recovery gates.
6. Incomplete handoff: the report schema and next-owner contract.
7. Recurring ambiguity: the instruction file or safer automation.

Retire a metric that never changes an action or duplicates stronger evidence. Promote a
new gate after a severe escape or a recurring failure. Review the flow when a source or
policy changes, a failure repeats, hosting behavior changes, or consequence rises.
Repository owners may set an inventory cadence for quiet worktree accumulation; no
interval is asserted.

## Completeness Checklist

An index to evidence, not proof by enumeration. Complete can still be wrong, stale,
unauthorized or unsafe.

**Reader and decision**

- [ ] The starting state, the requested or unknown outcome, and the consequence are named.
- [ ] A direct commit, push, draft pull request, keep, checkpoint, cleanup or discard
      request was honored without a redundant menu, after the safety gates.
- [ ] An unknown outcome received the four-option choice after finishability was
      established.
- [ ] The next state, the stop condition and the next owner are observable.

**Authority**

- [ ] User authorization, repository policy, observed state, guide defaults, external
      evidence and synthesis are kept distinct.
- [ ] Repository-specific bases, remotes, checks, push rules, message rules and cleanup
      rules replaced the generic defaults.
- [ ] The pull-request cleanup conflict was resolved conservatively unless current
      policy or explicit intent says otherwise.

**State and ownership**

- [ ] Root, working directory, branch or detached state and linked worktree were
      identified before mutation.
- [ ] Staged, unstaged, untracked, conflict and submodule state were inventoried.
- [ ] Every path or hunk in the save scope has an ownership class; unrelated and
      unknown work is untouched or stopped the action.
- [ ] Base, upstream and remote were verified when the transition needed them; common
      names were not assumed.
- [ ] Any mutation after capture reopened the dependent status, diff and quality
      evidence.

**Quality and readiness**

- [ ] Repository-defined checks ran against the relevant tree; their coverage is
      reported.
- [ ] A failing or unrun gate blocked the ready claim, unless the user asked for a
      labeled checkpoint.
- [ ] Local checks, remote CI, review, merge readiness and release readiness are
      reported as separate states.
- [ ] Tests were not used as a substitute for scope, ownership, authorization,
      destination or postcondition evidence.

**Transition**

- [ ] The action matches the explicit request or the selected option.
- [ ] Commit scope and message are intentional; broad staging happened only when every
      change was reviewed and owned.
- [ ] The message carries no forbidden content.
- [ ] Publication used the verified branch and remote, with the user's authorization,
      without force.
- [ ] A local merge used the intended base and reran the checks on the merged tree.
- [ ] Pull request publication did not trigger cleanup.
- [ ] Discard showed the inventory and waited for exact confirmation.
- [ ] An unexpected result stopped escalation and preserved the diagnostics.

**Postcondition and recovery**

- [ ] The resulting commit, branch, upstream, remote, pull request, merge, worktree and
      dirty state match the outcome.
- [ ] Unrelated tracked and untracked work is still there and is named in the handoff.
- [ ] Remote checks and review are observed, pending with an owner, inaccessible, or
      not applicable with a reason.
- [ ] Cleanup happened only after durability, absence of local-only state, exact target
      verification, and explicit intent or policy.
- [ ] Recovery references and limits are stated; the reflog is not promised for
      untracked or expired objects.
- [ ] The report names what was saved, where, the checks, pending work, the cleanup
      trigger and the next owner.

**Routing and maintenance**

- [ ] Unfinished work, conflicts, release, platform administration and damaged
      repository state were routed to their owners with a return condition.
- [ ] Durable scripts, hooks, prompts and policies have owners, scoped fixtures,
      rollback and update triggers.
- [ ] Recurring wrong-base, wrong-remote, mixed-scope, stale-check or premature-cleanup
      failures led to a change in policy or tools.
- [ ] Kept branches and worktrees have owners and retirement triggers.

**Compact mode** (low-risk keep or scoped local commit): requested outcome, identity,
dirty summary, ownership, relevant checks, action, postcondition, remaining state.
**Full mode** (remote publication, integration, shared state, cleanup, force, discard):
everything above. Environment-specific gates come from their own policy; this checklist
does not supersede protected-branch, compliance, release or hosting controls.

A good completion response points to the scoped diff, the current checks, the explicit
request, the resulting commit or pull request, the preserved unrelated file, the pending
owner and the cleanup trigger. A bad one says "covered" or "clean". A valid pending
response names the asynchronous gate, its consequence, its owner and the follow-up. If
an item cannot be answered and could change safety, the action stays blocked. Reopen
dependent items when the tree, policy, base, upstream, remote, check result, ownership
or requested outcome changes. If the checklist never changes or blocks an action, check
whether its questions still discriminate risk.

## Adjacent Reference Routing

Routing is an operational boundary. Keep this flow in control while determining the
requested outcome, repository identity, worktree state, ownership, quality evidence and
reversibility. Hand off before performing a mutation that belongs to implementation,
conflict recovery, release, platform administration, security or repository repair. A
route preserves the work and evidence needed to come back. It grants no new
authorization.

1. **Continue here** when the next action is a scoped commit, an authorized push, a pull
   request handoff, a local integration, a deliberate keep, a safe cleanup, or a
   confirmed discard of finishable work.
2. **Clarify here** when the state is understood but the outcome or ownership is not.
   Keep branch and worktree while asking the smallest consequential question.
3. **Route out** when the next mutation changes implementation, resolves history or
   content conflicts, performs a release or deployment, administers a protected platform
   resource, or repairs damaged repository state.
4. **Return here** only after the receiving procedure supplies its return evidence.
   Refresh every mutable observation the handoff invalidated.

The same person or agent may run both workflows. The boundary still matters because a
code fix, a conflict resolution, a deployment and a branch cleanup have different
authorization and verification contracts.

| Observed trigger | Receiving procedure | What this flow must not imply | Minimum transfer bundle | Return or stop condition |
| --- | --- | --- | --- | --- |
| Required behavior or tests are incomplete | The implementation and test workflow: [tdd-progress-and-resume](../tir-tdd-progress-and-resume/SKILL.md) | Editing more behavior to make the branch look finishable | Repository and worktree path, branch and commit, scoped diff, failing command and output, ownership notes, requested outcome | Return when the behavior is implemented and the checks have current results; stop if scope or intent changes materially |
| Work may be wrong; a claim needs checking; a test fails for an unknown reason | [review-verify-debug](../tir-code-review/SKILL.md) | That a commit makes the work correct | The diff, the failing evidence, the claim to verify | Return with a current verdict on the tree to be saved |
| A merge, rebase, cherry-pick or revert has unresolved conflicts | The repository's conflict-resolution or history-recovery procedure | Choosing conflict content, rewriting shared history, aborting an operation without understanding it | Active operation, conflict paths and stages, original heads, local-only changes, policy constraints, recovery objective | Return when the operation is intentionally resolved or aborted and checks can run; stop on ambiguous ownership |
| A commit or pull request is ready but release, package publication, deployment, migration or rollout is requested | The repository's release or deployment runbook | That a push, a merge or a green local test is production authorization | Immutable commit, target environment or channel, the release request, CI and review state, artifacts, approvals, rollback owner | Routing ends when the release authority accepts ownership |
| Branch protection, required checks, credentials, permissions or hosting configuration blocks progress | The platform administrator or repository maintainer | Bypassing protection, weakening checks, using other credentials, force-updating because ordinary publication failed | The exact platform error, repository and remote identity, requested operation, current access boundary, policy, non-secret diagnostics | Return when authorized configuration or access is confirmed |
| Objects, refs, index, worktree metadata, submodules or storage look damaged | Repository diagnosis and recovery | Deleting metadata, expiring recovery data, force-resetting, recloning over local-only state | Read-only diagnostics, locations, affected refs and paths, recent operations, backups, local-only inventory | Return only after integrity and ownership are established and the work is recoverable |
| The task only needs an explanation, a policy reading or a documentation fix | The documentation or policy owner | Mutating Git state to demonstrate an answer | The exact question, observed state if relevant, the policy cited, uncertainty and consequence | Resume only if the clarified rule changes a concrete delivery decision |
| The next task needs research or a design choice | [explore-and-decide](../tir-explore-and-decide/SKILL.md) | Starting the next task on a guess | The saved state, the project goals, the open question | Return to the development loop with a chosen task |
| Several agents share the work | [agent-context-and-orchestration](../tir-agent-context-and-prompts/SKILL.md) | That separate worktrees prevent shared-target races | The scale handoff fields above | Each unit comes back here for its own delivery |

**Transfer contract.** Before a handoff capture, without speculative cleanup:

- root, working directory, branch or detached state, current commit, linked worktree
  path;
- concise staged, unstaged, untracked, conflict and submodule state;
- ownership classification, including unrelated or unknown user work that must stay
  untouched;
- the requested outcome and the exact boundary that stopped this flow;
- commands already run, their scope and results, and which observations go stale if
  the tree or configuration changes;
- base, upstream, remote, pull request or platform identity, only where verified and
  relevant;
- the prohibited next action, the receiving owner, the return condition, and recovery
  information in case the handoff fails.

Do not remove the branch or worktree before transfer to make the environment tidy. A
dirty worktree may be the only durable location of the evidence.

**Handoff is not consent.** A route to release guidance does not authorize deployment.
A route to platform administration does not authorize changing branch protection. A
route to conflict recovery does not authorize a force push. A route to implementation
does not authorize a wider product scope. And a successful adjacent action does not
prove the original finish succeeded: on return, evaluate the preconditions and
postconditions against the new state instead of restoring an old "complete" label.

**Route record.**

| Field | Evidence |
| --- | --- |
| From state | Repository, worktree, branch or detached identity, commit, dirty summary, active Git operation |
| Route trigger | The blocker or requested action that crosses this flow's boundary |
| Destination | The named procedure or owner able to resolve it |
| Evidence bundle | Owned diff, local-only state, checks, policy, errors, relevant destination identities |
| Blocked mutation | The action deliberately withheld |
| Return condition | The observable condition that lets delivery resume, or an explicit terminal handoff |
| Refresh set | Status, diff, checks, base, upstream, remote, review or policy evidence the adjacent work invalidated |

**Examples.**

- Good: a required integration test fails because the feature is incomplete. Record the
  failing command and scoped diff, preserve unrelated files, route to implementation,
  return after the checks pass, and reinspect scope and ownership before committing.
- Bad: a merge conflict appears, so the agent picks one side, force-pushes, deletes the
  worktree and reports the branch finished.
- Borderline: a pull request is created correctly and local state is preserved, but
  the agent starts a production rollout because it read publication as release intent.

Routing loops, repeated rediscovery, lost local state, unexplained cleanup and
unauthorized follow-on actions are defects in the routing map. Record which trigger and
which transfer field failed. If no suitable authority exists and the missing decision
can affect safety: preserve the state, report the blocker and the recovery options, and
stop.

## Source Evidence Mapping Table

Sources route claims. They are not a vote. Two copies of the same text are one lineage,
not two confirmations.

| Source | Kind | What it contributes | Boundary or conflict |
| --- | --- | --- | --- |
| Owner's commit-push-continue agent definition (written for a Rust inference-server project) | Owner material | The three-phase flow (verify, commit and push, continue); conventional commit format; never commit failing tests; never-commit paths; delegation table; push-rejection handling; output format; communication style | Pushes as part of the flow and proactively. Project-specific checks and layer rules belong to that project's profile. |
| Owner's branch-finishing skill (later variant) | Owner material | Direct-request behavior; the four default paths and exact menu text; intentional saving; checkpoint commits; remote and branch selection; the runway handoff; guardrails | Does not specify worktree removal mechanics |
| Its interface metadata | Owner material | Short description and the one-line default prompt | Not copied as a file; the prompt is kept as the invocation line in the skill |
| This repository's instruction file | Repository policy | Never push without the explicit word; never put issue numbers in commit messages; issue references live in file content | Stricter than the commit-push agent on pushing; applies in this repository |
| Owner's branch-finish and worktree pattern reference | Owner synthesis | The state-transition model, authority ladder, matrix, failure table, retry gate, observability record, workload and scale model, evidence boundaries | Contains no measured rates; its priority scores are not measurements |
| Superpowers `finishing-a-development-branch` skill | Third-party, ideas only | Test-first completion, base discovery, the four-option structure, typed discard confirmation, cleanup mechanics | Contradicts itself on whether a pull request path removes the worktree |
| Superpowers `using-git-worktrees` skill | Third-party, ideas only | Directory priority, ignore check, setup detection, baseline tests, location report | Its instruction to fix and commit `.gitignore` at once needs authorization here; setup commands are ecosystem examples |
| GitHub Actions documentation; GitHub reusable-workflow documentation; the OpenAI Codex repository's agent-instruction file | External pointers, not read | Possible future evidence for CI semantics, composed workflows, and an example of repository instructions | Unread pointers establish nothing about content, validity or applicability |

**Retrieval order for a real operation.**

1. The user's explicit request. Commit, push, draft pull request, keep and discard are
   different authorizations; only explicit confirmation authorizes irreversible loss.
2. The repository's current instructions and ownership constraints.
3. Live state from non-mutating Git commands. Commands give state evidence, not policy.
4. This skill, for the defaults that the first three leave open.
5. Public documentation, only for a named platform question that is still open. Record
   the version, the passage, the applicability and the access date.
6. Stop gathering evidence when the outcome, ownership, state, checks, destructive
   boundary and postcondition are determined.

**What the material covers well:** ordinary feature-branch completion with common
branch and remote patterns: checks, base discovery, local merge, push and pull request,
keep, confirmed discard, project-local worktree safety, setup, baseline tests, handoff.
**What it does not govern:** protected-branch administration, release trains, force-push
policy, submodules, multi-repository publication, deployment, hosting permissions.
Literal commands need adapting for bare repositories, submodules, sparse checkout,
custom hosting, several remotes, protected branches, unusual base strategies and
project-specific dependency management. Keep the sequence and the safety reasoning;
verify the mechanics in the current environment.

**Using external documentation.** Only after local state identifies a question it can
answer. Inspect the repository's workflow files and the observed check names first, then
read the official page for the exact platform and feature. Documentation shows what a
platform supports; the checked-in workflow and the branch policy show what this
repository uses. For Git mechanics prefer the repository's instructions, the installed
`git help`, and non-mutating inspection. If a required authority is inaccessible, report
it as pending instead of filling the gap with a generic example.

| External source | Valid use after reading it | Invalid extrapolation |
| --- | --- | --- |
| CI platform documentation | Explain a named check's semantics, trigger, status or asynchronous completion, once the local workflow is identified | "Generic CI documentation proves this branch passed, or is safe to delete" |
| Reusable-workflow documentation | Trace why a check calls another workflow and what may still be pending | Assuming every composed workflow is required, secure or equivalent to branch policy |
| Another repository's agent-instruction file | Illustrate how a repository publishes agent-specific test and workflow instructions, at a pinned revision | Copying another repository's rules into this one, or inferring content from an unpinned URL |

Good: "The pull request references check `verify`; the inspected workflow delegates to
a reusable workflow; the official documentation explains the call; the observed remote
check is still pending." Bad: "The CI platform proves the branch is safe to remove."

For each consequential recommendation keep: the source or observed state, what it
establishes, the user authorization it needs, the command or gate that verifies it, and
the recovery path. Trace every destructive action back to an explicit confirmation.

## Evidence Boundary Notes

Evidence and authority are related and not interchangeable. A Git manual establishes
mechanics; it cannot authorize cleanup. Live status establishes that a file exists; it
cannot say who owns it. A user selects an outcome; a user cannot make a
policy-prohibited or technically unsafe transition complete without resolving the
constraint.

| Class | What it establishes | Permitted use | Prohibited inference | When to refresh |
| --- | --- | --- | --- | --- |
| User authorization | The requested outcome and explicit consent to a named consequence | Choose the commit, push, pull request, keep, checkpoint, merge, cleanup or confirmed discard path, within policy | Silence authorizes destruction; "push" implies merge, release, cleanup, force or unrelated staging; "commit" implies "push" | Scope or consequence changes; a destructive confirmation goes stale; a new policy or state conflict |
| Repository policy | Current local requirements for branches, remotes, checks, protection, ownership, messages, cleanup, release, tooling | Constrain or specify the operation; route exceptions to named owners | Every nearby document is policy; a generic guide overrides the repository's rules | The instruction file changes; a maintainer clarifies; a contradiction is observed |
| Observed repository state | What the repository, worktree, branch, index, diff, refs, remotes, checks and destination showed at that moment | Prove preconditions and postconditions for the actual operation | Observation grants authorization; an earlier snapshot is still current after mutation or concurrent work | Any relevant tree, index, ref, remote, policy, check or platform change |
| Guide text (this skill, or any workflow guide) | A procedure, defaults, examples | Structure the work where authority and state are silent | The text is universally correct, is repository policy, or describes live state | The text changes; a local authority supersedes it; a fixture fails; an incident occurs |
| Duplicate copy | The same content reachable by another path | Discoverability | Each copy is independent support | Either copy changes |
| External fact, actually read | A claim supported by an inspected, applicable primary source | Git or hosting mechanics, with URL, access date, version and scope | An unopened URL supplies evidence | A primary page is opened and its applicability recorded |
| External pointer, not read | A URL or query that may matter later | Mark a refresh route and the question it could answer | Current content, correctness, availability or applicability | A consequential open claim justifies reading it |
| Synthesis | Reasoning across the facts and constraints at hand | Select a conservative default, explain implications, name exceptions | The synthesis is quoted policy, a measurement, or a refreshed public fact | A source conflict changes; a live counterexample; a policy update; a failed fixture |
| Safety default | Least-destructive, reversible behavior chosen when authority or evidence is incomplete | Preserve work, stop mutation, ask, separate publication from cleanup, fail closed | Every repository mandates the default; the default overrides an explicit safe policy or request | Policy and intent provide a safer applicable alternative with verified preconditions |
| Repository-specific judgment | A decision applying local policy, state, ownership, risk and tooling to one operation | Choose the exact base, remote, checks, split, retry, cleanup and handoff | Portable guidance proves the local judgment without inspection | Any input to the judgment changes before the mutation or the postcondition |
| Unresolved uncertainty | A consequential gap in evidence, authority, identity or recovery | Block the affected action, preserve state, name the owner or the refresh route | "Unknown" means "probably safe", or can be resolved by a broader command | The missing evidence arrives; state changes; a specialist accepts the handoff |

Use the least authoritative label that describes the support accurately. When several
classes contribute, keep their roles apart: policy may require a test, observed state
may show it passed on a commit, and the user may request publication. Calling all three
"evidence" loses which one requires, which one establishes, and which one authorizes.

**Three decompositions.**

*Worktree after a pull request.* Source fact: the upstream finishing guide conflicts
with itself; the owner's later skill stresses explicit intent and intentional handoff.
State needed: branch and worktree identity, dirty and local-only files, published
commit, pull request head and base, durability. Authorization needed: an explicit
cleanup request or an applicable repository rule. Synthesis: publication and cleanup
are separate transitions. Safety default: keep branch and worktree when cleanup intent
or preconditions are absent. Verification: report what was kept or removed and prove
that unrelated work remains. This default is synthesis plus a safety default, not a
quotation from an uncontested source.

*Discard.* Source fact: confirmation is required before discard. State needed: the
exact tracked, staged, unstaged, untracked, conflict, branch, worktree and durable-copy
inventory. Authorization needed: a current, exact confirmation for the unchanged target
and consequence. Mechanics: the installed Git and the repository's recovery constraints
decide how an authorized discard is performed. Safety default: silence, ambiguity or a
changed inventory blocks destruction. Uncertainty: the reflog cannot be promised to
restore untracked content or expired objects.

*Remote publication.* User authorization decides whether publication is wanted (in this
repository, by the word "push"). Policy constrains remote, base, protection, checks and
review path. Observed state establishes the branch commit, upstream, remote identity
and the actual destination result. This skill gives the procedure and the handoff
defaults. Unread public pointers cannot establish the host's configuration or its retry
and idempotency behavior. The postcondition, not command success, establishes where the
work became durable.

**Claims.**

- Bad: "Best practice requires deleting the worktree after opening a pull request." No
  inspected source, user intent, repository policy or reconciliation supports it.
- Borderline: "The Git manual permits this cleanup, so proceed." Mechanics show that a
  command exists and how it behaves. They do not authorize deleting local work or prove
  durability and ownership.
- Good: "The pull request references the intended commit, the worktree holds no
  local-only task state, repository policy requests removal after publication, and the
  user asked for cleanup. Remove only the verified target and recheck the remaining
  worktrees."

**Claim audit** for a high-consequence recommendation:

1. What exactly is claimed: can, should, must, observed, requested, inferred, unknown?
2. Which source, policy, request, observation or reasoning supports it?
3. Is that support current, independent, applicable, and understood at the passage that
   matters?
4. Does a duplicate lineage or an internal conflict reduce the apparent corroboration?
5. Was public evidence actually read, or is it only a pointer?
6. Which repository-specific fact must still be observed before acting?
7. What would falsify or invalidate the recommendation?
8. Which verification or postcondition shows the action matched its claim?
9. What uncertainty remains, and does it block this consequence or only a stronger
   claim?
10. Is the evidence now enough to decide, or would more loading only repeat what is
    known?

Automated checks can verify paths, formats and fixture results. Human review is still
needed for semantic conflict, ownership, authorization, applicability and unsupported
escalation of authority.

**Decision sufficiency.** Proceed decisively when four things align: the user or a
delegated authority permits the outcome; repository policy permits and constrains it;
observed state establishes identity, ownership and preconditions; mechanics plus
verification can produce and prove the postcondition. When one consequential dimension
is open, preserve the state, name the missing evidence or owner, and route or ask. Do
not turn missing evidence into a destructive default, and do not keep loading unrelated
material once the decision is sufficient. Evidence boundaries constrain action; they are
not an excuse to avoid a safe, explicitly requested finish.

**What is not measured.** No performance, reliability, scale, retry or productivity
figure is established by any source. A numeric threshold needs a local policy or a
measurement packet with population, method, environment, uncertainty and owner.

## Future Refresh Search Queries

None of these queries has been run. They are plans, not citations. Refresh only when a
named uncertainty can change an operation. Public documentation can explain Git or
hosting semantics; it cannot establish local change ownership, the selected remote, the
configured protection, the required checks, or cleanup authorization.

**Sequence.**

1. State the claim or decision that may be stale and the consequence of being wrong.
2. Inspect local policy, tool version and help, and observed repository and platform
   state.
3. Query the primary manual or the official hosting documentation with product and
   feature terms, not a broad "best practices" phrase.
4. Open the page; verify version, product and configuration applicability; record the
   access date and revision. Search snippets are not evidence.
5. If the documentation stays ambiguous, reproduce in a disposable repository, worktree
   or remote under the matching installed version.
6. Classify the result as unchanged, clarified, contradicted, superseded or unresolved,
   and name every section and fixture affected.
7. Stop when one authoritative, applicable answer plus local state resolves the
   decision.

| Label | Trigger and decision | Check locally first | Query | Preferred authority | Acceptance and stop rule |
| --- | --- | --- | --- | --- | --- |
| Finish-guide drift | An upstream finishing skill changes; did direct-request, option, save or cleanup guidance change? | Compare the text you hold with the new one | `finishing a development branch skill commit push pull request worktree cleanup direct request source history` | The upstream project's files and history | Accept only reviewed semantic changes; identical copies stay one lineage |
| Worktree-guide drift | An upstream worktree skill changes; did location, ignore, setup, baseline or cleanup assumptions change? | Read the changed sections completely | `using git worktrees skill directory selection gitignore baseline tests cleanup source history` | The upstream project's files and history | Stop when the changed claims and affected sections are mapped |
| Worktree removal semantics | Git upgrade, a cleanup refusal that differs, or a recovery incident | `git --version`, installed help, worktree list, disposable dirty-worktree behavior | `site:git-scm.com/docs git-worktree remove force dirty locked prune repair version` | Official Git manual for the installed release | Accept the documented semantics; user intent and policy remain separate authorization |
| Worktree lock, prune, repair | Stale metadata, moved repository or locked worktree affects cleanup | Inspect worktree metadata and help without mutating | `site:git-scm.com/docs git-worktree lock unlock prune repair move repository` | Official Git manual and release notes | Route damaged state to recovery; a maintenance capability is not cleanup permission |
| Status machine format | Automation parses status across submodules, renames or unusual paths | Installed help; existing scripts and tests | `site:git-scm.com/docs git-status porcelain v2 untracked submodule rename format stability` | Official Git manual | Accept only a documented stable format; validate parser fixtures |
| Push rejection and force | A non-fast-forward or lease question affects a proposed recovery | Upstream, remote refs, policy, installed push help | `site:git-scm.com/docs git-push non-fast-forward force-with-lease expected value safety` | Official Git manual | Stop when the ordinary integration route is clear; force still needs separate authorization |
| Reflog recovery limits | A local commit looks unreachable, or recovery guidance is invoked | Preserve refs, reflog and objects; no pruning | `site:git-scm.com/docs git-reflog expire recover unreachable commit untracked files limitations` | Official Git manuals for reflog, reset, restore, maintenance | Record the exact recoverable object class; never imply the reflog restores untracked content |
| Pull request create effect | Create or update returned a timeout or unknown effect; can a retry duplicate? | Query existing requests for the head and base | `site:docs.github.com REST GraphQL pull request create head base duplicate idempotency retry timeout` | Official GitHub API and pull request documentation | Accept only behavior for the API or tool in use; if the effect stays unknown, keep the publication and stop |
| Head, base and forks | Cross-fork publication or base selection differs from the examples | Remotes, repository ownership, existing pull requests, policy | `site:docs.github.com pull request head repository fork base branch create permissions` | Official GitHub pull request documentation | Documentation shows capability; live state shows the actual repository and permissions |
| Branch protection rules | A direct push, merge or cleanup depends on required reviews, checks or rulesets | Repository policy and authorized platform configuration | `site:docs.github.com repositories rulesets protected branches required status checks merge queue current` | Official GitHub ruleset documentation | Do not infer enabled controls from documentation; accept only live configuration or maintainer evidence |
| Actions check scope | A readiness claim depends on a workflow, reusable workflow, event or commit coverage | Workflow files, required-check policy, run commit, current result | `site:docs.github.com actions workflow run event commit SHA reusable workflow required check status` | Official GitHub Actions documentation | Map the semantics to the actual workflow and commit; local tests stay distinct from remote CI |
| API rate and retry policy | Remote reads or writes are rate limited, or a wrapper needs pacing | Client behavior, response headers, tooling, hidden retry settings | `site:docs.github.com REST API rate limits retry-after secondary rate limit best practices idempotent requests` | Official GitHub API documentation | Adopt numeric pacing only from a current source that applies to the tool; expire it on API or client change |
| Commit-message cross-references | The no-issue-number rule needs its exact trigger patterns | A disposable repository and issue | `site:docs.github.com autolinked references URLs issues pull requests commit message cross-reference` | Official GitHub documentation on autolinked references | Extend the message check to every documented pattern |
| Squash-merge commit text | A squash merge may put a pull request number into a commit subject | The repository's merge settings | `site:docs.github.com squash merge default commit message pull request title number configure` | Official GitHub repository settings documentation | Decide whether squash-merge is compatible with the message rule |
| Repository-instruction example | The agent-instruction pointer is needed as an example | Validate the exact path and revision before reading | `site:github.com/openai/codex AGENTS.md testing instructions branch workflow revision` | The file at a verified revision | Example only; it governs no other repository |
| Git release changes | An upgrade changes worktree, push, status or recovery behavior | Installed version, release notes, affected fixtures | `site:git-scm.com/docs RelNotes git worktree push status reflog behavior change` | Official Git release notes and manuals | Refresh only affected claims; rerun their fixtures |
| Hosting release changes | A changelog announces ruleset, pull request, Actions or API changes | Repository usage and feature configuration | `site:github.blog/changelog pull request rulesets Actions API breaking change retry` | Official changelog, then product documentation | A changelog is a trigger; product documentation and live configuration establish applicability |

Add product version or date terms when the installed tool or platform release is known.
Do not put private repository names, confidential branch names, ticket content or
sensitive paths into public queries without authorization.

**Refresh result record.**

| Field | Content |
| --- | --- |
| Trigger | Guide drift, tool upgrade, policy change, contradictory incident, moved official page, failed fixture, or a named open decision |
| Claim at risk | The exact recommendation and the consequence if stale |
| Local state | Policy, installed version, relevant live configuration, safe direct observation |
| Query and source | Exact query, opened primary URL, access date, document or product version, revision |
| Finding | Concise paraphrase with applicability and any conflicting evidence |
| Verification | Disposable fixture or live read-only check, with version and limits |
| Disposition | Unchanged, clarified, contradicted, superseded, unresolved |
| Affected artifacts | Sections, scripts, hooks, prompts, tests, metrics and recovery guidance to review |
| Next invalidation | The version, policy, incident, URL or fixture event that should trigger another refresh |

- Good: ask whether the installed Git refuses ordinary removal of a dirty worktree,
  read the matching manual, use a disposable fixture only if interpretation is unclear.
  The finding explains semantics. It still cannot authorize removing the user's
  worktree.
- Bad: search "best Git workflow", copy a secondary summary, and turn an example command
  into universal policy.
- Borderline: read current branch-protection documentation and assume the target
  repository has those controls enabled. Documentation establishes possible behavior;
  authorized live configuration establishes actual behavior.

Keep earlier evidence and conflicts when refreshing. A moved page is a trigger for
semantic review, not proof that behavior changed. A recorded no-change result, with
scope and date, is legitimate evidence. Apply the strictest discipline to destructive
operations, history changes, remote destination behavior, branch protection, CI
coverage, recovery guarantees and platform retry and idempotency. Prefer event-driven
refresh to periodic broad search.

## Sources

- The owner's commit-push-continue agent definition, branch-finishing skill, repository
  instruction file, and branch-finish and worktree pattern reference. These are the
  backbone of this skill.
- **Superpowers** (third-party skill collection for coding agents): its
  `finishing-a-development-branch` and `using-git-worktrees` skills. Used for ideas
  only, restated here: test-first completion, the four-option structure, typed discard
  confirmation, worktree directory priority, ignore check, setup detection and baseline
  tests.
- GitHub documentation (Actions, reusable workflows) and the OpenAI Codex repository's
  agent-instruction file are named as future reading. They were not consulted.
