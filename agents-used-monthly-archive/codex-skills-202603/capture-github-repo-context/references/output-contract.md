# Output Contract

## Table Of Contents

1. Digest goals
2. Required sections
3. Coverage notes
4. Raw artifact expectations

## Digest Goals

The final digest should help a teammate answer:

- what was collected
- what happened when
- where the main decisions happened
- what gaps remain

## Required Sections

1. `Scope`
- repo
- capture type
- collection time
- since filter, if any
- page cap, if used

2. `Surfaces Queried`
- commits
- pull requests
- issues
- issue comments
- review comments
- commit comments
- timeline events, if captured
- discussions, if captured

3. `Chronology`
- recent commits
- recent PRs
- recent issues or discussions

4. `Key Conversations`
- review threads that matter
- accepted answers in discussions
- issues or PRs with dense comment activity

5. `Linked Artifacts`
- commit to PR associations
- PR to issue references when visible
- URLs for key artifacts

6. `Gaps And Limits`
- permissions
- disabled discussions
- uncaptured timeline surfaces
- search versus canonical list caveats

7. `Raw Output Paths`
- manifest
- raw JSON directory
- digest path

## Coverage Notes

The digest should explicitly distinguish:

- issue-thread comments
- PR review comments
- commit comments
- discussion comments and replies

## Raw Artifact Expectations

The raw output directory should be stable enough that Codex can rerun only the synthesis step without repeating network collection.
