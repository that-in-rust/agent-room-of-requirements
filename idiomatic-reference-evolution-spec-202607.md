# Idiomatic Reference Evolution Specification

> **Status:** Ready for Pass One execution
> **Working corpus:** `idiomatic-ref-202607/`
> **Semantic queue:** [`idiomatic-reference-evolution-tasks-202607.csv`](<idiomatic-reference-evolution-tasks-202607.csv>)
> **Method:** Four parallel agents, one permanent owner per file, one task row per Markdown semantic block

The job is simple: read each owned file completely, answer ten questions comprehensively for each header-defined section, evolve that section's semantic blocks from those answers, add substantial new insight, reconcile the section, then reread the entire rewritten file skeptically.

The CSV is the execution source of truth. This specification defines how its rows are parsed, assigned, processed, and verified.

## Executable Requirements

### Measured Execution Packet

The queue is derived programmatically from the frozen `20260710` working copies before any evolution edits begin.

| measured_property | measured_value |
| --- | ---: |
| Working reference files | 99 |
| Total physical source lines | 20,802 |
| Structural headings | 2,574 |
| Headings per file | 26 |
| Semantic review blocks | 11,961 |
| Minimum blocks per file | 113 |
| Median blocks per file | 118 |
| Maximum blocks per file | 158 |
| Minimum lines per block | 1 |
| Median lines per block | 2 |
| Maximum lines per block | 7 |
| CSV rows including header | 11,962 |
| CSV columns | 19 |

The parser produced these exact block types:

| block_type | task_rows |
| --- | ---: |
| `heading` | 2,574 |
| `paragraph` | 1,188 |
| `list_item` | 2,475 |
| `table_header` | 1,188 |
| `table_row` | 4,437 |
| `code_block` | 99 |
| **Total** | **11,961** |

This is semantic rather than arbitrary line-count chunking. Paragraphs, list items, and table rows become small tasks; code fences remain intact.

### Actors And Boundaries

| actor | responsibility | write_boundary |
| --- | --- | --- |
| Coordinator | Freeze the queue, start four workers, validate progress, and run final gates | CSV status and audit fields only; no specialist prose edits |
| `evolve_reference_sections_alpha` | Evolve its preassigned files in `agent_file_order` | Only files whose CSV rows name this agent |
| `evolve_reference_sections_beta` | Evolve its preassigned files in `agent_file_order` | Only files whose CSV rows name this agent |
| `evolve_reference_sections_gamma` | Evolve its preassigned files in `agent_file_order` | Only files whose CSV rows name this agent |
| `evolve_reference_sections_delta` | Evolve its preassigned files in `agent_file_order` | Only files whose CSV rows name this agent |

The agent names follow the four-word naming convention. All workers use the same reasoning method; they differ only in immutable whole-file assignments.

### Predetermined Agent Loads

The finer breakdown preserves the previous path-to-agent map exactly.

| agent_id | assigned_files | semantic_tasks | source_lines |
| --- | ---: | ---: | ---: |
| `evolve_reference_sections_alpha` | 25 | 3,018 | 5,251 |
| `evolve_reference_sections_beta` | 25 | 3,020 | 5,252 |
| `evolve_reference_sections_gamma` | 25 | 3,017 | 5,250 |
| `evolve_reference_sections_delta` | 24 | 2,906 | 5,049 |

The exact ownership manifest is materialized on every CSV row. Filtering by `agent_id` and deduplicating `reference_file_path` reveals each agent's complete file list.

### Programmatic Block Rules

The queue SHALL be derived from a CommonMark and GitHub-Flavored Markdown syntax tree with source positions.

1. Every heading is one `heading` block and establishes section context for following blocks.
2. Every root paragraph is one `paragraph` block.
3. Every direct item in a root list is one `list_item` block; nested content remains with its direct parent item.
4. Every GFM table header plus delimiter is one `table_header` block.
5. Every GFM table data row is one `table_row` block.
6. Every fenced or indented code node is one indivisible `code_block`, including Mermaid diagrams.
7. Blockquotes, HTML blocks, thematic breaks, definitions, and other root block nodes remain individually atomic when encountered.
8. Heading-like text inside code fences SHALL never become a heading or a separate block.
9. Selected block starts are ordered by source position. Each span ends immediately before the next selected block starts.
10. The first span begins at line 1 and the final span ends at the final physical source line, assigning intervening blank lines exactly once.

### Semantic Queue Schema

| csv_column | meaning |
| --- | --- |
| `task_order` | Deterministic global row order across the frozen corpus |
| `unit_id` | Stable identifier such as `REF-001-SEC-002-BLOCK-004` |
| `agent_id` | Preassigned whole-file owner |
| `agent_file_order` | Order in which that agent processes owned files |
| `reference_file_path` | Working file to read and eventually rewrite |
| `section_order` | Source-order section number inside the file |
| `section_heading_line` | Frozen source line where the governing heading begins |
| `section_heading_level` | Governing Markdown heading depth |
| `section_heading` | Exact governing heading text |
| `block_order` | Semantic block position inside the section |
| `block_type` | Parser-derived atomic content type |
| `block_anchor` | Exact first nonblank source line, whitespace-normalized and capped at 160 characters |
| `start_line` | First frozen source line in the non-overlapping block |
| `end_line` | Last frozen source line in the non-overlapping block |
| `line_count` | Inclusive block size: `end_line - start_line + 1` |
| `source_span_sha256` | SHA-256 of the LF-normalized frozen source span |
| `task_status` | `pending`, `in_progress`, `reviewed`, `section_complete`, `complete`, or `blocked` |
| `task_instruction` | Repeated semantic-block evolution instruction |
| `completion_notes` | Concise decision, uncertainty, movement, or blocker record |

### Ten Section Questions

Before changing any semantic block in a header-defined section, the owning LLM SHALL explicitly pose and answer all ten questions about the complete current section. The answers form a verbose working packet that drives the rewrite. The final reference should absorb the conclusions naturally; it should not become a pasted questionnaire unless question-and-answer form is genuinely useful to the reader.

1. What decision does this reference help make?
2. What is the recommended default, and why?
3. When does the default work well?
4. When does it fail or become the wrong choice?
5. Which alternatives and tradeoffs matter?
6. Which gotchas and failure modes matter most?
7. What do good, bad, and borderline examples look like?
8. How can the important claims be verified?
9. What is known confidently, and what remains judgment or uncertainty?
10. What deeper deductions, second-order consequences, or additional insights follow, and how should they change the guidance?

### Mandatory Question Packet

Every answer to every question SHALL contain these six elements:

1. `current_section_observation`: what the section presently says, omits, or assumes.
2. `supporting_reason`: why the current or proposed guidance may be correct.
3. `counterargument_or_limit`: why it may be wrong, incomplete, misleading, or context-dependent.
4. `assumptions_and_boundaries`: the conditions under which the conclusion holds or fails.
5. `revision_decision`: what to keep, rewrite, expand, move, or remove.
6. `additional_insight_to_add`: the concrete deduction, example, edge case, operational detail, or connection that will deepen the rewritten section.

The packet SHALL be completed before editing begins. It may live in the agent's resumable working notes rather than the final reference, but `completion_notes` SHALL record that the packet was completed and summarize the resulting revision decisions.

Section numbers, headings, question numbers, field names, and stock wrapper phrases SHALL NOT make otherwise repeated answers count as distinct. After those context labels are removed and whitespace is normalized, every one of a file's 1,560 field values SHALL remain textually unique. When one boundary genuinely applies to several questions or sections, each answer SHALL explain the different local consequence instead of copying or cosmetically relabeling the same rationale.

### Required Verbosity Standard

"Very verbose" means comprehensive reasoning coverage, not repetitive length. The rewritten section SHALL preserve every distinct useful conclusion from the ten-question packet and explain causal reasoning, operating conditions, counterarguments, failure boundaries, concrete examples, verification methods, uncertainty, and second-order effects wherever they apply. It SHALL add genuinely useful insights beyond the seed text and SHALL reject padding, restatement, generic advice, or duplicated prose that does not improve a coding decision.

### Frequent Persistence Cadence

The owner SHALL write progress as soon as one atomic section is coherent. For every section, it SHALL save the complete ten-question packet first, save the reconciled reference section second, and run a focused sanity check before beginning the next section. It SHALL update its lane journal at least every three completed sections and at every Red, Green, and Refactor transition. During final rereads, it SHALL persist a review checkpoint at least every five sections. Holding several completed sections or an entire file only in model context is prohibited.

### REQ-CORPUS-001.0: Freeze Working Reference Corpus

**WHEN** Pass One begins
**THEN** the working corpus SHALL contain exactly the 99 Markdown files ending in `-20260710.md`
**AND** the semantic queue SHALL be derived before any working file is edited
**AND** the archived seed files under `agents-used-monthly-archive/idiomatic-references-202606/` SHALL remain unchanged
**SHALL** block execution when the working file count or dated suffix differs.

### REQ-UNIT-001.0: Derive Semantic Markdown Blocks

**WHEN** a working file is parsed
**THEN** the program SHALL apply the programmatic block rules in this specification
**AND** SHALL preserve parser-reported source order and heading context
**AND** SHALL split root lists and GFM tables at their semantic child boundaries
**AND** SHALL keep fenced code and nested list content structurally intact
**SHALL** reject nodes without source positions instead of guessing their line spans.

### REQ-COVERAGE-001.0: Cover Every Source Line

**WHEN** all blocks for one file are ordered by source position
**THEN** the first `start_line` SHALL equal 1
**AND** every later `start_line` SHALL equal the previous `end_line + 1`
**AND** the final `end_line` SHALL equal the file's physical line count
**AND** every `line_count` SHALL equal its inclusive span length
**SHALL** reject gaps, overlaps, duplicates, reversed spans, and uncovered blank or trailing lines.

### REQ-OWNERSHIP-001.0: Preserve Single File Ownership

**WHEN** a file appears in the semantic queue
**THEN** every row for that file SHALL have exactly one identical `agent_id`
**AND** only that agent SHALL edit the file during Pass One
**AND** ownership SHALL remain fixed until the file is complete
**SHALL** prohibit block-level or section-level splitting of one file across agents.

### REQ-ASSIGN-001.0: Preserve Predetermined Agent Ownership

**WHEN** the semantic queue replaces the heading queue
**THEN** every path SHALL retain its previous `agent_id` and `agent_file_order`
**AND** agent file counts and source-line loads SHALL remain unchanged
**AND** semantic task counts SHALL match the measured load table
**SHALL** reject generation when any path changes owner.

### REQ-PARALLEL-001.0: Run Four Owners Concurrently

**WHEN** Pass One starts
**THEN** all four preassigned agents SHALL be allowed to work in parallel
**AND** each agent SHALL process only one owned file at a time
**AND** each agent SHALL follow ascending `agent_file_order`
**SHALL** allow parallel edits only when active paths differ.

### REQ-CONTEXT-001.0: Read Complete Owned File

**WHEN** an agent starts its next file
**THEN** the agent SHALL read the complete frozen file before its first semantic task
**AND** SHALL load every queue row for that file in source order
**AND** SHALL understand the thesis, user journey, heading hierarchy, tables, lists, and cross-section relationships
**SHALL** block block-level work when complete file context or the complete row set is missing.

### REQ-QUESTION-001.0: Complete Ten Question Packet

**WHEN** an agent reaches the next header-defined section and before it changes any block in that section
**THEN** the agent SHALL pose all ten section questions in order
**AND** SHALL answer every question using all six mandatory packet elements
**AND** SHALL ground the answers in the complete current section and complete-file context
**AND** SHALL record the resulting revision decisions in its resumable working notes
**SHALL** prohibit section editing while any question or packet element is missing, generic, or unresolved without an uncertainty statement.

### REQ-HASH-001.0: Verify Frozen Block Identity

**WHEN** an agent loads an owned file
**THEN** every semantic span SHALL match its recorded `source_span_sha256` before the first edit
**AND** the agent SHALL treat source coordinates as frozen anchors
**SHALL** mark the entire file blocked when any hash differs rather than applying stale rows.

### REQ-REASON-001.0: Reason Through Every Block

**WHEN** an agent processes a semantic row
**THEN** it SHALL read the complete block and challenge every meaningful claim or recommendation
**AND** SHALL apply the conclusions from the section's completed ten-question packet
**AND** SHALL decide whether material should be kept, rewritten, expanded, moved, or removed
**AND** SHALL distinguish sound guidance from plausible-sounding filler
**SHALL** state material uncertainty instead of manufacturing confidence.

### REQ-DEPTH-001.0: Add Extensive Useful Insight

**WHEN** the ten-question packet reveals missing rationale, alternatives, boundaries, examples, verification, uncertainty, or second-order effects
**THEN** the rewritten section SHALL incorporate every distinct useful conclusion
**AND** SHALL explain recommendations deeply enough that a coding agent can decide when, why, and how to apply or reject them
**AND** SHALL add concrete insights beyond the seed section rather than merely polishing its wording
**SHALL** reject verbosity that consists only of repetition, padding, unsupported precision, or generic best practices.

### REQ-EDIT-001.0: Evolve Blocks In Order

**WHEN** block reasoning is complete
**THEN** the agent SHALL evolve that block in source order according to the completed section packet
**AND** SHALL record the decision before advancing
**AND** SHALL process semantic rows in source order without skipping
**AND** SHALL read table rows with their table header and list items with their section context
**SHALL** avoid web research and added citations by default because this pass prioritizes coding judgment and internal coherence.

### REQ-PERSIST-001.0: Persist Every Completed Section

**WHEN** one section's ten-question packet is complete
**THEN** the owner SHALL save that packet section immediately
**AND** SHALL save the matching reconciled reference section immediately afterward
**AND** SHALL run a focused sanity check before advancing
**AND** SHALL journal no later than the third completed section since the prior checkpoint
**SHALL** prohibit holding multiple completed sections only in transient model context.

### REQ-SECTION-001.0: Reconcile Every Complete Section

**WHEN** every semantic block governed by one heading is `reviewed`
**THEN** the owner SHALL reread the complete evolved section as one argument
**AND** SHALL verify that every revision decision and additional insight from all ten answers was incorporated or explicitly declined with a reason
**AND** SHALL reconcile table semantics, list flow, examples, defaults, exceptions, and transitions
**AND** SHALL remove contradictions and repetition introduced by block-level edits
**SHALL** move all rows in that section to `section_complete` only after this checkpoint passes.

### REQ-SPAN-001.0: Prevent Stale Line Drift

**WHEN** working-draft edits shift lines, headings, or block boundaries
**THEN** original unit IDs and source hashes SHALL remain traceability anchors
**AND** later tasks SHALL be interpreted against the frozen snapshot, not shifted live line numbers
**AND** moved, merged, or removed material SHALL be recorded in `completion_notes`
**SHALL** save each canonical section after its governed source blocks reach `section_complete`.

### REQ-STATE-001.0: Track Honest Block State

**WHEN** work begins or advances on a row
**THEN** `task_status` SHALL transition through `pending`, `in_progress`, `reviewed`, `section_complete`, and `complete`
**AND** `blocked` SHALL identify a concrete unresolved condition
**AND** `completion_notes` SHALL record the principal decision without restating the source
**SHALL** reserve `complete` until the rewritten whole file passes its final skeptical reread.

### REQ-FILE-001.0: Verify Complete Rewritten File

**WHEN** every semantic row in one file is `section_complete`
**THEN** the owner SHALL save and read the complete rewritten file from beginning to end
**AND** SHALL journal reread evidence at least every five sections
**AND** SHALL verify that the ten questions are answered consistently across the file
**AND** SHALL verify defaults, boundaries, counterexamples, gotchas, verification methods, and uncertainty for internal consistency
**SHALL** mark every row for the file `complete` only after this full-file gate passes.

### REQ-QUEUE-001.0: Preserve Deterministic Queue Data

**WHEN** the queue is generated twice from identical frozen source bytes and ownership data
**THEN** both CSV outputs SHALL be byte-identical
**AND** SHALL contain exactly 11,962 rows including the header
**AND** SHALL contain exactly 11,961 unique `unit_id` values
**AND** SHALL use the 19-column schema in this specification
**SHALL** initialize every task row as `pending` with empty `completion_notes`.

### REQ-PASS-001.0: Complete Specialist Evolution Pass

**WHEN** Pass One completion is claimed
**THEN** all 11,961 semantic rows SHALL be `complete`
**AND** all 99 files SHALL have one owner, all section checkpoints, and one final full-file reread
**AND** every working file SHALL remain present under its original dated path
**SHALL** reject completion when any row is pending, active, merely reviewed, section-only complete, or blocked.

### REQ-MEGA-001.0: Defer Combined Reference Pass

**WHEN** any Pass One row is not `complete`
**THEN** no mega-reference synthesis SHALL begin
**AND** no final mega grouping SHALL be invented from incomplete specialist files
**SHALL** create a separately measured semantic queue for `mega-idiomatic-references-202607/` only after all 99 evolved files are available.

### Failure Handling

| failure_condition | required_response |
| --- | --- |
| Markdown parser cannot provide a source position | Stop generation; do not guess a span |
| Source hash mismatch | Mark every row for that file `blocked`; do not edit until deliberately refreshed |
| Missing, duplicated, or overlapping block | Stop that file; rebuild and reverify complete line coverage |
| Multiple owners for one path | Stop both agents; restore the predetermined owner |
| Agent interruption mid-file | Preserve private draft and last reviewed `unit_id`; the same owner resumes |
| Heading renamed or block moved | Retain frozen IDs; explain the merge, move, or removal in `completion_notes` |
| Table rows become inconsistent | Resolve against the header and complete table during section reconciliation |
| Block advice conflicts elsewhere | Resolve during section and final file rereads before completion |
| Ten questions expose weak evidence | Rewrite as bounded judgment or explicit uncertainty; do not fabricate support |
| Worker cannot finish an owned file | Mark its rows `blocked`; coordinator may reassign the entire file only |

## Test Matrix

| req_id | test_id | type | assertion | target |
| --- | --- | --- | --- | --- |
| `REQ-CORPUS-001.0` | `TEST-CORPUS-COUNT-001` | inventory | exactly 99 working files use the `-20260710.md` suffix | corpus scope |
| `REQ-UNIT-001.0` | `TEST-PARSER-BLOCKS-001` | unit | fixture produces exact heading, paragraph, list-item, table-row, code, and blockquote spans | parser behavior |
| `REQ-UNIT-001.0` | `TEST-PARSER-FENCE-002` | negative | heading-like code-fence content never becomes a heading | code integrity |
| `REQ-UNIT-001.0` | `TEST-PARSER-NESTED-003` | unit | nested list content stays with its direct parent item | list integrity |
| `REQ-COVERAGE-001.0` | `TEST-SPAN-COVERAGE-001` | property | ordered blocks cover lines 1 through EOF exactly once per file | complete coverage |
| `REQ-OWNERSHIP-001.0` | `TEST-FILE-OWNER-001` | invariant | every distinct path maps to one and only one agent | edit isolation |
| `REQ-ASSIGN-001.0` | `TEST-OWNER-PRESERVE-001` | regression | all 99 path owners and file orders match the prior queue | assignment stability |
| `REQ-PARALLEL-001.0` | `TEST-WRITE-BOUNDARY-001` | concurrency | simultaneous workers have disjoint active paths | collision prevention |
| `REQ-CONTEXT-001.0` | `TEST-CONTEXT-READ-001` | audit | first task records a complete-file read and complete row set | context completeness |
| `REQ-QUESTION-001.0` | `TEST-QUESTION-PACKET-001` | editorial audit | every section has ten answers and every answer contains all six packet elements before editing | question completeness |
| `REQ-QUESTION-001.0` | `TEST-PACKET-NORMALIZED-002` | regression | all 1,560 packet fields remain unique after section and question context labels are removed | substantive packet depth |
| `REQ-HASH-001.0` | `TEST-SPAN-HASH-001` | integrity | every recomputed frozen block hash equals its CSV hash | stale queue detection |
| `REQ-REASON-001.0` | `TEST-BLOCK-DECISION-001` | editorial audit | each reviewed row records a keep, rewrite, expand, move, or remove decision | reasoning coverage |
| `REQ-DEPTH-001.0` | `TEST-SECTION-DEPTH-001` | acceptance | rewritten section incorporates every distinct packet insight without filler or unsupported claims | useful verbosity |
| `REQ-EDIT-001.0` | `TEST-BLOCK-ORDER-001` | sequence | one owner processes all blocks in source order without skips | execution order |
| `REQ-PERSIST-001.0` | `TEST-ATOMIC-SAVE-001` | audit | every packet section save precedes its reference section save and no journal gap exceeds three completed sections | durable progress |
| `REQ-SECTION-001.0` | `TEST-SECTION-REVIEW-001` | acceptance | a section advances only after every child block and one reconciliation reread | section coherence |
| `REQ-SPAN-001.0` | `TEST-SNAPSHOT-ANCHOR-001` | traceability | line-changing edits retain source IDs and movement notes | stable identity |
| `REQ-STATE-001.0` | `TEST-STATUS-STATE-001` | state transition | status values and transitions follow the allowed lifecycle | honest progress |
| `REQ-FILE-001.0` | `TEST-FILE-REREAD-001` | acceptance | file rows become complete only after final full-file reread | file coherence |
| `REQ-QUEUE-001.0` | `TEST-QUEUE-DETERMINISM-001` | reproducibility | identical inputs generate byte-identical 11,962-row CSV output | queue reproducibility |
| `REQ-PASS-001.0` | `TEST-PASS-COMPLETE-001` | integration | 11,961 complete rows resolve to 99 complete files and four owners | Pass One completion |
| `REQ-MEGA-001.0` | `TEST-MEGA-BLOCK-001` | negative | any incomplete specialist row prevents Pass Two start | phase boundary |

## TDD Plan

### STUB: Define Parser Behaviors

1. Create fixtures containing headings, multiline paragraphs, flat and nested lists, GFM tables, fenced code, blockquotes, blank lines, and preamble content.
2. Specify exact block types, source spans, section context, and full line coverage.
3. Define ownership-regression and deterministic-output assertions before replacing the queue.
4. Define section-packet checks for ten questions, six answer elements, revision decisions, and insight incorporation.

### RED: Prove Missing Behavior Fails

1. Run the semantic parser tests before implementation.
2. Confirm failure occurs because the semantic-block indexer is absent.
3. Confirm completion gates fail while all generated rows remain `pending`.
4. Confirm section editing and completion fail when any question, answer element, or planned insight is absent.

### GREEN: Generate Semantic Tasks

1. Parse every working file with CommonMark plus GFM syntax support.
2. Generate semantic blocks using the programmatic rules.
3. Preserve the previous whole-file owner map exactly.
4. Materialize all 11,961 rows through the CSV authoring tool.
5. Run the parser fixtures and corpus-level structural checks.
6. Require a complete ten-question packet before each section's first edit.

### REFACTOR: Reconcile Evolved Content

1. During execution, remove repetition created by atomic block improvements.
2. Reconcile tables, lists, defaults, exceptions, examples, metrics, and terminology at every section checkpoint.
3. Reconcile the complete file after all section checkpoints pass.
4. Preserve source-unit traceability when blocks move, merge, or disappear.

### VERIFY: Prove Pass Completion

1. Run parser, coverage, ownership, hash, state, and determinism checks.
2. Confirm every file retains its predetermined owner.
3. Confirm all section checkpoints and 99 final file rereads are recorded.
4. Confirm all 11,961 rows are `complete` and none are blocked.
5. Confirm the archived corpus is unchanged.
6. Only then unlock the separately specified mega-reference pass.

## Quality Gates

### Queue Initialization Gate

- [ ] Exactly 99 working files are indexed.
- [ ] Exactly 20,802 physical source lines are covered.
- [ ] Exactly 11,961 unique semantic blocks exist.
- [ ] Every source line appears in exactly one block.
- [ ] The six measured block-type totals match this specification.
- [ ] Every file retains exactly one predetermined owner.
- [ ] The four agent load totals match the measured table.
- [ ] All parser fixtures pass.
- [ ] Every initial status is `pending` and every completion note is empty.

### Per Block Review Gate

- [ ] The complete frozen semantic span was read.
- [ ] The governing section and relevant table or list context were considered.
- [ ] The section's ten-question packet was completed before this block changed.
- [ ] Meaningful claims received for-and-against reasoning.
- [ ] Relevant conclusions from all ten answers were applied.
- [ ] A keep, rewrite, expand, move, or remove decision was recorded.
- [ ] Weak certainty was bounded or removed.
- [ ] Cross-block movement was noted.
- [ ] The next block was not started out of order.

### Per Section Reconciliation Gate

- [ ] Every governed block reached `reviewed`.
- [ ] All ten questions were explicitly posed and answered before section editing.
- [ ] Every answer contains all six mandatory packet elements.
- [ ] No answer reuses normalized core content from another field by changing only labels or wrapper prose.
- [ ] Every revision decision and additional insight was incorporated or explicitly declined with a reason.
- [ ] The evolved section was reread as one argument.
- [ ] Table rows agree with their headers and one another.
- [ ] List items form a coherent progression.
- [ ] Defaults, exceptions, examples, and gotchas do not conflict.
- [ ] The section is extensively detailed without padding, repetition, or generic filler.
- [ ] Repetition created by block edits was removed.
- [ ] All governed rows moved to `section_complete` only after reconciliation.

### Per File Completion Gate

- [ ] The owner read the complete seed file before editing.
- [ ] Every source block passed its initial hash check.
- [ ] Every section passed its reconciliation gate.
- [ ] The canonical working file was saved only after section reconciliation finished.
- [ ] The complete rewritten file was reread skeptically.
- [ ] The ten questions are answered consistently at file level.
- [ ] The packet contains 1,560 exact and 1,560 normalized-unique populated field values.
- [ ] All file rows moved to `complete` only after the final reread.

### Pass One Completion Gate

- [ ] All 11,961 semantic rows are `complete`.
- [ ] All 99 working files passed their per-file gate.
- [ ] No row is pending, active, merely reviewed, section-only complete, or blocked.
- [ ] No file was edited by more than one agent.
- [ ] No specialist file was lost, renamed, or skipped.
- [ ] The archived source corpus remains unchanged.
- [ ] Pass Two remained blocked until this gate passed.

### Pre Commit Quality Gate

- [ ] Every `REQ-*` ID has at least one `TEST-*` row.
- [ ] Parser fixtures and queue integrity checks pass.
- [ ] No `TODO`, `STUB`, or `FIXME` substitutes for completed reasoning.
- [ ] No numerical claim lacks a verification method or uncertainty label.
- [ ] `git diff --check` reports no whitespace errors.
- [ ] Nothing is staged, committed, or pushed without explicit user permission.

## Open Questions

No question blocks Pass One.

The exact mega-reference families, count, block structure, and agent allocation remain intentionally undecided. They SHALL be derived from the 99 evolved specialist files after Pass One so the combined references inherit the improved reasoning rather than the current documents' weaknesses.
