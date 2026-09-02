"""RUN 107 -- Rank-2 coset trace fluctuation Tr(P H Q P) over the full
q-grid (vectorized) at N=53.  This is the rank-2 analogue of the
cat-map S_off(q) fluctuation for the Sp4 Hecke kernel H = omega(w)
U(t) U_D restricted to the D-fixed coset.

The coset trace Tr(P H Q P) = Tr(Q P H P) = sum_x Q(x,x) (P H P)(x,x)
-- i.e. the Fourier transform over q of the diagonal of P H P.  The
diagonal of P H P is a small vector (size N^2); the trace is simply
its q-weighted sum.  This is a single matrix-vector product per q.

Output: artifacts/r107/rank2_coset_trace.json
"""

import numpy as np
import math
import os
import json
import time

N = 53
G = N * N
u1, u2 = 5, 3
iu1, iu2 = pow(u1, -1, N), pow(u2, -1, N)
b2 = pow(2, -1, N)
OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "..", "..", "artifacts", "r107")
os.makedirs(OUT_DIR, exist_ok=True)


def build_all():
    # Dilation
    Ud = np.zeros((G, G), dtype=complex)
    for x1 in range(N):
        for x2 in range(N):
            Ud[(iu1 * x1) % N * N + (iu2 * x2) % N, x1 * N + x2] = 1.0
    # Fourier
    W = np.zeros((G, G), dtype=complex)
    for x1 in range(N):
        for x2 in range(N):
            for y1 in range(N):
                for y2 in range(N):
                    W[x1 * N + x2, y1 * N + y2] = np.exp(
                        2j * np.pi * ((x1 * y1 + x2 * y2) % N) / N) / N
    # Unipotent with quadratic phase
    Ut = np.zeros((G, G), dtype=complex)
    for x1 in range(N):
        for x2 in range(N):
            Q = (b2 * (x1 * x1 + x2 * x2)) % N
            Ut[x1 * N + x2, x1 * N + x2] = np.exp(2j * np.pi * Q / N)
    # Hyperbolic
    H = W @ Ut @ Ud
    # Coset projector
    kcoset = [0, 13, 26, 39]
    lcoset = [0, 26]
    P = np.zeros((G, G), dtype=complex)
    for k in kcoset:
        for l in lcoset:
            for x1 in range(N):
                for x2 in range(N):
                    for x1p in range(N):
                        for x2p in range(N):
                            P[x1 * N + x2, x1p * N + x2p] += (
                                np.exp(2j * np.pi * (k * (x1 - x1p) +
                                                     l * (x2 - x2p)) / N)
                                / (N - 1))
    return H, P


def main():
    t0 = time.time()
    print("building H, P ...")
    H, P = build_all()
    print(f"built t={time.time()-t0:.0f}s")
    # P H P
    PHP = P @ H @ P
    # diagonal of PHP (the quantity that determines all coset traces)
    diag = np.diag(PHP)
    print(f"||diag(PHP)|| = {np.linalg.norm(diag):.4f}")
    # The coset trace Tr(P H Q P) = sum_i Q(i,i) diag[i]
    # = the inner product of diag with the q-phase vector
    # Build the q-phase vectors and measure the distribution
    q_list = [(q1, q2) for q1 in range(1, N) for q2 in range(1, N)]
    traces = []
    x1, x2 = np.meshgrid(np.arange(N), np.arange(N), indexing='ij')
    x1f = x1.flatten()
    x2f = x2.flatten()
    for q1, q2 in q_list:
        Qp = np.exp(2j * np.pi * ((q1 * x1f + q2 * x2f) % N) / N)
        t_val = complex(np.sum(Qp * diag))
        traces.append(t_val)
    ct = np.array(traces)
    mean = ct.mean()
    std = ct.std()
    print(f"Tr(PHQP) over full q-grid ({len(ct)} pts): "
          f"mean={mean:.4f} std={std:.4f}")
    print(f"  max={ct.max():.4f} min={ct.min():.4f}")
    print(f"  Var={std**2:.4f}")
    print(f"|coset| = 8, G = {G}, |coset|/G = {8/G:.4f}")
    # The rank-2 analogue of the cat-map structure: is the mean nonzero
    # (the flat part) with a fluctuation around it?
    print(f"\nRank-2 structure: mean (flat part) = {mean:.4f}")
    print(f"                   fluctuation (std) = {std:.4f}")
    print(f"                   rel = {std/abs(mean) if abs(mean)>1e-9 else 'N/A'}")

    out = {
        "run": "107",
        "design": {"N": N, "u1": u1, "u2": u2, "coset_size": 8},
        "n_q": len(ct),
        "mean_trace": float(mean),
        "std_trace": float(std),
        "var": float(std ** 2),
        "max_trace": float(ct.max()),
        "min_trace": float(ct.min()),
        "wall_s": time.time() - t0,
    }
    out_path = os.path.join(OUT_DIR, "rank2_coset_trace.json")
    with open(out_path, "w") as fh:
        json.dump(out, fh, indent=1)
    print(f"artifact written -> {out_path}")
    print(f"wall = {time.time()-t0:.0f}s")


if __name__ == "__main__":
    main()
