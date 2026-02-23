# MongoDB Sink Connector: Blind Retry Bug Analysis

## Status: RESOLVED (2026-02-23)

Fixed in `mongodb_sink/src/lib.rs`. Added typed `is_transient_error(&mongodb::error::Error)` matching on `ErrorKind` variants + string fallback. 6 new unit tests. All 66 tests passing (25 sink + 33 source + 8 E2E). Live demo verified with rebuilt binary.

**Date:** 2026-02-22
**Status:** FIXED — implementation complete by rust-coder-01, all 25 sink unit tests passing
**Severity:** High — production data pipeline can spin indefinitely on permanent failures

---

## Table of Contents

1. [The Bug: Precise Specification](#1-the-bug-precise-specification)
2. [The Fix: What Exactly Needs to Change](#2-the-fix-what-exactly-needs-to-change)
3. [Rubber Duck Debug: How Did This Happen](#3-rubber-duck-debug-how-did-this-happen)
4. [Industry Research: Kafka/Debezium MongoDB Connectors](#4-industry-research-kafkadebezium-mongodb-connectors)
5. [Lessons](#5-lessons)

---

## 1. The Bug: Precise Specification

### Location

File: `core/connectors/sinks/mongodb_sink/src/lib.rs`
Function: `insert_batch_with_retry`, lines 343-372

### The Broken Code

```rust
// lines 343-372 — mongodb_sink/src/lib.rs
async fn insert_batch_with_retry(
    &self,
    collection: &Collection<mongodb::bson::Document>,
    docs: &[mongodb::bson::Document],
) -> Result<(), Error> {
    let max_retries = self.get_max_retries();
    let retry_delay = self.retry_delay;
    let mut attempts = 0u32;

    loop {
        let result = collection.insert_many(docs.to_vec()).await;

        match result {
            Ok(_) => return Ok(()),
            Err(e) => {
                attempts += 1;
                if attempts >= max_retries {
                    error!("Batch insert failed after {attempts} attempts: {e}");
                    return Err(Error::CannotStoreData(format!(
                        "Batch insert failed after {attempts} attempts: {e}"
                    )));
                }
                warn!(
                    // This message is a lie: it says "Transient" but has not checked
                    "Transient database error (attempt {attempts}/{max_retries}): {e}. Retrying..."
                );
                tokio::time::sleep(retry_delay * attempts).await;
            }
        }
    }
}
```

### What the Bug Does

On ANY error from `collection.insert_many()`, the connector retries up to `max_retries` (default: 3) times with exponential back-off. The code even logs the word "Transient" in the warning — but it has never checked whether the error is transient.

Errors that are permanent and will NEVER succeed on retry:

| Error | MongoDB error code | Why retrying is wrong |
|---|---|---|
| Authentication failure | 18 (AuthenticationFailed) | Wrong credentials. Retry wastes time and may trigger rate-limiting or account lockout. |
| Authorization failure | 13 (Unauthorized) | Database user lacks `insert` privilege. Will not self-heal. |
| Duplicate key violation | 11000 (DuplicateKey) | The document's `_id` already exists. The exact same document will produce the exact same error. |
| BSON encoding violation | various | The document is structurally invalid for MongoDB. Resending it is futile. |
| Schema validation failure | 121 (DocumentValidationFailure) | The collection has a JSON schema validator and this document will never pass. |
| Collection does not exist (with strict mode) | 26 (NamespaceNotFound) | Will not auto-heal when `auto_create_collection` is false. |

### Observed Symptom in Production

1. Operator misconfigures credentials.
2. Every batch of messages causes 3 × `retry_delay` seconds of latency before reporting failure.
3. With default `retry_delay = 1s` and `max_retries = 3`, that is 1 + 2 + 3 = 6 seconds wasted per batch before giving up.
4. The warn log says "Transient database error" — which is factually wrong and misleads the operator.
5. For duplicate key errors, which CAN appear transiently in at-least-once delivery, the operator cannot distinguish a genuine transient issue from a structural data problem.

### The Deceptive Warn Message

Line 366-367:
```rust
warn!(
    "Transient database error (attempt {attempts}/{max_retries}): {e}. Retrying..."
);
```

This message appears in operator logs and Prometheus alert labels regardless of the actual error type. An operator seeing "Transient database error: Authentication failed" would be confused, because authentication failure is definitionally not transient.

---

## 2. The Fix: What Exactly Needs to Change

### Step 1: Add `is_transient_error` function

Add this function near the end of the `impl MongoDbSink` block, following the pattern already established in the MongoDB source connector (`mongodb_source/src/lib.rs`, lines 73-80):

```rust
fn is_transient_mongodb_error(error: &mongodb::error::Error) -> bool {
    use mongodb::error::ErrorKind;

    match error.kind.as_ref() {
        // Network-level problems: connection dropped, timeout, pool exhausted
        ErrorKind::Io(_) => true,
        ErrorKind::ServerSelection { .. } => true,
        ErrorKind::ConnectionPoolCleared { .. } => true,

        // Write errors: examine the MongoDB server-side error code
        ErrorKind::Write(write_failure) => {
            use mongodb::error::WriteFailure;
            match write_failure {
                WriteFailure::WriteError(write_error) => {
                    is_transient_write_error_code(write_error.code)
                }
                // BulkWriteError: check all individual write errors
                WriteFailure::BulkWriteError(bulk_error) => {
                    // If ANY write error is non-transient, the whole batch is non-transient
                    bulk_error.write_errors.iter().all(|we| {
                        is_transient_write_error_code(we.code)
                    })
                }
            }
        }

        // Auth / authorization / schema validation failures — never transient
        ErrorKind::Authentication { .. } => false,
        ErrorKind::InvalidArgument { .. } => false,
        ErrorKind::BsonDeserialization(_) => false,
        ErrorKind::BsonSerialization(_) => false,

        // Unknown error kinds: conservative default — do not retry
        _ => false,
    }
}

fn is_transient_write_error_code(code: i32) -> bool {
    // MongoDB server error codes that are genuinely transient
    // Reference: https://github.com/mongodb/mongo/blob/master/src/mongo/base/error_codes.yml
    matches!(
        code,
        // Transient transaction errors / write conflicts
        112 |  // WriteConflict
        244 |  // RetryChangeStream (internal)
        // Not-primary errors (replica set failover in progress)
        10107 | // NotPrimary
        13435 | // NotPrimaryNoSecondaryOk
        13436 | // NotPrimaryOrSecondary
        // Network/timing
        89 |   // NetworkTimeout
        9001   // SocketException
    )
    // Notably NOT included:
    // 11000 DuplicateKey — permanent
    // 13    Unauthorized — permanent
    // 18    AuthenticationFailed — permanent
    // 121   DocumentValidationFailure — permanent
    // 26    NamespaceNotFound — permanent
}
```

### Step 2: Update `insert_batch_with_retry` to gate retries

Replace lines 343-372 with:

```rust
async fn insert_batch_with_retry(
    &self,
    collection: &Collection<mongodb::bson::Document>,
    docs: &[mongodb::bson::Document],
) -> Result<(), Error> {
    let max_retries = self.get_max_retries();
    let retry_delay = self.retry_delay;
    let mut attempts = 0u32;

    loop {
        let result = collection.insert_many(docs.to_vec()).await;

        match result {
            Ok(_) => return Ok(()),
            Err(e) => {
                attempts += 1;

                // Gate: only retry errors that are genuinely transient
                if !is_transient_mongodb_error(&e) {
                    error!(
                        "Non-transient database error after {attempts} attempt(s), not retrying: {e}"
                    );
                    return Err(Error::CannotStoreData(format!(
                        "Non-transient batch insert error: {e}"
                    )));
                }

                if attempts >= max_retries {
                    error!("Transient batch insert failed after {attempts} attempts: {e}");
                    return Err(Error::CannotStoreData(format!(
                        "Batch insert failed after {attempts} attempts: {e}"
                    )));
                }

                warn!(
                    "Transient database error (attempt {attempts}/{max_retries}): {e}. Retrying..."
                );
                tokio::time::sleep(retry_delay * attempts).await;
            }
        }
    }
}
```

### Step 3: Add unit tests

Add to the `#[cfg(test)]` block at the bottom of `mongodb_sink/src/lib.rs`:

```rust
#[test]
fn given_io_error_should_be_transient() {
    use mongodb::error::{Error, ErrorKind};
    use std::io;

    let io_err = io::Error::new(io::ErrorKind::ConnectionReset, "connection reset by peer");
    let mongo_err = Error::from(ErrorKind::Io(io_err));
    assert!(is_transient_mongodb_error(&mongo_err));
}

#[test]
fn given_duplicate_key_error_should_not_be_transient() {
    use mongodb::error::{Error, ErrorKind, WriteFailure, WriteError};

    let write_err = WriteError {
        code: 11000,
        code_name: "DuplicateKey".to_string(),
        message: "E11000 duplicate key error".to_string(),
        details: None,
    };
    let mongo_err = Error::from(ErrorKind::Write(
        WriteFailure::WriteError(write_err)
    ));
    assert!(!is_transient_mongodb_error(&mongo_err));
}

#[test]
fn given_write_conflict_error_should_be_transient() {
    use mongodb::error::{Error, ErrorKind, WriteFailure, WriteError};

    let write_err = WriteError {
        code: 112, // WriteConflict
        code_name: "WriteConflict".to_string(),
        message: "Write conflict during plan execution".to_string(),
        details: None,
    };
    let mongo_err = Error::from(ErrorKind::Write(
        WriteFailure::WriteError(write_err)
    ));
    assert!(is_transient_mongodb_error(&mongo_err));
}
```

### Step 4: Verify the source connector's `is_transient_error` is adequate

The source connector (`mongodb_source/src/lib.rs`, lines 73-80) uses string matching:

```rust
fn is_transient_error(error: &str) -> bool {
    let msg = error.to_lowercase();
    msg.contains("timeout")
        || msg.contains("network")
        || msg.contains("connection")
        || msg.contains("pool")
        || msg.contains("server selection")
}
```

This is a different (and weaker) approach — it works on the formatted error string rather than the structured `mongodb::error::Error` type. It works because the source's retry wrapper (`poll_collection`) already converts the `mongodb::Error` to a string via `e.to_string()`. The source's approach is acceptable but imprecise (e.g., the word "connection" appears in "authentication connection refused" which could be a permanent failure). A follow-up improvement would be to give the source connector typed error checking as well, but that is a separate issue.

### Files Changed Summary

| File | Lines Changed | What |
|---|---|---|
| `core/connectors/sinks/mongodb_sink/src/lib.rs` | 343-372 (replace) | Add `is_transient_mongodb_error` guard in retry loop |
| `core/connectors/sinks/mongodb_sink/src/lib.rs` | after line 387 (add) | New `is_transient_mongodb_error` function |
| `core/connectors/sinks/mongodb_sink/src/lib.rs` | after line 387 (add) | New `is_transient_write_error_code` function |
| `core/connectors/sinks/mongodb_sink/src/lib.rs` | tests block (add) | 3 new unit tests |

---

## 3. Rubber Duck Debug: How Did This Happen

This section traces the actual sequence of decisions that produced the bug. It is not written to assign blame. It is written to understand the failure mode.

### The Build Order

The MongoDB source connector was built first. At the time the source was built, the author needed retry logic for network blips during `find()` operations. The author thought carefully about what errors deserve retries (they have to — polling is continuous and the source must be robust). The result was `is_transient_error()` at lines 73-80 of the source, plus tests for it at lines 847-887 (auth failure, duplicate key, invalid BSON all correctly marked non-transient).

The source connector's retry loop (`poll_collection`, lines 320-334) has the pattern:

```rust
Err(e) if is_transient_error(&e.to_string()) && attempts < max_retries => { ... }
Err(e) => return Err(e),
```

This is correct. The guard `is_transient_error(&e.to_string())` gates retries.

The MongoDB sink connector was built second, explicitly modeled on the source. When the sink's `insert_batch_with_retry` was written, the author copied the structural pattern of "loop, match Ok/Err, increment attempts, sleep, retry" — but did not copy the is-transient guard.

### Why Was the Guard Not Copied

Three plausible reasons, all of which likely contributed:

**Reason 1: The sink's failure mode feels different.**

When you are building a source connector, you are pulling data from MongoDB. A transient read failure blocks the pipeline — you cannot produce messages. The author is motivated to retry carefully because polling is a long-running loop and you want to distinguish "database down for 10 seconds" (retry) from "database rejected credentials" (fail immediately and alert).

When you are building a sink connector, you are pushing data to MongoDB. A write failure is handled at the batch level (`process_messages` simply logs the error and continues). The author's mental model may have been: "write errors are already caught and counted, so retry a few times then give up, and the batch is gone." The urgency to classify the error correctly was lower.

**Reason 2: The Postgres sink's pattern was used as a model, but incompletely.**

The Postgres sink (`postgres_sink/src/lib.rs`, lines 336-346) correctly gates retries with `is_transient_error`. However, the Postgres sink's architecture is more complex: `execute_batch_insert_with_retry` calls `bind_and_execute_batch`, which returns `Result<(), (sqlx::Error, bool)>` — the boolean in the tuple IS the transient flag, computed inside `bind_and_execute_batch` before returning. This is a two-function design where the transient check is visually separated from the retry loop.

When someone looked at this and modeled the MongoDB sink, they may have seen the retry loop structure but not fully internalized that the boolean flag in the return type was the key mechanism. The simpler single-function approach in the MongoDB sink (`insert_batch_with_retry` does everything in one function) lost the transient check in the simplification.

**Reason 3: The warn log message was wrong from day one but silently passed review.**

The message "Transient database error (attempt {attempts}/{max_retries})" was written at the same time as the code. If anyone had stopped to ask "wait, how do we know it's transient?", they would have caught the bug. The log message was a statement of intent that became the only place where the word "transient" appeared — no function, no variable, no check. The code assumed every error was transient and the log confirmed that assumption without questioning it.

This is a specific failure of the principle: "make reasoning explicit." The author had the right intention (retry only transient errors) but the implementation skipped the predicate.

### Why Did Tests Not Catch It

The tests that exist for the sink (`mongodb_sink/src/lib.rs`, lines 400-577) test:
- Config parsing
- PayloadFormat parsing
- Retry count and delay config
- URI redaction
- Verbose flag

There are zero tests for `insert_batch_with_retry` behavior with non-transient errors. A test like "given an auth failure, the retry function should return immediately without sleeping" would have caught this immediately. The test coverage mirrors the source's tests for `is_transient_error` (lines 847-887) but those tests do not exist in the sink because the function does not exist.

### The Root Cause, One Sentence

The developer who built the sink used the structural shape of the source's retry loop but not its predicate, wrote a log message asserting transience without checking it, and the test suite did not cover the retry guard — so the gap was invisible at review time.

---

## 4. Industry Research: Kafka/Debezium MongoDB Connectors

### 4.1 The Official MongoDB Kafka Connector (mongo-kafka)

Repository: https://github.com/mongodb/mongo-kafka

The official MongoDB Kafka sink connector (Java) does not implement its own transient/non-transient classification in application code. Instead, it delegates to two mechanisms:

**Mechanism A: The Kafka Connect framework's error tolerance.**

The connector exposes three error tolerance modes via `errors.tolerance`:
- `NONE` — any error immediately fails the connector task
- `DATA` — tolerates "network/server unreachable errors" (network failures only)
- `ALL` — skips over all problematic records

This is a blunt instrument. There is no per-error-code distinction: `ALL` will silently discard auth failures and duplicate key violations alike. This is a known and accepted design choice for the Kafka Connect ecosystem, where the Dead Letter Queue (DLQ) is the canonical mechanism for dealing with records that cannot be processed.

**Mechanism B: The MongoDB Java driver's built-in retryable writes.**

The MongoDB Java driver natively supports `retryWrites=true` in the connection string. When enabled, the driver automatically retries a subset of write operations that fail with specific transient errors (network issues, primary failover, `NotPrimary` errors). Crucially, the driver itself does NOT retry duplicate key violations or auth failures. The driver's retryable writes happen transparently below the Kafka connector's application code.

**What This Means for Our Comparison**

The official connector avoids the bug by outsourcing retry intelligence downward (to the driver) and upward (to the Kafka Connect framework). It does not have application-level retry loops that retry ALL errors like ours does.

In version 1.7, MongoDB explicitly REMOVED the application-level retry config properties `max.num.retries` and `retries.defer.timeout` from the connector. The official changelog note is:

> "The connector now relies on retries in the MongoDB Java driver and removes the retry properties."

This is the opposite choice from what we made. We added application-level retries. The official connector removed them.

### 4.2 The Community MongoDB Kafka Connector (hpgrahsl/kafka-connect-mongodb)

Repository: https://github.com/hpgrahsl/kafka-connect-mongodb (archived; integrated into the official connector in 2019)

This connector had the same structure: it surfaced write failures to the Kafka Connect framework rather than implementing its own retry classification. Duplicate key errors were a known issue (see GitHub issue #82 and #106) — but the solution was configuration of write strategies (upsert vs insert) and Kafka Connect's error tolerance settings, not application-level transient checks.

### 4.3 Debezium MongoDB Sink Connector

Reference: https://debezium.io/documentation/reference/stable/connectors/mongodb-sink.html

Debezium's MongoDB sink connector uses the Debezium engine (not the Kafka Connect framework directly in some deployments). It has a known bug: retriable errors including wrong passwords and insufficient privileges are retried indefinitely without honoring the `connect-max-attempts` setting.

Source: https://access.redhat.com/solutions/7026095

This is the SAME bug we have, but worse: Debezium retries indefinitely rather than up to `max_retries`. The Debezium bug demonstrates that this class of mistake is not unique to us — it is a recurring failure mode when engineers build retry loops for database connectors.

### 4.4 Confluent HTTP Sink Connector and Elasticsearch Connector

The Confluent Elasticsearch sink connector has a `RetryUtil.java` class. Its implementation, however, catches ALL exceptions uniformly:

```java
} catch (Exception e) {
    if (attempt >= maxTotalAttempts) {
        // throw ConnectException
    }
    // Otherwise it is retriable and we should retry
}
```

The comment "Otherwise it is retriable" is exactly the same false assumption as in our sink. The Confluent Elasticsearch connector also retries all errors up to a limit, not just transient ones.

### 4.5 Why This Is a Non-Issue in Kafka Connect Architectures (But an Issue for Us)

The Kafka Connect framework provides Dead Letter Queues as a first-class primitive. When a record fails permanently, it is routed to the DLQ topic. Operators inspect DLQ records, fix the data, and resubmit. The assumption in that ecosystem is: "you WILL have permanent failures, and the DLQ is your recovery path." Because permanent failures have a safe destination (the DLQ), the cost of retrying them a few times before routing to DLQ is low.

In the iggy connector SDK, there is no DLQ equivalent. When `insert_batch_with_retry` returns an error, `process_messages` (lines 222-231) logs it and moves on:

```rust
if let Err(e) = self
    .insert_batch(batch, topic_metadata, messages_metadata, &collection)
    .await
{
    let mut state = self.state.lock().await;
    state.insertion_errors += batch.len() as u64;
    error!("Failed to insert batch: {e}");
}
```

The messages are permanently lost (or rather, are acknowledged as consumed but not durably stored). This makes the cost of unnecessary retries higher: we are burning time that could be used alerting the operator and failing fast.

Additionally, the iggy connector runs as a long-lived process. In a Kafka Connect deployment, a failed task restarts at the Kafka framework level. In iggy, a permanent error (auth failure) that gets retried 3 times before giving up will happen again on the NEXT batch, and the next, and the next, for as long as the process runs. The cumulative wasted time is:

- Default `max_retries = 3`, `retry_delay = 1s`
- Wasted time per batch = 1s + 2s = 3s before the third attempt gives up
- At 100ms between batches, this means ~30x slowdown in error reporting

### 4.6 What We Should Have Learned From the Industry

The key lesson from the MongoDB Kafka connector's 1.7 decision (remove application-level retries, rely on the driver) is:

**If the underlying driver handles transient retries, do not add a second retry layer without carefully classifying errors at that layer.**

The MongoDB Rust driver (`mongodb` crate) also supports `retryWrites`. If we connect with `retryWrites=true`, the driver retries network-level failures automatically. Our application-level retry on top of that is useful ONLY for errors the driver does not retry (which are, by definition, the permanent ones). So our current code retries things the driver already retried, AND retries things that should never be retried.

The correct architecture is:
1. Let the driver handle its own retryable-writes for transient network errors.
2. At the application layer, add retries ONLY for things the driver does not cover (server selection errors with a secondary, connection pool exhaustion that the driver does not self-heal).
3. Never retry errors the driver passes up to you as permanent.

---

## 5. Lessons

### What We Got Right

- The MongoDB source connector has correct error classification (`is_transient_error` at lines 73-80) and uses it correctly in the retry loop (lines 320-334). The unit tests for it are thorough (lines 847-887).
- The Postgres sink connector has correct error classification (lines 503-517) and propagates the transient flag correctly through the return type (lines 337-353, 421-424).
- The concept of limiting retries at all is correct. Infinite retries (the Debezium bug) are worse.

### What We Got Wrong

- We applied the structural shape of the retry loop from the source connector without applying its predicate.
- We used the word "Transient" in a log message as a substitute for actually checking transience.
- The test suite for the sink covered configuration parsing but not retry behavior under non-transient errors.
- We built a second retry layer on top of the MongoDB driver without understanding that the driver already handles some transients, which means our layer only adds value for the errors we should NOT retry.

### The Test That Would Have Caught This

```rust
// This test does not exist yet. It should.
#[test]
fn given_auth_error_should_not_retry() {
    // If this test existed during development, the author would have
    // been forced to write is_transient_mongodb_error before the test passed.
    // TDD would have prevented this bug.
}
```

The source connector was built with tests for `is_transient_error`. The sink was built without tests for retry behavior. The absence of a TDD-first approach for the retry gate is the immediate procedural cause of the bug.

### Checklist for Future Connector Implementations

When building any connector with a retry loop:

- [ ] Write the `is_transient_error` test first (TDD-First, STUB phase)
- [ ] Implement the `is_transient_error` function before implementing the retry loop
- [ ] Ensure the retry loop calls `is_transient_error` and returns immediately on permanent errors
- [ ] Log message for non-transient errors must NOT say "Transient"
- [ ] Log message for non-transient errors should say "Non-transient, not retrying"
- [ ] Check whether the underlying driver already handles transient retries; avoid double-retrying
- [ ] Read the DLQ pattern for the target ecosystem; if no DLQ exists, fail fast is more important

---

## References

- MongoDB Kafka Connector official docs (error handling): https://www.mongodb.com/docs/kafka-connector/current/sink-connector/fundamentals/error-handling-strategies/
- MongoDB Kafka Connector error handling properties: https://www.mongodb.com/docs/kafka-connector/current/sink-connector/configuration-properties/error-handling/
- MongoDB Kafka Connector GitHub: https://github.com/mongodb/mongo-kafka
- Community MongoDB Kafka Connector (archived): https://github.com/hpgrahsl/kafka-connect-mongodb
- Debezium MongoDB sink connector docs: https://debezium.io/documentation/reference/stable/connectors/mongodb-sink.html
- Debezium retriable errors bug (Red Hat KB): https://access.redhat.com/solutions/7026095
- Confluent Elasticsearch RetryUtil (all-errors approach): https://github.com/confluentinc/kafka-connect-elasticsearch/blob/master/src/main/java/io/confluent/connect/elasticsearch/RetryUtil.java
- Kafka Connect error retry configuration: https://atchison.dev/error-retry-configuration-in-kafka-connect/
- MongoDB duplicate key in Kafka connector (KAFKA-305 Jira): https://jira.mongodb.org/browse/KAFKA-305
