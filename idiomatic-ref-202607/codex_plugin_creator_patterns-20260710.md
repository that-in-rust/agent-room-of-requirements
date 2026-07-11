# Codex Plugin Creator Patterns

Use this reference to decide whether a Codex capability should become an installable plugin, then carry that plugin through a verified local lifecycle. A plugin is a composition and distribution boundary: it gives one identity to selected skills, apps, MCP server declarations, assets, scripts, hooks, and interface metadata. It is not automatically the best container for every extension request.

Choose a plugin when capabilities should be installed, discovered, versioned, and maintained together. Prefer a narrower surface when the request is only one repository instruction, one reusable skill, one hook policy, one MCP server integration, one app declaration, or one script with no plugin-level distribution need. If the user already selected a plugin and supplied the destination and components, honor that decision after checking existing state rather than reopening the entire surface menu.

The installed local creator currently defaults new marketplace-backed work to a personal plugin under `~/plugins/<normalized-name>` and the personal marketplace at `~/.agents/plugins/marketplace.json`. Use a repository or team plugin and `<repo-root>/.agents/plugins/marketplace.json` only when the user or current repository policy explicitly selects that shared destination. Destination must be decided before marketplace generation because `./plugins/<name>` resolves relative to the chosen marketplace root.

Follow this lifecycle:

1. **Select:** Decide whether plugin packaging is justified and whether this is a new scaffold or an update to an existing local plugin.
2. **Inspect:** Check the requested destination, normalized-name collision, existing manifest, marketplace entry, write authority, and selected optional components before creating or replacing files.
3. **Scaffold:** Run the installed creator from its skill root, generate the required `.codex-plugin/plugin.json`, and create only the companion folders or files the capability actually needs.
4. **Complete:** Replace generic generated metadata with truthful plugin identity and interface content. Keep folder, manifest name, marketplace name, and install identity aligned.
5. **Validate:** Run the installed `scripts/validate_plugin.py <plugin-path>` and then component-specific checks. A created directory is not evidence of an accepted manifest.
6. **Expose:** Add or update the intended marketplace entry. The default personal marketplace is discovered implicitly; a nondefault marketplace path needs explicit configuration before installation guidance can rely on it.
7. **Install and invoke:** Install from the verified marketplace name and test in a fresh Codex task so newly installed skills and tools are loaded.
8. **Update:** For an existing local plugin, preserve the source relationship, use the installed cachebuster helper, reinstall from the confirmed local marketplace, and test in another fresh task. Do not recreate the scaffold or hand-edit marketplace state as an update shortcut.
9. **Recover or remove:** Keep the prior identity, source, and marketplace relationship visible until replacement works. State how to restore, reinstall, disable, or remove the plugin and its entry without deleting unrelated marketplace content.

Current-local evidence materially differs from the archived creator. The archive used repository-root defaults and generated bracketed placeholder values for later editing. The installed creator now uses valid defaults, defaults to a personal marketplace, validates before handoff, and defines an explicit update/reinstall flow. The installed manifest reference still illustrates a `hooks` top-level field, while the installed validator rejects that field and the installed skill instructs creators to omit unsupported manifest keys. For current local generation, treat validator behavior plus the installed skill as the executable contract and retain the sample conflict as a documentation defect, not as permission to bypass validation.

Keep component presence and manifest declarations consistent. Add `apps` only when `.app.json` exists. Add `mcpServers` only when a companion `.mcp.json` exists or a valid inline server object is intentionally supplied. Optional hook folders may be part of plugin content, but the current local validator does not accept a `hooks` key in `plugin.json`. Asset fields must point to real files inside the plugin archive. Existing destinations and marketplace entries are preserved unless replacement is explicit; force is an overwrite decision, not an ordinary retry.

Separate success claims:

| lifecycle_claim | minimum_evidence | claim_not_yet_supported |
| --- | --- | --- |
| scaffold_created | expected plugin root and required manifest exist at the selected destination | manifest acceptance, installation, or component behavior |
| structure_valid | current local validator passes the exact plugin tree | marketplace discovery, fresh runtime pickup, or remote dependency health |
| marketplace_exposed | intended marketplace entry points to the intended local source and preserves unrelated entries | marketplace installation for a nondefault path or plugin invocation |
| installed | Codex lists or installs the intended plugin from the verified marketplace identity | newly changed components are loaded in the current task |
| invoked | a fresh task observes the expected skill, app, or tool behavior | every optional component, permission, authentication path, or failure recovery works |
| updated | cachebuster, reinstall source, and fresh-task behavior correspond to the edited source | safe rollback or removal unless those paths were also verified |

A good personal-plugin flow normalizes one name, creates only the requested skill and assets, supplies real metadata, passes current validation, adds the personal marketplace entry, installs from the read marketplace name, and verifies behavior in a fresh task. A bad flow overwrites an existing path, copies the conflicted sample literally, and reports success because the scaffold command exited cleanly. A borderline flow validates the source tree but tests an older installed copy; structure is sound while runtime pickup remains unproven.

This guide owns plugin packaging, marketplace relationship, local validation, and update handoff. Route the internal design of skills, apps, MCP servers, hooks, authentication, remote services, and organization policy to their specialist authorities. The three public MCP links in the seed were not opened in this evolution and remain future pointers only; they supply no current facts about protocol behavior or server implementations.

Proceed when plugin fit, destination authority, identity, selected components, executable validation, marketplace source, and test plan align. Preserve and stop when an existing path or entry may be overwritten, a nondefault marketplace is not configured, the installed source differs from the edited source, or a component's contract remains consequentially unknown. The goal is not a populated directory. It is a plugin whose source, package, marketplace, installed copy, behavior, and recovery story refer to the same intentional capability.

## Source Evidence Mapping Table

This map routes claims; it is not a source-count vote. The user chooses the desired plugin outcome, repository or organization policy constrains shared destinations, observed files and CLI state establish what exists, and the executed creator plus validator establish current-local generation and acceptance. Public links may clarify a selected MCP component after refresh, but they cannot decide whether a plugin should exist or authorize a marketplace write.

| source_location_path_key | source_category_artifact_type | evidence_status | source_usage_synthesis_role | important_boundary_or_conflict |
| --- | --- | --- | --- | --- |
| `agents-used-monthly-archive/codex-skills-202603/.system/plugin-creator/SKILL.md` | archived_local_creator | local_corpus_sourced_fact | Historical creator workflow for name normalization, repository-root generation, optional folders/files, marketplace entry shape, overwrite protection, and validation guidance. | It predates the installed personal-marketplace default, uses bracketed metadata placeholders, and does not define the current update/reinstall lifecycle. |
| `agents-used-monthly-archive/codex-skills-202603/.system/plugin-creator/references/plugin-json-spec.md` | archived_manifest_reference | local_corpus_sourced_fact | Historical field guide for plugin and marketplace manifests, relative paths, interface metadata, and marketplace policy values. | Its sample and field guide include a `hooks` manifest key that the installed validator rejects. Treat it as lineage, not current acceptance proof. |
| `~/.codex/skills/.system/plugin-creator/SKILL.md` | installed_current_creator | current_local_observation | Current-local workflow for personal defaults, explicit repo/team override, valid generated metadata, conditional companion fields, validation, marketplace configuration, update/reinstall, and final app handoff. | It describes this installed tool version, not a permanent platform contract; commands are relative to its skill root. |
| `~/.codex/skills/.system/plugin-creator/references/plugin-json-spec.md` | installed_current_manifest_reference | current_local_observation_with_conflict | Current-local presentation metadata, marketplace, companion-file, and validation notes. | Its top sample still includes `hooks`, while its validation notes and executable validator reject that key. Follow validator acceptance and flag the documentation mismatch. |
| `~/.codex/skills/.system/plugin-creator/references/installing-and-updating.md` | installed_update_reference | current_local_observation | Existing-plugin cachebuster, marketplace-name lookup, reinstall, source-match, nondefault marketplace, and fresh-task pickup procedure. | Applies only after a marketplace entry already points at the source being edited; it does not create or rewrite the initial entry. |
| `~/.codex/skills/.system/plugin-creator/scripts/create_basic_plugin.py` | executable_scaffold | current_local_executable_evidence | Defines normalization, 64-character maximum, personal destination defaults, validation-ready generated manifest, conditional apps/MCP declarations, marketplace defaults, append/replace behavior, and force guard. | Successful execution proves generated file effects for its inputs, not component behavior, CLI installation, or user authorization. |
| `~/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py` | executable_validator | current_local_executable_evidence | Defines accepted top-level and interface keys, required values, strict semver, URL, path, asset, skill, app, and MCP companion checks. | Validation mirrors this local ingestion contract; it can drift with later installed versions and does not test remote services or marketplace pickup. |
| `~/.codex/skills/.system/plugin-creator/scripts/update_plugin_cachebuster.py` | executable_update_helper | current_local_executable_evidence | Replaces any prior build suffix with one `+codex.<token>` suffix while preserving the pre-`+` version prefix. | It mutates only the source manifest version; reinstall and fresh-task verification remain separate steps. |
| `~/.codex/skills/.system/plugin-creator/scripts/read_marketplace_name.py` | executable_marketplace_reader | current_local_executable_evidence | Reads and validates the nonempty top-level marketplace name from the personal default or an explicit file. | It does not prove the marketplace is configured, local, or points to the edited plugin source. |
| `https://modelcontextprotocol.io/specification/2025-06-18/server/resources` | external_research_source_material | unrefreshed_external_pointer | Future primary source for resource semantics if the selected plugin actually exposes an MCP server whose resource behavior affects design. | Not opened in this evolution; the dated URL supplies no current protocol fact and does not define plugin manifests. |
| `https://github.com/modelcontextprotocol/servers` | external_research_source_material | unrefreshed_external_pointer | Future implementation index for bounded examples after a specific MCP server decision is made. | Not inspected; community/repository examples cannot establish current validator acceptance or local marketplace policy. |
| `https://github.com/github/github-mcp-server` | external_research_source_material | unrefreshed_external_pointer | Future GitHub-server example when a plugin intentionally composes that server and current repository evidence is needed. | Not inspected; it does not authorize credentials, network access, marketplace publication, or broad plugin scope. |

Use this retrieval order for a real creation or update:

1. Read the explicit request and current repository or organization instructions. Decide whether the capability needs plugin distribution and whether the destination is personal or repo/team.
2. Inspect existing destination and marketplace state without overwriting it. Record normalized name, plugin root, manifest identity, entry identity, and whether the selected marketplace is configured.
3. Identify the creator root that will actually run. Use its installed skill for workflow, its scaffold for generated behavior, and its validator for accepted structure.
4. Use archive files to explain historical examples or migrate a pinned old workflow. Do not combine archive defaults with current output unless the resulting tree passes the selected validator.
5. For an existing local plugin whose marketplace entry already targets the edited source, use the installed update reference and helpers rather than the new-plugin scaffold path.
6. Load component-specific references only after the selected plugin structure requires them. An app, MCP server, skill, hook, or asset has its own behavior and verification contract.
7. Refresh an external source only when browsing is allowed and a named public protocol or implementation fact can change the component decision. Record URL, access date, revision/version, applicable claim, and local consequence.
8. Stop retrieval when plugin fit, destination, identity, schema, overwrite boundary, marketplace relationship, validation, installation source, and recovery path are sufficiently determined.

**Directly observed source differences**

- The archived creator defaults output to a repository plugin directory; the installed creator defaults to `~/plugins` and the personal marketplace.
- The archived creator begins with bracketed metadata placeholders; the installed scaffold emits syntactically valid concrete defaults and the validator rejects unresolved placeholder markers.
- Both normalize names to lowercase hyphen form, cap names at 64 characters, keep folder and manifest names aligned, preserve marketplace ordering by append, and require explicit force for replacement.
- The installed scaffold declares `apps` and `mcpServers` only when companion content is requested. The installed validator requires corresponding content and rejects unsupported top-level keys.
- The installed update guide separates source editing, cachebuster mutation, reinstall from the marketplace name, and testing in a fresh task.
- The installed manifest prose is internally inconsistent about `hooks`; validator code and the current skill agree that generated `plugin.json` should omit that key.

Do not treat executable code as user authorization. A script can show that `--force` exists and what it replaces; only explicit intent and current policy can make replacement appropriate. Likewise, a validator pass establishes structural acceptance for this installed version, not that a remote MCP service responds, authentication works, a nondefault marketplace is configured, or Codex loaded the intended installed copy.

Good source use identifies the installed creator root, creates a personal plugin with only requested companions, validates against that root's validator, reads the actual marketplace name, installs from the matching source, and tests in a fresh task. Bad use copies both archived and installed samples into one manifest and suppresses validator errors as documentation disagreement. Borderline use follows the installed skill but invokes a repository-vendored archived script; it is valid only when that version is deliberately pinned and its output is validated by the intended runtime.

For each consequential claim, retain source identity, capture hash or version where useful, what the source establishes, conflict or portability limits, required authorization, operational verification, and invalidation trigger. Reopen dependent guidance when the installed creator, validator, CLI, marketplace policy, or component contract changes; do not reread unrelated sources merely because one helper changed.

## Pattern Scoreboard Ranking Table

The scores below are inherited corpus-priority metadata. They are not plugin acceptance rates, confidence percentages, installation success measurements, or a precedence rule that can override user intent, repository policy, validator output, overwrite protection, or component-specific safety. Consequence outranks numeric order.

| pattern_identifier_stable_key | pattern_score_numeric_value | pattern_tier_adoption_level | pattern_failure_prevention_target |
| --- | ---: | --- | --- |
| `codex_plugin_creator_patterns` | 95 | default_adoption_pattern_tier | Source Map First: Load local codex plugin material before synthesizing creator patterns recommendations. |
| `codex_plugin_creator_patterns` | 91 | default_adoption_pattern_tier | Evidence Boundary Split: Separate local facts, external facts, and inference before giving agent instructions. |
| `codex_plugin_creator_patterns` | 88 | default_adoption_pattern_tier | Verification Gate Coupling: Attach each recommendation to at least one command, checklist, or review gate. |

Apply the rows through a plugin lifecycle loop:

1. **Source Map First:** identify the requested outcome, current policy, existing destination, creator root that will execute, manifest/marketplace version, and only the component sources needed for selected companions. The result is an applicability map, not a bibliography.
2. **Evidence Boundary Split:** distinguish historical archive facts, installed current-local behavior, executable scaffold/validator evidence, observed generated or installed state, unrefreshed public pointers, and synthesis. A script can define file effects without authorizing them.
3. **Verification Gate Coupling:** attach every lifecycle claim to a precondition, expected state change, independent postcondition, and recovery route. Scaffolding, structural validity, marketplace exposure, installation, fresh-task invocation, update, and removal are separate claims.
4. **Repair the first failed dependency:** wrong surface returns to design; normalized-name collision returns to identity/overwrite review; wrong destination returns to user or policy; rejected schema returns to current validator and component structure; wrong marketplace source returns to installation diagnosis; stale runtime returns to update/reinstall and fresh-task verification.

Use consequence-scaled modes:

| mode | appropriate_scope | minimum_evidence |
| --- | --- | --- |
| compact personal | New personal plugin with one or two local components and no external service or replacement. | plugin fit, normalized name, destination absence, selected companions, generated diff, validator pass, personal marketplace source, and fresh-task observation |
| shared repo/team | Repository-owned plugin or marketplace with several contributors or review policy. | compact evidence plus repository authority, ownership, explicit paths, marketplace configuration, review, source control, update owner, and removal policy |
| integration-bearing | Plugin includes apps, MCP servers, authentication, external assets, or remote services. | shared evidence plus component schemas, permissions, secret boundaries, failure behavior, service/integration tests, and degraded-mode handoff |
| existing-plugin update | Marketplace entry already points to the local source being edited. | source/installed identity, pre-update manifest, cachebuster result, marketplace name, reinstall result, fresh-task pickup, rollback source, and no manual marketplace rewrite |
| replacement or removal | Existing plugin files or marketplace entries may be overwritten, disabled, or deleted. | exact inventory, user/policy authorization, unaffected entries, backup or recovery, target-specific action, and postcondition |

The three inherited controls need complementary plugin rules:

- **Surface Fit First:** package only capabilities that need shared plugin identity, installation, and lifecycle.
- **Destination Before Generation:** select personal versus repo/team roots before creating a marketplace entry.
- **Minimal Companion Set:** create only requested component folders/files and declare only companions that exist or are intentionally inline.
- **Identity Consistency:** normalized folder name, `plugin.json` name, marketplace entry name/path, install target, and observed runtime must refer to the same plugin.
- **Executable Contract First:** when prose samples conflict with the current validator, follow validation for generated output and record the documentation defect.
- **Overwrite Is Explicit:** inspect existing paths/entries and use replacement flags only for a named intentional replacement.
- **Runtime Pickup Proof:** validate source, install from the verified marketplace, and test in a fresh task before claiming the update is active.
- **Lifecycle Closure:** report recovery, rollback, disable, or removal behavior and preserve unrelated marketplace state.

Each control leaves inspectable evidence. Source Map First leaves selected source identities, versions/hashes, conflicts, and skipped-source reasons. Evidence Boundary Split leaves claim labels and applicability. Verification Gate Coupling leaves commands/reviews plus results. Surface Fit leaves a rejected alternative or a concise plugin justification. Destination Before Generation leaves one authorized root. Identity Consistency leaves matching names and paths. Runtime Pickup Proof leaves fresh-task behavior from the intended installed source.

Good application uses the installed creator, chooses a personal destination, creates only a skill and assets, reviews generated metadata, passes the current validator, adds the personal marketplace entry, installs from its read name, and verifies the capability in a fresh task. Bad application lists every source, copies the conflicted sample, force-replaces an existing plugin, and reports success from file creation. Borderline application validates the intended source but reinstalls a same-named plugin from another marketplace; schema validity passed while source identity failed.

Use discriminating fixtures. Keep manifest content constant while changing the creator root. Normalize two inputs to the same name. Add an `apps` declaration without its companion. Include the prose-only `hooks` key. Point a marketplace entry at another source. Reinstall without changing the cache identity. Test in the same task and then a fresh one. The selected action and completion report should change. A workflow that reports the same success for every fixture is matching command exits rather than lifecycle state.

Change scores only with recorded criteria or observed failure-prevention evidence. More importantly, preserve the chain `capability -> surface -> destination -> identity -> generated structure -> validator -> marketplace source -> installed copy -> fresh invocation -> recovery owner`. That chain makes source drift and partial success diagnosable and provides a stronger maintenance target than any numeric rank.

## Idiomatic Thesis Synthesis Statement

`local_corpus_sourced_fact`: The two mapped archive sources establish the historical creator and manifest guidance: normalized names, a 64-character maximum, matching folder/manifest names, required `.codex-plugin/plugin.json`, optional component structure, marketplace entry policy, relative source paths, explicit replacement, and a validation step. They also preserve older repository-root defaults and metadata placeholders.

`current_local_observation`: The installed creator now defaults new marketplace-backed work to a personal plugin, emits valid initial metadata, declares apps and MCP servers only with selected companions, validates generated trees, and supplies a cachebuster/reinstall flow for existing local plugins. Its manifest sample includes `hooks`, but its validator rejects that key and its skill says to omit unsupported fields. Current generated output should follow the executable validator contract while the prose conflict remains visible.

`external_research_sourced_fact`: No public source was inspected in this no-browse evolution. The MCP specification and repository URLs are unrefreshed pointers. They provide no current evidence for plugin manifests, MCP semantics, authentication, server behavior, or installation policy.

`combined_evidence_inference_note`: Reliable plugin creation preserves one intentional identity across `capability -> extension surface -> destination -> folder -> manifest -> companions -> marketplace entry -> installed copy -> fresh-task behavior -> update or removal`. Select plugin packaging only when installation and coordinated distribution justify it. For a new plugin without a shared-destination requirement, use the installed personal workflow and the smallest coherent companion set. For a repository/team plugin, require explicit destination authority and marketplace configuration. For an existing plugin, use the update/reinstall procedure rather than recreating its structure.

Treat the lifecycle as a bounded state transition:

- **Preconditions:** the capability needs plugin packaging; personal or repo/team ownership is selected; normalized identity does not collide unexpectedly; existing files and marketplace entries are inventoried; chosen components and their authorities are known; writes and replacement are authorized.
- **Action:** scaffold from the selected creator root, review generated content, complete truthful metadata, add only existing or intentional companion declarations, validate, expose through the selected marketplace, install from that marketplace identity, and invoke in a fresh task.
- **Postconditions:** folder, manifest, marketplace entry, install source, and observed runtime refer to the intended plugin; unrelated files/entries remain; pending component gates are named; recovery, update, and removal have owners.

The personal default is a reversible starting point, not a universal governance rule. Adopt a repository/team destination when collaboration, source control, policy, or shared distribution requires it. Do not infer that a repository-relative marketplace is installed merely because its JSON exists. Nondefault marketplaces need explicit configuration before installation guidance can rely on them.

Keep package and component claims separate. The plugin validator can establish current-local manifest, asset, skill, app, and MCP companion shape. It cannot prove remote MCP protocol behavior, app permission decisions, authentication, hook effects, organization approval, network availability, or end-user usefulness. Route those claims to component tests and current authorities.

Keep creation and update paths separate. A new scaffold establishes a package and optional marketplace entry. An existing-plugin update should first prove that the chosen marketplace already points at the edited source, then change the source manifest's cache identity, reinstall from the actual marketplace name, and test in a fresh task. Manual marketplace rewrites during that loop can hide a source mismatch rather than solve it.

Use the thesis for personal experiments, maintained local plugins, explicit repo/team bundles, and plugins composing selected skills, apps, MCP servers, assets, scripts, or hooks. Stop or route when the request is only a narrower component, marketplace ownership is unknown, an existing name/path may be overwritten, manifest prose conflicts with validation, a nondefault marketplace is not configured, installed source cannot be identified, or remote/security authority is required.

A good synthesis receives a direct request for a personal skill plugin, normalizes and checks the identity, creates only skill/assets structure, fills truthful metadata, validates, adds the personal entry, reads its marketplace name, installs, verifies fresh-task invocation, and records how to remove it. A bad synthesis creates every optional surface from an illustrative sample, forces replacement, and calls the resulting directory production-ready. A borderline synthesis validates a repo/team plugin but cannot observe marketplace installation; report source validity and a pending platform handoff instead of claiming installability.

Verification follows the identity chain. Confirm the request and policy, inspect destination state, review generated differences, run the validator from the executed creator version, run component-specific checks, compare marketplace path/name/source, observe install output, test in a new task, and retain the prior source/version for recovery. Any change to creator root, manifest, companions, marketplace entry, installed version, or component configuration invalidates dependent evidence.

The deeper principle is that plugin creation is local deployment. Editing correct source is insufficient when marketplace or installed cache still points elsewhere. Conversely, installation success is insufficient when the manifest bundles unsupported or unverified behavior. A durable handoff names which lifecycle stages are verified, which remain pending, which source is active, and who owns the next update or retirement.

## Local Corpus Source Map

Select local sources by lifecycle question and creator root. The archive documents the seed's historical toolchain. The installed root documents and implements current-local behavior. Prefer a coherent set of skill, scripts, references, and validator from the root that will actually execute; mixing versions is an explicit migration that needs generated-diff and validation evidence.

| local_source_filepath_value | captured_sha256 | local_source_title_or_role | use_when | exclusion_or_conflict |
| --- | --- | --- | --- | --- |
| `agents-used-monthly-archive/codex-skills-202603/.system/plugin-creator/SKILL.md` | `3b43cb214f458a1ae13e1b93a69e493241d8e12c5a474afe8ae81ae0507aa216` | archived `plugin-creator` workflow | Explaining historical repo-root defaults, optional structure, marketplace policy, overwrite handling, and original validation handoff. | Historical for this task; metadata-placeholder and destination defaults differ from the installed creator. |
| `agents-used-monthly-archive/codex-skills-202603/.system/plugin-creator/references/plugin-json-spec.md` | `5d7223255decc44fcb93f3aa80bb17afc1469b2d3c339d65d9473c5c0c54fcdd` | archived plugin/marketplace field guide | Migrating or auditing the archived creator's intended manifest and marketplace content. | Its `hooks` guidance is not accepted by the installed validator; do not use it as current schema proof. |
| `~/.codex/skills/.system/plugin-creator/SKILL.md` | `8fd56316b2c49cbdc657a5d197967a233018e1fada65b00a5dd030dce6499a6e` | installed current creator workflow | Choosing personal versus explicit repo/team destination, new versus update path, optional components, validation, marketplace configuration, install handoff, and current guardrails. | Current-local rather than universal; commands assume this skill root and may change after installation updates. |
| `~/.codex/skills/.system/plugin-creator/references/plugin-json-spec.md` | `eeb640130f69636affaa299d4170d5a7ae6a0ff978296ddf75c409ce6dd87b91` | installed manifest and marketplace explanation | Understanding current interface intent, marketplace fields, companion declarations, assets, and validation notes. | Its top sample includes a key rejected by the validator; check every generated field against executable acceptance. |
| `~/.codex/skills/.system/plugin-creator/references/installing-and-updating.md` | `b030517fe05b12dda71babe2890656d7c6db6a0111797e1d20d208804427276d` | installed existing-plugin update guide | Updating a plugin whose marketplace entry already points to the edited local source, then reinstalling and testing in a fresh task. | Does not create initial marketplace structure or repair a source mismatch; those preconditions must already hold. |
| `~/.codex/skills/.system/plugin-creator/scripts/create_basic_plugin.py` | `b5aa34f7f9dcec4bb007a66d65cff0c5c77a67042ae6c4de57d8ab7f4ef737d2` | installed executable scaffold | Determining exact name normalization, destination defaults, generated manifest, optional files/directories, marketplace append/replace behavior, and CLI arguments. | Does not validate component semantics or prove Codex installation/pickup. Existing manifest replacement can occur only under explicit force. |
| `~/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py` | `ebda00d55d7518b127f675f062fb5c6e7a1ffdc0a99df1a55ac594400d7d3228` | installed executable validator | Establishing current-local accepted manifest/interface fields, strict semver, paths, HTTPS URLs, assets, skill metadata, app content, and MCP declarations. | It validates package structure for this installed contract, not marketplace configuration, remote services, authentication, or end-user behavior. |
| `~/.codex/skills/.system/plugin-creator/scripts/update_plugin_cachebuster.py` | `4fe3c5a49212f6e30a2306e245c460e01aaf5e36bc8ad3dd2852c199257eff89` | installed cache identity helper | Replacing an existing build suffix with one Codex cache token before reinstalling an edited local plugin. | It writes the source manifest version and does not itself reinstall, verify source selection, or test fresh pickup. |
| `~/.codex/skills/.system/plugin-creator/scripts/read_marketplace_name.py` | `7659216759152f83087020b4d2971b4ad3cc13851e2614efc30fc2317ad59d96` | installed marketplace-name reader | Reading the install identity from the personal default or an explicitly selected marketplace JSON. | A nonempty name does not prove that Codex configured the marketplace or that its plugin entry points to this source. |

Hashes establish captured byte identity, not normative authority, correctness, future immutability, or portability. Expand `~` and resolve the creator root at operation time. Durable user guidance should use paths relative to that verified root rather than copy this machine's absolute home path.

**Task-triggered retrieval**

- For a new personal plugin, start with the installed skill and scaffold; inspect the validator before customizing manifest or companions.
- For an explicitly requested repo/team plugin, add current repository instructions, destination ownership, and marketplace configuration while using the same installed executable contracts unless a repository version is pinned.
- For manifest or interface metadata, use the installed reference for intent and the validator for acceptance. When they conflict, generate to validator behavior and file a documentation maintenance finding.
- For assets, skills, apps, or MCP declarations, inspect validator branches and load the specialist component reference. Do not create every optional surface by default.
- For an existing local plugin update, verify that a marketplace entry already points to the edited source, then load the update guide, cache helper, and marketplace-name reader.
- For archived migration, keep the archive skill and reference together, compare generated trees against the selected current validator, and record each adaptation.
- For runtime diagnosis, add actual plugin/marketplace state and fresh-task behavior; source documentation alone cannot show what Codex loaded.

**Lifecycle ownership**

| phase | primary_local_source | resulting_evidence |
| --- | --- | --- |
| select and locate | installed skill plus user/repository policy | plugin fit, personal/team destination, creator root, existing-state inventory |
| scaffold | selected `create_basic_plugin.py` | generated root, normalized identity, manifest, requested companions, marketplace effect |
| customize | installed skill and manifest reference | truthful metadata and intentional component declarations |
| validate | matching `validate_plugin.py` plus component tests | accepted package shape and bounded component evidence |
| expose and install | marketplace file, name reader, current Codex CLI state | source path, marketplace identity/configuration, install result |
| invoke | fresh Codex task plus component behavior checks | observed loaded capability and failure state |
| update | update guide, cache helper, source/marketplace identity | one cache suffix, reinstall source, fresh pickup, rollback locator |
| remove or recover | pre-action inventory, marketplace/install state, user/policy | exact target removed or restored while unrelated state remains |

The local map is insufficient for remote MCP protocol behavior, app permissions, authentication design, hook execution semantics, production service operation, or organization marketplace approval. Route those decisions to current specialist authorities and return their verification result to the plugin lifecycle record.

Good retrieval for a new personal skill plugin uses the installed skill, scaffold, and validator, then component-specific skill checks. Bad retrieval opens only the manifest sample and hand-builds every optional field. Borderline retrieval follows current prose but invokes a repository-pinned archive script; treat it as a versioned migration, not as the default installed workflow.

When a local source changes, reopen only dependent decisions first. A scaffold hash change reopens generated defaults and CLI flags. A validator change reopens accepted schema and fixtures. An update-helper change reopens cache/reinstall evidence. A manifest-reference change reopens field intent but not executable acceptance unless validator behavior also changes. Finish with a whole-reference coherence check because changed defaults can still alter downstream examples and handoffs.

## External Research Source Map

These URLs are future retrieval entrypoints. No browsing occurred during this evolution, so current content, redirects, revisions, supported features, security posture, and relevant passages remain unverified. They do not presently define Codex plugin manifests, authorize credentials or network use, establish marketplace policy, or prove any server is installed.

| external_source_url_value | external_source_name_text | appropriate_use_after_refresh | invalid_extrapolation | evidence_boundary_label_value |
| --- | --- | --- | --- | --- |
| `https://modelcontextprotocol.io/specification/2025-06-18/server/resources` | Model Context Protocol resource specification at a dated path | Clarify resource semantics for a selected MCP companion when the plugin's server behavior depends on that exact or a deliberately chosen version. | Treating a dated resource page as current protocol, a Codex manifest schema, or permission to expose data. | unrefreshed_external_pointer |
| `https://github.com/modelcontextprotocol/servers` | MCP server implementation index | Locate bounded implementation examples or maintained servers after protocol and component requirements are known. | Assuming indexed projects are compatible, production-ready, approved, or applicable to the plugin without pinned review and tests. | unrefreshed_external_pointer |
| `https://github.com/github/github-mcp-server` | GitHub MCP server repository | Inspect a pinned GitHub-oriented server implementation when the user explicitly wants that dependency and repository operations are in scope. | Inferring current tools, authentication, permissions, repository policy, or safe credential use from an unopened default branch. | unrefreshed_external_pointer |

Use external evidence only after local plugin design identifies a question it can answer. First decide that the plugin needs MCP at all. Inspect the intended `.mcp.json` or inline `mcpServers` declaration, current validator contract, local server configuration, permitted credentials, and expected tool/resource behavior. Then refresh the primary protocol or implementation source for the exact unresolved claim.

Pair external evidence with local and runtime evidence:

| evidence_layer | question_answered | cannot_answer |
| --- | --- | --- |
| current local validator | Is this MCP declaration structurally accepted in the selected plugin package? | Does the server implement or honor the declaration? |
| plugin declaration | Which named server/configuration does this plugin intend to expose? | Is the endpoint reachable, authenticated, authorized, or safe? |
| refreshed protocol source | What does the selected protocol version specify for the relevant capability? | Which version the current server actually implements or which data policy applies locally? |
| pinned implementation source | What behavior and configuration does that reviewed revision intend? | Whether the deployed instance matches it or the organization approves it. |
| integration fixture | Does the selected plugin/server combination perform expected success and failure behavior in a safe environment? | Future availability, production authorization, or every permission boundary. |
| live authorized observation | What is configured and observable in the target environment now? | General protocol guarantees beyond that observation. |

For Git mechanics, plugin manifests, marketplace generation, installation, and cache updates, use the current local creator, validator, CLI state, and repository policy. For MCP resource semantics, refresh a primary protocol source at the chosen version. For server code, inspect a pinned revision and its license, configuration, tests, and change history when relevant. For credentials and data access, use organization security policy and least-privilege design; public examples cannot authorize secrets.

Good external use says: "This plugin intentionally declares an MCP companion; the local validator accepts its declaration; a refreshed primary source at the selected version defines the required resource behavior; a pinned server revision and disposable integration fixture demonstrate the expected response; production authentication remains owned by security policy." Bad use says: "The GitHub MCP repository proves the plugin is safe to install." Borderline use copies an example configuration from a current-looking branch but never verifies protocol version, credential scope, or that the installed plugin loads that server.

When external evidence is refreshed, record:

- the plugin/component decision that triggered research and the consequence of error;
- exact URL, access date, source owner, version or commit, and relevant passage or code location;
- local plugin declaration and validator version to which the finding applies;
- security and credential boundaries, with secrets excluded from the record;
- safe integration fixture, expected failure behavior, and observed result;
- whether guidance is unchanged, clarified, contradicted, superseded, or unresolved;
- which reference section, component test, install step, or recovery rule changes;
- the next version, policy, incident, or fixture failure that invalidates the finding.

A URL, repository star count, default-branch example, or successful network call is insufficient by itself. Public capability does not imply local configuration; local configuration does not imply authorization; one successful invocation does not establish failure handling or data minimization.

Stop external research when another source cannot change the selected MCP declaration, version, permission, test, degraded behavior, or recovery path. Keep server-specific guidance modular so a plugin can replace or remove one integration without rewriting stable package identity, marketplace, validation, and update instructions.

## Anti Pattern Registry Table

Use this registry before any creator, marketplace, reinstall, replacement, or removal mutation. A blocker changes the selected extension surface, plugin identity, destination, existing user state, accepted schema, permissions, installed source, or recoverability. Presentation defects can be repaired proportionately, but they cannot justify a stronger lifecycle claim.

| anti_pattern_failure_name | failure_cause_risk_reason | safer_default_replacement_pattern | detection_signal_review_method |
| --- | --- | --- | --- |
| `context_free_summary_output` | The creator skips the selected local toolchain and gives generic plugin advice. | `creator_root_and_state_first` | Require the executed skill root, destination, existing-state inventory, and applicable component sources. |
| `unsourced_recommendation_claims` | Archive, installed behavior, executable validation, public pointers, and synthesis are presented as one authority. | `evidence_and_authority_split` | Trace every consequential rule to its source role, applicability, and verification. |
| `unverified_agent_instruction` | A lifecycle action has no precondition, postcondition, or recovery check. | `verification_gate_coupling` | Predict the exact file/entry/runtime change and compare it with observed post-state. |
| `plugin_for_every_extension` | A narrow skill, hook, MCP server, app, script, or repository instruction is bundled without installation or composition need. | `surface_fit_before_scaffold` | State what plugin-level identity, distribution, versioning, or coordinated lifecycle the request requires. |
| `mixed_creator_toolchains` | Instructions, scaffold, reference, and validator come from incompatible archive or installed roots. | `coherent_creator_root` | Record the executed root and compare hashes/versions; treat cross-version use as a migration. |
| `implicit_plugin_destination` | Personal or repo/team location is inferred and a marketplace write lands under the wrong owner. | `destination_before_generation` | Confirm personal versus shared destination, write authority, plugin parent, marketplace file, and installation implications. |
| `normalized_name_collision` | Distinct user labels normalize to an existing folder or entry and replacement occurs unexpectedly. | `normalize_then_inventory` | Compute the normalized name before mutation and inspect exact destination plus marketplace entries. |
| `all_optional_components_by_default` | Empty apps, MCP, assets, scripts, hooks, and skills are generated as speculative scope. | `minimal_companion_set` | Every optional folder/file has a named capability, owner, declaration, and verification plan. |
| `illustrative_sample_as_schema` | A prose example is copied even where current validator behavior differs. | `validator_backed_manifest_shape` | Run the selected validator and specifically test conflicted keys such as the illustrated `hooks` field. |
| `manifest_companion_drift` | `apps` or path-valued `mcpServers` is present without its required companion, or a companion exists but the intended declaration is absent. | `declaration_companion_consistency` | Compare manifest fields with `.app.json`, `.mcp.json`, inline server objects, and validator output. |
| `unresolved_generated_metadata` | Generic generated identity or unresolved placeholder markers are handed off as final plugin metadata. | `truthful_manifest_completion` | Review required manifest and interface values for real identity, audience, category, and prompts before validation. |
| `unsafe_force_replacement` | Force is used as ordinary retry when a plugin path or marketplace entry already exists. | `inventory_authorize_replace` | Diff existing files and entry, preserve recovery state, and require explicit replacement intent. |
| `marketplace_order_or_entry_loss` | Manual rewrite reorders plugins, drops unrelated metadata, or replaces a same-name entry unintentionally. | `structured_append_or_targeted_replace` | Parse JSON structurally, preserve root/interface and unrelated entries, append by default, and compare before/after order. |
| `unrequested_policy_override` | Installation, authentication, products, or category policy is changed because a sample includes it. | `defaults_with_explicit_overrides` | Keep current generated defaults and omit product gating unless user/policy supplies an intentional override. |
| `nondefault_marketplace_assumed_discovered` | A repo/team or custom marketplace file exists but Codex is never configured to use it. | `configure_then_install_nondefault` | Verify configured marketplaces or add the explicit marketplace root before plugin installation guidance. |
| `wrong_source_reinstall` | A same-named plugin is reinstalled from a marketplace that does not point to the edited local source. | `source_marketplace_identity_check` | Compare marketplace entry path, selected marketplace name, source root, installed identity, and plugin listing. |
| `manual_marketplace_update_loop` | Existing-plugin iteration edits marketplace/config state rather than preserving the known source relationship and changing cache identity. | `cachebuster_reinstall_update` | Confirm entry-to-source precondition, use the cache helper, read marketplace name, reinstall, and verify fresh pickup. |
| `same_task_runtime_test` | Updated skills or tools are tested only in the task that loaded the old plugin. | `fresh_task_pickup_test` | Reinstall, then start a new Codex task and verify the expected capability there. |
| `validation_equals_runtime_success` | A structural validator pass is reported as installation, invocation, remote integration, or security readiness. | `layered_lifecycle_claims` | Record scaffold, validation, marketplace, install, invocation, component, and recovery status separately. |
| `unsafe_asset_or_secret_handling` | Asset paths escape the archive, files are missing, or credentials are embedded in manifests, examples, logs, or public queries. | `archive_bounded_assets_and_secret_free_config` | Validate paths/files, keep secrets in approved mechanisms, and redact diagnostics while retaining nonsecret identity. |
| `external_example_without_pin` | Default-branch MCP examples are treated as current guarantees and copied into a plugin. | `versioned_external_component_evidence` | Refresh primary docs, pin implementation, map local declaration, and run safe integration/failure fixtures. |
| `orphaned_plugin_handoff` | The plugin is created or updated without install source, next owner, rollback, removal, or marketplace cleanup information. | `lifecycle_closure_record` | Require source, marketplace, version, observed pickup, pending gates, recovery, and retirement trigger in the handoff. |

Review in this order: requested capability, extension-surface fit, creator root, destination authority, normalized identity, existing state, selected companions, generated diff, validator contract, marketplace source/configuration, installation, fresh-task invocation, component behavior, and recovery. Skip a dimension only when it cannot affect the selected action. A design-only answer need not mutate or install; a non-marketplace plugin need not emit marketplace handoff links.

Do not ban flags or fields by spelling alone. `--force` is appropriate for an intentional reviewed replacement with recovery; it is unsafe as a response to an unexpected collision. A repo/team marketplace is appropriate when explicitly governed; it is excessive for an ordinary personal request. Inline `mcpServers` can be valid under the current validator; it still needs component and secret review.

Use the smallest remediation that preserves intent:

- Keep a narrow extension standalone when plugin distribution adds no value.
- Choose a different intentional identity or stop when normalization collides; do not silently fork or replace.
- Remove speculative companions and unsupported manifest keys, then validate again.
- Preserve existing plugin and marketplace state before an authorized replacement.
- Repair the marketplace-to-source relationship before entering the update loop.
- Treat a valid source tree as partial progress when marketplace configuration or runtime pickup is pending.
- Reinstall and test in a fresh task before diagnosing unchanged behavior as component failure.
- Route credentials, remote service, app authorization, or organization marketplace decisions to current owners.

Good remediation discovers that a sample key is rejected, removes only that unsupported declaration, keeps the hook folder if independently required, and reruns current validation. Bad behavior force-replaces an existing normalized name and edits unrelated marketplace entries. Borderline behavior manually edits marketplace JSON during a source-mismatch diagnosis; the edit may be valid in an explicitly reviewed repair, but it invalidates evidence about which source was previously installed.

Verify blocker detection with contrasting fixtures: two names that normalize identically; personal versus repo/team defaults; existing file and entry with and without explicit replacement; selected versus absent companion files; conflicted sample key; missing asset; same plugin name in two marketplaces; unknown-effect install; cache update tested in old versus fresh tasks; and targeted removal with unrelated entries. Pair executable results with authorization because filesystem and CLI state cannot establish user intent.

If an anti-pattern appears in the shared skill, sample, scaffold, validator, or update guide, contain its propagation and preserve a failing fixture before repair. Durable tooling changes need an owner, migration impact, rollback, and versioned tests. Merge duplicate warnings and retire a row only after the remaining preflight or validator still detects its high-consequence failure.

## Verification Gate Command Set

`verification_gate_command_set`: Verification has two independent targets: this evolved reference and a plugin lifecycle that applies it. Passing one does not imply the other.

For this reference, run the focused verifier from the repository root:

```bash
python3 tests/verify_idiomatic_reference_file.py \
  --path idiomatic-ref-202607/codex_plugin_creator_patterns-20260710.md
```

The final focused evidence must report 26 reference sections in exact seed order, 26 packet sections, 260 exact questions, 1,560 populated mandatory fields, `uniqueFieldCount=1560`, `normalizedUniqueFieldCount=1560`, every section strictly longer than its seed, and clean marker, ASCII, table, fence, and whitespace checks.

The archive seed also records this corpus-wide command:

```bash
python3 agents-used-monthly-archive/idiomatic-references-202606/tools/verify_reference_generation.py --stage final
```

That command covers the shared generated-reference corpus. Localize failures to their owning paths and do not edit another lane or the shared queue to make global output green.

For an actual plugin, identify the creator root that will execute. The installed commands below are relative to that root; a repository-vendored creator may expose different paths or behavior.

**Gate 1, nonmutating preflight**

Before generation or update, record:

- capability request and why plugin packaging is preferred over a standalone component;
- personal or repo/team destination, exact plugin parent, exact marketplace file, and write authority;
- requested name and normalized name, including exact existing plugin directory and same-name marketplace entries;
- new scaffold versus existing-plugin update, with the source path currently referenced by any entry;
- selected optional components and the specialist contract/test each requires;
- files and marketplace entry expected to change, plus preservation/recovery for existing state;
- creator skill, scaffold, validator, and helper identity or captured hash when version drift matters.

Do not use creation or force flags to discover whether a path is occupied. Inspect first. Do not print credential-bearing URLs, tokens, or private configuration into the verification record.

**Gate 2, authorized scaffold or update action**

For a new plugin, use the selected creator's scaffold after preflight. The installed creator exposes:

```bash
python3 scripts/create_basic_plugin.py <plugin-name> \
  [--path <parent-directory>] \
  [--with-skills] [--with-hooks] [--with-scripts] [--with-assets] \
  [--with-mcp] [--with-apps] [--with-marketplace]
```

Pass explicit repo/team `--path` and `--marketplace-path` only when that destination was requested. Use `--marketplace-name` only for the installed creator's documented new-marketplace exception. Use `--force` only for an inventoried and authorized replacement.

For an existing plugin whose marketplace entry already points to the edited source, keep the source mapping stable and use:

```bash
python3 scripts/update_plugin_cachebuster.py <plugin-path>
```

The helper changes the source manifest version. It does not validate, reinstall, or prove runtime pickup.

**Gate 3, generated diff and structural validation**

Review the exact generated tree before installation:

- `.codex-plugin/plugin.json` exists at the intended root;
- normalized folder, manifest name, and intended marketplace entry name match;
- required metadata is truthful and no unresolved generated marker remains;
- only selected companion folders/files exist and manifest declarations agree with them;
- unsupported top-level keys, including the currently conflicted illustrated `hooks` key, are absent;
- strict semver, HTTPS URL, interface, asset, skill, app, and MCP requirements match the selected validator;
- assets resolve inside the plugin archive and sensitive values are not embedded;
- existing files and unrelated marketplace entries are preserved as planned.

Then run the validator from the same installed creator root:

```bash
python3 scripts/validate_plugin.py <plugin-path>
```

Record validator identity, plugin path, exit result, and concise errors. A pass establishes current-local structural acceptance for those bytes. Any later manifest, companion, skill, app, MCP, or asset change invalidates it.

**Gate 4, marketplace source and configuration**

Parse the marketplace JSON structurally. Verify root name, intended ordered entry, exact normalized plugin name, `source.source`, relative `source.path`, policy fields, category, preserved root interface, and unchanged unrelated entries.

Read the marketplace name with the installed helper:

```bash
python3 scripts/read_marketplace_name.py
```

For an explicit nondefault file:

```bash
python3 scripts/read_marketplace_name.py \
  --marketplace-path <path-to-marketplace.json>
```

The personal default is discovered implicitly by the installed workflow. For an explicit nondefault marketplace, inspect current Codex configuration and add its marketplace root only when it is not configured and the user authorized that action:

```bash
codex plugin marketplace add <path-to-marketplace-root>
```

File existence and a readable marketplace name do not prove a nondefault marketplace is configured.

**Gate 5, installation and fresh-task pickup**

Install or reinstall from the marketplace identity that points to the edited source:

```bash
codex plugin add <normalized-plugin-name>@<marketplace-name>
```

Use current `codex plugin list` output when diagnosing which configured marketplace surfaces a same-named plugin. After installation or update, start a fresh Codex task and verify the intended skill, app, or tool appears and performs a bounded expected behavior. Testing only in the task that loaded the prior plugin does not establish pickup.

**Gate 6, component behavior and failure boundaries**

Run tests appropriate to selected components:

| component | required evidence | not established by plugin validator |
| --- | --- | --- |
| skill | valid skill metadata plus representative trigger and non-trigger behavior | usefulness, complete domain correctness, or implicit invocation policy beyond tested cases |
| app | accepted `.app.json`, intended app identity/category, permission and UX checks | remote application health, authorization, or organization approval |
| MCP server | accepted path or inline declaration, safe connection/transport fixture, expected tools/resources, error and cancellation behavior | production credentials, server version, protocol completeness, or remote availability |
| hooks | current hook-specific configuration and event fixture outside unsupported manifest fields | organization policy, every shell environment, or safety of unrelated hook actions |
| assets | real archive-contained files and renderer/ingestion observation where used | visual quality, licensing, accessibility, or correct branding by path existence alone |

Component failure does not necessarily invalidate the preserved package tree. Report package validation as verified and component behavior as failed or pending with an owner. Do not weaken credentials or permissions merely to obtain a green invocation.

**Gate 7, update, recovery, and removal postconditions**

For updates, verify one intended cache suffix, matching source and marketplace, reinstall result, fresh-task behavior, and a recoverable prior source/version. For failed installation or invocation, stop repeated marketplace edits, identify actual installed source, preserve diagnostics without secrets, and follow the failure/retry sections.

For removal or replacement, use current CLI help and repository/marketplace policy rather than inventing a fixed command. Inventory the exact installed plugin, source directory, marketplace entry, cache state, and any user-owned content. Verify only the intended target is disabled, removed, or restored and unrelated marketplace entries remain unchanged.

Use precise evidence states: `verified`, `pending`, `not_observed`, `not_applicable_with_reason`, or `blocked`. A good record says which creator generated the plugin, which validator accepted which bytes, which marketplace entry resolves to which source, which install identity was used, what a fresh task observed, what component tests passed, and how to recover. A bad record says "plugin created." A borderline record proves source validation but cannot inspect a managed marketplace; preserve the valid tree and hand platform exposure to its owner.

Improve the ladder when a consequential defect escapes. Add a fixture that discriminates safe and unsafe state, then decide whether it belongs in scaffold preflight, validator acceptance, marketplace tooling, component tests, or runtime pickup. Retire redundant checks that never alter action. The goal is a small maintained set with independent coverage of surface, identity, package, marketplace, runtime, and recoverability.

## Agent Usage Decision Guide

`agent_usage_decision_guide`: Use this reference when the user wants a new local Codex plugin, optional plugin structure, manifest/marketplace validation, an existing local plugin update, or a plugin-lifecycle diagnosis. A theme or source-path mention triggers classification and state inspection, not automatic generation.

Follow this operating sequence:

1. **Name the requested final state.** Determine whether the user wants design only, source scaffold, personal marketplace exposure, repo/team publication, installation, update, diagnosis, replacement, or removal. Honor a complete direct request after its safety gates.
2. **Select the extension boundary.** Confirm that installable plugin packaging is justified. Route a standalone skill, MCP server, app, hook, script, or instruction when plugin-level composition and distribution are not needed.
3. **Read current authority.** Identify repository/organization policy and the creator root that will execute. Use its skill, scaffold, validator, and helpers as a coherent versioned toolchain.
4. **Choose destination and identity.** Personal is the installed default; repo/team is explicit. Normalize the requested name, inspect exact folder and same-name entries, and stop before an unintended collision or shared write.
5. **Choose minimal companions.** Add only components with a concrete capability, owner, declaration, specialist test, and recovery boundary.
6. **Generate or update through the right path.** Use scaffold for new structure. Use cachebuster/reinstall only when an existing marketplace entry already targets the edited local source. Replacement needs separate authorization.
7. **Review and validate.** Inspect generated differences, complete truthful metadata, align declarations and companions, run the selected validator, and run component-specific tests.
8. **Expose and install only when requested.** Verify marketplace root/name/source, configure a nondefault marketplace when authorized, install from the matching identity, and avoid secrets in commands or records.
9. **Test fresh pickup.** Use a new Codex task for newly installed or updated skills/tools and verify bounded expected and failure behavior.
10. **Close the lifecycle.** Report source, manifest/version, marketplace, installed identity, verified stages, pending owners, rollback/recovery, and removal trigger.

Ask only for missing facts that can change extension surface, destination, overwrite, component scope, external permission, installed source, or recovery. Do not force a broad architecture questionnaire after the user has already supplied a safe personal-plugin request with an unused identity.

| task_signal | recommended_use_or_route | authority_boundary |
| --- | --- | --- |
| "Create a personal plugin containing this skill." | Use the installed personal default, create only skill-related structure, complete metadata, validate, expose/install if requested, and test fresh pickup. | The request does not authorize replacing a same-named plugin, adding unrelated components, or using a shared marketplace. |
| "Add MCP and app companions to this existing plugin." | Inspect source/marketplace identity, add only requested files/declarations, validate, run component tests, then update/reinstall. | Plugin validation does not authorize remote credentials, app permissions, or service deployment. |
| "Make this plugin available to the team repository." | Use explicit repo/team paths and current repository governance; verify the nondefault marketplace is configured before install guidance. | Shared destination, review, policy, and publishing are distinct from the personal default. |
| "Update my local plugin so Codex sees the changes." | Confirm the marketplace entry already targets the edited source, run the cache helper, read marketplace name, reinstall, and test in a fresh task. | Do not rewrite marketplace/config state to conceal a source mismatch. |
| "Build a reusable skill" with no distribution request | Route to skill creation and add plugin packaging only if the user later needs installation/composition. | A plugin is optional overhead, not the default synonym for a skill. |
| "Connect this remote MCP service." | Route protocol, transport, authentication, and service behavior to MCP integration; use this guide for the plugin wrapper if requested. | Public examples and local manifests do not authorize credentials or production access. |
| Existing normalized name or marketplace entry is found | Stop generation, inventory state, and ask or follow explicit policy for reuse, rename, update, or replacement. | Force is never inferred from the original creation request. |
| Validator and prose sample disagree | Follow executable acceptance for generated output, record the documentation conflict, and create a regression case. | Do not suppress validator errors merely because a sample contains the field. |
| Managed marketplace or install state is inaccessible | Preserve and validate source, produce the exact platform handoff, and mark exposure/install pending. | Do not claim marketplace or runtime success from filesystem state. |
| User requests plugin removal or replacement | Inventory source, installed identity, entry, user-owned data, unrelated entries, and recovery; use current CLI/policy. | Do not invent a removal command or delete broad marketplace content. |

This guide works for locally scaffolded personal plugins, explicit repository/team plugin sources, marketplace entries, current-local validation, and existing local updates. It is not the controlling workflow for component implementation, remote MCP deployment, authentication/security approval, organization marketplace administration, production service operation, or damaged installation state whose recovery needs platform ownership.

Use defaults as hypotheses. Personal location, `personal` marketplace name, `AVAILABLE`, `ON_INSTALL`, `Productivity`, generated `0.1.0`, and a normalized folder can all be valid while still being wrong for the explicit request or existing environment. Verify any assumption that changes ownership, visibility, installation, or replacement.

Good agent usage receives a direct personal-plugin request, verifies no normalized collision, creates only the requested skill and assets, validates, exposes through the personal entry, installs from the read marketplace name, tests in a fresh task, and reports removal. Bad usage asks the user to choose every component again and then force-overwrites a collision. Borderline usage completes a valid repo/team source tree but cannot inspect marketplace configuration; stop at a platform handoff and keep the stronger install claim pending.

Audit usage against the user's desired installed state. Record trigger, selected surface, destination, creator root, normalized identity, existing-state decision, component scope, generated changes, validator result, marketplace source/configuration, install/update action, fresh-task observation, rejected alternative when consequential, recovery, and next owner. Success is not the number of generated files; it is a correct, traceable, and reversible transition to the requested lifecycle state.

Repeated choices can improve tooling. If a team consistently uses one repository marketplace, component layout, validation suite, cache update, or handoff convention, propose an owned repository rule or creator option with fixtures. Do not promote one personal request, temporary path, or emergency replacement into policy without approval.

## User Journey Scenario

Role-based opening scenario: a user or agent-tool platform builder has a capability that may need to become an installable Codex plugin, or has an existing local plugin whose edits are not reaching Codex. The journey turns desired behavior, destination ownership, current plugin/marketplace state, and selected creator evidence into a validated source tree, a correctly sourced installation when requested, fresh-task behavior, and a recoverable handoff.

Open this reference when a task asks for plugin creation, optional plugin structure, manifest/marketplace work, validation, local plugin updates, or diagnosis of a stale installed copy. A mention of a plugin, creator path, skill, MCP server, app, or hook is a discovery signal, not proof that plugin packaging or mutation is required.

**Stage 1, frame the outcome:** State what should exist afterward. Is the deliverable a design, source scaffold, personal plugin, repo/team plugin, marketplace entry, installed plugin, updated plugin, repaired source relationship, or removed plugin? A direct request selects that stage; it does not authorize unrelated companions, replacement, credentials, or shared publication. Exit when the final state and excluded effects are explicit.

**Stage 2, choose the extension surface:** Decide whether the capability needs one plugin identity, installation, marketplace discovery, versioning, and coordinated component lifecycle. Route a standalone skill, MCP server, app, hook, script, or repository instruction when those plugin-level needs are absent. Exit with a concise plugin-fit reason or a named adjacent workflow.

**Stage 3, establish toolchain and authority:** Identify current repository/organization policy and the creator root that will execute. Keep that root's skill, scaffold, validator, references, and update helpers coherent. Determine whether the user authorized personal or repo/team state and whether platform/security owners are needed. Exit when the operator can name which local contract governs each mutation and validation.

**Stage 4, select destination and identity:** The installed creator defaults to a personal plugin and personal marketplace; shared destinations are explicit. Normalize the proposed name before mutation. Inspect exact destination folder, manifest, same-name entries in relevant marketplaces, and current installed/listed plugin state. Exit with one intended source identity and a preservation/replacement decision. A collision with unknown ownership blocks generation.

**Stage 5, choose minimal components:** Map each requested behavior to a skill, app, MCP declaration, hook, script, asset, or interface field. Create only components with an owner and test. Keep remote credentials and organization permissions out of generated content. Exit with a component inventory, package declaration plan, and specialist verification owners.

**Stage 6, choose new or update path:** For a new plugin, scaffold into the selected unused or explicitly replaceable destination. For an existing plugin, first verify that the selected marketplace entry already targets the local source being edited; then use the cache identity and reinstall flow. Do not recreate the package or rewrite marketplace state merely because runtime behavior appears stale. Exit with an authorized mutation and predicted files/entry effects.

**Stage 7, review and validate source:** Inspect generated differences, complete truthful metadata, ensure names align, remove unsupported fields, align companion declarations with real files or intentional inline configuration, and validate assets inside the archive. Run the validator from the selected creator root and component-specific checks. Exit with package bytes and a precise set of verified, failed, pending, or inapplicable component claims.

**Stage 8, expose and install:** When marketplace exposure is requested, verify that the intended entry points to the source created or edited. Preserve unrelated entries and ordering. The personal default is discovered implicitly by the installed flow; a nondefault marketplace requires explicit configuration. Read the marketplace name and install from that identity. Exit when the exact intended source is installed or platform work is handed off as pending.

**Stage 9, prove fresh pickup:** Start a new Codex task after install or reinstall. Verify the expected skill, app, or tool is visible and exercise one bounded success plus an important failure or unavailable-state path. A validator pass or same-task observation does not establish pickup. Exit with runtime evidence tied to the installed plugin identity and version.

**Stage 10, close the lifecycle:** Record creator root/version, source path, normalized name, manifest version, component inventory, validator result, marketplace file/name/source, installation result, fresh-task evidence, external pending gates, unrelated state, rollback/recovery source, removal trigger, and next owner. The journey can end with a valid source-only handoff when installation authority is unavailable, but must not call that state installed.

The primary journey is a direct personal skill-plugin request. The agent confirms that plugin distribution is wanted, chooses the personal default, normalizes the name and finds no collision, creates only skill and asset structure plus a personal marketplace entry, fills truthful metadata, validates the package and skill, reads the marketplace name, installs the intended source, starts a fresh task, exercises the skill, and reports how the source, entry, and installed plugin can be updated or removed. No shared repository or external service state is created.

Alternative exits change the required evidence:

- **Repo/team plugin:** require explicit repository paths, ownership, review, source control, marketplace configuration, update owner, and removal policy. Source validation can complete before a platform administrator exposes it.
- **Existing local update:** verify entry-to-source identity, change only intended bytes and cache identity, reinstall from the actual marketplace, test in a fresh task, and preserve the prior version/source for recovery.
- **Source-only delivery:** stop after generated-diff and validator/component checks. Report marketplace, install, and fresh pickup as not observed, with the exact next commands or owner if authorized.
- **Narrower component route:** preserve the capability request and move to skill, MCP, app, hook, or script guidance. Return only if plugin packaging later becomes a concrete requirement.
- **Collision:** preserve existing state and choose reuse, intentional update, explicit replacement, or a genuinely different identity. Do not silently append suffixes that fork product identity.
- **Blocked external integration:** keep local package evidence and route credentials, remote service, permissions, or managed marketplace work to the responsible owner.
- **Removal or replacement:** inventory source, entry, installed identity, user-owned files, unrelated marketplace content, and recovery before using current policy/CLI.

Evidence can expire between stages. A creator-root change invalidates command and generated-default assumptions. A package-byte change invalidates validation and component results. A marketplace edit invalidates source-resolution evidence. A cache/version or install change invalidates prior fresh-task observation. A policy or ownership change invalidates destination authorization. Refresh only dependent gates and then perform a final lifecycle coherence check.

Good completion is the requested, validated, correctly sourced, observable, and recoverable lifecycle state. Bad completion force-overwrites an existing plugin and reports success after directory creation. A borderline journey validates the intended repo/team source but cannot configure its marketplace; source work succeeded, exposure remains pending, and the handoff must name its owner.

Repeated friction should improve the creator environment. Recurring normalized collisions may need clearer names. Repeated unsupported sample fields need documentation and fixture repair. Wrong-source reinstalls may need stronger marketplace diagnostics. Same-task confusion may need a standard fresh-task handoff. Promote changes only with an owner and regression evidence so one exceptional plugin does not become an unreviewed global default.

## Decision Tradeoff Guide

Use this guide to choose a lifecycle path, not merely to decide whether the prose sounds well sourced. The governing default is a minimal personal plugin created with the installed creator when the user explicitly wants one installable identity, the normalized destination is free, requested companions are known, and local validation plus fresh-task testing are available. Every condition is a precondition to inspect, not implicit authority to mutate state.

Make decisions in this order because later evidence depends on earlier choices:

1. Define the requested observable end state: design, source, marketplace exposure, installation, fresh invocation, update, repair, removal, or replacement.
2. Decide whether one plugin identity and lifecycle are useful, or whether a standalone skill, app, MCP server, hook, script, or repository instruction is enough.
3. Establish destination ownership and mutation authority: personal state is the installed creator's default; repository, team, organization, and managed platform state are explicit choices.
4. Normalize and resolve identity across destination folder, manifest, marketplace entries, installed listings, and the source the user intends to edit.
5. Choose new creation, in-place update, diagnostic repair, or replacement. Unknown same-name state blocks creation and replacement.
6. Include only components required by requested behavior and supported by files or deliberate inline configuration.
7. Stop at the completion level requested and actually proved. Valid source is not installed behavior; installation is not fresh-task invocation; invocation is not remote-service approval.

| decision_option_name | when_to_choose_condition | required_action_and_boundary | tradeoff_cost_description | verification_question_prompt | reversal_or_stop_trigger |
| --- | --- | --- | --- | --- | --- |
| Adopt when | plugin packaging is explicit; the installed creator is the selected executable contract; personal ownership is appropriate; normalized identity is unused; components are bounded; and local validation, marketplace resolution, installation, and fresh-task proof are available if requested | scaffold the smallest package, inspect generated differences, complete truthful metadata, validate with the same creator root, expose or install only to the requested level, then test in a new task | fastest and most coherent route, but it assumes personal defaults remain suitable and creates package lifecycle work that a standalone component would avoid | Can a reviewer trace the requested capability through one normalized source, manifest, marketplace entry, installed identity, and fresh invocation without an unexplained gap? | switch to Adapt if ownership, component scope, or completion level differs; stop if identity or authority becomes ambiguous |
| Adapt when | plugin fit remains sound but the task is a repo/team source, an existing update, a source-only handoff, a nondefault marketplace, a governed component, or a locally conflicted creator/documentation case | preserve the plugin identity and lifecycle invariants while substituting explicit paths, owners, update mechanics, review gates, or pending platform stages; record which local contract wins and why | preserves user and repository fit, but adds coordination, evidence, recovery, and future-maintenance obligations | Are the stable assertions about identity, acceptance, source resolution, invocation, and recovery still proved under the changed mechanics? | return to Adopt only when the exception disappears; route or stop when the adaptation needs authority or evidence the operator lacks |
| Avoid when | the request does not need plugin distribution; a same-name asset has unknown ownership; creator roots cannot be reconciled; replacement is unrecoverable; shared publication is unauthorized; secrets or remote permissions are unresolved; or the requested postcondition cannot be honestly observed | preserve existing state, produce the smallest safe design or source artifact if useful, and route to the component specialist, owner, security reviewer, marketplace administrator, or source-resolution workflow with a concrete return condition | delays the full lifecycle and may require another owner, but prevents false success, identity forks, destructive replacement, and unauthorized exposure | Does the handoff identify the completed stage, preserved evidence, blocking precondition, responsible owner, and observation that permits work to resume? | resume only after the blocker is independently resolved; do not turn repeated installation attempts into a substitute for source identity |
| Cost of being wrong | any earlier choice targets the wrong surface, destination, identity, lifecycle, component set, or completion claim | stop new mutation, inventory source, entry, installed state, task evidence, and user-owned files; restore or preserve the last known-good state before selecting a corrected route | costs range from unnecessary package maintenance to overwriting an authoritative plugin, installing stale bytes, exposing unapproved capability, or giving a reviewer irreproducible evidence | Would an independent reviewer know exactly what changed, which claims are invalid, what remains authoritative, and how to recover without inspecting unrelated state? | escalate before cleanup when ownership is uncertain, evidence would be destroyed, or shared users may depend on the current installation |

The original four labels are outcome judgments. They do not replace the following operational tradeoffs.

| decision_axis | preferred_choice_when | alternative_choice_when | principal_cost | required_evidence |
| --- | --- | --- | --- | --- |
| plugin or narrower extension | choose a plugin when one installable identity, marketplace discovery, versioning, and coordinated components add value | choose a standalone surface when one component already solves the request without package lifecycle | plugin packaging adds manifest, distribution, update, removal, and cross-component obligations | requested observable outcome plus a reason one package identity is or is not useful |
| personal or repo/team destination | choose personal for an explicitly personal experiment or reusable local capability under the installed creator default | choose repo/team only for an owned shared deliverable with explicit paths, review, distribution, update, and removal policy | shared placement increases governance and blast radius; personal placement may not satisfy collaboration | path ownership, policy, reviewer, marketplace owner, and recovery plan |
| new or existing lifecycle | scaffold when normalized identity is free and no existing source is intended | update in place when an authoritative plugin and marketplace-to-source relationship are known | creation risks collision; update risks editing source that is not the installed source | folder, manifest, marketplace, install inventory, source target, and preservation state |
| implicit or configured marketplace | use the installed personal discovery flow for its intended default | configure or hand off a nondefault marketplace only when explicitly requested and authorized | custom configuration adds platform state and another identity boundary | marketplace name, file, source target, current configuration, and install result |
| source-only or runtime completion | stop at source when that is the request or platform authority is unavailable | install and invoke when runtime behavior is part of acceptance and state mutation is authorized | stopping early leaves distribution pending; continuing broadens effects and proof burden | validator and component results for source; marketplace, install, and fresh-task evidence for runtime |
| minimal or multi-component package | include only behavior necessary for the accepted capability | add companions when each has a concrete contract, declaration, owner, and test | each component creates independent configuration, security, compatibility, and recovery risk | component inventory, package linkage, specialist check, success case, and important failure case |

**Identity is the dominant tradeoff.** A syntactically valid source tree can still be the wrong plugin. Before creation or update, compare the normalized proposed name with exact destination folders, manifest names, relevant marketplace entries, installed/listed plugin identity, and the source path the user expects to own. A collision with unknown provenance is an Avoid condition. Silent suffixing is not a neutral fix because it creates a second product identity and can leave users invoking the old one.

**The installed creator is the executable local default.** The archive explains historical intent, but it does not run the current scaffold or validator. When an illustrative manifest conflicts with the installed validator, record the disagreement, use the validator and current creator instructions as the current accepted contract, and avoid copying the disputed field. Reconcile the creator root as a unit: skill, references, scripts, defaults, and validation behavior must come from the same selected toolchain unless an adaptation is deliberate and tested.

**Update is not creation with overwrite enabled.** An existing update first proves that the marketplace entry points at the local source being edited. Preserve prior source/version information, change only intended package bytes and cache identity, use the current helper-driven reinstall flow, and test in a fresh task. Recreating the directory or rewriting marketplace state can erase the source relationship needed to diagnose stale behavior.

**Partial completion can be correct.** A repo/team plugin may be valid and reviewed while marketplace configuration remains with an administrator. A remote component may be packaged correctly while credentials or service acceptance remain pending. Report those as bounded states: what passed, what was not run, which owner has the next gate, and what observation closes it. Never promote source correctness into an installation or service-readiness claim.

Contrastive cases make the rows operational:

- **Good adoption:** The user requests a personal skill plugin. The agent confirms plugin distribution, finds no normalized collision, scaffolds only the skill and required assets, replaces generated metadata with truthful values, validates with the selected creator, resolves the personal marketplace identity, installs it, and proves behavior in a fresh task. The handoff names source, version, entry, installed identity, and removal path.
- **Bad adoption:** The agent sees the word "plugin," generates every optional component, uses force against an unknown same-name destination, copies a sample field rejected by the current validator, and reports success after directory creation. The path is fast only because it skipped the decisions that establish correctness.
- **Good adaptation:** A team owns an existing plugin. The agent proves entry-to-source identity, modifies the intended package, follows the cachebuster and reinstall workflow, preserves prior recovery data, and records repository review plus fresh-task evidence.
- **Borderline adaptation:** The team source validates and component tests pass, but the operator cannot inspect or configure the managed marketplace. The source stage is complete; exposure and invocation remain pending with a named platform owner.
- **Correct avoidance:** A proposed normalized name collides with an existing plugin whose owner cannot be established. The agent leaves it untouched, inventories the conflict, offers reuse/update/intentional replacement or a genuinely different identity, and waits for an ownership decision.

Verify a chosen route with a compact decision record:

```text
requested_end_state:
selected_surface_and_reason:
creator_root_and_contract_version:
destination_and_authority:
normalized_identity_and_collision_result:
lifecycle_new_update_repair_or_replace:
component_inventory_and_owners:
package_validation_and_component_results:
marketplace_source_and_install_result:
fresh_task_observation:
rejected_alternatives_and_reversal_triggers:
recovery_source_and_next_owner:
```

Not every field applies to every completion level; mark a later stage as not observed with a reason instead of inventing evidence. Refresh the record when creator files, package bytes, marketplace targets, installed version/cache identity, task startup, policy, or authority changes. Package validation follows bytes and validator version; runtime proof follows the resolved installation and fresh task.

The strongest local facts are current script interfaces, generated defaults, validator acceptance, and helper-driven update steps. Packaging fit, organization governance, remote-service readiness, and future Codex CLI behavior retain judgment or version uncertainty. Apply confidence to each claim and evidence lifetime rather than calling the entire request certain or uncertain.

Finally, feed repeated decision costs back into maintained tooling. Recurrent collisions may justify clearer naming guidance; recurring unsupported fields call for sample and fixture repair; wrong-source reinstalls call for better diagnostics; repeated team-path questions may belong in repository policy. Promote a new default only with repeated evidence or a high-consequence escape, an owner, a regression case, and a way to reverse it.

## Local Corpus Hierarchy

The hierarchy answers a claim-specific question: which local evidence governs the next plugin action in this environment? It is not a blanket ranking of old versus new prose. Select one coherent creator root for current mechanics, retain archive material for lineage, and treat generated output as behavior to inspect rather than a specification to copy.

The default precedence is:

1. **Explicit project or organization policy** governs destination ownership, review, publication, credentials, replacement, and removal. It can override a personal path default, but it cannot make an invalid package valid.
2. **The selected current creator root** governs the workflow and intended contract for that execution. Keep its skill, references, scripts, and validator together.
3. **Executable behavior from that root** governs what the selected scaffold emits, what its validator accepts, and how its helpers transform update identity. Record command, target, result, and source hash.
4. **Current explanatory references** supply field meaning, lifecycle order, and caveats not encoded by an exit status. They remain subordinate to observed acceptance when the two conflict.
5. **Historical archive sources** establish prior defaults, persistent invariants, and migration context. Reconfirm any mechanic before using it against current state.
6. **Generated fixtures and real plugin examples** demonstrate behavior under a named version. They prove neither universal support nor semantic fitness for another request.
7. **External pointers not refreshed in this evolution** are discovery leads only. They do not override local evidence or support a current public-platform claim.

For this reference, the installed current creator root is `/Users/amuldotexe/.codex/skills/.system/plugin-creator`. Its files were read as a unit before synthesis. The archive paths remain mapped because they explain what evolved, but the archive does not execute the current scaffold or validator.

| local_source_filepath_value | corpus_hierarchy_role | observed_contribution | use_for | do_not_infer | sha256_at_evolution |
| --- | --- | --- | --- | --- | --- |
| `/Users/amuldotexe/.codex/skills/.system/plugin-creator/SKILL.md` | selected current workflow authority | current creation destination defaults, minimal plugin guidance, optional component rules, validation flow, update direction, and preservation safeguards | present operating sequence and creator-root ownership | that every illustrative value is accepted or every organization uses personal defaults | `8fd56316b2c49cbdc657a5d197967a233018e1fada65b00a5dd030dce6499a6e` |
| `/Users/amuldotexe/.codex/skills/.system/plugin-creator/references/plugin-json-spec.md` | current explanatory schema source with a known conflict | manifest field descriptions and an illustrative package shape | field intent, metadata review, and identifying claims to probe | acceptance of a top-level `hooks` field under the selected validator | `eeb640130f69636affaa299d4170d5a7ae6a0ff978296ddf75c409ce6dd87b91` |
| `/Users/amuldotexe/.codex/skills/.system/plugin-creator/references/installing-and-updating.md` | current lifecycle support | installed guidance for marketplace identity, source relationship, cache-aware update, reinstall, and fresh-task pickup | existing-plugin update and installation handoff | exact behavior of a future CLI version or a marketplace outside the observed environment | `b030517fe05b12dda71babe2890656d7c6db6a0111797e1d20d208804427276d` |
| `/Users/amuldotexe/.codex/skills/.system/plugin-creator/scripts/create_basic_plugin.py` | executable scaffold evidence | current name normalization, destination creation, valid default manifest generation, optional structure creation, and collision/force behavior | predicting and safely exercising new-package mutations | truthful final metadata, desired component behavior, or authority to overwrite | `b5aa34f7f9dcec4bb007a66d65cff0c5c77a67042ae6c4de57d8ab7f4ef737d2` |
| `/Users/amuldotexe/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py` | executable acceptance oracle for the selected root | current manifest and companion validation, strict version and URL checks, asset checks, and rejection of unsupported top-level keys | determining whether package structure satisfies this local creator contract | product usefulness, secure remote behavior, marketplace configuration, installation, or invocation | `ebda00d55d7518b127f675f062fb5c6e7a1ffdc0a99df1a55ac594400d7d3228` |
| `/Users/amuldotexe/.codex/skills/.system/plugin-creator/scripts/update_plugin_cachebuster.py` | executable update helper | current mechanism for changing cache identity during an existing local plugin update | update mutation after source identity is proved | permission to retarget a marketplace or replace an unrelated plugin | `4fe3c5a49212f6e30a2306e245c460e01aaf5e36bc8ad3dd2852c199257eff89` |
| `/Users/amuldotexe/.codex/skills/.system/plugin-creator/scripts/read_marketplace_name.py` | executable marketplace identity helper | current extraction of the marketplace name used by the install flow | avoiding a guessed install identity | that the marketplace is configured, points to the intended source, or is authorized | `7659216759152f83087020b4d2971b4ad3cc13851e2614efc30fc2317ad59d96` |
| `agents-used-monthly-archive/codex-skills-202603/.system/plugin-creator/SKILL.md` | historical primary workflow source | earlier repository-oriented defaults, name rules, scaffold sequence, and generated bracketed metadata behavior | lineage, changed-default detection, and historical intent | current destination, generated validity, or current installation mechanics | `3b43cb214f458a1ae13e1b93a69e493241d8e12c5a474afe8ae81ae0507aa216` |
| `agents-used-monthly-archive/codex-skills-202603/.system/plugin-creator/references/plugin-json-spec.md` | historical supporting schema source | earlier manifest explanation and sample field set | compatibility history and source-evolution comparison | current validator acceptance or present public API support | `5d7223255decc44fcb93f3aa80bb17afc1469b2d3c339d65d9473c5c0c54fcdd` |

The selected current sources establish several important changes from the archive. New marketplace-backed plugins now default to a personal plugin under `~/plugins/<name>` and the personal marketplace at `~/.agents/plugins/marketplace.json`; a repository or team destination is explicit. The current scaffold emits defaults intended to validate rather than bracketed values that require replacement before structural acceptance. Existing-plugin updates use source-relationship inspection, the cachebuster helper, marketplace-name reading, reinstall, and a fresh task instead of recreating the package or manually rewriting marketplace state.

One current-source conflict is intentionally preserved. The current manifest reference contains an illustrative top-level `hooks` field, while the current workflow instructions say to omit it and the selected validator rejects it. For this local contract:

1. Use the validator result as the acceptance fact.
2. Omit the disputed top-level field from generated manifests.
3. Treat the sample as conflicted explanatory evidence, not as proof of support.
4. Record the exact root and validator hash when the result matters.
5. Route any claim about broader or future support to a refreshed owner rather than generalizing from this one local version.

This resolution does not declare the concept of hooks universally unsupported. It establishes only that copying the illustrated top-level field fails the selected creator's executable contract. The same distinction applies to any future mismatch between a sample and validator.

Use the hierarchy by claim:

| claim_to_make | primary_evidence | required_support | conflict_resolution |
| --- | --- | --- | --- |
| where a new personal plugin is created | selected current skill plus observed scaffold arguments/output | destination and collision inspection | explicit project policy overrides destination, then the chosen root must be recorded |
| which manifest keys this creator accepts | current validator source and safe fixture result | current schema explanation | validator governs local acceptance; preserve and escalate documentation disagreement |
| whether generated metadata is appropriate | requested product facts and generated-diff review | scaffold output and manifest field meaning | human review corrects semantic defects even if validation passes |
| whether an optional component belongs | requested behavior and component owner's contract | package declarations, files, and specialist check | omit companions without concrete behavior and verification |
| whether an existing update targets installed source | marketplace entry, local source path, installed listing, and update guide | prior version/cache identity and preservation record | stop on identity mismatch; do not repair by blind reinstall |
| whether a plugin is installed and active | marketplace resolution, install result, and fresh-task observation | package validation and component behavior | runtime evidence wins over assumptions from source creation |
| whether a shared or remote capability is approved | project policy and accountable owner | local package evidence and security/component review | local creator files cannot supply missing organizational authority |

Good hierarchy use selects the installed root, scaffolds and validates with scripts from that root, reviews metadata semantically, cites the archive only to explain changed defaults, and records the conflict above. Bad use reads the archive skill, runs the current scaffold, validates with another copy, then cites the illustrative manifest as proof that a rejected key is supported. A borderline case discovers that a repository pins a different complete creator version: the operator may use it, but must switch the whole contract and regenerate evidence rather than borrowing one convenient script.

Capture a reproducible source inventory before consequential use:

```text
selected_creator_root:
selection_reason_and_owner:
workflow_source_hash:
schema_reference_hash:
scaffold_script_hash_and_observed_help:
validator_hash_and_fixture_result:
update_helper_hash_if_used:
marketplace_helper_hash_if_used:
project_policy_source:
historical_sources_consulted:
conflicts_and_resolutions:
claims_still_pending_refresh:
```

Re-read and re-hash a source when its file changes, the creator root changes, a repository pins another version, command behavior differs from recorded help, a new component type is introduced, or a disputed field becomes consequential. Re-run behavioral fixtures when scaffold or validator hashes change. Revalidate package bytes after any generated or manual edit. Reprove marketplace and runtime claims after entry, cache identity, install, or task-start changes.

A hash proves only which bytes were inspected. It does not prove those bytes remain authoritative, correct, or suitable for a project. Conversely, an old path does not make every invariant obsolete: archive continuity can support historical explanation, but changed defaults are direct evidence that operational mechanics need current proof.

When discrepancies recur, convert them into maintained contract checks. A scaffold fixture should validate under the paired validator. Manifest examples should be exercised against accepted keys. Update helpers should preserve intended marketplace-to-source identity. Deliberate changes should carry versioned fixtures or migration notes. The hierarchy is successful when a maintainer can see which sources must evolve together and which historical claims may remain stable.

## Theme Specific Artifact

The required artifact is a **Plugin Lifecycle Decision Record (PLDR)**. It is a concise index of the requested outcome, authoritative identity, lifecycle actions, independent evidence, remaining ownership, and recovery. It prevents four different claims from being compressed into "plugin created":

- package source exists and matches the request;
- package structure validates under a named creator contract;
- a marketplace resolves the intended source and installation succeeds;
- a fresh Codex task exposes and exercises the intended capability.

Use a full PLDR when work mutates plugin source, marketplace state, installation, an existing identity, shared state, or an external component. A design-only comparison can use the decision and evidence-boundary fields. A new source-only scaffold can omit runtime details only by marking them `not_observed` with a reason. Do not leave consequential fields blank.

Allowed stage statuses are:

| status_value | meaning | required_detail |
| --- | --- | --- |
| `passed` | the named gate produced current affirmative evidence | evidence source, decisive observation, and freshness anchor |
| `failed` | the gate ran and contradicted acceptance | failure class, preserved diagnostics, affected claims, and next action |
| `blocked` | a known precondition prevents safe execution | blocker, owner, return condition, and preserved state |
| `pending_owner` | the next stage belongs to another accountable party | owner, handoff artifact, acceptance question, and expected response |
| `not_observed` | the stage may matter but was outside access or requested completion | why it was not run and which claim must not be made |
| `not_applicable` | the stage has no role in this request | concrete scope reason rather than convenience |
| `stale` | prior evidence was invalidated by a relevant state change | invalidating event and exact gate to refresh |

Do not use `passed` for a command that returned zero unless its postcondition was also inspected. Do not use `not_applicable` for installation merely because installation was inconvenient; use `not_observed` or `pending_owner` if runtime completion remains part of the desired outcome.

**PLDR Template**

```yaml
plugin_lifecycle_decision_record:
  record_identity:
    record_id: "stable local or issue identifier"
    recorded_at: "timestamp or durable checkpoint"
    operator: "agent or accountable person"
    requested_completion_level: "design | source | exposed | installed | invoked | updated | removed"

  request_contract:
    user_goal: "observable capability and intended audience"
    explicit_exclusions:
      - "components, destinations, publication, credentials, or replacement not requested"
    acceptance_questions:
      - "question whose observed answer closes the request"

  route_decision:
    selected_surface: "plugin | skill | app | mcp | hook | script | repository guidance"
    plugin_fit_reason: "why one installable identity and lifecycle add value"
    rejected_routes:
      - route: "alternative"
        reason: "material tradeoff"
        reversal_trigger: "observation that would reopen it"

  creator_contract:
    selected_root: "absolute or repository-controlled creator root"
    workflow_source_sha256: "hash"
    scaffold_source_sha256: "hash when used"
    validator_source_sha256: "hash when used"
    supporting_reference_sha256: "hash when consequential"
    contract_conflicts:
      - "disagreement, selected behavior, and bounded conclusion"

  destination_and_identity:
    ownership_class: "personal | repository | team | organization | managed"
    authority_source: "request, policy, or named owner"
    source_directory: "intended authoritative source"
    proposed_name: "user-facing proposal"
    normalized_name: "creator-normalized identity"
    collision_result: "none | known-update | known-replacement | blocked-unknown"
    manifest_name: "observed value"
    marketplace_file: "observed path or not_observed reason"
    marketplace_name: "helper-observed value or not_observed reason"
    marketplace_source_target: "resolved source or unresolved reason"
    installed_identity_and_version: "observed listing or not_observed reason"

  component_inventory:
    - component: "skill, app, MCP declaration, hook, script, asset, or interface field"
      requested_behavior: "specific contract"
      package_linkage: "declaration and file relationship"
      owner: "component verifier"
      verification: "result reference"
    omitted_components:
      - "component and reason it is unnecessary"

  lifecycle_mutation:
    path: "new | update | repair | replace | remove | design-only"
    authorized_actions:
      - "bounded mutation"
    generated_diff_summary:
      - "created or changed path and purpose"
    unrelated_state_preserved:
      - "entry, file, ordering, user data, or installation left unchanged"
    sensitive_inputs: "approved reference only; never a credential value"

  gate_ledger:
    - gate: "surface fit"
      status: "passed | failed | blocked | pending_owner | not_observed | not_applicable | stale"
      evidence: "request and decision observation"
      proves: "one bounded claim"
      does_not_prove: "important adjacent claim"
      freshness_anchor: "request revision or policy source"
    - gate: "source identity"
      status: "status value"
      evidence: "source, manifest, entry, and installed-state comparison"
      proves: "identity relationship"
      does_not_prove: "package or runtime behavior"
      freshness_anchor: "paths, entry content, installed version"
    - gate: "package validation"
      status: "status value"
      evidence: "creator root, validator hash, invocation, and decisive result"
      proves: "local structural acceptance"
      does_not_prove: "truthful metadata, installation, or component usefulness"
      freshness_anchor: "package-byte and validator hashes"
    - gate: "component behavior"
      status: "status value"
      evidence: "specialist check, success path, and important failure path"
      proves: "component-scoped behavior"
      does_not_prove: "marketplace or fresh Codex pickup"
      freshness_anchor: "component files and dependencies"
    - gate: "marketplace and installation"
      status: "status value"
      evidence: "entry target, marketplace identity, install result, independent listing"
      proves: "intended source was selected and installed"
      does_not_prove: "fresh task exposure or remote readiness"
      freshness_anchor: "entry, cache identity, and installed version"
    - gate: "fresh invocation"
      status: "status value"
      evidence: "new task visibility plus bounded success and failure/unavailable path"
      proves: "runtime pickup for the tested capability"
      does_not_prove: "all components, users, or future versions"
      freshness_anchor: "installed identity, task startup, and external state"

  recovery_and_handoff:
    prior_known_good_source_or_version: "preserved recovery point or not_applicable reason"
    rollback_or_removal_path: "current policy and CLI path to reconfirm before execution"
    user_owned_files_to_preserve:
      - "path or state class"
    unresolved_risks:
      - "bounded risk and affected claim"
    next_owner: "person, team, or workflow"
    next_acceptance_observation: "specific evidence that closes the pending stage"

  final_claim:
    achieved_state: "precise lifecycle state actually proved"
    prohibited_overclaim: "nearby state not established"
    rereview_triggers:
      - "creator, bytes, entry, install, task, policy, authority, or remote-state change"
```

The template is intentionally stable in field naming, but it is not an instruction to expose secrets or paste raw logs. Paths, normalized names, versions, nonsecret hashes, redacted error classes, and command outcomes are useful. Credential values, access tokens, private payloads, and unbounded environment dumps are not. Refer to an approved secret location or responsible owner without copying its contents.

**Artifact Composition**

| related_artifact | what_the_pldr_records | what_stays_in_the_original_artifact |
| --- | --- | --- |
| generated filesystem diff | changed paths, intent, unexpected additions, and review outcome | full byte-level patch |
| `plugin.json` | manifest identity, version, component declarations, and validator result | complete manifest content |
| creator or validator transcript | exact invocation, exit meaning, decisive redacted diagnostic, and source hash | routine output and sensitive environment detail |
| marketplace entry | marketplace identity, source target, preservation result, and postcondition | full marketplace file and unrelated entries |
| component test report | test owner, success/failure scenario, result, and affected claim | detailed fixtures, traces, and component-specific logs |
| issue or review record | accountable owner, approval status, requested change, and return condition | discussion history and governance workflow |
| fresh-task report | task freshness, visible capability, exercised path, and observed result | unrelated conversation or user data |

The PLDR indexes those artifacts; it does not duplicate them. Stable paths or issue identifiers are preferable to volatile transcript line numbers. If an evidence artifact is removed or changed, mark the dependent gate stale rather than leaving a success claim unsupported.

**Example Outcomes**

**Good personal-plugin record:** The goal is a personal installable skill. The selected installed creator root and hashes are named. Collision inspection finds no match. The component inventory contains one skill and its assets; unrelated apps and MCP declarations are explicitly omitted. Generated differences are reviewed, the current validator passes the exact package bytes, the personal marketplace entry resolves that source, installation is independently listed, and a new task exercises both the expected path and an invalid-input path. Recovery names the source and current removal flow. The final claim is "personal skill plugin installed and observed in a fresh task."

**Bad record:** "Created plugin successfully." There is no normalized identity, source directory, creator root, generated diff, validator version, marketplace source, installed listing, fresh task, or recovery. Even if files exist, none of the lifecycle claims can be reviewed or resumed.

**Bounded team handoff:** Repository-owned source validates and its component tests pass. Marketplace configuration is inaccessible to the operator. The distribution gate is `pending_owner`, names the platform administrator and entry/source assertion to verify, and the invocation gate is `not_observed`. The final claim is "team plugin source validated and ready for marketplace review," not "team plugin installed."

**Blocked collision record:** Normalization produces a name already present in a destination and marketplace, but ownership cannot be established. The identity gate is `blocked`; existing state is inventoried and untouched. The handoff asks the owner to select reuse, known update, intentional recoverable replacement, or a genuinely different identity. Preservation is the successful outcome of this run.

**Review Procedure**

1. Compare the request contract with the final claim and explicit exclusions.
2. Confirm that selected surface and destination authority follow the decision guide.
3. Trace normalized identity across source, manifest, marketplace, installed state, and fresh invocation wherever those stages apply.
4. Check every `passed` status for independent evidence and a current freshness anchor.
5. Check every incomplete status for a reason, affected claim, owner, and return condition.
6. Confirm package and component changes match the inventory and no unrequested companions appeared.
7. Confirm package-byte edits after validation, marketplace edits after resolution, install/cache changes after runtime testing, or policy changes after authorization have marked dependent gates stale.
8. Confirm sensitive values are absent and recovery preserves user-owned and unrelated state.

The record is complete when a reviewer can identify the correct next action, stop condition, and recovery path without rereading every source file. It remains a decision aid, not an oracle: metadata truth, packaging fit, governance, and acceptable risk still require accountable judgment.

Over time, approved nonsecret PLDR fields can form a maintenance corpus. Frequent normalized collisions may improve naming guidance. Repeated validator/sample conflicts may become contract fixtures. Wrong-source installs may improve diagnostics. Persistent platform handoff delays may clarify ownership policy. Aggregate only with defined retention and review; a metric should suggest investigation, not silently rewrite creator defaults.

## Worked Example Set

These examples are decision fixtures, not universal command transcripts. File roots, marketplace names, and CLI syntax must be reconfirmed from the selected creator and current command help. What transfers is the sequence of preconditions, bounded mutation, independent postconditions, and honest final claim.

| case_id | starting_state | decisive_observation | selected_outcome | verdict |
| --- | --- | --- | --- | --- |
| A | direct personal request, unused identity, one skill | one installable lifecycle adds value and all local stages are observable | minimal personal plugin through fresh invocation | good default |
| B | known existing local plugin appears stale after edits | marketplace entry resolves the exact local source being edited | cache-aware in-place update and fresh-task proof | good adaptation |
| C | repository-owned package, managed marketplace | source authority is local but distribution authority belongs to a platform owner | validated team source plus explicit handoff | bounded borderline |
| D | proposed normalized name already exists | owner and authoritative source cannot be established | preserve and block identity mutation | good avoidance |
| E | request needs one reusable skill but no installation lifecycle | plugin packaging adds no requested value | route to standalone skill workflow | good adjacent routing |
| F | agent assumes defaults and optimizes for command completion | identity, component, and task freshness gates are skipped | broad forceful creation followed by unsupported success claim | bad shortcut |

**Case A: good default, new personal skill plugin**

Request: "Make this review workflow an installable personal Codex plugin. It only needs a skill; do not add an app, MCP server, hook, or shared repository files."

Starting state:

- The installed creator root is readable as a coherent skill, references, scaffold, validator, and helpers.
- Personal destination and personal marketplace state are authorized by the direct request.
- The proposed name normalizes to one identity that is absent from the destination, relevant marketplace entries, and installed listing.
- The requested skill can be checked locally and does not require credentials or remote permission.

Decision: adopt the current creator's minimal personal path. Plugin packaging is justified because the user explicitly wants installation and one managed identity. Optional companions are excluded by both the request and minimum-surface rule.

Actions:

1. Record the requested completion level as fresh invocation, with explicit component exclusions.
2. Scaffold into the inspected personal destination without force.
3. Review every generated path. Replace generic metadata with truthful name, description, version, and asset values; confirm package declarations correspond to actual intended files.
4. Implement and check the skill under its specialist contract.
5. Validate the exact package bytes with the validator from the selected creator root.
6. Inspect the personal marketplace entry and confirm that its source target is the new directory while unrelated entries and ordering remain intact.
7. Read the marketplace identity with the current helper, install through current CLI guidance, and independently inspect the installed identity/version.
8. Open a new Codex task, confirm skill visibility, exercise the requested success path, and exercise one invalid-input or unavailable-state path.

Evidence: the PLDR names creator hashes, normalized identity, generated differences, validator result, component check, marketplace source, install result, fresh-task observation, and removal/recovery path. Validation does not substitute for the fresh-task test, and the fresh-task test does not expand the claim to untested components.

Final claim: "The requested personal skill plugin was created from the recorded source, validated under the selected creator contract, installed through the resolved personal marketplace, and observed in a fresh task. No app, MCP server, hook, or shared repository state was added."

Counterfactual: if the user had requested only a reusable skill file and did not need installation or coordinated lifecycle, the correct result would be Case E rather than this package.

**Case B: good adaptation, existing local plugin update**

Request: "I changed my local plugin skill, but Codex still behaves like the old version. Update the installed plugin without recreating it."

Starting state:

- A same-name source directory, manifest, marketplace entry, and installed identity exist.
- The marketplace entry is inspected and resolves to the exact local source the user edited.
- The prior manifest version/cache identity and source state are preserved for recovery.
- There is no request to rename, replace, or republish the plugin.

Decision: adapt to the installed creator's existing-plugin flow. Do not scaffold over the directory and do not rewrite marketplace state simply because runtime pickup is stale.

Actions:

1. Review intended source changes and check the affected component.
2. Revalidate the complete package after the edit.
3. Apply the selected creator's cachebuster update helper to the intended package, then inspect the resulting targeted change.
4. Read the marketplace name rather than guessing it, reinstall the same plugin identity through current guidance, and inspect the installed result.
5. Start a new task and reproduce the changed behavior. The old task remains evidence of stale pickup, not evidence that reinstall failed.

Failure boundary: if the marketplace points elsewhere, stop the update. Inventory both sources and repair identity with the owner; repeated reinstall is not a source-resolution method.

Final claim: "The authoritative local plugin source was updated and revalidated, cache identity was changed through the current helper, the same marketplace identity was reinstalled, and the changed behavior was observed in a new task. The prior source/version is preserved for recovery."

**Case C: bounded borderline, repository source with managed distribution**

Request: "Add this plugin to the team repository and prepare it for our managed marketplace. I cannot grant marketplace administration from this session."

Starting state:

- Repository policy names the destination, reviewers, manifest ownership, component checks, and source-control expectations.
- The requested normalized identity is free or an authorized known lifecycle action exists.
- The operator can create and validate repository source but cannot inspect or mutate the managed marketplace.

Decision: adapt to a repo/team destination and stop at a platform-owner handoff. Personal defaults must not leak into the shared package.

Actions: create the minimum package under repository policy, inspect differences, validate with the selected complete creator root, run component checks, and produce the marketplace entry requirements without asserting they were applied. Preserve the source path, version, review evidence, expected marketplace source, and acceptance question for the administrator.

Gate ledger:

- source ownership: `passed` under repository policy;
- package validation: `passed` for the recorded bytes and validator;
- component behavior: `passed` for locally testable cases;
- marketplace exposure: `pending_owner` with platform administrator and source-target assertion;
- installation and fresh invocation: `not_observed` because their precondition is pending.

Final claim: "The team plugin source is reviewed and valid under the recorded contract and is ready for managed marketplace configuration." Calling it installed would be false. This is borderline only relative to an end-to-end runtime request; it is a high-quality bounded result under the available authority.

**Case D: good avoidance, unknown normalized collision**

Request: "Create a plugin called `Review Helper`."

Starting state: normalization produces an identity already present in a destination or marketplace. The available files do not establish whether it is the requested product, an abandoned experiment, another user's plugin, or the authoritative installed source.

Decision: avoid creation and replacement under that identity. Do not force, silently add a suffix, delete an entry, or install a second package to see which one wins.

Actions: leave existing state untouched; record destination, manifest identity, marketplace source, installed listing, and unresolved owner; present four explicit paths: reuse the existing plugin, update it after authority is proved, intentionally replace it with recovery, or choose a genuinely different product identity.

Final claim: "Creation is blocked by an unresolved normalized-name collision; existing state was preserved and the ownership decision needed to resume is recorded." Preservation is the successful outcome.

**Case E: good adjacent routing, standalone skill**

Request: "Write a local skill that explains our release checklist. I do not need a plugin or marketplace installation."

Starting state: one skill surface satisfies the requested behavior. There is no need for plugin-level manifest identity, coordinated components, marketplace discovery, versioned installation, or plugin removal.

Decision: route to the skill-development workflow. Carry over the capability contract and verification needs, but do not create `plugin.json`, a plugin directory, or marketplace state.

Return condition: reopen this creator reference if the user later requests installable distribution, coordinated components, or a plugin lifecycle. Mentioning Codex or a skill alone is insufficient to select plugin packaging.

Final claim: "The request was routed to the narrower skill surface because plugin lifecycle adds no requested value."

**Case F: bad shortcut, broad forceful creation**

An agent sees "plugin" and immediately creates a package using whichever creator path it remembers. It assumes a personal destination despite a repository context, generates every optional directory, copies an illustrative manifest field rejected by the selected validator, force-writes a same-name destination, guesses a marketplace identity, installs without confirming the entry's source, and tests in the existing task. It reports "plugin created and working" because file creation and an install command returned successfully.

Why each local success signal is insufficient:

- directory creation does not establish requested surface, identity ownership, or valid metadata;
- a broad component tree does not establish behavior or package linkage;
- force completion can destroy the evidence needed to identify the prior plugin;
- validator failure cannot be waived by a documentation sample without resolving the contract;
- install success does not prove that the intended source was selected;
- old-task behavior does not prove fresh plugin pickup;
- no recovery record means the user cannot safely undo or diagnose the result.

The correct stop occurred at the first unresolved authority or collision check. Later commands increased state ambiguity rather than confidence.

**Replay and review**

For a safe local replay, use isolated temporary destinations and marketplace fixtures for scaffold validity, normalization collision, validator acceptance, and unsupported-key behavior. Do not point a documentation fixture at the user's active marketplace or installed plugins. Existing-update identity and fresh-task behavior require real state only when the request authorizes it.

Review each case with these questions:

1. What exact requested outcome justified the selected surface and completion depth?
2. Which observation established destination authority and normalized identity?
3. Did actions mutate only the intended source and lifecycle state?
4. Which independent postcondition proves each final claim?
5. Which nearby claim remains unproved or belongs to another owner?
6. What state is preserved if the decision or implementation is wrong?

Candidate deterministic fixtures include: current scaffold output validates under its paired validator; normalization detects a same-name destination before mutation; a rejected top-level field produces the expected local failure class; component declarations without required companions fail; update helpers change only intended cache identity; and a source-only PLDR cannot mark installation or fresh invocation passed. Governance and packaging-fit decisions remain review cases rather than machine-only verdicts.

## Outcome Metrics and Feedback Loops

Measure whether the reference helps operators reach the **requested lifecycle state with one preserved identity and a recoverable handoff**. Do not optimize for package count, generated file count, or validator pass rate alone. Those are process observations, not evidence that the right extension was built or installed from the intended source.

The original leading indicator remains useful after decomposition: an eligible user should be able to install, invoke, diagnose, and remove the extension without reading implementation code. A source-only or design-only request is not eligible for all four stages and must not be counted as a runtime failure. The original failure signal also remains: confusion between adjacent extension surfaces or omission of recovery is a reference defect even if generated files validate.

Use one PLDR as the unit of observation. Repeated attempts belong to the same record until the requested lifecycle outcome changes materially. Record at least requested completion level, selected surface, creator version/hash, destination class, normalized identity result, component count/type, stage statuses, retry causes, final claim, and recovery status. Aggregate only approved nonsecret fields.

| metric_name | definition_and_denominator | evidence_source | interpretation | balancing_guard |
| --- | --- | --- | --- | --- |
| route decision accuracy | reviewed runs whose selected plugin or adjacent surface matched the requested observable outcome divided by sampled reviewed runs | request contract, route decision, reviewer verdict | detects overpackaging and missed plugin-lifecycle needs | segment ambiguous requests and record rejected alternatives rather than forcing binary certainty |
| identity continuity | applicable runs in which normalized source, manifest, marketplace target, installed identity, and invoked capability form one explained chain divided by runs reaching those stages | destination inventory, manifest, entry, install listing, fresh-task record | detects wrong-source creation, update, or install | do not penalize honest `not_observed` later stages in source-only work |
| minimum-surface conformance | reviewed packages whose components are all requested or causally necessary divided by reviewed created/updated packages | component inventory and generated diff | detects speculative apps, servers, hooks, scripts, or assets | ensure missing required behavior is tracked separately so minimalism does not become underdelivery |
| first structural validation result | packages passing the selected validator before corrective iteration divided by packages first submitted to that validator | validator invocation, hash, and initial result | indicates scaffold/default/documentation alignment | never equate first-pass validation with semantic metadata, component behavior, or runtime success |
| requested-stage completion | runs whose final proved state equals the requested authorized completion level divided by runs with that level and available prerequisites | PLDR gate ledger and final claim | reveals lifecycle drop-off and overclaiming | classify blocked and pending-owner stages separately from operator defects |
| fresh-task pickup | runtime-eligible installations whose intended capability is visible and behaves as boundedly expected in a newly started task divided by installations tested in a new task | installed identity plus fresh-task report | detects stale cache, wrong source, missing package linkage, or pickup failures | include a meaningful failure/unavailable path and avoid generalizing to untested components |
| preservation escape count | runs that overwrite, delete, retarget, or replace unknown, unrelated, or user-owned state without explicit authority | diff, marketplace comparison, incident record, recovery review | safety invariant and immediate investigation trigger | verify the event rather than inferring it from a failed command |
| recovery clarity | failed, blocked, update, replacement, and removal runs whose record names a preserved state, responsible owner, and executable next or rollback condition | PLDR recovery block and reviewer audit | measures resumability and reversibility | a described rollback must be reconfirmed against current policy before use |
| lifecycle retry profile | retries per run grouped by source fit, identity, schema, component, marketplace, install/cache, task freshness, external state, and governance cause | gate ledger transitions | locates repeated friction without treating all retries as equivalent | keep retries within one record and distinguish evidence refresh from blind repetition |
| reviewer decision effort | time or steps needed to identify next action, stop condition, and affected claim from the record | bounded review sample | signals whether evidence is too sparse or too noisy | collect only for comparable reviews and do not claim causality without a baseline |
| post-acceptance escape | a defect discovered after a gate was marked passed, classified by which claim the gate purported to establish | incident or follow-up linked to original record | tests gate meaning and freshness rules | exclude behavior outside the recorded claim rather than inflating the escape rate |

Do not set numerical productivity thresholds merely because a table invites them. Establish a baseline from comparable cohorts before adopting a target. Strict invariants are appropriate where the desired count is structurally clear: unauthorized replacement, secret disclosure in records, and knowingly unsupported final claims should not be accepted. Even then, investigate data quality before drawing causal conclusions.

Segment results by factors that materially change the workflow:

- new creation, update, repair, replacement, or removal;
- personal, repository/team, organization, or managed destination;
- source-only, exposed, installed, or fresh-invocation completion;
- selected creator root and source hashes;
- component type and count;
- local-only versus remote or credential-bearing behavior;
- direct request versus route ambiguity;
- operator-owned versus pending external authority.

Without segmentation, a team package awaiting a platform administrator can look worse than a personal experiment, and an intentionally pinned creator can look like a current regression. Sparse cohorts should be reviewed as individual records rather than summarized with unstable percentages.

**Metrics to reject in isolation**

- High scaffold volume may mean the creator is convenient, or that agents package standalone capabilities unnecessarily.
- Low creation time may mean good defaults, or that collision, ownership, component, and recovery checks were skipped.
- High validator pass rate may mean aligned scaffold output, or that semantic and runtime defects are invisible to validation.
- Low retry count may mean predictable flow, or that failures were abandoned or omitted from records.
- High installation count may mean successful distribution, or repeated wrong-source reinstall attempts.
- Small packages may mean disciplined minimum surface, or missing required behavior.

Pair each process measure with route accuracy, identity continuity, requested-stage completion, preservation, and escape evidence before using it to change the creator.

**Feedback evidence choices**

| feedback_source | best_for | principal_limit | appropriate_use |
| --- | --- | --- | --- |
| scaffold and validator fixtures | deterministic schema, generated-default, collision, and companion regressions | cannot judge user intent, governance, or runtime pickup | run when paired creator files change and before adopting structural changes |
| focused reference verifier | heading, packet, expansion, uniqueness, marker, and evidence-shape invariants | does not prove plugin lifecycle truth | run after every evolved-reference edit and before handoff |
| PLDR sample review | route, identity, completion, recovery, and evidence-quality problems | manual sampling and self-report bias | review recurring workflows and all consequential shared/replacement cases |
| user or maintainer report | friction, surprise, usefulness, and missing guidance | incomplete reproduction and selection bias | classify into a lifecycle stage and request the smallest decisive evidence |
| component tests | skill, app, MCP, hook, script, or asset behavior | component scope does not prove package distribution | attach results to the component ledger and rerun after relevant bytes change |
| fresh-task scenario replay | install/cache/source resolution and runtime pickup | depends on current platform state and can be slower | use for runtime-eligible changes and release-sensitive regressions |
| incident analysis | high-consequence preservation, security, or wrong-source escapes | rare events do not estimate normal frequency | prioritize containment, recovery, root cause, and bounded preventive checks |

Use the following feedback loop:

1. **Observe:** capture a failed or costly stage with creator version, lifecycle path, decisive nonsecret evidence, and affected claim.
2. **Classify:** distinguish route, authority, identity, package schema, component, marketplace, install/cache, fresh-task, external-service, or recovery failure.
3. **Check recurrence and consequence:** one severe preservation or security escape can justify immediate action; ordinary friction needs repeated or clearly reproducible evidence.
4. **Propose the smallest intervention:** candidate locations include preflight, scaffold default, validator rule, manifest example, update helper, diagnostics, repository policy, or worked case.
5. **State counter-risk:** explain what valid workflow the intervention might block, slow, or misclassify.
6. **Build a fixture or bounded pilot:** automate deterministic local behavior; use accountable review for packaging fit, governance, and usability.
7. **Adopt or revert:** compare the targeted metric and balancing guards, document intentional behavior changes, and preserve a rollback path.
8. **Recheck after drift:** refresh when creator hashes, package format, CLI behavior, public API/docs, organizational policy, or component contracts change.

Good feedback: several independently reviewed update records show that operators edit the intended local source but reinstall a marketplace entry that points elsewhere. A proposed preflight prints or verifies the entry-to-source relationship before cache mutation. An isolated fixture covers match and mismatch, the update guide is aligned, wrong-source retries decline in a bounded pilot, and no valid nondefault source path is blocked.

Bad feedback: a dashboard reports many successful scaffold commands, so optional components are generated by default to increase package completeness. No outcome or preservation measure is checked. Validator passes rise while minimum-surface conformance and component ownership degrade.

Borderline feedback: first structural validation failures cluster in a repository that intentionally pins an older complete creator. The observation is real but does not justify changing the installed personal creator. Separate the cohort, verify the repository contract, and decide whether its owner needs a migration or versioned fixture.

Data quality is part of the loop. Define run identity, avoid counting retries as independent tasks, retain failed and blocked records, record known missingness, and freeze the creator version/hash used by each run. Redact credentials and private payloads. Set ownership and retention before aggregating personal paths or marketplace details.

Review cadence is event-driven first: rerun the focused verifier after every generated-reference edit; rerun creator contract fixtures when paired source hashes change; review a record after every high-consequence escape; refresh public evidence when relevant APIs, documentation, or tooling releases change; and choose a periodic trend review only when enough comparable records exist. The goal is reliable requested outcomes and recoverability, not maximum automation or the disappearance of legitimate human decisions.

## Completeness Checklist

Use this checklist after every section-specific gate, before claiming completion, and before handing work to another owner. First choose the applicable profile:

- **Decision profile:** read-only orientation, surface choice, or design. Complete request, route, evidence-boundary, uncertainty, and final-claim items.
- **Source profile:** new or updated package bytes without requested installation. Add creator, identity, component, diff, validation, preservation, and source-handoff items.
- **Runtime profile:** marketplace exposure, installation, or invocation requested. Add source resolution, install postcondition, fresh-task, and runtime-recovery items.
- **Existing-state profile:** update, repair, replacement, or removal. Add prior-authority, preservation, identity relationship, affected-user, and rollback/removal items.
- **Shared or remote profile:** repository/team/organization state or external integration. Add policy, reviewer, platform/security owner, credentials boundary, and external acceptance items.

An item can be complete as `passed`, `blocked`, `pending_owner`, `not_observed`, or `not_applicable` only when its status is accurate and the required reason/evidence is present. A stale result is incomplete until refreshed or removed from the final claim.

**Request and route**

- [ ] The requested observable end state is explicit: design, source, marketplace exposure, installation, fresh invocation, update, repair, replacement, removal, or another named stage.
- [ ] The intended audience and ownership class are explicit: personal, repository, team, organization, or managed platform.
- [ ] Explicit exclusions cover unrequested components, shared publication, credentials, replacement, and destructive effects.
- [ ] The selected surface follows desired outcome rather than a keyword. The record explains why one plugin identity and lifecycle add value, or names the narrower route.
- [ ] Rejected alternatives include the material reason and an observation that would reopen them.
- [ ] The role scenario names user/agent, starting state, decision, trigger, and authorized stop condition.

**Creator contract and source evidence**

- [ ] One complete creator root is selected. Its workflow, references, scaffold, validator, and helpers are not silently mixed with another root.
- [ ] Current source paths and consequential hashes are recorded, or an explicit project-pinned contract is named.
- [ ] Historical archive material is used for lineage rather than current mechanics unless behavior was reconfirmed.
- [ ] Conflicting samples, instructions, and executable behavior are preserved and resolved per claim. Under this selected local contract, the top-level `hooks` illustration is not treated as accepted manifest evidence.
- [ ] External sources that were not refreshed are labeled as discovery pointers rather than current support.
- [ ] A source hash or creator-root change invalidates dependent generated-default, validator, helper, and command assumptions.

**Destination, authority, and identity**

- [ ] The destination path was inspected before mutation and its ownership matches explicit request or policy.
- [ ] Personal placement is used as the installed creator default only when personal state is appropriate; repo/team placement is explicit.
- [ ] The proposed name and creator-normalized name are both recorded.
- [ ] Exact destination folders, manifests, relevant marketplace entries, installed/listed identities, and intended edit source were inspected where available.
- [ ] A normalized collision is classified as absent, authorized known update, recoverable known replacement, or blocked unknown state.
- [ ] Unknown same-name state remains untouched. No silent suffix, force replacement, deletion, or speculative install was used to resolve identity.
- [ ] The authoritative source-to-manifest-to-marketplace-to-install chain is explained for every applicable stage.

**Component minimum surface**

- [ ] Every included skill, app, MCP declaration, hook, script, asset, or interface field maps to requested behavior or a causally necessary package function.
- [ ] Each component has a package linkage, implementation owner, success check, and important failure/unavailable-state check.
- [ ] Apps and MCP declarations correspond to real intended companions or deliberate inline configuration under the selected contract.
- [ ] Unrequested optional companions are omitted and their absence does not break accepted behavior.
- [ ] Credential values, private payloads, and organization permissions are absent from generated content and audit records.
- [ ] Remote or managed behavior is not inferred from local package structure.

**Mutation and generated-diff review**

- [ ] The lifecycle path is explicit: new, update, repair, replace, remove, source-only, or design-only.
- [ ] Only authorized files and state were changed; exact changed paths and purposes are recorded.
- [ ] Generated metadata is truthful and product-specific rather than merely validator-compatible.
- [ ] Unexpected files, declarations, assets, or marketplace changes were removed or justified.
- [ ] Unrelated files, marketplace entries, ordering, installations, and user-owned state were preserved.
- [ ] Any force or replacement action, if explicitly requested, has known authority, prior inventory, recovery, affected-user consideration, and postcondition proof.
- [ ] The generated diff was reread after the final edit, not only after initial scaffold.

**Package and component acceptance**

- [ ] The exact final package bytes were validated with the validator from the recorded creator root.
- [ ] The validation record includes invocation, source hash/version, target, decisive result, and redacted failure details when applicable.
- [ ] Validator success is scoped to local structural acceptance and does not claim metadata truth, component behavior, marketplace configuration, installation, or invocation.
- [ ] Each component-specific check ran against the final relevant bytes and dependency state.
- [ ] A meaningful failure or unavailable-state path was exercised where component risk warrants it.
- [ ] Package or component edits after a pass marked the dependent evidence stale and triggered the necessary rerun.
- [ ] A failed gate is attributed to the correct layer rather than bypassed by changing unrelated state.

**Marketplace and installation acceptance, when applicable**

- [ ] Marketplace mutation was requested and authorized; source-only work did not silently broaden into platform state.
- [ ] The intended entry points to the exact source created or updated, and unrelated entries/order remain unchanged.
- [ ] The personal marketplace is handled through the selected creator's current discovery flow; a nondefault marketplace has explicit configuration or an owner handoff.
- [ ] Marketplace name comes from current state/helper evidence rather than memory or folder-name inference.
- [ ] Installation uses current CLI/help and the resolved identity, with credentials and sensitive output protected.
- [ ] Installed identity/version is queried independently after the mutating action.
- [ ] An install success is not used to waive a source mismatch or package failure.
- [ ] Marketplace entry, cache identity, or install changes invalidate prior runtime evidence.

**Fresh runtime acceptance, when applicable**

- [ ] A new Codex task was started after the final install or reinstall.
- [ ] The intended capability is visible under the expected plugin identity.
- [ ] One bounded requested success path was exercised.
- [ ] One important invalid-input, unavailable-state, permission, or failure path was exercised when relevant.
- [ ] The runtime claim is limited to tested components, environment, version, and external conditions.
- [ ] Same-task behavior is not presented as proof of fresh pickup.
- [ ] A remote integration records local package proof separately from service credentials, permissions, health, and acceptance.

**Existing update, repair, replacement, or removal, when applicable**

- [ ] The marketplace entry was proved to target the exact local source before an update.
- [ ] The prior manifest version/cache identity and recoverable source state were preserved.
- [ ] Existing updates use the selected helper-driven cache identity and reinstall sequence rather than package recreation or blind marketplace rewrite.
- [ ] A source mismatch routes to identity repair before retry.
- [ ] Replacement authority and affected users are explicit; recoverability was proved before destructive mutation.
- [ ] Removal inventories source, entry, installed identity, user-owned files, unrelated marketplace content, and current policy/CLI before execution.
- [ ] Post-removal or post-replacement state is queried independently, and rollback limitations are recorded.

**Handoff, recovery, and final claim**

- [ ] The PLDR names creator root/version, source path, normalized identity, manifest version, components, validator, marketplace source, installation, runtime, and recovery to the requested level.
- [ ] Every `blocked`, `pending_owner`, or `not_observed` stage names the affected claim, responsible owner, preserved evidence, and observation that closes it.
- [ ] Every `not_applicable` stage has a scope reason.
- [ ] The last known-good or prechange state is identifiable for updates, replacement, removal, and high-risk failures.
- [ ] Recovery or removal guidance is labeled for reconfirmation against current policy before use.
- [ ] The achieved-state sentence says exactly what is proved.
- [ ] A prohibited-overclaim sentence names the nearest state not established.
- [ ] Rereview triggers include relevant creator, package-byte, marketplace, install/cache, task, policy, authority, component, and remote-state changes.
- [ ] The next action is executable by its named owner without rediscovering the source relationship.

**Reference quality and evolution integrity**

- [ ] All 26 original reference headings remain exact and ordered.
- [ ] Every evolved section is strictly more detailed than its matching archive seed while avoiding unsupported precision and repeated filler.
- [ ] The decision guide retains Adopt when, Adapt when, Avoid when, and Cost of being wrong with plugin-specific conditions and recovery.
- [ ] The local corpus hierarchy identifies current executable, current supporting, historical, conflicted, generated, and unrefreshed evidence roles.
- [ ] The PLDR can be reviewed without reading every mapped source, while still linking decisive evidence.
- [ ] Worked cases cover good default, good adaptation, bad shortcut, bounded borderline, collision preservation, and adjacent routing.
- [ ] Outcome metrics retain the user lifecycle leading indicator and extension-confusion/recovery failure signal with applicability boundaries.
- [ ] Adjacent routing names the receiving workflow, handoff payload, and return condition.
- [ ] The focused evolution verifier passes exact packet counts, exact question texts, mandatory-field uniqueness, normalized uniqueness, heading preservation, expansion, and content hygiene.
- [ ] Packet and reference were reread completely with durable review checkpoints at the required cadence.

Classify the final audit:

- **Complete:** every applicable claim has current evidence; nonapplicable stages are justified; final state equals the requested authorized outcome.
- **Complete bounded handoff:** local applicable stages pass and inaccessible later stages have owners, preserved evidence, and return conditions; the final claim stops at the proved boundary.
- **Safely blocked:** continuing would violate identity, authority, security, or recovery; existing state is preserved and resumption evidence is explicit.
- **Incomplete:** an applicable gate lacks evidence, has become stale, or the final claim exceeds observed state.
- **Invalid completion:** state was overwritten or exposed without authority, identities diverge, sensitive data leaked, or unsupported success was claimed; contain and recover before further feature work.

As a final adversarial pass, ask: "What if this source is not the installed source?", "What changed after the last green result?", "Which optional surface was added without a contract?", "Who can actually perform the pending stage?", and "What would a reviewer restore if this decision is wrong?" A checklist that cannot answer those questions is not complete even when every box is marked.

Maintain the audit itself. Promote recurrent or high-consequence omissions into preflight or fixtures. Remove items when stronger evidence fully subsumes them and no distinct failure class remains. Every item needs a claim, owner, and reason to exist; length alone does not create reliability.

## Adjacent Reference Routing

This reference owns the decision to use a plugin and the coherence of its lifecycle: destination, normalized identity, source, manifest, component inventory, marketplace relationship, installed state, fresh pickup, and recovery. Route adjacent work when another workflow has distinct component expertise, mutation authority, or acceptance evidence. Do not route merely because another reference shares a keyword.

The default ownership split is:

- **Plugin lifecycle owner retains:** requested completion, package fit, creator contract, destination authority, normalized identity, generated-diff scope, manifest/component linkage, cross-stage validation, marketplace-to-source assertion, final claim, and recovery record.
- **Component or platform specialist receives:** one bounded behavior or authority domain, the files/state it may change, its success and failure contract, sensitive-data restrictions, and required return evidence.
- **Lifecycle owner reconciles:** returned bytes or approvals, package revalidation, invalidated gates, distribution/runtime evidence, explicit pending stages, and the final PLDR.

| route_trigger | receiving_workflow_or_owner | handoff_payload | receiving_acceptance | lifecycle_return_condition | prohibited_assumption |
| --- | --- | --- | --- | --- | --- |
| one reusable skill is sufficient and plugin installation adds no requested value | skill-development or skill-creator workflow | user capability, audience, examples, exclusions, and skill verification need | valid useful skill under its current contract | return only if installable plugin distribution or coordinated components become concrete | the word "Codex" or "skill" automatically requires a plugin |
| plugin remains selected and a skill component needs implementation or repair | skill specialist | plugin identity, component path, requested behavior, package linkage, allowed files, success/failure cases | final skill bytes and component-scoped evidence | lifecycle owner integrates, revalidates package, and refreshes runtime gates if installed | component success proves package installation or fresh pickup |
| app component is required | current app/component workflow or accountable app owner | plugin identity, intended UI/service contract, declaration shape from selected creator, data/security boundaries, owned files | app behavior and package linkage evidence under current component contract | return bytes/configuration and affected claims for package revalidation and runtime test | a directory name or manifest key proves the app exists or is usable |
| MCP capability or server declaration is required | `mcp-integration` workflow and service owner | tool/resource behavior, transport/configuration boundary, plugin linkage, credential policy, target environment, failure semantics | local configuration/package evidence plus separately scoped service and permission evidence | lifecycle owner reconciles declaration, validates package, installs, and tests fresh availability when authorized | valid JSON proves remote service readiness, credentials, or authorization |
| hook or event behavior is required | current hook/event workflow and policy owner | event contract, allowed effects, execution boundary, failure/reentrancy expectations, selected creator acceptance | behavior and safety evidence for the supported hook representation | return only supported package changes and identify any platform policy gate | the conflicted top-level `hooks` illustration is accepted by this local validator |
| a manifest field or package structure is disputed | selected creator's schema reference plus executable validator owner | exact package bytes, creator root/hash, disputed key, expected meaning, minimal fixture | reproducible acceptance/rejection and bounded interpretation | update package and documentation/fixture ownership, then revalidate final bytes | an illustration outranks paired validator behavior or validator success proves semantics |
| repository/team destination is requested | repository policy, maintainers, and review workflow | request, normalized identity, paths, component inventory, intended marketplace, generated diff, recovery plan | source ownership, review, test, and publication requirements satisfied | lifecycle record receives approval and any source changes before distribution gates continue | personal destination or personal marketplace defaults apply to shared state |
| organization or managed marketplace exposure is required | marketplace/platform administrator | validated source identity/version, intended entry/source assertion, ownership, review evidence, install audience, rollback expectation | configured entry and independently observed source resolution under platform policy | return marketplace identity, source target, action result, limitations, and next runtime gate | local source validity grants platform mutation authority |
| credentials, privileged permissions, external data, or security-sensitive effects are required | security owner and integration owner | threat-relevant behavior, minimum permissions, secret references without values, data paths, failure/revocation expectations | approved boundary and testable acceptance conditions | return approval scope, conditions, owner, and evidence reference; keep secrets out of PLDR | package validation or local invocation proves security approval |
| existing plugin edits are not visible | plugin update/source-resolution workflow in this reference using current install guidance | intended local source, manifest identity, marketplace entry, installed version/cache identity, observed stale behavior | source relationship proved, package revalidated, cache identity updated, same identity reinstalled | fresh task demonstrates intended change and recovery data remains available | repeated reinstall identifies or repairs the authoritative source |
| same-name source, entry, or installation has unknown ownership | identity and repository/user-owner resolution | complete nonsecret inventory, normalized collision, intended capability, preserved state, candidate choices | explicit reuse, update, recoverable replacement, or different-identity decision | resume the selected lifecycle path only after authority and source are known | force, deletion, or silent suffixing is harmless |
| plugin removal or replacement is requested | current platform/CLI policy plus affected owner | source, entry, installation, user-owned files, affected audience, prior known-good state, desired postcondition | authorized action, preservation, independent postcondition, and recoverability | final PLDR records removed/replaced state and residual risk | source deletion alone removes marketplace and installed state |
| request is only conceptual explanation or reference review | documentation/explanation workflow | exact question, evidence boundary, desired depth, no-mutation constraint | accurate bounded explanation or review findings | no plugin mutation unless a later direct request establishes scope | opening this creator reference authorizes scaffold or installation |

**Routing modes**

Choose the least distributed mode that supplies the needed authority and evidence:

1. **In-workflow execution:** one operator owns package and a simple local component. Best for a bounded personal plugin when the same current contract covers both and no external authority is needed.
2. **Sequential specialist handoff:** lifecycle owner freezes identity and component contract; specialist returns final bytes/evidence; lifecycle owner integrates and refreshes dependent gates. Best when one component needs distinct expertise.
3. **Parallel isolated review:** specialists inspect separate concerns without writes, then one owner reconciles conclusions before mutation. Best for security, manifest, and component design analysis that can proceed independently.
4. **Source-only platform handoff:** local owner completes and validates package source; marketplace/security administrator performs a later governed stage. Best when authority rather than technical package work is the boundary.
5. **Full stage transfer:** a managed platform owner owns marketplace and installation end to end. The lifecycle record still supplies expected identity and receives returned evidence; it does not pretend the original operator observed the stage.

Parallel writes to the same plugin, manifest, marketplace, or PLDR are not a routing mode. Assign one writer per artifact and one lifecycle reconciler. If a specialist must edit package-owned files, the handoff must enumerate those paths; all dependent package evidence becomes stale until integration review and revalidation.

**Minimum handoff envelope**

```yaml
handoff:
  requested_outcome: "observable state and audience"
  requested_completion_level: "source, installed, invoked, or other named stage"
  plugin_fit_and_selected_surface: "decision and reason"
  normalized_plugin_identity: "one shared identity"
  authoritative_source_path: "current intended source"
  creator_root_and_hashes: "selected contract evidence"
  destination_authority: "personal, repository, team, organization, or managed"
  component_or_stage_owned_here: "bounded responsibility"
  allowed_mutations: ["exact files or external state"]
  explicit_exclusions: ["state and components not authorized"]
  package_linkage_contract: "manifest/file relationship"
  success_and_failure_acceptance: ["observable cases"]
  sensitive_data_boundary: "references only; no credential values"
  current_gate_statuses: ["passed, blocked, pending, unobserved, or stale"]
  evidence_to_return: ["bytes, result, approval, source target, or postcondition"]
  return_owner_and_condition: "who reconciles and when"
```

For a read-only question, a shorter envelope can contain request, selected surface, identity if relevant, evidence boundary, and no-mutation constraint. Any mutation, external effect, or completion acceptance requires the applicable full fields.

The receiving workflow returns:

- exact changed paths or external state actions;
- component/platform result and its bounded claim;
- important failure or unavailable-state result;
- source/version/configuration anchors needed for freshness;
- assumptions, unresolved risks, and sensitive-data handling;
- which package, distribution, runtime, or recovery gates became stale;
- next owner if acceptance remains pending.

**Examples**

Good component routing: a plugin needs an MCP tool. The lifecycle owner freezes normalized identity, source, selected creator, declaration boundary, and allowed files. The MCP specialist implements/configures the component, proves local protocol behavior and separately reports remote permission status. The lifecycle owner integrates the declared component, runs the paired validator, verifies marketplace/source identity, installs when authorized, and tests tool availability in a fresh task. Neither owner claims more than its evidence.

Bad parallel routing: two agents independently scaffold the same proposed plugin into personal and repository destinations, normalize names differently, and each edits a marketplace. A later merge combines one manifest with the other's component. Both validator runs are obsolete and neither installed identity is authoritative. The preventable defect is ownership, not JSON syntax.

Bounded platform handoff: team source validates, but only an administrator can configure the marketplace. The outbound record names source/version and required entry target. The administrator returns configured marketplace identity and independent resolution evidence. Installation can then proceed, or remain `pending_owner` if another stage owns it. The original source work was complete before platform completion.

Safe security route: a plugin declaration references a remote service requiring credentials. Local package and error-path checks pass, but credentials are neither generated nor recorded. A security owner approves minimum permissions and revocation conditions; the integration owner proves service behavior in its environment. Fresh Codex pickup is tested only after those gates are satisfied.

**Handoff verification**

1. Compare the outbound request, identity, exclusions, allowed paths, and acceptance cases with the returned record.
2. Reject or explicitly approve changes outside delegated ownership.
3. Recompute package/component evidence invalidated by returned bytes or configuration.
4. Confirm specialists used the selected creator contract or explain a deliberate version boundary.
5. Inspect platform postconditions independently; an approval or successful action is not the same as source resolution.
6. Reconcile duplicate or missing responsibility before installation.
7. Update the final PLDR so each stage has one owner and one bounded evidence source.

Stable responsibilities are locally clear: the selected creator owns current package mechanics, skill and MCP workflows own their component contracts, repository policy owns shared source, and accountable platform/security owners govern external effects. Exact organization titles, app/hook interfaces, public CLI behavior, and managed-service procedures remain environment-specific. Unknown ownership blocks the stage; it does not authorize the plugin creator to absorb it.

Review recurring routes as interfaces. Circular handoffs suggest an undefined owner. Duplicate package edits suggest a missing single-writer rule. Repeatedly lost normalized identity suggests the envelope should become tooling. Standardize high-frequency or high-consequence paths with fixtures and owners; leave rare read-only consultations lightweight.

## Workload Model

`combined_evidence_inference_note`: Treat Codex Plugin Creator Patterns as an agent workflow operating reference, not as a prose summary. Workload is the number of independent identities, authorities, component contracts, state transitions, external effects, and evidence lifetimes the operator must reconcile. Raw file count is secondary.

An earlier bounded-capacity model proposed one primary task, up to ten source files, up to three delegated subtasks, and a written audit. This reference retains the useful intent, bounded work and durable audit, but does not present those counts as universal limits. No local evidence here establishes that ten files or three delegates is a reliability threshold across models, repositories, plugin types, or platform tooling. Teams may adopt numeric alarms after measuring comparable runs and naming an owner.

**Nonnegotiable workload invariants**

1. One lifecycle owner reconciles requested outcome, normalized identity, stage statuses, and final claim for each plugin.
2. One authoritative source relationship is active at a time. Competing candidate sources are diagnostic inputs, not simultaneous package authorities.
3. One writer owns each mutable artifact or external state surface at a time unless transactional isolation, conflict detection, and recovery are independently proved.
4. State-changing stages run against a current baseline and produce an independently inspected postcondition before the next dependent mutation.
5. Package, marketplace, install/cache, task, policy, component, and remote evidence is invalidated only by changes in its dependencies, then refreshed before reuse.
6. Every split or delegation names outbound scope, allowed writes, return evidence, and one reconciler.
7. Every durable stop records current authoritative state, passed/failed/stale gates, blocker, next action, and recovery.

**Workload dimensions**

| workload_dimension_name | low_pressure_state | rising_pressure_signal | split_or_control_response | verification_pressure_point |
| --- | --- | --- | --- | --- |
| plugin identity | one unused normalized identity with a clear destination | same name appears across sources, entries, or installations; rename/replacement is discussed | stop mutation, inventory identity graph, assign owner decision | reviewer can identify one authoritative source and intended installed identity |
| ownership and authority | personal state directly requested | repository, team, organization, managed marketplace, security, or affected users enter | split by accountable authority with expected returned evidence | each mutation has a real owner and no stage infers permission from file access |
| lifecycle depth | design or source-only package | marketplace, install, fresh pickup, update, replacement, or removal stages accumulate | checkpoint after each transition and keep later stages pending until prerequisites pass | final claim stops at the deepest current observed stage |
| component contracts | one local component with a clear test | several skills/apps/MCP/hooks/scripts/assets or remote dependencies need distinct acceptance | delegate component internals, retain package linkage and lifecycle reconciliation | each component has owner, linkage, success/failure evidence, and freshness anchor |
| creator/evidence sources | one complete selected root with coherent scripts | multiple installed, archived, pinned, or conflicting roots contribute | choose a target contract; isolate migration comparison; freeze hashes | scaffold, validator, references, and helpers used for acceptance are reproducible |
| external effects | isolated source files | marketplace mutation, installation, remote calls, credentials, shared publication, or user data | serialize effects, establish rollback and platform/security owner | mutating action and independent postcondition identify the intended target |
| mutable-state contention | one writer and inspected baseline | agents or processes may edit the same package, manifest, marketplace, or journal | lock or sequence ownership; reconcile before further mutation | no accepted evidence was computed against a baseline another writer changed |
| context and evidence volume | concise decisive outputs linked from PLDR | raw logs, many sources, and repeated full reads obscure current state | summarize durable decisions; keep detailed artifacts by reference; reread changed dependencies | independent reviewer reconstructs status without relying on hidden conversation memory |
| retries and uncertainty | one classified failure with a new corrective observation | repeated actions occur without changed evidence or failure classification | apply backpressure, return to the failed gate, narrow the claim or escalate | each retry states what changed and why the next result could differ |
| reversibility | source-only change or known prior state | force, replacement, removal, migration, broad publication, or unknown user files | require preservation, affected-owner review, rollback proof, and smaller steps | recovery does not depend on evidence destroyed by the mutation |
| batch breadth | one plugin lifecycle | many independent plugins, versions, or destinations are processed together | batch deterministic discovery/validation, retain per-plugin identity/result/recovery records | aggregate success can be decomposed to exact failing package and state |

**Workload profiles**

| profile | typical_state | execution_shape | required_checkpoint |
| --- | --- | --- | --- |
| W0 read-only decision | explanation, route choice, source comparison, or review with no mutation | one bounded analysis; specialist reads may be parallel | selected route, evidence boundary, uncertainty, no-mutation confirmation, next condition |
| W1 personal local creation | unused personal identity, minimum local component set, local validation and optional install | one lifecycle owner; serial create-review-validate-expose-install-test spine | after source validation and again after any requested runtime completion |
| W2 existing-state change | update, repair, replacement, or removal of known local plugin | identity resolution first; preserve baseline; serialize mutation and independent postconditions | before first change, after package acceptance, after platform mutation, and after fresh/runtime postcondition |
| W3 shared or external capability | repository/team source, managed marketplace, credentials, remote service, security or platform owner | split by component/authority; one package writer and lifecycle reconciler | at every owner handoff and after returned bytes or approval changes gate status |
| W4 independent plugin batch | repeated discovery, scaffold audit, validation, or migration over several plugin identities | batch read-only/mechanical steps; isolate results and state changes per plugin | per-plugin result plus batch summary; stop affected identity without hiding unaffected outcomes |

These profiles are not severity labels. A W1 package can be dangerous if collision or force appears. A W3 source can be straightforward when policy and owners are already clear. Reclassify when observed state changes.

**Serial mutation spine**

```text
request and authority
  -> surface and completion decision
  -> creator contract selection
  -> destination and identity inventory
  -> component contracts
  -> source mutation
  -> generated-diff review
  -> package and component validation
  -> marketplace source mutation and postcondition, when requested
  -> install/cache mutation and independent listing, when requested
  -> fresh-task behavior, when requested
  -> recovery and final claim
```

Read-only analysis can branch from a stable point. For example, a skill specialist and security reviewer can inspect separate contracts while the lifecycle owner holds source mutation. Their conclusions must reconcile before the package changes. Validator fixtures can run in isolated temporary directories while marketplace inventory remains read-only. Do not parallelize writes to the same source tree or marketplace merely because tools make it convenient.

**Split triggers**

Pause and split or hand off when any of these is true:

- no operator can name the authoritative creator root or plugin source;
- normalized identity has unresolved ownership or several plausible installed sources;
- a component needs credentials, permissions, data access, or a specialist acceptance contract absent from the current workflow;
- a repository, team, marketplace, or security owner controls the next stage;
- more than one writer would touch the same package, manifest, entry, or lifecycle record;
- current context cannot state which evidence remains valid after recent changes;
- repeated retries do not introduce a new observation, corrected precondition, or narrowed claim;
- raw source/log volume prevents a reviewer from locating decisive evidence;
- replacement/removal could destroy the only recovery or source-identity evidence;
- batch output cannot map each result to a unique plugin and recovery state.

Do not split solely because many files exist. Do not keep work monolithic solely because one agent can access every file. The useful boundary is an independently owned contract or state surface with a clear return artifact.

**Checkpoint contract**

After each meaningful state transition, save:

```yaml
workload_checkpoint:
  plugin_identity: "normalized name and destination class"
  authoritative_source: "current source path or unresolved candidates"
  selected_creator_contract: "root and consequential hashes"
  requested_completion: "named lifecycle state"
  current_profile: "W0, W1, W2, W3, or W4"
  completed_stages: ["stage plus decisive evidence"]
  failed_or_blocked_stages: ["classification, owner, return condition"]
  stale_evidence: ["claim, invalidating event, refresh gate"]
  active_writers_and_owned_artifacts: ["owner and exact path/state"]
  pending_handoffs: ["receiver, scope, expected return"]
  retries_and_new_observation: ["cause and changed precondition"]
  preserved_recovery_state: "last known-good or nonapplicable reason"
  immediate_next_action: "one executable bounded step"
  stop_condition: "observation that prevents further mutation"
```

This is a context-capacity control. If the checkpoint cannot be written accurately, the workflow is already too ambiguous to continue mutating state.

**Budgeting and calibration**

Optional local alarms may cover source files loaded, tool calls, wall time, retries, delegated owners, active components, or unresolved gates. Define each alarm with:

- the cohort and lifecycle profile it applies to;
- the failure it is expected to predict;
- the action taken when crossed;
- a balancing measure, such as completion or preservation;
- an owner and review date;
- evidence that the number remains useful.

Crossing an alarm should trigger checkpoint and review, not automatic failure or arbitrary task splitting. A hard limit is justified only when a platform constraint or tested safety property requires it.

**Examples**

Good W1 workload: one operator selects the current creator, confirms an unused personal identity, creates one skill component, saves source and validator evidence, configures the intended personal entry, installs, and tests a fresh task. Read operations are broad enough to prove state, but writes follow the serial spine.

Bad distributed workload: several agents search and then write the same plugin and marketplace in parallel. Each uses a different baseline, and aggregate logs show several successful commands. No result identifies the authoritative source or which validation survived the final write. Parallelism increased stale evidence and recovery cost.

Bounded W3 workload: repository maintainers own source, an MCP specialist owns protocol behavior, security owns credentials/permissions, and a platform administrator owns marketplace exposure. One lifecycle record supplies identity and acceptance contracts; each owner returns evidence; one reconciler revalidates package and final claim. The handoffs add time but reduce unauthorized effects and unsupported claims.

Safe W4 batch: a script reads and validates several independent source trees without mutating active marketplaces. Results retain plugin identity, source, creator hash, pass/fail reason, and next action per package. A failed package stops only its own migration. Any later update is scheduled as an isolated W2 lifecycle.

**Workload verification and feedback**

For a specific capacity question, record active plugin identities, owners, writers, component contracts, sources loaded, tool calls, retry classifications, wall time, handoffs, pending/stale gates, and final outcome. Do not collect all fields by default when they do not answer a decision. Review whether an independent person can reconstruct authoritative state, next action, and recovery from the checkpoint.

Single-writer ownership, identity isolation, durable checkpoints, and classified retries are strongly grounded controls. Optimal numerical source, time, tool-call, or delegation budgets remain environment- and model-dependent. Transactional tooling may permit different concurrency if it proves equivalent isolation, conflict detection, atomicity, and rollback.

Use bottlenecks to improve the creator carefully. Repeated identity ambiguity may justify preflight diagnostics. Repeated validator drift may justify paired contract fixtures. Platform handoff friction may justify policy templates. Fresh-pickup delays may justify update diagnostics. Automate deterministic stages only after preserving stop conditions, per-plugin evidence, and human authority decisions. Sustainable capacity comes from reducing state that must be remembered, not simply executing more actions at once.

## Reliability Target

The reliability target is bounded to what this reference controls: route quality, source/evidence boundaries, package-lifecycle identity, claim scope, and recoverable handoff. It does not promise component uptime, remote service availability, marketplace availability, organization approval time, or future Codex compatibility. Those claims require their own owners and evidence.

Strict values below are acceptance policies for reviewed outputs, not proof that latent defects are impossible. The sampled routing target is a finite regression gate, not an estimate of population reliability.

| reliability_target_name | target_class | measurable_threshold_value | applicability_and_formula | evidence_collection_method | response_to_miss | interpretation_limit |
| --- | --- | --- | --- | --- | --- | --- |
| source_boundary_preservation | per-output acceptance invariant | 100 percent of recommendations keep local, external, and combined-inference boundaries visible | applicable to every factual or prescriptive recommendation whose source class affects confidence; compliant recommendations divided by reviewed recommendations | map each claim to current local source, historical source, unrefreshed external pointer, or explicit synthesis; freeze consequential source hashes | block reuse, correct labels/claim scope, and add a verifier or review fixture when the escape is reproducible | correct labeling does not make a source correct, current, or authoritative for another environment |
| decision_accuracy_sample | bounded sampled evaluation | at least 18 of 20 sampled uses route to an acceptable Adopt, Adapt, Avoid, or adjacent-reference outcome | twenty frozen, stratified cases with explicit constraints; cases judged acceptable divided by twenty | record model/operator output, PLDR route, rejected alternatives, reviewer rubric, verdict, disagreement, and evidence anchors | inspect every miss, classify route/evidence/rubric defect, repair minimally, and rerun the frozen set plus relevant countercases | the result describes this case set and execution conditions; it is not a production probability or universal threshold |
| unsupported_claim_rate | per-output acceptance invariant | zero unsupported production, security, latency, or reliability claims in final guidance | unsupported consequential claims divided by reviewed consequential claims; any observed unsupported claim fails acceptance | require a direct source row, bounded local observation, explicit inference with verification method, or removal/qualification | remove or narrow claim, identify why review missed it, refresh evidence if authorized, and add a regression case for high-consequence escapes | zero accepted observations does not establish that no latent unsupported claim exists |
| recovery_path_clarity | per-case acceptance invariant with reviewer judgment | every Avoid, failed, blocked, update, repair, replacement, removal, or pending-owner case names recovery, escalation, or adjacent route | applicable cases with preserved state, owner, next observation, and affected claim divided by all applicable reviewed cases | inspect failure-mode, routing, PLDR recovery, and final-claim sections together; perform bounded recovery drill for high-risk changes | block destructive continuation or completion claim until recovery/handoff is executable and owned | a written recovery path must be reconfirmed against current CLI, policy, and state before execution |

Add three safety invariants to plugin work even though the seed table did not name them separately:

- unknown same-name source, marketplace, installation, or user-owned state is not overwritten, deleted, retargeted, or silently forked;
- credentials and sensitive values are not generated into source, copied into evidence, or exposed through raw transcripts;
- a final claim never promotes valid source to installed state, install result to fresh pickup, or local package proof to remote/security acceptance without the missing evidence.

These are reviewed acceptance rules. Any confirmed escape is investigated individually; it is not averaged away by a high route score.

**Reliability evidence stack**

1. **Mechanical reference gates:** exact 26 headings and order, every section longer than seed, 26 packet sections, 260 exact question headings, 1,560 populated field lines, exact and prefix-stripped uniqueness, ASCII/hygiene checks, valid Markdown tables/fences, and clean forbidden-marker scan.
2. **Creator contract fixtures:** paired scaffold output validates, normalized collision preserves existing state, unsupported manifest keys receive the expected local rejection, required companion relationships are checked, and cache update behavior is scoped to intended identity.
3. **Decision scenario suite:** diverse frozen requests exercise plugin fit, personal creation, standalone routing, existing update, collision, team source, managed platform handoff, remote/security boundary, replacement/removal, and stale evidence.
4. **PLDR audit:** sampled real or simulated records prove request-to-final-claim alignment, identity continuity, current evidence, explicit noncompletion, and recovery.
5. **Fresh-task replay:** runtime-eligible changes prove installation source and visible behavior after a new task begins.
6. **Escape monitoring:** later wrong-source, unsupported-claim, preservation, component, or recovery failures are linked back to the original gate and evidence lifetime.

No layer substitutes for another. Structural tests can prove packet shape without proving plugin guidance. A validator can prove local package acceptance without proving route or runtime. A successful fresh invocation cannot justify a security or reliability claim beyond the observed case.

**Twenty-case routing protocol**

The decision sample must be frozen before evaluation and cover materially different forks rather than twenty paraphrases of personal creation. Include direct and ambiguous plugin requests; standalone component fit; unused and colliding identities; personal and repository/team destinations; new and existing lifecycles; source-only and runtime completion; managed marketplace authority; remote or credential-bearing components; and recovery-sensitive replacement/removal. The exact mix is an owned evaluation design and must be recorded.

For each case, specify:

```yaml
routing_case:
  case_id: "stable identifier"
  user_request_and_starting_state: "all facts available to the operator"
  intended_observable_outcome: "requested completion"
  authority_and_exclusions: "allowed and prohibited effects"
  acceptable_route_set:
    - "one or more defensible Adopt, Adapt, Avoid, or adjacent outcomes"
  required_safety_invariants:
    - "identity, sensitive-data, preservation, and claim-scope constraints"
  decisive_evidence_expected: "what a strong answer must inspect or ask"
  unacceptable_outcomes:
    - "specific overreach, omission, or unsafe mutation"
  reviewer_rubric: "criteria independent of stylistic preference"
```

Run the reference under recorded conditions. Reviewers score correctness of requested outcome, surface, authority, identity handling, lifecycle depth, evidence boundary, stop/handoff, and recovery. A case can allow more than one design if each satisfies the constraints. Reviewer disagreement is preserved and adjudicated; uncertainty is not forced into a confident route merely to improve the score.

At least 18 of the 20 frozen cases must be acceptable under the rubric for this local evaluation gate. Every miss still requires analysis, including the two misses the threshold permits. A severe authorization, identity-destruction, sensitive-data, or unsupported-success miss blocks release regardless of aggregate score. After a targeted fix, rerun all frozen cases so improvement on one route does not regress another.

**Target examples**

Good source-boundary result: guidance says the installed validator currently rejects the illustrated top-level `hooks` key, cites the selected local contract and hash, limits the conclusion to that contract, and routes broader support to refresh. It does not convert a local observation into a universal platform statement.

Bad unsupported-claim result: a validator pass is described as proving the plugin is secure, reliable, and production-ready. No component, threat, runtime, or operational evidence exists. The unsupported-claim target fails even if every structural field is valid.

Good routing result: an ambiguous "make this a plugin" request is resolved by asking only whether installation/coordinated lifecycle is desired because that answer changes files and effects. A direct personal skill-plugin request proceeds without an unnecessary menu after destination and collision inspection.

Borderline routing result: two packaging choices both satisfy a team request. One reviewer prefers a plugin; another prefers a standalone skill distributed by repository policy. If both honor the stated distribution, identity, and authority constraints, the rubric may accept both or identify a missing premise. Reliability does not require stylistic unanimity.

Good recovery result: a marketplace-to-source mismatch blocks update. The record preserves both candidate paths, prior installed identity, owner, and observation needed to select authority. Bad recovery says "reinstall or delete and retry" without identifying source or preserving state.

**Measurement integrity**

- Predefine inclusion and exclusions; do not remove difficult, failed, or blocked cases after seeing results.
- Stratify by lifecycle and authority so easy personal cases do not mask shared or update errors.
- Freeze source hashes, package bytes, creator version, scenario facts, and rubric for each evaluation run.
- Keep test cases separate from tuning examples where practical, and record when a case influenced a change.
- Store reviewer disagreements and rationale; do not resolve them by score alone.
- Report severe failures individually rather than averaging impact.
- Preserve prior results when a metric definition changes, and label results noncomparable where necessary.
- Redact credentials and private data; synthetic cases should carry no active secrets or marketplaces.

**Failure attribution and intervention**

| missed_target | likely_owner_or_artifact | candidate_intervention | required_countercheck |
| --- | --- | --- | --- |
| source boundary omitted | reference prose, source map, focused verifier, reviewer rubric | explicit claim labels, hash/freshness field, boundary fixture | guidance remains readable and does not label obvious local facts redundantly |
| route decision wrong | decision guide, trigger description, worked cases | add decisive premise, counterexample, or adjacent return condition | direct requests remain low-friction and valid alternative designs stay allowed |
| unsupported consequential claim | evidence review, metrics/reliability prose, example | remove/narrow claim, require source or verification method | useful bounded observations are not suppressed merely because universal proof is unavailable |
| recovery unclear | PLDR, checklist, failure/routing sections, tool diagnostics | add prior-state capture, owner, rollback/removal preflight, or handoff template | recovery instructions remain current, authorized, and do not become unsafe copy-paste recipes |
| identity escape | scaffold/update preflight, marketplace diagnostics, workload ownership | collision/source resolution check and single-writer guard | legitimate known updates and nondefault destinations remain possible |
| stale evidence escape | checkpoint, invalidation rules, verifier | tie result to bytes/tool/version/task anchor and refresh dependent gate | read-only changes do not trigger unnecessary full reruns |

The local target set is known and reproducible once its sources, cases, rubric, and evidence are frozen. Route correctness, metadata truth, recovery usability, and organization fit retain judgment. Component and platform SLOs remain out of scope unless supplied and verified by their owners.

Review the target definitions when real outcomes diverge from the behavior they were intended to protect. Retire a target only when a stronger maintained gate fully covers its failure class. Add a target only for a distinct recurrent or high-consequence escape. The purpose is bounded learning and safer lifecycle decisions, not a single impressive reliability number.

## Failure Mode Table

Use the table to classify observed evidence, not to guess from a symptom. Several modes can coexist. Identify the earliest invalid or stale lifecycle gate, preserve current state, and repair prerequisites in dependency order. A downstream success does not waive an upstream identity or authority failure.

Common response protocol:

1. Stop new package, marketplace, install, replacement, or removal mutation.
2. Capture nonsecret current state: request, creator root/hash, source paths, manifest, entries, installed identity/version, task freshness, recent actions, and recovery assets.
3. Mark affected PLDR gates `failed`, `blocked`, `stale`, or `unknown`; do not preserve a false pass.
4. Locate the earliest failed prerequisite and distinguish primary cause from contributing conditions.
5. Contain immediate security, shared-state, destructive, or wrong-source impact before ordinary diagnosis.
6. Apply the smallest authorized repair that predicts a new observable result.
7. Query the postcondition independently and verify unrelated state was preserved.
8. Refresh only dependent gates, then perform one cross-stage identity and final-claim review.

| lifecycle_stage | failure_mode_name | likely_trigger_or_early_signal | causal_consequence | immediate_containment | required_mitigation_and_verification | confidence_boundary |
| --- | --- | --- | --- | --- | --- | --- |
| route | plugin chosen for a standalone capability | request names one skill/server/script and no installation, marketplace, versioning, or coordinated lifecycle outcome | unnecessary manifest, distribution, update, removal, and component obligations obscure the actual capability | stop generation before shared or installed state changes | restate requested observable outcome, compare narrower surface, and proceed only if plugin identity adds explicit value | packaging fit remains judgment; record rejected alternative and reversal trigger |
| route | plugin lifecycle omitted when distribution is required | implementation begins as a loose component despite explicit installable or coordinated-package request | source may work locally but cannot satisfy discovery, identity, update, or removal acceptance | freeze component bytes and avoid inventing ad hoc distribution | route back to creator, select destination/identity, integrate component under one package, validate, and prove requested later stages | do not infer plugin need from terminology alone; rely on desired outcome |
| authority | wrong personal or shared destination | personal default is applied inside repository/team request, or shared path is chosen without policy | files land under the wrong owner; publication/recovery duties become unclear | stop writes and preserve both intended and actual path inventory | obtain explicit destination authority, move or recreate only with recovery and review, then revalidate all path-dependent evidence | file-system access does not establish organizational permission |
| creator contract | mixed creator roots | instructions come from current root while scaffold, validator, or update helper comes from archive or another installation | generated output and acceptance use incompatible contracts; result cannot be reproduced | record every root and stop package acceptance | select one target root, rerun scaffold fixture/validation under it, and document deliberate migration differences | newest path is not automatically project-authoritative; coherence must be proved |
| creator contract | sample conflicts with executable acceptance | illustrative `plugin.json` includes top-level `hooks` while selected instructions/validator reject it | copying the sample produces local rejection or misleading support claims | remove disputed key from current package and preserve conflict evidence | run a minimal fixture against recorded validator, scope conclusion to that contract, and assign docs/fixture owner | validator result establishes local acceptance only, not universal platform support |
| identity | normalized-name collision missed | proposed spelling differs but normalization maps to an existing folder, entry, or installed identity | creation overwrites, forks, or shadows an existing product | leave existing state untouched; do not force, delete, suffix, or install experimentally | inventory all identity surfaces, establish owner, then choose reuse, known update, recoverable replacement, or genuinely distinct identity | absent evidence of ownership is a blocker, not permission |
| identity | authoritative source unresolved | same plugin name appears in several directories or marketplace target differs from edited source | valid edits and validation apply to bytes Codex does not install | stop update/reinstall and preserve candidate sources plus installed state | resolve entry-to-source-to-installed chain with owner; only then update cache and reinstall | repeated installation cannot determine source authority reliably |
| mutation | force overwrites unknown or unrelated state | scaffold collision is bypassed to make generation complete | prior plugin bytes and provenance can be destroyed, preventing diagnosis and recovery | stop further writes, snapshot surviving files/entry/install state, notify affected owner | restore known-good state if possible; reconstruct diff; require explicit replacement authority before retry | successful force exit says nothing about legitimacy or recoverability |
| scaffold | generated metadata validates but is untruthful | defaults are accepted without product-specific review | users and agents receive wrong identity, description, version, URLs, or assets despite structural pass | withhold exposure/install and mark semantic review failed | compare every field with request and owned evidence, correct bytes, rerun validator, review diff | validator cannot determine product truth or ownership |
| component | speculative companions generated | every optional directory or declaration is created "for completeness" | maintenance, security, configuration, and test obligations expand without requested behavior | remove unrequested companions before publication and inspect manifest linkage | rebuild component inventory from accepted behavior; run component checks only for retained surfaces | presence does not prove usefulness; absence is correct when behavior is unnecessary |
| component | declared companion missing or mismatched | manifest declares app/MCP/asset while referenced file/configuration is absent or inconsistent | validation or runtime discovery fails; package identity may install without usable behavior | stop installation and preserve validator/component diagnostics | align declaration with real intended companion or remove it; rerun paired validator and specialist check | structural pass may not cover remote/service semantics |
| package | bytes change after validation | metadata, component, asset, or cache identity changes after last pass | recorded validation no longer applies to final package | mark package and dependent distribution/runtime gates stale | hash or otherwise anchor final bytes, rerun validator and affected component tests, then continue | read-only evidence changes need not invalidate unrelated gates |
| package | generic advice escapes theme review | plausible plugin guidance lacks selected root, concrete artifact, command/postcondition, or evidence boundary | reference looks authoritative but cannot drive or verify a real action | block reuse or final claim | tie recommendation to local source/explicit inference, add verification and counterexample, rerun focused verifier | polished prose is not operational evidence |
| marketplace | entry points to wrong source | same-name entry exists, manual edit retargets it, or path is assumed from identity | installation can succeed using stale or unrelated bytes | stop install/update; snapshot entry and both sources | independently resolve entry target, repair only with authority, preserve unrelated entries/order, then reinstall and query installed state | marketplace name and plugin name alone do not prove source target |
| marketplace | nondefault marketplace assumed configured | source validates but marketplace is not added/discoverable in current environment | install command fails or selects another source; local completion is overclaimed | preserve valid source and avoid ad hoc global configuration | hand off to platform owner or follow current explicit configuration policy; verify entry resolution before install | local creator cannot infer managed platform state |
| update | existing plugin recreated instead of updated | stale behavior is treated as a new scaffold problem | source relationship, history, user changes, and marketplace provenance may be lost | stop scaffold/force path and inventory preexisting state | prove authoritative source, preserve prior version, use current cache helper and reinstall flow, then test fresh task | update mechanics are version-specific and must follow selected current guidance |
| update | cache identity remains stale | source bytes change but installed system continues using previous cached identity | reinstall or current task appears unchanged despite correct source | avoid repeated unrelated edits; preserve source and installed evidence | after source/validation proof, use selected cachebuster helper, reinstall same resolved identity, query version, and start new task | cache is a plausible cause only after wrong-source and invalid-package causes are excluded |
| installation | successful action lacks postcondition | install command exits successfully but installed listing/source/version is not queried | wrong marketplace or version may be accepted as success | do not mark install gate passed | inspect installed identity/version and source relationship independently; preserve command result as action evidence only | CLI wording and exit semantics can change by version |
| runtime | same task used for pickup proof | plugin is installed/reinstalled while current conversation remains open | old context can hide new capability or retain stale behavior | mark runtime observation not fresh | start a new task after final install, verify visibility, then exercise bounded success and failure/unavailable path | fresh pickup proves only tested identity, version, component, and environment |
| external integration | local package proof promoted to service readiness | valid declaration or local invocation exists while credentials, remote permissions, or service health are unknown | users receive unsupported security/reliability claims and runtime failures | stop exposure to unintended audience and protect sensitive details | separate local package, credential, permission, service, and security gates; obtain owner evidence for each applicable claim | coarse remote errors may remain externally unresolved |
| sensitive data | credentials or private payloads enter source/logs | agent asks for or dumps values during config, debugging, or PLDR capture | secret exposure and incident response obligations arise | stop output, restrict access, notify responsible security owner, rotate/revoke through approved process | remove sensitive material from artifacts/history under policy, retain redacted diagnostic class, and review generation/logging boundary | do not reproduce secret values to prove cleanup |
| shared state | unauthorized repository or marketplace mutation | agent treats access as consent or carries personal defaults into shared environment | other users receive unreviewed capability or existing distribution is disrupted | halt publication, preserve changed-state evidence, notify owner | restore or review under repository/platform policy, rerun affected package/distribution gates, record impacted users | technical success cannot supply missing governance approval |
| replacement/removal | destructive action loses recovery or user data | deletion/replacement proceeds without inventory of source, entry, installation, and user-owned files | authoritative source, configuration, or recovery path is destroyed | stop at first sign, snapshot remaining state, avoid cleanup that erases provenance | involve owner, restore last known-good where possible, rebuild identity map, and rehearse current removal/replacement preflight | recovery may remain partial; report loss honestly rather than declaring clean state |
| workload | context loses request or gate state | long session, raw logs, or unsaved work obscures exclusions and current evidence | agent repeats work, broadens scope, or reuses stale results | stop mutation and write a durable checkpoint from observable state | reread request/spec/PLDR, reconcile changed paths and gates, resume one bounded action | if checkpoint cannot identify authority and source, escalate rather than guess |
| workload | parallel writers or tool fanout conflict | agents mutate same package, marketplace, or journal from different baselines | accepted evidence is stale on arrival; changes duplicate or overwrite one another | stop all writers and preserve each branch/result | designate authoritative state and single writer, reconcile diffs, rerun dependent checks, add ownership/lock control | read-only parallelism remains safe only with stable inputs and later reconciliation |
| retry | blind retries add no evidence | same install, validation, or generation action repeats after unchanged failure | noise and state churn grow while root cause remains | apply backpressure after the classified bounded retry | state what observation changed; return to earliest gate or hand off if none changed | transient classification needs evidence such as a changed external condition |
| evidence | source or external guidance drifts | selected file hash, CLI behavior, docs, API, policy, or release changes after reference/evidence | previously accurate instructions or claims become stale | mark dependent claims and gates stale before reuse | reread changed local sources; refresh authorized external evidence; rerun fixtures and scope migration | unchanged hash does not prove continued project authority |
| observability | raw transcript overwhelms or leaks | every command output and environment detail is pasted into journal | reviewers miss decisive result and sensitive context may escape | restrict record access and stop indiscriminate capture | summarize invocation, target, exit meaning, redacted diagnostic, postcondition, and artifact reference | too little evidence is also harmful; retain reproducible nonsecret anchors |
| quality gate | checklist or metric produces false assurance | boxes are marked from assertions; easy cases dominate score; severe miss is averaged | process appears green while identity, authority, or recovery is unsafe | block final claim and inspect underlying evidence | audit sample, retain failed/blocked cases, report severe escapes individually, repair metric definition or workflow | compliance count cannot override an observed safety failure |

**False-green priority**

Some failures are obvious: a validator exits nonzero or an expected companion is absent. Others are more dangerous because ordinary commands succeed:

- a valid package belongs to the wrong normalized identity;
- a marketplace successfully installs a different source;
- an install succeeds but the current task still shows stale behavior;
- metadata validates but describes the wrong product;
- a team source validates without publication authority;
- a local MCP declaration validates while remote credentials and service health remain unknown;
- a completion checklist is full but its evidence predates the final edit.

Always ask what the success signal proves and what nearby claim it does not prove.

**Diagnostic examples**

Good diagnosis: edits are not visible. The operator first compares intended source with marketplace target and discovers a mismatch. Installation stops. The owner selects the authoritative source, the entry is repaired under authority, the final package validates, cache identity is updated, the same resolved plugin is installed, and a new task shows the change. The cause predicts and explains the postcondition.

Bad diagnosis: edits are not visible, so the operator repeatedly changes version strings, reinstalls guessed identities, and adds files. One attempt appears to work in the current task. Source authority remains unknown, several evidence records are stale, and recovery is harder.

Borderline external diagnosis: local package, declaration, and install identity are proved, but a managed service returns a coarse authorization error that the operator cannot inspect. The local gates remain passed; service readiness is `pending_owner`; redacted evidence and the smallest reproduction go to the platform owner. The record does not invent a token, network, or service cause.

**Safe verification candidates**

Use isolated temporary fixtures to prove that the paired scaffold validates, name normalization detects collision before mutation, force remains opt-in, disputed top-level keys receive the recorded rejection, missing companion relationships fail, final-byte edits stale validation, and source-only PLDRs cannot pass runtime stages. Use synthetic marketplace files rather than active personal state for parser/source-resolution tests.

Use an owner-controlled test environment for marketplace configuration, installation, cache pickup, security permissions, remote service failure, replacement, and removal. Never induce destructive or credential failures against active user state merely to complete a table row. Where reproduction is unsafe, use read-only snapshots, causal timelines, and bounded simulation, then label realism limits.

A mitigation is verified when a pre-fix case exposes the mode, the repair changes the predicted premise, the independent postcondition passes, unrelated state remains intact, and dependent gates are refreshed. Keep competing hypotheses when evidence cannot discriminate them. Use `known` for directly reproduced causes, `inferred` for causes that best explain current observations with alternatives recorded, and `pending_external` when another owner must inspect hidden state.

Feed recurring or severe modes back into the earliest maintainable control: route examples, creator preflight, scaffold defaults, validator fixtures, manifest documentation, marketplace diagnostics, update helper, checkpoint, or policy. Every added control needs a distinct protected claim, counter-risk, owner, and retirement condition. The table should reduce surprise without making the common safe path an accumulation of unowned historical checks.

## Retry Backpressure Guidance

Do not repeat an action merely because its result was undesirable. Retry only when the failed signal is classified and a changed causal premise or evidenced transient dependency makes a different result plausible. The safest next action is often a read of current state, not another write.

The default sequence is:

1. **Freeze new mutation.** Preserve request, creator contract, target identity, source/entry/install state, last invocation, result, and recovery assets.
2. **Inspect partial effects.** A failed command may have changed files, entries, cache identity, installation, or remote state before reporting failure.
3. **Classify the failure.** Use deterministic input, stale evidence, missing context, transient dependency, permission/ownership, state conflict, true contradiction, or unknown.
4. **Choose repair, refresh, bounded retry, rollback, scope reduction, or handoff.** State why this action can change or discriminate the result.
5. **Bound attempts and effects.** Follow current tool/service guidance for any timing or count; no universal delay is asserted here.
6. **Query the postcondition independently.** A successful retry does not prove the first attempt had no effects.
7. **Refresh dependent gates and checkpoint.** Stop again if no new information was gained.

**Failure classes**

| failure_class | defining_evidence | default_response | retry_condition | stop_or_handoff_condition |
| --- | --- | --- | --- | --- |
| deterministic input or contract | same bytes, creator, validator, path, and preconditions reproducibly yield the same error | repair package, metadata, component linkage, or selected contract | rerun only after the relevant input/tool changed | stop if the correct target contract cannot be selected |
| stale evidence | prior result is tied to old package bytes, source hash, entry, cache identity, installed version, task, policy, or remote state | mark dependent claim stale and refresh the narrow gate | run the gate once against the new anchored state | stop if authoritative new state is unresolved |
| missing context | request, exclusion, source identity, owner, or prior mutation is unknown | inspect and checkpoint; ask or route only for a consequential missing fact | resume action after the missing precondition is established | block mutation when identity, authority, or recovery remains unknown |
| transient dependency | current evidence indicates timeout, temporary unavailability, or externally changing state and no partial harmful mutation is observed | wait/back off according to current platform guidance and make a bounded attempt | retry while within owned budget and each attempt records state | circuit-break when budget is reached, signal changes class, or effects become ambiguous |
| permission or ownership | access is denied or no accountable owner authorized the stage | hand off with source/evidence; do not alter package to evade governance | retry only after explicit permission/owner state changes | stop immediately if requested workaround would broaden privilege or exposure |
| state conflict | normalized collision, changed baseline, competing writer, wrong marketplace source, or version conflict exists | preserve all candidates, choose authoritative state, reconcile or rollback | retry after conflict resolution and new baseline proof | escalate when authority or recovery cannot be established |
| true contradiction | two current authoritative sources or observations require incompatible behavior | isolate minimal reproduction, record both claims, select owner for contract resolution | rerun only under a deliberately chosen target contract or after source repair | do not blend contracts to manufacture a pass |
| unknown | available diagnostics do not distinguish plausible causes | perform one safe, information-gaining probe or route to owner | retry only when the probe changes confidence or state | stop blind repetition when no discriminatory observation is available |

**Gate-specific policy**

| gate_or_action | usual_failure_character | safe_next_action | retry_boundary |
| --- | --- | --- | --- |
| local source read or hash | missing path, permission, or changed bytes | verify selected root/path and ownership; reread changed source | repeat after path/permission/file change, not to make old evidence reappear |
| scaffold into unused isolated destination | deterministic arguments and filesystem state | inspect partial directory, remove only newly owned fixture state, correct arguments or identity | rerun after isolated target is clean and authoritative; never convert collision to force by default |
| normalized collision | deterministic state conflict | inventory owner/source/entry/install and select reuse, update, replacement, or new identity | no creation retry until ownership decision changes the premise |
| validator | deterministic package bytes and validator version | correct exact rejected structure or resolve contract conflict | rerun after bytes or validator change; unchanged invalid input does not merit repetition |
| component test | implementation, dependency, environment, or external-state failure | isolate component cause, preserve package linkage, correct or hand off | follow component policy; rerun only after relevant premise or transient evidence changes |
| marketplace inspection/read | local state or platform availability | distinguish missing/unconfigured from transient read failure; preserve source-only work | one bounded diagnostic/refresh may clarify transient or stale evidence; hand off if configuration authority is absent |
| marketplace write | active shared/personal state mutation | inspect whether entry partially changed and whether unrelated entries/order remain | retry only after authoritative baseline and idempotent/transactional behavior are proved |
| cache identity helper | deterministic source mutation | inspect exact targeted diff and prior value; correct source relationship first | do not bump repeatedly; rerun only for a deliberate new package update under helper contract |
| install or reinstall | platform mutation with possible partial success | query installed identity/version and marketplace source before another action | retry after transient evidence or corrected package/source/cache premise, within current platform policy |
| fresh-task pickup | task startup, installed identity, package linkage, or component/runtime state | confirm final install and start a genuinely new task; isolate visible versus behavioral failure | new task is a required new observation after install, not an unbounded loop |
| remote integration | permissions, credentials, network, service health, or contract | protect secrets; separate local/package from remote cause; involve owner | follow service-specific retry and rate policy only after classifying authorization versus transient failure |
| replacement or removal | destructive active-state mutation | inspect partial effects, preserve user data and provenance, invoke recovery owner | no automatic retry without current inventory, explicit authority, and proved recovery |
| focused reference verifier | deterministic files/spec/test code | fix exact failing invariant and rerun affected/full gate | repeat after content or verifier changes; unchanged failure output adds no evidence |

The seed's "one bounded retry" for stale external evidence is a conservative default for a documentation refresh, not a universal service policy. Refresh only when browsing or external access is authorized. If one refresh still leaves evidence stale, contradictory, or inaccessible, route to a human or narrower source-specific workflow rather than broadening searches indefinitely. Current provider guidance governs actual external API retry timing and rate limits.

**Action risk and backpressure**

- **Read-only inspection:** generally repeatable, but avoid unbounded scans and sensitive output. Stop when new reads no longer discriminate hypotheses.
- **Isolated fixture mutation:** repeatable after fixture state is inventoried and reset safely. Never point a fixture at active plugin or marketplace state.
- **Authoritative package mutation:** serialize under one writer, inspect partial effects, preserve prior source/version, and rerun package evidence.
- **Marketplace/install mutation:** require exact target identity, authorization, independent postcondition, and current platform policy.
- **Destructive or externally consequential mutation:** no automatic retry. Require accountable owner, affected-state inventory, recovery proof, and explicit new authorization when relevant.

Apply backpressure at the earliest red gate:

- stop component work when plugin fit or destination authority is unresolved;
- stop package acceptance when creator contract, identity, metadata, or component linkage is red;
- stop marketplace/install work when final bytes or source target are red;
- stop runtime claims when installed identity or task freshness is red;
- stop new feature generation when recovery from a prior mutation is incomplete;
- stop distributed writers when ownership or baseline conflicts appear;
- stop external calls when retry budget, permission boundary, or sensitive-data policy is unclear.

**Retry record**

```yaml
retry_record:
  gate: "failed lifecycle stage"
  target_identity: "source, plugin, marketplace, install, task, or service"
  prior_invocation_and_result: "bounded nonsecret summary"
  partial_effects_checked: "observed state after prior action"
  failure_class: "deterministic | stale | missing-context | transient | permission | conflict | contradiction | unknown"
  classification_evidence: "why this class fits"
  competing_hypotheses: ["alternatives not yet ruled out"]
  changed_premise: "input, tool, state, permission, time-dependent signal, or diagnostic probe"
  proposed_action: "repair, refresh, retry, rollback, narrow, or handoff"
  allowed_effects: ["exact bounded mutations"]
  attempt_budget_source: "current tool/service policy or locally owned alarm"
  independent_postcondition: "state query after action"
  unrelated_state_preservation: "what must remain unchanged"
  stop_condition: "when repetition ends"
  dependent_gates_to_refresh: ["claims made stale by the action"]
```

**Examples**

Good transient retry: a marketplace read that previously succeeded returns a documented temporary availability signal. The operator confirms no write occurred, records source identity, waits according to current platform guidance, and makes one bounded read. If it succeeds, source resolution continues; if it remains coarse or unavailable, source work is preserved and the platform owner receives the handoff. No package files are changed to address a read outage.

Bad state-conflict retry: scaffold reports an existing normalized destination. The operator repeats with force, then changes the name suffix and installs both variants. The first signal was a deterministic identity conflict; retries destroyed evidence and forked product identity.

Good deterministic rerun: validator rejects a missing declared companion. The package declaration is corrected to the actual requested component, final bytes change, and the same validator is run again. This is not blind repetition because the dependency changed and the new result is anchored to new bytes.

Good update sequence: changed source validates, authoritative marketplace relationship is proved, cache identity is updated once through the current helper, the same resolved plugin is reinstalled, installed identity is queried, and a new task tests behavior. Repeated cache bumps would add version churn without new evidence.

Borderline unknown remote error: local package/install gates pass, but an external tool returns a coarse failure. One safe, redacted diagnostic probe distinguishes availability from authorization only if current service guidance permits it. If ambiguity remains, the remote owner receives evidence; the agent does not cycle credentials or flood calls.

**Verification**

Test retry rules in isolated fixtures: repeat scaffold collision without state change and prove no new mutation; fix a deterministic validator fixture and prove only the changed input enables pass; simulate a transient read while verifying no duplicate write; repeat the cache helper under its documented contract and inspect exact diffs; ensure source-only records cannot gain runtime passes through retry. For active platform behavior, use owner-controlled test state and inspect both eventual result and absence of duplicate/unrelated effects.

Deterministic local dependencies, changed-premise requirements, evidence preservation, and independent postconditions are stable guidance. Exact retry counts, delays, timeout budgets, and provider error classes remain tool/service/version-specific. Calibrate local alarms from observed runs, and allow transactional tools to use different mechanics only when they prove equivalent identity, atomicity, conflict detection, and recovery.

Aggregate retry causes, not just attempt counts. Repeated wrong-source installs call for source diagnostics. Repeated validator reruns call for scaffold/docs alignment. Repeated permission retries call for ownership routing. Improve diagnostics and preflight before automating repetition. A healthy retry system increases information per attempt and ends in a coherent state, even when the correct endpoint is an explicit stop.

## Observability Checklist

Observability must let an independent operator reconstruct one plugin's authoritative state, actions, current evidence, failure boundary, recovery, and next owner without relying on hidden conversation memory. It is not a mandate to retain every command byte.

Use the PLDR as the lifecycle summary and append one structured event for each consequential decision, mutation, postcondition, retry classification, handoff, and evidence invalidation. A read-only explanation can use a compact source/decision note; source, marketplace, install, shared, remote, update, replacement, or removal work uses the full applicable profile.

**Lifecycle event envelope**

```yaml
plugin_lifecycle_event:
  record_id: "stable correlation with one PLDR"
  sequence: "monotonic order within this lifecycle"
  observed_at: "timestamp when cross-system freshness matters"
  plugin_identity: "normalized name plus destination class"
  authoritative_source: "path or unresolved candidate set"
  creator_contract: "root and consequential hashes"
  lifecycle_stage: "route, identity, package, component, marketplace, install, runtime, recovery, or handoff"
  event_kind: "decision | inspect | mutate | postcondition | fail | retry | invalidate | handoff"
  actor_and_authority: "operator or owner plus authority source"
  target: "exact nonsecret file, entry, install identity, task, or external boundary"
  prestate_anchor: "state/hash/version before action"
  action_summary: "bounded operation or reviewer decision"
  result_summary: "exit meaning or observed decision, redacted"
  independent_postcondition: "queried state after mutation"
  affected_claims: ["what this event supports or invalidates"]
  freshness_anchor: "bytes, tool, entry, version, task, policy, or remote-state reference"
  unrelated_state_preserved: "explicit observation where mutation occurred"
  sensitive_data_status: "none captured or redaction/reference policy"
  evidence_reference: "approved detailed artifact when needed"
  next_action_or_stop: "one bounded continuation or stop condition"
```

Sequence is sufficient for a serialized local workflow. Use timestamps when events cross systems, owners, tasks, or asynchronous services and timing affects freshness. Do not infer strict ordering from clocks that are not known to be synchronized.

**Stage checklist**

| stage | minimum_observable_state | decisive_event | common_missing_signal |
| --- | --- | --- | --- |
| request and route | requested outcome, audience, completion depth, exclusions, selected/rejected surfaces | route decision with reversal trigger | plugin selected from vocabulary without desired postcondition |
| creator contract | selected root, workflow/reference/script hashes, known conflicts | contract selection and any observed fixture | instructions and validator silently come from different roots |
| destination and identity | proposed/normalized name, destination owner, folders, manifests, entries, installed candidates | collision/source-authority decision | successful path access mistaken for ownership or no collision check |
| component inventory | requested behavior, included/omitted surfaces, package linkage, owner | specialist acceptance or explicit omission | generated directory counted as implemented behavior |
| source mutation | exact changed paths, generated diff, semantic metadata review, prior state | one bounded write event plus post-edit diff | only scaffold command output, no final-byte review |
| package validation | validator root/hash, exact target bytes, invocation, result, limitation | current validator pass/fail linked to package anchor | pass predates final edit or is promoted to runtime/security proof |
| marketplace | marketplace file/name, entry identity, source target, preservation of unrelated entries | entry mutation plus independent source-resolution query | plugin/marketplace name recorded but source target absent |
| install/cache | prior/current cache identity, install invocation, resulting installed identity/version | install or reinstall plus independent listing | action exit recorded with no installed postcondition |
| fresh runtime | new-task marker, visible identity, bounded success, failure/unavailable path | task observation tied to final install | current conversation treated as fresh pickup |
| external/security | local package boundary, secret reference policy, remote owner, permission/service acceptance | owner-approved result or explicit pending boundary | local declaration promoted to remote readiness |
| retry | prior result, partial effects, failure class, changed premise, budget source, postcondition | information-gaining attempt or explicit circuit break | repeated command with no new evidence |
| recovery/handoff | last known-good, affected state, rollback/removal preflight, owner, next observation | recovery result or accepted handoff | generic "escalate" with no owner or return condition |

**Evidence type selection**

| evidence_type | what_it_proves_well | what_it_does_not_prove | retention_guidance |
| --- | --- | --- | --- |
| source hash | exact bytes of an inspected local source or package | correctness, authority, semantic truth, or behavior | retain hash with path/version; reread when authority or bytes change |
| filesystem diff | what paths/bytes changed relative to a baseline | why the change is authorized or whether runtime uses it | keep concise summary in PLDR and detailed diff in normal source-review location |
| command summary | invocation, target, exit meaning, decisive diagnostic | independent postcondition or absence of partial effects | record nonsecret summary; link detailed output only when needed |
| validator result | selected local structural acceptance for anchored bytes | metadata truth, component usefulness, distribution, security, or invocation | retain tool hash/version, target anchor, and decisive result |
| marketplace snapshot | entry identity, source target, and unrelated-state comparison | installed pickup or platform approval beyond observed state | protect personal/team paths under policy; store only needed fields |
| installed listing | observed plugin identity/version after action | source correctness unless relationship is separately proved; fresh-task behavior | tie to marketplace/source assertion and install event |
| fresh-task report | capability visibility and tested behavior under a new task | untested components, users, environments, remote SLOs, or future versions | summarize bounded cases; do not retain unrelated conversation |
| metric | frequency, latency, effort, or trend for defined cohort | individual causal explanation or safety | store formula, cohort, missingness, and owner; avoid unsupported thresholds |
| owner attestation | accountable policy, approval, or managed-stage acceptance | hidden technical details not included in attestation | retain scope, conditions, owner, and stable reference |

Hashes establish evidence identity. Diffs establish change. Postcondition queries establish observed state. Reviewer decisions establish semantic or governance acceptance. None replaces the others.

**Operational metrics, when a decision requires them**

Capture tool-call count, context files loaded, delegated tasks/owners, retry count by class, handoff count, stale-gate count, wall time, and completion-audit outcome only when they answer a workload or improvement question. Record p50/p95/p99 latency or reviewer time only for a sufficiently defined and repeated cohort; include input, environment, sample, measurement method, and uncertainty. A single run has no meaningful percentile distribution and must not be labeled as one.

When this reference drives recurring work, retain the leading indicator and failure signal from the outcome section: eligible users can install, invoke, diagnose, and remove without reading implementation code; failures include confusing adjacent extension types or omitting recovery. Segment source-only work so absent runtime stages are not counted as failures.

**Redaction, access, and retention**

- Never store credential values, access tokens, private payloads, or broad environment dumps in PLDR or ordinary logs.
- Refer to approved secret locations or owners without copying values.
- Preserve nonsecret identity needed for diagnosis: normalized plugin name, selected path, manifest version, source hashes, marketplace identity/target, and installed version under applicable policy.
- Redact diagnostics to error class and decisive nonsecret context; keep detailed artifacts in approved access-controlled storage only when necessary.
- Define owner and retention for personal paths, team marketplace details, remote request identifiers, screenshots, traces, and user data.
- Remove routine output that does not support a claim, failure hypothesis, audit, or recovery.
- Record known missing evidence instead of filling the gap with more unrelated logs.

Audit evidence should stay small enough to review: source inventory, command/postcondition summary, exact changed-file list, gate ledger, retry classification, owner handoff, and unresolved-risk notes are preferable to raw transcript dumps. Detailed artifacts remain linked, not duplicated.

**Data-quality checks**

- [ ] Every event points to one record and normalized plugin identity or explicitly unresolved candidate set.
- [ ] Mutations include prestate, target, result, independent postcondition, and unrelated-state preservation.
- [ ] Evidence is tied to a freshness anchor and marked stale after a dependent change.
- [ ] Retries link to the prior attempt and name a changed premise.
- [ ] Failures and blocked outcomes are retained; successful cases do not dominate through omission.
- [ ] Source, manifest, marketplace, install, and task identities are not conflated.
- [ ] External blind spots name owner and pending acceptance instead of speculative internals.
- [ ] Sensitive-data status is explicit and retained artifacts follow approved access/retention.
- [ ] Metrics include formula, cohort, sample/missingness, and interpretation limits.
- [ ] Final claim can be derived from current passed gates and explicit incomplete stages.

**Examples**

Good wrong-source trace: the record shows request to update plugin `x`, intended source A, marketplace inspection resolving source B, install state tied to B, and a blocked update gate. No reinstall occurs. The owner selects A or B, the entry/source relationship changes under authority, package B or A is validated as selected, cache/install events follow, and a fresh task observes behavior. Each event explains why later evidence changed.

Bad trace: a multi-thousand-line transcript contains directory listings, full environment values, several install attempts, and validator output. It lacks normalized identity, marketplace source target, final bytes, installed version, task freshness, and a final claim. Volume cannot answer which source Codex used and may expose sensitive state.

Bounded managed trace: local source, validation, and component evidence are complete. The platform owner returns an approval reference and reports configured marketplace identity/source target but exposes no internal logs. The lifecycle owner records the attestation scope and marks fresh invocation pending until independently tested. Hidden platform detail is not invented.

**Reconstruction drill**

Hide conversation context and provide only the approved PLDR, lifecycle events, and linked nonsecret artifacts to a reviewer. The reviewer must identify:

1. requested state and explicit exclusions;
2. selected surface, creator contract, destination authority, and normalized identity;
3. authoritative source and exact mutations;
4. current package, component, marketplace, install, and runtime gate status;
5. first failed/stale gate and primary versus contributing cause;
6. which evidence became invalid after each change;
7. unrelated/user-owned state preserved;
8. recovery, next owner, next observation, and prohibited overclaim.

Run the drill across personal creation, existing update, shared handoff, remote integration, and recovery-sensitive cases. Intentionally remove one decisive signal, such as marketplace source or task freshness, and confirm the reviewer cannot safely make the corresponding claim. If the answer remains unchanged, either the signal was redundant and can be pruned or the drill/rubric is too weak.

Local hashes, diffs, validator results, entries, and installed listings are directly observable when captured against the right identity and final state. Retention policy, external tracing, and ideal metric sampling vary by environment. Improve producers when recurring ambiguity appears: make source target visible, emit structured validator diagnostics, include correlation fields, prompt for fresh-task proof, or tighten redaction. Add a signal only for a distinct diagnostic question and prune it when stronger evidence fully subsumes it.

## Performance Verification Method

Performance verification begins by naming the surface under test. Do not combine these into one unlabeled "plugin creation time":

| performance_surface | start_and_end_boundary | correctness_precondition | dominant_variability | appropriate_method |
| --- | --- | --- | --- | --- |
| route and planning effort | complete request available to accepted route, exclusions, and next gate | route satisfies observable outcome, authority, identity, and recovery rubric | request ambiguity, source loading, model/operator behavior | frozen scenario review with event timing and decision audit |
| scaffold execution | invocation begins to final generated filesystem state | expected target only, collision safeguards preserved, generated package valid under paired contract | filesystem, interpreter startup, destination state, optional components | isolated fixture microbenchmark plus exact diff/validation |
| validator execution | final package anchor submitted to decisive result | result is semantically correct for known valid/invalid fixtures | package size/shape, filesystem, interpreter startup, cache | paired valid/invalid corpus benchmark |
| component verification | component test starts to accepted result | behavior, failure case, and package linkage are correct | component domain, dependencies, network/service state | component-owned benchmark or scenario under its contract |
| marketplace and install | authorized action begins to independently observed entry/install postcondition | intended source and identity selected; unrelated state preserved | platform load, cache, local I/O, network, marketplace configuration | owner-controlled scenario with stage events and current policy |
| fresh pickup | new task startup begins to capability visible and bounded behavior observed | final installed identity/version and package/component gates pass | task startup, model/platform, cache, external dependencies | repeated fresh-task scenario with explicit environment and outcome |
| end-to-end lifecycle | request begins to requested authorized completion and recoverable PLDR | every applicable route, package, distribution, runtime, and recovery gate is correct | all prior sources plus owner handoffs and retries | representative scenario distribution with stage decomposition |
| reviewer decision effort | reviewer receives approved evidence to correct next action, gate, stop, and recovery decision | answer matches rubric without unrelated source reading | record quality, reviewer familiarity, scenario complexity | blinded reconstruction drill and bounded reviewer-time measurement |

A faster result that chooses the wrong surface, targets the wrong source, skips validation, mutates unauthorized state, or omits recovery fails correctness and is excluded from positive performance claims. Retain it as a failure observation rather than deleting it from the dataset.

**Default evidence rule**

Make no quantitative speed, latency, throughput, or effort claim until all of the following exist:

1. a concrete hypothesis and decision the measurement will inform;
2. a defined performance surface and stage boundaries;
3. correctness and preservation gates that every counted run must satisfy;
4. representative fixture/input with frozen source and package hashes;
5. environment, creator/tool versions, destination state, and relevant external conditions;
6. baseline and candidate measured through the same method;
7. repeated samples appropriate to observed variance and decision consequence;
8. cache/warmup, startup, concurrency, retry, failure, and outlier treatment;
9. raw approved observations or reproducible aggregate source;
10. uncertainty, limitations, and a claim no broader than the cohort.

One run can reveal a hang, severe regression, or case-specific upper observation. Report it as "this run took ... under ..." rather than p50, p95, p99, average population performance, or a general guarantee. Percentiles require enough observations and a stated calculation method; this reference does not invent a universal sample count.

Operational timeouts, tool-call limits, and retry budgets are capacity controls, not benchmark results. A workflow owner may set them from current platform behavior, cost, and risk. Crossing a control triggers checkpoint, classification, and possible split or handoff; remaining under it does not establish success or good performance.

**Method selection**

| method | choose_when | strength | limitation |
| --- | --- | --- | --- |
| event stopwatch | locating a coarse stage bottleneck in a real lifecycle | low instrumentation cost and direct user-path timing | weak causal control; includes platform and operator variance |
| structured stage timing | comparing where end-to-end time is spent | preserves decomposition and retry/handoff context | event boundaries and instrumentation need maintenance |
| microbenchmark | testing scaffold/validator or deterministic helper regression | repeatable and attributable under controlled input | may omit startup, interaction, platform, and user impact |
| end-to-end scenario | deciding whether a change improves requested lifecycle | realistic outcome and correctness coverage | higher variance, cost, and harder causal attribution |
| profiler or trace | explaining local CPU/I/O or component hot path | detailed mechanism evidence | can perturb timing and expose sensitive detail; platform access may be absent |
| reviewer study | measuring reference actionability and evidence quality | captures human decision cost and ambiguity | learning effects, reviewer variation, and small cohorts |
| operational telemetry | observing recurring real workloads and tails | reveals variance and rare conditions | privacy, retention, confounding, selection, and ownership obligations |

Use controlled benchmarks to establish likely cause and representative scenarios to establish practical impact. A consequential optimization may need both.

**Measurement packet**

```yaml
performance_measurement:
  claim_id: "stable identifier"
  hypothesis: "what may improve or regress and why"
  decision_if_supported: "specific bounded intervention"
  performance_surface: "route, scaffold, validator, component, platform, pickup, end-to-end, or review"
  stage_boundaries: "observable start and end events"
  correctness_gates:
    - "route, identity, package, behavior, preservation, and recovery requirements"
  fixture:
    description: "representative input and lifecycle profile"
    source_and_package_hashes: ["frozen anchors"]
    size_shape_and_components: "facts relevant to cost"
  environment:
    creator_root_and_hashes: "selected contract"
    runtime_and_tool_versions: "relevant versions"
    filesystem_and_destination_state: "clean, collision, existing update, or other"
    platform_network_remote_state: "observed conditions or not applicable"
    concurrency_and_resource_context: "relevant contention"
  design:
    baseline: "current behavior"
    candidate: "proposed change"
    sample_and_order_reason: "why observations support the decision"
    warmup_and_cache_policy: "cold/warm separation or reset"
    retry_failure_and_outlier_policy: "predeclared treatment"
    instrumentation_overhead_check: "when material"
  observations:
    stage_times: ["approved raw or referenced samples"]
    tool_calls_sources_handoffs_and_retries: "workflow context"
    correctness_failures: ["retained, not hidden"]
    p50_p95_p99_if_justified: "method and result, otherwise omitted"
    reviewer_time_if_applicable: "defined task and cohort"
  analysis:
    comparison: "baseline versus candidate"
    variability_and_uncertainty: "observed spread and limitations"
    competing_explanations: ["cache, startup, platform, learning, or other"]
    effect_on_balancing_guards: "route, identity, preservation, completion, recovery"
  conclusion:
    bounded_claim: "what evidence supports"
    unsupported_extension: "what must not be inferred"
    adoption_or_rejection: "decision and owner"
    rerun_trigger: "fixture, tool, environment, or platform drift"
```

Capture input size/shape, source count, tool-call count, wall time, retry classifications, handoffs, and reviewer time only where they explain the measured surface. Report p50/p95/p99 only where the sample and use case justify them. An input count is not a performance explanation by itself; record the characteristics that drive work, such as component count, manifest/assets, identity ambiguity, remote dependency, and lifecycle depth.

**Run validity checklist**

- [ ] Baseline and candidate use the same accepted request, fixture, selected contract, and correctness rubric.
- [ ] Source/package hashes and final result are recorded for every counted run.
- [ ] Failed, blocked, retried, and abandoned outcomes follow a predeclared inclusion policy.
- [ ] Cold startup and warm cache are separated or their mixture is deliberate and reported.
- [ ] Marketplace/network/service variance is not attributed to local source without stage evidence.
- [ ] Parallel contention and background load are controlled or documented.
- [ ] Instrumentation does not materially alter the short operation, or overhead is measured.
- [ ] Outliers are retained and explained; removal criteria were not invented after viewing results.
- [ ] Reviewer order and learning effects are randomized, counterbalanced, or acknowledged where relevant.
- [ ] No secrets or private payloads appear in fixtures or telemetry.
- [ ] The claim uses only the cohort and environment measured.

**Examples**

Good local regression evidence: a validator change is tested against the same frozen valid and invalid package corpus, under the same interpreter/environment and cache policy. All decisions remain correct. Repeated observations show the candidate consistently changes execution time in one direction, with distribution and uncertainty reported. A representative source-validation workflow is then checked to confirm the change matters and does not degrade diagnostics.

Bad speed claim: an agent creates one tiny personal package, skips collision inventory and fresh-task proof, observes a short wall time, and claims plugin creation is faster. There is no baseline, representative input, repeated sample, or correct end state. The skipped work is the apparent optimization.

Borderline platform observation: installs take longer during one external-service period while local package, source identity, and validator stages remain stable. The record can state that observed install-stage time increased for those runs. It cannot attribute the increase to plugin bytes or claim a platform regression without owner evidence.

Good reviewer-effort test: reviewers receive only PLDR/event artifacts for frozen scenarios and must identify next action, verification gate, stop condition, and recovery. Correctness is scored first; decision time is then compared under the same rubric. A faster wrong answer is a failure, not a performance win.

**Original operational pass/fail conditions, refined**

The reference passes its actionability condition when a reviewer can identify the correct next action, verification gate, stop condition, and recovery without reading unrelated files. The leading outcome remains that eligible users can install, invoke, diagnose, and remove without implementation-code archaeology. The failure signal remains extension-surface confusion or omitted recovery.

The reference fails as an operating guide when it encourages implementation before workload, reliability target, and failure modes are explicit; when it publishes an unsupported performance number; or when speed measurement excludes correctness and blocked/failure cases. A resumable journal is required when work exceeds one focused session or crosses handoff/state boundaries, regardless of whether measured wall time is low.

**Optimization feedback**

Stage evidence may show that source discovery, identity resolution, validator startup, component tests, marketplace handoff, install/cache retries, fresh-task startup, or reviewer ambiguity dominates. Choose the smallest intervention at the observed stage: better source index, identity preflight, paired fixtures, clearer diagnostics, structured handoff, or removal of an unnecessary lifecycle step. Recheck end to end because local optimization can shift cost, reduce observability, or weaken preservation.

No current local source establishes universal creator latency, throughput, reviewer-time, or percentile targets. Adopt repository or platform SLOs only with an owner, source, cohort, and executable verification. Confidence in the direction of a controlled regression can be higher than confidence in absolute magnitude or end-user relevance; state both separately.

## Scale Boundary Statement

This reference is sufficient while one Plugin Lifecycle Decision Record can represent one coherent plugin identity, authoritative source relationship, requested completion, specialist handoffs, current evidence, and recovery without hiding independently failing systems. It can coordinate several owners; it does not replace their component, service, security, marketplace, repository, or operational control planes.

The smallest independently failing and recoverable state is the control unit. Usually that is one normalized plugin identity. A transactional platform may define a larger atomic unit, but only when its isolation, conflict handling, partial-failure semantics, observability, and rollback are explicit and tested.

**Scale dimensions**

| dimension | remains_within_this_reference | route_or_split_signal | retained_leaf_invariant |
| --- | --- | --- | --- |
| plugin identities | one identity, including a known update/replacement/removal lifecycle | several independent plugins, versions, destinations, or aliases are mutated together | per identity: source, manifest, entry, install, runtime, and recovery remain traceable |
| ownership | bounded handoffs return evidence to one lifecycle reconciler | cross-team policy, approval, scheduling, or incident coordination becomes the primary work | every stage has one accountable owner and explicit return condition |
| components | several package components with independent specialist evidence | a component is an independently operated product/service with its own releases, data, SLO, and incidents | package linkage and imported acceptance stay scoped to the plugin version |
| marketplace | one intended entry/source relationship under known authority | bulk entry management, shared transactional updates, rollout cohorts, or fleet policy | exact target, unrelated-state preservation, postcondition, and rollback per affected identity |
| installation/runtime | one plugin or bounded audience can be installed and freshly tested | organization rollout, many users/environments, compatibility matrix, staged release, or widespread rollback | installed version/source and observed behavior remain attributable per cohort/identity |
| external systems | local package coordinates one approved integration and imports owner evidence | service architecture, capacity, data lifecycle, security operations, or production traffic are being designed/operated | local declaration never substitutes for service/security acceptance |
| source discovery | selected creator root and ranked sources can be read coherently | discovery is unbounded, many repositories/versions conflict, or authority cannot be ranked | target contract and consequential source hashes are explicit before mutation |
| execution concurrency | isolated reads and separately owned components reconcile before serial mutation | parallel writers target same package, marketplace, install state, or lifecycle record | one writer or proved transaction owns each mutable state surface |
| duration/context | checkpoints keep current identity, gates, risks, and next action recoverable | operator can no longer state authoritative state or evidence freshness from the record | context drift is a reliability failure; mutation stops until checkpoint reconciliation |
| operational reliability | plugin packaging consumes imported component/platform acceptance | production traffic or user impact needs SLOs, on-call, incident handling, capacity, data/security controls | this reference does not invent SLOs; it links owner-supplied evidence and boundaries |

**In-scope profiles**

- A personal plugin with one or several local components, an inspected personal marketplace entry, install, fresh-task check, and removal handoff.
- A known existing plugin update where one source-entry-install identity can be proved and preserved.
- A repository/team plugin whose source and components are locally owned and whose managed marketplace stage is handed to a named administrator.
- A plugin containing a remote integration when local package work is separated from credential, permission, service, and security acceptance returned by owners.
- A read-only audit or deterministic validation batch, provided each plugin result remains separately identifiable and no active shared state is mutated.

**Route-out profiles**

- Fleet creation, update, migration, replacement, or removal across independent plugin identities.
- Organization marketplace administration with policy, access control, transactions, rollout cohorts, audit retention, and rollback operations.
- Cross-repository release engineering, compatibility management, or schema migration that coordinates many versioned packages.
- Production service design or operations for an MCP server, app backend, data pipeline, or other independent component.
- Security architecture, credential lifecycle, privacy/data governance, incident response, or permission administration.
- Unbounded source archaeology across many roots where the target creator contract cannot yet be ranked.
- Multi-agent execution with shared writes and no lock, merge queue, transaction, or authoritative reconciler.
- Production traffic without an explicit owner-supplied reliability target, instrumentation, incident path, and capacity plan.

Routing out does not discard this guide. The orchestrator, release process, or service owner should use the one-plugin lifecycle contract as a leaf-level acceptance unit.

**Scale modes and control planes**

| mode | appropriate_control | why_this_reference_alone_is_insufficient | evidence_returned_to_each_pldr |
| --- | --- | --- | --- |
| small finite sequence | separate sequential PLDRs and shared read-only checklist | little benefit from platform investment; state remains inspectable manually | per-plugin source, validation, action, result, recovery |
| deterministic audit batch | script or job with frozen creator contract and per-target results | manual repetition is wasteful but mutation is unnecessary | exact identity/source, fixture/tool version, pass/fail/unknown, next action |
| controlled migration | versioned migration plan, dry run, canary cohorts, queue/locking, per-target rollback | order, compatibility, partial failure, and resumption span many identities | prestate, migration result, exceptions, final version/source, rollback status |
| marketplace fleet | owned platform with access policy, transactional semantics, audit log, conflict detection, staged rollout | shared entries and users create coupled consequences and governance | entry/source transition, installed cohort, postcondition, unrelated preservation, rollback |
| independent service | component engineering and operations with contract, SLO, telemetry, security, incident and release processes | package guidance cannot establish runtime capacity or production reliability | versioned interface/acceptance evidence and limitations imported into plugin record |
| multi-agent program | orchestrator with assignment manifest, exclusive writes, durable progress, merge/audit checkpoints | parallel reasoning and writes otherwise fork identity and invalidate evidence | owner, changed paths, verifier result, conflicts, accepted artifact hash, next dependency |

Do not build a control plane merely because a batch has several files. Escalate when repeated coordination, coupled consequences, concurrent mutation, governance, or recovery isolation justify maintained automation and ownership. A short finite batch can remain sequential; a single plugin can require route-out service operations.

**Scaled-operation invariants**

1. Every target has a stable identity and prestate before mutation.
2. Discovery and validation may batch, but each result maps to one target and selected contract.
3. Mutations are isolated through serialization, locking, queueing, or proved transactions.
4. Global force is prohibited; replacement authority and recovery are per target.
5. Version/schema cohorts are explicit, and migration logic is tested against each supported cohort.
6. Rollout is staged where blast radius warrants it; canary acceptance and stop conditions are defined.
7. Partial failure is first-class: unaffected targets retain valid outcomes, failed targets retain exact state and resume/rollback action.
8. Aggregate success is decomposable into per-target evidence; no boolean batch pass hides exceptions.
9. Shared automation preserves sensitive-data boundaries, audit ownership, retention, and least authority.
10. Final runtime/service claims come from their owners, not from package or rollout completion.

**Distributed execution**

Split by independent plugin, component contract, evidence-only review, or platform authority. Preserve one writer per file/state surface and one verification owner per split. Parallel agents must not rewrite the same reference, package, manifest, marketplace, or progress record without an explicit lock/merge mechanism and a post-merge full verifier. A merge checkpoint records accepted baseline, conflicting changes, final artifact hashes, stale evidence, and next owner.

Read-only analyses can run concurrently when they share a frozen baseline. Returned recommendations reconcile before writes. If one result changes the source/contract assumptions of another, mark the latter stale rather than merging both conclusions.

**Long-running workflows**

Context drift is a reliability failure. At every meaningful batch, owner handoff, phase change, or before destructive/shared mutation, persist plugin identities, source/creator anchors, changed paths, gate statuses, failures/retries, open risks, recovery, and immediate next step. Reread current spec/policy and checkpoint before continuing. If authoritative state cannot be reconstructed, stop mutation and inventory; do not fill gaps from memory.

**Large-codebase discovery**

Narrow before applying this reference. Rank repository policy, selected creator root, package source, marketplace configuration, component contracts, tests, and usage sites. Use dependency or source-graph evidence when available to find owners and affected paths. A long source list without authority roles, hashes, and claim mapping is not sufficient context. Source count alone does not trigger route-out; inability to rank authority does.

**Examples**

Good one-plugin coordination: a team plugin has a skill, MCP integration, security review, and managed marketplace. Separate owners return evidence, but one PLDR retains normalized identity, package linkage, final source, pending/passed stages, and recovery. This reference remains the lifecycle coordinator while service and platform operations route outward.

Bad fleet use: an agent loops through all marketplace entries, rewrites manifests and paths, uses force on collisions, and reports one aggregate success. There is no per-plugin prestate, version cohort, partial failure, or rollback. The task crossed into migration/orchestration before mutation began.

Borderline safe split: a tool reads and validates many plugin source trees under frozen creator versions, emitting per-plugin results. Failed packages are scheduled as isolated updates with individual PLDRs. Scalable read-only discovery and deliberately serialized mutation coexist.

Valid transactional exception: a centrally owned marketplace proves atomic multi-entry updates, conflict detection, audit events, staged cohorts, and rollback. Its transaction may be a legitimate larger control unit, but per-plugin source/version/runtime evidence is still retained for diagnosis and compatibility.

**Scale-readiness verification**

Before broad execution, answer:

- Can every independently failing target be named and stopped without guessing the rest?
- Can a dry run produce per-target planned changes and reject unknown identities?
- Can partial success be represented without rerunning successful targets blindly?
- Are locks/transactions, conflict behavior, idempotency, and resume semantics tested?
- Does each owner have bounded authority and returned acceptance?
- Are version/schema cohorts and compatibility assumptions explicit?
- Can a canary or synthetic target exercise failure without risking active user state?
- Is rollback tested for the same unit that mutation treats as atomic?
- Can audit evidence identify source, action, postcondition, and recovery per target?
- Are production service and security claims owned outside package lifecycle?

Use synthetic fixtures, dry runs, owner-controlled environments, and staged cohorts to simulate partial failure. Label untested failure modes. Exact batch size, rollout width, concurrency, and time budgets require local platform guarantees and measurements; no universal number is supplied here.

Repeated scale pressure can justify inventory services, policy-as-code, locks/queues, version cohorts, canaries, structured audit events, and rollback automation. Automate stable deterministic mechanics, not unresolved route, authority, or replacement decisions. Safe scaling externalizes coordination state into owned systems while preserving the one-plugin lifecycle contract at every leaf.

## Future Refresh Search Queries

No browser refresh was performed for this evolution. Every query below is a future discovery plan, not a citation or factual update. Current mechanics remain scoped to the selected local creator sources and recorded hashes until an authorized refresh opens, evaluates, and reconciles primary evidence.

Refresh local evidence first:

1. Re-read repository/organization policy and the selected creator root completely.
2. Hash workflow, schema references, scaffold, validator, update helper, and marketplace helper.
3. Inspect current command help and safe local fixture behavior where consequential.
4. Identify the exact stale, disputed, or future-version claim.
5. Browse only when authorized and when local evidence cannot answer the claim or a current public compatibility statement is required.

The seed's broad queries are retained as fallback discovery prompts, but they are not strong acceptance evidence:

| search_query_label_name | search_query_text_value | limitation_and_refinement |
| --- | --- | --- |
| `official_docs_query_phrase` | `codex plugin creator patterns official documentation best practices` | broad phrasing can return secondary summaries; add the exact field, command, component, and target version, then restrict to official product sources |
| `github_repository_query_phrase` | `codex plugin creator patterns GitHub repository examples` | examples may be stale or unrelated; search official repositories/releases and inspect versioned source rather than copying snippets |
| `release_notes_query_phrase` | `codex plugin creator patterns changelog release notes migration` | useful discovery shape but needs exact local old/new behavior and release range to locate a migration |

**Trigger-based query catalog**

| refresh_trigger | claim_to_resolve | preferred_source_class | query_variants | evidence_required_before_adoption |
| --- | --- | --- | --- | --- |
| local creator root or script hash changed | current plugin creation defaults and supported workflow | installed source, official release notes, official repository history | `Codex plugin creator scaffold destination marketplace defaults release notes`; `Codex plugin creator create_basic_plugin.py changes`; `Codex plugin creator skill changelog` | opened versioned source, changed behavior diff, safe scaffold fixture, migration impact on this reference |
| validator hash or acceptance changed | current manifest keys, formats, companions, assets, URLs, and versions | executable validator, official manifest schema/docs, official repository commit/release | `Codex plugin.json schema supported top-level fields`; `Codex validate_plugin.py manifest validation release`; `Codex plugin validator unknown field error` | minimal pass/fail fixtures under old/new validator, exact version scope, docs conflict resolution |
| top-level `hooks` conflict becomes consequential | whether and where hook declarations are supported | current validator/tool source, official plugin/hook docs, official release/migration notes | `Codex plugin.json hooks top-level field official`; `Codex plugin hook manifest schema`; `Codex plugin validator hooks migration` | target-version schema/tool result, supported representation, migration path, current-package test |
| naming behavior differs | normalization, allowed characters, length, collision semantics | scaffold source, official naming rules, official tests/releases | `Codex plugin name normalization hyphen case limit`; `Codex create plugin name collision force`; `Codex plugin manifest name constraints` | observed current normalization fixtures including collisions, versioned rule source, backward-compatibility impact |
| personal destination or marketplace default differs | source directory and personal marketplace discovery | installed creator source, official install docs, CLI help/release notes | `Codex personal plugin directory marketplace.json default`; `Codex plugin marketplace discovery personal install`; `Codex plugin creator default destination change` | current local help/source, fresh isolated creation, entry target, install identity, migration/cleanup implications |
| nondefault marketplace is required | marketplace configuration, identity, source format, add/list/install/remove behavior | official CLI docs/help, managed platform policy, official release notes | `Codex CLI plugin marketplace add list install remove`; `Codex custom plugin marketplace source configuration`; `Codex plugin marketplace name install syntax` | authorized platform owner, current command help, isolated or controlled postcondition, rollback/removal evidence |
| existing update behavior changes | authoritative source, cache identity, reinstall, fresh pickup | installed update guide/helpers, official CLI docs/releases | `Codex local plugin update cache reinstall fresh task`; `Codex plugin cachebuster update`; `Codex reinstall plugin marketplace source` | entry-to-source proof, helper diff, install listing, new-task behavior, preserved prior version |
| plugin removal or replacement is requested | current safe removal state transitions and user-data preservation | official CLI/help, platform policy, repository owner guidance | `Codex plugin uninstall remove marketplace entry source`; `Codex plugin replacement migration rollback`; `Codex plugin remove preserve user data` | complete state inventory, explicit authority, current postconditions, affected-user and recovery plan |
| skill packaging support changes | skill declaration, discovery, folder/file requirements, plugin linkage | current skill and plugin creator sources, official skill docs/releases | `Codex plugin skill directory manifest declaration official`; `Codex skills plugin packaging requirements`; `Codex plugin skill discovery release notes` | target-version component fixture, package validator, fresh-task skill visibility and bounded behavior |
| app support becomes required | app declaration, files, runtime, security, lifecycle | current creator/schema, official app docs/tool source, official releases | `Codex plugin app declaration plugin.json official`; `Codex plugin apps component requirements`; `Codex app plugin lifecycle release` | app-owner contract, schema/validator evidence, package linkage, runtime and security acceptance |
| MCP support changes | MCP declaration/configuration, transport, tool/resource exposure | current creator/schema, official MCP and Codex integration docs, protocol source | `Codex plugin mcpServers plugin.json official`; `Codex plugin MCP server declaration transport`; `Codex MCP plugin install tool discovery` | separate package-schema evidence, protocol/service evidence, permission/credential boundary, fresh-task availability |
| credential or security guidance changes | secret references, minimum permissions, remote data and failure handling | official security docs, component/service owner policy, platform release notes | `Codex plugin credentials secrets security official`; `Codex plugin MCP permissions least privilege`; `Codex plugin marketplace security policy` | accountable owner, target environment, threat/permission scope, approved secret handling, revocation/failure test |
| install succeeds but capability is absent | cache, package linkage, marketplace source, fresh task, known diagnostics | current update guide, official CLI troubleshooting/release notes, local state | `Codex plugin installed not visible fresh task`; `Codex plugin stale cache troubleshoot`; `Codex plugin marketplace wrong source diagnostics` | source-entry-install identity trace, final package validation, new-task reproduction, versioned diagnostic relevance |
| schema or CLI migration is announced | old/new fields, commands, destinations, compatibility window | official release notes, migration guide, source diff | `Codex plugin manifest migration <old-version> <new-version>`; `Codex CLI plugin command breaking change`; `Codex plugin marketplace format migration` | explicit old/new versions, migration fixture, rollback, mixed-version behavior, updated examples and checks |
| public claim in this reference needs currency | current official support or recommendation beyond local behavior | official docs, official repository/releases, then primary protocol source | `site:openai.com Codex plugin <exact claim>`; `site:github.com/openai Codex plugin <exact symbol or field>` | opened primary page/source, publisher, date/version, exact proposition, local reconciliation, bounded inference |
| community report suggests an unmodeled failure | reproduction and whether official issue/change exists | local minimal fixture, official issue/release/source; community source only as lead | `Codex plugin <exact error text> official issue`; `Codex plugin <failure condition> release notes`; `Codex plugin validator <minimal symptom>` | safe reproduction or authoritative acknowledgment, affected versions, counterexample, mitigation and recovery test |

Replace angle-bracket concepts with the exact field, command, error, version, or lifecycle state. Do not search with credential values, private paths, proprietary payloads, or user data.

**Source priority by claim**

| claim_type | first_choice | supporting_choice | insufficient_alone |
| --- | --- | --- | --- |
| what this installed creator accepts | local executable source and safe fixture | current local explanatory reference | search snippet, blog, or newer docs for an uninstalled version |
| what changed and why | official release/migration notes and versioned source history | issue/maintainer discussion with clear ownership | current behavior without old-version comparison |
| current public product support | current official product docs and official release/source | target-version local CLI/tool behavior | community example or mirrored archive |
| organization destination/publication policy | repository/organization policy and accountable owner | official platform capabilities | public docs cannot grant local authority |
| protocol or remote service behavior | primary protocol/service docs and executable integration tests | official Codex integration docs | valid plugin manifest or package install |
| real-world failure lead | reproducible local/controlled case or official acknowledgment | community report with environment detail | popularity or number of search results |

Official documentation can lag executable releases, and local installed files can lag public releases. Preserve that as a versioned conflict. Do not silently let the newer date win. Decide whether the task targets current local behavior, a planned upgrade, or broad public compatibility, then test the chosen target.

**Refresh evidence packet**

```yaml
plugin_reference_refresh:
  refresh_id: "stable identifier"
  trigger: "hash, release, error, component, policy, or claim-age event"
  target_claim: "exact old statement and its evidence boundary"
  target_environment_and_version: "current local, planned upgrade, or public compatibility"
  local_pre_refresh_anchors:
    - "policy/tool paths, hashes, help, and fixtures"
  queries_executed:
    - query: "exact search phrase"
      purpose: "claim or competing hypothesis"
  sources_opened:
    - publisher_and_url_or_path: "primary source identity"
      publication_or_release_date: "observed date"
      version_scope: "explicit or unknown"
      exact_supported_proposition: "bounded paraphrase"
      limitations: "what it does not establish"
  local_or_controlled_reproduction:
    fixture: "safe target and bytes"
    old_result: "pre-refresh observation"
    new_result: "target-version observation"
  conflicts:
    - "local, historical, public, policy, or executable disagreement"
  decision:
    adopt_adapt_defer_or_reject: "outcome and reason"
    claims_changed: ["exact bounded changes"]
    claims_left_current: ["unaffected boundaries"]
    migration_and_recovery: "when applicable"
  invalidated_evidence_and_gates:
    - "source, package, example, metric, or runtime proof to refresh"
  verifier_and_fixture_results:
    - "focused reference and creator/component tests"
  owner_and_next_refresh_trigger: "accountability"
```

Opening a search result is not enough. Inspect the primary content, verify publisher and version, avoid excessive quotation, state the exact proposition it supports, and reconcile it with current local behavior. If reproduction requires a future upgrade, classify the finding as future-version evidence and do not rewrite current operational steps until migration is chosen.

**Good, bad, and borderline refreshes**

Good: the selected validator changes and a manifest field now behaves differently. The operator freezes old/new hashes, searches official schema/release sources for that exact key and version, runs minimal old/new fixtures, updates conflict guidance and worked cases, reruns focused and creator checks, and records migration scope.

Bad: a broad query returns a recent tutorial, so personal destination, marketplace format, and hook syntax are copied wholesale. The page is for another product/version, no local fixture runs, and the reference overwrites stronger local evidence.

Borderline: an official page newer than the local creator documents a new app field, but local CLI/validator does not accept it. Record public future-version support and local current rejection separately. Adoption waits for target upgrade or explicit compatibility design.

**Stop rules**

- Stop broadening queries when an authoritative versioned source and reproducible target behavior answer the claim.
- Stop after one bounded stale-evidence refresh when access remains unavailable; hand off rather than searching indefinitely.
- Stop adoption when identity, version, publisher, or policy scope cannot be established.
- Stop transferring a cross-ecosystem example when target syntax/security/authority lacks evidence.
- Stop changing unrelated claims; refresh dependency boundaries, not the entire reference by association.

Consequential findings feed source maps, hashes, conflict fixtures, migration cases, query vocabulary, invalidation rules, and owner policy. Automated monitoring may detect changes in owned primary sources, but a human or accountable workflow must review claim impact and executable evidence before adoption. Retire queries that no longer map to a live claim and refine recurring searches around exact owners and drift triggers.

## Evidence Boundary Notes

Evidence provenance determines what a claim may mean, where it applies, and what invalidates it. It is not a decorative label. Use the narrowest evidence class that supports the proposition, then state important nonproof and uncertainty.

The three seed labels remain the top-level vocabulary:

- `local_corpus_sourced_fact`: a statement tied to a named local source, owner policy, archive file, or observed local state. Specify which subtype below; local files do not all have equal authority.
- `external_research_sourced_fact`: a statement tied to opened public primary evidence with publisher, URL, date/version scope, and exact supported proposition. This evolution performed no browsing, so no new claim in this file has this status.
- `combined_evidence_inference_note`: a recommendation synthesized from two or more bounded facts plus engineering judgment. Name component facts, alternative, counter-risk, and verification; do not phrase synthesis as a direct quotation or universal rule.

**Local evidence subtypes**

| evidence_class | definition | appropriate_claim | cannot_prove | invalidation_trigger |
| --- | --- | --- | --- | --- |
| `current_executable_local_fact` | observed source or safe execution from the selected current creator root | what this scaffold emits, validator accepts/rejects, or helper transforms under recorded hashes | product truth, broad platform support, organization approval, component usefulness, remote readiness | creator root/hash, target input, runtime/tool version, or observed behavior changes |
| `current_explanatory_local_fact` | current selected workflow or reference prose | intended sequence, field meaning, cautions, and owner guidance | executable acceptance when prose conflicts with tool; future compatibility | file hash, selected root, or explicit project override changes |
| `historical_archive_fact` | complete archived source tied to its snapshot | prior defaults, lineage, earlier examples, and persistent-invariant hypotheses | current mechanics or current public support without reconfirmation | target shifts from historical comparison; no automatic expiry, but operational use requires current proof |
| `project_or_owner_policy_fact` | explicit repository/organization policy or accountable owner decision | destination authority, review, publication, credential, replacement, and retention requirements | package validity or technical runtime behavior unless separately tested | policy revision, owner withdrawal, scope/audience change |
| `observed_package_state_fact` | inspected source, manifest, diff, entry, installed listing, or fresh-task behavior | exact state under recorded identity/version/time anchors | desired semantics, another environment, future state, or unobserved component | package bytes, entry, cache/install, task, environment, or remote state changes |
| `generated_fixture_fact` | output from isolated scaffold/validator/helper/component fixture | deterministic behavior for named tool/input and regression comparison | active user state, governance, or full lifecycle behavior | fixture, tool, environment, or expected contract changes |
| `owner_attestation_fact` | accountable external owner reports approval or managed-stage acceptance | policy/permission scope and state explicitly covered by the attestation | hidden technical details, broader service health, or future acceptance | conditions, version, owner, policy, or target state changes |

**External evidence states**

| evidence_state | use | required_boundary |
| --- | --- | --- |
| `opened_primary_external_fact` | supports current public product/protocol/release claim after authorized research | publisher, direct source, publication/release date, version, exact proposition, limitations, and local reconciliation |
| `opened_secondary_external_lead` | supplies examples, reported failures, or discovery context | label as lead; seek primary or reproducible evidence before normative guidance |
| `unrefreshed_external_pointer` | preserves a URL or search query for future work | no current factual support; do not cite as if opened or current |
| `search_result_snippet` | discovery navigation only | never sufficient as accepted evidence because context, version, and publisher meaning may be absent |

All external URLs and query families in this evolution are either previously mapped source facts or unrefreshed pointers as explicitly labeled. The future-query section is not evidence that any searched behavior exists.

**Claim card**

Use this structure for consequential, disputed, quantitative, shared-state, security, runtime, migration, performance, or recovery guidance:

```yaml
evidence_bounded_claim:
  claim_id: "stable identifier"
  proposition: "one precise statement"
  target_scope: "workspace, creator version, package, platform, audience, and lifecycle stage"
  evidence:
    - class: "local subtype, external fact, owner policy, or observation"
      source_identity: "path/hash, URL/date/version, owner, or state anchor"
      supported_proposition: "exact contribution"
      independence_note: "shared origin or genuinely separate evidence"
  combined_inference_if_any:
    reasoning_summary: "explicit high-level decision rationale"
    alternative: "material competing interpretation or route"
    counter_risk: "how recommendation could be wrong"
    verification: "test, review, owner, or postcondition"
  does_not_prove:
    - "important nearby claim outside evidence"
  confidence: "high, moderate, low, or pending with reason"
  invalidation_triggers:
    - "source, bytes, policy, entry, install, task, or external change"
  owner_and_refresh_action: "who resolves drift"
```

Confidence attaches to this proposition and scope, not to the whole reference. An executable local fact can be high confidence for this installed version while broader product compatibility remains pending. A repeated historical invariant can raise synthesis confidence but cannot replace target-version acceptance.

**Precedence and conflict rules**

1. Explicit project/owner policy governs authority and destination, but cannot make an invalid package valid.
2. Selected current executable behavior governs acceptance under that local creator contract.
3. Current explanatory material guides intent; preserve conflicts with executable behavior and scope the resolution.
4. Observed lifecycle state governs whether this exact source/entry/install/task postcondition currently exists.
5. Historical archive informs lineage and migration hypotheses, not present mechanics by default.
6. Opened primary external evidence governs its public/versioned proposition after reconciliation; it does not silently override a deliberately older local target.
7. Secondary/community material and search output generate hypotheses, not normative acceptance.
8. Combined inference may select a default only when component facts, alternatives, counter-risk, and verification are explicit.

When sources disagree, first ask whether they target different versions, layers, or owners. A validator and documentation sample can both be accurately recorded even when one rejects the other's example. A current public schema and older installed creator can both be true for their targets. Resolve the operational decision by choosing the intended target and testing it; do not flatten disagreement into one timeless statement.

**Category-error examples**

Good local claim: "Under validator `ebda...d3228` in the selected installed creator root, the tested top-level `hooks` key is rejected." This is reproducible current executable evidence scoped to one contract.

Bad broad claim: "Codex plugins never support hooks." The local result does not establish every version or supported representation. The statement crosses from local acceptance to universal product support.

Good combined inference: the installed creator defaults new marketplace-backed work to a personal source/marketplace, the request explicitly asks for a personal installable plugin, and no collision exists; therefore use the personal minimal path, with destination inspection and fresh-task verification. Policy or an existing shared identity reverses the default.

Bad semantic promotion: "The plugin is production-ready because `validate_plugin.py` passed." The validator supports structural acceptance only. Metadata truth, component behavior, marketplace source, runtime, security, reliability, and operations require separate evidence.

Good historical use: the archive shows earlier repository-oriented and bracketed-metadata behavior; the current scaffold differs. The reference describes evolution and uses current behavior for operations. It does not call the archive wrong merely because defaults changed.

Borderline version conflict: newer official documentation, if later opened, describes an app field that the current installed validator rejects. Record future/public and local/current facts separately. The owner chooses upgrade/migration, compatibility design, or current omission; neither source is silently discarded.

Bad authority inference: an agent can write a team marketplace, so it declares itself authorized. Access is a technical state; publication authority comes from policy or accountable owner.

Good runtime boundary: a fresh task observes one skill after installing the resolved source. The claim is bounded to that plugin/version/component/environment. It does not establish all components, all users, remote service SLOs, or future pickup.

**Evidence depth by consequence**

- Low-consequence read-only explanation: source path/class and concise uncertainty may suffice.
- Local source scaffold: selected creator, destination/identity, diff, validator, and component evidence are required.
- Marketplace/install claim: add entry source, action, independent installed postcondition, and fresh task when invocation is claimed.
- Shared, replacement, removal, credential, security, or remote effect: add policy/owner, preservation, failure path, recovery, and returned external acceptance.
- Quantitative performance/reliability claim: add measurement contract, cohort, raw/aggregate source, uncertainty, and balancing correctness guards.
- Cross-version migration: add old/new anchors, fixture, compatibility, staged adoption, rollback, and mixed-version boundary.

Evidence effort scales with consequence and change rate. A rhetorically strong sentence does not deserve more proof than a quiet one; the state it can change does.

**Focused evidence-boundary audit**

1. Inventory normative, disputed, quantitative, security, shared-state, runtime, performance, reliability, and recovery claims.
2. Assign each the narrowest source class and target scope.
3. Verify source identity, authority, hash/version/date, and exact supported proposition.
4. Check whether purportedly independent sources copied the same sample or upstream claim.
5. Reproduce executable claims with safe fixtures where possible.
6. For synthesis, state component facts, alternative, counter-risk, and verification.
7. Add `does_not_prove` where a likely adjacent overclaim exists.
8. Mark stale/pending evidence and remove unsupported operational conclusions.
9. Ask whether deleting an evidence row changes the recommendation; ornamental rows should not inflate confidence.
10. Rerun the focused reference verifier and affected creator/component fixtures after boundary edits.

Do not map every sentence if doing so adds no decision value. Prioritize claims that can cause file/platform mutation, exposure, security impact, destructive recovery, or asserted measurable outcome.

**Known in this evolution**

- The current and seed reference originally shared the frozen seed content and exact 26 heading structure before evolution.
- The selected installed creator files were read locally and hashed; their current workflow, scaffold, validator, update, and marketplace helper behavior grounds operational guidance in this workspace.
- Archive creator sources were read and hashed as historical lineage.
- The current manifest illustration and current validator/instructions conflict on the tested top-level `hooks` field; local acceptance follows the recorded executable contract.
- Current local defaults differ from the archive in personal marketplace-backed destination and generated metadata behavior.
- The question-packet and reference-evolution gates are local executable requirements.
- No browsing was performed for this assignment; future queries and public URLs were not refreshed into new external facts.

**Uncertain or target-dependent**

- Future Codex CLI, plugin schema, marketplace behavior, install/remove syntax, component support, and public guidance.
- Repository, team, organization, or managed-platform policy not supplied by an accountable source.
- Remote service health, credentials, permissions, security acceptance, latency, reliability, and production readiness.
- Universal performance, workload, retry, batch, or percentile thresholds; these require local measurement or platform policy.
- Whether another environment pins a different coherent creator root or supports a different manifest representation.
- User preference where several packaging routes satisfy the same constraints.

Treat these as refresh, owner, migration, or judgment boundaries rather than gaps to fill with confident prose.

Maintain provenance as a dependency system. Source-anchor changes should invalidate only dependent claims and fixtures. Consequential new evidence should update the source map, worked cases, verifier/creator fixtures, migration guidance, and PLDR fields together. Automate owned hash/change detection where useful, but require human semantic review before changing a recommendation. Remove obsolete claims and evidence rows rather than carrying them as ceremonial history.
