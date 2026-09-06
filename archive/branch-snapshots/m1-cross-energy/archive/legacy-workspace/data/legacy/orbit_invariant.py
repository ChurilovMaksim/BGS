"""
Run 82d: IS THE SHAPE MODULATION A FUNCTION OF THE ORBIT INVARIANT Q(n)?
=======================================================================
R82/R82c established at the real designs (N, K) = (3571, 17), (9349, 19):

  * the even spectral moments of V_n = P_+(T(n) + T(-n))P_+ fluctuate across
    A^T-orbits with std(mu_4) = 0.23 (m+ = 105) and 0.21 (m+ = 246), while the
    matched GOE reference has std 0.027 and 0.011 -- the arithmetic family's
    MACROSCOPIC spectral shape does not self-average;
  * odd moments are GOE-like, so the modulation is a symmetric-density
    (shape) effect;
  * Tr(V_n^2) is n-independent to 1.2% and equals N/K^2 to four digits;
  * the exact mod-N resonance count C_4(n) has NO extra solutions at
    (3571, 17) over 256 orbits, so extra resonances are NOT the driver
    (they ARE at the toy design N = 199: corr(C_4, mu_4) = 0.64).

The spectrum of V_n depends only on the A^T-orbit of n.  Orbits are graded by
the exact invariant of the centraliser torus,

    Q(n) = n_1^2 - n_1 n_2 - n_2^2   (mod N),      Q(A^T n) = Q(n),

whose level sets are unions of (N -+ 1)/K orbits each.  THIS RUN asks whether
the shape modulation is a function of Q alone:

  H5  mu_4(n) = f(Q(n)) + (small): the within-level-set variance of mu_4 is
      a small fraction of the total.                                  [~35%]
  H6  the modulation depends on the quadratic character chi(Q(n))
      (split vs inert level sets).                                    [~30%]

Two internal validations run first, both mandatory before any reading:
  V1  orbit invariance: spec(V_n) = spec(V_{A^T n}) to 1e-10 -- the theory
      demands it exactly, and it tests the whole eigenbasis pipeline;
  V2  two-key value check: mu_4(n) recomputed through the EXACT N x N
      projector (no randomised eigenbasis, no SVD) for a few n.

Output: artifacts/r82/orbit_invariant.json
"""

import json
import os
import sys
import time
from collections import defaultdict

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from catmap_independent import CatMap  # noqa: E402
from compression_spacings import eigen_basis  # noqa: E402
from parity_desymmetrised import apply_parity  # noqa: E402

A = [[2, 1], [1, 1]]


def Qform(n1, n2, N):
    return (n1 * n1 - n1 * n2 - n2 * n2) % N


def mu_of(ev, rmax=8):
    e = ev - ev.mean()
    e = e / np.sqrt((e ** 2).mean())
    return np.array([(e ** r).mean() for r in range(3, rmax + 1)])


def canon(n, AT, N, K):
    """canonical representative of the A^T-orbit of n (lexicographic min)."""
    w = np.array(n, dtype=np.int64) % N
    best = (int(w[0]), int(w[1]))
    for _ in range(K - 1):
        w = AT @ w % N
        c = (int(w[0]), int(w[1]))
        best = min(best, c)
    return best


def exact_projector_mu4(cm, K, lam, u):
    """V2: mu_4 through the exact N x N projector -- no randomised basis.
    Pi = ((1/K) sum_j lam^-j U^j) . ((1 + R)/2), applied to the identity."""
    N = cm.N
    Id = np.eye(N, dtype=complex)
    acc = np.zeros((N, N), dtype=complex)
    cur = Id.copy()
    for j in range(K):
        acc += (lam ** (-j)) * cur
        cur = cm.apply_U(cur)
    acc /= K                                   # eigenprojector
    acc = (acc + apply_parity(acc)) / 2        # parity-even part
    W = cm.apply_T(u, Id)
    W = W + W.conj().T
    M = acc @ W @ acc
    M = (M + M.conj().T) / 2
    ev = np.linalg.eigvalsh(M)
    keep = np.abs(ev) > 1e-9
    return mu_of(ev[keep]), int(keep.sum())


def design(N, batch, rng, n_levels=28, per_level=4, verbose=True):
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
    AT = np.array(A, dtype=np.int64).T % N
    row = {"N": N, "K": int(K), "m": int(m), "m_plus": mp, "eig_resid": res}
    print(f"=== N={N} K={K} m={m} m+={mp} ({time.time()-t0:.0f} s)", flush=True)

    def spec(u):
        H = Bp.conj().T @ cm.apply_T((int(u[0]) % N, int(u[1]) % N), Bp)
        H = H + H.conj().T
        return np.linalg.eigvalsh(H)

    # ---- V1: orbit invariance -----------------------------------------
    dev = []
    for _ in range(6):
        n = rng.integers(1, N, size=2)
        e1 = np.sort(spec(n))
        e2 = np.sort(spec(AT @ n % N))
        dev.append(float(np.abs(e1 - e2).max()))
    row["V1_orbit_invariance_maxdev"] = max(dev)
    print(f"  V1 orbit invariance: max |spec(V_n) - spec(V_An)| = {max(dev):.2e}",
          flush=True)

    # ---- V2: exact-projector two-key check ----------------------------
    if N <= 3571:
        u = (int(rng.integers(1, N)), int(rng.integers(1, N)))
        t1 = time.time()
        mu_exact, dim = exact_projector_mu4(cm, K, lam, u)
        mu_fast = mu_of(spec(u))
        row["V2_n"] = list(u)
        row["V2_dim_exact"] = dim
        row["V2_mu4_exact"] = float(mu_exact[1])
        row["V2_mu4_basis"] = float(mu_fast[1])
        row["V2_absdiff"] = float(abs(mu_exact[1] - mu_fast[1]))
        print(f"  V2 exact projector (dim {dim} vs m+ {mp}): mu_4 = "
              f"{mu_exact[1]:.8f} vs basis route {mu_fast[1]:.8f}  "
              f"|diff| = {abs(mu_exact[1]-mu_fast[1]):.2e} "
              f"({time.time()-t1:.0f} s)", flush=True)

    # ---- H5/H6: level sets of Q ---------------------------------------
    buckets = defaultdict(list)
    seen = set()
    tries = 0
    while tries < 60000 and sum(1 for v in buckets.values()
                                if len(v) >= per_level) < n_levels:
        tries += 1
        n = (int(rng.integers(0, N)), int(rng.integers(0, N)))
        if n == (0, 0):
            continue
        c = canon(n, AT, N, K)
        if c in seen:
            continue
        q = Qform(n[0], n[1], N)
        if q == 0 or len(buckets[q]) >= per_level:
            continue
        seen.add(c)
        buckets[q].append(c)
    levels = [(q, v) for q, v in buckets.items() if len(v) >= per_level][:n_levels]
    print(f"  collected {len(levels)} level sets with {per_level} distinct "
          f"orbits each ({tries} draws)", flush=True)

    mu4 = np.zeros((len(levels), per_level))
    for i, (q, orbs) in enumerate(levels):
        for j, o in enumerate(orbs):
            mu4[i, j] = mu_of(spec(o))[1]
    grand = mu4.mean()
    within = float(np.mean(mu4.var(axis=1, ddof=1)))
    between = float(np.var(mu4.mean(axis=1), ddof=1) * per_level)
    total = float(np.var(mu4.ravel(), ddof=1))
    row["H5_within_level_var"] = within
    row["H5_between_level_var"] = between
    row["H5_total_var"] = total
    row["H5_within_over_total"] = within / total
    print(f"  H5 ANOVA on mu_4 over Q-level sets: total var {total:.5f}, "
          f"within-level {within:.5f} ({within/total:.2f} of total), "
          f"between-level {between:.5f}", flush=True)
    print("     -> mu_4 is " + ("a function of Q (within << total)"
                                if within / total < 0.3 else
                                "NOT determined by Q (within ~ total)"),
          flush=True)

    # H6: quadratic character of Q
    qs = np.array([q for q, _ in levels], dtype=object)
    leg = np.array([1 if pow(int(q), (N - 1) // 2, N) == 1 else -1 for q in qs])
    m_plus_side = mu4.mean(axis=1)[leg == 1]
    m_minus_side = mu4.mean(axis=1)[leg == -1]
    if len(m_plus_side) > 1 and len(m_minus_side) > 1:
        sep = abs(m_plus_side.mean() - m_minus_side.mean())
        pooled = np.sqrt(m_plus_side.var(ddof=1) / len(m_plus_side) +
                         m_minus_side.var(ddof=1) / len(m_minus_side))
        row["H6_chi_split_mean"] = float(m_plus_side.mean())
        row["H6_chi_inert_mean"] = float(m_minus_side.mean())
        row["H6_z"] = float(sep / pooled) if pooled > 0 else 0.0
        print(f"  H6 chi(Q) = +1: mu_4 = {m_plus_side.mean():.4f} "
              f"(n={len(m_plus_side)});  chi(Q) = -1: "
              f"{m_minus_side.mean():.4f} (n={len(m_minus_side)});  "
              f"z = {sep/pooled if pooled>0 else 0:.2f}", flush=True)
    row["mu4_grand_mean"] = float(grand)
    return row


def main():
    rng = np.random.default_rng(820003)
    out = {"script": "src/r82d_orbit_invariant.py",
           "generated": time.strftime("%Y-%m-%dT%H:%M:%S"), "designs": []}
    for N, batch in ((3571, 512), (9349, 1024)):
        try:
            out["designs"].append(design(N, batch, rng))
        except Exception as exc:                       # noqa: BLE001
            print(f"design N={N} FAILED: {exc!r}", flush=True)
            out["designs"].append({"N": N, "error": repr(exc)})
    dest = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                        "artifacts", "r82", "orbit_invariant.json")
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w") as fh:
        json.dump(out, fh, indent=1, default=str)
    print("artifact ->", dest, flush=True)


if __name__ == "__main__":
    main()
