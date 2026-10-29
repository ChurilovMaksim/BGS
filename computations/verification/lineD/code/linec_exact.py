"""Exact maximal-ensemble (Line C, Prop. 2) values E|Tr U^m|^2 at prime p.

Imports eval_p from the in-repo Line C verifier
computations/verification/lineC/gauss_exact.py (two directories up from this
script, then lineC). Run from this directory:
python linec_exact.py 7 101 211 401
"""

if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import sys, json, time, os
_LINEC = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'lineC'))
if not os.path.isfile(os.path.join(_LINEC, 'gauss_exact.py')):
    raise SystemExit('Line C verifier not found at ' + _LINEC)
sys.path.insert(0, _LINEC)
from gauss_exact import eval_p
out = {}
for p in map(int, sys.argv[2:]):
    for m in range(1, int(sys.argv[1])+1):
        t = time.time(); v = eval_p(m, p); out[f'{p},{m}'] = complex(v).real
        print(p, m, complex(v), f'{time.time()-t:.1f}s', flush=True)
_LOG = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'logs', 'linec_exact_values.json'))
json.dump(out, open(_LOG, 'w'), indent=1)
