"""
Run 82g: THE MODULATION CURVE q -> spec(V_q) IN CLOSED FORM?
===========================================================
Theorem I (certified in src/r82f_torus_rigidity.py) states that the family
V_n = P_+(T(n) + T(-n))P_+ depends on n only through the torus invariant
q = Q(n) = n_1^2 - n_1 n_2 - n_2^2 mod N: at most N distinct spectra, each
level set being a single orbit of the centraliser torus T, which acts by Weil
operators commuting with U_A.

Since the level sets are indexed by q in F_N^* -- a cyclic GROUP -- the natural
expansions of any spectral functional f(q) are

  (M) the multiplicative-character expansion  f(q) = sum_chi a_chi chi(q),
  (Ad) the additive-Fourier expansion         f(q) = sum_a b_a e_N(a q).

The word expansion of Tr(V_n^r) is a sum of Weil-type phases w^{Q_J(v)} with
v = sum eps_i A^{J_i} n, i.e. quadratic forms in n; after Theorem I collapses
n to q, such sums are Gauss/Kloosterman-type functions of q.  A SPARSE
expansion in either basis would put the arithmetic modulation in closed form.

PRE-REGISTERED (before the run):
  P5  q -> mu_4(q) is far from constant (this is just the R82c spread seen
      through the correct parameter) and is a genuine function of q.  [~95%]
  P6  the additive-Fourier or multiplicative-character expansion of the
      raw second moment Tr(V_q^2) is SPARSE (a handful of coefficients
      carrying > 90% of the variance).                                [~45%]
  P7  the same for mu_4(q).                                           [~30%]
  P8  mu_4(q) is invariant under q -> -q or under q -> c q for a
      nontrivial subgroup of scalars (an extra hidden symmetry).      [~25%]

Every q in F_N^* is enumerated exhaustively -- no sampling, no Monte Carlo.

Output: artifacts/r82/q_curve.json  (+ the full curve arrays)
"""

import json
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from catmap_independent import CatMap  # noqa: E402
from compression_spacings import eigen_basis  # noqa: E402
from parity_desymmetrised import apply_parity  # noqa: E402

A = [[2, 1], [1, 1]]


def rep_for_each_q(N):
    """one n per nonzero value of Q, by a single pass over n_2 = 1 and the cone
    completion; falls back to a scan when a value is missed."""
    got = {}
    for n1 in range(N):
        for n2 in (1, 2, 3):
            q = (n1 * n1 - n1 * n2 - n2 * n2) % N
            if q and q not in got:
                got[q] = (n1, n2)
        if len(got) == N - 1:
            break
    if len(got) < N - 1:
        for n1 in range(N):
            for n2 in range(N):
                q = (n1 * n1 - n1 * n2 - n2 * n2) % N
                if q and q not in got:
                    got[q] = (n1, n2)
            if len(got) == N - 1:
                break
    return got


def sparsity(vals, mat):
    """fraction of the centred variance captured by the top 1, 3, 10 modes of
    the transform `mat` (rows = modes)."""
    c = vals - vals.mean()
    coef = np.abs(mat @ c) ** 2
    coef = np.sort(coef)[::-1]
    tot = coef.sum()
    if tot <= 0:
        return [0.0, 0.0, 0.0]
    return [float(coef[:k].sum() / tot) for k in (1, 3, 10)]


def design(N, batch, rng):
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
    reps = rep_for_each_q(N)
    qs = np.array(sorted(reps), dtype=np.int64)
    print(f"=== N={N} K={K} m={m} m+={mp}: {len(qs)} level sets "
          f"({time.time()-t0:.0f} s)", flush=True)

    s2 = np.empty(len(qs))
    mu4 = np.empty(len(qs))
    mu6 = np.empty(len(qs))
    for i, q in enumerate(qs):
        u = reps[int(q)]
        H = Bp.conj().T @ cm.apply_T(u, Bp)
        H = H + H.conj().T
        ev = np.linalg.eigvalsh(H)
        e = ev - ev.mean()
        v = (e ** 2).mean()
        s2[i] = v
        e = e / np.sqrt(v)
        mu4[i] = (e ** 4).mean()
        mu6[i] = (e ** 6).mean()
    print(f"  curve computed ({time.time()-t0:.0f} s):  "
          f"Tr(V^2)/m+ in [{s2.min():.5f}, {s2.max():.5f}] "
          f"(mean {s2.mean():.5f}, rel spread {s2.std()/s2.mean():.4f});  "
          f"mu_4 in [{mu4.min():.4f}, {mu4.max():.4f}] "
          f"(mean {mu4.mean():.4f}, std {mu4.std():.4f})", flush=True)

    row = {"N": N, "K": int(K), "m_plus": mp, "n_levels": int(len(qs)),
           "s2_mean": float(s2.mean()), "s2_rel_spread": float(s2.std() / s2.mean()),
           "s2_times_K2_over_N_times_mp": float(s2.mean() * K * K * mp / N),
           "mu4_mean": float(mu4.mean()), "mu4_std": float(mu4.std()),
           "mu4_min": float(mu4.min()), "mu4_max": float(mu4.max()),
           "mu6_mean": float(mu6.mean()), "mu6_std": float(mu6.std())}

    # ---- additive Fourier in q ------------------------------------------
    a = np.arange(1, N)
    Ead = np.exp(-2j * np.pi * np.outer(a, qs) / N) / np.sqrt(N - 1)
    # ---- multiplicative characters of F_N^* -----------------------------
    g = 2
    while pow(g, (N - 1) // 2, N) == 1 or any(pow(g, (N - 1) // p, N) == 1
                                              for p in (2, 3, 5, 7, 11, 13, 17, 19)
                                              if (N - 1) % p == 0):
        g += 1
    dl = np.zeros(N, dtype=np.int64)
    x = 1
    for k in range(N - 1):
        dl[x] = k
        x = x * g % N
    idx = dl[qs]
    kk = np.arange(1, N - 1)
    Emul = np.exp(-2j * np.pi * np.outer(kk, idx) / (N - 1)) / np.sqrt(N - 1)

    for name, vals in (("s2", s2), ("mu4", mu4), ("mu6", mu6)):
        sa = sparsity(vals, Ead)
        sm = sparsity(vals, Emul)
        row[f"sparsity_additive_{name}"] = sa
        row[f"sparsity_multiplicative_{name}"] = sm
        print(f"  {name}: top-1/3/10 additive Fourier mass "
              f"{sa[0]:.3f}/{sa[1]:.3f}/{sa[2]:.3f};  multiplicative "
              f"{sm[0]:.3f}/{sm[1]:.3f}/{sm[2]:.3f}", flush=True)

    # ---- P8: hidden symmetries q -> c q ---------------------------------
    pos = {int(q): i for i, q in enumerate(qs)}
    syms = []
    for c in range(2, min(N, 60)):
        if c % N == 0:
            continue
        tgt = [pos.get(int(c * q % N)) for q in qs]
        if any(t is None for t in tgt):
            continue
        d = float(np.abs(mu4[tgt] - mu4).max())
        syms.append((c, d))
    syms.sort(key=lambda z: z[1])
    row["mu4_scaling_symmetry_best"] = [[int(c), float(d)] for c, d in syms[:4]]
    print("  P8 best q -> cq symmetries of mu_4 (c, max|dev|): "
          + ", ".join(f"({c}, {d:.2e})" for c, d in syms[:4]), flush=True)
    # q -> -q is c = N-1
    if (N - 1) in [c for c, _ in syms]:
        dneg = dict(syms)[N - 1]
        row["mu4_q_to_minus_q_dev"] = float(dneg)
        print(f"  P8 q -> -q: max|dev| = {dneg:.2e}", flush=True)

    np.savez_compressed(
        os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                     "artifacts", "r82", f"q_curve_N{N}.npz"),
        q=qs, s2=s2, mu4=mu4, mu6=mu6)
    return row


def main():
    rng = np.random.default_rng(820006)
    out = {"script": "src/r82g_q_curve.py",
           "generated": time.strftime("%Y-%m-%dT%H:%M:%S"), "designs": []}
    for N, batch in ((199, 64), (3571, 512)):
        try:
            out["designs"].append(design(N, batch, rng))
        except Exception as exc:                       # noqa: BLE001
            print(f"design N={N} FAILED: {exc!r}", flush=True)
            out["designs"].append({"N": N, "error": repr(exc)})
    dest = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                        "artifacts", "r82", "q_curve.json")
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w") as fh:
        json.dump(out, fh, indent=1, default=str)
    print("artifact ->", dest, flush=True)


if __name__ == "__main__":
    main()
