---
name: finishing-a-development-branch
description: Use when implementation is complete and the user wants to commit, push, publish, preserve, or clean up the branch. Handles branch-finish decisions, explicit commit-and-push requests, and concise next-step handoff after the work has been saved.
---

# Finishing a Development Branch

## Overview

Guide completion of development work by verifying quality, saving the work intentionally, and leaving the next move clear.

**Core principle:** verify first -> save intentionally -> execute the chosen path -> leave a clean runway.

## Workflow

1. Verify the branch is actually finishable.
- Run the relevant tests or checks before proposing any save or publish action.
- If verification fails, stop and fix or report the failures before continuing.

2. Detect whether the user already chose the path.
- If the user explicitly said `commit`, `push`, `open a PR`, `keep this branch`, or `discard`, execute that path after verification.
- If the user did not choose, present a short set of options.

3. Use these four default paths when a choice is needed.
- merge locally
- push and create a PR
- keep the branch as-is
- discard the work after explicit confirmation

4. Save with intent.
- Write a commit message that says what changed and why.
- Never commit broken work unless the user explicitly asks for a checkpoint commit and understands the tradeoff.
- When pushing, prefer the named remote and branch the user gave; otherwise use the current branch and `origin`.

5. Leave the next-step runway.
- After the branch action, report:
- what was saved
- where it was saved
- what remains open
- the most obvious next action if the user wants to continue

## Direct-Request Behavior

If the user already knows what they want, do not force an option menu first.

Examples:
- `commit and push to origin`
- `open a draft PR`
- `save this progress and keep going`
- `discard this branch`

Execute the requested path directly once verification is complete and any destructive action is confirmed.

## Option Menu

When the user has not chosen, present exactly these options:

```text
Implementation complete. What would you like to do?

1. Merge back locally
2. Push and create a Pull Request
3. Keep the branch as-is
4. Discard this work
```

## Guardrails

- Do not claim the work is ready if tests are failing.
- Do not delete work without an explicit confirmation.
- Do not hide the branch, remote, or save location used.
- Do not leave the user guessing what the next action is after the save or push.

## Companion Use

- Pair with `verification-before-completion` when the repo has multiple verification gates.
- Pair with GitHub publishing skills when PR metadata or review workflows matter after the push.
