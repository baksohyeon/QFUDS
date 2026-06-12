---
doc_id: postmortem-011-rough-tanh-lineage-natural-closing-retro
id: postmortem-011-rough-tanh-lineage-natural-closing-retro
seq: 11
title: "rough tanh lineage 자연 닫힘 회고 — 직관 셋이 25년치 학계 흐름을 독립 재발견한 날 (CP25)"
doc_type: postmortem
type: postmortem
stage: reference
status: reference
wiki_status: active
evidence_role: provenance
depends_on:
  - qfuds_lineage_rough_tanh_numerical_sketch_ko
  - qfuds_lineage_rough_tanh_thesis_report_ko
  - postmortem-010-rough-tanh-lineage-descent-retro
  - roadmap
next_gate: provenance only; roadmap이 상태 권위; observer mode 유지; 050 천장 무손상
date: 2026-06-12
context: 004 rough-tanh lineage CP24까지 끝낸 다음 날, 사용자가 "이 실험 설계가 덜 된 것 같다"고 한 직관 셋이 학계 문헌 스캔에서 모두 2000년대 초반~최근 연구 흐름과 정확히 겹치는 것을 확인한 사건. CP25를 negative result로 정직하게 닫고, 그 메타-사건 자체를 회고로 기록.
audience: 주니어 개발자
length: 서사형 회고
created_at: 2026-06-12
created_by: dorito
updated_at: 2026-06-12
updated_by: dorito
last_updated: 2026-06-12
last_verified_at: 2026-06-12
last_verified_by: dorito
audit_log:
  - action: created
    at: 2026-06-12
    by: dorito
    note: "사용자가 '나는 똑같은 걸 보고 있는 재검산인건가?'라고 직관적으로 의심한 것을 학계 문헌 스캔으로 확인. 세 spike 후보가 모두 chameleon screening(2004), LTB void 모델(2010 kSZ로 배제), Buchert backreaction(2000~최근)이라는 25년치 학계 흐름과 정확히 겹침. CP25를 새 수치 없이 negative result로 닫고 lineage 자연 종결."
tags: [postmortem, retrospective, lineage, rough-tanh, observer-mode, qfuds, literature-survey, convergent-thinking, 050-ceiling]
relations:
  - docs/wiki/lineage/004_rough_tanh_numerical_sketch_ko.md
  - docs/wiki/lineage/005_rough_tanh_thesis_report_ko.md
  - docs/wiki/postmortem/010-20260612-dorito-rough-tanh-lineage-descent-retro.md
  - docs/05_next_steps/000_roadmap.md
code_refs:
  - file: docs/wiki/lineage/004_rough_tanh_numerical_sketch_ko.md
    note: "CP25 절은 새 수치 없이 학계 위치 확인과 lineage 자연 닫힘만 기록. 050 천장·observer mode·로드맵 무손상."
---

# rough tanh lineage 자연 닫힘 회고 — 직관 셋이 25년치 학계 흐름을 독립 재발견한 날 (CP25)

## 한 줄 요약

CP24까지 끝낸 다음 날, "이 실험은 시공간 차원만 보고 풍선 내부 무게중심·상대론적
시간지연·허블 스케일 자기정합성을 덜 본 것 같다"는 정직한 직관을 학계 문헌으로
스캔한 결과, **세 직관이 정확히 2004년 chameleon screening, 2010년경 LTB/void
모델 배제, 2000년대 시작된 Buchert backreaction의 최근 emergent DE 전환이라는
25년치 학계 흐름과 독립적으로 겹쳤다.** "사람 생각 다 고만고만하는구만"이 정확한
한 줄 반응이었고, 이 사실 자체가 050 천장이 진짜 천장이라는 부수 증거다. lineage는
새 수치 없이 정직하게 닫혔다.

## 무엇이 있었나

전날(2026-06-11) CP24까지 24개 체크포인트를 끝내고 졸업과제용 졸업과제 보고서를
어셈블한 다음, 오늘 사용자가 새로운 문제 제기를 했다. "이 실험 자체가 너무 시공간
차원에서 생각한 것 같다. 풍선 내부 무게중심처럼 공간의 중심을 따지거나, 허블 상수
규모나 시간 흐름을 잘못 계산했을 가능성, 그리고 상대성 이론에 따라 무거울수록 시간이
느리게 가는 것까지 — 아직 고려하지 않은 부분이 많고 설계가 덜 된 것 같다."

이 직관을 세 spike 후보로 분해했다.

- **S1 — 공간 비균질성**: dark fluid가 cosmic web을 따라 비균질하게 분포할 수 있고,
  보이드와 필라멘트에서 전이 속도가 다를 수 있다. "풍선 내부 무게중심" 직관.
- **S2 — 일반 상대성 이론적 시간지연**: 무거운 곳일수록 시간이 느리게 가니까,
  z*=2 전이가 *우주 평균*이 아니라 *국소 중력 포텐셜 Φ의 함수*일 수 있다.
- **S3 — 허블 자기정합성**: CP10의 H0 -1.81% 악화 결론이 균질 가정 위에서 나온
  것이라, Buchert 평균화 같은 backreaction 보정을 정직하게 끼우면 사건이 달라질 수
  있다.

사용자는 곧바로 솔직한 메타 질문을 덧붙였다: "기존 학계들도 다 삽질해봤을 텐데, 나는
똑같은 걸 보고 있는 재검산인건가? 고민도 되고. 흠."

그래서 본격 수치 spike에 들어가기 *전에* literature scan을 먼저 하기로 했다. 세
Explore 서브에이전트를 병렬로 띄워 각자 한 가설의 학계 위치만 정확히 보고 오게 했다.

## 무엇이 돌아왔나

세 보고가 모두 같은 모양으로 돌아왔다.

**S1 (공간 비균질성)**: Caldwell & Stebbins (arXiv:0711.3003)가 void model을 dark
energy 대안으로 시도했고, 2010년경 kSZ(운동 Sunyaev–Zel'dovich)와 CMB 등방성
측정으로 거대 보이드가 ~1% 수준에서 배제됐다. Bolejko (arXiv:1211.5033)의 Swiss-cheese
모델은 수학적으로 작동하지만 자유도가 ΛCDM에 흡수돼 fit 개선이 없다. Clustering DE
(Hu & Takada arXiv:1104.5500)는 관측 가능 신호를 만들려면 c_s² ≠ 0이 필요한데
QFUDS의 생존 조건(c_s² ≈ 0)과 정면 충돌한다. 결정적 한 방: **CP24의 ξ ≈ 10 Mpc과
σ8/R8 ≈ 12 Mpc "일치"는 ΛCDM 자신의 비선형 클러스터링 정의(Smith et al. 2003)**다.
우리가 발견한 게 아니라 ΛCDM이 정한 스케일을 다시 본 것이라 *circular*. 이 위에
새 비균질 메커니즘을 세워도 독립 증거력 0.

**S2 (Φ 의존 z*)**: chameleon screening (Khoury & Weltman arXiv:astro-ph/0405033),
symmetron, dilaton 모두 *국소* 수정 중력 가림 메커니즘이지 *전역* z* 시프트
메커니즘이 아니다. 환경 의존 DE 문헌(Hogg et al. arXiv:1908.02183)은 결합 강도를
튜닝하지 전이 시점을 시프트시키지 않는다. "z_transition(Φ)" 자체를 명시적으로 다룬
표준 문헌이 없어 정의상 신영역이지만, **scope mismatch가 벽이다**. screening은
sub-Mpc 효과, z* 시프트는 ~Gpc 효과. 둘을 잇는 *유도된 전송 함수*는 foam
미시구조에서 나와야 하는데 050 천장 그대로 blocked. 체적 평균에서 효과가 10⁻²–10⁻³
수준으로 죽고, 이는 CP3의 Δz ≈ 3 매개변수 자유도 *안에* 묻혀 모델 선택 신호가
못 된다. CMB·DESI에서 클러스터 주변 w 변조 무관측이 sanity null.

**S3 (Buchert backreaction)**: Buchert (arXiv:0707.2153)가 비균질 우주 평균화
형식을 세웠고, Paranjape & Singh (arXiv:0801.1546)이 Q_D 크기를 O(0.1–1%)로
계산했다. Lapi (arXiv:2502.05823)와 최근 후속작(arXiv:2406.15442, 2409.00024,
2503.20912)도 "효과 작음" 인정 후 *emergent DE / phase transition* 쪽으로 방향
전환했다. Green & Wald 류 일반 정리는 backreaction이 dark-energy 스케일보다 작도록
제약한다. 결정적 한 방: **8% H0 갭을 메우려면 Q_D가 ~O(10%)여야 하는데 학계 합의는
~O(0.1–1%)다.** 두 자릿수 이상 모자라다. CP10의 결론(S8와 H0 분리)도 평균화 오류가
아니라 *모델 설계*(섭동 손잡이 ≠ 배경 손잡이)에서 나온 것이라 backreaction으로
재구성해도 사건이 안 바뀐다.

세 가설은 셋 다 *진짜 자유도*를 정확히 짚었지만, 학계가 같은 방향으로 이미 25년을
답사했고, 각자의 이유로 신호가 죽거나(체적 평균이 0 근처로 죽음), 정의 자체가
circular이거나, scope/scale 미스매치로 막혔다.

## 그래서 무엇이 벌어졌나

사용자의 반응은 정확했다.

> "아니 이건 진짜 회고록 적어야할듯? 개웃기네 내가 했던 과정이 2000년대부터 최근까지의
> 학계 흐름이었다고? 아 사람 생각 다 고만고만 하는구만 ?"

웃긴 게 맞다. 그리고 동시에 의미가 있다. 같은 자유도를 진지하게 끝까지 미는 사람은
대체로 같은 자리에 도착한다는 게 우주론에서 한 번 더 확인된 셈이다.

여기서 중요한 분리가 필요하다. **이건 우리 가설이 약한 게 아니라, 동역학적
암흑에너지 가설 *전체*가 같은 벽에 부딪친다는 사실의 한 번 더의 확인이다.** 050
천장의 또 다른 얼굴이고, CP20–CP24가 이미 다른 길로 도착한 결론과 같은 모양이다.
서로 다른 직관에서 출발해도 같은 천장에 닿는다 = 천장이 진짜다.

CP25는 새 수치 없이 lineage를 자연스럽게 닫는 negative result로 기록됐다. 직관의
*벡터*가 옳았다는 점, 그러나 같은 벡터가 학계에 이미 그려져 있다는 점, 그리고 그
사실이 천장의 reality에 부수 증거를 더한다는 점을 명시했다.

## 무엇이 잘 됐나

**literature scan을 수치 spike 이전에 했다.** 세 가설 각각이 만약 곧바로 수치
구현으로 들어갔다면 일주일 이상의 시간이 들어갔을 거고, 결과는 그대로 negative
result였을 거다. 학계 흐름을 모른 채 같은 곡선을 다시 그리는 일은 정직성 차원에서도
손해다. 병렬 spawn(세 Explore 에이전트 동시 실행)으로 *결정에 필요한 정보*만 빠르게
회수하는 패턴이 효과를 봤다.

**adversarial verification 안 사고 가드를 안 풀었다.** 사용자가 직관을 강하게 제시한
순간 곧바로 "spike 진행"으로 미끄러질 위험이 있었지만, 워크플로 룰(긍정 주장에 적대적
검증, parametrize ≠ derive, brute-force hit ≠ derivation)이 "*먼저 학계 위치부터*
보자"는 정직한 길을 자동으로 강제했다.

**negative result를 정직하게 기록했다.** 사용자가 직관적으로 의심한 "재검산"이
사실로 확인된 순간, 그것을 *덮지 않고* CP25에 명시적으로 적었다. lineage가 빛나는
양성 결과로 닫히지 않더라도, 같은 자리에 다른 사람이 다시 오는 시간을 절약한다.

## 무엇이 아쉬웠나

**처음 사용자 메시지를 받았을 때 spike 가설을 곧바로 분해해 *literature scan을
병렬로 띄우는* 결정이 한 박자 더 빨랐을 수 있다.** 실제 흐름은 사용자가 "spike
가치 평가" 도구로 명시적으로 요청한 뒤에야 병렬 scan이 시작됐다. 다음에는 비슷한
직관이 들어오는 순간 거의 자동으로 literature scan을 먼저 트리거하는 게 좋다.

**postmortem 작성을 처음부터 별도 phase로 잡아두지 않았다.** CP25를 닫고 나서야
"이건 회고로 적어야 한다"는 사용자 지적으로 들어왔다. lineage 자연 닫힘 같은 큰
이벤트가 발생하면 회고를 같은 phase 안에서 자동으로 제안하는 패턴을 워크플로에
넣어두면 좋다.

## 무엇을 배웠나

1. **같은 자유도를 끝까지 미는 사람은 대체로 같은 자리에 도착한다.** 공간 비균질성,
   국소 중력 시간지연, 평균화 backreaction — 셋 다 직관적으로 자연스러운 후보고,
   학계가 25년에 걸쳐 이미 답사한 영역이다. 이건 같은 천장이 진짜라는 부수 증거이지
   우리 직관이 빈약하다는 신호가 아니다.

2. **literature scan은 수치 spike의 *대체재가 아니라 선행 단계*다.** 두 단계를 같은
   순서로 두는 것이 정직성·시간·코드 부피 모두에서 이득이다.

3. **negative result로 lineage가 닫혀도 그 자체가 가치다.** 미래의 같은 직관을 가진
   사람에게 빠른 지도를 제공한다. "어디까지 갔다, 거기서 왜 막혔다"를 기록한 것은
   "성공만 기록한 것"보다 길게 유용하다.

4. **agent harness가 정직성을 자동으로 강제한다.** parallel fan-out + adversarial
   check + 050 천장 가드의 조합이 사용자의 직관 강한 순간에도 "재검산 위험"을 자동
   검출하고 학계 위치부터 보게 했다. 인프라가 *해줘야 하는 일*을 정확히 해줬다.

5. **사용자가 가설 제안과 동시에 자기 의심("재검산인건가?")을 같이 던지면 그게
   결정적 signal이다.** 그 자기 의심을 *덮지 않고 첫 도구로 사용*하면 시간과 정직성
   둘 다 산다.

## 액션 아이템

- [x] CP25를 `004_rough_tanh_numerical_sketch_ko.md`에 추가 (새 수치 없는 학계 위치
  확인 + lineage 자연 닫힘 선언).
- [x] THESIS 보고서 `005_rough_tanh_thesis_report_ko.md` 부록 A에 CP25 행 추가.
- [x] 본 회고(011) 작성.
- [ ] (선택) 향후 비슷한 직관이 들어오면 *바로* literature scan을 병렬로 띄우는
  습관 자동화 — 다음 lineage에서 의식적으로 적용.
- [ ] (선택) Euclid 2026·DESI DR3 결과가 도착하면 CP14의 두 반증 신호(P(k) 스텝,
  γ_eff(k) running)에 대한 외부 답을 *별도 lineage*로 기록 — rough-tanh와 분리.

## 무엇이 안 바뀌었나

- 050 천장 그대로.
- observer mode 그대로.
- 로드맵 상태 그대로.
- foam → δQ 전이 유도라는 본 문제는 여전히 blocked.

이번 회고는 lineage 자연 닫힘과 *25년치 학계 흐름과 직관이 겹친 메타 사건*을
기록한다. 새 증거도, 새 천장도, 새 상태 변화도 없다.

## 참고 인용

- Caldwell, R. R. & Stebbins, A. (2008), "A test of the Copernican principle",
  arXiv:0711.3003.
- Bolejko, K. (2012), "Inhomogeneous cosmological models", arXiv:1211.5033.
- Hu, W. & Takada, M. (2011), "Power tomography for the dark sector",
  arXiv:1104.5500.
- Khoury, J. & Weltman, A. (2004), "Chameleon cosmology",
  arXiv:astro-ph/0405033.
- Hinterbichler, K. & Khoury, J. (2010), "Symmetron fields", arXiv:1001.4525.
- Hogg, D. W. et al. (2020), "Vacuum geodesic dark energy",
  arXiv:1908.02183.
- Buchert, T. (2007), "Dark energy from structure", arXiv:0707.2153.
- Paranjape, A. & Singh, T. P. (2008), "Structure formation, backreaction
  and weak gravitational fields", arXiv:0801.1546.
- Lapi, A. et al. (2025), "Emergent dark energy from structure formation",
  arXiv:2502.05823.
- Smith, R. E. et al. (2003), "Stable clustering, the halo model and
  non-linear cosmological power spectra" (Halofit) — 비선형 클러스터링 스케일
  정의의 표준 참조.
