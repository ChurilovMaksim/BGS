"""Wave 27, R40 experiment, CORRECTED (exact integers, R = Z[sqrt2]).

p=5, mod 625. H3 = Teichmueller subgroup of order 3 in the norm-1
group mod 625, built by Newton-lifting the order-3 solutions mod 5
of x^3 = 1 (derivative 3x^2 a unit mod 5). Real case: Abar/A mod 5
in H3 mod 5. Tests: (1) random real-case A, twists (1+25 b sqrt2),
(1+125 b' sqrt2): does the H3-orbit trace multiset survive?
(2) targeted swap search: A with E = A*theta_tilde - Abar == 0
mod 5, E1 = E/5, b* from E1 = -sqrt2 * b* * Abar mod 5; does the
b*-twist survive mod 125 (swap expected) and mod 625 (decisive)?
"""
import random

P = 5
M = 625


def add(a, b, m):
    return ((a[0] + b[0]) % m, (a[1] + b[1]) % m)


def sub(a, b, m):
    return ((a[0] - b[0]) % m, (a[1] - b[1]) % m)


def mul(a, b, m):
    return ((a[0] * b[0] + 2 * a[1] * b[1]) % m,
            (a[0] * b[1] + a[1] * b[0]) % m)


def conj(a, m):
    return (a[0] % m, (-a[1]) % m)


def norm(a, m):
    return (a[0] * a[0] - 2 * a[1] * a[1]) % m


def pw(a, e, m):
    r = (1, 0)
    while e:
        if e & 1:
            r = mul(r, a, m)
        a = mul(a, a, m)
        e >>= 1
    return r


def invR(a, m):
    n = norm(a, m)
    assert n % 5 != 0, "not a unit"
    ni = pow(n % 5, -1, 5)
    # inverse mod m via conj/n: need n^{-1} mod m; n is a unit mod 5
    # but may not be invertible mod 625 if gcd(n,625)!=1; here n%5!=0
    # so gcd(n,625)=1.
    ni = pow(n, -1, m)
    return ((a[0] * ni) % m, (-a[1] * ni) % m)


def inv5(a):
    n = norm(a, 5)
    assert n % 5 != 0
    ni = pow(n, -1, 5)
    return ((a[0] * ni) % 5, (-a[1] * ni) % 5)


def red(a, m):
    return (a[0] % m, a[1] % m)


def tr(a):
    return (2 * a[0]) % M


def orbit_multiset(A, H):
    return sorted(tr(mul(A, h, M)) for h in H)


def d_related(A, Aprime, H):
    cands = [mul(A, h, M) for h in H] + [mul(conj(A, M), h, M) for h in H]
    return any(c == Aprime for c in cands)


def newton_cube_root(x0):
    """Lift x0 (mod 5, x0^3 == 1) to a cube root of 1 mod 625."""
    x = (x0[0] % M, x0[1] % M)
    for _ in range(4):
        f = sub(pw(x, 3, M), (1, 0), M)
        d = mul((3, 0), pw(x, 2, M), M)
        x = sub(x, mul(f, invR(d, M), M), M)
    assert pw(x, 3, M) == (1, 0), pw(x, 3, M)
    assert norm(x, M) % 5 != 0
    return x


# order-3 elements mod 5 in the norm-1 group: (2,2),(2,3) (and (1,0))
H3 = []
for x0 in [(1, 0), (2, 2), (2, 3)]:
    w = newton_cube_root(x0)
    H3.append(w)
print("H3:", H3)
print("orders:", [pw(w, 3, M) for w in H3], "nontrivial^1:", H3[1], H3[2])
assert len(set(H3)) == 3
assert all(norm(w, M) == 1 for w in H3), [norm(w, M) for w in H3]
H3mod5 = set(red(h, 5) for h in H3)
print("H3 mod 5:", H3mod5)
SQ2 = (0, 1)

random.seed(12345)

# ---- (1) random real-case A, twist scan ----
found = 0
tested = 0
for _ in range(20000):
    A = (random.randrange(M), random.randrange(M))
    if norm(A, 5) == 0:
        continue
    theta = mul(conj(A, 5), inv5(red(A, 5)), 5)
    if theta not in H3mod5:
        continue
    tested += 1
    MA = orbit_multiset(A, H3)
    for b in range(1, 5):
        A2 = mul(A, add((1, 0), (0, 25 * b), M), M)
        if orbit_multiset(A2, H3) == MA and not d_related(A, A2, H3):
            print("COUNTEREXAMPLE p2-twist b=", b, "A=", A)
            found += 1
        A3 = mul(A, add((1, 0), (0, 125 * b), M), M)
        if orbit_multiset(A3, H3) == MA and not d_related(A, A3, H3):
            print("COUNTEREXAMPLE p3-twist b'=", b, "A=", A)
            found += 1
print(f"random scan: {tested} real-case A, {found} counterexamples")

# ---- (2) targeted swap search ----
nE = 0
nline = 0
for _ in range(200000):
    A = (random.randrange(M), random.randrange(M))
    if norm(A, 5) == 0:
        continue
    theta = mul(conj(A, 5), inv5(red(A, 5)), 5)
    if theta not in H3mod5:
        continue
    ttilde = None
    for h in H3:
        if red(h, 5) == theta:
            ttilde = h
            break
    E = sub(mul(A, ttilde, M), conj(A, M), M)
    if E[0] % 5 != 0 or E[1] % 5 != 0:
        continue
    nE += 1
    E1 = ((E[0] // 5) % 25, (E[1] // 5) % 25)
    E1m5 = red(E1, 5)
    sq2Abar = mul(SQ2, conj(A, 5), 5)
    q = mul(E1m5, inv5(sq2Abar), 5)
    if q[1] % 5 != 0:
        continue
    nline += 1
    bstar = (-q[0]) % 5
    if bstar == 0:
        continue
    A2 = mul(A, add((1, 0), (0, 25 * bstar), M), M)
    MA = orbit_multiset(A, H3)
    M2 = orbit_multiset(A2, H3)
    same125 = sorted(t % 125 for t in MA) == sorted(t % 125 for t in M2)
    print(f"SWAP CANDIDATE A={A} b*={bstar} same_mod125={same125} "
          f"same_mod625={M2 == MA} d_related={d_related(A, A2, H3)}")
    if M2 == MA and not d_related(A, A2, H3):
        print("  ==> COUNTEREXAMPLE TO R40")
    break
print(f"targeted: E==0 mod 5 found {nE}, line condition met {nline}")
