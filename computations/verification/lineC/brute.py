"""Exact E_theta |Tr (D_theta M)^m|^2 for i.i.d. uniform position phases theta_x (x in Z/N),
by brute force: E = sum_n |c_n|^2, c_n = sum_{x: occupation(x)=n} K(x), K(x)=prod_j M[x_j,x_{j+1}] (cyclic).
Uses the literal repository M_N (bgs-recon/code/model.py) or the reduced Fourier kernel F_c."""
import os, sys, itertools, numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from model import MN

def Fc(N, c):
    x = np.arange(N)[:, None]; y = np.arange(N)[None, :]
    return np.exp(2j*np.pi*((c*x*y) % N)/N)/np.sqrt(N)

def exact_E(M, m):
    N = M.shape[0]
    # enumerate x in Z_N^m in chunks: first coordinate loop
    acc = {}
    grids = np.array(list(itertools.product(range(N), repeat=m-1)), dtype=np.int64) if m > 1 else np.zeros((1, 0), np.int64)
    tot = None
    keys_all = []; vals_all = []
    for x0 in range(N):
        X = np.concatenate([np.full((grids.shape[0], 1), x0), grids], axis=1)
        K = np.ones(X.shape[0], complex)
        for j in range(m):
            K *= M[X[:, j], X[:, (j+1) % m]]
        Xs = np.sort(X, axis=1)
        # encode multiset as integer
        code = np.zeros(X.shape[0], dtype=np.int64)
        for j in range(m): code = code*N + Xs[:, j]
        keys_all.append(code); vals_all.append(K)
    code = np.concatenate(keys_all); K = np.concatenate(vals_all)
    u, inv = np.unique(code, return_inverse=True)
    c = np.zeros(len(u), complex)
    np.add.at(c, inv, K)
    return float(np.sum(np.abs(c)**2))

if __name__ == '__main__':
    for N, m in [(7, 3), (7, 4), (11, 3), (11, 4), (13, 5), (11, 6)]:
        M = MN(N)
        e1 = exact_E(M, m)
        e2 = exact_E(Fc(N, pow(4, -1, N)), m)
        print(N, m, e1, e2, abs(e1-e2))
