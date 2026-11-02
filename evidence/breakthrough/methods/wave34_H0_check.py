"""Wave 34, task 4: exact integer check of Lemma 1 (S_q Gamma-invariance).

m = 12, all five components q | D_12. Definitions (waves 14/16):
  H = 6I - S - S^-1 (circulant), X = adj(H) (exact, sympy),
  K_q = ker(H mod q) (SNF kernel, size q), W = H(K_q)/q,
  Q[i] = W_i^T X W_i mod q, P[i,j] = W_i^T X W_j mod q,
  T[i,j] = (2*Q[i] - P[i,j]) mod q   (s = 1; invariance is s-independent),
  S_q[j] = sum_i zeta_q^{T[i,j]}.
Gamma = dihedral group on positions (shifts + reflections), acting on
vectors by coordinate permutation: (gamma.v)[j] = v[p[j]].

Checks (all exact integers, no floating point):
  (0) gamma H gamma^-1 = H and gamma X gamma^-1 = X for every gamma.
  (1) Q[gamma.i] = Q[i] and P[gamma.i, gamma.j] = P[i,j] for every gamma.
  (2) S_q multiset invariance: sorted column T[:, gamma.j] = sorted
      column T[:, j] for every gamma, j (hence S_q[gamma.j] = S_q[j]).
  (3) S_q constant on every Gamma-orbit (signature = sorted T-column),
      and on the split q=81 fiber its three orbits have pairwise
      distinct signatures (so a split component fiber CAN carry
      distinct phases, while a single-orbit component fiber CANNOT).
Repository untouched; no Lean build.
"""
import sys

import numpy as np
import sympy as sp

sys.path.insert(0, ".")
from wave16_d1a_targeted import snf_kernel, gamma_perms, lex_canon, group_ids

m = 12
Hsp = sp.zeros(m)
for i in range(m):
    Hsp[i, i] = 6
    Hsp[i, (i - 1) % m] -= 1
    Hsp[i, (i + 1) % m] -= 1
H = np.array(Hsp.tolist(), dtype=np.int64)
X = np.array(Hsp.adjugate().tolist(), dtype=np.int64)
perms = gamma_perms(m)
print(f"m={m} |Gamma|={len(perms)} Xmax={int(np.abs(X).max())}", flush=True)

# (0) dihedral symmetry of H and of its adjugate
for p in perms:
    Pi = np.zeros((m, m), dtype=np.int64)
    Pi[np.arange(m), p] = 1
    assert np.array_equal(Pi @ H @ Pi.T, H), "H not dihedral-symmetric"
    assert np.array_equal(Pi @ X @ Pi.T, X), "X not dihedral-symmetric"
print("(0) gamma H gamma^-1 = H and gamma X gamma^-1 = X: ALL PASS",
      flush=True)


def H_np(v):
    return 6 * v - np.roll(v, 1, axis=1) - np.roll(v, -1, axis=1)


for q in (128, 81, 25, 49, 121):
    K = snf_kernel(m, q)
    assert len(K) == q
    HK = H_np(K)
    assert np.all(HK % q == 0)
    W = HK // q
    Q = np.einsum("ij,ij->i", W @ X, W) % q
    P = (W @ X) @ W.T % q
    T = (2 * Q[:, None] - P) % q
    lookup = {tuple(row): i for i, row in enumerate(K)}
    # (1)+(2) for every gamma
    Ts = np.sort(T, axis=0)
    for p in perms:
        idx = np.array([lookup[tuple(row)] for row in K[:, p]])
        assert np.all(Q[idx] == Q), (q, "Q invariance")
        assert np.all(P[np.ix_(idx, idx)] == P), (q, "P invariance")
        assert np.all(Ts[:, idx] == Ts), (q, "S multiset invariance")
    # (3) orbits vs fibers
    fib = group_ids(np.sort(K, axis=1))
    orb = group_ids(lex_canon(K, perms))
    sig = [tuple(np.sort(T[:, j]).tolist()) for j in range(len(K))]
    for o in set(orb.tolist()):
        ss = {sig[j] for j in np.where(orb == o)[0]}
        assert len(ss) == 1, (q, "S not constant on orbit", o)
    split = [f for f in set(fib.tolist())
             if len(set(orb[np.where(fib == f)[0]].tolist())) > 1]
    detail = []
    for f in split:
        os_ = sorted(set(orb[np.where(fib == f)[0]].tolist()))
        sigs = {sig[int(np.where(orb == o)[0][0])] for o in os_}
        detail.append((f, int((fib == f).sum()), len(os_), len(sigs)))
    print(f"q={q}: (1)(2) ALL {len(perms)} gamma PASS; "
          f"S constant on all {len(set(orb.tolist()))} orbits; "
          f"split fibers={len(split)} {detail}", flush=True)
print("ALL CHECKS PASS", flush=True)
