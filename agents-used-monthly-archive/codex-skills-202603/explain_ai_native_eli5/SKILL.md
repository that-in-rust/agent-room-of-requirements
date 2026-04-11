---
name: explain_ai_native_eli5
description: Explain AI-native engineering, four-word naming, TDD-first workflows, context engineering, and agent design in plain English. Use when Codex needs to turn dense notes, architecture writeups, or prompt-engineering guidance into an ELI5 markdown explainer with simple analogies, low-drama tone, and crisp takeaways.
---

# Explain AI Native ELI5

## Goal

Turn dense AI-native engineering notes into a short Markdown explainer that a smart beginner can understand in one pass.

## Default Reader

Assume the reader is either:

- A curious 12-year-old
- A non-engineer teammate
- A new developer who wants the idea before the jargon

## Writing Rules

- Start with the main idea in one sentence.
- Use plain words first, technical words second.
- Keep exact terms only when they matter, then define them once.
- Prefer short sections and short paragraphs.
- Use one everyday analogy per major concept.
- Keep the tone calm, factual, and low-drama.
- Output Markdown only unless the user explicitly asks for another format.

## Workflow

1. Find the core claim.
- Answer: "What is this really saying?"

2. Translate each concept into a real-world analogy.
- `four-word naming` -> putting clear labels on drawers
- `TDD-first` -> writing the answer key before building
- `summary docs` -> leaving bookmarks so you do not get lost
- `self-reasoning` -> talking out loud to catch your own mistakes
- `anti-pattern lists` -> a "do not step here again" map
- `context engineering` -> packing the right tools into a backpack
- `sub-agents` -> sending teammates into different rooms to check things in parallel

3. Explain in three layers.
- Layer 1: one-sentence takeaway
- Layer 2: short story version
- Layer 3: concrete rules or examples

4. Preserve what is source-specific.
- If the source claims numbers like `67% faster` or `90% fewer bugs`, present them as claims from the source notes unless independently verified.
- Keep facts separate from interpretation.

5. End with one sticky sentence.
- The final line should be memorable enough that the reader can repeat it later.

## AI-Native Cheat Sheet

Use these simple translations when the source material matches the meta-patterns in this repo.

| Source idea | ELI5 translation |
| --- | --- |
| LLMs are search and assimilation tools | The model is better at matching patterns than magically understanding everything |
| Four-word naming | Clear names help both people and models find the right drawer faster |
| Iteration matters | The first answer is a draft, not the finish line |
| Summary documents | Long chats forget, so write checkpoints |
| Self-reasoning | Asking the model to explain itself helps it catch weak logic |
| Anti-pattern references | Past mistakes are warning signs for future work |
| TDD-first | Tests tell the model what "done" looks like before coding starts |
| Context engineering | Good results depend on loading the right information, not all information |
| Give agents a computer | Agents work better when they can use files, shell tools, and scripts |
| Context offloading | Save old details to files instead of stuffing everything into the prompt |
| Context isolation | Split separate problems into separate workers so they do not trip over each other |

If the user wants the built-in plain-English version of this repo's meta-patterns note, load [AI-native engineering ELI5](references/ai_native_engineering_eli5.md).

## Recommended Output Shape

Use this structure unless the user asks for something shorter:

```markdown
# <Topic in simple words>

## Big Idea
## Why It Matters
## Core Ideas Made Simple
## Tiny Example
## What To Remember
```

## Tiny Example

When explaining four-word naming, prefer examples like this:

```markdown
Bad name: `filter()`
Better name: `filter_implementation_entities_only()`

Why? The better name tells you:
- what it does
- what it looks at
- what it keeps
```

## Guardrails

- Do not turn ELI5 into "wrong but cute."
- Do not remove important nuance when safety, correctness, or measurement matters.
- Do not repeat hype claims as universal truth.
- Do not drown the reader in jargon.
- Do not explain every detail from the source; keep only the details that unlock understanding.

## Done Check

Before finishing, verify:

- The first paragraph gives the big idea fast.
- Each major concept has a simple analogy.
- There is at least one concrete example.
- The explanation is readable by a smart beginner.
- The ending compresses the whole idea into one sentence.
