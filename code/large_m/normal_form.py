"""
Run 82h: THE EQUIVARIANT NORMAL FORM, certified without building U_g.
=====================================================================
THEORY 18.4 claims that in the Hecke basis {f_j} of a parity block the family
inside one level set of Q takes the form

    <f_j| T(n) |f_k>  =  c_{jk}(q) . zeta^{(j-k) s(n)},    zeta = e^{2 pi i/m},

so that V_n = D_{s(n)} (C_q + C_q^*) D_{s(n)}^* with D_s diagonal: the entire
arithmetic content of the level set is ONE matrix C_q of exponential sums, and
the n-dependence inside the level set is a diagonal unitary conjugation.  This
is the entry point for op:local in its post-Theorem-I form (a local law for a
single matrix with arithmetic entries).

The Hecke operators U_g are not implemented in this workspace, but they are not
needed.  Two facts make the basis constructible:

  * U_A acts on the eigenspace as the SCALAR lam, so V_{A^T n} = V_n exactly
    (as matrices, not merely spectrally); a level set therefore contains
    exactly m distinct matrices V_n, one per A^T-orbit;
  * the average over the level set,  H_q = (1/m) sum_{orbits} V_n
    = (1/|T/<A>|) sum_s U_{g_s} V U_{g_s}^*, is T-invariant, hence DIAGONAL in
    the Hecke basis.

So diagonalising H_q produces the Hecke basis (up to ordering and phases),
and the normal form becomes falsifiable:

  P9  |<f_j|T(n)|f_k>| is independent of n within a level set.       [~70%]
  P10 the phase differences between two members are linear in j - k:
      arg C_n - arg C_{n'} = 2 pi (j-k) ds / m  (mod 2 pi) for one ds. [~55%]

A negative control is included: the same tests across DIFFERENT level sets,
where the moduli must NOT agree.

Output: artifacts/r82/normal_form.json
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


def Qform(a, b, N):
    return (a * a - a * b - b * b) % N


def design(N, batch, rng, q_list=(1, 2, 3)):
    t0 = time.time()
    cm = CatMap(A, N)
    ordA, K = cm.orders()
    assert ordA == K
    B, lam, m, res, chi = eigen_basis(cm, K, 0, batch, rng)
    assert res < 1e-9 and m in ((N - 1) // K, (N + 1) // K)
    RB = B.conj().T @ apply_parity(B)
    w, Vv = np.linalg.eigh(RB)
    mp = int((w > 0).sum())
    Bp = B @ Vv[:, w > 0]
    AT = np.array(A, dtype=np.int64).T % N
    print(f"=== N={N} K={K} m={m} m+={mp} ({time.time()-t0:.0f} s)", flush=True)

    def orbit_reps_of_level(q):
        seen, reps = set(), []
        for a in range(N):
            for b in range(N):
                if (a, b) == (0, 0) or Qform(a, b, N) != q:
                    continue
                if (a, b) in seen:
                    continue
                x = np.array([a, b], dtype=np.int64)
                for _ in range(K):
                    seen.add((int(x[0]), int(x[1])))
                    x = AT @ x % N
                reps.append((a, b))
        return reps

    def comp(u):
        return Bp.conj().T @ cm.apply_T((int(u[0]) % N, int(u[1]) % N), Bp)

    row = {"N": N, "K": int(K), "m": int(m), "m_plus": mp, "levels": []}
    basis = {}
    for q in q_list:
        reps = orbit_reps_of_level(q)
        # V_{A^T n} = V_n exactly: check it on the first rep
        C0 = comp(reps[0])
        C0b = comp(tuple(int(t) for t in (AT @ np.array(reps[0]) % N)))
        orbit_exact = float(np.abs(C0 - C0b).max())

        H = np.zeros((mp, mp), dtype=complex)
        for u in reps:
            C = comp(u)
            H += C + C.conj().T
        H /= len(reps)
        H = (H + H.conj().T) / 2
        ev, F = np.linalg.eigh(H)
        gap = float(np.min(np.diff(np.sort(ev))))
        basis[q] = F

        # P9: are the moduli |<f_j|T(n)|f_k>| n-independent inside the level?
        mods = []
        for u in reps[:8]:
            Cn = F.conj().T @ comp(u) @ F
            mods.append(np.abs(Cn))
        mods = np.array(mods)
        scale = float(mods[0].max())
        dev = float(np.abs(mods - mods[0]).max())
        rel = dev / scale if scale > 0 else np.inf

        # P10: phase differences linear in j - k?
        C1 = F.conj().T @ comp(reps[0]) @ F
        C2 = F.conj().T @ comp(reps[1]) @ F
        big = np.abs(C1) > 0.25 * scale
        jj, kk = np.meshgrid(np.arange(mp), np.arange(mp), indexing="ij")
        dphi = np.angle(C2 / np.where(np.abs(C1) > 0, C1, 1))
        lin_r2 = np.nan
        if big.sum() > 20:
            x = (jj - kk)[big].astype(float)
            y = np.unwrap(dphi[big])
            Xd = np.column_stack([np.ones_like(x), x])
            c, *_ = np.linalg.lstsq(Xd, y, rcond=None)
            lin_r2 = float(1 - ((y - Xd @ c) ** 2).sum() /
                           max(1e-30, ((y - y.mean()) ** 2).sum()))

        print(f"  q={q}: {len(reps)} orbits;  V_(A^T n) = V_n to "
              f"{orbit_exact:.2e};  H_q spectral gap {gap:.2e}", flush=True)
        print(f"        P9 modulus deviation across 8 members: {dev:.3e} "
              f"(relative {rel:.3e}, scale {scale:.3e})", flush=True)
        print(f"        P10 linear-in-(j-k) fit of the phase difference: "
              f"R^2 = {lin_r2:.4f}", flush=True)
        row["levels"].append({"q": q, "n_orbits": len(reps),
                              "orbit_exactness": orbit_exact,
                              "H_gap": gap, "P9_abs_dev": dev,
                              "P9_rel_dev": rel, "P10_linear_R2": lin_r2})

    # negative control: moduli across DIFFERENT level sets in a common basis
    if len(q_list) >= 2:
        qa, qb = q_list[0], q_list[1]
        Fa = basis[qa]
        ra = orbit_reps_of_level(qa)[0]
        rb = orbit_reps_of_level(qb)[0]
        Ma = np.abs(Fa.conj().T @ comp(ra) @ Fa)
        Mb = np.abs(Fa.conj().T @ comp(rb) @ Fa)
        ctrl = float(np.abs(Ma - Mb).max() / Ma.max())
        row["control_cross_level_rel_dev"] = ctrl
        print(f"  NEGATIVE CONTROL (different level sets, same basis): "
              f"relative modulus deviation {ctrl:.3e}", flush=True)
    return row


def main():
    rng = np.random.default_rng(820009)
    out = {"script": "src/r82h_normal_form.py",
           "generated": time.strftime("%Y-%m-%dT%H:%M:%S"), "designs": []}
    for N, batch in ((199, 64), (3571, 512)):
        try:
            out["designs"].append(design(N, batch, rng))
        except Exception as exc:                       # noqa: BLE001
            print(f"design N={N} FAILED: {exc!r}", flush=True)
            out["designs"].append({"N": N, "error": repr(exc)})
    dest = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                        "artifacts", "r82", "normal_form.json")
    with open(dest, "w") as fh:
        json.dump(out, fh, indent=1, default=str)
    print("artifact ->", dest, flush=True)


if __name__ == "__main__":
    main()
