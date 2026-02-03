# Ruby-- Transpilable Subset Definition

## Date: 2026-02-04

## Definition

**Ruby--** (Ruby minus metaprogramming) is a subset of Ruby that can be statically transpiled to Rust.

A Ruby file is TRANSPILABLE if and only if it contains ZERO instances of the forbidden patterns.

## Forbidden Patterns (Compile-Time Detectable)

These patterns CANNOT be transpiled because they require runtime code generation or introspection:

| Pattern | Why Forbidden |
|---------|---------------|
| `method_missing` | Runtime method dispatch |
| `respond_to_missing?` | Runtime introspection support |
| `define_method` | Dynamic method creation |
| `define_singleton_method` | Dynamic singleton method creation |
| `eval` | Runtime code evaluation |
| `class_eval` | Runtime code evaluation in class context |
| `instance_eval` | Runtime code evaluation in instance context |
| `module_eval` | Runtime code evaluation in module context |
| `send` | Dynamic method dispatch |
| `public_send` | Dynamic public method dispatch |
| `__send__` | Dynamic method dispatch (bypass override) |
| `const_get` | Dynamic constant lookup |
| `const_set` | Dynamic constant definition |
| `const_missing` | Dynamic constant resolution |
| `included` | Module callback hook |
| `extended` | Module callback hook |
| `prepended` | Module callback hook |
| `inherited` | Class callback hook |
| `method(:name).call` | Runtime method lookup |
| `ObjectSpace` | Runtime object manipulation |
| `binding` | Runtime binding capture |
| `Proc.new` with `binding` | Dynamic scope capture |

## Allowed Patterns (Can Transpile)

These patterns are statically analyzable and can transpile to Rust:

### Class and Module Definitions

```ruby
# ALLOWED
class Foo < Bar
  # ...
end

module Baz
  # ...
end
```

### Method Definitions

```ruby
# ALLOWED
def method_name(arg1, arg2, *args, **kwargs, &block)
  # method body
end

def self.class_method
  # ...
end
```

### Attribute Accessors

```ruby
# ALLOWED
attr_reader :name
attr_writer :age
attr_accessor :email
```

### Control Flow

```ruby
# ALLOWED
if condition
  # ...
elsif other
  # ...
else
  # ...
end

unless condition
  # ...
end

case value
when pattern1
  # ...
when pattern2
  # ...
else
  # ...
end
```

### Loops

```ruby
# ALLOWED
while condition
  # ...
end

until condition
  # ...
end

for item in collection
  # ...
end

# Iterator methods with simple blocks
array.each { |item| process(item) }
array.map { |x| x * 2 }
array.select { |x| x > 5 }
```

### Exception Handling

```ruby
# ALLOWED
begin
  risky_operation
rescue StandardError => e
  handle_error(e)
ensure
  cleanup
end

raise ArgumentError, "message"
```

### Data Structures

```ruby
# ALLOWED
Person = Struct.new(:name, :age)

# Simple hashes and arrays
data = { key: "value", other: 123 }
list = [1, 2, 3, 4, 5]
```

### Simple Blocks (No Binding Capture)

```ruby
# ALLOWED - block doesn't capture complex bindings
items.map { |x| x.to_s }
items.select { |x| x > 0 }
items.reduce(0) { |sum, x| sum + x }
```

## Detection Algorithm

To determine if a Ruby file is transpilable:

```ruby
# Pseudocode for transpilability detection
FORBIDDEN_PATTERNS = [
  :method_missing,
  :respond_to_missing?,
  :define_method,
  :define_singleton_method,
  # ... etc
]

def transpilable?(ast)
  forbidden_nodes = []

  ast.walk do |node|
    case node
    when MethodDefinition
      forbidden_nodes << node if FORBIDDEN_PATTERNS.include?(node.name)
    when MethodCall
      forbidden_nodes << node if FORBIDDEN_PATTERNS.include?(node.method_name)
    when HeredocWithInterpolation
      # Check if used with eval/class_eval/module_eval
      forbidden_nodes << node if eval_context?(node)
    end
  end

  forbidden_nodes.empty?
end
```

## Transpilation Rules

### Classes → Rust Structs

```ruby
# Ruby--
class Person
  attr_accessor :name, :age

  def initialize(name, age)
    @name = name
    @age = age
  end

  def greet
    "Hello, #{@name}"
  end
end
```

```rust
// Rust output
use ruby_runtime::prelude::*;

struct Person {
    name: RubyValue,
    age: RubyValue,
}

impl Person {
    fn new(name: RubyValue, age: RubyValue) -> Self {
        Self { name, age }
    }

    fn name(&self) -> RubyValue {
        self.name.clone()
    }

    fn set_name(&mut self, value: RubyValue) {
        self.name = value;
    }

    fn age(&self) -> RubyValue {
        self.age.clone()
    }

    fn set_age(&mut self, value: RubyValue) {
        self.age = value;
    }

    fn greet(&self) -> RubyValue {
        RubyValue::String(format!("Hello, {}", self.name.to_s()))
    }
}
```

### Method Calls → Runtime Dispatch

```ruby
# Ruby--
result = object.method_name(arg1, arg2)
```

```rust
// Rust output
let result = object.send("method_name", &[arg1, arg2]);
```

## Limitations

1. **No Rails Apps**: Rails is foundationally metaprogrammed (ActiveRecord attributes, delegation, callbacks)

2. **No Most Gems**: Idiomatic Ruby gems use metaprogramming extensively

3. **No Dynamic Features**: Any code that relies on Ruby's dynamic nature

4. **Performance**: The `RubyValue` enum approach still requires runtime dispatch, yielding ~2-5x speedup over YARV, not 100x

## Use Cases for Ruby--

1. **New utility libraries** written specifically for transpilation
2. **Simple domain logic** (validators, value objects, calculations)
3. **CLI tools and scripts** without complex dependencies
4. **Gradual migration** of isolated components
5. **Educational purposes** to understand Ruby-to-Rust mapping
