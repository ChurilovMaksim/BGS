"""Wave 30, task 2: final scope tables."""
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

def Svals(y, w):
    return [sum(y[i]*w[(i+d) % 12] for i in range(12)) for d in range(12)]

d = json.load(open('wave18_Pw_m12_census.json'))
allpairs = []
for gi, g in enumerate(d['split_groups']):
    orbs = g['orbits']
    for a in range(len(orbs)):
        for b in range(a+1, len(orbs)):
            f = (orbs[a]['sorted_w'] == orbs[b]['sorted_w'])
            allpairs.append((gi, orbs[a]['rep'], orbs[b]['rep'], f))

full = Counter()
fail_defect = Counter()
for gi, y, yp, f in allpairs:
    taus = all_taus(y, yp)
    cpis = [t for t in taus if is_cpi(t)]
    if not cpis: continue
    tau = cpis[0]
    w = wvec(y); wp = wvec(yp)
    tw = [w[tau[j]] for j in range(12)]
    delta = [wp[j] - tw[j] for j in range(12)]
    sconst = (Svals(y, w) == Svals(yp, wp))
    sup = [j for j in range(12) if delta[j] != 0]
    tsup = sorted(set(tau[j] for j in sup))
    anti = False
    if not sup:
        anti = True
    else:
        for p in range(12):
            s = sorted({(p-1) % 12, (p+1) % 12, (p+5) % 12, (p+7) % 12})
            if tsup == s and y[(p-1) % 12] + y[(p+1) % 12] == y[(p+5) % 12] + y[(p+7) % 12]:
                anti = True
    full[(len(sup), anti, sconst, f)] += 1
    if f:
        defect = tuple(sorted(set(j % 4 for j in range(12) if delta[j] != 0)))
        fail_defect[defect] += 1
print("|sup| x antipodal x S-const x failing (cpi pairs):")
for k, n in sorted(full.items()):
    print("   ", k, n)
print("failing cpi defect sets:", dict(fail_defect))
