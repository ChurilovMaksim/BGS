"""Wave 10, task 3 — numeric check for G4b (NOT a proof).

Compares tuple class sums A_r^tup = sum_{n : yp*NmZ(n) == r (mod gp)} prod_j ghat_eta(n_j)
(truncated to |n_j| <= K, ghat_eta = continuum Fourier coeffs of exp(i*eta*f_diag)
via FFT on 16384 points) against dlib's exact finite orbit class sums A_r^dlib.

dlib is imported from ../g4/phase1/dlib.py, a connector download from main at
HEAD d87dce0d9277579568edfee6cffecbc96ea61024 (blob af79ab79...), NOT a repo edit.
f_diag uses only the l=0 row of the fixed symbol, as in dlib.

Usage: python3 wave10_task3_G4_check.py [m] [eta] [K]
Defaults: m=3, eta=1.0, K=32. Bandwidth scales ~7.1*eta, so large eta needs large K.
"""
import sys, math
sys.path.insert(0, '../g4/phase1')
import numpy as np
from dlib import Orbits, f_diag


def pell(m):
    xs, ys = [1], [0]
    for _ in range(m):
        x, y = xs[-1], ys[-1]
        xs.append(3 * x + 8 * y)
        ys.append(x + 3 * y)
    return xs, ys


def class_sums_tup(m, eta, K, L=16384):
    th = np.arange(L) / L
    g = np.exp(1j * eta * f_diag(th))
    c = np.fft.fft(g) / L
    freq = np.fft.fftfreq(L, 1 / L).astype(int)
    ghatd = np.zeros(2 * K + 1, dtype=complex)
    for i, fr in enumerate(freq):
        if -K <= fr <= K:
            ghatd[fr + K] = c[i]
    xs, ys = pell(m)
    g_ = math.gcd(xs[m] - 1, ys[m])
    gp = (xs[m] - 1) // g_
    yp = ys[m] // g_
    rng = np.arange(-K, K + 1)
    grids = np.meshgrid(*([rng] * m), indexing='ij')
    ns = [gr.ravel() for gr in grids]
    w = np.ones(ns[0].shape, dtype=complex)
    for nj in ns:
        w *= ghatd[nj + K]
    Nm = np.zeros(ns[0].shape, dtype=np.int64)
    for i in range(m):
        for j in range(m):
            Nm += ns[i] * ns[j] * xs[abs(i - j)]
    r = (yp * Nm) % gp
    return (np.bincount(r, weights=w.real, minlength=gp)
            + 1j * np.bincount(r, weights=w.imag, minlength=gp)), gp


def main():
    m = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    eta = float(sys.argv[2]) if len(sys.argv) > 2 else 1.0
    K = int(sys.argv[3]) if len(sys.argv) > 3 else 32
    O = Orbits(m)
    mu = np.fft.fft2(O.Phi(eta)) / O.D
    A_dlib = (np.bincount(O.cls.ravel(), weights=mu.real.ravel(), minlength=O.gp)
              + 1j * np.bincount(O.cls.ravel(), weights=mu.imag.ravel(), minlength=O.gp))
    A_tup, gp = class_sums_tup(m, eta, K)
    assert gp == O.gp
    print(f"m={m} eta={eta} K={K} gp={gp} D={O.D}")
    print(f"max|A_tup - A_dlib| = {np.max(np.abs(A_tup - A_dlib)):.6f}")
    Z_tup = np.fft.fft(A_tup)
    Z_dlib = O.Z_all(eta)
    print(f"max|Z_tup - Z_all| = {np.max(np.abs(Z_tup - Z_dlib)):.6f}")


if __name__ == '__main__':
    main()
