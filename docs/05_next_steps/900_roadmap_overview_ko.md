---
doc_id: roadmap_overview_ko
title: QFUDS Roadmap Overview Korean Guide
doc_type: guide
stage: "reference"
status: reference
evidence_role: reference
depends_on:
  - roadmap
  - experiment_summary
  - level_1_5_resolution_gate
  - traceability_matrix
next_gate: read roadmap for current status before acting
last_updated: 2026-06-09
---

# QFUDS Roadmap Overview Korean Guide

Date: 2026-06-09

이 문서는 새로 합류한 독자가 QFUDS 로드맵을 읽는 방법을 설명합니다.
현재 상태의 단일 진실 공급원은 항상
[docs/05_next_steps/000_roadmap.md](000_roadmap.md)입니다. 이 문서는 상태표를 대체하지
않고, 로드맵의 의도와 분기 구조를 설명합니다.

## 한 줄 요약

QFUDS는 암흑물질과 암흑에너지를 하나의 양자 거품 암흑부문의 두 유효
상으로 볼 수 있는지 테스트하는 연구 프로그램입니다. 현재 retained
branch에 대한 결론은 다음입니다.

```text
retained collapse/information-production Gamma(a)는 물리적 Level 1.5 승격에
실패했고, 현상론적 interacting-vacuum 전달 함수로 강등되었다.
```

## 현재 해석

현재 로드맵은 다음처럼 읽으면 됩니다.

1. retained `dF_coll/dln(a)` / `Gamma(a)` branch의 [Level 1.5](../wiki/glossary/repository_levels.md) 조사는
   물리적 승격 실패로 닫혔습니다.
2. 이 결정은 현재 retained source relation만 물리 유도로 기각한 것이며,
   더 넓은 DM-to-DE phase-transition 가설 전체를 반증하지는 않습니다.
3. 프로젝트는 현상론적 interacting-vacuum 모형 검증으로 계속될 수
   있습니다.
4. 물리적 QFUDS 섭동 이론인 Level 2B는 새 physical branch가 admission
   rule을 통과하기 전까지 막혀 있습니다.

즉, retained branch의 현상론적 진행과 future physical-QFUDS branch는
분리되어 있습니다.

## 이미 세워진 것

아래 항목은 현재 실험 기록 안에서 세워진 제한적 결론입니다.

- `Gamma(a)=0`이면 구현된 두 상 배경 모형은 LCDM 대조군으로 돌아갑니다.
- 상수 전달과 제한 없는 성장 기반 전달은 테스트된 진폭에서 배경
  수준 제약을 통과하지 못했습니다.
- 낮은 적색편이에서 켜지는 붕괴/정보생산 형태는 감사 대상으로
  남았지만, Level 1.5 물리 승격에는 실패했습니다.
- `exp_002`는 provenance로 강등되었습니다. 넓은 엔트로피 언어는
  핵심 증거가 아니며, `dF_coll/dln(a)` retained branch도 물리 유도로는
  강등되었습니다.
- Level 2A에서 P2 regularized phase-B fluid 닫힘은 실패했습니다.
- P1 interacting-vacuum 닫힘은 안정적으로 적분되지만, 물리적 QFUDS
  유도가 아니라 현상론적 상호작용 진공 모형으로만 남습니다.

## 아직 추측적인 것

다음은 아직 확립되지 않았습니다.

- 양자 거품이 실제 암흑물질/암흑에너지의 미시적 기원이라는 주장.
- retained `Gamma(a)`가 미시 물리, 엔트로피, 정보생산, 붕괴 역사에서
  유도된다는 주장.
- 붕괴 임계값 `M`이 물리적으로 고정되었다는 주장.
- `dF_coll/dln(a)`가 QFUDS 자체 성장으로 self-consistent하게 계산되었다는 주장.
- 물리적 Level 2B 섭동 방정식.
- CLASS/CAMB 구현.
- CMB, 물질 파워 스펙트럼, BAO, 초신성, DESI, Euclid, Roman 제약 통과.
- QFUDS가 LCDM, 통합 암흑 유체, 상호작용 암흑에너지와 구별되는 새
  물리라는 주장.

## Future Physical Branch Admission Rule

새 physical-QFUDS branch는 최소한 다음을 제시하기 전에는 열지 않습니다.

- `X =`
- `Q^nu =`
- `why phase B has w ~= -1 =`
- `delta Q route =`
- `known-model distinction =`

## 레벨 용어와 통과 기준

레벨 용어의 정의는
[repository_levels.md](../wiki/glossary/repository_levels.md)를 기준으로
읽습니다. Level 1.5 통과/실패 기준은
[015_level_1_5_resolution_gate.md](015_level_1_5_resolution_gate.md)에 두고,
이 overview 문서에는 중복해서 적지 않습니다.

## 남은 레벨의 성공과 실패

Level 2B의 정의와 현재 차단 조건도
[repository_levels.md](../wiki/glossary/repository_levels.md)와 roadmap을
기준으로 봅니다.

### Level 3: CLASS/CAMB 통합

성공:

- Level 2B 또는 명시적 현상론적 닫힘을 Boltzmann code에 넣고 재현 가능한
  실행 경로를 만듦.

실패:

- code interface가 모호하거나, gauge/transfer prescription이 Boltzmann
  solver에 들어갈 만큼 명확하지 않음.

### Level 4: CMB 비교

성공:

- CMB acoustic structure를 망가뜨리지 않음.
- LCDM과의 차이가 관측 제약 안에 있거나 명시적 예측으로 정리됨.

실패:

- acoustic peak 구조가 깨짐.
- 초기 우주 dark-energy fraction 또는 transfer가 CMB와 충돌함.

### Level 5: 물질 파워 스펙트럼

성공:

- matter power와 growth history가 관측 제약 안에 있음.
- 작은 스케일 차이가 있다면 baryonic feedback과 구분 가능한 형태로
  제시됨.

실패:

- 구조 형성이 지워짐.
- power spectrum이 관측과 충돌함.
- growth proxy 수준의 결과를 full matter-power viability로 과장함.

### Level 6: Survey likelihood

성공:

- BAO, 초신성, DESI, Euclid, Roman 등 실제 likelihood 또는 그에 준하는
  비교에서 LCDM과 정량적으로 비교됨.

실패:

- 데이터가 모형을 배제함.
- 추가 파라미터가 임의 튜닝으로만 작동함.
- LCDM보다 나은 설명력 없이 known model로 환원됨.

## 주요 분기

### 분기 A: 물리 유도 성공

`Gamma(a)`가 물리적으로 고정되고 Level 1.5를 통과하면 physical Level 2B로
진행합니다. 이 경우 목표는 QFUDS 고유의 섭동 방정식과 관측 가능량을
만드는 것입니다.

### 분기 B: 현상론으로 강등

`Gamma(a)`가 유도되지 않지만 안정적이고 유용한 닫힘이 남으면, 프로젝트는
현상론적 interacting-vacuum 모델로 계속됩니다. 이 경우 QFUDS라는 이름은
물리 기원 주장이 아니라 모델 동기 또는 해석으로만 남아야 합니다.

### 분기 C: 모델 폐기

물리성, 안정성, CMB, matter power, survey likelihood 중 하나에서 명확히
실패하면 해당 QFUDS 버전은 폐기 또는 축소됩니다. 실패는 삭제하지 않고
결과 문서와 decision log에 남깁니다.

## 새 독자의 권장 읽기 순서

- [README.md](../../README.md)
- [docs/05_next_steps/000_roadmap.md](000_roadmap.md)
- [docs/04_results/000_experiment_summary.md](../04_results/000_experiment_summary.md)
- [docs/00_project/traceability_matrix.md](../00_project/traceability_matrix.md)
- [docs/05_next_steps/015_level_1_5_resolution_gate.md](015_level_1_5_resolution_gate.md)
- 관심 있는 theory / experiment / result 문서
- [docs/00_project/decision_log.md](../00_project/decision_log.md)
- [docs/00_project/verification_guide.md](../00_project/verification_guide.md)

이 순서는 다음 흐름을 복원하기 위한 것입니다.

```text
hypothesis -> experiment -> result -> decision -> roadmap status
```
