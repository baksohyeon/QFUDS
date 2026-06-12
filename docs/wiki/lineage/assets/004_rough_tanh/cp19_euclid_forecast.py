"""
CP19: a representative Euclid-like TOMOGRAPHIC weak-lensing forecast for the two
falsifiable QFUDS handles — the CP9 P(k) STEP and the CP16 γ_eff(k) RUNNING.

WHY EUCLID, WHY NOW
  Euclid's first cosmology (weak-lensing / 3x2pt) data lands ~Oct 2026. Weak
  lensing is exactly the instrument for our two scale-dependent fingerprints:
    - CP9   : a SCALE-DEPENDENT step T(k)=P_QFUDS/P_LCDM at k_J≈1/ξ (c_s²=4.6e-6),
    - CP16  : an effective growth index γ_eff(k) that RUNS with scale (~0.22→0.55).
  CP14 scored the step with a SINGLE-bin, crude 2D-mode-count Fisher (~18σ). Here
  we UPGRADE that to a proper multi-bin tomographic shear (convergence) Fisher:
  representative source n(z), ~10 equal-count tomographic bins, full Limber
  cross-spectra C_ℓ^{ij}, Gaussian covariance with shape noise, and amplitude
  marginalization (overall AND per-bin) so a uniform low-σ8 cannot fake the step.

FRAMING — read this (mode A = forecast/positioning, NOT a likelihood)
  - EXPLORATORY sandbox. PARAMETRIZE-not-DERIVE. The whole w(a)/c_s²/η-Jeans stack
    is phenomenological; nothing here is derived from foam microphysics. The
    "050 ceiling" (deriving the dark sector, δQ transfer, the true c_eff² from the
    foam sector) STANDS UNTOUCHED. Observer mode UNTOUCHED. NOT evidence, NOT a
    roadmap change.
  - The Euclid survey CONFIG (f_sky, n_eff, n(z) shape, #bins, σ_ε) is a
    REPRESENTATIVE Euclid-like weak-lensing forecast configuration. The survey
    SCALE is sourced: Euclid Q1 (2025-03-19) covered 63 deg² = 0.45% of the
    nominal survey → nominal ≈ 14000 deg² (f_sky ≈ 0.34), so f_sky≈0.36
    (~15000 deg²) is the right order.
        SOURCE: https://www.euclid-ec.org/public/press-releases/euclid-quick-data-release-1/
        (context: https://www.nasa.gov/missions/euclid/esa-previews-euclid-missions-deep-view-of-dark-universe/)
    The detailed weak-lensing numbers (n_eff≈30 gal/arcmin², σ_ε≈0.3 per
    component, source z peaking z~0.7 / median ~0.9, ~10 tomographic bins) are the
    standard representative Euclid forecast configuration. This is a
    REPRESENTATIVE, SOURCED forecast — it is NOT a likelihood, ingests NO real
    data vector or covariance, and stores NO data.
  - The REAL detectability verdict needs the coupled clustering-DE perturbations
    in CLASS / hi_class with a real Euclid covariance. That is Level 3 and BLOCKED.
    Everything here is a back-of-envelope stand-in for that blocked computation.

PROXY LIMITS (stated loudly, not hidden):
  Gaussian covariance (no non-Gaussian / SSC); LINEAR P(k) (no nonlinear/baryon
  boost — high-k is a linear extrapolation AND shape-noise-dominated); single
  Limber projection; sharp top-hat tomographic bins with NO photo-z scatter; NO
  intrinsic alignments, NO baryonic feedback, NO multiplicative shear bias beyond
  the per-bin amplitude marginalization; common ΛCDM geometry for distances (the
  QFUDS V2 background ≈ ΛCDM at low z, so the signal isolated here is GROWTH, not
  geometry). Absolute SNR is uncertain by a factor of a few; robust statements are
  (i) the multi-bin vs single-bin comparison, (ii) the uniform-shift→0 sanity.
"""
from __future__ import annotations

import csv
import numpy as np
from scipy.integrate import cumulative_trapezoid
from scipy.optimize import brentq
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

import model as M
import cp5_sound_speed as cp5          # density-driven background (E, rho_x)
import cp16_growth_index as cp16       # scale-dependent growth D(k,a), γ_eff machinery

# =========================================================================== #
# Representative Euclid-like weak-lensing configuration (SOURCED scale; NOT a
# likelihood). See header for the Euclid Q1 press-release provenance.
# =========================================================================== #
F_SKY = 0.36                  # ~15000 deg² (Euclid Q1: 63 deg² = 0.45% of nominal)
N_EFF_ARCMIN2 = 30.0          # effective source density, gal / arcmin²
SIGMA_EPS = 0.30              # shape noise per ellipticity component
N_BINS = 10                   # tomographic redshift bins (equal galaxy counts)
Z0_TARGET_MEDIAN = 0.90       # n(z) ∝ z² exp(-(z/z0)^1.5), z0 set for median ~0.9
NZ_POW = 1.5                  # the (z/z0)^1.5 fall-off (standard Euclid-like form)

C2 = 4.6e-6                   # CP9/CP16 data-fit c_eff² (ξ≈10 Mpc)
OMEGA_M = M.OMEGA_M0_LCDM     # 0.315, common geometry/growth matter fraction
H0 = M.H0_CMB                 # 67.4 km/s/Mpc
C_KM_S = M.C_KM_S
H0_OVER_C = H0 / C_KM_S       # Mpc^-1
DH = C_KM_S / H0              # Hubble distance, Mpc
H_LITTLE = H0 / 100.0         # 0.674
NS = 0.965                    # primordial tilt
SIGMA8 = 0.81                 # ΛCDM σ8 normalization (z=0)
OMEGA_B = M.OMEGA_B0          # 0.049

ARCMIN_PER_RAD = 180.0 * 60.0 / np.pi
N_SR_TOTAL = N_EFF_ARCMIN2 * ARCMIN_PER_RAD ** 2     # gal / steradian (all bins)

# ℓ grid (weak-lensing): log-spaced; Δℓ from bin widths.
ELL = np.unique(np.round(np.logspace(np.log10(30), np.log10(3000), 36))).astype(float)


# --------------------------------------------------------------------------- #
# 1. Linear matter power spectrum P0(k) at z=0 (BBKS transfer, σ8-normalized).
#    BBKS (Bardeen+ 1986) with Sugiyama (1995) Γ. Textbook; assert T(k→0)→1.
# --------------------------------------------------------------------------- #
def _bbks_T(k_mpc):
    """BBKS transfer function. k in Mpc^-1 (converted to h/Mpc internally)."""
    # Sugiyama-corrected shape parameter Γ (baryon suppression)
    gamma = OMEGA_M * H_LITTLE * np.exp(-OMEGA_B - np.sqrt(2.0 * H_LITTLE) * OMEGA_B / OMEGA_M)
    q = (k_mpc / H_LITTLE) / gamma           # k in h/Mpc, then /Γ
    q = np.maximum(q, 1e-12)
    T = (np.log(1.0 + 2.34 * q) / (2.34 * q)) * \
        (1.0 + 3.89 * q + (16.1 * q) ** 2 + (5.46 * q) ** 3 + (6.71 * q) ** 4) ** (-0.25)
    return T


# sanity: T(k→0) → 1
assert abs(_bbks_T(np.array([1e-6]))[0] - 1.0) < 1e-3, "BBKS T(k→0) must → 1"


def _sigma8_sq(amp):
    """σ8² for P0=amp·k^ns·T² with a top-hat at R=8 Mpc/h."""
    R = 8.0 / H_LITTLE                                   # Mpc
    k = np.logspace(-4, 2, 4000)                         # Mpc^-1
    x = k * R
    W = 3.0 * (np.sin(x) - x * np.cos(x)) / x ** 3
    P0 = amp * k ** NS * _bbks_T(k) ** 2
    integ = k ** 2 * P0 * W ** 2 / (2.0 * np.pi ** 2)
    return np.trapezoid(integ, k)


# normalize P0 so σ8(z=0)=0.81
_AMP = 1.0
_AMP = SIGMA8 ** 2 / _sigma8_sq(1.0)
assert abs(np.sqrt(_sigma8_sq(_AMP)) - SIGMA8) < 1e-6, "σ8 normalization failed"


def P0_lcdm(k_mpc):
    """Linear ΛCDM P(k) at z=0 [Mpc³], σ8-normalized."""
    return _AMP * k_mpc ** NS * _bbks_T(k_mpc) ** 2


# --------------------------------------------------------------------------- #
# 2. Scale-dependent growth ratio R(k,a)=[D_QFUDS(k,a)/D_LCDM(a)]² on a grid.
#    Reuses cp16.growth_qfuds (η-Jeans, density-driven bg) and cp16.growth_lcdm.
#    Both ODEs share the IC D=A_I at a=A_I → ratio is a clean common-primordial
#    growth ratio (exactly CP9's T(k), now resolved in a).
# --------------------------------------------------------------------------- #
A_I = cp16.A_I
N_GROWTH = np.linspace(np.log(A_I), 0.0, 320)
A_GROWTH = np.exp(N_GROWTH)
K_GROWTH = np.logspace(-2.5, 0.7, 44)          # 0.003 .. 5 Mpc^-1


def build_growth_grids():
    a_l, D_l, _ = cp16.growth_lcdm(N_GROWTH)
    D_l = np.asarray(D_l)
    DQ = np.empty((K_GROWTH.size, A_GROWTH.size))
    for i, k in enumerate(K_GROWTH):
        _, D_q, _ = cp16.growth_qfuds(N_GROWTH, C2, k)
        DQ[i] = np.asarray(D_q)
    R = (DQ / D_l[None, :]) ** 2                  # [D_Q/D_L]²  (k, a)
    gL = D_l / D_l[-1]                             # D_LCDM(a)/D_LCDM(1)
    return a_l, D_l, R, gL


A_L, D_L, R_GRID, GL = build_growth_grids()
LOGK_G = np.log(K_GROWTH)


def _interp_ka(grid, k_mpc, a):
    """Bilinear-in-(log k, a) lookup with edge clamping (large/small-scale plateaus)."""
    lk = np.clip(np.log(k_mpc), LOGK_G[0], LOGK_G[-1])
    aa = np.clip(a, A_GROWTH[0], A_GROWTH[-1])
    ik = np.clip(np.searchsorted(LOGK_G, lk) - 1, 0, len(LOGK_G) - 2)
    ia = np.clip(np.searchsorted(A_GROWTH, aa) - 1, 0, len(A_GROWTH) - 2)
    fk = (lk - LOGK_G[ik]) / (LOGK_G[ik + 1] - LOGK_G[ik])
    fa = (aa - A_GROWTH[ia]) / (A_GROWTH[ia + 1] - A_GROWTH[ia])
    g00 = grid[ik, ia]; g10 = grid[ik + 1, ia]
    g01 = grid[ik, ia + 1]; g11 = grid[ik + 1, ia + 1]
    return (g00 * (1 - fk) * (1 - fa) + g10 * fk * (1 - fa)
            + g01 * (1 - fk) * fa + g11 * fk * fa)


def Rstep(k_mpc, a):
    return _interp_ka(R_GRID, k_mpc, a)


def gL_of_a(a):
    return np.interp(np.clip(a, A_GROWTH[0], A_GROWTH[-1]), A_GROWTH, GL)


def P_lcdm(k_mpc, a):
    return P0_lcdm(k_mpc) * gL_of_a(a) ** 2


def P_qfuds(k_mpc, a):
    return P_lcdm(k_mpc, a) * Rstep(k_mpc, a)


# --------------------------------------------------------------------------- #
# 3. Representative source n(z) and equal-count tomographic bins.
# --------------------------------------------------------------------------- #
def nz_unnormed(z, z0):
    return z ** 2 * np.exp(-(z / z0) ** NZ_POW)


def _median_of(z0, zg):
    n = nz_unnormed(zg, z0)
    cdf = cumulative_trapezoid(n, zg, initial=0.0)
    cdf /= cdf[-1]
    return float(np.interp(0.5, cdf, zg))


def build_tomography():
    zg = np.linspace(1e-3, 4.0, 4000)
    z0 = brentq(lambda z0: _median_of(z0, zg) - Z0_TARGET_MEDIAN, 0.2, 1.2)
    n = nz_unnormed(zg, z0)
    cdf = cumulative_trapezoid(n, zg, initial=0.0)
    cdf /= cdf[-1]
    # equal-count bin edges (quantiles of the source distribution)
    q = np.linspace(0.0, 1.0, N_BINS + 1)
    edges = np.interp(q, cdf, zg)
    z_med = _median_of(z0, zg)
    z_peak = float(zg[np.argmax(n)])
    return zg, n, z0, edges, z_med, z_peak


Z_NZ, N_NZ, Z0, BIN_EDGES, Z_MED, Z_PEAK = build_tomography()


# --------------------------------------------------------------------------- #
# 4. Tomographic convergence kernels and Limber cross-spectra.
#    g_i(z_l) = ∫_{z_l}^{∞} n_i(z_s)(1 - χ_l/χ_s) dz_s     (lensing efficiency)
#    W_i(z_l) = (3/2) Ω_m (H0/c)² (1+z_l) χ_l g_i(z_l)      (convergence kernel)
#    C_ℓ^{ij} = ∫ dχ W_i W_j P(ℓ/χ, a) / χ²                 (Limber)
# --------------------------------------------------------------------------- #
def comoving_chi_grid():
    z = np.linspace(1e-4, 3.5, 1400)
    E = np.array([float(M.E_LCDM(1.0 / (1.0 + zi))) for zi in z])
    chi = DH * cumulative_trapezoid(1.0 / E, z, initial=0.0)     # Mpc
    return z, chi, E


Z_LOS, CHI_LOS, E_LOS = comoving_chi_grid()


def per_bin_nz_normalized():
    """Normalized n_i(z) on Z_LOS for each tomographic bin (sharp top-hat in true z)."""
    bins = []
    for i in range(N_BINS):
        lo, hi = BIN_EDGES[i], BIN_EDGES[i + 1]
        ni = nz_unnormed(Z_LOS, Z0) * ((Z_LOS >= lo) & (Z_LOS < hi))
        norm = np.trapezoid(ni, Z_LOS)
        bins.append(ni / norm if norm > 0 else ni)
    return bins


NZ_BINS = per_bin_nz_normalized()


def lensing_kernels():
    """W_i(z) on Z_LOS for every bin. Returns array (N_BINS, len(Z_LOS))."""
    W = np.zeros((N_BINS, Z_LOS.size))
    chi = CHI_LOS
    for i, ni in enumerate(NZ_BINS):
        g = np.zeros_like(chi)
        for j, zl in enumerate(Z_LOS):
            mask = Z_LOS >= zl
            if not np.any(mask):
                continue
            integrand = ni[mask] * (1.0 - chi[j] / np.maximum(chi[mask], 1e-8))
            integrand = np.where(chi[mask] > 0, integrand, 0.0)
            g[j] = np.trapezoid(integrand, Z_LOS[mask])
        W[i] = 1.5 * OMEGA_M * H0_OVER_C ** 2 * (1.0 + Z_LOS) * chi * g
    return W


W_KERNELS = lensing_kernels()

# sanity: lensing efficiency must vanish at/after the last source plane and be ≥0
assert np.all(W_KERNELS >= -1e-30), "lensing kernel went negative"
assert abs(W_KERNELS[:, -1].max()) < 1e-12, "kernel must vanish at far edge (no sources beyond)"


def cl_matrix(ell, model="lcdm"):
    """Full N_BINS×N_BINS convergence C_ℓ^{ij} at one ℓ (Limber over Z_LOS)."""
    chi = CHI_LOS
    valid = chi > 1.0
    k = np.where(valid, ell / np.maximum(chi, 1e-8), np.nan)        # Mpc^-1
    a = 1.0 / (1.0 + Z_LOS)
    if model == "lcdm":
        P = np.where(valid, P_lcdm(np.where(valid, k, 1e-3), a), 0.0)
    else:
        P = np.where(valid, P_qfuds(np.where(valid, k, 1e-3), a), 0.0)
    # dχ = (c/H0)/E dz  ->  integrate over z
    dchi_dz = DH / E_LOS
    pref = np.where(valid, P / np.maximum(chi, 1e-8) ** 2, 0.0) * dchi_dz
    C = np.zeros((N_BINS, N_BINS))
    for i in range(N_BINS):
        for j in range(i, N_BINS):
            integ = W_KERNELS[i] * W_KERNELS[j] * pref
            val = np.trapezoid(integ, Z_LOS)
            C[i, j] = C[j, i] = val
    return C


def shape_noise_diag():
    """N_ℓ^{ii} = σ_ε² / n_i (per steradian); equal counts → n_i = n_tot/N_BINS."""
    n_i = N_SR_TOTAL / N_BINS
    return SIGMA_EPS ** 2 / n_i


N_SHOT = shape_noise_diag()


# --------------------------------------------------------------------------- #
# 5. Tomographic Fisher with amplitude marginalization.
#    Data per ℓ: the upper-triangle vector of ΔC^{ij}=C^Q-C^L over i≤j.
#    Gaussian covariance of the pair-vector:
#       Cov[C^{ij},C^{mn}] = [ (Ĉ^{im}Ĉ^{jn}+Ĉ^{in}Ĉ^{jm}) ] / [(2ℓ+1)f_sky Δℓ]
#       with Ĉ = C^L + N (shape noise on the diagonal).
#    Amplitude templates (marginalized so a uniform/per-bin σ8 cannot fake it):
#       per-bin A_i: ∂C^{ij}/∂A_k|_{A=1} = (δ_ik+δ_jk) C^{L,ij}.
#    SNR²_marg = Σ d^T Cinv d  -  b^T F⁻¹ b ,  F=Σ Pᵀ Cinv P, b=Σ Pᵀ Cinv d.
# --------------------------------------------------------------------------- #
PAIRS = [(i, j) for i in range(N_BINS) for j in range(i, N_BINS)]
NPAIR = len(PAIRS)


def _vec(C):
    return np.array([C[i, j] for (i, j) in PAIRS])


def _pair_cov(Chat, ell, dell):
    """Gaussian covariance of the pair-vector at one ℓ."""
    cov = np.zeros((NPAIR, NPAIR))
    norm = (2.0 * ell + 1.0) * F_SKY * dell
    for p, (i, j) in enumerate(PAIRS):
        for qd, (m, n) in enumerate(PAIRS):
            cov[p, qd] = (Chat[i, m] * Chat[j, n] + Chat[i, n] * Chat[j, m]) / norm
    return cov


def _amp_templates(CL):
    """P[pair, bin] = ∂C^{ij}/∂A_bin at A=1 = (δ_i,bin+δ_j,bin) C^{L,ij}."""
    Pm = np.zeros((NPAIR, N_BINS))
    for p, (i, j) in enumerate(PAIRS):
        Pm[p, i] += CL[i, j]
        Pm[p, j] += CL[i, j]
    return Pm


def run_fisher():
    dell = np.gradient(ELL)
    # accumulate per-ℓ; keep cumulative pieces for SNR-vs-ℓmax curve
    cum_S0 = 0.0
    F_perbin = np.zeros((N_BINS, N_BINS))
    b_perbin = np.zeros(N_BINS)
    F_global = 0.0                     # single overall-amplitude Fisher (scalar)
    b_global = 0.0
    cl_ii_q = np.zeros((len(ELL), N_BINS))
    cl_ii_l = np.zeros((len(ELL), N_BINS))
    cum_snr2_perbin = np.zeros(len(ELL))   # P(k) step, per-bin amp marginalized
    cum_snr2_global = np.zeros(len(ELL))   # γ-running, single amp marginalized
    cum_snr2_raw = np.zeros(len(ELL))      # un-marginalized (for reference)

    for li, ell in enumerate(ELL):
        CL = cl_matrix(ell, "lcdm")
        CQ = cl_matrix(ell, "qfuds")
        cl_ii_l[li] = np.diag(CL)
        cl_ii_q[li] = np.diag(CQ)

        Chat = CL + np.eye(N_BINS) * N_SHOT
        cov = _pair_cov(Chat, ell, dell[li])
        cinv = np.linalg.inv(cov)

        d = _vec(CQ) - _vec(CL)
        Pm = _amp_templates(CL)                 # per-bin templates
        Pg = Pm.sum(axis=1, keepdims=True)       # overall-amp template = Σ per-bin

        cum_S0 += float(d @ cinv @ d)
        F_perbin += Pm.T @ cinv @ Pm
        b_perbin += Pm.T @ cinv @ d
        F_global += float((Pg.T @ cinv @ Pg).item())
        b_global += float((Pg.T @ cinv @ d).reshape(-1)[0])

        # cumulative marginalized SNR² using modes up to this ℓ
        snr2_perbin = cum_S0 - float(b_perbin @ np.linalg.solve(F_perbin, b_perbin))
        snr2_global = cum_S0 - (b_global ** 2 / F_global if F_global > 0 else 0.0)
        cum_snr2_perbin[li] = max(snr2_perbin, 0.0)
        cum_snr2_global[li] = max(snr2_global, 0.0)
        cum_snr2_raw[li] = cum_S0

    return {
        "snr_perbin": np.sqrt(cum_snr2_perbin),
        "snr_global": np.sqrt(cum_snr2_global),
        "snr_raw": np.sqrt(cum_snr2_raw),
        "cl_ii_q": cl_ii_q, "cl_ii_l": cl_ii_l,
    }


# --------------------------------------------------------------------------- #
# 6. Sanity: a UNIFORM amplitude shift (no step, no scale dependence) must give
#    ~0 marginalized shape SNR (the per-bin amplitude templates span it exactly).
# --------------------------------------------------------------------------- #
def sanity_uniform_shift(shift=0.90):
    dell = np.gradient(ELL)
    cum_S0 = 0.0
    F = np.zeros((N_BINS, N_BINS))
    b = np.zeros(N_BINS)
    for li, ell in enumerate(ELL):
        CL = cl_matrix(ell, "lcdm")
        CQ = shift * CL                          # pure uniform amplitude, NO shape
        Chat = CL + np.eye(N_BINS) * N_SHOT
        cinv = np.linalg.inv(_pair_cov(Chat, ell, dell[li]))
        d = _vec(CQ) - _vec(CL)
        Pm = _amp_templates(CL)
        cum_S0 += float(d @ cinv @ d)
        F += Pm.T @ cinv @ Pm
        b += Pm.T @ cinv @ d
    snr2 = cum_S0 - float(b @ np.linalg.solve(F, b))
    return np.sqrt(cum_S0), np.sqrt(max(snr2, 0.0))   # (raw, marginalized)


# --------------------------------------------------------------------------- #
# 7. γ_eff(k) running magnitude (CP16 diagnostic, reported across the WL band).
# --------------------------------------------------------------------------- #
def gamma_running():
    n_grid = np.linspace(np.log(A_I), 0.0, 600)
    ks = np.array([0.01, 0.05, 0.1, 0.2, 0.5, 1.0])
    g0 = {}
    for k in ks:
        ak, Dk, Dpk = cp16.growth_qfuds(n_grid, C2, k)
        gk = cp16.gamma_eff(Dpk / Dk, cp16.Om_qfuds(ak))
        g0[k] = float(np.interp(1.0, ak, gk))
    dgamma = max(g0.values()) - min(g0.values())
    return ks, g0, dgamma


# =========================================================================== #
# MAIN
# =========================================================================== #
def main():
    print("=" * 78)
    print("CP19: representative Euclid-like TOMOGRAPHIC weak-lensing forecast")
    print("  (exploratory; config representative & sourced; NOT a likelihood;")
    print("   050 ceiling + observer mode untouched; real check = CLASS, BLOCKED)")
    print("=" * 78)
    print(f"  Euclid-like config (SOURCED scale, Euclid Q1 press release):")
    print(f"    f_sky={F_SKY} (~15000 deg²), n_eff={N_EFF_ARCMIN2}/arcmin², "
          f"σ_ε={SIGMA_EPS}, N_bins={N_BINS}")
    print(f"    n(z)∝z²exp(-(z/z0)^{NZ_POW}), z0={Z0:.3f} -> median z={Z_MED:.3f}, "
          f"peak z={Z_PEAK:.3f}")
    print(f"    bin edges z = [{', '.join(f'{e:.3f}' for e in BIN_EDGES)}]")
    print(f"    shape-noise floor N_ℓ = σ_ε²/n_i = {N_SHOT:.3e} (per bin)")
    print(f"    growth: c_eff²={C2} (CP9/CP16 data-fit); common ΛCDM geometry")

    # ---- Forecast 1 + 2: the tomographic Fisher ----
    res = run_fisher()
    snr_step = res["snr_perbin"][-1]      # P(k) step, per-bin amp marginalized
    snr_grun = res["snr_global"][-1]      # γ-running, single overall amp marginalized
    snr_raw = res["snr_raw"][-1]

    print("\n--- Forecast 1: P(k) STEP shape detectability (multi-bin tomographic) ---")
    print(f"  un-marginalized total SNR              ≈ {snr_raw:6.1f}σ  (incl. amplitude)")
    print(f"  PER-BIN amplitude-marginalized SNR     ≈ {snr_step:6.1f}σ  "
          f"(robust: no uniform OR per-bin σ8 can fake it)")
    print(f"  CP14 single-bin shape SNR was ~18σ  ->  multi-bin / single-bin ≈ "
          f"{snr_step/18.07:.1f}×")

    print("\n--- Forecast 2: γ_eff(k) RUNNING detectability (running vs constant-γ) ---")
    ks, g0, dgamma = gamma_running()
    print(f"  γ_eff(z=0) across k: " +
          ", ".join(f"k={k}:{g0[k]:.2f}" for k in ks))
    print(f"  running over WL band Δγ_eff ≈ {dgamma:.2f}  "
          f"(scale-dependent — a constant-γ MG cannot reproduce it)")
    print(f"  single-amplitude(=constant-γ MG)-marginalized SNR ≈ {snr_grun:6.1f}σ")
    verdict_g = ("DISTINGUISHABLE from constant-γ MG (running detected at high SNR)"
                 if snr_grun > 5 else
                 "marginal vs constant-γ MG (running near shape-noise floor)")
    print(f"  -> {verdict_g}")

    # ---- sanity ----
    raw_u, marg_u = sanity_uniform_shift(0.90)
    print(f"\n--- SANITY: uniform amplitude shift (T=0.90, NO step) ---")
    print(f"  raw SNR={raw_u:.1f}σ  ->  per-bin-amp-marginalized SNR={marg_u:.2e}σ "
          f"(≈0 expected: a pure amplitude shift carries NO shape info)")
    assert marg_u < 1e-3, f"uniform shift leaked shape SNR={marg_u:.3e} (should be ~0)"
    # multi-bin must at least be in the ballpark of / exceed the single-bin proxy
    assert snr_step > 5.0, f"multi-bin step SNR={snr_step:.2f} implausibly small"

    # ---------------------------------------------------------------- FIGURE
    fig, (axA, axB) = plt.subplots(1, 2, figsize=(15, 6.2))

    # (a) n(z) tomographic bins + a few C_ℓ^{ii} QFUDS vs ΛCDM + shape-noise floor
    axA.set_title("(a) Euclid-like n(z) tomography  +  C_ℓ^{ii} vs shape noise")
    axNZ = axA
    nz_norm = N_NZ / np.trapezoid(N_NZ, Z_NZ)             # total n(z), unit area
    nz_los = nz_unnormed(Z_LOS, Z0)
    nz_los = nz_los / np.trapezoid(nz_unnormed(Z_NZ, Z0), Z_NZ)
    axNZ.plot(Z_NZ, nz_norm, color="k", lw=1.4, label="total n(z)  (median z=0.90)")
    cmap = plt.cm.viridis(np.linspace(0, 1, N_BINS))
    for i in range(N_BINS):
        lo, hi = BIN_EDGES[i], BIN_EDGES[i + 1]
        seg = (Z_LOS >= lo) & (Z_LOS < hi)
        axNZ.fill_between(Z_LOS, 0, nz_los, where=seg, color=cmap[i],
                          alpha=0.55, lw=0)
    axNZ.set_xlabel("redshift z")
    axNZ.set_ylabel("source n(z)  [10 equal-count tomographic bins]")
    axNZ.set_xlim(0, 3.0)
    axNZ.set_ylim(bottom=0)
    axNZ.legend(loc="upper right", fontsize=8)

    # inset: C_ℓ^{ii} for low/mid/high bins, QFUDS vs ΛCDM, + shape noise
    axin = axA.inset_axes([0.50, 0.45, 0.47, 0.50])
    for bi, col in zip([1, 5, 9], ["tab:blue", "tab:green", "tab:red"]):
        axin.loglog(ELL, res["cl_ii_l"][:, bi], color=col, lw=1.6,
                    label=f"ΛCDM bin{bi}")
        axin.loglog(ELL, res["cl_ii_q"][:, bi], color=col, lw=1.4, ls="--")
    axin.axhline(N_SHOT, color="gray", ls=":", lw=1.4, label="shape-noise N_ℓ")
    axin.set_xlabel("ℓ", fontsize=7); axin.set_ylabel("C_ℓ^{ii}", fontsize=7)
    axin.tick_params(labelsize=6)
    axin.legend(fontsize=5.2, loc="lower left")
    axin.set_title("solid ΛCDM / dashed QFUDS", fontsize=6.5)

    # (b) cumulative shape SNR vs ℓ_max (multi-bin) + single-bin CP14 + γ marker
    axB.set_title("(b) cumulative P(k)-step SNR vs ℓ_max  (multi-bin vs CP14)")
    axB.semilogx(ELL, res["snr_perbin"], "o-", color="tab:purple", lw=2.2,
                 ms=4, label=f"multi-bin tomographic, per-bin amp marg "
                            f"({snr_step:.0f}σ)")
    axB.semilogx(ELL, res["snr_global"], "s--", color="tab:orange", lw=1.8,
                 ms=3, label=f"single overall-amp marg (γ-running, {snr_grun:.0f}σ)")
    axB.axhline(18.07, color="tab:gray", ls="-.", lw=1.6,
                label="CP14 single-bin step ≈ 18σ")
    axB.scatter([ELL[-1]], [snr_grun], color="tab:orange", zorder=6, s=55,
                marker="*", label=f"γ_eff(k) running  Δγ≈{dgamma:.2f}")
    axB.set_xlabel("ℓ_max")
    axB.set_ylabel("cumulative shape SNR  (amplitude-marginalized)")
    axB.legend(fontsize=8, loc="upper left")
    axB.grid(alpha=0.3)

    fig.suptitle("CP19: Euclid-like tomographic forecast — P(k) step + γ_eff(k) "
                 "running  (exploratory; Euclid config representative, sourced)",
                 fontweight="bold")
    fig.tight_layout()
    fig.savefig("fig_cp19_euclid_forecast.png", dpi=130)
    fig.savefig("fig_cp19_euclid_forecast.svg")
    print("\nsaved fig_cp19_euclid_forecast.png + .svg")

    # ---------------------------------------------------------------- CSV
    with open("cp19_euclid_forecast_results.csv", "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["# CP19 Euclid-like tomographic WL forecast (exploratory)"])
        w.writerow(["# PARAMETRIZE-not-DERIVE; 050 ceiling + observer mode UNTOUCHED;"])
        w.writerow(["# survey config REPRESENTATIVE & SOURCED but NOT a likelihood;"])
        w.writerow(["# real verdict = CLASS/hi_class, Level 3, BLOCKED."])
        w.writerow(["# SOURCE (survey scale): "
                    "https://www.euclid-ec.org/public/press-releases/euclid-quick-data-release-1/"])
        w.writerow([f"# config: f_sky={F_SKY}, n_eff={N_EFF_ARCMIN2}/arcmin^2, "
                    f"sigma_eps={SIGMA_EPS}, N_bins={N_BINS}, "
                    f"nz~z^2 exp(-(z/z0)^{NZ_POW}) z0={Z0:.4f} "
                    f"median={Z_MED:.4f} peak={Z_PEAK:.4f}, c_eff2={C2}"])
        w.writerow([f"# shape_noise_Nl={N_SHOT:.6e}"])
        w.writerow([])
        w.writerow(["# tomographic bin edges (z, equal galaxy counts)"])
        w.writerow(["bin_edge_index", "z_edge"])
        for i, e in enumerate(BIN_EDGES):
            w.writerow([i, f"{e:.5f}"])
        w.writerow([])
        w.writerow(["# cumulative shape SNR vs ell_max"])
        w.writerow(["ell_max", "cumulative_SNR_step_multibin_perbinmarg",
                    "cumulative_SNR_gamma_running_globalmarg",
                    "cumulative_SNR_raw_unmarginalized"])
        for li in range(len(ELL)):
            w.writerow([f"{ELL[li]:.0f}", f"{res['snr_perbin'][li]:.4f}",
                        f"{res['snr_global'][li]:.4f}", f"{res['snr_raw'][li]:.4f}"])
        w.writerow([])
        w.writerow(["# gamma_eff(z=0) running across k (CP16 diagnostic)"])
        w.writerow(["k_Mpc^-1", "gamma_eff_z0"])
        ks, g0, dgamma = gamma_running()
        for k in ks:
            w.writerow([k, f"{g0[k]:.5f}"])
        w.writerow([])
        w.writerow(["# headline numbers"])
        w.writerow(["quantity", "value"])
        w.writerow(["SNR_step_multibin_perbin_marg", f"{snr_step:.3f}"])
        w.writerow(["SNR_step_single_bin_CP14", "18.071"])
        w.writerow(["multibin_over_singlebin_ratio", f"{snr_step/18.07:.3f}"])
        w.writerow(["SNR_gamma_running_globalmarg", f"{snr_grun:.3f}"])
        w.writerow(["gamma_running_delta_over_WLband", f"{dgamma:.4f}"])
        w.writerow(["SANITY_uniform_shift_raw_SNR", f"{raw_u:.3f}"])
        w.writerow(["SANITY_uniform_shift_marg_SNR", f"{marg_u:.3e}"])
    print("saved cp19_euclid_forecast_results.csv")

    # ---------------------------------------------------------------- VERDICT
    print("\n" + "=" * 78)
    print("VERDICT (representative Euclid-like forecast; NOT a likelihood; "
          "real check = CLASS, BLOCKED):")
    print(f"  P(k) step : multi-bin tomographic, per-bin-amp-marginalized SNR "
          f"≈ {snr_step:.0f}σ")
    print(f"              vs CP14 single-bin ~18σ  ({snr_step/18.07:.1f}× — "
          f"tomography adds z-leverage & the full C_ℓ mode budget).")
    print(f"  γ running : Δγ_eff≈{dgamma:.2f} across the WL band; running vs "
          f"constant-γ MG detectable at ≈{snr_grun:.0f}σ.")
    print(f"  sanity    : uniform amplitude shift -> {marg_u:.1e}σ after "
          f"marginalization (≈0, as in CP14).")
    print(f"  050 ceiling + observer mode UNTOUCHED. Real verdict needs "
          f"CLASS/hi_class (Level 3, BLOCKED).")
    print("=" * 78)


if __name__ == "__main__":
    main()
