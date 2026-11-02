"""Wave 11, task 2, search D: per-class multisets mod p (prime, not prime power).

For odd p | D_m, M^m == I (mod p) in many cases (since d1,d2 divisible by p),
so Fix_m mod p = ALL recurrence sequences mod p (p^2 sequences). Group by
sorted multiset mod p; check D_t-canonical per-class tuple constant.
A failure mod p does not by itself lift to a global counterexample, but it
would pinpoint where a mod-p proof fails; 0 failures support the finite-field
(alpha) proof route.
"""
import math, time
import numpy as np
import sympy as sp

def d_t_perms(t):
    out = []
    for b in range(t):
        out.append(tuple((i+b) % t for i in range(t)))
        out.append(tuple((-i+b) % t for i in range(t)))
    return list(dict.fromkeys(out))

def check_modp(m, p):
    t0 = time.time()
    # generate all (y0,y1) grid, sequences length m via recurrence mod p
    y0 = np.repeat(np.arange(p, dtype=np.int64), p)
    y1 = np.tile(np.arange(p, dtype=np.int64), p)
    seqs = np.empty((p*p, m), dtype=np.int64)
    seqs[:, 0] = y0
    if m > 1:
        seqs[:, 1] = y1
    for i in range(2, m):
        seqs[:, i] = (6*seqs[:, i-1] - seqs[:, i-2]) % p
    # period check: sequences with y_m==y0 and y_{m+1}==y1
    nxt = (6*seqs[:, m-1] - seqs[:, m-2]) % p
    nxt2 = (6*nxt - seqs[:, m-1]) % p
    ok = (nxt == y0) & (nxt2 == y1)
    seqs = seqs[ok]
    t = math.gcd(m, 4)
    perms = d_t_perms(t)
    cls_idx = [[i for i in range(m) if i % t == r] for r in range(t)]
    srt = np.sort(seqs, axis=1).astype(np.int64)
    pc = np.empty((len(seqs), t, m//t), dtype=np.int64)
    for r, idx in enumerate(cls_idx):
        pc[:, r, :] = np.sort(seqs[:, idx], axis=1)
    best = None
    for pi in perms:
        cand = pc[:, list(pi), :].reshape(len(seqs), m)
        if best is None:
            best = cand.copy(); continue
        lt = np.zeros(len(seqs), dtype=bool); eq = np.ones(len(seqs), dtype=bool)
        for c in range(m):
            lt |= eq & (cand[:, c] < best[:, c])
            eq &= (cand[:, c] == best[:, c])
        best[lt] = cand[lt]
    groups = {}
    bad = []
    for j in range(len(seqs)):
        key = srt[j].tobytes(); can = best[j].tobytes()
        ent = groups.get(key)
        if ent is None:
            groups[key] = (can, j, {can})
        elif can not in ent[2]:
            if len(ent[2]) == 1:
                bad.append((ent[1], j))
            ent[2].add(can)
    print(f"m={m} p={p} t={t} fix_mod_p={len(seqs)} (p^2={p*p}) groups={len(groups)} BAD={len(bad)} time={time.time()-t0:.1f}s", flush=True)
    for a, b in bad[:3]:
        print(f"  BAD seq_a={tuple(seqs[a])} seq_b={tuple(seqs[b])}", flush=True)
    return len(bad)

def main():
    total = 0
    for m in range(4, 21):
        x, y = 1, 0
        for _ in range(m):
            x, y = 3*x+8*y, x+3*y
        D = 2*(x-1)
        for p in sorted(sp.factorint(D)):
            if p == 2 or p > 700:
                continue
            total += check_modp(m, p)
    print(f"TOTAL_BAD={total}", flush=True)

if __name__ == "__main__":
    main()
