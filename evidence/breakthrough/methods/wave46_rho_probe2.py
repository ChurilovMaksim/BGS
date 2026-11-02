from collections import defaultdict
ALPHA = (3, 2)
def mul(a, b, M): return ((a[0]*b[0]+2*a[1]*b[1]) % M, (a[0]*b[1]+a[1]*b[0]) % M)
def pw(a, n, M):
    r = (1, 0)
    while n:
        if n & 1: r = mul(r, a, M)
        a = mul(a, a, M); n >>= 1
    return r
print("alpha^16 mod 8192:", pw(ALPHA, 16, 8192), " alpha^32 mod 8192:", pw(ALPHA, 32, 8192))
# search primes q with alpha^32=1, alpha^16 != 1
def primes(n):
    s = [True]*(n+1); s[0]=s[1]=False
    for i in range(2, int(n**0.5)+1):
        if s[i]:
            for j in range(i*i, n+1, i): s[j]=False
    return [i for i, v in enumerate(s) if v]
found = []
for q in primes(20000):
    if pw(ALPHA, 32, q) == (1,0) and pw(ALPHA, 16, q) != (1,0):
        found.append((q, pw(ALPHA, 16, q)))
print("order-32-alpha primes <=20000:", found[:20], "count:", len(found))
# B2 scan: cross-class p-collisions?
def seq(B, M):
    ap = [pw(ALPHA, i, M) for i in range(32)]
    return [(2*mul(B, a, M)[0]) % M for a in ap]
bad2 = []
for x in range(8192):
    for y in range(8192):
        pass
    break
# vectorized-ish: iterate B2 but break early on first cross-class collision
import itertools
bad2 = []
for x in range(8192):
    # only need y up to symmetry? just do all, but cheap: precompute powers once
    pass
ap8 = [pw(ALPHA, i, 8192) for i in range(32)]
def seq_fast(B, ap, M):
    return [(2*((B[0]*a[0]+2*B[1]*a[1]) % M)) % M for a in ap]
bad2 = []
for x in range(8192):
    for y in range(8192):
        p = seq_fast((x,y), ap8, 8192)
        seen = {}
        mixed = False
        for i, v in enumerate(p):
            c = i % 4
            if v in seen and seen[v] != c: mixed = True; break
            seen[v] = c
        if mixed: bad2.append((x,y))
    if x % 2048 == 0: print(f"  B2 scan x={x}, bad so far={len(bad2)}", flush=True)
print("B2 with cross-class p-collision:", len(bad2), bad2[:20])
