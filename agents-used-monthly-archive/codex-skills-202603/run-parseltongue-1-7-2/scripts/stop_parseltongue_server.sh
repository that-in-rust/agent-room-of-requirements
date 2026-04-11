#!/usr/bin/env bash
set -euo pipefail

print_usage() {
  cat <<'EOF'
Usage:
  stop_parseltongue_server.sh <run_folder>

Behavior:
  - Read server PID from <run_folder>/server.pid
  - Stop the running parseltongue server process
EOF
}

main() {
  if [[ "${1:-}" == "--help" || "${1:-}" == "-h" ]]; then
    print_usage
    return 0
  fi

  if [[ $# -ne 1 ]]; then
    print_usage
    return 1
  fi

  local run_folder="$1"
  local pid_file="${run_folder}/server.pid"

  if [[ ! -f "${pid_file}" ]]; then
    echo "PID file not found: ${pid_file}" >&2
    return 1
  fi

  local pid
  pid="$(cat "${pid_file}")"
  if [[ -z "${pid}" ]]; then
    echo "Empty PID in ${pid_file}" >&2
    return 1
  fi

  if ! kill -0 "${pid}" >/dev/null 2>&1; then
    echo "Process ${pid} is not running."
    rm -f "${pid_file}"
    return 0
  fi

  kill "${pid}"
  rm -f "${pid_file}"
  echo "Stopped parseltongue server process ${pid}."
}

main "$@"
