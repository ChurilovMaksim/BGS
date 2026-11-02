import math
from collections import defaultdict, Counter
exec(open("wave38_blind_explore.py").read().split("m = 60")[0])

def seq_from_C(C, q, m):
    x, y = C
    t = [(2*x) % q, (2*(3*x+4*y)) % q]
    for i in range(2, m): t.append((6*t[-1]-t[-2]) % q)
    return tuple(t)

m = 120
sf625 = split_fibers(m, 625)
sf81 = split_fibers(m, 81)
print(f"m=120: 625 split fibers: {len(sf625)}, orbit counts: {[len(r) for _, r in sf625]}")
print(f"m=120: 81 split fibers: {len(sf81)}, orbit counts: {[len(r) for _, r in sf81]}")
if sf81 and sf625:
    a_fixed = sf81[0][1][0]
    print(f"a_fixed period: {period(a_fixed)}")
    for fi, (key, reps) in enumerate(sf625):
        print(f"--- 625 fiber {fi}: periods {[period(r) for r in reps]}")
        Cs = [recover_C(r, 625) for r in reps]
        print(f"    C's: {Cs} checks: {[check_C(r, C, 625) for r, C in zip(reps, Cs)]}")
    # triple test for q0 in {49,121,361,841}, locked=81, free=625
    for q0 in [49, 121, 361, 841]:
        pts0 = kernel_points(m, q0)
        blind = 0; total = 0
        for o in pts0:
            if all(v == 0 for v in o): continue
            total += 1
            hit = False
            for key, reps in sf625:
                ms = [tuple(sorted((a_fixed[i], b[i], o[i]) for i in range(m))) for b in reps]
                if len(set(ms)) < len(ms): hit = True; break
            if hit: blind += 1
        per = Counter(period(o) for o in pts0)
        print(f"q0={q0}: nonzero={total} blind625={blind} period dist={dict(sorted(per.items()))}")
