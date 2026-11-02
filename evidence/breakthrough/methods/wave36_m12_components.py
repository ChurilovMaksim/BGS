import itertools
from collections import defaultdict

def kernel_points(m, q):
    pts = []
    for y0 in range(q):
        for y1 in range(q):
            y = [y0, y1]
            for i in range(2, m+2):
                y.append((6*y[-1] - y[-2]) % q)
            if y[m] == y0 and y[m+1] == y1:
                pts.append(tuple(y[:m]))
    return pts

def orbits(pts, m, q):
    # dihedral: shift by k, and reversal+shift. Represent point as tuple; shift: rotate.
    seen = set(); orbs = []
    ptset = set(pts)
    for p in pts:
        if p in seen: continue
        orb = set()
        for k in range(m):
            orb.add(tuple(p[(i+k) % m] for i in range(m)))
            # reversal: reverse order then rotate
            rev = tuple(p[(-i) % m] for i in range(m))
            orb.add(tuple(rev[(i+k) % m] for i in range(m)))
        orb &= ptset
        seen |= orb
        orbs.append(orb)
    return orbs

for m, qs in [(12, [128, 81, 25, 49, 121])]:
    for q in qs:
        pts = kernel_points(m, q)
        fibers = defaultdict(list)
        for p in pts:
            fibers[tuple(sorted(p))].append(p)
        # orbit partition of each fiber
        nsplit = 0; splitinfo = []
        for key, members in fibers.items():
            orbs = orbits(members, m, q)
            if len(orbs) > 1:
                nsplit += 1
                splitinfo.append((len(members), len(orbs)))
        print(f"m={m} q={q}: kernel={len(pts)} fibers={len(fibers)} split={nsplit} splitinfo={splitinfo}")
