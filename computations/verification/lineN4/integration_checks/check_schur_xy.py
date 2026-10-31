#!/usr/bin/env python3
"""N4-F8 check: the integration reruns (b16_schur_xy.py) reproduce the author's Schur certificates exactly and D = diag(sqrt(x/y))
(normalised to max 1) is recomputed from the stored float vectors x, y; it equals the stored d bit for bit.
||R|| = 1/min d, (1 + 1e-12) slack as in b16_final.py / b8E_final.py."""
import json, os, numpy as np
H = os.path.dirname(os.path.abspath(__file__)); A = os.path.join(H, '..', 'logs'); I = os.path.join(H, 'logs')
ok = True
for n in ['b16_schur_V_P0', 'b16_schur_V_P1', 'b16_schur_E_P0', 'b16_schur_E_P1', 'b8_schur_E', 'b8_schur_V']:
    a = json.load(open(os.path.join(A, n + '.json'))); b = json.load(open(os.path.join(I, n + '.json')))
    same = all(a[k] == b[k] for k in ('alpha', 'beta', 'f_core', 'dim', 'blocks', 'condD'))
    da = np.load(os.path.join(A, n + '_d.npy')); db = np.load(os.path.join(I, n + '_d.npy'))
    x = np.load(os.path.join(I, n + '_x.npy')); y = np.load(os.path.join(I, n + '_y.npy'))
    d = np.sqrt(x / y); d /= d.max()
    r = dict(run=n, cert_fields_identical=same, d_identical_to_author=bool(np.array_equal(da, db)),
             d_equals_sqrt_x_over_y=bool(np.array_equal(d, db)), x_pos=bool((x > 0).all()), y_pos=bool((y > 0).all()),
             f_core=b['f_core'], normR_bound=float(1 / db.min()) * (1 + 1e-12))
    ok &= all(v for k, v in r.items() if isinstance(v, bool))
    print(json.dumps(r))
print('SCHUR_XY_OK' if ok else 'SCHUR_XY_FAIL'); raise SystemExit(0 if ok else 1)
