"""Wave 31, task 2, part 9: +6-shift symmetry of delta; tau commutation."""
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
            rows.append(dict(gi=gi, f=f, tau=tau, y=y, yp=yp, w=w, wp=wp, tw=tw, delta=delta))

print("=== tau commutes with +6? ===")
cnt = Counter()
for r in rows:
    tau = r['tau']
    comm6 = all(tau[(j+6) % 12] == (tau[j] + 6) % 12 for j in range(12))
    comm2 = all(tau[(j+2) % 12] == (tau[j] + 2) % 12 for j in range(12))
    cnt[(comm6, comm2)] += 1
print("  (commutes+6, commutes+2):", dict(cnt))

print("\n=== delta under +6 shift ===")
cnt2 = Counter()
for r in rows:
    dl = r['delta']
    eq = all(dl[(j+6) % 12] == dl[j] for j in range(12))
    neg = all(dl[(j+6) % 12] == -dl[j] for j in range(12))
    suppeq = all((dl[(j+6) % 12] != 0) == (dl[j] != 0) for j in range(12))
    cnt2[(eq, neg, suppeq)] += 1
print("  (delta[j+6]==delta[j], ==-delta[j], support-invariant):", dict(cnt2))

print("\n=== w under +6: w[j+6]-w[j] vs wp[j+6]-wp[j] ===")
cnt3 = Counter()
for r in rows:
    w, wp = r['w'], r['wp']
    dw = tuple(w[(j+6) % 12] - w[j] for j in range(6))
    dwp = tuple(wp[(j+6) % 12] - wp[j] for j in range(6))
    cnt3[(dw == dwp)] += 1
print("  (+6-differences of w and wp agree):", dict(cnt3))

print("\n=== defect indicator 2-periodicity ===")
cnt4 = Counter()
for r in rows:
    dl = r['delta']
    dind = tuple(1 if any(dl[j] != 0 for j in [cl, cl+4, cl+8]) else 0 for cl in range(4))
    cnt4[(dind, dind[0] == dind[2] and dind[1] == dind[3])] += 1
print("  (defect indicator, 2-periodic):", dict(cnt4))

print("\n=== y under +6 vs tau: check y'[j+6] == y[tau[j]+6] (from tau comm+6) ===")
# y'[j] = y[tau[j]]; tau commutes +6 => y'[j+6] = y[tau[j]+6].
# Also check the neighbor sums: is N(j+6) related to N(j)?
cnt5 = Counter()
for r in rows:
    y = r['y']
    # N(j) = y[j-1]+y[j+1]; compare N(j+6)-N(j) across j
    Ns = [y[(j-1) % 12] + y[(j+1) % 12] for j in range(12)]
    dN = tuple(Ns[(j+6) % 12] - Ns[j] for j in range(6))
    cnt5[(len(set(dN)) == 1)] += 1
print("  (N(j+6)-N(j) constant over j):", dict(cnt5))
