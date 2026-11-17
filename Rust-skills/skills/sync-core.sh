#!/usr/bin/env bash
# Copies _core.md into every skill, between the core:begin and core:end markers.
# Run from anywhere after editing _core.md:  Rust-skills/skills/sync-core.sh
set -euo pipefail
cd "$(dirname "$0")"
for skill in */SKILL.md; do
  grep -q '<!-- core:begin -->' "$skill" || { echo "no core marker in $skill" >&2; exit 1; }
  awk -v core=_core.md '
    /<!-- core:begin -->/ { print; while ((getline line < core) > 0) print line; close(core); skipping = 1; next }
    /<!-- core:end -->/   { skipping = 0 }
    !skipping             { print }
  ' "$skill" > "$skill.tmp"
  mv "$skill.tmp" "$skill"
  echo "synced $skill"
done
