# Github Context Capture Patterns

**Decision supported.** This section helps decide whether to run a bounded repository survey or focused artifact trace and how to turn separate GitHub surfaces into a recoverable, source-linked digest. The seed title names context capture but does not define repository context as separate content, chronology, and relationship surfaces or explain the preflight-scope-collect-preserve-synthesize workflow.

**Recommended default and causal basis.** Confirm GHCLI availability, active authentication, host, repository, and capabilities; choose Repo Survey or Artifact Trace with an explicit scope; select the canonical REST, GraphQL, or high-level command per surface; save raw JSON; then render a digest that names chronology, links, gaps, and limits. GitHub history is distributed across commits, PRs, issues, review threads, commit comments, timeline events, and Discussions, so a single command or flattened transcript can omit the evidence that explains a change.

**Operating conditions and assumptions.** This default works for onboarding, design archaeology, regression tracing, incident review, and commit-to-decision reconstruction when repository access and scope are known. Assume authorized read access only, never expose credentials, and do not claim complete history beyond the recorded scope, permissions, cursors, and capture time.

**Failure boundary and alternatives.** It becomes blocked by broken authentication or unknown repository identity and becomes misleading when permissions, pagination caps, disabled Discussions, or nested-reply truncation are hidden. Bounded alternatives and recoveries: Narrow to one PR, issue, commit, or discussion; run a bounded survey before widening; synthesize from previously saved raw JSON; report inaccessible surfaces; or ask the user to restore authentication.

**Counterexample, gotchas, and operational comparison.** One-command mythology, search-as-archive, comment flattening, unlimited pagination, repo-wide timeline crawling, mutation by default, and HTML scraping are the dominant hazards. Good: link a commit to its PR, collect issue comments and review comments separately, preserve raw JSON, and cite URLs. Bad: summarize `gh pr view` as the entire history. Borderline: a bounded survey is useful if its page cap and omitted surfaces are explicit.

**Verification, evidence, and uncertainty.** Check preflight output, repository and host, selected mode and time range, queried surfaces, endpoint and pagination manifest, raw paths, chronology, source URLs, coverage gaps, and absence of mutations. The local corpus directly specifies the three modes, preflight checks, scope choices, command biases, conversation separation, raw preservation, digest order, and read-only default. The right page cap, date window, and surface breadth depend on repository size, user intent, permissions, and rate limits.

**Second-order consequence.** Repository context capture is an evidence-preserving join across heterogeneous surfaces, not a search or summarization task; recoverability matters because synthesis can change without recollecting data.

**Revision decision.** Turn the title section into a mode-selection and collection state machine with bounded, blocked, and raw-artifact reuse branches.

**Retained seed evidence.** The original title remains while the evolved opening supplies the missing multi-surface and recoverability contract. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

## Source Evidence Mapping Table

**Decision supported.** This section helps decide which source governs capture behavior, which local references answer narrower questions, and which public pointers require relevance and freshness checks. The seed lists five local files and three public URLs but does not explain the local files' progressive roles or that the external Actions, MCP, and workflow-reuse pages are adjacent to, rather than primary evidence for, repository-history capture.

**Recommended default and causal basis.** Use SKILL.md as the operational authority, the thesis for scope and rationale, the GHCLI map for command selection, the Discussions playbook only when Discussions are in scope, and the output contract before digest writing; treat public rows as bounded external pointers. The local context strategy is explicitly progressive, and direct command/API guidance is more relevant to capture fidelity than generic automation material.

**Operating conditions and assumptions.** This map works when each claim records source role, retrieval state, date, supported surface, and whether the source changed collection or synthesis. No new browsing occurred, and public pointers cannot override local read-only, bounded-first, or provenance requirements.

**Failure boundary and alternatives.** It fails when all local files are loaded reflexively, three public URLs are treated as current proof, or workflow automation guidance is used to justify API completeness. Bounded alternatives and recoveries: Load only the governing skill for orientation, add one local reference on demand, use the thesis's recorded primary-doc evidence for provenance, or preserve uncertainty until authorized freshness checks occur.

**Counterexample, gotchas, and operational comparison.** Adjacent-source authority, stale endpoint assumptions, duplicate guidance, scaffold-as-policy confusion, and counting source rows as independent corroboration can distort confidence. Good: use the surface map for PR review endpoints and the GraphQL reference for a discussion. Bad: cite reusable Actions workflows as proof that issue comments include reviews. Borderline: use the MCP repository only to compare an explicitly named automation surface.

**Verification, evidence, and uncertainty.** Check all five local hashes and headings, progressive load triggers, public retrieval state, source-to-claim fit, the thesis's 2026-04-08 evidence date, and invalidation conditions. All five local files were read completely and their distinct roles and load order are direct corpus facts. No external URL was refreshed in this pass, so current contents and compatibility beyond the archived evidence date remain unknown.

**Second-order consequence.** A source map should reduce collection error, not maximize references; each added source must resolve a specific uncertainty about scope, endpoint, pagination, or output.

**Revision decision.** Retain all rows while adding progressive-loading, relevance, retrieval-state, evidence-date, and invalidation interpretation.

**Retained seed evidence.** Every seed source row remains for provenance, with authority and current-evidence limits made explicit. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| source_location_path_key | source_category_artifact_type | source_authority_confidence_level | source_usage_synthesis_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202603/capture-github-repo-context/SKILL.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/codex-skills-202603/capture-github-repo-context/references/discussions-graphql-patterns.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/codex-skills-202603/capture-github-repo-context/references/ghcli-surface-map.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/codex-skills-202603/capture-github-repo-context/references/github-repo-context-thesis.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/codex-skills-202603/capture-github-repo-context/references/output-contract.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| https://docs.github.com/actions | external_research_source_material | external_research_sourced_fact | primary workflow and automation documentation |
| https://github.com/github/github-mcp-server | external_research_source_material | external_research_sourced_fact | GitHub repository automation through MCP |
| https://docs.github.com/en/actions/concepts/workflows-and-actions/reusing-workflow-configurations | external_research_source_material | external_research_sourced_fact | workflow reuse and governance guidance |

## Pattern Scoreboard Ranking Table

**Decision supported.** This section helps decide how to prioritize capture controls without turning inherited scores into unsupported completeness or reliability claims. The seed assigns 95, 91, and 88 to generic source, evidence, and verification controls without a rubric or any representation of scope selection, surface separation, canonical endpoints, pagination, or raw recoverability.

**Recommended default and causal basis.** Treat the scores as uncalibrated metadata and order controls causally: preflight, scope, mode, surface selection, bounded pagination, raw preservation, provenance-rich synthesis, then verification. A well-sourced digest can still be wrong if it queried the wrong surface or hid a page cap, while later verification cannot recover data that was never collected.

**Operating conditions and assumptions.** The ordered controls work when reviewers need a compact dependency chain and understand that several gates are jointly required. Do not reinterpret seed numbers as probabilities, service levels, coverage percentages, or user preferences.

**Failure boundary and alternatives.** It fails when 95 implies percentage completeness, when a high row bypasses auth or scope, or when verification is reduced to Markdown structure. Bounded alternatives and recoveries: Use an unscored capture dependency graph or a calibrated matrix for scope fit, surface coverage, pagination, separation, provenance, recoverability, and digest usefulness.

**Counterexample, gotchas, and operational comparison.** False precision, score anchoring, independent ranking of dependent controls, and preserving inherited values because they sound authoritative are the main risks. Good: keep 95 as seed metadata and still reject an uncapped or unmanifested crawl. Bad: claim 95 percent repository coverage. Borderline: score capture quality only after publishing a corpus, denominator, reviewer rules, and uncertainty.

**Verification, evidence, and uncertainty.** Require derivation, dimensions, sample, reviewer calibration, sensitivity, and decision effect for each score; otherwise audit only the workflow dependencies. The values and row names are direct seed facts; their lack of calibration and the workflow ordering are explicit evidence boundary conclusions. The corpus supplies no benchmark connecting score differences to capture completeness, chronology accuracy, or user usefulness.

**Second-order consequence.** Capture reliability is limited by the earliest missing surface or scope decision, so downstream polish cannot compensate for upstream omission.

**Revision decision.** Preserve and qualify the rows while linking each pattern to the actual capture state machine.

**Retained seed evidence.** The original scoreboard stays visible with unsupported precision explicitly bounded. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| pattern_identifier_stable_key | pattern_score_numeric_value | pattern_tier_adoption_level | pattern_failure_prevention_target |
| --- | ---: | --- | --- |
| `github_context_capture_patterns` | 95 | default_adoption_pattern_tier | Source Map First: Load local github context material before synthesizing capture patterns recommendations. |
| `github_context_capture_patterns` | 91 | default_adoption_pattern_tier | Evidence Boundary Split: Separate local facts, external facts, and inference before giving agent instructions. |
| `github_context_capture_patterns` | 88 | default_adoption_pattern_tier | Verification Gate Coupling: Attach each recommendation to at least one command, checklist, or review gate. |

## Idiomatic Thesis Synthesis Statement

**Decision supported.** This section helps decide what compact thesis should govern GitHub history capture from scope choice through digest delivery. The seed says local first, public second, and verification-backed decisions but omits the corpus thesis that repository context is multi-surface, chronological, relational, read-only, bounded-first, and recoverable from raw artifacts.

**Recommended default and causal basis.** Use GHCLI and official APIs as the primary read-only collection layer; scope before collecting; preserve conversation surfaces separately; use canonical list/detail endpoints and GraphQL where required; save raw JSON; and synthesize a source-linked chronology with explicit gaps. The value comes from normalization plus synthesis across content, chronology, and relationships, not from raw volume or a single convenient command.

**Operating conditions and assumptions.** This thesis works for one repository and a defined survey or artifact trace whose selected surfaces can be queried under current permissions. Keep the task repo-scoped unless explicitly expanded and never imply that inaccessible or uncaptured history does not exist.

**Failure boundary and alternatives.** It fails when used for mutation, browser scraping, unbounded organization-wide intelligence, or claims of perfect conversation history despite incomplete access or pagination. Bounded alternatives and recoveries: Narrow the repository or time window, trace one artifact, reuse a previous raw capture, split independent surfaces, or defer inaccessible evidence.

**Counterexample, gotchas, and operational comparison.** Search shortcuts, merged comment streams, missing commit-to-PR links, timeline events mistaken for discussion, and a digest without raw paths can erase explanatory context. Good: collect a bounded repo survey, then focus on the PR and issue that explain a regression. Bad: dump search results. Borderline: a quick `gh pr view` is sufficient only for a narrow focused question with coverage limits.

**Verification, evidence, and uncertainty.** Trace each digest claim to a raw payload and URL, check chronology ordering, surface type, relationships, capture scope, page caps, permissions, and gaps. The multi-surface core thesis, read-only bias, bounded-first approach, raw recoverability, and digest contract are direct local statements. Exhaustiveness remains aspirational where GitHub permissions, rate limits, API behavior, or nested pagination constrain capture.

**Second-order consequence.** A digest is a reproducible interpretation layer over preserved evidence; separating collection from synthesis allows later questions to be answered without repeating network work.

**Revision decision.** Replace generic source ordering with a scope-surface-raw-digest thesis and explicit non-goals.

**Retained seed evidence.** The three evidence labels remain under a fuller repository-context thesis. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`local_corpus_sourced_fact`: The local row for `github_context_capture_patterns` contains 5 source path(s), which should be treated as the first retrieval surface for this theme.
`external_research_sourced_fact`: The external source map provides public documentation, repository, or ecosystem analogues where available.
`combined_evidence_inference_note`: Reliable use of Github Context Capture Patterns comes from loading the local corpus first, checking public ecosystem guidance second, and converting both into verification-backed agent decisions.

## Local Corpus Source Map

**Decision supported.** This section helps decide which local source to load at each capture stage and when optional detail earns its context cost. The seed provides correct local paths and headings but presents them as a flat map instead of the explicit five-step progressive context strategy.

**Recommended default and causal basis.** Load SKILL.md first, the thesis for scope and exclusions, the GHCLI map for endpoint choice, the Discussions patterns only when that capability is in scope, and the output contract immediately before digest synthesis. Progressive loading keeps operational rules visible while delaying endpoint detail and format constraints until the task has selected a mode and surface.

**Operating conditions and assumptions.** This hierarchy works when the repository, scope, and requested artifact are known before deep command selection. Archived local files define this corpus but remain subordinate to current user permissions and platform constraints.

**Failure boundary and alternatives.** It fails when every file is loaded for a small trace, when the output template anchors collection prematurely, or when Discussions detail is skipped despite nested replies being in scope. Bounded alternatives and recoveries: Use only SKILL.md for a quick focused read, add one reference for a diagnosed need, or create a narrow capture manifest from the relevant rules.

**Counterexample, gotchas, and operational comparison.** Flat heading maps hide rule ownership, optional references can become mandatory ceremony, and loading output constraints late can omit raw paths or coverage notes. Good: load the surface map for a commit-to-PR trace and skip Discussions. Bad: load all five before confirming the repo. Borderline: load the output contract early when the user already supplied a fixed digest shape.

**Verification, evidence, and uncertainty.** Record hashes, load order, trigger for each optional file, guidance applied, context cost, and whether the source changed endpoint choice or output. The exact five-step order and file triggers are direct statements in SKILL.md. The optimal context cost and timing vary with task complexity and already-known GitHub surfaces.

**Second-order consequence.** Progressive disclosure mirrors capture itself: start with orientation, then add only the surface detail needed to close a named coverage gap.

**Revision decision.** Convert the flat source map into a triggered loading protocol with stop and conflict rules.

**Retained seed evidence.** All five rows remain while their governing and on-demand roles become operational. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| local_source_filepath_value | local_source_title_text | local_source_heading_signals | local_source_usage_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202603/capture-github-repo-context/SKILL.md | capture-github-repo-context | Capture GitHub Repo Context; Goal; Choose The Right Mode; Workflow; Command Selection Guide; Use The Bundled Scripts | skill entrypoint or reusable agent prompt |
| agents-used-monthly-archive/codex-skills-202603/capture-github-repo-context/references/discussions-graphql-patterns.md | Discussions GraphQL Patterns | Discussions GraphQL Patterns; Table Of Contents; Why Discussions Need GraphQL; Repo-Wide Discussion Index; Focused Discussion Thread; Limits And Caveats | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/codex-skills-202603/capture-github-repo-context/references/ghcli-surface-map.md | GHCLI Surface Map | GHCLI Surface Map; Table Of Contents; Command Choice Rules; Surface Matrix; Common Traps; Trap 1: Treating issue comments as all PR discussion | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/codex-skills-202603/capture-github-repo-context/references/github-repo-context-thesis.md | GitHub Repo Context Thesis | GitHub Repo Context Thesis; Table Of Contents; Core Thesis; Why This Skill Matters; What Counts As Repository Context; Content surfaces | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/codex-skills-202603/capture-github-repo-context/references/output-contract.md | Output Contract | Output Contract; Table Of Contents; Digest Goals; Required Sections; Coverage Notes; Raw Artifact Expectations | reference detail file for deeper pattern evidence |

## External Research Source Map

**Decision supported.** This section helps decide when external research should refresh capture behavior and which source classes are authoritative for a named GitHub claim. The seed lists GitHub Actions, the GitHub MCP server, and reusable workflow documentation, which may constrain automation but do not directly establish REST, GraphQL, comment-surface, or pagination semantics.

**Recommended default and causal basis.** For freshness-sensitive endpoint or CLI claims, consult current official GHCLI manuals, REST references, and GraphQL documentation; use the seed external rows only for explicitly scoped automation, MCP, or workflow-governance questions. Official status alone is insufficient when the topic is adjacent; evidence must match the exact surface, version, and claim.

**Operating conditions and assumptions.** This approach works when browsing is authorized, the disputed claim is named, and retrieved material includes a date, locator, and applicability check. No browsing occurred in this evolution, so external rows are existing pointers, not newly verified facts.

**Failure boundary and alternatives.** It fails when no-browse constraints apply, when an unfetched URL is treated as current, or when Actions documentation is used to infer discussion pagination. Bounded alternatives and recoveries: Use archived local evidence with its date, inspect `gh --help` or API responses when authorized, narrow the claim, or state the freshness limitation.

**Counterexample, gotchas, and operational comparison.** Link drift, endpoint previews, version differences, official-source halo, and post-hoc citation collection can make a stale implementation look verified. Good: retrieve current `gh api` pagination docs for a changed command. Bad: use the MCP repository to prove REST completeness. Borderline: compare MCP coverage only when the user asks about replacing GHCLI collection.

**Verification, evidence, and uncertainty.** Capture authorization, URL, revision date, exact claim, source class, locator, contradiction, live behavior check, and resulting guidance change. The archived thesis lists direct primary documentation and records an evidence check date of 2026-04-08. The three seed URLs were not opened now, and current GitHub CLI or API behavior may have changed.

**Second-order consequence.** External refresh should be endpoint-first and claim-first; generic ecosystem research can widen options but cannot establish capture completeness.

**Revision decision.** Preserve the rows with relevance, retrieval, freshness, and claim-scope constraints, and point future refresh toward direct CLI/API sources.

**Retained seed evidence.** The public rows remain discovery surfaces with their adjacency and no-browse status explicit. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| external_source_url_value | external_source_name_text | external_source_usage_role | evidence_boundary_label_value |
| --- | --- | --- | --- |
| https://docs.github.com/actions | GitHub Actions documentation | primary workflow and automation documentation | external_research_sourced_fact |
| https://github.com/github/github-mcp-server | GitHub MCP server | GitHub repository automation through MCP | external_research_sourced_fact |
| https://docs.github.com/en/actions/concepts/workflows-and-actions/reusing-workflow-configurations | Reusable workflow docs | workflow reuse and governance guidance | external_research_sourced_fact |

## Anti Pattern Registry Table

**Decision supported.** This section helps decide which failures must block or revise a GitHub context digest before it is trusted. The seed captures generic context-free, unsourced, and unverified guidance but omits the local corpus's concrete capture failures across mode, surface, pagination, safety, and synthesis.

**Recommended default and causal basis.** Detect missing preflight, undefined scope, search-as-archive, one-command mythology, flattened comment types, issue/PR endpoint confusion, assumed Discussions support, hidden page caps, nested-reply truncation, browser scraping, mutation, lost raw data, and unsupported completeness claims. Each failure either omits a distinct evidence surface, destroys provenance, or makes the collection impossible to reproduce.

**Operating conditions and assumptions.** The registry works when every failure has an observable signal, containment action, owner, and rerun point. Judge explicit collection evidence and outputs only, never infer hidden completeness from a polished digest.

**Failure boundary and alternatives.** It fails as a label checklist when reviewers cannot inspect the endpoint manifest, cursors, raw payloads, or digest links. Bounded alternatives and recoveries: Use preflight assertions, surface-specific fixtures, pagination boundary tests, read-only command audits, raw-to-digest replay, and negative capability cases.

**Counterexample, gotchas, and operational comparison.** PR issue comments can look complete while review comments are absent, repo-wide issues include PRs, and top-level GraphQL pagination can hide truncated nested replies. Good: report that 100 nested replies may truncate and schedule a focused follow-up. Bad: flatten all comments and claim full history. Borderline: search can seed artifact IDs if canonical endpoints perform the actual capture.

**Verification, evidence, and uncertainty.** Test broken auth, private access, page-cap exhaustion, issue/PR filtering, comment separation, disabled Discussions, nested reply overflow, missing raw files, and attempted mutation. Every listed capture-specific failure is directly described in the governing skill or surface references. Operational frequency and severity depend on repository topology, permissions, and API evolution.

**Second-order consequence.** The most misleading failure is silent partial success: plausible chronology can survive even when the decisive conversation surface was never queried.

**Revision decision.** Expand the registry into preflight, scope, surface, pagination, safety, recoverability, and synthesis failure classes.

**Retained seed evidence.** The three generic seed rows remain as umbrella categories beneath concrete capture diagnostics. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| anti_pattern_failure_name | failure_cause_risk_reason | safer_default_replacement_pattern | detection_signal_review_method |
| --- | --- | --- | --- |
| context_free_summary_output | agent skips local corpus and produces generic advice | source_map_first_synthesis | verify every listed local path appears in the generated file |
| unsourced_recommendation_claims | guidance appears authoritative without source boundary | evidence_boundary_split_pattern | check for local, external, and inference labels |
| unverified_agent_instruction | recommendation cannot be checked by command or review gate | verification_gate_coupling | require concrete gate in generated reference |

## Verification Gate Command Set

**Decision supported.** This section helps decide what verifies both the evolved reference and a real GitHub context capture. The seed offers one repository-generation command, which cannot prove GHCLI auth, repository identity, surface coverage, pagination, comment separation, raw persistence, or digest provenance.

**Recommended default and causal basis.** Layer the focused reference verifier with GHCLI preflight, capability checks, endpoint and pagination manifests, raw artifact validation, surface-separation assertions, digest replay, URL checks, and a no-mutation audit. Document structure, collection completeness, and synthesis correctness are separate claims with different evidence.

**Operating conditions and assumptions.** The gate stack works when a live or fixture repository exposes the selected surfaces and capture scripts produce deterministic raw artifacts. The retained archive command proves only generated-reference properties and cannot validate GitHub data.

**Failure boundary and alternatives.** It fails when one PASS substitutes for API coverage, when rate-limit or permission errors are ignored, or when a digest is reviewed without raw payloads. Bounded alternatives and recoveries: Use recorded fixtures, a public test repository, focused endpoint probes, manual URL review, or explicitly mark an unverified surface.

**Counterexample, gotchas, and operational comparison.** Wrong host, stale auth, shell quoting, shared-suite noise, capped pages, GraphQL nested connections, and changed API schemas can produce false confidence. Good: validate a public repo survey, a focused PR trace, digest rendering, and disabled-Discussions degradation. Bad: run only the Markdown verifier. Borderline: fixture tests are sufficient for formatting but not live permissions or API drift.

**Verification, evidence, and uncertainty.** Record command, exit status, host, repo, capability response, scope, endpoints, pages, cursors, raw file hashes, digest path, source links, limits, and mutation count. The thesis directly specifies minimum live validation, and the skill defines preflight, scripts, modes, and output evidence. A single live repository cannot exercise every permission, pagination, or conversation topology.

**Second-order consequence.** Verification should replay synthesis from saved raw JSON; that proves recoverability and separates renderer defects from collection defects.

**Revision decision.** Keep the seed command as one layer and add live/fixture collection, surface, pagination, raw, digest, and safety gates.

**Retained seed evidence.** The original command remains with a precise proof boundary. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`verification_gate_command_set`: Run the repository verifier after editing this file.

```bash
python3 agents-used-monthly-archive/idiomatic-references-202606/tools/verify_reference_generation.py --stage final
```

## Agent Usage Decision Guide

**Decision supported.** This section helps decide when to run Repo Survey, Artifact Trace, Digest Mode, or stop before collection. The seed triggers generically on theme or paths and omits the three explicit modes, preflight stop, bounded-first rule, and read-only scope.

**Recommended default and causal basis.** Use Repo Survey for broad evolution, Artifact Trace for one commit, PR, issue, or discussion, and Digest Mode to render a reusable summary from captured data; always preflight and choose scope before querying. Mode selection prevents a narrow question from causing an expensive crawl and prevents a broad question from relying on a single artifact view.

**Operating conditions and assumptions.** The guide works when the user goal identifies breadth, artifact, date range, and expected output. Do not mutate GitHub state or expand collection breadth without explicit user authorization.

**Failure boundary and alternatives.** It is blocked by failed auth, unknown host or repo, missing permissions, or a mutation request that has not been explicitly authorized. Bounded alternatives and recoveries: Ask one scope question, start with a bounded survey, use a focused high-level view, synthesize existing raw artifacts, or route a write request to an authorized mutation workflow.

**Counterexample, gotchas, and operational comparison.** Over-collecting, unlimited pages, assuming Discussions, treating search as exhaustive, and rendering before surface capture finishes are common routing errors. Good: Artifact Trace for why commit `abc` exists. Bad: repo-wide crawl for one PR question. Borderline: start with a bounded survey and widen only after its gaps matter.

**Verification, evidence, and uncertainty.** Check mode, user objective, repository and host, auth, date/page bounds, selected surfaces, expected artifact, read-only status, and widening authorization. The three modes, preflight sequence, scope choices, and bounded-first rule are direct local requirements. Some requests need a survey followed by one or more traces, and the crossover depends on repository size and user intent.

**Second-order consequence.** Mode choice is the first context budget: it determines which evidence can enter the digest and which omissions must be declared.

**Revision decision.** Replace generic bullets with preflight plus Survey, Trace, Digest, widen, and blocked branches.

**Retained seed evidence.** The seed trigger remains while the actual mode decision governs use. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`agent_usage_decision_guide`: Use this reference when a task mentions this theme, one of the listed local source paths, or a nearby technology/workflow surface.

- Start with the local corpus source map.
- Prefer patterns with explicit verification gates.
- Treat external sources as freshness and ecosystem checks, not replacements for local repo conventions.
- Preserve the evidence boundary labels when reusing recommendations.

## User Journey Scenario

**Decision supported.** This section helps decide how a user obtains an auditable explanation of what changed, who discussed it, and where a decision was made. The seed frames generic context selection and delegation but never shows a user moving from a historical question through preflight, scope, multi-surface capture, chronology, and source-linked digest.

**Recommended default and causal basis.** Clarify the historical question, confirm repo and host, preflight auth and capabilities, choose survey or trace, bound date/pages, select surfaces, collect and save raw JSON, link relationships, render chronology and key conversations, then disclose gaps and raw paths. A visible capture journey lets the user control cost and understand which omissions limit the explanation.

**Operating conditions and assumptions.** The journey works when the user can identify the repository and either a broad period or focal artifact. Never reveal tokens or private content outside the user's authorized repository access and requested output.

**Failure boundary and alternatives.** It fails when credentials are unavailable, scope remains unbounded, or inaccessible surfaces are treated as empty. Bounded alternatives and recoveries: Pause for auth, narrow to a public or accessible artifact, reuse a prior capture, provide a conditional digest, or list the evidence needed next.

**Counterexample, gotchas, and operational comparison.** User fatigue from repeated scope questions, opaque page caps, chronology without conversation type, and digests without clickable origins can reduce trust. Good: trace a regression commit to its PR, reviews, linked issue, and timeline, then state that Discussions were disabled. Bad: dump commit messages. Borderline: a bounded survey answers onboarding needs if the cutoff is prominent.

**Verification, evidence, and uncertainty.** An independent reviewer should reconstruct the question, scope, mode, surfaces, bounds, chronology, links, decisive thread, gaps, and raw artifact locations. These states follow directly from the workflow and output contract. The number of follow-up traces needed after a survey depends on where explanatory density appears.

**Second-order consequence.** The user journey should narrow from repository breadth to decision-bearing threads, then preserve enough raw evidence to widen again without recollection.

**Revision decision.** Expand the scenario into preflight, scope, capture, synthesis, gap, and reuse states.

**Retained seed evidence.** The original user need for executable context remains but is grounded in a concrete GitHub history journey. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Role based opening scenario: The agent-system designer is starting from a task that needs context selection, tool use, delegation, and verification and needs a reference that turns source evidence into an executable next step.
Primary user starting state: The user has a `github_context_capture_patterns` task, one or more local source paths, and uncertainty about which pattern should drive implementation.
Decision being made: choosing what context to load, what to offload, when to delegate, and how to prove completion.
Reference opening trigger: Open this file when the task mentions github context capture patterns, any mapped local source path, or an adjacent workflow with the same failure mode.

## Decision Tradeoff Guide

**Decision supported.** This section helps decide which capture mode and breadth provide enough evidence at acceptable collection cost and risk. The seed's Adopt, Adapt, Avoid, and Cost rows are generic and do not address survey versus trace, bounded versus exhaustive collection, high-level commands versus API harvesting, or fresh capture versus raw-data reuse.

**Recommended default and causal basis.** Choose a bounded Repo Survey for orientation, Artifact Trace for a known focal item, exhaustive canonical pagination only when explicitly required, high-level `gh` views for quick reads, API harvesting for durable lists, GraphQL for Discussions, and digest-only replay when raw data is adequate. Each mode trades breadth, detail, network cost, and completeness differently, so no single command is a safe universal default.

**Operating conditions and assumptions.** The tradeoff model works when the question, repo size, surface, and acceptable gaps are explicit. Mode selection never relaxes read-only safety, provenance, or gap disclosure.

**Failure boundary and alternatives.** It fails when bounded data is called exhaustive, exhaustive capture ignores rate limits, or quick views are persisted as durable archives. Bounded alternatives and recoveries: Bounded Survey, Widened Survey, Focused Trace, Quick View, Canonical Harvest, Discussion Query, Raw Replay, or Defer, selected by the evidence need and declared coverage.

**Counterexample, gotchas, and operational comparison.** The middle path can combine incomplete data with high cost, and sunk collection effort can pressure the digest to overclaim. Good: bounded survey then focused trace of a dense PR. Bad: unlimited crawl by default. Borderline: quick view for immediate orientation followed by canonical capture only if the answer controls action.

**Verification, evidence, and uncertainty.** Record chosen mode, rejected modes, expected coverage, page/date bounds, network cost, surface semantics, raw requirements, and widening trigger. The mode and command tradeoffs are direct corpus guidance. No universal page cap or repository-size threshold determines the optimal breadth.

**Second-order consequence.** Collection should maximize explanatory value per queried surface, not raw object count.

**Revision decision.** Replace generic rows with capture-mode, command-surface, breadth, and raw-reuse decisions.

**Retained seed evidence.** The seed decision vocabulary remains as historical framing beneath GitHub-specific choices. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| decision_option_name | when_to_choose_condition | tradeoff_cost_description | verification_question_prompt |
| --- | --- | --- | --- |
| Adopt when | local corpus and external evidence agree on the github context capture patterns pattern | fastest path, but can copy stale local assumptions | Does the selected pattern appear in the canonical source and current external evidence? |
| Adapt when | local sources are strong but public ecosystem guidance has changed | preserves repo fit, but requires explicit inference notes | Did the reference label the local fact, external fact, and combined inference separately? |
| Avoid when | source evidence is thin, conflicting, or unrelated to the user journey | prevents false confidence, but may require deeper research | Is there a confidence warning or adjacent reference route? |
| Cost of being wrong | wrong github context capture patterns guidance can send an agent to the wrong files, tests, or abstraction | wasted implementation loop and weaker verification | Would a reviewer know what to undo and what to inspect next? |

## Local Corpus Hierarchy

**Decision supported.** This section helps decide how policy, rationale, endpoint detail, GraphQL detail, and output format interact across the five local files. The seed correctly labels one canonical skill and four supporting files but does not assign rule ownership or explain their progressive and non-corroborating relationship.

**Recommended default and causal basis.** Let SKILL.md govern invocation and workflow, the thesis govern scope and non-goals, the surface map govern command choice, the Discussions reference govern GraphQL shapes and limits, and the output contract govern digest structure and raw expectations. Clear rule ownership prevents a convenient query example or template from silently overriding bounded scope and safety policy.

**Operating conditions and assumptions.** The hierarchy works while detail files refine the canonical workflow within their named surfaces. These archived roles do not override current GitHub behavior, current instructions, or user permissions.

**Failure boundary and alternatives.** It fails when supporting files are counted as independent votes, a query shape becomes globally mandatory, or output format drives collection before scope. Bounded alternatives and recoveries: Follow the canonical rule, apply the narrowest relevant detail, document conflicts, or request owner adjudication for true divergence.

**Counterexample, gotchas, and operational comparison.** Archived evidence dates, stale command examples, duplicated rationale, and flat headings can hide contradictions. Good: obey the skill's page cap even when an endpoint example shows pagination. Bad: treat five files as five confirmations. Borderline: update a query shape without changing the governing coverage rule.

**Verification, evidence, and uncertainty.** Check file hashes, rule ownership, cross-file consistency, selected reference, conflict record, and whether supporting detail stays inside canonical bounds. The local context strategy and file contents directly establish these roles. No explicit version policy defines precedence if future archived files diverge.

**Second-order consequence.** The hierarchy localizes maintenance: endpoint and format changes need not destabilize mode, safety, or provenance rules.

**Revision decision.** Add rule ownership, progressive scope, conflict resolution, and non-corroboration guidance.

**Retained seed evidence.** All five hierarchy rows remain with their complementary functions explicit. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Classification vocabulary includes canonical, supporting, legacy, duplicate, and conflicting source roles.

| local_source_filepath_value | corpus_hierarchy_role | heading_signal_to_convert | reviewer_question_to_answer |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202603/capture-github-repo-context/SKILL.md | canonical primary source | Capture GitHub Repo Context; Goal; Choose The Right Mode | What guidance, warning, or example should this source contribute to Github Context Capture Patterns? |
| agents-used-monthly-archive/codex-skills-202603/capture-github-repo-context/references/discussions-graphql-patterns.md | supporting detail source | Discussions GraphQL Patterns; Table Of Contents; Why Discussions Need GraphQL | What guidance, warning, or example should this source contribute to Github Context Capture Patterns? |
| agents-used-monthly-archive/codex-skills-202603/capture-github-repo-context/references/ghcli-surface-map.md | supporting detail source | GHCLI Surface Map; Table Of Contents; Command Choice Rules | What guidance, warning, or example should this source contribute to Github Context Capture Patterns? |
| agents-used-monthly-archive/codex-skills-202603/capture-github-repo-context/references/github-repo-context-thesis.md | supporting detail source | GitHub Repo Context Thesis; Table Of Contents; Core Thesis | What guidance, warning, or example should this source contribute to Github Context Capture Patterns? |
| agents-used-monthly-archive/codex-skills-202603/capture-github-repo-context/references/output-contract.md | supporting detail source | Output Contract; Table Of Contents; Digest Goals | What guidance, warning, or example should this source contribute to Github Context Capture Patterns? |

## Theme Specific Artifact

**Decision supported.** This section helps decide what artifact makes a GitHub context capture reproducible, reviewable, and reusable. The seed calls for a generic context budget policy, but the local output contract requires a capture manifest, separated raw artifacts, source-linked digest, chronology, and explicit gaps.

**Recommended default and causal basis.** Produce a capture package containing repository and host, mode, scope, collection time, filters and page caps, capabilities, surfaces and endpoints, cursor/page results, raw JSON manifest, relationship links, digest, source URLs, gaps, permissions, and rerun instructions. The package separates immutable evidence collection from revisable synthesis and lets another pass reproduce or extend the analysis.

**Operating conditions and assumptions.** It works when raw filenames and manifest entries are stable and every digest claim can link to a payload or GitHub URL. Store only authorized data, redact secrets, and avoid presenting raw paths as portable when they are environment-specific.

**Failure boundary and alternatives.** It fails when only a Markdown summary survives, raw files mix surfaces, page caps are absent, or credentials leak into artifacts. Bounded alternatives and recoveries: Use a focused trace bundle for one artifact, a lightweight survey manifest, or a digest replay from an existing raw directory.

**Counterexample, gotchas, and operational comparison.** Unstable paths, overwritten captures, mixed hosts, missing timestamps, unredacted tokens, and undocumented schema versions can make artifacts unsafe or irreproducible. Good: manifest five queried surfaces and their JSON files, then render a digest with links and gaps. Bad: save terminal output only. Borderline: one raw PR JSON is enough for a narrow quick trace if coverage limits are stated.

**Verification, evidence, and uncertainty.** Validate manifest schema, raw file existence and hashes, surface separation, capture timestamps, page/cursor metadata, URL resolution, digest replay, redaction, and gap completeness. The output contract and thesis directly require stable raw output, seven digest sections, coverage notes, and recoverable synthesis. A universal manifest schema and retention period are not defined in the archived corpus.

**Second-order consequence.** The capture package is a small evidence warehouse: stable raw facts support multiple future narratives without re-querying GitHub.

**Revision decision.** Replace the generic context-budget artifact with a concrete capture manifest, raw directory, and digest contract.

**Retained seed evidence.** The seed's goal, boundary, and gate fields remain embedded in a GitHub-specific evidence package. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Theme specific artifact: context budget policy for prompt, file, memory, and sub-agent handoff.

| artifact_field_name | artifact_completion_rule | evidence_source_hint |
| --- | --- | --- |
| user_goal_statement | state the user's concrete goal before applying Github Context Capture Patterns | local corpus hierarchy plus critique findings |
| decision_boundary_rule | define the point where this reference should be used or avoided | decision tradeoff guide |
| verification_gate_rule | define the command, checklist, or review question that proves the artifact worked | verification gate command set |

## Worked Example Set

**Decision supported.** This section helps decide what good, bad, and borderline repository-context capture look like for the same historical question. The seed examples are circular statements about loading sources and adding confidence warnings; they do not demonstrate mode choice, surface separation, pagination limits, commit relationships, raw preservation, or digest provenance.

**Recommended default and causal basis.** Use one regression investigation across all three examples so differences in preflight, scope, surfaces, relationship joins, raw artifacts, chronology, and gap disclosure are directly comparable. A shared scenario reveals which collection decision changes the explanation rather than labeling process compliance as quality.

**Operating conditions and assumptions.** The example set works when every case asks why one commit changed behavior and uses the same repository access boundary. Examples illustrate capture behavior and are not current factual claims about any repository.

**Failure boundary and alternatives.** It fails when good merely follows the reference, bad merely ignores it, or borderline has no explicit coverage condition that would change the verdict. Bounded alternatives and recoveries: Use onboarding, architecture archaeology, incident review, or a discussion-history scenario when those surfaces better demonstrate the method.

**Counterexample, gotchas, and operational comparison.** Examples can invent GitHub data, overfit public repositories, conceal rate limits, or imply one comment type speaks for every conversation. Good: link the regression commit to its PR, issue thread, reviews, timeline, and raw URLs while noting disabled Discussions. Bad: search commits and summarize the first hit. Borderline: a page-capped survey is useful but cannot claim exhaustive history.

**Verification, evidence, and uncertainty.** Ask reviewers to identify mode, scope, queried surfaces, missing surfaces, relationship evidence, chronology, raw paths, source links, and the exact claim limited by the page cap. The good and bad behaviors are direct consequences of the workflow, surface map, thesis, and output contract. One regression scenario cannot represent every GitHub permission model, repository size, or discussion topology.

**Second-order consequence.** The borderline case should name which additional page or surface could overturn the explanation, not merely lower generic confidence.

**Revision decision.** Replace circular examples with a shared regression trace, failed shortcut, and bounded partial capture.

**Retained seed evidence.** The good, bad, and borderline labels remain while their evidence paths become operational. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Good example: Use Github Context Capture Patterns after loading the canonical source, confirming the external evidence boundary, and writing a verification gate before implementation.
Bad example: Use Github Context Capture Patterns as a generic tutorial while ignoring the mapped local paths, source hierarchy, and cost of being wrong.
Borderline case: Use Github Context Capture Patterns only after adding a confidence warning when local evidence is thin or conflicts with current ecosystem guidance.

## Outcome Metrics and Feedback Loops

**Decision supported.** This section helps decide how to determine whether context capture improves repository understanding without rewarding indiscriminate collection. The seed tracks fewer clarifications and unverifiable claims but omits surface coverage, pagination disclosure, relationship-link accuracy, digest provenance, raw replay success, mutation safety, and user decision value.

**Recommended default and causal basis.** Track selected-surface coverage, hidden-gap rate, page-cap disclosure, source-link validity, chronology corrections, commit-to-PR link accuracy, raw-to-digest replay, duplicate network work avoided, mutation count, reviewer actionability, and follow-up traces requested. These signals connect collection discipline to a trustworthy explanation rather than to object count, API calls, or digest length.

**Operating conditions and assumptions.** They work across comparable repository and mode classes with known scope, baseline, reviewer, and observation window. Metrics cannot turn inaccessible data into absence or justify broader collection than the user authorized.

**Failure boundary and alternatives.** They fail when unselected surfaces count as misses, larger captures score better automatically, or reviewer agreement substitutes for source verification. Bounded alternatives and recoveries: Use qualitative archaeology retrospectives, paired digest review, sampled claim-to-raw audits, or later incident and onboarding outcomes.

**Counterexample, gotchas, and operational comparison.** Repository size, permissions, cache reuse, dense threads, and reviewer familiarity can dominate apparent quality and speed. Good: measure that raw replay answers a follow-up without network calls and exposes one prior chronology error. Bad: celebrate ten thousand objects. Borderline: track coverage and link validity while outcome data accumulates.

**Verification, evidence, and uncertainty.** Define scope denominator, metric formula, task class, sample, reviewer, exclusions, uncertainty, threshold, action, and later invalidations; retain raw verdicts. Coverage, provenance, recoverability, and gaps are direct local quality goals. No corpus evidence supplies universal target rates or proves causal improvements in onboarding or incident resolution.

**Second-order consequence.** The best capture may query less while explaining more because it follows relationships into decision-bearing threads.

**Revision decision.** Expand the feedback loop from generic clarification counts to coverage, provenance, replay, safety, and downstream usefulness.

**Retained seed evidence.** The original leading and failure signals remain as high-level outcomes within a fuller measurement chain. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Leading indicator: the next run needs fewer clarifications and produces fewer unverifiable claims.
Failure signal: the reference tells agents what to do without defining context budget or escalation rules.
Review cadence: Re-run the verifier after every generated-reference edit and refresh external sources when public APIs, docs, or tooling releases change.

## Completeness Checklist

**Decision supported.** This section helps decide whether a capture is complete for its declared scope or which omitted evidence still blocks the digest. The seed checks generic scenario, tradeoff, hierarchy, artifact, examples, metrics, and routing but omits the complete GitHub preflight, scope, surface, pagination, raw-artifact, digest, and gap contract.

**Recommended default and causal basis.** Require tool and auth preflight, repository and host, capability check, mode, scope, date/page bounds, selected surfaces, canonical command paths, comment separation, pagination evidence, raw manifest, relationships, chronology, source URLs, gaps, permissions, raw paths, and no mutation. A capture can look coherent while silently omitting the exact review or discussion surface that explains the change.

**Operating conditions and assumptions.** The checklist works when critical omissions block completion and waivers name authority, reason, and affected claims. Complete-for-scope must never be shortened to complete repository history.

**Failure boundary and alternatives.** It fails as a memory list, when all surfaces are mandatory regardless of scope, or when checked boxes lack raw evidence. Bounded alternatives and recoveries: Use manifest schema validation, a severity-weighted coverage audit, focused trace checklist, or digest replay test.

**Counterexample, gotchas, and operational comparison.** Checklist theater, stale auth output, unlabeled page caps, mixed comment files, broken URLs, and a raw directory without a manifest create false completeness. Good: mark Discussions not applicable after capability check. Bad: mark review comments covered because issue comments exist. Borderline: omit timelines for a quick PR view but state the resulting limit.

**Verification, evidence, and uncertainty.** Corrupt one critical manifest field or remove one selected raw surface and confirm the completion gate and affected digest claims fail. Every default item is explicit in the governing workflow, thesis, surface map, GraphQL caveats, or output contract. Criticality and waiver policy vary by declared capture mode and user question.

**Second-order consequence.** Completeness is relative to an explicit scope and surface denominator; without that denominator, percentages and PASS labels are meaningless.

**Revision decision.** Add preflight, selection, pagination, separation, raw, provenance, gap, and safety checks to the retained artifact checklist.

**Retained seed evidence.** The seven seed checks remain as reference-level checks beneath the capture-specific gate. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- The role scenario names the user, starting state, decision, and trigger for Github Context Capture Patterns.
- The decision guide includes Adopt when, Adapt when, Avoid when, and Cost of being wrong.
- The local corpus hierarchy identifies canonical and supporting sources or gives a confidence warning.
- The theme specific artifact is concrete enough to review without reading every mapped source.
- The examples cover good, bad, and borderline usage.
- The metrics section names one leading indicator and one failure signal.
- The adjacent routing section points to a better reference when this one is not the right fit.

## Adjacent Reference Routing

**Decision supported.** This section helps decide when captured GitHub evidence should route to code archaeology, incident analysis, technical debate, review remediation, CI diagnosis, or another repository. The seed names debate, subagent, context, verification, and vague GitHub adjacencies without a pivot question, evidence handoff, destination capability, or return condition.

**Recommended default and causal basis.** Keep collection and provenance here; route only after a digest or focused evidence packet exists, carrying repository, scope, raw paths, key URLs, chronology, unresolved gaps, and confidence into the destination. Evidence-preserving handoffs prevent downstream agents from re-querying inconsistently or treating a conditional digest as complete history.

**Operating conditions and assumptions.** Routing works when the destination has a distinct analysis or action job and an explicit return or stop condition. A handoff cannot expand GitHub mutation rights, repository scope, or confidence beyond the capture.

**Failure boundary and alternatives.** It fails when keyword similarity chooses the route, mutation begins from an unverified summary, or cross-repo conclusions are inferred from one repo. Bounded alternatives and recoveries: Remain in focused trace, widen one surface, route to code dependency analysis, agent debate, GitHub review-comment handling, CI diagnosis, or defer.

**Counterexample, gotchas, and operational comparison.** Context loss, duplicated collection, raw-path inaccessibility, downstream permission expansion, and disagreement between capture times can fragment evidence. Good: hand a source-linked PR trace to a technical debate. Bad: ask a CI fixer to infer history from a generic digest. Borderline: route one missing commit relationship back to focused capture before analysis resumes.

**Verification, evidence, and uncertainty.** Record pivot, destination, evidence packet, permissions, unresolved gaps, expected output, owner, stop condition, return path, and whether the destination changed the interpretation. The output and provenance contracts directly support evidence-bearing handoffs; specific adjacent tools depend on the workspace. Destination availability and exact packet formats vary across environments.

**Second-order consequence.** Routing should transform preserved evidence into a new decision, not repeat collection or erase coverage boundaries.

**Revision decision.** Replace placeholder adjacency with evidence-packet routes and return contracts.

**Retained seed evidence.** The seed's adjacent categories remain as destinations governed by explicit pivots. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Adjacent reference guidance: Use debate, subagent, context, or verification references when the task narrows to a specific agent behavior.
Adjacent reference 1: consider the github adjacent reference when the current task pivots away from github context capture patterns.
Adjacent reference 2: consider the context adjacent reference when the current task pivots away from github context capture patterns.
Adjacent reference 3: consider the capture adjacent reference when the current task pivots away from github context capture patterns.

## Workload Model

**Decision supported.** This section helps decide how much repository breadth, pagination, and parallel collection one capture can coordinate coherently. The seed imposes one task, ten source files, three subtasks, and a completion audit, but those numbers are uncalibrated and ignore repository size, selected surfaces, page caps, nested GraphQL replies, and relationship density.

**Recommended default and causal basis.** Bound one repository, host, mode, time window, selected surface set, and page cap; parallelize only independent read-only surfaces with one manifest and digest owner; widen deliberately when a named gap affects the answer. Repository size and conversation topology, not source-file count, drive network cost and synthesis complexity.

**Operating conditions and assumptions.** The model works for a bounded survey or a focused trace whose surfaces and output ownership are explicit. Parallel work must stay read-only, use exclusive raw paths, and preserve one canonical manifest and digest owner.

**Failure boundary and alternatives.** It fails for organization-wide joins, unbounded histories, several repositories with incompatible permissions, or concurrent writers racing one manifest. Bounded alternatives and recoveries: Narrow time or artifact scope, split independent surfaces, create per-repo packages, use hierarchical synthesis, or schedule a separately authorized exhaustive crawl.

**Counterexample, gotchas, and operational comparison.** Raw item count hides thread density, page caps differ by endpoint, nested replies may not follow top-level pagination, and parallel requests can amplify rate-limit pressure. Good: collect commits, PRs, issues, and comments in disjoint files under one page cap and manifest. Bad: set unlimited pages by default. Borderline: widen only the PR surface after survey density points there.

**Verification, evidence, and uncertainty.** Record repo size proxies, selected surfaces, page caps, cursors, nested limits, API calls, active writers, rate-limit state, split reason, and synthesis owner. Bounded-first collection, focused traces, page caps, and one stable raw package are direct corpus controls. No universal page, object, duration, or worker count defines safe capacity.

**Second-order consequence.** The scarce resource is coherent relationship reconstruction, not storage or request throughput.

**Revision decision.** Replace arbitrary file and subtask counts with repository, surface, pagination, topology, rate-limit, and ownership bounds.

**Retained seed evidence.** The seed workload rows remain as inherited heuristics with their unsupported numbers qualified. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`combined_evidence_inference_note`: Treat Github Context Capture Patterns as a agent workflow operating reference, not as a prose summary.

| workload_dimension_name | workload_boundary_value | verification_pressure_point |
| --- | --- | --- |
| primary_usage_surface | agent planning, tool use, context loading, delegation, or skill/plugin execution where bad guidance compounds across long-running sessions | verify that the reference changes the next implementation or review action |
| bounded_capacity_model | one primary task, up to 10 source files, up to 3 delegated subtasks, and a written completion audit for every run | split the task or create a narrower reference when this boundary is exceeded |
| source_pressure_model | local heading signals include Capture GitHub Repo Context; Goal; Choose The Right Mode; Workflow; Command Selection Guide; Use The Bundled Scripts; Discussions GraphQL Patterns; Ta | compare guidance against canonical local sources before following external examples |
| artifact_pressure_model | required artifact is context budget policy for prompt, file, memory, and sub-agent handoff | require the artifact before claiming the reference is operationally usable |

## Reliability Target

**Decision supported.** This section helps decide which capture properties are hard invariants and which outcomes require calibrated empirical evidence. The seed mixes universal evidence labels, an uncalibrated eighteen-of-twenty routing sample, zero unsupported claims, and recovery coverage without GitHub-specific surface, pagination, provenance, replay, or safety targets.

**Recommended default and causal basis.** Make read-only behavior, declared scope, selected-surface separation, page-cap disclosure, raw preservation, claim provenance, gap reporting, and zero credential leakage hard controls; calibrate routing accuracy, chronology usefulness, and capture efficiency by task class. Safety and evidence lineage can be checked exhaustively, while usefulness and completeness depend on repository topology, permissions, and user question.

**Operating conditions and assumptions.** This reliability model works when denominator, mode, repository class, reviewer, adjudication, and corrective action are explicit. Do not convert inherited samples into service levels, probabilities, or cross-repository guarantees.

**Failure boundary and alternatives.** It fails when one hundred percent means superficial labels, eighteen of twenty implies universal decision accuracy, or zero unsupported claims ignores inference and inaccessible history. Bounded alternatives and recoveries: Use severity-weighted audits, fixture matrices, live-repo samples, confidence calibration, raw replay checks, or qualitative review for small samples.

**Counterexample, gotchas, and operational comparison.** A digest can be process-compliant yet miss a decisive inaccessible review, and reviewers can agree because they share the same incomplete package. Good: hard-fail mutation or an undisclosed cap and separately trend digest actionability. Bad: claim ninety-percent repository coverage. Borderline: require exhaustive provenance only for action-controlling claims.

**Verification, evidence, and uncertainty.** Retain raw verdicts, repo and mode class, scope denominator, surface manifest, pages, gaps, claim audit, reviewer, uncertainty, later corrections, and response. The hard controls are direct corpus requirements; empirical seed thresholds lack supplied methodology. No local evidence establishes universal accuracy, latency, or completeness targets.

**Second-order consequence.** Reliable capture fails safely by making missing evidence and replay paths visible, allowing conclusions to be revised locally.

**Revision decision.** Classify seed targets and add GitHub-specific scope, surface, pagination, raw, gap, safety, and replay controls.

**Retained seed evidence.** The four original target rows remain with evidence classes and calibration limits. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| reliability_target_name | measurable_threshold_value | evidence_collection_method |
| --- | --- | --- |
| source_boundary_preservation | 100 percent of recommendations keep local, external, and inference boundaries visible | review generated text for the three evidence labels before reuse |
| decision_accuracy_sample | at least 18 of 20 sampled uses route to the correct adopt, adapt, avoid, or adjacent-reference decision | sample downstream tasks and record reviewer verdicts |
| unsupported_claim_rate | zero unsupported production, security, latency, or reliability claims in final guidance | reject claims without source row, explicit inference note, or verification method |
| recovery_path_clarity | every avoid or failure case names the rollback, escalation, or next-reference route | inspect failure-mode and adjacent-routing sections together |

## Failure Mode Table

**Decision supported.** This section helps decide how to diagnose a misleading or incomplete GitHub context package at the earliest failing stage. The seed includes source drift, generic advice, context loss, and tool fanout but omits most causal capture failures from preflight through digest rendering.

**Recommended default and causal basis.** Classify auth/host, repository identity, scope, mode, capability, command-surface, pagination, separation, relationship, raw persistence, chronology, digest, permission, and mutation failures separately. More synthesis cannot repair an unqueried surface, while recollecting everything is wasteful when only rendering or chronology failed.

**Operating conditions and assumptions.** The taxonomy works when each mode has a reproducible signal, containment, prior valid artifact, owner, and recheck. Stop action-controlling conclusions when the failed stage affects their source, chronology, relationship, or coverage.

**Failure boundary and alternatives.** It fails when every omission is called context loss, when inaccessible means absent, or when tool errors and evidence contradictions are conflated. Bounded alternatives and recoveries: Restore auth, correct repo, narrow scope, switch endpoint, continue pagination, run a focused query, replay raw data, relink chronology, or state an unresolved gap.

**Counterexample, gotchas, and operational comparison.** Failures cascade: wrong host passes empty capability checks, missing PR review comments flattens disagreement, and a polished digest then overstates consensus. Good: rerun only nested discussion replies after detecting truncation. Bad: recollect the repo. Borderline: reopen scope when a missing link changes the central explanation.

**Verification, evidence, and uncertainty.** Reproduce the signal, identify earliest causal stage, change one condition, compare raw manifests and digest claims, rerun downstream gates, and record residual limits. Every failure class maps to a direct workflow step, guardrail, surface trap, or output requirement. Failure frequency and severity require operational capture data.

**Second-order consequence.** Stage-aware diagnosis preserves valid raw evidence and prevents execution failures from erasing sound historical findings.

**Revision decision.** Expand the table into a stage-indexed capture taxonomy with precise recovery.

**Retained seed evidence.** The four seed failures remain as broad symptoms inside a GitHub-specific causal model. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| failure_mode_name | likely_trigger_condition | required_mitigation_action |
| --- | --- | --- |
| source drift hides truth | external or local guidance changes after the reference was written | refresh public evidence, rerun local corpus gate, and mark stale claims before reuse |
| generic advice escapes review | agent copies plausible best practices without theme-specific verification | block completion until the verification gate names concrete command, reviewer question, or metric |
| context window loses plan | long-running session forgets early constraints or overwrites user intent | write checkpoint summaries and re-read plan before each destructive step |
| tool fanout outruns budget | parallel actions create conflicts, duplicate work, or unbounded external calls | cap fanout, assign ownership, and require merge/audit checkpoints |

## Retry Backpressure Guidance

**Decision supported.** This section helps decide when another GitHub call or synthesis pass can add information and when collection should stop, narrow, or escalate. The seed gives one stale-evidence retry and generic checkpoints but does not distinguish auth, rate-limit, pagination, GraphQL, endpoint, raw, or digest failures.

**Recommended default and causal basis.** Classify the failed stage, preserve successful raw artifacts, change one relevant condition, retry the smallest idempotent read, compare results, and stop when no new evidence appears or authorization is missing. Targeted retries avoid duplicate network work, rate-limit pressure, and narrative drift while preserving recoverability.

**Operating conditions and assumptions.** It works for transient auth state, rate limiting, one failed page, schema mismatch, nested reply follow-up, or renderer failure. Retries cannot bypass permissions, fabricate absent objects, mutate state, or broaden scope without consent.

**Failure boundary and alternatives.** It is wrong for prohibited access, missing user scope, repeated permission denial, unbounded pagination, mutation side effects, or evidence that cannot be obtained through authorized surfaces. Bounded alternatives and recoveries: Narrow the scope, wait for reset, refresh auth through the user, switch to a canonical endpoint, use saved raw data, state a gap, or defer.

**Counterexample, gotchas, and operational comparison.** Parallel retries, duplicate pages, changed cursors, overwritten raw files, hidden query changes, and unlimited retry loops can corrupt manifests. Good: retry one failed page into a new raw file and reconcile cursors. Bad: restart the full crawl. Borderline: one focused nested-reply query, then document truncation.

**Verification, evidence, and uncertainty.** Record failure class, changed condition, attempt, request identity, cursor, rate-limit state, preserved files, new evidence, manifest diff, stop reason, and escalation. Bounded retry, raw recoverability, page caps, and explicit limits are direct local principles. Appropriate attempts and delays depend on GitHub responses, repository importance, and user timing.

**Second-order consequence.** Backpressure preserves a truthful capture boundary by making missing data cheaper to admit than to conceal through repeated calls.

**Revision decision.** Add stage-specific idempotent retries, cursor safety, raw preservation, information-gain checks, and stop paths.

**Retained seed evidence.** The retained stale-evidence and checkpoint guidance becomes one branch of a precise capture retry protocol. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- Retry only after the failed verification signal is classified as transient, stale evidence, missing context, or true contradiction.
- Use one bounded retry for stale external evidence refresh, then escalate to a human or a narrower source-specific reference.
- Apply backpressure by stopping new generation or implementation work when source coverage, critique coverage, or verification gates are red.
- For long-running agent workflows, checkpoint after each batch and re-read the current spec before any broad rewrite, commit, push, or destructive operation.
- For distributed execution, assign one owner per generated file or theme batch and require merge-time verification of exact path, heading, and evidence-boundary invariants.

## Observability Checklist

**Decision supported.** This section helps decide what compact telemetry lets another reviewer replay collection and audit the digest without exposing credentials. The seed records sources, proof, generic percentiles, tool calls, delegated tasks, retries, and compact evidence but omits host, repo, mode, surfaces, endpoints, cursors, page caps, raw hashes, relationships, and gap-linked claims.

**Recommended default and causal basis.** Record capture ID, time, host, repository, auth status without token material, mode, scope, filters, capabilities, surfaces, endpoints, pages and cursors, rate limits, raw paths and hashes, relationship links, renderer version, digest path, gaps, retries, and mutation count. A reproducible manifest distinguishes data collection state from interpretation and lets failures resume at the smallest safe point.

**Operating conditions and assumptions.** It works when event names, request identities, raw schemas, and file paths are stable and sensitive values are redacted. Never log credentials or distribute private raw content beyond authorized recipients.

**Failure boundary and alternatives.** It fails when logs contain only the digest, raw terminal dumps hide boundaries, or tokens and private payloads exceed the authorized report. Bounded alternatives and recoveries: Use a minimal manifest, sampled request log, raw file index, risk-tiered telemetry, or isolated secure storage for sensitive captures.

**Counterexample, gotchas, and operational comparison.** Credential leakage, URL query secrets, overwritten manifests, meaningless p99 on one run, clock skew, and missing capture versions can mislead review. Good: preserve page cursors and raw hashes while logging only that auth succeeded. Bad: store `GH_TOKEN`. Borderline: omit request timing for a one-off but retain scope, pages, and artifacts.

**Verification, evidence, and uncertainty.** Give the manifest and raw directory to an uninvolved reviewer and require digest replay, scope reconstruction, page accounting, surface separation, gap identification, and secret scan. The output contract, thesis, scripts, and seed observability cues directly support this event set. Retention, encryption, and private-repository redaction policies vary by organization.

**Second-order consequence.** Observability converts an interrupted crawl into a resumable data pipeline rather than an opaque terminal session.

**Revision decision.** Convert the generic checklist into a capture-manifest event schema and replay test.

**Retained seed evidence.** The seed's compact-audit preference remains and gains collection-specific telemetry. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- Record which local sources were loaded and which were intentionally skipped.
- Record the exact verification command, reviewer question, or rendered artifact used as proof.
- Record p50/p95/p99 latency or reviewer-time measurements when the reference affects runtime or workflow speed.
- Capture tool-call count, context files loaded, delegated tasks, retry count, and completion-audit outcome.
- Record leading indicator and failure signal from this file in the coverage manifest or journal when the reference drives real work.
- Keep audit evidence small enough to review: command output summary, changed-file list, and unresolved-risk notes are preferred over raw transcript dumps.

## Performance Verification Method

**Decision supported.** This section helps decide whether a capture produces sufficient explanatory coverage and recoverability for its network, storage, and review cost. The seed requires budgets and generic percentiles but does not tie cost to selected surfaces, pages, cache reuse, explanatory value, raw replay, or rate limits.

**Recommended default and causal basis.** Measure preflight, requests, pages, objects, bytes, rate-limit consumption, collection and rendering time, cache reuse, selected-surface coverage, link validity, digest review time, follow-up calls avoided, and correction rate; use percentiles only across comparable modes and repository classes. A smaller focused trace can outperform a large survey when it reaches the decision-bearing thread with less ambiguity and preserved evidence.

**Operating conditions and assumptions.** The method works with stable events, comparable repository classes, a baseline, enough samples, and quality guardrails. Do not present one repository's timing as an SLO or cross-repo benchmark.

**Failure boundary and alternatives.** It fails on one-run p95 values, raw object vanity metrics, speed gained by hiding caps, or throughput that overwhelms synthesis. Bounded alternatives and recoveries: Use direct timing for one run, value-of-information analysis, paired survey/trace comparison, qualitative review, or raw-replay savings.

**Counterexample, gotchas, and operational comparison.** Network latency, API cache, repo size, thread density, permissions, and reviewer familiarity can dominate measurements. Good: compare two bounded surveys by coverage and follow-up work. Bad: celebrate calls per second. Borderline: record wall time provisionally while building comparable samples.

**Verification, evidence, and uncertainty.** Define repo/mode class, input scope, events, units, sample, baseline, caps, rate-limit context, reviewers, exclusions, quality floor, uncertainty, and action. Budgets, bounded pagination, raw reuse, and digest actionability are direct corpus concerns. No universal timeout, tool-call budget, or latency threshold is established.

**Second-order consequence.** Performance is explanatory value per collection and review cost, with recoverability reducing the cost of future questions.

**Revision decision.** Separate single-run audit, repeated statistics, and value-of-information interpretation while qualifying inherited budgets.

**Retained seed evidence.** The original measurement packet remains as an inventory with unsupported precision bounded. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Performance method: require tool-call budgets, timeout budgets, and a resumable journal when the workflow exceeds one focused session.
Leading indicator to measure: the next run needs fewer clarifications and produces fewer unverifiable claims.
Failure signal to watch: the reference tells agents what to do without defining context budget or escalation rules.
Required measurement packet: capture input size, source count, tool-call count, wall-clock time, p50/p95/p99 latency where runtime applies, and reviewer decision time where documentation applies.
Pass condition: the reference must let a reviewer identify the correct next action, verification gate, and stop condition without reading unrelated files.
Fail condition: the reference encourages implementation before the workload, reliability target, and failure-mode table are explicit.

## Scale Boundary Statement

**Decision supported.** This section helps decide when one capture package must split and how distributed collection preserves one coherent historical account. The seed names multiple systems, ownership boundaries, unbounded discovery, production traffic, context drift, and graph narrowing but does not define repository, host, surface, or manifest decomposition.

**Recommended default and causal basis.** Split by repository, host, independent surface, or focal artifact only after shared scope, capture ID, time basis, manifest schema, raw-path ownership, and integration rules are explicit; keep one digest owner. Parallel reads can scale canonical collection, but chronology and relationship synthesis require consistent identities and one adjudicated narrative.

**Operating conditions and assumptions.** It works when surfaces are independent, writes are disjoint, rate limits are coordinated, and cross-links are stable. Distributed work remains read-only and cannot merge private data into an output unauthorized for all sources.

**Failure boundary and alternatives.** It fails across organization-wide joins, mixed hosts, shared cursors, tightly coupled artifacts, or multiple writers racing one manifest and digest. Bounded alternatives and recoveries: Narrow to one repo, run sequential dependencies, create per-repo packages, use hierarchical synthesis, or schedule an explicitly scoped cross-repo project.

**Counterexample, gotchas, and operational comparison.** Duplicate objects, conflicting timestamps, URL identity changes, lost cross-links, permission asymmetry, and rate-limit fanout can fragment context. Good: collect PR reviews and issue timelines separately into one manifest, then integrate. Bad: let each worker write its own chronology. Borderline: separate repositories but retain a shared cross-reference ledger.

**Verification, evidence, and uncertainty.** Produce repository/surface dependency map, owner matrix, capture IDs, exclusive paths, request budgets, merge order, deduplication keys, gap reconciliation, and final review. Repo-scoped v1, bounded-first capture, separate surfaces, stable raw data, and one digest support these controls. No universal object, repository, surface, or worker count marks the split point.

**Second-order consequence.** Scale is reached when relationship reconciliation and permission asymmetry grow faster than evidence gained from another parallel request.

**Revision decision.** Add repository, host, surface, manifest, rate-limit, ownership, and merge boundaries.

**Retained seed evidence.** The seed scale cautions remain and become a distributed capture architecture. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Github Context Capture Patterns stops being sufficient when the task spans multiple independent systems, more than one ownership boundary, unbounded source discovery, or production traffic without an explicit SLO.
Under distributed execution, split work by theme file and preserve one verification owner per split; do not let parallel agents rewrite the same reference without a merge checkpoint.
Under long-running agent workflows, treat context drift as a reliability failure: checkpoint state, summarize open risks, and verify against the spec before continuing.
Under large-codebase scale, require dependency or source-graph narrowing before applying this reference; a source list without ranked canonical guidance is not enough.

## Future Refresh Search Queries

**Decision supported.** This section helps decide how future authorized research should refresh the exact GitHub behavior that controls capture correctness. The seed uses broad best-practice, GitHub example, and release-note searches that are unlikely to verify a specific GHCLI command, API surface, pagination rule, or GraphQL connection.

**Recommended default and causal basis.** Form claim-first queries against current official GHCLI, REST, and GraphQL documentation for the named command, endpoint, preview, pagination, permission, field, or deprecation, including version and date where relevant. Endpoint-specific research is falsifiable and avoids letting popular repositories or generic workflow guidance define API semantics.

**Operating conditions and assumptions.** It works when browsing is authorized, the disputed claim is atomic, and a live behavior check can follow documentation review. Future browsing requires permission and cannot expand repository access or mutate state.

**Failure boundary and alternatives.** It fails with broad theme searches, snippets, result-count authority, stale examples, or release-note queries unrelated to a versioned surface. Bounded alternatives and recoveries: Use `gh help`, `gh api` response headers, local fixtures, archived evidence with dates, direct schema introspection, or state a freshness gap.

**Counterexample, gotchas, and operational comparison.** GitHub previews, Enterprise host differences, CLI version drift, deprecated fields, and nested GraphQL pagination can make generic examples unsafe. Good: query current official docs for `gh api --slurp` behavior or Discussions nested pagination. Bad: search 'GitHub context capture best practices.' Borderline: use a repository example to form a test, never as sole proof.

**Verification, evidence, and uncertainty.** Record claim, query, authorization, date, source class, CLI/host version, locator, selected and rejected results, live check, contradiction, and guidance change. The archived evidence base identifies the direct primary-source families needed for refresh. No query was run now, and future API and CLI behavior may differ from the archived 2026-04-08 evidence.

**Second-order consequence.** Search plans are part of capture reliability because stale endpoint assumptions can silently change the evidence denominator.

**Revision decision.** Retain query labels but replace generic text with command-, endpoint-, and claim-oriented templates.

**Retained seed evidence.** The generic query rows remain visible as weak seeds under stricter refresh guidance. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| search_query_label_name | search_query_text_value |
| --- | --- |
| `official_docs_query_phrase` | github context capture patterns official documentation best practices |
| `github_repository_query_phrase` | github context capture patterns GitHub repository examples |
| `release_notes_query_phrase` | github context capture patterns changelog release notes migration |

## Evidence Boundary Notes

**Decision supported.** This section helps decide how each digest claim exposes its provenance, surface semantics, coverage, and invalidation conditions. The seed distinguishes local, external, and combined inference but omits API payloads, timeline metadata, human conversation, inferred relationships, search discovery, absent versus inaccessible data, truncation, permissions, and capture time.

**Recommended default and causal basis.** Label direct raw API fact, GitHub URL fact, timeline event, human-authored conversation, inferred relationship, search lead, synthesis inference, inaccessible surface, truncated surface, capture-time absence, confidence, and invalidation trigger at claim level. A source-linked digest can still mislead if metadata is presented as opinion, a search hit as complete history, or an inaccessible thread as nonexistent.

**Operating conditions and assumptions.** It works when claims are atomic, raw locators and URLs are stable, capture time and scope are known, and labels propagate into handoffs. Expose explicit provenance without leaking credentials, unauthorized private content, or unsupported completeness.

**Failure boundary and alternatives.** It fails when one section label covers mixed surfaces, when inference hides a missing join, or when absence claims omit permission and pagination state. Bounded alternatives and recoveries: Use inline citations, provenance columns, claim ledgers, chronology annotations, coverage matrices, or a separate evidence appendix.

**Counterexample, gotchas, and operational comparison.** Duplicate API objects, edited comments, stale URLs, missing timestamps, page-cap ambiguity, cross-reference inference, and downstream label loss are principal risks. Good: label merge time as timeline metadata, rationale as a review-comment quote summary, and commit-to-issue relation as inference. Bad: call an uncaptured discussion absent. Borderline: section-level labeling only when all claims share one surface and scope.

**Verification, evidence, and uncertainty.** Sample final claims and reconstruct raw path, object ID, URL, surface, timestamp, capture time, permissions, page state, inference, contrary evidence, confidence, and invalidation. The local corpus directly requires surface separation, provenance, chronology, explicit gaps, and limits. Correct labels cannot prove completeness, author intent, or causal relationships beyond the captured evidence.

**Second-order consequence.** Fine-grained boundaries make later recapture local: a changed or newly accessible surface invalidates identifiable claims rather than the entire digest.

**Revision decision.** Extend the three seed labels into a claim-level GitHub capture evidence grammar.

**Retained seed evidence.** The original evidence labels remain as a compatible subset of richer surface and coverage metadata. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- `local_corpus_sourced_fact`: statements tied directly to the local source paths above.
- `external_research_sourced_fact`: statements tied to the public URLs above.
- `combined_evidence_inference_note`: synthesis that combines local and public evidence into agent guidance.
