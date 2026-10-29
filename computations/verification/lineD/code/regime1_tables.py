"""Tables of the leading term Psi_m(s/D; K, eta) (fixed modes {1..K}, flat amplitudes a=1) over all residues s mod g'_m,
for the uniform-phase (J0) and circular-Gaussian (G) ensembles; eta -> infinity limits; Gamma-diagonal B^sym_m."""

if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import sys, numpy as np, math, time
from psi import *
m = int(sys.argv[1]); Ks = list(map(int, sys.argv[2].split(','))); etas = list(map(float, sys.argv[3].split(',')))
g, res = residues(m)
st = Setup(m, res[0][1])
ws = [class_weights(st, s) for r, s in res]
Bsym = st.gamma_diag()
out = [f"# m={m} D={st.D} D_eff={st.Deff} classes={len(st.w)} g'={g} residues(mod +-)={len(res)} B_sym={Bsym:.6f} 2m-B_sym={2*m-Bsym:.6f}"]
for K in Ks:
    pinf, ncl = psi_infinity(st, K, ws)
    out.append(f"m={m} K={K} eta=inf: #P_K-classes={ncl} (Gamma-classes {len(st.w)})  Psi_inf over s: min={min(pinf):.6f} mean={np.mean(pinf):.6f} max={max(pinf):.6f}")
    for ens in ('J0', 'G'):
        for eta in etas:
            Wm = kernel(st, list(range(1, K+1)), [1.0]*K, eta, ens)
            vals = np.array([np.real(np.conj(w) @ Wm @ w) for w in ws])
            out.append(f"m={m} K={K} {ens:2s} eta={eta:6.2f}: Psi min={vals.min():9.4f} mean={vals.mean():9.4f} max={vals.max():9.4f}  (mean-B_sym)={vals.mean()-Bsym:+.4f}")
open(f'../logs/regime1_tables_m{m}.log', 'w').write('\n'.join(out)+'\n')
