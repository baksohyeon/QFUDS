"""
QFUDS rough tanh model — shared contract for the parallel exploration.

STATUS: exploratory sandbox. This is a PHENOMENOLOGICAL parameterization, NOT a
derived theory. w(a) is hand-fitted with a tanh; nothing here is derived from
foam-sector microphysics. Do not read any of this as validating QFUDS or as a
roadmap status change. It exists only to answer "how far does the rough idea go,
shown as a curve instead of a sentence."

Unified-dark-sector reading:
    The QFUDS fluid replaces BOTH cold dark matter AND dark energy with a single
    component whose equation of state slides from w=0 (clusters like matter,
    early) to w=-1 (vacuum-like, late) across a phase transition near z=2
    (Cosmic Noon). Baryons and radiation are kept as ordinary separate species.

All three agent scripts import from this file so the physics stays identical.
"""

from __future__ import annotations

import numpy as np
from scipy.integrate import quad

# ---------------------------------------------------------------------------
# Cosmological constants (dimensionless density parameters, today, a=1)
# ---------------------------------------------------------------------------
OMEGA_B0 = 0.049      # baryons (ordinary matter, stays separate from QFUDS)
OMEGA_R0 = 9.0e-5     # radiation (photons + neutrinos, rough)
OMEGA_Q0 = 1.0 - OMEGA_B0 - OMEGA_R0   # QFUDS fluid carries DM + DE (flat closure)

# ΛCDM reference (Planck-ish, flat)
OMEGA_M0_LCDM = 0.315          # baryons + CDM
OMEGA_R0_LCDM = OMEGA_R0
OMEGA_L0_LCDM = 1.0 - OMEGA_M0_LCDM - OMEGA_R0_LCDM

# Hubble constants for distance/μ conversions (km/s/Mpc)
H0_CMB = 67.4         # early-universe / CMB-calibrated value
H0_LOCAL = 73.0       # local distance-ladder value
C_KM_S = 299792.458   # speed of light, km/s

# ---------------------------------------------------------------------------
# QFUDS equation-of-state parameterization (the whole "model" is these 4 knobs)
# ---------------------------------------------------------------------------
W_I = 0.0             # pre-transition: cold-dark-matter-like
W_F = -1.0            # post-transition: residual vacuum pressure
A_TR = 0.33           # transition scale factor  (z = 1/a - 1 ≈ 2.0)
DELTA_A = 0.05        # transition thickness (smaller = sharper = more 1st-order)


def z_to_a(z):
    return 1.0 / (1.0 + np.asarray(z, dtype=float))


def a_to_z(a):
    return 1.0 / np.asarray(a, dtype=float) - 1.0


def w_Q(a, a_tr=A_TR, delta_a=DELTA_A, w_i=W_I, w_f=W_F):
    """QFUDS equation of state w(a): tanh crossover from w_i to w_f at a_tr."""
    a = np.asarray(a, dtype=float)
    return 0.5 * (w_f - w_i) * np.tanh((a - a_tr) / delta_a) + 0.5 * (w_i + w_f)


def _rho_Q_exponent(a, **kw):
    """Compute -3 ∫_1^a (1+w(a'))/a' da' for a single a (scalar)."""
    integrand = lambda ap: (1.0 + w_Q(ap, **kw)) / ap
    val, _ = quad(integrand, 1.0, float(a), limit=200)
    return -3.0 * val


def rho_Q_over_crit(a, **kw):
    """ρ_Q(a) / ρ_crit,0  =  Ω_Q0 * exp(-3 ∫_1^a (1+w)/a' da'). Vectorized."""
    a_arr = np.atleast_1d(np.asarray(a, dtype=float))
    out = np.array([OMEGA_Q0 * np.exp(_rho_Q_exponent(ai, **kw)) for ai in a_arr])
    return out if out.size > 1 else out[0]


def E_QFUDS(a, **kw):
    """Dimensionless Hubble rate E(a) = H(a)/H0 for the QFUDS cosmology."""
    a = np.asarray(a, dtype=float)
    rho_q = rho_Q_over_crit(a, **kw)
    return np.sqrt(OMEGA_B0 * a ** -3 + OMEGA_R0 * a ** -4 + rho_q)


def E_LCDM(a):
    """Dimensionless Hubble rate E(a) = H(a)/H0 for the flat ΛCDM reference."""
    a = np.asarray(a, dtype=float)
    return np.sqrt(OMEGA_M0_LCDM * a ** -3 + OMEGA_R0_LCDM * a ** -4 + OMEGA_L0_LCDM)


# ---------------------------------------------------------------------------
# V2 "DE-only transition" variant.
#
# The naive unified V1 (above) breaks the early universe: putting the full
# Ω≈0.95 into a w:0→-1 fluid suppresses the early matter amplitude by ~a_tr^3,
# leaving far too little matter at high z (E_QFUDS ≪ E_LCDM at z≳3).
#
# V2 keeps ordinary matter (CDM+baryons, Ω_m0=0.315) as a normal a^-3 species
# and lets ONLY the dark-energy component carry the tanh transition w:0→-1.
# Because the transition suppresses its early amplitude, the early universe stays
# close to ΛCDM while the z≈2 feature survives late-time. This is the salvageable
# version that can actually be compared against data (H0 / S8 / DESI w0wa).
# ---------------------------------------------------------------------------
OMEGA_M0_V2 = OMEGA_M0_LCDM            # ordinary matter stays separate & normal
OMEGA_X0_V2 = 1.0 - OMEGA_M0_V2 - OMEGA_R0   # transitioning dark component today


def rho_X_over_crit(a, **kw):
    """ρ_X(a)/ρ_crit,0 for the V2 transitioning dark-energy component."""
    a_arr = np.atleast_1d(np.asarray(a, dtype=float))
    out = np.array([OMEGA_X0_V2 * np.exp(_rho_Q_exponent(ai, **kw)) for ai in a_arr])
    return out if out.size > 1 else out[0]


def E_QFUDS_V2(a, **kw):
    """Dimensionless Hubble rate for the V2 DE-only transition cosmology."""
    a = np.asarray(a, dtype=float)
    rho_x = rho_X_over_crit(a, **kw)
    return np.sqrt(OMEGA_M0_V2 * a ** -3 + OMEGA_R0 * a ** -4 + rho_x)


# Convenience: density fractions Ω_i(a) for the QFUDS model (sum to 1 by E^2 norm)
def omega_fractions_QFUDS(a, **kw):
    a = np.asarray(a, dtype=float)
    rho_b = OMEGA_B0 * a ** -3
    rho_r = OMEGA_R0 * a ** -4
    rho_q = rho_Q_over_crit(a, **kw)
    tot = rho_b + rho_r + rho_q
    return {"baryon": rho_b / tot, "radiation": rho_r / tot, "qfuds": rho_q / tot}


if __name__ == "__main__":
    # smoke test
    for z in (5, 2, 1, 0.5, 0):
        a = z_to_a(z)
        print(f"z={z:>4}  a={a:.3f}  w_Q={w_Q(a):+.3f}  "
              f"rhoQ/crit={float(rho_Q_over_crit(a)):.4f}  "
              f"E_QFUDS={float(E_QFUDS(a)):.4f}  E_LCDM={float(E_LCDM(a)):.4f}")
