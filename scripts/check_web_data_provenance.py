#!/usr/bin/env python3
"""Fail when the fiction codex web data files carry stale doc-number references.

The web app's two hand-authored data files
(``web/data/chronicle-data.js`` and ``lore-data.js``) reference source docs by
number in their prose and header comments. Shelf-band renumbering
(``00_workroom/417_shelf_renumber_map_ko.md``) silently turned those numbers
stale, and a by-hand fix pass missed several. This guard makes such drift a
hard failure instead of a thing a human has to remember.

It is a *referential-integrity* check, not retrieval: every shelf-qualified
token on a retained shelf (``world 113``, ``continuity 003``, ``bible 201``)
must resolve to a doc that currently exists on that shelf. Tokens on closed
SAGA shelves (``story``, ``workroom``, ``draft``, ``prototype``) are
history-only references and are accepted as-is. Bare numbers and years
(``(2008)``, ``(039)``) are deliberately ignored — they are ambiguous across
shelves after renumbering, so provenance refs must be shelf-qualified to be
checkable.

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
WORLDS = ROOT / "fiction/worlds/qfuds-verse"
LEGACY_VERSE = ROOT / "docs/wiki/fiction/10_universes/qfuds-verse"
LEGACY_SAGA = LEGACY_VERSE / "20_series/qfuds-saga"

# Retained shelves: keyword -> candidate directories, first existing wins.
# The 2026-07-10 fiction separation moves these from the legacy wiki path to
# the repository-root fiction vault; target, mid-migration (moved but not yet
# renamed), and legacy paths are all accepted so the guard stays green at
# every migration commit boundary.
SHELF_DIR_CANDIDATES: dict[str, tuple[Path, ...]] = {
    "continuity": (
        WORLDS / "continuity",
        WORLDS / "00_continuity",
        LEGACY_VERSE / "00_continuity",
    ),
    "world": (
        WORLDS / "world",
        WORLDS / "10_world",
        LEGACY_VERSE / "10_world",
    ),
    "bible": (
        WORLDS / "series-bible",
        WORLDS / "20_series/qfuds-saga/00_bible",
        LEGACY_SAGA / "00_bible",
    ),
}

# Closed shelves: the SAGA production track (story design, drafts, revisions,
# release, workroom) ended on 2026-07-10 and lives in Git history only
# (`git show bbbcb970:<path>`). Their tokens are historical references and
# cannot be validated against the working tree.
HISTORY_ONLY_KEYS = ("story", "workroom", "draft", "prototype")

DATA_FILE_CANDIDATES: list[tuple[Path, ...]] = [
    (
        ROOT / "tools/qfuds-verse-web/data/chronicle-data.js",
        WORLDS / "web/data/chronicle-data.js",
        LEGACY_VERSE / "web/data/chronicle-data.js",
    ),
    (
        ROOT / "tools/qfuds-verse-web/data/lore-data.js",
        WORLDS / "web/data/lore-data.js",
        LEGACY_VERSE / "web/data/lore-data.js",
    ),
]

SHELF_KEYWORDS = tuple(SHELF_DIR_CANDIDATES) + HISTORY_ONLY_KEYS

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


def resolve_shelf_dir(shelf: str) -> Path:
    """Return the first existing candidate directory for a retained shelf.

    Falls back to the first candidate (the target fiction-vault path) when
    none exists yet, so error messages name the intended location.
    """
    candidates = SHELF_DIR_CANDIDATES[shelf]
    for path in candidates:
        if path.exists():
            return path
    return candidates[0]


def resolve_data_files() -> list[Path]:
    """Return the first existing candidate for each web data file."""
    resolved: list[Path] = []
    for candidates in DATA_FILE_CANDIDATES:
        chosen = next((p for p in candidates if p.exists()), candidates[0])
        resolved.append(chosen)
    return resolved


def build_truth_map() -> dict[str, "set[int] | None"]:
    """Map each shelf keyword to its existing doc numbers.

    Closed shelves map to ``None``: their references are history-only and are
    never validated against the working tree.
    """
    truth: dict[str, set[int] | None] = {
        shelf: numbers_in_dir(resolve_shelf_dir(shelf))
        for shelf in SHELF_DIR_CANDIDATES
    }
    for key in HISTORY_ONLY_KEYS:
        truth[key] = None
    return truth


def find_unresolved(text: str, truth: "dict[str, set[int] | None]") -> list[Problem]:
    """Return every shelf-qualified reference in ``text`` that does not resolve."""
    problems: list[Problem] = []
    for lineno, line in enumerate(text.splitlines(), start=1):
        for match in TOKEN_RE.finditer(line):
            shelf, nums = match.group(1), match.group(2)
            valid = truth.get(shelf, set())
            if valid is None:
                continue
            for number in expand_numbers(nums):
                if number not in valid:
                    problems.append(Problem(lineno, shelf, nums, number))
    return problems


def check_files(paths: list[Path], truth: "dict[str, set[int] | None]") -> list[str]:
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
    data_files = resolve_data_files()
    errors = check_files(data_files, truth)
    if errors:
        print("web data provenance guard: FAILED")
        for error in errors:
            print(f"  {error}")
        print(
            "\nEvery provenance reference must be shelf-qualified and resolve to a "
            "current doc on a retained shelf\n(continuity/world/bible). Closed "
            "SAGA shelves are history-only: `git show bbbcb970:<path>`."
        )
        return 2
    checked = ", ".join(p.name for p in data_files)
    print(f"web data provenance guard: passed ({checked})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
