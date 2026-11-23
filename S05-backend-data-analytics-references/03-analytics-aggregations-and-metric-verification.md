# 03 · Analytics Aggregations & Metric Verification (Prompt Reference)

> **Purpose:** Connect backend table changes directly to the aggregations, rollups, and KPIs they produce—preventing join fan-out double counting, semi-additive balance errors, and silent metric regressions through control-total reconciliation and before/after notebook diffs.

## How to Use This Prompt Reference

Attach this file to any coding agent when designing a reporting query, adding a dashboard metric, refactoring a backend schema/service that feeds analytics, or reconciling numbers between an operational database and a warehouse. To convert into a Claude or Codex skill later, wrap the Additivity Rules, Fan-Out Prevention Pattern, and Reconciliation Gates in a thin `SKILL.md` pointing here.

---

## 1. Conditional Decision Matrix

| Situation / Condition | Use when… | Avoid when… | Primary Failure Mode if Ignored |
|---|---|---|---|
| **Additive measures** (e.g., `order_amount`, `units_sold`, `fee_cents`) | `SUM()` freely across **all** dimensions (time, customer, region, product) **only after** verifying the query grain matches the fact table's primary key (`fanout_factor == 1.0`). | Avoid summing an additive measure after joining to a 1:N child table (e.g., `orders` joined to `order_items` or `payments`). | Silent 2×–10× double counting of order-level totals (shipping, tax, order revenue). |
| **Semi-additive measures** (e.g., `account_balance`, `inventory_on_hand`, `active_subscribers`) | `SUM()` across non-time dimensions (accounts, branches, products), but take a **point-in-time snapshot** (`MAX`/`MIN` on time dimension per entity—MetricFlow `non_additive_dimension` pattern) across time. | Avoid `SUM(account_balance)` across multiple days/months. | Summing daily snapshots reports 30× the actual monthly deposits or inventory. |
| **Non-additive measures** (e.g., `average_order_value`, `conversion_rate`, `distinct_active_users`, `unit_price`) | Always compute from **additive numerator and denominator** (`SUM(revenue) / COUNT(DISTINCT order_id)`) at the final aggregation grain; never average pre-computed averages. | Avoid `AVG(daily_avg_price)` or `SUM(daily_unique_users)` across periods. | Simpson's paradox / unweighted-average distortion and inflated distinct user counts across days. |
| **Joining two fact tables at different grains** (e.g., `orders` + `payments` or `shipments`) | **Pre-aggregate each fact table to the shared grain first** (e.g., `payments_by_order` with unique `order_id`), then join 1:1 or N:1 (`FOREIGN → PRIMARY/UNIQUE` per MetricFlow entity rules). | Avoid joining two 1:N child tables directly on a shared parent key (`order_items JOIN payments ON order_id`). | Cartesian M:N explosion (`items × payments` rows per order) silently inflating both item and payment sums. |
| **Late-arriving, cancelled, or refunded records** | Explicitly define the **time anchor** (`event_time` vs. `settled_at` vs. `ingested_at`) and **cancellation rule** (net vs. gross, separate refund ledger rows vs. status flip). | Avoid mixing `created_at` in one metric and `updated_at` in another without documenting the attribution boundary. | Historical numbers "drift" retroactively every day, breaking finance reconciliation against prior closes. |
| **Verifying a backend change's analytics impact** | Run a **control-total reconciliation** and **before/after notebook diff** comparing row counts, null counts, and grouped totals by `(date, status, segment)` before shipping. | Avoid declaring a backend refactor "analytics-safe" just because unit tests pass. | Unit tests pass on mocked single-row fixtures while production rollups silently diverge by 3% on edge-case states. |

---

## 2. Entity Grain & Fan-Out Prevention (MetricFlow Discipline)

Before writing any aggregation over joined tables, classify every join key using the four entity roles:
- **`PRIMARY`:** uniquely identifies one row in this table (no nulls, no duplicates).
- **`UNIQUE`:** alternate unique key (no nulls, no duplicates).
- **`FOREIGN`:** references a `PRIMARY` or `UNIQUE` key in another table (duplicates expected).
- **`NATURAL`:** domain key that may repeat across time (e.g., SCD Type 2 history rows).

**Safe Join Rule:**
- `FOREIGN → PRIMARY/UNIQUE` (N:1) and `PRIMARY → PRIMARY` (1:1) preserve the left table's grain (`fanout_factor == 1.0`).
- `PRIMARY → FOREIGN` (1:N), `FOREIGN → FOREIGN` (M:N), and `ANY → NATURAL` **break grain**. Never aggregate left-side measures after such a join—**pre-aggregate the right table to `PRIMARY` grain first**, then join.

---

## 3. Control-Total Reconciliation & Before/After Metric Diffing

Every aggregation pipeline or backend refactor touching data must pass **two conservation invariants**:

1. **Row-count conservation:**
   `input_rows == matched_rows + explicitly_filtered_rows + orphan_rows`
   Every dropped or added row must have a named reason (e.g., `deleted_at IS NOT NULL`, `status = 'CANCELLED'`), never silent `INNER JOIN` loss or fan-out multiplication.
2. **Control-total conservation:**
   `SUM(source_measure) == SUM(output_measure)` (within stated rounding tolerance, e.g., `$0.01`) across the full dataset and per major partition (`date`, `currency`, `status`).

### Runnable Polars Fan-Out Trap & Reconciliation Template

```python
import polars as pl


def aggregate_safely_with_reconciliation(
    orders: pl.DataFrame,
    payments: pl.DataFrame,
    join_key: str = "order_id",
    order_measure: str = "order_total_cents",
    payment_measure: str = "paid_cents",
) -> dict:
    """Demonstrates fan-out detection, pre-aggregation fix, and control-total reconciliation."""
    # 1. Source control totals (ground truth before any join)
    expected_orders = orders.height
    expected_order_total = int(orders[order_measure].sum())
    expected_paid_total = int(payments[payment_measure].sum())

    # 2. Naive join (what breaks when an order has multiple partial payments)
    naive = orders.join(payments, on=join_key, how="left")
    naive_order_total = int(naive[order_measure].sum())
    naive_fanout = round(naive.height / expected_orders, 4) if expected_orders else 1.0

    # 3. Safe pattern: pre-aggregate child table to parent PK grain first
    payments_at_order_grain = payments.group_by(join_key).agg(
        pl.col(payment_measure).sum().alias(payment_measure),
        pl.len().alias("payment_count"),
    )
    safe = orders.join(payments_at_order_grain, on=join_key, how="left").with_columns(
        pl.col(payment_measure).fill_null(0),
        pl.col("payment_count").fill_null(0),
    )

    safe_order_total = int(safe[order_measure].sum())
    safe_paid_total = int(safe[payment_measure].sum())
    orphan_payments = payments.join(orders.select(join_key).unique(), on=join_key, how="anti")
    orphan_paid_total = int(orphan_payments[payment_measure].sum()) if orphan_payments.height else 0

    return {
        "naive_fanout_factor": naive_fanout,
        "naive_double_counted_delta": naive_order_total - expected_order_total,
        "safe_row_conservation_ok": (safe.height == expected_orders),
        "safe_order_total_ok": (safe_order_total == expected_order_total),
        "safe_paid_reconciles_with_orphans": (
            safe_paid_total + orphan_paid_total == expected_paid_total
        ),
        "orphan_payment_rows": orphan_payments.height,
        "orphan_paid_cents": orphan_paid_total,
    }


def semi_additive_period_end_balance(
    daily_balances: pl.DataFrame,
    entity_col: str = "account_id",
    date_col: str = "as_of_date",
    balance_col: str = "balance_cents",
) -> int:
    """MetricFlow non_additive_dimension (window_choice=MAX): latest balance per entity, then sum."""
    latest_per_entity = (
        daily_balances.sort(date_col)
        .group_by(entity_col)
        .agg(pl.col(balance_col).last().alias(balance_col))
    )
    return int(latest_per_entity[balance_col].sum())


def diff_metric_snapshots(
    before: pl.DataFrame,
    after: pl.DataFrame,
    grain_cols: list[str],
    metric_col: str,
    tol: float = 1e-6,
) -> pl.DataFrame:
    """Before/after notebook diff for backend changes feeding analytics."""
    joined = before.join(
        after, on=grain_cols, how="full", coalesce=True, suffix="_after"
    ).with_columns(
        pl.col(metric_col).fill_null(0.0).alias("before_val"),
        pl.col(f"{metric_col}_after").fill_null(0.0).alias("after_val"),
    ).with_columns(
        (pl.col("after_val") - pl.col("before_val")).alias("abs_diff"),
    )
    return joined.filter(pl.col("abs_diff").abs() > tol).sort("abs_diff", descending=True)
```

---

## 4. Failure Modes & Anti-Patterns

- **The "it looked close enough" trap:** A 1.5% fan-out from rare multi-payment orders hides inside noisy daily revenue charts until an external audit catches it months later. Always assert exact control-total equality.
- **Summing semi-additive balances across time:** Running `SUM(balance)` over a daily snapshot table without windowing to the period-end (`MAX(date)`) per account.
- **Averaging averages (`AVG(daily_avg)`):** Weights a 5-order Sunday equally with a 5,000-order Monday; always preserve numerator and denominator separately.
- **`INNER JOIN` hiding orphan facts:** Dropping orphan payments/refunds silently instead of counting them in a reconciliation line (`orphan_payment_rows`, `orphan_paid_cents`).
- **Floating-point money accumulation:** Summing binary `float64` dollars across millions of rows introduces cent drift; store and aggregate money as integer minor units (`amount_cents` / `BIGINT`) or exact `Decimal`.
- **Unbounded `COUNT(DISTINCT ...)` in streaming/sampled pipelines:** Sampling breaks exact distinct counts; state whether a metric is exact or HyperLogLog-approximated.

---

## 5. Verification Gates

Before shipping any analytics query, rollup table, or backend change that feeds metrics:
1. **Grain statement written:** Every output table/query declares its exact primary key (one row = what entity/time grain) and passes `audit_primary_key` from [02 · Univariate & Grain EDA Notebooks](02-univariate-and-grain-eda-notebooks.md).
2. **Additivity classified:** Every measure is labeled `additive`, `semi-additive` (with explicit `MIN`/`MAX` time window rule), or `non-additive` (numerator + denominator specified).
3. **Conservation checks pass:** `safe_row_conservation_ok == True`, `safe_order_total_ok == True`, and any orphan/filtered rows are explicitly accounted for in the control-total ledger.
4. **Before/after diff reviewed:** `diff_metric_snapshots` on a representative historical window returns zero unexplained diffs (every non-zero row has an approved business reason).
5. **Lineage & contract synced:** Downstream metric dependencies are recorded back in the service's dependency matrix ([01 · Backend Data Lineage & Contracts](01-backend-data-lineage-and-contracts.md)).
