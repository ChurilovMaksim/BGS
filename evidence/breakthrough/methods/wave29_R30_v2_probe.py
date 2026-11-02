"""Wave 29, task 1 probe: decisive numerics for the R30 v2 step.

Questions:
  (P) Does any genuine (c != 0) gap twist A' = A(1+pc sqrt2), c = -2b1,
      preserve the FULL orbit multiset {Tr(A tb^j)} mod p^3?
  (Q) What is the p^2-coefficient of sum(v'^2)-sum(v^2), and does it match
      4*sum(xi*k) + 8*b1*c*|H0|*N  (k_j = (c*t_j)//p multiplication carry)?
  (R) Is sum_{t=0} xi in {0, +-s, +-2s} with s^2 = N, and n0 <= 2?
Teichmueller-orbit setup as in wave 28 (no genuine k=3 prime below 2e9).
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


random.seed(29)
tot = preserved = 0
bad_formula = 0
examples = []
for p in (5, 7, 13):
    M = p ** 3
    alpha = (3, 2)
    for t in (1, 2, 4):
        beta = pw(alpha, t, M)
        tb = teich(beta, p)
        H0 = order_mod_p((beta[0] % p, beta[1] % p), p)
        if H0 < 3:
            continue
        n = n_pres = n_b1nz = n_s2nz = 0
        for _ in range(300):
            while True:
                A = (random.randrange(M), random.randrange(M))
                if (A[0] * A[0] - 2 * A[1] * A[1]) % p != 0:
                    break
            a = (A[0] % p, A[1] % p)
            ratio = mul(conj(a), inv(a, p), p)
            if pw(ratio, H0, p) != (1, 0):
                continue
            n += 1
            tauA = teich(A, p)
            Tj = [mul(tauA, pw(tb, j, M), M) for j in range(H0)]
            tbar = [(T[0] % p, T[1] % p) for T in Tj]
            xi = [u[0] for u in tbar]
            eta = [u[1] for u in tbar]
            N = (a[0] * a[0] - 2 * a[1] * a[1]) % p
            q = mul(inv(tauA, M), A, M)
            a1 = ((q[0] - 1) // p) % p
            b1 = (q[1] // p) % p
            if b1 != 0:
                n_b1nz += 1
            c = (-2 * b1) % p
            # full multisets
            def multiset(Ax):
                return Counter(
                    (2 * mul(Ax, pw(tb, j, M), M)[0]) % M for j in range(H0))
            v = multiset(A)
            Aprime = ((A[0] + 2 * A[1] * p * c) % M,
                      (A[1] + A[0] * p * c) % M)
            vp = multiset(Aprime)
            if v == vp:
                n_pres += 1
                if len(examples) < 5:
                    examples.append((p, t, A, b1, c))
            # second power sum p^2-coefficient vs carry formula
            tt = [(4 * e) % p for e in eta]
            kk = [(c * tv) // p for tv in tt]
            S_xik = sum((x * k) % p for x, k in zip(xi, kk)) % p
            S2 = sum(x * x for x in v.elements()) % M
            S2p = sum(x * x for x in vp.elements()) % M
            diff = (S2p - S2) % M
            coeff = (diff // (p * p)) % p if diff % (p * p) == 0 else None
            formula = (4 * S_xik + 8 * b1 * c * H0 * N) % p
            if coeff is None or coeff != formula:
                bad_formula += 1
                if bad_formula <= 3:
                    print(f"  FORMULA MISMATCH p={p} t={t} coeff={coeff} "
                          f"formula={formula} diff%p^2={diff % (p*p)}")
            # (R): t=0 positions
            idx0 = [j for j in range(H0) if eta[j] == 0]
            S0 = sum(xi[j] for j in idx0) % p
            s2 = pow(N, -1, p)  # placeholder, replaced below
            # check: S0 in {0, s, -s, 2s, -2s} where s^2 = N (if square)
            sq = [s for s in range(p) if (s * s) % p == N]
            if sq:
                s = sq[0]
                if S0 not in {0, s, (-s) % p, (2 * s) % p, (-2 * s) % p}:
                    print(f"  S0 OUT OF RANGE p={p} t={t} S0={S0} s={s}")
            else:
                if idx0:
                    print(f"  N NONSQUARE BUT t=0 EXISTS p={p} t={t}")
            if len(idx0) > 2:
                print(f"  n0 > 2! p={p} t={t} n0={len(idx0)}")
            if coeff is not None and coeff != 0:
                n_s2nz += 1
        print(f"p={p} t={t}: |H0|={H0} gap={n} preserved={n_pres} "
              f"b1!=0={n_b1nz} S2-coeff!=0 in {n_s2nz}/{n}")
        tot += n
        preserved += n_pres
print(f"TOTAL gap={tot} preserved={preserved} formula-mismatches={bad_formula}")
print("examples of preserved genuine twists:", examples)
print("DONE")
