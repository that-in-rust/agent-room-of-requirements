# Reference Map

Use this file to route quickly before loading the full Python references.

## Jump Points

- `Pattern Scoreboard`: fast triage of the highest-value reliability patterns.
- `1. API, Typing, And Data Design`: type hints, dataclasses, protocols, `Any` containment, and module APIs.
- `2. Boundary Parsing And Exceptions`: untrusted input, exception surfaces, logging, and diagnostics.
- `3. Async And Resource Reliability`: asyncio cancellation, task ownership, context managers, and cleanup.
- `4. Testing And Fixtures`: pytest, unittest, fixtures, monkeypatching, property tests, and failure readability.
- `5. Packaging And Tooling`: `pyproject.toml`, package layout, entry points, ruff, black, mypy, and pyright.
- `High-Value Anti-Patterns`: mistakes to reject before finishing.
- `Default Reliability Stack`: compact final checklist.

## Section Search

- `rg '^##|^###' references/python-reliability-reference.md`
- `rg '^##|^###' references/python-quality-gates-and-anti-patterns.md`
- `rg 'Pattern Scoreboard|High-Value Anti-Patterns|Default Reliability Stack' references/*.md`

## Use Order

1. Read `Pattern Scoreboard`.
2. Open only the sections that match the boundary being touched.
3. Finish with `High-Value Anti-Patterns` and `Default Reliability Stack`.
