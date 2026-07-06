"""Regression tests for the QFUDS SAGA Q-Day 14-domain matrix promotion PR.

This PR is documentation-only (Korean-language fiction wiki pages). The docs
were later relocated by the 2026-07-06 band renumber (the Q-Day canon moved to
qfuds-verse/00_continuity and 10_world; workroom docs renumbered), so the path
constants below track those current locations while the doc_ids stay. The
repository's
authoritative way of "testing" documentation is the frontmatter/link/gate
scripts under scripts/ (validate_docs.py, fiction_gate.py). These tests exercise
those scripts against exactly the files changed in this PR, plus assert on the
specific content commitments the diff makes (new doc registered in the
authority map/READMEs, production board marked done/promoted, depends_on
references resolvable, no duplicate doc_id, no banned terminology).

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

import validate_docs as vd  # noqa: E402
import fiction_gate as fg  # noqa: E402


VERSE = "docs/wiki/fiction/10_universes/qfuds-verse"
SAGA_ROOT = f"{VERSE}/20_series/qfuds-saga"
BIBLE = f"{SAGA_ROOT}/00_bible"
WORKROOM = f"{SAGA_ROOT}/00_workroom"
# The 2026-07-06 band renumber relocated the Q-Day canon docs off the saga
# bible shelf: 026 -> 10_world/115, 028 -> 10_world/116, the canon authority
# map -> 00_continuity/000, and workroom 009 -> 408, 011 -> 410. The doc_ids
# below are stable; only shelves and numeric prefixes changed.
CONTINUITY = f"{VERSE}/00_continuity"
WORLD = f"{VERSE}/10_world"

CHANGED_FILES = [
    f"{CONTINUITY}/000_canon_authority_and_ssot_map_ko.md",
    f"{WORLD}/115_qday_aftermath_timeline_and_world_ko.md",
    f"{WORLD}/116_qday_world_system_14domain_matrix_ko.md",
    f"{BIBLE}/README.md",
    f"{WORKROOM}/408_saga_production_board_ko.md",
    f"{WORKROOM}/410_expert_panel_world_system_handoff_ko.md",
    f"{WORKROOM}/README.md",
]

NEW_DOC_028 = f"{WORLD}/116_qday_world_system_14domain_matrix_ko.md"
NEW_DOC_011 = f"{WORKROOM}/410_expert_panel_world_system_handoff_ko.md"

DOC_028_ID = "qfuds_saga_qday_world_system_14domain_matrix_ko"
DOC_011_ID = "qfuds_saga_expert_panel_world_system_handoff_ko"

MD_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)\s]+\.md)(#[^)]*)?\)")


def _abspath(rel: str) -> Path:
    return REPO_ROOT / rel


def _read(rel: str) -> str:
    return _abspath(rel).read_text(encoding="utf-8")


class ChangedFilesExistTests(unittest.TestCase):
    """Sanity: every file this PR touches is present on disk."""

    def test_all_changed_files_exist(self) -> None:
        for rel in CHANGED_FILES:
            with self.subTest(path=rel):
                self.assertTrue(_abspath(rel).is_file(), f"missing file: {rel}")


class ValidateDocsComplianceTests(unittest.TestCase):
    """Exercise the repo's authoritative frontmatter/link validator."""

    def test_each_changed_file_passes_validate_doc(self) -> None:
        for rel in CHANGED_FILES:
            with self.subTest(path=rel):
                errors = vd.validate_doc(_abspath(rel))
                self.assertEqual(errors, [], f"{rel} failed validate_doc: {errors}")

    def test_new_world_spec_doc_has_expected_frontmatter(self) -> None:
        frontmatter, _ = vd.parse_frontmatter(_abspath(NEW_DOC_028))
        self.assertEqual(frontmatter["doc_id"], DOC_028_ID)
        self.assertEqual(frontmatter["doc_type"], "guide")
        self.assertEqual(frontmatter["stage"], "reference")
        self.assertEqual(frontmatter["status"], "draft")
        self.assertEqual(frontmatter["evidence_role"], "provenance")
        self.assertEqual(frontmatter["last_updated"], "2026-07-06")
        # 116 must defer authority to 115 (the SSOT) in its own next_gate note.
        self.assertIn("115", frontmatter["next_gate"])

    def test_new_workroom_brief_has_expected_frontmatter(self) -> None:
        frontmatter, _ = vd.parse_frontmatter(_abspath(NEW_DOC_011))
        self.assertEqual(frontmatter["doc_id"], DOC_011_ID)
        self.assertEqual(frontmatter["doc_type"], "guide")
        self.assertEqual(frontmatter["stage"], "reference")
        self.assertEqual(frontmatter["status"], "draft")
        self.assertEqual(frontmatter["evidence_role"], "provenance")
        self.assertEqual(frontmatter["last_updated"], "2026-07-06")
        # 410 is now provenance-only; its next_gate must record the promotion to 116.
        self.assertIn("116", frontmatter["next_gate"])

    def test_h1_matches_title_for_new_files(self) -> None:
        for rel in (NEW_DOC_028, NEW_DOC_011):
            with self.subTest(path=rel):
                frontmatter, body = vd.parse_frontmatter(_abspath(rel))
                self.assertEqual(vd.first_h1(body), frontmatter["title"])

    def test_last_updated_is_well_formed_date_for_all_changed_files(self) -> None:
        date_re = re.compile(r"^\d{4}-\d{2}-\d{2}$")
        for rel in CHANGED_FILES:
            with self.subTest(path=rel):
                frontmatter, _ = vd.parse_frontmatter(_abspath(rel))
                self.assertRegex(frontmatter["last_updated"], date_re)


class DocIdIntegrityTests(unittest.TestCase):
    """doc_id uniqueness and depends_on resolvability across the whole repo tree."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.doc_ids: dict[str, Path] = {}
        for path in sorted(vd.DOCS.rglob("*.md")):
            try:
                frontmatter, _ = vd.parse_frontmatter(path)
            except ValueError:
                continue
            doc_id = frontmatter.get("doc_id")
            if doc_id:
                cls.doc_ids.setdefault(doc_id, path)

    def test_new_doc_ids_are_globally_unique(self) -> None:
        for rel, expected_id in ((NEW_DOC_028, DOC_028_ID), (NEW_DOC_011, DOC_011_ID)):
            with self.subTest(path=rel):
                frontmatter, _ = vd.parse_frontmatter(_abspath(rel))
                self.assertEqual(frontmatter["doc_id"], expected_id)
                # Exactly one file in the whole docs tree should own this id.
                # Skip files without frontmatter (e.g. auto-converted asset
                # Markdown) the same way setUpClass does.
                owners = []
                for p in vd.DOCS.rglob("*.md"):
                    try:
                        fm, _ = vd.parse_frontmatter(p)
                    except ValueError:
                        continue
                    if fm.get("doc_id") == expected_id:
                        owners.append(p)
                self.assertEqual(len(owners), 1, f"duplicate doc_id {expected_id}: {owners}")

    def test_028_depends_on_all_resolve_to_existing_doc_ids(self) -> None:
        frontmatter, body = vd.parse_frontmatter(_abspath(NEW_DOC_028))
        raw_text = _read(NEW_DOC_028)
        depends_on = self._extract_depends_on(raw_text)
        self.assertGreater(len(depends_on), 0)
        for dep_id in depends_on:
            with self.subTest(dep_id=dep_id):
                self.assertIn(dep_id, self.doc_ids, f"unresolved depends_on: {dep_id}")

    def test_011_depends_on_all_resolve_to_existing_doc_ids(self) -> None:
        raw_text = _read(NEW_DOC_011)
        depends_on = self._extract_depends_on(raw_text)
        self.assertGreater(len(depends_on), 0)
        for dep_id in depends_on:
            with self.subTest(dep_id=dep_id):
                self.assertIn(dep_id, self.doc_ids, f"unresolved depends_on: {dep_id}")

    @staticmethod
    def _extract_depends_on(raw_text: str) -> list[str]:
        frontmatter_block = raw_text.split("\n---\n", 1)[0]
        lines = frontmatter_block.splitlines()
        deps: list[str] = []
        in_block = False
        for line in lines:
            if line.strip() == "depends_on:":
                in_block = True
                continue
            if in_block:
                if line.startswith("  - "):
                    deps.append(line.strip()[2:].strip())
                elif line.strip() and not line.startswith(" "):
                    break
        return deps

    def test_duplicate_doc_id_would_be_flagged(self) -> None:
        """Regression/negative case: simulate the uniqueness check main() performs.

        This guards the invariant that introducing a second file re-using the
        028 doc_id is a detectable error, mirroring validate_docs.main()'s
        duplicate-detection loop without mutating the real docs tree.
        """
        seen: dict[str, Path] = {}
        conflicts: list[str] = []
        candidate_paths = [_abspath(NEW_DOC_028), _abspath(NEW_DOC_028)]
        for path in candidate_paths:
            frontmatter, _ = vd.parse_frontmatter(path)
            doc_id = frontmatter.get("doc_id")
            if doc_id in seen:
                conflicts.append(doc_id)
            else:
                seen[doc_id] = path
        self.assertEqual(conflicts, [DOC_028_ID])


class InternalLinkIntegrityTests(unittest.TestCase):
    """All markdown cross-references introduced/edited in this PR must resolve."""

    def test_markdown_links_in_changed_files_point_to_existing_files(self) -> None:
        for rel in CHANGED_FILES:
            path = _abspath(rel)
            text = path.read_text(encoding="utf-8")
            for match in MD_LINK_RE.finditer(text):
                reference = match.group(1)
                target = vd.resolve_md_reference(path, reference)
                with self.subTest(path=rel, reference=reference):
                    self.assertTrue(target.exists(), f"{rel}: broken link -> {reference}")

    def test_bare_markdown_paths_are_not_left_unlinked(self) -> None:
        for rel in CHANGED_FILES:
            path = _abspath(rel)
            _, body = vd.parse_frontmatter(path)
            errors = vd.validate_markdown_doc_links(path, body)
            with self.subTest(path=rel):
                self.assertEqual(errors, [])


class FictionGateComplianceTests(unittest.TestCase):
    """The changed bible/workroom pages must pass the hard fiction gate checks."""

    def test_no_sensitive_terminology_or_hard_violations(self) -> None:
        errs, _warns = fg.check(CHANGED_FILES)
        self.assertEqual(errs, [])

    def test_no_em_dash_in_newly_added_files(self) -> None:
        # 028 and 011 are wholly new files added by this PR; the other five
        # changed files are pre-existing indexes that already carried
        # unrelated em dashes in untouched lines, so only the new files are
        # asserted to be completely free of the banned AI-tell character.
        for rel in (NEW_DOC_028, NEW_DOC_011):
            with self.subTest(path=rel):
                text = _read(rel)
                self.assertNotIn(fg.EMDASH, text)


class ContentCommitmentTests(unittest.TestCase):
    """Assert the specific cross-file wiring this PR promises actually landed."""

    def test_authority_map_registers_qday_world_system_row(self) -> None:
        text = _read(f"{CONTINUITY}/000_canon_authority_and_ssot_map_ko.md")
        self.assertIn("Q-Day 여파 세계-체계", text)
        self.assertIn(
            "[115](../10_world/115_qday_aftermath_timeline_and_world_ko.md)", text
        )
        self.assertIn(
            "[116](../10_world/116_qday_world_system_14domain_matrix_ko.md)", text
        )
        self.assertIn("115이 SSOT", text)

    def test_115_references_116_as_attachment_and_not_ssot_replacement(self) -> None:
        text = _read(f"{WORLD}/115_qday_aftermath_timeline_and_world_ko.md")
        self.assertIn("부속 매트릭스", text)
        self.assertIn(
            "[116 Q-Day 여파 14도메인 매트릭스](116_qday_world_system_14domain_matrix_ko.md)",
            text,
        )
        self.assertIn("115이 SSOT", text)

    def test_bible_readme_points_at_relocated_world_matrix(self) -> None:
        # After the renumber the 14-domain matrix lives on the shared-world
        # shelf; the saga bible README references it via the 10_world link.
        text = _read(f"{BIBLE}/README.md")
        self.assertIn("116 매트릭스", text)
        self.assertIn("../../../10_world/", text)

    def test_workroom_readme_lists_410_and_marks_promotion(self) -> None:
        text = _read(f"{WORKROOM}/README.md")
        self.assertIn("410_expert_panel_world_system_handoff_ko.md", text)
        self.assertIn("world 116", text)

    def test_production_board_marks_14domain_row_promoted(self) -> None:
        text = _read(f"{WORKROOM}/408_saga_production_board_ko.md")
        self.assertIn("14도메인 세계-체계 확장(410→116)", text)
        self.assertIn("`promoted`", text)
        self.assertIn(
            "[world 116](../../../10_world/116_qday_world_system_14domain_matrix_ko.md)",
            text,
        )

    def test_116_declares_canon_attachment_status_not_candidate(self) -> None:
        text = _read(NEW_DOC_028)
        self.assertIn("캐논 상태: canon 부속 (00_bible)", text)
        self.assertNotIn("candidate", text.lower())

    def test_410_declares_promotion_complete_and_provenance_status(self) -> None:
        text = _read(NEW_DOC_011)
        self.assertIn("승격 완료(2026-07-01, 경로 A)", text)
        self.assertIn("**작업 provenance**로 보존한다", text)

    def test_no_new_proper_nouns_hard_constraint_statement_present(self) -> None:
        """116 must explicitly restate the 'no new proper nouns/events/characters' guard."""
        text = _read(NEW_DOC_028)
        self.assertIn("새 고유명사·새 사건·새 인물을 만들지 않는다", text)


if __name__ == "__main__":
    unittest.main()