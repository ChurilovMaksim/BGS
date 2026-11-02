"""Wave 31, task 2, part 5: per-class delta structure."""
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
            rows.append(dict(gi=gi, f=f, tau=tau, w=w, wp=wp, tw=tw, delta=delta))

print("=== per-class support counts (nplus, nminus per class) x failing ===")
cnt = Counter()
for r in rows:
    per = []
    for cl in range(4):
        cls = [cl, cl+4, cl+8]
        np_ = sum(1 for j in cls if r['delta'][j] == 1)
        nm = sum(1 for j in cls if r['delta'][j] == -1)
        per.append((np_, nm))
    cnt[(tuple(per), r['f'])] += 0  # placeholder
    cnt[(tuple(sorted(per)), r['f'])] += 1
for k in sorted(cnt):
    print("  ", k, cnt[k])

print("\n=== class-sum differences dW_r = sum(delta|_r) x failing ===")
cnt2 = Counter()
for r in rows:
    dW = tuple(sum(r['delta'][j] for j in [cl, cl+4, cl+8]) for cl in range(4))
    cnt2[(dW, r['f'])] += 1
for k in sorted(cnt2):
    print("  ", k, cnt2[k])

print("\n=== failing cpi: is dW == 0 always? ===")
bad = [r for r in rows if r['f'] and any(sum(r['delta'][j] for j in [cl, cl+4, cl+8]) != 0 for cl in range(4))]
print("  failing cpi with some dW_r != 0:", len(bad), [r['gi'] for r in bad])

print("\n=== per-class delta triples (ordered by class position) x failing, |sup| ===")
cnt3 = Counter()
for r in rows:
    sup = sum(1 for x in r['delta'] if x != 0)
    for cl in range(4):
        trip = tuple(r['delta'][j] for j in [cl, cl+4, cl+8])
        cnt3[(sup, r['f'], trip)] += 1
for k in sorted(cnt3):
    print("  ", k, cnt3[k])
