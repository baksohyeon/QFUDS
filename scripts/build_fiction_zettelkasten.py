#!/usr/bin/env python3
"""Build a source-linked SOURCE INDEX for a fiction tree.

This tool does NOT produce a Zettelkasten. It produces a mechanical
source/heading INDEX:

- original fiction documents remain the source layer;
- each H1-H6 heading becomes an index card that captures a bounded excerpt
  of the text beneath it plus a provenance back-link to the source;
- template-conformant atomic zettels are skipped (they are already permanent
  notes; carding their section headings would only shred them);
- authors distill index cards into real atomic zettels by hand later.

Reserve the words "zettel" / "제텔카스텐" for hand-authored atomic notes.
The layer generated here is a source index only.

Usage:
    python3 scripts/build_fiction_zettelkasten.py \
        --source docs/wiki/fiction \
        --output fiction_zettelkasten_wip \
        [--dry-run] [--allow-ssot]

By default the generator refuses to write inside the SSOT (docs/wiki/fiction);
pass --allow-ssot only if you really mean to write into canon.
"""

from __future__ import annotations

import argparse
import hashlib
import re
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SSOT_FICTION = ROOT / "docs/wiki/fiction"
DEFAULT_SOURCE = SSOT_FICTION
DEFAULT_OUTPUT = ROOT / "fiction_zettelkasten_wip"

MAX_HEADING_LEVEL = 6
DOC_ID_HEX = 16          # 64-bit doc_id digest; collision-safe as the queue scales
FILENAME_HEX = 6         # short digest for filenames (line_no prefix keeps paths unique)
PROVENANCE_EPOCH = "2026-01-01"  # deterministic fallback when a source has no last_updated
EXCERPT_MAX_LINES = 40
EXCERPT_MAX_CHARS = 1600

# Roots resolved from CLI args inside main(); see resolve_roots().
SOURCE_ROOT = DEFAULT_SOURCE
OUTPUT_ROOT = DEFAULT_OUTPUT
ZK_ROOT = DEFAULT_OUTPUT / "02_zettelkasten"
CARD_ROOT = ZK_ROOT / "90_source_queue/cards"
SOURCE_MAP_ROOT = ZK_ROOT / "90_source_queue/sources"
INDEX_PATH = ZK_ROOT / "000_source_index_ko.md"
QUEUE_PATH = ZK_ROOT / "90_source_queue/000_queue_index_ko.md"


@dataclass(frozen=True)
class Heading:
    source: Path
    source_doc_id: str
    source_title: str
    source_updated: str
    level: int
    title: str
    line: int
    parent_h1: str
    parent_h2: str
    excerpt: str
    card_id: str
    card_path: Path


def yaml_quote(value: str) -> str:
    # Always emit a double-quoted scalar with escaping so titles containing
    # ':' or ' #' (inline-comment vectors) cannot mis-parse as YAML.
    value = value.replace("\n", " ")
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def markdown_link_label(value: str) -> str:
    value = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", value)
    return value.replace("|", "\\|").replace("[", "(").replace("]", ")")


def title_text(value: str) -> str:
    value = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", value)
    return value.replace("|", "/")


def slug_ascii(value: str, fallback: str = "item") -> str:
    # Keep Hangul in the slug (filesystems and git handle UTF-8 fine); only
    # fall back when nothing usable remains.
    value = value.lower()
    value = re.sub(r"[^a-z0-9가-힣]+", "-", value).strip("-")
    if not value:
        return fallback
    return value[:80].strip("-") or fallback


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}
    result: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" not in line or line.startswith(" "):
            continue
        key, raw = line.split(":", 1)
        raw = raw.strip().strip('"')
        result[key.strip()] = raw
    return result


def is_atomic_zettel(text: str, meta: dict[str, str]) -> bool:
    # A template-conformant permanent zettel: already one atomic note. Carding
    # its section headings (Statement / Links / Use Guard ...) would shred it.
    return (
        meta.get("doc_type") == "reference"
        and "## Statement" in text
        and "## Use Guard" in text
    )


def iter_source_files() -> list[Path]:
    files = []
    for path in SOURCE_ROOT.rglob("*.md"):
        if ZK_ROOT == path or ZK_ROOT in path.parents:
            continue
        if OUTPUT_ROOT in path.parents:
            continue
        files.append(path)
    return sorted(files)


def source_hash(path: Path) -> str:
    rel = path.relative_to(ROOT).as_posix()
    return hashlib.sha1(rel.encode("utf-8")).hexdigest()[:10]


def card_hash(path: Path, line: int, title: str) -> str:
    raw = f"{path.relative_to(ROOT).as_posix()}:{line}:{title}"
    return hashlib.sha1(raw.encode("utf-8")).hexdigest()[:DOC_ID_HEX]


def rel_from(target: Path, anchor_file: Path) -> str:
    # Relative POSIX path from anchor_file's directory to target, depth derived
    # from the anchor's ACTUAL location (relative to ROOT) — never hardcoded.
    depth = len(anchor_file.relative_to(ROOT).parent.parts)
    return (Path(*([".."] * depth)) / target.relative_to(ROOT)).as_posix()


def make_excerpt(lines: list[str], start_line: int, next_heading_line: int | None) -> str:
    # Capture the source text under a heading, up to the next heading of ANY
    # level (tight, non-overlapping), then bound by lines and characters.
    end = (next_heading_line - 1) if next_heading_line else len(lines)
    body = [ln for ln in lines[start_line:end]]
    # trim leading/trailing blank lines
    while body and not body[0].strip():
        body.pop(0)
    while body and not body[-1].strip():
        body.pop()
    truncated = False
    if len(body) > EXCERPT_MAX_LINES:
        body = body[:EXCERPT_MAX_LINES]
        truncated = True
    text = "\n".join(body)
    if len(text) > EXCERPT_MAX_CHARS:
        text = text[:EXCERPT_MAX_CHARS].rstrip()
        truncated = True
    if not text.strip():
        return "_(no text under this heading; navigation or section header only)_"
    # Blockquote each line so source fences/`---` cannot break the card markdown.
    quoted = "\n".join("> " + ln if ln.strip() else ">" for ln in text.splitlines())
    if truncated:
        quoted += "\n>\n> _(excerpt truncated — open the source for the full text)_"
    return quoted


def collect_headings() -> list[Heading]:
    headings: list[Heading] = []
    for source in iter_source_files():
        text = source.read_text(encoding="utf-8", errors="ignore")
        meta = parse_frontmatter(text)
        source_doc_id = meta.get("doc_id") or f"source_{source_hash(source)}"
        source_title = meta.get("title") or source.stem
        source_updated = meta.get("last_updated") or PROVENANCE_EPOCH
        lines = text.splitlines()
        atomic = is_atomic_zettel(text, meta)
        source_slug = f"{source_hash(source)}_{slug_ascii(source.stem)}"

        # Pre-scan heading positions so excerpts can stop at the next heading.
        raw_headings = []
        for line_no, line in enumerate(lines, 1):
            m = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
            if m:
                raw_headings.append((line_no, len(m.group(1)), m.group(2).strip()))

        current_h1 = ""
        current_h2 = ""
        for idx, (line_no, level, title) in enumerate(raw_headings):
            if level == 1:
                current_h1 = title
                current_h2 = ""
            elif level == 2:
                current_h2 = title
            if level > MAX_HEADING_LEVEL:
                continue
            # Already-atomic zettels: emit only ONE card (the H1), never shred.
            if atomic and level != 1:
                continue
            next_line = raw_headings[idx + 1][0] if idx + 1 < len(raw_headings) else None
            excerpt = make_excerpt(lines, line_no, next_line)
            digest = card_hash(source, line_no, title)
            card_id = f"srcidx_{digest}"
            heading_slug = slug_ascii(title, "heading")
            card_path = CARD_ROOT / source_slug / f"{line_no:04d}_{heading_slug}_{digest[:FILENAME_HEX]}.md"
            headings.append(
                Heading(
                    source=source,
                    source_doc_id=source_doc_id,
                    source_title=source_title,
                    source_updated=source_updated,
                    level=level,
                    title=title,
                    line=line_no,
                    parent_h1=current_h1,
                    parent_h2=current_h2,
                    excerpt=excerpt,
                    card_id=card_id,
                    card_path=card_path,
                )
            )
    return headings


def write_card(heading: Heading) -> None:
    rel_source_text = rel_from(heading.source, heading.card_path)
    parent_bits = []
    if heading.parent_h1 and heading.parent_h1 != heading.title:
        parent_bits.append(f"- H1: {heading.parent_h1}")
    if heading.parent_h2 and heading.parent_h2 != heading.title:
        parent_bits.append(f"- H2: {heading.parent_h2}")
    parent_text = "\n".join(parent_bits) if parent_bits else "- none"
    title = f"Source Index - {title_text(heading.title)}"
    body = f"""---
doc_id: {heading.card_id}
title: {yaml_quote(title)}
doc_type: reference
stage: reference
status: draft
evidence_role: provenance
depends_on:
  - {heading.source_doc_id}
next_gate: distill this source-index card into an atomic permanent zettel, or mark it source-only
last_updated: {heading.source_updated}
---

# {title}

```text
fiction/provenance only
research evidence: no
canon action: none
layer: source index (not a permanent zettel)
processing_state: queued
```

## Source

- Source document: [{heading.source_title}]({rel_source_text})
- Source path: [{heading.source.relative_to(ROOT).as_posix()}]({rel_source_text})
- Source line: [line {heading.line}]({rel_source_text})
- Heading level: `H{heading.level}`
- Source heading: `{heading.title}`

## Parent Context

{parent_text}

## Captured Source

{heading.excerpt}

## Processing Contract

This is a generated source-index card, not a permanent zettel.

To distill it:

1. Reopen the source document for the full context.
2. Extract one atomic claim, rule, tension, or open question.
3. Mark canon state explicitly as `canon`, `candidate`, `soft_canon`, `archive`, or `unknown`.
4. Link the distilled zettel back to this card and to related zettels.
5. If the source heading is only navigation or boilerplate, mark it `source-only` instead of inventing a note.
"""
    heading.card_path.parent.mkdir(parents=True, exist_ok=True)
    heading.card_path.write_text(body, encoding="utf-8")


def write_source_map(source: Path, headings: list[Heading]) -> Path:
    text = source.read_text(encoding="utf-8", errors="ignore")
    meta = parse_frontmatter(text)
    source_doc_id = meta.get("doc_id") or f"source_{source_hash(source)}"
    source_title = meta.get("title") or source.stem
    source_updated = meta.get("last_updated") or PROVENANCE_EPOCH
    map_id = f"srcidx_source_{source_hash(source)}"
    title = f"Source Map - {title_text(source_title)}"
    source_slug = f"{source_hash(source)}_{slug_ascii(source.stem)}"
    map_path = SOURCE_MAP_ROOT / f"{source_slug}.md"
    rel_source = rel_from(source, map_path)
    rows = []
    for h in headings:
        rel_card = Path("../cards") / h.card_path.parent.name / h.card_path.name
        rows.append(
            f"| H{h.level} | `{h.line}` | [{markdown_link_label(h.title)}]({rel_card.as_posix()}) | queued |"
        )
    rows_text = "\n".join(rows) if rows else "| - | - | - | - |"
    body = f"""---
doc_id: {map_id}
title: {yaml_quote(title)}
doc_type: index
stage: reference
status: draft
evidence_role: provenance
depends_on:
  - {source_doc_id}
next_gate: distill queued headings into permanent zettels or mark source-only
last_updated: {source_updated}
---

# {title}

```text
fiction/provenance only
research evidence: no
canon action: source map only
layer: source index (not a permanent zettel)
```

## Source

- Source document: [{source_title}]({rel_source})
- Source path: [{source.relative_to(ROOT).as_posix()}]({rel_source})
- Index cards: `{len(headings)}`

## Heading Index

| Level | Line | Index Card | State |
| --- | ---: | --- | --- |
{rows_text}
"""
    map_path.parent.mkdir(parents=True, exist_ok=True)
    map_path.write_text(body, encoding="utf-8")
    return map_path


def write_indexes(headings: list[Heading], source_maps: list[Path]) -> None:
    by_source: dict[Path, int] = {}
    for h in headings:
        by_source[h.source] = by_source.get(h.source, 0) + 1
    latest = max((h.source_updated for h in headings), default=PROVENANCE_EPOCH)
    source_rows = []
    for source_map in sorted(source_maps):
        rel = source_map.relative_to(QUEUE_PATH.parent).as_posix()
        source_rows.append(f"| [{source_map.stem}]({rel}) | queued |")
    source_rows_text = "\n".join(source_rows)
    index_body = f"""---
doc_id: qfuds_fiction_source_index_ko
title: QFUDS Fiction Source Index
doc_type: index
stage: reference
status: draft
evidence_role: provenance
depends_on:
  - wiki_fiction_index
next_gate: distill source-index cards into permanent zettels without deleting source documents
last_updated: {latest}
---

# QFUDS Fiction Source Index

```text
fiction/provenance only
research evidence: no
layer: source index (not a Zettelkasten; reserve "zettel" for hand-authored atomic notes)
canon action: migration operating layer
```

## 목적

이 선반은 소스 문서(`{SOURCE_ROOT.relative_to(ROOT).as_posix()}`)를 heading 단위로 색인한
**소스 인덱스**다. 제텔카스텐이 아니다 — 카드는 원자적 아이디어가 아니라 heading별 발췌·역링크다.
원문 문서는 삭제하지 않고 source layer로 보존하며, 작가가 카드를 하나씩 permanent zettel로
증류한다. 이미 원자적인 zettel(템플릿 준수)은 색인 대상에서 제외한다.

## 현재 생성 상태

| 항목 | 수 |
| --- | ---: |
| source markdown files | {len(by_source)} |
| H1-H6 index cards | {len(headings)} |
| source maps | {len(source_maps)} |

## 선반

| 경로 | 역할 |
| --- | --- |
| [90_source_queue/000_queue_index_ko.md](90_source_queue/000_queue_index_ko.md) | 전체 source map 진입점 |
| `90_source_queue/sources/` | 원문 파일별 heading 색인 |
| `90_source_queue/cards/` | heading 단위 색인 카드 |

## 처리 원칙

- 색인 카드는 permanent zettel이 아니다. "zettel" 명칭은 수기 원자 노트에만 쓴다.
- 원문을 대체하거나 삭제하지 않는다.
- canon/candidate/unknown은 처리자가 출처를 다시 확인한 뒤 표시한다.
- archive 문서도 provenance로 색인한다. active canon처럼 승격하지 않는다.
- boilerplate heading은 `source-only`로 표시하고 새 설정을 만들지 않는다.
"""
    INDEX_PATH.parent.mkdir(parents=True, exist_ok=True)
    INDEX_PATH.write_text(index_body, encoding="utf-8")

    queue_body = f"""---
doc_id: qfuds_fiction_source_queue_index_ko
title: QFUDS Fiction Source Queue
doc_type: index
stage: reference
status: draft
evidence_role: provenance
depends_on:
  - qfuds_fiction_source_index_ko
next_gate: choose a source map, distill cards one by one, then update the relevant MOC
last_updated: {latest}
---

# QFUDS Fiction Source Queue

```text
fiction/provenance only
research evidence: no
layer: source index (not a permanent zettel)
canon action: source queue only
```

## Source Maps

| Source Map | State |
| --- | --- |
{source_rows_text}
"""
    QUEUE_PATH.parent.mkdir(parents=True, exist_ok=True)
    QUEUE_PATH.write_text(queue_body, encoding="utf-8")


def resolve_roots(source: Path, output: Path) -> None:
    global SOURCE_ROOT, OUTPUT_ROOT, ZK_ROOT, CARD_ROOT, SOURCE_MAP_ROOT, INDEX_PATH, QUEUE_PATH
    SOURCE_ROOT = source.resolve()
    OUTPUT_ROOT = output.resolve()
    ZK_ROOT = OUTPUT_ROOT / "02_zettelkasten"
    CARD_ROOT = ZK_ROOT / "90_source_queue/cards"
    SOURCE_MAP_ROOT = ZK_ROOT / "90_source_queue/sources"
    INDEX_PATH = ZK_ROOT / "000_source_index_ko.md"
    QUEUE_PATH = ZK_ROOT / "90_source_queue/000_queue_index_ko.md"


def parse_args(argv: list[str] | None) -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Build a source index for a fiction tree.")
    p.add_argument("--source", type=Path, default=DEFAULT_SOURCE, help="source fiction tree (default: docs/wiki/fiction)")
    p.add_argument("--output", type=Path, default=DEFAULT_OUTPUT, help="output root, NON-SSOT (default: fiction_zettelkasten_wip)")
    p.add_argument("--dry-run", action="store_true", help="report planned deletes/writes and exit without touching disk")
    p.add_argument("--allow-ssot", action="store_true", help="permit writing inside docs/wiki/fiction (dangerous; off by default)")
    return p.parse_args(argv)


def guard_ssot(allow_ssot: bool) -> None:
    # Writing anywhere at or under the SSOT fiction root is refused by default.
    inside_ssot = (
        ZK_ROOT == SSOT_FICTION
        or SSOT_FICTION in ZK_ROOT.parents
        or OUTPUT_ROOT == SSOT_FICTION
        or SSOT_FICTION in OUTPUT_ROOT.parents
    )
    if inside_ssot and not allow_ssot:
        raise SystemExit(
            "refusing to write into the SSOT (docs/wiki/fiction). "
            "Pass --output to a non-SSOT dir, or --allow-ssot to override."
        )


def clean_owned(dry_run: bool) -> None:
    # Only remove generator-owned outputs — never rmtree a shared/SSOT root.
    for owned in (CARD_ROOT, SOURCE_MAP_ROOT):
        if owned.exists():
            print(f"{'would remove' if dry_run else 'removing'} dir {owned.relative_to(ROOT)}")
            if not dry_run:
                shutil.rmtree(owned)
    for owned_file in (INDEX_PATH, QUEUE_PATH):
        if owned_file.exists():
            print(f"{'would remove' if dry_run else 'removing'} file {owned_file.relative_to(ROOT)}")
            if not dry_run:
                owned_file.unlink()


def main(argv: list[str] | None = None) -> None:
    args = parse_args(argv)
    resolve_roots(args.source, args.output)
    guard_ssot(args.allow_ssot)

    headings = collect_headings()
    # Fail loudly on any card-path or doc_id collision instead of overwriting.
    seen_paths: set[Path] = set()
    seen_ids: set[str] = set()
    for h in headings:
        if h.card_path in seen_paths:
            raise SystemExit(f"card path collision: {h.card_path}")
        seen_paths.add(h.card_path)
        if h.card_id in seen_ids:
            raise SystemExit(f"doc_id collision: {h.card_id}")
        seen_ids.add(h.card_id)

    by_source: dict[Path, list[Heading]] = {}
    for heading in headings:
        by_source.setdefault(heading.source, []).append(heading)

    if args.dry_run:
        clean_owned(dry_run=True)
        print(
            f"dry-run: would write {len(headings)} index cards from {len(by_source)} "
            f"source files into {ZK_ROOT.relative_to(ROOT)}"
        )
        return

    clean_owned(dry_run=False)
    for heading in headings:
        write_card(heading)
    source_maps = [write_source_map(source, items) for source, items in sorted(by_source.items())]
    write_indexes(headings, source_maps)
    print(
        f"wrote {len(headings)} index cards from {len(source_maps)} source files "
        f"into {ZK_ROOT.relative_to(ROOT)}"
    )


if __name__ == "__main__":
    main(sys.argv[1:])
