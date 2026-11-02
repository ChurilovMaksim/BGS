"""Refined s=1 digit test (f=2): for normalised pairs (A'' == A mod p),
per class r check EXACT equality (not just D) of: full-coset part,
collapsed part, and total class multiset. For nonzero collapsed digits,
classify: flip-type (b == 0 mod p and d == -2*beta, beta = (b//p) mod p)
or other. Exact arithmetic in R = Z[sqrt2]."""
import itertools, math

def add(x, y, mod): return ((x[0]+y[0]) % mod, (x[1]+y[1]) % mod)
def mul(x, y, mod):
    return ((x[0]*y[0] + 2*x[1]*y[1]) % mod, (x[0]*y[1] + x[1]*y[0]) % mod)
def pw(x, n, mod):
    r = (1, 0)
    while n:
        if n & 1: r = mul(r, x, mod)
        x = mul(x, x, mod); n >>= 1
    return r
def tr(x, mod): return (2*x[0]) % mod
def conj(x, mod): return (x[0], (-x[1]) % mod)
def norm(x, mod): return (x[0]*x[0] - 2*x[1]*x[1]) % mod
def inv(x, mod):
    ni = pow(norm(x, mod) % mod, -1, mod)
    return ((x[0]*ni) % mod, ((-x[1])*ni) % mod)

for (m, p) in [(12, 3), (30, 5), (42, 7)]:
    mod = p**2; alpha = (3 % mod, 2 % mod); t = math.gcd(m, 4)
    a_p, g, L0 = (3 % p, 2 % p), (1, 0), 0
    while True:
        g = mul(g, a_p, p); L0 += 1
        if g == (1, 0): break
    gamma = pw(alpha, L0, mod)
    H0, g = [], (1, 0)
    gen = pw(alpha, t*p, mod)
    while True:
        H0.append(g); g = mul(g, gen, mod)
        if g == (1, 0): break
    def seq(A):
        out, gg = [], (1, 0)
        for _ in range(m):
            out.append(tr(mul(A, gg, mod), mod)); gg = mul(gg, alpha, mod)
        return tuple(out)
    fibres = {}
    for A in itertools.product(range(mod), repeat=2):
        fibres.setdefault(tuple(sorted(seq(A))), []).append(A)
    ainv = inv(alpha, mod)
    tot_pairs = 0; full_exact_fail = 0; coll_exact_fail = 0; total_exact_fail = 0
    nz = 0; flip = 0; other = 0; coll_pairs = 0
    for ms, As in fibres.items():
        A0 = As[0]
        for A1 in As[1:]:
            tot_pairs += 1
            normed = None; aj = (1, 0)
            for j in range(m):
                cand = mul(A1, aj, mod)
                if (cand[0] % p, cand[1] % p) == (A0[0] % p, A0[1] % p):
                    normed = cand; break
                cc = conj(cand, mod)
                if (cc[0] % p, cc[1] % p) == (A0[0] % p, A0[1] % p):
                    normed = cc; break
                aj = mul(aj, ainv, mod)
            if normed is None: continue
            for r in range(t):
                ar = pw(alpha, r, mod)
                full0, full1, coll0, coll1 = [], [], [], []
                for z in H0:
                    C = mul(mul(A0, ar, mod), z, mod)
                    Cp = mul(mul(normed, ar, mod), z, mod)
                    F = sorted(tr(mul(C, pw(gamma, j, mod), mod), mod)
                               for j in range(p))
                    Fp = sorted(tr(mul(Cp, pw(gamma, j, mod), mod), mod)
                                for j in range(p))
                    if len(set(F)) == 1:
                        coll_pairs += 1
                        coll0.append(F[0]); coll1.append(Fp[0])
                        d = ((Fp[0]-F[0]) % mod)//p % p
                        if d != 0:
                            nz += 1
                            b = F[0]
                            if b % p == 0 and d == (-2*(b//p)) % p: flip += 1
                            else: other += 1
                    else:
                        full0.extend(F); full1.extend(Fp)
                if sorted(full0) != sorted(full1): full_exact_fail += 1
                if sorted(coll0) != sorted(coll1): coll_exact_fail += 1
                if sorted(full0+coll0) != sorted(full1+coll1):
                    total_exact_fail += 1
    print(f"m={m} p={p} pairs={tot_pairs} full_exact_fail={full_exact_fail} "
          f"coll_exact_fail={coll_exact_fail} total_exact_fail={total_exact_fail} "
          f"coll_cosets={coll_pairs} nonzero_digits={nz} flip_type={flip} "
          f"other_type={other}")
print("DONE")
