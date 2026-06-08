# QFUDS / Dorito

Quantum Foam Unified Dark Sector 사고실험을 검증하기 위한 작업장.

목표는 이 아이디어를 옹호하는 것이 아니라, 기존 우주론 문헌과 충돌하지 않는 최소 모형으로 끝까지 밀어붙인 뒤 어디서 깨지는지 확인하는 것이다.

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

## What Must Survive

QFUDS/Dorito는 다음을 깨면 탈락이다.

- Planck CMB가 맞춘 ΛCDM background와 acoustic structure
- BAO/DESI expansion history
- linear growth와 weak lensing
- 은하 halo 형성 조건
- 작은 sound speed 조건
- black/white-hole remnant abundance 제약

현재 안전한 수학적 형태는 기존 Friedmann 방정식을 유지하는 effective dark sector다.

```text
rho_dark = rho_foam_wave + rho_foam_residual + rho_remnant
rho_foam_wave     ~ a^-3
rho_foam_residual ~ rho_*
rho_remnant       = n_r M_r
```

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
