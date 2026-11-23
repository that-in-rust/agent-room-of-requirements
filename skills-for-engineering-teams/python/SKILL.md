---
name: python
description: >-
  Reliability-first Python for implementing, refactoring or reviewing packages, CLIs,
  services, scripts, async code, tests and typed modules: classify the surface, name the
  main risk, pick modes (core, typing, boundary, async, resource, packaging, testing,
  review), apply the PY1 pattern set, and prove the result with the repository's own
  gates. Use when the task touches .py files or pyproject.toml and needs type hints,
  dataclasses, Protocol seams, boundary parsing, exception design, context managers,
  asyncio cancellation or timeouts, subprocess or file handling, packaging metadata,
  pytest or unittest strategy, or ruff, black, mypy or pyright gates; or when asked to
  "harden this script", "add types", "review this Python" or "why does this hang on
  cancel". Not for framework doctrine (Django, FastAPI, Flask), notebook exploration,
  deployment or distributed-system design, choosing a toolchain for a greenfield
  project, Rust or TypeScript code, or a throwaway script where speed matters more than
  correctness.
---

# Python Reliability

## Purpose

This skill makes Python work reliable by making dynamic behaviour explicit where it
matters: parsed boundaries, typed contracts, deterministic cleanup, preserved
cancellation, import-safe modules, and tests that exercise failure paths. It is a gate
and a router for an agent or reviewer, not a Python tutorial: it tells you which risks to
name, which rules apply, and which commands prove the result.

One rule stands above the rest: **preserve the repository's supported Python versions,
packaging tool, formatter, linter, type checker and test runner unless the request
explicitly includes a migration.** Hardening upgrades the code, not the toolchain.

## When to use

- `.py`, `pyproject.toml`, package layout, CLI, automation, service, worker or test code
  where correctness matters more than quick scripting.
- Typed module design, dataclasses, protocols, parsing, serialization, filesystem IO,
  subprocess work, context managers or asyncio.
- Refactors that need clearer interfaces, fewer implicit globals, safer exceptions or
  stronger test seams.
- Code reviews where the real question is whether the Python survives bad inputs,
  partial state, cancellation, import side effects or packaging drift.
- A change that is believed complete and needs a defensible ship, bounce or escalate
  decision.

Requests that should trigger this skill:

1. "Harden this CSV import CLI. It crashes on malformed rows and nobody knows which row."
2. "Turn this Python request into executable requirements, a boundary and type design,
   a verification matrix and quality gates."
3. "Our asyncio worker hangs on shutdown. Find out why and fix it."
4. "Review this PR to `billing/client.py` before we ship. Does it leak connections?"
5. "Add type hints to the `orders` package without changing what mypy and CI already do."

Requests that should not trigger it:

1. "Restyle this Django template" or "design the FastAPI router layout". That is
   framework work; use the framework's own guidance and keep only the general boundary
   and cleanup rules from here.
2. "Explore this dataset in a notebook." Exploratory notebooks are outside this skill. A
   notebook-derived ETL becomes a fit once it is turned into a tested module.
3. "Which formatter should our new project use?" Greenfield tool choice is out of scope;
   this skill discovers and preserves what a repository already configured.

Borderline cases:

- A throwaway script. Use the skill only when correctness matters more than speed. A
  small script may stay less formal as long as its effects and failures stay explicit.
- A typo or one-line mechanical fix. Do not activate the whole workflow for every `.py`
  edit. Name the mode and the gate, make the fix, run the gate.
- Rust or TypeScript files in the same repository belong to the sibling language skills.

## Workflow

1. **Classify the surface.** Name it first: library module, CLI, script, package config,
   async workflow, IO adapter, test suite, or review pass.
2. **Name the main risk.** Bad input, hidden `Any`, mutable state, resource leaks,
   cancellation loss, import side effects, or package compatibility. Take a short risk
   inventory before choosing controls: runtime inputs, public API, dynamic types, mutable
   state, expected and exceptional failures, resources, concurrency, imports, filesystem
   effects, package surface, supported versions.
3. **Pick one or more modes** (next section). Mode selection is risk selection. The plan
   must name the Python Work Mode and the surface before any implementation.
4. **Discover the repository's toolchain** before proposing commands (see
   [Commands](#commands)). Record the supported Python versions and the exact gate
   commands CI uses. Sample three neighbouring files to learn local style.
5. **Write executable requirements when behaviour is unclear.** Use
   `REQ-PY-<NNN>.<REV>` identifiers and `WHEN ... THEN ... SHALL ...` clauses. Replace
   vague words such as "pythonic", "safe", "clean" or "robust" with observable behaviour
   or a quality gate. Write them before implementation; backfilling requirements after
   the code exists is not acceptable.
6. **Load depth progressively.** Read the PY1 table in this file, then open only the
   parts of `reference.md` that match the boundary being touched, and always finish with
   the anti-pattern sweep and the Default Reliability Stack.
7. **Design boundaries and failure paths before implementation.** Parse untrusted input
   at the boundary and keep the core typed. Prefer small pure functions, explicit
   dependencies, dataclasses for value data and protocols for behaviour seams. Keep
   import-time side effects out of reusable modules.
8. **Treat resources and async as correctness-sensitive.** Use context managers for
   acquired resources. Preserve asyncio cancellation and timeout behaviour. Do not block
   the event loop; move blocking work to the appropriate executor or keep that layer
   synchronous.
9. **Implement behaviour-first.** Write the adverse tests for the affected boundary
   (malformed input, cleanup on failure, cancellation) before or with the change. Change
   one reviewable boundary at a time and preserve public behaviour.
10. **Verify with repo-native gates.** Run the configured formatter, linter, type checker
    and tests as one gate. Use the lightest test that proves the behaviour, but include
    real boundary tests when IO, packaging, subprocesses or async behaviour is part of
    the requirement.
11. **Run the handoff gate** (sweep, stack, battery, review pass) and hand back the
    result in the output order below, ending with open questions.

For review-only work, skip steps 5 to 9 and go straight to the handoff gate.

## Modes

Choose one or more before planning or coding. Each mode names a scope, the risk it
targets, the PY1 patterns that apply and the proof to ask for.

| Mode | Pick it when the work touches | Main risk | Patterns | Typical proof |
| --- | --- | --- | --- | --- |
| Core Python | modules, functions, classes, imports, naming, mutability, errors, logging, PEP 8 fit | mutable state, vague errors, import effects | PY1-05, PY1-08, PY1-10 | unit tests, linter, isolated import |
| Typing | annotations, `Protocol`, `TypedDict`, dataclasses, generics, `Any` containment, mypy or pyright | hidden `Any` | PY1-02, PY1-03, PY1-04 | the repo's type checker plus runtime tests |
| Boundary | CLI args, env vars, JSON, files, network payloads, database rows, parse-don't-validate flows | bad input reaching the core | PY1-01, PY1-05, PY1-09 | malformed-input tests, type checker |
| Async | asyncio tasks, task groups, cancellation, timeouts, shielding, streams, blocking-call isolation | cancellation loss, stalled loop | PY1-07 and the blocking rule | cancellation and timeout tests |
| Resource | context managers, file handles, temp dirs, subprocesses, sockets, cleanup, idempotent teardown | leaks, partial state | PY1-06, PY1-09 | cleanup tests on success, error and cancellation |
| Packaging | `pyproject.toml`, dependency groups, entry points, package data, version targets, build metadata | package compatibility drift | PY1-12, PY1-08, PY1-15 | build, clean install, entry-point run |
| Testing | pytest, unittest, fixtures, monkeypatching, property tests, integration tests, failure readability | untested failure paths, leaking fixtures | PY1-11, PY1-13, PY1-14 | the tests themselves, order randomisation where configured |
| Review | anti-pattern scan, import safety, global state, exception hygiene, quality gates, release risk | known hazards shipped | all, through the handoff gate | gate record |

Common combinations:

- CLI that parses untrusted CSV: Boundary + Testing.
- Async worker that hangs on shutdown: Async + Resource + Testing.
- Adding types to a legacy package: Typing + Review, staged one module per cycle.
- Subprocess wrapper script: Resource + Boundary (typed errors, context-managed temp
  directory).
- Release of a library: Packaging + Review.

### Core Python Mode

Pick it for ordinary module work. Keep functions small and pure where possible, pass
dependencies in rather than reaching for module globals, never use mutable default
arguments, raise specific exceptions with context, log instead of printing in library
code, and keep the module importable without side effects. Follow the repository's
existing naming and layout; PEP 8 is the fallback where the repository has no rule.

### Typing Mode

Pick it when the contract between modules is the problem. Annotate public functions and
important internal seams. Contain `Any` at the edge and narrow it at once. Use
dataclasses or `TypedDict` for stable shapes and `Protocol` for capabilities. Run the
type checker the repository already uses, and remember that a checker pass says nothing
about runtime data.

### Boundary Mode

Pick it whenever data enters from outside the process: CLI args, env vars, JSON, HTTP
payloads, CSV rows, subprocess output, database rows, files. Parse once at the edge into
domain values; reject with enough context to repair the input; let nothing unparsed
reach domain logic.

### Async Mode

Pick it when the code uses asyncio. Specify cancellation behaviour, cleanup, re-raise and
timeout bounds together. Give every task an owner. Keep blocking calls off the event
loop. Keep synchronous code synchronous when async adds no concurrency value.

### Resource Mode

Pick it when the code acquires something that must be released: files, locks, temp
directories, subprocesses, sockets, clients, sessions. Every acquisition gets a context
manager or an explicit cleanup path that runs on success, error and cancellation.
Teardown must be safe to run twice.

### Packaging Mode

Pick it when metadata, layout, entry points, dependencies or supported versions change.
Inspect `pyproject.toml`, `setup.cfg`, `setup.py`, `tox.ini`, `noxfile.py`,
`requirements*.txt` and lock files before changing anything. Do not change
`requires-python` or the build backend as a side effect of another change.

### Testing Mode

Pick it when the work is the tests, or when the change has failure paths that no test
reaches. Use pytest fixtures when the repository uses pytest and `unittest` when that is
the established stack. Test the behaviour that can fail. Keep monkeypatching narrow and
restore state reliably.

### Review Mode

Pick it for a diff or a module someone else wrote, and at the end of your own work. Run
the handoff gate in [Quality gates](#quality-gates): sweep the eleven anti-patterns,
check the nine-item stack, run the command battery, answer the eight review prompts.

## The PY1 pattern set

Scores are the author's adoption priorities on a 0 to 100 scale. They are not
measurements, probabilities, severities or defect-reduction figures. Use them to decide
what to look at first; every pattern that applies to the change is still required.

| ID | Score | Pattern | Proved by |
| --- | ---: | --- | --- |
| `PY1-01` | 97 | Parse untrusted data at the boundary | malformed-input and missing-field tests |
| `PY1-02` | 95 | Keep `Any` contained and justified | type checker; review of each `Any` |
| `PY1-03` | 94 | Use dataclasses for value data with explicit defaults | linter (mutable defaults); repeated-instance test |
| `PY1-04` | 93 | Prefer protocols for behaviour seams | tests that substitute a fake through the seam |
| `PY1-05` | 92 | Use exceptions for exceptional failures and typed returns for expected outcomes | error-path tests asserting type, message and cause |
| `PY1-06` | 91 | Acquire resources with context managers | cleanup tests on success, error, cancellation |
| `PY1-07` | 94 | Preserve asyncio cancellation | a test that cancels after the task reached an await |
| `PY1-08` | 90 | Avoid import-time side effects in reusable modules | import in a clean subprocess |
| `PY1-09` | 89 | Use pathlib and explicit encodings for filesystem work | linter; temp-path tests |
| `PY1-10` | 88 | Keep logging structured enough for diagnosis | search for `print` outside CLI paths; log capture test |
| `PY1-11` | 88 | Use pytest or unittest fixtures to isolate state | test-order randomisation; no writes outside temp paths |
| `PY1-12` | 87 | Preserve package metadata and supported Python versions | build; diff of metadata; version matrix |
| `PY1-13` | 86 | Prefer dependency injection over monkeypatching production code | tests pass a fake instead of patching |
| `PY1-14` | 85 | Test errors, cleanup, and boundary behaviour directly | the adverse tests exist and fail when the behaviour is removed |
| `PY1-15` | 84 | Run formatter, linter, type checker, and tests as a single gate | recorded commands and exit codes |

How to read the order:

- Context beats score. Cancellation dominates in an async worker, import safety in a
  library, explicit encodings in file interchange, whatever the numbers say.
- Under time pressure, look first at the four items that appear in both the anti-pattern
  table and the reliability stack: boundary validation, mutable defaults, cancellation
  preservation, import-time side effects.
- Reorder from the repository's own incident history or from what its linter can enforce
  once that information exists. `PY1-09` is largely mechanical and lintable; `PY1-15` is
  what makes the others enforceable.
- Never skip a low-scored pattern that applies, and never settle conflicting evidence by
  score.

## Rules

Each rule states which implicit behaviour becomes explicit. The proving gate is in the
table above.

### Repository preservation

- Do not add a new formatter, linter, package manager or type checker when the repository
  already has one, unless migration is requested. Example: do not introduce Ruff or
  pyright into a black-plus-flake8 repository, and do not add pyright to a mypy
  repository as part of a bug fix.
- Adopt safety rules at once (fix a mutable default, do not preserve a bare `except`).
  Adapt style, structure, packaging and tooling to the repository.
- Keep one behaviour change per change set. Combining checker, formatter, packaging and
  behaviour changes hides causality and makes rollback hard.
- In a loose codebase, strictness applied file by file can create two dialects. Use a
  bounded migration instead: one module per cycle, behind the existing gates.

### Boundary parsing (`PY1-01`, `PY1-09`)

- CLI args, env vars, JSON, HTTP payloads, CSV rows, subprocess output and database rows
  are runtime data. Type hints alone do not validate them.
- Decode with explicit encodings.
- Validate shape and required fields before domain logic.
- Convert primitive strings into domain values early.
- Return or raise errors with enough context to repair the input: source, position,
  field, what was expected.
- Validate in one place per boundary. Scattered validation duplicates badly and drifts.
- Use `pathlib.Path` for paths. String path handling hides OS and relative-path bugs.
- A dataclass or `TypedDict` describes a shape; neither validates runtime data. Do not
  use dataclass guidance as a substitute for parsing untrusted JSON.

### Typing and data (`PY1-02`, `PY1-03`, `PY1-04`)

- Use `Any` only at edges where the shape is truly unknown. Narrow it at once with
  parsing, validation or explicit runtime checks. One uncontained `Any` can erase the
  value of a typed module.
- Prefer `object` when callers must prove the type before use, `Protocol` when behaviour
  matters more than the concrete class, `TypedDict` or dataclasses when dictionary shapes
  are stable, and type aliases for repeated domain concepts.
- Do not reduce `Any` counts with casts. A cast hides the unknown instead of resolving it.
- Use dataclasses for simple values and state snapshots. Prefer `frozen=True` when
  mutation is not part of the model, `slots=True` when appropriate for memory and
  attribute discipline, and `field(default_factory=...)` for mutable defaults.
- Do not use `frozen` or `slots` when the model legitimately mutates, needs dynamic
  attributes, or a serializer requires otherwise. `slots=True` is not a default.
- No mutable default arguments in functions or dataclasses. Use factories for lists,
  dicts, sets and generated values.
- Use `Protocol` when the code needs a capability rather than a concrete class. Good
  seams: clock providers, filesystem adapters, HTTP clients, repositories, event
  publishers, command runners.
- Wrap legacy dynamic code with a typed adapter. Unknown values may enter the adapter;
  they may not escape into the core.

### Errors and logging (`PY1-05`, `PY1-10`)

- Use exceptions for unexpected or exceptional failures. Use typed return values for
  expected business outcomes that callers must handle.
- No bare `except:`. No catching `Exception` and returning `None`. No hiding file,
  network or parse errors behind vague messages. No `assert` for runtime validation of
  external input (`python -O` removes asserts). `assert` stays fine in tests and for
  internal invariants.
- When translating an exception, chain it (`raise NewError(...) from exc`) so the cause
  survives.
- Do not let these distinctions collapse: unknown into `Any`, failure into `None`,
  cancellation into success, shared state into hidden coupling.
- Library code does not use `print` for operational behaviour. Log at adapters and
  orchestration boundaries. CLI user output may print. A pure domain layer may return
  diagnostics instead of logging.
- Keep messages actionable: identifiers, counts, durations. Never log secrets or raw
  payloads. Let the application, not the library, configure handlers.

### Resources (`PY1-06`)

- Use `with` or `async with` for files, locks, temporary directories, network clients,
  database sessions and custom resource lifecycles.
- If a resource needs setup and teardown, use `contextlib.contextmanager` or
  `contextlib.asynccontextmanager` to make the lifecycle explicit.
- Resources close on success, on error and on cancellation. Do not rely on garbage
  collection for cleanup.
- Teardown is idempotent. A second call must not raise.
- Write files so that a failure cannot leave a partial result where a reader expects a
  complete one (write to a temporary name, then replace).

### Async (`PY1-07` and the blocking rule)

- Cancellation is part of asyncio control flow. Do not swallow `asyncio.CancelledError`
  in broad handlers. If cleanup is needed, clean up and re-raise.
- Cleanup can itself raise and mask the cancellation. Keep it small, or scope or shield
  it deliberately. Shielding cleanup can be right during shutdown and is dangerous as a
  habit.
- Use `asyncio.TaskGroup` when the project target supports it and sibling task ownership
  should be explicit. Preserve older supported Python targets when the repository
  requires them.
- Do not run blocking file, CPU, subprocess or network calls directly on the event loop.
  One synchronous call on the loop can stall every concurrent task. Keep the function
  synchronous or isolate the blocking work with the repository's accepted executor or
  thread pattern.
- State cancellation behaviour, cleanup, re-raise and the timeout bound together. Do not
  hide either cancellation or a timeout behind a broad `except`.
- Do not add async without a concurrency need.

### Imports (`PY1-08`)

- Importing a reusable module must not open network connections, read or write files,
  start threads, parse arguments or configure logging. Put effects behind functions,
  factories or the CLI entry point.
- No module-level clients. Build them in a factory and pass them in.
- A module-level cache is acceptable only if it is lazy, deterministic, resettable,
  thread-safe and tested. A cheap pure constant is fine.

### Testing (`PY1-11`, `PY1-13`, `PY1-14`)

Test the behaviour that can fail:

- malformed input and missing fields
- exception messages and typed error paths
- context manager cleanup
- cancellation and timeout behaviour
- import safety for reusable modules
- package entry points and CLI exit codes
- filesystem behaviour with temp paths

And:

- Prefer pytest fixtures when the repository uses pytest. Use `unittest` when it is the
  established local stack.
- Prefer passing a dependency in over monkeypatching production code. When you must
  monkeypatch, keep it narrow and restore state reliably.
- Never write to the real home directory or working tree from a test. Use temp paths.
- A cancellation test must schedule the work and let it reach an `await` before
  cancelling. Otherwise it proves nothing.
- Do not mock away the cleanup you are trying to prove.
- Happy-path tests do not prove cleanup, cancellation, import safety or package
  compatibility.

### Packaging and tooling (`PY1-12`, `PY1-15`)

- Preserve the repository's packaging system, metadata and supported Python versions.
- Use the command shape already present in CI or project docs.
- Run formatter, linter, type checker and tests as one gate; skip one only with a stated
  reason.
- Type hints are not proof that runtime data is valid. A type-checker pass does not parse
  runtime data; a lint pass does not prove cleanup; a unit-test pass does not prove
  import, packaging, cancellation or CLI behaviour.

## Where the guidance offers two positions

Both positions are kept. The right-hand column says what selects each.

| Question | Position A | Position B | What selects |
| --- | --- | --- | --- |
| How much gate for each change? | Verify all nine stack items and run the gates before finishing any Python work. | Tier it: routine changes get the sweep plus the eight-prompt pass; releases, new modules, async boundaries and boundary-heavy code get the full stack plus the battery. | A is the default. B applies only where the team has adopted tiering and audits tier assignment. The sweep is never skipped in either. |
| Protocol or concrete class? | Prefer protocols for behaviour seams. | Inject the concrete dependency first; add a protocol only when a second implementation or a test double justifies it. | Use a protocol where substitution or testing needs it now. Otherwise inject the concrete object and keep the protocol for later. |
| Read everything or route? | Read the pattern table, open only the matching sections, close with the gate. | Read all of it. | Route for a point question on one boundary. Read fully for activation decisions, audits, a task that spans several boundaries, or when you cannot classify the question. |
| Formal requirements? | Write `REQ-PY` requirements when behaviour is unclear. | Every nontrivial change needs modes, requirements and a traceability table. | Trivial mechanical fixes skip formal requirements but still name the mode and the gate. Anything with a behaviour change gets all three. |
| Which pattern first? | Scoreboard order. | The pattern that matches the dominant risk; under time pressure the four doubly listed items. | Use risk order whenever you can name the risk. Fall back to scoreboard order for a general review. |
| `ruff check .` or `ruff check`? | Commands with an explicit path (`ruff check .`, `mypy .`). | Bare commands that rely on configuration (`ruff check`, `mypy`). | Whatever CI or the project docs run. If neither exists, use the explicit path from the repository root. |
| Re-gate after a bounce? | Verify each bounced item, then run one full fresh sweep. | Skip the fresh sweep for a one-token fix such as adding `default_factory`. | Skip only when the record says so and names the fix. |
| Activate on every `.py` file? | Use for `.py` work where correctness matters more than quick scripting. | Do not activate for every `.py` edit or impose service controls on disposable scripts. | Activate when there is a runtime boundary, a lifecycle, a public contract or a release at stake. |
| Is `print` allowed? | Not for operational behaviour in libraries. | Yes for CLI user output. | The layer: entry points may print for the user; reusable modules log or return diagnostics. |
| How much can one pass take on? | One primary task, up to 10 source files, up to 3 delegated subtasks, plus a written completion audit. | One audience, one decision, up to 12 source documents, one verification checklist. | A is for implementation work, B for a review or reference decision. Both are provisional planning limits, not measured ones; split the work when either is exceeded. |

## Templates

### Executable requirement

```text
REQ-PY-001.1
WHEN the CSV row lacks an `id` value
THEN the importer SHALL reject the row with an error naming the file and line number
AND SHALL continue with the next row
AND SHALL exit with status 1 after all rows are processed
```

Rules: one observable behaviour per clause; bump the revision suffix (`.1` to `.2`) when
the requirement changes; every requirement maps to at least one runnable test. The
general method for writing and sizing such requirements is in
[A03 Executable Specs](../../A03-Executable-Specs01.md).

### Traceability table

| req_id | test_id | test_type | assertion | target |
| --- | --- | --- | --- | --- |
| REQ-PY-001.1 | `test_missing_id_is_rejected_with_location` | unit | raises `RowError` matching `orders.csv:7: missing required field 'id'` | `importer.orders.parse_order` |
| REQ-PY-001.1 | `test_bad_rows_are_reported_not_dropped` | integration (temp file) | one accepted row, one warning with line 3 | `importer.orders.load_orders` |

A set of modes and requirements without this table is intention, not evidence.

### Boundary parser into a typed core

```python
from __future__ import annotations

import csv
from dataclasses import dataclass, field
from decimal import Decimal, InvalidOperation
from pathlib import Path


class RowError(ValueError):
    """One CSV row that cannot become an Order."""

    def __init__(self, source: str, line: int, reason: str) -> None:
        super().__init__(f"{source}:{line}: {reason}")
        self.source = source
        self.line = line
        self.reason = reason


@dataclass(frozen=True, slots=True)
class Order:
    order_id: str
    amount: Decimal


@dataclass(frozen=True, slots=True)
class ImportReport:
    source: str
    accepted_rows: int
    warnings: list[str] = field(default_factory=list)


def parse_order(raw: dict[str, str | None], *, source: str, line: int) -> Order:
    """Boundary parser: raw CSV strings in, a valid Order or a RowError out."""
    order_id = (raw.get("id") or "").strip()
    if not order_id:
        raise RowError(source, line, "missing required field 'id'")
    amount_text = (raw.get("amount") or "").strip()
    try:
        amount = Decimal(amount_text)
    except InvalidOperation as exc:
        raise RowError(source, line, f"amount {amount_text!r} is not a decimal number") from exc
    if not amount.is_finite() or amount < 0:
        raise RowError(source, line, f"amount {amount_text!r} must be a finite number >= 0")
    return Order(order_id=order_id, amount=amount)


def load_orders(path: Path) -> tuple[list[Order], ImportReport]:
    """Bad rows are an expected outcome: collect them. An unreadable file is not: let it raise."""
    orders: list[Order] = []
    warnings: list[str] = []
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        for raw in reader:
            try:
                orders.append(parse_order(raw, source=path.name, line=reader.line_num))
            except RowError as exc:
                warnings.append(str(exc))
    return orders, ImportReport(source=path.name, accepted_rows=len(orders), warnings=warnings)
```

What it shows: explicit encoding, `pathlib`, a context-managed file, required-field
validation before domain logic, strings converted to `Decimal` early, an error that names
source and line, the cause chained with `from exc`, a frozen value type, and
`default_factory` for the mutable field. `slots=True` on a dataclass needs Python 3.10 or
later; drop it when the repository supports older versions.

### CLI entry point with exit codes

```python
import argparse
import sys
from collections.abc import Sequence
from pathlib import Path


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="import-orders")
    parser.add_argument("csv_path", type=Path)
    args = parser.parse_args(argv)
    try:
        _, report = load_orders(args.csv_path)
    except (OSError, UnicodeDecodeError) as exc:
        print(f"import-orders: cannot read {args.csv_path}: {exc}", file=sys.stderr)
        return 2
    for warning in report.warnings:
        print(warning, file=sys.stderr)
    print(f"accepted {report.accepted_rows} rows from {report.source}")
    return 1 if report.warnings else 0


if __name__ == "__main__":
    raise SystemExit(main())
```

Effects live behind `main()`. Importing the module does nothing. `main` takes `argv` so a
test can call it without patching `sys.argv`.

### Protocol seam

```python
from datetime import datetime, timezone
from typing import Protocol


class Clock(Protocol):
    def now(self) -> datetime: ...


class SystemClock:
    def now(self) -> datetime:
        return datetime.now(timezone.utc)


def is_expired(deadline: datetime, clock: Clock) -> bool:
    return clock.now() >= deadline
```

A test passes a `FixedClock` with the same method. No inheritance and no monkeypatching.

### Resource lifecycle

```python
import tempfile
from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path


@contextmanager
def workspace(prefix: str = "job-") -> Iterator[Path]:
    """Temporary directory that is removed on success, error and cancellation."""
    with tempfile.TemporaryDirectory(prefix=prefix) as name:
        yield Path(name)


def write_text_atomic(path: Path, text: str) -> None:
    """Readers see the old file or the new file, never a partial one."""
    tmp = path.with_name(path.name + ".tmp")
    try:
        tmp.write_text(text, encoding="utf-8")
        tmp.replace(path)
    finally:
        tmp.unlink(missing_ok=True)
```

Both run their cleanup on every exit path. The temporary name is in the same directory
as the target so the replace stays on one filesystem.

### Subprocess with a bound and a typed error

```python
import subprocess
from collections.abc import Sequence
from pathlib import Path


class ToolError(RuntimeError):
    """An external command failed or timed out."""


def run_tool(args: Sequence[str], *, cwd: Path, timeout: float) -> str:
    try:
        completed = subprocess.run(
            list(args),
            cwd=cwd,
            capture_output=True,
            text=True,
            encoding="utf-8",
            timeout=timeout,
            check=True,
        )
    except subprocess.CalledProcessError as exc:
        detail = (exc.stderr or "").strip()[:500]
        raise ToolError(f"{args[0]} exited with {exc.returncode}: {detail}") from exc
    except subprocess.TimeoutExpired as exc:
        raise ToolError(f"{args[0]} timed out after {timeout} s") from exc
    return completed.stdout
```

Subprocess output is runtime data. Parse `completed.stdout` before it reaches domain
logic.

### Async: cancellation, ownership, timeout, blocking work

```python
import asyncio
import logging

logger = logging.getLogger(__name__)


async def run_job() -> None:
    try:
        await do_work()
    except asyncio.CancelledError:
        await cleanup()
        raise


async def guarded_step() -> None:
    try:
        await step()
    except asyncio.CancelledError:
        raise                      # never fold cancellation into the generic handler
    except Exception:
        logger.exception("step failed")
        raise


async def fetch_all(urls, fetch) -> list[bytes]:
    async with asyncio.TaskGroup() as group:        # Python 3.11+: the group owns the tasks
        tasks = [group.create_task(fetch(url)) for url in urls]
    return [task.result() for task in tasks]


async def fetch_all_within(urls, fetch, seconds: float) -> list[bytes]:
    async with asyncio.timeout(seconds):            # Python 3.11+: the caller sets the bound
        return await fetch_all(urls, fetch)


async def read_config(path) -> str:
    return await asyncio.to_thread(path.read_text, encoding="utf-8")   # Python 3.9+
```

`do_work`, `cleanup` and `step` stand for the project's own coroutines.

Version notes to confirm against the repository's `requires-python`: `TaskGroup` and
`asyncio.timeout()` arrived in Python 3.11; use `asyncio.wait_for` and explicit task
bookkeeping on older targets. `asyncio.to_thread` arrived in 3.9; use
`loop.run_in_executor` before that, or whatever executor pattern the repository already
uses. Since Python 3.8 `asyncio.CancelledError` derives from `BaseException`, so
`except Exception` no longer catches it there, but a bare `except:` and
`except BaseException` still do.

### Tests for failure behaviour

pytest, when the repository uses pytest:

```python
import subprocess
import sys
from decimal import Decimal
from pathlib import Path

import pytest

from importer.orders import Order, RowError, load_orders, main, parse_order


def test_missing_id_is_rejected_with_location() -> None:
    with pytest.raises(RowError, match=r"orders\.csv:7: missing required field 'id'"):
        parse_order({"id": " ", "amount": "5"}, source="orders.csv", line=7)


def test_bad_amount_keeps_the_cause() -> None:
    with pytest.raises(RowError) as excinfo:
        parse_order({"id": "A1", "amount": "five"}, source="orders.csv", line=2)
    assert excinfo.value.__cause__ is not None


def test_bad_rows_are_reported_not_dropped(tmp_path: Path) -> None:
    csv_path = tmp_path / "orders.csv"
    csv_path.write_text("id,amount\nA1,5.00\n,3.00\n", encoding="utf-8")
    orders, report = load_orders(csv_path)
    assert orders == [Order("A1", Decimal("5.00"))]
    assert report.accepted_rows == 1
    assert report.warnings == ["orders.csv:3: missing required field 'id'"]


def test_cli_exit_code_for_unreadable_file(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    assert main([str(tmp_path / "absent.csv")]) == 2
    assert "cannot read" in capsys.readouterr().err


def test_import_has_no_side_effects(tmp_path: Path) -> None:
    # Requires the package to be installed in the test environment.
    result = subprocess.run(
        [sys.executable, "-c", "import importer.orders"],
        cwd=tmp_path,
        capture_output=True,
        text=True,
        timeout=30,
        check=False,
    )
    assert result.returncode == 0, result.stderr
    assert result.stdout == "" and result.stderr == ""
    assert list(tmp_path.iterdir()) == []
```

unittest, when that is the established stack (this form also needs no async plugin):

```python
import asyncio
import unittest


class CancellationTest(unittest.IsolatedAsyncioTestCase):
    async def test_cancel_runs_cleanup_and_propagates(self) -> None:
        started = asyncio.Event()
        cleaned = asyncio.Event()

        async def do_work() -> None:
            started.set()
            await asyncio.sleep(3600)

        async def cleanup() -> None:
            cleaned.set()

        task = asyncio.create_task(run_job(do_work, cleanup))
        await started.wait()          # cancel only after the task reached an await
        task.cancel()
        with self.assertRaises(asyncio.CancelledError):
            await task
        self.assertTrue(cleaned.is_set())


class WorkspaceTest(unittest.TestCase):
    def test_workspace_is_removed_when_the_body_raises(self) -> None:
        seen = []
        with self.assertRaises(RuntimeError):
            with workspace() as root:
                seen.append(root)
                raise RuntimeError("boom")
        self.assertFalse(seen[0].exists())
```

(The cancellation test uses a `run_job` that takes `do_work` and `cleanup` as parameters,
which is the injectable form of the example above.)

## Commands

### Discover what the repository uses

Run these before choosing any gate:

```bash
rg --files -g 'pyproject.toml' -g 'setup.cfg' -g 'setup.py' -g 'tox.ini' -g 'noxfile.py' -g 'requirements*.txt'
rg 'pytest|unittest|ruff|black|mypy|pyright|coverage|tox|nox' .
```

Then read the CI workflow and any `Makefile`, `tox.ini` or `noxfile.py` targets, and note:

```bash
rg -n 'requires-python|python_requires|target-version|python_version' pyproject.toml setup.cfg setup.py 2>/dev/null
python --version
python -m pip --version
```

Lock files count as configuration too. Check them before changing a dependency.

### Gate command menu

Use the commands the repository already uses. Prefer `python -m ...` forms when they
avoid path ambiguity; they bind the tool to the active interpreter.

```bash
python -m pytest
python -m unittest
ruff check .
ruff format --check .
black --check .
mypy .
pyright
python -m build
```

This is a menu, not a checklist:

- One test runner, one formatter and one type checker per repository. Do not run both
  `ruff format` and `black` unless the configuration requires both. During a migration
  the two can overlap; that does not make either the preferred runner.
- If `pyproject.toml` configures Ruff and mypy, the gate is `ruff check`,
  `ruff format --check`, `mypy` and `pytest`. Do not add pyright "for extra safety".
- A command with no configuration behind it (for example `black --check` in a repository
  that never configured Black) is a proposal, not a gate.
- `tox` or `nox` sessions can stand in for the individual commands when the repository
  defines them.
- `python -m build` is useful when packaging changed and noise for a pure logic change. A
  narrow script may skip the package build with the scope stated and the other gates run.
- For boundary changes, the minimum is the tests plus the configured type checker.
- `mypy .` on its own is not a sufficient gate. Pair every static check with the runtime
  tests for the affected boundary.
- `--help` in the target environment is stronger evidence for a flag than a remembered
  documentation page. Repositories should pin tool versions.

Extra checks, when the mode calls for them:

```bash
python -c "import your_package"                     # import isolation, from a clean directory
python -X importtime -c "import your_package"       # slow or surprising imports
python -m pip install . && your-console-script --help   # entry point, in a fresh virtual environment
python -W error -m pytest                           # surface warnings as failures, if the repo accepts that
```

Pitfalls when running gates: the wrong virtual environment, an editable install that
hides missing package data or metadata, plugin behaviour, cached diagnostics, two
formatters fighting, platform filesystem assumptions, and cancellation tests that never
reach an `await`.

Some claims have no command. No tool proves that code handles cancellation correctly
everywhere. Use the review prompts for those and say so in the record.

## Output contract

Return results in this order when planning or reviewing:

1. `Python Work Mode` - the surface, the main risk, the modes chosen.
2. `Executable Requirements` - `REQ-PY-<NNN>.<REV>` clauses, or a statement that the
   change is mechanical and needs none.
3. `Boundary And Type Design` - what is parsed where, the domain types, the seams, where
   `Any` enters and where it stops.
4. `Async/Resource Constraints` - owners, cleanup routes, cancellation and timeout
   behaviour, blocking-call isolation; or "none".
5. `Verification Matrix` - the traceability table (`req_id | test_id | test_type |
   assertion | target`).
6. `Implementation Plan` - ordered, one reviewable boundary at a time.
7. `Quality Gates` - the exact commands, their exit codes, and any gate skipped with its
   reason.
8. `Open Questions` - what is still unknown and who can answer it.

For review-only work hand back the gate record instead (template below). For a trivial
mechanical fix hand back the mode, the change and the gate result.

Every recommendation you make carries four things: the mode, the `PY1` identifier or
guardrail it comes from, when it applies, and a gate that can be run or a question a
reviewer can answer. A recommendation missing any of the four is not finished.

## Quality gates

The handoff gate is a stop sequence in four parts. It establishes that known hazards are
absent and known-good properties are present. It does not prove correctness, and the
lists are not exhaustive.

### 1. Anti-pattern sweep

Match the diff against all eleven rows of the table in
[Anti-patterns](#anti-patterns). For each hit give the mechanism (why it fails) and the
replacement (what to prefer), with file and line. Record no-hits as well: a log with only
hits cannot tell clean from unswept.

### 2. Default Reliability Stack

Before finishing Python work, verify:

1. Untrusted data is parsed or validated at the boundary.
2. Public functions and important internal seams have useful type hints.
3. `Any` is contained, justified, and narrowed quickly.
4. Mutable defaults are absent.
5. Resources are managed with context managers or explicit cleanup.
6. Async cancellation is preserved.
7. Import-time side effects are not added to reusable modules.
8. Tests cover errors, cleanup, and boundary behaviour.
9. Formatter, linter, type checker, and test gates were run or skipped with an explicit
   reason.

Each item needs a location: code, config, test, command output, or an explicit
"not applicable" with the reason. A tick without a location is a failure.

### 3. Command battery

Run the commands selected in [Commands](#commands) as one gate. Record the exact
commands, the Python and tool versions, and the exit codes.

### 4. Review pass

Answer all eight, in this order. Each answer is `yes`, `no` or `not-applicable`, plus one
line of evidence.

- `Input`: Are external values parsed before domain logic?
- `Types`: Are annotations precise enough to catch misuse?
- `Errors`: Are expected failures visible and actionable?
- `Resources`: Are acquired resources closed on every path?
- `Async`: Does cancellation propagate?
- `Imports`: Can importing the module run safely and quickly?
- `Tests`: Do tests prove malformed input, cleanup, and edge behaviour?
- `Gates`: Are repo-native tests and checks run?

`Gates = yes` requires that the commands were actually run, not inferred from reading the
code. A synchronous change may mark `Async` not-applicable, with the reason. A record
with a missing label or a missing evidence line is rejected. Split a huge diff before
gating it; one reviewable diff per cycle.

### Gate record template

```text
Gate record: <repository> / <change identifier> / <date>
Python: <version>   Tools: <name version, ...>

Sweep (hit: file:line, mechanism, replacement | no-hit)
  mutable default arguments ............
  bare except ..........................
  swallowed CancelledError .............
  uncontained Any ......................
  assert for external validation .......
  import-time network or fs mutation ...
  print in library behaviour ...........
  manual open/close ....................
  stringly path handling ...............
  blocking calls in async functions ....
  broad exception-to-None ..............

Stack (pass | fail | n-a, with location)
  1 boundary parsed .....  2 seams typed ......  3 Any contained ....
  4 no mutable defaults .  5 resources managed .  6 cancellation kept .
  7 imports clean .......  8 failure tests .....  9 gates run/skipped .

Battery (command -> exit code)
  <command> -> <code>

Review pass (yes | no | not-applicable + evidence)
  Input: ...   Types: ...   Errors: ...   Resources: ...
  Async: ...   Imports: ...  Tests: ...   Gates: ...

Decision: ship | bounce (cite row or item) | escalate
Unresolved risk: ...
```

Identify changes by identifier and line range. Never paste diff payloads or secrets into
the record.

### After a bounce

Verify each bounced item explicitly, then run one fresh full sweep. Mechanical hits
should converge in one cycle. Three cycles without convergence means the problem is the
design: escalate to a design review instead of a fourth patch.

When one place has several hits, fix in this order: resource handling and blocking calls
first, then narrow the exception handling. Fixing the resource path first avoids masking
cleanup while you work.

## Anti-patterns

| Anti-pattern | Why it fails | Prefer |
| --- | --- | --- |
| Mutable default arguments (`def f(items=[])`) | State leaks across calls | `None` sentinel or `default_factory` |
| Bare `except:` | Catches cancellation, interrupts, and hides root cause | Catch specific exceptions |
| Swallowing `asyncio.CancelledError` | Breaks cooperative cancellation; shutdown becomes a hang | Cleanup, then re-raise |
| Uncontained `Any` | Disables useful type checking downstream | Narrow at boundary |
| `assert` for external validation | Can be optimized away (`-O`) and gives poor diagnostics | Explicit validation and typed errors |
| Import-time network or filesystem mutation | Imports become slow, flaky, and unsafe | Move side effects behind functions or CLI entry points |
| `print` in library behaviour | Hard to route, test, and filter | `logging` or returned diagnostics |
| Manual open/close | Leaks resources on exceptions | `with` or `async with` |
| Stringly path handling | OS and relative-path bugs hide | `pathlib.Path` |
| Blocking calls in async functions | Event loop stalls under load | Synchronous API or executor isolation |
| Broad exception-to-`None` conversion | Callers lose cause and remediation | Typed result or contextual exception |

Legitimate boundaries, so the sweep does not over-report: `print` is fine for CLI user
output; `assert` is fine in tests and for internal invariants; entry points are the
proper home for side effects; a cheap pure module constant is usually fine.

Guardrails in one place:

- Do not introduce bare `except`, mutable default arguments, broad `Any`, import-time
  network calls, or resource acquisition without cleanup.
- Do not swallow `asyncio.CancelledError` in generic exception handling.
- Do not rely on `assert` for runtime validation of external input.
- Do not add a new formatter, linter, package manager, or type checker when the
  repository already has one unless migration is requested.
- Do not treat type hints as proof that runtime data is valid; parse and validate at
  trust boundaries.

More shapes to reject, beyond the eleven: validation scattered across layers; cleanup left
to garbage collection; clients created at import time; secrets in printed or logged
output; fixtures that leak global state; monkeypatches that are never restored; tests
that touch the real home directory.

Process anti-patterns: requirements written after the code; a new tool configuration
slipped into a bug fix; vague requirement words left in place; every listed tool added
"to be safe"; strictness exclusions that never expire; retrying a failing package test
until it turns green.

## Using reference.md

`reference.md` in this directory adds depth. The rules above are complete without it.
Open only what matches the boundary you are touching:

| You need | Open in reference.md |
| --- | --- |
| Why the patterns are ordered as they are; risk-based reordering | Pattern Scoreboard Ranking Table |
| API, typing and data design in depth (`PY1-02`, `PY1-03`, `PY1-04`, `PY1-08`) | Theme Specific Artifact, section 1 |
| Boundary parsing, exceptions, logging (`PY1-01`, `PY1-05`, `PY1-09`, `PY1-10`) | Theme Specific Artifact, section 2 |
| Async and resource reliability (`PY1-06`, `PY1-07`, blocking work) | Theme Specific Artifact, section 3 |
| Testing and fixtures (`PY1-11`, `PY1-13`, `PY1-14`) | Theme Specific Artifact, section 4 |
| Packaging and tooling (`PY1-12`, `PY1-15`) | Theme Specific Artifact, section 5 |
| Every anti-pattern with detection method and gotchas | Anti Pattern Registry Table |
| The nine-item final checklist as a reusable card | Theme Specific Artifact, section 6 (Default Reliability Stack) |

Those are the eight jump points for a coding task. The remaining sections are for
operating, auditing or refreshing the skill. They are listed so that every section of
`reference.md` is one step from here:

| You need | Open in reference.md |
| --- | --- |
| Activation limits, mode selection as risk selection, the handoff gate, the reading route | Agent Usage Decision Guide |
| Adopt, adapt or avoid; what each control costs; gate tiers; routing versus direct access | Decision Tradeoff Guide |
| Complete good, bad and borderline examples; step-by-step journeys | Worked Example Set; User Journey Scenario |
| Gate order, lint rule candidates, evidence to capture, heading checks | Verification Gate Command Set |
| What goes wrong and how to recover; retries and re-gating | Failure Mode Table; Retry Backpressure Guidance |
| How much one task may hold; proposed targets; where the skill stops scaling | Workload Model; Reliability Target; Scale Boundary Statement |
| What to record and measure in code, gates and routes | Observability Checklist; Performance Verification Method; Outcome Metrics and Feedback Loops |
| Audit lists for a change, a recommendation and this skill's own content | Completeness Checklist |
| Why a rule exists, which source backs it, how far to trust it | Idiomatic Thesis Synthesis Statement; Source Evidence Mapping Table; Evidence Boundary Notes |
| Work this skill does not own; what to search when a rule may be stale | Adjacent Reference Routing; Future Refresh Search Queries |

Use order: the PY1 table first; then only the matching sections; finish with the
anti-pattern table and the Default Reliability Stack. Record which match justified each
section you opened. An opened section with no recorded match is a routing failure, not
thoroughness.

An agent may start from the heading search instead of the numbered order. It searches
cheaply and follows prose order less reliably. The closing step stays mandatory either
way: end at the anti-pattern table and the Default Reliability Stack.

```bash
rg '^##|^###' reference.md
rg 'Pattern Scoreboard|Anti Pattern Registry|Default Reliability Stack' SKILL.md reference.md
```

If a section does not answer the question, search once, then re-diagnose which boundary
the task is really about before opening more. Opening everything for a one-line fixture
question is the failure this routing exists to prevent.

Keeping the two tables current:

- When a section is added to `reference.md`, add it to one of the tables above the same
  day. A routed reader does not find a section that is not listed here.
- Every new rule must be reachable from these tables in one step, and its basis must be
  findable in the Source Evidence Mapping Table in one lookup.
- Copying routed sections into a standing prompt for a recurring task shape skips the
  lookup and freezes the content. Date the copy and re-check it when either file
  changes.
- Check both directions at every refresh. For pointers, compare each name in the tables
  with the heading list from the first `rg` command above; a name with no heading is a
  defect in the pointer. For registration, run the loop below from this directory. It
  lists top-level sections of `reference.md` that are not named in this file and prints
  nothing when all are registered.

```bash
grep -E '^## ' reference.md | sed 's/^## //' | while IFS= read -r h; do
  grep -q -F "$h" SKILL.md || echo "not registered in SKILL.md: $h"
done
```

## Adjacent routing

Check first whether mode selection already answers the question. Route away only for the
part this skill does not own, and keep the general contracts (parsing, cleanup,
cancellation) when you do.

- Framework request lifecycles, web architecture, persistence and transactions, security
  threat models, distributed delivery, deployment, numerical correctness, performance
  engineering: the framework's or domain's primary reference. Example: route a FastAPI
  lifecycle question to FastAPI guidance and still keep parsed domain values and
  cancellation tests.
- Rust or TypeScript code: the sibling language skills.
- Writing and sizing requirements in general:
  [A03 Executable Specs](../../A03-Executable-Specs01.md).
- Matching the amount of process to the size of the work:
  [A01 LLM Workflow](../../A01-LLM-Workflow01.md).

Scope limit: this skill covers single-process Python reliability inside one repository's
toolchain. Subprocess lifecycle and cleanup are in scope. Multiprocessing design,
service topology, distributed queues and locks, fleet coordination and distributed
cancellation are not.

## Self-check before handing back

- [ ] The surface, the main risk and the modes are named, and were named before coding.
- [ ] The repository's Python versions and tools were discovered and left unchanged, or
      the request explicitly asked for a migration.
- [ ] Behaviour changes have `REQ-PY` requirements with no vague words, each mapped to a
      runnable test in the traceability table.
- [ ] Every external input is parsed at the boundary; no `Any` escapes into the core.
- [ ] No mutable defaults, bare `except`, exception-to-`None`, or `assert` on external
      input was added.
- [ ] Every acquired resource is released on success, error and cancellation.
- [ ] `CancelledError` propagates; timeouts are bounded; nothing blocks the event loop.
- [ ] Importing the changed modules has no side effects.
- [ ] Tests cover malformed input, cleanup and the expected failures, not just the happy
      path.
- [ ] The eleven-row sweep, nine-item stack, command battery and eight-prompt review pass
      are recorded, with exact commands and exit codes, and skipped gates carry a reason.
- [ ] Every recommendation names its mode, its `PY1` or guardrail source, when it
      applies, and its gate.
- [ ] Open questions are listed.
