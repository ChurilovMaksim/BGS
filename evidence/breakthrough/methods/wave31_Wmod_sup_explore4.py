"""Wave 31, task 2, part 4: shift-pattern analysis.
s(i) = tau(i) - i mod 12 in {0,4,8}. Neighbor identity:
D*delta_i = (y[tau(i)-1] - y[tau(i-1)]) + (y[tau(i)+1] - y[tau(i+1)]).
If s(i-1)=s(i)=s(i+1) then delta_i = 0. So supp(delta) is contained in
the boundary neighborhood of s."""
import json
from collections import Counter, defaultdict
from itertools import product

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

# --- Part A: all 81 cpi shift patterns, neighborhood sizes ---
print("=== All 81 cpi tau: shift pattern -> neighborhood size ===")
nb_dist = Counter()
patterns = {}
for fixed_choice in product(range(3), repeat=4):
    # fixed point of class r is r + 4*fixed_choice[r]
    tau = [None]*12
    for r in range(4):
        cls = [r, r+4, r+8]
        f = cls[fixed_choice[r]]
        others = [j for j in cls if j != f]
        tau[f] = f
        tau[others[0]] = others[1]
        tau[others[1]] = others[0]
    s = tuple((tau[i] - i) % 12 for i in range(12))
    nb = [i for i in range(12) if s[(i-1) % 12] != s[i] or s[(i+1) % 12] != s[i]]
    nb_dist[len(nb)] += 1
    patterns.setdefault(len(nb), []).append((fixed_choice, s, nb))
print("  neighborhood size distribution over 81 cpi:", dict(nb_dist))
for k in sorted(patterns):
    print(f"  size {k}: {len(patterns[k])} patterns, e.g. fixed={patterns[k][0][0]} s={patterns[k][0][1]} nb={patterns[k][0][2]}")

# --- Part B: census cpi pairs: |sup| vs neighborhood size ---
d = json.load(open('wave18_Pw_m12_census.json'))
cnt = Counter()
mismatch = []
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
            s = tuple((tau[i] - i) % 12 for i in range(12))
            nb = [i for i in range(12) if s[(i-1) % 12] != s[i] or s[(i+1) % 12] != s[i]]
            # verify neighbor identity
            for i in range(12):
                lhs = D * delta[i]
                rhs = (y[(tau[i]-1) % 12] - y[tau[(i-1) % 12]]) + (y[(tau[i]+1) % 12] - y[tau[(i+1) % 12]])
                assert lhs == rhs, (gi, i, lhs, rhs)
            cnt[(len(nb), len(sup), f)] += 1
            if set(sup) != set(nb):
                mismatch.append((gi, f, nb, sup, delta, s))
print("\n=== Census: (neighborhood size, |sup|, failing) ===")
for k in sorted(cnt):
    print("  ", k, cnt[k])
print("pairs where sup != neighborhood:", len(mismatch))
for m in mismatch[:10]:
    print("  gi", m[0], "f", m[1], "nb", m[2], "sup", m[3], "delta", m[4])
