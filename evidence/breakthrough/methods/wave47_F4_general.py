# Wave 47, task 9: generalized (non-injective-a) class analysis at 180/252 + lcm<M demo.
import sys
from collections import defaultdict
sys.path.insert(0, ".")
exec(open("wave38_blind_explore.py").read().split("m = 60")[0])

def classes_and_checks(a_per, b_per, d_a, M, label):
    # a_per: period-d_a list; b_per: period-36 list (b_r = b_{1-r} pairing)
    g = __import__("math").gcd(d_a, 36)
    L = d_a * 36 // g
    a = [a_per[i % d_a] for i in range(M)]
    b = [b_per[i % 36] for i in range(M)]
    # A_i sets
    A = []
    for i in range(d_a):
        A.append({s for s in range(d_a) if a_per[(i + s) % d_a] == a_per[i]})
    # class structure by brute force
    cls = defaultdict(list)
    for i in range(M):
        cls[(a[i], b[i])].append(i)
    sizes = sorted((len(v) for v in cls.values()), reverse=True)
    n_single = sum(1 for v in cls.values() if len(v) == 1)
    n_double = sum(1 for v in cls.values() if len(v) == 2)
    # generalized pair criterion: class(i) non-singleton <=> exists s in A_i with s = 1-2r mod g
    pred_nonsingle = set()
    for i in range(M):
        r = i % 36
        if any(s % g == (1 - 2*r) % g for s in A[i % d_a]):
            pred_nonsingle.add(i)
    actual_nonsingle = {i for v in cls.values() if len(v) > 1 for i in v}
    crit_ok = (pred_nonsingle == actual_nonsingle)
    # (H-dist): no i = 0 mod 18 with a_{i+1} == a_i
    hdist_fail = [i for i in range(M) if i % 18 == 0 and a[(i+1) % M] == a[i]]
    # (H-sep) generalized: for j non-singleton, j-1 and j-2 singleton (brute force)
    hsep_fail = []
    for j in actual_nonsingle:
        for k in (j-1, j-2):
            kk = k % M
            if kk in actual_nonsingle:
                hsep_fail.append((j, kk))
    # min distance across different non-singleton classes
    pos = sorted(actual_nonsingle)
    print(f"[{label}] d_a={d_a} g={g} L={L} M={M} classes={len(cls)} singletons={n_single} doubles={n_double} maxsize={sizes[0]}")
    print(f"  pair-criterion exact: {crit_ok} (pred {len(pred_nonsingle)} vs actual {len(actual_nonsingle)} nonsingleton positions)")
    print(f"  (H-dist) adjacent-collision failures at i=0 mod 18: {len(hdist_fail)} {hdist_fail[:5]}")
    print(f"  (H-sep) failures (j nonsingleton, j-1/j-2 nonsingleton): {len(hsep_fail)} {hsep_fail[:5]}")
    # distance-1 and distance-2 partners within same class (brute force)
    d1 = d2 = 0
    for v in cls.values():
        s = set(v)
        for i in v:
            if (i+1) % M in s and (i+1) % M != i: d1 += 1
            if (i+2) % M in s and (i+2) % M != i: d2 += 1
    print(f"  same-class distance-1 adjacencies: {d1}, distance-2: {d2}")
    return cls

# --- m = 180 ---
sf625 = split_fibers(180, 625)
a180 = sf625[0][1][0]
print(f"a180 C={recover_C(a180, 625)} period={period(a180)}")
sf729 = split_fibers(180, 729)
Cs729 = [recover_C(r, 729) for r in sf729[0][1]]
by_k = {C[1] // 27: r for C, r in zip(Cs729, sf729[0][1])}
b180 = by_k[20]
print(f"b180 C={recover_C(b180, 729)} period={period(b180)} distinct-over-period={len(set(b180[:36]))}")
a180_per = list(a180[:30])
print(f"a180 distinct over 30-period: {len(set(a180_per))} (expect 15)")
b_per = list(b180[:36])
print(f"b pairing check b_r == b_(1-r): {all(b_per[r] == b_per[(1-r) % 36] for r in range(36))}")
classes_and_checks(a180_per, b_per, 30, 180, "m=180")

# --- m = 252 ---
sf2401 = split_fibers(252, 2401)
a252 = sf2401[0][1][0]
print(f"a252 C={recover_C(a252, 2401)} period={period(a252)}")
a252_per = list(a252[:21])
print(f"a252 distinct over 21-period: {len(set(a252_per))} (expect 21, injective)")
classes_and_checks(a252_per, b_per, 21, 252, "m=252")
# double positions mod 3 at 252
cls252 = defaultdict(list)
a = [a252_per[i % 21] for i in range(252)]
b = [b_per[i % 36] for i in range(252)]
for i in range(252):
    cls252[(a[i], b[i])].append(i)
dbl_pos = sorted(i for v in cls252.values() if len(v) == 2 for i in v)
print(f"m=252 double positions all =2 mod 3: {all(i % 3 == 2 for i in dbl_pos)} (n={len(dbl_pos)})")
# min circular distance across different double pairs
dbl_pairs = [tuple(v) for v in cls252.values() if len(v) == 2]
def cdist(i, j):
    d = abs(i - j) % 252
    return min(d, 252 - d)
mind = 252
for x in range(len(dbl_pairs)):
    for y in range(x+1, len(dbl_pairs)):
        for i in dbl_pairs[x]:
            for j in dbl_pairs[y]:
                mind = min(mind, cdist(i, j))
print(f"m=252 min distance across different double pairs: {mind} (expect 3)")

# --- lcm<M demo: M=72, d_a=12, L=36 ---
print("--- lcm<M demo ---")
M2 = 72
a_demo = [i % 12 for i in range(M2)]  # 12-periodic
b_demo = [b_per[i % 36] for i in range(M2)]
# 5-periodic kernel seq mod 41, seed (1,0)
o = [1, 0]
for i in range(2, M2):
    o.append((6*o[-1] - o[-2]) % 41)
print(f"o period 5 check: {[o[i] == o[i % 5] for i in range(M2)][:10]}... all periodic: {all(o[i] == o[i % 5] for i in range(M2))}")
o_shift = [o[(i + 36) % M2] for i in range(M2)]
print(f"o∘σ36 == o: {o_shift == o} (expect False: 36 mod 5 = 1)")
cfg = sorted(zip(a_demo, b_demo, o))
cfg_shift = sorted(zip(a_demo, b_demo, o_shift))
print(f"M(o∘σ36) == M(o): {cfg_shift == cfg} (expect True)")
# success direction: 36-periodic o'
op = [b_per[i % 36] for i in range(M2)]
op_shift = [op[(i + 36) % M2] for i in range(M2)]
print(f"36-periodic o': o'∘σ36 == o': {op_shift == op} (expect True)")
