#!/usr/bin/env python3
"""Build a source-linked Zettelkasten queue for docs/wiki/fiction.

The generated queue is intentionally conservative:
- original fiction documents remain the source layer;
- each H1-H6 heading becomes a queue card;
- queue cards do not canonize, summarize, or rewrite the source;
- authors process cards one by one into permanent notes later.
"""

from __future__ import annotations

import hashlib
import re
import shutil
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parents[1]
FICTION_ROOT = ROOT / "docs/wiki/fiction"
ZK_ROOT = FICTION_ROOT / "02_zettelkasten"
CARD_ROOT = ZK_ROOT / "90_source_queue/cards"
SOURCE_MAP_ROOT = ZK_ROOT / "90_source_queue/sources"
INDEX_PATH = ZK_ROOT / "000_zettelkasten_system_index_ko.md"
QUEUE_PATH = ZK_ROOT / "90_source_queue/000_queue_index_ko.md"
MAX_HEADING_LEVEL = 6
TODAY = datetime.now(ZoneInfo("Asia/Seoul")).date().isoformat()


@dataclass(frozen=True)
class Heading:
    source: Path
    source_doc_id: str
    source_title: str
    level: int
    title: str
    line: int
    parent_h1: str
    parent_h2: str
    card_id: str
    card_path: Path


def yaml_quote(value: str) -> str:
    # validate_docs.py compares this line-oriented value directly to H1 text.
    value = value.replace("\n", " ")
    if ":" in value:
        return f'"{value}"'
    return value


def stable_title(value: str, suffix: str) -> str:
    # validate_docs.py strips trailing double quotes from frontmatter values.
    if value.endswith('"'):
        return f"{value} ({suffix})"
    return value


def markdown_link_label(value: str) -> str:
    value = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", value)
    return value.replace("|", "\\|").replace("[", "(").replace("]", ")")


def title_text(value: str) -> str:
    value = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", value)
    return value.replace("|", "/")


def slug_ascii(value: str, fallback: str = "item") -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9가-힣]+", "-", value).strip("-")
    if not value:
        return fallback
    if re.search(r"[가-힣]", value):
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


def iter_source_files() -> list[Path]:
    files = []
    for path in FICTION_ROOT.rglob("*.md"):
        if ZK_ROOT in path.parents:
            continue
        files.append(path)
    return sorted(files)


def source_hash(path: Path) -> str:
    rel = path.relative_to(ROOT).as_posix()
    return hashlib.sha1(rel.encode("utf-8")).hexdigest()[:10]


def card_hash(path: Path, line: int, title: str) -> str:
    raw = f"{path.relative_to(ROOT).as_posix()}:{line}:{title}"
    return hashlib.sha1(raw.encode("utf-8")).hexdigest()[:12]


def collect_headings() -> list[Heading]:
    headings: list[Heading] = []
    for source in iter_source_files():
        text = source.read_text(encoding="utf-8", errors="ignore")
        meta = parse_frontmatter(text)
        source_doc_id = meta.get("doc_id") or f"source_{source_hash(source)}"
        source_title = meta.get("title") or source.stem
        current_h1 = ""
        current_h2 = ""
        source_slug = f"{source_hash(source)}_{slug_ascii(source.stem)}"
        for line_no, line in enumerate(text.splitlines(), 1):
            match = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
            if not match:
                continue
            level = len(match.group(1))
            title = match.group(2).strip()
            if level == 1:
                current_h1 = title
                current_h2 = ""
            elif level == 2:
                current_h2 = title
            if level > MAX_HEADING_LEVEL:
                continue
            digest = card_hash(source, line_no, title)
            card_id = f"zkqv_{digest}"
            heading_slug = slug_ascii(title, "heading")
            card_path = CARD_ROOT / source_slug / f"{line_no:04d}_{heading_slug}_{digest[:6]}.md"
            headings.append(
                Heading(
                    source=source,
                    source_doc_id=source_doc_id,
                    source_title=source_title,
                    level=level,
                    title=title,
                    line=line_no,
                    parent_h1=current_h1,
                    parent_h2=current_h2,
                    card_id=card_id,
                    card_path=card_path,
                )
            )
    return headings


def write_card(heading: Heading) -> None:
    rel_source = Path(
        Path("../../../../..")
    )
    rel_source = Path(
        Path(
            Path(*([".."] * len(heading.card_path.relative_to(ROOT).parent.parts)))
        )
        / heading.source.relative_to(ROOT)
    )
    rel_source_text = rel_source.as_posix()
    parent_bits = []
    if heading.parent_h1 and heading.parent_h1 != heading.title:
        parent_bits.append(f"- H1: {heading.parent_h1}")
    if heading.parent_h2 and heading.parent_h2 != heading.title:
        parent_bits.append(f"- H2: {heading.parent_h2}")
    parent_text = "\n".join(parent_bits) if parent_bits else "- none"
    title = stable_title(f"ZK Queue - {title_text(heading.title)}", "queue")
    body = f"""---
doc_id: {heading.card_id}
title: {yaml_quote(title)}
doc_type: reference
stage: reference
status: draft
evidence_role: provenance
depends_on:
  - {heading.source_doc_id}
next_gate: process this queue card into an atomic permanent zettel or mark it as source-only
last_updated: {TODAY}
---

# {title}

```text
fiction/provenance only
research evidence: no
canon action: none
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

## Processing Contract

This is a generated queue card. Do not treat it as a permanent zettel yet.

To process it:

1. Reopen the source document.
2. Extract one atomic claim, rule, tension, or open question.
3. Mark canon state explicitly as `canon`, `candidate`, `soft_canon`, `archive`, or `unknown`.
4. Link the processed note back to this queue card and the source document.
5. If the source is only navigation or boilerplate, mark it `source-only` instead of inventing a note.
"""
    heading.card_path.parent.mkdir(parents=True, exist_ok=True)
    heading.card_path.write_text(body, encoding="utf-8")


def write_source_map(source: Path, headings: list[Heading]) -> Path:
    text = source.read_text(encoding="utf-8", errors="ignore")
    meta = parse_frontmatter(text)
    source_doc_id = meta.get("doc_id") or f"source_{source_hash(source)}"
    source_title = meta.get("title") or source.stem
    map_id = f"zkqv_source_{source_hash(source)}"
    title = stable_title(f"ZK Source Map - {title_text(source_title)}", "source map")
    source_slug = f"{source_hash(source)}_{slug_ascii(source.stem)}"
    map_path = SOURCE_MAP_ROOT / f"{source_slug}.md"
    rel_source = Path(
        Path(*([".."] * len(map_path.relative_to(ROOT).parent.parts)))
        / source.relative_to(ROOT)
    ).as_posix()
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
next_gate: process queued headings into permanent zettels or mark source-only
last_updated: {TODAY}
---

# {title}

```text
fiction/provenance only
research evidence: no
canon action: source map only
```

## Source

- Source document: [{source_title}]({rel_source})
- Source path: [{source.relative_to(ROOT).as_posix()}]({rel_source})
- Queue cards: `{len(headings)}`

## Heading Queue

| Level | Line | Queue Card | State |
| --- | ---: | --- | --- |
{rows_text}
"""
    map_path.parent.mkdir(parents=True, exist_ok=True)
    map_path.write_text(body, encoding="utf-8")
    return map_path


def write_indexes(headings: list[Heading], source_maps: list[Path]) -> None:
    source_rows = []
    by_source: dict[Path, int] = {}
    for h in headings:
        by_source[h.source] = by_source.get(h.source, 0) + 1
    for source_map in sorted(source_maps):
        rel = source_map.relative_to(QUEUE_PATH.parent).as_posix()
        source_rows.append(f"| [{source_map.stem}]({rel}) | queued |")
    source_rows_text = "\n".join(source_rows)
    index_body = f"""---
doc_id: qfuds_fiction_zettelkasten_system_index_ko
title: QFUDS Fiction 제텔카스텐 시스템 인덱스
doc_type: index
stage: reference
status: draft
evidence_role: provenance
depends_on:
  - wiki_fiction_index
next_gate: process queue cards into permanent zettels without deleting source documents
last_updated: {TODAY}
---

# QFUDS Fiction 제텔카스텐 시스템 인덱스

```text
fiction/provenance only
research evidence: no
canon action: migration operating layer
```

## 목적

이 선반은 `docs/wiki/fiction/` 전체를 제텔카스텐 방식으로 처리하기 위한 운영 층이다.
원문 문서는 삭제하지 않고 source layer로 보존한다. 모든 H1-H6 heading은 queue card로
분해되며, 작가나 에이전트가 하나씩 permanent zettel로 처리한다.

## 현재 생성 상태

| 항목 | 수 |
| --- | ---: |
| source markdown files | {len(by_source)} |
| H1-H6 queue cards | {len(headings)} |
| source maps | {len(source_maps)} |

## 선반

| 경로 | 역할 |
| --- | --- |
| [90_source_queue/000_queue_index_ko.md](90_source_queue/000_queue_index_ko.md) | 전체 source map 진입점 |
| `90_source_queue/sources/` | 원문 파일별 heading queue |
| `90_source_queue/cards/` | heading 단위 처리 대기 카드 |

## 처리 원칙

- queue card는 permanent zettel이 아니다.
- 원문을 대체하거나 삭제하지 않는다.
- canon/candidate/unknown은 처리자가 출처를 다시 확인한 뒤 표시한다.
- archive 문서도 provenance로 queue화한다. active canon처럼 승격하지 않는다.
- boilerplate heading은 `source-only`로 표시하고 새 설정을 만들지 않는다.
"""
    INDEX_PATH.parent.mkdir(parents=True, exist_ok=True)
    INDEX_PATH.write_text(index_body, encoding="utf-8")

    queue_body = f"""---
doc_id: qfuds_fiction_zettelkasten_source_queue_index_ko
title: QFUDS Fiction 제텔카스텐 Source Queue
doc_type: index
stage: reference
status: draft
evidence_role: provenance
depends_on:
  - qfuds_fiction_zettelkasten_system_index_ko
next_gate: choose a source map, process cards one by one, then update the relevant MOC
last_updated: {TODAY}
---

# QFUDS Fiction 제텔카스텐 Source Queue

```text
fiction/provenance only
research evidence: no
canon action: source queue only
```

## Source Maps

| Source Map | State |
| --- | --- |
{source_rows_text}
"""
    QUEUE_PATH.parent.mkdir(parents=True, exist_ok=True)
    QUEUE_PATH.write_text(queue_body, encoding="utf-8")


def main() -> None:
    if ZK_ROOT.exists():
        shutil.rmtree(ZK_ROOT)
    headings = collect_headings()
    for heading in headings:
        write_card(heading)
    by_source: dict[Path, list[Heading]] = {}
    for heading in headings:
        by_source.setdefault(heading.source, []).append(heading)
    source_maps = [write_source_map(source, items) for source, items in sorted(by_source.items())]
    write_indexes(headings, source_maps)
    print(f"wrote {len(headings)} queue cards from {len(source_maps)} source files into {ZK_ROOT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
