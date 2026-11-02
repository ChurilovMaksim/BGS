from collections import Counter
exec(open("wave38_blind_explore.py").read().split("m = 60")[0])
m = 180
for q0 in [49, 121, 361, 841, 1681, 3481, 72361]:
    sf = split_fibers(m, q0)
    print(f"q0={q0}: split fibers: {len(sf)}, orbit counts: {[len(r) for _, r in sf]}", flush=True)
