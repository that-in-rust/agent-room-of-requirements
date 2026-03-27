#!/usr/bin/env bash
set -euo pipefail

PARSELTONGUE_VERSION="1.7.2"

# Central log in the skill folder
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
CENTRAL_LOG_DIR="${SKILL_ROOT}/central-logs"
CENTRAL_LOG_FILE="${CENTRAL_LOG_DIR}/parseltongue-query-log.txt"

central_log() {
  mkdir -p "${CENTRAL_LOG_DIR}" || true
  local ts
  ts="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  echo "${ts} | $*" >> "${CENTRAL_LOG_FILE}"
}

print_usage() {
  cat <<'EOF'
Usage:
  reindex_parseltongue_1_7_2.sh <run_folder> [--codebase-path PATH] [--port PORT]

Behavior:
  - Verify run folder binary is parseltongue 1.7.2
  - Stop existing server process if running
  - Rebuild the workspace from inside the run folder
  - Record the actual workspace and DB paths chosen by the binary
  - Start server again and run health/stats/watcher checks
EOF
}

require_command() {
  local cmd="$1"
  command -v "${cmd}" >/dev/null 2>&1 || {
    echo "Missing required command: ${cmd}" >&2
    return 1
  }
}

start_detached_server() {
  local binary_path="$1"
  local db_uri="$2"
  local port="$3"
  local server_log="$4"
  local pid_file="$5"
  local codebase_path="$6"

  python3 - "${binary_path}" "${db_uri}" "${port}" "${server_log}" "${pid_file}" "${codebase_path}" <<'PY'
import os
import subprocess
import sys

binary_path, db_uri, port, server_log, pid_file, codebase_path = sys.argv[1:]

with open(server_log, "ab", buffering=0) as log_file:
    process = subprocess.Popen(
        [binary_path, "pt08-http-code-query-server", "--db", db_uri, "--port", port],
        cwd=codebase_path,
        stdin=subprocess.DEVNULL,
        stdout=log_file,
        stderr=subprocess.STDOUT,
        start_new_session=True,
    )

with open(pid_file, "w", encoding="utf-8") as pid_handle:
    pid_handle.write(f"{process.pid}\n")
PY
}

wait_for_server() {
  local server_url="$1"
  local retries=20
  local i
  for ((i = 1; i <= retries; i++)); do
    if curl -fsS "${server_url}/server-health-check-status" >/dev/null 2>&1; then
      return 0
    fi
    sleep 1
  done
  return 1
}

resolve_db_uri_from_index_log() {
  local run_folder="$1"
  local index_log="$2"
  local logged_db_uri
  logged_db_uri="$(
    grep -E '^[[:space:]]*rocksdb:[^[:space:]"]+$' "${index_log}" | \
      sed 's/^[[:space:]]*//' | \
      tail -n 1 || true
  )"

  if [[ -z "${logged_db_uri}" ]]; then
    logged_db_uri="$(
      grep -Eo 'rocksdb:[^[:space:]"]+' "${index_log}" | head -n 1 || true
    )"
  fi

  if [[ -z "${logged_db_uri}" ]]; then
    echo "Could not determine database URI from ${index_log}" >&2
    return 1
  fi

  local db_path="${logged_db_uri#rocksdb:}"
  if [[ "${db_path}" != /* ]]; then
    db_path="${run_folder}/${db_path}"
  fi

  echo "rocksdb:${db_path}"
}

resolve_workspace_path_from_db_uri() {
  local db_uri="$1"
  local db_path="${db_uri#rocksdb:}"
  dirname "${db_path}"
}

verify_db_path_exists() {
  local db_uri="$1"
  local db_path="${db_uri#rocksdb:}"

  if [[ -f "${db_path}/manifest" ]]; then
    return 0
  fi

  compgen -G "${db_path}/data/MANIFEST-*" >/dev/null 2>&1
}

remove_workspace_path_if_safe() {
  local run_folder="$1"
  local workspace_path="$2"

  if [[ -z "${workspace_path}" ]]; then
    return 0
  fi

  case "${workspace_path}" in
    "${run_folder}"/*)
      rm -rf "${workspace_path}"
      ;;
    *)
      echo "Refusing to remove workspace outside run folder: ${workspace_path}" >&2
      ;;
  esac
}

resolve_binary_path() {
  local run_folder="$1"
  if [[ -x "${run_folder}/bin/parseltongue" ]]; then
    echo "${run_folder}/bin/parseltongue"
    return 0
  fi
  if [[ -x "${run_folder}/bin/parseltongue.exe" ]]; then
    echo "${run_folder}/bin/parseltongue.exe"
    return 0
  fi
  echo "Parseltongue binary not found in ${run_folder}/bin" >&2
  return 1
}

stop_existing_server_if_running() {
  local run_folder="$1"
  local pid_file="${run_folder}/server.pid"
  if [[ ! -f "${pid_file}" ]]; then
    return 0
  fi

  local pid
  pid="$(cat "${pid_file}")"
  if [[ -z "${pid}" ]]; then
    return 0
  fi

  if kill -0 "${pid}" >/dev/null 2>&1; then
    kill "${pid}"
    echo "Stopped existing server process ${pid}."
  fi
}

main() {
  if [[ "${1:-}" == "--help" || "${1:-}" == "-h" ]]; then
    print_usage
    return 0
  fi

  if [[ $# -lt 1 ]]; then
    print_usage
    return 1
  fi

  local run_folder="$1"
  shift

  local codebase_path=""
  local port=""

  while [[ $# -gt 0 ]]; do
    case "$1" in
      --codebase-path)
        codebase_path="$2"
        shift 2
        ;;
      --port)
        port="$2"
        shift 2
        ;;
      *)
        echo "Unknown argument: $1" >&2
        print_usage
        return 1
        ;;
    esac
  done

  require_command "curl"
  require_command "dirname"
  require_command "grep"
  require_command "rm"
  require_command "mkdir"
  require_command "python3"
  require_command "tee"
  mkdir -p "${CENTRAL_LOG_DIR}" || true

  if [[ ! -d "${run_folder}" ]]; then
    echo "Run folder not found: ${run_folder}" >&2
    return 1
  fi

  local config_path="${run_folder}/run.config"
  if [[ -f "${config_path}" ]]; then
    # shellcheck source=/dev/null
    source "${config_path}"
  fi

  if [[ -z "${codebase_path}" && -n "${CODEBASE_PATH:-}" ]]; then
    codebase_path="${CODEBASE_PATH}"
  fi
  if [[ -z "${port}" && -n "${PORT:-}" ]]; then
    port="${PORT}"
  fi

  if [[ -z "${codebase_path}" ]]; then
    echo "Codebase path is required. Pass --codebase-path or provide run.config with CODEBASE_PATH." >&2
    return 1
  fi
  if [[ -z "${port}" ]]; then
    port="7777"
  fi
  if [[ ! -d "${codebase_path}" ]]; then
    echo "Codebase path does not exist: ${codebase_path}" >&2
    return 1
  fi

  local binary_path
  binary_path="$(resolve_binary_path "${run_folder}")"

  local version_output
  version_output="$("${binary_path}" --version 2>&1 || true)"
  if [[ "${version_output}" != *"${PARSELTONGUE_VERSION}"* ]]; then
    echo "Version check failed. Expected parseltongue ${PARSELTONGUE_VERSION}." >&2
    echo "Actual output: ${version_output}" >&2
    return 1
  fi
  echo "Verified: ${version_output}"
  central_log "REINDEX_START run_dir='${run_folder}' codebase='${codebase_path}'"

  stop_existing_server_if_running "${run_folder}"

  remove_workspace_path_if_safe "${run_folder}" "${WORKSPACE_PATH:-}"
  mkdir -p "${run_folder}/db" "${run_folder}/logs" "${run_folder}/queries"

  local index_log="${run_folder}/logs/index.log"
  echo "Reindexing codebase from inside ${run_folder}"
  (
    cd "${run_folder}"
    "${binary_path}" pt01-folder-to-cozodb-streamer "${codebase_path}" 2>&1
  ) | tee "${index_log}"

  local db_uri
  db_uri="$(resolve_db_uri_from_index_log "${run_folder}" "${index_log}")"
  if ! verify_db_path_exists "${db_uri}"; then
    echo "Resolved database path does not exist: ${db_uri}" >&2
    echo "Inspect index log at ${index_log}" >&2
    return 1
  fi

  local workspace_path
  workspace_path="$(resolve_workspace_path_from_db_uri "${db_uri}")"

  local server_log="${run_folder}/logs/server.log"
  start_detached_server "${binary_path}" "${db_uri}" "${port}" "${server_log}" "${run_folder}/server.pid" "${codebase_path}"
  local server_pid
  server_pid="$(cat "${run_folder}/server.pid")"

  local server_url="http://localhost:${port}"
  if ! wait_for_server "${server_url}"; then
    echo "Server failed health check after reindex. Check logs at ${server_log}" >&2
    central_log "SERVER_HEALTH_FAIL server='${server_url}' run_dir='${run_folder}'"
    return 1
  fi
  central_log "SERVER_HEALTH_OK server='${server_url}' run_dir='${run_folder}' pid=${server_pid}"

  code="$(curl -sS -o "${run_folder}/queries/server-health-check-status.json" -w '%{http_code}' "${server_url}/server-health-check-status" || echo 000)"
  central_log "QUERY endpoint='server-health-check-status' status=${code} server='${server_url}' run_dir='${run_folder}' out='${run_folder}/queries/server-health-check-status.json'"
  code="$(curl -sS -o "${run_folder}/queries/codebase-statistics-overview-summary.json" -w '%{http_code}' "${server_url}/codebase-statistics-overview-summary" || echo 000)"
  central_log "QUERY endpoint='codebase-statistics-overview-summary' status=${code} server='${server_url}' run_dir='${run_folder}' out='${run_folder}/queries/codebase-statistics-overview-summary.json'"
  code="$(curl -sS -o "${run_folder}/queries/file-watcher-status-check.json" -w '%{http_code}' "${server_url}/file-watcher-status-check" || echo 000)"
  central_log "QUERY endpoint='file-watcher-status-check' status=${code} server='${server_url}' run_dir='${run_folder}' out='${run_folder}/queries/file-watcher-status-check.json'"

  {
    printf 'PARSELTONGUE_VERSION=%q\n' "${PARSELTONGUE_VERSION}"
    printf 'CODEBASE_PATH=%q\n' "${codebase_path}"
    printf 'PORT=%q\n' "${port}"
    printf 'DB_URI=%q\n' "${db_uri}"
    printf 'WORKSPACE_PATH=%q\n' "${workspace_path}"
    printf 'INDEX_LOG=%q\n' "${index_log}"
  } > "${run_folder}/run.config"

  cat <<EOF
Reindex complete with parseltongue 1.7.2.
Run folder: ${run_folder}
Binary: ${binary_path}
Workspace: ${workspace_path}
Database URI: ${db_uri}
Server PID: ${server_pid}
Server URL: ${server_url}
EOF
  central_log "REINDEX_COMPLETE run_dir='${run_folder}' server='${server_url}'"
}

main "$@"
