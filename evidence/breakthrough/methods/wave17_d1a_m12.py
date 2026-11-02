"""Wave 17, task 1: D1a consequences at m=12.

1. Bsym_Gamma(supp) at m=12, EXACT, via component-stabilizer aggregation:
   global Gamma-orbit size of y = 24 / |intersection of component
   stabilizers| (CRT), global support = AND of component supports.
2. (fiber,w)-class check on the wave-16 split fiber (36 pts, 3 orbits):
   sorted(w) per orbit -- distinct means classes = orbits on this fiber.
3. s-dependence of the coherent-sum cancellation on that fiber
   (CRT phihat, correction modes from wave 16: raw at 128/81/49,
   u^-2-corrected at 25/121).
Repository untouched; no Lean build.
"""
import sys
from fractions import Fraction

import numpy as np

sys.path.insert(0, ".")
from wave16_d1a_targeted import (Dm, snf_kernel, torsion_data,
                                 comp_supported, global_supported,
                                 gamma_perms, lex_canon, group_ids,
                                 crt_combine)

m = 12
D = Dm(m)
QS = [128, 81, 25, 49, 121]
assert D == 128 * 81 * 25 * 49 * 121
Z, Qmod = torsion_data(m, D)
perms = gamma_perms(m)
assert len(perms) == 24
print(f"m={m} D={D} |V4|={len(Z)}", flush=True)


def H_np(v):
    return 6 * v - np.roll(v, 1, axis=1) - np.roll(v, -1, axis=1)


# ---------- 1. exact Bsym_Gamma(supp) ----------
comp_stat = {}
for q in QS:
    pts = snf_kernel(m, q)
    assert len(pts) == q
    sup = comp_supported(pts, Z, Qmod, q)
    # stabilizer bitmask over the 24 dihedral perms
    stab = np.zeros(len(pts), dtype=np.int64)
    for pi, p in enumerate(perms):
        stab |= ((pts[:, p] == pts).all(axis=1).astype(np.int64) << pi)
    sup_pts = pts[sup]
    sup_stab = stab[sup]
    # aggregate: bitmask -> count among supported points
    agg = {}
    for s_ in sup_stab.tolist():
        agg[s_] = agg.get(s_, 0) + 1
    comp_stat[q] = agg
    print(f"q={q}: supported={int(sup.sum())}/{q}, distinct supported "
          f"stabilizers={len(agg)}", flush=True)

n_supp = 1
for q in QS:
    n_supp *= sum(comp_stat[q].values())
print(f"|supp| = {n_supp}  (D/16 = {D // 16}, match: {n_supp == D // 16})",
      flush=True)

# intersect stabilizers across components, accumulating weights
inter = { (1 << 24) - 1: 1 }  # full group mask -> weight 1 (placeholder)
inter = {}
for q in QS:
    new = {}
    if not inter:
        for s_, c in comp_stat[q].items():
            new[s_] = new.get(s_, 0) + c
    else:
        for m1, w1 in inter.items():
            for s_, c in comp_stat[q].items():
                mm = m1 & s_
                new[mm] = new.get(mm, 0) + w1 * c
    inter = new
    print(f"  after q={q}: {len(inter)} distinct intersections", flush=True)

sum_orbit_size = 0  # sum over supported y of |Gamma y|
for mask, w in inter.items():
    assert w > 0
    sum_orbit_size += w * (24 // bin(mask).count("1"))
bsym_gamma = Fraction(sum_orbit_size, n_supp)
print(f"sum_{{y in supp}} |Gamma y| = {sum_orbit_size}", flush=True)
print(f"Bsym_Gamma(supp) = {bsym_gamma} = {float(bsym_gamma):.12f}",
      flush=True)

# ---------- 2. wave-16 fiber: (fiber,w)-classes ----------
comp = {}
for q in QS:
    K = snf_kernel(m, q)
    comp[q] = K
fixed = {}
for q in QS:
    sup = comp_supported(comp[q], Z, Qmod, q)
    fixed[q] = comp[q][np.where(sup)[0][0]]
    print(f"fixed q={q}: first supported point, stabilizer size="
          f"{int(sum(1 for p in perms if (fixed[q][p] == fixed[q]).all()))}",
          flush=True)
c81 = comp[81]
fib81 = group_ids(np.sort(c81, axis=1))
canon81 = lex_canon(c81, perms)
gam81 = group_ids(canon81)
gf = np.empty(int(gam81.max()) + 1, dtype=np.int64)
gf[gam81] = fib81
opf = np.bincount(gf, minlength=int(fib81.max()) + 1)
split81 = np.where(opf > 1)[0]
assert len(split81) == 1
idx = np.where(fib81 == int(split81[0]))[0]
lifts = {q: (comp[q][idx] if q == 81 else np.tile(fixed[q], (len(idx), 1)))
         for q in QS}
glob = crt_combine(m, D, QS, lifts)
assert len(set(group_ids(np.sort(glob, axis=1)).tolist())) == 1
gcan = lex_canon(glob, perms)
ggam = group_ids(gcan)
gsup = global_supported(glob, Z, Qmod, D)
assert int(gsup.sum()) == len(glob)
wglob = H_np(glob) // D
print(f"wave16 fiber: size={len(glob)} orbits="
      f"{sorted(int((ggam == g).sum()) for g in set(ggam.tolist()))} "
      f"supp={int(gsup.sum())}", flush=True)
sw = {}
for g in sorted(set(ggam.tolist())):
    oo = ggam == g
    svals = set(tuple(sorted(row.tolist())) for row in wglob[oo])
    sw[g] = svals
    print(f"  orbit {g}: size={int(oo.sum())} distinct sorted(w)="
          f"{len(svals)}", flush=True)
all_sw = [next(iter(v)) for v in sw.values()]
print(f"  sorted(w) pairwise distinct across orbits: "
      f"{len(set(all_sw)) == len(all_sw)} "
      f"-> (fiber,w)-classes = orbits on this fiber: "
      f"{len(set(all_sw)) == len(all_sw)}", flush=True)
print(f"  fiber contributions: Bsym_Gamma numerator 3*12^2=432; "
      f"Bsym_fiber numerator 36^2=1296", flush=True)

# ---------- 3. s-dependence of cancellation (CRT phihat) ----------
import sympy as sp
Hsp = sp.zeros(m)
for i in range(m):
    Hsp[i, i] = 6
    Hsp[i, (i - 1) % m] -= 1
    Hsp[i, (i + 1) % m] -= 1
X = np.array(Hsp.adjugate().tolist(), dtype=np.int64)


def pairnum(A, B):
    return (A @ X) @ B.T


def qnum(A):
    return np.einsum("ij,ij->i", A @ X, A)


corr = {128: False, 81: False, 25: True, 49: False, 121: True}
compQ, compP, lookup = {}, {}, {}
for q in QS:
    K = comp[q]
    W = H_np(K) // q
    compQ[q] = qnum(W) % q
    compP[q] = pairnum(W, W) % q
    lookup[q] = {tuple(row): i for i, row in enumerate(K)}


def phihat(s, target):
    ph = np.ones(len(target), dtype=np.complex128)
    for q in QS:
        ci = pow(D // q, -1, q)
        u = (D // q) % q
        inv_u2 = pow((u * u) % q, -1, q)
        T = (2 * s * compQ[q][:, None] - compP[q]) % q
        if corr[q]:
            T = (inv_u2 * T) % q
        E = np.exp(2j * np.pi * ((ci * T) % q) / q)
        Sj = E.sum(axis=0)
        idx = np.array([lookup[q][tuple(row)] for row in (target % q)])
        ph *= Sj[idx]
    return ph / D


print("s-dependence of fiber coherent sum (s coprime to D):", flush=True)
for s in (1, 13, 17, 19, 23, 29, 31, 37):
    phi = phihat(s, glob)
    mod2 = float((phi * np.conj(phi)).real.sum())
    coh = float(abs(phi.sum()) ** 2)
    print(f"  s={s}: |sum phi|^2 = {coh:.3e}  (fiber-constant prediction "
          f"36^2*16/D = {36**2 * 16.0 / D:.3e}; incoherent sum = {mod2:.3e})",
          flush=True)
print("DONE", flush=True)
