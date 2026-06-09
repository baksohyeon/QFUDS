#!/usr/bin/env python3
"""Enforce QFUDS documentation status-authority consistency.

This script is the repository-consistency layer that sits above
``scripts/validate_docs.py``. Where ``validate_docs.py`` checks per-document
frontmatter schema, this script checks *cross-document authority*: that the
roadmap is the single source of truth for project status and that no other
document maintains an independent, drift-prone copy of that status.

It runs no physics and rewrites no scientific conclusions. It only verifies that
the research record is internally consistent and reports blockers when it is not.

Authority hierarchy enforced here:

    CLAUDE.md  ->  AGENTS.md  ->  docs/05_next_steps/000_roadmap.md  (status SSOT)
                                    ->  docs/00_project/decision_log.md
                                          ->  docs/03_experiments/ + docs/04_results/

Checks:

1. Roadmap claims have evidence
   Every repository path the roadmap cites as evidence must exist on disk.

2. Completed experiments are fully documented
   Every experiment/result pair must exist and be recorded in the decision log.

3. AGENTS.md does not maintain independent roadmap status.
4. CLAUDE.md does not maintain independent roadmap status (and is a thin wrapper).
5. README.md, PROJECT.md, and the single project overview
   (docs/00_project/overview.md) do not contradict the roadmap with their own
   status.

6. No orphan completed experiment or result documents
   Completed experiment docs have matching result docs, result docs have matching
   experiment docs, and draft/in-progress experiment specs may exist before
   execution.

Usage:

    python3 scripts/research_consistency.py

Exit code 0 means the repository's status authority is consistent. Any other
exit code lists the failed checks; those are the drift blockers to fix.
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

ROADMAP = DOCS / "05_next_steps" / "000_roadmap.md"
DECISION_LOG = DOCS / "00_project" / "decision_log.md"
EXPERIMENTS_DIR = DOCS / "03_experiments"
RESULTS_DIR = DOCS / "04_results"

# The governance files that must defer status to the roadmap.
AGENTS = ROOT / "AGENTS.md"
CLAUDE = ROOT / "CLAUDE.md"
README = ROOT / "README.md"
PROJECT = ROOT / "PROJECT.md"

# The single project overview, which must also defer status to the roadmap.
OVERVIEW = DOCS / "00_project" / "overview.md"

ROADMAP_REF = "docs/05_next_steps/000_roadmap.md"

# A line "maintains status" if it ties a numbered Level to a status keyword.
# Both must appear on the same line for it to count as an independent status
# claim. This is deliberately narrow so that prose referencing levels, or prose
# using status words elsewhere, does not trip the gate.
LEVEL_RE = re.compile(r"\blevel\s*[0-9]", re.IGNORECASE)
STATUS_RE = re.compile(
    r"\b(completed|complete|blocked|not[ _-]?started|in[ _]progress|in_progress|done)\b",
    re.IGNORECASE,
)

# Repository paths the roadmap may cite as evidence.
EVIDENCE_PATH_RE = re.compile(r"(?:docs|outputs|tests|qfuds|scripts)/[A-Za-z0-9_./-]+")
_STRIP = "`'\".,;:)("

# Experiment / result identity tokens, e.g. exp_001_5 -> "001_5".
EXP_ID_RE = re.compile(r"exp_([0-9]+(?:_[0-9]+)?)")
RESULT_ID_RE = re.compile(r"result_([0-9]+(?:_[0-9]+)?)")


@dataclass
class CheckResult:
    name: str
    passed: bool
    details: list[str]


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _body_after_frontmatter(lines: list[str]) -> int:
    """Return the index of the first body line after any YAML frontmatter.

    The frontmatter ``next_gate`` field legitimately names a gate (e.g.
    "keep Level 2B blocked"); it is a controlled field, not a duplicated status
    table, so it is excluded from the status-line scan.
    """
    if not lines or lines[0].strip() != "---":
        return 0
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return i + 1
    return 0


def _status_lines(path: Path) -> list[str]:
    """Return 'file:line' markers for body lines that tie a Level to a status word."""
    offenders: list[str] = []
    if not path.exists():
        return offenders
    lines = _read(path).splitlines()
    start = _body_after_frontmatter(lines)
    for n, line in enumerate(lines[start:], start=start + 1):
        if LEVEL_RE.search(line) and STATUS_RE.search(line):
            offenders.append(f"{path.relative_to(ROOT)}:{n}: `{line.strip()}`")
    return offenders


def check_roadmap_evidence() -> CheckResult:
    """Every repository path the roadmap cites as evidence must exist."""
    details: list[str] = []
    if not ROADMAP.exists():
        return CheckResult("roadmap claims have evidence", False, ["MISSING roadmap"])

    refs: set[str] = set()
    for raw in EVIDENCE_PATH_RE.findall(_read(ROADMAP)):
        ref = raw.strip(_STRIP)
        if ref:
            refs.add(ref)

    missing = sorted(ref for ref in refs if not (ROOT / ref).exists())
    present = sorted(refs - set(missing))
    for ref in present:
        details.append(f"OK  {ref}")
    for ref in missing:
        details.append(f"MISSING evidence cited by roadmap: {ref}")
    return CheckResult("roadmap claims have evidence", not missing, details)


def _doc_pairs() -> tuple[dict[str, Path], dict[str, Path]]:
    experiments: dict[str, Path] = {}
    results: dict[str, Path] = {}
    for path in sorted(EXPERIMENTS_DIR.glob("*.md")):
        if path.name == "README.md":
            continue
        m = EXP_ID_RE.search(path.name)
        if m:
            experiments[m.group(1)] = path
    for path in sorted(RESULTS_DIR.glob("*.md")):
        if path.name == "README.md":
            continue
        m = RESULT_ID_RE.search(path.name)
        if m:
            results[m.group(1)] = path
    return experiments, results


def _frontmatter_value(path: Path, key: str) -> str | None:
    """Return a simple top-level frontmatter scalar value if present."""
    text = _read(path)
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end == -1:
        return None
    for line in text[4:end].splitlines():
        if line.startswith("  ") or line.startswith("- ") or ":" not in line:
            continue
        found_key, value = line.split(":", 1)
        if found_key.strip() == key:
            return value.strip().strip('"').strip("'")
    return None


def check_completed_experiments_documented() -> CheckResult:
    """Each experiment/result pair must be recorded in the decision log."""
    details: list[str] = []
    if not DECISION_LOG.exists():
        return CheckResult("experiments recorded in decision log", False, ["MISSING decision_log.md"])

    log_text = _read(DECISION_LOG)
    experiments, results = _doc_pairs()
    ok = True
    for exp_id, exp_path in sorted(experiments.items()):
        result_path = results.get(exp_id)
        if result_path is None:
            continue  # orphan check reports this; skip here
        needles = {
            f"exp_{exp_id}",
            f"result_{exp_id}",
            exp_path.name,
            result_path.name,
        }
        if any(needle in log_text for needle in needles):
            details.append(f"OK  exp_{exp_id} recorded in decision log")
        else:
            ok = False
            details.append(f"MISSING decision-log entry for exp_{exp_id}")
    if not details:
        details.append("no experiment/result pairs found (unexpected)")
        ok = False
    return CheckResult("experiments recorded in decision log", ok, details)


def _independent_status_check(path: Path, name: str, extra_refs: list[str]) -> CheckResult:
    details: list[str] = []
    passed = True
    if not path.exists():
        return CheckResult(name, False, [f"MISSING {path.name}"])

    text = _read(path)

    if ROADMAP_REF not in text:
        passed = False
        details.append(f"MISSING reference to roadmap SSOT ({ROADMAP_REF})")
    else:
        details.append(f"OK  references roadmap SSOT")

    for ref in extra_refs:
        if ref not in text:
            passed = False
            details.append(f"MISSING required reference: {ref}")
        else:
            details.append(f"OK  references {ref}")

    offenders = _status_lines(path)
    if offenders:
        passed = False
        details.append(f"maintains independent level/status ({len(offenders)} line(s)):")
        details.extend(f"  VIOLATION {o}" for o in offenders)
    else:
        details.append("OK  no independent level/status lines")

    return CheckResult(name, passed, details)


def check_agents_no_status() -> CheckResult:
    return _independent_status_check(AGENTS, "AGENTS.md defers status to roadmap", [])


def check_claude_no_status() -> CheckResult:
    # CLAUDE.md must be a thin wrapper: reference AGENTS.md and the roadmap.
    return _independent_status_check(CLAUDE, "CLAUDE.md is a thin wrapper", ["AGENTS.md"])


def check_human_facing_no_status() -> CheckResult:
    """Human-facing entry points and the overview must defer status to the roadmap."""
    details: list[str] = []
    passed = True
    for path in (README, PROJECT, OVERVIEW):
        sub = _independent_status_check(path, str(path.relative_to(ROOT)), [])
        marker = "OK " if sub.passed else "FAIL"
        details.append(f"[{marker}] {path.relative_to(ROOT)}")
        details.extend(f"    {line}" for line in sub.details)
        passed = passed and sub.passed
    return CheckResult("README.md, PROJECT.md, and overview defer status to roadmap", passed, details)


def check_no_orphan_docs() -> CheckResult:
    """Completed experiment docs have matching results; draft specs may wait."""
    details: list[str] = []
    experiments, results = _doc_pairs()
    exp_ids = set(experiments)
    result_ids = set(results)

    orphan_experiments: list[str] = []
    pending_experiments: list[str] = []
    for exp_id in sorted(exp_ids - result_ids):
        status = _frontmatter_value(experiments[exp_id], "status")
        if status in {"draft", "in_progress"}:
            pending_experiments.append(exp_id)
        else:
            orphan_experiments.append(exp_id)
    orphan_results = sorted(result_ids - exp_ids)

    for exp_id in pending_experiments:
        details.append(
            f"PENDING experiment spec {experiments[exp_id].relative_to(ROOT)} has no result yet"
        )
    for exp_id in orphan_experiments:
        details.append(
            f"ORPHAN experiment {experiments[exp_id].relative_to(ROOT)} has no matching result doc"
        )
    for result_id in orphan_results:
        details.append(
            f"ORPHAN result {results[result_id].relative_to(ROOT)} has no matching experiment doc"
        )

    if not orphan_experiments and not orphan_results:
        details.append(
            f"OK  {len(result_ids)} completed experiment/result pairs, "
            f"{len(pending_experiments)} pending spec(s), no invalid orphans"
        )

    return CheckResult(
        "no orphan completed experiment/result documents",
        not (orphan_experiments or orphan_results),
        details,
    )


CHECKS = (
    check_roadmap_evidence,
    check_completed_experiments_documented,
    check_agents_no_status,
    check_claude_no_status,
    check_human_facing_no_status,
    check_no_orphan_docs,
)


def main() -> int:
    print("QFUDS research consistency audit")
    print("=" * 60)
    results = [check() for check in CHECKS]

    failed = [r for r in results if not r.passed]
    for result in results:
        status = "PASS" if result.passed else "FAIL"
        print(f"\n[{status}] {result.name}")
        for line in result.details:
            print(f"    {line}")

    print("\n" + "=" * 60)
    if failed:
        print(f"CONSISTENCY FAILED: {len(failed)} check(s) found drift")
        print("Blockers (must be fixed):")
        for result in failed:
            print(f"  - {result.name}")
        return 1

    print("CONSISTENCY PASSED: roadmap is the single source of truth; no drift detected")
    return 0


if __name__ == "__main__":
    sys.exit(main())
