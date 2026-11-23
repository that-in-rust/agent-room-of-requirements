"""Check local Markdown paths, index coverage and Rust block sync. Run with Python 3."""
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills-for-engineering-teams"
INDEX = SKILLS / "README.md"
UPSTREAM = ROOT / "curated-upstream-skill-snapshots"


def local_targets(doc):
    fence = ""
    for line in doc.read_text(encoding="utf-8").splitlines():
        if fence:
            if re.fullmatch(rf" {{0,3}}{fence[0]}{{{len(fence)},}}\s*", line):
                fence = ""
            continue
        marker = re.match(r" {0,3}(`{3,}|~{3,})", line)
        if marker:
            fence = marker[1]
            continue
        for href in re.findall(r"\]\(([^)\s]+)\)", line):
            url = urlsplit(href)
            if url.path and not (url.scheme or url.netloc):
                yield (doc.parent / unquote(url.path)).resolve()


def main():
    tracked = subprocess.check_output(["git", "ls-files", "-z", "--", "*.md"], cwd=ROOT)
    docs = {ROOT / p.decode() for p in tracked.split(b"\0") if p}
    docs.add(INDEX)
    indexed = set()
    errors = []
    for doc in sorted(docs):
        if UPSTREAM in doc.parents and doc != UPSTREAM / "ATTRIBUTION.md":
            continue  # Verbatim upstream snapshots may link outside the copied subset.
        if not doc.is_file():
            errors.append(f"missing: {doc.relative_to(ROOT)}")
            continue
        for target in local_targets(doc):
            if doc == INDEX:
                indexed.add(target)
            if not target.exists():
                errors.append(f"{doc.relative_to(ROOT)}: missing {target}")
    skills = set(SKILLS.glob("*/SKILL.md"))
    for path in sorted(skills - indexed):
        errors.append(f"not indexed: {path.relative_to(ROOT)}")
    if subprocess.run([str(SKILLS / "sync-core.sh"), "--check"]).returncode:
        errors.append("Rust shared blocks failed verification")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Local Markdown paths resolve; {len(skills)} skills indexed; Rust blocks in sync.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
