"""Wave 42, task 4: 3-part SCL bound.

Part A: exact mod-3 computation proving N(b) = 1 for p = 3.
  alpha = 3 + 2*sqrt(2). d = ord_3(alpha) = 4, e = v_3(alpha^4 - 1) = 1,
  b = 2, u = (alpha^4 - 1)/3 mod 3 = sqrt(2).
  Level-b analysis (wave 35 f'=2): split fibers at level b <-> Gamma-orbits
  mod 3 with Z = empty, where Z = {j0 : Tr(C alpha^j0 u) = 0 mod 3}.
  Tr((x + y sqrt2) sqrt2) = 4y == y (mod 3), so B_j0 = y-coeff of C alpha^j0.
Part B: trace-model censuses (wave35_tm_census.tm_census) at
  (12,3,2), (36,3,3), (108,3,4) [controls] and (324,3,5) [new].
  Tower prediction: N(f) <= (f-1)*N(b) = f-1, i.e. 1, 2, 3, 4.
"""
import sys
sys.path.insert(0, ".")
from wave35_tm_census import tm_census
from wave16_d1a_targeted import Dm

# ---------- Part A ----------
def mul(p, C, D):
    a, b = C; c, d = D
    return ((a * c + 2 * b * d) % p, (a * d + b * c) % p)

def conj(C):
    return (C[0], (-C[1]) % 3)

p = 3
alpha = (0, 2)  # 3 + 2 sqrt2 mod 3
# alpha^j mod 3
pw = [(1, 0)]
for _ in range(4):
    pw.append(mul(p, pw[-1], alpha))
assert pw[4] == (1, 0) and pw[1] != (1, 0) and pw[2] != (1, 0), pw
print("ord_3(alpha) =", 4)
# alpha^4 - 1 = 576 + 408 sqrt2; v_3 = min(v_3(576), v_3(408)) = min(2,1) = 1
a4 = (577 % 9, 408 % 9)
print("alpha^4 mod 9 =", a4, "-> alpha^4 - 1 = 576 + 408 sqrt2, v_3 = 1, u = sqrt2 mod 3")
# B_j0 = y-coeff of C alpha^j0 mod 3; Z empty iff all B != 0
classes = [(a, b) for a in range(3) for b in range(3)]
def Zset(C):
    z = set()
    cur = C
    for j0 in range(4):
        if cur[1] % 3 == 0:
            z.add(j0)
        cur = mul(p, cur, alpha)
    return z

def gamma_orbit(C):
    orb = set()
    cur = C
    for _ in range(4):
        orb.add(cur)
        cur = mul(p, cur, alpha)
    cur = conj(C)
    for _ in range(4):
        orb.add(cur)
        cur = mul(p, cur, alpha)
    return frozenset(orb)

orbits = {}
for C in classes:
    orbits.setdefault(gamma_orbit(C), []).append(C)
zempty_orbits = [o for o in orbits if len(Zset(next(iter(o)))) == 0]
print(f"Gamma-orbits mod 3: {len(orbits)}, with Z empty: {len(zempty_orbits)}")
for o in zempty_orbits:
    print("  Z-empty orbit:", sorted(o), "Z =", Zset(next(iter(o))))
assert len(zempty_orbits) == 1, "N(b) != 1!"
print("Part A PASS: N(b) = 1 for p = 3 (proved by finite mod-3 computation)")

# ---------- Part B ----------
for (m, pp, f) in [(12, 3, 2), (36, 3, 3), (108, 3, 4), (324, 3, 5)]:
    D = Dm(m)
    assert D % (pp ** (2 * f)) == 0, (m, pp, f)
    print(f"--- census m={m} p={pp} f={f} (q={pp ** (2 * f)}) ---")
    res = tm_census(m, pp, f)
    onsup = [r for r in res if r[2]]
    mixed = [r for r in res if r[3] and not r[2]]
    print(f"  RESULT m={m}: split={len(res)} on-support={len(onsup)} "
          f"mixed={len(mixed)}; tower bound f-1={f - 1}")
    assert len(res) == f - 1, f"expected {f - 1} split fibers at m={m}"
    assert len(mixed) == 0, "mixed support!"
print("Part B PASS: N = f-1 exactly at m = 12, 36, 108, 324 (new: 324 gives 4)")
