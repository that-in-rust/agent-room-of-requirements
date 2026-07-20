# Skill Installer Distribution Patterns

**Decision supported.** This section helps decide how to classify and route a distribution-layer skill among authoring-layer themes. The seed no seed line states what this theme actually is, a 58-line preinstalled Codex system skill that turns GitHub directories into an installable skill registry, distributing skills from a three-tier upstream, curated, experimental, and preinstalled system tiers under openai/skills, plus arbitrary public or private repos, through two helper scripts and a defaults-plus-fallback download strategy.

**Recommended default and causal basis.** Route skill-movement questions here and skill-content questions to the creator themes, citing tier semantics whenever install-versus-preinstalled confusion appears. Codex needed skill distribution without a package manager, so the installer skill maps registry semantics onto plain GitHub structure, directories as packages, refs as versions, the API for listing and download-or-git for fetching, a distribution system built entirely from repository conventions.

**Operating conditions and assumptions.** The openai/skills repository retains its curated, experimental, and system directory layout. This reference covers skill distribution mechanics, skill authoring and evaluation belong to the creator-lineage themes.

**Failure boundary and alternatives.** Reading this as authoring guidance misses its category, the installer never teaches how to write skills, it defines how finished skills move from repos into $CODEX_HOME/skills and what the agent must say and do at each step. Bounded alternatives and recoveries: the Codex skill-creator theme for what gets distributed, this theme owns how it travels.

**Counterexample, gotchas, and operational comparison.** The skill is an agent prompt, not the scripts themselves, this corpus holds the 58 lines of instructions and interface descriptions, the Python that does the work is referenced but absent. Good: citing this theme for where installed skills land and how private repos authenticate. Bad: citing it for SKILL.md writing style. Borderline: citing it for the restart-required lifecycle fact, distribution-adjacent runtime behavior, this theme's edge but inside it.

**Verification, evidence, and uncertainty.** Re-read the 58 lines before any load-bearing reuse, the source is small enough to re-verify wholesale. One full read of the single mapped document this session. Whether the installer changed after 202603 is outside the corpus.

**Second-order consequence.** The installer is itself distributed by the mechanism it implements, it lives in the .system tier its own notes describe as preinstalled, a distribution tool shipped through its own channel, which is why its notes must special-case users asking to install it or its siblings, the bootstrap tier cannot be installed normally because it is already there.

**Revision decision.** Open with the registry-from-GitHub framing, the three-tier upstream, and the 58-line single-source evidence base.

**Retained seed evidence.** The exact theme title and reference framing remain unchanged. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

## Source Evidence Mapping Table

**Decision supported.** This section helps decide how much weight a single 58-line snapshot can carry. The seed one local row is the entire evidence base, a 58-line document with no sibling in any other sweep and no live-tree twin, making this the corpus's leanest theme, no identity diffs were possible and none of the multi-source triangulation richer themes enjoy applies here.

**Recommended default and causal basis.** Cite the one path for every local claim and date every operational statement to the 202603 sweep. The installer appears only in the 202603 Codex sweep, so every claim in this reference chains back to a single dated snapshot of a single file, evidence concentration by necessity rather than choice.

**Operating conditions and assumptions.** The archived file remains at its path unedited. Provenance for this document's statements, the three external URLs stayed unretrieved and confer no current-fact authority.

**Failure boundary and alternatives.** The risk of a one-source theme is invisible staleness, nothing in the repository can contradict or corroborate the snapshot, so overconfident reuse treats one month's text as standing truth. Bounded alternatives and recoveries: a future sweep importing a newer installer would double the evidence base and enable the lineage analysis this theme currently cannot do.

**Counterexample, gotchas, and operational comparison.** The document's own external references, the openai/skills URLs embedded in its text, are source-quoted facts about what the skill points at, not evidence about what those URLs currently contain. Good: an install-path claim cited to the one file with its sweep date. Bad: presenting the curated-list URL's current contents as verified because the skill names it. Borderline: quoting the embedded URLs as the skill's configured upstream, correct as source-quoted fact, wrong as live-repository claim.

**Verification, evidence, and uncertainty.** Confirm the file's continued presence and integrity at each audit cycle. The one full read and the sibling-absence check run this session. Everything beyond the snapshot, upstream layout, script behavior, current defaults, is unverified.

**Second-order consequence.** Single-source themes invert the duplication problem the skill-creator themes solved, there the work was discounting redundant copies, here the work is refusing to inflate one copy, the honest evidence statement is one file, one month, one platform, and every synthesis sentence must be built to survive on that.

**Revision decision.** Annotate the mapping with the single-source condition, the absent-twin fact, and the resulting all-claims-archive-dated rule.

**Retained seed evidence.** The one local row and three external rows with their column values remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| source_location_path_key | source_category_artifact_type | source_authority_confidence_level | source_usage_synthesis_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202603/.system/skill-installer/SKILL.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt |
| https://developers.openai.com/codex/guides/agents-md | external_research_source_material | external_research_sourced_fact | primary agent instruction context model |
| https://docs.github.com/actions | external_research_source_material | external_research_sourced_fact | verification and automation model |
| https://agents.md/ | external_research_source_material | external_research_sourced_fact | general agent instruction format |

## Pattern Scoreboard Ranking Table

**Decision supported.** This section helps decide which distribution patterns deserve default adoption. The seed three corpus-process rows stand where the installer's own patterns rank by robustness value, graceful method fallback ranks first, direct download falling back to git sparse checkout on auth errors, then HTTPS before SSH inside the git path, a three-deep resilience ladder in a 58-line skill, destination safety second, abort when the target directory exists, and explicit lifecycle communication third, the mandated restart-required message that keeps users from debugging a skill that simply is not loaded yet.

**Recommended default and causal basis.** Adopt fallback ladders for fetching, abort-on-existing for placement, and mandatory lifecycle messages for anything requiring a restart. Distribution failures are mostly environmental, auth walls, sandbox limits, existing state, so the installer's best patterns are the ones that convert environment variance into ordered fallbacks and clear messages rather than errors.

**Operating conditions and assumptions.** The fallback assumptions hold, download-first presumes public access is the common case. Ranking distribution patterns this skill teaches, authoring patterns rank under the creator themes.

**Failure boundary and alternatives.** Ranking by line count would elevate the options list over the fallback ladder, but options are surface area while the ladder is the design, the thing that makes one command work across public repos, private repos, and credential styles. Bounded alternatives and recoveries: the corpus's own queue-acceptance gates for document distribution, structural analogues at a different layer.

**Counterexample, gotchas, and operational comparison.** The one sanctioned overwrite is user-insisted reinstallation of preinstalled system skills, an explicit exception the notes carve out, safety defaults with a documented human override rather than an absolute rule. Good: an installer that falls through download, HTTPS git, SSH git before failing with the real error. Bad: silently overwriting an existing skill directory on reinstall. Borderline: overwriting a .system skill after the user insists, sanctioned, the exception is documented.

**Verification, evidence, and uncertainty.** Spot-check ranking claims against the behavior and notes sections. The full 58-line read this session. Actual failure-mode frequencies across the ladder are unrecorded.

**Second-order consequence.** The installer defaults to safety at state boundaries and permissiveness at transport boundaries, it will try three transports to fetch but refuses to touch an existing directory, write-side conservatism paired with read-side persistence, a asymmetry worth naming because most tools get it backwards.

**Revision decision.** Present the robustness ranking with the ladder's full depth and the abort-don't-overwrite default as the safety floor.

**Retained seed evidence.** The three scored seed rows with tier labels remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| pattern_identifier_stable_key | pattern_score_numeric_value | pattern_tier_adoption_level | pattern_failure_prevention_target |
| --- | ---: | --- | --- |
| `skill_installer_distribution_patterns` | 95 | default_adoption_pattern_tier | Source Map First: Load local skill installer material before synthesizing distribution patterns recommendations. |
| `skill_installer_distribution_patterns` | 91 | default_adoption_pattern_tier | Evidence Boundary Split: Separate local facts, external facts, and inference before giving agent instructions. |
| `skill_installer_distribution_patterns` | 88 | default_adoption_pattern_tier | Verification Gate Coupling: Attach each recommendation to at least one command, checklist, or review gate. |

## Idiomatic Thesis Synthesis Statement

**Decision supported.** This section helps decide what standard the installation dialogue must meet. The seed generic corpus formulas stand where the theme's thesis is that distribution is a conversation wrapped around a file copy, the skill spends more lines on what to say, the list format, the which-ones question, the restart notice, the explain-don't-install rule for system skills, than on how to fetch, because the copy is scripted and the judgment lives in the dialogue.

**Recommended default and causal basis.** Follow the templated dialogue at each stage and let the scripts own the mechanics. Installation decisions belong to the user, which skills, from where, whether to overwrite, so the skill's job is presenting options faithfully and reporting state transitions clearly, the scripts handle everything mechanical.

**Operating conditions and assumptions.** The interaction is user-driven, autonomous bulk installation would need different consent semantics than the ask-which-ones flow. The thesis governs distribution interactions, script internals are referenced machinery outside the corpus.

**Failure boundary and alternatives.** An agent that skips the dialogue installs the wrong things confidently, listing without the installed annotations hides what the user already has, and omitting the restart notice manufactures a support problem the message exists to prevent. Bounded alternatives and recoveries: silent scripted installation for provisioning pipelines, outside this skill's designed interaction model.

**Counterexample, gotchas, and operational comparison.** The already-installed annotation depends on reading $CODEX_HOME/skills, so listing is stateful, an accurate list requires local state inspection, not just the upstream fetch. Good: a numbered list with installed annotations ending in the which-ones question. Bad: installing three skills because the user asked what was available. Borderline: skipping the question when the user named an exact skill, sanctioned, the flow routes named requests straight to install.

**Verification, evidence, and uncertainty.** Sample installation transcripts for the templated messages at each stage. The communication section's quoted templates read this session. How strictly live agents follow the templates is unrecorded.

**Second-order consequence.** The skill templates its own user-facing speech, the listing format is given as a quoted block and the restart notice as an exact sentence, prompt-level output contracts, the same exact-format discipline the Claude harness applies to JSON applied here to human conversation, machine-readable rigor for human-readable output.

**Revision decision.** State the conversation-wrapped-copy thesis with the dialogue obligations enumerated, list with annotations, ask before installing, notify on lifecycle boundaries.

**Retained seed evidence.** The three labeled thesis statements remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`local_corpus_sourced_fact`: The local row for `skill_installer_distribution_patterns` contains 1 source path(s), which should be treated as the first retrieval surface for this theme.
`external_research_sourced_fact`: The external source map provides public documentation, repository, or ecosystem analogues where available.
`combined_evidence_inference_note`: Reliable use of Skill Installer Distribution Patterns comes from loading the local corpus first, checking public ecosystem guidance second, and converting both into verification-backed agent decisions.

## Local Corpus Source Map

**Decision supported.** This section helps decide which section answers a given distribution question. The seed heading signals list section names without the document's functional anatomy, five sections in 58 lines, a routing preamble mapping user requests to scripts, a communication section with output templates, a scripts section with invocation syntax including the sandbox escalation warning, a behavior section with the fallback and safety rules, and a notes section holding the tier semantics and credential details.

**Recommended default and causal basis.** Consult the section matching the question type and re-read the whole file when any two sections seem to conflict. The skill is organized as an interface contract, what to do, what to say, what to run, how it behaves, and edge knowledge, in that order, so navigation follows the question type directly to its section.

**Operating conditions and assumptions.** The archived file stays unedited at its path. Navigation of this theme's one document, the scripts it invokes are referenced but not in the corpus.

**Failure boundary and alternatives.** Answering credential questions from the scripts section misses that token fallbacks live in notes, and answering tier questions from the preamble misses that the preinstalled special case also lives in notes, the last section holds the subtlest rules. Bounded alternatives and recoveries: ripgrep is overkill here, wholesale re-reading is cheaper than searching a 58-line file.

**Counterexample, gotchas, and operational comparison.** The frontmatter carries a metadata block with a short-description field the other Codex skills' frontmatter conventions discuss, a small platform-specific schema detail sitting above the visible sections. Good: a private-repo auth question answered from notes with its token names. Bad: a tier question answered from the preamble alone, missing the preinstalled carve-out. Borderline: a listing-format question answered from memory of the template, re-quote it, exactness is the template's point.

**Verification, evidence, and uncertainty.** Trace each synthesis claim to its section at review time. The full anatomy read this session. None about structure, the document was read wholesale.

**Second-order consequence.** At 58 lines the whole source fits in one read, so the map's real value is inverted, it exists to keep synthesis honest rather than to save reading time, every claim in this reference should be traceable to one of five small sections, and any claim that cannot be is fabrication by construction.

**Revision decision.** Annotate the map with the five-section anatomy and the notes-holds-the-edge-cases warning.

**Retained seed evidence.** The one local source row with title, heading signals, and usage role remains preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| local_source_filepath_value | local_source_title_text | local_source_heading_signals | local_source_usage_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202603/.system/skill-installer/SKILL.md | skill-installer | Skill Installer; Communication; Scripts; Behavior and Options; Notes | skill entrypoint or reusable agent prompt |

## External Research Source Map

**Decision supported.** This section helps decide which external claims this theme owns, and the answer is the five seams. The seed three inherited agent-format anchors stand while the theme's real external surface is the machinery the skill names, the openai/skills repository's three directory tiers, the GitHub API the curated listing is fetched through, the git credential and token environment, GITHUB_TOKEN and GH_TOKEN, the $CODEX_HOME convention defaulting to ~/.codex, and the Codex sandbox whose network escalation the scripts require.

**Recommended default and causal basis.** Verify the five seams against current platform and upstream state before running the installer's doctrine live. The installer is a thin adapter over external systems, upstream layout, API availability, credential state, and sandbox policy all sit outside the skill, so its correctness is mostly a function of surfaces this corpus cannot verify.

**Operating conditions and assumptions.** The openai/skills repository and Codex sandbox conventions remain recognizable. External rows serve future freshness verification, all three URLs stayed unretrieved throughout this evolution.

**Failure boundary and alternatives.** Trusting the archive-dated surface descriptions on a current platform risks every named seam, a reorganized upstream breaks listing, an API change breaks fetching, renamed token conventions break private-repo access. Bounded alternatives and recoveries: the seed's inherited AGENTS.md and Actions anchors for ecosystem context, unmotivated for this theme's concrete seams.

**Counterexample, gotchas, and operational comparison.** The skill's URLs are upstream pointers baked into prompt text, updating the upstream location requires editing the skill itself, distribution configuration lives in prose, not in a config file. Good: a refresh checking the curated directory still exists at its URL. Bad: assuming GH_TOKEN still works because the archive names it. Borderline: reusing the ~/.codex default in current guidance, likely stable convention, still archive-dated.

**Verification, evidence, and uncertainty.** Record dated seam checks at each external refresh. Zero fetches this assignment and the seam inventory read from the source. Every seam's current state is unverified from local evidence.

**Second-order consequence.** The skill documents its own seam-failure behavior, if the curated listing is unavailable, explain the error and exit, a designed response to upstream rot written into the prompt, the source anticipates its external dependencies failing and scripts the honest degradation rather than a retry spiral.

**Revision decision.** Keep the inherited rows, add the five load-bearing seams with archive-dated markers, upstream layout, GitHub API, token conventions, CODEX_HOME, and sandbox escalation policy.

**Retained seed evidence.** All three external rows with their boundary labels remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| external_source_url_value | external_source_name_text | external_source_usage_role | evidence_boundary_label_value |
| --- | --- | --- | --- |
| https://developers.openai.com/codex/guides/agents-md | OpenAI Codex AGENTS.md guide | primary agent instruction context model | external_research_sourced_fact |
| https://docs.github.com/actions | GitHub Actions documentation | verification and automation model | external_research_sourced_fact |
| https://agents.md/ | AGENTS.md open format | general agent instruction format | external_research_sourced_fact |

## Anti Pattern Registry Table

**Decision supported.** This section helps decide which distribution failures need standing rules and where each rule binds. The seed three corpus-process rows stand where the source implies a distribution-failure registry, clobbering existing installations, prevented by the abort rule, silent lifecycle gaps, prevented by the mandated restart notice, unnecessary reinstallation of preinstalled tiers, prevented by the explain-first rule, credential leakage into URLs, avoided by routing auth through existing git credentials or environment tokens, and unlabeled source mixing, prevented by the label-the-source instruction when listing experimental skills.

**Recommended default and causal basis.** Enforce each rule at its stage, placement, communication, tier routing, auth, and listing. Each anti-pattern corrupts a different trust surface, state integrity, user mental model, tier semantics, secret hygiene, and provenance clarity, and the skill counters each with one explicit rule.

**Operating conditions and assumptions.** Agents actually follow prompt rules, script-level enforcement exists only for the abort behavior. Distribution-layer failures from the mapped source, authoring failures belong to the creator themes.

**Failure boundary and alternatives.** These failures are quiet, an overwritten skill just behaves differently, a missing restart notice just looks like a broken install, so prevention must be rule-shaped rather than detection-shaped, the damage is hard to see after the fact. Bounded alternatives and recoveries: post-install verification tooling, unmentioned by the source, prevention is its entire strategy.

**Counterexample, gotchas, and operational comparison.** The abort rule is the only one enforced by the script, the other four live purely in prompt discipline, so the registry's enforcement strength is uneven in a way the flat rule list hides. Good: an agent explaining the .system tier instead of reinstalling it. Bad: pasting a token into a repo URL to force a download. Borderline: reinstalling a system skill on explicit user insistence, sanctioned by the carve-out.

**Verification, evidence, and uncertainty.** Confirm each registry row cites its preventing line in the source. The behavior and notes rules read this session. How often live agents violate the prompt-only rules is unrecorded.

**Second-order consequence.** The registry is fully preventive, every entry pairs with a rule the 58 lines already state, meaning the skill was written failure-first, its authors enumerated what goes wrong in distribution and wrote one line against each, a compact demonstration that anti-pattern registries can be the generative skeleton of a skill rather than its afterthought.

**Revision decision.** Add the five rows each citing its preventing rule in the source, abort-on-existing, the exact notice, the .system carve-out, the credential routing, and the source labeling.

**Retained seed evidence.** The three seed process rows with their detection signals remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| anti_pattern_failure_name | failure_cause_risk_reason | safer_default_replacement_pattern | detection_signal_review_method |
| --- | --- | --- | --- |
| context_free_summary_output | agent skips local corpus and produces generic advice | source_map_first_synthesis | verify every listed local path appears in the generated file |
| unsourced_recommendation_claims | guidance appears authoritative without source boundary | evidence_boundary_split_pattern | check for local, external, and inference labels |
| unverified_agent_instruction | recommendation cannot be checked by command or review gate | verification_gate_coupling | require concrete gate in generated reference |

## Verification Gate Command Set

**Decision supported.** This section helps decide which operations run through the scripts and with which flags. The seed document verifier text stands where the theme's gates are the two helper scripts with their exact syntax, list-skills.py plain, with --format json, or with --path skills/.experimental, and install-skill-from-github.py with --repo plus one or more --path values or a --url form, governed by --ref, --dest, --name, and --method auto-download-git options, all requiring sandbox network escalation.

**Recommended default and causal basis.** Run listing before installation, use auto method unless diagnosing, and request escalation before either command. The skill routes every mechanical operation through these two commands, so they are the distribution layer's entire gate surface, listing gates what is visible, installation gates what lands.

**Operating conditions and assumptions.** The scripts exist beside the prompt in the deployed skill, the corpus holds their interface, not their code. The gate commands this skill defines, this document's own structural verification keeps the seed's retained block.

**Failure boundary and alternatives.** Bypassing the scripts, manual cloning into the skills directory, skips the abort safety, the installed annotations, and the naming conventions the scripts encode, reproducing exactly the failures they prevent. Bounded alternatives and recoveries: the corpus verifier command in the seed's retained block for this document's own checks.

**Counterexample, gotchas, and operational comparison.** Multiple --path values install several skills in one run with names taken from path basenames, a convenience that also means one typo installs under an unintended name unless --name pins it. Good: a diagnosis pinning --method download to isolate an auth failure. Bad: git cloning straight into ~/.codex/skills around the abort check. Borderline: batch-installing five curated skills with multiple --path flags, sanctioned, verify each landed name.

**Verification, evidence, and uncertainty.** Check installation transcripts for script provenance and escalation requests. The scripts section's syntax read this session. Script internals and error messages are undescribed beyond their interfaces.

**Second-order consequence.** The --method flag exposes the fallback ladder as user-selectable policy, auto for the designed ladder, download or git to pin a rung, which converts the resilience design from hidden behavior into a debuggable interface, when auto fails mysteriously a pinned method isolates which rung broke.

**Revision decision.** Inventory both commands with their full flag surface and the escalation requirement as a standing precondition.

**Retained seed evidence.** The seed's document verifier command block remains preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`verification_gate_command_set`: Run the repository verifier after editing this file.

```bash
python3 agents-used-monthly-archive/idiomatic-references-202606/tools/verify_reference_generation.py --stage final
```

## Agent Usage Decision Guide

**Decision supported.** This section helps decide which intent a request maps to and what the agent owes at each state change. The seed four generic bullets stand where the skill defines a single-agent protocol with three routed intents, list when the user asks what is available or gives no specifics, install-by-name when they name a curated skill, and install-by-location when they give a repo or path, plus one standing conversational duty at each state change and one refusal duty at the .system tier.

**Recommended default and causal basis.** Route by intent, default to listing, and never install what is already preinstalled without explicit insistence. Distribution needs no multi-agent cast, one agent with clear intent routing covers the whole surface, the complexity lives in the environment, not the role structure.

**Operating conditions and assumptions.** User intent is expressed in the request, genuinely ambiguous cases fall to the listing default by design. Agent behavior for this skill, the creator themes' multi-role casts govern authoring and evaluation.

**Failure boundary and alternatives.** Misrouted intents produce the annoying failure modes, a listing request answered with an installation, a named skill answered with the full catalog, or a system-skill request answered with a redundant download. Bounded alternatives and recoveries: the evaluation theme's five-role cast when the installed skills themselves need quality assessment.

**Counterexample, gotchas, and operational comparison.** Already-installed annotations change the conversation's meaning, a listing without them invites reinstall requests the abort rule will then reject, the annotations are conversational load-bearing, not decoration. Good: an unspecified request answered with the annotated curated list. Bad: install this repo's skill answered with the catalog question. Borderline: a request naming an experimental skill, route to install with the experimental path and label the source.

**Verification, evidence, and uncertainty.** Audit transcripts for intent-routing and annotation fidelity. The routing preamble and communication rules read this session. How live agents handle genuinely mixed intents is unrecorded.

**Second-order consequence.** The default intent is the humble one, when the user invokes the skill without saying what they want, the skill lists rather than guesses, defaulting to information over action, the same read-side permissiveness and write-side conservatism the method ladder shows, expressed at the conversational layer.

**Revision decision.** Recast the section as the three-intent router with the default-to-listing rule for unspecified requests and the explain-first rule for the preinstalled tier.

**Retained seed evidence.** The four seed usage bullets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`agent_usage_decision_guide`: Use this reference when a task mentions this theme, one of the listed local source paths, or a nearby technology/workflow surface.

- Start with the local corpus source map.
- Prefer patterns with explicit verification gates.
- Treat external sources as freshness and ecosystem checks, not replacements for local repo conventions.
- Preserve the evidence boundary labels when reusing recommendations.

## User Journey Scenario

**Decision supported.** This section helps decide which arrival this user is and which designed response serves them. The seed one generic engineer stands where the skill's flows imply three arrivals, the browser who asks what is available and needs the annotated catalog, the targeted installer who names a skill or repo and needs a fast clean install with the restart notice, and the confused system-tier user who asks to install what is already preinstalled and needs an explanation before any action.

**Recommended default and causal basis.** Identify the arrival from the request shape and follow its designed response including the exact lifecycle messages. Each arrival maps to one routed intent, so the journey layer and the routing layer are the same structure seen from the user's side.

**Operating conditions and assumptions.** Requests arrive through the conversational interface the skill assumes. Journeys through skill installation, journeys through the installed skills belong to their own themes.

**Failure boundary and alternatives.** Treating the browser as a targeted installer skips the consent question, and treating the system-tier user as a normal installer wastes a download and overwrites a managed tier. Bounded alternatives and recoveries: the creator themes' journey maps for users who arrive wanting to make skills rather than obtain them.

**Counterexample, gotchas, and operational comparison.** The private-repo journey is a variant of targeted installation, not a separate arrival, its difference is auth machinery the fallback ladder handles silently, the user experience is designed to be identical. Good: a which-skills-exist request answered with the numbered annotated list. Bad: a preinstalled-skill request answered with a fresh download. Borderline: a user insisting after the explanation, proceed with overwrite, the carve-out sanctions it.

**Verification, evidence, and uncertainty.** Check transcripts for arrival identification before action. The flows and notes read this session. The actual mix of arrivals among live users is unrecorded.

**Second-order consequence.** The third journey is preventive support, the skill anticipates a specific user confusion, asking to install preinstalled skills, and scripts the correction into the prompt, if they ask, just explain this, distribution tools accrete these explain-don't-act paths wherever their tier model diverges from user intuition.

**Revision decision.** Recast the scenario as the three arrivals with their designed responses, catalog with annotations, install with notice, explain with optional insisted override.

**Retained seed evidence.** The role, starting state, decision, and trigger lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Role based opening scenario: The new contributor or agent is starting from an unfamiliar theme and deciding whether this reference is the right tool and needs a reference that turns source evidence into an executable next step.
Primary user starting state: The user has a `skill_installer_distribution_patterns` task, one or more local source paths, and uncertainty about which pattern should drive implementation.
Decision being made: choosing what to load, what to trust, what to avoid, and what evidence proves success.
Reference opening trigger: Open this file when the task mentions skill installer distribution patterns, any mapped local source path, or an adjacent workflow with the same failure mode.

## Decision Tradeoff Guide

**Decision supported.** This section helps decide which method, tier, and batch shape serves a given installation request. The seed template rows skip the skill's live tensions, method choice, auto's resilient ladder against pinned methods' diagnosability, tier choice, curated stability against experimental novelty with its labeling duty, and batch size, multi-path efficiency against per-skill naming control.

**Recommended default and causal basis.** Auto method, curated tier, and single-path installs unless the request argues otherwise. Each axis is decided per-request, method by whether the goal is success or diagnosis, tier by the user's risk appetite, and batch by how much naming precision the install needs.

**Operating conditions and assumptions.** The upstream maintains its tier discipline, a curated directory that accepts anything collapses the gradient. Tradeoffs in operating the installer, tradeoffs in skill content belong to the creator themes.

**Failure boundary and alternatives.** Wrong poles fail characteristically, pinned methods in normal use forfeit the ladder's resilience, unlabeled experimental installs misrepresent provenance, and large batches with basename naming can land skills under surprising names. Bounded alternatives and recoveries: forking skills into one's own repo and installing from there, fully supported by the arbitrary-repo path and outside the tier gradient entirely.

**Counterexample, gotchas, and operational comparison.** --dest changes where skills land, useful for staging but the skill's installed annotations only read $CODEX_HOME/skills, so custom destinations silently fall off the annotation radar. Good: an experimental install performed on request with the source labeled. Bad: pinning --method git as a personal default and losing download-first speed. Borderline: installing to a custom --dest for testing, sanctioned by the flag, note the annotation blind spot.

**Verification, evidence, and uncertainty.** Review install decisions against the three axes' conditions. The options, tier, and labeling rules read this session. How the upstream's tier discipline holds over time is unverifiable locally.

**Second-order consequence.** The tier axis carries an implicit trust gradient the skill makes conversational, curated is the default nobody must ask for, experimental requires the user to ask and the agent to label, and system is closed to installation entirely, three tiers expressed not as permissions but as different amounts of required dialogue.

**Revision decision.** Add the three axes with their deciding conditions, purpose for method, risk appetite for tier, naming needs for batch size.

**Retained seed evidence.** The adopt, adapt, avoid, and cost-of-being-wrong rows remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| decision_option_name | when_to_choose_condition | tradeoff_cost_description | verification_question_prompt |
| --- | --- | --- | --- |
| Adopt when | local corpus and external evidence agree on the skill installer distribution patterns pattern | fastest path, but can copy stale local assumptions | Does the selected pattern appear in the canonical source and current external evidence? |
| Adapt when | local sources are strong but public ecosystem guidance has changed | preserves repo fit, but requires explicit inference notes | Did the reference label the local fact, external fact, and combined inference separately? |
| Avoid when | source evidence is thin, conflicting, or unrelated to the user journey | prevents false confidence, but may require deeper research | Is there a confidence warning or adjacent reference route? |
| Cost of being wrong | wrong skill installer distribution patterns guidance can send an agent to the wrong files, tests, or abstraction | wasted implementation loop and weaker verification | Would a reviewer know what to undo and what to inspect next? |

## Local Corpus Hierarchy

**Decision supported.** This section helps decide which part of the one document settles a given question. The seed role labels rank a single source against nothing, the one 58-line document is canonical by default, and the real hierarchy question is internal, which of its five sections settles a conflict, where the answer is that notes outranks the preamble on edge semantics, behavior outranks scripts on runtime rules, and the quoted templates outrank paraphrase everywhere.

**Recommended default and causal basis.** Answer routine questions from the matching section and edge questions from notes, quoting templates verbatim. With one source, precedence collapses into reading discipline, later sections refine earlier ones, and exact quotations beat remembered summaries, so hierarchy here is about resolving tensions inside one small text.

**Operating conditions and assumptions.** The file stays unedited, any modification would be a corpus-integrity event, not a version event. Precedence within this theme's single document, cross-theme precedence belongs to the corpus hierarchy.

**Failure boundary and alternatives.** Treating the preamble as complete doctrine misses the notes section's carve-outs, the preinstalled tier and the credential fallbacks, precisely the rules that change what an agent should do. Bounded alternatives and recoveries: escalating internal conflicts to nothing, wholesale re-reading is the single-source tiebreaker.

**Counterexample, gotchas, and operational comparison.** The seed labels this source canonical primary, correct but trivially so, the label carries no discriminating information when the source count is one. Good: resolving an auth question from the notes section's token rules. Bad: paraphrasing the restart notice loosely when the source gives its exact sentence. Borderline: citing the frontmatter description for trigger semantics, valid, it is the one section above the visible five.

**Verification, evidence, and uncertainty.** Test rulings against the section refinement order. The internal structure read this session. None about current structure, the document was read wholesale.

**Second-order consequence.** Single-source themes make the corpus's hierarchy machinery almost vacuous, and that emptiness is informative, this theme's confidence ceiling is set entirely by one snapshot's internal consistency, there is no second source to break ties, so any apparent contradiction in the 58 lines must be resolved by re-reading rather than by outranking.

**Revision decision.** Restate the hierarchy as internal, the five sections in refinement order with notes as the edge-case authority and templates as verbatim contracts.

**Retained seed evidence.** The one hierarchy row and the classification vocabulary remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Classification vocabulary includes canonical, supporting, legacy, duplicate, and conflicting source roles.
Confidence warning: only one local corpus source is mapped, so this reference should invite adjacent-source discovery before becoming canonical policy.

| local_source_filepath_value | corpus_hierarchy_role | heading_signal_to_convert | reviewer_question_to_answer |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202603/.system/skill-installer/SKILL.md | canonical primary source | Skill Installer; Communication; Scripts | What guidance, warning, or example should this source contribute to Skill Installer Distribution Patterns? |

## Theme Specific Artifact

**Decision supported.** This section helps decide what standing evidence makes the installer's operation consultable at speed. The seed generic worked-example artifact misses this theme's natural object, an installation decision runbook, one page mapping request shapes to intent routes, script invocations with flags, required dialogue at each stage, and the failure ladder's rungs with what each rung's failure means, distilled from the 58 lines into an operator's card.

**Recommended default and causal basis.** Consult the runbook during live installations and mine it when designing analogous distribution tools. The source is an agent prompt whose knowledge is already operational, so its natural artifact is not analysis but compression, the same rules reorganized by execution order for someone mid-installation.

**Operating conditions and assumptions.** The runbook stays synchronized with the single source, one small file makes drift cheap to catch. One runbook for this skill's operation, extensible if newer installer versions arrive in later sweeps.

**Failure boundary and alternatives.** Without the runbook, each installation re-derives the flow from the five sections, and the prompt-only rules, labeling, notices, tier explanations, are the ones most likely dropped under time pressure. Bounded alternatives and recoveries: leaving the operational knowledge in this packet's prose, recoverable but not execution-ordered.

**Counterexample, gotchas, and operational comparison.** The runbook must preserve the exact quoted messages, compressing the restart notice into a paraphrase defeats the template contract the source establishes. Good: a mid-install auth failure resolved by the runbook's ladder column in seconds. Bad: re-reading five sections while a user waits on a simple curated install. Borderline: extending the runbook with provisioning-pipeline guidance, useful, beyond the source's designed interaction model and must be labeled inference.

**Verification, evidence, and uncertainty.** Check the runbook exists with all elements source-cited. The operational inventory assembled from the full read this session. Whether later sweeps hold newer installer versions is a queue question.

**Second-order consequence.** The runbook's most valuable column is the failure-meaning one, download failing with auth errors means try git, git HTTPS failing means try SSH, destination existing means stop and ask, mapping each failure to its designed next step turns the skill's implicit resilience into explicit operator knowledge.

**Revision decision.** Define the artifact as the request-to-action runbook with the three intents, two commands, four dialogue obligations, and the three-rung failure ladder, each element cited to its source line.

**Retained seed evidence.** The artifact field rows with completion rules and evidence hints remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Theme specific artifact: skill activation contract with progressive disclosure, misuse case, and verification gate.

| artifact_field_name | artifact_completion_rule | evidence_source_hint |
| --- | --- | --- |
| user_goal_statement | state the user's concrete goal before applying Skill Installer Distribution Patterns | local corpus hierarchy plus critique findings |
| decision_boundary_rule | define the point where this reference should be used or avoided | decision tradeoff guide |
| verification_gate_rule | define the command, checklist, or review question that proves the artifact worked | verification gate command set |

## Worked Example Set

**Decision supported.** This section helps decide which exercises build routing and protocol fluency fastest. The seed abstract usage lines stand where this theme wants scenario drills, give a learner five request shapes, an open what-skills-exist, a named curated skill, a private-repo URL, an experimental-skill request, and a preinstalled-skill request, and require the correct intent route, command with flags, and dialogue for each, graded against the source's rules.

**Recommended default and causal basis.** Run the five-scenario drill before operating the installer and the composite scenario before certifying. The installer's competence is routing plus protocol, both testable through scenario response without any live installation, so drills exercise the whole skill at zero infrastructure cost.

**Operating conditions and assumptions.** Drills use realistic request phrasings, sanitized prompts hide the intent-ambiguity the routing must resolve. Teaching installer operation, authoring drills belong to the creator themes.

**Failure boundary and alternatives.** Undrilled operators fail on the edge scenarios, the preinstalled request and the experimental labeling duty, exactly the prompt-only rules with no script enforcement behind them. Bounded alternatives and recoveries: supervised live installations, richer and requiring infrastructure the drill does not.

**Counterexample, gotchas, and operational comparison.** The drill's answer for the open request must default to listing, learners who default to asking clarifying questions are being polite but wrong, the source designates listing as the no-specifics response. Good: a drilled response routing the private-repo URL to install-by-location with escalation noted. Bad: certifying an operator who reinstalls preinstalled skills on request. Borderline: a response adding an unrequested experimental listing to a curated request, helpful instinct, exceeds the routed intent.

**Verification, evidence, and uncertainty.** Grade drill responses against the source-derived answer key. The routing rules and dialogue obligations read this session. Transfer from drills to live operation is unmeasured.

**Second-order consequence.** The hardest drill scenario is the fourth and fifth combined, a user asking to install an experimental skill that is already installed, requiring the annotation check, the labeling duty, and the abort expectation simultaneously, composite scenarios reveal whether rules were learned as a system or as a list.

**Revision decision.** Anchor the section on the five-scenario drill with an answer key derived line-by-line from the source.

**Retained seed evidence.** The good, bad, and borderline seed lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Good example: Use Skill Installer Distribution Patterns after loading the canonical source, confirming the external evidence boundary, and writing a verification gate before implementation.
Bad example: Use Skill Installer Distribution Patterns as a generic tutorial while ignoring the mapped local paths, source hierarchy, and cost of being wrong.
Borderline case: Use Skill Installer Distribution Patterns only after adding a confidence warning when local evidence is thin or conflicts with current ecosystem guidance.

## Outcome Metrics and Feedback Loops

**Decision supported.** This section helps decide which measurements would prove the installer's designed properties hold in operation. The seed compile-centric indicator misses what installer operation would actually measure, install success rate by method rung, revealing which ladder steps carry the load, dialogue compliance, the four obligations present in transcripts, tier mix, curated versus experimental versus arbitrary-repo installs, and post-install confusion rate, users reporting broken skills that were merely unrestarted.

**Recommended default and causal basis.** Track rung usage and dialogue compliance where transcripts exist, and read rising fallback rates as seam alarms. The skill's design goals, resilience, clarity, tier discipline, each imply a measurable, and the restart notice exists precisely because the confusion it prevents was observable.

**Operating conditions and assumptions.** Transcripts or logs are available, the skill itself specifies no telemetry. Measuring installer operation and this node's evidence, installed-skill quality metrics belong to the evaluation theme.

**Failure boundary and alternatives.** Unmeasured rung usage hides upstream degradation, download failures silently shifting load to git fallback, and unmeasured dialogue compliance lets the prompt-only rules erode invisibly. Bounded alternatives and recoveries: the evaluation theme's benchmark machinery for measuring the installed skills themselves.

**Counterexample, gotchas, and operational comparison.** None of these series exist in the source, they are designed measurements this synthesis derives from its rules, reuse must label them inference, not documented practice. Good: a monthly rung-distribution review catching a drift toward git fallback. Bad: counting installs while dialogue obligations quietly disappear. Borderline: measuring restart-notice compliance by later confusion reports, indirect, the notice's absence is the likelier cause.

**Verification, evidence, and uncertainty.** Confirm the series exist with dated entries wherever the installer is operated. The design goals read from the source and this session's synthesis. No operational data exists in the corpus, all series are prospective.

**Second-order consequence.** Rung distribution is the highest-information series, a healthy system installs mostly by direct download, so rising fallback rates are an early warning about upstream auth or API changes before they become failures, the ladder doubles as a passive sensor for seam rot.

**Revision decision.** Adopt the four operational series plus this theme's evidence series, the single source's integrity check at audit cadence.

**Retained seed evidence.** The leading indicator, failure signal, and review cadence lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Leading indicator: the next task uses the reference to make a better decision with less ambiguity.
Failure signal: the reference remains a source map and never becomes an operating guide.
Review cadence: Re-run the verifier after every generated-reference edit and refresh external sources when public APIs, docs, or tooling releases change.

## Completeness Checklist

**Decision supported.** This section helps decide what must be confirmed before this operational reference is declared faithful. The seed shape items never audit this theme's distinctive claims, the single-source condition and its sibling-absence check, the runbook's line citations, the five-seam inventory's archive dating, the inference labeling on all prospective metrics, and the verbatim fidelity of the two quoted templates.

**Recommended default and causal basis.** Re-read the whole source at every audit cycle and re-run the sibling-absence check when any new sweep arrives. The theme's substance is operational compression of one small file, so completeness auditing means re-checking that compression against the source, cheap because the source is 58 lines.

**Operating conditions and assumptions.** The source stays 58 lines, growth via a newer version would move audits to the sampling regime. Auditing this reference against its source, the one document was read in full once.

**Failure boundary and alternatives.** A shape-only audit passes while a paraphrased restart notice or an unlabeled inferred metric quietly violates the theme's two strictest rules, template exactness and evidence honesty. Bounded alternatives and recoveries: sampling audits, unjustifiable at this source size.

**Counterexample, gotchas, and operational comparison.** Sibling absence is a standing claim that new sweeps can falsify at any time, it is the one distinctive claim whose truth is scheduled to change, treat its re-check as the audit's first item. Good: an audit logging a full re-read, clean template checks, and a fresh sibling scan. Bad: fidelity declared without re-checking the quoted notices. Borderline: skipping the sibling scan between sweeps, acceptable, nothing new could have arrived.

**Verification, evidence, and uncertainty.** Execute the distinctive items and date each result in the audit record. The claim structure of every distinctive statement in this document. Future sweep contents govern when sibling absence flips.

**Second-order consequence.** This theme has the corpus's cheapest full audit, re-reading the entire evidence base costs one minute, so unlike every multi-source theme there is no excuse for sampling, the audit standard should be total re-verification precisely because totality is affordable.

**Revision decision.** Add the distinctive items, source integrity, sibling absence re-check on new sweeps, runbook citation resolution, seam dating, inference labels, and template verbatim checks.

**Retained seed evidence.** All seven seed checklist bullets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- The role scenario names the user, starting state, decision, and trigger for Skill Installer Distribution Patterns.
- The decision guide includes Adopt when, Adapt when, Avoid when, and Cost of being wrong.
- The local corpus hierarchy identifies canonical and supporting sources or gives a confidence warning.
- The theme specific artifact is concrete enough to review without reading every mapped source.
- The examples cover good, bad, and borderline usage.
- The metrics section names one leading indicator and one failure signal.
- The adjacent routing section points to a better reference when this one is not the right fit.

## Adjacent Reference Routing

**Decision supported.** This section helps decide where to send a question arriving at the distribution theme. The seed token-split rows point nowhere while this theme's neighbors are functional, the Codex skill-creator theme for authoring what gets installed, the evaluation theme for measuring installed skills, the platform-entrypoint themes for how installed skills trigger and load, and the corpus's own distribution machinery, queues and sweeps, for document-artifact movement.

**Recommended default and causal basis.** Classify the question's lifecycle stage first and route accordingly, keeping only repo-to-directory movement here. This theme owns the movement of skills between repositories and runtime directories, everything about their content, quality, or runtime behavior after landing has a closer home.

**Operating conditions and assumptions.** The neighboring themes remain evolved, the two skill-creator themes completed as assignments 55 and 56. Sending away what this theme holds only incidentally, destination doctrine is deliberately not restated.

**Failure boundary and alternatives.** Answering authoring questions here produces distribution-flavored non-answers, and keeping post-install trigger questions here misses that loading semantics belong to the platform themes. Bounded alternatives and recoveries: for script-internals questions, nothing, the corpus holds the prompt but not the Python.

**Counterexample, gotchas, and operational comparison.** The restart-required fact sits on the boundary, it is a loading semantic this skill must communicate, so both this theme and the platform themes legitimately cite it, from different angles. Good: forwarding a description-triggering question to the platform theme. Bad: answering a skill-quality question with installation mechanics. Borderline: a question about installing skills one authored oneself, spans creation and movement, answer the movement half and route the rest.

**Verification, evidence, and uncertainty.** Sample recent answers for lifecycle-stage routing consistency. The theme boundaries assembled across this cluster's evolutions. Future sweeps may add distribution siblings that refine the boundaries.

**Second-order consequence.** The skill lifecycle now has full corpus coverage across four theme families, created, evaluated, distributed, and loaded, with this theme the thinnest but load-bearing link, distribution is where authored artifacts become runtime capabilities, and routing questions along the lifecycle is more reliable than routing by keyword.

**Revision decision.** Route by lifecycle stage, creation to the creator themes, movement here, loading and triggering to platform themes, quality to the evaluation theme.

**Retained seed evidence.** The three seed adjacent-reference lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Adjacent reference guidance: Use the nearest language, workflow, agent, or documentation reference when the theme becomes concrete.
Adjacent reference 1: consider the skill adjacent reference when the current task pivots away from skill installer distribution patterns.
Adjacent reference 2: consider the installer adjacent reference when the current task pivots away from skill installer distribution patterns.
Adjacent reference 3: consider the distribution adjacent reference when the current task pivots away from skill installer distribution patterns.

## Workload Model

**Decision supported.** This section helps decide how to budget the corpus's smallest theme without under-maintaining it. The seed symbol-count boundary misprices this node's work, whose units are per-audit full re-reads, one minute for 58 lines, per-sweep sibling scans, one find command, and per-question routing along the lifecycle split, with the one-time evolution read already sunk at the corpus's smallest source cost.

**Recommended default and causal basis.** Re-read wholesale at audit cadence, scan for siblings at each sweep, and provision a delta analysis only when a sibling appears. The source's size makes every maintenance operation total rather than sampled, so the workload model has no expensive steady-state regime at all, only the version-event regime if a newer installer ever arrives.

**Operating conditions and assumptions.** The source count stays one, a second version immediately promotes this theme to the lineage-analysis regime. Budgeting this node's upkeep and revision triggers, live installation runtime costs belong to operators.

**Failure boundary and alternatives.** Importing the multi-source themes' sampling habits here would be over-engineering, while forgetting the sweep-scan obligation would leave the single-source condition unwatched. Bounded alternatives and recoveries: the seed's crate-slice and symbol boundaries, retained as outer limits on any single consultation's scope.

**Counterexample, gotchas, and operational comparison.** Cheap maintenance invites neglect, a theme whose upkeep costs a minute is easy to skip entirely, the discipline risk here is not cost but forgettability, keep it on the same audit schedule as the expensive themes. Good: a scheduled one-minute re-read logged beside the big themes' audits. Bad: elaborate sampling infrastructure for 58 lines. Borderline: skipping one audit cycle for an unchanged archive file, low risk, the schedule's integrity is worth the minute.

**Verification, evidence, and uncertainty.** Check audit records show wholesale re-reads at the standard cadence. The read-cost ledger from this session. Whether future sweeps end the single-source condition is the model's one open variable.

**Second-order consequence.** This theme demonstrates the corpus's workload floor, total re-verification cheaper than any sampling scheme's bookkeeping, which suggests a general sizing rule, below some source size the right maintenance strategy is always wholesale, and elaborate audit machinery is pure overhead.

**Revision decision.** Restate the model in its three cheap units and the single expensive trigger, a newer installer version arriving in a future sweep.

**Retained seed evidence.** The workload dimension rows with boundary values remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`combined_evidence_inference_note`: Treat Skill Installer Distribution Patterns as a agent workflow operating reference, not as a prose summary.

| workload_dimension_name | workload_boundary_value | verification_pressure_point |
| --- | --- | --- |
| primary_usage_surface | agent planning, tool use, context loading, delegation, or skill/plugin execution where bad guidance compounds across long-running sessions | verify that the reference changes the next implementation or review action |
| bounded_capacity_model | one primary task, up to 10 source files, up to 3 delegated subtasks, and a written completion audit for every run | split the task or create a narrower reference when this boundary is exceeded |
| source_pressure_model | local heading signals include Skill Installer; Communication; Scripts; Behavior and Options; Notes | compare guidance against canonical local sources before following external examples |
| artifact_pressure_model | required artifact is skill activation contract with progressive disclosure, misuse case, and verification gate | require the artifact before claiming the reference is operationally usable |

## Reliability Target

**Decision supported.** This section helps decide which invariants must demonstrably hold for this node's claims to stay citable. The seed document-property thresholds stand where this node's invariants should, the source file's integrity at its archive path, the runbook's citations resolving into the 58 lines, the quoted templates matching the source verbatim, the inference labels persisting on every prospective metric and extrapolated claim, and the sibling-absence claim staying current with the sweep inventory.

**Recommended default and causal basis.** Hold all five invariants on the audit cadence, with the sweep scan additionally triggered by each new monthly import. Each invariant guards a load-bearing property, integrity guards the entire evidence base, citations and templates guard operational fidelity, labels guard evidence honesty, and the sibling check guards the theme's single-source framing.

**Operating conditions and assumptions.** The archive path remains stable and sweeps remain enumerable. Invariants for this node's claims, the installer's operational reliability belongs to its operators.

**Failure boundary and alternatives.** The invariants fail toward different victims, a corrupted source silently invalidates everything downstream, drifted templates break the dialogue contracts, and dropped inference labels convert designed measurements into fabricated documentation. Bounded alternatives and recoveries: dropping the verbatim invariant and paraphrasing freely, cheaper and a direct violation of the source's own output discipline.

**Counterexample, gotchas, and operational comparison.** The inference-label invariant covers this reference's own designed metrics, its riskiest content, because they read like documentation, the labels are the only thing distinguishing synthesis from source. Good: an audit comparing both quoted templates character-for-character. Bad: a runbook quietly rewording the restart notice for style. Borderline: tightening an inference label's wording without changing its claim, fine, the label's presence is the invariant.

**Verification, evidence, and uncertainty.** Review the five invariant series at each corpus checkpoint with dated evidence. The claim structure established across this document. None about current truth, all five invariants were verified this session.

**Second-order consequence.** The verbatim-template invariant is unusually strict for prose, most themes tolerate paraphrase, but this source defines exact user-facing sentences as contracts, so this node inherits an exactness obligation from its subject, references about template-bearing sources must themselves be template-faithful.

**Revision decision.** Publish the five invariants with evidence methods, file integrity checks, citation resolution, verbatim comparison, label audits, and sweep scans.

**Retained seed evidence.** All four seed reliability rows with thresholds remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| reliability_target_name | measurable_threshold_value | evidence_collection_method |
| --- | --- | --- |
| source_boundary_preservation | 100 percent of recommendations keep local, external, and inference boundaries visible | review generated text for the three evidence labels before reuse |
| decision_accuracy_sample | at least 18 of 20 sampled uses route to the correct adopt, adapt, avoid, or adjacent-reference decision | sample downstream tasks and record reviewer verdicts |
| unsupported_claim_rate | zero unsupported production, security, latency, or reliability claims in final guidance | reject claims without source row, explicit inference note, or verification method |
| recovery_path_clarity | every avoid or failure case names the rollback, escalation, or next-reference route | inspect failure-mode and adjacent-routing sections together |

## Failure Mode Table

**Decision supported.** This section helps decide which decay modes need standing probes for a high-synthesis small-source theme. The seed generic rows miss how this node specifically dies, template drift, the quoted messages rewording through reuse until the contracts are gone, inference laundering, the designed metrics and runbook extensions losing their labels and passing as documented practice, seam-claim staleness, archive-dated upstream and platform facts quoted as current, and sibling blindness, a newer installer arriving in a sweep while this theme keeps claiming single-source status.

**Recommended default and causal basis.** Run the four probes at their trigger points, weighting label audits toward the metrics and runbook sections. All four attack the theme's differentiators, exactness, evidence honesty, dated currency, and the single-source framing, the properties that make a 58-line theme worth consulting rather than just re-reading the source.

**Operating conditions and assumptions.** Reuse is observable enough to audit, unobserved reuse defaults the label audit to fixed cadence. Decay of this node's claims and reuse, the installer's operational failures belong to its operators.

**Failure boundary and alternatives.** They compound quietly, an unlabeled inference gets quoted, the quote gets reused, and within a few hops a designed measurement is platform lore, the small theme's version of the big themes' philosophy flattening. Bounded alternatives and recoveries: shrinking the theme to pure quotation, immune to laundering and useless as an operational reference, the wrong trade.

**Counterexample, gotchas, and operational comparison.** Template drift can enter through helpfulness, an agent improving the restart notice's phrasing is drifting the contract, the probe must compare against the source, not against fluency. Good: a label audit catching the rung-distribution metric cited as documented telemetry. Bad: a year of runbook reuse with an unnoticed reworded notice. Borderline: quoting a seam fact with its date dropped for brevity, degraded, restore the date.

**Verification, evidence, and uncertainty.** Confirm each failure row names its probe and trigger point. The decay structure consolidated from this document's preceding sections. Reuse observability determines audit weighting.

**Second-order consequence.** Inference laundering is the dominant risk precisely because this theme synthesizes more than it quotes, a 58-line source cannot fill 26 sections without designed extensions, so the ratio of synthesis to source here is the corpus's highest, and the labeling discipline is correspondingly the theme's main structural defense.

**Revision decision.** Add the four rows with probes, verbatim comparison for drift, label audits for laundering, dated seam checks for staleness, and sweep scans for blindness.

**Retained seed evidence.** All four seed failure rows with mitigations remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| failure_mode_name | likely_trigger_condition | required_mitigation_action |
| --- | --- | --- |
| source drift hides truth | external or local guidance changes after the reference was written | refresh public evidence, rerun local corpus gate, and mark stale claims before reuse |
| generic advice escapes review | agent copies plausible best practices without theme-specific verification | block completion until the verification gate names concrete command, reviewer question, or metric |
| context window loses plan | long-running session forgets early constraints or overwrites user intent | write checkpoint summaries and re-read plan before each destructive step |
| tool fanout outruns budget | parallel actions create conflicts, duplicate work, or unbounded external calls | cap fanout, assign ownership, and require merge/audit checkpoints |

## Retry Backpressure Guidance

**Decision supported.** This section helps decide which failures earn another attempt, with what changed strategy, and which end the operation. The seed corpus-process bullets stand beside the source's own retry doctrine, the method ladder is a designed retry sequence, download, then git over HTTPS, then SSH, each rung triggered by the previous rung's specific failure class, with two hard stops, the existing-destination abort that no retry may bypass, and the unavailable-listing rule, explain the error and exit rather than hammer the API.

**Recommended default and causal basis.** Let the ladder run to exhaustion on transport failures and terminate immediately with explanation on state and upstream failures. Distribution retries are fallback-shaped rather than repeat-shaped, retrying the same failed method reproduces the same auth wall, so the ladder changes strategy per attempt instead of repeating one.

**Operating conditions and assumptions.** Failure classes are distinguishable from error output, opaque failures default to the ladder's next rung. Retry semantics in skill distribution, evaluation-iteration retry rules belong to the sibling theme.

**Failure boundary and alternatives.** Repeat-shaped retries against the GitHub API risk rate limiting and mask the real failure class, while retrying past the abort would convert a safety stop into an overwrite. Bounded alternatives and recoveries: the descendants' exponential-backoff doctrine for API-level politeness if bulk installation ever gets built, beyond the source's design.

**Counterexample, gotchas, and operational comparison.** User insistence reopens exactly one hard stop, the preinstalled overwrite, but never the listing failure, the two stops have different override semantics though both read as terminal. Good: an auth failure on download answered by the git rung, not a second download. Bad: retrying an aborted install by deleting the existing directory unasked. Borderline: one repeat attempt on a transient network timeout before descending the ladder, reasonable, the source is silent on transients.

**Verification, evidence, and uncertainty.** Audit failure transcripts for strategy changes rather than blind repeats. The behavior section's fallback and abort rules read this session. The scripts' internal retry behavior below the ladder is undescribed.

**Second-order consequence.** The source distinguishes recoverable from unrecoverable failures structurally, transport failures get the ladder, state conflicts and upstream absence get honest termination, encoding in 58 lines the classification that retry doctrine usually spells out in pages, what can change on the next attempt determines whether a next attempt exists.

**Revision decision.** State the ladder as strategy-changing retries with failure-class triggers and the two hard stops as retry boundaries.

**Retained seed evidence.** All five seed retry and backpressure bullets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- Retry only after the failed verification signal is classified as transient, stale evidence, missing context, or true contradiction.
- Use one bounded retry for stale external evidence refresh, then escalate to a human or a narrower source-specific reference.
- Apply backpressure by stopping new generation or implementation work when source coverage, critique coverage, or verification gates are red.
- For long-running agent workflows, checkpoint after each batch and re-read the current spec before any broad rewrite, commit, push, or destructive operation.
- For distributed execution, assign one owner per generated file or theme batch and require merge-time verification of exact path, heading, and evidence-boundary invariants.

## Observability Checklist

**Decision supported.** This section helps decide which surfaces get recorded and which is authoritative for installed state. The seed generic records stand beside what installer operation makes observable, the installed-state surface, $CODEX_HOME/skills as the ground truth the annotations read, the method actually used per install, revealing ladder position, the dialogue record, whether the four obligations appeared, and the escalation record, when sandbox network requests were made and granted.

**Recommended default and causal basis.** Treat the skills directory as ground truth, log method and dialogue where transcripts exist, and note escalations. The skill's state model is refreshingly concrete, installation truth is directory existence, so observability starts from filesystem inspection and extends through conversational and sandbox records.

**Operating conditions and assumptions.** Operators can access transcripts and the directory, sandboxed contexts may see only the conversation. Records for installer operation and this node's evidence, installed-skill runtime records belong to platform themes.

**Failure boundary and alternatives.** Each missing record blinds a specific diagnosis, no method record obscures which rung is carrying load, no dialogue record hides protocol erosion, and ignoring the directory ground truth invites the annotation staleness the custom --dest case already creates. Bounded alternatives and recoveries: platform-level install telemetry if Codex ever exposes it, unavailable at the archive date.

**Counterexample, gotchas, and operational comparison.** Directory existence proves installation but not health, a skill can land complete and still be malformed, post-landing validation belongs to the creator themes' checkers, the boundary runs exactly at directory completeness. Good: a diagnosis starting from ls of the skills directory before any log reading. Bad: trusting a stale annotation over the directory it summarizes. Borderline: inferring method from timing when logs are absent, weak evidence, label it accordingly.

**Verification, evidence, and uncertainty.** Reconstruct an install's story from the four surfaces at the next refresh. The annotation, state, and escalation descriptions read this session. Transcript availability varies by deployment and is unrecorded.

**Second-order consequence.** The annotation mechanism is the skill observing itself, listing reads local state to mark what is installed, making the catalog conversation state-aware by construction, the one place where the skill's design already implements the observability this section otherwise has to prescribe.

**Revision decision.** Adopt the four observable surfaces with the directory as primary, plus this node's own audit records established in the completeness section.

**Retained seed evidence.** All six seed observability bullets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- Record which local sources were loaded and which were intentionally skipped.
- Record the exact verification command, reviewer question, or rendered artifact used as proof.
- Record p50/p95/p99 latency or reviewer-time measurements when the reference affects runtime or workflow speed.
- Capture tool-call count, context files loaded, delegated tasks, retry count, and completion-audit outcome.
- Record leading indicator and failure signal from this file in the coverage manifest or journal when the reference drives real work.
- Keep audit evidence small enough to review: command output summary, changed-file list, and unresolved-risk notes are preferred over raw transcript dumps.

## Performance Verification Method

**Decision supported.** This section helps decide what evidence shows the distribution path is appropriately fast. The seed latency packet stands beside the source's actual performance choices, direct download as the default because it is the fast path, git sparse checkout as the fallback because it trades speed for auth compatibility, sparse rather than full checkout to fetch only the skill's subtree, and batch multi-path installs to amortize one invocation across several skills.

**Recommended default and causal basis.** Keep download-first, sparse fallbacks, and batch invocations, measuring only when installs feel slow. Distribution performance is dominated by transfer scope and round trips, so the source's choices all shrink one or the other, download skips git overhead, sparseness skips the repo bulk, batching skips repeated startup.

**Operating conditions and assumptions.** Skills stay directory-sized, a skill with huge assets changes the transfer economics at every rung. Performance of the distribution operation, installed skills' context costs belong to the platform and creator themes.

**Failure boundary and alternatives.** Inverting the defaults, git-first fetching or full clones for one skill directory, multiplies transfer cost for no resilience gain, the ladder already provides the fallback when the fast path fails. Bounded alternatives and recoveries: caching or mirroring layers for fleet-scale provisioning, beyond the source's single-user design.

**Counterexample, gotchas, and operational comparison.** Batching amortizes invocation but serializes risk, one bad path in a multi-path install complicates the partial-success story, the source is silent on partial batch failure, an honest unknown. Good: a curated install landing via direct download in one round trip. Bad: a full clone of openai/skills to obtain one directory. Borderline: pinning git method on a network that blocks downloads, correct adaptation, document the environment cause.

**Verification, evidence, and uncertainty.** Sample installs for method choice and transfer scope at review time. The defaults and sparse-checkout description read this session. Actual transfer times and the partial-batch behavior are unmeasured.

**Second-order consequence.** Sparse checkout is the design's quiet efficiency commitment, even the fallback path refuses to fetch more than the skill's subtree, so the performance principle holds at every rung, transfer scope tracks the artifact, not the repository, a rule worth exporting to any repo-subset distribution tool.

**Revision decision.** State the three performance choices with their rationales and the ladder as the mechanism that keeps the fast default safe.

**Retained seed evidence.** The method, indicator, measurement packet, and pass and fail lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Performance method: require tool-call budgets, timeout budgets, and a resumable journal when the workflow exceeds one focused session.
Leading indicator to measure: the next task uses the reference to make a better decision with less ambiguity.
Failure signal to watch: the reference remains a source map and never becomes an operating guide.
Required measurement packet: capture input size, source count, tool-call count, wall-clock time, p50/p95/p99 latency where runtime applies, and reviewer decision time where documentation applies.
Pass condition: the reference must let a reviewer identify the correct next action, verification gate, and stop condition without reading unrelated files.
Fail condition: the reference encourages implementation before the workload, reliability target, and failure-mode table are explicit.

## Scale Boundary Statement

**Decision supported.** This section helps decide at what user count, skill count, and automation level the design stops applying. The seed task-splitting bounds stand beside the design's own scale assumptions, the installer serves one user installing single-digit skills per session into one $CODEX_HOME, its consent dialogue, per-request escalation, and abort-and-ask conflict handling all assume a human in the loop, and its upstream assumption is a repository small enough to list conversationally as a numbered catalog.

**Recommended default and causal basis.** Use the installer within its conversational envelope and treat bulk or unattended needs as new design problems, not flag combinations. Every mechanism scales with conversation, listing is a numbered chat message, conflicts become questions, and installs need per-run consent, so throughput is bounded by dialogue, not bandwidth.

**Operating conditions and assumptions.** The upstream catalog stays browsable at chat scale. Bounding the installer's designed operating range, larger distribution architectures are beyond the source.

**Failure boundary and alternatives.** Past the conversational scale, fleet provisioning, hundreds of skills, unattended automation, the dialogue becomes the bottleneck and the safety semantics, ask-on-conflict, insist-to-override, have no non-interactive answer. Bounded alternatives and recoveries: provisioning scripts calling install-skill-from-github.py directly for fleet cases, mechanically possible, semantically outside the skill's consent design and to be labeled as such.

**Counterexample, gotchas, and operational comparison.** Multiple --path values look like a bulk mechanism but inherit the single consent conversation, they scale the copy, not the consent, the distinction matters exactly at the automation boundary. Good: a session installing three chosen skills through the designed dialogue. Bad: a cron job driving the consent flow with assumed yeses. Borderline: a team member installing an agreed list of eight skills in one batch, near the envelope's edge, the consent still happened once and genuinely.

**Verification, evidence, and uncertainty.** At each proposed use, check user count, catalog size, and consent shape against the envelope. The interaction model and options read this session. Where the conversational catalog limit actually sits is a usability judgment, not a documented number.

**Second-order consequence.** The numbered-list format is the upstream size bound made visible, a catalog that cannot be presented as a short numbered message with a which-ones question has outgrown the interaction model, the communication template is quietly also the scalability specification.

**Revision decision.** Name the three scale assumptions, single user, catalog-sized upstream, conversational consent, and mark everything beyond them as design territory the source does not cover.

**Retained seed evidence.** All four seed scale-boundary paragraphs remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Skill Installer Distribution Patterns stops being sufficient when the task spans multiple independent systems, more than one ownership boundary, unbounded source discovery, or production traffic without an explicit SLO.
Under distributed execution, split work by theme file and preserve one verification owner per split; do not let parallel agents rewrite the same reference without a merge checkpoint.
Under long-running agent workflows, treat context drift as a reliability failure: checkpoint state, summarize open risks, and verify against the spec before continuing.
Under large-codebase scale, require dependency or source-graph narrowing before applying this reference; a source list without ranked canonical guidance is not enough.

## Future Refresh Search Queries

**Decision supported.** This section helps decide which probes reveal decay in this node's claims and on what clocks. The seed theme-name queries would surface generic package-manager chatter while this node's staleness has four homes, the single source's integrity, the sibling-absence condition each new sweep can falsify, the five external seams, upstream layout, GitHub API, tokens, CODEX_HOME, sandbox policy, and the openai/skills repository's actual current tier structure.

**Recommended default and causal basis.** Run the integrity check and sweep scan on the standard cadence and prioritize the upstream check at every external refresh window. The in-repo evidence is one static file, so nearly all decay pressure is external, upstream reorganizations and platform changes age this theme without touching anything the repository can see.

**Operating conditions and assumptions.** External verification windows occur, without them the theme's currency claims must stay strictly archive-dated. Refreshing this node's evidence, seams, and version awareness, installed skills' freshness belongs to their own themes.

**Failure boundary and alternatives.** Internal-only refreshing would keep confirming a pristine snapshot while the upstream it describes reorganized, the purest case of the archive-versus-live gap in the whole corpus. Bounded alternatives and recoveries: declaring the theme historical and freezing all claims as 202603 facts, defensible and the honest fallback if external windows never come.

**Counterexample, gotchas, and operational comparison.** A newer installer in a future sweep would be this theme's best possible refresh event, ending single-source status and enabling the lineage analysis every claim here currently lacks, the sweep scan is watching for good news. Good: a refresh logging integrity, a sweep scan, and a dated upstream tier check. Bad: logging that skill installer searches returned nothing new. Borderline: skipping the upstream check while no one operates the installer, defensible deprioritization, record it.

**Verification, evidence, and uncertainty.** Record each probe with its date and the claim it confirmed or updated. The seam inventory and single-source structure established this session. Future sweep contents and external window availability are exactly what the probes exist to learn.

**Second-order consequence.** This theme's refresh priorities invert the twin-bearing themes, they watch in-repo diffs first, this theme has nothing in-repo to diff and must look outward or stay blind, single-source themes referencing live external systems carry the corpus's highest ratio of external to internal refresh obligation.

**Revision decision.** Replace the name queries with the four probes, integrity check, sweep scan for installer siblings, dated seam checks, and an upstream tier-structure check when external verification windows allow.

**Retained seed evidence.** The three seed query rows remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| search_query_label_name | search_query_text_value |
| --- | --- |
| `official_docs_query_phrase` | skill installer distribution patterns official documentation best practices |
| `github_repository_query_phrase` | skill installer distribution patterns GitHub repository examples |
| `release_notes_query_phrase` | skill installer distribution patterns changelog release notes migration |

## Evidence Boundary Notes

**Decision supported.** This section helps decide under what label, chain, and state each claim class here may be reused. The seed label definitions stand without this assignment's distinctive ledger, one unique document read in full, 58 lines, one sibling-absence scan run across the sweeps, zero external URLs fetched, zero scripts executed, no installation performed, no upstream repository inspected, making this the corpus's smallest evidence base supporting its highest synthesis-to-source ratio.

**Recommended default and causal basis.** Before reusing a claim, declare class, chain, and state, and treat everything not traceable to a specific line as inference by default. 26 sections built on 58 lines necessarily contain more designed extension than quotation, runbooks, drills, metrics, and scale analysis are all synthesis over a complete but tiny factual floor.

**Operating conditions and assumptions.** The source stays unedited and the labels persist through reuse, both watched by the established probes. Reuse rules for this document's claims, each claim travels with class, chain, and verification state.

**Failure boundary and alternatives.** The costliest mislabel would present any operational claim as observed, no install ran, no ladder fell through its rungs, no template was ever spoken to a user, everything behavioral here is read, not demonstrated. Bounded alternatives and recoveries: running one real installation to convert the ladder and dialogue claims to demonstrated behavior, declined to keep scope on synthesis, queued as the natural next verification step.

**Counterexample, gotchas, and operational comparison.** The theme's most quotable content, the runbook and drills, is precisely its most synthetic, popularity and evidential strength run opposite here, reuse pressure will fall hardest on the least documented claims. Good: reusing the abort rule as source fact and the rung-distribution metric as designed inference. Bad: citing the ladder's failure handling as field-tested on this document's authority. Borderline: reusing the conversational scale bound, grounded in the templates but still interpretation, carry the label.

**Verification, evidence, and uncertainty.** Sample claims from earlier sections and confirm each declares class, chain, and state cleanly. This assignment's ledger, one full read, one sweep scan, zero fetches, zero executions. Behavioral verification awaits an actual installation on a live Codex platform.

**Second-order consequence.** Small sources make evidence boundaries easier to draw and easier to violate, easier because the factual floor is fully enumerable, fifty-eight lines admit no forgotten passages, and easier to violate because filling any gap requires invention, so this theme's honesty depends less on memory than on the discipline to keep invented scaffolding labeled as such.

**Revision decision.** Publish the strata explicitly, the document's contents as same-session facts, the operational reorganizations as same-session synthesis over a complete read, the designed metrics and envelope analyses as labeled inference, and all upstream and platform state as archive-quoted and unverified.

**Retained seed evidence.** The three labeled boundary definitions remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- `local_corpus_sourced_fact`: statements tied directly to the local source paths above.
- `external_research_sourced_fact`: statements tied to the public URLs above.
- `combined_evidence_inference_note`: synthesis that combines local and public evidence into agent guidance.
