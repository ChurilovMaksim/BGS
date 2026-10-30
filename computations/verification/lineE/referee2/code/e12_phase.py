"""Auditor: exact check of Theorem E12 phase identity using the theorem's OWN formulas for kappa, gamma
(kappa = -k u y' mod 8, gamma = -k v 2B(1-l^-m) mod a^2, B = iota((2y'+h sqrt2)/4)), against the true phase
-nu y' Nm(alpha_n)/g' computed from Nm(alpha_n)=sum n_i n_j x_|i-j| (integers), and real part s q(n)/(2a^2)
with q = n^T H^-1 n from exact rational inversion of H (sympy).  Random n.  Controls: wrong gamma / wrong kappa."""
import random, sys
from fractions import Fraction as Fr
import sympy
def pell(d):
    x, y = 1, 0
    for _ in range(d): x, y = 3*x + 8*y, x + 3*y
    return x, y
def frac(x): return x - (x.numerator // x.denominator)
def sqrt2_mod(a2, a):
    return [r for r in range(a2) if (r*r - 2) % a2 == 0]
def run(m, a, s, root, Hinv, trials=25, rnd=random.Random(1)):
    xm, ym = pell(m); D = 2*(xm - 1); h = sympy.integer_nthroot(D//4, 2)[0]; assert 4*h*h == D
    assert ym % h == 0; yp = ym//h; gp = 2*h; assert h*h + 1 == 2*yp*yp
    a2 = a*a
    if sympy.gcd(a, 2*h) != 1: return 'skip-gcd'
    # nu: odd lift of -s (4a^2)^-1 mod h
    nu = (-s*pow(4*a2, -1, h)) % h
    if nu % 2 == 0: nu += h
    assert (4*a2*nu + s) % h == 0; k = (4*a2*nu + s)//h
    u = pow(a2, -1, 8); v = Fr(1 - u*a2, 8); assert v.denominator == 1; v = int(v)
    kappa = (-k*u*yp) % 8; assert kappa % 2 == 1
    r = root; i2 = pow(2, -1, a2); i4 = pow(4, -1, a2)
    l = (3 + 2*r) % a2
    for p in sympy.factorint(a):
        if pow(l, m, p) == 1: return 'skip-(ii)'
    li = pow(l, -1, a2)
    B = ((2*yp + h*r) * i4) % a2
    gamma = (-k*v*2*B*(1 - pow(li, m, a2))) % a2
    ok = True
    for _ in range(trials):
        n = [rnd.randint(-9, 9) for _ in range(m)]
        Nm = sum(n[i]*n[j]*pell(abs(i-j))[0] for i in range(m) for j in range(m))
        lhs = frac(Fr(-nu*yp*Nm, gp))
        q = sum(n[i]*Hinv[i, j]*n[j] for i in range(m) for j in range(m)); q = Fr(int(q.p), int(q.q))
        # sigma: unique periodic orbit of sigma -> li (sigma + n_j) mod a^2
        c0 = 0
        for j in range(m): c0 = (li*(c0 + n[j])) % a2          # sigma_m = l^-m sigma_0 + c0
        inv1 = pow((1 - pow(li, m, a2)) % a2, -1, a2); sig = [(c0*inv1) % a2]
        for j in range(m - 1): sig.append((li*(sig[-1] + n[j])) % a2)
        assert (li*(sig[-1] + n[m-1]) - sig[0]) % a2 == 0
        g_term = Fr(gamma*(sum(n[j]*sig[j] for j in range(m)) + i2*sum(x*x for x in n)), a2)
        rhs = frac(Fr(s, 2*a2)*q + Fr(kappa*sum(n)**2, 8) + g_term)
        bad_g = frac(Fr(s, 2*a2)*q + Fr(kappa*sum(n)**2, 8) + Fr((gamma+1)*(sum(n[j]*sig[j] for j in range(m)) + i2*sum(x*x for x in n)), a2))
        ok &= (lhs == rhs)
    return dict(ok=ok, nu=nu, k=k, kappa=kappa, gamma=gamma, ctrl_wrong_gamma_differs=(bad_g != rhs))
if __name__ == '__main__':
    out = []
    for m in range(5, 26, 2):
        H = sympy.zeros(m, m)
        for i in range(m): H[i, i] = 6; H[i, (i+1) % m] -= 1; H[i, (i-1) % m] -= 1
        Hinv = H.inv()
        for a in (1, 7, 17, 23, 31):
            roots = sqrt2_mod(a*a, a) if a > 1 else [0]
            for r in roots:
                for s in (1, -1):
                    res = run(m, a, s, r, Hinv)
                    print(m, a, r, s, res, flush=True)
