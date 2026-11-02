from collections import defaultdict, Counter
exec(open("wave38_blind_explore.py").read().split("m = 60")[0])
import sympy as sp
m = 180
# D_m = Tr(alpha^m) - 2, alpha = 3+2 sqrt2: T_n via recurrence
T = [2, 6]
for n in range(2, m+1): T.append(6*T[-1]-T[-2])
Dm = T[m-1] - 2
print(f"D_180 = {Dm}")
fac = sp.factorint(Dm)
print(f"factorization: {fac}")
comps = [p**e for p, e in fac.items()]
print(f"components: {comps}")
sf729 = split_fibers(m, 729)
sf625 = split_fibers(m, 625)
a625 = sf625[0][1][0]
# test blind729 at every component except split ones and 2-part
for q0 in comps:
    if q0 in (729, 625, 512): continue
    pts0 = kernel_points(m, q0)
    total = 0; b729 = 0
    for o in pts0:
        if all(v == 0 for v in o): continue
        total += 1
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
        if hit: b729 += 1
    per = Counter(period(o) for o in pts0)
    print(f"q0={q0}: nonzero={total} blind729={b729} period dist={dict(sorted(per.items()))}")
