# Claude Plugin Development Reference

Depth material for [SKILL.md](SKILL.md). The rules needed to do the work are in the skill; this file adds rankings, trade-off tables, worked examples, failure and retry tables, metrics, and the source mapping.

Labels used throughout: *source-local* means a snapshot states the value and nobody measured it here; *illustrative* means an example value; *proposed* means a target suggested for adoption, not an observed result; **Observed** means the result came from running the bundled files (listed in the skill under "Bundled scripts and assets").

## Idiomatic Thesis Synthesis Statement

A Claude Code extension is a small contract around model behaviour, and the work is choosing the least powerful surface that honours that contract and then proving each link from declaration to removal.

- A plugin is a distribution boundary. Its manifest is a capability index and a trust boundary: each declaration widens what the host loads, starts, or exposes.
- A slash command is an interface: prompt, permissions, package entry point, and user-facing API in one Markdown file addressed to Claude.
- A hook is enforcement at a lifecycle moment. Its cost is matcher hit rate times hook cost, and its failure mode is silence (a crash does not block) or obstruction (a block that loops).
- An MCP server is a service and data boundary with three custodians: the plugin owns configuration shape, the user's shell owns environment secrets, the host owns OAuth tokens.
- A settings file is a hand-edited, single-writer-per-field contract between a user and scripts.
- A plugin agent is a triggering contract (its description and examples) plus a system prompt; a plugin skill is a triggering description plus instructions and bundled resources. Both are selected by the model, so their descriptions are the interface.
- An example is a teaching contract whose claims stop at its evidence status.
- Setup is control-plane design: recommend from observed friction, authorise separately, and keep "no change" in the option set.
- A Codex plugin obeys the same reasoning in a different ecosystem with its own manifest, validator, and marketplace.

Evidence never transfers upward on its own: documented, parsed, discovered, activated, correct, installable, updatable, and removable are eight separate claims.

## Pattern Scoreboard Ranking Table

Ranking is by how often the pattern prevents a real failure and how cheap it is to apply; it is a judgment ordering, not a measured score.

| Rank | Pattern | Applies to | Why it ranks here |
|---|---|---|---|
| 1 | Least powerful surface, with "no change" as an option | All | Prevents the largest class of waste and risk before anything is built |
| 2 | Contract before artifact (trace, command contract, hook row, MCP map, schema table) | All | Makes permissions, effects, and removal explicit while they are still cheap to change |
| 3 | `${CLAUDE_PLUGIN_ROOT}` for every plugin-internal path | Structure, commands, hooks, MCP | The most common portability failure, fully greppable |
| 4 | Restart, then verify in the host (`/help`, `/hooks`, `/mcp`, debug run) | Commands, hooks, MCP | Catches stale-session and registration failures that static checks cannot |
| 5 | Independent hooks with graceful skip and explicit exit 0 or 2 | Hooks | Removes order dependence and silent non-blocking crashes |
| 6 | Warn, then ask, then block | Hooks, hookify | Contains false positives; avoids blocking loops |
| 7 | Exact tool allowlists and filtered Bash scopes | Commands, MCP | Least privilege with a one-line change |
| 8 | Secrets from environment, TLS endpoints only | MCP | Greppable; prevents leaks |
| 9 | Quick-exit, default, validate, atomic update | Settings | Keeps hand-edited files from crashing hooks |
| 10 | Clean install of the packaged artifact, then update, disable, remove | Distribution | The only evidence for lifecycle claims |
| 11 | Prompt hook for intent, command hook for deterministic checks, hybrid for both | Hooks | Matches mechanism to rule type |
| 12 | Arguments for known values, questions for contextual choices | Commands | Removes guessing and needless friction |
| 13 | Thin command over a tested script when logic dominates | Commands | Moves determinism out of Markdown |
| 14 | Inspect before scaffold; `--force` only with inventory and authority | Codex | Prevents destructive overwrite |
| 15 | Fresh-task replay after install or update | Codex | Catches stale cache and same-task false greens |
| 16 | Evidence status ladder on every example | Examples | Stops decorative claims |
| 17 | Session-keyed state only across sequential events | Hooks | Narrow but prevents subtle races |
| 18 | Namespacing command families | Commands | Matters only once collisions are plausible |
| 19 | Triggering description with concrete examples and a stated non-use | Agents, skills | Decides whether a model-selected component is ever used, or used wrongly |
| 20 | One voice per surface (command directives, agent second person, skill verb-first, skill description third person) | Commands, agents, skills | Cheap to check; prevents misaddressed prompts |

## Agent Usage Decision Guide

### Choosing among surfaces

Ask in this order and stop at the first "yes":

1. Does existing tooling or documentation already produce the outcome? Then change nothing, or document.
2. Is it a one-off? Then do it by hand.
3. Must it happen automatically at a lifecycle moment? Hook (hookify first when personal and regex-expressible).
4. Is it an explicit, repeatable, bounded workflow with nameable inputs? Slash command.
5. Is it knowledge, a template, or a script the model should pull in when relevant? Skill.
6. Is it a separable analysis needing its own context or tools? Subagent.
7. Does it need structured access to an external service that has an owner and a credential scope? MCP server.
8. Do several of these need to ship and version together, or be standardised across a team? Plugin.

### Setup branch table

| Branch | Minimum evidence | Avoid when |
|---|---|---|
| No change | Existing commands and docs suffice | Friction is repeated and measured |
| Hook | Bounded deterministic rule, exact repository command known, rollback is "remove the entry" | The rule needs judgment nobody has written down; no owner |
| Skill | Repeated prompts or templated work | It would hide side effects |
| Subagent | Independent specialist task; reviewer does not grade its own work | Fan-in cost exceeds the benefit |
| Plugin | A maintained bundle removes duplication | One local component suffices |
| MCP | Necessary service boundary, least-privilege scope, read-only probe, retention rule | Owner or credential scope is unknown |

Lifecycle states for a setup item: proposed, adopted, observed, narrowed, paused, replaced, rejected, retired.

### Ten-step choice sequence for setup

Frame the outcome and prohibitions; capture the unchanged baseline; classify evidence (fact, guidance, lead, inference, untrusted, authority); pick the least powerful adequate surface; design authority before behaviour; define success, silence, denial, missing-prerequisite, failure, and restoration cases; validate reversibly; observe duplication, noise, latency, and maintenance; then expand, narrow, replace, or remove; record the decision.

### Usage modes for an example plugin

Primary skill demonstration; companion to another surface; package lifecycle exercise; integration exercise; promotion candidate; orientation only; or "avoid as primary" when the request is really about a command, hook, or server. Re-route when a script starts executing, the skill gains a command or hook, a mock becomes live, credentials appear, a wrapper is added, another project copies it, or ownership changes.

### Codex creator decisions

New or update; plugin or standalone component; personal or shared destination; which components; marketplace entry or not; replace or preserve on collision. For each, the default is the narrower, reversible option, and the shared or destructive option needs an explicit request.

### Routing vocabulary

Stay (the request is inside this subject), Route (it belongs to an adjacent skill), Compose (both are needed; hand over a packet stating outcome, constraints, evidence so far, and open questions), Stop (authority, ownership, or safety is unresolved).

## Decision Tradeoff Guide

| Decision | Option A | Option B | Select A when | Select B when |
|---|---|---|---|---|
| Hook mechanism | Prompt hook | Command hook | Rule is about intent, many surface forms, explanation useful | Check is arithmetic, deterministic, or an external tool's verdict; latency matters |
| Hook system | Hookify rule | Plugin hook | Personal, one project, regex suffices, want immediate effect | Team distribution, versioning, judgment or scripts needed |
| Hook default posture | Prompt first | Determinism first | General development projects | Security-critical repositories that want reviewed patterns |
| Enforcement level | Warn or ask | Block | New rule, unknown false-positive rate | Reviewed rule with a stable record |
| Hook toggle | `enabled` in settings | Flag file | Long-lived, user-visible configuration | Quick temporary switch |
| MCP config location | Root `.mcp.json` | Inline `mcpServers` | Several servers, separate maintenance | One simple server, single-file plugin |
| MCP transport | stdio | Hosted (SSE, HTTP, WebSocket) | Local tools, bundled server | Hosted service, OAuth, always-on, push |
| MCP auth | OAuth | Token header | Service offers it | Service offers only tokens; headless use |
| Command tool access | Exact list | Wildcard | Almost always | Admin command that needs every tool, reason recorded |
| MCP consumer | Command | Agent | User-driven, one or two calls, validation | Multi-step autonomous workflow |
| Command input | Arguments | Questions | Known values, scripting | Contextual choices, trade-offs to explain |
| Command logic | Markdown directives | Script behind a thin command | Judgment and synthesis | Deterministic mechanics, state, recovery |
| Settings absence | Skip | Defaults | Opt-in behaviour | Always-on behaviour with tunables |
| Settings parser | `sed` and `grep` | `yq` or Python | Flat scalars | Lists, nesting |
| Loop off-switch | File existence | `enabled` field | Short-lived loop state | Long-lived configuration |
| Mutable data | Project `.claude/` | Under the plugin root | Anything a user would miss | Disposable cache, root confirmed writable |
| Plugin shape | One coherent plugin | Split plugins | One domain, one owner | Independent release or permission domains |
| Command layout | Flat | Namespaced | Few commands, private | Collision risk, distributed, many commands |
| Agent model | `inherit` | Named model | Almost always | The agent needs a specific capability or must be cheap and fast |
| Agent tools | Explicit minimal list | Omitted (all tools) | Almost always | A generalist agent whose work cannot be bounded, reason recorded |
| Agent creation | Generated from a request, then edited | Manual | A first draft is wanted quickly | The triggering examples need careful control |
| Skill body size | Lean body, detail in references | Complete body | Context is contested and references load reliably | The skill must work as the only loaded file |
| Skill resource | Script | Reference or asset | Deterministic or repeatedly rewritten code | Knowledge to read (reference) or files used in output (asset) |
| Example scope | Skill only | Multi-surface | Teaching triggering and structure | A demonstrated responsibility needs the extra surface |
| Codex destination | Personal | Repository or team | Default | Explicit request and authority |

Surface trade-offs for setup: a manual command is cheap but undiscoverable; documentation does not enforce; hooks act immediately but can block or recurse; skills make invocation and side effects less visible; subagents add fan-in and evaluation cost; plugins add a bundle and update dependency; MCP adds a service and data boundary. Least powerful is the default, not dogma. Coherence of the whole portfolio matters more than the quality of any single item.

Example-plugin boundaries to hold: skill versus command; guidance versus execution; mock versus live service; local versus packaged; single host versus several; teaching artifact versus template; read-only versus mutating; one trigger family versus broad triggers; static evidence versus runtime evidence; author convenience versus learner transfer (moving effort to the learner is not simplification).

## Theme Specific Artifact

### Compatibility matrix (distributed plugin)

One row per tested combination. Columns: package hash; plugin version; host version; platform; install method; manifest fields used; default and custom paths; packaged files; expected components; observed discovery and activation; dependencies; effects; diagnostics; update migration; disable; removal. Each cell names its fixture and pass condition. A local plugin needs only a single-environment record.

### Command contract packet

```yaml
command: review-changes
purpose: Review uncommitted changes against the team rubric.
non_goals: [fixing code, committing]
surface_rationale: user-triggered, bounded, repeatable; not automatic, so not a hook
file: commands/review-changes.md
namespace: none
frontmatter: {description: "...", argument-hint: "[focus-area]", allowed-tools: "Read, Grep, Bash(git:*)"}
input_grammar: "optional single token; empty means everything"
questions: none
tools: [Read, Grep, "Bash(git:*)"]
plugin_resources: none
scripts: none
effects: read-only
state: none
confirmations: none
errors_recovery: "GIT_FAILED sentinel -> explain and stop"
tests: [no-arg, valid arg, not a git repo, denied Bash]
documentation: HTML comment block in file; README entry
compatibility: "verified on host version <fill>"
removal: delete file; no residue
```

### Hook lifecycle record

Seven core fields (event, matcher, hook type, timeout, output contract, escalation level, test evidence) plus bypass policy, safety constraints, log location, review cadence, and debug workflow. Example row: `Stop | * | prompt | 30 s | decision + reason | block | fixture and debug run`.

### MCP boundary map

| Server | Transport | Auth | Env vars | Tools confirmed in `/mcp` | Consumers | Permission model | Failure recovery |
|---|---|---|---|---|---|---|---|
| `db` | stdio | env | `DATABASE_URL` | `query`, `describe` | `/db-report` | exact allowlist | report connection error, suggest checking variable |
| `tracker` | SSE | OAuth | none | `search_tasks`, `create_task` | `/sync`, status agent | exact allowlist for command | re-authenticate; at most three retries on 429 |

### Settings schema table

| Field | Type | Default when absent | Validation | Consumer | Writer | Migration |
|---|---|---|---|---|---|---|
| `enabled` | boolean string | skip (opt-in) | `true` or `false` | every hook | setup command, user | none |
| `mode` | enum | `standard` | `strict`, `standard`, `lenient` | write guard | user | none |
| `max_iterations` | number | `0` = unlimited | `^[0-9]+$` | stop hook | setup command | none |
| `iteration` | number | `0` | `^[0-9]+$` | stop hook | stop hook only | none |

Fields such as `iteration` or `pr_number` need a named writer. A renamed field or file silently orphans old files; record the migration.

### Claude Code setup decision record

```yaml
status: proposed   # proposed | paused | rejected | authorized | trialing | adopted | disabled | replaced | retired
signal: "3 of the last 10 review handoffs omitted lint or tests (illustrative)"
unchanged_baseline: "current npm scripts, CI workflow, docs, manual checklist; counterfactual if unchanged: omissions stay ~30%"
outcome: "review handoffs include lint and affected-test results"
selected_surface: user-invoked review skill
rejected: [Stop hook (would block unrelated work), subagent (no separable context needed)]
overlap_and_dependencies: "calls repo lint/test scripts; CI runs independently; no other hook or skill owns review prep"
configuration: ".claude/skills/review-prep/SKILL.md, disable-model-invocation: true"
owner: "<team or person>"
invocation: "/review-prep"
tools_scopes: "Read, Grep, Bash(<repo lint cmd>), Bash(<repo test cmd>); no writes, network, credentials, commit, push"
failure_model:
  - trigger: "missing script or denied Bash"
    signal: "non-zero exit or permission denial"
    containment: "report failure and stop without mutating files"
    recovery: "run repo commands manually"
    escalation_owner: "<team or person>"
positive_cases: ["changed TS file -> lint + affected test reported"]
negative_cases: ["docs-only change -> no test run", "denied Bash -> reports and stops", "missing script -> says so"]
gate: "exact repository lint, test, and format-check commands exit 0 on the trial branch"
rollout: "disabled by default; trial on one feature branch for 1 week; enabled by repo owner; disable by removing skill dir; restores manual checklist"
rollback: "delete the skill directory"
unresolved_questions: []  # each entry: {question, owner, evidence_source, resolution_gate}
retirement_trigger: "handoff omissions stay at zero without the skill, or ownership lapses"
version_assumption: "<host version>"
```

Sizing rule: use the full schema for shared, automatic, side-effecting, externally connected, security-sensitive, or hard-to-remove setup. A reversible personal preference may use a short record (outcome, baseline, candidate, authority, verification, disable path). Split the record when two candidates cross different ownership, credential, production, or data boundaries.

### Setup candidate catalogue (snapshot roster; every name must be re-checked before it is recommended)

Hook detection details:

| Detected | Candidate hook |
|---|---|
| `.prettierrc*`, `prettier.config.js` | `PostToolUse` on `Edit|Write`: format |
| `.eslintrc*`, `eslint.config.js` | `PostToolUse`: lint with auto-fix |
| `pyproject.toml` with black or isort, `.black`, `setup.cfg` | `PostToolUse`: format Python |
| `ruff.toml`, `[tool.ruff]` | `PostToolUse`: lint and format |
| `go.mod` / `Cargo.toml` | `PostToolUse`: `gofmt` / `rustfmt` |
| `tsconfig.json`; `mypy.ini`, `pyrightconfig.json` | `PostToolUse`: `tsc --noEmit`; type check |
| Jest configuration, `__tests__/`, `*.test.ts`, `*.spec.ts`; pytest configuration, `tests/`, `test_*.py` | `PostToolUse`: run related tests; pytest on changed files |
| `.env*`, `credentials.json`, `secrets.yaml`, `.git/` | `PreToolUse` on `Edit|Write`: block (secret exposure, repository corruption) |
| Lock files | `PreToolUse`: block direct edits |
| Security-sensitive code | `PreToolUse`: require confirmation |
| A user who multitasks | `Notification` hooks: `permission_prompt` (a tool needs permission), `idle_prompt` (waiting for input; the snapshot says after 60 seconds idle, source-local), `auth_success`, `elicitation_dialog` (an MCP tool needs input); actions such as a sound (`afplay /System/Library/Sounds/Ping.aiff` on macOS), a desktop notification (`osascript -e 'display notification ...'`), or a log line |

MCP servers by need (named at snapshot time):

- Documentation and knowledge: context7, when the project uses popular libraries or SDKs (frontend frameworks, Express, FastAPI, Django, Prisma, Drizzle, Stripe, Twilio, SendGrid, cloud SDKs, LangChain, OpenAI or Anthropic SDKs); the stated benefit is current documentation instead of invented or outdated APIs.
- Browser: Playwright (component testing, end-to-end, visual regression, debugging UI, forms); Puppeteer (PDF from HTML, scraping, headless CI).
- Database: Supabase (`@supabase/supabase-js`; auth, database, realtime); PostgreSQL (`pg` or `postgres` dependency; raw queries, migrations, analysis, data debugging); Neon; Turso; MySQL.
- Version control and tracking: GitHub (GitHub remote, issue-driven work, PR workflows, Actions, releases); GitLab; Linear (issue references such as `ABC-123`, sprint planning, issues from TODOs).
- Cloud: AWS (`@aws-sdk/*`, Terraform, CDK, SAM, Lambda, S3, DynamoDB); Cloudflare (Workers, Pages, R2, D1); Vercel.
- Monitoring: Sentry (`@sentry/*`; production debugging, error grouping, release correlation); Datadog (APM, logs, metrics).
- Communication: Slack (webhook URLs present; notifications, deploy alerts, incident updates); Notion (documentation, knowledge-base search, meeting notes).
- Files and data: Filesystem (batch operations, watching, advanced search); Memory (long projects, preferences, patterns).
- Containers: Docker (compose, Dockerfile, logs, exec); Kubernetes (manifests, Helm, pod debugging).
- Research: Exa (web research).
- Scopes: project `.mcp.json` (that directory); user-global `~/.claude.json` (all projects); a checked-in `.mcp.json` for team sharing. Prerequisites sometimes needed: the `gh` CLI, a Playwright or Puppeteer install.

Plugins named at snapshot time: plugin-dev (skills for skill, hook, command, and agent development, MCP integration, plugin structure), pr-review-toolkit, code-review, code-simplifier, feature-dev, commit-commands (commit; commit, push, and open a PR), hookify, frontend-design, explanatory-output-style, learning-output-style, security-guidance; language-server plugins typescript-lsp, pyright-lsp, gopls-lsp, rust-analyzer-lsp, clangd-lsp, jdtls-lsp, kotlin-lsp, swift-lsp, csharp-lsp, php-lsp, lua-lsp. Signals: PR workflow gives pr-review-toolkit; TypeScript, Python, Go give the matching language-server plugin; security-sensitive code gives security-guidance; onboarding gives explanatory-output-style; general productivity gives the anthropic-agent-skills bundle; document workflows give docx, xlsx, and pdf skills; frontend work gives frontend-design; building AI tools gives mcp-builder. Commands: `/plugin install <name>`, `/plugin list`, `/plugin info <name>`. Recommend installing a plugin when the user wants ready-made automation from an official or shared marketplace, needs several related capabilities, wants team-standard workflows, or is setting up for the first time.

When each surface fits (setup view): MCP for external service integration, library documentation lookup, browser automation, team tools, cloud infrastructure. Skills for documentation generation, repeated prompts and workflows, project tasks with arguments, templates and scripts, quick `/name` actions, isolated runs. Hooks for repetitive post-edit actions, protection rules, validation checks. Subagents for specialised expertise, parallel review, background quality checks. Plugins for several related skills, pre-packaged bundles, team-wide standardisation. The recommender may go beyond fixed lists by searching for tools specific to the repository's own frameworks.

Project skill frontmatter at snapshot: `name`, `description`, `disable-model-invocation`, `user-invocable`, `allowed-tools`, `context: fork` (run in an isolated subagent), `agent: Explore` (agent type used when forked). Arguments: `$ARGUMENTS` in the body; when the body does not mention it, the arguments are appended as `ARGUMENTS: <value>`. An exclamation mark with a backticked command injects command output before Claude sees the content.

Custom project skill sketches:

| Skill | Invocation | Bundled file | What it does |
|---|---|---|---|
| `api-doc` | User and Claude | OpenAPI template | Read an endpoint, extract path, method, parameters, schemas; fill the template; output YAML |
| `create-migration` | User only | Validation script | Timestamp-prefixed migration with up and down; run validation; report |
| `gen-test` | User only | Example tests | Generate tests in the project's style |
| `new-component` | User only | Component, test, and story templates with `{{ComponentName}}` and `{{component-name}}` placeholders | Scaffold a component |
| `pr-check` | User only, `context: fork` | Checklist (tests added, no stray console logging, user-facing error messages, backward-compatible API, reversible migrations) | Inline `gh pr diff` and `gh pr view`, then check |
| `release-notes` | User only | none | Inline `git log $(git describe --tags --abbrev=0)..HEAD --oneline`; group by type; user-friendly wording; call out breaking changes |
| `project-conventions` | Claude only | none | Naming, patterns, forbidden constructs as background knowledge |
| `setup-dev` | User only | Prerequisites script | Install dependencies, copy the env template, set up the database, run tests |

Subagent sketches (placed in `.claude/agents/`; each has its own context window and tools and can run in parallel):

| Agent | Signal | Model at snapshot | Tools |
|---|---|---|---|
| code-reviewer | Large codebase | sonnet | Read, Grep, Glob, Bash |
| security-reviewer | Paths or names matching auth, login, session, stripe, payment, billing, user, profile, PII | sonnet | Read-only, for safety |
| test-writer | Few tests relative to source | sonnet | Read, Write, Grep, Glob |
| api-documenter | Route files, `.graphql`, `openapi.yaml`, `swagger.json` | sonnet | Read, Write, Grep, Glob |
| performance-analyzer | ORM or raw SQL, hot paths, complaints, nested loops; looks for N+1 queries, quadratic work, leaks | sonnet | Read, Grep, Glob, Bash |
| ui-reviewer | `components/`; accessibility, UX, responsiveness | sonnet | Read-only |
| dependency-updater | `npm outdated`, `npm audit` findings; incremental updates with testing | sonnet | Read, Write, Bash, Grep |
| migration-helper | Old framework, deprecations | opus | Full |

Model guide stated by the snapshot: haiku is fast and cheap but less thorough; sonnet is the default; opus is thorough, slower, and costlier.

### Demonstration contract record

Goal; observable success; non-goal; accidental-activation consequence; surface; permissions; effects; recovery; status (Conceptual, Source-valid, Host-loaded, Behavior-validated, Integrated, Packaged or promoted) with the claims that status forbids; commands run; observations; assumptions; one rejected design; owner; refresh triggers.

### Codex plugin lifecycle decision record

```yaml
plugin: my-plugin            # normalized name
route: plugin                # or standalone skill / app / mcp / hook / script / instruction
mode: new                    # new | update
destination: personal        # personal | repository | team (explicit request required for shared)
authority: "<who approved writes here>"
collision_check: {normalized_name: clear, path: clear, marketplace_entry: clear}
components: [skills]
companions: {mcp_json: n/a, app_json: n/a, assets: n/a}
metadata_truthful: pending
validator: pending           # verified | pending | not_observed | not_applicable_with_reason | blocked
marketplace: {name: "<read from file>", entry_appended: pending, unrelated_entries_unchanged: pending}
install: pending
fresh_task_pickup: pending
component_behaviour: pending
update_path: "cachebuster then reinstall"
recovery: "prior version and source mapping preserved at <location>"
status: pending              # passed | failed | blocked | pending_owner | not_observed | not_applicable | stale
```

Status rules:

- Never record `passed` for a command that returned exit code 0 unless its postcondition was also inspected.
- Never record `not_applicable` for installation merely because installing was inconvenient; use `not_observed` or `pending_owner` when runtime completion is still part of the desired outcome.
- `pending_owner` means the next stage belongs to another accountable party; record the owner, the handoff artifact, the acceptance question, and the expected response.
- A `stale` result is incomplete until refreshed or removed from the final claim.

## Worked Example Set

Grading rubric used below: **Good** = current evidence, proportionate authority, and a replayable failure, rollback, and lifecycle path; **Bad** = a material evidence, authority, data, behaviour, or recovery gate is crossed; **Borderline** = the candidate stays contained, with an owned route to resolution and a safe interim workflow.

### Structure

- Good: one manifest plus `skills/<name>/SKILL.md`; nothing else.
- Bad: every component inside `.claude-plugin/` with absolute local paths.
- Borderline: categorised commands in subdirectories; acceptable only when packaged, conflict-tested, and documented.
- Good split: a security-enforcement plugin and a documentation plugin shipped separately. Bad: one plugin that auto-starts unrelated servers and hooks.

### Commands

- Good: `/review-pr 123` takes a known PR number, gathers bounded context, applies a rubric, cites evidence. `/summarize-diff` is read-only with a filtered Bash scope.
- Bad: `/deploy` that mutates production silently with unrestricted Bash and no confirmation.
- Borderline: `/setup-service`, acceptable only with validated choices, atomic writes, a restart reminder, rollback, and clean uninstall.
- Manual-only approval command: `disable-model-invocation: true`; lists the checks (tests passed, security scan clean, stakeholder approval, rollback plan) and proceeds only after the user types an explicit confirmation word.
- Stateful family: `/deploy-init` writes `.claude/deploy-state.local.md` (branch, commit, timestamp, `status: initialized`) and names the next command; `/deploy-test` reads it, runs tests, sets `tested`; `/deploy-build`, `/deploy-execute` continue; a cleanup command removes state and lock. A complete family is four commands: init, validate, execute, cleanup.
- Environment-aware: `argument-hint: [dev|staging|prod]`, body loads `@${CLAUDE_PLUGIN_ROOT}/config/$1.json`, then runs smoke tests.
- Interactive launch: if no task-list argument is given, ask agent count, task-definition approach (guided or file), and coordination mode; guided mode collects tasks iteratively, then writes the task list.
- Pattern set: review (read tools plus git, inline changed files, rubric); testing (run tests for `$1` inline, analyse); documentation (`@$1`, list of parts to produce); workflow (`gh pr view $1`, then steps); multi-script (build, test, package through plugin scripts); pipeline (collect, categorise, prioritise, plan); parallel checks with one combined summary.

### Hooks

- Incident path: an accidental `rm -rf` leads to a hookify warn rule (`rm\s+-rf`), reviewed for a period, then a plugin `PreToolUse` hook on `Bash` at ask level.
- Good: a short allow-list command hook plus a prompt hook on the same matcher; a path-validation cache with a short lifetime private to one hook.
- Bad: a 15-second prompt hook on every `Bash` call; a script that greps only the literal `rm -rf`; state passed between parallel `PreToolUse` hooks through a temp file.
- Borderline: three cheap parallel checks on `Write`; flag-file activation (the script must already be registered, which is restart-bound).
- Cross-event: `SessionStart` initialises counters keyed by session id; `PostToolUse` increments when a Bash call ran tests; `Stop` blocks when the counter is zero; `SessionEnd` cleans up.
- Migration from command to prompt: substring test for `sudo` becomes "check for privilege escalation (sudo, su, and similar)"; an extension regex becomes "not writing credential files (.env, secrets, keys, tokens)"; several conditions become a numbered criteria list ending "deny if any fail". Migrate one hook at a time and confirm the prompt hook still catches everything the script caught, plus the edge cases it missed. Then document it and remove the old script.
- Keep as command hooks: a file-size ceiling using `stat` (the snapshot's 10 MB is illustrative), a scanner whose exit status is the verdict, a trivial allow-list.
- External integration from command hooks (chat webhook, database log, metrics push): keep them short and never let them block.
- Rate limit example: deny after ten commands in a minute (illustrative); needs locking to be correct across parallel runs.
- Secret detection: a regex over written content for key, password, secret, or token followed by a long token string.

### MCP

- Good: a bundled filesystem server through `npx` over stdio; a hosted tracker over SSE with OAuth and no auth block; two exact tool names in the command.
- Bad: a hardcoded bearer token over plain HTTP; an inline block with an absolute home path.
- Borderline: a wildcard allowlist on an admin command, with the reason recorded.
- Mixed: a local SQLite server over stdio plus a hosted tracker over SSE in one plugin.
- Development and production switch: `"url": "${API_URL}"`, with localhost only in development.
- Error message, good: "Could not create the task. Check that you are signed in, that you can access the workspace, and that the project exists." Bad: "tool returned 403".

### Settings

- Coordination file (multi-agent swarm example): written once per agent worktree by a launcher, read many times; fields such as `agent_name`, `task_number`, `pr_number`, `coordinator_session`, `enabled`, `dependencies`; body holds the task, requirements, success criteria. A `Stop` hook notifies the coordinator through `tmux send-keys`; check the session exists first. Lists may stay unparsed strings there.
- Loop file (ralph-loop example): `iteration`, `max_iterations`, `completion_promise`; the body is the prompt; the `Stop` hook quick-exits when the file is absent, ends the loop at the bound or when the last assistant text contains the promise inside `<promise>` tags, otherwise increments atomically and emits `{"decision": "block", "reason": <body>, "systemMessage": "iteration N"}`.
- Comparison: the first is long-lived configuration toggled by `enabled`; the second is short-lived state whose existence means active and which the hook deletes.
- Config-driven validation: `validation_level` (strict, standard, lenient) through `case`, `max_file_size`, `allowed_extensions`, `enable_logging`.

### Agents and skills

- Good agent: `diff-reviewer` with a description containing one reactive and one proactive example, read-only tools, and a body with responsibilities, process, quality standards, output format, and edge cases.
- Bad agent: `helper`, description "Helps with code", no examples, all tools, body in the first person.
- Borderline agent: all tools omitted for a migration agent; acceptable with the reason recorded and an explicit authorization step in its process.
- Good skill description: third person with quoted trigger phrases and named events. Bad: "Provides guidance for working with hooks."
- Planning skill contents from examples: repeated PDF rotation gives a script; the same web boilerplate gives a template asset; rediscovered table schemas give a schema reference; repeated hook validation gives validator and tester scripts plus a patterns reference.
- Good skill layout: a focused body plus `references/patterns.md` and `references/advanced.md`. Bad: one unstructured 8,000-word body (illustrative figure) with nothing split out and nothing named.

### Setup

- Review preparation: the decision record above.
- Formatting: adopt an automatic post-edit format hook only when the owner requires deterministic formatting, an existing formatter command is authoritative, automatic execution is approved, and the installed environment confirms the selected event. Run it first as a disabled trial proving six things: narrow matcher scope, idempotence (a second run changes nothing), bounded runtime, visible failure, no recursive activation, and one-step disable. Adopt only for the proven file scope, keep CI as independent enforcement, observe latency and false activation, and assign an owner for command or event drift.
- Migration: an old framework with deprecations gives a migration-helper subagent with broad tools and incremental testing, under explicit authorization.
- Plugin: several related skills used by a team give a maintained plugin; inventory its components and test removal before recommending.
- Issue context through MCP: tracker references in commits give a tracker MCP candidate; it stays a research item until owner, scope, read-only probe, and retention rule exist.
- Production or security change: binary gates apply; route to the owner.

### Codex

- Minimal personal plugin: one skill, personal destination, marketplace entry appended, fresh-task test.
- Existing-plugin update: prove the source, preserve the prior version, run the cachebuster once, reinstall, check the listing, test in a fresh task.
- Standalone component: the request needs only a skill; do not wrap it.
- Team plugin: explicit request, authority recorded, unrelated marketplace entries and order unchanged.
- Bounded team handoff: repository-owned source validates and component tests pass, but the operator cannot reach marketplace configuration. Record the distribution gate as `pending_owner`, naming the platform administrator and the entry/source-target assertion they must verify; record installation and fresh-task invocation as `not_observed`. The final claim is "team plugin source validated and ready for marketplace review", never "team plugin installed".
- Unknown collision: a normalized name already exists; leave state untouched and let the owner choose reuse, update, replacement, or a new identity.
- Bad shortcut: rerunning the scaffold with `--force` to "see if it works".

### Examples

- In scope: "show me the structure of a focused plugin skill"; "help me write a skill description that triggers correctly".
- Out of scope for a skill-only example: "deploy a GitHub MCP server"; "add a repository hook".
- A one-file ASCII tree is enough to illustrate a skill-only example.
- Clean-removal lifecycle: treating removal as an afterthought leaves residue, confusion about retained data, or a broken reinstall. A clean-removal claim requires disable, uninstall, host restart, a before-and-after resource inventory (files, processes, network calls, configuration changes, retained data), residue scan, a repeatable cleanup that never deletes ownership-marked user data under an explicit retained-data contract, partial-permission and denied-permission cases, and a clean reinstall.

## User Journey Scenario

### Building a plugin with a guard hook and a review command

1. A developer loses work to an edit of `.env`. They write a hookify warn rule for file events on `\.env$`, and it starts working on the next tool use.
2. After a week the rule has fired correctly and never wrongly. The team wants it for everyone, so it becomes a plugin: manifest, `hooks/hooks.json` in the wrapper form, `scripts/validate-write.sh` adapted from the upstream example hook.
3. Static gates pass. The fixture test shows exit 2 for `.env` and exit 0 for an ordinary file and for empty input.
4. They restart, see the hook in `/hooks`, and watch it register in the debug log. The first attempt fails because the matcher was written `write`; matchers are case-sensitive.
5. They add `/review-changes`, check `/help` for the plugin label, run it with and without an argument and outside a git repository.
6. A teammate wants to switch the guard off in one project. A settings file with `enabled` is added; the hook quick-exits when the file is absent, and the README documents the gitignore entry and the restart note.
7. Before sharing, they install the packaged artifact into a clean profile under a path containing a space, then update, disable, and remove it and check that no files remain.

### Adding an MCP server

Hosting first (local or hosted), then configuration method and transport, then authentication, restart, `/mcp`, expose exact tools to commands, test error cases (missing auth, invalid parameters, server down, rate limited), and finally document variables in the README. The first OAuth use needs a browser; a headless environment needs a documented manual step.

### Settings rollout

Schema and defaults, README template, gitignore entry in the user's project, quick-exit parsing, validation with defaults, documented update procedure, restart reminder.

### Setup survey

A TypeScript repository's review handoffs omit lint or tests (3 of the last 10; illustrative). The survey finds real `lint`, `test`, and `format:check` scripts. The candidate is a user-invoked review-prep skill with no writes, network, credentials, commit, or push. Failure cases are listed up front: script missing, tests flaky, Bash denied, docs-only change. One happy path is not accepted as evidence.

### Codex journeys

Personal installable skill; stale existing plugin update; team handoff; unknown collision; standalone skill instead of a plugin; and the bad shortcut (force and same-task testing) that produces a false green.

## Anti Pattern Registry Table

The skill's anti-pattern table lists the patterns and corrections. This registry adds the detector and the symptom.

| Area | Anti-pattern | Static detector | Runtime symptom | Bounded correction |
|---|---|---|---|---|
| Structure | Wrong manifest placement; components under `.claude-plugin/` | `ls -A .claude-plugin` | Nothing discovered | Move to plugin root |
| Structure | Invalid or stale fields | Schema check against current docs | Load warning or silent ignore | Remove unused fields |
| Structure | Absolute or parent paths | grep for `/Users/`, `/home/`, `~/`, `../` | Works only on the author's machine | Plugin-root variable; `./` paths |
| Structure | Duplicate registration | Compare custom paths with defaults | Name conflict error | Restore defaults |
| Structure | Missing targets; undeclared capabilities | Inventory declared versus packaged | Missing or unexpected components | Include files; declare or delete |
| Structure | Name collisions | List names across installed plugins | Conflict error or shadowing | Prefix or namespace |
| Structure | Embedded secrets | Secret scan | Leak on publish | Environment variables; rotate |
| Structure | Source-only validation | No packaged-install record | Clean install fails | Build and install the artifact |
| Command | Wildcard tools; unchecked `$1`; hardcoded paths | Frontmatter and body review | Unneeded approvals; wrong targets | Narrow tools; validate; plugin root |
| Command | Opaque state; partial writes; unconfirmed mutation | Look for state files without schema, locks, or confirmation | Stale locks; half-finished workflows | Versioned state, lock, atomic write, confirmation, rollback |
| Command | Hook-command recursion | Trace what the command triggers | Loop | Break the cycle; idempotent command |
| Command | Agent tools without budgets; skills used as automation | Review integration text | Runaway work; nothing happens automatically | Budget; use a hook for automation |
| Agent | No examples in description; generic name; all tools; first-person body | `scripts/validate-agent.sh`; review `tools` | Never selected, or selected with excess authority | Add examples; rename; minimal tools; second person |
| Skill | Vague description; wrong file name; unreferenced resources; second-person body | Frontmatter grep; file listing versus names in body | Never triggers; resources never loaded | Quoted trigger phrases; `SKILL.md`; name each file |
| Hook | Order dependence; exceeded timeout; crash on missing input; unquoted variables; hardcoded paths | Linter; fixture with `{}` | Intermittent or silent failure | Independence; budget; graceful skip; quoting; variables |
| Hook | Too-broad regex | Positive and negative samples | Fires on unrelated text | Anchor and escape |
| MCP | Committed token or `.env`; plain `http`/`ws`; wildcard allowlist; absolute path; per-item loop | grep | Leak; interception; over-exposure; slow | Variables; TLS; exact names; plugin root; filtered query |
| Settings | Hardcoded paths; unquoted variables; `sed -i`; missing defaults; `sed` range for body | grep; ShellCheck | Torn file; crash on hand edit | Atomic update; defaults; `awk` counter |
| Setup | Context-free summary; unsourced "current" claims; unverified instruction | Check each claim for a source | Wrong recommendation | Re-survey; label evidence |
| Setup | Dependency-name matching; unverified catalogue | Ask for the friction | Unused automation | Remove; confirm need |
| Setup | Blocking or recursive hook | Review matcher and command | Stalled work | Disable; narrow matcher; idempotent command; timeout; explicit fail-open or fail-closed policy |
| Setup | Secret or path exposure; over-broad MCP | Scope review | Data leaves the boundary | Revoke; redact; read-only scopes; denied-action tests |
| Setup | Opaque plugin; overpowered or self-grading subagent; unsafe skill script | Inventory components; review tools | Unexplained effects | Test removal; narrow tools; separate reviewer |
| Setup | Divergent team configuration; ownerless setup | Compare checked-in and local config | Different behaviour per person | Converge; name an owner or pause |
| Codex | Force overwrite; speculative companions; untruthful metadata; wrong marketplace source; same-task test | Diff review; `[TODO` grep | Lost files; false green | Snapshot; remove extras; correct metadata; fresh task |
| Example | Decorative components; broad trigger words; copied historical frontmatter | Compare claims with status | Learners copy unsupported capability | Trim to one goal |

Stop order when several problems are present in an example: secrets or destructive effects, excess permission, automatic invocation, residue, host mismatch, overlap, unreachable files, cosmetic complexity.

## Verification Gate Command Set

The runnable gates are in the skill under "Quality gates". Additional commands and orderings:

```bash
# Hook script by hand, without the bundled tester
echo '{"tool_name":"Write","tool_input":{"file_path":"/tmp/x"}}' | bash scripts/validate-write.sh; echo "exit: $?"
output=$(bash scripts/validate-write.sh < test-input.json 2>&1); echo "$output" | jq .

# Frontmatter marker count for a settings file (guarded for a missing file)
n=$(grep -c '^---$' .claude/my-plugin.local.md 2>/dev/null || echo 0); [ "$n" -ge 2 ] && echo OK || echo "markers: $n"

# HTTP MCP endpoint reachability (expect an HTTP status, not a connection error)
curl -sS -o /dev/null -w '%{http_code}\n' "$API_URL"

# Token variable present without printing it
[ -n "${API_TOKEN:-}" ] && echo "API_TOKEN set" || echo "API_TOKEN missing"

# Codex scaffold placeholder gate
grep -rn '\[TODO' <plugin-dir> && echo "placeholders remain" || echo "clean"

# Codex marketplace structural check: name present, target entry present, path relative
jq -e --arg n my-plugin '.name and (.plugins | map(select(.name==$n)) | length==1) and (.plugins[] | select(.name==$n) | .source.path | startswith("./"))' marketplace.json
```

Gate orders:

- Plugin structure: parse; names and path policy; declared versus default inventory; duplicate detection; portable-reference scan; build; clean install; observe discovery and activation; error cases; update; disable; remove. Also test symlink and letter-case portability, default-plus-custom duplication, and updates that strand old names.
- Command (seven levels): syntax and structure; frontmatter fields; manual invocation under debug; argument matrix (none, one, two, extra, quoted with spaces, empty string, dashes, embedded quotes, very long, `./f`, `../f`, `~/f`, path with spaces); file references (single, missing, several, large); inline shell (output present, disallowed command denied, failing command, empty output, very large output); integration (with a hook, with shared state across commands, with MCP).
- Agent: structural validation with `scripts/validate-agent.sh`; new session; a request phrased like an example; a paraphrase; a neighbouring request that must not select it; a typical task checked against process, output format, edge cases, and quality standards.
- Skill: location and exact file name; frontmatter keys; trigger phrases; instruction voice; every referenced file exists; examples complete; scripts executable; load the plugin and ask triggering and non-triggering questions; optionally ask a skill-reviewing agent to check description quality, organisation, and progressive disclosure.
- Hook (three layers): schema validation catches malformed configuration; fixture tests catch script logic; the debug run catches registration, timing, and matcher problems.
- MCP: restart; local install; `/mcp`; representative calls; debug log for connection, discovery, authentication, tool errors; reachability check for HTTP.
- Settings: location, `.local.md` suffix, plugin-name match, gitignore coverage, marker count, numeric and enum validation, traced run only when file contents and warnings disagree.
- Setup: identity and structure; source and repository signal; configuration shape; permission and data boundary; reversible positive case; unrelated-task negative case; overlap and fan-in; rollback and revocation; owner review.
- Example: source and structure; schema; links and file closure; clean fixture; host discovery; selection and non-selection; output, effects, failure; permissions and dependencies; package and lifecycle; independent copy.
- Codex (nine independent gates): surface and destination preflight; authorized scaffold or update; generated-diff review; structural validation; marketplace source and configuration; installation; fresh-task pickup; component behaviour (skill trigger and non-trigger; app declaration, identity, permissions; MCP declaration, transport, tools, errors, cancellation; hooks through the supported configuration with an event fixture; assets as real files inside the plugin); recovery and removal.

Automation: a suite script over all command files, a pre-commit check, and a CI job validating command files and linting hook matchers against tool names.

Hook development order: write the script; lint it; create a sample input; run it against the sample; add it to the hook configuration; validate the configuration; restart and run under debug. Command testing habits: test while developing, keep scenarios for regression, watch after release, iterate on real usage. One snapshot gives `~/.claude/debug-logs/latest` as the debug log location; that path is unverified. During a command run also watch memory, processor, and process count; no thresholds are given by any source.

## Failure Mode Table

| Area | Failure | Likely cause | Containment and correction |
|---|---|---|---|
| Structure | Component not loading | Wrong directory or extension; bad frontmatter; skill file not named `SKILL.md`; plugin not enabled | Fix placement; restart |
| Structure | Path errors | Hardcoded path; manifest path without `./`; file missing from package | Plugin-root variable; echo the variable inside a hook to confirm |
| Structure | Conflict between plugins | Same command or component names | Prefix or namespace; document |
| Structure | Effects persist after repair | Earlier initialisation already ran | Kill owned processes; clean owned files; reinstall |
| Command | Not in `/help` | Wrong directory; not `.md`; stale session | Fix; restart |
| Command | Arguments wrong | Hint and positionals disagree; extra spaces | Align; test matrix |
| Command | Inline shell fails | Bash not allowed; backtick syntax; command fails in terminal too | Allow filtered Bash; test in terminal |
| Command | File reference fails | Path invalid; Read not allowed | Fix path; allow Read |
| Command | Variable not expanding | Command not loaded from a plugin; misspelt variable | Check label in `/help`; exact spelling |
| Command | Questions do not appear | Tool not allowed; option count outside limits | Allow the tool; two to four options |
| Command | Stale lock or old state schema | Interrupted run; update changed the schema | Abort command; validate state on read; migrate |
| Agent | Never selected | Description lacks conditions or examples; stale session | Add "Use this agent when" and examples; restart |
| Agent | Selected for the wrong requests | Description too broad; no non-use statement | Narrow; add a negative example |
| Agent | Output unusable | Body lacks output format or process | Add both; retest with a typical task |
| Agent | Validator fails on a correct-looking file | Multi-line description; validator reads one line and aborts on first finding | Put the examples on the description line, or review by hand |
| Skill | Never triggers | Vague or second-person description; file not named `SKILL.md`; wrong directory | Quoted trigger phrases; fix name and place; restart |
| Skill | Resources ignored | Not named in the body | Add a resources list with one line per file |
| Hook | Never fires | Stale session; wrong event; matcher case | Restart; `/hooks`; fix matcher |
| Hook | Fires but does not block | Exit code other than 2; JSON on wrong stream | Explicit exit 2; stderr |
| Hook | Check silently skipped | Crash under `set -euo pipefail` on empty `grep` | Guard with `|| true`; test with `{}` |
| Hook | Timeout kill | Slow work in the hook | Budget; move to `Stop`; cache |
| Hook | Intermittent result | Shared temp-file race between parallel hooks | Make hooks independent |
| Hook | Agent loops | Blocking `Stop` hook misjudges | Exit condition; lower to warn |
| MCP | Server will not start | Command missing or not executable; path; permissions | Fix; read debug log |
| MCP | Protocol errors on stdio | Output on stdout | Log to stderr; unbuffered Python |
| MCP | Connection refused | URL, certificate, network, firewall | Fix endpoint |
| MCP | OAuth loop | Cached tokens; redirect URLs | Sign out and in; check redirects |
| MCP | 401 / 403 / 429 / 500 | Token missing or malformed / scope or tenant / rate limit / server fault | Fix token / request scope / back off / server logs |
| MCP | Tools missing | Not connected; wrong name; stale session | `/mcp`; exact names; restart |
| MCP | WebSocket drops | Network; no heartbeat | Reconnect; buffer; acknowledge messages |
| Settings | Missing markers; empty or `null` value; quoted values; `---` in body; edits not picked up | Hand edits; parser gaps; stale session | Validate; treat empty as missing; strip both quote kinds; `awk` counter; ask when the session was restarted |
| Settings | Orphaned file after rename | Plugin or field renamed | Migration reading the old name |
| Setup | Wrong recommendation adopted | Dependency-name matching; unverified catalogue | Disable; re-survey; record |
| Setup | Authority or recovery failure | No owner; no rollback | Binary gate: pause until resolved |
| Example | Learner cannot reproduce | Hidden dependency; host mismatch | Clean-copy test; state the host |
| Codex | Wrong route or omitted lifecycle | Plugin chosen where a component sufficed | Stop; restate outcome; narrower route |
| Codex | Wrong destination or authority | Wrote to a shared location unasked | Stop writes; preserve inventory; get owner decision |
| Codex | Mixed roots or conflicting sample | Two creator versions combined | One contract; minimal fixture; validator governs |
| Codex | Missed normalized collision | Checked the raw name only | Leave state untouched; owner chooses identity |
| Codex | Force overwrite; speculative companions | `--force` as retry; unused `.mcp.json` or `.app.json` | Stop; snapshot; restore; remove extras |
| Codex | Untruthful metadata; change after validation | Placeholders kept; late edit | Withhold exposure; correct; rerun validator; mark earlier gates stale |
| Codex | Wrong marketplace source | Entry points elsewhere | Stop install; resolve target independently |
| Codex | Stale cache; same-task test | No cachebuster; tested in the creating task | Cachebuster once; reinstall; fresh task |
| Codex | Local proof promoted to remote readiness | Assumed credentials and service health | Separate gates; owner acceptance |
| Codex | Secret exposure or destructive loss | Secrets in metadata; overwrite | Stop; restrict, notify, rotate under policy; preserve recovery |
| Codex | Blind retry; competing writers | Rerun without diagnosis | Freeze; inspect partial effects; serialise; retry only on a changed premise |
| Codex | Checklist false green | Ticked boxes without evidence | Block the final claim; inspect underlying evidence |

Failure layers to classify before acting: surface, discovery, metadata, prompt, substitution, permission, resource, script, interaction, state, integration, documentation, update, removal. For structure: build, parse, field semantics, path resolution, package inventory, discovery, registration, initialisation, activation, migration, deactivation, removal.

Common false-green causes with ordinary successful commands (Codex, but general): identity shadowing, installation from the wrong source, stale task or cache, untruthful metadata, unauthorized publication, unknown remote credentials or service health, and evidence gathered before the last edit. A mitigation counts as verified only when a fixture exposed the failure before the fix, the repair changed the predicted premise, an independent postcondition passes, unrelated state is intact, and dependent gates were refreshed.

## Workload Model

- Plugin: one coherent capability domain; one owner per manifest and path; minimal custom discovery edges; isolated initialisation; split when release or permission domains diverge.
- Hook: workload is matcher hit rate times hook cost. Narrow matchers, order cheap before expensive, cap prompt hooks on high-frequency events, move heavy checks to `Stop`. A `*` matcher on `PreToolUse` multiplies every tool call.
- MCP: workload is servers times transports times tools; lazy connection means a one-time first-call spike; batch filtered queries.
- Settings: per hook fire, the common case should be one file-existence test and exit 0; then one frontmatter parse and lazy field extraction.
- Setup: classify work as focused (one surface, one owner), coordinated (several surfaces that must not overlap), or specialist (needs a domain owner) across ten dimensions: decision breadth, source diversity, surface interaction, authority, ownership, reversibility, verification, context coupling, delegation, and lifecycle. Downgrade to a lighter class only when evidence removes the boundary that put the work in the heavier class, and record why. Keep a budget ledger of what each added surface costs in approvals, latency, and maintenance; treat rising noise or duplication as backpressure.
- Example: author workload, learner workload, research workload, and lifecycle workload are different; pushing effort onto the learner is not simplification.
- Working-size guidance from the analyses (one primary task, about ten source files, at most three delegated subtasks, a written completion audit) is provisional and explicitly not universal.

## Reliability Target

Hard invariants (binary, not percentages):

- Valid artifact identity; manifest and package agree; no unexpected or duplicate components; portable paths; declared initialisation; recovery guidance present; unsupported claims rejected.
- Hooks: parseable output on every path; only exit 2 blocks; missing or malformed input never crashes; deny and ask messages explain themselves.
- MCP: retry only retryable errors, at most three attempts (source-local); never retry authentication or validation failures.
- Settings: missing or malformed files never crash a consumer; invalid values warn and default; updates are atomic (killing an updater mid-write leaves the old file intact); one writer per field.
- Setup: no secret scope widening, unauthorized transfer, destructive mutation, hidden failure, failed rollback, or ownerless shared automation.
- Codex: unrelated marketplace entries, order, and interface metadata unchanged; prior identity recoverable.

Proposed targets from the analyses, not observed results: decision accuracy of at least 18 of 20 on a review set, zero unsupported claims, and every "avoid" or failure case naming a rollback, escalation, or next reference. Zero timeout exceedances is the pass line for hook performance. Unexpected activation is treated as seriously as omission.

## Retry Backpressure Guidance

| Situation | Rule |
|---|---|
| Plugin install or load failure | Retry only after classifying the failing phase, rebuilding the exact package (new hash), clearing owned cache and effects, changing a prerequisite, and proving the replay is idempotent. Use a fresh disposable profile when identity is ambiguous. Never delete user data. |
| Command timed out during a mutation | Do not rerun blindly. Inspect state; resume from a validated checkpoint, roll back, or reconfirm. |
| Tool denied | Do not broaden access. Report, stop, or take the narrower path. |
| Hook deny | Terminal until the input changes: zero verbatim retries, at most one modified attempt. |
| Hook ask | A human checkpoint. Do not rephrase around it. |
| Repeated hook timeouts | Redesign, do not raise the timeout repeatedly. |
| MCP 429 or network error | Back off; at most three attempts (source-local); then tell the user. |
| MCP 401, 403, validation error | Never retry as transient. |
| Settings corruption | Warn and default; deleting a corrupt file trades evidence for recovery, so copy it aside first when diagnosis matters. |
| Loop driven by settings | Bound iterations; increment before re-arming; delete state on every exit path. |
| Setup misbehaviour | Move through open, cautious, paused, stopped-and-escalated. A "read" action can still have effects (rate limits, audit logs, cost). Requalify with the trigger and nearby negatives before resuming. |
| Setup retry rules | Allow a bounded retry only for a classified transient failure with no side effect (or an idempotent/safely compensable one), unchanged input and authority, an observable result, a finite budget, a safe fallback, and a stable version. Never retry permission/policy/credential/production denials; unknown, partial, destructive, or external effects; unapproved transfers; deterministic syntax, schema, or logic errors; recursion, fan-out, or shared writes; hidden failures; unchanged repeated failures; ownerless conflicts; exhausted budgets; or scope-expanding attempts. Backoff changes timing, not cause. |
| Codex scaffold or install failure | Freeze; inspect partial effects; classify; serialise writers; retry only on a changed premise. `--force` is not a retry. |
| Example fails for a learner | Retry only for environmental causes that were corrected; record what changed; otherwise push the problem back to admission (the example is not ready) and label any fallback as a fallback. |

## Observability Checklist

- Plugin: installation id, plugin and host versions, package hash, scope, parsed manifest summary, resolved paths, expected and observed component ids, loader phase, diagnostics, owned processes and files, update, disable, residue. The set difference between expected and observed components is the smallest useful signal. Do not upload a whole debug directory.
- Command: invocation id, version and scope, redacted input shape, parsed metadata, granted and denied tools, resource and script status, state transitions, side-effect summary, errors, cancellation, recovery, result. Do not store raw prompts by default.
- Hook: verbose `systemMessage` on deny and ask, quiet approvals, durable audit lines for destructive matchers, `suppressOutput` for noise. Every hook names its log location and review cadence.
- MCP: connection attempts, tool discovery, authentication flow (sanitised), refresh attempts, tool-call errors, call counts.
- Settings: read the file first; stderr warnings second; shell tracing only when those disagree, because tracing can print tokens and prompts; never ship with tracing on.
- Setup: record expected opportunities where the automation did *not* run, not only invocations.
- Example: record each field as Observed, Not applicable, or Unknown; a failed collector means Unknown, not zero.
- Codex: an event per lifecycle step with plugin identity, source, destination, validator result, marketplace identity, install result, fresh-task result.
- Always redact secrets, tokens, raw hook input, and sensitive paths.

## Performance Verification Method

No universal latency threshold is established by any source. Measure, do not assume.

- Plugin: measure separately build, parse, path resolution, discovery, registration, initialisation, first activation, update, disable, removal. Compare matched default and custom packages, not source trees.
- Command: measure cold discovery, warm invocation, decision wait, tool and script time, model time, recovery, and total verified completion separately. Speed that raises approval noise, context use, or recovery cost is a negative optimisation.
- Hook: time the script with fixtures, including `jq` start-up: `time (bash scripts/check.sh < fixture.json)`. The "under 50 ms" figure is source-local. Confirm in the debug log that no hook exceeded its timeout.
- MCP: confirm call counts in the debug log; prefer filtered queries with limits; cache with invalidation; parallelise only independent calls.
- Settings: one frontmatter capture per run; cheap filters before file I/O. No benchmark against `yq` exists.
- Setup claim template: baseline, change, measured effect on the human outcome, cost added (approvals, latency, maintenance), period, and who observed it. A bad claim: "workers finish faster" while aggregate work triples.
- Codex: record durations per lifecycle step only alongside the correctness result of that step.

## Scale Boundary Statement

- Plugin: beyond one coherent domain, split by capability or permission; keep one manifest owner; version shared libraries; isolate components that start at load; namespace identifiers that cross plugins. Watch for duplicate commands, hook fan-out, MCP process multiplication, shared mutable state, dependency cycles, version skew, and breakage on removal.
- Command: split by outcome and ownership; namespace families; keep state local and versioned; isolate integrations; centralise deterministic libraries.
- Hook: hooks are stateless, session-scoped, loaded once, and parallel. Escalate out of hooks for cross-session coordination (external state with real locking), cross-user policy (a versioned plugin), and anything that must survive sessions (CI or server-side checks). An export at `SessionEnd` to a shared log is not durable coordination. A remote context changes filesystem assumptions.
- MCP: stdio is session-bound (spawned with the session, respawned on failure, ended when the host exits); SSE holds a stream and reconnects automatically; HTTP is stateless request and response; WebSocket needs heartbeat, reconnection, buffering during disconnects, message acknowledgement, and tolerance of out-of-order messages; move from stdio to a hosted transport when the service must be always on; move from HTTP to WebSocket when push is needed.
- Settings: the envelope is one small flat project-scoped file, one writer per field, simple values. Beyond that use JSON or SQLite.
- Setup: local (one person, reversible), coordinated (team, shared configuration, needs an owner), specialist (production, security, data; needs the domain owner). Expand one step at a time. Consequence matters more than volume.
- Codex: personal, repository, team, and remote publication are separate scales with separate authority.

## Outcome Metrics and Feedback Loops

Measure the human outcome, not installs or invocation counts.

- Plugin: clean-install success; expected versus observed inventory; duplicates and collisions; activation failures; missing paths; relocation success; update migrations; diagnosis without author support; removal residue. Do not infer health from file count, parse success, downloads, or uninstall alone. Leading indicator: users install, invoke, debug, and remove it without reading the implementation.
- Command: clean-install discovery; valid completion; invalid-input containment; unnecessary approvals; recovery from denied tools and interruptions; portability; diagnosis without support; update compatibility; uninstall residue.
- Hook: weekly review of the trigger log; false-positive rate; timeout frequency; lead time from incident to rule. Promote warn to ask to block on that evidence.
- MCP: authentication failures by class; retries; partial-success reports; call counts per workflow.
- Settings: warning frequency; default-fallback count; corrupt-file cleanups; silent drift. A spike in invalid-value warnings after an update signals schema or template drift.
- Setup: whether the stated friction actually dropped; guardrail breaches (any is a stop); maintenance and diagnosis cost.
- Example: selection precision on positive and negative requests; overlap; time to first success; recovery completion; repeatability; clean-copy success; unexpected effects; denials; file closure and residue; support incidents; descendants copied from it.
- Codex: validator pass on first attempt; fresh-task pickup; unrelated-state preservation; recoveries exercised.

Usability review for commands before release: intuitive name; clear `/help` description; documented arguments; helpful errors; readable output; progress for long runs; actionable results. A beta guide gives scenarios (basic, with arguments, error case), each with the expected result, and asks whether it was easy to understand, met expectations, what to change, and whether the tester would use it regularly.

## Completeness Checklist

- Structure: manifest location; name pattern; only used directories; path policy; no duplicate registration; README; version set; licence file; clean install tested.
- Command: description; argument hint matches positionals; tools minimal and justified; validation and usage message; documentation block; tested matrix; `disable-model-invocation` justified where set; no TODOs or debug code; changelog.
- Agent: name format; description with conditions, 2 to 4 examples, and a non-use; model; colour distinct within the plugin; minimal tools; second-person body with responsibilities, process, quality standards, output format, edge cases; triggering tested; listed in the README.
- Skill: valid frontmatter with `name` and `description`; third-person description with trigger phrases and concrete scenarios; substantial instruction-voice body; referenced files exist; examples complete and working; scripts executable and documented; no information duplicated across files; triggers on expected requests; references load when needed.
- Hook: event matches intent; matcher spelling and case; type justified; output schema matches event; quoted variables; portable paths; schema, fixture, and debug gates passed; restart done; bypass documented.
- MCP: server type; `command` (stdio) or `url` (remote); authentication; variables documented; TLS; plugin-root paths; tools listed in `/mcp`; calls succeed from commands; error cases handled.
- Settings: template in README; gitignore glob; quick-exit; validation; restart wording; schema table; one writer per field. Five of these seven are checkable with grep.
- Release groups for a command: structure, functionality, edge cases, integration, quality (performance, security, errors, output, documentation), distribution (tested by other people, feedback incorporated, README, examples).
- Distribution: version-compatibility check with a deprecation notice; discoverable description and keywords; demonstration examples; a feedback channel; platform detection with branches where behaviour differs; user configuration loaded when present with sensible defaults otherwise; user consent for anything touching private data; tested on macOS, Linux, and Windows through WSL where claimed; no hardcoded paths; dependency check with install hint; graceful degradation by feature detection; first-run message; safe repeated execution; atomic operations; README with installation, usage, configuration, requirements, troubleshooting, support contact, licence; security and privacy review; semantic versioning with a migration guide on major versions; beta label for unfinished commands.
- Setup: each item has status not applicable, unmet, blocked, failed, passed, or passed with bounded uncertainty; a completion claim is invalid when any hard gate is unmet, when only installation or syntax was checked, or when no negative case ran.
- Example: one goal; non-goal stated; status level stated; positive, paraphrased, and neighbouring-negative cases run; file closure checked; cleanup shown; owner named; refresh trigger named; rejected design recorded; claims limited to the status.
- Codex: normalized name; collision check; minimal components; no placeholders; validator passed; marketplace entry correct and others untouched; installed; fresh-task test; recovery recorded.

## Adjacent Reference Routing

| When the work becomes | Go to |
|---|---|
| Authoring or restructuring the content of a skill body or a reference document | The library skill `authoring-skills-and-references` |
| Delegation strategy, context budgets, multi-agent coordination, deeper system-prompt design | The library skill `agent-context-and-orchestration` |
| Turning the contract into executable acceptance criteria | The library skill `executable-specs` and [A03-Executable-Specs01.md](../../A03-Executable-Specs01.md) |
| Reviewing, verifying, or debugging the resulting plugin code | The library skill `review-verify-debug` |
| Branching, committing, and delivering the plugin | The library skill `git-delivery-flow` |
| Deciding whether to build at all, comparing options | The library skill `explore-and-decide` |
| General principles and workflow for model-assisted work | [A00-LLM-Principles01.md](../../A00-LLM-Principles01.md), [A01-LLM-Workflow01.md](../../A01-LLM-Workflow01.md), [A02-Mega-Idiomatic-Prompt.md](../../A02-Mega-Idiomatic-Prompt.md) |
| Implementing an MCP server's protocol logic | The MCP specification and SDK documentation (outside this library) |

Route by the first durable decision the request requires: personal or distributed; event-driven or invoked; inside the session or external. A matcher such as `mcp__.*__delete.*` needs both hook and MCP knowledge, so compose rather than route.

## Source Evidence Mapping Table

| Topic in the skill | Evidence unit | Kind | Supports | Does not support |
|---|---|---|---|---|
| Layout, manifest fields, path rules, discovery order | plugin-dev plugin-structure skill, manifest reference, component-patterns reference | Vendor plugin snapshot | Documented intent at snapshot | Current schema, runtime discovery on any version |
| Command frontmatter, arguments, file references, inline shell | plugin-dev command-development skill and its seven detail references (frontmatter, plugin features, interactive commands, advanced workflows, documentation patterns, testing strategies, marketplace considerations) | Vendor plugin snapshot | Documented intent | Parser behaviour on the installed version |
| Hook events, output shapes, exit codes, patterns, migration | plugin-dev hook-development skill; patterns, advanced, and migration references; utility-script README | Vendor plugin snapshot | Documented intent | Current event catalogue or timeouts |
| Hookify rule format | hookify plugin rule-writing skill | Vendor plugin snapshot | Rule file format at snapshot | Behaviour without the hookify plugin installed |
| MCP bundling, transports, authentication, tool use | plugin-dev mcp-integration skill; server-types, authentication, tool-usage references; example configurations | Vendor plugin snapshot | Documented intent | Current transports, `headersHelper`, hosted OAuth roster |
| Settings convention and parsing | plugin-dev plugin-settings skill; parsing-techniques and real-world-examples references | Vendor plugin snapshot | Convention used by shipped plugins | Any native settings API |
| Agent file format, triggering description, system-prompt skeleton, validation limits | plugin-dev agent-development skill and its validator script | Vendor plugin snapshot | Documented intent; validator behaviour (also **Observed**) | Required-field enforcement or colour list on the installed version |
| Skill placement, bundled directories, description style, creation process | plugin-dev skill-development skill | Vendor plugin snapshot | Documented intent | Word-count limits as host limits; the `--plugin-dir` flag on the installed version |
| Example skill structure | example-plugin example skill | Vendor plugin snapshot | Skill structure and description-led triggering | Manifest, command, hook, MCP, install, removal |
| Setup recommendations and signal maps | claude-code-setup recommender skill; hooks, MCP servers, plugins, skills, and subagent references | Vendor plugin snapshot | Candidate mappings as leads | That any listed server or plugin exists or fits today |
| Codex layout, fields, marketplace, scaffold | Codex plugin-creator skill, manifest spec, scaffold script (2026-03 snapshot) | Third-party tool snapshot | Scaffold behaviour (also **Observed** by running it) | Current Codex validator rules |
| Risk, lifecycle, evidence, metrics framing | Eight analysis digests dated 2026-07-10, one per sub-topic | Local analysis | Synthesis and conflict identification | Runtime behaviour |
| Upstream script behaviour notes | Local runs of upstream scripts and example hooks | **Observed** | Exactly the listed behaviours on Linux, bash 5, jq, python3 | Other platforms or shells |

Archive and live copies of the same vendor file were byte-identical and count once. MCP specification pages listed alongside several sub-topics are adjacent evidence for external integration only; they do not define slash-command frontmatter, hook behaviour, settings, or manifest fields.

### Sources

- Anthropic Claude Code `plugin-dev` plugin (skills: plugin-structure, command-development, hook-development, mcp-integration, plugin-settings, agent-development, skill-development) (Apache-2.0; ideas folded in, upstream linked in [the attribution notes](../../S02-curated-upstream-skill-snapshots/ATTRIBUTION.md)).
- Anthropic Claude Code `hookify` plugin (rule-writing skill).
- Anthropic Claude Code `example-plugin` (example skill).
- Anthropic Claude Code `claude-code-setup` plugin (automation recommender skill and references).
- OpenAI Codex `plugin-creator` system skill (2026-03 snapshot): skill text, manifest specification, and `create_basic_plugin.py` (ideas folded in; not bundled verbatim).
- Model Context Protocol specification (revision 2025-06-18 was the pinned revision in the analyses), `modelcontextprotocol/servers`, `github/github-mcp-server`, and the `@modelcontextprotocol/sdk` package: named as anchors, not retrieved.
- Claude Code documentation pages for hooks and MCP (`docs.claude.com/en/docs/claude-code/hooks`, `.../mcp`): named as the freshness anchors, not retrieved.
- Unverified public leads recorded by the setup analysis: `github.com/davepoon/buildwithclaude`, `github.com/Cranot/claude-code-guide`, `claudedirectory.org` (article comparing skills, subagents, and MCP).
- Example plugins referenced for settings behaviour: `ralph-loop` and `multi-agent-swarm`; `security-guidance` as a hook example.

## Evidence Boundary Notes

- Nothing in the skill or this reference was verified against a running Claude Code or Codex host. The only executed checks are the local observations of upstream helper scripts.
- Valid JSON is not an accepted schema; package presence is not discovery; discovery is not safe activation; activation is not clean removal; identical files are not corroboration.
- Field names, the nine-event catalogue, prompt-hook event support, default timeouts, exit-code semantics, the tool-name prefix, environment expansion, the four transports, `headersHelper`, and lazy connection are documented-at-snapshot contracts pending live documentation.
- Numbers that are source-local or illustrative and must not be quoted as measurements: under 50 ms command hooks; 60 s and 30 s default timeouts; 15 to 30 s prompt timeouts; five-minute cache; ten commands per minute; 10 MB file ceiling; three retry attempts; 60-character descriptions; 5 or 15 command namespace thresholds; question limits (1 to 4, 2 to 4, 12 characters); 100+ files for layered layouts; more than 500 files for a reviewer subagent; agent name, description, and prompt length ranges; skill body and reference word counts; two clean weeks before promotion; 3 of 10 handoffs; release cadences; 18 of 20 decision accuracy; one task, ten files, three delegates.
- Catalogues of MCP servers, official plugins, and LSP plugins are a snapshot roster. Availability, names, and install commands must be re-checked before recommending any of them.
- Conflicts kept open in the skill, each with its selecting condition: hook file format; MCP file shape; MCP start time; debug flag; settings restart; absent settings file; mutable data under the plugin root; temporary-file state; namespace threshold; default hook type; Codex top-level `hooks`; Codex scaffold defaults; Codex default destination; agent versus command MCP allowlists; agent frontmatter fields; skill body size.
- The plugin-structure snapshot shows agent frontmatter with a `capabilities` list, which differs from the agent snapshot's fields (`name`, `description`, `model`, `color`, optional `tools`); the skill keeps both under a Conflict label and selects by host verification.
- The agent snapshot names a trigger-testing script that is absent from the snapshot; only the structural validator exists and is bundled.
- One snapshot claims that paths with spaces need no special quoting in command files. That is unverified; quote in scripts regardless and test an install path containing a space.
- Prohibited evidence transfers for examples: from a historical tree to current behaviour; from a static parse to runtime; from one host to another; from a skill-only example to commands, hooks, MCP, or lifecycle.

## Future Refresh Search Queries

Refresh only after a documented drift signal (a gate fails on a new host version, a field is rejected, a documented behaviour is not observed). Include the host version and the field in the query, and bring a minimal packaged fixture.

- "Claude Code plugin manifest plugin.json fields" plus the host version
- "Claude Code plugin hooks.json format hooks wrapper" plus the host version
- "Claude Code hooks events list PreToolUse output permissionDecision"
- "Claude Code prompt hooks supported events"
- "Claude Code hook exit code 2 stderr behavior"
- "Claude Code plugin .mcp.json mcpServers format"
- "Claude Code MCP headersHelper"
- "Claude Code MCP server lazy connection startup"
- "Claude Code slash command frontmatter allowed-tools argument-hint disable-model-invocation"
- "Claude Code AskUserQuestion options limit"
- "Claude Code plugin agent frontmatter required fields model color tools"
- "Claude Code plugin-dir flag load local plugin"
- "Claude Code plugin skills SKILL.md frontmatter fields"
- "Claude Code plugin settings local.md" and "Claude Code native plugin settings"
- "Claude Code debug flag mcp-debug"
- "hookify plugin rule file format conditions operators"
- "Model Context Protocol specification current revision transports"
- "Codex plugin creator plugin.json hooks validator"
- "Codex plugin marketplace.json policy installation authentication"
- "Codex plugin add marketplace cachebuster"
- "ralph-loop plugin stop hook state file" and "multi-agent-swarm plugin settings"
