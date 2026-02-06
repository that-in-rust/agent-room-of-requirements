# Lint Tool Specification

## Date: 2026-02-06

## Purpose

The `rails-compile lint` command analyzes a Rails project and reports:
1. **What can be compiled** automatically
2. **What requires changes** to be compilable (Proc Embargo violations)
3. **What requires manual porting** (business logic, dynamic patterns)
4. **Overall migration effort estimate**

This document specifies exactly what the lint tool checks and how it reports results.

---

## Usage

```bash
rails-compile lint [OPTIONS] [PATH]

Arguments:
  [PATH]  Path to Rails project root [default: .]

Options:
  --format <FORMAT>   Output format: text, json, sarif [default: text]
  --output <FILE>     Write report to file instead of stdout
  --fix               Auto-fix Proc Embargo violations where possible
  --strict            Exit with error if any violations found
  --verbose           Show detailed analysis
  --model <NAME>      Only lint specific model(s)
```

---

## Report Structure

### Summary Section

```
═══════════════════════════════════════════════════════════════════════════════
                          RAILS COMPILE LINT REPORT
═══════════════════════════════════════════════════════════════════════════════

Project: my_rails_app
Path:    /Users/dev/my_rails_app
Mode:    Static

───────────────────────────────────────────────────────────────────────────────
                               SUMMARY
───────────────────────────────────────────────────────────────────────────────

Models:           42
Tables:           45 (3 join tables)
Associations:     127
Validations:      89
Callbacks:        34
Scopes:           56
Enums:            12

COMPILABILITY:
  ✓ Fully Compilable:     31 models (73.8%)
  ⚠ Needs Changes:        8 models  (19.0%)
  ✗ Requires Manual Port: 3 models  (7.1%)

ESTIMATED EFFORT:
  Auto-fixable:           23 issues
  Manual changes:         12 issues
  Business logic to port: 847 lines
```

### Detailed Model Report

```
───────────────────────────────────────────────────────────────────────────────
                               MODELS
───────────────────────────────────────────────────────────────────────────────

┌─────────────────────────────────────────────────────────────────────────────┐
│ ✓ User (app/models/user.rb)                                    [COMPILABLE] │
├─────────────────────────────────────────────────────────────────────────────┤
│ Columns:       8 (id, email, name, role, status, org_id, created, updated)  │
│ Associations:  3 (has_many :posts, belongs_to :organization, has_one :profile)│
│ Validations:   4 (all static)                                               │
│ Callbacks:     2 (all use symbol conditions)                                │
│ Scopes:        3 (all static)                                               │
│ Enums:         2 (role, status)                                             │
│                                                                             │
│ Notes: None. Model is fully compilable.                                     │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│ ⚠ Comment (app/models/comment.rb)                           [NEEDS CHANGES] │
├─────────────────────────────────────────────────────────────────────────────┤
│ Columns:       6 (id, body, author_id, commentable_id, commentable_type, ...)│
│ Associations:  2                                                            │
│ Validations:   3                                                            │
│ Callbacks:     1                                                            │
│ Scopes:        2                                                            │
│                                                                             │
│ ISSUES:                                                                     │
│                                                                             │
│   [PROC-EMBARGO] Line 12: Proc condition on callback                        │
│   │ before_save :sanitize_body, if: -> { body_changed? && body.length > 100 }│
│   │                                                                         │
│   │ FIX: Extract proc to named method                                       │
│   │ - before_save :sanitize_body, if: :should_sanitize_body?                │
│   │ + def should_sanitize_body?                                             │
│   │ +   body_changed? && body.length > 100                                  │
│   │ + end                                                                   │
│   │                                                                         │
│   │ Auto-fix available: --fix                                               │
│                                                                             │
│   [POLYMORPHIC] Line 5: Open polymorphic type set                           │
│   │ belongs_to :commentable, polymorphic: true                              │
│   │                                                                         │
│   │ Types found via inverse scan: Post, Image, Video                        │
│   │ Add annotation or migrate to delegated_type:                            │
│   │                                                                         │
│   │ Option A: Add compiler annotation                                       │
│   │ # @polymorphic_types [Post, Image, Video]                               │
│   │ belongs_to :commentable, polymorphic: true                              │
│   │                                                                         │
│   │ Option B: Use delegated_type (recommended)                              │
│   │ delegated_type :commentable, types: %w[Post Image Video]                │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│ ✗ Order (app/models/order.rb)                         [REQUIRES MANUAL PORT]│
├─────────────────────────────────────────────────────────────────────────────┤
│ Columns:       12                                                           │
│ Associations:  5                                                            │
│ Validations:   7                                                            │
│ Callbacks:     4                                                            │
│ Scopes:        6                                                            │
│ Business Logic: 234 lines                                                   │
│                                                                             │
│ ISSUES:                                                                     │
│                                                                             │
│   [PROC-EMBARGO] Line 23: Complex proc condition                            │
│   │ validate :inventory_available, if: -> {                                 │
│   │   status_changed? && status == 'confirmed' && warehouse.active?         │
│   │ }                                                                       │
│   │                                                                         │
│   │ FIX: Extract to named method (requires manual review)                   │
│                                                                             │
│   [RUNTIME-VALUE] Line 45: Scope with runtime value                         │
│   │ scope :recent, -> { where("created_at > ?", 1.week.ago) }               │
│   │                                                                         │
│   │ This scope uses Time.now (via 1.week.ago). The generated Rust           │
│   │ code will use Utc::now() which may have different behavior.             │
│   │                                                                         │
│   │ Action: Review and confirm behavior is acceptable                       │
│                                                                             │
│   [BUSINESS-LOGIC] Lines 67-145: calculate_total method                     │
│   │ def calculate_total                                                     │
│   │   items.sum { |i| i.price * i.quantity } + shipping + tax               │
│   │ end                                                                     │
│   │                                                                         │
│   │ This method contains business logic that must be manually ported.       │
│   │ A todo!() stub will be generated.                                       │
│                                                                             │
│   [BUSINESS-LOGIC] Lines 150-198: process_payment method                    │
│   │ External service call (Stripe). Requires manual port.                   │
│                                                                             │
│   [BUSINESS-LOGIC] Lines 203-234: send_confirmation_email callback          │
│   │ Mailer call. Requires manual port.                                      │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Issue Categories

### Category 1: Proc Embargo Violations

Patterns that use procs/lambdas where the compiler requires symbols.

#### 1.1 Proc Conditions on Callbacks

```ruby
# VIOLATION
before_save :check_inventory, if: -> { quantity_changed? && warehouse.active? }

# FIX (auto-fixable)
before_save :check_inventory, if: :should_check_inventory?

def should_check_inventory?
  quantity_changed? && warehouse.active?
end
```

**Detection**: Look for `if:` or `unless:` options with `->`/`proc`/`Proc.new`

**Auto-fix**: Extract proc body to named method, replace with symbol

**Complexity**: LOW — mechanical transformation

#### 1.2 Proc Conditions on Validations

```ruby
# VIOLATION
validates :discount, presence: true, if: -> { premium_user? && order_total > 100 }

# FIX (auto-fixable)
validates :discount, presence: true, if: :requires_discount?

def requires_discount?
  premium_user? && order_total > 100
end
```

**Detection**: Same as callbacks

**Auto-fix**: Same as callbacks

**Complexity**: LOW

#### 1.3 Complex Proc in Association Callbacks

```ruby
# VIOLATION
has_many :items, before_add: ->(order, item) { item.price ||= lookup_price(item) }

# FIX (manual)
has_many :items, before_add: :set_item_price

def set_item_price(item)
  item.price ||= lookup_price(item)
end
```

**Detection**: Look for `before_add`/`after_add`/`before_remove`/`after_remove` with procs

**Auto-fix**: Possible but complex (two parameters)

**Complexity**: MEDIUM

### Category 2: Polymorphic Type Resolution

#### 2.1 Open Polymorphic Associations

```ruby
# VIOLATION
belongs_to :imageable, polymorphic: true
# No way to know what types are valid at compile time

# FIX Option A: Compiler annotation
# @polymorphic_types [User, Post, Comment]
belongs_to :imageable, polymorphic: true

# FIX Option B: Migrate to delegated_type
delegated_type :imageable, types: %w[User Post Comment]
```

**Detection**: `polymorphic: true` without `# @polymorphic_types` annotation

**Auto-fix**: Can suggest types from inverse association scan

**Complexity**: MEDIUM — requires codebase scan or DB query

#### 2.2 STI Without Known Subclasses

```ruby
# base model
class Vehicle < ApplicationRecord
end

# PROBLEM: Subclasses may be in any file
class Car < Vehicle; end
class Truck < Vehicle; end
class Motorcycle < Vehicle; end
```

**Detection**: Model with `type` column but no explicit subclass list

**Resolution**: Scan for inheriting classes or query `DISTINCT type` from DB

**Complexity**: LOW — just needs codebase scan

### Category 3: Runtime Values

#### 3.1 Time-Based Scopes

```ruby
# WARNING
scope :recent, -> { where("created_at > ?", 1.week.ago) }
scope :today, -> { where(created_at: Date.today.all_day) }
scope :this_month, -> { where(created_at: Time.current.all_month) }
```

**Detection**: Calls to `Time.now`, `Date.today`, `1.week.ago`, etc. in scopes

**Action**: Generate code with `Utc::now()`, flag for review

**Complexity**: LOW — just needs warning

#### 3.2 Current User/Tenant Scopes

```ruby
# VIOLATION — cannot compile
scope :mine, -> { where(user_id: Current.user.id) }
scope :in_account, -> { where(account_id: Current.account_id) }
default_scope { where(tenant_id: Current.tenant_id) }
```

**Detection**: References to `Current.*` in scopes/default_scope

**Action**: Generate method with parameter, flag as breaking change

**Complexity**: HIGH — changes method signature

#### 3.3 Dynamic Class Names

```ruby
# VIOLATION
belongs_to :owner, class_name: -> { determine_owner_class }
has_many :items, class_name: ENV['ITEM_CLASS'] || 'Item'
```

**Detection**: `class_name` option with non-string value

**Action**: Error — cannot compile

**Complexity**: N/A — must be fixed manually

### Category 4: Business Logic

#### 4.1 Custom Methods

```ruby
def calculate_total
  items.sum(&:subtotal) + shipping_cost + tax_amount - discount
end
```

**Detection**: Any method that is not a Rails DSL macro

**Action**: Generate `todo!()` stub, count lines

**Complexity**: MANUAL — requires human porting

#### 4.2 External Service Calls

```ruby
def charge_payment
  Stripe::Charge.create(
    amount: total_cents,
    source: payment_method.token,
    customer: user.stripe_customer_id
  )
end
```

**Detection**: Calls to external gems/services

**Action**: Flag for manual port, suggest Rust equivalents if known

**Complexity**: MANUAL

#### 4.3 Mailer Calls

```ruby
after_create :send_welcome_email

def send_welcome_email
  UserMailer.welcome(self).deliver_later
end
```

**Detection**: Calls to `*Mailer.*`

**Action**: Flag for manual port (suggest lettre/sendgrid crate)

**Complexity**: MANUAL

### Category 5: Unsupported Patterns

#### 5.1 Abstract Classes

```ruby
class ApplicationRecord < ActiveRecord::Base
  self.abstract_class = true
end
```

**Detection**: `self.abstract_class = true`

**Action**: Skip compilation (it's not a real model)

**Complexity**: N/A

#### 5.2 Tableless Models

```ruby
class ContactForm
  include ActiveModel::Model
  # No table
end
```

**Detection**: No corresponding table in schema

**Action**: Generate struct without Diesel derive macros

**Complexity**: LOW

#### 5.3 Monkey Patches

```ruby
# In config/initializers/extensions.rb
class String
  def to_slug
    downcase.gsub(/\s+/, '-')
  end
end
```

**Detection**: Class reopening outside app/models

**Action**: Flag — cannot compile monkey patches

**Complexity**: MANUAL

---

## Metrics Collected

### Per-Model Metrics

| Metric | Description |
|--------|-------------|
| `columns` | Number of database columns |
| `associations` | Number of association declarations |
| `validations` | Number of validation declarations |
| `callbacks` | Number of callback declarations |
| `scopes` | Number of scope declarations |
| `enums` | Number of enum declarations |
| `methods` | Number of custom methods |
| `lines` | Lines of code in model file |
| `business_logic_lines` | Lines of custom methods (need manual port) |

### Per-Model Status

| Status | Meaning |
|--------|---------|
| `COMPILABLE` | No issues, can compile automatically |
| `NEEDS_CHANGES` | Has Proc Embargo violations that can be fixed |
| `REQUIRES_MANUAL_PORT` | Has business logic or unsupported patterns |

### Project-Wide Metrics

| Metric | Description |
|--------|-------------|
| `total_models` | Count of model files |
| `total_tables` | Count of database tables |
| `total_associations` | Sum of all associations |
| `total_validations` | Sum of all validations |
| `total_callbacks` | Sum of all callbacks |
| `total_scopes` | Sum of all scopes |
| `total_enums` | Sum of all enums |
| `compilable_models` | Count with COMPILABLE status |
| `needs_changes_models` | Count with NEEDS_CHANGES status |
| `manual_port_models` | Count with REQUIRES_MANUAL_PORT status |
| `proc_embargo_violations` | Count of Proc Embargo issues |
| `auto_fixable_issues` | Count of issues --fix can resolve |
| `business_logic_lines` | Total lines requiring manual port |

---

## JSON Output Format

```json
{
  "project": {
    "name": "my_rails_app",
    "path": "/Users/dev/my_rails_app",
    "mode": "static"
  },
  "summary": {
    "total_models": 42,
    "total_tables": 45,
    "total_associations": 127,
    "total_validations": 89,
    "total_callbacks": 34,
    "total_scopes": 56,
    "total_enums": 12,
    "compilable_models": 31,
    "needs_changes_models": 8,
    "manual_port_models": 3,
    "compilable_percentage": 73.8,
    "proc_embargo_violations": 23,
    "auto_fixable_issues": 23,
    "business_logic_lines": 847
  },
  "models": [
    {
      "name": "User",
      "path": "app/models/user.rb",
      "status": "COMPILABLE",
      "metrics": {
        "columns": 8,
        "associations": 3,
        "validations": 4,
        "callbacks": 2,
        "scopes": 3,
        "enums": 2,
        "methods": 0,
        "lines": 45,
        "business_logic_lines": 0
      },
      "issues": []
    },
    {
      "name": "Comment",
      "path": "app/models/comment.rb",
      "status": "NEEDS_CHANGES",
      "metrics": {
        "columns": 6,
        "associations": 2,
        "validations": 3,
        "callbacks": 1,
        "scopes": 2,
        "enums": 0,
        "methods": 1,
        "lines": 32,
        "business_logic_lines": 0
      },
      "issues": [
        {
          "type": "PROC_EMBARGO",
          "subtype": "callback_condition",
          "line": 12,
          "code": "before_save :sanitize_body, if: -> { body_changed? && body.length > 100 }",
          "message": "Proc condition on callback",
          "auto_fixable": true,
          "fix": {
            "original": "before_save :sanitize_body, if: -> { body_changed? && body.length > 100 }",
            "replacement": "before_save :sanitize_body, if: :should_sanitize_body?",
            "add_method": {
              "name": "should_sanitize_body?",
              "body": "body_changed? && body.length > 100"
            }
          }
        },
        {
          "type": "POLYMORPHIC",
          "subtype": "open_type_set",
          "line": 5,
          "code": "belongs_to :commentable, polymorphic: true",
          "message": "Open polymorphic type set",
          "auto_fixable": false,
          "detected_types": ["Post", "Image", "Video"],
          "suggestions": [
            {
              "approach": "annotation",
              "code": "# @polymorphic_types [Post, Image, Video]\nbelongs_to :commentable, polymorphic: true"
            },
            {
              "approach": "delegated_type",
              "code": "delegated_type :commentable, types: %w[Post Image Video]"
            }
          ]
        }
      ]
    },
    {
      "name": "Order",
      "path": "app/models/order.rb",
      "status": "REQUIRES_MANUAL_PORT",
      "metrics": {
        "columns": 12,
        "associations": 5,
        "validations": 7,
        "callbacks": 4,
        "scopes": 6,
        "enums": 1,
        "methods": 5,
        "lines": 267,
        "business_logic_lines": 234
      },
      "issues": [
        {
          "type": "BUSINESS_LOGIC",
          "subtype": "custom_method",
          "line": 67,
          "end_line": 145,
          "code": "def calculate_total...",
          "message": "Custom method requires manual porting",
          "auto_fixable": false,
          "lines_affected": 78
        }
      ]
    }
  ]
}
```

---

## SARIF Output Format

For IDE integration (VS Code, IntelliJ), the tool outputs [SARIF](https://sarifweb.azurewebsites.net/):

```json
{
  "$schema": "https://raw.githubusercontent.com/oasis-tcs/sarif-spec/master/Schemata/sarif-schema-2.1.0.json",
  "version": "2.1.0",
  "runs": [
    {
      "tool": {
        "driver": {
          "name": "rails-compile",
          "version": "0.1.0",
          "rules": [
            {
              "id": "PROC001",
              "name": "ProcConditionOnCallback",
              "shortDescription": {
                "text": "Proc condition on callback"
              },
              "fullDescription": {
                "text": "Callbacks with proc conditions cannot be compiled. Use a named method instead."
              },
              "defaultConfiguration": {
                "level": "warning"
              }
            }
          ]
        }
      },
      "results": [
        {
          "ruleId": "PROC001",
          "level": "warning",
          "message": {
            "text": "Proc condition on callback: before_save :sanitize_body, if: -> { body_changed? && body.length > 100 }"
          },
          "locations": [
            {
              "physicalLocation": {
                "artifactLocation": {
                  "uri": "app/models/comment.rb"
                },
                "region": {
                  "startLine": 12,
                  "startColumn": 3
                }
              }
            }
          ],
          "fixes": [
            {
              "description": {
                "text": "Extract proc to named method"
              },
              "artifactChanges": [
                {
                  "artifactLocation": {
                    "uri": "app/models/comment.rb"
                  },
                  "replacements": [
                    {
                      "deletedRegion": {
                        "startLine": 12,
                        "startColumn": 3,
                        "endLine": 12,
                        "endColumn": 80
                      },
                      "insertedContent": {
                        "text": "before_save :sanitize_body, if: :should_sanitize_body?"
                      }
                    }
                  ]
                }
              ]
            }
          ]
        }
      ]
    }
  ]
}
```

---

## Auto-Fix Capability

The `--fix` flag automatically applies fixes to Proc Embargo violations:

### What Can Be Auto-Fixed

1. **Proc conditions on callbacks** → Extract to named method
2. **Proc conditions on validations** → Extract to named method
3. **Simple proc callbacks** → Convert to method reference

### What Cannot Be Auto-Fixed

1. **Polymorphic type sets** — Needs human decision
2. **Runtime values** — Needs human review
3. **Business logic** — Needs manual porting
4. **Complex procs with parameters** — May need refactoring

### Fix Application

```bash
# Preview fixes without applying
rails-compile lint --fix --dry-run

# Apply fixes
rails-compile lint --fix

# Apply fixes and commit
rails-compile lint --fix && git commit -am "Fix Proc Embargo violations"
```

---

## Exit Codes

| Code | Meaning |
|------|---------|
| 0 | Success, no issues found |
| 1 | Issues found (warnings) |
| 2 | Critical issues found (errors with --strict) |
| 3 | Parse error in Rails project |
| 4 | Invalid arguments |

---

## Integration

### CI/CD Integration

```yaml
# GitHub Actions
- name: Lint Rails for Rust compilation
  run: rails-compile lint --format sarif --output lint.sarif --strict

- name: Upload SARIF
  uses: github/codeql-action/upload-sarif@v2
  with:
    sarif_file: lint.sarif
```

### Pre-Commit Hook

```bash
#!/bin/bash
# .git/hooks/pre-commit
rails-compile lint --strict app/models/
```

### VS Code Extension

The SARIF output integrates with VS Code's Problems panel, showing issues inline with suggested fixes.

---

## Summary

The lint tool is the **first point of contact** for a Rails-to-Rust migration:

1. **Run lint** to understand the codebase
2. **Apply auto-fixes** for Proc Embargo violations
3. **Address warnings** for polymorphic/STI/runtime values
4. **Estimate effort** for business logic porting
5. **Track progress** with CI/CD integration

The lint tool doesn't compile anything — it just reports. This makes it safe to run on any Rails project without side effects.
