---
name: kotlin-coder-01
description: Reliability-first Kotlin skill for implementing, refactoring, or reviewing Kotlin libraries, CLIs, JVM modules, shared domain code, coroutine code, and Java interop boundaries. Use when work needs null-safety discipline, value and sealed types, idiomatic scope-function use, typed errors, structured concurrency, testing, or JVM quality gates.
---

# Kotlin Reliability

## Overview

Use this skill when the task is primarily about writing, refactoring, or reviewing reliable Kotlin across libraries, JVM modules, CLIs, shared domain code, and coroutine-heavy flows. Bias toward Kotlin that makes invalid states harder to express, keeps Java interop boundaries explicit, and treats cancellation, nullability, and testability as correctness concerns.

For Spring Boot, Ktor, persistence, service runtime, or production backend delivery, combine this skill with `kotlin-backend-delivery-01`. Use this skill as the generic language reliability baseline.

## When To Use

- `.kt`, `.kts`, Gradle Kotlin DSL, or Kotlin/JVM module work where correctness matters more than style.
- Domain models, public APIs, Java interop, serialization boundaries, coroutines, flows, CLIs, or shared library contracts.
- Refactors that need clearer nullability, better type boundaries, safer error modeling, or less Java-shaped Kotlin.
- Code reviews where the real question is whether the Kotlin will stay safe and readable under malformed input, cancellation, API evolution, or mixed Java/Kotlin calls.

## Mode Selection

Choose one or more modes before planning or coding:

- `Core Kotlin Mode`: domain types, functions, collections, extension functions, visibility, packages, naming, and coding conventions.
- `Nullability Mode`: nullable modeling, platform type containment, `!!` removal, Java annotations, and absent-value semantics.
- `Type Boundary Mode`: value classes, sealed hierarchies, enums, data classes, immutable DTOs, and parse-don't-validate boundaries.
- `Coroutine Mode`: suspend APIs, Flow, cancellation, dispatcher choice, timeout behavior, and blocking-call isolation.
- `Interop Mode`: Java callers, Java libraries, platform types, checked exceptions, overloads, SAM adapters, and binary compatibility.
- `Testing Mode`: unit tests, coroutine tests, property or contract tests, fixtures, and behavior-first coverage.
- `Review Mode`: anti-pattern scan, API stability, quality gates, and risk-focused findings.

## Workflow

1. Classify the Kotlin surface.
- Name the surface first: library API, domain module, CLI, Gradle script, coroutine workflow, Java interop adapter, serialization boundary, or review pass.
- State whether the main risk is nullability, API misuse, platform types, cancellation, blocking IO, mutation, or test gaps.

2. Write executable requirements when behavior is unclear.
- Use `REQ-KOTLIN-<NNN>.<REV>` identifiers.
- Express behavior as `WHEN...THEN...SHALL`.
- Replace vague words such as "idiomatic", "safe", "clean", or "fast" with observable behavior or quality gates.

3. Load references progressively.
- Read [Reference map](./references/reference-map.md) first.
- Open the relevant sections in [Kotlin reliability reference](./references/kotlin-reliability-reference.md).
- Finish with [Kotlin quality gates and anti-patterns](./references/kotlin-quality-gates-and-anti-patterns.md).

4. Design boundaries before implementation.
- Keep raw inputs at the edge until parsed into domain types.
- Prefer non-null types, immutable values, value classes for meaningful primitives, and sealed results for closed outcome sets.
- Preserve Kotlin/JVM target, compiler version, build tool, and existing static-analysis tools unless migration is requested.

5. Treat coroutines as correctness-sensitive.
- Preserve structured concurrency and cancellation propagation.
- Avoid `GlobalScope` for request, command, or user-visible work.
- Keep blocking calls out of coroutine dispatchers unless isolated deliberately.
- Do not swallow `CancellationException`.

6. Verify with the smallest gate that proves the claim.
- Use focused tests for pure logic and real boundary tests for serialization, interop, coroutine cancellation, or persistence-like behavior.
- Prefer repository wrappers: `./gradlew test`, `./gradlew build`, `./gradlew ktlintCheck`, `./gradlew detekt`, or Maven equivalents if present.

## Output Expectations

Return results in this order when planning or reviewing:

1. `Kotlin Work Mode`
2. `Executable Requirements`
3. `Type And Boundary Design`
4. `Coroutine/Interop Constraints`
5. `Verification Matrix`
6. `Implementation Plan`
7. `Quality Gates`
8. `Open Questions`

Use this traceability shape when requirements exist:

| req_id | test_id | test_type | assertion | target |
| --- | --- | --- | --- | --- |

## Guardrails

- Do not use this skill as a replacement for backend-specific framework guidance when Spring Boot, Ktor, databases, migrations, auth, or operations are central.
- Do not introduce `!!`, `lateinit`, mutable global state, or platform type leaks without a narrow justification and test coverage.
- Do not use scope functions merely to appear idiomatic; prefer the form that keeps receiver and return value obvious.
- Do not hide expected business failures in generic exceptions when a sealed outcome or typed error would make callers safer.
- Do not convert Java-style nullable, mutable, inheritance-heavy designs into Kotlin syntax without improving the boundary model.

## References

- [Reference map](./references/reference-map.md)
- [Kotlin reliability reference](./references/kotlin-reliability-reference.md)
- [Kotlin quality gates and anti-patterns](./references/kotlin-quality-gates-and-anti-patterns.md)
- [Sources and research brief](./references/sources-and-research-brief.md)
