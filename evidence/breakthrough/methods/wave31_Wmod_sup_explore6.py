"""Wave 31, task 2, part 6: per-class transfer differences and rectangle sums."""
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
    """For each defect class: (m_r, p_r) = (minus position, plus position)."""
    out = {}
    for cl in range(4):
        cls = [cl, cl+4, cl+8]
        ms = [j for j in cls if r['delta'][j] == -1]
        ps = [j for j in cls if r['delta'][j] == 1]
        if ms:
            assert len(ms) == 1 and len(ps) == 1
            out[cl] = (ms[0], ps[0])
    return out

print("=== 4-point: aligned vs crossed matching, by failing ===")
cnt = Counter()
for r in rows:
    if len(r['sup']) != 4: continue
    mp = per_class_mp(r)
    cls = sorted(mp)
    (m1, p1), (m2, p2) = mp[cls[0]], mp[cls[1]]
    tw = r['tw']
    aligned = (tw[m1] == tw[p1] + 1 and tw[m2] == tw[p2] + 1)
    crossed = (tw[m1] == tw[p2] + 1 and tw[m2] == tw[p1] + 1)
    cnt[(r['f'], aligned, crossed)] += 1
print("  (failing, aligned, crossed):", dict(cnt))

print("\n=== per-class difference d_r = tw[m_r] - tw[p_r]: distribution by |sup| x failing ===")
cnt2 = Counter()
for r in rows:
    mp = per_class_mp(r)
    for cl, (m, p) in mp.items():
        cnt2[(len(r['sup']), r['f'], r['tw'][m] - r['tw'][p])] += 1
for k in sorted(cnt2):
    print("  ", k, cnt2[k])

print("\n=== 4-point: failing rate by rectangle index-sum ===")
cnt3 = Counter()
for r in rows:
    if len(r['sup']) != 4: continue
    decs = all_rect_decomps(r['delta'])
    assert len(decs) == 1
    (a, b, c, dd) = decs[0][0]
    cnt3[((a + b) % 12, r['f'])] += 1
for k in sorted(cnt3):
    print("  ", k, cnt3[k])

print("\n=== 8-point: per-decomp both-transfer vs rectangle sums ===")
cnt4 = Counter()
for r in rows:
    if len(r['sup']) != 8: continue
    for dec in all_rect_decomps(r['delta']):
        sums = tuple(sorted((a + b) % 12 for a, b, c, dd in dec))
        trs = tuple(sorted(tw for tw in [r['tw'][a] - (r['tw'][c] + 1) for a, b, c, dd in [dec[0]]]))  # unused
        from collections import Counter as C
        def tr(rect):
            a, b, c, dd = rect
            return sorted([r['tw'][a], r['tw'][b]]) == sorted([r['tw'][c] + 1, r['tw'][dd] + 1])
        both = tr(dec[0]) and tr(dec[1])
        cnt4[(r['f'], sums, both)] += 1
agg = Counter()
for (f, sums, both), n in cnt4.items():
    agg[(f, both)] += n
print("  (failing, both-transfer) over all decomps:", dict(agg))
print("  both-transfer decomps detail (failing only):")
for (f, sums, both), n in cnt4.items():
    if f and both:
        print("   ", sums, n)

print("\n=== N(j) structure: distinct neighbor-sum values per class (sample) ===")
# N(j) = y[j-1]+y[j+1]; check differences within a class are multiples of D
import itertools
sample = [r for r in rows[:50]]
# need y: reload reps
ys = []
for gi, g in enumerate(d['split_groups'][:20]):
    for o in g['orbits']:
        ys.append(o['rep'])
ndiff = Counter()
for y in ys[:30]:
    for cl in range(4):
        cls = [cl, cl+4, cl+8]
        Ns = [y[(j-1) % 12] + y[(j+1) % 12] for j in cls]
        for x, z in itertools.combinations(Ns, 2):
            ndiff[(x - z) % D == 0] += 1
            if (x - z) % D != 0:
                pass
print("  neighbor-sum differences within a class divisible by D:", dict(ndiff))
