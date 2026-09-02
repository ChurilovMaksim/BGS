"""
Part 2 of the clean-room replication: the compression experiment at large N.

Computes, entirely from scratch:

  * an orthonormal basis B of the eigenspace H_lam of U_A (via the exact
    projector P_lam = (1/K) sum_j lam^{-j} U^j applied to random vectors);
  * the compressions M_O = B^* T(u) B for single Weyl frequencies u;
  * Gaussian combinations over L orbits, generic and Theta-symmetrised;
  * nearest-neighbour spacing statistics against size-matched GOE / GUE /
    Poisson controls.

RED TEAM TARGET: the project's claim T20, "one orbit (two real parameters)
already gives GOE over ~3550 spacings".
"""

from __future__ import annotations

import json
import math
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from catmap_independent import (                    # noqa: E402
    CatMap, L1_to, reference_L1, unfolded_spacings,
)

EDGES = np.linspace(0.0, 4.0, 41)


def eigen_basis(cm: CatMap, K: int, branch: int, batch: int, rng, tol=1e-8):
    """Orthonormal basis of the eigenspace of U for the `branch`-th K-th root
    of chi, obtained from the exact projector applied to random vectors."""
    N = cm.N
    e0 = np.zeros((N, 1), dtype=complex)
    e0[0, 0] = 1.0
    v = e0.copy()
    for _ in range(K):
        v = cm.apply_U(v)
    chi = v[0, 0]                                    # U^K = chi * 1
    lam = np.exp((np.log(chi + 0j) + 2j * np.pi * branch) / K)
    R = (rng.standard_normal((N, batch)) + 1j * rng.standard_normal((N, batch)))
    acc = np.zeros_like(R)
    cur = R.copy()
    for j in range(K):
        acc += (lam ** (-j)) * cur
        cur = cm.apply_U(cur)
    acc /= K
    # orthonormalise, keep numerically nonzero directions
    Q, s, _ = np.linalg.svd(acc, full_matrices=False)
    m = int((s > tol * s[0]).sum())
    B = Q[:, :m]
    # residual: U B should equal lam B
    res = np.abs(cm.apply_U(B) - lam * B).max()
    return B, lam, m, float(res), complex(chi)


def compress(cm, B, u):
    """B^* T(u) B."""
    return B.conj().T @ cm.apply_T(u, B)


def orbit_reps(cm, K, L, rng):
    """L distinct A^T-orbit representatives in (Z/N)^2 \\ {0}."""
    N = cm.N
    AT = cm.A.T % N
    seen = set()
    reps = []
    while len(reps) < L:
        u = rng.integers(0, N, size=2)
        if u[0] % N == 0 and u[1] % N == 0:
            continue
        orb = []
        w = u.copy()
        for _ in range(K):
            orb.append((int(w[0]) % N, int(w[1]) % N))
            w = AT @ w % N
        if any(o in seen for o in orb):
            continue
        seen.update(orb)
        reps.append(tuple(int(t) % N for t in u))
    return reps


def stats(ev, m, refs):
    s = unfolded_spacings(ev)
    l1 = (L1_to(s, 1, EDGES), L1_to(s, 2, EDGES), L1_to(s, 0, EDGES))
    z = {}
    for kind, (mu, sd) in refs.items():
        z[kind] = [float((l1[i] - mu[i]) / sd[i]) if sd[i] > 0 else None
                   for i in range(3)]
    return {"n_spacings": int(len(s)), "L1_GOE": l1[0], "L1_GUE": l1[1],
            "L1_Poisson": l1[2], "z_vs_controls": z}


def main():
    rng = np.random.default_rng(11235813)
    out = {"generated": time.strftime("%Y-%m-%dT%H:%M:%S"), "runs": []}

    configs = [([[2, 1], [1, 1]], 3571, 400),
               ([[2, 1], [1, 1]], 1597, 120),
               ([[5, 2], [2, 1]], 2161, 120)]

    for A, N, batch in configs:
        t0 = time.time()
        cm = CatMap(A, N)
        ordA, K = cm.orders()
        # Theta data: R = [[p,q],[r,-p]] with p(a-d)+qc+br=0, p^2+qr=1
        (a, b), (c, d) = A
        R = None
        for p_ in range(-6, 7):
            for q_ in range(-6, 7):
                for r_ in range(-6, 7):
                    if p_ * (a - d) + q_ * c + b * r_ == 0 and p_ * p_ + q_ * r_ == 1:
                        Rc = np.array([[p_, q_], [r_, -p_]], dtype=np.int64)
                        if round(np.linalg.det(Rc)) == -1:
                            M = np.array([[1, 0], [0, -1]]) @ Rc
                            if math.gcd(int(M[1, 0]) % N, N) == 1:
                                R = Rc
                                break
                if R is not None:
                    break
            if R is not None:
                break
        thetaM = None
        if R is not None:
            M = (np.array([[1, 0], [0, -1]]) @ R)
            thetaM = CatMap([[int(M[0, 0]), int(M[0, 1])],
                             [int(M[1, 0]), int(M[1, 1])]], N)

        B, lam, m, res, chi = eigen_basis(cm, K, 0, batch, rng)
        print("=" * 78)
        print(f"A={A} N={N}: ord={ordA} K={K}  m={m}  "
              f"|UB-lam B|={res:.2e}  R={None if R is None else R.tolist()}  "
              f"[{time.time()-t0:.1f}s]")
        sys.stdout.flush()

        refs = {}
        for kind in ("GOE", "GUE", "Poisson"):
            refs[kind] = reference_L1(kind, m, 12, EDGES, rng)
        print(f"   controls (L1 vs GOE, GUE, Poisson curves):")
        for kind, (mu, sd) in refs.items():
            print(f"     true {kind:>7}: {mu[0]:.4f}+-{sd[0]:.4f}  "
                  f"{mu[1]:.4f}+-{sd[1]:.4f}  {mu[2]:.4f}+-{sd[2]:.4f}")

        run = {"A": A, "N": N, "ord": ordA, "K": K, "m": m,
               "proj_residual": res,
               "controls": {k: {"mean": list(map(float, v[0])),
                                "std": list(map(float, v[1]))}
                            for k, v in refs.items()},
               "experiments": []}

        # ---- pre-compute compressions for a pool of orbits
        L_MAX = 64
        reps = orbit_reps(cm, K, L_MAX, rng)
        Ms = [compress(cm, B, u) for u in reps]
        # Theta-conjugated compressions, if available
        Ms_theta = None
        if thetaM is not None:
            UM_B = None
            # Theta X Theta^{-1} on the compression: build U_M restricted
            # W = B^* U_M conj(B)  (unitary m x m, symmetric per T4)
            W = B.conj().T @ thetaM.apply_U(np.conj(B))
            Ms_theta = [W @ np.conj(Mo) @ W.conj().T for Mo in Ms]
            sym_err = float(np.abs(W - W.T).max())
            unit_err = float(np.abs(W.conj().T @ W - np.eye(m)).max())
            wwbar = float(np.abs(W @ np.conj(W) - np.eye(m)).max())
            run["theta"] = {"W_symmetric_dev": sym_err,
                            "W_unitary_dev": unit_err,
                            "W_Wbar_eq_I_dev": wwbar}
            print(f"   Theta block W = B* U_M conj(B):  |W-W^T|={sym_err:.2e}  "
                  f"|W*W-I|={unit_err:.2e}  |W conj(W)-I|={wwbar:.2e}")

        # ---- X1: single orbit, several choices of u
        print("   X1  SINGLE ORBIT compressions (project claim T20 = GOE)")
        for t in range(6):
            Mo = Ms[t]
            H = Mo + Mo.conj().T
            ev = np.linalg.eigvalsh(H)
            st = stats(ev, m, refs)
            st["kind"] = "single_orbit_hermitian_part"
            st["u"] = list(reps[t])
            run["experiments"].append(st)
            print(f"     u={reps[t]}: L1_GOE={st['L1_GOE']:.4f} "
                  f"L1_GUE={st['L1_GUE']:.4f} L1_Poi={st['L1_Poisson']:.4f}  "
                  f"z(GOE)={st['z_vs_controls']['GOE'][0]:+.2f} "
                  f"z(GUE)={st['z_vs_controls']['GUE'][1]:+.2f} "
                  f"z(Poi)={st['z_vs_controls']['Poisson'][2]:+.2f}")
            sys.stdout.flush()

        # ---- X2 / X3: Gaussian combinations over L orbits
        print("   X2/X3  Gaussian combination over L orbits "
              "(new Thm B: generic -> GUE, Theta-symmetrised -> GOE)")
        for L in (1, 2, 4, 8, 16, 32, 64):
            g = rng.standard_normal(L) + 1j * rng.standard_normal(L)
            Hgen = np.zeros((m, m), dtype=complex)
            for i in range(L):
                Hgen += g[i] * Ms[i] + np.conj(g[i]) * Ms[i].conj().T
            evg = np.linalg.eigvalsh(Hgen)
            sg = stats(evg, m, refs)
            sg.update({"kind": "gaussian_generic", "L": L})
            run["experiments"].append(sg)
            line = (f"     L={L:>3} generic : L1_GOE={sg['L1_GOE']:.4f} "
                    f"L1_GUE={sg['L1_GUE']:.4f} "
                    f"z(GUE)={sg['z_vs_controls']['GUE'][1]:+.2f}")
            if Ms_theta is not None:
                Hsym = Hgen + (
                    lambda X: X)(None) if False else None
                Hsym = np.zeros((m, m), dtype=complex)
                for i in range(L):
                    X = g[i] * Ms[i] + np.conj(g[i]) * Ms[i].conj().T
                    Xt = g[i] * Ms_theta[i] + np.conj(g[i]) * Ms_theta[i].conj().T
                    Hsym += X + Xt
                Hsym = (Hsym + Hsym.conj().T) / 2
                evs = np.linalg.eigvalsh(Hsym)
                ss = stats(evs, m, refs)
                ss.update({"kind": "gaussian_theta_symmetrised", "L": L})
                run["experiments"].append(ss)
                line += (f"  ||  theta-sym: L1_GOE={ss['L1_GOE']:.4f} "
                         f"L1_GUE={ss['L1_GUE']:.4f} "
                         f"z(GOE)={ss['z_vs_controls']['GOE'][0]:+.2f}")
            print(line)
            sys.stdout.flush()

        out["runs"].append(run)

    dest = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                        "artifacts", "r71", "compression_spacings.json")
    with open(dest, "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=1)
    print("\nartifact ->", os.path.normpath(dest))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
