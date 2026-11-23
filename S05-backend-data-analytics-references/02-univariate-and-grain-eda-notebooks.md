# 02 · Univariate & Grain EDA Notebooks (Prompt Reference)

> **Purpose:** Standard Operating Procedure (SOP) for profiling real backend tables in reproducible Jupyter notebooks using Polars (primary) or Pandas—combining classic banking SAS EDA discipline (`PROC CONTENTS`, `PROC FREQ`, `PROC UNIVARIATE`, `PROC MEANS`) with strict primary-key, text-column, join-cardinality, and sampling verification.

## How to Use This Prompt Reference

Attach this file to any agent when inspecting an unfamiliar database table, validating a migration/backfill, debugging a join, or reviewing what actual data a backend service writes. To convert into a Claude or Codex skill later, wrap the 6-Cell Notebook SOP and Verification Gates in a thin `SKILL.md` pointing here.

---

## 1. Conditional Decision Matrix

| Situation / Condition | Use when… | Avoid when… | Primary Failure Mode if Ignored |
|---|---|---|---|
| **Polars vs. Pandas** | Use **Polars** (`pl.scan_parquet` / lazy frames) by default for tables > 500k rows, multi-file Parquet/CSV extracts, or memory-constrained laptops. Use **Pandas** only when a team's downstream plotting/modeling stack strictly requires it and data fits comfortably (< 20% RAM). | Avoid loading multi-GB CSVs eagerly into Pandas `read_csv` with default `object` dtypes; avoid mixing `None`, `np.nan`, and `pd.NA` without normalizing. | OOM crashes, silent `int64 → float64` precision loss on 18-digit IDs when a single NULL appears in Pandas, and 10×–30× slower profiling. |
| **Univariate profiling on *every* column** | Run an automated profiling pass over **100% of columns** (numeric, date/timestamp, boolean, categorical, and free text) before writing any `JOIN`, `WHERE`, or `GROUP BY`. | Avoid eyeballing `df.head(5)` and assuming the rest of the table looks the same. | Missing 98%-null columns, hidden sentinel values (`-999`, `1900-01-01`, `'UNKNOWN'`, `'null'`), or constant/zero-variance flags. |
| **Alphabetical sorting on text columns** | Always inspect **alphabetically sorted distinct values** (first N and last N) alongside top-K frequencies, length distribution, whitespace/casing normalization checks, and non-ASCII checks. | Avoid checking only `value_counts().head(10)` on text columns—rare garbage values sit at the alphabetical extremes (`""`, `" "`, `"---"`, `"N/A"`, `"NULL"`, `"test"`, `"zzz_do_not_use"`). | Silent category fragmentation (`"USD"`, `"usd"`, `" USD "`), test rows leaking into production metrics, and broken `WHERE status = 'ACTIVE'` filters. |
| **Primary key & uniqueness audit** | Prove primary key uniqueness on **100% of rows** (`n_rows == n_unique(pk)` AND `null_count(pk) == 0`) before every join or upsert. Test composite keys explicitly when no single column is unique. | Avoid trusting a column named `id`, `order_id`, or `customer_id`—or even a DB migration comment—without measuring uniqueness on actual rows. | Silent M:N fan-out that doubles or triples revenue, balances, or event counts without raising a SQL error. |
| **Join-cardinality & orphan check** | Measure left-key uniqueness, right-key uniqueness, match rate, unmatched left orphans, and `post_join_rows / pre_join_rows` ratio **before** aggregating. | Avoid running `LEFT JOIN` + `SUM()` directly without checking whether the right table has multiple rows per join key (e.g., SCD Type 2 history, multiple addresses, retry events). | Double counting measures when a 1:1 assumed join is actually 1:N or M:N; silent row loss on `INNER JOIN` when orphan keys exist. |
| **Data sampling** | Use **deterministic stratified or entity-hashed sampling** (e.g., `hash(customer_id) % 100 < 5`) when exploring huge tables (> 10M rows) for distribution shape or text patterns, keeping all rows for sampled entities together. | Avoid random row sampling when checking **primary-key uniqueness, join fan-out, orphan rates, or rare-tail fraud/error codes**—random row samples artificially hide duplicates and break referential integrity. | False confidence: a 1% random sample shows 0 duplicate keys on a table where 100% of keys have 2 duplicate rows (probability of sampling both halves is 0.01%). |

---

## 2. Classic Banking SAS EDA → Modern Polars / Pandas Mapping

Banking and risk analytics teams built decades of rigor around SAS profiling macros because a single bad join or uncleaned sentinel value distorts regulatory and financial totals. Preserve that exact discipline in Jupyter:

| Classic SAS Procedure | Question It Answers | Polars Equivalent | Pandas Equivalent |
|---|---|---|---|
| `PROC CONTENTS` | Physical schema, column order, exact data types, row count, storage size | `df.schema`, `df.shape`, `df.estimated_size("mb")` | `df.info(memory_usage="deep")`, `df.dtypes` |
| `PROC UNIVARIATE` | Numeric distribution: `N`, `NMISS`, `MEAN`, `STD`, `MIN`, `P1/P5/P25/P50/P75/P95/P99`, `MAX`, **5 lowest & 5 highest extreme values**, zero count, negative count | `df.select(pl.col(c).null_count(), ...)` + `sort().head(5)` / `tail(5)` | `s.describe(percentiles=[.01,.05,.25,.5,.75,.95,.99])` + `nsmallest(5)` / `nlargest(5)` |
| `PROC FREQ` | Categorical & text audit: distinct count, missing count, top-K frequencies + cumulative %, **alphabetically sorted head/tail values** | `df.group_by(c).len().sort("len", descending=True)` + `unique().sort()` | `s.value_counts(dropna=False)` + `s.dropna().sort_values().unique()` |
| `PROC MEANS` / `CLASS` | Grouped control totals (count, sum, min, max) by date/status/segment to verify conservation across steps | `df.group_by(grp).agg(pl.len(), pl.col(m).sum())` | `df.groupby(grp, dropna=False)[m].agg(["count", "sum"])` |
| `PROC SORT NODUPKEY DUPOUT=` | Exact primary-key uniqueness proof + isolated dump of offending duplicate rows | `df.filter(pl.struct(pk).is_duplicated())` | `df[df.duplicated(subset=pk, keep=False)]` |

### Anomaly Alert Taxonomy (Adapted from `ydata-profiling` + Banking Audits)
Flag any column triggering one of these alerts automatically in the notebook summary:
- `CONSTANT` (`n_unique <= 1`): dead feature or broken ETL default.
- `MISSING` (`null_pct > 0%` on required key, or `> 20%` on attribute).
- `ZEROS` / `NEGATIVES`: unexpected zeros or negative amounts in balances/quantities.
- `DUPLICATES` / `NEAR_DUPLICATES`: repeated PKs or identical rows after whitespace/case trimming.
- `HIGH_CARDINALITY`: text column unexpectedly near `n_rows` (possible unparsed JSON, free-text notes, or UUID disguised as category).
- `IMBALANCE` / `SKEWED`: single value > 95% of rows or extreme P99/P50 ratio.
- `DATE_GAPS` / `FUTURE_DATES`: missing calendar days in time series or timestamps > `now()`.

---

## 3. Standard 6-Cell Jupyter Notebook SOP

Every EDA notebook must be **re-runnable top-to-bottom (`Restart & Run All`)** with zero hidden state, fixed random/hash seeds, and read-only source queries:

1. **Cell 1 — Context & Snapshot Header:** Table/query name, source DB/environment, extraction timestamp, row/column count, and link to upstream backend code (from [01 · Backend Data Lineage & Contracts](01-backend-data-lineage-and-contracts.md)).
2. **Cell 2 — `PROC CONTENTS` Schema & Nulls Overview:** Every column's physical dtype, null count, null %, distinct count, and cardinality ratio (`n_unique / n_rows`).
3. **Cell 3 — `PROC UNIVARIATE` Numeric & Date Audit:** Min, P1, P5, P25, P50, P75, P95, P99, Max, zero/negative counts, 5 lowest & 5 highest values, date range, and missing-day gaps.
4. **Cell 4 — `PROC FREQ` Text & Categorical Audit (with Alphabetical Sort):** For every string column, print top-10 frequencies **and** first-10 / last-10 **alphabetically sorted** values, leading/trailing whitespace count, mixed-case collision count (`n_unique(raw) != n_unique(lower.strip)`), and empty/sentinel string count.
5. **Cell 5 — Primary-Key & Join-Cardinality Audit:** Prove declared PK uniqueness (dump top duplicate keys if any), verify candidate composite keys, and run the pre-join cardinality + orphan report for every planned join.
6. **Cell 6 — Findings, Data-Quality Alerts & Contract Action Items:** Bullet list of anomalies, owning backend file/service, and whether the table is safe for downstream analytics.

---

## 4. Runnable Polars Profiling & PK / Join-Cardinality Template

```python
import polars as pl

SENTINEL_STRINGS = {"", "n/a", "na", "null", "none", "unknown", "-", "--", "undefined"}


def profile_contents(df: pl.DataFrame) -> pl.DataFrame:
    """PROC CONTENTS + cardinality overview for every column."""
    n = df.height
    rows = []
    for col in df.columns:
        s = df[col]
        nulls = s.null_count()
        n_uniq = s.n_unique()
        rows.append(
            {
                "column": col,
                "dtype": str(s.dtype),
                "n_rows": n,
                "null_count": nulls,
                "null_pct": round(100.0 * nulls / n, 2) if n else 0.0,
                "n_unique": n_uniq,
                "unique_ratio": round(n_uniq / n, 4) if n else 0.0,
                "is_unique_no_nulls": (nulls == 0 and n_uniq == n),
            }
        )
    return pl.DataFrame(rows)


def profile_text_columns(df: pl.DataFrame, sample_k: int = 8) -> list[dict]:
    """PROC FREQ + alphabetical head/tail + whitespace/case/sentinel scan for all string columns."""
    reports = []
    for col, dtype in df.schema.items():
        if dtype not in (pl.String, pl.Utf8, pl.Categorical):
            continue
        s = df[col].cast(pl.String)
        non_null = s.drop_nulls()
        trimmed_lower = non_null.str.strip_chars().str.to_lowercase()

        sorted_vals = non_null.unique().sort().to_list()
        ws_dirty = int((non_null != non_null.str.strip_chars()).sum())
        case_ws_collisions = non_null.n_unique() - trimmed_lower.n_unique()
        sentinel_hits = int(trimmed_lower.is_in(list(SENTINEL_STRINGS)).sum())
        top_freq = (
            df.group_by(col)
            .len()
            .sort("len", descending=True)
            .head(sample_k)
            .to_dicts()
        )
        reports.append(
            {
                "column": col,
                "n_unique_raw": non_null.n_unique(),
                "n_unique_norm": trimmed_lower.n_unique(),
                "whitespace_dirty_rows": ws_dirty,
                "case_or_ws_collisions": case_ws_collisions,
                "sentinel_rows": sentinel_hits,
                "alpha_head": sorted_vals[:sample_k],
                "alpha_tail": sorted_vals[-sample_k:],
                "top_freq": top_freq,
            }
        )
    return reports


def audit_primary_key(df: pl.DataFrame, pk_cols: list[str]) -> dict:
    """PROC SORT NODUPKEY equivalent: prove PK uniqueness and isolate offending keys."""
    null_rows = df.filter(pl.any_horizontal([pl.col(c).is_null() for c in pk_cols])).height
    dup_rows = df.filter(pl.struct(pk_cols).is_duplicated())
    dup_key_count = dup_rows.select(pk_cols).n_unique() if dup_rows.height else 0
    return {
        "pk_cols": pk_cols,
        "total_rows": df.height,
        "null_key_rows": null_rows,
        "duplicate_rows": dup_rows.height,
        "duplicate_distinct_keys": dup_key_count,
        "is_valid_pk": (null_rows == 0 and dup_rows.height == 0),
        "sample_duplicates": dup_rows.head(10).to_dicts(),
    }


def audit_join_cardinality(
    left: pl.DataFrame, right: pl.DataFrame, on: list[str]
) -> dict:
    """Classify join as 1:1, 1:N, N:1, or M:N and measure orphan keys before joining."""
    l_unique = left.select(on).n_unique() == left.height and left.filter(
        pl.any_horizontal([pl.col(c).is_null() for c in on])
    ).height == 0
    r_unique = right.select(on).n_unique() == right.height and right.filter(
        pl.any_horizontal([pl.col(c).is_null() for c in on])
    ).height == 0

    if l_unique and r_unique:
        cardinality = "1:1"
    elif l_unique and not r_unique:
        cardinality = "1:N (FAN-OUT RISK on left measures)"
    elif not l_unique and r_unique:
        cardinality = "N:1 (safe lookup join)"
    else:
        cardinality = "M:N (SEVERE FAN-OUT / DOUBLE-COUNTING RISK)"

    left_orphans = left.join(right.select(on).unique(), on=on, how="anti").height
    joined_rows = left.join(right.select(on), on=on, how="left").height
    fanout_factor = round(joined_rows / left.height, 4) if left.height else 1.0

    return {
        "join_keys": on,
        "cardinality": cardinality,
        "left_rows": left.height,
        "right_rows": right.height,
        "left_orphans": left_orphans,
        "post_left_join_rows": joined_rows,
        "fanout_factor": fanout_factor,
    }
```

### Schema Enforcement with Pandera (Polars or Pandas)
Once EDA reveals the true contract, lock it into code with **lazy validation (`lazy=True`)** so a single check run reports *all* failing columns/rows instead of stopping at the first error (e.g., `pandera.polars.DataFrameSchema` with `unique=True`, `nullable=False`, `Check.isin(...)`, `Check.str_matches(...)`).

---

## 5. Sampling Rules: When Sampling Helps vs. When It Lies

- **Safe for sampling (entity-hashed or stratified):** checking text formatting patterns, inspecting numeric distribution shape/quantiles, prototyping notebook cells on a 100M-row table.
  - **Entity-hashed sampling recipe:** filter `WHERE MOD(ABS(HASH(customer_id)), 100) < 5` so every order/event for a sampled customer stays together—preserving intra-entity sequences and 1:N child relationships.
- **Unsafe for sampling (must run on 100% of rows in SQL or lazy Polars):**
  - Primary-key uniqueness (`COUNT(*) vs COUNT(DISTINCT pk)`).
  - Join fan-out / duplicate-key detection.
  - Referential integrity / orphan-key counts.
  - Control totals (`SUM(amount)`) and rare error/fraud codes.

---

## 6. Failure Modes & Anti-Patterns

- **Inspecting only `.head()` or `value_counts().head(10)`:** Misses garbage values at alphabetical extremes (`""`, `" "`, `"NULL"`, `"zzz_test"`).
- **Pandas silent ID corruption:** Reading a nullable 64-bit integer ID column into Pandas turns `int64` into `float64`, silently rounding IDs above \(2^{53}\) (`9,007,199,254,740,992`) and creating fake duplicate keys. Use Polars `Int64`/`String` or Pandas nullable `Int64`/`string`.
- **Nulls in composite join keys:** In SQL, `NULL = NULL` evaluates to `UNKNOWN` (rows fail to join), whereas some DataFrame tools treat `NaN == NaN` or `null == null` differently (`join_nulls=False` default in Polars). Always audit `null_count` on every join key first.
- **Mutating notebooks out of order:** Running cells non-sequentially hides broken assumptions; every EDA notebook must pass `Restart & Run All`.

---

## 7. Verification Gates

Before using a table in a backend feature, migration, or analytics query, confirm:
1. `profile_contents(df)` ran on **all columns** with zero unexplained `CONSTANT` or high-`MISSING` columns.
2. `profile_text_columns(df)` checked **alphabetical head/tail**, whitespace, casing collisions, and sentinel strings on every string column.
3. `audit_primary_key(df, pk)` ran on **100% of rows** (not a random sample) and confirmed `is_valid_pk == True`, or documented the true composite grain.
4. `audit_join_cardinality(left, right, on)` confirmed `fanout_factor == 1.0` (1:1 or N:1) before any downstream aggregation, or handed off to [03 · Analytics Aggregations & Metric Verification](03-analytics-aggregations-and-metric-verification.md) to pre-aggregate before joining.
