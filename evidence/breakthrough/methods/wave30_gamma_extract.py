"""Wave 30, task 2: extract failing pairs, tau structure, and Gamma_q sets."""
import json
from collections import Counter, defaultdict

D = 1536796800
QS = [128, 81, 25, 49, 121]

def Hvec(y):
    return [6*y[i] - y[i-1] - y[(i+1) % 12] for i in range(12)]

def wvec(y):
    h = Hvec(y)
    assert all(x % D == 0 for x in h), "Hy not divisible by D"
    return [x // D for x in h]

def dihedral_perms():
    """24 perms pi with (gamma v)[i] = v[pi[i]]; pi[i] = eps*i + k mod 12."""
    perms = []
    for eps in (1, -1):
        for k in range(12):
            perms.append(tuple((eps*i + k) % 12 for i in range(12)))
    return perms

PERMS = dihedral_perms()

def gamma_sets(y, yp):
    """Gamma_q = {pi : yp[i] == y[pi[i]] mod q for all i}."""
    out = {}
    for q in QS:
        gs = [pi for pi in PERMS if all(yp[i] % q == y[pi[i]] % q for i in range(12))]
        out[q] = gs
    return out

def all_taus(y, yp):
    """All perms tau with yp[j] == y[tau[j]]. (Backtracking over value classes.)"""
    # positions grouped by value
    from collections import defaultdict
    byval = defaultdict(list)
    for i, v in enumerate(y):
        byval[v].append(i)
    # assign: for each j, tau[j] must be a position with value yp[j]
    # use simple backtracking with forward ordering
    order = sorted(range(12), key=lambda j: len(byval[yp[j]]))
    tau = [None]*12
    used = set()
    res = []
    def bt(t):
        if len(res) > 200:  # cap
            return
        if t == 12:
            res.append(tuple(tau))
            return
        j = order[t]
        for i in byval[yp[j]]:
            if i not in used:
                used.add(i); tau[j] = i
                bt(t+1)
                used.discard(i); tau[j] = None
    bt(0)
    return res

def is_cpi(tau):
    """Class-preserving involution: tau maps each mod-4 class to itself,
    tau^2 = id, and exactly one transposition per class (3 elements each)."""
    if any(tau[tau[j]] != j for j in range(12)):
        return False
    for r in range(4):
        cls = [r, r+4, r+8]
        img = sorted(tau[j] for j in cls)
        if img != cls:
            return False
        fixed = sum(1 for j in cls if tau[j] == j)
        if fixed != 1:
            return False
    return True

def main():
    d = json.load(open('wave18_Pw_m12_census.json'))
    failing = []  # (group_idx, y, yp, w, wp)
    for gi, g in enumerate(d['split_groups']):
        orbs = g['orbits']
        # pairs of orbits sharing sorted_w
        for a in range(len(orbs)):
            for b in range(a+1, len(orbs)):
                if orbs[a]['sorted_w'] == orbs[b]['sorted_w']:
                    failing.append((gi, orbs[a]['rep'], orbs[b]['rep']))
    print("failing pairs:", len(failing))
    # sanity: pw_ok flag
    npwfail = sum(1 for g in d['split_groups'] if not g['pw_ok'])
    print("groups with pw_ok False:", npwfail)

    stats = Counter()
    gamma_size_dist = defaultdict(Counter)
    tau_cpi_count = 0
    tau_unique = 0
    examples = []
    for gi, y, yp in failing:
        w = wvec(y); wp = wvec(yp)
        assert sorted(w) == sorted(wp)
        gs = gamma_sets(y, yp)
        for q in QS:
            gamma_size_dist[q][len(gs[q])] += 1
        taus = all_taus(y, yp)
        cpis = [t for t in taus if is_cpi(t)]
        if len(taus) == 1:
            tau_unique += 1
        if cpis:
            tau_cpi_count += 1
        stats['pairs'] += 1
        if len(examples) < 8:
            examples.append((gi, y, yp, w, wp, gs, taus, cpis))
    print("pairs with >=1 cpi tau:", tau_cpi_count)
    print("pairs with unique tau:", tau_unique)
    for q in QS:
        print(f"Gamma_{q} size distribution:", dict(gamma_size_dist[q]))
    for gi, y, yp, w, wp, gs, taus, cpis in examples:
        print(f"--- group {gi}: n_taus={len(taus)} n_cpi={len(cpis)}")
        for q in QS:
            # summarize gamma as (eps,k) pairs
            eks = []
            for pi in gs[q]:
                # recover eps,k: pi[0]=k, pi[1]-pi[0] mod 12 = eps
                k = pi[0]; eps = (pi[1]-pi[0]) % 12
                if eps == 11: eps = -1
                eks.append((eps, k))
            print(f"   Gamma_{q}: {eks}")
        if cpis:
            print(f"   cpi tau: {cpis[0]}")
        print(f"   w ={w}")
        print(f"   wp={wp}")

if __name__ == '__main__':
    main()
