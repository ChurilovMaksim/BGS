"""Wave 18, task 1: phihat (CRT factorisation, wave-16 method) for the
35,952 split-fiber points, then the exact pair-sum ratio R at m=12.
Validates phihat against wave16_m12_phi.json first.
"""
import json
import sys

import numpy as np
import sympy as sp

sys.path.insert(0, ".")
from wave16_d1a_targeted import (Dm, snf_kernel, torsion_data,
                                 comp_supported, gamma_perms, lex_canon,
                                 group_ids, crt_combine)

m = 12
D = Dm(m)
QS = [128, 81, 25, 49, 121]
assert D == 128 * 81 * 25 * 49 * 121
Z, Qmod = torsion_data(m, D)
perms = gamma_perms(m)

Hsp = sp.zeros(m)
for i in range(m):
    Hsp[i, i] = 6
    Hsp[i, (i - 1) % m] -= 1
    Hsp[i, (i + 1) % m] -= 1
X = np.array(Hsp.adjugate().tolist(), dtype=np.int64)


def H_np(v):
    return 6 * v - np.roll(v, 1, axis=1) - np.roll(v, -1, axis=1)


def pairnum(A, B):
    return (A @ X) @ B.T


def qnum(A):
    return np.einsum("ij,ij->i", A @ X, A)


# --- component data ---
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
    print(f"comp q={q} ready", flush=True)


# --- correction-mode test (wave-16 method) ---
def decide_corr(s):
    rng = np.random.default_rng(3)
    rand_pts = {}
    for c in comp:
        q = c["q"]
        sel = rng.integers(0, len(c["K"]), size=400)
        rand_pts[q] = c["K"][sel]
    rand_glob = crt_combine(m, D, QS, rand_pts)
    wrand = H_np(rand_glob) // D
    Qrand = qnum(wrand)
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
        print(f"  s={s} q={q}: raw_bad={raw_bad} corr_bad={corr_bad} "
              f"-> corr={c[f'corr_s{s}']}", flush=True)
        assert not (raw_bad > 0 and corr_bad > 0), "no mode fits"


def phihat(s, target_glob):
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


# --- validation: rebuild wave-16 fiber, compare to wave16_m12_phi.json ---
for s in [1, 13]:
    decide_corr(s)
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
lifts = {}
for c in comp:
    q = c["q"]
    lifts[q] = c["K"][idx] if q == 81 else np.tile(fixed[q], (len(idx), 1))
glob = crt_combine(m, D, QS, lifts)
gcan = lex_canon(glob, perms)
ggam = group_ids(gcan)
ref = json.load(open("wave16_m12_phi.json"))
ph = phihat(1, glob)
print("validation vs wave16_m12_phi.json (s=1):")
for g in sorted(set(ggam.tolist())):
    oo = ggam == g
    mean = np.mean(ph[oo])
    rmean = ref["s1"]["per_orbit"][str(g)]
    print(f"  orbit {g}: mean={mean.real:.6e}+{mean.imag:.6e}j "
          f"ref={rmean['phi_mean']:.6e}+{rmean['phi_mean_im']:.6e}j "
          f"diff={abs(mean - (rmean['phi_mean'] + 1j*rmean['phi_mean_im'])):.2e}")

# --- split-fiber points ---
raw = np.fromfile("wave18_splitpts.bin", dtype=np.uint32).reshape(-1, 12).astype(np.int64)
print(f"split points loaded: {len(raw)}")
assert len(raw) == 35952
fib = group_ids(np.sort(raw, axis=1))
print(f"split fibers from points: {len(set(fib.tolist()))} (expect 762)")
assert len(set(fib.tolist())) == 762
# fiber sizes check
import collections
sizes = collections.Counter(fib.tolist())
print(f"sum |F|^2 over split fibers: {sum(v*v for v in sizes.values())} (expect 1713888)")
assert sum(v * v for v in sizes.values()) == 1713888

supp = 96049800
sumF = 2303461770
sq_split = 1713888
for s in [1, 13]:
    ph = phihat(s, raw)
    mod2 = (ph * np.conj(ph)).real
    print(f"s={s}: |phi|^2 min={mod2.min():.6e} max={mod2.max():.6e} "
          f"target={16/D:.6e} maxerr={np.abs(mod2 - 16/D).max():.3e}")
    assert np.abs(mod2 - 16 / D).max() < 1e-15
    # orbit constancy within split fibers
    can = lex_canon(raw, perms)
    # group by (fiber, orbit)
    key = np.concatenate([np.sort(raw, axis=1), can], axis=1)
    uniq, _, inv = np.unique(key, axis=0, return_index=True, return_inverse=True)
    # per (fiber,orbit) group: check phi constant
    maxdev = 0.0
    for g in range(len(uniq)):
        vals = ph[inv == g]
        maxdev = max(maxdev, float(np.abs(vals - vals[0]).max()))
    print(f"s={s}: max |phi - phi_orbit_rep| within orbits: {maxdev:.3e}")
    # coherent sums per fiber
    S = np.zeros(len(sizes), dtype=np.complex128)
    np.add.at(S, fib, ph)
    coh = (np.abs(S) ** 2) * (D / 16.0)  # in Bsym units (|F|^2 if aligned)
    R = ((sumF - sq_split) + float(coh.sum())) / supp
    print(f"s={s}: R = {R:.12f}")
    print(f"s={s}: R - Bsym_Gamma = {R - 383766967/16008300:+.12f}")
    print(f"s={s}: R - Bsym_w = {R - 383795287/16008300:+.12f}")
    print(f"s={s}: R - Bsym_fiber = {R - 76782059/3201660:+.12f}")
    print(f"s={s}: split fibers with coherent=0 (|S|<1e-12): "
          f"{int((np.abs(S) < 1e-12).sum())} of {len(sizes)}; "
          f"coherent sum total = {float(coh.sum()):.6f} "
          f"(vs sumsq_split {sq_split})")
    if s == 1:
        np.save("wave18_split_coh_s1.npy", coh)
        json.dump({"R_s1": R}, open("wave18_R.json", "w"))
