#!/usr/bin/env python3
"""Checks for docs/specs/library-reduction/spec.md. Exit code 0 only when every check passes."""
import hashlib
import os
import re
import subprocess
import sys
from collections import defaultdict

BASELINE = "0dc7115"
SUBJECTS = [
    "agent-context-and-orchestration", "authoring-skills-and-references",
    "claude-plugin-development", "codebase-navigation", "executable-specs",
    "explore-and-decide", "generative-art-and-images", "git-delivery-flow", "kotlin-backend",
    "python", "react-frontend", "review-verify-debug", "stripe-payments", "structured-writing",
    "system-design-and-polyglot", "tdd-progress-and-resume", "typescript-backend",
    "visual-explainers",
]
RUST_SKILLS = [
    "rust-app-service", "rust-cli", "rust-infra-parsers", "rust-infra-performance",
    "rust-infra-storage", "rust-library", "rust-review", "rust-tauri", "rust-unsafe-ffi",
]
RECORD_NAMES = ["progress", "coverage-ledger", "evidence-index", "task-queue", "question-packets"]
PROCESS_TALK = ["seed bullet", "the seed offers", "in this pass", "this session", "was read completely"]
ROOT_DOCS = ["A00-LLM-Principles01.md", "A01-LLM-Workflow01.md", "A02-Mega-Idiomatic-Prompt.md",
             "A03-Executable-Specs01.md"]

ROOT = subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip()
os.chdir(ROOT)
FILES = [f for f in subprocess.check_output(["git", "ls-files", "-z"], text=True).split("\0")
         if f and os.path.exists(f)]


def read(path):
    with open(path, encoding="utf-8", errors="ignore") as handle:
        return handle.read()


def check_no_identical_copies_remain():
    groups = defaultdict(list)
    for f in FILES:
        data = open(f, "rb").read()
        if data.strip():
            groups[hashlib.sha1(data).hexdigest()].append(f)
    extra = sum(len(g) - 1 for g in groups.values())
    return extra == 0, f"{extra} redundant identical copies"


def check_tracked_file_count_limit():
    return len(FILES) <= 120, f"{len(FILES)} tracked files (limit 120)"


def check_every_subject_skill_exists():
    bad = []
    for s in SUBJECTS:
        path = f"library/skills/{s}/SKILL.md"
        if not os.path.exists(path):
            bad.append(s)
            continue
        head = re.match(r"---\n(.*?)\n---\n", read(path), re.S)
        if not head or not re.search(r"^name:", head.group(1), re.M) \
                or not re.search(r"^description:", head.group(1), re.M):
            bad.append(s + " (front matter)")
    return not bad, f"{len(SUBJECTS) - len(bad)}/{len(SUBJECTS)} subject skills present"


def check_skill_directories_stay_small():
    per_dir = defaultdict(list)
    for f in FILES:
        parts = f.split("/")
        if f.startswith("library/skills/") and len(parts) > 3 and f.endswith(".md"):
            per_dir[parts[2]].append("/".join(parts[3:]))
    bad = [d for d, names in per_dir.items() if set(names) - {"SKILL.md", "reference.md"}]
    return not bad, f"{len(bad)} skill directories hold more than SKILL.md and reference.md"


def check_no_production_records_remain():
    dirs = [d for d in ("archive", "projects", "Rust-skills/sources")
            if any(f.startswith(d + "/") for f in FILES)]
    named = [f for f in FILES if any(n in os.path.basename(f) for n in RECORD_NAMES)]
    return not dirs and not named, f"directories present: {dirs or 'none'}; {len(named)} record-named files"


def check_references_omit_process_talk():
    refs = [f for f in FILES if f.startswith("library/skills/") and f.endswith("/reference.md")]
    hits = sum(read(f).lower().count(p) for f in refs for p in PROCESS_TALK)
    old = [f for f in FILES if f.startswith("library/idiomatic/")]
    return hits == 0 and not old, f"{hits} process phrases in {len(refs)} references; {len(old)} unmerged references"


def check_third_party_is_attributed():
    stray = [f for f in FILES if f.startswith(("library/skills/claude/", "library/skills/hermes/"))]
    projects = sorted({f.split("/")[2] for f in FILES
                       if f.startswith("library/third-party/") and f.count("/") > 2})
    attribution = read("library/third-party/ATTRIBUTION.md") if os.path.exists(
        "library/third-party/ATTRIBUTION.md") else ""
    bad = [p for p in projects
           if not os.path.exists(f"library/third-party/{p}/LICENSE") or p not in attribution]
    ok = bool(attribution) and not stray and not bad
    return ok, f"{len(stray)} third-party files outside library/third-party; {len(bad)} projects without licence or attribution"


def check_rust_skills_embed_core():
    core = read("Rust-skills/skills/_core.md").strip()
    missing = [s for s in RUST_SKILLS
               if not os.path.exists(f"Rust-skills/skills/{s}/SKILL.md")
               or core not in read(f"Rust-skills/skills/{s}/SKILL.md")]
    return not missing, f"{len(RUST_SKILLS) - len(missing)}/{len(RUST_SKILLS)} Rust skills embed the shared core"


def check_root_documents_stay_unchanged():
    changed = subprocess.run(["git", "diff", "--quiet", BASELINE, "--"] + ROOT_DOCS).returncode
    return changed == 0, "A00-A03 identical to baseline" if changed == 0 else "A00-A03 differ from baseline"


def links_of(path):
    text = re.sub(r"```.*?```", "", read(path), flags=re.S)
    for target in re.findall(r"\]\(([^)\s]+)\)", text):
        if not re.match(r"[a-z]+:|#", target):
            yield os.path.normpath(os.path.join(os.path.dirname(path), target.split("#")[0]))


def check_library_index_links_skills():
    index = "library/README.md"
    if not os.path.exists(index):
        return False, "library/README.md missing"
    linked = set(links_of(index))
    skills = [f for f in FILES if f.endswith("/SKILL.md") and not f.startswith("library/third-party/")]
    unlisted = [s for s in skills if s not in linked]
    dead = [t for t in linked if not os.path.exists(t)]
    return not unlisted and not dead, f"{len(unlisted)} skills not in the index; {len(dead)} dead index links"


def check_relative_links_all_resolve():
    dead = [(f, t) for f in FILES if f.endswith(".md") and not f.startswith("library/third-party/")
            and f not in ROOT_DOCS
            for t in links_of(f) if not os.path.exists(t)]
    return not dead, f"{len(dead)} broken relative links"


CHECKS = [
    ("REQ-LIB-001.0", check_no_identical_copies_remain),
    ("REQ-LIB-002.0", check_tracked_file_count_limit),
    ("REQ-LIB-003.0", check_every_subject_skill_exists),
    ("REQ-LIB-004.0", check_skill_directories_stay_small),
    ("REQ-LIB-005.0", check_no_production_records_remain),
    ("REQ-LIB-006.0", check_references_omit_process_talk),
    ("REQ-LIB-007.0", check_third_party_is_attributed),
    ("REQ-LIB-008.0", check_rust_skills_embed_core),
    ("REQ-LIB-009.0", check_root_documents_stay_unchanged),
    ("REQ-LIB-010.0", check_library_index_links_skills),
    ("REQ-LIB-011.0", check_relative_links_all_resolve),
]

if __name__ == "__main__":
    failed = 0
    for req, check in CHECKS:
        ok, detail = check()
        failed += not ok
        print(f"{'PASS' if ok else 'FAIL'}  {req}  {check.__name__}: {detail}")
    print("MANUAL  REQ-LIB-012.0  catalogue comparison, reported in the pull request")
    print(f"\n{len(CHECKS) - failed} of {len(CHECKS)} checks pass")
    sys.exit(1 if failed else 0)
