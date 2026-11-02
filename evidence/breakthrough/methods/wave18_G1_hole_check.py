"""Wave 18, task 3: does the second-digit distribution distinguish the
twisted case in the G1 f=2 s=0 hole at p=13?

Setup (see wave16_G1_f2s0.md §5): R = Z[sqrt2], p=13, modulus p^2=169.
alpha = 3+2*sqrt2 has order 14 mod 13 and mod 169 (s=0).
G = <alpha> mod 169 (14 elements); H0 = <alpha^2> (7 elements, t=2 case).
Twist: A' = A*(1+13*f) with f purely imaginary mod 13, f != 0
(zeta in G is irrelevant: it permutes the orbit).
Gap case: B = A^14 real mod 13 (b-component 0 mod 13), where power
sums up to order L0 cannot see the twist.
Test: for every unit A mod 169 with B real mod 13, and every c=1..12,
is the orbit multiset {Tr(A'z)} equal to {Tr(Az)} mod 169?
Second digit: v = v0 + 13*v1, v0 = v mod 13, v1 in 0..12.
"""
from collections import Counter

P = 13
M = 169


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
for _ in range(14):
    G.append(x)
    x = mul(x, alpha, M)
a2 = mul(alpha, alpha, M)
H0 = []
x = (1, 0)
for _ in range(7):
    H0.append(x)
    x = mul(x, a2, M)
assert len(set(G)) == 14 and len(set(H0)) == 7


def orbit_multiset(A, grp):
    return sorted(tr(mul(A, z, M), M) for z in grp)


def digits(vals):
    return Counter(((v % P, (v - v % P) // P) for v in vals))


n_units = 0
n_Breal = 0
eq_G = []   # (A, c) with G-orbit multisets equal under twist
eq_H0 = []  # (A, c) with H0-orbit multisets equal under twist
example = None
for a in range(M):
    for b in range(M):
        if (a * a - 2 * b * b) % P == 0:
            continue
        n_units += 1
        A = (a, b)
        B = pw(A, 14, P)
        if B[1] % P != 0:
            continue
        n_Breal += 1
        base_G = orbit_multiset(A, G)
        base_H = orbit_multiset(A, H0)
        for c in range(1, P):
            Ap = mul(A, (1, (P * c) % M), M)
            if orbit_multiset(Ap, G) == base_G:
                eq_G.append((A, c))
            if orbit_multiset(Ap, H0) == base_H:
                eq_H0.append((A, c))
        if example is None and base_G:
            Ap = mul(A, (1, P), M)
            example = (A, base_G, orbit_multiset(Ap, G))

print(f"units mod 169: {n_units}")
print(f"units with B=A^14 real mod 13: {n_Breal}")
print(f"G-orbit multiset equalities under nonzero twist: {len(eq_G)}")
print(f"H0-orbit multiset equalities under nonzero twist: {len(eq_H0)}")
if eq_G[:5]:
    print("  first G equalities:", eq_G[:5])
if eq_H0[:5]:
    print("  first H0 equalities:", eq_H0[:5])

# Representative second-digit distributions (first B-real A, twist c=1)
A, base, tw = example
print(f"\nRepresentative A={A} (B real mod 13), twist c=1:")
print("  untwisted orbit values:", base)
print("  twisted   orbit values:", tw)
print("  untwisted v1 marginal:", sorted(Counter((v - v % P) // P for v in base).items()))
print("  twisted   v1 marginal:", sorted(Counter((v - v % P) // P for v in tw).items()))
cu = Counter((v % P, (v - v % P) // P) for v in base)
ct = Counter((v % P, (v - v % P) // P) for v in tw)
diff = {k: (cu.get(k, 0), ct.get(k, 0)) for k in set(cu) | set(ct) if cu.get(k, 0) != ct.get(k, 0)}
print(f"  (v0,v1) cells differing: {len(diff)} of {len(set(cu) | set(ct))}")
for k in sorted(diff)[:10]:
    print(f"    (v0,v1)={k}: untwisted {diff[k][0]}, twisted {diff[k][1]}")
