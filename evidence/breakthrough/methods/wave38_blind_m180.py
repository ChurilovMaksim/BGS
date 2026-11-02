import math
from collections import defaultdict, Counter
exec(open("wave38_blind_explore.py").read().split("m = 60")[0])

m = 180
sf729 = split_fibers(m, 729)
sf625 = split_fibers(m, 625)
print(f"m=180: 729 split fibers: {len(sf729)}, orbit counts: {[len(r) for _, r in sf729]}")
print(f"m=180: 625 split fibers: {len(sf625)}, orbit counts: {[len(r) for _, r in sf625]}")
if sf729:
    for fi, (key, reps) in enumerate(sf729):
        print(f"--- 729 fiber {fi}: periods {[period(r) for r in reps]}")
        Cs = [recover_C(r, 729) for r in reps]
        print(f"    C's: {Cs} checks: {[check_C(r, C, 729) for r, C in zip(reps, Cs)]}")
if sf625:
    for fi, (key, reps) in enumerate(sf625):
        print(f"--- 625 fiber {fi}: periods {[period(r) for r in reps]}")
        Cs = [recover_C(r, 625) for r in reps]
        print(f"    C's: {Cs} checks: {[check_C(r, C, 625) for r, C in zip(reps, Cs)]}")
# triple tests both directions (only if both split)
if sf729 and sf625:
    a729 = sf729[0][1][0]
    a625 = sf625[0][1][0]
    print(f"locked729 period: {period(a729)}, locked625 period: {period(a625)}")
    for q0 in [49, 121, 361, 841]:
        pts0 = kernel_points(m, q0)
        b625 = 0; b729 = 0; total = 0
        for o in pts0:
            if all(v == 0 for v in o): continue
            total += 1
            for key, reps in sf625:
                ms = [tuple(sorted((a729[i], b[i], o[i]) for i in range(m))) for b in reps]
                if len(set(ms)) < len(ms): b625 += 1; break
            for key, reps in sf729:
                ms = [tuple(sorted((a625[i], b[i], o[i]) for i in range(m))) for b in reps]
                if len(set(ms)) < len(ms): b729 += 1; break
        per = Counter(period(o) for o in pts0)
        print(f"q0={q0}: nonzero={total} blind625(locked729)={b625} blind729(locked625)={b729} period dist={dict(sorted(per.items()))}")
