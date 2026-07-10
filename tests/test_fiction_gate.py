"""Regression tests for scripts/fiction_gate.py path logic.

The 2026-07-10 fiction-vault migration moved fiction content from
``docs/wiki/fiction/`` to a repository-root ``fiction/`` vault (plus
``creative_harness/``). The SAGA production track (drafts, revisions,
release) closed and now lives in Git history only; the only live prose-draft
shelf is a per-project drafts directory (``fiction/projects/*/drafts/``).

These tests lock in that path logic so a future edit cannot silently revert
the gate to scanning a directory that no longer exists.

Run with: python3 -m unittest discover -s tests -p 'test_*.py'
"""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = REPO_ROOT / "scripts"

if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import fiction_gate as gate  # noqa: E402


class ScanRootsTests(unittest.TestCase):
    def test_scan_roots_point_at_the_vault_layout(self) -> None:
        self.assertEqual(gate.FICTION_ROOTS, ("fiction", "creative_harness"))

    def test_all_fiction_finds_real_vault_docs(self) -> None:
        found = gate.all_fiction()
        self.assertTrue(any(f.startswith("fiction/") for f in found))
        self.assertTrue(any(f.startswith("creative_harness/") for f in found))

    def test_all_fiction_does_not_scan_the_legacy_root(self) -> None:
        found = gate.all_fiction()
        self.assertFalse(any(f.startswith("docs/wiki/fiction") for f in found))


class ProjectDraftShelfTests(unittest.TestCase):
    def test_project_draft_path_is_recognized_as_the_draft_shelf(self) -> None:
        # Path-based recognition only fires for filenames that also carry the
        # reader-prose naming convention (korean/primary/adaptation/
        # manuscript/english) — unchanged keyword logic, just repointed to
        # the new directory shape.
        path = "fiction/projects/feathersmcgraw-coda/drafts/003_something_korean_ko.md"
        self.assertTrue(gate.is_active_draft(path))

    def test_real_project_draft_without_prose_naming_is_not_flagged(self) -> None:
        # feathersmcgraw-coda/README.md explicitly overrides the SAGA prose
        # rules for this work; its actual draft filenames don't carry the
        # korean/manuscript/english convention, so they fall outside the
        # gate's active-draft checks as a natural consequence of that.
        path = "fiction/projects/feathersmcgraw-coda/drafts/001_still_eating_spaghetti_ko.md"
        self.assertFalse(gate.is_active_draft(path))

    def test_legacy_saga_draft_path_is_not_matched(self) -> None:
        # SAGA drafts (old 20_series/qfuds-saga/20_drafts shelf) are closed
        # and Git-history-only; the gate must not special-case that path.
        path = "fiction/worlds/qfuds-verse/20_series/qfuds-saga/20_drafts/019_korean_ko.md"
        self.assertFalse(gate.is_active_draft(path))

    def test_non_draft_world_doc_is_not_a_draft(self) -> None:
        path = "fiction/worlds/qfuds-verse/world/101_world_anchor_and_verisimilitude_ko.md"
        self.assertFalse(gate.is_active_draft(path))


if __name__ == "__main__":
    unittest.main()
