"""Wave 35, task 2: exact checks for the Lemma F exponent identity.

For each m in {8, 12} and each prime-power component q of D_m:
  (A) component-level: T[i,j] = 2s*Q[i] - P[i,j] (mod q) from W = HK/q.
      Check whether (u^2 - 1)*T == 0 (mod q) for ALL pairs (i,j).
      If yes, raw mode (T == t) and corrected mode (u^-2 T == t) coincide
      on every occurring value -- this explains the code's "raw"
      components. If no, the u^-2 correction is genuinely needed.
  (B) global-level: sample global Fix points via CRT, compute the
      global exponent tg = (2s*Qnum(w_i) - pairNum(w_i,w_j)) mod q,
      and check u^-2 * T[idx_i, idx_j] == tg (mod q) for all samples.
      This is identity (a) of the proof: T == u^2 * t (mod q).
"""
import sys
import numpy as np
import sympy as sp

sys.path.insert(0, ".")
from wave16_d1a_targeted import Dm, snf_kernel, crt_combine

def H_np(v):
    return 6 * v - np.roll(v, 1, axis=1) - np.roll(v, -1, axis=1)

def adjugate(m):
    Hsp = sp.zeros(m)
    for i in range(m):
        Hsp[i, i] = 6
        Hsp[i, (i - 1) % m] -= 1
        Hsp[i, (i + 1) % m] -= 1
    return np.array(Hsp.adjugate().tolist(), dtype=np.int64)

def pairnum(A, B, X):
    return (A @ X) @ B.T

def qnum(A, X):
    return np.einsum("ij,ij->i", A @ X, A)

rng = np.random.default_rng(7)
for m, QS, ss in ((12, [128, 81, 25, 49, 121], (1, 13)),
                  (8, [9, 289, 512], (1, 5))):
    D = Dm(m)
    assert D == int(np.prod(QS)), (m, D, QS)
    X = adjugate(m)
    comp = {}
    for q in QS:
        K = snf_kernel(m, q)
        assert len(K) == q
        HK = H_np(K)
        assert np.all(HK % q == 0)
        W = HK // q
        comp[q] = {"K": K, "W": W, "Q": qnum(W, X) % q,
                   "P": pairnum(W, W, X) % q,
                   "lookup": {tuple(row): i for i, row in enumerate(K)}}
    print(f"== m={m} D={D} ==", flush=True)
    for s in ss:
        print(f"  s={s}:", flush=True)
        for q in QS:
            c = comp[q]
            u = (D // q) % q
            inv_u2 = pow((u * u) % q, -1, q)
            T = (2 * s * c["Q"][:, None] - c["P"]) % q
            # (A) exhaustive component check
            raw_all = bool(np.all(((u * u - 1) * T) % q == 0))
            n_raw_fail = int(np.count_nonzero(((u * u - 1) * T) % q))
            print(f"    q={q}: u={u} u^2%q={(u*u) % q} "
                  f"(u^2-1)*T==0 for all pairs: {raw_all} "
                  f"(fails {n_raw_fail}/{q*q})", flush=True)
        # (B) global sample check of identity (a)
        n = 400
        pts = {}
        for q in QS:
            sel = rng.integers(0, len(comp[q]["K"]), size=n)
            pts[q] = comp[q]["K"][sel]
        glob = crt_combine(m, D, QS, pts)
        assert np.all(H_np(glob) % D == 0)
        wglob = H_np(glob) // D
        Qg = qnum(wglob, X)
        bad = 0
        tot = 0
        for _ in range(2000):
            i = int(rng.integers(0, n))
            j = int(rng.integers(0, n))
            for q in QS:
                c = comp[q]
                u = (D // q) % q
                inv_u2 = pow((u * u) % q, -1, q)
                ii = c["lookup"][tuple(glob[i] % q)]
                jj = c["lookup"][tuple(glob[j] % q)]
                tg = int((2 * s * Qg[i]
                          - int(pairnum(wglob[i:i + 1], wglob[j:j + 1], X)[0, 0])) % q)
                tc = int((2 * s * c["Q"][ii] - c["P"][ii, jj]) % q)
                tot += 1
                if (inv_u2 * tc) % q != tg:
                    bad += 1
        print(f"    global identity (a): {tot - bad}/{tot} pass, bad={bad}",
              flush=True)
        assert bad == 0
print("ALL CHECKS PASS")
