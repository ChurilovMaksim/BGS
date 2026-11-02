"""Debug: print concrete examples of nonzero collapsed digits at m=42
and of per-class collapsed failure at m=12, with full detail."""
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

def run(m, p, want):
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
    shown = 0
    for ms, As in fibres.items():
        A0 = As[0]
        for A1 in As[1:]:
            normed = None; kind = None; aj = (1, 0)
            for j in range(m):
                cand = mul(A1, aj, mod)
                if (cand[0] % p, cand[1] % p) == (A0[0] % p, A0[1] % p):
                    normed = cand; kind = f"shift{j}"; break
                cc = conj(cand, mod)
                if (cc[0] % p, cc[1] % p) == (A0[0] % p, A0[1] % p):
                    normed = cc; kind = f"conj{j}"; break
                aj = mul(aj, ainv, mod)
            if normed is None: continue
            for r in range(t):
                ar = pw(alpha, r, mod)
                rows = []
                for z in H0:
                    C = mul(mul(A0, ar, mod), z, mod)
                    Cp = mul(mul(normed, ar, mod), z, mod)
                    F = sorted(tr(mul(C, pw(gamma, j, mod), mod), mod)
                               for j in range(p))
                    Fp = sorted(tr(mul(Cp, pw(gamma, j, mod), mod), mod)
                                for j in range(p))
                    if len(set(F)) == 1:
                        d = ((Fp[0]-F[0]) % mod)//p % p
                        rows.append((z, F[0], Fp[0], d))
                coll0 = sorted(x[1] for x in rows)
                coll1 = sorted(x[2] for x in rows)
                nz = [x for x in rows if x[3] != 0]
                if want == "nz_exact_ok" and nz and coll0 == coll1:
                    print(f"m={m} p={p} A0={A0} A1={A1} norm={kind} class r={r}")
                    print(f"   collapsed rows (z, val0, val1, digit): {rows}")
                    shown += 1
                if want == "coll_fail" and coll0 != coll1:
                    print(f"m={m} p={p} A0={A0} A1={A1} norm={kind} class r={r}")
                    print(f"   collapsed rows (z, val0, val1, digit): {rows}")
                    print(f"   coll0={coll0} coll1={coll1}")
                    shown += 1
                if shown >= 3: return
    print(f"m={m} p={p} want={want}: shown {shown}")

run(42, 7, "nz_exact_ok")
run(12, 3, "coll_fail")
print("DONE")
