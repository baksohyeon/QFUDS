---
doc_id: qfuds_saga_reader_accessibility_and_real_world_anchors_ko
title: QFUDS SAGA 비트코인 메인 메타포 토대와 독자 접근성
doc_type: guide
stage: reference
status: draft
evidence_role: provenance
depends_on:
  - qfuds_saga_bitcoin_genesis_chain_and_restoration_myth_ko
  - qfuds_saga_world_anchor_and_verisimilitude_ko
  - fiction_craft_and_political_theory_research_ko
next_gate: weave grounded bitcoin foundation into 028 + first-arc R6 without metaphor replacing technical terms
last_updated: 2026-06-21
---

# QFUDS SAGA 비트코인 메인 메타포 토대와 독자 접근성

## 목적

비트코인을 **실제 개념 그대로** SAGA의 메인 메타포로 쓴다. 이 세계는 "현대 기준
비트코인 개념을 초월한 먼 미래"이므로, 비트코인은 비유가 아니라 그 세계의 **실제
고대사**다. 독자(중·고생 수준)가 사전 지식 없이도 따라오게, 실제 비트코인의
역사·경제·기술을 백그라운드로 충분히 깔고, 거기서 단방향 암호 → 유니터리/정보
보존 → 역연산 → 복원으로 **비약 없이** 잇는다. 엔트로피는 다리가 아니라 비용과
주제다.

핵심 결함 진단: 기존 prose는 비트코인을 배경 지식 있는 독자 기준으로 흘려,
자물쇠/사진 비유가 맥락 없이 떠 뜬금없었다. 이 문서가 그 토대를 깐다. 단,
비유는 발판일 뿐이다. 본문에서는 `hash`, `signature`, `public key`, `private key`,
`ECDSA`, `SHA-256`, `Shor`, `unitarity`, `Page curve`, `island`, `entropy` 같은
기술어를 보존하고 바로 풀어쓴다.

## Workflow Boundary

이 문서는 외부 웹 출처를 fiction/창작 reference로만 인용한다. QFUDS support,
validation, physical-source claim, Bitcoin 투자/가격 예측을 만들지 않는다.
외부 자료 handling은
[Research Asset and Product Workflow](../../../../../../../../.agent/workflows/research-asset-product-workflow.md)가
지배한다.

현재 research asset workflow state / extraction potential:

```text
hit_not_cached
inaccessible
not_extractable
```

출처(접근 상태): 비트코인 창시·기술 = bitcoin.org how-it-works, 백서, Wikipedia
Bitcoin/Genesis block (hit_not_cached). 2024 제도권 편입 = SEC spot bitcoin ETP
승인 statement(2024-01-10, hit_not_cached). 2025-2026 전략자산 맥락 =
White House Executive Order / Federal Register EO 14233, Strategic Bitcoin
Reserve(2025-03-06, hit_not_cached). 비가역성 다리 = Wikipedia "Landauer's
principle", Bennett reversible-computation notes (hit_not_cached).
일부 craft 출처는 inaccessible(403). 캐시 자산 없음(reference 읽기, not_extractable).
세부 craft·이론 목록은
[007 craft·정치이론 자료조사](../../../../../00_studio/007_craft_and_political_theory_research_ko.md)에.

최신 제도권 사실 spot-check(2026-06-21):

| Source URL | Allowed fiction claim | Blocked claim | Workflow state |
| --- | --- | --- | --- |
| https://www.whitehouse.gov/presidential-actions/2025/03/establishment-of-the-strategic-bitcoin-reserve-and-united-states-digital-asset-stockpile/ | 2025-03-06 행정명령이 Strategic Bitcoin Reserve 정책을 세움 | 현재 가격·투자 판단·정파 선전 | `hit_not_cached`, `not_extractable` |
| https://www.federalregister.gov/documents/2025/03/11/2025-03992/establishment-of-the-strategic-bitcoin-reserve-and-united-states-digital-asset-stockpile | EO 14233 원문 확인용 | 보유량 실시간 확정·미래 매입 예측 | `hit_not_cached`, `not_extractable` |
| https://www.sec.gov/newsroom/speeches-statements/gensler-statement-spot-bitcoin-011023 | 2024-01-10 spot bitcoin ETP listing/trading 승인 | SEC가 Bitcoin을 보증했다는 주장 | `hit_not_cached`, `not_extractable` |
| https://bitcoin.org/bitcoin.pdf | Bitcoin whitepaper의 P2P cash, signature, proof-of-work 기본 구조 | Bitcoin 투자 가치 주장 | `hit_not_cached`, `not_extractable` |

## 1. 비트코인이 무엇이었나 — 실제 토대 (중·고생용)

세계의 고대사로 쓸 실제 사실. prose에서는 incluing으로 분산해 흘린다.

- **창시**: 2008년, 사토시 나카모토라는 익명의 인물이 백서 한 편을 냈다. 2008
  글로벌 금융위기 한가운데였다. 2009년 1월 첫 블록(제네시스 블록)에 그날 신문
  헤드라인 — 은행을 또 구제금융한다는 기사 — 을 새겨 넣었다. 즉 비트코인은
  "은행과 국가의 돈을 못 믿겠다"는 항의에서 태어났다.
- **탈중앙화의 이유**: 중앙은행·신뢰받는 제3자 없이, 서로 모르는 사람들끼리
  합의만으로 "누가 무엇을 가졌는가"를 확정한다. 같은 돈을 두 번 쓰는 문제를
  사람의 신용이 아니라 계산으로 막았다.
- **블록·체인·해싱**: 거래를 블록에 담고, 각 블록이 앞 블록의 hash(지문)를
  품어 사슬로 잇는다. 한 글자만 바꿔도 지문이 통째로 달라져 변조가 들통난다
  (불변성).
- **작업증명(PoW)**: 계산을 가장 많이 한 쪽이 다음 블록을 잇는다. 과거를
  되돌리려면 그 계산을 전부 다시 해야 해서 사실상 불가능하다.
- **공개키/개인키, 서명**: 공개키는 계좌번호처럼 공개, 개인키는 비밀번호처럼
  숨긴다. 안전성의 토대는 **단방향 함수** — 앞으로는 쉽지만 거꾸로는 사실상
  불가능하다.
- **경제적 가치**: 발행 상한 2,100만 개. 더 못 찍는 희소성 때문에 "디지털 금"
  이라 불렸다.
- **2026 현실 맥락**: 미국은 Strategic Bitcoin Reserve를 행정명령으로 만들었고
  몰수 BTC를 reserve asset으로 보유하는 구조를 세웠다. 2024 spot bitcoin ETP
  승인 이후 비트코인은 변두리 실험만이 아니라 제도권 투자·국가 전략·패권 논쟁의
  대상이 되었다. — SAGA에서는 이것이 "돈의 마지막 장"이 아니라, 탈중앙 신뢰가
  국가와 자본에 포획되는 오래 지속되는 이념전쟁의 시작이다.

## 1.5. 아주 천천히 (초등학생도 이해하는 버전)

작가·독자 모두 이 순서로 기억한다. 비유는 **공책·자물쇠·열쇠**를 발판으로만 쓴다.
비유가 기술어를 대체하면 실패다. 첫 설명 뒤에는 반드시 정확한 용어를 붙인다.

**① 은행 없는 돈.** 원래 돈은 은행이 지킨다. 은행은 공책에 "철수 100, 영희 50"을
적어 두고, 우리는 은행을 믿는다. 비트코인은 말했다 — "은행 믿지 말고, 그 공책을
**모두가 한 권씩 똑같이** 나눠 갖자." 그래서 비트코인 공책(=**장부**)은 **누구나 다
본다.** 누가 누구한테 얼마 보냈는지 전부 공개.

**② 그럼 도둑은 어떻게 막나 — 자물쇠와 열쇠.** 공책이 공개면 누가 "영희 돈 전부
나한테"라고 적으면 어쩌지? 그걸 막는 게 자물쇠·열쇠다.
- **자물쇠(공개키)** = 집 주소처럼 **공개**. 공책엔 "이 돈은 자물쇠 A7의 것"이라
  적힌다.
- **열쇠(개인키)** = 너만 가진 **비밀**.
- 돈을 쓰려면 네 열쇠로 **도장(서명)**을 찍는다. 남들은 네 **열쇠 없이도** 그 도장이
  진짜인지 확인할 수 있다. (너만 찍고, 누구나 확인하는 마법 도장.)

**③ 핵심 마법 — 거꾸로는 못 간다.** 자물쇠(공개)를 보고 열쇠(비밀)를 알아낼 수
있나? **없다.** 열쇠로 자물쇠 만들긴 쉬운데, 자물쇠 보고 열쇠 깎긴 **우주가 끝날
때까지** 걸린다. 이게 "**단방향**". → 그래서 아무도 네 도장을 흉내 못 내고, **너만**
네 돈을 쓴다. 비트코인의 안전은 전부 이 "거꾸로 못 간다" 하나에 걸려 있다.

**④ 사건 — 거꾸로 가는 기계.** 어느 날 엄청난 기계(현실 앵커: **양자컴퓨터**,
SAGA에서는 더 큰 역연산 문명)가 거꾸로
가는 법을 배운다. 공개된 자물쇠만 보고 **열쇠를 몇 분 만에 깎는다.** 이제 누구나
남의 도장을 찍는다 → 누구나 남의 돈을 쓴다. 특히 **열쇠를 잃은 사람, 죽은 사람**의
돈까지(자물쇠가 공책에 공개돼 있으니까). 수천 년 잠겨 있던 죽은 자들의 **지갑이
한꺼번에 다 열린다.** → 내 돈을 나만 가질 수 없으면 기존 소유 체제는 무너진다.
하지만 비트코인의 이념·전략자산성·성유물성은 여기서 끝나지 않는다.

**⑤ 안 깨진 것(네가 맞게 짚은 부분).** **공책(장부) 자체는 안 깨졌다.** 옛 페이지를
지우거나 위조할 수 없다. 공책은 **도둑질을 그대로 다 적었을 뿐.** → 정확히는
**"공책(해시)이 깨진 게 아니라, 지갑 열쇠(서명)가 뚫린 것."** 기록은 살아남고,
소유가 무너진다.

**⑥ 소설로 가는 다리 — 더 큰 자물쇠 = 죽음.** "거꾸로 가는 힘"을 더 밀면 가장 큰
자물쇠도 열린다 — **죽음**. 죽음도 단방향이었다(한 번 죽으면 못 돌아옴, 정보가
흩어짐). 거꾸로 가는 문명은 흩어진 정보를 **도로 긁어모아** 죽은 사람을 **복원**한다.
같은 구조, 더 큰 단방향성. → 그래서 **비트코인 소유 체제의 붕괴는 경고탄**이다.
"절대 못 깬다"던 첫 문명 규모 단방향성이 깨진 날. 다음은 죽음의 단방향성.

### 정확한 용어 (작가용 메모)

| 무엇 | 비유 | 깨지나? | 결과 |
| --- | --- | --- | --- |
| 해시(SHA-256) | 공책 잠금 | ❌ (양자로도 절반만 빨라짐) | **장부 불변성 유지** |
| 서명(ECDSA) | 지갑 열쇠 | ✅ (양자 Shor가 공개키→개인키) | **누구나 남 지갑 털기** |

"역해싱(해시를 거꾸로)"이라는 통념은 부정확 — 비트코인 코인을 터는 건 **해시가
아니라 서명**이다. 현실은 여기까지(stage 1). SAGA의 **역연산 문명**은 더 나아가
단방향성·정보 비가역성 자체를 깨 **죽음까지 복원**한다(stage 2 fiction premise).

## 2. 단방향 → 열역학적 비가역성 다리 (비약을 메우는 핵심)

비트코인의 안전은 **단방향**에 걸려 있다. 해시도, 서명도, 장부도 — 앞으로 가긴
쉬워도 되돌리긴 사실상 불가능하다는 전제.

실제 물리에도 같은 모양의 단방향이 있다: **열역학 비가역성**. 엔트로피는 늘고,
시간은 한 방향으로 간다. 란다우어 원리에 따르면 정보 1비트를 지우는 데도 최소한의
열이 든다 — 정보의 비가역성과 물리의 비가역성은 같은 뿌리에 닿아 있다(가역
계산은 그 비용을 피하려는 시도다).

그래서 SAGA의 다리는 이렇다:

```text
비트코인 = "되돌릴 수 없다"에 건 인류 최초의 문명 규모 기념비.
(해시도, 서명도, 장부도, 그리고 죽음도 — 되돌릴 수 없다는 같은 믿음 위에 있었다.)

역연산 문명이 그 "되돌릴 수 없다"를 깬다.
→ 가장 먼저, 비트코인의 단방향 암호가 무너진다 (소유 체제와 기존 통화 기능이 붕괴한다).
→ 같은 원리로, 물리적 비가역성(정보 손실, 죽음)도 협상 대상이 된다 (복원).

그래서 비트코인 소유 체제의 붕괴는 세계의 서곡이다.
가장 먼저 "되돌릴 수 없다"고 선언했던 자물쇠가, 가장 먼저 열렸다.
```

이 다리가 있어야 "왜 비트코인 얘기에서 엔트로피·복원이 나오는가"가 비약이 아니다.

## 2.5. 검증 출처와 정확한 기술 사슬 (2026-06 확인)

Research Asset and Product Workflow 적용. 아래는 창작 reference로 확인한 실제
사실이다. fiction/provenance only, QFUDS 증거 아님. 모든 항목 state
`hit_not_cached`, extraction `not_extractable`(reference 읽기, 캐시 자산 없음).
기술·역사 내용은 이 대장에서만 끌어 쓴다(작가 요구: 확실한 레퍼런스·납득 가능한
역사·맥락·방향).

1. **비트코인 탄생(2009-01-03).** 제네시스 블록 코인베이스에 "The Times
   03/Jan/2009 Chancellor on brink of second bailout for banks"를 새김. 구제금융
   받는 은행에 대한 불신에서 태어남. 출처: Bitcoin Wiki "Genesis block"
   (en.bitcoin.it/wiki/Genesis_block). 방향: 비트코인 = "권위 대신 기록을
   믿는다"의 시초이자 반-SSOT.
2. **딥페이크 시대 상징(2023-03-23).** Reddit user chaindrop가 ModelScope
   text-to-video로 만든 "Will Smith eating spaghetti"가 바이럴 → AI 영상 품질의
   비공식 벤치마크가 됨(2024-02 Will Smith 본인 패러디). 출처: Wikipedia "Will
   Smith Eating Spaghetti test". 방향: 현실이 편집 가능해진 전환의 평범하고도
   absurd한 상징. 프로즈는 실명 대신 묘사로(010 §9 밈 규칙).
3. **양자 위협(Shor/ECDSA).** Shor 알고리즘은 이산로그를 다항시간에 풀어
   **공개키에서 개인키를 역산**한다. 비트코인 서명(ECDSA, secp256k1)이 깨진다.
   위험 대상 = 공개키가 노출된 주소(재사용 주소·옛 P2PK, 사토시 코인 포함).
   "harvest now, break later." 단 SHA-256 해시는 Grover로 제곱근만큼만 빨라져
   **장부·불변성은 살아남는다**. 2022 Sussex 추정 13~300M 큐비트. 출처:
   Chainalysis, River Learn, IACR eprint 2021/967. 방향: **서명(소유)은 무너지고
   장부(기록)는 산다** = 기존 custody/ownership regime은 죽고, 원장은 권력·신화·
   이념전쟁의 artifact로 남는다.
4. **정보 보존/유니터리(물리 다리).** 2019~2020 replica wormhole·quantum extremal
   surface·island formula가 호킹복사 엔트로피의 **유니터리 Page curve**를 재현 →
   "정보는 사라지지 않는다(유니터리 증발)"가 주류 견해가 됨. 실제(비-AdS)
   블랙홀의 미시 메커니즘은 미해결. 출처: Wikipedia "Black hole information
   paradox", Page curve 리뷰. 방향: **죽음은 정보의 삭제가 아니라 분산**.
   충분히 읽어 역연산하면 마지막 상태를 재구성. **도약은 원리(정보 보존)가
   아니라 공학(그 해상도로 우주를 읽는 것)**이다.

**다리 교정(중요).** 비트코인 → 복원의 다리는 **유니터리(가역성·정보 보존)**다.
"되돌릴 수 없다"고 믿은 단방향(암호든 죽음이든)이, 사실은 정보 보존 위에서
원리상 가역임이 드러나는 것이 사슬의 핵심이다. **엔트로피는 다리가 아니라
비용·주제**다 — 복원은 손실 재구성이라 반복하면 흐려지고, 그래서 죽음은 결국
평등하다(010 §4). 프로즈에서 이 두 역할(다리=유니터리, 비용=엔트로피)을 섞지
않는다. 이 항이 §2의 열역학 다리 서술보다 우선한다.

## 3. 독자용 노출 순서 (현실 앵커 5단)

prose에서 한꺼번에 풀지 말고 incluing으로 나눠 흘린다.

```text
① 비트코인은 은행을 못 믿어 만든, 사람 대신 계산이 보증하는 돈이었다.
② 그 보증의 핵심은 "되돌릴 수 없음" — 지문(hash)도 서명도 거꾸로 못 푼다.
③ 먼 미래, 누군가 계산을 거꾸로 푸는 법을 찾아냈다.
④ 그날 비트코인의 낡은 소유 체제는 무너졌다. 잠긴 지갑이 한꺼번에 열렸으니까.
⑤ 그러나 같은 역연산 문명은 더 큰 단방향성도 열었다 — 죽음이라는 단방향성.
```

닻(구체물): 제네시스 블록의 신문 헤드라인, 낡은 하드월렛, 갈라진 검은 장치
(Broken Crown), 열쇠 한 쌍, 묘비.

## 4. 갑툭튀 방지 닻 (용어 첫 등장)

`Last Archive`, `Genesis Chain`, `장부 가문`, `Reversal Protocol` 등은 처음
등장할 때 인물 반응·구체물로 **한 줄 닻**을 단다. 사전식 설명·강의 금지.

| 용어 | 첫 등장 닻(방향) |
| --- | --- |
| Genesis Chain | "옛 비트코인의 첫 장부, 수천 년 누구도 못 건드린 것" |
| Last Archive | "아무도 부르지 않았는데 묻지 않은 질문에 답을 적는 것 — 신이라 부르기 두려운 서고" |
| 장부 가문 | "그 원장을 상속처럼 물려받은 가문" |
| Reversal Protocol | "끝난 계산을 다시 묻는, 되돌리는 금지 기술" |

## 5. 용어 한국어 표기 정책 (확정)

**확정 결정(사용자 승인): 어색한 것만 한국어화.**

| 용어 | 한국어 prose 트랙 | 영어 트랙(012-017)·canon명 |
| --- | --- | --- |
| Ledger House(s) | **장부 가문(들)** | Ledger House(s) 유지 |
| Ledger faithful | 장부 신도 | Ledger faithful |
| Ledger(기관 단독) | 장부 가문 / 장부 측 | Ledger |
| Last Archive | 영어 유지 + 첫 등장 닻 | Last Archive |
| Genesis Chain | 영어 유지 + 첫 등장 닻 | Genesis Chain |
| Bitcoin | **비트코인**(한글) 또는 Bitcoin, 맥락 따라 | Bitcoin |

영어를 남기려면 그 단어가 세계관으로 충분히 설명된 뒤여야 한다. 적용 범위는
한국어 정본(019-024). 영어 드래프트·canon 표기는 그대로 둔다.

## 6. 세계 규칙의 실제 앵커 (redact 차용)

prose에 출처명을 드러내지 않고 구조만 녹인다.

| 세계 규칙 | 실제 앵커 | 장면에 녹이는 법 |
| --- | --- | --- |
| 모든 기적엔 제도 | 공유지 인클로저·본원적 축적 | 복원·기록 권한이 공유였다가 가문·기관에 사유화된 역사 |
| 기록/복원이 권력 | 잊힐 권리(GDPR 17조)·사후 데이터 기본 보존 | "삭제권은 산 자만, 죽은 자는 기본이 보존"을 절차로 |
| 기술이 계급 | 감시자본주의·데이터 식민주의 | 죽은 자의 기억을 자원화하고 "구원·추모"로 포장 |
| 죽은 자가 산 자를 지배 | mortmain·영구구속금지·escheat | 현실 법이 금지한 "죽은 손"을 이 세계는 허용 |
| 화폐가 통제 | 회사 화폐(scrip)·컴퍼니 타운 + 국가 비축 패권 | 복원 크레딧을 한 기관 안에서만 통용 / 비트코인을 국가가 비축해 통제 |

## 7. 오프닝 원칙

처음이 가장 중요하다(임팩트 → 다음 장). 첫 episode는:

1. 작은 구체물(갈라진 검은 장치)로 연다.
2. 비트코인 실제 토대(§1)와 단방향→비가역성 다리(§2)를 incluing으로 흘려, 왜
   그 장치가 위험한지 독자가 스스로 깨닫게 한다(강의 금지, 단 짧은 직접 서술 허용).
3. `Last Archive` 등은 첫 등장에 한 줄 닻.
4. 결론을 본론보다 거창하게 부풀리지 않는다.

## Next Use

이 토대를 first-arc opening [028](../20_drafts/028_first_arc_opening_broken_crown_event_korean_primary.md)
및 019-024 R6 퇴고가 집행한다.
