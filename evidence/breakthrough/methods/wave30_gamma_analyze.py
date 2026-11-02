"""Wave 30, task 2: component patterns, type vs Gamma_q, constraint sets."""
import json
from collections import Counter, defaultdict

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

def gamma_sets(y, yp):
    out = {}
    for q in QS:
        out[q] = [pi for pi in PERMS if all(yp[i] % q == y[pi[i]] % q for i in range(12))]
    return out

def ek(pi):
    k = pi[0]; eps = (pi[1]-pi[0]) % 12
    if eps == 11: eps = -1
    return (eps, k)

def all_taus(y, yp):
    byval = defaultdict(list)
    for i, v in enumerate(y):
        byval[v].append(i)
    order = sorted(range(12), key=lambda j: len(byval[yp[j]]))
    tau = [None]*12; used = set(); res = []
    def bt(t):
        if len(res) > 500: return
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

def class_map_type(tau):
    """For a perm tau: does it preserve classes mod 4, or swap via r->-r+1, or other?"""
    cm = {}
    ok_pres = True; ok_swap = True
    for j in range(12):
        r = j % 4; s = tau[j] % 4
        cm.setdefault(r, set()).add(s)
        if s != r: ok_pres = False
        if s != (-r + 1) % 4: ok_swap = False
    if ok_pres: return 'I-preserve'
    if ok_swap: return 'II-swap'
    return 'other:' + str({k: sorted(v) for k, v in cm.items()})

def component_pattern(y, q):
    """v = y mod q; find its period and stabilizer subgroup in Dih."""
    v = [x % q for x in y]
    stab = [pi for pi in PERMS if all(v[pi[i]] == v[i] for i in range(12))]
    # minimal period
    per = None
    for p in (1, 2, 3, 4, 6, 12):
        if all(v[(i+p) % 12] == v[i] for i in range(12)):
            per = p; break
    return v, per, [ek(pi) for pi in stab]

def main():
    d = json.load(open('wave18_Pw_m12_census.json'))
    failing = []
    for gi, g in enumerate(d['split_groups']):
        orbs = g['orbits']
        for a in range(len(orbs)):
            for b in range(a+1, len(orbs)):
                if orbs[a]['sorted_w'] == orbs[b]['sorted_w']:
                    failing.append((gi, orbs[a]['rep'], orbs[b]['rep']))
    print("failing pairs:", len(failing))

    # 1. component patterns of y (first rep) per q
    pat_counter = defaultdict(Counter)
    for gi, y, yp in failing:
        for q in QS:
            v, per, stab = component_pattern(y, q)
            # pattern up to value renaming: equality pattern on one period
            pat_counter[q][per] += 1
    for q in QS:
        print(f"q={q} periods of y mod q:", dict(pat_counter[q]))

    # 2. v_81 pattern form: values on residues 0..3
    c81 = Counter()
    for gi, y, yp in failing:
        v = [x % 81 for x in y]
        pat = (v[0], v[4], v[8])
        # equality pattern among the 4 classes (values at residues 0,1,2,3)
        vals = [v[r] for r in range(4)]
        # canonical equality pattern
        eq = []
        for i in range(4):
            eq.append(min(j for j in range(4) if vals[j] == vals[i]))
        c81[tuple(eq)] += 1
    print("v_81 class-value equality patterns (residues 0..3):", dict(c81))

    # 3. type vs Gamma_q tuple
    type_gamma = defaultdict(Counter)
    type_count = Counter()
    gamma_tuple_by_type = defaultdict(set)
    for gi, y, yp in failing:
        taus = all_taus(y, yp)
        cpis = [t for t in taus if is_cpi(t)]
        if cpis:
            typ = 'I'
        else:
            # check the swap type on any tau
            typ = 'II?' if any(class_map_type(t) == 'II-swap' for t in taus) else 'other'
        type_count[typ] += 1
        gs = gamma_sets(y, yp)
        tup = tuple(tuple(sorted(ek(pi) for pi in gs[q])) for q in QS)
        gamma_tuple_by_type[typ].add(tup)
    print("types:", dict(type_count))
    for typ, s in gamma_tuple_by_type.items():
        print(f"type {typ}: distinct Gamma tuples: {len(s)}")
    # intersection of Gamma tuples across types?
    if 'I' in gamma_tuple_by_type and 'II?' in gamma_tuple_by_type:
        inter = gamma_tuple_by_type['I'] & gamma_tuple_by_type['II?']
        print("Gamma tuples shared between I and II?:", len(inter))
        if inter:
            print("  example shared tuple (q=128,81,25,49,121):")
            t = next(iter(inter))
            for q, tt in zip(QS, t):
                print(f"    q={q}: {tt}")

    # 4. For Type I pairs: within-class action of cpi tau, and mod-3 action
    mod3_counter = Counter()
    for gi, y, yp in failing:
        taus = all_taus(y, yp)
        cpis = [t for t in taus if is_cpi(t)]
        if not cpis: continue
        tau = cpis[0]
        # tau(j) mod 3 as function of j mod 3 and j mod 4?
        rel = tuple((tau[j] % 3, j % 3) for j in range(12))
        mod3_counter[rel] += 1
    print("distinct (tau(j) mod 3, j mod 3) relations over Type I:", len(mod3_counter))
    for rel, n in mod3_counter.most_common(5):
        print("   ", n, rel)

if __name__ == '__main__':
    main()
