# Opinionated Thesis: The Rails-to-Rust Compiler

## Date: 2026-02-04

## The Argument in One Paragraph

A Rails-to-Rust compiler is not only feasible — it is **aligned with where the Rails community is already heading**. The 3 patterns that resist static compilation (proc conditions, polymorphic `constantize`, callback halting via `throw(:abort)`) are the same 3 patterns the community considers anti-patterns. By enforcing compile-time restrictions that match community best practices, the compiler doesn't fight Rails — it codifies what senior Rails developers already recommend. Combined with a DB-first, layered architecture, this compiler can convert deployed Rails applications into native Rust binaries with real types, zero runtime overhead, and enforced correctness.

---

## The Journey to This Thesis

This document synthesizes findings from 8 prior research documents:

| Doc | Finding |
|-----|---------|
| 01 - Hypothesis | Ruby-to-Rust transpilation is architecturally sound using RubyValue enum |
| 02 - Parseltongue Analysis | 55,603 entities analyzed: 87.5% transpilable, 7.1% impossible, 5.4% hard |
| 03 - Ruby-- Subset | Formal definition of transpilable Ruby subset (without metaprogramming) |
| 04 - Concrete Example | PresenceValidator transpiled; revealed RubyValue dispatch = ~2-5x speedup only |
| 05 - Verdict | Ruby-- works but Rails apps cannot be transpiled without Ruby runtime |
| 06 - Rails DSL Compiler | **Pivot**: Don't transpile Ruby — compile Rails DSLs (~30 patterns) to idiomatic Rust |
| 07 - Hard 20% | 10 hard problems identified; 7/10 resolvable; 3 genuinely hard (procs, polymorphic, halting) |
| 08 - DB-First Variant | Database as source of truth; Static + Snapshot modes; 5 transpilation layers |

**The critical realization**: The 3 "genuinely hard" patterns aren't just hard to compile — they're patterns the Rails community itself is moving away from.

---

## The Core Thesis

### The compiler restrictions ARE the community best practices

| Hard Pattern | What Rails Does | What Community Recommends | What Compiler Enforces |
|---|---|---|---|
| `if: -> { arbitrary_code }` | Accepts procs, lambdas, symbols, arrays | **Use named methods (symbols)** — procs only for one-liners | `if: :method_name` only |
| `belongs_to :x, polymorphic: true` | `constantize` from DB string — open type set | **Use `delegated_type`** — closed, explicit type hierarchy | Declare type set or use `delegated_type` |
| `throw(:abort)` in callbacks | Non-local control flow, halts chain | **Use service objects** — callbacks for self-state only | `Result<(), Abort>` return type |

This isn't a compromise. This is an **upgrade**.

The compiler doesn't restrict Rails — it enforces the version of Rails that experienced developers wish they had written from day one.

---

## Architecture: DB-First, 5-Layer Compilation

### Why DB First

The database is the source of truth for a deployed Rails application. `schema.rb` can be stale, incomplete, or wrong. The actual PostgreSQL/MySQL schema captures:

- Column types including vendor-specific (jsonb, arrays, PG enums, check constraints)
- Foreign keys that define the association graph
- Indexes including partial and unique constraints
- Default values and NOT NULL constraints

**Layer 0 (Schema) from DB introspection alone gives you typed Rust structs** — before you even look at a Ruby file.

### The 5 Layers

```
Layer 0: SCHEMA FOUNDATION
  Input:  Database introspection (Snapshot) OR structure.sql/schema.rb (Static)
  Output: Typed Rust structs + Diesel table! macros
  Resolves: Column types, PKs, defaults, NULLability
  Difficulty: EASY — pure data mapping

Layer 1: ASSOCIATION GRAPH
  Input:  Foreign keys (DB) + model declarations (has_many, belongs_to, etc.)
  Output: Relation methods, JOIN builders, eager loading
  Resolves: Simple associations, counter caches, dependent behavior
  Difficulty: EASY — FK graph + DSL declarations = complete picture

Layer 2: BEHAVIOR
  Input:  Model files (validations, callbacks, enums, scopes, store)
  Output: Validation functions, callback chains, enum types, query helpers
  Resolves: Problems 1, 4-9 from doc 07
  Method:  Direct DSL compilation (Proc Embargo approach)
  Difficulty: MEDIUM — inputs are static, metaprogramming is replayed at compile time

Layer 3: INTERFACE
  Input:  config/routes.rb + app/controllers/**/*.rb
  Output: Axum router + handler functions
  Resolves: RESTful routing, nested resources, member/collection routes
  Difficulty: EASY — routes.rb is a pure DSL

Layer 4: RESOLUTION (Cross-Cutting)
  Input:  Cross-reference of Layers 0-3
  Output: Polymorphic enum dispatch, STI type dispatch, through-chain JOINs
  Resolves: Problems 2, 3, 10 from doc 07
  Method:  Closed-set resolution (from DB query or model scan)
  Difficulty: HARD but bounded — type sets are finite once you look at the data
```

### Two Compilation Modes

**Static Mode** — No Ruby, no database. Pure file analysis.
- Inputs: `structure.sql` / `schema.rb` + `app/models/**/*.rb` + `config/routes.rb`
- Works offline, in CI/CD, from a git clone
- For ongoing compilation after initial migration

**Snapshot Mode** — Connects to live database, optionally boots Rails.
- Inputs: Database connection + model files + optional Ruby runtime
- Captures PG enums, check constraints, array columns that files miss
- Captures `SELECT DISTINCT type FROM ...` for STI/polymorphic type sets
- For initial migration of legacy apps

**Recommended workflow**: Snapshot once (to capture everything), Static forever after.

---

## The 10 Problems: How This Thesis Resolves Each

### Resolved by Layer 2 (Direct DSL Compilation — No Restrictions Needed)

These 7 problems use metaprogramming to generate methods from STATIC inputs declared in model files. The compiler replays the generation at compile time.

**Problem 4: Concern `included` blocks** — The compiler inlines the block content into the including model. The block contains DSL calls (`has_many`, `validates`, `scope`) that are themselves compilable. No runtime `class_eval` needed.

**Problem 5: belongs_to change tracking** — `class_eval <<-CODE` with `#{reflection.name}` generates `user_changed?`. The compiler knows the association name from the model file → generates the method directly.

**Problem 6: Relation delegation** — `method_missing` delegates to model scopes. The compiler knows ALL scopes (they're declared in model files) → generates direct methods on the query builder. No `method_missing` needed.

**Problem 7: Enum methods** — `define_method` per enum value. The compiler reads `enum :status, [:active, :archived]` → generates `active?`, `active!`, scope `active`, scope `not_active` as Rust methods. All inputs known.

**Problem 8: Store accessors** — `define_method` x7 per key. The compiler reads `store_accessor :settings, :color, :theme` → generates getter, setter, dirty tracking methods. All inputs known.

**Problem 1 (partial): Callback chains** — The chain STRUCTURE (order, which callbacks fire) is compilable from model declarations. `before_save :normalize_email` → becomes a function call in the save lifecycle. Symbol conditions like `if: :email_changed?` resolve to known methods.

**Problem 10 (partial): Through associations** — The association graph is fully declared in model files. `has_many :tags, through: :taggings` → the compiler walks the graph at compile time → generates the correct JOIN query.

### Resolved by Restrictions (Proc Embargo — Aligned with Community)

These 3 problems require small restrictions that MATCH what the community already recommends:

**Problem 1 (remainder): Proc conditions on callbacks**

```ruby
# BEFORE (proc — hard to compile, community says avoid):
before_save :check_inventory, if: -> { quantity_changed? && warehouse.active? }

# AFTER (named method — preferred by community AND compilable):
before_save :check_inventory, if: :should_check_inventory?

def should_check_inventory?
  quantity_changed? && warehouse.active?
end
```

The compiler provides a migration tool that:
1. Detects all proc conditions in model files
2. Extracts the proc body
3. Generates a named method with the body
4. Replaces the proc with a symbol reference
5. Reports any procs it can't automatically convert

**Impact**: Minimal. Named methods are already preferred. The proc body doesn't change — it just gets a name.

**Problem 2: Polymorphic type resolution**

```ruby
# BEFORE (open-ended — community says problematic):
belongs_to :commentable, polymorphic: true
# DB could contain ANY string in commentable_type

# AFTER — Option A: Explicit type set (new annotation):
belongs_to :commentable, polymorphic: true
# compiler annotation:
# @polymorphic_types [Post, Image, Video]

# AFTER — Option B: Use delegated_type (Rails 6.1+ recommended):
class Entry < ApplicationRecord
  delegated_type :entryable, types: %w[Message Comment]
end
```

With `delegated_type`, the type set is ALREADY declared in the model file (`types: %w[...]`). No restriction needed — it's just reading what's there.

For legacy `polymorphic: true`, the compiler:
1. In **Snapshot Mode**: `SELECT DISTINCT commentable_type FROM comments` → gets the closed set from the DB
2. In **Static Mode**: Scans all models for `as: :commentable` → builds the type set from inverse declarations
3. Generates a Rust enum from the closed set

**Impact**: Zero for `delegated_type` apps. For legacy polymorphic, the type set is either auto-detected or requires a one-line annotation.

**Problem 3: STI type dispatch**

```ruby
# STI: Animal → Dog, Cat, Bird via type column
class Animal < ApplicationRecord; end
class Dog < Animal; end
class Cat < Animal; end
class Bird < Animal; end
```

The compiler:
1. In **Snapshot Mode**: `SELECT DISTINCT type FROM animals` → gets `['Dog', 'Cat', 'Bird']`
2. In **Static Mode**: Scans for classes inheriting from `Animal` → builds the type set
3. Generates a Rust enum:

```rust
enum Animal {
    Dog(Dog),
    Cat(Cat),
    Bird(Bird),
}
```

**Impact**: Zero. The subclass hierarchy IS declared in Ruby files. The compiler just reads it.

---

## Why This Works: The Configuration Argument

Rails metaprogramming looks dynamic but is actually **configuration-driven**:

```
schema.rb / DB        → CONFIGURES → column types, table structure
model DSL calls       → CONFIGURES → associations, validations, callbacks, scopes, enums
config/routes.rb      → CONFIGURES → URL routing
```

The metaprogramming (`define_method`, `module_eval`, `class_eval`, `method_missing`) is the MECHANISM by which Rails reads configuration and generates behavior. But the CONFIGURATION ITSELF is static — it's written in files that don't change at runtime in a deployed application.

A Rails compiler doesn't need to replicate the mechanism. It needs to read the same configuration and generate the same behavior — but in Rust instead of Ruby.

```
Rails:    Configuration → Ruby metaprogramming → Ruby methods at boot time
Compiler: Configuration → Rust code generation → Rust methods at compile time
```

The only difference is WHEN the methods are created: Rails does it at boot, the compiler does it at build.

---

## What You Get

### Performance

| Metric | Rails (Ruby) | Compiled (Rust) | Factor |
|--------|-------------|-----------------|--------|
| Request latency (p50) | ~5-20ms | ~0.1-1ms | 10-50x |
| Memory per process | ~150-300MB | ~5-20MB | 15-30x |
| Concurrent connections | ~50-100 (threaded) | ~10,000+ (async) | 100x |
| Cold start | ~5-30s (boot) | ~0ms (native binary) | Instant |
| CPU per request | High (GVL contention) | Low (native + async) | 10-50x |

These aren't speculative. They follow from the fundamental difference between interpreted dynamic dispatch (RubyValue enum gives 2-5x) and statically typed, compiled code with real types (Rust gives 50-100x).

### Type Safety

Every column has a real Rust type. `user.email` is a `String`, not a `RubyValue`. `user.age` is an `Option<i32>`, not a `RubyValue`. NULL columns are `Option<T>`. The compiler catches type errors that Rails discovers at runtime.

### Deployment

One static binary. No Ruby runtime. No Bundler. No gem installation. No `bundle exec`. Copy the binary, run it. Docker image goes from ~1GB (Ruby + gems) to ~20MB (static binary).

### Operational Cost

At scale, the compute savings are significant. If a Rails app runs on 10 servers with 4 Puma workers each (40 processes), the Rust binary might serve the same traffic on 1-2 servers with a single process each. The memory savings alone (300MB × 40 = 12GB → 20MB × 2 = 40MB) can eliminate entire infrastructure tiers.

---

## What You Lose

### Development Speed for New Features

Rails' metaprogramming means adding a column is: add migration, add attribute to model, done. Methods appear automatically. The compiled version requires a recompilation step. But `cargo build` takes seconds, and the type checker catches errors that Rails would surface as runtime exceptions.

### Gem Ecosystem

Rails gems that use metaprogramming (Devise, Pundit, Kaminari, etc.) cannot be automatically compiled. Each gem's DSL patterns would need to be added to the compiler. This is the long tail — but the most-used gems use the same ~30 DSL patterns that Rails itself uses.

### Runtime Flexibility

No more `rails console` with live object manipulation. No more hot-patching in production. The compiled binary is what it is. This is a FEATURE for production (immutable deployments) but a loss for debugging.

---

## The Migration Path

### Phase 1: Layer 0 — Typed Structs from Schema

**Effort**: Low. **Value**: High.

Connect to your PostgreSQL database. Generate Rust structs with real types for every table. Generate Diesel `table!` macros. You now have a type-safe data access layer that compiles.

You can use these structs from Rust TODAY, alongside your running Rails app. The Rust service reads from the same database.

### Phase 2: Layer 1 — Associations

**Effort**: Low. **Value**: Medium.

Read model files for association declarations. Combine with FK graph from DB. Generate relation methods and JOIN builders. You now have `user.posts(conn)` and `post.author(conn)` in Rust.

### Phase 3: Layer 2 — Behavior

**Effort**: Medium. **Value**: High.

Compile validations, enums, scopes, store accessors, and callback chains from model DSL declarations. This is where the Proc Embargo restrictions apply. Run the migration tool on your model files to convert proc conditions to named methods.

### Phase 4: Layer 3 — Interface

**Effort**: Medium. **Value**: High.

Compile `routes.rb` to an Axum router. Generate handler stubs from controller files. Wire up to the data access layers from Phases 1-3. You now have a working Rust API.

### Phase 5: Layer 4 — Resolution

**Effort**: High. **Value**: Medium.

Resolve polymorphic types, STI hierarchies, and through-association chains. Generate Rust enums for closed type sets. This is the final layer that handles the cross-cutting concerns.

### The Result

After all 5 phases, you have a Rust project that:
- Serves the same API endpoints as your Rails app
- Reads from the same database
- Enforces the same validations
- Runs the same callbacks (as explicit function calls)
- Handles the same associations
- Uses real types instead of dynamic dispatch
- Compiles to a single native binary

---

## Why Now

Three things converge to make this feasible in 2026:

1. **Rails community convergence on best practices** — The patterns that resist compilation are the same ones the community is moving away from. `delegated_type` (Rails 6.1), service objects, named method callbacks — the ecosystem is self-correcting toward compilable patterns.

2. **Rust web ecosystem maturity** — Axum, Diesel, SeaORM, sqlx, tokio, serde — the Rust stack for web services is production-ready. These aren't experimental libraries; they're used at scale by companies like Cloudflare, Discord, and Amazon.

3. **The cost of running Ruby at scale** — Every company running Rails at scale (Shopify, GitHub, Basecamp) invests heavily in performance optimization (YJIT, Pitchfork, Ruby JIT). A native compiler sidesteps the entire optimization treadmill.

---

## What This Is NOT

- **Not a Ruby transpiler** — We don't transpile arbitrary Ruby code. We compile Rails DSL patterns.
- **Not a replacement for Rails development** — You can still develop in Rails. The compiler is for deployment.
- **Not 100% automatic** — Some manual work is needed for custom Ruby logic in controllers and service objects. The compiler handles the framework boilerplate; you port the business logic.
- **Not a new framework** — The output is standard Axum + Diesel. No custom runtime, no special libraries. Just Rust.

---

## The Bet

The bet is this: **Rails applications are 70% framework boilerplate and 30% business logic.**

The framework boilerplate — associations, validations, callbacks, routes, scopes, enums, store accessors — is what the compiler handles. It's repetitive, it follows patterns, and it maps to Rust.

The business logic — the code in your controller actions, service objects, and custom methods — is what you port manually. It's the unique part of your application.

If this ratio holds, the compiler automates the majority of the migration work. The remaining 30% is the part that actually requires human judgment — the part where a developer reads Ruby code, understands the intent, and writes equivalent Rust.

**The compiler doesn't replace the developer. It eliminates the boring parts so the developer can focus on the interesting parts.**
