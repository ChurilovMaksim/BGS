"""R-collapse test: for flat ensembles at p=101 (logs/mc) and p=211/401 (logs/mcfast) print
R = pi*eta*a*sqrt(sum_{k<=K} k^2)/p, the deviation p*(E_m - E_LineC(p,m)) +- p*se, and chi2/dof vs finite-N COE over m=3..8."""

if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import numpy as np, json, glob, re
from analyze_scan import coe_exact, LC
rows = []
for f in glob.glob('../logs/mc/flat_p101_*.npy') + glob.glob('../logs/mcfast/flat_p*_seed2*.npy') + glob.glob('../logs/mcfast/flat_p*_seed41.npy'):
    mean, se = np.load(f)
    p = int(re.search(r'_p(\d+)_', f).group(1)); K = int(re.search(r'_K(\d+)_', f).group(1))
    eta = float(re.search(r'_eta([\d.]+)_', f).group(1)); a = float(re.search(r'_a([\d.]+)_', f).group(1))
    R = np.pi*eta*a*np.sqrt(sum(k*k for k in range(1, K+1)))/p
    z = [(mean[m-1]-coe_exact(p, m))/se[m-1] for m in range(3, 9)]
    dev = ' '.join(f'{p*(mean[m-1]-LC[f"{p},{m}"]):+7.1f}({p*se[m-1]:4.1f})' for m in range(3, 8))
    rows.append((p, R, f'p={p:4d} K={K:3d} R={R:5.2f}  chi2/dof(COE,m=3..8)={np.mean(np.square(z)):8.2f} | p*(E-E_LC) m=3..7: {dev}'))
for p, R, s in sorted(rows): print(s)
