#!/usr/bin/env python3
"""Guard external-research Markdown claims behind the workflow checklist."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path
from typing import Callable


ROOT = Path(__file__).resolve().parents[1]

STATE_TOKENS = {
    "not searched",
    "searched_no_hit",
    "hit_not_cached",
    "asset_available_not_downloaded",
    "asset_downloaded_not_extracted",
    "asset_extracted_not_digitized",
    "asset_digitized",
    "asset_cached",
    "inspected_no_numerical_product",
    "no_asset_found",
    "inaccessible",
}

WORKFLOW_MARKERS = {
    "Research Asset and Product Workflow",
    "research-asset-product-workflow.md",
    ".agent/workflows/research-asset-product-workflow.md",
}

TOOL_REFERENCE_LINKS = {
    "[PageIndex](https://github.com/VectifyAI/PageIndex)": "PageIndex",
    "[MarkItDown](https://github.com/microsoft/markitdown)": "MarkItDown",
}

STRICT_EXTERNAL_RESEARCH_RE = re.compile(
    r"(?ix)"
    r"https?://|"
    r"\barxiv\b|"
    r"\bdoi\b|"
    r"\bnasa\b|"
    r"\blambda\b|"
    r"\bdesi\b|"
    r"\beboss\b|"
    r"\bbao\b|"
    r"\bzenodo\b|"
    r"\bosf\b|"
    r"\bdataverse\b|"
    r"\bgithub\b|"
    r"\bpdf\b|"
    r"\bsupplement(?:ary)?\b|"
    r"\bsource bundle\b|"
    r"\bdownloadable\b|"
    r"\bpage[- ]?family\b|"
    r"\btemplated URL\b"
)

RESEARCH_FOLDER_RE = re.compile(
    STRICT_EXTERNAL_RESEARCH_RE.pattern
    + r"|"
    + r"\bfigure(?:-level)?\b|"
    + r"\btable(?:-level)?\b|"
    + r"\bdata[- ]?product\b|"
    + r"\basset\b",
    re.IGNORECASE | re.VERBOSE,
)

ABSENCE_CLAIM_RE = re.compile(
    r"(?ix)"
    r"no\s+(?:product|asset|data|source|hit)\s+(?:found|available)|"
    r"(?:product|asset|data|source)\s+(?:missing|unavailable|not\s+found)|"
    r"not\s+extractable|"
    r"QFUDS-ready\s+product\s+(?:not\s+found|missing|unavailable)|"
    r"literature\s+checked|"
    r"coverage\s+complete"
)


def run_git(args: list[str]) -> str:
    completed = subprocess.run(
        ["git", *args],
        cwd=ROOT,
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return completed.stdout


def staged_files() -> list[Path]:
    output = run_git(["diff", "--cached", "--name-only", "--diff-filter=ACMR"])
    return [Path(line) for line in output.splitlines() if line.strip()]


def all_doc_files() -> list[Path]:
    return [path.relative_to(ROOT) for path in (ROOT / "docs").rglob("*.md")]


def staged_text(path: Path) -> str:
    try:
        return run_git(["show", f":{path.as_posix()}"])
    except subprocess.CalledProcessError:
        return (ROOT / path).read_text(encoding="utf-8")


def staged_diff(path: Path) -> str:
    return run_git(["diff", "--cached", "--unified=0", "--", path.as_posix()])


def file_text(path: Path, staged: bool) -> str:
    if staged:
        return staged_text(path)
    return (ROOT / path).read_text(encoding="utf-8")


# Subtrees under docs/ that are Claude plugin sources, not QFUDS research docs,
# and therefore exempt from the external-research workflow guard.
EXCLUDED_PREFIXES = (
    "docs/wiki/fiction/saga-fiction-studio/",
)


def is_checked_markdown(path: Path) -> bool:
    if path.suffix.lower() != ".md":
        return False
    posix = path.as_posix()
    if not posix.startswith("docs/"):
        return False
    if posix.startswith(EXCLUDED_PREFIXES):
        return False
    return True


def has_workflow_marker(text: str) -> bool:
    return any(marker in text for marker in WORKFLOW_MARKERS)


def has_state_token(text: str) -> bool:
    lowered = text.lower()
    return any(token.lower() in lowered for token in STATE_TOKENS)


def has_external_research_signal(path: Path, text: str) -> bool:
    if path.as_posix().startswith("docs/wiki/research/"):
        return RESEARCH_FOLDER_RE.search(text) is not None
    return STRICT_EXTERNAL_RESEARCH_RE.search(text) is not None


def has_absence_claim(text: str) -> bool:
    return ABSENCE_CLAIM_RE.search(text) is not None


def normalize_tool_reference_links(text: str) -> str:
    for linked, plain in TOOL_REFERENCE_LINKS.items():
        text = text.replace(linked, plain)
    return text


def canonical_tool_reference_link_text(text: str) -> str:
    return " ".join(normalize_tool_reference_links(text).split())


# Matches the ``](target)`` tail of an inline markdown link, capturing the
# target; used to neutralize *internal* link targets so a pure relative-path
# edit compares equal on both sides.
LINK_TARGET_RE = re.compile(r"\]\(([^)]*)\)")
# Prefixes that make a link target external. These are left literal when
# masking so a target flipping to an external URL is NOT read as a cosmetic
# path edit (that would add an external-research claim the gate must catch).
EXTERNAL_LINK_PREFIXES = ("http://", "https://", "mailto:")


def mask_link_targets(text: str) -> str:
    def neutralize(match: re.Match[str]) -> str:
        if match.group(1).strip().startswith(EXTERNAL_LINK_PREFIXES):
            return match.group(0)
        return "](#)"

    return LINK_TARGET_RE.sub(neutralize, text)


def staged_hunks(path: Path) -> list[tuple[list[str], list[str]]]:
    """Return the staged diff's hunks as (removed_lines, added_lines) pairs."""
    diff = staged_diff(path)
    if not diff:
        return []

    hunks: list[tuple[list[str], list[str]]] = []
    removed: list[str] = []
    added: list[str] = []

    def flush() -> None:
        nonlocal removed, added
        if removed or added:
            hunks.append((removed, added))
        removed = []
        added = []

    for line in diff.splitlines():
        if line.startswith(("diff --git ", "index ", "--- ", "+++ ")):
            continue
        if line.startswith("@@"):
            flush()
            continue
        if line.startswith("-"):
            removed.append(line[1:])
        elif line.startswith("+"):
            added.append(line[1:])
        elif line.startswith(" "):
            flush()

    flush()
    return hunks


def hunks_match_after_normalize(
    hunks: list[tuple[list[str], list[str]]], normalize: Callable[[str], str]
) -> bool:
    """True if every non-``last_updated`` hunk is unchanged once ``normalize`` is
    applied to both sides, and at least one hunk really changed.
    """
    if not hunks:
        return False

    changed_any = False
    for removed_lines, added_lines in hunks:
        if not removed_lines or not added_lines:
            return False
        if all(line.startswith("last_updated:") for line in removed_lines + added_lines):
            continue
        removed_text = "\n".join(removed_lines)
        added_text = "\n".join(added_lines)
        if normalize(removed_text) != normalize(added_text):
            return False
        if removed_text != added_text:
            changed_any = True

    return changed_any


def staged_change_adds_no_research_claim(path: Path) -> bool:
    """True if the staged edit only rewrites tool-reference links or internal
    link *targets* (plus ``last_updated``) — none of which adds an
    external-research claim, so it must not trip the workflow gate. Parses the
    staged diff once and tests both exemptions against it.
    """
    hunks = staged_hunks(path)
    return hunks_match_after_normalize(
        hunks, canonical_tool_reference_link_text
    ) or hunks_match_after_normalize(hunks, mask_link_targets)


def is_navigation_index(text: str) -> bool:
    return re.search(r"(?m)^doc_type:\s*index\s*$", text) is not None


def check_file(path: Path, staged: bool) -> list[str]:
    text = file_text(path, staged=staged)
    if is_navigation_index(text):
        return []
    if not has_external_research_signal(path, text) and not has_absence_claim(text):
        return []

    errors: list[str] = []
    if not has_workflow_marker(text):
        errors.append(
            "missing Research Asset and Product Workflow marker/link "
            "for external-research or product-availability claims"
        )
    if not has_state_token(text):
        errors.append(
            "missing workflow state token such as asset_cached, "
            "hit_not_cached, no_asset_found, or inaccessible"
        )
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Require workflow evidence for staged Markdown files that make "
            "external-research, asset, or product-availability claims."
        )
    )
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--staged", action="store_true", help="check staged files")
    mode.add_argument("--all", action="store_true", help="check all docs files")
    args = parser.parse_args()

    staged = not args.all
    paths = staged_files() if staged else all_doc_files()
    paths = [path for path in paths if is_checked_markdown(path)]

    if not paths:
        scope = "staged" if staged else "docs"
        print(f"agent workflow guard: no {scope} Markdown files to check")
        return 0

    failures: list[tuple[Path, list[str]]] = []
    for path in paths:
        errors = check_file(path, staged=staged)
        if errors and staged and staged_change_adds_no_research_claim(path):
            continue
        if errors:
            failures.append((path, errors))

    if not failures:
        print("agent workflow guard: passed")
        return 0

    print("agent workflow guard: failed", file=sys.stderr)
    for path, errors in failures:
        print(f"- {path}", file=sys.stderr)
        for error in errors:
            print(f"  - {error}", file=sys.stderr)
    print(
        "\nApply .agent/workflows/research-asset-product-workflow.md and "
        "record the workflow state before committing.",
        file=sys.stderr,
    )
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
