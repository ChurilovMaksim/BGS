"""Wave 13, task 1 (f=2 only): numerical checks for the G1' proof at f=2.
Exact integer arithmetic in R = Z[sqrt(2)] mod p^2. No Lean, no repo.
(1) Polynomial identity for the coprime-to-p subgroup H (s=0 case):
    prod_{z in H} (X - Tr(Cz)) = u * (V_H(X, N(C)) - Tr(C^H))
    with u a unit independent of C (checked: u = +/-1 pattern below).
(2) f=2, s=1 case m=12, p=3: per-class check + count of fibres in which
    a real-Cz configuration occurs mod p (imaginary part 0 mod p).
"""
import itertools, random

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
def norm(x, mod): return (x[0]*x[0] - 2*x[1]*x[1]) % mod

def poly_mul(a, b, mod):
    c = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] = (c[i+j] + x*y) % mod
    return c

def lucas_V(n, N, mod):
    # V_0=2, V_1=X, V_{k+1}=X V_k - N V_{k-1}; coeffs low->high in X
    if n == 0: return [2 % mod]
    if n == 1: return [0, 1]
    vm, v = [2 % mod], [0, 1]
    for _ in range(2, n+1):
        nxt = [0]*(len(v)+1)
        for i, c in enumerate(v): nxt[i+1] = (nxt[i+1] + c) % mod
        for i, c in enumerate(vm): nxt[i] = (nxt[i] - N*c) % mod
        vm, v = v, nxt
    return v

def subgroup_coprime_part(alpha, mod, p):
    # full group <alpha> mod mod; return subgroup of order coprime to p
    G, g = [], (1, 0)
    while True:
        G.append(g); g = mul(g, alpha, mod)
        if g == (1, 0): break
    s = 0
    while len(G) % p == 0:
        s += 1; G = [pw(x, p, mod) for x in G]
        # dedupe preserving order
        seen, H = set(), []
        for x in G:
            if x not in seen: seen.add(x); H.append(x)
        G = H
    return G

print("=== (1) polynomial identity, s=0-type subgroups ===")
for p, mod in [(7, 49), (5, 25)]:
    alpha = (3 % mod, 2 % mod)
    H = subgroup_coprime_part(alpha, mod, p)
    h = len(H)
    ok = True; ratios = set()
    for _ in range(30):
        C = (random.randrange(mod), random.randrange(mod))
        # LHS = prod (X - Tr(Cz))
        lhs = [1]
        for z in H:
            lhs = poly_mul(lhs, [(-tr(mul(C, z, mod), mod)) % mod, 1], mod)
        N = norm(C, mod)
        V = lucas_V(h, N, mod)
        rhs = [(V[i] - (tr(pw(C, h, mod), mod) if i == 0 else 0)) % mod
               for i in range(len(V))]
        # find unit u with lhs == u*rhs (compare leading and constant coeffs)
        # leading coeff of lhs is 1; of rhs is 1 -> u must be 1, or rhs sign-flip
        if lhs == rhs:
            ratios.add(1)
        elif lhs == [(-c) % mod for c in rhs]:
            ratios.add(-1)
        else:
            ok = False; print("  MISMATCH p=", p, "C=", C); break
    print(f"  p={p} mod={mod} |H|={h} identity holds: {ok} signs seen: {ratios}")

print("=== (2) m=12, p=3, f=2: orders, real-Cz occurrence, per-class check ===")
p, f, m = 3, 2, 12
mod = p**f  # 9
alpha = (3 % mod, 2 % mod)
# order of alpha mod 3 (in R/3): work mod 3
a3, g, L0 = (0, 2), (1, 0), 0  # alpha mod 3 = (0,2) since 3==0
while True:
    g = mul(g, a3, 3); L0 += 1
    if g == (1, 0): break
print(f"  L0 (order mod 3) = {L0}")
# k = v_p(alpha^L0 - 1) in R: valuation = min v_p of coeffs of alpha^L0-1
d = add(pw(alpha, L0, mod*mod), (-1 % (mod*mod), 0), mod*mod)
# compute alpha^L0 - 1 over integers exactly (small): use exact R arithmetic
def mulZ(x, y): return (x[0]*y[0]+2*x[1]*y[1], x[0]*y[1]+x[1]*y[0])
def pwZ(x, n):
    r = (1, 0)
    while n:
        if n & 1: r = mulZ(r, x)
        x = mulZ(x, x); n >>= 1
    return r
e = pwZ((3, 2), L0); e = (e[0]-1, e[1])
def vp(n, pr):
    c = 0
    while n % pr == 0 and n != 0: n //= pr; c += 1
    return c
k = min(vp(e[0], p), vp(e[1], p)) if e != (0, 0) else 99
print(f"  alpha^L0 - 1 = {e}, k = {k}, s = f - k = {f-k} (expect s=1)")

# sequences mod 9, m=12: y_i = Tr(A alpha^i)
def seq(A):
    out, g = [], (1, 0)
    for _ in range(m):
        out.append(tr(mul(A, g, mod), mod)); g = mul(g, alpha, mod)
    return tuple(out)
t = 4
def d4_related(M1, M2):
    # M: tuple of 4 class multisets (sorted tuples); check some pi in D4 maps
    for b in range(4):
        for sgn in (1, -1):
            if all(tuple(sorted(M2[(sgn*r+b) % 4])) == tuple(sorted(M1[r]))
                   for r in range(4)):
                return True
    return False
fibres = {}
for A in itertools.product(range(mod), repeat=2):
    y = seq(A)
    fibres.setdefault(tuple(sorted(y)), []).append(y)
bad = 0; real_fibres = 0; total = 0
H0 = subgroup_coprime_part(alpha, mod, p)  # not used for classes; classes direct
for ms, ys in fibres.items():
    total += 1
    # per-class multisets of first vector vs all others
    def classes(y):
        return [tuple(sorted(y[i] for i in range(m) if i % t == r)) for r in range(t)]
    M0 = classes(ys[0])
    for y in ys[1:]:
        if not d4_related(M0, classes(y)): bad += 1
    # real-Cz occurrence: some A' in this fibre and some z in H0 with
    # (A' * z) having imaginary part 0 mod 3? Use class values: some sequence
    # value-pair... simpler: some A in fibre with A itself real mod 3
    # (imag 0) or A*alpha^j real mod 3 for some j (i.e. some Cz real mod p).
    found = False
    for y in ys:
        pass
    # recompute A values from fibre members is not stored; redo via A scan:
    # (done below in second pass)
print(f"  fibres={total} bad_perclass_pairs={bad}")
# second pass: real-Cz occurrence per fibre (by A)
fibA = {}
for A in itertools.product(range(mod), repeat=2):
    fibA.setdefault(tuple(sorted(seq(A))), []).append(A)
real_fibres = 0
for ms, As in fibA.items():
    occ = False
    for A in As:
        g = (1, 0)
        for _ in range(m):
            Cz = mul(A, g, mod)
            if Cz[1] % p == 0: occ = True; break
            g = mul(g, alpha, mod)
        if occ: break
    if occ: real_fibres += 1
print(f"  fibres containing a real-Cz (imag==0 mod 3) configuration: "
      f"{real_fibres}/{total}")
print("DONE")
