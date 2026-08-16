# Python Reliability Reference

## Premise

Reliable Python comes from making dynamic behavior explicit where it matters: typed public contracts, parsed boundaries, deterministic cleanup, import-safe modules, and tests that exercise failure behavior. Type hints are useful guardrails, but runtime inputs still need validation.

This reference is not a tutorial. It is a reliability checklist for LLM-authored Python work.

## Pattern Scoreboard

| ID | Score | Pattern |
| --- | ---: | --- |
| `PY1-01` | 97 | Parse untrusted data at the boundary |
| `PY1-02` | 95 | Keep `Any` contained and justified |
| `PY1-03` | 94 | Use dataclasses for value data with explicit defaults |
| `PY1-04` | 93 | Prefer protocols for behavior seams |
| `PY1-05` | 92 | Use exceptions for exceptional failures and typed returns for expected outcomes |
| `PY1-06` | 91 | Acquire resources with context managers |
| `PY1-07` | 94 | Preserve asyncio cancellation |
| `PY1-08` | 90 | Avoid import-time side effects in reusable modules |
| `PY1-09` | 89 | Use pathlib and explicit encodings for filesystem work |
| `PY1-10` | 88 | Keep logging structured enough for diagnosis |
| `PY1-11` | 88 | Use pytest or unittest fixtures to isolate state |
| `PY1-12` | 87 | Preserve package metadata and supported Python versions |
| `PY1-13` | 86 | Prefer dependency injection over monkeypatching production code |
| `PY1-14` | 85 | Test errors, cleanup, and boundary behavior directly |
| `PY1-15` | 84 | Run formatter, linter, type checker, and tests as a single gate |

## 1. API, Typing, And Data Design

### `PY1-02` Keep `Any` contained and justified

Use `Any` only at edges where the shape is genuinely unknown. Narrow it immediately with parsing, validation, or explicit runtime checks.

Prefer:

- `object` when callers must prove the type before use.
- `Protocol` when behavior matters more than concrete class.
- `TypedDict` or dataclasses when dictionary shapes are stable.
- Type aliases for repeated domain concepts.

Avoid spreading `Any` into the core. One uncontained `Any` can erase the value of a typed module.

### `PY1-03` Use dataclasses for value data with explicit defaults

Use dataclasses for simple values and state snapshots. Prefer `frozen=True` when mutation is not part of the model, `slots=True` when appropriate for memory and attribute discipline, and `field(default_factory=...)` for mutable defaults.

```python
from dataclasses import dataclass, field


@dataclass(frozen=True, slots=True)
class ImportReport:
    source: str
    accepted_rows: int
    warnings: list[str] = field(default_factory=list)
```

Avoid mutable default arguments in functions and dataclasses. Use factories for lists, dicts, sets, and generated values.

### `PY1-04` Prefer protocols for behavior seams

Use `Protocol` when the code needs a capability rather than a concrete class. This keeps tests lightweight and reduces inheritance pressure.

Good seams:

- clock providers
- filesystem adapters
- HTTP clients
- repositories
- event publishers
- command runners

## 2. Boundary Parsing And Exceptions

### `PY1-01` Parse untrusted data at the boundary

CLI args, env vars, JSON, HTTP payloads, CSV rows, subprocess output, and database rows are runtime data. Type hints alone do not validate them.

Boundary rules:

- Decode with explicit encodings.
- Validate shape and required fields before domain logic.
- Convert primitive strings into domain values early.
- Return or raise errors with enough context to repair the input.

### `PY1-05` Use exceptions and typed returns deliberately

Use exceptions for unexpected or exceptional failures. Use typed return values for expected business outcomes that callers must handle.

Avoid:

- bare `except:`
- catching `Exception` and returning `None`
- hiding file, network, or parse errors behind vague messages
- using `assert` for runtime validation of external input

### `PY1-10` Keep logging diagnosable

Library code should not rely on `print` for operational behavior. Use logging at adapters and orchestration boundaries. Keep messages actionable and avoid logging secrets.

## 3. Async And Resource Reliability

### `PY1-06` Acquire resources with context managers

Use `with` or `async with` for files, locks, temporary directories, network clients, database sessions, and custom resource lifecycles.

If a resource requires setup and teardown, consider `contextlib.contextmanager` or `contextlib.asynccontextmanager` to make the lifecycle explicit.

### `PY1-07` Preserve asyncio cancellation

Cancellation is part of asyncio control flow. Do not swallow `asyncio.CancelledError` in broad handlers. If cleanup is needed, perform cleanup and re-raise cancellation.

```python
import asyncio


async def run_job() -> None:
    try:
        await do_work()
    except asyncio.CancelledError:
        await cleanup()
        raise
```

Use `asyncio.TaskGroup` when the project target supports it and sibling task ownership should be explicit. Preserve older supported Python targets when the repo requires them.

### Blocking work in async code

Do not run blocking file, CPU, subprocess, or network calls directly on the event loop. Keep the function synchronous or isolate blocking work with the repository's accepted executor/thread pattern.

## 4. Testing And Fixtures

Test the behavior that can fail:

- malformed input and missing fields
- exception messages and typed error paths
- context manager cleanup
- cancellation and timeout behavior
- import safety for reusable modules
- package entry points and CLI exit codes
- filesystem behavior with temp paths

Prefer pytest fixtures when the repo uses pytest. Use `unittest` when it is the established local stack. Keep monkeypatching narrow and restore state reliably.

## 5. Packaging And Tooling

Preserve the repo's packaging system. Inspect `pyproject.toml`, `setup.cfg`, `setup.py`, `tox.ini`, `noxfile.py`, `requirements*.txt`, and lock files before changing tools.

Common gates:

- `python -m pytest`
- `python -m unittest`
- `ruff check .`
- `ruff format --check .`
- `black --check .`
- `mypy .`
- `pyright`
- `python -m build`

Use the command shape already present in CI or project docs when available.

## Python Review Questions

- Does untrusted data become typed before domain logic?
- Is every `Any` contained near a boundary?
- Are mutable defaults avoided?
- Are resources closed on success, error, and cancellation?
- Does async code preserve `CancelledError`?
- Are import-time side effects avoided in reusable modules?
- Do tests cover malformed input, cleanup, and expected failures?
