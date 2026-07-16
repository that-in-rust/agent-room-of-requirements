# Strata Failure Modes

## App or MCP Not Reachable

Symptoms:

- `curl: Failed to connect to 127.0.0.1 port 7337`
- `lsof -nP -iTCP:7337 -sTCP:LISTEN` prints nothing

Fix:

```bash
open -a Strata
lsof -nP -iTCP:7337 -sTCP:LISTEN
```

If the app is not installed, download/install Strata first. This skill expects `/Applications/Strata.app`.

## GET `/mcp` Returns 405

This is expected. Strata is a Streamable HTTP MCP endpoint and expects POST JSON-RPC calls. Use the bundled scripts or MCP tools, not a browser GET.

## Codex Does Not Show Strata Tools

If `codex mcp list` shows Strata but this session has no Strata tools, restart Codex or continue with:

```bash
/Users/amulbadjatya/.codex/skills/strata-202607/scripts/strata_mcp_tool.py list_projects
```

The server is still usable through raw JSON-RPC.

## Compile or Validation Error

`validate_diagram`, `create_diagram`, and `update_diagram` compile source before saving. If Strata returns `compile_error`, no snapshot was saved. Fix the source using the returned line/column errors, then validate again.

## Stale `base_version`

`update_diagram` should pass the per-diagram `version` last read from `get_diagram`. If Strata returns a conflict, re-read the diagram, merge the source intentionally, validate, and retry with the new base version.

## Active Diagram Ambiguity

Many tools allow omitting `diagram_id` to use the selected diagram. Prefer explicit IDs unless the user is actively looking at the target diagram in Strata and asks you to update "this diagram."

## Deletion Is Irreversible Over MCP

`delete_diagram` deletes version history. `delete_group` keeps diagrams but removes the group. Ask before using either.

## SQLite Is Not the API

Observed storage is `/Users/amulbadjatya/Library/Application Support/Strata/strata.sqlite`, but do not edit it. Use MCP so validation, snapshots, and app state stay coherent.

## Wrong Product Named Strata

This skill is only for the Legacy Code Labs macOS visual-spec app. It is not for Apache Strata, portfolio analytics libraries, or unrelated products named Strata.
