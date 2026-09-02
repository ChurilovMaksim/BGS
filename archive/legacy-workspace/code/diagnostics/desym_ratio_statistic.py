"""
Run 72, decisive measurement: the SPACING-RATIO statistic for the
parity-desymmetrised single-orbit compression.
================================================================

The nearest-neighbour L1 statistic requires unfolding, which at m ~ 100-500 is
the dominant systematic and discriminates beta = 1 from beta = 2 only weakly.
The consecutive-spacing-ratio statistic

        r~_n = min(s_n, s_{n+1}) / max(s_n, s_{n+1}),   s_n = E_{n+1} - E_n

needs NO unfolding at all, and its mean is a sharp symmetry-class label
(Atas-Bogomolny-Giraud-Roux):

        Poisson  <r~> = 0.38629
        GOE      <r~> = 0.53590
        GUE      <r~> = 0.60266
        GSE      <r~> = 0.67617

A superposition of two independent spectra lowers <r~> towards the Poisson value.
Here we measure <r~> for

    full        the whole compression P_lam (T(u)+T(u)^*) P_lam
    plus/minus  its two exact parity blocks (Theorem D)
    haar        a matched Haar-random frame of the same size (arithmetic-free)

together with size-matched empirical GOE/GUE/Poisson/superposition references,
over many frequencies u and several design points with A^k = +I (eps = +1),
where the parity symmetry is nontrivial.
"""

from __future__ import annotations

import json
import math
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from catmap_independent import CatMap                     # noqa: E402
from compression_spacings import eigen_basis, orbit_reps  # noqa: E402
from parity_desymmetrised import apply_parity, eps_of     # noqa: E402

RTILDE = {"Poisson": 0.38629, "GOE": 0.53590, "GUE": 0.60266, "GSE": 0.67617}


def r_tilde(ev):
    ev = np.sort(np.asarray(ev, dtype=float))
    s = np.diff(ev)
    s = s[s > 0]
    if len(s) < 3:
        return float("nan"), 0
    a, b = s[:-1], s[1:]
    r = np.minimum(a, b) / np.maximum(a, b)
    return float(r.mean()), int(len(r))


def ref_rtilde(kind, m, nrep, rng):
    vals = []
    for _ in range(nrep):
        if kind == "GOE":
            X = rng.standard_normal((m, m)); X = (X + X.T) / np.sqrt(2)
            ev = np.linalg.eigvalsh(X)
        elif kind == "GUE":
            X = rng.standard_normal((m, m)) + 1j * rng.standard_normal((m, m))
            X = (X + X.conj().T) / 2
            ev = np.linalg.eigvalsh(X)
        elif kind == "Poisson":
            ev = np.sort(rng.random(m))
        elif kind in ("SUP_GUE", "SUP_GOE"):
            parts = []
            for mm in (m - m // 2, m // 2):
                if kind == "SUP_GUE":
                    X = (rng.standard_normal((mm, mm))
                         + 1j * rng.standard_normal((mm, mm)))
                    X = (X + X.conj().T) / 2
                else:
                    X = rng.standard_normal((mm, mm)); X = (X + X.T) / np.sqrt(2)
                parts.append(np.linalg.eigvalsh(X) / np.sqrt(mm))
            ev = np.sort(np.concatenate(parts))
        vals.append(r_tilde(ev)[0])
    a = np.array(vals)
    return float(a.mean()), float(a.std(ddof=1))


def find_designs(A, pmax, kmax, mmin, want_eps):
    A0 = np.array(A, dtype=np.int64)
    I = np.eye(2, dtype=np.int64)
    sieve = np.ones(pmax + 1, dtype=bool)
    sieve[:2] = False
    for i in range(2, int(pmax ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i::i] = False
    out = []
    for p in np.flatnonzero(sieve):
        p = int(p)
        if p < 101 or math.gcd(int(A0[1, 0]) % p, p) != 1:
            continue
        M = A0 % p
        k = eps = None
        for j in range(1, kmax + 1):
            if np.array_equal(M % p, I):
                k, eps = j, +1
                break
            if np.array_equal(M % p, (-I) % p):
                k, eps = j, -1
                break
            M = M @ A0 % p
        if k is None or eps != want_eps:
            continue
        K = k if eps == 1 else 2 * k
        m = p // K
        if m >= mmin:
            out.append((p, k, eps, K, m))
    return out


def main():
    rng = np.random.default_rng(72727272)
    A = [[2, 1], [1, 1]]
    cands = find_designs(A, 60000, 40, 150, +1)
    cands.sort(key=lambda t: t[4])
    picked, seen = [], set()
    for p, k, eps, K, m in cands:
        b = int(math.log(m) * 1.6)
        if b in seen or m > 900:
            continue
        seen.add(b)
        picked.append((p, k, eps, K, m))
    print("eps=+1 design points (p,k,eps,K,m):", picked)
    sys.stdout.flush()

    out = {"generated": time.strftime("%Y-%m-%dT%H:%M:%S"),
           "rtilde_reference_values": RTILDE, "rows": []}
    NU = 16
    for p, k, eps, K, mpred in picked:
        t0 = time.time()
        cm = CatMap(A, p)
        ordA, KK = cm.orders()
        B, lam, m, res, chi = eigen_basis(cm, KK, 0, min(int(mpred * 1.7) + 40, 1300), rng)
        RB = B.conj().T @ apply_parity(B)
        w, Vv = np.linalg.eigh(RB)
        mp, mm_ = int((w > 0).sum()), int((w <= 0).sum())
        if min(mp, mm_) < 20:
            print(f"  p={p}: split {mp}/{mm_} too uneven, skip")
            continue
        Bp, Bm = B @ Vv[:, w > 0], B @ Vv[:, w <= 0]
        nrep = 20 if m <= 400 else 10
        refs = {"full": {kk: ref_rtilde(kk, m, nrep, rng)
                         for kk in ("GOE", "GUE", "Poisson", "SUP_GUE", "SUP_GOE")},
                "block": {kk: ref_rtilde(kk, mp, nrep, rng)
                          for kk in ("GOE", "GUE", "Poisson")}}
        reps = orbit_reps(cm, KK, NU, rng)
        vals = {kk: [] for kk in ("full", "plus", "minus", "haar")}
        for u in reps:
            H = B.conj().T @ cm.apply_T(u, B); H = H + H.conj().T
            vals["full"].append(r_tilde(np.linalg.eigvalsh(H))[0])
            Hp = Bp.conj().T @ cm.apply_T(u, Bp); Hp = Hp + Hp.conj().T
            vals["plus"].append(r_tilde(np.linalg.eigvalsh(Hp))[0])
            Hm = Bm.conj().T @ cm.apply_T(u, Bm); Hm = Hm + Hm.conj().T
            vals["minus"].append(r_tilde(np.linalg.eigvalsh(Hm))[0])
            Z = rng.standard_normal((p, mp)) + 1j * rng.standard_normal((p, mp))
            Q, _ = np.linalg.qr(Z)
            Y = Q.conj().T @ cm.apply_T(u, Q); Y = Y + Y.conj().T
            vals["haar"].append(r_tilde(np.linalg.eigvalsh(Y))[0])

        row = {"p": p, "k": k, "K": KK, "m": m, "m_plus": mp, "m_minus": mm_,
               "proj_res": res, "n_orbits": NU,
               "refs_full": {kk: list(v) for kk, v in refs["full"].items()},
               "refs_block": {kk: list(v) for kk, v in refs["block"].items()},
               "measured": {}, "secs": round(time.time() - t0, 1)}
        print("=" * 78)
        print(f"p={p} k={k} K={KK} m={m} (m+={mp}, m-={mm_})  [{row['secs']}s]")
        print(f"   refs full  : " + "  ".join(
            f"{kk}={v[0]:.4f}+-{v[1]:.4f}" for kk, v in refs["full"].items()))
        print(f"   refs block : " + "  ".join(
            f"{kk}={v[0]:.4f}+-{v[1]:.4f}" for kk, v in refs["block"].items()))
        for kk, v in vals.items():
            a = np.array([x for x in v if np.isfinite(x)])
            R = refs["full"] if kk == "full" else refs["block"]
            row["measured"][kk] = {
                "rtilde_mean": float(a.mean()),
                "rtilde_sem": float(a.std(ddof=1) / math.sqrt(len(a))),
                "z": {name: float((a.mean() - mu) / sd)
                      for name, (mu, sd) in R.items()}}
            z = row["measured"][kk]["z"]
            print(f"   {kk:<6} <r~> = {a.mean():.4f} +- "
                  f"{a.std(ddof=1)/math.sqrt(len(a)):.4f}   z: " +
                  "  ".join(f"{nm}={zz:+.2f}" for nm, zz in z.items()))
        out["rows"].append(row)
        sys.stdout.flush()

    print()
    print("SUMMARY  (arithmetic content after desymmetrisation)")
    for r in out["rows"]:
        mb = r["measured"]
        print(f"  p={r['p']:>6} m={r['m']:>4}: full <r~>={mb['full']['rtilde_mean']:.4f}"
              f" (z_SUPGUE={mb['full']['z']['SUP_GUE']:+.2f},"
              f" z_GUE={mb['full']['z']['GUE']:+.2f}) | "
              f"block <r~>={mb['plus']['rtilde_mean']:.4f}"
              f" (z_GUE={mb['plus']['z']['GUE']:+.2f},"
              f" z_GOE={mb['plus']['z']['GOE']:+.2f}) | "
              f"haar <r~>={mb['haar']['rtilde_mean']:.4f}"
              f" (z_GUE={mb['haar']['z']['GUE']:+.2f})")
    dest = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                        "artifacts", "r72", "desym_ratio_statistic.json")
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=1)
    print("artifact ->", os.path.normpath(dest))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
