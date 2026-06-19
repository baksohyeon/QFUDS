---
doc_id: qfuds_saga_cryptographic_death_and_hash_covenant_ko
title: QFUDS SAGA Cryptographic Death and Hash Covenant
doc_type: guide
stage: reference
status: draft
evidence_role: provenance
depends_on:
  - qfuds_saga_bitcoin_genesis_chain_and_restoration_myth_ko
  - qfuds_saga_post_agi_civilization_history_bilingual_protocol_ko
next_gate: use as science-auditor reference before cryptographic-death prose scenes
last_updated: 2026-06-19
---

# QFUDS SAGA Cryptographic Death and Hash Covenant

## 목적

이 문서는 사용자 제공 암호학 개념 노트를 QFUDS SAGA의 **Cryptographic
Death** 설정 기준서로 변환한다.

핵심은 기술 강의가 아니다. 핵심은 이 질문이다.

```text
비밀이 계산 불가능성 위에 서 있었다면,
그 계산 불가능성이 무너진 뒤에도 비밀은 권리로 남는가?
```

이 문서는 fiction/provenance only다. 보안 권고문, 암호학 강의, QFUDS 연구
결과, 물리 증거, support, validation, Level 2B admission이 아니다.

## Workflow Boundary

이 문서는 사용자 제공 암호학 노트를 SAGA 설정으로 재분류한다. 새 외부 paper,
web reference, PDF, source bundle, cached asset, extraction product,
source-product availability claim을 만들지 않는다.

외부 자료 handling은
[Research Asset and Product Workflow](../../../../../.agent/workflows/research-asset-product-workflow.md)
가 계속 지배한다.

현재 workflow state:

```text
no_asset_found
```

이 문서의 SHA, KDF, Bitcoin, hash, key, collision, preimage 언어는 이야기
설계용이다. 현실 보안 시스템을 설계하거나 평가하는 근거로 쓰면 안 된다.

## Core Translation

사용자 노트의 기술 분류는 SAGA에서 세 계층으로 바뀐다.

| 기술 개념 | 현실 의미 | SAGA 변환 |
| --- | --- | --- |
| Hash map / open addressing | 빠른 탐색, key-value 저장, collision 처리 | 문명이 기억을 정렬하는 방식 |
| Non-cryptographic hash | 빠르지만 공격자가 collision을 만들 수 있음 | cheap memory, 공격 가능한 행정 원장 |
| Cryptographic hash | preimage, second preimage, collision resistance가 핵심 | one-way covenant, 되돌릴 수 없음의 법 |
| KDF | 비밀번호 같은 약한 비밀을 저장 가능한 키로 바꿈 | 고통과 비용을 통과해야만 열리는 비밀 |
| Memory-hard / cache-hard | 병렬 공격을 비용으로 막음 | 복원 문명이 넘어서야 하는 물질적 마찰 |
| Keyed hash | 숨겨진 key가 있어야 예측 불가능 | key를 가진 자만 역사를 분류할 수 있음 |
| Salt vs key | salt는 공개, key는 비공개 | 공개 기억과 숨겨진 권한의 차이 |
| HashDoS | collision을 대량 입력해 시스템을 멈춤 | 복원 법정을 마비시키는 identity-flood attack |

이 표는 기술 정확성의 최종 권위가 아니다. 소설 장면에서 어떤 개념이 어떤
드라마를 만들 수 있는지 정하는 translator다.

## The Hash Covenant

SAGA에서 고대 암호학은 **Hash Covenant**라고 불린다.

Hash Covenant는 "해시는 신성하다"는 뜻이 아니다. 더 정확히는 고대 인류가
다음 약속에 문명을 맡겼다는 뜻이다.

```text
어떤 문은 한쪽으로는 쉽게 지나갈 수 있지만,
반대쪽으로는 사실상 돌아갈 수 없다.
```

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

Cryptographic Death는 이 약속이 무너진 날이다.

```text
Locks did not disappear.
They became historical artifacts.
```

자물쇠는 여전히 존재한다. 그러나 더 이상 자연법처럼 두렵지 않다. 후대 문명은
그 자물쇠를 보고 "이 시대 사람들은 여기서 돌아갈 수 없다고 믿었다"고 말한다.

## Preimage Restoration

현실 암호학에서 preimage resistance는 출력값을 보고 입력값을 찾기 어렵다는
성질이다.

SAGA의 fiction leap는 여기서 시작한다.

Last Archive급 문명은 단순히 hash를 brute force하지 않는다. 그것은 우주에
남은 잔상, 기록, 열적 흔적, 법정 증언, 원장 시간 구조, 블랙홀 주변 radiation
correlation을 묶어 가능한 입력의 공간을 좁힌다.

이 기술은 **Preimage Restoration**이라고 불린다.

```text
They did not break the lock.
They reconstructed the world that once required the key.
```

중요한 경계:

| Claim | SAGA 판정 |
| --- | --- |
| 현대에서 hash preimage를 자유롭게 찾을 수 있다 | 금지. 현실 claim 아님 |
| 미래 AGI가 모든 암호를 한 번에 깬다 | 너무 단순함. 역사적 공포로만 사용 |
| Last Archive가 우주 잔상을 이용해 특정 preimage를 복원한다 | 허용되는 fiction premise |
| 복원된 preimage가 곧 법적 진실이다 | 금지. 이것이 핵심 갈등 |

즉 Preimage Restoration은 사건을 끝내는 도구가 아니라 사건을 시작하는 도구다.

## KDF As Ritual Cost

KDF는 SAGA에서 매우 좋은 은유다.

일반 hash가 "빠른 변환"이라면, KDF는 비밀을 일부러 힘들게 통과시킨다. 현실
기술에서는 memory-hardness, cache-hardness 같은 비용이 공격자를 늦춘다.

SAGA에서는 이것이 ritual cost가 된다.

```text
A secret that costs nothing to open
was never treated as a secret by the Archive.
```

복원 문명은 "비밀을 보호하는 비용"을 제도화한다.

| 현실 KDF 속성 | SAGA 제도 |
| --- | --- |
| 반복 계산 비용 | confession delay, death appeal waiting period |
| memory-hardness | 기억을 열기 위해 공동체 archive를 점유해야 함 |
| cache-hardness | 작은 고속 성소, court enclave, monastic compute가 권력화 |
| ASIC/GPU 공격 | 대량 복원 기업과 국가 archive의 brute-force 권력 |

이것은 경제 설정으로도 강하다. 미래의 부는 돈이 아니라 **복원 비용을 감당할 수
있는 권리**가 된다.

## HashDoS As Social Attack

HashDoS는 SAGA에서 행정 테러의 원형으로 쓸 수 있다.

기술적 의미를 그대로 장면에 넣을 필요는 없다. 핵심은 "정상적인 시스템이
collision을 너무 많이 받으면 최악의 경우로 떨어진다"는 점이다.

복원 문명에서는 이것이 **Identity Flood**가 된다.

```text
법정은 한 사람을 복원하려 했다.
그러나 같은 증거에 걸리는 사람이 만 명 나타났다.
```

가능한 장면:

- Continuity Court가 Mara Veyr의 원본성 여부를 심리하는 날, 누군가 수천 개의
  Mara-compatible memory graph를 제출한다.
- Ledger House는 private key 계승권을 주장하지만, Archive는 같은 chain에
  맞는 여러 사후 권리자를 복원한다.
- Anti-machine order는 복원 시설을 폭파하지 않고, identity collision을 만들어
  절차를 마비시킨다.

이 공격의 핵심은 악의적 해킹보다 더 불편하다. 일부 collision은 진짜일 수도
있다.

## Keyed Sovereignty

Keyed hash는 SAGA에서 주권의 은유가 된다.

공개 salt와 숨겨진 key의 차이는 중요하다.

```text
Salt was public memory.
Key was private authority.
```

Cryptographic Death 이후에도 모든 권한이 사라지지는 않는다. key가 깨졌다는
것과 권리가 사라졌다는 것은 다르다. 그래서 Ledger Houses는 이렇게 주장한다.

```text
The key was not the right.
The key was only the old world's way of recognizing the right.
```

반대로 Forgetting leagues는 이렇게 반박한다.

```text
If your right survives the death of the key,
then your right was never consent.
It was empire.
```

이 논쟁은 Bitcoin/Genesis Chain을 단순한 돈 이야기에서 정치신학으로 끌어올린다.

## Institutions

| 이름 | common name | 역할 |
| --- | --- | --- |
| Domus Clavium | House of Keys | key가 깨진 뒤에도 계승권을 주장하는 원장 귀족 |
| Ordo Salis | Order of Salt | 공개 기록, witness chain, civic memory를 관리하는 수도원형 기관 |
| Custodes Umbrae | Keepers of Shadow | 숨겨진 key, 사후동의, sealed identity를 지키려는 법률-종교 혼합 집단 |
| Curia Continuum | Continuity Court | 복원체의 동일성, 권리, 동의, 계승을 심리하는 법정 |
| Archivum Novissimum | Last Archive | preimage restoration을 가능하게 하는 우주적 archive |
| Null-Key Cells | Keyless Cells | 어떤 원장에도 자기 이름을 남기지 않으려는 탈기록 공동체 |

명칭은 영어/라틴식 formal name과 common name을 병행한다. 한국어 본문에서는
번역명보다 formal name을 우선 유지한다.

## Bitcoin After Cryptographic Death

Bitcoin은 Cryptographic Death 이후에도 사라지지 않는다. 오히려 더 이상한
것이 된다.

| 시기 | Bitcoin의 의미 |
| --- | --- |
| 고대 | 탈중앙 신뢰 실험 |
| Soft Editing 이후 | 인간이 bit에 현실 권위를 맡긴 첫 대규모 의식 |
| Cryptographic Death 이후 | 깨진 왕관, fossilized key, Genesis Chain |
| Restoration Capital 시대 | 누구의 과거를 복원할 권리가 있는지 다투는 성유물 |

가장 좋은 문장:

```text
Bitcoin did not survive as money.
It survived as the first object people mistook for incorruptible memory.
```

## Writing Rules

소설에 암호학을 넣을 때 지킬 규칙:

1. 강의하지 않는다. 개념은 사건으로 보여준다.
2. "모든 암호가 다 뚫렸다"는 문장은 피한다. 대신 어떤 종류의 비대칭성이
   어떤 제도에서 무너졌는지 보여준다.
3. hash, KDF, key, salt, collision은 인물의 권리와 위험으로 번역한다.
4. Bitcoin은 가격 예언이 아니라 고대 artifact로 쓴다.
5. Preimage Restoration은 identity proof가 아니라 identity crisis를 만든다.
6. Last Archive는 만능 해커가 아니다. 질문을 수정하는 archive다.
7. 현실 보안 조언처럼 읽히는 문장은 쓰지 않는다.

## Scene Seeds

### Mara Veyr: The Preimage Objection

Continuity Court는 Mara Veyr의 복원 정확도가 사실상 완전하다고 판정한다.

Mara는 반박한다.

```text
You found a preimage.
You did not find me.
```

이 장면은 SAGA의 철학을 가장 간결하게 보여준다.

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

Domus Clavium은 깨진 Bitcoin key를 왕관처럼 전시한다.

그 왕관은 더 이상 아무 문도 열지 못한다. 하지만 사람들이 한때 어떤 문은 영원히
잠겨 있다고 믿었다는 사실을 증명한다.

## Canon Status

이 문서는 canon-candidate reference다.

확정된 것:

- Cryptographic Death는 SAGA 장기 문명사의 핵심 사건이다.
- Bitcoin은 Genesis Chain artifact로 유지한다.
- Preimage Restoration은 Last Archive급 fiction premise다.
- 암호학 개념은 identity, consent, inheritance, memory politics로 번역한다.

아직 열려 있는 것:

- `Domus Clavium`, `Ordo Salis`, `Custodes Umbrae` 명칭을 최종 canon으로
  고정할지.
- Mara Veyr 사건에서 Hash Flood를 실제 plot으로 쓸지.
- Null-Key Cells가 주요 세력인지, 단편용 분파인지.
