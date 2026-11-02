#!/usr/bin/env python3
"""Wave 17, task 3: verify the mod-p^3 e-test and exact k for known primes.
R = Z[sqrt(2)], alpha = 3 + 2*sqrt(2). All arithmetic exact (Python ints).
- e-test(t): alpha^e == 1 mod p^t  <=>  k >= t, e = p - (2/p), L0 = ord_p(alpha).
- Direct k: largest t with alpha^L0 == 1 mod p^t (t up to 4 here).
- Cross-check e-test(3) <=> k>=3 for all odd primes < 10000.
- Exact k for 13, 31, 1546463 (wave-16 k>=2 primes below 2e9).
- Partial sum of 1/p^2 over primes <= 1e6 (heuristic total ~0.4522).
"""
import math

def mulR(x, y, mod):
    a1, b1 = x; a2, b2 = y
    return ((a1*a2 + 2*b1*b2) % mod, (a1*b2 + b1*a2) % mod)

def powR(base, exp, mod):
    r = (1 % mod, 0)
    b = (base[0] % mod, base[1] % mod)
    while exp:
        if exp & 1: r = mulR(r, b, mod)
        b = mulR(b, b, mod)
        exp >>= 1
    return r

def eps(p):
    return 1 if p % 8 in (1, 7) else -1

def factors(n):
    fs = []
    d = 2
    while d*d <= n:
        if n % d == 0:
            fs.append(d)
            while n % d == 0: n //= d
        d += 1 if d == 2 else 2
    if n > 1: fs.append(n)
    return fs

def order_mod_p(p):
    e = p - eps(p)
    alpha = (3 % p, 2 % p)
    assert powR(alpha, e, p) == (1 % p, 0), f"alpha^e != 1 mod p for p={p}"
    ordv = e
    for q in factors(e):
        while ordv % q == 0:
            t = powR(alpha, ordv // q, p)
            if t == (1 % p, 0): ordv //= q
            else: break
    return ordv, e

def kval(p, L0, tmax=4):
    """Largest t<=tmax with alpha^L0 == 1 mod p^t; returns tmax+1 if beyond."""
    for t in range(1, tmax+1):
        if powR((3, 2), L0, p**t) != (1, 0):
            return t - 1
    return tmax + 1

def primes_upto(n):
    sieve = bytearray(b'\x01') * (n + 1)
    sieve[0:2] = b'\x00\x00'
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            sieve[i*i:n+1:i] = b'\x00' * len(sieve[i*i:n+1:i])
    return [i for i, v in enumerate(sieve) if v]

# --- cross-check below 10000 ---
bad = 0; kge3 = []
for p in primes_upto(10000):
    if p == 2: continue
    L0, e = order_mod_p(p)
    k = kval(p, L0)
    etest3 = powR((3, 2), e, p**3) == (1, 0)
    if etest3 != (k >= 3):
        bad += 1; print("MISMATCH", p, L0, k, etest3)
    if k >= 3: kge3.append((p, L0, k))
print(f"cross-check p<10000: mismatches={bad}, k>=3 primes={kge3}")

# --- exact k for the three wave-16 primes ---
for p in (13, 31, 1546463):
    L0, e = order_mod_p(p)
    k = kval(p, L0)
    a2 = powR((3, 2), L0, p**2)
    a3 = powR((3, 2), L0, p**3)
    etest3 = powR((3, 2), e, p**3) == (1, 0)
    print(f"p={p} pmod8={p%8} e={e} L0={L0} q={e//L0} 4|L0={L0%4==0} "
          f"k={k} alpha^L0 mod p^2 == 1: {a2==(1,0)} mod p^3 == 1: {a3==(1,0)} "
          f"e-test mod p^3: {etest3}")

# --- heuristic partial sum sum 1/p^2 ---
s = 0.0
for p in primes_upto(10**6):
    s += 1.0 / (p * p)
print(f"sum_{{p<=1e6}} 1/p^2 = {s:.6f} (full prime-zeta P(2) = 0.452247...)")
