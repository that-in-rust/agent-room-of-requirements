# Kotlin Reliability Reference

## Premise

Reliable Kotlin comes from making ambiguity visible at the boundary and keeping the core small, non-null, typed, and cancellation-aware. Kotlin's ergonomics are powerful, but they can also hide Java platform types, receiver confusion, coroutine leaks, and mutable domain models if used casually.

This reference is not a tutorial. It is a reliability checklist for LLM-authored Kotlin work.

## Pattern Scoreboard

| ID | Score | Pattern |
| --- | ---: | --- |
| `KC1-01` | 98 | Contain platform types at Java boundaries |
| `KC1-02` | 96 | Prefer non-null domain types and explicit absence |
| `KC1-03` | 94 | Use value classes for meaningful primitive identifiers |
| `KC1-04` | 93 | Use sealed outcomes for closed result and state spaces |
| `KC1-05` | 91 | Keep data classes for value data, not lifecycle-heavy entities |
| `KC1-06` | 90 | Prefer immutable collections and constructor-injected state |
| `KC1-07` | 90 | Parse raw inputs once before domain logic |
| `KC1-08` | 89 | Use scope functions only when receiver and return semantics stay obvious |
| `KC1-09` | 95 | Preserve structured concurrency and cancellation propagation |
| `KC1-10` | 94 | Do not swallow `CancellationException` |
| `KC1-11` | 91 | Isolate blocking calls from coroutine dispatchers |
| `KC1-12` | 88 | Make Java interop contracts explicit with annotations and overload choices |
| `KC1-13` | 87 | Use focused extension functions at stable ownership boundaries |
| `KC1-14` | 86 | Keep public API growth binary- and source-compatible where possible |
| `KC1-15` | 85 | Test cancellation, nullability, and serialization boundaries directly |

## 1. Kotlin API And Type Design

### `KC1-03` Use value classes for meaningful primitive identifiers

Use value classes when a primitive carries domain meaning:

```kotlin
@JvmInline
value class UserId(val value: String)
```

Prefer this for IDs, keys, units, offsets, and validated strings. It prevents accidentally passing a raw `String` or the wrong ID type through a large call chain.

Keep value classes small and invariant-bearing. If the constructor cannot enforce the invariant directly, expose a factory such as `parse` or `from`.

### `KC1-04` Use sealed outcomes for closed result and state spaces

Use sealed classes or sealed interfaces when the caller must handle a known set of outcomes:

```kotlin
sealed interface PaymentDecision {
    data class Approved(val authorizationId: String) : PaymentDecision
    data class Declined(val reason: DeclineReason) : PaymentDecision
    data object RequiresReview : PaymentDecision
}
```

Prefer sealed outcomes over booleans, sentinel strings, or exception-only business flow. This gives exhaustiveness checks in `when` expressions and makes new states visible during refactors.

### `KC1-05` Keep data classes for value data

Use data classes for immutable values, DTOs, events, and pure state snapshots. Avoid treating data classes as the default for objects with identity, lifecycle hooks, lazy loading, or mutable behavior.

Good defaults:

- Constructor parameters express required state.
- Properties are `val` unless mutation is part of the invariant.
- Copy semantics are safe for the domain.
- Equality is value equality, not identity or persistence identity.

### `KC1-07` Parse raw inputs once before domain logic

At boundaries, turn strings, maps, JSON, CLI args, environment values, or Java objects into typed Kotlin values before business logic runs. Keep parse errors close to the boundary and domain logic close to non-null validated types.

## 2. Nullability And Java Interop

### `KC1-01` Contain platform types at Java boundaries

Java interop can expose platform types whose nullability Kotlin cannot prove. Do not let platform types flow into the domain core.

Boundary rules:

- Convert Java return values into nullable or non-null Kotlin types immediately.
- Prefer Java APIs with nullability annotations when available.
- Wrap uncertain values with explicit checks and typed failure messages.
- Avoid assigning platform types directly to non-null domain fields without validation.

### `KC1-02` Prefer non-null domain types and explicit absence

Use `T?` only when absence is a real domain state. If absence means "not loaded", "forbidden", "invalid", "not found", or "not yet computed", model the distinction directly with a sealed type or result.

Avoid:

- `String?` for every field because the source is nullable.
- `!!` as a migration shortcut.
- `lateinit` for required dependencies outside lifecycle-managed frameworks.

### `KC1-12` Make Java interop contracts explicit

When Kotlin APIs are called from Java, check names, nullability, overloads, default parameters, exceptions, and binary compatibility. Consider `@JvmName`, `@JvmOverloads`, or explicit facade functions when they make Java call sites safer.

Do not optimize only for Kotlin call sites if Java is a supported consumer.

## 3. Coroutines And Flow Reliability

### `KC1-09` Preserve structured concurrency and cancellation propagation

Keep work tied to a caller-owned scope. Prefer `coroutineScope`, `supervisorScope` when independent child failure is intentional, and explicit lifecycle scopes supplied by the application.

Avoid `GlobalScope` for request, command, job, or user-visible work. It disconnects work from the caller's cancellation and error handling.

### `KC1-10` Do not swallow `CancellationException`

Cancellation is cooperative. Broad catches must rethrow cancellation:

```kotlin
try {
    runWork()
} catch (error: CancellationException) {
    throw error
} catch (error: Exception) {
    recordFailure(error)
}
```

Any retry, logging, or error-normalization layer around suspend work must preserve cancellation.

### `KC1-11` Isolate blocking calls from coroutine dispatchers

Name blocking calls honestly. File IO, JDBC, legacy SDK calls, and CPU-heavy operations should use an appropriate dispatcher or remain in an intentionally blocking API.

Do not label a function `suspend` if it only hides blocking work without isolation or operational tradeoff.

## 4. Testing And Fixtures

Test the risk, not the syntax.

High-value tests:

- Nullability and platform-type boundaries using Java fakes or adapter tests.
- Sealed outcome exhaustiveness through behavior tests.
- Value-class parse and round-trip tests.
- Coroutine cancellation tests and timeout behavior.
- Serialization compatibility tests when external contracts exist.
- Property tests for parsers, validators, and reversible transforms when the repo has a property-test stack.

Keep fixtures explicit and small. Prefer builders only when they prevent irrelevant noise without hiding required fields.

## 5. Tooling And Build Gates

Prefer repository-native gates:

- `./gradlew test`
- `./gradlew build`
- `./gradlew ktlintCheck`
- `./gradlew detekt`
- `./mvnw test`
- `./mvnw verify`

Preserve existing Kotlin version, JVM target, Gradle/Maven style, and static-analysis baseline unless the task explicitly includes changing them.

## Kotlin Review Questions

- Does any platform type escape past an adapter?
- Could `!!` fail in production from malformed or old data?
- Are business outcomes modeled as data instead of log messages or generic exceptions?
- Does cancellation propagate through every suspend boundary?
- Is a scope function hiding which object is being read or returned?
- Are tests proving nullability, cancellation, parse errors, and interop behavior where those are the risks?
