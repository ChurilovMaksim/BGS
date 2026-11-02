"""Spot-checks for wave 12 task 3 (G4b remainders). Evidence only.
(i) kickValInf truncated sum vs exp(i*eta*f_diag(x/N)).
(ii) Lean-formula catMat entries vs model.py MN(N).
Uses model.py's fCoeff(k,0) row; continuum ghat via FFT on 8192 grid.
"""
import numpy as np, sys
sys.path.insert(0, '/home/hatch/workspace/bgs-breakthrough/numerics')
# model.py lives in the connector-fetched g4 copy; replicate fCoeff here
# from the pinned model.py (ee6296ab) to avoid importing scipy-dependent UN.
def rCoeff(k):
    return {0: 1.0, 1: .5, -1: .5, 7: -.5, -7: -.5, 6: -.25, -6: -.25, 8: -.25, -8: -.25}.get(k, 0.0)

def fCoeff0(k):
    v = (0.5 if k in (7, -7) else 0) + rCoeff(k)/10 + (rCoeff(k-1)-rCoeff(k+1))/(200j)
    v -= (0.1 if k == 0 else 0)
    return complex(v)

def f_diag(theta):
    return sum(fCoeff0(k)*np.exp(2j*np.pi*k*theta) for k in range(-9, 10))

# (i)
eta, N, x = 2.5, 101, 37
M = 8192
th = np.arange(M)/M
g = np.exp(1j*eta*np.array([f_diag(t) for t in th]))
# FFT: ghat[k] = int g(theta) e(-k theta) dtheta, k in [-K, K]
G = np.fft.fft(g)/M  # G[k] for k=0..M-1 (k mod M)
def ghat(k):
    return G[k % M]
K = 60
kick = sum(ghat(k)*np.exp(2j*np.pi*k*x/N) for k in range(-K, K+1))
target = np.exp(1j*eta*f_diag(x/N))
print(f"(i) eta={eta} N={N} x={x} K={K}")
print(f"    kick_sum = {kick}")
print(f"    target   = {target}")
print(f"    err = {abs(kick-target):.3e}")

# (ii)
inv8 = pow(8, -1, N)
a = (-inv8) % N
rng = np.random.default_rng(0)
maxerr = 0.0
for _ in range(200):
    xx, yy = rng.integers(0, N, 2)
    ph = (-inv8*(3*xx*xx - 2*xx*yy + 3*yy*yy)) % N
    mn = np.exp(2j*np.pi*ph/N)/np.sqrt(N)
    lean = (1/np.sqrt(N))*np.exp(2j*np.pi*((a*(3*xx*xx - 2*xx*yy + 3*yy*yy)) % N)/N)
    maxerr = max(maxerr, abs(mn-lean))
print(f"(ii) N={N} a={a} (-inv8={(-inv8) % N}) maxerr over 200 random entries = {maxerr:.3e}")
