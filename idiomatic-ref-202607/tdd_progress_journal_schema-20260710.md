# Tdd Progress Journal Schema

**Decision supported.** This section helps decide whether a work session needs schema-shaped checkpointing and what each checkpoint must contain. The seed title names a journal schema without saying what problem the schema solves, keeping a TDD session resumable after context loss by recording phase, test status, and next steps in a fixed shape.

**Recommended default and causal basis.** Write one schema-shaped checkpoint entry per work batch, always naming the phase, exact test names with statuses, and a numbered next step. Long-running agent sessions lose context between checkpoints, and only a fixed-shape entry lets a successor reconstruct where the red-green-refactor loop stood.

**Operating conditions and assumptions.** The work follows a red-green-refactor rhythm, sessions can be interrupted, and a durable journal file persists between them. The schema governs checkpoint entries for TDD-style work and does not prescribe the tests, the code design, or the commit discipline around them.

**Failure boundary and alternatives.** A checkpoint schema adds pure overhead on one-sitting tasks that finish before any context loss can occur. Bounded alternatives and recoveries: commit messages as a coarse journal for small tasks, issue-tracker comments for team-visible work, or a full transcript dump when storage is cheap and review is not needed.

**Counterexample, gotchas, and operational comparison.** Entries degrade into vague prose once a session feels fluent, and the phase field silently goes stale when work pivots mid-batch. Good: an entry a fresh session resumes from without asking questions. Bad: a diary line saying made progress on tests. Borderline: a compressed entry on a trivial task that still names phase and next step.

**Verification, evidence, and uncertainty.** Hand an entry to a reader with no session context and check they can state the phase, the failing tests, and the next action. The local schema file mandates the entry template, phase field, and minimal completion rules this framing describes. The minimum task size where journaling pays for itself is unmeasured, so the overhead threshold stays judgment.

**Second-order consequence.** A journal entry is written for a reader who shares none of the writer's working memory, which is why every field must be self-contained.

**Revision decision.** Open by stating that this schema exists so a fresh session can resume mid-loop from the journal alone, without rereading the whole transcript.

**Retained seed evidence.** The exact theme title and its framing as a TDD progress journal schema remain unchanged. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

## Source Evidence Mapping Table

**Decision supported.** This section helps decide which recorded source may back which claim about the journal schema. The seed map presents two local schema paths as separate evidence rows although they are byte-identical copies, and lists three public URLs with no recorded retrieval.

**Recommended default and causal basis.** Cite the 202604 retainer copy as the working source, note the 202602 copy as its earlier mirror, and treat all three URLs as unrefreshed candidates. Claims backed by two rows read as independently corroborated, yet an identical mirror adds discoverability, not evidence.

**Operating conditions and assumptions.** Rows resolve to real paths or URLs and carry confidence labels a reader can act on without opening every source. The table records provenance for this document's claims and does not decide which mirrored copy the archive should keep.

**Failure boundary and alternatives.** The mapping cannot show which copy is maintained going forward, so citing either path risks pointing at the one that later rots. Bounded alternatives and recoveries: record a single row with a mirrors column, add content hashes so forks are detectable, or date-stamp external rows when first retrieved.

**Counterexample, gotchas, and operational comparison.** Monthly skill snapshots multiply mirrors over time, and each new copy widens the surface where an edit can fork the schema. Good: citing the schema template from the retainer copy with the mirror noted. Bad: presenting both copies as agreeing witnesses. Borderline: citing the agents.md format for journal vocabulary while flagging no retrieval was done.

**Verification, evidence, and uncertainty.** Diff the two local paths to confirm identity and check every external citation names which URL row it depends on. A diff run during this evolution confirmed both 80-line schema files are byte-identical. Whether the public agent-instruction guides say anything about progress journals at all is unknown, since none was retrieved.

**Second-order consequence.** When a skill is republished monthly its references duplicate by construction, so archives of this shape need identity notes as a standing habit.

**Revision decision.** Annotate the two local rows as one schema mirrored across the 202602 orchestrator and 202604 retainer skill folders, and mark external rows retrieval-undated.

**Retained seed evidence.** All five source rows with their category, confidence, and synthesis-role columns remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| source_location_path_key | source_category_artifact_type | source_authority_confidence_level | source_usage_synthesis_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202602/tdd-context-retainer-orchestrator-01/references/progress-journal-schema.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/codex-skills-202604/tdd-task-progress-context-retainer/references/progress-journal-schema.md | local_corpus_source_material | local_corpus_sourced_fact | reference detail file for deeper pattern evidence |
| https://developers.openai.com/codex/guides/agents-md | external_research_source_material | external_research_sourced_fact | primary agent instruction context model |
| https://docs.github.com/actions | external_research_source_material | external_research_sourced_fact | verification and automation model |
| https://agents.md/ | external_research_source_material | external_research_sourced_fact | general agent instruction format |

## Pattern Scoreboard Ranking Table

**Decision supported.** This section helps decide which journaling habits deserve default adoption when writing checkpoint entries. The seed scoreboard awards 95, 91, and 88 to generic corpus hygiene and never ranks the journaling practices the schema teaches, phase honesty, exact test naming, and next-step continuity.

**Recommended default and causal basis.** Rank always-name-the-phase first, exact test names with statuses second, and one-numbered-next-step third. Attention follows the ranking, and a scoreboard silent about phase and test fields lets writers polish citations while entries stop being resumable.

**Operating conditions and assumptions.** Each row names an observable resume failure the pattern prevents rather than an abstract quality. The scoreboard ranks journaling patterns for this theme and does not grade the TDD practice itself, which the source skill's other references govern.

**Failure boundary and alternatives.** The numbers have no measurement behind them in this corpus, so quoting them as evidence rather than editorial emphasis misleads. Bounded alternatives and recoveries: order rows by which missing field most often breaks resumption, replace scores with a resume-blocking flag, or drop numbers for a simple default tier.

**Counterexample, gotchas, and operational comparison.** High scores on hygiene rows crowd out the schema's own completion rules, and stable numbers acquire false authority. Good: adopting exact test naming after a resume stalled on which test was failing. Bad: citing the 91 score to settle a review dispute. Borderline: retaining scores with an editorial-only caveat attached.

**Verification, evidence, and uncertainty.** Map each top row to the schema field or completion rule that operationalizes it and confirm no ranked practice lacks a field. The schema's minimal completion rules, always a phase, always a next step, phase-specific captures, are the source form of these rankings. Which field omission most often breaks real resumptions is unmeasured, so the ordering encodes expected rather than observed cost.

**Second-order consequence.** The practices that make an entry resumable are exactly the ones that feel skippable while context is still warm.

**Revision decision.** Insert phase-field honesty, exact-test-status capture, and numbered-next-step rows above the hygiene rows, all marked editorial.

**Retained seed evidence.** All three scored rows with their tier labels and failure-prevention targets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| pattern_identifier_stable_key | pattern_score_numeric_value | pattern_tier_adoption_level | pattern_failure_prevention_target |
| --- | ---: | --- | --- |
| `tdd_progress_journal_schema` | 95 | default_adoption_pattern_tier | Source Map First: Load local tdd progress material before synthesizing journal schema recommendations. |
| `tdd_progress_journal_schema` | 91 | default_adoption_pattern_tier | Evidence Boundary Split: Separate local facts, external facts, and inference before giving agent instructions. |
| `tdd_progress_journal_schema` | 88 | default_adoption_pattern_tier | Verification Gate Coupling: Attach each recommendation to at least one command, checklist, or review gate. |

## Idiomatic Thesis Synthesis Statement

**Decision supported.** This section helps decide what single orienting claim should govern how checkpoint entries get written. The seed thesis counts two local paths and repeats the load-local-first formula instead of the theme's actual claim, that a checkpoint entry is a contract with a future reader who has lost all context.

**Recommended default and causal basis.** Phrase the thesis as journal so that resumption needs the journal alone, with the three labels kept on its clauses. The thesis is what survives quotation, and a retrieval slogan tells agents where to look rather than what a resumable entry must guarantee.

**Operating conditions and assumptions.** The evidence labels stay attached so the local schema facts remain distinguishable from ecosystem inference when the thesis is reused. The thesis orients use of this reference and does not restate the schema template, which the artifact and source map carry.

**Failure boundary and alternatives.** The contract framing overshoots for solo, uninterrupted work where the writer and only reader are the same warm context. Bounded alternatives and recoveries: quote the schema's own use-this-for-every-checkpoint instruction verbatim, split the thesis per label, or phrase it as a testable resumption criterion.

**Counterexample, gotchas, and operational comparison.** Paraphrases drop the successor-reader framing first, leaving a generic write-things-down platitude. Good: an agent citing the thesis to justify naming a failing test exactly. Bad: quoting it as ecosystem consensus on journal formats. Borderline: compressing it for a prompt while keeping the successor-reader clause.

**Verification, evidence, and uncertainty.** Check the local clause matches the schema file's instruction and that the combined clause is labeled inference. The schema opens with use this schema for every checkpoint entry, the imperative this thesis generalizes. Whether public agent-instruction formats endorse phase-based journaling is unverified without retrieval.

**Second-order consequence.** Writing for a context-free reader is the same discipline as writing a good bug report, and both fail in the same way, by assuming shared memory.

**Revision decision.** Restate the combined inference as every checkpoint must let a context-free successor name the phase, the failing tests, and the next action.

**Retained seed evidence.** All three labeled thesis lines, local fact, external fact, and combined inference, remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`local_corpus_sourced_fact`: The local row for `tdd_progress_journal_schema` contains 2 source path(s), which should be treated as the first retrieval surface for this theme.
`external_research_sourced_fact`: The external source map provides public documentation, repository, or ecosystem analogues where available.
`combined_evidence_inference_note`: Reliable use of Tdd Progress Journal Schema comes from loading the local corpus first, checking public ecosystem guidance second, and converting both into verification-backed agent decisions.

## Local Corpus Source Map

**Decision supported.** This section helps decide which part of the local schema file answers a given journaling question. The seed map records both mirrored schema paths with identical truncated heading signals and does not route readers to the file's three distinct parts, the entry template, the completion rules, and the worked example.

**Recommended default and causal basis.** Read the full schema file on first contact, then return to the completion rules section whenever deciding if an entry is finished. The schema file answers three different questions, what shape an entry takes, what the minimum content is, and what a filled entry looks like, and a file-level row hides that structure.

**Operating conditions and assumptions.** Rows record exact paths, honest heading signals, and a role distinguishing template, rules, and example material. The map indexes this theme's local evidence and does not inventory the surrounding skill folders, which hold orchestrator scripts beyond this theme.

**Failure boundary and alternatives.** The heading signals cut off mid-field, so a reader guessing coverage from signals alone will miss the next-steps and metrics fields entirely. Bounded alternatives and recoveries: collapse to one row with a mirror note, extend signals to cover all eight entry fields, or inline the template here and demote the map to provenance only.

**Counterexample, gotchas, and operational comparison.** The mirrored rows invite readers to open both files looking for differences that do not exist. Good: opening the completion rules to settle whether a Red entry needs failing tests listed. Bad: skimming heading signals and concluding metrics are optional. Borderline: quoting the template from memory while flagging exact field names need the file.

**Verification, evidence, and uncertainty.** Open the mapped path, confirm the three parts exist as recorded, and walk one field question to the part that answers it. Both mapped paths were opened in full during this evolution and matched each other exactly. Whether the orchestrator skill folder contains additional journal guidance beyond this schema was not exhaustively explored.

**Second-order consequence.** An 80-line source is cheap to read whole, so the map's real job here is telling readers they can and should read all of it.

**Revision decision.** Add per-part routing, template questions to the schema block, obligation questions to the minimal completion rules, and formatting questions to the example entry.

**Retained seed evidence.** Both local source rows with their paths, titles, heading signals, and usage roles remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| local_source_filepath_value | local_source_title_text | local_source_heading_signals | local_source_usage_role |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202602/tdd-context-retainer-orchestrator-01/references/progress-journal-schema.md | Progress Journal Schema | Progress Journal Schema; TDD Session State: [Date/Time]; Current Phase: [Red / Green / Refactor]; Tests Written:; Implementation Progress:; Current Focus: | reference detail file for deeper pattern evidence |
| agents-used-monthly-archive/codex-skills-202604/tdd-task-progress-context-retainer/references/progress-journal-schema.md | Progress Journal Schema | Progress Journal Schema; TDD Session State: [Date/Time]; Current Phase: [Red / Green / Refactor]; Tests Written:; Implementation Progress:; Current Focus: | reference detail file for deeper pattern evidence |

## External Research Source Map

**Decision supported.** This section helps decide which public source to consult, and for what kind of claim, when refreshing this theme. The seed map offers an AGENTS.md guide, GitHub Actions documentation, and the agents.md format as analogues without saying what each could actually confirm about a progress journal schema.

**Recommended default and causal basis.** Consult the AGENTS.md sources for how agent-facing files are conventionally structured and the Actions docs for how verification evidence is conventionally recorded, logging retrieval dates. The three URLs model adjacent ideas, agent instruction files and automated verification, not checkpoint journaling itself, so their refresh value is indirect.

**Operating conditions and assumptions.** Rows keep their boundary labels so analogue-derived claims stay distinguishable from local schema facts. The map guides freshness checks on surrounding conventions and cannot validate the schema's field set, which is a local design choice.

**Failure boundary and alternatives.** Citing an analogue as if it documented this schema fabricates external support the sources never provided. Bounded alternatives and recoveries: add a genuinely on-topic source such as published TDD journaling practices if one is found, drop the weakest analogue, or mark the whole map inspiration-only.

**Counterexample, gotchas, and operational comparison.** Analogue sources drift without affecting this schema at all, tempting needless rewrites in the name of freshness. Good: borrowing heading conventions from agents.md with a dated inspiration note. Bad: citing the Actions docs as evidence that phase fields are standard. Borderline: using Codex guide vocabulary for journal field names with an inference label.

**Verification, evidence, and uncertainty.** Resolve each URL, record what it can and cannot confirm, and re-label any local claim currently leaning on an analogue. The three mapped URLs are established public surfaces for agent instruction files and CI verification conventions. None of the three was retrieved during this evolution, so even their analogue value is asserted, not confirmed.

**Second-order consequence.** When external rows are analogues rather than sources, the honest label is inspiration, and inspiration cannot go stale the way facts can.

**Revision decision.** State each row's confirmable surface, instruction-file conventions from the AGENTS.md sources and check-run evidence conventions from the Actions docs, all undated.

**Retained seed evidence.** All three external rows with their names, usage roles, and evidence-boundary labels remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| external_source_url_value | external_source_name_text | external_source_usage_role | evidence_boundary_label_value |
| --- | --- | --- | --- |
| https://developers.openai.com/codex/guides/agents-md | OpenAI Codex AGENTS.md guide | primary agent instruction context model | external_research_sourced_fact |
| https://docs.github.com/actions | GitHub Actions documentation | verification and automation model | external_research_sourced_fact |
| https://agents.md/ | AGENTS.md open format | general agent instruction format | external_research_sourced_fact |

## Anti Pattern Registry Table

**Decision supported.** This section helps decide which recurring entry-writing failures deserve standing names and detection signals. The seed registry lists three corpus-hygiene failures and omits the journaling failures the schema's own rules imply, phaseless entries, vague test references, missing next steps, and diary-style prose.

**Recommended default and causal basis.** Reject any entry lacking a phase, an exact test name with status, or a numbered next step before accepting a checkpoint as done. A reviewer triaging a stalled resume needs named journal failures with detection signals, not generic advice hygiene.

**Operating conditions and assumptions.** Each row names the failure, why it is expensive at resume time, the replacement habit, and a scan-based detection method. The registry covers entry-writing failures, not TDD malpractice like skipping the red step, which the source skill's workflow owns.

**Failure boundary and alternatives.** Rows that cannot be matched against an actual journal entry detect nothing at the moment of resumption. Bounded alternatives and recoveries: encode detection as a lint script over journal files, fold the four rows into the completion checklist, or rank rows by observed resume breakage once history exists.

**Counterexample, gotchas, and operational comparison.** Fluent sessions produce the vaguest entries because the writer's warm context masks every omission. Good: bouncing an entry that says tests mostly passing with no names. Bad: approving it because the prose reads confidently. Borderline: accepting a compressed entry on a trivial task with fields merged but all present.

**Verification, evidence, and uncertainty.** Scan one real journal against the four detection signals and confirm each fires on a seeded violation. The schema's minimal completion rules prohibit exactly these omissions, phase always, next step always, phase-specific captures always. The relative frequency of the four failures in real journals is unmeasured, so row order is expected cost.

**Second-order consequence.** Every journal anti-pattern is a resume failure waiting for the worst moment, and all four are mechanically detectable.

**Revision decision.** Add phaseless-entry, unnamed-test-reference, missing-next-step, and prose-drift rows, each detectable by scanning an entry against the schema fields.

**Retained seed evidence.** All three seed rows, context-free summaries, unsourced claims, and unverified instructions, with their detection methods remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| anti_pattern_failure_name | failure_cause_risk_reason | safer_default_replacement_pattern | detection_signal_review_method |
| --- | --- | --- | --- |
| context_free_summary_output | agent skips local corpus and produces generic advice | source_map_first_synthesis | verify every listed local path appears in the generated file |
| unsourced_recommendation_claims | guidance appears authoritative without source boundary | evidence_boundary_split_pattern | check for local, external, and inference labels |
| unverified_agent_instruction | recommendation cannot be checked by command or review gate | verification_gate_coupling | require concrete gate in generated reference |

## Verification Gate Command Set

**Decision supported.** This section helps decide which checks must pass before this reference and the journal entries it governs count as verified. The seed gate names the repository verifier for this document and gives no check for journal entries themselves, whose completeness is scannable field by field.

**Recommended default and causal basis.** Run the repository verifier after editing this file and scan every new journal entry against the minimal completion rules before ending a batch. Entry completeness is the cheapest gate in this theme because the schema enumerates required fields that a scan can confirm without judgment.

**Operating conditions and assumptions.** Each gate names its check, the failure it intercepts, and where its result gets recorded. Gates here verify this reference and journal-entry form, not the test suites the journal reports on, which have their own commands.

**Failure boundary and alternatives.** No scan can judge whether a next step is genuinely actionable, so mechanical gates need a paired human read for quality. Bounded alternatives and recoveries: script the field scan over journal markdown, have the next session grade its predecessor's final entry, or accept documented manual review on small tasks.

**Counterexample, gotchas, and operational comparison.** Self-review at the end of a long session rubber-stamps its own entries, and unrecorded gate results cannot be audited later. Good: a batch that ends with a scanned, complete entry and a recorded verifier pass. Bad: a green document verifier taken as proof the journal is resumable. Borderline: an entry passing the scan while its next step is vague, flagged for the human read.

**Verification, evidence, and uncertainty.** Run the verifier, scan a sample entry for the required fields, and have a second reader attempt a resume from it. The schema's completion rules are phrased as always-include obligations, which is a checkable gate specification in source form. How much human review the actionability of next steps needs is a quality judgment no command settles.

**Second-order consequence.** Gating the journal at write time is vastly cheaper than discovering the gap at resume time, when the writer's context is gone.

**Revision decision.** Add an entry-completeness check, phase present, at least one test with status, numbered next step, run before any checkpoint is declared done.

**Retained seed evidence.** The repository verifier command and its run-after-editing instruction remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`verification_gate_command_set`: Run the repository verifier after editing this file.

```bash
python3 agents-used-monthly-archive/idiomatic-references-202606/tools/verify_reference_generation.py --stage final
```

## Agent Usage Decision Guide

**Decision supported.** This section helps decide whether a given task should keep a schema-shaped progress journal. The seed guide gives the four stock bullets and never says when journaling applies, any multi-batch or interruptible task, or when it is overhead, single-sitting work finished before context can decay.

**Recommended default and causal basis.** Start a schema-shaped journal for any task expected to outlive one session, and write the first entry before deep work begins. The schema pays exactly when future context loss is plausible, so admission turns on task duration and interruption risk, not on topic keywords.

**Operating conditions and assumptions.** The agent can estimate task duration honestly and has a durable journal location that survives the session. The guide admits tasks into journal-keeping and does not rank this reference against neighbors, which the routing section owns.

**Failure boundary and alternatives.** Journaling every trivial errand teaches agents the schema is ceremony, which corrodes compliance on the long tasks that need it. Bounded alternatives and recoveries: default to journaling and drop it only on provably tiny tasks, use commit messages as the journal for code-only work, or let a supervisor mandate journaling per task class.

**Counterexample, gotchas, and operational comparison.** Tasks routinely outgrow their estimate, and a task that starts unjournaled retrofits its journal from fading memory. Good: opening a journal at the start of a multi-day refactor. Bad: reconstructing a journal after context was already lost. Borderline: a two-hour task journaled with a single compressed entry at its midpoint.

**Verification, evidence, and uncertainty.** Review a sample of finished tasks and check journaled ones resumed cleanly while unjournaled ones were genuinely single-sitting. The schema's per-checkpoint mandate presumes the checkpointing decision was made affirmatively at task start. The duration threshold where journaling flips from overhead to necessity varies by agent and task, so the boundary stays judgment.

**Second-order consequence.** The decision to journal must be made at task start, because by the time context loss proves the need, the unjournaled context is already gone.

**Revision decision.** Key admission to task shape, journal when work spans batches, sessions, or owners, and skip with a note when a task completes in one warm sitting.

**Retained seed evidence.** The usage trigger sentence and all four seed bullets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`agent_usage_decision_guide`: Use this reference when a task mentions this theme, one of the listed local source paths, or a nearby technology/workflow surface.

- Start with the local corpus source map.
- Prefer patterns with explicit verification gates.
- Treat external sources as freshness and ecosystem checks, not replacements for local repo conventions.
- Preserve the evidence boundary labels when reusing recommendations.

## User Journey Scenario

**Decision supported.** This section helps decide which concrete situation should anchor a reader's mental model of the journal in use. The seed scenario opens with a lead turning ambiguity into acceptance criteria and stops before any journaling happens, no entry written, no interruption survived, no resume demonstrated.

**Recommended default and causal basis.** Show the agent checkpointing mid-loop with named tests and next steps, then a fresh session executing next step one without rereading the transcript. The schema's value is only visible across an interruption, so a journey that never loses context cannot show why the fields matter.

**Operating conditions and assumptions.** The extension keeps the seed persona, starting state, decision, and trigger so the arc stays anchored. The scenario illustrates one representative interruption-and-resume arc, not a claim that every task hits context loss.

**Failure boundary and alternatives.** A journey without a resume event argues the journal is bookkeeping, the exact belief that kills compliance. Bounded alternatives and recoveries: add a contrast mini-journey where a missing next step stalls the resume, or anchor to this corpus's own Alpha journal as a lived example.

**Counterexample, gotchas, and operational comparison.** A journey where the resume goes perfectly hides the failure modes, so the story should include one field the writer almost omitted. Good: a resume that starts by quoting the predecessor's next step. Bad: a journey ending at the team feels organized. Borderline: an illustrative synthetic arc labeled as such pending a logged real case.

**Verification, evidence, and uncertainty.** Walk the extended journey against the schema and confirm every stage names the field it reads or writes. This corpus's own Alpha lane journal, updated each batch and used to resume across continuations, is a live instance of the journey. How much journey detail transfers to readers versus a worked example is untested here.

**Second-order consequence.** The journey's hero is the second session, because the schema is written entirely for the reader who arrives with nothing.

**Revision decision.** Extend the journey through a written Green-phase entry, a session end, and a successor session resuming from the entry alone.

**Retained seed evidence.** The role-based opening, starting state, decision line, and reference opening trigger remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Role based opening scenario: The technical lead or implementation agent is starting from an ambiguous request that must become acceptance criteria and tests and needs a reference that turns source evidence into an executable next step.
Primary user starting state: The user has a `tdd_progress_journal_schema` task, one or more local source paths, and uncertainty about which pattern should drive implementation.
Decision being made: choosing the requirement IDs, negative cases, verification gates, and handoff evidence.
Reference opening trigger: Open this file when the task mentions tdd progress journal schema, any mapped local source path, or an adjacent workflow with the same failure mode.

## Decision Tradeoff Guide

**Decision supported.** This section helps decide how much journaling depth to adopt for a specific task. The seed table keys adopt, adapt, and avoid to generic evidence agreement instead of the variables that govern journaling cost, task length, interruption risk, and how many hands the work passes through.

**Recommended default and causal basis.** Adopt the full schema when work will cross a session or owner boundary, compress fields for short solo batches, and skip with a recorded reason otherwise. Full-schema entries pay on long multi-owner work, trimmed entries suit short solo work, and the wrong calibration either burns time or strands a successor.

**Operating conditions and assumptions.** Each row names its triggering task property, the cost accepted, and a journal-answerable verification question. The guide calibrates journaling depth for this theme and cannot excuse skipping the completion rules once an entry is being written at all.

**Failure boundary and alternatives.** Avoid chosen for a long task is discovered only at resume time, when the absent journal cannot be written retroactively. Bounded alternatives and recoveries: pilot the full schema on one batch before trimming, keep phase and next step mandatory even in compressed form, or let a reviewer set depth per task class.

**Counterexample, gotchas, and operational comparison.** Compressed entries tend to drop exactly the phase and test fields that make resumption possible. Good: full entries on a handoff-bound migration. Bad: skipping the journal on a refactor that then stretched across three sessions. Borderline: compressed entries on a day task, with phase and next step retained.

**Verification, evidence, and uncertainty.** Trace one adopt and one avoid decision to their outcomes in the journal record and check the skip notes were honest. The seed's four-row adopt-adapt-avoid-cost skeleton with verification prompts scaffolds the rekeyed conditions directly. The interruption-probability estimate driving the choice is subjective, so miscalibration risk never fully disappears.

**Second-order consequence.** Journaling depth is insurance pricing, and the premium should track the cost of losing the context, not the writer's enthusiasm.

**Revision decision.** Rekey adopt to multi-session or multi-owner work, adapt to compressed entries on short solo work, and avoid to one-sitting tasks with an explicit skip note.

**Retained seed evidence.** The Adopt when, Adapt when, Avoid when, and Cost of being wrong rows with their verification prompts remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| decision_option_name | when_to_choose_condition | tradeoff_cost_description | verification_question_prompt |
| --- | --- | --- | --- |
| Adopt when | local corpus and external evidence agree on the tdd progress journal schema pattern | fastest path, but can copy stale local assumptions | Does the selected pattern appear in the canonical source and current external evidence? |
| Adapt when | local sources are strong but public ecosystem guidance has changed | preserves repo fit, but requires explicit inference notes | Did the reference label the local fact, external fact, and combined inference separately? |
| Avoid when | source evidence is thin, conflicting, or unrelated to the user journey | prevents false confidence, but may require deeper research | Is there a confidence warning or adjacent reference route? |
| Cost of being wrong | wrong tdd progress journal schema guidance can send an agent to the wrong files, tests, or abstraction | wasted implementation loop and weaker verification | Would a reviewer know what to undo and what to inspect next? |

## Local Corpus Hierarchy

**Decision supported.** This section helps decide which mirrored copy of the schema is authoritative for citation and future edits. The seed hierarchy labels the 202602 copy canonical and the 202604 copy supporting although they are byte-identical, ranking a document against its own mirror.

**Recommended default and causal basis.** Cite the 202604 copy for current work, treat the 202602 copy as the historical mirror, and diff them before trusting either after any edit. The labels imply a content difference readers will hunt for, and the newer skill folder, not the older one, is where future edits will land.

**Operating conditions and assumptions.** Rows keep path, role, heading signals, and reviewer question, with the identity relation stated beside the roles. The hierarchy assigns retrieval priority within this corpus and does not decide which skill folder the archive should retire.

**Failure boundary and alternatives.** If either copy is edited alone the hierarchy inverts silently, with the canonical label pointing at the stale fork. Bounded alternatives and recoveries: hash both copies to catch divergence, ask the user which snapshot line is authoritative, or symlink one to the other in a separate cleanup task.

**Counterexample, gotchas, and operational comparison.** A canonical label on the older snapshot invites edits to the copy least likely to be read by future skills. Good: one citation naming the retainer copy with the mirror acknowledged. Bad: reconciling imaginary differences between identical files. Borderline: keeping both rows for discoverability with an explicit duplicate flag.

**Verification, evidence, and uncertainty.** Diff the copies now and after any archive edit, and check citations consistently name the chosen maintained copy. The byte-identical diff between the 202602 and 202604 schema files was verified during this evolution. Which snapshot lineage the repository owner considers canonical is their call, so the recency preference here is provisional.

**Second-order consequence.** In a monthly-snapshot archive, recency of the enclosing skill folder is a better canonicity signal than the row order someone once wrote.

**Revision decision.** Record the two rows as one schema mirrored across skill generations and prefer the newer 202604 retainer copy as the maintained location.

**Retained seed evidence.** The classification vocabulary line and both hierarchy rows with reviewer questions remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Classification vocabulary includes canonical, supporting, legacy, duplicate, and conflicting source roles.

| local_source_filepath_value | corpus_hierarchy_role | heading_signal_to_convert | reviewer_question_to_answer |
| --- | --- | --- | --- |
| agents-used-monthly-archive/codex-skills-202602/tdd-context-retainer-orchestrator-01/references/progress-journal-schema.md | canonical primary source | Progress Journal Schema; TDD Session State: [Date/Time]; Current Phase: [Red / Green / Refactor] | What guidance, warning, or example should this source contribute to Tdd Progress Journal Schema? |
| agents-used-monthly-archive/codex-skills-202604/tdd-task-progress-context-retainer/references/progress-journal-schema.md | supporting detail source | Progress Journal Schema; TDD Session State: [Date/Time]; Current Phase: [Red / Green / Refactor] | What guidance, warning, or example should this source contribute to Tdd Progress Journal Schema? |

## Theme Specific Artifact

**Decision supported.** This section helps decide what concrete artifact must exist before this reference counts as operational. The seed artifact names a RED/GREEN transcript with resume checkpoint but supplies only three abstract completion rules, never an actual schema-shaped entry a reviewer could inspect.

**Recommended default and causal basis.** Carry the schema's own example entry, the 2026-02-27 Green-phase message-dedupe checkpoint, as the reviewable artifact. An instantiated entry proves the template is fillable and shows what completeness looks like, which no rule statement can.

**Operating conditions and assumptions.** The artifact entry satisfies every minimal completion rule and is distinguishable from template placeholders. The artifact certifies this reference is operational and does not require every future task to reproduce it.

**Failure boundary and alternatives.** An artifact filled with placeholder brackets instead of task facts certifies only that the template was copied. Bounded alternatives and recoveries: point at this corpus's live Alpha journal entries instead, synthesize a fresh labeled example, or keep both a borrowed and a lived instance.

**Counterexample, gotchas, and operational comparison.** An example entry ages as conventions evolve, and a borrowed example can be mistaken for this corpus's own work history. Good: the dedupe example entry with failing and passing tests named. Bad: a template with brackets left in. Borderline: a lived entry that merges two fields but satisfies every rule.

**Verification, evidence, and uncertainty.** Check the artifact entry against each minimal completion rule and confirm a reader can state its phase, tests, and next action. The schema file's example entry demonstrates all eight fields filled with concrete task facts including a p95 metric. Whether a borrowed example teaches as well as a lived one from this corpus is untested.

**Second-order consequence.** The schema file already ships a worked entry, so the artifact's cheapest honest form is adopting and attributing that example.

**Revision decision.** Instantiate one complete journal entry, real date, phase, named tests with statuses, implementation surface, focus, numbered steps, notes, and metrics.

**Retained seed evidence.** The worked-example definition line and the three artifact field rows with completion rules and evidence hints remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Theme specific artifact: RED/GREEN transcript with refactor rule and resume checkpoint.

| artifact_field_name | artifact_completion_rule | evidence_source_hint |
| --- | --- | --- |
| user_goal_statement | state the user's concrete goal before applying Tdd Progress Journal Schema | local corpus hierarchy plus critique findings |
| decision_boundary_rule | define the point where this reference should be used or avoided | decision tradeoff guide |
| verification_gate_rule | define the command, checklist, or review question that proves the artifact worked | verification gate command set |

## Worked Example Set

**Decision supported.** This section helps decide which journal entries should be taught as exemplary, negligent, or conditionally acceptable. The seed examples restate generic load-canon verdicts and never show an actual journal entry judged good, bad, or borderline against the schema's rules.

**Recommended default and causal basis.** Grade entries by asking whether a successor could resume from this alone, and let that single question drive all three verdicts. Judgment transfers through inspectable instances, and entry quality is easiest to teach by contrasting a resumable entry with a vague one.

**Operating conditions and assumptions.** Each example names the entry's visible features, the rule applied, and the resume consequence that justifies the verdict. The examples grade journal entries, not the underlying engineering work the entries describe.

**Failure boundary and alternatives.** Verdicts about abstract usage cannot be applied by a reviewer holding a concrete entry that needs a pass-or-bounce call. Bounded alternatives and recoveries: draw examples from this corpus's own journals, add a fourth case for a stale entry never updated after a pivot, or pair each verdict with its registry row.

**Counterexample, gotchas, and operational comparison.** Wordcount masquerades as quality, and a lengthy entry can still omit the one field a resume needs. Good: an entry naming a failing dedupe test and three numbered steps. Bad: a paragraph of confident prose with no test names. Borderline: a one-line entry on a trivial batch carrying phase and next step only.

**Verification, evidence, and uncertainty.** Reproduce each verdict by scanning the described entry against the minimal completion rules and confirming the outcome matches. The schema's example entry and completion rules provide the grading standard the recast verdicts apply. Which entry pathologies dominate in this team's real journals is unknown, so the chosen cases reflect expected failure shapes.

**Second-order consequence.** The bad example teaches most when it looks superficially diligent, long, confident, and unresumable.

**Revision decision.** Recast the three verdicts around entry quality, a complete phase-honest entry, a nameless diary line, and a compressed but rule-satisfying note.

**Retained seed evidence.** The good, bad, and borderline example lines with their original verdict framing remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Good example: Use Tdd Progress Journal Schema after loading the canonical source, confirming the external evidence boundary, and writing a verification gate before implementation.
Bad example: Use Tdd Progress Journal Schema as a generic tutorial while ignoring the mapped local paths, source hierarchy, and cost of being wrong.
Borderline case: Use Tdd Progress Journal Schema only after adding a confidence warning when local evidence is thin or conflicts with current ecosystem guidance.

## Outcome Metrics and Feedback Loops

**Decision supported.** This section helps decide which observable signals should trigger revising the journal discipline or this reference. The seed metrics track requirement-ID coverage and specs evidence, inherited from spec themes, and measure nothing about journal health, resume success, entry completeness, or checkpoint cadence.

**Recommended default and causal basis.** Measure entries against the completion rules at write time, track how many resumes needed information beyond the journal, and review at skill-revision boundaries. This reference improves outcomes through successful resumptions, so its instruments must watch resume events and entry completeness, not requirement traceability.

**Operating conditions and assumptions.** Each metric states its unit, collection point, healthy range, breach action, and owner. These metrics gauge the journal discipline this reference teaches, not the delivery speed of the underlying work.

**Failure boundary and alternatives.** A signal that only fires when a resume has already failed measures the disaster, not the drift that caused it. Bounded alternatives and recoveries: sample audits of random entries instead of continuous counters, successor-graded resume scoring, or a staleness alarm wired into the batch cadence.

**Counterexample, gotchas, and operational comparison.** Counting entries rewards volume over completeness, and self-graded resume success inflates quietly. Good: tightening the cadence after a resume needed transcript archaeology. Bad: celebrating entry counts while half lack next steps. Borderline: skipping a review in a period with no interrupted sessions, with the skip noted.

**Verification, evidence, and uncertainty.** Audit recent resumes for information the journal lacked and check each identified gap led to a rule or cadence change. The seed's review cadence line ties re-verification to edits and releases, a loop the resume-focused metrics extend. Healthy baselines for resume success and staleness are unmeasured, so first thresholds are provisional.

**Second-order consequence.** Checkpoint staleness, the gap between the last entry and current work, is the leading indicator, because every resume failure begins as a stale journal.

**Revision decision.** Adopt resume-success rate, completion-rule violations per entry, and checkpoint staleness as the primary signals, each with a breach action on a named section.

**Retained seed evidence.** The leading indicator, failure signal, and verifier-driven review cadence lines remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Leading indicator: every shipped claim has a requirement ID and fresh verification evidence.
Failure signal: the reference describes TDD or specs without showing failing and passing evidence.
Review cadence: Re-run the verifier after every generated-reference edit and refresh external sources when public APIs, docs, or tooling releases change.

## Completeness Checklist

**Decision supported.** This section helps decide when this reference may be declared ready to hand to an agent. The seed checklist confirms generic sections exist and never checks the schema-specific obligations, that the artifact entry satisfies the completion rules and that every schema field appears somewhere in this reference.

**Recommended default and causal basis.** Tick structural items with citations, then verify field coverage by listing the template's eight fields against this document's text. This document is about a field contract, so its readiness check must confirm the contract is fully represented, not just that prose sections exist.

**Operating conditions and assumptions.** Each item names its target section, the satisfying evidence, and whether a script or human checks it. The checklist gates this document's readiness, not the quality of journals later written under it.

**Failure boundary and alternatives.** A reference that omits one schema field would still pass the current checklist and then propagate the omission to every downstream journal. Bounded alternatives and recoveries: generate field-coverage items mechanically from the schema template, spot-check two random fields deeply per review, or pair-review the artifact entry.

**Counterexample, gotchas, and operational comparison.** Field coverage can pass while descriptions contradict the source schema, so coverage and fidelity need separate ticks. Good: a field-coverage tick citing the line documenting Context Notes. Bad: all ticks green from a headings glance. Borderline: carrying forward last review's field tick with a staleness note.

**Verification, evidence, and uncertainty.** List the schema's fields, grep this document for each, and validate the artifact entry against every completion rule. The seed's seven structural items map onto real sections here and anchor the added field-coverage layer. How much fidelity checking each field needs per revision depends on edit volume, so depth stays judgment.

**Second-order consequence.** A checklist for a schema document is itself a schema, and it inherits the same failure mode, silently missing fields.

**Revision decision.** Append items requiring all eight entry fields to be documented, the completion rules restated, and the artifact entry validated against them.

**Retained seed evidence.** All seven structural checklist items covering scenario, decision guide, hierarchy, artifact, examples, metrics, and routing remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- The role scenario names the user, starting state, decision, and trigger for Tdd Progress Journal Schema.
- The decision guide includes Adopt when, Adapt when, Avoid when, and Cost of being wrong.
- The local corpus hierarchy identifies canonical and supporting sources or gives a confidence warning.
- The theme specific artifact is concrete enough to review without reading every mapped source.
- The examples cover good, bad, and borderline usage.
- The metrics section names one leading indicator and one failure signal.
- The adjacent routing section points to a better reference when this one is not the right fit.

## Adjacent Reference Routing

**Decision supported.** This section helps decide when a question should leave this reference and which neighbor owns it. The seed section splits the theme name into tdd, progress, and journal keywords aimed at unnamed destinations instead of routing by question type to real corpus files.

**Recommended default and causal basis.** Route how-to-split-work questions to the subagent development execution patterns reference, artifact-validation questions to the writing skills validation reference, and keep entry-format questions here. Readers leave this reference with distinct needs, task-decomposition questions, subagent-execution questions, validation questions, and each has an actual evolved neighbor in this corpus.

**Operating conditions and assumptions.** Each route names its trigger, a destination that resolves to a real file, the context carried, and what stays here. Routing redirects within this corpus and cannot decide priorities or authorize work in a destination's domain.

**Failure boundary and alternatives.** Keyword routes point at references that exist only as words, so a reader following them lands nowhere. Bounded alternatives and recoveries: consult the corpus index for exact titles before adding routes, keep unresolved needs here with a gap note, or escalate genuine ownership overlap to the user.

**Counterexample, gotchas, and operational comparison.** Journal questions masquerade as process questions, and over-eager routing scatters a reader who needed one field definition. Good: sending a lane-ownership question to the subagent execution reference while keeping the checkpoint-format question here. Bad: routing to the progress adjacent reference, a keyword with no file. Borderline: answering a small execution question inline with a route noted for depth.

**Verification, evidence, and uncertainty.** Resolve each named destination to an existing corpus file and walk one sample question through each trigger. The subagent development execution patterns reference evolved earlier in this same Alpha lane is a verified resolvable destination. The best split between answering inline and routing away depends on question depth, so borderline calls stay recorded judgment.

**Second-order consequence.** This theme is the connective tissue of the corpus, since nearly every long task journals, so its routes see more traffic than most.

**Revision decision.** Replace keyword stubs with condition-keyed routes to named neighbors, execution-pattern questions to the subagent development reference and writing-validation questions to the writing-skills reference.

**Retained seed evidence.** The adjacency guidance line and the three keyword-derived route stubs remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Adjacent reference guidance: Use TDD, traceability, or completion verification references when the work is already scoped.
Adjacent reference 1: consider the tdd adjacent reference when the current task pivots away from tdd progress journal schema.
Adjacent reference 2: consider the progress adjacent reference when the current task pivots away from tdd progress journal schema.
Adjacent reference 3: consider the journal adjacent reference when the current task pivots away from tdd progress journal schema.

## Workload Model

**Decision supported.** This section helps decide how much work may accumulate between journal entries before a checkpoint becomes mandatory. The seed model bounds work at twenty requirement IDs and one traceability matrix, spec-theme units, and its source-pressure cell truncates mid-list, while journaling workload is really bounded by batch size between checkpoints.

**Recommended default and causal basis.** Checkpoint at every phase transition and at most every few sections or components, whichever comes first. The risk this schema manages is context accumulating unjournaled, so the natural workload unit is the batch a single entry must cover.

**Operating conditions and assumptions.** The model tracks work since last entry, phase transitions crossed, and components touched in the active batch. The model bounds journaling cadence and entry scope, not the engineering workload the journal reports on.

**Failure boundary and alternatives.** A session honoring requirement-ID caps can still run six hours without a checkpoint, losing everything the model was meant to protect. Bounded alternatives and recoveries: time-based checkpointing for exploratory work, event-based checkpointing on phase transitions, or tool-enforced cadence via an orchestrator script.

**Counterexample, gotchas, and operational comparison.** Flow states stretch batches past what one entry can honestly summarize, and the model must bite exactly then. Good: an entry after each three-section batch in this corpus's own evolution work. Bad: a day of refactoring summarized as cleanup in one line. Borderline: a stretched batch checkpointed late with the overrun noted.

**Verification, evidence, and uncertainty.** Measure work volume between consecutive entries in real journals and test whether oversized batches produced thinner entries. The schema's multi-component tracking section presumes bounded batches whose touched components can be listed exhaustively. The optimal batch size varies by task texture, so the stated cadence is a defensible default rather than a derived constant.

**Second-order consequence.** Batch size and entry quality trade against each other, because a checkpoint covering too much work cannot name all its tests honestly.

**Revision decision.** Rederive the boundary as one entry per coherent batch, checkpoint before any risky operation, and never more than a session between entries, repairing the truncated cell.

**Retained seed evidence.** The four workload dimensions with their boundary values and verification pressure points remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

`combined_evidence_inference_note`: Treat Tdd Progress Journal Schema as a quality gate operating reference, not as a prose summary.

| workload_dimension_name | workload_boundary_value | verification_pressure_point |
| --- | --- | --- |
| primary_usage_surface | specification, test, review, and verification work where the artifact must turn ambiguous intent into executable evidence | verify that the reference changes the next implementation or review action |
| bounded_capacity_model | one requirement packet, 20 requirement IDs or fewer, one traceability matrix, and one final gate command set | split the task or create a narrower reference when this boundary is exceeded |
| source_pressure_model | local heading signals include Progress Journal Schema; TDD Session State: [Date/Time]; Current Phase: [Red / Green / Refactor]; Tests Written:; Implementation Progress:; Current Fo | compare guidance against canonical local sources before following external examples |
| artifact_pressure_model | required artifact is RED/GREEN transcript with refactor rule and resume checkpoint | require the artifact before claiming the reference is operationally usable |

## Reliability Target

**Decision supported.** This section helps decide what measurable reliability this reference must demonstrate before its guidance is trusted. The seed table demands perfect boundary preservation and 18-of-20 decision accuracy with no sampling procedure, population, or owner, and no target about what this theme actually promises, resumability.

**Recommended default and causal basis.** Keep the four dimensions grounded with methods, and lead with resume tests sampled from live journals at review boundaries. Unmeasurable targets decay into decoration, while resumability is concretely testable by handing an entry to a context-free reader.

**Operating conditions and assumptions.** Each target names its metric, sampling method, population, owner, and the corrective action a miss triggers. The targets judge this reference and the journal discipline, not the reliability of the software the journals describe.

**Failure boundary and alternatives.** Quoting the percentages as achieved performance manufactures rigor the corpus has never measured. Bounded alternatives and recoveries: binary pass-fail resume audits, pooling samples across the corpus's journaling themes, or defect review of every failed resume instead of rates.

**Counterexample, gotchas, and operational comparison.** The cold reader in a resume test is often not truly cold, having skimmed the transcript, which inflates the score. Good: three sampled entries resumed cleanly by a fresh session, logged. Bad: reporting the 18-of-20 figure nobody sampled. Borderline: a resume test done by a warm reader, recorded with that caveat.

**Verification, evidence, and uncertainty.** Run one genuine cold-reader resume test per review cycle and audit the boundary labels on a text sample. The four seed dimensions correspond to failure classes this corpus documents, label loss, misrouting, unsupported claims, and dead ends. No baseline exists for any threshold here, so the first measured cycle defines what is achievable.

**Second-order consequence.** Resumability is this theme's one target that can be tested cheaply and often, one entry and one cold reader at a time.

**Revision decision.** Add a resumability target, a sampled successor can resume from a random entry, and mark every threshold unbaselined with a named measurement owner.

**Retained seed evidence.** All four reliability rows with their threshold values and evidence-collection methods remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| reliability_target_name | measurable_threshold_value | evidence_collection_method |
| --- | --- | --- |
| source_boundary_preservation | 100 percent of recommendations keep local, external, and inference boundaries visible | review generated text for the three evidence labels before reuse |
| decision_accuracy_sample | at least 18 of 20 sampled uses route to the correct adopt, adapt, avoid, or adjacent-reference decision | sample downstream tasks and record reviewer verdicts |
| unsupported_claim_rate | zero unsupported production, security, latency, or reliability claims in final guidance | reject claims without source row, explicit inference note, or verification method |
| recovery_path_clarity | every avoid or failure case names the rollback, escalation, or next-reference route | inspect failure-mode and adjacent-routing sections together |

## Failure Mode Table

**Decision supported.** This section helps decide which failures in the journal fabric deserve standing mitigations. The seed table carries two hygiene rows plus green-check and metric-claim rows and omits the journal fabric failures, stale checkpoints, phase drift, entry-transcript divergence, and journals abandoned mid-task.

**Recommended default and causal basis.** Detect staleness by comparing last-entry time against work activity, and detect divergence by spot-checking entry claims against the repository state. Triage at a broken resume needs rows describing how journals fail, ranked by silence, and every journal failure is silent until resumption.

**Operating conditions and assumptions.** Each row names its trigger, earliest observable signal, blast radius at resume, containment, and correction. The table covers journal-keeping failures, while test-suite and code failures belong to the work the journal documents.

**Failure boundary and alternatives.** Rows are worthless if their earliest signal fires only after the resume has already stalled. Bounded alternatives and recoveries: wire staleness alarms into the batch cadence, require entry updates in the definition of done, or audit divergence on a sampled basis.

**Counterexample, gotchas, and operational comparison.** Phase drift begins the moment work pivots without an entry update, and it looks identical to diligence from outside. Good: a staleness alarm firing before a risky rewrite began. Bad: a resume executing next steps that no longer matched the code. Borderline: a knowingly stale journal during a hotfix, flagged and repaired immediately after.

**Verification, evidence, and uncertainty.** Seed one failure per row in a drill and confirm the named signal fires before a simulated resume would rely on the bad entry. The schema's checkpoint-per-entry mandate exists precisely because these decay modes were anticipated by its authors. Observed frequency of each journal failure in this team's history is unmeasured, so ordering encodes expected silence.

**Second-order consequence.** A journal that contradicts the work is worse than no journal, because a resume trusts it exactly where it lies.

**Revision decision.** Add stale-checkpoint, phase-drift, divergence-from-actual-work, and abandoned-journal rows with write-time detection signals.

**Retained seed evidence.** All four seed failure rows with their triggers and mitigation actions remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| failure_mode_name | likely_trigger_condition | required_mitigation_action |
| --- | --- | --- |
| source drift hides truth | external or local guidance changes after the reference was written | refresh public evidence, rerun local corpus gate, and mark stale claims before reuse |
| generic advice escapes review | agent copies plausible best practices without theme-specific verification | block completion until the verification gate names concrete command, reviewer question, or metric |
| green check misses requirement | test command passes while a requirement lacks traceability | audit every REQ ID against at least one test or review assertion |
| metric claim has no method | performance or reliability language appears without measurement | replace claim with threshold, fixture, command, and owner |

## Retry Backpressure Guidance

**Decision supported.** This section helps decide when a failed journal write or insufficient resume should be retried, escalated, or halted. The seed bullets classify verification failures and cap retries but never define journal-specific semantics, what to do when an entry cannot be written honestly or a resume finds the journal insufficient.

**Recommended default and causal basis.** Stop at any batch boundary where phase or test status cannot be stated, resolve the ambiguity, write the entry, then resume work. An unwritable entry means the work state is not understood, and pressing on multiplies the very confusion the journal exists to contain.

**Operating conditions and assumptions.** The guidance assumes batch boundaries where writing is expected and artifacts, diffs, and test output from which one reconstruction can be attempted. This governs journal-write and resume retries, not retries of the tests and builds the journal reports.

**Failure boundary and alternatives.** Retrying the resume against the same insufficient journal reproduces the stall, since the missing context is not in the file. Bounded alternatives and recoveries: escalate immediately when reconstruction sources are missing, ask the predecessor session's owner where possible, or restart the batch from the last good checkpoint.

**Counterexample, gotchas, and operational comparison.** The temptation is to write a vague entry and continue, which converts a loud failure into a silent one. Good: halting to rerun tests because the entry could not name what was failing. Bad: writing tests probably fine and continuing. Borderline: one reconstruction from git diff and test logs, labeled reconstructed, then escalation.

**Verification, evidence, and uncertainty.** Audit halted batches for whether the ambiguity was resolved before work resumed, and resumes for reconstruction-before-escalation ordering. The seed's classification-before-retry rule and checkpoint-before-destructive-step bullet transfer directly to journal semantics. How often honest-entry failure occurs in practice is unmeasured, and the single-reconstruction budget is a defensible default.

**Second-order consequence.** Inability to write a checkpoint is itself the highest-value signal, because it means the current state would already fail a resume.

**Revision decision.** Add journal semantics, halt work when an honest entry cannot be written, and on an insufficient resume reconstruct once from artifacts then escalate with the gap named.

**Retained seed evidence.** All five retry and backpressure bullets, including the one-owner-per-file rule, remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- Retry only after the failed verification signal is classified as transient, stale evidence, missing context, or true contradiction.
- Use one bounded retry for stale external evidence refresh, then escalate to a human or a narrower source-specific reference.
- Apply backpressure by stopping new generation or implementation work when source coverage, critique coverage, or verification gates are red.
- For long-running agent workflows, checkpoint after each batch and re-read the current spec before any broad rewrite, commit, push, or destructive operation.
- For distributed execution, assign one owner per generated file or theme batch and require merge-time verification of exact path, heading, and evidence-boundary invariants.

## Observability Checklist

**Decision supported.** This section helps decide what evidence must exist that the journal itself remains an honest instrument. The seed bullets recycle source-loading and latency records and never treat the journal itself as the observability instrument whose own health needs watching.

**Recommended default and causal basis.** Record scan results beside each entry, keep timestamps honest, and cross-check one claim per review against the repository state. In this theme the journal is the telemetry, so observability means keeping the instrument honest, entries timely, fields complete, and claims consistent with artifacts.

**Operating conditions and assumptions.** Entries carry timestamps, artifacts like diffs and test output are retained, and someone reviews the cross-checks. This covers observing journal health, while the journal itself observes the work, two layers that must not be conflated.

**Failure boundary and alternatives.** Meta-records about the journal can outgrow the journal, doubling the writing burden that already competes with work. Bounded alternatives and recoveries: script the completeness scan into the checkpoint routine, sample cross-checks rather than auditing every entry, or accept commit metadata as an independent activity trace.

**Counterexample, gotchas, and operational comparison.** Self-reported completeness drifts optimistic, and timestamp gaps are invisible unless someone actually compares them to activity. Good: a review catching an entry claiming a pass the test log contradicts. Bad: meta-dashboards about journaling nobody reads. Borderline: skipping the cross-check in a period with no resumes, noted for the next review.

**Verification, evidence, and uncertainty.** Compare entry timestamps against commit times, rerun the completeness scan over the journal, and cross-check one sampled claim per cycle. This corpus's own journals pair each claim with named test or verifier output, the cross-checkable pattern this checklist generalizes. The sampling rate that keeps the instrument honest without doubling overhead is untuned.

**Second-order consequence.** A journal is trustworthy exactly to the degree its claims are spot-checkable against artifacts that did not pass through the writer.

**Revision decision.** Recenter the checklist on instrument health, entry timestamps against work activity, completion-rule scan results, and spot-checks of entry claims against diffs and test output.

**Retained seed evidence.** All six observability bullets including the small-audit-evidence preference remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- Record which local sources were loaded and which were intentionally skipped.
- Record the exact verification command, reviewer question, or rendered artifact used as proof.
- Record p50/p95/p99 latency or reviewer-time measurements when the reference affects runtime or workflow speed.
- Capture reviewer decision, unresolved uncertainty, and next refresh trigger.
- Record leading indicator and failure signal from this file in the coverage manifest or journal when the reference drives real work.
- Keep audit evidence small enough to review: command output summary, changed-file list, and unresolved-risk notes are preferred over raw transcript dumps.

## Performance Verification Method

**Decision supported.** This section helps decide how to prove this schema's benefit exceeds its writing overhead. The seed method demands full REQ-to-test mapping and latency packets, spec-theme machinery, while this schema's performance is resume speed and checkpoint overhead, neither of which is mentioned.

**Recommended default and causal basis.** Time a sampled resume from journal-open to first productive action and log approximate writing time per entry alongside it. The schema performs well when resumes are fast and checkpoint writing stays cheap, so verification must time those two paths, not requirement traceability.

**Operating conditions and assumptions.** The method assumes journaled and comparable unjournaled tasks exist, resumes get sampled, and times are recorded honestly. This evaluates the schema's operational cost and benefit, not the performance of the software under development.

**Failure boundary and alternatives.** The two measures trade off, since richer entries speed resumes but cost more to write, and measuring only one hides the trade. Bounded alternatives and recoveries: count context questions a resuming session must ask instead of timing, run paired tasks with and without journals, or accept reviewer judgment as interim evidence.

**Counterexample, gotchas, and operational comparison.** Resume speed depends on task difficulty as much as journal quality, so single-sample comparisons mislead. Good: a resume reaching productive work in minutes by executing next step one. Bad: quoting p99 figures for markdown writing. Borderline: one paired comparison logged with an explicit sample-of-one caveat.

**Verification, evidence, and uncertainty.** Collect resume times and entry costs across several cycles and publish the ratio with its sample size. The seed's pass condition, a reviewer identifies the correct next action without reading unrelated files, is precisely a resume-speed criterion. Overhead and benefit vary widely by task texture, so early ratios deserve low-confidence labels.

**Second-order consequence.** The schema's return on investment is concentrated in its worst case, the resume that would otherwise require full transcript archaeology.

**Revision decision.** Measure minutes from session start to first productive action on resumes, and entry-writing time per checkpoint, comparing against unjournaled task baselines.

**Retained seed evidence.** The performance method line, both indicator lines, the measurement packet, and the pass and fail conditions remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Performance method: require 100 percent REQ-to-test mapping and fail closed when any claim lacks a verification command or review assertion.
Leading indicator to measure: every shipped claim has a requirement ID and fresh verification evidence.
Failure signal to watch: the reference describes TDD or specs without showing failing and passing evidence.
Required measurement packet: capture input size, source count, tool-call count, wall-clock time, p50/p95/p99 latency where runtime applies, and reviewer decision time where documentation applies.
Pass condition: the reference must let a reviewer identify the correct next action, verification gate, and stop condition without reading unrelated files.
Fail condition: the reference encourages implementation before the workload, reliability target, and failure-mode table are explicit.

## Scale Boundary Statement

**Decision supported.** This section helps decide at what scale a single schema-shaped journal stops sufficing and what structure replaces it. The seed statement recites multi-system and SLO limits and misses the journal-specific scale walls, entries ballooning past skimmability, many agents sharing one journal, and journals outliving their tasks unarchived.

**Recommended default and causal basis.** One journal per lane per task, a summary entry every dozen or so entries, and archive on task completion. Journals fail at scale through interleaving and bloat, since a resume must skim history linearly and concurrent writers shred the phase field's meaning.

**Operating conditions and assumptions.** The boundaries assume identifiable lanes, a place to archive, and resumes that read recent entries rather than whole histories. The boundaries bound the journal discipline, not the size of the engineering effort being journaled.

**Failure boundary and alternatives.** A shared phase field is undefined when three lanes write concurrently, which is a structural limit no writing discipline fixes. Bounded alternatives and recoveries: rolling summaries at the journal head, an index entry pointing at milestones, or a fresh journal per continuation with a handoff entry linking back.

**Counterexample, gotchas, and operational comparison.** Archiving too eagerly destroys the history a late audit needs, so archives must stay retrievable. Good: splitting into alpha through delta lane journals when four owners started writing. Bad: one interleaved journal for four concurrent lanes. Borderline: a long single-owner journal kept skimmable with periodic summary entries.

**Verification, evidence, and uncertainty.** Measure resume skim time as histories grow and confirm multi-writer journals show interleaving damage before prescribing splits. This repository's master-plus-lane journal layout is a working instance of the sharding boundary described here. The entry count where skimmability degrades is unmeasured, so the dozen-entry summary cadence is a heuristic.

**Second-order consequence.** This corpus already sharded, master journal for Red-Green-Refactor transitions and lane journals for batch detail, which is the pattern the boundary prescribes.

**Revision decision.** Add journal-scale signals, per-lane journals once writers multiply, summarize-and-archive once history exceeds a skimmable length, and close journals when tasks end.

**Retained seed evidence.** All four scale boundary statements including the distributed split and context-drift rules remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

Tdd Progress Journal Schema stops being sufficient when the task spans multiple independent systems, more than one ownership boundary, unbounded source discovery, or production traffic without an explicit SLO.
Under distributed execution, split work by theme file and preserve one verification owner per split; do not let parallel agents rewrite the same reference without a merge checkpoint.
Under long-running agent workflows, treat context drift as a reliability failure: checkpoint state, summarize open risks, and verify against the spec before continuing.
Under large-codebase scale, require dependency or source-graph narrowing before applying this reference; a source list without ranked canonical guidance is not enough.

## Future Refresh Search Queries

**Decision supported.** This section helps decide which future searches would genuinely refresh this reference's external evidence. The seed query table drops the internal theme name into three templates whose literal phrasing targets a coinage no external author uses.

**Recommended default and causal basis.** Search for agent context-persistence and session-handoff patterns on a periodic trigger, feeding the external map and thesis rather than the schema fields. Useful refresh queries speak the ecosystem's vocabulary, agent memory management, session handoff, checkpoint-resume workflows, not this corpus's file-naming scheme.

**Operating conditions and assumptions.** Each query names its target section, source type, and firing trigger. The queries refresh external analogues for this theme, while the schema itself changes only through repository edits.

**Failure boundary and alternatives.** Empty results from a coinage query, logged as freshness confirmed, convert search blindness into false confidence. Bounded alternatives and recoveries: follow the agents.md format's own changelog, track the Codex guide for instruction-file convention shifts, or drive refresh from dated retrieval records.

**Counterexample, gotchas, and operational comparison.** The agent-memory space is noisy with marketing content, so result quality screening matters more here than in framework themes. Good: a query on session-resume patterns for coding agents feeding the external map. Bad: searching the literal theme title and logging zero hits as freshness. Borderline: adopting a well-argued practitioner post with an inference label pending corroboration.

**Verification, evidence, and uncertainty.** Run each query once, grade the top results for on-topic value, and rewrite phrasings that return mostly noise. The seed's three-row structure targeting docs, repositories, and release notes is sound scaffolding for the revised vocabulary. Which phrasings will track this fast-moving vocabulary is unknowable in advance, so the queries need their own review cadence.

**Second-order consequence.** This theme sits where agent-memory research is most active, so its external landscape shifts faster than the stable local schema.

**Revision decision.** Rephrase toward ecosystem vocabulary, agent session persistence patterns, TDD workflow journaling practices, and AGENTS.md convention updates, each tied to the section it refreshes.

**Retained seed evidence.** All three labeled query rows with their official-docs, repository, and release-notes targets remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

| search_query_label_name | search_query_text_value |
| --- | --- |
| `official_docs_query_phrase` | tdd progress journal schema official documentation best practices |
| `github_repository_query_phrase` | tdd progress journal schema GitHub repository examples |
| `release_notes_query_phrase` | tdd progress journal schema changelog release notes migration |

## Evidence Boundary Notes

**Decision supported.** This section helps decide how statements in this reference must be labeled so readers know what each claim rests on. The seed notes define the three labels but ignore this file's specific hazards, mirrored local sources that could double-count and external rows that are analogues rather than sources.

**Recommended default and causal basis.** Label per claim, cite the schema mirror pair as one source, and mark anything derived from the unretrieved URLs as inference pending a dated retrieval. Downstream confidence calibrates on these labels, and an analogue labeled as external fact claims documentary support the URL never gave.

**Operating conditions and assumptions.** Labels stay stable corpus-wide, and every combined-inference clause names the local and external inputs it merges. The notes govern labeling in this reference and its reuses, not the ranking of sources, which other sections own.

**Failure boundary and alternatives.** Labels applied per section rather than per claim let one labeled sentence launder its unlabeled neighbors. Bounded alternatives and recoveries: introduce an explicit analogue-inspiration tag, inline labels parenthetically on key claims, or index claims to labels during verification.

**Counterexample, gotchas, and operational comparison.** Packet and prompt reuse strips labels mechanically, so load-bearing claims need labels embedded in their own sentences. Good: the completion rules cited as local fact from the schema file with the mirror noted. Bad: journal fields presented as AGENTS.md-endorsed practice. Borderline: an ecosystem-vocabulary claim labeled inference until a retrieval dates it.

**Verification, evidence, and uncertainty.** Sample load-bearing claims, confirm correct labels, and verify no external-fact label exists without a recorded retrieval. The three seed definitions match the corpus-wide label vocabulary and the boundary-preservation target elsewhere in this file. Label durability through packet reuse and prompt quotation is unaudited, so leakage risk remains an assumption.

**Second-order consequence.** The honest tier for an unretrieved analogue sits below external fact, and naming that tier prevents quiet promotion.

**Revision decision.** Add rules counting the mirrored schema copies as one local source and requiring analogue-derived external claims to carry an inference downgrade until retrieval.

**Retained seed evidence.** All three label definitions, local fact, external fact, and combined inference, remain preserved. The original source facts, examples, and tables follow so that the evolved guidance remains auditable.

- `local_corpus_sourced_fact`: statements tied directly to the local source paths above.
- `external_research_sourced_fact`: statements tied to the public URLs above.
- `combined_evidence_inference_note`: synthesis that combines local and public evidence into agent guidance.
