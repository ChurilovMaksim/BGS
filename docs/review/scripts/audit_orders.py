"""
AUDIT: independent computation of ord_p(alpha), projective order of A,
and quantum period K for the primes used in the paper's perturbation
experiments. Zero dependencies beyond stdlib. Exact integer arithmetic.

Definitions (paper, Sec 2.1):
  alpha  : split eigenvalue of A mod p in F_p^x
  k      : ord_p(alpha)
  K      : order of the image of A in PSL(2,Z/p) = least j>0 with
           A^j == +-I (mod p)
  m      : eigenspace dimension ~ floor or ceil of p/K_uphase where
           K_uphase (quantum period with U_A^K = chi*I) is K or 2K
           depending on the metaplectic sign convention.
We report both K_proj (order in PSL) and the multiplicity scale p/K_proj.
"""
import os as _os
_BGS_ROOT = _os.path.dirname(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))
import json
from sympy import primerange

def matmul(X, Y, p):
    return ((X[0]*Y[0] + X[1]*Y[2]) % p, (X[0]*Y[1] + X[1]*Y[3]) % p,
            (X[2]*Y[0] + X[3]*Y[2]) % p, (X[2]*Y[1] + X[3]*Y[3]) % p)

def matpow(A, n, p):
    R = (1, 0, 0, 1)
    while n:
        if n & 1:
            R = matmul(R, A, p)
        A = matmul(A, A, p)
        n >>= 1
    return R

def proj_order(A, p):
    """Least j>=1 with A^j == +I or -I (mod p). Exact."""
    j, X = 1, A
    while True:
        if X == (1, 0, 0, 1):
            return j, +1
        if X == (p - 1, 0, 0, p - 1):
            return j, -1
        X = matmul(X, A, p)
        j += 1

def sl_order(A, p):
    """Least j>=1 with A^j == +I."""
    j, X = 1, A
    while X != (1, 0, 0, 1):
        X = matmul(X, A, p)
        j += 1
    return j

def ord_alpha(A, p):
    """Split eigenvalue alpha of A mod p and its order. None if inert."""
    a, b, c, d = A
    tr = (a + d) % p
    disc = (tr * tr - 4) % p
    if disc == 0:
        return None, None, None
    # Tonelli-Shanks
    if pow(disc, (p - 1) // 2, p) != 1:
        return None, None, None
    if p % 4 == 3:
        r = pow(disc, (p + 1) // 4, p)
    else:
        q, s = p - 1, 0
        while q % 2 == 0:
            q //= 2; s += 1
        z = 2
        while pow(z, (p - 1) // 2, p) != p - 1:
            z += 1
        m, cc, t, r2 = s, pow(z, q, p), pow(disc, q, p), pow(disc, (q + 1) // 2, p)
        while t != 1:
            i, t2 = 0, t
            while t2 != 1:
                t2 = t2 * t2 % p; i += 1
            b = pow(cc, 1 << (m - i - 1), p)
            m, cc, t, r2 = i, b * b % p, t * b * b % p, r2 * b % p
        r = r2
    inv2 = pow(2, -1, p)
    alpha = (tr + r) * inv2 % p
    # order of alpha
    k, x = 1, alpha
    while x != 1:
        x = x * alpha % p
        k += 1
    return alpha % p, k, r

AROLD = (2, 1, 1, 1)

cases = {
    "exp_multi": [(1597,), (2161,), (2207,), (3001,)],
    "exp_beta":  [(3571,), (4481,), (5779,)],
    "ledger_R27": [(4481,), (2207,), (3001,)],
}

out = {}
for group, plist in cases.items():
    rows = []
    for (p,) in plist:
        alpha, k, _ = ord_alpha(AROLD, p)
        kp, sign_hit = proj_order(AROLD, p)
        slord = sl_order(AROLD, p)
        rows.append(dict(p=p, split=(alpha is not None),
                         ord_alpha=k,
                         proj_order_K=kp,
                         hit_minus_I=(sign_hit == -1),
                         sl_order=slord,
                         p_over_K=round(p / kp, 2)))
        print(f"{group} p={p}: ord(a)={k}  K_proj={kp} "
              f"(hit -I at {kp}? {sign_hit==-1})  SL_ord={slord}  "
              f"p/K={p/kp:.1f}")
    out[group] = rows

with open(_BGS_ROOT + r"\artifacts\audit_orders.json", "w") as f:
    json.dump(out, f, indent=1)
print("saved artifacts/audit_orders.json")
