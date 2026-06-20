---
doc_id: qfuds_saga_first_arc_release_immersion_revision_plan_ko
title: QFUDS SAGA 1부 Release 승격 — 현장감·묘사 강화 퇴고 기준
doc_type: guide
stage: reference
status: draft
evidence_role: provenance
depends_on:
  - qfuds_saga_first_arc_dejargon_polish_revision_plan_ko
  - qfuds_saga_prose_verisimilitude_audit_checklist_ko
  - qfuds_saga_bilingual_term_discipline_glossary_ko
next_gate: enhance 019-024 in place, re-audit, then promote to 40_release
last_updated: 2026-06-20
---

# QFUDS SAGA 1부 Release 승격 — 현장감·묘사 강화 퇴고 기준

## 목적

1부 한국어 정본 6편([019](../20_drafts/019_exhibit_s0_episode1_revised_v2_korean_adaptation.md)–[024](../20_drafts/024_the_broken_crown_revised_v2_korean_adaptation.md))을
`40_release/` 후보로 올리기 위한 **강화 퇴고**의 집행 기준. 1차 de-jargon pass는
[001 퇴고 계획](001_first_arc_dejargon_polish_revision_plan_ko.md)이 끝냈다. 이 문서는
그 위에서 **현장감·몰입·묘사**를 한 단계 끌어올리되, 이 작품의 절제 원칙을
깨지 않게 가드레일을 건다.

## Source Boundary

이 문서는 fiction/provenance 작업 기준이다. QFUDS 연구 증거, physical-source
claim이 아니다. SF 필력 reference는 일반 craft 원칙만 확인했다 — workflow state
`hit_not_cached`. 출처: Well-Storied(immersive setting), Lisa Hall Wilson(sensory
detail in deep POV), Writer's Digest(sensory detail in action). 외부 자료 handling은
[Research Asset and Product Workflow](../../../../../../../../.agent/workflows/research-asset-product-workflow.md).

## 강화 원칙 (무엇을 더하나)

일반 SF/소설 craft에서 확인한 몰입 기법을 이 작품 톤에 맞춰 채택한다.

1. **Deep POV(밀착 3인칭):** 묘사를 Liora(또는 시점 인물)가 **그 순간 실제로
   지각하는 방식**으로 건다. 카메라가 아니라 "인물의 눈 뒤 + 몸 안"에서 본다.
   심리적 거리를 줄인다.
2. **감각 특정성:** 시각에 치우치지 말고 소리·냄새·온도·촉각·무게를 **구체적
   개별물**로. "추웠다"가 아니라 "젖은 운동화 속 발가락", "회랑의 김 서린 유리".
   막연한 감각어 금지, 특정한 사물 우선.
3. **POV로 보여주기:** 배경은 그 자체로 설명하지 말고, 인물이 그것을 **어떻게
   다루고 무엇을 신경 쓰는가**로 드러낸다. 설정 정보도 인물의 행위·시선에 실어
   전달(incluing).
4. **긴장은 감각으로:** 고압 순간일수록 소리(크기·높이)·호흡·근육 긴장 같은
   몸의 신호로 felt consequence를 올린다. 추상 명사로 긴장을 "말하지" 않는다.
5. **상황 디테일:** 절차·도구·소품·관료적 마찰을 한 겹 더 구체화해 현장감을
   만든다(번호표, 도장 무게, 양식 빈칸, 줄의 위치). 핍진성 = 제도의 질감.

## 가드레일 (무엇을 하지 않나 — 이게 더 중요)

이 작품의 정체성은 **절제**다. 강화가 미사여구·장엄체로 흐르면 실패다.

- **장식적 비유 금지.** 비유는 땅에 붙고 한 장면에 **하나 이하**, 정보·정서를
  실어야만 허용. "심연·잔향·영토·울림" 같은 AI-tell 추상어 금지
  ([AI-tell 체크리스트](../00_studio/006_prose_verisimilitude_audit_checklist_ko.md)).
- **형용사·부사 적립 금지.** 동의어 이중수식, 정도부사 연발 금지. 명사·동사의
  특정성으로 승부한다.
- **단문 리듬 보존.** 이 작품의 짧은 단문 호흡을 길고 화려한 만연체로 바꾸지
  않는다. 긴 문장은 의도된 곳에만.
- **격언 1:1 부착 금지.** 구체 장면마다 "사람들은 ~한다" 식 일반화 격언을 붙여
  화자가 교훈을 먼저 닫지 않는다(027 감사 교훈).
- **분량 폭증 금지.** 강화는 밀도지 부피가 아니다. 본문이 20% 이상 길어지면
  과잉이다. 영어성 토큰(일반명사 영어)을 새로 늘리지 않는다.

## 의미 보존 철칙 (content-fidelity)

강화는 표면을 더하되 다음을 **한 글자도** 바꾸지 않는다.

- 플롯 사건과 그 순서, 인물의 행위·결정·결과.
- 대사의 의미(표현 다듬기는 가능, 뜻·정보 변경 불가).
- 사실·수치·고유명사·인용.
- 필드 마크/양식/Archive 응답 코드블록(```text```)은 **그대로**(영어 그대로,
  순서 그대로). 새 마크를 만들지 않는다.
- 시점(POV) 인물과 그가 아는 정보 범위.

새 plot 사건·새 인물·새 설정을 추가하지 않는다. 더하는 것은 **감각·상황
디테일과 POV 밀착**뿐이다.

## Before / After (보정의 결 — 예시)

```text
얇음(전):   서기관이 대답하지 않았다.
강화(후):   서기관이 대답하지 않았다. 그는 화면 모서리만 손톱으로 긁었고,
            그 작은 소리가 회랑의 김 서린 유리까지 닿았다.
```

(추가된 것: 소리·촉각·공간 감각. 바뀌지 않은 것: "대답하지 않았다"는 사실과
침묵의 의미.)

## 에피소드별 패스 체크리스트

각 편(019-024)에 적용한다.

1. 첫 장면(약 1쪽)을 deep-POV 감각으로 점검 — 독자를 즉시 몸 안에 넣는가?
2. 정보 전달 구간(설정·법·기술)이 강의조면 인물 행위·시선에 실어 incluing으로.
3. 대치/심리 비트에서 호흡·소리·근육 긴장 등 몸 신호로 긴장 보강.
4. 공간·소품·절차 디테일 한 겹 추가(핍진성 = 제도의 질감).
5. 가드레일 역점검 — 새 비유 1개 이하/장면, 격언 부착 제거, 분량 +20% 미만,
   필드 마크 불변.

## 검증 게이트 (release 승격 조건)

각 편이 아래를 모두 통과해야 `40_release/` 후보가 된다.

- `ai-tell-detector`: CLEAN(S1/S2 0).
- `naturalness-reviewer`: A급(과윤문 0).
- content-fidelity: 플롯·수치·인용·순서·필드 마크 불변.
- 영어성 토큰 density: de-jargon pass 수준 유지(증가 없음).
- `python3 scripts/validate_docs.py` 통과.

## 승격 절차

1. 019-024 in-place 강화(이 기준).
2. 편별 재감사 + fidelity 확인.
3. `40_release/`에 release candidate 번들(읽기 순서 + 확정 포인터) 생성,
   [Release Shelf](../40_release/README.md) 갱신.
4. 시리즈 [README](../README.md) 상태 갱신.
