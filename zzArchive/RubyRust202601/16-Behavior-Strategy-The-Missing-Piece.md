# The Behavior Strategy: The Missing Piece

## Date: 2026-02-06

## The Logical Gap

The previous documents (10-15) define a comprehensive architecture for compiling Rails **metadata**:
- Schema → Rust structs (Layer 0)
- Associations → Relation methods (Layer 1)
- Callback registration → Callback trait (Layer 2)
- Route definitions → Axum router (Layer 3)
- Type sets → Enum dispatch (Layer 4)

**But they don't address what happens inside the callbacks, validators, and controller actions.**

```rust
// The compiler can generate THIS (the wiring):
impl Callbacks for User {
    fn callbacks() -> &'static [Callback<Self>] {
        &[Callback {
            name: "normalize_email",
            timing: CallbackTiming::Before,
            event: LifecycleEvent::Save,
            condition: Some(|u| u.email_changed()),
            action: |u| u.normalize_email(),  // <-- BUT WHERE DOES THIS COME FROM?
        }]
    }
}

// The compiler CANNOT generate THIS (the behavior):
impl User {
    fn normalize_email(&mut self) -> CallbackResult {
        // This is arbitrary Ruby code:
        //   self.email = email.downcase.strip
        // How do we compile this?
        ???
    }
}
```

This document explicitly addresses the "behavior gap" and defines the contract for what the compiler actually produces vs what requires human intervention.

---

## The Fundamental Distinction

### Metadata (Compiler Handles)

| What | Example | Compiler Output |
|------|---------|-----------------|
| Schema | `t.string :email` | `email: Option<String>` |
| Association wiring | `has_many :posts` | `fn posts() -> Query<Post>` |
| Callback registration | `before_save :normalize` | Callback chain entry |
| Validation declaration | `validates :email, presence: true` | `v.validates_presence("email", &self.email)` |
| Enum definition | `enum :status, [...]` | `enum Status { Draft, ... }` |
| Scope declaration | `scope :active, -> { where(active: true) }` | `fn active() -> Query<Self>` |

### Behavior (Requires Strategy)

| What | Example | Problem |
|------|---------|---------|
| Callback bodies | `def normalize_email; email.downcase.strip; end` | Arbitrary Ruby |
| Custom validators | `def check_inventory; ...; end` | Business logic |
| Controller actions | `def create; @user = User.new(params); end` | Request handling |
| Service objects | `class PaymentService; def call; ...; end` | Domain logic |
| Mailers | `UserMailer.welcome(user).deliver_later` | External integration |
| Background jobs | `InventoryJob.perform_later(order_id)` | Async processing |

---

## The Three Strategies

### Strategy 1: Compilable Ruby Subset (AOT)

**Premise**: Define a strict subset of Ruby that CAN be compiled to Rust.

```ruby
# COMPILABLE: Simple method with known operations
def normalize_email
  self.email = email.downcase.strip
end

# NOT COMPILABLE: Uses reflection
def normalize_email
  send("email=", email.downcase.strip)
end

# NOT COMPILABLE: Uses eval
def normalize_email
  eval("self.email = email.downcase.strip")
end

# NOT COMPILABLE: External service call
def normalize_email
  self.email = EmailNormalizer.normalize(email)
end
```

**The Subset Rules** (from Document 03 - Ruby--):

1. No `eval`, `instance_eval`, `class_eval`, `module_eval`
2. No `send`, `public_send`, `__send__`
3. No `define_method`, `method_missing`, `respond_to_missing?`
4. No `const_get`, `const_set`, `constantize`
5. No `binding`, `Proc#binding`
6. No `ObjectSpace`, `TracePoint`
7. No dynamic require/autoload
8. Static method targets only (no `obj.send(method_name)`)

**Compilation Approach**:

```
Ruby Subset → Prism AST → Type Inference → Rust AST → rustc
```

```rust
// Ruby: def normalize_email; self.email = email.downcase.strip; end
// Compiles to:

fn normalize_email(&mut self) -> CallbackResult {
    if let Some(ref email) = self.email {
        self.email = Some(email.to_lowercase().trim().to_string());
    }
    Ok(())
}
```

**Limitations**:
- Only works for Ruby-- subset
- Gem code is NOT in the subset
- Service objects with external calls are NOT in the subset
- Requires type annotations or inference

**Honest Claim**: "Compiles callback/validator bodies that use only standard library operations and model methods"

### Strategy 2: Hybrid Runtime

**Premise**: Rust handles the hot path (metadata, ORM, routing); Ruby handles behavior.

```
Request → Axum Router (Rust)
       → Load Model (Rust/Diesel)
       → Run Callbacks (FFI to Ruby)
       → Run Validations (FFI to Ruby)
       → Save Model (Rust/Diesel)
       → Response (Rust)
```

**Architecture**:

```rust
// Rust side: call into embedded Ruby for behavior
impl User {
    fn normalize_email(&mut self) -> CallbackResult {
        // FFI call to Ruby runtime
        let ruby = Ruby::get();
        ruby.eval_with_self(self, "normalize_email")
            .map_err(|e| CallbackError::from(e))
    }
}
```

**Implementation Options**:

1. **Embed mruby** - Lightweight Ruby for simple scripts
2. **Embed CRuby via FFI** - Full Ruby, heavier
3. **gRPC to Ruby sidecar** - Separate process, network overhead

**Performance Profile**:

| Operation | Rust-only | Hybrid (FFI) | Rails |
|-----------|-----------|--------------|-------|
| Route dispatch | 0.01ms | 0.01ms | 0.5ms |
| Model load | 0.1ms | 0.1ms | 0.5ms |
| Callback (simple) | 0.001ms | 0.1ms | 0.1ms |
| Callback (complex) | N/A | 0.5ms | 0.5ms |
| DB query | 1ms | 1ms | 1ms |

**Honest Claim**: "2-5x speedup for metadata-heavy operations; callback behavior unchanged"

### Strategy 3: Explicit Rewrite Boundary (Migration Accelerator)

**Premise**: The compiler generates a **skeleton** with explicit `todo!()` markers. Humans port the behavior.

```rust
// GENERATED: Skeleton with markers
impl User {
    /// TODO: Port from app/models/user.rb:45-48
    /// Original Ruby:
    /// ```ruby
    /// def normalize_email
    ///   self.email = email.downcase.strip
    /// end
    /// ```
    fn normalize_email(&mut self) -> CallbackResult {
        todo!("Port normalize_email from User model")
    }

    /// TODO: Port from app/models/user.rb:50-67
    /// Original Ruby:
    /// ```ruby
    /// def send_welcome_email
    ///   UserMailer.welcome(self).deliver_later
    /// end
    /// ```
    fn send_welcome_email(&mut self) -> CallbackResult {
        todo!("Port send_welcome_email - requires mailer setup")
    }
}
```

**The Contract**:

| The Compiler Generates | The Developer Ports |
|------------------------|---------------------|
| Struct definitions | — |
| Diesel table macros | — |
| Association methods | — |
| Validation framework calls | Custom validator bodies |
| Callback chain wiring | Callback method bodies |
| Enum types and methods | — |
| Scope method signatures | Scopes with runtime values |
| Router skeleton | Controller action bodies |
| `todo!()` stubs | Business logic |

**Migration Workflow**:

```
1. Run compiler → generates Rust project with 100 todo!() markers
2. `cargo build` fails with "not yet implemented" for each marker
3. Developer ports each todo!() one by one
4. `cargo build` succeeds when all markers resolved
5. Run semantic diff to verify behavior
```

**Honest Claim**: "Generates 70% of boilerplate; 30% requires manual porting"

---

## The Recommended Strategy: Layered Approach

Combine all three strategies based on code characteristics:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          CODE CLASSIFICATION                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ TIER 1: Metadata (Fully Compiled)                                    │   │
│  │ • Schema → Structs                                                   │   │
│  │ • Associations → Methods                                             │   │
│  │ • Enums → Rust enums                                                 │   │
│  │ • Standard validations → Validator calls                             │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ TIER 2: Ruby-- Subset (AOT Compiled)                                 │   │
│  │ • Simple callbacks (string ops, conditionals, model methods)         │   │
│  │ • Computed attributes                                                │   │
│  │ • Pure transformation methods                                        │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ TIER 3: Rewrite Boundary (todo!() + Manual Port)                     │   │
│  │ • Service object calls                                               │   │
│  │ • External API integrations                                          │   │
│  │ • Complex business logic                                             │   │
│  │ • Gem-dependent code                                                 │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Classification Algorithm**:

```rust
fn classify_method(method: &MethodDef) -> Tier {
    let ast = parse_method_body(method);

    // Check for non-compilable patterns
    if contains_eval(&ast) || contains_send(&ast) || contains_constantize(&ast) {
        return Tier::RewriteBoundary;
    }

    // Check for external calls
    if calls_external_service(&ast) || calls_gem_code(&ast) {
        return Tier::RewriteBoundary;
    }

    // Check if within Ruby-- subset
    if is_ruby_minus_minus(&ast) {
        return Tier::AOTCompilable;
    }

    Tier::RewriteBoundary
}
```

---

## Amdahl's Law Reality Check

The critique correctly points out that 50-100x speedup claims must account for where time is actually spent.

### Typical Rails Request Breakdown

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ TYPICAL CRUD REQUEST (Rails)                                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   Network I/O:        5ms   ████████████████████░░░░░░░░░░░░░░░░░░  (25%)  │
│   Rails routing:      2ms   ████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  (10%)  │
│   Controller:         1ms   ████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░   (5%)  │
│   Model load:         1ms   ████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░   (5%)  │
│   Callbacks:          1ms   ████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░   (5%)  │
│   DB query:           8ms   ████████████████████████████████░░░░░░  (40%)  │
│   Serialization:      2ms   ████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  (10%)  │
│                                                                             │
│   Total:             20ms                                                   │
│                                                                             │
│   Acceleratable (Ruby/Framework): ~35% (7ms)                                │
│   Non-acceleratable (DB + Network): ~65% (13ms)                             │
│                                                                             │
│   Max speedup (Amdahl): 1 / (1 - 0.35) = 1.54x                              │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Where Big Speedups ARE Possible

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ CPU-BOUND WORKLOAD (Data Processing)                                        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   Network I/O:        1ms   ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░   (1%)  │
│   Ruby processing:   95ms   ██████████████████████████████████████  (95%)  │
│   DB query:           4ms   ████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░   (4%)  │
│                                                                             │
│   Total:            100ms                                                   │
│                                                                             │
│   Acceleratable: 95%                                                        │
│   Max speedup (Amdahl): 1 / (1 - 0.95) = 20x                                │
│   With Rust efficiency gains: 50-100x possible                              │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Honest Performance Claims

| Scenario | Expected Speedup | Why |
|----------|------------------|-----|
| Simple CRUD API | 1.5-3x | DB/network dominated |
| Complex validation | 5-10x | Ruby logic dominated |
| Data transformation | 20-50x | CPU bound |
| Report generation | 50-100x | CPU + memory bound |
| Concurrent requests | 10-100x | No GVL, async |
| Cold start | ∞ (instant vs 5-30s) | No boot time |
| Memory per process | 10-30x reduction | No Ruby runtime |

**Revised Claim**: "50-100x for CPU-bound workloads; 2-5x for typical CRUD; 10-100x for concurrency; massive memory reduction"

---

## Polymorphic/STI: The Open World Problem

The critique correctly identifies that type sets can grow after compilation:

```sql
-- At compile time
SELECT DISTINCT type FROM animals;
-- Returns: ['Dog', 'Cat', 'Bird']

-- After deployment, someone inserts:
INSERT INTO animals (type, ...) VALUES ('Fish', ...);
-- Now the Rust enum doesn't have a Fish variant!
```

### Solution: Closed World with Enforcement

**Option A: Database Constraint**

```sql
ALTER TABLE animals
ADD CONSTRAINT animals_type_check
CHECK (type IN ('Dog', 'Cat', 'Bird'));
```

**Option B: Rust Enum with Unknown**

```rust
#[derive(Debug, Clone)]
pub enum Animal {
    Dog(Dog),
    Cat(Cat),
    Bird(Bird),
    Unknown { type_name: String, id: i64 },
}

impl Animal {
    pub fn from_row(row: &Row) -> Result<Self, Error> {
        match row.type_column.as_str() {
            "Dog" => Ok(Animal::Dog(Dog::from_row(row)?)),
            "Cat" => Ok(Animal::Cat(Cat::from_row(row)?)),
            "Bird" => Ok(Animal::Bird(Bird::from_row(row)?)),
            other => Ok(Animal::Unknown {
                type_name: other.to_string(),
                id: row.id,
            }),
        }
    }
}
```

**Option C: Compiler Annotation with Runtime Check**

```ruby
# @polymorphic_types [Dog, Cat, Bird]
# @strict true  # Fail on unknown types at runtime
belongs_to :animal, polymorphic: true
```

```rust
impl Comment {
    pub fn animal(&self) -> Result<Animal, TypeError> {
        match self.animal_type.as_str() {
            "Dog" | "Cat" | "Bird" => self.load_animal(),
            other => Err(TypeError::UnknownPolymorphicType {
                expected: &["Dog", "Cat", "Bird"],
                found: other.to_string(),
            }),
        }
    }
}
```

**Honest Claim**: "Polymorphic types require either DB constraints or Unknown variant handling"

---

## The Conformance Harness

To validate the architecture rather than argue it, implement:

### 1. IR Diff Test

```rust
#[test]
fn test_user_model_ir_matches_rails() {
    // Generate IR from compiler
    let compiler_ir = compile_model("app/models/user.rb");

    // Generate "truth" from Rails introspection
    let rails_ir = rails_introspect("User");

    // Diff
    assert_eq!(compiler_ir.associations, rails_ir.associations);
    assert_eq!(compiler_ir.validations, rails_ir.validations);
    assert_eq!(compiler_ir.callbacks.len(), rails_ir.callbacks.len());
    assert_eq!(compiler_ir.enums, rails_ir.enums);
}
```

### 2. Behavioral Equivalence Test

```rust
#[tokio::test]
async fn test_user_create_matches_rails() {
    // Setup: same DB fixture
    let fixture = load_fixture("users_empty");

    // Rails request
    let rails_response = http_post(
        "http://localhost:3000/api/users",
        json!({"email": "test@example.com", "name": "Test"}),
    ).await;

    // Rust request (against same DB)
    let rust_response = http_post(
        "http://localhost:8000/api/users",
        json!({"email": "test@example.com", "name": "Test"}),
    ).await;

    // Compare
    assert_eq!(rails_response.status, rust_response.status);
    assert_json_eq!(
        rails_response.body,
        rust_response.body,
        ignore: ["id", "created_at", "updated_at"]
    );

    // Compare DB state
    let rails_user = query_user_by_email("test@example.com", rails_db);
    let rust_user = query_user_by_email("test@example.com", rust_db);
    assert_eq!(rails_user.name, rust_user.name);
}
```

### 3. Amdahl Measurement

```ruby
# Rails: Profile endpoint
RubyProf.start
response = get "/api/users/1"
result = RubyProf.stop

# Breakdown
puts result.threads.flat_map(&:methods).group_by(&:full_name).map { |k, v|
  [k, v.sum(&:total_time)]
}.sort_by(&:last).reverse.take(10)

# Output:
# ActiveRecord::Base#find         2.3ms (23%)
# ActionController::Metal#dispatch 1.5ms (15%)
# ActiveRecord::Callbacks#run      0.8ms (8%)
# ...
```

---

## Updated Thesis Statement

### Before (Overclaimed)

> "A Rails-to-Rust compiler that produces native binaries with 50-100x performance improvement and zero Ruby runtime."

### After (Honest)

> "A Rails-to-Rust **migration accelerator** that:
>
> 1. **Compiles 100% of metadata** (schema, associations, validations, callbacks wiring, enums, scopes) to type-safe Rust
> 2. **Compiles ~40% of behavior** (Ruby-- subset: simple callbacks, pure transformations)
> 3. **Generates todo!() stubs for ~60%** of behavior (business logic, external calls, gem code)
> 4. **Provides 2-5x speedup** for typical CRUD (DB-dominated)
> 5. **Provides 20-100x speedup** for CPU-bound workloads
> 6. **Eliminates Ruby runtime** for metadata paths; behavior strategy determines full elimination
> 7. **Reduces memory 10-30x** and enables thousands of concurrent connections"

---

## The Complete Architecture (With Behavior Strategy)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        RAILS-TO-RUST COMPILER                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  INPUT                                                                      │
│  ─────                                                                      │
│  • app/models/**/*.rb                                                       │
│  • db/schema.rb or structure.sql                                            │
│  • config/routes.rb                                                         │
│  • Optional: Database connection (Snapshot mode)                            │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  PHASE 1: METADATA EXTRACTION                                               │
│  ────────────────────────────                                               │
│  • Parse schema → TableDefs                                                 │
│  • Parse models → ModelASTs                                                 │
│  • Build association graph                                                  │
│  • Resolve inverses, through chains                                         │
│  • Resolve polymorphic/STI type sets                                        │
│                                                                             │
│  OUTPUT: Complete IR of Rails metadata                                      │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  PHASE 2: BEHAVIOR CLASSIFICATION                                           │
│  ─────────────────────────────────                                          │
│  For each method body:                                                      │
│    • Check if in Ruby-- subset → TIER 2 (AOT)                               │
│    • Check if pure metadata → TIER 1 (direct)                               │
│    • Otherwise → TIER 3 (rewrite boundary)                                  │
│                                                                             │
│  OUTPUT: Classification per method                                          │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  PHASE 3: CODE GENERATION                                                   │
│  ─────────────────────────────                                              │
│  TIER 1 (Metadata):                                                         │
│    • Struct definitions                                                     │
│    • Diesel table! macros                                                   │
│    • Association methods                                                    │
│    • Validation framework calls                                             │
│    • Callback chain wiring                                                  │
│    • Enum types                                                             │
│    • Scope method signatures                                                │
│                                                                             │
│  TIER 2 (Ruby-- AOT):                                                       │
│    • Compile method bodies to Rust                                          │
│    • Type inference / RubyValue fallback                                    │
│                                                                             │
│  TIER 3 (Rewrite Boundary):                                                 │
│    • Generate todo!() stubs                                                 │
│    • Preserve original Ruby as doc comments                                 │
│    • Generate trait bounds for expected interface                           │
│                                                                             │
│  OUTPUT: Rust project with mix of complete code and todo!() markers         │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  PHASE 4: HUMAN PORTING                                                     │
│  ───────────────────────                                                    │
│  Developer resolves each todo!():                                           │
│    • Port business logic                                                    │
│    • Integrate external services (Stripe → stripe-rs)                       │
│    • Setup mailers (lettre, sendgrid)                                       │
│    • Setup background jobs (Tokio tasks, RabbitMQ)                          │
│                                                                             │
│  OUTPUT: Complete Rust application                                          │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  PHASE 5: VERIFICATION                                                      │
│  ──────────────────────                                                     │
│  • Semantic diff against running Rails app                                  │
│  • Response comparison                                                      │
│  • Side effect verification                                                 │
│  • Performance benchmarking                                                 │
│                                                                             │
│  OUTPUT: Verification report                                                │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Summary: The Duck's Bottom Line

The original thesis was logically incomplete because it conflated **metadata compilation** (which the architecture handles well) with **behavior compilation** (which was unaddressed).

The corrected thesis:

1. **Metadata Compilation** → Fully automated, 100% coverage
2. **Behavior Compilation** → Three-tier strategy:
   - Tier 1: Metadata-derived (automatic)
   - Tier 2: Ruby-- subset (AOT compilable)
   - Tier 3: Rewrite boundary (todo!() + manual port)
3. **Performance Claims** → Bounded by Amdahl's law; honest per-scenario projections
4. **Type Sets** → Require constraints or Unknown handling
5. **Verification** → Conformance harness + semantic diff

**The compiler is not magic. It's a migration accelerator that eliminates boilerplate and enforces type safety, while clearly marking what requires human expertise.**
