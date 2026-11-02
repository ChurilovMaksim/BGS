#!/usr/bin/env python3
"""Wave 46, task 7, step 5: are single-component pairs dihedral images?

For each prime power q | D_24 (other components + 289), enumerate ker_q,
group by multiset, and for each pair check whether y' = y o d for some
dihedral position map d in D_24. A non-dihedral pair is the raw material
for a non-dihedral global sigma.
"""
D24 = []
for k in range(24):
    D24.append(tuple((i + k) % 24 for i in range(24)))
    D24.append(tuple((-i + k) % 24 for i in range(24)))

def kernel_small(q):
    out = []
    for y0 in range(q):
        for y1 in range(q):
            y = [0] * 26
            y[0], y[1] = y0, y1
            for n in range(24):
                y[n + 2] = (6 * y[n + 1] - y[n]) % q
            if y[24] == y0 and y[25] == y1:
                out.append(tuple(y[:24]))
    return out

for q in [25, 49, 81, 121, 289, 512]:
    K = kernel_small(q)
    by_mult = {}
    for y in K:
        by_mult.setdefault(tuple(sorted(y)), []).append(y)
    tot = dih = nondih = 0
    examples = []
    for ys in by_mult.values():
        for ii in range(len(ys)):
            for jj in range(ii + 1, len(ys)):
                y, yp = ys[ii], ys[jj]
                tot += 1
                ok = any(tuple(y[d[i]] for i in range(24)) == yp
                         for d in D24)
                if ok:
                    dih += 1
                else:
                    nondih += 1
                    if len(examples) < 3:
                        examples.append((y, yp))
    print(f"q={q}: pairs={tot} dihedral={dih} NONDIHEDRAL={nondih}")
    for (y, yp) in examples:
        print(f"   ex y={y}")
        print(f"      y'={yp}")
