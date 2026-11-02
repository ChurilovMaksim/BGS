"""Wave 24, task 5 probe: Teichmuller decomposition + delta for second-digit lemma.

R = Z[sqrt(2)], p odd. For A unit mod p^2:
  A = tau_A * (1 + p*lam_A), tau_A in Teichmuller subgroup T (order m, coprime to p).
  v1_j = second digit of Tr(A*alpha^j) = d1_j + Tr(tau_j * lam_A),
  where d1_j = second digit of Tr(tau_j), tau_j = tau_A * alpha^j mod p.
  Claim to test: d1_j = Tr(tau_j * delta) for a FIXED delta (depends only on tau_A),
  so v1_j = Tr(tau_j * lam_tilde), lam_tilde = lam_A + delta.
  Then twist lam -> lam + c*sqrt(2) shifts lam_tilde the same way.
  Questions: is e = sqrt2-coeff(delta) ever nonzero? In gap case (B real)?
  Does c = -2*b_tilde preserve the v1-marginal for genuine twists?
Exact integer arithmetic, p = 13 first.
"""

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

def conj(a, mod):
    return (a[0] % mod, (-a[1]) % mod)

def tr(a, mod):
    return (2 * a[0]) % mod

def norm(a, mod):
    return (a[0]*a[0] - 2*a[1]*a[1]) % mod

def inv(a, mod):
    # a unit mod p^2 (p prime, R/p^2 local-ish: use a * conj(a) = N, invert N mod mod)
    n = norm(a, mod) % mod
    # n must be coprime to p; invert mod mod via extended Eucldiean on integers
    import math
    assert math.gcd(n, mod) == 1 or True
    ni = pow(n, -1, mod)
    c = conj(a, mod)
    return ((c[0]*ni) % mod, (c[1]*ni) % mod)

def modp_elem(a, p):
    return (a[0] % p, a[1] % p)

def second_digit(val_mod_p2, p):
    # val in Z/p^2; returns (val mod p, (val - (val mod p))/p mod p)
    v0 = val_mod_p2 % p
    v1 = ((val_mod_p2 - v0) // p) % p
    return v0, v1

def teich(A, p, m):
    mod = p * p
    w = A
    wm = pw(w, m, mod)
    # wm should be 1 + p*u
    assert wm[0] % p == 1 and wm[1] % p == 0, wm
    u = ((wm[0] - 1) // p % p, wm[1] // p % p)
    mi = pow(m, -1, p)
    adj = (1, 0)
    adj = ((adj[0] - p * (u[0]*mi % p)) % mod, (adj[1] - p * (u[1]*mi % p)) % mod)
    tau = mul(w, adj, mod)
    assert pw(tau, m, mod) == (1, 0), (tau, pw(tau, m, mod))
    assert modp_elem(tau, p) == modp_elem(A, p)
    return tau

def lam_of(A, tau, p):
    mod = p * p
    q = mul(A, inv(tau, mod), mod)
    assert q[0] % p == 1 and q[1] % p == 0, q
    return ((q[0] - 1) // p % p, q[1] // p % p)

def solve_delta(tau, alpha, p):
    mod = p * p
    # d1_0, d1_1: second digits of Tr(tau), Tr(tau*alpha)
    t0 = tr(tau, mod)
    t1 = tr(mul(tau, alpha, mod), mod)
    _, d10 = second_digit(t0, p)
    _, d11 = second_digit(t1, p)
    xb, yb = modp_elem(tau, p)  # xi_bar, eta_bar
    # equations: 2*xb*d + 4*yb*e = d10 ; 2*(3xb+4yb)*d + 4*(2xb+3yb)*e = d11
    # solve 2x2 over F_p
    A11, A12, B1 = (2*xb) % p, (4*yb) % p, d10
    A21, A22, B2 = (2*(3*xb + 4*yb)) % p, (4*(2*xb + 3*yb)) % p, d11
    det = (A11*A22 - A12*A21) % p
    assert det != 0
    di = pow(det, -1, p)
    d = ((B1*A22 - A12*B2) * di) % p
    e = ((A11*B2 - B1*A21) * di) % p
    return (d, e)

def run(p):
    mod = p * p
    alpha = (3, 2)
    # L0 = order of alpha mod p
    L0 = None
    cur = (1, 0)
    for j in range(1, 2*p + 5):
        cur = mul(cur, alpha, p)
        if cur == (1, 0):
            L0 = j
            break
    assert L0 is not None
    eps = 1 if p % 8 in (1, 7) else -1
    m = (p - 1) ** 2 if eps == 1 else p * p - 1
    print(f"p={p} L0={L0} m={m} alpha^L0 mod p^2 = {pw(alpha, L0, mod)}")
    # iterate all units mod p^2
    n_units = 0
    bad_formula = 0
    e_nonzero = 0
    e_nonzero_gap = 0
    gap = 0
    preserved_genuine = []
    for x in range(mod):
        for y in range(mod):
            if norm((x, y), p) == 0:
                continue
            A = (x, y)
            n_units += 1
            tau = teich(A, p, m)
            lam = lam_of(A, tau, p)
            delta = solve_delta(tau, alpha, p)
            lamt = add(lam, delta, p)
            # verify v1_j = Tr(tau_j * lamt) for all j
            ok = True
            v1s = []
            for j in range(L0):
                aj = pw(alpha, j, mod)
                w = mul(A, aj, mod)
                _, v1 = second_digit(tr(w, mod), p)
                v1s.append(v1)
                tauj = modp_elem(mul(tau, aj, mod), p)
                if tr(mul(tauj, lamt, p), p) != v1:
                    ok = False
                    break
            if not ok:
                bad_formula += 1
                if bad_formula <= 3:
                    print("FORMULA FAIL", A, tau, lam, delta)
                continue
            b = lam[1]
            bt = lamt[1]
            e = delta[1]
            if e != 0:
                e_nonzero += 1
            # B = A^L0 mod p^2; gap iff sqrt2-coeff of B == 0 mod p
            B = pw(A, L0, mod)
            is_gap = (B[1] % p == 0)
            if is_gap:
                gap += 1
                if e != 0:
                    e_nonzero_gap += 1
            # test c* = -2*bt: marginal preservation + genuineness
            if is_gap and e != 0:
                cstar = (-2 * bt) % p
                if cstar != 0:
                    # twisted v1 marginal: v1_j + cstar * t_j, t_j = Tr(A sqrt2 aj) mod p
                    v1p = []
                    for j in range(L0):
                        aj = pw(alpha, j, mod)
                        tj = tr(mul(mul(A, (0, 1), mod), aj, mod), p)
                        v1p.append((v1s[j] + cstar * tj) % p)
                    if sorted(v1p) == sorted(v1s):
                        # genuine? cstar != -2b (since e!=0, -2bt != -2b) and B real
                        preserved_genuine.append((A, cstar, b, bt))
    print(f"units={n_units} gap(B real)={gap} bad_formula={bad_formula}")
    print(f"e!=0: {e_nonzero}, e!=0 and gap: {e_nonzero_gap}")
    print(f"genuine marginal preservations at c*=-2bt: {len(preserved_genuine)}")
    for ex in preserved_genuine[:5]:
        print("  example:", ex)

run(13)
