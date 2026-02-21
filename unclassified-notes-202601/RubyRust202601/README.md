# Ruby-to-Rust Transpilation Research

**Date:** 2026-02-04

## Overview

Research and analysis on the feasibility of transpiling Ruby code to pure Rust binaries, conducted using parseltongue to analyze the Rails framework codebase.

## Files

| File | Description |
|------|-------------|
| `01-Hypothesis-Ruby-to-Rust-Transpilation.md` | The original hypothesis and architecture options |
| `02-Parseltongue-Analysis-Rails-Codebase.md` | Quantitative analysis of Rails using parseltongue |
| `03-Transpilable-Subset-Definition.md` | Definition of "Ruby--" - the transpilable subset |
| `04-Concrete-Transpilation-Example.md` | Working example with Ruby input and Rust output |
| `05-Verdict-and-Recommendations.md` | Final verdict and recommended path forward |
| `06-Thesis-Rails-DSL-Compiler-to-Rust.md` | **KEY THESIS**: Rails DSL Compiler approach - compile Rails DSLs (not Ruby) to Rust |

## Key Findings

- **87.5%** of Rails code entities are theoretically transpilable
- **7.1%** require runtime code generation (impossible to transpile)
- The 7.1% is concentrated in **core framework components** (ActiveRecord, ActiveSupport)
- Rails applications **cannot** be transpiled without a Ruby runtime
- **Ruby--** (Ruby minus metaprogramming) is a viable target for transpilation
- **Critical pivot**: Rails metaprogramming is configuration-driven (schema.rb, routes.rb are static files) - a Rails DSL Compiler can resolve these at compile time

## Tools Used

- **parseltongue v1.4.7** - Code dependency graph generator
- Analyzed **55,603** code entities
- Mapped **158,170** dependency edges

## Conclusion

The hypothesis is **validated for Ruby--** but **not for Rails/idiomatic Ruby**.

A transpiler targeting Ruby-- can produce pure Rust binaries with ~2-5x performance improvement over YARV.
