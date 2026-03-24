# Apache Iggy Connectors Ecosystem Journal
> A chronological record of connector-related activity since Early Access (EA)

---

## Overview

Apache Iggy's connector ecosystem enables integration with external systems through sink (write) and source (read) connectors. This journal tracks all significant activity including PRs, issues, discussions, and community feedback.

**Current State (as of March 2026):**
- 5 native Rust connectors shipped (PostgreSQL, Elasticsearch, Iceberg, Quickwit, Stdout)
- 2 Java connectors (Pinot, Flink)
- 4 connectors in active PR review (ClickHouse, InfluxDB, MongoDB, Delta Lake)
- 120+ connector targets proposed in roadmap

---

## Timeline of Key Events

### 2025-05-28: Connectors Runtime Foundation
**PR [#1826](https://github.com/apache/iggy/pull/1826)** - `feat(connectors): add connectors runtime`
- **Status:** MERGED
- **Significance:** Initial implementation of the connectors runtime infrastructure
- Established the plugin model using Rust cdylib + C FFI

### 2025-06-17: Elasticsearch Connector
**PR [#1872](https://github.com/apache/iggy/pull/1872)** - `feat(connectors): support Elasticsearch sink and source connectors`
- **Status:** MERGED
- Native Rust implementation (~1,500 LOC)
- Bulk API sink, scroll/search source

### 2025-09-18: Apache Iceberg Sink
**PR [#2191](https://github.com/apache/iggy/pull/2191)** - `feat(connector): add Iceberg sink connector`
- **Status:** MERGED
- First data lakehouse connector

### 2025-09-23: Flink Connector (External)
**PR [#2175](https://github.com/apache/iggy/pull/2175)** - `feat(connectors): Apache Flink Connectors for Iggy`
- **Status:** CLOSED
- Moved to external repository approach

### 2025-11-07: Config Separation
**PR [#2317](https://github.com/apache/iggy/pull/2317)** - `refactor(connectors): split connectors configs from the runtime config`
- **Status:** MERGED
- Addressed issue [#2318](https://github.com/apache/iggy/issues/2318)

### 2025-11-19: Elasticsearch rustls Fix
**PR [#2374](https://github.com/apache/iggy/pull/2374)** - `fix(connectors): switch elasticsearch connector to use rustls`
- **Status:** MERGED

### 2025-11-19: Binary State Representation
**PR [#2378](https://github.com/apache/iggy/pull/2378)** - `fix(connectors): change connector state to binary representation`
- **Status:** MERGED

### 2025-12-03: HTTP Config Retry Mechanism
**PR [#2437](https://github.com/apache/iggy/pull/2437)** - `feat(connectors): add retry mechanism to connectors HTTP config provider`
- **Status:** MERGED

### 2025-12-11: ARM64 Builds & Connector Plugins
**PR [#2472](https://github.com/apache/iggy/pull/2472)** - `feat(ci): add ARM64 builds and connector plugins to edge release`
- **Status:** MERGED

### 2025-12-17: Apache Pinot Connector
**PR [#2499](https://github.com/apache/iggy/pull/2499)** - `feat(connector): add iggy-pinot external connector`
- **Status:** MERGED
- Java connector via Kafka compatibility layer

### 2025-12-18: Version Flag Support
**PR [#2502](https://github.com/apache/iggy/pull/2502)** - `feat(connectors): add --version flag support to connector runtime`
- **Status:** MERGED

---

## 2026 Activity

### 2026-01-13: Redshift Sink (Abandoned)
**PR [#2557](https://github.com/apache/iggy/pull/2557)** - `feat(connectors): implement Redshift Sink Connector with S3 staging`
- **Status:** CLOSED
- Issue [#2540](https://github.com/apache/iggy/issues/2540) remains open

### 2026-01-14: Flink TCP Transport
**PR [#2560](https://github.com/apache/iggy/pull/2560)** - `feat(java): Add TCP transport support for Flink connector`
- **Status:** CLOSED
- Issue [#2484](https://github.com/apache/iggy/issues/2484) remains open

### 2026-01-17: PostgreSQL Extensions
**PR [#2579](https://github.com/apache/iggy/pull/2579)** - `feat(connectors): extend Postgres sink & source connectors, add integration tests`
- **Status:** MERGED
- ~2,400 LOC, WAL-based CDC for source

### 2026-01-21: Iceberg Deps Update
**PR [#2605](https://github.com/apache/iggy/pull/2605)** - `deps: Update iceberg to 0.8.0`
- **Status:** MERGED

### 2026-01-28: Test Harness
**PR [#2632](https://github.com/apache/iggy/pull/2632)** - `feat(integration): add core test harness library`
- **Status:** MERGED

### 2026-01-28: Prometheus Metrics
**PR [#2633](https://github.com/apache/iggy/pull/2633)** - `feat(connectors): add Prometheus metrics and stats endpoints`
- **Status:** MERGED

### 2026-02-02: Connector Version in Stats
**PR [#2660](https://github.com/apache/iggy/pull/2660)** - `feat(connectors): add connector version to stats endpoint`
- **Status:** MERGED

### 2026-02-03: Test Migration
**PR [#2667](https://github.com/apache/iggy/pull/2667)** - `refactor(integration): migrate connectors tests to iggy_harness proc macro`
- **Status:** MERGED

### 2026-02-04: Mux Snapshot Interface
**PR [#2675](https://github.com/apache/iggy/pull/2675)** - `feat(metadata): impl Snapshot interface for Mux state machine`
- **Status:** MERGED

### 2026-02-05: Elasticsearch E2E Tests
**PR [#2684](https://github.com/apache/iggy/pull/2684)** - `test(connectors): add e2e tests for Elasticsearch sink connector`
- **Status:** CLOSED
- Issue [#2592](https://github.com/apache/iggy/issues/2592) was closed

### 2026-02-05: State & Memory Leak Fix
**PR [#2685](https://github.com/apache/iggy/pull/2685)** - `feat(connectors): fix state & memory leak, test all plugins, enrich sinks`
- **Status:** MERGED

### 2026-02-09: Pinot Gradle Fix
**PR [#2706](https://github.com/apache/iggy/pull/2706)** - `fix(java): resolve Gradle 9 task dependency error in Pinot connector publish`
- **Status:** MERGED

### 2026-02-10: Plugin Loading Hardening
**PR [#2713](https://github.com/apache/iggy/pull/2713)** - `fix(connectors): harden plugin loading and config metadata`
- **Status:** MERGED
- Closed issue [#2712](https://github.com/apache/iggy/issues/2712)

---

## Active PRs (March 2026)

### ClickHouse Sink Connector
**PR [#2886](https://github.com/apache/iggy/pull/2886)** - `feat(connectors): Clickhouse Sink Connector`
- **Status:** OPEN - REVIEW_REQUIRED
- **Author:** Community contributor
- **Created:** 2026-03-06
- **Closes:** Issue [#2539](https://github.com/apache/iggy/issues/2539)
- **Details:**
  - Real-time data analytics engine integration
  - Inspired by official ClickHouse Kafka Connector
  - Tested with 30k+ rows
- **Review Feedback:**
  - Codecov reports 79.47% patch coverage (323 lines missing coverage)
  - Review by @abonander (COMMENTED)
- **Previous iteration:** PR [#2885](https://github.com/apache/iggy/pull/2885) was closed

### MongoDB Sink Connector
**PR [#2815](https://github.com/apache/iggy/pull/2815)** - `feat(connectors): add MongoDB sink connector`
- **Status:** OPEN - REVIEW_REQUIRED
- **Author:** @amuldotexe
- **Created:** 2026-02-25
- **Partially addresses:** Issue [#2739](https://github.com/apache/iggy/issues/2739)
- **LOC:** ~401 lines added
- **Review History:**
  - @krishvishal: CHANGES_REQUESTED (9 review comments)
  - @atharvalade: Additional blocker feedback
- **Key Feedback Points:**
  1. Liveness issue with partial failures and offset commits
  2. `message.id.to_string()` as MongoDB `_id` isn't safe for multiple topics
  3. Need composite `_id` from stream+topic+partition+message_id
  4. Insert failures after partial writes need handling
- **Latest Update (2026-03-06):**
  - Removed shared runtime sink callback changes
  - Added `ordered(false)` batch inserts
  - Composite `_id` implementation
  - `AtomicU64` counters
  - Config normalization in `new()`
- **Codecov:** 87.59% patch coverage (50 lines missing)

### InfluxDB Connector
**PR [#2801](https://github.com/apache/iggy/pull/2801)** - `feat: Add InfluxDB connector implementation`
- **Status:** OPEN - CHANGES_REQUESTED
- **Author:** @ryerraguntla
- **Created:** 2026-02-24
- **Issue:** [#2700](https://github.com/apache/iggy/issues/2700)
- **Review Feedback:**
  - @mmodzelewski: "Quite a few unrelated changes have slipped into this PR"
  - Request to split Redshift and InfluxDB changes into separate PRs

### Delta Lake Sink Connector
**PR [#2783](https://github.com/apache/iggy/pull/2783)** - `feat(connectors): Delta Lake Sink Connector`
- **Status:** OPEN - CHANGES_REQUESTED
- **Created:** 2026-02-19
- **Closes:** Issue [#1852](https://github.com/apache/iggy/issues/1852)
- **Inspiration:** kafka-delta-ingest project
- **Testing:**
  - 32,632 messages tested
  - Verified Delta table creation on filesystem
  - E2E tests for local and S3 Delta Lake
- **Reviews:**
  - @hubcio: CHANGES_REQUESTED
  - @kriti-sc: 5 COMMENTED reviews
  - @krishvishal: COMMENTED
- **Codecov:** 95.72% patch coverage (29 lines missing)
- **Complexity:** +83 added

### Connector Restart Without Runtime Restart
**PR [#2781](https://github.com/apache/iggy/pull/2781)** - `feat(connectors): restart connector with new config without runtime restart`
- **Status:** OPEN - CHANGES_REQUESTED
- **Created:** 2026-02-19
- **Closes:** Issue [#2417](https://github.com/apache/iggy/issues/2417)
- **Design:**
  - Added `POST /sinks/{key}/restart` and `POST /sources/{key}/restart`
  - Watch channel for graceful cancellation
  - 5s timeout for task handles
  - Container NOT reloaded - only closed/reopened with new config

---

## Key Discussions

### Discussion #1670: Connectors Plugin System (2025-03-31)
The foundational discussion proposing a modular plugin system:
- **Connector Types:** Local (IPC via iceoryx2) and Remote (TCP/UDP/QUIC/HTTP)
- **Event Types:** Diagnostic and Data events
- **Architecture:** Pipes and filters pattern

### Discussion #2236: Flink Architecture (2025-10-03)
Discussed connector architecture involving data/stream processors like Flink.

### Discussion #2343: Configuration Storage Trait (2025-11-12)
Discussed configuration storage trait for connectors runtime.

### Discussion #2449: Apache Pinot Connector (2025-12-05)
Detailed the Apache Pinot connector implementation approach.

### Discussion #2756: Connector Ecosystem Tracking (2026-02-17)
**The master tracking discussion:**
- First draft of the comprehensive connector roadmap
- 120+ connector targets identified
- Priority system (P0-P4) established
- Community encouraged to claim proposed connectors

---

## Open Issues Tracking

| Issue | Title | Status | Notes |
|-------|-------|--------|-------|
| [#2539](https://github.com/apache/iggy/issues/2539) | Implement ClickHouse Sink Connector | Open | PR #2886 in review |
| [#2540](https://github.com/apache/iggy/issues/2540) | Implement Redshift Sink Connector with S3 staging | Open | No active PR |
| [#2484](https://github.com/apache/iggy/issues/2484) | Flink connector - transport - http to tcp | Open | Enhancement |
| [#2417](https://github.com/apache/iggy/issues/2417) | Restart connector without runtime restart | Open | PR #2781 in review |
| [#2500](https://github.com/apache/iggy/issues/2500) | JDBC Source and Sink Connectors | Open | Planned |
| [#2700](https://github.com/apache/iggy/issues/2700) | InfluxDB Connector (Sink, Source) | Open | PR #2801 needs rework |
| [#2739](https://github.com/apache/iggy/issues/2739) | MongoDB Connector | Open | PR #2815 (sink only) |
| [#2753](https://github.com/apache/iggy/issues/2753) | Connector Ecosystem Roadmap | Open | Master tracking issue |
| [#1846](https://github.com/apache/iggy/issues/1846) | Avro payload support | Open | In progress |
| [#2598](https://github.com/apache/iggy/issues/2598) | E2E tests for Pinot connector | Open | |

---

## Codecs/Serialization Status

| Format | Status | Notes |
|--------|--------|-------|
| JSON | Done | Built-in to runtime |
| Protobuf | Done | Built-in to runtime |
| FlatBuffers | Done | Zero-copy for IoT |
| Raw/Bytes | Done | Built-in |
| Text/String | Done | Built-in |
| Avro | In Progress | Issue #1846 |
| BSON | In Progress | For MongoDB |
| Parquet | Proposed | For S3/GCS/HDFS |
| CSV | Proposed | Batch import/export |
| MessagePack | Proposed | Compact binary for IoT |

---

## Key Contributors & Reviewers

### Maintainers/Reviewers
- @mmodzelewski (MEMBER)
- @hubcio (CONTRIBUTOR)
- @krishvishal (CONTRIBUTOR)
- @kriti-sc (CONTRIBUTOR)
- @atharvalade (CONTRIBUTOR)

### Active Contributors
- @amuldotexe (MongoDB sink)
- @ryerraguntla (InfluxDB)
- Community contributors (ClickHouse, Delta Lake)

---

## Lessons Learned & Patterns

1. **PR Hygiene:** InfluxDB PR flagged for mixing unrelated changes - always keep PRs focused
2. **Codecov Requirements:** All PRs need good test coverage (target 80%+)
3. **Composite IDs:** MongoDB taught that simple message IDs cause collisions across topics
4. **Partial Failure Handling:** Critical to handle mid-batch failures without infinite loops
5. **Config Separation:** Runtime config and connector config should be separate (merged Nov 2025)

---

*Last updated: 2026-03-07*
*Generated from GitHub API data via gh CLI*
