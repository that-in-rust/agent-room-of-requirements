# Strata MCP Tools

Local Strata app inspected on 2026-07-16:

- App path: `/Applications/Strata.app`
- Bundle identifier: `com.legacycode.strata`
- Version: `0.9.0` build `29`
- MCP URL: `http://127.0.0.1:7337/mcp`
- Storage observed: `/Users/amulbadjatya/Library/Application Support/Strata/strata.sqlite`

Official Strata page says the MCP server binds to `127.0.0.1`, specs live in local SQLite, and coding agents connect over local MCP.

OpenAI Codex MCP docs say Streamable HTTP servers are configured under `[mcp_servers.<server-name>]` with a required `url`.

## Installation Evidence

Codex MCP config:

```toml
[mcp_servers.strata]
url = "http://127.0.0.1:7337/mcp"
```

Smoke initialize returned:

```json
{
  "serverInfo": { "name": "strata", "version": "0.9.0" },
  "protocolVersion": "2024-11-05",
  "capabilities": { "tools": { "listChanged": false } }
}
```

Smoke write created:

```json
{
  "project_id": "019f68ee-4812-7168-826e-4eb2fb63e70a",
  "diagram_id": "019f68ee-da6b-71d2-86f6-b0cceb359172",
  "diagram_name": "Codex Strata MCP Smoke Flow",
  "kit": "user_flow",
  "version": 1
}
```

`get_diagram` returned `render_ok: true`.

Bundled deterministic helpers:

```bash
/Users/amulbadjatya/.codex/skills/strata-202607/scripts/strata_mcp_probe.py --kits
/Users/amulbadjatya/.codex/skills/strata-202607/scripts/strata_mcp_tool.py list_projects
```

## Tools

Current Strata MCP tool list:

| Tool | Use |
|---|---|
| `get_diagram` | Return visible name, current D2 source, version, and render status. |
| `update_diagram` | Replace full D2 source after compile; pass `base_version` to avoid stale edits. |
| `validate_diagram` | Dry-run compile source through `freeform`, `user_flow`, or `discovery_tree`. |
| `describe_kit` | Return grammar, vocabulary, statuses, directives, and examples for kits. |
| `list_versions` | List snapshots newest first. |
| `get_version` | Return D2 source for one version. |
| `restore_version` | Make an old snapshot current by creating a new snapshot. |
| `diff_versions` | Unified diff between versions or a version and current. |
| `list_projects` | List all projects. |
| `create_project` | Create a project. |
| `list_diagrams` | List diagrams in a project. |
| `create_diagram` | Create a diagram in a project, optionally in a group. |
| `rename_diagram` | Rename a diagram without changing source/history. |
| `list_groups` | List groups in a project. |
| `create_group` | Create a flat group. |
| `rename_group` | Rename a group. |
| `move_diagram` | Move diagram to a group or ungrouped. |
| `delete_diagram` | Delete diagram and version history; irreversible. |
| `delete_group` | Delete a group, preserving diagrams by moving them ungrouped; irreversible over MCP. |

## Common Calls

List projects:

```bash
scripts/strata_mcp_tool.py list_projects
```

List diagrams in a project:

```bash
scripts/strata_mcp_tool.py list_diagrams --args-json '{"project_id":"PROJECT_ID"}'
```

Validate a user flow:

```bash
scripts/strata_mcp_tool.py validate_diagram --args-json '{"kit":"user_flow","source":"@direction down\n\nstart s: Start\nscreen page: Page\nend done success: Done\ns -> page\npage -> done"}'
```

Create a diagram:

```bash
scripts/strata_mcp_tool.py create_diagram --args-json '{"project_id":"PROJECT_ID","name":"Feature Flow","kit":"user_flow","source":"..."}'
```

Update a diagram safely:

```bash
scripts/strata_mcp_tool.py get_diagram --args-json '{"diagram_id":"DIAGRAM_ID"}'
scripts/strata_mcp_tool.py update_diagram --args-json '{"diagram_id":"DIAGRAM_ID","base_version":1,"source":"...","message":"Explain the change"}'
```

The `base_version` is the per-diagram integer version from `get_diagram`. If there is a conflict, re-read and retry.

## Kit Notes

`describe_kit` reports three kits:

- `freeform`: raw D2 for arbitrary architecture, data models, state machines, migrations.
- `user_flow`: constrained UI navigation and branching flow. Use nodes like `start`, `screen`, `surface`, `action`, `decision`, `system`, `connector`, and `end`.
- `discovery_tree`: constrained outcome/task planning tree.

For `user_flow`, the first line can be:

```d2
@direction down
```

Then define nodes:

```d2
start open: Open app
screen home: Home
  action click: Click create
system save: Save draft
end done success: Draft created

open -> home
home -> click
click -> save
save -> done
```

Use `@status` when representing verified/building paths.
