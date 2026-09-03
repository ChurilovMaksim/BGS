"""
CORE EXPERIMENT (v2, correct quantisation).

Egorov-verified propagator of the cat map A in SL(2,Z), N odd, gcd(c,N)=1:

    U_A(x,y) = N^{-1/2} w^{ (2c)^{-1} (d x^2 - 2 x y + a y^2) },   w = e^{2 pi i / N}

Verified properties (see run log):
  * unitary to 1e-15,
  * exact Egorov  U T(n) U^dagger = T(An) for the Weyl operators
        T(n1,n2) = w^{ 2^{-1} n1 n2 } X^{n1} Z^{n2},
  * exact torsion U^k = chi * U_{+-I},  U^{2k} = chi^2 I,  k = ord_N(A).

Consequences implemented here:
  (A) spectrum of U_A is contained in a coset of the 2k-th roots of unity
      => at most 2k distinct eigenvalues, multiplicities >= N/(2k);
  (B) first-order degenerate perturbation theory: for a Hermitian observable V,
      the splitting inside the eigenspace H_lambda is the spectrum of the
      compression  V_lambda = P_lambda V P_lambda.  We measure the level
      statistics of V_lambda and compare with GOE / GUE / Poisson.
"""
import numpy as np, math, json, os

ART = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "artifacts")
os.makedirs(ART, exist_ok=True)


def U_cat(A, N):
    a, b, c, d = A
    w = np.exp(2j*np.pi/N)
    icb = pow((2*c) % N, -1, N)
    xs = np.arange(N)
    X, Y = np.meshgrid(xs, xs, indexing='ij')
    Q = (icb*(d*X*X - 2*X*Y + a*Y*Y)) % N
    return w**Q / math.sqrt(N)


def weyl(N):
    w = np.exp(2j*np.pi/N)
    b2 = pow(2, -1, N)
    Xm = np.zeros((N, N), dtype=complex)
    for x in range(N):
        Xm[x, (x-1) % N] = 1.0
    Zm = np.diag(w**np.arange(N))
    def T(n1, n2):
        n1 %= N; n2 %= N
        return (w**((b2*n1*n2) % N))*np.linalg.matrix_power(Xm, n1) @ np.linalg.matrix_power(Zm, n2)
    return T


def ord_pm(A, N):
    a, b, c, d = [v % N for v in A]
    P = (1, 0, 0, 1)
    for k in range(1, 2*N+3):
        P = ((P[0]*a+P[1]*c) % N, (P[0]*b+P[1]*d) % N,
             (P[2]*a+P[3]*c) % N, (P[2]*b+P[3]*d) % N)
        if P == (1, 0, 0, 1): return k, +1
        if P == (N-1, 0, 0, N-1): return k, -1
    return -1, 0


def eigenspaces(U, N, tol=1e-8):
    """Exact spectral decomposition; group eigenvectors by eigenvalue."""
    ev, W = np.linalg.eig(U)
    th = np.angle(ev)
    order = np.argsort(th)
    th, W = th[order], W[:, order]
    groups = []
    start = 0
    for i in range(1, len(th)+1):
        if i == len(th) or abs(th[i]-th[start]) > tol:
            groups.append((th[start:i].mean(), W[:, start:i]))
            start = i
    # orthonormalise each block (eig does not guarantee it)
    out = []
    for lam, B in groups:
        Q, _ = np.linalg.qr(B)
        out.append((lam, Q))
    return out


def spacing_stats(vals, tag, bins=60, smax=4.0):
    """Unfolded NN spacings of a real spectrum: local-density unfolding by
    a smooth polynomial fit of the counting function (standard protocol)."""
    x = np.sort(np.asarray(vals, dtype=float))
    n = len(x)
    if n < 12: return None
    # unfold: fit cumulative counting function by a low-order polynomial
    cnt = np.arange(1, n+1) - 0.5
    deg = min(8, max(3, n//12))
    cf = np.polyfit(x, cnt, deg)
    u = np.polyval(cf, x)
    s = np.diff(u)
    s = s[s >= 0]
    if len(s) < 8: return None
    s = s/s.mean()
    edges = np.linspace(0, smax, bins+1)
    h, _ = np.histogram(s, bins=edges, density=True)
    mid = 0.5*(edges[:-1]+edges[1:])
    w1 = (np.pi/2)*mid*np.exp(-np.pi*mid*mid/4)
    w2 = (32/np.pi**2)*mid*mid*np.exp(-4*mid*mid/np.pi)
    po = np.exp(-mid)
    mk = (mid > 0.05) & (mid < 3.5); dw = mid[1]-mid[0]
    return dict(tag=tag, n=int(len(s)),
                L1_goe=float(np.sum(np.abs(h[mk]-w1[mk])*dw)),
                L1_gue=float(np.sum(np.abs(h[mk]-w2[mk])*dw)),
                L1_poisson=float(np.sum(np.abs(h[mk]-po[mk])*dw)),
                hist=h.tolist(), bins=mid.tolist(), spacings=s.tolist())
