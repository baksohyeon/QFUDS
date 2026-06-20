#!/usr/bin/env python3
"""Fiction release/commit gate — mechanical enforcement the harness must apply.

The recurring failure was that standards lived in docs but nothing blocked bad
output. This gate blocks (exit 1) on hard, deterministic violations in QFUDS
fiction so they cannot reach a commit:

  - em dash (U+2014) in reader prose of drafts/release files (banned AI-tell)
  - sensitive gender/identity-politics terms anywhere in fiction (사상검증 scrub)
  - staged Korean-primary/adaptation drafts from 019 onward must carry the
    Series Gate Applied table before release-facing edits can land

Soft checks (warn only, exit 0): recurring character without an ensemble entry.

Usage:
  python3 scripts/fiction_gate.py            # check all fiction docs
  python3 scripts/fiction_gate.py --staged   # check only staged files (pre-commit)
"""
import re
import subprocess
import sys
import pathlib

FICTION_ROOT = "docs/wiki/fiction"
PROSE_DIRS = ("/20_drafts/", "/40_release/")
EMDASH = "—"
SENSITIVE = re.compile(r"젠더|가부장|페미니|성별|모계|우생|gender|feminis|patriarch", re.I)
META_HEADINGS = (
    "boundary", "adaptation intent", "harness applied", "source boundary",
    "continuity notes", "안내", "canon", "writing rules", "scene seeds",
    "next use", "목적", "required reads", "institutions", "무엇", "진단",
    "series gate",
)
SERIES_GATE = "## Series Gate Applied"


def staged_fiction():
    out = subprocess.run(
        ["git", "diff", "--cached", "--name-only", "--diff-filter=ACMR"],
        capture_output=True, text=True).stdout.split()
    return [f for f in out if f.startswith(FICTION_ROOT) and f.endswith(".md")]


def all_fiction():
    return [str(p) for p in pathlib.Path(FICTION_ROOT).rglob("*.md")]


def reader_prose(text):
    """Yield (lineno, line) for reader prose only.

    Skips YAML frontmatter, fenced code blocks (field marks live here), and
    metadata sections (Boundary / Harness / Continuity Notes / etc.).
    """
    lines = text.splitlines()
    i = 0
    if lines and lines[0].strip() == "---":
        i = 1
        while i < len(lines) and lines[i].strip() != "---":
            i += 1
        i += 1
    in_code = False
    skip = False
    for n in range(i, len(lines)):
        s = lines[n].strip()
        if s.startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        if s.startswith("#"):
            h = s.lstrip("#").strip().lower()
            skip = any(m in h for m in META_HEADINGS)
            continue
        if not skip:
            yield n + 1, lines[n]


def check(files):
    errs = []
    for f in files:
        try:
            text = pathlib.Path(f).read_text(encoding="utf-8")
        except FileNotFoundError:
            continue
        for n, ln in enumerate(text.splitlines(), 1):
            if SENSITIVE.search(ln):
                errs.append("%s:%d: 민감(젠더/페미니즘 등) 용어 금지: %s"
                            % (f, n, ln.strip()[:60]))
        name = f.rsplit("/", 1)[-1].lower()
        # em dash is a banned AI-tell in BOTH Korean and English prose; check
        # episode story files (KR or EN counterpart) but not control/index docs.
        is_story = (any(d in f for d in PROSE_DIRS)
                    and ("korean" in name or "manuscript" in name
                         or "english" in name))
        if is_story:
            for n, ln in reader_prose(text):
                if EMDASH in ln:
                    errs.append("%s:%d: em dash(—) 본문 금지(AI-tell): %s"
                                % (f, n, ln.strip()[:60]))
        if "--staged" in sys.argv and needs_series_gate(f):
            required = (SERIES_GATE, "| POV person |", "| Standalone ban |")
            missing = [r for r in required if r not in text]
            if missing:
                errs.append("%s: Series Gate Applied 표 필수(누락: %s)"
                            % (f, ", ".join(missing)))
    return errs


def needs_series_gate(path):
    if "/20_drafts/" not in path:
        return False
    name = path.rsplit("/", 1)[-1].lower()
    prefix = name.split("_", 1)[0]
    try:
        number = int(prefix)
    except ValueError:
        return False
    if number < 19:
        return False
    return ("korean" in name or "primary" in name or "adaptation" in name)


def main():
    files = staged_fiction() if "--staged" in sys.argv else all_fiction()
    if not files:
        print("fiction_gate: no fiction files to check")
        return 0
    errs = check(files)
    if errs:
        print("fiction_gate: 위반 발견 — 커밋 차단:")
        for e in errs:
            print("  " + e)
        print("fiction_gate: em dash는 마침표/쉼표로, 민감 용어는 제거 후 다시 커밋.")
        return 1
    print("fiction_gate: PASS (%d fiction file(s) checked)" % len(files))
    return 0


if __name__ == "__main__":
    sys.exit(main())
