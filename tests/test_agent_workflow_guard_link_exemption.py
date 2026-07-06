"""Regression tests for the workflow guard's pure-link-path-edit exemption.

agent_workflow_guard exempts staged diffs that only rewrite link *targets*
(e.g. fixing ``../`` depth after a rename) from the research-workflow gate,
because such an edit adds no new external-research claim. The exemption hinges
on ``mask_link_targets`` neutralizing the ``](target)`` span so that a
target-only change compares equal while any prose/text change does not.

Run with: python3 -m unittest discover -s tests -p 'test_*.py'
"""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parents[1] / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import agent_workflow_guard as guard  # noqa: E402


class MaskLinkTargetsTests(unittest.TestCase):
    def test_target_only_change_compares_equal(self) -> None:
        before = "see [the audit](../../../governance/x.md) for detail"
        after = "see [the audit](../../investigations/x.md) for detail"
        self.assertNotEqual(before, after)
        self.assertEqual(guard.mask_link_targets(before), guard.mask_link_targets(after))

    def test_link_text_change_is_not_masked_equal(self) -> None:
        before = "see [old label](x.md)"
        after = "see [new label](x.md)"
        self.assertNotEqual(
            guard.mask_link_targets(before), guard.mask_link_targets(after)
        )

    def test_surrounding_prose_change_is_not_masked_equal(self) -> None:
        before = "an external arxiv asset [ref](a.md)"
        after = "a NEW external arxiv asset [ref](b.md)"
        self.assertNotEqual(
            guard.mask_link_targets(before), guard.mask_link_targets(after)
        )

    def test_multiple_links_on_one_line_all_masked(self) -> None:
        before = "[a](one/old.md) and [b](two/old.md)"
        after = "[a](one/new.md) and [b](two/new.md)"
        self.assertEqual(guard.mask_link_targets(before), guard.mask_link_targets(after))

    def test_target_flipping_to_external_url_is_not_masked_equal(self) -> None:
        # A link becoming an external URL adds an external-research claim, so it
        # must NOT read as a cosmetic path edit.
        before = "[ref](local/x.md)"
        after = "[ref](https://arxiv.org/abs/2503.14739)"
        self.assertNotEqual(
            guard.mask_link_targets(before), guard.mask_link_targets(after)
        )

    def test_line_without_links_is_unchanged(self) -> None:
        line = "plain prose with no markdown link"
        self.assertEqual(guard.mask_link_targets(line), line)


if __name__ == "__main__":
    unittest.main()
