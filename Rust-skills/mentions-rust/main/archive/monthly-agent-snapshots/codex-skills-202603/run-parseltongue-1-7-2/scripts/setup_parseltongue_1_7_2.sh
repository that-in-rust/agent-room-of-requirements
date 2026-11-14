#!/usr/bin/env bash
set -euo pipefail

PARSELTONGUE_VERSION="1.7.2"
PARSELTONGUE_TAG="v1.7.2"
PARSELTONGUE_REPO="that-in-rust/parseltongue-rust-LLM-companion"
DEFAULT_RUNS_HOME_TEMPLATE='${CODEX_HOME:-$HOME/.codex}/tool-runs/parseltongue-1-7-2'

# Central log in the skill folder
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
CENTRAL_LOG_DIR="${SKILL_ROOT}/central-logs"
CENTRAL_LOG_FILE="${CENTRAL_LOG_DIR}/parseltongue-query-log.txt"

print_usage() {
  cat <<EOF
Usage:
  setup_parseltongue_1_7_2.sh <codebase_path> [--base-dir DIR] [--port PORT] [--hops N] [--cleanup-days N]

Behavior:
  - Create a fresh timestamped run folder in user space by default
  - Download parseltongue v1.7.2 binary
  - Verify binary reports version 1.7.2
  - Index codebase from inside the run folder
  - Record the actual workspace and DB paths chosen by the binary
  - Start HTTP server, verify watcher health, and run smoke queries

Options:
  --base-dir DIR   Parent folder for run folders (default: ${DEFAULT_RUNS_HOME_TEMPLATE})
  --port PORT      Server port (default: 7777)
  --hops N         Blast radius hops for smoke query (default: 2)
  --cleanup-days N Remove run folders older than N day(s) before setup (default: 1)
EOF
}

detect_asset_name() {
  local uname_s uname_m
  uname_s="$(uname -s)"
  uname_m="$(uname -m)"

  case "${uname_s}:${uname_m}" in
    Darwin:arm64) echo "parseltongue-macos-arm64" ;;
    Darwin:x86_64) echo "parseltongue-macos-x86_64" ;;
    Linux:x86_64) echo "parseltongue-linux-x86_64" ;;
    MINGW64_NT*:x86_64|MSYS_NT*:x86_64|CYGWIN_NT*:x86_64) echo "parseltongue-windows-x86_64.exe" ;;
    *)
      echo "Unsupported platform: ${uname_s} ${uname_m}" >&2
      echo "Supported assets: macOS arm64/x86_64, Linux x86_64, Windows x86_64." >&2
      return 1
      ;;
  esac
}

require_command() {
  local cmd="$1"
  command -v "${cmd}" >/dev/null 2>&1 || {
    echo "Missing required command: ${cmd}" >&2
    return 1
  }
}

default_runs_home_path() {
  if [[ -n "${CODEX_HOME:-}" ]]; then
    echo "${CODEX_HOME}/tool-runs/parseltongue-1-7-2"
  else
    echo "${HOME}/.codex/tool-runs/parseltongue-1-7-2"
  fi
}

build_codebase_slug() {
  local codebase_path="$1"
  local trimmed_path="${codebase_path%/}"
  local base_name="${trimmed_path##*/}"
  local slug

  if [[ -z "${base_name}" ]]; then
    base_name="codebase"
  fi

  slug="$(
    printf '%s' "${base_name}" | \
      tr '[:upper:]' '[:lower:]' | \
      sed -E 's/[^a-z0-9]+/-/g; s/^-+//; s/-+$//; s/^$/codebase/; s/^(.{1,40}).*$/\1/'
  )"

  printf '%s\n' "${slug}"
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

urlencode_component() {
  python3 - "$1" <<'PY'
import sys
import urllib.parse

print(urllib.parse.quote(sys.argv[1], safe=""))
PY
}

wait_for_server() {
  local server_url="$1"
  local retries=20
  local sleep_s=1
  local i

  for ((i = 1; i <= retries; i++)); do
    if curl -fsS "${server_url}/server-health-check-status" >/dev/null 2>&1; then
      return 0
    fi
    sleep "${sleep_s}"
  done

  return 1
}

resolve_server_url_from_log() {
  local server_log="$1"
  local retries=30
  local sleep_s=1
  local i

  for ((i = 1; i <= retries; i++)); do
    if [[ -f "${server_log}" ]]; then
      local server_url
      server_url="$(
        grep -Eo 'http://localhost:[0-9]+' "${server_log}" | tail -n 1 || true
      )"
      if [[ -n "${server_url}" ]]; then
        printf '%s\n' "${server_url}"
        return 0
      fi
    fi
    sleep "${sleep_s}"
  done

  return 1
}

resolve_db_uri_from_index_log() {
  local run_dir="$1"
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
    db_path="${run_dir}/${db_path}"
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

mtime_epoch_for_path() {
  local path="$1"

  if stat -f %m "${path}" >/dev/null 2>&1; then
    stat -f %m "${path}"
    return 0
  fi

  if stat -c %Y "${path}" >/dev/null 2>&1; then
    stat -c %Y "${path}"
    return 0
  fi

  echo "Unable to read mtime for path: ${path}" >&2
  return 1
}

cleanup_old_run_folders() {
  local base_dir="$1"
  local cleanup_days="$2"
  local now_epoch max_age_seconds
  local removed_count=0

  now_epoch="$(date +%s)"
  max_age_seconds=$((cleanup_days * 86400))

  shopt -s nullglob
  local run_path
  for run_path in "${base_dir}/parseltongue-${PARSELTONGUE_VERSION}-"*; do
    [[ -d "${run_path}" ]] || continue

    local mtime_epoch age_seconds
    mtime_epoch="$(mtime_epoch_for_path "${run_path}")" || continue
    age_seconds=$((now_epoch - mtime_epoch))

    if (( age_seconds > max_age_seconds )); then
      rm -rf "${run_path}"
      echo "Cleaned old run folder: ${run_path}"
      removed_count=$((removed_count + 1))
    fi
  done
  shopt -u nullglob

  echo "Cleanup complete: removed ${removed_count} folder(s) older than ${cleanup_days} day(s)."
}

central_log() {
  mkdir -p "${CENTRAL_LOG_DIR}" || true
  local ts
  ts="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  echo "${ts} | $*" >> "${CENTRAL_LOG_FILE}"
}

capture_query_output() {
  local server_url="$1"
  local endpoint="$2"
  local output_file="$3"
  local required="${4:-false}"
  local http_code
  http_code="$(curl -sS -o "${output_file}" -w '%{http_code}' "${server_url}/${endpoint}" || echo "000")"

  central_log "QUERY endpoint='${endpoint}' status=${http_code} server='${server_url}' run_dir='${run_dir}' out='${output_file}'"

  if [[ "${required}" == "true" ]]; then
    if [[ "${http_code}" != 2* ]]; then
      echo "Required query failed: ${server_url}/${endpoint} (HTTP ${http_code})" >&2
      return 1
    fi
  else
    if [[ "${http_code}" != 2* ]]; then
      echo "Warning: optional query failed: ${server_url}/${endpoint} (HTTP ${http_code})" >&2
    fi
  fi
  return 0
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

  local codebase_path="$1"
  shift

  local base_dir
  base_dir="$(default_runs_home_path)"
  local port="7777"
  local hops="2"
  local cleanup_days="1"

  while [[ $# -gt 0 ]]; do
    case "$1" in
      --base-dir)
        base_dir="$2"
        shift 2
        ;;
      --port)
        port="$2"
        shift 2
        ;;
      --hops)
        hops="$2"
        shift 2
        ;;
      --cleanup-days)
        cleanup_days="$2"
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
  require_command "date"
  require_command "dirname"
  require_command "grep"
  require_command "mkdir"
  require_command "mktemp"
  require_command "python3"
  require_command "rm"
  require_command "sed"
  require_command "stat"
  require_command "tee"
  require_command "tr"
  mkdir -p "${CENTRAL_LOG_DIR}" || true

  if ! [[ "${cleanup_days}" =~ ^[0-9]+$ ]]; then
    echo "Invalid --cleanup-days value: ${cleanup_days}. Use a non-negative integer." >&2
    return 1
  fi

  if [[ ! -d "${codebase_path}" ]]; then
    echo "Codebase path does not exist: ${codebase_path}" >&2
    return 1
  fi

  local asset_name
  asset_name="$(detect_asset_name)"
  local release_url="https://github.com/${PARSELTONGUE_REPO}/releases/download/${PARSELTONGUE_TAG}/${asset_name}"

  mkdir -p "${base_dir}"
  cleanup_old_run_folders "${base_dir}" "${cleanup_days}"

  local timestamp run_dir codebase_slug
  timestamp="$(date +"%Y%m%d-%H%M%S")"
  codebase_slug="$(build_codebase_slug "${codebase_path}")"
  run_dir="${base_dir}/parseltongue-${PARSELTONGUE_VERSION}-${codebase_slug}-${timestamp}"
  mkdir -p "${run_dir}/bin" "${run_dir}/db" "${run_dir}/logs" "${run_dir}/queries"
  central_log "SETUP_START run_dir='${run_dir}' codebase='${codebase_path}' base_dir='${base_dir}'"

  local binary_path="${run_dir}/bin/parseltongue"
  if [[ "${asset_name}" == *.exe ]]; then
    binary_path="${run_dir}/bin/parseltongue.exe"
  fi

  echo "Downloading parseltongue ${PARSELTONGUE_VERSION} from:"
  echo "  ${release_url}"
  curl -fL "${release_url}" -o "${binary_path}"
  chmod +x "${binary_path}"

  local version_output
  version_output="$("${binary_path}" --version 2>&1 || true)"
  if [[ "${version_output}" != *"${PARSELTONGUE_VERSION}"* ]]; then
    echo "Version check failed. Expected parseltongue ${PARSELTONGUE_VERSION}." >&2
    echo "Actual output: ${version_output}" >&2
    return 1
  fi

  echo "Verified: ${version_output}"

  local index_log="${run_dir}/logs/index.log"
  echo "Indexing codebase from inside ${run_dir}"
  (
    cd "${run_dir}"
    "${binary_path}" pt01-folder-to-cozodb-streamer "${codebase_path}" 2>&1
  ) | tee "${index_log}"

  local db_uri
  db_uri="$(resolve_db_uri_from_index_log "${run_dir}" "${index_log}")"
  if ! verify_db_path_exists "${db_uri}"; then
    echo "Resolved database path does not exist: ${db_uri}" >&2
    echo "Inspect index log at ${index_log}" >&2
    return 1
  fi

  local workspace_path
  workspace_path="$(resolve_workspace_path_from_db_uri "${db_uri}")"

  local server_log="${run_dir}/logs/server.log"
  : > "${server_log}"
  echo "Starting query server on requested port ${port}"
  start_detached_server "${binary_path}" "${db_uri}" "${port}" "${server_log}" "${run_dir}/server.pid" "${codebase_path}"
  local server_pid
  server_pid="$(cat "${run_dir}/server.pid")"

  local server_url
  server_url="$(resolve_server_url_from_log "${server_log}")" || {
    echo "Could not determine actual server URL from ${server_log}" >&2
    return 1
  }
  local actual_port="${server_url##*:}"

  if ! wait_for_server "${server_url}"; then
    echo "Server failed health check. Check logs at ${server_log}" >&2
    central_log "SERVER_HEALTH_FAIL server='${server_url}' run_dir='${run_dir}'"
    return 1
  fi
  central_log "SERVER_HEALTH_OK server='${server_url}' run_dir='${run_dir}' pid=${server_pid}"

  {
    printf 'PARSELTONGUE_VERSION=%q\n' "${PARSELTONGUE_VERSION}"
    printf 'CODEBASE_PATH=%q\n' "${codebase_path}"
    printf 'REQUESTED_PORT=%q\n' "${port}"
    printf 'PORT=%q\n' "${actual_port}"
    printf 'SERVER_URL=%q\n' "${server_url}"
    printf 'DB_URI=%q\n' "${db_uri}"
    printf 'WORKSPACE_PATH=%q\n' "${workspace_path}"
    printf 'INDEX_LOG=%q\n' "${index_log}"
  } > "${run_dir}/run.config"

  capture_query_output "${server_url}" "server-health-check-status" "${run_dir}/queries/server-health-check-status.json" "true"
  capture_query_output "${server_url}" "codebase-statistics-overview-summary" "${run_dir}/queries/codebase-statistics-overview-summary.json" "true"
  capture_query_output "${server_url}" "file-watcher-status-check" "${run_dir}/queries/file-watcher-status-check.json" "false"
  capture_query_output "${server_url}" "folder-structure-discovery-tree" "${run_dir}/queries/folder-structure-discovery-tree.json" "false"

  if ! grep -q '"file_watcher_active":true' "${run_dir}/queries/server-health-check-status.json"; then
    echo "Warning: server is healthy but file watcher is not yet reported as active." >&2
    echo "Check ${run_dir}/queries/file-watcher-status-check.json and ${server_log}" >&2
  fi

  local first_key
  first_key="$(
    curl -fsS "${server_url}/code-entities-list-all" | \
      jq -r '.data.entities[0].key // empty' 2>/dev/null || true
  )"

  if [[ -n "${first_key}" ]]; then
    local first_key_encoded
    first_key_encoded="$(urlencode_component "${first_key}")"

    capture_query_output "${server_url}" \
      "blast-radius-impact-analysis?entity=${first_key_encoded}&hops=${hops}" \
      "${run_dir}/queries/blast-radius-impact-analysis.json" \
      "false"

    capture_query_output "${server_url}" \
      "smart-context-token-budget?focus=${first_key_encoded}&tokens=4000" \
      "${run_dir}/queries/smart-context-token-budget.json" \
      "false"
  fi

  cat <<EOF
parseltongue 1.7.2 setup complete.
Run folder: ${run_dir}
Binary: ${binary_path}
Workspace: ${workspace_path}
Database URI: ${db_uri}
Server PID: ${server_pid}
Server URL: ${server_url}
Cleanup policy: remove folders older than ${cleanup_days} day(s)

Next queries:
  curl -fsS "${server_url}/code-entities-search-fuzzy?q=main"
  curl -fsS "${server_url}/circular-dependency-detection-scan"
  curl -fsS "${server_url}/complexity-hotspots-ranking-view?top=10"
EOF

  central_log "SETUP_COMPLETE run_dir='${run_dir}' server='${server_url}'"
}

main "$@"
