# Kotlin Quality Gates And Anti-Patterns

## High-Value Anti-Patterns

| Anti-pattern | Why it fails | Prefer |
| --- | --- | --- |
| `!!` in production paths | Converts uncertain input into crashes far from the boundary | Parse once, return typed failure, or keep `T?` explicit |
| Platform types in domain code | Java nullability uncertainty becomes invisible | Adapter-level normalization |
| `GlobalScope` for real work | Work outlives caller and loses cancellation/error ownership | Caller-owned scopes, `coroutineScope`, lifecycle scopes |
| Catching `Exception` around suspend work without rethrowing cancellation | Breaks cooperative cancellation | Catch `CancellationException` first and rethrow |
| Nested `let`/`also`/`apply` chains | Receiver and return value become unclear | Named locals or a simpler function |
| Nullable fields for every domain state | Conflates absent, invalid, forbidden, and unknown | Sealed outcomes or typed value objects |
| Data classes for identity-heavy objects | Equality/copy/destructuring can violate lifecycle expectations | Plain classes or framework-specific models |
| Hidden blocking inside `suspend` | Starves dispatchers and misleads callers | Isolate with dispatcher or keep blocking API explicit |
| Boolean result flags | Callers forget what `true` and `false` mean | Named sealed outcomes or enums |
| Mutable global singletons | Tests leak state and concurrency bugs hide | Constructor injection or scoped state |

## Default Reliability Stack

Before finishing Kotlin work, verify:

1. Boundary inputs are parsed or normalized before domain logic.
2. Domain types are non-null unless absence is meaningful.
3. No new `!!`, broad `lateinit`, or platform-type leakage exists.
4. Expected failures are modeled with typed outcomes or typed exceptions.
5. Coroutine code preserves structured concurrency and cancellation.
6. Blocking calls are isolated or intentionally exposed as blocking.
7. Tests cover the highest-risk behavior, not only the happy path.
8. Existing build, format, lint, and static-analysis gates were run or explicitly skipped with a reason.

## Quality Gate Commands

Use the commands the repo already uses. Prefer wrappers over globally installed tools.

```bash
./gradlew test
./gradlew build
./gradlew ktlintCheck
./gradlew detekt
./mvnw test
./mvnw verify
```

When a command is absent, inspect the build files before inventing a new toolchain:

```bash
rg --files -g 'build.gradle*' -g 'settings.gradle*' -g 'pom.xml'
rg 'ktlint|detekt|kotest|junit|mockk|turbine|kotlinx-coroutines-test' .
```

## Review Pass

Use this compact pass before handoff:

- `Nullability`: Are nullable values introduced only where absence is real?
- `Interop`: Are Java platform types contained?
- `Types`: Are primitive IDs, units, and closed states made explicit?
- `Coroutines`: Does cancellation propagate and blocking stay named?
- `Tests`: Does the test suite prove malformed input, cancellation, and boundary behavior?
- `Gates`: Are repo-native tests and static checks run?
