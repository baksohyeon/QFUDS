---
doc_id: postmortem-010-rough-tanh-lineage-descent-retro
id: postmortem-010-rough-tanh-lineage-descent-retro
seq: 10
title: "rough tanh lineage 하강 회고 — 관측 falsifiable에서 우주상수 문제까지 (CP13~CP24)"
doc_type: postmortem
type: postmortem
stage: reference
status: reference
wiki_status: active
evidence_role: provenance
depends_on:
  - qfuds_lineage_rough_tanh_numerical_sketch_ko
  - postmortem-009-qfuds-observer-mode-closing-retro
  - roadmap
next_gate: provenance only; roadmap이 상태 권위; observer mode 유지; 050 천장 무손상
date: 2026-06-12
context: worktree-qfuds-rough-tanh 브랜치에서 004 rough-tanh lineage 스케치 CP13~CP24 진행 후 마무리 회고
audience: 주니어 개발자
length: 서사형 마무리 회고
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
    note: "rough-tanh lineage CP13~CP24 12개 atomic 커밋 완료 후, 작업 전체 흐름과 운영 실수 1건을 회고로 기록."
tags: [postmortem, retrospective, lineage, rough-tanh, observer-mode, qfuds]
relations:
  - docs/wiki/lineage/004_rough_tanh_numerical_sketch_ko.md
  - docs/05_next_steps/000_roadmap.md
  - docs/wiki/postmortem/009-20260611-dorito-qfuds-observer-mode-closing-retro.md
code_refs:
  - file: docs/wiki/lineage/assets/004_rough_tanh/
    note: "CP13~CP24 스크립트 12개 + png/svg/csv. 전부 rough proxy, parametrize-not-derive."
---

# rough tanh lineage 하강 회고 — 관측 falsifiable에서 우주상수 문제까지 (CP13~CP24)

## 사건 한 줄 요약

worktree-qfuds-rough-tanh에서 rough tanh 탐색(004 lineage)을 CP13~CP24까지 밀었고,
"관측으로 어떻게 죽나 → 천장을 직격하면 뭐가 막나 → brute-force로 맞추면 손잡이가
주나"를 순서대로 내려가, **결국 남은 두 숫자(ξ≈10 Mpc, meV)가 곧 스케일/계층 문제와
우주상수 문제**임을 정직하게 못박았다. QFUDS 상태·050 천장·observer mode는 한 톨도
안 바뀌었다(이 문서를 포함해 전부 provenance).

## 0. 사전 지식

이 회고를 읽는 데 필요한 최소 개념만.

| 개념 | 한 줄 |
| --- | --- |
| lineage(004) | 연구 흐름 *기록*(provenance). 새 증거도, 상태 변경도 아님. roadmap이 상태 권위 |
| CP 로그 | append-only 체크포인트. 각 CP = `## CPn` 본문 + `### CPn 결론`. 이전 결론 덮지 않음 |
| parametrize vs derive | parametrize = 손으로 값을 *깔고* 곡선 맞춤. derive = 미시구조에서 값이 *나옴*. 050 천장 = derive가 막힘 |
| rough proxy | 모든 toy는 거친 근사. 진짜 검증은 CLASS/hi_class(Level 3, blocked) |
| observer mode | 새 관측 외엔 레포 내부 추가 유도 안 함. 이 세션 전체가 이 모드를 지킴 |

핵심 규약: 그림 png+svg, 수치 *_results.csv, 매 CP `__pycache__` 삭제, 표준식은
직접 유도·검산, 근사는 "proxy" 명시, 커밋 전 `validate_docs.py` +
`research_consistency.py` PASS, 한글 `docs:` 커밋(Co-Authored-By 금지).

## 1. 무엇을 했나 (CP13~CP24 한눈)

12개 체크포인트, 전부 atomic 커밋(1 CP = 1 커밋 = 스크립트+png+svg+csv+문서 섹션).

| CP | 주제 | 한 줄 결론 |
| --- | --- | --- |
| CP13 | 후기 ISW | falsifiable 신호 #3. C_ℓ 비 0.35→0.82 tilt로 균일 저-σ8과 원리적 구별, 단 저-ℓ cosmic variance |
| CP14 | 두 신호 실오차 채점 | w(z) freezing 대표 DESI서 5.5σ·반대 사분면, P(k) 스텝 Stage-IV ~18σ (외부 숫자=예시) |
| CP15 | GDM 점성 c_vis² | 독립 손잡이(c_s²와 다른 k-모양). c_vis²=0이 CP11 재현(잔차 4.2e-8). 천장 재확인 |
| CP16 | 성장지수 γ | γ_eff(z=0)≈0.48 f(R)와 단일스케일 축퇴, 단 γ_eff(k) running으로 구별 가능 |
| CP17 | CMB렌즈 내부모순 | tension 없음 — 늦은 유체라 CMB렌즈(z>1) 거의 안 건드림. CP10(H0)의 반대 결과 |
| CP18 | DESI z>2 Lyα | D_H/r_d z=2.33서 −1.06%(대표 ±1.1% 경계선). 가장 강한 곳에서도 아직 못 죽임 |
| CP19 | Euclid forecast | P(k) 스텝 다중-bin ~24σ, γ running ~24σ 구별. 균일 이동 0σ(sanity) |
| CP20 | 050 천장 직격 | 스펙 3개 → 스케일+코인시던스 문제 2개로 분해. red-team이 한쪽-편향 ξ 사다리 교정 |
| CP21 | ξ 근임계 brute-force | ε=10⁻⁵⁹~10⁻¹¹⁷, τ_Q=10¹¹⁶~10²³³ 칼날 튜닝. 손잡이 reduced 아니라 relocated |
| CP22 | coincidence tracker | IC 튜닝 16 decade 진짜 제거(부분 승리), meV/why-now는 잔존. 2→1 |
| CP23 | meV = 우주상수 문제 | ρ_vac/ρ_Λ 10¹²³. anthropic=select, transmutation=작음만 natural. 아무도 derive 못 함 |
| CP24 | ξ = σ8 스케일 | ξ≈R8(표준물리)=circular, transmutation relocate, Jeans circular. 독립 derive 후보 없음 |

커밋 해시: CP13 `2586b4b` … CP19 `541d77b`, CP20 `ec4a9a7`, CP21 `602fe4c`,
CP22 `ad1e3e1`, CP23 `c0c47b4`, CP24 `1141373`.

## 2. 세 국면 서사

이 세션은 거칠게 세 국면으로 내려갔다.

**국면 1 — 관측으로 어디서 죽나 (CP13~CP19).** 직전 결론(S8는 튜닝 완화, H0 악화,
죽일 곳은 DESI w(z)+렌즈 P(k))을 *실제 오차*로 밀었다. ISW를 세 번째 falsifiable
신호로 추가(CP13), 두 신호를 대표 오차로 채점(CP14), GDM/γ로 이론 위치 확정(CP15·16),
CMB렌즈 내부 정합성 통과(CP17), DESI z>2와 Euclid forecast로 "언제 죽나"를 구체화
(CP18·19). 핵심 교훈: **QFUDS의 진짜 증거 자리는 ΛCDM과 *갈라지는* 신호(P(k) 스텝·γ
running·ISW tilt)지, 공유하는 벽이 아니다.** 외부 관측 숫자는 전부 "대표값/예시,
likelihood 아님"으로 라벨링(사용자와 명시적으로 A=forecast vs B=likelihood 경계 합의).

**국면 2 — 천장을 직격 (CP20).** "관측 말고 천장 자체를 쳐보자"로 전환. 데이터가
원하는 손잡이 {ξ, N_X, z*}를 foam order-parameter ansatz에서 *유도 시도*. 결과는
돌파가 아니라 **분해**: 스펙 3개가 (1) 스케일 문제 + (2) 코인시던스 문제로 줄었다.
이때 **adversarial red-team**이 내 초안의 한쪽-편향(미시 foam 척도만 나열)을 잡아,
인과/Kibble 지평(~4400 Mpc, 461배 큼)을 추가해 양쪽 horn으로 교정했다 — 결론은
같지만 더 정직·더 강해짐.

**국면 3 — brute-force로 마저 맞춰봐 (CP21~CP24).** 사용자 요청으로 "남은 메커니즘을
brute-force 미세조정"에 들어갔다. 핵심 전제를 먼저 박음: *brute-force는 정의상
맞춘다. 출력은 "맞췄냐"가 아니라 튜닝 장부(손잡이가 주나 옮기나)다.* CP21(ξ
근임계/KZ): relocated, 칼날 튜닝. CP22(tracker): IC 튜닝 16 decade를 *진짜로* 제거
(이 세션 유일한 부분 승리, w_φ=−2/3 재현으로 검증) 하지만 meV는 잔존. 그다음 남은 두
숫자 자체에 들어가 CP23(meV=우주상수 문제)·CP24(ξ=σ8 스케일 문제). 둘 다 환각(가짜
해결) 없이 survey+ledger로 "아무도 derive 못 함, QFUDS가 ΛCDM과 똑같이 상속"을 못박음.

## 3. 핵심 발견

```text
22개 CP를 관통하는 한 줄:
  - 효과 수준(가정→fit)에선 작동한다. ΛCDM과 배경·S8·CMB렌즈·BAO 다 통과.
  - 그러나 ΛCDM보다 낫지 않다(이김은 S8 튜닝 덕, 고유 아님; H0는 악화).
  - 근본 수준(foam에서 유도)에선 막힌다. 손잡이를 못 줄인다.
  - 튜닝 장부의 바닥 = 2개 숫자 = 스케일/계층 문제 + 우주상수 문제.
    => QFUDS의 천장 = 이론물리 전체의 두 미해결 문제. QFUDS 고유 실패 아님.
유일한 부분 승리: tracker attractor가 초기조건 튜닝을 16 decade 제거(CP22).
```

`evidence` 노트: CP22의 부분 승리는 hand-wave가 아니다. 적분기가 Ratra–Peebles
물질기 tracker 상태방정식 `w_φ=-0.666`을 해석값 `-2/(α+2)=-0.667`로 재현(독립
실행으로 직접 확인) → attractor 로직이 옳다는 결정적 증거. 반면 meV 창은 0.31 decade로
좁아 why-now는 잔존.

## 4. 운영 실수 1건 — git checkout이 미스테이징 문서 편집을 되돌림

### 증상

CP18 커밋 직후 `git show --stat`이 **4 files**만 보였다(기대 5: 문서+asset 4).
문서 섹션(CP18)이 커밋에서 빠지고 asset 4개만 들어감.

### 원인

직전에 agent 재실행으로 생긴 *추적 도면 드리프트*(예: `fig_cp5_sound_speed.svg`)를
되돌리려고 다음을 실행:

```bash
git checkout -- $(git diff --name-only)
```

그 시점 `git diff --name-only`에는 **아직 stage 안 한 CP18 문서 편집**도 포함돼 있었고,
`git checkout`이 그것까지 같이 되돌려버렸다. 이후 `git add` 시 문서는 HEAD와 동일
상태(=변경 없음)라 스테이징되지 않았고, CP18 커밋엔 asset만 들어감.

### 해결

문서 섹션·repro를 다시 Edit로 삽입한 뒤(파일이 reverted돼 "Read first" 에러 →
Read 후 재편집), `git commit --amend --no-edit`로 문서를 CP18 커밋에 합쳤다. 결과
`d72a135`에 5 files(문서+asset 4) 완비.

### 결정 근거

| 선택지 | 채택? | 근거 |
| --- | --- | --- |
| 새 커밋으로 문서만 추가 | ✗ | atomic 규약 위반(1 CP = 1 커밋). 문서/asset 분리됨 |
| `commit --amend`로 합침 | ✓ | 로컬 워크트리 브랜치(미push)라 amend 안전. atomic 복원 |

## 5. 결정 / 열린 질문

이 세션이 닫지 않고 남긴 *유일한 열린 결정*:

```text
QFUDS를 어떤 레벨로 볼 것인가?
  (a) 효과모델: ξ·meV를 input으로 가정. fit은 되지만 ΛCDM 못 이김(파라미터 더 씀),
      증거는 falsifiable 신호(P(k)/ISW/γ)에서만. observer mode와 정합.
  (b) 근본이론: foam에서 유도 고집. 그게 QFUDS의 원래 정체성이자 050 천장.
      CP20~24가 보인 대로 현재 blocked.
"가정하면 되잖아"는 (a)를 고른다는 뜻 — 나쁜 게 아니라, 그게 무슨 선택인지 알고 고르면 됨.
```

이건 로드맵 결정이지 lineage가 정할 게 아니다. observer mode 하에선 둘 다 "새 관측
대기"로 수렴한다(Euclid 2026.10, DESI DR 계속).

## 6. 재발 방지 / 운영 메모

- **`git checkout -- $(git diff --name-only)` 금지 패턴.** 드리프트만 되돌릴 땐 대상
  파일을 *명시*하라(`git checkout -- docs/.../fig_cp5_sound_speed.svg`). 와일드/명령치환은
  스테이징 안 한 정당한 편집을 삼킨다. 이후 CP19~24는 도면만 골라 되돌리는
  `git diff --name-only -- 'fig_*' '*_results.csv'`로 안전 처리.
- **positive 주장 CP는 adversarial 검증 필수.** CP20(초안 편향)·CP22(부분 승리
  주장)·CP23/24(우주상수 문제, 환각 최대 위험)는 red-team 또는 독립 재실행으로
  검증 후 커밋. negative/relocated 결과는 안전 방향이라 라이트 검증.
- **외부 관측 숫자는 항상 "대표값/예시, likelihood/공분산 아님"으로 라벨.** A(forecast,
  provenance) vs B(real likelihood, evidence, observer mode 위반) 경계를 문서에 명시.
- **워크트리 cd 주의.** Bash wd가 assets 디렉터리로 이동하면 `scripts/*.py` 경로가
  깨진다. audit/커밋은 워크트리 루트 절대경로에서 실행.
- 재발 방지 코드 변경 없음 — by process, not by code.

## 7. 타임라인

- CP13~CP19: 관측 falsifiable 신호 확장·실오차 채점 (커밋 `2586b4b`…`541d77b`).
- CP18 커밋 중 git checkout 사고 → `--amend`로 복구(`d72a135`).
- CP20: 천장 직격 + red-team 교정(`ec4a9a7`).
- CP21·CP22: brute-force 튜닝 장부 — relocated / 부분 환원(`602fe4c`, `ad1e3e1`).
- CP23·CP24: 최심층 두 숫자 = 우주상수·스케일 문제(`c0c47b4`, `1141373`).
- 회고 작성(이 문서, seq 010). roadmap/050/observer mode 무손상 확인.
