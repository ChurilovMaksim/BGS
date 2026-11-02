"""Wave 30, task 2: refined analysis - antipodal vs S-const, moment mechanism,
Stab-orbit fibers, group 689, dual-valid pairs."""
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

def compose(a, b):
    """function composition: (a after b)(i) = a[b[i]]."""
    return tuple(a[b[i]] for i in range(12))

def inv(pi):
    q = [0]*12
    for i, v in enumerate(pi):
        q[v] = i
    return tuple(q)

def gamma_sets(y, yp):
    out = {}
    for q in QS:
        out[q] = [pi for pi in PERMS if all(yp[i] % q == y[pi[i]] % q for i in range(12))]
    return out

def stab_of(v):
    return [pi for pi in PERMS if all(v[pi[i]] == v[i] for i in range(12))]

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

def main():
    d = json.load(open('wave18_Pw_m12_census.json'))
    allpairs = []
    for gi, g in enumerate(d['split_groups']):
        orbs = g['orbits']
        for a in range(len(orbs)):
            for b in range(a+1, len(orbs)):
                f = (orbs[a]['sorted_w'] == orbs[b]['sorted_w'])
                allpairs.append((gi, orbs[a]['rep'], orbs[b]['rep'], f))
    print("all orbit pairs:", len(allpairs))

    # A. fibers = Stab-orbits? for all pairs, all q
    fiber_eq_orbit = Counter()
    for gi, y, yp, f in allpairs:
        for q in QS:
            v = [x % q for x in y]
            stab = stab_of(v)
            # orbits of stab on positions
            seen = set(); orbits = []
            for i in range(12):
                if i in seen: continue
                orb = set()
                stack = [i]
                while stack:
                    k = stack.pop()
                    if k in orb: continue
                    orb.add(k)
                    for pi in stab:
                        stack.append(pi[k])
                seen |= orb
                orbits.append(orb)
            # fibers of v
            fib = defaultdict(set)
            for i, val in enumerate(v):
                fib[val].add(i)
            fibsets = set(frozenset(s) for s in fib.values())
            orbsets = set(frozenset(s) for s in orbits)
            fiber_eq_orbit[(q, fibsets == orbsets)] += 1
    print("fibers == Stab-orbits (q, equal?):", dict(fiber_eq_orbit))

    # B. cpi pairs: cross-tab (failing, S-constant, antipodal, delta==0)
    ct = Counter()
    anti_fail_examples = []
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
        anti = True
        if sup:
            found = False
            for p in range(12):
                s = sorted({(p-1) % 12, (p+1) % 12, (p+5) % 12, (p+7) % 12})
                if tsup == s:
                    if y[(p-1) % 12] + y[(p+1) % 12] == y[(p+5) % 12] + y[(p+7) % 12]:
                        found = True
            anti = found
        ct[(f, sconst, anti, len(sup) == 0)] += 1
        if f and not anti:
            anti_fail_examples.append((gi, sup, tsup, delta))
    print("cpi cross-tab (failing, S-const, antipodal, delta==0):")
    for k, n in sorted(ct.items(), key=str):
        print("   ", k, n)
    print("failing cpi pairs failing antipodal:", anti_fail_examples)

    # C. moment mechanism: W_r = sum of w over j%3==r; check W congruences vs c
    mech = Counter()
    for gi, y, yp, f in allpairs:
        taus = all_taus(y, yp)
        cpis = [t for t in taus if is_cpi(t)]
        if not cpis: continue
        tau = cpis[0]
        w = wvec(y)
        c = tau[0] % 3  # tau(j)%3 = -j+c
        Wr = [sum(w[j] for j in range(12) if j % 3 == r) % 3 for r in range(3)]
        # predicted: W_{1-c} == W_{2-c} mod 3 (from derivation)
        pred = (Wr[(1-c) % 3] == Wr[(2-c) % 3])
        mech[(c, pred, tuple(Wr))] += 1
    print("moment mechanism (c, W_{1-c}==W_{2-c} mod 3, Wr mod 3):")
    agg = Counter()
    for (c, pred, Wr), n in mech.items():
        agg[(c, pred)] += n
    print("   aggregated (c, pred):", dict(agg))
    print("   Wr patterns:", Counter({Wr: n for (c, pred, Wr), n in mech.items()}))

    # D. group 689 detail + dual-valid (id and swapboth) pairs
    for gi, y, yp, f in allpairs:
        if gi == 689 and f:
            gs = gamma_sets(y, yp)
            print("group 689 Gamma_49:", [ek(pi) for pi in gs[49]])
            print("group 689 Gamma_25:", [ek(pi) for pi in gs[25]])
            print("group 689 Gamma_128 size:", len(gs[128]))
            taus = all_taus(y, yp)
            print("group 689 n_taus:", len(taus))
            for t in taus[:6]:
                print("   tau:", t, "cpi?", is_cpi(t))

if __name__ == '__main__':
    main()
