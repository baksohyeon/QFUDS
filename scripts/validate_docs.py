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

# Subtrees under docs/ that are not QFUDS documentation and therefore are exempt
# from the frontmatter schema and markdown-link hygiene. Currently this covers
# Claude plugin sources (SKILL.md files use the plugin frontmatter `name`/
# `description`, not the docs schema).
EXCLUDED_DOC_PREFIXES = (
    "docs/wiki/fiction/saga-fiction-studio/",
)


def is_excluded_doc(path: Path) -> bool:
    rel = path.relative_to(ROOT).as_posix()
    return rel.startswith(EXCLUDED_DOC_PREFIXES)


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
        "summary",
        "postmortem",
        "roadmap",
        "gate",
        "index",
        "reference",
    },
    "stage": {"0", "1", "1.5", "2", "3", "4", "5", "6", "reference"},
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
MD_PATH_RE = re.compile(
    r"(?P<path>(?:\.\.?/|docs/|outputs/|[A-Za-z0-9_-]+/)?[A-Za-z0-9_./-]+\.md)"
)
PNG_IMAGE_RE = re.compile(r"!\[[^\]]*\]\((?P<path>[^)#]+\.png)(?:#[^)]+)?\)")

SECTION_RULES = {
    "experiment": {
        "Objective": ("Objective",),
        "Hypothesis": ("Hypothesis",),
        "Scope": ("Scope",),
        "Failure Criteria": ("Failure Criteria",),
        "Outputs": ("Outputs", "Required Outputs"),
        "Decision": ("Decision", "Decision Rule"),
    },
    "result": {
        "Scope": ("Scope",),
        "Evidence or Outputs": (
            "Outputs",
            "Figures",
            "Evidence",
            "Plots / Output Files Produced",
        ),
        "Decision": ("Decision",),
        "Next Gate": ("Next Gate", "Next Test", "Next Step", "What Became The Next Target"),
    },
}


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


def headings(body: str) -> list[str]:
    found: list[str] = []
    for line in body.splitlines():
        stripped = line.strip()
        if stripped.startswith("#"):
            found.append(stripped.lstrip("#").strip().lower())
    return found


def has_heading(body_headings: list[str], labels: tuple[str, ...]) -> bool:
    lowered = tuple(label.lower() for label in labels)
    return any(any(label in heading for label in lowered) for heading in body_headings)


def resolve_md_reference(path: Path, reference: str) -> Path:
    if reference.startswith("docs/") or reference.startswith("outputs/"):
        return ROOT / reference
    relative_path = (path.parent / reference).resolve()
    if relative_path.exists():
        return relative_path
    root_path = ROOT / reference
    if root_path.exists():
        return root_path
    return relative_path


def validate_markdown_doc_links(path: Path, body: str) -> list[str]:
    """Require concrete Markdown document references to be clickable links."""
    errors: list[str] = []
    in_fence = False
    for line_number, line in enumerate(body.splitlines(), start=1):
        if line.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if line.lstrip().startswith("#"):
            continue
        for match in MD_PATH_RE.finditer(line):
            reference = match.group("path")
            if "*" in reference:
                continue
            previous = line[match.start() - 1] if match.start() > 0 else ""
            if previous in {"(", "[", "<"}:
                continue
            referenced_path = resolve_md_reference(path, reference)
            if referenced_path.exists() and referenced_path.suffix == ".md":
                rel = path.relative_to(ROOT)
                errors.append(
                    f"{rel}:{line_number}: `{reference}` should be a Markdown link"
                )
    return errors


def resolve_local_reference(path: Path, reference: str) -> Path:
    if reference.startswith("docs/") or reference.startswith("outputs/"):
        return ROOT / reference
    return (path.parent / reference).resolve()


def validate_local_png_links(path: Path, body: str) -> list[str]:
    """Require active stage local PNG image links to point at existing files."""
    errors: list[str] = []
    rel = path.relative_to(ROOT)
    for line_number, line in enumerate(body.splitlines(), start=1):
        for match in PNG_IMAGE_RE.finditer(line):
            reference = match.group("path")
            if "://" in reference or reference.startswith("/"):
                continue
            target = resolve_local_reference(path, reference)
            if not target.exists():
                errors.append(
                    f"{rel}:{line_number}: local PNG `{reference}` does not exist"
                )
    return errors


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

    doc_type = frontmatter.get("doc_type")
    if doc_type in SECTION_RULES:
        body_headings = headings(body)
        for section, accepted_labels in SECTION_RULES[doc_type].items():
            if not has_heading(body_headings, accepted_labels):
                errors.append(f"{rel}: missing required `{section}` section")

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

    errors.extend(validate_markdown_doc_links(path, body))
    if path.parent in ACTIVE_STAGE_DIRS:
        errors.extend(validate_local_png_links(path, body))

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


def validate_global_markdown_link_hygiene() -> list[str]:
    """Check non-docs Markdown files that are not part of the frontmatter schema."""
    errors: list[str] = []
    paths = list(ROOT.glob("*.md"))
    postmortem_dir = ROOT / "outputs" / "postmortem"
    if postmortem_dir.exists():
        paths.extend(postmortem_dir.rglob("*.md"))

    for path in sorted(paths):
        text = path.read_text(encoding="utf-8")
        errors.extend(validate_markdown_doc_links(path, text))
    return errors


def main() -> int:
    errors: list[str] = []
    doc_ids: dict[str, Path] = {}
    for path in sorted(DOCS.rglob("*.md")):
        if is_excluded_doc(path):
            continue
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
    errors.extend(validate_global_markdown_link_hygiene())

    if errors:
        for error in errors:
            print(error)
        return 1

    print("docs validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
