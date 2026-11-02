import math
from collections import defaultdict, Counter
exec(open("wave38_blind_explore.py").read().split("m = 60")[0])

m = 60
sf625 = split_fibers(m, 625)
sf81 = split_fibers(m, 81)
a_fixed = sf81[0][1][0]

def fiber_agree_pairs(a, o, reps):
    # returns list of colliding rep index pairs
    fib = defaultdict(list)
    for i in range(m): fib[(a[i], o[i])].append(i)
    coll = []
    for x in range(len(reps)):
        for y in range(x+1, len(reps)):
            ok = True
            for v, idxs in fib.items():
                if sorted(reps[x][i] for i in idxs) != sorted(reps[y][i] for i in idxs):
                    ok = False; break
            if ok: coll.append((x, y))
    return coll

# direct replication of wave-36 triple test for one q0, to cross-check
def triple_test(a_fixed, reps_list, o):
    for orbreps in reps_list:
        ms = [tuple(sorted((a_fixed[i], b[i], o[i]) for i in range(m))) for b in orbreps]
        if len(set(ms)) < len(ms): return True
    return False

for q0 in [49, 121, 361, 841]:
    pts0 = kernel_points(m, q0)
    blind_fiber = 0; blind_triple = 0; total = 0
    paircount = Counter()
    for o in pts0:
        if all(v == 0 for v in o): continue
        total += 1
        coll = []
        for fi, (key, reps) in enumerate(sf625):
            c = fiber_agree_pairs(a_fixed, o, reps)
            coll += [(fi, p) for p in c]
        if coll:
            blind_fiber += 1
            for fi, p in coll: paircount[(fi, p)] += 1
        if triple_test(a_fixed, [r for _, r in sf625], o):
            blind_triple += 1
    print(f"q0={q0}: nonzero={total} blind(fiber-agree)={blind_fiber} blind(triple)={blind_triple}")
    print(f"   colliding pairs: {dict(paircount)}")
