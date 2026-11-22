#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Collect a repo-wide GHCLI context snapshot.

Usage:
  collect_repo_context.sh --repo OWNER/REPO --output-dir PATH [--since ISO8601] [--max-pages N] [--no-discussions]

Examples:
  collect_repo_context.sh --repo cli/cli --output-dir /tmp/cli-context
  collect_repo_context.sh --repo cli/cli --output-dir /tmp/cli-context --since 2026-01-01T00:00:00Z --max-pages 3
EOF
}

die() {
  echo "error: $*" >&2
  exit 1
}

require_cmd() {
  command -v "$1" >/dev/null 2>&1 || die "missing required command: $1"
}

repo=""
output_dir=""
since=""
max_pages="5"
include_discussions=1

fetch_rest_pages() {
  local endpoint="$1"
  local output_path="$2"
  local page=1
  local first=1
  local response=""

  : > "$output_path"
  printf '[' >> "$output_path"

  while true; do
    if [[ "$max_pages" -gt 0 && "$page" -gt "$max_pages" ]]; then
      break
    fi

    response="$(gh api -X GET "${endpoint}&page=${page}")"
    if [[ "$response" == "[]" ]]; then
      break
    fi

    if [[ "$first" -eq 0 ]]; then
      printf ',\n' >> "$output_path"
    fi
    printf '%s' "$response" >> "$output_path"
    first=0
    page=$((page + 1))
  done

  printf ']\n' >> "$output_path"
}

fetch_discussion_pages() {
  local output_path="$1"
  local page=1
  local first=1
  local end_cursor="null"
  local response=""
  local next_info=""
  local has_next=""
  local next_cursor=""

  : > "$output_path"
  printf '[' >> "$output_path"

  while true; do
    if [[ "$max_pages" -gt 0 && "$page" -gt "$max_pages" ]]; then
      break
    fi

    if [[ "$end_cursor" == "null" ]]; then
      response="$(gh api graphql \
        -F owner="$owner" \
        -F name="$name" \
        -f query='
query($owner: String!, $name: String!, $endCursor: String) {
  repository(owner: $owner, name: $name) {
    discussions(first: 100, after: $endCursor, orderBy: {field: UPDATED_AT, direction: DESC}) {
      nodes {
        number
        title
        url
        createdAt
        updatedAt
        answerChosenAt
        category { name }
        author { login }
        comments { totalCount }
      }
      pageInfo {
        hasNextPage
        endCursor
      }
    }
  }
}')"
    else
      response="$(gh api graphql \
        -F owner="$owner" \
        -F name="$name" \
        -F endCursor="$end_cursor" \
        -f query='
query($owner: String!, $name: String!, $endCursor: String) {
  repository(owner: $owner, name: $name) {
    discussions(first: 100, after: $endCursor, orderBy: {field: UPDATED_AT, direction: DESC}) {
      nodes {
        number
        title
        url
        createdAt
        updatedAt
        answerChosenAt
        category { name }
        author { login }
        comments { totalCount }
      }
      pageInfo {
        hasNextPage
        endCursor
      }
    }
  }
}')"
    fi

    if [[ "$first" -eq 0 ]]; then
      printf ',\n' >> "$output_path"
    fi
    printf '%s' "$response" >> "$output_path"
    first=0

    next_info="$(python3 - <<'PY' "$response"
import json
import sys

payload = json.loads(sys.argv[1])
page_info = payload["data"]["repository"]["discussions"]["pageInfo"]
print("true" if page_info["hasNextPage"] else "false")
print(page_info["endCursor"] or "")
PY
)"
    has_next="$(printf '%s\n' "$next_info" | sed -n '1p')"
    next_cursor="$(printf '%s\n' "$next_info" | sed -n '2p')"

    if [[ "$has_next" != "true" || -z "$next_cursor" ]]; then
      break
    fi

    end_cursor="$next_cursor"
    page=$((page + 1))
  done

  printf ']\n' >> "$output_path"
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --repo)
      repo="${2:-}"
      shift 2
      ;;
    --output-dir)
      output_dir="${2:-}"
      shift 2
      ;;
    --since)
      since="${2:-}"
      shift 2
      ;;
    --max-pages)
      max_pages="${2:-}"
      shift 2
      ;;
    --no-discussions)
      include_discussions=0
      shift
      ;;
    --help|-h)
      usage
      exit 0
      ;;
    *)
      die "unknown argument: $1"
      ;;
  esac
done

[[ -n "$repo" ]] || die "--repo is required"
[[ -n "$output_dir" ]] || die "--output-dir is required"
[[ "$repo" == */* ]] || die "--repo must be in OWNER/REPO form"
[[ "$max_pages" =~ ^[0-9]+$ ]] || die "--max-pages must be a non-negative integer"

require_cmd gh
require_cmd python3

if ! gh auth status --active >/dev/null 2>&1; then
  die "gh authentication is not healthy; run 'gh auth login' or set GH_TOKEN/GITHUB_TOKEN"
fi

owner="${repo%%/*}"
name="${repo#*/}"
collected_at="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"

mkdir -p "$output_dir/raw"

echo "Collecting repo metadata..."
gh repo view "$repo" \
  --json nameWithOwner,description,defaultBranchRef,hasDiscussionsEnabled,isPrivate,owner,pushedAt,url,visibility \
  > "$output_dir/raw/repo.json"

default_branch="$(gh api "repos/$repo" --jq '.default_branch')"
has_discussions_enabled="$(gh repo view "$repo" --json hasDiscussionsEnabled --jq '.hasDiscussionsEnabled')"

commit_endpoint="repos/$repo/commits?sha=$default_branch&per_page=100"
if [[ -n "$since" ]]; then
  commit_endpoint="${commit_endpoint}&since=${since}"
fi

echo "Collecting commits from default branch..."
fetch_rest_pages "$commit_endpoint" "$output_dir/raw/commits.json"

echo "Collecting pull requests..."
fetch_rest_pages \
  "repos/$repo/pulls?state=all&sort=updated&direction=desc&per_page=100" \
  "$output_dir/raw/pulls.json"

echo "Collecting issues and pull-request issue records..."
fetch_rest_pages \
  "repos/$repo/issues?state=all&sort=updated&direction=desc&per_page=100" \
  "$output_dir/raw/issues_and_pull_requests.json"

echo "Collecting issue comments..."
fetch_rest_pages \
  "repos/$repo/issues/comments?sort=updated&direction=desc&per_page=100" \
  "$output_dir/raw/issue_comments.json"

echo "Collecting pull-request review comments..."
fetch_rest_pages \
  "repos/$repo/pulls/comments?sort=updated&direction=desc&per_page=100" \
  "$output_dir/raw/review_comments.json"

echo "Collecting commit comments..."
fetch_rest_pages \
  "repos/$repo/comments?sort=updated&direction=desc&per_page=100" \
  "$output_dir/raw/commit_comments.json"

if [[ "$include_discussions" -eq 1 && "$has_discussions_enabled" == "true" ]]; then
  echo "Collecting Discussions index..."
  fetch_discussion_pages "$output_dir/raw/discussions_index.json"
fi

python3 - "$output_dir/manifest.json" "$repo" "$owner" "$name" "$default_branch" "$collected_at" "$since" "$max_pages" "$include_discussions" "$has_discussions_enabled" <<'PY'
import json
import sys

(
    path,
    repo,
    owner,
    name,
    default_branch,
    collected_at,
    since,
    max_pages,
    include_discussions,
    has_discussions_enabled,
) = sys.argv[1:]

manifest = {
    "capture_type": "repo",
    "repo": repo,
    "owner": owner,
    "name": name,
    "default_branch": default_branch,
    "collected_at": collected_at,
    "since": since or None,
    "max_pages": int(max_pages),
    "include_discussions": include_discussions == "1",
    "has_discussions_enabled": has_discussions_enabled == "true",
}

with open(path, "w", encoding="utf-8") as handle:
    json.dump(manifest, handle, indent=2)
    handle.write("\n")
PY

echo "Repo snapshot written to $output_dir"
