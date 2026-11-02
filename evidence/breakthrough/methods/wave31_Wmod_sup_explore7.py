"""Wave 31, task 2, part 7: joint distribution of per-class differences."""
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

print("=== 4-point: joint (d_r1, d_r2) over defect classes ===")
cnt = Counter()
for r in rows:
    if len(r['sup']) != 4: continue
    mp = per_class_mp(r)
    ds = tuple(sorted(r['tw'][m] - r['tw'][p] for m, p in mp.values()))
    cnt[(ds, r['f'])] += 1
for k in sorted(cnt):
    print("  ", k, cnt[k])

print("\n=== sum of d_r by |sup| x failing ===")
cnt2 = Counter()
for r in rows:
    mp = per_class_mp(r)
    s = sum(r['tw'][m] - r['tw'][p] for m, p in mp.values())
    cnt2[(len(r['sup']), r['f'], s)] += 1
for k in sorted(cnt2):
    print("  ", k, cnt2[k])

print("\n=== 8-point: sorted d-tuple by failing ===")
cnt3 = Counter()
for r in rows:
    if len(r['sup']) != 8: continue
    mp = per_class_mp(r)
    ds = tuple(sorted(r['tw'][m] - r['tw'][p] for m, p in mp.values()))
    cnt3[(ds, r['f'])] += 1
for k in sorted(cnt3):
    if k[1]: print("  FAILING", k, cnt3[k])
print("  non-failing with sum(d)=4:", sum(n for (ds, f), n in cnt3.items() if not f and sum(ds) == 4))
print("  non-failing total:", sum(n for (ds, f), n in cnt3.items() if not f))

print("\n=== 594: per-class (m,p,tw values) ===")
for r in rows:
    if r['gi'] == 594:
        mp = per_class_mp(r)
        for cl in sorted(mp):
            m, p = mp[cl]
            print(f"  class {cl}: m={m} p={p} tw[m]={r['tw'][m]} tw[p]={r['tw'][p]} d={r['tw'][m]-r['tw'][p]} tau[m]={r['tau'][m]} tau[p]={r['tau'][p]}")

print("\n=== 4-point failing: per-class (m,p) vs tau: is m/p the swapped pair or fixed? ===")
cnt4 = Counter()
for r in rows:
    if len(r['sup']) != 4: continue
    mp = per_class_mp(r)
    tau = r['tau']
    for cl, (m, p) in mp.items():
        # cases: tau swaps m<->p; tau fixes m; tau fixes p; neither fixed nor swapped pair
        if tau[m] == p: rel = 'swap-mp'
        elif tau[m] == m and tau[p] == p: rel = 'both-fixed?!'
        elif tau[m] == m: rel = 'm-fixed'
        elif tau[p] == p: rel = 'p-fixed'
        else: rel = 'other'
        cnt4[(r['f'], rel)] += 1
print("  (failing, relation):", dict(cnt4))
