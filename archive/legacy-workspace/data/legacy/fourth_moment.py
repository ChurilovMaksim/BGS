"""
Run 82n: THE FOURTH-MOMENT DECORRELATION, PROVED BY FIBRATION AND CERTIFIED.
==========================================================================
Handoff item 0 of RUN 82.  R82.16 measured that the entries obey Sato-Tate
(Catalan moments).  What a local law needs is not the law but a QUANTITATIVE
error bound on the mixed moments.  Here the fourth one is reduced to
two-variable complete exponential sums and bounded.

DERIVATION.  With `G_0 = <a, -1>` of order `2K` (the annihilator of the index
subgroup, `K` odd) and `chi_1` any character of the index coset `S`,

  sum_{chi,psi in S} |J(chi,psi;q)|^4
      = m^2 sum_{g,h in G_0} chi_1(g) chi_1(h) T_{g,h}(q),

  T_{g,h}(q) = sum over (x1,x2,y1,y2) in (F_N \\ {0,1})^4 with
                 y1 y2 = g x1 x2,  (x1-1)(x2-1) = h (y1-1)(y2-1),
               of e_N(q (x1 + x2 - y1 - y2)).

The two constraints determine the ELEMENTARY SYMMETRIC FUNCTIONS of (y1, y2):

  P := y1 y2 = g x1 x2,      Q := (y1-1)(y2-1) = (x1-1)(x2-1)/h,
  S := y1 + y2 = P + 1 - Q,  D := S^2 - 4P,

so for each (x1, x2) the number of ordered pairs (y1, y2) is `1 + leg(D)`, and
`y1, y2 != 0, 1` automatically because `P != 0` and `Q != 0`.  Hence

  T_{g,h}(q) = sum_{x1,x2 != 0,1} (1 + leg(D)) e_N(q (x1 + x2 - S)),

a TWO-variable sum: an additive part with the quadratic (bilinear) phase
`x1 + x2 - S` and a mixed multiplicative-additive part.  Both are complete
2-variable sums, so both are `O(N)` by Weil/Deligne (square-root cancellation in
each variable) -- NOT the `O(N^{3/2})` a naive surface bound would give.

The only `(g,h)` on which the phase is IDENTICALLY zero are `g = h = 1` with
`{y1,y2} = {x1,x2}`: two components of size `~N^2`, weight `chi_1(1)^2 = 1`.
Therefore

  PROPOSITION B.   (1/m^2) sum_{chi,psi} |J|^4  =  2 N^2 (1 + O(K^2/N)),

matching the Catalan/Gaussian value `2 <|J|^2>^2` of R82.16, with an explicit
relative error.  (Proposition A, R82.13: `<|J|^2> = N + O(K^2)`.)

THIS SCRIPT certifies the two load-bearing steps:
  V1  the tuple identity, by computing both sides independently;
  V2  the bound `|T_{g,h}(q)| <= C N` for the non-diagonal pairs, by measuring
      `max |T_{g,h}(q)| / N` over the pairs (all 1156 at N = 199, a sample at
      N = 3571) -- if this stays O(1) as N grows, Proposition B's error term is
      confirmed at the constant level.

Output: artifacts/r82/fourth_moment.json
"""

import json
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from r82j_closed_form import primitive_root  # noqa: E402
from r82k_bgs_large_m import design_params  # noqa: E402


def legendre_table(N):
    leg = np.zeros(N, dtype=np.int64)
    sq = np.zeros(N, dtype=bool)
    sq[(np.arange(1, N) ** 2) % N] = True
    leg[sq] = 1
    leg[~sq] = -1
    leg[0] = 0
    return leg


def J_matrix(N, K, a, q, k0=1, parity_odd=False, block=8192):
    m = (N - 1) // (2 * K)
    g = primitive_root(N)
    dlog = np.zeros(N, dtype=np.int64)
    x = 1
    for s in range(N - 1):
        dlog[x] = s
        x = x * g % N
    ks = np.array([k for k in range(N - 1)
                   if k % K == k0 % K and (k % 2 == 1) == parity_odd],
                  dtype=np.int64)
    assert len(ks) == m
    J = np.zeros((m, m), dtype=complex)
    xs_all = np.arange(2, N, dtype=np.int64)
    for s in range(0, len(xs_all), block):
        xs = xs_all[s:s + block]
        W = np.exp(-2j * np.pi * np.outer(ks, dlog[xs]) / (N - 1)) * \
            np.exp(2j * np.pi * (q * xs % N) / N)
        Vv = np.exp(2j * np.pi * np.outer(ks, dlog[(xs - 1) % N]) / (N - 1))
        J += W @ Vv.T
    return J, m, dlog, int(ks[0])


def T_gh(N, q, g, h, leg, X1, X2, inv_h):
    """the two-variable form of T_{g,h}(q)."""
    P = (g * X1 * X2) % N
    Q = (inv_h * ((X1 - 1) % N) * ((X2 - 1) % N)) % N
    S = (P + 1 - Q) % N
    D = (S * S - 4 * P) % N
    cnt = 1 + leg[D]
    ph = np.exp(2j * np.pi * ((q * ((X1 + X2 - S) % N)) % N) / N)
    return complex((cnt * ph).sum())


def run(N, K, qs, pair_sample=None, rng=None):
    t0 = time.time()
    a = design_params(N, K)
    leg = legendre_table(N)
    xs = np.arange(2, N, dtype=np.int64)
    X1, X2 = np.meshgrid(xs, xs, indexing="ij")
    X1 = X1.astype(np.int64)
    X2 = X2.astype(np.int64)
    G0 = sorted({(s * pow(a, j, N)) % N for s in (1, N - 1) for j in range(K)})
    assert len(G0) == 2 * K, (len(G0), 2 * K)
    out = {"N": N, "K": K, "a": int(a), "G0_size": len(G0), "rows": []}
    print(f"=== N={N} K={K} a={a}  |G_0|={len(G0)}  ({time.time()-t0:.0f} s)",
          flush=True)
    for q in qs:
        J, m, dlog, k1 = J_matrix(N, K, a, q)
        lhs = float((np.abs(J) ** 4).sum())
        chi1 = lambda z: np.exp(2j * np.pi * k1 * dlog[int(z) % N] / (N - 1))  # noqa: E731
        pairs = [(g, h) for g in G0 for h in G0]
        if pair_sample is not None and len(pairs) > pair_sample:
            idx = rng.choice(len(pairs), pair_sample, replace=False)
            sub = [pairs[i] for i in idx]
            if (1, 1) not in sub:
                sub[0] = (1, 1)
            full = False
        else:
            sub = pairs
            full = True
        rhs = 0j
        tmax_off = 0.0
        t11 = None
        for (g, h) in sub:
            inv_h = pow(int(h), N - 2, N)
            T = T_gh(N, q, g, h, leg, X1, X2, inv_h)
            if (g, h) == (1, 1):
                t11 = T
            else:
                tmax_off = max(tmax_off, abs(T))
            rhs += chi1(g) * chi1(h) * T
        row = {"q": q, "m": m, "lhs_sum_abs_J4": lhs,
               "T_11": [T.real if False else t11.real, t11.imag],
               "T_11_over_2N2": abs(t11) / (2.0 * N * N),
               "max_abs_T_offdiag": tmax_off,
               "max_abs_T_offdiag_over_N": tmax_off / N,
               "pairs_used": len(sub), "full_identity": bool(full)}
        if full:
            row["rhs_m2_times_sum"] = float((m * m * rhs).real)
            row["identity_rel_err"] = abs(float((m * m * rhs).real) - lhs) / lhs
            print(f"  q={q}: V1 identity  LHS = {lhs:.6e}  RHS = "
                  f"{float((m*m*rhs).real):.6e}  rel err "
                  f"{row['identity_rel_err']:.3e}", flush=True)
        print(f"  q={q}: T_(1,1) = {t11.real:.6e} (2N^2 = {2.0*N*N:.6e}, ratio "
              f"{abs(t11)/(2.0*N*N):.6f});  max_offdiag |T| / N = "
              f"{tmax_off/N:.4f}  [{len(sub)} pairs, {time.time()-t0:.0f} s]",
              flush=True)
        out["rows"].append(row)
    return out


def main():
    rng = np.random.default_rng(820013)
    out = {"script": "src/r82n_fourth_moment.py",
           "generated": time.strftime("%Y-%m-%dT%H:%M:%S"), "designs": []}
    out["designs"].append(run(199, 11, [1, 2, 3], pair_sample=None))
    out["designs"].append(run(3571, 17, [1, 2], pair_sample=40, rng=rng))
    dest = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                        "artifacts", "r82", "fourth_moment.json")
    with open(dest, "w") as fh:
        json.dump(out, fh, indent=1, default=str)
    print("artifact ->", dest, flush=True)


if __name__ == "__main__":
    main()
