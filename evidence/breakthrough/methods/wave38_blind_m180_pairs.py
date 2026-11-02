from collections import defaultdict, Counter
exec(open("wave38_blind_explore.py").read().split("m = 60")[0])
m = 180
sf729 = split_fibers(m, 729)
sf625 = split_fibers(m, 625)
a625 = sf625[0][1][0]
for q0 in [49, 121, 361, 841]:
    pts0 = kernel_points(m, q0)
    paircount = Counter(); total = 0
    for o in pts0:
        if all(v == 0 for v in o): continue
        total += 1
        fib = defaultdict(list)
        for i in range(m): fib[(a625[i], o[i])].append(i)
        fibers = list(fib.values())
        for fi, (key, reps) in enumerate(sf729):
            for x in range(len(reps)):
                for y in range(x+1, len(reps)):
                    if all(sorted(reps[x][i] for i in idxs) == sorted(reps[y][i] for i in idxs) for idxs in fibers):
                        paircount[(fi, x, y)] += 1
    print(f"q0={q0}: nonzero={total} colliding-pair counts: {dict(sorted(paircount.items()))}")
