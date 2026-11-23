# 01 · Backend Data Lineage & Contracts (Prompt Reference)

> **Purpose:** Map every database, table, column, external API, config binding, and transformation a backend codebase depends on—starting with `codebase-memory-mcp` for structural code intelligence and handing off to SQL/schema/contract tooling where static code graphs stop.

## How to Use This Prompt Reference

Attach this file to any coding agent (Claude, Codex, Devin, Cursor) when onboarding onto a backend service, auditing a schema or API change, or building a data-dependency inventory. To turn it into an auto-triggered Claude/Codex skill later, wrap the Quick SOP and Verification Gates in a thin `SKILL.md` that points here.

---

## 1. Conditional Decision Matrix

| Situation / Condition | Use when… | Avoid when… | Primary Failure Mode if Ignored |
|---|---|---|---|
| **Code-to-query & cross-service discovery** | Use `codebase-memory-mcp` (`index_repository` → `get_graph_schema` → `search_graph` / `trace_path` / `query_graph`) first on any repo > 20 files. | Avoid grepping file-by-file before indexing; avoid relying on `codebase-memory-mcp` alone to parse raw SQL strings into relational column lineage. | Missing indirect callers, background workers, or cross-service `HTTP_CALLS` / `ASYNC_CALLS`; burning 10× tokens on blind reads. |
| **SQL column-level lineage** | Use `sqlglot.lineage.lineage(col, sql, schema=...)` with an explicit table/column schema dictionary extracted from migrations or `information_schema`. | Avoid running static SQL lineage *without* a schema when queries contain `SELECT *`, unqualified columns, or dialect-specific casts. | Silent resolution failure or dropped upstream columns on `SELECT *` and multi-CTE views. |
| **Direct vs. indirect column dependencies** | Track **both** direct (`SELECT` projections/transforms) and dataset-level indirect (`WHERE`, `JOIN`, `GROUP BY`, `WINDOW`, soft-delete `deleted_at IS NULL`, tenant filters) columns (OpenLineage model). | Avoid recording only `SELECT` columns as "used columns". | Dropping or mutating a filter/join column (e.g., `status`, `is_active`, `deleted_at`) breaks row population and downstream KPIs even though the column never appears in `SELECT`. |
| **ORM / dynamic query builders** | Combine `codebase-memory-mcp` `trace_path(mode="data_flow")` on ORM models/repositories with runtime query logs (`pg_stat_statements`, slow-query log, or test-suite SQL capture). | Avoid trusting static AST parsing alone when SQL is assembled dynamically from request params, ActiveRecord/SQLAlchemy scopes, or string interpolation. | Invisible tables/columns touched only under specific runtime flags or default ORM scopes. |
| **External APIs as data sources** | Trace outbound clients via `HTTP_CALLS`, `ASYNC_CALLS`, `CONFIGURES` (env vars/URLs), and `CONNECTS_TO` edges, then record payload schema, idempotency key, rate limit, and fallback behavior. | Avoid treating third-party webhooks/APIs as "pure backend glue" outside the data inventory. | Unversioned external enum changes, silent null fields, or duplicate webhook deliveries corrupting downstream warehouse tables. |
| **Schema & semantic contracts** | Define executable contracts (Open Data Contract Standard / `datacontract-cli`) for every table or event stream consumed outside the owning service—covering physical type, `primaryKey`, `unique`, `required`, allowed `enum` values, PII tags, and freshness SLAs. | Avoid relying on prose wikis or ORM model comments as contracts; avoid adding heavy contract YAML to strictly internal scratch tables with no external readers. | Silent semantic drift: column keeps type `VARCHAR` or `INT`, but meaning changes (e.g., cents → dollars, UTC → local time, new enum state) and breaks analytics without throwing a DB error. |

---

## 2. Essential Tool Backbone: `codebase-memory-mcp`

`codebase-memory-mcp` builds a persistent local SQLite knowledge graph over 164 tree-sitter grammars plus Hybrid LSP type resolution (Python, TS/JS, Go, Java, Kotlin, Rust, C#, PHP, etc.). Use it as **Step 1** of every backend data audit.

### Standard `codebase-memory-mcp` Discovery Sequence

1. **Index the repository** (use async mode on large repos so MCP clients do not time out):
   - Small/medium repo: `index_repository(repo_path="/abs/path/to/repo")`
   - Large repo: `index_repository(repo_path="/abs/path/to/repo", async=True)` then poll `index_repository(repo_path="/abs/path/to/repo", status=True)` until `state == "succeeded"`.
2. **Inspect the graph schema and architecture first**:
   - `get_graph_schema` — see exact node labels, edge types, and counts before writing queries.
   - `get_architecture` — identify packages, HTTP routes, hotspots, and existing ADRs.
3. **Locate all data touchpoints** using `search_graph` (structural regex + BM25 + `semantic_query`):
   - Models/entities, repository/DAO classes, migrations, SQL files, ORM hooks, serializers, external HTTP clients, queue producers/consumers.
4. **Trace callers, data flows, and service boundaries** with `trace_path` (alias `trace_call_path`, depth 1–15):
   - `mode="calls"` — who invokes a repository method, migration helper, or serializer?
   - `mode="data_flow"` — arg-to-param + field access chains (`DATA_FLOWS` edges) showing how a field mutates from HTTP request → domain logic → DB write (or DB read → API response / event payload).
   - `mode="cross_service"` — cross-service `HTTP_CALLS` and `ASYNC_CALLS` edges.
   - `mode="run"` / `mode="topology"` — connect Kubernetes/Compose services and env vars (`CONFIGURES`, `CONNECTS_TO`) to the exact code reading DB connection strings and API hosts.
5. **Query the graph directly with Cypher (`query_graph`, read-only)** to build the dependency inventory:

```cypher
-- 1. Find all functions reading database/API config env vars
MATCH (f)-[:CONFIGURES]->(e)
WHERE e.name =~ '(?i).*(DB|DATABASE|POSTGRES|MYSQL|SNOWFLAKE|REDIS|KAFKA|API_URL).*'
RETURN f.file, f.name, e.name
LIMIT 100

-- 2. Find outbound HTTP / async calls from backend handlers or workers
MATCH (src)-[r:HTTP_CALLS|ASYNC_CALLS|EMITS]->(dst)
RETURN src.file, src.name, type(r), dst.name
LIMIT 100

-- 3. Trace data-flow chains from a model or repository symbol
MATCH (a)-[r:DATA_FLOWS]->(b)
WHERE a.name =~ '(?i).*(Order|Account|Ledger|Repository|Query).*'
RETURN a.file, a.name, b.file, b.name
LIMIT 100
```

6. **Audit a pending change's blast radius**:
   - Run `detect_changes` on a git diff to list every affected symbol and downstream caller before touching a schema, serializer, or query.
   - Use `get_code_snippet` only for the specific symbols surfaced by the graph—never dump whole directories into context.

### Explicit Handoff Boundary (What `codebase-memory-mcp` Does *Not* Do)

`codebase-memory-mcp` maps **code symbols, intra-code `DATA_FLOWS`, config/env bindings, and cross-service edges**. It does **not**:
- Parse SQL strings inside Python/Go/Rust/JS into relational `table.column → output_column` DAGs.
- Resolve `SELECT *` against a live database catalog.
- Verify whether a declared foreign key or unique constraint actually holds in production data.

Hand off from `codebase-memory-mcp` to **Section 3 (SQL & Schema Lineage)** and **Reference 02 (Univariate & Grain EDA Notebooks)** at every database boundary.

---

## 3. Relational Column Lineage & Transformation Inventory

### Required Output Artifact: Backend Data Dependency Matrix

For any service or feature under audit, produce a single table (Markdown or CSV) with **one row per `(file, symbol, dependency_kind, target_object, column_or_field)`**:

| Field | Required Values / Notes |
|---|---|
| `source_file` & `symbol` | Exact path + function/class from `codebase-memory-mcp` |
| `dependency_kind` | `db_read`, `db_write`, `db_migration`, `external_api_read`, `external_api_write`, `event_emit`, `event_consume`, `file_or_blob` |
| `system` / `database` / `schema` | Logical DB or external service name (traced via `CONFIGURES` / `CONNECTS_TO` env vars, never hard-coded secrets) |
| `table_or_endpoint` | Physical table/view name, topic name, or `METHOD /path` |
| `columns_or_fields` | Explicit list—expand `SELECT *` using the schema catalog |
| `lineage_role` | `DIRECT` (`IDENTITY`, `TRANSFORMATION`, `AGGREGATION`, `MASKING`) vs. `INDIRECT` (`JOIN`, `FILTER`, `GROUP_BY`, `SORT`, `WINDOW`) |
| `transformation_summary` | Unit conversions, currency scaling, timezone shifts, coalescing, enum mapping, soft-delete filtering |
| `evidence_source` | `static_graph`, `sqlglot_ast`, `migration_ddl`, `runtime_query_log`, `live_catalog` |

### Extracting Column Lineage with `sqlglot` (Schema-Backed)

Always supply the table schema dictionary (from migrations or `information_schema.columns`) so `SELECT *` and unqualified column names resolve deterministically:

```python
import sqlglot
from sqlglot.lineage import lineage

schema = {
    "orders": {
        "order_id": "BIGINT",
        "customer_id": "BIGINT",
        "amount_cents": "BIGINT",
        "status": "VARCHAR",
        "deleted_at": "TIMESTAMP",
    },
    "customers": {
        "customer_id": "BIGINT",
        "country_code": "VARCHAR",
    },
}

sql = """
WITH valid_orders AS (
    SELECT order_id, customer_id, amount_cents / 100.0 AS amount_usd
    FROM orders
    WHERE deleted_at IS NULL AND status = 'PAID'
)
SELECT c.country_code, SUM(v.amount_usd) AS gross_revenue_usd
FROM valid_orders v
JOIN customers c ON c.customer_id = v.customer_id
GROUP BY c.country_code
"""

# 1. Direct column lineage for an output metric
node = lineage("gross_revenue_usd", sql, schema=schema, dialect="postgres")
direct_sources = [n.name for n in node.walk() if n.downstream == []]

# 2. Indirect (dataset-level) columns: WHERE, JOIN, GROUP BY
ast = sqlglot.parse_one(sql, dialect="postgres")
indirect_cols = set()
for clause in (sqlglot.exp.Where, sqlglot.exp.Join, sqlglot.exp.Group):
    for block in ast.find_all(clause):
        for col in block.find_all(sqlglot.exp.Column):
            indirect_cols.add(col.sql())

print("DIRECT:", direct_sources)
print("INDIRECT:", sorted(indirect_cols))
```

### Runtime Verification (Closing the Dynamic-SQL Gap)

Static analysis misses runtime-constructed queries, ORM default scopes, DB triggers, and views created outside the repo. Under high-impact changes (migrations, deprecations, backfills), cross-check the static inventory against:
- **Postgres:** `pg_stat_statements` + `information_schema.views` + `pg_trigger`
- **MySQL:** `performance_schema.events_statements_summary_by_digest`
- **ORM test suite:** enable SQL query logging during integration tests and diff touched tables/columns against the static matrix.

---

## 4. Data Contracts at Service & Table Boundaries

Adopt the **Open Data Contract Standard (ODCS)** mindset (e.g., `datacontract-cli`) for every table or event stream shared with data engineering or analytics:

### What Every Shared Table Contract Must Pin
1. **Identity & grain:** exact primary key (single or composite) and what one row represents in plain English (e.g., *"one row per settled order line item, immutable after settlement"*).
2. **Physical + semantic types:** not just `BIGINT` or `VARCHAR`, but unit (`amount_cents` vs. `amount_usd`), timezone (`UTC` ISO-8601), and nullability (`required: true`).
3. **Domain values & sentinel policy:** explicit `enum` list; forbid undocumented sentinels (`-1`, `9999-12-31`, `'N/A'`, `''`).
4. **Mutation & deletion semantics:** append-only ledger vs. in-place `UPDATE` vs. soft delete (`deleted_at`) vs. hard `DELETE` (critical for CDC and incremental warehouse loads).
5. **Freshness, volume & ownership:** expected update cadence, row-count floor, PII classification, and owning team.

### Breaking vs. Non-Breaking Contract Changes

| Change | Safe (Non-Breaking) | Breaking (Requires Versioned Migration / Dual-Write) |
|---|---|---|
| Columns | Adding a nullable column or optional JSON field | Dropping, renaming, narrowing type, or making nullable → non-null without backfill |
| Semantics | Adding a new enum value *only if* consumers have an explicit unknown-value handler | Reusing an enum code for a new meaning; changing currency/unit scale; changing timezone |
| Deletions | Adding a `deleted_at` timestamp column while keeping existing filters documented | Switching from soft delete to hard `DELETE` (breaks incremental syncs that don't run CDC deletes) |
| Grain | Adding a separate child table with FK to parent PK | Changing a table's primary key or allowing duplicate rows on a previously unique key |

---

## 5. Failure Modes & Anti-Patterns

- **The "SELECT-only lineage" blind spot:** Auditing only `SELECT` columns and missing `WHERE deleted_at IS NULL` or `JOIN` keys; downstream counts silently shift when filter semantics change.
- **Treating ORM models as ground truth:** Migrations, manual hotfixes, DB views, and raw SQL bypass ORM classes; always reconcile code models against live `information_schema` / migrations.
- **Unresolved `SELECT *` in views or services:** Adding or reordering columns upstream breaks positional consumers and hides column dependencies from static scans.
- **Implicit timezone / unit assumptions:** Storing `created_at` without timezone or mixing `amount_cents` with decimal `amount` across services causes off-by-100× or day-boundary attribution errors in analytics.
- **Hard-coding credentials in lineage scripts:** Trace DB/API targets via `CONFIGURES` env var names, never embed connection secrets in repo files or notebooks.

---

## 6. Verification Gates

Before declaring a backend data-lineage or contract audit complete, verify:

1. **Graph coverage:** `codebase-memory-mcp` `check_index_coverage` reports no unindexed source gaps in the target service directories.
2. **Direct + indirect completeness:** Every touched table/endpoint has both `DIRECT` (projected/written) and `INDIRECT` (`WHERE`/`JOIN`/`GROUP BY`) columns listed with evidence source (`static_graph`, `sqlglot_ast`, or `runtime_query_log`).
3. **Zero unresolved `SELECT *`:** Every `SELECT *` in critical queries/views is expanded against the schema catalog.
4. **Contract check:** For shared tables, primary key, nullability, enum domain, and deletion semantics are verified against live data (hand off to [02 · Univariate & Grain EDA Notebooks](02-univariate-and-grain-eda-notebooks.md)) or `datacontract test`.
5. **Blast radius reviewed:** `detect_changes` (plus downstream warehouse/dashboard search) confirms no unnotified consumer breaks.
