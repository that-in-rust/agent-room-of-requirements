# Bug Discovery as Quality Signal

How cross-referencing our MongoDB sink against the existing Postgres sink
revealed a real bug — and why fixing it before submission is the strongest
possible quality signal for the PR.

---

## The Discovery

**Trigger:** Reading `core/connectors/sinks/postgres_sink/src/lib.rs` lines
503-517 during PR preparation review. The Postgres sink has:

```rust
fn is_transient_error(e: &sqlx::Error) -> bool {
    match e {
        sqlx::Error::Io(_) => true,
        sqlx::Error::PoolTimedOut => true,
        sqlx::Error::Database(db_err) => {
            let code = db_err.code().unwrap_or_default();
            matches!(code.as_ref(), "40001" | "40P01" | "53300" | "57P03")
        }
        _ => false,
    }
}
```

**Our MongoDB sink had:** No `is_transient_error` function. The retry loop
retried ALL errors:

```rust
// Before fix:
if attempts >= max_retries {
    return Err(e.into());  // only stops on max retries
}
warn!("Transient database error...");  // LIE: not checking if transient
```

This means auth failures, duplicate key errors (11000), and schema
validation errors (121) would all be retried 3 times with delays — wasting
time and logging misleading "transient" messages.

---

## The Fix

Added typed `ErrorKind` matching for MongoDB:

```rust
fn is_transient_error(e: &mongodb::error::Error) -> bool {
    if e.contains_label(RETRYABLE_WRITE_ERROR) { return true; }
    match e.kind.as_ref() {
        ErrorKind::Io(_) => true,
        ErrorKind::ConnectionPoolCleared { .. } => true,
        ErrorKind::ServerSelection { .. } => true,
        ErrorKind::Authentication { .. } => false,           // permanent
        ErrorKind::InsertMany(err) => {
            !err.write_errors.as_ref()
                .is_some_and(|wes| wes.iter().any(|we| matches!(we.code, 11000 | 13 | 121)))
        }
        ErrorKind::Command(cmd) => !matches!(cmd.code, 11000 | 13 | 121),
        _ => { /* fallback: string matching for timeout/network/pool */ }
    }
}
```

Updated retry guard:

```rust
// After fix:
if !is_transient_error(&e) || attempts >= max_retries {
    return Err(e.into());  // stops immediately on non-transient
}
```

Added 6 unit tests covering both transient (IO timeout, network, pool
exhaustion, server selection timeout) and non-transient (auth failure,
duplicate key) cases.

---

## Industry Validation

| System | Behavior | Assessment |
|--------|----------|------------|
| **Debezium** | Retries ALL errors (infinite by default) | Same bug, worse |
| **MongoDB Kafka Connector** | Removed app-level retries in v1.7 | Solved by elimination |
| **Flink MongoDB** | No retry, relies on driver | Different approach |
| **Our fix** | Typed ErrorKind matching | Matches Postgres sink pattern |

Debezium having the same bug validates that this is a real issue, not
pedantry. MongoDB Kafka Connector solving it by removing retries entirely
validates that the error classification is genuinely hard.

---

## Why This Matters for the PR

1. **Shows we read the existing codebase.** We didn't write in isolation —
   we cross-referenced against the Postgres sink and found a gap.

2. **Shows we understand the domain.** The error code table (11000, 13, 121)
   shows MongoDB-specific knowledge, not generic "retry on error."

3. **Shows we do homework.** Industry comparison with Debezium/Kafka/Flink
   is research a drive-by PR doesn't do.

4. **Shows we improve, not just copy.** The source connector had a
   string-based `is_transient_error`. We added typed ErrorKind matching
   to the sink, which is strictly better.

---

## The Method

**Cross-reference review:** For every non-trivial function, find its
equivalent in another connector in the same codebase. Diff the approaches.
If they handle something you don't, you have a bug. If you handle something
they don't, validate against industry implementations before assuming it's
an improvement.

**The search pattern:**

```
grep -r "is_transient\|retry\|transient" core/connectors/
```

Find every retry-related function. Read each one. Compare error handling
strategies. The bugs live in the gaps between implementations.
