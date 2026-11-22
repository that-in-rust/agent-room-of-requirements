#!/usr/bin/env python3
"""Probe the local Strata Streamable HTTP MCP server without mutating data."""

from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.request
from typing import Any


DEFAULT_URL = "http://127.0.0.1:7337/mcp"
HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json, text/event-stream",
}


class McpError(RuntimeError):
    pass


def _decode_streamable_http(body: str) -> str:
    if not body.startswith("event:"):
        return body
    data_lines = [line[5:].strip() for line in body.splitlines() if line.startswith("data:")]
    return "\n".join(data_lines) if data_lines else body


def mcp_call(url: str, method: str, params: dict[str, Any] | None = None, ident: int = 1) -> dict[str, Any]:
    payload = {
        "jsonrpc": "2.0",
        "id": ident,
        "method": method,
        "params": params or {},
    }
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers=HEADERS,
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            raw = response.read().decode("utf-8")
    except urllib.error.URLError as exc:
        raise McpError(f"Cannot reach Strata MCP at {url}: {exc}") from exc

    decoded = _decode_streamable_http(raw)
    try:
        result = json.loads(decoded)
    except json.JSONDecodeError as exc:
        raise McpError(f"Strata MCP returned non-JSON response: {decoded[:300]}") from exc
    if "error" in result:
        raise McpError(json.dumps(result["error"], indent=2))
    return result


def tool_call(url: str, name: str, arguments: dict[str, Any] | None = None, ident: int = 100) -> Any:
    response = mcp_call(url, "tools/call", {"name": name, "arguments": arguments or {}}, ident)
    result = response.get("result", {})
    content = result.get("content", [])
    if content and isinstance(content, list) and "text" in content[0]:
        text = content[0]["text"]
        try:
            return json.loads(text)
        except json.JSONDecodeError:
            return text
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description="Probe local Strata MCP server.")
    parser.add_argument("--url", default=DEFAULT_URL)
    parser.add_argument("--kits", action="store_true", help="Also print describe_kit output.")
    parser.add_argument("--json", action="store_true", help="Print machine-readable JSON.")
    args = parser.parse_args()

    try:
        initialize = mcp_call(
            args.url,
            "initialize",
            {
                "protocolVersion": "2024-11-05",
                "capabilities": {},
                "clientInfo": {"name": "codex-strata-probe", "version": "0.1"},
            },
            1,
        )
        tools_response = mcp_call(args.url, "tools/list", {}, 2)
        tools = tools_response.get("result", {}).get("tools", [])
        projects = tool_call(args.url, "list_projects", {}, 3)
        kits = tool_call(args.url, "describe_kit", {}, 4) if args.kits else None
    except McpError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    payload = {
        "server": initialize.get("result", {}).get("serverInfo", {}),
        "protocolVersion": initialize.get("result", {}).get("protocolVersion"),
        "tool_count": len(tools),
        "tools": [tool.get("name") for tool in tools],
        "projects": projects,
        "kits": kits,
    }

    if args.json:
        print(json.dumps(payload, indent=2, sort_keys=True))
        return 0

    server = payload["server"]
    print(f"Strata MCP: {server.get('name')} {server.get('version')} at {args.url}")
    print(f"Protocol: {payload['protocolVersion']}")
    print(f"Tools: {payload['tool_count']}")
    for tool_name in payload["tools"]:
        print(f"  - {tool_name}")
    print("Projects:")
    print(json.dumps(projects, indent=2))
    if kits is not None:
        print("Kits:")
        print(json.dumps(kits, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
