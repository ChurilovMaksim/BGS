"""Wave 4 task 3: exact constant for hEquidistUnits with the ACTUAL kick.

Sources (pinned HEAD 6dbcc7a0ed38d780ff7643bdb55917a9bc5efed1, via GitHub
connector, SHAs re-verified this run):
- computations/verification/lineB/common/model.py, SHA ee6296ab...:
  rCoeff/fCoeff, diagonal coefficients c(0,k), |k|<=9.
- computations/verification/lineB/phase1/dlib.py, SHA af79ab79...:
  Orbits class (SNF orbit sums, cls = yp*Nm mod gp, Z_all, F).
- formalization/Bgs/LineBDerand.lean, SHA 01fa6e63...: Dm, gp.
- formalization/Bgs/LineBNAverageUnits.lean, SHA ae0e303d...:
  nuAvgUnits = mean over (Z/gp)^x of Btup, Btup(nu)=|Z(nu)|^2.

Definitions used here (same as wave 2 task 3 / wave 3 task 2):
  W_X = {X < N <= 2X, gcd(N,D)=1}, nu_N = N^{-1} mod gp,
  winAvg(X) = mean_{N in W_X} Btup(nu_N),
  nuAvgUnits = mean_{nu in (Z/gp)^x} Btup(nu),
  diff(X) = winAvg(X) - nuAvgUnits.
  Btup(nu) = |Z_all(eta)[nu]|^2 from dlib's Orbits (limit profile).
  s0_f = sum_k |c(0,k)| (the only finite-support coefficient object in
  model.py); also s0_exp(eta) = sum_k |Fourier coeff of exp(i*eta*f)|
  on a 16384-point grid, reported separately because the bridge's s0
  is ambiguous for the actual (non-finite) kick.

This is a numerical check on double arithmetic, NOT a proof.
"""
import json, math
import numpy as np

# ---- exact kick coefficients, verbatim logic from model.py ----
def rCoeff(k):
    return {0: 1.0, 1: .5, -1: .5, 7: -.5, -7: -.5, 6: -.25, -6: -.25, 8: -.25, -8: -.25}.get(k, 0.0)

def fCoeff(k, l):
    if l == 0:
        v = (0.5 if k in (7, -7) else 0) + rCoeff(k)/10 + (rCoeff(k-1)-rCoeff(k+1))/(200j)
        v -= (0.1 if k == 0 else 0)
        return complex(v)
    raise ValueError("only l=0 used here")

CK = {k: fCoeff(k, 0) for k in range(-9, 10) if abs(fCoeff(k, 0)) > 0}
S0_F = float(sum(abs(v) for v in CK.values()))
print(f"CK: {sorted(CK.items())}")
print(f"s0_f = sum|c(0,k)| = {S0_F:.6f}")

def e(x):
    return np.exp(2j*np.pi*x)

def f_diag(theta, ck=CK):
    th = np.asarray(theta, dtype=float)
    out = np.zeros(th.shape, complex)
    for k, c in ck.items():
        out += c*e(k*th)
    return out

def s0_exp(eta, ngrid=16384):
    th = np.arange(ngrid)/ngrid
    vals = np.exp(1j*eta*f_diag(th).real)
    coeff = np.fft.fft(vals)/ngrid
    return float(np.sum(np.abs(coeff)))

# ---- Pell / Derand quantities ----
def pell(m):
    xs, ys = [1], [0]
    for _ in range(m):
        xs.append(3*xs[-1]+8*ys[-1]); ys.append(xs[-2]+3*ys[-1])
    return xs, ys

def Dm(m):
    xs, ys = pell(m); return 2*(xs[m]-1)

def gprime(m):
    xs, ys = pell(m); g = xs[m]-1; y = ys[m]; d = math.gcd(g, y); return g//d, y//d

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

# ---- Orbits, copied logic from dlib.py (as in wave 3 task 2) ----
Lmat = np.array([[0, -1], [1, 6]], dtype=object)

def matpow_int(A, m):
    R = np.array([[1, 0], [0, 1]], dtype=object)
    for _ in range(m):
        R = R.dot(A)
    return R

def snf2(A):
    A = [[int(A[0][0]), int(A[0][1])], [int(A[1][0]), int(A[1][1])]]
    import sympy
    from sympy.matrices.normalforms import smith_normal_decomp
    M = sympy.Matrix(A)
    Dg, U, V = smith_normal_decomp(M)
    Ui = U.inv(); Vi = V.inv()
    d1, d2 = int(Dg[0, 0]), int(Dg[1, 1])
    P = np.array(Ui.tolist(), dtype=object)
    if d1 < 0: d1 = -d1; P[:, 0] = -P[:, 0]
    if d2 < 0: d2 = -d2; P[:, 1] = -P[:, 1]
    assert (P.dot(np.array([[d1, 0], [0, d2]], dtype=object)).dot(np.array(Vi.tolist(), dtype=object)) == np.array(A, dtype=object)).all()
    return P, d1, d2

class Orbits:
    def __init__(self, m, ck=CK):
        self.m = m
        A = matpow_int(Lmat, m) - np.eye(2, dtype=object)
        P, d1, d2 = snf2(A)
        self.P, self.d1, self.d2 = P, d1, d2
        self.D = d1*d2
        assert self.D == Dm(m), (self.D, Dm(m))
        k1, k2 = np.meshgrid(np.arange(d1, dtype=np.int64), np.arange(d2, dtype=np.int64), indexing='ij')
        import sympy
        PiT = np.array(sympy.Matrix(P.tolist()).T.inv().tolist(), dtype=object)
        X1 = (int(PiT[0, 0])*(k1*(d2//d1)) + int(PiT[0, 1])*k2) % d2
        X2 = (int(PiT[1, 0])*(k1*(d2//d1)) + int(PiT[1, 1])*k2) % d2
        T = np.empty((m, d1, d2), dtype=np.int64)
        a, b = X1.copy(), X2.copy()
        for j in range(m):
            T[j] = a
            a, b = b % d2, (-a + 6*b) % d2
        assert (a == X1).all() and (b == X2).all()
        self.T = T
        ftab = f_diag(np.arange(d2)/d2, ck)
        self.S = ftab[T].sum(axis=0)
        b1 = np.arange(d1, dtype=np.int64)[:, None]; b2 = np.arange(d2, dtype=np.int64)[None, :]
        self.gp, self.yp = gprime(m)
        P00, P01, P10, P11 = [int(v) for v in (P[0, 0], P[0, 1], P[1, 0], P[1, 1])]
        A_ = (P00*b1 + P01*b2); B_ = (P10*b1 + P11*b2)
        A_ %= self.gp; B_ %= self.gp
        self.cls = ((self.yp % self.gp) * ((A_*A_ + 6*A_*B_ + B_*B_) % self.gp)) % self.gp

    def Phi(self, eta):
        return np.exp(1j*eta*self.S)

    def Z_all(self, eta):
        mu = np.fft.fft2(self.Phi(eta))/self.D
        Acls = np.bincount(self.cls.ravel(), weights=mu.real.ravel(), minlength=self.gp) + \
               1j*np.bincount(self.cls.ravel(), weights=mu.imag.ravel(), minlength=self.gp)
        return np.fft.fft(Acls)

    def units(self):
        return np.array([v for v in range(self.gp) if math.gcd(v, self.gp) == 1])

# ---- window counts (eta-independent) ----
def window_counts(D, gp, X):
    counts = {}
    W = 0
    for N in range(X+1, 2*X+1):
        if math.gcd(N, D) == 1:
            W += 1
            nu = pow(N, -1, gp)
            counts[nu] = counts.get(nu, 0) + 1
    return counts, W

XGRID = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000]
ETAS = [0.5, 1.0, 2.0, 5.0, 10.0, 25.0, 50.0, 100.0, 200.0]

results = []
for m in range(3, 7):
    O = Orbits(m)
    D = O.D; gp = O.gp
    radSize = math.gcd(4, O.d1)*math.gcd(4, O.d2)
    Deff = D // radSize
    pD, pgp = phi_euler(D), phi_euler(gp)
    rho = pD / D
    units = O.units()
    assert len(units) == pgp
    # window counts per X
    win = []
    for X in XGRID:
        counts, W = window_counts(D, gp, X)
        assert all(math.gcd(nu, gp) == 1 for nu in counts), "nu must be a unit"
        dev = max(abs(c - W/pgp) for c in counts.values()) if counts else 0.0
        # units with zero count (only possible for small X)
        if len(counts) < pgp:
            dev = max(dev, W/pgp)
        win.append(dict(X=X, W=W, rho=W/X, counts={int(k): int(v) for k, v in counts.items()},
                        max_count_dev=dev))
    print(f"\nm={m} D={D} gp={gp} phi(D)={pD} phi(gp)={pgp} Deff={Deff} "
          f"D*Deff={D*Deff} 4gp*s0_f^(2m)={4*gp*S0_F**(2*m):.3f} rho={rho:.4f}")
    for Xw in win:
        print(f"  X={Xw['X']:>6} W={Xw['W']:>6} W/X={Xw['rho']:.4f} max|count-W/phi|={Xw['max_count_dev']:.2f}")
    for eta in ETAS:
        Z = O.Z_all(eta)
        Btup = {int(u): float(abs(Z[u])**2) for u in units}
        nuAvg = float(np.mean([Btup[int(u)] for u in units]))
        S = pgp * nuAvg
        s_exp = s0_exp(eta)
        curve = []
        for Xw in win:
            X, W, counts = Xw['X'], Xw['W'], Xw['counts']
            winAvg = sum(c*Btup[nu] for nu, c in counts.items())/W
            diff = winAvg - nuAvg
            curve.append(dict(X=X, W=W, winAvg=winAvg, diff=diff,
                              Xabsdiff=X*abs(diff),
                              ratio_2pi=X*abs(diff)/(2*math.pi),
                              ratio_DDeff=X*abs(diff)/(D*Deff),
                              ratio_s0f=X*abs(diff)/(4*gp*S0_F**(2*m))))
        sup_all = max(c['Xabsdiff'] for c in curve)
        big = [c for c in curve if c['X'] >= 10000]
        sup_big = max(c['Xabsdiff'] for c in big)
        lo_big = min(c['Xabsdiff'] for c in big)
        last = curve[-1]
        print(f"  eta={eta:6.1f} nuAvg={nuAvg:9.4f} S={S:10.2f} S/rho={S/rho:11.2f} "
              f"s0_exp={s_exp:.3f} 4gp*s0_exp^(2m)={4*gp*s_exp**(2*m):.3e} "
              f"supX|diff|={sup_all:11.2f} band[X>=10000]=[{lo_big:.2f},{sup_big:.2f}] "
              f"X=100000: X|diff|={last['Xabsdiff']:.2f} diff={last['diff']:.3e}")
        results.append(dict(m=m, D=D, gp=gp, phiD=pD, phigp=pgp, Deff=Deff,
                            DDeff=D*Deff, s0_f=S0_F, const_s0f=4*gp*S0_F**(2*m), rho=rho,
                            eta=eta, nuAvg=nuAvg, S=S, S_over_rho=S/rho, s0_exp=s_exp,
                            const_s0exp=4*gp*s_exp**(2*m),
                            sup_Xabsdiff=sup_all, band_lo_10000=lo_big, band_hi_10000=sup_big,
                            curve=[{k: c[k] for k in ('X','W','winAvg','diff','Xabsdiff','ratio_2pi','ratio_DDeff','ratio_s0f')} for c in curve]))

with open("/home/hatch/workspace/bgs-breakthrough/numerics/wave4_task3_results.json", "w") as f:
    json.dump(results, f, indent=1)
print("\nsaved wave4_task3_results.json")
print("DONE")
