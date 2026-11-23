#!/usr/bin/env python3
"""Call one Strata MCP tool through raw Streamable HTTP JSON-RPC."""

from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any


DEFAULT_URL = "http://127.0.0.1:7337/mcp"
HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json, text/event-stream",
}


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
        with urllib.request.urlopen(req, timeout=20) as response:
            raw = response.read().decode("utf-8")
    except urllib.error.URLError as exc:
        raise RuntimeError(f"Cannot reach Strata MCP at {url}: {exc}") from exc
    result = json.loads(_decode_streamable_http(raw))
    if "error" in result:
        raise RuntimeError(json.dumps(result["error"], indent=2))
    return result


def parse_args_json(args_json: str | None, args_file: str | None) -> dict[str, Any]:
    if args_json and args_file:
        raise ValueError("Use either --args-json or --args-file, not both.")
    if args_file:
        return json.loads(Path(args_file).read_text())
    if args_json:
        return json.loads(args_json)
    return {}


def unwrap_tool_result(response: dict[str, Any]) -> Any:
    result = response.get("result", {})
    content = result.get("content", [])
    if content and isinstance(content, list) and isinstance(content[0], dict) and "text" in content[0]:
        text = content[0]["text"]
        try:
            return json.loads(text)
        except json.JSONDecodeError:
            return text
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description="Call a Strata MCP tool.")
    parser.add_argument("tool", help="Tool name, e.g. list_projects or validate_diagram.")
    parser.add_argument("--url", default=DEFAULT_URL)
    parser.add_argument("--args-json", help="Tool arguments as JSON object.")
    parser.add_argument("--args-file", help="Path to JSON file containing tool arguments.")
    parser.add_argument("--raw", action="store_true", help="Print raw MCP response.")
    args = parser.parse_args()

    try:
        arguments = parse_args_json(args.args_json, args.args_file)
        response = mcp_call(args.url, "tools/call", {"name": args.tool, "arguments": arguments}, 1)
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    output = response if args.raw else unwrap_tool_result(response)
    print(json.dumps(output, indent=2, sort_keys=True) if not isinstance(output, str) else output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
