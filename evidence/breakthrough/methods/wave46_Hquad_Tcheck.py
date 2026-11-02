"""Wave 46, task 8: verify the derived H-quad/H-diff formulas against exact T.

Reuses phases_729 from wave45_F3_investigate.py (defs only).
Checks, per m:
 (1) Fexact[i,j] = ((ci*T[i,j] mod 729)/27) mod 27 equals the closed form
     Fpred = u^-2 * (-M_i*(2*L0_i - L0_j) + N_i*(2*L1_i - L1_j)) mod 27
     for ALL 729x729 (i,j), where M,N,L0,L1 are the trace linear forms.
 (2) the (a,b,c,d_j,e_j,f_j) expansion at one fiber-0 orbit.
 (3) H-diff: for every top-digit orbit pair (Cbar diff (0,9)),
     T[:,j'] - T[:,j] == 243*eps*ybar_i (mod 729) pointwise.
Also: kernel counts at 729 for m=45, 90 (the 36-divides-m failing cases).
"""
import numpy as np

src = open("wave45_F3_investigate.py").read().split("for m in [36, 72")[0]
exec(src)

def AB(m):
    A, B = 1, 0
    for _ in range(m):
        A, B = 3*A + 4*B, 2*A + 3*B
    return A, B

def params(m):
    A, B = AB(m); Am1, Bm1 = AB(m-1)
    a, b = (A-1)//27, B//27
    nu_0, nu_1 = 2*a % 27, 4*b % 27
    mu_0, mu_1 = (6*a - 8*b) % 27, (12*b - 8*a) % 27
    tau_0, tau_1 = (2*Am1) % 27, (4*Bm1) % 27
    D = 2*(A-1)
    u = (D//729) % 729
    return dict(nu_0=nu_0, nu_1=nu_1, mu_0=mu_0, mu_1=mu_1,
                tau_0=tau_0, tau_1=tau_1, uinv2=pow(u % 27, -2, 27),
                eps=(pow(u % 3, -1, 3)*(tau_1 % 3)*(nu_1 % 3)) % 3)

for m in [36, 72, 144, 180, 252]:
    info, T, ci, K, gam, fib = phases_729(m)
    assert len(K) == 729
    Cbars = []
    for row in K:
        x, y = recover_C(tuple(int(v) for v in row), 729)
        assert x % 27 == 0 and y % 27 == 0
        Cbars.append(((x//27) % 27, (y//27) % 27))
    xb = np.array([c[0] for c in Cbars]); yb = np.array([c[1] for c in Cbars])
    P = params(m)
    ciT = (int(ci)*T) % 729
    assert np.all(ciT % 27 == 0), "27 does not divide ci*T"
    Fexact = (ciT//27) % 27
    M = (P["mu_0"]*xb + P["mu_1"]*yb) % 27
    N = (P["nu_0"]*xb + P["nu_1"]*yb) % 27
    L0 = (2*xb) % 27
    L1 = (P["tau_0"]*xb + P["tau_1"]*yb) % 27
    Fpred = (P["uinv2"]*(-M[:, None]*(2*L0[:, None]-L0[None, :])
                          + N[:, None]*(2*L1[:, None]-L1[None, :])) ) % 27
    mm = int((Fexact != Fpred).sum())
    print(f"m={m}: Fexact vs Fpred mismatches = {mm} / 531441", flush=True)
    # expansion check at one fiber-0 orbit (xbar=14)
    reps = {}
    for r, (f, C, ph, sp, sz, val) in info.items():
        reps.setdefault(f, []).append((r, C))
    f0 = None
    for f, lst in reps.items():
        for r, C in lst:
            if C[0] == 378:
                f0 = (f, r, C); break
        if f0: break
    f, j, C = f0
    xj, yj = (C[0]//27) % 27, (C[1]//27) % 27
    a_p = ((-4*P["mu_0"] + 2*P["nu_0"]*P["tau_0"])*P["uinv2"]) % 27
    b_p = ((2*P["nu_1"]*P["tau_1"])*P["uinv2"]) % 27
    c_p = ((-4*P["mu_1"] + 2*P["nu_0"]*P["tau_1"] + 2*P["nu_1"]*P["tau_0"])*P["uinv2"]) % 27
    d_p = ((-6*P["mu_0"]*xj)*P["uinv2"]) % 27
    e_p = ((3*P["nu_1"]*P["tau_1"]*yj)*P["uinv2"]) % 27
    Mj = (P["mu_0"]*xj + P["mu_1"]*yj) % 27
    Nj = (P["nu_0"]*xj + P["nu_1"]*yj) % 27
    f_p = (P["uinv2"]*(-Mj*(2*xj) + Nj*(P["tau_0"]*xj + P["tau_1"]*yj))) % 27
    dx = (xb - xj) % 27; dy = (yb - yj) % 27
    Fexp = (a_p*dx*dx + b_p*dy*dy + c_p*dx*dy + d_p*dx + e_p*dy + f_p) % 27
    mm2 = int((Fexact[:, j] != Fexp).sum())
    print(f"   expansion at fiber-0 orbit C={C}: (a,b,c,d,e,f)=({a_p},{b_p},{c_p},{d_p},{e_p},{f_p}) mismatches={mm2}/729", flush=True)
    # H-diff over all top-digit orbit pairs in split fibers
    eps = 1 if P["eps"] == 1 else -1
    npair = 0; nbad = 0
    for f, lst in reps.items():
        byC = {((C[0]//27) % 27, (C[1]//27) % 27): r for r, C in lst}
        for (xj2, yj2), r in list(byC.items()):
            r2 = byC.get((xj2, (yj2-9) % 27))
            if r2 is not None:
                npair += 1
                diff = (T[:, r2]-T[:, r]) % 729
                exp = (243*eps*yb) % 729
                nbad += int((diff != exp).sum())
    print(f"   H-diff: {npair} top-digit pairs, eps={eps:+d}, bad rows={nbad}", flush=True)

# 36-not-divide-m cases: kernel size at 729 and 3-adic data
for m in [45, 90]:
    K45 = kernel_points(m, 729)
    A, B = AB(m)
    D = 2*(A-1)
    v = 0
    while D % 3 == 0:
        D //= 3; v += 1
    print(f"m={m}: len(kernel at 729)={len(K45)}, v3(D_m)={v}, 729|D_m: {2*(A-1) % 729 == 0}")
print("DONE")
