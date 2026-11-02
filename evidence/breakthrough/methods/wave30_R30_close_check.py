"""Wave 30, task 1 checks: R30 twist-form reduction + gap-case p^2-twist test.

Exact arithmetic in R = Z[sqrt(2)] mod p^3, Teichmueller orbits
(same construction as wave 28: no genuine k=3 prime known below 2e9,
R30's setting itself has beta Teichmueller).

Q1 (twist-form reduction identities): for C' = C(1 + p lam1 + p^2 lam2),
  p-coeff of sum (v')^2 - sum v^2  = 4|H0| N Re(lam1),
  and if Re(lam1)=0, p^2-coeff = 4|H0| N (Re(lam2) - Im(lam1)^2).
  Hence multiset equality forces Re(lam1)=0 (twist form at level p)
  and then Re(lam2)=Im(lam1)^2.
Q2 (gap-case p^2-twist): for gap-case unit A = tau(1+p lam1+p^2 lam2),
  which nu in R/p have multiset(A(1+p^2 nu)) == multiset(A)?
  D-related iff nu=0, or (b1=0 and nu=(0,-2 b2)).
  A non-D-related preserving nu is a COUNTEREXAMPLE to R30.
"""
import random
from collections import Counter


def mul(u, v, M):
    return ((u[0] * v[0] + 2 * u[1] * v[1]) % M,
            (u[0] * v[1] + u[1] * v[0]) % M)


def pw(u, e, M):
    r = (1, 0)
    while e:
        if e & 1:
            r = mul(r, u, M)
        u = mul(u, u, M)
        e >>= 1
    return r


def conj(u):
    return (u[0], -u[1])


def inv(u, M):
    n = (u[0] * u[0] - 2 * u[1] * u[1]) % M
    return ((conj(u)[0] * pow(n, -1, M)) % M,
            (conj(u)[1] * pow(n, -1, M)) % M)


def order_mod_p(u, p):
    r, cur = 1, u
    while cur != (1, 0):
        cur = mul(cur, u, p)
        r += 1
        assert r <= 4 * p + 10
    return r


def teich(A, p):
    M = p ** 3
    leg = pow(2, (p - 1) // 2, p)
    m = (p - 1) ** 2 if leg == 1 else p ** 2 - 1
    d = pow(p * p, -1, m)
    tau = pw(pw(A, p * p, M), d, M)
    assert tau[0] % p == A[0] % p and tau[1] % p == A[1] % p
    return tau


def orbit_multiset(C, tb, H0, M):
    return sorted((2 * mul(C, pw(tb, j, M), M)[0]) % M for j in range(H0))


random.seed(30)
print("== Q1: twist-form reduction identities ==")
q1 = 0
for p in (5, 7, 13):
    M = p ** 3
    alpha = (3, 2)
    for t in (1, 2, 4):
        beta = pw(alpha, t, M)
        tb = teich(beta, p)
        H0 = order_mod_p((beta[0] % p, beta[1] % p), p)
        if H0 < 3:
            continue
        for _ in range(60):
            while True:
                C = (random.randrange(M), random.randrange(M))
                if (C[0] ** 2 - 2 * C[1] ** 2) % p != 0:
                    break
            lam1 = (random.randrange(p), random.randrange(p))
            lam2 = (random.randrange(p), random.randrange(p))
            # C' = C (1 + p lam1 + p^2 lam2) mod p^3
            f = ((1 + p * lam1[0] + p * p * lam2[0]) % M,
                 (p * lam1[1] + p * p * lam2[1]) % M)
            Cp = mul(C, f, M)
            v = [mul(C, pw(tb, j, M), M) for j in range(H0)]
            vp = [mul(Cp, pw(tb, j, M), M) for j in range(H0)]
            S = sum((2 * x[0]) ** 2 for x in v) % (p ** 3)
            Sp = sum((2 * x[0]) ** 2 for x in vp) % (p ** 3)
            diff = (Sp - S) % (p ** 3)
            N = (C[0] ** 2 - 2 * C[1] ** 2) % p
            a1, b1 = lam1
            a2, b2 = lam2
            # p-coefficient must be 4 H0 N a1 mod p
            assert (diff // p) % p == (4 * H0 * N * a1) % p, \
                f"p-coeff fails p={p} t={t}"
            if a1 == 0:
                assert (diff // (p * p)) % p == \
                    (4 * H0 * N * (a2 - b1 * b1)) % p, \
                    f"p^2-coeff fails p={p} t={t}"
            q1 += 1
print(f"Q1 identities hold in {q1} cases")

print("== Q2: gap-case p^2-twists ==")
n_gap = 0
bad = []          # non-D-related preserving nu -> R30 counterexample
pattern = Counter()
for p in (5, 7, 13):
    M = p ** 3
    alpha = (3, 2)
    for t in (1, 2, 4):
        beta = pw(alpha, t, M)
        tb = teich(beta, p)
        H0 = order_mod_p((beta[0] % p, beta[1] % p), p)
        if H0 < 3:
            continue
        for _ in range(400):
            while True:
                A = (random.randrange(M), random.randrange(M))
                if (A[0] ** 2 - 2 * A[1] ** 2) % p != 0:
                    break
            a = (A[0] % p, A[1] % p)
            ratio = mul(conj(a), inv(a, p), p)
            if pw(ratio, H0, p) != (1, 0):
                continue  # not gap
            n_gap += 1
            tauA = teich(A, p)
            q = mul(inv(tauA, M), A, M)
            lam1 = (((q[0] - 1) // p) % p, (q[1] // p) % p)
            lam2 = (((q[0] - 1 - p * lam1[0]) // (p * p)) % p,
                    ((q[1] - p * lam1[1]) // (p * p)) % p)
            a1, b1 = lam1
            a2, b2 = lam2
            base = orbit_multiset(A, tb, H0, M)
            preserving = []
            for e in range(p):
                for f in range(p):
                    if e == 0 and f == 0:
                        continue
                    Astar = ((A[0] + 2 * A[1] * p * p * f) % M,
                             (A[1] + A[0] * p * p * f) % M)
                    # note: (x+ys)(1+p^2(e+fs)) = x+2y p^2 f + ...;
                    # e-part: x -> x + p^2 e x, y -> y + p^2 e y
                    Astar = ((Astar[0] + A[0] * p * p * e) % M,
                             (Astar[1] + A[1] * p * p * e) % M)
                    if orbit_multiset(Astar, tb, H0, M) == base:
                        preserving.append((e, f))
            # D-related preserving nu (excluding 0): b1==0 and nu=(0,-2b2)
            drel = [(0, (-2 * b2) % p)] if b1 == 0 else []
            for nu in preserving:
                if nu not in drel:
                    bad.append((p, t, A, (a1, b1), (a2, b2), nu))
            pattern[(b1 == 0, tuple(sorted(preserving)) == tuple(sorted(drel)))] += 1
print(f"gap cases: {n_gap}")
print(f"pattern (b1==0, preserving==D-related): {dict(pattern)}")
print(f"NON-D-RELATED preserving twists (R30 counterexamples): {len(bad)}")
for row in bad[:5]:
    print("  ", row)
print("DONE")
