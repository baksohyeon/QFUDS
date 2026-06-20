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

## 독자 이해도·오리엔테이션 게이트 (최우선, 신규)

AI 티·자연스러움만으로는 부족하다. 이게 1차 release를 성급하게 만든 빈틈이었다.
**독자가 첫 페이지에서 상황·세계·인물을 이해하는가**가 release의 1순위 조건이다
(문창과 기본기: orientation, establishing shot, "늦게 들어가되 빨리 자리잡게
하라"). 분위기·비유보다 **오리엔테이션이 먼저**다. AI-tell CLEAN·naturalness A를
받아도 독자가 길을 잃으면 release 불가.

각 편 첫 1쪽(약 첫 화면)을 외부 독자 관점으로 정독해 점검한다.

- **누가/어디/언제/무엇이 걸려 있나**가 처음 5~8줄 안에 잡히는가? (마션식 즉시 정착)
- 첫 등장 고유명사·기술어(Waiting City, Court of Continuance, Genesis 등)가
  쓰이기 전이나 직후에 **평이하게 grounding**되는가? 설명 없는 명사 무더기 금지.
- 첫 문장이 추상 명제·해독 필요한 비유로 시작하지 않는가? (구체 상황 우선)
- 한 문장에 미해독 신조어가 2개 이상 쌓이지 않는가?
- 핵심 전제(이 세계에서 무엇이 가능하고 무엇이 위태로운가)가 정보 블록에 묻히지
  않고 **장면으로** 먼저 전달되는가?
- 독자가 "이게 무슨 말이야"로 멈추는 지점이 있는가? 있으면 1순위 수정 대상.
- 기술·과학(비트코인·블록체인·복원·radiation 등)이 판타지가 아니라 **실제
  메커니즘대로 정확**하면서, 초등학생도 따라올 만큼 평이한가? 비유로 정확성을
  뭉개지 않았는가?

판정: 외부 독자가 첫 페이지만 읽고 **상황을 한 문장으로 요약**할 수 있어야 통과.

## 스토리 아키텍처 게이트 (구조, 신규·중요)

문장 층위(AI 티·자연스러움·이해도·정확성)만으로는 1부가 중반에 무너졌다. 진짜
원인은 문장이 아니라 **구조**였다. 그래서 구조를 별도 게이트로 본다.

- **인과 연결**: 사건이 "그리고 또"(and then)가 아니라 "그래서/하지만"(therefore/but)
  으로 이어지는가? 에피소드 단순 나열이면 실패.
- **상승**: 편이 갈수록 판돈·위험·압박이 커지는가? 매 편 같은 강도면 실패.
- **주인공 아크**: 시점 인물의 욕망·대가·변화가 1부를 관통해 자라는가?
- **중심 질문 연속성**: 1편이 건 약속(되살아난 거부자 Mara)이 중반에 새 의뢰인으로
  희석되지 않고 이어지는가?
- **RUE(설명 욕구 억제)**: 화자가 장면이 벌어 줄 의미를 격언으로 먼저 닫지 않는가?
- **장면 변주**: 매 장면이 "방에서 토론"인가? 장면 종류·감정 진폭이 다양한가?
- **반복 안무 금지**: 같은 연출(표식 거부 후 재입력, 미래시제 3단 클로징 등)을
  편마다 복붙하지 않는가?

### 1편 retroactive 적용 기록

사용자 지시로 `00_workroom/005`의 시리즈 프리플라이트를 1편([019](../20_drafts/019_exhibit_s0_episode1_revised_v2_korean_adaptation.md))에
먼저 역적용했다. 2-6편은 같은 방식으로 후속 적용한다.

| Gate | 1편 적용 |
| --- | --- |
| 반복 인물 시트 | Liora는 [012](../00_bible/012_character_liora_sen_ko.md), Mara/Elias/Pell/Last Archive는 [016](../00_bible/016_character_ensemble_voices_relationships_ko.md) 미니시트로 차단 조건 해소 |
| 시점 인물 선언 | Liora 제한 3인칭. draft의 `Series Gate Applied`에 명시 |
| 인과 연결 | Genesis Chain 접근권 -> Mara 복원 청구 -> Liora의 지연 표식으로 이어짐 |
| 상승 | 개인 배우자 청구가 `RECOVERABLE / NOT CLAIMABLE`이라는 제도 언어로 커짐 |
| 중심 질문 | "복원 가능하면 청구 가능한가"를 열고, `who may author loss`까지 이어지는 첫 질문으로 둠 |
| 단독 완결 금지 | Pell이 표식을 패소가 아니라 상품 언어로 읽는 불안을 남겨 2편 Dead Exchange로 연결 |
| POV 로테이션 준비 | 1부는 Liora 고정 POV로 시작하되, 2부 Noor/Ione/Sera 후보를 [016]과 [010 episode map](../10_story_design/010_arc_two_episode_map_ko.md)에 보존 |

## 검증 게이트 (release 승격 조건)

각 편이 아래를 모두 통과해야 `40_release/` 후보가 된다.

- **스토리 아키텍처 게이트(위), 구조 1순위.** 인과·상승·아크·중심질문·RUE.
- **시리즈 프리플라이트 표.** 기존 원고도 `Series Gate Applied` 또는 동등한
  편별 적용 기록이 있어야 한다.
- **독자 이해도 게이트(위), 최우선.** 첫 페이지 오리엔테이션 통과.
- **기술 정확성·평이성.** 과학/기술 서술이 실제 메커니즘대로 정확 + 초등학생 이해.
- **독자 페르소나 리텐션 테스트(아래) 통과.**
- `ai-tell-detector`: CLEAN(S1/S2 0). em dash 0 (한국어·영어판 모두 금지, 영미권에서도 AI-tell). 시각 장식 0.
- `naturalness-reviewer`: A급(과윤문 0).
- content-fidelity: 플롯·수치·인용·순서·필드 마크 불변.
- 영어성 토큰 density: de-jargon pass 수준 유지(증가 없음).
- `python3 scripts/validate_docs.py` 통과.

## 독자 페르소나 리텐션 테스트 (재미·흡입력 게이트)

서로 다른 독자 페르소나(중학생 SF 입문, 고등학생, 대학생~직장인, 웹소설 속독,
까다로운 순문학, 기술 문외한, 5분 출퇴근 독자, 안티-AI 냉소가, 테드 창식 하드SF
정밀·절제 독자, SF 애호가)를 서브에이전트로 만들어, 각자 release
원고([40_release/002](../40_release/002_first_arc_manuscript_ko.md))를 **재미·흥미가
유지되는 동안만** 읽게 한다. 각 페르소나가 보고한다.

- **이탈 지점**: 흥미가 끊겨 그만두고 싶어진 정확한 장면·줄과 그 이유(이탈 트리거).
- **편별 몰입 점수**(1~10)와 다음 편으로 넘어갈지 여부.
- 끝까지 끌고 간 훅, 가장 약한 구간.

집계해 **공통 이탈 지점**을 찾고, 그곳을 고친 뒤 테스트를 **반복**한다. 모든
페르소나가 목표 리텐션(사실상 끝까지 흥미 유지)에 도달할 때 통과한다.

## 승격 절차

1. 019-024 in-place 강화(이 기준).
2. 편별 재감사 + fidelity 확인.
3. `40_release/`에 release candidate 번들(읽기 순서 + 확정 포인터) 생성,
   [Release Shelf](../40_release/README.md) 갱신.
4. 시리즈 [README](../README.md) 상태 갱신.
