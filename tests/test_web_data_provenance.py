"""Regression tests for the web-data provenance guard.

The fiction codex web app ships two hand-authored data files
(``web/data/chronicle-data.js`` and ``lore-data.js``) whose prose carries
doc-number provenance references. Shelf-band renumbering silently made those
references stale. This guard makes such drift a test failure: every
shelf-qualified token (``world 113``, ``draft 024``) must resolve to a doc that
currently exists on that shelf.

These tests lock in the number-expression expansion, the qualified-token
detection (and the deliberate blindness to bare numbers/years), and the
end-to-end "the real data files have no unresolved reference" guarantee.

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

import check_web_data_provenance as guard  # noqa: E402


class ExpandNumbersTests(unittest.TestCase):
    def test_single_number(self) -> None:
        self.assertEqual(guard.expand_numbers("115"), [115])

    def test_leading_zeros_are_normalized(self) -> None:
        self.assertEqual(guard.expand_numbers("003"), [3])

    def test_slash_list(self) -> None:
        self.assertEqual(
            guard.expand_numbers("108/112/113/114"), [108, 112, 113, 114]
        )

    def test_range_is_inclusive(self) -> None:
        self.assertEqual(guard.expand_numbers("117-122"), [117, 118, 119, 120, 121, 122])

    def test_mixed_list_and_range(self) -> None:
        self.assertEqual(guard.expand_numbers("101/117-119"), [101, 117, 118, 119])


class FindUnresolvedTests(unittest.TestCase):
    TRUTH = {
        "world": {113, 117, 118, 119, 120, 121, 122, 126},
        # Snapshot shelves (renamed to slug filenames 2026-07-10; web data is
        # a frozen pre-rename snapshot until the reader rebuild): accepted
        # without validation, same mechanism as history-only.
        "continuity": None,
        "bible": None,
        # Closed shelves (SAGA production ended 2026-07-10): history-only,
        # tokens resolve against Git history instead of the working tree.
        "story": None,
        "workroom": None,
        "draft": None,
        "prototype": None,
    }

    def test_resolving_token_is_clean(self) -> None:
        self.assertEqual(guard.find_unresolved("정본 기전 (world 113)", self.TRUTH), [])

    def test_missing_number_is_flagged(self) -> None:
        problems = guard.find_unresolved("(world 999)", self.TRUTH)
        self.assertEqual(len(problems), 1)
        self.assertEqual(problems[0].shelf, "world")
        self.assertEqual(problems[0].number, 999)
        self.assertEqual(problems[0].lineno, 1)

    def test_bare_number_is_ignored(self) -> None:
        # No shelf keyword -> not a provenance token. Years and legacy bare
        # numbers must never trip the guard.
        self.assertEqual(guard.find_unresolved("2008년, (039), (2020s)", self.TRUTH), [])

    def test_history_only_draft_token_resolves(self) -> None:
        self.assertEqual(guard.find_unresolved("SAGA 부 좌표(draft 024)", self.TRUTH), [])

    def test_history_only_story_token_resolves(self) -> None:
        # story shelf was closed with the SAGA project; any story token is a
        # historical reference and must not fail against the working tree.
        self.assertEqual(guard.find_unresolved("(story 306, story 999)", self.TRUTH), [])

    def test_snapshot_shelf_tokens_are_accepted(self) -> None:
        # continuity/bible tokens are frozen snapshot references until the
        # web reader rebuild; the old numeric form must not fail.
        text = "심층시간(continuity 003), bible 201, continuity 001/002"
        self.assertEqual(guard.find_unresolved(text, self.TRUTH), [])

    def test_range_with_one_missing_member_is_flagged(self) -> None:
        truth = {**self.TRUTH, "world": {117, 118, 119, 121, 122}}  # 120 missing
        problems = guard.find_unresolved("world 117-122", truth)
        self.assertEqual([p.number for p in problems], [120])

    def test_slash_list_flags_only_the_missing(self) -> None:
        truth = {**self.TRUTH, "world": {108, 114}}  # 112, 113 missing
        problems = guard.find_unresolved("world 108/112/113/114", truth)
        self.assertEqual(sorted(p.number for p in problems), [112, 113])

    def test_lineno_is_reported_per_line(self) -> None:
        text = "clean line\nsecond\nworld 999 here"
        problems = guard.find_unresolved(text, self.TRUTH)
        self.assertEqual(problems[0].lineno, 3)


class BuildTruthMapTests(unittest.TestCase):
    """The truth map must be derived from the actual shelf directories."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.truth = guard.build_truth_map()

    def test_all_shelf_keys_present(self) -> None:
        for key in ("continuity", "world", "bible", "story", "workroom", "draft", "prototype"):
            self.assertIn(key, self.truth)

    def test_known_current_docs_are_present(self) -> None:
        self.assertIn(113, self.truth["world"])       # 113_restoration_mechanism_correction
        self.assertIn(126, self.truth["world"])       # 126_deeptime_catastrophe_pillar_spine

    def test_closed_shelves_are_history_only(self) -> None:
        # SAGA production shelves were removed from the active tree on
        # 2026-07-10; their tokens resolve against Git history only.
        for key in ("story", "workroom", "draft", "prototype"):
            self.assertIsNone(self.truth[key])

    def test_snapshot_shelves_are_unvalidated_until_rebuild(self) -> None:
        # continuity/series-bible dropped numeric prefixes on 2026-07-10; the
        # web data is a frozen snapshot until the hand-built reader rebuild.
        for key in ("continuity", "bible"):
            self.assertIsNone(self.truth[key])

    def test_renumbered_out_numbers_are_absent(self) -> None:
        # Old world 021 was renumbered to 113; a bare-old 21 must not resolve.
        self.assertNotIn(21, self.truth["world"])

    def test_retained_shelf_dirs_resolve_to_the_vault(self) -> None:
        # The migration is complete: each retained shelf must resolve to its
        # final fiction/worlds/qfuds-verse/* location, not a legacy fallback.
        expected = {
            "continuity": guard.WORLDS / "continuity",
            "world": guard.WORLDS / "world",
            "bible": guard.WORLDS / "series-bible",
        }
        for key, path in expected.items():
            with self.subTest(shelf=key):
                self.assertEqual(guard.resolve_shelf_dir(key), path)
                self.assertTrue(path.exists(), msg=f"missing shelf dir for {key}")


class ResolveDataFilesTests(unittest.TestCase):
    """The migration is complete: data files resolve to their final tool path."""

    def test_resolves_to_the_final_tool_location(self) -> None:
        resolved = guard.resolve_data_files()
        names = [str(p.relative_to(guard.ROOT)) for p in resolved]
        self.assertEqual(
            names,
            [
                "tools/qfuds-verse-web/data/chronicle-data.js",
                "tools/qfuds-verse-web/data/lore-data.js",
            ],
        )


class RealDataFilesTests(unittest.TestCase):
    """End-to-end lock: the shipped data files carry no unresolved reference."""

    def test_data_files_have_no_unresolved_refs(self) -> None:
        truth = guard.build_truth_map()
        for path in guard.resolve_data_files():
            with self.subTest(path=path.name):
                text = path.read_text(encoding="utf-8")
                problems = guard.find_unresolved(text, truth)
                self.assertEqual(
                    problems,
                    [],
                    msg="\n".join(
                        f"{path.name}:{p.lineno} unresolved `{p.shelf} {p.token}` "
                        f"(number {p.number} not on shelf {p.shelf})"
                        for p in problems
                    ),
                )


if __name__ == "__main__":
    unittest.main()
