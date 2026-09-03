"""
RUN 6 / M1 at r=5 -- clean implementation (supersedes m1_new_configs.py).

s_of_j5 returns the RAW resonant sum times t0ph; the identity applied by
the driver is

    Tr(Vbar^5 P_lam) = (N/K) a_5 + (1/K) sum_{J>=1} lam^{-J} S_J,
    S_J := raw_sum / K^5,

i.e. per-J contribution lam^{-J} * raw / K^6.  History of the three bugs
this fixes (all documented in review/run5_debug/):
  B1 missing zeta^{rho/N} phase conversion (raw exponents fed as phases);
  B2 flat rho index built from separately reduced components (no carry);
  B3 missing projector normalisation Pl /= K and missing final 1/K.
"""
import json, math, os, sys, time, itertools
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from catmap_core import ord_pm
import master_formula as MF

ART = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "artifacts")


def s_of_j5(gg, CO, SPH, PSI, rho, t0ph):
    """RAW order-5 resonant sum x t0ph (caller divides by K^5)."""
    Ndim = rho.shape[1]
    n = len(CO)
    W = (CO[:, None] * CO[None, :]
         * np.exp(1j * np.pi * ((SPH[:, None] + SPH[None, :] + PSI)
                                % (2 * Ndim)) / Ndim))
    gx = (gg[:, None, 0] + gg[None, :, 0]) % Ndim          # [n,n]
    gy = (gg[:, None, 1] + gg[None, :, 1]) % Ndim
    Wf = W.ravel()
    rhof = rho.ravel()
    kap = (Ndim + 1) % (2 * Ndim)
    gi1 = gg[:, 0].astype(np.int64)
    gi2 = gg[:, 1].astype(np.int64)
    tot = 0.0 + 0j
    for (a, b, c) in itertools.product(range(n), repeat=3):
        uP = (gg[a] + gg[b] + gg[c]) % Ndim
        phP = int(SPH[a] + SPH[b] + SPH[c]
                  + PSI[a, b] + PSI[a, c] + PSI[b, c])
        baseW = (complex(CO[a]) * complex(CO[b]) * complex(CO[c])
                 * np.exp(1j * np.pi * (phP % (2 * Ndim)) / Ndim))
        cross = np.exp(1j * np.pi * ((kap * (int(uP[1]) * gi1
                                             - int(uP[0]) * gi2))
                                     % (2 * Ndim)) / Ndim)
        qq = np.outer(cross, cross).ravel()
        us1 = (gx + int(uP[0])) % Ndim
        us2 = (gy + int(uP[1])) % Ndim
        rvz = np.exp(1j * np.pi * rhof[(us1 * Ndim + us2).ravel()] / Ndim)
        tot += baseW * np.dot(Wf * qq, rvz)
    return complex(tot * t0ph)


def run_config(A, N, note="", F=((1, 0),), seed=1):
    t0 = time.time()
    k, sg = ord_pm(A, N)
    assert k > 0
    K = k if sg > 0 else 2 * k
    info, Bm, SIG, U = MF.cocycle(A, N, K)
    RH, unimod = MF.rho_tables(N, K, U)
    ok_struct = bool(info["fit_err"] < 1e-9 and info["tele_err"] < 1e-9
                     and unimod)
    print(f"[{'PASS' if ok_struct else 'FAIL'}] structure A={A} N={N} K={K}",
          flush=True)
    rng = np.random.default_rng(seed)
    cs = {nn: (rng.normal() + 1j * rng.normal()) / math.sqrt(2) for nn in F}
    V = np.zeros((N, N), dtype=complex)
    for nn, cc in cs.items():
        V += cc * MF.weyl_matrix(nn[0] % N, nn[1] % N, N)
        V += np.conj(cc) * MF.weyl_matrix((-nn[0]) % N, (-nn[1]) % N, N)
    Xv, Vbar = V.copy(), np.zeros_like(V)
    for _ in range(K):
        Vbar += Xv
        Xv = U @ Xv @ U.conj().T
    Vbar /= K
    a_r = float(np.real(np.trace(np.linalg.matrix_power(Vbar, 5)))) / N

    terms = []
    for nn, cc in cs.items():
        terms.append((cc, +1, np.array(nn, dtype=np.int64) % N))
        terms.append((np.conj(cc), -1, np.array(nn, dtype=np.int64) % N))
    L = len(terms)
    G = np.empty((L, K, 2), dtype=np.int64)
    CO = np.empty(L * K, dtype=complex)
    SPH = np.empty(L * K)
    for si, (cf, ep, nv) in enumerate(terms):
        cur = nv.copy()
        for j in range(K):
            G[si, j] = (ep * cur) % N
            CO[si * K + j] = cf
            SPH[si * K + j] = ep * SIG[j][nv[0], nv[1]]
            cur = Bm @ cur % N
    n = L * K
    gg = G.reshape(n, 2)
    PSI = ((N + 1) * (gg[:, 1][:, None] * gg[:, 0][None, :]
                      - gg[:, 0][:, None] * gg[:, 1][None, :])) % (2 * N)

    UK = np.linalg.matrix_power(U, K)
    lam0 = (np.trace(UK) / N) ** (1.0 / K)
    rows = []
    for jj in (0, 1, 2):
        lam = lam0 * np.exp(2j * np.pi * jj / K)
        rhs = (N / K) * a_r
        Pl = np.zeros_like(U)
        Uj = np.eye(N, dtype=complex)
        for j in range(K):
            Pl += (lam ** (-j)) * Uj
            Uj = U @ Uj
        Pl /= K
        for J in range(1, K):
            UJ = np.linalg.matrix_power(U, J)
            tr = np.trace(UJ)
            t0ph = tr / abs(tr)
            raw = s_of_j5(gg, CO, SPH, PSI, RH[J], t0ph)
            rhs += (lam ** (-J)) * raw / (K ** 6)
        lhs = float(np.real(np.trace(np.linalg.matrix_power(Vbar, 5) @ Pl)))
        err = abs(lhs - float(np.real(rhs)))
        rows.append(dict(lam_idx=jj, lhs=lhs,
                         rhs_re=float(np.real(rhs)), err=err))
        print(f"   lam#{jj}: lhs={lhs:.8f} rhs={float(np.real(rhs)):.8f} "
              f"|err|={err:.2e}", flush=True)
    ok = bool(all(rr["err"] < 1e-9 * max(1.0, abs(rr["lhs"])) for rr in rows))
    print(f"[{'PASS' if ok else 'FAIL'}] master r=5 A={A} N={N} {note} "
          f"({time.time()-t0:.0f}s)", flush=True)
    return dict(A=A, N=N, note=note, K=K, passed=bool(ok), rows=rows)


def main():
    p = os.path.join(ART, "m1_run5.json")
    try:
        store = json.load(open(p))
    except Exception:
        store = {}
    store["implementation"] = "src/m1_r5.py"
    if not isinstance(store.get("rows"), dict):
        store["rows"] = {}          # legacy list format -> dict
    allpass = True
    for (A, N, note) in (
        ([7, 3, 2, 1], 71, "tr8 split K=5"),
        ([2, 1, 1, 1], 233, "arnold inert(p%5=3)"),
        ([2, 1, 1, 1], 101, "arnold split"),
    ):
        r = run_config(A, N, note)
        allpass &= r["passed"]
        key = f"{A}_{N}"
        store.setdefault("rows", {})
        store["rows"][key] = r
        json.dump(store, open(p, "w"), indent=1)   # incremental save
    store["all_pass"] = bool(allpass)
    json.dump(store, open(p, "w"), indent=1)
    print("saved artifacts/m1_run5.json")
    sys.exit(0 if allpass else 1)


if __name__ == "__main__":
    main()
