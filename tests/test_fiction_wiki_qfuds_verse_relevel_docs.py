"""Regression tests for the 2026-07-01 QFUDS Verse canon relevel PR.

The PR moved a large batch of `qfuds-saga` series bible documents that are
actually *shared universe* canon (world rules, physics, factions, history)
out of `20_series/qfuds-saga/00_bible/` into two new universe-level shelves:

  - `10_universes/qfuds-verse/00_continuity/`  (canon authority map, deep-time
    timeline, chronology/restoration admin)
  - `10_universes/qfuds-verse/10_world/`       (shared world bible + three new
    "world expansion wave" candidate registers)

It also updated a batch of relative Markdown links in `00_studio/` and in the
moved/created documents themselves to point at the new locations.

This is a documentation-only change, so these tests exercise the *content*
of the changed/added Markdown files using the repository's own validation
tooling (`scripts/validate_docs.py`, `scripts/fiction_gate.py`) plus a small
link-resolution helper, instead of testing application code.
"""

from __future__ import annotations

import importlib.util
import os
import re
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Optional

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = ROOT / "scripts"


def _load_module(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS_DIR / filename)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


validate_docs = _load_module("qfuds_validate_docs_under_test", "validate_docs.py")
fiction_gate = _load_module("qfuds_fiction_gate_under_test", "fiction_gate.py")

FICTION_ROOT = ROOT / "docs" / "wiki" / "fiction"
QFUDS_VERSE = FICTION_ROOT / "10_universes" / "qfuds-verse"
CONTINUITY_DIR = QFUDS_VERSE / "00_continuity"
WORLD_DIR = QFUDS_VERSE / "10_world"
STUDIO_DIR = FICTION_ROOT / "00_studio"
OLD_BIBLE_DIR = QFUDS_VERSE / "20_series" / "qfuds-saga" / "00_bible"

# (path, expected doc_id, expected title) for every file touched by the PR.
CHANGED_DOCS: list[tuple[Path, str, str]] = [
    (
        STUDIO_DIR / "006_prose_verisimilitude_audit_checklist_ko.md",
        "fiction_prose_verisimilitude_audit_checklist_ko",
        "Fiction Prose 핍진성·개연성 장면 감사 체크리스트",
    ),
    (
        STUDIO_DIR / "007_craft_and_political_theory_research_ko.md",
        "fiction_craft_and_political_theory_research_ko",
        "Fiction 창작 기법·정치이론 자료조사 (비약 없는 노출 + 세계규칙 실증 앵커)",
    ),
    (
        CONTINUITY_DIR / "000_canon_authority_and_ssot_map_ko.md",
        "qfuds_saga_canon_authority_and_ssot_map_ko",
        "QFUDS SAGA 캐논 권위·SSOT 지도",
    ),
    (
        CONTINUITY_DIR / "001_deep_time_restoration_timeline_ko.md",
        "qfuds_saga_deep_time_restoration_timeline_ko",
        "QFUDS SAGA 장기 복원 문명사 타임라인",
    ),
    (
        CONTINUITY_DIR / "002_chronology_restoration_admin_black_hole_seat_ko.md",
        "qfuds_saga_chronology_restoration_admin_black_hole_seat_ko",
        "QFUDS SAGA 연표·기술곡선·복원 행정·블랙홀 본거지",
    ),
    (
        CONTINUITY_DIR / "README.md",
        "qfuds_verse_continuity_index_ko",
        "QFUDS Verse Continuity",
    ),
    (
        WORLD_DIR / "101_world_anchor_and_verisimilitude_ko.md",
        "qfuds_saga_world_anchor_and_verisimilitude_ko",
        "QFUDS SAGA 세계 기준점과 핍진성 규칙",
    ),
    (
        WORLD_DIR / "102_factions_cultures_power_ecology_ko.md",
        "qfuds_saga_factions_cultures_power_ecology_ko",
        "QFUDS SAGA 세력 문화 권력 생태계 장부",
    ),
    (
        WORLD_DIR / "103_bitcoin_genesis_chain_and_restoration_myth_ko.md",
        "qfuds_saga_bitcoin_genesis_chain_and_restoration_myth_ko",
        "QFUDS SAGA Bitcoin Genesis Chain과 복원 신화",
    ),
    (
        WORLD_DIR / "104_post_agi_civilization_history_bilingual_protocol_ko.md",
        "qfuds_saga_post_agi_civilization_history_bilingual_protocol_ko",
        "QFUDS SAGA Post-AGI 문명사와 한국어 우선 이중언어 프로토콜",
    ),
    (
        WORLD_DIR / "105_cryptographic_death_and_hash_covenant_ko.md",
        "qfuds_saga_cryptographic_death_and_hash_covenant_ko",
        "QFUDS SAGA 암호학적 죽음과 해시 계약",
    ),
    (
        WORLD_DIR / "106_reader_accessibility_and_real_world_anchors_ko.md",
        "qfuds_saga_reader_accessibility_and_real_world_anchors_ko",
        "QFUDS SAGA 비트코인 메인 메타포 토대와 독자 접근성",
    ),
    (
        WORLD_DIR / "107_last_archive_origin_and_reversal_causality_ko.md",
        "qfuds_saga_last_archive_origin_and_reversal_causality_ko",
        "QFUDS SAGA Last Archive 기원·역연산 인과·문명 규모·죽음의 평등",
    ),
    (
        WORLD_DIR / "108_cryptographic_death_era_and_crypto_concepts_ko.md",
        "qfuds_saga_cryptographic_death_era_and_crypto_concepts_ko",
        "QFUDS SAGA Cryptographic Death 대격변과 암호 개념 상세 설정",
    ),
    (
        WORLD_DIR / "109_factions_canon_naming_ko.md",
        "qfuds_saga_factions_canon_naming_ko",
        "QFUDS SAGA 세력 명칭 Canon 확정",
    ),
    (
        WORLD_DIR / "110_bitcoin_stature_ideology_deeptime_ko.md",
        "qfuds_saga_bitcoin_stature_ideology_deeptime_ko",
        "QFUDS SAGA 비트코인 위상·이념전쟁·심층시간 유효성",
    ),
    (
        WORLD_DIR / "111_world_compendium_codex_ko.md",
        "qfuds_saga_world_compendium_codex_ko",
        "QFUDS SAGA 세계관 컴펜디움",
    ),
    (
        WORLD_DIR / "112_ai_automation_human_in_the_loop_ssot_ko.md",
        "qfuds_saga_ai_automation_human_in_the_loop_ssot_ko",
        "QFUDS SAGA AI·자동화·인간 확인 루프·아날로그 법정",
    ),
    (
        WORLD_DIR / "113_restoration_mechanism_correction_ko.md",
        "qfuds_saga_restoration_mechanism_correction_ko",
        "QFUDS SAGA 복원 메커니즘 정정 (정보 역산 + 인공 신체)",
    ),
    (
        WORLD_DIR / "114_in_world_physics_information_unitarity_restoration_ko.md",
        "qfuds_saga_in_world_physics_information_unitarity_restoration_ko",
        "QFUDS SAGA in-world 물리 캐논 — 정보·유니터리·복원",
    ),
    (
        WORLD_DIR / "115_qday_aftermath_timeline_and_world_ko.md",
        "qfuds_saga_qday_aftermath_timeline_and_world_ko",
        "QFUDS SAGA Q-Day 여파 타임라인과 세계 설정",
    ),
    (
        WORLD_DIR / "116_qday_world_system_14domain_matrix_ko.md",
        "qfuds_saga_qday_world_system_14domain_matrix_ko",
        "QFUDS SAGA Q-Day 여파 14도메인 세계-체계 매트릭스 (115 부속)",
    ),
    (
        WORLD_DIR / "117_world_expansion_wave1_names_places_events_ko.md",
        "qfuds_verse_world_expansion_wave1_names_places_events_ko",
        "QFUDS Verse 세계 확장 웨이브 1 (고유명사·지명·세력·인물·사건·어휘)",
    ),
    (
        WORLD_DIR / "118_world_expansion_wave2_factions_relationships_ko.md",
        "qfuds_verse_world_expansion_wave2_factions_relationships_ko",
        "QFUDS Verse 세계 확장 웨이브 2 (세력 내부 심화·인물·관계망)",
    ),
    (
        WORLD_DIR / "119_world_expansion_wave3_geography_event_chains_ko.md",
        "qfuds_verse_world_expansion_wave3_geography_event_chains_ko",
        "QFUDS Verse 세계 확장 웨이브 3 (지리 상세·궤도 역학·사건 연쇄 인과)",
    ),
    (
        WORLD_DIR / "README.md",
        "qfuds_verse_world_index_ko",
        "QFUDS Verse World",
    ),
]

# Filenames that used to live under 20_series/qfuds-saga/00_bible/ and were
# renamed (git mv) into 00_continuity/ or 10_world/ by this PR. If any of
# these still exist at the old path, the move regressed into a copy and
# doc_id uniqueness would be violated.
RENAMED_AWAY_BIBLE_FILENAMES = [
    "000_canon_authority_and_ssot_map_ko.md",
    "101_world_anchor_and_verisimilitude_ko.md",
    "001_deep_time_restoration_timeline_ko.md",
    "102_factions_cultures_power_ecology_ko.md",
    "103_bitcoin_genesis_chain_and_restoration_myth_ko.md",
    "104_post_agi_civilization_history_bilingual_protocol_ko.md",
    "105_cryptographic_death_and_hash_covenant_ko.md",
    "106_reader_accessibility_and_real_world_anchors_ko.md",
    "107_last_archive_origin_and_reversal_causality_ko.md",
    "002_chronology_restoration_admin_black_hole_seat_ko.md",
    "108_cryptographic_death_era_and_crypto_concepts_ko.md",
    "109_factions_canon_naming_ko.md",
    "110_bitcoin_stature_ideology_deeptime_ko.md",
    "111_world_compendium_codex_ko.md",
    "112_ai_automation_human_in_the_loop_ssot_ko.md",
    "113_restoration_mechanism_correction_ko.md",
    "114_in_world_physics_information_unitarity_restoration_ko.md",
    "115_qday_aftermath_timeline_and_world_ko.md",
    "116_qday_world_system_14domain_matrix_ko.md",
]

LINK_TARGET_RE = re.compile(r"\[[^\]]*\]\((?P<target>[^)\s]+)\)")


def iter_markdown_link_targets(body: str) -> list[str]:
    """Extract `[text](target)` link targets from Markdown body text.

    Skips fenced code blocks (field-mark samples live there) the same way
    `scripts/validate_docs.py` does.
    """
    targets: list[str] = []
    in_fence = False
    for line in body.splitlines():
        if line.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        for match in LINK_TARGET_RE.finditer(line):
            targets.append(match.group("target"))
    return targets


def resolve_relative_target(file_path: Path, target: str) -> Optional[Path]:
    """Resolve a Markdown link target relative to the file containing it.

    Returns None for external (http/https/mailto) links and for pure
    same-document anchors (`#section`), since neither refers to a file on
    disk.
    """
    target = target.strip()
    if target.startswith(("http://", "https://", "mailto:")):
        return None
    path_part = target.split("#", 1)[0]
    if not path_part:
        return None
    if path_part.startswith("/"):
        return None
    return (file_path.parent / path_part).resolve()


class ChangedDocFrontmatterTests(unittest.TestCase):
    """Frontmatter schema + doc_id/title checks for every file this PR touched."""

    def test_all_changed_docs_exist(self) -> None:
        for path, _doc_id, _title in CHANGED_DOCS:
            self.assertTrue(path.exists(), f"expected changed doc missing: {path}")

    def test_frontmatter_required_fields_present(self) -> None:
        for path, _doc_id, _title in CHANGED_DOCS:
            with self.subTest(path=path.relative_to(ROOT)):
                frontmatter, _body = validate_docs.parse_frontmatter(path)
                for field in validate_docs.REQUIRED_FIELDS:
                    self.assertIn(field, frontmatter, f"missing `{field}` in {path}")

    def test_doc_id_and_title_match_expected(self) -> None:
        for path, expected_doc_id, expected_title in CHANGED_DOCS:
            with self.subTest(path=path.relative_to(ROOT)):
                frontmatter, body = validate_docs.parse_frontmatter(path)
                self.assertEqual(frontmatter["doc_id"], expected_doc_id)
                self.assertEqual(frontmatter["title"], expected_title)
                self.assertEqual(
                    validate_docs.first_h1(body),
                    expected_title,
                    f"H1 does not match frontmatter title in {path}",
                )

    def test_last_updated_reflects_latest_shelf_renumber(self) -> None:
        # Releveled on 2026-07-01, then band-renumbered on 2026-07-06
        # (continuity 0xx / world 1xx), which bumped last_updated.
        for path, _doc_id, _title in CHANGED_DOCS:
            with self.subTest(path=path.relative_to(ROOT)):
                frontmatter, _body = validate_docs.parse_frontmatter(path)
                self.assertEqual(frontmatter.get("last_updated"), "2026-07-06")

    def test_allowed_enum_values(self) -> None:
        for path, _doc_id, _title in CHANGED_DOCS:
            frontmatter, _body = validate_docs.parse_frontmatter(path)
            for field, allowed in validate_docs.ALLOWED_VALUES.items():
                value = frontmatter.get(field)
                if value:
                    with self.subTest(path=path.relative_to(ROOT), field=field):
                        self.assertIn(value, allowed)


class ValidateDocsScriptTests(unittest.TestCase):
    """Runs the repository's own `validate_docs.validate_doc()` gate against
    every file touched by the PR, and checks doc_id uniqueness afterward."""

    def test_validate_doc_reports_no_errors(self) -> None:
        for path, _doc_id, _title in CHANGED_DOCS:
            with self.subTest(path=path.relative_to(ROOT)):
                errors = validate_docs.validate_doc(path)
                self.assertEqual(errors, [], f"validate_doc errors for {path}: {errors}")

    def test_doc_ids_are_globally_unique_across_fiction_wiki(self) -> None:
        doc_ids: dict[str, Path] = {}
        duplicates: list[tuple[str, Path, Path]] = []
        for path in sorted(FICTION_ROOT.rglob("*.md")):
            try:
                frontmatter, _body = validate_docs.parse_frontmatter(path)
            except ValueError:
                continue
            doc_id = frontmatter.get("doc_id")
            if not doc_id:
                continue
            if doc_id in doc_ids:
                duplicates.append((doc_id, doc_ids[doc_id], path))
            else:
                doc_ids[doc_id] = path
        self.assertEqual(duplicates, [], f"duplicate doc_ids found: {duplicates}")
        for _path, expected_doc_id, _title in CHANGED_DOCS:
            self.assertIn(expected_doc_id, doc_ids)


class RenamedBibleFilesRemovedTests(unittest.TestCase):
    """The relevel moved shared-world bibles out of 00_bible/; the old paths
    must not still exist, or the move regressed into a stale duplicate."""

    def test_old_bible_paths_do_not_exist(self) -> None:
        for filename in RENAMED_AWAY_BIBLE_FILENAMES:
            old_path = OLD_BIBLE_DIR / filename
            self.assertFalse(
                old_path.exists(),
                f"stale pre-relevel bible file still present: {old_path}",
            )

    def test_new_locations_exist_for_every_renamed_filename(self) -> None:
        for filename in RENAMED_AWAY_BIBLE_FILENAMES:
            new_in_continuity = (CONTINUITY_DIR / filename).exists()
            new_in_world = (WORLD_DIR / filename).exists()
            self.assertTrue(
                new_in_continuity or new_in_world,
                f"{filename} not found under 00_continuity/ or 10_world/",
            )


class LinkResolutionHelperTests(unittest.TestCase):
    """Boundary/negative-case checks on the link-resolution helper itself, so
    a passing `test_all_relative_links_resolve` below is not a false
    negative caused by a bug in the helper."""

    def test_ignores_external_links(self) -> None:
        body = "See [docs](https://example.com/readme.md) for more."
        targets = iter_markdown_link_targets(body)
        self.assertEqual(targets, ["https://example.com/readme.md"])
        self.assertIsNone(resolve_relative_target(ROOT / "x.md", targets[0]))

    def test_ignores_pure_anchor_links(self) -> None:
        self.assertIsNone(resolve_relative_target(ROOT / "x.md", "#section"))

    def test_strips_anchor_fragment_before_resolving(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            target_file = tmp_path / "target.md"
            target_file.write_text("# Target\n", encoding="utf-8")
            source_file = tmp_path / "source.md"
            resolved = resolve_relative_target(source_file, "target.md#some-heading")
            self.assertEqual(resolved, target_file.resolve())
            self.assertTrue(resolved.exists())

    def test_detects_broken_relative_link(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            source_file = Path(tmp) / "source.md"
            resolved = resolve_relative_target(source_file, "does_not_exist_ko.md")
            self.assertIsNotNone(resolved)
            self.assertFalse(resolved.exists())


class LinkResolutionTests(unittest.TestCase):
    """The relevel rewrote dozens of relative links; every relative Markdown
    link inside a changed file must resolve to a real file on disk."""

    def test_all_relative_links_resolve(self) -> None:
        broken: list[tuple[Path, str, Path]] = []
        for path, _doc_id, _title in CHANGED_DOCS:
            _frontmatter, body = validate_docs.parse_frontmatter(path)
            for target in iter_markdown_link_targets(body):
                resolved = resolve_relative_target(path, target)
                if resolved is None:
                    continue
                if not resolved.exists():
                    broken.append((path.relative_to(ROOT), target, resolved))
        self.assertEqual(broken, [], f"broken relative links: {broken}")

    def test_canon_authority_map_links_into_10_world(self) -> None:
        path = CONTINUITY_DIR / "000_canon_authority_and_ssot_map_ko.md"
        _frontmatter, body = validate_docs.parse_frontmatter(path)
        targets = iter_markdown_link_targets(body)
        for expected in (
            "../10_world/113_restoration_mechanism_correction_ko.md",
            "../10_world/109_factions_canon_naming_ko.md",
            "../10_world/107_last_archive_origin_and_reversal_causality_ko.md",
        ):
            with self.subTest(expected=expected):
                self.assertIn(expected, targets)
                resolved = resolve_relative_target(path, expected)
                self.assertTrue(resolved.exists())

    def test_continuity_readme_links_to_new_ssot_docs(self) -> None:
        path = CONTINUITY_DIR / "README.md"
        _frontmatter, body = validate_docs.parse_frontmatter(path)
        targets = set(iter_markdown_link_targets(body))
        self.assertIn("000_canon_authority_and_ssot_map_ko.md", targets)
        self.assertIn("001_deep_time_restoration_timeline_ko.md", targets)
        self.assertIn("002_chronology_restoration_admin_black_hole_seat_ko.md", targets)

    def test_world_readme_links_to_expansion_waves_and_continuity(self) -> None:
        path = WORLD_DIR / "README.md"
        _frontmatter, body = validate_docs.parse_frontmatter(path)
        targets = set(iter_markdown_link_targets(body))
        self.assertIn("117_world_expansion_wave1_names_places_events_ko.md", targets)
        self.assertIn("118_world_expansion_wave2_factions_relationships_ko.md", targets)
        self.assertIn("119_world_expansion_wave3_geography_event_chains_ko.md", targets)
        self.assertIn("../00_continuity/", targets)

    def test_studio_docs_point_at_relocated_world_bible(self) -> None:
        checklist = STUDIO_DIR / "006_prose_verisimilitude_audit_checklist_ko.md"
        _frontmatter, body = validate_docs.parse_frontmatter(checklist)
        targets = " ".join(iter_markdown_link_targets(body))
        self.assertIn(
            "10_universes/qfuds-verse/10_world/101_world_anchor_and_verisimilitude_ko.md",
            targets,
        )

        research = STUDIO_DIR / "007_craft_and_political_theory_research_ko.md"
        _frontmatter, body = validate_docs.parse_frontmatter(research)
        targets = " ".join(iter_markdown_link_targets(body))
        self.assertIn(
            "10_universes/qfuds-verse/10_world/106_reader_accessibility_and_real_world_anchors_ko.md",
            targets,
        )


class FictionGateComplianceTests(unittest.TestCase):
    """These are reference/index/provenance docs, not story prose, but they
    still must clear the commit-time `fiction_gate` sensitive-term scrub."""

    def setUp(self) -> None:
        self._old_cwd = os.getcwd()
        os.chdir(ROOT)

    def tearDown(self) -> None:
        os.chdir(self._old_cwd)

    def test_fiction_gate_check_reports_no_errors(self) -> None:
        files = [str(path.relative_to(ROOT)) for path, _doc_id, _title in CHANGED_DOCS]
        errs, _warns = fiction_gate.check(files)
        self.assertEqual(errs, [], f"fiction_gate errors: {errs}")

    def test_fiction_gate_check_flags_injected_sensitive_term(self) -> None:
        """Negative control: fiction_gate.check() must still be capable of
        catching a violation, so a clean result above is not vacuous."""
        with tempfile.TemporaryDirectory() as tmp:
            bad_file = Path(tmp) / "bad_ko.md"
            bad_file.write_text(
                "---\ndoc_id: x\ntitle: x\n---\n\n# x\n\n이것은 페미니즘 용어 테스트다.\n",
                encoding="utf-8",
            )
            errs, _warns = fiction_gate.check([str(bad_file)])
            self.assertTrue(errs, "expected fiction_gate to flag sensitive term")


if __name__ == "__main__":
    unittest.main()