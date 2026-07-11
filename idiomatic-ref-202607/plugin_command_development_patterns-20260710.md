# Plugin Command Development Patterns

**Decision supported.** This section helps decide whether a requested capability should become a plugin slash command and, if so, how to design its prompt, arguments, tools, resources, interaction, tests, and release contract. The seed title does not yet define when a plugin slash command is the correct extension surface, how its instruction contract should be bounded, or which installation, permission, interaction, recovery, and distribution evidence must accompany it.

**Recommended default and causal basis.** Choose a focused command for an explicitly invoked, repeatable agent workflow; write directives to Claude, keep frontmatter minimal, grant least-required tools, use plugin-root paths, validate inputs, expose recovery, and test discovery through real invocation. A command turns user intent into model instructions at invocation time, so clarity and permission scope shape behavior while portable paths and layered tests determine whether the same workflow survives installation and edge cases.

**Operating conditions and assumptions.** The workflow has a clear manual trigger, bounded goal, inspectable inputs, predictable tool needs, useful user-facing help, and a result that can be verified without hidden automatic execution. Use this reference for Claude Code plugin slash-command design and validation, not as current authoritative documentation for every extension surface or product release.

**Failure boundary and alternatives.** The capability must run automatically on events, maintain specialized autonomous reasoning, expose an external service protocol, persist configuration independently, or execute high-risk operations without an explicit human gate. Bounded alternatives and recoveries: use a hook for event-driven enforcement, a skill for reusable knowledge, an agent for delegated autonomy, MCP for external tools or resources, settings for persistent policy, or a tested script behind a thin command when deterministic logic dominates.

**Counterexample, gotchas, and operational comparison.** Writing marketing copy instead of instructions, granting broad Bash access, hardcoding installation paths, confusing arguments with interactive choices, embedding complex program logic in Markdown, assuming discovery, and omitting cancel or cleanup behavior. Good: `/review-pr` accepts a known PR number, gathers bounded context, applies a review rubric, and reports evidence. Bad: a command silently deploys with unrestricted tools. Borderline: a guided setup command is valid only when its questions, confirmation, writes, and restart path are tested.

**Verification, evidence, and uncertainty.** Record surface-selection rationale, command path and namespace, parsed frontmatter, help discovery, argument matrix, permission-denial cases, plugin-root resource checks, interactive branches, script exits, recovery behavior, cross-install invocation, and removal. The eight fully read local artifacts directly cover command semantics, frontmatter, arguments, interaction, workflows, documentation, plugin integration, distribution, and seven testing levels. The corpus is archived and external MCP links were not refreshed, so product-specific syntax and availability must be checked against the installed Claude Code version before release.

**Second-order consequence.** A command is an interface contract around model behavior, not merely a saved prompt; distribution turns every implicit local assumption into a potential installation or safety defect.

**Revision decision.** Add a surface-selection matrix, instruction contract, least-privilege and portability rules, interaction boundaries, layered verification, recovery expectations, distribution gates, and explicit freshness caveats.

**Retained seed evidence.** The exact title plus sixteen local and three external source rows remain unchanged as the frozen evidence base. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

## Source Evidence Mapping Table

**Decision supported.** This section helps decide which source may support command syntax, workflow, interaction, distribution, testing, or extension-routing claims, and how duplicate paths should affect confidence. The seed records sixteen local command-development paths as separate rows even though they form eight byte-identical archive and live-path pairs, then adds three MCP links whose subject is adjacent integration rather than slash-command semantics.

**Recommended default and causal basis.** Treat the archived skill as the canonical command overview, its seven detail files as topic authorities, the matching live-path copies as duplicate retrieval locations rather than corroboration, and MCP links only as adjacent evidence for routing external integrations. Counting duplicate bytes as independent support inflates apparent evidence, while allowing MCP resources to prove command behavior confuses two extension contracts with different invocation and lifecycle semantics.

**Operating conditions and assumptions.** Each recommendation names a claim class, cites the exact local file and relevant heading, identifies duplicate lineage, labels synthesis, and uses external material only where its capability boundary is actually relevant. Apply this provenance model to the frozen nineteen rows and distinguish source evidence from later installed-product tests.

**Failure boundary and alternatives.** Sixteen rows are presented as sixteen independent confirmations, a marketplace example becomes current product truth, MCP documentation defines slash-command frontmatter, or an inference has no claim-level provenance. Bounded alternatives and recoveries: collapse duplicate paths into one lineage ledger, downgrade stale syntax to archived guidance, verify behavior in the installed product, omit irrelevant external analogies, or route external-service needs to an MCP-specific reference.

**Counterexample, gotchas, and operational comparison.** Source-count theater, archive and live copies drifting later, titles standing in for content, examples being mistaken for grammar, and broad external authority masking a mismatch in extension surface. Good: cite frontmatter-reference for archived field intent and test the installed parser. Bad: cite the MCP resource specification for `allowed-tools`. Borderline: use MCP links to explain why an external tool belongs outside the command while labeling that as routing inference.

**Verification, evidence, and uncertainty.** Hash paired local paths, build a claim-to-heading ledger, flag conflicts and unused rows, record installed-version observations separately, and reject every tool-specific claim whose only support is duplicate count or adjacent MCP evidence. All eight unique local files were read completely and each live path is byte-identical to its archived counterpart; the seed directly preserves all nineteen source rows. The three public links and current Claude Code behavior were not refreshed, so archive guidance remains evidence of the corpus rather than a freshness guarantee.

**Second-order consequence.** Duplicate detection changes both context and epistemics: it halves redundant reading while preventing copied files from masquerading as independent consensus.

**Revision decision.** Add duplicate-lineage handling, claim-specific authority, external adjacency limits, current-version verification rules, and a provenance ledger while retaining every original path and URL.

**Retained seed evidence.** All sixteen local rows and three external rows remain exactly preserved beneath the expanded mapping guidance. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| source_location_path_key | source_category_artifact_type | source_authority_confidence_level | source_usage_synthesis_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/command-development/SKILL.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/command-development/references/advanced-workflows.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/command-development/references/documentation-patterns.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/command-development/references/frontmatter-reference.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/command-development/references/interactive-commands.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/command-development/references/marketplace-considerations.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/command-development/references/plugin-features-reference.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/command-development/references/testing-strategies.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| claude-skills/plugins/plugin-dev/command-development/SKILL.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt |
| claude-skills/plugins/plugin-dev/command-development/references/advanced-workflows.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| claude-skills/plugins/plugin-dev/command-development/references/documentation-patterns.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| claude-skills/plugins/plugin-dev/command-development/references/frontmatter-reference.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| claude-skills/plugins/plugin-dev/command-development/references/interactive-commands.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| claude-skills/plugins/plugin-dev/command-development/references/marketplace-considerations.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| claude-skills/plugins/plugin-dev/command-development/references/plugin-features-reference.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| claude-skills/plugins/plugin-dev/command-development/references/testing-strategies.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| https://modelcontextprotocol.io/specification/2025-06-18/server/resources | external_research_source_material | external_research_sourced_fact | primary MCP resource model for context sharing |
| https://github.com/modelcontextprotocol/servers | external_research_source_material | external_research_sourced_fact | reference and community server implementation index |
| https://github.com/github/github-mcp-server | external_research_source_material | external_research_sourced_fact | GitHub-backed MCP server for repository and issue operations |

## Pattern Scoreboard Ranking Table

**Decision supported.** This section helps decide how to sequence these three safeguards during command development without treating their numeric values as calibrated confidence or measured effectiveness. The seed gives scores of 95, 91, and 88 to local-first retrieval, evidence separation, and verification coupling without a scale, sample, or command-specific outcome measure.

**Recommended default and causal basis.** Use source mapping to establish the relevant command contract, evidence labels to separate archived facts from current tests and inference, and verification coupling to exercise discovery, permissions, branches, failures, and cleanup; require all three. A test against the wrong or assumed contract can pass locally yet fail after installation, while good provenance without invocation evidence leaves command behavior speculative.

**Operating conditions and assumptions.** The ranking orders attention, each row becomes an observable gate, reviewers may reorder gates for an active failure, and completion still requires every safeguard. Retain 95, 91, and 88 as frozen editorial metadata, not probabilities, service objectives, or cross-reference quality scores.

**Failure boundary and alternatives.** A score is quoted as a success probability, the lower row is skipped, small numeric differences resolve conflicting evidence, or one aggregate impression hides a failed permission or recovery test. Bounded alternatives and recoveries: replace numbers with prerequisite labels, use a risk matrix keyed to read-only versus mutating commands, prioritize invocation testing for a concrete regression, or combine the rows into one release checklist.

**Counterexample, gotchas, and operational comparison.** False precision, confusing adoption tier with source authority, optimizing documentation scores instead of user behavior, and claiming local-first means current-product-correct. Good: map sources, label archive-versus-observation, then invoke a least-privilege command across failures. Bad: call a command 95-percent reliable. Borderline: test discovery first during a not-found incident, then complete provenance and evidence gates.

**Verification, evidence, and uncertainty.** Sample command changes, record gate order, defects caught at each gate, downstream rework prevented, any justified reordering, and whether all three gates passed before release. The three seed patterns and failure targets are explicit, but none of the eight local artifacts defines or validates the numeric scoring scale. Relative benefit varies with command complexity, mutation risk, installed version, and distribution scope, so causal effect must be measured locally.

**Second-order consequence.** The rows form a dependency chain: source truth defines what to build, evidence boundaries define what is known, and executable tests determine whether the installed interface honors it.

**Revision decision.** State the scale limitation, convert each pattern into a pass/fail gate, add risk-based reordering examples, and prohibit release while any prerequisite remains red.

**Retained seed evidence.** The three identifiers, values, adoption tiers, and exact failure-prevention descriptions remain preserved in the seed table. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| pattern_identifier_stable_key | pattern_score_numeric_value | pattern_tier_adoption_level | pattern_failure_prevention_target |
| --- | ---: | --- | --- |
| `plugin_command_development_patterns` | 95 | default_adoption_pattern_tier | Source Map First: Load local plugin command material before synthesizing development patterns recommendations. |
| `plugin_command_development_patterns` | 91 | default_adoption_pattern_tier | Evidence Boundary Split: Separate local facts, external facts, and inference before giving agent instructions. |
| `plugin_command_development_patterns` | 88 | default_adoption_pattern_tier | Verification Gate Coupling: Attach each recommendation to at least one command, checklist, or review gate. |

## Idiomatic Thesis Synthesis Statement

**Decision supported.** This section helps decide what governing rule should control the design and release of a Claude Code plugin slash command. The seed says to load local sources, check public analogues, and add verification, but it does not state that a command is an instruction interface whose quality depends on surface fit, least privilege, portability, observable branches, and installed-product behavior.

**Recommended default and causal basis.** Select the command surface only for explicit reusable invocation, express one outcome as directives to Claude, expose a small argument or question contract, constrain tools, move deterministic complexity into plugin resources, and validate the installed user journey. Markdown wording drives model behavior, frontmatter shapes invocation context, and plugin packaging changes paths and discovery; therefore prose, permissions, resources, and lifecycle tests jointly define the interface.

**Operating conditions and assumptions.** The task is bounded, users know when to invoke it, inputs and decisions are visible, tool effects are limited, internal files resolve through the plugin root, and failures produce safe recovery. Use the thesis for plugin command decisions and treat adjacent extension docs or current product tests as separate evidence classes.

**Failure boundary and alternatives.** Automatic enforcement, deep delegated autonomy, external protocol integration, hidden persistent state, or irreversible execution is forced into a prompt file merely because commands are easy to add. Bounded alternatives and recoveries: route to hooks, skills, agents, MCP servers, settings, or ordinary scripts according to trigger, knowledge, autonomy, integration, persistence, and determinism needs.

**Counterexample, gotchas, and operational comparison.** Describing what users will receive instead of instructing Claude, embedding shell control flow as if Markdown were a program, granting wildcard tools, relying on cwd-relative plugin files, and verifying syntax without invocation. Good: a review command gathers a named diff, applies fixed criteria, and reports findings without mutation. Bad: a vague `/run` command has unrestricted Bash and implicit deployment. Borderline: a multi-step setup command is acceptable only with state validation, confirmation, cancellation, and resume tests.

**Verification, evidence, and uncertainty.** Trace one capability from surface decision through command text, parsed metadata, help discovery, substitutions, tool approvals, plugin-root resources, branch outputs, recovery, install, update, and uninstall behavior. The local overview and seven detail references consistently cover these contract dimensions, including command instructions, frontmatter, interaction, workflow state, distribution, plugin features, documentation, and tests. Archived examples may not match the currently installed Claude Code parser or tool names, so direct current-version observation is required for release claims.

**Second-order consequence.** The command file is simultaneously prompt, permission declaration, package entry point, and user-facing API; a defect in any one layer can invalidate otherwise excellent instructions.

**Revision decision.** Replace the generic synthesis with a surface-fit rule, four-layer command contract, failure alternatives, installed-path verification, and an explicit archived-versus-current evidence boundary.

**Retained seed evidence.** The local, external, and combined evidence statements remain retained as the original synthesis frame. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`local_corpus_sourced_fact`: The local row for `plugin_command_development_patterns` contains 16 source path(s), which should be treated as the first retrieval surface for this theme.
`external_research_sourced_fact`: The external source map provides public documentation, repository, or ecosystem analogues where available.
`combined_evidence_inference_note`: Reliable use of Plugin Command Development Patterns comes from loading the local corpus first, checking public ecosystem guidance second, and converting both into verification-backed agent decisions.

## Local Corpus Source Map

**Decision supported.** This section helps decide which local artifact should be opened for the current command-development decision and when the reader has enough evidence to stop loading more corpus. The seed inventories eight unique command artifacts twice but leaves readers to infer which file answers surface basics, metadata, interaction, orchestration, documentation, packaging, distribution, or testing questions.

**Recommended default and causal basis.** Start with the skill for command semantics and basic structure, then route narrowly to frontmatter, interaction, advanced workflow, documentation, plugin features, marketplace, or testing detail according to the unresolved contract. The files divide by responsibility, so task-based progressive disclosure reduces context while preventing an attractive workflow example from overriding metadata or packaging guidance.

**Operating conditions and assumptions.** The developer names the decision, opens one canonical overview and the relevant detail heading, records duplicate path lineage, and stops when the selected source plus installed tests answer it. Route within the sixteen frozen local paths while treating runtime observations and product documentation as additional evidence, not silent replacements.

**Failure boundary and alternatives.** All sixteen paths are loaded as independent material, examples from several files are merged into an oversized command, marketplace polish precedes safety, or testing guidance is opened only after implementation. Bounded alternatives and recoveries: read only frontmatter for a metadata defect, only plugin features for path discovery, only testing for a regression matrix, consult current installed behavior for freshness, or route away when the need is not a command.

**Counterexample, gotchas, and operational comparison.** Duplicate context crowding out requirements, confusing documentation comments with executable directives, borrowing interactive questions for known arguments, and missing the separation between prompt orchestration and script logic. Good: for a portable interactive command, read skill basics, interactive branching, plugin-root features, and matching tests. Bad: read advanced workflows to invent frontmatter fields. Borderline: use marketplace guidance only after the core command passes local installation tests.

**Verification, evidence, and uncertainty.** Record decision category, chosen source and heading, duplicate copy hash, intentionally skipped files, claim extracted, current-version check, resulting command change, and whether another source altered the decision. The eight unique documents have distinct, fully read scopes and their archive/live path pairs have identical hashes in this workspace. Heading coverage does not prove current syntax, and later edits could cause the duplicate copies to diverge.

**Second-order consequence.** The source map doubles as an architectural decomposition for commands: interface, interaction, orchestration, packaging, distribution, documentation, and verification should remain separable.

**Revision decision.** Turn the table into a question-to-source router with stop conditions, duplicate collapse, misuse examples, installed-version handoff, and a compact source-selection audit.

**Retained seed evidence.** All sixteen paths, titles, heading signals, and usage roles remain unchanged in the original map. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| local_source_filepath_value | local_source_title_text | local_source_heading_signals | local_source_usage_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/command-development/SKILL.md | command-development | Command Development for Claude Code; Overview; Command Basics; What is a Slash Command?; Critical: Commands are Instructions FOR Claude; Command Locations | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/command-development/references/advanced-workflows.md | Advanced Workflow Patterns | Advanced Workflow Patterns; Overview; Multi-Step Command Patterns; Sequential Workflow Command; PR Review Workflow for #$1; Step 1: Fetch PR Details | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/command-development/references/documentation-patterns.md | Command Documentation Patterns | Command Documentation Patterns; Overview; Self-Documenting Command Structure; Complete Command Template; Command Implementation; Documentation Comment Sections | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/command-development/references/frontmatter-reference.md | Command Frontmatter Reference | Command Frontmatter Reference; Frontmatter Overview; Field Specifications; description; allowed-tools; model | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/command-development/references/interactive-commands.md | Interactive Command Patterns | Interactive Command Patterns; Overview; When to Use AskUserQuestion; Use AskUserQuestion When:; Use Command Arguments When:; AskUserQuestion Basics | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/command-development/references/marketplace-considerations.md | Marketplace Considerations for Commands | Marketplace Considerations for Commands; Overview; Design for Distribution; Universal Compatibility; Platform-Aware Command; Windows-specific handling | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/command-development/references/plugin-features-reference.md | Plugin-Specific Command Features Reference | Plugin-Specific Command Features Reference; Table of Contents; Plugin Command Discovery; Auto-Discovery; Namespaced Plugin Commands; Command Naming Conventions | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/command-development/references/testing-strategies.md | Command Testing Strategies | Command Testing Strategies; Overview; Testing Levels; Level 1: Syntax and Structure Validation; Validate YAML frontmatter; Check for closing frontmatter marker | reference detail file for deeper pattern evidence |
| claude-skills/plugins/plugin-dev/command-development/SKILL.md | command-development | Command Development for Claude Code; Overview; Command Basics; What is a Slash Command?; Critical: Commands are Instructions FOR Claude; Command Locations | skill entrypoint or reusable agent prompt |
| claude-skills/plugins/plugin-dev/command-development/references/advanced-workflows.md | Advanced Workflow Patterns | Advanced Workflow Patterns; Overview; Multi-Step Command Patterns; Sequential Workflow Command; PR Review Workflow for #$1; Step 1: Fetch PR Details | reference detail file for deeper pattern evidence |
| claude-skills/plugins/plugin-dev/command-development/references/documentation-patterns.md | Command Documentation Patterns | Command Documentation Patterns; Overview; Self-Documenting Command Structure; Complete Command Template; Command Implementation; Documentation Comment Sections | reference detail file for deeper pattern evidence |
| claude-skills/plugins/plugin-dev/command-development/references/frontmatter-reference.md | Command Frontmatter Reference | Command Frontmatter Reference; Frontmatter Overview; Field Specifications; description; allowed-tools; model | reference detail file for deeper pattern evidence |
| claude-skills/plugins/plugin-dev/command-development/references/interactive-commands.md | Interactive Command Patterns | Interactive Command Patterns; Overview; When to Use AskUserQuestion; Use AskUserQuestion When:; Use Command Arguments When:; AskUserQuestion Basics | reference detail file for deeper pattern evidence |
| claude-skills/plugins/plugin-dev/command-development/references/marketplace-considerations.md | Marketplace Considerations for Commands | Marketplace Considerations for Commands; Overview; Design for Distribution; Universal Compatibility; Platform-Aware Command; Windows-specific handling | reference detail file for deeper pattern evidence |
| claude-skills/plugins/plugin-dev/command-development/references/plugin-features-reference.md | Plugin-Specific Command Features Reference | Plugin-Specific Command Features Reference; Table of Contents; Plugin Command Discovery; Auto-Discovery; Namespaced Plugin Commands; Command Naming Conventions | reference detail file for deeper pattern evidence |
| claude-skills/plugins/plugin-dev/command-development/references/testing-strategies.md | Command Testing Strategies | Command Testing Strategies; Overview; Testing Levels; Level 1: Syntax and Structure Validation; Validate YAML frontmatter; Check for closing frontmatter marker | reference detail file for deeper pattern evidence |

## External Research Source Map

**Decision supported.** This section helps decide whether these public rows should influence a command design and exactly where their authority stops. The seed preserves an MCP resource specification and two MCP server repositories, which concern external context and tools rather than the native Markdown command file contract.

**Recommended default and causal basis.** Use MCP evidence only when deciding that an external data or action capability should live behind a protocol server and be orchestrated by a thin command, never to define command frontmatter, substitutions, discovery, or plugin paths. MCP and slash commands can compose, but they have separate schemas, lifecycles, permissions, failure modes, and test surfaces; conflating them creates an interface that neither source actually documents.

**Operating conditions and assumptions.** The command's need for an external capability is explicit, an MCP-specific source governs the server boundary, local command sources govern invocation, and integration tests exercise both sides. Retain the three links as frozen external context for MCP routing, not as authoritative command-development documentation.

**Failure boundary and alternatives.** An MCP resource page is cited for a slash-command field, a GitHub server example becomes a generic packaging rule, public repository existence proves compatibility, or stale external content overrides observed command behavior. Bounded alternatives and recoveries: omit MCP entirely for local prompt workflows, invoke a deterministic plugin script, route to a dedicated MCP integration reference, or defer the external capability until its protocol contract can be verified.

**Counterexample, gotchas, and operational comparison.** Assuming resources and tools are interchangeable, granting command permissions broader than the server capability, hiding server startup failures behind prompt prose, and treating an adjacent ecosystem as freshness evidence. Good: a command collects a repository identifier and invokes a separately configured GitHub MCP tool under a tested contract. Bad: copy MCP JSON into command frontmatter. Borderline: mention MCP as an alternative without claiming the archived links are current.

**Verification, evidence, and uncertainty.** Map each external-derived claim to a URL and extension boundary, record refresh status, require local command evidence for native behavior, test server absence and denial, and remove decorative citations. The seed directly identifies the three URLs and their MCP roles, while the local corpus demonstrates native command mechanics independently. No browsing occurred, so current specification text, repository status, and compatibility remain unverified.

**Second-order consequence.** Adjacent evidence is most valuable as a boundary detector: it helps explain what should not be embedded in a command even when it cannot specify the command itself.

**Revision decision.** Add a native-versus-MCP capability matrix, composition rules, failure separation, freshness labels, and rejection examples while preserving every external row.

**Retained seed evidence.** The MCP resources, server index, and GitHub MCP server rows remain exactly preserved beneath the boundary guidance. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| external_source_url_value | external_source_name_text | external_source_usage_role | evidence_boundary_label_value |
| --- | --- | --- | --- |
| https://modelcontextprotocol.io/specification/2025-06-18/server/resources | Model Context Protocol resources | primary MCP resource model for context sharing | external_research_sourced_fact |
| https://github.com/modelcontextprotocol/servers | MCP server implementations | reference and community server implementation index | external_research_sourced_fact |
| https://github.com/github/github-mcp-server | GitHub MCP server | GitHub-backed MCP server for repository and issue operations | external_research_sourced_fact |

## Anti Pattern Registry Table

**Decision supported.** This section helps decide which observable defect should block a command release and what safer design or stronger extension surface should replace it. The seed lists generic source, evidence, and verification failures but omits command-specific defects that arise from prompt direction, permission scope, argument interpolation, plugin paths, interaction, workflow state, and packaging.

**Recommended default and causal basis.** Block user-facing narration without agent directives, wildcard tools without necessity, unchecked substitutions into shell or paths, hardcoded plugin locations, opaque state, unconfirmed mutation, unbounded interaction, and syntax-only testing. These defects cross trust boundaries or make behavior installation-dependent, so a command may look readable while remaining unsafe, nonportable, or impossible to recover.

**Operating conditions and assumptions.** Each anti-pattern names a concrete command snippet or runtime symptom, its consequence, a prevention rule, a detection test, and a recovery or routing action. Apply this registry to command design and invocation; assess scripts, hooks, agents, and MCP servers under their own threat and lifecycle models.

**Failure boundary and alternatives.** Warnings remain abstract, unsafe behavior is excused as model judgment, validation occurs only inside prompt prose, denial paths are skipped, or mitigation adds documentation without reducing capability. Bounded alternatives and recoveries: narrow `allowed-tools`, validate through a dedicated script, pass known values as arguments, ask users only for consequential choices, use plugin-root resources, introduce explicit state and locks, or move automatic behavior to a hook.

**Counterexample, gotchas, and operational comparison.** Shell metacharacters in positional inputs, file references outside intended scope, namespace collisions, state files from another revision, partial writes, recursive command composition, and commands that claim cancellation after side effects. Good: a read-only audit command validates a target and denies writes. Bad: interpolate `$1` into unrestricted deployment Bash. Borderline: a stateful wizard is acceptable only with schema validation, lock ownership, confirmation, cleanup, and resume tests.

**Verification, evidence, and uncertainty.** Scan command text and parsed metadata, fuzz argument and path inputs, exercise permission denials, install under a path with spaces, interrupt each state transition, test duplicate invocation, and confirm cleanup and alternate-surface routing. The local sources directly warn that commands are instructions, recommend restrictive tools and plugin-root paths, describe state and interaction, and provide layered test categories. The archived examples do not establish a complete security model or current substitution semantics, so adversarial installed-version testing remains necessary.

**Second-order consequence.** The most serious command defects occur at composition boundaries where natural-language intent meets shell, filesystem, plugin packaging, or another component.

**Revision decision.** Retain the three generic rows and add command-level failure signatures, security consequences, observable tests, safe replacements, and surface-switch exits.

**Retained seed evidence.** Context-free output, unsourced claims, and unverified instruction remain preserved as umbrella anti-patterns. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| anti_pattern_failure_name | failure_cause_risk_reason | safer_default_replacement_pattern | detection_signal_review_method |
| --- | --- | --- | --- |
| context_free_summary_output | agent skips local corpus and produces generic advice | source_map_first_synthesis | verify every listed local path appears in the generated file |
| unsourced_recommendation_claims | guidance appears authoritative without source boundary | evidence_boundary_split_pattern | check for local, external, and inference labels |
| unverified_agent_instruction | recommendation cannot be checked by command or review gate | verification_gate_coupling | require concrete gate in generated reference |

## Verification Gate Command Set

**Decision supported.** This section helps decide which independent gates must pass for the evolved reference and for a concrete plugin command to be accepted. The seed includes one generated-reference verifier, while command correctness also requires structured metadata parsing, plugin discovery, substitution, permission, interaction, resource, workflow, failure, and distribution evidence.

**Recommended default and causal basis.** Run the focused reference validator, parse command frontmatter with a real YAML parser, validate file and package placement, invoke the command in a test installation, exercise its input and denial matrix, then test integration, recovery, portability, and removal. Static artifact integrity cannot prove product discovery or model behavior, and a successful happy-path invocation cannot prove least privilege, failure containment, or cross-install path correctness.

**Operating conditions and assumptions.** Each claim maps to the smallest capable test, command fixtures isolate side effects, current-version observations are recorded, and failures identify whether metadata, prompt, permission, resource, interaction, or packaging is responsible. Separate QA for this reference from QA for command artifacts and from tests of external systems those commands may call.

**Failure boundary and alternatives.** Grep counts frontmatter delimiters as full YAML validation, help discovery is assumed from file existence, scripts are trusted without exit checks, manual success replaces regression fixtures, or reference validation certifies a command. Bounded alternatives and recoveries: fix document structure separately, reduce command capability, mock deterministic scripts and integration-test the thin prompt, use a disposable plugin install, or route untestable high-risk behavior to a safer surface.

**Counterexample, gotchas, and operational comparison.** Testing a project command instead of the packaged command, warm discovery caches, inherited permissions masking missing metadata, fixtures on one platform only, and cleanup that leaves state or installed artifacts. Good: parse metadata, install the plugin, inspect help, invoke valid and invalid cases, deny extra tools, interrupt state, and uninstall. Bad: run only the archive verifier. Borderline: syntax checks suffice for a draft only when no behavior claim is made.

**Verification, evidence, and uncertainty.** Capture exact commands, versions, test plugin path, parsed metadata, discovery output, invocation transcript summary, argument cases, approvals and denials, filesystem diff, script exits, restart or resume result, platform matrix, and uninstall residue. The testing source explicitly defines seven levels from structure through integration plus edge, performance, and user-experience checks; plugin features define discovery and internal-path behavior. This reference evolution has no sample plugin command to invoke, so concrete command gates are prescribed procedures rather than observed passes.

**Second-order consequence.** Verification must follow the interface stack from file bytes to user outcome; skipping a layer creates a blind spot that a pass at another layer cannot cover.

**Revision decision.** Add a layered gate matrix, structured parsing requirement, installed-plugin fixture, security and recovery cases, evidence packet, and current focused validator while retaining the seed command.

**Retained seed evidence.** The original final-stage reference-generation command remains intact as historical artifact evidence. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`verification_gate_command_set`: Run the repository verifier after editing this file.

```bash
python3 agents-used-monthly-archive/idiomatic-references-202606/tools/verify_reference_generation.py --stage final
```

## Agent Usage Decision Guide

**Decision supported.** This section helps decide whether to use this command reference and which command shape is the smallest fit for the requested workflow. The seed activates on theme or path mentions and recommends local-first evidence, but it does not classify extension surfaces or choose among simple arguments, interactive questions, deterministic scripts, and multi-step state.

**Recommended default and causal basis.** First classify trigger, autonomy, external integration, persistence, risk, and determinism; if explicit command invocation fits, choose a simple prompt, positional interface, guided interaction, script-backed command, or stateful workflow in increasing complexity. Surface and shape classification prevents a small prompt from accreting automatic, protocol, state, or program-logic responsibilities that belong elsewhere.

**Operating conditions and assumptions.** The user can state an invocation goal, known values become arguments, only context-dependent choices become questions, deterministic work lives in testable resources, and high-risk actions retain human confirmation. Activate for Claude Code slash-command design or diagnosis; route generic shell CLI design and other extension types to their dedicated references.

**Failure boundary and alternatives.** The request is event-triggered, continuously autonomous, primarily an external API, configuration-only, or impossible to bound with command permissions and recovery. Bounded alternatives and recoveries: select a hook, skill, agent, MCP server, settings entry, standalone script, or ordinary documentation; retain a thin command only when it adds a useful explicit interface.

**Counterexample, gotchas, and operational comparison.** Triggering on the word command when the user means shell command, choosing interaction for scriptability, forcing known values through questions, composing several commands without state ownership, and using model choice as a substitute for design. Good: known PR number plus review rubric becomes an argument command. Bad: filesystem policy enforcement becomes a manually invoked prompt. Borderline: deployment orchestration can use a command only with preflight, approval, script boundaries, state, rollback, and tests.

**Verification, evidence, and uncertainty.** Record capability request, surface matrix, chosen command shape, rejected surfaces, input classification, permission budget, deterministic components, confirmation points, state lifecycle, test plan, and explicit stop condition. The skill distinguishes command locations and inputs, the interaction reference separates arguments from questions, and the remaining corpus covers scripts, workflows, plugin components, and tests. Current product feature availability and organizational risk policy may alter the best route despite the archived patterns.

**Second-order consequence.** Complexity should migrate out of the command as it becomes deterministic or persistent, leaving the Markdown file responsible for orchestration and explanation.

**Revision decision.** Replace keyword activation with a surface decision tree, command-shape ladder, input classifier, risk exits, and a concise decision record.

**Retained seed evidence.** The local-first, explicit-gate, external-check, and evidence-label bullets remain preserved beneath the classifier. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`agent_usage_decision_guide`: Use this reference when a task mentions this theme, one of the listed local source paths, or a nearby technology/workflow surface.

- Start with the local corpus source map.
- Prefer patterns with explicit verification gates.
- Treat external sources as freshness and ecosystem checks, not replacements for local repo conventions.
- Preserve the evidence boundary labels when reusing recommendations.

## User Journey Scenario

**Decision supported.** This section helps decide how a builder should turn one repeated user workflow into a command that an unfamiliar user can discover, understand, run safely, recover, and uninstall. The seed identifies a platform builder choosing among command, hook, plugin, MCP, or setting, but it does not show the decisions and evidence from capability request through installation, invocation, debugging, and removal.

**Recommended default and causal basis.** Clarify the outcome and surface, prototype the smallest directive, define inputs and tools, package portable resources, add failure and recovery branches, test in a clean plugin installation, document use, and observe removal residue. Each stage resolves a separate risk: wrong abstraction, ambiguous prompt, excess authority, local-path coupling, unhandled failure, packaging drift, or unsupported user operation.

**Operating conditions and assumptions.** The builder can state one invocation trigger and success condition, has a disposable test project, knows which effects are allowed, and can reproduce the full lifecycle without private machine assumptions. Use this scenario for commands intended for project, personal, or plugin distribution, with stricter packaging and compatibility gates as audience broadens.

**Failure boundary and alternatives.** The capability lacks a stable manual trigger, depends on invisible environment state, requires unreviewed destructive authority, or cannot be meaningfully tested outside the author's session. Bounded alternatives and recoveries: start with a project-local command for learning, extract deterministic work into a script, route event behavior to a hook, expose external operations through MCP, or postpone marketplace distribution until the local lifecycle is stable.

**Counterexample, gotchas, and operational comparison.** Designing frontmatter before clarifying outcome, testing only from the source tree, inheriting personal permissions, skipping no-argument behavior, hiding installation prerequisites, and considering successful execution the end of the journey. Good: build `/review-pr`, test absent and valid numbers, denied GitHub access, plugin-root templates, help discovery, and uninstall. Bad: publish a local deployment prompt with hardcoded paths. Borderline: release a guided setup only after interruption and restart are safe.

**Verification, evidence, and uncertainty.** Preserve the initial request, surface decision, command contract, metadata parse, fixture setup, help listing, invocation matrix, permission evidence, file diffs, recovery results, documentation check, update test, and uninstall audit. The local corpus provides concrete patterns for every stage from command basics and interaction through marketplace readiness and seven-level testing. Marketplace and product procedures may have changed since the archived sources, so current installation mechanics must be observed rather than inferred.

**Second-order consequence.** The user journey is the real integration test; a command that works only when its author knows hidden setup has not yet become a plugin interface.

**Revision decision.** Replace the generic role statement with a lifecycle scenario, checkpoints, failure exits, evidence packet, and a realistic good, bad, and borderline release path.

**Retained seed evidence.** The platform-builder role, extension-surface uncertainty, lifecycle proof goal, and opening trigger remain retained. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Role based opening scenario: The agent-tool platform builder is starting from a capability request that could become a command, hook, plugin, MCP server, or setting and needs a reference that turns source evidence into an executable next step.
Primary user starting state: The user has a `plugin_command_development_patterns` task, one or more local source paths, and uncertainty about which pattern should drive implementation.
Decision being made: choosing the right extension surface and proving install, invocation, permissions, and recovery behavior.
Reference opening trigger: Open this file when the task mentions plugin command development patterns, any mapped local source path, or an adjacent workflow with the same failure mode.

## Decision Tradeoff Guide

**Decision supported.** This section helps decide whether to adopt a command pattern directly, adapt it for local constraints, avoid the command surface, or narrow a command to orchestration around another component. The seed frames adopt, adapt, and avoid around source agreement but omits the actual tradeoffs among a simple prompt, arguments, interactive questions, script delegation, workflow state, and alternate extension surfaces.

**Recommended default and causal basis.** Adopt simple explicit workflows, adapt when permissions or packaging require narrower mechanics, avoid when trigger or lifecycle mismatches, and treat stateful or mutating commands as higher-cost designs with stronger tests. Every added question, tool, script, state file, and integration increases capability and user value but also expands ambiguity, permission, recovery, compatibility, and maintenance surfaces.

**Operating conditions and assumptions.** The option compares user trigger, scriptability, determinism, risk, audience, portability, state, integration, and verification cost before implementation begins. Make the choice per workflow and risk class rather than adopting a single command architecture across an entire plugin.

**Failure boundary and alternatives.** Local and external agreement is treated as enough, adaptation papers over invalid syntax, avoidance has no alternate route, or marketplace ambition justifies premature complexity. Bounded alternatives and recoveries: use project-local scope, split one command into composable focused commands, move logic into a tested script, replace interaction with arguments and defaults, or choose hook, agent, skill, MCP, or settings.

**Counterexample, gotchas, and operational comparison.** Underpricing prompts that mutate data, confusing easy authoring with cheap maintenance, forcing every choice into AskUserQuestion, introducing state without ownership, and treating broad compatibility claims as defaults. Good: adopt a read-only argument command; adapt resource paths with plugin root; avoid a command for automatic policy enforcement. Bad: publish a stateful wildcard-Bash workflow because the example looks complete. Borderline: command-plus-script orchestration with explicit rollback.

**Verification, evidence, and uncertainty.** Write a tradeoff record with surface fit, complexity level, permission delta, known and interactive inputs, state lifecycle, portability target, alternatives, wrong-choice cost, rollback, and evidence threshold. The corpus provides direct designs for simple, interactive, advanced, script-backed, and marketplace commands plus distinct alternatives in the seed journey. Actual model behavior, tool approval UX, and packaging compatibility vary with installed versions and user policy.

**Second-order consequence.** The cheapest reliable design often keeps the command declarative and moves repeatable mechanics into a separately testable component.

**Revision decision.** Reframe the four seed options around interface complexity, lifecycle cost, permission risk, portability, partial orchestration, and alternate surfaces.

**Retained seed evidence.** Adopt when, Adapt when, Avoid when, and Cost of being wrong remain exactly preserved in the seed table. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| decision_option_name | when_to_choose_condition | tradeoff_cost_description | verification_question_prompt |
| --- | --- | --- | --- |
| Adopt when | local corpus and external evidence agree on the plugin command development patterns pattern | fastest path, but can copy stale local assumptions | Does the selected pattern appear in the canonical source and current external evidence? |
| Adapt when | local sources are strong but public ecosystem guidance has changed | preserves repo fit, but requires explicit inference notes | Did the reference label the local fact, external fact, and combined inference separately? |
| Avoid when | source evidence is thin, conflicting, or unrelated to the user journey | prevents false confidence, but may require deeper research | Is there a confidence warning or adjacent reference route? |
| Cost of being wrong | wrong plugin command development patterns guidance can send an agent to the wrong files, tests, or abstraction | wasted implementation loop and weaker verification | Would a reviewer know what to undo and what to inspect next? |

## Local Corpus Hierarchy

**Decision supported.** This section helps decide which evidence controls a claim when overview policy, topic examples, duplicate copies, current parser behavior, plugin installation results, and command outcomes differ. The seed marks the archived skill canonical, seven archive details supporting, and eight identical live paths as supporting context or detail, but it does not define conflict resolution with installed behavior or future divergence.

**Recommended default and causal basis.** Use the skill for archived conceptual defaults, the matching detail file for topic depth, hashes to collapse duplicates, installed parsing and discovery for current interface facts, and controlled command tests for behavioral outcomes. Authority is claim-relative: prose can describe intent, but only the current parser can accept metadata and only an invocation can demonstrate substitutions, permissions, resource paths, and recovery.

**Operating conditions and assumptions.** The reviewer classifies the claim, compares relevant evidence only, preserves version and hash identity, records disagreements, and updates guidance without rewriting frozen source roles. Preserve the frozen canonical and supporting labels while layering duplicate lineage and current observations as separate evidence dimensions.

**Failure boundary and alternatives.** Canonical is treated as universally current, two identical paths count as consensus, an example overrides a field reference, a successful run excuses insecure scope, or product behavior silently changes the archive. Bounded alternatives and recoveries: downgrade the claim, verify with a minimal fixture, inspect current official documentation when allowed, keep both interpretations, or block release until the conflict is reproducible.

**Counterexample, gotchas, and operational comparison.** Copy divergence after one path changes, discovery caches, inherited permission state, examples using pseudocode-like control flow, and test fixtures that accidentally validate a project command instead of plugin packaging. Good: archive frontmatter explains intent, a parser fixture establishes current acceptance, and invocation establishes behavior. Bad: two identical files prove a feature. Borderline: current behavior differs; follow it operationally while recording archive drift and version.

**Verification, evidence, and uncertainty.** Maintain a conflict ledger with claim class, source paths and hashes, installed version, fixture, observed result, selected authority, security implications, documentation action, and unresolved risk. The local files' roles and exact duplicate hashes are known, and the testing corpus explicitly separates structure from runtime integration. Without current external documentation, an observed discrepancy may reflect version drift, environment configuration, or an archival error.

**Second-order consequence.** The hierarchy should route questions to capable evidence rather than rank documents by prestige; current observations strengthen behavior claims but do not automatically establish design wisdom.

**Revision decision.** Add claim-relative precedence, duplicate collapse, installed-version fixtures, conflict handling, security review, and refresh obligations.

**Retained seed evidence.** All sixteen hierarchy rows and their canonical, supporting context, and supporting detail roles remain unchanged. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Classification vocabulary includes canonical, supporting, legacy, duplicate, and conflicting source roles.

| local_source_filepath_value | corpus_hierarchy_role | heading_signal_to_convert | reviewer_question_to_answer |
| --- | --- | --- | --- |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/command-development/SKILL.md | canonical primary source | Command Development for Claude Code; Overview; Command Basics | What guidance, warning, or example should this source contribute to Plugin Command Development Patterns? |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/command-development/references/advanced-workflows.md | supporting detail source | Advanced Workflow Patterns; Overview; Multi-Step Command Patterns | What guidance, warning, or example should this source contribute to Plugin Command Development Patterns? |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/command-development/references/documentation-patterns.md | supporting detail source | Command Documentation Patterns; Overview; Self-Documenting Command Structure | What guidance, warning, or example should this source contribute to Plugin Command Development Patterns? |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/command-development/references/frontmatter-reference.md | supporting detail source | Command Frontmatter Reference; Frontmatter Overview; Field Specifications | What guidance, warning, or example should this source contribute to Plugin Command Development Patterns? |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/command-development/references/interactive-commands.md | supporting detail source | Interactive Command Patterns; Overview; When to Use AskUserQuestion | What guidance, warning, or example should this source contribute to Plugin Command Development Patterns? |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/command-development/references/marketplace-considerations.md | supporting detail source | Marketplace Considerations for Commands; Overview; Design for Distribution | What guidance, warning, or example should this source contribute to Plugin Command Development Patterns? |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/command-development/references/plugin-features-reference.md | supporting detail source | Plugin-Specific Command Features Reference; Table of Contents; Plugin Command Discovery | What guidance, warning, or example should this source contribute to Plugin Command Development Patterns? |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/command-development/references/testing-strategies.md | supporting detail source | Command Testing Strategies; Overview; Testing Levels | What guidance, warning, or example should this source contribute to Plugin Command Development Patterns? |
| claude-skills/plugins/plugin-dev/command-development/SKILL.md | supporting context source | Command Development for Claude Code; Overview; Command Basics | What guidance, warning, or example should this source contribute to Plugin Command Development Patterns? |
| claude-skills/plugins/plugin-dev/command-development/references/advanced-workflows.md | supporting detail source | Advanced Workflow Patterns; Overview; Multi-Step Command Patterns | What guidance, warning, or example should this source contribute to Plugin Command Development Patterns? |
| claude-skills/plugins/plugin-dev/command-development/references/documentation-patterns.md | supporting detail source | Command Documentation Patterns; Overview; Self-Documenting Command Structure | What guidance, warning, or example should this source contribute to Plugin Command Development Patterns? |
| claude-skills/plugins/plugin-dev/command-development/references/frontmatter-reference.md | supporting detail source | Command Frontmatter Reference; Frontmatter Overview; Field Specifications | What guidance, warning, or example should this source contribute to Plugin Command Development Patterns? |
| claude-skills/plugins/plugin-dev/command-development/references/interactive-commands.md | supporting detail source | Interactive Command Patterns; Overview; When to Use AskUserQuestion | What guidance, warning, or example should this source contribute to Plugin Command Development Patterns? |
| claude-skills/plugins/plugin-dev/command-development/references/marketplace-considerations.md | supporting detail source | Marketplace Considerations for Commands; Overview; Design for Distribution | What guidance, warning, or example should this source contribute to Plugin Command Development Patterns? |
| claude-skills/plugins/plugin-dev/command-development/references/plugin-features-reference.md | supporting detail source | Plugin-Specific Command Features Reference; Table of Contents; Plugin Command Discovery | What guidance, warning, or example should this source contribute to Plugin Command Development Patterns? |
| claude-skills/plugins/plugin-dev/command-development/references/testing-strategies.md | supporting detail source | Command Testing Strategies; Overview; Testing Levels | What guidance, warning, or example should this source contribute to Plugin Command Development Patterns? |

## Theme Specific Artifact

**Decision supported.** This section helps decide what artifact must be completed before a plugin command can be reviewed as an interface rather than as an isolated Markdown prompt. The seed names command anatomy with arguments, interactive flow, test harness, and marketplace readiness, but its three generic fields cannot reproduce the interface, permissions, resources, state, recovery, or distribution proof.

**Recommended default and causal basis.** Create a command contract packet covering purpose and non-goals, surface rationale, filename and namespace, prompt directives, metadata, input grammar, questions, tools, plugin resources, deterministic scripts, effects, state, confirmations, errors, recovery, tests, docs, compatibility, and removal. Reviewers need a single trace from user invocation to side effects and evidence; otherwise risk hides between frontmatter, natural language, package layout, and external components.

**Operating conditions and assumptions.** The packet is concrete enough to build fixtures, every field has an owner and evidence location, nonapplicable capabilities are explicit, and high-risk effects link to confirmation and rollback. Require the full packet for distributed or mutating commands and allow a justified smaller variant for read-only personal commands.

**Failure boundary and alternatives.** The artifact copies the command file without analysis, lists tools without necessity, omits no-argument and denial behavior, treats marketplace polish as readiness, or cannot identify all writes and external calls. Bounded alternatives and recoveries: use a minimal contract for a read-only local command, add a state-transition appendix for workflows, add a platform matrix for distribution, or replace the design with another surface when the packet exposes mismatch.

**Counterexample, gotchas, and operational comparison.** Metadata and prompt disagreeing on tools, examples using different argument order, plugin resources absent from package, state schema without revision, script exit output ignored, and uninstall leaving project files. Good: a PR-review packet declares read-only effects, PR argument, GitHub dependency, denial output, report schema, and install fixture. Bad: a deploy prompt plus wildcard Bash. Borderline: a setup wizard with explicit files, confirmation, restart, and cleanup contracts.

**Verification, evidence, and uncertainty.** Derive a test from every contract row, parse metadata, inspect package contents, invoke all input classes, capture approvals, diff the fixture filesystem, interrupt state transitions, replay recovery, test platform claims, and audit uninstall. All packet dimensions are directly represented across the eight unique sources, and the seed explicitly requires arguments, interaction, testing, and marketplace readiness. Some current frontmatter fields or packaging rules may differ from the archive and must be filled from installed observations rather than assumption.

**Second-order consequence.** The artifact is an executable design review: gaps in its test derivation expose undefined behavior before natural-language flexibility turns it into production ambiguity.

**Revision decision.** Expand the three rows into a lifecycle command contract, risk and effects inventory, state model, test derivation, compatibility evidence, and removal audit.

**Retained seed evidence.** The user goal, decision boundary, and verification gate rows remain preserved as the artifact's foundation. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Theme specific artifact: command anatomy with arguments, interactive flow, test harness, and marketplace readiness.

| artifact_field_name | artifact_completion_rule | evidence_source_hint |
| --- | --- | --- |
| user_goal_statement | state the user's concrete goal before applying Plugin Command Development Patterns | local corpus hierarchy plus critique findings |
| decision_boundary_rule | define the point where this reference should be used or avoided | decision tradeoff guide |
| verification_gate_rule | define the command, checklist, or review question that proves the artifact worked | verification gate command set |

## Worked Example Set

**Decision supported.** This section helps decide what concrete evidence distinguishes a well-designed command, a dangerous misuse, and a conditionally acceptable complex workflow. The seed gives generic source-loading contrasts but no actual command text decisions involving arguments, interaction, permissions, plugin paths, state, failure, or installation.

**Recommended default and causal basis.** Compare examples across surface fit, directive clarity, input choice, least privilege, portable resources, side effects, recovery, and installed test evidence. The same workflow label can hide radically different contracts, so examples must expose consequences and repair paths rather than merely praise or condemn style.

**Operating conditions and assumptions.** The good case is small and reproducible, the bad case shows a plausible failure with user impact, and the borderline case states additional gates that make only a narrower claim acceptable. Use examples to calibrate design reasoning, not as copy-ready command files or proof of current product syntax.

**Failure boundary and alternatives.** Examples vary only in polish, unsafe behavior is cartoonish, the good case assumes permissions, or the borderline case receives unconditional approval. Bounded alternatives and recoveries: use read-only review, interactive configuration, stateful deployment, MCP-backed lookup, or marketplace portability examples depending on the decision being taught.

**Counterexample, gotchas, and operational comparison.** Calling output helpful without verifying it, mistaking a detailed prompt for a safe one, showing paths that work only in source checkout, and omitting invalid-input and cancellation behavior. Good: `/summarize-diff` uses a known target, read-only Git context, clear output, and denial tests. Bad: `/deploy` embeds unchecked arguments in broad shell access with no confirmation. Borderline: `/setup-service` is acceptable only with validated choices, atomic writes, restart, rollback, and clean uninstall.

**Verification, evidence, and uncertainty.** For each case, identify trigger, command contract, metadata, inputs, tools, resources, effects, test fixture, expected success, expected failure, recovery, distribution scope, and reviewer verdict. Local examples directly cover review, setup, deployment, plugin scripts, input validation, workflow state, atomicity, and distribution testing. These are reasoned examples rather than executions against a supplied plugin, so syntax details remain subject to current-version fixtures.

**Second-order consequence.** Borderline commands reveal an escalation rule: as effects and state grow, a command should become thinner and its deterministic implementation and recovery more explicit.

**Revision decision.** Replace generic source examples with read-only, unsafe mutating, and conditionally stateful cases that include consequences, counterexamples, evidence, and recovery.

**Retained seed evidence.** The original good, bad, and borderline evidence-boundary sentences remain retained. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Good example: Use Plugin Command Development Patterns after loading the canonical source, confirming the external evidence boundary, and writing a verification gate before implementation.
Bad example: Use Plugin Command Development Patterns as a generic tutorial while ignoring the mapped local paths, source hierarchy, and cost of being wrong.
Borderline case: Use Plugin Command Development Patterns only after adding a confidence warning when local evidence is thin or conflicts with current ecosystem guidance.

## Outcome Metrics and Feedback Loops

**Decision supported.** This section helps decide which signals demonstrate that a command is discoverable, safe, portable, recoverable, and useful, and how observed failures should change the contract. The seed's leading indicator is install, invoke, debug, and remove without code reading, while its failure signal is extension confusion or missing recovery; it does not define measurements or learning actions.

**Recommended default and causal basis.** Track clean-install discovery, valid-task completion, invalid-input containment, unnecessary approval prompts, denied-tool recovery, interruption recovery, platform and path portability, support-free diagnosis, update compatibility, and uninstall residue. Invocation volume rewards popularity but not reliability; lifecycle and containment signals reveal whether unfamiliar users can operate the interface without hidden author knowledge.

**Operating conditions and assumptions.** Metrics define cohort, denominator, command version, fixture state, expected effect, evidence, adverse threshold, owner, and the exact prompt, package, permission, or documentation change triggered. Measure command and distribution workflow quality, not model capability or external service reliability without separate controls.

**Failure boundary and alternatives.** Successful invocations exclude retries, support tickets are ignored, broad permissions make completion look easier, test installations share author state, or user satisfaction substitutes for side-effect correctness. Bounded alternatives and recoveries: use qualitative usability sessions at low volume, track only lifecycle gate failures before distribution, sample high-risk branches, or compare command versus direct workflow effort with matched tasks.

**Counterexample, gotchas, and operational comparison.** Mixing personal and marketplace users, counting cancellations as failures without intent, hiding inherited permissions, attributing external outages to prompt quality, and optimizing help text while recovery remains broken. Good: measure first-install discovery and recovery from denied GitHub access with versioned fixtures. Bad: claim reliability from total runs. Borderline: report improved completion time while retaining separate safety and cleanup outcomes.

**Verification, evidence, and uncertainty.** Publish metric definitions, task cohorts, raw counts, exclusions, fixture and version identity, permission state, side-effect checks, reviewer rubric, confidence caveats, and feedback-to-change trace. The seed establishes the desired lifecycle and failure categories, while testing and marketplace sources provide observable discovery, edge-case, portability, UX, and removal behaviors. No usage dataset accompanies the corpus, so targets and causal improvements must be established locally rather than fabricated.

**Second-order consequence.** The highest-value feedback often comes from contained failure: a clear denial or restart path can prove interface quality more strongly than another happy-path completion.

**Revision decision.** Operationalize lifecycle, containment, portability, support, and cleanup signals with denominators, version cohorts, owners, and explicit feedback actions.

**Retained seed evidence.** The install-invoke-debug-remove leading indicator, extension-confusion failure signal, and refresh cadence remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Leading indicator: users can install, invoke, debug, and remove the extension without reading implementation code.
Failure signal: the reference confuses adjacent extension types or omits failure recovery.
Review cadence: Re-run the verifier after every generated-reference edit and refresh external sources when public APIs, docs, or tooling releases change.

## Completeness Checklist

**Decision supported.** This section helps decide what evidence must exist before a command reference or concrete plugin command is complete for its claimed scope. The seed checks role, options, hierarchy, artifact, examples, metrics, and routing, but omits command surface fit, directive quality, metadata parsing, permissions, resource portability, side effects, state, recovery, installed invocation, and removal.

**Recommended default and causal basis.** Require the seven seed categories plus surface rationale, prompt and input contract, least-required tools, plugin-root resources, effect inventory, confirmation, failure and recovery, layered fixtures, current-version observation, documentation, compatibility claims, and uninstall audit. A missing layer can leave a command structurally valid yet undiscoverable, overprivileged, nonportable, state-corrupting, or impossible for an unfamiliar user to recover.

**Operating conditions and assumptions.** Every checkbox points to a saved artifact or observed result, nonapplicable items include rationale, higher-risk claims demand stronger tests, and reconciliation edits trigger affected checks again. Apply the full checklist to published plugin commands and document justified reductions for local read-only use.

**Failure boundary and alternatives.** Checkmarks have no evidence, parsing substitutes for invocation, happy paths substitute for denial and interruption, documentation claims exceed tested platforms, or marketplace readiness is inferred from polish. Bounded alternatives and recoveries: use a reduced checklist for a read-only personal command, add state and rollback gates for mutating workflows, add distribution and platform gates for marketplace scope, or route away from commands.

**Counterexample, gotchas, and operational comparison.** Testing the source checkout instead of packaged files, inherited tools hiding metadata errors, examples diverging from actual arguments, uninstall leaving state, and a current pass on one version becoming a timeless claim. Good: each lifecycle and safety item links to fixture evidence. Bad: declare complete because YAML and Markdown parse. Borderline: a personal read-only command may omit marketplace tests while explicitly limiting scope.

**Verification, evidence, and uncertainty.** Audit every checkbox against contract row, command file, package file, parser result, help output, invocation case, permission evidence, filesystem diff, recovery transcript, compatibility fixture, and removal result. The local corpus directly covers all added dimensions, and the seed checklist preserves the reference-level completeness frame. Organization-specific privacy, security, accessibility, or marketplace policy may require extra gates beyond the archived corpus.

**Second-order consequence.** Completeness is scope-relative but never implicit; reducing distribution or effects can reduce required gates, whereas merely calling a command simple cannot.

**Revision decision.** Extend each seed category with evidence pointers, command-contract gates, risk-based applicability, package lifecycle checks, and a final reviewer replay.

**Retained seed evidence.** All seven original checklist bullets remain unchanged as top-level categories. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- The role scenario names the user, starting state, decision, and trigger for Plugin Command Development Patterns.
- The decision guide includes Adopt when, Adapt when, Avoid when, and Cost of being wrong.
- The local corpus hierarchy identifies canonical and supporting sources or gives a confidence warning.
- The theme specific artifact is concrete enough to review without reading every mapped source.
- The examples cover good, bad, and borderline usage.
- The metrics section names one leading indicator and one failure signal.
- The adjacent routing section points to a better reference when this one is not the right fit.

## Adjacent Reference Routing

**Decision supported.** This section helps decide where to route when invocation trigger, domain knowledge, autonomy, event handling, external integration, persistent configuration, package structure, or deterministic execution dominates. The seed names command, hook, MCP, settings, manifest, plugin, and development references but does not define the capability gap that triggers each handoff or what evidence must travel.

**Recommended default and causal basis.** Stay here for slash-command interfaces; route automatic events to hooks, reusable expertise to skills, delegated tasks to agents, external services to MCP, policy values to settings, packaging to manifest guidance, and deterministic mechanics to scripts. A useful adjacent route changes lifecycle or evidence capability rather than merely opening a similarly named document.

**Operating conditions and assumptions.** The unresolved need is explicit, the destination owns it, the command packet carries minimal context, and returned evidence is reconciled without losing the original interface boundary. Route at capability boundaries and preserve command responsibility for its own invocation, explanations, and user-visible recovery.

**Failure boundary and alternatives.** Routing follows keywords, several extension references are opened at once, a command remains responsible for another component's lifecycle, or handoff results silently broaden permissions or scope. Bounded alternatives and recoveries: retain a thin command as a user-facing orchestrator, use project-local commands before plugin packaging, split one capability across explicit components, or decline integration when ownership and tests are unclear.

**Counterexample, gotchas, and operational comparison.** Hook-command recursion, agents launched without tool budgets, skills treated as executable automation, MCP failures hidden as prompt errors, settings mutated without schema, and manifests assumed to prove runtime discovery. Good: a command gathers intent and calls a tested plugin script; a hook enforces the automatic policy. Bad: simulate background enforcement through a manual command. Borderline: command plus MCP is valid when each permission, failure, and test boundary is separate.

**Verification, evidence, and uncertainty.** Record route trigger, destination capability, handoff fields, ownership, permissions, lifecycle, evidence returned, interface changes, contradictions, integration tests, and whether work returns or remains in the adjacent reference. The seed journey explicitly lists adjacent extension surfaces, and the local corpus describes command integration with scripts, agents, skills, hooks, and MCP. Specific adjacent reference filenames and current platform capabilities may evolve, so routing remains capability-based.

**Second-order consequence.** Component composition is safest when the command keeps user intent and presentation while each adjacent component owns one distinct mechanism.

**Revision decision.** Replace generic neighboring labels with capability triggers, minimal handoff packets, permission and lifecycle ownership, return criteria, and integration examples.

**Retained seed evidence.** The original plugin, command, and development pointers plus command-hook-MCP-settings-manifest guidance remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Adjacent reference guidance: Use command, hook, MCP, settings, or manifest references when one extension surface is already selected.
Adjacent reference 1: consider the plugin adjacent reference when the current task pivots away from plugin command development patterns.
Adjacent reference 2: consider the command adjacent reference when the current task pivots away from plugin command development patterns.
Adjacent reference 3: consider the development adjacent reference when the current task pivots away from plugin command development patterns.

## Workload Model

**Decision supported.** This section helps decide how much behavior one command and one review packet should own before the design must be split, delegated, or moved to another component. The seed sets one task, ten source files, three delegated subtasks, and a completion audit, but command complexity is more directly driven by inputs, tool capabilities, side effects, workflow states, integrations, and distribution environments.

**Recommended default and causal basis.** Keep one command centered on one user outcome, bound argument and question surfaces, minimize tool classes and integrations, externalize deterministic logic, and split independent state machines or ownership domains. Natural-language orchestration becomes harder to reason about as effects and branches multiply, even when source count remains low; packaging and recovery complexity also grows with audience breadth.

**Operating conditions and assumptions.** The packet inventories inputs, branches, tools, resources, effects, states, integrations, platforms, owners, and test cases, and it has a clear threshold for decomposition. Use this model for command and review ownership; evaluate external script or server throughput with component-specific methods.

**Failure boundary and alternatives.** One command performs unrelated setup, migration, deployment, and reporting, parallel delegates mutate shared state, context grows through raw outputs, or a ten-file limit is treated as proof of simplicity. Bounded alternatives and recoveries: compose focused commands, introduce a deterministic script library, delegate independent analysis to agents with isolated outputs, use explicit workflow state, or replace the surface with a service or hook.

**Counterexample, gotchas, and operational comparison.** Hidden complexity in shell snippets, interaction loops multiplying branches, plugin resources loaded wholesale, state schema changes, integration fanout, and distribution matrices expanding after marketplace release. Good: a command validates one target and delegates a bounded script, then summarizes evidence. Bad: an all-purpose release command spans repositories and environments. Borderline: a multi-step workflow can remain one command only with explicit state, ownership, resume, rollback, and tests.

**Verification, evidence, and uncertainty.** Measure command outcomes, input variants, interaction branches, tool and integration count, effects, state transitions, context size, platform fixtures, owner boundaries, test cases, and decomposition decisions. Advanced workflows, plugin features, marketplace, interaction, and testing sources collectively expose the complexity dimensions missing from the seed's numeric capacity model. No universal branch, tool, file, or platform threshold is supported; limits must follow risk and observed reviewability.

**Second-order consequence.** The binding capacity is reviewable behavior, not prompt length: a short command that calls broad tools can exceed safe workload before a long read-only rubric does.

**Revision decision.** Retain seed capacity rows but add behavioral dimensions, decomposition triggers, state and integration ownership, context controls, and risk-adjusted evidence.

**Retained seed evidence.** The four workload rows and the one-task, ten-source, three-subtask seed boundary remain preserved as provisional operating metadata. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`combined_evidence_inference_note`: Treat Plugin Command Development Patterns as a agent workflow operating reference, not as a prose summary.

| workload_dimension_name | workload_boundary_value | verification_pressure_point |
| --- | --- | --- |
| primary_usage_surface | agent planning, tool use, context loading, delegation, or skill/plugin execution where bad guidance compounds across long-running sessions | verify that the reference changes the next implementation or review action |
| bounded_capacity_model | one primary task, up to 10 source files, up to 3 delegated subtasks, and a written completion audit for every run | split the task or create a narrower reference when this boundary is exceeded |
| source_pressure_model | local heading signals include Command Development for Claude Code; Overview; Command Basics; What is a Slash Command?; Critical: Commands are Instructions FOR Claude; Command Locat | compare guidance against canonical local sources before following external examples |
| artifact_pressure_model | required artifact is command anatomy with arguments, interactive flow, test harness, and marketplace readiness | require the artifact before claiming the reference is operationally usable |

## Reliability Target

**Decision supported.** This section helps decide which command properties are deterministic release gates and which outcomes require sampled observation with explicit denominators. The seed sets complete evidence labels, 18-of-20 routing, zero unsupported claims, and universal recovery paths, but it neither marks these as proposed targets nor covers discovery, least privilege, side-effect containment, portability, and cleanup.

**Recommended default and causal basis.** Enforce hard gates for parseability, package presence, least-required permissions, declared effects, recovery instructions, and no unsupported high-impact claims; sample routing, first-use success, portability, and recovery outcomes separately. Artifact and safety invariants can demand complete compliance, while human-model interaction and diverse installations require empirical cohorts rather than invented certainty.

**Operating conditions and assumptions.** Each target names unit, command version, fixture, hard-or-sampled class, denominator, evidence collector, failure consequence, and retest rule. Treat seed values as acceptance proposals or sampling goals, never as achieved product or model reliability.

**Failure boundary and alternatives.** 18 of 20 is advertised as measured accuracy, complete labels imply correct behavior, broad tools pass because the command succeeds, or recovery documentation is counted without an interruption test. Bounded alternatives and recoveries: retain strict structural and permission gates, bootstrap outcome baselines with qualitative tests, sample high-risk commands more heavily, or limit distribution until compatibility evidence grows.

**Counterexample, gotchas, and operational comparison.** Small samples, inherited permissions, excluding abandoned runs, conflating external outages with command faults, testing only author platforms, and counting a clean uninstall without inspecting generated project state. Good: block wildcard tools as a hard gate and separately sample whether new users route to commands correctly. Bad: claim 90-percent reliability from the seed target. Borderline: release locally with full safety gates while marketplace portability remains explicitly unclaimed.

**Verification, evidence, and uncertainty.** For every target, record definition, class, command and plugin version, fixture, denominator, observed result, adverse cases, uncertainty, owner, remediation, and next measurement window. The seed supplies four reliability concerns and local sources provide direct discovery, permission, edge, recovery, distribution, and cleanup test surfaces. No evaluated command cohort accompanies the archive, so outcome rates and useful thresholds remain hypotheses.

**Second-order consequence.** Command reliability has two axes: interface safety can be gated before release, while behavioral usability must keep learning from real invocations.

**Revision decision.** Classify targets, add lifecycle and least-privilege gates, define empirical cohorts, require denominators and miss handling, and prohibit unsupported achieved-rate claims.

**Retained seed evidence.** The four original reliability rows and numeric thresholds remain exactly preserved as seed contracts. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| reliability_target_name | measurable_threshold_value | evidence_collection_method |
| --- | --- | --- |
| source_boundary_preservation | 100 percent of recommendations keep local, external, and inference boundaries visible | review generated text for the three evidence labels before reuse |
| decision_accuracy_sample | at least 18 of 20 sampled uses route to the correct adopt, adapt, avoid, or adjacent-reference decision | sample downstream tasks and record reviewer verdicts |
| unsupported_claim_rate | zero unsupported production, security, latency, or reliability claims in final guidance | reject claims without source row, explicit inference note, or verification method |
| recovery_path_clarity | every avoid or failure case names the rollback, escalation, or next-reference route | inspect failure-mode and adjacent-routing sections together |

## Failure Mode Table

**Decision supported.** This section helps decide which layer failed, what effects may already exist, which conclusions or state are invalid, and what recovery evidence is required. The seed covers drift, generic guidance, context loss, and tool fanout, but omits command discovery, metadata rejection, substitution errors, permission denial, resource paths, state corruption, partial effects, integration failure, and uninstall residue.

**Recommended default and causal basis.** Classify failures across surface choice, package discovery, metadata, prompt interpretation, input substitution, permissions, plugin resources, scripts, interaction, state, external integration, documentation, update, or removal. Layer-specific classification avoids unsafe retries and broad rewrites; a help-list failure differs fundamentally from a partial deployment or stale workflow state.

**Operating conditions and assumptions.** The first observable signal identifies a layer, side effects are inventoried, further mutation stops, recovery is bounded, fixtures reproduce the case, and recurrence changes the contract or test suite. Use this table for command and plugin-lifecycle failures, while diagnosing called scripts or MCP servers with their component-specific evidence.

**Failure boundary and alternatives.** All problems become prompt wording, nonzero script exits are summarized away, denied tools trigger broader permissions, partial files are overwritten, or cleanup is attempted without knowing state ownership. Bounded alternatives and recoveries: repair packaging, parse metadata, narrow tools, sanitize or redesign inputs, restore plugin resources, roll back deterministic scripts, reset validated state, isolate external failures, or route the capability elsewhere.

**Counterexample, gotchas, and operational comparison.** Discovery cache, path spaces, quoted arguments, permission inheritance, question cancellation after writes, stale lock files, script output without exit status, and updates that strand old state schemas. Good: a missing plugin resource stops before effects and reports install repair. Bad: grant wildcard Bash after denial. Borderline: preserve a partially completed workflow only when state schema and resume preconditions validate.

**Verification, evidence, and uncertainty.** Capture command and plugin version, layer, input, permission state, first signal, filesystem and external effects, state snapshot, reproduction fixture, mitigation, rollback or resume result, regression test, and prevention owner. All added layers appear directly across command basics, frontmatter, plugin features, advanced workflows, interaction, marketplace, and testing sources. Current product bugs and organization-specific policy failures can add classes not represented in the archive.

**Second-order consequence.** Failure handling should trace effect lineage: the correct recovery depends less on the final error message than on which actions occurred before it.

**Revision decision.** Retain the four generic rows and add command-layer taxonomy, side-effect containment, state-aware recovery, reproduction fixtures, and recurrence feedback.

**Retained seed evidence.** Source drift, generic advice, context loss, and tool fanout remain preserved as cross-cutting failure modes. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| failure_mode_name | likely_trigger_condition | required_mitigation_action |
| --- | --- | --- |
| source drift hides truth | external or local guidance changes after the reference was written | refresh public evidence, rerun local corpus gate, and mark stale claims before reuse |
| generic advice escapes review | agent copies plausible best practices without theme-specific verification | block completion until the verification gate names concrete command, reviewer question, or metric |
| context window loses plan | long-running session forgets early constraints or overwrites user intent | write checkpoint summaries and re-read plan before each destructive step |
| tool fanout outruns budget | parallel actions create conflicts, duplicate work, or unbounded external calls | cap fanout, assign ownership, and require merge/audit checkpoints |

## Retry Backpressure Guidance

**Decision supported.** This section helps decide when a failed command invocation may be retried, when mutation must stop, and when the user should resume, roll back, repair installation, or switch surfaces. The seed limits stale-evidence retries and stops on red gates, but it does not define safe command replay, idempotency, state ownership, external side effects, or how arguments and environment must be frozen between attempts.

**Recommended default and causal basis.** Retry only after classifying the failed layer, proving previous effects and state, changing a relevant prerequisite, preserving the original input contract, and confirming the next attempt is idempotent or explicitly compensated. A command retry can repeat shell, filesystem, deployment, or external operations; unchanged prompt repetition may multiply damage while hiding the original failure.

**Operating conditions and assumptions.** Attempt identity, budget, owner, state version, effect ledger, changed prerequisite, confirmation need, and semantic success condition are recorded before replay. Apply command-level retry controls and delegate external service or script retry policy to the owning component.

**Failure boundary and alternatives.** The model retries after tool denial by broadening access, network ambiguity triggers duplicate mutation, state is recreated over partial work, a new argument masks the same failure, or concurrency bypasses a lock. Bounded alternatives and recoveries: resume from a validated checkpoint, roll back through a tested script, repair packaging, ask the user to reconfirm, isolate an external service test, switch to manual recovery, or redesign the command as a thinner orchestrator.

**Counterexample, gotchas, and operational comparison.** At-least-once external APIs, stale lock files, duplicated notifications, temp directories from prior attempts, cached discovery, changed cwd, plugin update between retries, and cancellation that did not undo effects. Good: one retry after restoring a missing read-only resource and rechecking zero effects. Bad: rerun a timed-out deployment blindly. Borderline: resume a stateful setup only after schema, completed steps, ownership, and compensation are verified.

**Verification, evidence, and uncertainty.** Record failure fingerprint, invocation ID, exact inputs, environment and version, effects before and after, state hash, changed prerequisite, attempt count, confirmation, command output, semantic result, cleanup, and stop or escalation. Advanced workflow and marketplace sources explicitly discuss locks, checkpoints, idempotency, atomicity, rollback, and cleanup, while the seed requires bounded retries and ownership. Appropriate attempt budgets and compensation guarantees depend on the called operations and cannot be universalized.

**Second-order consequence.** Backpressure preserves user trust by making uncertainty visible before another invocation converts it into an additional side effect.

**Revision decision.** Add invocation identity, effect ledger, idempotency and compensation gates, state validation, concurrency ownership, semantic success, and modality-switch exits.

**Retained seed evidence.** The original classification, bounded refresh retry, red-gate stop, checkpoint, and sole-owner bullets remain retained. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- Retry only after the failed verification signal is classified as transient, stale evidence, missing context, or true contradiction.
- Use one bounded retry for stale external evidence refresh, then escalate to a human or a narrower source-specific reference.
- Apply backpressure by stopping new generation or implementation work when source coverage, critique coverage, or verification gates are red.
- For long-running agent workflows, checkpoint after each batch and re-read the current spec before any broad rewrite, commit, push, or destructive operation.
- For distributed execution, assign one owner per generated file or theme batch and require merge-time verification of exact path, heading, and evidence-boundary invariants.

## Observability Checklist

**Decision supported.** This section helps decide which minimal observations let maintainers reconstruct why a command behaved as it did without retaining sensitive prompts, file contents, credentials, or raw transcripts. The seed tracks loaded sources, proof, timing, tool calls, context, delegation, retries, outcomes, and concise audit evidence but omits command identity, metadata, inputs, permissions, effects, state, resources, installation, and privacy.

**Recommended default and causal basis.** Record command and plugin version, install scope, invocation class, redacted input shape, parsed metadata, granted and denied tools, resource and script status, state transitions, side-effect summary, errors, recovery, and user-visible outcome. Correlating interface, environment, capability, and effect state distinguishes prompt ambiguity from packaging, permission, dependency, or external failures while preserving a reviewable record.

**Operating conditions and assumptions.** Events share an invocation identifier, sensitive values are redacted at collection, timestamps and versions are stable, failures and cancellations remain visible, and summaries link to contract fields. Capture command lifecycle evidence with least data and route external component telemetry to its owner.

**Failure boundary and alternatives.** Raw prompts or command outputs leak data, success-only logs hide containment, tool-call counts have no capability context, filesystem writes are untracked, or installation scope cannot be reconstructed. Bounded alternatives and recoveries: use local fixture logs during development, aggregate privacy-preserving lifecycle metrics for distribution, capture script-level traces separately, or rely on a manual evidence packet for low-volume commands.

**Counterexample, gotchas, and operational comparison.** Arguments containing secrets, absolute user paths, inherited permissions, nested agent or MCP calls losing correlation, state updates after cancellation, and observability itself widening allowed tools. Good: a redacted record shows `/review-pr`, plugin version, GitHub denial, no writes, and recovery guidance. Bad: store the full review target and transcript. Borderline: capture detailed fixture traces in development but ship only aggregate lifecycle events.

**Verification, evidence, and uncertainty.** Sample records and reconstruct package, invocation class, permission decision, resource lookup, state and effects, failure layer, recovery, and result; inspect redaction with adversarial inputs and confirm opt-out or retention policy. The seed provides compact audit principles and workflow counters, while local sources expose every command lifecycle dimension to correlate. Telemetry storage, consent, retention, and privacy requirements depend on deployment policy and are not defined by the archived command corpus.

**Second-order consequence.** Observability is useful when it localizes the first contract divergence, not when it merely proves that the model and tools were active.

**Revision decision.** Add invocation correlation, version and scope, redacted inputs, metadata and permission state, resource and side-effect events, cancellation, privacy, and reconstruction tests.

**Retained seed evidence.** All six original observability bullets remain retained beneath the expanded event model. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- Record which local sources were loaded and which were intentionally skipped.
- Record the exact verification command, reviewer question, or rendered artifact used as proof.
- Record p50/p95/p99 latency or reviewer-time measurements when the reference affects runtime or workflow speed.
- Capture tool-call count, context files loaded, delegated tasks, retry count, and completion-audit outcome.
- Record leading indicator and failure signal from this file in the coverage manifest or journal when the reference drives real work.
- Keep audit evidence small enough to review: command output summary, changed-file list, and unresolved-risk notes are preferred over raw transcript dumps.

## Performance Verification Method

**Decision supported.** This section helps decide how to determine whether a command improves a repeatable workflow within acceptable cost while preserving correctness, least privilege, and recovery. The seed requires tool and timeout budgets plus a resumable journal for long work, but it does not define stages, task cohorts, correctness, side-effect safety, cold installation, interaction wait, or external latency.

**Recommended default and causal basis.** Measure cold discovery, warm invocation, user-decision wait, tool and script execution, model processing, recovery, and total verified completion separately on matched task classes. One wall-clock number can punish deliberate confirmation, hide setup or external delay, and reward a fast but unsafe or incorrect command.

**Operating conditions and assumptions.** The protocol fixes command and plugin version, fixture, task, inputs, permissions, dependencies, start and stop events, expected effects, correctness rubric, failures, retries, and comparison baseline. Evaluate command workflow performance and separate called script, MCP server, or production service throughput into dedicated tests.

**Failure boundary and alternatives.** Manual wait is counted as tool latency without label, cached and cold runs mix, only successful runs remain, response time ends before effect verification, or tool-call reduction is assumed beneficial. Bounded alternatives and recoveries: measure time to first actionable result, reviewer effort, support interventions, approval prompts, context volume, or qualitative task completion until sample size supports percentiles.

**Counterexample, gotchas, and operational comparison.** Discovery cache, model and network variance, user familiarity, external service throttling, hidden parallel work, oversized outputs, and benchmarks that omit denial or cleanup branches. Good: compare a warm read-only review command with the same manual workflow and score evidence quality. Bad: call fewer tool calls faster. Borderline: report median completion for a small cohort while withholding tail and causal claims.

**Verification, evidence, and uncertainty.** Publish protocol, raw stage timings, cold or warm state, cohort and sample size, outcomes, permission and effect checks, failures, retries, external delays, baseline, summary calculation, and uncertainty. Testing guidance covers response time, resources, edge cases, invocation, and integration, while the seed defines budgets and resumability as the operational concern. No benchmark dataset or universal latency threshold accompanies the corpus, so acceptable budgets must be set by command risk and user need.

**Second-order consequence.** The meaningful unit is a verified workflow outcome; command speed that increases approval noise, context, or recovery cost is negative optimization.

**Revision decision.** Define staged measurement, matched cohorts, correctness and effect gates, cold-versus-warm runs, failure inclusion, low-sample alternatives, and transparent uncertainty.

**Retained seed evidence.** The tool-call budget, timeout budget, resumable journal, lifecycle indicator, measurement packet, and pass-fail statements remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Performance method: require tool-call budgets, timeout budgets, and a resumable journal when the workflow exceeds one focused session.
Leading indicator to measure: users can install, invoke, debug, and remove the extension without reading implementation code.
Failure signal to watch: the reference confuses adjacent extension types or omits failure recovery.
Required measurement packet: capture input size, source count, tool-call count, wall-clock time, p50/p95/p99 latency where runtime applies, and reviewer decision time where documentation applies.
Pass condition: the reference must let a reviewer identify the correct next action, verification gate, and stop condition without reading unrelated files.
Fail condition: the reference encourages implementation before the workload, reliability target, and failure-mode table are explicit.

## Scale Boundary Statement

**Decision supported.** This section helps decide when one command, one plugin command set, or one owner can no longer provide a coherent, safely testable interface. The seed stops at multiple systems, ownership boundaries, unbounded discovery, production traffic, parallel edits, context drift, and large codebases, but command scale also fails through namespace growth, shared state, integration fanout, and compatibility matrices.

**Recommended default and causal basis.** Split by user outcome and ownership, namespace discoverable command families, keep state local and versioned, isolate external integrations, centralize shared deterministic libraries, and require coordinated release and compatibility evidence. As commands multiply, duplicated prompt logic, broad permissions, collisions, inconsistent arguments, shared state, and platform combinations create system behavior that no single Markdown review can cover.

**Operating conditions and assumptions.** Each command has one owner and contract, shared components have tested interfaces, namespaces remain understandable, state and effects do not overlap silently, and release fixtures cover supported environments. Use this statement for plugin command architecture and ownership, not production-service capacity without explicit operational design.

**Failure boundary and alternatives.** An umbrella command dispatches unrelated systems, several commands write the same state, distributed agents edit one artifact, integration combinations grow unbounded, or marketplace claims exceed tested installations. Bounded alternatives and recoveries: split plugins by domain, expose a script or service API, use hooks for shared enforcement, federate MCP integrations, generate common documentation from one source, or narrow supported platforms and versions.

**Counterexample, gotchas, and operational comparison.** Name collisions across plugins, duplicated descriptions, inconsistent option semantics, cascading updates, old state schemas, cross-command recursive invocation, and support burden hidden by successful author tests. Good: namespace review commands and share a read-only script library with separate fixtures. Bad: `/manage-everything` spans deployments and repositories. Borderline: a multi-system release command requires explicit orchestration ownership, compensations, and integration SLOs.

**Verification, evidence, and uncertainty.** Inventory commands, names, owners, inputs, tools, resources, state files, effects, integrations, supported versions and platforms, shared components, collision tests, release order, and decommission plan. Local sources directly discuss namespacing, composition, state, plugin components, marketplace compatibility, and distribution tests; the seed already marks system and ownership limits. The corpus supplies no maximum command count, integration count, or marketplace scale benchmark.

**Second-order consequence.** Scale is primarily contract coordination: once two commands can mutate the same state or promise inconsistent semantics, adding more prompt detail cannot restore local reasoning.

**Revision decision.** Add namespace and portfolio boundaries, state and effect ownership, shared-library rules, integration isolation, compatibility matrices, release coordination, and decommission gates.

**Retained seed evidence.** The original system, ownership, distributed execution, context drift, and large-codebase boundaries remain retained. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Plugin Command Development Patterns stops being sufficient when the task spans multiple independent systems, more than one ownership boundary, unbounded source discovery, or production traffic without an explicit SLO.
Under distributed execution, split work by theme file and preserve one verification owner per split; do not let parallel agents rewrite the same reference without a merge checkpoint.
Under long-running agent workflows, treat context drift as a reliability failure: checkpoint state, summarize open risks, and verify against the spec before continuing.
Under large-codebase scale, require dependency or source-graph narrowing before applying this reference; a source list without ranked canonical guidance is not enough.

## Future Refresh Search Queries

**Decision supported.** This section helps decide when and how future maintainers should refresh command guidance without allowing search results to overwrite frozen archive evidence or local tests. The seed supplies generic official-docs, GitHub-example, and release-note queries but does not define drift triggers, version and feature qualifiers, authoritative-source ranking, or reconciliation with installed command behavior.

**Recommended default and causal basis.** Search only after a documented drift or compatibility trigger, include the exact Claude Code version and command feature, prefer official versioned sources, archive accepted evidence, reproduce behavior in a minimal plugin, and record the claim diff. Search locates candidate evidence rather than validating syntax or semantics; source acceptance and fixture reproduction prevent snippets, mirrors, or latest-version docs from silently changing a pinned contract.

**Operating conditions and assumptions.** The trigger names a disputed field or behavior, queries are narrow, source ownership and date are recorded, current and archived versions stay separate, and each accepted change updates tests and migration notes. Use future searches to discover command-specific updates and keep MCP or other extension results in their own evidence lanes.

**Failure boundary and alternatives.** Result snippets become facts, current docs are assumed backward compatible, community examples define permissions, absence of results proves removal, or routine browsing is called verification. Bounded alternatives and recoveries: inspect installed help and debug output, create a minimal command fixture, compare release artifacts or version tags, retain a provisional warning, or defer the feature when authoritative evidence is unavailable.

**Counterexample, gotchas, and operational comparison.** Similarly named command systems, unstable `latest` pages, old blog examples, repository branches without release tags, generated docs, search personalization, and MCP results crowding native command material. Good: after a field stops parsing, search its exact name and version, locate official release evidence, reproduce in a packaged fixture, and write migration guidance. Bad: copy a popular example. Borderline: retain a community workaround as labeled provisional evidence.

**Verification, evidence, and uncertainty.** Record trigger, exact query, retrieval date, source owner, product version, archived hash, relevant claim summary, fixture and outcome, conflicts, accepted change, migration impact, reviewer, and next refresh condition. The seed provides the three query categories and the local corpus repeatedly emphasizes frontmatter, discovery, plugin features, compatibility, and testing surfaces that can drift. No browsing was performed in this pass, so all query rows remain unexecuted maintenance prompts and support no freshness claim.

**Second-order consequence.** A useful refresh produces a versioned evidence diff and regression fixture, not merely a newer collection of links.

**Revision decision.** Retain the exact query rows and add drift triggers, version qualifiers, authority ranking, archive and diff steps, reproduction gates, migration handling, and rejection examples.

**Retained seed evidence.** The official documentation, GitHub repository, and release-note query labels and texts remain unchanged. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| search_query_label_name | search_query_text_value |
| --- | --- |
| `official_docs_query_phrase` | plugin command development patterns official documentation best practices |
| `github_repository_query_phrase` | plugin command development patterns GitHub repository examples |
| `release_notes_query_phrase` | plugin command development patterns changelog release notes migration |

## Evidence Boundary Notes

**Decision supported.** This section helps decide how every command-development claim should disclose what was read, observed, tested, inferred, or left uncertain. The seed distinguishes local, external, and combined evidence but does not separate duplicate files, archived documentation, current official material, installed parser observations, command fixture results, user reports, or design inference.

**Recommended default and causal basis.** Preserve the three seed labels and add duplicate-lineage, installed-product observation, command-test result, and provisional design hypothesis classes in use, with combined claims listing every prerequisite. Command behavior spans documentation, package loading, model instructions, permissions, filesystem effects, and external components; one evidence label cannot transfer certainty across all layers.

**Operating conditions and assumptions.** Atomic claims cite exact files or fixtures, duplicate sources count once, current observations name versions and environments, inferences state scope, negative evidence names tested coverage, and conflicts remain visible. Apply the taxonomy to this reference and downstream command packets while retaining exact seed labels for compatibility.

**Failure boundary and alternatives.** Labels decorate unsourced paragraphs, archived examples become current facts, one successful invocation proves portability, MCP evidence proves native metadata, or uncertainty is detached from the release decision. Bounded alternatives and recoveries: split a broad statement, downgrade it to a hypothesis, run a minimal current-version fixture, preserve contradictory results, narrow distribution scope, or decline a feature claim.

**Counterexample, gotchas, and operational comparison.** Documented does not mean parsed, parsed does not mean discovered, discovered does not mean safe, executed does not mean correct, and two identical paths do not provide independent support. Good: archive guidance motivates least privilege, parsed frontmatter confirms acceptance, invocation confirms denial behavior, and synthesis recommends release scope. Bad: infer current marketplace compatibility from an example. Borderline: report one-platform success with portability pending.

**Verification, evidence, and uncertainty.** Sample every recommendation, trace each clause to evidence class and location, confirm version and fixture identity, inspect duplicate handling, test combined prerequisites, review conflicts and negative evidence, and ensure uncertainty changes action. The fully read local corpus and duplicate hashes directly support the expanded taxonomy, while the seed supplies the durable three-label base. Even detailed labels cannot eliminate model variability or prove environments not tested, so scope and confidence remain judgment.

**Second-order consequence.** Confidence is compositional: reviewers should know which evidence link, if falsified, would change the command design, permission budget, or release scope.

**Revision decision.** Extend the three-label note with duplicate lineage, current observations, fixture evidence, claim ledgers, combination rules, conflict handling, and compositional confidence.

**Retained seed evidence.** The exact local-corpus, external-research, and combined-evidence definitions remain preserved verbatim at the section end. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- `local_corpus_sourced_fact`: statements tied directly to the local source paths above.
- `external_research_sourced_fact`: statements tied to the public URLs above.
- `combined_evidence_inference_note`: synthesis that combines local and public evidence into agent guidance.
