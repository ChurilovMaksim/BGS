"""COE reference: exact finite-N E|Tr U^n|^2 (Haake, Quantum Signatures of Chaos, ch.4) and a
Monte-Carlo check of that formula (U = V^T V, V Haar on U(N), deterministic seed)."""
import numpy as np, sys
def coe_exact(N, n):
    if n == 0: return N*N
    if n <= N: return 2*n - n*sum(1/(m + (N-1)/2) for m in range(1, n+1))
    return 2*N - n*sum(1/(m + (N-1)/2) for m in range(n-N+1, n+1))
def haar(N, rng):
    Z = (rng.standard_normal((N, N)) + 1j*rng.standard_normal((N, N)))/np.sqrt(2)
    Q, R = np.linalg.qr(Z); d = np.diag(R); return Q*(d/abs(d))
if __name__ == '__main__':
    rng = np.random.default_rng(20261029)
    for N in (3, 5, 8):
        S = 100000; acc = np.zeros(2*N+3)
        for _ in range(S):
            V = haar(N, rng); ev = np.linalg.eigvals(V.T@V)
            acc += np.abs(np.array([np.sum(ev**n) for n in range(1, 2*N+4)]))**2
        acc /= S
        for n in range(1, 2*N+4):
            print(N, n, f'MC {acc[n-1]:.4f}  exact {coe_exact(N, n):.4f}')
