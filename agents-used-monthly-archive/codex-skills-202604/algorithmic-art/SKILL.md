---
name: algorithmic-art
description: Create generative art and creative coding outputs through p5.js, canvas, particle systems, flow fields, cellular systems, or mathematically driven visual experiments. Use when the user wants code-based art, computational aesthetics, interactive sketches, or concept-driven visual work rather than product UI.
---

# Algorithmic Art

## Overview

Use this skill when the deliverable is code that produces visual behavior, motion, or emergent composition.
Keep the workflow tight: concept -> system -> parameter surface -> implementation.

## Workflow

1. Distill the conceptual seed.
- Identify the feeling, metaphor, motion, or mathematical idea the piece should express.
- Decide whether the work is static, animated, interactive, or seed-driven.

2. Pick one dominant visual system.
- Choose the smallest fitting family from [Generative pattern menu](references/generative-pattern-menu.md).
- Prefer one strong behavior over a pile of loosely related effects.

3. Define the control surface.
- Pick a small set of expressive parameters such as seed, palette, density, decay, noise scale, velocity, or spawn rate.
- Make randomness reproducible when the medium allows it.

4. Translate the concept into implementation.
- Default to p5.js or plain canvas for fast iteration.
- Move to shaders, WebGL, or heavier stacks only when the effect genuinely depends on them.
- Separate update, render, and input logic.

5. Verify the piece as software.
- Check resize behavior, seed behavior, frame stability, and readability of the code.
- Add comments only where they clarify the system or the controls.

## Default Rules

- Prefer living motion over static ornament.
- Keep the parameter count small but meaningful.
- Make the same seed produce the same result unless the user asks for pure chaos.
- Use color deliberately; the motion system should still be interesting in monochrome.
- Make failure graceful: if the browser slows down, degrade density before adding complexity.

## Reference Use

- Read [Algorithmic philosophy template](references/algorithmic-philosophy-template.md) when the user wants the concept articulated as a short manifesto or design note.
- Read [Generative pattern menu](references/generative-pattern-menu.md) when choosing the visual system or looking for a better match than the first idea.

## Output Contract

Return results in this order when the task is substantial:

1. `Concept`
2. `Visual System`
3. `Parameter Plan`
4. `Implementation Notes`
5. `Code`

## Guardrails

- Do not mistake extra layers for depth.
- Do not ship unseeded randomness when repeatability matters.
- Do not turn a visual-art request into generic frontend scaffolding.
- If the user actually wants a polished application shell, bring in `frontend-design` or `playground` as a companion, but keep this skill focused on the art system itself.
