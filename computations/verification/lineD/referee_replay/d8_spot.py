"""Exact (theta-quadrature, literal matrices) E_theta|Tr U^m|^2 at p=101, flat J0 kick a_k=1, eta=2, K=1,2 -> compare 100(E-E_LC) rows of the D8 table."""

if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import json, os, numpy as np, itertools, core
p, eta = 101, 2.0
# Repo-relative: computations/verification/lineD/logs/linec_exact_values.json
# (research-box path was /workspace/bgs-lineD/logs/linec_exact_values.json).
_ELC_PATH = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'logs', 'linec_exact_values.json'))
ELC = json.load(open(_ELC_PATH))   # Line C engine values (read-only)
M = core.Mp(p); x = np.arange(p)
for K, Q in [(1, 128), (2, 64), (2, 96)]:
    acc = np.zeros(8)
    grid = 2*np.pi*np.arange(Q)/Q
    for th in itertools.product(grid, repeat=K):
        V = sum(np.cos(2*np.pi*(k+1)*x/p + th[k]) for k in range(K))
        tr = core.trace_powers(np.exp(1j*eta*V)[:, None]*M, 7)
        for m in range(3, 8): acc[m] += abs(tr[m])**2
    acc /= Q**K
    print(f"K={K} Q={Q}: " + "  ".join(f"m={m}: E={acc[m]:.5f} 100(E-E_LC)={100*(acc[m]-ELC[f'{p},{m}']):+.1f}" for m in range(3, 8)), flush=True)
