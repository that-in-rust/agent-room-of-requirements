---
name: claude-plugin-development
description: Design, build, test, and package Claude Code plugins - directory layout and `.claude-plugin/plugin.json` manifest, slash commands, hooks (plugin `hooks/hooks.json` and hookify rule files), MCP server bundling (`.mcp.json`), per-project plugin settings (`.claude/<plugin>.local.md`), plugin-shipped agent files (`agents/*.md` frontmatter and triggering examples) and plugin-shipped skills (`skills/<name>/SKILL.md` placement and trigger description), teaching/example plugins, Codex plugin scaffolding (`.codex-plugin/plugin.json`, marketplace entries), and evidence-led Claude Code setup recommendations for a repository. Use when the task says "create a plugin", "add a slash command", "write a hook", "add an agent to the plugin", "add a skill to the plugin", "block edits to .env", "bundle an MCP server", "plugin settings file", "scaffold a Codex plugin", "which hooks/skills/subagents/MCP servers should this repo use", or when editing files such as plugin.json, hooks.json, .mcp.json, commands/*.md, hookify.*.local.md, marketplace.json. Not for authoring or restructuring the content of a skill or reference file (use authoring-skills-and-references), not for subagent delegation strategy, context budgeting, or multi-agent orchestration (use agent-context-and-orchestration), not for implementing an MCP server's own protocol logic, and not for general shell scripting or CI pipelines unrelated to a plugin.
---

# Claude Plugin Development

## Purpose

This skill turns a wish ("Claude should always do X", "our team needs command Y", "connect Claude to service Z") into the smallest Claude Code extension that delivers it, with a contract, tests, and a removal path. It covers Claude Code plugins end to end, the neighbouring Codex plugin scaffold, and the read-only repository survey that decides whether anything should be built at all.

## When to use and when not to use

Use it for requests like these:

1. "Create a plugin that bundles our review command and a formatter hook." (structure, manifest, command, hook)
2. "Write a hook that asks before any `rm -rf`." (hookify rule or plugin hook)
3. "Add our internal API to the plugin as an MCP server and let `/sync` call two of its tools." (MCP bundling, tool allowlist)
4. "The hook should be switchable per project without editing hooks.json." (plugin settings file)
5. "Look at this repo and tell me which hooks, skills, subagents, plugins, and MCP servers are worth setting up." (setup recommendation)
6. "Scaffold a Codex plugin with a marketplace entry." (Codex creator)

Do not use it for:

1. Writing or restructuring the content of a `SKILL.md` or reference document. This skill covers where a skill sits inside a plugin, what its bundled directories are for, and how its description triggers.
2. Deciding how to delegate across subagents, budget their context, or coordinate several of them. This skill covers the agent file a plugin ships (frontmatter, triggering description, system-prompt skeleton, validation) and when a subagent is the right surface.
3. Implementing the server side of MCP (JSON-RPC handlers, tool schemas). This skill covers bundling, transport choice, authentication wiring, and tool consumption.

## Version and evidence boundary (read before trusting any field name)

Every field name, event name, output shape, default timeout, and CLI flag below comes from snapshots of the Claude Code plugin-dev, hookify, example-plugin and claude-code-setup plugins and of the Codex plugin-creator skill. None has been verified against a live host. Later written analyses of those snapshots (one per sub-topic, plus an analysis of a newer Codex creator) supplied the risk, lifecycle, and evidence rules; where the text says "the analysis", it means one of those. Treat every field and flag as "documented at snapshot time", and before shipping:

- check the current hook, MCP, and plugin documentation for the installed version (`https://docs.claude.com/en/docs/claude-code/hooks`, `https://docs.claude.com/en/docs/claude-code/mcp`, `https://modelcontextprotocol.io/`);
- run the gates in "Quality gates" against the real host.

Four evidence steps are distinct and none implies the next: documented is not parsed; parsed is not discovered; discovered is not safely activated; executed is not correct. Byte-identical copies of one document count as one witness, not several.

Where the snapshots disagree, both positions are kept below under the label **Conflict**, with the condition that selects between them. Numbers are labelled *source-local* (stated by a snapshot, never measured here), *illustrative*, or *proposed*. The only observations made by actually running something are those marked **Observed** in "Bundled scripts and assets".

## Workflow

1. **State the outcome and the prohibitions.** One sentence for what should be true afterwards, one for what must never happen (for example: "no writes outside the repo, no network").
2. **Survey before building.** Read-only inventory of the repository and existing Claude configuration (commands in "Claude Code setup recommendations"). File or dependency presence is a lead, not proof of need.
3. **Pick the least powerful surface that delivers the outcome** using the table in "Choosing the surface". "Manual command", "documentation", and "no change" are valid results.
4. **Write the contract first.** For a command: the command contract. For a hook: the lifecycle row. For an MCP server: the boundary map row. For settings: the schema table. For an agent or skill: the triggering description with one request that must select it and one that must not. For a plugin: the capability trace. Templates are under "Output contract".
5. **Build the smallest tree.** Manifest plus only the component directories that are used. Use `${CLAUDE_PLUGIN_ROOT}` for every plugin-internal path.
6. **Validate statically.** JSON parses, names match the pattern, paths obey the path policy, frontmatter parses, no secrets, no absolute paths.
7. **Test components in isolation.** Pipe fixture JSON into hook scripts; run settings parsers against sample files; check MCP config shape.
8. **Load in the real host.** Start a new Claude Code session (hooks and MCP config load at session start), then check `/help`, `/hooks`, `/mcp`, and run `claude --debug`.
9. **Exercise positive and negative cases.** Valid input, missing input, invalid input, a neighbouring request that must not trigger, a denied tool, a cancellation, a repeat run.
10. **Exercise the lifecycle** if the plugin is distributed: clean install from the packaged artifact, update, disable, remove, and check for residue.
11. **Record evidence and status.** Which gates ran, what was observed, what is still unverified, who owns the thing, and what triggers its removal.
12. **Start soft, promote on evidence.** New enforcement starts at warn or ask. Promote to block only after reviewing false positives.

## Choosing the surface

| Need | Surface | Minimum evidence before choosing it | Main cost |
|---|---|---|---|
| Nothing repeats, or existing commands/docs already cover it | No change / documentation / a manual shell command | Survey shows no repeated friction | Docs do not enforce; manual commands are easy to forget |
| A user explicitly triggers a bounded, repeatable workflow with known inputs | Slash command | The workflow has run by hand more than once and its inputs are nameable | Not automatic; needs discovery via `/help` |
| Something must happen or be checked automatically at a lifecycle moment | Hook | A deterministic or clearly stated rule tied to one event | Can block, loop, or slow every matching tool call |
| A personal or single-project guard, tried cheaply | Hookify rule file | One concrete incident and a regex that captures it | Regex only; user-local; needs the hookify plugin |
| Reusable knowledge, templates, or scripts the model should pull in when relevant | Skill | Repeated prompts or expertise with clear trigger wording | Invocation and side effects are less visible |
| Independent specialist analysis, parallel review, or an isolated context | Subagent | A separable task with its own tool needs | Fan-in and evaluation cost |
| Structured access to an external service | MCP server | A named service, an owner, credential scope, and a read-only probe | Adds a data and service boundary |
| Persistent per-project behaviour switches or state | Plugin settings file | Fields, defaults, and one writer per field are known | Hand-edited YAML; no locking |
| Several of the above must be installed, versioned, and maintained together | Plugin | Two or more coherent components, or team-wide distribution | Bundle and update dependency |

Three questions settle most hook decisions: which lifecycle moment (gives the event), deterministic or judgment (gives command or prompt hook), personal or distributable (gives hookify or plugin hook).

A custom structure must buy ownership, permission separation, or discoverability. If it only buys tidiness, keep the defaults. Split a plugin when its parts have independent release cycles or permission domains (for example a security-enforcement plugin and a documentation plugin), and avoid a single large plugin that auto-starts unrelated servers and hooks.

## Plugin structure and manifest

### Layout

```
my-plugin/
├── .claude-plugin/
│   └── plugin.json        # manifest: the only file that belongs in this directory
├── commands/              # *.md, one per slash command
├── agents/                # *.md, one per subagent
├── skills/
│   └── <skill-name>/
│       └── SKILL.md       # must be named exactly SKILL.md
├── hooks/
│   └── hooks.json
├── .mcp.json
├── scripts/               # hook scripts, helpers
└── README.md
```

Rules:

1. The manifest lives at `.claude-plugin/plugin.json`. Component directories live at the plugin root, never inside `.claude-plugin/`.
2. Create only the directories that are used. A minimal plugin is a manifest plus one component, for example `skills/<name>/SKILL.md`.
3. Use kebab-case for directories and files. Avoid catch-all names such as `utils/`, `misc.md`, `temp.sh`.
4. Commands: every `.md` in `commands/` loads; the file name is the command name (`code-review.md` gives `/code-review`). Skills: one directory per skill, optional `scripts/`, `references/`, `examples/`, `assets/`. Agents: `.md` files with frontmatter.
5. Keep related component names consistent (`test-runner` command, `test-runner-agent`). Commands are two or three words (`review-pr`, `run-ci`), agents describe a role, skills name a topic.
6. Put a README at the plugin root covering installation, usage, required environment variables, hook behaviour and how to switch it off, and dependencies with versions.

### Manifest

Minimal:

```json
{ "name": "my-plugin" }
```

Recommended for anything shared:

```json
{
  "name": "my-plugin",
  "version": "0.1.0",
  "description": "One sentence on what the plugin does.",
  "author": { "name": "Team Name", "email": "team@example.com", "url": "https://example.com" },
  "homepage": "https://example.com/docs",
  "repository": "https://example.com/repo",
  "license": "MIT",
  "keywords": ["review", "formatting"]
}
```

1. `name` is the only required field. Pattern: `^[a-z][a-z0-9]*(-[a-z0-9]+)*$` (lower-case letters, digits, hyphens; starts with a letter; ends with a letter or digit). It must be unique among installed plugins and is used for identification, conflict detection, and command labels. Rejected examples: `API Tester`, `code_review`, `-git-workflow`, `test-`.
2. `version` is semantic: major for breaking changes, minor for compatible features, patch for fixes. One snapshot states a default of `0.1.0` when absent (source-local). Bump on every release; stale version metadata is a known trap.
3. Optional component path fields: `commands`, `agents` (string or array), `hooks`, `mcpServers` (path or inline object).
4. Path policy for those fields: relative to the plugin root, start with `./`, never `../`, never absolute, forward slashes only, no backslashes.
5. Custom paths **supplement** default discovery; they do not replace it. Defaults are scanned first (`./commands/`, `./agents/`, `./skills/`, `./hooks/hooks.json`, `./.mcp.json`), then manifest paths; everything found is registered, nothing is overwritten, and a name conflict is an error. So a custom path that points at a default directory registers things twice.
6. The manifest is a capability index and a trust boundary: every declaration widens what the host loads, starts, or exposes. Declare nothing that the package does not contain, and contain nothing privileged that is not declared.
7. Load-time checks named by the snapshot: JSON syntax and field types, `name` present and valid, semantic `version` when present, `./` paths, well-formed URLs, referenced paths exist, hook and MCP configuration valid, no circular dependencies. Keep a changelog, a licence file at the plugin root when `license` is set, and current URLs; document why any non-default layout is used.
8. Valid JSON is not a valid manifest. Check field semantics, that every referenced path exists in the *packaged* artifact (source-tree tests hide missing files), and that the observed component inventory equals the expected one. Unexpected discovery is as serious as missing discovery.

### `${CLAUDE_PLUGIN_ROOT}`

The install location differs by install method, operating system, and user. Use `${CLAUDE_PLUGIN_ROOT}` in hook commands, MCP server commands and arguments, script references, and `@` file references in commands. Inside executed scripts it is an environment variable: `source "${CLAUDE_PLUGIN_ROOT}/lib/common.sh"`.

Never use a hardcoded absolute path, a `~/` shortcut, or a working-directory-relative path such as `./scripts/x.sh` for plugin files: the plugin root is not the user's working directory. In a command, `@./templates/foo.md` resolves against the user's project, not the plugin.

**Conflict (mutable data under the plugin root).** One snapshot example writes a cache under `${CLAUDE_PLUGIN_ROOT}/cache/`. The packaging guidance says the plugin root may be replaced on update or be read-only, and that later manifest repair does not clean up earlier effects. Select by lifetime: disposable, re-creatable cache that the plugin itself cleans may live under the plugin root after you have confirmed the root is writable on the target install method; anything a user would miss (state, settings, results) goes under the project's `.claude/` directory.

### Discovery, activation, and lifecycle

Loader sequence: parse, resolve, discover, register, initialize, activate, deactivate, remove. At host start the enabled plugins are scanned (manifest read), components are found in default and custom paths, frontmatter and configuration are parsed, components are registered, then MCP servers start and hooks register. Registration happens at initialisation, not continuously: a new session is the reload point for plugin configuration.

Activation differs by component: a command runs when the user types it; an agent is selected when a task matches its description; a skill loads when the task context matches its description; a hook is called when its event fires and its matcher matches; an MCP tool call is routed to the owning server.

Trace every capability through this chain and name the evidence at each link:

`capability -> component -> declaration -> packaged path -> discovery -> activation -> portable resource -> disable -> update migration -> removal cleanup`

### Organising a growing plugin

Start flat and reorganise when there is pressure. Options: commands flat, categorised in subdirectories, or hierarchical; agents by role, capability, or workflow; skills by topic, tool, or workflow; hooks as one `hooks.json`, split by event, or split by purpose with grouped scripts (generate a combined hook file at build time if the host needs one); scripts flat, categorised, or by language. Shared code goes in a `lib/` directory sourced through `${CLAUDE_PLUGIN_ROOT}`. A layered layout or a plugin-within-plugin (extra manifest paths for optional feature families) is for very large, multi-owner plugins; one snapshot's threshold of "100+ files" is a source-local heuristic. Categorised commands are acceptable only when packaged, conflict-tested, and documented.

## Slash commands

A slash command is a Markdown file whose body becomes Claude's instructions when the user invokes it. Write directives **to Claude** ("Review the diff below for ..."), never a description for the user ("This command will ...").

### Locations

| Scope | Directory | Label in `/help` |
|---|---|---|
| Project | `.claude/commands/` | `(project)` |
| Personal | `~/.claude/commands/` | `(user)` |
| Plugin | `<plugin>/commands/` | `(plugin:<plugin-name>)`; with a subdirectory, `(plugin:<plugin-name>:<namespace>)` |

A subdirectory adds a namespace label; it does not change the command name. Plugin commands are discovered at plugin load with no registration step.

**Conflict (when to add namespaces).** One snapshot says flat for roughly 5 to 15 commands and subdirectories from 15 commands up (stated for project commands); another says to namespace a plugin once it has 5 or more commands. Both are source-local heuristics. Select by collision risk: a distributed plugin whose commands could collide with other plugins namespaces or prefixes early (5+); a private project set stays flat longer (15+).

### Frontmatter

All fields are optional; start minimal and add only what the command needs.

| Field | Meaning | Guidance |
|---|---|---|
| `description` | Shown in `/help`; defaults to the first line of the body | Start with a verb; specific; under about 60 characters (source-local); not one word, not a paragraph, not "This command ..." |
| `allowed-tools` | Tools the command may use; string, comma list, or YAML array; default inherits from the conversation | As restrictive as works: `Read, Grep` for read-only; filtered Bash such as `Bash(git:*)` or narrower `Bash(git status:*)`. One snapshot calls bare `Bash` a common error and `"*"` not recommended. Document why if broad |
| `model` | `sonnet`, `opus`, or `haiku` at snapshot time; default inherits | Omit unless needed. Haiku for formulaic, frequent commands; opus for architecture or critical analysis |
| `argument-hint` | Autocomplete hint | One bracket per argument, descriptive names, same order as the positionals, mark optional ones: `[pr-number] [priority]` |
| `disable-model-invocation` | `true` means only a human can invoke it | Use for destructive, irreversible, or approval-gated commands and interactive wizards; add a comment saying why |

### Dynamic content

- `$ARGUMENTS` is the whole argument string. `$1`, `$2`, `$3` are positional. In one snapshot example the last positional soaks up the rest (`/deploy api staging --force --skip-tests` puts both flags in `$3`); verify on the target version.
- `@path` inlines a file. `@$1` inlines a file chosen by argument. `@${CLAUDE_PLUGIN_ROOT}/templates/report.md` inlines a plugin resource.
- An exclamation mark followed by a backticked shell command runs before the prompt is processed and its output replaces the placeholder. It requires Bash in `allowed-tools`. Keep it fast and read-only, and make failure visible: `npm run build 2>&1 || echo "BUILD_FAILED"`.
- Unverified constructs seen in snapshot examples: `$IF($1, ..., ...)` and shell-style defaults such as `${1:-staging}` in prompt text. Prefer plain language: "If `$1` is empty, use `staging` and say so."

### Rules

1. One command, one responsibility. Name it verb-noun (`review-pr`, `fix-issue`); avoid `test`, `run`, `do-stuff`; consider a plugin prefix for uniqueness.
2. Known values are arguments. Context-dependent choices are questions. Deterministic mechanics belong in a tested script the command calls. High-risk actions need an explicit confirmation.
3. Validate early and say how to fix it. Enum: inline `echo "$1" | grep -E "^(dev|staging|prod)$" || echo INVALID`. File: `test -f "$1" && echo EXISTS || echo MISSING` (with `Bash(test:*)` allowed). Plugin resource: `test -x "${CLAUDE_PLUGIN_ROOT}/bin/tool" && echo OK || echo MISSING`. Then instruct Claude what to do for each sentinel.
4. When arguments are missing, print usage or apply a stated default; never guess silently.
5. Never broaden tool access after a denial. Report the denial and stop or offer the narrower path.
6. As effects and state grow, make the Markdown thinner and the deterministic implementation and recovery more explicit. The ladder: plain prompt, positional arguments, guided questions, script-backed, stateful workflow.
7. Integration: to use an agent, name it in the body (it must exist in the plugin's `agents/`); to use a skill, mention it by name; to cooperate with a hook, say what the hook will check and tell Claude to read the hook's output; for MCP, list the exact tool names in `allowed-tools`.
8. Document inside the file with an HTML comment block: purpose, usage, arguments (type, valid values, defaults), examples, requirements, related commands, troubleshooting, changelog. A `help` argument branch that prints usage is worthwhile for complex commands.

### Asking questions

Use the `AskUserQuestion` tool (it must be in `allowed-tools`) for multiple-choice decisions that need explanation, multi-select preferences, and flows that adapt to earlier answers. Use arguments for simple values the user already has, scriptable invocations, and fast paths. They combine well: `argument-hint: [project-name]` plus questions for architecture choices.

Limits stated by the snapshot (source-local): 1 to 4 questions per call, 2 to 4 options per question, header at most 12 characters, an "Other" free-text choice is added automatically. `multiSelect: true` only for non-exclusive choices (features to enable), never for exclusive ones (database engine). Labels are 1 to 5 words; each description states the trade-off in a sentence or two, with equal detail across options. Order questions logically, ask as few as possible, recommend a default, allow cancel, and summarise then confirm before executing. Inspect the project first and ask only what detection could not settle.

### Stateful and multi-step commands

- Carry state between commands in `.claude/<plugin>-<workflow>.local.md` (frontmatter such as `workflow`, `stage`, `started`, `environment`, `branch`, `commit`, `tests_passed`). Each command reads the state, does its step, writes the new stage, and names the next command. A resume command continues from the recorded stage.
- Prevent concurrent runs with a lock file (`.claude/<workflow>.lock`): if present, report its start time, refuse, and point to an abort command; the completion and abort commands remove it. Always give a stale lock a cleanup path.
- Write state atomically and completely, validate its format on read, delete it when the workflow ends, and document the format.
- On failure: stop at the failed step, keep the state for recovery, record what to roll back, and state the next action. Never blindly rerun a timed-out mutation, recreate partial state, or bypass a lock; prefer validated resume, tested rollback, or reconfirmation.

### Minimal command template

```markdown
---
description: Review uncommitted changes against the team rubric
argument-hint: [focus-area]
allowed-tools: Read, Grep, Bash(git:*)
---

<!-- Usage: /review-changes [focus-area]. Read-only. Requires a git repository. -->

Focus area requested by the user: $1
If the focus area is empty, review everything and say so.

Changed files: !`git diff --name-only HEAD 2>&1 || echo "GIT_FAILED"`

If the output above is GIT_FAILED or empty, explain the likely cause and stop.

For each changed file, read it and report, with file and line:
1. Correctness risks.
2. Missing tests.
3. Naming or structure that conflicts with the surrounding code.

Finish with a three-line summary: blocking issues, non-blocking issues, files with no findings.
```

## Hooks

### Two systems

| | Hookify rule | Plugin hook |
|---|---|---|
| File | `.claude/hookify.<rule-name>.local.md` in the project | `<plugin>/hooks/hooks.json` plus scripts |
| Logic | Regex conditions in YAML frontmatter; message in the body | Prompt (natural-language judgment) or command (script) |
| Audience | One user, one project; gitignored | Everyone who installs the plugin |
| Takes effect | On the next tool use; no restart (per the hookify snapshot) | Only after a new session starts |
| Use for | The cheapest experiment after a real incident | Distributable, versioned automation |

A third place exists: a user's or project's `.claude/settings.json` can hold hooks directly. That is personal or project configuration, not a plugin.

Start from a real incident. Capture it as a hookify warn rule, review what it catches, then promote it to a plugin hook at ask level, and to block only after the false positives have been reviewed (one snapshot suggests two clean weeks; illustrative).

### Hookify rules

```markdown
---
name: warn-dangerous-rm
enabled: true
event: bash
action: warn
pattern: rm\s+-rf
---

A recursive forced delete was detected. Check the path, prefer a narrower delete,
and confirm with the user before running it.
```

- `name`: kebab-case, verb first (warn, prevent, block, require, check). `enabled`: `false` parks a rule without deleting it. `event`: `bash` (Bash commands), `file` (Edit, Write, MultiEdit), `stop` (agent wants to stop), `prompt` (user submits a prompt), or `all`. `action`: `warn` (show the message and allow; the default) or `block` (prevent the operation, or prevent stopping on a stop event).
- `pattern` is the one-condition form, a Python regex matched against `command` for bash events or `new_text` for file events. The multi-condition form is `conditions:` with a list of `field`, `operator`, `pattern`; all must match. Fields: `command` (bash); `file_path`, `new_text`, `old_text`, `content` (file); `user_prompt` (prompt). Operators: `regex_match`, `contains`, `equals`, `not_contains`, `starts_with`, `ends_with`.
- The body is the message Claude sees: what was detected, why it matters, what to do instead.
- Useful patterns. Bash: `rm\s+-rf`, `dd\s+if=`, `mkfs`, `sudo\s+`, `chmod\s+777`, `chown\s+root`. File content: `console\.log\(`, `debugger`, `print\(`, `eval\(`, `innerHTML\s*=`, `dangerouslySetInnerHTML`. File paths: `\.env$`, `credentials`, `\.pem$`, `node_modules/`, `dist/`, `build/`. Stop: pattern `.*` with a completion checklist in the body. Prompt: `user_prompt` contains "deploy to production" with a checklist.
- Regex traps: too broad (`log` also hits login, dialog, catalog; use `console\.log\(|logger\.`); too specific (`rm -rf /tmp` instead of `rm\s+-rf`); YAML quoting (inside quotes backslashes must be doubled; unquoted patterns work as written, so prefer unquoted).
- Test a pattern before saving: `python3 -c "import re; print(re.search(r'rm\s+-rf', 'rm -rf build'))"`.
- File naming: `hookify.dangerous-rm.local.md` is right; `hookify.rule1.local.md` (not descriptive), `hookify.md` (no `.local`), `danger.local.md` (no `hookify.` prefix) are wrong. Gitignore `.claude/*.local.md`.

### Plugin hook configuration

Event entry shape, identical in every format:

```json
{ "matcher": "Write|Edit",
  "hooks": [ { "type": "command", "command": "bash ${CLAUDE_PLUGIN_ROOT}/scripts/validate-write.sh", "timeout": 10 } ] }
```

**Conflict (file format).** The hook-development snapshot states that a plugin's `hooks/hooks.json` wraps events in a `hooks` object with an optional `description`, while user settings use the direct form with events at the top level:

```json
{ "description": "Write guard",
  "hooks": { "PreToolUse": [ { "matcher": "Write|Edit", "hooks": [ { "type": "prompt", "prompt": "..." } ] } ] } }
```

```json
{ "PreToolUse": [ { "matcher": "Write|Edit", "hooks": [ { "type": "prompt", "prompt": "..." } ] } ] }
```

The plugin-structure snapshot and several pattern examples show a plugin `hooks.json` in the direct form, and the setup snapshot shows project `.claude/settings.json` with events under a top-level `"hooks"` key. Selection rule: write the wrapper form for a plugin `hooks/hooks.json` (it is the form the hook-specific documentation designates for plugins), nest events under `"hooks"` inside a `settings.json`, never copy a block between the two without adjusting, and let the installed host decide: after a restart, `/hooks` must list the hook and `claude --debug` must show it registering. Upstream `plugin-dev` validators accept only the direct form; adapt wrapper files with `jq 'if has("hooks") then .hooks else . end'` before running them.

### Events and matchers

Events at snapshot time (nine): `PreToolUse` (before a tool; allow, deny, ask, or modify input), `PostToolUse` (after a tool; feedback, logging), `Stop` (main agent about to stop; completeness checks), `SubagentStop` (a subagent about to stop; not the same event as `Stop`), `UserPromptSubmit` (add context, validate, or block a prompt), `SessionStart` (load context, set environment), `SessionEnd` (cleanup, logging), `PreCompact` (add information to preserve), `Notification`. Guidance for `PreCompact` and `Notification` is thin in the snapshots. Notification matchers named by the setup snapshot: `permission_prompt`, `idle_prompt`, `auth_success`, `elicitation_dialog`.

Matchers are case-sensitive (`Write`, not `write`): exact `Write`; alternation `Read|Write|Edit`; `*` for all; regex such as `mcp__.*__delete.*`; `mcp__.*` for every MCP tool; `mcp__plugin_asana_.*` for one plugin's tools.

Load context at `SessionStart`, not on every `PreToolUse`. A `*` matcher on `PreToolUse` taxes every tool call.

### Prompt hooks and command hooks

```json
{ "type": "prompt", "prompt": "Command: $TOOL_INPUT.command. If it is destructive, return 'ask'; otherwise 'approve'.", "timeout": 30 }
{ "type": "command", "command": "bash ${CLAUDE_PLUGIN_ROOT}/scripts/check.sh", "timeout": 60 }
```

- Default to a **prompt hook** when the rule is about intent or has many surface forms. It reasons about variations a literal pattern misses and its denial explains itself. Prompt hooks are listed for `Stop`, `SubagentStop`, `UserPromptSubmit`, and `PreToolUse`; the bundled validator warns on other events. Prompt text may reference `$TOOL_INPUT`, `$TOOL_RESULT`, `$USER_PROMPT`, and a Stop prompt may direct the model to read the transcript at `$TRANSCRIPT_PATH`.
- Use a **command hook** for arithmetic or deterministic checks (file size), external tools that answer yes or no (a scanner's exit status), filesystem operations, and very fast simple checks. The "under 50 ms" figure in the snapshots is source-local and unmeasured; measure your own script including `jq` start-up.
- **Hybrid**: on one matcher, a short command hook (timeout about 5 s) for an allow-list and a prompt hook (timeout about 15 s) for the rest. They run in parallel, so each must decide independently.
- Do not turn a trivial deterministic check into a prompt hook, and do not put a prompt hook on a high-frequency event without a narrow matcher. Cost is matcher hit rate times hook cost.
- **Conflict (default type).** The snapshots default to prompt hooks. A security-critical repository may reasonably choose determinism first (command hooks, reviewed patterns) and accept more maintenance; a single-user project may choose hookify first. Record which default was chosen and why.
- Default timeouts stated by the snapshots (source-local): 60 s command, 30 s prompt; prompt hooks usually set 15 to 30 s. A slow scanner is acceptable only with a deliberately set timeout; repeated timeouts mean redesign, for example moving heavy checks to `Stop`.

### Input, output, exit codes

Input arrives as JSON on stdin: `session_id`, `transcript_path`, `cwd`, `permission_mode`, `hook_event_name`, plus `tool_name`, `tool_input`, `tool_result` (tool events), `user_prompt` (`UserPromptSubmit`), `reason` (`Stop`, `SubagentStop`).

Environment in command hooks: `$CLAUDE_PROJECT_DIR`, `$CLAUDE_PLUGIN_ROOT`, `$CLAUDE_ENV_FILE` (`SessionStart` only; append `export NAME=value` lines to persist variables), `$CLAUDE_CODE_REMOTE` (set in a remote context, where filesystem assumptions change).

Output:

```json
{ "continue": true, "suppressOutput": false, "systemMessage": "shown to Claude" }
{ "hookSpecificOutput": { "permissionDecision": "allow|deny|ask", "updatedInput": { } }, "systemMessage": "why" }
{ "decision": "approve|block", "reason": "what is missing", "systemMessage": "note" }
```

The first is valid for every event (`continue: false` halts; `suppressOutput` hides output from the transcript). The second is for `PreToolUse`. The third is for `Stop` and `SubagentStop`. Match the output schema to the event.

Exit codes (snapshot; verify): `0` success, stdout shown in the transcript; `2` blocking, stderr fed back to Claude; anything else is a non-blocking error. Consequences: a script that crashes with exit 1 does **not** deny anything, and `set -euo pipefail` without guards turns an empty `grep` into exactly that silent non-block.

### Command hook script rules

```bash
#!/bin/bash
set -euo pipefail
input=$(cat)                                              # read stdin once
file_path=$(echo "$input" | jq -r '.tool_input.file_path // empty')
if [ -z "$file_path" ]; then echo '{"continue": true}'; exit 0; fi   # nothing to check
if [[ "$file_path" == *".."* ]]; then
  echo '{"hookSpecificOutput": {"permissionDecision": "deny"}, "systemMessage": "Path traversal"}' >&2
  exit 2
fi
exit 0
```

1. Shebang, `set -euo pipefail`, read stdin once, parse with `jq`, treat every field as hostile.
2. Quote every variable. Validate identifiers (`^[a-zA-Z0-9_]+$`), reject `..`, check sensitive names (`.env`, credentials, secrets).
3. Produce `jq`-parseable output on every path; errors and denials go to stderr; exit only 0 or 2 on purpose.
4. Missing or unexpected input is a graceful skip (`{"continue": true, "systemMessage": "..."}` and exit 0), not a crash. Guard extraction pipelines with `|| true`.
5. No hardcoded paths; use `$CLAUDE_PROJECT_DIR` and `$CLAUDE_PLUGIN_ROOT`. Make the script executable.
6. No long-running work, no unpredictable global state, no secrets in logs. For audit logs record timestamp, tool name, and redacted input.
7. Portable `stat`: `stat -f%m "$f" 2>/dev/null || stat -c%Y "$f"` (BSD, then GNU).

### Parallelism and state

All matching hooks run on every matching event, in parallel, with non-deterministic order, unable to see each other's output. Plugin hooks merge with user hooks. Design every hook to decide alone.

**Conflict (temporary files).** The hook analysis states the rule: never pass state between hooks through `/tmp`. One snapshot shows caching validation results in temp files and chaining state across hooks with `/tmp/hook-state-$$`. Reconcile by case: (a) between parallel hooks of the same event, never; (b) a cache private to one hook, keyed by a hash of its input, tolerant of absence, with a short lifetime (the snapshot's five minutes is illustrative) is fine; (c) across *sequential events* (for example `SessionStart` initialises a counter, `PostToolUse` increments it, `Stop` reads it) is workable only when the file is keyed by `session_id` from the hook input in a per-user directory and cleaned at `SessionEnd`. `$$` is each hook process's own PID, so `$$`-named files are not shared between hook processes. Rate limiting that counts across parallel runs needs real locking. Coordination that must survive sessions or span users belongs outside hooks (external state with locking, a versioned plugin, or CI).

### Activation switches

- Flag file: the hook exits 0 unless `$CLAUDE_PROJECT_DIR/.enable-strict-validation` exists; `touch` to enable, `rm` to disable.
- Settings field: `enabled: true` in `.claude/<plugin>.local.md` (preferred over asking users to edit `hooks.json`, which needs a restart).
- Config file: `jq -r '.strictMode // false' .claude/plugin-config.json`.
- Environment: run only when `$CI` is set, or skip detailed checks for named users.

Document the switch in the README and always provide an escape hatch so users can bypass a misbehaving hook.

### Ten reusable patterns

1. Security validation: `PreToolUse` on `Write|Edit`, prompt checks system directories, credentials, traversal.
2. Test enforcement: `Stop` prompt reads the transcript; code changed and no tests ran gives block with a reason.
3. Context loading: `SessionStart` command detects the project type and exports variables through `$CLAUDE_ENV_FILE`.
4. Notification logging: `Notification` on `*` writes an audit line.
5. MCP monitoring: `PreToolUse` on `mcp__.*__delete.*` asks whether the deletion is intended, reversible, backed up.
6. Build verification: `Stop` prompt requires a build after code changes.
7. Permission confirmation: `PreToolUse` on `Bash`, destructive words give `ask`.
8. Code quality: `PostToolUse` on `Write|Edit` runs a linter on the changed file and never fails the hook (`|| true`).
9. Flag-file activation (above).
10. Configuration-driven behaviour (read limits and modes from project config).

A `Stop` hook that blocks on a misjudgment can loop the agent; give it an exit condition. A deny is terminal until the input changes: zero verbatim retries, at most one modified attempt. An ask is a human checkpoint; do not rephrase around it.

### Debugging order

After any change: restart, check `/hooks`, exercise under `claude --debug` (registration, input and output JSON, timing). When a hook seems dead, check in this order: wrong event, matcher (spelling and case), output schema, implementation. Four silent failure modes: stale session, dead or case-mismatched matcher, timeout kill, shared temp-file race. A renamed script is not reliably caught at startup (missing scripts produce warnings; invalid JSON prevents loading). If a script does not run: shebang, executable bit, path through `${CLAUDE_PLUGIN_ROOT}`.

## MCP integration

### Configuration

Two places: a `.mcp.json` at the plugin root (preferred: separate, easier to maintain, suits several servers) or an inline `mcpServers` object in `plugin.json` (acceptable for one simple server).

```json
{
  "db": {
    "command": "${CLAUDE_PLUGIN_ROOT}/servers/db-server.js",
    "args": ["--config", "${CLAUDE_PLUGIN_ROOT}/config/db.json"],
    "env": { "DATABASE_URL": "${DATABASE_URL}" }
  },
  "tracker": { "type": "sse", "url": "https://mcp.example.com/sse" },
  "api": { "type": "http", "url": "https://api.example.com/mcp",
           "headers": { "Authorization": "Bearer ${API_TOKEN}" } },
  "live": { "type": "ws", "url": "wss://example.com/mcp" }
}
```

**Conflict (file shape).** The MCP snapshot shows server names at the top level of a plugin `.mcp.json`, as above. The plugin-structure snapshot (and the Codex scaffold, which writes `{"mcpServers": {}}`) wraps them in an `mcpServers` object. Inline configuration in `plugin.json` always uses the `mcpServers` key. Select by host verification: write one shape, restart, and accept it only when `/mcp` lists the server and its tools; if it does not, try the other shape before debugging anything else.

`${CLAUDE_PLUGIN_ROOT}` and user shell variables such as `${API_TOKEN}` are expanded in MCP configuration. Document every required variable in the README: its name, how to obtain the value, and which permissions the token needs.

### Transport choice

| Type | Select when | Auth | Notes |
|---|---|---|---|
| stdio (`command`, `args`, `env`) | Local tools, local databases, a server shipped with the plugin or run through `npx` | Environment variables | Child process for the whole session; lowest latency; logs must go to stderr |
| SSE (`type: sse`, `url`) | Hosted services with OAuth | OAuth handled by the host, or headers | Automatic reconnection; no local install |
| HTTP (`type: http`, `url`, `headers`) | REST-style backends with token auth | Headers | Stateless; handle rate limits and timeouts |
| WebSocket (`type: ws`, `url`) | Real-time streaming, server push | Headers | Persistent; needs heartbeat, reconnection, buffering |

Latency and setup comparisons in the snapshots are qualitative, not measured. Decide hosting first (local or hosted), then transport, then authentication: transport is the early, hard-to-reverse fork, and adapting an OAuth SSE example to token HTTP means rewriting its authentication section. Types can be mixed in one plugin.

### Authentication and custody

- The plugin owns the shape of the configuration. The user's shell owns environment secrets. Claude Code owns OAuth tokens: they are stored by the host, refreshed by the host, cleared on sign-out, and not readable by the plugin.
- OAuth (SSE or HTTP): no auth block in the configuration. The first tool use opens a browser for consent; a headless environment needs a documented manual step. Scopes are decided by the server; list the needed permissions in the README.
- Token auth: `Authorization: Bearer ${API_TOKEN}`, an API-key header, or custom headers, always from environment variables. The header value needs the `Bearer ` prefix when the service expects it.
- Dynamic headers: `"headersHelper": "${CLAUDE_PLUGIN_ROOT}/scripts/get-headers.sh"`, a script that prints a JSON object of headers, for short-lived tokens, JWTs, or HMAC signatures. Verify the field on the target version.
- Multi-tenant: tenant through a header (`X-Workspace-ID: ${WORKSPACE_ID}`) or the URL (`https://${TENANT_ID}.api.example.com/mcp`).
- Mutual TLS is not expressible in the configuration per the snapshot; wrap the service in a plugin-shipped stdio server that holds the client certificate.
- For stdio servers: validate the command path, never execute a command supplied by a user, pass only the environment variables the server needs, restrict its filesystem scope, and pass configuration through arguments or environment, never stdin.
- Never commit a literal token, never put a token in documentation, use `https://` and `wss://` only (plain `http://localhost` only through a development-only `${API_URL}`), never skip certificate verification. If a token was ever hardcoded, move it to a variable and rotate it.

### Tools

Tool names are prefixed: `mcp__plugin_<plugin-name>_<server-name>__<tool-name>`, for example `mcp__plugin_asana_asana__asana_create_task`. Read the exact, case-sensitive names from `/mcp`.

- **Commands** pre-allow exact names: `allowed-tools: ["mcp__plugin_asana_asana__asana_search_tasks", "mcp__plugin_asana_asana__asana_create_task"]`. A wildcard (`mcp__plugin_asana_asana__*`) is for the rare command that truly needs every tool, with the reason written down.
- **Agents**, per the snapshot, may use MCP tools without a pre-allowed list. So for an agent the control is its own tool configuration and its instructions: name the exact tool for each step and document the tools it typically uses.
- Patterns: a thin command (gather input, validate, call one tool, confirm); an agent for multi-step autonomous work; a command that gathers input then hands over to an agent; CRUD command families that name sibling tools; several servers in one plugin for cross-service workflows.
- Before calling: validate required parameters and formats; ask the user for missing data instead of guessing. After: on success, extract and show the relevant data with ids or links; on error, classify (auth, rate limit, validation), say what to check in user terms, and do not leak internal details; on partial success, report "8 of 10 processed" with the failed items and reasons.
- Tell the user before and after a long call, break long operations into steps, and list the MCP tools a command uses in its comment block.
- Prefer one filtered query with a limit over a loop of per-item calls (a loop of fifty single gets is wrong even when run in parallel). Reuse results within a workflow.

### Lifecycle and failure

**Conflict (start time).** One statement in the snapshot says servers start when the plugin is enabled; another says connections are lazy and the first tool use triggers them. Both are kept. Plan for both: expect a one-time delay on the first call, and do not rely on a server being up before its first use. Either way, edits to MCP configuration do nothing until a new session.

Diagnose in order and stop at the first failing stage: connection (URL, command exists and is executable, certificate, network), discovery (`/mcp` lists the tools), authentication at first use. A stray `print` or `console.log` on stdout corrupts the stdio JSON-RPC stream; set `PYTHONUNBUFFERED=1` for Python servers and log to stderr. HTTP status meanings: 401 token missing, expired, or badly formatted; 403 valid token lacking scope or wrong tenant; 429 back off; 500 read server logs.

Retry only retryable failures (rate limit, network), at most three attempts (source-local), then tell the user and suggest checking configuration. Never retry authentication or validation failures as if they were transient. Ownership: the host reconnects, the command author decides retries, the message tells the user how to remediate.

**Conflict (debug flag).** Most snapshots use `claude --debug`; the setup snapshot names `claude --mcp-debug` for MCP configuration problems. Use whichever the installed version accepts (`claude --help`).

## Plugin settings

### Convention

Per-project, per-plugin configuration and state lives in `.claude/<plugin-name>.local.md` in the project root: YAML frontmatter for structured values that scripts read, Markdown body for prompt or task text that Claude reads. It is user-managed and must be gitignored (`.claude/*.local.md`, `.claude/*.local.json`); the plain `.md` suffix risks commits. The name must match the plugin name exactly. This is not the user-level `settings.json` and not the manifest. Machine-level values fit environment variables better. Hookify rule files share the `.local.md` idea but are read by the hookify engine, not by your scripts.

```markdown
---
enabled: true
mode: standard
max_file_size: 1000000
---

# Notes for Claude
Extra task context goes here.
```

### Rules

1. Design the schema and defaults before writing a parser. For every field record type, default when absent, validation, which surface consumes it, who writes it, and what happens on rename.
2. Quick-exit when the file is absent; then check `enabled`; then default and validate every field; update through a temporary file and `mv`, never `sed -i`.
3. **Conflict (absent file).** The snapshot shows both "absent means not configured, exit 0" and "absent means use defaults". Select by activation semantics: opt-in behaviour skips when the file is absent; always-on behaviour with tunables applies defaults.
4. Invalid values warn on stderr and fall back to the default; they never crash a hook. A setup command may refuse and exit 1.
5. One writer per field; there is no locking. Commands create the file (ask preferences, write, confirm, remind about restart). Hooks read it and may update counters. Hooks never prompt users. Agents are told in their instructions to check the file.
6. Security: escape quotes when writing user input, reject `..` in path-valued settings, `chmod 600` when it holds anything sensitive, never share it between users.
7. **Conflict (restart).** The snapshot (and the bundled validator's closing reminder) says changes to the settings file require restarting Claude Code. The settings analysis notes that a hook script which re-reads the file on every invocation picks up edits immediately, and that it is the hook *configuration* that needs a restart. Tell users to restart unless you have verified that every consumer re-reads the file per invocation; in that case say so explicitly for those fields.
8. Keep it small: one flat file, simple values. If the schema is too complex to hand-edit, use JSON or SQLite state instead.

### Parsing (bash)

```bash
FILE=".claude/my-plugin.local.md"
[ -f "$FILE" ] || exit 0                                           # quick exit
FRONTMATTER=$(sed -n '/^---$/,/^---$/{ /^---$/d; p; }' "$FILE")    # parse once
get() { echo "$FRONTMATTER" | grep "^$1:" | sed "s/$1: *//" | sed 's/^"\(.*\)"$/\1/' | sed "s/^'\(.*\)'$/\1/" || true; }
ENABLED=$(get enabled); [ "$ENABLED" = "true" ] || exit 0
MAX=$(get max_file_size)
if ! [[ "$MAX" =~ ^[0-9]+$ ]]; then echo "max_file_size invalid, using default" >&2; MAX=1000000; fi
MODE=$(get mode); case "$MODE" in strict|standard|lenient) ;; *) MODE=standard ;; esac
BODY=$(awk '/^---$/{i++; next} i>=2' "$FILE")                      # safe when the body contains ---
```

Atomic update:

```bash
TMP="${FILE}.tmp.$$"
sed "s/^iteration: .*/iteration: $NEXT/" "$FILE" > "$TMP" && mv "$TMP" "$FILE"
```

Traps: values may be bare, double-quoted, or single-quoted (strip both); values with colons, spaces, or regex characters must be quoted in the YAML and the shell variable quoted on use; empty, `""`, and `null` all mean missing; a `sed` range used for the body breaks when the body contains `---` (use the `awk` counter); booleans are compared as strings; a naive substring test on a list matches `item1` inside `item10` (use `yq -o json` plus `jq`, after checking `yq` is installed, or Python). Per hook fire do the cheap things first: filter on tool name, test file existence, parse the frontmatter once, extract fields lazily. Re-opening the file once per field is waste. To debug, print the parsed values to stderr and run the parser against a file with known contents.

### Loop state

When a settings file drives a loop (the ralph-loop example: `iteration`, `max_iterations`, `completion_promise` in frontmatter, the prompt in the body, a `Stop` hook that blocks and feeds the body back as `reason`): bound it with `max_iterations`, noting that `0` means unlimited in that example; increment atomically before re-arming; compare the completion text exactly after trimming whitespace; delete the state file on every exit path. File existence is a valid "active" switch for short-lived loop state; an `enabled` field is better for long-lived configuration that users toggle. A time bound is a sound alternative when a start timestamp is recorded.

## Plugin agents

This section covers the agent *file* a plugin ships: where it lives, its frontmatter, how it triggers, and how to validate it. Delegation strategy, context budgets, and multi-agent coordination are a different subject.

An agent is an autonomous subprocess for multi-step work that Claude starts when a task matches its description. A command is user-initiated; an agent is model-initiated. Every `.md` file in the plugin's `agents/` directory is discovered automatically. An agent in a subdirectory is addressed as `plugin:subdir:agent-name`.

```markdown
---
name: diff-reviewer
description: Use this agent when the user asks for a review of uncommitted changes, or right after a feature is finished and before a commit. Do not use it for whole-repository audits. Examples: <example>Context: the user has just finished a feature. user: "Review my changes before I commit." assistant: "I will use the diff-reviewer agent to examine the uncommitted diff." <commentary>Explicit review request on local changes.</commentary></example> <example>Context: Claude has just completed a multi-file edit. user: "Looks done." assistant: "Before we stop, I will run the diff-reviewer agent on the changes." <commentary>Proactive use after substantial edits.</commentary></example>
model: inherit
color: blue
tools: ["Read", "Grep", "Glob"]
---

You are a code reviewer specializing in uncommitted diffs.

**Your Core Responsibilities:**
1. Read every changed file in full before judging it.
2. Report correctness risks, missing tests, and inconsistencies with nearby code.

**Analysis Process:**
1. List changed files.
2. Read each one and its direct callers.
3. Classify findings as blocking or non-blocking.

**Quality Standards:**
- Every finding cites file and line.
- No finding without evidence from the code.

**Output Format:**
Blocking findings, non-blocking findings, files with no findings.

**Edge Cases:**
- No changes: say so and stop.
- Binary or generated files: list them, do not review them.
```

### Frontmatter

| Field | Required (per the agent snapshot) | Rule |
|---|---|---|
| `name` | Yes | Lower-case letters, digits, hyphens; 3 to 50 characters; starts and ends with a letter or digit. Good: `code-reviewer`, `api-docs-writer`. Bad: `helper` (generic), `-agent-`, `my_agent`, `ag` |
| `description` | Yes | The triggering contract and the most important field. Starts "Use this agent when ..."; contains 2 to 4 `<example>` blocks, each with Context, the user's words, the assistant's response, and a `<commentary>` saying why the agent applies; shows both reactive use (the user asks) and proactive use (Claude decides); varies the phrasing; says when not to use it. Length 10 to 5,000 characters, best 200 to 1,000 (source-local) |
| `model` | Yes | `inherit` (recommended), `sonnet`, `opus`, `haiku` at snapshot time |
| `color` | Yes | `blue`, `cyan`, `green`, `yellow`, `magenta`, `red`. Use different colours for different agents in one plugin and the same colour for similar roles: blue or cyan for analysis and review, green for success-oriented tasks, yellow for caution and validation, red for critical or security work, magenta for creative or generative work |
| `tools` | No | Array of tool names. When omitted the agent can use every tool. Give the minimum: read-only analysis `["Read", "Grep", "Glob"]`; generation `["Read", "Write", "Grep"]`; testing `["Read", "Bash", "Grep"]`; everything by omission or `["*"]` |

**Conflict (agent frontmatter).** The agent snapshot lists `name`, `description`, `model`, and `color` as required. The plugin-structure snapshot shows an agent with only a `description` and a `capabilities` list. Write the four-field form (it is the one the bundled validator checks), and confirm on the installed version that the agent appears and triggers; drop or add fields only on that evidence.

### System prompt (the body)

1. Write in the second person, addressed to the agent: "You are ...", "You will ...". Not the first person.
2. Include, in this order: role and domain; core responsibilities; a step-by-step process; quality standards; output format; edge cases with handling.
3. Be specific; a vague prompt gives vague work. Length 20 to 10,000 characters, best 500 to 3,000 (source-local).
4. Each surface has its own voice, and mixing them is a common error: a command body gives directives to Claude; an agent body addresses the agent as "you"; a skill body uses verb-first instructions; a skill description is in the third person.

### Creating one

- Generated: ask Claude for an agent configuration from a one-paragraph request, requiring it to extract the core intent and responsibilities, design an expert persona, write a system prompt with behavioural boundaries, method, edge cases, and output format, choose an identifier (lower-case, hyphens, 3 to 50 characters), and write the description with 2 to 3 examples; ask for JSON with `identifier`, `whenToUse`, and `systemPrompt`; then convert it to the file format above.
- Manual: choose the identifier; write the description with examples; pick the model (usually `inherit`); pick a colour; restrict tools; write the body; save as `agents/<name>.md`.

### Testing

- Triggering: in a new session, phrase a request like the examples and a paraphrase of them, and check the agent is selected; phrase a neighbouring request and check it is not.
- Behaviour: give a typical task; check it follows the process steps, returns the stated output format, handles each listed edge case, and meets the quality standards.
- Structure: validate frontmatter delimiters, `name` format/length, `description` length and `<example>` blocks, `model`, `color`, optional `tools`, and second-person body (upstream `plugin-dev` provides `validate-agent.sh`; see "Upstream reference utilities" for its known limits).
- Document the agent in the plugin README: what it does, when it triggers, which tools it has.

## Plugin skills

This section covers placing a skill in a plugin and making it trigger. Writing the skill's content well is a different subject.

1. Location: `<plugin>/skills/<skill-name>/SKILL.md`. The host scans `skills/` for subdirectories that contain a file named exactly `SKILL.md`. The name and description are always in context; the body loads when the skill triggers; bundled files load or run only when needed. Plugin skills ship with the plugin; there is no separate packaging step.
2. Frontmatter: `name` and `description` are required; `version` is optional.
3. Description: third person, with the literal phrases users say: `This skill should be used when the user asks to "create a hook", "add a PreToolUse hook", "validate tool use", or mentions hook events (PreToolUse, PostToolUse, Stop).` Weak forms: "Use this skill when working with hooks" (wrong person, vague), "Provides hook guidance" (no trigger phrases).
4. Body: verb-first instructions ("Parse the frontmatter with sed", "Validate values before use"), not "You should ..." and not "Claude should ...". Write for another Claude instance: include what is useful and non-obvious.
5. Bundled resources and what each is for: `scripts/` holds code that must be deterministic or would otherwise be rewritten every time (it can run without being read into context, though it may need reading to patch); `references/` holds documentation to load on demand (schemas, API documentation, policies; for a very large file, put search patterns in the body); `examples/` holds complete, runnable samples to copy; `assets/` holds files used in the output and never loaded (templates, icons, boilerplate). Create only the directories that are used, and name every bundled file in the body, or Claude will not know it exists.
6. Layout tiers: minimal (`SKILL.md` alone, for simple knowledge); standard (`SKILL.md`, `references/`, `examples/`); complete (adds `scripts/` with validation utilities).
7. Process: collect concrete examples of use and the words that should trigger it (a few questions at a time, not a questionnaire); for each example, decide what a script, a template asset, or a reference would save on repetition (rotating PDFs repeatedly suggests a script; the same web boilerplate each time suggests an asset; rediscovering table schemas suggests a reference); create the structure; write resources first, then the body; validate; use it on real tasks and iterate while the experience is fresh.

```bash
mkdir -p my-plugin/skills/my-skill/{references,examples,scripts}
touch my-plugin/skills/my-skill/SKILL.md
```

8. Validate: the directory is in the right place; frontmatter has `name` and `description`; the description has specific trigger phrases; the body is in instruction form; every referenced file exists; examples are complete; scripts are executable and work. Then test in the host: load the plugin (the snapshot shows starting Claude Code with `--plugin-dir /path/to/plugin`; verify the flag on the installed version), ask questions that should trigger the skill and one that should not.
9. Common iteration fixes: stronger trigger phrases; clearer instructions; a missing example or script; an edge case.

**Conflict (how much goes in the body).** The plugin-skill snapshot keeps the body lean (1,500 to 2,000 words ideal, under 3,000 without references, 5,000 at most; reference files of 2,000 to 5,000 words or more; all source-local) and moves detail to `references/`, with no duplication between the two. This library's own rule is that a skill must work when it is the only file loaded, so core rules stay in the body even when that makes it long. Select the lean form when the skill competes for context with many others and the host reliably loads references on demand; select the complete form when a missed rule costs more than the extra context. In both, an 8,000-word body with no structure and no references is the failure.

## Example and demonstration plugins

An example is a bounded teaching contract, not a showcase. It states one user goal, the observable success, a non-goal, what happens on accidental activation, the invocation surface, permissions, effects, failure recovery, and its evidence status.

1. Use the least powerful surface that establishes the outcome: contextual skill (model-selected guidance), command (explicit operation), hook (lifecycle event), MCP (protocol tools), setting (persistent configuration), wrapper plugin (distribution unit).
2. Build order: capability and non-goal, primary surface, target host contract (host, exact version, schema, paths, loader, validators, install, permissions, cleanup), minimal tree, deterministic behaviour, positive and negative activation, permission and failure cases, install and removal, copyability. Repair the earliest invalid boundary first.
3. Build the smallest deterministic, isolated artifact. Add files, privilege, network, or further surfaces only for a demonstrated responsibility. Decorative completeness teaches capabilities the example does not have.
4. An example that contains only a skill supports claims about focused purpose, description-led triggering, the required `SKILL.md`, optional support folders, and overlap testing. It supports no claim about manifests, commands, hooks, MCP, permissions, installation, upgrade, or removal.
5. Skill inside a plugin: `skills/<skill-name>/SKILL.md` with `name` and `description` (required), optional `version` and `license`; optional `README.md`, `references/`, `examples/`, `scripts/`. The description states activation in the third person with concrete phrases and keywords ("should be used when the user asks to ..., mentions ..., or discusses ..."). One domain per skill. Avoid generic cues such as "plugin", "tool", "development" that overlap with neighbours.
6. Skills are model-invoked, commands are user-invoked, agents are spawned by Claude. Say which one the example demonstrates.
7. Test: positive request, paraphrased request, neighbouring request that must not trigger, overlap with another skill, repeated run, invalid input, cancellation, denial, non-interference with other components, and lifecycle where relevant. One happy path is not enough.
8. What each check proves: static parsing proves shape; schema validation proves acceptance; host loading proves discovery; invocation proves activation; isolated behaviour proves output and effects; packaging and lifecycle exercises prove distribution claims.
9. Re-open evidence when things change: a description edit re-opens activation tests; a support-file edit re-opens reachability and packaging checks; a script edit re-opens permission, effect, and cleanup evidence.
10. Keep with the example: commands run, observations, assumptions, status, one rejected design, owner, refresh triggers. Promotion to a reusable template needs clean-copy, compatibility, security, lifecycle, ownership, and retirement evidence.
11. Do not copy historical frontmatter, paths, Unicode directory trees, optional folders, or broad trigger wording from an old example as if it were policy.

Status ladder, with the claim each level forbids:

| Status | Established by | Must not claim |
|---|---|---|
| Conceptual | Design only | That anything parses or loads |
| Source-valid | Static parse and schema checks | Discovery by a host |
| Host-loaded | Listed by the real host after a new session | Correct behaviour |
| Behavior-validated | Positive and negative cases observed in isolation | Integration with other components, install, removal |
| Integrated | Works with the other surfaces it names | Distribution |
| Packaged / promoted | Clean install, update, disable, remove, and ownership evidence | Anything about untested hosts or versions |

## Codex plugin creation

Codex plugins are a separate ecosystem with their own manifest location and tooling; nothing here defines Claude Code behaviour, and nothing in the Claude Code sections defines Codex behaviour.

A Codex plugin is a composition and distribution boundary for skills, apps, MCP declarations, assets, scripts, hooks, and interface metadata. Choose it when capabilities must be installed, discovered, versioned, and maintained together; prefer a standalone skill, app, MCP integration, hook policy, script, or repository instruction when plugin-level distribution adds nothing.

### Layout and naming

- Manifest: `<plugin>/.codex-plugin/plugin.json` (required). Optional: `skills/`, `hooks/`, `scripts/`, `assets/`, `.mcp.json`, `.app.json`.
- Name: lower-case hyphen-case, at most 64 characters; spaces, underscores, and punctuation become `-`, repeats collapse (`My Plugin` becomes `my-plugin`). The folder name equals the manifest `name`. Check for collisions on the *normalized* name before creating anything.
- Manifest fields at snapshot: `name`, `version`, `description`, `author` (`name`, `email`, `url`), `homepage`, `repository`, `license`, `keywords`, `skills`, `hooks`, `mcpServers`, `apps`, and `interface` (`displayName`, `shortDescription`, `longDescription`, `developerName`, `category`, `capabilities`, `websiteURL`, `privacyPolicyURL`, `termsOfServiceURL`, `defaultPrompt`, `brandColor`, `composerIcon`, `logo`, `screenshots`). Paths are relative and start with `./`. `defaultPrompt` holds at most three entries, each capped at 128 characters (aim for about 50); screenshots are PNG files under `./assets/`. Custom component paths supplement default discovery.
- Companions must agree with declarations: `apps` requires `.app.json`; a path-valued `mcpServers` requires `.mcp.json` (inline server objects can be valid); every referenced asset must exist inside the plugin directory.

**Conflict (top-level `hooks`).** The archived manifest sample, and the bundled scaffold's output, include a top-level `hooks` key. The current local validator described in the creator analysis rejects top-level `hooks`. The validator of the Codex version you target governs: omit the key when that validator rejects it, and configure hooks through the mechanism that version supports.

**Conflict (scaffold defaults).** The bundled scaffold (2026-03 snapshot) writes `[TODO: ...]` placeholders that must all be replaced or removed. The later creator described in the Codex creator analysis emits defaults that already validate. With the bundled script, treat every `[TODO` string as a failing gate.

**Conflict (default destination).** The snapshot defaults to a repository-local plugin at `<repo>/plugins/<name>` with the marketplace at `<repo>/.agents/plugins/marketplace.json`, and offers home-local `~/plugins` with `~/.agents/plugins/marketplace.json`. The later workflow defaults marketplace-backed creation to a personal plugin and marketplace and requires an explicit request for shared or team locations. When the location is not explicit, ask repository-local or home-local before writing a marketplace entry.

### Marketplace file

Top-level `name`, optional `interface.displayName`, and an ordered `plugins[]` (order is render order; append unless asked to reorder). Each entry: `name`, `source` (`{"source": "local", "path": "./plugins/<name>"}`), `policy.installation` (`NOT_AVAILABLE`, `AVAILABLE` default, `INSTALLED_BY_DEFAULT`), `policy.authentication` (`ON_INSTALL` default, `ON_USE`), `category`. Add `policy.products` only on explicit request. The display name belongs to the marketplace `interface`, not to entries. Preserve the existing `interface.displayName`, entry order, and every unrelated entry.

### Lifecycle

1. Decide the surface and whether this is a new plugin or an update.
2. Inspect the destination, normalized-name collisions, existing manifest, marketplace file, authority to write there, and companion files. Inspect first; never use creation or `--force` to discover whether a path is occupied.
3. Scaffold minimally (only the components that will be used).
4. Replace placeholders with truthful metadata.
5. Validate with the creator's validator for the target version.
6. Expose through the marketplace and install only when authorized.
7. Test in a **fresh** task: installation does not prove a new task picks the plugin up.
8. Update through the version cachebuster and reinstall flow; the cachebuster helper only changes the version and proves nothing else.
9. Recover or remove while preserving the prior identity and unrelated state.

Commands in the current creator (not bundled here; names from the Codex creator analysis, verify on the target version): `python3 scripts/validate_plugin.py <plugin-path>`, `python3 scripts/update_plugin_cachebuster.py <plugin-path>`, `python3 scripts/read_marketplace_name.py [--marketplace-path <path>]`, `codex plugin add <name>@<marketplace>`, `codex plugin list`, `codex plugin marketplace add <marketplace-root>`. `--marketplace-name` is only for the new-marketplace exception.

`--force` is never an ordinary retry. Use it only for an inventoried, explicitly authorized replacement with a recovery copy.

Claims ladder: a scaffold existing does not prove validation; validation does not prove marketplace discovery, installation, runtime behaviour, remote health, or security; installation does not prove fresh-task pickup; an invocation covers only the tested capability and environment; update evidence does not prove rollback or removal. Evidence statuses to use: `verified`, `pending`, `not_observed`, `not_applicable_with_reason`, `blocked`.

## Claude Code setup recommendations

Setup is control-plane design for a repository: automate only repeated work or material risk, and never bypass existing tools, permissions, or review. Recommending and authorising are separate phases: the survey is read-only and produces recommendations; nothing is created or changed until the owner approves.

### Survey (read-only)

```bash
ls -la package.json pyproject.toml Cargo.toml go.mod pom.xml 2>/dev/null
head -50 package.json 2>/dev/null
grep -E '"(react|vue|angular|next|express|fastapi|django|prisma|supabase|stripe)"' package.json 2>/dev/null
ls -la .claude/ CLAUDE.md .mcp.json 2>/dev/null
ls -la src/ app/ lib/ tests/ components/ pages/ api/ 2>/dev/null
ls .prettierrc* .eslintrc* eslint.config.* ruff.toml tsconfig.json mypy.ini pyrightconfig.json 2>/dev/null
ls -d .github/workflows .gitlab-ci.yml .circleci 2>/dev/null
```

Inventory: languages, frameworks, package manager, tests, formatters, CI, issue tracker references, external services, existing Claude configuration, team commands. Then state the observable friction, check whether existing commands or documentation already cover it, and choose one or two high-value items.

### Signal to candidate (each row is a lead to confirm, never a decision)

| Signal | Candidate |
|---|---|
| Prettier, Black, gofmt, rustfmt, Ruff configuration in active use | `PostToolUse` format hook on `Edit|Write` |
| ESLint or Ruff | `PostToolUse` lint hook; TypeScript: `tsc --noEmit`; mypy or pyright: type check |
| Test directories and runner configuration | `PostToolUse` related-tests hook, or a test-writer subagent when tests are sparse |
| `.env*`, `credentials.json`, `secrets.yaml`, `.git/` | `PreToolUse` hook blocking edits |
| Lock files (`package-lock.json`, `yarn.lock`, `pnpm-lock.yaml`, `Cargo.lock`, `poetry.lock`, `Pipfile.lock`) | `PreToolUse` hook blocking direct edits (change them through the package manager) |
| Multitasking users | `Notification` hooks (`permission_prompt`, `idle_prompt`) |
| Popular libraries and SDKs | Documentation-lookup MCP (context7) |
| Frontend UI | Browser MCP (Playwright; Puppeteer for PDF or headless CI); UI-reviewer subagent |
| Supabase, PostgreSQL or MySQL clients, Neon, Turso | Database MCP |
| GitHub or GitLab remote, issue references such as `ABC-123` | GitHub, GitLab, or Linear MCP |
| `@aws-sdk/*`, Terraform, Cloudflare, Vercel | Cloud MCP |
| `@sentry/*`, Datadog | Monitoring MCP |
| Slack webhooks, Notion | Communication MCP |
| Docker or Kubernetes files | Container MCP |
| Long projects needing persistence; web research | Memory MCP; Exa |
| Large codebase (the snapshot's ">500 files" is an unmeasured heuristic) | Code-reviewer subagent |
| Auth or payments code | Security-reviewer subagent (read-only tools) |
| API routes, OpenAPI, GraphQL | API-documenter subagent; `api-doc` skill with a template |
| Performance-critical paths, ORM use | Performance-analyzer subagent |
| Old framework, deprecations | Migration-helper subagent |
| Repeated prompts, templated tasks | Project skill at `.claude/skills/<name>/SKILL.md` (for example `create-migration`, `gen-test`, `new-component`, `pr-check`, `release-notes`, `setup-dev`, `project-conventions`) |
| PR-heavy workflow; language servers; onboarding | Existing plugins (review toolkits, LSP plugins, output-style plugins) from the official marketplace listing current at the time |

Skill invocation control: `disable-model-invocation: true` makes a skill user-only (anything with side effects: deploy, commit, send); `user-invocable: false` makes it Claude-only (background knowledge); omitting both allows both. `context: fork` runs it in an isolated subagent; `allowed-tools` restricts it. Subagent tool access: read-only (`Read`, `Grep`, `Glob`) for reviewers, add `Write` for generators, add `Bash` for migration and testing; model choice at snapshot: haiku for simple repetitive checks, sonnet by default, opus for migrations and architecture. Subagents live in `.claude/agents/<name>.md`. MCP scopes: project `.mcp.json` (checked in for team sharing), or user-global configuration.

### Rules

1. A dependency or file being present does not prove automation need, service need, authorization, or compatibility. Abandoned tests, obsolete formatter configuration, and unused SDKs do not justify automation. Installing every plugin or MCP server that dependency names suggest is not evidence-led.
2. Discover the repository's exact commands (its real lint, test, and format scripts); never invent `npm`, `pytest`, or `cargo` invocations from a catalogue match.
3. Each recommendation records: signal, unchanged baseline (current scripts, CI, docs, manual sequence, and counterfactual if unchanged), outcome, selected surface, rejected alternatives, overlap and dependencies (existing controls that duplicate, call, trigger, or are triggered by the candidate), configuration, owner, invocation, tools and scopes, failure model (trigger, observable signal, containment, recovery, escalation owner), positive and negative cases, exact validation gate, rollout (disabled by default, trial scope, observation period, who may enable, disable path, restoration of prior workflow) and rollback, unresolved questions (owner, evidence source, resolution gate), and retirement trigger. Use the full record for shared, automatic, side-effecting, externally connected, security-sensitive, or hard-to-remove setup; a reversible personal preference may use a short record (outcome, baseline, candidate, authority, verification, disable path); split records across different ownership, credential, production, or data boundaries.
4. Output shape for a survey: codebase profile (type, framework, key libraries); then the top one or two recommendations per relevant category, each with name, the signal that justifies it, where it would be installed or created, and how it is invoked; skip irrelevant categories; if the user asks about a single category, give three to five options; close by offering more detail per category.
5. Authority order on conflict: direct user constraint, then organisation or repository policy, then security and data rules, then compatible implementation behaviour, then owner-approved local workflow, then supporting examples. When sources conflict, keep both positions, freeze dependent work, and ask the controlling owner. Never choose by file count, length, apparent recency, or confidence of tone.
6. Hard gates that override convenience: secret exposure or over-broad secret scope, unauthorized external transfer, destructive mutation, hidden failure, failed rollback, ownerless shared automation.
7. Stop and route elsewhere when permission is unknown, an external mutation lacks idempotency or rollback, current product availability has not been re-checked, two surfaces would own the same behaviour, or nobody owns failures and updates. A database MCP without an owner, credential scope, read-only probe, and retention rule stays a research item.
8. Setup cannot repair missing product requirements, service access, credentials, policy, production governance, or model capability.
9. Durable setup needs a version assumption, an owner, evidence, and a removal condition. Remove it when the signal disappears, ownership changes, permissions widen, or its value no longer exceeds maintenance and diagnosis cost.
10. Negative gates matter: an unrelated file, a denied action, malformed input, a missing service, and an injected instruction must all leave the setup quiet or safely refusing. Never weaken the expected behaviour to make a gate pass.
11. When something misbehaves: stop the behaviour, preserve minimal evidence, classify the layer, inspect side effects, restore, substitute the least powerful replacement, rerun the trigger and nearby negatives.

Useful non-interactive invocations (snapshot; verify): `claude -p "fix lint errors in src/" --allowedTools Edit,Write`; `claude -p "<prompt>" --output-format stream-json | <consumer>`. Permission allow-lists live in `.claude/settings.json`, for example `{"permissions": {"allow": ["Edit", "Write", "Bash(npm test:*)"]}}`. MCP servers are added with `claude mcp add <name>`; plugins with `/plugin install <name>`, listed with `/plugin list`.

## Output contract

Deliver the artifact plus the record that matches it. Use the full form for anything shared, automatic, or side-effecting; a short form is enough for a reversible personal item.

**Capability trace (plugin)** - one row per capability: capability; component; declaration; packaged path; discovery evidence; activation evidence; portable resources; disable; update migration; removal cleanup.

**Command contract** - purpose and non-goals; why a command and not another surface; file name and namespace; directives; frontmatter; input grammar; questions; tools; plugin resources; scripts; effects; state; confirmations; errors and recovery; tests; documentation; compatibility; removal.

**Hook lifecycle row**

| Event | Matcher | Type | Timeout | Output contract | Escalation level | Test evidence | Bypass | Log location and review cadence |
|---|---|---|---|---|---|---|---|---|
| `Stop` | `*` | prompt | 30 s | `decision` + `reason` | block | fixture + debug run | `enabled: false` in settings | `.claude/audit.log`, weekly |

**MCP boundary map** - one row per server: server name; transport; auth method; required environment variables (none for OAuth); tools confirmed in `/mcp`; consuming commands and agents; permission model; failure recovery.

**Settings schema table**

| Field | Type | Default when absent | Validation | Consumer | Writer | Migration on rename |
|---|---|---|---|---|---|---|
| `max_iterations` | number | `0` (unlimited) | `^[0-9]+$` | stop hook | setup command | read old name for one release |

**Setup decision record** - status (proposed, paused, rejected, authorized, trialing, adopted, disabled, replaced, retired); signal; unchanged baseline; outcome; selected and rejected surfaces; overlap and dependencies; configuration; owner; invocation; tools and scopes; failure model (trigger, signal, containment, recovery, escalation owner); positive and negative cases; exact gate; rollout (disabled by default, trial scope, observation period, enabler, disable path, prior-workflow restoration) and rollback; unresolved questions (owner, evidence source, resolution gate); retirement trigger; version assumption. Full record for shared/automatic/side-effecting/externally-connected/security-sensitive/hard-to-remove setup; short record (outcome, baseline, candidate, authority, verification, disable path) for reversible personal preferences; split when candidates cross ownership, credential, production, or data boundaries.

**Demonstration record** - goal; observable success; non-goal; accidental-activation consequence; surface; permissions; effects; recovery; status from the ladder above; commands run and observations; one rejected design; owner; refresh triggers.

Every delivery ends with an evidence statement: which gates ran and passed, what was observed on which host version, and what remains unverified.

## Quality gates

Run from the plugin root. Each command is complete; replace only the plugin-specific names.

```bash
# 1. Manifest parses and the name is valid
jq -e '.name | test("^[a-z][a-z0-9]*(-[a-z0-9]+)*$")' .claude-plugin/plugin.json

# 2. Nothing but the manifest inside .claude-plugin/
[ "$(ls -A .claude-plugin | grep -v '^plugin.json$' | wc -l)" -eq 0 ] && echo OK || echo "components nested under .claude-plugin"

# 3. Manifest path policy: relative, ./ prefix, no parent, no backslash
jq -r '[.commands,.agents,.hooks,.mcpServers] | flatten | map(select(type=="string")) | .[]' .claude-plugin/plugin.json \
  | grep -vE '^\./[^\\]*$' ; jq -r '.. | strings' .claude-plugin/plugin.json | grep -F '../' ; echo "path policy scan done (no lines above = pass)"

# 4. Every JSON file parses
find . -name '*.json' -not -path './node_modules/*' -print0 | xargs -0 -n1 sh -c 'jq empty "$0" || echo "INVALID: $0"'

# 5. No hardcoded home or user paths, no literal bearer tokens, no plain http/ws endpoints
grep -rnE '(/Users/|/home/[a-z]|~/)' --include='*.json' --include='*.md' --include='*.sh' . ; \
grep -rnE 'Bearer [A-Za-z0-9_\-]{12,}' . ; grep -rnE '"(http|ws)://' --include='*.json' . ; echo "portability/secret scan done (no lines above = pass)"

# 6. Command frontmatter parses (needs python3 with PyYAML)
python3 - <<'PY'
import glob, sys, yaml
bad = 0
for p in glob.glob('commands/**/*.md', recursive=True):
    t = open(p).read()
    if t.startswith('---'):
        try: yaml.safe_load(t.split('---', 2)[1])
        except Exception as e: bad += 1; print('INVALID', p, e)
print('commands checked, invalid:', bad); sys.exit(1 if bad else 0)
PY

# 7. Hook configuration (unwrap top-level "hooks" wrapper if present, then check structure)
jq -e '(if has("hooks") then .hooks else . end) | to_entries | all(.value | type == "array")' hooks/hooks.json

# 8. Hook scripts: syntax check, allow/deny fixture runs, and empty-input resilience
bash -n scripts/*.sh
printf '{"tool_name":"Write","tool_input":{"file_path":"/tmp/test.txt"}}' | bash scripts/validate-write.sh; echo "allow exit: $? (expect 0)"
printf '{"tool_name":"Write","tool_input":{"file_path":"/etc/passwd"}}' | bash scripts/validate-write.sh; echo "deny exit: $? (expect 2)"
echo '{}' | bash scripts/validate-write.sh; echo "empty input exit: $? (must be 0)"

# 9. Settings file: two --- markers, non-empty frontmatter, and gitignored
head -n 1 .claude/my-plugin.local.md | grep -qx -- '---' && echo "frontmatter ok"
git check-ignore -q .claude/my-plugin.local.md && echo "gitignored" || echo "NOT gitignored"

# 9b. Agent files: frontmatter has name, description with <example>, model, and color
for f in agents/*.md; do grep -q '^name:' "$f" && grep -q '<example>' "$f" && echo "PASS $f" || echo "FAIL $f"; done

# 9c. Skill files: exact file name and required frontmatter keys
for d in skills/*/; do f="${d}SKILL.md"; [ -f "$f" ] && grep -q '^name:' "$f" && grep -q '^description:' "$f" && echo "PASS $f" || echo "FAIL $d"; done

# 10. Hookify pattern behaves on a positive and a negative sample
python3 -c "import re; p=r'rm\s+-rf'; print(bool(re.search(p,'rm -rf build')), bool(re.search(p,'npm run format')))"

# 11. Host gates (manual, in a NEW session): /help lists the commands with the plugin label;
#     /hooks lists the hooks; /mcp lists servers and tools; then run:
claude --debug
```

Gate order for a distributed plugin: static (1 to 6), isolated components (7 to 10), host load (11), then positive and negative invocation, denied and partial-permission cases, interruption and resume, clean install from the packaged artifact (in a path containing a space), update, disable, uninstall, host restart, before-and-after resource inventory and residue scan (files, processes, network calls, config changes, retained data), explicit retained-data contract, and clean reinstall. Never weaken an expected result to make a gate pass.

## Anti-patterns

| Anti-pattern | Why it fails | Do instead |
|---|---|---|
| Components inside `.claude-plugin/` | Not discovered | Component directories at plugin root |
| Absolute, `~/`, or `../` paths | Breaks on every other machine | `${CLAUDE_PLUGIN_ROOT}`, `./`-prefixed manifest paths |
| Custom manifest path duplicating a default directory | Registers twice; name conflicts | Rely on defaults; custom paths only for extra locations |
| Treating valid JSON as a valid plugin | Semantics, packaging, discovery untested | Run the gates through host load and clean install |
| Testing only from the source tree | Hides files missing from the package | Install the packaged artifact in a clean profile |
| Blind reinstall after a failure | Mixes artifacts, duplicates registrations, reruns hooks, hides the first failure | Classify the failing phase, rebuild, clear owned state, then retry once |
| Command body written as user-facing prose | Claude receives a description instead of instructions | Imperative directives to Claude |
| `allowed-tools: Bash(*)` or `"*"` | Far more authority than the workflow needs | Filtered scopes such as `Bash(git:*)` |
| Arguments used where a question is needed, or the reverse | Guessing, or friction on scriptable paths | Known values as arguments, contextual choices as questions |
| Agent description without examples, or agent with every tool | Never triggers, or triggers with too much authority | "Use this agent when" plus 2 to 4 examples; minimal `tools` |
| Wrong voice for the surface (first-person agent body, second-person skill body, user-facing command body) | The model misreads who is being addressed | Agent: "You are"; skill: verb-first; command: directives to Claude |
| Skill resources not named in the body, or skill file not named `SKILL.md` | Never loaded or never discovered | Name each bundled file; exact file name |
| Program logic written in Markdown | Untestable and non-deterministic | A tested script called by a thin command |
| Mutating command with no confirmation, lock, or rollback | Partial writes, concurrent runs | Confirmation, versioned state, lock, atomic writes, rollback |
| Broadening access after a denial | Defeats the permission model | Report and stop |
| Hooks that depend on order or shared `/tmp` state | They run in parallel | Independent hooks; session-keyed state only across events |
| Hook crashes on missing input | Exit 1 does not block; the check silently vanishes | Graceful skip, guarded pipelines, explicit exit 0 or 2 |
| Unquoted variables in hook scripts | Injection | Quote everything; validate fields |
| Prompt hook with a broad matcher on a frequent event | Slows every tool call | Narrow matcher, cheap command pre-check, or move to `Stop` |
| Starting a new rule at block | False positives stall work; a blocking `Stop` hook can loop | Warn, then ask, then block after review |
| Too-broad regex (`log`) | Matches unrelated text | Anchor and escape; test positive and negative samples |
| Expecting hook or MCP edits to apply mid-session | Loaded at session start | Restart, then `/hooks`, `/mcp` |
| Literal token in configuration; plain `http://` or `ws://` | Leak; interception | Environment variables; TLS endpoints |
| Wildcard MCP allowlist without a reason | Exposes destructive tools | Exact tool names |
| Per-item MCP query loops | Slow, rate-limited | One filtered query with a limit |
| Logging to stdout from a stdio server | Corrupts the protocol stream | Log to stderr |
| Retrying 401, 403, or validation errors | They are not transient | Fix the cause; retry only rate-limit and network errors |
| Settings file without `.local`, or not gitignored | Committed local state and secrets | `.claude/<plugin>.local.md` plus gitignore entry |
| `sed -i` on a settings file | Torn writes | Temporary file, then `mv` |
| No defaults, no validation of settings values | Hook crashes or misbehaves on hand edits | Default and validate each field |
| Unbounded loop state | Never terminates | Iteration bound, completion check, delete state on every exit |
| Example with decorative components | Teaches unsupported capabilities | Smallest artifact; claims limited to its status level |
| Removal treated as an afterthought | Leaves residue, confusion over retained user data, or a broken reinstall | Before/after resource inventory (files, processes, network, config, retained data), repeatable cleanup that preserves ownership-marked user data under an explicit retained-data contract, host restart, residue scan, and reinstall test |
| Recommending from dependency names | Automation nobody needs | Confirm friction, owner, and exact repository commands |
| Recommendation and implementation in one step | Unreviewed changes | Read-only survey, then authorization |
| Two surfaces owning one behaviour | Double execution, conflicting results | Disable one |
| Ownerless shared automation | Nobody fixes or removes it | Name an owner or pause it |
| `--force` as a retry (Codex scaffold) | Destroys existing plugin files or entries | Inspect, back up, get authorization |
| Carrying Codex fields into a Claude Code manifest or the reverse | Different ecosystems | Keep `.codex-plugin/` and `.claude-plugin/` contracts separate |

## Upstream reference utilities (linked, not bundled)

Third-party helper scripts from the Apache-2.0 Anthropic `plugin-dev` plugin (`validate-hook-schema.sh`, `test-hook.sh`, `hook-linter.sh`, `parse-frontmatter.sh`, `validate-settings.sh`, `validate-agent.sh`, plus example hooks and MCP configs) and the OpenAI Codex `plugin-creator` skill (`create_basic_plugin.py`) are not copied into this repository. See `library/third-party/ATTRIBUTION.md` for upstream links.

If you run those upstream utilities locally, watch for these observed quirks (verified on Linux with bash 5, jq, and python3):

1. `validate-hook-schema.sh` expects the direct events map, not the `{"hooks": ...}` plugin wrapper; unwrap with `jq 'if has("hooks") then .hooks else . end'` first. It also stops at the first error (exit 1), and warnings do not change the exit code.
2. `test-hook.sh` exits 0 even when the hook itself exited 2; assert on the printed `Exit Code:` line.
3. `hook-linter.sh` exits 0 even when reporting warnings; treat its output as review prompts, not a pass/fail verdict.
4. Example `validate-bash.sh` uses a `su*` prefix glob that false-positives on commands like `summarize x` — anchor patterns or use a prompt hook.
5. Example `read-settings-hook.sh` exits 1 (non-blocking, so silently skipped) when a parsed field is absent from frontmatter; add `|| true` to each extraction.
6. `validate-agent.sh` reads only the first line of `description` (multi-line `<example>` blocks trigger a false warning), stops at the first warning/error, and accepts uppercase in `name` despite the lowercase rule.
7. `create_basic_plugin.py` writes `[TODO: ...]` placeholders into `.codex-plugin/plugin.json` and writes `./plugins/<name>` into the marketplace file regardless of `--path`; scan for `\[TODO` before shipping and never pass `--force` blindly.

## Self-check

Before reporting the work as done, answer each line with evidence, not intention.

1. Is the chosen surface the least powerful one that delivers the outcome, and is "no change" recorded as considered?
2. Does the matching contract exist (capability trace, command contract, hook row, MCP map, settings schema, decision record, demonstration record)?
3. Is the manifest alone in `.claude-plugin/`, the name valid, and every path portable?
4. Does every command body address Claude, with minimal frontmatter and the narrowest tools?
4a. Does every agent have a triggering description with examples, least-privilege tools, and a second-person body; does every skill sit at `skills/<name>/SKILL.md` with a third-person trigger description and every bundled file named in its body?
5. Is each hook independent, quoted, bounded by a timeout, graceful on missing input, tested with allow, deny, and empty fixtures, and started at warn or ask?
6. Are MCP secrets in environment variables, endpoints on TLS, tool names exact, and the README complete?
7. Is the settings file named and gitignored correctly, with defaults, validation, atomic updates, and one writer per field?
8. Was the plugin loaded in a new session and seen in `/help`, `/hooks`, `/mcp`?
9. Were negative cases run (neighbouring request, invalid input, denial, cancellation, repeat)?
10. For distribution: clean install, update, disable, remove, residue check?
11. Is every version-dependent claim marked as verified on a named version or as unverified?
12. For each conflict noted in this skill that touched the work, is the selected position and its selecting condition written down?
13. Is there an owner, a rollback, and a retirement trigger?

Deeper tables, worked examples, failure modes, metrics, and source mapping are in [reference.md](reference.md); the root guides [A00-LLM-Principles01.md](../../../A00-LLM-Principles01.md), [A01-LLM-Workflow01.md](../../../A01-LLM-Workflow01.md), and [A03-Executable-Specs01.md](../../../A03-Executable-Specs01.md) cover the general working method.
