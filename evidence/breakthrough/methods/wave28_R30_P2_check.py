"""Wave 28, task 1 check: P2 carry-free computation for f=3, s=0.

Exact integer arithmetic in R = Z[sqrt(2)] mod p^3.
Since no k=3 prime is known below 2e9, the check runs on
Teichmueller orbits (tau_beta in place of beta): this tests the
P2 algebra and the gap-symmetry input exactly as R30's setting
needs them (there beta IS Teichmueller). It is NOT a check of
R30's setting at a genuine k=3 prime.
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


def teich(A, p):
    M = p ** 3
    leg = pow(2, (p - 1) // 2, p)
    m = (p - 1) ** 2 if leg == 1 else p ** 2 - 1
    d = pow(p * p, -1, m)
    tau = pw(pw(A, p * p, M), d, M)
    assert tau[0] % p == A[0] % p and tau[1] % p == A[1] % p
    assert pw(tau, m, M) == (1, 0)
    return tau


def digits_of_trace(T, p):
    """Base-p digits (d0,d1,d2) of Tr(T) mod p^3."""
    tr = (2 * T[0]) % (p ** 3)
    d0 = tr % p
    d1 = (tr // p) % p
    d2 = (tr // (p * p)) % p
    return d0, d1, d2


random.seed(28)
for p in (5, 7, 13):
    M = p ** 3
    alpha = (3, 2)
    L0 = order_mod_p(alpha, p)
    for t in (1, 2, 4):
        beta = pw(alpha, t, M)
        tb = teich(beta, p)
        H0 = order_mod_p((beta[0] % p, beta[1] % p), p)
        if H0 < 3:
            print(f"p={p} t={t}: |H0|={H0} degenerate, skipped")
            continue
        n_gap = n_K1 = n_P2 = n_s1 = 0
        n_naive_fail = 0
        s1_nonzero_cases = 0
        printed_ce = False
        for _ in range(300):
            while True:
                A = (random.randrange(M), random.randrange(M))
                if (A[0] * A[0] - 2 * A[1] * A[1]) % p != 0:
                    break
            a = (A[0] % p, A[1] % p)
            ratio = mul(conj(a), inv(a, p), p)
            if pw(ratio, H0, p) != (1, 0):
                continue  # not gap
            n_gap += 1
            tauA = teich(A, p)
            # gap symmetry via tau_beta (wave 27): conj(tauA) = tauA * tb^r
            # (conj reduced mod p^3; unreduced -y breaks tuple equality)
            tc = (tauA[0] % M, (-tauA[1]) % M)
            rs = [r for r in range(H0)
                  if mul(tauA, pw(tb, r, M), M) == tc]
            assert len(rs) == 1, f"gap symmetry fails p={p} t={t}"
            r = rs[0]
            # Teichmueller orbit and mod-p data
            Tj = [mul(tauA, pw(tb, j, M), M) for j in range(H0)]
            tbar = [(T[0] % p, T[1] % p) for T in Tj]
            xi = [u[0] for u in tbar]
            eta = [u[1] for u in tbar]
            N = (a[0] * a[0] - 2 * a[1] * a[1]) % p
            assert sum(xi) % p == 0 and sum(eta) % p == 0
            assert sum((x * x + 2 * e * e) % p for x, e in zip(xi, eta)) % p == 0
            # CORRECTED sign (wave 24 stated +H0*N/4; exact check gives
            # minus): sum eta^2 = -H0*N/4 mod p, hence sum t^2 = -4*H0*N.
            # The sign flips K1's definition but not K1 = 0 nor c = -2b1.
            assert (4 * sum((e * e) % p for e in eta)) % p == (-H0 * N) % p
            tt = [(4 * e) % p for e in eta]
            assert sum(tt) % p == 0
            assert sum((x * x) % p for x in tt) % p == (-4 * H0 * N) % p
            d1 = [digits_of_trace(T, p)[1] for T in Tj]
            # K1 = +2 sum d1*eta / (H0*N) mod p ; must be 0 in gap case
            K1 = (2 * sum((d * e) % p for d, e in zip(d1, eta)) % p) \
                * pow(H0 * N % p, -1, p) % p
            assert K1 == 0, f"K1 != 0 p={p} t={t} K1={K1}"
            n_K1 += 1
            # lambda1 from A = tauA (1 + p lam1 + p^2 lam2)
            q = mul(inv(tauA, M), A, M)
            lam1 = (((q[0] - 1) // p) % p, (q[1] // p) % p)
            a1, b1 = lam1
            lam2 = (((q[0] - 1 - p * lam1[0]) // (p * p)) % p,
                    ((q[1] - p * lam1[1]) // (p * p)) % p)
            a2, b2 = lam2
            # v1_j = d1_j + Tr(tbar_j * lam1)
            v1 = [(d + (2 * a1 * x + 4 * b1 * e) % p) % p
                  for d, x, e in zip(d1, xi, eta)]
            # P2 identity: 2 sum v1*t + c sum t^2 = 0  <=>  c = K1 - 2*b1
            # (sign-agnostic check: shifting c by 1 changes LHS by Stt).
            Svt = sum((v * t_) % p for v, t_ in zip(v1, tt)) % p
            Stt = sum((t_ * t_) % p for t_ in tt) % p
            assert Stt != 0
            assert (2 * Svt + ((K1 - 2 * b1) % p) * Stt) % p == 0
            assert (2 * Svt + ((K1 - 2 * b1 + 1) % p) * Stt) % p != 0
            assert K1 == 0  # gap case, so c = -2*b1
            n_P2 += 1
            # residual at p^3 for c = -2*b1: A' = A(1 + p c sqrt2).
            # TRUE claim: conj(A)^{-1} A' = tb^{-r} (1 + p^2 Q) for
            # SOME Q in R/p (p-coefficient vanishes). Read Q off by
            # normalised extraction; do NOT trust the naive formula
            # Q_naive = -4 b1^2 + 2 (b2 - a1 b1) sqrt2, which fails
            # by carry spills (see counterexample printed below).
            c = (-2 * b1) % p
            # Aprime = A * (1 + p c sqrt2):
            # (x + y s)(1 + p c s) = (x + 2 y p c) + (y + x p c) s
            Aprime = ((A[0] + 2 * A[1] * p * c) % M,
                      (A[1] + A[0] * p * c) % M)
            lhs = mul(inv(conj(A), M), Aprime, M)
            quot = mul(lhs, pw(tb, r, M), M)
            assert quot[0] % (p * p) == 1 and quot[1] % (p * p) == 0, \
                f"p-coefficient does not vanish p={p} t={t} quot={quot}"
            Q = (((quot[0] - 1) // (p * p)) % p, (quot[1] // (p * p)) % p)
            Qnaive = ((-4 * b1 * b1) % p, (2 * (b2 - a1 * b1)) % p)
            if Q != Qnaive:
                n_naive_fail += 1
                if not printed_ce:
                    printed_ce = True
                    print(f"  COUNTEREXAMPLE naive Q: A={A} lam1={(a1, b1)} "
                          f"lam2={(a2, b2)} Q_true={Q} Q_naive={Qnaive}")
            # s1 carry term for the NEXT (v2) step: delta_j = (T_j - tbar_j)/p
            delta = [(((T[0] - u[0]) // p) % p, ((T[1] - u[1]) // p) % p)
                     for T, u in zip(Tj, tbar)]
            im = [d[1] for d in delta]
            S_im_eta = sum((i * e) % p for i, e in zip(im, eta)) % p
            if S_im_eta != 0:
                s1_nonzero_cases += 1
            n_s1 += 1
        print(f"p={p} t={t}: |H0|={H0} gap={n_gap} K1=0:{n_K1} "
              f"P2:{n_P2} p-coeff-vanishes:{n_gap} naive-Q-fails:{n_naive_fail} "
              f"sumImDelta*eta!=0 in {s1_nonzero_cases}/{n_s1} gap cases")
print("ALL CHECKS PASS")
