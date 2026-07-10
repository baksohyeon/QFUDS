#!/usr/bin/env python3
"""Check local Markdown and image link targets under specified roots.

The checker is intentionally filesystem-only: it validates whether local link
destinations resolve to files or directories in the current checkout, while
ignoring external URLs, mail links, anchor-only links, and fenced code blocks.
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote


FENCE_RE = re.compile(r"^[ \t]{0,3}(`{3,}|~{3,})")
SCHEME_RE = re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*:")
REPO_ROOT = Path(__file__).resolve().parents[1]
SKIPPED_DIRECTORY_NAMES = {".git", ".obsidian", "__pycache__"}


@dataclass(frozen=True)
class MissingLink:
    source: Path
    line: int
    target: str
    resolved: Path


def iter_markdown_files(root: Path) -> list[Path]:
    """Return Markdown files, pruning config and nested-repository trees."""
    if not root.exists():
        return []
    if root.is_file():
        return [root] if root.suffix.lower() == ".md" else []

    markdown_files: list[Path] = []
    for current, directory_names, file_names in os.walk(root):
        current_path = Path(current)
        directory_names[:] = sorted(
            name
            for name in directory_names
            if name not in SKIPPED_DIRECTORY_NAMES
            and not (current_path / name / ".git").exists()
        )
        markdown_files.extend(
            current_path / name
            for name in sorted(file_names)
            if Path(name).suffix.lower() == ".md"
        )
    return markdown_files


def iter_content_lines(path: Path) -> list[tuple[int, str]]:
    """Return non-fenced-code Markdown lines with original line numbers."""
    lines: list[tuple[int, str]] = []
    fence: tuple[str, int] | None = None
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        fence_match = FENCE_RE.match(line)
        if fence_match:
            marker = fence_match.group(1)
            marker_char = marker[0]
            marker_len = len(marker)
            if fence is None:
                fence = (marker_char, marker_len)
            elif marker_char == fence[0] and marker_len >= fence[1]:
                fence = None
            continue
        if fence is None:
            lines.append((line_number, line))
    return lines


def iter_inline_link_destinations(line: str) -> list[str]:
    """Extract inline Markdown link/image destinations from one line."""
    line = mask_inline_code_spans(line)
    destinations: list[str] = []
    cursor = 0
    while cursor < len(line):
        open_bracket = line.find("[", cursor)
        if open_bracket == -1:
            break
        close_bracket = line.find("]", open_bracket + 1)
        if close_bracket == -1:
            break
        if close_bracket + 1 >= len(line) or line[close_bracket + 1] != "(":
            cursor = open_bracket + 1
            continue

        start = close_bracket + 2
        depth = 1
        pos = start
        escaped = False
        while pos < len(line):
            char = line[pos]
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == "(":
                depth += 1
            elif char == ")":
                depth -= 1
                if depth == 0:
                    destinations.append(line[start:pos])
                    break
            pos += 1
        cursor = pos + 1
    return destinations


def mask_inline_code_spans(line: str) -> str:
    """Replace inline-code contents with spaces while preserving positions."""
    chars = list(line)
    cursor = 0
    while cursor < len(chars):
        if chars[cursor] != "`":
            cursor += 1
            continue

        marker_len = 1
        while cursor + marker_len < len(chars) and chars[cursor + marker_len] == "`":
            marker_len += 1
        close = line.find("`" * marker_len, cursor + marker_len)
        if close == -1:
            break
        for index in range(cursor, close + marker_len):
            chars[index] = " "
        cursor = close + marker_len
    return "".join(chars)


def normalize_destination(raw_destination: str) -> str:
    """Strip Markdown destination wrappers and titles, preserving the target."""
    destination = raw_destination.strip()
    if not destination:
        return ""
    if destination.startswith("<"):
        end = destination.find(">")
        if end != -1:
            return destination[1:end].strip()
    return destination.split(None, 1)[0]


def is_ignored_destination(destination: str) -> bool:
    lower = destination.lower()
    return (
        not destination
        or destination.startswith("#")
        or lower.startswith("mailto:")
        or lower.startswith("//")
        or bool(SCHEME_RE.match(destination))
    )


def resolve_destination(
    source: Path,
    destination: str,
    *,
    repo_root: Path = REPO_ROOT,
) -> Path | None:
    if is_ignored_destination(destination):
        return None
    path_part = destination.split("#", 1)[0].split("?", 1)[0]
    if not path_part:
        return None
    decoded = unquote(path_part)
    if decoded.startswith("/"):
        return repo_root / decoded.lstrip("/")
    candidate = Path(decoded)
    if not candidate.is_absolute():
        candidate = source.parent / candidate
    return candidate


def check_file(path: Path, *, repo_root: Path = REPO_ROOT) -> list[MissingLink]:
    missing: list[MissingLink] = []
    for line_number, line in iter_content_lines(path):
        for raw_destination in iter_inline_link_destinations(line):
            destination = normalize_destination(raw_destination)
            resolved = resolve_destination(path, destination, repo_root=repo_root)
            if resolved is not None and not resolved.exists():
                missing.append(
                    MissingLink(
                        source=path,
                        line=line_number,
                        target=destination,
                        resolved=resolved,
                    )
                )
    return missing


def check_roots(
    roots: list[Path],
    *,
    repo_root: Path = REPO_ROOT,
) -> list[MissingLink]:
    missing: list[MissingLink] = []
    for root in roots:
        for path in iter_markdown_files(root):
            missing.extend(check_file(path, repo_root=repo_root))
    return missing


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Check local Markdown link and image targets under roots."
    )
    parser.add_argument(
        "roots",
        nargs="+",
        type=Path,
        help="Markdown file or directory roots to scan; missing roots are skipped.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    missing = check_roots(args.roots)
    if not missing:
        print("markdown link target check passed")
        return 0

    for item in missing:
        print(f"{item.source}:{item.line}: missing target {item.target} -> {item.resolved}")
    print(f"markdown link target check failed: {len(missing)} missing target(s)")
    return 1


if __name__ == "__main__":
    sys.exit(main())
