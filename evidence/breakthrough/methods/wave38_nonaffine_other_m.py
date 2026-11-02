"""Wave 38, task 5, part 3: slice tests at other m + b-sequence screen."""
import numpy as np, math
from collections import defaultdict

def kernel_rows(m, q):
    a, b = np.meshgrid(np.arange(q), np.arange(q), indexing="ij")
    a = a.ravel().astype(np.int64); b = b.ravel().astype(np.int64)
    prev, cur = a, b
    seqs = [a, b]
    for _ in range(m - 1):
        nxt = (6 * cur - prev) % q
        seqs.append(nxt); prev, cur = cur, nxt
    nxt = (6 * cur - prev) % q
    ok = (seqs[m] == a) & (nxt == b)
    return np.stack([s[ok] for s in seqs[:m]], axis=1)

def crt_pair(A, qa, B, qb):
    inv = pow(int(qa), -1, int(qb))
    A3 = A[:, None, :]; B3 = B[None, :, :]
    t = (((B3 - A3) % qb) * inv) % qb
    return (A3 + qa * t).reshape(-1, A.shape[1])

def affine_perms(m):
    perms = []
    for u in range(m):
        if math.gcd(u, m) != 1: continue
        for c in range(m):
            perms.append([(u * j + c) % m for j in range(m)])
    return np.array(perms, dtype=np.int64)

def analyze_slice(m, q1, q2):
    K1 = kernel_rows(m, q1); K2 = kernel_rows(m, q2)
    pts = crt_pair(K1, q1, K2, q2)
    srt = np.sort(pts, axis=1)
    _, inv, counts = np.unique(srt, axis=0, return_inverse=True, return_counts=True)
    perms = affine_perms(m)
    multi = []
    for fid in range(len(counts)):
        rows = pts[inv == fid]
        members = set(map(bytes, rows))
        remaining = set(members)
        orbits = []
        while remaining:
            base = np.frombuffer(next(iter(remaining)), dtype=np.int64)
            orb = set(map(bytes, base[perms])) & remaining
            orbits.append(len(orb)); remaining -= orb
        if len(orbits) > 1:
            multi.append((int(counts[fid]), orbits))
    print(f"m={m} slice ker({q1})xker({q2}): |K|={len(K1)},{len(K2)} pts={len(pts)} "
          f"fibers={len(counts)} maxsize={counts.max()} multi-orbit fibers={len(multi)}")
    for size, orbs in sorted(multi, reverse=True)[:10]:
        print(f"    size {size} orbits {orbs}")
    return multi

# b-sequence screen
def b_set(p):
    seen = set(); a, b = 0, 1
    while True:
        seen.add(a)
        a, b = b, (6 * b - a) % p
        if a == 0 and b == 1: break
    return seen

print("=== b-sequence screen (primes <= 200) ===")
def primes_upto(n):
    sieve = [True] * (n + 1); out = []
    for i in range(2, n + 1):
        if sieve[i]:
            out.append(i)
            for j in range(i * i, n + 1, i): sieve[j] = False
    return out
for p in primes_upto(200):
    S = b_set(p)
    if len(S) == p: continue
    nz = {x for x in S if x != 0}
    stab = [u for u in range(1, p) if {(u * x) % p for x in nz} == nz]
    print(f"p={p}: |S|={len(S)} stabilizer size={len(stab)} stabilizer={stab[:12]}")

print("=== slice tests ===")
analyze_slice(6, 25, 49)
analyze_slice(12, 81, 25)
analyze_slice(12, 128, 81)
analyze_slice(24, 81, 25)
analyze_slice(24, 512, 81)
analyze_slice(36, 729, 25)
analyze_slice(36, 128, 729)
analyze_slice(48, 25, 49)
analyze_slice(48, 289, 25)
analyze_slice(60, 625, 81)
analyze_slice(60, 625, 121)
analyze_slice(42, 2401, 25)
analyze_slice(42, 2401, 169)
