# QFUDS / Dorito

Quantum Foam Unified Dark Sector 사고실험을 검증하기 위한 작업장.

심심해서 밀어붙여 보는 이론 천체물리/우주론 검증 노트에 가깝다. 목표는 이 아이디어를 옹호하는 것이 아니라, 기존 문헌과 충돌하지 않는 최소 모형으로 끝까지 세워 본 뒤 어디서 깨지는지 확인하는 것이다.

## Core Claim

암흑물질과 암흑에너지는 완전히 분리된 두 물질이 아니라, 양자 시공간 foam의 두 거시적 infrared phase일 수 있다.

```text
dark sector
= foam-wave
+ foam-residual
+ optional remnants
```

- `foam-wave`: 뭉치는 진동 모드. 암흑물질처럼 보이려면 `w ~= 0`, `c_s^2 ~= 0`, `rho ~ a^-3`.
- `foam-residual`: 균일한 잔여 압력 모드. 암흑에너지처럼 보이려면 `w ~= -1`, `rho ~= constant`.
- `remnants`: black/white-hole remnant는 선택적 하위 성분. 핵심 장치가 아니라 정보 순환 보조 항으로 둔다.

논문형 한 줄:

```text
Dark matter and dark energy may be two infrared phases of quantum spacetime foam:
a clustering oscillatory mode with w ~= 0, and a homogeneous residual-pressure mode with w ~= -1.
```

## Dorito Intuition

진공은 비어 있지 않고, 시공간의 미시구조는 foam처럼 요동한다고 둔다. 그 foam의 한 거시적 모드는 뭉치는 진동으로 나타나 암흑물질처럼 행동하고, 다른 모드는 균일한 잔여 압력으로 남아 암흑에너지처럼 행동한다.

이 관점에서 기존 Friedmann 방정식은 폐기하지 않는다. 먼저 다음 치환이 관측을 깨지 않는지 본다.

```text
rho_DM      -> rho_foam_wave
rho_Lambda  -> rho_foam_residual
```

가장 단순한 안정 형태는 다음이다.

```text
rho_dark = rho_foam_wave + rho_foam_residual + rho_remnant

rho_foam_wave     ~ a^-3,    w ~= 0
rho_foam_residual ~ rho_*,   w ~= -1
rho_remnant       = n_r M_r
```

`remnant`는 핵심 장치가 아니다. black/white-hole remnant가 있다면 암흑물질의 일부 후보일 뿐이고, 반드시 질량함수와 abundance 제약을 통과해야 한다.

## Predictions To Kill

이 모델은 맞는 말을 하기보다 죽을 수 있는 예측을 가져야 한다.

1. WIMP식 직접 검출은 계속 null일 가능성이 높다. Dorito에서 암흑물질은 독립 입자라기보다 foam의 집단모드이므로, 핵반동 신호가 없어도 이상하지 않다. 단, 이것만으로 모델이 증명되지는 않는다.
2. 암흑에너지는 완벽한 상수가 아니라 약하게 시간 변화할 수 있다.

```text
w(a) = w_0 + w_a(1 - a)
LCDM:    w_0 = -1, w_a = 0
Dorito:  w_0 ~= -1, |w_a| > 0 but small
```

3. 작은 은하나 은하 중심부에서 collisionless CDM의 NFW cusp보다 완만한 core가 나올 수 있다. 회전곡선을 맞추려면 여전히 `rho_dark(r) ~ 1/r^2` 구간이 필요하지만, 중심부에서는 `rho(r) -> rho_0` 같은 flattening이 가능해야 한다.
4. 암흑물질 분포와 보통물질 분포 사이에 약한 추가 상관성이 남을 수 있다. 보통물질이 foam을 변형시키고, foam이 다시 중력장을 보강하는 feedback이 있다면 은하 형태와 halo 구조가 표준 LCDM보다 직접적으로 묶일 수 있다.
5. 우주상수는 정확한 상수가 아니라 평형값 주변에서 느리게 완화될 수 있다.

```text
d rho_Lambda / dt = -Gamma (rho_Lambda - rho_*)
```

이 식이 맞다면 높은 적색편이의 `H(z)`, BAO scale, supernova distance에 작은 흔적이 남아야 한다.

6. 블랙홀 정보 방출은 완전히 열적이지 않고 late-time radiation에 극도로 미세한 상관관계를 가져야 한다. 이건 현재 천체 관측으로는 거의 검증 불가능하지만, 이론적으로는 Page curve/island류 논의와 맞닿는 항이다.
7. white-hole remnant가 암흑물질 일부라면 허용 질량함수는 좁아야 한다.

```text
rho_remnant = n_r M_r
```

너무 무거우면 microlensing에 걸리고, 너무 가벼우면 구조형성, 증발, 검출 제약에 걸린다. 따라서 "remnant가 있다"가 아니라 "어떤 f(M)가 살아남는가"를 계산해야 한다.

## What Must Survive

QFUDS/Dorito는 다음을 깨면 탈락이다.

- Planck CMB가 맞춘 ΛCDM background와 acoustic structure
- BAO/DESI expansion history
- linear growth와 weak lensing
- 은하 halo 형성 조건
- 작은 sound speed 조건
- black/white-hole remnant abundance 제약

## Current Status

현재 결론은 보수적이다.

QFUDS는 아직 완성 이론이 아니다. 지금 형태만으로는 unified dark fluid, k-essence, scalar-field dark matter, interacting dark energy의 재해석에 가깝다.

새 내용이 되려면 최소 하나가 필요하다.

- foam의 covariant microscopic action
- phase-transfer law `Gamma(a)`의 물리적 유도
- `c_s^2 ~= 0`을 자연스럽게 만드는 perturbation mechanism
- remnant mass spectrum과 abundance 예측
- ΛCDM이나 기존 unified-fluid 모델과 구별되는 관측 신호

## Repository Contents

- `docs/qfuds_research_report.md`: 문헌 대응, 수학적 정식화, 실패 모드, 다음 연구 단계
- `qfuds/background.py`: two-phase background toy model
- `qfuds/growth.py`: smooth residual phase를 둔 linear growth toy model
- `scripts/run_minimal_model.py`: `H(a)`, `Omega(a)`, `w(a)`, `D(a)` CSV 생성
- `outputs/*.csv`: 현재 검증 산출물

## Minimal Run

```bash
python3 scripts/run_minimal_model.py --gamma0 0 --beta 0
python3 scripts/run_minimal_model.py --gamma0 0.03 --beta 5
```

`gamma0 = 0`은 exact ΛCDM limit이다. 이 한계가 맞지 않으면 이후 모형은 볼 필요가 없다.
