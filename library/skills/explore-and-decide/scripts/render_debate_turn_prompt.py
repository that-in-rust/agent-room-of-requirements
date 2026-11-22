#!/usr/bin/env python3
"""Render a debate-turn prompt from a shared markdown debate file."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


HEADER_PATTERNS = {
    "topic": re.compile(r"^# Debate:\s*(?P<value>.+?)\s*$"),
    "agent_1": re.compile(r"^\*\*Agent 1:\*\*\s*(?P<value>.+?)\s*$"),
    "agent_2": re.compile(r"^\*\*Agent 2:\*\*\s*(?P<value>.+?)\s*$"),
    "agent_3": re.compile(r"^\*\*Agent 3:\*\*\s*(?P<value>.+?)\s*$"),
    "max_rounds": re.compile(r"^\*\*Max Rounds:\*\*\s*(?P<value>\d+)\s*$"),
}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Render the next debate-turn prompt.")
    parser.add_argument("--debate-file", required=True, help="Path to the debate markdown file.")
    agent_group = parser.add_mutually_exclusive_group(required=True)
    agent_group.add_argument("--agent-name", help="Agent display name from the debate header.")
    agent_group.add_argument("--agent-number", type=int, choices=[1, 2, 3], help="Agent slot number.")
    parser.add_argument("--round", type=int, required=True, help="Current debate round.")
    parser.add_argument("--output", help="Optional path to save the rendered prompt.")
    return parser


def parse_header(content: str) -> dict[str, str]:
    values: dict[str, str] = {}
    for line in content.splitlines():
        for key, pattern in HEADER_PATTERNS.items():
            match = pattern.match(line)
            if match:
                values[key] = match.group("value")
    missing = [key for key in HEADER_PATTERNS if key not in values]
    if missing:
        missing_fields = ", ".join(missing)
        raise ValueError(f"Debate file is missing required header fields: {missing_fields}")
    return values


def resolve_agent(values: dict[str, str], agent_name: str | None, agent_number: int | None) -> tuple[int, str]:
    agent_map = {
        1: values["agent_1"],
        2: values["agent_2"],
        3: values["agent_3"],
    }
    if agent_number is not None:
        agent_value = agent_map[agent_number]
        if agent_value == "-":
            raise ValueError(f"Agent slot {agent_number} is not populated in the debate file.")
        return agent_number, agent_value

    assert agent_name is not None
    normalized_target = agent_name.strip().casefold()
    for number, value in agent_map.items():
        if value != "-" and value.strip().casefold() == normalized_target:
            return number, value
    raise ValueError(f"Agent name not found in debate header: {agent_name}")


def format_other_agents(agent_number: int, values: dict[str, str]) -> str:
    others = []
    for number in [1, 2, 3]:
        value = values[f"agent_{number}"]
        if number != agent_number and value != "-":
            others.append(value)
    if not others:
        return "no other agents"
    if len(others) == 1:
        return others[0]
    return ", ".join(others[:-1]) + f", and {others[-1]}"


def render_prompt(debate_path: Path, values: dict[str, str], agent_number: int, agent_name: str, round_number: int) -> str:
    max_rounds = int(values["max_rounds"])
    if round_number < 1:
        raise ValueError("--round must be at least 1.")
    if round_number > max_rounds:
        raise ValueError(f"--round must be <= max rounds ({max_rounds}).")

    other_agents = format_other_agents(agent_number, values)
    initial_proposal_rule = (
        "- Because you are Agent 1 in Round 1, write the first proposal directly in the PROPOSAL section."
        if agent_number == 1 and round_number == 1
        else "- Read the current proposal first, then edit the existing document in place."
    )

    return f"""You are {agent_name} in a technical debate with {other_agents}.
This is Round {round_number} of {max_rounds}.

Debate topic: {values["topic"]}
Debate file: {debate_path.resolve()}

Instructions:
- Open the debate file and edit that markdown file directly. Do not answer in chat format.
{initial_proposal_rule}
- Treat it as a living document. Disagree by striking through the exact claim and writing the counter directly below it.
- Tag every substantive edit with [A{agent_number}-R{round_number}].
- Update the dispute log whenever a disagreement opens, closes, or gets parked.

Evidence rules:
- Every problem statement must include inline evidence: file:line, logs, counts, runtime output, or actual vs expected values.
- Every proposed fix must cite the code it changes and what behavior changes.
- Accepting another agent's claim requires your own verification against source or runtime evidence.
- If you cannot produce evidence, move the point to the Parking Lot instead of the Proposal.

Quality rules:
- Prefer the minimum viable fix.
- Reject speculative infrastructure and unrelated enhancements.
- Flag both over-engineering and under-engineering.
- Stay scoped to the debate question.

Convergence rules:
- Do not leave STATUS: CONVERGED in place while any dispute remains OPEN.
- Only converge when the proposal is coherent and every dispute is CLOSED or PARKED.
- If the proposal is not ready, keep or revert STATUS: OPEN and explain why.
"""


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    debate_path = Path(args.debate_file)
    if not debate_path.exists():
        raise SystemExit(f"Debate file does not exist: {debate_path}")

    content = debate_path.read_text(encoding="utf-8")
    values = parse_header(content)
    agent_number, agent_name = resolve_agent(values, args.agent_name, args.agent_number)
    prompt = render_prompt(debate_path, values, agent_number, agent_name, args.round)

    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(prompt, encoding="utf-8")
        print(f"Wrote prompt: {output_path}")
        return

    print(prompt)


if __name__ == "__main__":
    main()
