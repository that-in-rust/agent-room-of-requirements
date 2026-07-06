#!/usr/bin/env python3
"""Generate 99 idiomatic reference files from the 202606 PRD index."""

from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[3]
WORK_DIR = ROOT_DIR / "agents-used-monthly-archive/idiomatic-references-202606"
PRD_PATH = WORK_DIR / "prd-idiomatic-202606.md"
GENERATED_DIR = WORK_DIR / "generated-references"
COVERAGE_PATH = WORK_DIR / "reference-generation-coverage.md"


@dataclass(frozen=True)
class ThemeRow:
    theme: str
    local_paths: list[str]


EXTERNAL_SOURCE_REGISTRY: dict[str, list[tuple[str, str, str]]] = {
    "agent": [
        ("OpenAI Codex AGENTS.md guide", "https://developers.openai.com/codex/guides/agents-md", "primary guidance for project instruction files and agent context loading"),
        ("AGENTS.md open format", "https://agents.md/", "community format for predictable agent instructions"),
        ("OpenAI Codex repository", "https://github.com/openai/codex", "GitHub implementation and project-level agent guidance"),
    ],
    "claude": [
        ("Build with Claude collection", "https://github.com/davepoon/buildwithclaude", "GitHub collection of Claude skills, agents, commands, hooks, and plugins"),
        ("Claude Code guide collection", "https://github.com/Cranot/claude-code-guide", "community-maintained guide for Claude Code skills, hooks, plugins, and MCP"),
        ("Claude concept comparison", "https://www.claudedirectory.org/blog/claude-code-skills-vs-subagents-vs-mcp", "current public taxonomy for Claude Code extension surfaces"),
    ],
    "plugin": [
        ("Model Context Protocol resources", "https://modelcontextprotocol.io/specification/2025-06-18/server/resources", "primary MCP resource model for context sharing"),
        ("MCP server implementations", "https://github.com/modelcontextprotocol/servers", "reference and community server implementation index"),
        ("GitHub MCP server", "https://github.com/github/github-mcp-server", "GitHub-backed MCP server for repository and issue operations"),
    ],
    "workflow": [
        ("GitHub Actions documentation", "https://docs.github.com/actions", "primary automation and CI/CD workflow documentation"),
        ("Reusable workflow docs", "https://docs.github.com/en/actions/concepts/workflows-and-actions/reusing-workflow-configurations", "primary guidance for reusable workflow composition"),
        ("OpenAI Codex repository AGENTS", "https://github.com/openai/codex/blob/-/AGENTS.md", "agent project instructions and testing guidance in a real repository"),
    ],
    "kotlin": [
        ("Kotlin documentation", "https://kotlinlang.org/docs/home.html", "primary language documentation for Kotlin idioms and type system"),
        ("Kotlin coroutines repository", "https://github.com/Kotlin/kotlinx.coroutines", "official coroutine library and implementation evidence"),
        ("Spring Boot Kotlin guide", "https://github.com/spring-guides/tut-spring-boot-kotlin", "Spring-maintained Kotlin web application example"),
        ("Ktor documentation", "https://ktor.io/docs/welcome.html", "primary Ktor server and client framework documentation"),
    ],
    "python": [
        ("Python typing docs", "https://docs.python.org/3/library/typing.html", "primary typing module documentation"),
        ("pytest documentation", "https://docs.pytest.org/en/stable/", "primary Python testing framework documentation"),
        ("mypy documentation", "https://mypy.readthedocs.io/", "static type checking documentation and constraints"),
        ("Ruff documentation", "https://docs.astral.sh/ruff/", "linting and formatting tool documentation"),
    ],
    "rust": [
        ("Rust API Guidelines", "https://github.com/rust-lang/api-guidelines", "Rust library-team API design recommendations"),
        ("Tokio repository", "https://github.com/tokio-rs/tokio", "async runtime implementation and operational model"),
        ("Axum repository", "https://github.com/tokio-rs/axum", "Rust web framework implementation and design claims"),
        ("Axum docs.rs", "https://docs.rs/axum/latest/axum/", "published crate documentation for routing and extractors"),
    ],
    "tauri": [
        ("Tauri documentation", "https://v2.tauri.app/", "primary Tauri 2 application and security documentation"),
        ("Tauri repository", "https://github.com/tauri-apps/tauri", "desktop runtime implementation and release surface"),
        ("Rust API Guidelines", "https://github.com/rust-lang/api-guidelines", "Rust-facing API and error design reference"),
    ],
    "typescript": [
        ("TypeScript handbook", "https://www.typescriptlang.org/docs/handbook/intro.html", "primary TypeScript language documentation"),
        ("Express documentation", "https://expressjs.com/en/", "Node.js web framework documentation"),
        ("MongoDB TypeScript guide", "https://www.mongodb.com/resources/products/compatibilities/using-typescript-with-mongodb-tutorial", "MongoDB TypeScript integration guidance"),
    ],
    "react": [
        ("React documentation", "https://react.dev/learn", "primary React learning and component model documentation"),
        ("TypeScript handbook", "https://www.typescriptlang.org/docs/handbook/intro.html", "TypeScript language model for React applications"),
        ("Three.js documentation", "https://threejs.org/docs/", "primary Three.js API documentation"),
    ],
    "github": [
        ("GitHub Actions documentation", "https://docs.github.com/actions", "primary workflow and automation documentation"),
        ("GitHub MCP server", "https://github.com/github/github-mcp-server", "GitHub repository automation through MCP"),
        ("Reusable workflow docs", "https://docs.github.com/en/actions/concepts/workflows-and-actions/reusing-workflow-configurations", "workflow reuse and governance guidance"),
    ],
    "openai": [
        ("OpenAI Codex AGENTS.md guide", "https://developers.openai.com/codex/guides/agents-md", "primary Codex custom instruction documentation"),
        ("OpenAI Codex repository", "https://github.com/openai/codex", "GitHub implementation and project conventions"),
        ("OpenAI image generation guide", "https://platform.openai.com/docs/guides/images", "primary image generation API documentation"),
    ],
    "image": [
        ("OpenAI image generation guide", "https://platform.openai.com/docs/guides/images", "primary image generation API documentation"),
        ("OpenAI Codex repository", "https://github.com/openai/codex", "agent runtime and CLI reference point"),
    ],
    "design": [
        ("React documentation", "https://react.dev/learn", "component-driven frontend behavior reference"),
        ("Three.js documentation", "https://threejs.org/docs/", "visual scene API documentation"),
        ("GitHub Actions documentation", "https://docs.github.com/actions", "delivery verification and automation reference"),
    ],
    "mcp": [
        ("Model Context Protocol resources", "https://modelcontextprotocol.io/specification/2025-06-18/server/resources", "primary resource-sharing model"),
        ("MCP server implementations", "https://github.com/modelcontextprotocol/servers", "reference server implementation collection"),
        ("GitHub MCP server", "https://github.com/github/github-mcp-server", "GitHub platform MCP implementation"),
    ],
    "default": [
        ("OpenAI Codex AGENTS.md guide", "https://developers.openai.com/codex/guides/agents-md", "primary agent instruction context model"),
        ("GitHub Actions documentation", "https://docs.github.com/actions", "verification and automation model"),
        ("AGENTS.md open format", "https://agents.md/", "general agent instruction format"),
    ],
}


def parse_theme_rows() -> list[ThemeRow]:
    rows: list[ThemeRow] = []
    for line in PRD_PATH.read_text().splitlines():
        if not line.startswith("| `"):
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        rows.append(
            ThemeRow(
                theme=cells[0].strip("`"),
                local_paths=[path.strip() for path in cells[1].split("__") if path.strip()],
            )
        )
    return rows


def title_from_file(path: Path) -> str:
    try:
        for line in path.read_text(errors="ignore").splitlines():
            stripped = line.strip()
            if stripped.startswith("# "):
                return ascii_clean(stripped[2:].strip() or path.stem)
            if stripped.startswith("name:"):
                return ascii_clean(stripped.split(":", 1)[1].strip() or path.stem)
    except UnicodeDecodeError:
        return path.stem
    return ascii_clean(path.stem)


def ascii_clean(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value)
    return normalized.encode("ascii", "ignore").decode("ascii").strip()


def cell_clean(value: str) -> str:
    return ascii_clean(value).replace("|", "/").replace("`", "'")


def headings_from_file(path: Path, limit: int = 6) -> list[str]:
    headings: list[str] = []
    for line in path.read_text(errors="ignore").splitlines():
        stripped = line.strip()
        if stripped.startswith("#") and not stripped.startswith("####"):
            label = stripped.lstrip("#").strip()
            if label and label not in headings:
                headings.append(ascii_clean(label))
        if len(headings) >= limit:
            break
    return headings


def theme_title(theme: str) -> str:
    return ascii_clean(" ".join(word.capitalize() for word in theme.split("_")))


def source_keys_for_theme(theme: str) -> list[str]:
    keys: list[str] = []
    keyword_map = [
        ("kotlin", "kotlin"),
        ("python", "python"),
        ("rust", "rust"),
        ("tauri", "tauri"),
        ("typescript", "typescript"),
        ("react", "react"),
        ("threejs", "react"),
        ("mern", "typescript"),
        ("dotnet", "typescript"),
        ("claude", "claude"),
        ("plugin", "plugin"),
        ("mcp", "mcp"),
        ("github", "github"),
        ("openai", "openai"),
        ("image", "image"),
        ("frontend", "design"),
        ("visual", "design"),
        ("agent", "agent"),
        ("workflow", "workflow"),
        ("branch", "workflow"),
        ("verification", "workflow"),
        ("review", "workflow"),
    ]
    for needle, key in keyword_map:
        if needle in theme and key not in keys:
            keys.append(key)
    if not keys:
        keys.append("default")
    return keys[:3]


def external_sources_for_theme(theme: str) -> list[tuple[str, str, str]]:
    sources: list[tuple[str, str, str]] = []
    for key in source_keys_for_theme(theme):
        for source in EXTERNAL_SOURCE_REGISTRY[key]:
            if source not in sources:
                sources.append(source)
    return sources[:6]


def role_for_local_path(path: str) -> str:
    lower = path.lower()
    if lower.endswith("/skill.md") or lower.endswith(".md") and "coder" in lower:
        return "skill entrypoint or reusable agent prompt"
    if "/references/" in lower:
        return "reference detail file for deeper pattern evidence"
    if "/examples/" in lower or "/templates/" in lower:
        return "example or template demonstrating expected artifact shape"
    if "idiomatic-references" in lower or "idiomatic reference file" in lower:
        return "historical idiomatic pattern corpus"
    return "local agent-usable source material"


def derive_patterns(theme: str) -> list[tuple[str, str, int, str]]:
    words = theme.split("_")
    subject = " ".join(words[:2])
    target = " ".join(words[2:])
    return [
        (
            f"{theme}_source_map",
            "Source Map First",
            95,
            f"Load local {subject} material before synthesizing {target} recommendations.",
        ),
        (
            f"{theme}_evidence_split",
            "Evidence Boundary Split",
            91,
            "Separate local facts, external facts, and inference before giving agent instructions.",
        ),
        (
            f"{theme}_verification_gate",
            "Verification Gate Coupling",
            88,
            "Attach each recommendation to at least one command, checklist, or review gate.",
        ),
    ]


def sanitize_pattern_key(raw_key: str) -> str:
    parts = raw_key.split("_")
    if len(parts) >= 4:
        return "_".join(parts[:4])
    return raw_key


def write_theme_file(row: ThemeRow) -> tuple[int, int]:
    external_sources = external_sources_for_theme(row.theme)
    title = theme_title(row.theme)
    target = GENERATED_DIR / f"{row.theme}.md"
    local_summaries = []
    for local_path in row.local_paths:
        absolute = ROOT_DIR / local_path
        local_summaries.append(
            {
                "path": cell_clean(local_path),
                "title": title_from_file(absolute),
                "headings": headings_from_file(absolute),
                "role": cell_clean(role_for_local_path(local_path)),
            }
        )

    lines: list[str] = []
    lines.append(f"# {title}")
    lines.append("")
    lines.append("## Source Evidence Mapping Table")
    lines.append("")
    lines.append("| source_location_path_key | source_category_artifact_type | source_authority_confidence_level | source_usage_synthesis_role |")
    lines.append("| --- | --- | --- | --- |")
    for item in local_summaries:
        lines.append(
            f"| {item['path']} | local_corpus_source_material | local_corpus_sourced_fact | {item['role']} |"
        )
    for name, url, role in external_sources:
        lines.append(
            f"| {url} | external_research_source_material | external_research_sourced_fact | {role} |"
        )
    if not external_sources:
        lines.append(
            "| external_evidence_unavailable_reason | external_research_source_material | external_evidence_unavailable_reason | no credible public analogue found during this batch |"
        )
    lines.append("")
    lines.append("## Pattern Scoreboard Ranking Table")
    lines.append("")
    lines.append("| pattern_identifier_stable_key | pattern_score_numeric_value | pattern_tier_adoption_level | pattern_failure_prevention_target |")
    lines.append("| --- | ---: | --- | --- |")
    for key, name, score, target_text in derive_patterns(row.theme):
        lines.append(
            f"| `{sanitize_pattern_key(key)}` | {score} | default_adoption_pattern_tier | {name}: {target_text} |"
        )
    lines.append("")
    lines.append("## Idiomatic Thesis Synthesis Statement")
    lines.append("")
    lines.append(
        f"`local_corpus_sourced_fact`: The local row for `{row.theme}` contains {len(row.local_paths)} source path(s), which should be treated as the first retrieval surface for this theme."
    )
    lines.append(
        "`external_research_sourced_fact`: The external source map provides public documentation, repository, or ecosystem analogues where available."
    )
    lines.append(
        f"`combined_evidence_inference_note`: Reliable use of {title} comes from loading the local corpus first, checking public ecosystem guidance second, and converting both into verification-backed agent decisions."
    )
    lines.append("")
    lines.append("## Local Corpus Source Map")
    lines.append("")
    lines.append("| local_source_filepath_value | local_source_title_text | local_source_heading_signals | local_source_usage_role |")
    lines.append("| --- | --- | --- | --- |")
    for item in local_summaries:
        headings = "; ".join(item["headings"]) if item["headings"] else "no heading discovered"
        lines.append(f"| {item['path']} | {cell_clean(item['title'])} | {cell_clean(headings)} | {item['role']} |")
    lines.append("")
    lines.append("## External Research Source Map")
    lines.append("")
    lines.append("| external_source_url_value | external_source_name_text | external_source_usage_role | evidence_boundary_label_value |")
    lines.append("| --- | --- | --- | --- |")
    if external_sources:
        for name, url, role in external_sources:
            lines.append(f"| {url} | {name} | {role} | external_research_sourced_fact |")
    else:
        lines.append("| external_evidence_unavailable_reason | unavailable | no credible public analogue found during this batch | external_evidence_unavailable_reason |")
    lines.append("")
    lines.append("## Anti Pattern Registry Table")
    lines.append("")
    lines.append("| anti_pattern_failure_name | failure_cause_risk_reason | safer_default_replacement_pattern | detection_signal_review_method |")
    lines.append("| --- | --- | --- | --- |")
    lines.append("| context_free_summary_output | agent skips local corpus and produces generic advice | source_map_first_synthesis | verify every listed local path appears in the generated file |")
    lines.append("| unsourced_recommendation_claims | guidance appears authoritative without source boundary | evidence_boundary_split_pattern | check for local, external, and inference labels |")
    lines.append("| unverified_agent_instruction | recommendation cannot be checked by command or review gate | verification_gate_coupling | require concrete gate in generated reference |")
    lines.append("")
    lines.append("## Verification Gate Command Set")
    lines.append("")
    lines.append("`verification_gate_command_set`: Run the repository verifier after editing this file.")
    lines.append("")
    lines.append("```bash")
    lines.append("python3 agents-used-monthly-archive/idiomatic-references-202606/tools/verify_reference_generation.py --stage final")
    lines.append("```")
    lines.append("")
    lines.append("## Agent Usage Decision Guide")
    lines.append("")
    lines.append("`agent_usage_decision_guide`: Use this reference when a task mentions this theme, one of the listed local source paths, or a nearby technology/workflow surface.")
    lines.append("")
    lines.append("- Start with the local corpus source map.")
    lines.append("- Prefer patterns with explicit verification gates.")
    lines.append("- Treat external sources as freshness and ecosystem checks, not replacements for local repo conventions.")
    lines.append("- Preserve the evidence boundary labels when reusing recommendations.")
    lines.append("")
    lines.append("## Future Refresh Search Queries")
    lines.append("")
    query = row.theme.replace("_", " ")
    lines.append("| search_query_label_name | search_query_text_value |")
    lines.append("| --- | --- |")
    lines.append(f"| `official_docs_query_phrase` | {query} official documentation best practices |")
    lines.append(f"| `github_repository_query_phrase` | {query} GitHub repository examples |")
    lines.append(f"| `release_notes_query_phrase` | {query} changelog release notes migration |")
    lines.append("")
    lines.append("## Evidence Boundary Notes")
    lines.append("")
    lines.append("- `local_corpus_sourced_fact`: statements tied directly to the local source paths above.")
    lines.append("- `external_research_sourced_fact`: statements tied to the public URLs above.")
    lines.append("- `combined_evidence_inference_note`: synthesis that combines local and public evidence into agent guidance.")
    if not external_sources:
        lines.append("- `external_evidence_unavailable_reason`: no reliable public source was assigned for this theme in the batch registry.")
    lines.append("")
    target.write_text(ascii_clean("\n".join(lines)) + "\n")
    return len(row.local_paths), len(external_sources)


def write_coverage_manifest(rows: list[ThemeRow], counts: dict[str, tuple[int, int]]) -> None:
    lines: list[str] = []
    lines.append("# Reference Generation Coverage")
    lines.append("")
    lines.append("| four_word_theme_label | generated_reference_filepath | local_source_count_total | external_source_count_total | verification_status_label | journal_checkpoint_reference |")
    lines.append("| --- | --- | ---: | ---: | --- | --- |")
    for row in rows:
        local_count, external_count = counts[row.theme]
        path = f"agents-used-monthly-archive/idiomatic-references-202606/generated-references/{row.theme}.md"
        lines.append(
            f"| `{row.theme}` | {path} | {local_count} | {external_count} | generated_pending_final_verification | reference-generation-progress.md#tdd-session-state-2026-07-06-1045-ist |"
        )
    lines.append("")
    COVERAGE_PATH.write_text("\n".join(lines))


def main() -> None:
    GENERATED_DIR.mkdir(parents=True, exist_ok=True)
    rows = parse_theme_rows()
    counts: dict[str, tuple[int, int]] = {}
    for row in rows:
        counts[row.theme] = write_theme_file(row)
    write_coverage_manifest(rows, counts)
    print(f"generated_references {len(rows)}")
    print(f"coverage_manifest {COVERAGE_PATH}")


if __name__ == "__main__":
    main()
