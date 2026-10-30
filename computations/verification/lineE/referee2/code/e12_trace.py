"""Auditor: E12 trace law Z_m(nu_{a,s}) = (1-lambda^-m) sum_b c_b Tr L_b^m (a=7) vs brute-force n-sum with the TRUE phase,
own Galerkin construction on H^2(D_rho) x C^{49}, random complex weights on {-L..L}.  Also a=1 (E2) sanity and controls."""
import numpy as np, itertools, math, random
from math import comb, factorial
lam = 3 + 2*math.sqrt(2); c = 1/(lam - 1/lam)
def pell(d):
    x, y = 1, 0
    for _ in range(d): x, y = 3*x + 8*y, x + 3*y
    return x, y
def params(m, a, s, r):
    xm, ym = pell(m); h = int(round(math.sqrt((xm-1)//2))); yp = ym//h; a2 = a*a
    nu = (-s*pow(4*a2, -1, h)) % h
    if nu % 2 == 0: nu += h
    k = (4*a2*nu + s)//h; u = pow(a2, -1, 8); v = (1 - u*a2)//8
    kappa = (-k*u*yp) % 8
    if a == 1: return h, yp, nu, kappa, 0, 1
    l = (3 + 2*r) % a2; li = pow(l, -1, a2); B = ((2*yp + h*r)*pow(4, -1, a2)) % a2
    gamma = (-k*v*2*B*(1 - pow(li, m, a2))) % a2
    return h, yp, nu, kappa, gamma, li
def nsum(m, wts, L, h, yp, nu):
    gp = 2*h; tot = 0
    X = [pell(d)[0] for d in range(m)]
    for n in itertools.product(range(-L, L+1), repeat=m):
        Nm = sum(n[i]*n[j]*X[abs(i-j)] for i in range(m) for j in range(m))
        tot += np.prod([wts[x+L] for x in n])*np.exp(2j*np.pi*((-nu*yp*Nm) % gp)/gp)
    return tot
def law(m, wts, L, a, s, kappa, gamma, li, K=18, rho=0.6):
    a2 = a*a; i2 = pow(2, -1, a2) if a > 1 else 0
    tot = 0
    for b in range(0, 8, 2):
        cb = sum(np.exp(2j*np.pi*(kappa*bb*bb - b*bb)/8) for bb in range(8))/8
        A = np.zeros((K*a2, K*a2), complex)
        for n in range(-L, L+1):
            x = n/a
            Cm = np.zeros((K, K)); Mm = np.zeros((K, K), complex)
            for k in range(K):
                for j in range(k+1): Cm[j, k] = comb(k, j)*lam**(-k)*(x/rho)**(k-j)
            for i in range(K):
                for j in range(i+1): Mm[i, j] = (2j*np.pi*s*c*x*rho)**(i-j)/factorial(i-j)
            blk = Mm @ Cm
            for sg in range(a2):
                w = wts[n+L]*np.exp(2j*np.pi*(s*c*x*x/2 + b*n/8 + (gamma*(n*sg + i2*n*n) % a2)/a2))
                sp = (li*(sg + n)) % a2
                A[sg*K:(sg+1)*K, sp*K:(sp+1)*K] += w*blk
        ev = np.linalg.eigvals(A)
        tot += cb*np.sum(ev**m)
    return (1 - lam**(-m))*tot
if __name__ == '__main__':
    rnd = np.random.default_rng(7)
    for (m, L, a, s, r) in ((5, 2, 1, 1, 0), (5, 3, 7, 1, 10), (5, 3, 7, -1, 10), (5, 3, 7, 1, 39), (7, 2, 7, 1, 10), (7, 2, 7, -1, 39)):
        wts = (rnd.normal(size=2*L+1) + 1j*rnd.normal(size=2*L+1))*0.5
        h, yp, nu, kappa, gamma, li = params(m, a, s, r)
        Zb = nsum(m, wts, L, h, yp, nu)
        Zl = law(m, wts, L, a, s, kappa, gamma, li)
        Zc = law(m, wts, L, a, s, kappa, (gamma + 1) % (a*a), li) if a > 1 else np.nan
        print(f'm={m} L={L} a={a} s={s:+d} root={r} nu={nu} kappa={kappa} gamma={gamma}: |Zbrute-Zlaw|/|Z| = {abs(Zb-Zl)/abs(Zb):.2e}  (control gamma+1: {abs(Zb-Zc)/abs(Zb):.2e})', flush=True)
