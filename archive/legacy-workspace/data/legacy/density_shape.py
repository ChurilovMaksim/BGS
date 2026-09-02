"""
Run 82c: THE MACROSCOPIC DENSITY OF V_n IS NOT THE SEMICIRCLE, AND ITS SHAPE
DEPENDS ON n -- the mechanism of the R81.4 "coherent fluctuation mode".
===========================================================================
R82 (src/r82_shape_modes.py) measured, for V_n = P_+(T(n)+T(-n))P_+ over
A^T-orbit representatives, a variance excess over the matched GOE reference
that is confined to the EVEN Chebyshev modes and grows with m:

    ratio Var_arith/Var_GOE   k = 3   4     5    6     7    8
      m+ = 105                1.03  80.7  1.59  71.4  2.81  78.1
      m+ = 246                0.53  375   2.89  306   5.21  302

and identical ratios for the even spectral moments mu_4, mu_6, mu_8.  Only a
SYMMETRIC macroscopic density can behave this way: even moments carry the
shape, odd moments carry nothing.  A first-principles estimate of the moments
of V_n via the Birkhoff/Weyl expansion,

    Tr(V_n^r) = K^{-r} sum_{eps, J} (phase) Tr(T(v) U^J),
    Tr(T(v)U^J) = N.delta_{v = 0} (J = 0 mod K), modulus 1 otherwise,
    v = sum_i eps_i A^{J_{i-1}} n,

gives the leading term N.C_r(n)/K^r with C_r(n) the count of (eps, J) whose
translation annihilates n; for generic n only the PAIRINGS survive, and at
r = 4 the pairing count is C_4 = 6(2K - 1), which predicts

    mu_4 = Tr(V^4).m / Tr(V^2)^2  ->  a value near 3/2, NOT the semicircle 2.

3/2 is exactly the fourth moment of the ARCSINE law of unit variance -- the
spectral law of T(n) + T(-n) itself.  So the prediction under test is:

  H1  the macroscopic density of V_n is arcsine-like, not semicircular; the
      R81.4 statement "density = semicircle, KS distance = GOE's own" is a
      defect of an insufficiently sensitive test.                    [~70%]
  H2  the ensemble "fluctuation excess" is the n-dependence of this
      MACROSCOPIC shape (a global, not a local, effect); per-sample local
      statistics stay GOE (R81.5 D1 unaffected).                     [~75%]
  H3  the excess variance is NOT carried by a few outlier n: the trimmed
      variance (10% trim) reproduces at least half of it.            [~60%]
  H4  mu_4(n) correlates with the exact resonance count C_4(n) computed by
      enumerating (eps, J) and testing M n = 0 mod N.                [~40%]

Every number below comes from an executed run; the GOE reference is a matched
Monte-Carlo with 4x the sample count.

Output: artifacts/r82/density_shape.json
"""

import json
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from catmap_independent import CatMap  # noqa: E402
from compression_spacings import eigen_basis, orbit_reps  # noqa: E402
from parity_desymmetrised import apply_parity  # noqa: E402
from r81_local_law_pilot import goe_samples  # noqa: E402

A = [[2, 1], [1, 1]]


# --------------------------------------------------------------- reference laws
def semicircle_cdf(x):
    """CDF of the unit-second-moment semicircle on [-sqrt2, sqrt2]."""
    a = np.sqrt(2.0)
    x = np.clip(x, -a, a)
    return 0.5 + (x * np.sqrt(a * a - x * x) + a * a * np.arcsin(x / a)) / (np.pi * a * a)


def arcsine_cdf(x):
    """CDF of the unit-second-moment arcsine law on [-sqrt2, sqrt2]."""
    a = np.sqrt(2.0)
    x = np.clip(x, -a, a)
    return 0.5 + np.arcsin(x / a) / np.pi


def ks_to(ev_s, cdf):
    n = len(ev_s)
    xs = np.sort(ev_s)
    emp = (np.arange(1, n + 1)) / n
    theo = cdf(xs)
    return float(np.max(np.abs(emp - theo)))


def norm_moments(ev, rmax=10):
    """centred, unit-second-moment spectrum and its moments 3..rmax."""
    e = ev - ev.mean()
    s2 = (e ** 2).mean()
    e = e / np.sqrt(s2)
    return e, float(s2), np.array([(e ** r).mean() for r in range(3, rmax + 1)])


def trimmed_var(x, frac=0.10):
    """variance after removing the `frac` most deviant samples (two-sided)."""
    d = np.abs(x - np.median(x))
    keep = d <= np.quantile(d, 1 - frac)
    return float(np.var(x[keep], ddof=1)), int(keep.sum())


# ------------------------------------------------- exact resonance count C_4(n)
def power_coeffs(t, K):
    """A^j = u_j I + v_j A for j = 0..K-1, using A^2 = tA - I:
    A^{j+1} = u_j A + v_j A^2 = -v_j I + (u_j + t v_j) A."""
    u = [1]
    v = [0]
    for j in range(1, K):
        u.append(-v[j - 1])
        v.append(u[j - 1] + t * v[j - 1])
    return u, v


def resonance_c4(N, K, t, reps):
    """C_4(n) = #{(eps, J_1, J_2, J_3) : sum_i eps_i A^{J_{i-1}} n = 0 mod N},
    with J_0 = 0 and the constraint J = 0 mod K absorbed (the exponents
    J_1..J_3 are free).  Returns (baseline_generic, per-n counts)."""
    u, v = power_coeffs(t, K)
    u = np.array([int(x) % N for x in u])
    v = np.array([int(x) % N for x in v])
    # all (eps, J1, J2, J3): matrix M = alpha I + beta A
    signs = np.array([[s0, s1, s2, s3]
                      for s0 in (1, -1) for s1 in (1, -1)
                      for s2 in (1, -1) for s3 in (1, -1)], dtype=np.int64)
    J = np.array(np.meshgrid(np.arange(K), np.arange(K), np.arange(K),
                             indexing="ij")).reshape(3, -1).T
    e0 = np.zeros((len(J), 1), dtype=np.int64)
    Jfull = np.hstack([e0, J])                       # J_0 = 0
    U = u[Jfull]                                     # (nJ, 4)
    V = v[Jfull]
    alpha = (signs @ U.T) % N                        # (16, nJ)
    beta = (signs @ V.T) % N
    alpha = alpha.ravel()
    beta = beta.ravel()
    nz = ~((alpha == 0) & (beta == 0))
    base = int((~nz).sum())                          # M = 0: the generic count
    al, be = alpha[nz], beta[nz]
    Am = np.array(A, dtype=np.int64)
    counts = []
    for n in reps:
        n = np.array([n[0], n[1]], dtype=np.int64)
        An = (Am.T @ n) % N                          # A^T acts on n
        # (alpha I + beta A^T) n = alpha*n + beta*An
        r0 = (al * n[0] + be * An[0]) % N
        r1 = (al * n[1] + be * An[1]) % N
        counts.append(base + int(((r0 == 0) & (r1 == 0)).sum()))
    return base, np.array(counts)


def design(N, batch, nrep, rng, do_c4=True):
    t0 = time.time()
    cm = CatMap(A, N)
    ordA, K = cm.orders()
    assert ordA == K
    B, lam, m, res, chi = eigen_basis(cm, K, 0, batch, rng)
    assert res < 1e-9 and m in ((N - 1) // K, (N + 1) // K), (res, m)
    RB = B.conj().T @ apply_parity(B)
    w, Vv = np.linalg.eigh(RB)
    mp = int((w > 0).sum())
    Bp = B @ Vv[:, w > 0]
    reps = orbit_reps(cm, K, nrep, rng)
    print(f"=== N={N} K={K} m={m} m+={mp} nrep={nrep} resid={res:.1e} "
          f"({time.time()-t0:.0f} s)", flush=True)

    mu, s2s, ks_sc, ks_as, evs = [], [], [], [], []
    for uu in reps:
        H = Bp.conj().T @ cm.apply_T(uu, Bp)
        H = H + H.conj().T
        ev = np.linalg.eigvalsh(H)
        e, s2, mm = norm_moments(ev)
        mu.append(mm)
        s2s.append(s2)
        ks_sc.append(ks_to(e, semicircle_cdf))
        ks_as.append(ks_to(e, arcsine_cdf))
        evs.append(e)
    mu = np.array(mu)                     # columns: mu_3 .. mu_10
    evs = np.array(evs)

    gref = goe_samples(mp, 4 * nrep, rng)
    gmu, gks_sc, gks_as = [], [], []
    for e in gref:
        _, _, mm = norm_moments(e)
        gmu.append(mm)
        gks_sc.append(ks_to(e, semicircle_cdf))
        gks_as.append(ks_to(e, arcsine_cdf))
    gmu = np.array(gmu)

    row = {"N": N, "K": int(K), "m": int(m), "m_plus": mp, "nrep": nrep,
           "raw_second_moment_mean": float(np.mean(s2s)),
           "raw_second_moment_rel_spread": float(np.std(s2s) / np.mean(s2s)),
           "prediction_2N_over_K2_over_m": float(2 * N / K ** 2 / mp)}
    print(f"  raw Tr(V^2)/m = {np.mean(s2s):.5f} "
          f"(rel spread {np.std(s2s)/np.mean(s2s):.4f});  2N/(K^2 m+) = "
          f"{2*N/K**2/mp:.5f}", flush=True)

    # ---- H1: which macroscopic law? ------------------------------------
    print(f"  mu_4: arithmetic {mu[:,1].mean():.4f} +- {mu[:,1].std():.4f} | "
          f"GOE {gmu[:,1].mean():.4f} +- {gmu[:,1].std():.4f} | "
          f"semicircle 2, arcsine 1.5", flush=True)
    print(f"  mu_6: arithmetic {mu[:,3].mean():.4f} | GOE {gmu[:,3].mean():.4f}"
          f" | semicircle 5, arcsine 2.5", flush=True)
    print(f"  KS to semicircle: arith {np.mean(ks_sc):.4f} | GOE "
          f"{np.mean(gks_sc):.4f}", flush=True)
    print(f"  KS to arcsine   : arith {np.mean(ks_as):.4f} | GOE "
          f"{np.mean(gks_as):.4f}", flush=True)
    row["mu_mean_arith"] = mu.mean(axis=0).tolist()
    row["mu_std_arith"] = mu.std(axis=0, ddof=1).tolist()
    row["mu_mean_goe"] = gmu.mean(axis=0).tolist()
    row["mu_std_goe"] = gmu.std(axis=0, ddof=1).tolist()
    row["ks_semicircle_arith"] = float(np.mean(ks_sc))
    row["ks_semicircle_goe"] = float(np.mean(gks_sc))
    row["ks_arcsine_arith"] = float(np.mean(ks_as))
    row["ks_arcsine_goe"] = float(np.mean(gks_as))

    # ---- H3: outliers or broad? ----------------------------------------
    v4 = float(np.var(mu[:, 1], ddof=1))
    tv4, nkeep = trimmed_var(mu[:, 1])
    kurt = float(((mu[:, 1] - mu[:, 1].mean()) ** 4).mean() / v4 ** 2)
    row["mu4_var"] = v4
    row["mu4_trimmed_var"] = tv4
    row["mu4_trim_fraction_retained"] = tv4 / v4
    row["mu4_kurtosis"] = kurt
    print(f"  mu_4 variance {v4:.5f}; 10%-trimmed {tv4:.5f} "
          f"({tv4/v4:.2f} of it, n={nkeep}); kurtosis {kurt:.2f} (3 = normal)",
          flush=True)
    order = np.argsort(-np.abs(mu[:, 1] - np.median(mu[:, 1])))[:5]
    row["mu4_extremes"] = [{"n": [int(reps[i][0]), int(reps[i][1])],
                            "mu4": float(mu[i, 1])} for i in order]
    print("  most deviant mu_4: "
          + ", ".join(f"{mu[i,1]:.3f}@n={tuple(int(x) for x in reps[i])}"
                      for i in order), flush=True)

    # ---- H4: the exact resonance count ---------------------------------
    if do_c4:
        t1 = time.time()
        base, c4 = resonance_c4(N, K, 3, reps)
        pred = 6 * (2 * K - 1)
        cc = float(np.corrcoef(c4, mu[:, 1])[0, 1]) if c4.std() > 0 else 0.0
        row["C4_generic"] = base
        row["C4_pairing_prediction"] = pred
        row["C4_extra_mean"] = float((c4 - base).mean())
        row["C4_extra_max"] = int((c4 - base).max())
        row["C4_corr_mu4"] = cc
        print(f"  C_4 generic (M = 0) = {base}  [pairing prediction 6(2K-1)"
              f" = {pred}];  extra resonances: mean {(c4-base).mean():.3f}, "
              f"max {int((c4-base).max())};  corr(C_4, mu_4) = {cc:.3f} "
              f"({time.time()-t1:.0f} s)", flush=True)
        # analytic mu_4 from the leading term
        mu4_pred = base * mp / (4.0 * N)
        row["mu4_leading_prediction"] = mu4_pred
        print(f"  leading-term prediction mu_4 = C_4.m+/(4N) = {mu4_pred:.4f} "
              f"vs measured {mu[:,1].mean():.4f}", flush=True)
    return row


def main():
    rng = np.random.default_rng(820002)
    out = {"script": "src/r82c_density_shape.py",
           "generated": time.strftime("%Y-%m-%dT%H:%M:%S"), "designs": []}
    for N, batch, nrep, doc4 in ((199, 64, 256, True),
                                 (3571, 512, 256, True),
                                 (9349, 1024, 128, True)):
        try:
            out["designs"].append(design(N, batch, nrep, rng, doc4))
        except Exception as exc:                      # noqa: BLE001
            print(f"design N={N} FAILED: {exc!r}", flush=True)
            out["designs"].append({"N": N, "error": repr(exc)})
    dest = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                        "artifacts", "r82", "density_shape.json")
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w") as fh:
        json.dump(out, fh, indent=1, default=str)
    print("artifact ->", dest, flush=True)


if __name__ == "__main__":
    main()
