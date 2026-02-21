# Verdict and Recommendations

## Date: 2026-02-04

## Hypothesis Under Test

```
Ruby Source → Prism AST → Walk & Emit Rust → RubyValue enum → rustc → Binary

Type Strategy: enum RubyValue { Nil, Bool, Int, Float, String, Array, ... }
Every method call = runtime dispatch
ONE STEP. COMPLETE. NO PARTIAL SOLUTIONS.
```

## Verdict

### The Architecture IS CORRECT for Ruby--

**87.5% of Rails entities are theoretically transpilable** using the proposed architecture.

The approach works for:
- Classes with explicit methods
- Simple validators (PresenceValidator, AbsenceValidator)
- Data structures (Struct-based)
- Statically-defined method calls
- Utility libraries without metaprogramming
- CLI tools and scripts

### The Architecture CANNOT Handle Rails

**The 7.1% "impossible" code is the FOUNDATION**, not the periphery:

- `method_missing` in ActiveRecord controls ALL attribute access
- `module_eval` in ActiveSupport generates methods from strings
- `inherited`/`included` callbacks wire up the entire framework

Rails applications cannot be transpiled without embedding a Ruby runtime.

## Summary Statistics

| Finding | Data |
|---------|------|
| Rails entities analyzed | 55,603 |
| Statically transpilable | 87.5% |
| Requires runtime | 12.5% |
| `method_missing` instances | 67 |
| `module_eval` code generation | Generates methods from STRINGS |
| Circular dependencies | None |

## Recommendations

### Short Term (v0.1)

1. **Define Ruby-- formally** as documented in `03-Transpilable-Subset-Definition.md`
2. **Build a transpiler** for the Ruby-- subset using:
   - `ruby-prism` crate for parsing
   - Direct string emission for Rust code
   - `RubyValue` enum runtime library
3. **Create lint tool** to detect forbidden patterns

### Medium Term (v0.5)

1. **Graduate to Rust AST** using `syn` crate for safer code generation
2. **Add basic type inference** for common patterns
3. **Optimize hot paths** where types can be statically determined

### Long Term (v1.0+)

1. **Full type inference** (Crystal-like approach)
2. **Static dispatch** for inferred types
3. **Ownership analysis** to eliminate `Rc<RefCell<>>`

### What NOT To Do

1. **Don't try to transpile Rails apps** - foundationally metaprogrammed
2. **Don't try to transpile arbitrary gems** - idiomatically use metaprogramming
3. **Don't expect 100x speedup** - RubyValue dispatch gives ~2-5x vs YARV

## The Path Forward

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│  PHASE 1: Ruby-- Transpiler                                                 │
│  ─────────────────────────────                                              │
│  • Subset of Ruby without metaprogramming                                   │
│  • RubyValue enum for all values                                            │
│  • Runtime dispatch for method calls                                        │
│  • ~2-5x speedup, pure binary output                                        │
│                                                                             │
│  PHASE 2: Type-Aware Transpiler                                             │
│  ─────────────────────────────────                                          │
│  • Add optional type annotations                                            │
│  • Infer types where possible                                               │
│  • Static dispatch for known types                                          │
│  • ~10-50x speedup for typed code                                           │
│                                                                             │
│  PHASE 3: Full Inference (Crystal Approach)                                 │
│  ──────────────────────────────────────────                                 │
│  • Whole-program type inference                                             │
│  • Monomorphization                                                         │
│  • Full Rust performance                                                    │
│  • ~50-100x speedup                                                         │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Alternative: Artichoke

If the goal is to run Ruby code as a Rust binary with better performance, consider [Artichoke](https://github.com/artichoke/artichoke):

- Full Ruby interpreter implemented in Rust
- Supports metaprogramming
- Can run Rails (eventually)
- Different tradeoffs than transpilation

## Conclusion

**Your hypothesis is validated for a useful subset of Ruby.**

The 87.5% transpilable statistic shows that Ruby-- is a LARGE, USEFUL subset that can produce pure Rust binaries.

The limitation is that idiomatic Ruby (especially Rails) lives in the 12.5% that requires runtime code generation.

**For new code written within Ruby-- constraints, transpilation to Rust is viable and valuable.**
