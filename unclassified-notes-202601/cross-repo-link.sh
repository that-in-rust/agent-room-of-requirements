#!/bin/bash
# cross-repo-link.sh
# Links the cross-repo-knowledge-base into any project via symlink.
# Invisible to upstream — uses .git/info/exclude (local-only, never committed).
#
# Usage:
#   From any git project root:
#     ~/cross-repo-knowledge-base/agent-room-of-requirements/cross-repo-link.sh
#
#   Or if added to PATH:
#     cross-repo-link.sh
#
#   Commands:
#     cross-repo-link.sh              Link into current project
#     cross-repo-link.sh unlink       Remove symlink from current project
#     cross-repo-link.sh status       Show link status across all projects
#     cross-repo-link.sh init         First-time setup (clone repo to central location)
#     cross-repo-link.sh sync         Pull latest from remote in the shared repo
#     cross-repo-link.sh push         Commit and push all changes in the shared repo

set -e

CENTRAL_DIR="$HOME/cross-repo-knowledge-base/agent-room-of-requirements"
LINK_NAME="cross-repo-knowledge-base"
REPO_URL="https://github.com/that-in-rust/agent-room-of-requirements.git"

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

cmd_init() {
    if [ -d "$CENTRAL_DIR/.git" ]; then
        echo -e "${YELLOW}Already initialized at $CENTRAL_DIR${NC}"
        return
    fi
    echo "Cloning to $CENTRAL_DIR..."
    mkdir -p "$(dirname "$CENTRAL_DIR")"
    git clone "$REPO_URL" "$CENTRAL_DIR"
    echo -e "${GREEN}Done. Now cd into any project and run: cross-repo-link.sh${NC}"
}

cmd_link() {
    # Verify we're in a git repo
    if [ ! -d ".git" ]; then
        echo -e "${RED}Error: Not in a git repository root.${NC}"
        exit 1
    fi

    # Verify central repo exists
    if [ ! -d "$CENTRAL_DIR/.git" ]; then
        echo -e "${RED}Error: Central repo not found. Run: cross-repo-link.sh init${NC}"
        exit 1
    fi

    # Check if already linked
    if [ -L "$LINK_NAME" ]; then
        echo -e "${YELLOW}Already linked: $LINK_NAME -> $(readlink "$LINK_NAME")${NC}"
        return
    fi

    if [ -e "$LINK_NAME" ]; then
        echo -e "${RED}Error: $LINK_NAME already exists and is not a symlink.${NC}"
        exit 1
    fi

    # Create symlink
    ln -s "$CENTRAL_DIR" "$LINK_NAME"

    # Add to .git/info/exclude (local-only, never committed)
    if ! grep -q "^$LINK_NAME$" .git/info/exclude 2>/dev/null; then
        echo "$LINK_NAME" >> .git/info/exclude
    fi

    # Also exclude parseltongue databases
    if ! grep -q "^parseltongue" .git/info/exclude 2>/dev/null; then
        echo "parseltongue*/" >> .git/info/exclude
    fi

    PROJECT_NAME=$(basename "$(pwd)")
    echo -e "${GREEN}Linked: $LINK_NAME -> $CENTRAL_DIR${NC}"
    echo -e "${GREEN}Hidden from git via .git/info/exclude${NC}"

    # Create project subfolder if it doesn't exist
    if [ ! -d "$CENTRAL_DIR/$PROJECT_NAME" ]; then
        mkdir -p "$CENTRAL_DIR/$PROJECT_NAME"
        echo -e "${GREEN}Created project folder: $LINK_NAME/$PROJECT_NAME/${NC}"
    fi
}

cmd_unlink() {
    if [ -L "$LINK_NAME" ]; then
        rm "$LINK_NAME"
        echo -e "${GREEN}Unlinked: $LINK_NAME removed${NC}"
    else
        echo -e "${YELLOW}No symlink found at $LINK_NAME${NC}"
    fi
}

cmd_status() {
    echo "Central repo: $CENTRAL_DIR"
    if [ -d "$CENTRAL_DIR/.git" ]; then
        echo -e "  Status: ${GREEN}initialized${NC}"
        echo "  Projects:"
        for dir in "$CENTRAL_DIR"/*/; do
            [ -d "$dir" ] && echo "    $(basename "$dir")/"
        done
    else
        echo -e "  Status: ${RED}not initialized${NC}"
        return
    fi

    echo ""
    echo "Current directory: $(pwd)"
    if [ -L "$LINK_NAME" ]; then
        echo -e "  Link: ${GREEN}$LINK_NAME -> $(readlink "$LINK_NAME")${NC}"
    elif [ ! -d ".git" ]; then
        echo -e "  ${YELLOW}Not a git repo${NC}"
    else
        echo -e "  Link: ${YELLOW}not linked${NC} (run: cross-repo-link.sh)"
    fi
}

cmd_sync() {
    if [ ! -d "$CENTRAL_DIR/.git" ]; then
        echo -e "${RED}Error: Central repo not found. Run: cross-repo-link.sh init${NC}"
        exit 1
    fi
    echo "Pulling latest..."
    git -C "$CENTRAL_DIR" pull origin main
    echo -e "${GREEN}Synced.${NC}"
}

cmd_push() {
    if [ ! -d "$CENTRAL_DIR/.git" ]; then
        echo -e "${RED}Error: Central repo not found. Run: cross-repo-link.sh init${NC}"
        exit 1
    fi
    cd "$CENTRAL_DIR"
    if [ -z "$(git status --porcelain)" ]; then
        echo -e "${YELLOW}Nothing to commit.${NC}"
        return
    fi
    echo "Changes:"
    git status --short
    git add -A
    git commit -m "research: update from $(hostname) at $(date +%Y-%m-%d)"
    git push origin main
    echo -e "${GREEN}Pushed.${NC}"
}

# Route commands
case "${1:-link}" in
    init)   cmd_init ;;
    link)   cmd_link ;;
    unlink) cmd_unlink ;;
    status) cmd_status ;;
    sync)   cmd_sync ;;
    push)   cmd_push ;;
    *)
        echo "Usage: cross-repo-link.sh [init|link|unlink|status|sync|push]"
        echo ""
        echo "Commands:"
        echo "  init     First-time setup (clone repo to central location)"
        echo "  link     Link into current git project (default)"
        echo "  unlink   Remove symlink from current project"
        echo "  status   Show link status and project folders"
        echo "  sync     Pull latest from remote"
        echo "  push     Commit and push all changes"
        exit 1
        ;;
esac
