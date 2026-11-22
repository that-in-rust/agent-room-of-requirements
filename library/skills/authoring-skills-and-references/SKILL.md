---
name: authoring-skills-and-references
description: Build, review, test and ship agent skills and long reference files, and run a multi-agent programme that produces many reference files at once. Use when asked to "create a skill", "write a SKILL.md", "improve this skill description", "why does my skill not trigger", "split this skill into references", "test or benchmark a skill", "add agents/openai.yaml", "install a skill from GitHub", or to plan a reference library with one owner per file, a task-queue CSV, ten-question section review packets, checkpoints and resume, and verifier scripts. Not for writing AGENTS.md or CLAUDE.md repository instructions, not for plugin manifests, hooks, commands or MCP server setup, and not for writing the subject matter of a reference (the language or framework content itself).
---

# Authoring Skills and References

## Purpose

A skill is a folder that another agent loads to do a job it could not do well from general knowledge. This skill covers the whole life of that folder: deciding whether it should exist, its layout and front matter, the description that makes it load, what goes in the body and what goes in reference files, how to test that it changes behaviour, how to add product metadata, and how to move it into a runtime. It also covers the method used to produce a 99-file reference library with four parallel agents: one owner per file, a task queue, a ten-question review of every section, save points and resume, and verification scripts.

Deeper material (full pattern catalogue, long tables, worked examples, failure modes, evidence limits) is in [reference.md](reference.md). Everything needed to do the work is on this page.

## When to use and when not to

Requests that should load this skill:

- "Turn the workflow we just did into a skill."
- "My skill never triggers. Fix the description."
- "This SKILL.md is 900 lines. Restructure it."
- "Is the new version of the skill better than the old one? Prove it."
- "We need 60 reference files written by several agents without them overwriting each other."

Requests that should not:

- "Write the AGENTS.md for this repository." Repository instructions are a different artifact with different loading rules.
- "Create a Claude Code plugin with hooks and a slash command." Plugin structure, manifests and hooks belong to plugin development; only the `skills/` part is covered here.
- "Write the Rust error-handling reference." The subject content belongs to that subject's skill; this skill supplies the shape and the review method only.

## Workflow for one skill

1. **Decide whether a skill is the right artifact.** Create one when the technique was not obvious, will be reused across projects, and applies broadly. Do not create one for a one-off fix, for a practice already well documented elsewhere, for project-specific conventions (those go in the repository instruction file), or for a constraint a script or validator can enforce (automate it and keep prose for judgment calls).
2. **Collect concrete uses.** Ask what the skill should enable, what a user would say that should trigger it, what the output looks like, and whether objective test cases make sense. Ask the most important question first and do not batch many questions in one message. If the request is "turn this into a skill", extract the tools used, the step order, the user's corrections and the input and output formats from the conversation before asking anything.
3. **Classify the skill.** Discipline (rules an agent has an incentive to break), technique (steps), pattern (a way of thinking), or reference (facts to look up). The type selects tone and test method below.
4. **Capture a baseline before writing rules.** Run the realistic task without the skill and record what the agent does, word for word. For a discipline skill this is mandatory. Write the skill against observed failures, not imagined ones.
5. **Plan bundled resources.** For each example use, ask what would be rewritten every time (make it a script), what would be rediscovered every time (make it a reference), and what is copied into output (make it an asset).
6. **Create the folder.** Use the bundled initializer or `mkdir`; see Commands.
7. **Write resources first, then `SKILL.md`.** Run every script you add. Write the description last, after the body is stable.
8. **Validate mechanically.** Front matter parses, name matches the folder, every referenced file exists, links resolve, no placeholders remain.
9. **Validate behaviour.** Run the test design that matches the type (see Evaluation). A clean validator run says nothing about behaviour.
10. **Add product metadata only if a harness consumes it** (`agents/openai.yaml`), then distribute.
11. **Iterate from use.** Use the skill on real work, notice where the agent struggles, change the skill, and retest. Stop when feedback is empty, the user is satisfied, or changes no longer help.

## Rules

### Layout and front matter

```
skill-name/
├── SKILL.md            required: YAML front matter + Markdown body
├── reference.md        or references/*.md, loaded on demand
├── scripts/            executable code, run without being read
├── assets/             files used in output (templates, icons, fonts)
├── examples/           complete runnable examples (plugin convention)
└── agents/openai.yaml  optional product metadata (OpenAI harnesses only)
```

- `name`: lowercase letters, digits and hyphens; no leading, trailing or doubled hyphen; at most 64 characters; identical to the folder name.
- `description`: at most 1024 characters, no angle brackets. It is the only text the agent sees before deciding to load the skill.
- Create only the directories that hold real files. Do not add `README.md`, `CHANGELOG.md`, installation guides or notes on how the skill was made.
- Use forward slashes in every path. Name files by content (`form_validation_rules.md`, not `doc2.md`).
- Link every bundled file from `SKILL.md` and say when to read or run it. A file that is not mentioned will not be used.
- Keep references one level deep: `SKILL.md` links to each file directly. Agents often preview nested files with a partial read and miss content.
- Give a long reference file a table of contents at the top, and give `SKILL.md` `grep` patterns for any reference above about 10,000 words.

### Description (the trigger)

- Write it in the third person. Never "I can help" or "You can use this".
- Name concrete triggers: phrases users say, symptoms, error messages, file types, tool and command names, synonyms.
- Describe the problem rather than one technology's symptom unless the skill is technology-specific.
- Never summarise the skill's workflow in the description. One source observed an agent follow a description that said "code review between tasks" and perform one review although the body required two; removing the summary fixed it.
- Do not stuff keywords. The sentence must still read as a sentence.
- Test queries must be substantive. Agents consult skills for work they cannot do in one step, so "read this PDF" may not trigger any skill however good its description.

Template used in this library:

```yaml
---
name: skill-name
description: <What it does, one clause>. Use when <phrases users say, file types, tools, symptoms>. Not for <nearest wrong uses>.
---
```

### Body

- Write for another agent that is already capable. For each paragraph ask whether the agent needs it and whether it earns its space. Keep schemas, local policy, exact commands and reasons that change execution. Drop tutorials on things any model knows.
- Use the imperative, verb first. Avoid "you should", "the agent should", "the user might".
- Match freedom to fragility: prose for tasks with many valid approaches; a parameterised template where one pattern is preferred; an exact command with "do not modify" where the operation is fragile or order matters.
- Give one default with one escape hatch, not a list of five options.
- Give one excellent, complete, runnable example in the most relevant language, with comments that say why. Not several languages, not fill-in-the-blank templates.
- Use one term per concept throughout.
- No time-sensitive statements. Put deprecated material under a collapsed "Old patterns" heading.
- For multi-step work, provide a checklist the agent copies and ticks off, and a validate, fix, repeat loop. For batch or destructive work, have the agent write a plan file, validate it with a script, then execute.
- Use a flowchart only for a non-obvious decision, a loop where an agent might stop early, or an A-versus-B choice. Use tables for reference material, code blocks for code, numbered lists for linear steps.
- Do not put content in both the body and a reference. Decide which one owns it.
- State whether each script is to be run or read. List required packages and how to install them. Use fully qualified MCP tool names (`ServerName:tool_name`).
- Scripts handle their own errors with specific messages and justify every constant.
- A skill must not contain anything that would surprise the user if its contents were described to them: no malware, exploit code or misleading purpose.

### Progressive disclosure

Three load levels: front matter is always in context; the body loads when the skill triggers; bundled files load or run only when needed. Keep in the body the core concepts, essential procedure, quick-reference tables, common cases and pointers. Move to references the detailed patterns, API documentation, migration guides, edge cases, troubleshooting and long walkthroughs. When a skill covers several variants (cloud providers, business domains), keep the workflow and the selection rule in the body and put one file per variant in references so only the relevant one is read.

When a skill outgrows its budget: body spills into references; references above about 10,000 words get `grep` hints; a domain that still does not fit becomes its own skill in its own directory. Splitting a skill splits its trigger surface, so each half needs its own description and its own trigger test. Two related skills may share one reference file by relative path; each is still discovered and triggered on its own.

### Where the sources disagree

Each row keeps both positions. The right-hand column says what selects one.

| Question | Position A | Position B | What decides |
| --- | --- | --- | --- |
| What the description contains | What the skill does plus when to use it (Anthropic guide, Codex creator, Claude creator) | Only when to use it, never what it does (superpowers) | Follow the target runtime or library convention for the capability clause. In every case leave the workflow out. If agents act on the description and skip the body, cut it back to triggers. |
| Description wording | "This skill should be used when the user asks to ..." with quoted phrases (plugin-dev) | "Use when ..." (superpowers, Anthropic examples); deliberately "pushy" wording (Claude creator) | The runtime's convention. Use pushy wording only where under-triggering was observed, and confirm with held-out trigger queries. |
| Body size | Under 500 lines (Codex, Anthropic, Claude creator) | 1,500 to 2,000 words ideal, under 3,000 acceptable, under 5,000 ceiling (plugin-dev); under 150, 200 or 500 words depending on how often the skill loads (superpowers) | How often the skill loads and which runtime reads it. Apply the strictest limit that applies. None of these limits was measured in this library. |
| "When to use" section in the body | Useless: the body loads after the decision (Codex, Claude creator) | Part of the standard body template, including when not to use (superpowers; this library's layout) | Triggers always go in the description. Keep a body section when the library layout asks for one; its job is boundary routing after load. |
| Tone | Explain why; capital-letter MUST and NEVER are a warning sign (Claude creator) | Authority language, "No exceptions", explicit loophole lists (superpowers) | Skill type: authority, commitment and social proof for discipline skills; moderate authority for technique; clarity only for reference. |
| Is testing mandatory | No skill or edit without a failing test first, no exceptions (superpowers) | Pure reference skills and skills with no rule to break need no pressure test (superpowers testing guide); the user may decline evaluation (Claude creator) | Whether a rule exists that an agent has an incentive to break. If yes, pressure-test. If no, retrieval and application checks still apply. Skipping rigor is the user's choice, never the agent's shortcut. When unsure, pilot one pressure scenario. |
| How to prompt a test subagent | Plain user-style task; the subagent must not know it is a test (Codex) | Framed scenario with forced A/B/C choice and "You have access to: [skill]" (superpowers) | Plain task for task quality and generalisation; forced choice for rule compliance under temptation. Neither is a quiz about the skill. |
| Front matter fields | Only `name` and `description` (Anthropic, superpowers, Codex prose) | `license`, `allowed-tools`, `metadata` accepted by the Codex validator; `version` used by plugin skills; `compatibility` in the Claude creator | The target runtime's validator. Run it. |
| Table of contents threshold | Reference files over 100 lines (Codex, Anthropic) | Over 300 lines (Claude creator) | Add one at 100 lines; it costs little. |
| Naming | Short verb-led phrase, namespaced by tool (Codex) | Gerund form such as `creating-skills` (Anthropic, superpowers) | Consistency inside one collection. |
| Creating and shipping | Init script, validate, install from GitHub (Codex); init script, validate and zip (ancestor creator) | `mkdir`, ships inside the plugin, no packaging (plugin-dev) | Target runtime. Dropping packaging also drops the validation it ran, so run the checklist by hand. |
| Blind comparison | Optional; human review usually suffices (Claude creator) | Required before claiming one version is better (evaluation digest) | Whether a comparative claim is being made. |
| Final reread grouping | Groups of five sections | Groups of no more than three | Section length and how much drift the first groups show. |
| Personal skill directory | `~/.claude/skills`, `~/.agents/skills` (superpowers) | `$CODEX_HOME/skills`, default `~/.codex/skills` (Codex) | Check the installed runtime. |

## Evaluation

Skill quality is a measured difference in behaviour, judged on runs the author did not steer.

| Skill type | Test with | Passes when |
| --- | --- | --- |
| Discipline | Baseline without the skill, then scenarios combining three or more pressures | The agent picks the right option under pressure, cites the skill, and admits the temptation |
| Technique | Application, variation and missing-information scenarios | The agent applies it to a new case |
| Pattern | Recognition, application and counter-example scenarios | The agent knows when and when not to apply it |
| Reference | Retrieval, application and gap checks | The agent finds the fact and uses it correctly |

**Red, green, refactor for a discipline skill.**

1. Red: run the scenario without the skill. Record the choice and every excuse verbatim.
2. Green: write the smallest skill that answers those excuses. Rerun the same scenario.
3. Refactor: for each new excuse make four edits: an explicit negation in the rule, a row in an excuse-and-reality table, a line in a red-flags list, and a symptom added to the description. Rerun.
4. If the agent still fails, ask: "You read the skill and chose C anyway. How could it have been written to make A the only acceptable answer?" The answer is one of: it was clear and ignored (add a foundational principle such as "violating the letter is violating the spirit"), it should have said X (add X verbatim), or section Y was not seen (move it up).
5. Finish one skill's campaign before starting the next. Never batch.

Pressure scenario template (pressures: time, sunk cost, authority, economic, exhaustion, social, pragmatic):

```markdown
Treat this as real work, not a quiz. Decide and act; do not ask what I would prefer.

You have spent the afternoon on a 180-line importer in /tmp/billing-import/importer.py.
It runs, and you checked three invoices by hand. It is Friday 17:40, friends are waiting,
and the demo is Monday 09:00. You have just noticed that you skipped <rule>.

A) <comply at real cost>
B) <violate now, repair later>
C) <partial compliance>

Choose A, B, or C.
```

Run the scenario once with no skill for the baseline, and once with a line that names the skill under test as available.

**Forward-testing task quality.** Launch a fresh subagent with a prompt a user would write, `Use $skill-x at /path/to/skill-x to solve problem y`, never "review this skill and pretend". Pass raw artifacts, not your diagnosis, expected answer or intended fix. Use a new thread per pass and delete artifacts left on disk between passes. If the test only passes when context leaks, fix the skill or the setup. Ask the user first when a test would run long, need approvals, or touch production.

**Quantitative comparison.** For each of two or three realistic prompts, launch a with-skill run and a baseline run in the same turn. The baseline is no skill for a new skill and a snapshot taken before editing for an existing one. Save token and duration figures the moment each run reports them; they are not stored elsewhere. Write assertions that are objectively checkable and that a baseline can fail; an assertion that passes in both configurations measures nothing. Grade with cited evidence, compare blind when claiming one version is better, and show outputs to the human before forming your own view. Keep the roles' knowledge apart: a run must not know it is a test, the grader accepts no claim without quoted evidence, and the comparator must not know which version produced which output. The author judging alone is the failure state; where the author must grade inline, the evidence rule still applies and the record says the check was not independent. After each change rerun everything into a new iteration directory; never reuse stale runs. Judge subjective skills (style, design) by human review and say that assertions were waived.

**Trigger evaluation.** Write about twenty realistic queries, half that should trigger and half near misses that share keywords but need something else. Include detail, typos and casual phrasing. Split 60/40, tune on the larger part, choose the description by its score on the held-out part, and report before and after.

**Without subagents.** Run the cases yourself one at a time, skip baselines and benchmarks, ask the human for feedback, and state that the check was not independent.

## Product metadata: `agents/openai.yaml`

Optional, read by the harness and not by the agent. It carries interface text, MCP dependencies and the implicit-invocation policy. Procedure stays in `SKILL.md`.

```yaml
interface:
  display_name: "Release Notes"
  short_description: "Draft release notes from merged changes"
  default_prompt: "Use $release-notes to draft notes for the latest tag."
policy:
  allow_implicit_invocation: false
```

- Include only fields the harness needs. Omit icons and dependencies that do not exist; never invent placeholders or copy another skill's dependency block.
- Quote every string value; leave keys unquoted.
- `short_description` is 25 to 64 characters. `default_prompt` is about one sentence and contains the exact `$skill-name`.
- Icon paths are relative to the skill folder, normally `./assets/...`, and must resolve.
- `dependencies.tools[].type` supports only `mcp`.
- `allow_implicit_invocation` defaults to true. Set false for destructive or sensitive skills; they remain callable as `$skill-name`.
- Parsing proves syntax, not activation. Record explicit and implicit activation only when you observed them. Regenerate the file when `SKILL.md` changes.

## Distribution

- **Plugin skills** ship inside the plugin under `skills/<name>/`. The plugin runtime finds a skill by scanning `skills/` for any subdirectory that contains a `SKILL.md`. There is no registration or packaging step, so the `skills/` directory is the unit that absorbs growth: a new domain is a new subdirectory. Test with `cc --plugin-dir /path/to/plugin` and ask questions that should trigger the skill. Discovery, the test flag and the load budgets are platform facts taken from the plugin guide; recheck them against the installed runtime before relying on them.
- **Codex skills** install into `$CODEX_HOME/skills/<name>` with the bundled installer.

Installer conduct:

1. A request with no specifics gets a numbered list with installed entries marked, followed by "Which ones would you like installed?" Do not answer with a clarifying question.
2. A skill name installs from the curated list; a repository path or URL installs from that location. Label experimental sources as experimental.
3. The scripts need network access; ask for sandbox escalation first.
4. Fetch order is direct download, then git over HTTPS, then git over SSH. Retry only by moving to the next method.
5. An existing destination aborts the install. Stop and ask. Never delete a directory unasked. Preinstalled system skills need no install; explain that, and overwrite only if the user insists.
6. Never put credentials in a URL. Use existing git credentials or `GITHUB_TOKEN` / `GH_TOKEN`.
7. After installing say: "Restart Codex to pick up new skills."
8. With several paths in one run, a failure on a later path leaves earlier ones installed. Report exactly which directories now exist.

Only one of these rules is enforced by code: the install script aborts when the destination exists. The restart notice, the experimental label, the explanation for a preinstalled skill, asking which skills to install, and keeping credentials out of URLs are the agent's obligations, and nothing checks them. Unchecked rules erode without anyone noticing, and the damage does not announce itself: overwritten or mislabelled state can look as if it works.

## Producing many reference files with several agents

Use this when a library needs tens of files of the same shape. Deterministic tools inventory, hash, verify and synchronise status. They never write prose; every section is written by an agent exercising judgment.

1. **Freeze the corpus.** Inventory every source file, assign each to exactly one output theme, and write the manifest before anyone drafts. Every candidate path appears exactly once in the inventory. Repeated copies of one file (monthly snapshots and the current copy) stay listed as separate paths and are not removed from the inventory; they go in the same theme row when they serve the same agent use case, and they count as one source of evidence.
2. **Assign one permanent owner per file.** Split files into disjoint lanes with an ordered manifest per lane. Two agents never write the same path. Only the coordinator edits the shared queue; the coordinator does not write specialist prose.
3. **Build the task queue.** Parse each file into atomic units (heading, paragraph, list item, table row, code block) with source line ranges, a stable identifier, a content hash and a status. Every source line belongs to exactly one unit. Before the first edit, check each unit's hash against the frozen file; a mismatch blocks the whole file until the snapshot is deliberately refreshed.
4. **Review every section with ten questions before changing it.** The owner reads the whole file first, then works through sections in order.
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

   Each answer has six fields: `current_section_observation`, `supporting_reason`, `counterargument_or_limit`, `assumptions_and_boundaries`, `revision_decision`, `additional_insight_to_add`.
5. **Save in a fixed order.** Packet for the section first, rewritten section second, a focused check third. Write a journal entry at least every three sections and at every phase change.
6. **Resume, never regenerate.** After an interruption the same owner continues from the last saved section. Valid saved work is kept.
7. **Reread before accepting.** Reread the finished file in bounded groups of sections and fix what the reread finds. The packet is draft evidence until the reread passes.
8. **Verify, then mark complete.** Run the per-file verifier. Only a passing file has its queue rows marked complete, by the coordinator, through an atomic write.
9. **Reopen narrowly.** When a later gate finds a defect, reopen only the affected rows and return them to the same owner.
10. **Synthesise last.** No combined or summary document starts until every file and every queue row is complete.

The uniqueness gate matters. Checking that packet values differ as exact strings is not enough: a section or question prefix makes copied generic prose look unique. Strip prefixes, collapse whitespace, fold case, then compare. In the source programme this normalised check found 525 duplicated values in the first pilot and 405 in a later batch, and reopened three accepted files (354 rows).

Label every claim by its evidence: taken from the local corpus, taken from an external source that was actually opened, or inferred from both. A URL that was not opened is a lead, not a fact. A planned test is not a result. A checklist is not proof of runtime behaviour.

## Commands

Run from this skill's folder. Python scripts need `python3`; three need PyYAML (`pip install pyyaml`).

```bash
# Create a skill folder (Codex layout; writes SKILL.md template and agents/openai.yaml)
python3 scripts/init_skill.py my-skill --path "${CODEX_HOME:-$HOME/.codex}/skills" --resources scripts,references
# Create a plugin skill folder by hand
mkdir -p plugin-name/skills/skill-name/{references,examples,scripts} && touch plugin-name/skills/skill-name/SKILL.md
# Validate front matter and naming
python3 scripts/quick_validate.py path/to/skill-folder
# Regenerate interface metadata
python3 scripts/generate_openai_yaml.py path/to/skill-folder --interface display_name="Release Notes" --interface short_description="Draft release notes from merged changes" --interface default_prompt='Use $release-notes to draft notes for the latest tag.'
# List and install (network required)
python3 scripts/list-skills.py
python3 scripts/list-skills.py --path skills/.experimental --format json
python3 scripts/install-skill-from-github.py --repo openai/skills --path skills/.curated/<skill-name>
python3 scripts/install-skill-from-github.py --url https://github.com/<owner>/<repo>/tree/<ref>/<path> --method auto
# Render the dot flowcharts in a skill's SKILL.md to SVG (needs graphviz)
node scripts/render-graphs.js path/to/skill-folder --combine
# Size checks
wc -l path/to/skill-folder/SKILL.md && wc -w path/to/skill-folder/SKILL.md
```

Checked when this page was written: the initializer, validator and metadata generator ran against a scratch folder, and the lister, installer and renderer printed their usage. Not run: anything needing the network, graphviz, a plugin runtime or a Codex harness.

## Bundled files

| File | Use | Notes |
| --- | --- | --- |
| [scripts/init_skill.py](scripts/init_skill.py) | Run | Normalises the name, refuses an existing folder, writes a template with TODO markers. `--examples` needs `--resources`. Imports `generate_openai_yaml.py` from the same folder. A fresh template fails `quick_validate.py` until the bracketed description placeholder is replaced. |
| [scripts/generate_openai_yaml.py](scripts/generate_openai_yaml.py) | Run | Writes only the `interface` block and overwrites the file. Add `dependencies` and `policy` by hand. Enforces 25 to 64 characters. |
| [scripts/quick_validate.py](scripts/quick_validate.py) | Run | Checks front matter keys, name form and length, description length and angle brackets. Rejects keys outside `name`, `description`, `license`, `allowed-tools`, `metadata`. |
| [scripts/list-skills.py](scripts/list-skills.py) | Run | Lists a GitHub path and marks names already present under `$CODEX_HOME/skills`. |
| [scripts/install-skill-from-github.py](scripts/install-skill-from-github.py) | Run | Options `--repo`, `--url`, `--path`, `--ref`, `--dest`, `--name` (single path only), `--method auto\|download\|git`. Aborts if the destination exists. |
| [scripts/github_utils.py](scripts/github_utils.py) | Imported | Shared request helper; reads `GITHUB_TOKEN` or `GH_TOKEN`. |
| [scripts/render-graphs.js](scripts/render-graphs.js) | Run | Extracts `dot` blocks from a skill's `SKILL.md` into a `diagrams/` folder. |
| [scripts/verify_idiomatic_reference_file.py](scripts/verify_idiomatic_reference_file.py) | Read, then adapt | Per-file verifier from the reference programme: headings preserved, every section expanded, no placeholders, packet has 26 sections, 10 questions each, 6 non-empty fields, exact and normalised uniqueness. |
| [scripts/test_idiomatic_reference_evolution.py](scripts/test_idiomatic_reference_evolution.py) | Read, then adapt | Corpus test suite: inventory counts, unique ownership, lane manifests, packet structure, queue completeness, placeholder ban. |
| [scripts/update_idiomatic_evolution_queue.py](scripts/update_idiomatic_evolution_queue.py) | Read, then adapt | Queue updater: verifies before marking complete, writes through a temporary file with `fsync` then replace, `--reopen` returns a path to pending. |
| [assets/graphviz-conventions.dot](assets/graphviz-conventions.dot) | Read | Flowchart style: diamond for a question, box for an action, plain text for a literal command, ellipse for a state, red octagon for a stop, double circle for start and end. |
| [assets/license.txt](assets/license.txt) | Keep | Apache 2.0 text shipped with the Codex skill-creator material. |
| `assets/skill-installer-small.svg`, `assets/skill-installer.png` | Asset | Installer icons, usable as `icon_small` and `icon_large` examples. |

The three programme scripts are copied unchanged. They compute the repository root from their original location and import each other as `tests.<module>`, so they do not run from `scripts/` as they stand. To reuse them, edit the path constants at the top (`REPO_ROOT`, working directory, queue path, packet directory), the import lines, the section count and the file-name pattern for the new corpus.

Not bundled: the Claude skill-creator evaluation harness (`aggregate_benchmark`, `generate_review.py`, `run_loop`, `package_skill`, the grader, comparator and analyzer prompts, and the JSON schemas). The evaluation rules above hold without it; its exact commands are listed in [reference.md](reference.md) for use where that plugin is installed.

## Output contract

A finished skill delivers:

- A folder named exactly as the skill, with `SKILL.md` whose front matter parses and whose description names triggers and nearest wrong uses.
- A body that works when it is the only file loaded.
- Every bundled file linked from the body with a run-or-read instruction; every script run at least once.
- A test record: the skill type, the baseline behaviour, the scenarios or prompts used, what changed, and the result. If a test was skipped, the record says which and why.
- For `agents/openai.yaml`: the fields chosen and omitted, the parse result, and activation results labelled observed or not run.

A finished reference programme delivers the manifest, the queue with every row complete, one packet per file, the journal, verifier output for every file, and the corpus test result.

## Quality gates

```bash
S=path/to/skill-folder
# 1. Front matter parses and the name equals the folder name
python3 - "$S" <<'EOF'
import re, sys, pathlib, yaml
d = pathlib.Path(sys.argv[1]); t = (d / "SKILL.md").read_text()
fm = yaml.safe_load(re.match(r"^---\n(.*?)\n---", t, re.S).group(1))
assert fm["name"] == d.name, (fm["name"], d.name)
assert len(fm["description"]) <= 1024 and "Use when" in fm["description"]
print("front matter ok", len(fm["description"]), "chars")
EOF
# 2. Every relative link resolves
python3 - "$S" <<'EOF'
import re, sys, pathlib
d = pathlib.Path(sys.argv[1]); bad = []
for f in d.glob("*.md"):
    text = re.sub(r"```.*?```", "", f.read_text(), flags=re.S)
    for link in re.findall(r"\]\(([^)#\s]+)", text):
        if "://" not in link and not (f.parent / link).exists():
            bad.append((f.name, link))
print(bad or "links ok"); sys.exit(1 if bad else 0)
EOF
# 3. No placeholders left (review each hit; a mention of the word is not a placeholder)
grep -n -E "\b(TODO|TBD|FIXME)\b" "$S"/*.md
# 4. Size
wc -l "$S/SKILL.md"; wc -w "$S/SKILL.md"
# 5. Metadata, if present
python3 -c "import yaml,sys; d=yaml.safe_load(open(sys.argv[1])); s=d['interface']['short_description']; assert 25<=len(s)<=64; print('yaml ok')" "$S/agents/openai.yaml"
```

Gates 1 to 5 are mechanical. The behavioural gate is the test record in the output contract.

## Anti-patterns

| Anti-pattern | Why it fails | Do instead |
| --- | --- | --- |
| Vague description ("Helps with documents") | The skill never loads | Name phrases, files, tools and symptoms |
| Workflow summarised in the description | The agent follows the summary and skips the body | Triggers only |
| Everything in one very long `SKILL.md` | Every load pays for detail it does not need | Core in the body, detail in references |
| Same content in body and reference | The two drift apart | One owner per fact |
| Bundled file never mentioned | It is never read or run | Link it with a when-to-use line |
| Narrative ("on that day we found ...") | Not reusable | State the technique |
| Second-person or tutorial prose | Longer and less direct | Imperative, verb first |
| Capital-letter rules added after one failure | Overfits to one case and makes the skill rigid | Explain the reason; reserve hard rules for discipline skills |
| Writing rules with no baseline | Addresses failures that do not occur | Run without the skill first |
| Single-pressure or quiz-style test | The agent recites the skill | Three or more pressures and a forced choice |
| Generic counter ("don't cheat") | The specific loophole stays open | Quote the excuse and negate it |
| Author grades own runs | No independence | Fresh subagent, blind comparison, cited evidence |
| All assertions pass in both configurations | The benchmark cannot tell the versions apart | Write assertions a baseline can fail |
| Hand-written grading JSON with guessed field names | The viewer shows empty results | Use the exact fields `text`, `passed`, `evidence` |
| Instructions inside `agents/openai.yaml` | The agent never reads that file | Put procedure in `SKILL.md` |
| Overwriting an installed skill | Destroys the user's state | Stop and ask |
| Two agents editing one file | Lost work, unreviewable history | One permanent owner per file |
| Marking a queue row complete before verification | The queue stops meaning anything | Verify, then update |
| Regenerating after an interruption | Throws away valid work | Resume the same owner at the saved section |
| Exact-string uniqueness only | Prefixed copies pass | Normalise, then compare |
| Reporting an unopened URL or a planned test as a finding | Unsupported claim | Label it as a lead or as not run |

## Self-check before finishing

- [ ] The description names what users say, the files and tools involved, and the nearest wrong uses, and contains no workflow.
- [ ] The body works alone; a reader who never opens another file can do the job.
- [ ] Each fact lives in one place; every bundled file is linked with a run-or-read instruction.
- [ ] Every command on the page was run or is marked as not run.
- [ ] The skill type is stated and the matching test was run, or the waiver and who chose it is recorded.
- [ ] Baseline behaviour was captured before rules were written.
- [ ] Every number is either measured here, attributed to its source, or removed.
- [ ] Where sources disagreed, both positions and the selector are written down.
- [ ] For a multi-file programme: one owner per file, packet saved before section, journal current, verifier passed before the queue changed.
