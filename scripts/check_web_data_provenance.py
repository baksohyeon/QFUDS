#!/usr/bin/env python3
"""Fail when the fiction codex web data files carry stale doc-number references.

The web app's two hand-authored data files
(``web/data/chronicle-data.js`` and ``lore-data.js``) reference source docs by
number in their prose and header comments. Shelf-band renumbering
(``00_workroom/417_shelf_renumber_map_ko.md``) silently turned those numbers
stale, and a by-hand fix pass missed several. This guard makes such drift a
hard failure instead of a thing a human has to remember.

It is a *referential-integrity* check, not retrieval: every shelf-qualified
token (``world 113``, ``continuity 003``, ``draft 024``) must resolve to a doc
that currently exists on that shelf. Bare numbers and years (``(2008)``,
``(039)``) are deliberately ignored — they are ambiguous across shelves after
renumbering, so provenance refs must be shelf-qualified to be checkable.

Stack: Python standard library only (re, pathlib).

Usage:
    python3 scripts/check_web_data_provenance.py

Read-only. Exit 0 when every reference resolves, exit 2 otherwise.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import NamedTuple

ROOT = Path(__file__).resolve().parents[1]
VERSE = ROOT / "docs/wiki/fiction/10_universes/qfuds-verse"
SAGA = VERSE / "20_series/qfuds-saga"

# Renumbered shelves: keyword -> directory holding NNN_*.md docs. The band
# renumber gave each a unique range (continuity 0xx, world 1xx, bible 2xx,
# story 3xx, workroom 4xx), so a shelf keyword plus number is unambiguous.
SHELF_DIRS: dict[str, Path] = {
    "continuity": VERSE / "00_continuity",
    "world": VERSE / "10_world",
    "bible": SAGA / "00_bible",
    "story": SAGA / "10_story_design",
    "workroom": SAGA / "00_workroom",
}

# Invariant docs kept their old numbers by the renumber rule (drafts 029-036,
# prototypes 015-028, plus revisions/archive/release). Both keywords resolve
# against the union of numbered docs under 20_drafts.
DRAFTS_DIR = SAGA / "20_drafts"
INVARIANT_KEYS = ("draft", "prototype")

DATA_FILES: list[Path] = [
    VERSE / "web/data/chronicle-data.js",
    VERSE / "web/data/lore-data.js",
]

SHELF_KEYWORDS = tuple(SHELF_DIRS) + INVARIANT_KEYS

# A shelf keyword followed by a number expression: a single number, a slash
# list (108/112/113), an inclusive range (117-122), or a mix (101/117-119).
TOKEN_RE = re.compile(
    r"\b(" + "|".join(SHELF_KEYWORDS) + r")\s+(\d+(?:[-/]\d+)*)"
)

# Numeric filename prefix, e.g. "003_far_future...md" -> 3.
NUM_PREFIX_RE = re.compile(r"^(\d+)_")


class Problem(NamedTuple):
    lineno: int
    shelf: str
    token: str
    number: int


def expand_numbers(nums: str) -> list[int]:
    """Expand a number expression into the concrete integers it names.

    Handles slash-separated lists and inclusive ``a-b`` ranges. Leading zeros
    are normalized (``003`` -> ``3``) to match filename-prefix integers.
    """
    out: list[int] = []
    for part in nums.split("/"):
        if "-" in part:
            start, end = part.split("-", 1)
            out.extend(range(int(start), int(end) + 1))
        else:
            out.append(int(part))
    return out


def numbers_in_dir(directory: Path, *, recursive: bool = False) -> set[int]:
    """Return the set of numeric filename prefixes of docs in a directory."""
    if not directory.exists():
        return set()
    paths = directory.rglob("*.md") if recursive else directory.glob("*.md")
    numbers: set[int] = set()
    for path in paths:
        match = NUM_PREFIX_RE.match(path.name)
        if match:
            numbers.add(int(match.group(1)))
    return numbers


def build_truth_map() -> dict[str, set[int]]:
    """Map each shelf keyword to the set of doc numbers that exist on it now."""
    truth = {shelf: numbers_in_dir(path) for shelf, path in SHELF_DIRS.items()}
    drafts = numbers_in_dir(DRAFTS_DIR, recursive=True)
    for key in INVARIANT_KEYS:
        truth[key] = drafts
    return truth


def find_unresolved(text: str, truth: dict[str, set[int]]) -> list[Problem]:
    """Return every shelf-qualified reference in ``text`` that does not resolve."""
    problems: list[Problem] = []
    for lineno, line in enumerate(text.splitlines(), start=1):
        for match in TOKEN_RE.finditer(line):
            shelf, nums = match.group(1), match.group(2)
            valid = truth.get(shelf, set())
            for number in expand_numbers(nums):
                if number not in valid:
                    problems.append(Problem(lineno, shelf, nums, number))
    return problems


def check_files(paths: list[Path], truth: dict[str, set[int]]) -> list[str]:
    """Return human-readable error lines for all unresolved references."""
    errors: list[str] = []
    for path in paths:
        if not path.exists():
            errors.append(f"{path.relative_to(ROOT)}: file not found")
            continue
        text = path.read_text(encoding="utf-8")
        for problem in find_unresolved(text, truth):
            errors.append(
                f"{path.relative_to(ROOT)}:{problem.lineno}: "
                f"`{problem.shelf} {problem.token}` -> number {problem.number} "
                f"does not exist on shelf `{problem.shelf}`"
            )
    return errors


def main() -> int:
    truth = build_truth_map()
    errors = check_files(DATA_FILES, truth)
    if errors:
        print("web data provenance guard: FAILED")
        for error in errors:
            print(f"  {error}")
        print(
            "\nEvery provenance reference must be shelf-qualified and resolve to a "
            "current doc.\nSee the shelf renumber map "
            "(00_workroom/417_shelf_renumber_map_ko.md) for the old->new mapping."
        )
        return 2
    checked = ", ".join(p.name for p in DATA_FILES)
    print(f"web data provenance guard: passed ({checked})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
