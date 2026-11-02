"""Wave 31, task 2, part 2: per-rectangle transfer and histogram defects."""
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
    """All ways to split delta into disjoint rectangles -e_a-e_b+e_c+e_d,
    a+b==c+d mod 12. Returns list of decomps (each a tuple of rects)."""
    Sm = [j for j in range(12) if delta[j] == -1]
    Sp = [j for j in range(12) if delta[j] == 1]
    if len(Sm) != len(Sp):
        return []
    def search(Sm, Sp):
        if not Sm:
            return [()]
        a = Sm[0]
        out = []
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

def histdist(w, wp):
    cw, cp = Counter(w), Counter(wp)
    return sum(abs(cw[v] - cp[v]) for v in set(cw) | set(cp)) // 2

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

print("histdist by |sup| x failing:")
print(Counter((len(r['sup']), r['f'], histdist(r['w'], r['wp'])) for r in rows))

print("\n8-point: per-rectangle transfer analysis (over ALL decomps):")
cnt = Counter()
examples_cross = []
for r in rows:
    if len(r['sup']) != 8: continue
    decs = all_rect_decomps(r['delta'])
    glob = transfer_of(r['tw'], [j for j in r['sup'] if r['delta'][j] == -1],
                       [j for j in r['sup'] if r['delta'][j] == 1])
    assert glob == r['f']
    # for each decomp: does every rect transfer? does at least one? none?
    per_dec = []
    for dec in decs:
        trs = [transfer_of(r['tw'], [a, b], [c, dd]) for a, b, c, dd in dec]
        per_dec.append(tuple(trs))
    ndec = len(decs)
    all_tr = any(all(t) for t in per_dec)
    any_tr = any(any(t) for t in per_dec)
    cnt[(r['f'], ndec, all_tr, any_tr)] += 1
    if r['f']:
        print(f"  FAILING gi={r['gi']}: ndecs={ndec} per-dec transfers={per_dec} delta={r['delta']}")
        for dec in decs:
            for (a, b, c, dd) in dec:
                print(f"    rect -({a},{b}) +({c},{dd}) sum={(a+b)%12} tw: Sm={[r['tw'][a], r['tw'][b]]} Sp+1={[r['tw'][c]+1, r['tw'][dd]+1]}")
    if glob and not all_tr:
        examples_cross.append(r['gi'])
print("  (failing, ndecs, some-dec-all-transfer, some-dec-any-transfer):", dict(cnt))
print("  cross-cancellation cases (global transfer but no dec all-transfer):", examples_cross)

print("\n8-point: rectangle sum equality vs failing:")
cnt2 = Counter()
for r in rows:
    if len(r['sup']) != 8: continue
    decs = all_rect_decomps(r['delta'])
    eq = any(len(set((a + b) % 12 for a, b, c, dd in dec)) == 1 for dec in decs)
    alleq = all(len(set((a + b) % 12 for a, b, c, dd in dec)) == 1 for dec in decs)
    cnt2[(r['f'], eq, alleq)] += 1
print("  (failing, some-dec-equal-sums, all-dec-equal-sums):", dict(cnt2))

print("\n8-point: do the two rectangles' tw-value multisets overlap?")
# For each decomp, check whether transfer could mix across rects: compare
# multiset {tw on Sm} vs {tw+1 on Sp} restricted per rect.
cnt3 = Counter()
for r in rows:
    if len(r['sup']) != 8: continue
    decs = all_rect_decomps(r['delta'])
    # imbalance vector e_v = #{Sm: tw=v} - #{Sp: tw=v-1}
    e = Counter()
    for j in r['sup']:
        if r['delta'][j] == -1: e[r['tw'][j]] += 1
        else: e[r['tw'][j] + 1] -= 1
    e = {v: c for v, c in e.items() if c != 0}
    cnt3[(r['f'], tuple(sorted(e.items())))] += 0  # skip detail; use norm
    cnt3[(r['f'], 'L1', sum(abs(c) for c in e.values()))] += 1
print("  (failing, L1 imbalance):", dict(cnt3))

print("\n4-point: per-rect transfer == failing (sanity) and histdist for non-failing:")
cnt4 = Counter()
for r in rows:
    if len(r['sup']) != 4: continue
    Sm = [j for j in r['sup'] if r['delta'][j] == -1]
    Sp = [j for j in r['sup'] if r['delta'][j] == 1]
    cnt4[(r['f'], transfer_of(r['tw'], Sm, Sp))] += 1
print("  (failing, rect-transfer):", dict(cnt4))
