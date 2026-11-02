"""Wave 14, task 1, part 2.
1. k-search to 10000: any k=2 prime with 4|L0? any k>=3 prime?
2. Brute force f=2 s=0 at p=13, m=14, t=2, mod 169 (all A in R/169).
3. Brute force f=3 (1,2) at p=5 (if k=1): m = 25*L0, mod 125.
4. (2,1) digit sanity at p=13, m=182, mod 2197: A'' = A(1+169*eta),
   Tr(eta)=0 vs Tr(eta)!=0.
"""
from math import gcd

def mul(x, y, n):
    a, b = x; c, d = y
    return ((a*c + 2*b*d) % n, (a*d + b*c) % n)

def pw(x, e, n):
    r = (1, 0)
    while e:
        if e & 1: r = mul(r, x, n)
        x = mul(x, x, n); e >>= 1
    return r

def primes_upto(N):
    sieve = bytearray(b'\x01') * (N+1)
    sieve[0:2] = b'\x00\x00'
    for i in range(2, int(N**0.5)+1):
        if sieve[i]:
            sieve[i*i:N+1:i] = b'\x00' * ((N - i*i)//i + 1)
    return [i for i in range(N+1) if sieve[i]]

def vp_int(v, p):
    if v == 0: return 99
    c = 0
    while v % p == 0:
        v //= p; c += 1
    return c

def order_and_k(p):
    x = (3 % p, 2 % p)
    cur = x; L0 = 1
    while cur != (1, 0):
        cur = mul(cur, x, p); L0 += 1
        if L0 > 2*p + 2: raise RuntimeError(p)
    a4 = pw((3, 2), L0, p**4)
    k = min(vp_int(a4[0]-1, p), vp_int(a4[1], p))
    return L0, k

def d_orbit(t, tup):
    out = set()
    for b in range(t):
        out.add(tuple(tup[(i+b) % t] for i in range(t)))
        out.add(tuple(tup[(-i+b) % t] for i in range(t)))
    return out

def brute(n, m, t):
    """Exhaustive G1' check: all A in R/n, sequences length m, classes mod t.
    Returns (ngroups, bad)."""
    alpha = (3, 2)
    pwrs = [(1, 0)]
    for i in range(1, m): pwrs.append(mul(pwrs[-1], alpha, n))
    groups = {}
    for a in range(n):
        for b in range(n):
            vals = tuple((2*((a*pwrs[i][0] + 2*b*pwrs[i][1]) % n)) % n
                         for i in range(m))
            g = tuple(sorted(vals))
            cl = tuple(tuple(sorted(vals[i] for i in range(m) if i % t == r))
                       for r in range(t))
            groups.setdefault(g, []).append(cl)
    bad = 0
    for g, cls in groups.items():
        orb = d_orbit(t, cls[0])
        if any(c not in orb for c in cls): bad += 1
    return len(groups), bad

def seq_vals(A, m, n):
    alpha = (3, 2)
    cur = (1, 0); vals = []
    for i in range(m):
        vals.append((2*((A[0]*cur[0] + 2*A[1]*cur[1]) % n)) % n)
        cur = mul(cur, alpha, n)
    return vals

def classes_of(vals, m, t):
    return tuple(tuple(sorted(vals[i] for i in range(m) if i % t == r))
                 for r in range(t))

print("=== 1. k-search to 10000 ===")
k2div4, k3 = [], []
for p in primes_upto(10000):
    if p == 2: continue
    L0, k = order_and_k(p)
    if k >= 3: k3.append((p, L0, k))
    elif k == 2 and L0 % 4 == 0: k2div4.append((p, L0))
print("k>=3 primes <=10000:", k3)
print("k=2 primes <=10000 with 4|L0:", k2div4)
print()
print("=== 2. f=2 s=0 brute force, p=13, m=14, t=2, mod 169 ===")
ng, bad = brute(169, 14, 2)
print(f"groups={ng} bad_groups={bad}")
print()
print("=== 3. p=5 parameters + f=3 (1,2) brute force ===")
L0, k = order_and_k(5)
print(f"p=5: L0={L0} k={k}")
if k == 1:
    m = 25*L0; t = gcd(m, 4)
    ng, bad = brute(125, m, t)
    print(f"(m,p)=({m},5) mod 125: groups={ng} bad_groups={bad}")
print()
print("=== 4. (2,1) digit sanity, p=13, m=182, mod 2197 ===")
p, m, t, n = 13, 182, 2, 2197
A = (1, 0)
v0 = seq_vals(A, m, n)
c0 = classes_of(v0, m, t)
for eta, tag in [((0, 1), "Tr(eta)=0"), ((1, 0), "Tr(eta)=2!=0")]:
    # A'' = A*(1 + p^2 eta) mod n
    Ap = ((A[0]*(1) + 2*A[1]*(p*p*eta[1])) % n,
          (A[0]*(p*p*eta[1]) + A[1]*1) % n)
    # A=(1,0): Ap = (1, p^2*eta1)
    Ap = (1 % n, (p*p*eta[1]) % n) if eta == (0, 1) else ((1 + p*p*eta[0]) % n, 0)
    v1 = seq_vals(Ap, m, n)
    c1 = classes_of(v1, m, t)
    print(f"eta={eta} ({tag}): global_equal={sorted(v0)==sorted(v1)} "
          f"perclass_exact_equal={c0==c1} perclass_D_related={c1 in d_orbit(t, c0)}")
