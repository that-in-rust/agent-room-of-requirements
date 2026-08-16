# GitHub Repo Context Thesis

## Table Of Contents

1. Core thesis
2. Why this skill matters
3. What counts as repository context
4. What the skill should optimize for
5. What the skill should not optimize for
6. Required capabilities
7. Recommended workflow
8. Packaging guidance
9. Validation guidance
10. Evidence base

## Core Thesis

GHCLI is an unusually strong tool for reconstructing repository history because it gives one authenticated command-line surface over both GitHub REST and GraphQL APIs, while also supporting JSON output, pagination, and templated formatting.

The right skill is not “use gh to browse GitHub.” The right skill is:

**capture the history of how a repository changed and what people said while it changed, using GHCLI as the primary read-only collection layer.**

That distinction matters because repository context is not one surface. It is spread across:

- commits
- commit comments
- pull requests
- PR review comments
- issues
- issue comments
- issue and PR timeline events
- GitHub Discussions

The skill should exist because most people only use `gh pr view`, `gh issue view`, or browser tabs. They do not usually build a repeatable, source-linked collection workflow that can answer:

- What changed?
- Who discussed it?
- Where was the decision made?
- What thread explains why the code looks like this?

## Why This Skill Matters

This skill is useful when:

- onboarding into an unfamiliar repository
- reconstructing design history
- tracing a regression to the surrounding discussion
- understanding why a PR merged the way it did
- finding discussion threads linked to a commit
- assembling a source-backed digest for incident review or architecture review

The biggest value is not raw collection. The biggest value is **normalization plus synthesis**.

Without the skill, people often:

- miss commit comments
- miss review comments that never landed in the PR body
- miss timeline events that explain state changes
- miss GitHub Discussions entirely
- over-trust search results as if they were complete history

## What Counts As Repository Context

Repository context includes both content and chronology.

### Content surfaces

- commit message and metadata
- commit comments
- PR title, body, reviews, review comments, linked commits, changed files
- issue title, body, comments
- discussion title, body, comments, replies, accepted answer state

### Chronology surfaces

- commit dates
- PR opened, reviewed, merged, closed dates
- issue opened, labeled, assigned, closed dates
- timeline events for state transitions
- discussion created, answered, updated dates

### Relationship surfaces

- commit to pull request mapping
- PR to issue linkage through references
- discussion URLs referenced from issues or PRs
- shared participants across threads

## What The Skill Should Optimize For

### 1. Read-only safety

The default mode should never create comments, reviews, edits, or mutations.

### 2. Exhaustiveness by surface

The skill should prefer canonical list and detail endpoints over lossy shortcuts. Search is helpful for discovery, but not a complete substitute for list endpoints.

For very large repositories, practical collection should start with a bounded survey mode and only widen on demand. Exhaustiveness remains the ideal, but bounded-first collection is the safer default for interactive use.

### 3. Provenance

Every digest should say what was queried, what was skipped, and where the facts came from.

### 4. Separation of conversation types

One of the easiest ways to create misleading output is to merge issue comments, review comments, commit comments, and discussion replies into one flat stream. The skill should preserve the source surface of every thread.

### 5. Chronology

The skill should help answer “what happened when,” not just “what exists.”

### 6. Recoverability

The raw collected JSON should be saved so a later pass can re-summarize without repeating the network collection.

## What The Skill Should Not Optimize For

### 1. Mutation workflows

This skill is not for writing issue comments, approving PRs, or editing discussions.

### 2. Browser scraping

The primary path should be GHCLI plus official APIs, not HTML scraping or browser automation.

### 3. One-command mythology

There is no single GHCLI command that returns the entire conversation history of a repo. The skill should explicitly model the collection as multi-surface.

### 4. Org-wide intelligence in v1

Keep the first version repo-scoped. Organization-wide graphing or cross-repo joins should be future work.

### 5. Overloaded SKILL.md

Keep the procedural guidance in `SKILL.md` short. Put endpoint maps, query shapes, and rationale in `references/`.

## Required Capabilities

The skill should include:

- repo capability detection
- host and auth checks
- repo-wide snapshot mode
- focused artifact trace mode
- discussion capture via GraphQL
- commit-to-PR linkage support
- Markdown digest generation
- explicit limits and gaps reporting

The skill should not require:

- third-party gh extensions
- local browser automation
- nonstandard GitHub apps
- a checked-out git clone of the target repo

## Recommended Workflow

1. Run `gh auth status --active`.
2. Confirm repo and host.
3. Inspect `gh repo view --json hasDiscussionsEnabled,...`.
4. Choose scope.
5. Capture canonical surfaces.
6. Save raw artifacts to disk.
7. Render a digest with chronology, key threads, and limits.

### Workflow split

Use `Repo Survey` when the user needs a broad context pack.

Use `Artifact Trace` when the user needs:

- a single PR history
- a single issue history
- a single commit story
- a single discussion thread

### Important implementation bias

- Prefer high-level `gh` commands for quick, typed views.
- Prefer `gh api --paginate --slurp` for durable harvesting.
- Prefer `gh api graphql` for GitHub Discussions.
- Prefer focused timeline collection over repo-wide timeline collection.

## Packaging Guidance

The skill should include:

- one concise `SKILL.md`
- one or more `references/` files for endpoint maps and rationale
- deterministic `scripts/` for capture and digest rendering
- `agents/openai.yaml`

### Good bundled resources

- a repo-wide capture script
- a focused artifact capture script
- a digest-rendering script
- a surface map reference
- a discussions GraphQL reference
- a clear output contract

### Resources to avoid

- long narrative README files
- repeated copies of GitHub API docs
- redundant examples that restate the same command pattern

## Validation Guidance

The skill is only trustworthy if it is tested on a live repository.

Minimum validation:

- run `quick_validate.py`
- run the repo capture script on a public repository
- run the focused artifact script on at least one PR or issue
- run the digest renderer on real captured output
- confirm Discussions degrade cleanly when disabled

## Evidence Base

This thesis is grounded in official GitHub CLI and GitHub Docs guidance checked on 2026-04-08.

Key facts used:

- `gh api` supports REST, GraphQL, pagination, slurping, and JSON shaping.
- `gh search commits` exists, but it is search-oriented rather than a canonical archival endpoint.
- `gh repo view --json ...` exposes `hasDiscussionsEnabled`.
- GitHub Discussions are available through GraphQL rather than a dedicated top-level `gh discussion` command.
- GitHub exposes separate surfaces for commits, commit comments, issue comments, PR review comments, and timeline events.

Primary docs:

- https://cli.github.com/manual/gh_api
- https://cli.github.com/manual/gh_pr_view
- https://cli.github.com/manual/gh_issue_view
- https://cli.github.com/manual/gh_search_commits
- https://cli.github.com/manual/gh_repo_view
- https://docs.github.com/en/graphql/guides/using-the-graphql-api-for-discussions
- https://docs.github.com/en/rest/commits/commits
- https://docs.github.com/en/rest/commits/comments
- https://docs.github.com/en/rest/issues/comments
- https://docs.github.com/en/rest/issues/timeline
- https://docs.github.com/en/rest/pulls/comments
