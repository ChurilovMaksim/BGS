"""Wave 30, task 2: verify gamma constraints numerically on specific pairs."""
import json
from collections import defaultdict

QS = [128, 81, 25, 49, 121]

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

d = json.load(open('wave18_Pw_m12_census.json'))
failing = []
for gi, g in enumerate(d['split_groups']):
    orbs = g['orbits']
    for a in range(len(orbs)):
        for b in range(a+1, len(orbs)):
            if orbs[a]['sorted_w'] == orbs[b]['sorted_w']:
                failing.append((gi, orbs[a]['rep'], orbs[b]['rep']))

# group 14 is failing index? find pairs with group index 14
for gi, y, yp in failing:
    if gi == 14:
        break
print("group", gi)
print("y =", y)
print("yp=", yp)
gs = gamma_sets(y, yp)
for q in QS:
    print(f"Gamma_{q}:", [ek(pi) for pi in gs[q]])
taus = all_taus(y, yp)
cpis = [t for t in taus if is_cpi(t)]
print("n_taus", len(taus), "n_cpi", len(cpis), "cpi", cpis[0] if cpis else None)
tau = cpis[0]
# check constraints per q
for q in QS:
    v = [x % q for x in y]
    bad = []
    for j in range(12):
        for pi in gs[q]:
            if v[tau[j]] != v[pi[j]]:
                bad.append((j, ek(pi)))
                break
    print(f"q={q}: constraint violations (tau vs gamma): {len(bad)}", bad[:5])
    # component pattern
    per = None
    for p in (1, 2, 3, 4, 6, 12):
        if all(v[(i+p) % 12] == v[i] for i in range(12)):
            per = p; break
    print(f"   v mod {q} = {v}, period {per}")
print("tau mod 3:", [tau[j] % 3 for j in range(12)])
print("tau mod 4:", [tau[j] % 4 for j in range(12)])
