r"""R108c -- independent checks of the EXACT layers: arcsine law (Thm 91.5)
and the subgroup-Kloosterman balanced second moment (Thm B, s=2).

Arcsine: build V = J/(N-1) over the FULL character group (all characters
chi_k, k = 0..N-2), J[i,j] = sum_{x != 0,1} conj(chi_i)(x) chi_j(x-1)
e_N(qx); M = V + V^*.  Verify:
  (A1) partial-isometry algebra: V V^* = I - E, V^* V = I - F with
       E = ones/m, F = alternating/m (to machine precision);
  (A2) Tr(M^{2s}) = binom(2s,s)*(N-1) - beta_s,
       beta_s = 2*sum_{j=0}^{s-1} 4^{s-1-j} Cat(j), for s = 1..6;
  (A3) q-independence for q = 1, 2, 3.

Thm B (s=2): for H of order k in F_p^*, -1 not in H:
  sum_{a,b in F_p} |S_H(a,b)|^4 = p^2 * (2k^2 - k).
"""
import json
import math
import os
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(HERE)))
OUT_DIR = os.path.join(ROOT, "data", "referee")
LOG_PATH = os.path.join(OUT_DIR, "r108c_exact_layers.log")

_t0 = time.time()


def log(msg):
    print(str(msg), flush=True)
    with open(LOG_PATH, "a", encoding="utf-8") as fh:
        fh.write(str(msg) + "\n")


def dlog_table(N, g):
    tab = np.zeros(N, dtype=np.int64)
    x = 1
    for s in range(N - 1):
        tab[x] = s
        x = x * g % N
    return tab


def prim_root(N):
    for g in range(2, N):
        if pow(g, N - 1, N) != 1:
            continue
        if all(pow(g, f, N) != 1 for f in range(2, N - 1) if (N - 1) % f == 0):
            return g
    raise RuntimeError


def catalan(j):
    return math.comb(2 * j, j) // (j + 1)


def beta_s(s):
    return 2 * sum(4 ** (s - 1 - j) * catalan(j) for j in range(s))


def build_V(N, q):
    g = prim_root(N)
    dlog = dlog_table(N, g)
    ks = np.arange(N - 1)
    xs = np.array([x for x in range(N) if x not in (0, 1)], dtype=np.int64)
    dl_x = dlog[xs]
    dl_xm1 = dlog[(xs - 1) % N]
    W = np.exp(-2j * np.pi * np.outer(ks, dl_x) / (N - 1))
    Vm = np.exp(2j * np.pi * np.outer(ks, dl_xm1) / (N - 1))
    ph = np.exp(2j * np.pi * (q * xs % N) / N)
    J = (W * ph) @ Vm.T
    return J / (N - 1)


def check_arcsine(N, qs=(1, 2, 3), smax=6):
    m = N - 1
    E = np.ones((m, m), dtype=complex) / m
    F = np.array([[(-1.0) ** (i + j) for j in range(m)] for i in range(m)],
                 dtype=complex) / m
    results = {}
    for q in qs:
        V = build_V(N, q)
        Wv = V.conj().T
        rel = lambda A, B: float(np.max(np.abs(A - B)) / max(1.0, np.max(np.abs(B))))
        a1_vv = rel(V @ Wv, np.eye(m) - E)
        a1_wv = rel(Wv @ V, np.eye(m) - F)
        M = V + Wv
        moms = []
        Mp = np.eye(m, dtype=complex)
        for s in range(1, smax + 1):
            Mp = Mp @ M @ M
            tr = complex(np.trace(Mp)).real
            pred = math.comb(2 * s, s) * m - beta_s(s)
            moms.append((s, tr, pred, abs(tr - pred) / abs(pred)))
        results[f"q{q}"] = dict(
            vv_err=a1_vv, wv_err=a1_wv,
            moments=[(s, f"{tr:.6f}", f"{pred:.6f}", f"{r:.2e}")
                     for s, tr, pred, r in moms],
        )
        log(f"N={N} q={q}: VV*-I+E rel {a1_vv:.2e}, V*V-I+F rel {a1_wv:.2e}")
        for s, tr, pred, relerr in moms:
            log(f"   s={s}: Tr(M^2s)={tr:.4f} pred={pred:.4f} rel={relerr:.2e}")
    return results


def check_thmB(p, a):
    """Subgroup Kloosterman balanced 2nd moment: sum |S_H|^4 = p^2(2k^2-k)."""
    K = 1
    x = a % p
    while x != 1:
        x = x * a % p
        K += 1
    H = np.array([pow(a, i, p) for i in range(K)], dtype=np.int64)
    assert (-1 % p) not in set(H.tolist()), "need -1 not in H for 2k^2-k"
    invH = np.array([pow(int(h), p - 2, p) for h in H], dtype=np.int64)
    S = np.zeros((p, p), dtype=complex)
    aa = np.arange(p, dtype=np.int64)
    for h, ih in zip(H, invH):
        ph = np.exp(2j * np.pi * ((aa[:, None] * h + aa[None, :] * ih) % p) / p)
        S += ph
    E22 = float(np.sum(np.abs(S) ** 4))
    pred = float(p**2 * (2 * K**2 - K))
    log(f"Thm B s=2: p={p}, k={K}: sum|S_H|^4 = {E22:.0f}, "
        f"p^2(2k^2-k) = {pred:.0f}, rel = {abs(E22 - pred) / pred:.2e}")
    return dict(p=p, k=K, E22=E22, pred=pred)


def main():
    log("R108c: exact-layer independent checks")
    out = {}
    for N in (53, 199):
        log(f"=== arcsine check N={N} ===")
        out[f"arcsine_N{N}"] = check_arcsine(N)
    log("=== Theorem B s=2 check (p=199, a=139, k=11) ===")
    out["thmB_p199"] = check_thmB(199, 139)
    with open(os.path.join(OUT_DIR, "r108c_exact_layers.json"), "w") as fh:
        json.dump(out, fh, indent=1, default=float)
    log(f"done at {time.time() - _t0:.1f}s")


if __name__ == "__main__":
    main()
