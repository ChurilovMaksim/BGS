"""Exact coefficient-level check of the a=7 law (the statement certified in Lean by cert49), and emission of Lean literals.
phase(n) = -nu y' Nm(alpha_n)/g'  ==  q(n)/98 + kappa (sum n)^2/8 + (gamma/49)[sum_i n_i sig_i + (1/2) sum n_i^2]   (mod 1)
coefficientwise: diag  -nu y'/g'        == X0/(98D) + kappa/8 + gamma*(Mt_m + inv2)/49
                 pair  -2 nu y' x_d/g'  == 2Xd/(98D) + kappa/4 + gamma*(Mt_d + Mt_{m-d})/49,   Mt_k = li^k (1-li^m)^{-1} mod 49."""
from fractions import Fraction as Fr
from lawlib import *
def frac1(x): return x - (x.numerator // x.denominator)
def check(m, s, r):
    d = mdata(m); h, yp, gp, D = d['h'], d['yp'], d['gp'], d['D']; xm, ym = d['xm'], d['ym']
    P = law_params(m, 7, s, r); nu, kap, gam, li = P['nu'], P['kappa'], P['gamma'], P['lami']
    X = lambda dd: ym if dd == 0 else ym*pell(dd)[0] - (xm - 1)*pell(dd)[1]
    inv = pow((1 - pow(li, m, 49)) % 49, -1, 49); Mt = lambda k: (pow(li, k, 49)*inv) % 49; inv2 = 25
    ok = frac1(Fr(-nu*yp, gp) - s*Fr(X(0), 98*D) - Fr(kap, 8) - Fr(gam*(Mt(m) + inv2), 49)) == 0
    for dd in range(1, m):
        ok &= frac1(Fr(-2*nu*yp*pell(dd)[0], gp) - s*Fr(2*X(dd), 98*D) - Fr(kap, 4) - Fr(gam*(Mt(dd) + Mt(m - dd)), 49)) == 0
    return ok, P
if __name__ == '__main__':
    for m in (5, 7, 11, 13, 17, 19, 23, 25, 29, 31, 35, 37, 41):
        for s in (1, -1):
            for r in (10, 39):
                ok, P = check(m, s, r)
                print(f'm={m} s={s:+d} root={r} nu={P["nu"]} kappa={P["kappa"]} gamma={P["gamma"]} lami={P["lami"]} exact_ok={ok}')
