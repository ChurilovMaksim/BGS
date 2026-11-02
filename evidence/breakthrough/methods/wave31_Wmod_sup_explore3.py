"""Wave 31, task 2, part 3: tau-relations of rectangles vs transfer."""
import json
from collections import Counter, defaultdict
from itertools import combinations

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

def all_rect_decomps(delta):
    Sm = [j for j in range(12) if delta[j] == -1]
    Sp = [j for j in range(12) if delta[j] == 1]
    if len(Sm) != len(Sp): return []
    def search(Sm, Sp):
        if not Sm: return [()]
        a = Sm[0]; out = []
        for b in Sm[1:]:
            for c, dd in combinations(Sp, 2):
                if (a + b) % 12 == (c + dd) % 12:
                    for rest in search([x for x in Sm[1:] if x != b],
                                       [x for x in Sp if x != c and x != dd]):
                        out.append(((a, b, c, dd),) + rest)
        return out
    return search(Sm, Sp)

def transfer_of(tw, Sm, Sp):
    return sorted(tw[j] for j in Sm) == sorted(tw[j] + 1 for j in Sp)

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

print("=== 4-point: tau-relation of the single rectangle vs transfer ===")
cnt = Counter()
for r in rows:
    if len(r['sup']) != 4: continue
    Sm = sorted(j for j in r['sup'] if r['delta'][j] == -1)
    Sp = sorted(j for j in r['sup'] if r['delta'][j] == 1)
    tau = r['tau']
    tSm = sorted(tau[j] for j in Sm)
    tSp = sorted(tau[j] for j in Sp)
    rel = None
    if tSm == Sp: rel = 'tau(Sm)=Sp'
    elif tSp == Sm: rel = 'tau(Sp)=Sm'
    elif tSm == Sm: rel = 'tau(Sm)=Sm'
    elif tSp == Sp: rel = 'tau(Sp)=Sp'
    else: rel = 'other'
    # note tau involution: tau(Sm)=Sp ⟺ tau(Sp)=Sm
    tr = transfer_of(r['tw'], Sm, Sp)
    assert tr == r['f']
    cnt[(r['f'], rel)] += 1
print("  (failing, tau-relation):", dict(cnt))

print("\n=== 8-point: tau-relation of decompositions vs transfer ===")
cnt2 = Counter()
for r in rows:
    if len(r['sup']) != 8: continue
    tau = r['tau']
    for dec in all_rect_decomps(r['delta']):
        (a1, b1, c1, d1), (a2, b2, c2, d2) = dec
        Sm1, Sp1 = {a1, b1}, {c1, d1}
        Sm2, Sp2 = {a2, b2}, {c2, d2}
        tSm1 = set(tau[j] for j in Sm1); tSm2 = set(tau[j] for j in Sm2)
        tSp1 = set(tau[j] for j in Sp1); tSp2 = set(tau[j] for j in Sp2)
        swap = (tSm1 == Sp2 and tSm2 == Sp1)
        parallel = (tSm1 == Sm2 and tSp1 == Sp2) or (tSm1 == Sm1 and tSm2 == Sm2)
        tr1 = transfer_of(r['tw'], sorted(Sm1), sorted(Sp1))
        tr2 = transfer_of(r['tw'], sorted(Sm2), sorted(Sp2))
        cnt2[(r['f'], swap, tr1 and tr2)] += 1
print("  (failing, tau-swaps-rects, both-rects-transfer) per decomp:", dict(cnt2))

print("\n=== 8-point: does tau swap Sm<->Sp globally? ===")
cnt3 = Counter()
for r in rows:
    if len(r['sup']) != 8: continue
    tau = r['tau']
    Sm = set(j for j in r['sup'] if r['delta'][j] == -1)
    Sp = set(j for j in r['sup'] if r['delta'][j] == 1)
    tSm = set(tau[j] for j in Sm)
    cnt3[(r['f'], tSm == Sp, tSm == Sm)] += 1
print("  (failing, tau(Sm)=Sp, tau(Sm)=Sm):", dict(cnt3))

print("\n=== 4-point failing: rectangle position relation to tau fixed points ===")
# For failing 4-point: where are Sm/Sp relative to tau's per-class fixed points?
cnt4 = Counter()
for r in rows:
    if len(r['sup']) != 4 or not r['f']: continue
    tau = r['tau']
    fixed = {}
    for cl in range(4):
        cls = [cl, cl+4, cl+8]
        fixed[cl] = [j for j in cls if tau[j] == j][0]
    Sm = [j for j in r['sup'] if r['delta'][j] == -1]
    Sp = [j for j in r['sup'] if r['delta'][j] == 1]
    # is any support position a fixed point of tau?
    nfix = sum(1 for j in r['sup'] if tau[j] == j)
    cnt4[nfix] += 1
print("  # support positions fixed by tau (failing 4-point):", dict(cnt4))
cnt5 = Counter()
for r in rows:
    if len(r['sup']) != 8: continue
    tau = r['tau']
    nfix = sum(1 for j in r['sup'] if tau[j] == j)
    cnt5[(r['f'], nfix)] += 1
print("  # support positions fixed by tau (8-point, by failing):", dict(cnt5))

print("\n=== 594 detail: w, tw, and the swap ===")
for r in rows:
    if r['gi'] == 594:
        print("  tau", r['tau'])
        print("  w ", r['w'])
        print("  wp", r['wp'])
        print("  tw", r['tw'])
        print("  delta", r['delta'])
        # class sums of w and wp
        for name, vec in (('w', r['w']), ('wp', r['wp'])):
            print("  ", name, "class sums", [sum(vec[j] for j in [cl, cl+4, cl+8]) for cl in range(4)])
