"""Wave 31, task 2, part 8: aligned (1,1,1,1) at 8 points? fixed-point correlation?"""
import json
from collections import Counter, defaultdict

D = 1536796800

def Hvec(y):
    return [6*y[i] - y[i-1] - y[(i+1) % 12] for i in range(12)]

def wvec(y):
    h = Hvec(y)
    assert all(x % D == 0 for x in h)
    return [x // D for x in h]

def all_taus(y, yp):
    byval = defaultdict(list)
    for i, v in enumerate(y):
        byval[v].append(i)
    order = sorted(range(12), key=lambda j: len(byval[yp[j]]))
    tau = [None]*12; used = set(); res = []
    def bt(t):
        if len(res) > 2000: return
        if t == 12:
            res.append(tuple(tau)); return
        j = order[t]
        for i in byval[yp[j]]:
            if i not in used:
                used.add(i); tau[j] = i; bt(t+1); used.discard(i); tau[j] = None
    bt(0)
    return res

def is_cpi(tau):
    if any(tau[tau[j]] != j for j in range(12)): return False
    for r in range(4):
        cls = [r, r+4, r+8]
        if sorted(tau[j] for j in cls) != cls: return False
        if sum(1 for j in cls if tau[j] == j) != 1: return False
    return True

d = json.load(open('wave18_Pw_m12_census.json'))
rows = []
for gi, g in enumerate(d['split_groups']):
    orbs = g['orbits']
    for a in range(len(orbs)):
        for b in range(a+1, len(orbs)):
            f = (orbs[a]['sorted_w'] == orbs[b]['sorted_w'])
            y, yp = orbs[a]['rep'], orbs[b]['rep']
            taus = all_taus(y, yp)
            cpis = [t for t in taus if is_cpi(t)]
            if not cpis: continue
            tau = cpis[0]
            w = wvec(y); wp = wvec(yp)
            tw = [w[tau[j]] for j in range(12)]
            delta = [wp[j] - tw[j] for j in range(12)]
            sup = [j for j in range(12) if delta[j] != 0]
            rows.append(dict(gi=gi, f=f, tau=tau, w=w, wp=wp, tw=tw, delta=delta, sup=sup))

def per_class_mp(r):
    out = {}
    for cl in range(4):
        cls = [cl, cl+4, cl+8]
        ms = [j for j in cls if r['delta'][j] == -1]
        ps = [j for j in cls if r['delta'][j] == 1]
        if ms:
            out[cl] = (ms[0], ps[0])
    return out

print("=== 8-point: full sorted d-tuple distribution ===")
cnt = Counter()
for r in rows:
    if len(r['sup']) != 8: continue
    mp = per_class_mp(r)
    ds = tuple(sorted(r['tw'][m] - r['tw'][p] for m, p in mp.values()))
    cnt[(ds, r['f'])] += 1
for k in sorted(cnt):
    print("  ", k, cnt[k])
print("  (1,1,1,1) occurrences:", sum(n for (ds, f), n in cnt.items() if ds == (1, 1, 1, 1)))

print("\n=== defect class vs tau fixed-point offset ===")
# fixed point of class cl: offset 0 (cl), 4 (cl+4), 8 (cl+8)
cnt2 = Counter()
for r in rows:
    tau = r['tau']
    mp = per_class_mp(r)
    for cl in range(4):
        cls = [cl, cl+4, cl+8]
        fx = [j for j in cls if tau[j] == j][0]
        off = (fx - cl) % 12
        cnt2[(cl in mp, off)] += 1
print("  (is-defect-class, fixed-offset):", dict(cnt2))

print("\n=== 4-point: defect pair {1,3} vs {0,2} by fixed offsets ===")
cnt3 = Counter()
for r in rows:
    if len(r['sup']) != 4: continue
    tau = r['tau']
    mp = per_class_mp(r)
    offs = tuple(( [j for j in [cl, cl+4, cl+8] if tau[j] == j][0] - cl) % 12 for cl in range(4))
    cnt3[(tuple(sorted(mp)), offs, r['f'])] += 1
for k in sorted(cnt3):
    print("  ", k, cnt3[k])

print("\n=== 8-point non-failing with sum(d)=4: their d-tuples ===")
cnt4 = Counter()
for r in rows:
    if len(r['sup']) != 8 or r['f']: continue
    mp = per_class_mp(r)
    ds = tuple(sorted(r['tw'][m] - r['tw'][p] for m, p in mp.values()))
    if sum(ds) == 4:
        cnt4[ds] += 1
print("  ", dict(cnt4))
