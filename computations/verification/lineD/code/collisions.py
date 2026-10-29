"""K=1 collisions (S_1(xi) = S_1(xi') for xi' not in Gamma xi) inside the support, m = 4, 6, 8: list groups, verify with 60-digit
arithmetic, and identify the mechanism."""

if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import sys, numpy as np, mpmath as mp
from psi import *
mp.mp.dps = 60
out = []
for m in map(int, sys.argv[1:]):
    g, res = residues(m); st = Setup(m, res[0][1]); d2 = st.o.d2
    S1 = st.Sk(1)
    R = np.round(np.stack([S1.real, S1.imag], 1)/1e-9).astype(np.int64)
    _, inv, cnt = np.unique(R, axis=0, return_inverse=True, return_counts=True); inv = inv.reshape(-1)
    groups = [np.flatnonzero(inv == c) for c in np.flatnonzero(cnt > 1)]
    out.append(f"m={m}: {len(groups)} collision groups among {len(st.w)} Gamma-classes in the support (d2={d2})")
    maxdiff = 0; mind = np.inf
    for G in groups:
        vals = [mp.fsum(mp.expjpi(2*mp.mpf(int(x))/d2) for x in st.rep[i]) for i in G]
        maxdiff = max(maxdiff, max(abs(v - vals[0]) for v in vals))
    # smallest nonzero distance for comparison
    o = np.argsort(S1.real)
    for sh in range(1, 30):
        d = np.abs(S1[o[sh:]] - S1[o[:-sh]]); d = d[d > 1e-6]
        if len(d): mind = min(mind, d.min())
    out.append(f"  max |S_1 diff| inside groups (60 digits) = {mp.nstr(maxdiff, 3)};  smallest nonzero |Delta S_1| = {mind:.3e}")
    for G in groups[:5]:
        out.append(f"  group S_1={complex(S1[G[0]]):.6f}: " + '; '.join(f"{(st.rep[i]).tolist()}/{d2} (|O|={st.size[i]})" for i in G))
print('\n'.join(out)); open('../logs/collisions.log', 'w').write('\n'.join(out)+'\n')
