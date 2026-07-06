#!/usr/bin/env python3
"""Rename a wiki/fiction markdown doc and update every reference in the repo.

What Obsidian does for GUI renames, this does for agent/CLI renames:

  1. `git mv old new`
  2. Replace the old basename with the new basename across the repo
     (markdown links, scripts, html) so no reference breaks.
  3. If the 3-digit number prefix changed, update link labels that carry the
     old number (e.g. `[026 Q-Day 여파](026_...)` -> `[115 Q-Day 여파](115_...)`).
  4. Scan docs/wiki for links that still point at the old basename (must be 0)
     and report the repo-wide broken-link count for the touched names.

It does NOT touch bare-number prose citations ("충돌 시 025 > 021" 류).
Those are semantic text, not machine-trackable references; if you change a
doc's number, grep for the old number yourself. Shelf band policy
(continuity 0xx / world 1xx / bible 2xx / story 3xx / workroom 4xx, mapping in
qfuds-saga/00_workroom/417) exists so numbers should never need to change.

Usage:
  python3 scripts/rename_doc.py <old_path> <new_basename_or_path> [--dry-run]

Examples:
  python3 scripts/rename_doc.py docs/wiki/fiction/.../NNN_old_slug_ko.md NNN_new_slug_ko.md --dry-run

After a real run: python3 scripts/validate_docs.py && python3 scripts/fiction_gate.py
"""

import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SCAN_GLOBS = ["docs/**/*.md", "docs/**/*.html", "docs/**/*.js",
              "scripts/**/*.py", ".agents/**/*.md", ".agent/**/*.md", "*.md"]
LINK = re.compile(r"\]\(([^)#]+\.md)")
TOKEN = re.compile(r"(?<![\d._/-])(\d{3})(?![\d._/-])")


def scan_targets():
    seen = set()
    for pat in SCAN_GLOBS:
        for p in REPO.glob(pat):
            if p.is_file() and ".git" not in p.parts and p not in seen:
                seen.add(p)
                yield p


def broken_links(root: Path) -> int:
    n = 0
    for p in root.rglob("*.md"):
        try:
            text = p.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for mo in LINK.finditer(text):
            target = mo.group(1).strip()
            if target.startswith(("http", "/")) or "`" in target:
                continue
            if not (p.parent / target).exists():
                n += 1
    return n


def main() -> int:
    args = [a for a in sys.argv[1:] if a != "--dry-run"]
    dry = "--dry-run" in sys.argv
    if len(args) != 2:
        print(__doc__)
        return 2

    old_path = (REPO / args[0]).resolve() if not Path(args[0]).is_absolute() else Path(args[0])
    if not old_path.exists():
        print(f"error: {old_path} not found")
        return 1
    new_arg = Path(args[1])
    new_path = old_path.parent / new_arg.name if new_arg.parent == Path(".") else (REPO / new_arg)
    if new_path.exists():
        print(f"error: {new_path} already exists")
        return 1

    old_name, new_name = old_path.name, new_path.name
    old_pref = old_name[:3] if re.match(r"\d{3}_", old_name) else None
    new_pref = new_name[:3] if re.match(r"\d{3}_", new_name) else None

    baseline_broken = broken_links(REPO / "docs/wiki")

    print(f"{'[dry-run] ' if dry else ''}git mv {old_path.relative_to(REPO)} -> {new_path.relative_to(REPO)}")
    if not dry:
        subprocess.run(["git", "mv", str(old_path), str(new_path)], check=True, cwd=REPO)

    changed = 0
    for p in scan_targets():
        try:
            text = p.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if old_name not in text:
            continue
        text = text.replace(old_name, new_name)
        # link labels carrying the old number prefix, adjacent to the renamed target
        if old_pref and new_pref and old_pref != new_pref:
            def fix_label(mo):
                label = mo.group(1)
                if old_pref in TOKEN.findall(label):
                    label = TOKEN.sub(lambda t: new_pref if t.group(1) == old_pref else t.group(1), label)
                return "[" + label + "](" + mo.group(2)
            text = re.sub(r"\[([^\]]*)\]\((" + re.escape(new_name) + r"|[^)]*/" + re.escape(new_name) + r")",
                          fix_label, text)
        changed += 1
        print(f"  update refs: {p.relative_to(REPO)}")
        if not dry:
            p.write_text(text, encoding="utf-8")

    if dry:
        print(f"[dry-run] {changed} file(s) would be updated. no changes written.")
        return 0

    leftovers = [str(p.relative_to(REPO)) for p in scan_targets()
                 if old_name in (p.read_text(encoding="utf-8", errors="ignore"))]
    after_broken = broken_links(REPO / "docs/wiki")
    print(f"refs updated in {changed} file(s); old-name leftovers: {len(leftovers)}")
    for l in leftovers:
        print("  LEFTOVER:", l)
    print(f"docs/wiki broken links: {baseline_broken} -> {after_broken}"
          + (" (NEW BREAKAGE, investigate)" if after_broken > baseline_broken else ""))
    if old_pref != new_pref:
        print(f"note: number changed {old_pref}->{new_pref}. 산문 속 맨 번호 인용은 자동 갱신되지 않는다:")
        print(f"  grep -rn '\\b{old_pref}\\b' docs/wiki/fiction --include='*.md'")
    print("next: python3 scripts/validate_docs.py && python3 scripts/fiction_gate.py")
    return 1 if (leftovers or after_broken > baseline_broken) else 0


if __name__ == "__main__":
    sys.exit(main())
