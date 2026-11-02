"""Wave 13, task 1, s=1 digit mechanism (f=2): for pairs (A,A') mod p^2 with
the same global multiset, normalise A' (shift/conjugation) so A' == A mod p,
write A' = A + pE, and check, for every class r and z in H0:
  - non-collapsed F-cosets: F(C') == F(C) as multisets (rigidity);
  - collapsed F-cosets: digit d = (value' - value)/p mod p; count nonzero d.
Also re-checks per-class D-relation. Exact arithmetic in R = Z[sqrt2].
"""
import itertools, math

def add(x, y, mod): return ((x[0]+y[0]) % mod, (x[1]+y[1]) % mod)
def sub(x, y, mod): return ((x[0]-y[0]) % mod, (x[1]-y[1]) % mod)
def mul(x, y, mod):
    return ((x[0]*y[0] + 2*x[1]*y[1]) % mod, (x[0]*y[1] + x[1]*y[0]) % mod)
def pw(x, n, mod):
    r = (1, 0)
    while n:
        if n & 1: r = mul(r, x, mod)
        x = mul(x, x, mod); n >>= 1
    return r
def tr(x, mod): return (2*x[0]) % mod
def norm(x, mod): return (x[0]*x[0] - 2*x[1]*x[1]) % mod
def conj(x, mod): return (x[0], (-x[1]) % mod)
def inv(x, mod):
    n = norm(x, mod) % mod
    ni = pow(n, -1, mod)
    return ((x[0]*ni) % mod, ((-x[1])*ni) % mod)
def mulZ(x, y): return (x[0]*y[0]+2*x[1]*y[1], x[0]*y[1]+x[1]*y[0])
def pwZ(x, n):
    r = (1, 0)
    while n:
        if n & 1: r = mulZ(r, x)
        x = mulZ(x, x); n >>= 1
    return r
def vp(n, pr):
    c = 0
    while n != 0 and n % pr == 0: n //= pr; c += 1
    return c

def d4_related(M1, M2, t):
    for b in range(t):
        for sgn in (1, -1):
            if all(tuple(sorted(M2[(sgn*r+b) % t])) == tuple(sorted(M1[r]))
                   for r in range(t)):
                return True
    return False

for (m, p) in [(12, 3), (30, 5), (42, 7), (14, 13)]:
    f = 2; mod = p**f; alpha = (3 % mod, 2 % mod)
    t = math.gcd(m, 4)
    # L0 = order of alpha mod p; k = v_p(alpha^L0 - 1) over Z
    a_p, g, L0 = (3 % p, 2 % p), (1, 0), 0
    while True:
        g = mul(g, a_p, p); L0 += 1
        if g == (1, 0): break
    e = pwZ((3, 2), L0); e = (e[0]-1, e[1])
    k = min(vp(e[0], p), vp(e[1], p)); s = f - k
    gamma = pw(alpha, L0, mod)          # = 1 + p*u mod p^2
    u = ((gamma[0]-1)//p % p, (gamma[1]//p) % p) if gamma[1] % p == 0 else None
    # H0 = <alpha^{t*p^s}> mod p^2
    H0, g = [], (1, 0)
    gen = pw(alpha, t*(p**s), mod)
    while True:
        H0.append(g); g = mul(g, gen, mod)
        if g == (1, 0): break
    def seq(A):
        out, gg = [], (1, 0)
        for _ in range(m):
            out.append(tr(mul(A, gg, mod), mod)); gg = mul(gg, alpha, mod)
        return tuple(out)
    def classes(y):
        return [tuple(sorted(y[i] for i in range(m) if i % t == r))
                for r in range(t)]
    fibres = {}
    for A in itertools.product(range(mod), repeat=2):
        fibres.setdefault(tuple(sorted(seq(A))), []).append(A)
    bad = 0; pairs = 0; nz_digit = 0; full_mismatch = 0; norm_fail = 0
    ainv = inv(alpha, mod)
    for ms, As in fibres.items():
        A0 = As[0]; M0 = classes(seq(A0))
        for A1 in As[1:]:
            pairs += 1
            if not d4_related(M0, classes(seq(A1)), t): bad += 1
            # normalise: find j, cflag with A1*alpha^{-j} == A0 (mod p) or conj
            normed = None
            aj = (1, 0)
            for j in range(m):
                cand = mul(A1, aj, mod)
                if (cand[0] % p, cand[1] % p) == (A0[0] % p, A0[1] % p):
                    normed = cand; break
                cc = conj(cand, mod)
                if (cc[0] % p, cc[1] % p) == (A0[0] % p, A0[1] % p):
                    normed = cc; break
                aj = mul(aj, ainv, mod)
            if normed is None:
                norm_fail += 1; continue
            # E = (normed - A0)/p in R/p
            E = (((normed[0]-A0[0]) % mod)//p % p,
                 ((normed[1]-A0[1]) % mod)//p % p)
            # digit check over classes r and z in H0
            for r in range(t):
                ar = pw(alpha, r, mod)
                for z in H0:
                    C = mul(mul(A0, ar, mod), z, mod)
                    Cp = mul(mul(normed, ar, mod), z, mod)
                    F = sorted(tr(mul(C, pw(gamma, j, mod), mod), mod)
                               for j in range(p))
                    Fp = sorted(tr(mul(Cp, pw(gamma, j, mod), mod), mod)
                                for j in range(p))
                    if len(set(F)) == 1:  # collapsed
                        d = ((Fp[0]-F[0]) % mod)//p % p
                        if d != 0: nz_digit += 1
                    else:
                        if F != Fp: full_mismatch += 1
    print(f"m={m} p={p} L0={L0} k={k} s={s} |H0|={len(H0)} "
          f"fibres={len(fibres)} pairs={pairs} bad_perclass={bad} "
          f"norm_fail={norm_fail} full_mismatch={full_mismatch} "
          f"nonzero_collapsed_digits={nz_digit}")
print("DONE")
