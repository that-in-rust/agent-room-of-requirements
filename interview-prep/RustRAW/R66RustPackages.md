# R66: Packages, Crates, and Dependencies - Rust's Module System

## Problem: How to Organize Code Across Multiple Files and Libraries

**ANSWER UPFRONT**: A **package** is defined by `Cargo.toml` (manifest) and contains one or more **crates** (compilation units). **Binary crates** (`src/main.rs`) are executables with `main()`. **Library crates** (`src/lib.rs`) provide reusable code. **Dependencies** in `[dependencies]` section pull code from crates.io or local paths.

**What's Wrong**: Can't keep all code in single file. Need to split into modules, reuse code across projects, and leverage community crates. But how to organize, declare, and depend on external code?

**The Solution**: Packages group crates via `Cargo.toml`. Libraries export code, binaries execute it. Dependencies declared in manifest, resolved/downloaded by Cargo. `Cargo.lock` ensures reproducible builds.

**Why It Matters**: Foundation of Rust ecosystem. Enables code reuse, modular design, and leveraging 100K+ crates on crates.io. Understanding packages/crates/dependencies essential for real-world Rust development.

---

## MCU Metaphor: Avengers Initiative Recruitment Protocol

**The Story**: Nick Fury's Avengers Initiative recruits heroes (dependencies) with specific capabilities. Each hero has dossier (Cargo.toml), skills (library), and may lead missions (binary). Initiative coordinates team (package).

**The Mapping**:

| Rust Concept | MCU Equivalent | How It Works |
|--------------|----------------|--------------|
| Package | Avengers Initiative | Coordination project defined by manifest |
| Cargo.toml | S.H.I.E.L.D. Dossier | Manifest listing team members and metadata |
| Library crate | Hero's abilities | Reusable skills others can call upon |
| Binary crate | Mission leader | Executable with `main()` entry point |
| Dependency | Recruited hero | External capability your team relies on |
| crates.io | S.H.I.E.L.D. Database | Registry of available heroes/crates |
| Cargo.lock | Team roster lock | Exact versions preventing surprise changes |
| `src/lib.rs` | Hero training facility | Where library skills are developed |
| `src/main.rs` | Mission briefing room | Where executable missions start |
| Path dependency | Local hero | Teammate from nearby location |
| Version requirement | Power level requirement | "Need hero with at least Level 1 abilities" |
| `[dev-dependencies]` | Training partners | Only needed for practice missions (tests) |

**The Insight**: Just as the Avengers Initiative assembles heroes (dependencies) with specific capabilities (libraries) to execute missions (binaries), coordinated via S.H.I.E.L.D. dossiers (Cargo.toml) and locked rosters (Cargo.lock), Rust packages organize crates and dependencies—enabling modular code reuse across the ecosystem while maintaining reproducible builds through version locking.

---

## Anatomy: Package Structure

### Package = Cargo.toml + Crates

```
my_project/
├── Cargo.toml          # Package manifest (defines package)
├── Cargo.lock          # Dependency lock file (exact versions)
├── src/
│   ├── lib.rs          # Library crate (optional, max 1)
│   ├── main.rs         # Binary crate (optional, can have many)
│   └── bin/            # Additional binaries
│       └── tool.rs
├── tests/              # Integration tests
│   └── integration.rs
├── benches/            # Benchmarks
│   └── bench.rs
└── examples/           # Example programs
    └── demo.rs
```

### Cargo.toml (Manifest)

```toml
[package]
name = "my_project"
version = "0.1.0"
edition = "2021"
authors = ["Your Name <you@example.com>"]

[dependencies]
serde = "1.0"
tokio = { version = "1", features = ["full"] }

[dev-dependencies]
criterion = "0.5"

[[bin]]
name = "my_tool"
path = "src/bin/tool.rs"
```

**Sections**:
- `[package]`: Metadata (name, version, edition)
- `[dependencies]`: Runtime dependencies
- `[dev-dependencies]`: Test/dev-only dependencies
- `[[bin]]`: Explicit binary declarations (optional)

---

## Library Crates vs Binary Crates

### Library Crate (`src/lib.rs`)

```rust
// src/lib.rs - Library crate root

/// A ticket management library
pub struct Ticket {
    pub id: u64,
    pub title: String,
}

pub fn create_ticket(title: String) -> Ticket {
    Ticket { id: 1, title }
}

// Private function (not exported)
fn internal_helper() {
    // ...
}
```

**Characteristics**:
- **Not executable**: Can't run directly
- **Exports code**: Other crates import with `use my_project::Ticket`
- **One per package**: Only one `lib.rs` allowed
- **Public API**: `pub` items are accessible to dependents

### Binary Crate (`src/main.rs`)

```rust
// src/main.rs - Binary crate root

use my_project::Ticket;  // Import from lib crate in same package

fn main() {
    let ticket = my_project::create_ticket("Fix bug".into());
    println!("Created ticket: {}", ticket.title);
}
```

**Characteristics**:
- **Executable**: Runs with `cargo run`
- **Requires `main()`**: Entry point for execution
- **Multiple allowed**: Can have many binaries in `src/bin/`
- **Can use package's library**: Imports own lib crate

### Both in Same Package

```toml
[package]
name = "ticket_system"
version = "0.1.0"
edition = "2021"
```

```
ticket_system/
├── Cargo.toml
└── src/
    ├── lib.rs    # Library: exports Ticket, create_ticket()
    └── main.rs   # Binary: uses library, prints ticket
```

```bash
# Build library
cargo build --lib

# Run binary (uses library)
cargo run

# Other projects can depend on library
# [dependencies]
# ticket_system = "0.1.0"
```

---

## Dependencies: Adding External Crates

### From crates.io (Default)

```toml
[dependencies]
serde = "1.0"              # At least 1.0.0, less than 2.0.0
tokio = "1.35"             # At least 1.35.0, less than 2.0.0
thiserror = "1"            # At least 1.0.0, less than 2.0.0
```

**Semantic versioning**:
- `"1.0"` = `">=1.0.0, <2.0.0"` (caret requirement, default)
- `"1.2.3"` = `">=1.2.3, <2.0.0"` (exact minor/patch)
- `"=1.2.3"` = exactly 1.2.3 (rarely used)

### With Features

```toml
[dependencies]
tokio = { version = "1", features = ["full"] }
serde = { version = "1.0", features = ["derive"] }
reqwest = { version = "0.11", default-features = false, features = ["json"] }
```

**Features**: Optional functionality to reduce compile times.

### Path Dependencies (Local Development)

```toml
[dependencies]
my_library = { path = "../my_library" }
ticket_core = { path = "./ticket_core" }
```

**Use case**: Working on multiple related crates locally.

### Git Dependencies

```toml
[dependencies]
my_crate = { git = "https://github.com/user/repo" }
my_crate = { git = "https://github.com/user/repo", branch = "dev" }
my_crate = { git = "https://github.com/user/repo", tag = "v0.1.0" }
my_crate = { git = "https://github.com/user/repo", rev = "abc123" }
```

**Use case**: Using unreleased versions or forks.

### Dev Dependencies (Test-only)

```toml
[dev-dependencies]
criterion = "0.5"          # Benchmarking
proptest = "1.0"           # Property testing
mockall = "0.12"           # Mocking
```

**Not included in final binary**: Only for `cargo test`, `cargo bench`.

---

## Cargo.lock: Version Locking

### Purpose

```toml
# Cargo.toml declares REQUIREMENTS
[dependencies]
serde = "1.0"  # "At least 1.0.0, less than 2.0.0"
```

```toml
# Cargo.lock records EXACT versions used
[[package]]
name = "serde"
version = "1.0.197"
source = "registry+https://github.com/rust-lang/crates.io-index"
checksum = "..."
```

**Why needed?** Ensures reproducible builds—same code compiles same way everywhere.

### When to Commit

```bash
# Binary/application projects: YES
my-app/
├── Cargo.toml
└── Cargo.lock  # Commit this!

# Library projects: NO (usually)
my-lib/
├── Cargo.toml
└── Cargo.lock  # .gitignore this
```

**Reasoning**:
- **Apps**: Want exact versions for reproducibility
- **Libraries**: Dependents should test with their own version ranges

### Updating Dependencies

```bash
# Update all dependencies (within semver constraints)
cargo update

# Update specific dependency
cargo update -p serde

# Update to latest compatible version
cargo update serde
```

---

## Real-World Package Examples

### Example 1: Library + Binary

```toml
# Cargo.toml
[package]
name = "json_parser"
version = "0.1.0"
edition = "2021"

[dependencies]
serde = { version = "1.0", features = ["derive"] }
serde_json = "1.0"
```

```
json_parser/
├── Cargo.toml
├── src/
│   ├── lib.rs          # Library: parse_json()
│   └── main.rs         # Binary: CLI tool using library
└── examples/
    └── simple.rs       # Example usage
```

```rust
// src/lib.rs
use serde::{Deserialize, Serialize};

#[derive(Serialize, Deserialize)]
pub struct Config {
    pub name: String,
    pub port: u16,
}

pub fn parse_json(input: &str) -> Result<Config, serde_json::Error> {
    serde_json::from_str(input)
}
```

```rust
// src/main.rs
use json_parser::parse_json;

fn main() {
    let json = r#"{"name": "server", "port": 8080}"#;
    match parse_json(json) {
        Ok(config) => println!("Parsed: {} on port {}", config.name, config.port),
        Err(e) => eprintln!("Error: {}", e),
    }
}
```

### Example 2: Multiple Binaries

```toml
[package]
name = "devtools"
version = "0.1.0"

[[bin]]
name = "formatter"
path = "src/bin/formatter.rs"

[[bin]]
name = "linter"
path = "src/bin/linter.rs"
```

```
devtools/
├── Cargo.toml
└── src/
    ├── lib.rs                # Shared library code
    └── bin/
        ├── formatter.rs      # cargo run --bin formatter
        └── linter.rs         # cargo run --bin linter
```

### Example 3: Workspace (Multiple Packages)

```toml
# Workspace root Cargo.toml
[workspace]
members = ["core", "cli", "web"]
resolver = "2"
```

```
project/
├── Cargo.toml          # Workspace root
├── core/
│   ├── Cargo.toml      # Library package
│   └── src/lib.rs
├── cli/
│   ├── Cargo.toml      # Binary package
│   └── src/main.rs
└── web/
    ├── Cargo.toml      # Binary package
    └── src/main.rs
```

**Benefits**: Shared `Cargo.lock`, unified `target/` directory, cross-package dependencies.

---

## Common Patterns

### Pattern 1: Internal Library + Binary

```rust
// src/lib.rs - Public library
pub mod parser {
    pub fn parse(input: &str) -> Vec<String> {
        input.split_whitespace().map(|s| s.to_string()).collect()
    }
}

pub mod formatter {
    pub fn format(tokens: &[String]) -> String {
        tokens.join(" | ")
    }
}

// src/main.rs - Binary using library
use my_crate::{parser, formatter};

fn main() {
    let input = "hello world rust";
    let tokens = parser::parse(input);
    let output = formatter::format(&tokens);
    println!("{}", output);
}
```

**Benefit**: Binary can test library functionality, library can be used by others.

### Pattern 2: Optional Features

```toml
[features]
default = ["std"]
std = []
async = ["tokio"]
serde = ["dep:serde"]

[dependencies]
tokio = { version = "1", optional = true }
serde = { version = "1", optional = true }
```

```rust
// src/lib.rs
#[cfg(feature = "serde")]
use serde::{Serialize, Deserialize};

#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub struct Data {
    pub value: i32,
}
```

**Use case**: Library supports multiple backends, avoid bloat.

### Pattern 3: Integration Tests

```
my_crate/
├── src/
│   └── lib.rs
└── tests/
    ├── integration.rs
    └── helpers/
        └── mod.rs
```

```rust
// tests/integration.rs - Uses library as external crate
use my_crate::create_ticket;

#[test]
fn test_ticket_creation() {
    let ticket = create_ticket("Test".into());
    assert_eq!(ticket.title, "Test");
}
```

**Tests in `tests/` compile as separate crates** (integration tests).

---

## Cargo Commands Reference

```bash
# Create new binary project
cargo new my_app

# Create new library project
cargo new --lib my_lib

# Build project
cargo build              # Debug build
cargo build --release    # Optimized build

# Run binary
cargo run                # Run default binary
cargo run --bin tool     # Run specific binary

# Run tests
cargo test               # All tests
cargo test test_name     # Specific test

# Check without building
cargo check              # Fast syntax check

# Update dependencies
cargo update             # Update Cargo.lock

# Add dependency (cargo-edit)
cargo add serde          # Add to [dependencies]
cargo add --dev criterion # Add to [dev-dependencies]

# Remove dependency
cargo rm serde

# Generate documentation
cargo doc --open

# Publish to crates.io
cargo publish
```

---

## Gotchas and Debugging

### Gotcha 1: Circular Dependencies

```toml
# crate_a/Cargo.toml
[dependencies]
crate_b = { path = "../crate_b" }

# crate_b/Cargo.toml
[dependencies]
crate_a = { path = "../crate_a" }  # ERROR: Circular!
```

**Fix**: Refactor shared code into third crate.

### Gotcha 2: Feature Unification

```toml
# Your Cargo.toml
[dependencies]
tokio = { version = "1", features = ["net"] }

# Another dependency uses:
# tokio = { version = "1", features = ["full"] }

# Result: tokio compiled with BOTH "net" and "full" (unified)
```

**Be aware**: Features are additive across dependency tree.

### Gotcha 3: Edition Mismatches

```toml
# Old crate
[package]
edition = "2018"

# Your crate
[package]
edition = "2021"  # Different edition OK!
```

**OK**: Each crate can use different edition. Compiled separately.

### Gotcha 4: Path Dependencies in Published Crates

```toml
[dependencies]
my_lib = { path = "../my_lib" }  # ERROR when publishing!
```

**Fix**: Use version from crates.io or git for published crates.

---

## Best Practices

### ✅ DO: Use Semantic Versioning

```toml
# Good: Allow compatible updates
[dependencies]
serde = "1.0"  # Gets 1.x.y updates

# Bad: Too restrictive
[dependencies]
serde = "=1.0.197"  # Blocks security fixes
```

### ✅ DO: Minimize Dependencies

```rust
// Good: Use std when possible
fn parse_number(s: &str) -> Result<i32, std::num::ParseIntError> {
    s.parse()
}

// Bad: Add dependency for simple task
// use some_parsing_crate::parse_number;
```

### ✅ DO: Commit Cargo.lock for Binaries

```bash
# Binary/app projects
git add Cargo.lock
git commit -m "Add dependency lock file"
```

### ✅ DO: Document Public APIs

```rust
/// Parses a ticket from JSON string.
///
/// # Examples
///
/// ```
/// let ticket = parse_ticket(r#"{"title": "Fix bug"}"#)?;
/// assert_eq!(ticket.title, "Fix bug");
/// ```
///
/// # Errors
///
/// Returns error if JSON is invalid.
pub fn parse_ticket(json: &str) -> Result<Ticket, serde_json::Error> {
    serde_json::from_str(json)
}
```

### ❌ DON'T: Publish with Path Dependencies

```toml
# Bad for published crates
[dependencies]
my_lib = { path = "../my_lib" }

# Good: Use crates.io version
[dependencies]
my_lib = "0.1.0"
```

### ❌ DON'T: Depend on Unstable Internal APIs

```rust
// Bad: Using internal module
use serde::private::de::...;  // May break!

// Good: Use public APIs
use serde::{Deserialize, Deserializer};
```

---

## Mental Model: Avengers Initiative

Think of Rust packages like assembling the Avengers:

1. **Initiative Dossier** (Cargo.toml):
   - Lists team members (dependencies)
   - Specifies required power levels (versions)
   - Documents mission parameters (metadata)

2. **Hero Abilities** (Library Crate):
   - Iron Man's repulsor tech (pub functions)
   - Shared across missions
   - Others can call upon these skills

3. **Mission Leader** (Binary Crate):
   - Captain America coordinates (main function)
   - Executes the mission using hero abilities
   - Entry point for action

4. **S.H.I.E.L.D. Database** (crates.io):
   - Registry of available heroes
   - Public catalog of capabilities
   - Version histories (semantic versioning)

5. **Team Roster Lock** (Cargo.lock):
   - Exact heroes on THIS mission
   - Prevents surprise replacements mid-mission
   - Reproducible team composition

6. **Training Partners** (Dev Dependencies):
   - Only for practice scenarios (tests)
   - Not deployed on actual missions
   - Help development without bloating final team

7. **Local Heroes** (Path Dependencies):
   - Teammates from nearby locations
   - Under active development
   - Not yet in public database

**The Analogy**: Just as Nick Fury assembles Avengers by recruiting heroes (dependencies) with specific capabilities (libraries) via S.H.I.E.L.D. dossiers (Cargo.toml), ensuring consistent team composition with locked rosters (Cargo.lock), Rust packages organize crates and dependencies—enabling modular code reuse across the ecosystem while maintaining reproducible builds and leveraging the community's 100,000+ crates for any capability needed.

---

## The Essence: Modular Code Organization

Packages organize Rust code via `Cargo.toml` manifest. Library crates export reusable code. Binary crates execute with `main()`. Dependencies from crates.io or paths enable code reuse. Cargo.lock ensures reproducible builds.

**Package**: Defined by Cargo.toml, contains crates  
**Library Crate**: `src/lib.rs`, exports code (max 1 per package)  
**Binary Crate**: `src/main.rs`, executable with `main()` (multiple allowed)  
**Dependencies**: `[dependencies]` in manifest, pulled from crates.io  
**Cargo.lock**: Exact versions for reproducibility (commit for apps)  
**crates.io**: Public registry with 100K+ crates

Like the Avengers Initiative assembling heroes (dependencies) with documented capabilities (libraries) and mission leaders (binaries), coordinated via S.H.I.E.L.D. dossiers (Cargo.toml) and locked rosters (Cargo.lock), Rust's package system enables modular development—organizing code into reusable libraries and executable binaries while leveraging the entire ecosystem through dependency management and reproducible builds.
