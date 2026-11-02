# Wave 38, task 1 check: count Gamma-orbits mod p^e with Z = empty,
# compare to N(b) from the notes and to the bound 2*p^{2e}/d.
# R = Z[sqrt(2)] mod m: element (a,b) = a + b*sqrt(2).

def mul(a, b, mod):
    return ((a[0]*b[0] + 2*a[1]*b[1]) % mod,
            (a[0]*b[1] + a[1]*b[0]) % mod)

def conj(a, mod):
    return (a[0] % mod, (-a[1]) % mod)

def vp(n, p):
    if n == 0:
        return 10**9
    c = 0
    while n % p == 0:
        n //= p
        c += 1
    return c

def alpha_pow_exact(n):
    r = (1, 0)
    a = (3, 2)
    while n:
        if n & 1:
            r = (r[0]*a[0] + 2*r[1]*a[1], r[0]*a[1] + r[1]*a[0])
        a = (a[0]*a[0] + 2*a[1]*a[1], 2*a[0]*a[1])
        n >>= 1
    return r

def z_empty(Cp, p, d, u):
    # Cp = C mod p; B_j0 = Tr(C alpha^j0 u) mod p; empty iff all nonzero.
    pa = (1, 0)
    ap = (3 % p, 2 % p)
    for _ in range(d):
        v = mul(mul(Cp, pa, p), u, p)
        if (2*v[0]) % p == 0:
            return False
        pa = mul(pa, ap, p)
    return True

CASES = [(3, 4, 1, 1), (5, 6, 1, 2), (7, 3, 1, 5), (13, 14, 2, 546),
         (17, 8, 1, 18)]
for (p, d_claim, e_claim, Nb) in CASES:
    # d = ord_p(alpha)
    cur = (3 % p, 2 % p)
    d = 1
    while cur != (1, 0):
        cur = mul(cur, (3 % p, 2 % p), p)
        d += 1
        assert d <= p*p
    assert d == d_claim, (p, d, d_claim)
    A = alpha_pow_exact(d)
    e = min(vp(A[0]-1, p), vp(A[1], p))
    assert e == e_claim, (p, e, e_claim)
    pe = p**e
    u = ((A[0]-1)//pe % p, A[1]//pe % p)
    assert u != (0, 0), "u must be nonzero mod p"
    seen = set()
    orbits_z = 0
    orbits_tot = 0
    z_bad = 0
    ape = (3 % pe, 2 % pe)
    for a0 in range(pe):
        for b0 in range(pe):
            C = (a0, b0)
            if C in seen:
                continue
            orb = set()
            stack = [C]
            while stack:
                x = stack.pop()
                if x in orb:
                    continue
                orb.add(x)
                stack.append(mul(x, ape, pe))
                stack.append(conj(x, pe))
            seen |= orb
            orbits_tot += 1
            zs = set()
            for (x0, y0) in orb:
                zs.add(z_empty((x0 % p, y0 % p), p, d, u))
            if len(zs) > 1:
                z_bad += 1
            if z_empty((a0 % p, b0 % p), p, d, u):
                orbits_z += 1
    ok = (orbits_z >= Nb) and (orbits_z * d <= 2 * pe * pe)
    print(f"p={p} d={d} e={e} N(b)={Nb} orbits_Zempty={orbits_z} "
          f"bound_2p2e/d={2*pe*pe/d:.1f} total_orbits={orbits_tot} "
          f"z_invariant_bad={z_bad} OK={ok}")
    assert ok
print("ALL CHECKS PASS")
