"""Wave 42, task 2: roots-of-unity ambiguity mu_1 vs <beta> per component.

R = Z[sqrt(2)], beta = 17+12*sqrt(2) (norm 1, beta+beta^-1 = 34).
For parameter modulus Q = p^f, compute:
  ord(beta) in R/QR, <beta>,
  mu_1 = {zeta in (R/QR)^x : zeta^ord = 1, N(zeta) = 1},
and report whether mu_1 strictly exceeds <beta>.
Also ord(beta) mod p (residue order) to see order collapse.
"""

def rmul(x, y, mod):
    a, b = x
    c, d = y
    return ((a * c + 2 * b * d) % mod, (a * d + b * c) % mod)


def rpow(x, n, mod):
    r = (1 % mod, 0)
    while n:
        if n & 1:
            r = rmul(r, x, mod)
        x = rmul(x, x, mod)
        n >>= 1
    return r


def norm(x, mod):
    return (x[0] * x[0] - 2 * x[1] * x[1]) % mod


def order_of(x, mod, divs):
    for d in divs:
        if rpow(x, d, mod) == (1 % mod, 0):
            return d
    return None


def divisors(n):
    ds = set()
    i = 1
    while i * i <= n:
        if n % i == 0:
            ds.add(i)
            ds.add(n // i)
        i += 1
    return sorted(ds)


def analyze(Q, p):
    mod = Q
    beta = (17 % mod, 12 % mod)
    # order of beta: beta^u = 1 for u = multiple of order; bound search:
    # compute powers until 1, cap at Q^2
    cur = (1 % mod, 0)
    ord_beta = None
    for k in range(1, mod * mod + 1):
        cur = rmul(cur, beta, mod)
        if cur == (1 % mod, 0):
            ord_beta = k
            break
    assert ord_beta is not None
    # <beta>
    gen = set()
    cur = (1 % mod, 0)
    for _ in range(ord_beta):
        gen.add(cur)
        cur = rmul(cur, beta, mod)
    # mu_1: enumerate units (norm coprime to Q)
    import math
    mu1 = set()
    for a in range(mod):
        for b in range(mod):
            if math.gcd(norm((a, b), mod), mod) != 1:
                continue
            z = (a, b)
            if rpow(z, ord_beta, mod) == (1 % mod, 0) and norm(z, mod) == 1:
                mu1.add(z)
    extra = mu1 - gen
    # residue order: beta mod p (work mod p)
    beta_p = (17 % p, 12 % p)
    cur = (1 % p, 0)
    ord_p = None
    for k in range(1, p * p + 1):
        cur = rmul(cur, beta_p, p)
        if cur == (1 % p, 0):
            ord_p = k
            break
    print(f"Q={Q} p={p}: ord(beta)={ord_beta} |<beta>|={len(gen)} "
          f"|mu_1|={len(mu1)} extra={len(extra)} ord_mod_p={ord_p} "
          f"collapse={ord_p != ord_beta}")
    if extra:
        ex = sorted(extra)[:6]
        print(f"   extra zeta sample: {ex}")
    return ord_beta, gen, mu1, extra


if __name__ == "__main__":
    comps = [(5, 5), (13, 13), (25, 5), (29, 29), (37, 37), (53, 53),
             (59, 59), (73, 73), (83, 83), (101, 101), (113, 113),
             (137, 137), (169, 13), (197, 197), (19, 19), (11, 11),
             (9, 3), (3, 3)]
    for Q, p in comps:
        analyze(Q, p)
