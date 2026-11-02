"""Wave 27, task 1: test identity (I1) Tr(u1) == 2*mu^2 mod p across primes.
alpha = 3+2 sqrt2. L0 = order of alpha mod p. gamma = alpha^L0 mod p^2.
u = (gamma-1)/p mod p^2. Check: Re(u) == 0 mod p (Lemma A), mu = Im(u) mod p,
u1 = (u - mu*sqrt2)/p mod p. Test Tr(u1) == 2*mu^2 mod p. Only k=1 primes
(u != 0 mod p) are relevant; record k>=2 primes separately.
"""
def primes_upto(n):
    sieve = [True]*(n+1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5)+1):
        if sieve[i]:
            for j in range(i*i, n+1, i):
                sieve[j] = False
    return [i for i, v in enumerate(sieve) if v]

def mulmod(x, y, m):
    return ((x[0]*y[0] + 2*x[1]*y[1]) % m, (x[0]*y[1] + x[1]*y[0]) % m)

bad = []
k_ge_2 = []
checked = 0
for p in primes_upto(500):
    if p == 2:
        continue
    # order of alpha mod p
    cur = (1, 0)
    L0 = None
    for i in range(1, 4*p+10):
        cur = mulmod(cur, (3, 2), p)
        if cur == (1, 0):
            L0 = i
            break
    assert L0 is not None
    # gamma = alpha^L0 mod p^3 (need mod p^3 to get u mod p^2)
    cur = (1, 0)
    for _ in range(L0):
        cur = mulmod(cur, (3, 2), p*p*p)
    gamma = cur
    if gamma[0] % p != 1 or gamma[1] % p != 0:
        print("gamma != 1 mod p at", p, gamma)
        continue
    u = ((gamma[0]-1)//p % p, gamma[1]//p % p)
    if u == (0, 0):
        k_ge_2.append(p)
        continue
    # Lemma A: Re(u) == 0 mod p
    if u[0] % p != 0:
        print("Lemma A fails at", p, u)
        continue
    mu = u[1] % p
    # u mod p^2 from gamma mod p^3:
    ux = (gamma[0]-1)//p % (p*p)
    uy = gamma[1]//p % (p*p)
    # u_full = mu*sqrt2 + p*u1 (mod p^2) with u1 in R/p:
    # ux = p * Re(u1) mod p^2 ; uy = mu + p * Im(u1) mod p^2
    assert ux % p == 0
    re_u1 = (ux//p) % p
    im_u1 = ((uy - mu)//p) % p
    tr_u1 = (2*re_u1) % p
    if tr_u1 != (2*mu*mu) % p:
        bad.append((p, L0, mu, re_u1, im_u1, tr_u1))
    checked += 1
print("k=1 primes checked:", checked)
print("k>=2 primes (skipped):", k_ge_2)
print("(I1) violations:", len(bad))
for b in bad[:20]:
    print("  p, L0, mu, Re(u1), Im(u1), Tr(u1) =", b)
