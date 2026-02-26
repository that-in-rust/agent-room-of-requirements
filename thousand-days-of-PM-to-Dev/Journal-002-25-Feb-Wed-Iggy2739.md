# PR-2815 Due Diligence Retrospective (MongoDB Sink)

PR: https://github.com/apache/iggy/pull/2815  
Date captured: February 25, 2026  
Branch: `codex/2739-sink-sync`

## 1) Why this document exists

This is a reusable record of what we investigated, how we investigated it, and which prompt/review patterns actually improved PR quality for a first-time dev+PM contribution.

The goal is not just "what changed", but "how we reduced risk before asking maintainers to review".

## 2) Outcome snapshot

- Sink PR split from source to keep scope reviewable.
- PR body aligned to Apache Iggy `PULL_REQUEST_TEMPLATE.md`.
- Failure behavior made explicit (no silent success on partial/duplicate failure).
- Added/validated integration and unit tests for high-risk sink behavior.
- Added docs for delivery semantics and limitations.
- Added reproducible demo evidence (GHCR image + smoke output in PR body).

## 3) Timeline (high level)

### Phase A - Discovery and critique loop

- Compared implementation with internal connector patterns and issue expectations.
- Identified risk themes:
  - ordering/state correctness
  - silent partial failures
  - docs vs behavior mismatch
  - test blind spots (end state only vs transition correctness)

### Phase B - Scope control and branch strategy

- Created isolated repo folders for ref/sink/source worktrees.
- Synced sink/source branches to `upstream/master` baseline.
- Transplanted sink-only changes into sink branch.
- Removed source leakage from shared integration wiring.

### Phase C - Hardening and proof

- Added/verified sink test suite including failure semantics.
- Ran local quality gates and crate tests.
- Finalized PR text with rationale, what changed, local execution, AI usage.

### Phase D - Maintainer empathy pass

- Added PR prep docs with explicit invariants, failure modes, and reviewer fast-path.
- Reframed technical points in plain language for clear reviewer consumption.

## 4) What we searched and why (research surfaces)

### A) Internal codebase precedent

Objective: avoid inventing patterns maintainers do not recognize.

We looked at:

- existing connector behavior (sink and source patterns)
- integration fixture wiring patterns
- connector runtime stats/error paths
- local PR template and contribution policy

Why it mattered:

- Maintainers prefer consistency over novelty.
- Existing patterns reduce "why is this different?" review friction.

### B) Git history and branch diffs

Objective: ensure sink PR is truly sink-only and reviewable.

Commands/patterns used repeatedly:

- `git diff --name-only upstream/master...HEAD`
- `git status --short --branch`
- `git log --oneline --decorate -n N`
- explicit-path staging (never broad `git add .` for split PR prep)

Why it mattered:

- Large mixed diffs slow review and trigger closure risk.
- Clean commit intent improves trust for first-time contributors.

### C) Maintainer feedback pattern mining (GitHub CLI)

Objective: learn what maintainers repeatedly object to in connector PRs.

Used:

- `gh api repos/apache/iggy/pulls/<id>/comments`
- `gh pr view <id> --json body`

What stood out across reviewed PRs/comments:

- silent data loss paths are high severity
- overbroad error matching is risky
- unclear lifecycle close/flush semantics trigger pushback
- unnecessary allocations and hidden behavior draw comments

Why it mattered:

- These comments gave a practical "review radar" before opening PR-2815.

### D) OSS behavior checks (MongoDB semantics)

Objective: align tests and contracts with real MongoDB failure modes.

Key behavior areas validated:

- ordered `insertMany` can partially succeed before failure
- duplicate key behavior in insert-only flows
- transient vs non-transient classes and retries
- write concern / retry ambiguity edges

Why it mattered:

- Test design should follow database semantics, not assumptions.

### E) Cross-repo knowledge-base research (`agent-room-of-requirements/iggy`)

Objective: use accumulated project notes to avoid rediscovering decisions and to keep prompt quality high.

Path researched:

- `/Users/amuldotexe/cross-repo-knowledge-base/agent-room-of-requirements/iggy`

Major areas referenced:

- `docs-2739/` (issue specs, connector comparisons, E2E learnings, retry bug analysis, PR prep)
- `meta-commentary/` (contribution method, quality-signal framing, merge simulation notes)

Representative files reviewed:

- `docs-2739/issue-2739-mongodb-connector-spec.md`
- `docs-2739/issue-2739-pr-preparation.md`
- `docs-2739/connector-best-practices-patterns-20260221180456.md`
- `docs-2739/e2e-testing-learnings-mongodb-kafka-20260221.md`
- `docs-2739/sink-retry-bug-analysis.md`
- `meta-commentary/issue2739-prd-final-merge-simulations.md`
- `meta-commentary/contribution-method.md`

Why it mattered:

- improved prompt specificity by grounding asks in prior documented context
- prevented repeating already-closed design debates
- accelerated due-diligence by reusing known risk and test patterns

## 5) Prompt patterns that worked

These prompt patterns repeatedly produced useful output.

### Pattern 1 - Precedent-first critique

"Compare this implementation against existing connectors in this repo. List only behavior gaps, not style issues."

Why useful:

- prevented generic advice
- grounded improvements in local precedent

### Pattern 2 - End-state vs transition test gap

"Which bugs can pass current tests because tests only validate final state, not transition/input used?"

Why useful:

- caught subtle correctness blind spots
- improved test quality without exploding test count

### Pattern 3 - Scope splitter

"Given this branch, produce sink-only and source-only file sets relative to upstream/master and identify leakage in shared files."

Why useful:

- directly enabled two-PR strategy
- minimized review blast radius

### Pattern 4 - Maintainer lens rewrite

"Rewrite this PR plan from maintainer perspective: what would block merge, what is non-blocking, what evidence removes doubt fastest?"

Why useful:

- improved signal-to-noise in PR description
- turned raw work into review-friendly evidence

### Pattern 5 - ELI5 + line-mapped explanation

"Explain this connector in layered maps and tie each claim to file:line."

Why useful:

- made review and handoff easier
- increased confidence to answer review questions

## 6) Due diligence checklist we actually used

- Scope discipline:
  - sink-only diff vs upstream validated
  - shared integration files checked for source leakage
- Correctness:
  - no silent success on failed writes
  - duplicate key path explicitly tested
  - accounting reflects successful writes only
- Operational safety:
  - URI redaction verified
  - startup collection behavior tested
- Testing:
  - unit + integration tests run locally
  - high-risk scenarios emphasized
- PR quality:
  - template-compliant PR body
  - exact local execution bullets
  - explicit AI usage and verification statement

## 7) Key anti-patterns we avoided

- Mixed sink+source PR for a first contribution.
- "CI will validate" without local execution evidence.
- Generic test bloat without risk-based prioritization.
- README claims not backed by tests/behavior.
- Silent partial-failure acceptance.

## 8) Artifacts produced during due diligence

- `pr-prep-2739-sink.md`
- `spec-2739-mongodb-sink-test-strategy.md`
- `tdd-journal-2739-mongodb-sink.md`
- cross-repo research corpus:
  - `/Users/amuldotexe/cross-repo-knowledge-base/agent-room-of-requirements/iggy/docs-2739/*`
  - `/Users/amuldotexe/cross-repo-knowledge-base/agent-room-of-requirements/iggy/meta-commentary/*`
- PR body for #2815 with explicit local execution evidence
- branch split setup (`iggy_2739_ref`, `iggy_2739_sink`, `iggy_2739_source`)

## 9) Reusable playbook for next PR

1. Start from `upstream/master` clean branch.  
2. Define scope contract before coding.  
3. Mine precedent and maintainer comments first.  
4. Build tests around failure transitions, not only final state.  
5. Keep a running due-diligence journal.  
6. Open PR only after local evidence is concrete and template-compliant.

## 10) Git history references that informed this process

Reference branch history (source hardening + docs chronology):

- `3314b4fb` feat(connectors): add MongoDB sink and source connectors
- `59bb817c` fix(source): checkpoint after mark/delete, add observability
- `6aa135c2` fix(source): use current batch offset in mark/delete
- `c5d8ee3e` fix(source): pass expected count to mark/delete warnings
- `3f8f59fb` fix(source): add partial mismatch telemetry for mark/delete
- `c7d7caa4` docs: refresh issue 2739 journal

Sink PR branch tip:

- `e2cf5fea` feat(connectors): add MongoDB sink connector

These commits gave us a concrete "what changed and why" narrative for sink/source split and review prep.
