"""Wave 26, task 4: quantitative G4c gap at concrete N.

Builds A_N exactly per TraceStatement/model.py (weylT, fCoeff) at N=101
(odd, near the wave-21 reference scale N~100), and measures:
  * ||A||, ||A_off|| (l=+-1 band), max/RMS off-diagonal entry
  * ||D_eta - I|| for eta=1 (diagonal-model gap at feasible N)
  * matched-regime eta=tau*N relative error ||A_off||/||A||
  * theta=1 regime: best diagonal approximation to exp(i A)
  * dlib profile F_m(eta) at m=3: F(0) vs F(1) (average-level gap)
Repository untouched; no Lean build.
"""
import sys, math
import numpy as np
sys.path.insert(0, '/home/hatch/workspace/bgs-breakthrough/g4/common')
sys.path.insert(0, '/home/hatch/workspace/bgs-breakthrough/g4/phase1')
from model import AN, fCoeff, weylT

N = 101
A = AN(N)
print(f"N = {N}")
print(f"Hermitian check  ||A - A^H|| = {np.linalg.norm(A - A.conj().T):.3e}")

# diagonal = f_diag(x/N) exactly? check against direct trig sum
xs = np.arange(N)
fdir = np.array([sum(fCoeff(k, 0) * np.exp(2j * np.pi * k * x / N)
                     for k in range(-9, 10)) for x in xs])
print(f"diag(A) real, max|imag| = {np.abs(np.diag(A).imag).max():.3e}")
print(f"diag(A) vs f_diag(x/N), max diff = "
      f"{np.abs(np.diag(A) - fdir).max():.3e}")
f = np.diag(A).real
print(f"f_diag range on grid: [{f.min():.6f}, {f.max():.6f}]")

nA = np.linalg.norm(A, 2)
Aoff = A - np.diag(np.diag(A))
nAoff = np.linalg.norm(Aoff, 2)
off = np.abs(Aoff)
mask = np.ones((N, N), bool); np.fill_diagonal(mask, False)
print(f"||A|| = {nA:.6f}  (bound sum|c_kl| = "
      f"{sum(abs(fCoeff(k, l)) for k in range(-9, 10) for l in (-1, 0, 1)):.6f})")
print(f"||A_off|| = {nAoff:.6f}   ||A_off||/||A|| = {nAoff / nA:.6f}")
nz = off[off > 1e-12]
print(f"max off-diag |entry| = {off[mask].max():.6f}   "
      f"band RMS (nonzero entries) = {np.sqrt((nz ** 2).mean()):.6f}")

# diagonal model gap at eta = O(1)
D1 = np.diag(np.exp(1j * f))
gap1 = np.linalg.norm(D1 - np.eye(N), 2)
print(f"||D_1 - I|| = {gap1:.6f}   (= 2 max|sin(f/2)| = "
      f"{2 * np.abs(np.sin(f / 2)).max():.6f})")

# feasible-N regime: theta = tau*N
theta = N * 1e-80
print(f"theta = tau*N = {theta:.3e};  theta*||A|| = {theta * nA:.3e}")
print(f"||exp(i theta A) - D_1|| = ||D_1 - I|| +- theta*||A|| "
      f"= {gap1:.6f} +- {theta * nA:.3e}")
print(f"matched eta=theta: ||exp - D_theta|| ~ theta*||A_off|| = "
      f"{theta * nAoff:.3e};  ||exp - I|| ~ theta*||A|| = {theta * nA:.3e};"
      f"  relative err = {nAoff / nA:.4f}")
print(f"entrywise lower bound, ANY diagonal D: ||exp(i theta A) - D|| >= "
      f"theta*max|A_jk| - theta^2||A||^2/2 = {theta * off[mask].max():.3e}")

# theta = 1 regime (N ~ 1/tau): best diagonal approximation to exp(iA)
w, V = np.linalg.eigh(A)
U = (V * np.exp(1j * w)) @ V.conj().T
Uoff = U - np.diag(np.diag(U))
print(f"theta=1: max off-diag |U_jk| = {np.abs(Uoff[mask]).max():.6f};"
      f"  ||U - diag(U)|| = {np.linalg.norm(Uoff, 2):.6f}")
best = (1e9, None)
for eta in np.arange(0, 6.30, 0.02):
    d = np.linalg.norm(U - np.diag(np.exp(1j * eta * f)), 2)
    if d < best[0]:
        best = (d, eta)
print(f"theta=1: min_eta ||U - D_eta|| = {best[0]:.6f} at eta = {best[1]:.2f};"
      f"  ||U - D_1|| = {np.linalg.norm(U - D1, 2):.6f}")

# average-level gap: dlib profile F_m(eta) at m=3
from dlib import Orbits
O3 = Orbits(3)
for eta in (0.0, 0.5, 1.0):
    Fv, _ = O3.F(eta)
    print(f"dlib m=3: F({eta}) = {Fv:.6f}")
