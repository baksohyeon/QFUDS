---
doc_id: qfuds_saga_world_direction_matrix_ko
title: QFUDS SAGA 세계관 방향 선택 매트릭스
doc_type: guide
stage: reference
status: draft
evidence_role: provenance
depends_on:
  - qfuds_saga_agentic_system_ko
  - qfuds_saga_index_ko
  - qfuds_public_story_bridge_ko
next_gate: user selects primary direction or hybrid before saga bible
last_updated: 2026-06-19
---

# QFUDS SAGA 세계관 방향 선택 매트릭스

## 목적

이 문서는 QFUDS SAGA의 세계관 방향을 바로 고정하지 않고, 후보를 비교하기
위한 선택 장부다.

학원물은 후보 중 하나일 뿐이다. 기본 추천은 더 넓은 구조다.

```text
Nested Cosmology
+ tactical/philosophical SF
+ it-from-bit mythos
+ QFUDS가 맞는 fiction 층위
```

즉, QFUDS가 현실 연구에서는 증명되지 않았지만 어떤 층위에서는 정답인 세계를
상상한다. 그 세계가 실제 우주인지, 모델인지, 훈련 공간인지, 감옥인지,
관측자가 만든 질문의 산물인지는 장편의 핵심 미스터리로 남긴다.

## Workflow Boundary

This document uses external references as genre/craft and philosophy pointers
only. It does not introduce a research asset, data product, numerical extraction,
or QFUDS evidence claim.

External-source handling remains governed by
[Research Asset and Product Workflow](../../../../.agent/workflows/research-asset-product-workflow.md).

Current workflow states:

```text
hit_not_cached
asset_available_not_downloaded
not_extractable
```

## Direction Matrix

| Direction | Core Engine | Why It Fits QFUDS | Risk | Use / Reject |
| --- | --- | --- | --- | --- |
| Nested Cosmology | Inception식 층위, 각 층의 물리 법칙과 관측자가 다름 | "QFUDS가 맞는 세계"를 fiction premise로 둘 수 있고, 바깥층에서는 audit이 계속 가능함 | 너무 관념적이면 장면이 약해짐 | **Use as spine** |
| Closed World Revelation | 닫힌 관측권, 금기 문서, 바깥 세계 반전 | 순환논리, 숨겨진 실패 문서, 금지된 Level 2B를 이야기 장치로 쓸 수 있음 | 특정 작품 구조를 너무 닮을 수 있음 | Use as reveal structure |
| Deep-Time Empire | 관측자료, 해석권, 암흑섹터 신학, 학회 권력이 문명을 지배 | Dune식 문화/제도/권력 밀도를 만들 수 있음 | 세계관 설명이 plot보다 커질 수 있음 | Use as texture |
| Tactical Philosophy SF | 작전 브리핑, 정보전, 배신, kill condition, after-action report | Call-of-Duty식 리듬을 "관측 전쟁"으로 변환 가능 | 과학이 단순 임무 목표로 납작해질 수 있음 | Use for pacing |
| It from Bit Mythos | 현실이 물질보다 질문, 관측, bit, 기록에서 발생 | black-hole information, 기록, audit harness와 잘 맞음 | 철학 구호로만 남으면 약함 | Use as metaphysics |
| Academy / Observatory | 훈련, 학파, 심사, 금기문서, mentor conflict | 기존 라우어 관측소/감사관 설정과 호환됨 | 너무 뻔한 학원물이 될 수 있음 | Keep as institution, not genre |
| Archive Mystery | 깨진 로그, 실패한 가설, 감마 신호, 누락된 source `X` 추적 | 실제 repo 여정의 감정선과 가장 직접 연결됨 | 스케일이 작아질 수 있음 | Use as episode engine |

## Recommended Hybrid

추천 방향은 다음과 같다.

```text
Nested Cosmology as spine
Deep-Time Empire as world texture
Tactical Philosophy SF as pacing
It from Bit Mythos as metaphysical question
Archive Mystery as episode engine
Academy/Observatory only as institution
```

이렇게 하면 학원물이 중심이 되지 않는다. 라우어 관측소는 학교가 아니라 오래된
문명 기관, 관측 군사조직, 기록 수도원, 과학 재판소가 겹친 장소가 된다.

## Core Premise Options

| Option | Premise | Strength | Weakness | Decision |
| --- | --- | --- | --- | --- |
| A. The Correct Layer | 어떤 관측 층위에서는 QFUDS가 완전히 맞다 | 사용자 상상력을 정면으로 살림 | 현실 연구와 혼동될 수 있음 | Candidate |
| B. The Training Universe | QFUDS가 맞는 세계는 agentic audit training chamber다 | 연구 하네스를 plot으로 만들기 좋음 | 감정적 stakes가 약해질 수 있음 | Candidate |
| C. The Prison of a Beautiful Theory | 인류는 아름다운 이론이 만든 감옥 안에 있다 | closed-world 반전과 잘 맞음 | 너무 음모론적으로 보일 수 있음 | Candidate |
| D. The War of Observers | 서로 다른 관측기관이 우주의 질문권을 놓고 싸운다 | tactical SF와 잘 맞음 | 과학보다 전쟁이 커질 수 있음 | Candidate |
| E. The Archive That Refused Proof | 우주는 답을 주지 않고, 질문 기록만 남긴다 | 기존 감사관/Archive 정서와 잘 맞음 | 장편 추진력이 약하면 산문적임 | Candidate |

## Scientific Use Rules

fiction 안에서는 다음을 허용한다.

- `Gamma(a)`를 "흔적", "작전명", "층위 간 timing fingerprint"로 사용.
- `Q^mu`, `delta Q`, phase-B pressure 부재를 세계의 금기 또는 재판 조건으로
  변환.
- NASA/BAO/CMB/LSS를 감시망, 심판기관, kill-map tribunal로 변환.
- black-hole information과 `it from bit`를 세계관 신화로 사용.

하지만 다음은 금지한다.

- fiction premise를 현실 QFUDS 증거로 되돌려 쓰기.
- 외부 관측자료를 보고 `xi`, width, amplitude를 고른 뒤 source라고 부르기.
- black hole, remnant, foam, information language를 equation 없이 물리 source로
  쓰기.
- 특정 작품의 고유 설정, 인물, 명칭, 사건 전개를 복제하기.

## Candidate Season Shape

| Part | Function | Fiction Question | QFUDS Echo |
| --- | --- | --- | --- |
| Part 1 | Closed world | 왜 관측소 바깥을 볼 수 없는가? | observer mode |
| Part 2 | Signal | Gamma fingerprint는 누가 남겼는가? | phenomenological timing |
| Part 3 | Kill-map | 아름다운 이론은 무엇에 의해 죽는가? | NASA/BAO/LSS/CMB constraints |
| Part 4 | Layer break | QFUDS가 맞는 세계는 진짜 우주인가, 검증 공간인가? | circularity audit |
| Part 5 | It from bit | 질문이 현실을 만들었다면 누가 질문했는가? | information-physics myth |

## Next Gate

다음 단계는 사용자 확인이다.

선택지는 둘 중 하나다.

1. 위 추천 hybrid를 1차 SAGA bible의 기본 방향으로 사용한다.
2. matrix를 더 확장해 다른 장르 구조를 추가한 뒤 다시 고른다.

2026-06-19 후속 선택 장부:
[QFUDS SAGA 장기 복원 문명사 타임라인](003_deep_time_restoration_timeline_ko.md)
은 이 matrix를 "복원 문명사" 방향으로 구체화한다. 그 문서는 완전 복원,
라스트 아카이브, 망각권, 알레테이아 자매회, 라우어 관측소를 시간순 역사로 묶어
SAGA bible 후보 backbone을 제안한다.
