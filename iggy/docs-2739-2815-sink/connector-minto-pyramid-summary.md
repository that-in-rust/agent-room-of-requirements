# Iggy Connectors: Minto Pyramid Analysis

**Date**: February 8, 2026
**Method**: Parseltongue v1.5.6 + GitHub CLI + 12 closed issues + 17 merged PRs

---

## Governing Thought

**Every Iggy connector follows a single pattern: 3 structs + 4 methods + 1 TOML config file.** The closed issues prove this pattern is stable and scalable — from the simplest sink (StdoutSink, 8 entities) to the most complex (IcebergSink, 47 entities), the skeleton never changes.

---

## Key Line: Clear patterns emerged from closed issues

### S1: The Sink/Source trait contract is the anchor

Every connector — regardless of complexity — implements exactly `new()`, `open()`, `consume()`/`poll()`, `close()`. The 12 resolved issues never changed these 4 methods. They only added depth *within* them (retries, batching, routing). New connector work is purely about the external system integration, not the framework.

### S2: Complexity grows in predictable layers

- **Layer 1** (8-11 entities): Stdout/Random — just the 4 methods
- **Layer 2** (11 entities): Quickwit/ES — adds client creation + bulk operations
- **Layer 3** (47-56 entities): Postgres/Iceberg — adds connection pooling, retry, CDC, routing, state management

Each layer adds capabilities without breaking the one below it. Zero circular dependencies confirms this.

### S3: Closed issues taught specific lessons the open issues will repeat

- **#2318** (split configs) -> Every new connector must have its own TOML file
- **#2416** (retry mechanism) -> Every connector doing HTTP/TCP needs exponential backoff
- **#2579** (Postgres extension) -> Database connectors need `PayloadFormat` enum + batch operations
- **#2594** (Quickwit e2e tests) -> Follow `given_*_should_*` naming, use Docker containers

---

## Biggest Challenge

The jump from StdoutSink (8 entities) to PostgresSink (54 entities) is 6.75x in complexity. No intermediate guidance exists for *when* to add connection pooling, retry logic, or state management. The resolved issues filled these gaps reactively.

**Recommendation**: Start with StdoutSink skeleton, add search-engine-layer methods for HTTP systems, escalate to database-layer methods for stateful systems. Iceberg router pattern only for multi-destination fan-out.

---

## Parseltongue Stats

- 15,637 code entities, 76,133 dependency edges
- 0 circular dependencies
- Sink trait blast radius: 494 entities at 2 hops
- Top complexity hotspot: `postgres_source/src/lib.rs` at 147 coupling
