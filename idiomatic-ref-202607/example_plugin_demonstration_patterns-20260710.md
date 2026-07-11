# Example Plugin Demonstration Patterns

Use this reference to turn one extension capability into a small, inspectable, and safely reusable demonstration. Begin by deciding what invokes the capability and what the user must observe. A skill supplies model-invoked contextual guidance; a command is explicitly invoked; a hook reacts to a lifecycle event; an MCP integration crosses a tool or resource boundary; a setting configures behavior; and a plugin wrapper distributes one or more surfaces. These are different contracts even when one package eventually combines them.

The only fully inspected local artifact for this theme is a focused historical `SKILL.md`. Its archive and working copies are byte-identical, so they are one source in two locations rather than corroborating evidence. It demonstrates a narrow description, trigger-oriented applicability, a required skill file, optional supporting folders, structured guidance, and trigger testing. It does not establish a current plugin manifest, host installation command, hook schema, MCP server, permission model, upgrade path, or uninstall behavior. The inherited public mappings were not browsed in this evolution.

Use this conservative demonstration sequence:

1. State one user goal, one observable successful behavior, one non-goal, and the consequence of accidental activation.
2. Select one primary extension surface from invocation semantics. Do not add a command, hook, server, setting, or wrapper merely to make the example look comprehensive.
3. Discover the target host, supported schema, file locations, validation commands, installation method, permission boundary, and cleanup behavior before claiming them.
4. Build the smallest artifact that can teach the selected surface. For the locally supported skill case, begin with one `SKILL.md`; add references, examples, or scripts only when the main skill links to them and the walkthrough exercises their responsibility.
5. Keep the baseline deterministic and side-effect free. If a demonstration must call a network, shell, repository, or external service, use an isolated fixture, least privilege, bounded data, and an explicit recovery path.
6. Verify structure, representative positive requests, neighboring negative requests, expected response behavior, and noninterference. Case count follows trigger breadth and consequence; it is not a universal quota.
7. Verify installation, invocation, permission denial, upgrade, removal, and residue only for lifecycle surfaces actually present in the target environment. Static inspection is not execution evidence.
8. Retain the accepted minimal tree, commands actually run, observations, known host assumptions, one useful rejected design, and the condition that would justify another surface.

| Primary surface | Choose it when | Minimum demonstration evidence | Route away or add a companion when |
|---|---|---|---|
| Skill | The model should load focused guidance from task context. | Valid target-host skill structure, bounded description, positive and negative activation cases, and observable guidance behavior. | The user needs explicit invocation, event automation, external tools, configuration, or distribution proof. |
| Command | The user must deliberately invoke a named operation. | Discoverable invocation, argument and error behavior, deterministic output, and help or recovery evidence. | The capability should activate implicitly from context or run on a host event. |
| Hook | A known host lifecycle event should trigger bounded automation. | Event match, ordering, timeout, failure isolation, reentrancy, and disable or recovery behavior. | The action requires user confirmation, broad reasoning, or an external service contract. |
| MCP integration | The capability must expose or consume tools, resources, or prompts across a protocol boundary. | Target protocol schema, transport lifecycle, capability negotiation, authentication or permission behavior, malformed-input handling, and shutdown. | Static contextual guidance is sufficient or the target host contract is unknown. |
| Setting | Users need a stable configuration choice rather than another action. | Default, validation, scope, precedence, migration, and rollback behavior. | The value represents a command or secret that should not be stored as ordinary configuration. |
| Plugin wrapper | Several proven surfaces need one installable and removable distribution unit. | Current manifest or package validation, complete file inclusion, install, load, version, upgrade, permission, removal, and residue checks. | Only one unwrapped teaching artifact is evidenced or packaging rules have not been inspected. |

A good baseline is one narrowly described skill that answers realistic requests, declines neighboring requests, uses only files the walkthrough needs, and labels host-specific lifecycle claims as unverified until executed. A bad example places a skill beneath a directory named `example-plugin`, advertises commands, hooks, and MCP tools that do not exist, and then calls the result installable. A wrapper is borderline when a target project supplies a real manifest: it becomes acceptable after schema validation, installation, invocation, denial, removal, and clean-state checks under the supported host.

Translate historical tree diagrams to ASCII and preserve the target repository's established layout. Do not infer current frontmatter fields or activation semantics from the archived version label alone. The demonstration can be decisive about method while remaining conditional about contemporary host APIs: inspect first, state the claim, run the smallest disconfirming gate, and report only what was observed.

Treat the example as replicated code, not decorative documentation. Names, triggers, optional folders, permissions, and missing checks will be copied into later extensions. A demonstration earns promotion to a reusable template only when its assumptions, ownership, supported versions, verification, and retirement path are visible. More surfaces do not make it more complete; a smaller example with an honest lifecycle is safer to learn from.

## Source Evidence Mapping Table

Treat every source as evidence for a bounded claim, not as authority for the whole example plugin. The two local paths contain exactly the same 84-line skill file with SHA-256 `87d90442621ace039aa3379805f99c3f95bf500e9f7b96f9e7876ac2dcf804f5`; preserve both locations for provenance, but count their content once.

| Source | Inspection state | Permitted use in this reference | Material limit | First applicability gate |
|---|---|---|---|---|
| `agents-used-monthly-archive/claude-skills-202603/plugins/example-plugin/SKILL.md` | Complete local read; frozen historical source, version label 1.0.0 | Primary historical evidence for a skill's focus, description-led triggering, required `SKILL.md`, optional support folders, structured instructions, examples, and overlap testing. | It contains no plugin manifest, command, hook, MCP implementation, permission declaration, installer, upgrade, or removal path. Its exact frontmatter and activation claims were not refreshed. | Validate adapted structure in the target host, then exercise realistic positive and neighboring negative requests. |
| `claude-skills/plugins/example-plugin/SKILL.md` | Complete local read; byte-identical duplicate locator | Shows the same skill was copied into a working corpus path and can help locate dependent repository material. | Duplicate bytes provide no independent corroboration and no evidence of installation or current host compatibility. | Compare content hash and repository ownership; cite the archive for historical claims and the working path only for current project discovery. |
| `https://modelcontextprotocol.io/specification/2025-06-18/server/resources` | Inherited date-pinned URL; not browsed in this evolution | Future primary-source candidate only if the selected demonstration exposes or consumes MCP resources. | It cannot establish skill triggers, plugin packaging, current protocol revision, host integration, authentication, transport, or lifecycle behavior here. | Confirm an MCP resource requirement, inspect the current applicable specification, and test the target server-client boundary. |
| `https://github.com/modelcontextprotocol/servers` | Inherited repository mapping; not browsed in this evolution | Future discovery index for maintained server examples after an MCP surface is selected. | Repository examples can vary in support, protocol revision, security, transport, and teaching quality; existence is not recommendation. | Verify publisher, commit or release, applicable protocol, complete implementation path, and target-host compatibility. |
| `https://github.com/github/github-mcp-server` | Inherited integration mapping; not browsed in this evolution | Future evidence only when the example's user goal actually requires GitHub operations through an MCP boundary. | A service-specific server cannot justify a generic plugin lifecycle, skill structure, permissions, or safe repository operations. | Define least-privilege GitHub capability, inspect current official material, and test authentication, denial, bounded side effects, and cleanup. |
| Target host and project artifacts, discovered at use time | Not available in this generic reference | Current applicability authority for manifest or package schema, file inclusion, supported extension surfaces, host help, installation, validation, permissions, tests, versioning, and removal. | Local artifacts can be stale or accidental and show what exists rather than what should be copied. | Combine schema validation with host loading, positive and negative behavior, permission denial, package inspection, and removal-residue checks. |

The local skill is a useful teaching skeleton, but its directory name does not make it a complete plugin. It states that skills are model-invoked and contrasts them with user-invoked commands, lists `name`, `description`, `version`, and `license` as frontmatter options, recommends a focused domain, and shows optional `README.md`, `references`, `examples`, and `scripts` folders. Those are historical observations. Current required fields, file locations, loader behavior, and invocation semantics remain target-verified concerns. Its Unicode tree diagrams are also translated to ASCII in this evolved reference rather than copied literally.

For each material extraction, retain:

```text
Source path or direct location
Exact observed claim and source version
Evidence class and permitted scope
Target host or project artifact affected
Selected or rejected design implication
Gate actually run and observed result
Residual uncertainty and refresh trigger
```

Good use extracts the skill's trigger-focus question, adapts the description to a real user goal, and proves both activation and nonactivation in the target host. Bad use cites the GitHub MCP server to claim that a directory containing only `SKILL.md` can be installed and removed as a plugin. Borderline use opens the MCP resource specification after a genuine resource-sharing requirement appears; it becomes actionable only after protocol, transport, permission, malformed-input, shutdown, and host-integration evidence is added.

No current public-page claim is established here. A future external refresh must record direct source, publisher, checked date, applicable release or revision, bounded finding, conflict, target implication, and local retest. Packaging truth comes from the declared files, files actually distributed, host loader behavior, permission boundary, and clean removal together; no single source row proves that lifecycle.

## Pattern Scoreboard Ranking Table

The inherited values are editorial ordering from the seed, not probabilities, confidence levels, measured effectiveness, or adoption results. Their derivation is unavailable. Preserve them for traceability, but do not compare their spacing, average them, or let them override a failed permission, invocation, lifecycle, or cleanup gate.

| Pattern | Inherited score or priority | Apply when | Failure prevented | Direct falsifier |
|---|---|---|---|---|
| Source Map First (`example_plugin_demonstration_patterns`) | 95; historical default tier | Before reusing any claim from the duplicated skill or unrefreshed external mappings. | A historical file or protocol link becomes current package authority without inspection. | Every material recommendation has a source disposition and target-host applicability result. |
| Evidence Boundary Split (`example_plugin_demonstration_patterns`) | 91; historical default tier | When local content, public mappings, target observations, and synthesis mix. | Directory names, duplicated files, or reputable links acquire confidence they have not earned. | Claims distinguish historical observation, duplicate locator, unrefreshed mapping, target evidence, illustration, and inference. |
| Verification Gate Coupling (`example_plugin_demonstration_patterns`) | 88; historical default tier | Before an example claims activation, installation, external access, permissions, upgrade, or removal. | Plausible files are reported as operational without a falsifiable observation. | Each lifecycle claim names the exact host boundary and executed or conditional gate. |
| Capability Contract First | First construction decision | A user request is being turned into any extension demonstration. | The example showcases mechanisms while the intended user behavior and non-goals remain ambiguous. | One compact contract states goal, successful observation, non-goal, accidental-invocation consequence, and recovery. |
| Smallest Primary Surface | Construction default | More than one skill, command, hook, MCP, setting, or wrapper is proposed. | A teaching fixture becomes a kitchen-sink package with overlapping invocation and failure ownership. | Every included surface owns a distinct interaction that cannot be taught safely through the baseline surface. |
| Target Host Contract Discovery | Hard currentness gate | File shape, schema, loader, commands, or lifecycle behavior depends on a host. | Historical syntax or guessed locations fail in the contemporary environment. | Current target help, schema, validator, and loading behavior are inspected before implementation claims. |
| Minimal Artifact Closure | Leads before optional folders | References, examples, scripts, assets, or generated files are added. | Decorative files drift, ship unexpectedly, or imply unimplemented behavior. | Every file is reachable from the walkthrough, has an owner, and is included or excluded deliberately in packaging. |
| Activation Isolation | Hard implicit-invocation gate | A model selects a skill or another surface can activate automatically. | Broad triggers capture unrelated tasks or overlap neighboring extensions unpredictably. | Positive, paraphrased, neighboring negative, and overlap cases produce the intended selection and nonselection. |
| Deterministic Safe Fixture | Hard teaching gate | The demonstration executes code, tools, filesystem writes, network calls, or service operations. | Learners copy nondeterminism, credentials, live side effects, or irreproducible state into later work. | A clean isolated run produces bounded output, no secret exposure, explicit state change, and repeatable cleanup. |
| Permission and Denial Contract | Hard trust gate | The example requests files, shell, network, repository, identity, or third-party access. | Happy-path instructions normalize excessive privileges or undefined denial behavior. | Least privilege, denied access, cancellation, partial effect, and safe recovery are exercised. |
| Install Remove Symmetry | Hard distribution gate | The example claims to be an installable plugin or reusable package. | Installation leaves hidden files, stale registrations, permissions, processes, or unusable host state after removal. | Clean install, load, upgrade or replacement, disable, removal, residue scan, and reinstall are observed. |
| Copyability and Promotion Review | Final template gate | A workshop example will be published, scaffolded, or reused across projects. | Illustrative shortcuts silently become supported defaults and compatibility promises. | Assumptions, versions, ownership, gates, limitations, and retirement path are visible to a copier. |

**Default construction order:** capability and non-goal, primary invocation surface, target host contract, minimal artifact tree, deterministic behavior, positive and negative activation, permission and failure paths, install or removal lifecycle when present, and copyability review. Freeze the behavior before adding a distribution wrapper; packaging should not make an incoherent example appear complete.

**Override rule:** repair begins at the earliest observed boundary that invalidates the example and then reruns its dependents. A permission escape or live destructive effect outranks every editorial row. A broad skill trigger makes activation isolation lead. An invalid manifest makes host discovery and schema validation lead. Removal residue makes lifecycle symmetry lead. Keep the override reason; repeated relevant failures or one high-consequence escape can justify changing the default order.

A narrow contextual skill with no external side effect is the default case. An event hook that can modify files elevates reentrancy, permission, rollback, and disable behavior before presentation polish. An MCP demonstration elevates protocol, authentication, malformed-input, transport shutdown, and external-service isolation. A multi-surface wrapper is borderline until each surface proves a distinct responsibility and all share one verified install, version, permission, and removal lifecycle.

Numeric rank cannot rescue an unverified example. The useful priority is the first pattern that changes the next implementation or test action and whose failure would teach the copier the wrong capability contract.

## Idiomatic Thesis Synthesis Statement

`historical_local_observation`: The two mapped local paths contain the same historical skill template. It teaches a focused purpose, description-led trigger cues, one required `SKILL.md`, optional linked support material, structured instructions, concrete examples, and overlap testing. It does not demonstrate a complete plugin distribution or another extension surface.

`external_mapping_unrefreshed_note`: The date-pinned MCP resource page, MCP server index, and GitHub MCP server repository were inherited and not opened. They provide no current protocol, security, server, or host-integration fact in this evolution.

`systems_synthesis_or_judgment`: An idiomatic extension demonstration is an executable teaching contract: the smallest target-host-compatible artifact that makes one user goal, invocation mechanism, expected observation, non-goal, failure recovery, permission boundary, and lifecycle claim inspectable. It is complete relative to the surfaces it includes, not relative to every mechanism the host supports.

Use this reversible loop:

1. Define the learner and user outcome. State the request, successful observation, non-goal, accidental-invocation consequence, side-effect boundary, and recovery expectation.
2. Select one primary surface by invocation semantics: contextual skill, explicit command, automatic hook, protocol integration, configuration, or distribution wrapper.
3. Inspect the current target host. Confirm supported schema, paths, loader behavior, validators, commands, permissions, package rules, versions, and cleanup before encoding them.
4. Build the minimal artifact closure. Every file must be required by the host or reached from the walkthrough; every optional folder needs a named consumer and owner.
5. Make the baseline deterministic and isolated. Prefer fixture data and reversible local state; add network, repository, shell, identity, or service access only when the capability contract requires it.
6. Verify invocation and noninterference. Exercise representative positive phrasing, paraphrases, neighboring negative requests, overlap, repeated invocation, invalid input, cancellation, and denied permission as applicable.
7. Verify behavior, not just shape. Check the expected user observation, bounded side effect, error or recovery message, logs or evidence, and unchanged state outside the declared scope.
8. Verify lifecycle only when claimed. For a plugin wrapper, inspect package contents and exercise install, load, version compatibility, upgrade or replacement, disable, removal, residue, and reinstall.
9. Make copying safe. Preserve exact commands run, host version, assumptions, known omissions, one informative rejected design, and the trigger for adding another surface.
10. Promote, version, and retire deliberately. A workshop artifact becomes a reusable template only after ownership, support scope, compatibility, and regression evidence are accepted.

The loop is intentionally asymmetric. A skill-only example does not need fake hook, server, or uninstall files to look complete. A packaged plugin cannot omit lifecycle evidence merely because its inner skill is clear. An automatic hook or external protocol server moves permission, reentrancy, timeout, denial, malformed-input, shutdown, and rollback checks earlier because its failure can occur without an explicit user command.

Prefer the least powerful surface that can establish the user outcome. A static walkthrough is easy to inspect but cannot prove host behavior. A runnable fixture is more persuasive but adds environment and cleanup obligations. A model-invoked skill demonstrates contextual guidance but needs careful nonactivation tests. A command makes intent explicit but needs arguments and error semantics. A hook automates a host event but expands reentrancy and failure isolation. An MCP server crosses protocol and security boundaries. A wrapper simplifies distribution only after its component surfaces and package lifecycle are real.

Do not copy the historical frontmatter list, directory shape, or broad trigger language as current universal policy. Keep an established target-host convention when its validator and loader prove it and the example remains understandable. Remove or avoid a layer, folder, script, resource, or surface that has no distinct teaching or runtime responsibility. Decorative completeness is a defect because learners infer support from presence.

A good demonstration is a narrow skill whose description reflects real requests, whose guidance produces a visible bounded result, whose negative cases leave unrelated work alone, and whose support files are all used. A bad demonstration is a directory named plugin that advertises a command, hook, MCP server, settings, and GitHub access while containing only one Markdown skill. A real wrapper is borderline until current manifest validation, package inclusion, least privilege, installation, invocation, denial, clean removal, and reinstall are observed.

Verification evidence must match the claim. Markdown parsing supports file-shape claims; a target validator supports schema claims; host loading supports discovery claims; positive and negative requests support activation claims; isolated behavior checks support output and side-effect claims; package inspection and lifecycle exercises support distribution claims. One green mechanism does not upgrade the others implicitly.

The thesis stops being sufficient when the example becomes production automation, a privileged external integration, a multi-service protocol, or a supported distribution with independent consumers and no accountable operations model. Keep this reference for the teaching slice, then route security, protocol, release, or service guarantees to specialist owners and return with the constraints the example must expose.

The durable artifact is a verified capability lesson plus visible lifecycle boundaries. Once copied, examples become compatibility and security inputs. Promotion should therefore preserve supported host versions, ownership, gates, limitations, migration, and retirement. More surfaces increase teaching cost and failure combinations; they do not increase quality unless each one earns its place.

## Local Corpus Source Map

Use the archive path as frozen provenance and the working path as a duplicate locator:

- `agents-used-monthly-archive/claude-skills-202603/plugins/example-plugin/SKILL.md`
- `claude-skills/plugins/example-plugin/SKILL.md`

Both files were read completely and have identical content. Do not read them twice for confidence or treat one as independent support. The map below segments their one shared 84-line historical artifact.

| Source region | Retrieve when | Useful candidate or question | Caveat | Target gate |
|---|---|---|---|---|
| YAML frontmatter | Identifying the skill, historical trigger description, or version annotation. | Does the name communicate scope, and does the description use realistic user language? | The listed `name`, `description`, `version`, and `license` behavior is historical and may not match the current host schema. | Inspect current target-host schema and validator; test the adapted fields rather than copying them blindly. |
| `Example Skill` and `Overview` | Distinguishing contextual skill guidance from commands or spawned agents. | Is a model-invoked skill the correct primary surface for the capability? | The source does not demonstrate a plugin wrapper, command, hook, agent, MCP server, or their interaction. | Confirm target invocation semantics and route any added surface to its own current contract. |
| `When This Skill Applies` | Designing activation and nonactivation cases. | Which user requests, paraphrases, topics, and neighboring requests should select or avoid this skill? | The three bullets are positive examples only; they do not prove host selection, overlap, or noninterference. | Run target-host positive, paraphrased, negative, overlap, and repeated-invocation cases. |
| `Skill Structure` and `Required Files` | Creating the minimum skill artifact. | Can one `SKILL.md` teach the capability without unused scaffolding? | The Unicode tree is illustrative and is not a packaging, installation, or current path specification. | Translate the tree to ASCII, validate the actual location, and prove the host loads the minimal artifact. |
| `Optional Supporting Files` | Deciding whether to add documentation, references, examples, or scripts. | Which material is too detailed for the main skill and has a real reader or invocation path? | Optional folders can become decorative cargo cult; helper scripts add executable and permission risk. | Trace each file from the walkthrough, inspect package inclusion, exercise scripts safely, and remove unreachable material. |
| `Frontmatter Options` | Evaluating metadata fields. | Which fields are required, optional, versioned, or governed by the target environment? | The source asserts options but supplies no current schema citation or invalid-field behavior. | Validate accepted, missing, unknown, and malformed fields with the current host or its official validator. |
| `Writing Effective Descriptions` | Refining activation language. | Does the description name specific requests without overclaiming adjacent work? | Copying the generic sample phrase would create broad triggers; phrases alone do not establish runtime selection. | Replace every generic phrase, compare neighboring skills, and verify activation plus nonactivation. |
| `Skill Content Guidelines` | Structuring the main instructions. | Are purpose, applicability, ordered guidance, concrete actions, and examples sufficient for the intended user result? | A well-structured document can still be wrong, unsafe, or impossible under the host. | Run the complete user journey and failure case; inspect output rather than scoring headings alone. |
| `Best Practices` | Reviewing focus, support files, activation, and overlap before reuse. | Is the domain narrow, support material necessary, expected phrasing covered, and overlap controlled? | These are historical recommendations without measured completeness or current host authority. | Treat them as review prompts and retain counterexamples, target evidence, and a promotion decision. |

Use progressive retrieval profiles:

- **Full skill demonstration:** read every region and reconcile metadata, activation, structure, content, support files, and overlap before host testing.
- **Trigger refinement:** read frontmatter, applicability, description, and best-practice regions, then inspect neighboring skills and run positive and negative cases.
- **Minimal structure review:** read required and optional structure plus content guidance, then validate actual host path and support-file reachability.
- **Template promotion:** read the entire source and add current schema, package, permission, lifecycle, compatibility, and copyability evidence absent from the corpus.
- **Plugin installation or MCP work:** use this map only for the inner skill concern and route the missing distribution or protocol contract elsewhere.

Record `(region, exact observation, durable question, caveat, adapted artifact, host evidence, selected or rejected decision, residual uncertainty)`. Good retrieval combines description, applicability, and overlap regions before changing a trigger. Bad retrieval copies both paths, Unicode trees, every optional folder, and all historical fields into a scaffold. A plugin wrapper is borderline: the local source can guide its inner skill, but it cannot establish manifest, installation, permissions, upgrade, or removal.

The source's bytes and teaching intent are known. Current host interpretation, supported metadata, activation quality, lifecycle behavior, and measured teaching effectiveness remain unproved. When one region changes, invalidate its dependents deliberately: a description edit reopens activation tests; a support-file edit reopens reachability and package checks; a script edit reopens permission, side-effect, and cleanup evidence.

## External Research Source Map

No browsing occurred in this evolution. These inherited locations are
`external_mapping_unrefreshed_note` records, not current facts or recommendations.

| Inherited location | Historical role | Permitted future use after inspection | Current disposition | Target applicability gate |
|---|---|---|---|---|
| `https://modelcontextprotocol.io/specification/2025-06-18/server/resources` | Date-pinned MCP resource specification page | Clarify resource discovery, listing, reading, addressing, or change behavior only when the selected example includes an MCP resource surface. | Retain as a plausible primary-source retrieval target; content, status, and current revision are unverified. | Confirm the capability needs resources, inspect the currently applicable specification, and test server-client schema, malformed input, permissions, transport, and shutdown. |
| `https://github.com/modelcontextprotocol/servers` | MCP server implementation index | Discover candidate maintained examples after protocol semantics and target transport are known. | Retain as an implementation-discovery index, not normative protocol or plugin guidance. | Verify publisher, support status, release or commit, protocol revision, complete code path, security model, and target-host compatibility. |
| `https://github.com/github/github-mcp-server` | GitHub-specific MCP server repository | Study repository and issue operations only when the demonstration's user goal actually requires that integration. | Retain as a service-specific candidate; no present installation, authentication, permission, or behavior claim. | Define bounded GitHub operations and least privilege, then test authentication, denial, cancellation, partial effects, rate or service failure, audit, and cleanup. |

These mappings cannot answer the ordinary skill demonstration's current questions: accepted frontmatter, loader paths, description semantics, invocation selection, plugin manifest, command or hook schemas, settings precedence, package inclusion, installation, permissions, upgrades, or removal. A future authorized refresh should first discover the target host and exact version, then seek its primary documentation, schema, help, release notes, migration guidance, and security or lifecycle material. This reference intentionally does not invent those URLs.

Refresh only when a changing public fact can alter a material decision. Useful triggers include a failed target validator, host upgrade, manifest migration, deprecated field, new extension surface, protocol revision, permission change, transport change, security review, incompatible copied template, or install and removal defect. A local project can keep working while relying on behavior a later release removes; local success and public support are different evidence.

Retain this future refresh record:

```text
Frozen question and implementation decision
Target host, extension surface, and exact version
Direct source, publisher, release or commit, and checked date
Relevant section and bounded paraphrased finding
Evidence role: specification, host documentation, release note, or example
Applicability, conflict, security consequence, and changed action
Target validation or behavior retest and observed result
Disposition, residual uncertainty, owner, and next refresh trigger
```

Classify a result as `inspected`, `applicable`, `reproduced`, `reconciled`, `rejected`, `superseded`, or `no_material_impact`. An official protocol page can be current but irrelevant to a skill. A repository example can run but target another transport or threat model. A host validator can pass while trigger behavior or removal remains wrong.

Good use selects an MCP resource surface first, refreshes the applicable resource specification, and then exercises the target server and client with permission and malformed-input cases. Bad use cites the server index to claim a directory containing only `SKILL.md` is a complete installable plugin. Borderline use studies the GitHub server after a real repository capability appears; it remains conditional until authentication, least privilege, user confirmation, bounded side effects, service failures, audit, and cleanup are verified.

Prefer event-driven refresh over bibliography growth. Retire a repeatedly irrelevant mapping while preserving why it was rejected and which future capability would reopen it. External evidence is complete only after the affected target-host behavior is rerun; link presence and repository popularity never establish the demonstration lifecycle by themselves.

## Anti Pattern Registry Table

Classify an anti-pattern only after naming the violated capability, invocation, trust, lifecycle, or copyability contract. Architectural resemblance is insufficient. Stop secret exposure and destructive effects first, then excessive permission, automatic invocation, removal residue, host mismatch, trigger overlap, unreachable files, and cosmetic complexity.

| Anti-pattern | Cause and consequence | Detection signal | Safer response | Valid boundary or exception |
|---|---|---|---|---|
| `context_free_summary_output` | Generic plugin advice replaces the one inspected skill and target-host evidence. | No source disposition or host artifact changes the recommendation. | Trace each pattern through local content, target contract, and one behavior gate. | A source region may be skipped when its inability to change the decision is recorded. |
| `unsourced_recommendation_claims` | Current schema, security, compatibility, or lifecycle language sounds authoritative without inspection. | Claim has no evidence class, target result, or uncertainty. | Separate historical observation, unrefreshed mapping, synthesis, and executed observation. | A preference is valid when clearly scoped and owned. |
| `directory_name_equals_plugin` | A folder named plugin is treated as an installable package although it contains only an inner artifact. | No manifest, loader, package contents, install, or removal evidence accompanies the claim. | Call it a skill example until the current distribution contract is proven. | A host may conventionally infer packaging, but that inference still needs current load and lifecycle evidence. |
| `kitchen_sink_demonstration` | Skill, command, hook, MCP, settings, and wrapper are included to showcase breadth rather than one user goal. | Surfaces have overlapping invocation or no distinct acceptance test. | Keep one primary surface and add another only for a separate necessary responsibility. | A composition workshop can include mocks when each is unmistakably labeled and isolated. |
| `duplicate_source_confidence` | Identical files are counted as corroborating evidence. | Different paths share the same content hash and claims. | Preserve both locators while treating the bytes as one source. | Independent project behavior can corroborate the claim even when documentation is copied. |
| `broad_trigger_capture` | A skill description names vague topics or common words and activates on unrelated requests. | Neighboring negative prompts select the skill or several skills overlap without resolution. | Use realistic bounded user language and test positive, paraphrased, negative, and overlap cases. | A broad router skill is valid when routing is its explicit responsibility and downstream selection is tested. |
| `positive_only_activation_test` | Demonstration proves one expected prompt but not noninterference. | No case shows the skill declining adjacent work. | Include negative and competing-trigger cases proportional to breadth and consequence. | Explicit commands need argument and name collision tests rather than model-selection tests. |
| `optional_folder_cargo_cult` | `README`, references, examples, or scripts are copied because the historical tree lists them. | Files have no link from the main artifact, walkthrough, loader, or test. | Remove them or name the consumer, owner, inclusion rule, and gate. | Staged workshop material is acceptable with a visible completion or deletion condition. |
| `orphan_support_file` | A referenced file is renamed, excluded from packaging, or never loaded. | Link, package inventory, or runtime lookup fails from a clean install. | Verify reachability from source through distributed package and host. | Non-distributed contributor documentation may stay outside the runtime package when labeled. |
| `historical_frontmatter_as_current_schema` | Archived keys and optionality are copied without a current validator. | Target host rejects, ignores, or interprets a field differently. | Inspect current schema and test missing, unknown, malformed, and valid metadata. | A frozen legacy host can retain its historical schema under explicit support scope. |
| `static_inspection_equals_runtime` | Valid Markdown, YAML, or JSON is reported as loaded, activated, and usable. | No host process or user journey observed the capability. | Match file validation, host loading, invocation, behavior, and lifecycle claims to separate gates. | Documentation-only examples may claim static conformance when execution is explicitly out of scope. |
| `live_side_effect_fixture` | The teaching path writes a real repository, account, issue, filesystem, or service by default. | Running the walkthrough changes shared state or requires personal credentials. | Use disposable fixtures, dry-run or preview, confirmation, bounded operations, and cleanup. | A live integration test is valid in an isolated account or repository with owner approval and audit. |
| `credential_in_example` | Tokens, secrets, personal paths, or authenticated state are embedded or expected implicitly. | Package, logs, screenshots, or fixtures contain reusable credentials or identity data. | Use documented secret injection, fake values, redaction, least privilege, and revocation checks. | Public nonsecret identifiers can appear when disclosure and reuse are safe. |
| `permission_happy_path_only` | Example asks for broad access and demonstrates only approval. | Denial, partial access, revocation, or scope mismatch has no recovery. | Request least privilege and exercise deny, cancel, expire, and retry-after-correction paths. | Read-only local fixtures may need no external permission when the boundary is truly absent. |
| `automatic_hook_without_isolation` | A lifecycle event executes code repeatedly, recursively, or during unsupported states. | Reentrancy, duplicate effects, timeouts, host slowdown, or destructive loops appear. | Bound events, make effects idempotent, isolate failures, support disable, and test rollback. | A pure read-only hook can use lighter controls when repeated invocation remains harmless and measured. |
| `nondeterministic_teaching_path` | Network, time, random data, mutable global state, or external rate limits decide the observed result. | Repeated clean runs differ without a declared variable. | Freeze fixtures, seed randomness, isolate clocks and services, and report controlled variability. | A resilience lesson may induce nondeterminism deliberately when the distribution and assertions are explicit. |
| `mock_advertised_as_integration` | A fake server or tool is described under the same name as a supported live capability. | Walkthrough never crosses authentication, transport, permission, or service failure boundaries. | Label the mock, use nonproduction names, and state which integration claims remain open. | A contract-first mock is useful before live access when promotion gates are retained. |
| `protocol_host_conflation` | MCP specification behavior is assumed to prove one host's packaging, transport, auth, or UI. | Protocol fixtures pass while host installation or invocation fails. | Verify protocol and host adapters separately, then run one combined path. | A host may embed a protocol directly, but its integration contract still needs evidence. |
| `manifest_package_divergence` | Declared entries point to files omitted, renamed, or generated differently in the distributed artifact. | Validator passes source tree while clean install cannot load a surface. | Inspect built package contents and load only from the packaged artifact. | Source-only development can defer packaging if distribution is not claimed. |
| `install_without_removal` | Example proves setup but leaves registrations, files, permissions, processes, caches, or state. | Clean removal and reinstall produce different host behavior. | Design disable, uninstall, residue scan, and reinstall alongside installation. | Ephemeral sandbox state may be discarded wholesale when that boundary is explicit and tested. |
| `versionless_host_assumption` | Example omits supported host, protocol, package, or schema versions. | Copiers cannot tell whether failure is misuse or incompatibility. | Record tested versions, compatibility boundary, upgrade trigger, and expiry. | A conceptual static example may avoid version claims while keeping syntax conditional. |
| `copy_without_promotion_review` | Workshop shortcuts become a scaffold or public template without support ownership. | New projects inherit mocks, broad triggers, disabled gates, or stale fields. | Review assumptions, compatibility, security, lifecycle, tests, ownership, and retirement before publication. | A clearly disposable personal snippet can remain unsupported when distribution is prevented. |

A good skill declines unrelated requests and uses only files exercised by its walkthrough. A bad automatic hook modifies real files on every matching event with broad permission and no disable path. An unused `examples` directory is borderline in a staged workshop: it becomes acceptable only when the stage, owner, completion test, and deletion condition are visible.

Use controlled probes: unknown and malformed metadata, positive and neighboring negative prompts, repeated or concurrent invocation, denied and revoked permission, fake credentials, network loss, recursive events, missing packaged files, stale host versions, disable, uninstall, residue, and reinstall. Use disposable repositories, accounts, and services unless live integration itself is the tested capability. A detector earns only the surface and failure timing it exercises.

Cascades matter. An overbroad description can activate an automatic helper on unrelated work, request unnecessary permission, mutate shared state, leave installation residue, and then spread through copied scaffolds. Repair the earliest supported cause and rerun all dependent gates. Repeated lifecycle patches often indicate that the example combines too many surfaces or claims a distribution contract it does not own.

## Verification Gate Command Set

Run the focused assignment verifier from the repository root after changing this reference and packet:

```bash
python3 tests/verify_idiomatic_reference_file.py --path idiomatic-ref-202607/example_plugin_demonstration_patterns-20260710.md
```

Then run the shared generation contract:

```bash
python3 agents-used-monthly-archive/idiomatic-references-202606/tools/verify_reference_generation.py --stage final
```

These commands verify the reference-evolution workflow. They do not validate a contemporary skill schema, load a host, select a trigger, invoke a command, run a hook, connect an MCP server, inspect permissions, install a plugin, or remove its residue.

For target implementation, discover the actual extension artifacts and host commands before choosing gates:

```bash
rg --files | rg '(^|/)(SKILL\.md|plugin\.json|package\.json|\.mcp\.json|commands?|hooks?|skills?|scripts?|tests?|examples?|references?)(/|$)'
```

Inspect the target host's help, version, schema or validator, project instructions, package builder, test scripts, and clean-environment workflow. A filename match is only discovery. Do not report a validator, installer, or invocation as run when it was guessed or unavailable.

| Claim | Required gate | Passing observation | Limit |
|---|---|---|---|
| Historical source was interpreted accurately. | Reopen the frozen `SKILL.md` region and compare the bounded claim, duplicate hash, and caveat. | Exact observation and one-source/two-location provenance agree. | Historical accuracy does not establish current host support. |
| Artifact schema is valid. | Run the current target-host parser or validator against accepted, missing-required, unknown, and malformed examples. | Valid candidate passes and invalid fixtures fail with useful bounded diagnostics. | Schema acceptance does not prove host loading or behavior. |
| Minimal file closure is real. | Trace every file from host requirement or walkthrough, scan links, and inspect generated package contents when distributed. | No required file is missing and no shipped runtime file is unreachable or unexplained. | Reachability does not prove correct content or safe execution. |
| Host discovers and loads the surface. | Start or refresh an isolated supported host with only the candidate installed or linked. | Host reports or exposes the intended surface without relying on personal cached state. | Discovery does not prove selection, output, or permissions. |
| Skill activation is bounded. | Run realistic positive phrases, paraphrases, neighboring negative requests, overlapping skills, and repeated requests. | Intended requests select the skill and unrelated requests remain unaffected under the declared routing policy. | A finite matrix cannot establish every natural-language phrasing. |
| Explicit command behavior is coherent. | Exercise help, valid arguments, missing and invalid input, cancellation, repeat, and output destination. | Invocation and errors match the user contract and do not mutate undeclared state. | Command tests do not cover automatic host events or plugin installation. |
| Hook automation is isolated. | Trigger matching and nonmatching events, reentrancy, concurrency, timeout, failure, disable, and rollback in a disposable workspace. | Events are bounded, repeated effects follow policy, host remains usable, and disable stops execution. | A fixture cannot reproduce every production timing interleaving. |
| MCP boundary is compatible. | Validate current protocol messages and exercise capability discovery, authentication or permission, malformed input, transport loss, cancellation, and shutdown. | Server and client agree on supported capabilities and fail without leaking or hanging. | Protocol success does not prove host packaging or service-specific safety. |
| Permission is least and denial is recoverable. | Run approved, denied, revoked, expired, and partially scoped cases with fake or isolated identities. | Requested scope matches the operation, denial is safe, and no partial undeclared effect remains. | Local mocks cannot prove live provider policy. |
| Fixture behavior is deterministic and bounded. | Run from a clean state repeatedly with controlled clock, randomness, network, filesystem, and service fixtures as applicable. | Declared output and state changes repeat; controlled variability is reported; cleanup restores the baseline. | Determinism can be intentionally relaxed for a measured resilience lesson. |
| Package and manifest agree. | Build from a clean tree, inspect the artifact, validate declared entrypoints, and load only the built package. | Every entry exists in the package and no credential, development-only file, or unexplained executable ships. | A correct package can still behave incorrectly after load. |
| Install and removal are symmetric. | Exercise clean install, load, upgrade or replacement, disable, uninstall, residue scan, reinstall, and host restart where required. | Supported state transitions work and removal leaves only explicitly retained user data. | Lifecycle commands and locations are host-specific and must be discovered. |
| Copied template remains honest. | Scaffold or copy into a clean fixture and run the documented path without hidden author state. | Assumptions, versions, commands, limitations, and failure recovery are sufficient for another user. | One copier cannot represent all environments or learning styles. |

Use fast source, schema, and link checks during construction. At candidate state, run host load, positive and negative invocation, deterministic behavior, permission denial, and surface-specific failure gates. Before claiming distribution, add package inventory, clean install, compatibility, upgrade, removal, residue, and reinstall. Stop downstream lifecycle work on an unexplained schema failure, missing entrypoint, or unsafe fixture; fix the earliest boundary and rerun its dependents.

A useful evidence packet records working directory, candidate identity, target host and version, exact command, environment or sandbox, credentials class without secret value, fixture state, result summary, retained output, claim supported, and limitation. "Validation passed" without those details does not prove loading or invocation. Keep at least one negative activation, denied permission, malformed input, repeated run, missing package file, or removal-residue case as a regression fixture when that risk applies.

## Agent Usage Decision Guide

Use the learner outcome, invocation semantics, side effects, and lifecycle claim rather than keywords to route the task.

| Usage mode | Choose when | Minimum action | Boundary |
|---|---|---|---|
| Primary skill demonstration | The deliverable teaches one model-invoked contextual capability and the local `SKILL.md` pattern is relevant. | Define goal and non-goal, inspect current host schema, build the minimal skill, test positive and negative activation, and verify visible guidance behavior. | This reference coordinates the complete teaching artifact; current host guidance owns exact syntax. |
| Surface companion | A command, hook, setting, or MCP surface is selected but the deliverable remains a bounded example. | Keep one capability contract, obtain specialist schema and runtime guidance, isolate fixtures, and return a tested surface artifact plus failure semantics. | Specialist guidance owns production mechanics; this reference owns minimality, walkthrough, and safe copyability. |
| Package lifecycle profile | Proven inner surfaces need an installable and removable wrapper. | Discover current manifest and builder, inspect package closure, test clean install, load, permissions, compatibility, disable, removal, residue, and reinstall. | A directory name or source-tree validator is insufficient distribution evidence. |
| Integration demonstration | The lesson intentionally crosses a live or emulated external service. | Define least privilege, fake or disposable environment, authentication and denial, bounded effects, transport failures, audit, and cleanup. | Production security, service operations, and incident response route to accountable specialists. |
| Promotion review | A workshop example will become a scaffold, published template, marketplace artifact, or supported dependency. | Review assumptions, host versions, names, triggers, permissions, mocks, lifecycle, compatibility, ownership, support, migration, and retirement. | No disposable shortcut becomes a default silently. |
| Orientation only | The user is comparing surfaces or reading the historical corpus without creating an artifact. | Produce a decision and unresolved evidence list; do not claim installation or invocation. | Implementation and lifecycle gates remain unrun. |
| Avoid as primary | The decisive work is production plugin engineering, privileged automation, protocol conformance, security architecture, incident response, marketplace policy, or a generic extension unrelated to demonstration quality. | Open the specialist reference and attach only the bounded example or copyability checks that still matter. | Do not let the historical skill substitute for current production authority. |

Before creating files, record:

- the learner, user request, successful observation, non-goal, accidental-invocation consequence, and failure recovery;
- the target host and version, current schemas, supported surfaces, file locations, validators, help, package builder, and lifecycle commands actually discovered;
- who invokes the capability, whether invocation is explicit or automatic, and how repeated, concurrent, cancelled, and unrelated requests behave;
- every filesystem, shell, network, repository, identity, process, or service side effect and its permission, isolation, confirmation, audit, and cleanup owner;
- whether the artifact is static, runnable, installable, published, supported, or disposable, and what evidence makes that status true;
- the exact structure, host-load, activation, behavior, denial, package, compatibility, removal, and copyability gates the change can invalidate.

A reduced static profile can omit runtime and install evidence, but it must say that it is conceptual and cannot be reported as loaded or usable. Re-run routing when a support script begins executing, a skill gains a command or hook, a mock becomes live, external credentials appear, a wrapper is added, another project copies the example, or support ownership changes.

Stop before claiming a real extension when the target host is unknown, current schema has not been inspected, invocation behavior cannot be observed, neighboring triggers are undiscovered, a side effect lacks isolation and cleanup, required permission is unowned, package files cannot be enumerated, or removal cannot restore a known state. An exploratory mock may proceed under a distinct nonproduction name and fixture, with a convergence gate; it cannot claim live compatibility.

Good routing uses the primary profile for a narrow skill-trigger lesson and adds current host evidence. Bad routing opens this reference to deploy a privileged GitHub MCP server in production. A real manifest wrapping the skill is borderline: retain this reference for teaching quality, add package-lifecycle guidance, and withhold installable status until the built artifact loads and removes cleanly.

Retain a routing record containing learner goal, user behavior, target host, chosen surface, side effects, permissions, distribution status, source evidence, selected profile, companions, rejected profiles, first probe, gate set, and reversal condition. The route remains provisional until a current host load and representative user path confirm it. A correct route minimizes duplicated walkthroughs while assigning schema, runtime, security, package, lifecycle, and support evidence to explicit owners.

## User Journey Scenario

Use this hypothetical journey to hold one learning outcome constant: a platform builder wants a small example that answers requests such as "show me the structure of a focused plugin skill" and "help me write a skill description that triggers correctly." The example should not activate for "deploy a GitHub MCP server" or "add a repository hook." Its result is deterministic guidance containing a purpose, applicability boundary, minimal ASCII tree, ordered authoring steps, and verification plan. It performs no external side effect.

| Phase | Action | Evidence to retain | Rework or stop condition |
|---|---|---|---|
| Discover | Identify the target host and version, current skill schema or validator, supported paths, reload behavior, neighboring skills, and whether a distribution wrapper is required. | Direct host or project artifacts, exact commands available, and current example behavior. | Stop current-host claims when schema, loader, or required wrapper cannot be identified. Continue only as a labeled static sketch. |
| Specify the lesson | State learner, representative positive requests, neighboring negative requests, expected answer shape, non-goals, and absence of external side effects. | Frozen capability contract and one rejected broader interpretation. | Split or reroute if the lesson also needs an explicit command, automatic hook, or external tool behavior. |
| Select the surface | Choose a model-invoked skill because contextual guidance is the behavior being taught. | Surface decision and comparison with the nearest alternative. | Reopen when users require deliberate invocation or host events rather than contextual selection. |
| Build the minimum | Start with one target-valid `SKILL.md`. Use an ASCII tree in the guidance and add no support directory yet. | Candidate tree, file ownership, schema or parser result, and clean diff. | Remove or justify every file that the host or walkthrough does not reach. |
| Write activation metadata | Use bounded, realistic user language for skill-format and trigger-design requests. Avoid generic plugin, tool, or development terms as sole cues. | Description candidate, positive phrases, paraphrases, negative neighbors, and overlap map. | Narrow when unrelated requests select the skill or another skill owns the same phrases. |
| Write the body | Give purpose, applicability, minimal structure, ordered decisions, one concrete example, failure cautions, and target-host verification. | Review against the frozen lesson and source-region caveats. | Rework if the body advertises unsupported fields, folders, commands, hooks, servers, permissions, or install behavior. |
| Validate structure | Run the discovered target validator or parser, link checks, ASCII and unresolved-token scans, and minimal-file closure review. | Exact command, host version, result, and limits. | Static success cannot advance to loaded or installable status by itself. |
| Load and exercise | Refresh an isolated host, run positive and paraphrased requests, neighboring negative requests, overlap, and repeated invocation. | Selection and nonselection observations plus the resulting answer shape. | Return to metadata when routing fails; return to the body when selection is correct but guidance is wrong. |
| Test clean copying | Move or scaffold the candidate into a clean fixture with no author-specific state and repeat the documented path. | Required context, commands, output, and unresolved environment assumptions. | Remove hidden paths, personal config, cached state, or undocumented steps. |
| Decide distribution | Keep the result a skill demonstration unless the actual host and user goal require a wrapper. | Explicit status: static, host-loaded, or distributable, with evidence for that exact level. | Do not claim install, upgrade, permission, removal, or reinstall until those paths exist and run. |
| Handoff and refresh | Retain the accepted file, trigger matrix, rejected expansion, target-host evidence, owner, and invalidation triggers. | Compact evidence packet and promotion decision. | Reopen after host schema, neighboring skills, wrapper, permissions, or support scope changes. |

The simplest candidate is one file:

```text
skills/
`-- example-skill/
    `-- SKILL.md
```

This tree is a teaching shape, not a universal current installation path. Use the actual target location found during discovery. Add `references`, `examples`, or `scripts` only when the walkthrough needs material that should not live in the main skill, and then prove links, package inclusion, execution safety, and cleanup as applicable.

A good result loads in the inspected host, answers the representative skill-format intents with the promised bounded guidance, declines the MCP and hook requests, contains no unreachable support file, and can be reproduced from a clean fixture. A bad result triggers on any mention of plugin, displays Unicode copied from the archive despite the ASCII requirement, and claims commands, MCP tools, install, and removal that do not exist. A wrapper is borderline: it becomes part of the journey only after current manifest validation, built-package inspection, clean install, load, denied permission when relevant, disable, removal, residue, and reinstall are observed.

This journey is a worked decision model, not evidence of a contemporary host API or measured teaching outcome. Its durable product is the accepted capability contract, minimal artifact, activation and nonactivation matrix, observed host scope, clean-copy path, one useful rejected design, and the conditions that require the lesson or lifecycle claim to be revisited.

## Decision Tradeoff Guide

Make each choice against a fixed learning contract and current target host. State what the learner should understand or observe, then run the smallest host-compatible candidate. Add a file, surface, privilege, external dependency, or wrapper only when it owns a demonstrated responsibility or enables evidence the baseline cannot provide.

| Decision boundary | Lightweight default | Choose the stronger alternative when | Cost or failure if misapplied | Verification and reversal signal |
|---|---|---|---|---|
| Contextual skill or explicit command | Use a skill when the model should apply guidance from task context. | Use a command when users need deliberate named invocation, arguments, and predictable help or error behavior. | A broad skill can activate unexpectedly; a command can add ceremony and be undiscoverable in natural workflow. | Test positive and negative selection for a skill or help, valid, invalid, and cancellation paths for a command. Reopen when invocation intent changes. |
| One file or linked support material | Keep the complete bounded lesson in one `SKILL.md`. | Move stable detail into references or examples when it has a distinct reader, format, size, or maintenance lifetime and the main file links to it. | One file can become noisy; split files can become unreachable, stale, or omitted from packaging. | Trace every link from a clean copy and remove the split when no independent responsibility remains. |
| Static or runnable demonstration | Prefer static structure and deterministic text when execution adds no teaching value. | Add a runnable fixture when the user outcome depends on transformation, host behavior, protocol, timing, or side effects. | Static prose can overclaim behavior; runnable code adds environment, permission, security, determinism, and cleanup obligations. | Run from a clean isolated state and compare the observation with the lesson. Revert to static when execution proves no distinct claim. |
| Mock or live integration | Use an unmistakably named fake for protocol shape and failure rehearsal before live access. | Use a live isolated service when authentication, provider behavior, quotas, permissions, or real compatibility is the lesson. | A mock can be mistaken for integration; live examples can leak credentials or mutate shared state. | Test contract divergence, denial, network or service failure, bounded effects, audit, and cleanup. |
| Manual artifact or scaffold generator | Write the smallest file manually when the host contract is simple and transparent. | Use generation when the host or organization owns a reproducible schema and copied volume makes drift cost material. | Manual copies diverge; generators can hide defaults, ship extra files, or encode stale schema. | Generate from a clean state, inspect contents, diff, validate, load, and remove unexplained output. |
| One surface or composed extension | Teach one primary skill, command, hook, server, or setting. | Compose surfaces only when each owns a distinct step in one user lifecycle and their handoff is observable. | A showcase package creates overlap, privilege, state, and failure combinations learners cannot reason about. | Remove one surface and rerun the contract; if no relevant evidence fails, composition lacks justification. |
| Local fixture or external dependency | Use checked-in synthetic data and disposable local state. | Add network or service dependency when external behavior itself is under test and an isolated account or sandbox exists. | Local fixtures can miss provider reality; external dependencies introduce flakiness, quotas, credentials, privacy, and cleanup. | Compare contract fixtures with one bounded live path and retain a safe offline fallback for teaching where appropriate. |
| Implicit default or configurable setting | Keep behavior fixed and explicit in a small lesson. | Add a setting when users have a stable legitimate choice whose default, scope, precedence, validation, migration, and rollback are teachable. | Configuration multiplies states and can hide commands or secrets. | Test missing, valid, invalid, conflicting, migrated, and reset states; remove configuration if no real choice remains. |
| Unwrapped artifact or plugin package | Keep a skill or other inner artifact unwrapped when the lesson does not claim distribution. | Add a wrapper when the target host requires it or several proven surfaces need one install, version, permission, and removal lifecycle. | A wrapper can create false installability, missing files, version skew, and residue. | Validate manifest and package, load from the built artifact, then exercise install, upgrade, disable, remove, residue, and reinstall. |
| Workshop example or reusable template | Mark a teaching experiment disposable and isolate it from supported names. | Promote after repeated clean-copy use, current-host evidence, security review as applicable, ownership, compatibility, and maintenance are accepted. | Copiers inherit shortcuts as defaults and expect support. | A new user completes the documented path without hidden state; incidents and host changes have owners and regression gates. |

**Adopt, Adapt, Avoid, or Escalate**

- **Adopt** a candidate when the historical responsibility exists in the target lesson, current host accepts the mechanism, and a focused gate demonstrates value.
- **Adapt** it when focus or teaching intent is useful but metadata, path, invocation, package, permissions, or lifecycle differs in the target.
- **Avoid** it when it exists only in the duplicate corpus, adds no distinct lesson, relies on an unrefreshed surface, or cannot name a failure it prevents.
- **Escalate** when the choice introduces live credentials, destructive or automatic effects, external protocol, public distribution, marketplace policy, persistent user state, or supported compatibility.

Good: one target-valid `SKILL.md` teaches a contextual skill and proves activation plus nonactivation. Bad: the same lesson receives a helper script, hook, MCP mock, settings file, and plugin wrapper with no distinct behavior. Borderline: a wrapper is reasonable when the current host requires a manifest, but only after the built package and full lifecycle are tested.

Retain this ledger for a consequential choice:

```text
Learning behavior held constant
Target host evidence and mandatory scaffold
Selected option and responsibility owned
Simpler candidate rejected because
Focused gate and observed result
Permissions, side effects, and lifecycle impact
Known uncertainty or untested environment
Owner and reopen condition
```

This guide does not establish current host APIs, schema, or package commands. Version-sensitive mechanics require target validation and future primary-source refresh where material. Uncertainty should narrow the example, isolate side effects, and make the choice reversible rather than selecting a larger scaffold.

## Local Corpus Hierarchy

The archive `SKILL.md` is **primary historical provenance** for this theme. The working-corpus `SKILL.md` is a **byte-identical duplicate locator**, not independent support. Neither is current project policy or a complete plugin specification merely because it lives beneath a directory named `plugins`.

| Hierarchy role | Assignment test | Permitted use | Promotion, demotion, or retirement trigger |
|---|---|---|---|
| Historical observation | Exact content can be located in the frozen archive. | Describe what the example taught and claimed at that version. | Never promote from archive presence alone; attach current target and behavior evidence. |
| Duplicate locator | Another path contains the same bytes or claim without independent observation. | Find copied repository material and preserve movement history. | Reclassify only when the working artifact diverges and gains its own ownership and evidence. |
| Candidate teaching guidance | The responsibility remains relevant and the source is not internally misleading for the bounded claim. | Seed a capability contract, review question, trigger matrix, or minimal artifact. | Promote after target-host fit, copier review, and focused gates; demote after counterexample. |
| Target project policy | Current schema, code, tests, governance, or support ownership explicitly requires the choice. | Treat as local default inside the documented host and version boundary. | Reopen after host, surface, owner, compatibility, or support changes. |
| Legacy mechanism | The metadata, path, loader behavior, or syntax belongs to an older supported environment. | Explain existing examples and migration constraints. | Retire for new work after legacy hosts and copied consumers leave support. |
| Conflicting evidence | Historical content disagrees with current host, neighboring examples, or observed behavior. | Drive a comparison test and retain the disagreement. | Resolve only with a named contract and reproducible target observation. |
| Negative evidence | An omission or pattern demonstrates a failure worth preventing. | Populate anti-patterns, mutation cases, and promotion review. | Keep while the mistake remains plausible; update when the boundary changes. |
| Reusable template rule | Current repeated use, ownership, support, and regression evidence justify propagation. | Scaffold or publish the bounded default with its limitations and lifecycle. | Demote after host breakage, security concern, copied failure, or loss of owner. |

Apply those roles by source theme:

| Source theme | Role in this reference | Useful contribution | Limitation and required gate |
|---|---|---|---|
| Frontmatter identity and description | Historical observation plus candidate | Names focus and realistic trigger language as design concerns. | Exact fields, optionality, and loader interpretation are version-sensitive; run the current target validator and activation matrix. |
| Skill-versus-command overview | Candidate teaching guidance | Distinguishes contextual model invocation from explicit user invocation at a high level. | It does not define commands, agents, wrappers, or current host composition; inspect the selected surface contract. |
| Applicability bullets | Candidate plus negative evidence | Supplies positive trigger categories for skill creation and understanding. | No neighboring negative, paraphrase, or overlap cases are retained; add target selection and nonselection evidence. |
| Required one-file tree | Candidate with formatting adaptation | Encourages a minimal `SKILL.md` baseline. | Unicode rendering is converted to ASCII and the path is illustrative rather than a current package rule; validate actual host location and load. |
| Optional supporting tree | Conditional candidate | Suggests ways to separate references, examples, documentation, and scripts. | Presence does not establish need, packaging, or script safety; require a consumer, reachability, inclusion, permissions, and cleanup. |
| Frontmatter option list | Legacy or conditional mechanism | Provides historical metadata vocabulary for investigation. | No current schema or invalid-field behavior is sourced; do not promote without target documentation or validator evidence. |
| Effective description pattern | Strong candidate question | Encourages user-language cues and topic boundaries. | Literal sample phrases and keyword lists can overactivate; replace all generic text and test natural-language neighbors. |
| Content guidelines and best practices | Candidate teaching guidance | Emphasizes purpose, applicability, structure, actions, examples, focus, and overlap checks. | These are review prompts, not measured completeness; execute the user journey and clean-copy test. |
| Missing plugin lifecycle | Negative evidence | Shows why an inner skill should not be called an installed plugin by directory context alone. | Another target may provide a wrapper outside this source; discover and test manifest, package, permissions, install, removal, and residue before changing status. |

Good reuse extracts the focus principle, records its historical source, adapts the description, and proves intended activation plus noninterference. Bad reuse treats the optional tree and metadata list as a current scaffold. Borderline reuse adds a helper script: promote it only when a deterministic executable responsibility cannot remain in prose and sandbox, permission, package, and cleanup gates pass.

Use this extraction record for consequential claims:

```text
Archive path, heading signal, and content hash
Exact historical observation
Role: candidate | legacy | conflicting | negative | duplicate
Learner consequence and target host boundary
Current project evidence inspected
Executed gate and result
Unresolved applicability or support risk
Disposition, owner, and refresh trigger
```

Promotion is reversible. A target host can demote a historically useful mechanism without altering the archive, and a legacy path can remain valuable for migration after it stops guiding new examples. Rules that affect published scaffolds, executable scripts, permissions, external services, or package lifecycle need an owner and invalidation trigger; a disposable orientation note can use a lighter record.

## Theme Specific Artifact

Use a **demonstration contract** to reconcile what an example teaches, what invokes it, which files and privileges it needs, which host and lifecycle claims are proven, and whether it is safe to copy. The contract links authoritative artifacts; it does not replace the current host schema, manifest, `SKILL.md`, command or hook implementation, MCP definitions, package inventory, tests, or lifecycle evidence.

| Contract field | Completion rule | Why it matters |
|---|---|---|
| Capability identity | Give the lesson and candidate a stable local name without implying public support. | Connects triggers, tests, package, and feedback while preserving status. |
| Learner and user promise | State who learns, what request is served, and what observable result follows. | Prevents mechanism showcase from replacing the teaching outcome. |
| Non-goals and route-away | Name neighboring requests and production guarantees this example does not own. | Makes noninterference and specialist handoff reviewable. |
| Target environment | Record host, version, schema, loader, validator, supported surfaces, and required refresh behavior actually inspected. | Separates current target evidence from historical syntax. |
| Primary invocation surface | Name skill, command, hook, MCP, setting, or wrapper and who initiates it. | Determines trigger, argument, reentrancy, protocol, and lifecycle gates. |
| Minimal artifact closure | Link every required and optional file, its consumer, package inclusion, owner, and deletion condition. | Prevents missing entrypoints and decorative scaffolding. |
| Behavior and failure contract | State accepted, ignored, invalid, denied, cancelled, repeated, partial, and cleanup outcomes that apply. | Keeps user recovery and side-effect truth aligned. |
| Side effects and permissions | Enumerate filesystem, shell, network, repository, identity, process, or service access plus least privilege and confirmation. | Exposes trust and rollback obligations before execution. |
| Fixture and determinism | Define clean state, synthetic data, clock, randomness, network, credentials class, isolation, and reset. | Makes the walkthrough reproducible and safe. |
| Distribution lifecycle | State whether the artifact is conceptual, source-valid, host-loaded, behavior-validated, integrated, packaged, or promoted. | Stops static validation from becoming installability. |
| Evidence and limits | Link exact commands, observations, reviewers, negative cases, and untested combinations. | Lets a copier reproduce and challenge claims. |
| Ownership and refresh | Name author, support owner, accepted host range, promotion decision, invalidation triggers, and retirement. | Prevents examples from becoming ownerless compatibility promises. |

Use status values precisely:

| Status | Minimum evidence | Claims still prohibited |
|---|---|---|
| Conceptual | Capability, surface rationale, non-goals, and static illustration are explicit. | Current schema, host load, activation, execution, install, or support. |
| Source-valid | Current target parser or validator accepts the minimal files and invalid fixtures fail as expected. | Host discovery, selection, behavior, package, or lifecycle. |
| Host-loaded | An isolated current host discovers the intended surface from clean state. | Correct invocation, output, permissions, distribution, or removal. |
| Behavior-validated | Positive and negative invocation plus applicable failure and side-effect cases match the contract. | Package installation, compatibility, upgrade, or uninstall unless separately exercised. |
| Integrated | A live or faithful protocol or service boundary passes authentication, denial, malformed-input, failure, and cleanup gates. | General production security, scale, and support beyond the tested boundary. |
| Packaged | Built artifact contents match declarations and clean install, load, compatibility, disable, removal, residue, and reinstall pass. | Marketplace, public support, or copied-template quality automatically. |
| Promoted template | Clean copiers succeed; versions, ownership, security, compatibility, migration, support, feedback, and retirement are accepted. | Universal host or learner effectiveness outside the declared scope. |

**Completed example: focused skill-format lesson**

| Contract area | Accepted record |
|---|---|
| Capability identity | `example-skill-format-lesson`, a local teaching candidate rather than a published package name. |
| Learner promise | A plugin author asks how to structure a focused skill or write a bounded description and receives purpose, applicability, a minimal ASCII tree, authoring steps, and verification guidance. |
| Non-goals | It does not deploy MCP servers, create hooks or commands, request repository access, prove plugin installation, or define current host schema without target evidence. |
| Primary surface | Model-invoked contextual skill; an explicit command is rejected because deliberate named execution is not the lesson. |
| Minimum artifact | One target-host-valid `SKILL.md`; no optional support folder until a concrete section exceeds the main lesson's useful scope. |
| Positive cases | Requests to show skill structure, create a focused skill template, or refine trigger descriptions select the lesson under the target routing policy. |
| Negative cases | Requests to deploy a GitHub MCP server, add a repository hook, change generic plugin settings, or operate a live service do not select it as primary. |
| Behavior | The answer uses ASCII, states current-host uncertainty, gives one-file baseline, compares surfaces, and names direct gates without executing external effects. |
| Permissions and effects | No shell, filesystem mutation, network, identity, repository, process, or external service is required by the baseline behavior. |
| Evidence scope | Historical source was read and adapted; target source validation, host load, activation matrix, and clean-copy result must be attached in the concrete project. |
| Current status | Conceptual in this generic reference; it advances only as target evidence arrives. |
| Promotion trigger | Repeated clean-copy use and accepted ownership justify a template review; a real wrapper separately reopens package and lifecycle gates. |

Pair every operational claim with its proof:

| Claim | Direct evidence | Negative or boundary evidence | Unresolved example |
|---|---|---|---|
| Description activates correctly. | Positive and paraphrased requests select the skill in the current host. | Neighboring and overlapping requests remain unselected or route deliberately. | Phrasing outside the sampled language remains uncertain. |
| Files form a closed lesson. | Validator, link scan, walkthrough trace, and package inventory when applicable reach every required file. | A removed support file breaks a named gate; an unused file is excluded. | Host-injected or cached files require separate discovery. |
| Behavior is safe and repeatable. | Clean isolated runs produce the bounded result and restore state. | Invalid, denied, cancelled, repeated, and dependency-failure cases preserve declared state. | Production timing or provider behavior remains outside a local fixture. |
| Wrapper is installable. | Built package loads after clean install and survives supported replacement or upgrade. | Disable, removal, residue, restart, and reinstall return to the declared states. | Other host versions and marketplace policy remain unclaimed. |
| Template is reusable. | A copier with no author state completes the documented path and understands non-goals. | A deliberately omitted step or stale field causes promotion review to fail. | Broader learner comprehension needs repeated feedback rather than one run. |

Reject or repair a contract that copies full schemas, leaves a claimed surface unowned, cites a gate that cannot distinguish statuses, or marks unresolved lifecycle behavior as optional. Use `not applicable` with the architectural reason when a concern cannot occur and `unresolved` with owner and decision trigger when it can.

Refresh the contract when capability, description, neighboring extensions, target host, schema, support files, side effects, permissions, package, lifecycle, support scope, or copied usage changes. Retire it when the example is no longer published, installed, copied, or used as a regression fixture. Authoritative files and executable tests remain after retirement because this artifact coordinates evidence rather than owns behavior.

## Worked Example Set

These examples hold one lesson constant: help a plugin author understand the shape and trigger boundary of a focused skill. They demonstrate semantics and evidence, not a current host schema. Adapt metadata and paths to the discovered target, run its validator, and retain the behavior cases.

**Good example: one bounded skill candidate.** The historical source uses YAML frontmatter, so this sketch keeps that shape for explanation while refusing to claim current support:

```yaml
---
name: skill-format-guide
description: Use for requests to show a focused skill structure, design a skill template, or refine model-invoked skill trigger language.
---
Purpose: Teach the minimum structure and activation boundary of one focused skill.
Applies when: The user is authoring or reviewing contextual skill guidance.
Does not apply when: The user needs a command, hook, MCP deployment, live service operation, or generic plugin installation.
Guidance:
  - Freeze one user goal and one non-goal.
  - Inspect the current target-host schema and path.
  - Start with one skill file and add support material only for a named consumer.
  - Test realistic positive, paraphrased, negative, and overlap requests.
  - Report static, loaded, behavior-validated, and packaged status separately.
```

The exact fields and body format must be validated against the target host. The useful behavior is the bounded description, explicit non-goals, one-file baseline, and direct verification plan.

```text
skills/
`-- skill-format-guide/
    `-- SKILL.md
```

| Request case | Intended result | Failure exposed if result differs |
|---|---|---|
| "Show me the minimum structure for a focused skill." | Select the skill and return purpose, applicability, ASCII tree, ordered steps, and gates. | Missing positive coverage or wrong host loading. |
| "Help me narrow a skill description that triggers on too many requests." | Select the skill and emphasize user-language cues, negative cases, and overlap review. | Body does not fulfill an intended trigger. |
| "Create a plugin skill template for contextual documentation guidance." | Select when template design remains skill-focused; state current-host uncertainty. | Overly narrow trigger or unsupported schema certainty. |
| "Deploy a GitHub MCP server with repository write access." | Do not select this skill as primary; route to current MCP and security guidance. | Broad plugin or skill keywords capture privileged integration work. |
| "Add a pre-commit hook that rewrites files." | Do not select as primary; route to hook safety and repository behavior. | Contextual guidance is confused with automatic execution. |
| "Change a plugin setting precedence rule." | Do not select unless the task is documenting a skill that teaches settings. | Topic overlap replaces capability ownership. |

An acceptable alternative moves a long, stable explanation into `references/skill-format-details.md` when the main skill links to it, a clean copy includes it, and target loading or author workflow proves the separation helps. An `examples` folder is justified when several concrete inputs are directly exercised. A helper script is not an equivalent formatting choice; it introduces executable, permission, determinism, package, and cleanup obligations.

**Bad example: directory theater.** A folder named `example-plugin` contains `SKILL.md`, empty `commands`, `hooks`, and `scripts` directories, an MCP configuration copied from another project, and a README claiming install and uninstall. The lesson teaches that presence implies support. A learner can copy excessive permission, invoke nothing, ship unreachable files, and discover removal residue only after installation. Repair by returning to the capability contract, deleting unsupported surfaces, and rebuilding evidence from the one-file baseline.

**Bad example: keyword-only confidence.** A test checks whether the string `skill` appears in the user request and calls every match successful. That validates a different router from a model-selected target host, ignores paraphrases and neighbors, and cannot establish noninterference. Keep a lightweight lexical unit only if it is the actual production mechanism; otherwise run the target selection path and record its limits.

**Borderline example: required plugin wrapper.** Suppose target discovery shows that a valid wrapper is mandatory around the skill. The wrapper is acceptable only after these claims advance independently:

| Wrapper claim | Required evidence | Status before evidence |
|---|---|---|
| Manifest or package schema is current. | Target-host validation with valid, missing, unknown, and malformed fixtures. | Unresolved, not inferred from the archive directory. |
| Built package contains the skill. | Clean build, inventory, entrypoint resolution, and credential or development-file scan. | Source tree only. |
| Host installs and loads it. | Clean isolated install and host discovery using documented current commands. | Not installable. |
| Permissions are bounded. | Approved, denied, revoked, and partial-scope cases for any requested access. | No permission assurance. |
| Removal is clean. | Disable, uninstall, host restart, residue scan, reinstall, and explicit retained-data policy. | No lifecycle assurance. |
| Copiers can reproduce it. | Another user runs the complete path without author config or cached state. | Workshop candidate, not promoted template. |

| Claim protected by the worked set | Minimum adapted gate | Expected disconfirming failure |
|---|---|---|
| Description is bounded. | Current-host positive, paraphrased, negative, and overlap activation matrix. | A privileged or unrelated request selects the skill. |
| One-file baseline is complete. | Schema validation, link scan, host load, and clean-copy walkthrough. | Hidden author state or a missing undeclared support file is required. |
| Answer teaches the promised lesson. | Review the actual host-produced response against purpose, non-goals, ASCII tree, ordered actions, and gates. | Selection succeeds but guidance advertises unsupported mechanisms. |
| Optional material earns its place. | Remove or exclude each support file and run the consumer or package check. | No relevant observation changes, proving the file is decorative. |
| Distribution status is honest. | Package, install, compatibility, disable, removal, residue, and reinstall evidence when claimed. | A source validator passes while the built package cannot load or cleanly remove. |

These examples establish information preservation and review shape, not that the shown metadata compiles in every host. When copied artifacts evolve, retain a current-host adapter and explicit status rather than silently editing the historical example. A strict current validator and a documented migration path for legacy examples can coexist when each supported form normalizes to the same bounded capability contract.

## Outcome Metrics and Feedback Loops

Measure whether the demonstration teaches a bounded capability and can be reused without importing hidden author state. File count, invocation count, and authoring time can describe effort, but none of them establishes that the example selects the right requests, produces the promised result, avoids unrelated work, or cleans up after installation. A useful measure therefore names its population, evidence source, artifact status, observation window, owner, blind spot, and the design decision it can change.

Do not import a universal success percentage into a new host. Establish a local baseline from deterministic fixtures and classified copier feedback first. Define a threshold only after the denominator and collection path are stable. It is acceptable to record that no baseline exists; that statement is more actionable than an unsupported target because it identifies the next measurement task.

| Outcome | Definition and denominator | Evidence | Decision enabled | Principal blind spot |
|---|---|---|---|---|
| Capability-contract conformance | Claimed behaviors that have matching passing observations, divided by all claimed behaviors | Claim-to-gate matrix and focused verification run | Repair an uncovered claim or narrow the contract | A passing adapter can still teach the wrong abstraction |
| Positive activation | In-scope requests that select the intended surface, divided by all reviewed in-scope requests | Versioned positive trigger fixtures on the target host | Refine descriptions, examples, or host registration | Synthetic language may not represent actual requests |
| Noninterference | Out-of-scope and adjacent-surface requests that do not select the demonstration, divided by all reviewed negative requests | Negative and overlap trigger fixtures | Narrow activation or add an explicit handoff | The sampled negatives may miss a new neighboring feature |
| Behavior completeness | Selected cases that produce every promised output and recovery observation | Output-shape, failure-path, and mutation tests | Repair implementation or reduce the promise | A mock can conceal live integration failure |
| Clean-copy completion | Independent copy attempts that succeed from a documented clean state, classified by first failure | Disposable workspace rehearsal and copier notes | Remove hidden state or improve the smallest complete example | A small reviewer group cannot establish broad usability |
| File closure | Referenced files and paths that exist in the copied package, divided by all references | Link and package traversal from the declared entry point | Add the missing support file or remove the reference | Runtime-created resources require a separate contract |
| Deterministic fixture result | Repeated runs with the same declared inputs that yield the same asserted result | Isolated repeated execution with cache and environment controls | Seed randomness, freeze data, or label environmental variance | Stable output does not prove semantic correctness |
| Side-effect containment | Runs with no undeclared file, network, process, credential, or configuration effect | Before-and-after resource inventory and denied-capability run | Remove the effect, request the capability explicitly, or isolate the example | Instrumentation may not observe every host-managed effect |
| Permission recovery | Denied-permission cases that fail clearly and leave the environment recoverable | Least-privilege and denial fixtures | Improve preflight, error guidance, and cleanup | A simulated denial may differ from host enforcement |
| Package closure | Declared package contents whose dependencies and entry points resolve in a clean host | Built-artifact inspection and clean-host load | Fix packaging or keep the artifact source-valid only | A load test alone does not prove useful behavior |
| Lifecycle symmetry | Install mutations that removal reverses, except explicitly retained user data | Pre-install, post-install, and post-remove comparison | Repair uninstall, document retained state, or block promotion | Host caches may require a separately documented reset |
| Copied-template escape | Copied descendants that reproduce a known lesson defect after its repair | Repository search, support classification, and migration sampling | Publish migration guidance and strengthen regression gates | Unreported private copies remain invisible |
| Diagnosis interval | Elapsed time from a reproducible copied failure report to a classified cause and protected correction | Issue history with environment and version fields | Improve diagnostics, ownership, or observability | Faster diagnosis does not imply fewer defects |
| Host compatibility | Supported host-version combinations that pass the declared status gate | Version matrix on clean environments | Restrict support, add an adapter, or schedule migration | The matrix cannot cover every local configuration |

**Evidence levels.** Keep evidence commensurate with the artifact's status. A conceptual sketch can be reviewed for contract clarity and misleading implications. A source-valid example can pass metadata, file-closure, and static safety checks. A host-loaded example must add discovery and load evidence. A behavior-validated example must exercise positive, negative, output, and failure cases. An integrated example adds the dependency, permission, and cross-surface checks that its capability activates; a packaged example adds built-artifact, installation, removal, and clean-host evidence. Promotion to a reusable template also requires a clean-copy rehearsal and a migration owner. Passing a lower level must never be reported as evidence for a higher one.

**Fast authoring loop.** After each edit, run the focused reference verifier, ASCII and whitespace checks, fence and table checks, and claim-to-file closure checks. For a target implementation, add metadata validation and deterministic fixtures at the same cadence. These gates should identify mechanical or contract drift before a reviewer has to reconstruct intent. A deliberate mutation, such as broadening a trigger or removing a required support file, should fail the relevant gate; otherwise the test may be observing the wrong boundary.

**Host-validation loop.** On a disposable target host, test discovery, positive activation, adjacent negative activation, output shape, unsupported input, denied permission, and recovery. Record the host and schema version with the observation. Do not retain private request text merely to compute activation statistics; classify intent using the minimum data needed. Test an absent-signal path as well, because broken collection can otherwise look like quiet success.

**Copier loop.** Give an independent reviewer the documented starting state and desired outcome without the author's shell history, untracked files, caches, or credentials. Record the first blocking assumption, the repair attempted, and whether the copied artifact still represents the same lesson. Disagreement between host fixtures and copier results is valuable: it often exposes hidden author context, an undocumented prerequisite, or wording that implies a capability the implementation does not have.

**Package and lifecycle loop.** Inspect the built artifact rather than only the source tree. Install it into a clean environment, verify declared entry points and dependencies, run the bounded behavior cases, remove it, and compare state. Classify retained user data separately from accidental residue. Where the source is intentionally not packaged, mark lifecycle outcomes as not claimed rather than treating them as implicitly successful.

**Promotion, demotion, and retirement.** Promote a demonstration only when its evidence level matches its public claim and ownership exists for compatibility changes. Demote it when the host loader, schema, permissions, or package path can no longer be reproduced. Retire it when the lesson has moved to a maintained template, the target surface is unsupported, or copied defects cannot be corrected safely. A demotion note should state what remains useful, which observations no longer hold, and what users should choose instead.

Pair each attractive outcome with a counter-measure. Positive activation without noninterference can reward an overbroad description. Fast clean-copy completion without side-effect review can reward hidden privilege. A successful install without removal comparison can conceal residue. Short diagnosis time without defect classification can reward repetitive failures. High invocation volume can reflect accidental capture rather than teaching value. These pairs make local optimization visible before it changes the demonstration's meaning.

Feedback should update three artifacts, not merely a dashboard: the example, the focused gate that prevents recurrence, and any migration note needed by copied descendants. Preserve versioned metric definitions when denominators or status levels change; overlap old and new definitions long enough to explain discontinuity, then retire the obsolete measure. The long-term objective is a shorter, well-evidenced path from a copied failure to a corrected lesson, a regression check, and a clear migration decision.

## Completeness Checklist

Completeness is relative to the demonstration's declared lesson, surface matrix, and evidence status. A conceptual sketch does not need to install, but it must not imply that it installs. A packaged example does need clean-host installation and removal evidence because the package claim activates those obligations. Record one of four outcomes for every applicable gate:

| Outcome | Meaning | Required record |
|---|---|---|
| Pass | The claimed observation was reproduced at the declared status | Evidence location, environment or review basis, and date |
| Fail | The observation contradicted the claim or could not be reproduced | Blocking consequence, owner, and repair or scope-reduction decision |
| Not claimed | The gate belongs to a surface or status the demonstration explicitly excludes | The exclusion in the capability contract |
| Time-bounded exception | The risk is accepted temporarily without presenting the gate as passed | Owner, consequence, expiry, and replacement evidence |

An empty result is not equivalent to Not claimed. Determine applicability from the capability contract before evaluating evidence. Aggregate completion is allowed only when every applicable gate passes or has an approved, visible, time-bounded exception whose consequence is acceptable for the publication audience. An exception cannot substitute for claim traceability, status fidelity, secret safety, containment of destructive effects, recovery closure, or evidence health; lower the claimed status or block publication when one of those categorical boundaries fails.

**Universal teaching-contract gates**

| Gate | Completion evidence | Failure response |
|---|---|---|
| Audience and starting state | The role scenario names the learner, available tools, assumed knowledge, starting files, and prohibited hidden state | Narrow the audience or supply the missing prerequisite |
| Decision outcome | The reference states the exact choice the learner should be able to make after using the example | Replace feature narration with an observable decision and consequence |
| Capability boundary | A surface matrix identifies what the example teaches, coordinates with, and explicitly does not provide | Remove ambiguous directory or plugin-wide implications |
| Status declaration | The artifact is labeled conceptual, source-valid, host-loaded, behavior-validated, integrated, packaged, or promoted | Lower the status to the highest evidenced level |
| Minimality | Every included file and surface supports the primary lesson or a necessary verification path | Remove decorative surfaces or split a composition lesson explicitly |
| Evidence hierarchy | Canonical, supporting, duplicate-locator, contextual, and unrefreshed sources have distinct claim roles | Downgrade unsupported claims and stop counting duplicate files as corroboration |
| Currentness boundary | Target-owned schema, loader, command, hook, permission, and package facts cite a current authoritative source or remain conditional | Refresh the authority or mark the adapter unknown |
| Decision alternatives | Adopt, adapt, avoid, and escalation conditions identify the cost of a wrong choice | Add the nearest viable alternative and its tradeoff |
| Good example | A bounded example shows input, expected selection, output, and relevant evidence | Add enough context for review without reconstructing every source |
| Negative example | An adjacent or out-of-scope case shows nonselection, handoff, or explicit refusal | Add a case that can reveal overbroad activation or capability theater |
| Borderline example | A conditional choice identifies the missing fact that changes the decision | Replace vague caution with a discriminating observation |
| Failure and recovery | Credible malformed input, unavailable host, missing file, and unsupported-surface paths state safe outcomes | Add actionable failure classification and recoverable next state |
| Verification mapping | Each important claim maps to a review, static gate, fixture, host observation, or lifecycle drill | Narrow any claim that has no feasible disconfirming observation |
| Metrics and counter-metrics | Each retained outcome names denominator, evidence, owner, action, and likely gaming path | Remove vanity counts or pair them with a boundary measure |
| Adjacent routing | The reference directs nonmatching work to a more appropriate extension or template reference | Add routing before users copy the wrong surface pattern |

**Source-valid artifact gates**

These gates apply when the reference presents files as syntactically or structurally usable, even if the target host has not loaded them.

| Gate | Completion evidence | Failure response |
|---|---|---|
| Required-file closure | Every required path in the tree exists, is included in the artifact, and has a defined role | Add the file, correct the path, or remove the reference |
| Optional-file justification | Each optional support file solves a named complexity that the entry file should not absorb | Inline small content or explain the split boundary |
| Metadata adaptation | The candidate metadata is checked against the selected target's current schema | Label an illustrative schema as illustrative until adapted |
| Link and example closure | Local links, commands, snippets, and referenced fixtures resolve from a clean copy | Repair the link or remove the unsupported instruction |
| Text hygiene | The artifact passes ASCII policy, whitespace, fence, table, and prohibited-marker checks | Correct the mechanical defect before broader review |
| Secret and identity safety | Examples contain no credential, private endpoint, personal path, or realistic secret-shaped value | Replace sensitive material with an obviously inert fixture and scan again |
| Deterministic inputs | Time, randomness, network data, locale, and host state are fixed, injected, mocked, or declared variable | Control the input or reduce the repeatability claim |
| Copy boundary | The smallest complete set can be copied without relying on untracked author files or shell history | Package the missing support or document an explicit prerequisite |

**Host-loaded and behavior-validated gates**

These gates activate only after the target host and its authoritative validation mechanism are selected.

| Gate | Completion evidence | Failure response |
|---|---|---|
| Discovery | A clean host identifies the intended entry point using the documented registration path | Correct registration or retain source-valid status only |
| Positive activation | Representative in-scope requests select the intended surface | Refine description, examples, or host adapter |
| Negative activation | Adjacent and unrelated requests do not select it unless explicit routing is the lesson | Narrow the trigger or add a tested handoff |
| Overlap behavior | Requests matching neighboring extensions resolve predictably and visibly | Establish precedence, composition, or refusal rules |
| Output contract | Selected cases produce the promised structure, content, and durable effects | Repair behavior or narrow the promise |
| Unsupported input | Invalid or unsupported requests fail clearly without fabricated success | Add validation and a recovery route |
| Denied capability | Filesystem, network, process, or credential denial leaves a clear, recoverable state | Reduce privilege or improve preflight and cleanup |
| Mutation sensitivity | Deliberately broadening a trigger, removing a file, or changing an asserted output causes a focused failure | Strengthen a gate that currently observes the wrong boundary |
| Environment record | Host, schema, dependency, platform, and relevant configuration versions accompany the result | Reproduce in a declared environment before compatibility claims |

**Integration and package gates**

Apply only the rows supported by the declared surface. A static skill-format example without a distribution wrapper records these as Not claimed; it does not silently pass them.

| Gate | Completion evidence | Failure response |
|---|---|---|
| Dependency closure | All declared runtime and build dependencies resolve from the built artifact in a clean environment | Correct packaging or keep the artifact unintegrated |
| Least privilege | Requested permissions are the minimum required by tested behavior and denial is handled | Remove excess capability or isolate privileged behavior |
| Side-effect inventory | Files, processes, network calls, configuration changes, and retained data match the contract | Eliminate, mock, or explicitly document each extra effect |
| Clean installation | The documented installation path works without author caches, private registries, or undeclared tools | Repair the package or add a justified prerequisite |
| Upgrade behavior | Supported prior versions migrate or fail with a clear compatibility decision | Add migration, version restriction, or replacement guidance |
| Removal symmetry | Uninstall reverses installation mutations except explicitly retained user-owned data | Repair cleanup and document intentional retention |
| Failure rollback | Interrupted install, load, invocation, or removal leaves a recoverable state | Add transactional behavior, idempotent repair, or manual recovery |
| Cross-surface composition | Commands, hooks, services, settings, or wrappers cooperate according to the declared interaction | Split unrelated surfaces or add interaction tests |

**Reusable-template and publication gates**

| Gate | Completion evidence | Failure response |
|---|---|---|
| Independent copy rehearsal | A reviewer reaches the intended result from the documented clean state without author assistance | Remove hidden assumptions and repeat the rehearsal |
| Template parameter boundary | Values intended for change are distinguished from stable capability and package identity | Add validation and prevent accidental identity collisions |
| Maintainer ownership | A named role owns host refreshes, security reports, copied defects, and retirement | Keep the artifact local until ownership exists |
| Compatibility statement | Supported hosts and versions are explicit and backed by the declared evidence level | Narrow support or add the missing matrix observation |
| Copied-descendant response | Known reusable descendants receive correction and migration guidance when the lesson changes | Publish a migration note and strengthen regression coverage |
| Promotion criteria | Public reuse requires evidence beyond a polished source tree, including copy and lifecycle gates where applicable | Demote the artifact to a workshop example |
| Retirement route | Superseded or unsupported examples identify the maintained replacement and safe removal path | Keep a discoverable tombstone rather than silently deleting guidance |

**Completion sequence**

1. Freeze the audience, teaching outcome, capability matrix, non-goals, and target status.
2. Review source roles and mark any current target mechanics that still need authoritative adaptation.
3. Complete universal contract gates before adding optional files or additional surfaces.
4. Validate source closure, deterministic fixtures, secrets hygiene, and clean-copy boundaries.
5. Bind semantic checks to target-owned validators only when a host has been selected.
6. Run positive, negative, overlap, output, failure, and deliberate-mutation cases at the claimed behavior status.
7. Activate permission, dependency, package, upgrade, rollback, and removal gates only for corresponding claims.
8. Rehearse independent copying before presenting the artifact as a reusable template.
9. Record owners, versions, evidence locations, exceptions, refresh triggers, and the nearest replacement.
10. Reread the artifact as a skeptical learner and remove any implication that exceeds the recorded status.

The release record should state the highest evidenced status and list lower or excluded claims explicitly. This prevents a green static check from being retold as runtime validation and prevents a successful load from being retold as safe installation. The checklist is complete when every advertised dependency has both a verification path and a responsible change path.

## Adjacent Reference Routing

Keep this reference when the primary question is how to teach, compare, bound, verify, and safely copy an extension example. Route to a specialized reference when one surface owns the acceptance criteria or when the first irreversible effect introduces a distinct schema, permission, protocol, package, or lifecycle contract. A route selects the owner of a question; it does not transfer currentness or verification automatically.

```text
Need a bounded teaching example?
|
+-- No surface selected yet
|   `-- Stay here: declare audience, outcome, surface matrix, and status.
|
+-- One surface owns the behavior
|   +-- Model-invoked instructions ........ skill references
|   +-- User-invoked operation ............ command reference
|   +-- Event-triggered policy/action ..... hook reference
|   +-- External tool/resource protocol ... MCP reference
|   +-- User or project configuration ..... settings reference
|   `-- Package identity/discovery ........ manifest reference
|
+-- Distribution or installation owns risk
|   `-- Route to creator/installer guidance and activate lifecycle gates.
|
`-- Interaction among surfaces is the lesson
    `-- Route each surface mechanic, then return here for composition review.
```

**Primary route table**

| Request signal | Primary destination | Use it to decide | Do not route there merely because |
|---|---|---|---|
| The model should select reusable instructions from a description | `skill_development_reference_patterns-20260710.md` | Skill scope, activation description, content boundary, and support-file structure | The directory is called a plugin or contains documentation |
| The task needs rigorous skill authoring and validation workflow | `writing_skills_validation_patterns-20260710.md` | Authoring sequence, validation evidence, negative cases, and maintainable skill quality | A prose example only resembles a skill |
| The target requires a current skill metadata format | `openai_skill_yaml_patterns-20260710.md` | Target-owned YAML fields, constraints, and validation expectations | Historical frontmatter happens to parse somewhere |
| A user explicitly invokes a named operation | `plugin_command_development_patterns-20260710.md` | Command input, execution, output, error, and discovery behavior | A skill response happens to include a command line |
| An event automatically triggers policy or work | `plugin_hook_development_patterns-20260710.md` | Event selection, ordering, timeout, failure, side effect, and recovery behavior | The example mentions automation without registering a hook |
| The extension exposes or consumes an MCP server | `plugin_mcp_integration_patterns-20260710.md` | Transport, capability, tool or resource contract, authentication, failure, and cleanup | An example calls an ordinary local script or generic HTTP endpoint |
| Users or projects change persistent extension behavior | `plugin_settings_configuration_patterns-20260710.md` | Configuration schema, precedence, validation, migration, secret boundary, and defaults | A fixed teaching constant is not intended to be configurable |
| Package identity, discovery, declared surfaces, or compatibility is at issue | `plugin_structure_manifest_patterns-20260710.md` | Manifest structure, identity, registration, dependency, and package-level claims | A sample tree looks package-shaped but makes no distribution claim |
| The task is to scaffold or update an actual Codex plugin | `codex_plugin_creator_patterns-20260710.md` | Current plugin creation, optional structure, manifest, cache or reinstall workflow, and marketplace boundary | The learner only needs to understand one extension format |
| The task is to distribute, install, update, or remove a reusable skill | `skill_installer_distribution_patterns-20260710.md` | Source trust, installation location, update behavior, conflict, and removal | A private source-valid example has not been offered for distribution |
| The task is to evaluate whether a skill performs its intended lesson | `skill_creator_evaluation_patterns-20260710.md` | Evaluation cases, comparison, diagnosis, and improvement evidence | Static format validation is the only current claim |

Paths above are confirmed repository neighbors, not transitive endorsements. Before using a destination for implementation, inspect its own evidence map, target-version boundary, focused verifier, and evolution status. If a destination is still a seed or relies on unrefreshed external material, preserve that uncertainty rather than borrowing confidence from this evolved reference.

**Route by the first durable decision.** Shared nouns are weak selectors. The word `plugin` can describe a package, a collection of surfaces, or merely a directory. Prefer the first decision that changes acceptance criteria:

- A model-selection contract routes to skill guidance.
- A user-invocation contract routes to command guidance.
- An event and ordering contract routes to hook guidance.
- A protocol and external-failure contract routes to MCP guidance.
- A persistence and precedence contract routes to settings guidance.
- A package identity and discovery contract routes to manifest guidance.
- A trust, installation, upgrade, or removal contract routes to distribution guidance.

**Stay in this reference when:**

- no surface has been selected and the learner needs a comparison;
- the artifact is a conceptual or source-valid lesson whose runtime adapter remains conditional;
- the primary concern is example minimality, copyability, evidence status, or teaching safety;
- several mechanics are already understood and the remaining question is how to compose them without implying absent capability; or
- a polished tree needs skeptical review for capability theater, hidden state, or copied-template risk.

**Use a route stack only for genuine composition.** List one primary destination and add a secondary destination only when the example claims its capability. For example, a command that changes persistent user behavior may need command guidance for invocation, settings guidance for schema and precedence, and manifest guidance for registration. The interaction is not complete until the demonstration also verifies that the command updates the intended setting, invalid values recover safely, the package declares both surfaces, and removal handles retained user data explicitly.

Do not create a route stack simply because a plugin can technically contain many surface types. Optional directories are possibilities, not requirements. Every added route creates another evidence owner, compatibility boundary, and copied dependency.

**Examples**

| Request | Route | Reason and return condition |
|---|---|---|
| "Show the smallest skill that answers format questions and declines deployment work" | Skill development, then return here | Skill guidance owns activation mechanics; this reference owns the good, negative, and clean-copy lesson |
| "Add a user command that validates the demonstration" | Command development, with manifest guidance if packaged | The command owns input and execution; return when its example contract and package claim can be reviewed together |
| "Run validation before every tool call" | Hook development | Event scope, ordering, latency, denial, and recovery dominate; return only if teaching the hook is itself the goal |
| "Expose a remote catalog through tools" | MCP integration | Protocol, authentication, unavailable service, and capability discovery dominate the risk |
| "Put commands, hooks, settings, and MCP folders under an example plugin" | Stay here for scope before routing | Directory names do not establish why each surface exists; define the primary lesson before adding mechanics |
| "Package the skill example for other teams" | Plugin creator or installer guidance, then return here | Distribution activates trust, dependency, compatibility, install, upgrade, removal, and copied-descendant gates |

**Bad route:** send every request containing `plugin` to the manifest reference. This confuses package identity with behavior and can hide the actual command, hook, skill, or protocol contract.

**Borderline route:** a tutorial intentionally teaches command-plus-hook coordination. Use both specialized references only after declaring that coordination is the learning outcome. If the hook merely decorates the command, split it or omit it; otherwise learners may copy an event-triggered side effect they did not need.

**Route verification**

1. Confirm the destination path exists in the current repository.
2. Read its opening decision contract, not only its filename.
3. Verify that the request satisfies the destination's entry condition and not an avoid condition.
4. Identify which claim, file, side effect, or lifecycle responsibility moves to that destination.
5. Check that no two references defer ownership of the same acceptance criterion to each other.
6. Bind target mechanics to the destination's current authoritative evidence and focused gates.
7. Return to this reference after implementation to reassess minimality, noninterference, failure recovery, clean copying, and lifecycle closure across the whole lesson.

If no neighboring reference owns a required cross-surface behavior, record the gap and escalate rather than circulating among links. That gap is architectural information: it identifies a responsibility whose schema, evidence, or maintainer has not yet been made explicit.

## Workload Model

Treat the demonstration as a bounded teaching workflow, not as a prose summary and not as a miniature showcase of every available extension surface. The workload includes more than authored files: source retrieval, learner context, host discovery, fixture execution, machine state, permissions, cleanup, review, compatibility, and support all consume capacity. A small tree with hidden setup can impose more work than a longer self-contained example.

No universal file, token, time, or delegation limit is established by the frozen evidence. Measure those values locally when they help planning. Split or escalate based on observed interaction, failure, and ownership pressure rather than treating an inherited count as a reliability threshold.

**Recommended default envelope**

- One primary teaching decision.
- One primary extension surface.
- One smallest complete source set.
- A deterministic happy-path fixture.
- Representative adjacent negative or nonselection fixtures.
- A credible failure and recovery path.
- One declared evidence status and target boundary.
- One clean-copy starting state.
- One owner for refresh and retirement.

This is a design default, not a claim that every good example has the same shape. A composition demonstration can include multiple surfaces when their interaction is the lesson. In that case, each surface still needs a specialized evidence owner and the composed behavior needs its own assertions.

**Workload dimensions**

| Dimension | Low-pressure profile | Pressure signal | Response and evidence |
|---|---|---|---|
| Teaching decisions | One observable choice and one success definition | Several unrelated choices compete for the title, examples, or conclusion | Split by decision or state explicitly that comparison is the lesson; trace each example to one outcome |
| Extension surfaces | One skill, command, hook, MCP integration, setting, or manifest concern | Added surfaces have independent schemas, triggers, permissions, or failures | Route mechanics to specialized references and retain a thin, tested composition scenario |
| Interaction edges | Components can be understood and failed independently | Ordering, shared state, retries, or recovery spans surfaces | Add an interaction matrix and cross-surface fixtures; assign one composition owner |
| Source evidence | One canonical local source with clearly bounded support | Duplicates, conflicting versions, unrefreshed public links, or inferred host behavior | Deduplicate by content, separate source roles, and block currentness claims until refreshed |
| Learner context | Entry file plus directly relevant support can be reviewed from a clean start | The learner must infer undisclosed history, conventions, or absent files | Add the missing prerequisite, narrow the audience, or split progressive material |
| Tool context | A small set of target-owned validators has nonoverlapping roles | Large schemas, overlapping tools, or generated output obscures the next decision | Load tools progressively and preserve only the observations needed by the current gate |
| Input variability | Fixed, synthetic, and non-sensitive fixtures | Time, randomness, locale, remote data, or private content changes outcomes | Inject or freeze variability, sanitize inputs, or label and test the environmental boundary |
| Runtime state | Execution is isolated and leaves no undeclared mutation | Caches, configuration, background processes, shared files, or databases affect later runs | Inventory before and after state; isolate, reset, or document intended persistence |
| External dependency | No network or a deterministic local substitute | Authentication, rate limits, remote availability, protocol drift, or cost affects the lesson | Prefer a mock for the default; add a separately labeled live validation path when realism matters |
| Privilege | Read-only or narrowly scoped capability | Broad filesystem, shell, network, credential, or administrative access is requested | Reduce capability, add denial tests, and require explicit least-privilege review |
| Failure diversity | One local, classified failure with a direct recovery | Partial success, timeout, retries, rollback, or ambiguous ownership appears | Add state-transition cases and route operational mechanics to the appropriate specialist |
| Environment matrix | One declared host and platform profile | Several host versions, platforms, shells, architectures, or configurations are claimed | Define a supported matrix, automate representative clean runs, or narrow compatibility |
| Package lifecycle | Source-valid artifact with no distribution claim | Install, upgrade, migration, removal, rollback, or retained data becomes part of the promise | Activate package and lifecycle gates and move ownership to creator or installer guidance |
| Copy population | Private workshop artifact with a known audience | Reuse across teams, generated descendants, or untracked copies becomes likely | Add stable identity, migration notes, support ownership, and retirement signaling |
| Evidence debt | Every claim has a current observation at its status | Claims rely on analogy, unrefreshed links, or lower-level checks | Narrow status, schedule authoritative refresh, or remove the unsupported promise |
| Review burden | One reviewer can inspect contract, files, and evidence coherently | Reviewers repeatedly miss interactions or reconstruct setup manually | Split responsibilities, produce a claim-evidence map, and rehearse a clean copy |

**Separate four kinds of workload.** Combining them into one count hides where complexity moved.

1. **Research workload** covers corpus discovery, source deduplication, external refresh, authority selection, and uncertainty classification. A large research corpus can still yield a small learner artifact.
2. **Author workload** covers writing, fixtures, adapters, gates, package work, and review. Fast authoring that relies on personal caches or implicit knowledge creates downstream debt.
3. **Learner workload** covers discovery, reading, selection, copying, invocation, diagnosis, and cleanup from the documented starting state. This is the primary workload for a demonstration.
4. **Lifecycle workload** covers compatibility, support, copied defects, security response, migration, demotion, and retirement. Promotion multiplies this cost across descendants.

Record these categories independently. A change that reduces author workload but increases learner setup is a transfer, not a net simplification. A change that moves instructions from the entry file into several unexplained references is context displacement, not progressive disclosure.

**Choose a representation by workload**

| Situation | Preferred form | Tradeoff | Required check |
|---|---|---|---|
| One structural lesson with no runtime claim | Static, source-valid example | Fast and portable but cannot establish host behavior | Schema-adapted review, file closure, and status label |
| Deterministic local behavior is the lesson | Runnable local fixture | Stronger evidence but adds language and toolchain setup | Repeatability, failure path, and clean execution |
| Remote behavior is incidental | Local mock plus explicit protocol boundary | Stable and safe but less realistic | Contract parity with the claimed remote interface |
| Remote behavior changes the decision | Mocked default plus separately controlled live check | More realistic but adds credentials, cost, privacy, and availability | Secret handling, denial, timeout, cleanup, and version evidence |
| Several concepts build progressively | Graded example set with one recommended starting point | Teaches evolution but multiplies maintenance | Each step must remain complete and state what changed |
| Several surfaces jointly create the outcome | Composition example with specialized subcontracts | Preserves interaction but raises context and failure load | Cross-surface state, ordering, permissions, and lifecycle matrix |
| Reuse is local and supervised | Workshop artifact | Low distribution overhead but limited portability | Explicit environment and instructor assumptions |
| Reuse is independent and repeated | Maintained template or package | Copy efficiency but durable compatibility and support obligations | Clean copy, installation, upgrade, removal, migration, and ownership |

**Split signals**

Split the demonstration, route a specialized concern, or create a staged example when any of these signals recur:

- Two examples require different audiences or success definitions.
- A support file has an independent activation or lifecycle contract.
- A negative case for one surface is a positive case for another and precedence is not the lesson.
- A live dependency dominates setup, failure handling, or security review.
- The simple path and production path share labels but have materially different effects.
- Reviewers cannot identify which claim a file, permission, or dependency supports.
- Clean-copy failures cluster around prerequisites unrelated to the primary decision.
- Compatibility or removal work exceeds the teaching value of the source example.
- Corrections must be released on different schedules or by different owners.

Do not split merely to reduce line count. If two parts share state, fail together, and must migrate together, separate files can conceal rather than reduce coupling. In that case, keep a thin composition contract and make the interaction explicit.

**Workload audit procedure**

1. State the learner's decision and highest claimed evidence status.
2. Inventory surfaces, entry points, files, generated artifacts, tools, effects, permissions, external dependencies, and cleanup.
3. Draw the interaction edges that cross trigger, state, failure, or lifecycle boundaries.
4. Trace the complete learner path from clean discovery through success, failure, recovery, and exit.
5. Reset the environment and repeat without author caches, untracked files, credentials, or shell history.
6. Record the first blocking assumption and classify it as missing prerequisite, hidden state, unclear contract, broken artifact, or unsupported environment.
7. Measure local values such as review time, fixture duration, artifact size, or support frequency only after defining their population and decision use.
8. Apply split, mock, route, narrow, or escalation responses to the pressure dimensions.
9. Repeat the clean-copy trace and verify that the primary lesson remains intact.

**Worked profiles**

Good low-pressure profile: a skill-format lesson contains one entry file, bounded activation wording, a positive request, an adjacent deployment request that must not select, a response-shape review, and a clean-copy check. It makes no package or runtime-host claim beyond its evidence.

Bad hidden-workload profile: a tiny tree invokes a remote service using an author's cached credential, relies on an undeclared configuration file, and leaves generated state. The source count is low, but learner, privilege, failure, and cleanup pressure are high.

Borderline composition profile: a command invokes validation and a hook enforces the same policy. Keep it unified only if coordination, precedence, and failure recovery are the lesson. Otherwise teach the command and hook separately and link them through a small integration case.

The operational boundary is reached when the team can no longer reproduce, review, support, or retire the demonstration within its declared ownership and evidence model. At that point, reduce the claim, split the lesson, isolate live behavior, or promote it into a maintained package with the corresponding lifecycle controls. Optimize for total lesson lifecycle cost, not minimum initial author effort.

## Reliability Target

The reliability target is status fidelity under skeptical reuse: the demonstration must make no stronger claim than its evidence, reproduce its promised observations inside a declared envelope, avoid capturing adjacent work, fail without undeclared harm, and leave the learner with a recoverable next state. Package, compatibility, installation, and removal reliability apply only when those capabilities are claimed.

Do not reuse the seed's fixed routing sample as a universal threshold. The frozen evidence does not establish a general population, sampling method, or risk basis for that number. Separate categorical release gates from behavioral objectives that require a local baseline.

**Categorical release gates**

Every applicable row must pass for the corresponding status. These are contract checks rather than statistical claims.

| Reliability property | Passing condition | Evidence | Blocking response |
|---|---|---|---|
| Claim traceability | Every consequential recommendation maps to a local source fact, a refreshed authoritative fact, or an explicit inference with a verification path | Claim-evidence matrix and skeptical review | Remove, narrow, or label the unsupported claim |
| Source-role fidelity | Canonical, duplicate-locator, contextual, unrefreshed external, and inferred material are not presented as interchangeable corroboration | Source map, content hashes, and claim-level citations | Downgrade confidence and correct source roles |
| Status fidelity | Static validation is not described as host load, load is not described as behavior, and behavior is not described as package lifecycle | Status declaration and evidence-level comparison | Demote to the highest demonstrated status |
| Capability fidelity | Files and directory names do not imply commands, hooks, MCP, settings, installation, or other absent surfaces | Capability matrix and artifact inventory | Remove the implication or implement and verify the surface |
| Bounded activation | The intended in-scope cases select the example and named adjacent cases follow the expected nonselection or handoff behavior | Positive, negative, and overlap fixtures | Narrow or clarify activation before publication |
| Output truthfulness | Every promised artifact, answer shape, or durable effect appears in the validated case | Output assertions and artifact inspection | Repair behavior or reduce the promise |
| Safe unsupported input | Malformed, unavailable, and out-of-scope cases produce an explicit failure or route without fabricated success | Failure fixtures and reviewer observation | Add validation and recovery guidance |
| Secret safety | The source, fixtures, logs, package, and instructions contain no real credentials or private identifiers | Secret scan plus manual fixture review | Revoke exposed material if needed, sanitize, and repeat checks |
| Side-effect declaration | Observed files, processes, network calls, configuration changes, and retained data match the capability contract | Before-and-after resource inventory | Remove, isolate, or declare the effect and its permission |
| Recovery closure | Every tested failure ends in a known state with retry, rollback, escalation, or adjacent route | State-transition evidence and recovery rehearsal | Block the affected status until recovery is defined |
| Evidence health | Required validators execute, deliberate mutations are detected, and missing observations do not appear as success | Verifier self-check and mutation cases | Treat the evaluation as failed and repair it first |
| Reference integrity | Original heading contract, tables, fences, links, ASCII policy, and whitespace checks pass | Focused reference verifier and hygiene scan | Correct the artifact before content promotion |
| Ownership closure | A maintainer role owns source refresh, compatibility change, security response, demotion, migration, and retirement | Release record | Keep the example local or lower its distribution claim |

**Locally calibrated objectives**

These outcomes need a defined population and cannot inherit a meaningful percentage from another project. Record the baseline, observation window, host and artifact version, sample construction, decision threshold, and action before calling any result a target.

| Objective | Numerator and denominator or distribution | Why it matters | Counter-measure |
|---|---|---|---|
| Positive activation | Reviewed in-scope requests that select correctly over all reviewed in-scope requests | Detects missed intended use | Pair with noninterference so broad capture does not look beneficial |
| Noninterference | Reviewed adjacent and unrelated requests handled as declared over all reviewed negative requests | Detects overbroad selection | Pair with positive activation so excessive refusal does not look safe |
| Repeated fixture stability | Identical controlled runs with matching asserted outcomes over all repeated controlled runs | Detects nondeterminism and hidden state | Track semantic correctness separately from repeatability |
| Clean-copy completion | Independent clean-copy attempts reaching the declared outcome over all observed attempts, classified by first failure | Exposes author-only context and missing files | Review side effects and permission use so easy copying is not unsafe copying |
| Diagnosis interval | Distribution from reproducible report to classified cause and protected correction | Tests support and observability quality | Track recurrence so fast diagnosis does not excuse repeated defects |
| Compatibility coverage | Declared host and environment combinations with current evidence over all combinations claimed as supported | Prevents vague portability claims | Record untested configurations rather than assuming equivalence |
| Recovery completion | Exercised failure cases that reach the declared recoverable state over all exercised failure cases | Detects ambiguous partial failure | Keep severity visible; a rare destructive failure cannot be averaged away |
| Lifecycle closure | Clean install, supported upgrade, failed-install recovery, and removal cases passing over all lifecycle cases claimed | Detects package residue and migration gaps | Compare source and built artifact so packaging omissions remain visible |
| Copied-defect response | Known affected maintained descendants migrated or retired over all known affected maintained descendants | Limits propagation after lesson correction | Acknowledge that unknown private copies are outside the denominator |
| Route agreement | Sampled requests whose destination matches the documented decision rule over all independently reviewed sampled requests | Detects ambiguous adjacent routing | Record reviewer disagreement and destination currentness |

**Set a local target without invented precision**

1. Name the decision the objective will change, such as narrow activation, block promotion, demote a host version, or improve recovery.
2. Define the population before collecting outcomes. Separate authored fixtures, observed learner requests, host versions, and clean-copy rehearsals.
3. Establish that the collection path works, including a known failing case and a missing-signal case.
4. Record a baseline with its environment, sample construction, and uncertainty.
5. Choose a threshold from consequence and remediation cost, not from an inherited round number.
6. Pair the target with the most likely gaming or displacement measure.
7. Freeze the definition for the review interval; version it when the status, denominator, or host changes.
8. Specify the action that follows breach and the evidence required to recover status.

For sparse examples, a classified case table can be more honest than a rate. Report "three reviewed clean copies, with one missing-path failure" rather than converting a tiny convenience sample into a universal usability claim. For open-ended activation, retain deterministic boundary fixtures and add sampled observations only when privacy-safe, representative collection is available.

**Reliability profiles by status**

| Highest claimed status | Minimum reliability evidence | Claims explicitly unavailable at this status |
|---|---|---|
| Conceptual | Capability clarity, alternatives, non-goals, misleading-implication review, and evidence boundary | Syntax, host discovery, execution, package, and lifecycle |
| Source-valid | Conceptual gates plus metadata adaptation, file closure, deterministic fixtures where present, text hygiene, and secret safety | Host discovery, actual selection, runtime effects, and package lifecycle |
| Host-loaded | Source-valid gates plus clean-host discovery and loader diagnostics | Behavioral correctness, integration reliability, and distribution lifecycle |
| Behavior-validated | Host-loaded gates plus positive, negative, overlap, output, failure, recovery, and side-effect observations | Package installation, upgrade, and removal unless separately claimed |
| Integrated | Behavior gates plus cross-surface ordering, permissions, dependencies, and partial-failure handling | Distribution reliability unless a built artifact is tested |
| Packaged | Integrated gates plus built-artifact closure, clean install, supported upgrade, rollback, removal, and residue comparison | General compatibility outside the tested matrix |
| Promoted template | Packaged or appropriately distributable gates plus independent copy rehearsal, ownership, compatibility statement, migration, and retirement route | Unknown private descendants and untested environments |

**Failure severity prevents misleading averages.** Classify failures by consequence before aggregating observations:

- A documentation ambiguity may permit correction without reducing source-valid status.
- An overbroad trigger can block behavior validation because it interferes with adjacent work.
- A fabricated success, credential exposure, undeclared destructive effect, or unrecoverable package mutation blocks the affected status regardless of average success.
- An untested host version reduces the compatibility claim; it does not become supported because another version passed.
- A broken collector or verifier invalidates the result rather than counting as an uneventful run.

**Release evidence record**

Record the artifact version and content hash; target host, schema, platform, and dependency versions; highest claimed status; applicable categorical gate results; calibrated objective definitions and observations; known failing and missing-signal controls; unresolved exceptions; residual uncertainty; owner; refresh triggers; demotion action; and replacement route. Keep raw private request text out of the record unless it is necessary, authorized, and appropriately protected.

**Worked reliability decisions**

Good: a source-valid skill-format example passes metadata adaptation against the selected target, file closure, deterministic text fixtures, negative-request review, secret scanning, and independent copying. It says that host activation is unverified. Its reliability claim matches its evidence.

Bad: an example parses successfully and is called production-ready, even though no host loads it, no negative activation case exists, and no package was built. The defect is status inflation; adding a success percentage does not repair it.

Borderline: a live integration passes on one declared host and platform. Report that exact observation and keep broader compatibility unknown. Add a matrix only when the distribution promise and maintenance ownership justify its cost.

Promotion is reliable when independent evidence converges at the claimed level, severe failures remain categorical, the evaluation path detects deliberate defects, and uncertainty narrows the public promise. Reducing an unsupported claim is a reliability improvement, not a loss of feature completeness.

## Failure Mode Table

This registry is a minimum challenge set, not proof that every failure has been enumerated. Apply rows according to the capability matrix and highest claimed status. When an unclassified failure appears, default to explicit failure, no fabricated success, no undeclared mutation, and demotion to the last evidenced state until the cause and recovery are understood.

| Category and failure | Trigger and earliest observable signal | Status or consequence | Immediate containment and safe state | Recovery and prevention evidence |
|---|---|---|---|---|
| Evidence: duplicate source treated as corroboration | Two paths have identical content but are counted as independent support | Confidence is inflated at every status | Mark one source fact and the other as a locator; stop promotion based on source count | Content-hash deduplication and claim-level source-role review |
| Evidence: authoritative source drift | Host schema, loader, permission, or package guidance changes after capture | Target-specific claims may be stale | Mark affected mechanics unrefreshed and lower the relevant status | Refresh the authoritative source, record version and date, rerun target gates |
| Evidence: inference presented as fact | Plausible advice has no mapped source or disconfirming observation | Learners may copy unsupported policy | Label the inference or remove the claim before reuse | Claim-evidence matrix rejects unmapped consequential claims |
| Scope: directory capability theater | Folder names imply commands, hooks, MCP, settings, or installation that the artifact does not implement | Learner selects or copies the wrong surface | Remove empty or decorative surfaces; retain only the declared lesson | Capability inventory compared with files, registration, and evidence |
| Scope: wrong primary surface | A request is implemented as a skill when it needs explicit command invocation, event handling, protocol access, configuration, or packaging | Acceptance criteria and failure model no longer match | Pause implementation and route to the specialized reference | Decision table review using activation, timing, effects, and lifecycle |
| Activation: missed intended request | In-scope request does not select or discover the example | Behavior status is not earned | Preserve the request and expected route; keep a manual alternative visible | Positive fixture tied to current target metadata and loader |
| Activation: adjacent request captured | Deployment, packaging, or another neighboring request selects the narrow demonstration | Noninterference fails and unrelated work may receive misleading guidance | Narrow description and add an explicit handoff or refusal | Negative and overlap fixtures that mirror the production selection contract |
| Activation: ambiguous precedence | Two extensions match and selection depends on incidental order | Results vary by installation or host state | Declare precedence, composition, or refusal; avoid silent tie breaking | Controlled overlap cases across supported host configurations |
| Structure: missing required file | Entry content references a support path absent from the copied artifact | Source-valid and copyable claims fail | Stop at the missing dependency and name it; do not improvise content | File-closure gate plus deliberate file-removal mutation |
| Structure: optional-file drift | Support content changes while the entry instructions or links retain an older contract | Learner follows inconsistent guidance | Pin the relationship or inline the small dependency | Link, content-version, and clean-copy review |
| Reproducibility: hidden author state | Example works only with untracked files, caches, shell history, credentials, or local configuration | Clean-copy claim fails | Reproduce in a disposable state and identify the first hidden prerequisite | Environment reset and independent copier rehearsal |
| Reproducibility: nondeterministic fixture | Time, randomness, locale, remote data, or unordered output changes assertions | Tests become flaky or misleading | Freeze or inject the variable; isolate environmental checks | Repeated controlled runs plus a known variance assertion where needed |
| Privacy: sensitive fixture or log | Real request text, credential, private endpoint, personal path, or secret-shaped value enters source or output | Confidentiality and distribution safety fail | Stop sharing, revoke real credentials when applicable, and sanitize all copies | Secret scanning, fixture review, and minimum-data logging policy |
| Permission: capability overreach | Example requests broad filesystem, process, network, or credential access for a narrow result | Copied template gains unnecessary privilege | Deny or remove excess capability; keep the artifact unpromoted | Least-privilege review and denied-capability fixture |
| Behavior: fabricated success | Unsupported input or unavailable dependency produces a confident completion without the promised artifact | Trust and behavior status fail categorically | Return an explicit classified failure and a safe route | Output existence assertions and unavailable-dependency case |
| Behavior: mock presented as live | Deterministic local substitute is described as proof of remote integration | Integration confidence is inflated | Relabel the status and separate mock from live evidence | Contract-parity review plus controlled live check when claimed |
| External: service unavailable or throttled | Timeout, authentication failure, rate limit, protocol change, or network denial occurs | Invocation may be incomplete or delayed | Bound the attempt, preserve input, avoid duplicate effects, and report availability class | Target-specific timeout, cancellation, idempotency, and retry tests |
| State: partial side effect | Failure occurs after a file, setting, process, or remote mutation but before completion | Retry may duplicate or corrupt state | Inventory completed effects and enter a repair or rollback state | Fault injection at each mutation boundary and residual-state assertions |
| Integration: ordering race | Command, hook, setting, or external tool observes state before another surface commits it | Intermittent behavior and misleading fixtures | Serialize, make state transitions explicit, or reject unsafe overlap | Controlled ordering tests and interaction state diagram |
| Integration: context loss | A long authoring run forgets scope, evidence status, exclusive paths, or user intent | Work may overwrite ownership or inflate claims | Stop at the last durable section, reread packet, reference, and journal | Per-section saves, three-section checkpoints, and boundary sanity checks |
| Coordination: fanout conflict | Parallel work touches shared files, duplicates sections, or uses inconsistent source snapshots | Merge damage and evidence divergence | Enforce exclusive ownership and one writer per artifact | Path allowlist, durable checkpoints, and post-write diff review |
| Package: built artifact omits source dependency | Source tree passes but package lacks an entry point, support file, dependency, or fixture | Packaged status fails | Withdraw or demote the package; inspect actual contents | Built-artifact traversal and clean-host load |
| Lifecycle: interrupted installation | Failure leaves partial files, registration, or configuration | Environment may not support retry or removal | Detect partial state and use idempotent repair or rollback | Fault injection across install steps and state comparison |
| Lifecycle: incompatible upgrade | New metadata, identity, configuration, or behavior cannot consume a supported prior state | Existing users break or retain stale behavior | Restrict the version, migrate explicitly, or provide replacement | Versioned upgrade fixtures and rollback rehearsal |
| Lifecycle: removal residue | Uninstall leaves registration, cache, process, generated file, or configuration not declared as retained user data | Lifecycle symmetry fails | Remove accidental residue and document intentional retention | Before-install, after-install, and after-remove inventory |
| Compatibility: untested host generalized | One host or platform passes and prose implies broad support | Users receive unsupported compatibility claims | Narrow the support statement to observed combinations | Versioned environment matrix and expiry trigger |
| Verification: gate observes wrong boundary | A deliberate trigger broadening, missing file, or changed output still passes | Green evidence is invalid | Stop relying on the gate and repair its assertion | Mutation cases for selection, closure, output, and lifecycle |
| Verification: missing signal looks successful | Validator, telemetry, or review collection silently stops | Absence is misread as quiet reliability | Mark result unknown and fail evidence health | Known-failure control and missing-collector alarm |
| Propagation: copied defect persists | A fixed lesson flaw remains in maintained descendants or generated templates | Harm continues after local correction | Identify known affected copies and publish migration or retirement guidance | Repository search, version marker, and descendant response record |
| Ownership: maintainer disappears | Compatibility, security, support, or refresh trigger has no responsible role | Promoted status decays without response | Demote, archive, or transfer ownership visibly | Periodic owner confirmation and replacement route |

**Response sequence**

1. **Classify:** identify the failed claim, surface, status, environment, and trigger. Do not retry an unknown failure merely because retry is convenient.
2. **Contain:** stop new reuse or side effects, protect sensitive data, and preserve the smallest diagnostic evidence.
3. **Observe state:** inventory what completed, what did not, and which resources remain. Error text alone is insufficient for partial mutation.
4. **Choose a safe end state:** retry only when the operation is known to be transient and idempotent; otherwise repair, roll back, route, demote, or retire.
5. **Recover:** execute the bounded recovery and verify the resulting state, including absence of forbidden residue.
6. **Prevent recurrence:** correct the example, add or strengthen a gate, and update migration guidance for known descendants.
7. **Restore status deliberately:** rerun every gate activated by the affected claim rather than only the new regression case.

**Consequence classes**

- **Immediate publication block:** real secret exposure, fabricated success, undeclared destructive effect, unrecoverable mutation, or a verifier proven unable to detect the claimed boundary.
- **Status demotion:** stale authoritative mechanics, unverified host loading, incomplete behavior evidence, broken packaging, or unsupported compatibility expansion.
- **Scoped repair:** a broken link, unclear route, malformed table, or missing noncritical example whose consequence does not exceed the currently claimed status.
- **Retirement candidate:** absent ownership, obsolete host surface, repeated copied harm, or a maintained replacement with a safer migration path.

Do not average a severe categorical failure into an otherwise high success rate. A single exposed credential or destructive undeclared effect challenges the safety claim directly. Conversely, a source-valid example need not be penalized for lacking installation evidence when it clearly makes no distribution claim.

**Fault-injection set**

| Deliberate fault | Expected detection | Expected safe state |
|---|---|---|
| Remove a required support file | File-closure or clean-copy gate fails before invocation | No fabricated replacement; missing path identified |
| Broaden activation wording to an adjacent request | Negative or overlap case fails | Example is not promoted until scope is narrowed |
| Change an asserted output field | Behavior fixture fails | Prior artifact remains intact and mismatch is visible |
| Deny a declared permission | Preflight or denial case reports the exact unavailable capability | No partial undeclared effect remains |
| Make the remote dependency unavailable | Bounded failure and cancellation path executes | Input is preserved and duplicate side effects are prevented |
| Interrupt install after each mutation boundary | Lifecycle drill identifies partial state | Repair or rollback returns to a known inventory |
| Disable the verifier's result collection | Evidence-health control fails | Release result is unknown, never silently green |
| Substitute a similarly named adjacent reference | Purpose and entry-condition review rejects the route | Original decision remains unowned until corrected |

Good response: an unrefreshable metadata claim is demoted to illustrative syntax, target behavior is marked unverified, and a current-schema validation gate is required before promotion.

Bad response: a denied permission is retried repeatedly without idempotency, budget, or cleanup evidence. This increases load and can duplicate partial effects while teaching the wrong recovery policy.

Borderline response: a flaky live check is isolated from the deterministic default and reported with environment details. This is acceptable for exploratory compatibility evidence, but it cannot establish a general reliability rate until the variance and population are understood.

Failure handling is part of the lesson's public contract. Copiers learn what to retry, what to ignore, and what to clean up from the example. Correct unsafe semantics even when compatibility is inconvenient, then provide a visible migration path rather than preserving the defect silently.

## Retry Backpressure Guidance

Do not treat retry as a generic response to failure. Retry repeats a state transition and can repeat its cost, disclosure, load, or side effect. The default is to stop after a failed attempt until the failure class, completed effects, retry safety, total budget, cancellation behavior, and expected recovery signal are known.

Exact attempt counts, delays, and queue sizes are target-owned values. The frozen local corpus establishes no universal constants. Calibrate policy against dependency semantics, quota, latency objective, effect idempotency, user intent, and observed capacity.

**Retry decision procedure**

```text
Failure observed
|
+-- Is the signal itself trustworthy?
|   +-- No  -> fail evidence health; repair the observer
|   `-- Yes
|
+-- What state or effect completed?
|   +-- Unknown -> contain and inspect; do not retry
|   `-- Known
|
+-- Is the cause transient and distinguishable?
|   +-- No  -> repair, route, demote, roll back, or stop
|   `-- Yes
|
+-- Is repetition effect-free or idempotent for the full retry window?
|   +-- No  -> recover or compensate before another attempt
|   `-- Yes
|
+-- Is there remaining operation-wide budget and dependency capacity?
|   +-- No  -> return bounded failure or degraded result
|   `-- Yes -> wait according to target policy, honor cancellation, retry
|
`-- On every outcome: expose attempts, cause class, final state, and freshness
```

**Retry domains**

| Domain | Potentially retryable case | Non-retryable or repair-first case | Required evidence before automation |
|---|---|---|---|
| Reference authoring | Validator process failed to start for a known transient environment reason | Duplicate packet value, wrong heading, malformed table, missing section, or deterministic content assertion | Re-run produces the same input and no concurrent writer owns the file |
| Source refresh | Authoritative endpoint is temporarily unavailable and the last status is clearly marked stale | Source identity is unknown, authority conflicts, access is forbidden, or returned content contradicts the claim | Bounded fetch policy, freshness label, privacy boundary, and escalation route |
| Host discovery | Loader is temporarily unavailable without mutating registration | Manifest or metadata is invalid, entry file is missing, or host version is unsupported | Clean state, trustworthy error class, and target-owned loader semantics |
| Local deterministic behavior | Process interruption occurs before any effect and input remains valid | Assertion, syntax, contract, schema, or unsupported-input failure repeats deterministically | Controlled fixture proves no prior effect and cancellation is honored |
| Remote read | Transient transport or declared availability error | Authentication denial, invalid request, quota policy, privacy prohibition, or semantic contradiction | Total deadline, dependency budget, freshness label, and bounded attempt visibility |
| Remote mutation | Target confirms an idempotency mechanism covering the complete supported retry window | Effect status is unknown, key scope is wrong, compensation is absent, or conflict needs user choice | Fault injection before and after effect, duplicate-effect assertion, and reconciliation path |
| Hook or event work | Host redelivers with a stable event identity and processing is idempotent | Ordering is unsafe, event identity is absent, or repeated work compounds a side effect | Deduplication, bounded queue, cancellation, and poison-event handling |
| Installation or upgrade | A documented repair operation resumes from known partial state | Mutation boundary is unknown, version conflict requires choice, or rollback cannot restore state | Step-level state inventory, idempotent repair, rollback rehearsal, and lock ownership |
| Removal | A cleanup step is repeatable and cannot delete user-owned retained data | Package identity is ambiguous or state may belong to another installation | Ownership markers, before-and-after inventory, and retained-data contract |

**Never retry blindly**

- A deterministic schema, syntax, assertion, or contract failure.
- Missing required content or an unresolved source contradiction.
- Permission denial that requires a user or policy decision.
- Authentication failure without an approved credential-refresh path.
- An unknown partial mutation.
- An unsupported host, platform, version, input, or capability.
- A secret-safety or privacy violation.
- A verifier that failed to observe a deliberate known defect.
- A request cancelled by the user unless a new request explicitly resumes it.
- Work after removal or retirement has begun without reconciling ownership.

Repeated success after one of these failures does not automatically restore confidence. It can reveal hidden state, a flaky gate, a concurrent change, or an unobserved effect. Classify the difference and rerun the affected status gates.

**Operation-wide retry contract**

Before implementing automatic retry in a runnable demonstration, record:

| Contract field | Required answer |
|---|---|
| Failure classes | Exact target signals considered transient, permanent, contradictory, denied, cancelled, or unknown |
| State boundary | Effects that may complete before each signal and how completion is observed |
| Idempotency | Identity scope, storage, collision behavior, retention window, and reconciliation for uncertain results |
| Total budget | Maximum total attempts, elapsed work, dependency calls, and resource use across all nested layers |
| Wait policy | Target-calibrated delay, server guidance handling, jitter where appropriate, and upper bound |
| Cancellation | How user cancellation and host shutdown interrupt waiting and active work |
| Admission | When new work is delayed, rejected, queued, or degraded because capacity is unavailable |
| Observability | Attempt ordinal, original operation identity, cause class, wait decision, final state, and freshness |
| Fallback | Whether cached, mocked, partial, or alternate output still satisfies the contract and how it is labeled |
| Recovery | Rollback, compensation, manual repair, adjacent route, and evidence required before resumption |

Nested layers must not each reset their own attempt budget. Pass a shared operation budget downward or centralize retry ownership. Otherwise an apparently small per-layer policy multiplies calls and latency. Preserve the original cause when reporting exhaustion; the last timeout alone can conceal the invalid request that began the sequence.

**Backpressure triggers and responses**

| Pressure signal | Stop or slow | Safe response | Resume evidence |
|---|---|---|---|
| Packet or reference atomic order is broken | New section authoring | Persist or repair the current section boundary first | Complete packet section, matching reference section, and sanity result |
| Exact or normalized uniqueness regresses | Additional packet generation | Identify and rewrite duplicate values in the affected scope | Unique counts equal mandatory field counts |
| Heading, expansion, table, fence, ASCII, whitespace, or marker gate is red | Promotion and downstream reuse | Correct the artifact without touching unowned paths | Focused structural and hygiene checks pass |
| Source authority is stale or contradictory | Current target claims | Preserve historical fact and mark target mechanics conditional | Refreshed authority and claim-level reconciliation |
| Exclusive file ownership is unclear | Concurrent writes | Stop writers on the contested artifact and establish one owner | Allowlist and durable boundary agree |
| Dependency is throttled or unavailable | New remote work | Reject, queue within a bounded capacity, serve a clearly labeled safe fallback, or fail explicitly | Health and admission criteria recover within policy |
| Queue or context grows beyond review capacity | New admissions or delegated fanout | Narrow scope, serialize ownership, checkpoint state, and discard irrelevant context | Named owner, bounded backlog, and current plan reread |
| Partial side effects are unresolved | Retry and new mutation | Reconcile, compensate, roll back, or escalate | Resource inventory matches a declared recoverable state |
| Lifecycle operation is active | Conflicting invoke, upgrade, or remove work | Lock or reject conflicting operations according to target semantics | Installation identity and state become stable |
| Security or privacy failure appears | Distribution and telemetry collection | Contain exposure, revoke when applicable, sanitize, and investigate descendants | Security owner approves corrected evidence |

Backpressure must reach admission. Merely slowing a worker while requests accumulate without bound transfers failure into queue growth, stale work, memory pressure, and delayed cancellation. A demonstration need not implement a production queue, but it must not teach unbounded accumulation as a harmless default.

**Fallback and degradation**

A fallback is valid only when it preserves the user's declared outcome or reports the changed semantics visibly. A cached result must state freshness and source. A mock must not be presented as live evidence. A partial result must identify omitted claims. An adjacent route must preserve the original decision context. Silent fallback turns availability into misinformation.

**Verification cases**

| Injected condition | Asserted policy | Asserted final state |
|---|---|---|
| Transient read fails, then recovers | Attempts stay within the shared budget and expose the cause transition | One fresh result, no duplicate effect |
| Permanent invalid input | No automatic retry | Explicit validation failure, input preserved |
| Permission denied | No retry loop or privilege escalation | No partial side effect, required capability named |
| Cancellation during wait | Pending attempt is abandoned promptly according to target semantics | Cancellation distinguished from dependency failure |
| Failure after a mutation | Reconciliation occurs before any replay | Effect count and resource state match the declared recovery |
| Nested client and wrapper both want retry | One layer owns policy or both consume one budget | Total attempts remain bounded by the operation contract |
| Dependency pressure crosses admission limit | New work is bounded, rejected, or degraded visibly | Queue and resource use remain within the tested envelope |
| Result collector is disabled | Evidence-health gate fails | Run is unknown, never counted as success |

Good: a transient, effect-free authoritative read uses a bounded shared budget, honors cancellation, records freshness, and stops with the original cause when the dependency remains unavailable.

Bad: a denied permission is retried through several wrappers while each resets its counter. No attempt can change policy, load multiplies, and partial effects become harder to reconcile.

Borderline: a remote mutation provides an idempotency key. Retry is acceptable only after tests prove key scope, retention, duplicate suppression, uncertain-result reconciliation, and effect state across the complete supported retry window.

For long-running authoring work, persist each complete packet section before its reference counterpart, sanity-check immediately, checkpoint no later than every three completed sections, and reread the governing specification before broad or irreversible actions. The strongest default lesson is often how to stop with preserved state and a clear next decision, not how to continue attempting work whose safety is unknown.

## Observability Checklist

Observe the decisions and state transitions needed to verify or diagnose the claimed lesson. Do not preserve an internal reasoning transcript, raw user request, credential, or full command dump merely because it is available. Every retained field must support a named release, safety, compatibility, diagnosis, performance, migration, or retirement decision.

The minimum record distinguishes three states explicitly:

- **Observed:** a trustworthy signal reports the expected or unexpected result.
- **Not applicable:** the capability or status is outside the declared contract.
- **Unknown:** the signal was required but collection, correlation, or interpretation failed.

Unknown must never collapse into success. A failed verifier or missing telemetry path is an evidence-health failure.

**Status-aware observation requirements**

| Claimed status | Minimum observation | Conditional extension |
|---|---|---|
| Conceptual | Artifact identity, teaching decision, source roles, reviewer decision, unsupported implications, and unresolved uncertainty | Record disagreement when reviewer judgment changes the claim |
| Source-valid | Conceptual record plus content hash, validation adapter, file closure, text hygiene, secret-safety result, and changed paths | Record deterministic fixture identity when executable snippets are included |
| Host-loaded | Source-valid record plus host and schema version, discovery path, entry identity, load result, and loader diagnostic class | Correlate multiple registration steps when the host requires them |
| Behavior-validated | Host record plus intent class, activation decision, output class, failure class, effects, recovery state, and fixture version | Add retry and external-dependency fields when those behaviors exist |
| Integrated | Behavior record plus surface interaction, ordering, permission decision, dependency status, partial state, and cancellation | Add trace correlation across components when one event spans them |
| Packaged | Integrated record plus built-artifact hash, install identity, prior version, mutations, rollback or upgrade result, removal result, and residue inventory | Record retained user-owned data separately from package residue |
| Promoted template | Appropriate lower-level record plus copy identity, source template version, compatibility result, known descendant, migration, owner, and retirement signal | Aggregate privacy-safe support classifications when the population is defined |

**Minimum structured record**

Use target-native logs, test reports, traces, or journals, but preserve these semantic fields when applicable.

| Field | Purpose | Privacy and cardinality boundary |
|---|---|---|
| `artifact_id` | Stable demonstration or package identity | Bounded maintained identifier, not a local absolute path |
| `artifact_version` | Correlates claims, examples, and migrations | Version or content hash from the evaluated artifact |
| `evidence_status` | States conceptual through promoted level being evaluated | Enumerated status, never inferred from a green result |
| `target_environment` | Names host, schema, platform, and relevant dependency versions | Record only compatibility-relevant configuration, not full machine inventory |
| `operation_id` | Correlates selection, behavior, retry, effects, and recovery | Opaque per-operation identifier without user content |
| `parent_operation_id` | Links composed or delegated work | Include only when causal hierarchy is claimed |
| `fixture_id` | Identifies a sanitized regression case | Stable bounded name, with sensitive detail stored nowhere in routine telemetry |
| `intent_class` | Distinguishes in-scope, adjacent, unrelated, malformed, and unsupported requests | Classification rather than raw request text by default |
| `selection_decision` | Records selected, declined, routed, overlapped, or unavailable | Enumerated result plus destination identity where routed |
| `expected_observation` | Names the assertion used by the current gate | Stable claim identifier or concise expected class |
| `observed_result` | Records success, classified failure, cancellation, degradation, or unknown | Avoid dumping large output; link a bounded artifact when necessary |
| `effect_summary` | Reports declared files, processes, network, settings, or retained data changed | Resource class and owned identifier, with secrets redacted |
| `attempt_ordinal` | Exposes retry behavior inside one operation budget | Bounded integer only when retry is activated |
| `failure_class` | Distinguishes transient, permanent, denied, contradictory, cancelled, partial, or unknown | Stable controlled vocabulary with original cause preserved |
| `recovery_decision` | Names retry, repair, rollback, route, demotion, retirement, or no action | Must correspond to a tested safe state |
| `final_state` | Confirms success, unchanged, rolled back, partially repaired, retained-data, or unknown | Prefer resource observation over prose assertion |
| `evidence_health` | Reports whether collectors, validators, and correlation operated correctly | A failed collector makes the run unknown |
| `owner` | Identifies the role responsible for response | Role or queue, not unnecessary personal metadata |
| `observed_at` | Supports expiry and event ordering | Use target-consistent timestamp semantics and document clock limits |

**Authoring evidence checklist**

- Record the exact reference, packet, and journal paths owned by the lane.
- Record archive seed path, content hash, heading sequence, and source-span or queue evidence used to freeze the baseline.
- Record local source paths, content hashes, duplicate relationships, and intentionally unrefreshed external links.
- Record which claims are local facts, refreshed target facts, inferences, examples, or unknown mechanics.
- Record each completed section boundary only after the packet section, reference section, and immediate sanity result exist.
- Record cumulative packet sections, exact question texts, mandatory field count, exact uniqueness, and prefix-stripped normalized uniqueness.
- Record heading order, per-section character comparison, ASCII, whitespace, marker, fence, table, and link results.
- Keep the changed-path list exact and note any observed unrelated shared-workspace changes without modifying them.
- Summarize command results and decisive error lines; avoid retaining an indiscriminate shell transcript.
- Preserve unresolved risks, blocked claims, next action, and next assigned file in the progress journal.

**Behavior and integration checklist**

- Correlate discovery, selection, behavior, external call, retry, effect, and recovery under one operation identity.
- Record both positive and adjacent negative intent classes so activation counts have meaningful denominators.
- Distinguish no selection from loader unavailable and distinguish explicit refusal from collection failure.
- Preserve the original failure class when retries end in a different final error.
- Record whether output is fresh, cached, mocked, partial, or live; do not make these states visually equivalent.
- Record declared and observed effects, then compare them with a before-and-after resource snapshot.
- Record permission decisions and denial outcomes without exposing credential material.
- Record cancellation separately from failure and verify that pending work and queued retry stop as intended.
- Record dependency and compatibility versions with the result so stale observations can expire.
- Sample or aggregate only after defining the population and keeping severe categorical failures visible.

**Package and lifecycle checklist**

- Identify the built artifact by hash or immutable version, not only the source revision.
- Record installation identity, starting state, declared mutations, actual mutations, and installer outcome.
- For upgrade, record the prior version, migration path, compatibility decision, and rollback state.
- For removal, compare before-install, after-install, and after-remove inventories.
- Classify intentional retained user data separately from accidental residue.
- Record known copied descendants affected by a defect, plus migration, demotion, or retirement action.
- Keep owner and replacement route visible when the artifact can no longer be maintained.

**Choose the evidence form deliberately**

| Evidence form | Best for | Limitation |
|---|---|---|
| Structured log | Discrete decisions, errors, effects, and recovery | Weak for aggregation unless schema and population are stable |
| Counter or rate | Frequency across a defined population | Hides sequence and severity; requires a trustworthy denominator |
| Distribution | Latency, size, or reviewer-time variation | Instrumentation, sample, warmup, and environment can dominate |
| Trace | Causal work across components, retries, and asynchronous boundaries | Higher volume, correlation, and privacy cost |
| Resource snapshot | File, process, configuration, package, and cleanup state | Captures state at points, not every transition |
| Test report | Deterministic assertion and regression evidence | Synthetic cases may not represent actual requests |
| Journal checkpoint | Authoring ownership, decisions, changed paths, and next action | Human-maintained and unsuitable as runtime telemetry |
| Reviewer note | Lesson clarity, misleading implication, and copyability | Subjective; preserve rationale and disagreement |

Collect p50, p95, p99, reviewer time, tool-call count, context size, delegated work, or retry count only when that measure changes an explicit decision and its population is defined. A percentile over a tiny or mixed sample is not useful precision. Tool-call count can reflect tool granularity rather than efficiency. Reviewer time can reflect audience knowledge rather than artifact quality. Pair each measure with environment, version, sample construction, and a counter-measure.

**Privacy and retention boundaries**

- Classify intent instead of recording raw user content by default.
- Use obviously synthetic fixtures for secrets, paths, endpoints, identities, and personal data.
- Redact before persistence, and test the redactor with representative secret shapes.
- Do not use hashes as automatic anonymization for small or guessable sensitive values.
- Bound cardinality; do not place raw paths, request bodies, errors, or generated output in metric labels.
- Grant access according to the evidence purpose and delete incident-only detail after its approved retention period.
- Separate routine aggregate evidence from deeper incident traces.
- Document when observability itself makes an external call, writes a file, or changes timing.

**Example authoring record**

```text
artifact_id: example-plugin-demonstration-review-fixture
artifact_version: review-fixture-v1
source_seed_version: sha256-347fac4364c59babf2991db65d50e4231f8ecce0834712e1b524cfce17a9652a
evidence_status: source-valid
workflow_phase: red
operation_id: beta-assignment-04-section-022
fixture_id: observability-checklist-rewrite
expected_observation: packet-first-reference-second-sanity-pass
observed_result: pass
effect_summary: assigned packet, assigned reference, beta progress journal
final_state: section saved and structurally valid
evidence_health: exact and normalized uniqueness checker passed
owner: beta lane
```

**Example privacy-safe activation record**

```text
artifact_id: focused-skill-format-example
artifact_version: local-example-v1
evidence_status: behavior-validated
operation_id: fixture-negative-adjacent-01
fixture_id: adjacent-deployment-request
intent_class: adjacent-out-of-scope
selection_decision: declined-and-routed
expected_observation: deployment work is not captured by format skill
observed_result: expected route returned
effect_summary: none
final_state: unchanged
evidence_health: pass
```

The record does not need the original private wording to establish that the classified negative case followed the declared route. When wording itself is under test, use a reviewed sanitized fixture in the test corpus rather than routine telemetry.

**Observation-path verification**

1. Produce one known success and confirm every required identity and result field.
2. Produce one known classified failure and confirm the original cause, recovery decision, and final state.
3. Exercise an adjacent negative case and confirm it contributes to the correct denominator without storing private text.
4. Exercise retry and cancellation where claimed, checking correlation and total attempt visibility.
5. Create a declared side effect, recover, and compare logs against the resource snapshot.
6. Disable or corrupt the collector and confirm evidence health becomes failed or unknown.
7. Inject a secret-shaped fixture and confirm it is rejected or redacted before persistence.
8. Change the artifact or host version and confirm stale evidence is not silently reused.
9. Review retained fields against their named decisions and remove unused collection.

Good observability records a bounded request class, selection decision, artifact and host version, observed effects, safe end state, and evidence health. Bad observability emits raw prompts, credentials, full output, and local paths into an unbounded label while logging only successful cases. Borderline observability enables a detailed trace for a controlled incident; it is acceptable when access, retention, redaction, and disabling behavior are explicit.

Treat the observation pattern as part of promotion review because copiers often preserve it. The safest reusable default records decisions, evidence status, effects, and recovery, not private content or hidden-thought narration.

## Performance Verification Method

Performance is a claim only when time, throughput, resource use, or reviewer effort changes the teaching or implementation decision. A static source-valid example can be complete without a latency target. When performance is claimed, verify the complete user outcome within a declared workload and environment; do not time a convenient component and generalize it to discovery, installation, invocation, diagnosis, or removal.

No current numeric result or universal budget is supported by the frozen corpus. Tool-call count, source count, wall time, reviewer time, and percentiles become evidence only after their population, boundary, and decision use are defined.

**Select the performance question first**

| Performance question | Operation boundary | Primary measure | Required guard |
|---|---|---|---|
| Can a learner choose the correct surface efficiently? | From documented starting state to an adopt, adapt, avoid, or route decision | Completion distribution and first-blocking assumption | Independent reviewers, correct decision, and no unrelated required files |
| Can a learner copy and validate the example efficiently? | From clean workspace to declared evidence status | End-to-end completion and setup or recovery breakdown | Final artifact, hidden-state check, and side-effect inventory |
| Does target discovery remain responsive? | From host discovery request to selected or declined result | Latency and resource distribution by intent class | Positive, adjacent negative, overlap, and unavailable-host outcomes |
| Does invocation meet an operational objective? | From accepted operation to promised result or bounded failure | End-to-end latency, throughput, queue, and resource use | Output correctness, attempt budget, cancellation, and effect count |
| Does an external dependency dominate? | From dependency admission through response, degradation, or failure | Dependency latency, retries, wait, and fallback classification | Freshness, quota, privacy, idempotency, and total deadline |
| Can package lifecycle complete within an acceptable window? | From clean pre-state through install, upgrade, repair, or removal to verified final state | End-to-end duration and mutation or resource distribution | Correct package, rollback, residue, and retained-data assertions |
| Can reviewers detect regressions efficiently? | From changed artifact to evidence-backed release decision | Review duration and classification of missed or disputed issues | Stable reviewer task, claim matrix, and known-defect controls |

**Required measurement record**

| Field | Requirement |
|---|---|
| Decision | Name the action a result can change: optimize, split, narrow, reject, demote, increase capacity, or keep current design |
| Claim | State the operation, workload, environment, statistic, bound or comparison, and evidence status |
| User outcome | Define success, explicit bounded failure, degradation, cancellation, and correctness assertions |
| Timed boundary | Identify setup, discovery, queue, execution, retry, cleanup, and reporting phases included or excluded |
| Workload strata | Separate input size, intent class, success or failure, cache state, dependency state, and concurrency where relevant |
| Environment | Record artifact, host, schema, platform, dependency, hardware or capacity class, and relevant configuration versions |
| Baseline | Preserve the current or comparison implementation and run it under the same controlled method |
| Repetition | Use enough repeated observations to expose variance for the local decision; report the actual sample count |
| Order | Interleave or randomize baseline and candidate when drift or warmup could bias one side |
| Warmup and cache | State cold, warm, primed, reset, or mixed behavior and never combine them without justification |
| Resources | Capture only decision-relevant CPU, memory, allocation, disk, network, context, tool, queue, or external cost |
| Instrumentation | Estimate observer overhead and keep collection consistent across comparisons |
| Result summary | Report raw count, center, spread, tails where supported, outliers, failures, and missing observations |
| Correctness guard | Assert output, selection, side effects, recovery, and evidence health for every measured class |
| Uncertainty | State sampling, representativeness, environmental, and measurement limits |
| Pass action | Define what result changes the design and what evidence restores status after regression |

**Method A: learner and reviewer workflow**

1. Freeze the audience, starting state, allowed references, requested decision, and correct completion criteria.
2. Use a clean workspace without author caches, untracked files, credentials, or prior conversational context.
3. Give reviewers the same bounded task and record the first blocking assumption, route, final decision, artifact status, and recovery needed.
4. Include unsuccessful and misrouted attempts rather than timing only completed cases.
5. Separate reading, setup, validation, diagnosis, and cleanup where the breakdown changes an edit decision.
6. Review qualitative causes alongside duration; a faster wrong decision fails the outcome guard.
7. Change one lesson element at a time when comparing versions, or label the comparison as a bundle.
8. Repeat with additional independent reviewers or controlled tasks when generalization matters.

Reviewer time is not an intrinsic property of the document. It varies with expertise, familiarity, environment, and task framing. Report those conditions and the observed cases; do not convert a small convenience sample into a universal productivity percentage.

**Method B: runtime or host behavior**

1. Define intent classes and input distributions, including positive, adjacent negative, malformed, unavailable dependency, cancellation, and recovery cases.
2. Set up a reproducible host environment and record its versions and capacity class.
3. Decide whether cold discovery, warm invocation, cache behavior, and initialization are separate user experiences; measure them separately when they are.
4. Assert semantic output and side effects before accepting a timing observation.
5. Include queue wait, nested retries, dependency calls, fallback, and cleanup inside the boundary when the user experiences them.
6. Run baseline and candidate under comparable conditions, interleaving order where drift matters.
7. Record every failed, cancelled, rejected, and degraded observation with its class. Do not omit them from throughput or latency interpretation.
8. Report counts and distribution summaries justified by the actual sample. Percentiles such as p50, p95, or p99 are inappropriate when the sample and workload do not support stable tail interpretation.
9. Profile or trace only after the end-to-end result identifies a bottleneck worth explaining.
10. Repeat after changing the suspected cause and verify both practical improvement and unchanged correctness.

**Method C: package lifecycle**

Measure clean install, supported upgrade, interrupted-operation repair, rollback, and removal as distinct workloads. Start from declared state, identify the built artifact, capture every mutation, and end with a resource inventory. Source compilation time is not installation time; successful install is not removal performance; fast removal that leaves residue fails correctness.

Include dependency resolution, registration, host restart if required, migration, validation, cleanup, and user-visible wait according to the actual contract. Separate network cache effects from package logic and record retained user-owned data explicitly.

**Validity and invalidation checks**

- The measured operation produced the promised outcome or a correctly classified bounded failure.
- Baseline and candidate used the same workload strata and compatible environments.
- Setup or cleanup was not moved outside the timed boundary selectively.
- Failed, rejected, cancelled, and degraded operations were not discarded silently.
- Cold and warm results, or cache hits and misses, remain distinguishable.
- Clock source and timing resolution are appropriate for the operation scale.
- Instrumentation and logging overhead are consistent and material overhead is disclosed.
- External-service changes, quota, network location, and concurrent load are recorded or controlled.
- Concurrency tests include admission and queue wait rather than measuring only active workers.
- Retries consume one operation-wide budget and their calls and delays remain visible.
- Memory, disk, network, token, or external cost is not exchanged for speed without reporting the tradeoff.
- The collector detects a known slow or failed case; otherwise evidence health fails.

**Method choices and blind spots**

| Method | Answers | Does not establish by itself |
|---|---|---|
| End-to-end benchmark | Whether the declared operation changed under controlled load | Why it changed or how actual users distribute requests |
| Microbenchmark | Cost of a narrow repeatable component | Discovery, queueing, dependency, cleanup, or learner outcome |
| Profile | Where CPU, allocation, or wait appears in one observed run set | A user-facing improvement or representative production behavior |
| Trace | Causal phases, retries, dependency waits, and effects | Stable aggregate performance without a defined sample |
| Load test | Behavior under a controlled concurrency and admission model | Compatibility with a different environment or real workload mix |
| Clean-copy study | Learner setup, comprehension, and diagnosis pressure | Runtime scalability or broad usability from a small cohort |
| Production observation | Actual workload behavior within collection scope | Causality without controlled comparison and privacy-safe classification |

**Common misleading results**

- A parser microbenchmark is used to claim that installation is faster.
- Only successful calls are timed, making quick failures look like throughput improvement.
- Warm cache observations are compared with a cold baseline.
- Setup, retries, queueing, or cleanup move outside the measured interval.
- A tiny mixed sample produces tail percentiles with unsupported precision.
- A remote dependency changes between baseline and candidate runs.
- Concurrency is increased without measuring rejected work, queue growth, or downstream pressure.
- Tool-call count is treated as efficiency even though one tool merely bundles more work.
- Reviewer time improves because reviewers already saw the earlier version.
- Faster output changes the answer, side effects, or recovery contract.

**Worked cases**

Good: compare two versions of a clean-copy lesson from the same starting state. Record correct routing, completion, first blocking assumption, setup, validation, and cleanup. A shorter completion is useful only if both versions reach the same evidenced result without hidden state.

Bad: time only metadata parsing and claim that users can install and invoke the plugin faster. The operation boundary omits discovery, package closure, host load, behavior, and lifecycle.

Borderline: collect live remote latency from one declared environment during an exploratory run. Preserve the raw observation and dependency state, but do not set a broad objective until workload representativeness, sample stability, cost, and failure classes are understood.

**Pass and fail decisions**

A performance claim passes when the workload and environment are reproducible, semantic guards pass, the comparison or bound is decision-relevant, variability and missing observations are visible, and the evidence supports no broader scope than reported. It fails when a faster proxy replaces the user outcome, correctness or recovery changes, collection health is unknown, or the result is generalized beyond its sample and environment.

Keep the smallest reproducible harness, fixture identities, baseline artifact, command or target adapter, result summary, and decision rationale under maintained ownership. Future maintainers should be able to reproduce why a budget exists, not merely rerun a number whose workload has drifted.

## Scale Boundary Statement

This reference is sufficient while one reviewable teaching contract can bound the learner outcome, surfaces, evidence, effects, environment, failure recovery, and ownership. It stops being the governing authority when operational or governance responsibilities dominate the lesson. The example may remain useful as a fixture, reproducer, or onboarding artifact after that boundary, but it must route production decisions to their real owners.

**Default sufficiency envelope**

- One primary learner decision with explicit non-goals.
- One primary extension surface, or a small composition whose interaction is the named lesson.
- Ranked and deduplicated evidence with finite retrieval and currentness boundaries.
- Deterministic local fixtures by default; live behavior isolated and separately labeled.
- Declared, bounded side effects and least privilege.
- One reproducible starting state, failure path, recovery state, and clean-copy route.
- One declared target environment or an explicit statement that target adaptation remains unverified.
- One accountable owner for the lesson, with specialized owners for any composed mechanics.
- No implicit production availability, multi-tenant isolation, regulatory, or broad distribution promise.

These are qualitative design boundaries, not universal file, token, request, or time limits. Local teams may add numeric thresholds after defining consequence, capacity, and evidence.

**Boundary dimensions**

| Dimension | This reference remains sufficient when | Boundary crossing signal | Required ownership or route |
|---|---|---|---|
| Teaching outcome | Examples support one decision or an explicit comparison | Independent outcomes require different audiences, success criteria, or conclusions | Split into focused demonstrations and retain a routing index |
| Surface count | One surface owns behavior or composition itself is the lesson | Commands, hooks, MCP, settings, skills, and manifest concerns accumulate without interaction assertions | Route each mechanic to its specialist and assign a composition owner |
| System interaction | Effects and failures can be reproduced in a bounded fixture | Several services, queues, databases, or agents share state and partial failure | Production architecture and integration guidance own the system contract |
| Source discovery | Canonical and supporting evidence can be ranked and retrieved finitely | Search is open-ended, versions conflict, or authority cannot be established | Narrow by source graph, domain owner, version, and claim before synthesis |
| Host environments | One declared host profile or a small owned matrix supports the claim | Platforms, versions, shells, architectures, or configurations expand faster than evidence | Compatibility owner and automated matrix decide supported scope |
| Input distribution | Sanitized fixtures cover the claimed selection and behavior boundary | Open-ended language, adversarial input, large data, or tenant-specific policy dominates | Target evaluation, security, and data owners define representative workloads |
| External dependency | A mock teaches the contract and live evidence is bounded | Availability, quotas, authentication, cost, protocol drift, or vendor behavior drives outcomes | Integration and operations guidance own timeout, retry, degradation, and incident policy |
| Privilege and data | Capability is narrow and fixtures are non-sensitive | Secrets, private data, broad filesystem, process, network, or administrative effects enter | Security, privacy, and platform owners approve design and evidence |
| Runtime traffic | The artifact is a controlled demonstration or diagnostic fixture | Production requests, concurrent users, queues, or shared dependency load rely on it | Service owner defines SLO, capacity, admission, resilience, and on-call response |
| State durability | Effects are local, reversible, and explicitly inventoried | Shared databases, durable remote mutations, migrations, or long-lived processes appear | Data and operations owners define transactions, backup, repair, and recovery |
| Package lifecycle | No distribution claim, or one maintained artifact has bounded lifecycle evidence | Multiple channels, versions, upgrades, supply chain, signing, or fleet removal appears | Release and supply-chain owners define provenance, rollout, rollback, and retirement |
| Reuse population | Use is local, supervised, and known | Independent teams, generators, public templates, or unknown descendants copy it | Template maintainer owns compatibility, migration, support, and security response |
| Availability | Explicit failure is acceptable for the teaching outcome | Users depend on uptime, bounded latency, disaster recovery, or geographic service | Production operations own measurable objectives and failure budgets |
| Governance | One accountable role can approve and retire the artifact | Several organizations, compliance regimes, or data jurisdictions must approve change | Governance and domain owners define policy and audit evidence |
| Authoring coordination | Exclusive paths and durable section boundaries prevent conflict | Parallel writers need the same artifact or evidence snapshot | Partition ownership, serialize shared edits, and run merge-time verification |
| Context capacity | Current decisions, evidence, and next action fit a durable journal and bounded source set | Repeated context loss, duplicated analysis, or unreviewable tool output appears | Split work, offload evidence, and appoint one integration verifier |

**Choose the boundary response**

| Response | Use when | Preserve | New obligation |
|---|---|---|---|
| Stay | The sufficiency envelope still holds | One complete learner journey and evidence record | Continue focused refresh and regression checks |
| Narrow | One claim or environment exceeds evidence but the core lesson remains valid | Demonstrated subset and explicit non-goal | Demotion note and route for excluded capability |
| Split | Independent lessons or owners can fail and evolve separately | Shared conceptual vocabulary and routing | Each child must be complete at its own status |
| Compose | Interaction among specialized surfaces is the primary outcome | Thin end-to-end scenario and cross-surface assertions | One composition owner plus specialist evidence owners |
| Mock and isolate | A live dependency adds disproportionate variability, privilege, cost, or privacy | Protocol shape and deterministic teaching path | Clearly separate mock evidence from controlled live validation |
| Promote | Repeated independent reuse justifies maintained template or package | Smallest complete example and copy workflow | Compatibility, security, lifecycle, migration, support, and retirement ownership |
| Escalate | Production traffic, sensitive data, irreversible state, multi-tenancy, or regulated behavior dominates | Example as fixture or reproducer | Production architecture, security, data, operations, and governance contracts |
| Retire | The host surface is unsupported, ownership is absent, or a maintained replacement is safer | Discoverable migration and historical evidence boundary | Remove active recommendation and track known descendant response |

Splitting is not sufficient when parts still share state, ordering, failure, or migration. Separate files can hide coupling. In that case, retain an explicit interaction contract and transfer system reliability to a production owner. Conversely, keeping everything together for narrative continuity is not sufficient when independent surfaces have different permissions, release schedules, or maintainers.

**Categorical escalation triggers**

Escalate beyond this reference as governing authority when any of these becomes part of the promised outcome:

- Production SLOs, capacity planning, admission control, incident response, or disaster recovery.
- Multi-tenant isolation, authorization policy, abuse resistance, or adversarial execution.
- Sensitive or regulated data collection, retention, residency, deletion, or audit.
- Irreversible or high-value external mutations without transactional and reconciliation ownership.
- Broad shell, filesystem, network, credential, or administrative privilege.
- Supply-chain provenance, artifact signing, registry trust, staged rollout, or fleet rollback.
- A compatibility matrix whose failures require coordinated customer or team migration.
- Several independent services or queues whose partial failures cannot be represented by one fixture.
- Unknown public descendants or a support population beyond the current maintainer's response capacity.

The trigger can be consequence rather than volume. A single low-traffic operation that exposes a credential or mutates shared production state requires stronger ownership than a heavily read static example.

**Distributed authoring boundary**

Shared-workspace scale is safe only with exclusive artifact ownership and durable integration points. Assign one writer per reference and packet. Save the complete packet section first, then the matching reference section, then run immediate sanity. Journal no later than each three-section boundary. During whole-file rereads, persist a review checkpoint at least every five sections. Never use parallelism to write the same file or to bypass evidence reconciliation.

If several agents must contribute to one future artifact, partition by independently mergeable files or gather read-only findings under one writer. Record the source snapshot or hash each finding used. Merge-time verification must recheck heading order, per-section expansion, unique packet values, tables, fences, ASCII, whitespace, markers, and changed-path ownership.

**Large evidence and codebase boundary**

A long file list is not context selection. Before applying this reference in a large repository:

1. Name the capability and decision whose evidence is required.
2. Rank canonical target-owned sources before contextual examples.
3. Deduplicate identical content and record version relationships.
4. Narrow code by entry point, dependency, caller or callee relation, configuration ownership, and affected lifecycle.
5. Load the smallest spans that can confirm or refute the claim.
6. Preserve unresolved source conflicts rather than blending them into a smooth synthesis.
7. Escalate when evidence discovery remains open-ended or no owner can resolve authority.

**Scale review worksheet**

At authoring, promotion, every new surface or permission, every new external dependency, and every audience expansion, record:

- primary learner outcome and highest evidence status;
- surfaces and their specialized owners;
- interaction edges, shared state, and partial-failure boundaries;
- source authorities, versions, duplicates, and refresh triggers;
- hosts, platforms, configurations, and compatibility claims;
- input classes, sensitive data, and adversarial assumptions;
- declared effects, privileges, external calls, and cleanup;
- runtime traffic, concurrency, queue, availability, and dependency expectations;
- package channels, upgrades, rollback, removal, and retained data;
- known distributions, copied descendants, support owner, and retirement route;
- boundary crossings, chosen response, and evidence required to return.

**Worked profiles**

In scope: a local skill-format demonstration teaches one activation boundary with sanitized positive and negative fixtures, source-valid structure, no live dependency, no package claim, and an independent clean-copy review. This reference can own the complete lesson.

Out of scope as architecture: a multi-tenant service exposes remote tools, stores credentials, processes production traffic, writes durable shared state, and promises availability across regions. This reference can supply a small mocked example, but service, security, data, SLO, capacity, and incident decisions require production owners.

Borderline: a command and validation hook demonstrate coordinated policy. Keep one composition example when ordering and recovery are the lesson, route command and hook mechanics to their specialists, and escalate if the same pair begins enforcing shared production state or high-consequence policy.

Hidden distribution scale: a static source-valid example is copied into generators across several teams. Runtime traffic remains absent, but compatibility, copied defects, migration, and retirement now require a maintained-template contract. Promote it with ownership or narrow the reuse claim.

Scale is crossed when externalities require a new operating contract, not merely when source or traffic becomes large. Preserve the demonstration as a bounded teaching or diagnostic artifact where useful, but do not let familiarity turn it into an implicit production design.

## Future Refresh Search Queries

No browsing occurred during this evolution. This section is a future retrieval and reconciliation plan, not evidence that the target host, schema, examples, or inherited external pages are current. Run a query only after selecting the target product, exact version, extension surface, and implementation decision it can change.

The seed phrases are too broad for implementation authority. Searching for "example plugin demonstration patterns best practices" is likely to retrieve derivative advice, unrelated products, and pages that repeat the topic words. Construct each future query from the actual target host name, exact release or version, exact surface or field, and the authority type needed.

**Refresh triggers**

Begin an authorized refresh when one of these events affects a material claim:

- A target validator, loader, trigger, or behavior gate changes or fails.
- A host or protocol version is adopted, deprecated, or removed.
- Manifest, command, hook, skill, MCP, settings, permission, or package schema changes.
- Installation, upgrade, removal, rollback, or residue behavior differs from recorded evidence.
- A security advisory or permission-model change affects the example.
- A maintained template copy reports an incompatibility or misleading lesson.
- A new surface is added to the capability contract.
- A current authoritative source conflicts with the frozen local corpus or another target-owned source.

Do not refresh merely to make the bibliography longer. Stop when the material decision is resolved, applicable evidence is recorded, and affected behavior has been reproduced or left explicitly conditional.

**Target and metadata query families**

| Query label | Terms to combine with actual target name and exact version | Preferred authority | Decision and stop condition |
|---|---|---|---|
| `official_extension_index` | extension development official documentation supported surfaces | Product owner documentation or locally installed official help | Identify canonical vocabulary and supported surfaces; stop when the target-owned index and version boundary are clear |
| `skill_metadata_schema` | skill metadata frontmatter schema required fields description validation | Published schema, official skill docs, or target validator help | Adapt the illustrative skill format; stop after schema validation succeeds and unsupported fields are removed |
| `skill_selection_semantics` | skill description activation selection matching overlap precedence | Official host behavior docs plus focused target cases | Define positive, negative, and overlap expectations; stop after current semantics and fixtures converge |
| `plugin_manifest_schema` | plugin manifest schema identity entry points compatibility dependencies | Official schema and manifest documentation | Establish package identity and declared surfaces; stop after a clean manifest validation and load observation |
| `plugin_directory_contract` | plugin directory structure required files optional directories discovery | Official structure docs and loader diagnostics | Distinguish required structure from illustrative possibility; stop after file closure and discovery pass |
| `command_registration_contract` | plugin command registration arguments output errors discovery | Official command development docs and schema | Implement a user-invoked surface; stop after positive, invalid-input, and unavailable cases pass |
| `hook_event_contract` | plugin hook events ordering timeout failure policy side effects | Official hook docs and event schema | Implement event-triggered behavior; stop after event, ordering, denial, cancellation, and recovery evidence exists |
| `settings_schema_precedence` | plugin settings configuration schema defaults precedence validation migration secrets | Official settings docs and migration guidance | Define persistent configuration; stop after precedence, invalid value, secret boundary, and migration cases pass |
| `permission_capability_model` | plugin permissions capabilities least privilege denial user confirmation | Official security and permission docs | Bound privilege and denial behavior; stop after capability inventory and denied-permission fixtures agree |
| `host_diagnostics_commands` | plugin validate inspect list load debug official command line | Version-matched official CLI help | Bind semantic gates to exact target commands; stop after known-good and known-bad artifacts are distinguished |

**MCP query families**

Use these only when an MCP capability is actually selected. A directory containing a skill does not become an MCP integration because an MCP repository exists.

| Query label | Terms to combine with current protocol revision and target host | Preferred authority | Decision and reproduction gate |
|---|---|---|---|
| `mcp_capability_selection` | MCP tools resources prompts capability negotiation official specification | Applicable protocol specification and target host docs | Select the correct primitive; reproduce discovery and unsupported-capability behavior |
| `mcp_resource_semantics` | MCP resources list read URI change notification pagination official specification | Current applicable resource specification | Define addressing and change behavior; test valid, missing, malformed, denied, and changed resources |
| `mcp_transport_lifecycle` | MCP transport initialization shutdown cancellation errors current specification | Protocol transport and lifecycle specification | Define process or connection ownership; test startup, timeout, cancellation, disconnect, and cleanup |
| `mcp_security_authentication` | MCP security authentication authorization least privilege user consent | Protocol and target security guidance | Bound identity and capabilities; test denial, expired identity, confirmation, audit, and no-secret logging |
| `mcp_server_example_version` | maintained MCP server release protocol compatibility installation | Publisher repository release and package metadata after normative semantics are known | Select an implementation example; reproduce exact tagged version in a clean environment |
| `github_mcp_operations` | GitHub MCP server repository issue pull request permission rate limit audit | GitHub-owned server docs and repository | Use only for a bounded GitHub outcome; test least privilege, unavailable service, partial effect, and cleanup |

The inherited MCP resource URL, MCP servers index, and GitHub MCP server repository remain unrefreshed retrieval targets recorded in the External Research Source Map. Inspect the currently applicable versions rather than assuming the inherited date-pinned resource page or a repository default branch still governs the selected target.

**Package and lifecycle query families**

| Query label | Terms to combine with actual package channel and version | Preferred authority | Decision and reproduction gate |
|---|---|---|---|
| `plugin_packaging_contents` | plugin package build include exclude entry point dependency official | Official packaging docs, package schema, and built artifact | Establish package closure; inspect actual contents and load from a clean host |
| `plugin_installation_path` | plugin install local project user scope official | Official installer or product docs and CLI help | Choose scope and mutation contract; compare clean pre-state and post-install state |
| `plugin_upgrade_migration` | plugin upgrade migration compatibility breaking change rollback | Official migration guide and release notes | Support or reject prior state explicitly; reproduce upgrade and rollback |
| `plugin_removal_cleanup` | plugin uninstall remove cleanup cache settings retained data | Official lifecycle docs and installer help | Define removal symmetry; compare post-remove state and intentional retention |
| `plugin_distribution_trust` | plugin registry marketplace provenance signing trust verification | Official distribution and security docs | Define publisher and artifact trust; verify built identity and channel policy |
| `skill_install_update_remove` | skill install update conflict source trust removal official | Official skill installation and distribution guidance | Promote a reusable skill only after clean install, conflict, update, and removal evidence |

**Release, compatibility, and problem-evidence queries**

| Query label | Search focus | Use | Limitation |
|---|---|---|---|
| `release_notes_breaking_change` | Exact target release plus extension surface, breaking, deprecated, removed, migration | Find version transitions and required action | Release notes may summarize rather than define full schema |
| `supported_version_matrix` | Exact plugin or protocol plus supported host versions and compatibility | Bound support claim and expiry | A published matrix still requires reproduction in the selected environment |
| `security_advisory_surface` | Exact host and surface plus advisory, vulnerability, credential, permission | Identify known security consequences and remediation | Search results are not a substitute for the publisher advisory and patched-version evidence |
| `official_example_repository` | Product owner plus exact surface, example, template, tag, release | Inspect maintained implementation after semantics are known | Examples can lag docs and may assume a different threat model |
| `maintainer_issue_failure` | Exact error or behavior plus target version and official repository issue | Discover known defects and workarounds | Issue reports are problem evidence, not normative contract |
| `removed_page_archive_check` | Exact former page title plus product docs and release migration | Determine whether guidance moved or was retired | An archive preserves history but not current support |

**Authority order by claim**

1. Current target-owned specification, schema, or generated validator and CLI help for exact machine contracts.
2. Current target-owned documentation for supported behavior, security, compatibility, and lifecycle.
3. Target-owned release notes and migration guides for change boundaries.
4. Tagged maintained source and built package metadata for implementation evidence.
5. Maintainer issues and advisories for observed failures and remediation context.
6. Community examples for additional questions, never as sole authority for target contract or security.

Authority is claim-specific. A protocol specification can define an MCP resource but cannot prove a host registers it. A host validator can accept metadata but cannot prove trigger quality. A repository can run but cannot establish broad support or safe permissions. Reconcile rather than average these roles.

**Reject or downgrade a result when:**

- publisher or product identity is unclear;
- the page targets another host, extension surface, transport, package channel, or threat model;
- version, release, commit, or checked date cannot be established for a changing claim;
- a mirror, summary, snippet, or generated answer lacks primary provenance;
- an untagged default branch is used to support a released version;
- popularity is substituted for maintenance, compatibility, or security evidence;
- the result repeats a claim without schema, behavior, or lifecycle detail;
- the observed implementation contradicts the normative source and the conflict is unresolved;
- local success is generalized to public support without a compatibility statement;
- access restrictions prevent inspection of the material needed for the claim.

**Refresh record**

For each material query, persist:

| Record field | Content |
|---|---|
| Frozen question | Exact claim or decision that triggered refresh |
| Target | Product, surface, mode, exact version, and package or protocol channel |
| Query | Actual query text or direct retrieval route used |
| Source identity | Direct location, publisher, title, release or commit, and checked date |
| Bounded finding | Concise paraphrase of the relevant section without copying unrelated material |
| Evidence role | Specification, schema, host docs, CLI help, release note, migration, security, source, package, issue, or contextual example |
| Applicability | Why the finding does or does not govern this artifact and environment |
| Conflict | Disagreement with local corpus, another authority, target behavior, or prior guidance |
| Changed action | Keep, adapt, narrow, demote, migrate, reject, supersede, or no material impact |
| Reproduction | Focused static, selection, behavior, security, compatibility, package, or lifecycle observation |
| Residual uncertainty | Untested cases, unavailable environment, unknown descendants, or unresolved authority |
| Ownership | Maintainer and next event that requires refresh |

Allowed dispositions are `inspected`, `applicable`, `reproduced`, `reconciled`, `rejected`, `superseded`, and `no_material_impact`. Do not label a source reproduced when only the page was read. Do not label target behavior authoritative when it is merely observed locally.

**Reconciliation procedure**

1. Freeze the current claim, artifact status, and implementation decision before searching.
2. Identify the target and exact version; if those are unknown, remain in discovery and avoid implementation claims.
3. Retrieve the strongest claim-specific authority, then inspect release and migration context.
4. Record bounded findings and source roles before reading examples that could bias interpretation.
5. Compare with local evidence and preserve conflicts explicitly.
6. Adapt the smallest affected artifact and run the matching focused gate.
7. Reproduce a prior failure or deliberate mutation to show the changed guidance protects the intended boundary.
8. Review security, compatibility, package, and lifecycle consequences activated by the change.
9. Update known descendants and migration guidance when a promoted lesson changes.
10. Record the disposition, residual uncertainty, owner, and next trigger; stop searching when the material decision is resolved.

**Query quality examples**

Good future query construction combines the selected host name, exact host release, `plugin manifest schema`, and `migration`, then checks the official schema and release notes before validating a clean artifact. The query has a decision, authority, and stop condition.

Bad future query construction searches `best example plugin practices` and adopts a popular repository's folder tree as current target contract. It lacks product identity, version, authority, applicability, and reproduction.

Borderline use studies the GitHub MCP server after the user goal requires bounded repository operations. It becomes applicable only after protocol and host compatibility, authentication, least privilege, confirmation, rate or service failure, audit, partial effects, and cleanup are verified for the selected version.

Preserve rejected and superseded results when they are likely to recur. Durable negative knowledge prevents a later refresh from treating the same irrelevant repository or stale schema as new corroboration. A mature refresh process reduces future search while increasing the precision of what must be retested.

## Evidence Boundary Notes

Evidence role is claim-specific. A path proves location, a hash proves content identity, a source proves only what it actually states, a target run proves behavior only in its recorded environment, and a recommendation remains a judgment even when informed by strong evidence. Use the weakest accurate role and upgrade it only after inspection, applicability review, and the required reproduction.

No browsing occurred in this evolution. The inherited external URLs are unrefreshed retrieval targets, not `external_research_sourced_fact` claims. Current plugin manifest, command, hook, MCP-host, settings, package, permission, installation, upgrade, and removal mechanics remain unverified until a selected target and version are checked against authoritative evidence and focused behavior.

**Claim-level evidence roles**

| Evidence role | Meaning | Permitted use | Prohibited inference | Upgrade gate |
|---|---|---|---|---|
| `frozen_archive_seed` | The June generated reference read completely before evolution | Establish original headings, source text, section lengths, and inherited claims | The seed is not automatically correct, current, or evidence-backed | Reconcile each claim against mapped corpus and target evidence |
| `local_corpus_sourced_fact` | A bounded statement directly supported by a completely read local source span | Describe what that historical local artifact contains or instructs | Do not generalize to current host behavior or unrelated surfaces | Confirm current applicability against target authority and behavior |
| `duplicate_source_locator` | A second path has byte-identical content to a source already counted | Help readers locate the same material in another tree | Do not count it as independent corroboration | A materially different independently authored source requires its own role |
| `historical_pattern_inference` | A design lesson is inferred from dated local examples | Generate review questions and conservative starting guidance | Do not state current syntax, support, compatibility, or security as fact | Refresh target authority and test the adapted pattern |
| `external_mapping_unrefreshed_note` | A public location is retained for future authorized retrieval but was not inspected now | Plan a decision-specific refresh | Do not paraphrase its current contents or claim applicability | Inspect direct source, record version and date, assess applicability |
| `external_research_sourced_fact` | A future bounded statement is tied to an inspected direct public source | Support the exact claim within source scope and version | Do not let an official source for one product or version govern another | Reconcile conflicts and reproduce affected target behavior |
| `target_observed_fact` | A focused test or manual observation occurred in a recorded artifact and environment | Describe what happened for that exact version and configuration | Do not equate local behavior with normative support or broad compatibility | Add authority and representative environment evidence as needed |
| `normative_target_fact` | Current target-owned specification, schema, documentation, or help defines a contract | State supported mechanics within its version and applicability | Do not assume the implementation conforms or the example satisfies it | Validate the actual artifact and relevant failure cases |
| `combined_evidence_inference_note` | Several evidence roles are synthesized into a causal conclusion | Explain likely tradeoffs, boundaries, and review actions | Do not hide conflicts or present judgment as quoted source fact | Record assumptions, counterargument, disconfirming test, and decision |
| `recommended_default` | A conservative choice follows from evidence, risk, and engineering judgment | Guide implementation when assumptions match | Do not call it mandatory, universal, or source-required without authority | Replace or narrow when target evidence or outcome data contradicts it |
| `illustrative_example` | A synthetic case demonstrates reasoning or a semantic contract | Teach good, bad, borderline, and mutation cases | Do not copy syntax into a target without schema adaptation | Adapt to target, validate, and relabel at the attained status |
| `unknown_target_mechanic` | Required current behavior has not been established | Bound claims, block promotion, and identify the next verification | Do not fill the gap with analogy, popularity, or confident prose | Select target and version, inspect authority, then reproduce behavior |
| `superseded_evidence` | New authority or behavior has replaced a prior claim | Preserve history, migration rationale, and invalidation trail | Do not use it for new implementation except historical comparison | None; route to the replacement evidence |

**Frozen identity facts**

| Artifact relationship | Verified fact | Boundary |
|---|---|---|
| Archive seed and pre-evolution working reference | Both had SHA-256 `347fac4364c59babf2991db65d50e4231f8ecce0834712e1b524cfce17a9652a` | Establishes the exact starting artifact, not truth of its claims |
| Archived local skill and working local skill | Both had SHA-256 `87d90442621ace039aa3379805f99c3f95bf500e9f7b96f9e7876ac2dcf804f5` | Establishes one source at two locations, not two confirmations |
| Local skill corpus scope | Completely read 84-line copies describe a historical model-invoked skill with focused applicability, required `SKILL.md`, optional support directories, content guidance, examples, and overlap checks | Does not establish a complete current plugin package or any other extension surface |
| Inherited external map | Contains an MCP resource specification location, an MCP server index, and a GitHub MCP server repository location | None was browsed or used as a current factual source in this evolution |
| Target implementation | No target host, exact host version, package channel, or current validator was selected and executed for the demonstration | Runtime, compatibility, security, performance, and lifecycle results are unavailable |

The working reference is now a synthesis artifact. Its expanded causal explanations, boundaries, alternatives, counterexamples, verification procedures, uncertainty, and second-order insights are engineering recommendations unless a narrower evidence role is named. Their value lies in making decisions and tests explicit, not in pretending that the historical source stated every conclusion.

**What the local corpus supports directly**

- A focused skill has an entry file named `SKILL.md` in the historical artifact.
- Its description and content are intended to help selection and explain when the skill applies.
- Required and optional structure are distinguished rather than every possible directory being mandatory.
- Supporting references, examples, and scripts can be separated when they carry enough complexity to justify the split.
- Example guidance and overlap awareness are part of a useful skill lesson.

These are historical local facts and bounded pattern inputs. Exact metadata fields, accepted directories, loader behavior, selection semantics, precedence, and current support require target adaptation.

**What the local corpus does not establish**

- A current plugin manifest schema or package identity contract.
- Command registration, argument, output, or error behavior.
- Hook events, ordering, timeout, side effects, or recovery.
- MCP transport, capability negotiation, tools, resources, prompts, authentication, or shutdown behavior.
- Settings schema, precedence, persistence, migration, or secret handling.
- Permission declarations, user confirmation, or least-privilege enforcement.
- Package building, installation scope, marketplace publication, upgrade, rollback, removal, or residue behavior.
- Host compatibility, runtime reliability, throughput, latency, security, or production readiness.

No directory tree, generic best practice, or repository popularity may fill those gaps.

**Evidence dimensions are not interchangeable**

| Dimension | Question answered | Example evidence | Cannot answer alone |
|---|---|---|---|
| Identity | Is this the same artifact? | Content hash, immutable version | Authority, meaning, currentness, or behavior |
| Authority | Who defines the contract? | Product-owned specification, schema, or help | Whether the implementation conforms |
| Currentness | Which release or date does it govern? | Versioned docs, release, checked date | Applicability to another host mode or channel |
| Applicability | Does this claim govern the selected artifact and threat model? | Target and surface comparison | Whether behavior actually passes |
| Reproduction | What occurred in a recorded environment? | Focused test, clean-host observation, resource inventory | Public support or untested compatibility |
| Representativeness | Does the evidence cover the claimed population? | Defined workload, sample, and environment matrix | Normative requirement or causal explanation |
| Causality | Why did the outcome change? | Controlled comparison, mutation, trace, state transition | Universal behavior outside the experiment |
| Judgment | What should the team choose? | Explicit assumptions, alternatives, consequence, reviewer decision | Source-mandated truth without authority |

More evidence in one dimension cannot compensate for another missing dimension. Several hashes do not establish authority. Several popular repositories do not establish current support. A clean local run does not establish security. An official page does not establish that the artifact was packaged correctly.

**Prohibited evidence transfers**

- Two identical local paths become two independent confirmations.
- A historical skill tree becomes a current plugin manifest.
- An official MCP protocol page becomes proof of target-host registration.
- A repository example becomes normative security or lifecycle guidance.
- Successful schema parsing becomes host discovery or useful activation.
- Successful host loading becomes behavior validation.
- A behavior fixture becomes package installation, upgrade, or removal evidence.
- One environment becomes broad compatibility.
- A mock becomes live integration evidence.
- Absence of an observed failure becomes proof of safety.
- A research plan becomes a sourced public fact.
- A recommendation becomes mandatory merely because it appears in a reference.

**Claim evidence audit**

1. Isolate the consequential claim and the decision it changes.
2. Assign its weakest accurate role from the taxonomy.
3. Identify exact source location, bounded span, content hash or version, and capture date where applicable.
4. Check source identity and deduplicate equivalent material.
5. Confirm the source actually supports the paraphrase and preserve limiting context.
6. Separate authority, currentness, applicability, reproduction, representativeness, and judgment.
7. Record conflicts and counterevidence instead of smoothing them into one conclusion.
8. Map the claim to a focused observation capable of disproving it.
9. Test a deliberate mutation or known failure to validate the evidence path.
10. State residual uncertainty and prohibit the strongest likely overinterpretation.
11. Record owner, expiry or refresh trigger, and known dependent artifacts.
12. During skeptical reread, quote the sentence without surrounding caveats and verify its boundary still travels with it.

**Invalidation triggers**

Reassess a claim when its source content hash changes; its authoritative page moves or is superseded; the selected target or package channel changes; a validator or behavior disagrees; a new permission or side effect appears; a compatibility case fails; an example is promoted or copied; or ownership changes. Invalidate dependents at the claim level instead of treating the whole document as uniformly stale or current.

**Examples**

Good: "The two local skill paths are byte-identical historical evidence that this source uses `SKILL.md` and separates optional support content. Adapt metadata and loader behavior against the selected target before implementation." Identity, historical scope, and currentness boundary travel with the recommendation.

Bad: "Two examples prove the current plugin schema." The files are one duplicated skill artifact, no current schema was inspected, and skill structure does not establish plugin packaging.

Borderline: "The selected host loaded this candidate in the recorded environment." This is a useful `target_observed_fact` for debugging. It becomes a broader support claim only after current authority, representative compatibility, behavior, and lifecycle evidence justify that scope.

**End-state inventory**

- Known: exact frozen seed identity, exact duplicate local corpus identity, complete historical source scope, original heading order, evolved packet rationale, and focused local structural evidence.
- Inferred: conservative demonstration design, failure, reliability, retry, observability, performance, scale, and evidence recommendations derived from the source gaps and systems reasoning.
- Illustrative: skill-format candidates, route scenarios, state models, metric records, mutation cases, and query formulations that require target adaptation.
- Unknown: current target schemas, loader and selection behavior, permissions, protocols, package lifecycle, compatibility, numeric performance, and production outcomes.

Honest unknowns are operationally useful because they identify the precise authority and observation needed next. As reuse and consequence grow, maintain claim-to-source, claim-to-test, claim-to-owner, and claim-to-descendant relationships so a changed authority can trigger focused demotion and migration. The durable unit of maintenance is the claim and every artifact that depends on it.
