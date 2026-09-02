"""
AUDIT GPU REPLICATION - independent key for the paper's perturbation
experiments (Exp multi + eps sweep), torch/cuSOLVER backend.

Pipeline re-implemented from the paper's Appendix A.3 description only:
  (i)   diagonalise U_A, cluster eigenvalues at tol 1e-4;
  (ii)  draw E ~ GUE(N) (E=(X+X^dag)/2, X complex iid);
  (iii) U_eps = expm(i eps E) U_A via eigendecomposition of E;
  (iv)  match levels by Hungarian assignment on |lambda_new - lambda_old|;
  (v)   three largest clusters -> unfold gaps -> pooled KS per prime.
"""
import os as _os
_BGS_ROOT = _os.path.dirname(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))
import json
import numpy as np
import torch
from scipy.optimize import linear_sum_assignment
from scipy.stats import kstest

DEV = "cuda"
A = (2, 1, 1, 1)


def U_cat(Amat, N, dev):
    a, b, c, d = Amat
    icb = pow((2 * c) % N, -1, N)
    xs = torch.arange(N, dtype=torch.float64, device=dev)
    X, Y = torch.meshgrid(xs, xs, indexing="ij")
    Q = (icb * (d * X * X - 2 * X * Y + a * Y * Y)) % N
    w = torch.exp(2j * np.pi / N * torch.ones(1, device=dev)).item()
    return w**Q / np.sqrt(N)


def gue(N, gen, dev):
    X = torch.complex(torch.randn(N, N, generator=gen, device=dev, dtype=torch.float64),
                      torch.randn(N, N, generator=gen, device=dev, dtype=torch.float64))
    return (X + X.conj().T) / 2


def run_prime(p, eps=1e-4, seed=None, topk=3):
    gen = None
    if seed is not None:
        gen = torch.Generator(device=DEV).manual_seed(seed)
    U = U_cat(A, p, DEV)
    w0 = torch.linalg.eigvals(U).cpu().numpy()
    del U
    E = gue(p, gen, DEV)
    ev, V = torch.linalg.eigh(E)
    Ue = ((V * torch.exp(1j * eps * ev)) @ V.conj().T)
    del E, ev, V
    A2 = U_cat(A, p, DEV)
    Ue = Ue @ A2
    del A2
    wp = torch.linalg.eigvals(Ue).cpu().numpy()
    del Ue
    torch.cuda.empty_cache()

    Cm = np.abs(wp[:, None] - w0[None, :])
    ri, ci = linear_sum_assignment(Cm)
    splits = {}
    for i, j in zip(ri, ci):
        key = (round(float(w0[j].real), 5), round(float(w0[j].imag), 5))
        splits.setdefault(key, []).append(float(np.angle(wp[i])))
    big = sorted((sorted(v) for v in splits.values() if len(v) >= 12),
                 key=len, reverse=True)[:topk]
    sp, sizes = [], []
    for arr in big:
        a_ = np.array(arr)
        d_ = np.diff(a_)
        sp.extend((d_ / d_.mean()).tolist())
        sizes.append(len(arr))
    s = np.sort(np.array(sp))
    ks_wd = kstest(s, lambda x: 1 - np.exp(-np.pi * x * x / 4))[0]
    ks_po = kstest(s, lambda x: 1 - np.exp(-x))[0]
    return dict(n=int(len(s)), sizes=sizes,
                ks_wd=float(ks_wd), ks_poisson=float(ks_po))


def main():
    out = {"backend": "torch/cuSOLVER", "model": "U_eps=expm(i eps E)U_A"}
    rows = []
    for p in [1597, 2161, 2207, 3001]:
        r = run_prime(p, seed=7000 + p)
        r["p"] = p
        rows.append(r)
        print(f"p={p}: n={r['n']} clusters={r['sizes']} "
              f"KS_WD={r['ks_wd']:.4f} KS_Pois={r['ks_poisson']:.4f}", flush=True)
    out["exp_multi"] = rows
    r = run_prime(2207, eps=1e-3, seed=991)
    out["eps_sensitivity"] = [{"eps": 1e-3, **{k: v for k, v in r.items() if k != 'sizes'}}]
    print(f"eps=1e-3 p=2207: KS_WD={r['ks_wd']:.4f}", flush=True)
    with open(_BGS_ROOT + r"\artifacts\audit_gpu_replication.json", "w") as f:
        json.dump(out, f, indent=1)
    print("saved artifacts/audit_gpu_replication.json")


if __name__ == "__main__":
    main()
