# Method: How to Prepare a High-Quality Open Source PR

Context: MongoDB sink + source connectors for Apache Iggy (issue 2739).
3,600+ lines, first contribution to the project. Here's what we did and why.

---

## 1. Git Archaeology Before Writing Code

Before writing a single line, we studied every prior connector PR:

| PR | Lines | Who | Outcome |
|----|-------|-----|---------|
| Postgres #1959 | +1,882 | jaroslawroszyk | Merged, sink+source together |
| Elasticsearch #1872 | +2,079 | kaori-seasons | 5-month disaster, maintainer rewrote |
| Iceberg #2191 | +1,906 | EdgarModesto23 | Merged, sink only |
| E2E test suite #2190 | +2,587 | spetz (maintainer) | Merged, test infrastructure |
| Postgres extend #2579 | +3,726 | spetz (maintainer) | Merged, extended connector |

**What this revealed:**
- Sink + source always ship together (Postgres, Elasticsearch both did this)
- E2E tests were always added LATER by the maintainer — no external contributor shipped them
- The Elasticsearch PR is the cautionary tale: AI-generated code, didn't use SDK traits, 3 months of "I'll fix it this week", maintainer had to rewrite. This is what tightened CONTRIBUTING.md
- The 500-line limit is for drive-by PRs, not feature implementations. Pinot (+2,312 lines) had an EMPTY PR body and got merged

**The method:** `git log --oneline --all | grep connector` + `gh pr view` on every result. Read the PR comments, not just the code. The comments tell you what the maintainer cares about.

---

## 2. Bug Discovery Through Cross-Reference Review

We found a real bug by comparing our implementation against the existing codebase:

**The pattern:** Read the Postgres sink's `is_transient_error` function (typed `sqlx::Error` matching with specific Postgres error codes like "40001", "40P01"). Then looked at our MongoDB sink — our `insert_batch_with_retry` was retrying ALL errors, including auth failures, duplicate keys, and schema validation errors. The log said "Transient database error" without checking.

**Industry validation:** Researched how Kafka MongoDB Connector and Debezium handle this:
- Debezium has the SAME bug (worse — infinite retries on non-transient errors)
- MongoDB Kafka Connector solved it by removing app-level retries entirely in v1.7, relying on driver retries
- Our fix: typed `ErrorKind` matching with MongoDB-specific codes (11000=duplicate key, 13=unauthorized, 121=schema validation)

**The method:** For every function you write, find its equivalent in another connector in the same codebase. If they're doing something you're not, you have a bug. If you're doing something they're not, you either have an improvement or a mistake — validate against industry implementations.

**Why this matters for the PR:** This fix + 6 unit tests became the strongest quality signal. It shows we read the existing codebase, understood the patterns, and improved on them.

---

## 3. README Iteration — 4 Rewrites to Find the Right Level

The README went through 4+ iterations. Each time we asked: "what would the best engineers say?"

| Iteration | Lines | Problem |
|-----------|-------|---------|
| v1 (initial) | 284+122 | Feature docs, payload format sections, offset tracking — screamed "AI generated" |
| v2 (stripped) | 106+81 | Quick Start + Config + Payload Formats + Verify It Works — still too much |
| v3 (minimal) | ~20 | Matched repo convention but stripped too much — "think more what is our context" |
| v4 (final) | 60+70 | Quick Start + Config + Testing with test names listed |
| v5 (current) | 131+137 | Added "Try It" interactive test section |

**Key tensions:**
- Other connector READMEs range from 13 lines (stdout_sink) to 375 lines (postgres_source)
- Kafka MongoDB Connector's README is 84 lines: one-liner, docs link, build command, maintainers. Zero features, zero config docs, zero examples
- But Kafka has an external docs site. We don't. The README IS the documentation
- "Can we have quick start and test and not have more features etc. shit?" — the user's exact words

**What we landed on:**
- Config table stays (no external docs site to link to)
- Testing section lists test names (reviewer can see what's covered at a glance)
- "Try It" section is the lead — copy-paste commands that prove the connector works
- No "Features" section, no "Payload Formats" section, no "Offset Tracking" section

**The method:** Compare with 3 reference points: (1) other READMEs in the same repo, (2) the equivalent in the industry leader (Kafka), (3) what a reviewer needs to verify correctness. Write for #3, format for #1, learn from #2.

---

## 4. E2E Tests as Proof, Not Afterthought

The Elasticsearch PR disaster is the negative example. The code "worked" but nobody could verify it. The maintainer had to rewrite it himself.

Our approach: E2E tests are the PR's centerpiece.

- 8 E2E tests (4 sink + 4 source) using testcontainers + iggy_harness
- Tests include edge cases: restart survival, delete-after-read, mark-processed, auto-create-collection
- Following the exact patterns from the Postgres/Elasticsearch E2E fixtures

**The argument for keeping E2E in the same PR:** "Think logically how can you even test the PR without E2E tests — it is the proof that the thing works." Without E2E tests, the PR is "trust me, it works." With E2E tests, the reviewer can run `cargo test --test mod -- mongodb` and see 8 green checks.

**The method:** Tests aren't a separate concern. They're the primary deliverable. The implementation is what makes the tests pass. Lead with test coverage in the PR description: "52 unit tests + 8 E2E integration tests. All passing."

---

## 5. Interactive Test as Reviewer Empathy

The E2E tests prove correctness (automated, repeatable). The interactive test proves usefulness (human, tangible).

**What the "Try It" section does:**
1. Start MongoDB with `docker run` (one line)
2. Start iggy-server (one line)
3. Create stream + topic (two lines)
4. Create connector config via heredoc (self-contained, no file editing)
5. Start connector runtime (one line)
6. Send/insert a message (one line)
7. Verify it arrived (one line with expected output)

**Why this matters:** The reviewer can see the full data flow in 60 seconds. They don't have to trust the tests — they can see `{"hello":"mongodb"}` land in a real MongoDB collection. This directly addresses the CONTRIBUTING.md concern about being a "proxy between maintainer and LLM."

**The method:** The interactive test isn't documentation. It's a trust-building exercise. Show the reviewer what success looks like before they read a single line of implementation.

---

## 6. PR Strategy: One PR, Full Context

Despite 3,600+ lines exceeding the 500-line guideline for new contributors:

**Why one PR:**
- Precedent: every connector PR shipped sink+source together
- E2E tests can't be separated — they're the proof the implementation works
- Splitting creates review overhead (reviewer has to context-switch between PRs)
- The 500-line limit is for drive-by fixes, not feature implementations

**PR description strategy:** Use `PULL_REQUEST_TEMPLATE.md` format exactly. Lead with test coverage. Include design decisions table. Reference the Postgres PR (#2579, +3,726 lines, same scope) as precedent. Disclose AI usage honestly.

**The method:** Study the project's merge history to understand what actually gets merged, not just what the guidelines say. The guidelines are the floor, not the ceiling.

---

## Summary: The Checklist

1. Read every prior PR in the same area (git archaeology)
2. Cross-reference your implementation against existing code in the repo (find bugs before reviewer does)
3. Validate design decisions against industry leaders (Kafka, Debezium, Flink)
4. Write E2E tests first, then make them pass (TDD)
5. Iterate the README until it passes the "best engineer" test
6. Add an interactive test that proves usefulness in 60 seconds
7. Lead the PR description with test coverage, not feature list
8. Study merge history to choose the right PR strategy
