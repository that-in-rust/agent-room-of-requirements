# From Here to Merged PR: Exact Execution Plan

## Context

MongoDB sink + source connectors are fully implemented. 22 files staged (+3,765 lines), zero commits. Branch `ab_202602_issue02` is up to date with `upstream/master`. Three clippy errors in test code are the only CI blocker. This plan is the exact sequence from current state to PR on `apache/iggy`.

---

## Current State (verified 2026-02-23)

| Aspect | Status |
|--------|--------|
| Branch | `ab_202602_issue02` tracking `upstream/master` (up to date) |
| Remotes | `origin` = `amuldotexe/iggy.git`, `upstream` = `apache/iggy.git` |
| Staged | 22 files, +3,765 lines, **not committed** |
| Fork master | 48 commits behind upstream (stale) |
| `cargo fmt` | PASS |
| `cargo clippy --all-targets` | **FAIL** — 3 errors in source test code |
| `cargo sort` | PASS |
| `cargo machete` | PASS |
| Trailing newlines | PASS |
| TOML formatting | PASS |
| License headers | PASS (READMEs exempt — matches all other connector READMEs) |
| `prek` | **NOT installed** |
| `gh` CLI | Installed, authenticated as `amuldotexe` |

---

## Step 1: Fix 3 Clippy Errors

All in `core/connectors/sources/mongodb_source/src/lib.rs` (test code only):

| Line | Error | Fix |
|------|-------|-----|
| 635 | `bool_assert_comparison` | `assert_eq!(source.verbose, false)` → `assert!(!source.verbose)` |
| 658 | `bool_assert_comparison` | `assert_eq!(source.verbose, true)` → `assert!(source.verbose)` |
| 735 | `unnecessary_get_then_check` | `state.tracking_offsets.get(&config.collection).is_none()` → `!state.tracking_offsets.contains_key(&config.collection)` |

Then re-stage: `git add core/connectors/sources/mongodb_source/src/lib.rs`

---

## Step 2: Verify ALL CI Checks Pass

Run these sequentially — every one must pass before committing:

```bash
# Tier 1: Formatting & Linting
cargo fmt --all -- --check
cargo clippy --all-targets --all-features -- -D warnings
cargo sort --check --workspace
cargo machete

# Tier 2: Compilation & Tests
cargo test -p iggy_connector_mongodb_sink    # expect 25 tests
cargo test -p iggy_connector_mongodb_source  # expect 33 tests
cargo test --test mod --no-run               # E2E compilation gate

# Tier 3: CI Scripts (optional but recommended)
./scripts/ci/trailing-whitespace.sh --check --ci
./scripts/ci/trailing-newline.sh --check --ci
./scripts/ci/taplo.sh --check --ci
```

**If any fail**: fix, re-stage, re-run. Do NOT commit until all green.

---

## Step 3: Install prek + Pre-commit Hooks

CONTRIBUTING.md explicitly requires this:

```bash
cargo install prek
prek install
```

This installs git hooks that run automatically on `git commit`. The hooks will validate formatting, clippy, etc. If we already pass Step 2, hooks should pass too — but they must be installed.

---

## Step 4: Commit

Single commit. Everything is already staged.

**Commit message format** (from CONTRIBUTING.md): `type(scope): subject`

```
feat(connectors): add MongoDB sink and source connectors
```

**Critical rule from CLAUDE.md**: Do NOT put `#2739` in the commit message. The issue reference goes in the PR body only. When the maintainer squash-merges, GitHub appends the PR number automatically (this is the repo's convention — see: `feat(cluster): create a unified abstraction for subsystems (#2780)`).

**What prek hooks do on commit**: They run the same checks as Step 2 (fmt, clippy, etc.). If they fail, the commit is rejected — fix issues and try again as a NEW commit (never `--amend` a failed commit).

---

## Step 5: Sync Fork's Master

The fork's `origin/master` is 48 commits behind `upstream/master`. This doesn't block the PR, but it's good hygiene and avoids confusion if anyone looks at the fork.

```bash
git fetch upstream
git push origin upstream/master:master
```

This pushes the latest upstream master to the fork's master without switching branches.

---

## Step 6: Push Branch to Fork

```bash
git push origin ab_202602_issue02
```

This pushes to `amuldotexe/iggy.git`. The branch now exists on GitHub.

---

## Step 7: Create PR on apache/iggy

```bash
gh pr create --repo apache/iggy --base master --head amuldotexe:ab_202602_issue02 \
  --title "feat(connectors): add MongoDB sink and source connectors" \
  --body "$(cat <<'EOF'
Closes #2739

## What changed?

Adds MongoDB sink and source connectors as cdylib plugins for the existing
connector runtime. Follows the established patterns (PostgreSQL connector
as primary reference). No changes to the SDK or runtime code.

**Sink**: consumes Iggy messages → inserts into MongoDB collection.
**Source**: polls MongoDB collection → produces Iggy messages.

**Coverage**: 58 unit tests (33 source + 25 sink) + 8 E2E integration tests
using testcontainers + iggy_harness. All passing locally.

### Design decisions

| Decision | Choice | Why |
|---|---|---|
| Connection field | `connection_uri` | MongoDB's own Kafka Connector uses `connection.uri` |
| Batch API | `insert_many()` | `bulk_write()` needs Server 8.0+. Identical perf for append-only |
| Missing collection | Warn, don't fail | Kafka Connect, Debezium, Flink all do this |
| Retry logic | Typed `ErrorKind` matching | Matches postgres_sink's `is_transient_error` pattern. Only retries IO/network/pool errors — never auth failures, duplicate keys, or schema validation |

### Files

| Path | Lines | What |
|---|---|---|
| `sinks/mongodb_sink/src/lib.rs` | 651 | Sink plugin + 25 unit tests |
| `sources/mongodb_source/src/lib.rs` | 888 | Source plugin + 33 unit tests |
| `integration/tests/connectors/mongodb/` | 715 | 4 sink + 4 source E2E tests |
| `integration/tests/connectors/fixtures/mongodb/` | 656 | Test fixtures (container, harness) |
| `*/README.md` | 131+137 | Config docs + interactive "Try It" section |
| `*/config.toml` | 46+44 | Reference configs |

## Local execution

```
cargo fmt --all --check          # clean
cargo clippy -- -D warnings      # clean
cargo test -p iggy_connector_mongodb_sink   # 25/25
cargo test -p iggy_connector_mongodb_source # 33/33
cargo test --test mod --no-run   # E2E compiles clean
cargo machete                    # clean
cargo sort --workspace           # clean
```

Pre-commit hooks (prek) installed and passing.

## AI usage

Claude Code (Anthropic CLI) used for: research (industry patterns from
Kafka Connect, Debezium, Flink), implementation, test generation, PR
preparation. All code compiled and tested locally. E2E tests verified
against real MongoDB 7 via testcontainers.
EOF
)"
```

---

## Step 8: Post-PR Verification

After PR is created:

1. **Check CI status**: `gh pr checks <PR_NUMBER> --repo apache/iggy`
   - CI triggers: `pre-merge.yml` → `common` → `detect` → `test-rust`
   - Our connector changes trigger Rust checks (fmt, clippy, tests)
   - E2E tests may or may not run in CI (depends on Docker availability)

2. **Watch for bot comments**: Stale PR bot, license checker, etc.

3. **If CI fails on something we didn't catch locally**: Fix on branch, push again. The PR auto-updates.

---

## Potential Pitfalls (Mentor Notes)

### 1. prek hooks reject the commit
**Why**: Hooks run the full CI suite. If anything we missed fails, commit is rejected.
**Fix**: The commit didn't happen, so no damage. Fix the issue, re-stage, commit again (NEW commit, never amend).

### 2. CI fails on upstream code changes
**Why**: Someone merged to master between our `git fetch` and PR creation, introducing a conflict or new check.
**Fix**: Rebase onto latest master: `git fetch upstream && git rebase upstream/master`. Push force to branch (safe since it's our PR branch): `git push origin ab_202602_issue02 --force-with-lease`.

### 3. Maintainer asks to split the PR
**Why**: 3,765 lines from a first-time contributor. Despite precedent (Postgres +1,882, Pinot +2,312), some maintainers prefer smaller PRs.
**Fix**: Offer to split into PR1 (sink + source, ~2,100 lines) and PR2 (E2E tests, ~1,500 lines). But argue that E2E tests are the proof — the code review is harder without them.

### 4. Maintainer asks about the "docs/" folder
**Why**: No other connector has a docs folder.
**Actually**: The docs/ folder is NOT in this PR. It was moved to agent-room. No issue here.

### 5. `addlicense` check fails on READMEs
**Why**: Our README.md files don't have Apache license headers.
**Actually**: No other connector README has them either (stdout_sink, random_source, elasticsearch_sink all start with `# Title`). If CI flags this, it's a pre-existing issue across all connectors, not our problem.

### 6. Maintainer flags AI-generated code
**Why**: CONTRIBUTING.md warns about "proxy between maintainer and LLM" PRs.
**Counter**: We disclosed AI usage. We have 58 unit tests + 8 E2E tests. We found and fixed a real bug (sink retry logic) that the Postgres sink handles but we initially missed. The interactive "Try It" section lets them verify in 60 seconds. This is the opposite of a drive-by AI dump.

---

## The Sequence (TL;DR)

```
1. Fix 3 clippy errors in mongodb_source/src/lib.rs (test code)
2. Re-stage the file
3. Run full CI suite locally (all must pass)
4. Install prek + hooks
5. git commit -m "feat(connectors): add MongoDB sink and source connectors"
6. git push origin upstream/master:master          (sync fork)
7. git push origin ab_202602_issue02               (push branch)
8. gh pr create --repo apache/iggy ...             (create PR)
9. gh pr checks <number> --repo apache/iggy        (watch CI)
```

---

## Maintainer Review: What to Expect

### Most Likely Outcome: Clean Merge (1-3 days)
Based on prior connector PRs:
- Postgres #1959: merged with minimal comments
- Elasticsearch #1872: disaster due to contributor inexperience (we're the opposite)
- Iceberg #2191: merged quickly
- Pinot #2499: merged despite empty PR body

Our PR has:
- Test coverage that exceeds all prior connector PRs
- Interactive "Try It" section for quick verification
- Design decisions documented
- AI usage disclosed
- Following every CONTRIBUTING.md rule

### Possible Feedback Areas
1. **"Can you add X config option?"** — Easy, we can extend
2. **"Use bulk_write instead of insert_many"** — We have the rationale ready (Server 8.0 requirement)
3. **"Split the PR"** — We argue E2E tests are the proof
4. **"Change error handling"** — We already match postgres_sink pattern

### Worst Case: Long Review Cycle
If maintainer is busy or wants changes:
- Respond within 24 hours
- Make requested changes promptly
- Keep PR updated with master (rebase weekly if needed)
- Don't let it go stale
