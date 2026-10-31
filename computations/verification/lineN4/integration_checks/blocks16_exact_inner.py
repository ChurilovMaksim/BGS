#!/usr/bin/env python3
"""N4-F5 (integration): exact Z[zeta16] check of the (f1, f2) bases of the 128 (+-2,16) blocks (16 cases x 8 blocks) used by b16_schur.py.
Data: computations/verification/lineJ/J3/logs/blocks16_exact.json (entries zeta16^e on a support). Exact arithmetic in Z[z]/(z^8 + 1)
(basis 1, z, ..., z^7). Checks for every block: <f1, f2> = sum_s f1_s conj(f2_s) = 0 exactly; |f1|^2 = |f2|^2 (support sizes, entries unimodular);
support pattern (disjoint or identical); the permutation pattern of the 2x2 action is swap^(n + PAR) with PAR in {0, 1};
counts: 64 + 64 blocks per pattern, 16 distinct actions."""
import json, os
H = os.path.dirname(os.path.abspath(__file__))
J = json.load(open(os.path.join(H, '..', '..', 'lineJ', 'J3', 'logs', 'blocks16_exact.json')))
def zpow(e):
    e %= 16; v = [0] * 8; v[e % 8] = 1 if e < 8 else -1; return v
def zadd(u, v): return [a + b for a, b in zip(u, v)]
nblk = 0; ok = True; supp = {'disjoint': 0, 'identical': 0, 'other': 0}; par = {0: 0, 1: 0}; acts = set(); norms = set()
for case, v in J['cases'].items():
    for b in v['blocks']:
        nblk += 1
        f1 = {int(k): e for k, e in b['f1'].items()}; f2 = {int(k): e for k, e in b['f2'].items()}
        ip = [0] * 8
        for s in set(f1) & set(f2): ip = zadd(ip, zpow(f1[s] - f2[s]))   # zeta^a * conj(zeta^b) = zeta^(a-b)
        if any(ip): ok = False; print('nonzero inner product', case, ip)
        if len(f1) != len(f2): ok = False; print('norm mismatch', case)
        norms.add(len(f1))
        S1, S2 = set(f1), set(f2)
        supp['disjoint' if not (S1 & S2) else ('identical' if S1 == S2 else 'other')] += 1
        perms = tuple(tuple(b['act'][str(r)]['perm']) for r in range(16))
        q = [Q for Q in (0, 1) if perms == tuple(((0, 1) if (r + Q) % 2 == 0 else (1, 0)) for r in range(16))]
        if len(q) != 1: ok = False; print('pattern', case, perms)
        else: par[q[0]] += 1
        acts.add(json.dumps(b['act'], sort_keys=True))
print(dict(blocks=nblk, inner_products_zero=ok, norms=sorted(norms), supports=supp, parity_counts=par, distinct_actions=len(acts)))
ok &= nblk == 128 and supp['other'] == 0 and par == {0: 64, 1: 64}
print('BLOCKS16_EXACT_OK' if ok else 'BLOCKS16_EXACT_FAIL'); raise SystemExit(0 if ok else 1)
