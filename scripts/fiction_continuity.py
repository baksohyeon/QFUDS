#!/usr/bin/env python3
"""Fiction continuity checker — character x arc/era consistency.

Clean-room implementation. The check taxonomy (dead character walking, era /
timeline mismatch) is design-inspired by public fiction-continuity tooling
(danjdewhurst/story-skills continuity engine, MIT, https://github.com/danjdewhurst/story-skills);
no external code was copied. External-tool adoption is governed by
`.agent/workflows/fiction-ip-management-workflow.md` (External Tool and Code
Adoption, fiction only, relaxed 2026-06-30): source recorded here, fiction side
only, never into QFUDS research evidence.

Single source of truth: the canon character map
  docs/wiki/fiction/.../00_bible/024_character_map_and_timeline_coordinates_ko.md

It parses the roster (character -> arc/era) from the `## 인물 표` table and scans
prose drafts under `20_drafts/<부>/`. In this deep-time SAGA the arcs are
millennia apart (1부 = 21c, 2부 = far-future 4기), so a character bound to one
arc appearing in another arc's prose is only valid as a copy/restoration and
must be deliberate. Such cross-era appearances are flagged for review.

Characters whose era cell says `전 시대` or `기원` (e.g. Last Archive, Vera,
Karvath) are background/all-era and exempt.

Deliberate deep-time seeding (a future-arc character intentionally appearing in
an earlier draft, e.g. the 1부 origin seeding 2부's Mara) is registered in 024's
`## 의도된 교차 등장` allowlist (character + draft-arc + optional file numbers)
and suppressed. Cross-era appearances that are NOT registered there still flag,
so the engine stays sensitive to real drift.

Warn-only by default (exit 0). `--strict` makes cross-era appearances block (1).

Usage:
  python3 scripts/fiction_continuity.py            # scan all drafts
  python3 scripts/fiction_continuity.py --staged   # only staged drafts
  python3 scripts/fiction_continuity.py --strict   # exit 1 on cross-era hits
"""
import re
import subprocess
import sys
import pathlib

FICTION_ROOT = "docs/wiki/fiction"
SAGA = FICTION_ROOT + "/10_universes/qfuds-verse/20_series/qfuds-saga"
CHAR_MAP = SAGA + "/00_bible/024_character_map_and_timeline_coordinates_ko.md"
DRAFT_ROOT = SAGA + "/20_drafts"

ARC_DIRS = ("1부", "2부", "3부")
ARC_ORDER = {"1부": 0, "2부": 1, "3부": 2}  # deep-time chronological order
EXEMPT_TOKENS = ("전 시대", "전시대", "기원")  # background / all-era characters
META_HEADINGS = (
    "boundary", "harness applied", "source boundary", "continuity notes",
    "canon", "writing rules", "목적", "안내", "required reads", "series gate",
)
# parenthetical English aliases inside a name cell, e.g. "사엘 (Sael)"
EN_IN_PARENS = re.compile(r"\(([^)]+)\)")


def parse_roster(text):
    """Return [{'tokens': [...], 'arc': '1부'|'2부'|'3부'|None, 'exempt': bool,
    'display': str}] parsed from the `## 인물 표` markdown table."""
    roster = []
    in_table = False
    for line in text.splitlines():
        s = line.strip()
        if s.startswith("## "):
            in_table = s == "## 인물 표"
            continue
        if not in_table or not s.startswith("|"):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if len(cells) < 2:
            continue
        name_cell, era_cell = cells[0], cells[1]
        if name_cell.startswith("---") or "이름" in name_cell:
            continue  # header / separator
        display = name_cell.replace("**", "").strip()
        if not display:
            continue
        exempt = any(tok in era_cell for tok in EXEMPT_TOKENS)
        arc = None
        for a in ARC_DIRS:
            if a in era_cell:
                arc = a
                break
        roster.append({
            "tokens": name_tokens(display),
            "arc": arc,
            "exempt": exempt,
            "display": display,
        })
    return roster


def parse_crossover_allow(text):
    """Return [{'name': str, 'arc': '1부'|..., 'files': set()}] parsed from the
    `## 의도된 교차 등장` table in 024. Each row registers a DELIBERATE cross-era
    appearance (deep-time seeding / handoff) that should be suppressed.

    `name` is the canonical display string (matches the roster `## 인물 표` name
    cell). `arc` is the draft arc the character is allowed to appear in. `files`
    is the set of leading file-number tokens scoping the allowance; an empty set
    means the whole arc.
    """
    allow = []
    in_table = False
    for line in text.splitlines():
        s = line.strip()
        if s.startswith("## "):
            in_table = s.startswith("## 의도된 교차 등장")
            continue
        if not in_table or not s.startswith("|"):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if len(cells) < 2:
            continue
        name_cell, arc_cell = cells[0], cells[1]
        if name_cell.startswith("---") or "인물" in name_cell:
            continue  # header / separator
        name = name_cell.replace("**", "").strip()
        if not name:
            continue
        arc = None
        for a in ARC_DIRS:
            if a in arc_cell:
                arc = a
                break
        if arc is None:
            continue
        files = set()
        if len(cells) >= 3:
            files = set(re.findall(r"\d+", cells[2]))
        allow.append({"name": name, "arc": arc, "files": files})
    return allow


def is_allowed(entry, arc, path, allow):
    """True if (character, draft-arc, file) is a registered deliberate crossover."""
    num = file_num(path)
    for a in allow:
        if a["name"] == entry["display"] and a["arc"] == arc:
            if not a["files"] or (num is not None and num in a["files"]):
                return True
    return False


def file_num(path):
    """Leading file-number token of a draft filename, e.g. '030' -> '030'."""
    m = re.match(r"(\d+)", pathlib.Path(path).name)
    return m.group(1) if m else None


def name_tokens(display):
    """Search tokens from a name cell. KR tokens >=2 chars, EN aliases >=3.

    Short tokens (1-char KR) are dropped to avoid substring false positives.
    """
    en = []
    for m in EN_IN_PARENS.findall(display):
        en.extend(p for p in m.replace(",", " ").split() if len(p) >= 3)
    kr_part = EN_IN_PARENS.sub("", display)
    kr = [t for t in kr_part.split() if len(t) >= 2 and _is_hangul(t)]
    # also keep the full KR phrase and a romanizable EN full string
    return {"kr": sorted(set(kr), key=len, reverse=True), "en": sorted(set(en))}


def _is_hangul(s):
    return any("가" <= ch <= "힣" for ch in s)


def reader_prose(text):
    """Yield (lineno, line) for reader prose; skip frontmatter/code/meta."""
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


def draft_arc(path):
    for a in ARC_DIRS:
        if "/20_drafts/%s/" % a in path:
            return a
    return None


def name_hits(line, entry):
    for t in entry["tokens"]["kr"]:
        # Left-boundary match only: a KR name token counts as a hit when the
        # character before it is not Hangul (line start, space, punctuation).
        # Korean particles attach on the RIGHT, so '누어가'/'누어를' still match,
        # but '누어' inside '나누어'(divide) does not. Avoids substring aliasing.
        idx = line.find(t)
        while idx != -1:
            before = line[idx - 1] if idx > 0 else ""
            if not _is_hangul(before):
                return t
            idx = line.find(t, idx + 1)
    for t in entry["tokens"]["en"]:
        if re.search(r"\b%s\b" % re.escape(t), line):
            return t
    return None


def staged_drafts():
    out = subprocess.run(
        ["git", "diff", "--cached", "--name-only", "--diff-filter=ACMR"],
        capture_output=True, text=True).stdout.split()
    return [f for f in out if f.startswith(DRAFT_ROOT) and f.endswith(".md")]


def all_drafts():
    paths = []
    for a in ARC_DIRS:
        d = pathlib.Path(DRAFT_ROOT) / a
        if d.exists():
            paths += [str(p) for p in d.glob("*.md")
                      if p.name != "README.md" and "/_versions/" not in str(p)]
    return sorted(paths)


def check(drafts, roster, allow):
    flags = []
    bound = [e for e in roster if e["arc"] and not e["exempt"]]
    for f in drafts:
        arc = draft_arc(f)
        if arc is None:
            continue
        try:
            text = pathlib.Path(f).read_text(encoding="utf-8")
        except FileNotFoundError:
            continue
        for entry in bound:
            if entry["arc"] == arc:
                continue
            # Only a FUTURE-arc character appearing in an EARLIER draft is an
            # anomaly (foreknowledge/teaser/drift). A later draft naming an
            # earlier-arc character is a normal historical reference, not a hit.
            if ARC_ORDER.get(entry["arc"], 0) <= ARC_ORDER.get(arc, 0):
                continue
            # Deliberate deep-time seeding registered in 024's allowlist is not
            # a continuity break; unregistered crossovers still flag below.
            if is_allowed(entry, arc, f, allow):
                continue
            for n, ln in reader_prose(text):
                if "](../" in ln or "](docs/" in ln:
                    continue  # doc cross-reference link line, not prose
                hit = name_hits(ln, entry)
                if hit:
                    flags.append(
                        "%s:%d: 시대 불일치 — '%s'(%s 인물)이 %s 원고에 등장"
                        " (딥타임상 사본/복원으로만 가능; 의도면 mark 명시): %s"
                        % (f, n, entry["display"], entry["arc"], arc,
                           ln.strip()[:50]))
                    break  # one flag per character per file is enough
    return flags


def main():
    try:
        map_text = pathlib.Path(CHAR_MAP).read_text(encoding="utf-8")
    except FileNotFoundError:
        print("fiction_continuity: 캐릭터 지도(024)를 찾을 수 없음: %s" % CHAR_MAP)
        return 0
    roster = parse_roster(map_text)
    if not roster:
        print("fiction_continuity: 024에서 인물 표를 파싱하지 못함")
        return 0
    allow = parse_crossover_allow(map_text)
    drafts = staged_drafts() if "--staged" in sys.argv else all_drafts()
    if not drafts:
        print("fiction_continuity: 검사할 원고 없음")
        return 0
    flags = check(drafts, roster, allow)
    if flags:
        print("fiction_continuity: 시대 정합 리뷰 플래그(%d):" % len(flags))
        for fl in flags:
            print("  " + fl)
        if "--strict" in sys.argv:
            print("fiction_continuity: --strict — 커밋 차단. 사본/복원 mark를"
                  " 명시하거나 인물·원고 배치를 024와 맞추세요.")
            return 1
        return 0
    print("fiction_continuity: PASS (%d 인물 / %d 원고, 시대 불일치 없음)"
          % (len([e for e in roster if e["arc"]]), len(drafts)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
