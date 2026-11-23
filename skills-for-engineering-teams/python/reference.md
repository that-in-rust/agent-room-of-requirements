# Python Reliability Reference

Depth for the `python` skill. `SKILL.md` holds the rules, templates and gates and is
complete without this file. This file holds the full pattern catalogue, the registries,
worked examples, failure modes and the limits of the evidence.

It is a reliability checklist for Python written or reviewed by an agent. It is not a
tutorial.

## Idiomatic Thesis Synthesis Statement

Reliable Python comes from making dynamic behaviour explicit where it matters: typed
public contracts, parsed boundaries, deterministic cleanup, import-safe modules, and
tests that exercise failure behaviour. Type hints are useful guardrails, but runtime
inputs still need validation.

In working form:

- Convert dynamic uncertainty at system boundaries into validated domain values.
- Keep typed contracts in the core and contain `Any`.
- Model stable values explicitly.
- Depend on protocols where substitution or testing warrants them.
- Distinguish expected outcomes from exceptional failures.
- Own every resource and task lifecycle, and preserve cancellation.
- Avoid import effects.
- Verify adverse behaviour through the repository's supported gates.

Reliability here is information preservation. Parsed values, typed errors, exception
context, cancellation, logs and tests each carry the meaning of a failure across a layer.
The four collapses to refuse are: unknown into `Any`, failure into `None`, cancellation
into success, shared state into hidden coupling.

Consequences of the thesis:

- Every recommendation states which implicit behaviour becomes explicit and which gate
  proves it. Quality is expressed either as a named bad shape with a replacement or as a
  numbered property that can be verified. Virtue words that cannot be measured are not
  used.
- "Releasable" means known-bad shapes are absent and known-good properties are present.
  The enumeration is not exhaustive and never proves correctness. Shape checks can pass
  while behaviour is wrong, so tests stay necessary.
- Type hints do not inspect runtime data. Happy-path tests do not prove cleanup,
  cancellation, import safety or package compatibility.
- The thesis does not justify ceremony for quick automation, and it says nothing about
  exploratory notebooks.
- Tools are subordinate to repository preservation. Keep a synchronous design when
  concurrency adds no value. Wrap legacy dynamic code with typed adapters. Stage
  strictness module by module. Preserve an established `unittest` or checker workflow.
- The guardrails state the thesis in the negative: no bare `except`, no mutable defaults,
  no broad or uncontained `Any`, no import-time IO, no swallowed cancellation.

Good: a CLI parses strings into domain values, uses a protocol-backed service, and tests
invalid input plus file cleanup. Bad: annotated dictionaries and broad `except` blocks.
Borderline: a small script stays less formal only while its effects and failures are
explicit.

## Pattern Scoreboard Ranking Table

### Code patterns

| ID | Score | Pattern | Mode | Section below |
| --- | ---: | --- | --- | --- |
| `PY1-01` | 97 | Parse untrusted data at the boundary | Boundary | 2 |
| `PY1-02` | 95 | Keep `Any` contained and justified | Typing | 1 |
| `PY1-03` | 94 | Use dataclasses for value data with explicit defaults | Typing | 1 |
| `PY1-04` | 93 | Prefer protocols for behaviour seams | Typing | 1 |
| `PY1-05` | 92 | Use exceptions for exceptional failures and typed returns for expected outcomes | Boundary, Core | 2 |
| `PY1-06` | 91 | Acquire resources with context managers | Resource | 3 |
| `PY1-07` | 94 | Preserve asyncio cancellation | Async | 3 |
| `PY1-08` | 90 | Avoid import-time side effects in reusable modules | Core, Packaging | 1 |
| `PY1-09` | 89 | Use pathlib and explicit encodings for filesystem work | Boundary, Resource | 2 |
| `PY1-10` | 88 | Keep logging structured enough for diagnosis | Core | 2 |
| `PY1-11` | 88 | Use pytest or unittest fixtures to isolate state | Testing | 4 |
| `PY1-12` | 87 | Preserve package metadata and supported Python versions | Packaging | 5 |
| `PY1-13` | 86 | Prefer dependency injection over monkeypatching production code | Testing | 4 |
| `PY1-14` | 85 | Test errors, cleanup, and boundary behaviour directly | Testing | 4 |
| `PY1-15` | 84 | Run formatter, linter, type checker, and tests as a single gate | Review | 5 |

The range is 84 to 97. The scores are authorial adoption priorities with no empirical
calibration. They are not probabilities, severities, defect-reduction figures, service
objectives or a comparison between tools. Do not turn 97 into a reliability percentage.

How to use the order:

- All applicable controls remain required. A pattern scored 84 that applies is not
  optional.
- Classify each pattern for the change as a hard prerequisite or as contextual. Boundary
  parsing and lifecycle safety are the usual hard prerequisites.
- Context dominates: cancellation in an async worker, import safety in a library,
  explicit encodings in file interchange.
- Do not optimise annotations while cleanup is missing.
- Under time pressure, take the doubly listed items first: boundary validation, mutable
  defaults, cancellation preservation, import-time side effects. Run the mechanical
  anti-pattern sweep before the stack, and the judgment-heavy review last.
- Priority is not severity. An explicit skip reason can still block a handoff.
- Local overrides are reasonable. Stringly paths may deserve first place in a repository
  that ships to Windows.
- Replace the order with the repository's own hit history, incident history or lint
  enforceability once enough exists. Until then do not reorder on instinct.
- Better instruments than the score: a small risk matrix, failure-cost ordering, and an
  omission review (which applicable pattern did the change not touch?).

### Working-method patterns

These three rank how to use the guidance, not how to write code. Do not mix them with the
code scoreboard. The numbers are emphasis, not measured efficiency.

| Score | Pattern | Prevents |
| ---: | --- | --- |
| 95 | Source map first: read the map, then the matching material, before synthesising | advice written without loading the relevant guidance |
| 91 | Evidence boundary split: keep repository facts, external facts and inference apart | mixed claims nobody can audit |
| 88 | Verification gate coupling: every recommendation carries a command, a checklist item or a reviewer question | recommendations that cannot be checked |

## Agent Usage Decision Guide

### Activation and modes

Order of work:

1. Declare the Python Work Mode or modes, the surface and the dominant risk.
2. When behaviour is unclear, write executable requirements in `WHEN ... THEN ... SHALL
   ...` form with identifiers such as `REQ-PY-001.1`. Never leave "pythonic", "safe",
   "clean" or "robust" in a requirement.
3. Load depth progressively.
4. Design boundaries and failure paths.
5. Implement.
6. Run the applicable gates.
7. Present a verification matrix with `test_id`, `test_type`, `assertion` and `target`.
8. End with open questions.

Before selecting controls, take the risk inventory: runtime inputs, public API, dynamic
types, mutable state, expected and exceptional failures, resources, concurrency, imports,
filesystem effects, package surface, supported versions. Select the smallest set of
controls that closes the actual risks. Strictness is asymmetric: spend it on untrusted
data, irreversible effects, concurrency and public contracts.

Do not:

- activate for every `.py` edit;
- impose service controls on disposable scripts;
- treat every function as public;
- add async without need;
- migrate tools before fixing behaviour.

A CSV importer may need parsing, typed values, explicit encoding, contextual errors, temp
fixtures and package gates. A typo does not need a toolchain replacement.

Record for each use: task type, risk inventory, selected pattern IDs, controls and
boundaries skipped, repository commands, Python versions, adverse tests, the adjacent
route if any, and the stop condition.

Trivial mechanical fixes may skip formal requirements only if the mode and the gate are
still named. Backfilling requirements after implementation is not a substitute.

### Handoff gate

For every reviewed change, emit eight labelled answers in order: `Input`, `Types`,
`Errors`, `Resources`, `Async`, `Imports`, `Tests`, `Gates`. Each is `yes`, `no` or
`not-applicable` plus one evidence line. `Gates = yes` requires running the commands. A
synchronous change may mark `Async` not-applicable only with a reason. Reject records
with a missing label or evidence line. Split huge diffs first.

Which part answers which question:

| Question | Part of the gate |
| --- | --- |
| What code shape is banned? | the anti-pattern table |
| What property must hold? | the Default Reliability Stack |
| What command should run? | the command menu and the discovery commands |
| What must the reviewer ask? | the eight-prompt review pass |

Do not drop the review pass because the sweep was clean. Its `Errors` and `Types` prompts
cover things the anti-pattern table does not. "Why prefer this pattern?" is a design
question and belongs in the pattern sections, not in the gate.

### Reading route

1. Read the scoreboard.
2. Match the task to a boundary and open only the matching section or sections. Note the
   match. If nothing matches, search headings once, then escalate instead of widening the
   read.
3. Close with the anti-pattern table and the Default Reliability Stack.
4. When someone challenges the grounds for a rule, go to the Source Evidence Mapping
   Table and the Evidence Boundary Notes.

The task must name or imply one of the five numbered areas. Opening every jump point
defeats the purpose. Skipping step 1 on repeated work is efficient when you can name the
destination before looking it up; note the skip. Good: open only the async section for a
cancellation bug. Bad: load the whole reference for a one-line fixture question.
Borderline: re-route for every subtask of one feature, which is correct but wasteful.

Reject a routing record that cannot show, for every section opened, the step 2 match
that justified it. An agent that opens every jump point has technically routed and has
reproduced the context dump the route exists to prevent. The word "only" in step 2
carries the value. Step 2 also fails open: a task that matches no jump point tempts the
reader to open everything, and the correct move is the single heading search and then
escalation. Good record: scoreboard read, section 3 opened for a cancellation task,
stack cited at close. Bad record: eight jump points opened for a docstring question.
Noting which step produced each loaded section costs nothing extra and leaves the trace
that the reading anti-patterns in Anti Pattern Registry Table are detected from.

Which aid leads depends on the reader. For a person the numbered order is the habit, the
jump points are its address book, and the heading search is the fallback for a heading
that is not listed. For an agent the priority inverts: it searches headings cheaply and
follows prose order unreliably, so it may lead with the heading search (commands under
Verification Gate Command Set, "Checking this skill's own headings") instead of the
numbered steps. Step 3 does not move. Whatever started the route, it closes at the
anti-pattern table and the Default Reliability Stack. Jumping straight to a memorised
section is the borderline case for both readers: efficient, and it silently skips the
closing step unless that step is done on purpose. Reorder the aids further only from
recorded misroutes, once enough routed uses have been logged to show where readers get
lost. How often a reader who skips the numbered order misroutes is not measured.

When a full read is right instead: activation decisions, audits, tasks that span several
boundaries, and questions you cannot classify. A full sequential read is slower and
avoids misrouting.

## Decision Tradeoff Guide

### Adopt, adapt, avoid

| Choice | When | Cost and check |
| --- | --- | --- |
| Adopt | The safety rule applies and local conventions do not conflict; local and external evidence agree | Fastest. May copy stale assumptions. Confirm the rule is in the canonical guidance and matches current evidence. |
| Adapt | The rule is sound but the repository's style, structure, packaging or tooling differs, or ecosystem guidance has changed | Preserves repository fit. Label repository fact, external fact and inference separately. |
| Avoid or route | Evidence is thin or conflicting, the task is out of scope, or the packaging system is unfamiliar | Add a confidence warning or name the next reference. May need deeper research. |
| Cost of a wrong choice | Wrong routing sends work to the wrong files, tests or abstraction | Wasted implementation loop and weaker verification. The reviewer must be told what to undo and what to inspect next. |

Applied to Python work:

- Adopt safety rules at once: fix mutable defaults, do not preserve a bare `except`.
- Adapt style, structure, packaging and tooling to the repository. Do not add pyright to
  a mypy repository as part of a bug fix.
- Defer broad migrations behind stable seams.
- Avoid complexity whose verification cost exceeds the bounded need.
- Decide per boundary and per change, not as repository-wide strictness.
- Sample three neighbouring files and record which branch you took and why.

Good: adopt parsing and cleanup now, adapt typing module by module, avoid async for
sequential work. Bad: add every listed tool. Borderline: a protocol only when several
implementations or testing justify it.

### What each control costs

| Control | Cost | Alternative when the cost is too high |
| --- | --- | --- |
| Boundary parsing | Scattered validation duplicates poorly | One parser per boundary; narrower runtime checks |
| Strict typing | Exposes existing debt | Runtime checks without a checker migration; typed adapters; one module per cycle; staged CI warnings |
| Protocols | Adds abstraction | Inject the concrete object first; add the protocol when a second implementation or test double appears |
| Dataclass or `TypedDict` | Choice depends on how stable the data is | Either one; neither replaces runtime validation |
| Async | Adds cancellation as a concern everywhere | Synchronous execution |
| Tool migration | Churn | Narrow fixtures and staged warnings inside the existing toolchain |

For each decision record: risk, pattern IDs, benefit, complexity and compatibility cost,
alternatives, controls skipped, consequence, tests, rollout, rollback, and the trigger to
revisit. Costs and benefits are not quantified by the available evidence.

### Gate tiers

The base rule is to verify the full stack before finishing Python work. A team that has
adopted tiering uses this instead:

| Tier | Changes | Gate |
| --- | --- | --- |
| Routine | small, familiar, no new boundary | sweep plus the compact eight-prompt pass |
| Full | releases, new modules, async boundaries, boundary-heavy code | full nine-item stack plus the command battery, plus the sweep and pass |

Rules for tiering:

- The sweep is always retained. Never skip safety-critical or doubly listed rows.
- Uniform maximal gating can push people to batch work into huge PRs that get a less
  thorough review. Automate the mechanical rows in CI where possible.
- Audit tier assignment quarterly. Risky paths tend to be quietly reclassified as
  routine.
- The throughput cost per item is not measured.

Tiering, the gate card, drills and escalation limits in this file are constructed
operating guidance. They are not requirements of the base skill.

### Routing versus direct access

Fully route the first contact with a boundary. Later direct access is allowed with a
noted skip. A change to the map resets everyone to full routing. Never skip the closing
gate anchors. Familiarity means you can name the destination before opening the map, not
that the material feels familiar. A newcomer does not inherit a veteran's skip, and a
long gap reduces familiarity. The threshold is judgment, not a measured value.

A third option exists for a task shape that recurs: copy the routed sections into the
standing prompt for that task.

| Option | Gain | Cost | Selects it |
| --- | --- | --- | --- |
| Live routing | content is always current | one lookup per task | first contact, changed files, any task that is not a known shape |
| Direct access with a noted skip | no lookup | depends on real familiarity | repeated work where the destination can be named in advance |
| Routed sections embedded in a standing prompt | no lookup and no familiarity needed | the copy is frozen and goes stale when `reference.md` changes | a recurring task shape, with someone who owns re-copying |

Treat an embedded copy like a routing card (Theme Specific Artifact, section 7): date
it, and re-copy when either skill file changes. An embedded copy does not remove the
closing step.

## Theme Specific Artifact

### 1. API, typing, and data design

#### `PY1-02` Keep `Any` contained and justified

Use `Any` only at edges where the shape is genuinely unknown. Narrow it immediately with
parsing, validation or explicit runtime checks.

Prefer:

- `object` when callers must prove the type before use.
- `Protocol` when behaviour matters more than concrete class.
- `TypedDict` or dataclasses when dictionary shapes are stable.
- Type aliases for repeated domain concepts.

Avoid spreading `Any` into the core. One uncontained `Any` can erase the value of a typed
module, because every value derived from it is unchecked too.

```python
import json
from dataclasses import dataclass


class SettingsError(ValueError):
    """Settings text that cannot become Settings."""


@dataclass(frozen=True, slots=True)
class Settings:
    host: str
    port: int


def parse_settings(raw: object) -> Settings:
    if not isinstance(raw, dict):
        raise SettingsError(f"settings must be a JSON object, got {type(raw).__name__}")
    host = raw.get("host", "127.0.0.1")
    if not isinstance(host, str) or not host:
        raise SettingsError("settings.host must be a non-empty string")
    port = raw.get("port")
    if isinstance(port, bool) or not isinstance(port, int) or not 0 < port < 65536:
        raise SettingsError(f"settings.port must be an integer in 1..65535, got {port!r}")
    return Settings(host=host, port=port)


def load_settings(text: str) -> Settings:
    try:
        raw: object = json.loads(text)      # unknown shape enters here ...
    except json.JSONDecodeError as exc:
        raise SettingsError(f"settings are not valid JSON: {exc}") from exc
    return parse_settings(raw)              # ... and stops here
```

Notes:

- `json.loads` returns `Any`. Assigning it to `object` forces every use to be proved.
- `bool` is a subclass of `int`. A port parser that forgets this accepts `true`.
- Where `Any` must stay (a third-party callback, a plugin payload), put the reason in a
  comment on the line and keep the function that holds it small.
- A cast is not narrowing. Do not lower `Any` counts with casts.
- Legacy dynamic code: wrap it in one adapter with explicit parsing, logging, tests and
  removal criteria. Unknown values may enter the adapter but may not leave it.
- A `TypedDict` is a static description. It performs no runtime validation.

Checker support, to confirm with the installed tool's `--help` and the repository
configuration: mypy has `--strict`, `--disallow-any-generics`, `--disallow-any-explicit`,
`--warn-return-any` and `--disallow-untyped-defs`; pyright has a strict type-checking
mode that reports unknown types. Use only what the repository already runs. Staging one
module at a time in mypy looks like this:

```toml
[[tool.mypy.overrides]]
module = ["importer.orders"]
disallow_untyped_defs = true
disallow_any_generics = true
warn_return_any = true
```

Permanent exclusions are debt. Give each exclusion an expiry condition.

#### `PY1-03` Use dataclasses for value data with explicit defaults

Use dataclasses for simple values and state snapshots. Prefer `frozen=True` when mutation
is not part of the model, `slots=True` when appropriate for memory and attribute
discipline, and `field(default_factory=...)` for mutable defaults.

```python
from dataclasses import dataclass, field


@dataclass(frozen=True, slots=True)
class ImportReport:
    source: str
    accepted_rows: int
    warnings: list[str] = field(default_factory=list)
```

Avoid mutable default arguments in functions and dataclasses. Use factories for lists,
dicts, sets and generated values.

```python
def add_tag(tag: str, tags: list[str] | None = None) -> list[str]:
    tags = [] if tags is None else tags
    tags.append(tag)
    return tags
```

Notes:

- A function default is evaluated once, when the function is defined. That applies to
  `[]` and `{}` and also to generated values such as a timestamp or an identifier.
- The `dataclass` decorator itself rejects a bare `list`, `dict` or `set` default with a
  `ValueError` that names `default_factory`. It does not catch other mutable objects.
- `frozen=True` stops attribute assignment. It does not freeze what the attributes point
  to: the `warnings` list above can still be appended to. Use a tuple when the contents
  must not change.
- `slots=True` needs Python 3.10 or later. It removes the instance `__dict__`, so it
  breaks code that sets undeclared attributes and serializers that read `__dict__`. Use
  it when appropriate, not by default.
- Do not use `frozen` or `slots` when the model legitimately mutates, needs dynamic
  attributes, or a serializer requires otherwise.
- A dataclass does not validate the values it is given. Parse first, construct second.
- Choose a dataclass for a domain value with invariants or behaviour, and a `TypedDict`
  for data that stays a dictionary. Neither replaces runtime validation.
- Keep secrets out of `repr`: `token: str = field(repr=False)`.

#### `PY1-04` Prefer protocols for behaviour seams

Use `Protocol` when the code needs a capability rather than a concrete class. This keeps
tests lightweight and reduces inheritance pressure.

Good seams:

- clock providers
- filesystem adapters
- HTTP clients
- repositories
- event publishers
- command runners

```python
from datetime import datetime, timedelta, timezone
from typing import Protocol


class Clock(Protocol):
    def now(self) -> datetime: ...


def is_expired(deadline: datetime, clock: Clock) -> bool:
    return clock.now() >= deadline


class FixedClock:
    def __init__(self, moment: datetime) -> None:
        self._moment = moment

    def now(self) -> datetime:
        return self._moment


def test_deadline_in_the_past_is_expired() -> None:
    noon = datetime(2026, 1, 1, 12, tzinfo=timezone.utc)
    assert is_expired(noon - timedelta(seconds=1), FixedClock(noon))
```

Notes:

- A protocol needs a justification: a second implementation, or a test that substitutes
  behaviour. Without one, inject the concrete object and add the protocol when the need
  appears. Introduce the protocol before the replacement implementation, not after.
- Keep protocols small: the methods the caller uses, nothing else.
- The protocol belongs with the code that consumes the capability.
- Environment and time are seams too. Pass `env: Mapping[str, str]` and a clock in from
  the entry point instead of reading `os.environ` and the system clock deep in the core.

#### `PY1-08` Avoid import-time side effects in reusable modules

Importing a reusable module should define names and nothing else. Network calls, file
writes, argument parsing, logging configuration, thread starts and client construction
at import time make imports slow, flaky and unsafe, and they run in every test, tool and
worker that touches the module.

```python
# Avoid: runs on import, in every process that imports the module.
SESSION = make_session(os.environ["API_URL"])

# Prefer: the entry point builds it and passes it in.
def build_session(api_url: str) -> Session:
    return make_session(api_url)
```

Rules:

- Effects live behind functions, factories or the CLI entry point
  (`if __name__ == "__main__": raise SystemExit(main())`).
- No module-level clients. A module-level cache is acceptable only if it is lazy,
  deterministic, resettable, thread-safe and tested. A cheap pure constant is usually
  fine.
- A library does not configure logging handlers. The application does.
- If imports depend on the environment, put the dependency behind an adapter.
- Import caches (`sys.modules`) can hide an import-time effect in a test run that
  imported the module earlier. Prove import safety in a fresh interpreter:

```bash
python -c "import your_package"
python -X importtime -c "import your_package" 2>&1 | sort -t'|' -k2 -n | tail -15
```

### 2. Boundary parsing and exceptions

#### `PY1-01` Parse untrusted data at the boundary

CLI args, env vars, JSON, HTTP payloads, CSV rows, subprocess output, and database rows
are runtime data. Type hints alone do not validate them.

Boundary rules:

- Decode with explicit encodings.
- Validate shape and required fields before domain logic.
- Convert primitive strings into domain values early.
- Return or raise errors with enough context to repair the input.

| Input | Parse into | Typical failure to test |
| --- | --- | --- |
| CLI arguments | typed options and `Path` values at the entry point | missing argument, wrong type, path that does not exist |
| Environment variables | typed settings object built once at start-up | unset versus empty, non-numeric number, unknown flag spelling |
| JSON | dataclass or validated `TypedDict` | wrong top-level type, missing key, `null`, number as string, boolean as integer |
| HTTP payload | request or response value type | truncated body, wrong content type, unexpected status |
| CSV row | row value type | missing column, blank required field, bad number, wrong encoding |
| Subprocess output | parsed result plus exit status | non-zero exit, empty output, undecodable bytes, timeout |
| Database row | domain value | `NULL` in a required column, unexpected type, missing row |

```python
from collections.abc import Mapping


class ConfigError(ValueError):
    """An environment value that cannot be used."""


def read_port(env: Mapping[str, str]) -> int:
    text = env.get("APP_PORT")
    if text is None:
        raise ConfigError("APP_PORT is not set")
    try:
        port = int(text)
    except ValueError as exc:
        raise ConfigError(f"APP_PORT={text!r} is not an integer") from exc
    if not 0 < port < 65536:
        raise ConfigError(f"APP_PORT={port} is outside 1..65535")
    return port
```

The entry point calls `read_port(os.environ)`. A test calls `read_port({"APP_PORT":
"8080"})` and needs no monkeypatching.

Notes:

- Parse once, at the edge. After that point the core accepts domain types only.
- Validation scattered through the layers duplicates poorly and drifts apart.
- An error message names the source, the position, the field and what was expected. Do
  not echo secrets or whole payloads into it.
- If the repository already uses a validation library, use it at the boundary. Do not
  add one as part of unrelated work.
- The full CSV example is in `SKILL.md` under Templates.

#### `PY1-09` Use pathlib and explicit encodings for filesystem work

- Use `pathlib.Path` for paths. String concatenation and manual separators hide OS and
  relative-path bugs.
- Pass `encoding=` on every text open, read and write. Without it the encoding depends on
  the platform and locale on the Python versions most repositories support.
- For the `csv` module, open the file with `newline=""`.
- Resolve relative paths against an explicit base (a project root or a config
  directory), not the current working directory, unless the CLI contract says cwd.
- Tests use temp paths and never the real home directory.
- Write through a temporary name in the same directory and replace, so a failure cannot
  leave a partial file (see `write_text_atomic` in `SKILL.md`).
- Platform assumptions to watch: case sensitivity, path separators, reserved names, file
  locking behaviour, and whether a replace over an open file succeeds.

Python 3.10 and later can warn about a missing encoding:

```bash
python -X warn_default_encoding -m pytest
```

#### `PY1-05` Use exceptions and typed returns deliberately

Use exceptions for unexpected or exceptional failures. Use typed return values for
expected business outcomes that callers must handle.

Avoid:

- bare `except:`
- catching `Exception` and returning `None`
- hiding file, network, or parse errors behind vague messages
- using `assert` for runtime validation of external input

An expected outcome as a typed return:

```python
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Accepted:
    order_id: str


@dataclass(frozen=True, slots=True)
class Rejected:
    line: int
    reason: str


Outcome = Accepted | Rejected      # Python 3.10+ at runtime


def describe(outcome: Outcome) -> str:
    if isinstance(outcome, Accepted):
        return f"accepted {outcome.order_id}"
    return f"line {outcome.line}: {outcome.reason}"
```

Notes:

- The caller of a typed outcome cannot forget the failure branch without the type checker
  noticing. The caller of a `None`-on-failure function can.
- Chain when translating: `raise ConfigError(...) from exc`. The cause (`__cause__`) is
  what a later reader needs.
- Catch the narrowest exception that the code can act on, at the layer that can act.
- A broad handler is legitimate at an orchestration boundary (a worker loop, a CLI
  `main`) when it logs with the traceback and either re-raises or converts to a defined
  exit status. It is not legitimate as a way to return `None`.
- `assert` is removed under `python -O` and gives poor diagnostics. It is right for tests
  and for internal invariants that indicate a programmer error.
- Bare `except:` and `except BaseException` also catch `KeyboardInterrupt`, `SystemExit`
  and cancellation.
- Do not retry programmer errors. A `TypeError` from a wrong call will fail the same way
  the second time.

#### `PY1-10` Keep logging diagnosable

Library code should not rely on `print` for operational behaviour. Use logging at
adapters and orchestration boundaries. Keep messages actionable and avoid logging
secrets.

```python
import logging

logger = logging.getLogger(__name__)

logger.info("imported %d rows from %s in %.2f s", report.accepted_rows, report.source, elapsed)
```

Notes:

- CLI user output may `print`. That is the program's interface, not its diagnostics.
- A pure domain layer may return diagnostics (as `ImportReport.warnings` does) instead of
  logging.
- Messages carry identifiers, counts and durations. They do not carry secrets, tokens,
  environment dumps or raw payloads.
- Do not log whole dataclasses or request objects. Their `repr` may hold secrets. Mark
  secret fields `repr=False` and log named fields.
- Keep the exception chain: `logger.exception(...)` inside the handler, or
  `exc_info=True`.
- Do not report cancellation as an error. It is control flow.
- Name tasks (`asyncio.create_task(coro, name="worker-3")`) so a log line can say which
  one.
- The library obtains a logger and leaves handlers to the caller. Configuring handlers at
  import produces duplicate handlers and duplicate lines.
- Logging inside a tight loop can change timing. Keep it out of the hot path when a
  latency budget exists.
- Checks: search for `print(` outside CLI modules; capture logs in a test and assert a
  secret value is absent.

### 3. Async and resource reliability

#### `PY1-06` Acquire resources with context managers

Use `with` or `async with` for files, locks, temporary directories, network clients,
database sessions, and custom resource lifecycles.

If a resource requires setup and teardown, consider `contextlib.contextmanager` or
`contextlib.asynccontextmanager` to make the lifecycle explicit.

```python
from collections.abc import AsyncIterator, Awaitable, Callable
from contextlib import asynccontextmanager
from typing import Protocol


class Session(Protocol):
    async def close(self) -> None: ...


@asynccontextmanager
async def open_session(connect: Callable[[], Awaitable[Session]]) -> AsyncIterator[Session]:
    session = await connect()
    try:
        yield session
    finally:
        await session.close()
```

A child process is a resource too:

```python
import subprocess
from collections.abc import Iterator, Sequence
from contextlib import contextmanager


@contextmanager
def running(args: Sequence[str], *, grace: float = 5.0) -> Iterator[subprocess.Popen[bytes]]:
    """Child process that is stopped on every exit path."""
    process = subprocess.Popen(list(args))
    try:
        yield process
    finally:
        if process.poll() is None:
            process.terminate()
            try:
                process.wait(timeout=grace)
            except subprocess.TimeoutExpired:
                process.kill()
                process.wait()
```

Idempotent teardown:

```python
class Closer:
    def __init__(self) -> None:
        self._closed = False

    def close(self) -> None:
        if self._closed:
            return
        self._closed = True
        ...  # release the underlying resource exactly once
```

Notes:

- The three exit paths are success, error and cancellation. A resource that closes on
  two of them leaks on the third.
- Garbage collection is not a cleanup strategy. When and whether a finalizer runs is not
  part of the contract.
- Acquire as late as possible and release in reverse order. Nested `with` statements or
  `contextlib.ExitStack` do the ordering for you.
- Cleanup code can raise. An exception from `close()` in a `finally` block replaces the
  original error. Keep cleanup small, and log and continue where losing the original
  error would be worse.
- Partial state: a failure between two state changes leaves the first one applied. Order
  the steps so the visible change is last, or make the sequence replaceable as a unit
  (temporary file then replace; transaction then commit).
- Every subprocess call carries a timeout.
- In tests, count acquisitions and releases, or assert the path, process or connection is
  gone after the block exits with an error.

#### `PY1-07` Preserve asyncio cancellation

Cancellation is part of asyncio control flow. Do not swallow `asyncio.CancelledError` in
broad handlers. If cleanup is needed, perform cleanup and re-raise cancellation.

```python
import asyncio


async def run_job() -> None:
    try:
        await do_work()
    except asyncio.CancelledError:
        await cleanup()
        raise
```

Use `asyncio.TaskGroup` when the project target supports it and sibling task ownership
should be explicit. Preserve older supported Python targets when the repository requires
them.

A worker pool with explicit ownership and shutdown:

```python
import asyncio
import logging
from collections.abc import Awaitable, Callable
from dataclasses import dataclass

logger = logging.getLogger(__name__)


@dataclass(frozen=True, slots=True)
class Job:
    job_id: str


async def worker(queue: asyncio.Queue[Job], handle: Callable[[Job], Awaitable[None]]) -> None:
    while True:
        job = await queue.get()
        try:
            await handle(job)
        except asyncio.CancelledError:
            raise
        except Exception:
            logger.exception("job %s failed", job.job_id)
        finally:
            queue.task_done()


async def run_workers(
    queue: asyncio.Queue[Job],
    handle: Callable[[Job], Awaitable[None]],
    *,
    count: int,
    shutdown: asyncio.Event,
) -> None:
    async with asyncio.TaskGroup() as group:        # Python 3.11+
        workers = [
            group.create_task(worker(queue, handle), name=f"worker-{number}")
            for number in range(count)
        ]
        await shutdown.wait()
        for task in workers:
            task.cancel()
```

Notes:

- Never drop the re-raise. A swallowed cancellation turns cooperative shutdown into a
  hang, and timeouts built on cancellation stop working.
- The cleanup call in `run_job` can itself raise and mask the cancellation. Production
  code may need to bound the cleanup with a timeout, scope it, or shield the one step
  that must complete. Shielding can be right during shutdown. As a habit it defeats
  cancellation.
- `try ... finally` is the simpler form when the same cleanup must run on every path.
- Specify four things together: what cancels the task, what cleanup runs, that
  cancellation is re-raised, and the timeout bound.
- Class hierarchy depends on the version. Since Python 3.8 `asyncio.CancelledError`
  derives from `BaseException`. Since 3.11 `asyncio.TimeoutError` is the built-in
  `TimeoutError`. Code that supports older targets must not rely on either. Check
  `requires-python` first.
- `TaskGroup` and `asyncio.timeout()` need Python 3.11. On older targets use
  `asyncio.wait_for`, keep references to tasks you create, and cancel and await them in a
  `finally` block.
- Keep a reference to every task you create. A task with no owner can fail silently or
  disappear.
- Cancellation can arrive at any `await`, including one between two state changes. Treat
  each `await` inside a multi-step update as a possible exit.
- A cancellation test must let the task reach an `await` before cancelling it. A task
  cancelled before it starts never runs the code under test.

#### Blocking work in async code

Do not run blocking file, CPU, subprocess, or network calls directly on the event loop.
Keep the function synchronous or isolate blocking work with the repository's accepted
executor or thread pattern.

| Blocking call | Options |
| --- | --- |
| `time.sleep` | `asyncio.sleep` |
| File reads and writes | keep the function synchronous; or `asyncio.to_thread` (3.9+) or the repository's executor |
| `subprocess.run` | `asyncio.create_subprocess_exec`; or run the synchronous call in a thread |
| Synchronous HTTP client | the async client the repository already uses; or a thread |
| CPU-bound work | a process pool through the repository's executor pattern; or keep it out of the async path |

Notes:

- One synchronous call on the loop delays every concurrent task, not only the caller.
- Cancelling the `await` on a thread does not stop the thread. The work continues in the
  background, so the function running there needs its own bound.
- A whole call chain that never awaits anything concurrent should stay synchronous.
- Check loop responsiveness with a heartbeat while the handler runs:

```python
import asyncio
import contextlib
from collections.abc import Awaitable


async def max_loop_lag(work: Awaitable[object], *, tick: float = 0.01) -> float:
    """Largest delay, in seconds, that a heartbeat task saw while `work` ran."""
    loop = asyncio.get_running_loop()
    worst = 0.0

    async def heartbeat() -> None:
        nonlocal worst
        while True:
            before = loop.time()
            await asyncio.sleep(tick)
            worst = max(worst, loop.time() - before - tick)

    beat = asyncio.create_task(heartbeat(), name="heartbeat")
    try:
        await work
    finally:
        beat.cancel()
        with contextlib.suppress(asyncio.CancelledError):
            await beat
    return worst
```

A test asserts `await max_loop_lag(handler(request))` stays under the budget the owner
set. The suppression here is deliberate and local: the helper is awaiting a task it has
just cancelled itself.

### 4. Testing and fixtures

Test the behaviour that can fail:

- malformed input and missing fields
- exception messages and typed error paths
- context manager cleanup
- cancellation and timeout behaviour
- import safety for reusable modules
- package entry points and CLI exit codes
- filesystem behaviour with temp paths

Prefer pytest fixtures when the repository uses pytest. Use `unittest` when it is the
established local stack. Keep monkeypatching narrow and restore state reliably.

#### `PY1-14` Test errors, cleanup, and boundary behaviour directly

The adverse-test catalogue:

| Risk | Test technique |
| --- | --- |
| Unparsed input reaching the core | malformed and missing-field cases, parametrised with readable ids |
| Shared mutable default | call twice, or build two instances, and assert they do not share state |
| Lost failure meaning | assert the exception type, the message and that `__cause__` is set |
| Resource leak | fault injection inside the `with` block; counters or existence checks after it |
| Lost cancellation | cancel after the task reached an await; assert cleanup ran and `CancelledError` propagated |
| Unbounded wait | a timeout fixture with a small bound; assert `TimeoutError` |
| Stalled event loop | heartbeat lag check while the handler runs |
| Import-time effect | import in a fresh interpreter from an empty directory; assert no output and no files |
| Filesystem assumptions | temp paths only; assert nothing was written elsewhere |
| Secret in logs | capture logs at debug level; assert the secret value is absent |
| Order dependence | run with randomised test order where the repository has a plugin for it |
| Broken entry point | install the built package in a clean environment and run the console script |

Parametrised malformed-input test:

```python
import pytest


@pytest.mark.parametrize(
    ("text", "message"),
    [
        ("[]", "must be a JSON object"),
        ('{"port": "80"}', "settings.port"),
        ('{"port": true}', "settings.port"),
        ('{"port": 70000}', "settings.port"),
        ("{", "not valid JSON"),
    ],
    ids=["not-an-object", "port-is-text", "port-is-bool", "port-out-of-range", "broken-json"],
)
def test_bad_settings_are_rejected(text: str, message: str) -> None:
    with pytest.raises(SettingsError, match=message):
        load_settings(text)
```

Secret-in-logs test:

```python
import logging

import pytest


def test_token_is_never_logged(caplog: pytest.LogCaptureFixture) -> None:
    credentials = Credentials(user="svc", token="s3cr3t-value")   # token has repr=False
    with caplog.at_level(logging.DEBUG):
        logging.getLogger("importer").info("connecting as %s", credentials)
    assert "s3cr3t-value" not in caplog.text
```

Failure readability: one behaviour per test; a name that states the behaviour; an
assertion on the specific message or value; ids on parametrised cases. A failing test
should tell the reader what broke without opening the test body.

Do not mock away the thing under proof. A cleanup test that replaces `close()` with a
mock proves the mock was called, not that the resource was released.

Property tests fit parsers well (round trip; never an unexpected exception type). Use
them where the repository already has a property-testing library. Do not add one as part
of unrelated work.

#### `PY1-11` Use pytest or unittest fixtures to isolate state

State that leaks between tests: module globals and singletons, environment variables, the
working directory, `sys.path` and `sys.modules`, logging handlers and levels, the real
home directory, open event loops, and files in the working tree.

| Need | pytest | unittest |
| --- | --- | --- |
| Temporary directory | `tmp_path` | `tempfile.TemporaryDirectory()` with `addCleanup` or `with` |
| Environment variable | `monkeypatch.setenv` | `unittest.mock.patch.dict(os.environ, {...})` |
| Captured output | `capsys` | `contextlib.redirect_stdout` |
| Captured logs | `caplog` | `assertLogs` |
| Async test | the repository's async plugin | `unittest.IsolatedAsyncioTestCase` |
| Guaranteed restore | fixture teardown after `yield` | `addCleanup`, `tearDown` |

Rules:

- Every fixture that changes global state restores it, even when the test fails.
- Prefer the narrowest fixture scope. Session-scoped state is shared state.
- A monkeypatch that is not restored is a leak. Use the fixture or the context-manager
  form, never a bare assignment to a module attribute.
- Golden tests can preserve bugs. When you characterise existing behaviour before a
  refactor, mark which recorded outputs are known to be wrong.
- When there is no baseline at all, characterise with integration tests first.

#### `PY1-13` Prefer dependency injection over monkeypatching production code

Pass the clock, the environment mapping, the client, the runner or the filesystem adapter
in as a parameter. The test then supplies a small fake. This needs no patching, survives
renames, and keeps the test honest about what the code depends on.

Monkeypatch only where injection is not available (third-party code, a module-level
constant you cannot change), patch the narrowest name, and let the fixture restore it.

### 5. Packaging and tooling

#### `PY1-12` Preserve package metadata and supported Python versions

Preserve the repository's packaging system. Inspect `pyproject.toml`, `setup.cfg`,
`setup.py`, `tox.ini`, `noxfile.py`, `requirements*.txt`, and lock files before changing
tools.

What to read before a change:

```toml
[project]
requires-python = ">=3.10"          # every syntax and stdlib choice must fit this

[project.scripts]
import-orders = "importer.orders:main"   # the entry point a release must keep working
```

Rules:

- Do not raise or lower `requires-python` as a side effect. Newer typing syntax or a
  newer stdlib API is adopted only after a deliberate change to the target versions and
  the build matrix.
- Do not change the build backend, the dependency manager or the lock format unless
  migration is the task.
- Entry points, package data, dependency groups and optional extras are part of the
  contract. A change to any of them needs a build and an install check.
- An editable install can hide missing package data and stale metadata. Check the built
  artifact in a clean environment:

```bash
python -m build
python -m venv /tmp/check-env
/tmp/check-env/bin/python -m pip install dist/*.whl
/tmp/check-env/bin/import-orders --help
```

- A package that passes on one platform or one interpreter has passed on one cell of the
  matrix. Report the other cells as pending.
- Watch for: shared `pyproject.toml` configuration across packages, namespace packages,
  optional extras, version skew between lock file and metadata, generated code.
- If ownership of the packaging is unclear, defer the packaging migration and fix cleanup
  and errors first.

#### `PY1-15` Run formatter, linter, type checker, and tests as a single gate

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

Which tool to pick is decided by the repository, not by preference:

| Role | Candidates | Pick |
| --- | --- | --- |
| Test runner | pytest, unittest | the one the tests are written for and CI runs |
| Formatter | ruff format, black | the one configured; both only if the configuration requires both |
| Linter | ruff check, or the repository's existing linter | the one configured |
| Type checker | mypy, pyright | the one configured; do not generalise one checker's behaviour to the other |
| Orchestrator | tox, nox, make targets | use the session or target if it exists; it replaces the individual commands |

The complete order of a gate run: inspect Python targets and existing commands; write
behaviour-first tests for the affected boundaries and failures; then run the established
formatter, linter, type checker, tests, build, import-isolation check and entry-point
check. The details and the evidence to capture are in Verification Gate Command Set.

### 6. Default Reliability Stack and the handoff gate card

Keep one dated gate card per repository. Section B of the card is the Default
Reliability Stack: the nine checks that close every piece of Python work. The fixed
parts never change; the command battery is discovered from the repository's current
configuration.

```text
GATE CARD  repository: <name>   owner: <name>   discovered: <date>

A. Eleven bans (fixed)
   mutable default arguments | bare except | swallowed CancelledError | uncontained Any |
   assert for external validation | import-time network or filesystem mutation |
   print in library behaviour | manual open/close | stringly path handling |
   blocking calls in async functions | broad exception-to-None conversion

B. Default Reliability Stack (fixed)
   [ ] 1 Untrusted data is parsed or validated at the boundary.
   [ ] 2 Public functions and important internal seams have useful type hints.
   [ ] 3 Any is contained, justified, and narrowed quickly.
   [ ] 4 Mutable defaults are absent.
   [ ] 5 Resources are managed with context managers or explicit cleanup.
   [ ] 6 Async cancellation is preserved.
   [ ] 7 Import-time side effects are not added to reusable modules.
   [ ] 8 Tests cover errors, cleanup, and boundary behaviour.
   [ ] 9 Formatter, linter, type checker, and test gates were run or skipped with an
         explicit reason.

C. Review prompts (fixed)
   Input | Types | Errors | Resources | Async | Imports | Tests | Gates

D. Command battery (editable; from pyproject.toml / setup.cfg / tox.ini / noxfile.py / CI)
   test:      <command>
   format:    <command>
   lint:      <command>
   types:     <command>
   build:     <command or "not applicable: no packaging change">
```

Rules for the card:

- Refresh section D whenever a configuration file changes. A mismatch between the card
  and a fresh discovery proves the card is stale.
- A card without an owner rots.
- A CI pipeline may execute the mechanical parts. The card keeps the human prompts.
- Share a card across the packages of a monorepo only when their tool configurations
  really match.
- The bans are safe to fix in place for good. Tool flags are not.

### 7. Reading route card

For a team that uses this skill often, keep a small dated routing card per active
checkout:

- the eight jump points (scoreboard; sections 1 to 5; anti-pattern table; Default
  Reliability Stack), written as heading anchors, not line numbers, because positions
  drift;
- the result of the last heading check;
- the heading search commands;
- the three-step use order;
- which class of source backs which class of claim (official Python documentation for
  exception, context manager, dataclass, unittest and asyncio guidance; packaging and
  tool documentation for the gate commands);
- owner and last-verified date.

Refresh the card whenever the skill files change, and retire the old card at once. An
undated card is worse than none. Refreshing the card is its own small task and belongs
to the card's owner; when nobody budgets it, a stale card is paid for silently as
confusion during routed work. The alternative to refreshing on every change is to
re-verify the card on a fixed weekly schedule whether or not the files changed. That
wastes effort in quiet weeks and removes the need to watch for change events. A generated card removes manual refresh and needs its
own maintenance. Review fields: the concrete user goal, the adopt, adapt or avoid
boundary, and the verification gate.

Before trusting an existing card, verify it:

1. Compare its last-verified date with the change history of `SKILL.md` and
   `reference.md`. A card older than the latest change to either file is stale.
2. Rerun at least two of its heading checks and confirm they still hit.

```bash
git log -1 --format=%cs -- SKILL.md reference.md   # date of the latest committed change to either file
stat -c '%y %n' SKILL.md reference.md              # modification dates, for uncommitted changes (GNU stat)
rg -n '^### 3\. Async and resource reliability' reference.md
rg -n '^## Anti Pattern Registry Table' reference.md
```

The date field turns card freshness from a matter of trust into arithmetic: anyone can
compare the card's date with the files' dates and know whether a re-check is owed. Good:
a card dated last week with all eight heading checks marked found. Bad: an undated card
from a fork three revisions old. Borderline: one card shared by teammates on the same
commit, which is sound until one checkout diverges. What card upkeep costs across many
simultaneous checkouts is untested.

Authority when the card, the map and the content disagree: the destination section
governs content; the map governs reading order; the source list governs what was
consulted and when. A mismatch between the map and a heading is map drift. Trust the
destination, repair the map, and never delete content because a pointer rotted.

### 8. Reliability adoption packet and claim ledger

A change to policy or tooling (a new checker option, a new lint rule set, a raised
Python floor) needs an adoption packet:

- goal and risk;
- the pattern IDs involved and the class of each claim (repository fact, external fact,
  inference);
- Python and tool versions;
- repository configuration as found;
- current primary evidence for the mechanism, with retrieval date;
- affected boundaries;
- behaviour fixtures, including adverse ones, written before the migration;
- compatibility matrix, with unsupported combinations stated;
- rollout, rollback, and the trigger for the next refresh.

Rules:

- Every control links to source evidence and to an observation in the repository.
- Rollback preserves behaviour.
- Freshness is a reproduced behaviour difference, not a timestamp. Newer guidance that
  breaks a supported version or weakens a runtime test is not an improvement.
- Do not make the packet a link list, infer adoption from the latest documentation,
  bundle several tool upgrades, or declare freshness without a baseline and a diff.
- Replay from a clean environment: resolve versions and configuration, run the baseline
  and the new adverse fixtures, compare type and lint diagnostics, build, test the
  rollback, review unresolved claims.

Good: refresh one mypy option, prove its effect in configuration, stage it module by
module, keep runtime validation. Borderline: newer typing syntax only after a deliberate
change to target versions and the build matrix.

For a narrow code change a lighter claim ledger is enough: each claim, its pattern ID,
the file and line, and the test or command that proves it.

### 9. Requirements and traceability artifact

For a nontrivial change require all three: declared modes, executable `REQ-PY`
requirements, and a requirement-to-test table with `req_id`, `test_id`, `test_type`,
`assertion` and `target`.

- Requirements use observable `WHEN ... THEN ... SHALL` clauses.
- A revision suffix records change: `REQ-PY-001.1` becomes `REQ-PY-001.2`.
- Each row names a runnable test.
- Modes and requirements without the table are intention, not evidence.
- Review-only work may use the compact review-pass checklist instead.

## Worked Example Set

Judge an example by uncertainty containment, clarity of the public contract, lifecycle
ownership, failure context, compatibility, adverse tests and repository gates. Do not
judge it by annotation density.

For each example identify: the boundary and the core type, the expected versus the
exceptional outcome, resources, async flow, imports, filesystem use, fixtures, package
targets, gates, compatibility, and the reviewer's verdict. The examples are schematic.
Adapt them to the framework and the repository, and re-run them in the repository's own
tests, including the cancellation path, on the Python versions the repository supports.

### Example 1 (good): harden a CSV import CLI

Request: "Harden this CSV import CLI. It crashes on malformed rows and nobody knows which
row."

Mode: Boundary plus Testing. Surface: CLI. Main risk: bad input.

Requirements:

```text
REQ-PY-001.1
WHEN the CSV row lacks an `id` value
THEN the importer SHALL reject the row with an error naming the file and line number
AND SHALL continue with the next row
AND SHALL exit with status 1 after all rows are processed

REQ-PY-002.1
WHEN the input file cannot be opened or decoded as UTF-8
THEN the importer SHALL print one line naming the file and the cause to stderr
AND SHALL exit with status 2 without a traceback
```

Design: the CLI turns strings into a `Path`; the reader opens with `encoding="utf-8"` and
`newline=""`; each row dictionary is parsed into a frozen `Order` dataclass or raises
`RowError` with source and line; the core receives `Order` values only; `main` returns the
exit status and is called under `if __name__ == "__main__"`.

Traceability:

| req_id | test_id | test_type | assertion | target |
| --- | --- | --- | --- | --- |
| REQ-PY-001.1 | `test_missing_id_is_rejected_with_location` | unit | `RowError` message names `orders.csv:7` and the field | `parse_order` |
| REQ-PY-001.1 | `test_bad_rows_are_reported_not_dropped` | integration, temp file | one order kept, one warning naming `orders.csv:3` | `load_orders` |
| REQ-PY-002.1 | `test_cli_exit_code_for_unreadable_file` | integration | exit status 2, stderr names the file | `main` |
| (import safety) | `test_import_has_no_side_effects` | subprocess | fresh interpreter import prints nothing and writes nothing | package import |

The exit-status clause of `REQ-PY-001.1` has no row yet. That is an open item in the
matrix, and the change does not ship until a test for status 1 exists.

Gate: the repository's formatter, linter, type checker and tests; build and entry-point
check only if packaging changed. Verdict: ship when the record is complete.

The full code for this example is in `SKILL.md` under Templates.

### Example 2 (bad): unknown values inward, failures out as `None`

```python
def load(path: str) -> Any:
    f = open(os.path.join("data", path))
    try:
        data = f.read()
    except:
        return None
    f.close()
    assert data, "empty"
    print("loaded")
    return data
```

Sweep result for these ten lines: uncontained `Any`; manual open/close (the file leaks on
the `return None` path); stringly path; no explicit encoding; bare `except`; broad
exception-to-`None`; `assert` on external data; `print` in library behaviour. Eight hits,
each with a mechanism and a replacement. Fix the resource path first, then narrow the
exception.

```python
import logging
from pathlib import Path

logger = logging.getLogger(__name__)


class DataFileError(Exception):
    """A data file that cannot be used."""


def load(name: str, *, base: Path) -> str:
    path = base / name
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        raise DataFileError(f"cannot read {path}: {exc}") from exc
    if not text:
        raise DataFileError(f"{path} is empty")
    logger.debug("loaded %d characters from %s", len(text), path)
    return text
```

What became explicit: the return type, the base directory, the encoding, the two failure
cases, and the cause of each.

### Example 3 (borderline): one dynamic third-party adapter

A vendor callback hands over an untyped object. Isolating it is acceptable when the
adapter has explicit parsing, logging, tests and removal criteria. Unknown values may
enter the adapter. They may not escape into the core.

```python
import logging
from dataclasses import dataclass

logger = logging.getLogger(__name__)


class VendorPayloadError(ValueError):
    """A vendor callback payload that cannot become an Event."""


@dataclass(frozen=True, slots=True)
class Event:
    kind: str
    ident: str


def to_event(payload: object) -> Event:
    """Adapter for the untyped vendor callback. Remove when the vendor ships type stubs."""
    kind = getattr(payload, "kind", None)
    ident = getattr(payload, "id", None)
    if not isinstance(kind, str) or not isinstance(ident, str):
        logger.warning(
            "vendor payload rejected: kind is %s, id is %s",
            type(kind).__name__,
            type(ident).__name__,
        )
        raise VendorPayloadError("vendor payload lacks a text kind and id")
    return Event(kind=kind, ident=ident)
```

The parameter is `object`, not `Any`, so the function body has to prove each attribute.
The log line reports types, not values.

### Example 4 (multi-hit): an async poller that hangs on shutdown

```python
async def poll(url: str) -> None:
    while True:
        try:
            handle(requests.get(url).text)   # blocks the loop
            time.sleep(5)                    # blocks the loop
        except:                              # also catches CancelledError
            pass
```

Three hits in one place: blocking calls in an async function, a bare `except`, and
swallowed cancellation. Fix order: blocking and resource handling first, then the
exception handling.

```python
import asyncio
import logging
from collections.abc import Awaitable, Callable

logger = logging.getLogger(__name__)


class FetchError(Exception):
    """The upstream could not be read."""


async def poll(
    fetch: Callable[[], Awaitable[str]],
    handle: Callable[[str], None],
    *,
    interval: float,
) -> None:
    while True:
        try:
            handle(await fetch())
        except FetchError:
            logger.warning("poll failed; next attempt in %.0f s", interval, exc_info=True)
        await asyncio.sleep(interval)
```

The handler is now narrow, so it cannot catch cancellation. The fetch is injected, so the
test needs no network. The test cancels the task after it has reached an `await` and
asserts that `CancelledError` propagates.

### Example 5: the two source examples and their limits

- `ImportReport` (`PY1-03`) shows frozen, slotted value data with an explicit
  `default_factory`. Port the `default_factory` shape wherever a default is mutable. Do
  not port `frozen` or `slots` where the model mutates, needs dynamic attributes, or a
  serializer requires otherwise.
- `run_job` (`PY1-07`) shows cancellation discipline: cleanup, then a bare `raise`. Never
  drop the re-raise. Its cleanup call can itself raise and mask the cancellation, so
  production code may need scoped or shielded cleanup.

### Example 6 (tooling): one checker option, staged

Good: refresh one mypy option, prove its effect in the repository's configuration,
enable it for one module per cycle behind the existing gates, and keep the runtime
validation. Bad: migrate the formatter, the checker, the async design and the packaging
together. Borderline: adopt newer typing syntax only after a deliberate change to the
target versions and the build matrix.

Strictness applied file by file in a loose codebase can create two dialects. Bound the
migration and give it an end.

### Other verdicts to calibrate against

| Verdict | Case |
| --- | --- |
| Good | Parse JSON into a frozen value, inject a protocol, test malformed input and client cleanup |
| Good | A subprocess script with typed errors and a context-managed temporary directory |
| Good | Staged CSV hardening: malformed-row tests, typed records, explicit encoding, contextual errors, temp fixtures, then package and type gates |
| Good | Harden an HTTP adapter first, then the core types |
| Good | Find mutable defaults plus stringly paths in a diff and apply both replacements |
| Bad | Pass `Any` inward and catch everything as `None` |
| Bad | Annotated dictionaries and broad `except` blocks |
| Bad | Memorise the anti-pattern names without sweeping the diff |
| Bad | Add every listed tool |
| Bad | Use general typing rules to decide transaction retries |
| Borderline | A protocol with only one implementation and no test double |
| Borderline | A small script kept informal while its effects and failures stay explicit |
| Borderline | Generated code: the sweep applies, but idiom frequency in it is unrealistic |

Things an example must not do: present a `TypedDict` as runtime validation; add a protocol
with no seam; mock away the cleanup it claims to test; test cancellation without
scheduling the work; hide a behaviour change inside a tool migration.

### Practising with the examples

- Gate training: take one recent real diff. Sweep all eleven rows and record the explicit
  no-hits. Answer all eight prompts. Then gate a second diff alone.
- Routing training: start with a hit case (scoreboard, the one matching async and
  resource section for a cancellation bug, the closing anchors, the source list when
  challenged). Then a miss case (no jump point matches; resolve with one heading search;
  never open everything).
- Pair a newcomer who routes aloud with an experienced observer. It surfaces
  misconceptions.
- Rotate a renamed-section drill so nobody overfits to the current pointers.
- How much recognition these drills build is not measured.

## User Journey Scenario

### Hardening working-but-loose code

The user has scripts, CLIs, services or async workflows that work but are loose. They
must harden them without breaking the repository's conventions. They name the surface,
the main risk and the gates that already run. They select modes, perform one bounded
hardening step, and prove it with an existing gate.

Steps:

1. Capture current behaviour and the Python targets.
2. Identify runtime boundaries and effects.
3. Write adverse tests.
4. Introduce parsed values and owned lifecycles.
5. Tighten types behind seams.
6. Run the existing gates.
7. Build artifacts.
8. Migrate incrementally, with rollback points.

Rules along the way:

- Preserve public behaviour. One reviewable boundary at a time.
- If no baseline exists, characterise with integration tests.
- If imports depend on the environment, add an adapter.
- If ownership is unclear, defer the package migration while fixing cleanup and errors.
- Introduce protocols before replacements. Keep synchronous flow where it is adequate.
- Watch for: golden tests that preserve bugs, editable installs that hide metadata,
  permanent strictness exclusions, leaking fixtures, accidental changes to supported
  versions.

In scope: clearer interfaces, fewer implicit globals, safer exceptions, stronger test
seams, review of bad inputs, partial state or cancellation. Out of scope: greenfield
framework choice, FastAPI architecture, data-science pipelines, governance.

Record: baseline outputs, targets, risk inventory, characterisation tests, the changed
boundary, the type and validation delta, resource and cancellation cases, artifact,
compatibility, rollback, and remaining debt. The actual order depends on architecture,
ownership and tool configuration.

### Gating a change that is believed complete

Enter when a Python change is believed complete and needs a defensible decision: ship,
bounce with citations, or escalate.

- Every bounce cites an anti-pattern row or a stack item. That keeps the review from
  becoming an argument about taste.
- Self-gating is valid. It is especially prone to excusing the `Gates` answer, so run the
  commands and paste the exit codes.
- Do not use the gate to choose between dataclasses and dictionaries, to design a
  pattern, or to decide whether the skill applies. Those are design questions.

### Routing before reading

Open the routing table before reading or implementing, when a bounded Python task that
has not started needs a short list of sections. Return afterwards only when someone
challenges where a rule came from.

- A pattern question in the middle of implementation goes straight to the pattern
  section.
- A quality doubt after implementation goes to the gates.
- Good: route a flaky-cancellation ticket and leave with one section. Bad: use the
  routing table as a source of code-review prompts. Borderline: re-route every subtask of
  one feature.
- The time a correct shortlist takes is not measured.

## Anti Pattern Registry Table

Match every reviewed diff against all eleven rows. For each hit require both the
mechanism and the replacement. A bare taboo list produces comments nobody can act on.

### The eleven rows

| Anti-pattern | Why it fails | Prefer | Enforcement class | How to find it |
| --- | --- | --- | --- | --- |
| Mutable default arguments | State leaks across calls | `None` sentinel or `default_factory` | lint | lint rule; search for `=[]`, `={}`, `=set()` in signatures |
| Bare `except:` | Catches cancellation, interrupts, and hides root cause | Catch specific exceptions | lint | lint rule; search for `except:` |
| Swallowing `asyncio.CancelledError` | Breaks cooperative cancellation; shutdown becomes a hang | Cleanup, then re-raise | human, plus a cancellation test | read every handler around an `await`; search for `CancelledError` and `BaseException` |
| Uncontained `Any` | Disables useful type checking downstream | Narrow at boundary | type checker, lint for annotations | checker options; search for `Any`, `cast(`, `# type: ignore` |
| `assert` for external validation | Can be optimized away and gives poor diagnostics | Explicit validation and typed errors | lint, then human | lint rule outside tests; decide per hit whether the value is external |
| Import-time network or filesystem mutation | Imports become slow, flaky, and unsafe | Move side effects behind functions or CLI entry points | human, plus an isolated-import test | read module top level; import in a fresh interpreter |
| `print` in library behaviour | Hard to route, test, and filter | `logging` or returned diagnostics | lint | lint rule with the CLI module exempted; search for `print(` |
| Manual open/close | Leaks resources on exceptions | `with` or `async with` | lint for files, human for other resources | lint rule; search for `.close()` not inside `finally` or a context manager |
| Stringly path handling | OS and relative-path bugs hide | `pathlib.Path` | lint | lint rules; search for `os.path.` and `+ "/"` |
| Blocking calls in async functions | Event loop stalls under load | Synchronous API or executor isolation | lint for known calls, human for the rest | lint rules; read `async def` bodies for sync IO, `time.sleep`, `subprocess.run` |
| Broad exception-to-`None` conversion | Callers lose cause and remediation | Typed result or contextual exception | human | search for `except Exception` followed by `return None`, `pass` or `continue` |

Cover all three enforcement classes. Lint catches shapes. The type checker catches
erased types. Some rows need judgment, and exception-to-`None` conversion is the clearest
case.

Legitimate boundaries: `print` is acceptable for CLI user output. `assert` is acceptable
in tests and for internal invariants. Entry points are the sanctioned home for effects. A
cheap pure cached module constant is usually acceptable.

### More code shapes to reject

| Shape | What it erases | Replacement |
| --- | --- | --- |
| Unparsed runtime data reaching core logic | type information | parse into domain values at the boundary |
| Validation scattered across layers | one place to fix | one parser per boundary |
| Cleanup left to garbage collection | lifecycle ownership | context managers |
| Clients created at import time | import safety | import-safe factories |
| Secrets in printed or logged output | confidentiality | structured logging with named fields; `repr=False` |
| Fixtures that leak global state | test isolation | isolated fixtures with guaranteed restore |
| Exception translated without its cause | failure context | `raise ... from exc` |
| Tasks with no owner | lifecycle ownership | `TaskGroup`, or a kept reference that is cancelled and awaited |

These erase type information, failure context or lifecycle ownership, and they often
survive happy-path tests.

### Gotchas

- Mutable dataclass fields.
- Subprocess calls that block.
- Module-level clients.
- Monkeypatches that are not restored.
- Real home paths in tests.
- Cancellation classes that depend on the Python version.
- Import caches that hide an import-time effect.
- A module-level cache is acceptable only if lazy, deterministic, resettable,
  thread-safe and tested.

### Guidance and reading anti-patterns

These apply to an agent's use of this skill, not to Python code. They show up in the
working record, not in a linter.

| Failure | Cause or risk | Safer replacement | Detection |
| --- | --- | --- | --- |
| Context-free summary | generic advice that skipped the skill's content | read the map, then the matching material, then answer | the answer cites no pattern, rule or section |
| Unsourced recommendation | confident prose hides where a claim came from | label repository fact, external fact and inference | check for all three labels |
| Unverified instruction | nothing to check it against | couple every recommendation to a gate | a concrete command, reviewer question or metric is present |
| Whole-reference dumping | thoroughness disguises waste | scoreboard, then matching sections only | compare what was loaded with the size of the task |
| Unrouted reading | browsing replaces a deliberate route | follow the use order literally | no trace of the use order |
| Pedigree-free synthesis | a claim has no auditable basis | cite the source list | no source cited |
| Stale-router trust | pointers outlive the headings they point at | check headings at every refresh | a pointer with no matching heading |

A hard cap on how much may be loaded is a blunt alternative where records are
unreliable. Aggregate these by boundary, never by person. They are not a tool for
watching individuals.

## Verification Gate Command Set

### Order

1. Inspect the Python targets and the existing commands.
2. Write behaviour-first tests for the affected boundaries and failures.
3. Run the established formatter, linter, type checker and tests.
4. When packaging changed: build, then the entry-point check in a clean environment.
5. When a reusable module changed: the isolated-import check.

Run and record the selected battery as one gate.

### Discovery

```bash
rg --files -g 'pyproject.toml' -g 'setup.cfg' -g 'setup.py' -g 'tox.ini' -g 'noxfile.py' -g 'requirements*.txt'
rg 'pytest|unittest|ruff|black|mypy|pyright|coverage|tox|nox' .
```

Then read the CI workflow. The command shape in CI or the project documentation wins
over any generic form.

### Menu

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

- Prefer `python -m` forms when they avoid path ambiguity. They bind the tool to the
  active interpreter.
- Some repositories run the tools with a path argument (`ruff check .`, `mypy .`) and
  some run them bare (`ruff check`, `mypy`) and let configuration select the files. Use
  the form CI uses.
- One test runner, one formatter, one type checker. `tox` or `nox` sessions can subsume
  the individual commands.
- Whether each flag still exists in the current release of each tool is not verified
  here. Confirm with `--help` in the target environment.

### What each gate does not prove

| Gate | Does not prove |
| --- | --- |
| Type checker | that runtime data is valid; it does not parse anything |
| Linter | that cleanup happens |
| Unit tests passing | import safety, packaging, cancellation or CLI behaviour, unless a test targets them |
| Formatter | anything about behaviour |
| Build | that the installed entry point runs |
| Any command | that cancellation is handled correctly everywhere; use the review prompts |

### Lint rule candidates

Where the repository already uses Ruff, these rule codes correspond to anti-pattern rows.
The names were confirmed with `ruff rule <code>` on Ruff 0.17.6. Rule sets move between
releases, so confirm on the installed version, and do not enable rules the repository
has not chosen as part of unrelated work.

| Row | Candidate rules |
| --- | --- |
| Mutable default arguments | `B006`; `RUF012` for mutable class attributes |
| Bare `except:` | `E722` |
| Blind `except Exception` | `BLE001`; `S110` for `except ...: pass` |
| Uncontained `Any` | `ANN401` for annotations; the type checker for inferred `Any` |
| `assert` | `S101`, with tests exempted |
| `print` | `T201`, with the CLI module exempted by a per-file ignore |
| Manual open/close | `SIM115` |
| Missing `encoding=` | `PLW1514` (preview at the time of the check) |
| Stringly paths | the `PTH` family, for example `PTH118`, `PTH123` |
| Blocking calls in async | the `ASYNC` family, for example `ASYNC210`, `ASYNC230`, `ASYNC251` |
| Lost exception cause | `B904` |
| Task with no kept reference | `RUF006` |

The source count is that eight of the eleven rows can be expressed as lint rules, which
leaves three for human judgment. A fixture holding all eleven shapes agreed on Ruff
0.17.6: the rules above flagged eight rows and did not flag swallowed cancellation, the
import-time client, or the conversion to `None` as such. That is one fixture on one
version, not a general result.

`T201` also flags `print` in a CLI entry point. Exempt the CLI module instead of
disabling the rule.

### Evidence to capture

Python and tool versions; the configuration files read; the exact commands; the tests
selected, including the adverse ones; exit codes; the isolated-import result; resource
and cancellation observations; the build artifact; the entry-point result; failures; and
unresolved risk. Keep the project's gates separate from tests that need external
services.

### Pitfalls

The wrong virtual environment. An editable install that masks missing files. Plugin
behaviour. Cached diagnostics. Formatter overlap. Platform filesystem assumptions.
Cancellation tests that never reach an `await`.

### Checking this skill's own headings

```bash
rg '^##|^###' reference.md
rg 'Pattern Scoreboard|Anti Pattern Registry|Default Reliability Stack' SKILL.md reference.md
```

Run them from the skill directory. An empty result can mean the wrong directory, so
confirm the paths resolve before reading absence as drift. A pointer in `SKILL.md` with
no matching heading here is a defect in the pointer.

The opposite defect is a section here that `SKILL.md` never names. A routed reader
cannot find it. This loop lists every top-level section of this file that is missing
from `SKILL.md` and prints nothing when all are registered:

```bash
grep -E '^## ' reference.md | sed 's/^## //' | while IFS= read -r h; do
  grep -q -F "$h" SKILL.md || echo "not registered in SKILL.md: $h"
done
```

It matches whole heading text on one line, so keep each heading name unbroken in the
"Using reference.md" tables of `SKILL.md`.

## Failure Mode Table

### Code failures by class

Classify the failure. Identify which distinction disappeared. Withdraw the claims that
depended on it until it is repaired.

| Class | Typical symptom | Distinction lost | Recovery |
| --- | --- | --- | --- |
| Runtime boundary | `KeyError` or `TypeError` deep in the core | valid versus invalid input | boundary adapter that parses |
| Core contract | wrong type flows through unnoticed | known versus unknown type | narrow types; contain `Any` |
| State model | a value changes between calls | fresh versus shared state | factories; frozen values |
| Expected outcome | caller ignores a `None` | success versus business failure | typed result |
| Exceptional path | vague message, no cause | which failure, and why | preserved cause; narrow handlers |
| Resource lifecycle | leaked handle, leftover temp file | open versus closed | context managers |
| Async control | hang on shutdown, timeout ignored | cancelled versus completed | re-raise cancellation; bounded waits |
| Event loop | every task slows together | async versus blocking work | isolate blocking calls |
| Import | import is slow, or fails without network | definition versus execution | deferred imports; factories |
| Filesystem | partial file, wrong separator, wrong encoding | complete versus partial write | temp path then replace; explicit encoding |
| Diagnostics | cannot tell what happened; secret in a log | signal versus noise | structured logging with redaction |
| Test isolation | passes alone, fails in the suite | this test's state versus another's | restore fixture state |
| Package | works in the checkout, fails when installed | source tree versus artifact | repair metadata; clean install check |
| Tooling | checker green while a module is excluded | checked versus configured | fix the configuration; stage strictness |

Do not make every defect a typing issue. Do not suppress diagnostics. Do not patch away
ownership.

Watch for: cleanup exceptions; cancellation between state changes; partial files;
logging failures; import caches; test order; editable installs; checker configuration
that masks modules. A cleanup leak under timeout is both a resource failure and an async
failure. Add a cancellation fixture.

### Process failures

| Failure | Trigger | Mitigation |
| --- | --- | --- |
| Source drift hides the truth | repository or ecosystem guidance changed | refresh the public evidence, rerun the local gate, mark stale claims |
| Generic advice escapes review | plausible practice with no specific check | block until it has a concrete command, reviewer question or metric |
| Implicit decision path | adopt, adapt or avoid is unclear | add the decision table, the cost of error and the adjacent route |
| Sources become a flat list | many sources, no ranking | classify each as canonical, supporting, legacy, duplicate or conflicting |
| The plan is lost in long work | constraints and intent forgotten | checkpoint, and reread the plan before destructive steps |
| Tool fanout exceeds the budget | parallel actions conflict or duplicate | cap fanout, assign ownership, add merge and audit checkpoints |
| Out-of-scope activation | framework, web, data or deployment concern | route to the companion guidance |
| Skipped activation | qualifying Python work with no mode declared | reclassify before review |
| Vague requirements | words such as `robust` left in place | bounce the requirements; demand observable SHALL clauses |
| Tool-migration smuggling | a new tool configuration appears in a bug fix | search the diff and CI for new tool configuration; require an explicit migration |
| Green checks, missing requirement | tests pass but a `REQ` has no test | audit every `REQ` identifier to a test or review assertion |
| Metric claim without a method | a number with no way to reproduce it | replace with threshold, fixture, command and owner |

The last four activation rows are detectable from the artifact alone: missing modes,
missing `REQ-PY`, vague words, new tools. How often activation mismatches happen is not
measured.

### Gate and routing operation failures

| Failure | Trigger | Mitigation |
| --- | --- | --- |
| Rubber-stamping | records look perfect, nobody looked | one seeded-hazard drill per quarter |
| Commands never run | exit codes were typed, not observed | re-execute the recorded battery on a sampled change |
| Gate decay | one person gates everything | rotate gate duty |
| Silent map staleness | a section was renamed or edited | heading check at every refresh; automate a failing check |
| Unregistered section | a section was added here and not to the tables in `SKILL.md` | register it the day it lands; run the registration loop at every refresh |
| Unjustified opens | the record lists sections with no step 2 match beside them | reject the record; re-route from the diagnosed boundary |
| Stale card or embedded copy | the card or prompt copy predates the latest change to the skill files | compare dates, rerun two heading checks, re-copy |
| Ritual routing | the route is recorded but sections are chosen from memory | quarterly route-aloud spot check |
| Provenance rot | the dated source list ages | date every citation and refresh the evidence |

Frame drills as calibration, not punishment. A terse pass may be fluency or
rubber-stamping; the drill tells them apart. Healthy-looking records can hide all of
these. Each row needs an owner and a cadence, and they decay at different rates.

## Workload Model

- Scope one unit of work to one coherent behaviour change and one compatibility matrix.
- Split independent adapters, resource owners, async task trees, packages, domain
  migrations and owners. Give each split one verification owner.
- Do not combine checker, formatter, packaging and behaviour changes. Combining them
  obscures cause and makes rollback hard.
- Inventory before starting: modules, contracts, runtime inputs, effects, resources,
  tasks, dependencies, Python versions, tools, owners, adverse fixtures.
- Watch for: shared `pyproject.toml` configuration, namespace packages, `Any` crossing
  modules, fixture scopes, event-loop ownership, generated code, artifacts that span
  owners.

Gating:

- Gate one reviewable diff per cycle. Split oversized diffs instead of skimming. A
  thousand-line diff cannot be swept meaningfully in one cycle.
- Six small diffs with full records are better than one very large diff waved through.
- Batching saves setup and degrades attention. Track cycle counts, duration, and whether
  records thin out toward the end of a long sitting.
- CI can move the mechanical rows out of the human cycle.
- The gate is a quality-bar rubric: review blockers, lint gates, release criteria.

Reading:

- Budget one mode's section family per question. For point work use the routing table
  plus one matching section.
- Cost tracks sections opened, not files touched.
- Route each task at pickup, not a backlog in one batch. Routing twenty unrelated tasks
  in a row degrades well before the end. Routing once per epic that shares a boundary is
  defensible if noted.
- Clarify unroutable tasks upstream.
- Batch tiny fixes to amortise the requirements and traceability overhead.
- Record what was loaded and flag overruns.

Capacity limits. The sources give three positions and none is measured:

| Position | Limit |
| --- | --- |
| Agent workflow | one primary task, up to 10 source files, up to 3 delegated subtasks, plus a written completion audit |
| Reference use | one audience, one decision, up to 12 source documents, one verification checklist |
| Pattern application | do not treat source count as capacity; no universal module, source or fixture limit is supported |

Use the first two as provisional split triggers. Beyond them, split the task or narrow
the reading. Check that the output changes the next implementation or review action.

## Reliability Target

These are proposed review and sampling contracts. They are not achieved results, and
they are not runtime certification. Each sampled target needs an owner.

Hard gates for every affected change:

1. Boundary parsing.
2. Justified dynamic escapes.
3. Deterministic defaults.
4. Meaningful errors.
5. Owned cleanup.
6. Preserved cancellation.
7. Import safety.
8. Supported targets unchanged.
9. Unsupported claims rejected.

Failure-path guidance is rejected unless it names the bound, the cleanup route, the
re-raise or rejection behaviour, and the validation error. The target is every
failure-path recommendation. Resources close on success, error and cancellation. Async
code preserves `CancelledError`. Untrusted data becomes typed before domain logic.

Guidance-quality targets:

| Target | Threshold or method |
| --- | --- |
| Evidence boundaries | 100% of recommendations show repository fact, external fact and inference separately |
| Decision accuracy | at least 18 of 20 sampled uses route correctly to adopt, adapt, avoid or adjacent |
| Unsupported claims | zero production, security, latency or reliability claims without a source, an inference label or a verification method |
| Recovery clarity | every avoid or failure case names rollback, escalation or the next reference |

Gate targets:

- Triage every discovery after handoff of an enumerated hazard within one week. Attribute
  it to a sweep miss, a stack miss, a battery gap or a review-pass miss.
- Operational target: zero escapes of enumerated hazards per quarter, with every escape
  triaged.
- In low-traffic repositories statistics accumulate slowly. Use qualitative review or
  sampled re-gating. Seeded drills corroborate a zero.
- Do not count novel hazards outside the twenty enumerated items (eleven rows plus nine
  checks) as gate failures. Whether an escape through an explicitly skipped gate counts
  is a matter of local policy.

Routing targets:

- Zero stale pointers at each refresh.
- Triage every reported misroute within a week as a map defect or an operator error.
- Recording must be low-blame. Silent recovery makes the numbers meaningless.
- If live misses are sparse, have a second person re-route sampled past tasks, or run a
  seeded misroute drill.

Do not claim 18 of 20, complete labels, zero `Any`, or working cleanup without the
samples, the fault tests and the cancellation tests behind them. A target states scope,
versions, class, denominator, fixtures, consequence, owner, retest, raw results,
exclusions and uncertainty. Sample routing outcomes and migration outcomes separately.

## Retry Backpressure Guidance

Four different things are called retry. Their failure semantics differ. Do not carry a
rule from one to another.

### Runtime retries in Python code

Retry only after all of these:

- the failure is classified;
- partial effects and resources are inspected;
- cancellation is preserved;
- a relevant prerequisite has changed;
- the replay is proven idempotent, or there is explicit compensation.

A blind retry duplicates actions, overwrites partial files, reruns subprocesses, leaks
clients, or revives cancelled workflows.

Require: operation identity, input, state snapshot, effect ledger, attempt budget, the
changed prerequisite, cleanup, owner, and a definition of semantic success.

Never broadly retry programmer errors, cancellation, package tests until they turn green,
or file and database effects that are only assumed to be atomic.

Alternatives: resume from a validated checkpoint; temp-file or transaction rollback;
recreate an isolated fixture; repair the environment or the dependency; synchronous or
manual recovery; escalate to the domain owner.

| Verdict | Case |
| --- | --- |
| Good | one retry of a classified transient read-only HTTP fetch, with cleanup |
| Bad | retry `CancelledError` or a partial mutation |
| Borderline | rebuild a wheel after cleaning the environment and changing a verified dependency |

### Async backpressure and cancellation

- Specify cancellation behaviour, cleanup, re-raise and timeout bounds together.
- Preserve `CancelledError` and isolate blocking calls. Hide neither behind a broad
  `except`.
- Use `TaskGroup` only when the supported Python version allows it.
- Keep synchronous code synchronous when async adds no concurrency value.
- Shielding cleanup can be correct during shutdown and is dangerous as a habit.
- Bound queues and concurrency explicitly. An unbounded queue hides overload until memory
  runs out. Runtime cancellation policy is a different subject from retrying a
  documentation refresh.

### Re-gating after a bounce

- Verify each bounced item explicitly, then run one full fresh sweep. The focused check
  catches the requested fix. The fresh sweep catches regressions.
- Mechanical hits should converge in one cycle.
- Three total cycles without convergence triggers a design-review escalation. Pair the
  author and the gate operator for complex fixes.
- A one-token fix (for example a `default_factory`) may skip the fresh sweep only if the
  record says so.

### Re-routing and refreshing guidance

- Wrong section: try one heading search. If that misses, stop and re-diagnose the task's
  boundary before opening more. Cap at two re-routes and note every fallback.
- What each miss means: a missed jump point suggests a stale pointer; a missed search
  suggests the content is absent; a boundary re-diagnosis suggests the task cannot be
  routed here.
- Pairing with someone who knows the material collapses the loop.
- Retry a guidance check only after classifying the signal as transient, stale evidence,
  missing context, or a true contradiction. Allow one bounded refresh of stale external
  evidence, then escalate to a person or a narrower reference.
- Stop implementation when source coverage, critique coverage or verification gates are
  red.
- In long work, checkpoint after each batch and reread the current specification before
  broad rewrites, commits, pushes or destructive operations.
- In distributed work, one owner per file or batch, with a merge-time check of paths,
  headings and evidence labels.

## Observability Checklist

### In the code

- Log at adapters and orchestration boundaries. Messages are actionable and carry
  identifiers, counts and duration.
- Record: revision; package, Python and dependency versions; boundary and operation
  identifiers; the validated shape, not sensitive raw data; exception type, cause and
  chain; resource and task lifecycle; cancellation; an effect summary.
- Use correlation identifiers. Redact at collection, not afterwards.
- Library logging is structured and configured by the caller.
- A pure domain layer may return diagnostics instead of logging.
- Library code does not use `print`. CLI user output may.

Avoid: raw payloads and environment values; `print`-only diagnostics; lost exception
causes; success-only events; missing tool versions; secrets in `repr`; logging whole
dataclasses; duplicate handlers added at import; nameless tasks; cancellation labelled as
an error; logs that change timing.

Good: a redacted import record that includes the parser rejection, a correlation
identifier, the exception cause, the fact that no file was written, and the closed
client.

Checks: search for boundary logging and for `print` outside CLI paths. Test the
redaction. From the logs alone, reconstruct the boundary, the outcome, resources, tasks,
effects, package and tool versions, the gate and the recovery. Retention and volume
budgets are deployment-specific.

### In the gate record

Every cycle emits:

- all eleven row outcomes, including no-hits;
- all nine stack results;
- the exact command battery and exit codes;
- the eight labelled prompt answers.

Rules:

- Negative results are essential. A hit-only log cannot tell clean from unswept.
- CI may generate the mechanical part. People answer the prompts.
- Never copy diff payloads or secrets into the record. Identify changes by identifier and
  line range.
- A thumbs-up is not a record. Deviation-only records erase most of the signal.
- Store records where a quarterly tally can reach them. Sample them for complete,
  non-generic fields.

### In the routing record

One light record per use, including misses and fallbacks: task identifier, diagnosed
boundary, jump point or fallback used, sections opened, confirmation of the closing gate
anchors, operator, date.

`sections opened` is the essential field. It separates a disciplined route from a ritual
one. Write the step 2 match beside each opened section. A record with an opened section
and no match is rejected, however complete its other fields are. An agent can derive the
record from what it loaded. A person records at routing time, not from memory.

### Audit packet

Keep audit evidence small: sources loaded and deliberately skipped; the exact proof
command, reviewer question or artifact; p50, p95 and p99 where runtime latency applies,
or reviewer time otherwise; tool calls; files in context; delegated tasks; retries; the
completion-audit outcome; the decision; uncertainty; the refresh trigger; the leading
indicator and the failure signal. Prefer a command summary, a changed-file list and
unresolved risks over raw transcripts.

## Performance Verification Method

### Code

- Inspect structural idioms first. Demand latency measurements only when an explicit
  budget exists.
- One synchronous call on an event loop can degrade every concurrent task. Audit async
  handlers for blocking file and network IO and isolate it.
- `slots=True` is for memory and attribute discipline when appropriate, not a default. It
  can break dynamic attributes and serializers.
- `pathlib` is a structural idiom, not a performance choice.
- If a budget is missed and no structural fix is obvious, profile.
- Record the idiom present and the measured value against the budget. Service budgets are
  not known here. They come from the owners.

### The gate

- Timestamp request, start and completion. Review waiting against working time monthly.
  Fix waiting before trimming checks.
- Measure each tier separately. Read latency next to the escape ledger: a fast average
  with rising escapes is a failure.
- Track p95 queue wait, not only the mean. One day-long oversized diff disappears in an
  average.
- The compact tier is expected to take minutes. That is an expectation, not a
  measurement. Dedicated gate hours trade immediacy for predictable waits.
- The acceptable p95 is local policy.

### Routing and review

- Measure the time from task pickup to section shortlist, and the footprint: sections
  opened against sections the map named. Review monthly beside the misroute rate.
- A fast wrong route is worse than a slow correct one.
- Track the median and the worst monthly footprint. One section is success. All eight
  jump points is the dumping failure.
- Report first-contact routings separately instead of excluding them.
- Route-time ceilings depend on urgency and are local policy.

### The ten-minute hypothesis

"A reviewer finds the correct next action in ten minutes or less" is an unproven
candidate hypothesis. No observed sample supports it.

To test it: compare matched Python tasks. Measure orientation, risk classification,
routing, test selection, time to a verified next action, correctness, and evidence
completeness. Do not measure skimming or tool adoption. Fix the task and code snapshot,
Python targets, reviewer experience, sources, start and stop events, expected decision,
rubric, failures and baseline.

Keep documentation-review time apart from runtime and tool latency. Until samples
support percentiles, use time to the first relevant pattern or adverse fixture, effort,
sources avoided, or qualitative clarity.

Publish: cohort, raw durations, decisions, rubric and evidence score, exclusions, the
percentile calculation, baseline, uncertainty. Confounders: learning effects,
familiarity, codebase size, hidden setup, caching, parallel review, excluded uncertainty.

Measurement packet: input size, source count, tool-call count, wall-clock time, p50, p95
and p99 where runtime applies, reviewer decision time otherwise. Beyond one focused
sitting, require tool-call and timeout budgets and a resumable journal.

Pass: the reviewer can identify the next action, the verification gate and the stop
condition without opening unrelated files. Fail: implementation is encouraged before the
workload, the reliability target and the failure modes are explicit.

## Scale Boundary Statement

This skill covers single-process Python reliability inside one repository's toolchain,
typically one interpreter with one event loop or thread pool.

In scope: subprocess lifecycle and cleanup. Not in scope: multiprocessing design,
topology, distributed queues and locks, fleet coordination, distributed cancellation.

Hand off at the first question about a framework, another process, another service, a
distributed queue or lock, or fleet coordination. Also hand off when the work spans
several independent systems, more than one ownership boundary, unbounded source
discovery, or production traffic without an explicit service-level objective.

When splitting:

- Split by package, service, runtime boundary, concurrency domain or owner.
- Preserve typed interface contracts across the split. Coordinate shared configuration.
- Add evidence the general skill does not supply: service-level objectives, security,
  persistence, deployment, integration, release, rollback.
- Each split needs: behaviour boundary, owner, Python and dependency matrix, artifact,
  tests, effect model, integration contract, operational evidence.
- One checklist cannot certify several services. One mypy run cannot certify a monorepo.

Watch for: namespace packages, shared environments, configuration inheritance in a
monorepo, cross-service schemas, queue semantics, optional extras, version skew,
generated clients, implicit async and sync lifecycles, parallel edits to fixtures and
configuration.

Under distributed execution: one verification owner per split and a merge checkpoint.
Under long work: checkpoint, summarise risks, re-verify the specification. In a large
codebase: narrow the dependency and source graph first.

Prefer vertical hardening (parsing, types, resources) before treating pressure as a
scale problem.

The gate design fits one team and a few repositories. At larger scale, automate the
mechanical rows in shared configuration before adding gate operators. Copying a gate card
does not copy calibration: where automation is unavailable, have several operators gate
the same sample diff. Shared CI becomes a drift surface and needs an owner and a refresh
habit.

The routing table works while it fits in one glance and has one date. Beyond roughly a
dozen jump points use a hierarchy or per-area maps. References revised independently
need per-file dates. Several skill bundles need a router of routers. A list of forty
entries is a table of contents, which is dangerous for an agent that may open several
matches. A generated map scales mechanically and loses curation. The exact threshold is
an estimate, not a measurement.

## Outcome Metrics and Feedback Loops

### Per task

After each task that used this skill, record the nine-item Default Reliability Stack and,
for each recommendation, whether it shipped, was adapted, or was rejected.

- The ninth item is an honesty valve. Track the skip reasons. They show which gates are
  treated as noise.
- The metric saturates once all nine pass. Then sample the quality of the requirements
  instead.
- Counting citations such as `PY1-01` is cheap and easy to game. Treat it as a weak
  signal, not proof of improvement.
- If recording every task costs too much, sample merged Python changes against the
  anti-pattern table.
- Keep the two loops apart: the health of the guidance and the health of the code. A
  green CI badge does not show that the guidance is current.

### Per gate

- Record row-level hits and no-hits, stack pass or fail, prompt answers and exact command
  outcomes for every gated change.
- Automate the top recurring mechanical hit each quarter.
- Review aggregates by area of the codebase, not by person.
- A falling hit rate does not prove the gate is useless. It may mean the gate works. A
  row that never hits may mean the hazard is extinct or that nobody looks. Seeded-defect
  audits tell them apart.
- The second offence in one area is the strongest immediate signal for a lint rule or a
  fixture.
- Tracking escaped defects is sharper and slower.
- Expected hit rates are unknown until tracking begins.

### Per route

- Each record notes the matched or missed jump point, the fallback used, and the outcome
  of any provenance challenge. Review quarterly with the task mix.
- Each fallback is a backlog signal. It names a missing or weak jump point.
- Do not call a jump point useless because experienced people stopped consulting it.
  Inspect the task distribution.
- An agent wrapper can log automatically. People still need the habit.
- No baseline exists for expected fallback rates.

### Code-health metrics

Track: unparsed boundary escapes; unjustified `Any` crossings; adverse-input detection;
error-context preservation; cleanup and cancellation failures; import side effects;
fixture leakage; supported-version regressions; package-entry failures; gate bypasses.

- Raw counts of annotations or tests can rise while semantics weaken.
- Every metric needs scope, denominator, baseline, versions, expected behaviour, an
  adverse threshold, an owner, and the code, test or policy change it triggers.
- Exclude or label: generated code, third-party stubs, intentional adapters, expected
  cancellations, platform differences, duplicate signals.
- Do not game `Any` counts with casts, replace failure assertions with coverage, suppress
  warnings, or exclude flaky cancellation tests.
- At low volume use qualitative audits, sampled boundary modules, gate-failure counts, or
  a debt ledger with expiry criteria.
- Publish raw counts, exclusions, fixtures, failures, uncertainty, owner, and the trace
  from feedback to change.
- No repository baseline or incident data comes with this skill. Thresholds and any claim
  of causal improvement are local.

### Signals

- Leading indicator: the next agent can modify the package without weakening type, lint
  or fixture coverage.
- Failure signal: the guidance says quality matters and gives no migration path from
  loose scripts to strict package code.
- Refresh triggers: an edit to this skill's files; a change in public APIs,
  documentation or tool releases.

## Completeness Checklist

### For a change

Every item links to code, configuration, a test, command output, or an explicit
non-applicability. High-risk boundaries require adverse evidence.

- [ ] Runtime inputs are parsed.
- [ ] Dynamic types are contained before the core.
- [ ] Data defaults are deterministic.
- [ ] Behaviour seams exist where substitution or testing needs them.
- [ ] Expected and exceptional outcomes are distinguished.
- [ ] Every resource has an owner.
- [ ] Async control flow preserves cancellation and bounds waits.
- [ ] Imports are safe.
- [ ] Paths and encodings are explicit.
- [ ] Logs are diagnosable and free of secrets.
- [ ] Fixtures are isolated.
- [ ] Supported versions are unchanged, or changed on purpose.
- [ ] The established gates ran.

Full gates apply to reusable packages and services. A disposable script may document
justified reductions. Add the cancellation and packaging items only when they apply.

Failures of the checklist itself: ticks without locations; a checker pass standing in for
a runtime test; a happy-path test standing in for lifecycle coverage; unsupported
versions left implicit; tool setup mistaken for completion.

Audit trail: boundary map, type diagnostics, adverse fixtures, resource and cancellation
observations, isolated import, temp filesystem, log scan, metadata, Python matrix, build,
entry point, project gates. Completeness closes every relevant uncertainty and lifecycle
boundary. It does not mean every possible tool ran.

### For a recommendation

Reject any recommendation that lacks one of the four: mode; `PY1` identifier, guardrail
or section; applicability; a gate that can be run or reviewed. The pass bar is zero
missing attributes. A search for mode names and `PY1` identifiers near recommendation
verbs automates most of it.

Also confirm that the guidance in use has: a role scenario; the adopt, adapt, avoid
guide with the cost of error; a source hierarchy with a confidence warning; a concrete
artifact; good, bad and borderline examples; a leading indicator and a failure signal;
and an adjacent route. A new checklist item gets the same verification as a structural
one.

### For this skill's own content

At each reread or refresh, count and inspect:

| Item | Count |
| --- | ---: |
| Modes | 8 |
| `PY1` patterns | 15 |
| Anti-pattern rows, each with mechanism and replacement | 11 |
| Default Reliability Stack items, with the "verify" framing | 9 |
| Gate commands in the menu | 8 |
| Configuration discovery lines | 2 |
| Review prompts | 8 |
| Jump points | 8 |
| Use-order steps | 3 |
| Primary source links | 16 |
| Synthesis notes behind the source list | 3 |

- Counts alone miss semantic drift. Check the mechanisms, the replacements, the clauses,
  and the explicit-reason requirement for skipped gates.
- Spot-check three source links against the claims they are said to support. A dropped
  Pyright entry is the kind of loss this catches.
- A short comparison script can automate much of this. Re-auditing only when a checksum
  changes trades vigilance for effort, and a checksum alone misses meaning.
- Do not reject legitimate reorganisation. Audit presence and accuracy, not layout.
- The same rule appears in the guardrails, the anti-pattern table and the pattern
  sections. If the wording disagrees between them, a revision was left incomplete.
- Audit the files, not memory. Whether count-plus-clause auditing catches every
  meaningful drift is unproven.

When adding guidance to this skill:

- Write it so a reader reaches it from the "Using reference.md" tables in `SKILL.md` in
  one step, and can audit its basis in the Source Evidence Mapping Table in one lookup.
- When a section is added to this file, add it to those tables the same day. Good: a
  new section registered the day it lands. Bad: a new pattern justified by "it is well
  known" with no entry in the source table. Borderline: a Python convention backed only
  by the owner's Rust or TypeScript skill, which is disclosed and still cross-language.
- This discipline assumes the tables are current. A stale table sends readers to
  sections that no longer exist, and then the routing itself is the source of the
  misdirection. Run both heading checks (Verification Gate Command Set, "Checking this
  skill's own headings") at every refresh.
- The alternative to one central source table is inline citations inside each section.
  That is heavier to maintain and cannot drift apart from the sections it describes.
  Select it when sections are revised independently or the central table has stopped
  being kept up. Whether one central table stays maintained past a handful of reference
  files is unresolved.
- Whether the three-step use order stays sufficient as this file grows is untested.

## Adjacent Reference Routing

Check first whether mode selection answers the question. Route away only for the
dominant mechanism this skill does not own. Keep the general boundary and lifecycle
contracts when you do.

| Concern | Goes to |
| --- | --- |
| Web request lifecycles, framework architecture (Django, FastAPI, Flask) | the framework's primary documentation or a companion framework skill |
| Persistence and transactions | the database or ORM reference |
| Security threat models | security guidance |
| Distributed delivery, queues, cross-service concerns | distributed-systems guidance |
| Data-science pipelines and notebooks | data guidance |
| Deployment | deployment guidance |
| Numerical correctness, performance engineering, event-loop internals | the domain reference |
| Packaging build mechanics | packaging documentation; import safety stays here |
| Rust or TypeScript code | the sibling language skills |
| Requirement writing in general | [A03 Executable Specs](../../A03-Executable-Specs01.md) |
| Sizing the process to the task | [A01 LLM Workflow](../../A01-LLM-Workflow01.md) |
| Greenfield formatter or checker choice | out of scope; in a configured repository, discovery answers it |

Inside this skill:

| Question | Where |
| --- | --- |
| "Should I use ...?" (design) | the pattern sections in Theme Specific Artifact |
| "When should the skill apply?" | When to use and Modes in `SKILL.md` |
| "What blocks handoff?" | Quality gates in `SKILL.md` |
| "Which source backs this?" | Source Evidence Mapping Table |
| "Which section covers protocols?" | the routing table; what Python actually does is not a routing question |
| A tool flag | `--help` on the installed tool; external documentation is unverified until fetched |

Handoff packet: the unresolved question; the capability of the destination; Python and
dependency versions; the handoff boundary; the controls retained; the evidence to bring
back; conflicts; integration tests; owner; the return or stop decision.

Rules:

- Do not route by keyword. A destination that only shares words with the question is
  circular and useless.
- Confirm the destination exists and covers the concern.
- Do not load references indiscriminately.
- Do not let specialised advice silently weaken parsing or cleanup.
- Do not turn the bans into design advice.

Good: route a FastAPI lifecycle question and keep parsed domain values and cancellation
tests. Bad: use general typing rules for transaction retries.

## Source Evidence Mapping Table

### What the skill is built from

The owner's Python reliability skill was prepared on 2026-06-23 from primary Python,
packaging and tool documentation, and it follows the shape of the owner's Rust and
TypeScript coder skills. It has one author and one date. It is internally coherent and
not independently corroborated.

| Content | Basis | Status |
| --- | --- | --- |
| Modes, workflow, output order, guardrails | the owner's skill | owner's rules, reproduced |
| `PY1` patterns, scores, code examples for `ImportReport` and `run_job` | the owner's reliability reference | owner's rules, reproduced |
| Eleven anti-patterns, nine-item stack, gate commands, discovery commands, review prompts | the owner's quality-gates reference | owner's rules, reproduced |
| Use order and jump points | the owner's reference map | owner's rules, adapted to these two files |
| Gate tiers, gate card, drills, escalation limits, record schemas, routing card, retry caps, cadences, scale seams, volatility ordering | constructed operating guidance | inference, not the owner's base requirements |
| Additional code templates and tests in `SKILL.md` and here | written for this skill | exercised on Python 3.12 with pytest 9.2.0, mypy 2.4.1 in strict mode, and Ruff 0.17.6 |

### Primary sources the owner listed

None of these pages was retrieved for this file. They show what informed the guidance on
2026-06-23. They do not show that the links still resolve or that current behaviour
matches.

| Source | Supports |
| --- | --- |
| [PEP 8, Style Guide for Python Code](https://peps.python.org/pep-0008/) | baseline style |
| [PEP 484, Type Hints](https://peps.python.org/pep-0484/) | typing rules (`PY1-02`, `PY1-04`) |
| [Python asyncio tasks](https://docs.python.org/3/library/asyncio-task.html) | cancellation, `TaskGroup`, timeouts (`PY1-07`) |
| [Python contextlib](https://docs.python.org/3/library/contextlib.html) | context managers (`PY1-06`) |
| [Python dataclasses](https://docs.python.org/3/library/dataclasses.html) | dataclass rules (`PY1-03`) |
| [Python built-in exceptions](https://docs.python.org/3/library/exceptions.html) | exception rules (`PY1-05`) |
| [Python unittest](https://docs.python.org/3/library/unittest.html) | unittest strategy (`PY1-11`) |
| [Python packaging guide for pyproject.toml](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/) | packaging metadata (`PY1-12`) |
| [pytest fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html) | fixtures (`PY1-11`) |
| [pytest good practices](https://docs.pytest.org/en/stable/explanation/goodpractices.html) | test layout and invocation |
| [mypy documentation](https://mypy.readthedocs.io/) | mypy gate and configuration |
| [Pyright documentation](https://microsoft.github.io/pyright/) | pyright gate |
| [Ruff documentation](https://docs.astral.sh/ruff/) | lint gate |
| [Ruff formatter](https://docs.astral.sh/ruff/formatter/) | format gate |
| [Black documentation](https://black.readthedocs.io/) | format gate |
| [Typing dataclasses specification](https://typing.python.org/en/latest/spec/dataclasses.html) | how type checkers treat dataclasses |

Two more candidate entry points, also not retrieved: the
[typing module documentation](https://docs.python.org/3/library/typing.html) and the
[pytest documentation root](https://docs.pytest.org/en/stable/).

How the groups divide:

- Official Python documentation supports the exception, context manager, dataclass,
  unittest and asyncio cancellation guidance.
- Packaging and tool documentation supports the `pyproject.toml`, ruff, black, mypy,
  pyright and pytest gate recommendations.
- The skill stays generic and repository-preserving. Framework-specific web, data-science
  and deployment doctrine belongs in companion skills.

A disputed claim therefore needs only its own group refreshed.

### Matching a claim to an authority

| Claim about | Authority |
| --- | --- |
| Cross-cutting priorities | this skill |
| Language and typing semantics | Python documentation |
| pytest behaviour | pytest documentation, only when pytest is the project's stack |
| Checker behaviour | the documentation of the checker in use; do not generalise mypy to pyright |
| Lint and format behaviour | the documentation of the tool in use |
| Local truth | the repository's configuration, CI, tests and runtime results |

- Tool documentation governs the tool's interface. It does not govern runtime
  validation, whether the repository should adopt the tool, or compatibility with other
  tools.
- Checker documentation cannot validate runtime input. A test framework does not define
  typing semantics. Generic guidance cannot override supported Python versions or CI.
- Do not universalise one row. Do not use tool documentation as application policy. Do
  not assume a listed command is installed. Do not count links as corroboration. Do not
  substitute a source's title for its constraints.
- A long bibliography can create false confidence. Do not justify a Python convention
  with a precedent from another language or with "well known".
- When evidence falls short: downgrade to provisional guidance, preserve the existing
  tooling, build a runtime fixture, inspect the installed tool's help, or use the
  framework's primary documentation.
- Record: source class, version and date, repository configuration, installed command,
  runtime fixture, contradiction, the authority selected, and the effect on the guidance.
- For an external claim also record: URL, retrieval status, Python and tool versions,
  lock and configuration files, the CI command, a minimal checker fixture, its runtime
  counterpart, conflicts, the adoption decision, and the migration path.
- Watch for: typing features that differ by Python version, pytest plugins, mypy modes,
  rule and formatter drift in Ruff, two formatters owning the same files, CI wrappers. A
  migration needs compatibility, overlap, rollout and rollback evidence.

## Evidence Boundary Notes

### Labels

| Label | Meaning |
| --- | --- |
| `local_corpus_sourced_fact` | tied directly to the owner's skill: its table rows, stack items, commands, prompts and patterns can be re-checked |
| `external_research_sourced_fact` | tied to a public URL, and only after retrieval; an unretrieved URL is a candidate, not evidence |
| `combined_evidence_inference_note` | synthesis that combines the two into guidance; label it as inference |

Add further classes as needed: repository contract, current primary source, static
analysis, runtime fixture, package artifact, operational observation, provisional
inference, conflict, negative evidence.

Check the label before reusing a claim. Reuse enumerations with a citation to their
heading. Carry the reasoning along with anything constructed. Do not present quarterly
drills or tiering as the owner's base requirements. The explicitness thesis, however
sound, is inference. The cancellation rule with `PY1-07` is locally sourced.

### Rules

- An atomic claim cites exact evidence and version. A combined claim lists its
  prerequisites. Negative evidence names what it covered. Conflicts stay visible.
  Uncertainty must change the action.
- Configured is not executed. Checked is not validated. Tested is not packaged. Packaged
  is not deployed. Observed once is not invariant.
- Confidence is compositional. Say which boundary, checker, fixture, package or
  operational premise would change the guidance if it turned out false.
- The source list is disclosure, not verification. Quoting it accurately proves what the
  author listed, never that the pages were correct.
- The date scopes the authority. A source list from 2026-06-23 cannot prove later edits
  or current external facts. Newer documentation may target a newer CPython than the
  repository supports.
- Volatility differs by group. PEP and standard-library pages are comparatively stable.
  Packaging guidance drifts slowly. Tool documentation drifts fastest. This ordering is
  itself an inference.
- For current tool behaviour prefer the repository's pinned versions and changelogs. A
  claim about current behaviour needs a dated retrieval of the specific page, or evidence
  from the repository.
- The commands in the menu are the owner's forms as written. Which have drifted since
  2026-06-23 is unknown.
- Classify sources as canonical, supporting, legacy, duplicate or conflicting. With one
  author behind all of it, seek an adjacent source before treating a rule as settled
  policy.
- Authority inside the skill: the gates decide what blocks handoff; the pattern sections
  explain why and how to fix; the guardrail summary never overrides either. A specific
  `PY1` section beats a summary of it.

### Evidence chains

Good: the pattern motivates parsing; current documentation defines the syntax; the
project configuration establishes the target; a runtime fixture rejects malformed input;
a package test bounds the support claim. Bad: infer reliability from mypy alone.
Borderline: report package success on one platform with the other matrix cells pending.

To audit: sample recommendations; trace each clause to its class and location; confirm
versions and configuration; replay fixtures and builds; inspect prerequisites; keep
conflicts and negative evidence; decline or narrow a recommendation when it is
falsified.

### What is not known

- No repository baseline, incident data or hit history accompanies this skill.
- The pattern scores and the method-pattern scores have no empirical calibration.
- No timing in this file is measured: routing time, gate time, the ten-minute hypothesis.
- The thresholds in Reliability Target are proposals.
- Framework behaviour, checker options and version-specific APIs need current evidence
  from the project.
- The code examples were exercised on one interpreter version and one platform. Other
  versions are pending.
- Exploratory notebooks are not addressed.

## Future Refresh Search Queries

Search only after a documented drift signal in the language, a checker, a test tool, a
linter, packaging or compatibility. A search finds candidates. Targets, installed tools,
configuration and behaviour tests decide adoption.

### Order

Order probes by how fast the subject ages: tools first, standard-library features
second, PEP conventions last. Fetching the handful of tool pages covers most realistic
staleness. If a newer version of the owner's source list exists, compare against it
before fetching every page again.

### Probes

Include the exact mechanism and the versions. Prefer primary, versioned sources.

- `ruff <installed version> changelog rule <code>` for each lint-backed anti-pattern row.
  A new autofix changes the enforcement class of a row, not whether the row exists.
- `ruff format black compatibility <version>` when a repository runs both.
- `mypy <version> release notes strict` and `pyright <version> configuration strict`
  for checker options.
- `pytest <version> changelog fixtures` and invocation changes.
- `python <version> whatsnew asyncio TaskGroup timeout CancelledError`.
- `python <version> whatsnew typing dataclasses slots`.
- `python <version> default encoding EncodingWarning` for the explicit-encoding rule.
- `packaging.python.org pyproject.toml requires-python project.scripts` for packaging
  metadata.
- One new hazard per major Python release: is there a new pitfall that deserves a row?
- Order per-row probes by the repository's own hit rate, once one exists.

### Low-value fallbacks

These generic forms mostly find listings. Use them only when a targeted probe finds
nothing. Substitute the topic: `python reliability reference patterns`,
`python quality antipattern gates`, `python reference routing sources` or
`python language skill entrypoint`.

- `<topic> official documentation best practices`
- `<topic> GitHub repository examples`
- `<topic> changelog release notes migration`

### Rules

- Do not treat a snippet as semantics, the latest documentation as an override, a popular
  repository as policy, an absent result as a deprecation, or browsing as validation.
- A newer feature is not automatically a deprecation. Test whether the claim is
  superseded.
- Chase redirects and site reorganisations before marking a link dead.
- Inspect installed help, metadata, lock files, release artifacts and minimal fixtures.
  Reproduce the behaviour in the repository or in a minimal fixture.
- Keep uncertain guidance provisional. Update or caveat every claim whose pinned surface
  moved.
- Record: trigger, query, date, owner, Python and tool versions, an archived copy or
  hash, the claim, configuration, fixture result, conflict, the accepted change, the
  migration and rollback, reviewer, and the next trigger. For each probe note which row
  or command it confirmed or changed.
- Re-fetching the sixteen primary links and comparing claims is a bounded staleness
  audit. Subscribing to release notes is steadier and costs more.
- Check the headings named in `SKILL.md` against this file at every refresh, and check
  the top-level sections of this file against `SKILL.md`, so that a renamed section and
  an unregistered one are both caught.
