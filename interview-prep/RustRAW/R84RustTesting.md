# R84: Rust Testing - Ensuring Code Quality Through Automated Verification

## Problem Statement
**Software that works today might break tomorrow.** <cite index="18-27">Testing ensures code behaves as expected and prevents regressions</cite>. Without systematic testing, you can't verify that changes preserve existing functionality, catch bugs before production, or confidently refactor code. Manual testing is slow, error-prone, and doesn't scale. **How do you build confidence that your Rust code works correctly, now and after future changes?**

## Solution in One Sentence
**Rust provides a built-in testing framework integrated with Cargo that supports three complementary testing approaches—unit tests for isolated components, integration tests for public APIs, and documentation tests for code examples—enabling comprehensive automated verification with a single `cargo test` command.**

## Conceptual Foundation

### The Three Testing Pillars

<cite index="11-8,11-9,11-10,11-11">The Rust community thinks about tests in terms of two main categories: unit tests (small, focused, testing one module in isolation, can test private interfaces) and integration tests (entirely external, using only public interfaces, exercising multiple modules)</cite>. Plus documentation tests for verifying examples.

**Key Insight**: <cite index="18-28,18-29">Rust's testing framework is integrated into cargo, making it easy to run tests with a single command</cite>.

```rust
// All three test types run with one command:
$ cargo test
```

### Testing Philosophy

<cite index="19-14,19-15">The purpose of unit tests is to test each unit of code in isolation from the rest of the code to quickly pinpoint where code is and isn't working as expected</cite>.

<cite index="19-17,19-18,19-19">Integration tests are entirely external to your library, using only the public interface and potentially exercising multiple modules per test, allowing you to test how multiple crates interact with each other</cite>.

## MCU Metaphor: SHIELD Evaluation Protocols

Think of **your codebase as SHIELD's operations**—a complex organization with multiple divisions, each performing critical functions.

**Testing is SHIELD's evaluation system**:
- **Unit tests = Agent evaluations**: <cite index="15-11,15-12">Test functions verify non-test code is functioning in expected manner, performing setup, running code, then asserting results</cite>—like testing each agent's individual skills (marksmanship, hand-to-hand combat, intelligence analysis) in isolation
- **Integration tests = Mission simulations**: <cite index="17-8,17-9">Integration testing tests the entire process by going through multiple steps in correct order, verifying the result</cite>—like running full mission scenarios to ensure agents work together effectively
- **Documentation tests = Training manuals verification**: Ensuring SHIELD's training materials contain accurate, working examples that new recruits can follow

| SHIELD Concept | Rust Testing Equivalent |
|---------------|------------------------|
| Agent skill evaluation | Unit tests (`#[test]`) |
| Individual drill | Test function |
| Skills assessment report | `cargo test` output |
| Mission simulation | Integration tests (tests/ directory) |
| Multi-division operation | Multiple modules tested together |
| Training manual examples | Documentation tests (/// with ```) |
| Quality control director | `#[cfg(test)]` module |
| Mission success criteria | `assert!`, `assert_eq!`, `assert_ne!` |

## Anatomy of Rust Testing

### Testing Architecture

```mermaid
graph TD
    A[cargo test] --> B[Unit Tests]
    A --> C[Integration Tests]
    A --> D[Doc Tests]
    
    B --> B1[src/ files]
    B --> B2[#cfg test modules]
    B --> B3[Test private code]
    
    C --> C1[tests/ directory]
    C --> C2[Each file = separate crate]
    C --> C3[Test public API only]
    
    D --> D1[/// doc comments]
    D --> D2[``` code blocks]
    D --> D3[Ensure examples work]
    
    style A fill:#333,stroke:#666,color:#fff
    style B fill:#444,stroke:#666,color:#fff
    style C fill:#444,stroke:#666,color:#fff
    style D fill:#444,stroke:#666,color:#fff
```

### 1. Unit Tests: Testing in Isolation

<cite index="15-13,15-14,15-15">Most unit tests go into a tests mod with the #[cfg(test)] attribute; test functions are marked with #[test] and fail when something panics</cite>.

```rust
// src/lib.rs or any source file
pub fn add(a: i32, b: i32) -> i32 {
    a + b
}

pub fn divide(a: i32, b: i32) -> Result<i32, String> {
    if b == 0 {
        Err("Cannot divide by zero".to_string())
    } else {
        Ok(a / b)
    }
}

#[cfg(test)]
mod tests {
    use super::*;  // Import items from parent module
    
    #[test]
    fn test_add() {
        assert_eq!(add(2, 3), 5);
        assert_eq!(add(-1, 1), 0);
        assert_eq!(add(0, 0), 0);
    }
    
    #[test]
    fn test_divide_success() {
        assert_eq!(divide(10, 2), Ok(5));
        assert_eq!(divide(7, 3), Ok(2));
    }
    
    #[test]
    fn test_divide_by_zero() {
        assert!(divide(5, 0).is_err());
        assert_eq!(
            divide(5, 0),
            Err("Cannot divide by zero".to_string())
        );
    }
}
```

**Key attributes**:
- `#[cfg(test)]`: Only compiles test module when running `cargo test`
- `#[test]`: Marks a function as a test
- `use super::*`: Imports parent module items into test module

### 2. Integration Tests: Testing the Public API

<cite index="11-17,11-18,11-19,11-20">To create integration tests, create a tests directory at the top level of your project directory, next to src; Cargo knows to look for integration test files in this directory and compiles each file as an individual crate</cite>.

```text
my_project/
├── Cargo.toml
├── src/
│   ├── lib.rs
│   └── utils.rs
└── tests/
    ├── integration_basic.rs
    ├── integration_advanced.rs
    └── common/
        └── mod.rs  # Shared test utilities
```

```rust
// tests/integration_basic.rs
use my_project::add;  // Use crate as external dependency

#[test]
fn test_public_api() {
    assert_eq!(add(5, 7), 12);
}

#[test]
fn test_multiple_operations() {
    let result = add(add(1, 2), add(3, 4));
    assert_eq!(result, 10);
}
```

<cite index="12-8">Each Rust source file in the tests directory is compiled as a separate crate</cite>.

**Shared test utilities**:

```rust
// tests/common/mod.rs
pub fn setup_test_environment() -> TestEnv {
    TestEnv {
        // Setup code
    }
}

pub struct TestEnv {
    // Test environment state
}

// tests/integration_test.rs
mod common;  // Import shared utilities

#[test]
fn test_with_setup() {
    let env = common::setup_test_environment();
    // Test using env
}
```

### 3. Documentation Tests: Verifying Examples

<cite index="13-15,13-16">Documentation tests allow you to write sample code in your documentation comments; Rust will compile and run this code as part of your test suite, ensuring examples remain valid</cite>.

```rust
/// Multiplies two numbers together.
///
/// # Examples
///
/// Basic multiplication:
/// ```
/// let result = my_crate::multiply(6, 7);
/// assert_eq!(result, 42);
/// ```
///
/// Multiplication with zero:
/// ```
/// let result = my_crate::multiply(5, 0);
/// assert_eq!(result, 0);
/// ```
pub fn multiply(a: i32, b: i32) -> i32 {
    a * b
}
```

When you run `cargo test`, these examples are extracted, compiled, and executed!

```bash
$ cargo test --doc  # Run only documentation tests
```

**Advanced doc test features**:

```rust
/// # Examples
///
/// ```
/// # use my_crate::*;  // Hidden line (# prefix)
/// # fn expensive_setup() {}
/// expensive_setup();  // Visible in docs
/// assert_eq!(compute(), 42);
/// ```
///
/// Should panic example:
/// ```should_panic
/// divide_by_zero();  // This test expects a panic
/// ```
///
/// Ignore flaky test:
/// ```ignore
/// test_external_service();  // Skipped during normal tests
/// ```
///
/// No-run example (compile only):
/// ```no_run
/// connect_to_database();  // Compiles but doesn't run
/// ```
pub fn compute() -> i32 {
    42
}
```

## Assert Macros Family

<cite index="15-16,15-17,15-18,15-19,15-20">Helper macros: assert!(expression) panics if expression evaluates to false; assert_eq!(left, right) and assert_ne!(left, right) test for equality and inequality respectively</cite>.

### Basic Assertions

```rust
#[test]
fn test_assertions() {
    // Boolean assertion
    assert!(5 > 3);
    assert!(true);
    
    // Equality
    assert_eq!(2 + 2, 4);
    assert_eq!(vec![1, 2], vec![1, 2]);
    
    // Inequality
    assert_ne!(3, 4);
    assert_ne!("hello", "world");
}
```

### Custom Error Messages

```rust
#[test]
fn test_with_messages() {
    let x = 10;
    let y = 20;
    
    assert!(x < y, "x should be less than y: {} < {}", x, y);
    assert_eq!(x + 10, y, "x + 10 should equal y");
}
```

### Testing for Panics

```rust
#[test]
#[should_panic]
fn test_divide_by_zero_panics() {
    let _result = panic!("This should panic");
}

#[test]
#[should_panic(expected = "divide by zero")]
fn test_specific_panic_message() {
    let _result = 5 / 0;  // Should panic with specific message
}
```

### Testing with Result

```rust
#[test]
fn test_with_result() -> Result<(), String> {
    let result = divide(10, 2)?;
    if result == 5 {
        Ok(())
    } else {
        Err(format!("Expected 5, got {}", result))
    }
}
```

## Running Tests

### Basic Commands

```bash
# Run all tests
cargo test

# Run with output (show println! calls)
cargo test -- --show-output

# Run tests in serial (not parallel)
cargo test -- --test-threads=1

# Run specific test
cargo test test_add

# Run tests matching pattern
cargo test divide

# Run only unit tests
cargo test --lib

# Run only integration tests
cargo test --test integration_basic

# Run only doc tests
cargo test --doc
```

### Test Output Structure

<cite index="11-29">The three sections of output include the unit tests, the integration test, and the doc tests</cite>.

```text
$ cargo test
   Compiling myproject v0.1.0
    Finished test [unoptimized + debuginfo] target(s) in 0.50s
     Running unittests src/lib.rs (target/debug/deps/myproject-abc123)

running 5 tests
test tests::test_add ... ok
test tests::test_divide_success ... ok
test tests::test_divide_by_zero ... ok
test tests::test_multiply ... ok
test tests::test_panic ... ok

test result: ok. 5 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

     Running tests/integration_basic.rs (target/debug/deps/integration_basic-def456)

running 2 tests
test test_public_api ... ok
test test_multiple_operations ... ok

test result: ok. 2 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

   Doc-tests myproject

running 3 tests
test src/lib.rs - multiply (line 15) ... ok
test src/lib.rs - multiply (line 21) ... ok
test src/lib.rs - compute (line 35) ... ok

test result: ok. 3 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.02s
```

<cite index="11-1,11-30">If a unit test fails, integration and doc tests won't run, because those tests only run if all unit tests are passing; if any test in a section fails, the following sections will not be run</cite>.

## Advanced Testing Patterns

### Ignored Tests

<cite index="15-1,15-2">Tests can be marked with the #[ignore] attribute to exclude some tests, or run them with cargo test -- --ignored</cite>.

```rust
#[test]
#[ignore]
fn expensive_test() {
    // This test takes a long time
    thread::sleep(Duration::from_secs(60));
    assert!(true);
}

#[test]
#[ignore = "requires external service"]
fn test_external_api() {
    // Needs network access
}
```

```bash
# Run only ignored tests
cargo test -- --ignored

# Run all tests including ignored
cargo test -- --include-ignored
```

### Test Organization

```rust
// Nested test modules
#[cfg(test)]
mod tests {
    use super::*;
    
    mod addition {
        use super::*;
        
        #[test]
        fn positive_numbers() {
            assert_eq!(add(2, 3), 5);
        }
        
        #[test]
        fn negative_numbers() {
            assert_eq!(add(-2, -3), -5);
        }
    }
    
    mod subtraction {
        use super::*;
        
        #[test]
        fn basic_subtract() {
            assert_eq!(subtract(5, 3), 2);
        }
    }
}
```

### Setup and Teardown

```rust
#[cfg(test)]
mod tests {
    use super::*;
    
    fn setup() -> TestContext {
        TestContext {
            temp_dir: create_temp_directory(),
            // other setup
        }
    }
    
    #[test]
    fn test_with_setup() {
        let ctx = setup();
        // Test using ctx
        // Drop automatically cleans up (RAII)
    }
}

struct TestContext {
    temp_dir: TempDir,
}

impl Drop for TestContext {
    fn drop(&mut self) {
        // Cleanup happens automatically
    }
}
```

### Testing Private Functions

```rust
// src/lib.rs
pub fn public_function() -> i32 {
    private_helper() + 10
}

fn private_helper() -> i32 {
    42
}

#[cfg(test)]
mod tests {
    use super::*;
    
    #[test]
    fn test_private_function() {
        // Can test private functions in unit tests!
        assert_eq!(private_helper(), 42);
    }
    
    #[test]
    fn test_public_function() {
        assert_eq!(public_function(), 52);
    }
}
```

### Conditional Compilation

```rust
#[test]
#[cfg(target_os = "linux")]
fn linux_specific_test() {
    // Only runs on Linux
}

#[test]
#[cfg(not(target_os = "windows"))]
fn not_windows_test() {
    // Runs on all platforms except Windows
}
```

## Testing Async Code

```rust
// Add tokio to dev-dependencies:
// [dev-dependencies]
// tokio = { version = "1", features = ["macros", "rt"] }

#[cfg(test)]
mod tests {
    use super::*;
    
    #[tokio::test]
    async fn test_async_function() {
        let result = async_computation().await;
        assert_eq!(result, 42);
    }
    
    #[tokio::test]
    async fn test_async_timeout() {
        let result = tokio::time::timeout(
            Duration::from_secs(1),
            slow_async_function()
        ).await;
        
        assert!(result.is_ok());
    }
}

async fn async_computation() -> i32 {
    42
}

async fn slow_async_function() {
    tokio::time::sleep(Duration::from_millis(100)).await;
}
```

## Testing Error Handling

```rust
#[test]
fn test_error_types() {
    match fallible_operation() {
        Ok(_) => panic!("Expected error"),
        Err(e) => {
            assert_eq!(e.kind(), ErrorKind::NotFound);
        }
    }
}

#[test]
fn test_error_with_question_mark() -> Result<(), Box<dyn std::error::Error>> {
    let result = may_fail()?;
    assert_eq!(result, "success");
    Ok(())
}

#[test]
fn test_custom_error() {
    let err = MyError::new("test error");
    assert_eq!(err.to_string(), "test error");
    assert!(err.source().is_none());
}
```

## Benchmarking (Nightly)

```rust
#![feature(test)]
extern crate test;

#[cfg(test)]
mod benches {
    use super::*;
    use test::Bencher;
    
    #[bench]
    fn bench_add(b: &mut Bencher) {
        b.iter(|| {
            test::black_box(add(2, 3))
        });
    }
    
    #[bench]
    fn bench_multiply(b: &mut Bencher) {
        let x = test::black_box(100);
        let y = test::black_box(200);
        
        b.iter(|| {
            multiply(x, y)
        });
    }
}
```

```bash
# Run benchmarks (requires nightly)
cargo +nightly bench
```

## Mock Objects and Test Doubles

```rust
// Using trait for testability
trait DataStore {
    fn get(&self, key: &str) -> Option<String>;
    fn set(&mut self, key: String, value: String);
}

struct RealDataStore {
    // Real implementation
}

impl DataStore for RealDataStore {
    fn get(&self, key: &str) -> Option<String> {
        // Real database access
        unimplemented!()
    }
    
    fn set(&mut self, key: String, value: String) {
        // Real database write
    }
}

// Mock for testing
#[cfg(test)]
struct MockDataStore {
    data: std::collections::HashMap<String, String>,
}

#[cfg(test)]
impl DataStore for MockDataStore {
    fn get(&self, key: &str) -> Option<String> {
        self.data.get(key).cloned()
    }
    
    fn set(&mut self, key: String, value: String) {
        self.data.insert(key, value);
    }
}

fn process_data(store: &mut dyn DataStore, key: &str) -> Option<String> {
    store.get(key).map(|v| v.to_uppercase())
}

#[cfg(test)]
mod tests {
    use super::*;
    
    #[test]
    fn test_with_mock() {
        let mut mock = MockDataStore {
            data: std::collections::HashMap::new(),
        };
        mock.set("test".to_string(), "value".to_string());
        
        let result = process_data(&mut mock, "test");
        assert_eq!(result, Some("VALUE".to_string()));
    }
}
```

## Best Practices and Gotchas

### ✅ DO: Write Tests First (TDD)

```rust
// 1. Write the test
#[test]
fn test_factorial() {
    assert_eq!(factorial(5), 120);
    assert_eq!(factorial(0), 1);
}

// 2. Watch it fail
// 3. Implement the function
pub fn factorial(n: u64) -> u64 {
    match n {
        0 | 1 => 1,
        _ => n * factorial(n - 1),
    }
}

// 4. Watch it pass
// 5. Refactor if needed
```

### ✅ DO: Test Edge Cases

```rust
#[test]
fn test_edge_cases() {
    // Empty input
    assert_eq!(process_vec(&[]), vec![]);
    
    // Single element
    assert_eq!(process_vec(&[1]), vec![1]);
    
    // Boundary values
    assert_eq!(parse_age("0"), Some(0));
    assert_eq!(parse_age("150"), Some(150));
    
    // Invalid input
    assert_eq!(parse_age("-1"), None);
    assert_eq!(parse_age("abc"), None);
}
```

### ✅ DO: Use Descriptive Test Names

```rust
#[test]
fn test_add() { /* ❌ Too vague */ }

#[test]
fn test_add_positive_numbers_returns_sum() { /* ✅ Clear intent */ }

#[test]
fn add_negative_numbers_returns_correct_negative_sum() { /* ✅ Even better */ }
```

### ✅ DO: One Assertion Per Test (When Possible)

```rust
// ❌ Multiple unrelated assertions
#[test]
fn test_everything() {
    assert_eq!(add(2, 3), 5);
    assert_eq!(multiply(2, 3), 6);
    assert_eq!(divide(6, 2), Ok(3));
}

// ✅ Separate focused tests
#[test]
fn add_returns_sum() {
    assert_eq!(add(2, 3), 5);
}

#[test]
fn multiply_returns_product() {
    assert_eq!(multiply(2, 3), 6);
}

#[test]
fn divide_returns_quotient() {
    assert_eq!(divide(6, 2), Ok(3));
}
```

### ❌ DON'T: Test Implementation Details

```rust
// ❌ BAD: Testing internal structure
#[test]
fn test_internal_cache_size() {
    let processor = Processor::new();
    assert_eq!(processor.cache.len(), 0);  // Implementation detail!
}

// ✅ GOOD: Test behavior
#[test]
fn test_processor_computes_correctly() {
    let mut processor = Processor::new();
    assert_eq!(processor.process(5), 25);
}
```

### ❌ DON'T: Rely on Test Execution Order

```rust
// ❌ BAD: Tests depend on each other
static mut GLOBAL_STATE: i32 = 0;

#[test]
fn test_one() {
    unsafe { GLOBAL_STATE = 5; }
}

#[test]
fn test_two() {
    unsafe { assert_eq!(GLOBAL_STATE, 5); }  // Fragile!
}

// ✅ GOOD: Tests are independent
#[test]
fn test_with_own_state() {
    let state = 5;
    assert_eq!(process(state), 10);
}
```

## Comparison with Other Languages

| Language | Testing Framework | Built-in Support | Test Location |
|----------|------------------|------------------|---------------|
| **Rust** | Built-in | ✅ Yes (`cargo test`) | Same file + tests/ dir | <cite index="18-28">Built-in framework integrated with cargo</cite> |
| **Go** | Built-in | ✅ Yes (`go test`) | *_test.go files |
| **Python** | unittest/pytest | ⚠️ Partial (unittest) | Separate test files |
| **Java** | JUnit | ❌ External | Separate test classes |
| **JavaScript** | Jest/Mocha | ❌ External | Separate test files |
| **C++** | Google Test | ❌ External | Separate test files |

## Summary

**Testing in Rust is a first-class citizen** with <cite index="20-11,20-12">first-class support for unit and integration testing, integrated into cargo</cite>.

**Three testing approaches**:
1. **Unit tests**: <cite index="11-9">Small, focused, testing one module in isolation, can test private interfaces</cite>
2. **Integration tests**: <cite index="11-10">Entirely external, using only public interface, exercising multiple modules per test</cite>
3. **Documentation tests**: <cite index="13-16">Compile and run sample code in documentation, ensuring examples remain valid</cite>

**Key principles**:
- Write tests alongside code (`#[cfg(test)]`)
- Use `assert!`, `assert_eq!`, `assert_ne!` for verification
- Test edge cases and error conditions
- Keep tests independent and focused
- Run `cargo test` frequently during development

**Remember**: <cite index="18-10">Testing is essential to software development, ensuring code behaves as expected and preventing regressions</cite>—invest in tests to move faster with confidence!

---

**Further Reading**:
- [The Rust Book: Writing Tests](https://doc.rust-lang.org/book/ch11-00-testing.html)
- [Rust By Example: Testing](https://doc.rust-lang.org/rust-by-example/testing.html)
- [Cargo Book: Tests](https://doc.rust-lang.org/cargo/guide/tests.html)

<citations>
  <document>
    <document_type>WEB_SEARCH_RESULT</document_type>
    <document_id>11</document_id>
  </document>
  <document>
    <document_type>WEB_SEARCH_RESULT</document_type>
    <document_id>12</document_id>
  </document>
  <document>
    <document_type>WEB_SEARCH_RESULT</document_type>
    <document_id>13</document_id>
  </document>
  <document>
    <document_type>WEB_SEARCH_RESULT</document_type>
    <document_id>15</document_id>
  </document>
  <document>
    <document_type>WEB_SEARCH_RESULT</document_type>
    <document_id>17</document_id>
  </document>
  <document>
    <document_type>WEB_SEARCH_RESULT</document_type>
    <document_id>18</document_id>
  </document>
  <document>
    <document_type>WEB_SEARCH_RESULT</document_type>
    <document_id>19</document_id>
  </document>
  <document>
    <document_type>WEB_SEARCH_RESULT</document_type>
    <document_id>20</document_id>
  </document>
</citations>
