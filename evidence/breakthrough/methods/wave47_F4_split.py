# Mod-p split enumeration (wave-46 definition) for (41,5), (239,7), (71,35).
from collections import defaultdict

def analyze(p, order):
    fibers = defaultdict(list)
    for y0 in range(p):
        for y1 in range(p):
            if y0 == 0 and y1 == 0:
                continue
            t = [y0, y1]
            for i in range(2, order):
                t.append((6*t[-1] - t[-2]) % p)
            t = tuple(t)
            assert (6*t[-1] - t[-2]) % p == t[0] and (6*t[0] - t[-1]) % p == t[1]
            fibers[tuple(sorted(t))].append(t)
    def canon(t):
        rots = [tuple(t[(i+k) % order] for i in range(order)) for k in range(order)]
        rev = (t[0],) + tuple(t[order-1-i] for i in range(order-1))
        rrots = [tuple(rev[(i+k) % order] for i in range(order)) for k in range(order)]
        return min(rots + rrots)
    split = 0
    for key, members in fibers.items():
        orbits = {canon(t) for t in members}
        if len(orbits) > 1:
            split += 1
    sizes = sorted((len(v) for v in fibers.values()), reverse=True)[:5]
    print(f"p={p} order={order}: seeds={p*p-1}, fibers={len(fibers)}, split={split}, largest={sizes}", flush=True)

analyze(41, 5)
analyze(239, 7)
analyze(71, 35)
