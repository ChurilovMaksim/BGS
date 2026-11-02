"""Wave 29, task 1 check: r=2 ring power sum for the R30 v2 step.

Claims (exact arithmetic in R = Z[sqrt(2)] mod p^3, Teichmueller beta):
  (A) sum_j v_j*W_j == 0 mod p^3, where v_j = Tr(C tb^j),
      W_j = Tr(C tb^j sqrt2).
  (B) sum_j W_j^2 == -4*|H0|*N(C) mod p^3.
  (C) For C' = C(1+pc sqrt2), c != 0: sum(v'^2)-sum(v^2) ==
      p^2*c^2*(-4*|H0|*N(C)) mod p^3, hence != 0: twist detected.
  (D) Borrow mechanism (gap case): delta_{r-j} == conj(delta_j) + b,
      b = (0, p-1) if eta_j != 0 else (0,0); hence w is NOT odd
      under gap symmetry, so sum xi*w != 0 in general.
Checked for random units C (not only gap) at p = 5, 7, 13.
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
    assert pw(tau, m, M) == (1, 0)
    return tau


def tr(u):
    return (2 * u[0])


random.seed(31)
tot = 0
for p in (5, 7, 13):
    M = p ** 3
    alpha = (3, 2)
    for t in (1, 2, 4):
        beta = pw(alpha, t, M)
        tb = teich(beta, p)
        H0 = order_mod_p((beta[0] % p, beta[1] % p), p)
        if H0 < 3:
            continue
        n = 0
        for _ in range(60):
            while True:
                C = (random.randrange(M), random.randrange(M))
                if (C[0] * C[0] - 2 * C[1] * C[1]) % p != 0:
                    break
            N = (C[0] * C[0] - 2 * C[1] * C[1]) % M
            vs, Ws = [], []
            for j in range(H0):
                X = mul(C, pw(tb, j, M), M)
                vs.append(tr(X) % M)
                Ws.append(tr(mul(X, (0, 1), M)) % M)
            # (A), (B)
            assert sum((v * w) % M for v, w in zip(vs, Ws)) % M == 0
            assert sum((w * w) % M for w in Ws) % M == \
                (-4 * H0 * N) % M
            # (C) for a random nonzero c
            c = random.randrange(1, p)
            Cp = ((C[0] + 2 * C[1] * p * c) % M,
                  (C[1] + C[0] * p * c) % M)
            vps = []
            for j in range(H0):
                vps.append(tr(mul(Cp, pw(tb, j, M), M)) % M)
            diff = (sum((v * v) % M for v in vps) -
                    sum((v * v) % M for v in vs)) % M
            assert diff == (p * p * c * c * (-4 * H0 * N)) % M
            assert diff != 0
            n += 1
        tot += n
        print(f"p={p} t={t}: |H0|={H0} ring-identities-ok={n}")
print(f"TOTAL ring checks passed: {tot}")

# (D) borrow mechanism in one gap case (p=5, t=2, A=(44,76) from debug)
p, t = 5, 2
M = p ** 3
beta = pw((3, 2), t, M)
tb = teich(beta, p)
H0 = order_mod_p((beta[0] % p, beta[1] % p), p)
A = (44, 76)
tauA = teich(A, p)
tc = (tauA[0] % M, (-tauA[1]) % M)
rs = [r for r in range(H0) if mul(tauA, pw(tb, r, M), M) == tc]
r = rs[0]
Tj = [mul(tauA, pw(tb, j, M), M) for j in range(H0)]
for j in range(H0):
    T = Tj[j]
    tbar = (T[0] % p, T[1] % p)
    delta = (((T[0] - tbar[0]) // p) % p, ((T[1] - tbar[1]) // p) % p)
    jj = (r - j) % H0
    T2 = Tj[jj]
    tbar2 = (T2[0] % p, T2[1] % p)
    delta2 = (((T2[0] - tbar2[0]) // p) % p, ((T2[1] - tbar2[1]) // p) % p)
    b = (0, p - 1) if tbar[1] != 0 else (0, 0)
    pred = ((delta[0] + b[0]) % p, (-delta[1] + b[1]) % p)
    # conj(delta) in R/p is (u, -w); plus borrow b
    assert delta2 == pred, f"borrow formula fails j={j}"
    print(f"j={j}: delta={delta} delta_r-j={delta2} borrow-pred={pred} "
          f"eta={tbar[1]} w_odd_would_give={(delta[0], (-delta[1]) % p)}")
print("BORROW FORMULA VERIFIED")
print("ALL CHECKS PASS")
