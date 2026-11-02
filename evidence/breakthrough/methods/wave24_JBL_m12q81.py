"""Wave 24, task 2: JBL rigidity at m=12, q=81 (p | m/P case).

Setup: R = Z[sqrt2], alpha = 3+2*sqrt2, beta = alpha^4, t = gcd(12,4) = 4,
q2 = 128 (v2(D12) = 7), q = 81, D12 = 2^7 * 3^4 * 5^2 * 7^2 * 11^2.
Genuine class parameter B mod 10368 satisfies (alpha^12 - 1) * B == 0.
Joint multiset J(B) = {(Tr(B) mod 128, Tr(B*beta^s) mod 81) : s in Z/3}.
D-related (up to trace-kernel): exists conj choice c, j, kernel eps with
  B' == c(B)*beta^j (mod 81)  and  B' == eps*c(B)*beta^j (mod 128)
(j mod 16 and j mod 27 are independent by CRT since gcd(16,27)=1).
All arithmetic exact integers. Repository untouched; no Lean build.
"""

def mul(a, b, M):
    return ((a[0]*b[0] + 2*a[1]*b[1]) % M, (a[0]*b[1] + a[1]*b[0]) % M)

def pw(a, n, M):
    r = (1, 0)
    while n:
        if n & 1:
            r = mul(r, a, M)
        a = mul(a, a, M)
        n >>= 1
    return r

def conj(a, M):
    return (a[0] % M, (-a[1]) % M)

def tr(a, M):
    return (2 * a[0]) % M

ALPHA = (3, 2)

def order(beta, M):
    cur = (1, 0)
    for k in range(1, 5000):
        cur = mul(cur, beta, M)
        if cur == (1, 0):
            return k
    return None

# --- sanity: orders of beta ---
for M in (81, 128):
    beta = pw(ALPHA, 4, M)
    print(f"beta mod {M} = {beta}, order = {order(beta, M)}")

# --- genuine parameters mod 128 and mod 81 ---
def genuine(M):
    delta = ((pw(ALPHA, 12, M)[0] - 1) % M, pw(ALPHA, 12, M)[1] % M)
    out = []
    for x in range(M):
        for y in range(M):
            if mul(delta, (x, y), M) == (0, 0):
                out.append((x, y))
    return out, delta

G128, d128 = genuine(128)
G81, d81 = genuine(81)
print(f"delta mod 128 = {d128}, genuine count = {len(G128)} (expect 128)")
print(f"delta mod 81  = {d81}, genuine count = {len(G81)} (expect 81)")
assert len(G128) == 128 and len(G81) == 81

# --- CRT combine to mod 10368 ---
M1, M2 = 128, 81
inv = pow(M1, -1, M2)
def crt(a1, a2):
    # x = a1 mod 128, x = a2 mod 81
    t = ((a2 - a1) * inv) % M2
    return (a1 + M1 * t) % (M1 * M2)

beta81 = pw(ALPHA, 4, 81)
beta128 = pw(ALPHA, 4, 128)
beta_pow81 = [pw(beta81, j, 81) for j in range(27)]
beta_pow128 = [pw(beta128, j, 128) for j in range(16)]
kernel = [(u, v) for u in (1, 65) for v in (0, 32, 64, 96)]

def joint(b128, b81):
    p = tr(b128, 128)
    ts = []
    cur = b81
    for _ in range(3):
        ts.append(tr(cur, 81))
        cur = mul(cur, beta81, 81)
    return (p, tuple(sorted(ts)))

def d_related(b128, b81, c128, c81):
    # shared conjugation choice c in {0: id, 1: conj}
    for c in (0, 1):
        x128 = conj(b128, 128) if c else b128
        x81 = conj(b81, 81) if c else b81
        for j81 in range(27):
            lhs81 = mul(x81, beta_pow81[j81], 81)
            if lhs81 != c81:
                continue
            for j128 in range(16):
                base = mul(x128, beta_pow128[j128], 128)
                for eps in kernel:
                    if mul(eps, base, 128) == c128:
                        return True
    return False

# --- full enumeration: group genuine B by J, check D-orbits ---
groups = {}
for b128 in G128:
    for b81 in G81:
        key = joint(b128, b81)
        groups.setdefault(key, []).append((b128, b81))
print(f"genuine B mod 10368: {len(G128)*len(G81)}, distinct J keys: {len(groups)}")

bad = []
for key, members in groups.items():
    b0 = members[0]
    for other in members[1:]:
        if not d_related(b0[0], b0[1], other[0], other[1]):
            bad.append((key, b0, other))
            break
print(f"J-groups containing a non-D-related pair: {len(bad)}")

# --- the explicit counterexample ---
B128 = (0, 0)
B81 = (0, 9)      # B = 9*sqrt2 mod 81
C128 = (0, 0)
C81 = (0, 36)     # B'' = 36*sqrt2 = 4*B mod 81
print("J(B)  =", joint(B128, B81))
print("J(B'')=", joint(C128, C81))
print("D-related (up to kernel)?", d_related(B128, B81, C128, C81))
# D-orbit of B mod 81, exhaustive
orbit = set()
for c in (0, 1):
    x = conj(B81, 81) if c else B81
    for j in range(27):
        orbit.add(mul(x, beta_pow81[j], 81))
print("B'' mod 81 in D-orbit of B mod 81?", C81 in orbit, "| orbit size:", len(orbit))

# --- global lift check: B, B'' mod D12 with 0 mod other prime powers ---
D12 = 2**7 * 3**4 * 5**2 * 7**2 * 11**2
def crt3(a10368, M=10368):
    # lift: residue a10368 mod 10368, 0 mod D12/10368
    N = D12 // M
    invN = pow(N, -1, M)
    t = ((a10368 - 0) * invN) % M
    return (N * t) % D12
B_full = (crt3(crt(B128[0], B81[0])), crt3(crt(B128[1], B81[1])))
C_full = (crt3(crt(C128[0], C81[0])), crt3(crt(C128[1], C81[1])))
delta_full = pw(ALPHA, 12, D12)
delta_full = ((delta_full[0] - 1) % D12, delta_full[1] % D12)
print("genuine mod D12: B:", mul(delta_full, B_full, D12) == (0, 0),
      " B'':", mul(delta_full, C_full, D12) == (0, 0))
print("B mod D12 =", B_full, " B'' mod D12 =", C_full)

if bad:
    key, b0, other = bad[0]
    print("first bad group key:", key)
    print("  member0 (mod128, mod81):", b0)
    print("  member1 (mod128, mod81):", other)
