---
name: git-delivery-flow
description: >-
  Takes a finished change to a delivered change in Git: inspects the repository state,
  stages only the owned paths, writes the commit message, commits, pushes only when the
  user said so, opens a pull request, merges locally, keeps or discards a branch, and
  creates or retires a git worktree, then reports what was saved, where, and what is
  still open. Carries this repository's two mandatory rules: never run `git push` without
  the user's explicit word "push", and never put issue numbers (`org/repo#123`, `#123`)
  in a commit message. Use when the user says "commit this", "commit and push", "push to
  origin", "save this progress", "checkpoint this", "open a PR", "open a draft PR",
  "merge this branch", "finish this branch", "keep the branch", "discard this branch",
  "clean up the worktree", "set up a worktree for this feature", or "implementation is
  done, what next"; when work with passing tests is waiting uncommitted; when `git push`
  is rejected; when a commit message is being drafted. Not for deciding whether the work
  is correct or debugging a failing test (review-verify-debug), running the test-first
  loop or the progress journal (tdd-progress-and-resume), resolving merge or rebase
  conflicts, rewriting shared history, release, deployment, or branch-protection
  administration.
---

# Git Delivery Flow

This skill moves a finished change from the working tree to the place the user wants it:
a commit, a remote branch, a pull request, a merged base branch, a kept branch, or a
confirmed discard. It treats every step as a state change that needs three things: the
user's authority for it, an inspected starting state, and a checked result.

Core principle: **verify first, save with intent, execute the chosen path, prove the
result, leave the next step clear.**

Depth, long tables and worked examples are in [reference.md](reference.md). The entry
documents are [A00](../../../A00-LLM-Principles01.md) (verify every result) and
[A01](../../../A01-LLM-Workflow01.md) (the workflow this delivery step closes).

## When to Use

Use it when:

- The implementation is complete and the user wants it committed, pushed, published,
  merged, kept, or cleaned up.
- The user asks for a checkpoint of unfinished work.
- A commit message is being written in this repository or in any repository that has
  message rules.
- A feature needs an isolated workspace (a git worktree), or a worktree's task is done.
- A push was rejected, or a pull request call failed half way.
- The user says the work is done and asks what comes next.
- The user signals that work is ready to persist without naming Git: "this looks good",
  "tests are passing", "let's save this progress". Start proactively with verification
  and a commit. Proactive never covers a push in a repository that requires the word,
  and never covers cleanup or discard.

Requests that should trigger it:

- "Tests are passing, commit this work and let's move forward with the GPU integration."
- "Commit and push to origin ultrathink, then keep going. I trust you."
- "Open a draft PR for the auth branch."
- "Implementation is done. What now?"
- "Set up a worktree for the parser rewrite."

Requests that should not trigger it:

- "Why does this test fail on CI but pass locally?" Use
  [review-verify-debug](../review-verify-debug/SKILL.md).
- "Write the failing test first, then implement." Use
  [tdd-progress-and-resume](../tdd-progress-and-resume/SKILL.md).
- "Deploy this to production" or "cut the release". A push or a merge is not a release.

Also outside this skill: resolving a merge or rebase conflict. That is a different
authority and a different check. Preserve the state, hand off, and come back here after.

## Pick the Path

Two questions select everything else.

**1. Did the user already choose the outcome?**

| The user said | Path | Menu? |
| --- | --- | --- |
| `commit`, "save this", "checkpoint" | Scoped commit. No push unless the word "push" is there too. | No |
| `commit and push`, "push to origin `<branch>`" | Commit, then push to the named remote and branch. | No |
| "open a PR", "open a draft PR" | Commit if needed, push, create the pull request. Keep branch and worktree. | No |
| "merge it", "merge locally" | Local merge into the confirmed base, tests on the merged tree. | No |
| "keep this branch" | No change. Report branch, path, dirty state. | No |
| "discard this branch" | Inventory, exact confirmation, targeted removal. | No |
| "done, what next?" or nothing | Verify, then show the four-option menu. | Yes |

A direct request removes the menu. It does not remove verification, scope review, or
the confirmation for destruction.

**2. How much can go wrong?** This sets the evidence depth, not the safety rules.

| Mode | Use when | Evidence needed |
| --- | --- | --- |
| Compact | Keep, status report, or a scoped local commit with known identity and ownership | Requested outcome, repository and branch, dirty summary, scoped diff, relevant checks, the save, the postcondition |
| Full | Push, pull request, local merge, shared branch, cleanup, discard | All of compact, plus base, upstream, remote, policy, concurrency, recovery path, remote checks, exact cleanup or discard target |
| Blocked | Ownership, intent, repository integrity, or the consequence of a destructive step is unknown | Preserve state, report facts and the missing decision, change nothing |

Do not downgrade a shared or destructive action because the diff is small.

## Workflow

1. **Name the outcome.** Write down what should exist afterwards and what must stay
   untouched. If the user chose a path, keep it. Ask only about details that change
   scope, destination, destruction, or the readiness claim.
2. **Read the repository's rules.** Open the instruction file (`CLAUDE.md`, `AGENTS.md`
   or equivalent) and any contributing guide. Look for: push permission, commit message
   format, paths that must never be committed, required checks, the integration branch,
   the remote, worktree location. These override every default in this skill.
3. **Inspect before changing anything.** From the exact worktree: repository root,
   branch or detached state, worktree list, status, unstaged and staged diff, upstream,
   remotes. Use the commands in [Quality Gates](#quality-gates).
4. **Separate owned from unrelated changes.** Classify each changed path as task-owned,
   user-owned, shared, generated, or unknown. Unknown stops the action. Never make the
   tree clean by absorbing someone else's edits.
5. **Verify the claim.** Run the project's tests and checks against the tree you are
   about to save. If they fail: stop and fix, or report the failures. Commit failing work
   only as an explicitly requested, labeled checkpoint.
6. **Choose the path.** Known intent: go on. Unknown intent: show the four-option menu
   and wait.
7. **Stage exactly.** `git add <paths>` or `git add -p`. Review `git diff --cached`
   before committing. Confirm no never-commit path is staged.
8. **Commit with intent.** The message says what changed and why, in the project's
   format. Run the message checks. Commit. Record the new commit hash.
9. **Push only with authority.** In this repository: only when the user said "push".
   Otherwise ask and wait. Push to the remote and branch the user named; if none was
   named, the current branch and `origin`, after checking that they are the right ones.
   No force.
10. **Publish or integrate, if that was the path.** Create the pull request, or merge
    into the confirmed base and rerun the checks on the merged tree.
11. **Keep cleanup separate.** A push or a pull request is not permission to delete the
    branch or the worktree. Clean up only on an explicit request or a repository rule,
    and only after the work is durable somewhere else.
12. **Prove the postcondition.** Check the result independently of the command's own
    output: the commit contains only the intended paths, the remote ref holds the commit,
    the pull request head matches, the unrelated file is still there.
13. **Hand off.** Report what was saved, where, which checks ran, what is still open, and
    the next action. If the user asked to continue, continue; otherwise stop there.

If any step gives an unexpected result, stop. Do not retry, force, widen the staging, or
clean up to make the state look right. See [When Something Fails](#when-something-fails).

## Rules

### Authority

- The user's explicit request selects the outcome. Repository policy constrains it.
  Observed Git state shows whether it is possible. This skill only supplies defaults for
  what those three leave open.
- One permission does not imply another. "Commit" is not "push". "Push" is not "merge",
  "force", "release", "clean up", or "stage everything". "Open a PR" is not "delete the
  worktree".
- Silence never authorizes destruction.
- Trust from the user ("go ahead, I trust you") widens what you may do next without
  asking. It does not remove verification. Be bold but not reckless: always verify before
  committing.
- Do not fill an unknown with a plausible default. `main`, `master`, `origin`, a
  configured upstream and a clean status are hypotheses until checked.

### This repository's mandatory rules

These apply in this repository. Treat them as the model for any repository whose
instruction file states similar rules.

1. **Never push without explicit permission.** Do not run `git push` unless the user
   explicitly says "push". Always ask before pushing. "Commit", "save", "looks good" and
   "keep going" are not "push".
2. **Never reference external issue numbers in commit messages.** This repository's
   commits show up as cross-references on GitHub issues. A commit message must never
   contain patterns like `org/repo#123`, `apache/iggy#2739`, or a bare `#123`. Strip all
   issue references from the message. Put issue references inside file content only.
   - BAD: `Add deep analysis for MongoDB connector (apache/iggy#2739)`
   - GOOD: `Add MongoDB connector deep analysis for iggy`

By the same reasoning, keep full issue or pull request URLs and `GH-123` style
references out of commit messages too; they produce the same cross-reference. The
cross-reference appears when the commit reaches GitHub, so check every unpushed commit
before a push, not only the one being written.

### State and scope

- Inspect before every mutation: root, branch, worktree, status, diff, upstream, remotes.
- Check `git status` before and after each operation.
- Stage by path or by hunk. `git add -A` is acceptable only when every visible change is
  owned and reviewed. It is wrong in a mixed tree.
- Respect `.gitignore`. Never commit paths the project marks as local-only (for example
  a `.doNotCommit/` research directory), credentials, or generated debris.
- Unrelated and unknown changes stay untouched and are named in the report.
- Any change to the tree after inspection invalidates the status, diff and test evidence
  that depended on it. Re-run what it affects.

### Verification

- Run the project's test command before proposing a save or publish action. Tests
  support the quality claim only. They do not prove branch identity, commit scope, remote
  destination, or permission.
- Never commit broken code or code that fails tests, with one exception: the user
  explicitly asks for a checkpoint and accepts the tradeoff. Label it as a checkpoint in
  the message and the report, and record the failing check and the condition for
  resuming.
- If the test suite itself cannot compile or run and the project documents that, test
  manually and write the manual results into the report.
- Do not claim "ready", "complete", "merged" or "verified" without current checks that
  cover the exact tree and outcome claimed. Local checks, remote CI, review, merge
  readiness and release readiness are separate states.
- When the repository has several verification gates, pair this skill with
  [review-verify-debug](../review-verify-debug/SKILL.md).

### Commit messages

- Say what changed and why. A future developer must be able to understand the history
  from the messages.
- Use the project's format. Check `git log --oneline -15` first.
- No issue numbers where the repository forbids them (always in this repository).
- A checkpoint commit says so in its subject.
- If the change deviates from the project's standard patterns, say why in the message
  body or in the report.

### Push and publication

- Prefer the remote and branch the user named. Otherwise the current branch and
  `origin`, after confirming both.
- Never force-push without an explicit request and a policy that allows it. A rejected
  push is not that request.
- Report the remote, the branch and the final commit hash.
- A pull request is publication, not merge readiness. Report CI and review as observed,
  pending, or inaccessible.
- When pull request metadata or the review workflow matters after the push, pair this
  skill with the host's publishing tooling (`gh`, or a GitHub publishing skill if one is
  installed).

### Cleanup and destruction

- After a pull request, keep the branch and the worktree by default.
- Remove a branch or worktree only when all hold: explicit request or repository rule;
  the commit is merged or on the remote; no local-only files remain; the exact target is
  re-checked by full path.
- Discard needs an inventory shown to the user first (branch, commits, dirty and
  untracked files, worktree path), then an exact confirmation of that inventory. The
  opening words "discard this branch" are the request, not the confirmation.
- A refusal from Git (dirty worktree, unmerged branch) is protection. Do not add a force
  flag to get past it.
- Do not promise recovery through the reflog. It cannot restore untracked files or
  expired objects.

### Reporting

- Do not hide the branch, remote, or save location used.
- Do not leave the user guessing what the next action is.
- Show the Git commands you ran.
- Give each open item an owner: who acts next, and on what trigger.

## A. Commit and Push

Pick this when the user asked to save work, with or without a push.

**Phase 1: pre-commit verification**

1. `git status` to see what is staged and what is not.
2. Run the tests (`cargo test --workspace`, `npm test`, `pytest`, `go test ./...`, or
   the project's own command). If the suite is known to be broken, test manually and
   document it.
3. Check that the change follows the project's standards: tests written first where the
   project works test-first, both unit and integration tests where appropriate.
4. Check that no never-commit path is staged.
5. Check the project's structural rules (for example layer dependency rules: no circular
   dependencies between layers, the core crate stays minimal).
6. Where the project states performance goals, check that the change's performance
   implications fit them.

**Phase 2: commit and push**

1. Stage the files: `git add <files>`.
2. Write the message (see [Templates](#templates-and-commands)).
3. Commit: `git commit -m "<message>"`.
4. Push, if and only if authorized: `git push origin <branch>`.
5. Confirm the result and report the final commit hash.

**Phase 3: continuation (only when the user asked to continue)**

1. Read the project's steering or priority document for the next priority.
2. Read the architecture documents for guidance on that step.
3. If research is needed, delegate it (see below).
4. Propose the next logical task from the project's goals, the current status and the
   user's stated direction.
5. Be proactive, but seek confirmation before a major architectural change.

**Delegation during the flow**

| Situation | Action |
| --- | --- |
| New approach, research in reference repositories, unfamiliar domain, architecture exploration | Delegate to an exploration agent |
| File operations, documentation updates, refactoring, utility scripts | Delegate to a general-purpose agent |
| Standard Git operations, established patterns, well-defined features | Proceed yourself |
| Ambiguous requirements, a decision that departs from the architecture documents, a merge conflict that needs human judgment | Escalate to the user |

Brief every delegated agent on the project context and say in one line why you are
handing off. Keep continuity: the delegate's result comes back into this flow.

**If the push is rejected because the remote moved**

1. `git fetch origin`
2. `git rebase origin/<branch>` or `git merge origin/<branch>`
3. Resolve conflicts if any. Escalate complex conflicts to the user.
4. Re-run the checks (the tree changed), then retry the push.

Which of rebase or merge: follow the repository's rule if it names one. On a branch only
you write to, either is acceptable. On a shared branch, or when no rule exists and the
histories have really diverged, ask. Never answer a rejection with force.

## B. Finishing a Branch

Pick this when the implementation is complete and the question is where the branch goes.

**The four default outcomes** (show them only when the user has not chosen):

```text
Implementation complete. What would you like to do?

1. Merge back locally
2. Push and create a Pull Request
3. Keep the branch as-is
4. Discard this work
```

Show exactly these four, without added explanation. Name the base branch in option 1
when you have confirmed it. Do not ask an open "what should I do next?".

| Outcome | Steps | Branch after | Worktree after |
| --- | --- | --- | --- |
| 1. Merge locally | Confirm the base from repository policy; switch to it; update it the way the project allows; merge; run the checks on the merged tree | Delete with `git branch -d` only after the merged checks pass | Remove only on request or rule |
| 2. Push and PR | Push the branch; create the pull request against the confirmed base; report CI as pending | Keep | Keep |
| 3. Keep | Nothing | Keep | Keep |
| 4. Discard | Inventory; exact confirmation; `git branch -D`; remove the worktree | Deleted | Removed |

Related saves that are not in the menu but are valid direct requests:

- **Local commit:** intentional local save, no remote durability.
- **Checkpoint commit:** preserves failing or incomplete work; always labeled non-ready.
- **Push without a pull request:** remote durability without review.
- **Draft pull request:** review and durability before readiness.

**Base branch.** Repository policy first. `git merge-base HEAD main` only tests a
candidate; it does not prove that `main` is the integration branch. If the project says
`develop`, a successful merge into `main` is still wrong.

**Discard.** Show what will disappear, then wait:

```text
This will permanently delete:
- Branch: <name>
- Commits not on any remote: <list>
- Uncommitted and untracked files: <list>
- Worktree: <path>

Recovery: commits may be recoverable from the reflog for a limited time.
Untracked files are not recoverable.

Type "discard" to confirm.
```

If the inventory changes after the confirmation, the confirmation is void. Ask again.

## C. Worktrees

Pick this when work needs isolation from the current checkout (parallel features, a
long-running agent task, a risky change), and again when that work is finished.

**Creating one**

1. **Choose the directory.** In order: an existing `.worktrees/` directory, then an
   existing `worktrees/` directory; a location named in the repository's instruction
   file; otherwise ask the user (a hidden directory inside the project, or a directory
   outside the project). Do not assume.
2. **Check ignore safety** for a directory inside the project:
   `git check-ignore -q .worktrees`. If it is not ignored, the worktree's files would
   show up as untracked content of the main checkout. Report this. Edit and commit
   `.gitignore` only when the user or the repository's rules allow that change. A
   directory outside the project needs no check.
3. **Create it:** `git worktree add <path> -b <branch>`.
4. **Set it up** with the project's own setup command. Detect it from the project files
   (`package.json`, `Cargo.toml`, `requirements.txt`, `pyproject.toml`, `go.mod`); do not
   hardcode one. Skip the step if there is nothing to install.
5. **Run the baseline tests.** Record the result. If they fail, report the failures and
   ask whether to proceed or investigate. Without a baseline you cannot tell a new bug
   from an old one at finish time.
6. **Report:** full path, baseline result, what the worktree is for.

**Finishing in one**

- Identify the worktree with `git worktree list --porcelain` and compare the full path
  and branch. Do not select it by matching a substring of the branch name.
- Keep the worktree after a pull request, after "keep", and whenever cleanup was not
  requested.
- Before `git worktree remove <path>`: the work is merged or on the remote, `git status`
  inside the worktree shows no local-only files, and the user or a rule asked for
  removal.
- A kept worktree needs an owner and a trigger for retiring it (for example "remove
  after the pull request merges and the author confirms"). Otherwise it becomes debris.
- Separate worktrees isolate working directories and indexes. They do not prevent two
  workers from pushing to the same remote branch or opening duplicate pull requests. One
  writer per shared target.

## D. Repository Profile

Every repository adds its own rules to the flow. Collect them once per task, before the
first mutation.

| Slot | This repository (research knowledge base) | Example: a Rust service project |
| --- | --- | --- |
| Push permission | Only on the user's explicit "push"; always ask first | Push to the named working branch as part of "commit and push" |
| Message format | Plain imperative sentence, as in the existing log | `<type>(<scope>): <description>` |
| Forbidden in messages | Issue references of any form | None stated |
| Never-commit paths | Whatever `.gitignore` covers | A local research directory such as `.doNotCommit/` |
| Checks before commit | Link and structure checks of the changed documents | `cargo test --workspace`; manual testing, documented, when the test build is known broken |
| Structural rules | Issue references live in file content only | Layered crates, no circular dependencies, core crate minimal and `no_std` compatible |
| Where next priorities live | The user | A steering document and architecture documents |

When the instruction file and a default in this skill disagree, the instruction file
wins.

## Templates and Commands

**Commit message, plain form** (this repository):

```text
Add MongoDB connector deep analysis for iggy

Covers the sink connector's batching and retry behavior and the gaps
found against the connector trait. Issue links are inside the document.
```

**Commit message, conventional form** (projects that use it):

```text
<type>(<scope>): <description>

<why the change was needed, and anything a reader of the history must know>
```

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`.
Example: `feat(engine): add MLX inference streaming support`.

**Checkpoint commit:**

```text
checkpoint: parser recovery, 1 test failing (not ready)

test_recover_from_unclosed_brace fails: recovery skips one token too many.
Resume: fix skip_to_sync(), then rerun cargo test -p parser.
```

**Scoped commit:**

```bash
git status --porcelain=v1 --branch
git diff --name-status
git add path/one path/two            # or: git add -p
git diff --cached --name-status      # must list only the intended paths
git diff --cached --check
git commit -m "<message>"
git rev-parse --short HEAD
git status --porcelain=v1 --branch   # unrelated changes still present
```

**Push** (only with authority):

```bash
git remote -v                         # redact credentials if you quote this
git rev-parse --abbrev-ref --symbolic-full-name '@{upstream}' 2>/dev/null
git push origin <branch>              # add -u for a new branch
git ls-remote origin "refs/heads/<branch>"   # hash must equal: git rev-parse HEAD
```

**Pull request:**

```bash
git push -u origin <branch>
gh pr create --draft --base <base> --title "<title>" --body "$(cat <<'EOF'
## Summary
- <what changed>
- <why>

## Test plan
- [ ] <how it was verified, and what is still pending>
EOF
)"
gh pr view --json url,isDraft,headRefOid,baseRefName
```

Drop `--draft` for a ready pull request. Keep issue numbers out of the pull request
title if the repository squash-merges, because the title becomes a commit message.

**Local merge:**

```bash
git switch <base>
git pull --ff-only                    # or the project's update rule
git merge <feature-branch>
<project test command>                # on the merged tree
git branch -d <feature-branch>        # only after the checks pass
```

**Worktree:**

```bash
git check-ignore -q .worktrees && echo ignored || echo "NOT ignored"
git worktree add .worktrees/<name> -b <branch>
git worktree list --porcelain
git -C <worktree-path> status --porcelain    # must be empty before removal
git worktree remove <worktree-path>          # no --force
```

**Asking for push permission:**

```text
Committed <hash> on <branch>: "<subject>".
Not pushed. Say "push" and I will push <branch> to <remote>.
```

**One-line invocation** for delegating this flow to another agent:

```text
Use git-delivery-flow to verify this work, carry out the requested commit or push path,
and leave a concise next-step handoff after the branch is saved.
```

## Output Contract

Hand back a report with these parts, in this order. Begin with a clear statement of the
actions being taken, show the commands, report success or failure of each operation with
the relevant output, and conclude with next steps.

```text
## Committing changes
- Status checked: <branch>, <n> owned paths, <n> unrelated paths left untouched
- Tests: `<command>` -> <result>
- Staged: `git add <files>`
- Committed: `git commit -m "<subject>"` -> <hash>
- Pushed: `git push origin <branch>` -> origin/<branch> at <hash>
  (or: Not pushed. Waiting for "push".)

## State now
- Saved: <what>
- Where: <branch>, <remote or "local only">, <worktree path if any>
- Checks: <ran and passed> / <pending> / <not run, with reason>
- Left untouched: <unrelated files>
- Kept: <branch and worktree, with the trigger for cleanup>

## Next steps
- <the most obvious next action, and who owns it>
```

Use one of these states for each consequential item, never a blank: `verified`,
`pending` (with owner and follow-up), `not observed` (with its effect), `not applicable`
(with reason), `blocked`.

Style: decisive and action-oriented; status updates during multi-step operations;
structured lists for complex flows; match the user's collaborative tone.

## Quality Gates

Run from the exact worktree under review. Each gate proves one thing only.

```bash
# Identity
git rev-parse --show-toplevel
git branch --show-current || true     # empty means detached:
git rev-parse --short HEAD
git worktree list --porcelain

# Dirty state and scope
git status --porcelain=v1 --branch
git diff --name-status
git diff --cached --name-status
git diff --check

# Destination
git rev-parse --abbrev-ref --symbolic-full-name '@{upstream}'
git remote -v
git merge-base HEAD <candidate-base>

# Project quality (use the project's own command)
cargo test --workspace   # or: npm test / pytest / go test ./...
```

Message gates. Both must print nothing:

```bash
# The commit just made
git log -1 --format=%B | grep -nE '([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)?#[0-9]+|GH-[0-9]+|/(issues|pull)/[0-9]+'

# Every commit that a push would publish
git log '@{upstream}..HEAD' --format='%h %B' | grep -nE '([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)?#[0-9]+|GH-[0-9]+|/(issues|pull)/[0-9]+'
```

If the first one matches, fix the tip with `git commit --amend` before anything else.
If an older unpushed commit matches, tell the user and reword it only with their
agreement.

Push gate for this repository: the user's latest instruction contains the word "push".
If not, the gate fails and the answer is the permission request from the templates.

Postconditions by outcome:

| Outcome | Must be true afterwards |
| --- | --- |
| Commit or checkpoint | New commit exists; `git show --stat HEAD` lists only intended paths; unrelated changes still in `git status` |
| Push | `git ls-remote <remote> refs/heads/<branch>` equals `git rev-parse HEAD` |
| Pull request | One pull request; head commit and base as intended; draft state as requested; CI reported as pending or observed |
| Local merge | On the intended base; feature commit is an ancestor (`git merge-base --is-ancestor <feature> HEAD`); checks pass on the merged tree |
| Keep | Status equals the pre-state; branch and path reported |
| Cleanup or discard | Only the confirmed target is gone (`git worktree list`, `git branch --list`); everything else unchanged |

## When Something Fails

First response to any unexpected result:

1. Stop. No retry loop, no cleanup, no force.
2. Capture the command, its output, the root, branch, commit, status and any active Git
   operation.
3. Inventory local-only and unrelated work without resetting or deleting anything.
4. Ask the remote what actually happened. An error message does not prove nothing
   changed on the server.
5. Classify: no effect, complete, partial, wrong target, or unknown.
6. Choose the narrowest authorized response: retry, roll forward, checkpoint, wait, or
   escalate.
7. Verify the correction and report what is still uncertain.

| Failure | Response |
| --- | --- |
| Tests fail | Report the specific failures with output. Do not commit, unless a checkpoint was requested. |
| Push rejected, remote moved | Fetch, integrate by the allowed strategy, re-run checks, retry. No force. |
| Push rejected by branch protection | Not a retry case. Keep the commit; use the pull request route or ask the maintainer. |
| Push worked, pull request call failed or timed out | Look for an existing pull request for that head before trying again. |
| Hook changed files and the commit failed | Inspect index and tree, review the hook's changes, re-run checks, then decide. |
| Wrong branch or detached HEAD | Keep the commit hash. Do not checkout or reset until the destination is confirmed. |
| Too much staged | Unstage without discarding (`git restore --staged <path>`), then restage narrowly. |
| Worktree removal refused | Treat as success of a safety check. Inventory the local files and report. |
| Merge conflict | Leave this flow. Record the operation and conflict paths; hand to conflict resolution. |
| Project documentation unclear about the next step | Investigate (or delegate exploration) before proceeding. |
| Architectural question | Read the architecture documents first; escalate if still ambiguous. |

## Anti-Patterns

| Anti-pattern | Do instead |
| --- | --- |
| Pushing because the commit succeeded | Push only on the user's word; otherwise ask |
| Issue number in the commit message | Put the reference in file content; keep the message clean |
| Committing before looking at status | Inspect root, branch, status, diff, upstream first |
| `git add -A` in a mixed tree | Stage by path or hunk; review the staged diff |
| Showing the four-option menu after "commit and push" | Execute the requested path after the gates |
| Asking "what should I do next?" when intent is unknown | Show exactly the four options |
| Treating green tests as proof of scope, destination or permission | Check each separately |
| Treating a clean tree as finished | Check the outcome: unpushed commits, pending CI, wrong branch |
| Assuming `main` and `origin` | Confirm base and remote when the action depends on them |
| Removing the worktree after opening a pull request | Keep it; clean up on request after the work is durable |
| Deleting the branch before the merged tests ran | Postcondition first, cleanup after |
| Discarding on the word "discard" alone | Inventory, then exact confirmation |
| Force as the first answer to a surprise | Stop, classify, preserve, escalate |
| Editing and committing `.gitignore` on your own while setting up a worktree | Report the risk; change it with permission |
| Picking a worktree by a substring of its name | Use `--porcelain` output and the full path |
| Calling a checkpoint "done" | Label it; record the failure and the resume condition |
| "Clean and pushed" as the whole report | Name commit, branch, remote, checks, leftovers, next owner |
| Batching commit, two remotes, merge, deploy and cleanup in one go | One outcome per unit; sequence the units |

## Where the Sources Disagree

Both positions are kept. The selector says which applies.

| Topic | Position 1 | Position 2 | What selects |
| --- | --- | --- | --- |
| Pushing | Push is part of the commit flow and may be done proactively once work is complete | Never push unless the user explicitly says "push"; always ask | The repository's instruction file. This repository: position 2. Elsewhere: position 1 only when the request named the push or the project grants it. |
| Failing tests | Never commit code that fails tests | A failing state may be committed as a checkpoint | An explicit checkpoint request from a user who understands the tradeoff |
| Option menu | Always present exactly four options | Never force the menu on a direct request | Whether the user already chose |
| Worktree after a pull request | Remove it as part of finishing | Keep it | Keep by default; remove on explicit request or rule, after durability checks |
| Message format | Conventional `<type>(<scope>): <description>` | Plain imperative sentence | The project's existing log and instruction file |
| Unignored worktree directory | Fix `.gitignore` and commit at once | Report; change only with authorization | Whether the user or repository rules allow that commit |
| After the save | Continue into the next task autonomously | Report the next step and stop | Whether the user asked to continue ("and keep going") |
| Rejected push | Fetch, rebase or merge, retry | Retry only with an authorized integration strategy | Whether the branch is shared and whether policy names a strategy |
| Discard confirmation | A typed word | Explicit confirmation | Either form, but always after the inventory and against an unchanged inventory |
| Staging | Name the files | `git add -A` is fine when everything is owned | Whether every visible change is owned and reviewed |

## Bundled Scripts

None. The gates above are plain Git and `gh` commands.

## Self-Check Before You Finish

- [ ] I can state the outcome the user asked for, and I did that and nothing more.
- [ ] I read the repository's instruction file before the first mutation.
- [ ] I inspected root, branch, worktree, status and diff before changing anything.
- [ ] Only owned paths were staged; unrelated files are untouched and named in the report.
- [ ] Tests ran on the tree I saved, or the commit is labeled a checkpoint with the failure recorded.
- [ ] The commit message says what and why, in the project's format.
- [ ] The message gates print nothing: no issue reference in any commit I made or am about to push.
- [ ] I pushed only because the user said "push" (this repository), or the request named the push.
- [ ] No force flag was used.
- [ ] The postcondition for my outcome is checked, not assumed from an exit code.
- [ ] Branch and worktree are still there unless cleanup was requested and safe.
- [ ] Nothing was deleted without an inventory and an exact confirmation.
- [ ] The report names what was saved, where, which checks ran, what is open, and the next action with its owner.
