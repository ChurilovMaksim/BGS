"""Line D core library: band-limited random kicks on the quantized cat map S=[[3,4],[2,3]].
Conventions identical to Line B/C:  M_p(x,y) = p^{-1/2} e_p(-8^{-1}(3x^2-2xy+3y^2)),  U = diag(g(x/p)) M_p,
g(q) = exp(i eta v(q)),  v(q) = sum_{k in modes} a_k cos(2 pi k q + theta_k).
H = H_m = 6I - C - C^T (circulant), D_m = det H_m = Tr S^m - 2, X_m = D_m H_m^{-1} (integer, Line B Lemma Q).
Orbit group Fix_m = H^{-1}Z^m / Z^m, parametrised by (xi_0, xi_1) via xi_j = (L^j e_0).(xi_0,xi_1), L=[[0,-1],[1,6]]."""

if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import numpy as np, math
from fractions import Fraction

def eN(N, t): return np.exp(2j*np.pi*(np.asarray(t) % N)/N)

def MN(N):
    x = np.arange(N)[:, None]; y = np.arange(N)[None, :]
    inv8 = pow(8, -1, N)
    return eN(N, (-inv8*(3*x*x - 2*x*y + 3*y*y)) % N)/np.sqrt(N)

def pell(m):
    xs, ys = [1], [0]
    for _ in range(m):
        x, y = xs[-1], ys[-1]; xs.append(3*x + 8*y); ys.append(x + 3*y)
    return xs, ys

def Dm(m):
    xs, ys = pell(m); return 2*(xs[m]-1)

def Hmat(m):
    H = [[0]*m for _ in range(m)]
    for i in range(m):
        H[i][i] += 6; H[i][(i+1) % m] -= 1; H[(i+1) % m][i] -= 1
    return H

def Xmat(m):
    """X = D H^{-1}, Line B Lemma Q: X[i][j] = y_m x_d - (D/2) y_d [i!=j], d=|i-j|."""
    xs, ys = pell(m); D = 2*(xs[m]-1)
    return [[ys[m]*xs[abs(i-j)] - (D//2)*ys[abs(i-j)]*(i != j) for j in range(m)] for i in range(m)], D

def check_HX(m):
    H = Hmat(m); X, D = Xmat(m)
    P = [[sum(H[i][k]*X[k][j] for k in range(m)) for j in range(m)] for i in range(m)]
    return all(P[i][j] == (D if i == j else 0) for i in range(m) for j in range(m))

# ---------- Smith normal form for 2x2 integer matrices (with transforms) ----------
def _egcd(a, b):
    if b == 0: return (a, 1, 0) if a >= 0 else (-a, -1, 0)
    g, x, y = _egcd(b, a % b); return g, y, x - (a//b)*y

def mmul(A, B): return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]

def snf2(A):
    """returns P, Q, (d1, d2) with P A Q = diag(d1, d2), P, Q unimodular, d1 | d2, d1, d2 > 0."""
    P = [[1, 0], [0, 1]]; Q = [[1, 0], [0, 1]]; M = [r[:] for r in A]
    for _ in range(100):
        # clear column 0 below pivot via row ops
        a, c = M[0][0], M[1][0]
        if c != 0:
            g, x, y = _egcd(a, c)
            R = [[x, y], [-c//g, a//g]]
            M = mmul(R, M); P = mmul(R, P)
        a, b = M[0][0], M[0][1]
        if b != 0:
            g, x, y = _egcd(a, b)
            C = [[x, -b//g], [y, a//g]]
            M = mmul(M, C); Q = mmul(Q, C)
        if M[1][0] == 0 and M[0][1] == 0:
            if M[1][1] % M[0][0] == 0: break
            # make divisible: add row 1 to row 0
            R = [[1, 1], [0, 1]]; M = mmul(R, M); P = mmul(R, P)
    if M[0][0] < 0: R = [[-1, 0], [0, 1]]; M = mmul(R, M); P = mmul(R, P)
    if M[1][1] < 0: R = [[1, 0], [0, -1]]; M = mmul(R, M); P = mmul(R, P)
    assert mmul(mmul(P, A), Q) == [[M[0][0], 0], [0, M[1][1]]]
    return P, Q, (M[0][0], M[1][1])

def inv2(P):
    det = P[0][0]*P[1][1] - P[0][1]*P[1][0]; assert abs(det) == 1
    return [[P[1][1]*det, -P[0][1]*det], [-P[1][0]*det, P[0][0]*det]]

class Orbits:
    """Fix_m with exact integer coordinates Xi[ξ, j] in Z/d2 (xi_j = Xi/d2), and the n-class group Z^2/(L^m-I)Z^2."""
    def __init__(self, m):
        self.m = m
        L = [[0, -1], [1, 6]]
        Lm = [[1, 0], [0, 1]]
        self.Lpows = []
        for j in range(m):
            self.Lpows.append([Lm[0][0], Lm[1][0]])  # L^j e_0 (coords of lambda^j in basis 1, lambda)
            Lm = mmul(L, Lm)
        A = [[Lm[0][0]-1, Lm[0][1]], [Lm[1][0], Lm[1][1]-1]]
        self.A = A
        P, Q, (d1, d2) = snf2(A)
        self.P, self.Q, self.d1, self.d2 = P, Q, d1, d2
        self.D = d1*d2
        assert self.D == Dm(m), (self.D, Dm(m))
        X, D = Xmat(m); self.X = X
        # orbit points: (xi0, xi1) = P^T (k/d1, l/d2);  as integers mod d2: P^T (k*d2/d1, l)
        k = np.repeat(np.arange(d1), d2); l = np.tile(np.arange(d2), d1)
        u = k*(d2//d1); w = l
        xi0 = (P[0][0]*u + P[1][0]*w) % d2
        xi1 = (P[0][1]*u + P[1][1]*w) % d2
        self.kl = (k, l)
        Xi = np.zeros((self.D, m), dtype=np.int64)
        for j in range(m):
            c, d = self.Lpows[j]
            Xi[:, j] = (c*xi0 + d*xi1) % d2
        self.Xi = Xi
    def check_orbits(self, nsample=2000):
        """H xi in Z^m for all xi (exact, on a sample) and xi_{j+1}=6xi_j-xi_{j-1} cyclically."""
        Xi = self.Xi[:nsample]; m = self.m; d2 = self.d2
        ok = True
        for j in range(m):
            r = (6*Xi[:, j] - Xi[:, (j-1) % m] - Xi[:, (j+1) % m]) % d2
            ok &= bool(np.all(r == 0))
        return ok
    def phihat(self, s):
        """phihat_s(xi) = (1/D) sum_{n in Z^m/HZ^m} e(2 s n^T H^{-1} n - n.xi); n=(a,b,0..0), (a,b)=P^{-1}(i,j)."""
        d1, d2, D = self.d1, self.d2, self.D
        Pi = inv2(self.P)
        i = np.arange(d1)[:, None]; j = np.arange(d2)[None, :]
        a = (Pi[0][0]*i + Pi[0][1]*j); b = (Pi[1][0]*i + Pi[1][1]*j)
        X = self.X
        # 2 s n^T X n / D  with n=(a,b,0,...): n^T X n = X00 a^2 + 2 X01 a b + X11 b^2
        num = (2*s*((X[0][0]*a*a) % D + (2*X[0][1]*a*b) % D + (X[1][1]*b*b) % D)) % D
        phi = np.exp(2j*np.pi*num/D)
        F = np.fft.fft2(phi)/D   # F[k,l] = (1/D) sum phi(i,j) e(-ik/d1 - jl/d2)
        return F.reshape(-1)     # ordering matches self.kl (k major)
    def Sk(self, k):
        return np.exp(2j*np.pi*((k*self.Xi) % self.d2)/self.d2).sum(axis=1)

def gamma_classes(orb, Xi=None):
    """canonical representative of each orbit under the dihedral group (rotations, reversal) -> class labels, sizes."""
    Xi = orb.Xi if Xi is None else Xi; m = orb.m
    keys = []
    def cands():
        for r in range(m):
            R = np.roll(Xi, -r, axis=1); yield R; yield R[:, ::-1]
    best = Xi.copy()
    for C in cands():
        # compare rows lexicographically
        less = np.zeros(len(Xi), bool); eq = np.ones(len(Xi), bool)
        for j in range(m):
            less |= eq & (C[:, j] < best[:, j]); eq &= (C[:, j] == best[:, j])
        best[less] = C[less]
    _, lab, cnt = np.unique(best, axis=0, return_inverse=True, return_counts=True)
    return lab.reshape(-1), cnt

def multiset_classes(orb):
    S = np.sort(orb.Xi, axis=1)
    _, lab, cnt = np.unique(S, axis=0, return_inverse=True, return_counts=True)
    return lab.reshape(-1), cnt
