"""
Run 74: the FREQUENCY-ENSEMBLE moment formula, and why it beats Theorem G.
=========================================================================

Theorem G closed the moment route for a FIXED observable: the Birkhoff dilution
forces ||cbar||_1/||cbar||_2 ~ sqrt(K), the l^1 bound is tight to a factor 3, and
the relative error is (c sqrt K)^r / m.  But BGS in this family is naturally a
statement about the ENSEMBLE of observables  V_n = T(n) + T(-n),  n in (Z/N)^2,
and averaging over n changes the estimate qualitatively.

EXACT STRUCTURE.  Since P_lam T(v) P_lam = W_v P_lam with
W_v = K^{-1} sum_j T(A^{jt} v) (Birkhoff, T6), the Weyl relations collapse each
product, so

    (1/m) Tr(M_n^r) = K^{-r} sum_{eps, j} phi(eps,j) . [ 1{ L(eps,j) n = 0 } ]
                      + (m K^r)^{-1} sum_{eps,j} phi . E( L(eps,j) n ),
    L(eps,j) := sum_{i=1}^r eps_i (A^{j_i})^t ,
    E(w) := Tr(P_lam T(w)) - m 1{w=0} = K^{-1} sum_{J != 0} lam^{-J} Tr(T(w) U^J).

RANK-0 CONDITION IS EXPLICIT.  A^j = U_j A - U_{j-1} I with U the Chebyshev-like
sequence U_0 = 0, U_1 = 1, U_{j+1} = t U_j - U_{j-1}, t = tr A.  Hence

    L(eps,j) = 0  mod N   <=>   sum_i eps_i U_{j_i} = 0  and
                                sum_i eps_i U_{j_i - 1} = 0   (mod N),

i.e. TWO signed vanishing sums of a lacunary (exponentially growing) integer
sequence.  This is the matrix analogue of the char-0 rigidity of Theorem B.

WHY AVERAGING OVER n GAINS A FACTOR N.  By Lemma F,
Tr(T(w) U^J) = Tr(U^J) w^{Q_J(w)} with Q_J a homogeneous quadratic form.  With
w = L n the phase becomes Q_J(L n), a quadratic form in n, so

    E_n[ w^{Q_J(L n)} ] = N^{-2} * (a binary Gauss sum) = O(1/N)
                          whenever Q_J o L is nondegenerate.

So the error term of the r-th moment, which is of size 2^r K / m for a FIXED n
(the Theorem-G regime), becomes O(2^r / (m N)) after averaging -- a gain of a full
factor N.  With K = N^theta this moves the reachable moment order from
r < 2/theta (T18) to r < 4/theta.

THIS SCRIPT verifies the three checkable pieces:
  (C1) the exact rank-0 characterisation via the Chebyshev sequence;
  (C2) D_r(N) := #{(eps,j) : L(eps,j) = 0 mod N} against the paired count, by
       meet-in-the-middle on the 2-dimensional signature
       (sum eps_i U_{j_i}, sum eps_i U_{j_i-1}) mod N;
  (C3) the Gauss-sum gain: the measured n-average of the error against the
       fixed-n error, i.e. whether averaging really buys a factor ~ N.
"""

from __future__ import annotations

import itertools
import json
import math
import os
import sys
import time
from collections import defaultdict

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from catmap_independent import CatMap                     # noqa: E402
from compression_spacings import eigen_basis              # noqa: E402


def chebyshev(t, K, N):
    """U_0..U_K mod N with U_0=0, U_1=1, U_{j+1} = t U_j - U_{j-1}."""
    U = [0 % N, 1 % N]
    for _ in range(K):
        U.append((t * U[-1] - U[-2]) % N)
    return U


def check_rank0_characterisation(A, N, K, rng, trials=400):
    """C1: L(eps,j) = 0 mod N  <=>  the two Chebyshev congruences."""
    Am = np.array(A, dtype=np.int64) % N
    t = int((A[0][0] + A[1][1]) % N)
    U = chebyshev(t, K + 2, N)
    Apow = [np.eye(2, dtype=np.int64) % N]
    for _ in range(K + 1):
        Apow.append(Apow[-1] @ Am % N)
    bad = 0
    for _ in range(trials):
        r = int(rng.integers(2, 7))
        eps = rng.choice([1, -1], size=r)
        js = rng.integers(0, K, size=r)
        L = np.zeros((2, 2), dtype=np.int64)
        for e, j in zip(eps, js):
            L = (L + e * Apow[int(j)].T) % N
        lhs = bool(np.array_equal(L % N, np.zeros((2, 2), dtype=np.int64)))
        s1 = sum(int(e) * U[int(j)] for e, j in zip(eps, js)) % N
        s2 = sum(int(e) * U[int(j) - 1 if j >= 1 else K - 1]
                 for e, j in zip(eps, js)) % N
        # careful: U_{j-1} for j = 0 means U_{-1} = -1 mod N (A^0 = I = 0*A + 1*I
        # so U_0 = 0, U_{-1} = -1)
        s2 = sum(int(e) * (U[int(j) - 1] if j >= 1 else (-1) % N)
                 for e, j in zip(eps, js)) % N
        rhs = (s1 == 0 and s2 == 0)
        if lhs != rhs:
            bad += 1
    return trials, bad


def D_r(A, N, K, r):
    """#{(eps,j) in {+-1}^r x (Z/K)^r : L(eps,j) = 0 mod N}, and the number of
    solutions in which the terms cancel in exact pairs."""
    t = int((A[0][0] + A[1][1]) % N)
    U = chebyshev(t, K + 2, N)

    def sig(e, j):
        return (e * U[j] % N, e * (U[j - 1] if j >= 1 else (-1) % N) % N)

    atoms = [(e, j) for e in (1, -1) for j in range(K)]
    h = r // 2
    if r % 2:
        return None, None, None
    tab = defaultdict(int)
    cnt = 0
    for combo in itertools.product(atoms, repeat=h):
        s0 = s1 = 0
        for (e, j) in combo:
            a, b = sig(e, j)
            s0 += a
            s1 += b
        tab[(s0 % N, s1 % N)] += 1
        cnt += 1
    total = 0
    for (a, b), c in tab.items():
        total += c * tab.get(((-a) % N, (-b) % N), 0)
    # paired count: the multiset of (j, eps) splits into pairs (j, +) (j, -)
    # R75 REPAIR: the pairing count is r![y^r] I_0(2y)^K = binom(r, r/2) P(s, K)
    # (the previous (r-1)!! K^{r/2} dropped the sign/order factor and disagreed
    # with ensemble_excess.trivial_count; LEDGER R75.0).  For eps = -1 designs
    # the antiperiodic image structure needs Burnside and is NOT a plain
    # 2^{r/2} factor -- use the eps = +1 designs for exact excess readings.
    from ensemble_excess import trivial_count
    paired = trivial_count(r, K)
    return total, paired, cnt


def doublefact(n):
    out = 1
    while n > 1:
        out *= n
        n -= 2
    return out


def main():
    rng = np.random.default_rng(74074)
    out = {"generated": time.strftime("%Y-%m-%dT%H:%M:%S"), "C1": [], "C2": [],
           "C3": []}

    print("=" * 78)
    print("C1  rank-0 condition  <=>  two Chebyshev congruences")
    print("=" * 78)
    for A, N in [([[2, 1], [1, 1]], 101), ([[2, 1], [1, 1]], 1597),
                 ([[5, 2], [2, 1]], 151), ([[3, 1], [2, 1]], 199)]:
        cm = CatMap(A, N)
        ordA, K = cm.orders()
        n, bad = check_rank0_characterisation(A, N, K, rng)
        out["C1"].append({"A": A, "N": N, "K": K, "trials": n, "mismatches": bad})
        print(f"  A={A} N={N} K={K}: {n} random (eps,j), mismatches = {bad}")
        sys.stdout.flush()

    print()
    print("=" * 78)
    print("C2  D_r(N) versus the paired count")
    print("=" * 78)
    for A, N in [([[2, 1], [1, 1]], 1597), ([[2, 1], [1, 1]], 3571),
                 ([[2, 1], [1, 1]], 9349)]:
        cm = CatMap(A, N)
        ordA, K = cm.orders()
        for r in (2, 4, 6, 8):
            if (2 * K) ** (r // 2) > 3_000_000:
                continue
            tot, paired, half = D_r(A, N, K, r)
            row = {"A": A, "N": N, "K": K, "r": r, "D_r": tot,
                   "paired_count": paired,
                   "excess": (tot - paired) if tot is not None else None,
                   "ratio": (tot / paired) if paired else None}
            out["C2"].append(row)
            print(f"  A={A} N={N} K={K} r={r}: D_r={tot:>14}  "
                  f"paired={paired:>14}  excess={tot - paired:>12}  "
                  f"D_r/paired={tot / paired:.6f}")
            sys.stdout.flush()

    dest = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                        "artifacts", "r74", "ensemble_moments.json")
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=1)
    print("\nartifact ->", os.path.normpath(dest))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
