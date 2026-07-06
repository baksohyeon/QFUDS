---
doc_id: fiction_craft_and_political_theory_research_ko
title: Fiction 창작 기법·정치이론 자료조사 (비약 없는 노출 + 세계규칙 실증 앵커)
doc_type: guide
stage: reference
status: draft
evidence_role: reference
depends_on:
  - fiction_university_creative_writing_reference_matrix_ko
  - fiction_prose_verisimilitude_audit_checklist_ko
next_gate: apply incluing ladder + theory anchors to first-arc opening revision
last_updated: 2026-07-06
---

# Fiction 창작 기법·정치이론 자료조사 (비약 없는 노출 + 세계규칙 실증 앵커)

## 목적

"어려운 개념(비트코인 붕괴, 복원 물리, 제도 권력)을 중·고생 독자도 **비약 없이**
따라오게" 쓰기 위한 창작 기법과, 세계 규칙을 뒷받침할 실제 정치·경제 이론·사례를
모은 참고 문서. 테드 창식 "배경 비약 없는" 노출을 목표로 한다.

이 문서는 reference다. QFUDS 연구 증거가 아니다.

## Workflow Boundary

이 문서는 외부 웹 출처를 craft/이론 reference로만 인용한다. QFUDS support,
validation, physical-source claim을 만들지 않는다. 외부 자료 handling은
[Research Asset and Product Workflow](../../../../.agent/workflows/research-asset-product-workflow.md)가
지배한다.

현재 research asset workflow state:

```text
hit_not_cached
inaccessible
```

`hit_not_cached`: 일부 출처는 본문을 직접 확인했으나 asset로 캐시하지 않았다.
`inaccessible`: 일부 출처(예: Uncanny "Let Me Tell You")는 403으로 접근 불가.

## A. 비약 없는 노출 기법 (craft)

| 기법 | 핵심 | SAGA 적용 |
| --- | --- | --- |
| Incluing (Jo Walton) | 설명 장면 없이 세계 정보를 행동·소품·관용어에 흩뿌려 독자가 모르게 흡수 | 복원·비트코인 유물 규칙을 인물의 일상 행동·물건 속에 녹인다 |
| AYKB 안티패턴 회피 | "알다시피 …잖아" 식 상호 설명 금지 | 같은 정보를 인물이 규칙에 **부딪히는 사건**으로 전환 |
| Show/Tell 균형 (Ann Leckie) | 인물·계급은 보여주되, 제도·역사 배경은 짧고 명료한 직접 서술이 더 빠를 수 있음 | 페이싱 위해 배경은 한 문단 직접 서술 허용 |
| 정보 유보 | 독자가 원하기 전엔 주지 않음. 주인공을 독자와 같은 무지에 둠 | 복원의 진짜 대가를 주인공도 모르게, 알아내는 과정을 보상으로 |
| MICE-Inquiry (Kowal) | 질문으로 열고 답으로 닫음 | "비트코인은 왜 유물이 되었나"를 챕터 추진 질문으로 |
| 테드 창식 구조-개념 일치 | 서술 형식·장면 배치 자체가 개념을 체험시킴; 친숙한 사례로 닻 | "신뢰 붕괴"를 장면 구조로 체험시키고 자물쇠/열쇠로 닻 |
| 구체→추상 (학습과학) | 추상 규칙은 구체물로 먼저 닻 내린 뒤 도입 | 모든 규칙을 만질 수 있는 물건(낡은 지갑, 묘비, 열쇠 한 쌍)으로 먼저 |

출처(접근 상태): Ann Leckie "Show, Don't Tell"(hit), IndieCat 테드 창 분석(hit),
Wikipedia Exposition/Infodumping(partial), Writing Excuses MICE(partial),
학습과학 구체예시 연구(partial).

## B. 비트코인 붕괴를 비약 없이 설명하는 5단 사다리

중·고생 독자도 따라오는 설명 순서. prose에서는 한꺼번에 풀지 말고 incluing으로
나눠 흘린다.

```text
① 공개키 = 자물쇠 사진,  개인키 = 그 자물쇠를 여는 열쇠.
② 옛 세계: 사진만 보고 열쇠를 깎으려면 우주 나이보다 오래 걸린다 (그래서 안전).
③ 역연산 기계가 등장: 사진만으로 열쇠를 몇 분 만에 깎는다.
④ 자물쇠는 그대로다. 깨진 것은 "되돌릴 수 없다"는 전제다.
⑤ 그래서 불변의 원장은, 죽은 모든 사람의 금고가 동시에 열린 박물관이 된다.
```

기술 배경(중·고생용 최소): 비트코인은 공개 분산원장이고, 각 블록의 hash가 앞
블록과 연결되어 한 글자만 바뀌어도 들통난다(불변성). 안전성은 "공개키→개인키
역산이 사실상 불가능"하다는 전제에서 온다. 그 전제가 깨지면(SAGA의 역연산 문명,
현실의 Shor 알고리즘류 위협) 서명·소유·불변성이 동시에 무너진다.

출처: bitcoin.org how-it-works(partial), River cryptography(partial),
Ledger 양자 위협(partial), CoinDesk(2026) 양자 대비(partial).

## C. 세계 규칙을 받치는 실제 정치·경제 앵커

세계 규칙 4개에 실제 이론·법을 1:1로 차용한다(redact: 출처는 prose에 드러내지 않고
구조만 녹인다).

| 세계 규칙 | 실제 앵커 | 차용 포인트 |
| --- | --- | --- |
| 모든 기적엔 제도가 필요 | 공유지 인클로저 / 본원적 축적(Marx) | 복원·기록 권한을 공유 자원에서 법의 외형으로 사유화한 원죄 |
| 기록/복원이 권력 | 잊힐 권리 GDPR 17조 + 사후 데이터 | 삭제권은 산 자만, 죽은 자는 기본값이 "보존" → 복원 거부권 갈등 |
| 기술이 계급을 만든다 | 감시자본주의(Zuboff)·데이터 식민주의(Couldry&Mejias) | 죽은 자의 기억을 행동잉여로 채굴, "구원·추모" 이데올로기로 정당화 |
| 죽은 자가 산 자를 지배 | mortmain "죽은 손"·영구구속금지·escheat | 현실 법은 죽은 손을 **금지**했다 → 이 세계는 그 반대를 택함 |
| 화폐가 통제 수단 | 회사 화폐(scrip)·컴퍼니 타운 | 복원 크레딧을 한 기관 안에서만 통용시켜 시민을 묶음 |

출처(접근 상태): Marxist.com 인클로저(partial), GDPR Art.17 / MediaLaws 사후
잊힐권리(partial), Zuboff PDF(partial), Couldry&Mejias LSE PDF(partial),
Cornell Wex Mortmain·Wikipedia Rule against perpetuities(partial),
Wikipedia Company scrip(partial).

## D. 적용 규칙

1. 위 앵커는 prose에서 **이름을 대지 않는다**(redact). 구조·결과만 장면에 녹인다.
2. 비트코인 5단 사다리는 한 장면에 몰아넣지 말고 incluing으로 분산한다.
3. 새 용어(Last Archive, Ledger House 등)는 처음 나올 때 한 줄로 **무엇인지**
   닻을 내린다(갑툭튀 금지). 닻은 설명이 아니라 인물의 반응·구체물로.
4. 모든 추상은 구체물 먼저. 강의 대사("…란 …이다") 금지.

## Next Use

이 자료는
[비트코인 독자 접근성 + 실제 이론 앵커 bible](../10_universes/qfuds-verse/10_world/106_reader_accessibility_and_real_world_anchors_ko.md)과
첫 arc 오프닝 퇴고가 집행한다.
