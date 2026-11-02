"""Wave 25, task 5 (part 2): component-lift global split fibers at
m=16 and m=20 — C(y) separation and Sigma y_i w_i constancy.

For each prime power q || D_m, enumerate component Fix points,
find component split fibers, lift each with fixed supported points
elsewhere (CRT), and test on the resulting global split fibers:
  (a) C(y) distinct across global orbits?
  (b) S(y) = sum y_i w_i (w = Hy/D, exact) constant across global
      orbits? (Equivalently A(y) = sum y_i y_{i+1}, by the identity
      D*S = 6*sum y_i^2 - 2*A with sum y_i^2 fiber-constant.)
  (c) support pattern (FULL/PARTIAL/EMPTY) of the lifted fiber.
All S/A/C values computed in Python ints on canon representatives
(S, A, C are dihedral-invariant: S = <y,Hy>/D with H equivariant;
A and C are cyclic sums with symmetric kernels).
Usage: python3 wave25_lifts.py 16|20
Repository untouched; no Lean build.
"""
import json
import sys

import numpy as np
import sympy as sp

sys.path.insert(0, ".")
from wave16_d1a_targeted import (Dm, snf_kernel, torsion_data,
                                 comp_supported, global_supported,
                                 gamma_perms, lex_canon, group_ids,
                                 crt_combine)


def Hvec_py(y, D):
    mm = len(y)
    w = []
    for i in range(mm):
        v = 6 * y[i] - y[(i - 1) % mm] - y[(i + 1) % mm]
        assert v % D == 0, f"Hy not divisible by D: {v} % {D}"
        w.append(v // D)
    return w


def stats_py(y, D):
    mm = len(y)
    w = Hvec_py(y, D)
    S = sum(y[i] * w[i] for i in range(mm))
    A = sum(y[i] * y[(i + 1) % mm] for i in range(mm))
    C = sum(y[i] * y[(i + 1) % mm] * abs(y[i] - y[(i + 1) % mm])
            for i in range(mm))
    return S, A, C, w


def main():
    m = int(sys.argv[1])
    D = Dm(m)
    fac = sp.factorint(D)
    qs = [p ** e for p, e in fac.items()]
    print(f"== m={m} D={D} prime powers={qs}", flush=True)
    Z, Qmod = torsion_data(m, D)
    perms = gamma_perms(m)

    comp = {}
    for q in qs:
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
        comp[q] = {"pts": pts, "fib": fib, "gam": gam,
                   "split": split_fibs, "sup": sup}
        print(f"  q={q}: pts={q} fibers={n_fib} split={len(split_fibs)} "
              f"comp_supp={int(sup.sum())}", flush=True)

    fixed = {}
    for q in qs:
        sup = comp[q]["sup"]
        fixed[q] = comp[q]["pts"][np.where(sup)[0][0]] if sup.any() \
            else comp[q]["pts"][0]
        print(f"  fixed supported point q={q}: supported={bool(sup.any())}",
              flush=True)

    results = []
    for q in qs:
        pts, fib = comp[q]["pts"], comp[q]["fib"]
        for f in comp[q]["split"]:
            idx = np.where(fib == f)[0]
            lifts = {}
            for qq in qs:
                lifts[qq] = pts[idx] if qq == q else np.tile(
                    fixed[qq], (len(idx), 1))
            glob = crt_combine(m, D, qs, lifts)
            gfib = group_ids(np.sort(glob, axis=1))
            assert len(set(gfib.tolist())) == 1, "lift broke the fiber!"
            gcan = lex_canon(glob, perms)
            ggam = group_ids(gcan)
            gsup = global_supported(glob, Z, Qmod, D)
            n_sup = int(gsup.sum())
            pat = ("FULL" if n_sup == len(idx) else
                   "PARTIAL" if n_sup > 0 else "EMPTY")
            orbits = sorted(set(ggam.tolist()))
            per_orbit = []
            for g in orbits:
                j = np.where(ggam == g)[0][0]
                rep = [int(v) for v in gcan[j]]
                S, A, C, w = stats_py(rep, D)
                per_orbit.append({"orbit": int(g),
                                  "size": int((ggam == g).sum()),
                                  "n_supp": int(gsup[ggam == g].sum()),
                                  "S": S, "A": A, "C": C,
                                  "sorted_w": sorted(w)})
            c_ok = len({o["C"] for o in per_orbit}) == len(per_orbit)
            s_const = len({o["S"] for o in per_orbit}) == 1
            a_const = len({o["A"] for o in per_orbit}) == 1
            sw_const = len({tuple(o["sorted_w"]) for o in per_orbit}) == 1
            rec = {"m": m, "q": q, "fiber": int(f), "size": int(len(idx)),
                   "n_orbits": len(orbits), "pattern": pat,
                   "n_supp": n_sup, "C_separates": bool(c_ok),
                   "S_constant": bool(s_const), "A_constant": bool(a_const),
                   "sorted_w_same": bool(sw_const),
                   "per_orbit": per_orbit}
            results.append(rec)
            print(f"  LIFT q={q} fiber={f} size={len(idx)} "
                  f"orbits={len(orbits)} supp={n_sup}->{pat} "
                  f"C_ok={c_ok} S_const={s_const} A_const={a_const} "
                  f"w_same={sw_const}", flush=True)

    n_lift = len(results)
    n_c_fail = sum(1 for r in results if not r["C_separates"])
    n_s_var = sum(1 for r in results if not r["S_constant"])
    n_on_sup = sum(1 for r in results if r["pattern"] != "EMPTY")
    print(f"SUMMARY m={m}: lifts={n_lift} C_failures={n_c_fail} "
          f"S_varying={n_s_var} meeting_support={n_on_sup}", flush=True)
    with open(f"/home/hatch/workspace/bgs-breakthrough/methods/"
              f"wave25_lifts_m{m}.json", "w") as fh:
        json.dump({"m": m, "D": int(D), "lifts": results,
                   "summary": {"n_lifts": n_lift, "C_failures": n_c_fail,
                               "S_varying": n_s_var,
                               "meeting_support": n_on_sup}}, fh, indent=1)
    print(f"wrote wave25_lifts_m{m}.json", flush=True)


if __name__ == "__main__":
    main()
