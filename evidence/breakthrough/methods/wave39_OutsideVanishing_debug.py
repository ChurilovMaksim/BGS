"""Debug: why do 176 level-3 split fibers map to >1 M4 group?
1. Check M3(canonical lift) hash == census hash of (a,b) mod 2197.
2. For one such fiber: S = {D mod 169 : D in F3'}; compare M4 hashes
   of canonical lifts of c in S; list groups mapping to the fiber.
"""
import sys, hashlib
sys.path.insert(0, ".")
import numpy as np
from collections import defaultdict
from wave36_tower import census_level
from wave39_OutsideVanishing_checkC import cycle_hashes, MOD2, MOD3, MOD4, D3, D4, P

lv3 = census_level(182, P, 3)
fib3 = defaultdict(list)
for idx, h in enumerate(lv3['hashes']):
    fib3[h].append(idx)
canon3 = {h: {(int(lv3['ca'][i]), int(lv3['cb'][i])) for i in idxs}
          for h, idxs in fib3.items()}
split3 = {h: c for h, c in canon3.items() if len(c) >= 2}

classes = np.array([(a, b) for a in range(MOD2) for b in range(MOD2)],
                   dtype=np.int64)
h4 = cycle_hashes(MOD4, D4, classes)
h3 = cycle_hashes(MOD3, D3, classes)
g4 = defaultdict(set)
for i, (a, b) in enumerate(classes):
    g4[h4[i]].add((int(a), int(b)))

# 1. M3 hash vs census hash
mism = 0
for i in range(0, len(classes), 37):
    a, b = int(classes[i][0]), int(classes[i][1])
    if h3[i] != lv3['hashes'][a * MOD3 + b]:
        mism += 1
print(f"M3-vs-census mismatches (sampled): {mism}")

# 2. find a split fiber hit by >1 group
def idx3(a, b):
    return a * MOD3 + b
fib_to_grp = defaultdict(list)
for h, grp in g4.items():
    a, b = next(iter(grp))
    fib_to_grp[lv3['hashes'][idx3(a, b)]].append(h)
multi = {fh: v for fh, v in fib_to_grp.items()
         if len(v) > 1 and fh in split3}
print(f"split fibers hit by >1 group: {len(multi)}")
fh = next(iter(multi))
print(f"example fiber: groups mapping to it: {len(multi[fh])}")
S = {(i // MOD3 % MOD2, i % MOD3 % MOD2) for i in fib3[fh]}
print(f"|S| = {len(S)}")
groups_here = multi[fh]
for gh in groups_here:
    grp = g4[gh]
    print(f"  group size={len(grp)} subset-of-S: {grp <= S} "
          f"overlap-with-S: {len(grp & S)}")
# M4 hashes of canonical lifts of c in S: all equal?
h4_of_S = {h4[int(a) * MOD2 + int(b)] for (a, b) in S}
print(f"distinct M4 hashes over S: {len(h4_of_S)}")
# Z-status of the fiber: B_j0 = Tr(C alpha^j0 u) mod 13, u=(0,6)
# take one D in F3', compute B over j0 in Z/14
idxs = fib3[fh]
x = idxs[0]
xa, xb = x // MOD3, x % MOD3
# alpha powers mod 13
A = [(1, 0)]
for _ in range(14):
    a_, b_ = A[-1]
    A.append(((3 * a_ + 4 * b_) % P, (2 * a_ + 3 * b_) % P))
# u = (0,6): C*alpha^j0*u: (a+b s)(6 s) = 12b + 6a s -> Tr = 24b mod 13
B = []
ca, cb = xa % P, xb % P
for j0 in range(14):
    B.append((24 * cb) % P)
    ca, cb = (3 * ca + 4 * cb) % P, (2 * ca + 3 * cb) % P
print(f"fiber element ({xa},{xb}) mod13=({xa%P},{xb%P}) B={B} Z={[j for j,v in enumerate(B) if v==0]}")
print(f"fiber size={len(idxs)} orbits={len(canon3[fh])}")
