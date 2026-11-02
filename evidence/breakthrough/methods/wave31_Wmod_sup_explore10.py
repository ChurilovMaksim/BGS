"""Wave 31, task 2, part 10: parity-pair d-sums; verify Sp = Sm+6; Dv sums."""
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

print("=== verify: Sp == Sm + 6 (as sets), and p_r = m_{r+2} + 6 ===")
bad = 0
for r in rows:
    Sm = set(j for j in r['sup'] if r['delta'][j] == -1)
    Sp = set(j for j in r['sup'] if r['delta'][j] == 1)
    if set((j + 6) % 12 for j in Sm) != Sp:
        bad += 1
    mp = per_class_mp(r)
    for cl, (m, p) in mp.items():
        if (mp[(cl + 2) % 4][0] + 6) % 12 != p:
            bad += 1
print("  violations:", bad, "of", len(rows))

print("\n=== parity-pair d-sums (d0+d2, d1+d3) by |sup| x failing ===")
cnt = Counter()
for r in rows:
    mp = per_class_mp(r)
    dsum = {}
    for cl, (m, p) in mp.items():
        dsum[cl] = r['tw'][m] - r['tw'][p]
    if len(mp) == 4:
        cnt[((dsum[0] + dsum[2], dsum[1] + dsum[3]), len(r['sup']), r['f'])] += 1
    elif len(mp) == 2:
        cnt[(('pair', tuple(sorted(mp))), len(r['sup']), r['f'])] += 1
for k in sorted(cnt, key=str):
    print("  ", k, cnt[k])

print("\n=== 8-point: parity-pair sums distribution (marginal) ===")
cnt2 = Counter()
for r in rows:
    if len(per_class_mp(r)) != 4: continue
    mp = per_class_mp(r)
    d = {cl: r['tw'][m] - r['tw'][p] for cl, (m, p) in mp.items()}
    cnt2[(d[0] + d[2], d[1] + d[3], r['f'])] += 1
for k in sorted(cnt2):
    print("  ", k, cnt2[k])
