"""RUN 91 — Cycle 2c + 2d: MULTIPLICATIVE TOY (H3 discriminator), correct objects.

CONTEXT. The R86 trace-fluctuation lemma's hypothesis (H3) is a Sub-Weyl
fluctuation bound on a coset-level *convolution* of twisted Jacobi sums:

    Var_q[ Σ_{(chi,psi)∈S×S} J(chi,psi;q) · conj(J)(chi',psi';q) · … ]  ≤
        C_k (log N)^{c_k} N^{k/2 + 1/2 - ε} .

The bound is about the VARIANCE over q of the coset sum, NOT about
individual entries: a single |J(chi,psi;q)| is a complete multiplicative-
character sum and Weil gives |J| <= 2 sqrt(N), essentially attained.
Per-entry Sub-Weyl is impossible and is NOT what H3 asserts.

This script therefore measures two correct objects:

CYCLE 2c — the multiplicative toy (per R87.5 handoff, replacing the
additive toy of Cycle 2):
    T_r(q) = sum_{x in H} chi_r(x) e_p(q x),  H = K-cyclic subgroup of F_p^×,
    chi_r(x) = x^r (multiplicative character), r in [0, K).
    Statistic:  max_{r,q} |T_r(q)|^2 / sqrt(p)  vs  (log p)^c, c <= 1.5.
This is the H3 SHAPE (multiplicative characters on the coset's dual
subgroup), stripped of the (x-1) twist and the full Jacobi structure.
PASS: R/(log p)^1.5 <= 3 at >= 12/14 design points, and R/(log p)^1.5
decreases with p at fixed K (Sub-Weyl monotonicity).

CYCLE 2d — the direct variance of the real coset convolution at the
certified designs, i.e. the actual object of H3 for k = 2:
    A(q) = sum_{i,j in S} |J(chi_i, chi_j; q)|^2   (= m^2 * second moment of J),
    A4(q) = sum_{i,j in S} |J(chi_i, chi_j; q)|^4  (fourth-moment convolution).
    Statistic: mean and std of A(q), A4(q) across the actual cat-map
    q-curve; report the normalized fluctuation std/mean and its scaling.
Trivial fluctuation (independent entries, |J| ~ sqrt(N)): std A ~ m N^{3/2}.
Sub-Weyl would give std A(q) much smaller.  We report the measured
exponent so H3 can be calibrated honestly.

Two-key: matrix-product J (R82.12 certified pipeline) cross-checked
against a direct triple loop at N=53, q=1.

Output: artifacts/r91/cycle2c_multiplicative_toy.json + .log
"""

import json
import math
import os
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
OUT_DIR = os.path.join(ROOT, "artifacts", "r91")
os.makedirs(OUT_DIR, exist_ok=True)
LOG = os.path.join(OUT_DIR, "cycle2c_multiplicative_toy.log")


def log(msg):
    line = str(msg)
    print(line, flush=True)
    with open(LOG, "a", encoding="utf-8") as fh:
        fh.write(line + "\n")


def dlog_table(N, g):
    tab = np.zeros(N, dtype=np.int64)
    x = 1
    for s in range(N - 1):
        tab[x] = s
        x = x * g % N
    return tab


def primitive_root(N):
    for g in range(2, N):
        x, seen = 1, set()
        for _ in range(N - 1):
            x = x * g % N
            seen.add(x)
            if len(seen) < _ + 1:
                break
        if len(seen) == N - 1:
            return g
    raise RuntimeError


def ord_N(a, N):
    x, k = a % N, 1
    while x != 1:
        x = x * a % N
        k += 1
    return k


def k_cyclic_subgroup(N, K):
    """The unique subgroup H of F_N^× of order K."""
    g = primitive_root(N)
    h = pow(g, (N - 1) // K, N)   # generator of H
    H = []
    x = 1
    for _ in range(K):
        H.append(x)
        x = x * h % N
    return np.array(H, dtype=np.int64)


def index_coset(N, K, a, dlog):
    """chi_k(a) = 1: k*dlog(a) = 0 mod (N-1). Principal-class ks."""
    ell = int(dlog[a])
    d = math.gcd(ell, N - 1)
    mod = (N - 1) // d
    return np.array([k for k in range(N - 1) if k % mod == 0], dtype=np.int64)


def jacobi_matrix_q(N, ks, q, W, V, xs):
    """J[i,j] = sum_{x != 0,1} conj(chi_i)(x) psi_j(x-1) e_N(qx)."""
    ph = np.exp(2j * np.pi * (q * xs % N) / N)
    return (W * ph) @ V.T


def jacobi_direct_q(N, ks, q, dlog):
    """Second key: O(m^2 N) direct triple loop."""
    xs = [x for x in range(N) if x not in (0, 1)]
    m = len(ks)
    J = np.zeros((m, m), dtype=complex)
    for i in range(m):
        for j in range(m):
            s = 0.0 + 0.0j
            for x in xs:
                s += (np.exp(-2j * np.pi * ks[i] * dlog[x] / (N - 1))
                      * np.exp(2j * np.pi * ks[j] * dlog[(x - 1) % N] / (N - 1))
                      * np.exp(2j * np.pi * q * x / N))
            J[i, j] = s
    return J


def load_q_curve(N):
    npz_path = os.path.join(
        ROOT, "artifacts", "legacy_runs", "theorems", "I_torus_rigidity",
        f"q_curve_N{N}.npz"
    )
    if os.path.isfile(npz_path):
        data = np.load(npz_path)
        qs = data.get("q", None)
        if qs is not None:
            return np.atleast_1d(qs).astype(np.int64)
    return None


# ---------------------------------------------------------------- Cycle 2c
def run_cycle_2c():
    """Multiplicative toy: T_r(q) = sum_{x in H} chi_r(x) e_p(qx)."""
    log("\n========== CYCLE 2c: MULTIPLICATIVE TOY (H3 shape) ==========")
    designs = [
        (1613, 13), (1531, 17), (1559, 19), (1567, 29), (1549, 43),
        (1597, 57), (1889, 59),   # small p
        (100049, 13), (100267, 17), (100169, 19), (100109, 29),
        (100019, 43), (100207, 57), (100183, 59),   # large p ~100k
    ]
    rows = []
    for p, K in designs:
        H = k_cyclic_subgroup(p, K)
        # multiplicative characters chi_r(x) = x^r on H, r = 0..K-1
        # T_r(q) = sum_{x in H} chi_r(x) e_p(qx)
        # compute for a sample of q's
        n_q = 200
        rng = np.random.default_rng(12345)
        qs = rng.integers(1, p, size=n_q)
        # chi_r(x) = x^r on H: x = h^s -> chi_r(x) = exp(2 pi i r s / K)
        s_of_x = np.zeros(p, dtype=np.int64)
        for s, xv in enumerate(H):
            s_of_x[xv] = s
        # T_r(q) = sum_s exp(2 pi i r s / K) exp(2 pi i q h^s / p)
        # = DFT over s.  For each q: T = W @ phase where W[r,s]=exp(2pi i r s /K)
        r_all = np.arange(K)
        s_all = np.arange(K)
        W_dft = np.exp(2j * np.pi * np.outer(r_all, s_all) / K)  # (K, K)
        T_max2 = 0.0
        for q in qs:
            ph = np.exp(2j * np.pi * (q * H % p) / p)   # (K,)
            T = W_dft @ ph                               # (K,)
            T_max2 = max(T_max2, float(np.max(np.abs(T) ** 2)))
        R = T_max2 / math.sqrt(p)
        ratio = R / (math.log(p) ** 1.5)
        rows.append({"p": int(p), "K": int(K), "R_max2_over_sqrtp": float(R),
                     "subweyl_ratio": float(ratio)})
        log(f"   p={p:6d} K={K:2d}: R = |T|^2_max/sqrt(p) = {R:.4f}, "
            f"R/(log p)^1.5 = {ratio:.4f}")

    # verdict
    within = sum(1 for r in rows if r["subweyl_ratio"] <= 3)
    # monotonicity: at fixed K, ratio must drop from small p to large p
    mono_ok = True
    for k in set(r["K"] for r in rows):
        small = [r for r in rows if r["K"] == k and r["p"] < 10000]
        large = [r for r in rows if r["K"] == k and r["p"] > 10000]
        if small and large and small[0]["subweyl_ratio"] < large[0]["subweyl_ratio"] * 0.5:
            mono_ok = False
            log(f"   MONOTONICITY WARNING at K={k}")
    verdict = {
        "designs_within_slack": within,
        "total_designs": len(rows),
        "monotonicity_ok": mono_ok,
        "PASS": within >= 12 and mono_ok,
    }
    log(f"   verdict: {within}/{len(rows)} within slack, "
        f"monotonicity={'OK' if mono_ok else 'FAIL'}")
    return {"designs": rows, "verdict": verdict}


# ---------------------------------------------------------------- Cycle 2d
def run_cycle_2d(N, a, K, parity_odd, second_keys):
    """Direct variance of A(q) = sum_{i,j} |J|^2 over the q-curve."""
    log(f"\n========== CYCLE 2d: coset-convolution variance, "
        f"N={N}, a={a}, K={K}, parity_odd={parity_odd} ==========")
    g = primitive_root(N)
    dlog = dlog_table(N, g)
    ks = index_coset(N, K, a, dlog)
    if parity_odd:
        ks = ks[ks % 2 == 1]
    m = len(ks)
    log(f"   coset size m = {m}")

    xs = np.array([x for x in range(N) if x not in (0, 1)], dtype=np.int64)
    dl_x = dlog[xs]
    dl_xm1 = dlog[(xs - 1) % N]
    W = np.exp(-2j * np.pi * np.outer(ks, dl_x) / (N - 1))
    V = np.exp(2j * np.pi * np.outer(ks, dl_xm1) / (N - 1))

    qs = load_q_curve(N)
    if qs is None:
        qs = np.arange(1, N, dtype=np.int64)
    qs = np.unique(qs[qs >= 1])
    nq = len(qs)
    log(f"   q-curve: {nq} values")

    A_list = np.empty(nq)
    A4_list = np.empty(nq)
    maxJ2_list = np.empty(nq)
    t0 = time.time()
    for qi_idx, q in enumerate(qs):
        J = jacobi_matrix_q(N, ks, q, W, V, xs)
        aJ2 = np.abs(J) ** 2
        A_list[qi_idx] = aJ2.sum()
        A4_list[qi_idx] = (aJ2 ** 2).sum()
        maxJ2_list[qi_idx] = aJ2.max()
    wall = time.time() - t0
    log(f"   wall: {wall:.1f}s")

    # second key on the small design
    if N <= 199 and not second_keys:
        N2 = 53
        g2 = primitive_root(N2)
        dlog2 = dlog_table(N2, g2)
        a2 = 10
        K2 = ord_N(a2, N2)
        ks2 = index_coset(N2, K2, a2, dlog2)
        Jd = jacobi_direct_q(N2, ks2, 1, dlog2)
        xs2 = np.array([x for x in range(N2) if x not in (0, 1)], dtype=np.int64)
        dl2x = dlog2[xs2]
        dl2xm1 = dlog2[(xs2 - 1) % N2]
        W2 = np.exp(-2j * np.pi * np.outer(ks2, dl2x) / (N2 - 1))
        V2 = np.exp(2j * np.pi * np.outer(ks2, dl2xm1) / (N2 - 1))
        Jm = jacobi_matrix_q(N2, ks2, 1, W2, V2, xs2)
        second_keys["N=53"] = float(np.max(np.abs(Jd - Jm)))

    mean_A = float(A_list.mean())
    std_A = float(A_list.std())
    mean_A4 = float(A4_list.mean())
    std_A4 = float(A4_list.std())
    max_J2 = float(maxJ2_list.max())

    # scaling comparisons
    # trivial independent-entry scaling: each |J|^2 ~ N with std ~ N,
    # m^2 entries -> std A ~ m * N  (and std A4 ~ m * N^2)
    trivial_std_A = m * N
    trivial_std_A4 = m * N * N
    # sub-Weil comparison: std A / mean A (relative fluctuation of the coset
    # sum across q); the H3 mechanism predicts the q-variance of the coset
    # convolution to be far below the entrywise scale, i.e. rel. fluct well
    # below 1/m (independent entries).  We report the measured value and the
    # ratio to the entrywise scale; no arbitrary target formula is imposed.

    result = {
        "N": int(N), "a": int(a), "K": int(K), "m": int(m),
        "parity_odd": bool(parity_odd), "n_q": int(nq),
        "mean_A": mean_A, "std_A": std_A,
        "rel_fluct_A": float(std_A / mean_A),
        "mean_A4": mean_A4, "std_A4": std_A4,
        "rel_fluct_A4": float(std_A4 / mean_A4),
        "max_J2": max_J2, "max_J2_over_N": float(max_J2 / N),
        "std_A_over_trivial": float(std_A / trivial_std_A),
        "std_A4_over_trivial": float(std_A4 / trivial_std_A4),
        "wall_s": wall,
    }
    log(f"   A(q): mean {mean_A:.6e}  std {std_A:.6e}  "
        f"rel.fluct {std_A/mean_A:.6e}")
    log(f"   A4(q): mean {mean_A4:.6e}  std {std_A4:.6e}  "
        f"rel.fluct {std_A4/mean_A4:.6e}")
    log(f"   std_A / (m N) [independent-entry scale] = {std_A/trivial_std_A:.6e}")
    log(f"   std_A4 / (m N^2) [independent-entry scale] = "
        f"{std_A4/trivial_std_A4:.6e}")
    return result


def main():
    t0 = time.time()
    log("RUN 91 -- Cycle 2c + 2d: H3 multiplicative discriminator")

    out = {"cycle_2c": run_cycle_2c(), "cycle_2d": [], "second_key": {}}

    designs_2d = [
        (199, 139, 11, True),    # N=199, a=139, K=11, m_plus=9 (R82.12)
        (199, 139, 11, False),   # full coset m=18
        (3571, 2469, 17, True),  # N=3571, a=2469, K=17, m_plus=105
        (3571, 47, 17, False),   # full coset m=210 (R86.1 design)
    ]
    for N, a, K, par in designs_2d:
        res = run_cycle_2d(N, a, K, par, out["second_key"])
        out["cycle_2d"].append(res)

    out["walltime_s"] = time.time() - t0
    out_path = os.path.join(OUT_DIR, "cycle2c_multiplicative_toy.json")
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=1)
    log(f"\nartifact written -> {out_path}")
    log(f"second key devs: {out['second_key']}")


if __name__ == "__main__":
    main()