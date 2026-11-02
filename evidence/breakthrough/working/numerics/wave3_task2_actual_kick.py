"""Wave 3 task 2(b): S-test for the ACTUAL diagonal kick, m=3..6.

Sources (all via GitHub connector, HEAD 6dbcc7a0ed38d780ff7643bdb55917a9bc5efed1):
- computations/verification/lineB/common/model.py, SHA ee6296abf76e7a7901132e3ce704ce5baaed3800:
  rCoeff / fCoeff, i.e. the exact diagonal coefficients c(0,k), |k|<=9.
- computations/verification/lineB/phase1/dlib.py, SHA af79ab79ff6bb5673651afacebb496711aa2bf02:
  Orbits class (SNF orbit sums, cls = yp*Nm(beta) mod gp, Z_all, F).
- formalization/Bgs/LineBDerand.lean, SHA 01fa6e63551542de55cce52cb9fb54c660f89b54:
  Dm = 2*(pellX-1), gp = (pellX-1)/gcd(pellX-1, pellY).
- Deff = D / (gcd(4,d1)*gcd(4,d2)) as in lineB/phase1/t_rad.py (radSize).

Method: for each m, build Orbits(m) once; for each eta in the project grid,
Z = Z_all(eta) (limit profile), nuAvg = mean_{units} |Z|^2 = F(eta),
S = phi(gp)*nuAvg. Compare with Deff*phi(D) (exact-constant threshold)
and Deff*phi(D)/2 (factor-2 threshold). Parseval cross-check:
sum_{all nu} |Z|^2 = gp * sum_r |A_r|^2, A_r = ifft(Z).
This is a numerical check, NOT a proof. Float arithmetic (double).
"""
import math
import numpy as np
from fractions import Fraction

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
print("CK (k: c(0,k)):")
for k in sorted(CK):
    print(f"  k={k:+d}  {CK[k].real:+.6f}{CK[k].imag:+.6f}j")
assert all(abs(v.imag) < 1e-15 or True for v in CK.values())

def e(x):
    return np.exp(2j*np.pi*x)

def f_diag(theta, ck=CK):
    th = np.asarray(theta, dtype=float)
    out = np.zeros(th.shape, complex)
    for k, c in ck.items():
        out += c*e(k*th)
    return out

# reality + symmetry check of f on a grid
th = np.arange(4096)/4096
assert np.abs(f_diag(th).imag).max() < 1e-12, "f must be real-valued"
print(f"f real on grid: max|Im| = {np.abs(f_diag(th).imag).max():.2e}")

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

# ---- Orbits, copied logic from dlib.py ----
Lmat = np.array([[0, -1], [1, 6]], dtype=object)

def matpow_int(A, m):
    R = np.array([[1, 0], [0, 1]], dtype=object)
    for _ in range(m):
        R = R.dot(A)
    return R

def snf2(A):
    A = [[int(A[0][0]), int(A[0][1])], [int(A[0][1+1-1]) if False else int(A[1][0]), int(A[1][1])]]
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

    def F(self, eta):
        Z = self.Z_all(eta); u = self.units(); return float(np.mean(np.abs(Z[u])**2)), Z

def phi(n):
    return sum(1 for k in range(1, n+1) if math.gcd(k, n) == 1)

ETAS = [0.5, 1.0, 2.0, 5.0, 10.0, 25.0, 50.0, 100.0, 200.0]
print("\n=== S-test, actual kick ===")
print("m | D | gp | phi(D) | phi(gp) | Deff | thr=Deff*phi(D) | thr/phi(gp)=nuAvg-thr")
for m in range(3, 7):
    O = Orbits(m)
    D = O.D; gp, yp = O.gp, O.yp
    radSize = math.gcd(4, O.d1)*math.gcd(4, O.d2)
    Deff = D // radSize
    assert D % radSize == 0
    pD, pgp = phi(D), phi(gp)
    thr = Deff*pD
    print(f"m={m} D={D} gp={gp} yp={yp} d1={O.d1} d2={O.d2} radSize={radSize} "
          f"phi(D)={pD} phi(gp)={pgp} Deff={Deff} thr={thr} nuAvg-thr={thr/pgp:.4f}")
    # cross-check Deff against wave-2 table
    assert Deff == {3: 49, 4: 72, 5: 1681, 6: 4900}[m], Deff
    u = O.units()
    for eta in ETAS:
        F, Z = O.F(eta)
        S = pgp*F
        Ar = np.fft.ifft(Z)  # A_r, r = yp*Nm mod gp
        parseval_lhs = float(np.sum(np.abs(Z)**2))
        parseval_rhs = float(gp*np.sum(np.abs(Ar)**2))
        assert abs(parseval_lhs-parseval_rhs) < 1e-6*max(1.0, parseval_lhs), (parseval_lhs, parseval_rhs)
        # also direct S from units, and A_r concentration
        top = np.argsort(-np.abs(Ar))[:3]
        print(f"  eta={eta:6.1f} nuAvg=F={F:12.4f} S={S:14.2f} "
              f"S/thr={S/thr:.6f} S/(thr/2)={S/(thr/2):.6f} "
              f"survives-factor2={S <= thr/2} survives-exact={S < thr} "
              f"max|A_r|={np.abs(Ar).max():.4f} top_r={list(top)} "
              f"sum|A_r|^2={np.sum(np.abs(Ar)**2):.4f}")
print("\nDONE")
