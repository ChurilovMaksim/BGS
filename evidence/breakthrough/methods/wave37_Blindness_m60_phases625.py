"""Trimmed 625-phase check: wave-34 formula, correction validated at 625.
Validates against published first-fiber phases, then reports second fiber.
"""
import sys
import numpy as np
sys.path.insert(0, ".")
exec(open("wave37_Blindness_m60.py").read().split("# ---------- small components")[0])
# lex_canon / group_ids / gamma_perms from wave16, defs only (lines 130-160):
src = open("wave16_d1a_targeted.py").read().splitlines()
exec("\n".join(src[129:160]))
perms = gamma_perms(M)

q = 625
D = 8572001542975368419584080488440354732051920000  # D_60 (wave 32)
assert D % q == 0 and D % 81 == 0
K = np.array(kernel_points(M, q), dtype=np.int64)
assert len(K) == q
fib = group_ids(np.sort(K, axis=1))
canon = lex_canon(K, perms)
gam = group_ids(canon)
gam_fiber = np.empty(int(gam.max()) + 1, dtype=np.int64)
gam_fiber[gam] = fib
opf = np.bincount(gam_fiber, minlength=int(fib.max()) + 1)
splits = [f for f in np.where(opf > 1)[0]]
print("split fibers:", splits, "orbits:", [len(set(gam[fib == f].tolist())) for f in splits])

def H_np(v):
    return 6 * v - np.roll(v, 1, axis=1) - np.roll(v, -1, axis=1)
HK = H_np(K)
assert np.all(HK % q == 0)
W = HK // q
dqm = (D // q) % q
Q = (dqm * np.einsum("ij,ij->i", W, K)) % q
P = (dqm * (W @ K.T)) % q
u = (D // q) % q
inv_u2 = pow((u * u) % q, -1, q)
T = (inv_u2 * (2 * Q[:, None] - P)) % q  # correction: validated True at 625 (wave 34)
ci = pow(D // q, -1, q)
for f in splits:
    idxf = np.where(fib == f)[0]
    phs = []
    for g in sorted(set(gam[idxf].tolist())):
        oo = idxf[gam[idxf] == g]
        E = np.exp(2j * np.pi * ((ci * T[:, oo]) % q) / q)
        vals = E.sum(axis=0)
        phs.append(float(np.angle(vals[0])))
        print(f"  fiber {f} orbit {g}: size={len(oo)} phase={phs[-1]:.6f} "
              f"spread={np.abs(vals - vals[0]).max():.2e}", flush=True)
    print(f"  fiber {f}: phases distinct: {len(set(round(p, 4) for p in phs))} of {len(phs)}", flush=True)
print("PHASES625 DONE", flush=True)
