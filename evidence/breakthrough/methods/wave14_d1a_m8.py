"""Wave 14, task 3: D1a at m=8 — coherent sums per Gamma-orbit inside fibers.

phihat_s from main (LineDOrbitPairFull, HEAD d87dce0, fetched via connector):
  phihat_s([w]) = (1/D) * sum_{eta in Vquot} e((2s*Qnum(y) - pairNum(y,w))/D),
  pairNum(y,w) = (X y).w, Qnum(y) = pairNum(y,y), X = adjugate(H),
  fixEquivQuot maps xi in Fix to [w_xi], w_xi = (H * lift(xi))/D.
Taking eta representatives as w_{xi'} for xi' in Fix_8, the summand is
  e((2s*Qnum(w') - pairNum(w',w))/D),  w' = w_{xi'}, w = w_xi.
The exponent factorises over CRT components q in (9,289,512):
  e(t/D) = prod_i e(c_i * t_i / q_i),  c_i = (D/q_i)^{-1} mod q_i,
  t_i = t mod q_i, computed from component kernel points.
Hence phihat(xi) = (1/D) * prod_i S_i(xi_i), S_i[j] = sum_k e_i(k,j),
which is validated below against the Lean modulus dichotomy
|phihat|^2 in {0, |V4|/D} = {0, 4/D} and the torsion support criterion.
"""
import json
import numpy as np
import sympy as sp
from fractions import Fraction

m = 8
D = 1331712
MODS = (9, 289, 512)
S_VALS = (1, 5)  # both odd and coprime to D; s=3 is NOT coprime (3 | D)
MOD_TARGET = 16.0 / D  # |V4|/D, |V4| = 16 at m=8 (Lean phihatFix_modulus_values)


def kernel_mod(mod):
    res = []
    for a in range(mod):
        for b in range(mod):
            seq = [a, b]
            for _ in range(m):
                seq.append((6 * seq[-1] - seq[-2]) % mod)
            if seq[m] == a and seq[m + 1] == b:
                res.append(seq[:m])
    return np.array(res, dtype=np.int64)


def Hmat_np(v):
    return 6 * v - np.roll(v, 1, axis=1) - np.roll(v, -1, axis=1)


# --- adjugate of H_8 (exact) ---
Hsp = sp.zeros(m)
for i in range(m):
    Hsp[i, i] = 6
    Hsp[i, (i - 1) % m] -= 1
    Hsp[i, (i + 1) % m] -= 1
X = np.array(Hsp.adjugate().tolist(), dtype=np.int64)
print("X max abs:", int(np.abs(X).max()), "det check:", int(round(float(Hsp.det()))), flush=True)
assert int(round(float(Hsp.det()))) == D


def pairnum(A, B):
    # (X a).b for rows a in A, b in B -> matrix; X symmetric
    return (A @ X) @ B.T


def qnum(A):
    return np.einsum("ij,ij->i", A @ X, A)


# --- component kernels and their w-vectors ---
comp = []
for q in MODS:
    K = kernel_mod(q)
    W = Hmat_np(K) // q
    assert np.all(Hmat_np(K) % q == 0)
    comp.append({"q": q, "K": K, "W": W, "Q": qnum(W) % q})
    print(f"ker mod {q}: n={len(K)} w-range=({int(W.min())},{int(W.max())})", flush=True)

# --- global Fix_8 via CRT ---
def crt_combine(A, mod_a, B, mod_b):
    inv = pow(mod_a, -1, mod_b)
    diff = (B[None, :, :] - A[:, None, :]) % mod_b
    t = (diff * inv) % mod_b
    return (A[:, None, :] + mod_a * t).reshape(-1, m)


pts = crt_combine(comp[0]["K"], 9, comp[1]["K"], 289)
pts = crt_combine(pts, 9 * 289, comp[2]["K"], 512)
assert pts.shape[0] == D
assert np.all(Hmat_np(pts) % D == 0)
wglob = Hmat_np(pts) // D
print("Fix_8 points:", pts.shape, "w range:", int(wglob.min()), int(wglob.max()), flush=True)

# component indices of global points
comp_idx = []
for c in comp:
    q = c["q"]
    lookup = {tuple(row): i for i, row in enumerate(c["K"])}
    idx = np.array([lookup[tuple(row)] for row in (pts % q)], dtype=np.int64)
    comp_idx.append(idx)
    print(f"component q={q}: distinct idx used = {len(set(idx.tolist()))} of {len(c['K'])}", flush=True)

# --- validate CRT factorisation of the exponent on random pairs ---
# Component kernel w-vectors satisfy [w_i] = (D/q_i) * [w] in Vquot, so
# component Q/P are scaled by u^2, u = (D/q_i) mod q_i, relative to the
# global values mod q_i.  For q=9,289 the scaling happens to act trivially
# on the values that occur; for q=512 it does not.  Select per component,
# by direct test on random global pairs, whether raw or u^{-2}-corrected
# component data equals the global t mod q_i.
rng = np.random.default_rng(0)
s = 1
Qglob = qnum(wglob)
for c, idx in zip(comp, comp_idx):
    q = c["q"]
    u = (D // q) % q
    inv_u2 = pow((u * u) % q, -1, q)
    Pc = pairnum(c["W"], c["W"]) % q
    c["Pc"] = Pc
    raw_bad = corr_bad = 0
    for _ in range(500):
        i = int(rng.integers(0, D))
        j = int(rng.integers(0, D))
        tg = int((2 * s * Qglob[i] - int(pairnum(wglob[i:i + 1], wglob[j:j + 1])[0, 0])) % q)
        tc = int((2 * s * c["Q"][idx[i]] - Pc[idx[i], idx[j]]) % q)
        if tc != tg:
            raw_bad += 1
        if (inv_u2 * tc) % q != tg:
            corr_bad += 1
    c["corr"] = (raw_bad > 0 and corr_bad == 0)
    print(f"q={q}: u={u} raw_bad={raw_bad}/500 corr_bad={corr_bad}/500 "
          f"-> use_correction={c['corr']}", flush=True)
    assert not (raw_bad > 0 and corr_bad > 0), "no component mode fits"
maxdiff = 0.0
for trial in range(3000):
    i = int(rng.integers(0, D))
    j = int(rng.integers(0, D))
    t = int((2 * s * Qglob[i] - int(pairnum(wglob[i:i + 1], wglob[j:j + 1])[0, 0])) % D)
    ph_direct = np.exp(2j * np.pi * t / D)
    ph_fact = 1.0 + 0.0j
    for c, idx in zip(comp, comp_idx):
        q = c["q"]
        ci = pow(D // q, -1, q)
        u = (D // q) % q
        inv_u2 = pow((u * u) % q, -1, q)
        tc = int((2 * s * c["Q"][idx[i]] - c["Pc"][idx[i], idx[j]]) % q)
        ti = (inv_u2 * tc) % q if c["corr"] else tc
        ph_fact *= np.exp(2j * np.pi * ((ci * ti) % q) / q)
    maxdiff = max(maxdiff, abs(ph_direct - ph_fact))
print("exponent factorisation max phase diff over 3000 random pairs:", maxdiff, flush=True)
assert maxdiff < 1e-9


def phihat_for_s(s):
    ph = np.ones(D, dtype=np.complex128)
    for c, idx in zip(comp, comp_idx):
        q = c["q"]
        ci = pow(D // q, -1, q)
        u = (D // q) % q
        inv_u2 = pow((u * u) % q, -1, q)
        P = c["Pc"]  # [k, j], mod q
        T = (2 * s * c["Q"][:, None] - P) % q
        if c["corr"]:
            T = (inv_u2 * T) % q
        E = np.exp(2j * np.pi * ((ci * T) % q) / q)
        Sj = E.sum(axis=0)
        ph *= Sj[idx]
    return ph / D


# --- support via torsion criterion (wave 8 script) ---
V4 = []
for code in range(4 ** m):
    v = []
    cc = code
    for _ in range(m):
        v.append(cc % 4)
        cc //= 4
    hv = [6 * v[i] - v[(i - 1) % m] - v[(i + 1) % m] for i in range(m)]
    if all(x % 4 == 0 for x in hv):
        V4.append(v)
assert len(V4) == 16
tors = [[x // 4 for x in [6 * v[i] - v[(i - 1) % m] - v[(i + 1) % m] for i in range(m)]]
        for v in V4]
Z = np.array(tors, dtype=np.int64)
Qnum_tors = []
for z in tors:
    t = Hsp.LUsolve(sp.Matrix([D * zz for zz in z]))
    assert all(x.q == 1 for x in t)
    Qnum_tors.append(sum(zz * int(tt) for zz, tt in zip(z, t)))
Qnum_tors = np.array(Qnum_tors, dtype=np.int64)
pair = pts @ Z.T
passcount = (((2 * Qnum_tors[None, :] - pair) % D) == 0).sum(axis=1)
supp = passcount == 16
print("support size (torsion):", int(supp.sum()), flush=True)
assert int(supp.sum()) == 83232

# --- fibers and Gamma orbits ---
gam_perms = []
for k in range(8):
    gam_perms.append([(j + k) % 8 for j in range(8)])
    gam_perms.append([(k - j) % 8 for j in range(8)])
gam_perms = np.array(gam_perms, dtype=np.int64)


def lex_canon(arr, perms):
    out = np.empty_like(arr)
    CH = 50000
    for st in range(0, len(arr), CH):
        chunk = arr[st:st + CH]
        permuted = np.stack([chunk[:, p] for p in perms], axis=1)
        mask = np.ones((len(chunk), len(perms)), dtype=bool)
        for cc in range(arr.shape[1]):
            vals = np.where(mask, permuted[:, :, cc], np.iinfo(np.int64).max)
            mask &= (permuted[:, :, cc] == vals.min(axis=1, keepdims=True))
        chosen = mask.argmax(axis=1)
        out[st:st + CH] = permuted[np.arange(len(chunk)), chosen]
    return out


sorted_keys = np.sort(pts, axis=1)
gam_canon = lex_canon(pts, gam_perms)
uniq_fib, fib_id = np.unique(sorted_keys, axis=0, return_inverse=True)
uniq_gam, gam_id = np.unique(gam_canon, axis=0, return_inverse=True)
fib_id = np.asarray(fib_id).reshape(-1)
gam_id = np.asarray(gam_id).reshape(-1)
n_fib, n_gam = len(uniq_fib), len(uniq_gam)
fib_size = np.bincount(fib_id, minlength=n_fib)
gam_size = np.bincount(gam_id, minlength=n_gam)
gam_fiber = np.empty(n_gam, dtype=np.int64)
gam_fiber[gam_id] = fib_id
orbits_per_fiber = np.bincount(gam_fiber, minlength=n_fib)
bad_fib = np.where(orbits_per_fiber > 1)[0]
print(f"fibers={n_fib} orbits={n_gam} bad(split) fibers={len(bad_fib)}", flush=True)

# support composition by fiber
in_supp_fib = np.bincount(fib_id[supp], minlength=n_fib)
fib_full = np.where(in_supp_fib == fib_size)[0]
fib_empty = np.where(in_supp_fib == 0)[0]
fib_partial = np.where((in_supp_fib > 0) & (in_supp_fib < fib_size))[0]
print(f"fibers fully in supp={len(fib_full)} empty={len(fib_empty)} partial={len(fib_partial)}", flush=True)
print(f"split fibers meeting supp: {int(np.intersect1d(bad_fib, fib_full).size)} "
      f"(+partial {int(np.intersect1d(bad_fib, fib_partial).size)})", flush=True)

out = {"D": D, "n_fibers": int(n_fib), "n_gamma_orbits": int(n_gam),
       "bad_fibers": int(len(bad_fib)), "support_size": int(supp.sum()),
       "fibers_full_in_supp": int(len(fib_full)), "fibers_empty": int(len(fib_empty)),
       "fibers_partial": int(len(fib_partial)),
       "split_fibers_in_supp": int(np.intersect1d(bad_fib, fib_full).size)}

for s in S_VALS:
    phi = phihat_for_s(s)
    mod2 = (phi * np.conj(phi)).real
    # modulus dichotomy validation
    err_supp = float(np.max(np.abs(mod2[supp] - MOD_TARGET))) if supp.any() else 0.0
    err_off = float(np.max(np.abs(mod2[~supp]))) if (~supp).any() else 0.0
    supp_from_phi = mod2 > MOD_TARGET / 2.0
    agree = bool(np.array_equal(supp_from_phi, supp))
    # constancy within orbits and within fibers (max |phi - orbit/fiber mean|)
    def max_spread(ids, n_ids):
        sums = np.zeros(n_ids, dtype=np.complex128)
        np.add.at(sums, ids, phi)
        cnts = np.bincount(ids, minlength=n_ids)
        means = sums / np.maximum(cnts, 1)
        return float(np.max(np.abs(phi - means[ids])))
    spread_orb = max_spread(gam_id, n_gam)
    spread_fib = max_spread(fib_id, n_fib)
    # coherent vs incoherent per fiber
    fsum = np.zeros(n_fib, dtype=np.complex128)
    np.add.at(fsum, fib_id, phi)
    incoh = np.zeros(n_fib)
    np.add.at(incoh, fib_id, mod2)
    coh2 = (fsum * np.conj(fsum)).real
    # split fibers detail
    split_phi_max = float(np.max(np.abs(phi[np.isin(fib_id, bad_fib)]))) if len(bad_fib) else 0.0
    split_coh_max = float(np.max(coh2[bad_fib])) if len(bad_fib) else 0.0
    split_incoh_max = float(np.max(incoh[bad_fib])) if len(bad_fib) else 0.0
    ratio = float(coh2.sum() / mod2.sum())
    target = float(Fraction(318335, 20808))
    print(f"--- s={s}: |phi|^2 err on supp={err_supp:.3e} off supp={err_off:.3e} "
          f"supp agreement={agree}", flush=True)
    print(f"    spread within Gamma-orbit={spread_orb:.3e} within fiber={spread_fib:.3e}", flush=True)
    print(f"    split fibers: max|phi|={split_phi_max:.3e} max coherent|sum|^2={split_coh_max:.3e} "
          f"max incoherent sum={split_incoh_max:.3e}", flush=True)
    print(f"    aggregate sum_F |sum_F phi|^2 / sum |phi|^2 = {ratio:.9f} "
          f"vs Bsym 318335/20808 = {target:.9f} diff={abs(ratio - target):.3e}", flush=True)
    out[f"s{s}"] = {
        "modulus_err_on_supp": err_supp, "modulus_err_off_supp": err_off,
        "support_agreement": agree, "spread_within_orbit": spread_orb,
        "spread_within_fiber": spread_fib, "split_max_abs_phi": split_phi_max,
        "split_max_coherent_sq": split_coh_max, "split_max_incoherent": split_incoh_max,
        "aggregate_ratio": ratio, "bsym_target": target,
    }
    if s == 1:
        # per-orbit coherent sums inside split fibers: distribution
        osum = np.zeros(n_gam, dtype=np.complex128)
        np.add.at(osum, gam_id, phi)
        bad_orbits = np.unique(gam_id[np.isin(fib_id, bad_fib)])
        out["split_orbit_abs_sums"] = {
            "n_orbits_in_split_fibers": int(len(bad_orbits)),
            "max_abs_orbit_sum": float(np.max(np.abs(osum[bad_orbits]))),
        }
        print(f"    split-fiber Gamma-orbits={len(bad_orbits)} "
              f"max |per-orbit sum|={float(np.max(np.abs(osum[bad_orbits]))):.3e}", flush=True)
        # a concrete split fiber example
        f0 = int(bad_fib[0])
        sub = np.where(fib_id == f0)[0]
        ex = {"fiber_size": int(len(sub)),
              "orbit_sizes": sorted([int((gam_id[sub] == g).sum()) for g in set(gam_id[sub].tolist())]),
              "phi_values": [complex(round(float(phi[i].real), 12), round(float(phi[i].imag), 12))
                             for i in sub[:4]]}
        out["first_split_fiber_example"] = {"fiber_size": ex["fiber_size"], "orbit_sizes": ex["orbit_sizes"]}
        print("    first split fiber:", ex, flush=True)

with open("/tmp/wave14_d1a_m8_result.json", "w") as fh:
    json.dump(out, fh, indent=1)
print(json.dumps(out, indent=1))
