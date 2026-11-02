"""Check the R50 mod-p^2 step: r=2 power sum for C' = C(1+p^2 eta) mod p^5.

R = Z[sqrt(2)] as pairs (a,b). H = Teichmueller lift of <alpha> mod p,
alpha = 3+2*sqrt(2), of order n coprime to p. Predicts:
  pure eta = b*sqrt(2) FAILS the r=2 power sum mod p^5 unless b = 0 mod p;
  corrected eta = b*sqrt(2) + p^2*(b mod p)^2 PASSES it always.
"""
import random

def add(x, y, m): return ((x[0]+y[0]) % m, (x[1]+y[1]) % m)
def mul(x, y, m): return ((x[0]*y[0]+2*x[1]*y[1]) % m, (x[0]*y[1]+x[1]*y[0]) % m)
def pw(x, e, m):
    r = (1, 0)
    while e:
        if e & 1: r = mul(r, x, m)
        x = mul(x, x, m); e >>= 1
    return r
def tr(x): return (2*x[0])  # trace of a+b*sqrt2, kept unreduced where needed
def norm(x, m): return (x[0]*x[0]-2*x[1]*x[1]) % m

def teich(alpha, p, k):
    """Hensel-lift alpha (order n coprime to p mod p) to a root of x^n-1 mod p^k."""
    m = p
    x = (alpha[0] % p, alpha[1] % p)
    # order of alpha mod p
    n = 1
    y = x
    while y != (1, 0):
        y = mul(y, x, p); n += 1
        assert n < 100
    for _ in range(k-1):
        m *= p
        # Newton for f = x^n - 1, f' = n*x^(n-1), unit mod p
        f = (pw(x, n, m)[0]-1) % m, pw(x, n, m)[1] % m
        fp = (n % m, 0)
        fp = mul(fp, pw(x, n-1, m), m)
        inv = pow(fp[0]*fp[0]-2*fp[1]*fp[1], -1, m)  # norm inverse, fp is real
        # fp real => inverse is (fp0/norm, 0); general: use conjugate/norm
        invf = ((fp[0]*inv) % m, (-fp[1]*inv) % m)
        step = mul(f, invf, m)
        x = ((x[0]-step[0]) % m, (x[1]-step[1]) % m)
    return x, n

def run(p, trials, seed):
    random.seed(seed)
    k = 5
    mod = p**k
    beta, n = teich((3, 2), p, k)
    assert pw(beta, n, mod) == (1, 0) and pw(beta, 2, mod) != (1, 0), (p, n)
    H = [(1, 0)]
    for _ in range(n-1): H.append(mul(H[-1], beta, mod))
    pure_fail = pure_pass = corr_fail = 0
    for _ in range(trials):
        while True:
            C = (random.randrange(mod), random.randrange(mod))
            if norm(C, p) % p != 0: break
        b = random.randrange(p**3)
        b0 = b % p
        for eta, kind in [((0, b), 'pure'), ((p*p*b0*b0 % mod, b), 'corr')]:
            Cp = mul(C, add((1, 0), mul((p*p % mod, 0), eta, mod), mod), mod)
            s = sum(tr(mul(C, h, mod))**2 for h in H) % mod
            sp = sum(tr(mul(Cp, h, mod))**2 for h in H) % mod
            ok = (s == sp)
            if kind == 'pure':
                if b0 != 0 and ok: pure_pass += 1  # unexpected pass
                if b0 != 0 and not ok: pure_fail += 1
                if b0 == 0 and not ok: print("UNEXPECTED pure fail b0=0", p)
            else:
                if not ok: corr_fail += 1
    print(f"p={p} n={n} trials={trials}: pure(b0!=0) fail={pure_fail} "
          f"unexpected-pass={pure_pass} corrected fail={corr_fail}")
    assert pure_pass == 0 and corr_fail == 0

run(5, 40, 1)
run(7, 20, 2)
print("ALL CHECKS PASS")
