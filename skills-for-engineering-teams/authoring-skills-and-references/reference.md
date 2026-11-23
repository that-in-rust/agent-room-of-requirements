# Authoring Skills and References: Reference

Deeper material for [SKILL.md](SKILL.md). The rules needed to do the work are on that page; this file holds the full catalogue, long tables, worked examples, operating guidance and evidence limits.

**Contents**

- Idiomatic Thesis Synthesis Statement
- Pattern Scoreboard Ranking Table
- Agent Usage Decision Guide
- Decision Tradeoff Guide
- Theme Specific Artifact
- Worked Example Set
- User Journey Scenario
- Anti Pattern Registry Table
- Verification Gate Command Set
- Failure Mode Table
- Workload Model
- Reliability Target
- Retry Backpressure Guidance
- Observability Checklist
- Performance Verification Method
- Scale Boundary Statement
- Outcome Metrics and Feedback Loops
- Completeness Checklist
- Adjacent Reference Routing
- Source Evidence Mapping Table
- Evidence Boundary Notes
- Future Refresh Search Queries

## Idiomatic Thesis Synthesis Statement

A skill is an onboarding guide written for another model instance. Its runtime is that instance's judgment, so it has to be treated like production code: it needs a failing case before it is written, a check that it changes behaviour, and maintenance when the consuming model changes.

Five ideas carry most of the weight.

1. **Loading comes first.** A skill that does not load cannot help. The description is the only text seen before the load decision, so trigger quality outranks body quality.
2. **Context is shared.** Every loaded token competes with the conversation. Keep only what is useful and not obvious to a capable model. The threshold moves as models improve, so the content doctrine is implicitly versioned.
3. **Quality is a measured difference.** Author satisfaction is not evidence. Evidence is a run the author did not steer, graded by someone who did not write the skill, compared with a baseline.
4. **Distribution is a conversation wrapped around a file copy.** Scripts own fetching and placing; the agent owns intent, choices, consent and reporting. Be permissive at transport boundaries and conservative at state boundaries.
5. **At scale, judgment and bookkeeping are separated.** Agents write prose section by section. Deterministic tools inventory, hash, verify and synchronise status, and never write prose. One owner per file, a queue, save points and verifiers make the work resumable and auditable.

Two creator traditions exist and are not interchangeable. One is a quantitative harness (baselines, assertions, benchmark deltas, held-out trigger scores). The other is principles-first forward-testing (uncontaminated subagent runs on realistic tasks). Send measurement questions to the first and authoring discipline to the second. A third tradition, pressure-testing, applies test-driven development to rule-bearing skills. They answer different questions; choose by the question, do not blend their procedures.

## Pattern Scoreboard Ranking Table

The order is editorial, by cost of failure. No source measured these ranks. The source references carried numeric scores for three process patterns (95, 91, 88); those were stated to have no empirical basis and are kept here only as an order.

### Authoring patterns

| Rank | Pattern | What it is | Fails when absent |
| --- | --- | --- | --- |
| 1 | Trigger description discipline | Third person, concrete phrases, symptoms, files, tools; no workflow summary | Skill never loads, or loads and the body is skipped |
| 2 | Progressive disclosure | Core in body, detail in references, scripts executed not read | Every load pays for everything |
| 3 | Beneficial and non-obvious filter | Keep schemas, local policy, exact commands, reasons | Body fills with tutorials |
| 4 | Degrees of freedom | Prose, parameterised template, or exact command by fragility | Fragile steps improvised; flexible steps strangled |
| 5 | Imperative style, one term per concept | Verb-first instructions | Longer, vaguer text |
| 6 | One default plus one escape hatch | A single recommended tool with a named exception | Agent must choose among five options |
| 7 | Study working siblings | Copy the shape of skills that already work | Reinvented structure |

### Evaluation patterns

| Rank | Pattern | What it is |
| --- | --- | --- |
| 1 | Blind baseline comparison | Same prompt with and without the skill; the judge does not know which is which. The only direct causal test |
| 2 | Evidence-cited grading | Every pass or fail quotes the output that justifies it |
| 3 | Discriminating assertions | Assertions the baseline can fail |
| 4 | Held-out trigger optimisation | Tune the description on 60 percent of queries, select on the other 40 |
| 5 | Baseline before writing | Observe the failure before writing the rule |
| 6 | Three or more combined pressures | Agents resist one pressure and break under several |
| 7 | Verbatim rationalisation capture | Quote the excuse; a paraphrase loses the loophole |

### Distribution patterns

| Rank | Pattern | What it is |
| --- | --- | --- |
| 1 | Fetch ladder | Direct download, then git over HTTPS, then git over SSH |
| 2 | Placement safety | Abort when the destination exists |
| 3 | Lifecycle notice | Tell the user to restart so the skill is picked up |

### Scale-production patterns

| Rank | Pattern | What it is |
| --- | --- | --- |
| 1 | Source map first | Inventory and assign every source before drafting |
| 2 | Evidence boundary split | Label each claim local fact, external fact or inference |
| 3 | Verification gate coupling | No status change without a passing verifier |
| 4 | One permanent owner per file | Disjoint lanes; the coordinator owns only the queue |
| 5 | Packet before prose | Ten answers with six fields each saved before the section is rewritten |
| 6 | Normalised uniqueness | Strip prefixes, collapse whitespace, fold case, then compare |
| 7 | Resume at the saved boundary | Same owner continues; valid work is kept |

### A published rubric makes a ranking auditable

The tables above are ordered by editorial judgment. When a reference ranks many patterns, publish the scoring rubric with the ranking, so a reader can see why an entry sits where it does and can dispute one axis instead of the whole order.

Worked example: this library's Rust reliability reference scores each of its sixty patterns out of 100 and prints the rubric beside the table.

| Axis | Points |
| --- | --- |
| Bug-prevention power | 35 |
| Misuse resistance | 20 |
| Diagnosability | 15 |
| Concurrency or async safety | 15 |
| Breadth and repeatability | 15 |

Only patterns scoring above 80 are kept. Newtypes with parse-don't-validate (entry RC2-02) score 98, and no blocking and no locks across `.await` (RC2-20) scores 97; both reach the maximum on the bug-prevention axis. An 82-point entry such as `rustfmt` survives on breadth. The scores therefore say why each pattern matters, not only where it ranks.

How to use a scored table:

- Classify the task first. Scores order patterns inside the sections the task touches; they do not replace that classification.
- Adopt in score order within those sections. Scores order the defaults and the task overrides them: taking an 83-point pattern first is correct when the task is exactly its use case.
- Treat anything the author listed as deliberately not elevated (powerful techniques that are easy to copy without understanding) as needing explicit justification. That list is part of the ranking.
- Quote a score as scored local judgment. It is one author's rubric applied to that author's sources. It is not a measurement and not community consensus, and its stability between raters cannot be tested from one author's file.
- A complementary ranking is a team's own defect history. The rubric predicts where bugs come from; incident history reports where they came from.

Good: starting an async service review at the three highest-scored entries of the async section. Bad: leading with an advanced type-system technique on a plain CRUD crate. To check use, see whether the order in which patterns were adopted follows the scores within the touched sections, or whether the deviation is written down.

## Agent Usage Decision Guide

### Which artifact

| Situation | Artifact |
| --- | --- |
| Reusable technique across projects | Skill |
| Convention for one repository | Repository instruction file |
| Constraint a script can check | Validator or hook, not prose |
| One-off solution | Nothing |
| Facts looked up during work | Reference file inside a skill |
| Code rewritten every time | Script inside a skill |
| File copied into output | Asset inside a skill |

### Which shape

| Shape | Contents | Use when |
| --- | --- | --- |
| Minimal | `SKILL.md` only | Simple knowledge, everything fits |
| Standard | `SKILL.md`, references, examples | Most skills with detailed documentation |
| Complete | Adds scripts | Complex domains with validation utilities |

Body structure options: workflow-based for sequential processes; task-based for collections of operations; reference or guidelines for standards; capabilities-based for integrated features. Mix them when needed.

### Which test

| If the skill | Then |
| --- | --- |
| States a rule the agent has an incentive to break | Baseline, pressure scenarios, loophole closing |
| Teaches steps | Application, variation, missing-information scenarios |
| Teaches a way of thinking | Recognition, application, counter-examples |
| Holds facts | Retrieval, application, gap checks |
| Produces objectively checkable output | With and without runs, assertions, benchmark |
| Produces subjective output | Human review; record that assertions were waived |
| Is of uncertain type | Pilot one pressure scenario and let a reviewer classify |

### Who may know what during an evaluation

The quantitative harness defines five roles. They partition knowledge. This is an information architecture, not a way of splitting the work: each role lacks exactly the knowledge that would bias it.

| Role | Does | May know | Must not |
| --- | --- | --- | --- |
| Orchestrating creator | Runs the loop, launches runs, edits the skill | Everything | Keep the judgment to itself. It routes judgment outward: to the human through the review viewer and to the grader through the evidence rule |
| Executor subagent | Runs one prompt, with or without the skill | The task, the input files, the skill path when there is one | Know that it is being tested |
| Grader | Scores each assertion | The outputs and the assertions | Accept a claim without evidence. Every pass or fail cites the output that justifies it |
| Blind comparator | Picks the better of two outputs | Unlabelled outputs and the evaluation prompt, nothing else | Know which skill or version produced which output |
| Analyzer | Unblinds the comparison and explains why the winner won | Everything, once the comparator has decided | Take part in the blind judgment |

- The orchestrator's neutrality is procedural, not epistemic. It knows what it hoped to see, so it is not blinded; its bias is managed by where the judgment goes.
- The Codex form is the same partition with two roles: the author and an uncontaminated forward-tester. The principle scales down.
- Inline grading by the orchestrator, where subagents are unavailable, is an allowed degraded mode. The evidence rule still binds.
- Zero roles, the author alone, is the failure state both creator systems are built to prevent. Collapsing two roles into one collapses the boundary between them.
- Before the runs, read each role prompt for boundary violations. An executor prompt that says "this tests the new version of the skill" is one.
- How strictly live orchestrators keep these boundaries is not recorded in any source.

**The two creator systems, concern by concern.** Use this map to answer a cross-platform question in the right vocabulary. Prescribing benchmark JSON to a Codex author, or forward-test purity rules to a harness user, is the error it prevents.

| Evaluation concern | Quantitative harness (Claude skill-creator) | Forward-testing (Codex skill-creator) |
| --- | --- | --- |
| Causal isolation | Runs with the skill against baseline runs without it | Forward-tests on realistic tasks |
| Judge independence | Blind comparison of unlabelled outputs | Contamination controls on what the tester is told |
| Execution independence | Executor subagents that do not know they are being tested | An uncontaminated forward-tester, separate from the author |
| Assertion quality | Graded assertions; every pass or fail cites the output that justifies it | No assertions; the author observes where the agent struggles |
| Overfit control | Trigger description tuned on 60 percent of queries and selected on the held-out 40 | Not stated in the sources |
| Presentation integrity | Judgment routed to the human through the review viewer | Not stated in the sources |
| Gaps | No counterpart to the degrees-of-freedom ladder | No counterpart to trigger-description optimisation |

- Correspondence is not equivalence. The harness gives quantified differences between assertion pass rates. Forward-testing gives a qualitative observation of where the agent struggles. They measure different things.
- Each empty cell in the gaps row is something one system can import from the other.
- The sources name the six concerns but give the mechanisms only for causal isolation and judge independence. The other four rows are filled in from the role and method descriptions elsewhere in this reference; a cell that those do not cover says so.

### When to open this guidance

Before creating a skill, before editing its rules, and before deploying it. A cosmetic typo fix is a recorded exemption. "Just adding a section" is not exempt.

### Where the user is

| Arrival | Start at |
| --- | --- |
| Idea only | Interview and concrete examples |
| Draft in hand | Evaluation loop |
| Migrating from a generic creator to a plugin | The delta table below; unlearn the init and package scripts |
| Wants no formal evaluation | Human review only, at the user's choice |
| Not a programmer | Same loop; explain "assertion" and "JSON" before using them. "Evaluation" and "benchmark" are usually fine |

## Decision Tradeoff Guide

### Conflicts between sources

The compact table is in `SKILL.md`. Additional detail on the ones that need it:

**Description contents.** The Anthropic guide and both creator skills want what the skill does and when to use it. The superpowers guide wants only when, because it observed an agent act on a workflow summary and skip the body. These agree on the important point: never describe the procedure. A short capability clause is not a procedure. Use the clause when the runtime or the library convention asks for it.

**Pushy descriptions.** The Claude creator reports a tendency to under-trigger and recommends a slightly "pushy" closing clause: after the capability sentence, tell the agent to use the skill whenever the user mentions any of several named neighbouring topics, even when the user never says the skill's key word. Its example is a dashboard skill whose description also names data visualisation and internal metrics as triggers. This is model-relative advice. Apply it where under-triggering is observed and check false positives with near-miss queries.

**Tone.** "Explain why" and "authority language" are both right for different skill types.

| What the skill is for | Principles that fit | Principles to keep out |
| --- | --- | --- |
| Enforcing a discipline | Authority together with commitment and social proof | Liking; reciprocity |
| Guiding a technique | Authority in moderation; unity | Authority at full strength |
| Working with the user as a collaborator | Unity; commitment | Authority; liking |
| Holding facts to look up | None. Be clear | Every persuasion principle |

Authority is imperative wording and "no exceptions". Commitment is announcing skill use, forced choices and tracked checklists. Scarcity is "before proceeding" and "immediately after". Social proof is "every time" and "X without Y fails". Unity is "we are colleagues". The ethical test: would the technique serve the user's real interests if they fully understood it? Do not create false urgency or guilt.

**Testing exemptions.** One superpowers file says no skill or edit without a failing test and lists "it's just a reference" as an excuse. Its companion file says not to pressure-test pure reference skills. Read together: what is waived for a reference skill is the pressure campaign, not testing. Retrieval and application checks remain.

**Subagent framing.** Codex forward-testing hides the fact of testing and gives a plain task. Superpowers scenarios announce "this is a real scenario" and name the skill. The first measures whether the skill generalises on real work. The second measures whether a rule survives temptation.

### Other tradeoffs

| Choice | Lean one way when | Lean the other when |
| --- | --- | --- |
| Rigor of evaluation | Output is objective, a comparative claim will be made | User declines; output is subjective |
| Freedom per instruction | Many valid approaches | Fragile operation, exact sequence |
| One skill or two | Shared trigger surface | Domain does not fit the budget; each half then needs its own description. When the domains are entangled, two skills may share one reference file by relative path; each skill is still discovered and triggered separately |
| Bundle a script | Three test runs each wrote the same helper | Logic varies by case |
| Install method `auto` | Normal use | Pin `download` or `git` to diagnose a failure |
| Install `--dest` staging | Inspect before use | Note that staged skills are not shown as installed |
| Implicit invocation | Benign skill, false positives sampled | Destructive or sensitive skill: explicit only |
| Reread group size | Five sections | Three when sections are long or early groups show drift |

Failure poles to avoid: forced rigor that alienates the user; low freedom that strangles a flexible task; high freedom that lets a fragile task wobble; chasing each complaint until the skill overfits three known examples.

## Theme Specific Artifact

### Skill body template

```markdown
---
name: skill-name
description: <capability clause>. Use when <phrases, files, tools, symptoms>. Not for <nearest wrong uses>.
---

# Skill Name

## Overview
Core principle in one or two sentences.

## When to use
Signals that this skill applies, and the nearby cases it should stay out of.

## Core pattern
A before-and-after pair, or the numbered workflow.

## Quick reference
Table for scanning common operations.

## Implementation
Inline code for simple cases; link to a file for heavy reference or tools.

## Common mistakes
What goes wrong and the fix.

## Additional resources
- `references/patterns.md` - read when <condition>
- `scripts/validate.sh` - run to <purpose>
```

### Pressure campaign record

Keep one per discipline skill, written as the campaign happens. A reconstruction afterwards is not equivalent.

```markdown
Skill: <name>   Model: <id>   Date: <date>
Scenario: <text>   Pressures: time, sunk cost, exhaustion
Baseline choice: C   Verbatim excuses: "Tests after achieve same goals"
Iteration 1 change: added "Why order matters"   Result: C   New excuse: "Spirit not letter"
Iteration 2 change: added "Violating the letter is violating the spirit"   Result: A, cited the principle
Meta-test answer: "The skill was clear, I should follow it"
Verdict: holds for this scenario
```

### Evaluation files (quantitative harness)

Field names below are the harness's own and must be used exactly. The values are illustrations written for a release-notes skill.

Test cases, `evals/evals.json`. Top level: `skill_name` and an `evals` array. Each entry: `id`, `prompt`, `expected_output` (a description, not a literal match) and `files`. Write only prompts at first; an `assertions` field is added to each entry once the runs are under way.

```json
{"skill_name": "release-notes",
 "evals": [{"id": 1,
            "prompt": "draft the notes for v2.4.0, we tagged it friday. CHANGES.md exists but half the PRs never got an entry",
            "expected_output": "One Markdown section per change type; every change merged since v2.3.0 listed once",
            "files": ["fixtures/CHANGES.md"]}]}
```

Per-case metadata, `eval_metadata.json`, one per test-case directory. Fields: `eval_id`, `eval_name`, `prompt`, `assertions`. Give the case a name that says what it tests and use the same name for its directory. Create the file again for every new or changed prompt; do not assume it carries over from the previous iteration.

```json
{"eval_id": 1, "eval_name": "tag-range-with-missing-changelog-entries",
 "prompt": "draft the notes for v2.4.0, we tagged it friday. CHANGES.md exists but half the PRs never got an entry",
 "assertions": []}
```

Timing, `timing.json`, one per run directory. Fields: `total_tokens` and `duration_ms`, both copied from the task-completion notification, and `total_duration_seconds`, which is `duration_ms` divided by 1000. The notification is the only place these figures appear.

Grading files use an expectations array whose entries have exactly `text`, `passed` and `evidence`. Feedback files have `reviews` (each with `run_id`, `feedback`, `timestamp`) and `status`. Trigger sets are `[{"query": "...", "should_trigger": true}]`.

Workspace layout: `<skill-name>-workspace/iteration-N/<eval-name>/{with_skill,without_skill|old_skill}/outputs/`, a sibling of the skill folder, created as runs happen and not in advance.

Prompt for the with-skill executor. It reads as an ordinary task and says nothing about testing:

```
Carry out the task below as you would for a user.
Skill to use: <path-to-skill>
Task: <the eval prompt, unchanged>
Inputs: <paths of the eval files, or "none">
Write results under: <workspace>/iteration-<N>/<eval-name>/with_skill/outputs/
Keep: <the deliverables the user will judge, for example the notes file>
```

The baseline executor gets the same prompt without the skill line and writes to `without_skill/outputs/` (new skill), or gets the snapshot's path as its skill and writes to `old_skill/outputs/` (existing skill).

A simpler case format from the Anthropic guide, for a home-made runner. Fields: `skills` (which to load), `query`, `files`, and `expected_behavior` (a list of statements a grader checks). The guide notes that no built-in runner exists for this format.

```json
{"skills": ["release-notes"],
 "query": "Write release notes for everything merged since v2.3.0 into NOTES.md",
 "files": ["fixtures/git-log.txt"],
 "expected_behavior": ["Works out the commit range from the previous tag without asking",
                       "Lists each merged change once, under a change-type heading",
                       "Writes the result to NOTES.md as Markdown"]}
```

### `agents/openai.yaml` full form

| Field | Purpose | Constraint |
| --- | --- | --- |
| `interface.display_name` | Title a person sees in skill lists and chips | Quoted string |
| `interface.short_description` | Short blurb for scanning a list | 25 to 64 characters |
| `interface.icon_small` | Small icon | Path relative to the skill folder; keep icons under `./assets/` |
| `interface.icon_large` | Larger logo | Same as the small icon |
| `interface.brand_color` | Accent colour for interface elements such as badges | Hex value |
| `interface.default_prompt` | Starter prompt inserted when the skill is invoked | About one sentence; must name the skill as `$skill-name` |
| `dependencies.tools[].type` | Kind of dependency | Only `mcp` is supported |
| `dependencies.tools[].value` | Identifier of the tool or server | |
| `dependencies.tools[].description` | Explanation of the dependency for a person | |
| `dependencies.tools[].transport` | Connection type | Applies when the type is `mcp` |
| `dependencies.tools[].url` | Server address | Applies when the type is `mcp` |
| `policy.allow_implicit_invocation` | When false, the skill is not placed in the model's context by default and can still be called explicitly as `$skill-name` | Defaults to true |

Quote every string value and leave keys unquoted. Other product-specific configuration may sit beside this file in `agents/`.

An example that uses every field, so the shape is visible:

```yaml
interface:
  display_name: "Release Notes"
  short_description: "Draft release notes from merged changes"
  icon_small: "./assets/release-notes-small.svg"
  icon_large: "./assets/release-notes.png"
  brand_color: "#0F766E"
  default_prompt: "Use $release-notes to draft notes for the latest tag."

dependencies:
  tools:
    - type: "mcp"
      value: "issue-tracker"
      description: "Issue tracker server, used to resolve ticket titles"
      transport: "streamable_http"
      url: "https://mcp.example.com/issues/"

policy:
  allow_implicit_invocation: false
```

A real file carries only the fields in use. The two real instances in the Codex material carry `display_name`, `short_description` and two icon paths and nothing else. Icon formats are not prescribed: the bundled installer icons are a small SVG and a large PNG, and the vendor's own field example has it the other way round, so do not infer a required format for either.

Activation contract to fill in for each metadata change: skill identity; user goal; product; fields selected and omitted with reasons; rendered text; asset inventory; prompt; dependency owner and readiness; implicit policy and a misuse case; parse result; runtime observations; rollback. Never record a planned test as passed.

### Installer listing text

A header line names the repository and, for experimental sources, the tier. The entries are numbered, and each one already present locally carries an installed mark. The reply ends with the question that asks for a choice. With invented skill names:

```
Skills from openai/skills (curated):
1. changelog-writer
2. form-filler (already installed)
3. sheet-cleanup
Which ones would you like installed?
```

### Queue, packet and journal for a multi-file programme

Queue row, one per atomic unit, 19 columns in the source programme:

| Column | Meaning |
| --- | --- |
| `task_order` | Global order |
| `unit_id` | Stable identifier, for example `REF-001-SEC-002-BLOCK-004` |
| `agent_id` | The file's permanent owner |
| `agent_file_order` | Position of the file in the owner's lane |
| `reference_file_path` | File the unit belongs to |
| `section_order`, `section_heading_line`, `section_heading_level`, `section_heading` | Section context |
| `block_order`, `block_type` | Position and kind: heading, paragraph, list item, table header, table row, code block |
| `block_anchor` | First non-blank line, whitespace-normalised, capped at 160 characters |
| `start_line`, `end_line`, `line_count` | Source span |
| `source_span_sha256` | Hash of the span with line endings normalised to LF |
| `task_status` | `pending`, `in_progress`, `reviewed`, `section_complete`, `complete`, `blocked` |
| `task_instruction` | What to do with the unit |
| `completion_notes` | Principal decision, without restating the source |

Block rules: parse with a CommonMark plus GFM syntax tree that keeps source positions. A heading is a unit and sets section context. A root paragraph is a unit. A direct item of a root list is a unit; nested items stay with their parent. A table header with its delimiter row is one unit; each data row is one unit. A fenced or indented code block is indivisible, diagrams included. Blockquotes, HTML, thematic breaks and definitions are atomic. Heading-like text inside a fence is never a heading. The first span starts at line 1, each span starts where the previous ended, the last ends at the final line, and blank lines are assigned exactly once. Chunking is by meaning, not by line count.

Measured by the queue generator in the source programme: 99 files, 20,802 physical lines, 2,574 headings (26 per file), 11,961 units; 113, 118 and 158 units per file at minimum, median and maximum; 1, 2 and 7 lines per unit. Lanes were balanced by source lines: 25 files and 3,018 units, 25 and 3,020, 25 and 3,017, 24 and 2,906.

Status lifecycle: `pending` to `in_progress` to `reviewed` (unit read and decided) to `section_complete` (section reconciled) to `complete` (whole file passed its reread and verifier). `blocked` names a concrete unresolved condition. Regenerating the queue from the same frozen bytes and ownership data must give a byte-identical file, and must never change a file's owner.

Packet (one per file): one block per section, each with the ten questions and, under each, the six fields. With 26 sections that is 260 answers and 1,560 field values per file.

```markdown
## Section 007: Decision Tradeoff Guide
### Question 04: When does it fail or become the wrong choice?
- **current_section_observation:** ...
- **supporting_reason:** ...
- **counterargument_or_limit:** ...
- **assumptions_and_boundaries:** ...
- **revision_decision:** keep | rewrite | expand | move | remove, with the reason
- **additional_insight_to_add:** ...
```

The bundled verifier expects exactly this shape: three-digit section numbers, two-digit question numbers followed by the exact question text, and single-line field values. The packet is working material. The finished reference absorbs its conclusions as normal prose; it is not a pasted questionnaire unless question-and-answer form helps the reader. When one boundary applies to several questions, each answer explains the different local consequence instead of repeating the boundary.

"Very verbose" in the source specification means complete reasoning coverage, not length: causal reasoning, operating conditions, counterarguments, failure boundaries, examples, verification, uncertainty and second-order effects. Padding, restatement and generic advice are rejected.

Journal entry: phase (red, green, refactor, verify), tests written with passing or failing state, implementation progress, current focus, next steps (never empty), context notes, metrics such as accepted files and completed and pending rows. Write one at least every three sections, at each phase change, after each verification failure, and at least every five sections during the final reread. Keep one journal per lane and one master journal.

Handoff document, written whenever work passes to another agent or person. "Start from evidence, not memory."

- Latest save point: branch, commit, summary, time, working-tree state.
- Current phase and the reason for it.
- Counts: files accepted and remaining, rows complete and pending, packets on disk versus accepted versus partial.
- The partial item with its durable progress, for example "Sections 001 to 009 complete; next is section 010; do not regenerate 001 to 009".
- Core artifacts and the quality contract.
- Verification status, listing the expected failures with counts and stating that they reflect unfinished work, not corruption.
- State of each lane: accepted through which assignment, remaining files, immediate next steps.
- How to resume (commands), the per-file completion procedure, the journal update procedure.
- Constraints, the plan for the later combined pass, a rollback strategy, and a ready-to-use next prompt.

Reference file contract from the generation specification, in the order the requirements were added:

1. Inventory: parse the theme table; each row is one required file; fail when the count differs from the expected number. Deduplication rule for the table: every candidate path appears exactly once; repeated monthly copies and the current copy of one file stay visible as separate paths, and are folded into the same theme row when they serve the same agent use case.
2. One file per theme, named by its four-word label; reject extra, missing, duplicate or differently named files.
3. Local corpus: every source path listed for the theme appears in the file's source map with its role.
4. External evidence: primary documentation and maintainer sources where available; otherwise an explicit reason it was unavailable. Never invent support.
5. Minimum structure: source mapping, pattern scoring, thesis, anti-pattern registry, verification gates, agent usage guidance, refresh queries.
6. Four-word labels: every reusable label, table column, pattern family, risk category and gate name has exactly four meaningful words. Weak single-word labels such as `metrics`, `tracing`, `security`, `tests`, `sources`, `quality` are rejected.
7. Agent utility: the file must help an agent decide what to load, prefer, avoid and verify. Generic tutorials that do not change behaviour are rejected.
8. Progress journal with a non-empty next step at every entry.
9. Coverage manifest: theme, file path, local source count, external source count, verification status, journal link.
10. Each recommendation marked as local fact, external fact or inference, with uncertainty notes for conflicts, stale sources and missing primary documentation.
11. A product-strategy critique: one block per reference naming missing user-journey clarity, missing tradeoffs, missing coverage, missing source synthesis and concrete additions, including at least one theme-specific missing artifact (threat model, decision table, worked example, runbook, rubric or checklist). Generic praise and summary-only blocks fail.
12. Upgrade beyond an evidence index: a role-based opening scenario, the user's starting state, the decision being made, the trigger for opening the file, and adopt, adapt or avoid guidance with the cost of being wrong.
13. Local source hierarchy: classify each source as canonical, supporting, legacy, duplicate or conflicting; add a confidence warning when there is only one local source.
14. Completeness apparatus: one theme-specific artifact; one good, one bad and one borderline example; a completeness checklist; metrics, leading indicators and failure signals; routing to adjacent references.
15. A systems critique: one block per reference, at least 35 lines, naming missing scale limits, reliability guarantees, operational robustness, technical grounding, production-load risks and simplifications, with explicit scale model, reliability model, instrumentation, failure modes, backpressure, observability and latency-percentile markers.
16. Production-readiness apparatus: workload model, reliability target, failure-mode table, retry and backpressure guidance, observability checklist, performance verification method, and a statement of where the guidance stops applying.
17. Each critique pass tracked in its own journal with red and green entries for existence, coverage and format.

The ordered headings of this file are that contract applied to itself.

Open decisions the generation specification left to the programme owner: whether the decision-quality requirements block the existing corpus or only the next rewrite; how many external sources a theme needs before an unavailable-reason is acceptable; whether critique output is a separate review artifact or tracked rewrite items; whether production-readiness is applied everywhere at once or to the highest-risk themes first; and whether one universal service-level template or per-theme thresholds are used.

### Plugin delta table

| Generic creator | Plugin skill |
| --- | --- |
| `init_skill.py` | `mkdir -p plugin/skills/name/{references,examples,scripts}` |
| Validate and zip with a packaging script | None; ships with the plugin |
| Script validation | Eight-point checklist plus a reviewer agent |
| Generic testing | `cc --plugin-dir` trigger test |
| No `examples/` folder | `examples/` added |
| Anatomy, progressive disclosure, style, iteration loop | Unchanged |

The packaging script named by the ancestor creator is not bundled here.

## Worked Example Set

### 1. Descriptions: bad, good, borderline

Bad, with the fault:

```yaml
description: Use this skill for database work.              # vague; no phrases users say
description: Load when the user wants migration help.       # addressed to the loader, not third person
description: Gives migration advice.                        # no triggers at all
description: Helps with documents                           # matches everything and nothing
description: I can help you with flaky tests                # first person
description: Use when executing plans - dispatches subagent per task with code review between tasks   # summarises workflow (the observed case)
```

Good, one per convention:

```yaml
# Plugin convention: third person, quoted phrases, named tools
description: This skill should be used when the user asks to "write a migration", "add a column safely", "roll back a schema change", or mentions a migration tool (Alembic, Flyway, sqlx migrate).
# Capability clause, then triggers
description: Draft release notes from merged pull requests and tags. Use when the user mentions a changelog, release notes, "what shipped", or a version tag.
# Triggers only, written as the problem
description: Use when a plan holds several independent tasks that can be carried out in the current conversation
description: Use when a test passes alone and fails in the suite, or flips between pass and fail with no code change
```

Borderline: a keyword-stuffed list of twenty quoted phrases that no longer reads as a sentence. It may trigger more often and it will also trigger wrongly; score it with near-miss queries before keeping it.

Drill: write a description in the target convention with three trigger phrases and one concrete scenario, then check it reads as a sentence and contains no workflow.

### 2. Concise versus verbose body text

Concise:

````markdown
## Read a Parquet file
Use pyarrow:
```python
import pyarrow.parquet as pq
rows = pq.read_table("events.parquet").to_pylist()
```
````

Verbose: the same snippet after a paragraph that explains what a columnar file is and that several libraries can read one. The paragraph adds nothing a capable model lacks. A BigQuery table schema, by contrast, is exactly what the model cannot know.

The Anthropic guide makes the point with a PDF text-extraction section: a heading, one line naming the library and a three-line snippet, which it estimates at about 50 tokens, against a version of about 150 tokens that first explains the file format and surveys libraries. Both figures are the guide's estimates.

Compression moves that preserve meaning: put flag details behind `--help` instead of listing them; name another skill instead of repeating its content; shorten an example to the minimum that shows the pattern (one source example went from 42 to 20 words).

### 3. Degrees of freedom

- High (prose): "Review the change for correctness, unhandled edge cases, readability and fit with the project's conventions. Report findings by severity."
- Medium (parameterised template): "Start from this call and adjust the arguments: `build_report(rows, fmt="markdown", charts=True)`."
- Low (exact command): "Run `python scripts/rotate_keys.py --dry-run`, read the plan, then run it again without `--dry-run`. Do not add, remove or reorder flags."

A narrow bridge with cliffs needs guardrails; an open field needs only a direction.

### 4. Placement drill

Sort these for a BigQuery analysis skill:

| Fact | Goes in |
| --- | --- |
| "Always exclude test accounts" | Body (core rule) |
| Workflow: pick dataset, write query, validate | Body |
| Finance table schemas | `reference/finance.md` |
| Sales pipeline schemas | `reference/sales.md` |
| `grep -i "revenue" reference/finance.md` hint | Body (navigation) |
| Complete example query with comments | `examples/` |
| Query cost checker | `scripts/` |
| Report template | `assets/` |
| How the skill was developed | Nowhere |
| What SQL is | Nowhere |

Good: schemas in references plus a search hint in the body. Bad: the same workflow written in both the body and a reference. Borderline: a one-file skill with everything inline, which is fine while it is small. Source examples of lean plugin skills: one body of 1,651 words with three references, three examples and three scripts; one of 1,438 words. A reported bad case put 8,000 words in the body; the repair was a body of 1,800 words with references of 2,500 and 3,700 words.

Split patterns:

```
bigquery-skill/                 cloud-deploy/
├── SKILL.md                    ├── SKILL.md  (workflow + provider selection)
└── reference/                  └── references/
    ├── finance.md                  ├── aws.md
    ├── sales.md                    ├── gcp.md
    └── product.md                  └── azure.md
```

A third pattern keeps basic usage inline and links advanced features: "For tracked changes see REDLINING.md".

### 5. Pressure campaign on a test-first rule

Scenario ladder:

- Bad: a quiz. "You are about to implement a feature. What does the skill tell you to do?" The agent recites.
- Better: one pressure. Checkout is failing, every minute costs money, the manager wants a two-line patch shipped inside the deploy window. Agents often hold.
- Best: several pressures at once. Hours of sunk work that runs, end of the day, somewhere else to be, a review in the morning, and a forced A/B/C choice with real file paths and no way to defer. Ask for an honest answer.

Five properties of a good scenario: concrete options, real constraints, real file paths, a demand to act ("What do you do?"), and no option to defer or ask.

Typical baseline excuses in the source campaign: manual testing was already done; "tests after achieve the same goals"; deleting finished work is wasteful; this is pragmatism, not dogma. Record the agent's own words, not a summary like this one.

Closing one loophole takes four edits. The source closes "keep the old code as a reference while writing the tests" for a test-first rule. The same four edits for a verify-before-claiming-done rule and the excuse "the change is too small to need a run":

1. Explicit negation in the rule:

```markdown
About to say it is done without running the check? Do not say it. Run the check first.

**This covers:**
- one-line changes
- changes "only to comments or config"
- a run made before the last edit
- a run somebody else made
```

2. A row in the excuse-and-reality table:

```markdown
| Excuse | Reality |
| --- | --- |
| "Too small to need a run" | Small edits break builds too. The run is the evidence; the size of the diff is not. |
```

3. A red-flag entry:

```markdown
## Red flags: stop and run the check
- "It's a trivial change"
- "It passed earlier"
```

4. Symptoms in the description, describing the moment just before the violation:

```yaml
description: Use when about to report work as done, fixed or passing, when a change looks too small to test, or when relying on an earlier run.
```

Iteration trace from the source's test-first campaign: first run chose C with "tests after achieve the same goals"; a "why order matters" section was added and the agent still chose C with "spirit, not letter"; the principle "violating the letter is violating the spirit" was added and the agent chose A and cited it. The source reports six iterations, more than ten distinct excuses and full compliance at its final check for that skill. That result is the source's report and was not reproduced for this library.

Signs the skill holds: correct choice under maximum pressure, cites sections, acknowledges the temptation, and the meta-test answer is "the skill was clear". Signs it does not: new excuses, arguing the skill is wrong, hybrid approaches, asking permission while arguing for the violation.

Excuses authors use to skip testing, with answers:

| Excuse | Reality |
| --- | --- |
| "The skill is obviously clear" | Clear to the author is not clear to another agent |
| "It's just a reference" | References have gaps; test retrieval |
| "Testing is overkill" | Untested skills have issues; a short test costs less than a bad deployment |
| "I'll test if problems emerge" | Then users find the problems |
| "Too tedious" | Less tedious than debugging a bad skill in use |
| "I'm confident it's good" | Confidence is not evidence |
| "Academic review is enough" | Reading is not using |
| "No time to test" | Deploying untested costs more later |

### 6. Variant test for an instruction-file passage

Goal: find wording that makes agents check for skills under pressure. Four scenarios, each a forced A/B choice: time pressure plus confidence (production down, $5k a minute, check skills first or debug now); sunk cost plus working code (45 minutes spent, tests pass); authority plus speed ("just add validation and ship it"); familiarity plus efficiency (a routine refactor).

Five variants: no mention at all (the null baseline); a soft suggestion ("consider checking"); a directive with browse and search commands; an emphatic block with capital letters and "if a skill existed and you didn't use it, you failed"; a process-oriented numbered workflow with reasons.

Protocol: run the null baseline first and record the choice and exact excuses; run each variant on the same scenario; add pressure and note where compliance breaks; then ask the agent why it did not check although the passage was in front of it, and how the passage could be made clearer

Pass: checks unprompted, reads completely before acting, follows under pressure, cannot argue out of it. Fail: skips even without pressure, "adapts the concept" without reading, treats the skill as optional reference.

The source lists expected outcomes per variant (soft suggestion skipped under pressure, directive easy to argue away, emphatic strong but rigid, process-oriented balanced but long). Those are predictions written before running. The source does not report results.

### 7. Trigger queries

Bad: "Convert this file", "Summarise the report", "Make a graph". Too short and abstract; an agent may handle them without any skill.

Good: "hey can you fix up the timesheet export payroll sent over, its in ~/Downloads as 'hours_march (3).csv'. i need one row per person with their total overtime, i think overtime is the col called OT_hrs or maybe 'Overtime'?? finance wants it by thursday". It has a backstory, a file name, a guess at column names, casual spelling and a deadline.

Should-trigger queries: different phrasings of one intent, cases that never name the skill or file type, uncommon uses, and cases where another skill competes but this one should win. Should-not queries: near misses that share keywords but need something else. "Write a fibonacci function" as a negative for a PDF skill tests nothing.

### 8. Product metadata

Good: a destructive deployment-check skill with `allow_implicit_invocation: false` and `default_prompt: "Use $deploy-check to verify the release before promotion."`. Good: a release-notes skill with a short name, a 40-character description and two icons whose paths were checked.

Bad: a generic prompt with no skill token, an icon path that does not exist, and a GitHub dependency block copied from another skill. Bad: a multi-step workflow written into `default_prompt`.

Borderline: omit icons when the interface permits and no approved asset exists. Borderline: a benign formatter keeps implicit invocation after sampled prompts show no false positives, with a note saying when to review.

### 9. Installer requests

| Request | Correct handling |
| --- | --- |
| "What skills can I install?" | Run the lister, show the numbered list with installed marks, ask which |
| "Install the X skill" | Curated path for X; then the restart notice |
| "Install from this private repository URL" | `--url`; rely on git credentials or a token in the environment; never embed the token in the URL |
| "Install the experimental Y" | List or install with the experimental path; say it is experimental |
| "Install skill-creator" (preinstalled) | Explain it is already present; overwrite only if the user insists, and only after they agree to remove the existing folder |

The hardest combination is an experimental skill that is already installed: label the tier, report the existing destination, stop and ask.

### 10. Workflows with checklists and feedback loops

Without code:

```markdown
Incident review progress:
- [ ] 1. Read the timeline, the alerts and the chat log
- [ ] 2. List the decisions that changed the outcome
- [ ] 3. Check each claimed cause against the timeline
- [ ] 4. Write the summary and the action list
- [ ] 5. Confirm every action has an owner (if one does not, return to 4)
```

With code:

```markdown
- [ ] 1. Export the live settings: `python scripts/export_settings.py prod > current.json`
- [ ] 2. Copy to `proposed.json` and edit the copy
- [ ] 3. Validate: `python scripts/check_settings.py proposed.json` (fix every error before continuing)
- [ ] 4. Apply: `python scripts/apply_settings.py proposed.json`
- [ ] 5. Verify: `python scripts/diff_settings.py prod proposed.json` (if it reports a difference, return to 2)
```

The validator can be a document instead of a script: check the draft against the style guide, note each problem with the section it is in, revise, check again, and move on only when nothing is left.

Plan, validate, execute: for a request to update 50 form fields from a spreadsheet, have the agent write `changes.json`, run a validator on it, and only then apply. Make the validator's messages specific enough to act on: "No field named 'sign_date' in the form. Fields found: full_name, total, date_signed". Use this for batch operations, destructive changes, complex validation rules and high-stakes work. The plan can be revised without touching the originals, and errors surface before anything is applied.

Conditional workflow: "Creating new content? Follow the creation workflow. Editing existing content? Follow the editing workflow." Push large branches into separate files.

Output templates: strict ("ALWAYS use this exact template structure") for data formats and API responses; flexible ("a sensible default; use judgment") when adaptation helps. Input and output example pairs teach style better than description, for example three commit messages followed by "Follow this style: type(scope): brief description, then detail."

Offer one default: "Search with `rg`. Where it is not installed, use `grep -rn`." Not "you can use grep, or ripgrep, or ag, or ack, or ...".

Old patterns:

```markdown
## Current method
Request a short-lived token from `auth.example.com/token` and send it as a bearer token.

## Old patterns
<details><summary>Static API keys (retired)</summary>
Requests used to carry a long-lived key in the `X-Api-Key` header. The gateway now rejects it.
</details>
```

### 11. Scripts that solve instead of punting

```python
import json
import sys

# The upstream API cuts requests off after 30 seconds; 35 leaves room for the network.
REQUEST_TIMEOUT_SECONDS = 35


def load_settings(path):
    """Return the settings stored at `path`, or defaults when the file is absent."""
    try:
        with open(path) as handle:
            return json.load(handle)
    except FileNotFoundError:
        # A missing file is normal on first use: say so and carry on.
        print(f"{path} is missing; continuing with built-in defaults", file=sys.stderr)
        return {}
    except json.JSONDecodeError as err:
        # A broken file is not recoverable here: stop with a message the agent can act on.
        sys.exit(f"{path} is not valid JSON (line {err.lineno}: {err.msg}). Fix it and rerun.")
```

Bad: `return json.load(open(path))` and `TIMEOUT = 47  # why 47?`. If the author does not know the right value, the agent cannot determine it either.

Document each script with its command and output format. When layout matters, render the input to images and have the agent look at them.

### 12. The two-instance method

Work a real task with one instance and notice what context you keep supplying (table names, filter rules, preferences). Ask that instance to write the skill. Review it for unneeded explanation ("remove the explanation of win rate") and for structure ("put the schema in a separate file"). Give the skill to a fresh instance on real tasks. Bring specific observations back to the first instance: "it forgot to filter by date for Q4; should there be a section on date filters?" Repeat. Share with teammates and ask whether it activates when expected, whether instructions are clear, and what is missing.

Watch how the consuming agent navigates: an unexpected reading order means the structure is not intuitive; a missed link needs to be more prominent; a file read every time belongs in the body; a file never read is unnecessary or badly signposted.

Test on every model tier the skill will run on. A smaller model may need more guidance; the most capable may be slowed by over-explanation.

### 13. Resume in a multi-file programme

A worker stops with the packet for section 018 saved and the rewritten section 018 not yet saved. The same owner resumes: it reads the journal, confirms sections 001 to 017 exist in both packet and reference, rewrites section 018 from the saved packet, runs the focused check, and continues at 019. Nothing before 018 is regenerated. In the source programme a worker hit a usage quota mid-repair; the same agent was resumed at its saved artifacts instead of redoing 699 targeted repairs.

A repair case: the normalised uniqueness check found copied generic values in three accepted files. The coordinator reopened only those files' rows (354), the original owners rewrote the duplicated values, the focused and corpus uniqueness checks passed, and the files were accepted again. Unrelated rows were untouched.

### 14. Good, bad and borderline at programme level

Good: packet saved, section rewritten, check run, journal updated every third section, verifier passed, coordinator marks rows complete. Bad: five files drafted from memory in one sitting, packets back-filled afterwards with the same sentences under different question labels, queue marked complete by the worker. Borderline: a pure-reference file checked by retrieval only, with the waiver recorded in the journal.

## User Journey Scenario

**Workshop skill from a transcript.** A consultant has just walked a team through a release-notes workflow and says "turn that into a skill". The agent mines the conversation for tools, step order, corrections and formats, confirms the gaps with one question at a time, classifies the skill as a technique, runs the task once without a skill to see what goes wrong, writes resources then the body then the description, validates mechanically, and forward-tests with a fresh subagent on a different repository. The first pass shows the subagent re-deriving the tag range each time; the agent bundles a script. The record lists the type, baseline, prompts, changes and result.

**Draft that never triggers.** A user arrives with a working body and a description that says "Helps with deployments". The agent goes straight to the trigger evaluation: twenty realistic queries with near misses, a 60/40 split, rewrite, and selection on the held-out part. It reports before and after and notes that the result is relative to the model used.

**Rule that gets ignored.** A team's "always run verification before claiming done" skill is skipped when people are in a hurry. The agent classifies it as a discipline skill, runs a baseline with three pressures, records the excuses, adds explicit negations, an excuse table, red flags and description symptoms, and reruns until the agent complies and cites the skill. The campaign record is kept with the skill.

**Plugin migration.** An author used to an init script and a packaging script moves a skill into a plugin. The agent uses the delta table: `mkdir`, no packaging, the eight-point checklist by hand, and a `cc --plugin-dir` trigger test.

**Install request.** "What skills are there?" gets the annotated list and "Which ones would you like installed?". The chosen skill is fetched by the ladder; an existing destination stops the install and the agent asks; after success the agent gives the restart notice.

**Ninety-nine references.** A library owner wants every reference deepened. The coordinator freezes the corpus, generates the queue, assigns four lanes, and starts four workers. Each worker reads a whole file, answers ten questions per section, saves the packet then the section, journals every three sections, rereads, and runs the verifier. The coordinator marks rows complete. The corpus suite starts red (in the source programme four checks passed and three failed at the outset, for unchanged references, missing packets and pending rows) and stays red until the last file is accepted. In the source programme the count went from 47 files and 5,703 rows at a handoff to 99 files and 11,961 rows, with the final suite passing eight of eight tests.

**Arrival without programming background.** The loop is the same. The agent says "a check that can be marked pass or fail" before it says "assertion".

## Anti Pattern Registry Table

| Area | Anti-pattern | Signal | Replace with |
| --- | --- | --- | --- |
| Trigger | Vague description | Skill never loads | Phrases, files, tools, symptoms |
| Trigger | Workflow in description | Agent skips steps the body requires | Triggers only |
| Trigger | Wrong grammatical person | Inconsistent with injected system text | Third person |
| Trigger | Keyword stuffing | No longer a sentence; false positives | Readable sentence, near-miss test |
| Trigger | Language-specific symptom for a general skill | Misses other languages | Describe the problem |
| Body | Monolithic body | Thousands of words loaded every time | Progressive disclosure |
| Body | Duplicate content in body and reference | Drift | One owner per fact |
| Body | Unreferenced resource | File never opened | Link with a when-to-use line |
| Body | Second-person or tutorial prose | "You should ..." | Imperative |
| Body | Narrative ("on that date we found ...") | Not reusable | The technique |
| Body | Many options without a default | Agent dithers | One default, one escape hatch |
| Body | Time-sensitive statement | Wrong after the date | Current method plus old patterns |
| Body | Mixed terminology | "field", "box", "element" for one thing | One term |
| Body | Multi-language examples | Diluted quality | One excellent example |
| Body | Code or reference material in a flowchart | Cannot copy or scan | Code block or table |
| Body | Generic flowchart labels (step1, helper2) | No meaning | Semantic labels |
| Body | Windows-style paths | Fail on Unix | Forward slashes |
| Body | Assumed tools | "Use the pdf library" | Install command, then usage |
| Body | Unqualified MCP tool name | Tool not found | `ServerName:tool_name` |
| Body | Deeply nested references | Partial reads miss content | One level deep |
| Body | Force-loading links to other skills | Context consumed before needed | Name the skill with "required" marker |
| Body | Auxiliary files (README, changelog) | Clutter | Delete |
| Body | Ancestor workflow in a plugin | Init or packaging script that does not exist there | Delta table |
| Scripts | Punting errors to the agent | Bare `open(path).read()` | Handle and explain |
| Scripts | Unexplained constants | `TIMEOUT = 47` | Justified values |
| Scripts | Untested bundled script | Fails on first use | Run it |
| Evaluation | No baseline | Rules for imagined failures | Run without the skill first |
| Evaluation | Academic test | Agent recites | Forced choice under pressure |
| Evaluation | One pressure | Agent holds, then breaks in real use | Three or more |
| Evaluation | Paraphrased excuse | Loophole lost | Verbatim |
| Evaluation | Generic counter | "Don't cheat" | Negate the specific excuse |
| Evaluation | Stop after first pass | Next excuse unseen | Rerun until no new excuses |
| Evaluation | Softening pressure until it passes | False pass | Keep pressure; meta-test instead |
| Evaluation | Non-discriminating assertion | Passes with and without the skill | Assertion a baseline can fail |
| Evaluation | Ungrounded grade | Pass with no quote | Cite evidence |
| Evaluation | Context leakage | Subagent given diagnosis or fix | Raw artifacts only |
| Evaluation | Overfit to known examples | Fiddly special cases | Generalise; think of many future uses |
| Evaluation | Capital-letter rules after one failure | Rigid skill | Explain the reason |
| Evaluation | Stale runs reused | Old outputs graded as new | Fresh iteration directory |
| Evaluation | Hand-built viewer JSON | Empty fields | Exact schema |
| Evaluation | Author self-evaluation only | No independence | Any independent role |
| Evaluation | Batch-writing skills | None tested | One campaign at a time |
| Metadata | Instructions in `agents/openai.yaml` | Never read by the agent | `SKILL.md` |
| Metadata | Unquoted strings or quoted keys | Parse differences | Quote values only |
| Metadata | Missing `$skill-name` | Prompt does not invoke | Exact token |
| Metadata | Unsupported dependency type | Ignored or rejected | `mcp` only |
| Metadata | Copied optional boilerplate | Dependency the skill does not use | Omit |
| Metadata | Accidental implicit activation | Sensitive skill fires unasked | `false` |
| Metadata | Field accepted but ignored | Silent no-op | Check the harness version |
| Distribution | Clobbering an existing skill | Destination exists | Stop and ask |
| Distribution | Missing restart notice | "Installed but not there" | Say it |
| Distribution | Reinstalling preinstalled skills | Redundant download | Explain |
| Distribution | Credentials in URLs | Token in logs | Environment or git credentials |
| Distribution | Unlabelled experimental source | Trust confusion | Label the tier |
| Distribution | Manual clone | Bypasses abort and naming | Use the script |
| Programme | Summary without a source map | Cannot audit | Map sources first |
| Programme | Unsourced recommendation as fact | No label | Evidence label |
| Programme | Instruction without a gate | Cannot check | Couple each to a verification |
| Programme | Two writers on one path | Lost work | One owner |
| Programme | Worker edits the queue | Status unreliable | Coordinator only |
| Programme | Tool-written prose | Generic filler | Agent writes, tool checks |
| Programme | Prose before packet | Unreviewed rewrite | Packet first |
| Programme | Several sections held only in context | Lost on interruption | Save each section |
| Programme | Exact-match uniqueness only | Prefixed copies pass | Normalise |
| Programme | Complete before verifier | False status | Verify first |
| Programme | Regenerate after interruption | Valid work lost | Resume |
| Programme | Early combined synthesis | Inherits weak inputs | Wait for all rows |
| Programme | Duplicate copies counted as separate evidence | Inflated support | Identify lineage; one source |
| Programme | Length as quality | Padding | Coverage of reasoning |
| Programme | Shell loop variable named `path` in zsh | Command lookup breaks | `ref` or `file_path` |

## Verification Gate Command Set

Status of each group is stated. "Run on a fixture" means the command was executed against a small synthetic input while writing this file and behaved as described. "Not run" means the command is recorded from its source and was not executed.

### Skill gates (run on this skill)

The five mechanical gates in `SKILL.md` (front matter, links, placeholders, size, metadata). Add:

```bash
# Every bundled file is mentioned in SKILL.md
S=path/to/skill-folder
for f in "$S"/scripts/* "$S"/assets/* "$S"/references/* "$S"/examples/*; do
  [ -e "$f" ] && { grep -q "$(basename "$f")" "$S/SKILL.md" || echo "not mentioned: $f"; }
done
# Bundled validator (Codex field rules); needs PyYAML
python3 scripts/quick_validate.py "$S"
```

### Plugin skill checklist (manual, eight points)

1. `SKILL.md` is at `skills/<name>/SKILL.md` inside the plugin.
2. Front matter has `name` and `description`.
3. The description contains specific trigger phrases.
4. The body is imperative, not second person.
5. The body is lean; detail is in references.
6. Every referenced file exists.
7. Examples are complete and correct.
8. Scripts are executable and documented.

Then `cc --plugin-dir /path/to/plugin` and ask questions that should trigger the skill (not run). A reviewer agent, where the plugin provides one, is asked "Review my skill and check if it follows best practices". When no reviewer is available the checklist still applies.

### Pre-share checklist (Anthropic guide)

Core quality: description specific with key terms and stating what and when; body under 500 lines; details in separate files; no time-sensitive information; consistent terminology; concrete examples; references one level deep; progressive disclosure; clear workflow steps.

Code and scripts: scripts solve problems instead of punting; explicit, helpful error handling; no unexplained constants; required packages listed and confirmed available; scripts documented; forward-slash paths; validation steps for critical operations; feedback loops for quality-critical tasks.

Testing: at least three evaluations; tested on each model tier in use; tested with real usage; team feedback incorporated.

### Discipline skill checklist

Red: scenarios with three or more pressures written; baseline run without the skill; excuses recorded verbatim; patterns identified. Green: name and front matter valid; description with triggers and keywords; overview states the core principle; baseline failures addressed; code inline or linked; one excellent example; scenarios rerun with the skill. Refactor: new excuses found; counters added; excuse table built; red flags listed; rerun until no new excuses. Quality: flowchart only where the decision is not obvious; quick-reference table; common mistakes; no narrative; extra files only where a tool or bulky reference material needs them. Deployment: commit through the repository's normal review process. The source checklist also says to push to a fork; do that only when the repository owner has asked for it.

### Quantitative harness (not run; requires the Claude skill-creator plugin, which is not bundled)

```bash
cp -r <skill-path> <workspace>/skill-snapshot/                     # baseline snapshot before editing
python -m scripts.aggregate_benchmark <workspace>/iteration-N --skill-name <name>
python <skill-creator-path>/eval-viewer/generate_review.py <workspace>/iteration-N \
  --skill-name "my-skill" --benchmark <workspace>/iteration-N/benchmark.json \
  [--previous-workspace <workspace>/iteration-(N-1)] [--static <output_path>]
python -m scripts.run_loop --eval-set <trigger-eval.json> --skill-path <path-to-skill> \
  --model <model-id-in-use> --max-iterations 5 --verbose
python -m scripts.package_skill <path/to/skill-folder>
```

`aggregate_benchmark` must run as a module from the creator's directory. It writes pass rate, time and tokens per configuration as mean and standard deviation plus the difference, with the with-skill configuration listed first. The trigger loop runs each query three times, splits 60/40 and returns the description with the best held-out score. Use `--static` where no display is available. The ancestor creator's `scripts/package_skill.py <folder> [./dist]` validates and zips, and refuses to package when validation fails.

### Installer (not run; needs network)

```bash
python3 scripts/list-skills.py --format json
python3 scripts/install-skill-from-github.py --repo <owner>/<repo> --path <path> [<path> ...] [--ref <ref>] [--dest <dir>] [--method auto|download|git]
ls "${CODEX_HOME:-$HOME/.codex}/skills/<name>/SKILL.md"       # ground truth: the directory exists
```

Directory existence proves the install happened, not that the skill works.

### Programme gates (run on a fixture)

```bash
# 1. Inventory and file set: one file per theme, four-word names, no extras
python3 - themes.md refs <<'EOF'
import re, sys, pathlib
themes = re.findall(r"^\| `([a-z0-9_]+)` \|", pathlib.Path(sys.argv[1]).read_text(), re.M)
files = {p.stem for p in pathlib.Path(sys.argv[2]).glob("*.md")}
assert all(len(t.split("_")) == 4 for t in themes), "label is not four words"
assert len(themes) == len(set(themes)), "duplicate theme"
assert files == set(themes), (sorted(set(themes) - files)[:5], sorted(files - set(themes))[:5])
print("inventory_file_set_ok", len(themes))
EOF

# 2. Required headings present and in order, ignoring headings inside code fences
python3 - refs/some_theme_label_here.md "Workload Model" "Reliability Target" <<'EOF'
import sys, pathlib
heads, fence = [], False
for line in pathlib.Path(sys.argv[1]).read_text().splitlines():
    if line.lstrip().startswith(("```", "~~~")):
        fence = not fence
    elif not fence and line.startswith("## "):
        heads.append(line[3:].strip())
want = sys.argv[2:]
pos = [heads.index(h) for h in want]          # ValueError names a missing heading
assert pos == sorted(pos), "headings out of order"
print("heading_order_ok", len(want))
EOF

# 3. Four-word label gate for backticked snake_case labels
python3 - refs <<'EOF'
import re, sys, pathlib
bad = [(p.name, m) for p in pathlib.Path(sys.argv[1]).glob("*.md")
       for m in re.findall(r"`([a-z][a-z0-9]*(?:_[a-z0-9]+)+)`", p.read_text()) if len(m.split("_")) != 4]
print(bad or "four_word_label_ok"); sys.exit(1 if bad else 0)
EOF

# 4. Queue: one owner per file, every line covered once, unique ids, status counts
python3 - queue.csv <<'EOF'
import csv, sys, collections, pathlib
rows = list(csv.DictReader(open(sys.argv[1])))
by = collections.defaultdict(list)
for r in rows: by[r["reference_file_path"]].append(r)
for path, rs in by.items():
    assert len({r["agent_id"] for r in rs}) == 1, f"{path}: more than one owner"
    nxt = 1
    for r in sorted(rs, key=lambda r: int(r["start_line"])):
        assert int(r["start_line"]) == nxt, f"{path}: gap or overlap at line {nxt}"
        nxt = int(r["end_line"]) + 1
    total = len(pathlib.Path(path).read_text().splitlines())
    assert nxt - 1 == total, f"{path}: covered {nxt - 1} of {total} lines"
assert len({r["unit_id"] for r in rows}) == len(rows), "duplicate unit_id"
status = collections.Counter(r["task_status"] for r in rows)
accepted = sum(all(r["task_status"] == "complete" for r in rs) for rs in by.values())
print("queue_ok", dict(status), "files", len(by), "accepted", accepted)
EOF

# 5. Packet uniqueness, exact and normalised (exit 1 when prefixed copies exist)
python3 - packet.md <<'EOF'
import re, sys, collections, pathlib
prefix = re.compile(r'^Section \d{3}\s+(?:\([^)]*\)|"[^"]*"),\s*Question \d{2}(?:\s+on\s+[^:]+)?:?\s*')
vals = re.findall(r"^- \*\*[a-z_]+:\*\* (.+)$", pathlib.Path(sys.argv[1]).read_text(), re.M)
norm = [" ".join(prefix.sub("", v).split()).casefold() for v in vals]
dupes = [v for v, n in collections.Counter(norm).items() if n > 1]
print("fields", len(vals), "exact_unique", len(set(vals)), "normalised_unique", len(set(norm)))
sys.exit(1 if dupes else 0)
EOF

# 6. Placeholders and whitespace
grep -n -E "\b(TODO|TBD|FIXME|STUB)\b" refs/*.md packets/*.md
git diff --check
```

On the fixture, gate 5 reported four exact-unique values and three normalised-unique values for a packet in which two answers differed only by their section and question prefix. That is the failure the gate exists to catch.

Other gates from the generation specification, to write per programme: every listed source path appears in its reference; the coverage manifest has one row per theme; each critique file has one header, one fenced block and one exact path per reference, and each block contains the required markers; the journal has its seven headings and a non-empty next step.

### Programme scripts as used in the source programme (not run from this folder)

```bash
python3 <verification-dir>/tests/verify_idiomatic_reference_file.py --path <reference>
python3 <automation-dir>/update_idiomatic_evolution_queue.py --path <reference> [--path <reference> ...]
python3 <automation-dir>/update_idiomatic_evolution_queue.py --path <reference> --reopen
python3 -m unittest tests.test_idiomatic_reference_evolution
python3 -m unittest tests.test_idiomatic_reference_evolution.IdiomaticReferenceEvolutionTests.test_packet_content_uniqueness
```

The verifier prints JSON with status, reference and packet paths, owner, section count, original and rewritten character counts, question count, field count and both uniqueness counts. The updater verifies each path, then sets every row for it to complete with a note recording the packet path and the completed stages, writing through a temporary file, `fsync` and replace. With `--reopen` it sets the rows back to pending and clears the notes without verifying. It refuses to write an empty queue and fails when a path has no rows. The corpus suite checks inventory counts, unique ownership, lane manifests against the queue, that each reference differs from its original with the same headings and every section longer, packet structure and exact question text, uniqueness, queue completeness with non-empty notes, and the placeholder ban. The uniqueness test skips packets that are not yet full, so partial drafts do not fail it. The full suite stays red until the last file is accepted; that is expected.

What these scripts do not check: truth of any claim, whether the right owner did the work, whether the reread happened, or whether longer is better. The length check counts characters only.

### Gate checklists from the evolution specification

Queue initialisation: file count, physical line count and unit count match the measured values; every source line is in exactly one unit; block-type totals match; every file has exactly one predetermined owner; lane totals match; parser fixtures pass; every status is pending and every note empty.

Per unit: the whole frozen span was read; section, table and list context considered; the section's packet was complete before the unit changed; meaningful claims received reasoning for and against; conclusions from all ten answers applied; a keep, rewrite, expand, move or remove decision recorded; weak certainty bounded or removed; movement across units noted; the next unit not started out of order.

Per section: every unit reviewed; ten questions posed and answered before editing; six fields in every answer; no answer reusing normalised content from another field under a different label; every decision and insight incorporated or declined with a reason; the section reread as one argument; table rows consistent with headers and each other; list items forming a progression; defaults, exceptions, examples and gotchas not in conflict; detailed without padding; repetition created by unit edits removed; rows moved to section-complete only afterwards.

Per file: the owner read the whole original before editing; every unit passed its hash check; every section reconciled; the file saved only after reconciliation; the whole rewritten file reread sceptically; the ten questions answered consistently at file level; the packet has all field values unique both ways; rows moved to complete only after the reread.

Per pass: all rows complete; all files passed; no row pending, active, merely reviewed, section-only or blocked; no file edited by more than one agent; no file lost, renamed or skipped; the archived originals unchanged; the combined pass still blocked until now.

Before committing: every requirement has a test; fixtures and queue integrity pass; no placeholder stands in for reasoning; no number lacks a verification method or an uncertainty label; `git diff --check` is clean; nothing is staged, committed or pushed without the user's explicit permission.

## Failure Mode Table

| Failure | Signal | Response |
| --- | --- | --- |
| Skill does not trigger | Fresh agent ignores it on a matching request | Add phrases and symptoms; test with substantive queries; check that the query is hard enough to need a skill |
| Skill triggers wrongly | Near-miss queries load it | Add "Not for" clauses; remove stuffed keywords |
| Agent follows the description, skips the body | Steps in the body not performed | Remove workflow from the description; retest |
| Agent ignores a bundled file | File never read in transcripts | Signpost it in the body or delete it |
| Agent rereads one reference every time | Same file in every transcript | Move that content to the body |
| Rule broken under pressure | New excuse in the campaign record | Four-edit counter; rerun the original scenarios |
| Same excuse survives two counters | Repeated quote | Meta-test; if the skill was clear and ignored, redesign or escalate; do not soften the pressure |
| Edit reopens a closed loophole | Old excuse returns | Rerun all original scenarios after each edit |
| Pressure results stale | Model or scenario changed | Re-baseline |
| Benchmark all green | No difference between configurations | Check assertions for discrimination; read the analyst notes |
| Flaky evaluation | High variance across runs | More runs; inspect transcripts before trusting the mean |
| Test passes only with leaked context | Subagent given the diagnosis | Tighten the skill or the setup |
| Timing data lost | Notification not saved | Cannot be recovered; rerun |
| Viewer shows empty fields | Hand-written JSON with other field names | Regenerate with the exact schema |
| Front matter rejected | Unexpected key, long description, angle bracket | Use the target validator's field list |
| Metadata parses but skill not shown | Harness ignores a field or caches the interface | Check harness version; record activation as not observed |
| Broken icon path | Asset missing | Fix the path or omit the field |
| MCP dependency unavailable | Server unreachable or wrong transport | Bounded probes; escalate to whoever owns the integration |
| Implicit false activation | Sensitive skill fires unasked | Set implicit invocation false |
| Download fails with 401, 403 or 404 | Installer error | Next method: git over HTTPS, then SSH |
| Destination exists | "Destination already exists" | Stop and ask |
| Curated listing unavailable | 404 or network error from the lister | Explain and stop |
| Partial multi-path install | Later path failed | Report which directories exist |
| Parser yields a node without a source position | Queue generation error | Stop; fix the parser |
| Hash mismatch on a span | Verifier error before first edit | Block every row of the file until the snapshot is deliberately refreshed |
| Missing, duplicate or overlapping unit | Coverage gate fails | Stop the file; rebuild; reverify coverage |
| Two owners for one file | Ownership gate fails | Stop both; restore the predetermined owner |
| Interruption mid-file | Journal ends mid-section | Preserve the draft and the last reviewed unit; same owner resumes |
| Heading renamed or unit moved | Live lines differ from the frozen snapshot | Keep frozen identifiers; explain in the completion notes |
| Table rows inconsistent | Found at reconciliation | Resolve against the header during section reconciliation |
| Advice conflicts with another section | Found at reread | Resolve during section and final rereads |
| Ten questions expose weak evidence | Answers cannot support the claim | Rewrite as bounded judgment or stated uncertainty |
| Worker cannot finish its file | Repeated failure or quota | Mark rows blocked; the coordinator may reassign the whole file only, never part of it |
| Prefixed generic duplicates | Normalised uniqueness below field count | Reopen affected rows only; same owner repairs |
| Queue write interrupted | Temporary file left behind | The atomic replace protects the original; rerun the updater |
| Damage suspected in a programme file | Verifier or diff shows unexpected change | Stop; identify which artifact (reference, packet, journal, queue); diff only that file; restore from version control only with the user's approval; keep completed sections of the partial file; rerun the focused verifier before continuing |

## Workload Model

**One skill.** One author conversation, one skill folder, a handful of bundled files. Evaluation load is two or three prompts in two configurations for a quantitative check (the harness default is three runs per configuration), or a handful of scenarios of three or more pressures for a discipline campaign, or about twenty trigger queries each run three times. One campaign per skill; campaigns are never interleaved.

**One metadata change.** One skill, one product, one `agents/openai.yaml`, its assets and dependencies, one policy decision, one rollback. Copying one file across twenty unrelated skills is the wrong unit. A template is acceptable only when optional fields, resources and policy are parameters and each skill is validated separately.

**One install conversation.** One person, a single-digit number of skills, one home directory, network consent per run.

**One reference programme.** In the source programme: 99 files of 26 sections, 11,961 units, four workers and one coordinator, each worker on one file at a time in lane order. Per file: 260 answers and 1,560 field values, saved section by section.

**One agent reading a reference.** The source references use a shared, uncalibrated bound: one primary task, at most ten source files, at most three delegated subtasks, and a written completion audit.

None of these figures is a capacity measurement. They describe how the work was organised.

## Reliability Target

Targets below are stated by the sources as working goals. No baseline was measured for any of them.

- Every recommendation shows whether it is a local fact, an external fact or an inference.
- At least 18 of 20 sampled uses route to the right guidance. This is a smoke test, not a validation study, and it cannot be allowed to hide one dangerous false activation.
- No unsupported claim.
- Every "avoid" or failure entry names a rollback, an escalation or a next route.
- A reviewer can identify the next action, the gate and the stop condition without opening unrelated files, within about ten minutes.
- A discipline skill "holds" when the agent chooses correctly, cites the skill, acknowledges the temptation and complies under combined pressure, on fresh scenario variants so that memorisation is not what is measured.
- A programme file is accepted only when both artifacts exist, all sections and questions are present, every field is populated and unique both ways, structure and whitespace checks pass, the reread is recorded and the verifier passes. The queue is updated only after that.
- Installation is reliable at the state boundary: no existing directory is ever overwritten by the script.
- Regenerating the queue from the same inputs gives the same bytes.

## Retry Backpressure Guidance

- **Classify before retrying.** A deterministic check (parse, validate, link check) is rerun only after the file changes. Fail fast on unchanged invalid input.
- **Installer.** Retry only with a changed strategy, which means the next method on the ladder. Do not repeat a method that failed on authentication. An existing destination and an unavailable listing are hard stops. One repeat after a transient timeout is reasonable; the source does not document it. Never delete a directory to make a retry succeed.
- **Dependency probes.** Bounded. Do not repeat activation tests without new evidence.
- **Evaluation.** After any change to the skill, regenerate every run in a new iteration directory with fresh metadata. The only deliberate reuse is the snapshot baseline in improve mode. Forward tests use a fresh thread and a cleaned workspace each pass. When parallel runs time out, fall back to running in series.
- **Pressure campaigns.** When the same excuse survives two counters, stop adding counters and run the meta-test. Never lower the pressure to get a pass.
- **Programme.** Four workers is the concurrency limit in the source design; parallel edits are allowed only when the active paths differ. A worker holds at most one unsaved section. Backpressure is the gate: a file that fails verification does not advance, and the combined pass does not start while any row is incomplete. Reopen the narrowest set of rows. A blocked file is reassigned whole or not at all. After an interruption, resume; do not regenerate.
- **Feedback.** When human feedback stops arriving or stops being specific, stop expanding the evaluation set. Feedback quality runs out before compute does.

## Observability Checklist

For a skill evaluation, keep:

- [ ] The transcript of each run, not only its output.
- [ ] Token and duration figures saved at notification time.
- [ ] Assertions and grades with cited evidence.
- [ ] Analyst notes: non-discriminating assertions, high variance, time and token tradeoffs.
- [ ] Notes the executor left for the user.
- [ ] Human feedback per run.
- [ ] The model identifier used.

For a pressure campaign, per iteration: scenario, pressures, choice, verbatim excuse, the change made, the counter added, the verdict.

For a metadata change: skill and product version, file hash, fields present and omitted, parse result, resolved assets, dependency status, activation samples, false positives and misses, retries, reviewer decision, rollback. Redact credentials. Never log authorisation headers or URLs that carry credentials.

For an install: method used, the user's choices, whether escalation was requested, and the resulting directory.

For a programme: queue status counts; the journal per lane and the master journal; the last saved section per file; verifier JSON per file; uniqueness counts; rows reopened and why; the owner of every file.

For navigation: which bundled files the consuming agent actually opened, and in what order.

## Performance Verification Method

Performance of a skill means its effect on outcomes and its cost in context and time.

1. **Effect.** Same prompts with and without the skill (or old and new version). Report pass rate per configuration as mean and standard deviation over repeated runs, and the difference.
2. **Cost.** Report tokens and duration the same way. Read cost and benefit together. The source schema's illustration is a gain of 50 points in pass rate for 13 extra seconds, which may well be worth it; that is an illustration, not a result.
3. **Decompose token overhead** into skill loading and script-output handling before optimising either.
4. **Size.** `wc -l` and `wc -w` on the body. Word counts undercount tables, code fences and front matter, so check both and track where content sits as well as how much there is; an 1,800-word body can still duplicate its references.
5. **Triggering.** Held-out score on the trigger set, before and after.
6. **Compliance.** Number of new excuses per rerun; zero is convergence.
7. **Programme throughput.** Files accepted and rows complete over time, from the journal; reopened rows as a share of accepted rows.

Not measured anywhere in the sources: live trigger rate in production use, install transfer times, how often each fetch method fails, latency of any step, or the claim that testing saves time overall. Treat those as open.

**Installer fetch cost.** The installer downloads the requested directory directly first, because that avoids git overhead. Its git fallback is a sparse checkout of the requested paths, not a full clone, so the rest of the repository is never fetched. Several `--path` values in one run avoid repeated start-up, but the paths are then fetched in series. Do not start with git or clone a whole repository for one directory unless the environment forces it. Caching or mirroring skills for a fleet is a separate design. Large assets inside a skill change the transfer cost.

## Scale Boundary Statement

- The quantitative harness is designed for a single-digit number of evaluations reviewed by one attentive person. Expand the set only after feedback converges.
- Full re-testing of every skill is practical while a library is small. Beyond that, move to risk-ranked sampling, shared and versioned scenario suites, rolling quotas and visible staleness markers. Re-baseline discipline skills after a major model change; a model upgrade silently invalidates old compliance results. Two preconditions make this workable: each pressure campaign has exactly one named owner, and every skill carries a type and a risk label so that sampling can rank them (discipline skills first after an upgrade). Running one campaign at a time is itself a scale rule: it stops verification debt from piling up unseen. The library size at which sampling must begin was not measured; check that sampled skills show no more violations than fully tested ones.
- The installer serves one person interactively. Fleet or scheduled provisioning is a different design with different consent rules.
- The section-by-section programme assumes files of similar shape (26 sections in the source). Files of very different shape need their own section count, verifier constants and reread grouping.
- The verifier checks structure and text, not truth. Past a few files, add sampling by a reviewer who did not write them.
- Body-size limits are runtime-dated. A cross-platform skill takes the strictest applicable limit.
- Guidance on trigger wording is relative to the model that reads descriptions. Recheck after a model change.
- "Skills ship with the plugin, no packaging" is platform policy and likely to change first.
- The combined pass that groups specialist files into larger references was planned and deferred in the source programme. Its grouping (candidate dimensions included agent design, test-first and specifications, language backends, frontend, plugin and skill development, documentation and visuals, debugging and review, planning and design), its queue and its agent allocation were to be derived from the finished specialist files, not decided in advance.

## Outcome Metrics and Feedback Loops

| Metric | Source of data | Reading |
| --- | --- | --- |
| With and without pass rate, time, tokens | Benchmark | Effect and cost together |
| Held-out trigger score | Trigger loop | Reach without overfitting |
| Human feedback per iteration | Review | Empty feedback is weak evidence of convergence, not proof |
| New excuses per rerun | Campaign record | Zero means the rule holds for those scenarios |
| Share of skills with a baseline captured before writing | Records | Process discipline |
| Share of skills with a campaign or test record | Records | Coverage |
| Violations seen after deployment | Use | Reopen the campaign |
| Body words and lines; trigger phrases covered | `wc`, description | Count and placement, separately |
| Eight-point checklist pass rate; time from friction to fix | Reviews | Plugin skills |
| Parse failures, broken paths, prompt-token compliance, description-length violations, missing dependencies | Metadata checks | More fields and one successful invocation are not quality |
| Explicit activation success; implicit false positives and misses | Runtime observation | Only when observed |
| Install success by fetch method (direct download, git over HTTPS, git over SSH) | Install records (proposed) | Which method carries the load; a rising share of fallback installs is an early warning |
| Dialogue compliance: annotated list shown, "which ones" asked, source labelled, restart notice given | Transcripts (proposed) | Whether the unenforced installer rules are eroding |
| Share of installs from curated, experimental and arbitrary repositories | Install records (proposed) | Trust mix |
| Reports of a "broken" skill that only needed a restart | Support requests (proposed) | Missing restart notices, measured indirectly |
| Files accepted, rows complete, rows reopened | Queue and journal | Programme progress and rework |
| Normalised-unique field count | Verifier | Generic-prose detection |

The four installer rows are proposed measures. They are inferred from the installer's rules; the installer specifies no telemetry and no source holds data for them, so reuse them as inference, not as documented practice. The fetch-method split carries the most information. A healthy installer works mostly by direct download, so a rising share of git fallbacks points to an upstream authentication or API change before it becomes an outright failure. Counting installs while the dialogue obligations quietly disappear is the bad version of this measurement. Confusion reports are an indirect reading of restart-notice compliance; checking transcripts for the notice is the direct one. Quality of the installed skills themselves is measured by the evaluation rows, not here.

Feedback loops:

- Use, notice struggle, update, retest. Improving only the paths that were just exercised can overfit; a periodic formal evaluation is the counterweight.
- Generalise from feedback. The skill will be used many times on inputs unlike the test prompts. Explain reasons instead of adding rigid special cases; try a different metaphor or pattern when a change does not stick; remove parts that make runs do unproductive work.
- Read transcripts. When several runs independently write the same helper, bundle it as a script.
- Draft, then reread with fresh eyes before testing.
- In a programme, defects found by a later gate feed back as narrowly reopened rows to the same owner, and the new check that found them becomes part of the per-file verifier from then on.

## Completeness Checklist

A skill:

- [ ] Purpose stated in one or two sentences.
- [ ] Type classified; tone and test chosen from it.
- [ ] Description in the target convention with triggers and exclusions; no workflow.
- [ ] Body within the strictest applicable size limit.
- [ ] Workflow steps numbered; fragile steps given exact commands.
- [ ] One default per choice.
- [ ] One strong example.
- [ ] Every bundled file linked, with run-or-read stated.
- [ ] Dependencies listed with install commands.
- [ ] No duplication between body and references; references one level deep; long references have contents.
- [ ] No time-sensitive statements; one term per concept.
- [ ] Baseline captured; test record written; waiver recorded if any.
- [ ] Metadata, if any, minimal, quoted, with the skill token and a deliberate policy.
- [ ] Distribution route chosen for the target runtime.

A discipline campaign covers three phases (red, green, refactor), draws on seven pressure types, and applies the four-type test matrix.

A reference file in a programme:

- [ ] Thesis, ranked patterns, usage guide, tradeoffs.
- [ ] One theme-specific artifact.
- [ ] Good, bad and borderline examples.
- [ ] A user journey.
- [ ] Anti-patterns, gates, failure modes.
- [ ] Workload, reliability target, retry guidance, observability, performance method, scale boundary.
- [ ] Metrics and feedback loops.
- [ ] Routing to adjacent references.
- [ ] Source map with roles and lineage; evidence labels; refresh queries.

A programme:

- [ ] Frozen inventory and manifest.
- [ ] One owner per file; lane manifests.
- [ ] Queue covering every line.
- [ ] Packet per file; journal per lane; master journal.
- [ ] Verifier and corpus suite.
- [ ] Handoff document when work changes hands.
- [ ] Combined synthesis blocked until all rows are complete.

## Adjacent Reference Routing

Sibling skills are named, not linked, because each is installed separately.

| Need | Go to |
| --- | --- |
| Repository instruction files, context budgeting, subagent orchestration | `agent-context-and-orchestration` |
| Plugin manifests, hooks, commands, agents, MCP server setup | `claude-plugin-development` |
| Requirements written as testable statements with a test matrix | `executable-specs` |
| Progress journals, save points and resume across interruptions in general | `tdd-progress-and-resume` |
| Reviewing, verifying before claiming completion, debugging | `review-verify-debug` |
| Prose structure and plain writing | `structured-writing` |
| Diagrams and visual explanations | `visual-explainers` |
| Commits, branches and pull requests | `git-delivery-flow` |
| Language or framework content of a reference | The skill for that language or framework |
| Icon or image creation for metadata | `generative-art-and-images` |

Library-level background: [LLM principles](../../A00-LLM-Principles01.md), [LLM workflow](../../A01-LLM-Workflow01.md), [the reference-generation prompt](../../A02-Mega-Idiomatic-Prompt.md), and [executable specifications](../../A03-Executable-Specs01.md).

When routing a metadata question to another skill or owner, hand over a compact packet: the disputed question, the skill and the product, the existing metadata, the evidence gathered so far, the answer expected back, the condition for returning, the field that would change, and a check that the route does not loop back to where it started. Do not route by keyword alone, do not dump the whole context on the receiver, and reconcile the returned answer with the invocation policy before changing the field.

Boundaries inside this subject: asset creation and asset-path validation are separate jobs that share one contract, the asset path; MCP server credentials belong to integration work, not to skill metadata; generic YAML syntax questions go to a YAML parser.

## Source Evidence Mapping Table

Sources are named by role. The audit ledger kept with the merge work lists exact paths.

| Source | Role | Class | Contributed |
| --- | --- | --- | --- |
| Reference-generation specification (June 2026) | Canonical for the file contract | Local | Seventeen-step contract, four-word labels, critique passes, production-readiness headings, gate scripts, open decisions |
| Theme index (June 2026) | Supporting | Local | One theme per reference role; every source path listed once; counts |
| Evolution project README (July 2026) | Supporting | Local | Which records are kept and why |
| Evolution specification (July 2026) | Canonical for the multi-agent method | Local | Actors, lanes, unit rules, queue schema, ten questions, six fields, cadence, requirements, failure handling, gate checklists |
| Evolution handoff | Supporting | Local | Handoff shape, per-file procedure, constraints, rollback, later-pass plan |
| Evolution progress journal | Canonical for outcomes | Local, measured | Duplicate counts, reopened rows, resume cases, final counts |
| Queue updater script | Canonical, bundled | Local | Verify-then-complete, atomic write, reopen |
| Corpus test suite | Canonical, bundled | Local | Inventory, ownership, packet and queue tests |
| Per-file verifier | Canonical, bundled | Local | Per-file acceptance checks |
| Reference on skill metadata YAML | Digest of the Codex metadata material | Local | Activation contract, policy guidance, failure classes, metrics |
| Reference on creator evaluation | Digest of both creator skills | Local | Two-tradition split, independence, roles, ranking |
| Reference on plugin skill development | Digest of the plugin guide and its ancestor | Local | Delta table, budget ladder, spillover chain |
| Reference on installer distribution | Digest of the installer skill | Local | Fetch ladder, dialogue obligations, scale envelope |
| Reference on writing-skills validation | Digest of the test-first material | Local | Campaign record, convergence metric, scaling |
| Codex skill-creator (March 2026 snapshot) | Canonical for Codex | Local | Anatomy, freedom levels, process, forward-testing |
| Codex metadata reference | Canonical for the field list | Local | Fields and constraints |
| Codex creator scripts (three) | Canonical, bundled | Local | Init, metadata generation, validation |
| Codex creator and installer `openai.yaml` files | Instances | Local | Minimal real field use (not bundled) |
| Codex creator licence | Bundled | Local | Apache 2.0 terms |
| Codex skill-installer | Canonical for Codex distribution | Local | Listing and install conduct |
| Codex installer scripts (three) and icons (two) | Canonical, bundled | Local | Fetch ladder, traversal guard, abort on existing destination |
| Plugin-development skill guide | Canonical for plugin skills | Local | Third-person descriptions, word budget, checklist, plugin testing |
| Embedded original creator | Ancestor of the plugin guide | Local, duplicate lineage | Packaging step only |
| Claude skill-creator | Canonical for the quantitative harness | Local | Loop, workspace, schemas, trigger optimisation, environments |
| Superpowers writing-skills | Canonical for test-first authoring | Local | Iron Law, description rule, body template, word targets, loophole closing |
| Anthropic authoring guide (copy inside writing-skills) | Canonical vendor guidance | Local copy of external text | Conciseness, naming, workflows, feedback loops, scripts, runtime model, checklist |
| Subagent testing guide | Canonical for pressure tests | Local | Phases, pressures, scenario design, meta-test |
| Persuasion principles | Supporting | Local, cites external study | Tone by skill type; ethics test |
| Instruction-file variant test | Example | Local | Variant test design (predictions only) |
| Flowchart conventions and renderer | Bundled | Local | Diagram style and rendering |
| Rust reliability skill and the reference digesting it | Example of a published scoring rubric | Local, scored judgment | Five-axis 100-point rubric, the above-80 floor, example scores, how to use a scored table |

Lineage: the plugin guide and the Codex creator both descend from the embedded original creator; where the three say the same thing it counts once. The five digests summarise sources also listed here and are not independent confirmation. The Anthropic guide is a local copy; the live document was not consulted.

## Evidence Boundary Notes

**Measured, by the source programme's own tools:** corpus counts (files, lines, headings, units, per-file and per-unit ranges, lane loads); duplicate counts found by the normalised check (525, 405, later 52 and 50); three files and 354 rows reopened; 699 targeted repairs preserved by resuming; 47 files and 5,703 rows at handoff; 99 files and 11,961 rows at completion; suite results at start and end.

**Reported by a source, not reproduced:** six iterations, more than ten excuses and full final compliance for one test-first skill; the agent that performed one review instead of two because of a description; a study cited by the persuasion file (Meincke and colleagues, 2025, about 28,000 conversations, compliance rising from 33 to 72 percent); word counts of sibling plugin skills; approximate token counts of the concise and verbose examples; a context cost attributed to force-loading links.

**Stated as targets or conventions, never measured:** every body-size limit; the description length preferences; 18 of 20 routing; the ten-minute reader target; the ten-file and three-subtask bound; scoreboard numbers; "testing saves time".

**Predictions, not results:** the expected outcomes of the instruction-file variant test.

**Executed while writing this file:** the mechanical gates on this skill folder and the programme gates on a small fixture.

**Not executed:** the installer and lister (network), the quantitative harness (not bundled), plugin trigger tests, any subagent run, any pressure campaign, the three programme scripts in their copied location, and metadata activation in any harness.

**Not consulted:** external URLs named by the digests (the Codex repository, the guide to repository instruction files, image-generation documentation) and the live Anthropic guide. They are leads.

**Distinctions to keep in any reference:** a recommendation is not an authorisation; a capability is not an observed outcome; authoring evidence is not runtime evidence; fixture behaviour is not provider behaviour; a checklist is not proof; a planned search is not a search result; two copies of one text are one source. Label each claim, not each section, and put the label in the sentence that carries the claim.

**Platform-dated facts likely to drift:** plugin skill discovery by directory scan, the `cc --plugin-dir` test flag, the three load levels and their budgets, and the availability of a reviewer agent (all described by the plugin guide and never run here; run one skill through the local plugin test to turn the description into an observation); field lists accepted by validators; personal skill directories; the curated and experimental repository layout; subagent notification fields; plugin packaging policy; trigger behaviour of current models.

## Future Refresh Search Queries

Run these against the installed runtime or the primary source. A good query targets one field or behaviour in the version in use; "skill best practices" is a bad query.

- Installed harness source: `allow_implicit_invocation` default and handling.
- Installed harness source: accepted `SKILL.md` front matter keys.
- Installed harness: `agents/openai.yaml` interface fields, icon formats and sizes.
- Installed harness: supported `dependencies.tools` types beyond `mcp`.
- Skills repository layout: curated, experimental and system directories.
- Personal skills directory for each runtime in use.
- Vendor authoring guide: current description length, body size and naming guidance.
- Plugin runtime: skill discovery rules and whether packaging is required.
- Subagent task notifications: token and duration fields.
- Trigger behaviour: under-triggering or over-triggering on the current model.
- Prompt-evaluation frameworks; agent instruction testing; pressure-testing model instructions; behavioural red-teaming of models.
- The persuasion study cited above: publication status and replication.
- CommonMark and GFM parsers that expose source positions.

Refresh when a field is disputed, a product is upgraded, a test fails unexpectedly, or a staleness review is due. Hazards: drift on a main branch, generated documentation, renamed fields, assumptions about icons, URL churn, and parser tolerance that is not documented. A query in this list is a plan. Record a result only after running it.
