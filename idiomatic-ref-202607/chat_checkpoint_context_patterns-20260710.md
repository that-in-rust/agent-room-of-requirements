# Chat Checkpoint Context Patterns

A chat checkpoint is a persisted continuity artifact. The first decision is its purpose, because three artifacts that look similar solve different problems:

- A **conversation backup** preserves recent visible messages with high textual fidelity.
- A **resumable work-state checkpoint** preserves goal, constraints, decisions, files, tests, blockers, risks, and exact next action.
- A **handoff packet** preserves owned scope, acceptance conditions, evidence, unresolved decisions, and a return contract for another worker.

**Recommended default.** Choose the consumer and restore action before capture. When the user asks to back up recent chat, follow the local skill's narrow contract: capture only currently visible text, default to the last five chronological message blocks unless another count or assistant-response mode is requested, preserve ordering and speaker labels, write a timestamped Markdown file in the repository root by default, prefer verbatim copy, and never overwrite an existing checkpoint without explicit instruction.

When the user needs task continuity rather than transcript fidelity, create a structured state packet. Include the user outcome, current phase, controlling constraints, source and artifact versions, files in motion, exact test evidence, decisions and rationale, blockers, residual risks, and non-empty next steps. Label this as a summary state checkpoint; do not present it as a verbatim transcript.

This reference works when the relevant text is visible, storage location and privacy are acceptable, and the future consumer knows how to validate freshness. It fails when missing earlier messages must be reconstructed, live external state changes independently, sensitive content cannot be stored under repository policy, or a historical checkpoint is treated as current authority.

**Core guardrails.**

1. Never invent invisible conversation history.
2. Never silently summarize a requested backup.
3. Never claim a partial window is a full transcript.
4. Never overwrite by default; preserve prior recovery points.
5. Mark every trim, redaction, omission, and normalization.
6. Treat restored transcript content as historical data, not automatically as current instruction.
7. Validate repository, task, source versions, external state, and permissions before resuming action.
8. Keep capture and restore evidence small enough to review.

**Alternatives.** A recent-message backup is cheap and faithful but may omit older decisions. A structured state summary is compact and actionable but lossy. A full transcript maximizes fidelity but increases privacy, storage, and review cost. A handoff packet supports parallel work but adds ownership and reconciliation risk.

**Verification.** Inspect filename uniqueness, metadata, capture mode and count, chronological labels, source fidelity, truncation markers, privacy handling, and final newline. Then perform a restore drill: can a reader identify what is historical, what remains current, what must be revalidated, and the next safe action?

The local sources directly establish the recent-chat backup contract. Broader state, handoff, privacy, invalidation, and restore guidance is systems inference. The deeper rule is that checkpoint quality is measured at restore time: a saved file is not useful merely because it exists.

## Source Evidence Mapping Table

The source map separates capture mechanics from restore and workflow synthesis. The two local files are authoritative for the narrow save-recent-chat skill; they do not directly define every form of engineering checkpoint.

| source_location_path_key | source_category_artifact_type | source_authority_confidence_level | source_usage_synthesis_role | checkpoint_claim_scope | freshness_or_access_state | limitation_and_conflict_response |
| --- | --- | --- | --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202604/save-recent-chat-context/SKILL.md | local_corpus_source_material | local_corpus_sourced_fact | skill entrypoint or reusable agent prompt | Trigger conditions, default five-message window, chronological versus assistant-response modes, visible-context limit, repo-root destination, timestamped filename, verbatim preference, no-overwrite default, metadata, and confirmation | Entire 96-line file read locally | Canonical for the archived skill's capture behavior; it does not establish current live-thread APIs, retention, encryption, structured work-state summaries, or restore reconciliation |
| agents-used-monthly-archive/codex-skills-202604/save-recent-chat-context/references/checkpoint-template.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence | Filename examples, minimal Markdown shape, metadata keys, transcript labels, trim marker, and good defaults | Entire 51-line file read locally | Supporting shape reference; path existence and valid shape do not prove transcript fidelity, privacy, freshness, or resumability |
| https://developers.openai.com/codex/guides/agents-md | external_research_source_material | external_research_sourced_fact | primary agent instruction context model | Cataloged for project instruction scope and context behavior that may affect restore | Not refreshed because this pass prohibits browsing | Do not add current Codex claims; future checks must include runtime version and local applicability |
| https://docs.github.com/actions | external_research_source_material | external_research_sourced_fact | verification and automation model | Cataloged for automated integrity, retention, and artifact workflows if checkpointing becomes automated | Not refreshed because this pass prohibits browsing | Workflow mechanics do not establish semantic checkpoint quality or privacy suitability |
| https://agents.md/ | external_research_source_material | external_research_sourced_fact | general agent instruction format | Cataloged for interoperable project instruction conventions relevant to restored agent context | Not refreshed because this pass prohibits browsing | Community format cannot override local authority or turn transcript data into instructions |

**Evidence workflow.**

1. Name whether the claim concerns capture, file shape, storage, restore, handoff, retention, privacy, or automation.
2. Use the skill for capture behavior and the template for minimum shape.
3. Label broader restore, invalidation, integrity, and handoff recommendations as synthesis unless another source directly supports them.
4. Preserve public rows as unrefreshed leads in this pass.
5. Attach a verification step to both capture and restore; a valid file can still be semantically incomplete.

**Good use.** Cite the skill for the last-five visible-message default and the template for the metadata layout. **Bad use.** Claim the template proves a reader can resume an engineering task. **Borderline use.** Keep the official Codex guide as a future version check without attributing current behavior to it.

The local content and seed roles are known. Current public guidance and empirical restore reliability are unknown.

The second-order insight is asymmetric evidence. Capture and restore are different operations; a source can strongly define one and remain silent on the other.

## Pattern Scoreboard Ranking Table

The inherited values are retained for traceability. The seed provides no scorer, rubric, sample, date, or checkpoint outcomes behind 95, 91, and 88. Treat them as heuristic priority metadata, not percentages, probabilities, benchmarks, or evidence that one small score difference is meaningful.

| pattern_identifier_stable_key | inherited_pattern_score_numeric_value | pattern_tier_adoption_level | control_name_action_phrase | checkpoint_failure_prevention_target | required_restore_evidence |
| --- | ---: | --- | --- | --- | --- |
| chat_checkpoint_context_patterns | 95 | default_adoption_pattern_tier | Source Map First: distinguish visible conversation, file template, current task state, and external dependencies before capture | Prevent invented history, wrong capture mode, and use of irrelevant sources | Every captured or summarized field resolves to visible text, current state evidence, or explicit inference |
| chat_checkpoint_context_patterns | 91 | default_adoption_pattern_tier | Evidence Boundary Split: separate verbatim transcript, summary, current instruction, historical data, uncertainty, trim, and redaction | Prevent a lossy summary from masquerading as transcript or stale chat from regaining authority | Boundaries survive the saved file and restore handoff |
| chat_checkpoint_context_patterns | 88 | default_adoption_pattern_tier | Verification Gate Coupling: test file identity, content fidelity, metadata, uniqueness, privacy, freshness, and restoration | Prevent a well-formed but unusable or unsafe checkpoint from being called complete | Capture audit plus restore drill records expected and observed continuity |

**Recommended adoption.** Use all three as one pipeline. Source mapping without boundary labels can copy historical instructions as current authority. Labels without verification can document an incomplete capture. A restore drill built on invented or stale source material tests the wrong continuity.

**Alternative treatment.** Replace unexplained scores with required, recommended, and contextual tiers, or recover a rubric and rescore against representative cases: chronological capture, assistant-response mode, trim, collision, sensitive text, stale checkpoint, changed repository, and handoff.

**Good use.** A checkpoint records its visible source window, marks a trim, never overwrites, and restores only after current-state validation. **Bad use.** "Source Map First is 95 percent reliable." **Borderline use.** Capture fidelity passes, but no one tests whether the next action is still valid.

**Verification.** Sample each recommendation for mapped source, fidelity boundary, and restore evidence. Report missing-control count and severity rather than averaging the values.

The score facts are known; provenance is not. The deeper consequence is conjunctive reliability: one missing authority or restore control can dominate several high structural scores.

## Idiomatic Thesis Synthesis Statement

**local_corpus_sourced_fact:** The archived save-recent-chat-context skill and template define a lightweight conversation backup. They specify a default window of five visible chronological message blocks, an assistant-response mode with an adjacent user prompt when needed, timestamped repo-root Markdown, mostly verbatim text, speaker order, metadata, trim marking, confirmation, and a no-overwrite default.

**external_research_sourced_fact:** Three public sources are cataloged for agent instruction context, automation, and an open instruction format. They were not refreshed in this no-browsing pass.

**combined_evidence_inference_note:** Reliable checkpointing is a lifecycle with separate capture and restore evidence:

1. **Purpose:** Decide whether the consumer needs transcript fidelity, resumable work state, or a handoff.
2. **Capture:** Use only visible or otherwise authorized source material; preserve order, boundaries, and loss markers.
3. **Persist:** Choose an authorized destination, create a unique immutable artifact, and record identity metadata.
4. **Validate:** Check count, labels, source fidelity, trims, redactions, privacy, and file integrity.
5. **Restore:** Treat transcript as historical data, reconcile repository and task identity, revalidate external state, permissions, tests, and unresolved decisions, then choose the next safe action.
6. **Invalidate:** Mark checkpoints stale or superseded when controlling sources, artifacts, owners, or external state change.
7. **Retain or delete:** Apply repository and organizational privacy policy rather than keeping chat forever by default.

This pattern works when the source window is sufficient and the consumer can validate current state. It fails when invisible history must be invented, the stored text is unsafe for the destination, or changing external state is omitted.

**Good synthesis.** A five-message transcript backup is labeled partial and verbatim; a separate TDD state checkpoint records failing tests and next action. **Bad synthesis.** Any Markdown file is called a complete resumable context. **Borderline synthesis.** Capture is faithful but the repository and test state changed; restore must pause for reconciliation.

**Verification.** Prove capture fidelity and restore validity separately. A checkpoint can pass one and fail the other.

The local capture behavior is known. Restore, invalidation, retention, and distributed handoff guidance is systems inference. The deeper consequence is lifecycle ownership: checkpoint completion at write time is only provisional until a restore consumer can safely use it.

## Local Corpus Source Map

The local corpus uses progressive disclosure: the skill entrypoint defines behavior and guardrails; the template supplies a ready-made filename and Markdown shape.

| local_source_filepath_value | local_source_title_text | local_source_heading_signals | local_source_usage_role | direct_checkpoint_contribution | unsupported_or_silent_area | hierarchy_and_verification |
| --- | --- | --- | --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202604/save-recent-chat-context/SKILL.md | save-recent-chat-context | Save Recent Chat Context; Default Behavior; Workflow; File Contract; Chat Checkpoint; Transcript | skill entrypoint or reusable agent prompt | Trigger semantics; five-visible-message default; chronological and assistant-response modes; source-of-truth rule; repo-root timestamped destination; no overwrite; mostly verbatim content; metadata; confirmation; guardrails; progressive loading | Full-thread export, hidden-history reconstruction, structured engineering-state summary, encryption, retention, deletion, restore reconciliation, multi-agent merge, and live implementation details | Canonical primary source for the archived skill version; verify every behavioral claim against the complete file |
| agents-used-monthly-archive/codex-skills-202604/save-recent-chat-context/references/checkpoint-template.md | Checkpoint Template | Checkpoint Template; Filename Pattern; Minimal File Shape; Chat Checkpoint; Transcript; 01 user | reference detail file for deeper pattern evidence | Filename pattern and examples; minimal metadata; transcript heading; numbered speaker labels; direct-copy preference; explicit trim marker; Markdown, repo-root, no-overwrite, and local-time defaults | Capture-mode selection rationale, current-thread access mechanics, privacy policy, summary-state schema, restore validation, and lifecycle ownership | Supporting detail source; compare with entrypoint whenever either file changes |

**Direct source facts.**

- Default count is five visible messages when no count is provided.
- "Messages" or "turns" means chronological speaker blocks; "responses" means assistant messages, with an immediately preceding user prompt when needed for clarity.
- The active visible conversation is the source of truth; missing earlier text must not be invented.
- The default filename is chat-checkpoint-YYYYMMDD-HHMMSS.md in the repository root.
- Existing checkpoints are not overwritten unless explicitly requested.
- Backup text remains mostly verbatim; intentional shortening uses a visible trim marker.
- Confirmation reports path, capture mode and count, and any normalization or trimming.

**Bounded synthesis.** A structured resume or handoff checkpoint may borrow metadata and immutability, but it should use a distinct mode and schema. Do not attribute tests, blockers, or next-step fields to the chat backup skill when the source does not contain them.

**Good use.** The entrypoint controls count and mode while the template controls layout. **Bad use.** An example timestamp is treated as current metadata. **Borderline use.** A work-state summary uses the template shape but clearly labels itself summary_state and adds restore fields.

**Verification.** Cross-check source links, duplicated defaults, filename, metadata, labels, and overwrite rules. Progressive disclosure is useful only while entrypoint and detail remain consistent.

Both file contents are known. Their maintenance owner and any current runtime implementation are not established here.

## External Research Source Map

No public source was opened during this pass. These rows are a future evidence plan, not support for new current claims.

| external_source_url_value | external_source_name_text | external_source_usage_role | evidence_boundary_label_value | checkpoint_decision_it_may_support | decision_it_cannot_set_alone | required_refresh_record |
| --- | --- | --- | --- | --- | --- | --- |
| https://developers.openai.com/codex/guides/agents-md | OpenAI Codex AGENTS.md guide | primary agent instruction context model | external_research_sourced_fact | Current project-instruction discovery and scope that may affect restored context for a compatible Codex version | What visible chat existed, repository privacy policy, or current task authority | Retrieval date, relevant section, documented version, installed-version comparison, restore test |
| https://docs.github.com/actions | GitHub Actions documentation | verification and automation model | external_research_sourced_fact | Current automation, artifact, workflow, permissions, or retention mechanics if checkpoints are processed in GitHub Actions | Semantic checkpoint completeness, privacy suitability, or restore correctness | Retrieval date, feature/version, workflow fixture, permissions, retention setting, observed artifact |
| https://agents.md/ | AGENTS.md open format | general agent instruction format | external_research_sourced_fact | Interoperable project-instruction conventions that a restored agent may need to rediscover | Local precedence, transcript authority, or user storage consent | Retrieval date, format revision if available, runtime compatibility, local conflict review |

**Recommended use.** Refresh the Codex guide for a current instruction-scope question, GitHub Actions documentation for a concrete automation or artifact question, and the open format for interoperability. Then validate the finding locally.

**Failure boundaries.** Browsing is prohibited in this evolution. Public pages may change or describe versions unlike the installed tool. Automation documentation does not prove that checkpoint content is sufficient, private, or current.

**Good use.** A future workflow records the current artifact-retention behavior and tests a non-sensitive fixture. **Bad use.** "GitHub Actions supports artifacts, therefore repo chat checkpoints are safe and resumable." **Borderline use.** A current official instruction page is found but local runtime compatibility remains untested.

**Verification.** Record access result, date, version, relevant finding, affected lifecycle rule, local compatibility, contradiction, and stop state.

The URLs and seed roles are known. Current content is unknown. A useful search starts from one unresolved capture, storage, restore, or retention claim rather than the broad phrase "checkpoint best practices."

## Anti Pattern Registry Table

A checkpoint anti-pattern is operational only when it has a trigger, observable signal, safer replacement, containment, and recovery proof.

| anti_pattern_failure_name | failure_cause_risk_reason | detection_signal_review_method | safer_default_replacement_pattern | containment_and_recovery |
| --- | --- | --- | --- | --- |
| context_free_summary_output | Summary omits the task, constraints, evidence, or next action needed by its consumer | Restore drill cannot identify a safe next step | consumer_driven_checkpoint_contract | Mark unusable, return to visible/current sources, and create a correctly labeled state packet |
| unsourced_recommendation_claims | Checkpoint presents inference or reconstructed history as observed conversation | Claims cannot trace to visible text or current state | source_boundary_checkpoint_ledger | Split fact, summary, inference, and unknown; do not invent missing content |
| unverified_agent_instruction | Saved file is called complete without fidelity or restore evidence | Only path existence or Markdown shape is checked | capture_restore_dual_verification | Withdraw completeness and run both audits |
| invisible_history_reconstruction | Earlier conversation is no longer visible but is recreated from memory | Checkpoint contains text outside the available source window | visible_context_only_capture | Remove invented text, mark the missing interval, and ask for another source if required |
| silent_summary_substitution | User requested backup but content is paraphrased | Wording differs materially and capture mode still claims transcript | verbatim_backup_default_mode | Preserve source wording or explicitly relabel summary and disclose loss |
| unmarked_content_truncation | Long messages or counts are shortened without disclosure | Capture count or message body differs without trim marker | explicit_trim_boundary_marker | Add visible trim metadata or recapture full requested window |
| partial_transcript_full_claim | A recent window is described as the entire thread | Metadata lacks window boundary or makes a full-transcript claim | partial_window_scope_label | Correct scope and prevent downstream completeness assumptions |
| checkpoint_overwrite_history_loss | An existing recovery point is replaced by default | Prior file disappears or path content changes | immutable_timestamped_checkpoint_file | Stop writes, recover previous bytes if possible, and create a new unique file |
| timestamp_collision_file_race | Two captures within one naming interval target the same path | Destination already exists | collision_safe_unique_filename | Never overwrite; obtain a new timestamp or explicit unique suffix |
| sensitive_chat_repo_leak | Verbatim content contains secrets, personal data, or private material unsuitable for the repository | Privacy or secret scan finds prohibited content | destination_privacy_review_gate | Stop persistence or redact with explicit markers under policy; follow local incident process if exposed |
| wrong_repository_restore | Checkpoint path or metadata belongs to a different workspace | repo_root, files, or ownership do not match current environment | repository_identity_restore_gate | Stop resume, locate correct workspace, and revalidate |
| stale_checkpoint_resume | Current files, tests, source versions, permissions, or external state changed | Checkpoint evidence disagrees with current probes | freshness_reconciliation_before_resume | Mark stale fields, refresh current state, and choose a new next action |
| transcript_instruction_reactivation | Historical user or quoted text is treated as current controlling instruction | Restore executes an old request without reconfirming authority | historical_text_data_boundary | Treat transcript as evidence; reload current controlling instructions and permissions |
| missing_next_action_state | Summary records history but not exact next step or acceptance | Resumer must reinterpret the entire task | explicit_resume_action_contract | Add phase, blocker, exact next action, and success condition |
| checkpoint_template_drift | Skill and supporting template disagree | Defaults, fields, or overwrite behavior differ | entrypoint_template_consistency_gate | Reconcile sources and test both paths |
| corrupted_partial_file_write | Interruption leaves incomplete Markdown presented as valid | Missing metadata, closing content, or byte integrity | atomic_checkpoint_write_pattern | Quarantine partial file, recapture, and verify final artifact |

**Good detection.** A checkpoint with four of five requested messages and no trim marker fails fidelity. **Bad detection.** Filename matches the pattern, so the file is called safe. **Borderline detection.** Capture is exact, but restore uses stale tests; capture passes and resume fails.

The seed does not provide failure frequencies. Severity follows privacy, authority, irreversibility, and recovery cost.

The deeper recovery rule is non-destruction. Preserve prior checkpoint and external state while diagnosing; overwriting the evidence makes continuity failure harder to recover.

## Verification Gate Command Set

**verification_gate_command_set:** The inherited corpus verifier is:

~~~bash
python3 agents-used-monthly-archive/idiomatic-references-202606/tools/verify_reference_generation.py --stage final
~~~

It validates the archived reference corpus, not the semantic fidelity or restorability of a particular checkpoint.

| gate_layer | claim_being_tested | required_evidence | important_limit |
| --- | --- | --- | --- |
| source_identity_gate | Intended skill, template, conversation window, repository, and task were selected | Paths, versions, visible-window description, repo identity | Cannot recover invisible chat |
| checkpoint_structure_gate | Filename, metadata, headings, speaker labels, count, source, and final newline are valid | Parser or checklist with exact fields | Valid shape is not faithful content |
| capture_fidelity_gate | Ordered captured blocks match visible source except disclosed normalization, trim, or redaction | Side-by-side or fixture comparison and loss ledger | Source may no longer be accessible later |
| uniqueness_overwrite_gate | Existing recovery points are preserved and collisions do not overwrite | Preexisting-file fixture and resulting path inventory | Unique name does not prove semantic uniqueness |
| privacy_destination_gate | Content and destination comply with repository and organizational rules | Secret/privacy scan, policy review, redaction record | Automated scanners miss contextual sensitivity |
| integrity_completion_gate | File write completed and bytes remain intact | Size, parse result, optional digest or atomic-write evidence | Byte integrity does not prove meaning |
| freshness_reconciliation_gate | Repository, files, tests, versions, permissions, owners, and external state still match | Current probes compared with checkpoint metadata | Some external state may be unavailable |
| historical_authority_gate | Restored transcript is treated as historical evidence, not automatic current instruction | Resume plan reloads current controlling instructions | Authority review can require a human owner |
| restore_usability_gate | Consumer can identify current phase, reliable evidence, unresolved risk, and next safe action | Timed restore drill and reviewer verdict | Transcript backup may intentionally lack work-state fields |
| handoff_ownership_gate | Delegated checkpoint preserves exact owned scope and acceptance | Ownership and return-contract review | Does not guarantee integration correctness |

**Capture fixture.** Test default five-message chronology, explicit count, assistant-response mode with needed prompt, trim marking, collision, no-overwrite, and partial-window labeling.

**Restore fixture.** Change one file, one test result, and one permission after capture. The restorer should mark those fields stale, preserve historical transcript, and derive a new safe next action rather than replaying the old one.

**Good evidence.** Exact source blocks, metadata, no overwrite, privacy pass, and successful reconciled restore are reported separately. **Bad evidence.** "Saved successfully" proves only that a write was attempted. **Borderline evidence.** Optional digest matches, but the checkpoint belongs to another repository; integrity passes and restore fails.

For each gate, record command or reviewer rule, expected result, observed result, failure interpretation, and rerun condition. Verification evidence should be stored with the checkpoint or in a durable index so future consumers can assess trust.

## Agent Usage Decision Guide

**agent_usage_decision_guide:** Use this reference when the user asks to back up recent chat, preserve a resume point, hand work to another agent, or recover after context loss. Do not create a checkpoint merely because a conversation is long.

**Capture procedure.**

1. **Name the consumer and purpose.** Backup, resume, audit, or handoff determines required fidelity and fields.
2. **Choose the mode.**
   - chronological_messages: visible user and assistant blocks in order;
   - assistant_responses: assistant blocks plus an immediately preceding user prompt when needed;
   - summary_state: goal, phase, constraints, decisions, files, tests, blockers, risks, and next action;
   - handoff_state: summary state plus owned scope, acceptance, return contract, and integrator.
3. **Choose the window.** Use the user's count. For recent chat with no count, default to five visible messages. Do not reconstruct missing text.
4. **Review destination and privacy.** Default local skill behavior is repo root, but controlling policy and explicit user destination govern. Check sensitive content before persistence.
5. **Select a unique path.** Use the timestamp pattern and never overwrite by default; handle collisions with a new unique name.
6. **Capture with boundaries.** Preserve order and speaker labels. Mark trims, redactions, omitted intervals, and normalization.
7. **Validate.** Check structure, count, source fidelity, uniqueness, privacy, and write completion.
8. **Confirm.** Report path, mode, requested and actual count, and every trim or normalization.

**Restore procedure.**

1. Select by task and repository identity, not newest timestamp alone.
2. Read metadata and identify whether content is transcript, summary, or handoff.
3. Treat historical text as data; reload current controlling instructions and permissions.
4. Reconcile repository, branch or revision when relevant, files, tests, owners, versions, and external state.
5. Mark stale or conflicting fields instead of silently choosing.
6. Derive the next safe action from current evidence.
7. Record restore result, residual uncertainty, and whether the checkpoint is active, stale, superseded, or invalid.

**Good use.** The user asks for a backup; five visible messages are copied mostly verbatim and the path plus count are reported. **Bad use.** Ten messages are reconstructed from memory and called a full transcript. **Borderline use.** The user wants to resume a failing test, but a five-message transcript omits exact test state; create a summary_state packet instead.

**Route elsewhere.** Use a live thread API or export tool when a full transcript is required and available. Use a TDD progress journal for exact phase and tests. Use a security or privacy process when content is sensitive. Use distributed-work coordination when multiple owners must merge state.

The two-phase model prevents a common failure: capture success is not restore authorization.

## User Journey Scenario

Role based opening scenario: An agent-system designer sees continuity risk in an active task and must decide whether the user needs a recent conversation backup, a resumable work-state summary, or a handoff packet.

Primary user starting state: The user has a chat_checkpoint_context_patterns need, visible recent messages, a repository destination, and uncertainty about capture fidelity, privacy, and what a later agent will require.

Decision being made: Choose checkpoint mode and window, what can be stored, how to preserve loss boundaries, how to verify the file, and how a future consumer will reconcile current state before action.

Reference opening trigger: Open this file when the user asks to save recent chat, preserve a resume point, hand off work, or recover continuity. Do not checkpoint by habit when the current answer or existing task journal already provides sufficient state.

**Capture moment.**

1. The user states backup, resume, audit, or handoff intent.
2. The agent selects transcript, assistant-response, summary-state, or handoff mode.
3. It confirms count or uses the five-visible-message backup default.
4. It reviews destination, repository policy, and sensitive content.
5. It captures only visible or otherwise authorized evidence, preserving labels and ordering.
6. It marks every trim, redaction, omission, and summary boundary.
7. It creates a unique non-overwriting file, validates it, and reports path, mode, count, and losses.

**Restore moment.**

1. The consumer selects by task and repository identity rather than timestamp alone.
2. It distinguishes transcript, summary, and handoff semantics.
3. It treats chat as historical evidence and reloads current instructions.
4. It probes current repository, files, tests, owners, permissions, versions, and external state.
5. It marks stale and conflicting fields.
6. It derives the next safe action, records residual uncertainty, and updates status.

**Good path.** A five-message backup is saved mostly verbatim; days later a restorer sees changed test state, keeps the transcript as history, and chooses a new next action. **Bad path.** The newest checkpoint is opened and an old request to mutate state is executed without current permission. **Borderline path.** The capture includes sensitive credentials visible in chat; pause persistence or apply policy-approved redaction with explicit markers rather than silently changing the backup.

**Success condition.** The capturer can prove what was saved and disclosed. The restorer can prove what remains current and what action is authorized. These are separate success criteria.

The local source directly supports the capture journey. Restore and lifecycle guidance is synthesis. The two-user model prevents a common blind spot: an artifact optimized only for the capturer may be unusable or unsafe for the restorer.

## Decision Tradeoff Guide

Choose a branch using purpose, source visibility, fidelity, privacy, destination, retention, consumer needs, current-state volatility, and recovery cost.

| decision_option_name | when_to_choose_condition | tradeoff_cost_description | required_evidence | verification_question_prompt | revisit_trigger |
| --- | --- | --- | --- | --- | --- |
| Adopt recent backup | User wants recent visible chat preserved, repo-root storage is acceptable, and verbatim fidelity matters | Low setup and strong local fidelity, but limited window and potential sensitive content | Visible window, count, destination review, no-overwrite path, fidelity audit | Does the file contain exactly the requested accessible window with disclosed losses? | New privacy, destination, or scope requirement |
| Adapt to summary state | Consumer needs decisions, tests, blockers, risks, and next action more than exact wording | Compact and actionable, but lossy and vulnerable to author interpretation | Explicit summary label, source references, uncertainty, current-state fields, restore drill | Is every omitted detail either irrelevant to resume or visibly marked? | Consumer needs exact wording or source dispute arises |
| Adapt to handoff state | Another worker needs owned scope and acceptance evidence | Supports delegation, but adds ownership, merge, and stale-state risk | Exact ownership, constraints, evidence, return contract, integrator | Can the receiver work independently and return reviewable proof? | Ownership or dependency changes |
| Pause for evidence | Count, source visibility, destination policy, privacy, owner, or current state is unresolved | Delays capture or restore while preventing unsafe persistence or action | Named missing decision, owner, safe interim state | What evidence moves this to adopt, adapt, avoid, or route? | Evidence or consent arrives |
| Avoid persistence | Content is too sensitive, storage is unauthorized, or artifact adds no continuity value | Avoids leakage and clutter but sacrifices a recovery point | Privacy or utility decision plus alternative continuity method | Is non-persistence safer and is necessary state preserved elsewhere? | Destination or need changes |
| Route to export or storage tool | Full thread, encryption, retention controls, indexing, or shared live state is required | Stronger capability and governance, but more tooling and access cost | Tool authority, data policy, export scope, integrity and access controls | Does the specialized system own the requirement the local file cannot meet? | Tool availability or policy changes |
| Cost of being wrong | Wrong checkpoint can leak data, erase history, replay stale instructions, or send work down a false next step | Includes disclosure, reconstruction, rework, state damage, and trust loss | Sensitivity, overwrite risk, staleness, action consequence, recovery owner | Can the error be contained, reconstructed, and safely revalidated? | New external state or irreversible action |

**Mode tradeoff.** Verbatim capture maximizes textual fidelity but costs review and privacy. Summary maximizes scanability but loses wording and may encode bias. Full export increases coverage and storage cost. Handoff improves ownership but increases reconciliation. None is universally best.

**Destination tradeoff.** Repo root is the local skill default and keeps artifacts near the task, but it may be tracked, synchronized, or broadly visible. Another location may offer stronger controls but requires explicit user direction and discoverability.

**Good adaptation.** A work resume is labeled summary_state and links to the transcript backup. **Bad adoption.** Sensitive visible chat is copied into a public repository because repo root is the default. **Borderline pause.** Policy is unclear; do not persist until an owner resolves destination or redaction.

**Verification.** Record branch, purpose, source window, losses, destination, privacy, current-state volatility, restore consumer, error cost, and revisit trigger.

The second-order insight is orthogonality: checkpoint mode and destination are separate decisions. A faithful artifact can still be stored unsafely, while a secure file can still be semantically inadequate.

## Local Corpus Hierarchy

Classification vocabulary includes canonical, supporting, inferred, legacy, duplicate, conflicting, provisional, and silent. Assign roles per checkpoint claim.

| local_source_filepath_value | corpus_hierarchy_role | claim_scope | heading_signal_to_convert | reviewer_question_to_answer | conflict_or_gap_action |
| --- | --- | --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202604/save-recent-chat-context/SKILL.md | Canonical primary source for archived recent-chat capture behavior | Trigger, count, mode, source visibility, destination, filename, no-overwrite, fidelity, metadata, confirmation, guardrails, progressive loading | Save Recent Chat Context; Default Behavior; Workflow | Does this recommendation reproduce the complete archived skill behavior without extending its authority? | Preserve explicit behavior; label restore, privacy, retention, and distributed additions as inference |
| agents-used-monthly-archive/codex-skills-202604/save-recent-chat-context/references/checkpoint-template.md | Supporting detail source for file shape | Filename examples, metadata layout, transcript headings, numbered speakers, trim marker, good defaults | Checkpoint Template; Filename Pattern; Minimal File Shape | Does the shape remain consistent with the entrypoint and clearly identify capture mode? | Reconcile any duplicate-field drift against the skill entrypoint |

**Claim roles beyond the files.**

- **Inferred:** Structured work-state schema, restore reconciliation, invalidation, atomic writing, privacy review, retention, deletion, indexing, and multi-agent merge guidance in this reference.
- **Silent:** The local sources do not decide encryption, secret handling policy, repository tracking, live-thread API behavior, or current external state.
- **Conflicting:** Any future skill and template defaults that differ.
- **Provisional:** A locally tested restore rule that lacks canonical documentation.

**Default conflict procedure.** Treat the entrypoint as controlling for duplicated capture behavior, preserve the template's illustrative role, inspect current implementation if available, and ask the maintainer when a material mismatch remains. Do not choose whichever source is shorter or newer without scope evidence.

**Good hierarchy.** No-overwrite comes from SKILL.md; filename shape comes from the template; stale-state reconciliation is labeled inference. **Bad hierarchy.** "Repo root" becomes proof the destination is safe for secrets. **Borderline hierarchy.** An added summary_state field proves useful in restore drills but remains provisional until adopted by the skill owner.

**Verification.** Compare links, duplicated defaults, metadata, trim behavior, examples, and fixtures. Progressive disclosure saves context only while entrypoint and detail stay synchronized.

The source bytes and relationship are known. Maintenance ownership and live version are not. The deeper protection is explicit silence: canonical labels should not hide policy the source never addressed.

## Theme Specific Artifact

Theme specific artifact: context budget policy for prompt, file, memory, and sub-agent handoff.

The concrete form is a checkpoint manifest plus one mode-specific payload. A transcript backup may use only the shared and transcript fields; resume and handoff artifacts require current-state and ownership fields.

| artifact_field_name | artifact_completion_rule | evidence_source_hint | failure_if_missing |
| --- | --- | --- | --- |
| checkpoint_identity_unique_key | Unique path or ID, created time with zone, creator, and non-overwrite state | Local filename contract | Recovery points collide or cannot be referenced |
| repository_task_identity | Repository root, task/thread identifier when available, user goal, and phase | User journey and restore gate | Wrong workspace or task is resumed |
| checkpoint_mode_capture_type | chronological_messages, assistant_responses, summary_state, or handoff_state | Local skill plus bounded synthesis | Consumer assumes the wrong fidelity |
| source_window_boundary | Visible source, requested and actual count, first/last labels, unavailable interval | Local capture rules | Partial context appears complete |
| fidelity_loss_disclosure | Verbatim, normalized, summarized, trimmed, or redacted fields and reasons | Skill guardrails and template trim marker | Loss is hidden |
| destination_privacy_decision | Destination, tracking/sync visibility, sensitivity review, redaction policy | Decision tradeoffs | Chat is persisted unsafely |
| controlling_instruction_snapshot | References to current controlling instructions at capture time, labeled historical on restore | Evidence boundaries | Transcript instructions regain authority |
| artifact_version_source_state | Relevant file paths, revisions or digests when useful, tests, tools, and external-state observations | Restore verification | Staleness cannot be detected |
| decision_rationale_summary | Explicit decisions, alternatives rejected, uncertainty, and why next step follows | Summary-state synthesis | Consumer repeats settled debate or cannot audit branch |
| blocker_risk_register | Blockers, unresolved owner questions, permission limits, and residual risks | Failure modes | Resume acts through known risk |
| exact_next_action_contract | One next action, owner, prerequisite, expected evidence, and stop condition | Resume workflow | Consumer must reinterpret history |
| handoff_ownership_acceptance | Owned paths, prohibited paths, acceptance checks, return format, integrator | Distributed workflow | Parallel work conflicts or cannot merge |
| restore_validation_rules | Repository, instruction, file, test, permission, version, and external-state probes | Verification gate set | Historical state is replayed blindly |
| lifecycle_status_marker | active, stale, superseded, invalid, archived, or deleted plus reason and successor | Lifecycle synthesis | Multiple checkpoints compete as truth |
| retention_deletion_policy | Review date, retention owner, secure deletion or archival rule under local policy | Privacy boundary | Sensitive artifacts accumulate forever |

**Filled transcript example.**

- mode: chronological_messages
- source: active visible thread
- requested_count: 5
- actual_count: 5
- fidelity: mostly verbatim
- loss: whitespace normalized; no trim or redaction
- destination: unique repo-root timestamped Markdown after privacy review
- restore rule: historical transcript only; reload current instructions and task state

**Filled resume example.**

- goal: make one failing integration test pass within two owned files
- phase: Red
- current evidence: named test and exact failure
- decisions: request validation stays at the boundary
- blocker: fixture credential absent; owner is user
- next action: obtain authorized fixture, rerun one test, stop if credential remains absent
- restore rules: verify repository, branch/revision when relevant, file digests, test status, permission, and fixture availability
- status: active until any controlling input changes

A paired transcript and state packet often gives better fidelity than forcing both purposes into one file. A machine-readable manifest improves indexing and linting but adds schema migration and can encourage mechanical completion.

**Verification.** Every field must change a capture, restore, handoff, privacy, or lifecycle decision. Run a restore drill after changing one file, test result, and permission. The checkpoint must mark stale fields and derive a safe current action.

The expanded schema is synthesis. Its second-order purpose is truth management: immutable files remain useful only when status and supersession prevent several recovery points from masquerading as equally current.

## Worked Example Set

The cases use one task: preserve recent work before context loss, then resume after a file and test result change.

**Good example.**

- **Purpose:** Preserve exact recent conversation and actionable engineering state.
- **Capture:** Five visible chronological messages are copied mostly verbatim to a unique file; a separate summary_state block names goal, Red phase, failing test, owned files, blocker, and exact next action.
- **Loss disclosure:** One whitespace normalization is reported; no trim or redaction.
- **Privacy:** Destination is reviewed and contains no prohibited sensitive content.
- **Change before restore:** One file changes and the formerly failing test now passes.
- **Restore:** Transcript remains historical. File and test fields are marked stale; current instructions and permissions are reloaded; next action becomes inspect the new passing change rather than implement the old fix.
- **Verdict:** Capture passes and restore passes.

**Bad example.**

- **Purpose:** Claimed full continuity.
- **Capture:** Ten messages are reconstructed although only five are visible, summarized without a mode label, and written over an older checkpoint.
- **Loss disclosure:** None.
- **Privacy:** A secret visible in chat is copied into a tracked repository.
- **Restore:** The newest timestamp is selected blindly and an old mutation request is executed.
- **Verdict:** Capture, privacy, history preservation, authority, and restore all fail.

**Borderline case.**

- **Purpose:** Verbatim recent backup.
- **Capture:** Exactly five visible messages, correct labels, unique file, and complete metadata.
- **Privacy:** One sensitive token is present; storage policy is unclear.
- **Restore need:** Consumer expects exact failing-test state, which the transcript window does not contain.
- **Correct interim action:** Pause persistence or apply authorized explicit redaction; create a separate summary_state only from current verified evidence.
- **Promotion to good:** Privacy owner approves destination or redaction, and state packet passes restore.
- **Rejection to bad:** Persist silently or claim the transcript is sufficient for task resume.

**Second contrast: trim.** A good checkpoint marks a shortened long message and reports actual count. A bad one silently truncates. A borderline one links to an authorized full source and includes enough visible context; accept only if the consumer can retrieve that source.

**Third contrast: handoff.** A good handoff names exact ownership and acceptance. A bad handoff sends chat prose and lets two agents edit the same file. A borderline handoff has disjoint files but one shared unresolved schema; keep schema ownership centralized.

**Verification.** Score capture fidelity, privacy, identity, non-overwrite, freshness detection, authority, and restore usability separately. One axis can pass while another fails.

The deeper example pattern is dual verdict. "Checkpoint succeeded" is ambiguous unless capture and restore results are reported independently.

## Outcome Metrics and Feedback Loops

Leading indicator: on comparable continuity events, a future consumer reconstructs the current safe next action with less avoidable clarification and less unrelated rereading, while fidelity, privacy, and stale-state detection remain acceptable.

Failure signal: files are created successfully, but captures hide loss, overwrite history, leak content, or restore stale instructions and state.

| metric_name | operational_definition | collection_method | interpretation_limit | feedback_action |
| --- | --- | --- | --- | --- |
| capture_fidelity_rate | Requested visible blocks preserved in order and substance divided by eligible blocks | Source-to-file fixture comparison | Normalization rules affect judgment | Tighten copy and loss disclosure |
| undisclosed_loss_rate | Trims, summaries, omissions, or redactions not marked divided by observed losses | Audit and adversarial fixtures | Some source may no longer be available | Require explicit loss ledger |
| overwrite_collision_rate | Existing artifacts modified or naming collisions mishandled per capture | Preexisting-file and concurrent fixture | Filesystem semantics vary | Strengthen unique naming and atomic write |
| sensitive_content_violation_rate | Checkpoints persisted contrary to policy or without required redaction/consent | Secret/privacy review | Automated scans miss context | Change destination, minimization, or approval |
| repository_task_identity_error | Restores selecting the wrong repository, task, or owner | Restore audit | Identity metadata can itself be stale | Strengthen selection and current probes |
| stale_field_detection_rate | Changed files, tests, versions, permissions, or external facts correctly marked stale | Controlled change fixture | Cannot simulate every external state | Expand high-risk probes |
| restore_next_action_accuracy | Restores choosing the reviewer-approved current next action | Scenario review | Reviewer disagreement matters | Improve state fields and reconcile conflicts |
| restore_usability_rate | Consumer can identify phase, trustworthy evidence, blockers, risks, and next action | Timed restore drill | Transcript backups may not target work resume | Measure by mode |
| historical_authority_violation | Restores treating transcript content as current instruction without reconfirmation | Adversarial old-request case | Authority models vary | Strengthen historical-data boundary |
| resume_review_time | Time to select, read, reconcile, and act safely | Timed drill with task cohort | Faster can mean skipped checks | Pair with correctness and stale detection |
| handoff_conflict_rate | Delegated work colliding on ownership or acceptance | Merge and review record | Complex work naturally costs more | Improve ownership and return contract |
| recovery_completeness_rate | Failed captures/restores with containment, preserved evidence, owner, correction, and rerun | Failure audit | Some disclosure is irreversible | Strengthen prevention and incident route |
| checkpoint_storage_profile | File count, bytes, age, sensitive class, active/stale status, and review burden | Index or repository audit | Small storage can still contain high sensitivity | Apply retention, archival, or deletion policy |

**Measurement protocol.** Define checkpoint mode, task cohort, source window, expected restore, change fixture, numerator, denominator, baseline, reviewer, and correction policy. Include failure and stale cases.

**Good evidence.** A restore catches changed tests and selects a new next action. **Bad evidence.** Ten checkpoint files means continuity improved. **Borderline evidence.** Resume time drops because freshness checks are skipped; reject the optimization.

No baseline in the seed establishes current values. The closed loop matters: undisclosed loss changes capture, stale misses change restore probes, privacy failures change destination or minimization, and handoff conflict changes ownership. Stop collecting metrics that never change policy.

## Completeness Checklist

Use this checklist twice: once before accepting the saved file and again before using it to resume or hand work to another agent. A checkpoint can pass capture fidelity while failing resumability. Record those verdicts separately instead of calling the artifact simply complete.

**Mode and intended outcome**

- [ ] The artifact declares whether it is a transcript backup, a resumable work-state checkpoint, or a cross-agent handoff. It does not imply all three by using the generic word "checkpoint."
- [ ] The intended consumer, repository or workspace, task identity, and reason for capture are named. A personal quotation backup may omit engineering state, but it must then say that it is not a resume record.
- [ ] The consequence of a wrong restore is understood. Higher-risk continuations require stronger freshness, ownership, privacy, and verification evidence than low-impact reading notes.

**Capture source and fidelity**

- [ ] The source is the currently visible active-thread text unless another source is explicitly named. The local skill does not authorize reconstruction of messages that are no longer visible.
- [ ] The capture count and selection rule are stated. The local default is the last five visible chronological messages; when "responses" means assistant responses, include a preceding user prompt when it is needed for meaning.
- [ ] Speaker labels and chronological order are preserved. Transcript text is mostly verbatim, and every summary, normalization, omission, or inference is visibly distinguished from quoted conversation.
- [ ] Any shortened passage is marked `[trimmed for length]`. A partial capture is labeled partial; it is not presented as a complete conversation history.
- [ ] The role scenario, decision guide, source hierarchy, worked examples, and outcome metrics in this reference remain internally consistent with the selected mode.

**Privacy, destination, and persistence**

- [ ] The selected text has been reviewed for credentials, personal data, customer material, proprietary code, and other destination-sensitive content before it is written.
- [ ] Redaction is disclosed without reproducing the removed secret. When safe redaction would destroy the checkpoint's purpose, change the destination or do not create the artifact.
- [ ] The destination is authorized for the content and expected retention period. A repository-root Markdown file is a local default, not permission to place sensitive text in version control.
- [ ] The filename is unique and timestamped with local time in the documented `chat-checkpoint-YYYYMMDD-HHMMSS.md` form, unless the user requested another safe destination.
- [ ] No existing checkpoint was overwritten. On collision, generate a new path and preserve both lineages until a reviewer deliberately resolves them.
- [ ] The required metadata is present: local creation time, repository root, capture mode, capture count, source, and transcript. Resume and handoff modes add the state fields defined in the theme-specific artifact.

**Work state and handoff integrity**

- [ ] Changed paths, artifact status, decisions, assumptions, blockers, risks, and verification evidence are current as of a stated observation time.
- [ ] The exact next action is executable and bounded. "Continue implementation" is insufficient; name the next file, check, decision, or command and its expected evidence.
- [ ] Historical user instructions are retained as provenance but are not treated as irrevocable authority. The latest applicable user instruction and current repository policy govern restoration.
- [ ] One owner or integrator is named when multiple agents could act on the same state. Conflicting checkpoints are reconciled rather than silently merged.
- [ ] Status and lineage are explicit: active, stale, superseded, invalid, archived, or deleted. A replacement points back to the artifact it supersedes.

**Restore verification**

- [ ] The consumer confirms the repository and task identity before following any mutation instruction.
- [ ] Current file state, branch or workspace state where relevant, tests, external dependencies, and blocking conditions are probed again. Captured observations remain historical evidence, not live truth.
- [ ] The consumer distinguishes immutable transcript facts from summarized work state, inferred rationale, and fresh restore-time observations.
- [ ] The checkpoint's next action is still authorized, non-conflicting, and consistent with current instructions. If not, mark the artifact stale or superseded and record the replacement decision.
- [ ] At least one representative restore drill demonstrates that the artifact leads a cold reader to the correct next action without relying on unrecorded memory.

**Verdict and corrective action**

- [ ] Capture verdict is recorded as pass, conditional, or reject, with evidence pointers for every conditional or rejected item.
- [ ] Restore verdict is recorded independently. Transcript-only artifacts may pass capture and be rejected for resumption without being defective for their stated purpose.
- [ ] Hard failures such as invented source text, undisclosed loss, sensitive exposure, overwrite, wrong task identity, or destructive stale replay trigger recapture, redaction, relocation, reconciliation, or invalidation before use.
- [ ] The adjacent routing section points to a full export, progress journal, security process, verification record, or handoff protocol when this reference is not the correct evidence owner.
- [ ] A recurring failure changes the schema, destination policy, or capture and restore workflow. Repeated reviewer warnings are not an adequate control.

The checklist is complete only when its evidence supports the artifact's declared purpose. File existence and syntactic Markdown establish persistence, not trustworthy continuity.

## Adjacent Reference Routing

Route by the claim that needs an authoritative owner, not by whichever title also contains "chat," "checkpoint," or "context." This reference owns bounded visible-conversation capture and the bridge between captured text and safe restoration. It should link to specialized evidence rather than becoming a second, stale copy of every related artifact.

The categories below are functional routes. Confirm the actual local reference, tool, access policy, and retention behavior before using one; the local capture skill and template do not themselves establish organization-specific adjacent destinations.

| trigger | route to | minimum outgoing payload | expected return | this reference stops when |
| --- | --- | --- | --- | --- |
| The user needs more history than is currently visible, a complete export, or platform-level conversation recovery | Authorized full transcript or conversation-export workflow | Thread identity, requested time or message range, destination constraints, and authorization | A complete or explicitly partial export with provenance and access details | The request exceeds the visible-text contract; do not reconstruct missing messages locally |
| The primary need is exact red, green, refactor status, changed paths, commands, failures, and next tests | TDD progress journal or task-state reference | Task identity, current phase, known test evidence, and journal path | A structured current-state checkpoint with nonempty next steps | Engineering progress, rather than conversation wording, becomes the authoritative payload |
| The decision depends on current branch, diff, worktree, generated artifacts, or repository ownership | Repository-state and version-control workflow | Repository root, relevant paths, expected branch or workspace, and mutation constraints | Fresh command evidence and an explicit state verdict | Live source state can be probed; captured chat remains historical context only |
| Transcript text may contain credentials, customer data, personal data, regulated material, or proprietary content | Security, privacy, or data-handling policy | Data classification question and intended destination, without repeating suspected secrets | Redaction, destination, access, and retention decision | The checkpoint cannot be saved safely under the current destination policy |
| Work moves between agents or several agents may mutate overlapping files | Subagent or multi-agent handoff protocol | Scope, exclusive paths, completed work, blockers, exact next action, and proposed owner | Accepted ownership, conflict boundaries, and integration plan | More than one actor could reasonably believe it owns the same next mutation |
| The record must explain an incident chronology, production action, approval, or rollback | Incident or operational evidence system | Event time, actor, affected system, observed result, and relevant checkpoint link | An append-only operational timeline or approved action record | Audit-grade chronology and operational authority exceed a chat checkpoint's purpose |
| Checkpoints require managed retention, discovery, access control, encryption, or deletion at scale | Approved artifact or records-management store | Classification, owner, lifecycle state, retention need, and integrity metadata | Stable locator, access policy, retention rule, and deletion or archival mechanism | A repository-root Markdown file no longer satisfies lifecycle or confidentiality requirements |
| The main question is whether a claim, test, benchmark, or recovery behavior is true | Verification or evidence reference | Claim, preconditions, expected observation, and relevant artifact locator | Reproducible command or review evidence with a scoped verdict | The checkpoint has supplied context and the claim now requires independent proof |
| The task is a contested architecture choice with meaningful alternatives | Decision or debate reference | Decision statement, constraints, alternatives, evidence, and unresolved disagreements | An owner-approved decision record and rejected alternatives | Conversation preservation is no longer the dominant need |

**Routing protocol**

1. Name the dominant continuity question: exact conversation wording, executable work state, current repository truth, privacy authorization, ownership, operations, storage lifecycle, or claim verification.
2. Declare one authoritative owner for each volatile claim. The checkpoint may summarize that claim for navigation, but it must link to the owner and preserve the observation time.
3. Send the smallest payload the adjacent workflow needs. Do not duplicate an entire transcript into a security ticket, or an entire test journal into a conversation backup, when a locator and bounded excerpt suffice.
4. Record the expected returned evidence before routing. "Consult the verification reference" is not complete; state whether the checkpoint needs a test result, permission decision, owner acceptance, stable locator, or other concrete return.
5. Check that the intended consumer can access the returned artifact for the required lifetime. A private or expiring link is not a usable handoff merely because the creator can open it.
6. On restore, probe the route again. If it is unavailable, stale, superseded, or conflicts with a newer authority, do not fill the gap from memory. Use a declared fallback, request access, or mark the checkpoint conditional or invalid.

**Composition boundaries**

- A full transcript and a resume-state record may be paired, but transcript facts and inferred work state must remain visibly distinct.
- A progress journal should own test phase and exact next steps when TDD continuity is the purpose; this checkpoint should link to it and preserve only enough bridge context to explain why it matters.
- Current repository commands outrank captured claims about files, branches, and tests. The checkpoint records what was observed, when, and where the fresh evidence now lives.
- Security policy outranks convenience. If safe routing is uncertain, withhold or redact the content rather than copying it into multiple candidate stores.
- One integrator owns convergence when adjacent handoffs disagree. Do not silently merge conflicting next actions into a synthetic instruction.

**Route rejection signals** include a circular referral, no named evidence owner, an inaccessible return artifact, weaker destination permissions, unexplained duplication, conflicting repository identity, or a route that does not change the next decision. In those cases, keep a minimal explicitly bounded local record, escalate ownership, or stop until the correct destination is known.

Good routing reduces the number of independently changing copies. It does not maximize the number of links. Measure success by whether a cold consumer can locate the authoritative evidence, understand its scope, and resume without reconstructing an undocumented join across artifacts.

## Workload Model

`combined_evidence_inference_note`: Treat Chat Checkpoint Context Patterns as an agent workflow operating reference, not as a prose summary. The numeric values below are conservative planning guardrails inherited from the seed. They are not measured universal limits, context-window capacities, or guarantees of a correct restore.

The workload unit is one coherent restore decision: a bounded body of conversation and state that one consumer can validate and turn into one authorized next action. Storage bytes are rarely the first constraint. The practical constraints are source review, privacy inspection, freshness probes, authority reconciliation, and the number of joins needed to recover intent.

| workload_dimension_name | default boundary or signal | verification pressure point | split or route trigger |
| --- | --- | --- | --- |
| `primary_usage_surface` | agent planning, tool use, context loading, delegation, or skill and plugin execution where bad guidance compounds across long-running sessions | verify that the reference changes the next implementation or review action | the artifact becomes passive archive material with no bounded resume decision |
| `bounded_capacity_model` | one primary task, up to 10 source files, up to 3 delegated subtasks, and a written completion audit for every run | cold-read the artifact and confirm one owner can reconcile every source into the correct next action | any count is exceeded, or a lower-count workload crosses an authority, privacy, repository, or volatility boundary |
| `visible_message_volume` | use the local default of the last five visible chronological messages unless the user specifies a different visible selection | compare order, speaker labels, capture count, omissions, and trim markers against the visible source | the user requires invisible history, a complete export, or more text than can be reviewed faithfully |
| `source_pressure_model` | local heading signals include Save Recent Chat Context; Default Behavior; Workflow; File Contract; Chat Checkpoint; Transcript; Checkpoint Template; Filename Pattern; Minimal File | compare capture guidance against the canonical local skill and template before relying on broader synthesis | mapped sources disagree, lack provenance, or do not govern the claim being made |
| `source_size_and_shape` | record both count and approximate size or type; ten small stable files are not equivalent to ten generated logs | sample the actual source distribution and measure omitted or misunderstood evidence during restore | large generated outputs, binary artifacts, or repeated logs dominate review and should be summarized with locators |
| `repository_scope` | one repository or workspace identity per resumable checkpoint by default | verify root, relevant paths, and current state before executing the next action | the checkpoint spans independently versioned repositories without a parent manifest and integrator |
| `checkpoint_age` | record creation and observation time; no age alone establishes freshness | replay restore drills after realistic delays and measure stale-state detection | changed code, instructions, owners, credentials, or external dependencies invalidate the proposed action |
| `external_state_volatility` | prefer captured identifiers and observation times over copied live values | probe current API, issue, deployment, permission, or service state before use | the action depends on state that changes faster than the checkpoint review cycle |
| `handoff_fan_out` | up to three delegated subtasks only when scopes are disjoint and one integrator owns convergence | compare accepted ownership and returned evidence against the parent task | multiple agents can mutate the same files, issue conflicting next actions, or bypass one integration owner |
| `restore_fan_in` | one root artifact should identify every authoritative evidence owner needed for the next decision | count unresolved joins, inaccessible links, and conflicting authorities in a cold restore | the consumer must infer how several artifacts combine or cannot locate one required authority |
| `privacy_class` | one compatible data-handling and retention policy per destination | inspect selected text and destination permissions before writing; test redaction disclosure | regulated, secret, customer, personal, or proprietary content requires a different store or no capture |
| `artifact_pressure_model` | required artifact is a checkpoint manifest with mode-specific transcript, state, handoff, restore, and lifecycle fields | require the artifact and a capture or restore verdict before claiming operational usability | a free-form note cannot expose source boundaries, authority, freshness, or exact next action |
| `lifecycle_volume` | a small set may use unique timestamped files; repeated use needs status and lineage | detect collisions, stale active records, missing supersession, inaccessible owners, and expired retention | manual discovery can no longer identify the current artifact reliably |

**Initial operating tiers**

| tier | suitable workload | required controls | exit condition |
| --- | --- | --- | --- |
| Bounded transcript backup | One visible conversation selection, one destination, no resumability claim | Exact source window, chronological labels, mostly verbatim text, disclosed trimming or redaction, unique path | Invisible history, complete export requirements, or destination sensitivity requires another workflow |
| Bounded resume checkpoint | One task, one repository, up to ten moderately sized sources, and one exact next action | Transcript/source distinction, current state block, verification evidence, privacy review, restore probes, and one owner | Independent task, repository, security, or authority domains appear |
| Coordinated handoff | One parent task and up to three disjoint delegated subtasks with an integrator | Exclusive scopes, accepted ownership, returned evidence, conflict checks, and parent-child lineage | More than three active handoffs, overlapping writes, or no convergence owner |
| Managed checkpoint set | Repeated checkpoints whose discovery, access, or retention exceeds manual review | Index, stable identity, status, supersession, access control, integrity checks, retention, and deletion process | Move to an approved records or artifact platform when repository files cannot satisfy policy or scale |

**Decomposition order**

1. Split first across incompatible authority or privacy boundaries; those cannot be repaired by a larger context budget.
2. Split next by independent task and repository, giving each child one owner and executable next action.
3. Separate volatile live state from durable conversation evidence. Link to fresh probes rather than copying values that will age quickly.
4. Add a root manifest when splitting would otherwise force the consumer to discover parent-child relationships or join many tiny artifacts from memory.
5. Preserve lineage in both directions: each child identifies its parent decision, and the parent records each child's owner, status, and returned evidence.

**Counterexamples**

- A 2 MB immutable transcript can be straightforward archival work if it has one source, one privacy policy, and no action claim. It may exceed a byte guideline without exceeding restore complexity.
- A ten-line checkpoint can be overloaded if it combines two repositories, a credential-dependent deployment, conflicting agent ownership, and an unverified production action.
- Ten source files do not satisfy the default merely because the count is within bounds. One generated log, sensitive export, or independently changing service may trigger an earlier split or route.
- Three delegated subtasks are not safe when their file scopes overlap. Conversely, more read-only research subtasks may be manageable in a purpose-built indexed workflow, but that requires observed evidence before raising this reference's guardrail.

**Calibration method**

Build restore fixtures that vary visible message count, source bytes and type, repositories, checkpoint age, external volatility, handoff fan-out, privacy class, and number of evidence joins. Test immediately below, at, and above each proposed boundary. Record capture completion, disclosed loss, privacy findings, review time, stale-state detection, unresolved joins, wrong next actions, and recovery effort. Tune boundaries from those restore outcomes, not from write speed or file existence.

Until representative trials justify a change, exceeding the guardrail means split the task, route specialized evidence, or create a narrower checkpoint. High-impact privacy, authority, or stale-action risk can require the same response even below the numeric limits.

## Reliability Target

These are acceptance policies for this reference and its checkpoint workflow, not observed production results. Preserve the target, cohort, mode, denominator, severity, and evidence locator together. Do not report a percentage when those fields are unavailable.

| reliability_target_name | measurable_threshold_value | evidence_collection_method | status and enforcement |
| --- | --- | --- | --- |
| `source_boundary_preservation` | 100 percent of recommendations keep local, external, and inference boundaries visible | review generated text for the three evidence labels before reuse | Seed policy target; block reuse when a claim's provenance changes the decision and is missing |
| `decision_accuracy_sample` | at least 18 of 20 sampled uses route to the correct adopt, adapt, avoid, or adjacent-reference decision | sample downstream tasks, preserve mode and consequence, and record independent reviewer verdicts and disagreements | Seed sampled target; investigate both misses and any unresolved rubric dispute rather than generalizing beyond the cohort |
| `unsupported_claim_rate` | zero unsupported production, security, latency, or reliability claims in final guidance | reject claims without a source row, explicit inference note, or verification method | Seed hard stop; remove, qualify, or verify the claim before reuse |
| `recovery_path_clarity` | every avoid or failure case names the rollback, escalation, or next-reference route | inspect failure-mode, retry, and adjacent-routing sections together and execute representative recovery drills | Seed hard stop for operational guidance; a named but unusable route does not pass |
| `visible_source_fidelity` | 100 percent of selected visible messages retain chronological order, speaker identity, and disclosed omission or trimming | compare the checkpoint against the selected visible source window using exact-count and order checks | Checkpoint policy target; recapture or invalidate on invented, reordered, or silently omitted source text |
| `capture_scope_disclosure` | 100 percent of artifacts state source, capture mode, capture count, and whether the record is partial | validate required metadata and compare the claim of completeness with the available source | Checkpoint policy target; an unlabeled partial capture cannot be promoted to a complete transcript |
| `existing_artifact_preservation` | zero existing checkpoint files overwritten without explicit authorization | create a collision fixture and verify that a new unique path is selected while both lineages remain intact | Hard stop; restore the prior artifact where possible and create a new checkpoint under a unique identity |
| `sensitive_content_violation` | zero unauthorized credentials, personal data, customer material, or restricted content written to the destination | run destination-appropriate privacy review with safe fixtures and inspect redaction disclosure without logging raw secrets | Hard stop; contain exposure, follow the applicable incident process, and relocate, redact, or delete under policy |
| `task_identity_match` | 100 percent of resume attempts confirm repository or workspace and task identity before mutation | inject wrong-root and wrong-task fixtures and record whether the restore gate blocks action | Hard stop for mutation; reconcile identity or mark the checkpoint invalid for the current task |
| `historical_authority_safety` | zero resume attempts execute superseded user instructions or captured mutations without checking current authority | change instructions between capture and restore and observe whether the newer applicable instruction wins | Hard stop; stop the action, record the conflict, and produce a superseding decision |
| `stale_state_detection` | 100 percent of injected material changes to files, tests, owners, permissions, or external dependencies are detected before the affected action | run restore drills with one changed dependency at a time and record detection, containment, and replacement action | Predeployment policy target for covered fixtures; production claims require representative observed cohorts |
| `next_action_accuracy` | at least 18 of 20 representative resumable checkpoints lead a cold reviewer to the correct bounded next action | compare the chosen action with an independently prepared expected outcome and retain reviewer disagreements | Initial sampled objective aligned with the seed decision sample; calibrate by mode and consequence before broader claims |
| `handoff_conflict_containment` | 100 percent of injected overlapping ownership cases stop parallel mutation until one integrator resolves scope | create conflicting owner and file-scope fixtures and inspect accepted ownership plus reconciliation evidence | Hard stop for shared mutations; no majority success rate can waive one unresolved overlap |
| `recovery_execution_success` | every detected hard failure has a tested containment and a named path to recapture, redact, relocate, reconcile, supersede, archive, or invalidate | execute representative recovery paths and verify final artifact status and lineage | Policy target; measure recovery separately from initial failure detection |

**Severity rules**

- Hard-stop events are not averaged into an overall success rate. One fabricated transcript passage, unauthorized disclosure, overwrite, wrong-task mutation, or destructive stale replay blocks acceptance for the affected artifact.
- Sampled objectives are appropriate for usability outcomes such as routing accuracy, resume time, or reviewer clarity. Report numerator, denominator, mode, workload distribution, uncertainty, exclusions, and reviewer disagreement.
- A transcript-only backup is not penalized for lacking engineering-state fields when it explicitly disclaims resumability. A resume checkpoint is evaluated against both capture and restore targets.
- Faster restoration is favorable only when stale detection, identity confirmation, privacy controls, and next-action accuracy remain stable. Skipping those checks is not a performance improvement.

**Collection protocol**

1. Predeclare the checkpoint modes and consequence classes in the cohort.
2. Include successful, partial, collision, privacy, wrong-identity, stale-state, inaccessible-route, instruction-change, and ownership-conflict fixtures.
3. Deduplicate repeated observations of the same incident and retain rejected cases in the denominator where the target requires them.
4. Separate automated structural checks from semantic reviewer verdicts. Record disagreement rather than forcing consensus after the fact.
5. Run recovery after failure injection and confirm final status, lineage, and safe next action.
6. Review trends only after verifying that mode mix, source distribution, destination policy, and exclusion rules have not drifted.

The local corpus supplies capture behavior and the seed supplies the four original policy values. It does not supply a baseline showing these targets have already been achieved. Until representative evidence exists, report them as gates and objectives, not measured reliability claims.

## Failure Mode Table

Classify failures by lifecycle phase and consequence before retrying. For hard integrity, privacy, identity, authority, or ownership failures, stop affected mutations, preserve non-sensitive evidence, and change artifact status before attempting recovery.

| failure_mode_name | phase and likely trigger | detection signal | immediate containment | required recovery and postcondition |
| --- | --- | --- | --- | --- |
| `source drift hides truth` | Reference or restore: external or local guidance changes after the reference or checkpoint was written | Source hash, version, current instruction, or observed behavior differs from captured provenance | Mark affected claims stale and block dependent action | Refresh authorized evidence, rerun the local corpus or current-state gate, supersede invalid claims, and record the new observation time |
| `generic advice escapes review` | Reference authoring: plausible best practices are copied without checkpoint-specific verification | No source boundary, concrete command, reviewer question, fixture, or metric supports the recommendation | Block completion and prevent promotion as operational guidance | Add claim-scoped provenance, boundaries, counterexample, and verification; otherwise remove or label the statement as unresolved judgment |
| `context window loses plan` | Long-running capture or restore: early constraints or newer user intent fall outside attention | Current action conflicts with saved scope, exclusive paths, checkpoint mode, or latest instruction | Stop broad or destructive work and reread current authoritative instructions plus the latest state record | Write a bounded checkpoint with exact next action, reconcile conflicts, and mark older instructions historical or superseded |
| `tool fanout outruns budget` | Delegation or restore: parallel actions create conflicts, duplicate work, or unbounded calls | Overlapping paths, duplicate artifacts, divergent next actions, unexpected call volume, or no integrator | Stop new fan-out, preserve each result, and assign one convergence owner | Reconcile scopes and evidence, invalidate conflicting actions, and resume only with explicit ownership and bounded fan-out |
| `invisible source reconstruction` | Capture: requested history is no longer visible and the creator fills gaps from memory or inference | Checkpoint claims completeness beyond the observable source window or contains unverifiable messages | Reject the transcript claim and prevent it from becoming handoff evidence | Recapture only visible text with a partial label, or route to an authorized full-export workflow; never invent the missing history |
| `silent transcript transformation` | Capture: messages are summarized, reordered, normalized, or shortened without disclosure | Source comparison finds changed wording, speaker order, omissions, or missing `[trimmed for length]` markers | Mark capture fidelity failed and block verbatim or complete-history claims | Recapture mostly verbatim text, disclose summaries and redactions, preserve chronology, and record an updated capture verdict |
| `checkpoint collision or overwrite` | Write: a timestamp collision, reused path, or convenience edit replaces an existing artifact | Destination exists, prior content hash changes, or lineage has two creators under one identity | Abort the write and preserve both the prior artifact and attempted payload | Generate a new unique identity, link lineages where needed, and verify the original remains byte-for-byte intact unless explicit overwrite authorization exists |
| `sensitive content exposure` | Capture or storage: credentials, personal data, customer material, or restricted code is written to an unauthorized destination or log | Privacy scanner, manual review, access audit, or inert test marker detects disallowed content | Stop distribution and further logging; preserve only safe incident metadata | Follow applicable security or privacy handling, revoke or rotate where required, redact or relocate safely, and set final artifact status under policy |
| `wrong repository or task identity` | Restore: a checkpoint from another root, branch, worktree, or task is mistaken for current state | Metadata and current environment disagree, referenced paths are absent, or task owner rejects the identity | Block every mutation and do not adapt paths by guesswork | Locate the correct artifact or explicitly rebase the context through fresh inspection and owner approval; invalidate the mismatched restore attempt |
| `stale state drives action` | Restore: files, tests, dependencies, permissions, owners, or external services changed after capture | Fresh probe contradicts captured state or the next action's precondition no longer holds | Mark the checkpoint stale for the affected claim and stop dependent action | Reinspect current state, rerun relevant verification, write the replacement decision, and supersede or narrow the old checkpoint |
| `historical instruction replays as authority` | Restore: an old user request or mutation command is followed despite a newer applicable instruction | Instruction chronology shows conflict, or current policy forbids the captured action | Stop before mutation and escalate ambiguity to the current owner or user | Record which instruction governs now, retain the older text as provenance only, and issue a new bounded next action |
| `adjacent route becomes unusable` | Handoff or restore: linked evidence is deleted, permissioned differently, expired, moved, or superseded | Consumer cannot access the locator or finds a newer authoritative artifact | Mark the route conditional and block claims that depend on it | Restore access under policy, locate the superseding artifact, or create a minimal authorized snapshot with explicit loss and provenance |
| `checkpoint copies diverge` | Storage or handoff: several artifacts independently summarize the same volatile state | Conflicting test status, owner, file list, or next action appears under active status | Stop convergence by majority vote and name one integrator | Identify one authority per claim, reconcile from fresh evidence, supersede stale copies, and update the root manifest |
| `partial or corrupt write appears complete` | Write: interruption, disk failure, or non-atomic workflow leaves a truncated artifact | Required metadata, final delimiter, section count, checksum, or parse validation fails | Quarantine the incomplete path and prevent restore | Recreate under a new identity from preserved source, validate completeness and integrity, and retain or remove the corrupt file according to policy |
| `handoff ownership collides` | Delegation: two actors accept overlapping files or both believe they own integration | Scope manifests overlap, concurrent diffs touch exclusive paths, or next actions conflict | Pause affected writers and preserve both work products without overwriting | Assign one integrator, reconcile changes explicitly, update ownership, and record which checkpoint supersedes the conflicting instructions |
| `retention or indexing loses current truth` | Lifecycle: many checkpoint files accumulate without status, owner, supersession, or deletion handling | Search returns several active candidates, orphaned artifacts, expired records, or missing current pointers | Stop automatic resume from ambiguous search results | Build or repair the index, resolve active lineage, apply retention and deletion rules, and verify the consumer finds exactly the intended artifact |

**Failure interaction rules**

- Treat compound failures as a cascade, not as independent checklist misses. A stale checkpoint with conflicting ownership can propagate a wrong action across several files even when each defect alone appears recoverable.
- Prefer barriers early in the lifecycle: source-window disclosure before capture, privacy review before write, collision checks before persistence, identity and freshness probes before restore, and ownership acceptance before mutation.
- Do not place raw conversation or sensitive payloads in diagnostic logs. Record event identity, field name, safe hash or count where useful, status transition, and evidence locator.
- A warning without a status change is insufficient when another consumer can still discover the artifact as active. Use conditional, stale, superseded, invalid, archived, or deleted states deliberately.
- Recovery is complete only after the safe postcondition is verified: the original was preserved, exposure was contained under policy, the correct task was identified, current state was probed, one owner was accepted, or the defective artifact can no longer authorize action.

Verify the table with inert fault fixtures for missing visible history, silent trimming, collisions, restricted markers, wrong roots, changed files and tests, changed instructions, inaccessible routes, truncated writes, and overlapping scopes. Add compound cases, then assert no unauthorized mutation, no overwrite, no sensitive payload in telemetry, explicit lineage, and a tested recovery path.

## Retry Backpressure Guidance

Retry only after the failed signal is classified. A retry repeats the same logically idempotent operation after a transient condition changes. Recapture, writing under a new identity, reconciling current state, rerouting evidence, and requesting an owner decision are different recovery operations and should be recorded as such.

| failure classification | retry decision | required preconditions | backpressure and escalation |
| --- | --- | --- | --- |
| Transient local read or validation failure | Allow one bounded retry | Source remains intact; operation is read-only or idempotent; no partial mutation occurred; repository and task identity still match | Stop after the second failure and inspect the environment rather than looping |
| Ambiguous write timeout | Do not immediately repeat the write | Probe destination, artifact identity, size, integrity, and lineage to determine whether the first attempt completed | Quarantine partial output; if a new write is needed, use a new unique path and verify the prior artifact remains intact |
| Existing filename or identity collision | Never retry the same create operation against the occupied identity | Preserve the existing file and choose a fresh timestamp or collision-resistant identity | Escalate if lineage is ambiguous or explicit overwrite was requested without clear authority |
| Partial or corrupt checkpoint file | Do not repair it as though it were a trusted source | Preserve original visible source or an independently valid payload; mark the file invalid or quarantined | Recreate under a new identity, validate the whole artifact, and apply retention policy to the corrupt copy |
| Missing invisible conversation history | No retry and no reconstruction | Confirm what remains visible and whether an authorized export workflow exists | Save only a clearly partial visible capture or route to full export; ask the user when purpose cannot be met safely |
| Transcript fidelity failure | Recapture rather than replaying the same transformed payload | Re-read the visible source; preserve order and speaker labels; disclose trimming, redaction, and summaries | Block transcript-complete and resumability claims until comparison passes |
| Sensitive-content finding | No automatic retry | Stop further writes and raw logging; determine applicable privacy or security handling | Contain and follow policy, then redact, relocate, or decline capture; an ordinary retry budget does not apply |
| Wrong repository or task identity | No mutation retry | Establish the correct root, task, artifact, current instruction, and owner | Mark the attempted restore invalid for this context and request clarification if identity cannot be proven |
| Stale file, test, dependency, permission, or external state | Reconcile, then reconsider the action; do not merely rerun the captured command | Probe current state, identify changed preconditions, and confirm current authority | Mark stale claims, write a replacement decision, and use one bounded refresh attempt only when the owning external workflow defines it as safe |
| True contradiction between sources or instructions | No retry until authority is resolved | Preserve both claims, chronology, provenance, and affected action | Escalate to the current owner or user; record the governing decision and supersede the losing action without erasing history |
| Temporarily inaccessible adjacent artifact | One delayed access retry may be reasonable | Consumer permission is expected, locator is still authoritative, and no mutation depends on unverified content | Request access, locate a superseding artifact, or degrade to an explicit partial checkpoint after the bounded attempt |
| Handoff ownership conflict | No distributed write retry | One integrator accepts ownership and reconciles overlapping scopes | Freeze affected fan-out, preserve both work products, and resume only after an explicit scope update |
| Repeated structural validation failure | Stop generation for the affected artifact | Identify whether the schema, generator, source data, or validator expectation is wrong | Fix the failed assumption and rerun from a preserved source; repeated formatting attempts without diagnosis consume evidence and attention |

**Bounded retry protocol**

1. Record the failed operation, artifact identity, time, safe error class, and any observable side effect. Do not copy raw transcript or sensitive content into telemetry.
2. Classify the failure as transient, ambiguous side effect, collision, missing source, fidelity, privacy, identity, stale state, contradiction, route access, corruption, or ownership.
3. Confirm idempotency. A timeout is not proof that an operation failed; inspect state before repetition.
4. Re-read the latest applicable user instruction, current repository policy, and active checkpoint status. A once-valid action may have become unauthorized while waiting.
5. Preserve the source and prior artifact. Never make retry success depend on overwriting the only evidence of the failed attempt.
6. Execute at most the action allowed by the classification table. For the generic transient case, the default budget is one bounded retry; service-specific policies require verified local contracts.
7. Verify the final state: artifact count, identity, integrity, lineage, privacy, owner, current-state probe, and absence of duplicate mutation.
8. Record whether the result is active, conditional, stale, superseded, invalid, archived, or deleted, plus the exact next action.

**Backpressure rules**

- Stop dependent generation or implementation when source coverage, privacy review, identity, authority, ownership, or restore verification is red. Read-only diagnosis that cannot propagate the failed assumption may continue under explicit scope.
- Stop new fan-out when two agents can touch the same files, when returned evidence conflicts, or when no integrator owns convergence.
- For long-running workflows, checkpoint after each bounded batch and reread the current specification before a broad rewrite, commit, push, publication, deletion, or other high-impact operation.
- For distributed execution, assign one owner per generated file or theme batch and verify exact path, heading, lineage, and evidence-boundary invariants at integration time.
- Release backpressure only when evidence shows the failed precondition changed: access is restored, a unique path is selected, current state is reconciled, privacy handling is authorized, or one owner accepts scope. A quieter error signal alone is insufficient.

Test retry behavior with timeouts before and after write completion, occupied paths, truncated files, inaccessible links, changed instructions, stale files and tests, restricted inert markers, and overlapping agent scopes. Assert bounded attempts, no overwrite, no duplicate action, no raw sensitive payload in logs, preserved evidence, explicit final status, and a safe recovery path.

## Observability Checklist

Observe the lifecycle without creating a second transcript store. Routine telemetry should explain what operation occurred, which artifact and task it concerned, what safe evidence supported the decision, and how status changed. It should not copy raw conversation, credentials, personal data, proprietary payloads, or a private internal reasoning transcript.

**Core correlation fields**

- [ ] Stable checkpoint identifier and parent or superseded identifier where lineage exists.
- [ ] Task and repository or workspace identifiers that are safe for the destination.
- [ ] Capture mode: transcript backup, resumable work state, or cross-agent handoff.
- [ ] Lifecycle phase and status: requested, selected, reviewed, writing, validated, active, conditional, stale, superseded, invalid, archived, or deleted.
- [ ] Actor or owner role, delegated subtask identifier, and integrator when shared execution applies.
- [ ] Local event time plus sequence or parent-event identifier when clock order may be ambiguous.
- [ ] Schema version, safe result code, retry classification, and bounded attempt number.
- [ ] Safe evidence locator, count, size, or digest only when it has a documented comparison and retention purpose.

| lifecycle event | emit when | minimum safe evidence | invariant to inspect |
| --- | --- | --- | --- |
| `capture_requested` | The user or workflow requests a checkpoint | Requested mode, destination class, task identity, requester role | No write begins before mode and destination are known |
| `source_window_selected` | Visible messages or other authorized sources are chosen | Visible count, chronological range descriptor, loaded local source identifiers, intentionally skipped source identifiers | Claimed scope does not exceed observable or authorized source material |
| `privacy_review_completed` | Selected content and destination are assessed | Review result, classification, redaction-present flag, policy locator | A failed review prevents ordinary persistence and does not log the sensitive payload |
| `checkpoint_write_attempted` | A unique destination is prepared | Proposed artifact identifier, path class, collision result, attempt number | Existing content is never silently overwritten |
| `checkpoint_write_completed` | Persistence returns success | Artifact identifier, safe size, integrity result, destination class | Success is provisional until structural and fidelity validation pass |
| `checkpoint_validation_completed` | Required metadata, structure, source fidelity, and mode fields are checked | Validation profile, pass or failure classes, evidence locator | A rejected artifact cannot transition directly to active |
| `handoff_ownership_recorded` | Work moves between actors | Sender, receiver, accepted scope, overlapping-path result, integrator | One owner controls each mutation boundary |
| `restore_started` | A consumer attempts to use the artifact | Consumer role, artifact status, current task and repository identity | Mutation remains blocked until identity, authority, and freshness checks complete |
| `restore_probe_completed` | Current files, tests, instructions, permissions, or external state are checked | Probe class, safe result, changed-precondition flag, evidence locator | Captured historical state is not treated as live truth |
| `stale_or_conflict_detected` | A material change, authority conflict, or ownership overlap appears | Affected field class, severity, blocked-action flag, owner | Status changes and dependent action stops |
| `resume_decision_recorded` | The consumer chooses continue, adapt, stop, reroute, or request clarification | Decision, bounded next action, verification gate, stop condition | Decision rationale names evidence and tradeoff without private reasoning logs |
| `checkpoint_superseded` | A newer artifact or decision replaces active guidance | Old and new identifiers, reason class, owner | Discovery no longer presents the old artifact as current authority |
| `checkpoint_archived_or_deleted` | Retention policy or explicit owner action retires the artifact | Final status, policy locator, index-update result | No active pointer or child route silently depends on removed evidence |

**Evidence checklist**

- [ ] Record which local sources were loaded and which were intentionally skipped; include source version or digest when drift matters.
- [ ] Record the exact verification command, reviewer question, rendered artifact, or restore fixture used as proof. Store a compact result and locator rather than a raw output dump.
- [ ] Capture changed-file list, current-state observation time, unresolved-risk notes, and exact next action when the artifact supports resumption.
- [ ] Capture context files loaded, delegated tasks, tool-call count, retry classification and count, ownership conflicts, and completion-audit outcome when those values explain workload or failure.
- [ ] Record the leading indicator and failure signal from this file in the journal or coverage manifest when the reference drives real work.
- [ ] Record p50, p95, or p99 latency and reviewer-time measurements only for repeated, comparable samples with a stated workload distribution, timer boundary, and denominator. A single run has a duration, not a percentile.
- [ ] Keep failures and abandoned attempts in the denominator where the metric requires them; success-only sampling invalidates restore and retry conclusions.
- [ ] Reconcile artifact status with telemetry after stale detection, supersession, archival, or deletion.

**Privacy and retention controls**

- Use enumerated error classes instead of exception strings that may include source content.
- Avoid message text, code excerpts, user prompts, credentials, personal identifiers, customer names, and unrestricted paths in routine labels.
- Treat hashes and locators as potentially sensitive identifiers. Collect them only when a named consumer can use them and apply access and retention controls.
- Do not use high-cardinality free text as metric labels. Keep detailed evidence in an authorized artifact and emit a bounded reference.
- Route actual exposure or audit-grade events to the applicable security, privacy, or incident system; retain only a safe bridge identifier here.
- Update discovery indexes and dependent pointers when artifacts are deleted or superseded so telemetry does not preserve false active authority.

**Verification**

Exercise event sequences for a successful transcript capture, unique-path collision, privacy stop, stale restore, changed user instruction, inaccessible adjacent route, ownership conflict, supersession, archival, and deletion. Assert correlation, valid phase transitions, inclusion of failed attempts, no unauthorized mutation, no raw transcript or inert secret marker in telemetry, accessible evidence pointers, and agreement between final event status and artifact discovery status.

For a one-off local capture, the same model may be a concise journal entry rather than a logging system. For repeated or distributed workflows, structured events make missing transitions, duplicate lineages, and biased denominators detectable. In neither case does telemetry itself prove semantic fidelity; source comparison and restore probes remain authoritative.

## Performance Verification Method

Performance means reaching a correct, authorized, and verifiable continuation with bounded total effort. Measure capture and restore separately, then evaluate the complete loop. A fast write that causes extra clarification, missed stale state, or recovery work is not an improvement.

**Performance method:** require tool-call budgets, timeout budgets, and a resumable journal when the workflow exceeds one focused session. Freeze or record the checkpoint schema, workload distribution, destination policy, reviewer rubric, and expected next actions before comparing variants.

**Capture-stage intervals**

1. Source selection: from request to a declared visible message range and authorized supporting-source set.
2. Privacy review: inspection, redaction decision, destination confirmation, and any policy routing.
3. Artifact construction: transcript rendering, state-field assembly, lineage assignment, and unique-path preparation.
4. Persistence: write attempt through durability and collision result.
5. Validation: metadata, heading or schema, source fidelity, trim and redaction disclosure, non-overwrite, and mode completeness checks.

**Restore-stage intervals**

1. Discovery: from restore request to identification of the intended active artifact and accessible adjacent evidence.
2. Review: reading the checkpoint and separating transcript facts, captured observations, inference, and current authority.
3. Freshness and identity probes: repository or task confirmation, file and test state, instructions, owners, permissions, dependencies, and relevant external systems.
4. Decision: selecting continue, adapt, stop, reroute, or clarify and naming the bounded next action, verification gate, and stop condition.
5. Recovery: additional time and work after a collision, privacy finding, stale artifact, wrong identity, inaccessible route, or ownership conflict.

**Required measurement packet**

| field group | record |
| --- | --- |
| Workload | Checkpoint mode, visible message count and bytes, supporting source count and approximate bytes, source type, repository count, checkpoint age, privacy class, handoff fan-out, restore fan-in, and external-state volatility |
| Execution | Tool-call count, context files loaded, delegated tasks, retry classification and count, timeout events, wall-clock intervals by phase, warm or cold condition, and reviewer identifier or experience band where appropriate |
| Artifact | Output bytes, field completeness, linked-artifact count, collision result, disclosed trimming or redaction, validation result, and lifecycle status |
| Continuity outcome | Capture fidelity, undisclosed loss, task identity match, stale-state detection, route accessibility, correct next action, verification-gate identification, stop-condition identification, reviewer clarification count, and unresolved disagreement |
| Safety outcome | Unsupported high-impact claim, sensitive-content violation, overwrite, historical-authority violation, ownership conflict, unauthorized mutation, and hard-stop count |
| Recovery | Detection interval, containment interval, restored safe state, replacement artifact, lineage update, and total recovery effort |
| Provenance | Fixture or field cohort, baseline or compared variant, timer boundaries, exclusions, denominator, observation date, and evidence locator |

Record p50, p95, and p99 latency or reviewer-time measurements only when enough repeated, comparable samples exist to make those percentiles meaningful. State the sample count, workload mix, warm or cold condition, and timer boundary. A single run should report its measured duration without a percentile label.

**Experiment protocol**

1. Choose a baseline: no checkpoint, the prior schema, or another mode-correct artifact. Do not compare against an undefined historical impression.
2. Build fixtures for small and boundary workloads, including exact transcript capture, trimming, privacy review, collision, wrong repository, changed files and tests, changed instructions, inaccessible routes, and overlapping ownership.
3. Use a cold consumer who did not create the checkpoint when testing resumability. Provide only the artifact and the access a real consumer would have.
4. Predeclare the expected next action, verification gate, stop condition, and hard-stop events through an independent reviewer or fixture.
5. Run enough repetitions to characterize the claimed statistic. Randomize or counterbalance variant order when reviewer learning could favor the second condition.
6. Include failed, abandoned, and recovered runs in the appropriate denominator. Report exclusions and reviewer disagreements.
7. Compare both phase cost and outcomes. Reject any latency or size improvement that introduces fabrication, undisclosed loss, overwrite, unauthorized disclosure, wrong-task mutation, stale destructive replay, or unresolved ownership conflict.
8. Repeat after material changes to schema, source distribution, destination policy, tooling, or external dependencies.

**Leading indicator to measure:** the next run needs fewer clarifications and produces fewer unverifiable claims. Interpret this jointly with next-action accuracy and stale detection: fewer questions may otherwise indicate unsafe confidence.

**Failure signal to watch:** the reference tells agents what to do without defining context budget or escalation rules, or a faster variant omits privacy, fidelity, identity, freshness, or ownership work.

**Pass condition:** the reference lets a cold reviewer identify the correct bounded next action, verification gate, and stop condition without reading unrelated files, while all applicable hard-stop safety gates remain clear and untriggered.

**Fail condition:** the reference encourages implementation before the workload, reliability target, and failure-mode table are explicit; shifts verification work into undocumented clarification; or improves timing while worsening a hard-stop or material continuity outcome.

The corpus supplies this method as guidance, not measured results. No baseline, sample distribution, or demonstrated percentile is present. Establish those locally before claiming speedup, optimal size, capacity, or causal improvement.

## Scale Boundary Statement

Chat Checkpoint Context Patterns is sufficient while one cold consumer can locate the intended artifact, understand its mode and provenance, verify current state, identify one owner, and choose one authorized next action within a bounded review. It stops being sufficient when discovery, authority, access, retention, concurrency, or production consequences require controls that a timestamped Markdown file and manual checklist cannot enforce.

| boundary signal | why the simple pattern is insufficient | minimum control before continuing | route or decomposition |
| --- | --- | --- | --- |
| Multiple independent systems or repositories | Captured state changes under separate versions, owners, and deployment cycles | Parent manifest, per-system checkpoints, current-state probes, and one integrator | Split by repository or authority; link returned evidence to one parent decision |
| More than one ownership boundary | Several actors can issue incompatible next actions or mutate overlapping scope | Accepted ownership, exclusive path boundaries, conflict detection, and convergence owner | Use a handoff or orchestration protocol; freeze overlapping writes until reconciliation |
| Unbounded source discovery | The consumer cannot know whether the evidence set is complete, canonical, or worth the review cost | Ranked canonical sources, explicit stopping rule, source budget, and provenance | Narrow by task, dependency or source graph, time horizon, or evidence claim |
| Repeated checkpoint versions | Filenames no longer reveal which artifact is current, stale, or superseded | Stable identity, active pointer, status, parent-child lineage, owner, and index consistency | Add a root manifest or managed index and test cold discovery |
| Incompatible privacy, access, or retention classes | One repository destination cannot lawfully or safely serve every artifact and consumer | Classification, approved stores, least-privilege access, retention, deletion, and audit controls | Split by policy domain and link only safe bridge metadata |
| Concurrent creators or restorers | Unique filenames prevent overwrite but not divergent authority or duplicate mutation | Concurrency control, idempotent identity, owner arbitration, and status transition rules | Use a managed store or orchestrator with one integration owner |
| Long-running workflow with material context drift | Captured files, tests, instructions, permissions, owners, or external state become historical | Periodic checkpoints, observation times, stale probes, risk summary, and supersession | Split by milestone or time horizon; verify against current specification before continuing |
| Large codebase with broad source lists | Review budget is consumed by unrelated files and canonical evidence is obscured | Dependency or source-graph narrowing, ranked evidence, bounded fan-in, and exact next action | Create narrower task checkpoints rather than one codebase-wide resume file |
| Production traffic or production mutations | Wrong restoration can affect availability, data, customers, or rollback authority | Explicit service objective, authorization, durable and auditable state, idempotency, rollback, monitoring, and incident integration | Route to production operations and deployment controls; use this reference only for supporting context |
| Regulated, audit-grade, or legal recordkeeping | Editable local files may not satisfy immutability, custody, access, residency, or deletion obligations | Approved records system, integrity and custody evidence, policy-driven retention, and authorized export | Do not treat repository-root Markdown as the system of record |
| Index or managed-store outage | Central discovery can become a new availability bottleneck | Defined read-only fallback, last-known status with age, no unsafe mutation, and reconciliation after recovery | Degrade to explicitly conditional access; never infer current authority from an arbitrary cached copy |

**Operating stages**

1. **Standalone bounded file:** suitable for one task, one repository, one owner, compatible destination policy, and a small manually reviewable set. Use unique timestamped naming, explicit mode, complete metadata, and capture or restore verdicts.
2. **Manifested checkpoint set:** add a root manifest when a task has several child artifacts but still one convergence owner. The manifest names current status, child owner, authority by claim, and returned evidence. It does not itself enforce permissions or retention.
3. **Managed checkpoint store:** move when search produces several plausible active artifacts, concurrent actors update status, access differs by consumer, or lifecycle volume exceeds manual reconciliation. Require stable identity, indexed lineage, integrity checks, access control, retention, deletion, audit events, and recovery behavior.
4. **Domain operations or records system:** route production actions, incidents, regulated evidence, and audit-grade chronology to their authoritative systems. A chat checkpoint can explain context but must not replace execution approval, operational state, or custody controls.

**Distributed execution**

Split work by theme or owned artifact and preserve one verification owner per split. Do not let parallel agents rewrite the same reference or action-bearing checkpoint without an integration boundary. Each child reports accepted scope, changed paths or evidence, verification, blockers, and exact next action. One integrator resolves conflicts and updates parent status; majority agreement among divergent checkpoints is not an authority rule.

**Long-running workflows**

Treat context drift as a reliability failure. Checkpoint after bounded milestones, preserve observation times, summarize open risks, and verify current instructions plus repository or external state before broad mutation. Old transcripts remain evidence of what was said, while old next actions become conditional on fresh probes. Supersede rather than silently editing history when the governing decision changes.

**Large-codebase workflows**

Require dependency or source-graph narrowing before applying this reference. A source list without ranked canonical guidance is not enough. Separate high-volume generated outputs from the resume artifact, preserve locators and bounded summaries, and keep one exact next code or verification action. If a cold consumer must inspect unrelated files to discover the intended work, the checkpoint boundary is too broad.

**Migration invariants**

- Preserve original artifact bytes or an integrity-verifiable export, provenance, creation time, mode, owner, and status.
- Preserve links in both directions between parent, child, superseded, archived, and replacement artifacts.
- Confirm intended consumers retain access under the new store without widening permissions.
- Update active pointers atomically or through an equivalent reconciled transition so two artifacts do not claim current authority.
- Apply retention and deletion policy to both payloads and indexes; a deleted artifact must not remain discoverable as active.
- Provide a read-only fallback that exposes age and uncertainty but blocks unsafe mutation when the index or store is unavailable.

**Scale verification**

Test cold discovery across many versions, concurrent creators, stale active records, owner changes, cross-repository children, permission mismatches, retention expiry, deletion, index rebuild, and temporary store outage. The consumer should find exactly the intended current artifact, identify one owner and next action, detect stale or inaccessible evidence, and degrade without mutation when authority cannot be proven.

No universal artifact-count or traffic threshold is established by the corpus. The seed's exit conditions are qualitative policy. Calibrate local thresholds from observed discovery errors, restore outcomes, concurrency conflicts, access incidents, lifecycle cost, and production consequence. A single high-impact authority or privacy boundary can justify escalation before volume grows.

## Future Refresh Search Queries

| search_query_label_name | search_query_text_value |
| --- | --- |
| `official_docs_query_phrase` | chat checkpoint context patterns official documentation best practices |
| `github_repository_query_phrase` | chat checkpoint context patterns GitHub repository examples |
| `release_notes_query_phrase` | chat checkpoint context patterns changelog release notes migration |

Preserve those seed phrases as broad discovery queries. They are not citations, and they were not executed for this evolution. Future maintainers should narrow them by product or skill name, version, date, lifecycle claim, and authoritative domain before treating any result as relevant.

| refresh_question | future_query_phrase | preferred evidence | trigger and possible decision change |
| --- | --- | --- | --- |
| Has the local visible-message capture contract changed? | `save recent chat context visible messages transcript capture count chronological speaker labels version` | Canonical local skill and template diff first; official tool documentation if the behavior is platform-owned | Local source version changes or capture fixture fails; update source scope, default count, ordering, or metadata only if authoritative behavior changed |
| Is a complete conversation export now available or different? | `official conversation export complete thread history partial visible messages provenance documentation` | Official platform documentation and release notes for the exact product and account surface | A user needs invisible history or complete export; route differently if an authorized complete-history mechanism exists |
| Have overwrite, naming, or persistence semantics changed? | `official chat checkpoint timestamp filename collision overwrite atomic write documentation` | Canonical local implementation, official filesystem or storage contract, and maintained repository tests | Collision or partial-write incident; strengthen identity, atomicity, integrity, or recovery guidance |
| Have privacy, retention, or destination requirements changed? | `official chat transcript data privacy retention deletion access control checkpoint storage policy` | Applicable organization policy and official product privacy or security documentation | New data class, destination, jurisdiction, exposure, or policy revision; change redaction, storage, access, retention, or deletion route |
| Are managed checkpoint lifecycle patterns available? | `agent checkpoint store lifecycle active stale superseded invalid archived deleted lineage official` | Official product documentation, maintained reference implementation, and migration notes | Manual discovery yields conflicting active artifacts; adopt indexed identity and lifecycle controls if evidence fits the workload |
| Have agent handoff and ownership controls changed? | `official multi agent handoff ownership exclusive file scope integration checkpoint pattern` | Official agent or orchestration documentation plus maintained implementation tests | Concurrent writers, ownership collision, or new orchestration capability; revise acceptance and convergence rules |
| What failures recur in maintained implementations? | `chat checkpoint transcript restore stale context overwrite privacy failure issue repository` | Maintained repository issue history and fixes linked to code or releases | Restore incident or unexplained failure trend; add a failure mode only after confirming applicability and resolution state |
| How are stale-state and resume safety verified? | `agent checkpoint restore stale state current instructions repository verification cold resume evaluation` | Official evaluation guidance, research with disclosed method, and local restore drills | Wrong-action or stale-miss event; update fixtures and gates when evidence improves detection or exposes a counterexample |
| How should large checkpoint sets be indexed and retired? | `checkpoint artifact index lineage retention deletion current pointer consistency official documentation` | Approved artifact or records platform documentation and operational tests | Multiple active candidates, expired artifacts, or deletion inconsistency; migrate only with integrity, access, and fallback evidence |
| Have performance or reliability claims been measured credibly? | `checkpoint resume time clarification wrong action stale detection benchmark methodology` | Primary research, official benchmark methodology, or local repeated trials with workload distributions | A speed, capacity, or accuracy claim is proposed; accept only if timer boundaries, denominators, safety outcomes, and uncertainty are present |
| What migrations or breaking changes affect captured artifacts? | `chat checkpoint context patterns changelog release notes migration schema compatibility` | Official release notes, migration guide, and compatibility tests | Tool, template, schema, or store version changes; preserve old interpretation and test forward or backward migration |
| Which counterexamples challenge the current default? | `chat checkpoint context pattern anti pattern failure privacy overwrite stale handoff conflict` | Incident reports, maintained issues, security advisories, and local fault drills | Periodic adversarial review or hard-stop event; narrow or reverse guidance when the counterexample matches local boundaries |

**Refresh protocol**

1. Start with a claim and invalidation trigger, not a broad desire to make the reference newer. Record the current guidance and what evidence could confirm, narrow, reverse, or leave it unchanged.
2. Diff the canonical local skill, template, implementation, and tests before public discovery. Local behavior remains authoritative for local contracts unless a governing source explicitly changes it.
3. Run the narrow query only when browsing or repository research is authorized. Record the exact query, execution date, product and version qualifiers, source locator, publication or release date, and access boundary.
4. Prefer primary official documentation and release notes for normative behavior, maintained code and tests for implementation behavior, applicable policy for privacy and retention, and issue or incident evidence for failure modes.
5. Open and read the selected source. Search snippets, rankings, copied summaries, and query strings are discovery aids, not evidence.
6. Map a concise source span to one claim. Record inclusion, rejection, conflict, applicability boundaries, and any missing evidence. Do not infer proof of absence from an unsuccessful query.
7. Preserve conflicting authoritative evidence and resolve it by product, version, scope, or owner. Do not blend incompatible behaviors into a universal rule.
8. Apply the proposed guidance diff, then rerun relevant capture, collision, privacy, restore, stale-state, ownership, lifecycle, and scale fixtures.
9. Record a no-change outcome when new evidence does not alter the decision. Refresh activity is not itself a reason to rewrite stable guidance.

**Selection cautions**

- Generic terms such as "checkpoint" and "context" span unrelated databases, model training, operating systems, and chat products. Add exact product and lifecycle qualifiers.
- Recency does not outrank authority or applicability. A newer commentary page may be less useful than the versioned local contract.
- Official documentation can define intended behavior but may omit failure history; maintained issues can expose failures but may be fixed, unrepresentative, or unsupported.
- Secondary material may locate a primary source, but it should not silently inherit the primary source's authority.
- Search results can change ranking without any source change. Preserve stable locators and a dated selection record.

At this revision boundary, only the query design is guidance. No future query result has been used as evidence, and the evidence notes below retain that limitation.

## Evidence Boundary Notes

- `local_corpus_sourced_fact`: statements tied directly to the local source paths above. For this evolution, the read capture skill and checkpoint template support the visible active-thread scope, default selection behavior, chronological speaker labels, mostly verbatim capture, explicit trim marker, local timestamped filename, non-overwrite rule, metadata fields, and transcript shape.
- `external_research_sourced_fact`: statements tied to the public URLs above. No public URL was browsed or refreshed for this evolution, so cataloged external claims retain their prior boundary and should be revalidated before a high-impact decision.
- `combined_evidence_inference_note`: synthesis that combines local and public evidence, or local evidence with systems reasoning, into agent guidance. The capture and restore lifecycle, mode matrix, authority rules, managed-store escalation, reliability extensions, and many failure and retry controls are synthesis unless a narrower source row states otherwise.

Use those three preserved labels with the checkpoint-specific classes below. A class describes origin and allowed interpretation; it does not guarantee correctness by itself.

| evidence class | establishes | does not establish | required treatment |
| --- | --- | --- | --- |
| `captured_transcript_fact` | What selected visible messages said, in the preserved order, subject to disclosed trimming or redaction | Complete invisible history, truth of every statement, current repository state, or current authorization | Preserve source window, speakers, transformations, and capture time; label partial scope |
| `captured_work_state_observation` | What files, tests, owners, blockers, or external conditions were observed at the stated time | That the same state remains true at restore time | Preserve observation method and time; run fresh probes before dependent action |
| `checkpoint_summary_or_inference` | A bounded interpretation created to aid continuation | Verbatim conversation, direct source fact, or independently verified current state | Label the transformation, inputs, omissions, assumptions, and uncertainty |
| `local_corpus_sourced_fact` | Behavior or guidance directly supported by a named local file and version or digest | Universal behavior across other products, later versions, or organization policy | Cite the exact local path and claim span; recheck after local source drift |
| `external_research_sourced_fact` | A claim directly supported by a read, dated, applicable public source | Local contract authority, unmentioned edge cases, or applicability to another version | Record URL, date, version, claim span, authority, and conflicts; do not cite search snippets |
| `combined_evidence_inference_note` | A reasoned recommendation derived from identified inputs | A direct quotation, measured result, or authoritative policy | State assumptions, boundary, counterexample, uncertainty, and verification or reversal condition |
| `current_user_instruction` | The latest applicable user intent and mutation authority within governing policy | Current file, test, service, or permission state | Resolve chronology and conflicts; pair high-impact action with fresh state evidence |
| `historical_user_instruction` | What the user previously requested and why an earlier action made sense | Continuing authority after a newer conflicting request | Preserve as provenance; never replay automatically when applicability is uncertain |
| `current_restore_observation` | What an authorized probe shows now about identity, files, tests, access, owners, or external dependencies | Broader truth outside the probe's scope or future stability | Record command or method, time, scope, result, and evidence locator |
| `policy_target_not_observation` | The acceptance threshold the workflow is intended to meet | That the threshold has been achieved in fixtures or field use | Label target status, denominator, enforcement, and required collection method |
| `observed_measurement` | A result for a declared cohort, workload, timer boundary, and method | Universal capacity, causal improvement, or an unmeasured percentile | Preserve numerator, denominator, distribution, exclusions, uncertainty, and baseline |
| `future_refresh_query_only` | A discovery phrase and the uncertainty it is intended to investigate | Any source-backed claim or evidence of absence | Keep it in the refresh plan until authorized research selects and evaluates a source |
| `applicable_policy_or_owner_decision` | What handling, access, retention, incident, or ownership action is authorized for the scoped domain | Transcript fidelity or live technical state unless separately verified | Name the authority, effective scope, decision time, and supersession conditions |

**Operational authority rules**

1. Transcript evidence governs what was captured from visible conversation; it does not authorize current mutation merely because a command appears in the transcript.
2. The latest applicable user instruction governs over a conflicting historical user instruction, subject to system, repository, privacy, security, and other applicable policy.
3. Fresh repository, test, permission, owner, and external-state observations govern current technical preconditions over captured work-state summaries.
4. Canonical local sources govern the local capture contract over generic public examples. External primary sources may govern their own product behavior but must match product, version, and scope.
5. Applicable privacy, security, retention, and incident policy governs destination and handling over convenience or a generic repository-root default.
6. An explicit owner or integrator decision governs overlapping shared-workspace mutations. Conflicting checkpoint summaries do not resolve authority by majority.
7. Synthesis may recommend a default and verification method; it cannot be described as a measured result or source-mandated rule without supporting evidence.

These rules are not a single global ranking. Each evidence class governs a different question: historical fidelity, local contract, permission, present state, ownership, or expected quality. A safe restore usually needs several compatible classes rather than one apparently authoritative artifact.

**Minimum claim record**

For each action-bearing, high-impact, time-sensitive, disputed, or quantitatively precise claim, record:

- Claim identifier and concise statement.
- Evidence class, source path or URL, source version or observation time, and exact scope.
- Transformation: verbatim, trimmed, redacted, summarized, calculated, or inferred.
- Authority question the evidence can answer and questions it cannot answer.
- Confidence plus known conflict, absence, staleness, or applicability limit.
- Verification method, result if executed, and evidence locator.
- Allowed action: describe history, guide review, permit bounded continuation, block, reroute, or require owner clarification.
- Invalidation trigger and downstream sections, fixtures, metrics, or checkpoints that must be reconsidered.

**Uncertainty and conflict states**

- `unverified`: a plausible claim lacks direct evidence or a completed verification method.
- `stale`: provenance is known, but time or version drift may invalidate present use.
- `conflicting`: two applicable sources or owners disagree and authority has not been resolved.
- `absent`: the required evidence was not available; absence of a result is not proof that the claim is false.
- `partial`: selected evidence is valid within a disclosed window but does not cover the complete history or state.
- `superseded`: a newer applicable source, instruction, decision, or artifact replaces current authority while preserving lineage.
- `invalid`: integrity, identity, privacy, or authority failure prevents the artifact from supporting its intended action.

Uncertainty should change action. A partial transcript may remain useful for reading; a stale work-state claim requires a fresh probe; conflicting ownership blocks shared mutation; an unverified performance claim must be removed, qualified, or measured.

**Good boundary example:** "The local capture skill specifies the last five visible chronological messages by default (`local_corpus_sourced_fact`). A resumable checkpoint should also record current tests and an exact next action (`combined_evidence_inference_note`). At restore time, rerun the relevant test and inspect current files (`current_restore_observation`) before continuing." Each clause has a different evidence owner and operational role.

**Bad boundary example:** "The checkpoint proves the next command is safe because the transcript says to run it." This collapses historical wording, current authority, and live state into one unsupported conclusion.

**Borderline boundary example:** a public agent guide recommends a managed checkpoint store and matches the local workload, but its version and privacy model differ. Keep it as scoped external comparison, verify those boundaries, and do not promote it to a local default solely because the design is plausible.

**Bidirectional evidence audit**

1. Trace every material recommendation backward to a local source, evaluated external source, policy decision, current observation, measured cohort, or explicit inference.
2. Confirm quoted and mostly verbatim material against the selected source; confirm all trimming, redaction, summary, and calculation disclosures.
3. Search for policy targets described as achieved results, single durations described as percentiles, and historical observations written in the present tense.
4. Inject source version changes, instruction changes, stale file state, evidence conflicts, and missing routes; verify confidence, status, and allowed action change.
5. Trace each changed or removed source forward to every affected recommendation, example, test, metric, retry rule, scale boundary, and active checkpoint.
6. Preserve disagreement and no-evidence outcomes. Do not manufacture a unified narrative when authority or applicability remains unresolved.

The evolved reference therefore has a deliberate evidence ceiling. Local capture facts are supported by the read local skill and template. The three seed search queries remain future discovery aids. No new external research was performed. Broader restore, lifecycle, reliability, observability, and scale guidance is explicit systems synthesis or policy proposal until local drills, authoritative policy, or refreshed primary sources provide stronger evidence.
