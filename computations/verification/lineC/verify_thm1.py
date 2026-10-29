"""Theorem 1 check: M_N = Delta F_{1/4} Delta exactly, and D_theta M_N is unitarily conjugate to
D_{theta'} F_DFT (F_DFT(x,y)=N^{-1/2}e_N(xy)) with theta'_x = theta_{2x} + phase of Delta^2 at 2x.
Checks matrix identity and eigenvalue equality for random theta; plus E|Tr|^2 equality (brute)."""
import os, sys, numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from model import MN
from brute import exact_E, Fc
rng = np.random.default_rng(20261029)
for N in (5, 7, 9, 11, 13, 15, 21, 101, 103):
    M = MN(N); x = np.arange(N)
    i8 = pow(8, -1, N)
    Delta = np.exp(2j*np.pi*((-3*i8*x*x) % N)/N)
    F4 = Fc(N, pow(4, -1, N))
    err1 = np.abs(M - Delta[:, None]*F4*Delta[None, :]).max()
    # P: (P f)(x) = f(2x) ; P^{-1} F_{1/4} P = F_1 ?
    i2 = pow(2, -1, N)
    P = np.zeros((N, N)); P[x, (2*x) % N] = 1
    err2 = np.abs(P @ F4 @ P.T - Fc(N, 1)).max()
    th = 2*np.pi*rng.random(N)
    U = np.exp(1j*th)[:, None]*M
    # D M = D Delta F4 Delta ~ (Delta D Delta) F4 ; then P^T (.) P = P^T G P P^T F4 P with G diagonal
    G = np.exp(1j*th)*Delta**2
    Gp = (P @ np.diag(G) @ P.T).diagonal()
    V = Gp[:, None]*Fc(N, 1)
    e1 = np.sort_complex(np.round(np.linalg.eigvals(U), 10)); e2 = np.sort_complex(np.round(np.linalg.eigvals(V), 10))
    err3 = np.abs(np.sort(np.angle(np.linalg.eigvals(U))) - np.sort(np.angle(np.linalg.eigvals(V)))).max()
    line = f'N={N:4d} |M-Delta F Delta|={err1:.1e}  |P F_(1/4) P^T - F_DFT|={err2:.1e}  max eigenphase diff={err3:.1e}'
    if N <= 13:
        line += f'  E|TrU^4|^2: M {exact_E(M,4):.12f}  F_DFT {exact_E(Fc(N,1),4):.12f}'
    print(line); sys.stdout.flush()
