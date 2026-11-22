# Checkpoint Template

Use this template when creating a repo-root conversation checkpoint.

## Filename Pattern

```text
chat-checkpoint-YYYYMMDD-HHMMSS.md
```

Examples:

```text
chat-checkpoint-20260422-164510.md
chat-checkpoint-20260422-181233.md
```

## Minimal File Shape

```md
# Chat Checkpoint

- created_at_local: 2026-04-22 16:45:10 IST
- repo_root: /absolute/path/to/repo
- capture_mode: chronological_messages
- capture_count: 5
- source: active Codex thread

## Transcript

### 01 user
Paste the recent user message here.

### 02 assistant
Paste the recent assistant message here.
```

## Capture Rules

- Default to the last `5` visible messages when the user does not specify a count.
- If the user says `responses`, capture assistant responses instead of mixed speaker chronology.
- Preserve speaker order.
- Prefer direct copy over paraphrase.
- If a message is intentionally shortened, mark it with `[trimmed for length]`.

## Good Defaults

- format: Markdown
- location: repo root
- overwrite policy: never overwrite by default
- timestamp: local machine time
