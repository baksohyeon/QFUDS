# Result 001: v0.3 Gamma-Law Scan

Date: 2026-06-08

## What Did We Learn?

The first useful constraint on `Gamma(a)` is timing. A transfer law that is active during matter domination can destroy the background history when integrated backward from present-day densities. Low-redshift gated transfer is safer at background level.

The scan also confirmed a conceptual limit:

```text
free Gamma(a) -> ordinary interacting dark energy
Gamma(a)=0    -> LCDM
```

Therefore QFUDS needs a physically fixed transfer law, not only a fitted one.

## Did The Model Survive?

Only in a narrow background-level sense.

- The zero-transfer model survives because it is LCDM.
- Power-law and horizon-entropy-gated laws survive as ordinary interacting dark-energy examples.
- Collapsed-fraction, black-hole-entropy, and star-formation proxies survive the minimal background checks and remain worth testing.
- Constant and ungated growth-driven transfer fail at the tested amplitudes.

No v0.3 result establishes perturbation stability, CMB viability, or novelty.

## Why?

The failing laws are too active too early. They can produce negative `rho_B` when the present-day boundary condition is integrated backward and can move `H(a)` away from the LCDM-like early universe.

The surviving toy laws are mostly low-redshift gates. They leave the early universe close to LCDM and defer transfer until structure formation, black-hole growth, or star formation becomes significant.

## What Failed?

1. Constant transfer with `gamma0=0.01`.
2. Ungated growth-driven transfer with `gamma0=0.01`.
3. Any claim that background-level survival proves QFUDS as a new theory.
4. Any claim that black-hole or star-formation proxies are derived microphysics.

## What Became The Next Target?

The next target is not more background scanning. It is perturbation-level specification:

1. define phase-A perturbations;
2. define whether phase B is exactly smooth;
3. define transfer perturbations `delta_Q`;
4. identify stability and sound-speed conditions;
5. implement the surviving candidates in CLASS or CAMB;
6. compare CMB and matter power against LCDM.

Evidence:

- `docs/04_results/qfuds_v0_3_gamma_laws.md`
- `docs/03_experiments/exp_001_gamma_scan_v03.md`
- `outputs/qfuds_*gamma*.csv`
- `tests/test_gamma_v03.py`
