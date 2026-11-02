"""Wave 31, task 2: why do failing pairs have |sup| in {0,4}?
Explore delta structure over all cpi pairs in the wave-18 census."""
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

def rect_decomp(delta):
    """Decompose delta (values in {-1,0,1}) as sum of disjoint rectangles
    -e_a - e_b + e_c + e_d with a+b == c+d (mod 12). Greedy exact search."""
    Sm = [j for j in range(12) if delta[j] == -1]
    Sp = [j for j in range(12) if delta[j] == 1]
    if len(Sm) != len(Sp):
        return None
    # search pairing into rectangles
    def search(Sm, Sp):
        if not Sm:
            return []
        a = Sm[0]
        for bi, b in enumerate(Sm[1:], 1):
            for ci, c in enumerate(Sp):
                for di, d in enumerate(Sp):
                    if di <= ci: continue
                    if (a + b) % 12 == (c + d) % 12:
                        rest = search([x for k, x in enumerate(Sm[1:], 1) if k != bi],
                                      [x for k, x in enumerate(Sp) if k != ci and k != di])
                        if rest is not None:
                            return [(a, b, c, d)] + rest
        return None
    return search(Sm, Sp)

d = json.load(open('wave18_Pw_m12_census.json'))
pairs = []
for gi, g in enumerate(d['split_groups']):
    orbs = g['orbits']
    for a in range(len(orbs)):
        for b in range(a+1, len(orbs)):
            f = (orbs[a]['sorted_w'] == orbs[b]['sorted_w'])
            pairs.append((gi, orbs[a]['rep'], orbs[b]['rep'], f))

rows = []
for gi, y, yp, f in pairs:
    taus = all_taus(y, yp)
    cpis = [t for t in taus if is_cpi(t)]
    if not cpis: continue
    assert len(cpis) == 1, (gi, len(cpis))
    tau = cpis[0]
    w = wvec(y); wp = wvec(yp)
    tw = [w[tau[j]] for j in range(12)]
    delta = [wp[j] - tw[j] for j in range(12)]
    sup = [j for j in range(12) if delta[j] != 0]
    Sm = [j for j in sup if delta[j] == -1]
    Sp = [j for j in sup if delta[j] == 1]
    sconst = (Svals(y, w) == Svals(yp, wp))
    defect = tuple(sorted(set(j % 4 for j in sup)))
    # transfer condition (exact for +-1 delta): {tw on Sm} == {tw+1 on Sp}
    transfer = (sorted(tw[j] for j in Sm) == sorted(tw[j] + 1 for j in Sp)) if set(delta) <= {-1, 0, 1} else None
    # weighted sum sum_i y[tau[i]] delta[i]  (== Delta S^(0) up to psi terms? record raw)
    wsum = sum(y[tau[i]] * delta[i] for i in range(12))
    # per-class fixed point of tau
    fixed = {}
    for r in range(4):
        cls = [r, r+4, r+8]
        fixed[r] = [j for j in cls if tau[j] == j][0]
    rows.append(dict(gi=gi, y=y, yp=yp, f=f, tau=tau, w=w, wp=wp, tw=tw,
                     delta=delta, sup=sup, Sm=Sm, Sp=Sp, sconst=sconst,
                     defect=defect, transfer=transfer, wsum=wsum, fixed=fixed))

print("cpi pairs:", len(rows))
print("delta value sets:", Counter(tuple(sorted(set(r['delta']))) for r in rows))
print("|sup| x failing:", Counter((len(r['sup']), r['f']) for r in rows))
print("defect classes x failing:", Counter((r['defect'], r['f']) for r in rows))
print("transfer (failing):", Counter((r['f'], r['transfer']) for r in rows))
print("wsum==0 x failing x sconst:", Counter((r['wsum'] == 0, r['f'], r['sconst']) for r in rows))
# rectangle decompositions by |sup|
for s in (4, 8):
    sub = [r for r in rows if len(r['sup']) == s]
    dec = Counter()
    for r in sub:
        rd = rect_decomp(r['delta'])
        if rd is None:
            dec['none'] += 1
        else:
            sums = tuple(sorted((a + b) % 12 for a, b, c, dd in rd))
            dec[('rects', len(rd), sums if len(set(sums)) == 1 else 'mixed-sums')] += 1
    print(f"|sup|={s}: rect decomps:", dict(dec))
# failing 8-point pairs: list them
print("\nFailing pairs with |sup|=8:")
for r in rows:
    if r['f'] and len(r['sup']) == 8:
        print("  group", r['gi'], "delta", r['delta'], "tau", r['tau'],
              "defect", r['defect'], "sconst", r['sconst'], "transfer", r['transfer'])
# non-failing S-const 8-point: how does sorted(wp) differ from sorted(w)?
print("\nNon-failing S-const 8-point: sorted(w) vs sorted(wp) diff patterns:")
pat = Counter()
for r in rows:
    if (not r['f']) and r['sconst'] and len(r['sup']) == 8:
        sw = sorted(r['w']); swp = sorted(r['wp'])
        pat[(tuple(sorted(Counter(sw).items())), tuple(sorted(Counter(swp).items())))] += 0  # placeholder
        # histogram distance
        cw, cp = Counter(sw), Counter(swp)
        dist = sum(abs(cw[v] - cp[v]) for v in set(cw) | set(cp)) // 2
        pat[('histdist', dist)] += 1
print("  ", dict(pat))
# For 8-point pairs: tau-image of support, and sign-set y-sums
print("\n8-point pairs: tau(Sm), tau(Sp), and y-sums over sign sets:")
for r in rows:
    if len(r['sup']) == 8 and (r['f'] or r['sconst']):
        tSm = sorted(r['tau'][j] for j in r['Sm'])
        tSp = sorted(r['tau'][j] for j in r['Sp'])
        ySm = sum(r['y'][j] for j in r['Sm']); ySp = sum(r['y'][j] for j in r['Sp'])
        yTSm = sum(r['y'][r['tau'][j]] for j in r['Sm']); yTSp = sum(r['y'][r['tau'][j]] for j in r['Sp'])
        print(f"  gi={r['gi']} f={int(r['f'])} sc={int(r['sconst'])} Sm={r['Sm']} Sp={r['Sp']} "
              f"tSm={tSm} tSp={tSp} ySm==ySp:{ySm==ySp} yTSm==yTSp:{yTSm==yTSp} transfer={r['transfer']}")
