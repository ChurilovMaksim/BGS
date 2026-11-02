"""Wave 31 exploration: fiber structure of the Joint Lemma.

Setup as in wave30 Q2: p in {5,7,13}, beta = alpha^t (alpha=(3,2)),
tb = Teichmuller lift of beta, H0 = order of beta mod p, gap bases A.
Digits: v_j = Tr(A beta^j) mod p^3 = v0 + p v1 + p^2 v2.
Twist by (1 + p^2 nu), nu = (0,g): v2 -> v2 + g*t_j, t_j = Tr(tau_j sqrt2)
where tau_j = (tau_A * tb^j) mod p.

Questions:
  (a) for gap bases with b1 != 0, which (v0,v1)-fibers break the twist?
  (b) is there always a fiber with sum t != 0 (first-moment kill)?
  (c) is there always a singleton fiber with t != 0?
  (d) what does the t-profile of failing fibers look like?
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


random.seed(31)
stats = Counter()
fail_examples = []
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
            if pw(ratio, H0, p) != (1, 0):
                continue  # not gap
            tauA = teich(A, p)
            q = mul(inv(tauA, M), A, M)
            lam1 = (((q[0] - 1) // p) % p, (q[1] // p) % p)
            a1, b1 = lam1
            if b1 == 0:
                continue
            # orbit digits and t
            v0, v1, v2, tt = [], [], [], []
            for j in range(H0):
                Tb = mul(tauA, pw(tb, j, M), M)
                Ab = mul(A, pw(tb, j, M), M)
                v = (2 * Ab[0]) % M
                v0.append(v % p)
                v1.append((v // p) % p)
                v2.append((v // (p * p)) % p)
                # t_j = Tr(tau_j sqrt2) mod p, tau_j = Tb mod p
                tt.append((4 * (Tb[1] % p)) % p)
            fibers = defaultdict(list)
            for j in range(H0):
                fibers[(v0[j], v1[j])].append(j)
            # per-fiber twist check for all g != 0
            some_fiber_sum_t_nonzero = False
            some_singleton_t_nonzero = False
            failing_fibers = 0
            total_fibers = len(fibers)
            size_dist = Counter(len(v) for v in fibers.values())
            for F, idxs in fibers.items():
                if sum(tt[j] for j in idxs) % p != 0:
                    some_fiber_sum_t_nonzero = True
                if len(idxs) == 1 and tt[idxs[0]] != 0:
                    some_singleton_t_nonzero = True
                # does some g != 0 break this fiber?
                cvals = [v2[j] for j in idxs]
                breaks = False
                for g in range(1, p):
                    shifted = sorted((v2[j] + g * tt[j]) % p for j in idxs)
                    if shifted != sorted(cvals):
                        breaks = True
                        break
                if breaks:
                    failing_fibers += 1
            stats["bases"] += 1
            stats["some_fiber_sum_t_nonzero"] += some_fiber_sum_t_nonzero
            stats["some_singleton_t_nonzero"] += some_singleton_t_nonzero
            stats["all_fibers_break"] += (failing_fibers == total_fibers)
            stats["some_fiber_breaks"] += (failing_fibers > 0)
            stats[f"size_dist_{p}_{t}"] += 0  # placeholder
            if len(fail_examples) < 3 and failing_fibers > 0:
                fail_examples.append((p, t, H0, (a1, b1), total_fibers,
                                      failing_fibers, dict(size_dist)))
print(dict(stats))
for e in fail_examples:
    print(e)
print("DONE")
