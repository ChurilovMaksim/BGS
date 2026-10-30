"""Independent check of Proposition G (class-sum form) against the brute-force TRACE-163 Thm 1 n-sum (exact integer phases), k1 kick."""
import numpy as np, json
from lawlib import mdata
from check_trace import brute
from cmp_full import ghat_of, KICKS
import cert_class
for m, L in ((5, 9), (7, 4)):
    d = mdata(m); h = d['h']; G = ghat_of(KICKS['k1'], 2.0, L)
    for off in (4, -4, 17, 101):
        N = (-off) % h; nu = pow(N, -1, h); nu = nu + h if nu % 2 == 0 else nu
        zb = abs(brute(G, m, nu))**2
        rec = cert_class.run('k1', m, '2.0', [off], 2)
        zc = rec['residues'][0]['Z2_float']
        print(json.dumps(dict(m=m, L=L, N_mod_h=-off, nu=nu, Z2_nsum=zb, Z2_propG=zc, rel=abs(zb-zc)/zc)), flush=True)
