"""Structural regression test for the fiction-vault migration (2026-07-10).

``docs/wiki/fiction/`` was moved to a repository-root ``fiction/`` vault, plus
``creative_harness/`` (craft/methods reference) and ``tools/qfuds-verse-web/``
(the web reader). This locks in three invariants so a future edit cannot
silently resurrect the old layout:

  1. ``docs/wiki/fiction/`` stays gone.
  2. No path under ``fiction/`` carries a prohibited SAGA production family
     segment (``10_story_design``, ``20_drafts``, ``30_revisions``,
     ``40_release``, ``90_archive``, ``00_workroom``, ``20_series``). That
     production track ended on 2026-07-10 and lives in Git history only:
     ``git show bbbcb970:<path>``.
  3. The new vault roots exist.

Run with: python3 -m unittest discover -s tests -p 'test_*.py'
"""
from __future__ import annotations

import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]

PROHIBITED_SAGA_FAMILIES = frozenset((
    "10_story_design",
    "20_drafts",
    "30_revisions",
    "40_release",
    "90_archive",
    "00_workroom",
    "20_series",
))

NEW_ROOTS = (
    "fiction/inbox",
    "fiction/knowledge",
    "fiction/research",
    "fiction/worlds",
    "fiction/projects",
    "creative_harness/craft",
    "creative_harness/methods",
    "tools/qfuds-verse-web/data",
)


class LegacyWikiFictionTests(unittest.TestCase):
    def test_docs_wiki_fiction_does_not_exist(self) -> None:
        self.assertFalse((REPO_ROOT / "docs/wiki/fiction").exists())


class ProhibitedSagaProductionFamiliesTests(unittest.TestCase):
    def test_no_prohibited_family_segment_under_fiction(self) -> None:
        fiction_root = REPO_ROOT / "fiction"
        offending = [
            str(p.relative_to(REPO_ROOT))
            for p in fiction_root.rglob("*")
            if set(p.relative_to(fiction_root).parts) & PROHIBITED_SAGA_FAMILIES
        ]
        self.assertEqual(offending, [])


class NewVaultRootsTests(unittest.TestCase):
    def test_new_roots_exist(self) -> None:
        missing = [r for r in NEW_ROOTS if not (REPO_ROOT / r).is_dir()]
        self.assertEqual(missing, [])


if __name__ == "__main__":
    unittest.main()
