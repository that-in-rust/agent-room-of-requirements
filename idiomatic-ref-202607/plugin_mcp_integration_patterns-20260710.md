# Plugin Mcp Integration Patterns

**Decision supported.** This section helps decide which configuration method, transport, and tool-exposure route an external integration should take. The seed title names the theme without its governing pipeline, a plugin bundles an MCP server via .mcp.json or an inline mcpServers field, picks one of four transports, and its tools surface under the mcp__plugin_<plugin>_<server>__<tool> prefix.

**Recommended default and causal basis.** Start from a dedicated .mcp.json at plugin root, choose stdio for local or bundled servers and SSE for hosted OAuth services, and pre-allow specific prefixed tools in commands. The mcp-integration skill states plugins bundle servers in exactly two ways, names stdio, SSE, HTTP, and WebSocket as the supported types, and defines the tool-prefix format that every downstream command must spell out.

**Operating conditions and assumptions.** The plugin runtime performs the documented environment-variable expansion and tool prefixing, both are archive-local contracts until live docs are checked. This reference operationalizes MCP server bundling, transport selection, authentication, and tool consumption inside Claude Code plugins, not MCP server implementation itself.

**Failure boundary and alternatives.** A builder who skips the pipeline hardcodes a server path, picks a transport by habit, then cannot find the tools because the prefixed names were never checked with /mcp. Bounded alternatives and recoveries: shelling out to service CLIs from command hooks, or a standalone user-level MCP configuration outside any plugin.

**Counterexample, gotchas, and operational comparison.** MCP servers start when the plugin enables and configuration changes require restarting Claude Code, so mid-session edits to .mcp.json silently do nothing. Good: a database plugin with .mcp.json, a ${CLAUDE_PLUGIN_ROOT} stdio command, and two pre-allowed tools. Bad: an inline mcpServers block with a hardcoded /Users path. Borderline: inline configuration for a genuine single-server plugin, sanctioned by the skill.

**Verification, evidence, and uncertainty.** Run /mcp after install to confirm the server connects and the prefixed tool names match what commands pre-allow. The mcp-integration SKILL.md states the two methods, four types, naming format, and lifecycle promoted here. How the four-transport catalog and prefix format evolve across Claude Code releases is not verifiable from the archive.

**Second-order consequence.** The whole corpus is a portability argument, ${CLAUDE_PLUGIN_ROOT} for paths, ${VAR} expansion for secrets, and prefixed tool names all exist so one plugin folder installs cleanly on any machine.

**Revision decision.** Open with the two configuration methods, the four transport types, and the tool-naming contract that links server configuration to command frontmatter.

**Retained seed evidence.** The exact theme title and its integration-patterns framing remain unchanged. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

## Source Evidence Mapping Table

**Decision supported.** This section helps decide which recorded source may back which claim about plugin MCP integration. The seed map lists eight local rows without noting they collapse to four texts, one skill plus three reference files, each present as byte-identical archive and live copies.

**Recommended default and causal basis.** Cite the skill for configuration and lifecycle claims, server-types for transport claims, authentication for credential claims, and tool-usage for naming and consumption claims. Diffing every archive path against its claude-skills live counterpart during this evolution produced no differences, so citing both copies of a file adds no corroboration.

**Operating conditions and assumptions.** The live copies stay identical to their archive snapshots, divergence would make the live copies authoritative. The table records provenance for this document's claims and does not rank MCP documentation outside the archive.

**Failure boundary and alternatives.** Treating the eight rows as eight independent witnesses would double-count every MCP claim in this file. Bounded alternatives and recoveries: collapse the map to four evidence units with alias notes, or diff the copies each cycle to catch divergence.

**Counterexample, gotchas, and operational comparison.** The three external URLs appear twice each in the seed rows, and none of the six rows was retrieved during this evolution. Good: citing server-types.md for the stdio process lifecycle. Bad: citing archive and live SKILL.md as two confirmations. Borderline: citing the MCP resources spec URL, mapped with a dated version but never retrieved.

**Verification, evidence, and uncertainty.** Confirm every claim traces to one of the four evidence units and the copy-identity checks are recorded. All eight mapped files were read in full and the four archive-live pairs compared byte-identical during this evolution. Why the seed lists each external URL twice with slightly different role text is unrecorded.

**Second-order consequence.** The four texts split by question type, the skill answers what to configure, server-types answers which transport, authentication answers how credentials flow, and tool-usage answers how commands and agents consume the result.

**Revision decision.** Mark all eight paths read in full, group them into four evidence units, and note the archive-live identity check as the deduplication proof.

**Retained seed evidence.** All source rows with their category, confidence, and synthesis-role columns remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| source_location_path_key | source_category_artifact_type | source_authority_confidence_level | source_usage_synthesis_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/mcp-integration/SKILL.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/mcp-integration/references/authentication.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/mcp-integration/references/server-types.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/mcp-integration/references/tool-usage.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| claude-skills/plugins/plugin-dev/mcp-integration/SKILL.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt |
| claude-skills/plugins/plugin-dev/mcp-integration/references/authentication.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| claude-skills/plugins/plugin-dev/mcp-integration/references/server-types.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| claude-skills/plugins/plugin-dev/mcp-integration/references/tool-usage.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| https://modelcontextprotocol.io/specification/2025-06-18/server/resources | external_research_source_material | external_research_sourced_fact | primary MCP resource model for context sharing |
| https://github.com/modelcontextprotocol/servers | external_research_source_material | external_research_sourced_fact | reference and community server implementation index |
| https://github.com/github/github-mcp-server | external_research_source_material | external_research_sourced_fact | GitHub-backed MCP server for repository and issue operations |
| https://modelcontextprotocol.io/specification/2025-06-18/server/resources | external_research_source_material | external_research_sourced_fact | primary resource-sharing model |
| https://github.com/modelcontextprotocol/servers | external_research_source_material | external_research_sourced_fact | reference server implementation collection |
| https://github.com/github/github-mcp-server | external_research_source_material | external_research_sourced_fact | GitHub platform MCP implementation |

## Pattern Scoreboard Ranking Table

**Decision supported.** This section helps decide which integration rules deserve default adoption when bundling an MCP server. The seed scoreboard scores corpus hygiene while the corpus's load-bearing integration rules go unranked, ${CLAUDE_PLUGIN_ROOT} for every path, environment variables for every token, HTTPS/WSS only, and specific pre-allowed tools over wildcards.

**Recommended default and causal basis.** Apply all four rules on every plugin MCP configuration, checked at review time before install testing. Each rule guards a distinct failure, hardcoded paths break on other machines, hardcoded tokens leak through git, plain HTTP exposes credentials in transit, and wildcard allowlists grant every server tool to one command.

**Operating conditions and assumptions.** Each promoted rule keeps its falsifiable phrasing so a reviewer can point at the violating line. The scoreboard ranks integration-discipline rules for adoption priority and does not rank the four transports against each other.

**Failure boundary and alternatives.** The seed's numeric scores were never measured and the corpus offers only DO and DONT lists, not numbers. Bounded alternatives and recoveries: rank by observed integration-failure frequency once measured, or rank by blast radius with credential leaks first.

**Counterexample, gotchas, and operational comparison.** Tool-usage sanctions wildcards when a command truly needs every tool from a server, so narrow allowance is a default with a documented exception. Good: a config whose only absolute path is ${CLAUDE_PLUGIN_ROOT} and whose README lists API_TOKEN. Bad: a Bearer sk-abc123 literal committed in headers. Borderline: a wildcard allowlist on a genuinely all-tools admin command.

**Verification, evidence, and uncertainty.** Grep the plugin for hardcoded home paths, literal Bearer tokens, http:// or ws:// URLs, and wildcard allowlists. The security best practices and quick-reference DO and DONT lists of SKILL.md state each promoted rule. Which rule violations occur most often in published plugins is unmeasured.

**Second-order consequence.** All four rules are visible in a plain-text review of .mcp.json and command frontmatter, no runtime needed, which makes them the cheapest quality gate in the whole corpus.

**Revision decision.** Promote a top tier of four rules, portable paths via ${CLAUDE_PLUGIN_ROOT}, tokens via ${VAR} expansion documented in the README, secure transports only, and narrow tool pre-allowance in command frontmatter.

**Retained seed evidence.** All scored rows with their tier labels and failure-prevention targets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| pattern_identifier_stable_key | pattern_score_numeric_value | pattern_tier_adoption_level | pattern_failure_prevention_target |
| --- | ---: | --- | --- |
| `plugin_mcp_integration_patterns` | 95 | default_adoption_pattern_tier | Source Map First: Load local plugin mcp material before synthesizing integration patterns recommendations. |
| `plugin_mcp_integration_patterns` | 91 | default_adoption_pattern_tier | Evidence Boundary Split: Separate local facts, external facts, and inference before giving agent instructions. |
| `plugin_mcp_integration_patterns` | 88 | default_adoption_pattern_tier | Verification Gate Coupling: Attach each recommendation to at least one command, checklist, or review gate. |

## Idiomatic Thesis Synthesis Statement

**Decision supported.** This section helps decide what single claim should orient a builder integrating an external service. The seed thesis repeats the load-local-first formula instead of the corpus's claim, that external capability should enter a plugin as a bundled MCP server whose transport matches its hosting and whose credentials never live in the configuration.

**Recommended default and causal basis.** Phrase the thesis as stdio-local, SSE-hosted, secrets-external, tools-narrow, with the three evidence labels kept on its clauses. The skill's closing workflow prescribes choosing the type first, using ${CLAUDE_PLUGIN_ROOT} for all references, documenting environment variables, and letting OAuth or env-var expansion carry every secret.

**Operating conditions and assumptions.** The labels stay attached so skill-derived clauses remain distinguishable from reference-file-derived ones. The thesis orients use of this reference and does not compress the per-transport rules it stands on.

**Failure boundary and alternatives.** A thesis built on configuration mechanics alone would bless a working integration that leaks its token the first time the plugin is pushed to git. Bounded alternatives and recoveries: a latency-first thesis that favors stdio everywhere, or a zero-trust thesis that wraps every service in an mTLS stdio proxy.

**Counterexample, gotchas, and operational comparison.** OAuth tokens are stored by Claude Code and are not accessible to plugins, so a thesis assuming plugins can read their own tokens is wrong by design. Good: a reader who moves a hardcoded token into ${API_TOKEN} and documents it. Bad: one who deploys a local-only file tool as a hosted SSE service. Borderline: HTTP with a headers helper for short-lived JWTs, endorsed by authentication.md.

**Verification, evidence, and uncertainty.** Check the thesis names transport matching, secret custody, and tool narrowing in one statement. The implementation workflow and security sections of SKILL.md state each thesis clause. The corpus asserts but never benchmarks the latency ordering that makes stdio lowest.

**Second-order consequence.** The thesis is a separation of custody, the plugin owns configuration shape, the user's shell owns secrets, and Claude Code owns OAuth tokens, so no party ever holds all three.

**Revision decision.** Restate the combined inference as bundle the server with the plugin, match transport to hosting, keep secrets in the environment, and expose the fewest prefixed tools each command needs.

**Retained seed evidence.** The three labeled thesis clauses remain preserved beneath the evolved statement. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`local_corpus_sourced_fact`: The local row for `plugin_mcp_integration_patterns` contains 8 source path(s), which should be treated as the first retrieval surface for this theme.
`external_research_sourced_fact`: The external source map provides public documentation, repository, or ecosystem analogues where available.
`combined_evidence_inference_note`: Reliable use of Plugin Mcp Integration Patterns comes from loading the local corpus first, checking public ecosystem guidance second, and converting both into verification-backed agent decisions.

## Local Corpus Source Map

**Decision supported.** This section helps decide which mapped file to open first for a given integration question. The seed map lists headings without the reading order that makes the corpus usable, skill first for the pipeline, server-types second for transport choice, authentication third for credentials, tool-usage last for consumption.

**Recommended default and causal basis.** Route configuration questions to SKILL.md, transport tradeoffs to server-types.md, credential questions to authentication.md, and naming or allowlist questions to tool-usage.md. The skill's additional-resources section prescribes exactly that division, server-types as the deep dive, authentication for patterns and OAuth, tool-usage for commands and agents.

**Operating conditions and assumptions.** The reader's task is MCP integration, other plugin surfaces have their own skill files outside this map. The map orders this theme's four texts and does not catalog the wider plugin-dev skill tree they sit in.

**Failure boundary and alternatives.** A reader starting in tool-usage meets prefixed names and allowlists before learning which server produces them or how it authenticates. Bounded alternatives and recoveries: task-first routing that opens the troubleshooting sections directly, or a single merged document trading modularity for one read.

**Counterexample, gotchas, and operational comparison.** The skill references stdio-server.json, sse-server.json, and http-server.json examples that are not among the mapped paths, so their contents stay unverified here. Good: opening server-types.md to weigh HTTP against WebSocket for streaming. Bad: debugging a 401 from the skill's overview instead of authentication.md's troubleshooting table. Borderline: starting in tool-usage when the server is already configured and connected.

**Verification, evidence, and uncertainty.** Confirm the map's usage-role column matches each file's self-description. The additional-resources section of SKILL.md assigns each reference file its role. Whether the cited examples directory exists in this archive was not checked during this evolution.

**Second-order consequence.** The four files mirror the four failure sites of an integration, wrong bundling, wrong transport, failed auth, and missing tools, so the file to open is the file matching where the integration broke.

**Revision decision.** Annotate each row with its pipeline position, configure, transport, authenticate, consume, and note the examples/ configs the skill cites as untracked here.

**Retained seed evidence.** All local source rows with their heading-signal and usage-role columns remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| local_source_filepath_value | local_source_title_text | local_source_heading_signals | local_source_usage_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/mcp-integration/SKILL.md | mcp-integration | MCP Integration for Claude Code Plugins; Overview; MCP Server Configuration Methods; Method 1: Dedicated .mcp.json (Recommended); Method 2: Inline in plugin.json; MCP Server Types | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/mcp-integration/references/authentication.md | MCP Authentication Patterns | MCP Authentication Patterns; Overview; OAuth (Automatic); How It Works; Configuration; Supported Services | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/mcp-integration/references/server-types.md | MCP Server Types: Deep Dive | MCP Server Types: Deep Dive; stdio (Standard Input/Output); Overview; Configuration; Process Lifecycle; Use Cases | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/mcp-integration/references/tool-usage.md | Using MCP Tools in Commands and Agents | Using MCP Tools in Commands and Agents; Overview; Tool Naming Convention; Format; Examples; Discovering Tool Names | reference detail file for deeper pattern evidence |
| claude-skills/plugins/plugin-dev/mcp-integration/SKILL.md | mcp-integration | MCP Integration for Claude Code Plugins; Overview; MCP Server Configuration Methods; Method 1: Dedicated .mcp.json (Recommended); Method 2: Inline in plugin.json; MCP Server Types | skill entrypoint or reusable agent prompt |
| claude-skills/plugins/plugin-dev/mcp-integration/references/authentication.md | MCP Authentication Patterns | MCP Authentication Patterns; Overview; OAuth (Automatic); How It Works; Configuration; Supported Services | reference detail file for deeper pattern evidence |
| claude-skills/plugins/plugin-dev/mcp-integration/references/server-types.md | MCP Server Types: Deep Dive | MCP Server Types: Deep Dive; stdio (Standard Input/Output); Overview; Configuration; Process Lifecycle; Use Cases | reference detail file for deeper pattern evidence |
| claude-skills/plugins/plugin-dev/mcp-integration/references/tool-usage.md | Using MCP Tools in Commands and Agents | Using MCP Tools in Commands and Agents; Overview; Tool Naming Convention; Format; Examples; Discovering Tool Names | reference detail file for deeper pattern evidence |

## External Research Source Map

**Decision supported.** This section helps decide which external sources deserve retrieval when this reference is refreshed. The seed map lists the MCP resources spec, the community servers index, and the GitHub MCP server, each twice, while the corpus's own anchors, modelcontextprotocol.io and the Claude Code MCP docs, appear only inside SKILL.md.

**Recommended default and causal basis.** Treat archive claims about transports, OAuth handling, and prefixes as archive-local until the official Claude Code MCP documentation is retrieved. The skill names https://modelcontextprotocol.io/ and https://docs.claude.com/en/docs/claude-code/mcp as official docs, and none of the mapped or cited URLs was retrieved during this evolution.

**Operating conditions and assumptions.** External retrieval is available, offline sessions must label runtime-contract claims as unverified. The map governs external freshness checks for this theme and does not vouch for any URL's current content.

**Failure boundary and alternatives.** A refresh cycle following the seed map would poll a dated resources spec page while transport options, auth flows, and the tool-prefix format drift unwatched. Bounded alternatives and recoveries: drop the duplicated rows, or keep them with an explicit dedup note and a spec-version column.

**Counterexample, gotchas, and operational comparison.** Server-types.md presents mcp.github.com/sse as an SSE example while the seed maps github/github-mcp-server as a repository, and neither was checked live. Good: a refresh that fetches the Claude Code MCP docs and diffs the transport table. Bad: one that validates the resources spec and calls this file current. Borderline: fetching the community servers index to sample real configurations.

**Verification, evidence, and uncertainty.** Confirm every external claim in this file carries an unretrieved-candidate label. The additional-resources section of SKILL.md names the two official documentation anchors. Whether the pinned 2025-06-18 spec revision is still current is unknowable from the archive.

**Second-order consequence.** MCP is a versioned protocol, the seed URL pins spec 2025-06-18, so even a successful retrieval must record which protocol revision it validated against or the freshness check itself goes stale.

**Revision decision.** Flag all listed URLs as unretrieved candidates, deduplicate the doubled rows, and record the Claude Code MCP docs as the missing primary anchor for future refresh.

**Retained seed evidence.** All external source rows with their name, role, and boundary-label columns remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| external_source_url_value | external_source_name_text | external_source_usage_role | evidence_boundary_label_value |
| --- | --- | --- | --- |
| https://modelcontextprotocol.io/specification/2025-06-18/server/resources | Model Context Protocol resources | primary MCP resource model for context sharing | external_research_sourced_fact |
| https://github.com/modelcontextprotocol/servers | MCP server implementations | reference and community server implementation index | external_research_sourced_fact |
| https://github.com/github/github-mcp-server | GitHub MCP server | GitHub-backed MCP server for repository and issue operations | external_research_sourced_fact |
| https://modelcontextprotocol.io/specification/2025-06-18/server/resources | Model Context Protocol resources | primary resource-sharing model | external_research_sourced_fact |
| https://github.com/modelcontextprotocol/servers | MCP server implementations | reference server implementation collection | external_research_sourced_fact |
| https://github.com/github/github-mcp-server | GitHub MCP server | GitHub platform MCP implementation | external_research_sourced_fact |

## Anti Pattern Registry Table

**Decision supported.** This section helps decide which failure shapes reviewers must reject in plugin MCP configurations. The seed registry lists generic synthesis failures while the corpus names concrete integration anti-patterns, hardcoded tokens, plain HTTP, wildcard allowlists, hardcoded absolute paths, and per-item queries where one filtered call would do.

**Recommended default and causal basis.** Screen every .mcp.json, command frontmatter, and workflow description against all five before install testing. The DONT lists of SKILL.md and authentication.md prohibit each directly, and the performance sections of the skill and tool-usage.md show the many-individual-queries shape as the pattern to avoid.

**Operating conditions and assumptions.** Detection signals stay text-level, literal tokens, http:// or ws:// schemes, trailing wildcards, absolute home paths, and per-ID loops. The registry catalogs integration-specific failure shapes and their replacements, not general prose defects.

**Failure boundary and alternatives.** An agent screening against only the seed's three generic rows would pass a plugin that commits Bearer sk-abc123 in its headers. Bounded alternatives and recoveries: enforce via a pre-publish lint script, or via marketplace review rather than author-side checks.

**Counterexample, gotchas, and operational comparison.** Environment-variable indirection can still leak if the README instructs users to paste tokens into committed .env files, authentication.md says gitignore them. Good: rejecting a config whose url is http://mcp.example.com/sse. Bad: approving a wildcard allowlist because the demo worked. Borderline: a dev-only localhost HTTP URL behind an ${API_URL} switch, shown in server-types.md's conditional configuration.

**Verification, evidence, and uncertainty.** Run the text-level checks on every configuration and frontmatter file in the plugin. The security best practices, DONT lists, and batching sections state each appended anti-pattern. Relative frequency of these failures in the wild is unmeasured in the corpus.

**Second-order consequence.** Four of the five are detectable by grep before any server runs, only the batching failure needs runtime observation, so the registry doubles as a static review checklist.

**Revision decision.** Append the five corpus anti-patterns with their safer defaults, ${VAR} tokens, HTTPS/WSS, named tool lists, ${CLAUDE_PLUGIN_ROOT} paths, and batched filtered queries.

**Retained seed evidence.** All registry rows with their cause, replacement, and detection columns remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| anti_pattern_failure_name | failure_cause_risk_reason | safer_default_replacement_pattern | detection_signal_review_method |
| --- | --- | --- | --- |
| context_free_summary_output | agent skips local corpus and produces generic advice | source_map_first_synthesis | verify every listed local path appears in the generated file |
| unsourced_recommendation_claims | guidance appears authoritative without source boundary | evidence_boundary_split_pattern | check for local, external, and inference labels |
| unverified_agent_instruction | recommendation cannot be checked by command or review gate | verification_gate_coupling | require concrete gate in generated reference |

## Verification Gate Command Set

**Decision supported.** This section helps decide which commands must pass before an integration change is trusted. The seed gate lists one repository verifier while the corpus prescribes an integration test loop, run /mcp to see servers and tools, run claude --debug for connection and auth logs, and walk a validation checklist before publishing.

**Recommended default and causal basis.** Run the full loop after any configuration change plus the required session restart. SKILL.md's testing section orders local testing as configure, install locally, verify with /mcp, test tool calls, then check claude --debug logs.

**Operating conditions and assumptions.** Gates run in a session where the plugin is installed locally under .claude-plugin/. The gates prove this reference and its integrations are checkable, they do not replace the external service's own test environment.

**Failure boundary and alternatives.** A plugin passing only the document verifier can still fail at first use because no gate ever confirmed the server connects or the tools appear. Bounded alternatives and recoveries: curl the health endpoint with the Bearer token as authentication.md shows, or script the checklist into CI.

**Counterexample, gotchas, and operational comparison.** Forgetting the restart between edit and /mcp makes the old configuration test as if the edit failed. Good: a change validated by restart, /mcp, one tool call, and a debug-log scan. Bad: shipping after the JSON parsed. Borderline: curl-only validation for an HTTP server when a live session is unavailable.

**Verification, evidence, and uncertainty.** Record command outputs, server list, tool list, and auth status alongside the change. The testing, debugging, and validation-checklist sections of SKILL.md prescribe each gate. Exact debug-log formats are archive-local and may differ in current Claude Code builds.

**Second-order consequence.** /mcp and claude --debug split observability the way the corpus splits failure, /mcp answers whether the integration reached steady state while debug answers why it did not.

**Revision decision.** Add the corpus loop, /mcp for server and tool visibility, claude --debug for connection attempts, discovery logs, auth flows, and tool errors, and the seven-item validation checklist.

**Retained seed evidence.** The seed verifier command and its gate note remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`verification_gate_command_set`: Run the repository verifier after editing this file.

```bash
python3 agents-used-monthly-archive/idiomatic-references-202606/tools/verify_reference_generation.py --stage final
```

## Agent Usage Decision Guide

**Decision supported.** This section helps decide whether a capability ships as a pre-allowed command tool or an autonomous agent workflow. The seed guide says when to open this reference but not the corpus's sharpest agent rule, commands must pre-allow each prefixed MCP tool in frontmatter while agents may use any tool autonomously without pre-approval.

**Recommended default and causal basis.** Expose single validated operations as commands with named tools and reserve agents for workflows that chain queries, analysis, and writes. Tool-usage.md states agents have broader tool access than commands, can use any tool Claude determines necessary, and need no pre-allowed lists, while commands enumerate tools or use a sparing wildcard.

**Operating conditions and assumptions.** Tool names are confirmed against /mcp output first, the prefix format is easy to guess wrong. The guide routes usage of this reference and the exposure decision between commands and agents, not agent architecture at large.

**Failure boundary and alternatives.** An author applying command rules to agents writes pointless allowlists, and one applying agent freedom to commands ships tools that silently cannot run. Bounded alternatives and recoveries: wildcard-scoped commands for genuine all-tools surfaces, or hybrid commands that gather input then hand off to an agent.

**Counterexample, gotchas, and operational comparison.** Tool names are case-sensitive and must match exactly, a one-character prefix error fails only at call time. Good: create-task as a command naming one tool, status-reporting as an agent chaining search and comment tools. Bad: an agent frontmatter stuffed with allowlists it does not need. Borderline: a CRUD command pre-allowing four sibling tools, shown in tool-usage's CRUD pattern.

**Verification, evidence, and uncertainty.** Check each command's frontmatter names exist in /mcp output and each agent documents its typical tools. The using-tools-in-commands and agent-tool-access sections of tool-usage.md state the fork. Whether agent tool access is further restricted by user-level permission settings is not covered in the mapped files.

**Second-order consequence.** The fork is a permission gradient, commands trade flexibility for reviewable least privilege while agents trade reviewability for autonomy, which is why tool-usage still asks agents to document their typical tools.

**Revision decision.** Add the exposure fork, wrap user-interactive validated calls in commands with named tools, give autonomous multi-step workflows to agents that document which tools they typically use.

**Retained seed evidence.** The four seed usage bullets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`agent_usage_decision_guide`: Use this reference when a task mentions this theme, one of the listed local source paths, or a nearby technology/workflow surface.

- Start with the local corpus source map.
- Prefer patterns with explicit verification gates.
- Treat external sources as freshness and ecosystem checks, not replacements for local repo conventions.
- Preserve the evidence boundary labels when reusing recommendations.

## User Journey Scenario

**Decision supported.** This section helps decide where in the integration pipeline the current task actually sits. The seed scenario names a platform builder without the corpus's concrete journey, choose a configuration method, pick a transport, wire authentication, restart, verify with /mcp, then expose tools to commands or agents.

**Recommended default and causal basis.** Enter at step one with the service's hosting model known, local process or hosted endpoint, since that decides the transport fork immediately. The skill's nine-step implementation workflow walks exactly that order, ending with error-case testing and README documentation.

**Operating conditions and assumptions.** The user can restart their session freely, environments that cannot restart cannot complete the journey. The scenario frames who opens this reference and where in the pipeline they stand, not the full plugin-development journey.

**Failure boundary and alternatives.** A journey that starts at tool exposure strands the user with allowlists referencing a server that never connected. Bounded alternatives and recoveries: start from a working example config in the skill's examples list, or clone an existing plugin's .mcp.json and adapt.

**Counterexample, gotchas, and operational comparison.** First OAuth use opens a browser consent flow, so the journey's verify step needs an interactive session, not a headless run. Good: a builder who names the transport before writing any JSON. Bad: one debugging tool names while /mcp shows no server. Borderline: adapting a working SSE example to HTTP, fine if the auth section is rewritten too.

**Verification, evidence, and uncertainty.** Confirm the recorded journey position matches what /mcp currently shows. The implementation-workflow section of SKILL.md defines the nine steps. Typical wall-clock time per step is not recorded anywhere in the corpus.

**Second-order consequence.** The journey has one irreversible fork, transport choice, everything else, auth headers, allowlists, even server names, can be edited and re-verified cheaply after a restart.

**Revision decision.** Recast the journey as the nine-step workflow with the restart and /mcp checkpoint as its pivot, before it configuration is text, after it tools are real.

**Retained seed evidence.** The role, starting state, decision, and trigger lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Role based opening scenario: The agent-tool platform builder is starting from a capability request that could become a command, hook, plugin, MCP server, or setting and needs a reference that turns source evidence into an executable next step.
Primary user starting state: The user has a `plugin_mcp_integration_patterns` task, one or more local source paths, and uncertainty about which pattern should drive implementation.
Decision being made: choosing the right extension surface and proving install, invocation, permissions, and recovery behavior.
Reference opening trigger: Open this file when the task mentions plugin mcp integration patterns, any mapped local source path, or an adjacent workflow with the same failure mode.

## Decision Tradeoff Guide

**Decision supported.** This section helps decide which transport an integration adopts and when to revisit that choice. The seed guide weighs adopt, adapt, avoid without the corpus's central tradeoff table, stdio versus SSE versus HTTP versus WebSocket across transport, state, auth, latency, and reconnection.

**Recommended default and causal basis.** Stdio when the plugin ships the server, SSE when a vendor hosts it, HTTP when wrapping a REST API, WebSocket only when latency or push justifies persistent connections. Server-types.md closes with a comparison matrix and a choosing-the-right-type section that assigns each transport its use cases and costs.

**Operating conditions and assumptions.** The service actually offers the chosen endpoint, migration between types is a config rewrite plus redeployment as server-types shows. The guide covers transport and adoption tradeoffs for this theme, not service-side architecture.

**Failure boundary and alternatives.** Transport chosen by familiarity ships WebSocket complexity for a stateless REST backend or stdio for a service that needs OAuth. Bounded alternatives and recoveries: multi-server plugins mixing types per service, shown in both the skill and server-types advanced configuration.

**Counterexample, gotchas, and operational comparison.** Stdio processes live for the whole session and die with it, so long-running background state beyond the session needs a hosted transport. Good: SQLite via stdio next to a hosted Asana SSE server in one plugin. Bad: WebSocket for a nightly batch report. Borderline: HTTP now with a planned WebSocket migration when real-time lands, the documented migration path.

**Verification, evidence, and uncertainty.** Answer the two matrix questions in writing before accepting a transport choice. The comparison matrix and choosing sections of server-types.md state every fork. The matrix's latency orderings are qualitative labels, no measurements exist in the corpus.

**Second-order consequence.** The matrix is really two questions, where does the process run and who holds the connection state, answer both and the transport falls out without reading the marketing names.

**Revision decision.** Add the four-way fork, stdio for local lowest-latency stateful tools, SSE for hosted OAuth services with automatic reconnection, HTTP for stateless token-auth request-response, WebSocket for real-time bidirectional streaming.

**Retained seed evidence.** The adopt, adapt, avoid, and cost-of-being-wrong rows remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| decision_option_name | when_to_choose_condition | tradeoff_cost_description | verification_question_prompt |
| --- | --- | --- | --- |
| Adopt when | local corpus and external evidence agree on the plugin mcp integration patterns pattern | fastest path, but can copy stale local assumptions | Does the selected pattern appear in the canonical source and current external evidence? |
| Adapt when | local sources are strong but public ecosystem guidance has changed | preserves repo fit, but requires explicit inference notes | Did the reference label the local fact, external fact, and combined inference separately? |
| Avoid when | source evidence is thin, conflicting, or unrelated to the user journey | prevents false confidence, but may require deeper research | Is there a confidence warning or adjacent reference route? |
| Cost of being wrong | wrong plugin mcp integration patterns guidance can send an agent to the wrong files, tests, or abstraction | wasted implementation loop and weaker verification | Would a reviewer know what to undo and what to inspect next? |

## Local Corpus Hierarchy

**Decision supported.** This section helps decide which copy of each text a claim should cite and how much weight it carries. The seed hierarchy marks the archive skill canonical and everything else supporting without noting the live claude-skills copies are byte-identical duplicates, making the duplicate role, not supporting context, their accurate label.

**Recommended default and causal basis.** Cite archive paths in this reference, and re-run the identity diff whenever the live tree updates. Diff comparisons during this evolution showed each claude-skills file identical to its archive counterpart, and the seed's own vocabulary includes a duplicate role it never assigns.

**Operating conditions and assumptions.** Identity was checked during this evolution only, future syncs of claude-skills can silently break it. The hierarchy assigns evidential weight within this theme's eight rows, not across the repository.

**Failure boundary and alternatives.** A reviewer following the seed labels would treat the live SKILL.md as independent supporting context and cite it as corroboration. Bounded alternatives and recoveries: collapse the table to four rows with an alias column, or track divergence in the refresh queries of this file.

**Counterexample, gotchas, and operational comparison.** The doubled rows also double the heading signals, so a naive signal count overstates corpus breadth by two. Good: one citation per text with the pair identity noted. Bad: archive plus live citations presented as two sources. Borderline: citing the live copy directly when writing guidance for the live skill tree.

**Verification, evidence, and uncertainty.** Re-run diff on the four pairs and update roles if any pair diverges. Byte-identical diff results for all four pairs during this evolution. Which tree, archive or live, updates first when the skills are next revised is unknown.

**Second-order consequence.** The hierarchy inverts on drift, the moment a live copy diverges it stops being a duplicate and becomes the canonical row because it reflects current skill behavior.

**Revision decision.** Keep the archive skill canonical, keep its three reference files supporting, and relabel the four live copies as duplicates pending divergence.

**Retained seed evidence.** All hierarchy rows with their role, signal, and reviewer-question columns remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Classification vocabulary includes canonical, supporting, legacy, duplicate, and conflicting source roles.

| local_source_filepath_value | corpus_hierarchy_role | heading_signal_to_convert | reviewer_question_to_answer |
| --- | --- | --- | --- |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/mcp-integration/SKILL.md | canonical primary source | MCP Integration for Claude Code Plugins; Overview; MCP Server Configuration Methods | What guidance, warning, or example should this source contribute to Plugin Mcp Integration Patterns? |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/mcp-integration/references/authentication.md | supporting detail source | MCP Authentication Patterns; Overview; OAuth (Automatic) | What guidance, warning, or example should this source contribute to Plugin Mcp Integration Patterns? |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/mcp-integration/references/server-types.md | supporting detail source | MCP Server Types: Deep Dive; stdio (Standard Input/Output); Overview | What guidance, warning, or example should this source contribute to Plugin Mcp Integration Patterns? |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/mcp-integration/references/tool-usage.md | supporting detail source | Using MCP Tools in Commands and Agents; Overview; Tool Naming Convention | What guidance, warning, or example should this source contribute to Plugin Mcp Integration Patterns? |
| claude-skills/plugins/plugin-dev/mcp-integration/SKILL.md | supporting context source | MCP Integration for Claude Code Plugins; Overview; MCP Server Configuration Methods | What guidance, warning, or example should this source contribute to Plugin Mcp Integration Patterns? |
| claude-skills/plugins/plugin-dev/mcp-integration/references/authentication.md | supporting detail source | MCP Authentication Patterns; Overview; OAuth (Automatic) | What guidance, warning, or example should this source contribute to Plugin Mcp Integration Patterns? |
| claude-skills/plugins/plugin-dev/mcp-integration/references/server-types.md | supporting detail source | MCP Server Types: Deep Dive; stdio (Standard Input/Output); Overview | What guidance, warning, or example should this source contribute to Plugin Mcp Integration Patterns? |
| claude-skills/plugins/plugin-dev/mcp-integration/references/tool-usage.md | supporting detail source | Using MCP Tools in Commands and Agents; Overview; Tool Naming Convention | What guidance, warning, or example should this source contribute to Plugin Mcp Integration Patterns? |

## Theme Specific Artifact

**Decision supported.** This section helps decide what completed integration documentation must contain to be reviewable. The seed artifact names a resource/tool boundary map without the concrete columns the corpus supplies, server name, transport type, auth method, env vars required, tools exposed, and commands pre-allowing them.

**Recommended default and causal basis.** Fill the table from .mcp.json and command frontmatter before publishing, and regenerate it on every configuration change. Every corpus example carries exactly those fields, .mcp.json declares server and transport, authentication.md declares the credential route, tool-usage.md declares prefixed names and allowlists.

**Operating conditions and assumptions.** Tool names are taken from /mcp output, not guessed from the prefix formula. The artifact documents one plugin's integration surface for review and onboarding, not the external service's API.

**Failure boundary and alternatives.** A boundary map without the env-var column cannot answer the first setup question a new user asks, what must I export before this works. Bounded alternatives and recoveries: auto-generate the table by parsing .mcp.json and frontmatter, or fold it into the plugin README setup section.

**Counterexample, gotchas, and operational comparison.** OAuth rows have no env-var entry by design, writing token variables for OAuth servers signals a misunderstood auth flow. Good: a row reading asana, sse, oauth, none, three tool names, two commands. Bad: a map omitting which commands consume which tools. Borderline: a wildcard row documented as all server tools with justification.

**Verification, evidence, and uncertainty.** Cross-check each row against /mcp output and the README's environment-variable list. Configuration, authentication, and tool-usage examples across all four texts supply every column. No standard artifact format exists in the corpus, the columns are synthesized from its examples.

**Second-order consequence.** The artifact is the README the corpus keeps demanding, three separate files order authors to document required environment variables, and this table is that documentation in reviewable form.

**Revision decision.** Complete the artifact as a per-server table, name, transport, auth method, required environment variables, exposed tool names, and the commands or agents consuming each.

**Retained seed evidence.** The artifact-field table with completion rules and evidence hints remains preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Theme specific artifact: resource/tool boundary map with permission model and integration failure recovery.

| artifact_field_name | artifact_completion_rule | evidence_source_hint |
| --- | --- | --- |
| user_goal_statement | state the user's concrete goal before applying Plugin Mcp Integration Patterns | local corpus hierarchy plus critique findings |
| decision_boundary_rule | define the point where this reference should be used or avoided | decision tradeoff guide |
| verification_gate_rule | define the command, checklist, or review question that proves the artifact worked | verification gate command set |

## Worked Example Set

**Decision supported.** This section helps decide how to judge whether a proposed integration follows the pattern or violates it. The seed examples grade reference hygiene while the corpus supplies graded integration cases, the filesystem npx stdio server, the Asana OAuth SSE service, the Bearer-token HTTP backend, and the hardcoded-token config as the canonical bad case.

**Recommended default and causal basis.** Test candidate configurations against the graded set before writing new patterns. SKILL.md and server-types.md present each configuration verbatim, and authentication.md marks the literal sk-abc123 header with NEVER.

**Operating conditions and assumptions.** Cases stay verbatim from the corpus so calibration does not drift with paraphrase. The set calibrates review judgment for this theme, it does not replace the full pattern files.

**Failure boundary and alternatives.** Without concrete graded cases a reviewer cannot calibrate what passes, every judgment reduces to taste. Bounded alternatives and recoveries: grade against the validation checklist instead, or maintain a plugin-specific example set once real configs accumulate.

**Counterexample, gotchas, and operational comparison.** The good SSE example carries no auth block at all, absence of configuration is the correct OAuth shape, not an omission. Good: matching the npx stdio shape for a bundled server. Bad: copying the NEVER-marked token header because it ran. Borderline: the sparing wildcard, allowed by tool-usage only with genuine need.

**Verification, evidence, and uncertainty.** Trace each graded case to its verbatim source section before relying on it. Configuration examples in SKILL.md, server-types.md, authentication.md, and tool-usage.md supply every case. Whether the Asana SSE URL still works as shown is unverifiable from the archive.

**Second-order consequence.** The corpus's bad examples are all silent successes, the hardcoded token works, the HTTP URL works, the wildcard works, so grading must judge risk left behind, not whether the demo ran.

**Revision decision.** Replace the generic trio with corpus cases, good npx filesystem stdio and OAuth Asana SSE, bad hardcoded Bearer token over plain HTTP, borderline wildcard allowlist on an admin command.

**Retained seed evidence.** The good, bad, and borderline seed lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Good example: Use Plugin Mcp Integration Patterns after loading the canonical source, confirming the external evidence boundary, and writing a verification gate before implementation.
Bad example: Use Plugin Mcp Integration Patterns as a generic tutorial while ignoring the mapped local paths, source hierarchy, and cost of being wrong.
Borderline case: Use Plugin Mcp Integration Patterns only after adding a confidence warning when local evidence is thin or conflicts with current ecosystem guidance.

## Outcome Metrics and Feedback Loops

**Decision supported.** This section helps decide which signals prove an integration is healthy and which demand immediate debugging. The seed metrics name install-and-invoke success without the corpus's observable loop, servers visible in /mcp, tool calls succeeding from commands, auth completing without loops, and error cases handled gracefully.

**Recommended default and causal basis.** Walk the checklist at publish time and after any transport, auth, or tool change. The validation checklist enumerates exactly those checks and the troubleshooting sections define their failure signatures, server not connecting, tools not available, authentication failing.

**Operating conditions and assumptions.** A local install and interactive session are available for the OAuth and /mcp checks. The metrics track integration health for plugins using this reference, not external service uptime.

**Failure boundary and alternatives.** Without named signals an integration degrades silently, users see generic tool errors while the plugin author sees nothing. Bounded alternatives and recoveries: scripted health probes via curl for HTTP servers, or marketplace telemetry once distribution matters.

**Counterexample, gotchas, and operational comparison.** 429 rate-limit failures look like flakiness, tool-usage prescribes retry with a three-attempt cap before informing the user. Good: a release note recording checklist results. Bad: shipping on parsed JSON alone. Borderline: skipping the OAuth check in a headless CI run, acceptable only with a documented manual follow-up.

**Verification, evidence, and uncertainty.** Keep checklist outcomes with the plugin version so regressions are attributable. The validation checklist and troubleshooting sections across SKILL.md and the reference files define every signal. No numeric thresholds exist in the corpus, the loop is binary pass or investigate.

**Second-order consequence.** The corpus's error-message guidance doubles as a metric, if users report errors in the good three-line remediation form the UX layer works, raw 403 reports mean the error handling never shipped.

**Revision decision.** Adopt the checklist as the leading indicators and the three troubleshooting signatures as the failure signals, each with its debug route.

**Retained seed evidence.** The leading indicator, failure signal, and review cadence lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Leading indicator: users can install, invoke, debug, and remove the extension without reading implementation code.
Failure signal: the reference confuses adjacent extension types or omits failure recovery.
Review cadence: Re-run the verifier after every generated-reference edit and refresh external sources when public APIs, docs, or tooling releases change.

## Completeness Checklist

**Decision supported.** This section helps decide when an integration configuration or this reference may be called done. The seed checklist audits document shape without the corpus's configuration completeness bar, type-specific fields present, auth configured, env vars documented, secure schemes used, and portable paths throughout.

**Recommended default and causal basis.** Run both halves, text checks then human review, before marking an integration or this reference complete. The skill's configuration checklist enumerates those six items as the bar a finished configuration must clear.

**Operating conditions and assumptions.** The checklist tracks the archive's contract, live docs may add fields the archive does not know. The checklist gates this reference's completeness and the completeness of configurations built from it.

**Failure boundary and alternatives.** A document-complete reference can still bless configurations missing the README env-var documentation three corpus files demand. Bounded alternatives and recoveries: encode the machine-checkable half as a lint script, or adopt the marketplace's review checklist if one exists.

**Counterexample, gotchas, and operational comparison.** A stdio entry needs command while remote types need url, checking for one universal field passes broken configs. Good: a config failing review for an undocumented DB_URL. Bad: calling done at valid JSON. Borderline: passing a dev config with localhost HTTP behind an env switch, documented as dev-only.

**Verification, evidence, and uncertainty.** Record which checklist items were machine-checked and which were human-reviewed. The configuration checklist in SKILL.md's quick reference states all six items. Whether current Claude Code validates any of these fields at load time is not stated in the archive.

**Second-order consequence.** The six items split evenly, three are machine-checkable from the JSON while three, auth correctness, documentation, and portability intent, need a human reviewer, so the checklist assigns work to both.

**Revision decision.** Append the configuration bar, server type specified, command or url complete, authentication configured, environment variables documented, HTTPS/WSS only, ${CLAUDE_PLUGIN_ROOT} for paths.

**Retained seed evidence.** All seven seed checklist bullets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- The role scenario names the user, starting state, decision, and trigger for Plugin Mcp Integration Patterns.
- The decision guide includes Adopt when, Adapt when, Avoid when, and Cost of being wrong.
- The local corpus hierarchy identifies canonical and supporting sources or gives a confidence warning.
- The theme specific artifact is concrete enough to review without reading every mapped source.
- The examples cover good, bad, and borderline usage.
- The metrics section names one leading indicator and one failure signal.
- The adjacent routing section points to a better reference when this one is not the right fit.

## Adjacent Reference Routing

**Decision supported.** This section helps decide which reference should answer the current question when it leaves integration scope. The seed routing names plugin, mcp, and integration neighbors without the corpus's own boundary, commands and agents that consume MCP tools have their own skill surfaces, and hooks are a separate event-time system entirely.

**Recommended default and causal basis.** Stay here while the question involves .mcp.json, transports, credentials, or tool discovery, and route on everything else. Tool-usage.md constantly hands off to command frontmatter and agent definitions it does not own, and the plugin-dev tree keeps hook development in a sibling skill.

**Operating conditions and assumptions.** Adjacent references exist in this corpus generation, the hook reference was evolved immediately before this one. The routing bounds this reference to server bundling, transport, auth, and tool exposure.

**Failure boundary and alternatives.** A reader debugging a command's allowlist inside this reference misses that the failure lives in command definition, one skill over. Bounded alternatives and recoveries: a merged plugin mega-reference, rejected because the corpus itself splits these skills.

**Counterexample, gotchas, and operational comparison.** MCP tool monitoring via hooks, shown in the hook corpus's patterns file, genuinely spans both references and needs them read together. Good: routing a frontmatter syntax question to the command skill. Bad: explaining hook exit codes here. Borderline: a PreToolUse hook that audits MCP tool calls, legitimately spanning both.

**Verification, evidence, and uncertainty.** Check the question names a routing key before answering it in this file. The plugin-dev tree's skill boundaries and tool-usage's handoffs define the borders. The exact set of sibling references in future corpus generations may differ.

**Second-order consequence.** The tool prefix is the routing key, questions about producing mcp__plugin names belong here, questions about who may call them belong to the command and agent surfaces.

**Revision decision.** Route command-definition questions to the command skill, agent-behavior questions to agent references, event-time guardrails to the hook reference, and protocol-level questions to the MCP spec anchors.

**Retained seed evidence.** The three seed adjacent-reference lines and their guidance remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Adjacent reference guidance: Use command, hook, MCP, settings, or manifest references when one extension surface is already selected.
Adjacent reference 1: consider the plugin adjacent reference when the current task pivots away from plugin mcp integration patterns.
Adjacent reference 2: consider the mcp adjacent reference when the current task pivots away from plugin mcp integration patterns.
Adjacent reference 3: consider the integration adjacent reference when the current task pivots away from plugin mcp integration patterns.

## Workload Model

**Decision supported.** This section helps decide how much integration surface one plugin should carry before splitting. The seed model bounds source counts without the corpus's operational load shape, one plugin may run multiple servers of mixed types, each contributing ten-plus tools that commands and agents fan out across.

**Recommended default and causal basis.** Bound each plugin to the services one workflow needs, and batch filtered queries instead of per-item calls as both performance sections instruct. The skill's key capabilities promise ten-plus related tools per service and both the skill and server-types show multi-server plugins mixing stdio, SSE, and HTTP.

**Operating conditions and assumptions.** Connection pooling and lazy loading behave as the archive describes, both are archive-local claims. The model sizes integration work per plugin, not external service capacity.

**Failure boundary and alternatives.** A model assuming one server and a handful of tools underestimates allowlist sprawl and debug surface the moment a second service joins. Bounded alternatives and recoveries: split heavy multi-service workflows across plugins, or push aggregation into the MCP server itself.

**Counterexample, gotchas, and operational comparison.** Parallel tool calls are encouraged for independent operations, but per-item loops over large lists remain the documented anti-shape regardless of parallelism. Good: one plugin, three servers, each feeding a distinct command set. Bad: a loop of fifty get_task calls where one filtered search was available. Borderline: a wildcard agent workflow spanning all servers, acceptable with documented tool usage.

**Verification, evidence, and uncertainty.** Count servers, tools, and consuming surfaces per plugin and compare against the one-workflow bound. The capabilities, multi-server, lazy-loading, and batching sections state the load shape. No numeric tool or server limits exist anywhere in the corpus.

**Second-order consequence.** Lazy loading shifts cost from startup to first call, so perceived tool latency includes connection setup exactly once, a spike the corpus says is managed automatically but authors should expect.

**Revision decision.** Model workload as servers times transports times tools, with lazy connection on first use and batching as the pressure valves the corpus provides.

**Retained seed evidence.** The workload dimension table with its boundary and pressure columns remains preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`combined_evidence_inference_note`: Treat Plugin Mcp Integration Patterns as a agent workflow operating reference, not as a prose summary.

| workload_dimension_name | workload_boundary_value | verification_pressure_point |
| --- | --- | --- |
| primary_usage_surface | agent planning, tool use, context loading, delegation, or skill/plugin execution where bad guidance compounds across long-running sessions | verify that the reference changes the next implementation or review action |
| bounded_capacity_model | one primary task, up to 10 source files, up to 3 delegated subtasks, and a written completion audit for every run | split the task or create a narrower reference when this boundary is exceeded |
| source_pressure_model | local heading signals include MCP Integration for Claude Code Plugins; Overview; MCP Server Configuration Methods; Method 1: Dedicated .mcp.json (Recommended); Method 2: Inline in  | compare guidance against canonical local sources before following external examples |
| artifact_pressure_model | required artifact is resource/tool boundary map with permission model and integration failure recovery | require the artifact before claiming the reference is operationally usable |

## Reliability Target

**Decision supported.** This section helps decide which reliability responsibilities the plugin author owns versus inherits. The seed targets track evidence hygiene without the corpus's reliability posture, automatic reconnection for SSE and WebSocket, retry with a bounded cap for tool calls, and graceful degradation with user-facing remediation.

**Recommended default and causal basis.** Rely on transport reconnection, implement the three-attempt retry only for retryable errors, and template the error messages on the corpus's checklist form. Server-types assigns automatic reconnection to SSE and WebSocket and process respawn to stdio, and tool-usage's error pattern caps retries at three attempts before informing the user.

**Operating conditions and assumptions.** Error types are classified first, auth failures must not be retried like rate limits. Targets cover the plugin-side integration path, the external service's own SLA is out of scope.

**Failure boundary and alternatives.** An integration without the bounded retry turns a transient 429 into either an infinite loop or an immediate user-facing failure. Bounded alternatives and recoveries: circuit breakers above the retry cap, or health probes before workflows that chain many calls.

**Counterexample, gotchas, and operational comparison.** Stdio has no reconnection, only process respawn, so a crashing local server needs its own crash-handling per server-types best practices. Good: a 429 retried twice then reported with quota guidance. Bad: retrying a 401 three times before surfacing it. Borderline: buffering WebSocket messages during disconnection, prescribed but unspecified in size.

**Verification, evidence, and uncertainty.** Test the missing-auth, invalid-parameter, and nonexistent-resource cases the testing section lists. Reconnection rows in the comparison matrix and the retry pattern in tool-usage state each target. Reconnection backoff timing is undocumented in the archive.

**Second-order consequence.** The corpus's reliability chain has three layers with distinct owners, transport reconnection belongs to Claude Code, retry policy to the command author, and remediation text to the UX, so a gap analysis checks each owner separately.

**Revision decision.** Set targets as reconnection handled by transport, tool retries capped at three, every failure path ending in a remediation message naming what the user should check.

**Retained seed evidence.** All reliability target rows with thresholds and collection methods remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| reliability_target_name | measurable_threshold_value | evidence_collection_method |
| --- | --- | --- |
| source_boundary_preservation | 100 percent of recommendations keep local, external, and inference boundaries visible | review generated text for the three evidence labels before reuse |
| decision_accuracy_sample | at least 18 of 20 sampled uses route to the correct adopt, adapt, avoid, or adjacent-reference decision | sample downstream tasks and record reviewer verdicts |
| unsupported_claim_rate | zero unsupported production, security, latency, or reliability claims in final guidance | reject claims without source row, explicit inference note, or verification method |
| recovery_path_clarity | every avoid or failure case names the rollback, escalation, or next-reference route | inspect failure-mode and adjacent-routing sections together |

## Failure Mode Table

**Decision supported.** This section helps decide which failure signature matches the observed symptom and which check sequence follows. The seed table lists synthesis failures without the corpus's three diagnosed integration failures, server not connecting, tools not available, and authentication failing, each with its documented check sequence.

**Recommended default and causal basis.** Diagnose in lifecycle order with claude --debug open, and check the restart-after-config-change gotcha before anything else. SKILL.md's common-issues section defines all three signatures and their checks, URL and process for connection, /mcp and exact names for tools, cached tokens and scopes for auth.

**Operating conditions and assumptions.** Debug logging is available, without it only /mcp visibility and tool errors remain observable. The table catalogs plugin-side integration failures, service-side outages appear only as their connection symptoms.

**Failure boundary and alternatives.** An operator without the signatures debugs by restart superstition instead of walking the documented checks. Bounded alternatives and recoveries: curl-based endpoint checks for remote transports, or stderr log inspection for stdio servers that log correctly.

**Counterexample, gotchas, and operational comparison.** Tools not available often means the config edit never loaded because the session was not restarted, the corpus repeats this fix in two files. Good: a 403 traced to workspace permissions via the auth checks. Bad: reinstalling the plugin for a stale-session tool miss. Borderline: a stray print corrupting stdio JSON-RPC, diagnosed only through the protocol-communication checks.

**Verification, evidence, and uncertainty.** Confirm each incident record names the signature, the failing lifecycle stage, and the check that found it. The common-issues, troubleshooting, and HTTP-error sections state every signature and check. Relative frequency of the three signatures in production plugins is unmeasured.

**Second-order consequence.** The three signatures are ordered by lifecycle stage, connection before discovery before auth-at-use, so the fastest diagnosis walks them in lifecycle order and stops at the first failing stage.

**Revision decision.** Append the three signatures with their triggers and mitigations, plus the 401, 403, 429, 500 HTTP ladder from server-types troubleshooting.

**Retained seed evidence.** All failure mode rows with trigger and mitigation columns remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| failure_mode_name | likely_trigger_condition | required_mitigation_action |
| --- | --- | --- |
| source drift hides truth | external or local guidance changes after the reference was written | refresh public evidence, rerun local corpus gate, and mark stale claims before reuse |
| generic advice escapes review | agent copies plausible best practices without theme-specific verification | block completion until the verification gate names concrete command, reviewer question, or metric |
| context window loses plan | long-running session forgets early constraints or overwrites user intent | write checkpoint summaries and re-read plan before each destructive step |
| tool fanout outruns budget | parallel actions create conflicts, duplicate work, or unbounded external calls | cap fanout, assign ownership, and require merge/audit checkpoints |

## Retry Backpressure Guidance

**Decision supported.** This section helps decide when a failed tool call is retried, slowed, or surfaced. The seed guidance classifies verification failures without the corpus's call-level policy, classify the error first, retry transient failures at most three times, respect rate limits, and batch to avoid provoking them.

**Recommended default and causal basis.** Batch first, retry transient failures up to three times with waits, and surface everything else with remediation text. Tool-usage's error-handling pattern waits and retries with a three-attempt maximum, its 429 row demands rate-limit handling, and both performance sections prescribe batching as the load reducer.

**Operating conditions and assumptions.** Error responses distinguish transient from permanent causes, opaque errors must be treated as permanent after one retry. The guidance governs plugin-side tool calls, server-side throttling policy belongs to the service.

**Failure boundary and alternatives.** Unclassified retries hammer a rate-limited service harder, converting a soft 429 into sustained throttling. Bounded alternatives and recoveries: exponential backoff beyond the flat wait, or queueing writes through the MCP server when it offers bulk endpoints.

**Counterexample, gotchas, and operational comparison.** Partial batch success needs its own report shape, the corpus's eight-of-ten summary with named failures, not a blanket retry of the whole batch. Good: a timeout retried twice then reported. Bad: retrying a 400 validation error three times unchanged. Borderline: retrying a 500 once before escalating, reasonable though the corpus only says check server logs.

**Verification, evidence, and uncertainty.** Review workflows for the cap, the classification step, and the partial-success report shape. The error-handling pattern, HTTP ladder, and batching sections state the policy. Wait durations between retries are unspecified in the archive.

**Second-order consequence.** Batching is preemptive backpressure, the corpus's single-filtered-query rule removes the call volume that makes retry policy matter in the first place.

**Revision decision.** Adopt classify-then-retry with the three-attempt cap, treat 429 as a signal to slow and batch, and treat auth and validation errors as non-retryable.

**Retained seed evidence.** All seed retry bullets and their classification framing remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- Retry only after the failed verification signal is classified as transient, stale evidence, missing context, or true contradiction.
- Use one bounded retry for stale external evidence refresh, then escalate to a human or a narrower source-specific reference.
- Apply backpressure by stopping new generation or implementation work when source coverage, critique coverage, or verification gates are red.
- For long-running agent workflows, checkpoint after each batch and re-read the current spec before any broad rewrite, commit, push, or destructive operation.
- For distributed execution, assign one owner per generated file or theme batch and require merge-time verification of exact path, heading, and evidence-boundary invariants.

## Observability Checklist

**Decision supported.** This section helps decide which surface answers the current question about integration behavior. The seed checklist audits document reviews without the corpus's observability surfaces, /mcp for server and tool inventory, claude --debug for connection, discovery, auth, and call errors, and stderr-only logging for stdio servers.

**Recommended default and causal basis.** Check /mcp after every restart, keep debug logs during integration work, and validate stderr discipline in custom stdio servers. The debugging sections direct authors to debug logs for four named signal classes, and server-types insists stdio servers log to stderr because stdout carries the protocol.

**Operating conditions and assumptions.** Debug mode is enabled deliberately, normal sessions do not record the flows. The checklist covers plugin-side observability, service-side dashboards are out of scope.

**Failure boundary and alternatives.** A stdio server that logs to stdout corrupts its own JSON-RPC channel, the observability mistake that breaks the thing observed. Bounded alternatives and recoveries: wrapping tool calls in audit logging, a technique the adjacent hook corpus documents for MCP monitoring.

**Counterexample, gotchas, and operational comparison.** User-facing progress feedback, searching then found-fifteen updates, is part of observability per tool-usage, silence during long operations reads as a hang. Good: a bug report with /mcp output and a sanitized debug excerpt. Bad: a custom server printing status lines to stdout. Borderline: temporary verbose LOG_LEVEL env in production debugging, shown in stdio examples.

**Verification, evidence, and uncertainty.** Confirm each debugging session records which surface was consulted and what it showed. The debugging sections of SKILL.md and the stdio best practices state every surface. Debug log retention and exact formats are archive-local details.

**Second-order consequence.** The corpus's sanitized-header note means debug logs are safe to share by design, which makes them the right artifact to attach to bug reports instead of raw configs that may embed secrets.

**Revision decision.** Adopt the three surfaces as the checklist, inventory via /mcp, flows via debug logs, server internals via stderr, each mapped to the failure stage it illuminates.

**Retained seed evidence.** All seed observability bullets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- Record which local sources were loaded and which were intentionally skipped.
- Record the exact verification command, reviewer question, or rendered artifact used as proof.
- Record p50/p95/p99 latency or reviewer-time measurements when the reference affects runtime or workflow speed.
- Capture tool-call count, context files loaded, delegated tasks, retry count, and completion-audit outcome.
- Record leading indicator and failure signal from this file in the coverage manifest or journal when the reference drives real work.
- Keep audit evidence small enough to review: command output summary, changed-file list, and unresolved-risk notes are preferred over raw transcript dumps.

## Performance Verification Method

**Decision supported.** This section helps decide whether a workflow's call pattern is efficient enough to ship. The seed method verifies document quality without the corpus's performance levers, batch filtered queries over per-item calls, cache expensive results for reuse, and parallelize independent tool calls.

**Recommended default and causal basis.** Review every multi-call workflow against the three levers before shipping, then confirm with debug-log call counts. Both performance sections show the same before-after query shape, and tool-usage adds caching and parallel calls as the remaining levers.

**Operating conditions and assumptions.** The service exposes filtered search endpoints, without them batching degrades to pagination. The method verifies plugin-side call efficiency, server-side query optimization is out of scope.

**Failure boundary and alternatives.** A workflow looping get_task over fifty IDs performs fifty round trips where one filtered search with a limit would do. Bounded alternatives and recoveries: push aggregation into a custom MCP server, or precompute reports on a schedule outside the session.

**Counterexample, gotchas, and operational comparison.** Caching trades staleness for speed, tool-usage says re-fetch when data changes, so cached workflows need an invalidation cue. Good: one search with project, status, and limit filters feeding all downstream steps. Bad: sequential get calls in a loop. Borderline: parallel calls to three unrelated getters, encouraged when truly independent.

**Verification, evidence, and uncertainty.** Count implied calls per user action in the workflow text and compare against the filtered-single-call baseline. The batching, caching, and parallel-call sections of SKILL.md and tool-usage.md state each lever. No latency numbers exist in the corpus to convert call counts into user-visible time.

**Second-order consequence.** All three levers are visible in the workflow text before execution, so performance review here is static analysis, count the calls the instructions imply per user action.

**Revision decision.** Verify by inspecting workflows for the three levers, filters with limits on searches, cached reuse of expensive results, and parallel calls only for independent operations.

**Retained seed evidence.** The seed verification method lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Performance method: require tool-call budgets, timeout budgets, and a resumable journal when the workflow exceeds one focused session.
Leading indicator to measure: users can install, invoke, debug, and remove the extension without reading implementation code.
Failure signal to watch: the reference confuses adjacent extension types or omits failure recovery.
Required measurement packet: capture input size, source count, tool-call count, wall-clock time, p50/p95/p99 latency where runtime applies, and reviewer decision time where documentation applies.
Pass condition: the reference must let a reviewer identify the correct next action, verification gate, and stop condition without reading unrelated files.
Fail condition: the reference encourages implementation before the workload, reliability target, and failure-mode table are explicit.

## Scale Boundary Statement

**Decision supported.** This section helps decide whether the requirement fits a transport's designed envelope or needs migration or wrapping. The seed statement bounds reference usage without the corpus's scale edges, stdio dies with the session, HTTP is stateless per request, WebSocket holds persistent connections, and mTLS enterprise auth needs a stdio wrapper workaround.

**Recommended default and causal basis.** Operate inside each transport's designed edge and reach for the stdio wrapper when configuration cannot express the requirement. Server-types assigns each transport its state model, and authentication.md states mTLS is not directly supported, prescribing the wrapper as the boundary-crossing device.

**Operating conditions and assumptions.** The wrapper inherits stdio's own session-bound lifecycle, an escape hatch, not a scale fix. The statement bounds plugin-side integration scale, service capacity planning is external.

**Failure boundary and alternatives.** Pushing session-lifetime stdio into always-on service duty or stateless HTTP into streaming duty fails at the transport's designed edge, not from bugs. Bounded alternatives and recoveries: hosting a custom SSE service for always-on needs, the documented stdio-to-SSE migration path.

**Counterexample, gotchas, and operational comparison.** Heartbeat, reconnection logic, and message buffering are the WebSocket author's duties per its best practices, not free transport features. Good: HMAC request signing via a headers helper script. Bad: expecting a stdio server to survive between sessions. Borderline: JWT generation in a headersHelper, documented but adding a moving part per call.

**Verification, evidence, and uncertainty.** Name the transport edge nearest each integration and the planned response when load reaches it. The state rows of the comparison matrix and the mTLS workaround state every edge. Connection-count or message-rate ceilings are absent from the archive.

**Second-order consequence.** The wrapper workaround generalizes, any capability the MCP configuration cannot express, mTLS, custom signing, exotic transports, moves into a stdio server the plugin ships, making stdio the escape hatch at every boundary.

**Revision decision.** State the edges per transport, session-bound stdio, stateless HTTP, connection-holding WebSocket with heartbeat and buffering duties, and wrapper-mediated enterprise auth.

**Retained seed evidence.** The seed scale boundary lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Plugin Mcp Integration Patterns stops being sufficient when the task spans multiple independent systems, more than one ownership boundary, unbounded source discovery, or production traffic without an explicit SLO.
Under distributed execution, split work by theme file and preserve one verification owner per split; do not let parallel agents rewrite the same reference without a merge checkpoint.
Under long-running agent workflows, treat context drift as a reliability failure: checkpoint state, summarize open risks, and verify against the spec before continuing.
Under large-codebase scale, require dependency or source-graph narrowing before applying this reference; a source list without ranked canonical guidance is not enough.

## Future Refresh Search Queries

**Decision supported.** This section helps decide which searches the next refresh cycle must run first. The seed queries target generic theme drift while the volatile surfaces here are the MCP spec revision beyond 2025-06-18, the Claude Code transport and tool-prefix contracts, and the OAuth-enabled hosted server roster.

**Recommended default and causal basis.** Run the transport, prefix, and roster queries against official docs before trusting any allowlist or URL example here. The seed pins a dated spec URL, the skill marks GitHub and Google OAuth servers as when available, and the prefix format is a runtime contract one release can change.

**Operating conditions and assumptions.** Retrieval is available, offline refreshes can only re-verify internal consistency. The queries steer the next refresh cycle, they do not validate today's claims.

**Failure boundary and alternatives.** A refresh checking only theme keywords would miss a renamed prefix format that silently breaks every documented allowlist example. Bounded alternatives and recoveries: subscribe to MCP spec release notes, or diff the live claude-skills tree as a cheap local proxy for drift.

**Counterexample, gotchas, and operational comparison.** The doubled seed URL rows mean naive query generation from the map produces duplicate searches. Good: checking whether mcp.github.com/sse now exists as server-types anticipates. Bad: re-searching generic plugin integration blogs. Borderline: sampling the community servers index for new transport idioms.

**Verification, evidence, and uncertainty.** Record each query, its date, and whether it confirmed or contradicted the archive claim. The when-available markers, dated spec pin, and prefix contract locate the volatility. Everything this section targets is by definition unverifiable until retrieved.

**Second-order consequence.** The when-available markers are the corpus telling us where it expects to be wrong first, so the hosted-server roster is the highest-yield refresh query in the file.

**Revision decision.** Target the refresh at the current MCP spec revision, the live Claude Code MCP docs for transports and prefixes, headersHelper support status, and which hosted OAuth servers now exist.

**Retained seed evidence.** All seed refresh query lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| search_query_label_name | search_query_text_value |
| --- | --- |
| `official_docs_query_phrase` | plugin mcp integration patterns official documentation best practices |
| `github_repository_query_phrase` | plugin mcp integration patterns GitHub repository examples |
| `release_notes_query_phrase` | plugin mcp integration patterns changelog release notes migration |

## Evidence Boundary Notes

**Decision supported.** This section helps decide which statements in this reference may be reused without fresh verification. The seed notes state the three-label discipline without this file's actual boundary inventory, four texts read in full, four byte-identical live duplicates, six external rows never retrieved, and runtime contracts held as archive-local.

**Recommended default and causal basis.** Carry the labels forward when quoting this file and re-verify runtime contracts against live docs before operational use. Every claim above traces to the skill or one of its three reference files, while transports, prefixes, OAuth behavior, and env-var expansion are runtime contracts only live docs can confirm.

**Operating conditions and assumptions.** The boundary holds until any live copy diverges or any external row is retrieved, either event forces a relabel. The notes bound what this evolved reference may assert, not what the corpus asserts elsewhere.

**Failure boundary and alternatives.** Without the inventory a reuser cannot tell the corroborated tool-naming claim from the never-retrieved spec citation sitting beside it. Bounded alternatives and recoveries: an inline per-claim citation format, rejected here to keep the seed structure intact.

**Counterexample, gotchas, and operational comparison.** The seed's external rows look load-bearing because they carry a dated spec version, yet nothing in this file's guidance rests on them. Good: reusing the tool-prefix format with its archive-local label attached. Bad: citing the resources spec row as verified fact. Borderline: reusing the Asana OAuth example, corroborated across three texts but unverified live.

**Verification, evidence, and uncertainty.** Spot-check quoted claims against the inventory labels before they leave this file. The reading log, diff results, and unretrieved URL list from this evolution constitute the inventory. Future corpus syncs may change which copies are canonical without notice.

**Second-order consequence.** The strongest evidence in this file is the negative result, the byte-identical diff, because it is the only claim verified by direct computation during this evolution rather than by reading.

**Revision decision.** Record the inventory, local facts from four texts, duplicates acknowledged, externals downgraded to unretrieved candidates, and runtime contracts labeled archive-local pending the official MCP docs.

**Retained seed evidence.** All seed evidence boundary lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- `local_corpus_sourced_fact`: statements tied directly to the local source paths above.
- `external_research_sourced_fact`: statements tied to the public URLs above.
- `combined_evidence_inference_note`: synthesis that combines local and public evidence into agent guidance.
