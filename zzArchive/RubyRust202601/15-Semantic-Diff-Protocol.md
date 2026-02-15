# Semantic Diff Protocol

## Date: 2026-02-06

## Purpose

This document specifies how to **verify semantic equivalence** between a Rails application and its compiled Rust counterpart. The goal is to ensure that the Rust binary behaves identically to the Rails app for all tested inputs.

**The Problem**: Compilation correctness isn't just about compiling without errors — it's about producing the same behavior. A semantic diff tool compares Rails and Rust responses to detect divergence.

---

## Verification Architecture

```
                          ┌─────────────────┐
                          │   Test Suite    │
                          │  (Scenarios)    │
                          └────────┬────────┘
                                   │
                          ┌────────▼────────┐
                          │   Diff Driver   │
                          └────────┬────────┘
                                   │
              ┌────────────────────┴────────────────────┐
              │                                         │
     ┌────────▼────────┐                      ┌────────▼────────┐
     │   Rails App     │                      │   Rust Binary   │
     │ localhost:3000  │                      │ localhost:8000  │
     └────────┬────────┘                      └────────┬────────┘
              │                                         │
              │         ┌───────────────┐              │
              └────────►│  Comparator   │◄─────────────┘
                        └───────┬───────┘
                                │
                       ┌────────▼────────┐
                       │   Diff Report   │
                       └─────────────────┘
```

---

## Test Scenario Format

### Scenario Definition

```yaml
# scenarios/user_crud.yaml
name: User CRUD Operations
description: Test create, read, update, delete for User model

setup:
  # Database state before each test
  fixtures:
    - users:
        - id: 1
          email: alice@example.com
          name: Alice
          status: active
        - id: 2
          email: bob@example.com
          name: Bob
          status: suspended

tests:
  - name: List all users
    request:
      method: GET
      path: /api/v1/users
      headers:
        Accept: application/json
    expect:
      status: 200
      body:
        type: json
        match: exact
        value:
          - id: 1
            email: alice@example.com
            name: Alice
            status: active
          - id: 2
            email: bob@example.com
            name: Bob
            status: suspended

  - name: Get single user
    request:
      method: GET
      path: /api/v1/users/1
    expect:
      status: 200
      body:
        type: json
        match: subset
        value:
          id: 1
          email: alice@example.com

  - name: Create user with valid data
    request:
      method: POST
      path: /api/v1/users
      headers:
        Content-Type: application/json
      body:
        email: charlie@example.com
        name: Charlie
        password: secret123
    expect:
      status: 201
      body:
        type: json
        match: subset
        value:
          email: charlie@example.com
          name: Charlie
      db_state:
        users:
          - email: charlie@example.com
            name: Charlie

  - name: Create user with invalid email
    request:
      method: POST
      path: /api/v1/users
      body:
        email: not-an-email
        name: Invalid
    expect:
      status: 422
      body:
        type: json
        match: subset
        value:
          errors:
            email: ["is invalid"]

  - name: Update user
    request:
      method: PATCH
      path: /api/v1/users/1
      body:
        name: Alice Updated
    expect:
      status: 200
      db_state:
        users:
          - id: 1
            name: Alice Updated

  - name: Delete user
    request:
      method: DELETE
      path: /api/v1/users/2
    expect:
      status: 204
      db_state:
        users:
          absent:
            - id: 2

  - name: Get non-existent user
    request:
      method: GET
      path: /api/v1/users/999
    expect:
      status: 404
```

### Scenario Categories

| Category | Purpose | Example Tests |
|----------|---------|---------------|
| **CRUD** | Basic create/read/update/delete | User creation, listing, updating |
| **Validations** | Validation error messages | Invalid email, required fields |
| **Associations** | Related record behavior | User posts, nested resources |
| **Callbacks** | Side effect verification | Counter cache, timestamps |
| **Scopes** | Query behavior | Published posts, recent orders |
| **Authentication** | Auth flow equivalence | Login, token validation |
| **Edge Cases** | Boundary conditions | Empty results, large payloads |

---

## Comparison Modes

### Mode 1: Exact Match

Both responses must be byte-identical (after normalization).

```yaml
expect:
  body:
    match: exact
    value: { ... }
```

**Use for**: Static data, configuration endpoints

### Mode 2: Subset Match

Rails response must contain at least what Rust response contains.

```yaml
expect:
  body:
    match: subset
    value: { id: 1, name: "Alice" }
    # Rails can return more fields, Rust must have at least these
```

**Use for**: API responses where Rails might have extra fields

### Mode 3: Structural Match

Same structure, values may differ (e.g., timestamps, IDs).

```yaml
expect:
  body:
    match: structural
    schema:
      type: object
      properties:
        id: { type: integer }
        created_at: { type: string, format: datetime }
```

**Use for**: Responses with auto-generated values

### Mode 4: Semantic Match

Custom comparator function for complex equivalence.

```yaml
expect:
  body:
    match: semantic
    comparator: compare_user_response
```

```rust
fn compare_user_response(rails: &Value, rust: &Value) -> CompareResult {
    // Custom comparison logic
    // e.g., ignore order of array elements
}
```

**Use for**: Complex business logic, order-independent comparisons

---

## Response Normalization

Before comparison, responses are normalized to handle acceptable differences:

### Timestamp Normalization

```rust
fn normalize_timestamps(response: &mut Value) {
    // Convert all datetime strings to UTC
    // Round to second precision
    // Replace with placeholder if --ignore-timestamps
}
```

### ID Normalization

```rust
fn normalize_ids(response: &mut Value, id_map: &mut HashMap<i64, i64>) {
    // Map Rails IDs to Rust IDs if they differ
    // Maintain consistency within test
}
```

### Field Ordering

```rust
fn normalize_object_keys(response: &mut Value) {
    // Sort object keys alphabetically
    // Sort arrays by ID or deterministic key
}
```

### Whitespace Normalization

```rust
fn normalize_whitespace(response: &mut Value) {
    // Trim strings
    // Normalize newlines
}
```

---

## Database State Verification

Beyond HTTP responses, verify database state after operations:

### State Assertion

```yaml
expect:
  db_state:
    users:
      - id: 1
        name: Alice Updated
        updated_at: changed  # Special: verify it changed
    posts:
      count: 5  # Verify count without checking each record
    comments:
      absent:
        - id: 999  # Verify record was deleted
```

### Counter Cache Verification

```yaml
expect:
  db_state:
    users:
      - id: 1
        posts_count: 3  # Counter cache was incremented
```

### Timestamp Verification

```yaml
expect:
  db_state:
    posts:
      - id: 1
        updated_at: changed  # Verify touch worked
```

---

## Diff Report Format

### Console Output

```
═══════════════════════════════════════════════════════════════════════════════
                         SEMANTIC DIFF REPORT
═══════════════════════════════════════════════════════════════════════════════

Rails:  http://localhost:3000
Rust:   http://localhost:8000
Tests:  47 scenarios, 156 assertions

───────────────────────────────────────────────────────────────────────────────
                               RESULTS
───────────────────────────────────────────────────────────────────────────────

  ✓ 152 passed
  ✗ 4 failed
  ⊘ 0 skipped

───────────────────────────────────────────────────────────────────────────────
                               FAILURES
───────────────────────────────────────────────────────────────────────────────

┌─────────────────────────────────────────────────────────────────────────────┐
│ FAIL: User CRUD > Create user with invalid email                            │
├─────────────────────────────────────────────────────────────────────────────┤
│ Request:                                                                    │
│   POST /api/v1/users                                                        │
│   Body: { "email": "not-an-email", "name": "Invalid" }                      │
│                                                                             │
│ Expected status: 422                                                        │
│ Rails status:    422 ✓                                                      │
│ Rust status:     422 ✓                                                      │
│                                                                             │
│ Body diff:                                                                  │
│   Rails:                                                                    │
│   {                                                                         │
│     "errors": {                                                             │
│       "email": ["is invalid"]                                               │
│     }                                                                       │
│   }                                                                         │
│                                                                             │
│   Rust:                                                                     │
│   {                                                                         │
│     "errors": {                                                             │
│       "email": ["is not a valid email"]                                     │
│     }                                                                       │
│   }                                                                         │
│                                                                             │
│ Difference:                                                                 │
│   - errors.email[0]: "is invalid" → "is not a valid email"                  │
│                                                                             │
│ Severity: LOW (error message wording differs, behavior correct)             │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│ FAIL: Order Processing > Calculate total with discount                      │
├─────────────────────────────────────────────────────────────────────────────┤
│ Request:                                                                    │
│   GET /api/v1/orders/1                                                      │
│                                                                             │
│ Body diff:                                                                  │
│   Rails:                                                                    │
│   { "total": "99.99", "subtotal": "109.99", "discount": "10.00" }           │
│                                                                             │
│   Rust:                                                                     │
│   { "total": "99.98", "subtotal": "109.99", "discount": "10.01" }           │
│                                                                             │
│ Difference:                                                                 │
│   - total: 99.99 → 99.98 (0.01 off)                                         │
│   - discount: 10.00 → 10.01 (0.01 off)                                      │
│                                                                             │
│ Severity: HIGH (monetary calculation differs)                               │
│ Note: Possible floating point rounding difference                           │
└─────────────────────────────────────────────────────────────────────────────┘

───────────────────────────────────────────────────────────────────────────────
                               SUMMARY
───────────────────────────────────────────────────────────────────────────────

Pass rate: 97.4% (152/156)

By severity:
  HIGH:   1 (monetary calculation)
  MEDIUM: 1 (behavior difference)
  LOW:    2 (message wording)

Recommendation: Fix HIGH severity issues before deployment.
```

### JSON Report

```json
{
  "summary": {
    "rails_url": "http://localhost:3000",
    "rust_url": "http://localhost:8000",
    "total_scenarios": 47,
    "total_assertions": 156,
    "passed": 152,
    "failed": 4,
    "skipped": 0,
    "pass_rate": 97.4
  },
  "failures": [
    {
      "scenario": "User CRUD",
      "test": "Create user with invalid email",
      "request": {
        "method": "POST",
        "path": "/api/v1/users",
        "body": {
          "email": "not-an-email",
          "name": "Invalid"
        }
      },
      "rails": {
        "status": 422,
        "body": {
          "errors": {
            "email": ["is invalid"]
          }
        }
      },
      "rust": {
        "status": 422,
        "body": {
          "errors": {
            "email": ["is not a valid email"]
          }
        }
      },
      "diff": {
        "type": "value_mismatch",
        "path": "errors.email[0]",
        "rails_value": "is invalid",
        "rust_value": "is not a valid email"
      },
      "severity": "LOW",
      "category": "error_message_wording"
    }
  ],
  "by_category": {
    "crud": { "passed": 45, "failed": 0 },
    "validations": { "passed": 32, "failed": 2 },
    "associations": { "passed": 28, "failed": 0 },
    "callbacks": { "passed": 20, "failed": 1 },
    "scopes": { "passed": 27, "failed": 1 }
  }
}
```

---

## Severity Classification

### HIGH Severity

Differences that affect correctness:

| Issue | Example |
|-------|---------|
| Wrong status code | 200 vs 404 |
| Missing data | Field not returned |
| Wrong calculation | Price calculation off |
| Data corruption | Wrong record modified |
| Security issue | Auth bypass |

**Action**: Must fix before deployment

### MEDIUM Severity

Differences that affect behavior but not correctness:

| Issue | Example |
|-------|---------|
| Different ordering | Array in different order |
| Extra fields | Rust returns more than Rails |
| Timing difference | Timestamps slightly off |

**Action**: Review and decide if acceptable

### LOW Severity

Cosmetic differences:

| Issue | Example |
|-------|---------|
| Error message wording | "is invalid" vs "is not valid" |
| Whitespace | Trailing newline |
| Field casing | `created_at` vs `createdAt` |

**Action**: Often acceptable, document if intentional

---

## CLI Usage

```bash
rails-compile verify [OPTIONS]

Options:
  --rails-url <URL>     Rails app URL [default: http://localhost:3000]
  --rust-url <URL>      Rust app URL [default: http://localhost:8000]
  --scenarios <DIR>     Scenarios directory [default: ./scenarios]
  --output <FILE>       Write report to file
  --format <FORMAT>     Output format: text, json [default: text]
  --fail-on <SEVERITY>  Exit with error if severity >= threshold [default: high]
  --parallel <N>        Run N tests in parallel [default: 4]
  --reset-db            Reset database before each scenario
  --verbose             Show request/response details

Examples:
  # Basic verification
  rails-compile verify

  # Strict mode (fail on any difference)
  rails-compile verify --fail-on low

  # CI mode with JSON report
  rails-compile verify --format json --output report.json --fail-on high
```

---

## Workflow Integration

### Pre-Deployment Check

```yaml
# .github/workflows/verify.yml
name: Semantic Verification

on:
  push:
    branches: [main]

jobs:
  verify:
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:15
        env:
          POSTGRES_PASSWORD: postgres
        ports:
          - 5432:5432

    steps:
      - uses: actions/checkout@v3

      - name: Start Rails
        run: |
          bundle install
          rails db:setup
          rails server -d -p 3000

      - name: Start Rust
        run: |
          cargo build --release
          ./target/release/my_app &
          sleep 5

      - name: Run verification
        run: rails-compile verify --fail-on high --format json --output report.json

      - name: Upload report
        uses: actions/upload-artifact@v3
        with:
          name: semantic-diff-report
          path: report.json
```

### Continuous Verification

Run verification on every PR to catch regressions:

```yaml
on:
  pull_request:
    paths:
      - 'app/models/**'
      - 'rust_app/src/**'

jobs:
  semantic-diff:
    # ... same as above
```

---

## Edge Cases

### Handling Non-Determinism

#### Random Values

```yaml
tests:
  - name: Create with random token
    request:
      method: POST
      path: /api/v1/tokens
    expect:
      body:
        match: structural
        ignore:
          - token  # Ignore random token value
```

#### Timestamps

```yaml
tests:
  - name: Record has timestamp
    expect:
      body:
        match: structural
        value:
          created_at:
            type: datetime
            tolerance: 5s  # Within 5 seconds
```

### Handling Side Effects

#### Emails

```yaml
tests:
  - name: Create user sends welcome email
    request:
      method: POST
      path: /api/v1/users
      body:
        email: test@example.com
    expect:
      status: 201
      side_effects:
        emails:
          - to: test@example.com
            subject: Welcome!
```

#### Background Jobs

```yaml
tests:
  - name: Order triggers fulfillment job
    request:
      method: POST
      path: /api/v1/orders/1/confirm
    expect:
      status: 200
      side_effects:
        jobs:
          - class: FulfillmentJob
            args:
              order_id: 1
```

---

## Best Practices

### 1. Start with CRUD

Begin verification with basic CRUD operations — they're the most important and easiest to test.

### 2. Test Validations Explicitly

Validation error messages often differ. Decide upfront if exact match is required or if "same behavior" is sufficient.

### 3. Test Edge Cases

Include tests for:
- Empty results
- Large payloads
- Special characters
- Unicode
- Null/missing fields

### 4. Version Your Scenarios

Scenarios are part of the migration — commit them alongside code changes.

### 5. Document Intentional Differences

If Rails and Rust intentionally differ (e.g., better error messages in Rust), document it in the scenario:

```yaml
tests:
  - name: Invalid email error
    expect:
      body:
        match: semantic
        note: "Rust uses more descriptive error messages"
```

---

## Summary

The semantic diff protocol ensures that compiled Rust code behaves identically to the original Rails application:

1. **Define scenarios** in YAML with expected requests/responses
2. **Run both apps** against the same database
3. **Compare responses** with configurable matching modes
4. **Generate reports** with severity classification
5. **Integrate with CI** to catch regressions

This is the **final verification step** before sunsetting the Rails application. If the semantic diff passes, the Rust binary is ready for production.
