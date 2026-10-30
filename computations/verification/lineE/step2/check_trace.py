"""Brute-force Line B n-sum (exact integer phases) vs the vector-valued transfer-operator law, random finite-support weights."""
import numpy as np, itertools, sys
from lawlib import *
from tm49 import Z_TO
rng = np.random.default_rng(7)
def brute(ghat, m, nu):
    d = mdata(m); gp, yp = d['gp'], d['yp']
    vals = np.array(sorted(ghat)); g = np.array([ghat[v] for v in vals])
    X = np.array([[pell(abs(i-j))[0] for j in range(m)] for i in range(m)], dtype=np.int64)
    idx = np.array(list(itertools.product(range(len(vals)), repeat=m)), dtype=np.int64); nv = vals[idx]
    Nm = np.einsum('ki,ij,kj->k', nv, X, nv) % gp
    ph = ((-nu*yp % gp)*Nm) % gp
    return np.sum(np.prod(g[idx], axis=1)*np.exp(2j*np.pi*ph/gp))
if __name__ == "__main__":
  for (m, L) in ((5, 3), (7, 2), (5, 4)):
      ghat = {n: complex(rng.normal(), rng.normal())*0.5**abs(n) for n in range(-L, L+1)}
      for a in (1, 7):
          for s in (+1, -1):
              nu = nu_res(m, a, s); zb = brute(ghat, m, nu)
              zt = Z_TO(ghat, m, a, s, rho=max(1.0, 1.3*(L/a)/(LAM-1)), K=40 if a > 1 else 60)
              print(f'm={m} L={L} a={a} s={s:+d} nu={nu}: brute={zb:.10f}  TO={zt:.10f}  |diff|/|brute|={abs(zb-zt)/abs(zb):.2e}', flush=True)
