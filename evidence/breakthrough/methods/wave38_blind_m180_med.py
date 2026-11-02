from collections import defaultdict, Counter
exec(open("wave38_blind_explore.py").read().split("m = 60")[0])
m = 180
sf729 = split_fibers(m, 729)
sf625 = split_fibers(m, 625)
a625 = sf625[0][1][0]
# D_36 | D_180, so 73^2, 179^2, 197^2, 199^2 are components of D_180
for q0 in [5329, 32041, 38809, 39601]:
    pts0 = kernel_points(m, q0)
    per = Counter(period(o) for o in pts0)
    print(f"q0={q0}: n={len(pts0)} period dist={dict(sorted(per.items()))}", flush=True)
    # sample: up to 40 nonzero o's per period class, test blind729
    byper = defaultdict(list)
    for o in pts0:
        if any(v != 0 for v in o): byper[period(o)].append(o)
    for d, os_ in sorted(byper.items()):
        sample = os_[:40]
        nb = 0
        for o in sample:
            fib = defaultdict(list)
            for i in range(m): fib[(a625[i], o[i])].append(i)
            fibers = list(fib.values())
            hit = False
            for key, reps in sf729:
                for x in range(len(reps)):
                    for y in range(x+1, len(reps)):
                        if all(sorted(reps[x][i] for i in idxs) == sorted(reps[y][i] for i in idxs) for idxs in fibers):
                            hit = True; break
                    if hit: break
                if hit: break
            if hit: nb += 1
        print(f"   period {d}: sampled {len(sample)}, blind729={nb}", flush=True)
