"""Wave 34, task 5: exact check of the F2 counterexample at m=816, qt=17^4.
Split coordinates mod 289: sqrt(2) = 244, alpha_1 = 3+2*244 = 202,
alpha_2 = 3-2*244 = 93. C = (c1, c2) means Tr(C alpha^j) = c1*a1^j + c2*a2^j.
"""
from collections import Counter

p, f, m = 17, 2, 816
q = p ** (2 * f)  # 83521, not used directly; trace model lives mod p^f = 289
mod = p ** f  # 289

# --- 1. v_17(D_816) = 4 via the t-recurrence t_0=2, t_1=6, t_{n+1}=6 t_n - t_{n-1}
t0, t1 = 2, 6
for _ in range(m - 1):
    t0, t1 = t1, 6 * t1 - t0
Dm = t1 - 2  # t_m - 2
v = 0
x = Dm
while x % p == 0:
    x //= p
    v += 1
print("v_17(D_816) =", v)
assert v == 4

# --- 2. split data mod 289
s = 244
assert (s * s) % mod == 2
a1 = (3 + 2 * s) % mod  # 202
a2 = (3 - 2 * s) % mod  # 93
assert (a1 * a2) % mod == 1
assert pow(a1, 136, mod) == 1 and pow(a1, 68, mod) != 1 and pow(a1, 8, mod) != 1
assert pow(a1, m, mod) == 1
a1_8 = pow(a1, 8, mod)
a2_8 = pow(a2, 8, mod)
assert a1_8 % p == 1 and a1_8 != 1  # e = 1: alpha^8 = 1 + 17*u, u unit
u1 = ((a1_8 - 1) // p) % p
u2 = ((a2_8 - 1) // p) % p
assert u1 != 0 and u2 != 0 and (u1 + u2) % p == 0
print("a1 =", a1, "a2 =", a2, "ord 136 ok, u1 =", u1, "u2 =", u2)

# precompute powers
a1pow = [1] * m
a2pow = [1] * m
for j in range(1, m):
    a1pow[j] = (a1pow[j - 1] * a1) % mod
    a2pow[j] = (a2pow[j - 1] * a2) % mod


def multiset(c1, c2):
    return Counter((c1 * a1pow[j] + c2 * a2pow[j]) % mod for j in range(m))


def orbit(c1, c2):
    # Gamma-orbit as C-values: shifts C*alpha^j (period 136) + reversals Cbar*alpha^j
    o = set()
    for j in range(136):
        o.add((c1 * a1pow[j] % mod, c2 * a2pow[j] % mod))
        o.add((c2 * a1pow[j] % mod, c1 * a2pow[j] % mod))
    return o


# --- 3. the counterexample: C0 = (1,0) vs C' = (1,17)
C0 = (1, 0)
Cp = (1, 17)
assert multiset(*C0) == multiset(*Cp), "multisets differ!"
assert Cp not in orbit(*C0), "C' is in the orbit!"
print("C0 vs C': same multiset, C' NOT in Gamma-orbit of C0 -> F2 single-orbit FALSE")
print("orbit size of C0:", len(orbit(*C0)))

# --- 4. B_{j0} != 0 for C0 (line argument), and all 289 lifts of class (1,0) share
a1bar, a2bar = a1 % p, a2 % p
for j0 in range(8):
    assert (u1 * pow(a1bar, j0, p)) % p != 0
base = multiset(*C0)
for e1 in range(p):
    for e2 in range(p):
        assert multiset(1 + p * e1, p * e2) == base
print("all 289 lifts of class (1,0) share the multiset")

# --- 5. full fiber of C0: 16 mod-17 classes x 289 lifts, orbit count
a1b = [pow(a1bar, j, p) for j in range(8)]
a2b = [pow(a2bar, j, p) for j in range(8)]
classes = set()
for j in range(8):
    classes.add((a1b[j], 0))
    classes.add((0, a2b[j]))
assert len(classes) == 16
fiber = []
for (r1, r2) in classes:
    for e1 in range(p):
        for e2 in range(p):
            c1, c2 = r1 + p * e1, r2 + p * e2
            assert multiset(c1, c2) == base
            fiber.append((c1, c2))
print("fiber size:", len(fiber))
assert len(fiber) == 16 * 289 == 4624
# orbit count via canonical representative
canon = set()
for (c1, c2) in fiber:
    canon.add(min(orbit(c1, c2)))
print("distinct Gamma-orbits in fiber:", len(canon))
assert len(canon) == 17

# --- 6. supporting case C=(1,2): D_{j0} != 0, all 289 lifts share
for j0 in range(8):
    d = (pow(a1bar, j0, p) - 2 * pow(a2bar, j0, p)) % p
    assert d != 0
base12 = multiset(1, 2)
for e1 in range(p):
    for e2 in range(p):
        assert multiset(1 + p * e1, 2 + p * e2) == base12
print("C=(1,2): D != 0, all 289 lifts share the multiset")
print("ALL CHECKS PASS")
