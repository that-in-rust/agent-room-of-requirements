# Plugin Structure Manifest Patterns

**Decision supported.** This section helps decide how to choose a Claude Code plugin directory structure, manifest fields, component paths, names, and lifecycle checks for the plugin's actual capabilities and distribution scope. The seed title does not yet define how a capability set should become a minimal plugin layout and manifest whose components are discoverable, portable, nonduplicated, versioned, and testable after packaging.

**Recommended default and causal basis.** Place the manifest at `.claude-plugin/plugin.json`, keep components at plugin root in conventional directories, create only used component types, rely on defaults, use relative manifest paths and plugin-root runtime references, and validate a packaged clean install. Discovery depends on exact package topology and parsed configuration, while portability and maintenance depend on avoiding cwd assumptions, duplicate registrations, unnecessary custom paths, and undocumented component ownership.

**Operating conditions and assumptions.** The plugin has one coherent purpose, conventional component boundaries fit, names are unique, every declared path exists, internal references survive relocation, and clean-install discovery can be observed. Use this reference for Claude Code plugin package structure and manifest decisions, not as current authoritative schema for unrelated extension ecosystems.

**Failure boundary and alternatives.** Components are nested under the manifest directory, custom paths duplicate defaults, absolute or parent paths leak local layout, names collide, manifest claims exceed packaged files, or archived field behavior is assumed current. Bounded alternatives and recoveries: remove unused fields, return to default directories, split independent capability domains into separate plugins, generate a combined hook file at build time, place deterministic shared logic in a library, or defer custom organization until scale requires it.

**Counterexample, gotchas, and operational comparison.** Valid JSON with invalid semantics, source-tree tests masking missing package files, plugin-root versus working-directory confusion, custom paths supplementing rather than replacing defaults, nested discovery assumptions, stale version metadata, and hidden component conflicts. Good: a skill-only plugin has one manifest and one `skills/<name>/SKILL.md`. Bad: all components live inside `.claude-plugin/` with local absolute paths. Borderline: categorized commands need custom paths only when each directory is packaged, conflict-tested, and documented.

**Verification, evidence, and uncertainty.** Parse JSON, validate name and path policy, inventory declared and default components, detect duplicate registrations and names, scan portable references, build the package, install into a clean profile, observe discovery and activation, test errors, update, disable, and remove. The three fully read local artifacts directly cover manifest location and fields, default and custom discovery, component organization, path portability, lifecycle, naming, and clean-install guidance. The corpus is archived and current Claude Code manifest schema or discovery behavior was not refreshed, so release claims require tests against the installed version.

**Second-order consequence.** The manifest is a capability index and trust boundary, not a directory catalog; every declaration expands what the host loads, starts, or exposes.

**Revision decision.** Add a capability-to-component matrix, minimal-manifest rule, path and duplication invariants, package lifecycle tests, conflict handling, scale alternatives, and archived-versus-current evidence labels.

**Retained seed evidence.** The exact title, six local source rows, and three external rows remain preserved as the frozen evidence base. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

## Source Evidence Mapping Table

**Decision supported.** This section helps decide which evidence can support manifest schema, package topology, component organization, lifecycle, or MCP-boundary claims without duplicate inflation. The seed presents six local paths that are three byte-identical archive and live-path pairs, plus three MCP rows that describe an adjacent integration model rather than native plugin manifest discovery.

**Recommended default and causal basis.** Treat the plugin-structure skill, component-patterns file, and manifest reference as three local evidence lineages; mark their paired paths duplicate; use MCP links only for the server component boundary. Copied files do not corroborate each other, and protocol-server documentation cannot establish native plugin manifest fields, path resolution, or discovery behavior.

**Operating conditions and assumptions.** Every claim names its source lineage and heading, separates archive guidance from installed observation, labels synthesis, and limits external evidence to its actual integration role. Apply this source model to the frozen nine rows and maintain installed tests as a separate evidence class.

**Failure boundary and alternatives.** Six paths become six votes, manifest examples are assumed current, MCP repositories define native package layout, or a source title substitutes for checking the relevant field and caveat. Bounded alternatives and recoveries: collapse duplicates, downgrade current-behavior claims, validate with a minimal installed plugin, omit irrelevant MCP analogies, or route server configuration to a dedicated MCP reference.

**Counterexample, gotchas, and operational comparison.** Future divergence between paired paths, examples being mistaken for exhaustive schema, source-count theater, external prestige, and an archive file silently treated as host runtime evidence. Good: cite manifest-reference for archived path rules and prove them in a fixture. Bad: cite the GitHub MCP server for `.claude-plugin/plugin.json`. Borderline: use MCP sources only to justify a separate `.mcp.json` component boundary.

**Verification, evidence, and uncertainty.** Hash paired files, build a claim-to-heading ledger, flag conflicts and unused rows, preserve external freshness status, and require current installed evidence for every discovery or parser claim. All three unique local files were read completely and each archive/live pair has identical bytes; the seed directly records all nine rows. Public MCP pages and current Claude Code behavior were not refreshed, so neither external nor archived rows prove present compatibility.

**Second-order consequence.** Lineage-aware mapping reduces both context and false certainty, leaving more review attention for the real difference between declared package shape and observed loading.

**Revision decision.** Add duplicate lineage, claim-relative authority, MCP adjacency limits, current-version handoff, conflict treatment, and a provenance ledger while retaining every row.

**Retained seed evidence.** All six local and three external rows remain exactly preserved below the expanded mapping rules. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| source_location_path_key | source_category_artifact_type | source_authority_confidence_level | source_usage_synthesis_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/plugin-structure/SKILL.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/plugin-structure/references/component-patterns.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/plugin-structure/references/manifest-reference.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| claude-skills/plugins/plugin-dev/plugin-structure/SKILL.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt |
| claude-skills/plugins/plugin-dev/plugin-structure/references/component-patterns.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| claude-skills/plugins/plugin-dev/plugin-structure/references/manifest-reference.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| https://modelcontextprotocol.io/specification/2025-06-18/server/resources | external_research_source_material | external_research_sourced_fact | primary MCP resource model for context sharing |
| https://github.com/modelcontextprotocol/servers | external_research_source_material | external_research_sourced_fact | reference and community server implementation index |
| https://github.com/github/github-mcp-server | external_research_source_material | external_research_sourced_fact | GitHub-backed MCP server for repository and issue operations |

## Pattern Scoreboard Ranking Table

**Decision supported.** This section helps decide how to order these safeguards during plugin structure work without interpreting the values as probabilities or observed reliability. The seed scores source-first, evidence-boundary, and verification-gate practices at 95, 91, and 88 without defining a measurement scale or manifest defect sample.

**Recommended default and causal basis.** Establish package and source truth first, separate archived facts from current tests and design inference second, and verify manifest parsing, component discovery, portability, conflicts, and lifecycle third; require every gate. Testing an assumed schema can institutionalize a stale layout, while accurate documentation without package installation evidence leaves discovery speculative.

**Operating conditions and assumptions.** The ordering guides attention, each row has observable pass criteria, urgent discovery failures may reorder execution, and final acceptance still requires all three. Retain the frozen numbers as editorial metadata, not probabilities, compatibility rates, service levels, or cross-reference comparisons.

**Failure boundary and alternatives.** 95 is called confidence, lower-ranked verification is skipped, score differences resolve conflicts, or a high aggregate impression hides missing packaged files or duplicate registration. Bounded alternatives and recoveries: replace numbers with prerequisites, use a risk matrix keyed to component lifecycle, prioritize clean-install reproduction for an active failure, or combine the rows into one release gate.

**Counterexample, gotchas, and operational comparison.** False precision, adoption tier confused with source authority, optimizing manifest prose instead of package behavior, and assuming local-first means current-version-correct. Good: inspect canonical layout, label version uncertainty, then install and enumerate components. Bad: call a plugin 95-percent compatible. Borderline: reproduce a not-loaded component first, then complete evidence and source gates.

**Verification, evidence, and uncertainty.** Sample plugin changes, record gate order, defects caught, rework prevented, justified reorderings, and whether all safeguards passed before distribution. The seed explicitly preserves three practices and targets, but the local corpus offers no calibrated scoring model. Impact varies with plugin size, component types, custom paths, host version, and distribution audience.

**Second-order consequence.** The scoreboard encodes prerequisite dependency: evidence makes the manifest hypothesis legible, and installation makes it falsifiable.

**Revision decision.** State the scale limit, turn each row into a package gate, add risk-based reorderings, and prohibit release while any safeguard remains red.

**Retained seed evidence.** The identifiers, 95, 91, 88 values, tiers, and exact prevention descriptions remain intact. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| pattern_identifier_stable_key | pattern_score_numeric_value | pattern_tier_adoption_level | pattern_failure_prevention_target |
| --- | ---: | --- | --- |
| `plugin_structure_manifest_patterns` | 95 | default_adoption_pattern_tier | Source Map First: Load local plugin structure material before synthesizing manifest patterns recommendations. |
| `plugin_structure_manifest_patterns` | 91 | default_adoption_pattern_tier | Evidence Boundary Split: Separate local facts, external facts, and inference before giving agent instructions. |
| `plugin_structure_manifest_patterns` | 88 | default_adoption_pattern_tier | Verification Gate Coupling: Attach each recommendation to at least one command, checklist, or review gate. |

## Idiomatic Thesis Synthesis Statement

**Decision supported.** This section helps decide what governing rule should control plugin topology and manifest evolution from first capability through distribution. The seed recommends local-first evidence and verification but does not state that plugin structure should follow capabilities and lifecycle, with the manifest kept minimal and observed package behavior outranking assumed discovery.

**Recommended default and causal basis.** Derive components from explicit capabilities, use conventional root directories and auto-discovery, declare only necessary metadata or custom paths, keep runtime references relocatable, and verify the built package in a clean host. Convention reduces configuration and duplicate loading, while package-level tests expose missing files, path assumptions, name conflicts, and lifecycle effects that source-tree review cannot.

**Operating conditions and assumptions.** Each component has a trigger and owner, defaults fit, custom paths solve a documented organization need, manifest and package agree, and install-to-remove behavior is reproducible. Apply the thesis to Claude Code plugin packages and keep MCP protocol claims or current host schema in their own evidence lanes.

**Failure boundary and alternatives.** The manifest becomes an aspirational catalog, nested folders are assumed discoverable, custom paths accumulate without conflict checks, or structural neatness is valued over actual host loading. Bounded alternatives and recoveries: simplify to one component type, use build-time generation for complex hook configuration, split independent plugin domains, externalize shared code to `lib`, or postpone marketplace metadata.

**Counterexample, gotchas, and operational comparison.** Valid JSON mistaken for valid host schema, default and custom paths both registering a component, source directories absent from package, plugin-root references used in the wrong context, and version changes without migration. Good: a command-plus-skill plugin uses default roots and a small manifest, then installs cleanly. Bad: declare every component path before files exist. Borderline: a modular plugin family uses custom paths only with package inventory, ownership, and conflict tests.

**Verification, evidence, and uncertainty.** Trace capability to component, manifest declaration, packaged path, discovery event, activation behavior, portable resource, disable result, update migration, and removal cleanup. The local skill and detail references consistently describe topology, manifest fields, component lifecycle, organization patterns, path resolution, and maintenance. Archived field lists and discovery descriptions may differ from the installed product and require direct fixture confirmation.

**Second-order consequence.** The best manifest minimizes the distance between declared capability and observable component; extra structure is debt unless it improves ownership or discovery.

**Revision decision.** Replace generic synthesis with capability derivation, minimal declaration, package-truth testing, lifecycle evidence, scale alternatives, and freshness limits.

**Retained seed evidence.** The local-first, external-context, and combined-inference statements remain preserved as the original thesis frame. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`local_corpus_sourced_fact`: The local row for `plugin_structure_manifest_patterns` contains 6 source path(s), which should be treated as the first retrieval surface for this theme.
`external_research_sourced_fact`: The external source map provides public documentation, repository, or ecosystem analogues where available.
`combined_evidence_inference_note`: Reliable use of Plugin Structure Manifest Patterns comes from loading the local corpus first, checking public ecosystem guidance second, and converting both into verification-backed agent decisions.

## Local Corpus Source Map

**Decision supported.** This section helps decide which unique local artifact should be read for the current plugin-structure decision and when additional source loading should stop. The seed lists the skill, component patterns, and manifest reference twice without explaining which source answers topology, field, lifecycle, organization, or scaling questions.

**Recommended default and causal basis.** Open the skill for baseline layout and portability, manifest-reference for field and path claims, and component-patterns for discovery lifecycle, organization, shared resources, and scaling. The three files divide policy, schema detail, and architectural organization; routing by question prevents examples from one layer being misused as guarantees in another.

**Operating conditions and assumptions.** The developer names the unresolved claim, opens one primary heading plus only necessary support, records duplicate lineage, and hands current behavior to an installed fixture. Route among the six frozen paths while preserving installed observations as separate evidence.

**Failure boundary and alternatives.** All six paths are loaded as separate context, component examples define manifest grammar, field tables dictate architecture, or a heading list substitutes for reading caveats. Bounded alternatives and recoveries: read only manifest-reference for a rejected field, only component patterns for organization pressure, only the skill for a minimal scaffold, or bypass archive guidance when reproducing a current host defect.

**Counterexample, gotchas, and operational comparison.** Duplicate bytes, examples with scale thresholds treated as universal, nested organization assumptions, and archive/live path labels confused with authority. Good: a custom command-path question uses manifest field detail plus lifecycle conflict testing. Bad: consult MCP links for name validation. Borderline: use component scaling guidance as a design heuristic while measuring actual reviewability.

**Verification, evidence, and uncertainty.** Record question class, selected file and heading, duplicate hash, skipped sources, claim extracted, fixture needed, observed result, and whether another source changed the decision. All three unique artifacts were fully read and their paired files have identical hashes. The map cannot prove current host behavior or future divergence between paired paths.

**Second-order consequence.** The source split mirrors design review: package skeleton, declarative manifest, and component architecture should be challenged independently.

**Revision decision.** Turn the source inventory into a question router with stop conditions, duplicate collapse, misuse examples, fixture handoff, and source-selection audit.

**Retained seed evidence.** All six paths, titles, heading signals, and usage roles remain exactly preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| local_source_filepath_value | local_source_title_text | local_source_heading_signals | local_source_usage_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/plugin-structure/SKILL.md | plugin-structure | Plugin Structure for Claude Code; Overview; Directory Structure; Plugin Manifest (plugin.json); Required Fields; Recommended Metadata | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/plugin-structure/references/component-patterns.md | Component Organization Patterns | Component Organization Patterns; Component Lifecycle; Discovery Phase; Activation Phase; Command Organization Patterns; Flat Structure | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/plugin-structure/references/manifest-reference.md | Plugin Manifest Reference | Plugin Manifest Reference; File Location; Complete Field Reference; Core Fields; Metadata Fields; Component Path Fields | reference detail file for deeper pattern evidence |
| claude-skills/plugins/plugin-dev/plugin-structure/SKILL.md | plugin-structure | Plugin Structure for Claude Code; Overview; Directory Structure; Plugin Manifest (plugin.json); Required Fields; Recommended Metadata | skill entrypoint or reusable agent prompt |
| claude-skills/plugins/plugin-dev/plugin-structure/references/component-patterns.md | Component Organization Patterns | Component Organization Patterns; Component Lifecycle; Discovery Phase; Activation Phase; Command Organization Patterns; Flat Structure | reference detail file for deeper pattern evidence |
| claude-skills/plugins/plugin-dev/plugin-structure/references/manifest-reference.md | Plugin Manifest Reference | Plugin Manifest Reference; File Location; Complete Field Reference; Core Fields; Metadata Fields; Component Path Fields | reference detail file for deeper pattern evidence |

## External Research Source Map

**Decision supported.** This section helps decide when external MCP evidence matters to plugin structure and where it must not influence native layout claims. The seed preserves three MCP sources that may inform the `.mcp.json` or `mcpServers` boundary but do not document native plugin manifests, root directories, or auto-discovery.

**Recommended default and causal basis.** Use MCP material only after selecting a server capability, to define that component's protocol and implementation context, while local plugin sources and installed tests govern package placement and declaration. MCP servers can be packaged components, but protocol resources and server repositories have separate schemas and lifecycles from the host plugin manifest.

**Operating conditions and assumptions.** The server requirement is explicit, native and MCP responsibilities are separated, configuration paths are packaged and portable, and integration tests cover startup, absence, permission, and shutdown. Retain these rows as adjacent MCP context, not current native plugin-manifest documentation.

**Failure boundary and alternatives.** MCP specification text is cited for plugin name or path rules, a server repository layout becomes a universal plugin example, or external freshness is inferred without browsing. Bounded alternatives and recoveries: omit an MCP component, call a local deterministic script, route server implementation to an MCP reference, or postpone external integration until ownership and lifecycle are defined.

**Counterexample, gotchas, and operational comparison.** Inline and file configuration drift, server process startup hidden during discovery, environment secrets, platform executables, and plugin removal leaving processes or state. Good: native manifest points to a packaged `.mcp.json`, then MCP tests validate the server. Bad: use MCP resources to define `.claude-plugin/plugin.json`. Borderline: list MCP as a future component while clearly withholding compatibility claims.

**Verification, evidence, and uncertainty.** Map each external claim to its URL and boundary, record refresh status, require native evidence for manifest behavior, and test packaged server configuration plus failure cleanup. The seed accurately identifies the three MCP roles, and local sources explicitly place MCP configuration as one plugin component. The public pages were not refreshed, so specification and repository currency remain unknown.

**Second-order consequence.** External evidence helps define a component seam, but seam clarity depends on refusing to transfer protocol authority into package-schema claims.

**Revision decision.** Add native-versus-MCP responsibility, startup and cleanup boundaries, freshness labels, composition tests, and rejection examples while preserving every URL.

**Retained seed evidence.** The three MCP rows and external evidence labels remain exactly intact. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| external_source_url_value | external_source_name_text | external_source_usage_role | evidence_boundary_label_value |
| --- | --- | --- | --- |
| https://modelcontextprotocol.io/specification/2025-06-18/server/resources | Model Context Protocol resources | primary MCP resource model for context sharing | external_research_sourced_fact |
| https://github.com/modelcontextprotocol/servers | MCP server implementations | reference and community server implementation index | external_research_sourced_fact |
| https://github.com/github/github-mcp-server | GitHub MCP server | GitHub-backed MCP server for repository and issue operations | external_research_sourced_fact |

## Anti Pattern Registry Table

**Decision supported.** This section helps decide which structural or manifest signature should block packaging and what safer topology or declaration should replace it. The seed lists generic source and verification failures but omits plugin defects such as misplaced manifests, components under `.claude-plugin`, duplicate default and custom discovery, local paths, missing package files, collisions, and aspirational declarations.

**Recommended default and causal basis.** Reject wrong manifest placement, root-component violations, invalid or stale fields, absolute or parent paths, duplicate registrations, missing targets, undeclared capabilities, name collisions, embedded secrets, and source-only validation. These defects alter what the host can discover, start, or expose and often remain invisible until the plugin is relocated or installed with other plugins.

**Operating conditions and assumptions.** Each anti-pattern has a static detector, clean-install symptom, consequence, bounded correction, and regression fixture. Apply the registry to plugin package topology and route component-internal correctness to its specific reference.

**Failure boundary and alternatives.** Valid JSON is considered sufficient, warnings are fixed only in README text, custom paths are added to work around package omissions, or broader declarations replace root-cause diagnosis. Bounded alternatives and recoveries: restore conventional roots, remove redundant custom paths, package missing files, rename components, generate complex configuration at build time, split plugins, or eliminate unused component types.

**Counterexample, gotchas, and operational comparison.** Default-plus-custom double registration, nested commands assumed recursive, symlinks or casing differing by platform, plugin-root references evaluated in the wrong layer, secrets committed in environment blocks, and updates stranding old names. Good: a package audit catches an absent hook script before install. Bad: fix discovery with an absolute developer path. Borderline: custom categorized directories are safe only with existence, uniqueness, portability, and lifecycle tests.

**Verification, evidence, and uncertainty.** Lint JSON structurally and semantically, inventory package paths, compare defaults and declarations, scan for forbidden paths and secrets, install beside collision fixtures, enumerate components, activate each type, disable, update, and remove. The local sources directly define required placement, root components, path rules, merge behavior, naming, lifecycle, and troubleshooting. Current host validation and nested-discovery behavior may differ from archived prose, requiring direct observation.

**Second-order consequence.** Manifest anti-patterns are load-graph defects: one bad declaration can omit, duplicate, or unexpectedly activate capabilities before user intent is involved.

**Revision decision.** Retain the three generic rows and add package-level signatures, security implications, static detectors, clean-install symptoms, safe replacements, and regression gates.

**Retained seed evidence.** Context-free summary, unsourced recommendation, and unverified instruction remain preserved as umbrella failures. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| anti_pattern_failure_name | failure_cause_risk_reason | safer_default_replacement_pattern | detection_signal_review_method |
| --- | --- | --- | --- |
| context_free_summary_output | agent skips local corpus and produces generic advice | source_map_first_synthesis | verify every listed local path appears in the generated file |
| unsourced_recommendation_claims | guidance appears authoritative without source boundary | evidence_boundary_split_pattern | check for local, external, and inference labels |
| unverified_agent_instruction | recommendation cannot be checked by command or review gate | verification_gate_coupling | require concrete gate in generated reference |

## Verification Gate Command Set

**Decision supported.** This section helps decide which independent gates prove the evolved reference and a concrete plugin manifest or layout are structurally and operationally sound. The seed supplies only a generated-reference verifier, while plugin acceptance also needs JSON parsing, current schema validation, package inventory, path checks, conflict detection, clean installation, component activation, update, disable, and removal evidence.

**Recommended default and causal basis.** Run the focused reference validator, parse and semantically validate the manifest, compare declarations to package files and defaults, scan portability and secrets, then install a built artifact in a clean host and exercise every component lifecycle. Reference integrity cannot prove a package, and source-tree linting cannot prove discovery, process startup, name conflicts, or cleanup after relocation.

**Operating conditions and assumptions.** Each claim maps to a capable gate, fixtures use the packaged artifact and pinned host version, negative cases are intentional, and failures identify parse, package, discovery, activation, or lifecycle layers. Keep reference QA, package QA, and component behavior QA as separate evidence layers.

**Failure boundary and alternatives.** Delimiter or grep checks replace JSON parsing, installation uses the source folder, only one component is invoked, custom paths are not collision-tested, or uninstall is assumed clean. Bounded alternatives and recoveries: repair the reference separately, minimize the manifest, generate package inventories, isolate component fixtures, test a local plugin before marketplace packaging, or withhold unsupported compatibility claims.

**Counterexample, gotchas, and operational comparison.** Cached plugin discovery, inherited user configuration, platform path differences, background MCP processes, hook side effects during fixtures, and version metadata not matching the built artifact. Good: validate JSON and package contents, clean-install, enumerate, activate, deny malformed paths, update, disable, and remove. Bad: run only the archive verifier. Borderline: static gates certify a draft but cannot support runtime discovery claims.

**Verification, evidence, and uncertainty.** Capture exact commands, host and package versions, artifact hash, parsed fields, inventory diff, path and secret scan, collision fixture, discovery output, component activation results, process and file effects, update migration, and removal residue. Manifest-reference covers validation and fields, component-patterns covers discovery and activation, and the skill covers structure, portability, and troubleshooting. No sample plugin artifact is provided in this evolution task, so package gates remain procedures rather than observed product passes.

**Second-order consequence.** Verification should follow the loader's causal sequence: parse, resolve, discover, register, initialize, activate, deactivate, and remove.

**Revision decision.** Add structured and semantic validation, package inventory, portability and secret scans, clean-host lifecycle matrix, evidence packet, and focused validator while retaining the seed command.

**Retained seed evidence.** The original final-stage reference-generation command remains preserved as historical artifact evidence. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`verification_gate_command_set`: Run the repository verifier after editing this file.

```bash
python3 agents-used-monthly-archive/idiomatic-references-202606/tools/verify_reference_generation.py --stage final
```

## Agent Usage Decision Guide

**Decision supported.** This section helps decide whether this structure reference is the right tool and which package decision should be made before opening component-specific guidance. The seed activates on theme mentions but does not help decide whether the task concerns plugin scaffold, manifest fields, component organization, component internals, MCP integration, marketplace packaging, or a non-plugin extension.

**Recommended default and causal basis.** Classify the capability set, audience, component types, discovery defaults, custom organization need, portability boundary, lifecycle risk, and distribution scope; then choose the smallest conventional scaffold. Early package classification prevents the manifest from absorbing component behavior and prevents component authors from inventing incompatible package topology.

**Operating conditions and assumptions.** The task requires a plugin package, components and triggers are identifiable, default roots are feasible, ownership is clear, and clean-install verification is possible. Activate for Claude Code plugin package and manifest design, not generic repository organization or standalone component implementation.

**Failure boundary and alternatives.** The user only needs one command or skill outside a plugin, the issue is internal component behavior, an external protocol dominates, or no package lifecycle can be tested. Bounded alternatives and recoveries: route to command, agent, skill, hook, MCP, settings, marketplace, or component-development guidance; use a project-local artifact before packaging when distribution is premature.

**Counterexample, gotchas, and operational comparison.** Assuming every capability needs a manifest entry, creating empty directories, selecting custom paths for aesthetics, mixing component naming with plugin naming, and treating structure as a substitute for behavior design. Good: a plugin with one command and one skill uses conventional roots and component-specific follow-up. Bad: scaffold all component directories for a settings change. Borderline: a plugin family needs custom paths only after ownership and conflict analysis.

**Verification, evidence, and uncertainty.** Record capability inventory, trigger and component mapping, chosen audience, default-versus-custom decision, manifest fields, package paths, ownership, rejected surfaces, lifecycle tests, and stop condition. The local skill gives the baseline capability map and both references cover field and organization decisions in detail. Current host support and project constraints can alter the feasible scaffold despite archive recommendations.

**Second-order consequence.** Structure guidance should terminate as soon as package boundaries are explicit; deeper command, hook, agent, skill, or server behavior belongs to its owner.

**Revision decision.** Replace keyword routing with a package decision tree, capability matrix, minimal-scaffold ladder, component handoffs, and activation audit.

**Retained seed evidence.** The local-first, explicit-gate, external-check, and evidence-label bullets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`agent_usage_decision_guide`: Use this reference when a task mentions this theme, one of the listed local source paths, or a nearby technology/workflow surface.

- Start with the local corpus source map.
- Prefer patterns with explicit verification gates.
- Treat external sources as freshness and ecosystem checks, not replacements for local repo conventions.
- Preserve the evidence boundary labels when reusing recommendations.

## User Journey Scenario

**Decision supported.** This section helps decide how a builder should move from a capability request to a package an unfamiliar user can install, inspect, use, troubleshoot, update, and remove. The seed identifies a platform builder selecting an extension surface but does not trace plugin capabilities into a manifest, package tree, clean installation, component activation, update, diagnosis, disable, and removal.

**Recommended default and causal basis.** Inventory capabilities and triggers, map only needed components, scaffold conventional roots, write a minimal manifest, add portable resources, build an exact package, validate in a clean host, document lifecycle, and test update and removal. The sequence exposes wrong-surface and missing-package errors before distribution and gives every declared capability a traceable path to observable host behavior.

**Operating conditions and assumptions.** The builder controls a disposable profile, can name supported components and effects, packages deterministic files, and can reproduce discovery without personal configuration. Use this scenario for plugin packaging and route each component's internal behavior to dedicated guidance.

**Failure boundary and alternatives.** The plugin purpose is incoherent, component ownership is shared implicitly, the package cannot be isolated, required secrets are embedded, or lifecycle effects cannot be inventoried. Bounded alternatives and recoveries: start with one project-local component, split independent capabilities, defer optional MCP or hooks, generate complex config at build time, or route non-package work to a component reference.

**Counterexample, gotchas, and operational comparison.** Scaffolding empty directories, authoring from installed state, forgetting package excludes, metadata drifting from features, custom paths hiding omissions, and treating first activation as journey completion. Good: a skill-focused package installs, activates on a fixture task, updates with migration notes, disables cleanly, and removes without residue. Bad: distribute the source tree with local symlinks. Borderline: a full plugin is acceptable only with per-component lifecycle and ownership evidence.

**Verification, evidence, and uncertainty.** Preserve capability inventory, component map, manifest parse, package file list and hash, clean install, discovery inventory, activation cases, effects, diagnostics, update path, disable result, removal residue, and user documentation review. The local corpus covers the entire package lifecycle and multiple minimal, full, skill-focused, and scaled organization examples. Current marketplace or host procedures may differ from the archived source and must be observed in the target environment.

**Second-order consequence.** The package journey is a bidirectional trace: every capability must reach a component, and every packaged component must justify a capability.

**Revision decision.** Replace the generic role statement with a capability-to-package lifecycle, checkpoints, failure exits, evidence packet, and good, bad, and borderline package outcomes.

**Retained seed evidence.** The platform-builder role, extension choice, lifecycle proof goal, and opening trigger remain retained. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Role based opening scenario: The agent-tool platform builder is starting from a capability request that could become a command, hook, plugin, MCP server, or setting and needs a reference that turns source evidence into an executable next step.
Primary user starting state: The user has a `plugin_structure_manifest_patterns` task, one or more local source paths, and uncertainty about which pattern should drive implementation.
Decision being made: choosing the right extension surface and proving install, invocation, permissions, and recovery behavior.
Reference opening trigger: Open this file when the task mentions plugin structure manifest patterns, any mapped local source path, or an adjacent workflow with the same failure mode.

## Decision Tradeoff Guide

**Decision supported.** This section helps decide whether to adopt conventional structure, adapt it for scale, avoid a plugin package, or split responsibilities across packages and components. The seed bases adopt, adapt, and avoid on source agreement but omits practical choices among default and custom paths, minimal and rich metadata, one plugin and split packages, inline and file configuration, or flat and categorized components.

**Recommended default and causal basis.** Adopt defaults for small coherent plugins, adapt only for measurable organization or ownership pressure, split independent lifecycle domains, and avoid packaging when one local component or external service configuration suffices. Custom structure can improve ownership and discovery at scale but increases manifest surface, duplicate-registration risk, package testing, migration, and user support.

**Operating conditions and assumptions.** The decision compares capability cohesion, component count and types, permission domains, release cadence, ownership, package audience, custom-path benefit, and compatibility evidence. Decide per package and capability domain, not by applying one layout to every plugin in a marketplace.

**Failure boundary and alternatives.** Agreement between archive and external links substitutes for package need, adaptation works around an invalid manifest, avoid offers no route, or a full-featured example drives premature scaffolding. Bounded alternatives and recoveries: use default roots, add one custom path, generate configuration, share a library, create a plugin family, keep a project-local artifact, or expose an MCP server independently.

**Counterexample, gotchas, and operational comparison.** Custom paths supplementing defaults, inline hooks becoming unreviewable, split plugins introducing version coordination, rich metadata becoming stale, and categorized folders exceeding user discoverability. Good: adopt a minimal skill plugin; adapt commands into two owned custom roots after conflicts are tested; avoid a plugin for one temporary project file. Bad: mirror every example directory. Borderline: split a plugin only when independent release and permission boundaries outweigh coordination cost.

**Verification, evidence, and uncertainty.** Write a decision record with capabilities, default fit, custom-path delta, package split criteria, ownership, release coupling, metadata need, migration cost, alternatives, wrong-choice consequences, and test gates. The corpus directly describes minimal, complete, custom-path, nested, shared-resource, layered, and plugin-family patterns. The source provides illustrative count thresholds rather than measured universal breakpoints.

**Second-order consequence.** Custom structure should purchase a specific property such as ownership or permission separation; aesthetics alone cannot repay the additional loader and migration contracts.

**Revision decision.** Reframe the four seed options around defaults, custom paths, package splitting, inline configuration, metadata depth, lifecycle cost, and reversible alternatives.

**Retained seed evidence.** Adopt when, Adapt when, Avoid when, and Cost of being wrong remain exactly preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| decision_option_name | when_to_choose_condition | tradeoff_cost_description | verification_question_prompt |
| --- | --- | --- | --- |
| Adopt when | local corpus and external evidence agree on the plugin structure manifest patterns pattern | fastest path, but can copy stale local assumptions | Does the selected pattern appear in the canonical source and current external evidence? |
| Adapt when | local sources are strong but public ecosystem guidance has changed | preserves repo fit, but requires explicit inference notes | Did the reference label the local fact, external fact, and combined inference separately? |
| Avoid when | source evidence is thin, conflicting, or unrelated to the user journey | prevents false confidence, but may require deeper research | Is there a confidence warning or adjacent reference route? |
| Cost of being wrong | wrong plugin structure manifest patterns guidance can send an agent to the wrong files, tests, or abstraction | wasted implementation loop and weaker verification | Would a reviewer know what to undo and what to inspect next? |

## Local Corpus Hierarchy

**Decision supported.** This section helps decide which evidence controls when conceptual layout, field reference, organization example, duplicate copy, current parser, package inventory, and discovery behavior disagree. The seed labels the archived skill canonical, two details supporting, and three identical live paths supporting, but does not define conflict resolution with package contents or current host observations.

**Recommended default and causal basis.** Use the skill for archived baseline conventions, manifest-reference for archived field intent, component-patterns for organization heuristics, hashes to collapse duplicates, current parsing for schema facts, and clean installs for lifecycle facts. Authority follows claim capability: prose can guide design, while only packaged files and host observations can establish what was shipped and loaded.

**Operating conditions and assumptions.** The disputed claim is classified, relevant authorities are compared, versions and hashes are retained, conflicts stay visible, and guidance changes without altering frozen source roles. Preserve the six frozen roles while layering duplicate lineage, package facts, and current observations separately.

**Failure boundary and alternatives.** Canonical means universally current, duplicate paths count as consensus, examples override field validation, package success excuses incoherent design, or one clean install proves every platform. Bounded alternatives and recoveries: downgrade the claim, reproduce with a minimal fixture, inspect current official schema when allowed, preserve both interpretations, simplify the manifest, or block release.

**Counterexample, gotchas, and operational comparison.** Paired paths diverging later, host caches, package build transforms, symlinks, platform casing, default configuration inherited from the test profile, and field behavior changing by version. Good: archive docs motivate a relative custom path, package inventory proves it exists, and current host proves loading. Bad: two identical files prove support. Borderline: observed behavior differs; use it operationally while recording versioned archive drift.

**Verification, evidence, and uncertainty.** Maintain a conflict ledger with claim class, paths and hashes, host version, package artifact, fixture, result, chosen authority, design impact, migration action, and unresolved scope. Local roles, hashes, and lifecycle distinctions are directly known from the fully read corpus. Without refreshed product docs, observed differences may reflect environment, version, packaging, or archive error.

**Second-order consequence.** Hierarchy is a claim router rather than a prestige list; design guidance and runtime truth can coexist without being interchangeable.

**Revision decision.** Add claim-relative precedence, duplicate collapse, package and host evidence, conflict handling, scope limits, and refresh obligations.

**Retained seed evidence.** All six hierarchy rows and their canonical or supporting roles remain unchanged. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Classification vocabulary includes canonical, supporting, legacy, duplicate, and conflicting source roles.

| local_source_filepath_value | corpus_hierarchy_role | heading_signal_to_convert | reviewer_question_to_answer |
| --- | --- | --- | --- |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/plugin-structure/SKILL.md | canonical primary source | Plugin Structure for Claude Code; Overview; Directory Structure | What guidance, warning, or example should this source contribute to Plugin Structure Manifest Patterns? |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/plugin-structure/references/component-patterns.md | supporting detail source | Component Organization Patterns; Component Lifecycle; Discovery Phase | What guidance, warning, or example should this source contribute to Plugin Structure Manifest Patterns? |
| agents-used-monthly-archive/claude-skills-202603/plugins/plugin-dev/plugin-structure/references/manifest-reference.md | supporting detail source | Plugin Manifest Reference; File Location; Complete Field Reference | What guidance, warning, or example should this source contribute to Plugin Structure Manifest Patterns? |
| claude-skills/plugins/plugin-dev/plugin-structure/SKILL.md | supporting context source | Plugin Structure for Claude Code; Overview; Directory Structure | What guidance, warning, or example should this source contribute to Plugin Structure Manifest Patterns? |
| claude-skills/plugins/plugin-dev/plugin-structure/references/component-patterns.md | supporting detail source | Component Organization Patterns; Component Lifecycle; Discovery Phase | What guidance, warning, or example should this source contribute to Plugin Structure Manifest Patterns? |
| claude-skills/plugins/plugin-dev/plugin-structure/references/manifest-reference.md | supporting detail source | Plugin Manifest Reference; File Location; Complete Field Reference | What guidance, warning, or example should this source contribute to Plugin Structure Manifest Patterns? |

## Theme Specific Artifact

**Decision supported.** This section helps decide what matrix must be completed before a plugin package can claim compatibility for a host, platform, installation method, and component set. The seed requests a manifest compatibility matrix with install validation and failure examples, but its three generic rows omit host versions, package inventory, fields, paths, components, discovery, activation, effects, update, and removal.

**Recommended default and causal basis.** Record package hash, plugin and host versions, platform, install method, manifest fields, default and custom paths, packaged files, expected components, discovery and activation results, dependencies, effects, diagnostics, update migration, disable, and removal. Compatibility is a relation among one artifact, one host, one environment, and one claim; a manifest alone cannot establish that relation.

**Operating conditions and assumptions.** Each matrix cell has a fixture and pass condition, unsupported combinations are explicit, failures preserve diagnostics, and every component maps to both package files and observed lifecycle. Require the full matrix for distribution and allow a small single-environment record for explicitly local plugins.

**Failure boundary and alternatives.** The matrix lists aspirational checkmarks, reuses one source-tree run across platforms, omits negative cases, treats parse success as activation, or ignores processes and state after removal. Bounded alternatives and recoveries: publish a narrower support matrix, split optional components, defer custom paths, provide a migration guide, or keep the plugin local until clean-host evidence exists.

**Counterexample, gotchas, and operational comparison.** Package hashes changing between tests, host caches, platform path casing, missing executable permissions, environment secrets, default and custom duplicates, and version metadata differing from the artifact. Good: a skill-only package matrix proves two supported host fixtures and clean removal. Bad: a complete manifest marked universal after local parsing. Borderline: one-platform beta is acceptable when scope and unsupported cells are explicit.

**Verification, evidence, and uncertainty.** Rebuild from a clean checkout, hash and inventory the artifact, run every supported cell, enumerate discoveries, invoke components, capture effects and logs, exercise malformed and collision fixtures, update, disable, remove, and inspect residue. The seed names the matrix, and local sources directly define manifest, component, portability, validation, distribution, and lifecycle dimensions. Current host and marketplace combinations were not supplied, so the reference defines the matrix rather than filling compatibility claims.

**Second-order consequence.** The matrix turns compatibility from a plugin adjective into a versioned evidence set that can shrink or expand without ambiguity.

**Revision decision.** Expand the three fields into an artifact-host matrix, inventory and lifecycle evidence, failure cells, migration and removal checks, and support-scope rules.

**Retained seed evidence.** User goal, decision boundary, and verification gate remain preserved as the matrix's core rows. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Theme specific artifact: manifest compatibility matrix with install validation and failure examples.

| artifact_field_name | artifact_completion_rule | evidence_source_hint |
| --- | --- | --- |
| user_goal_statement | state the user's concrete goal before applying Plugin Structure Manifest Patterns | local corpus hierarchy plus critique findings |
| decision_boundary_rule | define the point where this reference should be used or avoided | decision tradeoff guide |
| verification_gate_rule | define the command, checklist, or review question that proves the artifact worked | verification gate command set |

## Worked Example Set

**Decision supported.** This section helps decide what observable package and host behavior distinguishes a sound minimal plugin, a structurally broken plugin, and a conditionally justified complex layout. The seed offers only generic evidence-loading contrasts and does not show how package topology, manifest declarations, custom paths, duplicate discovery, or lifecycle evidence change a verdict.

**Recommended default and causal basis.** Judge examples by capability fit, conventional placement, manifest-package agreement, path portability, unique discovery, component activation, ownership, and clean lifecycle. Directory trees can look plausible while placing files outside the loader's model or packaging declarations that duplicate, omit, or overactivate components.

**Operating conditions and assumptions.** The good case proves minimal behavior, the bad case exposes a realistic load failure and consequence, and the borderline case names every extra condition needed for acceptance. Use examples as decision calibration, not copy-ready current schemas.

**Failure boundary and alternatives.** Examples differ only by folder count, the broken case is implausible, the good case assumes package inclusion, or the complex case is approved without update and conflict tests. Bounded alternatives and recoveries: illustrate a skill-only plugin, categorized command roots, external hook file, MCP component, shared library, or split plugin family depending on the decision.

**Counterexample, gotchas, and operational comparison.** Empty default directories alongside custom paths, nested commands without explicit loading, source-relative scripts, inline secrets, and stale names after a split. Good: one manifest and one conventional skill directory install and activate cleanly. Bad: commands sit under `.claude-plugin` and reference an absolute script. Borderline: categorized command roots are valid only when each path is packaged, unique, owned, migrated, and tested.

**Verification, evidence, and uncertainty.** For each example, enumerate capabilities, tree, manifest fields, package contents, expected and actual discovery, activation, portability, conflicts, effects, update behavior, cleanup, and reviewer decision. Minimal, full, skill-focused, categorized, hierarchical, shared-resource, and plugin-family patterns are directly represented in the local corpus. The examples are reasoned package shapes rather than executions on a supplied host.

**Second-order consequence.** Borderline structure is acceptable when complexity purchases explicit ownership or compatibility and every added loader edge has a test.

**Revision decision.** Replace generic source contrasts with minimal, misplaced, and custom-layout packages that expose causal failures, safeguards, verification, and recovery.

**Retained seed evidence.** The original good, bad, and borderline source-boundary statements remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Good example: Use Plugin Structure Manifest Patterns after loading the canonical source, confirming the external evidence boundary, and writing a verification gate before implementation.
Bad example: Use Plugin Structure Manifest Patterns as a generic tutorial while ignoring the mapped local paths, source hierarchy, and cost of being wrong.
Borderline case: Use Plugin Structure Manifest Patterns only after adding a confidence warning when local evidence is thin or conflicts with current ecosystem guidance.

## Outcome Metrics and Feedback Loops

**Decision supported.** This section helps decide which signals show that structure and manifest choices make the plugin discoverable, portable, diagnosable, maintainable, and removable. The seed values install, invoke, debug, and remove without implementation reading and flags extension confusion, but it does not define package-specific indicators or feedback actions.

**Recommended default and causal basis.** Track clean-install success, expected-versus-observed component inventory, duplicate and collision detections, activation failures, missing package paths, relocation success, update migrations, support-free diagnosis, and removal residue. File count and parse success say little about the user's lifecycle, while inventory mismatches and residual effects directly reveal structural defects.

**Operating conditions and assumptions.** Metrics name artifact and host versions, fixture, denominator, expected set, observed set, adverse threshold, owner, and the manifest, package, or documentation change triggered. Measure package and manifest quality, not internal component usefulness or external server reliability without dedicated controls.

**Failure boundary and alternatives.** Author installations dominate the sample, successful components hide missing ones, unsupported platforms are excluded silently, caches mask discovery, or uninstall success ignores spawned processes and project files. Bounded alternatives and recoveries: use qualitative clean-install walkthroughs at low volume, track only inventory diffs before release, sample complex components separately, or narrow supported environments.

**Counterexample, gotchas, and operational comparison.** Duplicate copies counted as separate evidence, multiple failures from one missing file double-counted, host updates changing baselines, and package build systems rewriting permissions. Good: record zero unexpected components and one missing-path regression caught before release. Bad: claim health from download count. Borderline: report high clean-install success while separately retaining update and removal uncertainty.

**Verification, evidence, and uncertainty.** Publish metric definitions, package hashes, host cohorts, raw expected and observed inventories, failures, cache controls, migrations, cleanup checks, exclusions, uncertainty, and feedback trace. The lifecycle and validation corpus directly exposes all proposed metrics, and the seed supplies the user-self-service objective. No package telemetry or compatibility dataset is provided, so thresholds and causal improvement remain local.

**Second-order consequence.** Unexpected discovery deserves equal attention to missing discovery because an extra hook or server can expand behavior and trust without user intent.

**Revision decision.** Operationalize discovery, duplication, portability, diagnosis, update, and removal indicators with denominators, version cohorts, owners, and learning actions.

**Retained seed evidence.** The install-invoke-debug-remove indicator, extension-confusion signal, and verifier-refresh cadence remain retained. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Leading indicator: users can install, invoke, debug, and remove the extension without reading implementation code.
Failure signal: the reference confuses adjacent extension types or omits failure recovery.
Review cadence: Re-run the verifier after every generated-reference edit and refresh external sources when public APIs, docs, or tooling releases change.

## Completeness Checklist

**Decision supported.** This section helps decide what evidence must exist before a plugin structure reference or package can be called complete for its claimed support scope. The seed checks role, options, hierarchy, artifact, examples, metrics, and routing but omits capability coverage, exact package inventory, manifest semantics, default and custom path conflicts, portability, component lifecycle, updates, and removal.

**Recommended default and causal basis.** Require the seven seed categories plus capability-to-component mapping, minimal manifest rationale, JSON and current-schema validation, package inventory, unique path resolution, portable references, clean discovery and activation, failure diagnostics, migration, disable, and removal. A package may satisfy prose completeness while omitting a component, loading an unexpected one, failing after relocation, or leaving processes and state behind.

**Operating conditions and assumptions.** Every checkbox links to a file, parsed value, inventory result, fixture observation, or lifecycle outcome, and nonapplicable component gates include rationale. Apply full gates to distributed plugins and document justified reductions for local single-purpose packages.

**Failure boundary and alternatives.** Checkmarks lack evidence, one successful install covers all components, source-tree presence proves package inclusion, or supported platform and version cells are left implicit. Bounded alternatives and recoveries: use a reduced checklist for a local single-component plugin, add server and hook lifecycle gates when present, narrow the compatibility matrix, or route component internals elsewhere.

**Counterexample, gotchas, and operational comparison.** Package excludes, generated files, duplicate default/custom scans, inherited configuration, stale version fields, background initialization, and removal that leaves user-created versus plugin-created state ambiguous. Good: every declared and default component maps to packaged bytes and observed lifecycle. Bad: complete because `plugin.json` parses. Borderline: a local skill plugin may omit distribution metadata while explicitly limiting scope.

**Verification, evidence, and uncertainty.** Audit all items against capability map, manifest parse, package hash and list, path graph, discovery set, activation cases, effects, diagnostics, version cells, migration, disable, and residue. The local corpus directly supports every added package and lifecycle gate, while the seed retains reference-level categories. Organization policy and current marketplace requirements may add signing, privacy, provenance, or accessibility checks.

**Second-order consequence.** Package completeness is bidirectional equality between intended capabilities and observed components: neither omissions nor extras are acceptable without explanation.

**Revision decision.** Extend seed categories with evidence pointers, package graph invariants, compatibility cells, component lifecycle, migration, and final clean-host replay.

**Retained seed evidence.** All seven original checklist bullets remain unchanged. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- The role scenario names the user, starting state, decision, and trigger for Plugin Structure Manifest Patterns.
- The decision guide includes Adopt when, Adapt when, Avoid when, and Cost of being wrong.
- The local corpus hierarchy identifies canonical and supporting sources or gives a confidence warning.
- The theme specific artifact is concrete enough to review without reading every mapped source.
- The examples cover good, bad, and borderline usage.
- The metrics section names one leading indicator and one failure signal.
- The adjacent routing section points to a better reference when this one is not the right fit.

## Adjacent Reference Routing

**Decision supported.** This section helps decide where to route once package topology is settled and the unresolved work concerns a specific component, distribution process, security property, or external integration. The seed names command, hook, MCP, settings, manifest, plugin, structure, and development references but does not define the capability boundary or handoff evidence for each.

**Recommended default and causal basis.** Stay here for package layout and manifest; route command, agent, skill, hook, MCP, settings, marketplace, script, testing, or security questions to the owner of that component or lifecycle. Structure determines what loads, while component references determine what loaded capabilities do; mixing the two hides distinct schemas, permissions, and failure modes.

**Operating conditions and assumptions.** The unresolved claim is explicit, the destination can answer it, package context travels in a minimal handoff, and returned evidence updates only relevant manifest or lifecycle decisions. Route after package responsibility is clear and keep manifest ownership with the package maintainer.

**Failure boundary and alternatives.** Routing follows a similar noun, component behavior remains undocumented because the manifest declares it, several adjacent references load at once, or returned guidance silently adds capabilities. Bounded alternatives and recoveries: retain a thin package decision here, use a project-local component before plugin distribution, split plugin ownership, or decline a component whose lifecycle cannot be tested.

**Counterexample, gotchas, and operational comparison.** Hooks and MCP starting automatically, settings living outside package ownership, component names colliding, shared scripts gaining multiple owners, and marketplace metadata confused with runtime compatibility. Good: manifest declares a hook file, then hook guidance defines events and tests. Bad: infer hook safety from valid package structure. Borderline: a script library remains structural only until its deterministic behavior becomes a separate contract.

**Verification, evidence, and uncertainty.** Record trigger, destination, package and component identifiers, paths, owner, permissions, lifecycle, evidence returned, manifest changes, integration tests, conflicts, and return or stop decision. The local corpus enumerates component types and their activation lifecycles, and the seed explicitly identifies adjacent surfaces. Adjacent filenames and current host capabilities can evolve, so routing is by evidence capability.

**Second-order consequence.** A good handoff preserves the loader boundary: package evidence says the component exists, component evidence says whether its behavior is acceptable.

**Revision decision.** Replace generic pointers with capability triggers, minimal handoff fields, lifecycle ownership, return criteria, and cross-component examples.

**Retained seed evidence.** The original plugin, structure, manifest, command, hook, MCP, and settings route labels remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Adjacent reference guidance: Use command, hook, MCP, settings, or manifest references when one extension surface is already selected.
Adjacent reference 1: consider the plugin adjacent reference when the current task pivots away from plugin structure manifest patterns.
Adjacent reference 2: consider the structure adjacent reference when the current task pivots away from plugin structure manifest patterns.
Adjacent reference 3: consider the manifest adjacent reference when the current task pivots away from plugin structure manifest patterns.

## Workload Model

**Decision supported.** This section helps decide how much capability and loader complexity one plugin package and one manifest review should own before the design must split. The seed bounds work by one task, ten sources, three delegated subtasks, and an audit, but structure workload is driven by component and path graph size, initialization effects, owners, release coupling, and compatibility cells.

**Recommended default and causal basis.** Keep one coherent capability domain per package, minimize custom discovery edges, assign one owner per manifest and component path, isolate initialization effects, and split independent release or permission domains. Every component path, startup action, platform, host version, and owner multiplies package states that must remain consistent through install, update, disable, and removal.

**Operating conditions and assumptions.** The review inventories capabilities, component types, default and custom paths, names, startup effects, shared libraries, owners, versions, platforms, and test cells. Use this model for package architecture and review capacity, not component runtime throughput.

**Failure boundary and alternatives.** One manifest aggregates unrelated plugins, custom roots proliferate, parallel owners edit the same declaration, compatibility combinations grow unbounded, or raw source count is treated as capacity. Bounded alternatives and recoveries: split plugins, consolidate paths, generate manifest fragments, externalize shared deterministic libraries, narrow supported hosts, or create a plugin family with explicit version choreography.

**Counterexample, gotchas, and operational comparison.** Cross-package name collisions, duplicated component loading, shared state, MCP process fanout, hook event fanout, version skew, and compatibility matrices that omit component combinations. Good: one package owns a related command and skill with one release cadence. Bad: a manifest loads unrelated admin, deployment, and analysis systems. Borderline: a plugin family is viable only with ownership, dependency, collision, migration, and coordinated release tests.

**Verification, evidence, and uncertainty.** Measure capability domains, component and path counts, initialization effects, owner boundaries, shared files, release dependencies, host-platform cells, package size, test matrix, and split thresholds. Component-patterns directly covers flat, categorized, hierarchical, layered, shared, and plugin-family organization, while the seed recognizes ownership and task limits. Illustrative file-count thresholds in the corpus are not measured universal limits.

**Second-order consequence.** The binding workload is the number of loader and lifecycle contracts a reviewer can reconcile, not the number of Markdown files.

**Revision decision.** Retain seed capacity metadata but add loader graph, initialization, ownership, release, compatibility, and decomposition boundaries.

**Retained seed evidence.** The four workload rows and one-task, ten-source, three-subtask values remain preserved as provisional metadata. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`combined_evidence_inference_note`: Treat Plugin Structure Manifest Patterns as a agent workflow operating reference, not as a prose summary.

| workload_dimension_name | workload_boundary_value | verification_pressure_point |
| --- | --- | --- |
| primary_usage_surface | agent planning, tool use, context loading, delegation, or skill/plugin execution where bad guidance compounds across long-running sessions | verify that the reference changes the next implementation or review action |
| bounded_capacity_model | one primary task, up to 10 source files, up to 3 delegated subtasks, and a written completion audit for every run | split the task or create a narrower reference when this boundary is exceeded |
| source_pressure_model | local heading signals include Plugin Structure for Claude Code; Overview; Directory Structure; Plugin Manifest (plugin.json); Required Fields; Recommended Metadata; Component Organ | compare guidance against canonical local sources before following external examples |
| artifact_pressure_model | required artifact is manifest compatibility matrix with install validation and failure examples | require the artifact before claiming the reference is operationally usable |

## Reliability Target

**Decision supported.** This section helps decide which plugin-structure properties should be hard release invariants and which compatibility outcomes require sampled observations. The seed proposes full evidence labels, 18-of-20 routing, zero unsupported claims, and universal recovery paths but does not classify them or cover expected component equality, portability, startup containment, update migration, and removal.

**Recommended default and causal basis.** Enforce hard gates for valid artifact identity, manifest-package agreement, no unexpected or duplicate components, portable paths, declared initialization, recovery guidance, and unsupported-claim rejection; sample host and platform outcomes separately. Package invariants are deterministic for one artifact, while compatibility across hosts and environments needs explicit cohorts and cannot be inferred from a single installation.

**Operating conditions and assumptions.** Each target defines unit, artifact hash, host scope, hard-or-sampled class, denominator, evidence, miss consequence, owner, and retest. Treat seed values as proposed contracts or sampling goals, never observed host or plugin reliability.

**Failure boundary and alternatives.** 18 of 20 is advertised as compatibility, complete labels imply clean loading, expected components omit unexpected ones, or removal documentation substitutes for residue checks. Bounded alternatives and recoveries: retain strict artifact gates, bootstrap host baselines qualitatively, narrow support cells, sample initialization-heavy components separately, or delay distribution.

**Counterexample, gotchas, and operational comparison.** Cached discovery, paired source files counted twice, hidden user settings, environment-specific executables, missing failures excluded, and update tests starting from a clean install. Good: block a package with one unexpected hook and separately sample clean installs by host version. Bad: claim 90-percent manifest reliability. Borderline: local release may pass all hard gates while broader platform compatibility remains unclaimed.

**Verification, evidence, and uncertainty.** Record target class, package hash, host and platform, expected and observed set, denominator, raw outcomes, adverse cases, cache controls, migration state, residue, uncertainty, and remediation. Seed targets directly express provenance and routing concerns, and local sources support package equality, path, lifecycle, and maintenance gates. No compatibility cohort accompanies the archive, so achieved rates and thresholds remain unknown.

**Second-order consequence.** Reliable loading requires both absence of omissions and absence of surprises; unexpected activation can be more dangerous than a missing feature.

**Revision decision.** Classify targets, add package-set equality and lifecycle containment, define compatibility cohorts, require denominators, and prohibit unsupported achieved-rate claims.

**Retained seed evidence.** The four original reliability rows and thresholds remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| reliability_target_name | measurable_threshold_value | evidence_collection_method |
| --- | --- | --- |
| source_boundary_preservation | 100 percent of recommendations keep local, external, and inference boundaries visible | review generated text for the three evidence labels before reuse |
| decision_accuracy_sample | at least 18 of 20 sampled uses route to the correct adopt, adapt, avoid, or adjacent-reference decision | sample downstream tasks and record reviewer verdicts |
| unsupported_claim_rate | zero unsupported production, security, latency, or reliability claims in final guidance | reject claims without source row, explicit inference note, or verification method |
| recovery_path_clarity | every avoid or failure case names the rollback, escalation, or next-reference route | inspect failure-mode and adjacent-routing sections together |

## Failure Mode Table

**Decision supported.** This section helps decide which loader or lifecycle phase failed, which capabilities were affected, and what evidence is needed before the package can advance. The seed covers drift, generic advice, context loss, and fanout but omits manifest parse, semantic validation, package omission, path resolution, discovery, collision, initialization, activation, update, disable, and removal failures.

**Recommended default and causal basis.** Classify failures across artifact build, manifest parse, field semantics, path resolution, package inventory, discovery, registration, initialization, activation, migration, deactivation, or removal. Phase localization determines blast radius and recovery; a parser rejection should not be handled like a started server or a package update that changed state.

**Operating conditions and assumptions.** The first failing phase is observable, expected and actual components are compared, side effects stop, rollback or repair is bounded, and a fixture reproduces the issue. Use this table for package and loading failures and route internal component failures to their own references.

**Failure boundary and alternatives.** All failures become bad paths, custom declarations mask missing package files, retries ignore started processes, or a fixed manifest is assumed to clean previous initialization effects. Bounded alternatives and recoveries: rebuild the artifact, simplify fields, repair paths, include files, rename conflicts, isolate initialization, migrate state, disable components, kill owned processes, or remove and reinstall cleanly.

**Counterexample, gotchas, and operational comparison.** Host caches, duplicate default and custom registration, partial initialization, environment secrets, file permissions, version skew, stale state schemas, and removal that cannot distinguish user from plugin state. Good: an inventory omission blocks discovery and is fixed before activation. Bad: add an absolute path after a packaged script is missing. Borderline: preserve initialized state only when ownership and migration schema are verified.

**Verification, evidence, and uncertainty.** Capture phase, package hash, host version, expected set, signal, logs, resolved paths, processes and files, affected components, mitigation, replay, migration or cleanup, regression fixture, and owner. The source corpus directly describes the loader sequence, validation errors, discovery, initialization, conflicts, troubleshooting, and maintenance. Current host defects and platform package behavior may create additional failure classes.

**Second-order consequence.** Failure blast radius follows the loader timeline: errors after initialization demand effect cleanup even if a later manifest repair succeeds.

**Revision decision.** Retain generic rows and add loader-phase taxonomy, component-set diffs, effect containment, migration, clean replay, and recurrence feedback.

**Retained seed evidence.** Source drift, generic advice, context loss, and tool fanout remain preserved as cross-cutting failures. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| failure_mode_name | likely_trigger_condition | required_mitigation_action |
| --- | --- | --- |
| source drift hides truth | external or local guidance changes after the reference was written | refresh public evidence, rerun local corpus gate, and mark stale claims before reuse |
| generic advice escapes review | agent copies plausible best practices without theme-specific verification | block completion until the verification gate names concrete command, reviewer question, or metric |
| context window loses plan | long-running session forgets early constraints or overwrites user intent | write checkpoint summaries and re-read plan before each destructive step |
| tool fanout outruns budget | parallel actions create conflicts, duplicate work, or unbounded external calls | cap fanout, assign ownership, and require merge/audit checkpoints |

## Retry Backpressure Guidance

**Decision supported.** This section helps decide when a failed validation, installation, discovery, or activation may be retried and when package work must stop for repair or cleanup. The seed limits retries and pauses on red gates but does not define artifact identity, discovery cache, component process state, installation idempotency, or safe cleanup between plugin load attempts.

**Recommended default and causal basis.** Retry only after classifying the phase, preserving the exact package or rebuilding with a new hash, clearing owned cache and effects deliberately, changing a relevant prerequisite, and proving replay is idempotent or cleanly compensated. Blind reinstallation can mix artifacts, duplicate registrations, restart servers, rerun hooks, or hide the first failure behind cached state.

**Operating conditions and assumptions.** Attempt identity, package hash, host profile, cache state, process and file ledger, changed prerequisite, budget, owner, and semantic success criteria are recorded. Apply controls to plugin packaging and host loading; let components own their internal retry policies.

**Failure boundary and alternatives.** The same package is repeatedly enabled, custom paths are added per attempt, processes survive uninstall, a new version number masks unchanged bytes, or concurrent owners test one profile. Bounded alternatives and recoveries: use a fresh disposable profile, revert to default layout, remove optional components, stop owned processes, cleanly uninstall, inspect logs, isolate a minimal fixture, or escalate current-host uncertainty.

**Counterexample, gotchas, and operational comparison.** Auto-start MCP servers, session-bound discovery, hooks firing during tests, state migrations, plugin-root temp files, platform locks, and user data that must not be deleted during cleanup. Good: rebuild after adding a missing file, install into a fresh profile, and compare component sets. Bad: toggle enable repeatedly after partial initialization. Borderline: retry one transient process start only after verifying no prior process or state remains.

**Verification, evidence, and uncertainty.** Record failure fingerprint, attempt, package hash, profile, cache, processes and files before and after, changed prerequisite, exact commands, component inventory, activation result, cleanup, and stop reason. The seed establishes bounded retry and ownership, while local lifecycle and troubleshooting guidance exposes discovery, initialization, and cleanup concerns. Safe attempt budgets and host cache controls vary by current product implementation.

**Second-order consequence.** Backpressure preserves package-state identity; once artifact, cache, and effects are ambiguous, a fresh profile is cheaper than reasoning from contaminated evidence.

**Revision decision.** Add package and attempt identity, cache and effect ledger, idempotency, fresh-profile fallback, concurrency ownership, semantic pass criteria, and cleanup escalation.

**Retained seed evidence.** The original classification, bounded refresh, red-gate stop, checkpoint, and one-owner bullets remain retained. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- Retry only after the failed verification signal is classified as transient, stale evidence, missing context, or true contradiction.
- Use one bounded retry for stale external evidence refresh, then escalate to a human or a narrower source-specific reference.
- Apply backpressure by stopping new generation or implementation work when source coverage, critique coverage, or verification gates are red.
- For long-running agent workflows, checkpoint after each batch and re-read the current spec before any broad rewrite, commit, push, or destructive operation.
- For distributed execution, assign one owner per generated file or theme batch and require merge-time verification of exact path, heading, and evidence-boundary invariants.

## Observability Checklist

**Decision supported.** This section helps decide which minimal events let maintainers reconstruct a plugin structure failure from artifact build through removal without exposing secrets or raw user data. The seed records sources, proof, timing, tool calls, context, delegation, retries, and concise audits but omits package hash, manifest fields, resolved paths, expected and observed components, loader phase, processes, files, and privacy.

**Recommended default and causal basis.** Record plugin and host versions, package hash, install scope, parsed manifest summary, resolved default and custom paths, expected and observed component identifiers, loader phase, diagnostics, owned processes and files, update, disable, and residue. Correlation across artifact, loader phase, and effect state distinguishes malformed packages, stale caches, collisions, component failures, and incomplete cleanup.

**Operating conditions and assumptions.** Events share an installation or attempt identifier, sensitive environment values are redacted, component sets are diffable, failures remain visible, and summaries link to matrix cells. Capture package lifecycle evidence and route component-specific data to its owner.

**Failure boundary and alternatives.** Logs contain tokens, only successful components appear, package identity is missing, path errors lack resolution context, or raw debug output overwhelms the decision record. Bounded alternatives and recoveries: use detailed local fixture logs during development, aggregate privacy-preserving lifecycle metrics in distribution, retain a manual package packet for low-volume plugins, or delegate component telemetry.

**Counterexample, gotchas, and operational comparison.** MCP environment secrets, absolute user paths, hook input data, host profile identifiers, processes losing plugin ownership, cache state not logged, and update events crossing package hashes. Good: a record links one artifact hash to an unexpected hook registration and clean disable. Bad: upload the full debug directory. Borderline: development captures resolved paths while production retains only redacted set differences.

**Verification, evidence, and uncertainty.** Sample records and reconstruct package, manifest, resolution, discovery, initialization, activation, migration, deactivation, and removal; test redaction with secrets and paths. The source corpus directly defines loader phases and package fields, while the seed establishes concise evidence and workflow measurements. Retention, consent, centralized logging, and marketplace privacy requirements are outside the archived sources.

**Second-order consequence.** The most useful structural telemetry is set-based: expected versus observed components reveals omissions and surprises with little sensitive content.

**Revision decision.** Add artifact and attempt correlation, resolved path and component-set events, phase and effect tracking, secret redaction, privacy limits, and reconstruction tests.

**Retained seed evidence.** All six original observability bullets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- Record which local sources were loaded and which were intentionally skipped.
- Record the exact verification command, reviewer question, or rendered artifact used as proof.
- Record p50/p95/p99 latency or reviewer-time measurements when the reference affects runtime or workflow speed.
- Capture tool-call count, context files loaded, delegated tasks, retry count, and completion-audit outcome.
- Record leading indicator and failure signal from this file in the coverage manifest or journal when the reference drives real work.
- Keep audit evidence small enough to review: command output summary, changed-file list, and unresolved-risk notes are preferred over raw transcript dumps.

## Performance Verification Method

**Decision supported.** This section helps decide how to evaluate plugin structure efficiency without rewarding a fast loader that omits components, duplicates registrations, or leaves initialization effects. The seed requires tool and timeout budgets plus resumability, but it does not define build, install, discovery, initialization, activation, update, or removal stages or guard timing against incorrect component sets.

**Recommended default and causal basis.** Measure package build, manifest parse, path resolution, discovery, registration, initialization, first activation, update, disable, and removal separately while requiring expected component equality and clean effects. Latency without correctness can improve by silently skipping work, and one total duration hides whether custom paths, startup servers, hooks, or package size dominate.

**Operating conditions and assumptions.** The protocol fixes artifact hash, host, profile, platform, expected set, cache state, component mix, start and stop events, side effects, failures, retries, and comparison baseline. Evaluate package loading and maintenance workflow, not internal component or external server throughput.

**Failure boundary and alternatives.** Cold and warm loads mix, only successful installs remain, source-tree timing replaces package timing, removal ends before process checks, or file count is treated as causal proof. Bounded alternatives and recoveries: measure time to diagnosed failure, component discovery throughput, initialization contribution, reviewer effort, or qualitative lifecycle clarity until sample size supports percentiles.

**Counterexample, gotchas, and operational comparison.** Host caches, background MCP startup, hook side effects, platform filesystem behavior, antivirus or package extraction, hidden parallel initialization, and version drift. Good: compare default and custom path packages with identical expected sets and component mix. Bad: call a smaller manifest faster from one run. Borderline: report median clean-install time while withholding tail and causality claims.

**Verification, evidence, and uncertainty.** Publish fixture, artifact, host, raw stage timings, cache state, expected and observed sets, effects, failures, retries, summary calculations, baseline, and uncertainty. The seed names timing budgets, and the local corpus identifies discovery lifecycle, custom paths, nesting, configuration size, and initialization surfaces. No benchmark dataset or universal latency threshold is supplied.

**Second-order consequence.** The right performance unit is a correct lifecycle transition, because structural optimization that changes the loaded capability set is a behavior change.

**Revision decision.** Define staged timing, component correctness gates, cold and warm states, matched packages, failure inclusion, low-sample alternatives, and uncertainty.

**Retained seed evidence.** Tool-call and timeout budgets, resumable journal, lifecycle indicator, measurement packet, and pass-fail statements remain retained. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Performance method: require tool-call budgets, timeout budgets, and a resumable journal when the workflow exceeds one focused session.
Leading indicator to measure: users can install, invoke, debug, and remove the extension without reading implementation code.
Failure signal to watch: the reference confuses adjacent extension types or omits failure recovery.
Required measurement packet: capture input size, source count, tool-call count, wall-clock time, p50/p95/p99 latency where runtime applies, and reviewer decision time where documentation applies.
Pass condition: the reference must let a reviewer identify the correct next action, verification gate, and stop condition without reading unrelated files.
Fail condition: the reference encourages implementation before the workload, reliability target, and failure-mode table are explicit.

## Scale Boundary Statement

**Decision supported.** This section helps decide when one plugin manifest and package cease to be a coherent ownership and release boundary. The seed stops at multiple systems, ownership, unbounded discovery, production traffic, parallel edits, context drift, and large codebases but not plugin families, shared loader paths, component fanout, or version coordination.

**Recommended default and causal basis.** Split independent capability or permission domains, keep one manifest owner, version shared libraries explicitly, isolate startup components, namespace cross-plugin identifiers, and coordinate compatibility and migration across plugin families. As components and owners grow, path collisions, duplicated loading, shared state, release skew, and compatibility combinations exceed what one package review can reconcile.

**Operating conditions and assumptions.** The package boundary aligns with ownership and release cadence, shared code has contracts, plugin dependencies are explicit, supported host cells are bounded, and a coordinator owns migration order. Use this statement for package architecture and release coordination, not production service capacity.

**Failure boundary and alternatives.** One manifest spans unrelated systems, nested pseudo-plugins hide multiple ownership domains, many plugins share mutable files, cross-plugin names collide, or family releases have no version choreography. Bounded alternatives and recoveries: create separate plugins, consolidate a small coherent core, expose shared deterministic libraries, use external services, narrow supported versions, or deprecate unused components.

**Counterexample, gotchas, and operational comparison.** Duplicate commands across packages, hook fanout, MCP process multiplication, shared settings, package dependency cycles, version skew, and removal of one plugin breaking another. Good: separate security enforcement and documentation plugins with explicit shared library versions. Bad: a mega-plugin auto-starts unrelated servers and hooks. Borderline: a plugin family is viable only with namespacing, dependency contracts, coordinated tests, and rollback.

**Verification, evidence, and uncertainty.** Inventory packages, manifests, owners, component identifiers, shared paths and state, startup effects, dependencies, host matrices, release order, migrations, collisions, rollback, and decommission plan. Component-patterns directly discusses layered and plugin-family structures, while the seed already recognizes system and ownership boundaries. The archive provides no measured maximum package size, component count, or family scale.

**Second-order consequence.** Scale failure begins when package identity no longer predicts ownership, lifecycle, or loaded capability set.

**Revision decision.** Add plugin-family, shared-resource, startup-fanout, dependency, version, compatibility, migration, and decommission boundaries.

**Retained seed evidence.** The original system, ownership, distributed execution, context drift, and graph-narrowing limits remain retained. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Plugin Structure Manifest Patterns stops being sufficient when the task spans multiple independent systems, more than one ownership boundary, unbounded source discovery, or production traffic without an explicit SLO.
Under distributed execution, split work by theme file and preserve one verification owner per split; do not let parallel agents rewrite the same reference without a merge checkpoint.
Under long-running agent workflows, treat context drift as a reliability failure: checkpoint state, summarize open risks, and verify against the spec before continuing.
Under large-codebase scale, require dependency or source-graph narrowing before applying this reference; a source list without ranked canonical guidance is not enough.

## Future Refresh Search Queries

**Decision supported.** This section helps decide when and how maintainers should refresh structure and manifest guidance without overwriting frozen archive claims with search snippets or latest-version assumptions. The seed provides generic official-docs, GitHub-example, and release-note queries without drift triggers, exact manifest feature or host version, source ranking, or package reproduction.

**Recommended default and causal basis.** Search after a documented parser, discovery, path, component, or marketplace drift signal; include the exact host version and field; prefer official versioned sources; archive the result; reproduce it with a minimal packaged fixture; and record the diff. Search discovers candidate evidence, while package behavior and versioned authoritative material determine whether guidance actually changed.

**Operating conditions and assumptions.** The trigger is narrow, query names the field or lifecycle phase, source ownership and date are recorded, archive and current versions stay separate, and accepted changes update matrix fixtures and migration notes. Search native plugin structure separately from MCP component behavior and preserve each evidence lane.

**Failure boundary and alternatives.** Result snippets become schema facts, community trees define host behavior, current docs are assumed backward compatible, absence proves unsupported behavior, or routine browsing is called verification. Bounded alternatives and recoveries: inspect installed diagnostics, build a minimal manifest fixture, compare tagged source or release artifacts, preserve provisional uncertainty, or remove the disputed custom field.

**Counterexample, gotchas, and operational comparison.** Similar plugin ecosystems, unstable latest pages, old repositories, generated docs, marketplace versus local-install differences, and MCP results crowding native manifest evidence. Good: after a path field stops loading, search its exact name and host version, reproduce the official change, and add migration. Bad: copy a popular complete manifest. Borderline: retain a community workaround as provisional until packaged reproduction.

**Verification, evidence, and uncertainty.** Record trigger, exact query, date, owner, version, archived hash, claim summary, package fixture, observed component set, conflict, accepted change, migration, reviewer, and next trigger. The seed supplies three query categories and local sources identify concrete field, discovery, and lifecycle surfaces likely to drift. No browsing occurred, so these rows are unexecuted maintenance prompts and prove no current behavior.

**Second-order consequence.** Refresh quality is measured by a versioned package-behavior diff, not the number or recency of links.

**Revision decision.** Retain exact queries and add triggers, field and version qualifiers, authority ranking, archiving, package reproduction, migration, and rejection examples.

**Retained seed evidence.** The official documentation, GitHub repository, and release-note query labels and texts remain unchanged. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| search_query_label_name | search_query_text_value |
| --- | --- |
| `official_docs_query_phrase` | plugin structure manifest patterns official documentation best practices |
| `github_repository_query_phrase` | plugin structure manifest patterns GitHub repository examples |
| `release_notes_query_phrase` | plugin structure manifest patterns changelog release notes migration |

## Evidence Boundary Notes

**Decision supported.** This section helps decide how every structure or compatibility claim should reveal what was read, packaged, parsed, observed, tested, inferred, or left uncertain. The seed defines local, external, and combined evidence but not duplicate lineage, package artifact facts, current host parsing, observed component sets, lifecycle fixtures, or provisional architecture judgments.

**Recommended default and causal basis.** Preserve the three seed labels and add duplicate-lineage, package-artifact, installed-host observation, lifecycle-test, and provisional-design classes in use, with combined claims listing each prerequisite. Manifest work crosses documentation, bytes, loader semantics, component behavior, platform state, and external protocols; certainty cannot transfer automatically between those layers.

**Operating conditions and assumptions.** Atomic claims cite exact evidence, duplicate files count once, artifact and host identities are explicit, expected and observed sets are compared, inferences state scope, and conflicts remain visible. Apply these labels to this reference and downstream manifest matrices while preserving exact seed labels.

**Failure boundary and alternatives.** Labels decorate unsupported prose, archive examples become current schema, package presence proves discovery, one host proves portability, MCP sources prove native fields, or uncertainty does not alter support claims. Bounded alternatives and recoveries: split broad statements, downgrade to a hypothesis, build a minimal package, preserve contradictory outcomes, narrow compatibility, or decline the field or component.

**Counterexample, gotchas, and operational comparison.** Valid JSON does not mean accepted schema, discovery does not mean safe activation, activation does not mean clean removal, and two identical paths do not corroborate. Good: archive guidance proposes a path, package inventory proves bytes, current host proves discovery, and lifecycle test bounds support. Bad: infer marketplace compatibility from structure prose. Borderline: report one-host success with other cells pending.

**Verification, evidence, and uncertainty.** Sample each recommendation, trace clauses to class and location, confirm hashes and versions, inspect duplicate handling, test combined prerequisites, preserve negative evidence and conflicts, and ensure uncertainty changes action. The three fully read sources, exact duplicate hashes, and loader model directly support the expanded taxonomy. Taxonomy cannot eliminate host variability or cover untested environments.

**Second-order consequence.** Confidence is compositional: a reviewer should know whether changing documentation, package bytes, host behavior, or lifecycle results would alter the decision.

**Revision decision.** Extend the three-label note with lineage, artifact, host, fixture, set-difference, combination, conflict, and compositional-confidence rules.

**Retained seed evidence.** The exact local-corpus, external-research, and combined-evidence definitions remain preserved verbatim. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- `local_corpus_sourced_fact`: statements tied directly to the local source paths above.
- `external_research_sourced_fact`: statements tied to the public URLs above.
- `combined_evidence_inference_note`: synthesis that combines local and public evidence into agent guidance.
