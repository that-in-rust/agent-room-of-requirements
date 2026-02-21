# Scope Reframe: What Are We Actually Building?

## Date: 2026-02-06

## The Problem With "Rails-to-Rust Compiler"

The original thesis — "compile Rails apps to Rust binaries" — has a fundamental scope problem:

```
CLAIMED SCOPE:
  Rails App (all of it) → Magic Compiler → Rust Binary (same behavior)

ACTUAL CAPABILITY:
  Rails Metadata (schema, DSL) → Compiler → Rust Skeleton + todo!() stubs
  Rails Behavior (method bodies) → ??? → Manual port
```

**The name promises more than the technology can deliver.**

---

## Five Alternative Framings

### Option A: "ActiveRecord-to-Diesel Generator"

**Scope**: Just the ORM layer. Schema + models → Rust structs + Diesel.

```
WHAT IT DOES:
  ✓ schema.rb → Diesel table! macros
  ✓ Model classes → Rust structs with types
  ✓ Associations → Relation methods
  ✓ Validations → Validation trait calls
  ✓ Enums → Rust enums
  ✓ Scopes → Query builder methods

WHAT IT DOESN'T DO:
  ✗ Controllers
  ✗ Routes
  ✗ Views
  ✗ Business logic
  ✗ Background jobs
  ✗ Mailers
```

**Value proposition**: "Generate a type-safe Rust data layer from your Rails models. Use it for new Rust services that share your database."

**Use case**: Microservice extraction. Keep Rails monolith, add Rust services that need DB access.

**Honest claim**: 100% automatable for what it covers.

---

### Option B: "Rust Proxy with Rails Backend"

**Scope**: Rust handles HTTP + concurrency. Rails handles business logic via RPC.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        ARCHITECTURE                                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   Internet                                                                  │
│      │                                                                      │
│      ▼                                                                      │
│   ┌──────────────────────┐                                                  │
│   │   Rust Proxy (Axum)  │  ← Handles: TLS, rate limiting, auth tokens,    │
│   │   100k+ connections  │    request validation, response caching,        │
│   │   ~20MB memory       │    WebSocket fanout, static files               │
│   └──────────┬───────────┘                                                  │
│              │                                                              │
│              │ gRPC / HTTP (internal)                                       │
│              │                                                              │
│              ▼                                                              │
│   ┌──────────────────────┐                                                  │
│   │   Rails App (Puma)   │  ← Handles: Business logic, DB queries,         │
│   │   Existing codebase  │    validations, callbacks, all behavior         │
│   │   No code changes    │                                                  │
│   └──────────────────────┘                                                  │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Value proposition**: "10x your concurrent connection capacity without changing a line of Rails code."

**Use case**: WebSocket-heavy apps, API gateways, apps hitting Puma limits.

**Honest claim**: Zero Rails changes. Rust handles what Rails is bad at (concurrency), Rails handles what it's good at (business logic).

---

### Option C: "Rust Web Framework with Rails Ergonomics"

**Scope**: New framework. Not a compiler, but "Rails-like Rust."

```
// NOT THIS (compiled from Rails):
// Rails → Compiler → Rust

// THIS (new Rust framework inspired by Rails):
// Developer writes Rust with Rails-like patterns

#[model]
#[table = "users"]
struct User {
    id: i64,
    email: String,
    name: String,

    #[has_many]
    posts: Vec<Post>,

    #[validates(presence, uniqueness)]
    email: String,

    #[before_save(if = "email_changed")]
    fn normalize_email(&mut self) {
        self.email = self.email.to_lowercase();
    }
}

#[controller]
impl UsersController {
    #[action(GET, "/users")]
    async fn index(&self) -> Json<Vec<User>> {
        User::all().await
    }

    #[action(POST, "/users")]
    async fn create(&self, params: UserParams) -> Result<Json<User>, Error> {
        User::create(params).await
    }
}
```

**Value proposition**: "The productivity of Rails with the performance of Rust."

**Use case**: Greenfield projects. Teams that love Rails patterns but need Rust performance.

**Honest claim**: Not a migration tool. A new framework. Requires learning Rust.

**Prior art**: Loco.rs is already doing this.

---

### Option D: "Rails Migration Toolkit"

**Scope**: Tools that help humans migrate, not magic automation.

```
TOOLKIT COMPONENTS:

1. rails-analyze
   - Scan Rails codebase
   - Report: compilable %, manual port %, blockers
   - Output: migration plan document

2. rails-generate-schema
   - Generate Rust structs from schema.rb
   - Generate Diesel table! macros
   - 100% automatic

3. rails-generate-models
   - Generate model skeletons with todo!() markers
   - Preserve Ruby code as doc comments
   - Developer fills in behavior

4. rails-diff
   - Compare Rails vs Rust responses
   - Semantic equivalence testing
   - Regression detection

5. rails-migrate-incremental
   - Route-by-route migration support
   - Nginx config to split traffic
   - Gradual cutover
```

**Value proposition**: "Migrate Rails to Rust in 6 months instead of 18. Tools, not magic."

**Use case**: Companies committed to migration, want acceleration not automation.

**Honest claim**: Human effort required. Tools make it faster and safer.

---

### Option E: "Concurrency Sidecar for Rails"

**Scope**: Rust handles specific high-concurrency features. Rails stays for everything else.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        SIDECAR PATTERN                                       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   RAILS HANDLES:                    RUST SIDECAR HANDLES:                   │
│   ─────────────                     ────────────────────                    │
│   • CRUD operations                 • WebSocket connections                 │
│   • Business logic                  • Real-time notifications               │
│   • Admin dashboards                • Live updates                          │
│   • Background jobs                 • Presence tracking                     │
│   • Email                           • Pub/sub fanout                        │
│   • Authentication                  • Event streaming                       │
│                                                                             │
│   ┌─────────────────┐              ┌─────────────────┐                     │
│   │   Rails App     │◄────────────►│   Rust Sidecar  │                     │
│   │   (unchanged)   │   Redis/     │   (new code)    │                     │
│   │                 │   Kafka      │                 │                     │
│   └─────────────────┘              └─────────────────┘                     │
│          │                                │                                 │
│          │                                │                                 │
│          ▼                                ▼                                 │
│   HTTP Requests                    WebSocket Connections                    │
│   (low concurrency)                (high concurrency)                       │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Value proposition**: "Add real-time to Rails without replacing Rails."

**Use case**: Apps that need WebSocket/real-time but don't want to rewrite.

**Honest claim**: Additive, not replacement. Rails stays. Rust handles what Rails can't.

---

## Comparison Matrix

| Framing | Scope | Automation | Migration Effort | Value |
|---------|-------|------------|------------------|-------|
| **A: ORM Generator** | Data layer only | 100% | None (additive) | Microservices |
| **B: Rust Proxy** | HTTP layer only | 100% | None (additive) | Concurrency |
| **C: New Framework** | Greenfield only | N/A | N/A (new code) | Productivity |
| **D: Migration Toolkit** | Full migration | 50-70% | 6-18 months | Accelerator |
| **E: Sidecar** | Real-time only | 100% | None (additive) | Specific features |

---

## The Honest Reframe

### What We Should Stop Saying

```
❌ "Rails-to-Rust compiler"
❌ "Deploy Rails as Rust binary"
❌ "No Ruby runtime needed"
❌ "50-100x faster"
❌ "Zero migration effort"
```

### What We Should Start Saying

**If Option A (ORM Generator)**:
```
"Generate type-safe Rust data access from your Rails schema.
 Perfect for adding Rust microservices to a Rails monolith."
```

**If Option B (Rust Proxy)**:
```
"10x your concurrent connections with a Rust proxy.
 Zero changes to your Rails code."
```

**If Option C (New Framework)**:
```
"Rust web framework with Rails-like productivity.
 For teams starting new projects who want Rust performance."
```

**If Option D (Migration Toolkit)**:
```
"Accelerate Rails-to-Rust migration with analysis tools,
 code generators, and semantic diff testing."
```

**If Option E (Sidecar)**:
```
"Add real-time features to Rails with a Rust sidecar.
 WebSockets, presence, and live updates at scale."
```

---

## My Recommendation: Start With B + A

### Phase 1: Rust Proxy (Option B)

**Why first**:
- Zero Rails changes required
- Immediate value (concurrency)
- Proves the concept
- Low risk

**Deliverable**: Open-source Rust proxy that sits in front of Rails.

### Phase 2: ORM Generator (Option A)

**Why second**:
- Builds on proxy success
- Enables Rust microservices
- Still additive, not replacement
- 100% automatable

**Deliverable**: `rails-to-diesel` CLI tool.

### Phase 3: Migration Toolkit (Option D)

**Why third**:
- Only after proving B + A work
- Bigger commitment from users
- More complex tooling
- Requires behavior strategy

**Deliverable**: `rails-migrate` suite of tools.

---

## The Pivot Statement

### From:
> "We're building a Rails-to-Rust compiler that converts your entire Rails application into a native Rust binary with 50-100x performance improvement."

### To:
> "We're building tools for Rails teams that need Rust performance:
>
> 1. **Rust Proxy**: Handle 100k+ connections without changing Rails
> 2. **ORM Generator**: Type-safe Rust data layer from your schema
> 3. **Migration Toolkit**: When you're ready to fully migrate
>
> Start with what you need. Grow as your needs grow."

---

## Why This Reframe Works

### 1. Honest About Capabilities

Each tool does exactly what it claims. No "magic compiler" promises.

### 2. Incremental Adoption

Companies can start small (proxy) and expand (ORM, full migration) as they gain confidence.

### 3. Multiple Entry Points

- Need concurrency? Start with proxy.
- Need microservices? Start with ORM generator.
- Need full migration? Use the toolkit.

### 4. Each Piece Is Valuable Alone

Even if a company never fully migrates, the proxy and ORM generator are useful.

### 5. Matches Reality

The "behavior gap" is addressed by either:
- Not touching behavior (B, E)
- Generating only data layer (A)
- Acknowledging manual work (D)
- New code, not migration (C)

---

## Next Steps

1. **Decide on initial focus**: B (proxy) or A (ORM generator)?

2. **Build MVP**:
   - Proxy: Axum + hyper + config for Rails backends
   - ORM: schema.rb parser + Diesel codegen

3. **Validate with real Rails apps**:
   - Can we proxy a real app?
   - Does generated ORM compile?

4. **Iterate based on feedback**

5. **Expand scope only after success**

---

## Summary

The "Rails-to-Rust compiler" framing is broken because it promises automatic behavior compilation that isn't possible.

The reframe:
- **Proxy** = Rust handles HTTP, Rails handles logic (additive)
- **ORM Generator** = Rust data layer from Rails schema (additive)
- **Migration Toolkit** = Tools for human-driven migration (accelerator)
- **Sidecar** = Rust for real-time features only (additive)
- **New Framework** = Rails-like Rust for greenfield (not migration)

Each is honest about what it does. Each delivers real value. Each avoids the "behavior gap" problem by either not touching behavior, or acknowledging it requires human work.

**The question isn't "can we compile Rails to Rust?" It's "what do Rails teams actually need from Rust?"**
