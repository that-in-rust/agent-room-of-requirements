# J02 · Bridging Backend Engineering, Data Engineering, and Analytics

## The story in short

**Backend code is not just HTTP handlers and services—it is the upstream producer of every table, contract, and metric the business relies on.** Most backend workflows stop at unit tests and ORM models, leaving column-level lineage, primary-key grain, dirty text values, and join fan-out invisible until dashboards break weeks later.

To close that gap, [S05 · Backend, Data Engineering & Analytics Prompt References](../S05-backend-data-analytics-references/README.md) adds three tool-agnostic Prompt Reference files built around a three-layer chain: **`codebase-memory-mcp`** for structural code/service discovery, **SQL/schema/contract tooling** (`sqlglot`, OpenLineage, Open Data Contracts) for direct and indirect column lineage, and **Jupyter + Polars/Pandas notebooks** modeled on classic banking SAS EDA (`PROC CONTENTS`, `PROC FREQ`, `PROC UNIVARIATE`, `PROC MEANS`).

---

## Why Prompt References first (instead of packaged skills)

1. **Tool-agnostic for workshops:** Prompt References attach directly to Claude, Codex, Devin, or Cursor without client-specific packaging or frontmatter constraints.
2. **Full conditional density:** They follow the [A02](../A02-Mega-Idiomatic-Prompt.md) conditional-guidance format (*under condition X do Y; under condition Z avoid Y*) with runnable Cypher and Polars/Pandas recipes.
3. **Lossless conversion later:** Any team that wants auto-triggering can wrap a Prompt Reference in a thin Claude or Codex `SKILL.md` using [Authoring Skills and References](../S01-skills-for-engineering-teams/authoring-skills-and-references/SKILL.md).

---

## The three-layer architecture

| Layer | Reference | Core toolset | What it proves |
|---|---|---|---|
| **1. Code & Service Graph + Contracts** | [01 · Backend Data Lineage & Contracts](../S05-backend-data-analytics-references/01-backend-data-lineage-and-contracts.md) | `codebase-memory-mcp`, `sqlglot`, OpenLineage taxonomy, `datacontract-cli` (ODCS) | Which files, symbols, env vars, and external APIs touch each database, table, and column—both `DIRECT` (`SELECT`) and `INDIRECT` (`WHERE`/`JOIN`/`GROUP BY`). |
| **2. Univariate & Grain EDA** | [02 · Univariate & Grain EDA Notebooks](../S05-backend-data-analytics-references/02-univariate-and-grain-eda-notebooks.md) | Jupyter, Polars / Pandas, Pandera, SAS banking EDA equivalents | Every column profiled (including alphabetically sorted text columns for dirty/sentinel values), primary-key uniqueness proven on 100% of rows, join cardinality (`1:1`, `1:N`, `M:N`) measured before aggregating, and safe sampling boundaries enforced. |
| **3. Analytics Aggregations & Reconciliation** | [03 · Analytics Aggregations & Metric Verification](../S05-backend-data-analytics-references/03-analytics-aggregations-and-metric-verification.md) | Polars / Pandas, SQL, MetricFlow entity/additivity rules | Additive vs. semi-additive (point-in-time balance windowing) vs. non-additive (numerator/denominator) rules, pre-aggregation before 1:N joins, row-count and control-total conservation, and before/after metric diffs. |

---

## How this expansion was built and verified

1. **Executable spec first:** Driven by the repository's own [Executable Specs](../S01-skills-for-engineering-teams/executable-specs/SKILL.md) skill (`STUB → RED → GREEN → REFACTOR → VERIFY`).
2. **Two separate knowledge sources:** First-principles engineering judgment combined with direct pattern extraction from open-source reference repos (`DeusData/codebase-memory-mcp`, `tobymao/sqlglot`, `OpenLineage`, `datacontract-cli`, `pandera`, `ydata-profiling`, `metricflow`) cloned into gitignored `/ignore-repos/` plus banking SAS EDA literature—synthesized in original prose per the repository's licensing policy.
3. **Executable verification:** Runnable Polars profiling, primary-key, fan-out, and reconciliation code verified against dirty synthetic fixtures, alongside `S03-how-to-use-skills/check.py` link and index checks.
