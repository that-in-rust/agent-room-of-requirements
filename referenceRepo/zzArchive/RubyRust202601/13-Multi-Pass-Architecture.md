# Multi-Pass Compiler Architecture

## Date: 2026-02-06

## Purpose

This document specifies the architecture of the Rails-to-Rust compiler. The key insight is that the original "layered pyramid" model (Layer 0 → 4) is too simplistic — **dependencies between layers require multiple passes**. This document defines a query-based architecture inspired by Salsa (used in rust-analyzer) that handles these dependencies correctly.

---

## The Problem: Layer Dependencies

### Original Model (Too Simple)

```
Layer 0: Schema → Rust structs
Layer 1: Associations → Relation methods
Layer 2: Behavior → Validations, callbacks
Layer 3: Interface → Routes, controllers
Layer 4: Resolution → Polymorphic, STI
```

**The assumption was**: Each layer only depends on layers below it.

**The reality is**: Dependencies cross layers in both directions.

### Cross-Layer Dependencies

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ EXAMPLE: Polymorphic Association                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│ Layer 1 (Associations):                                                      │
│   belongs_to :commentable, polymorphic: true                                 │
│                                                                              │
│ NEEDS information from:                                                      │
│   • Layer 0: What columns exist? (commentable_id, commentable_type)          │
│   • Layer 1 (other models): Which models have `as: :commentable`?            │
│   • Layer 4: What is the closed type set? (needs DB query or file scan)      │
│                                                                              │
│ PRODUCES information for:                                                    │
│   • Layer 2: Validation of commentable_type against type set                 │
│   • Layer 4: Enum type for polymorphic dispatch                              │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│ EXAMPLE: Counter Cache                                                       │
├─────────────────────────────────────────────────────────────────────────────┤
│ Layer 1 (belongs_to side):                                                   │
│   belongs_to :author, counter_cache: true                                    │
│                                                                              │
│ NEEDS information from:                                                      │
│   • Layer 0: Does `authors` table have `posts_count` column?                 │
│   • Layer 1 (Author model): Is there inverse `has_many :posts`?              │
│                                                                              │
│ PRODUCES information for:                                                    │
│   • Layer 2: Callback to increment/decrement counter on save/destroy         │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│ EXAMPLE: Inverse Association                                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│ Layer 1:                                                                     │
│   class User                                                                 │
│     has_many :posts                                                          │
│   end                                                                        │
│                                                                              │
│   class Post                                                                 │
│     belongs_to :author, class_name: 'User'                                   │
│   end                                                                        │
│                                                                              │
│ To resolve `inverse_of`:                                                     │
│   • Need to know User has `has_many :posts`                                  │
│   • Need to know Post belongs_to with `class_name: 'User'`                   │
│   • Need to match by FK (posts.author_id → users.id)                         │
│                                                                              │
│ This is a GRAPH problem, not a single-pass problem.                          │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## The Solution: Query-Based Architecture

### What is a Query?

A **query** is a question the compiler can ask, with:
- **Inputs**: Parameters to the question
- **Output**: The answer (memoized after first computation)
- **Dependencies**: Other queries this one calls

### Example Queries

```
struct_for(model_name) → RustStruct
    "What Rust struct represents the User model?"

columns_for(table_name) → Vec<Column>
    "What columns does the users table have?"

associations_for(model_name) → Vec<Association>
    "What associations does User declare?"

inverse_of(model_name, association_name) → Option<Association>
    "What is the inverse of User.posts?"

polymorphic_types(model_name, association_name) → Vec<TypeName>
    "What types can Comment.commentable be?"

callbacks_for(model_name) → Vec<Callback>
    "What callbacks does User have?"

validations_for(model_name) → Vec<Validation>
    "What validations does User have?"
```

### Query Dependencies Form a DAG

```
                    ┌────────────────┐
                    │ generate_code  │ (final output)
                    └───────┬────────┘
                            │
           ┌────────────────┼────────────────┐
           │                │                │
    ┌──────┴──────┐  ┌──────┴──────┐  ┌──────┴──────┐
    │ struct_for  │  │ callbacks   │  │ validations │
    └──────┬──────┘  └──────┬──────┘  └──────┬──────┘
           │                │                │
    ┌──────┴──────┐  ┌──────┴──────┐  ┌──────┴──────┐
    │ columns_for │  │ associations│  │ associations│
    └──────┬──────┘  └──────┬──────┘  └──────┬──────┘
           │                │                │
    ┌──────┴──────┐  ┌──────┴──────┐        │
    │ parse_schema│  │ inverse_of  │        │
    └─────────────┘  └──────┬──────┘        │
                            │                │
                     ┌──────┴──────┐        │
                     │ associations│◄───────┘
                     │ (other model)│
                     └──────┬──────┘
                            │
                     ┌──────┴──────┐
                     │ columns_for │
                     │ (other table)│
                     └─────────────┘
```

### The Red-Green Algorithm

Salsa uses the "red-green" algorithm for incremental recomputation:

1. **Input change**: A source file is modified
2. **Mark red**: All queries depending on that input are marked "potentially stale" (red)
3. **Lazy verification**: When a red query is accessed:
   - Recursively verify its dependencies
   - If all dependencies are unchanged, mark query "green" (valid)
   - If any dependency changed, recompute the query
4. **Memoization**: Computed results are cached until inputs change

---

## Compiler Queries

### Input Queries (Layer 0)

These are the "base" queries that read from files or database:

```rust
/// Input: Raw schema information
#[salsa::input]
pub struct SchemaInput {
    /// Path to schema.rb or structure.sql
    #[return_ref]
    pub schema_path: PathBuf,

    /// Raw file contents
    #[return_ref]
    pub schema_text: String,
}

/// Input: Raw model file
#[salsa::input]
pub struct ModelFileInput {
    #[return_ref]
    pub model_name: String,
    #[return_ref]
    pub file_path: PathBuf,
    #[return_ref]
    pub file_text: String,
}

/// Input: Database connection (for Snapshot mode)
#[salsa::input]
pub struct DatabaseInput {
    #[return_ref]
    pub connection_string: String,
}
```

### Derived Queries (Computed)

```rust
/// Parse schema into table definitions
#[salsa::tracked]
pub fn tables(db: &dyn Db, schema: SchemaInput) -> Vec<TableDef> {
    let text = schema.schema_text(db);
    parse_schema(&text)  // Returns Vec<TableDef>
}

/// Get columns for a specific table
#[salsa::tracked]
pub fn columns_for(db: &dyn Db, schema: SchemaInput, table_name: String) -> Vec<ColumnDef> {
    tables(db, schema)
        .into_iter()
        .find(|t| t.name == table_name)
        .map(|t| t.columns)
        .unwrap_or_default()
}

/// Parse model file into AST
#[salsa::tracked]
pub fn model_ast(db: &dyn Db, model: ModelFileInput) -> ModelAst {
    let text = model.file_text(db);
    parse_ruby_model(&text)  // Returns ModelAst
}

/// Extract associations from model AST
#[salsa::tracked]
pub fn associations_for(db: &dyn Db, model: ModelFileInput) -> Vec<AssociationDef> {
    let ast = model_ast(db, model);
    extract_associations(&ast)
}

/// Extract validations from model AST
#[salsa::tracked]
pub fn validations_for(db: &dyn Db, model: ModelFileInput) -> Vec<ValidationDef> {
    let ast = model_ast(db, model);
    extract_validations(&ast)
}

/// Extract callbacks from model AST
#[salsa::tracked]
pub fn callbacks_for(db: &dyn Db, model: ModelFileInput) -> Vec<CallbackDef> {
    let ast = model_ast(db, model);
    extract_callbacks(&ast)
}

/// Extract enums from model AST
#[salsa::tracked]
pub fn enums_for(db: &dyn Db, model: ModelFileInput) -> Vec<EnumDef> {
    let ast = model_ast(db, model);
    extract_enums(&ast)
}

/// Extract scopes from model AST
#[salsa::tracked]
pub fn scopes_for(db: &dyn Db, model: ModelFileInput) -> Vec<ScopeDef> {
    let ast = model_ast(db, model);
    extract_scopes(&ast)
}
```

### Cross-Model Queries (Resolution)

```rust
/// Find all models in the project
#[salsa::tracked]
pub fn all_models(db: &dyn Db) -> Vec<ModelFileInput> {
    // Glob for app/models/**/*.rb
    glob_model_files(db)
}

/// Find the inverse association
#[salsa::tracked]
pub fn inverse_of(
    db: &dyn Db,
    model: ModelFileInput,
    association: &AssociationDef,
) -> Option<AssociationDef> {
    let target_model_name = association.class_name();
    let target_model = find_model_by_name(db, &target_model_name)?;
    let target_associations = associations_for(db, target_model);

    // Find association pointing back to us
    target_associations
        .into_iter()
        .find(|a| a.class_name() == model.model_name(db) && a.foreign_key() == association.foreign_key())
}

/// Resolve polymorphic type set
#[salsa::tracked]
pub fn polymorphic_types(
    db: &dyn Db,
    model: ModelFileInput,
    association_name: &str,
) -> Vec<String> {
    // Find all models with `as: :association_name`
    all_models(db)
        .into_iter()
        .filter_map(|m| {
            let assocs = associations_for(db, m);
            assocs.into_iter().find(|a| a.as_option() == Some(association_name))
                .map(|_| m.model_name(db).to_string())
        })
        .collect()
}

/// Resolve STI type set
#[salsa::tracked]
pub fn sti_subclasses(db: &dyn Db, base_model: ModelFileInput) -> Vec<String> {
    let base_name = base_model.model_name(db);

    all_models(db)
        .into_iter()
        .filter_map(|m| {
            let ast = model_ast(db, m);
            if ast.parent_class() == Some(&base_name) {
                Some(m.model_name(db).to_string())
            } else {
                None
            }
        })
        .collect()
}

/// Build the full association graph
#[salsa::tracked]
pub fn association_graph(db: &dyn Db) -> AssociationGraph {
    let mut graph = AssociationGraph::new();

    for model in all_models(db) {
        let model_name = model.model_name(db);
        let associations = associations_for(db, model);

        for assoc in associations {
            graph.add_edge(
                &model_name,
                assoc.class_name(),
                assoc.clone(),
            );
        }
    }

    graph
}

/// Resolve through association chain
#[salsa::tracked]
pub fn through_chain(
    db: &dyn Db,
    model: ModelFileInput,
    association: &AssociationDef,
) -> Vec<AssociationDef> {
    let through = association.through_option()?;
    let graph = association_graph(db);

    // Walk the graph to find the chain
    graph.find_path(
        model.model_name(db),
        association.class_name(),
        &through,
    )
}
```

### Code Generation Queries

```rust
/// Generate Rust struct for a model
#[salsa::tracked]
pub fn rust_struct(db: &dyn Db, model: ModelFileInput, schema: SchemaInput) -> String {
    let model_name = model.model_name(db);
    let table_name = model_name.to_snake_case() + "s";  // Rails convention
    let columns = columns_for(db, schema, table_name);

    generate_struct(&model_name, &columns)
}

/// Generate association methods
#[salsa::tracked]
pub fn rust_associations(db: &dyn Db, model: ModelFileInput) -> String {
    let associations = associations_for(db, model);
    let mut code = String::new();

    for assoc in associations {
        match assoc.kind {
            AssociationKind::BelongsTo => {
                code.push_str(&generate_belongs_to(&assoc));
            }
            AssociationKind::HasMany => {
                code.push_str(&generate_has_many(&assoc));
            }
            AssociationKind::HasOne => {
                code.push_str(&generate_has_one(&assoc));
            }
            // ...
        }
    }

    code
}

/// Generate validation implementation
#[salsa::tracked]
pub fn rust_validations(db: &dyn Db, model: ModelFileInput) -> String {
    let validations = validations_for(db, model);
    generate_validatable_impl(&validations)
}

/// Generate callback implementation
#[salsa::tracked]
pub fn rust_callbacks(db: &dyn Db, model: ModelFileInput) -> String {
    let callbacks = callbacks_for(db, model);
    generate_callbacks_impl(&callbacks)
}

/// Generate complete model file
#[salsa::tracked]
pub fn rust_model_file(db: &dyn Db, model: ModelFileInput, schema: SchemaInput) -> String {
    let struct_code = rust_struct(db, model, schema);
    let assoc_code = rust_associations(db, model);
    let valid_code = rust_validations(db, model);
    let callback_code = rust_callbacks(db, model);

    format!(
        "{}\n\n{}\n\n{}\n\n{}",
        struct_code, assoc_code, valid_code, callback_code
    )
}
```

---

## Compilation Phases

### Phase 1: Input Collection

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ INPUT COLLECTION                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│ Static Mode:                                                                 │
│   • Read schema.rb or structure.sql                                          │
│   • Glob app/models/**/*.rb                                                  │
│   • Glob config/routes.rb                                                    │
│   • Glob app/controllers/**/*.rb                                             │
│                                                                              │
│ Snapshot Mode (additional):                                                  │
│   • Connect to database                                                      │
│   • Introspect tables, columns, types                                        │
│   • Query for polymorphic type sets                                          │
│   • Query for STI type sets                                                  │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Phase 2: Parsing

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ PARSING                                                                      │
├─────────────────────────────────────────────────────────────────────────────┤
│ For each model file:                                                         │
│   • Parse Ruby using ruby-prism                                              │
│   • Extract DSL calls: associations, validations, callbacks, enums, scopes   │
│   • Build ModelAst                                                           │
│                                                                              │
│ For schema:                                                                   │
│   • Parse schema.rb DSL or structure.sql DDL                                 │
│   • Extract: tables, columns, types, foreign keys, indexes                   │
│   • Build SchemaAst                                                          │
│                                                                              │
│ For routes:                                                                   │
│   • Parse config/routes.rb DSL                                               │
│   • Extract: resources, nested routes, member/collection actions             │
│   • Build RoutesAst                                                          │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Phase 3: Resolution

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ RESOLUTION (Multi-Pass)                                                      │
├─────────────────────────────────────────────────────────────────────────────┤
│ Build Association Graph:                                                     │
│   • Collect all associations from all models                                 │
│   • Build directed graph of relationships                                    │
│   • Detect cycles (allowed in Rails but need special handling)               │
│                                                                              │
│ Resolve Inverses:                                                            │
│   • For each belongs_to, find has_many/has_one on target                     │
│   • Match by FK column                                                       │
│   • Record inverse_of relationships                                          │
│                                                                              │
│ Resolve Polymorphic Types:                                                   │
│   • For each polymorphic: true association                                   │
│   • Find all models with matching as: option                                 │
│   • OR query database for DISTINCT type values                               │
│   • Build closed type set                                                    │
│                                                                              │
│ Resolve STI Types:                                                           │
│   • For each model with subclasses                                           │
│   • Find all models inheriting from it                                       │
│   • OR query database for DISTINCT type values                               │
│   • Build closed type set                                                    │
│                                                                              │
│ Resolve Through Chains:                                                      │
│   • For each has_many :through                                               │
│   • Walk association graph to find path                                      │
│   • Record JOIN chain                                                        │
│                                                                              │
│ Validate Consistency:                                                        │
│   • FK columns exist in schema                                               │
│   • Referenced classes exist                                                 │
│   • Counter cache columns exist                                              │
│   • Touch targets have updated_at                                            │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Phase 4: Code Generation

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ CODE GENERATION                                                              │
├─────────────────────────────────────────────────────────────────────────────┤
│ For each model:                                                              │
│   • Generate Rust struct with typed fields                                   │
│   • Generate Diesel table! macro                                             │
│   • Generate derive macros (Queryable, Insertable, etc.)                     │
│   • Generate DirtyTracking state struct                                      │
│   • Generate association methods                                             │
│   • Generate Validatable implementation                                      │
│   • Generate Callbacks implementation                                        │
│   • Generate Persistable implementation                                      │
│   • Generate enum types for enum columns                                     │
│   • Generate scope methods                                                   │
│                                                                              │
│ For polymorphic/STI:                                                         │
│   • Generate Rust enum with variants                                         │
│   • Generate dispatch methods                                                │
│                                                                              │
│ For routes:                                                                   │
│   • Generate Axum router                                                     │
│   • Generate handler stubs                                                   │
│                                                                              │
│ For project:                                                                  │
│   • Generate Cargo.toml                                                      │
│   • Generate main.rs                                                         │
│   • Generate lib.rs with module structure                                    │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Data Structures

### Model AST

```rust
/// Parsed model file
#[derive(Debug, Clone)]
pub struct ModelAst {
    pub name: String,
    pub parent_class: Option<String>,
    pub associations: Vec<AssociationDef>,
    pub validations: Vec<ValidationDef>,
    pub callbacks: Vec<CallbackDef>,
    pub enums: Vec<EnumDef>,
    pub scopes: Vec<ScopeDef>,
    pub store_accessors: Vec<StoreAccessorDef>,
    pub nested_attributes: Vec<NestedAttributesDef>,
    pub methods: Vec<MethodDef>,
}

/// Association definition
#[derive(Debug, Clone)]
pub struct AssociationDef {
    pub kind: AssociationKind,
    pub name: String,
    pub options: AssociationOptions,
}

#[derive(Debug, Clone)]
pub enum AssociationKind {
    BelongsTo,
    HasOne,
    HasMany,
    HasAndBelongsToMany,
    DelegatedType,
}

#[derive(Debug, Clone, Default)]
pub struct AssociationOptions {
    pub class_name: Option<String>,
    pub foreign_key: Option<String>,
    pub foreign_type: Option<String>,
    pub primary_key: Option<String>,
    pub polymorphic: bool,
    pub through: Option<String>,
    pub source: Option<String>,
    pub as_option: Option<String>,
    pub dependent: Option<DependentOption>,
    pub counter_cache: Option<CounterCacheOption>,
    pub touch: Option<TouchOption>,
    pub inverse_of: Option<String>,
    pub optional: bool,
    pub validate: bool,
    pub autosave: bool,
}

/// Validation definition
#[derive(Debug, Clone)]
pub struct ValidationDef {
    pub attributes: Vec<String>,
    pub validators: Vec<ValidatorDef>,
    pub condition: Option<ConditionDef>,
}

#[derive(Debug, Clone)]
pub enum ValidatorDef {
    Presence { options: PresenceOptions },
    Uniqueness { options: UniquenessOptions },
    Length { options: LengthOptions },
    Numericality { options: NumericalityOptions },
    Format { options: FormatOptions },
    Inclusion { options: InclusionOptions },
    Custom { class_name: String, options: HashMap<String, Value> },
}

/// Callback definition
#[derive(Debug, Clone)]
pub struct CallbackDef {
    pub timing: CallbackTiming,
    pub event: CallbackEvent,
    pub target: CallbackTarget,
    pub condition: Option<ConditionDef>,
}

#[derive(Debug, Clone)]
pub enum CallbackTarget {
    Method(String),
    Proc(String),  // Source code of proc (flagged)
}

#[derive(Debug, Clone)]
pub enum ConditionDef {
    Symbol(String),   // if: :method_name (compilable)
    Proc(String),     // if: -> { ... } (flagged)
}
```

### Schema AST

```rust
/// Parsed schema
#[derive(Debug, Clone)]
pub struct SchemaAst {
    pub tables: Vec<TableDef>,
    pub indexes: Vec<IndexDef>,
    pub foreign_keys: Vec<ForeignKeyDef>,
}

/// Table definition
#[derive(Debug, Clone)]
pub struct TableDef {
    pub name: String,
    pub columns: Vec<ColumnDef>,
    pub primary_key: String,
}

/// Column definition
#[derive(Debug, Clone)]
pub struct ColumnDef {
    pub name: String,
    pub sql_type: SqlType,
    pub nullable: bool,
    pub default: Option<DefaultValue>,
    pub array: bool,  // PostgreSQL arrays
}

#[derive(Debug, Clone)]
pub enum SqlType {
    Integer,
    BigInt,
    SmallInt,
    Float,
    Decimal { precision: Option<u8>, scale: Option<u8> },
    String { limit: Option<u32> },
    Text,
    Boolean,
    Date,
    Time,
    DateTime,
    Timestamp,
    Binary,
    Json,
    Jsonb,
    Uuid,
    Inet,
    Cidr,
    MacAddr,
    Enum { name: String, values: Vec<String> },  // PG enum
    Custom(String),
}
```

### Association Graph

```rust
/// Graph of model associations
#[derive(Debug, Clone)]
pub struct AssociationGraph {
    /// Adjacency list: model_name -> [(target_model, association)]
    edges: HashMap<String, Vec<(String, AssociationDef)>>,

    /// Reverse index: model_name -> models that reference it
    reverse_edges: HashMap<String, Vec<(String, AssociationDef)>>,
}

impl AssociationGraph {
    pub fn new() -> Self {
        Self {
            edges: HashMap::new(),
            reverse_edges: HashMap::new(),
        }
    }

    pub fn add_edge(&mut self, from: &str, to: &str, assoc: AssociationDef) {
        self.edges
            .entry(from.to_string())
            .or_default()
            .push((to.to_string(), assoc.clone()));

        self.reverse_edges
            .entry(to.to_string())
            .or_default()
            .push((from.to_string(), assoc));
    }

    /// Find associations from a model
    pub fn associations_from(&self, model: &str) -> &[(String, AssociationDef)] {
        self.edges.get(model).map(|v| v.as_slice()).unwrap_or(&[])
    }

    /// Find associations to a model (reverse lookup)
    pub fn associations_to(&self, model: &str) -> &[(String, AssociationDef)] {
        self.reverse_edges.get(model).map(|v| v.as_slice()).unwrap_or(&[])
    }

    /// Find inverse association
    pub fn find_inverse(&self, from: &str, assoc: &AssociationDef) -> Option<&AssociationDef> {
        let to = assoc.class_name();
        self.associations_from(&to)
            .iter()
            .find(|(target, a)| {
                target == from && a.foreign_key() == assoc.foreign_key()
            })
            .map(|(_, a)| a)
    }

    /// Find path for through association
    pub fn find_path(&self, from: &str, to: &str, through: &str) -> Option<Vec<AssociationDef>> {
        // BFS to find path from -> through -> to
        let step1 = self.associations_from(from)
            .iter()
            .find(|(target, _)| target == through)?;

        let through_model = &step1.0;
        let step2 = self.associations_from(through_model)
            .iter()
            .find(|(target, _)| target == to)?;

        Some(vec![step1.1.clone(), step2.1.clone()])
    }
}
```

---

## Error Handling

### Compilation Errors

```rust
/// Compiler error types
#[derive(Debug, Clone)]
pub enum CompileError {
    // Parse errors
    ParseError {
        file: PathBuf,
        line: usize,
        message: String,
    },

    // Resolution errors
    UnknownModel {
        referenced_by: String,
        model_name: String,
    },
    UnknownColumn {
        model: String,
        column: String,
    },
    MissingForeignKey {
        model: String,
        association: String,
        expected_column: String,
    },
    MissingCounterCache {
        model: String,
        expected_column: String,
    },
    UnresolvedPolymorphic {
        model: String,
        association: String,
    },
    CircularDependency {
        chain: Vec<String>,
    },

    // Proc embargo violations
    ProcCondition {
        model: String,
        location: String,
        proc_source: String,
    },
    DynamicClassname {
        model: String,
        association: String,
    },

    // Code generation errors
    TypeMismatch {
        model: String,
        column: String,
        expected: String,
        found: String,
    },
}

/// Compiler warnings (non-fatal)
#[derive(Debug, Clone)]
pub enum CompileWarning {
    // Patterns that work but are suboptimal
    MissingInverseOf {
        model: String,
        association: String,
    },
    DeprecatedPattern {
        model: String,
        pattern: String,
        suggestion: String,
    },

    // Flagged for manual review
    RuntimeValue {
        model: String,
        location: String,
        description: String,
    },
    DynamicScope {
        model: String,
        scope_name: String,
    },
    ComplexCallback {
        model: String,
        callback_name: String,
    },
}
```

---

## CLI Interface

```
rails-compile [OPTIONS] <COMMAND>

Commands:
  lint       Analyze Rails project and report compilability
  schema     Generate Rust structs from schema (Layer 0)
  models     Generate complete model files (Layers 0-2)
  full       Generate complete Rust project (Layers 0-4)
  verify     Compare Rails vs Rust behavior (semantic diff)

Options:
  --mode <MODE>        Compilation mode: static, snapshot [default: static]
  --db <URL>           Database URL (for snapshot mode)
  --output <DIR>       Output directory [default: ./rust_app]
  --verbose            Show detailed progress
  --strict             Treat warnings as errors

Examples:
  # Lint a Rails project
  rails-compile lint .

  # Generate from schema only
  rails-compile schema --output ./rust_app

  # Full compilation with database snapshot
  rails-compile full --mode snapshot --db postgres://localhost/myapp

  # Verify semantic equivalence
  rails-compile verify --rails-url http://localhost:3000 --rust-url http://localhost:8000
```

---

## Summary

### Why Query-Based?

1. **Handles cross-layer dependencies**: Queries can call other queries regardless of "layer"
2. **Incremental**: Only recompute what changed (important for large codebases)
3. **Debuggable**: Each query is a named, testable unit
4. **Parallel**: Independent queries can run in parallel

### The Query DAG

```
                         ┌───────────────────┐
                         │  rust_model_file  │
                         └─────────┬─────────┘
                                   │
        ┌──────────────────────────┼──────────────────────────┐
        │                          │                          │
┌───────┴───────┐        ┌─────────┴─────────┐      ┌─────────┴─────────┐
│  rust_struct  │        │ rust_associations │      │ rust_validations  │
└───────┬───────┘        └─────────┬─────────┘      └─────────┬─────────┘
        │                          │                          │
┌───────┴───────┐        ┌─────────┴─────────┐      ┌─────────┴─────────┐
│  columns_for  │        │ associations_for  │      │ validations_for   │
└───────┬───────┘        └─────────┬─────────┘      └─────────┬─────────┘
        │                          │                          │
        │                ┌─────────┴─────────┐                │
        │                │    inverse_of     │                │
        │                └─────────┬─────────┘                │
        │                          │                          │
┌───────┴───────┐        ┌─────────┴─────────┐      ┌─────────┴─────────┐
│    tables     │        │   model_ast (B)   │      │    model_ast      │
└───────┬───────┘        └─────────┬─────────┘      └─────────┬─────────┘
        │                          │                          │
┌───────┴───────┐        ┌─────────┴─────────┐      ┌─────────┴─────────┐
│ SchemaInput   │        │  ModelFileInput   │      │  ModelFileInput   │
└───────────────┘        └───────────────────┘      └───────────────────┘
     (input)                   (input B)                  (input A)
```

### Next Steps

- **Document 14**: Lint Tool Spec — What the lint tool reports
- **Document 15**: Semantic Diff Protocol — How to verify equivalence
