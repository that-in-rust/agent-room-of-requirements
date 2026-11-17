#!/usr/bin/env bash
# Copies the shared blocks into every skill:
#   _core.md        between <!-- core:begin --> and <!-- core:end -->          (every skill)
#   _essentials.md  between <!-- essentials:begin --> and <!-- essentials:end --> (writer skills)
# Run from anywhere after editing either file:  Rust-skills/skills/sync-core.sh
set -euo pipefail
cd "$(dirname "$0")"
for skill in */SKILL.md; do
  grep -q '<!-- core:begin -->' "$skill" || { echo "no core marker in $skill" >&2; exit 1; }
  awk '
    function emit(file,   line) { while ((getline line < file) > 0) print line; close(file) }
    /<!-- core:begin -->/       { print; emit("_core.md");       skipping = 1; next }
    /<!-- essentials:begin -->/ { print; emit("_essentials.md"); skipping = 1; next }
    /<!-- (core|essentials):end -->/ { skipping = 0 }
    !skipping { print }
  ' "$skill" > "$skill.tmp"
  mv "$skill.tmp" "$skill"
  echo "synced $skill"
done
