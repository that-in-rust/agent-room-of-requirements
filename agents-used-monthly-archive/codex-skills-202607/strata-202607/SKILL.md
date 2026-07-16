---
name: strata-202607
description: Use Strata, the Legacy Code Labs macOS visual-spec app, through its local Streamable HTTP MCP server. Trigger when Codex needs to create, read, validate, update, version, diff, or restore Strata diagrams; build visual specs from user flows, discovery trees, architecture sketches, or D2; diagnose Strata MCP setup; or verify a feature against a shared Strata canvas.
---

# Strata 202607

Strata is a native macOS visual-spec tool. The app runs a loopback-only MCP server at `http://127.0.0.1:7337/mcp`; use it to work against versioned D2 diagrams instead of keeping a visual spec only in chat.

## Startup Check

1. Confirm Strata is installed and launch it:
   ```bash
   test -x /Applications/Strata.app/Contents/MacOS/Strata
   open -a Strata
   lsof -nP -iTCP:7337 -sTCP:LISTEN
   ```
2. If Codex has not been configured yet, install the MCP server:
   ```bash
   codex mcp add strata --url http://127.0.0.1:7337/mcp
   codex mcp list
   ```
3. Probe the local server:
   ```bash
   /Users/amulbadjatya/.codex/skills/strata-202607/scripts/strata_mcp_probe.py --kits
   ```

If this session does not expose Strata MCP tools after installation, restart Codex or use `scripts/strata_mcp_tool.py` as a temporary raw JSON-RPC fallback. Do not hand-edit Strata's SQLite database.

## Core Workflow

1. List projects, then create or choose a project.
2. Pick the right kit:
   - `user_flow`: UI navigation, user journeys, branching logic, E2E proof paths.
   - `discovery_tree`: outcomes, nested tasks, planning trees.
   - `freeform`: raw D2 for architecture, state machines, data flows.
3. Before authoring constrained diagrams, call `describe_kit` for the selected kit or read `references/strata-kits.md`.
4. Draft source and call `validate_diagram` until it compiles.
5. Call `create_diagram` for a new visual spec or `get_diagram` then `update_diagram` for an existing one.
6. Always preserve concurrency:
   - Read `version` from `get_diagram`.
   - Pass that as `base_version` to `update_diagram`.
   - If Strata reports a conflict, re-read, merge, validate, and retry.
7. Use `list_versions`, `diff_versions`, `get_version`, and `restore_version` for review, rollback, and audit.

## Safety Rules

- Treat `diagram_id`, `project_id`, and `group_id` as opaque API handles.
- In user-facing summaries, use `diagram_name`, not internal IDs.
- Never claim an edit landed unless Strata returned `render_ok: true` or the create/update result succeeded.
- Prefer `validate_diagram` before mutating diagrams.
- Keep source replacement intentional: `update_diagram` replaces the full D2 source and creates a snapshot.
- Use `message` on updates for meaningful snapshot notes.
- Use `delete_diagram` and `delete_group` only after explicit confirmation; there is no MCP undo for deletion.
- Do not use Strata for repo dependency analysis; use Clarity or codebase-memory for code structure, then represent the result in Strata if a visual spec is useful.

## Raw MCP Fallback

Use the bundled helpers when the Codex tool list has not picked up Strata yet:

```bash
scripts/strata_mcp_probe.py --kits
scripts/strata_mcp_tool.py list_projects
scripts/strata_mcp_tool.py validate_diagram --args-json '{"kit":"user_flow","source":"@direction down\n\nstart s: Start\nscreen page: Page\nend e success: Done\ns -> page\npage -> e"}'
```

## References

- Read `references/strata-mcp-tools.md` when you need exact tool names, arguments, or installation evidence.
- Read `references/strata-kits.md` when authoring `user_flow`, `discovery_tree`, or `freeform` diagrams.
- Read `references/strata-failure-modes.md` when setup, validation, concurrency, or visibility is confusing.
