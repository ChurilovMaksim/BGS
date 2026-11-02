"""Wave 27, R40 decisive test: the DEEP real subcase.

p=5, mod 625. H3 (order 3) and H6 (order 6) Teichmueller subgroups
via Newton lifting (x^3-1 and x^6-1; derivatives units mod 5).
Deep subcase: Cbar == C*theta_tilde mod 25 (E^(1) == 0 mod 5).
For a non-fixed pair {z, z' = theta_tilde/z}:
  D = (Tr(Cz') - Tr(Cz))/25 mod 25, Y = Im(Cz) mod 25,
  b_hat = D * inv(4Y) mod 25.
Twist C' = C(1 + 25*b_hat*sqrt2): does it preserve the orbit
multiset mod 625? Is it D-related? A preserved non-D-related twist
is a counterexample to R40; if b_hat always gives the conjugate
branch (or never preserves), R40 stands.
"""
import random

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
    assert n % 5 != 0
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


def newton_root(x0, n):
    """Lift x0 (mod 5, x0^n == 1) to a root of x^n - 1 mod 625."""
    x = (x0[0] % M, x0[1] % M)
    for _ in range(4):
        f = sub(pw(x, n, M), (1, 0), M)
        d = mul((n, 0), pw(x, n - 1, M), M)
        x = sub(x, mul(f, invR(d, M), M), M)
    assert pw(x, n, M) == (1, 0)
    return x


w3 = newton_root((2, 2), 3)
H3 = [(1, 0), w3, pw(w3, 2, M)]
w6 = newton_root((3, 2), 6)
H6 = [pw(w6, i, M) for i in range(6)]
for H, nm in [(H3, "H3"), (H6, "H6")]:
    assert len(set(H)) == len(H), nm
    assert all(norm(h, M) == 1 for h in H), nm
    print(nm, "ok, size", len(H))

random.seed(999)


def test_group(H, nm, target=60):
    Hmod5 = set(red(h, 5) for h in H)
    ndeep = 0
    npres = 0
    ncounter = 0
    nrelated = 0
    tries = 0
    while ndeep < target and tries < 3000000:
        tries += 1
        A = (random.randrange(M), random.randrange(M))
        if norm(A, 5) == 0:
            continue
        theta = mul(conj(A, 5), inv5(red(A, 5)), 5)
        if theta not in Hmod5:
            continue
        ttilde = None
        for h in H:
            if red(h, 5) == theta:
                ttilde = h
                break
        E = sub(mul(A, ttilde, M), conj(A, M), M)
        if E[0] % 25 != 0 or E[1] % 25 != 0:
            continue
        ndeep += 1
        # non-fixed pairs: z with z != ttilde/z
        pairs = []
        seen = set()
        for z in H:
            zp = mul(ttilde, invR(z, M), M)
            if zp in seen:
                continue
            seen.add(z)
            seen.add(zp)
            if zp != z:
                pairs.append((z, zp))
        MA = orbit_multiset(A, H)
        bhats = set()
        for (z, zp) in pairs:
            tz = tr(mul(A, z, M))
            tzp = tr(mul(A, zp, M))
            diff = (tzp - tz) % M
            assert diff % 25 == 0, (diff, nm)
            D = (diff // 25) % 25
            Y = mul(A, z, M)[1] % 25
            assert Y % 5 != 0, "non-fixed pair must have Y unit mod 5"
            bhat = (D * pow((4 * Y) % 25, -1, 25)) % 25
            bhats.add(bhat)
        if len(bhats) == 1:
            bhat = bhats.pop()
            Aprime = mul(A, add((1, 0), (0, 25 * bhat), M), M)
            if orbit_multiset(Aprime, H) == MA:
                npres += 1
                if d_related(A, Aprime, H):
                    nrelated += 1
                else:
                    ncounter += 1
                    print(f"  COUNTEREXAMPLE {nm} A={A} b_hat={bhat}")
                    if ncounter >= 3:
                        break
        else:
            # b_hat inconsistent across pairs: no single twist works
            pass
    print(f"{nm}: deep={ndeep} (tries={tries}), b_hat-consistent "
          f"preserving={npres}, of which D-related={nrelated}, "
          f"counterexamples={ncounter}")


test_group(H3, "H3", target=60)
test_group(H6, "H6", target=60)
