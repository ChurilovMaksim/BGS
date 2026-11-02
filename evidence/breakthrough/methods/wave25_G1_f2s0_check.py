"""Wave 25, task 4: exact checks for the degenerate |H0| <= 2 cases.

Claims verified:
1. L0(3) = 4 and alpha^4 = 1 + 3*sqrt2 mod 9, so k(3) = 1.
2. L0(17) = 8 and alpha^8 = 1 + 51*sqrt2 mod 289, so k(17) = 1.
3. |H0| = 1 singleton invariance: at p = 3, C = 1 mod 9, the twist
   C' = 1 + 3*c*sqrt2 preserves Tr(C) = 2 but C' != C, C' != conj(C).
All arithmetic exact integers in R = Z[sqrt2].
"""
def mul(x, y, m):
    return ((x[0]*y[0] + 2*x[1]*y[1]) % m, (x[0]*y[1] + x[1]*y[0]) % m)

def pw(x, e, m):
    r = (1 % m, 0)
    while e:
        if e & 1:
            r = mul(r, x, m)
        x = mul(x, x, m)
        e >>= 1
    return r

def order(x, m, cap=5000):
    cur = (1 % m, 0)
    for j in range(1, cap + 1):
        cur = mul(cur, x, m)
        if cur == (1 % m, 0):
            return j
    return None

alpha = (3, 2)
for p, L0_expect in ((3, 4), (17, 8)):
    L0 = order((alpha[0] % p, alpha[1] % p), p)
    assert L0 == L0_expect, (p, L0)
    aL0 = pw((alpha[0] % (p*p), alpha[1] % (p*p)), L0, p*p)
    assert aL0 != (1, 0), (p, aL0)  # k = 1, not >= 2
    print(f"p={p}: L0={L0}, alpha^L0 mod p^2 = {aL0}, k=1 OK")

for c in (1, 2):
    Cp = (1, (3*c) % 9)
    assert (2*Cp[0]) % 9 == 2 and Cp != (1, 0) and Cp != (1, 0)
    print(f"p=3 singleton: c={c}, Tr(C')=2=Tr(C), C'!=C, C'!=conj(C) OK")
print("ALL CHECKS PASS")
