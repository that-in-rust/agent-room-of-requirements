# R65: `Index` and `IndexMut` Traits - Custom Indexing Syntax

## Problem: Custom Types Need Array-Like `[]` Access

**ANSWER UPFRONT**: `Index<Idx>` trait enables `container[index]` syntax for immutable access. `IndexMut<Idx>` enables `container[index] = value` for mutable access. Both use generic index type `Idx` and associated type `Output`. Index panics on invalid access (not `Option`).

**What's Wrong**: `TicketStore::get(id)` requires method call syntax. Want `store[id]` like arrays/vectors. Need trait to tell compiler what `[]` means for custom type.

**The Solution**: Implement `Index<TicketId>` to enable `&store[id]` (immutable). Implement `IndexMut<TicketId>` to enable `store[id] = ticket` (mutable). Compiler translates `[]` to `index()` or `index_mut()` method calls.

**Why It Matters**: Enables intuitive ergonomic APIs matching built-in collection types. Operator overloading for subscript syntax. `IndexMut` requires `Index` (supertra it), ensuring consistent behavior.

---

## MCU Metaphor: Tesseract Portal Access Protocol

**The Story**: The Tesseract creates portals to specific coordinates. `Index` = portal viewing (read-only), `IndexMut` = portal manipulation (read-write). Index type = coordinates, Output = what's at that location.

**The Mapping**:

| Rust Concept | MCU Equivalent | How It Works |
|--------------|----------------|--------------|
| `Index` trait | Tesseract viewing portal | Look through portal at coordinates (read-only) |
| `IndexMut` trait | Tesseract manipulation portal | Reach through portal to modify (read-write) |
| `Idx` generic parameter | Portal coordinates | usize, TicketId, Range—different coordinate systems |
| `Output` associated type | What's at destination | Type of entity at those coordinates |
| `container[index]` syntax | Portal activation | Compiler opens portal using coordinates |
| Panics on invalid index | Invalid coordinates | Portal to nonexistent location fails |
| Supertrait requirement | Viewing before manipulation | Must establish viewing portal before manipulation |
| Multiple Idx implementations | Multi-dimensional portals | Different coordinate systems for same container |
| Reference return | Portal view, not teleportation | Return reference, not owned value |

**The Insight**: Just as the Tesseract opens portals to different coordinates (index types) revealing what's at that location (Output type), Rust's `Index` traits enable `[]` syntax for custom containers—with viewing portals (Index) required before manipulation portals (IndexMut), ensuring type-safe ergonomic access to contained data.

---

## Anatomy of `Index` and `IndexMut`

### The `Index` Trait (Immutable Access)

```rust
pub trait Index<Idx> {
    type Output;  // What type is returned
    
    fn index(&self, index: Idx) -> &Self::Output;
}
```

**Components**:
- **Generic parameter `Idx`**: Type of the index (usize, TicketId, Range, etc.)
- **Associated type `Output`**: Type being accessed
- **Returns reference**: `&Self::Output` (not owned value)

### The `IndexMut` Trait (Mutable Access)

```rust
pub trait IndexMut<Idx>: Index<Idx> {  // Supertrait: requires Index
    fn index_mut(&mut self, index: Idx) -> &mut Self::Output;
}
```

**Key points**:
- **Supertrait bound**: Must implement `Index<Idx>` first
- **Returns mutable reference**: `&mut Self::Output`
- **Consistent behavior**: Both use same `Idx` and `Output`

---

## Basic Examples

### Vec Indexing (Built-in)

```rust
let v = vec![10, 20, 30];

// Immutable indexing (uses Index<usize>)
let first: &i32 = &v[0];  // Compiler: v.index(0)
assert_eq!(*first, 10);

// Mutable indexing (uses IndexMut<usize>)
let mut v = vec![10, 20, 30];
v[1] = 99;  // Compiler: *v.index_mut(1) = 99
assert_eq!(v[1], 99);
```

### Custom Type: TicketStore

```rust
use std::collections::HashMap;

struct TicketStore {
    tickets: HashMap<TicketId, Ticket>,
}

#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash)]
struct TicketId(u64);

struct Ticket {
    title: String,
    description: String,
}

// Implement Index for immutable access
impl Index<TicketId> for TicketStore {
    type Output = Ticket;
    
    fn index(&self, id: TicketId) -> &Ticket {
        self.tickets.get(&id)
            .expect("Ticket not found")  // Panics if missing
    }
}

// Implement IndexMut for mutable access
impl IndexMut<TicketId> for TicketStore {
    fn index_mut(&mut self, id: TicketId) -> &mut Ticket {
        self.tickets.get_mut(&id)
            .expect("Ticket not found")
    }
}

// Usage
let mut store = TicketStore::new();
let id = store.add_ticket(/* ... */);

// Immutable access with []
let ticket: &Ticket = &store[id];
println!("{}", ticket.title);

// Mutable access with []
store[id].title = "Updated".to_string();
```

**Desugaring**:
```rust
// store[id]         → store.index(id)
// store[id] = value → *store.index_mut(id) = value
```

---

## Multiple Index Types

Types can implement `Index<Idx>` for multiple `Idx` types:

```rust
struct Grid {
    data: Vec<i32>,
    width: usize,
    height: usize,
}

// Index by single usize (linear)
impl Index<usize> for Grid {
    type Output = i32;
    
    fn index(&self, index: usize) -> &i32 {
        &self.data[index]
    }
}

// Index by (usize, usize) tuple (2D coordinates)
impl Index<(usize, usize)> for Grid {
    type Output = i32;
    
    fn index(&self, (x, y): (usize, usize)) -> &i32 {
        assert!(x < self.width && y < self.height);
        &self.data[y * self.width + x]
    }
}

// Usage
let grid = Grid::new(3, 3, vec![1, 2, 3, 4, 5, 6, 7, 8, 9]);

let linear: &i32 = &grid[4];      // Uses Index<usize>
let coord: &i32 = &grid[(1, 1)];  // Uses Index<(usize, usize)>
assert_eq!(*linear, 5);
assert_eq!(*coord, 5);
```

**Why multiple implementations?** Different access patterns for same data (linear vs 2D).

---

## Range Indexing (Slicing)

Vec implements `Index<Range<usize>>` for slicing:

```rust
use std::ops::Range;

let v = vec![0, 1, 2, 3, 4];

// Range indexing returns slice
let slice: &[i32] = &v[1..4];  // [1, 2, 3]
assert_eq!(slice, &[1, 2, 3]);

// Different Output type!
// Index<usize> has Output = i32
// Index<Range<usize>> has Output = [i32] (slice DST)
```

**Custom range indexing**:

```rust
use std::ops::Range;

impl Index<Range<usize>> for Grid {
    type Output = [i32];  // Returns slice
    
    fn index(&self, range: Range<usize>) -> &[i32] {
        &self.data[range]
    }
}

// Usage
let grid = Grid::new(3, 3, vec![1, 2, 3, 4, 5, 6, 7, 8, 9]);
let slice: &[i32] = &grid[1..4];  // [2, 3, 4]
```

---

## Panics vs Option: Design Decision

### Index Panics on Invalid Access

```rust
let v = vec![1, 2, 3];
let x = &v[10];  // PANICS at runtime
```

**Why?** Matches array/Vec behavior, cleaner syntax for expected-valid access.

### Use `.get()` for Fallible Access

```rust
let v = vec![1, 2, 3];

// Safe access with Option
if let Some(x) = v.get(10) {
    println!("{}", x);
} else {
    println!("Index out of bounds");
}
```

**Guideline**: 
- Use `[]` when index SHOULD be valid (panic = programming error)
- Use `.get()` when validity is uncertain

### Custom Type Example

```rust
impl TicketStore {
    // Fallible access: returns Option
    pub fn get(&self, id: TicketId) -> Option<&Ticket> {
        self.tickets.get(&id)
    }
}

impl Index<TicketId> for TicketStore {
    type Output = Ticket;
    
    // Infallible syntax: panics if missing
    fn index(&self, id: TicketId) -> &Ticket {
        self.get(id).expect("Ticket not found")
    }
}

// Usage
let store = TicketStore::new();
let id = TicketId(1);

// Safe check
if let Some(ticket) = store.get(id) {
    println!("{}", ticket.title);
}

// Expect valid (panics if not)
let ticket = &store[id];
println!("{}", ticket.title);
```

---

## Mutable Indexing with `IndexMut`

### Supertrait Requirement

```rust
pub trait IndexMut<Idx>: Index<Idx> {  // `: Index<Idx>` = supertrait
    fn index_mut(&mut self, index: Idx) -> &mut Self::Output;
}
```

**Why supertrait?** Ensures consistent behavior: if you can mutate via `[idx]`, you can also read via `[idx]`.

### Example: Mutable Grid Access

```rust
struct Grid {
    data: Vec<i32>,
    width: usize,
}

impl Index<(usize, usize)> for Grid {
    type Output = i32;
    fn index(&self, (x, y): (usize, usize)) -> &i32 {
        &self.data[y * self.width + x]
    }
}

impl IndexMut<(usize, usize)> for Grid {
    fn index_mut(&mut self, (x, y): (usize, usize)) -> &mut i32 {
        &mut self.data[y * self.width + x]
    }
}

// Usage
let mut grid = Grid::new(2, 2, vec![1, 2, 3, 4]);

// Read
let val: &i32 = &grid[(0, 1)];
assert_eq!(*val, 3);

// Write
grid[(0, 1)] = 99;
assert_eq!(grid[(0, 1)], 99);
```

### Common Pattern: HashMap-backed Store

```rust
use std::collections::HashMap;

struct Store<K, V> {
    items: HashMap<K, V>,
}

impl<K, V> Index<K> for Store<K, V>
where
    K: Eq + std::hash::Hash,
{
    type Output = V;
    
    fn index(&self, key: K) -> &V {
        self.items.get(&key).expect("Key not found")
    }
}

impl<K, V> IndexMut<K> for Store<K, V>
where
    K: Eq + std::hash::Hash,
{
    fn index_mut(&mut self, key: K) -> &mut V {
        self.items.get_mut(&key).expect("Key not found")
    }
}
```

---

## Real-World Examples

### Database-backed Store

```rust
use std::collections::HashMap;

#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash)]
pub struct UserId(u64);

pub struct User {
    pub name: String,
    pub email: String,
}

pub struct UserStore {
    users: HashMap<UserId, User>,
}

impl Index<UserId> for UserStore {
    type Output = User;
    
    fn index(&self, id: UserId) -> &User {
        self.users.get(&id)
            .unwrap_or_else(|| panic!("User {} not found", id.0))
    }
}

impl IndexMut<UserId> for UserStore {
    fn index_mut(&mut self, id: UserId) -> &mut User {
        self.users.get_mut(&id)
            .unwrap_or_else(|| panic!("User {} not found", id.0))
    }
}

// Usage
let mut store = UserStore::new();
let id = store.add_user(User {
    name: "Alice".into(),
    email: "alice@example.com".into(),
});

// Read
println!("User: {}", store[id].name);

// Modify
store[id].email = "alice@newdomain.com".to_string();
```

### Matrix with Row/Column Access

```rust
pub struct Matrix {
    data: Vec<f64>,
    rows: usize,
    cols: usize,
}

// Index by (row, col)
impl Index<(usize, usize)> for Matrix {
    type Output = f64;
    
    fn index(&self, (row, col): (usize, usize)) -> &f64 {
        assert!(row < self.rows && col < self.cols, "Index out of bounds");
        &self.data[row * self.cols + col]
    }
}

impl IndexMut<(usize, usize)> for Matrix {
    fn index_mut(&mut self, (row, col): (usize, usize)) -> &mut f64 {
        assert!(row < self.rows && col < self.cols, "Index out of bounds");
        &mut self.data[row * self.cols + col]
    }
}

// Usage: natural matrix access
let mut m = Matrix::new(3, 3);
m[(0, 0)] = 1.0;
m[(1, 1)] = 2.0;
m[(2, 2)] = 3.0;

println!("Diagonal sum: {}", m[(0,0)] + m[(1,1)] + m[(2,2)]);
```

---

## Common Patterns

### Pattern 1: Wrapper with Validation

```rust
pub struct BoundedVec<T> {
    data: Vec<T>,
    max_size: usize,
}

impl<T> Index<usize> for BoundedVec<T> {
    type Output = T;
    
    fn index(&self, index: usize) -> &T {
        assert!(index < self.max_size, "Index beyond max_size");
        &self.data[index]
    }
}

impl<T> IndexMut<usize> for BoundedVec<T> {
    fn index_mut(&mut self, index: usize) -> &mut T {
        assert!(index < self.max_size, "Index beyond max_size");
        &mut self.data[index]
    }
}
```

### Pattern 2: Lazy Initialization

```rust
use std::collections::HashMap;

pub struct LazyStore<K, V> {
    cache: HashMap<K, V>,
    default: V,
}

impl<K, V> Index<K> for LazyStore<K, V>
where
    K: Eq + std::hash::Hash + Copy,
    V: Clone,
{
    type Output = V;
    
    fn index(&self, key: K) -> &V {
        self.cache.get(&key).unwrap_or(&self.default)
    }
}

// Note: IndexMut would need different approach (can't return &mut to temp)
```

### Pattern 3: Type-Safe Indices (Newtype)

```rust
#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash)]
pub struct RowIndex(usize);

#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash)]
pub struct ColIndex(usize);

pub struct DataFrame {
    data: Vec<Vec<String>>,
}

// Type-safe row access
impl Index<RowIndex> for DataFrame {
    type Output = Vec<String>;
    
    fn index(&self, row: RowIndex) -> &Vec<String> {
        &self.data[row.0]
    }
}

// Cannot accidentally use ColIndex for row access (compile error!)
// let row = df[ColIndex(0)];  // Error: Index<ColIndex> not implemented
```

---

## Gotchas and Debugging

### Gotcha 1: Cannot Return Owned Value

```rust
// ERROR: Index must return reference
// impl Index<usize> for MyVec {
//     type Output = String;
//     fn index(&self, i: usize) -> String {  // Wrong: not &String
//         self.data[i].clone()
//     }
// }

// Correct: return reference
impl Index<usize> for MyVec {
    type Output = String;
    fn index(&self, i: usize) -> &String {
        &self.data[i]
    }
}
```

**Why?** `[]` syntax expects reference, not owned value.

### Gotcha 2: IndexMut Requires Index

```rust
// ERROR: Cannot implement IndexMut without Index
// impl IndexMut<usize> for MyVec {  // Error: no Index<usize> impl
//     fn index_mut(&mut self, i: usize) -> &mut String {
//         &mut self.data[i]
//     }
// }

// Must implement Index first
impl Index<usize> for MyVec {
    type Output = String;
    fn index(&self, i: usize) -> &String { &self.data[i] }
}

// Now IndexMut works
impl IndexMut<usize> for MyVec {
    fn index_mut(&mut self, i: usize) -> &mut String {
        &mut self.data[i]
    }
}
```

### Gotcha 3: Panics vs Bounds Checking

```rust
impl Index<usize> for MyVec {
    type Output = String;
    
    fn index(&self, i: usize) -> &String {
        // Propagates panic from Vec's Index impl
        &self.data[i]  // Panics if i >= len
    }
}

// Better: explicit bounds check with clear message
impl Index<usize> for MyVec {
    type Output = String;
    
    fn index(&self, i: usize) -> &String {
        assert!(i < self.data.len(), "MyVec index {} out of bounds (len: {})", i, self.data.len());
        &self.data[i]
    }
}
```

---

## Best Practices

### ✅ DO: Use Type-Safe Index Types

```rust
// Good: Newtype prevents index confusion
#[derive(Clone, Copy, PartialEq, Eq, Hash)]
struct UserId(u64);

impl Index<UserId> for UserStore {
    type Output = User;
    fn index(&self, id: UserId) -> &User { /* ... */ }
}
```

### ✅ DO: Implement Both Index and IndexMut Together

```rust
// Good: Consistent behavior
impl Index<K> for Store<K, V> { /* ... */ }
impl IndexMut<K> for Store<K, V> { /* ... */ }
```

### ✅ DO: Provide Fallible `.get()` Alternative

```rust
// Good: Both panic and Option variants
impl Store {
    pub fn get(&self, id: Id) -> Option<&Value> { /* ... */ }
}

impl Index<Id> for Store {
    type Output = Value;
    fn index(&self, id: Id) -> &Value {
        self.get(id).expect("ID not found")
    }
}
```

### ❌ DON'T: Return Owned Values from Index

```rust
// Bad: Cannot return owned value
// impl Index<usize> for MyVec {
//     type Output = String;
//     fn index(&self, i: usize) -> String { /* ... */ }
// }

// Good: Return reference
impl Index<usize> for MyVec {
    type Output = String;
    fn index(&self, i: usize) -> &String { /* ... */ }
}
```

### ❌ DON'T: Use Index for Expensive Operations

```rust
// Bad: Index does expensive computation
// impl Index<String> for Database {
//     type Output = Record;
//     fn index(&self, query: String) -> &Record {
//         self.execute_sql(&query).expect("Query failed")  // Network call!
//     }
// }

// Good: Use explicit method for expensive ops
impl Database {
    pub fn query(&self, sql: &str) -> Result<Record, Error> {
        self.execute_sql(sql)
    }
}
```

---

## Mental Model: Tesseract Portal Protocol

Think of `Index` traits like Tesseract portal access:

1. **Portal Coordinates** (`Idx` Parameter):
   - usize = linear coordinates
   - (usize, usize) = 2D coordinates
   - UserId = custom coordinate system
   - Different coordinate types = different portal protocols

2. **Portal Destination** (`Output` Type):
   - What exists at those coordinates
   - Always referenced (portal view, not teleportation)
   - Uniquely determined by coordinate system

3. **Viewing Portal** (`Index`):
   - Look through portal at coordinates (immutable)
   - See what's there without touching
   - `container[coord]` opens viewing portal

4. **Manipulation Portal** (`IndexMut`):
   - Reach through to modify destination
   - Requires viewing portal established first (supertrait)
   - `container[coord] = value` opens manipulation portal

5. **Invalid Coordinates** (Panic):
   - Portal to nonexistent location fails catastrophically
   - Like array out-of-bounds panic
   - Use `.get()` for uncertain coordinates

6. **Multi-Dimensional Portals** (Multiple Implementations):
   - Same container, different coordinate systems
   - Grid: linear OR 2D access
   - Compiler selects based on coordinate type

**The Analogy**: Just as the Tesseract opens portals to different coordinates (index types) allowing viewing (Index) and manipulation (IndexMut) of what exists at that location (Output type), Rust's indexing traits enable ergonomic `[]` syntax for custom containers—with viewing portals required before manipulation, ensuring type-safe zero-cost access to contained data through multiple coordinate systems.

---

## The Essence: Ergonomic Container Access

`Index<Idx>` and `IndexMut<Idx>` enable custom `[]` subscript syntax. Generic index type allows flexible access patterns. Associated Output type is what's accessed. IndexMut requires Index (supertrait). Panics on invalid access (use `.get()` for fallible).

**Index Trait**: Immutable `container[idx]` → `&Output`  
**IndexMut Trait**: Mutable `container[idx]` → `&mut Output` (requires Index)  
**Generic Idx**: Flexible index types (usize, custom IDs, tuples, ranges)  
**Associated Output**: Type being accessed  
**Panics**: Invalid index panics (not Option) — matches array/Vec behavior

Like Tesseract portals opened with coordinates (Idx) revealing what's at that location (Output), with viewing portals (Index) required before manipulation portals (IndexMut), Rust's indexing traits provide ergonomic `[]` syntax for custom containers—enabling zero-cost operator overloading while maintaining type safety and consistent behavior across different access patterns and coordinate systems.
