"""Check (v0,t) injectivity on G for p=13, 31 (k=2, s=0).
R = Z[sqrt2] represented as pairs (a,b) = a + b*sqrt2.
Elements mod p^2; G = <alpha> mod p^2, alpha = (3,2).
For every unit A mod p (v0,t depend only on A mod p) and every
z in G: map z -> (Tr(Az) mod p, Tr(A*sqrt2*z) mod p) must be injective.
Also verifies alpha^L0 == 1 mod p^2 and L0 = order mod p.
Exact integer arithmetic. Repository untouched, no Lean build.
"""
import sys

def add(x, y, M):
    return ((x[0] + y[0]) % M, (x[1] + y[1]) % M)

def mul(x, y, M):
    return ((x[0]*y[0] + 2*x[1]*y[1]) % M, (x[0]*y[1] + x[1]*y[0]) % M)

def tr(x):
    return 2 * x[0]

def is_unit_mod_p(A, p):
    # A mod p is a unit in R/p iff N(A) != 0 mod p OR split-case zero
    # divisor check: use determinant of mult-by-A over F_p: det = N(A).
    # In split case N(A)=0 with A!=0 gives zero divisor (not unit).
    return (A[0]*A[0] - 2*A[1]*A[1]) % p != 0

def check(p):
    M = p * p
    alpha = (3, 2)
    # order of alpha mod p
    cur = (1, 0)
    L0 = None
    for i in range(1, p * p + 2):
        cur = mul(cur, alpha, p)
        if cur == (1, 0):
            L0 = i
            break
    assert L0 is not None
    # alpha^L0 mod p^2
    cur = (1, 0)
    for _ in range(L0):
        cur = mul(cur, alpha, M)
    assert cur == (1, 0), f"p={p}: alpha^L0 != 1 mod p^2, hypothesis fails"
    # G mod p^2
    G = []
    cur = (1, 0)
    for _ in range(L0):
        G.append(cur)
        cur = mul(cur, alpha, M)
    assert len(set(G)) == L0
    sqrt2 = (0, 1)
    bad = 0
    nA = 0
    for a0 in range(p):
        for a1 in range(p):
            A = (a0, a1)
            if not is_unit_mod_p(A, p):
                continue
            nA += 1
            seen = {}
            Asqrt2 = mul(A, sqrt2, M)
            for z in G:
                v0 = tr(mul(A, z, M)) % p
                t = tr(mul(Asqrt2, z, M)) % p
                key = (v0, t)
                if key in seen and seen[key] != z:
                    bad += 1
                seen[key] = z
            assert len(seen) == L0, f"p={p}, A={A}: collision"
    print(f"p={p}: L0={L0} |G|={L0} units-mod-p={nA} bad={bad}")
    return bad

total = 0
for p in (13, 31):
    total += check(p)
print("TOTAL_BAD =", total)
sys.exit(0 if total == 0 else 1)
