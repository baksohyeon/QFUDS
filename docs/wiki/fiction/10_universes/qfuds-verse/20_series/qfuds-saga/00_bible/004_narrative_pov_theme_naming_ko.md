---
doc_id: qfuds_saga_narrative_pov_theme_naming_ko
title: QFUDS SAGA 시점 주제 고유명사 규칙
doc_type: guide
stage: reference
status: draft
evidence_role: provenance
depends_on:
  - qfuds_saga_factions_cultures_power_ecology_ko
  - qfuds_saga_deep_time_restoration_timeline_ko
next_gate: apply as active POV/theme/naming defaults; 015 overrides faction formal names
last_updated: 2026-06-21
---

# QFUDS SAGA 시점 주제 고유명사 규칙

## 목적

이 문서는 시점, 중심 주제, 고유명사 체계, 역사 차용 규칙의 active 기본값을
고정한다. 세력 formal name은 [015](015_factions_canon_naming_ko.md)가 우선한다.

이 문서는 fiction/provenance only다. QFUDS 연구 결과, 물리 증거, support,
validation, Level 2B admission이 아니다.

## Decision Summary

기본 시점은 **3인칭 제한 시점**이다.

1인칭은 금지하지 않는다. 다만 본문 기본 시점으로 쓰지 않고, 법정 진술,
복원 로그, 고해 기록, 사후동의서, 작전 보고서, 라스트 아카이브 응답 같은
문서형 interlude에서만 쓴다.

고유명사는 영어권 독자도 읽을 수 있는 common name과, 역사적 층이 느껴지는
ritual/legal name을 함께 둔다.

```text
common name: The Last Archive
ritual/legal name: Archivum Novissimum
```

한국어는 active prose의 1차 본문 언어다. 다만 주요 고유명사와 field mark는
영어, 프랑스어, 라틴어, 그리스어, 페르시아/아랍 행정어풍,
산스크리트/팔리어풍, 튀르크/몽골 군영어풍을 기능별로 섞어 남길 수 있다.

## POV Decision Matrix

| Candidate | 장점 | 실패 모드 | 판정 |
| --- | --- | --- | --- |
| 1인칭 단일 주인공 | 감정 몰입이 강함 | 복원 문명 전체의 정치/법/종교/경제가 좁아짐 | Reject as default |
| 1인칭 다중 화자 | 복원체/증언/기억 오류를 직접 보여 줄 수 있음 | 화자 구분이 어려워지고 장기 문명사 밀도가 흔들림 | Use only for interludes |
| 전지적 3인칭 | 대서사와 역사 설명에 강함 | 설명 과잉, 인물 욕망 약화, "설정표"로 회귀 위험 | Reject as default |
| 3인칭 제한 시점 | 인물 욕망과 대서사를 동시에 유지 | POV 설계가 느슨하면 산만해짐 | **Default** |
| 문서 모자이크 | 법정기록, 감사문, 기도문, 작전보고서에 강함 | 본문 장면성이 약해질 수 있음 | Use as structural spice |

시스템 설계 기준:

```text
needs politics scale       -> not pure 1st person
needs identity uncertainty -> not omniscient too early
needs emotional stakes     -> not pure archive/document format
needs faction contrast     -> rotating 3rd-limited POV
```

따라서 기본은 3인칭 제한 시점이고, 1인칭은 "증거물"로 쓴다.

## 왜 3인칭 제한인가

이 SAGA의 재미는 한 인물의 고백보다, 같은 사건을 세력마다 다르게 해석하는
데서 나온다.

3인칭 제한 시점은 다음 장점이 있다.

- 정치/종교/경제/법정/전쟁 스케일을 유지할 수 있다.
- 각 인물의 욕망과 오해를 가까이 따라갈 수 있다.
- "복원된 기억이 진짜인가"를 독자에게 계속 의심시킬 수 있다.
- 문서형 1인칭 interlude와 대비가 생긴다.

기본 카메라는 세 명을 돈다.

| POV | 역할 | 독자가 보는 세계 |
| --- | --- | --- |
| Laur auditor | 복원 claim을 의심하는 사람 | 법, 감사, unknown, circularity |
| Aletheia custodian | 삭제된 자와 망각권 사이에 선 사람 | 계승, 동의, 돌봄, 비밀 결사 |
| Ledger heir or deserter | 원장 권력 내부를 아는 사람 | exit-only 통치, 불변원장, 기술귀족 |

라스트 아카이브는 기본 POV가 아니다. 너무 빨리 내면을 주면 신비가 죽는다.
대신 응답문, 법정 제출문, 오류 메시지, 기도문 같은 형태로만 나타난다.

## POV Operating Rules

| Rule | 이유 |
| --- | --- |
| 한 장면에는 한 POV만 둔다 | 복원 기억의 진위와 인물 오해를 명확히 유지 |
| 장면 시작 3문단 안에 POV의 욕망을 드러낸다 | 설정 설명보다 인물 욕망을 먼저 세움 |
| 라스트 아카이브는 직접 내면 독백 금지 | AGI를 너무 빨리 인간화하지 않음 |
| 1인칭은 문서 증거로만 사용 | 증언, 고해, 로그, 법정 기록의 불안정성을 활용 |
| 역사 설명은 장면 후에 짧게만 삽입 | "역사책"이 아니라 소설 리듬 유지 |

## 중심 주제

한 문장 주제:

```text
완전한 복원이 가능해진 세계에서, 인간에게는 잊힐 권리와 죽을 권리가 남아 있는가?
```

더 짧게:

```text
기억이 영원해지면, 자유는 어디에 남는가?
```

이 SAGA는 "QFUDS가 맞다"를 증명하는 이야기가 아니다.

이야기의 주제는 다음 네 갈등이다.

| 갈등 | 질문 |
| --- | --- |
| 보존 vs 망각 | 모든 정보를 보존하는 것이 정말 선인가? |
| 복원 vs 재창조 | 구분 불가능한 재계산은 원본의 귀환인가? |
| 사랑 vs 동의 | 사랑하는 사람을 되살리고 싶은 욕망은 어디까지 허용되는가? |
| 자유 vs 원장 | 삭제 불가능한 진실은 해방인가 감옥인가? |

## 역사 차용 규칙

실제 역사를 약하게 차용해도 된다. 다만 "이 세력은 어느 실제 집단이다"처럼
일대일 대응시키지 않는다.

차용 단위는 고유명사가 아니라 구조다.

| 역사 기능 | SAGA 변환 |
| --- | --- |
| 제국 행정 | 다민족/다행성 복원권역을 관리하는 법과 도로망 |
| 디아스포라 | 흩어진 잔상과 이름을 보존하는 망명 기록공동체 |
| 초원 정복국가 | 잔상 회수, 이동 oath, 죽은 적의 기억 흡수 |
| 로마법/교회법 | 원본/복원체/상속/죄의 연속성 판례 |
| 수도원 | 망각과 기록 절제를 훈련하는 공동체 |
| 상업 공화국 | 복원 보험, 원장 가문, 사후 권리 거래 |
| 기술봉건주의 | CEO-집정관, 주주귀족, exit-only 자유의 풍자 |

현실 집단을 선악으로 단순 대응시키지 않는다. 좋은 차용은 특정 역사와 닮았다는
느낌을 주지만, 독자가 "그냥 X를 우주 버전으로 바꿨네"라고 느끼게 만들지
않는다.

## 고유명사 원칙

한국어판은 active reader-facing prose다. 소설 본문에서 주요 고유명사는 영어,
프랑스어, 라틴어 계열을 기본으로 둘 수 있고, 필요한 경우 그리스어,
페르시아어풍, 아랍어풍 음운을 섞어 장기 문명사의 층을 만든다.

원칙:

- 기관명은 영어/프랑스어/라틴어풍을 보존할 수 있다.
- 일상 별명은 짧은 영어 또는 프랑스어 별칭을 보존할 수 있다.
- 한국어 본문은 고유명사를 억지로 번역하지 않고 장면 안에서 의미가 드러나게 한다.
- QFUDS 같은 연구 약어는 그대로 둔다.
- 너무 노골적인 실제 종교/민족 명칭은 피한다.

## Naming Strata

| Stratum | 역사적 기능 | 적용 대상 | 예시 질감 |
| --- | --- | --- | --- |
| Latin / Roman-canon | 법, 판례, 죄, 고해, 부활, 최후 심판 | 법원, 의례, 복원 판결, 사후동의 | `Curia`, `Consensus`, `Archivum`, `Novissimum` |
| French scientific-bureaucratic | 근대 관측소, 행정, 세속 과학기관 | 관측소, 감사기관, 도시명 | `Observatoire`, `Bureau`, `Registre` |
| Greek technical-philosophical | 존재론, 동일성, 기억, 형상 | 이론명, 학파명, 금지 모델 | `Eidolon`, `Mnemos`, `Aletheia` |
| Persian / Arabic administrative | 천문학, 장부, 조세, 제국 관료제 | 복원청, 권역, 시장, 도로망 | `Diwan`, `Sijil`, `Miraj`, `Dar` |
| Sanskrit / Pali-inspired | 무아, 해탈, 집착, 다시 태어남의 거부 | 망각권 연맹, 수도원, 수행명 | `Sangha`, `Anatta`, `Nirvana` |
| Turkic / Mongol camp-military | 기동성, oath, 군영, 이동 공동체 | 잔상 유목민, 전쟁 집단 | `Ordu`, `Yasa`, `Tumen` |
| English plain-name | 독자 가독성, 공용명 | 모든 핵심 기관의 common name | `The Last Archive`, `Ledger Houses` |

이름은 두 겹으로 둔다.

| Layer | 역할 | 예 |
| --- | --- | --- |
| Common name | 독자가 쉽게 부르는 이름 | The Last Archive |
| Formal/Ritual name | 법정, 의례, 고문서에서 쓰는 이름 | Archivum Novissimum |

## Naming Table

| 한국어 설명 | Common name | Formal / ritual name | 역사적 질감 |
| --- | --- | --- | --- |
| 라스트 아카이브 | The Last Archive | Archivum Novissimum | 최후의 것들, 종말론, 기록관 |
| 라우어 관측소 | Observatoire de Laur | Bureau Laurien | 프랑스식 관측소/감사 관료제 |
| 연속성 법원 | Court of Continuance | Curia Continuationis | 로마법/교회법/판례 |
| 복원청 | Ministry of Restoration | Diwan al-Restitution | 제국 행정, 장부, 복원 허가 |
| 원장 가문 | Ledger Houses | Domus Tabularii | 로마 archive, 상업 귀족, 불변원장 |
| 원장 성채 | Ledger Keeps | Castra Tabularii | 성채, 군영, 데이터 봉건제 |
| 알레테이아 베일 | Aletheia Veil | Velum Aletheiae / Custodes Velati | 계승, 결사, 수도회 |
| 망각권 연맹 | League of Oblivion | Sangha Oblivionis | 해탈, 잊힐 권리, 수도원 |
| 망각 수도원 | Oblivion Cloister | Cloister Anatta | 무아, 집착의 중단 |
| 잔상 유목민 | Remnant Nomads | Ordu Remanentium | 초원 군영, oath, 이동 공동체 |
| 관측 전쟁 | Wars of Observation | Bella Observationis | 로마식 전쟁명, 관측 군사화 |
| 복원 대기실 도시 | Waiting Cities | Civitates Expectantium | 순례지, 법원 도시, 대기 공동체 |
| QFUDS 금지 연구실 | Forbidden QFUDS Lab | Laboratorium Vetitum | 금지 지식, 이단 심문, 실패한 아름다움 |
| 불변원장 | Immutable Ledger | Liber Indelibilis | 지워지지 않는 책, 원장 신학 |
| 사후동의서 | Posthumous Consent | Consensus Posthumus | 법/고해/사후 권리 |
| 자기부정 복원체 | Self-Denying Restored | Eidolon Negans | 그리스적 형상, 동일성 부정 |
| 잔상 밀매자 | Echo Brokers | Mercatores Vestigii | 상업 공화국, 암시장 |

## Naming Decision Criteria

고유명사는 다음 기준을 통과해야 한다.

| Criterion | 질문 | 실패 예 |
| --- | --- | --- |
| 가독성 | 독자가 한 번에 읽을 수 있는가? | 너무 긴 가짜 라틴어 |
| 역사적 질감 | 법/종교/제국/유목/수도원 중 어떤 층을 떠올리게 하는가? | 무국적 SF 단어 |
| 기능 일치 | 이름이 세력의 역할과 맞는가? | 망각권 단체에 군사식 이름 |
| 과잉 대응 회피 | 실제 종교/민족을 그대로 우주 버전으로 보이게 하지 않는가? | 현실 집단명 변형 |
| 장면성 | 대사에서 자연스럽게 불릴 수 있는가? | 문서에만 멋있는 이름 |

예를 들어 `League of Oblivion`은 독자가 바로 이해하는 common name이고,
`Sangha Oblivionis`는 수도원/해탈/망각권의 ritual layer다. 둘을 모두 두면
정치 장면과 의례 장면의 질감이 달라진다.

## 톤

문체는 한국어 reference 문서와 한국어 소설 본문을 분리한다.

문서 톤:

```text
짧고 직접적.
설정 회의록처럼 읽힌다.
```

소설 톤:

```text
장면 중심.
제도와 철학은 사건 속에서 드러난다.
인물은 논문 설명자가 아니라 욕망을 가진 사람이다.
```

좋은 장면 예:

```text
복원 법정에서 판사가 "당신은 원본입니까?"라고 묻는다.
복원체는 대답하지 않고, 원본만 알던 아이의 자장가를 부른다.
방청석의 어머니가 무너진다.
감사관은 울지 않고 체크박스에 unknown을 찍는다.
```

나쁜 장면 예:

```text
인물이 다섯 쪽 동안 정보철학을 설명한다.
```

## 작품 설정 기준서로 넘길 결정

작품 설정 기준서에는 다음을 canon 기본값으로 넘긴다.

- 본문 기본 시점: 3인칭 제한 시점.
- interlude 시점: 1인칭 문서, 법정 진술, 로그, 기도문, 작전 보고서 허용.
- 중심 주제: 완전 복원 시대의 잊힐 권리와 죽을 권리.
- 고유명사: common name + formal/ritual name의 2층 구조.
- naming strata: Latin/Roman-canon, French bureaucratic, Greek technical,
  Persian/Arabic administrative, Sanskrit/Pali-inspired, Turkic/Mongol
  camp-military, English plain-name.
- 역사 차용: 고유 집단 대응이 아니라 제도, 이념, 공동체 구조 차용.
- 라스트 아카이브는 직접 POV가 아니라 문서와 응답으로 노출.
