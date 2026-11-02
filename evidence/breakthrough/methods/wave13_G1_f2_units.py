"""Unit-case s=1 digit test (f=2): restrict to pairs where A0 is a unit
mod p (norm not 0 mod p). Normalisation is then unique. Per class r check
EXACT equality of full part, collapsed part, total; classify nonzero
collapsed digits as flip-type or other. Exact arithmetic in R=Z[sqrt2]."""
import itertools, math

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
        if norm(A, mod) % p == 0: continue  # divisible / non-unit: induction case
        fibres.setdefault(tuple(sorted(seq(A))), []).append(A)
    ainv = inv(alpha, mod)
    pairs = 0; full_fail = 0; coll_fail = 0; tot_fail = 0
    nz = 0; flip = 0; other = 0; coll_n = 0; norm_fail = 0
    for ms, As in fibres.items():
        A0 = As[0]
        for A1 in As[1:]:
            pairs += 1
            normed = None; aj = (1, 0)
            for j in range(m):
                cand = mul(A1, aj, mod)
                if (cand[0] % p, cand[1] % p) == (A0[0] % p, A0[1] % p):
                    normed = cand; break
                cc = conj(cand, mod)
                if (cc[0] % p, cc[1] % p) == (A0[0] % p, A0[1] % p):
                    normed = cc; break
                aj = mul(aj, ainv, mod)
            if normed is None: norm_fail += 1; continue
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
                        coll_n += 1; coll0.append(F[0]); coll1.append(Fp[0])
                        d = ((Fp[0]-F[0]) % mod)//p % p
                        if d != 0:
                            nz += 1; b = F[0]
                            if b % p == 0 and d == (-2*(b//p)) % p: flip += 1
                            else: other += 1
                    else:
                        full0.extend(F); full1.extend(Fp)
                if sorted(full0) != sorted(full1): full_fail += 1
                if sorted(coll0) != sorted(coll1): coll_fail += 1
                if sorted(full0+coll0) != sorted(full1+coll1): tot_fail += 1
    print(f"m={m} p={p} UNIT pairs={pairs} norm_fail={norm_fail} "
          f"full_fail={full_fail} coll_fail={coll_fail} tot_fail={tot_fail} "
          f"coll_cosets={coll_n} nonzero_digits={nz} flip={flip} other={other}")
print("DONE")
