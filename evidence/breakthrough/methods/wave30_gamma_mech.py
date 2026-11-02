"""Wave 30, task 2: mechanism hunts - defect sets, support size vs antipodal,
moment-law identity, CRT on all pairs."""
import json
from collections import Counter, defaultdict
from itertools import product

D = 1536796800
QS = [128, 81, 25, 49, 121]

def Hvec(y):
    return [6*y[i] - y[i-1] - y[(i+1) % 12] for i in range(12)]

def wvec(y):
    h = Hvec(y)
    assert all(x % D == 0 for x in h)
    return [x // D for x in h]

def dihedral_perms():
    return [tuple((eps*i + k) % 12 for i in range(12)) for eps in (1, -1) for k in range(12)]

PERMS = dihedral_perms()

def ek(pi):
    k = pi[0]; eps = (pi[1]-pi[0]) % 12
    if eps == 11: eps = -1
    return (eps, k)

def gamma_sets(y, yp):
    out = {}
    for q in QS:
        out[q] = [pi for pi in PERMS if all(yp[i] % q == y[pi[i]] % q for i in range(12))]
    return out

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

def crt_map(f, g):
    tau = []
    for j in range(12):
        a, b = f[j % 4], g[j % 3]
        t = (b - a) % 3
        tau.append(a + 4*t)
    return tuple(tau)

F_MAPS = {'id': (0,1,2,3), 'swap01': (1,0,2,3), 'swap23': (0,1,3,2), 'swapboth': (1,0,3,2)}
G_MAPS = {}
for p in product(range(3), repeat=3):
    if sorted(p) == [0,1,2]:
        kind = 'rot' if p == tuple((x + p[0]) % 3 for x in range(3)) else 'refl'
        G_MAPS[(kind, p)] = p

def Svals(y, w):
    return [sum(y[i]*w[(i+d) % 12] for i in range(12)) for d in range(12)]

def main():
    d = json.load(open('wave18_Pw_m12_census.json'))
    allpairs = []
    for gi, g in enumerate(d['split_groups']):
        orbs = g['orbits']
        for a in range(len(orbs)):
            for b in range(a+1, len(orbs)):
                f = (orbs[a]['sorted_w'] == orbs[b]['sorted_w'])
                allpairs.append((gi, orbs[a]['rep'], orbs[b]['rep'], f))

    # 1. CRT valid maps on ALL pairs: does any mixed f survive anywhere?
    mixed_all = []
    fpat_all = Counter()
    for gi, y, yp, f in allpairs:
        valid = []
        for fname, ff in F_MAPS.items():
            for (kind, gg), g in G_MAPS.items():
                tau = crt_map(ff, g)
                if all(y[tau[j]] == yp[j] for j in range(12)):
                    valid.append((fname, kind))
        fpat_all[tuple(sorted(set(v[0] for v in valid)))] += 1
        if any(v[0] in ('swap01', 'swap23') for v in valid):
            mixed_all.append(gi)
    print("CRT f-patterns over ALL pairs:", dict(fpat_all))
    print("pairs with mixed CRT map valid:", len(mixed_all), mixed_all[:10])

    # 2. defect sets for cpi pairs + correlation with c, per128
    defect_tab = Counter()
    supsize_anti = Counter()
    for gi, y, yp, f in allpairs:
        taus = all_taus(y, yp)
        cpis = [t for t in taus if is_cpi(t)]
        if not cpis: continue
        tau = cpis[0]
        w = wvec(y); wp = wvec(yp)
        tw = [w[tau[j]] for j in range(12)]
        delta = [wp[j] - tw[j] for j in range(12)]
        defect = tuple(sorted(set(j % 4 for j in range(12) if delta[j] != 0)))
        c = tau[0] % 3
        v128 = [x % 128 for x in y]
        per128 = 1 if len(set(v128)) == 1 else 2
        defect_tab[(defect, c, per128, f)] += 1
        # support size vs antipodal (S-constant pairs only)
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
        if sconst:
            supsize_anti[(len(sup), anti, f)] += 1
    print("defect sets (defect, c, per128, failing): count")
    agg = Counter()
    for (df, c, p128, f), n in defect_tab.items():
        agg[df] += n
    print("   defect-set totals:", dict(agg))
    print("   by (defect, failing):", Counter({(df, f): n for (df, c, p128, f), n in defect_tab.items()}))
    print("support-size vs antipodal (S-constant cpi pairs): (size, anti, failing)")
    for k, n in sorted(supsize_anti.items()):
        print("   ", k, n)

    # 3. moment mechanism hunt: test identities mod 12
    # M1 = sum j*delta_j ; candidates:
    #  A = sum_j (j - tau(j)) * wp[j]  (using wp instead of w)
    #  B = sum_j (j - tau(j)) * w[j]
    #  C = M(wp) - M(w)  where M(v) = sum j*v[j]
    #  D = sum_j delta_j * tau(j)
    ident = Counter()
    for gi, y, yp, f in allpairs:
        taus = all_taus(y, yp)
        cpis = [t for t in taus if is_cpi(t)]
        if not cpis: continue
        tau = cpis[0]
        w = wvec(y); wp = wvec(yp)
        tw = [w[tau[j]] for j in range(12)]
        delta = [wp[j] - tw[j] for j in range(12)]
        M1 = sum(j*delta[j] for j in range(12)) % 12
        A = sum(((j - tau[j]) % 12) * wp[j] for j in range(12)) % 12
        B = sum(((j - tau[j]) % 12) * w[j] for j in range(12)) % 12
        C = (sum(j*wp[j] for j in range(12)) - sum(j*w[j] for j in range(12))) % 12
        Dd = sum(delta[j] * tau[j] for j in range(12)) % 12
        ident[('M1==0', M1 == 0)] += 1
        ident[('M1==A', M1 == A)] += 1
        ident[('M1==B', M1 == B)] += 1
        ident[('M1==C', M1 == C)] += 1
        ident[('M1+D==0', (M1 + Dd) % 12 == 0)] += 1
    print("moment identity tests:", dict(ident))

if __name__ == '__main__':
    main()
