"""Wave 47, task 6: exact checks on the 16 fixed torsion patterns.
For pattern z, with A_z = z0 - z2 - 6*z3, B_z = z1 + 6*z2 + 35*z3
(from U = A_z*S_0 + B_z*S_1 via the class-sum recurrence), verify:
 (1) A_z + 3*B_z = 0 mod 8 for all 16 patterns (nonmax proof);
 (2) B_z mod 2 = pat_z for all 16 patterns;
 (3) max-bit table: with c_z = (A_z+3*B_z)/8 mod 2, the condition
     c_z*tau0 + B_z*k = pat_z (mod 2) for all patterns
     holds iff tau0 = 0 and k = 1.
"""
import sys; sys.path.insert(0, ".")
from wave16_d1a_targeted import torsion_data, Dm
Z, _ = torsion_data(32, Dm(32))
pats = [tuple(int(Z[r, i]) for i in range(4)) for r in range(16)]
pat_z = [0 if len({v % 4 for v in pat}) == 1 else 1 for pat in pats]
ok1 = ok2 = True
rows = []
for pat, pz in zip(pats, pat_z):
    z0, z1, z2, z3 = pat
    A = z0 - z2 - 6*z3; B = z1 + 6*z2 + 35*z3
    ok1 &= ((A + 3*B) % 8 == 0)
    ok2 &= ((B % 2) == pz)
    rows.append((pat, A, B, (A + 3*B)//8 % 2, B % 2, pz))
print(f"(1) A+3B = 0 mod 8 for all 16: {ok1}")
print(f"(2) B mod 2 = pat_z for all 16: {ok2}")
sols = [(t, k) for t in (0, 1) for k in (0, 1)
        if all((c*t + bm*k) % 2 == pz for (_, _, _, c, bm, pz) in rows)]
print(f"(3) (tau0, k) solutions: {sols} (expect [(0, 1)] only)")
assert ok1 and ok2 and sols == [(0, 1)]
print("ALL PATTERN CHECKS PASS")
