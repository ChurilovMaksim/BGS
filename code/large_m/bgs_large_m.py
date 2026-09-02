"""
Run 82k: BGS AT LARGE m THROUGH THE CLOSED FORM.
===============================================
R82.12 (src/r82j_closed_form.py) verified, over EVERY level set at two designs
and to 2.4e-13, that the compressed observable in the Hecke basis is

    M_q[chi, psi] = e_N(-q/2) J(chi, psi; q)/(N-1)  +  (conjugate transpose),
    J(chi, psi; q) = sum_{x != 0, 1} conj(chi)(x) psi(x-1) e_N(q x),

with chi, psi running over the m_+ multiplicative characters of a fixed
chi(a)-class and fixed parity.  Building M_q therefore costs one (m x N)(N x m)
product -- no N x N linear algebra, no randomised eigenbasis, no SVD.  That
removes the memory wall which had capped this programme at m_+ = 246
(N = 9349) and makes the PER-SYSTEM BGS statement testable at m_+ in the
thousands: after Theorem I the correct statement is "for a fixed q, the
spectrum of M_q has GOE local statistics", and each q is one system.

Designs (ord(A) = K, m_+ = (N-1)/(2K), all split):
    N =  19489, K = 29, m_+ =  336        <- also validated out of sample
    N =  95419, K = 57, m_+ =  837           against the workspace pipeline
    N = 144481, K = 43, m_+ = 1680
    N = 336419, K = 59, m_+ = 2851        (--big)

Statistics (unfolding-free first, per the programme's standard):
  * <r~>, the consecutive-spacing ratio: GOE 0.5307, GUE 0.5996, Poisson
    0.3863 -- no unfolding, no density model;
  * the spacing distribution after polynomial unfolding, KS distance to the
    beta = 1 Wigner surmise;
  * the number variance Sigma^2(L) in the bulk at several L;
all against a matched GOE Monte-Carlo reference of the same dimension and the
same number of samples, so no asymptotic formula is needed.

Output: artifacts/r82/bgs_large_m.json
"""

import json
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from catmap_independent import unfolded_spacings  # noqa: E402
from r82j_closed_form import (multiplicative_order,  # noqa: E402
                              primitive_root, sqrt_mod)

T_TRACE = 3


def design_params(N, K):
    inv2 = pow(2, N - 2, N)
    a = None
    for r in sqrt_mod(T_TRACE * T_TRACE - 4, N):
        c = (T_TRACE + r) * inv2 % N
        if multiplicative_order(c, N) == K:
            a = c
            break
    assert a is not None, (N, K)
    return a


def build_M(N, K, a, q, k0=1, parity_odd=False, block=8192, verbose=False):
    """M_q for the closed-form model, built in blocks over x."""
    g = primitive_root(N)
    dlog = np.zeros(N, dtype=np.int64)
    x = 1
    for s in range(N - 1):
        dlog[x] = s
        x = x * g % N
    ks = np.array([k for k in range(N - 1)
                   if k % K == k0 % K and (k % 2 == 1) == parity_odd],
                  dtype=np.int64)
    m = len(ks)
    assert m == (N - 1) // (2 * K), (m, (N - 1) // (2 * K))
    J = np.zeros((m, m), dtype=complex)
    xs_all = np.arange(2, N, dtype=np.int64)          # x != 0, 1
    t0 = time.time()
    for s in range(0, len(xs_all), block):
        xs = xs_all[s:s + block]
        dl_x = dlog[xs]
        dl_xm1 = dlog[(xs - 1) % N]
        ph = np.exp(2j * np.pi * (q * xs % N) / N)
        W = np.exp(-2j * np.pi * np.outer(ks, dl_x) / (N - 1)) * ph
        Vv = np.exp(2j * np.pi * np.outer(ks, dl_xm1) / (N - 1))
        J += W @ Vv.T
        if verbose and (s // block) % 4 == 0:
            print(f"      block {s//block+1}/{-(-len(xs_all)//block)} "
                  f"({time.time()-t0:.0f} s)", flush=True)
    C = np.exp(-2j * np.pi * (pow(2, N - 2, N) * q % N) / N) * J / (N - 1)
    M = C + C.conj().T
    return (M + M.conj().T) / 2, m


def ratio_stat(ev, cut=0.10):
    """<r~> = mean min(s_i, s_{i+1})/max(...), bulk only, no unfolding."""
    ev = np.sort(ev)
    n = len(ev)
    lo, hi = int(cut * n), int((1 - cut) * n)
    s = np.diff(ev[lo:hi])
    s = s[s > 0]
    r = s[1:] / s[:-1]
    rt = np.minimum(r, 1.0 / r)
    return float(rt.mean()), len(rt)


def number_variance(ev, Ls=(2, 5, 10, 20), cut=0.15, nwin=400, rng=None):
    """Sigma^2(L) of the unfolded bulk spectrum."""
    ev = np.sort(ev)
    n = len(ev)
    lo, hi = int(cut * n), int((1 - cut) * n)
    x = ev[lo:hi]
    u = np.arange(len(x), dtype=float)          # already "unfolded" by index
    # unfold properly: fit the integrated density on the full spectrum
    cf = np.polyfit(ev, np.arange(1, n + 1) - 0.5, min(9, max(3, n // 40)))
    u = np.polyval(cf, x)
    out = {}
    for L in Ls:
        lo_u, hi_u = u.min() + L, u.max() - L
        if hi_u <= lo_u:
            out[L] = float("nan")
            continue
        cs = rng.uniform(lo_u, hi_u, nwin) if rng is not None else \
            np.linspace(lo_u, hi_u, nwin)
        cnt = np.array([np.sum((u >= c - L / 2) & (u < c + L / 2)) for c in cs],
                       dtype=float)
        out[L] = float(cnt.var(ddof=1))
    return out


def goe_reference(m, nrep, rng):
    evs = []
    for _ in range(nrep):
        X = rng.standard_normal((m, m))
        H = (X + X.T) / 2
        evs.append(np.linalg.eigvalsh(H))
    return evs


def wigner_ks(spacings, beta=1):
    """KS distance of the unfolded spacings to the beta-Wigner surmise."""
    s = np.sort(spacings)
    if beta == 1:
        cdf = 1 - np.exp(-np.pi * s ** 2 / 4)
    else:
        cdf = 1 - np.exp(-4 * s ** 2 / np.pi)
    emp = np.arange(1, len(s) + 1) / len(s)
    return float(np.max(np.abs(emp - cdf)))


def run_design(N, K, nq, rng, block=8192, verbose=False, goe_mult=8):
    t0 = time.time()
    a = design_params(N, K)
    print(f"=== N={N} K={K} m+={(N-1)//(2*K)}  a={a}", flush=True)
    evs, rs = [], []
    for i in range(nq):
        q = int(rng.integers(1, N))
        M, m = build_M(N, K, a, q, block=block, verbose=verbose)
        ev = np.linalg.eigvalsh(M)
        evs.append(ev)
        r, nr = ratio_stat(ev)
        rs.append(r)
        print(f"  q={q:7d}: <r~> = {r:.4f} (n={nr})  "
              f"[{time.time()-t0:.0f} s]", flush=True)
    m = len(evs[0])
    gref = goe_reference(m, nq * goe_mult, rng)
    grs = [ratio_stat(e)[0] for e in gref]

    # spacing distribution, pooled
    sp_a = np.concatenate([unfolded_spacings(e) for e in evs])
    sp_g = np.concatenate([unfolded_spacings(e) for e in gref])
    ks_a, ks_g = wigner_ks(sp_a), wigner_ks(sp_g)
    nv_a = [number_variance(e, rng=rng) for e in evs]
    nv_g = [number_variance(e, rng=rng) for e in gref[:nq * 2]]
    Ls = sorted(nv_a[0])
    nv_a_m = {str(L): float(np.mean([d[L] for d in nv_a])) for L in Ls}
    nv_g_m = {str(L): float(np.mean([d[L] for d in nv_g])) for L in Ls}
    nv_g_s = {str(L): float(np.std([d[L] for d in nv_g]) /
                            np.sqrt(len(nv_g))) for L in Ls}

    se_a = float(np.std(rs, ddof=1) / np.sqrt(nq))
    se_g = float(np.std(grs, ddof=1) / np.sqrt(len(grs)))
    row = {"N": N, "K": K, "m_plus": m, "nq": nq, "n_goe": len(grs),
           "r_arith_mean": float(np.mean(rs)), "r_arith_std": float(np.std(rs, ddof=1)),
           "r_arith_se": se_a,
           "r_goe_mean": float(np.mean(grs)), "r_goe_std": float(np.std(grs, ddof=1)),
           "r_goe_se": se_g,
           "r_GOE_asymptotic": 0.5307, "r_Poisson": 0.3863,
           "z_vs_goe_mc": float((np.mean(rs) - np.mean(grs)) /
                                np.hypot(se_a, se_g)),
           "z_vs_goe_asymptote": float((np.mean(rs) - 0.5307) / max(se_a, 1e-30)),
           "z_vs_poisson": float((np.mean(rs) - 0.3863) / max(se_a, 1e-30)),
           "ks_spacings_arith": ks_a, "ks_spacings_goe": ks_g,
           "ks_noise_floor_95": float(1.36 / np.sqrt(len(sp_a))),
           "n_spacings": int(len(sp_a)),
           "number_variance_arith": nv_a_m,
           "number_variance_goe": nv_g_m, "number_variance_goe_se": nv_g_s,
           "seconds": time.time() - t0}
    print(f"  POOLED ({nq} systems vs {len(grs)} GOE): <r~> arithmetic "
          f"{np.mean(rs):.5f} +- {se_a:.5f} (se) | GOE MC {np.mean(grs):.5f} "
          f"+- {se_g:.5f} | asymptote 0.5307, Poisson 0.3863", flush=True)
    print(f"     z vs GOE MC = {row['z_vs_goe_mc']:+.2f};  z vs GOE asymptote "
          f"= {row['z_vs_goe_asymptote']:+.2f};  z vs Poisson = "
          f"{row['z_vs_poisson']:+.1f}", flush=True)
    print(f"  spacing KS to Wigner(beta=1): arithmetic {ks_a:.4f} | GOE "
          f"{ks_g:.4f} | 95% noise floor {1.36/np.sqrt(len(sp_a)):.4f}  "
          f"({len(sp_a)} spacings)", flush=True)
    print(f"  number variance Sigma^2(L): arith "
          f"{ {k: round(v,3) for k,v in nv_a_m.items()} }", flush=True)
    print(f"                              GOE   "
          f"{ {k: round(v,3) for k,v in nv_g_m.items()} } "
          f"(se { {k: round(v,3) for k,v in nv_g_s.items()} })", flush=True)
    return row


def main():
    big = "--big" in sys.argv
    rng = np.random.default_rng(820012)
    out = {"script": "src/r82k_bgs_large_m.py",
           "generated": time.strftime("%Y-%m-%dT%H:%M:%S"), "designs": []}
    plan = [(19489, 29, 48), (95419, 57, 24), (144481, 43, 8)]
    if big:
        plan = [(336419, 59, 3)]
    for N, K, nq in plan:
        try:
            out["designs"].append(run_design(N, K, nq, rng, verbose=(N > 90000)))
        except Exception as exc:                       # noqa: BLE001
            print(f"design N={N} FAILED: {exc!r}", flush=True)
            out["designs"].append({"N": N, "error": repr(exc)})
    dest = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                        "artifacts", "r82",
                        "bgs_large_m_big.json" if big else "bgs_large_m.json")
    with open(dest, "w") as fh:
        json.dump(out, fh, indent=1, default=str)
    print("artifact ->", dest, flush=True)


if __name__ == "__main__":
    main()
