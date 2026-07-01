---
doc_id: qfuds_saga_consistency_audit_2026_07_01_ko
title: QFUDS SAGA 전문서 정합 감사 (2026-07-01)
doc_type: guide
stage: reference
status: draft
evidence_role: provenance
depends_on:
  - qfuds_saga_near_future_recenter_direction_ko
  - qfuds_saga_character_map_and_timeline_coordinates_ko
  - qfuds_saga_machine_childhood_ai_history_narrator_throughline_ko
next_gate: "사용자 게이트 대기 항목(036 리네임 여부·본문 전면 재라벨·status 강등·011 번호 지위) 결정 후 2차 패스"
last_updated: 2026-07-01
---

# QFUDS SAGA 전문서 정합 감사 (2026-07-01)

## Boundary

```text
fiction/provenance only
research evidence: no
이 문서는 사가 문서 정합 감사 기록이다. QFUDS 연구 증거·roadmap status 아님.
workflow: 멀티에이전트 감사(7 폴더 리더 + 편집자 종합 + 완결성 검수), 발견·정리 기록.
```

## 1. 감사 개요

- **범위**: qfuds-saga 전 115개 .md (00_workroom·00_bible·10_story_design·20_drafts·30_revisions·40_release).
- **방법**: 폴더별 병렬 리더 7 → 편집자 종합(단일 픽스 원장) → 완결성 검수. 51개 findings.
- **핵심 결론**: 캐논 자체는 건강하다. 산문 원고 전부 온캐논, 폐기명 '주아' 본문 침투 0건.
  진짜 구조 결함은 소수(005 링크 오타 + 산문 원고 em dash 2곳)이고, 나머지 약 70%는
  단일 계통 = **2026-06-30/07-01 리센터의 라벨 지연**(신설 4문서에는 반영됐으나 구세대
  캐릭터·인덱스 문서·board에는 미도달)이다.

## 2. 현행 캐논 SSOT 지도

| 관통선 단계 | 부 | 시대좌표(024) | 주인공 | 자산 | 기계의 성장 |
| --- | --- | --- | --- | --- | --- |
| 씨앗 | 0부 | 현재편 2026 | 캐스(Cassandra) | 036 | 판정의 충동 |
| (grief-tech) | 1부 | 근미래 2030년대 | 오웬(Owen) | 035 | 어머니 복원 사본 |
| 제도 | 1.5부 | 근미래 Q-Day | 사엘(Sael) | 033 (030=폐기 프로토타입) | 도장·선례 |
| 신 | 2부 | 먼 미래 4기 | 마라 베이르 | 034 (029=원천 초고) | 죽은 자 복원·소유 |
| (소재 보존) | 3부 | 먼 미래 | author-loss | 025·026·027 | |

**권위 규칙**: 시대좌표·캐릭터 SSOT=024 / 톤·무게중심 SSOT=025(근미래 grounded, 먼 미래=도달점)
/ 관통선 정본=027 / 복원=사본 물리=021+025-physics / 명칭=015 / 실명 차용=018 §9.
**폐기**: 주아(→캐스), 단일 주인공 통일(→앤솔로지), 오페라 먼미래 중심(→근미래 무대), 사엘=1부(→1.5부).
**em dash 규칙**: 20_drafts 산문 원고에만 0 하드 제약. planning·인덱스·아카이브 문서의 표·헤더 em dash는 위반 아님.

## 3. 이번 패스에서 적용한 안전 배치 픽스

| 구분 | 대상 | 처리 |
| --- | --- | --- |
| 링크 오타 | 00_workroom/005 | depends_on doc_id `agentic_saga`→`agentic` 정정 |
| em dash 0 | 20_drafts/1.5부/033, 3부/027 | 산문 원고 em dash(부록 헤더·아티팩트) 전부 콜론/괄호 치환 |
| 라벨 정정 | 033 | 사엘 title/H1/Boundary "1부 origin"→"1.5부 origin" |
| 인덱스 커버리지 | SAGA README·10_story_design README·00_bible README·20_drafts README·009 board | 0부 캐스(036) 행 + 신설 캐논(024·025·026·027) 진입점 추가 |
| 드리프트 배너 | 023·009fmt·018·008·012·016·019·002 | H1 아래 "024·025·027 우선" 표준 배너(본문 전면 재라벨 안 함) |
| SSOT 내부 정정 | 00_bible/024 | 자기모순 노트 "사엘=1부"→"1.5부"(상단 확정표와 일치) |
| 무게중심 | 10_story_design/011 | §갱신에 025 근미래 무게중심 + 본문 라벨 주의 각인 |
| 문구 정정 | 30_revisions README | 커밋 해시 c158d31→1308777, 번호 SSOT→024 우선 |
| 프레이밍 | 20_drafts/0부/036 | title/Boundary "단일 주인공·앤솔로지 폐기"→"앤솔로지 현재편(씨앗, 캐스)" |
| next_gate | 3부/025·026 | flat 에피소드 순번 잔재 매핑 정정 |

## 4. 사용자 게이트 대기 (deferred, 개별 판단)

| # | 항목 | 결정할 것 |
| --- | --- | --- |
| D1 | 036 파일명·doc_id `jua` 잔재 | stable-ID 정책 예외로 cass 리네임할지(본문·표시명은 이미 캐스). 기본값=유지 |
| D2 | 008·012·016·019·018 §8 본문 전면 재라벨 | 배너로 충분한지, "1부"→"2부" 전면 교체까지 밀지 |
| D3 | 30_revisions 003·008 status: completed | 강등 전 지시를 provenance로 낮출지 본문 갱신할지 |
| D4 | 011의 "아크 번호 SSOT" 지위 | 024 우선으로 완전 강등할지, 아크 번호 참고 지위 유지할지 |
| D5 | 00_bible 005 `concept_origin` depends_on | 저장소 밖 `01_origin/` 외부 참조인지 진짜 dangling인지 확인(검수자 지적, 자동삭제 보류) |

## 5. 검수 보정 기록 (완결성 검수 반영분)

- 036 앤솔로지 프레이밍: 원장 HIGH → 검수 LOW 하향 채택(025가 이미 "앤솔로지 현재편"으로 재분류).
- 024를 무비판 SSOT로 본 진실 시트 전제 철회: 024는 내부 자기모순을 품었고(§3에서 정정), 상단 확정표만 신뢰.
- M9(005 concept_origin) 자동삭제 제외: 외부 provenance 참조 가능성(D5).
- 3부/027 em dash: 하드 제약 문자대로 처리(치환 완료). 부록·아티팩트 헤더 예외 해석은 하니스 소유자 확인 여지.
- 커버리지 재확인 권고: 00_bible/011(≠10_story_design/011)·004·007·010·013·014·015·017·020~023, 00_workroom/006·010은 개별 픽스 대상 아님(현행 캐논 충돌 미발견 또는 배너 세트로 커버).
