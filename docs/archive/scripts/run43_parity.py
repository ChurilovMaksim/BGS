"""
run43_parity.py -- the hidden unitary symmetry, and a clean symmetry-class test.

Structural point (analytic, then verified here):

  * -I is central in SL(2,Z), so the quantised parity Pi = U_{-I} commutes with
    U_A for EVERY A.  Pi T(n) Pi^dagger = T(-n), hence for V = sum_n c_n T(n)
    (Hermitian, c_{-n} = conj(c_n)):

        [Pi, V] = 0   <=>   c_{-n} = c_n   <=>   all c_n REAL
                      <=>   the classical symbol is EVEN, f(-theta) = f(theta).

  * If A^k = +I mod N (sign = +1, K = k) then Pi is NOT a power of U_A, so Pi
    acts on each multiplet H_lam with both eigenvalues +-1 and SPLITS it into
    two independent sectors.  A real (even) observable therefore produces a
    SUPERPOSITION of two independent spectra inside every multiplet, which
    fakes a lower level-repulsion exponent.  If A^k = -I mod N (sign = -1,
    K = 2k) then Pi acts on H_lam as a scalar and there is no splitting.

  Every earlier run of this project used real coefficients (e.g. run29:
  V = T10 + T10^* + 0.7(T01 + T01^*)), so this systematic was present in all
  previous GOE/GUE readings.

Protocol here: unfolding-free consecutive-spacing ratios rtilde (Atas et al.),
per multiplet and per parity sector, with GOE/GUE/Poisson controls AND
"superposition of two independent GOE/GUE spectra" controls.
"""
import json
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bgs_core as bc                                            # noqa: E402
from run42_esd import rtilde                                     # noqa: E402

ART = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "artifacts")
REF = dict(poisson=0.38629, goe=0.53590, gue=0.59946)


def close_labels(freqs, mats, N):
    """Smallest label set containing freqs and closed under the matrices."""
    labs = set()
    stack = [(int(a) % N, int(b) % N) for a, b in freqs]
    while stack:
        cur = stack.pop()
        if cur in labs:
            continue
        labs.add(cur)
        v = np.array(cur, dtype=np.int64)
        for Mt in mats:
            w = (Mt @ v) % N
            stack.append((int(w[0]) % N, int(w[1]) % N))
    return sorted(labs)


def build_coeffs(labels, N, rng, gens):
    """Assign coefficients c_n subject to constraints c_{g n} = conj(c_n)^{e_g}.

    `gens` is a list of (2x2 integer matrix, conj_flag).  Hermiticity
    (c_{-n} = conj(c_n)) must be supplied by the caller as (-I, True).
    Returns dict label -> complex.
    """
    labels = list(labels)
    idx = {lab: i for i, lab in enumerate(labels)}
    val = {}
    seen_flag = {}
    for root in labels:
        if root in val:
            continue
        # BFS over the group orbit, tracking the conjugation parity
        comp = {root: False}
        stack = [root]
        conflict = False
        while stack:
            cur = stack.pop()
            f = comp[cur]
            v = np.array(cur, dtype=np.int64)
            for Mt, cf in gens:
                w = tuple(int(t) % N for t in (Mt @ v) % N)
                if w not in idx:
                    continue
                nf = f ^ bool(cf)
                if w in comp:
                    if comp[w] != nf:
                        conflict = True
                else:
                    comp[w] = nf
                    stack.append(w)
        c = complex(rng.standard_normal(), 0.0) if conflict else complex(
            rng.standard_normal(), rng.standard_normal()) / math.sqrt(2)
        for lab, f in comp.items():
            val[lab] = np.conj(c) if f else c
        seen_flag[root] = conflict
    return val


def parity_sectors(Pi, B, tol=1e-8):
    """Split the multiplet basis B into eigenspaces of the parity operator."""
    P = B.conj().T @ (Pi @ B)
    P = 0.5 * (P + P.conj().T)                  # Pi is Hermitian involution
    ev, W = np.linalg.eigh(P)
    plus = W[:, ev > 0]
    minus = W[:, ev < 0]
    return P, ev, plus, minus


def superposition_control(sizes, kind, seed=5, reps=2):
    """rtilde for the union of TWO independent spectra of size m/2 each."""
    rng = np.random.default_rng(seed)
    acc = []
    for _ in range(reps):
        for m in sizes:
            halves = []
            for h in (m // 2, m - m // 2):
                if h < 4:
                    continue
                if kind == "goe":
                    G = rng.standard_normal((h, h))
                    H = (G + G.T) / math.sqrt(2)
                else:
                    G = (rng.standard_normal((h, h)) +
                         1j * rng.standard_normal((h, h))) / math.sqrt(2)
                    H = (G + G.conj().T) / math.sqrt(2)
                halves.append(np.linalg.eigvalsh(H))
            if len(halves) == 2:
                acc.append(rtilde(np.sort(np.concatenate(halves))))
    rr = np.concatenate([a for a in acc if len(a)])
    return float(rr.mean()), int(len(rr))


def plain_control(sizes, kind, seed=6, reps=2):
    rng = np.random.default_rng(seed)
    acc = []
    for _ in range(reps):
        for m in sizes:
            if kind == "goe":
                G = rng.standard_normal((m, m))
                H = (G + G.T) / math.sqrt(2)
                ev = np.linalg.eigvalsh(H)
            elif kind == "gue":
                G = (rng.standard_normal((m, m)) +
                     1j * rng.standard_normal((m, m))) / math.sqrt(2)
                H = (G + G.conj().T) / math.sqrt(2)
                ev = np.linalg.eigvalsh(H)
            else:
                ev = np.sort(rng.random(m))
            acc.append(rtilde(ev))
    rr = np.concatenate([a for a in acc if len(a)])
    return float(rr.mean()), int(len(rr))


FREQS = [(1, 0), (0, 1), (1, 1), (1, -1), (2, 0), (0, 2)]


def analyse(A, N, seed=3, verbose=True):
    U = bc.U_cat(A, N)
    k, sign, K = bc.mat_order(A, N)
    chi, tres = bc.torsion_certificate(U, K)
    Pi = bc.parity_operator(N).astype(complex)
    AT = np.array([[A[0], A[2]], [A[1], A[3]]], dtype=np.int64)
    Rs = bc.reversing_involution(A)
    R = Rs[0]
    RT = np.array([[R[0], R[2]], [R[1], R[3]]], dtype=np.int64)
    negI = -np.eye(2, dtype=np.int64)
    Rs = [Rx for Rx in Rs if (-int(Rx[2])) % N != 0]     # need gcd(c,N)=1 for U_M
    R = Rs[0]
    RT = np.array([[R[0], R[2]], [R[1], R[3]]], dtype=np.int64)
    UM, M = bc.theta_operator(A, N, R)

    labels = close_labels(FREQS, [RT, negI], N)
    out = dict(A=list(A), N=N, k=k, sign=int(sign), K=K, n_labels=len(labels),
               torsion_res=tres, R=list(R), M=list(M), n_involutions=len(Rs))

    # Pi commutes with U_A exactly, and is it a scalar on multiplets?
    out["pi_commutator_U"] = float(np.max(np.abs(Pi @ U - U @ Pi)))

    modes = {
        # (theta-invariant?, parity-invariant?)
        "sym_par":  (True, True),
        "sym_nopar": (True, False),
        "gen_par":  (False, True),
        "gen_nopar": (False, False),
    }
    res = {}
    for name, (thinv, parinv) in modes.items():
        rng = np.random.default_rng(seed)
        gens = [(negI, True)]                       # Hermiticity
        if thinv:
            gens.append((RT, True))
        if parinv:
            gens.append((negI, False))
        coeffs = build_coeffs(labels, N, rng, gens)
        Id = np.eye(N, dtype=complex)
        V = bc.weyl_sum_operator(coeffs, N, Id)
        herm = float(np.max(np.abs(V - V.conj().T)))
        th_dev = float(np.max(np.abs(bc.theta_conjugate(UM, V) - V)))
        pi_dev = float(np.max(np.abs(Pi @ V - V @ Pi)))
        best_th = min(float(np.max(np.abs(
            bc.theta_conjugate(bc.theta_operator(A, N, Rx)[0], V) - V)))
            for Rx in Rs)
        levels_all, r_all, r_plus, r_minus = [], [], [], []
        sector_dims = []
        for s in range(K):
            lam, B, m, cert = bc.multiplet_basis(U, K, chi, s, seed=seed)
            Pmat, pev, plus, minus = parity_sectors(Pi, B)
            sector_dims.append((int(plus.shape[1]), int(minus.shape[1])))
            VL = B.conj().T @ bc.weyl_sum_operator(coeffs, N, B)
            VL = 0.5 * (VL + VL.conj().T)
            ev = np.linalg.eigvalsh(VL)
            levels_all.append(ev)
            r_all.append(rtilde(ev))
            for Q, bucket in ((plus, r_plus), (minus, r_minus)):
                if Q.shape[1] >= 6:
                    Vs = Q.conj().T @ VL @ Q
                    Vs = 0.5 * (Vs + Vs.conj().T)
                    bucket.append(rtilde(np.linalg.eigvalsh(Vs)))

        def agg(bucket):
            if not bucket:
                return None
            rr = np.concatenate([b for b in bucket if len(b)])
            return dict(mean=float(rr.mean()), n=int(len(rr)),
                        sem=float(rr.std(ddof=1) / math.sqrt(len(rr))))
        res[name] = dict(herm_res=herm, theta_dev=th_dev, theta_dev_best=best_th,
                         parity_dev=pi_dev, sector_dims=sector_dims[:3],
                         whole=agg(r_all), plus=agg(r_plus), minus=agg(r_minus))
    out["modes"] = res
    sizes = [int(round(N / K))] * K
    half = [max(6, int(round(N / K / 2)))] * K
    out["controls"] = dict(
        goe=plain_control(sizes, "goe"), gue=plain_control(sizes, "gue"),
        poisson=plain_control(sizes, "poisson"),
        goe_half=plain_control(half, "goe"), gue_half=plain_control(half, "gue"),
        superpos_goe=superposition_control(sizes, "goe"),
        superpos_gue=superposition_control(sizes, "gue"))
    return out


def main():
    configs = [((2, 1, 1, 1), 521), ((2, 1, 1, 1), 2207), ((2, 1, 1, 1), 1597)]
    rows = []
    for A, N in configs:
        out = analyse(A, N)
        rows.append(out)
        print(f"\n===== A={A} N={N} k={out['k']} sign={out['sign']} K={out['K']} "
              f"labels={out['n_labels']} =====")
        print(f"  [Pi,U] = {out['pi_commutator_U']:.2e}   "
              f"parity sector dims (first 3 multiplets): "
              f"{out['modes']['gen_par']['sector_dims']}")
        c = out["controls"]
        print(f"  controls: GOE {c['goe'][0]:.4f}  GUE {c['gue'][0]:.4f}  "
              f"Poisson {c['poisson'][0]:.4f} | half-size GOE {c['goe_half'][0]:.4f} "
              f"GUE {c['gue_half'][0]:.4f} | superpos GOE {c['superpos_goe'][0]:.4f} "
              f"GUE {c['superpos_gue'][0]:.4f}")
        for name, d in out["modes"].items():
            w = d["whole"]
            pl = d["plus"]
            mi = d["minus"]
            print(f"  {name:>10}  theta_dev {d['theta_dev']:.1e} "
                  f"(best over R: {d['theta_dev_best']:.1e})  "
                  f"parity_dev {d['parity_dev']:.1e}")
            print(f"             whole <r> = {w['mean']:.4f} +- {w['sem']:.4f} "
                  f"(n={w['n']})" +
                  (f"   sectors + {pl['mean']:.4f} +- {pl['sem']:.4f} "
                   f"(n={pl['n']})" if pl else "") +
                  (f"   - {mi['mean']:.4f} +- {mi['sem']:.4f} (n={mi['n']})"
                   if mi else ""))
    os.makedirs(ART, exist_ok=True)
    with open(os.path.join(ART, "run43_parity.json"), "w") as f:
        json.dump(rows, f, indent=1, default=float)
    print("\nwrote artifacts/run43_parity.json")


if __name__ == "__main__":
    main()



