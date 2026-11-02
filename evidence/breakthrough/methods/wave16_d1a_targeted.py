"""Wave 16, task 3: targeted search for a SPLIT fiber meeting support at m>=11.

Strategy (no full enumeration): CRT component lifts.
  - D_m factored into prime powers q_j.
  - For each q_j small enough, enumerate component Fix points mod q_j
    (SNF kernel of M^m - I, size q_j), group into component fibers
    (sorted multiset) and component Gamma-orbits (dihedral canon).
    A component SPLIT fiber lifts (other components fixed) to a global
    split fiber: the lift map c -> K*c mod D is injective on values,
    and a global dihedral identification would reduce mod q_j.
  - Support factorizes over CRT exactly: y in supp (global torsion
    criterion, s=1) iff every component is component-supported, where
    component support at q_j uses Q(z) mod q_j = ((D*(z.v))//4) % q_j
    (validated against the adjugate at m=8,12) and dot z.c mod q_j.
  - For each component split fiber, lifts are built with every other
    component fixed to a supported point (enumerated, else sampled),
    and the global fiber's support pattern (full/empty/partial) and
    global orbits are computed directly.
  - Separately, a bounded gluing search at m=12 pairs bad component
    fibers at q=128 and q=25 with relative dihedral shifts.

Definitions: fiber = same sorted multiset; Gamma-orbit = dihedral
action on positions (shifts + reflections); split = >1 orbit in a
fiber; partial = 0 < #(fiber cap supp) < |fiber|.
Repository untouched; no Lean build.
"""
import json
import math
import sys

import numpy as np
import sympy as sp
from sympy.matrices.normalforms import smith_normal_decomp

ENUM_CAP = 2_000_000


def Dm(m):
    s0, s1 = 2, 6
    if m == 1:
        return 4
    for _ in range(2, m + 1):
        s0, s1 = s1, 6 * s1 - s0
    return s1 - 2


def snf_kernel(m, q):
    """Seeds (seq0, seq1) of Fix sequences mod q via SNF of M^m - I."""
    M = sp.Matrix([[6, -1], [1, 0]])
    A = M**m - sp.eye(2)
    S, U, V = smith_normal_decomp(A, domain=sp.ZZ)
    assert U * A * V == S
    d1, d2 = abs(int(S[0, 0])), abs(int(S[1, 1]))
    g1, g2 = math.gcd(d1, q), math.gcd(d2, q)
    assert g1 * g2 == q, (m, q, d1, d2, g1, g2)
    y0s = np.arange(0, q, q // g1, dtype=np.int64)
    y1s = np.arange(0, q, q // g2, dtype=np.int64)
    Y0, Y1 = np.meshgrid(y0s, y1s, indexing="ij")
    y0, y1 = Y0.ravel(), Y1.ravel()
    Vn = np.array(V.tolist(), dtype=np.int64) % q
    k0 = (Vn[0, 0] * y0 + Vn[0, 1] * y1) % q
    k1 = (Vn[1, 0] * y0 + Vn[1, 1] * y1) % q
    seqs = np.empty((len(k0), m), dtype=np.int64)
    seqs[:, 0] = k1
    if m >= 2:
        seqs[:, 1] = k0
        for i in range(1, m - 1):
            seqs[:, i + 1] = (6 * seqs[:, i] - seqs[:, i - 1]) % q
    Hy = (6 * seqs - np.roll(seqs, 1, axis=1)
          - np.roll(seqs, -1, axis=1)) % q
    assert np.all(Hy == 0), "Hy != 0 mod q"
    return seqs


def sample_kernel_points(m, q, n, rng):
    """Sample Fix points mod q (for huge q): random SNF coordinates."""
    M = sp.Matrix([[6, -1], [1, 0]])
    A = M**m - sp.eye(2)
    S, U, V = smith_normal_decomp(A, domain=sp.ZZ)
    d1, d2 = abs(int(S[0, 0])), abs(int(S[1, 1]))
    g1, g2 = math.gcd(d1, q), math.gcd(d2, q)
    Vn = np.array(V.tolist(), dtype=np.int64) % q
    y0 = rng.integers(0, g1, size=n) * (q // g1)
    y1 = rng.integers(0, g2, size=n) * (q // g2)
    k0 = (Vn[0, 0] * y0 + Vn[0, 1] * y1) % q
    k1 = (Vn[1, 0] * y0 + Vn[1, 1] * y1) % q
    seqs = np.empty((n, m), dtype=np.int64)
    seqs[:, 0] = k1
    if m >= 2:
        seqs[:, 1] = k0
        for i in range(1, m - 1):
            seqs[:, i + 1] = (6 * seqs[:, i] - seqs[:, i - 1]) % q
    return seqs


def torsion_data(m, D):
    vs = []
    for a in range(4):
        for b in range(4):
            seq = [a, b]
            for _ in range(m):
                seq.append((2 * seq[-1] - seq[-2]) % 4)
            if seq[m] == a and seq[m + 1] == b:
                vs.append(seq[:m])
    Z, Qmod = [], []
    for v in vs:
        hv = [6 * v[i] - v[(i - 1) % m] - v[(i + 1) % m] for i in range(m)]
        assert all(x % 4 == 0 for x in hv)
        z = [x // 4 for x in hv]
        Z.append(z)
        num = D * sum(zi * vi for zi, vi in zip(z, v))
        assert num % 4 == 0
        Qmod.append(num // 4)  # exact integer Qnum(z); reduce mod D/q below
    return np.array(Z, dtype=np.int64), Qmod


def comp_supported(pts, Z, Qmod, q):
    """Boolean mask: component support at modulus q."""
    Qm = np.array([qq % q for qq in Qmod], dtype=np.int64)
    dot = pts @ Z.T  # int64: |dot| <= m*q*6, fits for q <= ~1e15
    return ((2 * Qm[None, :] - dot) % q == 0).all(axis=1)


def global_supported(pts, Z, Qmod, D):
    Qm = np.array([qq % D for qq in Qmod], dtype=np.int64)
    dot = pts @ Z.T
    return ((2 * Qm[None, :] - dot) % D == 0).all(axis=1)


def gamma_perms(m):
    perms, seen = [], set()
    for k in range(m):
        for p in (tuple((j + k) % m for j in range(m)),
                  tuple((k - j) % m for j in range(m))):
            if p not in seen:
                seen.add(p)
                perms.append(p)
    return np.array(perms, dtype=np.int64)


def lex_canon(arr, perms, chunk=10000):
    out = np.empty_like(arr)
    for st in range(0, len(arr), chunk):
        ch = arr[st:st + chunk]
        permuted = np.stack([ch[:, p] for p in perms], axis=1)
        mask = np.ones((len(ch), len(perms)), dtype=bool)
        for cc in range(arr.shape[1]):
            vals = np.where(mask, permuted[:, :, cc],
                            np.iinfo(arr.dtype).max)
            mask &= (permuted[:, :, cc] == vals.min(axis=1, keepdims=True))
        chosen = mask.argmax(axis=1)
        out[st:st + chunk] = permuted[np.arange(len(ch)), chosen]
    return out


def group_ids(keys):
    _, ids = np.unique(keys, axis=0, return_inverse=True)
    return np.asarray(ids).reshape(-1)


def component_analysis(m):
    D = Dm(m)
    fac = sp.factorint(D)
    qs = [p**e for p, e in fac.items()]
    Z, Qmod = torsion_data(m, D)
    perms = gamma_perms(m)
    print(f"== m={m} D={D} prime powers={qs} |V4|={len(Z)}", flush=True)
    comp = {}
    for q in qs:
        if q > ENUM_CAP:
            print(f"   q={q}: TOO LARGE to enumerate; sampled later if needed",
                  flush=True)
            comp[q] = {"points": None}
            continue
        pts = snf_kernel(m, q)
        assert len(pts) == q
        fib = group_ids(np.sort(pts, axis=1))
        canon = lex_canon(pts, perms)
        gam = group_ids(canon)
        n_fib = int(fib.max()) + 1
        gam_fiber = np.empty(int(gam.max()) + 1, dtype=np.int64)
        gam_fiber[gam] = fib
        opf = np.bincount(gam_fiber, minlength=n_fib)
        split_fibs = np.where(opf > 1)[0]
        sup = comp_supported(pts, Z, Qmod, q)
        n_sup = int(sup.sum())
        # support pattern inside component split fibers
        split_pat = {}
        for f in split_fibs[:500]:
            idx = np.where(fib == f)[0]
            split_pat[int(f)] = {"size": int(len(idx)),
                                 "n_orbits": int(len(set(gam[idx].tolist()))),
                                 "n_supp": int(sup[idx].sum())}
        comp[q] = {"points": pts, "fib": fib, "gam": gam,
                   "split_fibs": split_fibs, "sup": sup}
        print(f"   q={q}: pts={len(pts)} fibers={n_fib} "
              f"split_fibers={len(split_fibs)} comp_supp={n_sup} "
              f"(split supp patterns: "
              + ", ".join(f"{v['size']}:{v['n_orbits']}o:{v['n_supp']}s"
                          for v in list(split_pat.values())[:12])
              + (", ..." if len(split_pat) > 12 else "") + ")",
              flush=True)
    return D, qs, Z, Qmod, perms, comp


def crt_combine(m, D, qs, comp_points):
    """comp_points: dict q -> (n, m) array (same n). Returns (n, m) global."""
    n = len(next(iter(comp_points.values())))
    out = np.zeros((n, m), dtype=np.int64)
    for q, pts in comp_points.items():
        dq = D // q
        K = (dq * pow(dq % q, -1, q)) % D
        out = (out + K * pts) % D
    return out


def lift_split_fibers(m, D, qs, Z, Qmod, perms, comp, rng):
    """For each component split fiber, lift with other components fixed
    to a supported point; report global support pattern + orbits."""
    results = []
    # fixed supported point per component (enumerated or sampled)
    fixed = {}
    for q in qs:
        if comp[q]["points"] is not None:
            sup = comp[q]["sup"]
            if sup.any():
                fixed[q] = comp[q]["points"][np.where(sup)[0][0]]
            else:
                fixed[q] = comp[q]["points"][0]
                print(f"   !! q={q}: NO supported component point; "
                      f"lifts will be off-support", flush=True)
        else:
            samp = sample_kernel_points(m, q, 4000, rng)
            sup = comp_supported(samp, Z, Qmod, q)
            if sup.any():
                fixed[q] = samp[np.where(sup)[0][0]]
            else:
                fixed[q] = samp[0]
                print(f"   !! q={q}: no supported point in 4000 samples",
                      flush=True)
    for q in qs:
        if comp[q]["points"] is None:
            continue
        pts, fib, gam = comp[q]["points"], comp[q]["fib"], comp[q]["gam"]
        for f in comp[q]["split_fibs"]:
            idx = np.where(fib == f)[0]
            lifts = {}
            for qq in qs:
                if qq == q:
                    lifts[qq] = pts[idx]
                else:
                    lifts[qq] = np.tile(fixed[qq], (len(idx), 1))
            glob = crt_combine(m, D, qs, lifts)
            gfib = group_ids(np.sort(glob, axis=1))
            assert len(set(gfib.tolist())) == 1, "lift broke the fiber!"
            gcan = lex_canon(glob, perms)
            ggam = group_ids(gcan)
            gsup = global_supported(glob, Z, Qmod, D)
            # per-orbit support
            per_orbit = {}
            for g in sorted(set(ggam.tolist())):
                oo = ggam == g
                per_orbit[int(g)] = {"size": int(oo.sum()),
                                     "n_supp": int(gsup[oo].sum())}
            n_sup = int(gsup.sum())
            pat = ("FULL" if n_sup == len(idx) else
                   "PARTIAL" if n_sup > 0 else "EMPTY")
            rec = {"m": m, "q": q, "fiber": int(f), "size": int(len(idx)),
                   "n_global_orbits": int(len(per_orbit)),
                   "n_supp": n_sup, "pattern": pat,
                   "per_orbit": per_orbit}
            results.append(rec)
            print(f"   LIFT m={m} q={q} fiber={f} size={len(idx)} "
                  f"orbits={len(per_orbit)} supp={n_sup} -> {pat}",
                  flush=True)
            if pat == "PARTIAL":
                print("   PARTIAL DETAIL: " + json.dumps(rec), flush=True)
    return results


def validate_factorization(m=12):
    """Global support == AND of component supports, on random lifts."""
    D = Dm(m)
    fac = sp.factorint(D)
    qs = [p**e for p, e in fac.items()]
    Z, Qmod = torsion_data(m, D)
    rng = np.random.default_rng(7)
    comp_pts = {}
    for q in qs:
        pts = snf_kernel(m, q)
        sel = rng.integers(0, len(pts), size=300)
        comp_pts[q] = pts[sel]
    glob = crt_combine(m, D, qs, comp_pts)
    gs = global_supported(glob, Z, Qmod, D)
    ok = True
    for q in qs:
        cs = comp_supported(comp_pts[q], Z, Qmod, q)
        # AND over components must equal global
        if "and" not in dir():
            pass
    anded = np.ones(len(glob), dtype=bool)
    for q in qs:
        anded &= comp_supported(comp_pts[q], Z, Qmod, q)
    ok = bool(np.all(anded == gs))
    print(f"VALIDATION m={m}: factorization global==AND(components): {ok} "
          f"(global supp {int(gs.sum())}/300)", flush=True)
    assert ok


if __name__ == "__main__":
    validate_factorization(12)
    lo, hi = int(sys.argv[1]), int(sys.argv[2])
    rng = np.random.default_rng(3)
    all_results = []
    for m in range(lo, hi + 1):
        D, qs, Z, Qmod, perms, comp = component_analysis(m)
        res = lift_split_fibers(m, D, qs, Z, Qmod, perms, comp, rng)
        all_results.extend(res)
        # free big arrays
        for q in qs:
            comp[q]["points"] = None
    with open("/tmp/wave16_targeted.json", "w") as fh:
        json.dump(all_results, fh, indent=1)
    n_partial = sum(1 for r in all_results if r["pattern"] == "PARTIAL")
    n_full = sum(1 for r in all_results if r["pattern"] == "FULL")
    print(f"SUMMARY: lifted split fibers={len(all_results)} "
          f"FULL={n_full} PARTIAL={n_partial}", flush=True)
