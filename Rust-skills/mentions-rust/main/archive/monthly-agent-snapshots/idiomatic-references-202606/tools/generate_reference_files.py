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


CATEGORY_PROFILES: dict[str, dict[str, str]] = {
    "kotlin": {
        "actor": "Kotlin backend builder",
        "start": "starting from a service, route, or worker that must become production-safe",
        "decision": "choosing the smallest reliable backend pattern that preserves coroutine, framework, and operational discipline",
        "artifact": "service slice runbook with request model, validation, coroutine boundary, persistence boundary, and release gate",
        "metric": "lead time from requirement to verified endpoint stays under one focused implementation session",
        "failure": "framework choice or coroutine behavior is guessed instead of verified with tests and docs",
        "adjacent": "Use runtime, security, or testing Kotlin references when the question is about day-two operation, abuse cases, or fixtures.",
    },
    "rust": {
        "actor": "Rust reliability engineer",
        "start": "starting from a requirement that needs a safe API, explicit error model, and testable boundary",
        "decision": "choosing the idiomatic ownership, async, error, and crate-boundary shape before coding",
        "artifact": "requirement-to-API worksheet with Result type, ownership notes, async boundary, tests, and benchmark gate",
        "metric": "compile attempts and review comments decrease because the API shape is explicit before implementation",
        "failure": "the reference hides ownership or error tradeoffs behind generic guidance",
        "adjacent": "Use backend, executable, or quality-gate Rust references when the question shifts to HTTP delivery, specs, or review gates.",
    },
    "python": {
        "actor": "Python maintainer",
        "start": "starting from scripts or services that need typing, fixtures, packaging, and lint discipline",
        "decision": "choosing how strict to make typing, tests, validation, and dependency hygiene for the current risk level",
        "artifact": "typed-package adoption ladder with pyproject choices, pytest fixtures, mypy or pyright checks, and ruff gates",
        "metric": "the next agent can modify the package without weakening type, lint, or fixture coverage",
        "failure": "the reference says quality matters but gives no migration path from loose scripts to strict package code",
        "adjacent": "Use reliability, routing, or quality references when the problem is governance rather than syntax.",
    },
    "tauri": {
        "actor": "Tauri desktop app team",
        "start": "starting from a frontend action that must cross into Rust commands and platform permissions",
        "decision": "choosing the safest command, permission, IPC, packaging, and verification boundary",
        "artifact": "desktop feature slice with frontend call, Rust command, permission surface, packaging check, and failure recovery",
        "metric": "the feature can be tested across frontend, Rust command, and packaged desktop behavior",
        "failure": "the reference ignores permissions, IPC risk, or platform-specific verification",
        "adjacent": "Use executable, doctrine, or legacy Tauri references when the task is about specs, policy, or migration.",
    },
    "frontend": {
        "actor": "frontend product engineer",
        "start": "starting from a user workflow that must become a typed, accessible, resilient interface",
        "decision": "choosing component boundaries, state ownership, loading/error/empty states, and visual verification",
        "artifact": "screen-level interaction map with state model, component contract, accessibility checks, and visual QA",
        "metric": "primary workflow completion improves without introducing layout, accessibility, or state regressions",
        "failure": "the reference lists tools without describing the user workflow and failure states",
        "adjacent": "Use React, Three.js, or design references when the task is component logic, canvas behavior, or UI quality.",
    },
    "plugin": {
        "actor": "agent-tool platform builder",
        "start": "starting from a capability request that could become a command, hook, plugin, MCP server, or setting",
        "decision": "choosing the right extension surface and proving install, invocation, permissions, and recovery behavior",
        "artifact": "extension decision tree with manifest, invocation contract, test harness, versioning, and rollback path",
        "metric": "users can install, invoke, debug, and remove the extension without reading implementation code",
        "failure": "the reference confuses adjacent extension types or omits failure recovery",
        "adjacent": "Use command, hook, MCP, settings, or manifest references when one extension surface is already selected.",
    },
    "agent": {
        "actor": "agent-system designer",
        "start": "starting from a task that needs context selection, tool use, delegation, and verification",
        "decision": "choosing what context to load, what to offload, when to delegate, and how to prove completion",
        "artifact": "task trace showing prompt, context budget, tool calls, checkpoints, verification, and retained learning",
        "metric": "the next run needs fewer clarifications and produces fewer unverifiable claims",
        "failure": "the reference tells agents what to do without defining context budget or escalation rules",
        "adjacent": "Use debate, subagent, context, or verification references when the task narrows to a specific agent behavior.",
    },
    "delivery": {
        "actor": "technical lead or implementation agent",
        "start": "starting from an ambiguous request that must become acceptance criteria and tests",
        "decision": "choosing the requirement IDs, negative cases, verification gates, and handoff evidence",
        "artifact": "miniature feature packet with WHEN/THEN/SHALL requirements, RED output, GREEN output, and audit checklist",
        "metric": "every shipped claim has a requirement ID and fresh verification evidence",
        "failure": "the reference describes TDD or specs without showing failing and passing evidence",
        "adjacent": "Use TDD, traceability, or completion verification references when the work is already scoped.",
    },
    "documentation": {
        "actor": "reader or documentation author",
        "start": "starting cold and deciding whether the reference answers the next practical question",
        "decision": "choosing the reading path, example, diagram, or rewrite pattern that makes action obvious",
        "artifact": "reader journey map with before-and-after example, comprehension check, and edit rubric",
        "metric": "a new reader can apply the reference without asking the author for hidden context",
        "failure": "the reference is a literature dump instead of a guided explanation",
        "adjacent": "Use visual, ASCII, HTML, or writing references when the output medium is fixed.",
    },
    "architecture": {
        "actor": "system designer or debugger",
        "start": "starting from a design choice, failure symptom, dependency map, or unclear boundary",
        "decision": "choosing the evidence, option set, tradeoff, and validation probe before changing structure",
        "artifact": "diagnostic worksheet with symptoms, hypotheses, probes, options, rejected alternatives, and verification gates",
        "metric": "the chosen boundary reduces blast radius or uncertainty measured by explicit probes",
        "failure": "the reference jumps to a pattern before proving the problem shape",
        "adjacent": "Use dependency, debugging, timeline, or system design references when the inquiry narrows.",
    },
    "creative": {
        "actor": "creative tool builder or artifact creator",
        "start": "starting from vague creative intent that needs constraints, iteration, and quality review",
        "decision": "choosing the prompt, controls, taste rubric, regeneration trigger, and final acceptance bar",
        "artifact": "creative iteration loop with brief, draft, critique, revised artifact, and acceptance criteria",
        "metric": "iteration improves the artifact against named taste criteria rather than random novelty",
        "failure": "the reference celebrates creativity without defining what good output looks like",
        "adjacent": "Use image, art, playground, or timeline references when the artifact type is specific.",
    },
    "default": {
        "actor": "new contributor or agent",
        "start": "starting from an unfamiliar theme and deciding whether this reference is the right tool",
        "decision": "choosing what to load, what to trust, what to avoid, and what evidence proves success",
        "artifact": "role-based usage guide with examples, tradeoffs, common mistakes, and completion checks",
        "metric": "the next task uses the reference to make a better decision with less ambiguity",
        "failure": "the reference remains a source map and never becomes an operating guide",
        "adjacent": "Use the nearest language, workflow, agent, or documentation reference when the theme becomes concrete.",
    },
}


def category_for_theme(theme: str) -> str:
    tokens = set(theme.split("_"))
    if "kotlin" in tokens:
        return "kotlin"
    if "rust" in tokens:
        return "rust"
    if "python" in tokens:
        return "python"
    if "tauri" in tokens:
        return "tauri"
    if tokens & {"typescript", "react", "mern", "threejs", "frontend", "dotnet", "angular"}:
        return "frontend"
    if tokens & {"plugin", "command", "hook", "mcp", "settings", "manifest", "stripe"}:
        return "plugin"
    if tokens & {"agent", "claude", "subagent", "parallel", "context", "codex"}:
        return "agent"
    if tokens & {"tdd", "executable", "specification", "traceability", "verification", "completion"}:
        return "delivery"
    if tokens & {"writing", "minto", "html", "ascii", "visual", "explainer", "documentation"}:
        return "documentation"
    if tokens & {"image", "art", "playground", "timeline", "creative"}:
        return "creative"
    if tokens & {"system", "design", "architecture", "dependency", "debugging"}:
        return "architecture"
    return "default"


def topic_artifact_for_theme(theme: str, title: str) -> str:
    tokens = set(theme.split("_"))
    ordered = [
        ("security", "threat model with abuse cases, permission boundaries, and supply-chain review gates"),
        ("privacy", "data classification table with retention, consent, and PII handling rules"),
        ("testing", "fixture plan with unit, integration, negative, and flaky-test handling"),
        ("tdd", "RED/GREEN transcript with refactor rule and resume checkpoint"),
        ("runtime", "operations runbook for deploy, rollback, SLO breach, logging, and incident review"),
        ("operations", "day-two runbook with owner handoff, rollback trigger, and failure drill"),
        ("routing", "canonical source routing rules for stale, duplicate, and conflicting sources"),
        ("quality", "quality bar rubric with review blockers, lint gates, and release criteria"),
        ("mcp", "resource/tool boundary map with permission model and integration failure recovery"),
        ("hook", "hook lifecycle map with bypass policy, safety constraints, and debug workflow"),
        ("command", "command anatomy with arguments, interactive flow, test harness, and marketplace readiness"),
        ("settings", "configuration schema with migration behavior, validation errors, and recovery paths"),
        ("manifest", "manifest compatibility matrix with install validation and failure examples"),
        ("roadmap", "now/next/later prioritization model with opportunity sizing and kill criteria"),
        ("debate", "debate rubric with convergence criteria, dissent handling, and evidence thresholds"),
        ("creation", "agent charter template with owner, user, trigger, tool budget, escalation, and retirement rule"),
        ("context", "context budget policy for prompt, file, memory, and sub-agent handoff"),
        ("prompt", "prompt contract with bad-prompt rewrite and evaluation criteria"),
        ("frontend", "workflow state map with accessibility, loading, error, and empty-state checks"),
        ("react", "component ownership map with state, data boundary, render budget, and tests"),
        ("threejs", "canvas verification plan with asset loading, render loop, performance, and mobile framing"),
        ("visual", "visual grammar with before/after diagram and comprehension test"),
        ("ascii", "terminal layout rubric with width constraints and readability checks"),
        ("html", "responsive explainer outline with hierarchy, visual QA, and accessibility review"),
        ("writing", "reader promise with before/after rewrite and plain-language acceptance test"),
        ("minto", "top-line answer pyramid with evidence ordering and executive-reader stress test"),
        ("github", "repository workflow map with auth, API failure handling, PR trail, and audit expectations"),
        ("branch", "dirty-worktree matrix with commit scope, push decision, and recovery commands"),
        ("worktree", "worktree lifecycle with branch naming, dependency sync, and cleanup guardrails"),
        ("dependency", "dependency graph probe with ownership map, false-positive rules, and blast-radius examples"),
        ("debugging", "symptom-to-hypothesis loop with repro minimization, probes, and confidence scoring"),
        ("architecture", "decision record with boundary options, rejected alternatives, and migration sequence"),
        ("timeline", "scenario map with assumptions, leading indicators, and reversal triggers"),
        ("playground", "interactive control map with saved states, inspectability, and learning outcomes"),
        ("image", "prompt anatomy with style constraints, edit loop, safety review, and output rubric"),
        ("art", "creative seed strategy with iteration scoring and export QA"),
        ("backend", "request lifecycle diagram with persistence boundary, observability hook, and failure table"),
        ("skill", "skill activation contract with progressive disclosure, misuse case, and verification gate"),
        ("reference", "reference freshness workflow with canonical source policy and update checklist"),
    ]
    for token, artifact in ordered:
        if token in tokens:
            return artifact
    return f"worked {title.lower()} example with user goal, decision point, failure mode, and verification gate"


def classification_for_source(index: int, local_count: int, item: dict[str, object]) -> str:
    path = str(item["path"]).lower()
    if index == 0:
        return "canonical primary source"
    if "/references/" in path:
        return "supporting detail source"
    if "archive" in path or "202602" in path or "202603" in path:
        return "legacy historical source"
    if "/examples/" in path or "/templates/" in path:
        return "supporting example source"
    if local_count == 1:
        return "canonical single source"
    return "supporting context source"


def adjacent_reference_candidates(theme: str) -> list[str]:
    tokens = theme.split("_")
    candidates: list[str] = []
    for token in tokens:
        candidates.append(f"{token} adjacent reference")
    candidates.append("nearest workflow reference")
    return candidates[:3]


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
    profile = CATEGORY_PROFILES[category_for_theme(row.theme)]
    query = row.theme.replace("_", " ")
    artifact = topic_artifact_for_theme(row.theme, title)

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
    lines.append("## User Journey Scenario")
    lines.append("")
    lines.append(f"Role based opening scenario: The {profile['actor']} is {profile['start']} and needs a reference that turns source evidence into an executable next step.")
    lines.append(f"Primary user starting state: The user has a `{row.theme}` task, one or more local source paths, and uncertainty about which pattern should drive implementation.")
    lines.append(f"Decision being made: {profile['decision']}.")
    lines.append(f"Reference opening trigger: Open this file when the task mentions {query}, any mapped local source path, or an adjacent workflow with the same failure mode.")
    lines.append("")
    lines.append("## Decision Tradeoff Guide")
    lines.append("")
    lines.append("| decision_option_name | when_to_choose_condition | tradeoff_cost_description | verification_question_prompt |")
    lines.append("| --- | --- | --- | --- |")
    lines.append(f"| Adopt when | local corpus and external evidence agree on the {query} pattern | fastest path, but can copy stale local assumptions | Does the selected pattern appear in the canonical source and current external evidence? |")
    lines.append(f"| Adapt when | local sources are strong but public ecosystem guidance has changed | preserves repo fit, but requires explicit inference notes | Did the reference label the local fact, external fact, and combined inference separately? |")
    lines.append(f"| Avoid when | source evidence is thin, conflicting, or unrelated to the user journey | prevents false confidence, but may require deeper research | Is there a confidence warning or adjacent reference route? |")
    lines.append(f"| Cost of being wrong | wrong {query} guidance can send an agent to the wrong files, tests, or abstraction | wasted implementation loop and weaker verification | Would a reviewer know what to undo and what to inspect next? |")
    lines.append("")
    lines.append("## Local Corpus Hierarchy")
    lines.append("")
    lines.append("Classification vocabulary includes canonical, supporting, legacy, duplicate, and conflicting source roles.")
    if len(local_summaries) == 1:
        lines.append("Confidence warning: only one local corpus source is mapped, so this reference should invite adjacent-source discovery before becoming canonical policy.")
    lines.append("")
    lines.append("| local_source_filepath_value | corpus_hierarchy_role | heading_signal_to_convert | reviewer_question_to_answer |")
    lines.append("| --- | --- | --- | --- |")
    for index, item in enumerate(local_summaries):
        headings = item["headings"]
        signal = "; ".join(headings[:3]) if headings else "no heading discovered"
        classification = classification_for_source(index, len(local_summaries), item)
        lines.append(
            f"| {item['path']} | {classification} | {cell_clean(signal)} | What guidance, warning, or example should this source contribute to {title}? |"
        )
    lines.append("")
    lines.append("## Theme Specific Artifact")
    lines.append("")
    lines.append(f"Theme specific artifact: {artifact}.")
    lines.append("")
    lines.append("| artifact_field_name | artifact_completion_rule | evidence_source_hint |")
    lines.append("| --- | --- | --- |")
    lines.append(f"| user_goal_statement | state the user's concrete goal before applying {title} | local corpus hierarchy plus critique findings |")
    lines.append(f"| decision_boundary_rule | define the point where this reference should be used or avoided | decision tradeoff guide |")
    lines.append(f"| verification_gate_rule | define the command, checklist, or review question that proves the artifact worked | verification gate command set |")
    lines.append("")
    lines.append("## Worked Example Set")
    lines.append("")
    lines.append(f"Good example: Use {title} after loading the canonical source, confirming the external evidence boundary, and writing a verification gate before implementation.")
    lines.append(f"Bad example: Use {title} as a generic tutorial while ignoring the mapped local paths, source hierarchy, and cost of being wrong.")
    lines.append(f"Borderline case: Use {title} only after adding a confidence warning when local evidence is thin or conflicts with current ecosystem guidance.")
    lines.append("")
    lines.append("## Outcome Metrics and Feedback Loops")
    lines.append("")
    lines.append(f"Leading indicator: {profile['metric']}.")
    lines.append(f"Failure signal: {profile['failure']}.")
    lines.append("Review cadence: Re-run the verifier after every generated-reference edit and refresh external sources when public APIs, docs, or tooling releases change.")
    lines.append("")
    lines.append("## Completeness Checklist")
    lines.append("")
    lines.append(f"- The role scenario names the user, starting state, decision, and trigger for {title}.")
    lines.append("- The decision guide includes Adopt when, Adapt when, Avoid when, and Cost of being wrong.")
    lines.append("- The local corpus hierarchy identifies canonical and supporting sources or gives a confidence warning.")
    lines.append("- The theme specific artifact is concrete enough to review without reading every mapped source.")
    lines.append("- The examples cover good, bad, and borderline usage.")
    lines.append("- The metrics section names one leading indicator and one failure signal.")
    lines.append("- The adjacent routing section points to a better reference when this one is not the right fit.")
    lines.append("")
    lines.append("## Adjacent Reference Routing")
    lines.append("")
    lines.append(f"Adjacent reference guidance: {profile['adjacent']}")
    for index, candidate in enumerate(adjacent_reference_candidates(row.theme), 1):
        lines.append(f"Adjacent reference {index}: consider the {candidate} when the current task pivots away from {query}.")
    lines.append("")
    lines.append("## Future Refresh Search Queries")
    lines.append("")
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
