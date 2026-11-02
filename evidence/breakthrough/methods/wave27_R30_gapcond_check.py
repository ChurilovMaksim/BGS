"""Wave 27, task 2 check (revised): gap symmetry at level p^3.

R30's setting is f=3, s=0, hence k=3: alpha^L0 == 1 mod p^3, so
beta = alpha^t IS Teichmueller mod p^3 there. The first version of
this check used beta = alpha^t at primes with k<3, where beta is
NOT Teichmueller -- and the beta-form of gap symmetry fails there
(documented below). This version checks the correct claim:
  gap (B_H real mod p) ==> conj(tau_A) == tau_A * tau_beta^r (mod p^3)
for tau_beta = Teichmueller part of beta, and records k = v_p(alpha^L0-1)
and the beta-form failure count at each prime.
Exact integer arithmetic throughout.
"""
import random


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
    ni = pow(n, -1, M)
    c = conj(u)
    return (c[0] * ni % M, c[1] * ni % M)


def order_mod_p(u, p):
    r, cur = 1, u
    while cur != (1, 0):
        cur = mul(cur, u, p)
        r += 1
        assert r <= 2 * p + 5
    return r


def vp(n, p):
    # n is a residue mod p^3; exact 0 means valuation >= 3 (precision cap)
    if n % (p ** 3) == 0:
        return 3
    k = 0
    while n % p == 0:
        n //= p
        k += 1
    return k


def teich(A, p):
    M = p ** 3
    leg = pow(2, (p - 1) // 2, p)
    m = (p - 1) ** 2 if leg == 1 else p ** 2 - 1
    d = pow(p * p, -1, m)
    tau = pw(pw(A, p * p, M), d, M)
    # self-checks: tau == A mod p, tau^m == 1 mod p^3
    assert tau[0] % p == A[0] % p and tau[1] % p == A[1] % p
    assert pw(tau, m, M) == (1, 0)
    return tau


random.seed(27)
for p in (5, 7, 13):
    M = p ** 3
    alpha = (3 % p, 2 % p)
    L0 = order_mod_p(alpha, p)
    aL0 = pw((3, 2), L0, M)
    k = min(vp(aL0[0] - 1, p), vp(aL0[1], p))
    for t in (1, 2, 4):
        beta_p = pw(alpha, t, p)
        H0 = order_mod_p(beta_p, p)
        if H0 < 3:
            print(f"p={p} t={t}: |H0|={H0} (degenerate, skipped)")
            continue
        beta = pw((3, 2), t, M)
        tb = teich(beta, p)
        assert pw(tb, H0, M) == (1, 0)  # tau_beta has order |H0|
        n_gap = bad_tau = bad_beta = 0
        for _ in range(400):
            while True:
                A = (random.randrange(M), random.randrange(M))
                if (A[0] * A[0] - 2 * A[1] * A[1]) % p != 0:
                    break
            a = (A[0] % p, A[1] % p)
            ratio = mul(conj(a), inv(a, p), p)
            if pw(ratio, H0, p) != (1, 0):
                continue
            n_gap += 1
            tau = teich(A, p)
            tc = (tau[0] % M, (-tau[1]) % M)
            if not any(mul(tau, pw(tb, r, M), M) == tc
                       for r in range(H0)):
                bad_tau += 1
            if not any(mul(tau, pw(beta, r, M), M) == tc
                       for r in range(H0)):
                bad_beta += 1
        print(f"p={p} t={t}: L0={L0} |H0|={H0} k={k} "
              f"gap={n_gap}/400 bad_tau={bad_tau} bad_beta={bad_beta}")
        assert bad_tau == 0
print("GAP SYMMETRY VIA tau_beta HOLDS mod p^3 IN ALL CASES")
