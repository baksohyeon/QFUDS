#!/usr/bin/env python3
"""Assemble every QFUDS SAGA doc into ONE readable encyclopedia page.

Motivation: the per-folder README maps are hand-maintained and drift. This
generator reads the frontmatter of every SAGA doc and emits a single
scroll-top-to-bottom digest so the author can see the whole project in one
file. Re-run it whenever docs change; it never goes stale by hand.

Stack: Python standard library only (re, pathlib, datetime).

Usage:
    python3 scripts/build_saga_digest.py

Read-only over the docs tree except for the one generated output file.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SAGA = ROOT / "docs/wiki/fiction/10_universes/qfuds-verse/20_series/qfuds-saga"
OUT = SAGA / "000_saga_encyclopedia_ko.md"

DOC_ID = "qfuds_saga_encyclopedia_ko"
TITLE = "QFUDS SAGA 백과사전 (자동 생성 · 한 장 요약)"
SUMMARY_MAX = 280

# A doc self-declaring pre-reboot / pre-recenter labels via a drift banner.
# Flag it so the digest never presents its stale body as current.
STALE_MARKERS = ("드리프트 주의", "리센터 이전", "리부트 이전", "reboot 이전")
STALE_NOTE = (
    "**주의 — 리센터 이전 라벨 포함:** 이 문서 본문은 옛 부 번호를 담을 수 있다. "
    "현행 매핑은 024·025·027 SSOT가 우선."
)

# Shelf order + human role. Drives section ordering top-to-bottom.
SHELVES: list[tuple[str, str]] = [
    ("20_drafts", "실제 원고 (부/arc별). 지금 읽고 고치는 소설"),
    ("10_story_design", "아이디어·아웃라인·arc 지도·씬카드 (확정 전 설계)"),
    ("00_bible", "확정된 세계 사실·인물·제도·과학 경계 (설정 기준서)"),
    ("30_revisions", "출간용 교정·게이트 기록"),
    ("00_workroom", "운영 규칙·GSD brief·오늘 작업 상태판"),
    ("40_release", "출간 후보·내보내기 (게이트 통과 후)"),
]


def parse_frontmatter(path: Path) -> tuple[dict[str, str], str]:
    """Return (frontmatter dict, body). Mirrors build_doc_graph conventions."""
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.S)
    if not m:
        return {}, text
    fm: dict[str, str] = {}
    for line in m.group(1).splitlines():
        mm = re.match(r"^([a-z_]+):\s*(.*)$", line)
        if mm and mm.group(2).strip():
            fm[mm.group(1)] = mm.group(2).strip()
    return fm, m.group(2)


def first_summary(body: str) -> str:
    """First real prose paragraph after the H1, skipping headings/quotes/tables."""
    lines = body.splitlines()
    buf: list[str] = []
    for line in lines:
        s = line.strip()
        if not s:
            if buf:
                break
            continue
        if s[0] in "#>|`-*=" or s.startswith("```"):
            if buf:
                break
            continue
        buf.append(s)
    para = " ".join(buf)
    para = re.sub(r"\s+", " ", para).strip()
    if len(para) > SUMMARY_MAX:
        para = para[:SUMMARY_MAX].rstrip() + "…"
    return para


def rel_from_saga(path: Path) -> str:
    return path.relative_to(SAGA).as_posix()


def sort_key(path: Path) -> tuple:
    """Sort by numeric filename prefix, then folder, then name."""
    name = path.name
    m = re.match(r"^(\d+)", name)
    num = int(m.group(1)) if m else 9999
    return (rel_from_saga(path.parent), num, name)


def shelf_of(rel: str) -> str | None:
    for shelf, _role in SHELVES:
        if rel == shelf or rel.startswith(shelf + "/"):
            return shelf
    return None


def collect() -> dict[str, list[dict]]:
    """Return shelf -> list of doc records (excluding READMEs and self)."""
    by_shelf: dict[str, list[dict]] = {s: [] for s, _ in SHELVES}
    for path in sorted(SAGA.rglob("*.md"), key=sort_key):
        if path == OUT or path.name == "README.md":
            continue
        rel = rel_from_saga(path)
        shelf = shelf_of(rel)
        if shelf is None:
            continue
        fm, body = parse_frontmatter(path)
        by_shelf[shelf].append(
            {
                "rel": rel,
                "title": fm.get("title", path.stem),
                "status": fm.get("status", "?"),
                "last_updated": fm.get("last_updated", "?"),
                "next_gate": fm.get("next_gate", ""),
                "doc_type": fm.get("doc_type", ""),
                "summary": first_summary(body),
                "stale": any(mark in body for mark in STALE_MARKERS),
            }
        )
    return by_shelf


def newest_date(by_shelf: dict[str, list[dict]]) -> str:
    dates = [
        d["last_updated"]
        for docs in by_shelf.values()
        for d in docs
        if re.match(r"^\d{4}-\d{2}-\d{2}$", d["last_updated"])
    ]
    return max(dates) if dates else "2026-01-01"


def render(by_shelf: dict[str, list[dict]]) -> str:
    total = sum(len(v) for v in by_shelf.values())
    stamp = newest_date(by_shelf)
    all_docs = [d for docs in by_shelf.values() for d in docs]

    out: list[str] = []
    out.append("---")
    out.append(f"doc_id: {DOC_ID}")
    out.append(f"title: {TITLE}")
    out.append("doc_type: index")
    out.append("stage: reference")
    out.append("status: reference")
    out.append("evidence_role: reference")
    out.append("depends_on:")
    out.append("  - qfuds_saga_index_ko")
    out.append("  - qfuds_saga_drafts_index_ko")
    out.append("next_gate: 문서 변경 후 python3 scripts/build_saga_digest.py 재실행으로 갱신")
    out.append(f"last_updated: {stamp}")
    out.append("---")
    out.append("")
    out.append(f"# {TITLE}")
    out.append("")
    out.append(
        "> **자동 생성 파일.** 손으로 고치지 마세요. 원고·설계 문서가 바뀌면 "
        "`python3 scripts/build_saga_digest.py`를 다시 돌리면 이 한 장이 최신으로 갱신됩니다. "
        "이 페이지는 SAGA 전체를 위에서 아래로 쭉 읽는 백과사전이고, 실제 편집은 각 원본 문서에서 합니다."
    )
    out.append("")
    out.append(
        f"수록 문서 {total}개 · 최신 갱신 기준 {stamp} · "
        "완성/작성중 같은 판단은 "
        "[20_drafts 지도](20_drafts/README.md)가 최종 기준(SSOT)이다."
    )
    out.append("")
    stale_docs = [d for d in all_docs if d["stale"]]
    if stale_docs:
        links = " · ".join(f"[{d['title'].split('(')[0].strip()}]({d['rel']})" for d in stale_docs)
        out.append(
            f"**리센터 이전 라벨 포함 {len(stale_docs)}개** (본문에 옛 부 번호 잔존, "
            f"상단 SSOT 우선): {links}"
        )
        out.append("")

    # --- 선반 지도 ---
    out.append("## 1. 선반 지도 — 폴더가 곧 성숙 단계")
    out.append("")
    out.append("아이디어 → 설계 → 원고 → 교정 → 출간 순으로 익어간다.")
    out.append("")
    out.append("| 선반 | 역할 | 문서 수 |")
    out.append("| --- | --- | --- |")
    for shelf, role in SHELVES:
        out.append(f"| [`{shelf}`]({shelf}/) | {role} | {len(by_shelf[shelf])} |")
    out.append("")

    # --- 최근 갱신 ---
    dated = [d for d in all_docs if re.match(r"^\d{4}-\d{2}-\d{2}$", d["last_updated"])]
    recent = sorted(dated, key=lambda d: d["last_updated"], reverse=True)[:12]
    out.append("## 2. 최근 갱신 — 지금 뜨거운 곳")
    out.append("")
    out.append("가장 최근에 손댄 문서들. \"지금 뭘 작업 중인가\"의 데이터 기반 신호다.")
    out.append("")
    out.append("| 갱신일 | 문서 | 선반 |")
    out.append("| --- | --- | --- |")
    for d in recent:
        shelf = shelf_of(d["rel"]) or ""
        out.append(f"| {d['last_updated']} | [{d['title']}]({d['rel']}) | `{shelf}` |")
    out.append("")

    # --- 작업 큐 (next_gate) ---
    out.append("## 3. 작업 큐 — 각 문서의 다음 할 일 (next_gate)")
    out.append("")
    out.append(
        "각 문서가 스스로 적어둔 \"다음 관문\". 원고(20_drafts)와 설계(10_story_design)의 "
        "미완 항목이 곧 당신의 결정·집필 대기열이다. 버전 히스토리(`_versions/`)는 뺐다 — "
        "옛 판본 계보는 4절 전체 목록에서 볼 수 있다."
    )
    out.append("")
    for shelf in ("20_drafts", "10_story_design"):
        pending = [
            d for d in by_shelf[shelf]
            if d["next_gate"] and "/_versions/" not in d["rel"]
        ]
        if not pending:
            continue
        out.append(f"### {shelf}")
        out.append("")
        for d in pending:
            out.append(f"- **[{d['title']}]({d['rel']})** — {d['next_gate']}")
        out.append("")

    # --- 선반별 전체 문서 ---
    out.append("## 4. 전체 문서 — 선반별 요약")
    out.append("")
    out.append("각 문서의 한 문단 요약. 여기서 훑고, 자세히 볼 것만 링크로 연다.")
    out.append("")
    for shelf, role in SHELVES:
        docs = by_shelf[shelf]
        out.append(f"### `{shelf}` — {role}")
        out.append("")
        if not docs:
            out.append("_(문서 없음)_")
            out.append("")
            continue
        for d in docs:
            out.append(f"#### [{d['title']}]({d['rel']})")
            meta = f"`{d['status']}` · {d['last_updated']}"
            if d["doc_type"]:
                meta += f" · {d['doc_type']}"
            out.append(meta)
            out.append("")
            if d["stale"]:
                out.append(STALE_NOTE)
                out.append("")
            if d["summary"]:
                out.append(f"> {d['summary']}")
                out.append("")
            if d["next_gate"]:
                out.append(f"다음: {d['next_gate']}")
                out.append("")
    out.append("---")
    out.append("")
    out.append(
        "이 파일은 `scripts/build_saga_digest.py`가 생성한다. fiction/provenance only이며 "
        "QFUDS 연구 증거·roadmap status가 아니다."
    )
    out.append("")
    return "\n".join(out)


def main() -> None:
    by_shelf = collect()
    OUT.write_text(render(by_shelf), encoding="utf-8")
    total = sum(len(v) for v in by_shelf.values())
    print(f"wrote {OUT.relative_to(ROOT)}  ({total} docs)")
    for shelf, _role in SHELVES:
        print(f"  {shelf:18s} {len(by_shelf[shelf])}")


if __name__ == "__main__":
    main()
