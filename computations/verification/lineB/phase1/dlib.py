"""BGS derandomization library. Conventions = bgs-recon/code/model.py (MN, weylT) and audit46_core (exact symbol).
Diagonal (l=0) part of the fixed 32-mode kick: f(theta)=sum_k c(0,k) e(k theta), real-valued, |k|<=9."""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import sys, math, numpy as np
from fractions import Fraction as Fr
sys.path.insert(0, __import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)),'..','common')); sys.path.insert(0, __import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)),'..','common'))
from model import MN, weylT, fCoeff
LAM = 3 + 2*math.sqrt(2)

def e(x): return np.exp(2j*np.pi*x)

# exact diagonal coefficients c_k (k=-9..9) of the actual kick, l=0 row
CK = {k: fCoeff(k, 0) for k in range(-9, 10) if abs(fCoeff(k, 0)) > 0}
def f_diag(theta, ck=CK):
    th = np.asarray(theta, dtype=float); out = np.zeros(th.shape, complex)
    for k, c in ck.items(): out += c*e(k*th)
    assert np.abs(out.imag).max() < 1e-12
    return out.real

def ghat(eta, ck=CK, L=4096):
    """continuum Fourier coeffs of g=exp(i eta f) on R/Z: dict n->ghat(n), |n|<L/2 (FFT on L points; aliasing ~ superexp small)."""
    th = np.arange(L)/L
    g = np.exp(1j*eta*f_diag(th, ck))
    c = np.fft.fft(g)/L
    n = np.fft.fftfreq(L, 1/L).astype(int)
    return n, c

def pell(m):
    xs, ys = [1], [0]
    for _ in range(m): x, y = xs[-1], ys[-1]; xs.append(3*x+8*y); ys.append(x+3*y)
    return xs, ys

def Dm(m):
    xs, ys = pell(m); return 2*(xs[m]-1)

def gprime(m):
    xs, ys = pell(m); g = xs[m]-1; y = ys[m]; d = math.gcd(g, y); return g//d, y//d   # (g', y')

def Hmat(m):
    H = np.zeros((m, m), dtype=object)
    for j in range(m):
        H[j, j] += 6; H[j, (j+1) % m] -= 1; H[(j+1) % m, j] -= 1
    return H

def trace_ratio_quantum(N, m_list, eta, ck=CK):
    """exact Tr(DM)^m / Tr M^m for diagonal kick D=diag exp(i eta f(x/N)), via eigenvalues."""
    M = MN(N); x = np.arange(N)
    D = np.exp(1j*eta*f_diag(x/N, ck))
    evU = np.linalg.eigvals(D[:, None]*M); evM = np.linalg.eigvals(M)
    return {m: (np.sum(evU**m), np.sum(evM**m)) for m in m_list}

# ---------------- limit object Z_m(nu) via the group O/(lambda^m-1) -----------------
Lmat = np.array([[0, -1], [1, 6]], dtype=object)   # multiplication by lambda on basis {1,lambda}

def matpow_int(A, m):
    R = np.array([[1, 0], [0, 1]], dtype=object)
    for _ in range(m): R = R.dot(A)
    return R

def snf2(A):
    """Smith normal form of 2x2 integer matrix: returns P,Q unimodular (object), d1,d2 with A = P diag(d1,d2) Q."""
    A = [[int(A[0][0]), int(A[0][1])], [int(A[1][0]), int(A[1][1])]]
    import sympy
    M = sympy.Matrix(A)
    # use sympy's smith with transforms if available, else manual
    from sympy.matrices.normalforms import smith_normal_decomp
    Dg, U, V = smith_normal_decomp(M)   # Dg = U*M*V
    Ui = U.inv(); Vi = V.inv()           # M = Ui*Dg*Vi
    d1, d2 = int(Dg[0, 0]), int(Dg[1, 1])
    P = np.array(Ui.tolist(), dtype=object); Q = np.array(Vi.tolist(), dtype=object)
    if d1 < 0: d1 = -d1; P[:, 0] = -P[:, 0]
    if d2 < 0: d2 = -d2; P[:, 1] = -P[:, 1]
    assert (P.dot(np.array([[d1, 0], [0, d2]], dtype=object)).dot(Q) == np.array(A, dtype=object)).all()
    return P, Q, d1, d2

def norm(a, b): return a*a + 6*a*b + b*b

class Orbits:
    """All D_m periodic 'q-sequences' xi in G^ = (L^m-I)^{-T}Z^2/Z^2, theta_j(xi)=<L^j e1, xi>."""
    def __init__(self, m, ck=CK):
        self.m = m; A = matpow_int(Lmat, m) - np.eye(2, dtype=object)
        P, Q, d1, d2 = snf2(A); self.P, self.d1, self.d2 = P, d1, d2
        self.D = d1*d2; assert self.D == Dm(m), (self.D, Dm(m))
        k1, k2 = np.meshgrid(np.arange(d1, dtype=np.int64), np.arange(d2, dtype=np.int64), indexing='ij')
        PinvT = np.array(np.array(P.T.tolist(), dtype=object), dtype=object)
        import sympy
        PiT = np.array(sympy.Matrix(P.tolist()).T.inv().tolist(), dtype=object)  # integer unimodular
        X1 = (int(PiT[0, 0])*(k1*(d2//d1)) + int(PiT[0, 1])*k2) % d2
        X2 = (int(PiT[1, 0])*(k1*(d2//d1)) + int(PiT[1, 1])*k2) % d2
        # theta_j * d2 = ((L^T)^j X)_1 mod d2 ; L^T = [[0,1],[-1,6]]
        T = np.empty((m, d1, d2), dtype=np.int64)
        a, b = X1.copy(), X2.copy()
        for j in range(m):
            T[j] = a
            a, b = b % d2, (-a + 6*b) % d2
        assert (a == X1).all() and (b == X2).all()   # period m
        self.T = T   # theta numerators over d2
        ftab = f_diag(np.arange(d2)/d2, ck)
        self.S = ftab[T].sum(axis=0)    # orbit sums S(xi) (real), shape (d1,d2)
        # norm classes on dual side: beta = P b
        b1, b2 = np.meshgrid(np.arange(d1, dtype=object), np.arange(d2, dtype=object), indexing='ij')
        self.gp, self.yp = gprime(m)
        P00, P01, P10, P11 = [int(v) for v in (P[0, 0], P[0, 1], P[1, 0], P[1, 1])]
        bb1 = np.arange(d1, dtype=np.int64)[:, None]; bb2 = np.arange(d2, dtype=np.int64)[None, :]
        A_ = (P00*bb1 + P01*bb2); B_ = (P10*bb1 + P11*bb2)
        gp = self.gp
        A_ %= gp; B_ %= gp
        self.cls = ((self.yp % gp) * ((A_*A_ + 6*A_*B_ + B_*B_) % gp)) % gp   # class of beta: y' Nm(beta) mod g'

    def Phi(self, eta): return np.exp(1j*eta*self.S)

    def Z_all(self, eta):
        """Z(nu) for nu=0..g'-1 : Z(nu)=sum_beta mu(beta) e(-nu y' Nm(beta)/g')."""
        mu = np.fft.fft2(self.Phi(eta))/self.D
        Acls = np.bincount(self.cls.ravel(), weights=mu.real.ravel(), minlength=self.gp) + \
               1j*np.bincount(self.cls.ravel(), weights=mu.imag.ravel(), minlength=self.gp)
        return np.fft.fft(Acls)   # sum_r A_r e(-nu r/g')

    def units(self): return np.array([v for v in range(self.gp) if math.gcd(v, self.gp) == 1])

    def F(self, eta):
        Z = self.Z_all(eta); u = self.units(); return float(np.mean(np.abs(Z[u])**2)), Z
