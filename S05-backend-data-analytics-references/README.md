# S05 · Backend, Data Engineering & Analytics Prompt References

Agent-agnostic **Prompt Reference** files for the boundary where backend code becomes data tables, contracts, and analytics metrics.

Unlike `S01` (packaged skills), these files are written as direct **Prompt References** in the [A02](../A02-Mega-Idiomatic-Prompt.md) conditional-guidance style (*under condition X do Y; under condition Z avoid Y*). Attach any file directly to Claude, Codex, Devin, or Cursor during a workshop or engineering session—or wrap it into a thin Claude/Codex `SKILL.md` later using [Authoring Skills and References](../S01-skills-for-engineering-teams/authoring-skills-and-references/SKILL.md).

## The 3-Layer Operating Model

Backend engineers routinely ship schema, ORM, or API changes without seeing column-level lineage, primary-key grain, or actual production data distributions. Problems—fan-out double counting, silent enum drift, dirty text values—only surface weeks later in dashboards. Chain these three layers in order:

```text
Layer 1: Code & Service Graph          Layer 2: Relational & Contract Lineage      Layer 3: Data & Metric Verification
──────────────────────────────         ──────────────────────────────────────      ────────────────────────────────────
codebase-memory-mcp                    sqlglot + DB catalogs + migrations          Jupyter + Polars / Pandas (SAS EDA)
- index_repository                     - direct (SELECT) & indirect (WHERE/JOIN)   - PROC CONTENTS / FREQ / UNIVARIATE
- search_graph / trace_path            - table/column read & write inventory       - alphabetical text sort & dirty-value scan
- DATA_FLOWS / HTTP_CALLS / CONFIGURES - Open Data Contracts (PK, enum, SLA)       - PK uniqueness, join cardinality, control totals
```

## Prompt References

| # | Reference | Use when… | Primary tools |
|---|---|---|---|
| **01** | [Backend Data Lineage & Contracts](01-backend-data-lineage-and-contracts.md) | Mapping every DB, table, column, external API, and transformation a backend codebase reads or writes; auditing blast radius before changing a schema or query. | `codebase-memory-mcp`, `sqlglot`, OpenLineage model, `datacontract-cli` (ODCS) |
| **02** | [Univariate & Grain EDA Notebooks](02-univariate-and-grain-eda-notebooks.md) | Profiling real tables in Jupyter before writing joins, migrations, or features; catching dirty text values, broken primary keys, and M:N fan-out. | Jupyter, Polars (primary) / Pandas, Pandera, SAS banking EDA equivalents |
| **03** | [Analytics Aggregations & Metric Verification](03-analytics-aggregations-and-metric-verification.md) | Designing or reviewing rollups, KPIs, and backend-fed analytics; preventing double counting on joins, handling balances/ratios, and reconciling control totals. | Polars / Pandas, SQL, MetricFlow entity/additivity rules |

## Converting a Prompt Reference to a Claude or Codex Skill

Keep the Prompt Reference as the single source of truth. When a team wants auto-triggering in Claude Code or Codex:

1. Create a skill folder (e.g. `skills/<name>/SKILL.md`) with a crisp `name` and trigger-oriented `description` (what triggers it, what does not).
2. Keep `SKILL.md` short (~100–250 lines): workflow steps, hard gates, and a link to this Prompt Reference for full decision tables and code recipes.
3. Follow [Authoring Skills and References](../S01-skills-for-engineering-teams/authoring-skills-and-references/SKILL.md) to avoid duplicating the reference body.

## Provenance & Sources

These references combine first-principles systems engineering with patterns verified against open-source projects (not copied verbatim; original synthesis only):
- [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) — local tree-sitter + Hybrid LSP code knowledge graph and 17 MCP tools.
- [tobymao/sqlglot](https://github.com/tobymao/sqlglot) — SQL AST and schema-backed column lineage.
- [OpenLineage](https://github.com/OpenLineage/OpenLineage) — direct vs. dataset-level (`INDIRECT`) column lineage taxonomy.
- [datacontract/datacontract-cli](https://github.com/datacontract/datacontract-cli) — Open Data Contract Standard (ODCS) schema, quality, and SLA testing.
- [unionai-oss/pandera](https://github.com/unionai-oss/pandera) & [ydata-profiling](https://github.com/ydataai/ydata-profiling) — Polars/Pandas schema validation and univariate alert taxonomy.
- [dbt-labs/metricflow](https://github.com/dbt-labs/metricflow) — entity grain (`PRIMARY`/`UNIQUE`/`FOREIGN`) and semi-additive window semantics.
- Classic banking SAS EDA procedures (`PROC CONTENTS`, `PROC FREQ`, `PROC UNIVARIATE`, `PROC MEANS`).
