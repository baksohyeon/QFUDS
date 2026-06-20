---
doc_id: qfuds_saga_cryptographic_death_and_hash_covenant_ko
title: QFUDS SAGA 암호학적 죽음과 해시 계약
doc_type: guide
stage: reference
status: draft
evidence_role: provenance
depends_on:
  - qfuds_saga_bitcoin_genesis_chain_and_restoration_myth_ko
  - qfuds_saga_post_agi_civilization_history_bilingual_protocol_ko
next_gate: use as science-auditor reference before cryptographic-death prose scenes
last_updated: 2026-06-20
---

# QFUDS SAGA 암호학적 죽음과 해시 계약

## 목적

이 문서는 작가 본인의 암호학 학습 노트를 SAGA 설정으로 정리한다. 목표는
`Cryptographic Death`, `Preimage Restoration`, `Identity Flood`, Bitcoin
Genesis Chain을 장면 설계에 쓸 수 있게 만드는 것이다.

현실 보안 권고가 아니라 작품 설정 기준서다.

**확장:** 대격변(The Hinge Era)의 난리·붕괴·전환점과, 사용자 학습 노트(해시맵·
CHF 4계율·NCHF·KDF 계보·HashDoS/SipHash/djb·Bloom/Cuckoo/XOR 필터)의 상세 매핑은
[013 Cryptographic Death 대격변과 암호 개념 상세 설정](013_cryptographic_death_era_and_crypto_concepts_ko.md)이
보유한다. 이 문서(007)는 핵심 개념 기준, 013은 era 전개 + 용어 사전.

## Source Boundary

이 문서는 작가 본인의 학습 노트를 재분류한다. 새 외부 paper, web reference, PDF,
source bundle, cached asset, extraction product, source-product availability
claim을 만들지 않는다.

외부 자료 handling은
[Research Asset and Product Workflow](../../../../../../../../.agent/workflows/research-asset-product-workflow.md)
가 계속 지배한다.

현재 workflow state:

```text
no_asset_found
```

## 기술어 보존 및 장면 연결표

사용자 노트의 기술 개념은 먼저 기술어로 보존한다. 작중 제도나 사건은 그
기술어가 만든 사회적 결과를 보여 주는 장치다.

| 기술 개념 | 현실 의미 | SAGA 장면 연결 |
| --- | --- | --- |
| Hash map / open addressing | 빠른 key-value 탐색, 충돌 처리 | 기억/신원 record를 정렬하는 행정 기술 |
| Non-cryptographic hash | 빠르지만 공격적 collision에 약함 | cheap ledger, 취약한 시민 원장 |
| Cryptographic hash | preimage, second preimage, collision resistance | 되돌릴 수 없음에 기대는 법적/사회적 약속 |
| KDF | 약한 비밀을 저장 가능한 key로 바꿈 | 비밀을 열기 위한 비용과 대기 시간 |
| Memory-hard / cache-hard | 병렬 공격을 비용으로 막음 | 복원 접근권을 제한하는 물질적 병목 |
| Keyed hash | 숨겨진 key로 예측을 어렵게 함 | 공개 기록과 비공개 권한의 분리 |
| Salt vs key | salt는 공개, key는 비공개 | public memory와 private authority의 차이 |
| HashDoS | collision 대량 입력으로 최악 케이스 유도 | identity-flood attack |

## Hash Covenant

SAGA에서 고대 암호학은 **Hash Covenant**라고 불린다.

뜻은 단순하다. 고대 인류는 어떤 관계가 사실상 한 방향이라고 믿고 문명을
세웠다.

이 약속 위에 세워진 것들:

- private key;
- digital signature;
- password storage;
- blockchain ownership;
- sealed evidence;
- posthumous consent records;
- identity claims;
- archive integrity;
- court-grade proof.

Cryptographic Death는 이 약속이 자연법이 아니라 역사적 한계였음이 드러난
사건이다.

## Preimage Restoration

Preimage Restoration은 Last Archive급 문명이 과거 입력을 복원하려는 기술이다.
단순 brute force가 아니다. 잔상, 기록, 열적 흔적, 증언, 원장 시간 구조,
블랙홀 주변 radiation correlation을 묶어 가능한 입력 공간을 좁힌다.

핵심 경계:

| 주장 | 판정 |
| --- | --- |
| 현대에서 hash preimage를 자유롭게 찾는다 | 쓰지 않음 |
| 미래 AGI가 모든 암호를 한 번에 깬다 | 너무 단순함 |
| Last Archive가 우주 잔상으로 특정 preimage 후보를 복원한다 | 사용 가능 |
| 복원된 preimage가 곧 법적 진실이다 | 사용 금지. 갈등을 없앰 |

즉 Preimage Restoration은 사건을 끝내는 도구가 아니라 사건을 시작하는 도구다.

## KDF와 비용

`KDF`는 기술어로 보존한다. SAGA에서 이 개념은 "비밀을 여는 데 비용이 든다"는
사회적 결과와 연결된다. 그 비용은 계산 시간뿐 아니라 제도, 대기, 접근권,
archive 점유권으로 나타난다.

| 현실 KDF 속성 | SAGA 제도 |
| --- | --- |
| 반복 계산 비용 | death appeal 대기 기간 |
| memory-hardness | 공동체 archive 점유 비용 |
| cache-hardness | 고속 court enclave의 희소성 |
| ASIC/GPU 공격 | 대량 복원 기업과 국가 archive 권력 |

설정상 중요한 점: 미래의 부는 돈이 아니라 복원 비용을 감당할 수 있는 권리다.

## Identity Flood

`HashDoS`는 기술어로 보존한다. `Identity Flood`는 그 구조에서 따온 작중
사건명이다. 정상 시스템이 너무 많은 collision을 받으면 최악의 경우로
떨어진다는 구조만 가져온다.

가능한 장면:

- Continuity Court가 Mara Veyr의 원본성 여부를 심리하는 날, 누군가 수천 개의
  Mara-compatible memory graph를 제출한다.
- Ledger House는 private key 계승권을 주장하지만, Archive는 같은 chain에
  맞는 여러 사후 권리자를 복원한다.
- Anti-machine order는 복원 시설을 폭파하지 않고, identity collision을 만들어
  절차를 마비시킨다.

## Keyed Sovereignty

Keyed hash는 공개 기록과 숨겨진 권한의 차이를 보여주는 장치다.

Cryptographic Death 이후에도 모든 권리가 사라지지는 않는다. key가 깨졌다는
것과 권리가 사라졌다는 것은 다르다. Ledger Houses는 이 틈을 이용한다.

```text
The key was not the right.
The key was only the old world's way of recognizing the right.
```

반대편은 이렇게 본다. key가 죽은 뒤에도 살아남는 권리는 consent가 아니라
제국의 잔여물이다.

## Institutions

| 이름 | common name | 역할 |
| --- | --- | --- |
| Domus Clavium | House of Keys | key가 깨진 뒤에도 계승권을 주장하는 원장 귀족 |
| Ordo Salis | Order of Salt | 공개 기록, witness chain, civic memory를 관리하는 수도원형 기관 |
| Custodes Umbrae | Keepers of Shadow | 숨겨진 key, 사후동의, sealed identity를 지키려는 법률-종교 혼합 집단 |
| Curia Continuum | Continuity Court | 복원체의 동일성, 권리, 동의, 계승을 심리하는 법정 |
| Archivum Novissimum | Last Archive | preimage restoration을 가능하게 하는 우주적 archive |
| Null-Key Cells | Keyless Cells | 어떤 원장에도 자기 이름을 남기지 않으려는 탈기록 공동체 |

명칭은 후보 상태다. 다음 세력 문서 업데이트 전까지 canon 확정으로 보지 않는다.

## Bitcoin After Cryptographic Death

Bitcoin은 가격 예언이 아니라 artifact다.

| 시기 | Bitcoin의 의미 |
| --- | --- |
| 고대 | 탈중앙 신뢰 실험 |
| Soft Editing 이후 | 인간이 bit에 현실 권위를 맡긴 첫 대규모 의식 |
| Cryptographic Death 이후 | 깨진 왕관, fossilized key, Genesis Chain |
| Restoration Capital 시대 | 누구의 과거를 복원할 권리가 있는지 다투는 성유물 |

## Writing Rules

소설에 암호학을 넣을 때 지킬 규칙:

1. 강의하지 않는다. 개념은 사건으로 보여준다.
2. "모든 암호가 다 뚫렸다"는 문장은 피한다. 대신 어떤 종류의 비대칭성이
   어떤 제도에서 무너졌는지 보여준다.
3. `hash`, `KDF`, `key`, `salt`, `collision`은 기술어로 보존한다. 작중에서는
   그 기술어가 권리, 비용, 신원, 절차에 어떤 압력을 주는지 보여준다.
4. Bitcoin은 가격 예언이 아니라 고대 artifact로 쓴다.
5. Preimage Restoration은 identity proof가 아니라 identity crisis를 만든다.
6. Last Archive는 만능 해커가 아니다.
7. 현실 보안 조언처럼 읽히는 문장은 쓰지 않는다.

## Scene Seeds

### Mara Veyr: The Preimage Objection

Continuity Court는 Mara Veyr의 복원 정확도가 사실상 완전하다고 판정한다. Mara는
이렇게 반박한다.

```text
You found a preimage.
You did not find me.
```

### The Hash Flood

Null-Key Cells는 폭탄을 쓰지 않는다. 그들은 court archive에 수천 개의
plausible self를 제출한다.

법정은 묻는다.

```text
Which one is the person?
```

Last Archive는 답하지 않는다. 대신 질문을 고친다.

```text
WHICH ONE HAS THE RIGHT TO BE TREATED AS THE LOSS?
```

### The Broken Crown

Domus Clavium은 깨진 Bitcoin key를 왕관처럼 전시한다. 더 이상 아무 문도 열지
못하지만, 고대 신뢰 체계의 상징으로 남는다.

## Canon Status

이 문서는 canon-candidate reference다.

확정된 것:

- Cryptographic Death는 SAGA 장기 문명사의 핵심 사건이다.
- Bitcoin은 Genesis Chain artifact로 유지한다.
- Preimage Restoration은 Last Archive급 fiction premise다.
- 암호학 개념은 기술어로 보존하고, identity, consent, inheritance, memory
  politics 갈등과 연결한다.

아직 열려 있는 것:

- `Domus Clavium`, `Ordo Salis`, `Custodes Umbrae` 명칭을 최종 canon으로
  고정할지.
- Mara Veyr 사건에서 Hash Flood를 실제 plot으로 쓸지.
- Null-Key Cells가 주요 세력인지, 단편용 분파인지.
