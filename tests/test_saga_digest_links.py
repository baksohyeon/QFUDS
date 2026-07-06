"""Regression tests for build_saga_digest link handling.

The SAGA encyclopedia is generated at the SAGA root by concatenating a one
paragraph summary of every SAGA doc. Those summaries carry inline markdown
links written relative to each *source* doc, so they must be rewritten to be
SAGA-root-relative or they break in the digest. These tests lock in the
rewrite, the link-aware truncation, and the end-to-end "no broken internal
links" guarantee.

Run with: python3 -m unittest discover -s tests -p 'test_*.py'
"""

from __future__ import annotations

import importlib.util
import re
import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = REPO_ROOT / "scripts"

if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import build_saga_digest as digest  # noqa: E402

SAGA = digest.SAGA
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")


class RewriteLinkTargetTests(unittest.TestCase):
    def test_same_shelf_link_becomes_saga_root_relative(self) -> None:
        out = digest.rewrite_link_target(
            "319_new_book1_orpheus_design_ko.md", SAGA / "10_story_design"
        )
        self.assertEqual(out, "10_story_design/319_new_book1_orpheus_design_ko.md")

    def test_parent_relative_link_is_reanchored(self) -> None:
        out = digest.rewrite_link_target(
            "../../10_story_design/320_x_ko.md", SAGA / "20_drafts/1.5부"
        )
        self.assertEqual(out, "10_story_design/320_x_ko.md")

    def test_link_outside_saga_keeps_dotdot_prefix(self) -> None:
        out = digest.rewrite_link_target(
            "../../../10_world/115_x_ko.md", SAGA / "20_drafts/2부"
        )
        self.assertTrue(out.startswith("../"), out)
        self.assertIn("10_world/115_x_ko.md", out)

    def test_anchor_is_preserved(self) -> None:
        out = digest.rewrite_link_target("202_x_ko.md#section", SAGA / "00_bible")
        self.assertEqual(out, "00_bible/202_x_ko.md#section")

    def test_external_and_anchor_only_links_pass_through(self) -> None:
        for target in ("https://example.com/x", "mailto:a@b.c", "#local"):
            self.assertEqual(
                digest.rewrite_link_target(target, SAGA / "00_bible"), target
            )


class TruncateSummaryTests(unittest.TestCase):
    def test_short_summary_unchanged(self) -> None:
        text = "짧은 요약 [030 원고](20_drafts/1.5부/030_x_ko.md)."
        self.assertEqual(digest.truncate_summary(text, limit=280), text)

    def test_truncation_never_splits_a_link(self) -> None:
        link = "[030 원고](20_drafts/1.5부/030_origin_arc_sael_korean_primary_ko.md)"
        text = "가" * 270 + " " + link + " 뒤에 더 있는 문장"
        out = digest.truncate_summary(text, limit=280)
        self.assertTrue(out.endswith("…"))
        # The link must be dropped whole, never left as a dangling "[..](.." fragment.
        self.assertNotIn("](", out)
        self.assertNotIn("[030", out)


class GeneratedDigestTests(unittest.TestCase):
    def test_no_broken_internal_links_in_regenerated_digest(self) -> None:
        rendered = digest.render(digest.collect())
        broken: list[str] = []
        for _text, target in LINK_RE.findall(rendered):
            t = target.strip()
            if t.startswith(("http://", "https://", "mailto:", "#")):
                continue
            path_part = t.split("#", 1)[0]
            if not path_part:
                continue
            if not (SAGA / path_part).resolve().exists():
                broken.append(t)
        self.assertEqual(broken, [], f"broken internal links: {broken}")


if __name__ == "__main__":
    unittest.main()
