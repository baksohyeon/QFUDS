#!/usr/bin/env python3
"""Deterministic fiction-system gate.

Hard checks cover mechanical contracts only. Literary taste, topics, punctuation,
and character voice are not commit blockers. Those belong to work-local profiles
and evidence-based review.
"""

import pathlib
import re
import subprocess
import sys


ROOTS = (
    "AGENTS.md",
    "CLAUDE.md",
    "fiction",
    "creative_harness",
    ".agent/templates/fiction",
    ".agent/workflows",
    ".agents/skills/fiction-production",
    "tools/saga-fiction-studio",
)

KOREAN_AI_TELL = re.compile(
    r"단순히\s+.{1,30}(넘어|아니라)|"
    r"그것은\s+.{1,30}(언어|증명|선언|질문|대답)(이었|였|이다)|"
    r"결론적으로|시사하는\s+바가\s+크다|"
    r"^(또한|따라서|그러므로|나아가)[,\s]",
    re.I,
)

STALE_ACTIVE_PATH = re.compile(
    r"creative_harness/craft/(009_korean_fiction_prose_naturalness_harness_ko|"
    r"010_reader_onboarding_harness_ko)\.md"
)

PROJECT_HOME_FIELDS = (
    "- Work id:",
    "- Style profile:",
    "- Canon promotion authority/rule:",
    "- Current draft:",
    "## Current Next Action",
)

ZETTEL_KINDS = {"idea", "question", "pattern", "principle", "technique", "observation"}


def staged_markdown():
    out = subprocess.run(
        ["git", "diff", "--cached", "--name-only", "--diff-filter=ACMR"],
        capture_output=True,
        text=True,
        check=False,
    ).stdout.splitlines()
    return [p for p in out if p.endswith(".md") and p.startswith(ROOTS)]


def all_markdown():
    found = []
    for root in ROOTS:
        path = pathlib.Path(root)
        if path.is_file() and path.suffix == ".md":
            found.append(str(path))
        elif path.exists():
            found.extend(str(p) for p in path.rglob("*.md"))
    return found


def project_root(path):
    parts = pathlib.PurePosixPath(path).parts
    try:
        index = parts.index("projects")
    except ValueError:
        return None
    if index == 0 or parts[index - 1] != "fiction" or len(parts) <= index + 1:
        return None
    return pathlib.Path(*parts[: index + 2])


def parse_simple_frontmatter(text):
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end < 0:
        return None
    values = {}
    for line in text[4:end].splitlines():
        match = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if match:
            values[match.group(1)] = match.group(2).strip()
    return values


def check_project_home(file_path, text, errors):
    if not re.fullmatch(r"fiction/projects/[^/]+/README\.md", file_path):
        return
    for field in PROJECT_HOME_FIELDS:
        if field not in text:
            errors.append(f"{file_path}: project Home Note missing {field!r}")


def check_zettel(file_path, text, errors):
    if not file_path.startswith("fiction/knowledge/notes/") or file_path.endswith("/README.md"):
        return
    frontmatter = parse_simple_frontmatter(text)
    if frontmatter is None:
        errors.append(f"{file_path}: Zettel requires real top-of-file YAML frontmatter")
        return
    if frontmatter.get("type") != "zettel":
        errors.append(f"{file_path}: Zettel frontmatter requires type: zettel")
    if frontmatter.get("kind") not in ZETTEL_KINDS:
        errors.append(f"{file_path}: Zettel kind must be one supported atomic-note kind")
    for key in ("created", "source-ids", "related-notes", "related-projects"):
        if key not in frontmatter:
            errors.append(f"{file_path}: Zettel frontmatter missing {key}")


def check_project_member(file_path, errors):
    root = project_root(file_path)
    if root is None or pathlib.PurePosixPath(file_path).name == "README.md":
        return
    if not (root / "README.md").exists():
        errors.append(f"{file_path}: project artifact has no project Home Note at {root / 'README.md'}")


def check_release(file_path, text, errors):
    if "/release/candidates/" in file_path:
        if not re.search(r"_[0-9a-f]{7,40}\.md$", file_path):
            errors.append(f"{file_path}: release candidate filename must end with baseline short SHA")
    if "/release/published/" not in file_path:
        return
    root = project_root(file_path)
    if root is None:
        return
    home = root / "README.md"
    home_text = home.read_text(encoding="utf-8") if home.exists() else ""
    if not re.search(r"(?:State|Status):\s*`?released`?", home_text, re.I):
        errors.append(f"{file_path}: published snapshot requires project state released")
    review_root = root / "reviews"
    if not any(review_root.glob("retention/*.md")):
        errors.append(f"{file_path}: published snapshot requires a retention gate artifact")
    if not any(review_root.glob("release/*.md")):
        errors.append(f"{file_path}: published snapshot requires a release checklist artifact")


def is_korean_prose(path):
    name = pathlib.Path(path).name.lower()
    return "/drafts/" in path and (
        name.endswith("_ko.md")
        or "korean" in name
        or "한국어" in name
    )


def in_example_or_watchlist(path, line):
    if path.endswith("korean_fiction_prose_naturalness_harness.md"):
        return True
    if path.endswith("prose_verisimilitude_audit_checklist.md"):
        return True
    return "failure signal" in line.lower() or "실패 신호" in line


def check(files):
    errors = []
    warnings = []

    for file_path in files:
        path = pathlib.Path(file_path)
        try:
            text = path.read_text(encoding="utf-8")
        except FileNotFoundError:
            continue

        if STALE_ACTIVE_PATH.search(text):
            errors.append(f"{file_path}: removed numeric craft path referenced")

        check_project_home(file_path, text, errors)
        check_zettel(file_path, text, errors)
        check_project_member(file_path, errors)
        check_release(file_path, text, errors)

        if is_korean_prose(file_path):
            for number, line in enumerate(text.splitlines(), 1):
                if KOREAN_AI_TELL.search(line) and not in_example_or_watchlist(file_path, line):
                    warnings.append(
                        f"{file_path}:{number}: Korean prose diagnostic; review span in context: "
                        f"{line.strip()[:90]}"
                    )

    return errors, warnings


def main():
    files = staged_markdown() if "--staged" in sys.argv else all_markdown()
    if not files:
        print("fiction_gate: no matching Markdown files")
        return 0

    errors, warnings = check(files)
    if warnings:
        print("fiction_gate: warnings (work-profile review, not commit blockers):")
        for warning in warnings:
            print("  " + warning)

    if errors:
        print("fiction_gate: mechanical contract violations:")
        for error in errors:
            print("  " + error)
        return 1

    print(f"fiction_gate: PASS ({len(files)} Markdown file(s) checked)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
