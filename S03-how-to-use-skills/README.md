# Use one skill on one change

Choose a skill by **what you need to do**, not by the name of your agent. Open its `SKILL.md` from the [task index](../S01-skills-for-engineering-teams/README.md) and give that file to the agent as context. Keep its directory intact if copying a skill with helper scripts or assets. Open `reference.md` only if the short guide doesn’t settle a decision.

## A workshop you can run on this library

**Goal:** make a new skill discoverable. Work in a disposable checkout with Git, Python 3 and Bash; run the commands from its root. This exercise changes only that checkout. Do not push it.

| Step | Give the agent | Ask for evidence |
|---|---|---|
| **Map** | [Codebase navigation](../S01-skills-for-engineering-teams/codebase-navigation/SKILL.md) | “Trace how a reader finds the Rust CLI skill from the front page. Show the links, then find the check that would detect a missing index entry. Don’t edit yet.” |
| **Specify** | [Executable specs](../S01-skills-for-engineering-teams/executable-specs/SKILL.md) | “When a skill exists but the task index doesn’t link to it, the check shall exit nonzero and name it. When the link is added, it shall pass. Show how you’ll demonstrate both outcomes.” |
| **Verify** | [Review, verify and debug](../S01-skills-for-engineering-teams/review-verify-debug/SKILL.md) | “Run the experiment below. Report the failing output, the one edit that fixed it, and the final exit status. Do not change the checker.” |

First get a passing baseline. Then create a stand-in for a participant’s new skill and rerun the same check:

```sh
python3 S03-how-to-use-skills/check.py
mkdir S01-skills-for-engineering-teams/workshop-demo
printf '%s\n' '---' 'name: workshop-demo' 'description: Practice the workshop exercise.' '---' '# Workshop demo' > S01-skills-for-engineering-teams/workshop-demo/SKILL.md
python3 S03-how-to-use-skills/check.py
```

The last run should fail with `not indexed: S01-skills-for-engineering-teams/workshop-demo/SKILL.md`. Now add the reader’s route and rerun:

```sh
printf '\n[Workshop demo](workshop-demo/SKILL.md)\n' >> S01-skills-for-engineering-teams/README.md
python3 S03-how-to-use-skills/check.py
git status --short
```

Click the new link in the index. The check is green and a reader can reach the skill; neither alone proves the skill teaches the right thing. Discard the disposable checkout when finished.

## Take the exercise to a client repo

Replace “find the Rust CLI skill” with one observable change, such as “an unknown config key makes the CLI exit nonzero and name the key.” Ask for the route from user input to validation, then a failing CLI test, then the smallest fix. Use focused interface or unit tests for faster feedback; rerun the outer test before claiming the change works.

**Copyable agent setup.** In a target repo’s `AGENTS.md`, adapt the following. Replace both placeholders with paths or commands you verified there:

```markdown
For an unfamiliar change, read <path-to-codebase-navigation/SKILL.md>.
Before edits, show the entry point, affected boundary, and one observable outcome.
Verify with <project test command>. Report what failed before and passed after.
```

If the project also uses `CLAUDE.md`, point it to the same instructions rather than keeping two copies:

```markdown
Read AGENTS.md in this directory before planning changes. Use the test command there.
```

These are **examples**, not active instructions for this library. Its [git rules](repository-rules.md) apply when editing it. The [library check](check.py) verifies local document links, the skill index and embedded Rust guidance; the old migration’s file-count ceiling is not a workshop requirement.
