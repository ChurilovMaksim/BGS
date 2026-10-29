"""Compare band-limited MC with (a) finite-N COE over m=3..2p and (b) Line C exact values (m=3..7)."""

if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import numpy as np, json, glob, sys, re
def coe_exact(N, n):   # copied from /workspace/bgs-lineC/code/coe.py (Haake)
    if n == 0: return N*N
    if n <= N: return 2*n - n*sum(1/(m + (N-1)/2) for m in range(1, n+1))
    return 2*N - n*sum(1/(m + (N-1)/2) for m in range(n-N+1, n+1))
LC = json.load(open('../logs/linec_exact_values.json'))
def main():
  rows = []
  for f in sorted(glob.glob(f'../logs/mc/{sys.argv[1]}*.npy'), key=lambda s: (int(re.search(r'_K(\d+)_', s).group(1)) if re.search(r'_K(\d+)_', s) else 0)):
      mean, se = np.load(f); p = int(re.search(r'_p(\d+)_', f).group(1)); tag = f.split('/')[-1][:-4]
      ms = np.arange(3, 2*p+1)
      z = np.array([(mean[m-1]-coe_exact(p, m))/se[m-1] for m in ms])
      blocks = [(3, 25), (26, 50), (51, 100), (101, 2*p)]
      bl = ' '.join(f'{np.mean(z[(ms>=a)&(ms<=b)]**2):8.1f}' for a, b in blocks)
      zl = [(mean[m-1]-LC[f'{p},{m}'])/se[m-1] for m in range(3, 8)]
      rows.append(f'{tag:45s} chi2/dof(COE,m=3..2p)={np.mean(z*z):9.2f}  blocks[3-25,26-50,51-100,101-2p]: {bl} | z vs LineC exact m=3..7: ' + ' '.join(f'{v:+6.1f}' for v in zl) + ' | m=3..7 values: ' + ' '.join(f'{mean[m-1]:.3f}' for m in range(3, 8)))
  print('\n'.join(rows))

if __name__ == '__main__': main()
