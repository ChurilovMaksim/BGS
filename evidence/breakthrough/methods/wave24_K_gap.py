"""Wave 24, task 5 probe 3: K=0 iff gap-type? + rho=1 identity.

gap-type(tau): (a/abar) in <abar_alpha> where a = tau mod p, i.e.
(a/abar)^L0 == 1. (Equivalently B real for any A with this tau.)
Symmetry lemma prediction: if gap-type, with r s.t. abar/a = abar_alpha^r,
then rho = (tau_bar/tau) * alpha^{-r} == 1 exactly in R/p^2, hence
Tbar_j = T_{r-j} exactly, hence K = 0.
Check at p=31: crosstab (gap?, K==0?) over all tau in T, and rho==1.
Exact integer arithmetic.
"""
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

def conj(a, mod):
    return (a[0] % mod, (-a[1]) % mod)

def teich(A, p, m):
    mod = p * p
    wm = pw(A, m, mod)
    u = ((wm[0] - 1) // p % p, wm[1] // p % p)
    mi = pow(m, -1, p)
    adj = ((1 - p * (u[0]*mi % p)) % mod, (-p * (u[1]*mi % p)) % mod)
    tau = mul(A, adj, mod)
    assert pw(tau, m, mod) == (1, 0) and modp(tau, p) == modp(A, p)
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
    abar = modp(alpha, p)
    # powers of abar in R/p
    abar_pows = {}
    cur = (1, 0)
    for r in range(L0):
        abar_pows[cur] = r
        cur = mul(cur, abar, p)
    assert len(abar_pows) == L0
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
    from collections import Counter
    ct = Counter()
    rho_fail = 0
    rho_checked = 0
    for tau in taus:
        a = modp(tau, p)
        abar_a = conj(a, p)
        # gap-type: (a/abar_a)^L0 == 1 ; need inverse of abar_a mod p
        inv_ab = (abar_a[0], -abar_a[1])
        # inverse via norm: abar_a^{-1} = conj(abar_a)/N
        n = norm(abar_a, p) % p
        ni = pow(n, -1, p)
        inv_ab = ((abar_a[0]*ni) % p, (-abar_a[1]*ni) % p)
        ratio = mul(a, inv_ab, p)  # a / abar
        gap = (pw(ratio, L0, p) == (1, 0))
        # K
        S = 0
        for j in range(L0):
            tj = mul(tau, pw(alpha, j, mod), mod)
            tval = tr(tj, mod)
            d1 = ((tval - tval % p) // p) % p
            eta = modp(tj, p)[1]
            S = (S + d1 * eta) % p
        N = norm(tau, p) % p
        K = (-2 * S * pow(L0 * N % p, -1, p)) % p
        ct[(gap, K == 0)] += 1
        if gap:
            # abar/a should be in <abar>: find r with abar^r == abar_a/a
            # abar_a/a: inverse of ratio
            inv_ratio = ((ratio[0]*pow(norm(ratio, p) % p, -1, p)) % p,
                         (-ratio[1]*pow(norm(ratio, p) % p, -1, p)) % p)
            r = abar_pows.get(inv_ratio)
            assert r is not None, (tau, inv_ratio)
            # rho = (tau_bar/tau) * alpha^{-r} in R/p^2, expect == (1,0)
            tbar = conj(tau, mod)
            # tau^{-1} mod p^2: conj(tau)/N(tau)
            nt = norm(tau, mod) % mod
            nti = pow(nt, -1, mod)
            tau_inv = ((tau[0]*nti) % mod, (-tau[1]*nti) % mod)
            rho = mul(mul(tbar, tau_inv, mod), pw(alpha, -r % (L0), mod), mod)
            # note: alpha^{-r} mod p^2: use pw with exponent L0*? alpha^{L0}=1 mod p^2, so alpha^{-r} = alpha^{L0-r}
            rho_checked += 1
            if rho != (1, 0):
                rho_fail += 1
                if rho_fail <= 3:
                    print("RHO FAIL", tau, r, rho)
    print(f"p={p} crosstab (gap, K==0): {dict(ct)}")
    print(f"rho==1 checked: {rho_checked}, failed: {rho_fail}")

run(31)
