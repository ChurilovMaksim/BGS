"""Restricted carry transfer on 6145 pair states x trailing-zero count.

State (e_{k-1}, e_k, z), z in {0,1,2,3}. Step (a,b,z) -> (b,c,z') with
letter u = a - 2b - c, |u| <= 60, (b,c) a closed-path carry state.
If u = 0 and z = 3 the step is forbidden (zero-run would reach 4).
Otherwise z' = z+1 when u = 0, and z' = 0 otherwise.

This matrix is the norm majorant of the sesquilinear carry operator:
edge (u) is weighted by a scalar W(u) >= 0. It keeps the carry (the
collision phase constraint) and the bad-run restriction. It does not keep
the phases inside the blocks T_u. Spectral radius is certified by
Collatz-Wielandt in flint balls, on a positive vector obtained by power
iteration.

Weights:
  kappa(|u|) for 1 <= |u| <= 24 are the N14 b_cp2 float table (input [N]).
  |u| > 24 is given weight 0 in the lower model (omitting edges lowers rho).
"""
from __future__ import annotations

import json
import os
import time

import numpy as np
from flint import arb, ctx
from scipy import sparse

ctx.prec = 128

ROOT = os.path.dirname(os.path.abspath(__file__))
LOGS = os.path.join(ROOT, "logs")
os.makedirs(LOGS, exist_ok=True)

# N14 logs/b_cp2_0.28.json, letterwise CP weights. Used as given floats.
KAPPA = {
    1: "0.9017067237540188",
    2: "2.062903146311669",
    3: "4.997527869010045",
    4: "10.819275975521442",
    5: "22.438031809541023",
    6: "40.26711693513123",
    7: "60.494410980824654",
    8: "73.05377672930896",
    9: "66.6678077413794",
    10: "45.12659540362299",
    11: "26.621359652122187",
    12: "40.373989772210855",
    13: "66.25689042920246",
    14: "73.11795132456507",
    15: "61.11027642617975",
    16: "42.534028178778335",
    17: "26.95234244472972",
    18: "14.82897640861532",
    19: "7.063071607701012",
    20: "2.932560521501574",
    21: "1.1005506237378673",
    22: "0.37574312253759495",
    23: "0.11844469875962228",
    24: "0.034939256443583575",
}
RHO = arb("0.28")
W0 = arb("0.28")


def closed_states():
    B = 51
    ok = lambda a, b, c: abs(a - 2 * b - c) <= 60

    def bfs(forward):
        S = {(0, 0)}
        fr = [(0, 0)]
        while fr:
            nf = []
            for x, y in fr:
                for w in range(-B, B + 1):
                    if forward and ok(x, y, w) and (y, w) not in S:
                        S.add((y, w))
                        nf.append((y, w))
                    if not forward and ok(w, x, y) and (w, x) not in S:
                        S.add((w, x))
                        nf.append((w, x))
            fr = nf
        return S

    fw, bw = bfs(True), bfs(False)
    S = fw & bw
    return sorted(S), len(fw), len(bw)


def build(states, forbid_run, weight_of):
    """weight_of(u: int) -> float. Returns csr matrix and edge list (i,j,u)."""
    idx = {s: i for i, s in enumerate(states)}
    nS = len(states)
    n = nS * 4
    rows, cols, data, letters = [], [], [], []
    for (a, b), i0 in idx.items():
        for c in range(-51, 52):
            u = a - 2 * b - c
            if abs(u) > 60 or (b, c) not in idx:
                continue
            j0 = idx[(b, c)]
            w = weight_of(u)
            if w == 0.0 and u != 0:
                # still record structural zeros? skip zero-weight off edges
                continue
            for z in range(4):
                if u == 0:
                    if forbid_run and z == 3:
                        continue
                    zp = z + 1 if z < 3 else 3
                    # if not forbid, cap at 3 so the state space stays finite
                    if not forbid_run:
                        zp = min(z + 1, 3)
                else:
                    zp = 0
                rows.append(i0 * 4 + z)
                cols.append(j0 * 4 + zp)
                data.append(w if u != 0 or w != 0.0 else weight_of(0))
                letters.append(u)
    # fix zero-letter weight: weight_of(0) may be nonzero while the branch above
    # used `w` computed before the z loop. Recompute cleanly.
    rows, cols, data, letters = [], [], [], []
    n_forbidden = 0
    for (a, b), i0 in idx.items():
        for c in range(-51, 52):
            u = a - 2 * b - c
            if abs(u) > 60 or (b, c) not in idx:
                continue
            wu = float(weight_of(u))
            if wu == 0.0:
                continue
            j0 = idx[(b, c)]
            for z in range(4):
                if u == 0 and forbid_run and z == 3:
                    n_forbidden += 1
                    continue
                zp = (min(z + 1, 3) if u == 0 else 0)
                rows.append(i0 * 4 + z)
                cols.append(j0 * 4 + zp)
                data.append(wu)
                letters.append(u)
    M = sparse.csr_matrix((np.array(data, dtype=np.float64), (rows, cols)), shape=(n, n))
    return M, n_forbidden, len(data)


def power_rho(M, iters=800):
    """L1 power iteration. Returns growth rate, vector, and Rayleigh range on x>0."""
    n = M.shape[0]
    x = np.ones(n, dtype=np.float64)
    x /= np.linalg.norm(x, 1)
    rho = 0.0
    for _ in range(iters):
        y = M.dot(x)
        rho = float(np.linalg.norm(y, 1))
        if rho == 0.0:
            return 0.0, x, 0.0, 0.0
        x = y / rho
    y = M.dot(x)
    mask = x > x.max() * 1e-15
    quot = y[mask] / x[mask]
    return rho, x, float(quot.min()), float(quot.max())


def certify(M, x, weight_scale_digits=12):
    """Collatz-Wielandt on the support x_i > 0, weights already in M as float.

    Rebuild quotients from the stored float matrix in arb. Float weights are
    treated as exact dyadic values of the constructed model (the kappa inputs
    are a separate [N] hypothesis).
    """
    n = M.shape[0]
    # v is the float64 power vector, zero below the cutoff. If (Mv)_i >= lam v_i
    # on {v_i>0}, then Mv >= lam v and rho(M) >= lam.
    cutoff = float(x.max()) * 1e-12
    pos = np.flatnonzero(x > cutoff)
    xf = [arb(float(x[i])) if x[i] > cutoff else arb(0) for i in range(n)]
    M = M.tocsr()
    indptr, indices, data = M.indptr, M.indices, M.data
    lo = None
    hi = None
    for i in pos:
        acc = arb(0)
        for k in range(indptr[i], indptr[i + 1]):
            j = int(indices[k])
            if x[j] <= cutoff:
                continue
            acc += arb(float(data[k])) * xf[j]
        q = acc / xf[i]
        if lo is None or bool(q < lo):
            lo = q
        if hi is None or bool(q > hi):
            hi = q
    return lo, hi, int(len(pos)), 0


def crit_kappa(states, forbid_run, mode):
    """Largest kappa such that rho(W) <= 0.28.

    mode 'all': every u != 0 has weight kappa, u = 0 has weight 0.28.
    mode 'v1': only |u| = 1 has weight kappa, u = 0 has weight 0.28.
    """

    def weight_of_factory(kappa):
        def weight_of(u):
            if u == 0:
                return 0.28
            if mode == "v1" and abs(u) != 1:
                return 0.0
            if mode == "all":
                return kappa
            if mode == "v1":
                return kappa
            raise RuntimeError(mode)
        return weight_of

    # float bisection
    lo, hi = 0.0, 1.0
    for _ in range(50):
        mid = 0.5 * (lo + hi)
        M, _, _ = build(states, forbid_run, weight_of_factory(mid))
        rho, x, qlo, qhi = power_rho(M, iters=300)
        if rho <= 0.28:
            lo = mid
        else:
            hi = mid
    return lo, hi


def main():
    t0 = time.time()
    states, nfw, nbw = closed_states()
    print("closed", len(states), "fw", nfw, "bw", nbw, "vertices", 4 * len(states), flush=True)
    assert len(states) == 6145

    def kappa_weight(scale):
        def weight_of(u):
            if u == 0:
                return 0.28
            a = abs(u)
            if a not in KAPPA:
                return 0.0
            return scale * float(KAPPA[a])
        return weight_of

    out = {
        "n_carry": len(states),
        "n_vertices": 4 * len(states),
        "fw": nfw,
        "bw": nbw,
        "models": [],
    }
    specs = [
        ("kappa_table_forbid", True, kappa_weight(1.0)),
        ("kappa_table_noforbid", False, kappa_weight(1.0)),
        ("half_kappa_forbid", True, kappa_weight(0.5)),
        ("tenth_kappa_forbid", True, kappa_weight(0.1)),
    ]
    for name, forbid, wfun in specs:
        M, nforb, nedges = build(states, forbid, wfun)
        rho, x, qlo, qhi = power_rho(M)
        print(name, "float rho", rho, "quot", qlo, qhi, "edges", nedges, "forb", nforb, flush=True)
        lo, hi, npos, nleak = certify(M, x)
        print("  cert", lo.str(12), hi.str(12), "support", npos, "leak", nleak, flush=True)
        above = bool(lo > RHO)
        below = bool(hi < RHO)
        out["models"].append(
            dict(
                name=name,
                forbid_zero_run=forbid,
                n_edges=nedges,
                n_forbidden_continuations=nforb,
                float_rho=rho,
                float_quot=[qlo, qhi],
                cert_lo=float(lo.lower()),
                cert_hi=float(hi.upper()),
                rho_gt_0_28=above,
                rho_lt_0_28=below,
                support=int(npos),
                leak=int(nleak),
                prefactor_C_at_0_28="infinity" if above else "finite_not_computed",
            )
        )

    for mode in ("all", "v1"):
        for forbid in (True, False):
            lo_k, hi_k = crit_kappa(states, forbid, mode)
            print("kappa*", mode, "forbid", forbid, lo_k, hi_k, flush=True)
            out.setdefault("kappa_star", []).append(
                dict(mode=mode, forbid_zero_run=forbid, kappa_rho_le_0_28=[lo_k, hi_k])
            )

    probes = []
    def probe(name, forbid, weight_of):
        M, nforb, nedges = build(states, forbid, weight_of)
        rho, x, qlo, qhi = power_rho(M, iters=400)
        lo, hi, npos, _ = certify(M, x)
        rec = dict(
            name=name,
            forbid_zero_run=forbid,
            n_edges=nedges,
            float_rho=rho,
            cert_lo=float(lo.lower()),
            cert_hi=float(hi.upper()),
            rho_gt_0_28=bool(lo > RHO),
            rho_lt_0_28=bool(hi < RHO),
            support=int(npos),
        )
        probes.append(rec)
        print("probe", name, rec["cert_lo"], rec["cert_hi"], rec["rho_gt_0_28"], rec["rho_lt_0_28"], flush=True)
    def uniform(kappa):
        def weight_of(u):
            return 0.28 if u == 0 else (kappa if u != 0 else 0.0)
        return weight_of
    for kap in ("0.003", "0.0034", "0.0035"):
        probe("uniform_"+kap, True, uniform(float(kap)))
    probe("v1_at_0.90", True, lambda u: 0.28 if u == 0 else (0.90 if abs(u) == 1 else 0.0))
    out["probes"] = probes
    out["seconds"] = time.time() - t0
    path = os.path.join(LOGS, "transfer_24580.json")
    with open(path, "w") as f:
        json.dump(out, f, indent=1)
    print("wrote", path, "in", out["seconds"], flush=True)


def is_dag(M):
    """Kahn's algorithm. True iff the support of M has no directed cycle."""
    import numpy as np
    from collections import deque

    n = M.shape[0]
    M = M.tocsr()
    indeg = np.zeros(n, dtype=np.int32)
    for i in range(n):
        indeg[M.indices[M.indptr[i] : M.indptr[i + 1]]] += 1
    q = deque(i for i in range(n) if indeg[i] == 0)
    seen = 0
    while q:
        i = q.popleft()
        seen += 1
        for k in range(M.indptr[i], M.indptr[i + 1]):
            j = int(M.indices[k])
            indeg[j] -= 1
            if indeg[j] == 0:
                q.append(j)
    return seen == n, seen, n


if __name__ == "__main__":
    main()
