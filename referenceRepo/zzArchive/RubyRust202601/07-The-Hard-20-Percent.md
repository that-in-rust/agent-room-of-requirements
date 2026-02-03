# The Hard 20%: What Resists Rails-to-Rust Compilation

## Date: 2026-02-04

## Overview

The Rails DSL Compiler thesis (doc 06) established that ~80% of Rails DSL patterns map cleanly to Rust. This document dissects the remaining ~20% - the areas that resist static compilation due to runtime metaprogramming. Each area is backed by **exact source file evidence** from the Rails framework and **quantitative data** from parseltongue analysis (55,603 entities, 158,170 dependency edges).

---

# Section 1: The 10 Hard Problems

## Parseltongue Quantitative Summary

| Metaprogramming Pattern | Entity Count | Key Locations |
|-------------------------|-------------|---------------|
| `method_missing` | **67** | ActiveRecord, ActionPack, ActiveModel, ActionView |
| `class_eval` | **6** | ActiveSupport::CodeGenerator, kernel ext |
| `module_eval` | **1** (unresolved) | Called pervasively but not defined as named entity |
| `define_method` | **10** | redefine_method, attribute_methods/read |
| `constantize` | **35** | inflections, rescuable, inheritance |
| `callbacks` (all) | **740** | ActiveSupport::Callbacks backbone |
| `polymorphic` (all) | **386** | associations, reflection, routing |
| `inheritance` (all) | **183** | STI, callback inheritance |
| `store_accessor` | **13** | ActiveRecord::Store |
| `nested_attributes` | **222** | NestedAttributes module |
| `delegated_type` | **8** | DelegatedType module |

> **Key insight**: The raw entity counts are LOW (67 method_missing, 6 class_eval) but they sit on CRITICAL PATHS. Every ActiveRecord attribute access flows through `method_missing`. Every callback flows through `module_eval`-generated runners. Low count, infinite blast radius.

---

## Problem 1: Callback System - Dynamic Method Generation

### Source Evidence
- **File**: `activesupport/lib/active_support/callbacks.rb`
- **Mechanism**: `module_eval` with heredoc string interpolation

### What Happens

At class load time, `define_callbacks :save` triggers generation of `_run_save_callbacks` and `_run_save_callbacks!` methods via string-based `module_eval`:

```ruby
# callbacks.rb — the heart of before_save, after_commit, around_action
module_eval <<~RUBY, __FILE__, __LINE__ + 1
  def _run_#{name}_callbacks(&block)
    run_callbacks(#{name.inspect}, &block)
  end
  private :_run_#{name}_callbacks
RUBY
```

The callback chain supports:
- **`:if` / `:unless`** — symbols (method names) or procs, resolved at RUNTIME
- **`:prepend`** — reorder callbacks dynamically
- **Halting** — `throw(:abort)` stops the chain
- **Around callbacks** — wraps with `yield`, requires stack unwinding

### Why It's Hard

The method NAMES are generated from strings. `define_callbacks :save, :validate, :destroy` creates 6+ methods whose names don't exist in source code. The `:if` conditions reference methods by symbol name — `before_save :do_thing, if: :active?` — requiring runtime method dispatch.

### Blast Radius

740 callback-related entities. Powers ALL of:
- `before_save`, `after_save`, `around_save` (ActiveRecord)
- `before_action`, `after_action`, `around_action` (ActionController)
- `before_validation`, `after_validation` (ActiveModel)
- `after_commit`, `after_rollback` (ActiveRecord transactions)
- `before_enqueue`, `around_perform` (ActiveJob)

### Difficulty: **HARD**

---

## Problem 2: Polymorphic Associations - Dynamic Class Loading

### Source Evidence
- **File**: `activerecord/lib/active_record/inheritance.rb:217-223`
- **File**: `activerecord/lib/active_record/reflection.rb:526, 934`
- **Mechanism**: `String#constantize` — converts database string to Ruby class

### What Happens

```ruby
# inheritance.rb:217-223
def polymorphic_class_for(name)
  if store_full_class_name
    name.constantize  # <-- THIS. A string from the DB becomes a class.
  else
    compute_type(name)
  end
end
```

A `belongs_to :commentable, polymorphic: true` stores `"Comment"` or `"Post"` in the `commentable_type` column. At query time, Rails reads this string and calls `.constantize` to get the actual Ruby class, then instantiates it.

### Why It's Hard

The set of possible types is **not declared anywhere in source code**. It's in the DATABASE. Any table that has a `_type` column could contain ANY class name string. The compiler cannot know at compile time which classes to instantiate.

### What It Powers

- `belongs_to :imageable, polymorphic: true` (e.g., Image belongs to either User or Product)
- `has_many :comments, as: :commentable` (the inverse side)
- Polymorphic routing (`polymorphic_path(record)`)
- 386 polymorphic-related entities across Rails

### Difficulty: **VERY HARD** — fundamentally open-ended type dispatch

---

## Problem 3: Single Table Inheritance (STI) - Runtime Class Dispatch

### Source Evidence
- **File**: `activerecord/lib/active_record/inheritance.rb:55-77`
- **Mechanism**: Overrides `new()` itself, reads `type` column, calls `constantize`

### What Happens

```ruby
# inheritance.rb:55-77 — overrides the constructor
def new(attributes = nil, &block)
  if abstract_class? || self == Base
    super
  elsif (subclass = subclass_from_attributes(attributes))
    subclass.new(attributes, &block)  # <-- returns a DIFFERENT class
  else
    super
  end
end

# subclass_from_attributes reads the type column:
def find_sti_class(type_name)
  type_name = sti_class_for(type_name)
  # ... which calls type_name.constantize
end
```

`Animal.all` returns a heterogeneous collection: `[#<Dog>, #<Cat>, #<Bird>]` based on the `type` column value. The `type_condition` method (line 321-326) generates SQL:

```sql
WHERE "animals"."type" IN ('Dog', 'Cat', 'Bird')
```

### Why It's Hard

Same table, different Rust struct types. Rust's type system is monomorphic — you can't return `Vec<Dog | Cat | Bird>` without an enum or trait object. The set of subtypes is OPEN (new subclasses can be added without changing parent code).

### What It Powers

- All STI hierarchies (e.g., `Vehicle` → `Car`, `Truck`, `Motorcycle`)
- `inheritance_column` configuration
- `sti_name` / `find_sti_class` class methods
- 183 inheritance-related entities

### Difficulty: **HARD** — requires Rust enum generation from model hierarchy

---

## Problem 4: ActiveSupport::Concern - Module Inclusion with class_eval Blocks

### Source Evidence
- **File**: `activesupport/lib/active_support/concern.rb:129-139, 209-215`
- **Mechanism**: `class_eval` with stored block, `extend const_get(:ClassMethods)`

### What Happens

```ruby
# concern.rb:129-139 — append_features override
def append_features(base)
  # ...
  base.class_eval(&@_included_block) if instance_variable_defined?(:@_included_block)
  # The block stored by `included do ... end` is evaluated
  # IN THE CONTEXT of the including class
end

# concern.rb:209-215 — class_methods block
def class_methods(&class_methods_module_definition)
  mod = const_defined?(:ClassMethods, false) ?
    const_get(:ClassMethods) :
    const_set(:ClassMethods, Module.new)
  mod.module_eval(&class_methods_module_definition)
end
```

The `included do ... end` block is STORED as a proc and evaluated LATER when another class includes the concern. This is deferred execution — the block runs in a class context that doesn't exist yet when the concern is defined.

### Why It's Hard

The `included` block can contain ANY Ruby code — `has_many`, `validates`, `scope`, `before_action` — and it runs in the INCLUDING class's context. The concern doesn't know which class will include it. This is essentially runtime code injection.

### What It Powers

- Every Rails concern (`app/models/concerns/*.rb`, `app/controllers/concerns/*.rb`)
- All of Rails' own internal module composition
- The pattern: `include Searchable`, `include Authenticatable`, etc.

### Difficulty: **MEDIUM** — blocks contain DSL calls that ARE compilable if we inline them

---

## Problem 5: belongs_to Change Tracking via class_eval with String Interpolation

### Source Evidence
- **File**: `activerecord/lib/active_record/associations/builder/belongs_to.rb:154-166`
- **Mechanism**: `class_eval <<-CODE` with `#{reflection.name}` interpolation

### What Happens

```ruby
# belongs_to.rb:154-166
def self.define_change_tracking_methods(model, reflection)
  model.generated_association_methods.class_eval <<-CODE, __FILE__, __LINE__ + 1
    def #{reflection.name}_changed?
      association(:#{reflection.name}).target_changed?
    end

    def #{reflection.name}_previously_changed?
      association(:#{reflection.name}).target_previously_changed?
    end
  CODE
end
```

For `belongs_to :user`, this generates `user_changed?` and `user_previously_changed?` methods as STRINGS that get compiled by Ruby's parser at class load time.

### Why It's Hard

The method names are constructed from association names via string interpolation. A Rust compiler needs to know all association names at compile time to generate the corresponding methods. But association names come from model DSL declarations.

### What It Powers

- Dirty tracking for associations: `post.user_changed?`
- `belongs_to` touch cascading: detecting when parent association changes
- Counter cache invalidation triggers

### Difficulty: **MEDIUM** — association names ARE known from model files (static DSL)

---

## Problem 6: Relation Delegation - method_missing to Model

### Source Evidence
- **File**: `activerecord/lib/active_record/relation/delegation.rb:70-90, 117-134`
- **Mechanism**: `module_eval` + `method_missing` + `public_send`

### What Happens

```ruby
# delegation.rb:70-90 — GeneratedRelationMethods
class GeneratedRelationMethods < Module
  def generate_method(method)
    MUTEX.synchronize do
      return if method_defined?(method)
      module_eval <<-RUBY, __FILE__, __LINE__ + 1
        def #{method}(...)
          scoping { model.#{method}(...) }
        end
      RUBY
    end
  end
end

# delegation.rb:117-134 — ClassSpecificRelation
def method_missing(method, ...)
  if model.respond_to?(method)
    model.generate_relation_method(method)  # cache it for next time
    scoping { model.public_send(method, ...) }
  else
    super
  end
end
```

When you call `User.where(active: true).my_custom_scope`, the Relation doesn't have `my_custom_scope`. It hits `method_missing`, checks if `User` responds to it, delegates via `public_send`, and CACHES the delegation for next time.

### Why It's Hard

The Relation class dynamically discovers which scopes/class methods exist on the model and creates delegation methods on-the-fly. The set of delegatable methods is the ENTIRE public API of the model class — unknown until runtime.

### What It Powers

- Chaining custom scopes: `User.active.premium.recent`
- Model class method delegation through relations
- Association scope chaining: `user.posts.published.recent`

### Difficulty: **MEDIUM** — scopes ARE declared in model files, so the set is finite and known

---

## Problem 7: Enum - Dynamic Method Generation per Value

### Source Evidence
- **File**: `activerecord/lib/active_record/enum.rb:252-278, 294-323`
- **Mechanism**: `module_eval` block + `define_method` per enum value + `scope`

### What Happens

```ruby
# enum.rb:252-278
_enum_methods_module.module_eval do
  pairs.each do |label, value|
    define_enum_methods(name, value_method_name, value, scopes, instance_methods)
  end
end

# enum.rb:302-322 — define_enum_methods
def define_enum_methods(name, value_method_name, value, scopes, instance_methods)
  if instance_methods
    define_method("#{value_method_name}?") { public_send(:"#{name}_for_database") == value }
    define_method("#{value_method_name}!") { update!(name => value) }
  end
  if scopes
    klass.scope value_method_name, -> { where(name => value) }
    klass.scope "not_#{value_method_name}", -> { where.not(name => value) }
  end
end
```

For `enum :status, [:active, :archived]`, this generates:
- `active?`, `archived?` (predicates)
- `active!`, `archived!` (bang setters)
- `Conversation.active` (scope)
- `Conversation.not_active` (negated scope)
- `Conversation.statuses` (mapping hash)

### Why It's Hard

The method names come from enum VALUE NAMES — strings/symbols declared in the model. Each value spawns 4+ methods. The `prefix` and `suffix` options further modify method names.

### What It Powers

- All enum-based workflows: `order.pending?`, `order.shipped!`, `Order.pending`
- Enum validation
- Enum serialization/deserialization

### Difficulty: **MEDIUM** — enum values ARE declared in model files, fully known at compile time

---

## Problem 8: Store/store_accessor - 7 Methods per Key via define_method

### Source Evidence
- **File**: `activerecord/lib/active_record/store.rb:134-188`
- **Mechanism**: `module_eval` + 7x `define_method` per key

### What Happens

```ruby
# store.rb:134-188
_store_accessors_module.module_eval do
  keys.each do |key|
    accessor_key = "#{accessor_prefix}#{key}#{accessor_suffix}"

    define_method("#{accessor_key}=") { |value| write_store_attribute(store_attribute, key, value) }
    define_method(accessor_key) { read_store_attribute(store_attribute, key) }
    define_method("#{accessor_key}_changed?") { ... }
    define_method("#{accessor_key}_change") { ... }
    define_method("#{accessor_key}_was") { ... }
    define_method("saved_change_to_#{accessor_key}?") { ... }
    define_method("saved_change_to_#{accessor_key}") { ... }
    define_method("#{accessor_key}_before_last_save") { ... }
  end
end
```

For `store :settings, accessors: [:color, :homepage]`, generates 8 methods PER key = 16 methods total, all accessing a serialized JSON/YAML column.

### Why It's Hard

Methods are generated from key names passed to `store_accessor`. The underlying storage is a serialized hash in a single database column — no schema definition for individual keys.

### What It Powers

- JSON/YAML column accessors: `user.color`, `user.color=`
- Dirty tracking on store attributes: `user.color_changed?`
- PostgreSQL hstore/json column access

### Difficulty: **MEDIUM** — key names ARE declared in model files

---

## Problem 9: Conditional Validations - Symbol/Proc Runtime Resolution

### Source Evidence
- **File**: `activemodel/lib/active_model/validations.rb:166-191`
- **File**: `activesupport/lib/active_support/callbacks.rb:327-331`
- **Mechanism**: `:if` / `:unless` accept symbols or procs, resolved via `send`

### What Happens

```ruby
# validations.rb:190
set_callback(:validate, *args, options, &block)

# The :if option flows into callbacks.rb:327-331
# callbacks.rb converts symbols to MethodCall objects:
class MethodCall
  def initialize(method_name)
    @method_name = method_name
  end
  def call(target, value)
    target.send(@method_name)  # <-- dynamic dispatch by method name
  end
end
```

`validates :email, presence: true, if: :requires_email?` stores `:requires_email?` as a symbol. At validation time, Rails calls `record.send(:requires_email?)` — dynamic method dispatch by name.

Procs are even worse: `validates :age, numericality: true, if: -> { signup_step > 2 }` — arbitrary Ruby code as a condition.

### Why It's Hard

- **Symbol conditions**: The compiler must resolve method names to actual methods. These ARE defined somewhere in the model, but linking them requires cross-referencing.
- **Proc conditions**: Arbitrary Ruby code that cannot be statically compiled in the general case.
- **Arrays**: `if: [:admin?, :active?]` — ALL must be true. Combines multiple dynamic dispatches.

### What It Powers

- All conditional validations
- Conditional callbacks: `before_save :normalize, if: :title_changed?`
- Context-dependent validation: `validates :password, on: :create`

### Difficulty: **HARD for procs, MEDIUM for symbols** — symbols map to known methods, procs are arbitrary code

---

## Problem 10: has_many :through - Recursive Join Chain Resolution

### Source Evidence
- **File**: `activerecord/lib/active_record/reflection.rb:988-1265`
- **File**: `activerecord/lib/active_record/associations/has_many_through_association.rb`
- **Mechanism**: Recursive `collect_join_reflections`, singular/plural name guessing

### What Happens

```ruby
# reflection.rb:1130-1148 — source_reflection_name
def source_reflection_name
  options[:source] ||= name  # try the association name first
end

# If source not found, tries BOTH singular and plural:
# has_many :tags, through: :taggings
# Looks for: tagging.tag AND tagging.tags

# reflection.rb:988-1020 — ThroughReflection
# collect_join_reflections builds the join chain RECURSIVELY
# because through associations can chain through OTHER through associations
```

`has_many :subscribers, through: :subscriptions` must:
1. Find `subscriptions` association on the model
2. Find `subscriber` (or `subscribers`) association on the Subscription model
3. Generate JOIN SQL across the intermediary table
4. Handle nested through: `has_many :tags, through: :taggings` where `taggings` itself is `through: :post_taggings`

### Why It's Hard

- **Recursive resolution**: Through associations can chain through OTHER through associations, creating arbitrary-depth join chains
- **Name guessing**: Rails tries both singular and plural forms of the source name
- **Polymorphic through**: `source_type` option adds type conditions to the join
- **Counter cache through intermediary**: Complex update propagation

### What It Powers

- All join model patterns: `has_many :physicians, through: :appointments`
- Nested through: `has_many :comments, through: :posts` on a User
- Tag systems: `has_many :tags, through: :taggings`
- Complex querying through joins

### Difficulty: **HARD** — requires resolving multi-model join graphs at compile time

---

## Difficulty Matrix

```mermaid
quadchart
    title Hard 20% Difficulty vs Blast Radius
    x-axis Low Blast Radius --> High Blast Radius
    y-axis Easy to Compile --> Hard to Compile
    quadrant-1 "Hardest: Must Solve"
    quadrant-2 "Hard but Contained"
    quadrant-3 "Easy Wins"
    quadrant-4 "Medium Priority"
    "Callbacks": [0.95, 0.80]
    "Polymorphic": [0.60, 0.95]
    "STI": [0.40, 0.85]
    "Concern": [0.85, 0.45]
    "belongs_to tracking": [0.30, 0.35]
    "Relation Delegation": [0.75, 0.50]
    "Enum": [0.50, 0.30]
    "Store": [0.25, 0.35]
    "Conditional Validation": [0.65, 0.70]
    "has_many through": [0.55, 0.75]
```

## Compilation Feasibility Summary

| Problem | Difficulty | Key Blocker | Resolvable at Compile Time? |
|---------|-----------|-------------|---------------------------|
| 1. Callbacks | HARD | `:if`/`:unless` with procs, `throw(:abort)` halting | **Partially** — chain structure yes, proc conditions no |
| 2. Polymorphic | VERY HARD | `constantize` from DB string | **Partially** — if all types declared in models |
| 3. STI | HARD | `type` column → class instantiation | **Yes** — if subclass list is closed and known |
| 4. Concern | MEDIUM | `class_eval` of stored blocks | **Yes** — blocks contain compilable DSL calls |
| 5. belongs_to tracking | MEDIUM | String interpolation for method names | **Yes** — association names from model files |
| 6. Relation Delegation | MEDIUM | `method_missing` → model class methods | **Yes** — scopes declared in model files |
| 7. Enum | MEDIUM | `define_method` per enum value | **Yes** — enum values from model files |
| 8. Store | MEDIUM | `define_method` per store key | **Yes** — keys from model files |
| 9. Conditional Validation | HARD | Symbol → `send`, Proc → arbitrary code | **Partially** — symbols yes, procs no |
| 10. Through associations | HARD | Recursive join resolution, name guessing | **Yes** — all associations declared in model files |

### The Pattern

**7 of 10 problems are RESOLVABLE** because the dynamic code reads from STATIC declarations in model files. The metaprogramming GENERATES methods, but the INPUTS to that generation (association names, enum values, store keys, scope names) are all declared in `app/models/*.rb`.

**3 problems remain genuinely hard:**
1. **Proc conditions** — arbitrary Ruby code in `:if` / `:unless` lambdas
2. **Polymorphic type resolution** — open-ended set from database values
3. **Callback halting** — `throw(:abort)` requires stack unwinding semantics

---

# Section 2: Creative Solutions

## Pre-Research: Initial Thoughts & Exploration Direction

### The Core Realization from Section 1

The 10 hard problems collapse into **3 fundamental challenges**:

1. **Method Generation from Static Inputs** (Problems 4-8) — `define_method`/`module_eval` generates methods, but from KNOWN inputs (association names, enum values, store keys). These are **solved problems** — we just replay the generation at compile time.

2. **Dynamic Dispatch by Name** (Problems 1, 6, 9) — `send(:method_name)`, `public_send`, callback `:if` symbols. The method names ARE known from source, but resolution requires cross-model analysis.

3. **Open-Ended Type Resolution** (Problems 2, 3, 10) — `constantize` from DB strings, STI type columns, recursive through-chains. The type set is NOT declared in one place.

### 3 Solution Directions to Explore

#### Direction A: "The Boot Snapshot" — Run Rails Boot, Freeze the Result

**Core Insight**: Instead of replicating Ruby's metaprogramming, EXECUTE it once (in Ruby) and capture the output. Boot the Rails app in a special "compilation mode" that:
- Loads all models, runs all `define_method`/`module_eval` calls
- Captures the COMPLETE method table for every model class
- Captures the complete callback chain (ordered, with conditions)
- Captures the complete association reflections graph
- Exports this as a JSON/TOML manifest: every class, every method, every callback, every association, typed
- The Rust compiler reads THIS manifest, not the Ruby source

**Why this might work**: Ruby IS capable of introspecting itself. `Model.reflections`, `Model._validators`, `Model.defined_enums`, `Model.stored_attributes` — Rails exposes ALL of this as queryable data structures at runtime. We don't need to parse Ruby; we need to RUN it once and snapshot the result.

**Solves**: Problems 1-10 (ALL of them — if Ruby can run it, we can capture it)

**Risks**: Requires a working Ruby environment at compile time. Database connection needed for schema. Doesn't capture proc bodies.

**Research direction**: Look at how Sorbet does Rails introspection (tapioca gem generates RBI files by booting Rails). Look at how bootsnap works. Look at `rails runner` for scriptable boot.

#### Direction B: "The Proc Embargo" — Restrict + Generate

**Core Insight**: For the 3 genuinely hard problems (procs, polymorphic, halting), don't try to compile arbitrary Ruby — instead:
- **Proc conditions**: Restrict to a compilable subset. `if: :method_name` → compiled. `if: -> { ... }` → require the user to rewrite as a named method. Provide a migration tool.
- **Polymorphic types**: Require explicit type registration: `polymorphic_types :commentable, [Comment, Post, Article]`. Generate a Rust enum. Validate DB data against the closed set.
- **Callback halting**: Replace `throw(:abort)` with a `Result<(), Abort>` return type. Around callbacks become middleware-style wrappers with `next.call()`.

**Why this might work**: Most Rails apps use proc conditions minimally. Most polymorphic associations have a small, known set of types. This is the Crystal approach — restrict the language slightly to enable compilation.

**Solves**: ALL 10 problems by restricting the 3 hard cases to compilable forms

**Risks**: Requires code changes to existing Rails apps. Migration burden. Some edge cases may not map.

**Research direction**: Look at Crystal's restrictions vs Ruby. Look at Sorbet's strict mode. Look at how TypeScript restricted JavaScript.

#### Direction C: "The Futamura Projection" — Partial Evaluation of Rails Boot

**Core Insight**: Combine A and B using the theory of partial evaluation (Futamura projections). The Rails boot process IS a program. The model files ARE its input. Partially evaluate the boot process with respect to the model files to produce a SPECIALIZED program (the Rust code).

Concretely:
- Parse `schema.rb` → known columns and types (static)
- Parse `app/models/*.rb` → known DSL calls (static)
- For each DSL call, apply the KNOWN Rails metaprogramming transformation (we know exactly what `has_many` does — it creates 17 methods, we can enumerate them)
- The compiler IS the partial evaluator — it "runs" the Rails DSL interpretation at compile time
- This is different from Direction A because we don't need Ruby at all — we reimplement the DSL interpretation in Rust/at compile time

This is what GraalVM Truffle does: partial evaluation of an interpreter + a program produces compiled native code.

**Solves**: Problems 1-10, but with deep investment in reimplementing Rails' DSL interpretation logic

**Risks**: Must perfectly replicate Rails' method generation logic. Any divergence = bugs. Rails upgrades require compiler updates.

**Research direction**: Futamura projections papers. GraalVM Truffle partial evaluation. PyPy's meta-tracing. Zig's comptime as a simpler model.

### Key References to Research

| Topic | Why Relevant |
|-------|-------------|
| **Sorbet + Tapioca** | Tapioca boots Rails and generates type stubs — proof that "boot and snapshot" works |
| **GraalVM Truffle PE** | Partial evaluation of interpreter + program → native code |
| **Crystal language** | Ruby-like syntax compiled to native via type inference + restrictions |
| **Zig comptime** | Compile-time code execution model — "run the program at compile time" |
| **Futamura projections** | Theoretical foundation: specializing an interpreter to a program |
| **PyPy meta-tracing** | Tracing JIT that specializes an interpreter — different approach but same goal |
| **Scala 3 inline/transparent** | Compile-time metaprogramming in a typed language |
| **Nim macros** | AST-level macros that can generate code from DSL-like inputs |
| **TypeScript vs JavaScript** | How a typed language was layered over a dynamic one — migration strategy |
| **Rails Packwerk** | Facebook's tool for enforcing boundaries in Rails — understands Rails module structure |

### The Meta-Question

All 3 directions converge on one question: **at what stage do we resolve the metaprogramming?**

```
Direction A: RUNTIME (Ruby) → Snapshot → Rust codegen
Direction B: SOURCE (restrict) → Static analysis → Rust codegen
Direction C: COMPILE-TIME (reimplement) → Partial eval → Rust codegen
```

The answer might be: **ALL THREE, layered.**
- Use B (restrictions) for the easy 70% — pure DSL compilation
- Use C (partial evaluation) for the medium 20% — reimplement Rails' DSL logic
- Use A (boot snapshot) for the hard 10% — fall back to Ruby introspection for edge cases

This layered approach = **"The Rails Compiler Pyramid"**

```
         /\
        /  \   A: Boot Snapshot (escape hatch, 10%)
       /    \
      /──────\  C: Partial Evaluation (reimplemented DSL, 20%)
     /        \
    /──────────\ B: Static DSL Compilation (direct, 70%)
   /______________\
```

### Next Steps for Section 2 Full Writeup

1. **Flesh out each direction** with concrete Rust code examples for all 10 problems
2. **Research** Sorbet/Tapioca, GraalVM Truffle PE, Crystal, Zig comptime
3. **Score** feasibility and impact for each
4. **Design the layered pyramid** approach as the recommended path
5. **Identify** which of the 10 problems falls into which layer
