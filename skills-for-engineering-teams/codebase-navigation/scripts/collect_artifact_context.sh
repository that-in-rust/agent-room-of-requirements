#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Collect focused GHCLI context for a commit, pull request, issue, or discussion.

Usage:
  collect_artifact_context.sh --repo OWNER/REPO --kind KIND --id VALUE --output-dir PATH

Kinds:
  commit
  pr
  issue
  discussion

Examples:
  collect_artifact_context.sh --repo cli/cli --kind pr --id 10477 --output-dir /tmp/pr-trace
  collect_artifact_context.sh --repo cli/cli --kind commit --id abc1234 --output-dir /tmp/commit-trace
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
kind=""
artifact_id=""
output_dir=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --repo)
      repo="${2:-}"
      shift 2
      ;;
    --kind)
      kind="${2:-}"
      shift 2
      ;;
    --id)
      artifact_id="${2:-}"
      shift 2
      ;;
    --output-dir)
      output_dir="${2:-}"
      shift 2
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
[[ -n "$kind" ]] || die "--kind is required"
[[ -n "$artifact_id" ]] || die "--id is required"
[[ -n "$output_dir" ]] || die "--output-dir is required"

case "$kind" in
  commit|pr|issue|discussion) ;;
  *)
    die "--kind must be one of: commit, pr, issue, discussion"
    ;;
esac

require_cmd gh
require_cmd python3

if ! gh auth status --active >/dev/null 2>&1; then
  die "gh authentication is not healthy; run 'gh auth login' or set GH_TOKEN/GITHUB_TOKEN"
fi

owner="${repo%%/*}"
name="${repo#*/}"
collected_at="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"

mkdir -p "$output_dir/raw"

case "$kind" in
  pr)
    echo "Collecting PR view..."
    gh pr view "$artifact_id" -R "$repo" \
      --json number,title,body,author,comments,commits,files,headRefName,baseRefName,isDraft,labels,mergedAt,reviewDecision,reviews,state,statusCheckRollup,url,createdAt,updatedAt \
      > "$output_dir/raw/pr.json"

    echo "Collecting PR issue timeline..."
    gh api --paginate --slurp -X GET \
      "repos/$repo/issues/$artifact_id/timeline?per_page=100" \
      > "$output_dir/raw/timeline.json"

    echo "Collecting PR review comments..."
    gh api --paginate --slurp -X GET \
      "repos/$repo/pulls/$artifact_id/comments?per_page=100" \
      > "$output_dir/raw/review_comments.json"

    echo "Collecting PR reviews..."
    gh api --paginate --slurp -X GET \
      "repos/$repo/pulls/$artifact_id/reviews?per_page=100" \
      > "$output_dir/raw/reviews.json"
    ;;
  issue)
    echo "Collecting issue view..."
    gh issue view "$artifact_id" -R "$repo" \
      --json number,title,body,author,assignees,comments,closed,closedAt,createdAt,labels,milestone,reactionGroups,state,url,updatedAt \
      > "$output_dir/raw/issue.json"

    echo "Collecting issue timeline..."
    gh api --paginate --slurp -X GET \
      "repos/$repo/issues/$artifact_id/timeline?per_page=100" \
      > "$output_dir/raw/timeline.json"
    ;;
  commit)
    echo "Collecting commit detail..."
    gh api "repos/$repo/commits/$artifact_id" > "$output_dir/raw/commit.json"

    echo "Collecting commit comments..."
    gh api --paginate --slurp -X GET \
      "repos/$repo/commits/$artifact_id/comments?per_page=100" \
      > "$output_dir/raw/commit_comments.json"

    echo "Collecting pull requests associated with commit..."
    gh api --paginate --slurp -X GET \
      "repos/$repo/commits/$artifact_id/pulls?per_page=100" \
      > "$output_dir/raw/associated_pulls.json"
    ;;
  discussion)
    echo "Collecting discussion thread..."
    gh api graphql --paginate --slurp \
      -F owner="$owner" \
      -F name="$name" \
      -F number="$artifact_id" \
      -f query='
query($owner: String!, $name: String!, $number: Int!, $endCursor: String) {
  repository(owner: $owner, name: $name) {
    discussion(number: $number) {
      number
      title
      body
      url
      createdAt
      updatedAt
      answerChosenAt
      category { name }
      author { login }
      comments(first: 100, after: $endCursor) {
        nodes {
          id
          body
          createdAt
          updatedAt
          url
          isAnswer
          author { login }
          replyTo { id }
          replies(first: 100) {
            totalCount
            nodes {
              id
              body
              createdAt
              updatedAt
              url
              isAnswer
              author { login }
              replyTo { id }
            }
          }
        }
        pageInfo {
          hasNextPage
          endCursor
        }
      }
    }
  }
}' \
      > "$output_dir/raw/discussion_thread.json"
    ;;
esac

python3 - "$output_dir/manifest.json" "$repo" "$owner" "$name" "$kind" "$artifact_id" "$collected_at" <<'PY'
import json
import sys

path, repo, owner, name, kind, artifact_id, collected_at = sys.argv[1:]

manifest = {
    "capture_type": "artifact",
    "repo": repo,
    "owner": owner,
    "name": name,
    "kind": kind,
    "id": artifact_id,
    "collected_at": collected_at,
}

with open(path, "w", encoding="utf-8") as handle:
    json.dump(manifest, handle, indent=2)
    handle.write("\n")
PY

echo "Artifact snapshot written to $output_dir"
