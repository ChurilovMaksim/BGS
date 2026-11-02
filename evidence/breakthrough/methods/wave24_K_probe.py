"""Wave 24, task 5 probe 2: the P_2 obstruction constant K(tau).

For fixed tau_A in T (Teichmuller), orbit tau_j = tau_A * alpha^j mod p^2:
  d1_j = second digit of Tr(tau_j)  (Tr in Z/p^2)
  eta_j = sqrt2-coeff of (tau_j mod p)
  S = sum_j d1_j * eta_j  (mod p)
  K = -2*S / (L0 * N(tau_A))  (mod p)
P_2 lemma (rigorous): if v1-marginal preserved by twist c != 0 then
2b + c = K, i.e. c = K - 2b, where b = sqrt2-coeff of lam_A.
Questions: distribution of K over tau in T at p=13, p=31.
Also: direct marginal test for A = tau (lam=0, b=0), c = K (if nonzero):
P_2-blind by construction; is the full marginal preserved? (Would be a
genuine counterexample if yes.)
Exact integer arithmetic.
"""
import math

def add(a, b, mod):
    return ((a[0] + b[0]) % mod, (a[1] + b[1]) % mod)

def mul(a, b, mod):
    return ((a[0]*b[0] + 2*a[1]*b[1]) % mod, (a[0]*b[1] + a[1]*b[0]) % mod)

def pw(a, n, mod):
    r = (1, 0)
    while n:
        if n & 1:
            r = mul(r, a, mod)
        a = mul(a, a, mod)
        n >>= 1
    return r

def tr(a, mod):
    return (2 * a[0]) % mod

def norm(a, mod):
    return (a[0]*a[0] - 2*a[1]*a[1]) % mod

def modp(a, p):
    return (a[0] % p, a[1] % p)

def teich(A, p, m):
    mod = p * p
    wm = pw(A, m, mod)
    assert wm[0] % p == 1 and wm[1] % p == 0
    u = ((wm[0] - 1) // p % p, wm[1] // p % p)
    mi = pow(m, -1, p)
    adj = ((1 - p * (u[0]*mi % p)) % mod, (-p * (u[1]*mi % p)) % mod)
    tau = mul(A, adj, mod)
    assert pw(tau, m, mod) == (1, 0)
    assert modp(tau, p) == modp(A, p)
    return tau

def run(p):
    mod = p * p
    alpha = (3, 2)
    L0 = None
    cur = (1, 0)
    for j in range(1, 2*p + 5):
        cur = mul(cur, alpha, p)
        if cur == (1, 0):
            L0 = j
            break
    eps = 1 if p % 8 in (1, 7) else -1
    m = (p - 1) ** 2 if eps == 1 else p * p - 1
    print(f"p={p} L0={L0} m={m}")
    # all tau in T: teich lifts of all units mod p
    taus = []
    seen = set()
    for x in range(p):
        for y in range(p):
            if norm((x, y), p) == 0:
                continue
            tau = teich((x, y), p, m)
            if tau not in seen:
                seen.add(tau)
                taus.append(tau)
    print(f"|T| = {len(taus)} (expect {m})")
    from collections import Counter
    Kdist = Counter()
    K_nonzero_taus = []
    for tau in taus:
        S = 0
        for j in range(L0):
            tj = mul(tau, pw(alpha, j, mod), mod)
            tval = tr(tj, mod)
            v0 = tval % p
            d1 = ((tval - v0) // p) % p
            eta = modp(tj, p)[1]
            S = (S + d1 * eta) % p
        N = norm(tau, p) % p
        K = (-2 * S * pow(L0 * N % p, -1, p)) % p
        Kdist[K] += 1
        if K != 0:
            K_nonzero_taus.append((tau, K))
    print("K distribution:", dict(Kdist))
    # direct marginal test for A = tau (b=0), c = K != 0
    n_pres = 0
    n_test = 0
    for tau, K in K_nonzero_taus[:50]:
        # A = tau: lam = 0, so v1_j = d1_j; t_j = Tr(tau*sqrt2*alpha^j) mod p
        v1s = []
        ts = []
        for j in range(L0):
            tj = mul(tau, pw(alpha, j, mod), mod)
            tval = tr(tj, mod)
            v1s.append(((tval - tval % p) // p) % p)
            uj = mul(mul(tau, (0, 1), mod), pw(alpha, j, mod), mod)
            ts.append(tr(uj, p))
        v1p = sorted((v1s[j] + K * ts[j]) % p for j in range(L0))
        n_test += 1
        if v1p == sorted(v1s):
            n_pres += 1
            print("MARGINAL PRESERVED (genuine, b=0, c=K):", tau, K)
    print(f"direct tests: {n_test}, preserved: {n_pres}")

run(13)
run(31)
