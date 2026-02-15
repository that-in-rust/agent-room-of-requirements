# Parseltongue Analysis: Rails Codebase Transpilability

## Date: 2026-02-04

## Analysis Methodology

Used parseltongue v1.4.7 to analyze the Rails framework codebase:
- Ingested `rails-framework/` directory
- 3,416 files processed
- 113,803 CODE entities created
- 158,170 dependency edges mapped

## Quantitative Findings

### Total Codebase Statistics

| Metric | Value |
|--------|-------|
| Code entities | 55,603 |
| Test entities | 0 (excluded for LLM context) |
| Dependency edges | 158,170 |
| Languages detected | JavaScript, Ruby |

### Transpilability Breakdown

| Category | Count | Percentage | Examples |
|----------|-------|------------|----------|
| TRANSPILABLE | 10,464 | 87.5% | class, def, initialize, Struct |
| HARD (closures) | 651 | 5.4% | proc, lambda, yield, block_given |
| IMPOSSIBLE | 848 | 7.1% | method_missing, eval, define_method |

### Detailed Pattern Counts

#### Impossible to Transpile (requires Ruby runtime)

| Pattern | Count | Description |
|---------|-------|-------------|
| method_missing | 67 | Runtime dispatch |
| define_method | 10 | Dynamic method creation |
| class_eval | 6 | Runtime code evaluation |
| instance_eval | 4 | Runtime code evaluation |
| module_eval | 1 | Runtime code evaluation |
| eval | 59 | Runtime code evaluation |
| send | 148 | Dynamic dispatch |
| public_send | 1 | Dynamic dispatch |
| respond_to | 216 | Runtime introspection |
| const_get | 1 | Dynamic constant lookup |
| const_set | 1 | Dynamic constant definition |
| included | 78 | Module callback hooks |
| inherited | 92 | Class callback hooks |
| prepend | 75 | Module prepending |
| extend | 88 | Runtime module extension |
| alias_method | 1 | Method aliasing |
| **TOTAL** | **848** | |

#### Hard but Possible (needs closure/callback runtime support)

| Pattern | Count | Description |
|---------|-------|-------------|
| proc | 367 | Closures |
| lambda | 40 | Closures |
| yield | 55 | Block invocation |
| block_given | 5 | Block detection |
| delegate | 88 | Delegation pattern |
| concern | 96 | Rails concerns |
| **TOTAL** | **651** | |

#### Transpilable (static patterns)

| Pattern | Count | Description |
|---------|-------|-------------|
| initialize | 984 | Constructors |
| attr_accessor | 9 | Attribute accessors |
| Struct | 446 | Data structures |
| class | 6,631 | Class definitions |
| module | 379 | Module definitions |
| def | 2,015 | Method definitions |
| **TOTAL** | **10,464** | |

## Critical Insight: Location of Metaprogramming

The 7.1% "impossible" entities are NOT randomly distributed:

### method_missing by Rails Component

| Component | Count | What It Controls |
|-----------|-------|------------------|
| activesupport | 18 | Core utilities, delegation, time |
| activerecord | 18 | ALL ATTRIBUTE ACCESS (user.name, etc) |
| actionpack | 10 | Controllers, routing, MIME types |
| railties | 9 | Framework boot, configuration |
| activemodel | 4 | Model validations, callbacks |
| actionview | 3 | View helpers, templates |
| actionmailer | 2 | Email handling |
| tools | 1 | Rails inspector |

**THE 7.1% IS THE FOUNDATION, NOT THE PERIPHERY**

## Code Examples

### Example 1: ActiveRecord method_missing (UNTRANSPILABLE)

```ruby
def method_missing(name, ...)
  # We can't know whether some method was defined or not because
  # multiple thread might be concurrently be in this code path.
  # So the first one would define the methods and the others would
  # appear to already have them.
  self.class.define_attribute_methods

  # So in all cases we must behave as if the method was just defined.
  method = begin
    self.class.public_instance_method(name)
  rescue NameError
    nil
  end

  # The method might be explicitly defined in the model, but call a generated
  # method with super. So we must resume the call chain at the right step.
  method = method.super_method while method && !method.owner.is_a?(GeneratedAttributeMethods)
  if method
    method.bind_call(self, ...)
  else
    super
  end
end
```

**Why untranspilable:** Uses `define_attribute_methods` (generates methods at runtime), `public_instance_method` (runtime introspection), `super_method` (dynamic method chain), `bind_call` (runtime binding).

### Example 2: ActiveSupport Delegation (UNTRANSPILABLE)

```ruby
def generate_method_missing(owner, target, allow_nil: nil)
  target = target.to_s
  target = "self.#{target}" if RESERVED_METHOD_NAMES.include?(target) || target == "__target"

  nil_behavior = if allow_nil
    "nil"
  else
    "::Kernel.raise ::ActiveSupport::DelegationError.nil_target(method, :'#{target}')"
  end

  owner.module_eval <<~RUBY, __FILE__, __LINE__ + 1
    def respond_to_missing?(name, include_private = false)
      return false if name == :marshal_dump || name == :_dump
      #{target}.respond_to?(name) || super
    end

    def method_missing(method, ...)
      __target = #{target}
      if __target.nil? && !nil.respond_to?(method)
        #{nil_behavior}
      elsif __target.respond_to?(method)
        __target.public_send(method, ...)
      else
        super
      end
    end
  RUBY
end
```

**Why untranspilable:** Uses `module_eval <<~RUBY` with string interpolation (`#{target}`) to GENERATE CODE FROM STRINGS at runtime.

### Example 3: PresenceValidator (TRANSPILABLE)

```ruby
class PresenceValidator < EachValidator
  def validate_each(record, attr_name, value)
    record.errors.add(attr_name, :blank, **options) if value.blank?
  end
end
```

**Why transpilable:** Simple class inheritance, single method, conditional logic, method calls - all statically analyzable.

## Circular Dependencies

```json
{
  "has_cycles": false,
  "cycle_count": 0,
  "cycles": []
}
```

No circular dependencies detected in the Rails codebase.
