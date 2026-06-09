#!/usr/bin/env python3
"""Record-consistency gate originally created before experiment 004 planning.

This script enforces a narrow record rule: the exp_003 documentation, roadmap,
outputs, and decision log must stay internally consistent. It does not run any
physics. It does not rewrite scientific conclusions. It does not authorize
exp_004 for the demoted retained branch. It only verifies that the research
record is complete and non-contradictory, and reports blockers when it is not.

Companion document: ``docs/05_next_steps/030_exp003_record_consistency_gate.md``.
It complements (does not replace) ``scripts/validate_docs.py``, which checks
per-document frontmatter schema. This gate checks cross-document state for the
exp_003 record.

Usage:

    python3 scripts/preflight_exp004.py

Exit code 0 means the exp_003 record-consistency gate passes. Any other exit
code lists the failed checks; those are the blockers that must be fixed first.
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

# Canonical exp_003 documents (theory, experiment, result) and supporting files.
THEORY_DOC = DOCS / "02_theory" / "030_qfuds_phenomenological_perturbations.md"
EXPERIMENT_DOC = DOCS / "03_experiments" / "030_exp_003_phenomenological_perturbation_closure.md"
RESULT_DOC = DOCS / "04_results" / "030_result_003_phenomenological_perturbation_closure.md"
DECISION_LOG = DOCS / "00_project" / "decision_log.md"
ROADMAP = DOCS / "05_next_steps" / "000_roadmap.md"
DOCS_INDEX = DOCS / "README.md"

# Files that are indexes, not "active docs" that must themselves be indexed.
INDEX_FILENAMES = {"README.md"}

# Output references are extracted with this pattern (relative to repo root).
OUTPUT_REF = re.compile(r"outputs/[\w./-]+?\.(?:csv|json|png)")

# A document "claims completion" of a blocked level if any of these match.
# These are deliberately narrow so legitimate "... | blocked" rows and prose
# that merely *mentions* CLASS/CMB/matter-power do not trip the gate.
FORBIDDEN_COMPLETION = [
    re.compile(r"CLASS\s+integration\s*\|\s*completed", re.IGNORECASE),
    re.compile(r"CAMB\s+integration\s*\|\s*completed", re.IGNORECASE),
    re.compile(r"CMB\s+comparison\s*\|\s*completed", re.IGNORECASE),
    re.compile(r"matter[- ]power(?:\s+spectrum)?\s*\|\s*completed", re.IGNORECASE),
    re.compile(r"\bCMB\s+viability\b[^.\n]*\b(established|confirmed|achieved|completed)\b", re.IGNORECASE),
    re.compile(r"\bmatter[- ]power\s+viability\b[^.\n]*\b(established|confirmed|achieved|completed)\b", re.IGNORECASE),
    re.compile(r"\|\s*3\s*\|\s*CLASS[^|]*\|\s*completed", re.IGNORECASE),
    re.compile(r"\|\s*4\s*\|\s*CMB[^|]*\|\s*completed", re.IGNORECASE),
    re.compile(r"\|\s*5\s*\|\s*matter[^|]*\|\s*completed", re.IGNORECASE),
]


@dataclass
class CheckResult:
    name: str
    passed: bool
    details: list[str]


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def check_exp003_documents() -> CheckResult:
    """exp_003 theory, experiment, and result documents must all exist."""
    details: list[str] = []
    for label, path in (
        ("theory", THEORY_DOC),
        ("experiment", EXPERIMENT_DOC),
        ("result", RESULT_DOC),
    ):
        if path.exists():
            details.append(f"OK  exp_003 {label} document: {path.relative_to(ROOT)}")
        else:
            details.append(f"MISSING exp_003 {label} document: {path.relative_to(ROOT)}")
    passed = all(line.startswith("OK") for line in details)
    return CheckResult("exp_003 core documents exist", passed, details)


def check_postmortem_if_referenced() -> CheckResult:
    """If the result or decision log references the friction-bug postmortem, it must exist."""
    details: list[str] = []
    referenced = False
    needle = "postmortem/exp003_friction_bug"
    for path in (RESULT_DOC, DECISION_LOG):
        if path.exists() and needle in _read(path):
            referenced = True
            details.append(f"referenced in {path.relative_to(ROOT)}")

    if not referenced:
        return CheckResult(
            "exp_003 postmortem note (if referenced)",
            True,
            ["no postmortem reference found; nothing to verify"],
        )

    pm_dir = ROOT / "outputs" / "postmortem" / "exp003_friction_bug"
    pm_readme = pm_dir / "README.md"
    passed = pm_dir.is_dir() and pm_readme.exists()
    if passed:
        details.append(f"OK  postmortem note present: {pm_readme.relative_to(ROOT)}")
    else:
        details.append(f"MISSING referenced postmortem note: {pm_readme.relative_to(ROOT)}")
    return CheckResult("exp_003 postmortem note (if referenced)", passed, details)


def check_decision_log_verdict() -> CheckResult:
    """The decision log must record the final exp_003 verdict (P2 fail, P1 survives)."""
    details: list[str] = []
    if not DECISION_LOG.exists():
        return CheckResult("decision log has exp_003 verdict", False, ["MISSING decision_log.md"])
    text = _read(DECISION_LOG)
    required = {
        "experiment 003 mention": "experiment 003" in text.lower() or "exp_003" in text.lower(),
        "P2 failure recorded": bool(re.search(r"P2[^.\n]*fail", text)),
        "P1 survival recorded": bool(re.search(r"P1[^.\n]*(closed|stable|surviv)", text, re.IGNORECASE)),
        "friction-bug correction logged": "friction" in text.lower(),
    }
    for label, ok in required.items():
        details.append(f"{'OK ' if ok else 'MISSING'} {label}")
    return CheckResult("decision log has exp_003 verdict", all(required.values()), details)


def check_roadmap_level2a() -> CheckResult:
    """Roadmap must mark Level 2A completed and 2B/3/4/5 blocked."""
    details: list[str] = []
    if not ROADMAP.exists():
        return CheckResult("roadmap reflects Level 2A status", False, ["MISSING roadmap"])
    text = _read(ROADMAP)
    required = {
        "Level 2A completed": "phenomenological perturbation closure | completed" in text,
        "Level 2B blocked": "physical perturbation closure | blocked" in text,
        "Level 3 CLASS blocked": "CLASS integration | blocked" in text,
        "Level 4 CMB blocked": "CMB comparison | blocked" in text,
        "Level 5 matter-power blocked": "matter power spectrum | blocked" in text,
    }
    for label, ok in required.items():
        details.append(f"{'OK ' if ok else 'MISSING'} {label}")
    return CheckResult("roadmap reflects Level 2A status", all(required.values()), details)


def check_referenced_outputs_exist() -> CheckResult:
    """Every outputs/* file referenced by exp_003 docs must exist on disk."""
    details: list[str] = []
    referenced: set[str] = set()
    for path in (RESULT_DOC, EXPERIMENT_DOC, DECISION_LOG):
        if path.exists():
            referenced.update(OUTPUT_REF.findall(_read(path)))

    if not referenced:
        return CheckResult(
            "exp_003 referenced outputs exist",
            False,
            ["no outputs/* references found in exp_003 docs (unexpected)"],
        )

    missing = sorted(ref for ref in referenced if not (ROOT / ref).exists())
    present = sorted(referenced - set(missing))
    for ref in present:
        details.append(f"OK  {ref}")
    for ref in missing:
        details.append(f"MISSING {ref}")
    return CheckResult("exp_003 referenced outputs exist", not missing, details)


def check_no_premature_completion() -> CheckResult:
    """No document may claim Level 3 / CLASS / CMB / matter-power completion."""
    details: list[str] = []
    scanned = sorted(DOCS.rglob("*.md")) + [ROOT / "README.md"]
    offenders: list[str] = []
    for path in scanned:
        if not path.exists():
            continue
        text = _read(path)
        for pattern in FORBIDDEN_COMPLETION:
            match = pattern.search(text)
            if match:
                offenders.append(
                    f"VIOLATION {path.relative_to(ROOT)}: matched `{match.group(0).strip()}`"
                )
    if offenders:
        details.extend(offenders)
    else:
        details.append("OK  no premature Level 3/CLASS/CMB/matter-power completion claims")
    return CheckResult("no premature completion claims", not offenders, details)


def check_docs_index_complete() -> CheckResult:
    """docs/README.md must reference every active (non-index) doc under docs/."""
    details: list[str] = []
    if not DOCS_INDEX.exists():
        return CheckResult("docs/README.md indexes all active docs", False, ["MISSING docs/README.md"])
    index_text = _read(DOCS_INDEX)
    missing: list[str] = []
    for path in sorted(DOCS.rglob("*.md")):
        if path == DOCS_INDEX or path.name in INDEX_FILENAMES:
            continue
        rel_to_docs = path.relative_to(DOCS).as_posix()
        # Accept either the docs-relative path or the bare filename in the index.
        if rel_to_docs not in index_text and path.name not in index_text:
            missing.append(rel_to_docs)
    if missing:
        for rel in missing:
            details.append(f"NOT INDEXED {rel}")
    else:
        details.append("OK  every active doc appears in docs/README.md")
    return CheckResult("docs/README.md indexes all active docs", not missing, details)


CHECKS = (
    check_exp003_documents,
    check_postmortem_if_referenced,
    check_decision_log_verdict,
    check_roadmap_level2a,
    check_referenced_outputs_exist,
    check_no_premature_completion,
    check_docs_index_complete,
)


def main() -> int:
    print("QFUDS exp_003 record consistency gate")
    print("=" * 60)
    results = [check() for check in CHECKS]

    failed = [r for r in results for _ in (0,) if not r.passed]
    for result in results:
        status = "PASS" if result.passed else "FAIL"
        print(f"\n[{status}] {result.name}")
        for line in result.details:
            print(f"    {line}")

    print("\n" + "=" * 60)
    if failed:
        print(f"PREFLIGHT FAILED: {len(failed)} exp_003 record check(s)")
        print("Record blockers:")
        for result in failed:
            print(f"  - {result.name}")
        return 1

    print("PREFLIGHT PASSED: exp_003 record is consistent")
    return 0


if __name__ == "__main__":
    sys.exit(main())
