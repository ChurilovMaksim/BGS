"""Direct (non-digit-formula) verification of the p=31 example A=(1,3), c=13,
plus structural checks of the p=31 twist setup. Exact integer arithmetic."""
P, M = 31, 961


def mul(x, y, m):
    return ((x[0] * y[0] + 2 * x[1] * y[1]) % m,
            (x[0] * y[1] + x[1] * y[0]) % m)


def pw(x, n, m):
    r = (1, 0)
    while n:
        if n & 1:
            r = mul(r, x, m)
        x = mul(x, x, m)
        n >>= 1
    return r


def tr(x, m):
    return (2 * x[0]) % m


alpha = (3, 2)
G = []
x = (1, 0)
while True:
    G.append(x)
    x = mul(x, alpha, M)
    if x == (1, 0):
        break
print(f"|G| mod 961 = {len(G)} (expect 15)")
print(f"alpha^15 mod 29791 = {pw(alpha, 15, 29791)} (expect (1,1922): k=2)")
Gset = set(G)

A = (1, 3)
c = 13
Ap = mul(A, (1, (31 * c) % M), M)
print(f"A={A}, twist c={c}, A'={Ap}")
base = sorted(tr(mul(A, z, M), M) for z in G)
tw = sorted(tr(mul(Ap, z, M), M) for z in G)
print("base orbit == twisted orbit (direct mul):", base == tw)
print("base orbit:", base)
# triviality: A' in A*G or Abar*G ?
Abar = (A[0], (-A[1]) % M)
in_AG = any(Ap == mul(A, z, M) for z in G)
in_AbarG = any(Ap == mul(Abar, z, M) for z in G)
print(f"A' in A*G: {in_AG}; A' in Abar*G: {in_AbarG}; genuine: {not (in_AG or in_AbarG)}")
# B-real?
B31 = pw((A[0] % P, A[1] % P), 15, P)
print(f"B = A^15 mod 31 = {B31}, B real: {B31[1] == 0}")
# second digits via direct values, and via digit formula
v1_base = sorted(((v - v % P) // P) for v in base)
v1_tw = sorted(((v - v % P) // P) for v in tw)
print("v1 marginals equal:", v1_base == v1_tw)
# digit-formula cross-check on this example
a, b = A
a31, b31 = a % P, b % P
ok = True
for z in G:
    v = tr(mul(A, z, M), M)
    t = (4 * (b31 * (z[0] % P) + a31 * (z[1] % P))) % P
    v0, v1 = v % P, (v - v % P) // P
    np_ = v1 + (c * t) % P
    if np_ >= P:
        np_ -= P
    if v0 + P * np_ not in tw:
        ok = False
print("digit-formula twisted values all present in direct twisted orbit:", ok)
# how many c preserve for this A, and are they all genuine?
pres = []
for cc in range(1, 31):
    Apc = mul(A, (1, (31 * cc) % M), M)
    twc = sorted(tr(mul(Apc, z, M), M) for z in G)
    if twc == base:
        gen = not (any(Apc == mul(A, z, M) for z in G) or
                   any(Apc == mul(Abar, z, M) for z in G))
        pres.append((cc, gen))
print(f"preserving c for A=(1,3): {pres}")
