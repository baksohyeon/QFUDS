---
doc_id: qfuds_saga_final_chronicler_report_ko
title: QFUDS Verse 최종 통합 Chronicler Report (전 범위 감사·의존성 그래프·P0/P1/P2 로드맵)
doc_type: guide
stage: reference
status: provenance
evidence_role: provenance
depends_on:
  - qfuds_verse_worldbuilding_architecture_ko
  - qfuds_verse_canon_drift_and_tech_debt_report_ko
  - qfuds_saga_chronicler_pass_plan_ko
  - qfuds_saga_canon_authority_and_ssot_map_ko
  - qfuds_saga_character_map_and_timeline_coordinates_ko
next_gate: P0 없음. P1 Chronicler Pass(414 5-Phase)부터 사용자 승인 하에. 그래프는 scripts/build_doc_graph.py 재생성
last_updated: 2026-07-06
---

# QFUDS Verse 최종 통합 Chronicler Report (전 범위 감사·의존성 그래프·P0/P1/P2 로드맵)

## 무엇인가

`qfuds-verse` **전 범위**(in-scope + drafts + revisions + release) 전문 완독 감사를 하나로 묶은
최종 리포트다. 앞선 산출물([900 아키텍처](../../../00_continuity/900_worldbuilding_architecture_ko.md)·
[901 드리프트/부채](../../../00_continuity/901_canon_drift_and_tech_debt_report_ko.md)·
[414 Chronicler Pass 계획](414_chronicler_pass_plan_ko.md)·[413 Truth-State Ledger](413_truth_state_ledger_ko.md))
을 통합하고, drafts/revisions/archive 확장 감사를 §9로 더한다.

**읽기 전용 분석서**다. 파일을 삭제·이동·리라이트하지 않는다. drafts/revisions/archive는 현행
SSOT 대비 **드리프트 탐지에만** 참조하며 승격하지 않는다. 문학 리뷰가 아니다. 불확실은 "미정"
또는 "검증 필요"로 표기한다.

의존성 그래프는 도구로 산출한다: `python3 scripts/build_doc_graph.py` →
`outputs/qfuds_verse_doc_graph.{db,dot,html}`. 이 리포트의 노드/엣지 수치는 그 산출 기준이다.

```text
fiction/provenance only
research evidence: no
external source claim: no
```

## 1. 전체 문서 인덱스 (전 범위 138노드)

그래프 도구가 스캔한 `qfuds-verse/**` 전 `.md` 138개. class 분포:

| class | 수 | 선반 |
| --- | --- | --- |
| canon | 32 | 00_continuity 6 · 10_world 16 · 00_bible 10 |
| candidate | 10 | 10_world 8(117-122·123·124) · story_design 2(322·309) |
| design | 20 | 10_story_design |
| provenance | 24 | 00_workroom 15 · 40_release 2 · README·root 등 |
| draft | 36 | 20_drafts |
| revision | 16 | 30_revisions |
| 합계 | 138 | |

in-scope 81(감사 고정 범위)의 문서별 path·doc_id·type·status·class 전수 표는
[414 §1](414_chronicler_pass_plan_ko.md)이 보유(중복 회피). 확장분(drafts 36·revisions 16)은
전부 `status: draft`·`evidence_role: provenance`이며, 부별 폴더(0/1/1.5/2/3부)로 정리돼 있다.
전 노드의 쿼리 가능한 표는 `outputs/qfuds_verse_doc_graph.db`의 `nodes` 테이블.

## 2. SSOT 계층도

권위 루트 = [000 캐논 권위·SSOT 지도](../../../00_continuity/000_canon_authority_and_ssot_map_ko.md)
(§도메인 권위 표: 명시 우선 > 도메인 표 > last_updated > unknown).

```text
000 (권위 루트)
├─ 복원 물리       → 113   (원본 부재 물리 114가 최상위)
├─ 명칭·세력명      → 109   (Domus Clavium 단일화)
├─ Q-Day 여파      → 115   (부속 116)
├─ 인과·Last Archive → 107  (키스톤)
├─ 연표·복원 행정    → 002   (+ 딥타임 001, 심층시간 003)
├─ 인간 확인 루프    → 112
├─ 시대 좌표(인물)   → 209   (series bible)
└─ 이념 형이상학·원어 → 123·124 (candidate)
```

충돌 우선순위(000·123): **114 > 113 > 115 > 102 > 109**. 전 범위 피의존 키스톤 = 107
(in_degree 21; drafts까지 포함해 최상). 그다음 310 질문(14), 106·110·209(13), 205(11), 001(10).

## 3. Canon / Candidate 분류표

| 구분 | 문서 | 규율 |
| --- | --- | --- |
| **canon** (32) | 00_continuity 000·001·002·003, 10_world 101·102·103·104·105·106·107·108·109·110·111·112·113·114·115·116, 00_bible 201·202·203·204·205·206·207·208·209·210 | SSOT. 충돌 시 §2 우선순위 |
| **candidate** (10) | 10_world 117·118·119·120·121·122(웨이브)·123(이기)·124(원어), story_design 322(프렐류드)·309(sovereign-AI brainstorm) | 6체크 게이트 전까지 canon 아님 |
| **design** (20) | 10_story_design 나머지(아웃라인·리빌·씬 카드) | 승격 전 stable canon 아님 |
| **provenance** (24) | 00_workroom 15 + 40_release 900·README + 전 README + 루트 | 생산·감사·색인. canon 아님 |
| **draft** (36) | 20_drafts 산문 | 승격 대상 아님. 감사 참조만 |
| **revision** (16) | 30_revisions 개정 계획·게이트 런 | provenance. 감사 참조만 |

6체크(승격 전): (1) 109 명칭 충돌 없음, (2) 114/113 물리 모순 없음, (3) 115 여파 착지,
(4) em dash 0·"박-" 슬랭 0·강의조 없음, (5) 실존 집단 비대응, (6) 상위 SSOT depends_on·인덱스 배선.

## 4. 중복 개념 목록 (의도된 layering vs 실제 중복)

| 클러스터 | 성격 | 판정 |
| --- | --- | --- |
| 캐릭터 203·205·206·209 | 203=Liora, 205=Voice·관계, 206=Arc, 209=좌표 SSOT | 의도된 layering. 206 Core Drive 20-30% 반복만 참조화(901 DRIFT-013) |
| 115 ↔ 116 | 116이 115 부속(14도메인) | 중복 아님(부속) |
| 202 9단서 ↔ 115 §4 떡밥 지도 | 반전 배치 vs 화자 회수 지도 | 상보(413 Ledger가 통합) |
| 001 ↔ 003 | 001 딥타임 골격 ↔ 003 심층시간 확장 레이어 | 상보(003이 113>001 우선 선언) |
| 107 인과 ↔ 111 컴펜디움 | 111=색인/내비 | 역할 인접, 중복 아님 |

## 5. Canon 충돌 목록 (검증 필요 포함)

| # | 충돌 | 근거 위치 | 판정 |
| --- | --- | --- | --- |
| C1 | 시대 좌표 SSOT 본문이 "사엘(1부)" 표기 | `00_bible/024_..:108` "사엘(1부) ┄ 2부 청구 사건" | 현행 매핑 사엘=1.5부와 어긋남. SSOT 자체 라벨이라 **P1 최우선**. 단 포괄 의미인지 오기인지 **검증 필요** |
| C2 | legacy "Arc Two" 부 라벨 | `00_bible/008_..:182-239` Arc Two Hook, `story_design/007_..:3·17·53` title·본문, `story_design/012_..:94`, `013_..:148` | 306 §remap과 정합하나 표기 legacy. P1 Chronicler Pass |
| C3 | 폐기 어근 잔존 지명 | `00_bible/201_..:187` `Castra Tabularii`(원장 성채) | 109가 Domus Clavium 단일화. 지명 의도인지 **검증 필요**(P1) |
| C4 | "복원=부활" 현대 gloss | `002_..:24-`, `005_..:24-` 배너, `113 §5` | **해소됨**: 124 원어 층 + 배너(901 D2). 충돌 아님 |

물리·의미 충돌 시 114 > 113 > 115 > 102 > 109가 항상 이긴다(§2).

## 6. Dead Link / 오래된 참조

- **깨진 마크다운 링크: 0**(전 범위). 권위 링크 전부 유효.
- **미해소 depends_on 대상 27건**(그래프 dangling). 3분류:
  - (a) **범위 밖 유효**(studio/catalog/root 인덱스): `fiction_ip_management_system_ko`(00_studio/001),
    `fiction_catalog_index_ko`(01_catalog), `agentic_fiction_harness_perspectives_ko`(00_studio/008),
    `wiki_fiction_index`(루트). 실재 문서, 스캔 루트 밖일 뿐. **정상**.
  - (b) **아카이브 provenance**(정상 보존): `qfuds_saga_the_broken_crown_english_draft`·
    `mara_veyr_prologue_draft_ko` 등 → `90_archive/qfuds-saga_1부_legacy/`,
    `world_direction_matrix_ko`·`six_episode_outline_ko`·`liora_sen_first_episode_beat_sheet_ko`·
    `genesis_chain_artifact_scene_packet_ko` 등 → `90_archive/qfuds-saga_pre_reboot_planning/`.
    삭제된 1세대 원고·계획을 가리키는 lineage 참조. 아카이브에 실재. **P2**.
  - (c) **진짜 dead 2건**: `concept_origin`(`10_world/103` depends_on의 의미 토큰, 실제 doc 아님),
    `qfuds_lineage_agentic_research_system_ko`(lineage 포인터, 해소 안 됨). **P2**(경미, 정합 시 정리).
- 그래프에서 (b)(c)는 별색(red dashed) 노드로 표기돼 한눈에 구분된다.

## 7. 리팩터링 우선순위

| 순위 | 대상 | 근거 | 위험 |
| --- | --- | --- | --- |
| P1 | C1 209 "사엘(1부)"(검증 후) → C2 Arc Two 라벨 → C3 Castra Tabularii(검증) | §5·901·109 | 중(SSOT·완료 문서 포함) |
| P1 | 명칭 잔재 정리(201 Naming ↔ 109) | 901 DRIFT-009/012 | 낮음 |
| P2 | 206 Core Drive 참조화, candidate 배너·6체크 명문화 | 901 DRIFT-013/005/019/021 | 낮음 |
| P2 | dead 토큰 2건 정리(concept_origin·lineage) | §6(c) | 낮음 |
| P3 | status 위생(안정 문서 draft→reference), 029 결번 각주 | 901 §5 | 낮음 |

이미 처리됨(재작업 불필요): 복원 용어(D2, 124), Truth-State Ledger(204), 그래프 도구(이 리포트).

## 8. 세계관 아키텍처 다이어그램 + 그래프 도구

캐논 3층 + 집행층(상세 [900 §3](../../../00_continuity/900_worldbuilding_architecture_ko.md)):

```mermaid
graph TD
  subgraph Canon
    W[World Canon · 10_world]
    C[Continuity Canon · 00_continuity]
    S[Story Canon · 00_bible]
  end
  subgraph 집행·설계층 (canon 아님)
    WR[00_workroom · provenance]
    SD[10_story_design · design]
    RL[40_release]
  end
  OUT[20_drafts · 30_revisions · 90_archive<br/>범위 밖·감사 참조만]
  C --> W
  C --> S
  W --> S
  S --> SD
  WR --> SD
  SD --> OUT
  RL --> OUT
```

**의존성 그래프 도구(옵시디언식 인터랙티브):**

- 생성: `python3 scripts/build_doc_graph.py` (Python 표준 라이브러리만, 외부 의존 0).
- 산출(`outputs/`):
  - `qfuds_verse_doc_graph.db` : sqlite. `nodes`(doc_id·path·title·layer·class·status·in_degree)·
    `edges`(src·dst·resolved)·`dangling` 테이블. 예: `SELECT doc_id,in_degree FROM nodes ORDER BY
    in_degree DESC LIMIT 10;`로 허브 확인.
  - `qfuds_verse_doc_graph.dot` : GraphViz. `dot -Tsvg`로 정적 렌더.
  - `qfuds_verse_doc_graph.html` : 자체 완결 인터랙티브 force-directed(레이어별 색·in_degree별
    크기·검색·클릭 툴팁). 브라우저로 연다.
- 해석: 노드 138·엣지 461(resolved 404). 색=선반, 크기=피의존. red dashed=미해소(§6). 큰 붉은
  허브가 107(21). 고아(피의존 0, non-README) 30개 = 신규/말단 노드(003·123·124·210·204 등).

## 9. Draft / Revision / Archive Drift Audit Addendum

확장 범위 `20_drafts`(36)·`30_revisions`(16)·`90_archive`(qfuds-saga 하위 0, 비어 있음). 현행
SSOT 대비 드리프트만 탐지(리라이트·승격 없음). 근거 경로·행 인용.

### 9.1 활성 산문은 대체로 SSOT 정합 (긍정 증거)
- **복원=사본(113) 이미 적용:** `20_drafts/2부/029_first_arc_book1_reboot_korean_primary.md:2316`
  "복원은 부활이 아닙니다", 동:2453·3107·3140 "사본·Restoration-as-copy·보존 != 부활";
  `20_drafts/2부/034_mara_full_novel_korean_primary.md:2519·2708` 동일. → 드리프트 아님.
- **근미래 리센터(320) 반영:** `20_drafts/0부/036_jua_full_novel_korean_primary.md:31`
  "톤: 근미래 grounded SF ... 오페라·라벨 0". → 모순 없음.
- **폐기 세력명 없음:** 활성 산문(029·033·034·035·036)에 `House Tabularii` 미출현.

### 9.2 드리프트 발견 + 분류

| ID | 발견 | 근거 위치 | 분류 |
| --- | --- | --- | --- |
| AUD-1 | `House Tabularii` 잔존(폐기 세력명) | `2부/_versions/1부_prototype/{015,016,017}_*english_draft.md`, `2부/_versions/1부_v3_pre_R4/{022,023,024}_*korean_adaptation.md` | **P2**(프로토타입, `_versions/README.md`가 pre-reboot로 라벨) |
| AUD-2 | legacy "Arc Two" 부 라벨 | `20_drafts/3부/{025,026,027}_*:` 말미 주석("Episode 025 opens Arc Two") | **P1-lite/P2**(서사 본문 아닌 주석. 폴더는 3부. 306 §remap 정합) |
| AUD-3 | revision 문서의 폐기명 언급 | `30_revisions/007_..:484` "House Tabularii 금지; Domus Clavium 병기" | **Ignore**(오히려 폐기를 문서화. 정상) |
| AUD-4 | 아카이브 오인 위험 | `90_archive/qfuds-saga_1부_legacy/`, `_pre_reboot_planning/`(§6b) | **archive-only**(전 draft 폴더 README에 `canon 상태: 초안`+universe/IP 헤더. 오인 위험 완화) |

- **부 라벨·캐릭터 좌표 모순:** 활성 산문 폴더 구조가 이미 0/1/1.5/2/3부로 정합. 산문 본문에서
  현행 좌표(209)와 정면 충돌하는 사례는 발견되지 않음(주석 레벨 legacy만, AUD-2).
- **복원=부활 함의:** 활성 산문에 없음(9.1). `_versions/` 프로토타입은 미점검 항목이나 pre-reboot로
  격리돼 릴리스 경로 밖.

### 9.3 분류 요약
- **P0(릴리스 블로커): 0건.** 활성 산문·캐논은 현행 SSOT와 충돌 없음.
- **P1: 경미.** AUD-2(3부 주석 Arc Two) + §5 C1-C3(in-scope, Chronicler Pass 대상).
- **P2: AUD-1**(프로토타입 House Tabularii)·§6(b)(c). 무해 legacy/provenance.
- **archive-only: AUD-4.** 조치 불요(라벨로 완화됨).

## 10. P0/P1/P2 Final Roadmap

- **P0 (즉시): 없음.** 릴리스 블로커 드리프트 미발견. 활성 산문은 113·114·109 정합.
- **P1 (Chronicler Pass, 사용자 승인 하):** [414 계획](414_chronicler_pass_plan_ko.md)의 5-Phase.
  - Phase 1 명칭(C3 Castra Tabularii 검증·201↔109).
  - Phase 2 부 라벨(**C1 209:108 최우선** → C2 202·105·203·108 → AUD-2 3부 주석). 배너는 본문
    정합 후 축약. stable ID상 파일명·doc_id는 유지, 본문 라벨만.
  - Phase 3 캐릭터 참조화(206). Phase 4 candidate 위생. Phase 5 검증·마감.
- **P2 (위생, 비긴급):** dead 토큰 2건(§6c) 정리, status draft→reference 승격 검토, 029 결번 각주,
  _versions 프로토타입은 현상 유지(라벨 충분).
- **미정/검증 필요:** C1(209 "사엘(1부)"가 포괄 의미인지 오기인지), C3(Castra Tabularii 지명 의도).
  저자 확인 후 Phase 2·1 착수.

각 Phase 착수 전 사용자 승인. 실행 시 900/901/413/이 리포트를 함께 갱신해 원장과 본문 정합 유지.
커밋 전 점검은 [414 §10](414_chronicler_pass_plan_ko.md) 명령 사용.

```text
fiction/provenance only
research evidence: no
external source claim: no
```

이 리포트는 전 범위 전문 완독 감사의 최종 통합본이다. P0 없음, P1은 109 Chronicler Pass로 정리,
drafts/revisions/archive는 참조만 하고 수정하지 않는다. 의존성 그래프는 `scripts/build_doc_graph.py`
로 언제든 재생성한다.
