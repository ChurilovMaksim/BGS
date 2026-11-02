"""Inspect the small level-3 split fibers at (147,7): their orbit canons,
divisibility by 7, and the level-2 fiber they reduce to."""
import sys
sys.path.insert(0, ".")
import numpy as np
from collections import defaultdict
from wave36_tower import census_level, alpha_powers
import hashlib

m, p = 147, 7
lv3 = census_level(m, p, 3)
lv2 = census_level(m, p, 2)
mod3, d3 = lv3['mod'], lv3['d']
mod2, d2 = lv2['mod'], lv2['d']
# level-2 fiber info by hash
l2 = {h: (sz, nc, allsup) for (h, sz, nc, allsup, anysup, _) in lv2['fibers']}
# level-3 cycle of a C (for printing)
A3 = alpha_powers(m, mod3)


def cycle3(a, b):
    ca, cb = a, b
    out = []
    for j in range(d3):
        out.append((2 * ca) % mod3)
        ca, cb = (3 * ca + 4 * cb) % mod3, (2 * ca + 3 * cb) % mod3
    return tuple(sorted(out))


def hash_level2(a, b):
    ca, cb = a % mod2, b % mod2
    cyc = []
    for j in range(d2):
        cyc.append((2 * ca) % mod2)
        ca, cb = (3 * ca + 4 * cb) % mod2, (2 * ca + 3 * cb) % mod2
    return hashlib.blake2b(
        np.sort(np.array(cyc, dtype=np.int64)).tobytes(),
        digest_size=16).digest()


small = [x for x in lv3['fibers'] if x[2] >= 2 and x[1] == 294]
print(f"small level-3 split fibers: {len(small)}")
for (h, sz, nc, allsup, anysup, canons) in small[:2]:
    print(f"--- fiber size={sz} orbits={nc} allsup={allsup}")
    print("  orbit canons (a,b) mod 343:")
    for (a, b) in sorted(canons):
        print(f"    ({a},{b})  a%7={a % 7} b%7={b % 7}  gcd-ish: a%49={a % 49} b%49={b % 49}")
    ca, cb = next(iter(canons))
    h2 = hash_level2(ca, cb)
    print(f"  reduces to level-2 fiber: {l2.get(h2)}")
    # cycle sample of first canon
    cyc = cycle3(ca, cb)
    print(f"  cycle values mod 7 (first 21): {[v % 7 for v in cyc[:21]]}")
    print(f"  cycle min/max: {cyc[0]}..{cyc[-1]}, distinct: {len(set(cyc))}")
    # check: are all elements of this fiber divisible by 7? use hashes/ca/cb arrays
    # find all C in this fiber via hash match
    idxs = np.where(lv3['hashes'] == h)[0]
    div7 = sum(1 for i in idxs if lv3['ca'][i] % 7 == 0 and lv3['cb'][i] % 7 == 0)
    print(f"  fiber elements: {len(idxs)}, of which canon-divisible-by-7 (canon C%7==0): {div7}")
    # orbit sizes: group idxs by canon
    bycanon = defaultdict(int)
    for i in idxs:
        bycanon[(int(lv3['ca'][i]), int(lv3['cb'][i]))] += 1
    print(f"  orbit sizes: {sorted(bycanon.values())}")
