# Python Quality Gates And Anti-Patterns

## High-Value Anti-Patterns

| Anti-pattern | Why it fails | Prefer |
| --- | --- | --- |
| Mutable default arguments | State leaks across calls | `None` sentinel or `default_factory` |
| Bare `except:` | Catches cancellation, interrupts, and hides root cause | Catch specific exceptions |
| Swallowing `asyncio.CancelledError` | Breaks cooperative cancellation | Cleanup, then re-raise |
| Uncontained `Any` | Disables useful type checking downstream | Narrow at boundary |
| `assert` for external validation | Can be optimized away and gives poor diagnostics | Explicit validation and typed errors |
| Import-time network or filesystem mutation | Imports become slow, flaky, and unsafe | Move side effects behind functions or CLI entry points |
| `print` in library behavior | Hard to route, test, and filter | `logging` or returned diagnostics |
| Manual open/close | Leaks resources on exceptions | `with` or `async with` |
| Stringly path handling | OS and relative-path bugs hide | `pathlib.Path` |
| Blocking calls in async functions | Event loop stalls under load | Synchronous API or executor isolation |
| Broad exception-to-`None` conversion | Callers lose cause and remediation | Typed result or contextual exception |

## Default Reliability Stack

Before finishing Python work, verify:

1. Untrusted data is parsed or validated at the boundary.
2. Public functions and important internal seams have useful type hints.
3. `Any` is contained, justified, and narrowed quickly.
4. Mutable defaults are absent.
5. Resources are managed with context managers or explicit cleanup.
6. Async cancellation is preserved.
7. Import-time side effects are not added to reusable modules.
8. Tests cover errors, cleanup, and boundary behavior.
9. Formatter, linter, type checker, and test gates were run or skipped with an explicit reason.

## Quality Gate Commands

Use the commands the repo already uses. Prefer `python -m ...` forms when they avoid path ambiguity.

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

When command choice is unclear, inspect configuration first:

```bash
rg --files -g 'pyproject.toml' -g 'setup.cfg' -g 'setup.py' -g 'tox.ini' -g 'noxfile.py' -g 'requirements*.txt'
rg 'pytest|unittest|ruff|black|mypy|pyright|coverage|tox|nox' .
```

## Review Pass

Use this compact pass before handoff:

- `Input`: Are external values parsed before domain logic?
- `Types`: Are annotations precise enough to catch misuse?
- `Errors`: Are expected failures visible and actionable?
- `Resources`: Are acquired resources closed on every path?
- `Async`: Does cancellation propagate?
- `Imports`: Can importing the module run safely and quickly?
- `Tests`: Do tests prove malformed input, cleanup, and edge behavior?
- `Gates`: Are repo-native tests and checks run?
