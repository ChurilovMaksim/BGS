"""Step 2 (Line E extension): exact transfer-operator law at the residues N == -/+ 4a^2 (mod h_m), a odd.
Independent of the Line E author code and of the referee code (own Pell utilities)."""
import math, itertools, numpy as np
LAM = 3 + 2*math.sqrt(2); C0 = 1/(LAM - 1/LAM)          # c = 1/(4 sqrt 2)
def pell(d):                       # S^d = [[x,4y],[2y,x]], S=[[3,4],[2,3]]
    x, y = 1, 0
    for _ in range(d): x, y = 3*x + 8*y, x + 3*y
    return x, y
def mdata(m):
    assert m % 2 == 1 and m >= 3
    xm, ym = pell(m); D = 2*(xm - 1); h = math.isqrt(D//4); assert 4*h*h == D
    assert ym % h == 0; yp = ym//h; gp = 2*h
    assert math.gcd(yp, gp) == 1 and h*h + 1 == 2*yp*yp
    return dict(m=m, h=h, yp=yp, gp=gp, D=D, xm=xm, ym=ym)
def nu_res(m, a, s=+1):
    """odd lift (mod g'=2h) of nu with 4 a^2 nu == -s (mod h), i.e. N = nu^{-1} == -s 4a^2 (mod h)."""
    d = mdata(m); h = d['h']; assert math.gcd(a, 2*h) == 1
    nu = (-s*pow(4*a*a, -1, h)) % h
    if nu % 2 == 0: nu += h
    return nu
def phase_exact(m, nu, n):
    """Line B phase  -nu y' Nm(alpha_n)/g'  mod 1 as an exact Fraction; Nm = sum_ij x_|i-j| n_i n_j."""
    from fractions import Fraction
    d = mdata(m); X = [pell(k)[0] for k in range(m)]
    Nm = sum(X[abs(i-j)]*n[i]*n[j] for i in range(m) for j in range(m))
    return Fraction((-nu*d['yp']*Nm) % d['gp'], d['gp'])
def sqrt2_mod(M):
    r = [t for t in range(M) if (t*t - 2) % M == 0]
    return r
def law_params(m, a, s=+1, root=None):
    """Parameters of the exact law  phase(n) = s*c/a^2 [sum n_j s_j + n_j^2/2] + kappa (sum n)^2/8 + gamma/a^2 [sum n_j sig_j + n_j^2/2]
    with s_j the real periodic IFS orbit, sig_j the periodic orbit of sig -> lam^{-1}(sig + n) in Z/a^2 (embedding sqrt2 -> root)."""
    d = mdata(m); h, yp = d['h'], d['yp']; A2 = a*a
    nu = nu_res(m, a, s); k = (4*A2*nu + s)//h; assert (4*A2*nu + s) % h == 0
    # 1/(8a^2) = u/8 + v/a^2
    u = pow(A2, -1, 8); v = (1 - u*A2)//8; assert u*A2 + 8*v == 1
    kappa = (-k*u*yp) % 8
    out = dict(m=m, a=a, s=s, nu=nu, k=k, kappa=kappa, u=u, v=v)
    if a == 1: return out
    r = root if root is not None else sqrt2_mod(A2)[0]
    lam = (3 + 2*r) % A2; lami = pow(lam, -1, A2); lm = pow(lami, m, A2)   # lam^{-m}
    assert math.gcd((1 - lm) % A2, A2) == 1, 'lam^m == 1 mod p for some p | a'
    B = ((2*yp + h*r) * pow(4, -1, A2)) % A2
    gamma = (-k*v*2*B*(1 - lm)) % A2
    out.update(root=r, lam=lam, lami=lami, B=B, gamma=gamma)
    return out
def law_phase(m, a, s, n, P=None):
    """phase from the law (float real part + exact rational arithmetic parts), for checking."""
    P = P or law_params(m, a, s)
    nn = list(n); sreal = []
    # real periodic orbit s_j = sum_{k>=1} n_{j-k} lam^{-k}  (periodic)
    for j in range(m):
        sreal.append(sum(nn[(j-kk) % m]*LAM**(-kk) for kk in range(1, 40*m+1)))
    real = s*C0/(a*a)*(sum(nn[j]*sreal[j] for j in range(m)) + 0.5*sum(t*t for t in nn))
    tot = (P['kappa']*sum(nn)**2) % 8 / 8
    if a > 1:
        A2 = a*a; lami = P['lami']; lm = pow(lami, m, A2)
        # periodic sigma: sig_{j+1} = lami (sig_j + n_j); sig_0 = sum_{j} lami^{m-j} n_j / (1 - lami^m)
        acc = 0
        for j in range(m): acc = (lami*(acc + nn[j])) % A2
        sig0 = (acc*pow((1 - lm) % A2, -1, A2)) % A2
        sig = [sig0]
        for j in range(m-1): sig.append((lami*(sig[-1] + nn[j])) % A2)
        assert (lami*(sig[-1] + nn[m-1]) - sig0) % A2 == 0
        inv2 = pow(2, -1, A2)
        br = (sum(nn[j]*sig[j] for j in range(m)) + inv2*sum(t*t for t in nn)) % A2
        tot += (P['gamma']*br % A2)/A2
    return (real + tot) % 1.0
