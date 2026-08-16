# Reference Map

Use this file to route quickly before loading the full Kotlin references.

## Jump Points

- `Pattern Scoreboard`: fast triage of the highest-value reliability patterns.
- `1. Kotlin API And Type Design`: value classes, sealed outcomes, data classes, visibility, and extension boundaries.
- `2. Nullability And Java Interop`: nullable modeling, platform types, annotations, overloads, and binary compatibility.
- `3. Coroutines And Flow Reliability`: structured concurrency, cancellation, dispatcher choice, timeouts, and blocking isolation.
- `4. Testing And Fixtures`: unit tests, coroutine tests, property tests, interop tests, and test readability.
- `5. Tooling And Build Gates`: Gradle/Maven wrappers, compiler warnings, ktlint, detekt, dependency checks, and CI.
- `High-Value Anti-Patterns`: mistakes to reject before finishing.
- `Default Reliability Stack`: compact final checklist.

## Section Search

- `rg '^##|^###' references/kotlin-reliability-reference.md`
- `rg '^##|^###' references/kotlin-quality-gates-and-anti-patterns.md`
- `rg 'Pattern Scoreboard|High-Value Anti-Patterns|Default Reliability Stack' references/*.md`

## Use Order

1. Read `Pattern Scoreboard`.
2. Open only the sections that match the boundary being touched.
3. Finish with `High-Value Anti-Patterns` and `Default Reliability Stack`.
