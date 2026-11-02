import math
from collections import defaultdict, Counter
exec(open("wave38_blind_explore.py").read().split("m = 60")[0])

def seq_from_C(C, q, m):
    x, y = C
    t = [(2*x) % q, (2*(3*x+4*y)) % q]
    for i in range(2, m): t.append((6*t[-1]-t[-2]) % q)
    return tuple(t)

m = 60
sf625 = split_fibers(m, 625)
sf81 = split_fibers(m, 81)
a_fixed = sf81[0][1][0]
t = seq_from_C((0, 1), 25, m)

print("== t on mod-12 classes (expect full coset {c+5j} or constant) ==")
for r in range(12):
    vals = sorted(t[i] for i in range(m) if i % 12 == r)
    mods = sorted(set(v % 5 for v in vals))
    print(f"  r={r}: {vals} mod5={mods}")

print("== a-fibers: rho-invariance of t-multiset ==")
afib = defaultdict(list)
for i in range(m): afib[a_fixed[i]].append(i)
print(f"  #a-fibers={len(afib)} sizes={sorted(Counter(len(v) for v in afib.values()).items())}")
for rho in [6, 11, 16, 21, 4, 9, 14, 19]:
    bad = 0
    for v, idxs in afib.items():
        if sorted((rho*t[i]) % 25 for i in idxs) != sorted(t[i] for i in idxs):
            bad += 1
    print(f"  rho={rho} (mod5={rho%5}): failing a-fibers={bad}/{len(afib)}")

print("== periods of all sequences at q0 ==")
for q0 in [49, 121, 361, 841]:
    pts0 = kernel_points(m, q0)
    dist = Counter(period(o) for o in pts0)
    print(f"  q0={q0}: n={len(pts0)} period dist={dict(sorted(dist.items()))}")

print("== rho=-1 failure witness for o at 49 ==")
pts49 = kernel_points(m, 49)
o49 = next(o for o in pts49 if any(o))
fib = defaultdict(list)
for i in range(m): fib[(a_fixed[i], o49[i])].append(i)
for rho in [4]:
    for v, idxs in fib.items():
        tv = sorted(t[i] for i in idxs)
        rv = sorted((rho*t[i]) % 25 for i in idxs)
        if tv != rv:
            print(f"  fiber v={v} idxs={idxs} t={tv} rho*t={rv}")
            print(f"    mod5 counts t: {Counter(x % 5 for x in tv)}, rho*t: {Counter(x % 5 for x in rv)}")
            break
