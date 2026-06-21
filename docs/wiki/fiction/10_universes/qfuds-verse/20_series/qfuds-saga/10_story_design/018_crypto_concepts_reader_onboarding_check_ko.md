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
last_updated: 2026-06-21
---

# QFUDS SAGA 암호 개념 독자 온보딩 점검

## 1. 문서 역할과 boundary

이 문서는 1부 origin 원고 진입 전, 비트코인·블록체인·암호 개념이 일반 독자에게
장면 압력으로 전달되는지 점검한다. 원고 산문이 아니며 새 설정을 만들지 않는다.

기준 문서:

- [016 origin outline](016_first_arc_origin_outline_ko.md)
- [017 origin scene cards](017_first_arc_origin_scene_cards_ko.md)
- [013 Cryptographic Death 상세 설정](../00_bible/013_cryptographic_death_era_and_crypto_concepts_ko.md)
- [007 Hash Covenant](../00_bible/007_cryptographic_death_and_hash_covenant_ko.md)
- [017 Bitcoin 위상](../00_bible/017_bitcoin_stature_ideology_deeptime_ko.md)
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
장면 안에서 한 번 더 물건/행동으로 고정해야 한다.** 기술 개념 설명은 숨기지 말고,
“왜 이 사람이 지금 잃는가”와 붙여야 한다.

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

## 3. 핵심 개념 최소 정의

| Concept | 작품 안 최소 정의 | 설명 강도 |
| --- | --- | --- |
| public key | 모두가 볼 수 있는 자물쇠 모양. 평소엔 안전하지만 Q-Day에는 그 모양이 표적이 된다 | 반드시 설명 |
| private key | 지갑의 코인을 움직일 수 있게 해 주는 비밀 서명 열쇠 | 반드시 설명 |
| signature | 비밀키로 찍는 이동 허가 도장. 장부는 이 도장이 진짜인지 공개키로 확인한다 | 반드시 설명 |
| wallet | 코인이 들어 있는 상자라기보다, 장부 위 코인을 움직일 수 있는 권한 묶음 | 반드시 설명 |
| ledger | 모두가 보는 거래 공책. 누가 얼마를 보냈는지 남고, 고치면 지문이 틀어진다 | 반드시 설명 |
| hash | 기록의 지문. 내용이 바뀌면 지문도 바뀌어서 몰래 고치기 어렵다 | 설명하면 좋음 |
| consensus | 여러 사람이 같은 장부를 진짜로 인정하는 상태 | 장면으로 보여줘도 됨 |
| verification | 어떤 서명·기록·복원이 맞다고 도장을 찍는 절차 | 반드시 설명 |
| one-wayness / irreversibility | 자물쇠 모양은 볼 수 있어도 열쇠는 만들 수 없다는 약속 | 반드시 설명 |
| reverse computation / Q-Day threat | 그 약속이 깨져 공개된 자물쇠 모양에서 열쇠를 깎을 수 있게 되는 날 | 반드시 설명 |

## 4. 각 개념의 첫 등장 위치와 장면화 방식

| Concept | 현재 첫 등장 후보 | 장면화 방식 | 점검 |
| --- | --- | --- | --- |
| public key | 017 B1 threat / B3 threat, 029 prologue에 이미 교육 화면 있음 | “서명하면 공개키가 장부에 뜬다”를 화면 경고로 보여줌 | B1에서 한 문장 손잡이 필요 |
| private key | 016 B1/B4, 017 B3-B4 | 망명 자금을 움직이는 서명 열쇠 | 충분 |
| signature | 016 B1 catch-22, 017 B1 impossible choice | send 버튼을 누르려면 서명해야 함 | 충분하나 “전송=서명”을 B1에서 명시 |
| wallet | 016 §5, 017 B1 | 단순 재산이 아니라 망명 자금+신분 회복 열쇠 | 충분 |
| ledger | 016 §5, 013 A1-A3, 029 교육 화면 | 모두가 보는 장부라 노출이 공적 사건이 됨 | B1에서 “모두가 보는 장부” 한 손잡이 권장 |
| hash | 013 B2, 029 교육 화면 | 장부 페이지의 지문 | B1에는 불필요, B3 이후 가능 |
| consensus | 013 A5, 017 Bitcoin bible | 모두가 같은 장부를 인정함. 나중에 Last Archive와 주제 연결 | 1부 B1에는 설명 금지, B6/B7 또는 후속에서 충분 |
| verification | 016 B2-B4, 017 B2-B4 | 사엘의 seal/provisional seal/audit record | 충분 |
| one-wayness | 013 A1, 016 B3, 017 B3 | 중지 키가 안 먹히고 공개키→비밀키 역방향 진행 | 충분하나 technical note 허용 |
| reverse computation / Q-Day | 013 A1-A2, 016 B1-B3, 017 B1-B3 | 내일 기계가 켜지면 공개된 자물쇠들의 열쇠가 깎임 | 충분 |

## 5. B1~B7에서 독자가 헷갈릴 수 있는 지점

| Beat | 헷갈릴 수 있는 지점 | 보강 방향 |
| --- | --- | --- |
| B1 | 왜 전송하면 공개키가 노출되는지 | send 버튼 옆 경고문: “전송하려면 공개 검증 정보가 장부에 남는다” |
| B1 | 공개키가 원래 공개라면서 왜 위험한지 | 평소엔 안전하지만 내일은 자물쇠 사진만으로 열쇠를 깎을 수 있다고 설명 |
| B1 | 지갑이 돈상자인지 권한인지 | 지갑=장부 위 코인을 움직이는 서명권이라고 손잡이 제공 |
| B2 | 사엘이 왜 처리권을 갖는지 | 상급자 봉쇄 + emergency authority/provisional seal이 이미 017에 보강됨 |
| B3 | 역연산이 “해킹”인지 “복원”인지 | 장부를 고친 게 아니라 공개키에서 비밀키 material을 복원한다고 구분 |
| B4 | 사엘 도장이 왜 세계 선례가 되는지 | provisional seal도 audit record로 남아 precedent가 된다는 장치가 017에 있음 |
| B5 | 40만 큐가 숫자 설명으로 보일 위험 | 각 요청이 B1 닮은 파일이라는 반복으로 사람화 |
| B6 | Karvath/Archive 신격화 설명 과다 위험 | UI, seal protocol, 위임 로그로만 보여줌 |
| B7 | 지갑 복원이 왜 사람 복원으로 이어지는지 | 지갑 → 지워진 기록 → 마지막 순간 → 사람의 사다리를 짧고 명확하게 표시 |

## 6. 강의 없이 이해시키는 장면 장치

강의 금지가 아니다. 기술 설명은 허용한다. 다만 설명은 반드시 아래 장치 중 하나에
실려야 한다.

| 장치 | 쓰임 |
| --- | --- |
| send 버튼 | 전송=서명=노출을 한 동작으로 압축 |
| 카운트다운 | Q-Day가 내일이며 선택 지연도 비용임을 표시 |
| 화면 경고문 | 공개키/서명/장부 노출을 짧게 기술 설명 |
| 자물쇠/열쇠 손잡이 | public/private key의 최소 이해 |
| 모두가 보는 공책 | ledger와 consensus의 최소 이해 |
| 장부 지문 | hash의 최소 이해 |
| provisional seal | verification이 권력이 되는 순간 |
| audit record | 왜 사엘의 도장이 나중에 선례로 인용되는지 |
| 큐 숫자+파일 제목 | The Great Drain을 세계 설명 대신 사람들의 요청으로 보여줌 |

## 7. 절대 넣지 말아야 할 설명 방식

- “블록체인이란...”으로 시작하는 백과사전 문단.
- ECDSA·secp256k1 수학을 장면 전개보다 먼저 놓는 방식.
- “양자컴퓨터가 모든 암호를 깬다” 같은 과단순화.
- 공개키가 노출되면 위험하다는 결론만 말하고, 왜 위험한지 장면 선택과 연결하지 않는 방식.
- 비트코인을 죽은 유물로 처리해 사상·합의·권위의 축을 지우는 방식.
- 독자가 “그래서 이 사람이 지금 뭘 잃지?”라고 물어야 하는 설명.

## 8. 1부 원고 진입 전 보강 TODO

| TODO | 대상 | 필요도 |
| --- | --- | --- |
| B1 첫 화면에 public key / signature / ledger 최소 손잡이를 넣는다 | 017 B1 또는 원고 intent card | release-blocking |
| “평소엔 공개키가 안전하지만 Q-Day에는 표적”이라는 대비를 B1 안에서 해결한다 | 017 B1 또는 원고 intent card | release-blocking |
| B3에서 장부 해킹이 아니라 서명권 붕괴임을 구분한다 | 017 B3 | high |
| B4에서 provisional seal이 왜 precedent가 되는지 한 화면/로그로 보여준다 | 017 B4 | already addressed, verify in prose |
| B5 queue 파일 제목을 사람의 손실로 만든다 | 017 B5 | high |
| consensus는 B1에서 강의하지 말고 B6/B7 이후 주제 연결로 미룬다 | 원고 계획 | medium |
| hash는 B1이 아니라 B3 이후 교육 화면/검증 로그에서 짧게 설명한다 | 원고 계획 | medium |

## Appendix. 캐릭터 설계 템플릿 확인 요약

실제 파일 검색 결과, 캐릭터 설계 기반은 이미 있다. 새 템플릿을 만들지 않는다.

| 항목 | 위치 | 필드 |
| --- | --- | --- |
| Character sheet template | [.agent/templates/fiction/character_sheet_template.md](../../../../../../../../.agent/templates/fiction/character_sheet_template.md) | Identity, Role/function, Want, Need, Fear, Wound, Lie, Choice under pressure, Contradiction, Relationship function, Arc, Voice, Knowledge State |
| Work bible cast table | [.agent/templates/fiction/work_bible_template.md](../../../../../../../../.agent/templates/fiction/work_bible_template.md) | Character, Role, Want, Fear, Secret, Voice notes |
| Liora full sheet | [012 Liora](../00_bible/012_character_liora_sen_ko.md) | 상세 인물 시트 |
| Ensemble mini-sheets | [016 ensemble](../00_bible/016_character_ensemble_voices_relationships_ko.md) | 반복 인물 Want/Need/Fear/Wound/Lie/관계 기능 |
| Character depth sheets | [019 depth sheets](../00_bible/019_character_depth_sheets_ko.md) | Liora, Mara, Elias, Noor, Ione, Pell, Karvath, Vera 등 확장 |
| Scene-card archetype gate | [013 scene cards](013_first_arc_scene_cards_ko.md) | scene Want/Obstacle/Turn/Cost, archetype hook gate |

적용 상태:

| Character | 적용 상태 |
| --- | --- |
| Liora | 012 full sheet + 016/019 상속 |
| Mara | 016 mini-sheet + 019 depth sheet |
| Karvath | 019 depth sheet 있음. 1부 origin에서는 직접 POV 금지, 시스템 손자국만 |
| Vera | 019 depth sheet 있음. 1부에서는 회수 금지, 그림자만 |
| Sael | 016/017에서 원죄 기능은 있음. full character sheet는 아직 없음 |

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
