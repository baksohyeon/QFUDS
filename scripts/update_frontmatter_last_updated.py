#!/usr/bin/env python3
"""Update staged Markdown frontmatter ``last_updated`` dates.

This script is intended for the local pre-commit hook. It only touches staged
Markdown files that already have YAML frontmatter and a ``last_updated`` field.
Raw source assets are skipped because they may be upstream snapshots, not QFUDS
documentation records.
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FRONTMATTER_END = "\n---\n"
LAST_UPDATED_RE = re.compile(r"(?m)^last_updated:\s*.*$")

SKIP_PARTS = (
    ("docs", "wiki", "research", "assets", "sources"),
)


def run_git(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=ROOT,
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )


def staged_markdown_paths() -> list[Path]:
    result = run_git(
        ["diff", "--cached", "--name-only", "--diff-filter=ACMR", "--", "*.md"]
    )
    if result.returncode != 0:
        print(result.stderr, file=sys.stderr, end="")
        raise SystemExit(result.returncode)
    return [ROOT / line for line in result.stdout.splitlines() if line]


def has_unstaged_changes(path: Path) -> bool:
    rel = str(path.relative_to(ROOT))
    result = run_git(["diff", "--quiet", "--", rel])
    return result.returncode == 1


def should_skip(path: Path) -> bool:
    try:
        rel_parts = path.relative_to(ROOT).parts
    except ValueError:
        return True

    for prefix in SKIP_PARTS:
        if rel_parts[: len(prefix)] == prefix and "source" in rel_parts:
            return True
    return False


def update_file(path: Path, today: str) -> bool:
    if should_skip(path) or not path.exists():
        return False

    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return False

    end = text.find(FRONTMATTER_END, 4)
    if end == -1:
        return False

    frontmatter = text[: end + len(FRONTMATTER_END)]
    if not LAST_UPDATED_RE.search(frontmatter):
        return False

    updated_frontmatter = LAST_UPDATED_RE.sub(
        f"last_updated: {today}", frontmatter, count=1
    )
    if updated_frontmatter == frontmatter:
        return False

    path.write_text(updated_frontmatter + text[end + len(FRONTMATTER_END) :], encoding="utf-8")
    return True


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--staged",
        action="store_true",
        help="update staged Markdown files and re-stage changed files",
    )
    args = parser.parse_args()

    if not args.staged:
        parser.error("only --staged mode is supported")

    paths = staged_markdown_paths()
    dirty_paths = [path for path in paths if path.exists() and has_unstaged_changes(path)]
    if dirty_paths:
        print(
            "frontmatter last_updated: refusing to auto-update partially staged files:",
            file=sys.stderr,
        )
        for path in dirty_paths:
            print(f"  {path.relative_to(ROOT)}", file=sys.stderr)
        print("Stage or stash unstaged changes, then commit again.", file=sys.stderr)
        return 1

    today = dt.date.today().isoformat()
    changed: list[Path] = []
    for path in paths:
        if update_file(path, today):
            changed.append(path)

    if changed:
        add_result = run_git(["add", *[str(path.relative_to(ROOT)) for path in changed]])
        if add_result.returncode != 0:
            print(add_result.stderr, file=sys.stderr, end="")
            return add_result.returncode
        print("frontmatter last_updated: updated")
        for path in changed:
            print(f"  {path.relative_to(ROOT)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
