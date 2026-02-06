# Query Builder Algebra: Arel → Rust Mapping

## Date: 2026-02-06

## Purpose

This document specifies how Rails' Arel query builder maps to Rust query builder patterns. The goal is to enable the compiler to translate Rails scopes and queries into composable Rust code that generates equivalent SQL.

**Key Insight**: Arel implements Codd's Relational Algebra as a Ruby DSL. The same algebra can be expressed in Rust with static typing, enabling the compiler to generate query builder code that composes exactly like Rails scopes.

---

## Arel Architecture Overview

### What Arel Is

Arel is a SQL AST (Abstract Syntax Tree) manager that:
1. Represents SQL queries as Ruby object trees
2. Provides composable operations (chainable methods)
3. Uses the Visitor pattern to generate database-specific SQL
4. Is the foundation underneath ActiveRecord's query interface

### Arel's AST Structure

```
                           SelectStatement (root)
                                   │
            ┌──────────────────────┼──────────────────────┐
            │                      │                      │
       SelectCore            [Orders]               [Limit]
            │                      │                      │
    ┌───────┼───────┐         Ascending              Limit
    │       │       │              │                    │
[Projections] JoinSource   [Wheres]  Attribute         10
    │           │              │
 Attribute   Table        And/Equality
    │           │              │
 "name"    "users"    ┌────────┴────────┐
                      │                 │
                 Equality          Equality
                      │                 │
              ┌───────┴───────┐   ┌─────┴─────┐
           Attribute   Casted  Attribute  Casted
              │          │        │          │
           "status"     1     "deleted"   false
```

### Core Node Types

| Arel Node | Purpose | SQL Fragment |
|-----------|---------|--------------|
| `SelectStatement` | Root of SELECT query | `SELECT ... FROM ... WHERE ...` |
| `SelectCore` | Core SELECT components | projections, sources, wheres |
| `JoinSource` | FROM clause with joins | `FROM users JOIN posts ON ...` |
| `Equality` | Column = value | `status = 1` |
| `NotEqual` | Column != value | `status != 1` |
| `In` | Column IN (values) | `status IN (1, 2, 3)` |
| `NotIn` | Column NOT IN (values) | `status NOT IN (1, 2, 3)` |
| `Matches` | LIKE pattern | `name LIKE '%foo%'` |
| `DoesNotMatch` | NOT LIKE pattern | `name NOT LIKE '%foo%'` |
| `GreaterThan` | Column > value | `age > 18` |
| `GreaterThanOrEqual` | Column >= value | `age >= 18` |
| `LessThan` | Column < value | `age < 65` |
| `LessThanOrEqual` | Column <= value | `age <= 65` |
| `Between` | Column BETWEEN | `age BETWEEN 18 AND 65` |
| `And` | Logical AND | `(a = 1) AND (b = 2)` |
| `Or` | Logical OR | `(a = 1) OR (b = 2)` |
| `Not` | Logical NOT | `NOT (deleted = true)` |
| `Grouping` | Parentheses | `(...)` |
| `InnerJoin` | INNER JOIN | `INNER JOIN posts ON ...` |
| `OuterJoin` | LEFT OUTER JOIN | `LEFT OUTER JOIN posts ON ...` |
| `Ascending` | ORDER BY ASC | `ORDER BY name ASC` |
| `Descending` | ORDER BY DESC | `ORDER BY name DESC` |
| `Limit` | LIMIT clause | `LIMIT 10` |
| `Offset` | OFFSET clause | `OFFSET 20` |
| `Count` | COUNT aggregate | `COUNT(*)` |
| `Sum` | SUM aggregate | `SUM(amount)` |
| `Average` | AVG aggregate | `AVG(score)` |
| `Minimum` | MIN aggregate | `MIN(price)` |
| `Maximum` | MAX aggregate | `MAX(price)` |

---

## Relational Algebra Mapping

Arel implements Codd's Relational Algebra operations:

| Operation | Algebra Symbol | Arel Method | SQL |
|-----------|----------------|-------------|-----|
| Selection | σ (sigma) | `.where()` | `WHERE ...` |
| Projection | π (pi) | `.select()` | `SELECT col1, col2` |
| Rename | ρ (rho) | `.as()` | `AS alias` |
| Union | ∪ | `.union()` | `UNION` |
| Intersection | ∩ | `.intersect()` | `INTERSECT` |
| Difference | − | `.except()` | `EXCEPT` |
| Cartesian Product | × | `.join()` (no ON) | `CROSS JOIN` |
| Natural Join | ⋈ | `.join().on()` | `JOIN ... ON ...` |

### The Composability Property

The key algebraic property is **closure**: every operation on a relation returns a relation. This enables infinite chaining:

```ruby
# Each method returns a Relation, enabling composition
User.where(status: :active)           # σ(status=active)
    .where(role: :admin)              # σ(role=admin)
    .order(:created_at)               # τ(created_at)
    .limit(10)                        # LIMIT 10
    .select(:id, :name)               # π(id, name)
```

---

## Rust Query Builder Design

### Design Goals

1. **Type Safety**: Invalid queries should not compile
2. **Composability**: Operations return queryable types, enabling chaining
3. **Zero-Cost Abstractions**: No runtime overhead vs hand-written SQL
4. **Database Agnostic**: Support PostgreSQL, MySQL, SQLite

### Core Types

```rust
/// A query that can be further composed or executed
pub struct Query<T: Model> {
    /// The underlying query builder (Diesel/SeaORM/SQLx)
    inner: BoxedSelectStatement<'static, T::SqlType, T::Table>,
    /// Phantom data for the model type
    _marker: PhantomData<T>,
}

/// Trait for types that can be queried
pub trait Queryable: Model {
    type Query: QueryDsl;

    /// Start a new query
    fn query() -> Self::Query;

    /// Get the Arel-like table reference
    fn table() -> Self::Table;
}

/// Trait for query operations (implements relational algebra)
pub trait QueryDsl: Sized {
    type Model: Model;

    // ═══════════════════════════════════════════════════════════════
    // SELECTION (σ) - WHERE clauses
    // ═══════════════════════════════════════════════════════════════

    /// Filter by equality
    fn filter<C, V>(self, column: C, value: V) -> Self
    where
        C: Column,
        V: AsExpression<C::SqlType>;

    /// Filter with a predicate expression
    fn filter_by<P>(self, predicate: P) -> Self
    where
        P: Expression<SqlType = Bool>;

    /// Filter using OR
    fn or_filter<P>(self, predicate: P) -> Self
    where
        P: Expression<SqlType = Bool>;

    // ═══════════════════════════════════════════════════════════════
    // PROJECTION (π) - SELECT columns
    // ═══════════════════════════════════════════════════════════════

    /// Select specific columns
    fn select<S>(self, selection: S) -> Query<S::Output>
    where
        S: Selectable;

    /// Select all columns (default)
    fn select_all(self) -> Self;

    // ═══════════════════════════════════════════════════════════════
    // JOIN (⋈) - Table joins
    // ═══════════════════════════════════════════════════════════════

    /// Inner join with another table
    fn inner_join<J>(self) -> Self
    where
        J: JoinTo<Self::Model>;

    /// Left outer join
    fn left_join<J>(self) -> Self
    where
        J: JoinTo<Self::Model>;

    /// Join with explicit ON clause
    fn join_on<J, P>(self, predicate: P) -> Self
    where
        J: Table,
        P: Expression<SqlType = Bool>;

    // ═══════════════════════════════════════════════════════════════
    // ORDERING (τ) - ORDER BY
    // ═══════════════════════════════════════════════════════════════

    /// Order by ascending
    fn order_asc<C>(self, column: C) -> Self
    where
        C: Column;

    /// Order by descending
    fn order_desc<C>(self, column: C) -> Self
    where
        C: Column;

    /// Order by multiple columns
    fn order<O>(self, ordering: O) -> Self
    where
        O: OrderClause;

    /// Replace existing ordering
    fn reorder<O>(self, ordering: O) -> Self
    where
        O: OrderClause;

    // ═══════════════════════════════════════════════════════════════
    // LIMIT/OFFSET
    // ═══════════════════════════════════════════════════════════════

    fn limit(self, count: i64) -> Self;
    fn offset(self, count: i64) -> Self;

    // ═══════════════════════════════════════════════════════════════
    // GROUPING
    // ═══════════════════════════════════════════════════════════════

    fn group_by<G>(self, grouping: G) -> Self
    where
        G: GroupByClause;

    fn having<P>(self, predicate: P) -> Self
    where
        P: Expression<SqlType = Bool>;

    // ═══════════════════════════════════════════════════════════════
    // SET OPERATIONS
    // ═══════════════════════════════════════════════════════════════

    fn union(self, other: Self) -> Self;
    fn union_all(self, other: Self) -> Self;
    fn intersect(self, other: Self) -> Self;
    fn except(self, other: Self) -> Self;

    // ═══════════════════════════════════════════════════════════════
    // EXECUTION
    // ═══════════════════════════════════════════════════════════════

    /// Execute and load all results
    async fn load<C: Connection>(self, conn: &C) -> Result<Vec<Self::Model>>;

    /// Execute and load first result
    async fn first<C: Connection>(self, conn: &C) -> Result<Option<Self::Model>>;

    /// Execute and count results
    async fn count<C: Connection>(self, conn: &C) -> Result<i64>;

    /// Check if any results exist
    async fn exists<C: Connection>(self, conn: &C) -> Result<bool>;

    /// Get the generated SQL (for debugging)
    fn to_sql(&self) -> String;
}
```

### Predicate Builder

```rust
/// Column predicate methods (equivalent to Arel predications)
pub trait Predicate: Column {
    // ═══════════════════════════════════════════════════════════════
    // EQUALITY
    // ═══════════════════════════════════════════════════════════════

    /// Column = value
    fn eq<V>(self, value: V) -> EqExpr<Self, V>
    where
        V: AsExpression<Self::SqlType>;

    /// Column != value
    fn ne<V>(self, value: V) -> NeExpr<Self, V>
    where
        V: AsExpression<Self::SqlType>;

    /// Column IS NULL
    fn is_null(self) -> IsNullExpr<Self>;

    /// Column IS NOT NULL
    fn is_not_null(self) -> IsNotNullExpr<Self>;

    // ═══════════════════════════════════════════════════════════════
    // COMPARISON
    // ═══════════════════════════════════════════════════════════════

    /// Column > value
    fn gt<V>(self, value: V) -> GtExpr<Self, V>
    where
        V: AsExpression<Self::SqlType>;

    /// Column >= value
    fn gte<V>(self, value: V) -> GteExpr<Self, V>
    where
        V: AsExpression<Self::SqlType>;

    /// Column < value
    fn lt<V>(self, value: V) -> LtExpr<Self, V>
    where
        V: AsExpression<Self::SqlType>;

    /// Column <= value
    fn lte<V>(self, value: V) -> LteExpr<Self, V>
    where
        V: AsExpression<Self::SqlType>;

    /// Column BETWEEN low AND high
    fn between<V>(self, low: V, high: V) -> BetweenExpr<Self, V>
    where
        V: AsExpression<Self::SqlType>;

    // ═══════════════════════════════════════════════════════════════
    // SET MEMBERSHIP
    // ═══════════════════════════════════════════════════════════════

    /// Column IN (values)
    fn in_<I, V>(self, values: I) -> InExpr<Self, I>
    where
        I: IntoIterator<Item = V>,
        V: AsExpression<Self::SqlType>;

    /// Column NOT IN (values)
    fn not_in<I, V>(self, values: I) -> NotInExpr<Self, I>
    where
        I: IntoIterator<Item = V>,
        V: AsExpression<Self::SqlType>;

    // ═══════════════════════════════════════════════════════════════
    // PATTERN MATCHING
    // ═══════════════════════════════════════════════════════════════

    /// Column LIKE pattern
    fn like<V>(self, pattern: V) -> LikeExpr<Self, V>
    where
        V: AsExpression<Text>;

    /// Column NOT LIKE pattern
    fn not_like<V>(self, pattern: V) -> NotLikeExpr<Self, V>
    where
        V: AsExpression<Text>;

    /// Column ILIKE pattern (case-insensitive, PostgreSQL)
    fn ilike<V>(self, pattern: V) -> ILikeExpr<Self, V>
    where
        V: AsExpression<Text>;

    /// Column ~ regex (PostgreSQL)
    fn matches_regex<V>(self, pattern: V) -> RegexExpr<Self, V>
    where
        V: AsExpression<Text>;

    // ═══════════════════════════════════════════════════════════════
    // STRING OPERATIONS
    // ═══════════════════════════════════════════════════════════════

    /// Contains substring (generates LIKE '%value%')
    fn contains<V>(self, value: V) -> ContainsExpr<Self, V>
    where
        V: AsExpression<Text>;

    /// Starts with prefix (generates LIKE 'value%')
    fn starts_with<V>(self, value: V) -> StartsWithExpr<Self, V>
    where
        V: AsExpression<Text>;

    /// Ends with suffix (generates LIKE '%value')
    fn ends_with<V>(self, value: V) -> EndsWithExpr<Self, V>
    where
        V: AsExpression<Text>;

    // ═══════════════════════════════════════════════════════════════
    // ORDERING
    // ═══════════════════════════════════════════════════════════════

    /// Ascending order
    fn asc(self) -> Asc<Self>;

    /// Descending order
    fn desc(self) -> Desc<Self>;

    /// Nulls first
    fn nulls_first(self) -> NullsFirst<Self>;

    /// Nulls last
    fn nulls_last(self) -> NullsLast<Self>;
}

/// Logical expression combinators
pub trait BoolExpr: Expression<SqlType = Bool> {
    /// expr AND other
    fn and<E>(self, other: E) -> AndExpr<Self, E>
    where
        E: Expression<SqlType = Bool>;

    /// expr OR other
    fn or<E>(self, other: E) -> OrExpr<Self, E>
    where
        E: Expression<SqlType = Bool>;

    /// NOT expr
    fn not(self) -> NotExpr<Self>;
}
```

---

## Scope Composition

### Rails Scope Definition

```ruby
class Post < ApplicationRecord
  scope :published, -> { where(published: true) }
  scope :recent, -> { order(created_at: :desc) }
  scope :by_author, ->(author) { where(author: author) }
  scope :featured, -> { published.where(featured: true) }  # Composition!
end

# Usage: scopes compose
Post.published.recent.by_author(user).limit(10)
```

### Rust Scope Translation

```rust
/// Scopes are implemented as associated functions returning Query<T>
impl Post {
    // ═══════════════════════════════════════════════════════════════
    // SIMPLE SCOPES (no parameters)
    // ═══════════════════════════════════════════════════════════════

    /// scope :published, -> { where(published: true) }
    pub fn published() -> Query<Self> {
        Self::query().filter(posts::published, true)
    }

    /// scope :recent, -> { order(created_at: :desc) }
    pub fn recent() -> Query<Self> {
        Self::query().order_desc(posts::created_at)
    }

    // ═══════════════════════════════════════════════════════════════
    // PARAMETERIZED SCOPES
    // ═══════════════════════════════════════════════════════════════

    /// scope :by_author, ->(author) { where(author: author) }
    pub fn by_author(author: &User) -> Query<Self> {
        Self::query().filter(posts::author_id, author.id)
    }

    /// scope :by_status, ->(status) { where(status: status) }
    pub fn by_status(status: PostStatus) -> Query<Self> {
        Self::query().filter(posts::status, status.to_i32())
    }

    // ═══════════════════════════════════════════════════════════════
    // COMPOSED SCOPES
    // ═══════════════════════════════════════════════════════════════

    /// scope :featured, -> { published.where(featured: true) }
    pub fn featured() -> Query<Self> {
        Self::published().filter(posts::featured, true)
    }

    /// scope :recent_featured, -> { featured.recent.limit(5) }
    pub fn recent_featured() -> Query<Self> {
        Self::featured().order_desc(posts::created_at).limit(5)
    }
}

/// Scope trait for chainable operations on existing queries
pub trait PostScopes: QueryDsl<Model = Post> {
    /// Add published filter to existing query
    fn published(self) -> Self {
        self.filter(posts::published, true)
    }

    /// Add recent ordering to existing query
    fn recent(self) -> Self {
        self.order_desc(posts::created_at)
    }

    /// Add author filter to existing query
    fn by_author(self, author: &User) -> Self {
        self.filter(posts::author_id, author.id)
    }
}

// Implement for Query<Post>
impl PostScopes for Query<Post> {}

// Usage: scopes compose exactly like Rails
let posts = Post::published()
    .recent()
    .by_author(&user)
    .limit(10)
    .load(&conn)
    .await?;

// Or start from query and chain scopes
let posts = Post::query()
    .published()
    .featured()
    .load(&conn)
    .await?;
```

### Scope Chaining Implementation

The key insight is that **scopes are not stored state** — they're functions that return queries. Composition works by transforming queries:

```rust
// Conceptually, scope chaining is function composition:
// Post.published.recent.limit(10)
//   = limit(10, recent(published(Post.query())))
//   = Post.query().filter(...).order(...).limit(10)

// In Rust, method chaining achieves the same:
Post::query()           // Query<Post>
    .published()        // Query<Post>  (adds WHERE published = true)
    .recent()           // Query<Post>  (adds ORDER BY created_at DESC)
    .limit(10)          // Query<Post>  (adds LIMIT 10)
    .load(&conn)        // Vec<Post>    (executes SQL)
```

---

## Complex Query Patterns

### OR Conditions

```ruby
# Rails: Using Arel for OR
User.where(status: :active).or(User.where(role: :admin))
```

```rust
// Rust equivalent
User::query()
    .filter_by(
        users::status.eq(UserStatus::Active.to_i32())
            .or(users::role.eq(UserRole::Admin.to_i32()))
    )
    .load(&conn)
    .await?;

// Or using the or_filter method
User::query()
    .filter(users::status, UserStatus::Active)
    .or_filter(users::role.eq(UserRole::Admin))
    .load(&conn)
    .await?;
```

### Subqueries

```ruby
# Rails: Subquery in WHERE
Post.where(author_id: User.where(active: true).select(:id))
```

```rust
// Rust equivalent
let active_user_ids = User::query()
    .filter(users::active, true)
    .select(users::id);

Post::query()
    .filter_by(posts::author_id.in_(active_user_ids))
    .load(&conn)
    .await?;
```

### JOINs with Conditions

```ruby
# Rails: JOIN with conditions
Post.joins(:author).where(users: { status: :active })
```

```rust
// Rust equivalent
Post::query()
    .inner_join::<User>()
    .filter(users::status, UserStatus::Active)
    .load(&conn)
    .await?;

// With explicit ON clause
Post::query()
    .join_on::<User>(
        posts::author_id.eq(users::id)
            .and(users::status.eq(UserStatus::Active))
    )
    .load(&conn)
    .await?;
```

### Through Associations as JOINs

```ruby
# Rails: has_many :tags, through: :taggings
user.tags  # Generates JOIN automatically
```

```rust
// Rust: Explicit JOIN chain
impl User {
    pub async fn tags(&self, conn: &impl Connection) -> Result<Vec<Tag>> {
        Tag::query()
            .inner_join::<Tagging>()
            .filter(taggings::user_id, self.id)
            .load(conn)
            .await
    }
}

// Or as a scope
impl User {
    pub fn tags_query(&self) -> Query<Tag> {
        Tag::query()
            .inner_join::<Tagging>()
            .filter(taggings::user_id, self.id.unwrap())
    }
}
```

### Aggregations

```ruby
# Rails
Post.group(:author_id).count
Post.where(published: true).average(:views)
Post.maximum(:created_at)
```

```rust
// Rust equivalents
// Group and count
Post::query()
    .group_by(posts::author_id)
    .select((posts::author_id, count_star()))
    .load::<(i64, i64)>(&conn)
    .await?;

// Average
Post::query()
    .filter(posts::published, true)
    .select(avg(posts::views))
    .first::<Option<f64>>(&conn)
    .await?;

// Maximum
Post::query()
    .select(max(posts::created_at))
    .first::<Option<DateTime<Utc>>>(&conn)
    .await?;
```

---

## Mapping Table: Rails → Rust

### Simple Queries

| Rails | Rust |
|-------|------|
| `User.all` | `User::query().load(&conn)` |
| `User.first` | `User::query().first(&conn)` |
| `User.find(1)` | `User::find(&conn, 1)` |
| `User.find_by(email: x)` | `User::query().filter(users::email, x).first(&conn)` |
| `User.count` | `User::query().count(&conn)` |
| `User.exists?` | `User::query().exists(&conn)` |

### WHERE Clauses

| Rails | Rust |
|-------|------|
| `where(status: 1)` | `.filter(col::status, 1)` |
| `where(status: [1,2])` | `.filter_by(col::status.in_([1,2]))` |
| `where.not(status: 1)` | `.filter_by(col::status.ne(1))` |
| `where("age > ?", 18)` | `.filter_by(col::age.gt(18))` |
| `where("name LIKE ?", "%foo%")` | `.filter_by(col::name.like("%foo%"))` |
| `where(name: nil)` | `.filter_by(col::name.is_null())` |
| `where.not(name: nil)` | `.filter_by(col::name.is_not_null())` |

### ORDER BY

| Rails | Rust |
|-------|------|
| `order(:name)` | `.order_asc(col::name)` |
| `order(name: :asc)` | `.order_asc(col::name)` |
| `order(name: :desc)` | `.order_desc(col::name)` |
| `order(:name, :email)` | `.order((col::name.asc(), col::email.asc()))` |
| `reorder(:created_at)` | `.reorder(col::created_at.asc())` |

### LIMIT/OFFSET

| Rails | Rust |
|-------|------|
| `limit(10)` | `.limit(10)` |
| `offset(20)` | `.offset(20)` |
| `limit(10).offset(20)` | `.limit(10).offset(20)` |

### SELECT

| Rails | Rust |
|-------|------|
| `select(:id, :name)` | `.select((col::id, col::name))` |
| `select("id, name")` | `.select((col::id, col::name))` |
| `distinct` | `.distinct()` |

### JOINs

| Rails | Rust |
|-------|------|
| `joins(:author)` | `.inner_join::<Author>()` |
| `left_joins(:author)` | `.left_join::<Author>()` |
| `includes(:author)` | `.preload::<Author>()` or eager load |

### GROUP BY / HAVING

| Rails | Rust |
|-------|------|
| `group(:status)` | `.group_by(col::status)` |
| `group(:status).count` | `.group_by(col::status).select((col::status, count_star()))` |
| `having("count(*) > 5")` | `.having(count_star().gt(5))` |

### Scopes

| Rails | Rust |
|-------|------|
| `scope :active, -> { where(active: true) }` | `fn active() -> Query<Self> { Self::query().filter(col::active, true) }` |
| `scope :recent, -> { order(created_at: :desc) }` | `fn recent() -> Query<Self> { Self::query().order_desc(col::created_at) }` |
| `Post.active.recent` | `Post::active().recent()` |

---

## Compiler Translation Rules

### Rule 1: Simple Scope → Static Function

```ruby
# INPUT
scope :published, -> { where(published: true) }

# OUTPUT
pub fn published() -> Query<Self> {
    Self::query().filter(posts::published, true)
}
```

### Rule 2: Parameterized Scope → Function with Arguments

```ruby
# INPUT
scope :by_author, ->(author) { where(author_id: author.id) }

# OUTPUT
pub fn by_author(author: &User) -> Query<Self> {
    Self::query().filter(posts::author_id, author.id.unwrap())
}
```

### Rule 3: Composed Scope → Chained Calls

```ruby
# INPUT
scope :featured, -> { published.where(featured: true) }

# OUTPUT
pub fn featured() -> Query<Self> {
    Self::published().filter(posts::featured, true)
}
```

### Rule 4: Lambda in Scope → Captured Variable

```ruby
# INPUT (runtime value - flagged)
scope :recent, -> { where("created_at > ?", 1.week.ago) }

# OUTPUT (with warning: runtime value)
pub fn recent() -> Query<Self> {
    let cutoff = Utc::now() - Duration::weeks(1);
    Self::query().filter_by(posts::created_at.gt(cutoff))
}
// WARNING: Contains runtime value (1.week.ago)
```

### Rule 5: default_scope → Default Query Method

```ruby
# INPUT
default_scope { where(deleted: false) }

# OUTPUT
impl Post {
    pub fn query() -> Query<Self> {
        Query::new().filter(posts::deleted, false)
    }

    pub fn unscoped() -> Query<Self> {
        Query::new_unscoped()
    }
}
```

---

## Dynamic Query Patterns (Flagged)

These patterns contain runtime values and are flagged for review:

### Pattern 1: Time-Based Queries

```ruby
scope :recent, -> { where("created_at > ?", 1.week.ago) }
scope :today, -> { where(created_at: Date.today.all_day) }
```

**Translation**: Generate code with `Utc::now()` call, flag as "runtime value"

### Pattern 2: Current User/Tenant

```ruby
scope :mine, -> { where(user_id: Current.user.id) }
scope :in_tenant, -> { where(tenant_id: Current.tenant_id) }
```

**Translation**: Cannot compile — requires runtime context. Generate:
```rust
// MANUAL PORT REQUIRED: Uses Current.user
pub fn mine(_current_user: &User) -> Query<Self> {
    todo!("Implement with current_user parameter")
}
```

### Pattern 3: Conditional Logic in Scope

```ruby
scope :visible, -> {
  if Current.user&.admin?
    all
  else
    where(published: true)
  end
}
```

**Translation**: Cannot compile — conditional on runtime state. Generate:
```rust
// MANUAL PORT REQUIRED: Runtime conditional
pub fn visible(is_admin: bool) -> Query<Self> {
    if is_admin {
        Self::query()
    } else {
        Self::query().filter(posts::published, true)
    }
}
```

---

## Integration with activerust

The query builder integrates with the `activerust` crate from Document 11:

```rust
// Full example: Model with scopes, associations, and activerust traits
#[derive(Queryable, Insertable, DirtyTracking, Validatable)]
#[table_name = "posts"]
pub struct Post {
    pub id: Option<i64>,
    pub title: String,
    pub body: String,
    pub author_id: i64,
    pub status: PostStatus,
    pub published: bool,
    pub featured: bool,
    pub views: i32,
    pub created_at: Option<DateTime<Utc>>,
    pub updated_at: Option<DateTime<Utc>>,
}

// Scopes
impl Post {
    pub fn published() -> Query<Self> {
        Self::query().filter(posts::published, true)
    }

    pub fn featured() -> Query<Self> {
        Self::published().filter(posts::featured, true)
    }

    pub fn by_author(author: &User) -> Query<Self> {
        Self::query().filter(posts::author_id, author.id.unwrap())
    }

    pub fn popular() -> Query<Self> {
        Self::query()
            .filter_by(posts::views.gt(1000))
            .order_desc(posts::views)
    }
}

// Association queries
impl User {
    pub fn posts(&self) -> Query<Post> {
        Post::by_author(self)
    }

    pub async fn published_posts(&self, conn: &impl Connection) -> Result<Vec<Post>> {
        self.posts()
            .published()
            .order_desc(posts::created_at)
            .load(conn)
            .await
    }
}

// Usage
async fn example(conn: &impl Connection, user: &User) -> Result<()> {
    // Compose scopes
    let posts = Post::featured()
        .by_author(user)
        .limit(10)
        .load(conn)
        .await?;

    // Association with scope
    let recent_posts = user.posts()
        .published()
        .order_desc(posts::created_at)
        .limit(5)
        .load(conn)
        .await?;

    // Complex query
    let top_posts = Post::query()
        .filter(posts::published, true)
        .filter_by(posts::views.gt(100))
        .order_desc(posts::views)
        .limit(10)
        .load(conn)
        .await?;

    Ok(())
}
```

---

## Summary

### What the Compiler Generates

For each Rails scope, the compiler generates:

1. **Static function** returning `Query<Self>`
2. **Trait implementation** for chainable scopes
3. **SQL construction** via Diesel/SeaORM query builder
4. **Type-safe predicates** using column types

### What Remains Manual

1. **Runtime values** (Current.user, Time.now, etc.) — flagged
2. **Conditional scopes** — require parameter extraction
3. **Dynamic SQL** — raw SQL strings

### The Algebra Holds

The key insight is that Codd's Relational Algebra works identically in Rust:
- Selection (σ) → `.filter()`
- Projection (π) → `.select()`
- Join (⋈) → `.inner_join()`
- Union (∪) → `.union()`

Scopes are **named selections** — functions that return filtered relations. Composition is function application. The algebra is closed under all operations.

**Rails scopes compose. Rust query builders compose. The mapping is direct.**
