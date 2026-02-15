# Concrete Transpilation Example

## Date: 2026-02-04

## Ruby-- Input (PresenceValidator from Rails)

This is a real example from Rails that IS transpilable:

```ruby
class PresenceValidator < EachValidator
  def validate_each(record, attr_name, value)
    record.errors.add(attr_name, :blank, **options) if value.blank?
  end
end
```

## Rust Output (using RubyValue enum strategy)

```rust
use ruby_runtime::prelude::*;

struct PresenceValidator {
    _super: EachValidator,
    options: RubyValue,
}

impl PresenceValidator {
    fn validate_each(
        &self,
        record: RubyValue,
        attr_name: RubyValue,
        value: RubyValue,
    ) -> RubyValue {
        // value.blank?
        if value.send("blank?", &[]).truthy() {
            // record.errors.add(attr_name, :blank, **options)
            let errors = record.send("errors", &[]);
            let args = vec![attr_name, RubyValue::Symbol("blank".into())];
            errors.send_with_kwargs("add", &args, &self.options);
        }
        RubyValue::Nil
    }
}
```

## The Required Runtime Library

```rust
use std::cell::RefCell;
use std::collections::HashMap;
use std::rc::Rc;

/// The core Ruby value type - everything in Ruby is a RubyValue
#[derive(Clone, Debug)]
pub enum RubyValue {
    Nil,
    Bool(bool),
    Int(i64),
    Float(f64),
    String(Rc<RefCell<String>>),
    Symbol(Rc<str>),
    Array(Rc<RefCell<Vec<RubyValue>>>),
    Hash(Rc<RefCell<HashMap<RubyValue, RubyValue>>>),
    Object(Rc<RefCell<dyn RubyObject>>),
}

impl RubyValue {
    /// Runtime method dispatch - the heart of Ruby semantics
    pub fn send(&self, method: &str, args: &[RubyValue]) -> RubyValue {
        match self {
            RubyValue::Object(obj) => obj.borrow().dispatch(method, args),
            RubyValue::String(s) => string_dispatch(s, method, args),
            RubyValue::Array(a) => array_dispatch(a, method, args),
            RubyValue::Hash(h) => hash_dispatch(h, method, args),
            RubyValue::Int(i) => int_dispatch(*i, method, args),
            RubyValue::Float(f) => float_dispatch(*f, method, args),
            RubyValue::Bool(b) => bool_dispatch(*b, method, args),
            RubyValue::Symbol(s) => symbol_dispatch(s, method, args),
            RubyValue::Nil => nil_dispatch(method, args),
        }
    }

    /// Send with keyword arguments
    pub fn send_with_kwargs(
        &self,
        method: &str,
        args: &[RubyValue],
        kwargs: &RubyValue,
    ) -> RubyValue {
        // Implementation would merge kwargs into dispatch
        self.send(method, args) // Simplified
    }

    /// Ruby truthiness: only false and nil are falsy
    pub fn truthy(&self) -> bool {
        !matches!(self, RubyValue::Nil | RubyValue::Bool(false))
    }

    /// Convert to string representation
    pub fn to_s(&self) -> String {
        match self {
            RubyValue::Nil => "".to_string(),
            RubyValue::Bool(b) => b.to_string(),
            RubyValue::Int(i) => i.to_string(),
            RubyValue::Float(f) => f.to_string(),
            RubyValue::String(s) => s.borrow().clone(),
            RubyValue::Symbol(s) => s.to_string(),
            RubyValue::Array(a) => format!("{:?}", a.borrow()),
            RubyValue::Hash(h) => format!("{:?}", h.borrow()),
            RubyValue::Object(o) => o.borrow().to_s(),
        }
    }
}

/// Trait for Ruby objects
pub trait RubyObject {
    fn dispatch(&self, method: &str, args: &[RubyValue]) -> RubyValue;
    fn to_s(&self) -> String;
}

// Dispatch implementations for built-in types
fn string_dispatch(s: &Rc<RefCell<String>>, method: &str, args: &[RubyValue]) -> RubyValue {
    match method {
        "blank?" => RubyValue::Bool(s.borrow().trim().is_empty()),
        "length" => RubyValue::Int(s.borrow().len() as i64),
        "upcase" => RubyValue::String(Rc::new(RefCell::new(s.borrow().to_uppercase()))),
        "downcase" => RubyValue::String(Rc::new(RefCell::new(s.borrow().to_lowercase()))),
        // ... more methods
        _ => RubyValue::Nil, // method_missing behavior
    }
}

fn array_dispatch(a: &Rc<RefCell<Vec<RubyValue>>>, method: &str, args: &[RubyValue]) -> RubyValue {
    match method {
        "blank?" => RubyValue::Bool(a.borrow().is_empty()),
        "length" => RubyValue::Int(a.borrow().len() as i64),
        "first" => a.borrow().first().cloned().unwrap_or(RubyValue::Nil),
        "last" => a.borrow().last().cloned().unwrap_or(RubyValue::Nil),
        // ... more methods
        _ => RubyValue::Nil,
    }
}

// ... similar dispatch functions for other types
```

## The Brutal Truth

The `send()` in the Rust output **IS `method_missing` by another name**.

You're not eliminating dynamic dispatch. You're IMPLEMENTING it in Rust instead of Ruby.

### Performance Implications

| Approach | Speedup vs YARV | Why |
|----------|-----------------|-----|
| RubyValue enum dispatch | ~2-5x | Still runtime dispatch, but Rust is faster |
| Static types (no enum) | ~50-100x | Direct function calls, no dispatch |
| Crystal approach | ~50-100x | Type inference enables static dispatch |

### For TRUE Rust Performance, You Need:

1. **Static types** (no RubyValue enum)
2. **Direct method calls** (no dispatch tables)
3. **Ownership semantics** (no `Rc<RefCell<>>`)

That requires **TYPE ANNOTATIONS** or **TYPE INFERENCE** - which is exactly what Crystal does.

## A More Optimized Approach (Future Work)

If you want Rust performance, you need to infer or annotate types:

```ruby
# Ruby-- with type hints (hypothetical)
class PresenceValidator < EachValidator
  # @param record [Record]
  # @param attr_name [Symbol]
  # @param value [String]
  def validate_each(record, attr_name, value)
    record.errors.add(attr_name, :blank, **options) if value.blank?
  end
end
```

Could transpile to:

```rust
// Optimized Rust with known types
struct PresenceValidator {
    options: ValidatorOptions,
}

impl PresenceValidator {
    fn validate_each(
        &self,
        record: &mut Record,
        attr_name: &str,
        value: &str,
    ) {
        if value.is_empty() || value.trim().is_empty() {
            record.errors.add(attr_name, "blank", &self.options);
        }
    }
}
```

This is **much faster** because:
- No enum wrapping/unwrapping
- Direct method calls
- No runtime dispatch
- Compiler can inline everything
