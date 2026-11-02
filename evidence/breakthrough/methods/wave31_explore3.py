"""Wave 31 exploration 3: verify the injectivity lemma and Joint Lemma.

Claims to verify:
  L1: on an orbit, V1 - a1*V0 - b1*T depends only on V0
      (i.e. d1 = D(V0, N0)).
  L2: if b1 != 0, the map j -> (v0_j, v1_j) is injective
      (max fiber size 1), for gap AND non-gap bases.
  L3: if b1 == 0, fibers are V0-fibers (coarse) -- sanity check.
  L4: if H0 >= 3, some t_j != 0.
  JL: for bases with b1 != 0 (gap or not), no nonzero nu preserves
      the orbit multiset under the p^2-twist.
"""
import random
from collections import Counter, defaultdict


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


def orbit_multiset(A, tb, H0, M):
    return sorted((2 * mul(A, pw(tb, j, M), M)[0]) % M for j in range(H0))


random.seed(31)
res = Counter()
for p in (5, 7, 13):
    M = p ** 3
    alpha = (3, 2)
    for t in (1, 2, 4):
        beta = pw(alpha, t, M)
        tb = teich(beta, p)
        H0 = order_mod_p((beta[0] % p, beta[1] % p), p)
        if H0 < 3:
            continue
        for _ in range(300):
            while True:
                A = (random.randrange(M), random.randrange(M))
                if (A[0] ** 2 - 2 * A[1] ** 2) % p != 0:
                    break
            a = (A[0] % p, A[1] % p)
            ratio = mul(conj(a), inv(a, p), p)
            is_gap = (pw(ratio, H0, p) == (1, 0))
            tauA = teich(A, p)
            q = mul(inv(tauA, M), A, M)
            lam1 = (((q[0] - 1) // p) % p, (q[1] // p) % p)
            a1, b1 = lam1
            v0, v1, tt = [], [], []
            for j in range(H0):
                Tb = mul(tauA, pw(tb, j, M), M)
                Ab = mul(A, pw(tb, j, M), M)
                v = (2 * Ab[0]) % M
                v0.append(v % p)
                v1.append((v // p) % p)
                tt.append((4 * (Tb[1] % p)) % p)
            # L1: V1 - a1 V0 - b1 T constant on V0-fibers?
            byV0 = defaultdict(set)
            for j in range(H0):
                byV0[v0[j]].add((v1[j] - a1 * v0[j] - b1 * tt[j]) % p)
            l1 = all(len(s) == 1 for s in byV0.values())
            res["L1_ok"] += l1
            res["L1_cases"] += 1
            # L2/L3: max (V0,V1)-fiber size
            fib = Counter(zip(v0, v1))
            mx = max(fib.values())
            if b1 != 0:
                res["b1ne_maxfiber1"] += (mx == 1)
                res["b1ne_cases"] += 1
            else:
                res["b1eq_maxfiber_gt1_or_H0small"] += (mx > 1 or H0 <= 2)
                res["b1eq_cases"] += 1
            # L4: some t != 0
            res["L4_some_t_nonzero"] += any(x != 0 for x in tt)
            res["L4_cases"] += 1
            # JL: no nonzero nu preserves (b1 != 0 only)
            if b1 != 0:
                base = orbit_multiset(A, tb, H0, M)
                preserving = 0
                for e in range(p):
                    for f in range(p):
                        if e == 0 and f == 0:
                            continue
                        Astar = ((A[0] + 2 * A[1] * p * p * f) % M,
                                 (A[1] + A[0] * p * p * f) % M)
                        Astar = ((Astar[0] + A[0] * p * p * e) % M,
                                 (Astar[1] + A[1] * p * p * e) % M)
                        if orbit_multiset(Astar, tb, H0, M) == base:
                            preserving += 1
                res["JL_no_preserving"] += (preserving == 0)
                res["JL_cases"] += 1
                res["JL_gap_cases"] += is_gap
                res["JL_gap_no_preserving"] += (is_gap and preserving == 0)
print(dict(res))
print("DONE")
