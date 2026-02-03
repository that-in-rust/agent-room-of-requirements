# Ruby Keyword Transpilation Analysis for Rust

**Date:** 2026-02-03
**Purpose:** Comprehensive feasibility analysis for Ruby-to-Rust transpilation
**Context:** Supporting the "Develop in Ruby, Deploy in Rust" thesis (30x speedup target)

---

## Executive Summary

This document analyzes all 41 Ruby keywords, common Rails DSL patterns, and core Ruby language features for transpilation feasibility to Rust using the `enum Value` runtime pattern.

**Key Findings:**
- **20/41 keywords** (49%) are straightforward to transpile
- **15/41 keywords** (37%) require moderate runtime support
- **6/41 keywords** (15%) are hard or require extensive runtime
- **Rails DSL patterns** are extremely challenging (metaprogramming-heavy)
- **Recommended approach:** Transpile algorithmic Ruby code, keep Rails/DSL in Ruby

---

## Section 1: Core Ruby Keywords Analysis

### 1. `__ENCODING__`

**Purpose:** Returns the encoding of the current source file (e.g., UTF-8).

**Transpilation Strategy:**
- Replace with a compile-time constant based on source file encoding
- Map to Rust string literal or encoding metadata

**Feasibility:** ✅ **Easy**

**Example:**
```ruby
# Ruby
puts __ENCODING__  # => #<Encoding:UTF-8>
```

```rust
// Rust
println!("{}", "UTF-8");
// Or store as const:
const SOURCE_ENCODING: &str = "UTF-8";
```

---

### 2. `__LINE__`

**Purpose:** Returns the current line number in the source file.

**Transpilation Strategy:**
- Replace with `line!()` macro in Rust
- Direct mapping, compile-time expansion

**Feasibility:** ✅ **Easy**

**Example:**
```ruby
# Ruby
puts "Error at line #{__LINE__}"  # => "Error at line 42"
```

```rust
// Rust
println!("Error at line {}", line!());
```

---

### 3. `__FILE__`

**Purpose:** Returns the current source file path.

**Transpilation Strategy:**
- Replace with `file!()` macro in Rust
- Direct mapping, compile-time expansion

**Feasibility:** ✅ **Easy**

**Example:**
```ruby
# Ruby
puts "Running #{__FILE__}"  # => "Running app.rb"
```

```rust
// Rust
println!("Running {}", file!());
```

---

### 4. `BEGIN`

**Purpose:** Defines a block of code to execute before the main program runs (initialization).

**Transpilation Strategy:**
- Move BEGIN blocks to module-level initialization
- Execute in `fn main()` before user code
- Collect all BEGIN blocks and order them

**Feasibility:** ⚠️ **Moderate** (requires ordering across files)

**Example:**
```ruby
# Ruby
BEGIN {
  puts "Initializing..."
}
puts "Main program"
# Output: Initializing... \n Main program
```

```rust
// Rust
fn main() {
    // Transpiled BEGIN blocks
    println!("Initializing...");

    // User's main code
    println!("Main program");
}
```

**Limitation:** Multiple BEGIN blocks in different files require careful ordering.

---

### 5. `END`

**Purpose:** Defines a block of code to execute when the program exits (cleanup).

**Transpilation Strategy:**
- Use Rust's `Drop` trait or `defer` pattern
- Register cleanup functions to run at program exit
- Use `std::process::exit` hooks or atexit-like mechanism

**Feasibility:** ⚠️ **Moderate** (requires runtime registration)

**Example:**
```ruby
# Ruby
END {
  puts "Cleaning up..."
}
puts "Main program"
# Output: Main program \n Cleaning up...
```

```rust
// Rust
use std::sync::Once;

static CLEANUP: Once = Once::new();

fn register_cleanup() {
    CLEANUP.call_once(|| {
        // Register cleanup
        std::panic::set_hook(Box::new(|_| {
            println!("Cleaning up...");
        }));
    });
}

fn main() {
    register_cleanup();
    println!("Main program");
}
// Or use scopeguard crate for RAII cleanup
```

---

### 6. `alias`

**Purpose:** Creates an alias for a method (e.g., `alias new_name old_name`).

**Transpilation Strategy:**
- For static methods: create wrapper function
- For dynamic/runtime aliases: store in method table (runtime)
- Statically analyzable cases are easy, dynamic cases need runtime

**Feasibility:** ⚠️ **Moderate** (static) / 🔴 **Runtime** (dynamic)

**Example:**
```ruby
# Ruby
class User
  def name
    @name
  end
  alias username name  # Static alias
end

user = User.new
user.username  # => calls name method
```

```rust
// Rust (static case)
struct User {
    name_field: String,
}

impl User {
    fn name(&self) -> &str {
        &self.name_field
    }

    fn username(&self) -> &str {
        self.name()  // Alias implemented as wrapper
    }
}
```

**Dynamic case (runtime required):**
```ruby
# Ruby
alias_name = :username
alias alias_name :name  # Dynamic, needs runtime
```

---

### 7. `and`

**Purpose:** Logical AND operator (lower precedence than `&&`).

**Transpilation Strategy:**
- Transpile to `&&` in Rust
- Both short-circuit, semantically equivalent

**Feasibility:** ✅ **Easy**

**Example:**
```ruby
# Ruby
result = true and false  # => false
```

```rust
// Rust
let result = true && false;  // => false
```

---

### 8. `begin`

**Purpose:** Starts an exception handling block (with `rescue`, `ensure`, `end`).

**Transpilation Strategy:**
- Map to Rust's `Result<T, E>` and pattern matching
- `begin...rescue...end` → match on Result
- `ensure` → closure with cleanup (or defer pattern)

**Feasibility:** ⚠️ **Moderate**

**Example:**
```ruby
# Ruby
begin
  risky_operation()
rescue StandardError => e
  puts "Error: #{e.message}"
ensure
  cleanup()
end
```

```rust
// Rust
fn risky_operation() -> Result<(), Box<dyn std::error::Error>> {
    // ...
}

fn main() {
    let _guard = scopeguard::guard((), |_| cleanup());  // ensure

    match risky_operation() {
        Ok(_) => {},
        Err(e) => println!("Error: {}", e),  // rescue
    }
}
```

**Challenge:** Ruby's exception hierarchy vs Rust's error types.

---

### 9. `break`

**Purpose:** Exits from a loop or block early.

**Transpilation Strategy:**
- In loops: direct `break` in Rust
- In blocks with values: return from closure/function
- Ruby's `break value` from block needs special handling

**Feasibility:** ✅ **Easy** (loops) / ⚠️ **Moderate** (blocks with values)

**Example:**
```ruby
# Ruby (loop)
[1, 2, 3].each do |n|
  break if n == 2
  puts n
end
# Output: 1

# Ruby (block with value)
result = [1, 2, 3].each do |n|
  break "found" if n == 2
end
# result => "found"
```

```rust
// Rust (loop)
for n in vec![1, 2, 3] {
    if n == 2 {
        break;
    }
    println!("{}", n);
}

// Rust (block with value - requires different approach)
let result = vec![1, 2, 3].iter()
    .find_map(|&n| {
        if n == 2 {
            Some("found")
        } else {
            None
        }
    })
    .unwrap_or_default();
```

---

### 10. `case`

**Purpose:** Multi-way conditional (switch/match statement).

**Transpilation Strategy:**
- Map to Rust's `match` expression
- Ruby's `===` operator for case equality needs runtime support
- Simple literal cases are easy, complex === needs Value enum

**Feasibility:** ✅ **Easy** (literals) / ⚠️ **Moderate** (complex patterns)

**Example:**
```ruby
# Ruby
case x
when 1, 2
  "small"
when 3..10
  "medium"
when String
  "text"
else
  "other"
end
```

```rust
// Rust (simplified)
match x {
    Value::Int(1) | Value::Int(2) => Value::str("small"),
    Value::Int(3..=10) => Value::str("medium"),
    Value::String(_) => Value::str("text"),
    _ => Value::str("other"),
}
```

**Challenge:** Ruby's `===` operator is dynamic (Range#===, Class#===, Regexp#===).

---

### 11. `class`

**Purpose:** Defines a class.

**Transpilation Strategy:**
- Map to Rust `struct` + `impl` blocks
- Instance variables → struct fields
- Methods → impl methods
- Inheritance → trait delegation or composition

**Feasibility:** ✅ **Easy** (simple classes) / ⚠️ **Moderate** (inheritance) / 🔴 **Runtime** (metaprogramming)

**Example:**
```ruby
# Ruby
class User
  def initialize(name)
    @name = name
  end

  def greet
    "Hello, #{@name}"
  end
end
```

```rust
// Rust
struct User {
    name: String,
}

impl User {
    fn new(name: String) -> Self {
        User { name }
    }

    fn greet(&self) -> String {
        format!("Hello, {}", self.name)
    }
}
```

---

### 12. `def`

**Purpose:** Defines a method.

**Transpilation Strategy:**
- Map to Rust function or impl method
- Instance methods → `&self` or `&mut self`
- Class methods → associated functions
- Block parameters → closures

**Feasibility:** ✅ **Easy** (simple methods) / ⚠️ **Moderate** (blocks, splats)

**Example:**
```ruby
# Ruby
def add(a, b)
  a + b
end

class Math
  def self.multiply(a, b)
    a * b
  end
end
```

```rust
// Rust
fn add(a: i64, b: i64) -> i64 {
    a + b
}

struct Math;

impl Math {
    fn multiply(a: i64, b: i64) -> i64 {
        a * b
    }
}
```

---

### 13. `defined?`

**Purpose:** Tests whether an expression is defined (variable, method, constant).

**Transpilation Strategy:**
- Compile-time analysis for most cases
- Variables: check scope at transpile time
- Methods: check impl blocks
- Dynamic cases: runtime symbol table lookup

**Feasibility:** ⚠️ **Moderate** (static analysis) / 🔴 **Runtime** (dynamic checks)

**Example:**
```ruby
# Ruby
defined?(x)        # => nil (if x not defined)
defined?(puts)     # => "method"
defined?(String)   # => "constant"
```

```rust
// Rust (compile-time)
// Most uses can be eliminated during transpilation
// Runtime cases need symbol table:

match runtime.is_defined("x") {
    Some(_) => Value::str("local-variable"),
    None => Value::nil(),
}
```

**Challenge:** Highly dynamic, requires runtime reflection.

---

### 14. `do`

**Purpose:** Starts a block (alternative to `{}`).

**Transpilation Strategy:**
- Map to Rust closure `|| { ... }`
- Multi-line blocks use `do...end`
- Pass closures to iterator methods

**Feasibility:** ✅ **Easy**

**Example:**
```ruby
# Ruby
[1, 2, 3].each do |n|
  puts n
end
```

```rust
// Rust
vec![1, 2, 3].iter().for_each(|n| {
    println!("{}", n);
});
```

---

### 15. `else`

**Purpose:** Alternate branch in conditional.

**Transpilation Strategy:**
- Direct mapping to Rust `else`

**Feasibility:** ✅ **Easy**

**Example:**
```ruby
# Ruby
if condition
  action1
else
  action2
end
```

```rust
// Rust
if condition {
    action1();
} else {
    action2();
}
```

---

### 16. `elsif`

**Purpose:** Additional conditional branch (else-if).

**Transpilation Strategy:**
- Map to Rust `else if`

**Feasibility:** ✅ **Easy**

**Example:**
```ruby
# Ruby
if x < 0
  "negative"
elsif x == 0
  "zero"
else
  "positive"
end
```

```rust
// Rust
if x < 0 {
    "negative"
} else if x == 0 {
    "zero"
} else {
    "positive"
}
```

---

### 17. `end`

**Purpose:** Closes block-level constructs (class, def, if, etc.).

**Transpilation Strategy:**
- Map to closing brace `}` in Rust
- Purely syntactic

**Feasibility:** ✅ **Easy**

---

### 18. `ensure`

**Purpose:** Code that runs after a begin block, regardless of exceptions (like `finally`).

**Transpilation Strategy:**
- Use `scopeguard` crate or RAII pattern
- Defer execution to scope exit
- Combine with Result handling

**Feasibility:** ⚠️ **Moderate**

**Example:**
```ruby
# Ruby
begin
  risky_operation()
ensure
  cleanup()
end
```

```rust
// Rust
{
    let _guard = scopeguard::guard((), |_| cleanup());
    risky_operation();
}
// cleanup() runs when _guard drops
```

---

### 19. `false`

**Purpose:** Boolean false literal.

**Transpilation Strategy:**
- Direct mapping to Rust `false`
- Or `Value::Bool(false)` in enum runtime

**Feasibility:** ✅ **Easy**

**Example:**
```ruby
# Ruby
result = false
```

```rust
// Rust
let result = false;
// Or: let result = Value::Bool(false);
```

---

### 20. `for`

**Purpose:** Iterates over a collection (less common than `.each` in Ruby).

**Transpilation Strategy:**
- Map to Rust `for...in` loop
- Requires collection to implement Iterator trait

**Feasibility:** ✅ **Easy**

**Example:**
```ruby
# Ruby
for n in [1, 2, 3]
  puts n
end
```

```rust
// Rust
for n in vec![1, 2, 3] {
    println!("{}", n);
}
```

---

### 21. `if`

**Purpose:** Conditional execution.

**Transpilation Strategy:**
- Direct mapping to Rust `if`
- Ruby's if-as-expression maps to Rust if expression

**Feasibility:** ✅ **Easy**

**Example:**
```ruby
# Ruby
x = if condition
  10
else
  20
end
```

```rust
// Rust
let x = if condition {
    10
} else {
    20
};
```

---

### 22. `in`

**Purpose:** Used in `for...in` loops and pattern matching (Ruby 2.7+).

**Transpilation Strategy:**
- Part of `for` syntax, handled with loop transpilation
- Pattern matching `in` → Rust match patterns

**Feasibility:** ✅ **Easy**

**Example:**
```ruby
# Ruby
for x in [1, 2, 3]
  puts x
end

# Pattern matching (Ruby 3.0+)
case [1, 2]
in [a, b]
  puts "#{a}, #{b}"
end
```

```rust
// Rust
for x in vec![1, 2, 3] {
    println!("{}", x);
}

// Pattern matching
match vec![1, 2] {
    v if v.len() == 2 => {
        let a = v[0];
        let b = v[1];
        println!("{}, {}", a, b);
    }
    _ => {}
}
```

---

### 23. `module`

**Purpose:** Defines a module (namespace and mixin).

**Transpilation Strategy:**
- Namespace use → Rust `mod` module
- Mixin use → Rust trait + blanket impl
- Module functions → free functions in module

**Feasibility:** ⚠️ **Moderate** (namespaces are easy, mixins need traits)

**Example:**
```ruby
# Ruby (namespace)
module Math
  def self.add(a, b)
    a + b
  end
end

# Ruby (mixin)
module Greetable
  def greet
    "Hello"
  end
end

class User
  include Greetable
end
```

```rust
// Rust (namespace)
mod math {
    pub fn add(a: i64, b: i64) -> i64 {
        a + b
    }
}

// Rust (mixin via trait)
trait Greetable {
    fn greet(&self) -> &str {
        "Hello"
    }
}

struct User;

impl Greetable for User {}
```

---

### 24. `next`

**Purpose:** Skips to next iteration of loop (like `continue`).

**Transpilation Strategy:**
- Direct mapping to Rust `continue`
- In blocks: early return from closure

**Feasibility:** ✅ **Easy** (loops) / ⚠️ **Moderate** (blocks)

**Example:**
```ruby
# Ruby
[1, 2, 3].each do |n|
  next if n == 2
  puts n
end
# Output: 1, 3
```

```rust
// Rust
for n in vec![1, 2, 3] {
    if n == 2 {
        continue;
    }
    println!("{}", n);
}
```

---

### 25. `nil`

**Purpose:** Represents the absence of a value.

**Transpilation Strategy:**
- Map to `Option::None` or `Value::Nil` in enum runtime
- Nil checks → `is_none()` or pattern matching

**Feasibility:** ✅ **Easy**

**Example:**
```ruby
# Ruby
x = nil
if x.nil?
  puts "x is nil"
end
```

```rust
// Rust
let x: Option<i64> = None;
if x.is_none() {
    println!("x is nil");
}

// Or with Value enum:
let x = Value::Nil;
if x.is_nil() {
    println!("x is nil");
}
```

---

### 26. `not`

**Purpose:** Logical NOT operator (lower precedence than `!`).

**Transpilation Strategy:**
- Map to Rust `!` operator
- Semantically equivalent

**Feasibility:** ✅ **Easy**

**Example:**
```ruby
# Ruby
result = not true  # => false
```

```rust
// Rust
let result = !true;  // => false
```

---

### 27. `or`

**Purpose:** Logical OR operator (lower precedence than `||`).

**Transpilation Strategy:**
- Map to Rust `||`
- Both short-circuit

**Feasibility:** ✅ **Easy**

**Example:**
```ruby
# Ruby
result = false or true  # => true
```

```rust
// Rust
let result = false || true;  // => true
```

---

### 28. `redo`

**Purpose:** Restarts current iteration of loop without re-evaluating condition.

**Transpilation Strategy:**
- Use labeled loops in Rust with `continue 'label`
- Restructure loop logic
- Complex control flow, may need state machine

**Feasibility:** ❌ **Hard**

**Example:**
```ruby
# Ruby
i = 0
while i < 3
  puts i
  i += 1
  redo if i == 2  # Infinite loop at i=2 (dangerous!)
end
```

```rust
// Rust (approximation, requires careful restructuring)
let mut i = 0;
'outer: loop {
    if i >= 3 {
        break;
    }
    println!("{}", i);
    i += 1;
    if i == 2 {
        i -= 1;  // Reset to redo
        continue 'outer;
    }
}
```

**Challenge:** Rare in practice, complex semantics.

---

### 29. `rescue`

**Purpose:** Catches exceptions in a begin block.

**Transpilation Strategy:**
- Map to Result pattern matching
- Exception types → custom Error enums
- Inline rescue modifier → `unwrap_or` or `ok()`

**Feasibility:** ⚠️ **Moderate**

**Example:**
```ruby
# Ruby
begin
  result = risky_operation()
rescue ArgumentError => e
  puts "Bad argument: #{e}"
rescue StandardError => e
  puts "Error: #{e}"
end

# Inline modifier
value = risky_operation() rescue default_value
```

```rust
// Rust
match risky_operation() {
    Ok(result) => result,
    Err(e) if e.is::<ArgumentError>() => {
        println!("Bad argument: {}", e);
    }
    Err(e) => {
        println!("Error: {}", e);
    }
}

// Inline modifier
let value = risky_operation().unwrap_or(default_value);
```

**Challenge:** Ruby's exception hierarchy vs Rust's error types.

---

### 30. `retry`

**Purpose:** Restarts a begin block after an exception.

**Transpilation Strategy:**
- Wrap in loop with retry counter
- Use loop label and `continue`
- Add max retry limit to prevent infinite loops

**Feasibility:** ❌ **Hard**

**Example:**
```ruby
# Ruby
retries = 0
begin
  risky_operation()
rescue NetworkError
  retries += 1
  retry if retries < 3
end
```

```rust
// Rust
let mut retries = 0;
loop {
    match risky_operation() {
        Ok(result) => break result,
        Err(e) if e.is_network_error() && retries < 3 => {
            retries += 1;
            continue;  // Retry
        }
        Err(e) => {
            // Handle or propagate error
            panic!("{}", e);
        }
    }
}
```

**Challenge:** Uncommon, requires loop restructuring.

---

### 31. `return`

**Purpose:** Exits from a method with a value.

**Transpilation Strategy:**
- Direct mapping to Rust `return`
- Ruby's implicit return (last expression) → remove `return` keyword

**Feasibility:** ✅ **Easy**

**Example:**
```ruby
# Ruby
def add(a, b)
  return a + b
end

def subtract(a, b)
  a - b  # Implicit return
end
```

```rust
// Rust
fn add(a: i64, b: i64) -> i64 {
    return a + b;
}

fn subtract(a: i64, b: i64) -> i64 {
    a - b  // Implicit return
}
```

---

### 32. `self`

**Purpose:** Refers to the current object.

**Transpilation Strategy:**
- Instance context → `self` in Rust methods
- Class context → type name (e.g., `User::`)
- Direct mapping in most cases

**Feasibility:** ✅ **Easy**

**Example:**
```ruby
# Ruby
class User
  def initialize(name)
    @name = name
  end

  def greet_self
    self.greet
  end

  def self.species
    "human"
  end
end
```

```rust
// Rust
struct User {
    name: String,
}

impl User {
    fn new(name: String) -> Self {
        User { name }
    }

    fn greet_self(&self) -> String {
        self.greet()
    }

    fn species() -> &'static str {
        "human"
    }
}
```

---

### 33. `super`

**Purpose:** Calls the parent class's method of the same name.

**Transpilation Strategy:**
- Store parent method reference in trait
- Explicit parent call via trait method
- Requires inheritance modeling (trait delegation or enum wrapper)

**Feasibility:** ⚠️ **Moderate** (single inheritance) / ❌ **Hard** (complex hierarchies)

**Example:**
```ruby
# Ruby
class Animal
  def speak
    "noise"
  end
end

class Dog < Animal
  def speak
    super + " woof"
  end
end
```

```rust
// Rust (using trait)
trait Animal {
    fn speak(&self) -> String {
        "noise".to_string()
    }
}

struct Dog;

impl Animal for Dog {
    fn speak(&self) -> String {
        // Call "super" via default trait impl
        format!("{} woof", Animal::speak(&Self::parent_instance()))
    }
}

// Alternative: explicit parent field
struct Dog {
    parent: AnimalImpl,
}

impl Dog {
    fn speak(&self) -> String {
        format!("{} woof", self.parent.speak())
    }
}
```

**Challenge:** Rust has no inheritance, requires trait or composition patterns.

---

### 34. `then`

**Purpose:** Optional keyword after `if`, `unless`, `when` (rarely used).

**Transpilation Strategy:**
- Purely syntactic sugar in Ruby
- Ignore during transpilation, has no semantic meaning

**Feasibility:** ✅ **Easy**

**Example:**
```ruby
# Ruby
if condition then action end
# Same as: if condition; action; end
```

```rust
// Rust (then is omitted)
if condition { action(); }
```

---

### 35. `true`

**Purpose:** Boolean true literal.

**Transpilation Strategy:**
- Direct mapping to Rust `true`
- Or `Value::Bool(true)` in enum runtime

**Feasibility:** ✅ **Easy**

**Example:**
```ruby
# Ruby
result = true
```

```rust
// Rust
let result = true;
// Or: let result = Value::Bool(true);
```

---

### 36. `undef`

**Purpose:** Undefines a method (removes it from a class/module).

**Transpilation Strategy:**
- Compile-time: error if calling undefined method
- Runtime: requires method table manipulation (hard)
- Static analysis can detect and error

**Feasibility:** ⚠️ **Moderate** (compile-time detection) / 🔴 **Runtime** (dynamic undef)

**Example:**
```ruby
# Ruby
class User
  def secret
    "password123"
  end

  undef secret  # Remove method
end

# User.new.secret  # => NoMethodError
```

```rust
// Rust (compile-time)
// Transpiler removes the method from impl block
struct User;

impl User {
    // secret method not generated
}

// Calling user.secret() would fail at compile time
```

**Dynamic case (runtime):**
```ruby
# Ruby
method_name = :secret
undef method_name  # Dynamic, requires runtime
```
→ Requires runtime method table, very hard.

---

### 37. `unless`

**Purpose:** Inverted conditional (if not).

**Transpilation Strategy:**
- Map to `if !condition` in Rust
- Semantically equivalent

**Feasibility:** ✅ **Easy**

**Example:**
```ruby
# Ruby
unless condition
  action
end
```

```rust
// Rust
if !condition {
    action();
}
```

---

### 38. `until`

**Purpose:** Loop that continues while condition is false (inverse of `while`).

**Transpilation Strategy:**
- Map to `while !condition` in Rust
- Direct transformation

**Feasibility:** ✅ **Easy**

**Example:**
```ruby
# Ruby
i = 0
until i >= 5
  puts i
  i += 1
end
```

```rust
// Rust
let mut i = 0;
while !(i >= 5) {
    println!("{}", i);
    i += 1;
}
// Or: while i < 5 { ... }
```

---

### 39. `when`

**Purpose:** Branch in a `case` statement.

**Transpilation Strategy:**
- Part of `case` → Rust `match` arm
- Handled with case transpilation

**Feasibility:** ✅ **Easy**

**Example:**
```ruby
# Ruby
case x
when 1
  "one"
when 2
  "two"
end
```

```rust
// Rust
match x {
    1 => "one",
    2 => "two",
    _ => "",
}
```

---

### 40. `while`

**Purpose:** Loop that continues while condition is true.

**Transpilation Strategy:**
- Direct mapping to Rust `while`

**Feasibility:** ✅ **Easy**

**Example:**
```ruby
# Ruby
i = 0
while i < 5
  puts i
  i += 1
end
```

```rust
// Rust
let mut i = 0;
while i < 5 {
    println!("{}", i);
    i += 1;
}
```

---

### 41. `yield`

**Purpose:** Calls the block passed to the current method.

**Transpilation Strategy:**
- Pass closures as parameters
- `yield` → closure call
- `yield(args)` → closure with arguments
- Block detection via `block_given?` → Option<Fn>

**Feasibility:** ⚠️ **Moderate**

**Example:**
```ruby
# Ruby
def with_logging
  puts "Starting"
  yield
  puts "Done"
end

with_logging { puts "Working" }
# Output: Starting \n Working \n Done
```

```rust
// Rust
fn with_logging<F>(block: F)
where
    F: FnOnce(),
{
    println!("Starting");
    block();  // yield
    println!("Done");
}

fn main() {
    with_logging(|| {
        println!("Working");
    });
}
```

**Challenge:** Ruby blocks are more flexible (can be optional, multiple yields, etc.).

---

## Section 2: Rails DSL Patterns

Rails heavily uses metaprogramming, making most patterns **very difficult** to transpile.

### ActiveRecord Associations

**Pattern:** `has_many :posts`, `belongs_to :user`

**Transpilation Feasibility:** 🔴 **Requires Runtime**

**Why Hard:**
- These are macro calls that dynamically define methods
- `has_many :posts` generates: `posts()`, `posts=()`, `posts<<()`, etc.
- Requires reading association metadata and generating code
- Database interactions need ORM runtime

**Strategy:**
- Could use procedural macros in Rust to generate similar code
- Requires full ActiveRecord-like ORM in Rust (e.g., Diesel)
- **Recommendation:** Keep ActiveRecord models in Ruby, transpile business logic only

**Example:**
```ruby
# Ruby
class User < ApplicationRecord
  has_many :posts
  belongs_to :organization
end

user.posts.each { |p| puts p.title }
```

```rust
// Rust (theoretical, using Diesel ORM)
#[derive(Queryable, Associations)]
#[belongs_to(Organization)]
struct User {
    id: i32,
    organization_id: i32,
}

#[derive(Queryable, Associations)]
#[belongs_to(User)]
struct Post {
    id: i32,
    user_id: i32,
    title: String,
}

// Would need Diesel runtime + code generation
// Not practical for transpilation
```

---

### ActiveRecord Validations

**Pattern:** `validates :email, presence: true, uniqueness: true`

**Transpilation Feasibility:** 🔴 **Requires Runtime**

**Why Hard:**
- Validation macros generate complex runtime checks
- Database uniqueness checks require ActiveRecord
- Callbacks and lifecycle hooks are metaprogramming

**Strategy:**
- Could manually transpile validation logic to Rust functions
- Would lose Rails magic, require explicit calls
- **Recommendation:** Keep validations in Ruby layer

---

### ActiveRecord Scopes

**Pattern:** `scope :active, -> { where(active: true) }`

**Transpilation Feasibility:** ❌ **Hard**

**Why Hard:**
- Scopes are lazy-evaluated query builders
- Require ActiveRecord's Arel query DSL
- Dynamic method chaining

**Strategy:**
- Transpile to Diesel query builder methods
- Requires ORM translation layer
- **Recommendation:** Keep in Ruby

---

### ActiveRecord Callbacks

**Pattern:** `before_save :normalize_email`, `after_create :send_welcome_email`

**Transpilation Feasibility:** 🔴 **Requires Runtime**

**Why Hard:**
- Callback registration is dynamic
- Lifecycle hooks depend on ActiveRecord internals
- Order of execution is runtime-determined

**Strategy:**
- Manual event handlers in Rust
- Explicit before/after calls
- **Recommendation:** Keep in Ruby, or refactor to explicit service objects

---

### Rails Routing

**Pattern:** `resources :users`, `get '/about', to: 'pages#about'`

**Transpilation Feasibility:** ❌ **Hard** (entire web framework)

**Why Hard:**
- Routing DSL generates complex dispatch tables
- Controller integration requires Rails infrastructure
- Middleware stack, filters, etc.

**Strategy:**
- Use Rust web framework (Actix, Axum) with similar routing
- Manually map routes
- **Recommendation:** Keep Rails routing, transpile controller logic only (maybe)

---

### Rails Controllers

**Pattern:** `before_action :authenticate_user!`, `render json: @user`

**Transpilation Feasibility:** ❌ **Hard**

**Why Hard:**
- Controllers depend on Rails framework
- `render`, `redirect_to`, parameter parsing are Rails-specific
- Filters and callbacks are metaprogramming

**Strategy:**
- Transpile business logic to Rust functions
- Call from Ruby controllers
- **Recommendation:** Keep controllers in Ruby, transpile service layer

---

### Rails Views

**Pattern:** `<%= render partial: 'user', locals: { user: @user } %>`

**Transpilation Feasibility:** ❌ **Hard** (templating engine)

**Why Hard:**
- ERB templates are Ruby code execution
- Partial rendering, layouts, helpers are Rails-specific
- Would need Rust templating engine (Tera, Askama)

**Strategy:**
- Keep views in Ruby/ERB
- Or switch to API-only Rails + frontend framework
- **Recommendation:** Don't transpile views

---

## Section 3: Ruby Language Features Beyond Keywords

### 3.1 Blocks and Procs

**Description:** Ruby blocks (`do...end`, `{}`) and Proc objects.

**Transpilation Strategy:**
- Blocks → Rust closures (`|| { }`)
- Procs → boxed closures or function pointers
- Lambdas → strict closures with arity checking

**Feasibility:** ⚠️ **Moderate**

**Example:**
```ruby
# Ruby
[1, 2, 3].map { |x| x * 2 }

my_proc = Proc.new { |x| puts x }
my_proc.call(5)
```

```rust
// Rust
vec![1, 2, 3].iter().map(|x| x * 2).collect();

let my_proc = Box::new(|x: i64| println!("{}", x));
my_proc(5);
```

**Challenges:**
- Ruby blocks can access/modify outer variables (closures capture)
- `break`, `return`, `next` in blocks have special semantics
- Block vs Proc vs Lambda differences

---

### 3.2 Metaprogramming

**Description:** `define_method`, `method_missing`, `class_eval`, `send`

**Transpilation Feasibility:** 🔴 **Requires Extensive Runtime** (mostly impossible)

**Why Hard:**
- These features modify code at runtime
- `method_missing` intercepts undefined method calls
- `define_method` creates methods dynamically
- `class_eval` executes code in class context
- Requires full reflection and dynamic dispatch

**Examples:**

#### `define_method`
```ruby
# Ruby
class User
  [:name, :email].each do |attr|
    define_method(attr) { instance_variable_get("@#{attr}") }
    define_method("#{attr}=") { |val| instance_variable_set("@#{attr}", val) }
  end
end
```

**Transpilation:** Could be statically analyzed and unrolled, but requires sophisticated compiler.

#### `method_missing`
```ruby
# Ruby
class OpenStruct
  def method_missing(method, *args)
    if method.to_s.end_with?('=')
      @data[method[0..-2].to_sym] = args.first
    else
      @data[method]
    end
  end
end

obj = OpenStruct.new
obj.name = "Alice"  # Calls method_missing
puts obj.name       # Calls method_missing
```

**Transpilation:** Requires runtime method dispatch table and reflection. **Not practical**.

**Recommendation:** Refactor code to avoid metaprogramming before transpiling.

---

### 3.3 Symbols vs Strings

**Description:** Ruby symbols (`:name`) are immutable, unique identifiers.

**Transpilation Strategy:**
- Symbols → string literals or enum variants
- Symbol table → compile-time constant pool
- Symbol-to-proc (`:to_s.to_proc`) → manual closure

**Feasibility:** ✅ **Easy** (most cases)

**Example:**
```ruby
# Ruby
status = :active
users.map(&:name)  # Symbol to proc
```

```rust
// Rust
let status = "active";  // Or enum: Status::Active

users.iter().map(|u| u.name()).collect();
```

---

### 3.4 Everything is an Object

**Description:** In Ruby, even primitives are objects (`1.class` → Integer).

**Transpilation Strategy:**
- Use `enum Value` to wrap all types
- Primitives → Value::Int, Value::Float, etc.
- Method calls → match on Value variants

**Feasibility:** ⚠️ **Moderate** (enum Value pattern)

**Example:**
```ruby
# Ruby
1.times { puts "Hello" }
5.even?  # => false
```

```rust
// Rust (using Value enum)
enum Value {
    Int(i64),
    Float(f64),
    String(String),
    Bool(bool),
    Nil,
}

impl Value {
    fn times<F>(&self, f: F)
    where
        F: Fn(),
    {
        if let Value::Int(n) = self {
            for _ in 0..*n {
                f();
            }
        }
    }

    fn even(&self) -> Value {
        if let Value::Int(n) = self {
            Value::Bool(n % 2 == 0)
        } else {
            Value::Nil
        }
    }
}

// Usage
Value::Int(1).times(|| println!("Hello"));
Value::Int(5).even();  // => Value::Bool(false)
```

**Trade-off:** Performance cost for boxing/unboxing vs Ruby compatibility.

---

### 3.5 Duck Typing

**Description:** Ruby doesn't check types, only whether methods exist.

**Transpilation Strategy:**
- Use Rust traits for duck typing
- `impl Trait` for generic behavior
- Static dispatch where possible, dynamic (`dyn Trait`) where needed

**Feasibility:** ⚠️ **Moderate**

**Example:**
```ruby
# Ruby (duck typing)
def process(obj)
  obj.quack  # Works for any object with quack method
end

class Duck
  def quack
    "Quack!"
  end
end

class Person
  def quack
    "I'm not a duck!"
  end
end

process(Duck.new)    # => "Quack!"
process(Person.new)  # => "I'm not a duck!"
```

```rust
// Rust (trait-based)
trait Quackable {
    fn quack(&self) -> &str;
}

fn process<T: Quackable>(obj: &T) {
    println!("{}", obj.quack());
}

struct Duck;
impl Quackable for Duck {
    fn quack(&self) -> &str {
        "Quack!"
    }
}

struct Person;
impl Quackable for Person {
    fn quack(&self) -> &str {
        "I'm not a duck!"
    }
}

fn main() {
    process(&Duck);    // => "Quack!"
    process(&Person);  // => "I'm not a duck!"
}
```

**Challenge:** Requires type inference or annotations during transpilation.

---

### 3.6 Modules and Mixins

**Description:** Ruby modules can be `include`d (instance methods) or `extend`ed (class methods).

**Transpilation Strategy:**
- Modules → Rust traits
- `include` → implement trait for type
- `extend` → implement trait for type itself (associated functions)
- Multiple mixins → multiple trait bounds

**Feasibility:** ⚠️ **Moderate**

**Example:**
```ruby
# Ruby
module Greetable
  def greet
    "Hello, #{name}"
  end
end

module Identifiable
  def id
    @id
  end
end

class User
  include Greetable
  include Identifiable

  attr_reader :name

  def initialize(id, name)
    @id = id
    @name = name
  end
end
```

```rust
// Rust
trait Greetable {
    fn name(&self) -> &str;

    fn greet(&self) -> String {
        format!("Hello, {}", self.name())
    }
}

trait Identifiable {
    fn id(&self) -> i64;
}

struct User {
    id_field: i64,
    name_field: String,
}

impl Greetable for User {
    fn name(&self) -> &str {
        &self.name_field
    }
}

impl Identifiable for User {
    fn id(&self) -> i64 {
        self.id_field
    }
}
```

---

### 3.7 Operators

**Description:** Ruby operators like `<<`, `===`, `=~`, `<=>` have special semantics.

**Transpilation Strategy:**
- `<<` (append) → `push()` method or implement trait
- `===` (case equality) → custom `case_eq()` method
- `=~` (regex match) → regex library
- `<=>` (spaceship) → `Ord` trait

**Feasibility:** ⚠️ **Moderate**

**Examples:**

```ruby
# Ruby
arr = []
arr << 1 << 2  # => [1, 2]

case x
when 1..10
  "in range"  # Uses Range#===
end

"hello" =~ /ll/  # => 2 (match position)

1 <=> 2  # => -1 (comparison)
```

```rust
// Rust
let mut arr = vec![];
arr.push(1);
arr.push(2);  // No chaining in Rust

// case/when handled in match section above

let re = regex::Regex::new(r"ll").unwrap();
re.find("hello").map(|m| m.start());  // => Some(2)

use std::cmp::Ordering;
1.cmp(&2)  // => Ordering::Less
```

---

### 3.8 Open Classes (Monkey Patching)

**Description:** Ruby allows reopening classes to add/modify methods.

**Transpilation Feasibility:** 🔴 **Requires Runtime** (mostly impossible in Rust)

**Why Hard:**
- Rust doesn't allow modifying existing types from external code
- Orphan rule prevents implementing traits on external types
- Would require runtime class table

**Example:**
```ruby
# Ruby
class String
  def shout
    self.upcase + "!"
  end
end

"hello".shout  # => "HELLO!"
```

**Rust:** Not possible without newtype pattern or extension traits (which require wrapping).

**Recommendation:** Refactor to avoid monkey patching before transpiling.

---

### 3.9 Global Variables and Constants

**Description:** `$global`, `CONSTANT`

**Transpilation Strategy:**
- Constants → Rust `const` or `static`
- Global variables → `static mut` (unsafe) or `lazy_static!` / `OnceCell`
- Scoped constants → module-level constants

**Feasibility:** ✅ **Easy** (constants) / ⚠️ **Moderate** (mutable globals)

**Example:**
```ruby
# Ruby
TIMEOUT = 30
$debug_mode = true

def check
  puts "Timeout: #{TIMEOUT}"
  puts "Debug: #{$debug_mode}"
end
```

```rust
// Rust
const TIMEOUT: i32 = 30;

use std::sync::atomic::{AtomicBool, Ordering};
static DEBUG_MODE: AtomicBool = AtomicBool::new(true);

fn check() {
    println!("Timeout: {}", TIMEOUT);
    println!("Debug: {}", DEBUG_MODE.load(Ordering::Relaxed));
}
```

---

### 3.10 Regular Expressions

**Description:** `/pattern/` literal syntax, `=~` operator.

**Transpilation Strategy:**
- Use `regex` crate in Rust
- Literal regex → `Regex::new(r"pattern")`
- Match operator → `.is_match()` or `.find()`

**Feasibility:** ✅ **Easy**

**Example:**
```ruby
# Ruby
if "hello" =~ /ll/
  puts "Match found"
end

"test@example.com" =~ /(\w+)@(\w+)\.(\w+)/
domain = $2  # Capture group
```

```rust
// Rust
use regex::Regex;

let re = Regex::new(r"ll").unwrap();
if re.is_match("hello") {
    println!("Match found");
}

let email_re = Regex::new(r"(\w+)@(\w+)\.(\w+)").unwrap();
if let Some(caps) = email_re.captures("test@example.com") {
    let domain = &caps[2];  // Capture group
}
```

---

### 3.11 String Interpolation

**Description:** `"Hello, #{name}"`

**Transpilation Strategy:**
- Map to `format!()` macro in Rust
- Parse interpolation expressions
- Simple and direct

**Feasibility:** ✅ **Easy**

**Example:**
```ruby
# Ruby
name = "Alice"
puts "Hello, #{name}! You are #{age} years old."
```

```rust
// Rust
let name = "Alice";
println!("Hello, {}! You are {} years old.", name, age);
// Or: format!("Hello, {}! You are {} years old.", name, age)
```

---

### 3.12 Ranges

**Description:** `1..10` (exclusive end), `1...10` (inclusive end).

**Transpilation Strategy:**
- Map to Rust ranges: `1..10`, `1..=10`
- Note: Ruby's `..` is inclusive, Rust's `..` is exclusive
- **Careful:** Ruby `1..10` includes 10, Rust `1..10` excludes 10

**Feasibility:** ✅ **Easy** (watch for off-by-one!)

**Example:**
```ruby
# Ruby
(1..5).each { |n| puts n }   # 1, 2, 3, 4, 5
(1...5).each { |n| puts n }  # 1, 2, 3, 4
```

```rust
// Rust
for n in 1..=5 {  // Inclusive (1..5 is exclusive!)
    println!("{}", n);
}

for n in 1..5 {  // Exclusive
    println!("{}", n);
}
```

**Important:** Ruby `..` → Rust `..=`, Ruby `...` → Rust `..`

---

### 3.13 Splat Operators

**Description:** `*args` (array splat), `**kwargs` (hash splat).

**Transpilation Strategy:**
- `*args` → variadic parameters or `Vec<T>`
- `**kwargs` → `HashMap<String, Value>` or struct
- Requires runtime support for dynamic dispatch

**Feasibility:** ⚠️ **Moderate** (simple cases) / ❌ **Hard** (complex cases)

**Example:**
```ruby
# Ruby
def greet(greeting, *names)
  names.each { |n| puts "#{greeting}, #{n}" }
end

greet("Hello", "Alice", "Bob")

def config(**options)
  puts options[:timeout]
end

config(timeout: 30, retries: 3)
```

```rust
// Rust
fn greet(greeting: &str, names: Vec<&str>) {
    for n in names {
        println!("{}, {}", greeting, n);
    }
}

greet("Hello", vec!["Alice", "Bob"]);

use std::collections::HashMap;

fn config(options: HashMap<String, Value>) {
    if let Some(timeout) = options.get("timeout") {
        println!("{:?}", timeout);
    }
}

let mut opts = HashMap::new();
opts.insert("timeout".to_string(), Value::Int(30));
opts.insert("retries".to_string(), Value::Int(3));
config(opts);
```

---

## Section 4: Summary Recommendation

### Feasibility Table

| Category | Total Features | ✅ Easy | ⚠️ Moderate | ❌ Hard | 🔴 Runtime | % Transpilable |
|----------|---------------|---------|-------------|---------|-----------|----------------|
| **Keywords** | 41 | 20 | 15 | 2 | 4 | 85% (35/41) |
| **Rails DSL** | ~10 patterns | 0 | 0 | 5 | 5 | 0% |
| **Language Features** | ~13 | 4 | 7 | 1 | 1 | 85% (11/13) |
| **Overall** | 64 | 24 (38%) | 22 (34%) | 8 (13%) | 10 (16%) | 72% |

**Legend:**
- ✅ **Easy:** Direct mapping, no special runtime needed
- ⚠️ **Moderate:** Requires runtime support or patterns, but feasible
- ❌ **Hard:** Difficult to transpile, may need restructuring
- 🔴 **Runtime:** Requires extensive runtime reflection/metaprogramming

---

### Category Breakdown

#### 1. Keywords (41 total)

**Easy (20):** `__LINE__`, `__FILE__`, `__ENCODING__`, `and`, `break` (loops), `do`, `else`, `elsif`, `end`, `false`, `for`, `if`, `in`, `next` (loops), `nil`, `not`, `or`, `return`, `self`, `then`, `true`, `unless`, `until`, `when`, `while`

**Moderate (15):** `BEGIN`, `END`, `alias` (static), `begin`, `case`, `class`, `def`, `ensure`, `module`, `rescue`, `super`, `yield`

**Hard (2):** `redo`, `retry`

**Runtime (4):** `defined?`, `alias` (dynamic), `undef`, metaprogramming variants

---

#### 2. Rails DSL (10 patterns analyzed)

**Easy:** None

**Moderate:** None

**Hard (5):** Routing, Controllers, Validations, Scopes, Callbacks

**Runtime (5):** ActiveRecord associations, `has_many`, `belongs_to`, Views, metaprogramming DSLs

**Recommendation:** **Do NOT transpile Rails DSL.** Keep Rails layer in Ruby.

---

#### 3. Language Features (13 analyzed)

**Easy (4):** Symbols (most), String interpolation, Ranges, Regular expressions

**Moderate (7):** Blocks/Procs, Everything is object (Value enum), Duck typing (traits), Modules/Mixins, Operators, Global variables, Splat operators (simple)

**Hard (1):** Open classes (monkey patching)

**Runtime (1):** Metaprogramming (`method_missing`, `define_method`, `class_eval`)

---

## Section 5: Recommended Transpilation Scope

### Phase 1: What to Transpile FIRST (Highest Value, Easiest)

**Target:** Algorithmic, computation-heavy Ruby code without Rails dependencies.

**Good Candidates:**
1. **Data processing scripts**
   - CSV/JSON parsers
   - ETL pipelines
   - Report generators

2. **Background jobs (non-Rails)**
   - Image resizing
   - Video encoding
   - Batch calculations

3. **Business logic services**
   - Pricing calculators
   - Tax computations
   - Data validators (pure logic, no AR validations)

4. **Utility libraries**
   - String formatters
   - Date/time helpers
   - Math libraries

**Why These:**
- ✅ Use core Ruby features (loops, conditionals, methods)
- ✅ No metaprogramming
- ✅ No Rails dependencies
- ✅ Clear inputs/outputs
- ✅ Easy to test
- ✅ High performance gain potential (30x speedup)

**Example:**
```ruby
# GOOD: Transpile this
class PriceCalculator
  def calculate(base_price, quantity, discount)
    subtotal = base_price * quantity
    discount_amount = subtotal * discount
    subtotal - discount_amount
  end
end
```

---

### Phase 2: What to Add NEXT (Medium Difficulty)

**Target:** Ruby code with moderate complexity, some object-oriented patterns.

**Good Candidates:**
1. **Simple Ruby classes**
   - POJOs (Plain Old Ruby Objects)
   - Value objects
   - Service objects

2. **API clients (non-Rails)**
   - HTTP wrappers
   - SDK implementations
   - Data mappers

3. **Algorithms**
   - Sorting, searching
   - Graph traversal
   - Pattern matching

4. **Parsers**
   - Custom DSL parsers
   - Configuration readers
   - Protocol handlers

**Why These:**
- ⚠️ Require `class`, `module`, inheritance
- ⚠️ May use blocks/procs
- ⚠️ Simple mixins acceptable
- ✅ Still no metaprogramming
- ✅ Clear boundaries

**Example:**
```ruby
# ACCEPTABLE: Can transpile with moderate effort
module Discountable
  def apply_discount(amount)
    amount * 0.9
  end
end

class Product
  include Discountable

  attr_reader :price

  def initialize(price)
    @price = price
  end

  def final_price
    apply_discount(@price)
  end
end
```

---

### Phase 3: NEVER Transpile (Stay Ruby-Only)

**Target:** Ruby code that depends on dynamic features or Rails.

**Never Transpile:**
1. **Rails components**
   - ActiveRecord models (keep in Ruby)
   - Controllers (keep in Ruby)
   - Views (keep in Ruby)
   - Routes (keep in Ruby)
   - Migrations (keep in Ruby)

2. **Metaprogramming-heavy code**
   - DSLs using `method_missing`
   - Dynamic method generation (`define_method`)
   - `class_eval`, `instance_eval`
   - Monkey patching

3. **Code using gems with C extensions**
   - Native gems (unless Rust equivalent exists)
   - Complex gems like RMagick, Nokogiri

4. **Scripts requiring REPL/IRB**
   - Interactive debugging
   - Pry sessions
   - Dynamic exploration

**Why NOT:**
- 🔴 Requires extensive runtime support
- 🔴 Metaprogramming is Ruby's strength, Rust's weakness
- 🔴 Rails magic would be lost in translation
- 🔴 Maintenance nightmare
- 🔴 Little performance gain (Rails is already I/O bound)

**Alternative:** Keep these in Ruby, call transpiled Rust code for heavy lifting.

**Example:**
```ruby
# BAD: Do NOT transpile this
class User < ApplicationRecord
  has_many :posts
  validates :email, presence: true

  def method_missing(method, *args)
    # Dynamic attribute handling
  end
end

# INSTEAD: Transpile the business logic it calls
class User < ApplicationRecord
  has_many :posts
  validates :email, presence: true

  def calculate_reputation
    # Call Rust-transpiled function
    RustLib.calculate_reputation(self.posts.pluck(:score))
  end
end
```

---

## Recommended Architecture: Hybrid Approach

### Development Workflow

```
┌─────────────────────────────────────────┐
│         Ruby Layer (Stay Ruby)          │
│                                         │
│  • Rails (models, controllers, views)  │
│  • ActiveRecord                         │
│  • Routing, middleware                  │
│  • Validations, callbacks               │
│  • DSLs, metaprogramming                │
└─────────────────────────────────────────┘
                   ↓ calls
┌─────────────────────────────────────────┐
│    Rust Layer (Transpiled for Speed)    │
│                                         │
│  • Business logic                       │
│  • Data processing                      │
│  • Algorithms                           │
│  • Calculations                         │
│  • Background jobs                      │
└─────────────────────────────────────────┘
```

### Example Integration

```ruby
# app/models/user.rb (STAY RUBY)
class User < ApplicationRecord
  has_many :orders

  def lifetime_value
    # Call Rust-transpiled function for heavy calculation
    RustCalculator.lifetime_value(
      orders.pluck(:total, :created_at)
    )
  end
end

# app/services/pricing_service.rb (TRANSPILE TO RUST)
class PricingService
  def self.calculate(items, discounts)
    total = 0
    items.each do |item|
      price = item[:price] * item[:quantity]
      discount = discounts[item[:category]] || 0
      total += price * (1 - discount)
    end
    total
  end
end

# After transpilation:
# lib/rust_calculator.so (Rust library)
```

---

## Transpilation Guidelines

### DO Transpile:
- ✅ Pure functions (no side effects)
- ✅ Algorithmic code (loops, conditionals)
- ✅ Data transformations
- ✅ Math-heavy computations
- ✅ String/array processing
- ✅ CPU-bound tasks
- ✅ Code with clear inputs/outputs
- ✅ Self-contained classes

### DON'T Transpile:
- ❌ Rails framework code
- ❌ ActiveRecord models
- ❌ Metaprogramming
- ❌ `method_missing`, `define_method`
- ❌ Monkey patches
- ❌ DSLs (RSpec, FactoryBot, etc.)
- ❌ Code using many gems
- ❌ I/O-bound code (network, database)

---

## Expected Performance Gains

### High Gain (10-50x):
- Tight loops (numerical computation)
- String processing
- Array/hash operations
- Recursive algorithms
- Data parsing

### Medium Gain (3-10x):
- Object creation/destruction
- Method calls
- Business logic
- Data validation (pure logic)

### Low Gain (<3x):
- I/O operations (database, network)
- Rails request/response cycle
- Template rendering

**Target scenarios for transpilation:** High and Medium gain categories.

---

## Conclusion

**Ruby-to-Rust transpilation is feasible for a subset of Ruby:**

1. **72% of analyzed features** can be transpiled (Easy + Moderate)
2. **Core Ruby keywords** (85%) transpile well
3. **Rails DSL** (0%) should stay in Ruby
4. **Language features** (85%) are mostly transpilable

**Recommended Strategy:**
- ✅ Transpile: CPU-heavy business logic, algorithms, data processing
- ❌ Don't transpile: Rails framework, metaprogramming, DSLs
- 🎯 Target: 30x speedup on transpiled code
- 🏗️ Architecture: Hybrid (Ruby for web, Rust for computation)

**This aligns with the "Develop in Ruby, Deploy in Rust" thesis:**
- Keep the Ruby development experience
- Deploy performance-critical paths in Rust
- Gradual, incremental adoption
- Clear boundaries between layers

---

**End of Analysis**

*Total Lines: 1,800+*
*Date: 2026-02-03*
