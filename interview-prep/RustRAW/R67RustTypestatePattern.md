# R67: Rust Typestate Pattern - Compile-Time State Machine Enforcement

## Part 1: The Problem - Runtime Validation of Invalid States

### 1.1 Why Invalid States Matter

**The typestate pattern eliminates impossible states at compile time by encoding state machines into the type system, preventing entire classes of bugs before your program runs.**

Traditional approaches force runtime validation:

```mermaid
flowchart TD
    subgraph TRADITIONAL["❌ RUNTIME STATE VALIDATION"]
        direction TB
        
        STATE1["struct Ticket {
        id: Option&lt;TicketId&gt;,
        title: String,
        status: Status
        }
        "]
        
        STATE1 --> CHECK1{"id.is_none()?"}
        CHECK1 -->|"Yes"| PANIC1["❌ panic!(uncreated ticket)"]
        CHECK1 -->|"No"| USE1["✅ Can use id"]
        
        STATE1 --> CHECK2{"is_draft()?"}
        CHECK2 -->|"Yes"| PANIC2["❌ Can't have status"]
        CHECK2 -->|"No"| USE2["✅ Can read status"]
    end
    
    PROBLEM["😰 THE DILEMMA:
    Every retrieval checks Option&lt;TicketId&gt;
    Status exists even when meaningless
    Runtime panics for logic errors"]
    
    CHECK1 --> PROBLEM
    CHECK2 --> PROBLEM
    
    style STATE1 fill:#f5f5f5,stroke:#333,color:#000
    style CHECK1 fill:#e0e0e0,stroke:#333,color:#000
    style CHECK2 fill:#e0e0e0,stroke:#333,color:#000
    style PANIC1 fill:#bfbfbf,stroke:#333,color:#000
    style PANIC2 fill:#bfbfbf,stroke:#333,color:#000
    style USE1 fill:#e8e8e8,stroke:#333,color:#000
    style USE2 fill:#e8e8e8,stroke:#333,color:#000
    style PROBLEM fill:#cccccc,stroke:#333,color:#000
```

**The pain**: You must defensively check `Option<TicketId>` every time you retrieve a ticket, even though conceptually "a stored ticket ALWAYS has an ID." Status fields exist in drafts where they're meaningless. The compiler can't help—it allows `Ticket { id: None, status: Closed }`.

---

### 1.2 Two Conflicting Requirements

```mermaid
flowchart LR
    subgraph REQUIREMENT["😰 CONFLICTING NEEDS"]
        direction TB
        
        REQ1["📝 REQUIREMENT 1:
        ════════════════════
        Draft tickets NEED:
        • No ID (not created yet)
        • No status (doesn't exist)
        • title + description only"]
        
        REQ2["💾 REQUIREMENT 2:
        ════════════════════
        Stored tickets NEED:
        • Guaranteed ID (unique)
        • Current status
        • title + description
        • NEVER optional fields"]
    end
    
    NAIVE["🤷 Naive Approach:
    ═════════════════════
    Make ID/status Optional
    Check everywhere
    Runtime validation"]
    
    REQ1 --> NAIVE
    REQ2 --> NAIVE
    
    NAIVE --> WASTE["💸 WASTE:
    Redundant checks
    Runtime panics
    Invalid representations"]
    
    style REQ1 fill:#f5f5f5,stroke:#333,color:#000
    style REQ2 fill:#e8e8e8,stroke:#333,color:#000
    style NAIVE fill:#d9d9d9,stroke:#333,color:#000
    style WASTE fill:#bfbfbf,stroke:#333,color:#000
```

**The insight**: Drafts and stored tickets are fundamentally different states with different invariants. Representing them with the same type forces compromises (optional fields) that create maintenance burden and bugs.

---

## Part 2: The Solution - Separate Types for Each State

### 2.1 Typestate Pattern Core Idea

**Instead of runtime checks on optional fields, create separate types for each state—making invalid states unrepresentable.**

```mermaid
flowchart TD
    subgraph TYPESTATE["✅ TYPESTATE PATTERN"]
        direction TB
        
        DRAFT["struct TicketDraft {
        title: TicketTitle,
        description: TicketDescription
        }
        ══════════════════════════════
        • No ID field exists
        • No status field exists
        • Can't compile with id.unwrap()"]
        
        STORED["struct Ticket {
        id: TicketId,  // NOT Option!
        title: TicketTitle,
        description: TicketDescription,
        status: Status
        }
        ══════════════════════════════
        • ID always present
        • Status always present
        • No runtime checks needed"]
        
        TRANS["fn create(draft: TicketDraft) 
        → Ticket {
        Ticket {
            id: generate_id(),
            title: draft.title,
            description: draft.description,
            status: Status::Open
        }
        }"]
    end
    
    DRAFT --> TRANS
    TRANS --> STORED
    
    BENEFIT["✅ COMPILE-TIME GUARANTEES:
    Can't read ID from draft (no field)
    Can't forget to set status (required)
    Can't store draft (type mismatch)"]
    
    TRANS --> BENEFIT
    
    style DRAFT fill:#e8e8e8,stroke:#333,color:#000
    style STORED fill:#d4d4d4,stroke:#333,color:#000
    style TRANS fill:#f5f5f5,stroke:#333,color:#000
    style BENEFIT fill:#e0e0e0,stroke:#333,color:#000
```

**Key insight**: By making `id` and `status` non-optional in `Ticket` and absent in `TicketDraft`, the compiler enforces state invariants—you literally cannot write code that accesses an ID on a draft.

---

### 2.2 State Transition as Function Signatures

```mermaid
flowchart LR
    subgraph TRANSITIONS["🔄 STATE MACHINE AS TYPES"]
        direction LR
        
        STATE1["TicketDraft
        ═══════════════
        User creates
        No ID yet"]
        
        STATE2["Ticket
        ═══════════════
        System assigned ID
        Has Status"]
        
        STATE3["ArchivedTicket
        ═══════════════
        Immutable history
        Read-only"]
        
        STATE1 -->|"fn create(TicketDraft) → Ticket"| STATE2
        STATE2 -->|"fn archive(Ticket) → ArchivedTicket"| STATE3
    end
    
    OWNERSHIP["🔐 OWNERSHIP ENFORCEMENT:
    Transitions consume old state
    Can't use TicketDraft after create()
    Type signature = state contract"]
    
    STATE2 --> OWNERSHIP
    
    style STATE1 fill:#f5f5f5,stroke:#333,color:#000
    style STATE2 fill:#e0e0e0,stroke:#333,color:#000
    style STATE3 fill:#cccccc,stroke:#333,color:#000
    style OWNERSHIP fill:#e8e8e8,stroke:#333,color:#000
```

**Pattern**: State transitions are functions that take ownership of the old state (consuming it) and return the new state. Once you call `create(draft)`, the `draft` is moved—you can't accidentally use it again.

---

## Part 3: Mental Model - Vision's Mind Stone Calibration Protocol

### 3.1 The MCU Metaphor

**The Vision creation sequence in *Avengers: Age of Ultron*—incomplete vessel → complete android → activated Mind Stone bearer—mirrors typestate transitions.**

```mermaid
flowchart TD
    subgraph MCU["🎬 MCU: VISION'S CREATION PROTOCOL"]
        direction TB
        
        CRADLE["⚙️ REGENERATION CRADLE
        ═══════════════════════════
        State: Incomplete (VisionDraft)
        Components: Synthetic tissue, vibranium
        Missing: Mind Stone, consciousness
        Can't: Think, act, exist independently"]
        
        BODY["🤖 COMPLETE BODY
        ═══════════════════════════
        State: Assembled (Vision)
        Components: Full android body + Mind Stone
        Capabilities: Consciousness, powers
        Can't: Return to cradle (consumed)"]
        
        ACTIVE["💎 ACTIVATED VISION
        ═══════════════════════════
        State: Fully Operational
        Components: Everything + experience
        Capabilities: Infinity Stone mastery
        Irreversible: Can't undo consciousness"]
        
        CRADLE -->|"Thor's lightning
        (fn create)"| BODY
        BODY -->|"First words
        (fn activate)"| ACTIVE
    end
    
    IMPOSSIBLE["❌ IMPOSSIBLE SCENARIOS:
    Can't think without Mind Stone (no field)
    Can't put consciousness back in cradle (consumed)
    Can't be half-assembled (type enforced)"]
    
    ACTIVE --> IMPOSSIBLE
    
    style CRADLE fill:#f5f5f5,stroke:#333,color:#000
    style BODY fill:#e0e0e0,stroke:#333,color:#000
    style ACTIVE fill:#d4d4d4,stroke:#333,color:#000
    style IMPOSSIBLE fill:#cccccc,stroke:#333,color:#000
```

---

### 3.2 MCU-to-Rust Mapping Table

| MCU Concept | Rust Typestate | Enforced Invariant |
|-------------|----------------|-------------------|
| **Regeneration Cradle (incomplete)** | `TicketDraft` | No ID/status fields exist—can't access what isn't there |
| **Complete Body (Mind Stone inserted)** | `Ticket` | ID/status are non-optional—always present, no runtime checks |
| **Activated Vision (conscious)** | `ArchivedTicket` | Immutable history—can't modify archived state |
| **Thor's lightning (creation)** | `fn create(draft: TicketDraft) → Ticket` | Consumes draft via ownership—can't reuse old state |
| **First words (activation)** | `fn activate(ticket: Ticket) → Active` | Transition function signature encodes valid flow |
| **Can't think without Stone** | Compiler error: `draft.id` | Field doesn't exist on that type—caught at compile time |
| **Can't return to cradle** | Ownership moved | Once `create()` called, `draft` is gone—prevents misuse |

**Narrative**: When Ultron's cradle holds the incomplete Vision body, it's like `TicketDraft`—you can't query its Mind Stone status because that field doesn't exist yet. Thor's lightning (the `create` function) consumes the cradle contents (moves ownership) and returns a complete Vision (`Ticket` with guaranteed ID). Once activated, Vision can't be disassembled back into the cradle—the state transition is one-way, enforced by consuming the previous state through ownership.

Just as you can't ask "what are Vision's thoughts?" while he's still in the cradle (the question is meaningless), Rust's compiler won't let you write `draft.id` because `TicketDraft` has no such field. The type system makes impossible states unrepresentable.

---

## Part 4: Anatomy of Typestate Pattern

### 4.1 State Type Definitions

```mermaid
flowchart TD
    subgraph STATES["📦 TYPE DEFINITIONS"]
        direction TB
        
        subgraph DRAFT["struct TicketDraft"]
            D_TITLE["title: TicketTitle"]
            D_DESC["description: TicketDescription"]
        end
        
        subgraph TICKET["struct Ticket"]
            T_ID["id: TicketId  // NOT Option!"]
            T_TITLE["title: TicketTitle"]
            T_DESC["description: TicketDescription"]
            T_STATUS["status: Status"]
        end
        
        subgraph ARCHIVED["struct ArchivedTicket"]
            A_ID["id: TicketId"]
            A_TITLE["title: TicketTitle"]
            A_DESC["description: TicketDescription"]
            A_CLOSED["closed_at: Timestamp"]
        end
    end
    
    FIELDS["🔧 FIELD STRATEGY:
    Only include fields valid for that state
    Make all fields non-optional
    Share validated types (TicketTitle, etc.)"]
    
    TICKET --> FIELDS
    
    style DRAFT fill:#f5f5f5,stroke:#333,color:#000
    style TICKET fill:#e0e0e0,stroke:#333,color:#000
    style ARCHIVED fill:#d4d4d4,stroke:#333,color:#000
    style D_TITLE fill:#e8e8e8,stroke:#333,color:#000
    style D_DESC fill:#e8e8e8,stroke:#333,color:#000
    style T_ID fill:#e8e8e8,stroke:#333,color:#000
    style T_TITLE fill:#e8e8e8,stroke:#333,color:#000
    style T_DESC fill:#e8e8e8,stroke:#333,color:#000
    style T_STATUS fill:#e8e8e8,stroke:#333,color:#000
    style A_ID fill:#e8e8e8,stroke:#333,color:#000
    style A_TITLE fill:#e8e8e8,stroke:#333,color:#000
    style A_DESC fill:#e8e8e8,stroke:#333,color:#000
    style A_CLOSED fill:#e8e8e8,stroke:#333,color:#000
    style FIELDS fill:#cccccc,stroke:#333,color:#000
```

**Critical pattern**: Each state type contains *only* the fields that make sense for that state. No `Option` wrappers, no nullable fields. `TicketDraft` physically cannot have an `id` field—accessing `draft.id` is a compiler error, not a runtime check.

**Validation reuse**: Notice `title: TicketTitle` appears in all three types. The validation logic lives in `TicketTitle`'s constructor—each state reuses the validated type without duplicating validation code.

---

### 4.2 Transition Functions

```mermaid
flowchart LR
    subgraph TRANSITIONS["🔄 STATE TRANSITION FUNCTIONS"]
        direction LR
        
        CREATE["fn create(
        draft: TicketDraft
        ) → Ticket
        ══════════════════════
        • Takes ownership
        • Generates ID
        • Assigns initial status
        • Returns new state"]
        
        UPDATE["fn update(
        mut self,
        changes: Changes
        ) → Self
        ══════════════════════
        • Consumes self
        • Validates changes
        • Returns modified state"]
        
        ARCHIVE["fn archive(
        self
        ) → ArchivedTicket
        ══════════════════════
        • Consumes Ticket
        • Records timestamp
        • Immutable result"]
        
        CREATE --> UPDATE
        UPDATE --> ARCHIVE
    end
    
    OWNERSHIP["🔐 OWNERSHIP PATTERN:
    All transitions take self/input by value
    Previous state becomes unavailable
    Can't accidentally reuse old state"]
    
    ARCHIVE --> OWNERSHIP
    
    style CREATE fill:#f5f5f5,stroke:#333,color:#000
    style UPDATE fill:#e0e0e0,stroke:#333,color:#000
    style ARCHIVE fill:#d4d4d4,stroke:#333,color:#000
    style OWNERSHIP fill:#cccccc,stroke:#333,color:#000
```

**Key mechanism**: Every transition function consumes the input state via ownership. After `let ticket = create(draft);`, the variable `draft` is moved—attempting to use it again produces a compiler error: "value borrowed after move."

**Method syntax**: Notice `update` uses `self` (not `&self`), meaning it consumes the `Ticket` and returns a new one. This is the builder pattern merged with typestate—you chain transitions while the compiler tracks state validity.

---

### 4.3 Complete Lifecycle Example

```rust
// Step 1: Create draft (no ID, no status)
let draft = TicketDraft {
    title: TicketTitle::new("Fix bug")?,
    description: TicketDescription::new("Details here")?,
};

// Compiler error if you try:
// println!("{}", draft.id);  // ERROR: no field `id` on type `TicketDraft`

// Step 2: Transition to Ticket (creates ID, assigns status)
let ticket = create(draft);

// Compiler error if you try:
// println!("{}", draft.title);  // ERROR: value borrowed after move

// Step 3: Ticket operations (ID and status guaranteed present)
println!("Ticket ID: {}", ticket.id);  // No Option unwrapping!
println!("Status: {:?}", ticket.status);  // Always valid

// Step 4: Archive (consume Ticket, produce ArchivedTicket)
let archived = archive(ticket);

// Compiler error if you try:
// println!("{}", ticket.id);  // ERROR: value borrowed after move
```

---

## Part 5: Common Typestate Patterns

### 5.1 The Builder Pattern Typestate

```mermaid
flowchart LR
    subgraph BUILDER["🏗️ BUILDER WITH TYPESTATE"]
        direction LR
        
        UNINIT["ConfigBuilder&lt;Uninitialized&gt;
        ═══════════════════════════════════
        • No fields set
        • Can't call build()
        • Must set required fields"]
        
        PARTIAL["ConfigBuilder&lt;PartialConfig&gt;
        ═══════════════════════════════════
        • Some fields set
        • Can't call build() yet
        • Type tracks what's missing"]
        
        READY["ConfigBuilder&lt;ReadyToBuild&gt;
        ═══════════════════════════════════
        • All required fields set
        • Can call build()
        • Compiler enforces completeness"]
        
        UNINIT -->|"set_host()"| PARTIAL
        PARTIAL -->|"set_port()"| READY
        READY -->|"build()"| CONFIG["Config
        ═══════════════
        Immutable
        Complete"]
    end
    
    PHANTOM["🎭 PhantomData&lt;State&gt;:
    Zero-sized marker type
    Tracks state at compile time
    No runtime cost"]
    
    READY --> PHANTOM
    
    style UNINIT fill:#f5f5f5,stroke:#333,color:#000
    style PARTIAL fill:#e0e0e0,stroke:#333,color:#000
    style READY fill:#d4d4d4,stroke:#333,color:#000
    style CONFIG fill:#cccccc,stroke:#333,color:#000
    style PHANTOM fill:#e8e8e8,stroke:#333,color:#000
```

**Pattern**: Use generic type parameters (`ConfigBuilder<State>`) with marker types (`Uninitialized`, `ReadyToBuild`) to track builder state. Only implement `build()` on `ConfigBuilder<ReadyToBuild>` so the compiler prevents calling it prematurely.

**Zero cost**: The state markers are `PhantomData<State>`—they occupy zero bytes at runtime. The state tracking is purely compile-time information.

---

### 5.2 Protocol State Machines

```mermaid
flowchart TD
    subgraph PROTOCOL["🔌 TCP-LIKE CONNECTION STATES"]
        direction TB
        
        CLOSED["TcpStream&lt;Closed&gt;
        ════════════════════════
        • Socket created
        • Not connected
        • Can: connect()
        • Can't: send(), recv()"]
        
        CONNECTING["TcpStream&lt;Connecting&gt;
        ════════════════════════
        • Connection in progress
        • Can: wait_established()
        • Can't: send(), recv()"]
        
        ESTABLISHED["TcpStream&lt;Established&gt;
        ════════════════════════
        • Connected and ready
        • Can: send(), recv(), close()
        • Can't: connect() again"]
        
        CLOSED -->|"fn connect(self) → TcpStream&lt;Connecting&gt;"| CONNECTING
        CONNECTING -->|"fn wait_established(self) → TcpStream&lt;Established&gt;"| ESTABLISHED
        ESTABLISHED -->|"fn close(self) → TcpStream&lt;Closed&gt;"| CLOSED
    end
    
    ENFORCEMENT["⚖️ COMPILER ENFORCEMENT:
    Can't call send() on Closed stream
    Can't connect() on Established stream
    State transitions = type transformations"]
    
    ESTABLISHED --> ENFORCEMENT
    
    style CLOSED fill:#f5f5f5,stroke:#333,color:#000
    style CONNECTING fill:#e0e0e0,stroke:#333,color:#000
    style ESTABLISHED fill:#d4d4d4,stroke:#333,color:#000
    style ENFORCEMENT fill:#cccccc,stroke:#333,color:#000
```

**Real-world use**: This pattern appears in:
- **tokio_postgres**: `Client` vs `Transaction` types (can't start transaction on transaction)
- **hyper**: `Request<Empty>` vs `Request<Body>` (can't send body twice)
- **rusqlite**: `Statement` vs `Rows` (can't mix prepare and execute)

---

### 5.3 Generic State Parameter Pattern

```rust
// Define marker types for each state
pub struct Draft;
pub struct Active;
pub struct Archived;

// Generic type with state parameter
pub struct Ticket<State> {
    id: Option<TicketId>,  // Optional in Draft, guaranteed in Active/Archived
    title: TicketTitle,
    description: TicketDescription,
    status: Status,
    _state: PhantomData<State>,
}

// Implement state-specific constructors
impl Ticket<Draft> {
    pub fn new(title: TicketTitle, description: TicketDescription) -> Self {
        Self {
            id: None,  // No ID yet
            title,
            description,
            status: Status::Open,
            _state: PhantomData,
        }
    }
    
    // Transition to Active
    pub fn create(self, id: TicketId) -> Ticket<Active> {
        Ticket {
            id: Some(id),  // Now has ID
            title: self.title,
            description: self.description,
            status: self.status,
            _state: PhantomData,
        }
    }
}

// Only Active tickets can be archived
impl Ticket<Active> {
    pub fn archive(self) -> Ticket<Archived> {
        Ticket {
            id: self.id,
            title: self.title,
            description: self.description,
            status: Status::Closed,
            _state: PhantomData,
        }
    }
}
```

**Trade-off**: This approach uses a single struct with generic state parameters, reducing code duplication but still requiring `Option<TicketId>`. Better for cases where many fields are shared across states.

---

## Part 6: Real-World Use Cases

### 6.1 Database Transaction States

```mermaid
flowchart TD
    subgraph DB["💾 DATABASE TRANSACTION LIFECYCLE"]
        direction TB
        
        CONN["Connection&lt;Idle&gt;
        ══════════════════════
        • No transaction active
        • Can: begin_transaction()
        • Can't: commit(), rollback()"]
        
        TRANS["Connection&lt;InTransaction&gt;
        ══════════════════════
        • Transaction active
        • Can: query(), commit(), rollback()
        • Can't: begin_transaction() again"]
        
        COMMITTED["Connection&lt;Idle&gt;
        ══════════════════════
        • Transaction committed
        • Can: begin_transaction()
        • Previous transaction consumed"]
        
        CONN -->|"begin_transaction(self)"| TRANS
        TRANS -->|"commit(self)"| COMMITTED
        TRANS -->|"rollback(self)"| ROLLBACK["Connection&lt;Idle&gt;
        (rolled back)"]
    end
    
    BENEFIT["✅ SAFETY BENEFITS:
    Can't forget to commit (must consume transaction)
    Can't nest transactions (type mismatch)
    Can't query after commit (moved)"]
    
    TRANS --> BENEFIT
    
    style CONN fill:#f5f5f5,stroke:#333,color:#000
    style TRANS fill:#e0e0e0,stroke:#333,color:#000
    style COMMITTED fill:#d4d4d4,stroke:#333,color:#000
    style ROLLBACK fill:#cccccc,stroke:#333,color:#000
    style BENEFIT fill:#e8e8e8,stroke:#333,color:#000
```

**Example**: The `diesel` ORM uses this pattern—`Connection::transaction()` returns a `Transaction` type that must be explicitly committed or rolled back. The compiler prevents you from forgetting.

---

### 6.2 API Client Authentication States

```mermaid
flowchart LR
    subgraph CLIENT["🔐 API CLIENT AUTHENTICATION FLOW"]
        direction LR
        
        UNAUTH["ApiClient&lt;Unauthenticated&gt;
        ═══════════════════════════════════
        • No credentials
        • Can: login()
        • Can't: call_api()"]
        
        AUTH["ApiClient&lt;Authenticated&gt;
        ═══════════════════════════════════
        • Has valid token
        • Can: call_api(), logout()
        • Can't: login() again"]
        
        EXPIRED["ApiClient&lt;TokenExpired&gt;
        ═══════════════════════════════════
        • Token invalid
        • Can: refresh_token(), login()
        • Can't: call_api()"]
        
        UNAUTH -->|"login(self, creds)"| AUTH
        AUTH -->|"logout(self)"| UNAUTH
        AUTH -->|"(auto-detect)"| EXPIRED
        EXPIRED -->|"refresh_token(self)"| AUTH
    end
    
    SECURITY["🔒 SECURITY BENEFITS:
    Can't make API calls without authentication
    Token lifetime tracked by type
    Forces explicit re-authentication"]
    
    AUTH --> SECURITY
    
    style UNAUTH fill:#f5f5f5,stroke:#333,color:#000
    style AUTH fill:#e0e0e0,stroke:#333,color:#000
    style EXPIRED fill:#d4d4d4,stroke:#333,color:#000
    style SECURITY fill:#cccccc,stroke:#333,color:#000
```

**Real implementation**: The `aws-sdk-rust` uses similar patterns—unauthenticated clients cannot call AWS APIs, enforced by the type system.

---

### 6.3 File Handle State Management

```mermaid
flowchart TD
    subgraph FILE["📁 FILE HANDLE STATES"]
        direction TB
        
        UNOPENED["File&lt;Unopened&gt;
        ══════════════════════
        • Path specified
        • Can: open(), create()
        • Can't: read(), write()"]
        
        READONLY["File&lt;ReadOnly&gt;
        ══════════════════════
        • Opened for reading
        • Can: read(), seek()
        • Can't: write()"]
        
        WRITEONLY["File&lt;WriteOnly&gt;
        ══════════════════════
        • Opened for writing
        • Can: write(), seek()
        • Can't: read()"]
        
        READWRITE["File&lt;ReadWrite&gt;
        ══════════════════════
        • Opened for both
        • Can: read(), write(), seek()"]
        
        UNOPENED -->|"open_read(self)"| READONLY
        UNOPENED -->|"open_write(self)"| WRITEONLY
        UNOPENED -->|"open_readwrite(self)"| READWRITE
    end
    
    PERMISSIONS["🔐 PERMISSION ENFORCEMENT:
    Compiler prevents writes to read-only files
    Prevents reads from write-only files
    OS permissions = type system guarantee"]
    
    READONLY --> PERMISSIONS
    WRITEONLY --> PERMISSIONS
    
    style UNOPENED fill:#f5f5f5,stroke:#333,color:#000
    style READONLY fill:#e0e0e0,stroke:#333,color:#000
    style WRITEONLY fill:#e0e0e0,stroke:#333,color:#000
    style READWRITE fill:#d4d4d4,stroke:#333,color:#000
    style PERMISSIONS fill:#cccccc,stroke:#333,color:#000
```

**Real-world library**: The `typestate-file` crate implements exactly this, making file permission errors impossible at compile time.

---

## Part 7: Performance Characteristics

### 7.1 Zero-Cost Abstraction Guarantee

```mermaid
flowchart TD
    subgraph COMPILE["⚙️ COMPILE-TIME TRANSFORMATION"]
        direction TB
        
        SOURCE["// Source code
        let draft = TicketDraft { ... };
        let ticket = create(draft);
        println!('{}', ticket.id);"]
        
        MONOMORPH["🔧 MONOMORPHIZATION:
        Generic types become concrete
        State markers erased
        Function signatures specialized"]
        
        OPTIMIZED["// Optimized assembly
        mov rax, [ticket_id]
        call println
        
        (No state checks)
        (No PhantomData bytes)
        (Zero overhead)"]
        
        SOURCE --> MONOMORPH
        MONOMORPH --> OPTIMIZED
    end
    
    GUARANTEE["✅ ZERO-COST GUARANTEE:
    State transitions = no runtime code
    PhantomData&lt;State&gt; = 0 bytes
    Identical performance to manual state tracking"]
    
    OPTIMIZED --> GUARANTEE
    
    style SOURCE fill:#f5f5f5,stroke:#333,color:#000
    style MONOMORPH fill:#e0e0e0,stroke:#333,color:#000
    style OPTIMIZED fill:#d4d4d4,stroke:#333,color:#000
    style GUARANTEE fill:#cccccc,stroke:#333,color:#000
```

**Key insight**: The state parameters (`<Draft>`, `<Active>`) are purely compile-time metadata. The final binary contains no state checks, no type wrappers, no overhead—the compiler erases all the safety machinery, leaving only the underlying data.

**Measurement**: Benchmark comparisons show typestate implementations compile to identical assembly as hand-rolled state machines, but with compile-time safety.

---

### 7.2 Compilation Cost

```mermaid
flowchart LR
    subgraph COST["⏱️ COMPILE-TIME COST"]
        direction LR
        
        SMALL["Small Type Count:
        ═══════════════════════
        3-5 state types
        ~ 10 transition functions
        
        Overhead: Minimal
        Compile time: +2-5%"]
        
        LARGE["Large State Space:
        ═══════════════════════
        20+ state types
        100+ specialized methods
        
        Overhead: Moderate
        Compile time: +15-30%
        Binary size: +10-20%"]
        
        GENERIC["Generic State Param:
        ═══════════════════════
        Single struct + markers
        PhantomData
        
        Overhead: Minimal
        Compile time: +1-3%"]
    end
    
    TRADE["⚖️ TRADE-OFF ANALYSIS:
    Compile-time cost → Runtime safety
    Increased type count → Better errors
    Worth it for critical state machines"]
    
    LARGE --> TRADE
    
    style SMALL fill:#f5f5f5,stroke:#333,color:#000
    style LARGE fill:#e0e0e0,stroke:#333,color:#000
    style GENERIC fill:#d4d4d4,stroke:#333,color:#000
    style TRADE fill:#cccccc,stroke:#333,color:#000
```

**Recommendation**: For simple state machines (3-10 states), the compilation cost is negligible. For complex state spaces (20+ states), consider the generic parameter approach or evaluate if the safety benefits justify the cost.

---

## Part 8: Comparison to Other Patterns

### 8.1 Typestate vs Runtime State Machines

```mermaid
flowchart TD
    subgraph COMPARISON["⚖️ TYPESTATE VS RUNTIME STATE ENUM"]
        direction TB
        
        subgraph RUNTIME["Runtime State Enum"]
            RT_DEF["enum TicketState {
            Draft { title, desc },
            Active { id, title, desc, status },
            Archived { id, closed_at }
            }"]
            
            RT_CHECK["fn get_id(ticket: &TicketState) 
            → Option&lt;TicketId&gt; {
            match ticket {
                Draft { .. } ⇒ None,
                Active { id, .. } ⇒ Some(*id),
                Archived { id, .. } ⇒ Some(*id),
            }
            }"]
        end
        
        subgraph TYPESTATE_PATTERN["Typestate Pattern"]
            TS_DEF["struct TicketDraft { title, desc }
            struct Ticket { id, title, desc, status }
            struct ArchivedTicket { id, closed_at }"]
            
            TS_CHECK["fn get_id(ticket: &Ticket) 
            → TicketId {
            ticket.id  // Always present!
            }
            
            // Draft has no get_id() method"]
        end
    end
    
    RUNTIME --> RT_CHECK
    TYPESTATE_PATTERN --> TS_CHECK
    
    style RT_DEF fill:#f5f5f5,stroke:#333,color:#000
    style RT_CHECK fill:#e8e8e8,stroke:#333,color:#000
    style TS_DEF fill:#e0e0e0,stroke:#333,color:#000
    style TS_CHECK fill:#d4d4d4,stroke:#333,color:#000
```

**When to use each**:

| Scenario | Runtime Enum | Typestate Pattern |
|----------|--------------|------------------|
| **States known at runtime** | ✅ Best choice | ❌ Can't represent dynamic states |
| **State transitions sequential** | 🤷 Works but verbose | ✅ Compiler-enforced flow |
| **Invalid state access critical** | 🤷 Requires exhaustive match | ✅ Compile error, impossible to access |
| **Need to store mixed states** | ✅ `Vec<TicketState>` easy | ❌ Can't mix `Vec<TicketDraft>` + `Vec<Ticket>` |
| **Builder APIs** | ❌ Can't enforce required fields | ✅ Perfect fit |
| **Protocol implementations** | ❌ Easy to call wrong method | ✅ Type-safe API |

---

### 8.2 Typestate vs Option-Based Design

```mermaid
flowchart LR
    subgraph OPTIONS["🤷 OPTION-BASED (Traditional)"]
        direction TB
        
        OPT_STRUCT["struct Ticket {
        id: Option&lt;TicketId&gt;,
        status: Option&lt;Status&gt;,
        title: String
        }"]
        
        OPT_USE["// Must check everywhere
        if let Some(id) = ticket.id {
        println!('{}', id);
        } else {
        panic!('No ID!');
        }"]
    end
    
    subgraph TYPESTATE_VS["✅ TYPESTATE (Safe)"]
        direction TB
        
        TS_STRUCT["struct TicketDraft { title }
        struct Ticket { id, title, status }"]
        
        TS_USE["// No checks needed
        println!('{}', ticket.id);
        
        // Compiler prevents:
        println!('{}', draft.id);"]
    end
    
    OPT_STRUCT --> OPT_USE
    TS_STRUCT --> TS_USE
    
    style OPT_STRUCT fill:#f5f5f5,stroke:#333,color:#000
    style OPT_USE fill:#e8e8e8,stroke:#333,color:#000
    style TS_STRUCT fill:#e0e0e0,stroke:#333,color:#000
    style TS_USE fill:#d4d4d4,stroke:#333,color:#000
```

**Migration path**: If you have an existing codebase with `Option`-based state, you can refactor incrementally:
1. Identify distinct states with different invariants
2. Create separate types for each state
3. Replace `Option<T>` with state-specific fields
4. Update functions to use state-specific types
5. Remove runtime checks (now compile errors)

---

## Part 9: Best Practices and Gotchas

### 9.1 When to Use Typestate

```mermaid
flowchart TD
    subgraph DECISION["🎯 WHEN TO USE TYPESTATE"]
        direction TB
        
        YES["✅ EXCELLENT FIT:
        ════════════════════════════════
        • Sequential state transitions (A→B→C)
        • States have different capabilities
        • Invalid state access is critical bug
        • Builder APIs with required fields
        • Protocol implementations
        • Resource lifecycle management"]
        
        MAYBE["🤷 CONSIDER ALTERNATIVES:
        ════════════════════════════════
        • States determined at runtime
        • Need to store heterogeneous states
        • Simple boolean flags suffice
        • States frequently mixed
        • Prototyping (overhead not justified)"]
        
        NO["❌ AVOID:
        ════════════════════════════════
        • Dynamic state machines (user-defined)
        • States loaded from config/database
        • Hot-reloading state definitions
        • FFI boundaries (C API)
        • State persistence (serialization)"]
    end
    
    YES --> MAYBE
    MAYBE --> NO
    
    style YES fill:#e8e8e8,stroke:#333,color:#000
    style MAYBE fill:#d9d9d9,stroke:#333,color:#000
    style NO fill:#cccccc,stroke:#333,color:#000
```

**Heuristic**: If you find yourself writing `if state == X { panic!("Invalid state"); }` more than twice, typestate pattern will eliminate those runtime checks at compile time.

---

### 9.2 Common Pitfalls

```mermaid
flowchart TD
    subgraph GOTCHAS["⚠️ COMMON TYPESTATE GOTCHAS"]
        direction TB
        
        PITFALL1["🚨 PITFALL 1: Forgetting PhantomData
        ════════════════════════════════════════════
        struct Ticket&lt;State&gt; {
        id: TicketId,
        // MISSING: _state: PhantomData&lt;State&gt;
        }
        
        Problem: Compiler error - State unused
        Fix: Add _state: PhantomData&lt;State&gt; field"]
        
        PITFALL2["🚨 PITFALL 2: Shared Mutable References
        ════════════════════════════════════════════
        fn process(ticket: &mut Ticket&lt;Draft&gt;) {
        // Can't transition! We only have &mut
        }
        
        Problem: Can't move out of &mut
        Fix: Use self (take ownership) for transitions"]
        
        PITFALL3["🚨 PITFALL 3: Over-Engineering
        ════════════════════════════════════════════
        20+ state types for simple flag
        
        Problem: Compile time explodes
        Fix: Use runtime enum for dynamic states"]
        
        PITFALL4["🚨 PITFALL 4: Trait Object Incompatibility
        ════════════════════════════════════════════
        let boxed: Box&lt;dyn Ticket&lt;?&gt;&gt; = ...
        
        Problem: Can't make trait object from generic
        Fix: Use enum wrapper or separate traits"]
    end
    
    PITFALL1 --> PITFALL2
    PITFALL2 --> PITFALL3
    PITFALL3 --> PITFALL4
    
    style PITFALL1 fill:#f5f5f5,stroke:#333,color:#000
    style PITFALL2 fill:#e8e8e8,stroke:#333,color:#000
    style PITFALL3 fill:#e0e0e0,stroke:#333,color:#000
    style PITFALL4 fill:#d4d4d4,stroke:#333,color:#000
```

---

### 9.3 Design Checklist

**Before implementing typestate pattern, verify:**

1. **Distinct States**: Can you clearly enumerate all states?
2. **Sequential Transitions**: Are state changes mostly one-directional?
3. **State-Specific Behavior**: Do different states have different valid operations?
4. **Ownership Feasible**: Can transition functions take ownership?
5. **Compilation Cost Acceptable**: Are you willing to pay 2-10% longer compile times?
6. **Not Dynamic**: Are states known at compile time?

**If all YES → Typestate is a great fit.**

---

## Part 10: Advanced Patterns

### 10.1 Combining Typestate with Sealed Traits

```rust
// Prevent external crates from implementing state traits
mod sealed {
    pub trait Sealed {}
}

pub trait State: sealed::Sealed {}

pub struct Draft;
pub struct Active;

impl sealed::Sealed for Draft {}
impl sealed::Sealed for Active {}
impl State for Draft {}
impl State for Active {}

// Now only your crate can define new states
pub struct Ticket<S: State> {
    data: String,
    _state: PhantomData<S>,
}
```

**Purpose**: The sealed trait pattern prevents external crates from adding new states, maintaining your state machine invariants.

---

### 10.2 Const Generics for State Parameters

```rust
// State encoded as const generic
pub struct Ticket<const STATE: u8> {
    id: Option<TicketId>,
    title: String,
}

const DRAFT: u8 = 0;
const ACTIVE: u8 = 1;

impl Ticket<DRAFT> {
    pub fn create(self) -> Ticket<ACTIVE> {
        Ticket {
            id: Some(generate_id()),
            title: self.title,
        }
    }
}
```

**Benefit**: Const generics enable compile-time state tracking without defining separate marker types, though this approach has limited adoption (marker types are more idiomatic).

---

### 10.3 Drop-Based Transition Enforcement

```rust
impl<T> Drop for Transaction<T> {
    fn drop(&mut self) {
        if !self.completed {
            panic!("Transaction dropped without commit or rollback!");
        }
    }
}

impl Transaction<InProgress> {
    pub fn commit(mut self) -> Transaction<Committed> {
        self.completed = true;  // Mark before state change
        // ... actual commit logic
        Transaction {
            completed: true,
            _state: PhantomData,
        }
    }
}
```

**Safety**: Using `Drop` to enforce that certain state transitions must occur (like committing or rolling back a transaction) prevents resource leaks at runtime if the typestate transitions are bypassed.

---

## Part 11: Key Takeaways and Cross-Language Comparison

### 11.1 Core Principles Summary

```mermaid
flowchart TD
    subgraph PRINCIPLES["🎓 TYPESTATE CORE PRINCIPLES"]
        direction TB
        
        P1["1️⃣ STATES ARE TYPES
        ════════════════════════════════
        Each state = separate struct
        Compiler tracks current state
        Invalid states unrepresentable"]
        
        P2["2️⃣ TRANSITIONS CONSUME
        ════════════════════════════════
        Functions take ownership
        Old state becomes unavailable
        One-way enforcement via moves"]
        
        P3["3️⃣ ZERO RUNTIME COST
        ════════════════════════════════
        PhantomData = 0 bytes
        State checks erased by compiler
        Identical assembly to unsafe code"]
        
        P4["4️⃣ COMPILER IS REFEREE
        ════════════════════════════════
        Type errors prevent bugs
        No runtime panics for state errors
        Correctness proven at compile time"]
        
        P1 --> P2
        P2 --> P3
        P3 --> P4
    end
    
    style P1 fill:#f5f5f5,stroke:#333,color:#000
    style P2 fill:#e8e8e8,stroke:#333,color:#000
    style P3 fill:#e0e0e0,stroke:#333,color:#000
    style P4 fill:#d4d4d4,stroke:#333,color:#000
```

---

### 11.2 Cross-Language Comparison

| Language | Equivalent Pattern | Implementation | Limitations |
|----------|-------------------|----------------|-------------|
| **Rust** | Typestate Pattern | Separate types + ownership | ✅ Zero-cost, compile-time enforced |
| **TypeScript** | Discriminated Unions + Type Guards | `type Ticket = Draft \| Active`; `if (ticket.state === 'draft')` | ⚠️ Runtime checks, no ownership |
| **C++** | Template Metaprogramming | `template<State S> class Ticket` | ⚠️ Complex syntax, no move semantics like Rust |
| **Java** | Sealed Classes (Java 17+) | `sealed interface State permits Draft, Active` | ⚠️ Runtime polymorphism overhead |
| **Go** | Interface + Type Assertions | `switch t := ticket.(type)` | ❌ Runtime checks only, no compile-time safety |
| **Haskell** | GADTs (Generalized ADTs) | `data Ticket (s :: State) where ...` | ✅ Similar to Rust, but different ownership model |

**Rust's advantage**: The combination of zero-cost generics, ownership-based consumption, and trait system makes Rust's typestate pattern uniquely powerful—compile-time safety without runtime cost.

---

### 11.3 When NOT to Use Typestate

**Anti-patterns where typestate creates more problems than it solves:**

1. **Dynamic State Machines**: If states are loaded from config files or databases at runtime, use runtime enums instead.
2. **Serialization Boundaries**: Typestate types with `PhantomData` don't serialize cleanly—wrap in a runtime enum for JSON/DB storage.
3. **FFI (Foreign Function Interface)**: C APIs can't understand Rust's type-level states—use runtime state fields at FFI boundaries.
4. **Heterogeneous Collections**: Can't store `Vec<Ticket<??>>` with mixed states—use `enum TicketState { Draft(TicketDraft), Active(Ticket) }` instead.
5. **Prototyping**: The upfront design cost (identifying all states, defining transitions) slows down rapid iteration—add typestate after the design stabilizes.

---

## Part 12: Summary - Compile-Time State Machine Magic

**The typestate pattern transforms state machines from runtime validation nightmares into compile-time correctness guarantees by encoding states as types.**

**Three key mechanisms:**
1. **Separate types per state** → Invalid states physically unrepresentable
2. **Ownership-consuming transitions** → Can't reuse old states after transitions
3. **Zero-cost abstraction** → All safety checks erased by compiler

**MCU metaphor recap**: Vision's creation—incomplete cradle body (Draft), Mind Stone insertion (transition), activated consciousness (Active)—mirrors typestate's irreversible, type-tracked state progression. Just as you can't ask Vision's thoughts before the Mind Stone exists, Rust won't compile `draft.id` because the field literally doesn't exist on that type.

**When to use**: Builder APIs, protocol implementations, resource lifecycle management, any sequential state machine where invalid state access is a critical bug.

**When to avoid**: Dynamic states, serialization boundaries, FFI, heterogeneous collections, rapid prototyping.

**The promise**: Write your state machine once with typestate, and the compiler will forever prevent state-related bugs—no runtime checks, no performance cost, just compile-time proof of correctness.

---

## References

**Primary source**: Mainmatter's "100 Exercises To Learn Rust" - Section 6 (Ticket Management), Chapter 12 (Two States)

**Key concepts covered**:
- Problem: `Option<TicketId>` forces redundant runtime checks
- Solution: Separate `TicketDraft` and `Ticket` types with distinct fields
- Transitions: Functions consume old state via ownership
- Validation reuse: Shared validated types (`TicketTitle`, `TicketDescription`) across state types

**Real-world implementations**:
- `diesel` ORM: Transaction types
- `tokio_postgres`: Connection vs Transaction
- `hyper`: Request body state tracking
- `aws-sdk-rust`: Authenticated vs unauthenticated clients

**Academic background**: Typestate pattern originated in Robert Strom and Shimon Yemini's 1986 paper "Typestate: A Programming Language Concept for Enhancing Software Reliability" (CMU technical report). Rust's ownership system makes the pattern practical at zero runtime cost.
