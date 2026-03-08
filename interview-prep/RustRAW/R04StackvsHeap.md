# 📦 Stack vs Heap in Rust: The Design Philosophy

> **Why does Rust make you think about memory location? And why is `Box` explicit?**

---

## 🧠 Part 1: The Fundamental Problem

### 1.1 What Are Stack and Heap?

``` mermaid
%%{init: {'theme': 'dark'}}%%

flowchart TB
    subgraph STACK["📚 THE STACK"]
        S1["Fast allocation
        ══════════════════
        Just move a pointer
        O(1) - instant"]
        
        S2["Fixed size required
        ══════════════════
        Compiler must know
        exact size at compile"]
        
        S3["Automatic cleanup
        ══════════════════
        Pop when function
        returns - free!"]
        
        S4["Limited space
        ══════════════════
        Usually 1-8 MB
        Stack overflow risk"]
        
        S1 --> S2 --> S3 --> S4
    end
```

``` mermaid
%%{init: {'theme': 'dark'}}%%

flowchart TB
    subgraph HEAP["🗄️ THE HEAP"]
        H1["Slower allocation
        ══════════════════
        Ask OS for memory
        Search for free space"]
        
        H2["Dynamic size OK
        ══════════════════
        Can grow/shrink
        Size unknown at compile"]
        
        H3["Manual cleanup
        ══════════════════
        Must free explicitly
        (Rust: Drop trait)"]
        
        H4["Large space
        ══════════════════
        Limited by RAM
        Gigabytes available"]
        
        H1 --> H2 --> H3 --> H4
    end
```

### 1.2 The Core Trade-off

``` mermaid
%%{init: {'theme': 'dark'}}%%

flowchart TB
    subgraph TRADEOFF["⚖️ THE TRADE-OFF"]
        FAST["🚀 STACK
        ══════════════
        + Blazing fast
        + Auto cleanup
        − Fixed size only
        − Limited space"]
        
        FLEX["🎯 HEAP
        ══════════════
        + Any size
        + Huge capacity
        − Slower alloc
        − Must manage"]
        
        CHOICE["Rust's Goal:
        Stack when possible
        Heap when necessary
        YOU decide consciously"]
        
        FAST --> CHOICE
        FLEX --> CHOICE
    end
```

---

## 🔍 Part 2: When Does Rust Use Stack?

### 2.1 Rule: Known Size at Compile Time → Stack

``` mermaid
%%{init: {'theme': 'dark'}}%%

flowchart TB
    subgraph STACK_RULE["📚 STACK ELIGIBILITY"]
        Q1{"Size known at
        compile time?"}
        
        Q2{"Size fixed
        forever?"}
        
        STACK["✅ Goes on STACK"]
        HEAP["❌ Needs HEAP"]
        
        Q1 -->|"Yes"| Q2
        Q1 -->|"No"| HEAP
        Q2 -->|"Yes"| STACK
        Q2 -->|"No"| HEAP
    end
```

### 2.2 Stack Examples

```rust
// ═══════════════════════════════════════════════════════════
// ALL OF THESE GO ON THE STACK
// ═══════════════════════════════════════════════════════════

// 1. Primitives - size always known
let x: i32 = 42;           // 4 bytes, always
let y: f64 = 3.14;         // 8 bytes, always
let z: bool = true;        // 1 byte, always
let c: char = 'A';         // 4 bytes, always

// 2. Tuples - sum of component sizes
let point: (i32, i32) = (10, 20);      // 8 bytes (4+4)
let mixed: (bool, i64, char) = (true, 100, 'X');  // 13 bytes

// 3. Fixed-size arrays - element_size × length
let nums: [i32; 5] = [1, 2, 3, 4, 5];  // 20 bytes (4×5)
let grid: [[u8; 3]; 3] = [[0; 3]; 3];  // 9 bytes

// 4. Structs with all stack fields
struct Point {
    x: i32,  // 4 bytes
    y: i32,  // 4 bytes
}            // Total: 8 bytes - STACK!

let p = Point { x: 10, y: 20 };

// 5. Enums - size of largest variant + tag
enum Direction {
    Up,      // 0 bytes payload
    Down,    // 0 bytes payload  
    Left,    // 0 bytes payload
    Right,   // 0 bytes payload
}            // Total: 1 byte tag - STACK!

enum Value {
    Int(i64),      // 8 bytes payload
    Float(f64),    // 8 bytes payload
    Pair(i32, i32) // 8 bytes payload
}                  // Total: 8 + tag = 9-16 bytes - STACK!
```

### 2.3 Why Stack is Preferred

``` mermaid
%%{init: {'theme': 'dark'}}%%

flowchart TB
    subgraph WHY_STACK["🚀 WHY PREFER STACK"]
        SPEED["⚡ SPEED
        ══════════════════
        Stack allocation:
        sub rsp, 8  // one instruction!
        
        Heap allocation:
        Call malloc()
        Search free list
        Update bookkeeping
        Maybe ask OS..."]
        
        CACHE["🧠 CPU CACHE
        ══════════════════
        Stack is contiguous
        CPU prefetches it
        Cache hits = FAST
        
        Heap is fragmented
        Pointer chasing
        Cache misses = SLOW"]
        
        FREE["♻️ FREE CLEANUP
        ══════════════════
        Function returns?
        Stack pointer moves
        All locals 'freed'
        
        No destructor calls
        No bookkeeping
        Just gone!"]
        
        SPEED --> CACHE --> FREE
    end
```

---

## 🗄️ Part 3: When Does Rust Need Heap?

### 3.1 The Three Reasons for Heap

``` mermaid
%%{init: {'theme': 'dark'}}%%

flowchart TB
    subgraph HEAP_REASONS["🗄️ WHY HEAP IS NEEDED"]
        R1["📏 UNKNOWN SIZE
        ══════════════════
        User input length?
        File contents?
        Network data?
        
        Can't know at compile!"]
        
        R2["📈 DYNAMIC SIZE
        ══════════════════
        Collection grows?
        String appended?
        Buffer resized?
        
        Stack can't grow!"]
        
        R3["🔄 OUTLIVE SCOPE
        ══════════════════
        Return from function?
        Share between threads?
        Store in long-lived struct?
        
        Stack dies at }!"]
    end
```

### 3.2 Heap Examples

```rust
// ═══════════════════════════════════════════════════════════
// THESE NEED THE HEAP
// ═══════════════════════════════════════════════════════════

// ─────────────────────────────────────────────────────────
// Reason 1: SIZE UNKNOWN AT COMPILE TIME
// ─────────────────────────────────────────────────────────

// String from user input - how long? Nobody knows!
let mut input = String::new();
std::io::stdin().read_line(&mut input)?;

// File contents - could be 1 byte or 1 gigabyte
let contents = std::fs::read_to_string("file.txt")?;

// Network response - completely dynamic
let response = client.get("https://api.com").send()?;

// ─────────────────────────────────────────────────────────
// Reason 2: SIZE CHANGES AT RUNTIME
// ─────────────────────────────────────────────────────────

// Vec grows as you push - can't predict final size
let mut numbers = Vec::new();  // starts empty
numbers.push(1);               // now 1 element
numbers.push(2);               // now 2 elements
// ... could grow to millions!

// String grows as you append
let mut name = String::from("Hello");
name.push_str(", World!");  // grew!
name.push_str(" How are you?");  // grew again!

// ─────────────────────────────────────────────────────────
// Reason 3: DATA MUST OUTLIVE CURRENT SCOPE
// ─────────────────────────────────────────────────────────

fn create_data() -> Vec<i32> {
    let data = vec![1, 2, 3];  // created here
    data  // returned! Must outlive this function
}
// If data was on stack, it would be destroyed at }
// But Vec's heap data survives, ownership transfers

// Sharing between threads
let shared = Arc::new(Mutex::new(vec![1, 2, 3]));
// Must live as long as any thread needs it
```

---

## 📦 Part 4: What is `Box<T>` and Why Explicit?

### 4.1 What Box Does

``` mermaid
%%{init: {'theme': 'dark'}}%%

flowchart TB
    subgraph BOX_WHAT["📦 WHAT BOX DOES"]
        BEFORE["WITHOUT BOX
        ══════════════════
        let x: i32 = 42;
        
        Stack: [42]
        Size: 4 bytes on stack"]
        
        AFTER["WITH BOX
        ══════════════════
        let x: Box<i32> = Box::new(42);
        
        Stack: [pointer] → Heap: [42]
        Size: 8 bytes ptr on stack
              4 bytes data on heap"]
        
        BEFORE --> AFTER
    end
```

### 4.2 Memory Layout Visualization

```
┌─────────────────────────────────────────────────────────────┐
│                         STACK                                │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  let a: i32 = 42;                                           │
│  ┌─────────┐                                                 │
│  │   42    │  ← 4 bytes, value right here                   │
│  └─────────┘                                                 │
│                                                              │
│  let b: Box<i32> = Box::new(42);                            │
│  ┌─────────────┐                                             │
│  │  0x7f3a... ─┼────────────────────┐                       │
│  └─────────────┘                     │                       │
│       ↑                              │                       │
│   8 bytes pointer                    │                       │
│                                      ▼                       │
├──────────────────────────────────────┼──────────────────────┤
│                         HEAP          │                      │
├──────────────────────────────────────┼──────────────────────┤
│                                      │                       │
│                               ┌──────┴────┐                  │
│                               │    42     │ ← 4 bytes        │
│                               └───────────┘                  │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### 4.3 When You NEED Box

``` mermaid
%%{init: {'theme': 'dark'}}%%

flowchart TB
    subgraph BOX_WHEN["📦 WHEN BOX IS REQUIRED"]
        R1["🔄 RECURSIVE TYPES
        ══════════════════
        struct Node {
          value: i32,
          next: Node  // ❌ infinite size!
        }
        
        struct Node {
          value: i32,
          next: Box<Node>  // ✅ pointer = 8 bytes
        }"]
        
        R2["🎭 TRAIT OBJECTS
        ══════════════════
        // Size unknown - could be any impl!
        fn process(x: dyn Animal) // ❌ 
        
        fn process(x: Box<dyn Animal>) // ✅
        // Pointer to heap, size known"]
        
        R3["📦 FORCE HEAP ALLOC
        ══════════════════
        // Large data, don't want on stack
        let huge: Box<[u8; 1_000_000]> = 
            Box::new([0; 1_000_000]);
        
        // 1MB on heap, not stack!"]
    end
```

### 4.4 Recursive Type Example

```rust
// ═══════════════════════════════════════════════════════════
// THE RECURSIVE TYPE PROBLEM
// ═══════════════════════════════════════════════════════════

// ❌ THIS WON'T COMPILE - Infinite size!
// struct List {
//     value: i32,
//     next: List,  // Error: recursive type has infinite size
// }
// 
// Why? Compiler tries to calculate size:
// size(List) = size(i32) + size(List)
//            = 4 + size(List)
//            = 4 + 4 + size(List)
//            = 4 + 4 + 4 + size(List)
//            = ... infinite!

// ✅ THIS WORKS - Box has known size (pointer = 8 bytes)
struct List {
    value: i32,
    next: Option<Box<List>>,  // 8 bytes pointer (or None)
}

// Size calculation:
// size(List) = size(i32) + size(Option<Box<List>>)
//            = 4 + 8
//            = 12 bytes  ✓ Known at compile time!

// Usage:
let list = List {
    value: 1,
    next: Some(Box::new(List {
        value: 2,
        next: Some(Box::new(List {
            value: 3,
            next: None,
        })),
    })),
};
```

### 4.5 Trait Object Example

```rust
// ═══════════════════════════════════════════════════════════
// THE TRAIT OBJECT PROBLEM
// ═══════════════════════════════════════════════════════════

trait Animal {
    fn speak(&self);
}

struct Dog { name: String }           // Size: 24 bytes
struct Cat { name: String, age: u8 }  // Size: 25 bytes
struct Elephant { weight: u64 }       // Size: 8 bytes

impl Animal for Dog { fn speak(&self) { println!("Woof!"); } }
impl Animal for Cat { fn speak(&self) { println!("Meow!"); } }
impl Animal for Elephant { fn speak(&self) { println!("Trumpet!"); } }

// ❌ THIS WON'T COMPILE
// fn pet(animal: dyn Animal) { ... }
// Error: the size of `dyn Animal` cannot be statically determined
//
// Why? Could be Dog (24 bytes), Cat (25 bytes), or Elephant (8 bytes)!
// Compiler doesn't know how much stack space to reserve.

// ✅ SOLUTION 1: Box (owned, heap-allocated)
fn adopt(animal: Box<dyn Animal>) {
    animal.speak();
}
// Box<dyn Animal> is always 16 bytes: 8-byte data ptr + 8-byte vtable ptr

// ✅ SOLUTION 2: Reference (borrowed)
fn pet(animal: &dyn Animal) {
    animal.speak();
}
// &dyn Animal is always 16 bytes: 8-byte ptr + 8-byte vtable ptr

// Usage:
let dog = Dog { name: String::from("Buddy") };
let cat = Cat { name: String::from("Whiskers"), age: 3 };

pet(&dog);  // Works!
pet(&cat);  // Works!

adopt(Box::new(dog));  // Transfers ownership to heap
adopt(Box::new(cat));
```

---

## 🎯 Part 5: The Design Philosophy

### 5.1 Why Make Heap Explicit?

``` mermaid
%%{init: {'theme': 'dark'}}%%

flowchart TB
    subgraph WHY_EXPLICIT["🎯 WHY EXPLICIT HEAP?"]
        P1["👀 VISIBILITY
        ══════════════════
        You SEE the cost
        
        Box::new() = heap alloc
        vec![] = heap alloc
        String::from() = heap
        
        No hidden allocations!"]
        
        P2["🎮 CONTROL
        ══════════════════
        YOU choose where
        
        Need stack? Use value
        Need heap? Use Box/Vec
        
        Not compiler's guess"]
        
        P3["⚡ PERFORMANCE
        ══════════════════
        Predictable speed
        
        See Box? Expect alloc
        No Box? It's fast
        
        Optimize consciously"]
        
        P1 --> P2 --> P3
    end
```

### 5.2 Contrast with Other Languages

``` mermaid
%%{init: {'theme': 'dark'}}%%

flowchart TB
    subgraph JAVA_WAY["☕ JAVA'S APPROACH"]
        J1["new Object()
        ══════════════════
        ALWAYS heap
        You have no choice
        Even Integer = heap"]
        
        J2["Hidden allocation
        ══════════════════
        String concat? Heap
        Autoboxing? Heap
        Lambda? Heap
        You don't see it"]
        
        J3["GC cleans up
        ══════════════════
        Eventually...
        When it wants...
        Might pause you..."]
    end
```

``` mermaid
%%{init: {'theme': 'dark'}}%%

flowchart TB
    subgraph RUST_WAY["🦀 RUST'S APPROACH"]
        R1["Box::new(value)
        ══════════════════
        EXPLICIT heap
        You chose this
        You see the cost"]
        
        R2["Visible allocation
        ══════════════════
        See Box/Vec/String?
        That's heap alloc
        No surprises"]
        
        R3["Deterministic drop
        ══════════════════
        Scope ends = freed
        Exactly when
        No GC pauses"]
    end
```

### 5.3 The Philosophy in One Diagram

``` mermaid
%%{init: {'theme': 'dark'}}%%

flowchart TB
    subgraph PHILOSOPHY["🧠 RUST'S MEMORY PHILOSOPHY"]
        PRINCIPLE["CORE PRINCIPLE
        ══════════════════════════════
        Make costs VISIBLE
        Make choices EXPLICIT
        Give programmer CONTROL"]
        
        STACK_RULE["📚 STACK BY DEFAULT
        ══════════════════════════════
        If size is known → stack
        Fast, automatic, free
        Zero overhead"]
        
        HEAP_RULE["🗄️ HEAP WHEN ASKED
        ══════════════════════════════
        Box/Vec/String = explicit
        You see allocation
        You control lifetime"]
        
        RESULT["🎯 RESULT
        ══════════════════════════════
        No hidden costs
        Predictable performance
        Optimizable code"]
        
        PRINCIPLE --> STACK_RULE
        PRINCIPLE --> HEAP_RULE
        STACK_RULE --> RESULT
        HEAP_RULE --> RESULT
    end
```

---

## 📊 Part 6: Complete Decision Flowchart

### 6.1 Does My Type Need Heap?

``` mermaid
%%{init: {'theme': 'dark'}}%%

flowchart TB
    START["I have a type T"]
    
    Q1{"Is size known
    at compile time?"}
    
    Q2{"Will size
    change at runtime?"}
    
    Q3{"Need to outlive
    current scope?"}
    
    Q4{"Is it recursive?"}
    
    Q5{"Is it a trait object
    (dyn Trait)?"}
    
    STACK["📚 STACK
    Just use T directly"]
    
    VEC["🗄️ Use Vec&lt;T&gt;
    or String"]
    
    BOX["📦 Use Box&lt;T&gt;"]
    
    RETURN["Return T or
    wrap in heap type"]
    
    START --> Q1
    Q1 -->|"No"| VEC
    Q1 -->|"Yes"| Q2
    Q2 -->|"Yes"| VEC
    Q2 -->|"No"| Q3
    Q3 -->|"Yes"| RETURN
    Q3 -->|"No"| Q4
    Q4 -->|"Yes"| BOX
    Q4 -->|"No"| Q5
    Q5 -->|"Yes"| BOX
    Q5 -->|"No"| STACK

    classDef stackStyle fill:#2d5a27,stroke:#4ade80,stroke-width:3px,color:#fff
    classDef heapStyle fill:#5c1f1f,stroke:#f87171,stroke-width:3px,color:#fff
    classDef boxStyle fill:#1e3a5f,stroke:#60a5fa,stroke-width:3px,color:#fff
    
    class STACK stackStyle
    class VEC heapStyle
    class BOX,RETURN boxStyle
```

### 6.2 Which Heap Type Should I Use?

``` mermaid
%%{init: {'theme': 'dark'}}%%

flowchart TB
    START["Need heap storage"]
    
    Q1{"Collection of items?"}
    Q2{"Text data?"}
    Q3{"Single value?"}
    Q4{"Shared ownership?"}
    Q5{"Thread-safe sharing?"}
    
    VEC["Vec&lt;T&gt;
    Growable array"]
    
    STRING["String
    Growable UTF-8"]
    
    BOX["Box&lt;T&gt;
    Single heap value"]
    
    RC["Rc&lt;T&gt;
    Reference counted"]
    
    ARC["Arc&lt;T&gt;
    Atomic ref count"]
    
    START --> Q1
    Q1 -->|"Yes"| VEC
    Q1 -->|"No"| Q2
    Q2 -->|"Yes"| STRING
    Q2 -->|"No"| Q3
    Q3 -->|"Yes"| Q4
    Q4 -->|"Yes"| Q5
    Q4 -->|"No"| BOX
    Q5 -->|"Yes"| ARC
    Q5 -->|"No"| RC
```

---

## 🔬 Part 7: Real-World Examples

### 7.1 Building a Tree Structure

```rust
// ═══════════════════════════════════════════════════════════
// EXAMPLE: Binary Search Tree
// ═══════════════════════════════════════════════════════════

// ❌ Without Box - IMPOSSIBLE (infinite size)
// struct BSTNode {
//     value: i32,
//     left: BSTNode,   // infinite!
//     right: BSTNode,  // infinite!
// }

// ✅ With Box - Works perfectly
struct BSTNode {
    value: i32,
    left: Option<Box<BSTNode>>,   // 8 bytes (pointer or null)
    right: Option<Box<BSTNode>>,  // 8 bytes (pointer or null)
}
// Total size: 4 + 8 + 8 = 20 bytes (fixed!)

impl BSTNode {
    fn new(value: i32) -> Self {
        BSTNode { value, left: None, right: None }
    }
    
    fn insert(&mut self, value: i32) {
        if value < self.value {
            match &mut self.left {
                None => self.left = Some(Box::new(BSTNode::new(value))),
                Some(node) => node.insert(value),
            }
        } else {
            match &mut self.right {
                None => self.right = Some(Box::new(BSTNode::new(value))),
                Some(node) => node.insert(value),
            }
        }
    }
}

// Memory layout:
// 
// Stack: [BSTNode root]
//            │
//            ▼
// Heap:  ┌─────────────────┐
//        │ value: 50       │
//        │ left: ──────────┼──► [value: 25, left: ─►..., right: ─►...]
//        │ right: ─────────┼──► [value: 75, left: None, right: None]
//        └─────────────────┘
```

### 7.2 Polymorphic Collection

```rust
// ═══════════════════════════════════════════════════════════
// EXAMPLE: Heterogeneous Collection of Shapes
// ═══════════════════════════════════════════════════════════

trait Shape {
    fn area(&self) -> f64;
    fn name(&self) -> &str;
}

struct Circle { radius: f64 }
struct Rectangle { width: f64, height: f64 }
struct Triangle { base: f64, height: f64 }

impl Shape for Circle {
    fn area(&self) -> f64 { std::f64::consts::PI * self.radius * self.radius }
    fn name(&self) -> &str { "Circle" }
}

impl Shape for Rectangle {
    fn area(&self) -> f64 { self.width * self.height }
    fn name(&self) -> &str { "Rectangle" }
}

impl Shape for Triangle {
    fn area(&self) -> f64 { 0.5 * self.base * self.height }
    fn name(&self) -> &str { "Triangle" }
}

// ❌ This won't work - different sizes!
// let shapes: Vec<dyn Shape> = vec![...];

// ✅ Box makes them all the same size (pointer)
let shapes: Vec<Box<dyn Shape>> = vec![
    Box::new(Circle { radius: 5.0 }),
    Box::new(Rectangle { width: 4.0, height: 6.0 }),
    Box::new(Triangle { base: 3.0, height: 4.0 }),
];

// All elements are 16 bytes (8-byte ptr + 8-byte vtable)
for shape in &shapes {
    println!("{}: area = {:.2}", shape.name(), shape.area());
}
```

### 7.3 Avoiding Stack Overflow

```rust
// ═══════════════════════════════════════════════════════════
// EXAMPLE: Large Data That Would Overflow Stack
// ═══════════════════════════════════════════════════════════

// ❌ This might cause stack overflow!
// fn dangerous() {
//     let huge_array: [u8; 10_000_000] = [0; 10_000_000];  // 10 MB on stack!
//     // Stack is typically only 1-8 MB...
// }

// ✅ Use Box to put large data on heap
fn safe() {
    // Only 8 bytes on stack (the pointer)
    // 10 MB safely on heap
    let huge_array: Box<[u8; 10_000_000]> = Box::new([0; 10_000_000]);
    
    println!("Array length: {}", huge_array.len());
}

// ✅ Even better: use Vec for dynamic sizing
fn flexible() {
    let huge_vec: Vec<u8> = vec![0; 10_000_000];
    // Can grow or shrink!
}
```

---

## 📚 Part 8: Summary

### 8.1 The Mental Model

``` mermaid
%%{init: {'theme': 'dark'}}%%

flowchart TB
    subgraph MENTAL["🧠 MENTAL MODEL"]
        M1["📚 STACK = Fast & Automatic
        ════════════════════════════
        • Size known at compile time
        • Allocation is instant
        • Cleanup is free
        • DEFAULT choice"]
        
        M2["🗄️ HEAP = Flexible & Controlled
        ════════════════════════════
        • Size can be dynamic
        • Allocation costs time
        • Must manage lifetime
        • EXPLICIT choice"]
        
        M3["📦 BOX = 'Put This On Heap'
        ════════════════════════════
        • Makes heap explicit
        • Solves recursive types
        • Enables trait objects
        • YOU decide"]
    end
```

### 8.2 Quick Reference

| Situation | Solution | Why |
|-----------|----------|-----|
| Fixed-size primitive | `let x: i32` | Known size, stack |
| Unknown-size text | `String` | Grows dynamically |
| Collection of items | `Vec<T>` | Dynamic size |
| Recursive type | `Box<T>` | Breaks infinite size |
| Trait object | `Box<dyn T>` | Known pointer size |
| Large data | `Box<[T; N]>` | Avoid stack overflow |
| Shared ownership | `Rc<T>` / `Arc<T>` | Multiple owners |

### 8.3 The Golden Rule

``` mermaid
%%{init: {'theme': 'dark'}}%%

flowchart TB
    subgraph GOLDEN["🏆 THE GOLDEN RULE"]
        RULE["Stack by default.
        Heap when you need:
        
        • Dynamic size
        • Recursive types
        • Trait objects
        • Large allocations
        • Outliving scope
        
        Make it EXPLICIT.
        See the COST.
        Own the DECISION."]
    end
    
    classDef goldStyle fill:#4a3728,stroke:#fbbf24,stroke-width:3px,color:#fff
    class RULE goldStyle
```

---

> **Remember**: In Rust, you're not just writing code—you're making conscious decisions about where every piece of data lives. This explicitness is a feature, not a burden. It gives you control and makes performance predictable.

---

*🦀 Rust: Where memory decisions are visible, explicit, and yours to make.*
