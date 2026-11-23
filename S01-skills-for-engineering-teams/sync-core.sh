#!/usr/bin/env bash
# Sync the Rust skills only. Use --check to report drift without changing a skill.
set -euo pipefail
cd "$(dirname "$0")"
if (( $# > 1 )) || [[ $# == 1 && $1 != --check ]]; then
  echo 'usage: sync-core.sh [--check]' >&2; exit 2
fi
[[ -s _core.md && -s _essentials.md ]] || { echo 'missing Rust shared block' >&2; exit 1; }
tmp=$(mktemp)
trap 'rm -f "$tmp"' EXIT
for skill in tir-rust-*/SKILL.md; do
  writer=1
  [[ $skill != tir-rust-review/SKILL.md ]] || writer=0
  awk -v writer="$writer" '
    /^<!-- (core|essentials):begin -->$/ {
      name = $2; sub(/:begin$/, "", name)
      if (block || seen[name]++) exit 1
      print; block = name; file = "_" name ".md"
      while ((getline line < file) > 0) print line
      close(file); next
    }
    /^<!-- (core|essentials):end -->$/ {
      if ($2 != block ":end") exit 1
      block = ""
    }
    !block { print }
    END { if (block || seen["core"] != 1 || seen["essentials"] != writer) exit 1 }
  ' "$skill" > "$tmp" || { echo "invalid shared blocks: $skill" >&2; exit 1; }
  if ! cmp -s "$tmp" "$skill"; then
    [[ ${1:-} != --check ]] || { echo "out of sync: $skill" >&2; exit 1; }
    cat "$tmp" > "$skill"
    echo "synced $skill"
  fi
done
