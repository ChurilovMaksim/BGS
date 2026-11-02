"""Wave 30, task 2: CRT-form test + delta-law scope test."""
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
    """f: Z/4 -> Z/4 perm, g: Z/3 -> Z/3 perm; return tau on Z/12 via CRT.
    tau(j) = unique x with x%4 = f(j%4), x%3 = g(j%3)."""
    tau = []
    for j in range(12):
        a, b = f[j % 4], g[j % 3]
        # solve x = a mod 4, x = b mod 3: x = a + 4t, a+4t = b mod 3 -> t = b-a mod 3
        t = (b - a) % 3
        tau.append(a + 4*t)
    return tuple(tau)

# class maps preserving pairs {0,1},{2,3}
F_MAPS = {
    'id': (0, 1, 2, 3),
    'swap01': (1, 0, 2, 3),
    'swap23': (0, 1, 3, 2),
    'swapboth': (1, 0, 3, 2),
}
# all perms of Z/3
G_MAPS = {}
for p in product(range(3), repeat=3):
    if sorted(p) == [0, 1, 2]:
        kind = 'rot' if p == tuple((x + p[0]) % 3 for x in range(3)) else 'refl'
        G_MAPS[(kind, p)] = p

def main():
    d = json.load(open('wave18_Pw_m12_census.json'))
    failing = []
    allpairs = []  # (gi, y, yp, failing?)
    for gi, g in enumerate(d['split_groups']):
        orbs = g['orbits']
        for a in range(len(orbs)):
            for b in range(a+1, len(orbs)):
                f = (orbs[a]['sorted_w'] == orbs[b]['sorted_w'])
                allpairs.append((gi, orbs[a]['rep'], orbs[b]['rep'], f))
                if f:
                    failing.append((gi, orbs[a]['rep'], orbs[b]['rep']))
    print("all orbit pairs:", len(allpairs), "failing:", len(failing))

    # 1. Gamma_81 identical across failing pairs?
    g81set = set()
    for gi, y, yp in failing:
        gs = gamma_sets(y, yp)
        g81set.add(tuple(sorted(ek(pi) for pi in gs[81])))
    print("distinct Gamma_81 among failing:", len(g81set), g81set if len(g81set) <= 2 else '')

    # 2. CRT test: which (f,g) CRT maps are valid taus (y[tau[j]] == yp[j])?
    crt_stats = Counter()
    mixed_survive = []
    for gi, y, yp in failing:
        valid = []
        for fname, f in F_MAPS.items():
            for (kind, g), gg in G_MAPS.items():
                tau = crt_map(f, gg)
                if all(y[tau[j]] == yp[j] for j in range(12)):
                    valid.append((fname, kind, gg))
        crt_stats[tuple(sorted(v[0] for v in valid))] += 1
        # check: does any mixed f survive?
        if any(v[0] in ('swap01', 'swap23') for v in valid):
            mixed_survive.append((gi, valid))
    print("CRT valid-map f-patterns across failing pairs:", dict(crt_stats))
    print("pairs where a MIXED class map survives:", len(mixed_survive))
    for gi, valid in mixed_survive[:5]:
        print("   group", gi, valid)

    # 3. delta-law scope: for ALL orbit pairs, find cpi tau (if any), check laws
    # laws: parity (defect classes subset of {0,2} or {1,3} or all/none),
    #       moment sum i*delta_i == 0 mod 12,
    #       antipodal: tau-images of delta-support form {p-1,p+1,p+5,p+7} with N(p)==N(p+6)
    law_stats = Counter()
    for gi, y, yp, f in allpairs:
        taus = all_taus(y, yp)
        cpis = [t for t in taus if is_cpi(t)]
        if not cpis:
            law_stats[('no-cpi', f)] += 1
            continue
        tau = cpis[0]
        w = wvec(y); wp = wvec(yp)
        tw = [w[tau[j]] for j in range(12)]
        delta = [wp[j] - tw[j] for j in range(12)]
        # parity law: defect classes (classes r where some delta[j]!=0 for j in class r)
        defect = set()
        for j in range(12):
            if delta[j] != 0:
                defect.add(j % 4)
        parity_ok = defect <= {0, 2} or defect <= {1, 3} or defect == set() or defect == {0, 1, 2, 3}
        moment_ok = (sum(j*delta[j] for j in range(12)) % 12 == 0)
        # antipodal law: tau-images of support
        sup = [j for j in range(12) if delta[j] != 0]
        tsup = sorted(set(tau[j] for j in sup))
        anti_ok = True
        if sup:
            # check tsup == {p-1,p+1,p+5,p+7} for some p with N(p)==N(p+6)
            found = False
            for p in range(12):
                s = sorted({(p-1) % 12, (p+1) % 12, (p+5) % 12, (p+7) % 12})
                if tsup == s:
                    Np = y[(p-1) % 12] + y[(p+1) % 12]
                    Np6 = y[(p+5) % 12] + y[(p+7) % 12]
                    if Np == Np6:
                        found = True
            anti_ok = found
        law_stats[('cpi', f, parity_ok, moment_ok, anti_ok)] += 1
    print("delta-law scope (has-cpi, failing?, parity, moment, antipodal):")
    for k, n in sorted(law_stats.items(), key=str):
        print("   ", k, n)

if __name__ == '__main__':
    main()
