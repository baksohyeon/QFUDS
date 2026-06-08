#!/usr/bin/env python3
"""Validate QFUDS documentation metadata and roadmap links.

This script is the executable, authoritative form of the frontmatter schema
convention documented in `docs/00_project/frontmatter_convention.md`. If that
document and this script disagree, this script wins and the document must be
corrected. Keep the enumerations below in sync with that convention.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

REQUIRED_FIELDS = [
    "doc_id",
    "title",
    "doc_type",
    "stage",
    "status",
    "evidence_role",
    "depends_on",
    "next_gate",
    "last_updated",
]

ALLOWED_VALUES = {
    "doc_type": {
        "overview",
        "decision_log",
        "guide",
        "theory_note",
        "experiment",
        "result",
        "roadmap",
        "gate",
        "index",
        "reference",
    },
    "stage": {"0", "1", "1.5", "2", "reference"},
    "status": {
        "draft",
        "completed",
        "in_progress",
        "blocked",
        "provenance",
        "reference",
    },
    "evidence_role": {
        "control",
        "hypothesis",
        "proxy_scan",
        "provenance",
        "audit",
        "ssot",
        "reference",
    },
}

ACTIVE_STAGE_DIRS = {
    DOCS / "02_theory",
    DOCS / "03_experiments",
    DOCS / "04_results",
    DOCS / "05_next_steps",
}

PREFIXED_NAME = re.compile(r"^(000|010|015|020|030|040|900)_.+\.md$")


def parse_frontmatter(path: Path) -> tuple[dict[str, str], str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError("missing YAML frontmatter")

    end = text.find("\n---\n", 4)
    if end == -1:
        raise ValueError("unterminated YAML frontmatter")

    raw = text[4:end]
    body = text[end + 5 :]
    data: dict[str, str] = {}
    for line in raw.splitlines():
        if not line or line.startswith("  ") or line.startswith("- "):
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"')
    return data, body


def first_h1(body: str) -> str | None:
    for line in body.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return None


def validate_doc(path: Path) -> list[str]:
    rel = path.relative_to(ROOT)
    errors: list[str] = []

    try:
        frontmatter, body = parse_frontmatter(path)
    except ValueError as exc:
        return [f"{rel}: {exc}"]

    raw_frontmatter = path.read_text(encoding="utf-8").split("\n---\n", 1)[0]
    for line in raw_frontmatter.splitlines()[1:]:
        if ":" not in line or line.startswith("  ") or line.startswith("- "):
            continue
        key, value = line.split(":", 1)
        value = value.strip()
        if ":" in value and not (
            (value.startswith('"') and value.endswith('"'))
            or (value.startswith("'") and value.endswith("'"))
        ):
            errors.append(f"{rel}: `{key.strip()}` contains unquoted colon")

    for field in REQUIRED_FIELDS:
        if field not in frontmatter:
            errors.append(f"{rel}: missing frontmatter field `{field}`")

    for field, allowed in ALLOWED_VALUES.items():
        value = frontmatter.get(field)
        if value and value not in allowed:
            errors.append(f"{rel}: invalid {field} `{value}`")

    h1 = first_h1(body)
    if not h1:
        errors.append(f"{rel}: missing H1")
    elif frontmatter.get("title") and h1 != frontmatter["title"]:
        errors.append(
            f"{rel}: H1 `{h1}` does not match title `{frontmatter['title']}`"
        )

    parent = path.parent
    if parent in ACTIVE_STAGE_DIRS and path.name != "README.md":
        if not PREFIXED_NAME.match(path.name):
            errors.append(f"{rel}: active stage filename lacks sortable prefix")

    if frontmatter.get("status") in {"provenance", "reference"}:
        role = frontmatter.get("evidence_role")
        if role not in {"provenance", "reference"}:
            errors.append(
                f"{rel}: status `{frontmatter['status']}` needs provenance/reference evidence_role"
            )

    return errors


def require_text(path: Path, needle: str, errors: list[str]) -> None:
    if needle not in path.read_text(encoding="utf-8"):
        errors.append(f"{path.relative_to(ROOT)}: missing `{needle}`")


def validate_crosslinks() -> list[str]:
    errors: list[str] = []
    roadmap = DOCS / "05_next_steps" / "000_roadmap.md"
    decision_log = DOCS / "00_project" / "decision_log.md"

    for exp_id in ("exp_000", "exp_001", "exp_002"):
        require_text(roadmap, exp_id, errors)
        require_text(decision_log, exp_id, errors)

    require_text(roadmap, "Level 1.5", errors)
    require_text(roadmap, "phenomenological perturbation closure | completed", errors)
    require_text(roadmap, "physical perturbation closure | blocked", errors)
    require_text(roadmap, "CLASS integration | blocked", errors)
    require_text(roadmap, "CMB comparison | blocked", errors)
    require_text(decision_log, "Demote experiment 002 from evidence to provenance", errors)

    pairs = [
        (
            DOCS / "03_experiments" / "000_exp_000_lcdm_baseline.md",
            DOCS / "04_results" / "000_result_000_lcdm_baseline.md",
        ),
        (
            DOCS / "03_experiments" / "010_exp_001_gamma_scan.md",
            DOCS / "04_results" / "010_result_001_gamma_scan.md",
        ),
        (
            DOCS / "03_experiments" / "015_exp_001_5_phase_transfer_physicality.md",
            DOCS / "04_results" / "015_result_001_5_phase_transfer_physicality.md",
        ),
        (
            DOCS / "03_experiments" / "020_exp_002_entropy_information_gate.md",
            DOCS / "04_results" / "020_result_002_entropy_information_gate.md",
        ),
        (
            DOCS / "03_experiments" / "030_exp_003_phenomenological_perturbation_closure.md",
            DOCS / "04_results" / "030_result_003_phenomenological_perturbation_closure.md",
        ),
    ]
    for experiment, result in pairs:
        if not experiment.exists():
            errors.append(f"{experiment.relative_to(ROOT)}: missing experiment document")
        if not result.exists():
            errors.append(f"{result.relative_to(ROOT)}: missing result document")

    return errors


def main() -> int:
    errors: list[str] = []
    doc_ids: dict[str, Path] = {}
    for path in sorted(DOCS.rglob("*.md")):
        errors.extend(validate_doc(path))
        try:
            frontmatter, _ = parse_frontmatter(path)
        except ValueError:
            continue
        doc_id = frontmatter.get("doc_id")
        if doc_id in doc_ids:
            errors.append(
                f"{path.relative_to(ROOT)}: duplicate doc_id `{doc_id}` also used by {doc_ids[doc_id].relative_to(ROOT)}"
            )
        elif doc_id:
            doc_ids[doc_id] = path
    errors.extend(validate_crosslinks())

    if errors:
        for error in errors:
            print(error)
        return 1

    print("docs validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
