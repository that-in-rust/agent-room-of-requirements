---
name: save-recent-chat-context
description: Save the most recent visible conversation text from the active Codex thread into a timestamped Markdown checkpoint file in the current repo root. Use when the user asks to back up the last few chat messages, dump recent thread context to disk, preserve a resume point before context loss, or create a lightweight conversation recovery file.
---

# Save Recent Chat Context

Use this skill to create a simple conversation checkpoint file that can be reopened later if the thread loses continuity.

## Default Behavior

- Capture the last `5` visible messages from the active conversation unless the user asks for a different count.
- Treat `messages` or `turns` as chronological message blocks, regardless of speaker.
- Treat `responses` as assistant messages only. Include the immediately preceding user prompt when clarity would otherwise be lost.
- Write a timestamped Markdown file to the current repo root.
- Use local time from the current environment.
- Prefer direct copy of the recent chat text over summarization.

## Workflow

1. Determine the capture window.
- If the user specifies a count such as `3`, `5`, or `10`, use it.
- If no count is given, default to `5`.
- If the user asks for `responses`, capture assistant responses.
- Otherwise capture chronological messages from both sides.

2. Determine the destination file.
- Write to the repo root or current working directory if that is the repo root.
- Use the filename pattern `chat-checkpoint-YYYYMMDD-HHMMSS.md`.
- Never overwrite an existing checkpoint unless the user explicitly asks.

3. Capture only what is actually visible in the active thread context.
- Use the current conversation as the source of truth.
- Do not invent or reconstruct missing earlier text.
- Preserve ordering and speaker labels.

4. Write the checkpoint file.
- Use the template in [Checkpoint template](./references/checkpoint-template.md).
- Keep the transcript mostly verbatim.
- Light whitespace cleanup is fine, but do not rewrite substance unless the user explicitly asks for a summary checkpoint instead.

5. Confirm the result.
- Report the saved path.
- Report the capture mode and count.
- Mention if anything had to be trimmed or normalized.

## File Contract

Every checkpoint should contain:

- `created_at_local`
- `repo_root`
- `capture_mode`
- `capture_count`
- `source`
- `Transcript`

Preferred structure:

```md
# Chat Checkpoint

- created_at_local: 2026-04-22 16:45:10 IST
- repo_root: /absolute/path/to/repo
- capture_mode: chronological_messages
- capture_count: 5
- source: active Codex thread

## Transcript

### 01 user
...

### 02 assistant
...
```

## Guardrails

- Do not summarize by default when the user asked for a backup or checkpoint.
- Do not silently drop a recent message unless the user asked for a smaller window.
- Do not claim the file is a full transcript unless it actually is.
- Do not store the file outside the repo root unless the user explicitly requests another location.
- Prefer one new checkpoint file per request instead of updating an older one in place.

## Context Strategy

Load progressively:

1. Read this `SKILL.md`.
2. Read [Checkpoint template](./references/checkpoint-template.md) if you need a ready-made file structure or naming rule refresher.
3. Use the active conversation thread as the source material.

## References

- [Checkpoint template](./references/checkpoint-template.md)
