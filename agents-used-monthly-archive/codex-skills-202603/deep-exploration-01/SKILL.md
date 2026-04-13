---
name: deep-exploration-01
description: Conduct deep research and multi-perspective exploration for complex questions, decisions, and problem spaces. Use when the user asks for rigorous analysis, deeper context, strategic options, premise checking, thesis testing, creative but defensible alternatives, or a nuanced answer that goes beyond summary and must separate sourced facts from inference.
---

# Deep Exploration 01

Use this skill to turn broad, ambiguous, or high-complexity prompts into evidence-based analysis with strong premise checking, multiple expert lenses, and explicit verification.

## Workflow

1. Calibrate the task.
- Identify the real objective, output shape, time sensitivity, and domain boundaries.
- If the prompt contains a material ambiguity, flawed premise, or missing constraint, state it plainly and ask a targeted clarification question.
- If the prompt is workable, proceed without ceremony.

2. Build an expert council.
- Choose 3 to 5 expert lenses appropriate to the task.
- Always include one skeptical or adversarial lens that attacks assumptions and weak evidence.
- Keep the lenses domain-relevant; avoid theatrical persona naming.

3. Map the solution space.
- Start with the conventional approach.
- Generate three non-obvious alternatives, ideally by blending the problem with a distant but useful domain.
- Evaluate the tradeoffs and choose the best path or hybrid.

4. Gather and separate evidence.
- Prefer primary sources and current information when stakes or freshness matter.
- Distinguish clearly between sourced facts, reasoned inference, and speculation.
- Surface what would change the conclusion.

5. Run structured challenge.
- Let the skeptical lens challenge the leading approach.
- Let the other lenses respond with counter-evidence or constraints.
- Synthesize the debate into a single working thesis.

6. Verify before finalizing.
- Generate fact-checkable verification questions for the main claims.
- Answer them from available evidence.
- Revise the response if verification exposes gaps or overstatement.

## Output Contract

Return results in this order when the task is substantial:

1. `Premise Check`
2. `Expert Lenses`
3. `Candidate Approaches`
4. `Chosen Thesis`
5. `Evidence and Verification`
6. `Final Synthesis`
7. `Open Questions`

For smaller tasks, compress the same logic into fewer sections.

## Guardrails

- Do not present hidden chain-of-thought; present conclusions, evidence, assumptions, and tradeoffs.
- Do not claim certainty where the evidence is thin.
- Do not use "omniscient" or authority-theater language in the final response.
- Do not confuse creativity with rigor; novel options must still be defensible.
- If information is not from the provided sources or verified research, label it as inference or background knowledge.

## Research Standard

- Use web research when freshness, citations, or precise source attribution matter.
- Prefer primary documentation, official publications, research papers, and direct data sources.
- Include links when the user would benefit from source access.

## Companion Use

- Pair with `timeline-traverser` when the user needs explicit future-state simulations across several choices after the evidence is gathered.
- Use this skill for the research and thesis work; use `timeline-traverser` for the causal scenario map.

## Context Strategy

Load progressively:

1. Load this `SKILL.md`.
2. Load [Exploration output patterns](./references/exploration-output-patterns.md) for response scaffolds.
3. Load [Expert lens and verification playbook](./references/expert-lens-and-verification-playbook.md) when the task needs structured debate or deeper rigor.

## References

- [Exploration output patterns](./references/exploration-output-patterns.md)
- [Expert lens and verification playbook](./references/expert-lens-and-verification-playbook.md)
