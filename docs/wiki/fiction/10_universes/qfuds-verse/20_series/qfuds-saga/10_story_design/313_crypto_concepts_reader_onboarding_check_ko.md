---
doc_id: qfuds_saga_crypto_concepts_reader_onboarding_check_ko
title: QFUDS SAGA 암호 개념 독자 온보딩 점검
doc_type: guide
stage: reference
status: draft
evidence_role: provenance
depends_on:
  - qfuds_saga_first_arc_origin_outline_ko
  - qfuds_saga_first_arc_origin_scene_cards_ko
  - qfuds_saga_cryptographic_death_era_and_crypto_concepts_ko
  - qfuds_saga_cryptographic_death_and_hash_covenant_ko
  - qfuds_saga_bitcoin_stature_ideology_deeptime_ko
  - fiction_reader_onboarding_harness_ko
next_gate: revise B1-B7 cards only if this check finds a release-blocking onboarding gap
last_updated: 2026-07-06
---

# QFUDS SAGA 암호 개념 독자 온보딩 점검

## 1. 문서 역할과 boundary

이 문서는 1부 origin 원고 진입 전, 비트코인·블록체인·암호 개념이 일반 독자에게
장면 압력으로 전달되는지 점검한다. 원고 산문이 아니며 새 설정을 만들지 않는다.

기준 문서:

- [311 origin outline](311_first_arc_origin_outline_ko.md)
- [312 origin scene cards](312_first_arc_origin_scene_cards_ko.md)
- [108 Cryptographic Death 상세 설정](../../../10_world/108_cryptographic_death_era_and_crypto_concepts_ko.md)
- [105 Hash Covenant](../../../10_world/105_cryptographic_death_and_hash_covenant_ko.md)
- [110 Bitcoin 위상](../../../10_world/110_bitcoin_stature_ideology_deeptime_ko.md)
- [Reader Onboarding Harness](../../../../../00_studio/010_reader_onboarding_harness_ko.md)

Boundary:

```text
fiction/provenance only
research evidence: no
investment/legal/security advice: no
new external source claim: no
draft prose: no
number cascade: no
```

판정: **B1 콜드오픈은 사전 지식 없이도 작동 가능하지만, 공개키 노출 catch-22는 반드시
정확한 기술 설명, 쉬운 비유, 장면 압력으로 세 번 고정해야 한다.** 기술 개념 설명은
숨기지 말고, 먼저 맞게 설명한 뒤 “왜 이 사람이 지금 잃는가”와 붙여야 한다.

B1의 기본 온보딩 순서:

```text
정확한 설명:
지갑을 옮기려면 서명해야 하고, 그 과정에서 공개키가 장부 위에 드러난다.
평소에는 공개키를 알아도 개인키를 계산할 수 없기 때문에 안전했지만,
Q-Day 이후에는 공개키가 공격 대상이 된다.

쉬운 비유:
비유상 공개키는 집 주소이고, 개인키는 문을 여는 열쇠다.
예전에는 집 주소를 알아도 문을 열 수 없었다.
Q-Day 이후에는 주소만 보고 열쇠를 복사할 수 있게 된다.
도망치려면 문을 열어야 하는데, 문을 여는 순간 주소가 모두에게 보인다.

장면 압력:
전송하면 공개키가 드러나 공격 대상이 된다.
전송하지 않으면 내일 기존 지갑이 통째로 털린다.
도망이 곧 노출이고, 보류가 곧 증발이다.
```

## 2. 독자가 몰라도 되는 것 / 반드시 알아야 하는 것

| 몰라도 되는 것 | 이유 |
| --- | --- |
| ECDSA 수학, secp256k1 곡선 방정식 | 장면 선택 이해에 불필요. B3에서 기술명으로만 노출 가능 |
| SHA-256 내부 구조 | hash가 장부 지문이라는 손잡이면 충분 |
| 블록 생성, 난이도 조정, 채굴 보상 세부 | B1-B7의 직접 압력이 아님 |
| UTXO 모델, 수수료, mempool 세부 | 전송=서명=노출 catch-22만 필요 |
| 양자 알고리즘 세부 | Q-Day 위협은 “공개된 자물쇠 모양에서 열쇠를 깎을 수 있게 됨”이면 충분 |

| 반드시 알아야 하는 것 | 이유 |
| --- | --- |
| 지갑은 돈상자가 아니라 서명할 수 있는 권한에 가깝다 | 법적 소유와 실제 접근이 갈라지는 핵심 |
| 개인키는 돈을 움직이는 서명 열쇠다 | B1/B4의 생존선 |
| 공개키는 평소엔 안전한 공개 자물쇠지만 Q-Day에는 표적이 된다 | B1 catch-22의 핵심 |
| 서명하면 장부가 “이 사람이 움직였다”고 검증할 수 있다 | 전송이 왜 노출인지 이해해야 함 |
| 장부는 모두가 보는 거래 기록이다 | 전송/노출/합의가 왜 공개 사건인지 설명 |
| hash는 기록의 지문이다 | 불가역성과 장부 훼손 방지의 최소 손잡이 |
| consensus는 모두가 같은 장부를 인정하는 상태다 | 비트코인과 Last Archive의 주제 연결 |
| verification은 “맞다” 도장을 찍는 행위다 | 사엘의 오비준이 권력이 되는 이유 |
| one-wayness는 자물쇠에서 열쇠를 만들 수 없다는 약속이다 | 그 약속이 깨져야 Cryptographic Death가 이해됨 |
| reverse computation / Q-Day는 그 약속을 깨는 역사적 사건이다 | B3-B5의 붕괴 엔진 |

## 2.5 QFUDS 1부 온보딩 방식 결정

1부 origin의 기본 온보딩 방식은 **테크노스릴러형 + 인월드 문서형**이다.

이 문서에서는 아래 의미로 쓴다.

| 방식 | 1부에서의 용도 |
| --- | --- |
| 문제 발생형 | B1과 B5. 피해와 선택 압력이 먼저 보이고, 설명은 그 뒤를 따라온다 |
| 짧은 강의노트형 | B2-B4. 사엘이 검증관이므로 기술·절차 설명이 비교적 자연스럽다 |
| 은유 보조형 | B1 공개키 catch-22. 주소/열쇠 비유를 쓰되 정확한 기술 설명을 대체하지 않는다 |
| 전문가 대화형 | B2-B4. 사엘, 상급자, 시스템, 감사 로그 사이의 충돌로 설명한다 |
| 인월드 문서형 | B4, B6, B7. seal protocol, audit record, court exhibit, fieldmark로 제도화를 보여 준다 |
| 반복 노출형 | `seal`, `verification`, `claim`, `recoverable` 같은 제도어에 사용한다 |
| 튜토리얼형 | Petitioner에게 일부만 허용한다. Petitioner는 독자 대리인이 아니라 손실을 가진 사람이어야 한다 |

Beat별 운영:

| Beat | 기본 방식 | 금지 |
| --- | --- | --- |
| B1 | 문제 발생형 + 은유 보조형 + 짧은 정확 설명 | 공개키를 모르는 독자에게 “위험하다”만 던지고 넘어가기 |
| B2-B4 | 짧은 강의노트형 + 전문가 장면 + 인월드 로그 | 독자용 대화처럼 보이는 설명 |
| B5 | 문제 발생형 | 강의, 정의, 제도 해설 |
| B6-B7 | 인월드 문서형 + 반복 노출형 | “검증자가 신이 되었다” 같은 요약 선언 |

## 3. 핵심 개념 최소 정의

| Concept | 정확한 기술 설명 | 쉬운 비유 | 장면 압력 |
| --- | --- | --- | --- |
| public key | 서명이 특정 개인키에서 나왔는지 검증하는 공개 정보. 평소에는 공개키에서 개인키를 계산할 수 없어서 안전하다 | 비유상 집 주소 또는 자물쇠 모양 | B1에서 전송하면 공개키가 장부에 남고, Q-Day 이후 공격 대상이 된다 |
| private key | 코인을 움직이는 서명을 만들 수 있는 비밀 값 | 문을 여는 열쇠 | 잃으면 코인을 움직일 수 없고, 복제되면 남이 코인을 움직인다 |
| signature | 개인키로 만든 승인 증거. 장부는 공개키로 그 서명이 맞는지 확인한다 | 도장 또는 서명 날인 | 전송 버튼을 누르는 순간 승인 증거가 남고, 공개 검증 정보가 따라온다 |
| wallet | 코인이 들어 있는 상자라기보다, 장부 위 코인을 움직일 수 있는 키와 권한의 묶음 | 금고 자체가 아니라 금고 열쇠 꾸러미 | 지갑 이동은 돈상자를 옮기는 일이 아니라 서명권을 써서 장부 상태를 바꾸는 일이다 |
| ledger | 모두가 공유하고 검증하는 거래 기록 | 모두가 보는 거래 공책 | 노출은 사적인 일이 아니라 공개 기록 위에 남는 사건이다 |
| hash | 데이터가 조금만 바뀌어도 달라지는 고정 길이 지문 | 기록의 지문 | 누가 기록을 몰래 바꾸면 지문이 어긋난다 |
| consensus | 참여자들이 같은 장부 상태를 유효하다고 받아들이는 과정/상태 | 여러 사람이 같은 공책을 진짜 장부로 인정함 | 나중에 Last Archive의 “무엇이 진짜인가”와 연결된다 |
| verification | 서명·기록·복원이 규칙에 맞는지 확인하고 유효 판정을 내리는 절차 | 확인 도장 | 사엘의 provisional seal이 사람을 구하는 동시에 권력을 만든다 |
| one-wayness / irreversibility | 공개 정보에서 비밀값을 되돌려 계산하기 어렵다는 암호의 전제 | 주소를 알아도 열쇠를 만들 수 없음 | 그 전제가 깨지는 순간 장부와 소유가 동시에 흔들린다 |
| reverse computation / Q-Day threat | 공개키 같은 공개 정보에서 개인키 material을 역으로 계산할 수 있게 되는 위협 | 주소만 보고 열쇠를 복사하는 날 | B1에서 전송해도 망하고 전송하지 않아도 망하는 시간 제한을 만든다 |

## 4. 각 개념의 첫 등장 위치와 장면화 방식

| Concept | 현재 첫 등장 후보 | 장면화 방식 | 점검 |
| --- | --- | --- | --- |
| public key | 110 B1 threat / B3 threat, 029 prologue에 이미 교육 화면 있음 | “서명하면 공개키가 장부에 뜬다”를 정확한 설명 → 주소/열쇠 비유 → 전송/보류 비용으로 보여줌 | B1에서 3단 온보딩 필요 |
| private key | 205 B1/B4, 110 B3-B4 | 망명 자금을 움직이는 서명 열쇠 | 충분 |
| signature | 205 B1 catch-22, 110 B1 impossible choice | send 버튼을 누르려면 서명해야 함 | 충분하나 “전송=서명”을 B1에서 명시 |
| wallet | 205 §5, 110 B1 | 단순 재산이 아니라 망명 자금+신분 회복 열쇠 | 충분 |
| ledger | 205 §5, 108 A1-A3, 029 교육 화면 | 모두가 보는 장부라 노출이 공적 사건이 됨 | B1에서 “모두가 보는 장부” 한 손잡이 권장 |
| hash | 108 B2, 029 교육 화면 | 장부 페이지의 지문 | B1에는 불필요, B3 이후 가능 |
| consensus | 108 A5, 110 Bitcoin bible | 모두가 같은 장부를 인정함. 나중에 Last Archive와 주제 연결 | 1부 B1에는 설명 금지, B6/B7 또는 후속에서 충분 |
| verification | 205 B2-B4, 110 B2-B4 | 사엘의 seal/provisional seal/audit record | 충분 |
| one-wayness | 108 A1, 205 B3, 110 B3 | 중지 키가 안 먹히고 공개키→비밀키 역방향 진행 | 충분하나 technical note 허용 |
| reverse computation / Q-Day | 108 A1-A2, 205 B1-B3, 110 B1-B3 | 내일 기계가 켜지면 공개된 자물쇠들의 열쇠가 깎임 | 충분 |

## 5. B1-B7에서 독자가 헷갈릴 수 있는 지점

| Beat | 헷갈릴 수 있는 지점 | 보강 방향 |
| --- | --- | --- |
| B1 | 왜 전송하면 공개키가 노출되는지 | 정확한 설명: 지갑을 옮기려면 서명해야 하고 공개 검증 정보가 장부에 남는다 |
| B1 | 공개키가 원래 공개라면서 왜 위험한지 | 쉬운 비유: 평소엔 주소를 알아도 문을 열 수 없지만, Q-Day 이후에는 주소만 보고 열쇠를 복사할 수 있다 |
| B1 | 선택 압력이 왜 catch-22인지 | 전송하면 노출, 전송하지 않으면 기존 지갑이 털림. 도망이 곧 노출이고 보류가 곧 증발 |
| B1 | 지갑이 돈상자인지 권한인지 | 지갑=장부 위 코인을 움직이는 서명권이라고 손잡이 제공 |
| B2 | 사엘이 왜 처리권을 갖는지 | 상급자 봉쇄 + emergency authority/provisional seal이 이미 110에 보강됨 |
| B3 | 역연산이 “해킹”인지 “복원”인지 | 장부를 고친 게 아니라 공개키에서 비밀키 material을 복원한다고 구분 |
| B4 | 사엘 도장이 왜 세계 선례가 되는지 | provisional seal도 audit record로 남아 precedent가 된다는 장치가 110에 있음 |
| B5 | 40만 큐가 숫자 설명으로 보일 위험 | 각 요청이 B1 닮은 파일이라는 반복으로 사람화 |
| B6 | Karvath/Archive 신격화 설명 과다 위험 | UI, seal protocol, 위임 로그로만 보여줌 |
| B7 | 지갑 복원이 왜 사람 복원으로 이어지는지 | 지갑 → 지워진 기록 → 마지막 순간 → 사람의 사다리를 짧고 명확하게 표시 |

## 6. 기술 설명을 장면 압력으로 넘기는 장치

강의 금지가 아니다. 기술 설명은 허용한다. 다만 설명은 먼저 정확해야 하고, 쉬운
비유를 거쳐, 아래 장치 중 하나로 손실과 선택 압력에 실려야 한다.

| 장치 | 쓰임 |
| --- | --- |
| send 버튼 | 전송=서명=노출을 한 동작으로 압축 |
| 카운트다운 | Q-Day가 내일이며 선택 지연도 비용임을 표시 |
| 화면 경고문 | 공개키/서명/장부 노출을 짧고 정확하게 기술 설명 |
| 주소/열쇠 손잡이 | public/private key의 최소 이해. 완전히 같은 구조가 아니므로 비유상으로 처리 |
| 감사 로그 | 전문가 설명을 인월드 문서로 분산 |
| seal protocol excerpt | verification, provisional seal, precedent를 제도 장치로 설명 |
| court exhibit | B4의 임시 도장이 훗날 청구 문서에서 인용되는 과정을 보여줌 |
| Last Archive fieldmark | 설명을 결론이 아니라 제도 문장으로 남김 |
| 모두가 보는 공책 | ledger와 consensus의 최소 이해 |
| 장부 지문 | hash의 최소 이해 |
| provisional seal | verification이 권력이 되는 순간 |
| audit record | 왜 사엘의 도장이 나중에 선례로 인용되는지 |
| 큐 숫자+파일 제목 | The Great Drain을 세계 설명 대신 사람들의 요청으로 보여줌 |

## 7. 절대 넣지 말아야 할 설명 방식

- “블록체인이란...”으로 시작하는 백과사전 문단.
- ECDSA·secp256k1 수학을 장면 전개보다 먼저 놓는 방식.
- “양자컴퓨터가 모든 암호를 깬다” 같은 과단순화.
- 공개키가 노출되면 위험하다는 결론만 말하고, 평소 안전성/Q-Day 이후 위험성/장면
  선택을 연결하지 않는 방식.
- 비유만 남기고 정확한 기술 설명을 생략하는 방식.
- 비트코인을 죽은 유물로 처리해 사상·합의·권위의 축을 지우는 방식.
- 독자가 “그래서 이 사람이 지금 뭘 잃지?”라고 물어야 하는 설명.

## 8. 1부 원고 진입 전 보강 TODO

| TODO | 대상 | 필요도 |
| --- | --- | --- |
| B1 첫 화면에 public key / signature / ledger의 정확한 기술 설명을 짧게 넣는다 | 312 B1 또는 원고 intent card | release-blocking |
| B1 안에서 주소/열쇠 비유로 공개키/개인키/Q-Day를 일반 독자가 잡게 한다 | 312 B1 또는 원고 intent card | release-blocking |
| B1 선택 압력을 “전송=노출 / 보류=증발”로 고정한다 | 312 B1 또는 원고 intent card | release-blocking |
| B3에서 장부 해킹이 아니라 서명권 붕괴임을 구분한다 | 110 B3 | high |
| B4에서 provisional seal이 왜 precedent가 되는지 한 화면/로그로 보여준다 | 110 B4 | already addressed, verify in prose |
| B5 queue 파일 제목을 사람의 손실로 만든다 | 110 B5 | high |
| consensus는 B1에서 강의하지 말고 B6/B7 이후 주제 연결로 미룬다 | 원고 계획 | medium |
| hash는 B1이 아니라 B3 이후 교육 화면/검증 로그에서 짧게 설명한다 | 원고 계획 | medium |

## Appendix. 캐릭터 설계 템플릿 확인 요약

실제 파일 검색 결과, 캐릭터 설계 기반은 이미 있다. 새 템플릿을 만들지 않는다.

| 항목 | 위치 | 필드 |
| --- | --- | --- |
| Character sheet template | [.agent/templates/fiction/character_sheet_template.md](../../../../../../../../.agent/templates/fiction/character_sheet_template.md) | Identity, Role/function, Want, Need, Fear, Wound, Lie, Choice under pressure, Contradiction, Relationship function, Arc, Voice, Knowledge State |
| Work bible cast table | [.agent/templates/fiction/work_bible_template.md](../../../../../../../../.agent/templates/fiction/work_bible_template.md) | Character, Role, Want, Fear, Secret, Voice notes |
| Liora full sheet | [203 Liora](../00_bible/203_character_liora_sen_ko.md) | 상세 인물 시트 |
| Ensemble mini-sheets | [205 ensemble](../00_bible/205_character_ensemble_voices_relationships_ko.md) | 반복 인물 Want/Need/Fear/Wound/Lie/관계 기능 |
| Character depth sheets | [206 depth sheets](../00_bible/206_character_depth_sheets_ko.md) | Liora, Mara, Elias, Noor, Ione, Pell, Karvath, Vera 등 확장 |
| Scene-card archetype gate | [308 scene cards](308_first_arc_scene_cards_ko.md) | scene Want/Obstacle/Turn/Cost, archetype hook gate |

적용 상태:

| Character | 적용 상태 |
| --- | --- |
| Liora | 203 full sheet + 205/206 상속 |
| Mara | 205 mini-sheet + 206 depth sheet |
| Karvath | 206 depth sheet 있음. 1부 origin에서는 직접 POV 금지, 시스템 손자국만 |
| Vera | 206 depth sheet 있음. 1부에서는 회수 금지, 그림자만 |
| Sael | 311/312에서 원죄 기능은 있음. full character sheet는 아직 없음 |

1부 origin의 사엘에게 추가로 필요한 필드:

- Want: B1 사람을 구하려는 직무/충동.
- Need: 검증 도장이 사람을 구하는 동시에 권력을 만든다는 사실을 직시.
- Fear: 자기 비준이 거짓 확신 또는 대량 피해의 시작이 되는 것.
- Wound: 아직 만들지 말 것. 과확장 금지.
- Lie: “절차상 임시 도장은 중립이다.”
- Choice under pressure: 막다 실패 → 구하려고 provisional seal → 보고 버튼을 닫는 침묵.
- Relationship function: 1부 origin과 2부 Mara를 잇는 원죄 참여자.

새 캐릭터 디테일은 여기서 만들지 않는다. 원고 진입 전 필요한 것은 full biography가
아니라 B1-B7에서 선택·비용·지식 상태가 일관되는지 확인하는 것이다.
