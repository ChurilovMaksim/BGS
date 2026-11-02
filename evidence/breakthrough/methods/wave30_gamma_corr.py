"""Wave 30, task 2: correlations between Gamma_q data and tau structure."""
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

    # 1. Type I: c (mod-3 reflection constant) vs Gamma_49 k mod 3, Gamma_25, Gamma_128
    corr = Counter()
    typeII_info = []
    for gi, y, yp in failing:
        taus = all_taus(y, yp)
        cpis = [t for t in taus if is_cpi(t)]
        gs = gamma_sets(y, yp)
        g49 = sorted(ek(pi) for pi in gs[49])
        g25 = sorted(ek(pi) for pi in gs[25])
        g128 = sorted(ek(pi) for pi in gs[128])
        # Gamma_49 k mod 3 set
        k49 = sorted(set(k % 3 for (eps, k) in g49))
        eps49 = sorted(set(eps for (eps, k) in g49))
        # Gamma_25: rotation k's mod 6 and reflection k's mod 6
        rot25 = sorted(set(k % 6 for (eps, k) in g25 if eps == 1))
        ref25 = sorted(set(k % 6 for (eps, k) in g25 if eps == -1))
        # v_128 period
        v128 = [x % 128 for x in y]
        per128 = 1 if len(set(v128)) == 1 else (2 if all(v128[(i+2) % 12] == v128[i] for i in range(12)) else 12)
        if cpis:
            tau = cpis[0]
            # c: tau(j) mod 3 = -j + c mod 3
            c = (tau[0] % 3 + 0) % 3  # j=0: tau(0)%3 = c
            assert all((tau[j] % 3) == (-j + c) % 3 for j in range(12)), (gi, tau)
            corr[('I', c, tuple(k49), tuple(eps49), tuple(rot25), tuple(ref25), per128)] += 1
        else:
            # Type II: record class action and mod-3 action of every tau
            acts = set()
            for t in taus:
                cm = tuple(tuple(sorted(set(t[j] % 4 for j in [r, r+4, r+8]))) for r in range(4))
                m3 = tuple(t[j] % 3 for j in range(12))
                acts.add((cm, m3))
            typeII_info.append((gi, tuple(k49), tuple(eps49), tuple(rot25), tuple(ref25), per128, acts))
    print("Type I correlations (c, k49mod3, eps49, rot25mod6, ref25mod6, per128): count")
    for k, n in sorted(corr.items()):
        print("   ", k, n)
    print()
    print("Type II pairs:")
    for gi, k49, eps49, rot25, ref25, per128, acts in typeII_info:
        print(f"  group {gi}: k49={k49} eps49={eps49} rot25={rot25} ref25={ref25} per128={per128}")
        for cm, m3 in sorted(acts)[:3]:
            print(f"      class images: {cm}, tau mod 3: {m3}")

if __name__ == '__main__':
    main()
