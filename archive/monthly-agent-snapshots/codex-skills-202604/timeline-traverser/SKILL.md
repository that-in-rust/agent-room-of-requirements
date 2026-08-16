---
name: timeline-traverser
description: Simulate multiple plausible futures for a decision, architecture choice, strategy question, or difficult conversation. Use when the user needs scenario planning, causal step-by-step timelines, risk comparison, regret analysis, or a clearer view of tradeoffs across possible paths before choosing.
---

# Timeline Traverser

## Overview

Use this skill when the right answer depends on how different choices unfold over time.
Do not give advice by vibe. Build 3 to 5 plausible timelines and compare them.

## Workflow

1. Frame the decision.
- Identify the actual fork in the road.
- Capture goals, values, hard constraints, and what would count as a win.

2. Choose the horizon.
- Pick the relevant time windows: first week, first month, first quarter, first year, or whatever fits the problem.

3. Build the timelines.
- Give each path a clear label.
- Start from a concrete action.
- Explain the causal chain step by step.
- Include likely reactions from other people, teams, or systems.

4. Add the lived-experience layer.
- Note stress, relief, attention cost, and daily reality, not just the abstract outcome.

5. Compare across timelines.
- Summarize upside, downside, reversibility, regret risk, and variance.
- Surface the inflection points where small changes create different branches.

6. End with a decision filter.
- Recommend the most robust path or the next experiment that would collapse uncertainty.

## Output Contract

Return results in this order:

1. `Decision Frame`
2. `Timeline A`
3. `Timeline B`
4. `Timeline C`
5. `Cross-Timeline Analysis`
6. `Decision Filter`

Add `Timeline D` and `Timeline E` only when the problem genuinely needs them.

## Guardrails

- Do not confuse unlikely stories with useful scenarios.
- Do not hide assumptions; state them.
- Do not skip the emotional or operational cost of a path.
- If the task needs source-backed research first, pair with `deep-exploration-01` and then simulate from the evidence.

## Reference Use

- Use [Timeline comparison template](references/timeline-comparison-template.md) when the output needs a stable structure or the problem is high stakes.
