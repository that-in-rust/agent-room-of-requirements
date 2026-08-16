---
name: python-coder-01
description: Reliability-first Python skill for implementing, refactoring, or reviewing Python packages, CLIs, services, scripts, async code, tests, and typed modules. Use when work needs type hints, dataclasses, boundary parsing, exception design, context managers, asyncio cancellation, packaging, pytest or unittest strategy, ruff, mypy, pyright, or runtime safety.
---

# Python Reliability

## Overview

Use this skill when the task is primarily about writing, refactoring, or reviewing reliable Python across packages, CLIs, services, scripts, automation, and async workflows. Bias toward code that keeps runtime boundaries explicit, uses typing to document and check contracts, manages resources deterministically, and treats exceptions and cancellation as first-class behavior.

Preserve the repository's supported Python versions, packaging tool, formatter, linter, type checker, and test runner unless the request explicitly includes a migration.

## When To Use

- `.py`, `pyproject.toml`, package layout, CLI, automation, service, worker, or test code where correctness matters more than quick scripting.
- Typed module design, dataclasses, protocols, parsing, serialization, filesystem IO, subprocess work, context managers, or asyncio.
- Refactors that need clearer interfaces, fewer implicit globals, safer exceptions, or stronger test seams.
- Code reviews where the real question is whether the Python survives bad inputs, partial state, cancellation, import side effects, or packaging drift.

## Mode Selection

Choose one or more modes before planning or coding:

- `Core Python Mode`: modules, functions, classes, imports, naming, mutability, errors, logging, and PEP 8 fit.
- `Typing Mode`: annotations, `Protocol`, `TypedDict`, dataclasses, generics, `Any` containment, mypy, or pyright.
- `Boundary Mode`: CLI args, env vars, JSON, files, network payloads, database rows, and parse-don't-validate flows.
- `Async Mode`: asyncio tasks, task groups, cancellation, timeouts, shielding, streams, and blocking-call isolation.
- `Resource Mode`: context managers, file handles, temp dirs, subprocesses, sockets, cleanup, and idempotent teardown.
- `Packaging Mode`: `pyproject.toml`, dependency groups, entry points, package data, version targets, and build metadata.
- `Testing Mode`: pytest, unittest, fixtures, monkeypatching, property tests, integration tests, and failure readability.
- `Review Mode`: anti-pattern scan, import safety, global state, exception hygiene, quality gates, and release risk.

## Workflow

1. Classify the Python surface.
- Name the surface first: library module, CLI, script, package config, async workflow, IO adapter, test suite, or review pass.
- State whether the main risk is bad input, hidden `Any`, mutable state, resource leaks, cancellation, import side effects, or package compatibility.

2. Write executable requirements when behavior is unclear.
- Use `REQ-PY-<NNN>.<REV>` identifiers.
- Express behavior as `WHEN...THEN...SHALL`.
- Replace vague words such as "pythonic", "safe", "clean", or "robust" with observable behavior or quality gates.

3. Load references progressively.
- Read [Reference map](./references/reference-map.md) first.
- Open the relevant sections in [Python reliability reference](./references/python-reliability-reference.md).
- Finish with [Python quality gates and anti-patterns](./references/python-quality-gates-and-anti-patterns.md).

4. Design boundaries before implementation.
- Parse untrusted input at the boundary and keep the core typed.
- Prefer small pure functions, explicit dependencies, dataclasses for value data, and protocols for behavior seams.
- Keep import-time side effects out of reusable modules.

5. Treat resources and async as correctness-sensitive.
- Use context managers for acquired resources.
- Preserve asyncio cancellation and timeout behavior.
- Avoid blocking the event loop; move blocking work to the appropriate executor or synchronous layer.

6. Verify with repo-native gates.
- Prefer existing commands: `python -m pytest`, `python -m unittest`, `ruff check`, `ruff format --check`, `black --check`, `mypy`, `pyright`, or package build checks when configured.
- Use the lightest test that proves behavior, but include real boundary tests when IO, packaging, subprocesses, or async behavior is part of the requirement.

## Output Expectations

Return results in this order when planning or reviewing:

1. `Python Work Mode`
2. `Executable Requirements`
3. `Boundary And Type Design`
4. `Async/Resource Constraints`
5. `Verification Matrix`
6. `Implementation Plan`
7. `Quality Gates`
8. `Open Questions`

Use this traceability shape when requirements exist:

| req_id | test_id | test_type | assertion | target |
| --- | --- | --- | --- | --- |

## Guardrails

- Do not introduce bare `except`, mutable default arguments, broad `Any`, import-time network calls, or resource acquisition without cleanup.
- Do not swallow `asyncio.CancelledError` in generic exception handling.
- Do not rely on `assert` for runtime validation of external input.
- Do not add a new formatter, linter, package manager, or type checker when the repo already has one unless migration is requested.
- Do not treat type hints as proof that runtime data is valid; parse and validate at trust boundaries.

## References

- [Reference map](./references/reference-map.md)
- [Python reliability reference](./references/python-reliability-reference.md)
- [Python quality gates and anti-patterns](./references/python-quality-gates-and-anti-patterns.md)
- [Sources and research brief](./references/sources-and-research-brief.md)
