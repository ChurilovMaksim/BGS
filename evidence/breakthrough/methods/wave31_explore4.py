"""Wave 31 robustness: Joint Lemma for RANDOM norm-1 beta_bar (not just
alpha^t) and at p=3, 17, 19. beta, tau = Teichmuller lifts; A =
tau(1 + p lam1 + p^2 lam2) with b1 != 0. Check (V0,V1) injective and
no nonzero nu preserves the orbit multiset.
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
        if r > 4 * p + 10:
            return None
    return r


def teich(A, p):
    M = p ** 3
    leg = pow(2, (p - 1) // 2, p)
    m = (p - 1) ** 2 if leg == 1 else p ** 2 - 1
    d = pow(p * p, -1, m)
    return pw(pw(A, p * p, M), d, M)


def orbit_multiset(A, tb, H0, M):
    return sorted((2 * mul(A, pw(tb, j, M), M)[0]) % M for j in range(H0))


random.seed(7)
res = Counter()
for p in (3, 5, 17, 19):
    M = p ** 3
    tries = 0
    while tries < 400:
        tries += 1
        # random norm-1 beta_bar
        while True:
            bb = (random.randrange(p), random.randrange(p))
            if (bb[0] ** 2 - 2 * bb[1] ** 2) % p == 1:
                break
        H0 = order_mod_p(bb, p)
        if H0 is None or H0 < 3:
            continue
        tb = teich(bb, p)
        while True:
            tb0 = (random.randrange(p), random.randrange(p))
            if (tb0[0] ** 2 - 2 * tb0[1] ** 2) % p != 0:
                break
        tauA = teich(tb0, p)
        a1 = random.randrange(p)
        b1 = random.randrange(1, p)
        a2 = random.randrange(p)
        b2 = random.randrange(p)
        # A = tau (1 + p lam1 + p^2 lam2)
        f = ((1 + p * a1 + p * p * a2) % M,
             (p * b1 + p * p * b2) % M)
        A = mul(tauA, f, M)
        v0, v1 = [], []
        for j in range(H0):
            Ab = mul(A, pw(tb, j, M), M)
            v = (2 * Ab[0]) % M
            v0.append(v % p)
            v1.append((v // p) % p)
        inj = len(set(zip(v0, v1))) == H0
        base = orbit_multiset(A, tb, H0, M)
        preserving = 0
        for e in range(p):
            for f_ in range(p):
                if e == 0 and f_ == 0:
                    continue
                Astar = ((A[0] + 2 * A[1] * p * p * f_) % M,
                         (A[1] + A[0] * p * p * f_) % M)
                Astar = ((Astar[0] + A[0] * p * p * e) % M,
                         (Astar[1] + A[1] * p * p * e) % M)
                if orbit_multiset(Astar, tb, H0, M) == base:
                    preserving += 1
        res["cases"] += 1
        res["inj"] += inj
        res["no_preserving"] += (preserving == 0)
        if not inj or preserving != 0:
            print("FAIL", p, bb, H0, inj, preserving)
print(dict(res))
print("DONE")
