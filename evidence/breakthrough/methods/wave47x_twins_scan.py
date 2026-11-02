# Wave 47x task B: scan split primes p for (a) v2(ord(eps1 mod p))==2 [odd-u admissibility],
# (b) p | ord(beta mod p^2) [twin level condition at f=2, a=1].
def primes_upto(n):
    sieve = [True]*(n+1); out = []
    for i in range(2, n+1):
        if sieve[i]:
            out.append(i)
            for j in range(i*i, n+1, i): sieve[j] = False
    return out
def order_of(x, mod):
    o, y = 1, x
    while y != 1:
        y = y*x % mod; o += 1
        if o > 4*mod: return None
    return o
def v2(n):
    c = 0
    while n % 2 == 0: n //= 2; c += 1
    return c
def hensel_r(p, f):
    mod = p**f
    r0 = next((r for r in range(p) if (r*r - 2) % p == 0), None)
    if r0 is None: return None
    r, m = r0, p
    while m < mod:
        for t in range(p):
            cand = r + t*m
            if (cand*cand - 2) % (m*p) == 0:
                r, m = cand, m*p; break
        else: return None
    return r % mod
hits = []
for p in primes_upto(2000):
    if p == 2: continue
    r = hensel_r(p, 1)
    if r is None: continue  # inert
    eps1 = (1 + r) % p
    oe = order_of(eps1, p)
    if oe is None: continue
    if v2(oe) != 2: continue
    # lift to p^2, check p | ord(beta)
    r2 = hensel_r(p, 2)
    b2 = (17 + 12*r2) % (p*p)
    T2 = order_of(b2, p*p)
    hits.append((p, oe, T2, T2 % p == 0))
    print(f"split p={p} v2(ord(eps1))==2: ord(eps1)={oe} ord(beta mod p^2)={T2} p|T2? {T2 % p == 0}", flush=True)
print("total v2==2 split primes <=2000:", len(hits))
print("with p|T2:", [h[0] for h in hits if h[3]])
