"""Markdown version of analyze_fast.py output (D8 table)."""

if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import numpy as np, glob, re
from analyze_scan import coe_exact, LC
rows = []
for f in glob.glob('../logs/mc/flat_p101_*.npy') + glob.glob('../logs/mcfast/flat_p211_*seed21.npy') + glob.glob('../logs/mcfast/flat_p401_*seed41.npy'):
    mean, se = np.load(f); p = int(re.search(r'_p(\d+)_', f)[1]); K = int(re.search(r'_K(\d+)_', f)[1])
    R = np.pi*2.0*np.sqrt(sum(k*k for k in range(1, K+1)))/p
    chi = np.mean([((mean[m-1]-coe_exact(p, m))/se[m-1])**2 for m in range(3, 9)])
    dev = ' | '.join(f'{100*(mean[m-1]-LC[f"{p},{m}"]):+.0f}±{100*se[m-1]:.0f}' for m in range(3, 8))
    rows.append((R, f'| {p} | {K} | {R:.2f} | {chi:.1f} | {dev} |'))
print('| p | K | R | χ²/dof vs COE (m=3..8) | 100(E−E_LC) m=3 | m=4 | m=5 | m=6 | m=7 |'); print('|---|---|---|---|---|---|---|---|---|')
for R, r in sorted(rows): print(r)
