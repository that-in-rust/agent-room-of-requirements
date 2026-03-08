# R60: Iterator Methods and Combinators - Functional Collection Processing

**Answer-First (Minto Pyramid)**

Iterator methods transform collections functionally via method chaining without intermediate allocations. Core methods: iter() borrows elements, into_iter() consumes collection, iter_mut() allows mutation. Combinators: map() transforms elements, filter() selects subset, collect() materializes results. Closures (|x| expr) provide inline functions for transformations. Method chains are lazy—only evaluated when consumed by collect/for/fold. Common patterns: filter().map().collect(), flat_map() for nested iteration, zip() combines iterators. Prefer iterators over indexing for safety and performance (no bounds checks). Iterator trait requires next() returning Option<Item>, enabling zero-cost abstractions.

---

## 1. The Problem: Manual Collection Processing Is Tedious

### 1.1 The Core Challenge

Processing collections with manual loops is verbose and error-prone:

```rust
let numbers = vec![1, 2, 3, 4, 5];

// Get squares of even numbers - manual approach
let mut result = Vec::new();
for n in &numbers {
    if n % 2 == 0 {
        result.push(n * n);
    }
}
// result: [4, 16]
```

Problems:
- **Mutable state** - Requires `mut` and manual push
- **Verbose** - Many lines for simple operation
- **Index errors** - Manual indexing risks bounds violations
- **Not composable** - Hard to chain operations
- **Intent unclear** - Implementation obscures what, not how

### 1.2 What Iterator Methods Provide

```rust
let numbers = vec![1, 2, 3, 4, 5];

// Same operation - iterator approach
let result: Vec<i32> = numbers.iter()
    .filter(|&n| n % 2 == 0)
    .map(|&n| n * n)
    .collect();
// result: [4, 16]
```

Benefits:
- **Declarative** - Expresses intent clearly
- **Composable** - Chain operations fluently
- **Lazy evaluation** - No intermediate allocations
- **Zero-cost** - Optimizes to same code as manual loops
- **Safe** - No bounds checking needed

---

## 2. The Solution: Iterator Trait and Combinators

### 2.1 The Iterator Trait

```rust
pub trait Iterator {
    type Item;
    
    fn next(&mut self) -> Option<Self::Item>;
    
    // 50+ provided methods (map, filter, etc.)
}
```

**Core concept**: Iterator produces sequence of values via `next()`, returning `Some(item)` or `None` when exhausted.

### 2.2 Three Ways to Iterate

```rust
let vec = vec![1, 2, 3];

// 1. iter() - borrow elements (&T)
for n in vec.iter() {
    // n: &i32
}

// 2. into_iter() - consume collection (T)
for n in vec.into_iter() {
    // n: i32
    // vec is moved, can't use after
}

// 3. iter_mut() - mutable borrow (&mut T)
for n in vec.iter_mut() {
    *n += 1;  // Can modify
}
```

### 2.3 Key Combinators

**Transform:**
- `map(f)` - Apply function to each element
- `flat_map(f)` - Map and flatten nested iterators
- `filter_map(f)` - Combined filter + map

**Select:**
- `filter(predicate)` - Keep elements matching condition
- `take(n)` - First n elements
- `skip(n)` - Skip first n elements

**Combine:**
- `zip(other)` - Pair elements from two iterators
- `chain(other)` - Concatenate iterators
- `enumerate()` - Add indices (index, item)

**Consume:**
- `collect()` - Materialize into collection
- `fold(init, f)` - Reduce to single value
- `for_each(f)` - Side effects on each element
- `sum()`, `count()`, `min()`, `max()`

---

## 3. Mental Model: Quantum Realm Navigation

Think of iterators as Ant-Man navigating the Quantum Realm with transformation waypoints:

**The Metaphor:**
- **Iterator** - Navigation path through Quantum Realm
- **Combinators** - Waypoint gates that transform/filter
- **Lazy evaluation** - Path planned but not traveled until needed
- **collect()** - Exiting Quantum Realm with collected items
- **Method chaining** - Sequence of quantum gates

### Metaphor Mapping Table

| Concept | MCU Metaphor | Technical Reality |
|---------|--------------|-------------------|
| Iterator | Quantum navigation path | Sequence producer with next() |
| iter() | Observing particles (no consumption) | Borrowing iterator (&T) |
| into_iter() | Consuming particles (destructive) | Owning iterator (T) |
| map() | Quantum transformation gate | Element-wise function application |
| filter() | Selective quantum tunnel | Predicate-based selection |
| Lazy evaluation | Path exists but not traveled | No computation until consumed |
| collect() | Exit portal materializing items | Gather elements into collection |
| Chain | Sequential quantum gates | Fluent method composition |

### The Quantum Navigation Story

When Ant-Man enters the Quantum Realm, he doesn't immediately visit every particle. Instead, he plans a navigation path (iterator chain) through transformation gates (combinators):

**Path Planning (Lazy)**: Scott plans "enter realm → skip first 10 particles → transform blue particles to red → collect energy signatures." The path exists, but no travel happens yet. Similarly, `iter().skip(10).map(transform).collect()` plans operations but doesn't execute until `collect()` is called.

**Transformation Gates (map/filter)**: Each quantum gate transforms or filters particles. Passing through a "color change" gate (map) transforms every particle. Passing through a "selection" gate (filter) only lets matching particles through. Gates are visited in sequence, processing one particle at a time.

**Zero Copying**: In the Quantum Realm, particles can be observed without disturbing them (iter), or consumed and transformed (into_iter), or modified in place (iter_mut). No particle duplication unless explicitly requested—maximum efficiency.

**Exit Portal (collect)**: Only when Scott triggers the exit portal does the actual journey begin. He travels the planned path, processes each gate, and materializes results in the macro world. Similarly, `collect()` triggers iterator execution, applying all chained operations.

---

## 4. Anatomy: Iterator Trait and Method Types

### 4.1 Iterator Trait Essentials

```rust
pub trait Iterator {
    type Item;  // Type of elements
    
    // Required method
    fn next(&mut self) -> Option<Self::Item>;
    
    // Provided methods (50+)
    fn map<B, F>(self, f: F) -> Map<Self, F>
    where F: FnMut(Self::Item) -> B { ... }
    
    fn filter<P>(self, predicate: P) -> Filter<Self, P>
    where P: FnMut(&Self::Item) -> bool { ... }
    
    // Many more...
}
```

### 4.2 Iterator Adapters vs Consumers

**Adapters** (return new iterator):
```rust
map, filter, take, skip, enumerate, zip, chain
// Lazy - don't do anything until consumed
```

**Consumers** (produce final value):
```rust
collect, fold, for_each, sum, count, any, all
// Execute the iterator chain
```

### 4.3 The Three Iterator Methods

```rust
impl<T> Vec<T> {
    // 1. Shared references
    pub fn iter(&self) -> Iter<'_, T> {
        // Returns iterator over &T
    }
    
    // 2. Mutable references
    pub fn iter_mut(&mut self) -> IterMut<'_, T> {
        // Returns iterator over &mut T
    }
}

// 3. Consuming (via IntoIterator)
impl<T> IntoIterator for Vec<T> {
    type Item = T;
    fn into_iter(self) -> IntoIter<T> {
        // Consumes Vec, returns iterator over T
    }
}
```

---

## 5. Common Patterns

### 5.1 map - Transform Elements

```rust
let numbers = vec![1, 2, 3];
let doubled: Vec<i32> = numbers.iter()
    .map(|x| x * 2)
    .collect();
// [2, 4, 6]

// With type conversion
let strings: Vec<String> = numbers.iter()
    .map(|n| n.to_string())
    .collect();
// ["1", "2", "3"]
```

### 5.2 filter - Select Elements

```rust
let numbers = vec![1, 2, 3, 4, 5];
let evens: Vec<i32> = numbers.iter()
    .filter(|&n| n % 2 == 0)
    .copied()  // or cloned()
    .collect();
// [2, 4]

// Complex predicates
let large_evens: Vec<i32> = numbers.iter()
    .filter(|&&n| n % 2 == 0 && n > 2)
    .copied()
    .collect();
// [4]
```

### 5.3 filter_map - Combined Filter + Map

```rust
let strings = vec!["1", "two", "3", "four"];
let numbers: Vec<i32> = strings.iter()
    .filter_map(|s| s.parse().ok())
    .collect();
// [1, 3]  (parsed successfully, "two" and "four" filtered out)
```

### 5.4 collect - Materialize Results

```rust
let vec: Vec<i32> = (0..5).collect();
let set: HashSet<i32> = (0..5).collect();
let result: Result<Vec<i32>, _> = vec!["1", "2", "3"]
    .iter()
    .map(|s| s.parse::<i32>())
    .collect();
```

### 5.5 Chain Multiple Iterators

```rust
let v1 = vec![1, 2, 3];
let v2 = vec![4, 5, 6];
let combined: Vec<i32> = v1.iter()
    .chain(v2.iter())
    .copied()
    .collect();
// [1, 2, 3, 4, 5, 6]
```

### 5.6 enumerate - Add Indices

```rust
let words = vec!["a", "b", "c"];
for (i, word) in words.iter().enumerate() {
    println!("{}: {}", i, word);
}
// 0: a
// 1: b
// 2: c
```

### 5.7 zip - Combine Iterators

```rust
let names = vec!["Alice", "Bob"];
let ages = vec![30, 25];
let combined: Vec<_> = names.iter()
    .zip(ages.iter())
    .collect();
// [("Alice", 30), ("Bob", 25)]
```

### 5.8 flat_map - Flatten Nested

```rust
let nested = vec![vec![1, 2], vec![3, 4]];
let flat: Vec<i32> = nested.iter()
    .flat_map(|v| v.iter())
    .copied()
    .collect();
// [1, 2, 3, 4]
```

### 5.9 fold - Reduce to Value

```rust
let numbers = vec![1, 2, 3, 4];
let sum = numbers.iter().fold(0, |acc, &x| acc + x);
// 10

let product = numbers.iter().fold(1, |acc, &x| acc * x);
// 24
```

### 5.10 take and skip

```rust
let numbers: Vec<i32> = (0..10).skip(2).take(5).collect();
// [2, 3, 4, 5, 6]
```

---

## 6. Closures

### 6.1 Closure Syntax

```rust
// Basic closure
let add_one = |x| x + 1;

// Multiple arguments
let add = |x, y| x + y;

// Block body
let complex = |x| {
    let doubled = x * 2;
    doubled + 1
};

// Type annotations
let typed = |x: i32| -> i32 { x + 1 };
```

### 6.2 Capturing Environment

```rust
let multiplier = 10;
let multiply = |x| x * multiplier;  // Captures multiplier

let result = multiply(5);  // 50
```

### 6.3 Closure Traits

Three traits based on how they capture:

```rust
// Fn - borrows immutably
let immutable = |x| x + value;

// FnMut - borrows mutably
let mut count = 0;
let mut incrementer = |x| {
    count += 1;
    x + count
};

// FnOnce - takes ownership (can only call once)
let vec = vec![1, 2, 3];
let consumer = move || vec;  // Takes ownership via move
```

---

## 7. Real-World Examples

### 7.1 Data Processing Pipeline

```rust
let users = vec![
    ("Alice", 30),
    ("Bob", 25),
    ("Charlie", 35),
];

let adult_names: Vec<String> = users.iter()
    .filter(|(_, age)| *age >= 18)
    .map(|(name, _)| name.to_string())
    .collect();
```

### 7.2 Parsing with Error Handling

```rust
let inputs = vec!["1", "2", "invalid", "4"];

// Collect successes
let valid: Vec<i32> = inputs.iter()
    .filter_map(|s| s.parse().ok())
    .collect();
// [1, 2, 4]

// Or fail-fast with Result
let all_or_nothing: Result<Vec<i32>, _> = inputs.iter()
    .map(|s| s.parse::<i32>())
    .collect();
// Err because "invalid" fails
```

### 7.3 Grouping and Aggregation

```rust
use std::collections::HashMap;

let scores = vec![
    ("Alice", 90),
    ("Bob", 85),
    ("Alice", 95),
];

let totals: HashMap<&str, i32> = scores.iter()
    .fold(HashMap::new(), |mut acc, (name, score)| {
        *acc.entry(name).or_insert(0) += score;
        acc
    });
// {"Alice": 185, "Bob": 85}
```

### 7.4 Complex Transformations

```rust
let data = vec![
    vec![1, 2, 3],
    vec![4, 5],
    vec![6],
];

let result: Vec<i32> = data.iter()
    .flat_map(|v| v.iter())
    .filter(|&&x| x % 2 == 0)
    .map(|&x| x * x)
    .collect();
// [4, 16, 36]
```

---

## 8. Best Practices

### 8.1 Prefer Iterators Over Indexing

✅ **Iterators:**
```rust
for item in vec.iter() {
    // No bounds checking needed
}
```

❌ **Manual indexing:**
```rust
for i in 0..vec.len() {
    let item = &vec[i];  // Bounds check on every access
}
```

### 8.2 Use iter() vs into_iter() Appropriately

```rust
let vec = vec![1, 2, 3];

// Preserve vec - use iter()
for n in vec.iter() {
    // vec still usable after
}

// Consume vec - use into_iter()
for n in vec.into_iter() {
    // vec moved, can't use after
}
```

### 8.3 Chain Operations Fluently

✅ **Readable:**
```rust
data.iter()
    .filter(|x| x.is_valid())
    .map(|x| x.process())
    .take(10)
    .collect()
```

❌ **Nested:**
```rust
data.iter()
    .take(10)
    .collect::<Vec<_>>()
    .iter()
    .filter(|x| x.is_valid())
    .collect()
```

### 8.4 Avoid Unnecessary collect()

❌ **Wasteful:**
```rust
let intermediate: Vec<_> = data.iter().map(f).collect();
let result: Vec<_> = intermediate.iter().filter(p).collect();
```

✅ **Efficient:**
```rust
let result: Vec<_> = data.iter()
    .map(f)
    .filter(p)
    .collect();
```

---

## 9. Summary

**Iterator methods** enable functional collection processing via lazy, composable operations. **iter()** borrows, **into_iter()** consumes, **iter_mut()** mutates. **Combinators** like map/filter/collect chain operations declaratively. **Closures** provide inline functions for transformations. Iterator chains are **lazy**—no work until consumed by collect/fold/for_each. Prefer iterators over manual indexing for safety (no bounds checks) and clarity (expresses intent). Master common patterns: filter().map().collect() for transformations, flat_map() for nested data, fold() for aggregation. Iterator trait's 50+ methods provide zero-cost abstractions for expressive, efficient collection processing.
