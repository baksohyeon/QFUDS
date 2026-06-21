#!/usr/bin/env python3
"""Fiction release/commit gate — mechanical enforcement the harness must apply.

The recurring failure was that standards lived in docs but nothing blocked bad
output. This gate blocks (exit 1) on hard, deterministic violations in QFUDS
fiction so they cannot reach a commit:

  - em dash (U+2014) in reader prose of drafts/release files (banned AI-tell)
  - sensitive gender/identity-politics terms anywhere in fiction (사상검증 scrub)
  - staged Korean-primary/adaptation drafts from 019 onward must carry the
    Series Gate Applied table before release-facing edits can land

Soft checks (warn only, exit 0): recurring character without an ensemble entry;
active staged drafts missing the agentic production markers introduced after the
Series Gate.

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
    warns = []
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
        # _versions/ 는 동결된 판본 스냅샷·레거시 보관소다. 활성 산문 규칙(em dash,
        # Series Gate)을 적용하지 않는다(과거 세대는 그대로 보존). 민감어 검사는 유지.
        is_archive = "/_versions/" in f
        # em dash is a banned AI-tell in BOTH Korean and English prose; check
        # episode story files (KR or EN counterpart) but not control/index docs.
        is_story = (not is_archive
                    and any(d in f for d in PROSE_DIRS)
                    and ("korean" in name or "manuscript" in name
                         or "english" in name))
        if is_story:
            for n, ln in reader_prose(text):
                if EMDASH in ln:
                    errs.append("%s:%d: em dash(—) 본문 금지(AI-tell): %s"
                                % (f, n, ln.strip()[:60]))
        if "--staged" in sys.argv and not is_archive and needs_series_gate(f):
            required = (SERIES_GATE, "| POV person |", "| Standalone ban |")
            missing = [r for r in required if r not in text]
            if missing:
                errs.append("%s: Series Gate Applied 표 필수(누락: %s)"
                            % (f, ", ".join(missing)))
        if "--staged" in sys.argv and not is_archive and is_active_draft(f):
            missing_soft = missing_agentic_markers(text)
            if missing_soft:
                warns.append("%s: agentic fiction production marker 권장(누락: %s)"
                             % (f, ", ".join(missing_soft)))
    return errs, warns


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


def is_active_draft(path):
    if "/20_drafts/" not in path or "/_versions/" in path:
        return False
    name = path.rsplit("/", 1)[-1].lower()
    return ("korean" in name or "primary" in name or "adaptation" in name
            or "manuscript" in name or "english" in name)


def missing_agentic_markers(text):
    markers = {
        "Chapter Intent": ("Chapter Intent", "Intent Card", "chapter intent",
                           "intent card", "의도 카드"),
        "Review Wave": ("Review Wave", "review wave", "foundation scan",
                        "re-scan", "리뷰 웨이브"),
        "Chronicler": ("Chronicler", "chronicler", "canon delta",
                       "회수 패스", "chronicler pass"),
    }
    missing = []
    for label, needles in markers.items():
        if not any(needle in text for needle in needles):
            missing.append(label)
    return missing


def main():
    files = staged_fiction() if "--staged" in sys.argv else all_fiction()
    if not files:
        print("fiction_gate: no fiction files to check")
        return 0
    errs, warns = check(files)
    if warns:
        print("fiction_gate: 경고(커밋 차단 아님):")
        for w in warns:
            print("  " + w)
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
