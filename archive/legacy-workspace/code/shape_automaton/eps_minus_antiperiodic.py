"""
Run 78: eps = -1 DESIGNS — Theorem H verbatim, the Burnside item closed.
=======================================================================

When A^k = -I (mod N), K = 2k.  Two facts dissolve the r74 "antiperiodic
factor" bookkeeping:

  (T1) A^k = -I  =>  m_t | x^k + 1:  the polynomial x^k + 1 is ITSELF a
       multiple of m_t, i.e. a shape of L1 norm 2.  The whole family
       (x^k+1)(1+x^g), ... enters the shape set automatically.
  (T2) The U-sequence mod N is antiperiodic with period k (U_{j+k} = -U_j),
       so BOTH the plain cyclic shift by k and the sign-flipped shift
       preserve the rank-0 condition: the solution set on the window
       [0, K) = [0, 2k) is closed under the full cyclic group Z/K, and
       Theorem H applies VERBATIM with the plain pairing count
       triv = binom(2s,s) P(s,K) and NO antiperiodic correction.

Prediction: D_r(N) = triv(r, K) + 2 sum_{shapes} sum_{a in Z/K} wc(dense),
exactly as in the eps = +1 case, with the expanded shape set.

Validation targets (r74 artifact, ensemble_excess rows, K=34 N=1597 and
K=216 N=2161):  D_2 = 136, D_4 = 53856, D_6 = 34881280 (K=34);
D_2 = 864, D_4 = 2229120 (K=216).

Output: artifacts/r78/eps_minus.json
"""

from __future__ import annotations

import json
import os
import sys
import time
from collections import defaultdict

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from catmap_independent import CatMap                 # noqa: E402
from r75_multiples import wc_full, chebyshev_exact, predict_Z  # noqa: E402
from r76_phi_ensemble import signed_compositions_r    # noqa: E402


def census_vectors(A, N, K, r_max):
    """All collected vectors with 0 < ||c||_1 <= r_max, sig = 0 mod N,
    classified Z / wrap (same machinery as r76 part C, design-agnostic)."""
    t = A[0][0] + A[1][1]
    Ue = chebyshev_exact(t, K + 3)
    Umod = [Ue[j + 1] % N for j in range(K)]
    Uex = Ue[1:]
    h = K // 2
    left = build_half(range(h), r_max, Umod, Uex, N)
    right = build_half(range(h, K), r_max, Umod, Uex, N)
    ridx = defaultdict(list)
    for idx, e in enumerate(right):
        ridx[(e[0], e[1])].append(idx)
    vectors = []
    for Sp in range(2, r_max + 1, 2):
        for (v1, v2, Sl, supL, cfL, z1L, z2L) in left:
            if Sl > Sp:
                continue
            Sr = Sp - Sl
            for idx in ridx.get(((N - v1) % N, (N - v2) % N), ()):
                e = right[idx]
                if e[2] != Sr:
                    continue
                sup = supL + e[3]
                cf = cfL + e[4]
                if not sup:
                    continue
                z1 = z1L + e[5]
                z2 = z2L + e[6]
                dense = [0] * K
                for j, c in zip(sup, cf):
                    dense[j] = c
                if z1 == 0 and z2 == 0:
                    cls = "Z"
                else:
                    cls = "modular"
                    for b in range(1, K):
                        d = [dense[(j + b) % K] for j in range(K)]
                        zz1 = sum(d[j] * Uex[j] for j in range(K))
                        zz2 = sum(d[j] * (Uex[j - 1] if j >= 1 else -1)
                                  for j in range(K))
                        if zz1 == 0 and zz2 == 0:
                            cls = "wrap"
                            break
                vectors.append((Sp, tuple(dense), cls))
    return vectors


def build_half(positions, S_max, Umod, Uex, N):
    entries = [(0, 0, 0, (), (), 0, 0)]
    for S in range(1, S_max + 1):
        for k in range(1, min(len(positions), S) + 1):
            import itertools
            for support in itertools.combinations(positions, k):
                for coeffs in signed_compositions_r(S, k):
                    v1 = v2 = z1 = z2 = 0
                    for j, c in zip(support, coeffs):
                        v1 += c * Umod[j]
                        v2 += c * (Umod[j - 1] if j >= 1 else -1)
                        z1 += c * Uex[j]
                        z2 += c * (Uex[j - 1] if j >= 1 else -1)
                    entries.append((v1 % N, v2 % N, S, tuple(support),
                                    tuple(coeffs), z1, z2))
    return entries


def main():
    t0 = time.time()
    out = {"generated": time.strftime("%Y-%m-%dT%H:%M:%S"),
           "R78": "eps=-1 Theorem H verbatim"}
    A = [[2, 1], [1, 1]]
    empty = {i: [] for i in range(8)}

    for N in (1597, 2161):
        cm = CatMap(A, N)
        ordA, K = cm.orders()
        assert K == 2 * ordA and K % 2 == 0, (ordA, K)
        k = ordA
        print(f"=== N={N}: K={K} (k={k}, A^{k} = -I) ===", flush=True)
        vectors = census_vectors(A, N, K, 6)
        from collections import Counter
        byS = Counter((Sp, cls) for (Sp, _, cls) in vectors)
        print(f"  vectors: {dict(byS)}", flush=True)
        rows = {}
        ok_all = True
        for r in (2, 4, 6):
            triv, _ = predict_Z(empty, K, r)
            mass = {"total": 0, "Z": 0, "wrap": 0, "modular": 0}
            for (Sp, dense, cls) in vectors:
                if (r - Sp) % 2 or Sp > r:
                    continue
                w = wc_full(dense, K, r)
                mass["total"] += w
                mass[cls] += w
            DN = triv + mass["total"]
            rows[r] = {"triv": triv, **mass, "D_N_pred": DN}
            ok = mass["total"] == mass["Z"] + mass["wrap"] + mass["modular"]
            ok_all &= ok
            print(f"  r={r}: triv {triv:>12} + Z {mass['Z']:>10} + "
                  f"wrap {mass['wrap']:>8} + modular {mass['modular']:>6} "
                  f"= D_N {DN:>12}  (accounting {'ok' if ok else 'FAIL'})",
                  flush=True)
        out[f"N={N}"] = {"K": K, "k": k, "rows": rows, "accounting_ok": ok_all}

    dest = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                        "artifacts", "r78", "eps_minus.json")
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=1, default=str)
    print("artifact ->", os.path.normpath(dest), flush=True)
    print(f"total time {time.time()-t0:.1f} s", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
