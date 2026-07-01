---
doc_id: qfuds_saga_bilingual_term_discipline_glossary_ko
title: QFUDS SAGA 이중언어 용어규율 글로서리
doc_type: guide
stage: reference
status: draft
evidence_role: provenance
depends_on:
  - qfuds_saga_agentic_system_ko
  - qfuds_saga_post_agi_civilization_history_bilingual_protocol_ko
next_gate: apply to first-arc Korean adaptations 019-024 dejargon polish
last_updated: 2026-07-01
---

# QFUDS SAGA 이중언어 용어규율 글로서리

## 목적

한국어 prose 본문에서 어떤 단어를 영어로 남기고 어떤 단어를 한국어로 옮길지
정하는 집행 기준. SAGA 한국어판이 "영어가 섞인 기계 초안"이 아니라 "한국어
소설"로 읽히게 한다.

이 문서는 운영 스펙이다. 세계관 canon이 아니라, prose를 다듬을 때 적용하는
작가실 규율이다. canon 출처는
[bible 006](../../../10_world/006_post_agi_civilization_history_bilingual_protocol_ko.md)
§Korean-Primary Bilingual Fiction Protocol이다.

## 적용 경계

- 적용 대상: `20_drafts/`의 **한국어 prose 본문**. (예: 019-024, 한국어 프롤로그)
- 비적용: `00_bible/`, `00_workroom/`, `10_story_design/` 등 **운영/설정 문서**.
  이들은 영어 약어 혼용이 허용된다(빠른 참조 목적). 규율은 독자가 읽는 prose에만 건다.
- fiction/provenance only. QFUDS 연구 결과·물리 증거·support·validation 아님.
- 새 외부 source claim 없음. workflow state: `not searched`.

## Canon 규칙 (bible 006 §389-393 재인용)

```text
1. 한국어 본문은 직역투가 아니라 한국어 소설로 읽혀야 한다.
2. 영어판은 한국어판의 literal translation이 아니라 독립 각색판이다.
3. 고유명사, 제도명, 법정 문구, archive response, field mark는 필요하면 영어를 유지한다.
4. 영어 각색판은 특정 작가의 문체를 모방하지 않는다.
```

이 글로서리는 위 규칙 1·3을 실행 가능한 목록으로 옮긴 것이다.

## Keep in English (영어 유지 — 4범주만)

| 범주 | 예 | 이유 |
| --- | --- | --- |
| 고유명사 | Liora Sen, Mara Veyr, Noor Aram, Genesis Chain, Last Archive, Aletheia, Sarqel, Ione, Laur Observatory | 이름·세계 고유 지명/기관명 |
| 제도 분위기어(소수) | Trust, Court, Ledger House, Continuity Court, Keyless Orders, Oblivion Cloisters | 세계의 제도 색을 남기는 최소 집합. 일반화하지 않음 |
| 암호/물리 용어 | hash, key, signature, salt, entropy, Hawking radiation, event-horizon | technical grounding 규칙상 보존 |
| 의도적 영어 장치 | `ACCESS != AUTHORITY`, `THE LAST QUESTION WAS MISSTATED`, archive response, field mark, 법정 영어 인용 | 화면·기록·고대 영어로 일부러 영어. 한국어 번역은 한 박자 늦게 병기하는 기존 기법 유지 |

규칙: 위 4범주에 들지 않으면 한국어로 옮긴다.

## Translate to Korean (한국어로 — 일반명사·동사구)

직역투의 주범인 일반명사·절차어는 모두 한국어로. 권장 대응:

| 영어 | 한국어 |
| --- | --- |
| access | 접근 / (문맥상) 권한 |
| authority | 권한 |
| heirship / heir | 상속(권) / 상속인 |
| petition | 청원 / 신청 |
| residence | 거처 / 거주 |
| employment | 일자리 / 고용 |
| delegation | 대표단 |
| charter | 헌장 |
| custody | 보관 / 관할 |
| respondent | 피심인 |
| filing | 접수 / 제출 |
| receipt | 영수증 / 수령증 |
| queue | 줄 |
| rumor | 소문 |
| screen | 화면 |
| banner | 현수막 |
| relic | 성물 / 유물 |
| slogan / chant | 구호 |
| invoice | 청구서 |
| client | 의뢰인 |
| value | 가치 |
| tool | 도구 |
| patience | 인내 |
| uniform | 제복 |
| seal (wrist seal) | 인장 / 손목 인장 |
| core (object) | 핵 / 원통 |
| display | 화면 / 표시판 |
| intake door | 접수창구 |
| gallery | 회랑 / 관람석 |
| square | 광장 |

표에 없어도 일반명사면 같은 원칙으로 옮긴다. 한국어가 어색해지는 경우에만
영어 유지를 고려하되, 그 판단을 Continuity Notes에 한 줄로 남긴다.

## 전환 방식 — 세 갈래 (직역만이 답이 아님)

일반명사를 옮길 때 **맥락에서 가장 자연스러운** 갈래를 고른다. 목표는
"기계 직역"이 아니라 "한국어 소설". 해리포터 초기 번역 정도의 자연스러움을
기준으로 삼는다.

1. **자연 한국어**: 대부분의 경우. screen→화면, rumor→소문.
2. **외래어 표기**: 한국어가 어색하거나 외래어가 더 일상적인 경우. 굳어진
   외래어는 한글 표기로 받아들인다. 예: drone→드론, lens→렌즈, slate→슬레이트
   (또는 기록판), core→코어(또는 핵). 영문 알파벳 노출 대신 **한글 표기**로.
3. **독립 재각색**: 직역도 외래어도 어색하면, 같은 뜻을 **다른 한국어 묘사로
   다시 쓴다**(literal translation 의무 아님). 예: "wrist seal이 금색으로
   변했다" → "손목의 인장이 금빛으로 달아올랐다"처럼 장면을 다시 묘사.

판단 기준: 한국인 독자가 소리 내어 읽었을 때 걸리지 않는 쪽. 셋 다 가능하면
가장 짧고 구체적인 쪽. 영문 알파벳을 한국어 문장 한가운데 박지 않는다(고유명사·
기술어·의도적 장치 제외).

## 측정법 (집행 확인)

퇴고 전후로 영어성 토큰 density를 측정해 감소를 확인한다.

```bash
grep -oE '[A-Za-z]{3,}' FILE.md \
  | grep -ivE '^(md|ko|http|https|doc|the|qfuds|saga|com|www)$' | wc -l
```

목표: 한국어 정본에서 영어 토큰이 위 Keep 4범주(고유명사·제도 분위기어·기술어·
의도적 장치)에 수렴. 일반명사 잔존이 거의 없어야 한다.

## 자가 점검 4문항

1. 이 영어 단어가 고유명사·제도 분위기어·기술어·의도적 장치 중 하나인가?
2. 아니라면 자연스러운 한국어 대응이 있는가? (있으면 옮긴다)
3. 옮긴 뒤 의미·사실·수치·인용·플롯 순서가 그대로인가? (불변 필수)
4. 문장이 직역투 어순이 아니라 한국어로 읽히는가?

## Next Use

이 글로서리는
[30_revisions 1부 de-jargon 퇴고 계획](../30_revisions/001_first_arc_dejargon_polish_revision_plan_ko.md)
이 집행한다.
