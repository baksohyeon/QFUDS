---
doc_id: postmortem-010-rough-tanh-lineage-descent-retro
id: postmortem-010-rough-tanh-lineage-descent-retro
seq: 10
title: "rough tanh lineage 하강 회고 — 반증 가능 신호에서 우주상수 문제까지 (CP13~CP24)"
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

# rough tanh lineage 하강 회고 — 반증 가능 신호에서 우주상수 문제까지 (CP13~CP24)

## 사건 한 줄 요약

worktree-qfuds-rough-tanh 브랜치에서 rough tanh 탐색(004 lineage)을 CP13부터
CP24까지 진행했다. "이 모델을 관측으로 어떻게 반증할 수 있나 → 이론적 천장을
정면으로 두드리면 무엇이 막나 → 끝까지 끼워 맞추면 자유 파라미터가 줄어드나"라는
세 단계를 차례로 내려갔고, **마지막에 남은 두 숫자(상관길이 ξ≈10 Mpc, 그리고
에너지 스케일 meV)가 결국 우주론의 스케일·계층 문제와 우주상수 문제 그 자체**임을
정직하게 확인했다. QFUDS의 상태, 050 천장, observer mode는 전혀 바뀌지 않았다(이
문서를 포함해 모두 연구 흐름 기록일 뿐이다).

## 0. 먼저 알아둘 것

이 회고를 읽는 데 필요한 최소한의 개념만 정리한다.

| 개념 | 설명 |
| --- | --- |
| lineage(004) | 연구가 어떻게 흘러갔는지 남기는 *기록*(provenance)이다. 새 증거도, 상태 변경도 아니다. 프로젝트의 공식 상태는 roadmap이 정한다 |
| CP 로그 | 덧붙이기만 하는(append-only) 체크포인트. 각 CP는 `## CPn` 본문과 `### CPn 결론`으로 이뤄지며, 앞선 결론을 덮어쓰지 않는다 |
| parametrize vs derive | parametrize는 값을 손으로 *깔아 두고* 곡선을 맞추는 것, derive는 미시구조에서 값이 *저절로 나오는* 것이다 |
| 050 천장 | 이 프로젝트가 못 넘는 한계선. "QFUDS가 가정하는 거품(foam) 미시구조에서 출발해 암흑물질·암흑에너지의 전이를 *유도*해 내는 것은 현재 불가능하다(blocked)"는 결론을 줄여 부르는 말이다. 곡선을 *그릴* 수는 있어도 *왜* 그런지를 끌어낼 수는 없다는 뜻 |
| rough proxy | 여기 나오는 모든 모델은 거친 근사다. 제대로 된 검증은 Boltzmann 코드(CLASS/hi_class)로 해야 하고, 그건 Level 3이라 막혀 있다(blocked) |
| observer mode | 새 관측이 들어오는 것 말고는 레포 안에서 새 유도를 하지 않는 상태. 이 세션 전체가 이 모드를 지켰다 |

작업 규약도 정리해 둔다. 그림은 png와 svg로, 수치는 `*_results.csv`로 남긴다. 매 CP마다
`__pycache__`를 지운다. 표준 우주론 식은 코드 안에서 직접 유도·검산하고, 근사를 쓸 때는
"proxy"라고 명시한다. 커밋 전에 `validate_docs.py`와 `research_consistency.py`가
모두 PASS해야 한다. 커밋 메시지는 한글 `docs:` 형식으로 쓰되, 이 lineage 작업에서는
Co-Authored-By를 붙이지 않는다.

## 1. 무엇을 했나 (CP13~CP24 한눈)

12개 체크포인트, 전부 atomic 커밋(1 CP = 1 커밋 = 스크립트+png+svg+csv+문서 섹션).

| CP | 주제 | 한 줄 결론 |
| --- | --- | --- |
| CP13 | 후기 ISW | falsifiable 신호 #3. C_ℓ 비 0.35→0.82 tilt로 균일 저-σ8과 원리적 구별, 단 저-ℓ cosmic variance |
| CP14 | 두 신호 실오차 채점 | w(z) freezing 대표 DESI서 5.5σ·반대 사분면, P(k) 스텝 Stage-IV ~18σ (외부 숫자=예시) |
| CP15 | GDM 점성 c_vis² | 독립 파라미터(c_s²와 다른 k-모양). c_vis²=0이 CP11 재현(잔차 4.2e-8). 천장 재확인 |
| CP16 | 성장지수 γ | γ_eff(z=0)≈0.48 f(R)와 단일스케일 축퇴, 단 γ_eff(k) running으로 구별 가능 |
| CP17 | CMB렌즈 내부모순 | tension 없음 — 늦은 유체라 CMB렌즈(z>1) 거의 안 건드림. CP10(H0)의 반대 결과 |
| CP18 | DESI z>2 Lyα | D_H/r_d z=2.33서 −1.06%(대표 ±1.1% 경계선). 가장 강한 곳에서도 아직 못 죽임 |
| CP19 | Euclid forecast | P(k) 스텝 다중-bin ~24σ, γ running ~24σ 구별. 균일 이동 0σ(sanity) |
| CP20 | 050 천장 직격 | 스펙 3개 → 스케일+코인시던스 문제 2개로 분해. red-team이 한쪽-편향 ξ 사다리 교정 |
| CP21 | ξ 근임계 brute-force | ε=10⁻⁵⁹~10⁻¹¹⁷, τ_Q=10¹¹⁶~10²³³ 극단적 미세조정. 파라미터 reduced 아니라 relocated |
| CP22 | coincidence tracker | IC 튜닝 16 decade 진짜 제거(부분 승리), meV/why-now는 잔존. 2→1 |
| CP23 | meV = 우주상수 문제 | ρ_vac/ρ_Λ 10¹²³. anthropic=select, transmutation=작음만 natural. 아무도 derive 못 함 |
| CP24 | ξ = σ8 스케일 | ξ≈R8(표준물리)=circular, transmutation relocate, Jeans circular. 독립 derive 후보 없음 |

커밋 해시: CP13 `2586b4b` … CP19 `541d77b`, CP20 `ec4a9a7`, CP21 `602fe4c`,
CP22 `ad1e3e1`, CP23 `c0c47b4`, CP24 `1141373`.

## 2. 세 국면 서사

이 세션은 크게 세 국면을 거치며 내려갔다.

**국면 1 — 관측으로 어디서 반증되나 (CP13~CP19).** 직전 결론(S8 tension은 튜닝으로
완화되지만 H0는 오히려 악화되고, 이 모델을 반증할 곳은 DESI의 w(z)와 약중력렌즈
P(k)다)을 *실제 오차 막대*로 검증했다. 먼저 ISW를 세 번째 반증 신호로 추가하고(CP13),
두 신호를 대표 오차로 채점했다(CP14). GDM과 성장지수 γ로 이 모델이 기존 이론 지도
위 어디에 놓이는지 확정하고(CP15·16), CMB렌즈와의 내부 정합성도 통과했다(CP17).
이어 DESI z>2와 Euclid 예측으로 "언제 반증될 수 있나"를 구체화했다(CP18·19). 핵심
교훈은 이렇다. **QFUDS가 진짜 증거를 얻을 수 있는 자리는 ΛCDM과 *갈라지는* 신호
(P(k) 계단, γ running, ISW 기울기)이지, ΛCDM과 함께 부딪치는 공통의 벽이 아니다.**
외부 관측 숫자는 모두 "대표값·예시이지 likelihood가 아니다"로 표시했다(forecast인지
실제 likelihood인지의 경계를 사용자와 명시적으로 합의했다).

**국면 2 — 050 천장을 정면으로 파고들다 (CP20).** 관측으로 모델을 흔드는 대신,
"왜 이 모델이 근본 이론으로 못 올라가는가"라는 한계선 자체를 분석하는 쪽으로 방향을
틀었다. 데이터가 요구하는 자유 파라미터 {ξ, N_X, z*}를 foam order-parameter ansatz
(거품을 하나의 질서변수로 보는 가정)에서 *유도해 보려* 했다. 결과는 돌파가 아니라
**분해**였다. 세 숫자가 (1) 스케일 문제 (2) 코인시던스 문제, 두 가지 기존 난제로
줄어들었다.
이 과정에서 **반대편을 일부러 파고드는 검토(adversarial red-team)**가 내 초안의
한쪽 편향(미시 foam 척도만 늘어놓은 것)을 잡아냈고, 인과/Kibble 지평(~4400 Mpc,
데이터보다 461배 큼)을 추가해 양쪽 극단을 모두 보도록 교정했다. 결론은 같지만 더
정직하고 더 단단해졌다.

**국면 3 — 끝까지 끼워 맞춰 보다 (CP21~CP24).** 사용자 요청으로 "남은 메커니즘을
끝까지 미세조정해 보자"에 들어갔다. 먼저 핵심 전제를 분명히 했다. *끼워 맞추기는
정의상 언제나 맞출 수 있다. 그러니 진짜 출력은 "맞췄냐"가 아니라 튜닝 장부 — 즉
자유 파라미터가 줄어드는지, 아니면 자리만 옮겨가는지 — 다.* CP21(ξ를 근임계성이나
Kibble-Zurek으로 맞추기)에서는 파라미터가 줄지 않고 자리만 옮겨갔고, 그것도 현실적으로
불가능한 수준의 극단적 미세조정이 필요했다. CP22(tracker)에서는 초기조건 튜닝을 16 decade
*실제로* 제거했다(이 세션의 유일한 부분 승리이며, w_φ=−2/3 재현으로 검증했다). 다만
meV 스케일은 끝까지 남았다. 그다음에는 남은 두 숫자 자체로 들어가, CP23(meV =
우주상수 문제)과 CP24(ξ = σ8 스케일 문제)를 다뤘다. 둘 다 가짜 해결로 빠지지 않고
문헌 조사와 튜닝 장부만으로 "아무도 유도하지 못했고, QFUDS도 ΛCDM과 똑같이 이
문제를 그대로 물려받는다"를 분명히 했다.

## 3. 핵심 발견

```text
24개 CP 전체를 꿰뚫는 핵심:
  - 효과 수준(파라미터를 입력으로 가정하고 fit)에선 작동한다.
    ΛCDM과 배경·S8·CMB렌즈·BAO를 모두 통과.
  - 그러나 ΛCDM보다 낫지는 않다(이긴 건 S8를 낮춘 보편 효과 덕이지 고유한 강점이 아니고,
    H0는 오히려 악화).
  - 근본 수준(foam에서 유도)에선 막힌다. 자유 파라미터를 줄이지 못한다.
  - 튜닝 장부의 맨 밑바닥 = 숫자 2개 = 스케일/계층 문제 + 우주상수 문제.
    => QFUDS의 천장 = 이론물리 전체의 두 미해결 난제. QFUDS만의 고유한 실패가 아님.
유일한 부분 승리: tracker attractor가 초기조건 튜닝을 16 decade 제거(CP22).
```

근거 메모: CP22의 부분 승리는 막연한 주장이 아니다. 적분기가 Ratra–Peebles 모델의
물질 지배기 tracker 상태방정식 `w_φ=-0.666`을 해석값 `-2/(α+2)=-0.667`로 재현했고(별도
실행으로 직접 확인했다), 이는 attractor 로직이 옳게 구현됐다는 결정적 증거다. 반면
에너지 스케일 meV가 관측 창에 들어오는 폭은 0.31 decade로 좁아서, "왜 하필 지금
가속이 시작되나(why-now)" 문제는 끝까지 남았다.

## 4. 운영 실수 1건 — git checkout이 미스테이징 문서 편집을 되돌림

### 증상

CP18 커밋 직후 `git show --stat`에 **파일 4개**만 잡혔다(기대한 건 5개: 문서 1 +
asset 4). 문서 섹션(CP18)이 커밋에서 빠지고 asset 4개만 들어간 것이다.

### 원인

직전에 에이전트를 다시 실행하면서 추적 중이던 그림 파일이 의도치 않게 바뀌어 있었고
(예: `fig_cp5_sound_speed.svg`), 이걸 되돌리려고 다음을 실행했다.

```bash
git checkout -- $(git diff --name-only)
```

문제는 그 시점의 `git diff --name-only` 목록에 **아직 스테이징하지 않은 CP18 문서
편집**도 들어 있었다는 점이다. `git checkout`이 그 문서 편집까지 함께 되돌려 버렸다.
그래서 이후 `git add`를 했을 때 문서는 HEAD와 똑같은 상태(=바뀐 게 없음)라 스테이징되지
않았고, 결국 CP18 커밋에는 asset만 들어갔다.

### 해결

문서 섹션과 재현 절을 Edit로 다시 삽입한 뒤(파일이 되돌려진 상태라 "Read first"
에러가 떠서, Read 후 재편집했다), `git commit --amend --no-edit`로 문서를 CP18 커밋에
합쳤다. 그 결과 `d72a135`에 파일 5개(문서 1 + asset 4)가 모두 들어갔다.

### 결정 근거

| 선택지 | 채택? | 근거 |
| --- | --- | --- |
| 새 커밋으로 문서만 추가 | ✗ | atomic 규약 위반(1 CP = 1 커밋). 문서와 asset이 두 커밋으로 쪼개진다 |
| `commit --amend`로 합침 | ✓ | 로컬 워크트리 브랜치라 아직 push 전이라서 amend가 안전하고, atomic 규약도 복원된다 |

## 5. 결정 / 열린 질문

이 세션이 닫지 않고 남긴 *유일하게 열린 결정*은 이것이다.

```text
QFUDS를 어떤 레벨로 볼 것인가?
  (a) 효과모델: ξ와 meV를 입력으로 가정. fit은 되지만 ΛCDM을 이기지는 못하고
      (파라미터를 더 쓰니까), 증거는 ΛCDM과 갈라지는 반증 가능 신호(P(k)/ISW/γ)에서만 나온다.
      observer mode와 잘 맞는다.
  (b) 근본이론: foam에서 유도하기를 고집. 그게 QFUDS의 원래 정체성이자 050 천장이다.
      CP20~24가 보여준 대로 지금은 막혀 있다(blocked).
"그냥 가정하면 되잖아"는 (a)를 고른다는 뜻이다. 나쁜 선택이 아니라,
그게 무슨 선택인지 알고 고르면 된다.
```

이건 roadmap이 내릴 결정이지 lineage가 정할 일이 아니다. observer mode 아래에서는
두 선택지 모두 결국 "새 관측을 기다린다"로 수렴한다(Euclid 2026년 10월, DESI 데이터
릴리스 계속).

## 6. 재발 방지 / 운영 메모

- **`git checkout -- $(git diff --name-only)`는 금지 패턴이다.** 바뀐 그림만 되돌릴
  때는 대상 파일을 *직접 지정*해야 한다(`git checkout -- docs/.../fig_cp5_sound_speed.svg`).
  와일드카드나 명령 치환을 쓰면 아직 스테이징하지 않은 정당한 편집까지 함께 삼킨다.
  이후 CP19~24에서는 그림과 결과 파일만 골라 되돌리는
  `git diff --name-only -- 'fig_*' '*_results.csv'`로 안전하게 처리했다.
- **무언가를 줄였다·풀었다 같은 긍정 주장 CP는 반대 검증이 필수다.** CP20(초안 편향),
  CP22(부분 승리 주장), CP23·24(우주상수 문제, 가짜 해결 위험이 가장 큼)는 red-team이나
  별도 재실행으로 검증한 뒤 커밋했다. 반대로 막혔다·자리만 옮겼다 같은 부정적 결과는
  과대주장 위험이 없는 안전한 방향이라 가볍게만 검증했다.
- **외부 관측 숫자는 항상 "대표값·예시이지 likelihood/공분산이 아니다"로 표시한다.**
  forecast(연구 흐름 기록)와 실제 likelihood(증거, 쓰면 observer mode 위반)의 경계를
  문서에 명시한다.
- **워크트리에서 디렉터리 이동에 주의한다.** Bash 작업 디렉터리가 assets 폴더로
  옮겨가면 `scripts/*.py` 경로가 깨진다. 검사와 커밋은 워크트리 루트의 절대경로에서
  실행한다.
- 재발 방지를 위한 코드 변경은 없다 — 코드가 아니라 작업 절차로 막는다.

## 7. 타임라인

- CP13~CP19: 관측 반증 신호 확장과 실제 오차 채점(커밋 `2586b4b`…`541d77b`).
- CP18 커밋 도중 git checkout 사고 발생 → `--amend`로 복구(`d72a135`).
- CP20: 이론적 천장 정면 두드리기 + red-team 교정(`ec4a9a7`).
- CP21·CP22: 끝까지 끼워 맞추기 튜닝 장부 — 자리만 옮김 / 부분 환원(`602fe4c`, `ad1e3e1`).
- CP23·CP24: 가장 깊은 곳의 두 숫자 = 우주상수 문제·스케일 문제(`c0c47b4`, `1141373`).
- 회고 작성(이 문서, seq 010). roadmap·050 천장·observer mode가 바뀌지 않았음을 확인.
