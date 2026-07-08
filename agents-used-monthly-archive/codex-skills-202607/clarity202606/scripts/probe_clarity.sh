#!/usr/bin/env bash
set -euo pipefail

find_clarity() {
  if [[ -n "${CLARITY_BIN:-}" && -x "${CLARITY_BIN}" ]]; then
    printf '%s\n' "${CLARITY_BIN}"
    return 0
  fi

  if command -v clarity >/dev/null 2>&1; then
    command -v clarity
    return 0
  fi

  local candidates=(
    "./clarity"
    "/Users/amuldotexe/Desktop/oss-read-only/_tools/clarity/clarity"
    "/Users/amuldotexe/Desktop/oss-read-only/clarity-cli/clarity"
    "/Users/amuldotexe/Desktop/personal-repos-lane/parseltongue-rust-LLM-companion/git-ref-repo/ignore-this-folder-repos/LegacyCodeHQ__clarity-cli/clarity"
  )

  local candidate
  for candidate in "${candidates[@]}"; do
    if [[ -x "${candidate}" ]]; then
      printf '%s\n' "${candidate}"
      return 0
    fi
  done

  return 1
}

bin="$(find_clarity || true)"

if [[ -z "${bin}" ]]; then
  echo "CLARITY_BIN="
  echo "No clarity binary found. Install, build, or set CLARITY_BIN=/path/to/clarity."
  exit 1
fi

echo "CLARITY_BIN=${bin}"
echo
echo "== version =="
"${bin}" --version || true
echo
echo "== root help =="
"${bin}" --help
echo
echo "== available subcommand help =="
for cmd in show watch workspace languages extensions modules cycles setup diff why; do
  if "${bin}" "${cmd}" --help >/tmp/clarity-probe-help.$$ 2>/tmp/clarity-probe-err.$$; then
    echo
    echo "-- ${cmd} --"
    sed -n '1,80p' /tmp/clarity-probe-help.$$
  fi
done
rm -f /tmp/clarity-probe-help.$$ /tmp/clarity-probe-err.$$
