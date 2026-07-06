---
doc_id: qfuds_verse_shelf_renumber_map_ko
title: QFUDS Verse 선반별 밴드 재번호 매핑 (2026-07-06)
doc_type: reference
stage: reference
status: provenance
evidence_role: provenance
depends_on:
  - qfuds_saga_canon_authority_and_ssot_map_ko
  - qfuds_verse_canon_drift_and_tech_debt_report_ko
next_gate: 새 문서는 선반 밴드의 다음 번호를 쓴다(continuity 004+, world 127+, bible 211+, story 324+, workroom 418+). 원고·revisions·archive는 구번호 유지
last_updated: 2026-07-06
---

# QFUDS Verse 선반별 밴드 재번호 매핑 (2026-07-06)

## 무엇인가

사용자 승인(2026-07-06)으로 실행한 선반별 밴드 재번호의 구→신 매핑 원장이다.
선반 안 번호를 연속으로 만들고, 전역 유니크를 유지하며, 원고 번호(0xx)와의
충돌을 없앤다.

| 선반 | 밴드 | 다음 번호 |
| --- | --- | --- |
| 00_continuity | 000~ (+900/901 감사 계열) | 004 |
| 10_world | 1xx | 127 |
| 00_bible | 2xx | 211 |
| 10_story_design | 3xx | 324 |
| 00_workroom | 4xx | 418 |

**불변 규칙:** `20_drafts`(원고 029~036, 프로토타입 015~028), `30_revisions`,
`90_archive`, `40_release`는 구번호 그대로다(stable ID, 게이트 런 불변 규칙).
provenance 문서가 인용하는 과거 행 번호(line NNN)와 드리프트 ID(DRIFT-012 등)도
구 표기 그대로 둔다.

## continuity (00_continuity)

| 구 | 신 |
| --- | --- |
| 002 | 001 |
| 011 | 002 |
| 036 | 003 |

## world (10_world)

| 구 | 신 |
| --- | --- |
| 001 | 101 |
| 003 | 102 |
| 005 | 103 |
| 006 | 104 |
| 007 | 105 |
| 009 | 106 |
| 010 | 107 |
| 013 | 108 |
| 015 | 109 |
| 017 | 110 |
| 018 | 111 |
| 020 | 112 |
| 021 | 113 |
| 025 | 114 |
| 026 | 115 |
| 028 | 116 |
| 030 | 117 |
| 031 | 118 |
| 032 | 119 |
| 033 | 120 |
| 034 | 121 |
| 035 | 122 |
| 037 | 123 |
| 038 | 124 |
| 039 | 125 |
| 040 | 126 |

## bible (00_bible)

| 구 | 신 |
| --- | --- |
| 004 | 201 |
| 008 | 202 |
| 012 | 203 |
| 014 | 204 |
| 016 | 205 |
| 019 | 206 |
| 022 | 207 |
| 023 | 208 |
| 024 | 209 |
| 027 | 210 |

## story_design (10_story_design)

| 구 | 신 |
| --- | --- |
| 002 | 301 |
| 007 | 302 |
| 008 | 303 |
| 009 | 304 |
| 010 | 305 |
| 011 | 306 |
| 012 | 307 |
| 013 | 308 |
| 014 | 309 |
| 015 | 310 |
| 016 | 311 |
| 017 | 312 |
| 018 | 313 |
| 019 | 314 |
| 020 | 315 |
| 021 | 316 |
| 022 | 317 |
| 023 | 318 |
| 024 | 319 |
| 025 | 320 |
| 026 | 321 |
| 027 | 322 |
| 028 | 323 |

## workroom (00_workroom)

| 구 | 신 |
| --- | --- |
| 001 | 401 |
| 003 | 402 |
| 004 | 403 |
| 005 | 404 |
| 006 | 405 |
| 007 | 406 |
| 008 | 407 |
| 009 | 408 |
| 010 | 409 |
| 011 | 410 |
| 012 | 411 |
| 013 | 412 |
| 014 | 413 |
| 015 | 414 |
| 016 | 415 |
| 017 | 416 |

## 이후 리네임 절차

파일명을 바꿀 일이 생기면 손으로 하지 않는다.

- 에이전트/CLI: `python3 scripts/rename_doc.py <old_path> <new_name> --dry-run`으로
  영향 범위를 보고 실행한다. git mv + 전 저장소 링크·라벨 갱신 + 깨진 링크 검사까지 한
  명령이다. 산문 속 맨 번호 인용은 자동 갱신되지 않으므로 번호 변경은 피한다(밴드에
  여유 번호가 있다).
- Obsidian: `docs/wiki`를 vault로 열면 리네임 시 링크가 자동 갱신된다(공유 설정
  `.obsidian/app.json`: 마크다운 링크·상대 경로·자동 갱신 on).

## Boundary

```text
fiction/provenance only
research evidence: no
external source claim: no
```
