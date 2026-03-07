# Iggy Code Review Standards

## Overview

This document captures the code review standards and conventions established through PR discussions in the Apache Iggy project.

---

## 1. PR Requirements

### Template Sections

| Section | Purpose |
|---------|---------|
| **Which issue does this PR close?** | Link related issues (e.g., `Closes #123`) |
| **Rationale** | Explain WHY the change is needed |
| **What changed?** | 2-4 sentences: problem first, then solution |
| **Local Execution** | Confirm code ran locally, pre-commit hooks passed |
| **AI Usage** | Declare any AI tools used, scope, verification method |

### Example Rationale

> Messages were unavailable when background message_saver committed the journal and started async disk I/O before completion. This PR ensures messages are available by completing the journal commit synchronously before async persistence.

---

## 2. Approval Requirements

- **At least 2 approvals** required for merge
- Maintainers provide final approval
- All CI checks must pass

---

## 3. Code Review Patterns

### Technical Deep-Dives

Reviewers often:
- Suggest alternative implementations
- Request benchmarks for performance changes
- Ask about edge cases

### Example Review Discussion

> **Reviewer**: "Where are tests?"
> 
> **Response**: Tests tracked in separate issue #2807, linked in the PR description.

---

## 4. Quality Gates

### Rust Quality Checks

```bash
cargo fmt --all
cargo clippy --all-targets --all-features -- -D warnings
cargo build
cargo test
cargo machete
cargo sort --workspace
```

### Pre-commit Hooks (prek)

```bash
cargo install prek
prek install
```

### Typos Check

```bash
cargo install typos-cli --locked
typos
typos --write-changes
```

---

## 5. Size Limits

### For New Contributors

- PRs under 500 lines of code
- Single purpose per PR
- Split large changes into multiple PRs

### Example Feedback

> "3000+ LoC is definitely too large to review! The byte operations are easy to go wrong in future edits, thus testing could be helpful!"

---

## 6. High-Risk Areas

These require design discussion in the issue **before** coding:

- Persistence (segments, indexes, state, crash recovery)
- Protocol (binary format, wire encoding)
- Concurrency (shards, inter-shard)
- Public API (HTTP, SDKs, CLI)
- Connectors

---

## 7. Commit Message Format

### Pattern: type(scope): subject

```
feat(server): add consumer group rebalancing
fix(protocol): handle connection timeout correctly
refactor(client): extract common retry logic
perf(storage): optimize message polling
docs(readme): update installation instructions
ci(actions): add coverage reporting
```

### Good Examples from Repository

```
fix(server): prevent panic when segment rotates during async persistence
fix(server): chunk vectored writes to avoid exceeding IOV_MAX limit
feat(server): add SegmentedSlab collection
refactor(server): consolidate permissions into metadata crate
chore(integration): remove streaming tests superseded by API-level coverage
```

---

## 8. Testing Requirements

| Aspect | Standard |
|--------|----------|
| **Coverage** | Codecov integration tracks all PRs |
| **Local testing** | **MANDATORY** - "Relying on CI is not acceptable" |
| **Test coordination** | Tests may be in separate issues/PRs if acknowledged |
| **Flaky tests** | Acknowledge and create separate issues |

---

## 9. Performance PR Requirements

### Required for Performance Changes

- **Before/after benchmarks**
- **Hardware specs and test configuration**
- **Visual charts when possible**

### Example Benchmark Report

```
Bench: Apple M4, macOS 15.7.4
Test: pinned-producer/TCP
Config: 8 producers, 8 streams, 1000B msgs, 1000 msgs/batch

Before: 2.1M msg/sec, p99 latency 850µs
After:  2.8M msg/sec, p99 latency 420µs
Improvement: 33% throughput, 50% latency reduction
```

---

## 10. AI Usage Disclosure

| Requirement | Details |
|-------------|---------|
| **Mandatory declaration** | List tools used (Copilot, Claude, ChatGPT, etc.) |
| **Scope** | Describe extent (autocomplete, generated functions, entire implementation) |
| **Verification** | Explain how generated code was verified |
| **Accountability** | "Can you explain every line of the code if asked?" |

---

## 11. Close Policy

PRs may be closed if:

- Maintainer feels like proxy between maintainer and LLM
- No approved issue or no approval from a maintainer
- Code not ran and tested locally
- Mixed purposes or purposes not clear
- Can't answer questions about the change
- Inactivity for longer than 7 days

---

## 12. Multi-SDK Consistency

The project maintains SDKs in multiple languages:

- Rust (core)
- Go (`foreign/go/`)
- C# (`foreign/csharp/`)
- Java (`foreign/java/`)
- Python (`foreign/python/`)
- Node.js (`foreign/node/`)
- C++ (`foreign/cpp/`)

### Pattern

New features should follow patterns from existing SDKs.

### Example

> TLS implementation in Go SDK followed patterns from Rust, Java, C#, and Node.js SDKs.

---

## 13. Comment Style

### WHY, Not WHAT

```rust
// Bad: Increment counter
counter += 1;

// Good: Offset by 1 because segment IDs are 1-indexed in the wire protocol
counter += 1;
```

Don't comment obvious code. Do explain non-obvious decisions, invariants, and constraints.

---

## 14. Formatting Notes

### cargo-sort and taplo Conflict

> `cargo-sort` and `taplo` can conflict on `features` formatting - project added `--no-format` flag to resolve.

```bash
cargo sort --workspace --no-format
```

---

## Summary: PR Checklist

- [ ] Link to approved issue
- [ ] Clear rationale explaining WHY
- [ ] Run code locally before submitting
- [ ] Install and run `prek` pre-commit hooks
- [ ] Include benchmarks for performance changes
- [ ] Follow patterns from existing SDK implementations
- [ ] Declare any AI tools used
- [ ] Be prepared to split large PRs
- [ ] Ensure at least 2 reviewers approve
- [ ] Keep subject under 72 chars
- [ ] Use conventional commit format
