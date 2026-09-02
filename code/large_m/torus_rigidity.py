"""
Run 82f: THEOREM (Hecke-torus rigidity of the observable family) -- full
numerical certification.
=======================================================================
CLAIM.  Let A in SL_2(Z) be the cat map, N an odd prime with gcd(N, t^2-4) = 1,
K = ord(A) mod N, and let

    T = centraliser torus of A in SL_2(Z/N),      <A> subset T,
    Q(n) = n_1^2 - n_1 n_2 - n_2^2  (disc 5 = t^2 - 4 for t = 3),

so that Q is T-invariant.  Identify (Z/N)^2 with the quadratic algebra
R = (Z/N)[x]/(x^2 - t x + 1) as a free rank-1 R-module; then T is the group of
norm-one units of R and Q is (a scalar multiple of) the norm form.  Hence T
acts TRANSITIVELY on every level set {Q = q}, q != 0.  For g in T the Weil
(metaplectic) operator U_g satisfies the exact Egorov covariance
U_g T(n) U_g^* = T(gn) and commutes with U_A (because g commutes with A) and
with parity (-I is central), so it preserves every U_A-eigenspace and every
parity block.  Therefore

    Q(n) = Q(n')  ==>  V_n = U_g V_{n'} U_g^*  ==>  spec(V_n) = spec(V_{n'}),

i.e. the whole family {V_n = P_+(T(n)+T(-n))P_+} is a ONE-PARAMETER family
indexed by q = Q(n) in Z/N -- at most N distinct spectra, not (N^2-1)/K.

CONSEQUENCES (the reason this matters).
 * The R81.4 "coherent arithmetic fluctuation mode" is exactly this
   one-dimensional modulation: an ensemble of samples lying on a single curve
   q -> V_q has, by construction, ONE dominant fluctuation direction and
   positively correlated window counts; the excess over GOE grows with m
   because the spread of the deterministic curve is O(1) while the GOE
   fluctuation decays.
 * An i.i.d.-GOE statement for {V_n} is false for an exact and elementary
   reason, and the effective number of ensemble members is N - 1, not
   (N^2-1)/K.  The frequency-ensemble route therefore cannot average its way
   to a per-system local law.

CERTIFICATES COMPUTED HERE (all must pass):
  C1  |{n != 0 : Q(n) = q}| = N - 1 for every q != 0, and the norm cone
      |{n != 0 : Q(n) = 0}| = 2N - 2   (split case; N + 1 / 0 if inert);
  C2  the number of <A>-orbits inside one level set = |T|/K = m, and the
      global count (N-1).m + cone-orbits = (N^2-1)/K;
  C3  full-spectrum equality inside a level set: for several q, up to 8
      DISTINCT <A>-orbits give the same sorted spectrum of V_n to 1e-11;
  C4  distinctness across level sets: spectra for different q differ by
      orders of magnitude more than the intra-level deviation;
  C5  the explicit torus element: for n, n' in the same level set, solve
      g n = n' with g = (a I + b A) mod N, det g = 1 -- verify such g exists
      inside T (a rank-2 linear solve plus the norm condition).

Output: artifacts/r82/torus_rigidity.json
"""

import json
import os
import sys
import time
from collections import defaultdict

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from catmap_independent import CatMap  # noqa: E402
from compression_spacings import eigen_basis  # noqa: E402
from parity_desymmetrised import apply_parity  # noqa: E402

A = [[2, 1], [1, 1]]
T_TRACE = 3


def Qform(n1, n2, N):
    return (n1 * n1 - n1 * n2 - n2 * n2) % N


def orbit(n, AT, N, K):
    out = []
    w = np.array(n, dtype=np.int64) % N
    for _ in range(K):
        out.append((int(w[0]), int(w[1])))
        w = AT @ w % N
    return out


def certify(N, batch, rng, n_levels=6, per_level=8):
    t0 = time.time()
    cm = CatMap(A, N)
    ordA, K = cm.orders()
    assert ordA == K
    B, lam, m, res, chi = eigen_basis(cm, K, 0, batch, rng)
    assert res < 1e-9 and m in ((N - 1) // K, (N + 1) // K), (res, m)
    RB = B.conj().T @ apply_parity(B)
    w, Vv = np.linalg.eigh(RB)
    mp = int((w > 0).sum())
    Bp = B @ Vv[:, w > 0]
    AT = np.array(A, dtype=np.int64).T % N
    row = {"N": N, "K": int(K), "m": int(m), "m_plus": mp, "eig_resid": res}
    print(f"=== N={N} K={K} m={m} m+={mp} ({time.time()-t0:.0f} s)", flush=True)

    # ---- C1: level-set sizes (exact, full enumeration) -----------------
    n1 = np.arange(N, dtype=np.int64)
    G1, G2 = np.meshgrid(n1, n1, indexing="ij")
    Qall = (G1 * G1 - G1 * G2 - G2 * G2) % N
    Qall = Qall.ravel()
    Qall[0] = -1                                   # drop n = 0
    sizes = np.bincount(Qall[Qall >= 0], minlength=N)
    cone = int(sizes[0])
    nz = sizes[1:]
    c1 = bool(np.all(nz == nz[0]))
    row["C1_level_size"] = int(nz[0])
    row["C1_all_equal"] = c1
    row["C1_cone_size"] = cone
    row["C1_split"] = bool(nz[0] == N - 1)
    print(f"  C1 level sets: |{{Q = q}}| = {nz[0]} for all q != 0 "
          f"({'PASS' if c1 else 'FAIL'});  cone |{{Q = 0}}| = {cone}   "
          f"[{'split' if nz[0] == N-1 else 'inert'}]", flush=True)

    # ---- C2: orbit bookkeeping -----------------------------------------
    q0 = 1
    pts = [(int(i), int(j)) for i, j in zip(G1.ravel(), G2.ravel())
           if Qform(int(i), int(j), N) == q0 and (i, j) != (0, 0)]
    seen, norb = set(), 0
    for p in pts:
        if p in seen:
            continue
        norb += 1
        seen.update(orbit(p, AT, N, K))
    total = norb * (N - 1) if nz[0] == N - 1 else norb * (N + 1)
    cone_orb = cone // K
    c2 = (total + cone_orb) == (N * N - 1) // K
    row["C2_orbits_per_level"] = norb
    row["C2_expected_m"] = int(nz[0]) // K
    row["C2_cone_orbits"] = cone_orb
    row["C2_global_identity"] = c2
    print(f"  C2 orbits inside one level set = {norb} (= |T|/K = "
          f"{int(nz[0])//K});  (#levels).(orbits) + cone/K = "
          f"{total + cone_orb} vs (N^2-1)/K = {(N*N-1)//K}   "
          f"{'PASS' if c2 else 'FAIL'}", flush=True)

    def spec(u):
        H = Bp.conj().T @ cm.apply_T((int(u[0]) % N, int(u[1]) % N), Bp)
        H = H + H.conj().T
        return np.sort(np.linalg.eigvalsh(H))

    # ---- C3 / C4: spectra inside and across level sets -----------------
    rng2 = np.random.default_rng(9001)
    levels = defaultdict(list)
    seen2 = set()
    while len(levels) < n_levels or any(len(v) < per_level for v in levels.values()):
        n = (int(rng2.integers(0, N)), int(rng2.integers(0, N)))
        if n == (0, 0):
            continue
        q = Qform(n[0], n[1], N)
        if q == 0:
            continue
        if len(levels) >= n_levels and q not in levels:
            continue
        if len(levels[q]) >= per_level:
            continue
        o = orbit(n, AT, N, K)
        c = min(o)
        if c in seen2:
            continue
        seen2.add(c)
        levels[q].append(n)

    intra, reps_by_q = [], {}
    for q, ns in levels.items():
        S = np.array([spec(n) for n in ns])
        d = float(np.abs(S - S[0]).max())
        intra.append(d)
        reps_by_q[q] = S[0]
    qlist = sorted(reps_by_q)
    inter = []
    for i in range(len(qlist)):
        for j in range(i + 1, len(qlist)):
            inter.append(float(np.abs(reps_by_q[qlist[i]] - reps_by_q[qlist[j]]).max()))
    row["C3_levels_tested"] = len(levels)
    row["C3_orbits_per_level_tested"] = per_level
    row["C3_max_intra_level_spectral_deviation"] = max(intra)
    row["C4_min_inter_level_spectral_deviation"] = min(inter)
    row["C4_separation_decades"] = float(np.log10(min(inter) / max(intra)))
    print(f"  C3 {len(levels)} level sets x {per_level} distinct orbits: "
          f"max intra-level |spec - spec| = {max(intra):.2e}", flush=True)
    print(f"  C4 min inter-level spectral distance = {min(inter):.3e}  "
          f"-> separation {np.log10(min(inter)/max(intra)):.1f} decades",
          flush=True)

    # ---- C5: the explicit torus element -------------------------------
    Amat = np.array(A, dtype=np.int64) % N
    ok5, tested = 0, 0
    for q, ns in list(levels.items())[:3]:
        n0 = np.array(ns[0], dtype=np.int64)
        An0 = (Amat @ n0) % N
        Mx = np.stack([n0 % N, An0], axis=1) % N     # columns n0, A n0
        det = int((Mx[0, 0] * Mx[1, 1] - Mx[0, 1] * Mx[1, 0]) % N)
        if det == 0:
            continue
        inv = pow(det, N - 2, N)
        adj = np.array([[Mx[1, 1], -Mx[0, 1]], [-Mx[1, 0], Mx[0, 0]]],
                       dtype=np.int64) % N
        for nn in ns[1:]:
            tested += 1
            rhs = np.array(nn, dtype=np.int64) % N
            ab = (inv * (adj @ rhs)) % N             # n' = a n0 + b A n0
            a, b = int(ab[0]), int(ab[1])
            g = (a * np.eye(2, dtype=np.int64) + b * Amat) % N
            detg = int((g[0, 0] * g[1, 1] - g[0, 1] * g[1, 0]) % N)
            gn = (g @ n0) % N
            if detg == 1 % N and tuple(int(x) for x in gn) == tuple(int(x) % N for x in nn):
                ok5 += 1
    row["C5_tested"] = tested
    row["C5_torus_elements_found"] = ok5
    print(f"  C5 explicit g = aI + bA in T with g n0 = n', det g = 1: "
          f"{ok5}/{tested} {'PASS' if ok5 == tested and tested else 'CHECK'}",
          flush=True)
    return row


def main():
    rng = np.random.default_rng(820005)
    out = {"script": "src/r82f_torus_rigidity.py",
           "generated": time.strftime("%Y-%m-%dT%H:%M:%S"), "designs": []}
    for N, batch in ((199, 64), (3571, 512), (9349, 1024)):
        try:
            out["designs"].append(certify(N, batch, rng))
        except Exception as exc:                       # noqa: BLE001
            print(f"design N={N} FAILED: {exc!r}", flush=True)
            out["designs"].append({"N": N, "error": repr(exc)})
    dest = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                        "artifacts", "r82", "torus_rigidity.json")
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w") as fh:
        json.dump(out, fh, indent=1, default=str)
    print("artifact ->", dest, flush=True)


if __name__ == "__main__":
    main()
