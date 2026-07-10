"""Regression tests for the independent Markdown link-target checker.

Run with: python3 -m unittest tests.test_markdown_link_targets
"""

from __future__ import annotations

import contextlib
import io
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parents[1] / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import check_markdown_link_targets as checker  # noqa: E402


class MarkdownLinkTargetTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tempdir = tempfile.TemporaryDirectory()
        self.root = Path(self.tempdir.name)

    def tearDown(self) -> None:
        self.tempdir.cleanup()

    def write(self, rel: str, text: str = "") -> Path:
        path = self.root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return path

    def test_reports_missing_document_target_with_source_line(self) -> None:
        self.write(
            "docs/source.md",
            "\n".join(
                [
                    "# Source",
                    "",
                    "See [missing](missing-target.md).",
                    "",
                ]
            ),
        )

        missing = checker.check_roots([self.root / "docs"])

        self.assertEqual(len(missing), 1)
        self.assertEqual(missing[0].source, self.root / "docs/source.md")
        self.assertEqual(missing[0].line, 3)
        self.assertEqual(missing[0].target, "missing-target.md")

    def test_scans_recursively_and_skips_missing_optional_roots(self) -> None:
        self.write("vault/nested/source.md", "[missing](../missing.md)")

        missing = checker.check_roots([self.root / "does-not-exist", self.root / "vault"])

        self.assertEqual(len(missing), 1)
        self.assertEqual(missing[0].source, self.root / "vault/nested/source.md")

    def test_ignores_fenced_code_external_mail_and_anchor_only_links(self) -> None:
        self.write(
            "source.md",
            "\n".join(
                [
                    "# Source",
                    "",
                    "```",
                    "[ignored](missing-in-code.md)",
                    "![ignored](missing-in-code.png)",
                    "```",
                    "[external](https://example.com/x.md)",
                    "[mail](mailto:editor@example.com)",
                    "[anchor](#local-heading)",
                    "",
                ]
            ),
        )

        self.assertEqual(checker.check_roots([self.root]), [])

    def test_ignores_inline_code_link_examples(self) -> None:
        self.write(
            "source.md",
            "Document examples like `![alt](missing.png)` are not real links.\n",
        )

        self.assertEqual(checker.check_roots([self.root]), [])

    def test_resolves_url_encoded_and_angle_bracket_targets(self) -> None:
        self.write("notes/file with space.md")
        self.write("images/photo one.png")
        self.write(
            "source.md",
            "\n".join(
                [
                    "[encoded](notes/file%20with%20space.md)",
                    "![angle](<images/photo one.png>)",
                    "",
                ]
            ),
        )

        self.assertEqual(checker.check_roots([self.root]), [])

    def test_checks_missing_image_links(self) -> None:
        self.write("source.md", "![missing](images/missing.png)\n")

        missing = checker.check_roots([self.root])

        self.assertEqual(len(missing), 1)
        self.assertEqual(missing[0].target, "images/missing.png")

    def test_resolves_repository_root_relative_target(self) -> None:
        self.write("target.md")
        source = self.write("docs/source.md", "[target](/target.md)\n")

        self.assertEqual(
            checker.check_roots([source], repo_root=self.root),
            [],
        )

    def test_skips_nested_git_repository_when_scanning_parent_root(self) -> None:
        self.write("tools/story-skills/.git", "gitdir: elsewhere\n")
        self.write(
            "tools/story-skills/README.md",
            "[nested repository link](missing.md)\n",
        )

        self.assertEqual(checker.check_roots([self.root / "tools"]), [])

    def test_cli_reports_file_line_and_target(self) -> None:
        self.write("docs/source.md", "See [missing](missing.md).\n")
        stdout = io.StringIO()

        with contextlib.redirect_stdout(stdout):
            exit_code = checker.main([str(self.root / "docs")])

        self.assertEqual(exit_code, 1)
        out = stdout.getvalue()
        self.assertIn("docs/source.md:1", out)
        self.assertIn("missing.md", out)


if __name__ == "__main__":
    unittest.main()
