# Ruby to Rust Transpilation Hypothesis

## Date: 2026-02-04

## The Constraint

```
INPUT:  Working Ruby code (.rb files)
OUTPUT: Pure Rust binary (no Ruby runtime, no FFI, no interpreter)
RULE:   One step. Complete. No partial solutions.
```

## What Dies Immediately

| Eliminated | Why |
|------------|-----|
| FFI Hybrid | Still needs Ruby installed |
| Embedded mruby | That's a runtime dependency |
| Bytecode translation | Multi-step, needs YARV |
| Service extraction | Partial, not complete |
| DSL transforms | Partial, not complete |
| WASM intermediate | Multi-step roundabout |
| Gradual migration | Not "one step" |
| Runtime library calling Ruby | Not "pure" |

## What Survives: 4 Architectures

```
┌─────────────────────────────────────────────────────────────┐
│  ALL ROADS LEAD TO: rustc → Pure Binary                    │
│                                                             │
│  The only question is HOW you get to Rust source           │
└─────────────────────────────────────────────────────────────┘

OPTION 1: Direct Emit (Simplest)
────────────────────────────────
Ruby Source → Ruby AST → Walk & Emit Rust Strings → rustc → Binary

OPTION 2: Structured AST (Safer)
────────────────────────────────
Ruby Source → Ruby AST → Rust AST (syn) → Pretty Print → rustc → Binary

OPTION 3: Custom IR (Optimizable)
────────────────────────────────
Ruby Source → Ruby AST → RubyIR → Optimize → Rust Source → rustc → Binary

OPTION 4: LLVM Direct (Maximum Perf, Skip Rust)
────────────────────────────────
Ruby Source → Ruby AST → LLVM IR → LLVM → Binary
(This is Crystal's approach - you don't even see Rust)
```

## Type Strategy: Only 1 Makes Sense for "Simple"

If we want ONE STEP with NO annotations required from the user:

**Everything becomes `enum RubyValue`**

```rust
// This is the ONLY type strategy that requires ZERO user input
enum RubyValue {
    Nil,
    Bool(bool),
    Int(i64),
    Float(f64),
    String(Rc<RefCell<String>>),
    Array(Rc<RefCell<Vec<RubyValue>>>),
    Hash(Rc<RefCell<HashMap<RubyValue, RubyValue>>>),
    Object(Rc<RefCell<RubyObject>>),
}
```

Type inference = complexity. Annotations = user burden. Skip both.

## Final Answer: 4 Options (or really, 2 practical ones)

| # | Architecture | Complexity | Output Quality | Recommendation |
|---|--------------|------------|----------------|----------------|
| **1** | AST → Rust Strings | Low | Medium | **Start here (v0.1)** |
| **2** | AST → Rust AST → Strings | Medium | High | **Graduate to this (v0.5)** |
| **3** | AST → Custom IR → Rust | High | Very High | Only if v0.5 needs optimization |
| **4** | AST → LLVM IR | Very High | Maximum | Overkill; you're building Crystal |

## The Brutal Simplification

If you want **ONE** answer:

```
┌────────────────────────────────────────────────────────────┐
│                                                            │
│   Ruby Source                                              │
│        ↓                                                   │
│   Prism Parser (ruby-prism crate)                          │
│        ↓                                                   │
│   Ruby AST                                                 │
│        ↓                                                   │
│   Walk AST → Emit Rust strings                             │
│   (every value is RubyValue enum)                          │
│   (every method call is runtime dispatch)                  │
│        ↓                                                   │
│   Rust Source (.rs file)                                   │
│        ↓                                                   │
│   rustc                                                    │
│        ↓                                                   │
│   Pure Binary                                              │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

**That's it. One architecture. One type strategy. One output.**

From 3,125 theoretical combinations → **1 practical choice** for "simple, complete, one-step."
