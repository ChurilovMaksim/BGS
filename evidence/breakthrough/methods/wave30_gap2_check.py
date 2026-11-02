"""Wave 30, task 4 checks: twin sums at 12|m, cofactor floor, composite-u structure.
Exact integer arithmetic; sympy only for factoring (verified by multiplication)."""
from sympy import factorint

# Pell: x_m + y_m*sqrt(2) = (3+2*sqrt(2))^m, recurrence z_{n+1} = 6 z_n - z_{n-1}
X = [1, 3]
Y = [0, 2]
for _ in range(2, 200):
    X.append(6 * X[-1] - X[-2])
    Y.append(6 * Y[-1] - Y[-2])

def v2(n):
    c = 0
    while n % 2 == 0:
        n //= 2; c += 1
    return c

def odd_part(n):
    while n % 2 == 0:
        n //= 2
    return n

def Dm(m):
    return 2 * (X[m] - 1)

# --- 1. D_m = 2^a * S_m^2 with a = 2 v2(m)+3, S_m = odd part of y_{m/2} (m even) ---
for m in range(2, 121, 2):
    D = Dm(m)
    a = v2(D)
    assert a == 2 * v2(m) + 3, (m, a)
    S2 = D // (2 ** a)
    S = int(S2 ** 0.5)
    # exact integer sqrt check without float reliance for big values
    import math
    S = math.isqrt(S2)
    assert S * S == S2, m
    assert S == odd_part(Y[m // 2]), (m, S, odd_part(Y[m // 2]))
print("1. D_m structure OK for even m <= 120 (a = 2v2(m)+3, S_m = odd part of y_{m/2})")

# --- 2. orders of beta = 17+12*sqrt(2) at 9, 25, 49, 121 (direct powering in (Z/q)[sqrt2]) ---
def mul(u, w, q):
    return ((u[0]*w[0] + 2*u[1]*w[1]) % q, (u[0]*w[1] + u[1]*w[0]) % q)
def pw(u, e, q):
    r = (1, 0)
    while e:
        if e & 1: r = mul(r, u, q)
        u = mul(u, u, q); e >>= 1
    return r
BETA = (17, 12)
for q, expect in [(9, 6), (25, 15), (49, 21), (121, 66)]:
    o = 1; cur = BETA
    cur = (BETA[0] % q, BETA[1] % q)
    while cur != (1, 0):
        cur = mul(cur, (BETA[0] % q, BETA[1] % q), q); o += 1
        assert o <= 10000
    assert o == expect, (q, o)
    assert o % 3 == 0
print("2. ord(beta): 9->6, 25->15, 49->21, 121->66, all divisible by 3 (never twin)")

# --- 3. y_6 | y_{6u} and C_u = y_{6u}/y_6 ---
y6 = Y[6]
assert y6 == 13860
for u in range(1, 21):
    assert Y[6*u] % y6 == 0, u
print("3. y_6 = 13860 = 2^2*3^2*5*7*11 divides y_{6u} for u <= 20; odd part 3465 | S_m at 12|m")

# --- 4. twin test: qt = p^{2f} || D_m twin iff 3 ∤ ord_qt(beta); test via beta^{G3} != 1 ---
def legendre2(p):
    return 1 if p % 8 in (1, 7) else -1  # (2/p): 1 if p = +-1 mod 8
def is_twin(p, f):
    qt = p ** (2 * f)
    eps = legendre2(p)
    G = p ** (2 * f - 1) * (p - eps)  # norm-1 group order in (Z/qt)[sqrt2]
    G3 = G
    while G3 % 3 == 0:
        G3 //= 3
    return pw((17 % qt, 12 % qt), G3, qt) == (1, 0)  # twin iff 3 ∤ ord iff beta^G3 = 1

print("4. twin sums at 12|m (m <= 120):")
for m in range(12, 121, 12):
    D = Dm(m)
    a = v2(D)
    import math
    S = math.isqrt(D // (2 ** a))
    fac = factorint(S)  # S odd; factorint exact (product verified below)
    assert math.prod(p ** e for p, e in fac.items()) == S
    twins = []
    minc = None
    for p, e in fac.items():
        if is_twin(p, e):
            twins.append((p, e, p ** (2 * e)))
            c = S // (p ** e)
            minc = c if minc is None or c < minc else minc
    tsum = sum(t[2] for t in twins)
    ratio = tsum / D
    # dichotomy bound: <= 1/(2^a * 3465^2) + 3m/(2^a * S^{2/3})
    bound = 1 / (2 ** a * 3465 ** 2) + 3 * m / (2 ** a * float(S) ** (2/3))
    assert ratio <= bound + 1e-30, (m, ratio, bound)
    if minc is not None:
        assert minc >= 3465, (m, minc)
    print(f"   m={m}: S digits={len(str(S))} twins={[(t[0], t[1]) for t in twins]} "
          f"sum/D={ratio:.3e} min_cofactor={minc}")
    if m == 48:
        assert tsum == 289 + 332929, tsum

# --- 5. composite u: C_u has >= 2 distinct odd prime factors; primitive prime exists ---
print("5. composite u <= 30: C_u odd-prime-factor count and primitive prime:")
for u in range(4, 31):
    # composite only
    if all(u % d for d in range(2, u)):
        continue
    Cu = Y[6*u] // y6
    fac = factorint(odd_part(Cu))
    assert math.prod(p ** e for p, e in fac.items()) == odd_part(Cu)
    assert len(fac) >= 2, (u, fac)
    # primitive prime: divides Cu, divides no C_d for d|u, d<u
    divs = [d for d in range(1, u) if u % d == 0]
    prim = [p for p in fac if all((Y[6*d] // y6) % p != 0 for d in divs)]
    assert prim, (u, fac)
    print(f"   u={u}: odd primes of C_u = {sorted(fac)} (count {len(fac)}), primitive {prim}")
print("ALL CHECKS PASS")
