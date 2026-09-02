"""
Run 82v: THE BRANCH STRUCTURE AT A THIRD DESIGN (referee D1 follow-up).
=======================================================================
Predictions (from the two-design analysis, LEDGER R82.22):
  C1  the two (k0, c) branches satisfy  c1 * c2 = -(t^2 - 4)  (mod N);
  C2  c1 = L_{(K-1)/2} mod N, the half-index Lucas trace of A
      (L_j: L_0 = 2, L_1 = 3, L_j = 3 L_{j-1} - L_{j-2}).
At (N,K) = (199,11): c = (123, 76), L_5 = 123;  at (3571,17): c = (2207,1364),
L_8 = 2207.  Both verified.  Here the THIRD design (19489, 29):

      prediction:  c1 = L_14 mod 19489,  c2 = -5/c1 mod 19489.

Method: the pipeline q-curve (mu_4 per level set) at 8 probe values; the
closed-form model at candidate (k0, c) for k0 in {1, -1 mod K} and
c in {L_14, -5/L_14}; a branch is confirmed if all 8 probes match.

Output: artifacts/r82/branch_third_design.json
"""

import json
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from catmap_independent import CatMap  # noqa: E402
from compression_spacings import eigen_basis  # noqa: E402
from parity_desymmetrised import apply_parity  # noqa: E402
from r82k_bgs_large_m import design_params, build_M  # noqa: E402
from r82j_closed_form import primitive_root  # noqa: E402

A = [[2, 1], [1, 1]]


def lucas_mod(N, count):
    L = [2 % N, 3 % N]
    for _ in range(count):
        L.append((3 * L[-1] - L[-2]) % N)
    return L


def main():
    N, K = 95419, 57          # chi = -i != 1: branch 0 is clean (no zero mode)
    inv = lambda z: pow(int(z) % N, N - 2, N)                    # noqa: E731
    L = lucas_mod(N, K)
    c_pred = L[(K - 1) // 2]
    c2_pred = (-5) * inv(c_pred) % N
    print(f"=== third design N={N} K={K} m+={(N-1)//(2*K)}", flush=True)
    print(f"  C2 prediction: c1 = L_{(K-1)//2} = {c_pred}", flush=True)
    print(f"  C1 prediction: c2 = -5/c1 = {c2_pred}", flush=True)

    rng = np.random.default_rng(820019)
    cm = CatMap(A, N)
    ordA, Kc = cm.orders()
    assert ordA == K == Kc
    B, lam, m, res, chi = eigen_basis(cm, K, 0, 4096, rng)
    assert res < 1e-9 and m == (N - 1) // K, (res, m)
    RB = B.conj().T @ apply_parity(B)
    w, Vv = np.linalg.eigh(RB)
    mp = int((w > 0).sum())
    Bp = B @ Vv[:, w > 0]
    print(f"  pipeline eigenspace built: m={m}, m+={mp}, resid={res:.1e}",
          flush=True)

    def pipeline_mu4(u):
        H = Bp.conj().T @ cm.apply_T((int(u[0]) % N, int(u[1]) % N), Bp)
        H = H + H.conj().T
        ev = np.linalg.eigvalsh(H)
        e = ev - ev.mean()
        e = e / np.sqrt((e ** 2).mean())
        return float((e ** 4).mean())

    def Q(a, b):
        return (a * a - a * b - b * b) % N

    probes = []
    while len(probes) < 8:
        n = (int(rng.integers(0, N)), int(rng.integers(0, N)))
        q = Q(*n)
        if q and all(q != p[0] for p in probes):
            probes.append((q, n))
    meas = {}
    for q, n in probes:
        meas[q] = pipeline_mu4(n)
    print(f"  pipeline probes: {[(q, round(v,4)) for q, v in meas]}",
          flush=True)

    # the model: for each (k0, parity-even) block, compare against q' = c^-1 q
    g = primitive_root(N)
    dlog = np.zeros(N, dtype=np.int64)
    x = 1
    for s in range(N - 1):
        dlog[x] = s
        x = x * g % N
    ks_all = np.array([k for k in range(N - 1) if k % K == 1 and k % 2 == 0],
                      dtype=np.int64)
    assert len(ks_all) == (N - 1) // (2 * K)

    def model_mu4(qp, k0):
        ks = (ks_all + (k0 - 1)) % (N - 1)
        assert len(ks) == len(ks_all)
        J = np.zeros((len(ks), len(ks)), dtype=complex)
        xs = np.arange(2, N, dtype=np.int64)
        for s in range(0, len(xs), 16384):
            xb = xs[s:s + 16384]
            W = np.exp(-2j * np.pi * np.outer(ks, dlog[xb]) / (N - 1)) * \
                np.exp(2j * np.pi * (qp * xb % N) / N)
            Vv = np.exp(2j * np.pi * np.outer(ks, dlog[(xb - 1) % N]) / (N - 1))
            J += W @ Vv.T
        C = np.exp(-2j * np.pi * (pow(2, N - 2, N) * qp % N) / N) * J / (N - 1)
        M = C + C.conj().T
        ev = np.linalg.eigvalsh(M)
        e = ev - ev.mean()
        e = e / np.sqrt((e ** 2).mean())
        return float((e ** 4).mean())

    out = {"script": "src/r82v_branch_third.py", "N": N, "K": K,
           "c1_pred": int(c_pred), "c2_pred": int(c2_pred), "branches": []}
    inv_c1 = inv(c_pred)
    inv_c2 = inv(c2_pred)
    for k0 in (0, K - 1):          # k0 = 1 and k0 = -1 mod K  (0-indexed shift)
        for cname, cinv in ((f"L_half={c_pred}", inv_c1),
                            (f"-5/c={c2_pred}", inv_c2)):
            devs = []
            for q, _ in probes:
                mv = model_mu4((cinv * q) % N, k0)
                devs.append(abs(mv - meas[q]))
            ok = max(devs) < 1e-9
            out["branches"].append({"k0": int(k0), "c_name": cname,
                                    "max_dev": float(max(devs)), "match": ok})
            print(f"  branch (k0={k0} {'(=1 mod K)' if k0==0 else '(=-1 mod K)'}, "
                  f"{cname}): max |model - pipeline| over 8 probes = "
                  f"{max(devs):.2e}  -> {'MATCH' if ok else 'no'}", flush=True)
    ok1 = any(b["match"] and b["c_name"] == f"L_half={c_pred}"
              for b in out["branches"])
    ok2 = any(b["match"] and b["c_name"] == f"-5/c={c2_pred}"
              for b in out["branches"])
    out["C1_confirmed"] = ok2
    out["C2_confirmed"] = ok1
    print(f"  C1 (c1*c2 = -(t^2-4)) confirmed at third design: {ok2}", flush=True)
    print(f"  C2 (c1 = L_(K-1)/2) confirmed at third design:     {ok1}", flush=True)
    dest = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                        "artifacts", "r82", "branch_third_design.json")
    with open(dest, "w") as fh:
        json.dump(out, fh, indent=1, default=str)
    print("artifact ->", dest, flush=True)


if __name__ == "__main__":
    main()
