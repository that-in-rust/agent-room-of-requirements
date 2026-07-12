# Plugin Hook Development Patterns

**Decision supported.** This section helps decide which hook system and hook type a guardrail or automation should be built on. The seed title names the theme without its governing split, hookify rules are user-local markdown files matched by regex while plugin hooks are hooks.json event handlers, and prompt-based hooks are the recommended default over command hooks.

**Recommended default and causal basis.** Reach for a hookify rule for personal per-project guardrails and a plugin hooks.json entry for distributable event automation, with prompt hooks unless the check is deterministic. Hook-development states focus on prompt-based hooks for most use cases and reserve command hooks for performance-critical or deterministic checks, while hookify stores rules in .claude/hookify.{rule-name}.local.md files.

**Operating conditions and assumptions.** The plugin runtime supports prompt hooks on the target event, only Stop, SubagentStop, UserPromptSubmit, and PreToolUse are listed as supported. This reference operationalizes the hookify rule format and the plugin hook lifecycle across its nine events, not Claude Code plugin development at large.

**Failure boundary and alternatives.** Conflating the two systems sends a user editing hooks.json when a one-file hookify rule would do, or shipping a personal hookify rule where a plugin hook was needed. Bounded alternatives and recoveries: pure command-hook validation scripts, or no hooks with review-time enforcement instead of event-time enforcement.

**Counterexample, gotchas, and operational comparison.** Hooks load at session start and cannot be hot-swapped, editing hooks.json mid-session silently changes nothing until restart. Good: a dangerous-rm warning shipped as a hookify bash rule in minutes. Bad: a regex-only command hook that misses rm -fr variants the prompt hook would catch. Borderline: a fast path-safety check kept as a command hook for latency, sanctioned by the deterministic exception.

**Verification, evidence, and uncertainty.** Confirm new guardrails record which system was chosen and why, and that prompt-hook events are among the four supported ones. Hookify SKILL.md and hook-development SKILL.md state every element promoted here. How the nine-event catalog evolves across Claude Code releases is not verifiable from the archive.

**Second-order consequence.** Both systems converge on the same design pressure, validation logic wants to live in natural language, hookify puts the message body in markdown and hook-development migrates regex scripts into prompt criteria.

**Revision decision.** Open with the two-system split, the nine hook events, and the prompt-over-command default with its deterministic-check exception.

**Retained seed evidence.** The exact theme title and its development-patterns framing remain unchanged. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

## Source Evidence Mapping Table

**Decision supported.** This section helps decide which recorded source may back which claim about hook development. The seed map lists ten local rows without noting they collapse to five texts, one hookify skill plus one hook-development skill with three reference files, each present as byte-identical archive and live copies.

**Recommended default and causal basis.** Cite hookify for rule-file claims, the hook-development skill for event and output-format claims, and the specific reference file for pattern, migration, or advanced-technique claims. Diffing every archive path against its claude-skills live counterpart during this evolution produced no differences, so citing both copies for one claim adds no corroboration.

**Operating conditions and assumptions.** The live copies stay identical to their archive snapshots, divergence would make the live copies authoritative. The table records provenance for this document's claims and does not rank hook documentation outside the archive.

**Failure boundary and alternatives.** Treating the ten rows as ten independent witnesses would double-count every hook claim in this file. Bounded alternatives and recoveries: collapse the map to five evidence units with alias notes, or diff the copies each cycle to catch divergence.

**Counterexample, gotchas, and operational comparison.** The three external URLs in the seed map point at MCP resources, not hook documentation, and none were retrieved. Good: citing patterns.md for the test-enforcement Stop hook. Bad: citing archive and live hookify copies as two confirmations. Borderline: citing the MCP spec URL for context-sharing claims, mapped but never retrieved.

**Verification, evidence, and uncertainty.** Confirm every claim traces to one of the five evidence units and the copy-identity checks are recorded. All ten mapped files were read in full and the five archive-live pairs compared byte-identical during this evolution. Why the seed's external rows carry MCP URLs rather than the hooks documentation URL that hook-development itself cites is unrecorded.

**Second-order consequence.** The five texts form a deliberate ladder, SKILL.md holds the core API, patterns.md holds ten copyable patterns, migration.md holds the conversion argument, and advanced.md holds the techniques the skill only gestures at.

**Revision decision.** Mark all ten paths read in full, group them into five evidence units, and note the archive-live identity check as the deduplication proof.

**Retained seed evidence.** All source rows with their category, confidence, and synthesis-role columns remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| source_location_path_key | source_category_artifact_type | source_authority_confidence_level | source_usage_synthesis_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/claude-skills-202603/plugins/hookify/SKILL.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/hook-development/SKILL.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/hook-development/references/advanced.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/hook-development/references/migration.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/hook-development/references/patterns.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| claude-skills/plugins/hookify/SKILL.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt |
| claude-skills/plugins/plugin-dev/hook-development/SKILL.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt |
| claude-skills/plugins/plugin-dev/hook-development/references/advanced.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| claude-skills/plugins/plugin-dev/hook-development/references/migration.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| claude-skills/plugins/plugin-dev/hook-development/references/patterns.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| https://modelcontextprotocol.io/specification/2025-06-18/server/resources | external_research_source_material | external_research_sourced_fact | primary MCP resource model for context sharing |
| https://github.com/modelcontextprotocol/servers | external_research_source_material | external_research_sourced_fact | reference and community server implementation index |
| https://github.com/github/github-mcp-server | external_research_source_material | external_research_sourced_fact | GitHub-backed MCP server for repository and issue operations |

## Pattern Scoreboard Ranking Table

**Decision supported.** This section helps decide which hook rules deserve default adoption when building event automation. The seed scoreboard scores corpus hygiene while the corpus's load-bearing hook rules go unranked, prompt hooks over regex scripts, ${CLAUDE_PLUGIN_ROOT} for every path, parallel-safe independent hooks, and restart-to-reload awareness.

**Recommended default and causal basis.** Apply all four rules on every hook, with portability and independence checked at review time. Each rule guards a distinct failure, regex scripts miss variants, hardcoded paths break portability, order-dependent hooks race, and stale sessions run yesterday's hooks.

**Operating conditions and assumptions.** Each promoted rule keeps its falsifiable phrasing so a reviewer can point at the violation. The scoreboard ranks hook-discipline rules for adoption priority and does not rank the nine events against each other.

**Failure boundary and alternatives.** The seed's numeric scores were never measured and the corpus offers only a recommended-versus-reserved ordering, not numbers. Bounded alternatives and recoveries: rank by observed hook-failure frequency once measured, or rank by debuggability with silent failures first.

**Counterexample, gotchas, and operational comparison.** Migration.md keeps a real place for command hooks, deterministic math, external scanners, and sub-50ms checks, so prompt-first is a default, not a ban. Good: a hooks.json whose every command uses ${CLAUDE_PLUGIN_ROOT} and whose hooks share no temp files. Bad: two PreToolUse hooks passing state through /tmp expecting order. Borderline: a 40ms regex allowlist kept as a command hook under the fast-check exception.

**Verification, evidence, and uncertainty.** Trace each promoted rule to its stated section in the skill or its reference files. The DO and DONT lists, the parallel-execution section, and the lifecycle section of hook-development state each promoted rule. Which rule violations occur most often in real plugin repositories is unmeasured.

**Second-order consequence.** Three of the four rules fail silently, a hardcoded path, an order assumption, or a stale session produces no error message, only wrong behavior, which is why the corpus repeats them across skill, patterns, and advanced files.

**Revision decision.** Promote a top tier of four rules, prefer prompt hooks for complex logic, reference all files through ${CLAUDE_PLUGIN_ROOT}, design hooks to run independently because matching hooks execute in parallel, and restart the session after any hook change.

**Retained seed evidence.** All scored rows with their tier labels and failure-prevention targets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| pattern_identifier_stable_key | pattern_score_numeric_value | pattern_tier_adoption_level | pattern_failure_prevention_target |
| --- | ---: | --- | --- |
| `plugin_hook_development_patterns` | 95 | default_adoption_pattern_tier | Source Map First: Load local plugin hook material before synthesizing development patterns recommendations. |
| `plugin_hook_development_patterns` | 91 | default_adoption_pattern_tier | Evidence Boundary Split: Separate local facts, external facts, and inference before giving agent instructions. |
| `plugin_hook_development_patterns` | 88 | default_adoption_pattern_tier | Verification Gate Coupling: Attach each recommendation to at least one command, checklist, or review gate. |

## Idiomatic Thesis Synthesis Statement

**Decision supported.** This section helps decide what single claim should orient a builder choosing hook machinery. The seed thesis repeats the load-local-first formula instead of the corpus's claim, that event-time guardrails should be expressed as natural-language criteria evaluated by prompt hooks, with command hooks reserved for deterministic speed.

**Recommended default and causal basis.** Phrase the thesis as prompt-first with a deterministic exception, with the three evidence labels kept on its clauses. Migration.md argues the conversion case end to end, regex catches literal strings while prompts understand intent, and hook-development's closing line makes prompt-first the official stance.

**Operating conditions and assumptions.** The labels stay attached so skill-derived clauses remain distinguishable from reference-file-derived ones. The thesis orients use of this reference and does not compress the per-event rules it stands on.

**Failure boundary and alternatives.** A thesis built on command-hook mechanics alone would canonize the exact style the corpus spends a whole reference file migrating away from. Bounded alternatives and recoveries: a determinism-first thesis for security-critical repositories, or a hookify-first thesis for single-user projects.

**Counterexample, gotchas, and operational comparison.** Prompt hooks carry 15-30 second timeouts, so a thesis ignoring latency invites hooks that time out and block the workflow. Good: a thesis reader who converts a brittle rm-rf grep into prompt criteria. Bad: one who converts a 10ms file-size check into a 15s prompt. Borderline: a hybrid quick-check plus deep-analysis pair, endorsed by advanced.md as multi-stage validation.

**Verification, evidence, and uncertainty.** Check the thesis names both the prompt-first rule and its deterministic exception. Migration.md's why-migrate and when-to-keep sections state both halves of the thesis. The actual accuracy gap between prompt and regex validation is asserted, not benchmarked, anywhere in the corpus.

**Second-order consequence.** The migration is really a trust shift, from trusting the pattern author to enumerate every dangerous string to trusting the model to recognize the category, which is why hybrid multi-stage validation keeps both layers.

**Revision decision.** Restate the combined inference as express guardrails in natural language where reasoning helps, keep bash where determinism and latency rule, and make every hook portable, parallel-safe, and restart-aware.

**Retained seed evidence.** The three labeled thesis clauses remain preserved beneath the evolved statement. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`local_corpus_sourced_fact`: The local row for `plugin_hook_development_patterns` contains 10 source path(s), which should be treated as the first retrieval surface for this theme.
`external_research_sourced_fact`: The external source map provides public documentation, repository, or ecosystem analogues where available.
`combined_evidence_inference_note`: Reliable use of Plugin Hook Development Patterns comes from loading the local corpus first, checking public ecosystem guidance second, and converting both into verification-backed agent decisions.

## Local Corpus Source Map

**Decision supported.** This section helps decide which mapped file to open first for a given hook question. The seed map lists headings without the reading order that makes the corpus usable, skill first for the API, patterns second for copyable configs, migration third for style conversion, advanced last for techniques.

**Recommended default and causal basis.** Route API questions to SKILL.md, copy-paste needs to patterns.md, style debates to migration.md, edge techniques to advanced.md, and personal guardrails to hookify. Hook-development's additional-resources section prescribes exactly that division, patterns for 8+ proven patterns, migration for basic-to-advanced, advanced for advanced use cases.

**Operating conditions and assumptions.** The reader's task is hook construction, other plugin surfaces have their own skill files outside this map. The map orders this theme's five texts and does not catalog the wider plugin-dev skill tree they sit in.

**Failure boundary and alternatives.** A reader starting in advanced.md meets state-sharing and rate-limiting tricks before learning hooks run in parallel and cannot share state safely. Bounded alternatives and recoveries: task-first routing that opens patterns.md directly, or a single merged document trading modularity for one read.

**Counterexample, gotchas, and operational comparison.** Both skills point at examples/ and scripts/ directories that are not among the mapped paths, so their contents stay unverified here. Good: copying pattern 2 test enforcement then reading its Stop-event contract in SKILL.md. Bad: building from advanced.md's hook-chaining example without its sequential-events-only warning. Borderline: starting in hookify for what will become a distributed plugin hook.

**Verification, evidence, and uncertainty.** Confirm the map's usage-role column matches each file's self-description. The additional-resources section of hook-development assigns each reference file its role. Whether the unmapped examples and scripts directories exist in this archive was not checked during this evolution.

**Second-order consequence.** Hookify is the only text addressed to end users rather than plugin authors, its rules need no plugin, no manifest, and no restart-to-install, which makes it the cheapest experiment surface before promoting a rule into a plugin hook.

**Revision decision.** Annotate each row with its ladder position and note hookify as a parallel entry point for user-local rules rather than a rung on the plugin ladder.

**Retained seed evidence.** All local source rows with their heading-signal and usage-role columns remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| local_source_filepath_value | local_source_title_text | local_source_heading_signals | local_source_usage_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/claude-skills-202603/plugins/hookify/SKILL.md | writing-hookify-rules | Writing Hookify Rules; Overview; Rule File Format; Basic Structure; Frontmatter Fields; Advanced Format (Multiple Conditions) | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/hook-development/SKILL.md | hook-development | Hook Development for Claude Code Plugins; Overview; Hook Types; Prompt-Based Hooks (Recommended); Command Hooks; Hook Configuration Formats | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/hook-development/references/advanced.md | Advanced Hook Use Cases | Advanced Hook Use Cases; Multi-Stage Validation; !/bin/bash; Immediate approval for safe commands; Let prompt hook handle complex cases; Conditional Hook Execution | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/hook-development/references/migration.md | Migrating from Basic to Advanced Hooks | Migrating from Basic to Advanced Hooks; Why Migrate?; Migration Example: Bash Command Validation; Before (Basic Command Hook); !/bin/bash; Hard-coded validation logic | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/hook-development/references/patterns.md | Common Hook Patterns | Common Hook Patterns; Pattern 1: Security Validation; Pattern 2: Test Enforcement; Pattern 3: Context Loading; !/bin/bash; Detect project type | reference detail file for deeper pattern evidence |
| claude-skills/plugins/hookify/SKILL.md | writing-hookify-rules | Writing Hookify Rules; Overview; Rule File Format; Basic Structure; Frontmatter Fields; Advanced Format (Multiple Conditions) | skill entrypoint or reusable agent prompt |
| claude-skills/plugins/plugin-dev/hook-development/SKILL.md | hook-development | Hook Development for Claude Code Plugins; Overview; Hook Types; Prompt-Based Hooks (Recommended); Command Hooks; Hook Configuration Formats | skill entrypoint or reusable agent prompt |
| claude-skills/plugins/plugin-dev/hook-development/references/advanced.md | Advanced Hook Use Cases | Advanced Hook Use Cases; Multi-Stage Validation; !/bin/bash; Immediate approval for safe commands; Let prompt hook handle complex cases; Conditional Hook Execution | reference detail file for deeper pattern evidence |
| claude-skills/plugins/plugin-dev/hook-development/references/migration.md | Migrating from Basic to Advanced Hooks | Migrating from Basic to Advanced Hooks; Why Migrate?; Migration Example: Bash Command Validation; Before (Basic Command Hook); !/bin/bash; Hard-coded validation logic | reference detail file for deeper pattern evidence |
| claude-skills/plugins/plugin-dev/hook-development/references/patterns.md | Common Hook Patterns | Common Hook Patterns; Pattern 1: Security Validation; Pattern 2: Test Enforcement; Pattern 3: Context Loading; !/bin/bash; Detect project type | reference detail file for deeper pattern evidence |

## External Research Source Map

**Decision supported.** This section helps decide which external sources deserve retrieval when this reference is refreshed. The seed map lists three MCP URLs while the corpus's own external anchor, the hooks documentation at docs.claude.com, goes unlisted.

**Recommended default and causal basis.** Treat archive claims about events, fields, and variables as archive-local until the official hooks documentation is retrieved. Hook-development names https://docs.claude.com/en/docs/claude-code/hooks as official docs, yet the seed's external rows cover the MCP resource model instead.

**Operating conditions and assumptions.** External retrieval is available, offline sessions must label runtime-contract claims as unverified. The map governs external freshness checks for this theme and does not vouch for any URL's current content.

**Failure boundary and alternatives.** A refresh cycle following the seed map would poll MCP specifications while hook events, output schemas, and timeout defaults drift unwatched. Bounded alternatives and recoveries: drop the MCP rows into an adjacent MCP reference, or keep them with an explicit off-theme label.

**Counterexample, gotchas, and operational comparison.** The seed's MCP rows look authoritative because they carry a dated spec version, but nothing in this theme's claims rests on them. Good: a refresh that fetches the hooks docs and diffs the event table. Bad: one that validates MCP resource schemas and calls this file current. Borderline: fetching the marketplace security-guidance plugin the skill cites as an example.

**Verification, evidence, and uncertainty.** Confirm every external claim in this file carries an unretrieved-candidate label. The external-resources subsection of hook-development lists the docs URL the seed map omits. Whether the docs.claude.com URL still resolves and matches the archive's API description is unknown until retrieved.

**Second-order consequence.** Hook payloads are volatile in exactly the way archives handle worst, event names, JSON fields, and environment variables are runtime contracts a single release can change, so the live docs outrank every mapped file for those details.

**Revision decision.** Flag all listed URLs as unretrieved candidates and record the official hooks documentation as the missing primary anchor for future refresh.

**Retained seed evidence.** All external source rows with their usage-role and boundary-label columns remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| external_source_url_value | external_source_name_text | external_source_usage_role | evidence_boundary_label_value |
| --- | --- | --- | --- |
| https://modelcontextprotocol.io/specification/2025-06-18/server/resources | Model Context Protocol resources | primary MCP resource model for context sharing | external_research_sourced_fact |
| https://github.com/modelcontextprotocol/servers | MCP server implementations | reference and community server implementation index | external_research_sourced_fact |
| https://github.com/github/github-mcp-server | GitHub MCP server | GitHub-backed MCP server for repository and issue operations | external_research_sourced_fact |

## Anti Pattern Registry Table

**Decision supported.** This section helps decide which failure modes must be checked before a hook is shipped. The seed registry lists generic synthesis failures while the corpus names concrete hook anti-patterns, assuming hook order, long-running hooks, uncaught exceptions on missing files, unquoted bash variables, and hardcoded paths.

**Recommended default and causal basis.** Review new hooks against all five entries before shipping, with the parallel-independence check first. Advanced.md's common-pitfalls section marks order assumptions and sleep-120 hooks as BAD outright, and the skill's security section pairs each unquoted variable with its injection risk.

**Operating conditions and assumptions.** Hooks are bash command hooks, prompt hooks dodge the quoting and crash entries but keep the timeout and order entries. The registry catalogs hook-construction failures, not plugin manifest or marketplace failures.

**Failure boundary and alternatives.** A registry without the parallel-execution pitfall leaves the corpus's most surprising rule undefended, hooks do not see each other's output and ordering is non-deterministic. Bounded alternatives and recoveries: encode the checks into the hook-linter script the skill ships, or enforce them in code review only.

**Counterexample, gotchas, and operational comparison.** Too-broad regex is also an anti-pattern but lives in hookify's pitfalls, a pattern like log matches dialog and catalog. Good: a hook that exits 0 with a skip message when its target file is absent. Bad: cat on an unchecked path crashing the hook. Borderline: a 90-second scanner hook, legal only if its timeout is raised deliberately.

**Verification, evidence, and uncertainty.** Run test-hook.sh with missing-file and hostile-input samples and confirm graceful JSON output. The common-pitfalls and security-best-practices sections state each added entry and its fix. How often each pitfall fires in production plugins is not recorded in the corpus.

**Second-order consequence.** Every added anti-pattern is a correctness bug that masquerades as working in the happy path, the corpus's fix is uniform, fail gracefully with a continue-true systemMessage rather than crashing the event.

**Revision decision.** Add five entries, order-dependent hooks, hooks exceeding their timeout budget, crash-on-missing-input scripts, injection-prone unquoted variables, and non-portable hardcoded paths, each with its corpus-stated mitigation.

**Retained seed evidence.** All registry rows with their cause, replacement, and detection columns remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| anti_pattern_failure_name | failure_cause_risk_reason | safer_default_replacement_pattern | detection_signal_review_method |
| --- | --- | --- | --- |
| context_free_summary_output | agent skips local corpus and produces generic advice | source_map_first_synthesis | verify every listed local path appears in the generated file |
| unsourced_recommendation_claims | guidance appears authoritative without source boundary | evidence_boundary_split_pattern | check for local, external, and inference labels |
| unverified_agent_instruction | recommendation cannot be checked by command or review gate | verification_gate_coupling | require concrete gate in generated reference |

## Verification Gate Command Set

**Decision supported.** This section helps decide which commands must pass before a hook change is trusted. The seed gate names only the repository verifier while the corpus ships a three-layer hook verification kit, validate-hook-schema.sh for hooks.json, test-hook.sh for sample-input runs, and claude --debug for live registration logs.

**Recommended default and causal basis.** Run schema validation and sample-input tests before every commit touching hooks, and a debug-mode session before release. The implementation workflow orders them explicitly, validate configuration, test before deployment, then test in Claude Code with claude --debug.

**Operating conditions and assumptions.** The scripts directory ships with the plugin-dev skill as documented, otherwise fall back to jq and manual echo pipes. The gate set verifies hook artifacts and this reference file, not plugin marketplace publication.

**Failure boundary and alternatives.** A hook verified only by the corpus-file verifier can still carry invalid JSON that makes the whole hooks.json fail to load at startup. Bounded alternatives and recoveries: CI-run hook tests on every push, or the /hooks command for an in-session registration snapshot.

**Counterexample, gotchas, and operational comparison.** A passing test-hook.sh run proves nothing about the live session until restart, because hooks load only at session start. Good: echo a sample tool_input JSON into the hook and jq-validate its output. Bad: shipping after only reading the script. Borderline: skipping debug mode for a one-line prompt tweak, cheap but exactly where matcher typos hide.

**Verification, evidence, and uncertainty.** Confirm the gate list includes schema, sample-input, and debug layers with expected outputs. The utility-scripts and debugging sections of hook-development document each command. The utility scripts' own behavior is documented but their code was not among the mapped files.

**Second-order consequence.** The layers catch disjoint failures, schema validation catches malformed config, sample-input runs catch script logic, and debug mode catches what only the runtime knows, registration, timing, and matcher hits.

**Revision decision.** Add the three corpus commands plus the jq round-trip for hook output validity and echo-piped stdin tests for command hooks.

**Retained seed evidence.** The original verifier command and its final-stage flag remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`verification_gate_command_set`: Run the repository verifier after editing this file.

```bash
python3 agents-used-monthly-archive/idiomatic-references-202606/tools/verify_reference_generation.py --stage final
```

## Agent Usage Decision Guide

**Decision supported.** This section helps decide which event, hook type, and hook system fit a given automation need. The seed guide says use this reference when the theme matches but not the corpus's own selection logic, event choice by lifecycle moment, hook type by determinism, and system choice by distribution need.

**Recommended default and causal basis.** Answer all three questions in writing before opening hooks.json or a hookify file. The events-summary table pairs each of nine events with its use, validation before tools, feedback after, completeness at stop, context at session start, and the migration guide pairs hook types with check character.

**Operating conditions and assumptions.** The automation reacts to Claude Code events at all, scheduled or external triggers belong to other machinery. The guide routes hook-construction decisions and does not route plugin-versus-MCP architecture choices.

**Failure boundary and alternatives.** An agent skipping the three questions defaults to PreToolUse command hooks for everything, the exact posture the corpus migrates away from. Bounded alternatives and recoveries: pattern-first selection from patterns.md's ten entries, or hookify-first prototyping before plugin promotion.

**Counterexample, gotchas, and operational comparison.** SubagentStop exists separately from Stop, a completeness gate on the main agent does not cover subagents. Good: test enforcement routed to a Stop prompt hook. Bad: context loading attempted in PreToolUse instead of SessionStart. Borderline: audit logging on Notification versus PostToolUse, both defensible by the events table.

**Verification, evidence, and uncertainty.** Confirm new hooks record answers to the three questions alongside their configuration. The events-summary table and migration guidance state the mapping each question relies on. Guidance for events the corpus leaves thin, PreCompact and Notification, is extrapolated from their one-line descriptions.

**Second-order consequence.** The questions are ordered by irreversibility, a wrong event silently never fires, a wrong type merely costs latency or accuracy, and a wrong system just costs a port later.

**Revision decision.** Add the three-question routine, which lifecycle moment, deterministic or judgment-based, personal or distributable, then map answers to event, type, and system.

**Retained seed evidence.** The four seed usage bullets remain preserved beneath the evolved guide. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`agent_usage_decision_guide`: Use this reference when a task mentions this theme, one of the listed local source paths, or a nearby technology/workflow surface.

- Start with the local corpus source map.
- Prefer patterns with explicit verification gates.
- Treat external sources as freshness and ecosystem checks, not replacements for local repo conventions.
- Preserve the evidence boundary labels when reusing recommendations.

## User Journey Scenario

**Decision supported.** This section helps decide how a builder moves from a felt incident to a shipped, tested guardrail. The seed scenario names a platform builder abstractly while the corpus implies a concrete journey, a builder who saw a dangerous operation slip through and wants event-time enforcement without breaking the team's flow.

**Recommended default and causal basis.** Start new guardrails at warn or ask severity and promote to block only after false-positive review. Patterns.md opens with exactly these journeys, block dangerous writes, enforce tests before stopping, load context at session start, each a response to a felt incident.

**Operating conditions and assumptions.** A real incident or policy anchors the guardrail, speculative hooks accumulate as unreviewed friction. The scenario motivates this reference and does not prescribe one pattern for all teams.

**Failure boundary and alternatives.** Without the incident framing the scenario cannot explain the corpus's insistence on warn-versus-block and ask-decisions, escalation levels only matter to someone weighing friction against safety. Bounded alternatives and recoveries: review-time enforcement through checklists, or CI-side enforcement decoupled from the session.

**Counterexample, gotchas, and operational comparison.** A block-severity Stop hook that misjudges completeness can trap the agent in a loop of forced continuation. Good: an rm -rf incident becoming a warn-level hookify rule then a plugin ask-hook. Bad: a speculative block-everything hook shipped without sample-input tests. Borderline: a personal hookify rule quietly required of teammates, distribution by social pressure instead of a plugin.

**Verification, evidence, and uncertainty.** Confirm the scenario's acts each name their corpus tool, routing questions, escalation levels, and the verification kit. Patterns 1, 2, and 7 plus hookify's action field document the journey and its escalation ladder. Team-scale adoption dynamics beyond the single-builder journey are outside the corpus.

**Second-order consequence.** The journey's real fork is escalation choice, hookify defaults to warn, PreToolUse offers allow, deny, and ask, and pattern 7 shows ask as the middle path that confirms rather than blocks.

**Revision decision.** Recast the journey in three acts, incident and desired guardrail, selection via the three routing questions, then implementation with schema validation, sample-input tests, and a debug-mode session.

**Retained seed evidence.** The role, starting state, decision, and trigger lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Role based opening scenario: The agent-tool platform builder is starting from a capability request that could become a command, hook, plugin, MCP server, or setting and needs a reference that turns source evidence into an executable next step.
Primary user starting state: The user has a `plugin_hook_development_patterns` task, one or more local source paths, and uncertainty about which pattern should drive implementation.
Decision being made: choosing the right extension surface and proving install, invocation, permissions, and recovery behavior.
Reference opening trigger: Open this file when the task mentions plugin hook development patterns, any mapped local source path, or an adjacent workflow with the same failure mode.

## Decision Tradeoff Guide

**Decision supported.** This section helps decide which side of each hook tradeoff a given guardrail should take. The seed guide's adopt-adapt-avoid rows never name the corpus's live tradeoffs, prompt accuracy versus command latency, block safety versus warn friction, and hookify speed versus plugin distribution.

**Recommended default and causal basis.** Hybrid validation for high-traffic events, warn-first severity, and hookify-first prototyping. Migration.md prices the first tradeoff, prompts understand intent but cost 15-30 second timeouts against sub-50ms regex checks, and the action field prices the second, block prevents while warn merely shows.

**Operating conditions and assumptions.** Latency budgets and false-positive costs are actually known, otherwise measure before hard-coding a choice. The guide arbitrates hook-construction tradeoffs, not whether event automation is worth having at all.

**Failure boundary and alternatives.** A builder using only the seed's generic rows gets no help choosing between a 10ms allowlist and a 15s reasoning pass on every bash call. Bounded alternatives and recoveries: static analysis outside the session, or trusting model behavior with no event-time checks.

**Counterexample, gotchas, and operational comparison.** Every matching hook runs on every matching event, so an expensive hook on a matcher like * taxes the whole session. Good: a deletion guard using ask after weighing block friction. Bad: a prompt hook on every Read call for a rule regex handles. Borderline: rate limiting in a command hook, deterministic but stateful across parallel runs.

**Verification, evidence, and uncertainty.** Confirm each tradeoff row names its cost, its trigger condition, and its verification question. The when-to-keep-command-hooks section and the hybrid-approach section price the tradeoffs directly. Real latency distributions for prompt hooks are given only as timeout defaults, not measurements.

**Second-order consequence.** The hybrid pattern dissolves the first tradeoff instead of picking a side, a quick command check approves the obvious and the prompt hook reasons about the rest, paying latency only on ambiguous cases.

**Revision decision.** Add three concrete rows, type choice by check character and latency budget, severity choice by false-positive cost, and system choice by who must receive the guardrail.

**Retained seed evidence.** The adopt, adapt, avoid, and cost-of-being-wrong rows remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| decision_option_name | when_to_choose_condition | tradeoff_cost_description | verification_question_prompt |
| --- | --- | --- | --- |
| Adopt when | local corpus and external evidence agree on the plugin hook development patterns pattern | fastest path, but can copy stale local assumptions | Does the selected pattern appear in the canonical source and current external evidence? |
| Adapt when | local sources are strong but public ecosystem guidance has changed | preserves repo fit, but requires explicit inference notes | Did the reference label the local fact, external fact, and combined inference separately? |
| Avoid when | source evidence is thin, conflicting, or unrelated to the user journey | prevents false confidence, but may require deeper research | Is there a confidence warning or adjacent reference route? |
| Cost of being wrong | wrong plugin hook development patterns guidance can send an agent to the wrong files, tests, or abstraction | wasted implementation loop and weaker verification | Would a reviewer know what to undo and what to inspect next? |

## Local Corpus Hierarchy

**Decision supported.** This section helps decide which text settles a conflict between hook claims. The seed hierarchy labels the hook-development skill a legacy historical source while it is the canonical API text the three reference files explicitly extend.

**Recommended default and causal basis.** Resolve API disputes from the matching SKILL.md and pattern disputes from the reference file that owns the pattern. Each reference file opens by naming itself an extension, patterns as starting points, migration as a guide from basic to advanced, advanced for when basic hooks are insufficient.

**Operating conditions and assumptions.** Claims stay within one system, cross-system claims need both canonical texts. The hierarchy ranks this theme's five texts for claim authority, not for reading pleasure.

**Failure boundary and alternatives.** A reader trusting the seed's legacy label would discount the only text defining output schemas, exit codes, and environment variables. Bounded alternatives and recoveries: recency-based ranking once live copies diverge, or authority by specificity with the most detailed text winning.

**Counterexample, gotchas, and operational comparison.** Advanced.md's hook-chaining example contradicts the skill's independence rule unless its sequential-events-only caveat travels with it. Good: settling an exit-code question from SKILL.md over a pattern comment. Bad: citing the archive copy as older and therefore more authoritative than its identical live twin. Borderline: trusting advanced.md's caching numbers, plausible but illustrative.

**Verification, evidence, and uncertainty.** Confirm the hierarchy column now matches each file's self-declared role. The reference files' own opening lines and the byte-identity checks ground the reranking. Whether upstream plugin-dev has since revised these files is unknowable from the archive.

**Second-order consequence.** The two canonical texts never cite each other, hookify and plugin hooks are parallel systems joined only by the shared event vocabulary, so neither can settle a dispute about the other.

**Revision decision.** Rank both SKILL.md files canonical for their own systems, the three reference files supporting detail, and the live copies duplicates by byte-identity rather than independent witnesses.

**Retained seed evidence.** All hierarchy rows with their heading-signal and reviewer-question columns remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Classification vocabulary includes canonical, supporting, legacy, duplicate, and conflicting source roles.

| local_source_filepath_value | corpus_hierarchy_role | heading_signal_to_convert | reviewer_question_to_answer |
| --- | --- | --- | --- |
| agents-used-monthly-archive/claude-skills-202603/plugins/hookify/SKILL.md | canonical primary source | Writing Hookify Rules; Overview; Rule File Format | What guidance, warning, or example should this source contribute to Plugin Hook Development Patterns? |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/hook-development/SKILL.md | legacy historical source | Hook Development for Claude Code Plugins; Overview; Hook Types | What guidance, warning, or example should this source contribute to Plugin Hook Development Patterns? |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/hook-development/references/advanced.md | supporting detail source | Advanced Hook Use Cases; Multi-Stage Validation; !/bin/bash | What guidance, warning, or example should this source contribute to Plugin Hook Development Patterns? |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/hook-development/references/migration.md | supporting detail source | Migrating from Basic to Advanced Hooks; Why Migrate?; Migration Example: Bash Command Validation | What guidance, warning, or example should this source contribute to Plugin Hook Development Patterns? |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/hook-development/references/patterns.md | supporting detail source | Common Hook Patterns; Pattern 1: Security Validation; Pattern 2: Test Enforcement | What guidance, warning, or example should this source contribute to Plugin Hook Development Patterns? |
| claude-skills/plugins/hookify/SKILL.md | supporting context source | Writing Hookify Rules; Overview; Rule File Format | What guidance, warning, or example should this source contribute to Plugin Hook Development Patterns? |
| claude-skills/plugins/plugin-dev/hook-development/SKILL.md | supporting context source | Hook Development for Claude Code Plugins; Overview; Hook Types | What guidance, warning, or example should this source contribute to Plugin Hook Development Patterns? |
| claude-skills/plugins/plugin-dev/hook-development/references/advanced.md | supporting detail source | Advanced Hook Use Cases; Multi-Stage Validation; !/bin/bash | What guidance, warning, or example should this source contribute to Plugin Hook Development Patterns? |
| claude-skills/plugins/plugin-dev/hook-development/references/migration.md | supporting detail source | Migrating from Basic to Advanced Hooks; Why Migrate?; Migration Example: Bash Command Validation | What guidance, warning, or example should this source contribute to Plugin Hook Development Patterns? |
| claude-skills/plugins/plugin-dev/hook-development/references/patterns.md | supporting detail source | Common Hook Patterns; Pattern 1: Security Validation; Pattern 2: Test Enforcement | What guidance, warning, or example should this source contribute to Plugin Hook Development Patterns? |

## Theme Specific Artifact

**Decision supported.** This section helps decide what written form a guardrail must take before implementation. The seed artifact names a hook lifecycle map without the fields the corpus makes mandatory, event, matcher, hook type, timeout, output contract, escalation action, and restart note.

**Recommended default and causal basis.** Fill the artifact before writing hooks.json and attach it to the plugin README as the bypass and debug documentation. Every worked configuration in the corpus carries exactly these parts, a matcher string, a typed hook with optional timeout, and a documented output schema per event family.

**Operating conditions and assumptions.** Hooks are declarative hooks.json entries, hookify rules compress the same fields into frontmatter plus message body. The artifact template covers one guardrail's lifecycle, a plugin-wide hooks.json aggregates several such maps.

**Failure boundary and alternatives.** A lifecycle map missing the output contract cannot be reviewed, PreToolUse returns permissionDecision while Stop returns decision and reason, and confusing them yields silently ignored output. Bounded alternatives and recoveries: generate the artifact from hooks.json by script, losing intent, or skip it for single-hook plugins.

**Counterexample, gotchas, and operational comparison.** Plugin hooks.json wraps events in a hooks object while settings-format hooks sit at top level, an artifact silent on format breeds copy-paste breakage. Good: a row reading Stop, *, prompt, 30s, decision-plus-reason, block, tested-via-debug. Bad: a hooks.json with no record of why the matcher targets Write|Edit. Borderline: timeout left to defaults, acceptable since the corpus documents 60s command and 30s prompt defaults.

**Verification, evidence, and uncertainty.** Review the artifact row against the event's documented output schema before merging. The hook-configuration formats and output-format sections supply every artifact field. Whether teams sustain artifact upkeep across hook revisions is a process claim the corpus cannot settle.

**Second-order consequence.** The seven fields are exactly what claude --debug cannot reconstruct after the fact, the intent behind the matcher and the chosen escalation level live only in the artifact.

**Revision decision.** Define the artifact as a seven-field row per hook, event, matcher, type, timeout, output contract, escalation level, and test evidence from the three-layer kit.

**Retained seed evidence.** The artifact table's field, completion-rule, and evidence-hint columns remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Theme specific artifact: hook lifecycle map with bypass policy, safety constraints, and debug workflow.

| artifact_field_name | artifact_completion_rule | evidence_source_hint |
| --- | --- | --- |
| user_goal_statement | state the user's concrete goal before applying Plugin Hook Development Patterns | local corpus hierarchy plus critique findings |
| decision_boundary_rule | define the point where this reference should be used or avoided | decision tradeoff guide |
| verification_gate_rule | define the command, checklist, or review question that proves the artifact worked | verification gate command set |

## Worked Example Set

**Decision supported.** This section helps decide which concrete exemplar a new hook should be built from. The seed examples speak abstractly while the corpus ships ten numbered patterns with full JSON and scripts, security validation, test enforcement, context loading, notification logging, MCP monitoring, build verification, permission confirmation, quality checks, flag-file activation, and configuration-driven hooks.

**Recommended default and causal basis.** Start from the nearest catalog pattern and adapt its matcher and criteria rather than composing hooks from scratch. Patterns.md presents each with configuration, use-for guidance, and where needed a complete bash script such as load-context.sh detecting project type into $CLAUDE_ENV_FILE.

**Operating conditions and assumptions.** The adapted pattern's event contract is re-checked against SKILL.md, catalog JSON shows event structure without the plugin wrapper. The example set illustrates hook construction, it does not exhaust the pattern catalog's ten entries.

**Failure boundary and alternatives.** Abstract good-bad-borderline lines cannot show a newcomer what a correct matcher, prompt, and output schema actually look like together. Bounded alternatives and recoveries: example-free minimal rules from hookify's quick reference, or the marketplace security-guidance plugin as a live exemplar.

**Counterexample, gotchas, and operational comparison.** Pattern scripts use $$ for temp-file naming, which advanced.md then reuses across hooks where separate processes make it a different value. Good: adapting test-enforcement into build verification by swapping criteria. Bad: copying the before-migration regex script as a template. Borderline: flag-file activation for a temporary debug hook, sanctioned yet restart-bound.

**Verification, evidence, and uncertainty.** Confirm each exemplar cites its pattern number and carries its use-for line. Patterns.md's ten entries and migration.md's before-after pair supply every exemplar named. Whether the ten patterns cover the actual frequency distribution of team needs is unmeasured.

**Second-order consequence.** The catalog's combinable design is its quiet lesson, the pattern-combinations section layers write validation, bash validation, completeness checks, and context loading into one hooks.json without interference because each hook stays independent.

**Revision decision.** Anchor good on pattern 2's test-enforcement Stop hook, bad on migration.md's before-script that greps only literal rm -rf, and borderline on pattern 9's flag-file hooks that work but demand a restart after every toggle.

**Retained seed evidence.** The good, bad, and borderline seed lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Good example: Use Plugin Hook Development Patterns after loading the canonical source, confirming the external evidence boundary, and writing a verification gate before implementation.
Bad example: Use Plugin Hook Development Patterns as a generic tutorial while ignoring the mapped local paths, source hierarchy, and cost of being wrong.
Borderline case: Use Plugin Hook Development Patterns only after adding a confidence warning when local evidence is thin or conflicts with current ecosystem guidance.

## Outcome Metrics and Feedback Loops

**Decision supported.** This section helps decide which signals prove a shipped guardrail is helping rather than hurting. The seed metrics name install-and-debug ease while the corpus implies hook-specific signals, false-positive rate per guardrail, hook timeout frequency, and time from incident to shipped rule.

**Recommended default and causal basis.** Review each guardrail's trigger log before promoting severity and after any prompt-criteria edit. The escalation ladder from warn to ask to block only functions if someone counts wrong triggers, and the timeout defaults only protect flow if exceedances are noticed.

**Operating conditions and assumptions.** Trigger events are visible somewhere durable, the corpus's audit-logging pattern supplies the append-only log if nothing else does. The metrics govern shipped hooks in use, construction-time checks live in the verification gate.

**Failure boundary and alternatives.** A guardrail with unmeasured false positives drifts to either ignored warnings or resented blocks, and either way the incident it guards recurs. Bounded alternatives and recoveries: user-complaint-driven review only, or debug-mode spot checks without durable logs.

**Counterexample, gotchas, and operational comparison.** Prompt hooks give non-deterministic verdicts, so a false-positive rate needs a sample of runs, not a single replay. Good: a warn rule promoted to ask after two clean weeks of trigger review. Bad: a block hook shipped and never re-examined. Borderline: measuring only timeout counts, cheap but blind to accuracy.

**Verification, evidence, and uncertainty.** Confirm each shipped hook names its trigger log location and review cadence. The action-field semantics, timeout defaults, and audit-logging pattern ground each loop. Acceptable false-positive thresholds are judgment calls the corpus does not quantify.

**Second-order consequence.** Hookify makes the first loop nearly free, toggling enabled false parks a noisy rule without deleting its logic, so the cost of measuring is a frontmatter edit.

**Revision decision.** Add three loops, sample triggered hooks weekly for false positives before any block promotion, alert on repeated hook timeouts, and track incident-to-rule lead time as the system's responsiveness.

**Retained seed evidence.** The leading indicator, failure signal, and review cadence lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Leading indicator: users can install, invoke, debug, and remove the extension without reading implementation code.
Failure signal: the reference confuses adjacent extension types or omits failure recovery.
Review cadence: Re-run the verifier after every generated-reference edit and refresh external sources when public APIs, docs, or tooling releases change.

## Completeness Checklist

**Decision supported.** This section helps decide when a hook change may be declared done. The seed checklist audits document sections while a hook is complete only when its event, matcher, type, output schema, tests, and restart step are all in place.

**Recommended default and causal basis.** Run the extended checklist on every new hook and after any edit to matcher, prompt, or script. The implementation workflow enumerates nine steps ending in schema validation, sample-input tests, debug-mode verification, and README documentation.

**Operating conditions and assumptions.** One person can verify all items, cross-plugin interactions need the parallel-execution review beyond this list. The checklist gates individual hook completion, plugin-wide review aggregates it per hooks.json entry.

**Failure boundary and alternatives.** A hook passing the seed's document checks can still ship with an output schema from the wrong event family and fail silently at runtime. Bounded alternatives and recoveries: encode the items into hook-linter.sh checks, or fold them into PR templates.

**Counterexample, gotchas, and operational comparison.** Matchers are case-sensitive, so a checklist pass on write instead of Write still ships a dead hook. Good: a PR showing all seven items with command output. Bad: done claimed after the script merely looks right. Borderline: skipping the restart item for a docs-only edit, safe but habit-eroding.

**Verification, evidence, and uncertainty.** Confirm the checklist's new items each map to a corpus-stated failure they prevent. The implementation workflow and matcher notes state every appended item. Checklist fatigue over many small hooks is a human factor outside the corpus.

**Second-order consequence.** The checklist doubles as the debugging script in reverse, when a hook misbehaves, walking the same items top-down localizes the fault, wrong event, wrong matcher, wrong schema, in that order.

**Revision decision.** Append seven hook items, event matches lifecycle intent, matcher case-sensitivity checked, type justified against the determinism rule, output schema matches the event family, variables quoted and paths portable, all three verification layers run, and session restarted before live testing.

**Retained seed evidence.** All seven seed checklist bullets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- The role scenario names the user, starting state, decision, and trigger for Plugin Hook Development Patterns.
- The decision guide includes Adopt when, Adapt when, Avoid when, and Cost of being wrong.
- The local corpus hierarchy identifies canonical and supporting sources or gives a confidence warning.
- The theme specific artifact is concrete enough to review without reading every mapped source.
- The examples cover good, bad, and borderline usage.
- The metrics section names one leading indicator and one failure signal.
- The adjacent routing section points to a better reference when this one is not the right fit.

## Adjacent Reference Routing

**Decision supported.** This section helps decide when a task should leave this reference for a neighbor. The seed routing names plugin, hook, and development neighbors without the boundaries the corpus itself draws, hookify for user-local rules, plugin surfaces for commands and MCP, and settings files for direct user hooks.

**Recommended default and causal basis.** Apply the three tests before opening this reference, and exit to the matching neighbor on the first mismatch. Hook-development distinguishes plugin hooks.json format from settings format explicitly, and hookify positions its rules as needing no plugin at all.

**Operating conditions and assumptions.** The adjacent references exist in the corpus generation, otherwise the route names the concept for external search. The routing covers surfaces adjacent to hook construction, not the whole extension taxonomy.

**Failure boundary and alternatives.** A task about a personal .claude settings hook routed into plugin-format guidance yields a wrapper-object mismatch that fails to load. Bounded alternatives and recoveries: keep all extension guidance in one oversized reference, or route by filename convention alone.

**Counterexample, gotchas, and operational comparison.** The mcp__.*__delete.* matcher example shows the surfaces composing, a hook guarding MCP tools needs both references at once. Good: a slash-command request routed out to command guidance. Bad: forcing settings-format hooks through plugin-format examples. Borderline: a hook that validates MCP tool calls, legitimately astride both references.

**Verification, evidence, and uncertainty.** Confirm each route names its test condition and its destination concept. The format-distinction and hookify-positioning passages ground each boundary. The corpus generation's actual coverage of command and MCP references was not enumerated here.

**Second-order consequence.** The seed map's MCP URLs make sense here rather than in evidence, MCP is this theme's most confusable neighbor because both wire external behavior into the session, hooks react to events while MCP serves tools and resources.

**Revision decision.** Route by three tests, personal-versus-distributed to hookify or plugins, event-driven-versus-invoked to hooks or commands, and in-session-versus-external-context to hooks or MCP references.

**Retained seed evidence.** The three seed adjacent-reference lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Adjacent reference guidance: Use command, hook, MCP, settings, or manifest references when one extension surface is already selected.
Adjacent reference 1: consider the plugin adjacent reference when the current task pivots away from plugin hook development patterns.
Adjacent reference 2: consider the hook adjacent reference when the current task pivots away from plugin hook development patterns.
Adjacent reference 3: consider the development adjacent reference when the current task pivots away from plugin hook development patterns.

## Workload Model

**Decision supported.** This section helps decide how much hook machinery a session can carry before latency degrades flow. The seed model bounds generic sessions while hook workloads have their own axes, events fire on every matching tool call, all matching hooks run in parallel, and each hook holds a private timeout budget.

**Recommended default and causal basis.** Narrow matchers first, order hybrid stages cheap-to-expensive, and cap prompt hooks on high-frequency events. The parallel-execution section shows three hooks on one Write matcher running simultaneously, and the optimization guidance orders quick deterministic checks before expensive reasoning.

**Operating conditions and assumptions.** Tool-call frequency is roughly known, exploratory sessions with heavy file traffic need stricter caps. The model bounds per-session hook execution, plugin distribution scale is out of frame.

**Failure boundary and alternatives.** A session with chatty matchers like * on PreToolUse multiplies every tool call by the full hook set, and one slow hook throttles everything it matches. Bounded alternatives and recoveries: caching validation results in temp files as advanced.md shows, or moving heavy checks to Stop where frequency is lowest.

**Counterexample, gotchas, and operational comparison.** Parallel execution means adding a hook never delays other hooks, but every hook still delays the tool call it gates. Good: a five-second cache on repeated file-path validations. Bad: a 15s prompt hook matching every Bash call in a script-heavy session. Borderline: three parallel command checks on Write, individually cheap, jointly gating every save.

**Verification, evidence, and uncertainty.** Confirm high-frequency matchers carry either deterministic hooks or an explicit latency justification. The parallel-execution, optimization, and caching sections supply the model's terms. Real matcher hit-rate distributions across sessions are unmeasured in the corpus.

**Second-order consequence.** Matcher specificity is the cheapest capacity lever, narrowing Write|Edit to a file-type condition cuts invocations without touching any hook body, which is why hookify's condition lists exist.

**Revision decision.** Model the workload as matcher hit rate times hook cost, with command hooks budgeted in milliseconds, prompt hooks in tens of seconds, and totals reviewed per event.

**Retained seed evidence.** All workload rows with their boundary and pressure-point columns remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`combined_evidence_inference_note`: Treat Plugin Hook Development Patterns as a agent workflow operating reference, not as a prose summary.

| workload_dimension_name | workload_boundary_value | verification_pressure_point |
| --- | --- | --- |
| primary_usage_surface | agent planning, tool use, context loading, delegation, or skill/plugin execution where bad guidance compounds across long-running sessions | verify that the reference changes the next implementation or review action |
| bounded_capacity_model | one primary task, up to 10 source files, up to 3 delegated subtasks, and a written completion audit for every run | split the task or create a narrower reference when this boundary is exceeded |
| source_pressure_model | local heading signals include Writing Hookify Rules; Overview; Rule File Format; Basic Structure; Frontmatter Fields; Advanced Format (Multiple Conditions); Hook Development for Cl | compare guidance against canonical local sources before following external examples |
| artifact_pressure_model | required artifact is hook lifecycle map with bypass policy, safety constraints, and debug workflow | require the artifact before claiming the reference is operationally usable |

## Reliability Target

**Decision supported.** This section helps decide what an individual hook must guarantee to be trusted in the loop. The seed targets track document hygiene while hook reliability has sharper contracts, valid JSON out of every hook, correct exit-code semantics, graceful handling of missing input, and zero secret leakage into logs.

**Recommended default and causal basis.** Test all four targets with sample and hostile inputs before shipping, and re-test after any script edit. The output-format section fixes the contract, exit 0 shows stdout, exit 2 feeds stderr back to Claude, other codes are non-blocking, and the DONT list bans logging sensitive information.

**Operating conditions and assumptions.** Command hooks under test, prompt-hook reliability rests on the runtime honoring its decision schema. The targets bind individual hook executions, plugin-level reliability aggregates them.

**Failure boundary and alternatives.** A hook emitting malformed JSON or the wrong exit code degrades into noise, its verdicts silently ignored while its author believes the guardrail stands. Bounded alternatives and recoveries: wrap all hooks in a shared harness enforcing the contract, or accept fail-open and rely on Stop-time review.

**Counterexample, gotchas, and operational comparison.** Set -euo pipefail hardens scripts but converts unexpected conditions into silent fail-open exits unless traps are added. Good: a validator returning continue-true with a skip message on missing files. Bad: an uncaught cat crash approving by accident. Borderline: exit 1 on config errors, non-blocking by contract yet easy to misread as denial.

**Verification, evidence, and uncertainty.** Pipe hostile, empty, and valid inputs through each hook and check output parse plus exit code. The exit-code table, error-handling example, and security DONT list state each target. Whether the runtime's exit-code handling has changed since the archive snapshot is unverified.

**Second-order consequence.** Exit 2 is the only blocking signal, so reliability is asymmetric, a crash with code 1 fails open and lets the operation through, meaning defensive hooks must treat their own errors as approvals they never intended.

**Revision decision.** Set four targets, every execution path emits jq-parseable output, exit codes match the documented semantics, hostile or missing input yields a graceful skip not a crash, and no secret ever reaches transcript or audit log.

**Retained seed evidence.** All reliability rows with their threshold and evidence-method columns remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| reliability_target_name | measurable_threshold_value | evidence_collection_method |
| --- | --- | --- |
| source_boundary_preservation | 100 percent of recommendations keep local, external, and inference boundaries visible | review generated text for the three evidence labels before reuse |
| decision_accuracy_sample | at least 18 of 20 sampled uses route to the correct adopt, adapt, avoid, or adjacent-reference decision | sample downstream tasks and record reviewer verdicts |
| unsupported_claim_rate | zero unsupported production, security, latency, or reliability claims in final guidance | reject claims without source row, explicit inference note, or verification method |
| recovery_path_clarity | every avoid or failure case names the rollback, escalation, or next-reference route | inspect failure-mode and adjacent-routing sections together |

## Failure Mode Table

**Decision supported.** This section helps decide which hook failure modes need standing detection rather than incident-time discovery. The seed table lists corpus-drift failures while the corpus documents runtime hook failures, hooks not firing after config edits, matcher typos silently matching nothing, timeouts killing slow validators, and parallel hooks racing on shared temp files.

**Recommended default and causal basis.** After any hook change, restart, run /hooks to confirm registration, and exercise one matching event under debug. The lifecycle section states hooks cannot be hot-swapped and require restart, the matcher notes state case sensitivity, and the pitfalls section shows $$-keyed state failing across parallel processes.

**Operating conditions and assumptions.** The session is restartable, long-lived shared sessions widen the stale-config window. The table catalogs runtime and configuration failures of hooks themselves, document-generation failures stay in the seed rows.

**Failure boundary and alternatives.** Each documented mode is silent, no error surfaces when an edited hooks.json is stale or a lowercase matcher never fires, so the guardrail's absence is discovered only by the incident it missed. Bounded alternatives and recoveries: CI checks that lint matchers against tool-name lists, or convention tests that fire each hook synthetically.

**Counterexample, gotchas, and operational comparison.** Startup validation catches malformed JSON but only warns on missing scripts, so a renamed script fails later, not at load. Good: a release ritual of restart, /hooks, and one debug-mode probe. Bad: three config edits in one session tested against the first. Borderline: trusting startup warnings to catch script drift, partial coverage at best.

**Verification, evidence, and uncertainty.** Confirm each added row pairs a silent failure with an observable detection signal. The lifecycle, matcher, timeout, and pitfalls passages document all four modes. Frequency ranking among the four modes is not derivable from the corpus.

**Second-order consequence.** The shared property of all four is silence, which elevates claude --debug and /hooks from conveniences to the only instruments that make these failures observable at all.

**Revision decision.** Add four rows, stale-session config with restart as mitigation, dead matcher with /hooks inspection as detection, timeout kill with budget review, and state races with independence redesign.

**Retained seed evidence.** All failure rows with their trigger and mitigation columns remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| failure_mode_name | likely_trigger_condition | required_mitigation_action |
| --- | --- | --- |
| source drift hides truth | external or local guidance changes after the reference was written | refresh public evidence, rerun local corpus gate, and mark stale claims before reuse |
| generic advice escapes review | agent copies plausible best practices without theme-specific verification | block completion until the verification gate names concrete command, reviewer question, or metric |
| context window loses plan | long-running session forgets early constraints or overwrites user intent | write checkpoint summaries and re-read plan before each destructive step |
| tool fanout outruns budget | parallel actions create conflicts, duplicate work, or unbounded external calls | cap fanout, assign ownership, and require merge/audit checkpoints |

## Retry Backpressure Guidance

**Decision supported.** This section helps decide how agents and builders should respond when hooks push back. The seed guidance covers corpus-refresh retries while hooks need their own policy, a denied operation is a verdict to respect, a timeout is a budget signal, and rate limiting is a pattern hooks themselves can implement.

**Recommended default and causal basis.** One modified retry after a deny with changed input, zero verbatim retries, and caching before timeout raises. Advanced.md ships a rate-limiting hook denying after ten commands per minute, and the timeout defaults define when the runtime abandons a hook rather than waiting.

**Operating conditions and assumptions.** Deny reasons are informative, a bare deny without explanation invites blind retry and should itself be fixed. The guidance governs behavior around hook verdicts and budgets, not network retries inside hook scripts.

**Failure boundary and alternatives.** An agent retrying a deny verbatim converts a working guardrail into a loop, and raising timeouts to accommodate slow hooks trades the whole session's latency for one check. Bounded alternatives and recoveries: escalate persistent denies to a human instead of any retry, or tune matcher scope so fewer benign operations meet the gate.

**Counterexample, gotchas, and operational comparison.** The ask decision creates a human checkpoint, retrying around it by rephrasing the operation defeats the confirmation it exists to force. Good: a deny answered by narrowing the file path and retrying once. Bad: resubmitting an identical rm command until the limiter trips. Borderline: raising one validator's timeout from 5 to 15 seconds, legal but a smell that staging is missing.

**Verification, evidence, and uncertainty.** Confirm deny paths carry reasons and retry behavior around them is logged. The rate-limiting pattern, timeout defaults, and permission-decision semantics ground each rule. How gracefully agents actually behave after ask-decisions is behavioral territory the corpus does not measure.

**Second-order consequence.** Hooks invert the usual retry frame, they are the backpressure mechanism, the rate-limiting pattern shows the guardrail side deliberately pushing back on the agent rather than the agent retrying past it.

**Revision decision.** Add three rules, treat deny as terminal until the input genuinely changes, treat repeated timeouts as a redesign signal toward hybrid staging or caching, and implement frequency caps as hooks when runaway operations are the risk.

**Retained seed evidence.** All five seed guidance bullets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- Retry only after the failed verification signal is classified as transient, stale evidence, missing context, or true contradiction.
- Use one bounded retry for stale external evidence refresh, then escalate to a human or a narrower source-specific reference.
- Apply backpressure by stopping new generation or implementation work when source coverage, critique coverage, or verification gates are red.
- For long-running agent workflows, checkpoint after each batch and re-read the current spec before any broad rewrite, commit, push, or destructive operation.
- For distributed execution, assign one owner per generated file or theme batch and require merge-time verification of exact path, heading, and evidence-boundary invariants.

## Observability Checklist

**Decision supported.** This section helps decide which signals must be captured for hooks to be debuggable and accountable. The seed checklist logs corpus-session facts while hook observability has named instruments, claude --debug for registration and timing, /hooks for the loaded set, audit-log hooks for durable trails, and systemMessage for in-transcript explanation.

**Recommended default and causal basis.** Verbose systemMessage on deny and ask paths, quiet approvals, and durable audit lines for destructive-operation matchers. The debugging section says to look for hook registration, execution logs, input-output JSON, and timing information under debug mode, and the audit pattern appends timestamp, user, tool, and input per event.

**Operating conditions and assumptions.** Logs stay secret-free, the audit pattern writes raw input and must be scrubbed where inputs may carry credentials. The checklist observes hooks in operation, construction-time verification lives in the gate section.

**Failure boundary and alternatives.** Without these instruments the failure-mode table's silent modes stay invisible, an unregistered hook and a never-matching matcher look identical to absence of events. Bounded alternatives and recoveries: metrics emission to statsd as advanced.md sketches, or database logging where compliance demands query access.

**Counterexample, gotchas, and operational comparison.** Debug output exists only for sessions launched with the flag, a failure in a normal session leaves no trace to inspect afterward. Good: a deny whose systemMessage names the rule and the offending pattern. Bad: a silent block leaving the agent guessing. Borderline: audit-logging full tool input, complete but a secret-leak risk the security list warns about.

**Verification, evidence, and uncertainty.** Confirm each shipped hook states its transcript verbosity and its durable-log destination if any. The debugging, standard-output, and audit-logging passages name every instrument. The transcript retention and privacy properties of systemMessage content are runtime details beyond the archive.

**Second-order consequence.** SuppressOutput and systemMessage make observability a designed property per hook, each hook chooses what the transcript shows, so silent hooks are a choice that should be deliberate rather than a default.

**Revision decision.** Add four items, capture debug output on every release probe, snapshot /hooks after each restart, run an audit-log hook where accountability matters, and have deny paths explain themselves via systemMessage.

**Retained seed evidence.** All six seed checklist bullets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- Record which local sources were loaded and which were intentionally skipped.
- Record the exact verification command, reviewer question, or rendered artifact used as proof.
- Record p50/p95/p99 latency or reviewer-time measurements when the reference affects runtime or workflow speed.
- Capture tool-call count, context files loaded, delegated tasks, retry count, and completion-audit outcome.
- Record leading indicator and failure signal from this file in the coverage manifest or journal when the reference drives real work.
- Keep audit evidence small enough to review: command output summary, changed-file list, and unresolved-risk notes are preferred over raw transcript dumps.

## Performance Verification Method

**Decision supported.** This section helps decide how hook cost is proven acceptable before and after changes. The seed method demands latency packets generically while hook performance has two documented levers with numbers, timeout ceilings of 60 seconds for command and 30 for prompt hooks, and a five-minute result cache shown in advanced.md.

**Recommended default and causal basis.** Measure under debug before and after any hook addition on PreToolUse or file-event matchers, the highest-frequency surfaces. The optimization guidance orders the method, use command hooks for quick deterministic checks, prompt hooks for complex reasoning, cache validation results in temp files, and minimize I/O in hot paths.

**Operating conditions and assumptions.** Debug timing output is available, otherwise bracket hook cost by toggling the plugin and comparing session feel. The method verifies hook execution cost, model-side prompt evaluation cost is observable only as wall-clock.

**Failure boundary and alternatives.** An unverified hook stack degrades every gated tool call, and because hooks run before the tool, users experience the cost as global session sluggishness with no obvious culprit. Bounded alternatives and recoveries: synthetic benchmarks piping canned inputs through hooks in a loop, or acceptance of defaults until users complain.

**Counterexample, gotchas, and operational comparison.** Sub-50ms is the corpus's threshold for keeping a check in bash, but the measurement must include jq parsing overhead the scripts all carry. Good: a timing diff showing the new write-validator adds 12ms p50. Bad: shipping a prompt hook on Bash with no timing at all. Borderline: relying on the 30s default as implicit budget, permitted yet unexamined.

**Verification, evidence, and uncertainty.** Confirm the packet fields exist for each high-frequency hook and exceedances are zero. The timeout defaults, optimization list, and caching example supply the numbers and levers. Prompt-hook latency variance across model versions is outside anything the archive can state.

**Second-order consequence.** The deepest lever is architectural rather than tunable, the hybrid pattern converts p99 pain into a two-tier cost curve where the cheap tier absorbs the common case and the expensive tier prices only ambiguity.

**Revision decision.** Define the packet as per-hook wall-clock under debug timing, matcher hit counts per session, cache hit rate where caching exists, and timeout-exceedance count as the hard failure line.

**Retained seed evidence.** The leading indicator, failure signal, measurement packet, and pass-fail lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Performance method: require tool-call budgets, timeout budgets, and a resumable journal when the workflow exceeds one focused session.
Leading indicator to measure: users can install, invoke, debug, and remove the extension without reading implementation code.
Failure signal to watch: the reference confuses adjacent extension types or omits failure recovery.
Required measurement packet: capture input size, source count, tool-call count, wall-clock time, p50/p95/p99 latency where runtime applies, and reviewer decision time where documentation applies.
Pass condition: the reference must let a reviewer identify the correct next action, verification gate, and stop condition without reading unrelated files.
Fail condition: the reference encourages implementation before the workload, reliability target, and failure-mode table are explicit.

## Scale Boundary Statement

**Decision supported.** This section helps decide when a guardrail has outgrown hooks and needs a different enforcement plane. The seed statement bounds corpus generation while hook machinery has its own edges, per-session parallel execution with no cross-hook state, restart-bound configuration, and a single hooks.json per plugin merged with user hooks.

**Recommended default and causal basis.** Keep hooks stateless and per-session, and escalate to external systems the moment two sessions or two users must agree. The corpus states plugin hooks merge with user hooks and run in parallel, state sharing works only across sequential events, and configuration loads once per session.

**Operating conditions and assumptions.** The session model matches the archive's description, remote contexts flagged by CLAUDE_CODE_REMOTE may alter file-system assumptions. The boundary statement marks where hook-level design stops sufficing, not where automation itself should stop.

**Failure boundary and alternatives.** Past these edges the pitfalls arrive, cross-hook temp-file protocols race, per-session counters reset invisibly, and fleet-wide policy pushed through personal hookify files fragments per machine. Bounded alternatives and recoveries: a coordinating MCP server for cross-session state, or repository-level enforcement through CI gates.

**Counterexample, gotchas, and operational comparison.** The $$-keyed temp files in corpus examples scope state to a process, quietly narrower than the session scope a reader might assume. Good: team policy shipped as a plugin with versioned hooks.json. Bad: fleet compliance assumed from a README asking everyone to copy a hookify file. Borderline: a SessionEnd hook exporting counters to a shared log, at the boundary and leaning on external durability.

**Verification, evidence, and uncertainty.** Confirm designs crossing an edge name their external mechanism explicitly. The merge-and-parallel, state-sharing, and environment-variable passages define each edge. Enterprise-scale policy tooling above plugins is entirely outside the archive.

**Second-order consequence.** Hooks are a session-scoped enforcement plane, everything they know dies at session end unless a hook exports it, which is why SessionEnd cleanup and audit exports appear in the corpus as the bridge to durable systems.

**Revision decision.** State three edges, coordination beyond one event sequence needs external state with real locking, policy beyond one user needs plugin distribution rather than hookify convention, and enforcement beyond the session needs CI or server-side controls hooks cannot provide.

**Retained seed evidence.** All four seed boundary paragraphs remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Plugin Hook Development Patterns stops being sufficient when the task spans multiple independent systems, more than one ownership boundary, unbounded source discovery, or production traffic without an explicit SLO.
Under distributed execution, split work by theme file and preserve one verification owner per split; do not let parallel agents rewrite the same reference without a merge checkpoint.
Under long-running agent workflows, treat context drift as a reliability failure: checkpoint state, summarize open risks, and verify against the spec before continuing.
Under large-codebase scale, require dependency or source-graph narrowing before applying this reference; a source list without ranked canonical guidance is not enough.

## Future Refresh Search Queries

**Decision supported.** This section helps decide which searches will actually catch drift in this reference's claims. The seed queries search the generic theme phrase while refresh should target the volatile contracts, hook event catalog, output schemas, timeout defaults, prompt-hook event support, and hookify rule syntax.

**Recommended default and causal basis.** Fetch the official docs first each refresh cycle, then diff the event table, output schemas, and defaults against this file. These are exactly the claims this file labels archive-local, and hook-development itself points refresh at the official docs URL and claude --debug behavior.

**Operating conditions and assumptions.** The docs URL still resolves, otherwise search the vendor documentation root for the hooks section. The queries serve refresh of this reference, not general hook education.

**Failure boundary and alternatives.** Generic queries return tutorials repeating the archive while a changed permissionDecision schema or a widened prompt-hook event list goes undetected. Bounded alternatives and recoveries: watch the marketplace security-guidance plugin for working-code drift, or subscribe to release notes if a changelog surface exists.

**Counterexample, gotchas, and operational comparison.** Community tutorials lag releases, a query answered by blog posts can look fresher than the archive while being equally stale. Good: a query surfacing a new hook event missing from the nine listed here. Bad: a query returning the same archive text mirrored on a blog. Borderline: querying MCP hook integration, adjacent but a real composition surface.

**Verification, evidence, and uncertainty.** Confirm each query maps to a named archive-local claim it would revalidate. The external-resources section and this file's own boundary labels select the targets. Which claims have already drifted since the archive snapshot is unknowable until the fetches run.

**Second-order consequence.** The highest-value single fetch is the official hooks page the skill already cites, one retrieval either revalidates or invalidates most archive-local claims at once, making it the cheapest refresh anchor.

**Revision decision.** Add targeted queries for the claude code hooks documentation, hooks.json schema changes, prompt hook supported events, hook timeout configuration, and hookify rule frontmatter fields.

**Retained seed evidence.** The three seed query rows remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| search_query_label_name | search_query_text_value |
| --- | --- |
| `official_docs_query_phrase` | plugin hook development patterns official documentation best practices |
| `github_repository_query_phrase` | plugin hook development patterns GitHub repository examples |
| `release_notes_query_phrase` | plugin hook development patterns changelog release notes migration |

## Evidence Boundary Notes

**Decision supported.** This section helps decide which confidence label each claim in this file must carry. The seed notes define three labels without this file's actual boundary decisions, five texts read in full, archive-live pairs proven identical, runtime contracts held archive-local, and external URLs left unretrieved.

**Recommended default and causal basis.** Cite design doctrine freely with local-fact labels and hedge every enumeration with its archive-local marker. The strongest available evidence here is full-text reading plus byte-identity checks, while everything about live runtime behavior, event catalogs, schemas, defaults, rests on an archive that names newer authority elsewhere.

**Operating conditions and assumptions.** No newer retrieval has occurred, the first docs fetch should trigger relabeling throughout. The notes bound this document's claims only, downstream reuse must re-evaluate against its own moment.

**Failure boundary and alternatives.** Without these notes a reader cannot tell the settled claims, rule syntax as written in hookify, from the volatile ones, whether prompt hooks now support more than four events. Bounded alternatives and recoveries: a claims ledger with per-claim retrieval dates, or wholesale demotion of all runtime claims until fetched.

**Counterexample, gotchas, and operational comparison.** The corpus's own confidence is seductive, its tables and defaults read as timeless while the lifecycle section quietly admits the runtime evolves. Good: citing the exit-code table with an archive-local marker. Bad: asserting the nine-event catalog as currently exhaustive. Borderline: the timeout defaults, twice-stated locally yet still a runtime contract.

**Verification, evidence, and uncertainty.** Spot-check claims across this file against the four recorded boundary decisions. The reading and diff checks performed during this evolution ground every boundary decision named. The gap between archive snapshot and current runtime is the standing unknown this section exists to flag.

**Second-order consequence.** This theme's evidence risk is asymmetric by claim type, design doctrine like prompt-first and independence ages slowly while enumerable contracts like event lists age per release, so the labels matter most on the enumerations.

**Revision decision.** Record four decisions, local-fact status for all five-text content, duplicate status for live copies by byte-identity, archive-local status for every runtime contract pending a docs fetch, and candidate status for all mapped URLs.

**Retained seed evidence.** The three seed label definitions remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- `local_corpus_sourced_fact`: statements tied directly to the local source paths above.
- `external_research_sourced_fact`: statements tied to the public URLs above.
- `combined_evidence_inference_note`: synthesis that combines local and public evidence into agent guidance.
