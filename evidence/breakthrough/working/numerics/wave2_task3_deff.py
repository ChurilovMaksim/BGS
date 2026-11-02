"""Wave 2 task 3: C2 constant and the Deff branch.
Model only: m=3..6, finite-support ghat, exact integer NmZ, grouping by NmZ mod gp.
Definitions (from Bridge/Derand, test copies; not a claim about current main):
  D_m = 2(x_m-1), gp = (x_m-1)/gcd(x_m-1,y_m), yp = y_m/gcd(...),
  NmZ(n) = sum_{i,j} n_i n_j x_{|i-j|}, x_d = Pell x_d,
  Z(nu) = sum_n phi(n) exp(-2 pi i nu yp NmZ(n)/gp), Btup(nu)=|Z(nu)|^2,
  S = sum_{nu units} Btup(nu), nuAvg = S/phi(gp),
  Deff = D_m/radSize, radSize = gcd(4,d1)*gcd(4,d2).
Window: W_X = {X < N <= 2X, gcd(N,D_m)=1}, nu_N = N^{-1} mod gp,
  winAvg = mean_N Btup(nu_N), diff = winAvg - nuAvg.
Ratios: R_Deff(X) = X*|diff|/(D_m*Deff), R_s(X) = X*|diff|/(4*gp*s0^(2m)).
Verbatim Deff branch (with prefactor D_m) would need R_Deff(X) <= 1 for all X.
S-route bound: |diff| <= S/|W|; for large X, |W|/X -> phi(D)/D, so
  S-route can prove the branch only if S <= Deff*phi(D), i.e. nuAvg <= Deff*phi(D)/phi(gp).
No constants are fitted to points: ghat families are fixed grids below.
"""
import json, math
from math import gcd
import numpy as np

def phi_euler(n):
    r, x, p = n, n, 2
    while p * p <= x:
        if x % p == 0:
            while x % p == 0:
                x //= p
            r -= r // p
        p += 1 if p == 2 else 2
    if x > 1:
        r -= r // x
    return r

def pell_xy(m):
    x, y = 1, 0
    for _ in range(m):
        x, y = 3 * x + 8 * y, x + 3 * y
    return x, y

def pell_x_list(nmax):
    xs = [1]
    # x_0=1, x_1=3, recurrence x_{d+1}=6 x_d - x_{d-1} (since (3+2sqrt2)^d)
    if nmax >= 1:
        xs.append(3)
    for d in range(2, nmax + 1):
        xs.append(6 * xs[-1] - xs[-2])
    return xs

def table(m):
    x, y = pell_xy(m)
    D = 2 * (x - 1)
    g = gcd(x - 1, y)
    gp, yp = (x - 1) // g, y // g
    # d1 from L^m, L=[[0,-1],[1,6]]
    a, b, c, d = 1, 0, 0, 1
    for _ in range(m):
        a, b, c, d = b, -a + 6 * b, d, -c + 6 * d
    d1 = math.gcd(math.gcd(abs(a - 1), abs(b)), math.gcd(abs(c), abs(d - 1)))
    d2 = D // d1
    rad = math.gcd(4, d1) * math.gcd(4, d2)
    Deff = D // rad
    return dict(m=m, D=D, gp=gp, yp=yp, phiD=phi_euler(D), phigp=phi_euler(gp),
                Deff=Deff, nuAvg_thresh=Deff * phi_euler(D) / phi_euler(gp))

def profile(m, supp, gvals):
    """supp: list of integer k; gvals: dict k->float ghat_k. Returns S, nuAvg, Btup dict."""
    t = table(m)
    gp, yp = t["gp"], t["yp"]
    K = len(supp)
    total = K ** m
    if total > 2_000_000:
        return None
    xs = pell_x_list(m)
    Xmat = np.array([[xs[abs(i - j)] for j in range(m)] for i in range(m)], dtype=np.int64)
    idx = np.arange(total, dtype=np.int64)
    digits = np.empty((total, m), dtype=np.int64)
    tmp = idx.copy()
    for j in range(m):
        digits[:, j] = tmp % K
        tmp //= K
    vals = np.array(supp, dtype=np.int64)[digits]  # (total, m)
    # NmZ = v^T X v
    NmZ = np.einsum("ij,jk,ik->i", vals, Xmat, vals)
    garr = np.array([gvals[k] for k in supp], dtype=float)
    phi = np.prod(garr[digits], axis=1)
    residues = np.mod(NmZ, gp)
    A = np.bincount(residues, weights=phi, minlength=gp).astype(complex)
    units = [u for u in range(gp) if gcd(u, gp) == 1]
    r = np.arange(gp)
    # Z_u = sum_r A_r exp(-2 pi i u yp r / gp)
    E = np.exp(-2j * np.pi * np.outer(units, r) * yp / gp)
    Z = E @ A
    Btup = np.abs(Z) ** 2
    S = float(np.sum(Btup))
    return dict(S=S, nuAvg=S / t["phigp"], Btup={int(u): float(b) for u, b in zip(units, Btup)},
                A_r=A, units=units, table=t)

def window_diff(m, Btup, Xvals):
    t = table(m)
    D, gp, phi_gp = t["D"], t["gp"], t["phigp"]
    nuAvg = sum(Btup.values()) / phi_gp
    out = []
    for X in Xvals:
        counts = {}
        W = 0
        for N in range(X + 1, 2 * X + 1):
            if gcd(N, D) == 1:
                W += 1
                nu = pow(N, -1, gp)
                counts[nu] = counts.get(nu, 0) + 1
        if W == 0:
            continue
        win = sum(c * Btup[nu] for nu, c in counts.items()) / W
        diff = win - nuAvg
        out.append(dict(X=X, W=W, rho=W / X, diff=diff,
                        R_Deff=abs(diff) * X / (D * t["Deff"]),
                        S_over_W=sum(Btup.values()) / W))
    return out

FAMILIES = []
for K in (2, 3, 4, 5, 7, 9, 10, 12):
    FAMILIES.append((f"uniform 0..{K-1}", list(range(K)), {k: 1.0 for k in range(K)}))
for K in (1, 2, 3, 4):
    supp = list(range(-K, K + 1))
    FAMILIES.append((f"uniform -{K}..{K}", supp, {k: 1.0 for k in supp}))
supp = list(range(-4, 5))
FAMILIES.append(("decay 2^-|k|, -4..4", supp, {k: 2.0 ** (-abs(k)) for k in supp}))
for K in (4, 8):
    supp = list(range(K))
    FAMILIES.append((f"alternating (-1)^k, 0..{K-1}", supp, {k: (-1.0) ** k for k in supp}))
FAMILIES.append(("single 0", [0], {0: 1.0}))

XGRID = [100, 200, 500, 1000, 2000, 5000, 10000, 20000]
results = []
for m in range(3, 7):
    t = table(m)
    print(f"m={m} D={t['D']} gp={t['gp']} yp={t['yp']} phiD={t['phiD']} phigp={t['phigp']} "
          f"Deff={t['Deff']} nuAvg_thresh={t['nuAvg_thresh']:.1f}")
    for name, supp, gvals in FAMILIES:
        s0 = sum(abs(v) for v in gvals.values())
        q = sum(abs(v) ** 2 for v in gvals.values())
        pr = profile(m, supp, gvals)
        if pr is None:
            print(f"  SKIP {name}: {len(supp)}^{m} modes > 2e6")
            continue
        wd = window_diff(m, pr["Btup"], XGRID)
        maxR = max((d["R_Deff"] for d in wd), default=0.0)
        # s-branch ratio at largest X in grid
        Rs = [abs(d["diff"]) * d["X"] / (4 * t["gp"] * s0 ** (2 * m)) for d in wd]
        rec = dict(m=m, family=name, supp=supp, s0=s0, q=q, diag=q ** m,
                   S=pr["S"], nuAvg=pr["nuAvg"], thresh=t["nuAvg_thresh"],
                   ratio_S_over_Deff_phiD=pr["S"] / (t["Deff"] * t["phiD"]),
                   max_R_Deff=maxR,
                   max_R_s=max(Rs) if Rs else None,
                   window=[{k: (round(v, 6) if isinstance(v, float) else v) for k, v in d.items()} for d in wd])
        results.append(rec)
        flag = "KILL-S-route" if rec["ratio_S_over_Deff_phiD"] > 1 else ""
        flag2 = "KILL-verbatim" if maxR > 1 else ""
        print(f"  {name}: s0={s0} q^m={q**m:.1f} nuAvg={pr['nuAvg']:.1f} "
              f"S/(Deff*phiD)={rec['ratio_S_over_Deff_phiD']:.4f} maxR_Deff={maxR:.4f} {flag} {flag2}")

with open("/home/hatch/workspace/bgs-breakthrough/numerics/wave2_task3_deff_results.json", "w") as f:
    json.dump(results, f, indent=1)
print("saved results json")
