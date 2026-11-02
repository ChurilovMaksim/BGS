"""Wave 16, task 3 (follow-up): phihat values on the m=12 split fiber
that lifts to FULL support, via CRT factorisation (wave 14 method).

m=12, D=1536796800 = 128*81*25*49*121. The q=81 component split fiber
(36 points, 3 component orbits) lifts, with other components fixed to
supported points, to a global fiber of 36 points, 3 Gamma-orbits,
36/36 in support (wave16_d1a_targeted.py). Here phihat_s is computed
for those 36 points by CRT factorisation over the 5 components, with
the raw-vs-u^{-2}-corrected mode per component decided by direct test
against global exponents from the 12x12 adjugate (as in wave 14).
s=1 primary; s=13 (also coprime to D) as a check.
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

m = 12
D = Dm(m)
QS = [128, 81, 25, 49, 121]
assert D == 128 * 81 * 25 * 49 * 121
Z, Qmod = torsion_data(m, D)
perms = gamma_perms(m)

# --- adjugate of H_12 (exact) ---
Hsp = sp.zeros(m)
for i in range(m):
    Hsp[i, i] = 6
    Hsp[i, (i - 1) % m] -= 1
    Hsp[i, (i + 1) % m] -= 1
X = np.array(Hsp.adjugate().tolist(), dtype=np.int64)
print("X max abs:", int(np.abs(X).max()), "det==D:", int(Hsp.det()) == D,
      flush=True)


def H_np(v):
    return 6 * v - np.roll(v, 1, axis=1) - np.roll(v, -1, axis=1)


def pairnum(A, B):
    return (A @ X) @ B.T


def qnum(A):
    return np.einsum("ij,ij->i", A @ X, A)


# --- component kernels, W vectors, Q/P ---
comp = []
for q in QS:
    K = snf_kernel(m, q)
    assert len(K) == q
    HK = H_np(K)
    assert np.all(HK % q == 0)
    W = HK // q
    comp.append({"q": q, "K": K, "W": W, "Q": qnum(W) % q,
                 "P": pairnum(W, W) % q,
                 "lookup": {tuple(row): i for i, row in enumerate(K)}})
    print(f"ker mod {q}: n={len(K)} W range=({int(W.min())},{int(W.max())})",
          flush=True)

# --- the lifted split fiber (same construction as targeted script) ---
rng = np.random.default_rng(3)
fixed = {}
for c in comp:
    q = c["q"]
    sup = comp_supported(c["K"], Z, Qmod, q)
    fixed[q] = c["K"][np.where(sup)[0][0]] if sup.any() else c["K"][0]
c81 = comp[1]
fib81 = group_ids(np.sort(c81["K"], axis=1))
canon81 = lex_canon(c81["K"], perms)
gam81 = group_ids(canon81)
gf = np.empty(int(gam81.max()) + 1, dtype=np.int64)
gf[gam81] = fib81
opf = np.bincount(gf, minlength=int(fib81.max()) + 1)
split81 = np.where(opf > 1)[0]
assert len(split81) == 1
f0 = int(split81[0])
idx = np.where(fib81 == f0)[0]
print(f"q=81 split fiber {f0}: size={len(idx)} component orbits="
      f"{len(set(gam81[idx].tolist()))}", flush=True)
lifts = {}
for c in comp:
    q = c["q"]
    lifts[q] = c["K"][idx] if q == 81 else np.tile(fixed[q], (len(idx), 1))
glob = crt_combine(m, D, QS, lifts)
assert np.all(H_np(glob) % D == 0)
gfib = group_ids(np.sort(glob, axis=1))
assert len(set(gfib.tolist())) == 1
gcan = lex_canon(glob, perms)
ggam = group_ids(gcan)
gsup = global_supported(glob, Z, Qmod, D)
print(f"global fiber: size={len(glob)} orbits={len(set(ggam.tolist()))} "
      f"supp={int(gsup.sum())} orbit sizes="
      f"{sorted(int((ggam == g).sum()) for g in set(ggam.tolist()))}",
      flush=True)
assert int(gsup.sum()) == len(glob)
wglob = H_np(glob) // D

# --- correction-mode test per component (random global points) ---
comp_idx_rand = []
rand_pts = {}
for c in comp:
    q = c["q"]
    sel = rng.integers(0, len(c["K"]), size=400)
    rand_pts[q] = c["K"][sel]
rand_glob = crt_combine(m, D, QS, rand_pts)
assert np.all(H_np(rand_glob) % D == 0)
wrand = H_np(rand_glob) // D
Qrand = qnum(wrand)
for s in (1, 13):
    print(f"--- correction test s={s}", flush=True)
    for c in comp:
        q = c["q"]
        u = (D // q) % q
        inv_u2 = pow((u * u) % q, -1, q)
        idx = np.array([c["lookup"][tuple(row)] for row in (rand_glob % q)])
        raw_bad = corr_bad = 0
        for _ in range(300):
            i = int(rng.integers(0, len(rand_glob)))
            j = int(rng.integers(0, len(rand_glob)))
            tg = int((2 * s * Qrand[i]
                      - int(pairnum(wrand[i:i + 1], wrand[j:j + 1])[0, 0])) % q)
            tc = int((2 * s * c["Q"][idx[i]] - c["P"][idx[i], idx[j]]) % q)
            if tc != tg:
                raw_bad += 1
            if (inv_u2 * tc) % q != tg:
                corr_bad += 1
        c[f"corr_s{s}"] = (raw_bad > 0 and corr_bad == 0)
        print(f"  q={q}: u={u} raw_bad={raw_bad}/300 corr_bad={corr_bad}/300 "
              f"-> correction={c[f'corr_s{s}']}", flush=True)
        assert not (raw_bad > 0 and corr_bad > 0), "no mode fits"


def phihat(s, target_glob):
    """phihat_s for target global Fix points via CRT factorisation."""
    tw = H_np(target_glob) // D
    assert np.all(H_np(target_glob) % D == 0)
    ph = np.ones(len(target_glob), dtype=np.complex128)
    for c in comp:
        q = c["q"]
        ci = pow(D // q, -1, q)
        u = (D // q) % q
        inv_u2 = pow((u * u) % q, -1, q)
        T = (2 * s * c["Q"][:, None] - c["P"]) % q
        if c[f"corr_s{s}"]:
            T = (inv_u2 * T) % q
        E = np.exp(2j * np.pi * ((ci * T) % q) / q)
        Sj = E.sum(axis=0)
        idx = np.array([c["lookup"][tuple(row)] for row in (target_glob % q)])
        ph *= Sj[idx]
    return ph / D


out = {"m": m, "D": D, "fiber_size": int(len(glob)),
       "orbit_sizes": sorted(int((ggam == g).sum())
                             for g in set(ggam.tolist()))}
for s in (1, 13):
    phi = phihat(s, glob)
    mod2 = (phi * np.conj(phi)).real
    target = 16.0 / D
    err = float(np.max(np.abs(mod2 - target)))
    # per-orbit coherent sums
    osums = {}
    for g in sorted(set(ggam.tolist())):
        oo = ggam == g
        osums[int(g)] = {"size": int(oo.sum()),
                         "abs_sum": float(abs(phi[oo].sum())),
                         "phi_mean": complex(np.mean(phi[oo])).real,
                         "phi_mean_im": complex(np.mean(phi[oo])).imag}
    spread = float(np.max(np.abs(phi - np.mean(phi))))
    print(f"s={s}: |phi|^2 max err vs 16/D = {err:.3e}; "
          f"max |phi-mean| over fiber = {spread:.3e}", flush=True)
    for g, v in osums.items():
        print(f"   orbit {g}: size={v['size']} |sum phi|={v['abs_sum']:.6e} "
              f"mean phi={v['phi_mean']:.6e}+{v['phi_mean_im']:.6e}j",
              flush=True)
    out[f"s{s}"] = {"modulus_err": err, "fiber_spread": spread,
                    "per_orbit": osums,
                    "fiber_coherent_abs": float(abs(phi.sum())),
                    "fiber_incoherent": float(mod2.sum())}
    # aggregate check: |sum_F phi|^2 vs |F|^2 * 16/D if constant
    print(f"   fiber |sum phi|^2 = {float(abs(phi.sum())**2):.6e} vs "
          f"|F|^2*16/D = {len(glob)**2 * target:.6e}", flush=True)

with open("/tmp/wave16_m12_phi.json", "w") as fh:
    json.dump(out, fh, indent=1, default=str)
print(json.dumps(out, indent=1, default=str))
