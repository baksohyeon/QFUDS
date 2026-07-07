---
doc_id: qfuds_fiction_zettelkasten_wip_readme
title: fiction_zettelkasten_wip
doc_type: reference
stage: reference
status: draft
evidence_role: provenance
depends_on:
  - wiki_fiction_index
next_gate: distill source-index cards into permanent zettels; keep this tree outside the SSOT
last_updated: 2026-07-07
---

# fiction_zettelkasten_wip

픽션 소스 인덱스 + 수기 zettel 작업본을 **SSOT 밖에서** 보존하는 폴더다.

## 성격 / 경계

- **Universe / IP**: qfuds-verse (일부 vector-sandbox 포함). 원 위치는 `docs/wiki/fiction/` 였다.
- **Authoring baseline**: 2026-07-07 (작가 측 기준일; 작중 연대기와 무관).
- **Format**: source-index / zettelkasten working copy (Markdown, 비정본).
- **Canon status**: **비정본 · 작업본(WIP)**. 여기의 어떤 파일도 정본이 아니다.
- **SSOT 경계**: 정본 SSOT는 `docs/wiki/fiction/` 이며 `main` 상태를 유지한다.
  이 폴더는 SSOT가 아니고, 문서/픽션 게이트(validate_docs, fiction_gate 등)의
  스캔 범위(`docs/`, `docs/wiki/fiction*`) 밖에 두기 위해 저장소 루트에 있다.
- **Inherited rules**: 원 위치의 규칙을 참고만 한다. 정본 승격은
  `.agent/workflows/fiction-ip-management-workflow.md` 절차를 거쳐
  `docs/wiki/fiction/` 로 다시 라우팅해야 한다.
- **Local overrides**: 없음. 소스 인덱스 카드는 원문 발췌+역링크만 담고 내용을 지어내지 않는다.
- **Fiction / provenance 경계**: 픽션 전제는 QFUDS 연구 근거가 아니다.

## 용어 (중요)

- `02_zettelkasten/`의 생성 카드는 **소스 인덱스**다 — heading 단위 발췌·역링크이지
  원자적 아이디어 노트가 아니다. **제텔카스텐이 아니다.**
- "zettel" / "제텔카스텐" 명칭은 `10_universes/` 아래 **수기 원자 노트**(예 900–914,
  상호 링크·템플릿 준수)에만 쓴다.
- 소스 인덱스 카드는 작가가 하나씩 수기 zettel로 **증류**하는 원재료다.

## 유래(provenance)

- `codex/fiction-zettelkasten-worldbuilding` 브랜치가 `docs/wiki/fiction/`(SSOT)에
  직접 추가했던 산출물을 SSOT 밖으로 옮겨 보존한 복제본이다.
- 소스 인덱스 층(`02_zettelkasten/`)은 리뷰 후 `scripts/build_fiction_zettelkasten.py`로
  `--source docs/wiki/fiction --output fiction_zettelkasten_wip` 재생성했다 (링크 정합·한글
  슬러그·결정적 날짜·원자 zettel 미분쇄 반영).
- 수기 노트/카탈로그(`10_universes/`, `01_catalog/`)는 커밋 `70d6c7d`의 추가분을 그대로 보존.

## 구성 (현재 카운트)

| 경로 | md 파일 수 | 성격 |
| --- | ---: | --- |
| `02_zettelkasten/` | 2,747 | 소스 인덱스 (카드 2,536 · 소스맵 209 · 인덱스 2) |
| `01_catalog/` | 3 | 파일럿 인덱스 / MoC / 인박스 (수기) |
| `10_universes/` | 16 | 수기 원자 zettel · 스토리 씨앗 레지스터 |
| README.md | 1 | 이 파일 |
| **합계** | **2,767** | |
